# -*- coding: utf-8 -*-
"""เพิ่ม "กลไกการเกิดโรคแบบภาพเคลื่อนไหว" + "หลักจำ" ให้หน้า MED421 learn

    python3 patch_learn_anim.py page <learn index.html ที่ดาวน์โหลด> <out.html>
    python3 patch_learn_anim.py data <โฟลเดอร์ data ของ learn> <โฟลเดอร์ anim/*.json> <โฟลเดอร์ data ออก>

ข้อมูลใน section (data/<ชุด>.json):
  anims = {key: {title, svg, steps:[{t, cap, ms?}]}}  · md มี [[anim:key]] ตรงจุดที่จะแสดง
  mnem  = [{name, what, lines:[[ตัวอักษร/คำ, ความหมาย], ...], note?, src?}]   → กล่อง "หลักจำ" ต่อจาก "จำไปสอบ"

SVG ของภาพเคลื่อนไหวใช้ class เดียวกับ figure เดิม (.fig) + กลไกขั้น:
  data-s="k"  → โผล่ตั้งแต่ขั้น k   · data-x="k" → หายไปตั้งแต่ขั้น k
  class fl (เส้นประไหล) · rv (ไหลกลับทาง) · pl (กะพริบ/เต้น) · sl (ไหลช้า) · <animate>/<animateMotion> ได้
ตัวเล่น: เล่นเองเมื่อเลื่อนมาเห็น วนกลับขั้นแรก · ปุ่ม ‹ ⏸/▶ › และจุดบอกขั้น · prefers-reduced-motion → ไม่เล่นเอง
"""
import sys, os, json, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_deeplinks import unwrap, sub  # noqa: E402

CSS = r'''
/* ---------- กลไกแบบภาพเคลื่อนไหว ([[anim:key]] + section.anims) ---------- */
.fig.anim{border-color:color-mix(in srgb,var(--accent) 30%,var(--rule))}
.fig.anim .figt span{color:var(--accent);}
.anim svg [data-s],.anim svg [data-x]{transition:opacity .55s var(--e)}
.anim svg .aoff{opacity:0}
.anim svg .anow{animation:anow 1.1s var(--e) both}
@keyframes anow{0%{opacity:0}35%{opacity:1}100%{opacity:1}}
.anim svg .fl{stroke-dasharray:7 7;animation:afl 1.1s linear infinite}
.anim svg .fl.rv{animation-direction:reverse}
.anim svg .fl.sl{animation-duration:2.6s}
.anim svg .pl{animation:apl 1.3s ease-in-out infinite}
@keyframes afl{to{stroke-dashoffset:-14}}
@keyframes apl{0%,100%{opacity:1}50%{opacity:.35}}
.anim.paused svg .fl,.anim.paused svg .pl{animation-play-state:paused}
.actl{display:flex;align-items:center;gap:8px;margin-top:10px;flex-wrap:wrap}
.actl .ab{font:inherit;font-size:14px;font-weight:700;min-width:38px;height:34px;padding:0 11px;border-radius:999px;border:1px solid var(--rule-strong);background:var(--surface);color:var(--ink-2);cursor:pointer}
.actl .ab:hover{border-color:var(--accent);color:var(--accent-ink)}
.actl .ab.pp{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.actl .dots{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.actl .dot{width:22px;height:22px;border-radius:50%;border:1px solid var(--rule-strong);background:var(--surface);font:600 11px/20px var(--mono);color:var(--ink-3);cursor:pointer;padding:0;text-align:center}
.actl .dot.on{background:var(--accent-soft);border-color:var(--accent);color:var(--accent-ink)}
.actl .dot.cur{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.acap{margin-top:10px;padding-top:9px;border-top:1px dashed var(--rule);font-size:13.6px;line-height:1.6;color:var(--ink-2);min-height:4.2em}
.acap b.st{display:block;color:var(--accent-ink);font-size:13px;margin-bottom:2px}
.acap strong{color:var(--ink)}
/* ---------- หลักจำ (section.mnem) ---------- */
.mnem{margin:18px 0 0;padding:15px 17px;border:1px solid color-mix(in srgb,var(--miss) 45%,var(--rule));border-radius:var(--r-md);background:var(--miss-soft)}
.mnem>h4{margin:0 0 4px;font-size:12px;letter-spacing:.07em;text-transform:uppercase;color:var(--miss);font-family:var(--sans)}
.mnem .mn+.mn{margin-top:14px;padding-top:13px;border-top:1px dashed color-mix(in srgb,var(--miss) 40%,var(--rule))}
.mnem .mnh{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:baseline}
.mnem .mnh b{font:700 17px/1.3 var(--mono);color:var(--ink);letter-spacing:.04em}
.mnem .mnh span{font-size:13.4px;color:var(--ink-2)}
.mnem ul{list-style:none;margin:8px 0 0;padding:0;display:grid;gap:4px}
.mnem li{display:grid;grid-template-columns:minmax(2.2em,max-content) 1fr;gap:10px;font-size:14.2px;line-height:1.5}
.mnem li b{font-family:var(--mono);color:var(--miss);font-weight:700}
.mnem .mnn{font-size:13px;color:var(--ink-2);margin:7px 0 0}
.mnem .mns{font-size:11.8px;color:var(--ink-3);margin:5px 0 0}
.chip.anc{border-color:var(--accent);color:var(--accent-ink)}
'''

