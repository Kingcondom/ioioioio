#!/usr/bin/env python3
"""MED421 exam kit — build ครั้งเดียวจบ: รวม -> ตรวจ -> สลับเฉลย -> เว็บ -> PDF

ใช้:
    python3 build.py                  # ทุกระบบ
    python3 build.py air              # เฉพาะระบบ air
    python3 build.py air --no-pdf     # ไม่ทำ PDF (เร็ว ใช้ตอนเขียนข้อ)
"""
import html
import json
import random
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHOICE_LETTERS = "abcde"


# ---------------------------------------------------------------- load/validate
class BuildError(Exception):
    pass


def load_config():
    return json.loads((ROOT / "config.json").read_text(encoding="utf-8"))


def load_nl(cfg):
    path = ROOT / cfg["build"]["nl_reference_file"]
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def validate(sysdef, data, nl, errors, warnings):
    lecs = {l["lec"] for l in sysdef["lectures"]}
    nl_entries = nl.get("entries", {})
    seen = set()
    for item in data["items"]:
        iid = item.get("id") or "<ไม่มี id>"
        if iid in seen:
            errors.append("%s: id ซ้ำ" % iid)
        seen.add(iid)
        if item.get("lec") not in lecs:
            errors.append("%s: lec '%s' ไม่มีในปฏิทินของระบบ %s" % (iid, item.get("lec"), sysdef["key"]))
        if item.get("type") == "mcq":
            ch = item.get("choices") or []
            if len(ch) != 5:
                errors.append("%s: ต้องมีตัวเลือก 5 ข้อ (พบ %d)" % (iid, len(ch)))
            if len(set(ch)) != len(ch):
                errors.append("%s: ตัวเลือกซ้ำกัน" % iid)
            if item.get("answer") != 0:
                errors.append("%s: ต้องเขียน answer: 0 เสมอ (วางคำตอบถูกไว้ตัวแรก แล้ว build สลับให้)" % iid)
            if not item.get("stem"):
                errors.append("%s: ไม่มี stem" % iid)
        elif item.get("type") == "meq":
            qs = item.get("questions") or []
            if not qs:
                errors.append("%s: MEQ ต้องมี questions" % iid)
            for n, q in enumerate(qs, 1):
                if not q.get("q") or not q.get("a"):
                    errors.append("%s: MEQ ข้อย่อยที่ %d ไม่มีคำถามหรือคำตอบ" % (iid, n))
            if not item.get("scenario"):
                errors.append("%s: MEQ ไม่มี scenario" % iid)
        else:
            errors.append("%s: type ต้องเป็น mcq หรือ meq" % iid)

        if not item.get("ref"):
            warnings.append("%s: ลืมใส่ ref" % iid)
        if not item.get("pearl"):
            warnings.append("%s: ลืมใส่ pearl" % iid)
        for code in item.get("nl", []):
            if nl_entries and code not in nl_entries:
                warnings.append("%s: NL code '%s' ไม่มีในไฟล์อ้างอิง" % (iid, code))
        if not item.get("nl"):
            warnings.append("%s: ยังไม่ผูก NL reference" % iid)


# ---------------------------------------------------------------- shuffle
def shuffle_answers(sysdef, data):
    """สลับตัวเลือกแบบ deterministic ต่อระบบ (seed คงที่ => build ใหม่ได้ผลเหมือนเดิม)"""
    rng = random.Random(sysdef["seed"])
    for item in sorted([i for i in data["items"] if i["type"] == "mcq"], key=lambda i: i["id"]):
        choices = list(item["choices"])
        correct = choices[0]
        order = list(range(len(choices)))
        rng.shuffle(order)
        item["choices"] = [choices[i] for i in order]
        item["answer"] = item["choices"].index(correct)
    return data


# ---------------------------------------------------------------- render
def esc(s):
    return html.escape(str(s), quote=False)


