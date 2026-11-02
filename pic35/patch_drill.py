#!/usr/bin/env python3
"""เพิ่มข้อสอบที่เป็นรูป (MED35) เข้า Ward Drill ที่ publish อยู่ — แก้จากหน้าเว็บจริง ไม่ build ใหม่

ใช้:
    python3 pic35/patch_drill.py <live.html ที่ได้จาก Artifact read> <ไฟล์ปลายทาง> <โฟลเดอร์รูปต้นฉบับ>

ทำอะไร
1. ย่อ/ครอปรูปจาก Google Doc → pic35/img/med35-XX.jpg (ครอปส่วนที่เฉลยคำตอบออก)
2. ถอด wrapper ที่บริการ artifact ใส่ไว้รอบหน้า (ถ้ามี)
3. ใส่ข้อจาก items_med35.py ลง BANK[set].mcq / .meq (id ซ้ำ = แทนที่ → รันซ้ำได้)
   MCQ สลับตำแหน่งคำตอบแบบ deterministic ด้วย seed ตาม id
4. แพตช์ CSS/JS: รองรับฟิลด์ `img` (ภาพในโจทย์ MCQ/MEQ/SAQ) + โหมด "ข้อสอบมีรูป"
   (รันซ้ำได้: ถ้าแพตช์อยู่แล้วจะข้าม)
"""
import json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from items_med35 import ITEMS  # noqa: E402

# ---------------------------------------------------------------- images
# ชื่อไฟล์ใน Google Doc (ตามลำดับ inline object) → ไฟล์ปลายทาง + กรอบครอป (left, top, right, bottom) หรือ None
IMAGES = {
    "med35-01": ("40_pzbw8k9yw00e", (1060, 300, 1880, 649)),  # EKG จากโพย MEQ (ตัดลายมือเฉลยออก)
    "med35-02": ("34_lzp2le6to019", (180, 62, 870, 405)),     # EKG FA MEQ (ตัดกล่องเฉลยด้านล่างออก)
    "med35-03": ("55_9auao3gvas1n", None),                    # Mobitz II
    "med35-04": ("47_nsg0udr1ults", None),                    # India ink (FA SAQ)
    "med35-05": ("63_a33zjut5552s", None),                    # India ink (ลงกอง 1)
    "med35-06": ("62_umxbk0wbemub", None),                    # eschar
    "med35-07": ("75_u7p0bi2qtk08", None),                    # P. vivax
    "med35-08a": ("48_qpeq4i6wl9s6", None),                   # PV ที่หลัง
    "med35-08b": ("49_4cxgjytbz33z", None),                   # KOH
    "med35-09": ("49_4cxgjytbz33z", None),                    # KOH (ข้อ MCQ)
    "med35-10": ("72_d9hg9gpoblxa", None),                    # tinea unguium
    "med35-11": ("73_9961ma1ekgzz", (40, 20, 360, 268)),      # zoster (ตัดคำว่า Shingles ออก)
    "med35-12": ("76_6pcukpvmv6ml", None),                    # varicella
    "med35-13": ("50_lcqtc6y8r9nn", (85, 95, 910, 525)),      # thyroid scan (ตัดตัวเลือก/เฉลย LMS ออก)
    "med35-14": ("51_pxpzxh5h09kk", None),                    # Vibrio
    "med35-15": ("59_p863wviouewv", None),                    # urticaria
    "med35-16": ("52_54qogkf4akdc", (0, 0, 260, 262)),        # MSU crystals (ตัด caption)
    "med35-17": ("70_130ie9w6x1bp", None),                    # synovial fluid
    "med35-18": ("53_shp96tmiwpx2", None),                    # face (MCTD)
    "med35-19": ("56_tw8zcycd83qw", (90, 0, 1300, 905)),      # clubbing (ตัดเฉลย Lung CA)
    "med35-20": ("61_kqgztth7wkec", (40, 90, 415, 325)),      # GNB (ตัดชื่อเชื้อออก)
    "med35-21": ("69_gjsdv7e6uua7", None),                    # KUB staghorn
    "med35-22": ("65_5xqbxr86zoaw", None),                    # CXR TB
    "med35-23": ("67_4pay2ks9aeyj", None),                    # CXR parapneumonic
    "med35-24": ("68_rw90dgxl29vk", None),                    # PBS IDA
}
MAX_EDGE = 1200