JS = r'''
/* ---------- กลไกแบบภาพเคลื่อนไหว + หลักจำ ---------- */
var ANIMS={},ANIMN=0,RMOTION=false;
try{RMOTION=window.matchMedia("(prefers-reduced-motion: reduce)").matches;}catch(e){}
function animHtml(k){
  var a=ANIMS[k];if(!a||!a.svg||!a.steps||!a.steps.length)return "";
  var m=/viewBox="\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)\s*"/.exec(a.svg),w=m?+m[1]:560;
  var wide=w>440,sty="max-width:"+Math.round(w*1.25)+"px"+(wide?";min-width:"+Math.round(w*0.74)+"px":"");
  ANIMN++;
  var dots="";for(var i=1;i<=a.steps.length;i++)dots+="<button class='dot' data-astep='"+i+"' aria-label='ขั้นที่ "+i+"'>"+i+"</button>";
  return "<figure class='fig anim' data-ak='"+esc(k)+"' data-n='"+a.steps.length+"'>"+
    "<div class='figt'><span>▶ กลไก "+ANIMN+"</span>"+inline(a.title||"")+"</div>"+
    "<div class='figsv'><div class='figin' style='"+sty+"'>"+a.svg+"</div></div>"+
    (wide?"<div class='figscroll on'>← เลื่อนภาพไปทางขวาเพื่อดูส่วนที่เหลือ →</div>":"")+
    "<div class='actl'><button class='ab' data-aprev='1' aria-label='ขั้นก่อนหน้า'>‹</button>"+
    "<button class='ab pp' data-aplay='1' aria-label='เล่น/หยุด'>"+(RMOTION?"▶":"⏸")+"</button>"+
    "<button class='ab' data-anext='1' aria-label='ขั้นถัดไป'>›</button><span class='dots'>"+dots+"</span></div>"+
    "<div class='acap' aria-live='polite'></div>"+
    "<script type='application/json' class='asteps'>"+JSON.stringify(a.steps).replace(/</g,"\\u003c")+"<\/script></figure>";
}
function animShow(f,i){
  var A=f._a;A.i=i;
  var svg=f.querySelector("svg");
  if(svg){
    svg.querySelectorAll("[data-s]").forEach(function(el){var k=+el.getAttribute("data-s");
      el.classList.toggle("aoff",k>i);el.classList.toggle("anow",k===i);});
    svg.querySelectorAll("[data-x]").forEach(function(el){if(+el.getAttribute("data-x")<=i)el.classList.add("aoff");
      else if(!el.hasAttribute("data-s")||+el.getAttribute("data-s")<=i)el.classList.remove("aoff");});
  }
  f.querySelectorAll(".dot").forEach(function(d){var k=+d.getAttribute("data-astep");d.classList.toggle("on",k<i);d.classList.toggle("cur",k===i);});
  var s=A.steps[i-1]||{};
  f.querySelector(".acap").innerHTML="<b class='st'>ขั้น "+i+"/"+A.n+(s.t?" · "+inline(s.t):"")+"</b>"+(s.cap?inline(s.cap):"");
}
function animTick(f){
  var A=f._a;clearTimeout(A.tm);A.tm=null;
  if(!A.play||!A.vis)return;
  var s=A.steps[A.i-1]||{},ms=+s.ms||Math.max(3200,Math.min(9000,1800+String(s.cap||"").length*38));
  if(A.i>=A.n)ms+=2200;
  A.tm=setTimeout(function(){animShow(f,A.i>=A.n?1:A.i+1);animTick(f);},ms);
}
function animSetPlay(f,on){
  var A=f._a;A.play=on;f.classList.toggle("paused",!on);
  var b=f.querySelector("[data-aplay]");if(b)b.textContent=on?"⏸":"▶";
  var svg=f.querySelector("svg");
  try{if(svg&&svg.pauseAnimations){if(on&&A.vis&&!RMOTION)svg.unpauseAnimations();else svg.pauseAnimations();}}catch(e){}
  animTick(f);
}
var ANIM_IO=("IntersectionObserver" in window)?new IntersectionObserver(function(es){
  es.forEach(function(e){var f=e.target;if(!f._a)return;f._a.vis=e.isIntersecting&&e.intersectionRatio>0.35;animSetPlay(f,f._a.play);});
},{threshold:[0,0.35,0.6]}):null;
function animInit(root){
  (root||document).querySelectorAll("figure.anim").forEach(function(f){
    if(f._a)return;
    var steps=[];try{steps=JSON.parse(f.querySelector(".asteps").textContent);}catch(e){}
    f._a={i:1,n:+f.getAttribute("data-n")||steps.length,steps:steps,play:!RMOTION,vis:!ANIM_IO,tm:null};
    animShow(f,1);animSetPlay(f,f._a.play);
    if(ANIM_IO)ANIM_IO.observe(f);
  });
}
document.addEventListener("click",function(e){
  var b=e.target.closest&&e.target.closest("figure.anim button");if(!b)return;
  var f=b.closest("figure.anim"),A=f._a;if(!A)return;
  if(b.hasAttribute("data-aplay")){if(!A.play&&A.i>=A.n)animShow(f,1);animSetPlay(f,!A.play);return;}
  var to=b.hasAttribute("data-aprev")?Math.max(1,A.i-1):b.hasAttribute("data-anext")?Math.min(A.n,A.i+1):+b.getAttribute("data-astep");
  animShow(f,to);animSetPlay(f,false);
});
(function(){var m=document.getElementById("main");if(!m||!("MutationObserver" in window))return;
  new MutationObserver(function(){animInit(m);}).observe(m,{childList:true,subtree:true});})();
function mnemBody(list){
  return list.map(function(x){
    return "<div class='mn'><div class='mnh'><b>"+esc(x.name)+"</b>"+(x.what?"<span>"+inline(x.what)+"</span>":"")+"</div>"+
      (x.lines&&x.lines.length?"<ul>"+x.lines.map(function(r){return "<li><b>"+esc(r[0])+"</b><span>"+inline(r[1]||"")+"</span></li>";}).join("")+"</ul>":"")+
      (x.note?"<p class='mnn'>"+inline(x.note)+"</p>":"")+(x.src?"<p class='mns'>ที่มา: "+inline(x.src)+"</p>":"")+"</div>";
  }).join("");
}
function mnemHtml(s){return s.mnem&&s.mnem.length?"<div class='mnem'><h4>หลักจำ</h4>"+mnemBody(s.mnem)+"</div>":"";}
function animCount(s){return Object.keys(s.anims||{}).length;}
'''