CSS = """
:root{color-scheme:light dark;--bg:#f6f7f9;--card:#fff;--ink:#16181d;--muted:#5b6472;--line:#e3e6ec;
--accent:ACCENT;--accent-soft:ACCENT14;--ok:#137a4d;--ok-soft:#137a4d18;--warn:#8a5a00;--radius:14px}
:root:not([data-theme=light]){@media (prefers-color-scheme:dark){}}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#12141a;--card:#1a1d25;--ink:#e8eaee;
--muted:#9aa3b2;--line:#2a2f3a;--accent-soft:ACCENT28;--ok:#4ade80;--ok-soft:#4ade8020}}
:root[data-theme=dark]{--bg:#12141a;--card:#1a1d25;--ink:#e8eaee;--muted:#9aa3b2;--line:#2a2f3a;
--accent-soft:ACCENT28;--ok:#4ade80;--ok-soft:#4ade8020}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans Thai",Sarabun,sans-serif}
.wrap{max-width:900px;margin:0 auto;padding-block:28px;padding-left:18px;padding-right:18px}
header.hero{border-left:5px solid var(--accent);padding:2px 0 2px 14px;margin-bottom:18px}
h1{font-size:1.6rem;margin:0 0 4px}
.sub{color:var(--muted);font-size:.92rem}
.stats{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 18px}
.stat{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:8px 12px;font-size:.85rem}
.stat b{color:var(--accent);font-size:1.05rem}
.bar{position:sticky;top:0;z-index:9;background:var(--bg);padding:10px 0;border-bottom:1px solid var(--line);
display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:16px}
select,input[type=search],button{font:inherit;color:var(--ink);background:var(--card);
border:1px solid var(--line);border-radius:9px;padding:7px 11px}
button{cursor:pointer}
button.primary{background:var(--accent);border-color:var(--accent);color:#fff}
input[type=search]{flex:1;min-width:140px}
.item{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px;margin-bottom:14px}
.meta{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-bottom:9px;font-size:.76rem;color:var(--muted)}
.tag{background:var(--accent-soft);color:var(--accent);border-radius:999px;padding:2px 9px;font-weight:600}
.tag.grey{background:var(--line);color:var(--muted)}
.stem{margin:0 0 12px}
ol.choices{list-style:none;margin:0;padding:0;counter-reset:c}
ol.choices li{counter-increment:c;border:1px solid var(--line);border-radius:10px;padding:8px 12px 8px 38px;
margin-bottom:7px;position:relative;cursor:pointer}
ol.choices li::before{content:counter(c,lower-alpha) ".";position:absolute;left:14px;color:var(--muted);font-weight:600}
ol.choices li.correct{border-color:var(--ok);background:var(--ok-soft)}
ol.choices li.wrong{border-color:#d9534f;background:#d9534f14}
.answer{display:none;margin-top:12px;border-top:1px dashed var(--line);padding-top:11px;font-size:.92rem}
.item.show .answer{display:block}
.item.show ol.choices li.key{border-color:var(--ok);background:var(--ok-soft)}
.answer .lbl{font-weight:700;color:var(--ok)}
.pearl{background:var(--accent-soft);border-radius:10px;padding:9px 12px;margin:9px 0}
.pearl b{color:var(--accent)}
.ref{color:var(--muted);font-size:.83rem}
.nl{margin-top:9px;display:flex;flex-wrap:wrap;gap:6px}
.nlchip{font-size:.76rem;border:1px solid var(--accent);color:var(--accent);border-radius:999px;
padding:2px 9px;cursor:help}
.nlbox{margin-top:8px;font-size:.82rem;color:var(--muted);border-left:3px solid var(--accent);padding-left:10px}
.meq .scenario{background:var(--accent-soft);border-radius:10px;padding:11px 13px;margin-bottom:11px}
.meq ol.sub{padding-left:20px;margin:0}
.meq ol.sub li{margin-bottom:10px}
.meq .a{display:none;color:var(--ok);margin-top:4px}
.item.show .meq-a,.item.show .a{display:block}
.note{font-size:.82rem;color:var(--warn);margin-top:8px}
footer{color:var(--muted);font-size:.82rem;border-top:1px solid var(--line);margin-top:26px;padding-top:14px}
a{color:var(--accent)}
.syslist{display:grid;gap:12px}
.syscard{display:block;background:var(--card);border:1px solid var(--line);border-left:5px solid var(--accent);
border-radius:var(--radius);padding:16px 18px;text-decoration:none;color:inherit}
.syscard h2{margin:0 0 4px;font-size:1.15rem}
@media print{
 .bar,.stats{display:none}
 body{background:#fff}
 .item{break-inside:avoid;border-color:#ccc}
 .answer,.a{display:block !important}
}
"""

