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
:root{
 --bg:#f4f7f7; --surface:#fff; --surface-2:#eef3f3; --ink:#0f1719; --muted:#5b6f74; --line:#dbe5e6;
 --accent:ACCENT; --accent-soft:ACCENT16; --ok:#0b6b4f; --ok-soft:#0b6b4f14; --bad:#a83a34; --bad-soft:#a83a3412;
 --shadow:0 1px 2px rgba(15,23,25,.05);
 --f-ui:"IBM Plex Sans Thai","IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
 --f-data:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){
 --bg:#0c1113; --surface:#131a1d; --surface-2:#182125; --ink:#e7eeef; --muted:#94a7ac; --line:#233035;
 --accent-soft:ACCENT2e; --ok:#5fd39f; --ok-soft:#5fd39f1c; --bad:#e08079; --bad-soft:#e0807916;
 --shadow:none;}}
:root[data-theme=dark]{
 --bg:#0c1113; --surface:#131a1d; --surface-2:#182125; --ink:#e7eeef; --muted:#94a7ac; --line:#233035;
 --accent-soft:ACCENT2e; --ok:#5fd39f; --ok-soft:#5fd39f1c; --bad:#e08079; --bad-soft:#e0807916; --shadow:none;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f-ui);font-size:15.5px;line-height:1.62;
 -webkit-font-smoothing:antialiased}
.wrap{max-width:780px;margin:0 auto;padding-block:34px 56px;padding-left:18px;padding-right:18px}
header.hero{display:flex;flex-direction:column;gap:6px;padding-bottom:20px;border-bottom:2px solid var(--ink)}
.eyebrow{font-family:var(--f-data);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
h1{font-size:clamp(1.55rem,4.4vw,2.1rem);line-height:1.18;margin:0;font-weight:600;letter-spacing:-.015em;text-wrap:balance}
.sub{color:var(--muted);font-size:.9rem}
.stats{display:flex;flex-wrap:wrap;gap:0;margin:0;border-bottom:1px solid var(--line)}
.stat{padding:12px 20px 12px 0;margin-right:20px;font-size:.78rem;color:var(--muted);letter-spacing:.02em}
.stat b{display:block;font-family:var(--f-data);font-size:1.35rem;font-weight:500;color:var(--ink);
 font-variant-numeric:tabular-nums;line-height:1.2}
.bar{position:sticky;top:0;z-index:9;background:var(--bg);padding:12px 0;border-bottom:1px solid var(--line);
 display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:8px}
select,input[type=search],button{font:inherit;font-size:.88rem;color:var(--ink);background:var(--surface);
 border:1px solid var(--line);border-radius:7px;padding:7px 11px}
button{cursor:pointer}
button:hover{border-color:var(--accent)}
button.primary{background:var(--accent);border-color:var(--accent);color:#fff}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
input[type=search]{flex:1;min-width:150px}
.score{font-family:var(--f-data);font-size:.8rem;color:var(--muted);font-variant-numeric:tabular-nums;margin-left:auto}
.score b{color:var(--ink)}
.item{padding:22px 0;border-bottom:1px solid var(--line)}
.meta{display:flex;flex-wrap:wrap;gap:10px;align-items:baseline;margin-bottom:10px;
 font-family:var(--f-data);font-size:.74rem;letter-spacing:.03em;color:var(--muted)}
.meta .id{color:var(--accent);font-weight:600}
.meta .topic{font-family:var(--f-ui);font-size:.82rem;color:var(--ink);letter-spacing:0;font-weight:500}
.meta .lec{font-size:.72rem;opacity:.8}
.stem{margin:0 0 14px}
ol.choices{list-style:none;margin:0;padding:0;counter-reset:c;display:flex;flex-direction:column;gap:6px}
ol.choices li{counter-increment:c;border:1px solid var(--line);background:var(--surface);border-radius:8px;
 padding:9px 13px 9px 40px;position:relative;cursor:pointer;transition:border-color .12s,background .12s}
ol.choices li:hover{border-color:var(--accent)}
ol.choices li::before{content:counter(c,lower-alpha);position:absolute;left:14px;top:9px;
 font-family:var(--f-data);font-size:.82rem;color:var(--muted)}
ol.choices li.correct,.item.show ol.choices li.key{border-color:var(--ok);background:var(--ok-soft)}
ol.choices li.wrong{border-color:var(--bad);background:var(--bad-soft)}
.answer{display:none;margin-top:14px;padding-left:15px;border-left:3px solid var(--accent);font-size:.94rem}
.item.show .answer{display:block}
.answer .lbl{display:block;font-weight:600;color:var(--ok);margin-bottom:8px}
.pearl{margin:0 0 8px}
.pearl b{font-family:var(--f-data);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);
 margin-right:6px}
.ref{color:var(--muted);font-size:.82rem}
.nl{margin-top:10px;display:flex;flex-wrap:wrap;gap:6px}
.nlchip{font-family:var(--f-data);font-size:.72rem;background:var(--accent-soft);color:var(--accent);
 border-radius:4px;padding:2px 7px;cursor:help}
.nlbox{margin-top:8px;font-size:.82rem;color:var(--muted);display:flex;flex-direction:column;gap:5px}
.nlbox b{font-family:var(--f-data);color:var(--ink);font-weight:500}
.meq .scenario{background:var(--surface-2);border-radius:8px;padding:13px 15px;margin-bottom:13px}
.meq ol.sub{padding-left:22px;margin:0;display:flex;flex-direction:column;gap:11px}
.meq .a{display:none;color:var(--ok);margin-top:5px;font-size:.92rem}
.item.show .a{display:block}
.note{font-size:.82rem;color:var(--muted);margin-top:8px;font-style:italic}
.toggle{margin-top:12px;font-size:.8rem;padding:5px 10px}
footer{color:var(--muted);font-size:.82rem;margin-top:30px;padding-top:16px;border-top:2px solid var(--ink);
 display:flex;flex-direction:column;gap:6px}
code{font-family:var(--f-data);font-size:.85em;background:var(--surface-2);padding:1px 5px;border-radius:4px}
a{color:var(--accent)}
.syslist{display:flex;flex-direction:column;gap:14px;margin-top:22px}
.syscard{display:block;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--accent);
 border-radius:10px;padding:17px 19px;text-decoration:none;color:inherit;box-shadow:var(--shadow)}