def patch_page(src):
    s = unwrap(src)
    s = sub(s, '.mk{fill:var(--ink-2)}.mk-ac{fill:var(--accent)}',
            CSS.strip() + '\n.mk{fill:var(--ink-2)}.mk-ac{fill:var(--accent)}')
    s = sub(s, '/* ---------- tiny markdown (เหมือน drill.html) ---------- */',
            JS.strip() + '\n\n/* ---------- tiny markdown (เหมือน drill.html) ---------- */')
    # md: [[anim:key]]
    s = sub(s, '''    if(fm){flushPara();out.push(figHtml(fm[1]));i++;continue;}''',
            '''    if(fm){flushPara();out.push(figHtml(fm[1]));i++;continue;}
    var am=/^\\s*\\[\\[anim:([\\w-]+)\\]\\]\\s*$/.exec(L);
    if(am){flushPara();out.push(animHtml(am[1]));i++;continue;}''')
    # หน้า section: ตั้ง ANIMS คู่กับ FIGS · กล่องหลักจำต่อจาก "จำไปสอบ"
    s = sub(s, '''    (FIGS=s.figs||{},FIGN=0,"<div class='prose'>"+(hid?recallHtml(s):md(s.md))+"</div>");
  FIGS={};''', '''    (FIGS=s.figs||{},FIGN=0,ANIMS=s.anims||{},ANIMN=0,"<div class='prose'>"+(hid?recallHtml(s):md(s.md))+"</div>");
  FIGS={};ANIMS={};''')
    s = sub(s, '''    h+="<div class='pearls'><h4>จำไปสอบ</h4><ul>"+s.pearls.map(function(p){return "<li>"+inline(p)+"</li>";}).join("")+"</ul></div>";
''', '''    h+="<div class='pearls'><h4>จำไปสอบ</h4><ul>"+s.pearls.map(function(p){return "<li>"+inline(p)+"</li>";}).join("")+"</ul></div>";
  if(!hid)h+=mnemHtml(s);
''')
    # โหมดทวน: หลักจำเป็นอีกหัวข้อที่กดเปิดได้
    s = sub(s, '''    h+=rvBlock(s.id+"-p","จำไปสอบ",3,"<ul>"+s.pearls.map(function(p){return "<li>"+inline(p)+"</li>";}).join("")+"</ul>");
  return h;''', '''    h+=rvBlock(s.id+"-p","จำไปสอบ",3,"<ul>"+s.pearls.map(function(p){return "<li>"+inline(p)+"</li>";}).join("")+"</ul>");
  if(s.mnem&&s.mnem.length)h+=rvBlock(s.id+"-m","หลักจำ",3,"<div class='mnem'>"+mnemBody(s.mnem)+"</div>");
  return h;''')
    # การ์ดหัวข้อในหน้าคาบ: บอกว่ามีภาพเคลื่อนไหว/หลักจำ
    s = sub(s, '''      (hid?"":"<span>"+esc(s.summary||"")+"</span>")+''',
            '''      (hid?"":"<span>"+esc(s.summary||"")+"</span>")+
      (animCount(s)||(s.mnem&&s.mnem.length)?"<span class='chip anc' style='align-self:flex-start'>"+
        (animCount(s)?"▶ กลไก "+animCount(s):"")+(animCount(s)&&s.mnem&&s.mnem.length?" · ":"")+(s.mnem&&s.mnem.length?"หลักจำ "+s.mnem.length:"")+"</span>":"")+''')
    return s