JS = """
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
let revealed=false;
function apply(){
  const lec=$('#lec').value, q=$('#q').value.trim().toLowerCase();
  let n=0;
  $$('.item').forEach(el=>{
    const okLec = lec==='all' || el.dataset.lec===lec;
    const okQ = !q || el.innerText.toLowerCase().includes(q);
    const show = okLec && okQ;
    el.hidden = !show; if(show) n++;
  });
  $('#count').textContent=n;
}
function toggleAll(){
  revealed=!revealed;
  $$('.item').forEach(el=>el.classList.toggle('show',revealed));
  $('#reveal').textContent = revealed ? 'ซ่อนเฉลยทั้งหมด' : 'เปิดเฉลยทั้งหมด';
}
document.addEventListener('click',e=>{
  const li=e.target.closest('ol.choices li');
  if(li){
    const item=li.closest('.item');
    if(!item.classList.contains('show')){
      li.classList.add(li.dataset.key==='1'?'correct':'wrong');
      item.classList.add('show');
    }
    return;
  }
  const head=e.target.closest('[data-toggle]');
  if(head){ head.closest('.item').classList.toggle('show'); }
});
document.addEventListener('DOMContentLoaded',()=>{
  $('#lec').addEventListener('change',apply);
  $('#q').addEventListener('input',apply);
  $('#reveal').addEventListener('click',toggleAll);
  $('#reset').addEventListener('click',()=>{
    $$('ol.choices li').forEach(li=>li.classList.remove('correct','wrong'));
    $$('.item').forEach(el=>el.classList.remove('show'));
    revealed=false; $('#reveal').textContent='เปิดเฉลยทั้งหมด';
  });
  apply();
});
"""


def nl_chips(item, nl_entries):
    codes = item.get("nl", [])
    if not codes:
        return ""
    chips = "".join(
        '<span class="nlchip" title="%s">NL %s</span>'
        % (esc(nl_entries.get(c, {}).get("title", "ไม่พบในดัชนี")), esc(c))
        for c in codes
    )
    lines = []
    for c in codes:
        e = nl_entries.get(c)
        if not e:
            continue
        grp = " — กลุ่มที่ %s" % e["group"] if e.get("group") else ""
        lines.append("<div><b>NL %s</b> · %s%s<br>%s <span class=ref>(%s, หน้า %s)</span></div>"
                     % (esc(c), esc(e.get("section", "")), esc(grp), esc(e.get("title", "")),
                        esc(e.get("part", "")), esc(e.get("page", "-"))))
    box = '<div class="nlbox">%s</div>' % "".join(lines) if lines else ""
    return '<div class="nl">%s</div>%s' % (chips, box)


def render_item(item, nl_entries, lec_title):
    meta = ('<div class="meta"><span class="tag">%s</span><span class="tag grey">%s</span>'
            '<span>%s</span><span>· %s</span></div>'
            % (esc(item["id"]), esc(item["type"].upper()), esc(item.get("topic", "")), esc(lec_title)))
    nl = nl_chips(item, nl_entries)
    note = '<div class="note">หมายเหตุ: %s</div>' % esc(item["source_note"]) if item.get("source_note") else ""
    ref = '<div class="ref">อ้างอิง: %s</div>' % esc(item["ref"]) if item.get("ref") else ""
    pearl = '<div class="pearl"><b>Pearl</b> — %s</div>' % esc(item["pearl"]) if item.get("pearl") else ""

    if item["type"] == "mcq":
        lis = "".join(
            '<li data-key="%s" class="%s">%s</li>' % ("1" if i == item["answer"] else "0",
                                                      "key" if i == item["answer"] else "",
                                                      esc(c))
            for i, c in enumerate(item["choices"]))
        body = ('<p class="stem">%s</p><ol class="choices">%s</ol>'
                '<div class="answer"><span class="lbl">เฉลย: %s. %s</span>%s%s%s%s</div>'
                % (esc(item["stem"]), lis,
                   CHOICE_LETTERS[item["answer"]], esc(item["choices"][item["answer"]]),
                   pearl, ref, note, nl))
    else:
        subs = "".join(
            '<li>%s <span class="ref">(%s คะแนน)</span><div class="a"><b>แนวตอบ:</b> %s</div></li>'
            % (esc(q["q"]), esc(q.get("points", 1)), esc(q["a"]))
            for q in item["questions"])
        total = sum(q.get("points", 1) for q in item["questions"])
        body = ('<div class="meq"><div class="scenario">%s</div>'
                '<ol class="sub">%s</ol></div>'
                '<div class="answer">%s%s%s%s<div class="ref">รวม %s คะแนน</div></div>'
                % (esc(item["scenario"]), subs, pearl, ref, note, nl, total))
    return ('<article class="item" data-lec="%s" id="%s">%s%s'
            '<div style="margin-top:10px"><button data-toggle>เปิด/ปิดเฉลย</button></div></article>'
            % (esc(item["lec"]), esc(item["id"]), meta, body))