.syscard:hover{border-color:var(--accent)}
.syscard h2{margin:0 0 3px;font-size:1.1rem;font-weight:600}
@media (max-width:430px){.stat{padding-right:14px;margin-right:14px}.score{margin-left:0}}
@media print{
 .bar,.toggle{display:none}
 body{background:#fff;color:#000;font-size:11pt}
 .answer,.a{display:block !important}
 .item{break-inside:avoid;border-bottom:1px solid #bbb}
 ol.choices li{border-color:#ccc}
}
"""

JS = """
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
let revealed=false, tried=0, right=0;
function apply(){
  const lec=$('#lec').value, q=$('#q').value.trim().toLowerCase();
  let n=0;
  $$('.item').forEach(el=>{
    const show=(lec==='all'||el.dataset.lec===lec) && (!q||el.innerText.toLowerCase().includes(q));
    el.hidden=!show; if(show) n++;
  });
  $('#count').textContent=n;
}
function score(){ $('#score').innerHTML = tried ? 'ตอบแล้ว <b>'+tried+'</b> · ถูก <b>'+right+'</b> ('+Math.round(right/tried*100)+'%)' : 'ยังไม่ได้ตอบ'; }
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
      const ok=li.dataset.key==='1';
      li.classList.add(ok?'correct':'wrong');
      item.classList.add('show');
      tried++; if(ok) right++; score();
    }
    return;
  }
  const head=e.target.closest('[data-toggle]');
  if(head) head.closest('.item').classList.toggle('show');
});
document.addEventListener('DOMContentLoaded',()=>{
  $('#lec').addEventListener('change',apply);
  $('#q').addEventListener('input',apply);
  $('#reveal').addEventListener('click',toggleAll);
  $('#reset').addEventListener('click',()=>{
    $$('ol.choices li').forEach(li=>li.classList.remove('correct','wrong'));
    $$('.item').forEach(el=>el.classList.remove('show'));
    revealed=false; tried=0; right=0; score();
    $('#reveal').textContent='เปิดเฉลยทั้งหมด';
  });
  score(); apply();
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
    meta = ('<div class="meta"><span class="id">%s</span><span>%s</span>'
            '<span class="topic">%s</span><span class="lec">%s</span></div>'
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
            '<button class="toggle" data-toggle>เปิด/ปิดเฉลย</button></article>'
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

    return """<title>%(key_up)s Exam Drill</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Sans+Thai:wght@400;500;600&display=swap">
<style>%(css)s</style>
<div class="wrap">
<header class="hero">
  <div class="eyebrow">MED421 · %(key_up)s</div>
  <h1>%(name)s</h1>
  <div class="sub">%(name_th)s · ผูกเกณฑ์แพทยสภา พ.ศ. 2567 รายข้อ · build %(built)s</div>
</header>
<div class="stats">
  <div class="stat"><b>%(n_mcq)d</b>MCQ</div>
  <div class="stat"><b>%(n_meq)d</b>MEQ</div>
  <div class="stat"><b>%(n_lec)d</b>lecture</div>
  <div class="stat"><b>%(n_nl)d</b>หัวข้อ NL ที่ครอบคลุม</div>
</div>
<div class="bar">
  <select id="lec" aria-label="เลือก lecture"><option value="all">ทุก lecture</option>%(opts)s</select>
  <input id="q" type="search" placeholder="ค้นหาในโจทย์ เฉลย หรือ pearl">
  <button id="reveal" class="primary">เปิดเฉลยทั้งหมด</button>
  <button id="reset">ล้างคำตอบ</button>
  <span class="score" id="score"></span>
</div>
<div class="sub" style="margin:6px 0 4px">แสดง <b id="count">0</b> ข้อ — คลิกตัวเลือกเพื่อตอบ ระบบจะเฉลยและนับคะแนนให้</div>
%(body)s
<footer>
  <div>ชิป <span class="nlchip">NL …</span> คือรหัสหัวข้อตาม %(nlsrc)s (ชี้เมาส์เพื่อดูชื่อเต็ม)</div>
  <div>สร้างจาก med421-kit — แก้ข้อสอบที่ <code>%(file)s</code> แล้วสั่ง <code>python3 build.py %(key)s</code></div>
</footer>
</div>
<script>%(js)s</script>
""" % dict(name=esc(sysdef["name_en"]), name_th=esc(sysdef["name_th"]), course=esc(cfg["course"]),
           css=css, js=JS, opts=opts, body=body, built=date.today().isoformat(),
           n_mcq=n_mcq, n_meq=n_meq, n_lec=len(sysdef["lectures"]), n_nl=n_nl, key_up=esc(sysdef["key"].upper()),
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
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Sans+Thai:wght@400;500;600&display=swap">
<style>%(css)s</style>
<div class="wrap">
<header class="hero">
  <div class="eyebrow">คลังข้อสอบแยกตามระบบ</div>
  <h1>%(course)s</h1>
  <div class="sub">ผูกเกณฑ์แพทยสภา พ.ศ. 2567 รายข้อ · build %(built)s</div>
</header>
<div class="syslist">%(cards)s</div>
<footer><div>อ้างอิงเกณฑ์: %(nlsrc)s</div></footer>
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