def _insert_marker(md, after, marker):
    """วาง marker ท้ายช่วงของหัวข้อ `after` (ก่อนหัวข้อระดับเดียวกันหรือสูงกว่าถัดไป) · ไม่เจอ/ว่าง → ท้าย md"""
    lines = md.split("\n")
    if after:
        want = re.sub(r"^#+\s*", "", after).strip()
        for i, L in enumerate(lines):
            m = re.match(r"^\s*(#{3,4})\s+(.*)$", L)
            if m and m.group(2).strip() == want:
                lvl = len(m.group(1))
                j = i + 1
                while j < len(lines):
                    m2 = re.match(r"^\s*(#{3,4})\s+", lines[j])
                    if m2 and len(m2.group(1)) <= lvl:
                        break
                    j += 1
                while j > i + 1 and not lines[j - 1].strip():
                    j -= 1
                return "\n".join(lines[:j] + ["", marker, ""] + lines[j:]).replace("\n\n\n", "\n\n"), True
    return md.rstrip() + "\n\n" + marker, not after


def patch_data(data_dir, anim_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    adds = {}
    for f in sorted(glob.glob(os.path.join(anim_dir, "*.json"))):
        a = json.load(open(f, encoding="utf-8"))
        adds.setdefault(a["set"], []).append(a)
    report = []
    for f in sorted(glob.glob(os.path.join(data_dir, "*.json"))):
        name = os.path.basename(f)
        d = json.load(open(f, encoding="utf-8"))
        st = name[:-5]
        if st in adds:
            secs = {s["id"]: s for L in d for s in L["sections"]}
            for a in adds[st]:
                for it in a.get("items", []):
                    s = secs[it["sec"]]
                    k = it["anim"]["key"]
                    s.setdefault("anims", {})
                    assert k not in s["anims"], (st, k)
                    an = {x: it["anim"][x] for x in ("title", "svg", "steps")}
                    s["anims"][k] = an
                    s["md"], ok = _insert_marker(s["md"], it.get("after", ""), "[[anim:%s]]" % k)
                    if not ok:
                        report.append("หัวข้อ '%s' ไม่พบใน %s → วางท้าย" % (it.get("after"), it["sec"]))
                for m in a.get("mnem", []):
                    s = secs[m["sec"]]
                    s.setdefault("mnem", []).append({x: m[x] for x in ("name", "what", "lines", "note", "src") if m.get(x)})
        json.dump(d, open(os.path.join(out_dir, name), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    return report


if __name__ == "__main__":
    if len(sys.argv) >= 4 and sys.argv[1] == "page":
        out = patch_page(open(sys.argv[2], encoding="utf-8").read())
        open(sys.argv[3], "w", encoding="utf-8").write(out)
        print("ok", len(out))
    elif len(sys.argv) == 5 and sys.argv[1] == "data":
        for r in patch_data(sys.argv[2], sys.argv[3], sys.argv[4]):
            print(r)
        print("ok")
    else:
        sys.exit(__doc__)