def render_system(sysdef, data, nl, cfg):
    nl_entries = nl.get("entries", {})
    lec_title = {l["lec"]: "%s %s" % (l["lec"], l["title"]) for l in sysdef["lectures"]}
    items = sorted(data["items"], key=lambda i: (i["lec"], i["id"]))
    n_mcq = sum(1 for i in items if i["type"] == "mcq")
    n_meq = sum(1 for i in items if i["type"] == "meq")
    n_nl = len({c for i in items for c in i.get("nl", [])})

    opts = "".join('<option value="%s">%s</option>' % (esc(l["lec"]), esc(lec_title[l["lec"]]))
                   for l in sysdef["lectures"])
    body = "".join(render_item(i, nl_entries, lec_title[i["lec"]]) for i in items)
    css = CSS.replace("ACCENT28", sysdef["color"] + "28").replace("ACCENT14", sysdef["color"] + "14").replace("ACCENT", sysdef["color"])

    return """<title>%(name)s — MED421 Drill</title>
<style>%(css)s</style>
<div class="wrap">
<header class="hero">
  <h1>%(name)s</h1>
  <div class="sub">%(course)s · %(name_th)s · build %(built)s</div>
</header>
<div class="stats">
  <div class="stat"><b>%(n_mcq)d</b> MCQ</div>
  <div class="stat"><b>%(n_meq)d</b> MEQ</div>
  <div class="stat"><b>%(n_lec)d</b> lecture</div>
  <div class="stat"><b>%(n_nl)d</b> หัวข้อ NL 2567 ที่ครอบคลุม</div>
</div>
<div class="bar">
  <select id="lec"><option value="all">ทุก lecture</option>%(opts)s</select>
  <input id="q" type="search" placeholder="ค้นหาคำในโจทย์ / เฉลย / pearl">
  <button id="reveal" class="primary">เปิดเฉลยทั้งหมด</button>
  <button id="reset">ล้างคำตอบ</button>
  <span class="ref">แสดง <b id="count">0</b> ข้อ</span>
</div>
%(body)s
<footer>
  อ้างอิงเกณฑ์ NL: %(nlsrc)s<br>
  ชิป <span class="nlchip">NL …</span> ในแต่ละข้อคือรหัสหัวข้อตามเกณฑ์แพทยสภา พ.ศ. 2567 (ชี้เมาส์เพื่อดูชื่อเต็ม)<br>
  สร้างจาก med421-kit — แก้ข้อสอบที่ <code>%(file)s</code> แล้วสั่ง <code>python3 build.py %(key)s</code>
</footer>
</div>
<script>%(js)s</script>
""" % dict(name=esc(sysdef["name_en"]), name_th=esc(sysdef["name_th"]), course=esc(cfg["course"]),
           css=css, js=JS, opts=opts, body=body, built=date.today().isoformat(),
           n_mcq=n_mcq, n_meq=n_meq, n_lec=len(sysdef["lectures"]), n_nl=n_nl,
           nlsrc=esc(nl.get("source", "-")), file=esc(sysdef["file"]), key=esc(sysdef["key"]))