def build_images(src_dir, out_dir):
    from PIL import Image
    os.makedirs(out_dir, exist_ok=True)
    total = 0
    for name, (src, box) in IMAGES.items():
        im = Image.open(os.path.join(src_dir, src)).convert("RGB")
        if box:
            im = im.crop(box)
        im.thumbnail((MAX_EDGE, MAX_EDGE))
        p = os.path.join(out_dir, name + ".jpg")
        im.save(p, "JPEG", quality=82, optimize=True, progressive=True)
        total += os.path.getsize(p)
    print(f"images: {len(IMAGES)} files, {total/1024:.0f} KB -> {out_dir}")


# ---------------------------------------------------------------- page patch
CSS = """
/* ---------- ภาพในโจทย์ (ข้อสอบที่เป็นรูป) ---------- */
.qfigs{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 16px;max-width:74ch}
.qfig{margin:0;flex:1 1 260px;min-width:0;background:var(--surface-sunk);border-radius:var(--r-md);padding:8px}
.qfig a{display:block;border-radius:8px;overflow:hidden}
.qfig img{display:block;max-width:100%;width:auto;height:auto;max-height:460px;margin:0 auto;object-fit:contain;background:#fff;border-radius:8px}
.qfig figcaption{font-size:12px;color:var(--ink-3);margin:7px 2px 1px;line-height:1.45}
.tag.pic{color:var(--accent);background:var(--accent-soft);font-weight:600}
"""

JS_FUNCS = r"""
/* ---------- ข้อสอบที่เป็นรูป: ฟิลด์ img = [{src, cap}] ---------- */
var PIC_SCOPE="all";
function hasPic(it){return !!(it&&it.img&&it.img.length);}
function picItems(scope){scope=scope||PIC_SCOPE;var out=[];
  SETS.forEach(function(s){if(scope!=="all"&&s.k!==state.set)return;
    newItems(s.k).forEach(function(it){if(hasPic(it))out.push({set:s.k,it:it});});});
  return out;}
function figs(it){
  if(!hasPic(it))return "";
  return "<div class='qfigs'>"+it.img.map(function(f){var s=esc(f.src);
    return "<figure class='qfig'><a href='"+s+"' target='_blank' rel='noopener' title='เปิดภาพขนาดเต็ม'>"+
      "<img src='"+s+"' alt='"+esc(f.cap||"ภาพประกอบโจทย์")+"' loading='lazy'></a>"+
      (f.cap?"<figcaption>"+inline(f.cap)+"</figcaption>":"")+"</figure>";}).join("")+"</div>";
}
function buildPicRail(){
  var el=document.getElementById("picscope");el.innerHTML="";
  [{k:"all",label:"ทุกระบบ",n:picItems("all").length},{k:"set",label:"เฉพาะ "+setLabel(state.set),n:picItems("set").length}]
    .forEach(function(o){var b=document.createElement("button");b.type="button";b.className="chip";
      b.setAttribute("aria-pressed",String(PIC_SCOPE===o.k));b.textContent=o.label+" · "+o.n;
      b.addEventListener("click",function(){PIC_SCOPE=o.k;render();});el.appendChild(b);});
  document.getElementById("picinfo").innerHTML="ภาพจากโพยข้อสอบจริง (EKG, CXR, KUB, PBS, Gram / KOH / India ink, ผื่น) · แตะภาพเพื่อเปิดขนาดเต็ม · ข้อเหล่านี้อยู่ในแท็บ <b>ข้อสอบใหม่</b> ของแต่ละระบบด้วย";
}
function renderPic(stream){
  var list=picItems();
  if(!list.length){stream.innerHTML="<p class='empty'>ระบบนี้ยังไม่มีข้อสอบที่เป็นรูป — เลือก “ทุกระบบ” ที่แถบด้านข้าง</p>";return;}
  var head=document.createElement("div");head.className="part-head";
  head.innerHTML="<h2>ข้อสอบที่เป็นรูป · โพย MED35</h2><span class='meta'>"+list.length+" ข้อ</span>";
  stream.appendChild(head);
  var cur="";
  list.forEach(function(e){
    if(e.set!==cur){cur=e.set;var h=document.createElement("div");h.className="part-head";
      h.innerHTML="<h2 style='font-size:16px'>"+esc(setLabel(e.set))+"</h2><span class='meta'>"+
        list.filter(function(x){return x.set===e.set;}).length+" ข้อ</span>";stream.appendChild(h);}
    stream.appendChild(partOf(e.it)==="MCQ"?renderMCQ(e.it,0):renderLong(e.it));
  });
}
"""

