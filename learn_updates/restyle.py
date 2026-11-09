# -*- coding: utf-8 -*-
"""ปรับหน้า MED421 learn ให้ตรงกฎ study-page-design (สเกลตัวอักษร spacing radius น้ำหนัก ปุ่ม motion)
อ่านจากไฟล์ที่ได้จาก Artifact read แล้วเขียนเป็น learn_index.html"""
import re, sys
SRC, DST = sys.argv[1], sys.argv[2]
html = open(SRC, encoding="utf-8").read()

# ---------- 1. ฟอนต์: ตัด Noto Serif Thai (ไม่ได้ใช้) ใส่ Noto Sans Thai เป็นสำรอง
html = html.replace(
    "family=IBM+Plex+Sans+Thai:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Noto+Serif+Thai:wght@500;600;700&display=swap",
    "family=IBM+Plex+Sans+Thai:wght@400;500;600&family=Noto+Sans+Thai:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap")

# ---------- 2. ตัวแปรสี: palette ชั้นเดียว แล้วตั้งชื่อตามหน้าที่ · dark mode = สลับการอ้าง palette
start = html.index(":root{\n  --paper:#eef3f0;")
end = html.index("@keyframes rise")
TOKENS = """:root{
  /* palette — สีดิบ เขียนครั้งเดียว */
  --g-50:#eef3f0; --g-0:#ffffff; --g-100:#e3ebe6; --g-900:#0d1712; --g-700:#3d4c44; --g-500:#6d7f75; --g-200:#d8e2dc; --g-300:#bccbc3;
  --wine-700:#8c1d2f; --wine-50:#f6e9eb; --wine-800:#6e1624;
  --green-700:#0f7a4a; --green-50:#dff0e6; --amber-700:#9a5f08; --amber-50:#f8efdc; --red-700:#a3271f; --red-50:#f8e9e7; --blue-600:#1f6feb;
  --n-950:#090d0b; --n-900:#111915; --n-850:#18221d; --n-50:#e7f0ea; --n-300:#a5b8ac; --n-400:#788c80; --n-800:#1d2922; --n-700:#2a3830;
  --pink-300:#ff8fa3; --pink-950:#24151a; --pink-200:#ffb3c0; --mint-300:#5fe3a1; --mint-950:#0f2419; --gold-300:#e8bb63; --gold-950:#241f10;
  --coral-300:#e8877c; --coral-950:#2a1715; --sky-300:#7fb4ff;
  /* ชื่อตามหน้าที่ — โค้ดส่วนอื่นใช้แค่ชุดนี้ */
  --paper:var(--g-50); --surface:var(--g-0); --surface-sunk:var(--g-100);
  --ink:var(--g-900); --ink-2:var(--g-700); --ink-3:var(--g-500);
  --rule:var(--g-200); --rule-strong:var(--g-300);
  --accent:var(--wine-700); --accent-soft:var(--wine-50); --accent-ink:var(--wine-800); --on-accent:#ffffff;
  --ok:var(--green-700); --ok-soft:var(--green-50); --miss:var(--amber-700); --miss-soft:var(--amber-50);
  --bad:var(--red-700); --bad-soft:var(--red-50);
  --focus:var(--blue-600);
  --shadow:0 1px 2px rgba(13,23,18,.05),0 12px 28px -20px rgba(13,23,18,.3);
  /* สเกล (study-page-design) */
  --r-sm:6px; --r-md:10px; --r-lg:16px;
  --s-1:4px; --s-2:8px; --s-3:12px; --s-4:16px; --s-5:24px; --s-6:32px; --s-7:48px;
  --sans:"IBM Plex Sans Thai","Noto Sans Thai",system-ui,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,"SF Mono",Menlo,monospace;
  --serif:var(--sans);
  --e:cubic-bezier(.22,.9,.28,1);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:var(--n-950); --surface:var(--n-900); --surface-sunk:var(--n-850);
    --ink:var(--n-50); --ink-2:var(--n-300); --ink-3:var(--n-400); --rule:var(--n-800); --rule-strong:var(--n-700);
    --accent:var(--pink-300); --accent-soft:var(--pink-950); --accent-ink:var(--pink-200); --on-accent:#08110c;
    --ok:var(--mint-300); --ok-soft:var(--mint-950); --miss:var(--gold-300); --miss-soft:var(--gold-950);
    --bad:var(--coral-300); --bad-soft:var(--coral-950); --focus:var(--sky-300);
    --shadow:0 1px 2px rgba(0,0,0,.6),0 18px 40px -28px rgba(0,0,0,1);
  }
}
:root[data-theme="dark"]{
  --paper:var(--n-950); --surface:var(--n-900); --surface-sunk:var(--n-850);
  --ink:var(--n-50); --ink-2:var(--n-300); --ink-3:var(--n-400); --rule:var(--n-800); --rule-strong:var(--n-700);
  --accent:var(--pink-300); --accent-soft:var(--pink-950); --accent-ink:var(--pink-200); --on-accent:#08110c;
  --ok:var(--mint-300); --ok-soft:var(--mint-950); --miss:var(--gold-300); --miss-soft:var(--gold-950);
  --bad:var(--coral-300); --bad-soft:var(--coral-950); --focus:var(--sky-300);
  --shadow:0 1px 2px rgba(0,0,0,.6),0 18px 40px -28px rgba(0,0,0,1);
}
"""
html = html[:start] + TOKENS + html[end:]