def render_index(cfg, built, nl):
    cards = "".join(
        '<a class="syscard" href="%s.html" style="--accent:%s"><h2>%s</h2>'
        '<div class="sub">%s · %d ข้อ (%d MCQ / %d MEQ) · %d lecture</div></a>'
        % (esc(s["key"]), esc(s["color"]), esc(s["name_en"]), esc(s["name_th"]),
           len(d["items"]), sum(1 for i in d["items"] if i["type"] == "mcq"),
           sum(1 for i in d["items"] if i["type"] == "meq"), len(s["lectures"]))
        for s, d in built)
    css = CSS.replace("ACCENT28", "#0ea5a428").replace("ACCENT14", "#0ea5a414").replace("ACCENT", "#0ea5a4")
    return """<title>MED421 Exam Kit</title>
<style>%(css)s</style>
<div class="wrap">
<header class="hero"><h1>%(course)s</h1>
<div class="sub">คลังข้อสอบแยกตามระบบ · ผูกเกณฑ์ NL 2567 รายข้อ · build %(built)s</div></header>
<div class="syslist">%(cards)s</div>
<footer>อ้างอิงเกณฑ์: %(nlsrc)s</footer>
</div>
""" % dict(css=css, course=esc(cfg["course"]), built=date.today().isoformat(), cards=cards,
           nlsrc=esc(nl.get("source", "-")))


# ---------------------------------------------------------------- pdf
def find_chromium():
    for c in ("/opt/pw-browsers/chromium", "chromium", "chromium-browser", "google-chrome"):
        p = shutil.which(c) or (c if Path(c).exists() else None)
        if p:
            return p
    return None


def to_pdf(html_path, pdf_path):
    exe = find_chromium()
    if not exe:
        print("  ข้าม PDF: ไม่พบ chromium/chrome ในเครื่อง")
        return False
    cmd = [exe, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
           "--print-to-pdf=%s" % pdf_path, "--virtual-time-budget=4000", html_path.as_uri()]
    r = subprocess.run(cmd, capture_output=True)
    if not pdf_path.exists():
        print("  ข้าม PDF: chromium ล้มเหลว (%s)" % r.stderr.decode()[-200:])
        return False
    return True


# ---------------------------------------------------------------- main
def main(argv):
    args = [a for a in argv[1:] if not a.startswith("-")]
    do_pdf = "--no-pdf" not in argv[1:]
    cfg = load_config()
    nl = load_nl(cfg)
    out = ROOT / cfg["build"]["out_dir"]
    out.mkdir(exist_ok=True)

    systems = [s for s in cfg["systems"] if not args or s["key"] in args]
    if not systems:
        raise BuildError("ไม่พบระบบที่ระบุ: %s" % ", ".join(args))

    errors, warnings, built = [], [], []
    for sysdef in systems:
        data = json.loads((ROOT / sysdef["file"]).read_text(encoding="utf-8"))
        validate(sysdef, data, nl, errors, warnings)
        built.append((sysdef, data))

    if errors:
        print("พบข้อผิดพลาด %d จุด — หยุด build" % len(errors))
        for e in errors:
            print("  ERROR %s" % e)
        return 1
    for w in warnings:
        print("  เตือน: %s" % w)

    for sysdef, data in built:
        shuffle_answers(sysdef, data)
        page = out / ("%s.html" % sysdef["key"])
        page.write_text(render_system(sysdef, data, nl, cfg), encoding="utf-8")
        print("  เขียน %s (%d ข้อ)" % (page.relative_to(ROOT), len(data["items"])))
        if do_pdf:
            pdf = out / ("%s.pdf" % sysdef["key"])
            if to_pdf(page, pdf):
                print("  เขียน %s" % pdf.relative_to(ROOT))

    (out / "index.html").write_text(render_index(cfg, built, nl), encoding="utf-8")
    print("  เขียน %s" % (out / "index.html").relative_to(ROOT))
    print("\nbuild สำเร็จ — %d ระบบ, เตือน %d จุด" % (len(built), len(warnings)))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except BuildError as e:
        print("BUILD ERROR: %s" % e)
        sys.exit(1)