JS_SCORE = r"""  if(state.mode==="pic"){var pl=picItems(),pd=0,pr=0;
    pl.forEach(function(e){var a=state.answers[e.it.id];if(a){pd++;if(a.ok)pr++;}});
    var pp=pd?Math.round(pr/pd*100):0;
    document.getElementById("sc-done").textContent=pd;document.getElementById("sc-right").textContent=pr;
    var pa=document.getElementById("sc-acc");pa.textContent=pd?pp+"%":"—";pa.style.setProperty("--pct",pp);
    document.getElementById("railnote").innerHTML="<b>ข้อสอบมีรูป</b> MCQ "+pl.filter(function(e){return partOf(e.it)==="MCQ";}).length+
      " ข้อ · SAQ "+pl.filter(function(e){return partOf(e.it)!=="MCQ";}).length+" สถานี · คะแนนด้านบนนับเฉพาะข้อที่มีรูป · กด <b>1–5</b> เพื่อตอบข้อที่เห็นอยู่บนจอ";
    return;}
"""

RAIL = """    <div id="picblock" style="display:none">
      <h2>แสดงข้อจาก</h2>
      <div class="parts" id="picscope"></div>
      <p class="qzinfo" id="picinfo"></p>
    </div>
"""

# (คำค้น, ข้อความแทน, เครื่องหมายว่าแพตช์แล้ว)
REPLACEMENTS = [
    ("@media print{", CSS.lstrip("\n") + "@media print{", ".qfigs{"),
    ('{k:"quiz",label:"สุ่มทำข้อสอบ"}', '{k:"pic",label:"ข้อสอบมีรูป"},{k:"quiz",label:"สุ่มทำข้อสอบ"}', '{k:"pic",label:"ข้อสอบมีรูป"}'),
    ('function partOf(it){return it.part||"MCQ";}', 'function partOf(it){return it.part||"MCQ";}' + JS_FUNCS, "function renderPic("),
    ("  h+=\"<p class='stem'>\"+inline(it.stem)+\"</p>\";\n",
     "  h+=\"<p class='stem'>\"+inline(it.stem)+\"</p>\";\n  h+=figs(it);\n", "  h+=figs(it);\n  sec.innerHTML=h;\n  var wrap"),
    ("  if(it.instruction)h+=vign(it.instruction);\n",
     "  if(it.instruction)h+=vign(it.instruction);\n  h+=figs(it);\n", "vign(it.instruction);\n  h+=figs(it);"),
    ('    hot:hotList(state.set).length,', '    hot:hotList(state.set).length,\n    pic:picItems("all").length,', 'pic:picItems("all").length'),
    ('  var qz=state.mode==="quiz",rv=state.mode==="review";',
     '  var qz=state.mode==="quiz",rv=state.mode==="review",pc=state.mode==="pic";', 'pc=state.mode==="pic"'),
    ('document.getElementById("lecbar").parentNode.style.display=(qz||rv)?"none":"";',
     'document.getElementById("lecbar").parentNode.style.display=(qz||rv||pc)?"none":"";\n'
     '  document.getElementById("picblock").style.display=pc?"":"none";\n  if(pc)buildPicRail();', "if(pc)buildPicRail();"),
    ('var showBtns=!qz&&(rv||(state.mode==="new")||', 'var showBtns=!qz&&(rv||pc||(state.mode==="new")||', "(rv||pc||"),
    ('  else if(state.mode==="hot")renderHot(stream);\n',
     '  else if(state.mode==="hot")renderHot(stream);\n  else if(pc)renderPic(stream);\n', "else if(pc)renderPic(stream);"),
    ('  if(state.mode==="new")return filtered();\n',
     '  if(state.mode==="new")return filtered();\n  if(state.mode==="pic")return picItems().map(function(e){return e.it;});\n',
     'if(state.mode==="pic")return picItems()'),
    ('  if(state.mode==="quiz"){var q=qScore()', JS_SCORE + '  if(state.mode==="quiz"){var q=qScore()', 'if(state.mode==="pic"){var pl=picItems()'),
    ('    <div id="rvblock" style="display:none">', RAIL + '    <div id="rvblock" style="display:none">', 'id="picblock"'),
    ('  if(h==="review"||/^review~/.test(h)){rvFromHash(h);return true;}',
     '  if(h==="review"||/^review~/.test(h)){rvFromHash(h);return true;}\n'
     '  if(h==="pic"){state.mode="pic";PIC_SCOPE="all";save();return true;}', 'if(h==="pic")'),
    ("(NL) รายข้อ</p>", "(NL) รายข้อ · <b>ข้อสอบที่เป็นรูปจากโพย MED35</b> อยู่ในแท็บ “ข้อสอบมีรูป”</p>", "ข้อสอบที่เป็นรูปจากโพย MED35"),
]