# ---------- 3. แปลงค่าใน CSS ของหน้า (ไม่แตะตัวอักษรใน SVG แผนภาพ)
cs = html.index("<style>\n:root{\n  /* palette")
ce = html.index("</style>", cs)
css = html[cs:ce]

def fs(x):
    x = float(x)
    for lim, v in ((28, 30), (22, 24), (19, 20), (17, 18), (15, 16), (13, 14)):
        if x >= lim: return v
    return 12
SP = [0, 4, 8, 12, 16, 24, 32, 48]
def sp(x):
    x = float(x); s = -1 if x < 0 else 1
    return s * min(SP, key=lambda v: (abs(v - abs(x)), v))
def rad(x):
    x = float(x)
    if x >= 900: return "999px"
    if x <= 7: return "var(--r-sm)"
    if x <= 12: return "var(--r-md)"
    return "var(--r-lg)"

SVG_KEEP = (".fig svg text{", ".fig .lg{", ".fig .sm{", ".fig .xs{")
out = []
for line in css.split("\n"):
    if any(k in line for k in SVG_KEEP):
        out.append(line); continue
    # font-size:Npx
    line = re.sub(r"font-size:(\d+(?:\.\d+)?)px", lambda m: "font-size:%dpx" % fs(m.group(1)), line)
    # font shorthand: font:W Spx/LH
    def fshort(m):
        w, size, lh = m.group(1), m.group(2), m.group(3)
        w = "600" if w in ("700", "800") else w
        if lh == "1": lh = "1.3"
        return "font:%s %dpx/%s" % (w, fs(size), lh)
    line = re.sub(r"font:(\d{3}) (\d+(?:\.\d+)?)px/([\d.]+(?:px)?)", fshort, line)
    line = line.replace("font-weight:700", "font-weight:600")
    # padding / margin / gap
    def spfix(m):
        prop, val = m.group(1), m.group(2)
        if any(t in val for t in ("calc", "var(", "env(", "max(", "min(", "auto", "%")):
            return m.group(0)
        val = re.sub(r"(-?\d+(?:\.\d+)?)px", lambda n: "%dpx" % sp(n.group(1)) if sp(n.group(1)) else "0", val)
        return prop + ":" + val
    line = re.sub(r"\b((?:padding|margin)(?:-(?:top|bottom|left|right|block|inline))?|gap|row-gap|column-gap):([^;{}]+)", spfix, line)
    # border-radius
    def rfix(m):
        prop, val = m.group(1), m.group(2)
        if "var(" in val or "%" in val: return m.group(0)
        return prop + ":" + re.sub(r"(\d+(?:\.\d+)?)px", lambda n: rad(n.group(1)), val)
    line = re.sub(r"\b(border(?:-(?:top|bottom)-(?:left|right))?-radius):([^;{}]+)", rfix, line)
    # transitions 150–200ms
    if "transition" in line and ".anim svg" not in line:
        line = re.sub(r"\.(22|2|5)s", ".18s", line)
    out.append(line)
css = "\n".join(out)

# ค่าที่ต้องตั้งเฉพาะ
css = css.replace("line-height:1.64", "line-height:1.65")
css = css.replace(".card h2{font-size:clamp(22px,4.4vw,27px);margin:8px 0 4px;line-height:1.24}",
                  ".card h2{font-size:24px;margin:8px 0 8px;line-height:1.35}")
css = css.replace("padding:24px 24px;animation:rise .32s var(--e) both}", "padding:24px}")
css = css.replace(".ch.correct{border-color:var(--ok);background:var(--ok-soft);animation:pop .3s var(--e)}",
                  ".ch.correct{border-color:var(--ok);background:var(--ok-soft);animation:pop .18s var(--e)}")
css = css.replace("padding-inline:24px}", "padding-inline:24px}")  # no-op guard

