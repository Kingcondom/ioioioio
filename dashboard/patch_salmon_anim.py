# -*- coding: utf-8 -*-
"""ตัวเล่นภาพเคลื่อนไหวกลไกสำหรับ Salmon NL (แบบเดียวกับ learn · patch_learn_anim.py)

    python3 patch_salmon_anim.py <salmon index.html ที่ดาวน์โหลด> <out.html>

section.anims = {id: {title, svg, steps:[{t, cap}]}} · md มี [[anim:id]]
SVG ใช้ class ของ figure ใน Salmon (box sunk acsoft c1soft badsoft lna lnc2 t2 t3 tb ta …)
+ data-s / data-x (โผล่/หายตามขั้น) + class fl (เส้นประไหล) pl (กะพริบ) + SMIL ได้
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_deeplinks import unwrap, sub  # noqa: E402

CSS = r'''
/* ---------- กลไกแบบภาพเคลื่อนไหว ([[anim:id]] + section.anims) ---------- */
.fig.anim .fbody svg{min-width:0;max-width:620px}
.fig.anim .ftitle::before{content:"▶ ";color:var(--accent)}
.anim svg [data-s],.anim svg [data-x]{transition:opacity .55s var(--e)}
.anim svg .aoff{opacity:0}
.anim svg .anow{animation:anow 1.1s var(--e) both}
@keyframes anow{0%{opacity:0}35%{opacity:1}100%{opacity:1}}
.anim svg .fl{stroke-dasharray:7 7;animation:afl 1.1s linear infinite}
.anim svg .pl{animation:apl 1.3s ease-in-out infinite}
@keyframes afl{to{stroke-dashoffset:-14}}
@keyframes apl{0%,100%{opacity:1}50%{opacity:.35}}
.anim.paused svg .fl,.anim.paused svg .pl{animation-play-state:paused}
.actl{display:flex;align-items:center;gap:8px;padding:8px 14px 0;flex-wrap:wrap}
.actl .ab{font:inherit;font-size:14px;font-weight:700;min-width:38px;height:34px;padding:0 11px;border-radius:999px;border:1px solid var(--rule-strong);background:var(--surface);color:var(--ink-2);cursor:pointer}
.actl .ab.pp{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.actl .dots{display:flex;gap:6px;flex-wrap:wrap}
.actl .dot{width:22px;height:22px;border-radius:50%;border:1px solid var(--rule-strong);background:var(--surface);font:600 11px/20px var(--mono);color:var(--ink-3);cursor:pointer;padding:0;text-align:center}
.actl .dot.on{background:var(--accent-soft);border-color:var(--accent);color:var(--accent-ink)}
.actl .dot.cur{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.acap{font-size:13.6px;line-height:1.6;color:var(--ink-2);padding:8px 14px 12px;min-height:4.4em}
.acap b.st{display:block;color:var(--accent-ink);font-size:13px;margin-bottom:2px}
.acap strong{color:var(--ink)}
'''

JS = r'''
/* ---------- กลไกแบบภาพเคลื่อนไหว ---------- */
var ANIMS={},RMOTION=false;
try{RMOTION=window.matchMedia("(prefers-reduced-motion: reduce)").matches;}catch(e){}
function animHtml(k){
  var a=ANIMS[k];if(!a||!a.svg||!a.steps||!a.steps.length)return "";
  var dots="";for(var i=1;i<=a.steps.length;i++)dots+="<button class='dot' data-astep='"+i+"' aria-label='ขั้นที่ "+i+"'>"+i+"</button>";
  return "<figure class='fig anim' data-ak='"+esc(k)+"' data-n='"+a.steps.length+"'>"+(a.title?"<div class='ftitle'>"+esc(a.title)+"</div>":"")+
    "<div class='fbody'>"+a.svg+"</div>"+
    "<div class='actl'><button class='ab' data-aprev='1' aria-label='ขั้นก่อนหน้า'>‹</button>"+
    "<button class='ab pp' data-aplay='1' aria-label='เล่น/หยุด'>"+(RMOTION?"▶":"⏸")+"</button>"+
    "<button class='ab' data-anext='1' aria-label='ขั้นถัดไป'>›</button><span class='dots'>"+dots+"</span></div>"+
    "<div class='acap' aria-live='polite'></div>"+
    "<script type='application/json' class='asteps'>"+JSON.stringify(a.steps).replace(/</g,"\\u003c")+"<\/script></figure>";
}
function animShow(f,i){
  var A=f._a;A.i=i;var svg=f.querySelector("svg");
  if(svg){
    svg.querySelectorAll("[data-s]").forEach(function(el){var k=+el.getAttribute("data-s");el.classList.toggle("aoff",k>i);el.classList.toggle("anow",k===i);});
    svg.querySelectorAll("[data-x]").forEach(function(el){if(+el.getAttribute("data-x")<=i)el.classList.add("aoff");
      else if(!el.hasAttribute("data-s")||+el.getAttribute("data-s")<=i)el.classList.remove("aoff");});
  }
  f.querySelectorAll(".dot").forEach(function(d){var k=+d.getAttribute("data-astep");d.classList.toggle("on",k<i);d.classList.toggle("cur",k===i);});
  var s=A.steps[i-1]||{};
  f.querySelector(".acap").innerHTML="<b class='st'>ขั้น "+i+"/"+A.n+(s.t?" · "+inline(s.t):"")+"</b>"+(s.cap?inline(s.cap):"");
}
function animTick(f){
  var A=f._a;clearTimeout(A.tm);A.tm=null;if(!A.play||!A.vis)return;
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
    if(f._a)return;var steps=[];try{steps=JSON.parse(f.querySelector(".asteps").textContent);}catch(e){}
    f._a={i:1,n:+f.getAttribute("data-n")||steps.length,steps:steps,play:!RMOTION,vis:!ANIM_IO,tm:null};
    animShow(f,1);animSetPlay(f,f._a.play);if(ANIM_IO)ANIM_IO.observe(f);
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
'''


def patch(src):
    s = unwrap(src) if src.startswith("<!doctype html><html><head><meta charset=utf8>") else src
    if "function animHtml" in s:
        return s
    s = sub(s, '.fig .ftitle{', CSS.strip() + '\n.fig .ftitle{')
    s = sub(s, '''function mdFigs(s){
  md._used={};''', JS.strip() + '''
function mdFigs(s){
  ANIMS=s.anims||{};md._used={};''')
    s = sub(s, '''    if(fm){flushPara();var f=(figs||[]).filter(function(x){return x.id===fm[1];})[0];if(f){used[f.id]=1;out.push(figHtml(f));}i++;continue;}''',
            '''    if(fm){flushPara();var f=(figs||[]).filter(function(x){return x.id===fm[1];})[0];if(f){used[f.id]=1;out.push(figHtml(f));}i++;continue;}
    var am=L.match(/^\\s*\\[\\[anim:([\\w-]+)\\]\\]\\s*$/);
    if(am){flushPara();out.push(animHtml(am[1]));i++;continue;}''')
    return s


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    open(sys.argv[2], "w", encoding="utf-8").write(patch(open(sys.argv[1], encoding="utf-8").read()))
    print("ok")