WRAP_HEAD = re.compile(r'^<!doctype html><html><head><meta charset=utf8>.*?</head><body>\n', re.S)


def strip_wrapper(html):
    m = WRAP_HEAD.match(html)
    if not m:
        return html
    html = html[m.end():]
    tail = "\n</body></html>"
    k = html.rstrip("\n").rfind(tail)
    if k >= 0 and html.count("</body></html>") >= 2:
        html = html[:k] + "\n"
    print("stripped service wrapper")
    return html


def place_items(bank, nl_index):
    n = {"mcq": 0, "meq": 0}
    seen = set()
    for raw in ITEMS:
        it = json.loads(json.dumps(raw, ensure_ascii=False))
        s = it.pop("set")
        assert s in bank, s
        assert it["id"] not in seen, it["id"]
        seen.add(it["id"])
        it["years"] = ["35"]
        for c in it.get("nl", []):
            if c not in nl_index:
                print(f"  ! {it['id']}: NL {c} ไม่มีในดัชนีของหน้าเว็บ")
        if it["part"] == "MCQ":
            ch = it["choices"]
            assert len(ch) == 5 and len(set(ch)) == 5, it["id"]
            order = list(range(5))
            random.Random("med35-pic:" + it["id"]).shuffle(order)
            it["choices"] = [ch[i] for i in order]
            it["answer"] = order.index(0)
            key = "mcq"
            fields = ["id", "lec", "lecture", "topic", "img", "stem", "choices", "answer", "explain", "pearl", "ref", "part", "nl", "years"]
        else:
            assert it.get("questions"), it["id"]
            key = "meq"
            fields = ["id", "part", "lec", "lecture", "topic", "station", "img", "vignette", "questions", "ref", "nl", "years"]
        it = {f: it[f] for f in fields if f in it}
        lst = bank[s][key]
        lst[:] = [x for x in lst if x.get("id") != it["id"]]
        # วางต่อท้ายข้อของคาบเดียวกัน (ให้อยู่กลุ่มเดียวกันในรายการ)
        pos = max([i for i, x in enumerate(lst) if x.get("lec") == it["lec"]], default=len(lst) - 1) + 1
        lst.insert(pos, it)
        n[key] += 1
    print(f"items: MCQ {n['mcq']} + SAQ {n['meq']}")


def patch(html):
    html = strip_wrapper(html)
    lines = html.split("\n")
    bi = [i for i, l in enumerate(lines) if l.startswith('<script type="application/json" id="bank">')]
    assert len(bi) == 1
    l = lines[bi[0]]
    bank = json.loads(l[l.index(">") + 1:l.rindex("</script>")])
    nl_line = [x for x in lines if x.startswith("var NL  = {")][0]
    nl_index = json.loads(nl_line[nl_line.index("{"):nl_line.rindex("}") + 1])
    place_items(bank, nl_index)
    js = json.dumps(bank, ensure_ascii=False).replace("</", "<\\/")
    lines[bi[0]] = '<script type="application/json" id="bank">' + js + "</script>"
    html = "\n".join(lines)
    for old, new, marker in REPLACEMENTS:
        if marker in html:
            continue
        c = html.count(old)
        assert c == 1, f"anchor found {c}x: {old[:60]!r}"
        html = html.replace(old, new)
    return html


def main():
    live, out, src_dir = sys.argv[1:4]
    build_images(src_dir, os.path.join(HERE, "img"))
    html = patch(open(live, encoding="utf-8").read())
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {out} ({len(html.encode())/1e6:.2f} MB)")


if __name__ == "__main__":
    main()