OVERRIDES = """
/* ---------- study-page-design: ส่วนเสริมทับท้าย (9 พ.ย.) ---------- */
body{text-rendering:optimizeLegibility}
.prose p,.prose li,.lede,.explain,.stem{text-wrap:pretty}
h2,h3,h4,.card h2,.card h3{line-height:1.4}
.card h3{font-size:20px;margin:24px 0 8px}
.prose h4{font-size:18px;line-height:1.45;margin:24px 0 8px}
.qhead h3{font-size:20px}
.ltile b,.tile b{font-size:16px;line-height:1.4}
table,.timer,.olec .num,.q .qid,.ltile .lnum,.actl .dot,.nlbox li code,.ring{font-variant-numeric:tabular-nums}
/* ตัวอักษรเลือก A–E และหัวหลักจำเป็นป้ายกำกับ ไม่ใช่ตัวเลข → ใช้ฟอนต์หลัก */
.ch .k{font-family:var(--sans);font-weight:600;font-size:16px;line-height:1.65;flex:0 0 16px}
.mnem .mnh b{font-family:var(--sans);font-size:18px;line-height:1.45;letter-spacing:0}
.mnem li b{font-family:var(--sans)}
/* พื้นที่กดอย่างน้อย 44×44 */
.btn,.figq,.ai-hd button,.ai-quick button,.ai-in button,.a3dgo,.ai-fab{min-height:44px;display:inline-flex;align-items:center;justify-content:center;gap:var(--s-2)}
.btn{padding:var(--s-2) var(--s-4);border-radius:var(--r-md)}
.nav .btn{justify-content:flex-start}
#mastBtn,#asideBtn{padding:var(--s-2) var(--s-3)}
.tqbar .btn,.mnem .mnpin{padding:var(--s-1) var(--s-3);font-size:14px}
.olec>button,.osec li button{min-height:44px;align-items:center}
.osec li button .tick{margin-top:0}
.ch{min-height:44px}
.actl .ab{min-width:44px;height:44px}
.actl .dot{width:44px;height:44px;padding:8px;background-clip:content-box;line-height:26px;font-size:12px}
.ai-sel{min-height:44px;padding:var(--s-2) var(--s-3)}
.tick{flex:0 0 16px;height:16px;font:600 12px/14px var(--sans)}
/* state ครบ: hover กด focus disabled กำลังโหลด */
.btn:focus-visible,.ch:focus-visible,.tile:focus-visible,.ltile:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
.btn:disabled,.btn[aria-disabled="true"]{opacity:.5;cursor:not-allowed;transform:none}
.btn[aria-busy="true"]{cursor:progress;opacity:.75}
.btn[aria-busy="true"]::after{content:"";width:14px;height:14px;border:2px solid currentColor;border-right-color:transparent;border-radius:999px;animation:spin .8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.btn.primary:hover{filter:brightness(1.08);background:var(--accent);color:var(--on-accent)}
.btn.on:hover{background:var(--accent);color:var(--on-accent)}
/* การ์ดไม่เล่นอนิเมชันตอนแสดง — อ่านได้ทันที */
.card{animation:none}
main{gap:var(--s-4)}
@media (max-width:560px){.card{padding:var(--s-4);border-radius:var(--r-lg)}}
/* ชื่อชุดบนมือถือไม่ให้ปุ่มทับ — ตัดเป็น … แทน */
.brand{min-width:0}.brand b{overflow:hidden;text-overflow:ellipsis;min-width:0}
@media (min-width:900px){.brand b{flex:none}}
@media (max-width:560px){.brand span{display:none}}
/* ลิงก์ชิปที่กดได้ต้องสูง 44 */
.meta a.chip{min-height:44px;display:inline-flex;align-items:center;padding:0 var(--s-3)}
"""
css = css + OVERRIDES
html = html[:cs] + css + html[ce:]

# ---------- 4. JS: ปุ่ม primary หนึ่งปุ่มต่อการ์ด
# หน้าหัวข้อ: ปุ่ม "ทำเครื่องหมายว่าเรียนแล้ว" เป็นปุ่มรอง ให้ปุ่มไปหัวข้อถัดไปเป็นปุ่มหลักปุ่มเดียว
old = "\"<button class='btn \"+(st.complete?\"\":\"primary\")+\"' data-act='markread'>\""
assert old in html
html = html.replace(old, "\"<button class='btn' data-act='markread' aria-pressed='\"+(state.done[s.id]?\"true\":\"false\")+\"'>\"")
# MEQ: ปุ่ม "ดูแนวคำตอบ" มีหลายข้อในการ์ดเดียว → ปุ่มรองทั้งหมด
old = "\"<div class='nav' style='margin-top:9px'><button class='btn\"+(open?\"\":\" primary\")+\"' data-reveal='\"+esc(kid)+\"'>\""
assert old in html
html = html.replace(old, "\"<div class='nav' style='margin-top:8px'><button class='btn' data-reveal='\"+esc(kid)+\"' aria-expanded='\"+(open?\"true\":\"false\")+\"'>\"")
# ระยะใน style inline ให้อยู่ในสเกล
html = html.replace("style='margin-top:14px'", "style='margin-top:16px'").replace("style='margin-top:10px'", "style='margin-top:12px'")

open(DST, "w", encoding="utf-8").write(html)
print("ok", len(html))
