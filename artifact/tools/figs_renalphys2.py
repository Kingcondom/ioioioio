# -*- coding: utf-8 -*-
"""ภาพประกอบคาบ nephro "Physio2" — สรีรวิทยาไตพื้นฐาน II (Watchara Chongsa, PhD) — ใช้ใน build_renalphys2.py

ทุกฟังก์ชันคืน fig(title, cap, svg) · กว้าง ≤ 420 · ภาพเซลล์/อวัยวะเป็นแผนผัง ไม่ใช่สัดส่วนจริง"""
from svg import *


def _blunt(x1, y1, x2, y2, c="lok w2"):
    """เส้นยับยั้ง (ปลายเป็นขีดตั้งฉาก)"""
    import math
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L * 7, dx / L * 7
    return line(x1, y1, x2, y2, c) + line(x2 - nx, y2 - ny, x2 + nx, y2 + ny, c)


def _segbar(rows, segs, x0=70, y0=30, scale=3.3, bh=26, gap=16, lab_w=60):
    """แถบซ้อนแนวนอน (ร้อยละ) — rows = [(ชื่อแถว, [ค่าแต่ละ seg], [ป้ายแต่ละ seg หรือ None])]"""
    out = []
    y = y0
    for name, vals, labs in rows:
        out.append(t(x0 - 8, y + bh / 2 + 4, name, "sm b end"))
        x = x0
        for (sname, cls), v, lab in zip(segs, vals, labs):
            if v <= 0:
                continue
            w = v * scale
            out.append(rect(x, y, w, bh, cls, 3))
            if lab and w >= 22:
                out.append(t(x + w / 2, y + bh / 2 + 4, lab, "xs b mid"))
            x += w
        y += bh + gap
    return out, y


# ═══════════════════════════════════════ 1 osmolarity → น้ำเคลื่อนเข้า/ออกเซลล์
def osm():
    out = []
    panels = [("ECF isotonic", "~285 mOsm", "sk", 32, 0, "เซลล์ปกติ", ""),
              ("ECF hypertonic", "↑Na · ↑glucose", "ms", 23, -1, "เซลล์เหี่ยว", "cell dehydration"),
              ("ECF hypotonic", "↓Na (น้ำเกิน)", "wa", 40, 1, "เซลล์บวม", "cell edema")]
    for i, (name, sub, cls, r, d, res, res2) in enumerate(panels):
        x0 = 8 + i * 138
        cx, cy = x0 + 64, 114
        out += [rect(x0, 30, 128, 150, cls, 10), t(cx, 48, name, "sm b mid"), t(cx, 63, sub, "xs mid i2")]
        if d:
            out.append(circ(cx, cy, 32, "lmu da"))
        out += [circ(cx, cy, r, "bx"), t(cx, cy + 4, "ICF", "xs b mid")]
        if d < 0:   # น้ำออก
            for ang in (0, 1, 2, 3):
                import math
                a = math.pi / 4 + ang * math.pi / 2
                out.append(ar(cx + (r + 2) * math.cos(a), cy + (r + 2) * math.sin(a),
                              cx + (r + 18) * math.cos(a), cy + (r + 18) * math.sin(a), "lwa w2", "ah-wa"))
        if d > 0:   # น้ำเข้า
            for ang in (0, 1, 2, 3):
                import math
                a = math.pi / 4 + ang * math.pi / 2
                out.append(ar(cx + (r + 17) * math.cos(a), cy + (r + 17) * math.sin(a),
                              cx + (r + 3) * math.cos(a), cy + (r + 3) * math.sin(a), "lwa w2", "ah-wa"))
        out += [t(cx, 196, res, "sm b mid" + (" tbad" if d else "")), t(cx, 210, res2, "xs mid mu")]
    out += [rect(8, 222, 404, 64, "ac", 9),
            t(20, 242, "Posm = 2[Na] + glucose/18 + BUN/2.8", "sm b"),
            t(20, 260, "Tonicity (effective) = 2[Na] + glucose/18", "sm b tac"),
            t(20, 277, "urea ผ่านเยื่อหุ้มเซลล์ได้ → นับใน Posm แต่ไม่ดึงน้ำ", "xs i2")]
    return fig("น้ำเคลื่อนตาม tonicity ของ ECF — เซลล์เหี่ยวหรือบวม",
               "เยื่อหุ้มเซลล์ให้น้ำผ่านได้อิสระแต่กั้น Na และ glucose ไว้ น้ำจึงไหลจากฝั่งที่ osmolarity ต่ำไปฝั่งที่สูงจนสองฝั่งเท่ากัน · ECF **hypertonic** (Na หรือ glucose สูง) → น้ำออกจากเซลล์ → **เซลล์เหี่ยว** · ECF **hypotonic** (น้ำเกินเมื่อเทียบกับ Na) → น้ำเข้าเซลล์ → **เซลล์บวม** — สมองอยู่ในกะโหลกจึงทนบวมได้น้อยที่สุด · **urea** ผ่านเยื่อได้ จึงเพิ่ม Posm ที่วัดได้ (เช่นในไตวาย) แต่ไม่ทำให้น้ำเคลื่อน = ไม่เพิ่ม tonicity และไม่กระตุ้น ADH",
               svg(420, 294, "ผลของ ECF ที่ isotonic hypertonic และ hypotonic ต่อขนาดเซลล์ พร้อมสูตร plasma osmolarity", *out))


# ═══════════════════════════════════════ 2 Darrow–Yannet
def darrow():
    out = [t(10, 16, "แกนนอน = ปริมาตร · แกนตั้ง = osmolarity · เส้นประ = ค่าปกติ", "xs mu"),
           rect(300, 7, 12, 11, "wa", 2), t(316, 16, "ICF", "xs b"), rect(346, 7, 12, 11, "ok", 2), t(362, 16, "ECF", "xs b")]
    rows = [("ปริมาตรลด (contraction)", [
        ("Isosmotic", 66, 22, 50, 0, "diarrhea · burn · เลือดออก"),
        ("Hyperosmotic", 56, 26, 60, 1, "เหงื่อ · ขาดน้ำ · DI"),
        ("Hyposmotic", 72, 16, 42, -1, "adrenal insufficiency")]),
            ("ปริมาตรเกิน (expansion)", [
        ("Isosmotic", 66, 44, 50, 0, "ให้ 0.9% NaCl มาก"),
        ("Hyperosmotic", 58, 46, 60, 1, "เกลือมาก · 3% NaCl"),
        ("Hyposmotic", 74, 38, 42, -1, "ดื่มน้ำมาก · SIADH")])]
    for r, (rname, panels) in enumerate(rows):
        y0 = 28 + r * 148
        out.append(t(10, y0 + 8, rname, "sm b tac"))
        for i, (nm, wi, we, h, shift, ex) in enumerate(panels):
            x0 = 8 + i * 138
            xl, yb = x0 + 16, y0 + 104
            out += [rect(x0, y0 + 14, 128, 128, "bx", 9), t(x0 + 64, y0 + 30, nm, "sm b mid")]
            out += [rect(xl, yb - h, wi, h, "wa", 2), rect(xl + wi, yb - h, we, h, "ok", 2),
                    rect(xl, yb - 50, 66, 50, "lmu da", 0), rect(xl + 66, yb - 50, 34, 50, "lmu da", 0)]
            if shift:
                xb, yy = xl + wi, yb - h / 2 - 4
                if shift > 0:
                    out.append(ar(xb - 16, yy, xb + 12, yy, "lbad w3", "ah-bad"))
                else:
                    out.append(ar(xb + 12, yy, xb - 16, yy, "lbad w3", "ah-bad"))
            out.append(t(x0 + 64, y0 + 122, ex, "xs mid i2"))
            out.append(t(x0 + 64, y0 + 136, {1: "น้ำออกจากเซลล์", -1: "น้ำเข้าเซลล์", 0: "น้ำไม่ย้าย"}[shift],
                         "xs b mid" + ("" if shift == 0 else " tbad")))
    return fig("Darrow–Yannet diagram — 6 แบบของการเสียสมดุลปริมาตร",
               "ดูสองอย่างเสมอ: **ECF เปลี่ยนปริมาตรไปทางไหน** และ **osmolarity ของ ECF เปลี่ยนหรือไม่** — ถ้า osmolarity ไม่เปลี่ยน (isosmotic) น้ำไม่ย้ายเข้า/ออกเซลล์ ICF คงเดิม · ถ้า ECF เข้มขึ้น (hyperosmotic) น้ำออกจากเซลล์ ICF หด · ถ้า ECF จางลง (hyposmotic) น้ำเข้าเซลล์ ICF บวม · ภาวะที่อันตรายต่อสมองคือแบบ hyper/hyposmotic เพราะเซลล์สมองเปลี่ยนขนาด (สไลด์ Types of volume deficit/excess · Costanzo Table 6.2)",
               svg(420, 326, "Darrow-Yannet diagram หกแบบ: ขาดและเกินแบบ isosmotic hyperosmotic hyposmotic", *out))


# ═══════════════════════════════════════ 3 การดูด Na กลับในแต่ละส่วน (ตามความดัน)
def na_segments():
    segs = [("PT", "ac"), ("TAL", "ok"), ("DT", "wa"), ("CD", "ms"), ("ขับทิ้ง", "bad")]
    rows = [("ปกติ", [65, 25, 5, 3, 2], ["65%", "25%", "5", "3", None]),
            ("BP ต่ำ", [80, 15, 3, 2, 0], ["80%", "15%", "3", "", None]),
            ("BP สูง", [50, 30, 12, 2, 6], ["50%", "30%", "12%", "", "6"])]
    out, y = _segbar(rows, segs, x0=70, y0=28, scale=3.3)
    out.insert(0, t(10, 16, "สัดส่วนของ Na ที่กรองแล้ว ถูกดูดกลับที่แต่ละส่วน (สไลด์ Glomerulotubular balance)", "xs mu"))
    out += [t(70 + 98 * 3.3 + 4, 28 + 13 + 4, "<1%", "xs b tbad"), t(70 + 100 * 3.3 + 4, 70 + 13 + 4, "0%", "xs b tbad")]
    lx = 70
    for nm, c in segs:
        out += [rect(lx, y + 2, 14, 12, c, 2), t(lx + 18, y + 12, nm, "xs")]
        lx += 62
    out += [rect(10, y + 24, 400, 46, "sk", 8),
            t(20, y + 42, "BP ต่ำ → PT ดูดเพิ่มเป็น 80% → ขับทิ้ง ~0 (เก็บ volume)", "xs"),
            t(20, y + 60, "BP สูง → PT ดูดลดเหลือ 50% → ขับทิ้ง 6% = pressure natriuresis", "xs")]
    return fig("ร่างกายปรับการขับ Na ด้วยการเปลี่ยนสัดส่วนการดูดกลับที่ proximal tubule",
               "GFR ถูก autoregulation ตรึงไว้เมื่อ MAP อยู่ราว 80–170 mmHg ไตจึงคุมการขับ Na ด้วย **การดูดกลับ** มากกว่าการกรอง · เมื่อความดัน/ปริมาตรต่ำ ระบบ sympathetic และ angiotensin II ทำให้ proximal tubule ดูด Na กลับมากขึ้นจน **แทบไม่มี Na ออกในปัสสาวะ** · เมื่อความดันสูง PT ดูดน้อยลง Na ที่ล้นไปส่วนปลายเกินกำลังดูด → **ขับ Na ทิ้ง (pressure natriuresis)** · ตัวเลขจากสไลด์ (ปัดเศษ — ส่วนปกติรวมได้ ~98% + ขับทิ้ง < 1%)",
               svg(420, y + 78, "แถบแสดงร้อยละการดูด Na กลับในแต่ละส่วนของ nephron ที่ความดันปกติ ต่ำ และสูง", *out))


# ═══════════════════════════════════════ 4 FF → Starling ของ peritubular capillary
def ff():
    L = ["↓ blood volume / BP", "↑ sympathetic + Ang II", "efferent หดมากกว่า afferent\nGFR ลดนิด · RPF ลดมาก",
         "FF = GFR/RPF ↑", "เลือดที่ออกจาก glomerulus:\nPc ↓ · πc ↑ (โปรตีนเข้มข้น)", "peritubular capillary ดูด\nน้ำ+Na จาก PT มากขึ้น",
         "↓ ขับ Na (เก็บ volume)"]
    R = ["↑ blood volume / BP", "↓ sympathetic + Ang II\n↑ ANP", "afferent ขยาย\nGFR ↑นิด · RPF ↑ มาก",
         "FF ↓", "Pc ↑ · πc ↓", "PT ดูดกลับน้อยลง\n(back-leak เพิ่ม)", "↑ ขับ Na\n(pressure natriuresis)"]
    out = [t(105, 16, "ปริมาตรลด", "sm b mid tbad"), t(315, 16, "ปริมาตรเกิน", "sm b mid twa")]
    y = 24
    for i in range(7):
        h = 40 if ("\n" in L[i] or "\n" in R[i]) else 30
        cl = "bad" if i in (0, 6) else "bx"
        cr = "wa" if i in (0, 6) else "bx"
        out += [box(10, y, 190, h, cl, L[i], fs=11), box(220, y, 190, h, cr, R[i], fs=11)]
        if i < 6:
            out += [ar(105, y + h, 105, y + h + 10, "ln", "ah"), ar(315, y + h, 315, y + h + 10, "ln", "ah")]
        y += h + 12
    return fig("Filtration fraction ควบคุมแรง Starling ที่ peritubular capillary",
               "เลือดที่ไหลออกจาก glomerulus ผ่าน efferent arteriole ไปเป็น peritubular capillary รอบ proximal tubule · เมื่อ **FF สูง** (กรองน้ำออกไปมาก) เลือดที่เหลือ **โปรตีนเข้มข้น (πc ↑) และความดันต่ำ (Pc ↓ เพราะ efferent หด)** จึงดูดน้ำและ Na จาก interstitium กลับเข้าหลอดเลือดได้ดี → PT ดูดกลับมากขึ้น · ปริมาตรเกินทำตรงข้าม → Na ที่ถูกขนออกจากเซลล์รั่วกลับเข้าท่อ (back-leak) → ขับ Na มากขึ้น · นี่คือกลไกหนึ่งของ **glomerulotubular balance** (ทบทวน GFR/RBF ใน Part I)",
               svg(420, y + 4, "ห่วงโซ่จากปริมาตรเลือดถึงการดูด Na กลับที่ proximal tubule ผ่าน filtration fraction", *out))


# ═══════════════════════════════════════ 5 RAAS
def raas():
    out = [box(10, 8, 186, 58, "bad", "↓ BP / ↓ ECF volume\n↓ NaCl ถึง macula densa\n↑ sympathetic (β1)", fs=11),
           box(232, 16, 178, 42, "ac", "JG cell หลั่ง renin", fs=12),
           ar(196, 37, 230, 37, "lac w2", "ah-ac"),
           box(10, 82, 120, 36, "sk", "angiotensinogen\n(ตับ)", fs=11),
           box(176, 82, 72, 36, "sk", "Ang I", fs=12),
           box(296, 82, 114, 36, "bad", "Ang II", tc="b", fs=14),
           ar(130, 100, 174, 100, "ln", "ah", "renin", "xs i2 mid"),
           ar(248, 100, 294, 100, "ln", "ah", "ACE", "xs i2 mid"),
           path("M353 118 L353 128 L150 128 L150 330", "lbad w2")]
    eff = [("หลอดเลือดแดงทั่วตัวหดตัว → ↑ BP", "bx"),
           ("efferent หดมากกว่า → รักษา GFR · ↑ FF", "bx"),
           ("PT: ↑ NHE3 → ดูด Na + HCO3 กลับ", "bx"),
           ("adrenal → aldosterone → P cell\n↑ ดูด Na · ↑ ขับ K · (A-IC ↑ ขับ H)", "ms"),
           ("hypothalamus → ↑ ADH + กระหายน้ำ", "wa")]
    y = 138
    for s, c in eff:
        h = 40 if "\n" in s else 32
        out += [box(168, y, 242, h, c, s, fs=11), ar(150, y + h / 2, 166, y + h / 2, "lbad", "ah-bad")]
        y += h + 8
    out += [box(10, 150, 122, 58, "ok", "ANP (atrium ยืด)\nยับยั้ง renin\naldo · ADH", fs=11),
            _blunt(132, 179, 148, 179, "lok w3"),
            box(10, 264, 122, 42, "ms", "↑ K+ ในเลือด\nกระตุ้นโดยตรง", fs=11),
            ar(132, 285, 166, 285, "lms w2", "ah-ms"),
            box(10, y + 4, 400, 34, "ok", "ผลรวม: เก็บ Na + น้ำ → ECF/BP กลับมา → renin ลด (negative feedback)", fs=11)]
    return fig("Renin–angiotensin–aldosterone system — ตัวรักษาปริมาตร ECF",
               "ตัวกระตุ้น renin สามทาง: **ความดันที่ afferent arteriole ลด** · **NaCl ที่ไปถึง macula densa ลด** · **sympathetic (β1) ที่ JG cell** · Ang II ทำหลายจุดพร้อมกันให้ร่างกาย **เก็บ Na และน้ำ** และพยุงความดัน · aldosterone ยังถูกกระตุ้นโดยตรงจาก **K ในเลือดสูง** (จึงเป็นทั้งฮอร์โมนปริมาตรและฮอร์โมนคุม K) · **ANP** จากหัวใจห้องบนที่ถูกยืดเป็นเบรกของทั้งระบบ · ยา ACEi/ARB/spironolactone ตัดวงจรนี้ จึงทำให้ K สูงได้",
               svg(420, y + 46, "แผนภาพระบบ renin angiotensin aldosterone พร้อมผลของ angiotensin II และตัวยับยั้ง ANP", *out))


# ═══════════════════════════════════════ 6 ADH → AQP2 ใน principal cell
def adh():
    out = [rect(10, 30, 84, 190, "wa", 6), t(52, 22, "lumen", "sm b mid"), t(52, 48, "ปัสสาวะ", "xs mid i2"),
           rect(102, 30, 200, 190, "bx", 12), t(202, 22, "principal cell (late DT/CD)", "xs b mid"),
           rect(310, 30, 100, 190, "ms", 6), t(360, 22, "interstitium", "sm b mid"), t(360, 48, "medulla", "xs mid i2"),
           t(360, 62, "~1,200 mOsm", "xs b mid"),
           # V2R + ADH
           rect(296, 92, 14, 22, "acf", 3), t(330, 128, "V2R", "xs b mid tac"),
           ar(400, 103, 314, 103, "lac w2", "ah-ac"), t(372, 96, "ADH", "sm b mid tac"),
           box(186, 84, 96, 40, "ac", "Gs → cAMP\n→ PKA", fs=11), ar(294, 103, 284, 103, "lac", "ah-ac"),
           # vesicles
           circ(150, 140, 10, "wa"), circ(174, 148, 10, "wa"), circ(156, 164, 10, "wa"),
           t(190, 158, "ถุง AQP2", "xs i2"),
           ar(212, 124, 182, 138, "lac", "ah-ac"),
           ar(146, 172, 110, 186, "lac w2", "ah-ac"),
           # channels
           rect(98, 188, 8, 18, "waf", 2), t(110, 216, "AQP2", "xs b twa"),
           rect(298, 188, 8, 18, "waf", 2), t(294, 216, "AQP3/4", "xs b end twa"),
           ar(22, 197, 92, 197, "lwa w3", "ah-wa", "H2O", "xs b mid twa"),
           ar(112, 197, 290, 197, "lwa w3", "ah-wa"),
           ar(310, 197, 380, 197, "lwa w3", "ah-wa", "H2O", "xs b mid twa"),
           box(10, 232, 196, 50, "ok", "TAL: ↑ NKCC2\n→ ↑ ความเข้มข้นใน medulla", fs=11),
           box(214, 232, 196, 50, "ok", "IMCD: ↑ UT-A1 ดูด urea\n→ ↑ osm ของ inner medulla", fs=11)]
    return fig("ADH เปิด “ประตูน้ำ” aquaporin-2 ที่ท่อรวม",
               "ADH จับ **V2 receptor** ด้าน basolateral → Gs → cAMP → PKA → ถุงที่บรรจุ **aquaporin-2** ถูกส่งไปแทรกที่ผนังด้าน lumen · น้ำจึงไหลตาม gradient จากปัสสาวะผ่านเซลล์ออกทาง AQP3/4 สู่ medulla ที่เข้มข้นสูง → ปัสสาวะเข้มข้น ปริมาณน้อย · ไม่มี ADH → AQP2 ถูกดึงกลับเข้าเซลล์ → ท่อรวมไม่ให้น้ำผ่าน → ปัสสาวะเจือจาง · ADH ยังเพิ่ม NaCl ที่ TAL และ urea ที่ inner medullary CD เพื่อ **สร้าง gradient** ให้ดูดน้ำได้ (สไลด์ ADH affecting on renal tubule) · ADH ขนาดสูงจับ V1R ที่หลอดเลือด → หดตัว (vasopressin)",
               svg(420, 290, "กลไก ADH ผ่าน V2 receptor cAMP และการแทรก aquaporin-2 ใน principal cell", *out))


# ═══════════════════════════════════════ 7 ADH vs Posm และผลของปริมาตร
def adh_curve():
    X = lambda p: 60 + (p - 270) * 9.6      # 270–305
    Y = lambda a: 210 - a * 17               # 0–10 pg/mL
    out = [rect(X(285), Y(10.4), X(295) - X(285), Y(0) - Y(10.4), "ok", 0),
           t((X(285) + X(295)) / 2, Y(10.4) - 5, "Posm ปกติ 285–295", "xs b mid tok"),
           line(60, 210, 400, 210, "ln"), line(60, 210, 60, 28, "ln")]
    for p in range(270, 306, 5):
        out += [line(X(p), 210, X(p), 214, "ln"), t(X(p), 226, str(p), "xs mid")]
    for a in (0, 5, 10):
        out += [t(54, Y(a) + 4, str(a), "xs end")]
    out += [t(230, 244, "plasma osmolality (mOsm/kg)", "xs mid i2"), t(14, 24, "ADH (pg/mL)", "xs i2")]
    out += [path("M%s %s L%s %s L%s %s" % (X(270), Y(0), X(280), Y(0), X(300), Y(10)), "lac w3"),
            path("M%s %s L%s %s L%s %s" % (X(270), Y(0.6), X(273), Y(0.8), X(290), Y(10.4)), "lbad w2 da"),
            path("M%s %s L%s %s" % (X(286), Y(0), X(305), Y(7.6)), "lwa w2 da"),
            t(X(271), Y(8.2), "volume ลด:", "xs b tbad"), t(X(271), Y(8.2) + 13, "เกณฑ์ต่ำลง ชันขึ้น", "xs tbad"),
            t(X(300) + 6, Y(10) + 10, "ปกติ", "xs b tac"),
            t(X(305), Y(3), "volume เกิน", "xs b end twa"),
            line(X(295), 40, X(295), 210, "lms da"), t(X(295) + 4, 204, "กระหายน้ำ", "xs b tms"),
            ]
    return fig("ADH ตอบสนองต่อ osmolality อย่างไว — แต่ปริมาตรที่ลดมากชนะได้",
               "osmoreceptor ใน hypothalamus ไวมาก: Posm เปลี่ยนเพียง 1–2% ADH ก็เปลี่ยนชัด · ต่ำกว่า ~275 mOsm ไม่หลั่ง ADH (สไลด์) ช่วงปกติ 285–295 · **การกระหายน้ำเริ่มที่เกณฑ์สูงกว่า ADH เล็กน้อย** (~295) ไตจึงเก็บน้ำก่อน แล้วค่อยหาน้ำเพิ่ม · baroreceptor/volume receptor ไวน้อยกว่า (ต้องลดราว 5–10%) แต่เมื่อปริมาตรลดมาก **เส้นจะเลื่อนซ้ายและชันขึ้น** — ร่างกายยอมเก็บน้ำแม้ Na ต่ำ = กลไกของ hyponatremia ใน hypovolemia, หัวใจวาย, ตับแข็ง (เส้นเป็นแผนภาพ อิง Robertson/Guyton — ส่วนเกณฑ์กระหายและเส้นปริมาตรไม่อยู่ในสไลด์)",
               svg(420, 254, "กราฟ ADH ในพลาสมาเทียบ osmolality และการเลื่อนของเส้นเมื่อปริมาตรลดหรือเกิน", *out))


# ═══════════════════════════════════════ 8 ปริมาณปัสสาวะ = ภาระ osmole / Uosm
def urine_vol():
    X = lambda u: 60 + u * 0.28           # 0–1200
    Y = lambda v: 220 - v * 15            # 0–12 L
    out = [line(60, 220, 400, 220, "ln"), line(60, 220, 60, 30, "ln")]
    for u in (50, 290, 600, 1200):
        out += [line(X(u), 220, X(u), 224, "ln"), t(X(u), 236, str(u), "xs mid")]
    for v in (0, 4, 8, 12):
        out += [t(54, Y(v) + 4, str(v), "xs end")]
    out += [t(230, 254, "urine osmolality (mOsm/kg)", "xs mid i2"), t(14, 24, "ปัสสาวะ (L/วัน)", "xs i2")]
    pts = [(u, 600 / u) for u in (50, 60, 75, 100, 150, 200, 300, 450, 600, 900, 1200)]
    out.append(poly([(X(u), Y(v)) for u, v in pts], "lac w3"))
    pts2 = [(u, 250 / u) for u in (50, 60, 75, 100, 150, 200, 300, 600, 1200)]
    out.append(poly([(X(u), Y(v)) for u, v in pts2], "lms w2 da"))
    out += [line(X(290), 30, X(290), 220, "lmu da"), t(X(290) + 4, 160, "= Posm", "xs mu"),
            circ(X(50), Y(12), 4, "badf"), t(X(50) + 8, Y(12) + 4, "ADH = 0: ~12 L (600 mOsm)", "xs b tbad"),
            circ(X(1200), Y(0.5), 4, "acf"), t(X(1200) - 4, Y(0.5) - 10, "ADH สูงสุด: 0.5 L", "xs b end tac"),
            circ(X(50), Y(5), 4, "msf"), t(122, 140, "← solute น้อย 250 mOsm: ขับได้แค่ ~5 L", "xs b tms"),
            t(390, 120, "ภาระ 600 mOsm/วัน", "xs end tac"), t(390, 134, "(อาหารปกติ)", "xs end mu")]
    return fig("ไตขับน้ำได้เท่าไร — ปริมาณปัสสาวะ = ภาระ osmole ÷ ความเข้มข้นของปัสสาวะ",
               "ทุกวันต้องขับ osmole (urea + เกลือ) ราว **600 mOsm** · ถ้า ADH สูงสุด ปัสสาวะเข้มได้ ~1,200 mOsm/kg → ต้องใช้น้ำเพียง **0.5 L** (obligatory urine volume) · ถ้า ADH เป็นศูนย์ ปัสสาวะจางสุด ~50 → ขับน้ำได้ถึง ~12 L/วัน (Guyton ระบุได้ถึง ~20 L ถ้า solute มาก) · **คนที่กินแต่เบียร์หรือข้าวกับชา** ได้ solute เพียง ~250 mOsm → แม้ปัสสาวะจางสุดก็ขับน้ำได้แค่ ~5 L ดื่มเกินนี้ Na จะตก (beer potomania) · ตัวเลขเป็นค่าประมาณจากตำรา ไม่อยู่ในสไลด์",
               svg(420, 262, "กราฟปริมาณปัสสาวะต่อวันเทียบ urine osmolality ที่ภาระ solute 600 และ 250 mOsm", *out))


# ═══════════════════════════════════════ 9 SIADH
def siadh():
    steps = [("ADH หลั่งไม่หยุด แม้ Posm ต่ำ\n(มะเร็งปอด small cell · ยา · โรคปอด/สมอง · ปวด/คลื่นไส้)", "bad"),
             ("AQP2 เปิดค้าง → เก็บ \"น้ำเปล่า\" → Na ในเลือดเจือจาง", "wa"),
             ("น้ำกระจาย 2/3 เข้าเซลล์ → ECF ขยายเพียงเล็กน้อย → ไม่บวม", "bx"),
             ("ตัวรับปริมาตรเห็น ECF เกินนิด: ↑ ANP · ↓ renin/aldo · ↑ GFR", "ok"),
             ("ไตขับ Na ทิ้ง (UNa > 30) → ECF กลับเกือบปกติ แต่ Na ยังต่ำ", "ms"),
             ("ผล: euvolemic hyponatremia · Uosm > 100 · UNa > 30\nuric acid/BUN ต่ำ (GFR ↑ และขับเพิ่ม)", "ac")]
    out = []
    y = 8
    for i, (s, c) in enumerate(steps):
        h = 42 if "\n" in s else 30
        out.append(box(10, y, 400, h, c, s, fs=11))
        if i < len(steps) - 1:
            out.append(ar(210, y + h, 210, y + h + 10, "ln", "ah"))
        y += h + 12
    return fig("SIADH — ทำไม Na ต่ำ ปริมาตรปกติ แต่ปัสสาวะยังมี Na มาก",
               "ต้นเหตุคือ **น้ำเกิน ไม่ใช่ Na ขาด**: ADH ที่หลั่งไม่เหมาะสมทำให้ไตเก็บน้ำเปล่า · น้ำที่เก็บไว้ 2 ใน 3 เข้าไปในเซลล์ ECF จึงขยายไม่มากพอจะบวม · แต่ ECF ที่เกินเล็กน้อยก็พอให้ **ANP เพิ่ม RAAS ลด GFR เพิ่ม** → ไตขับ Na ออกทางปัสสาวะ (UNa สูง) — ร่างกายเสีย Na เพื่อรักษาปริมาตร ผลคือ Na ต่ำลงอีก · ต่างจาก hyponatremia จาก **ปริมาตรลด** (อาเจียน/ท้องเสีย) ที่ไตเก็บ Na เต็มที่ (UNa < 20) · การให้ 0.9% NaCl ใน SIADH จึงมักไม่ช่วย: Na ถูกขับทิ้ง น้ำถูกเก็บ (ส่วนนี้เติมจากตำรา — สไลด์มีเพียง SIADH = hyposmotic volume expansion)",
               svg(420, y, "ห่วงโซ่กลไกของ SIADH ที่ทำให้ hyponatremia แบบปริมาตรปกติและ urine sodium สูง", *out))


# ═══════════════════════════════════════ 10 สมองปรับตัว + osmotic demyelination
def ods():
    P = [("ปกติ", 26, "bx", "", ""),
         ("Na ตกเร็ว\n(< 48 ชม.)", 38, "wa", "น้ำเข้าเซลล์", "สมองบวม · ชัก"),
         ("ปรับตัว\n(> 48 ชม.)", 28, "bx", "ขับ K, Cl,", "osmolyte ออก"),
         ("แก้ Na เร็ว\nเกินไป", 17, "bad", "น้ำออกจากเซลล์", "→ ODS (pons)")]
    out = []
    for i, (nm, r, c, a, b) in enumerate(P):
        cx = 54 + i * 104
        out += [t(cx, 18, nm, "sm b mid"), rect(cx - 50, 44, 100, 104, "sk", 14)]
        if i:
            out.append(circ(cx, 96, 26, "lmu da"))
        out += [circ(cx, 96, r, c)]
        if i == 1:
            out += [ar(cx - 49, 96, cx - 40, 96, "lwa w2", "ah-wa"), ar(cx + 49, 96, cx + 40, 96, "lwa w2", "ah-wa")]
        if i == 3:
            out += [ar(cx - 18, 96, cx - 40, 96, "lbad w2", "ah-bad"), ar(cx + 18, 96, cx + 40, 96, "lbad w2", "ah-bad")]
        if i == 2:
            out += [ar(cx, 70, cx, 52, "lms w2", "ah-ms")]
        out += [t(cx, 164, a, "xs mid i2"), t(cx, 177, b, "xs b mid" + (" tbad" if i == 3 else ""))]
    out += [rect(10, 190, 400, 66, "ms", 9),
            t(20, 210, "ขีดจำกัดการแก้ hyponatremia เรื้อรัง (European guideline 2014):", "xs b"),
            t(20, 228, "เพิ่ม Na ไม่เกิน 10 mmol/L ใน 24 ชม.แรก และ 8 mmol/L ในแต่ละ 24 ชม.ถัดไป", "xs"),
            t(20, 246, "อาการรุนแรง: 3% NaCl 150 mL → เป้าเพิ่ม ~5 mmol/L ก่อน", "xs")]
    return fig("เซลล์สมองปรับตัวต่อ Na ต่ำ — และทำไมการแก้เร็วเกินไปจึงอันตราย",
               "Na ตกเร็ว → น้ำเข้าเซลล์สมอง → **สมองบวม** ปวดหัว อาเจียน ชัก herniation · ภายใน ~48 ชม. เซลล์ขับ K, Cl และ **organic osmolyte** (myo-inositol, glutamate, taurine) ออก ขนาดเซลล์จึงกลับมาใกล้ปกติ = hyponatremia เรื้อรังมักมีอาการน้อย · แต่การสร้าง osmolyte กลับใช้เวลาหลายวัน ถ้าเพิ่ม Na เร็ว ECF จะ hypertonic เทียบกับเซลล์ที่ \"ปรับลดไปแล้ว\" → **น้ำออกจากเซลล์** → oligodendrocyte บาดเจ็บ → **osmotic demyelination** (pons: พูดไม่ชัด กลืนลำบาก อัมพาตทั้งตัว locked-in) มักเกิดหลังแก้ไปแล้ว 2–6 วัน · ตัวเลขขีดจำกัดจาก European clinical practice guideline on hyponatremia 2014 (ไม่อยู่ในสไลด์ — รายละเอียดการรักษาอยู่ในคาบ 22 Dysnatremia)",
               svg(420, 264, "ขนาดเซลล์สมองใน hyponatremia เฉียบพลัน หลังปรับตัว และเมื่อแก้เร็วเกินไปจน osmotic demyelination", *out))


# ═══════════════════════════════════════ 11 เยื่อหุ้มเซลล์: RMP เทียบ threshold (ใช้ทั้ง K และ Ca)
def _mp(cols, vmin, vmax, thr_label, top_note):
    Y = lambda v: 40 + (vmax - v) * 4.0
    out = [t(10, 18, top_note, "xs mu"), line(64, Y(vmax), 64, Y(vmin), "ln")]
    for v in range(vmin, vmax + 1, 10):
        out += [line(60, Y(v), 64, Y(v), "ln"), t(56, Y(v) + 4, str(v), "xs end")]
    out.append(t(14, Y(vmax) - 6, "mV", "xs i2"))
    for i, (nm, rmp, thr, c, note1, note2) in enumerate(cols):
        cx = 120 + i * 108
        out += [t(cx, Y(vmin) + 18, nm, "sm b mid"),
                line(cx - 40, Y(thr), cx + 40, Y(thr), "lbad w2 da"),
                line(cx - 40, Y(rmp), cx + 40, Y(rmp), "l%s w3" % c),
                t(cx + 42, Y(thr) + 4, "", "xs"),
                path("M%s %s L%s %s" % (cx, Y(rmp) - 3, cx, Y(thr) + 6), "lmu w2", "ah-mu"),
                t(cx + 6, (Y(rmp) + Y(thr)) / 2 + 4, "%d" % abs(thr - rmp), "xs b"),
                t(cx, Y(vmin) + 34, note1, "xs mid i2"), t(cx, Y(vmin) + 47, note2, "xs b mid")]
    out += [line(330, 26, 350, 26, "lbad w2 da"), t(354, 30, thr_label, "xs"),
            ]
    return out, Y(vmin) + 56


def k_rmp():
    cols = [("K ปกติ", -90, -70, "ac", "ห่าง threshold 20", "ปกติ"),
            ("K สูง", -80, -70, "bad", "ใกล้ threshold", "กระตุก → อ่อนแรง"),
            ("K ต่ำ", -100, -70, "wa", "ไกล threshold", "อ่อนแรง")]
    out, h = _mp(cols, -110, -60, "threshold", "เส้นทึบ = RMP · ตัวเลข = ระยะ (mV) ที่ต้องดีโพลาไรซ์จึงจะเกิด AP")
    return fig("K ในเลือดกำหนด resting membrane potential — สูงหรือต่ำก็อ่อนแรงได้",
               "RMP ขึ้นกับอัตราส่วน K ในเซลล์/นอกเซลล์ และ K ที่รั่วออกทาง leak channel · **K สูง** → K รั่วออกน้อย → RMP ขยับเข้าใกล้ threshold → ช่วงแรกไวเกิน (กล้ามเนื้อกระตุก ตะคริว) แต่ถ้าดีโพลาไรซ์ค้าง **voltage-gated Na channel ถูก inactivate** เปิดไม่ได้อีก → อ่อนแรงแบบปวกเปียก และหัวใจนำไฟฟ้าช้า (QRS กว้าง) · **K ต่ำ** → K รั่วออกมาก → RMP ติดลบมากขึ้น (hyperpolarize) → ต้องกระตุ้นแรงขึ้นจึงจะถึง threshold → อ่อนแรง · ตัวเลข mV เป็นแผนภาพตามสไลด์ Neuromuscular function",
               svg(420, h, "เทียบ resting membrane potential กับ threshold ในภาวะโพแทสเซียมปกติ สูง และต่ำ", *out))


def ca_thr():
    cols = [("Ca ปกติ", -70, -55, "ac", "threshold −55", "ปกติ"),
            ("Ca ต่ำ", -70, -62, "bad", "threshold ต่ำลง", "ไวเกิน → tetany"),
            ("Ca สูง", -70, -48, "wa", "threshold สูงขึ้น", "เฉื่อย → อ่อนแรง")]
    out, h = _mp(cols, -80, -40, "threshold", "Ca เปลี่ยน \"threshold\" ไม่ใช่ RMP (Ca ไปเกาะ/คุม voltage-gated Na channel)")
    return fig("Ionized Ca เลื่อน threshold ของ Na channel — Ca ต่ำจึงชาและเกร็ง",
               "Ca2+ นอกเซลล์เกาะผิวด้านนอกของ voltage-gated Na channel ทำให้เปิดยากขึ้น · **ionized Ca ต่ำ** → channel เปิดง่าย threshold เลื่อนเข้าใกล้ RMP → เส้นประสาทยิงเอง: ชาปลายมือปลายเท้า/รอบปาก ตะคริว **carpopedal spasm** · Chvostek (เคาะหน้าหู) และ Trousseau (รัด cuff เหนือ SBP 20 mmHg 3 นาที ไว 94%) คือการกระตุ้นเส้นประสาทที่ไวเกิน · **Ca สูง** → threshold สูงขึ้น → อ่อนแรง ซึม ท้องผูก · ตัวเลขตามสไลด์ (Na channel เปิดที่ −55 mV เมื่อ Ca ปกติ) — hypomagnesemia ก็ทำให้เกิด tetany ได้เช่นกัน",
               svg(420, h, "แผนภาพ threshold ของ action potential ใน calcium ปกติ ต่ำ และสูง", *out))


# ═══════════════════════════════════════ 12 K shift
def k_shift():
    cx, cy = 210, 150
    out = [circ(cx, cy, 62, "ac"), t(cx, cy - 8, "ICF", "sm b mid"), t(cx, cy + 8, "K ~140 mmol/L", "xs mid"),
           t(cx, cy + 22, "(~98% ของ K ทั้งตัว)", "xs mid i2"),
           circ(cx + 44, cy - 44, 11, "okf"), t(cx + 44, cy - 40, "P", "xs b mid tpa"),
           t(cx, 26, "ECF K 3.5–5.0 (~65 mmol ทั้งหมด)", "xs b mid"),
           t(70, 50, "เข้าเซลล์ → K ↓", "sm b mid tok"), t(350, 50, "ออกนอกเซลล์ → K ↑", "sm b mid tbad")]
    L = ["insulin", "β2-agonist (salbutamol)", "aldosterone", "alkalosis", "Posm ต่ำ"]
    R = ["ขาด insulin (DM type 1)", "β-blocker · α-agonist", "acidosis (กรดแร่ เช่น HCl)", "Posm สูง (glucose)",
         "digoxin (ยับยั้ง pump)", "ออกกำลังมาก", "cell lysis · rhabdo"]
    import math
    def edge(px, py, r=64):
        a = math.atan2(py - cy, px - cx)
        return cx + r * math.cos(a), cy + r * math.sin(a)
    y = 64
    for s in L:
        ex, ey = edge(136, y + 13)
        out += [box(8, y, 128, 26, "ok", s, fs=10.5), ar(137, y + 13, ex, ey, "lok", "ah-ok")]
        y += 34
    y = 64
    for s in R:
        ex, ey = edge(284, y + 13, 62)
        out += [box(284, y, 128, 26, "bad", s, fs=10.5), ar(ex, ey, 282, y + 13, "lbad", "ah-bad")]
        y += 32
    out += [t(cx, 300, "P = Na/K-ATPase (3Na ออก / 2K เข้า)", "xs mid i2")]
    return fig("K shift — ตัวกำหนดว่า K อยู่ในหรือนอกเซลล์",
               "K เกือบทั้งหมดอยู่ในเซลล์ การย้ายเพียง 1–2% ออกมาก็ทำให้ K ในเลือดเปลี่ยนมาก · **insulin, β2-agonist, aldosterone** กระตุ้น Na/K-ATPase ในกล้ามเนื้อ ตับ กระดูก RBC → ดึง K เข้าเซลล์ (จึงใช้ insulin + glucose และ salbutamol แก้ K สูงเร่งด่วน) · **acidosis จากกรดแร่** ยับยั้ง pump และแลก H เข้า/K ออก → K สูง (กรดอินทรีย์ เช่น lactate, ketone ผ่านเยื่อพร้อม H จึงดึง K ออกน้อยกว่า — สไลด์ ICF buffer) · **Posm สูง** ดึงน้ำออกจากเซลล์และ K ตามน้ำออกมา (solvent drag) · ออกกำลัง → ATP ในกล้ามเนื้อลด → ATP-sensitive K channel เปิด (สไลด์ Table 5.4)",
               svg(420, 308, "ปัจจัยที่ดึงโพแทสเซียมเข้าเซลล์และปล่อยออกนอกเซลล์", *out))


# ═══════════════════════════════════════ 13 principal cell — K secretion
def pcell():
    out = [rect(10, 30, 86, 200, "wa", 6), t(53, 22, "lumen", "sm b mid"),
           rect(104, 30, 200, 200, "bx", 12), t(204, 22, "principal cell", "sm b mid"),
           rect(312, 30, 98, 200, "sk", 6), t(361, 22, "เลือด", "sm b mid"),
           # ENaC
           rect(98, 56, 12, 18, "acf", 3), t(116, 50, "ENaC", "xs b tac"),
           ar(20, 65, 94, 65, "lac w2", "ah-ac", "Na+", "xs b mid tac"),
           ar(114, 65, 286, 98, "lac", "ah-ac"),
           circ(304, 108, 13, "okf"), t(304, 112, "ATP", "xs b mid tpa"),
           ar(318, 100, 396, 100, "lac w2", "ah-ac", "3Na+", "xs b mid tac"),
           ar(396, 122, 320, 122, "lok w2", "ah-ok", "2K+", "xs b mid tok", dy=16),
           # ROMK
           ar(290, 120, 118, 150, "lok", "ah-ok"),
           rect(98, 142, 12, 18, "okf", 3), t(116, 176, "ROMK", "xs b tok"), t(150, 176, "← Mg2+ อุดจากในเซลล์", "xs b tms"),
           ar(96, 151, 22, 151, "lok w3", "ah-ok", "K+", "xs b mid tok"),
           # BK
           rect(98, 196, 12, 18, "okf", 3), t(116, 222, "BK", "xs b tok"),
           ar(96, 205, 22, 205, "lok w2", "ah-ok"),
           t(53, 100, "− − −", "lg b mid tbad"), t(53, 116, "lumen ลบ", "xs mid tbad"),
           t(30, 190, "flow ↑", "xs b"),
           # aldosterone
           ar(398, 46, 262, 46, "lms w2", "ah-ms", "aldosterone", "xs b mid tms", dx=30),
           circ(244, 46, 12, "ms"), t(244, 50, "MR", "xs b mid"),
           t(204, 112, "↑ ENaC · ↑ ROMK · ↑ pump", "xs b mid tms")]
    rows = [("1 K ในเลือดสูง", "pump ดึง K เข้าเซลล์มาก → ขับมาก"),
            ("2 aldosterone", "เพิ่ม ENaC/ROMK/pump"),
            ("3 Na + flow มาถึงมาก", "ENaC ↑ · BK เปิด · K ในท่อถูกพาไป"),
            ("4 anion ที่ดูดกลับไม่ได้", "HCO3, ยา → lumen ลบยิ่งขึ้น"),
            ("5 Mg ต่ำ", "ROMK ไม่ถูก Mg อุด → K รั่วทิ้ง"),
            ("6 alkalosis", "pump ↑ · ROMK เปิดมากขึ้น")]
    y = 242
    for a, b in rows:
        out += [t(14, y + 12, a, "xs b"), t(160, y + 12, b, "xs i2")]
        y += 18
    return fig("Principal cell — ทำไมปัจจัยทั้ง 6 ทำให้ขับ K มากขึ้น",
               "Na เข้าเซลล์ทาง **ENaC** โดยไม่มี anion ตามไปด้วย → lumen เป็นประจุ **ลบ** → ดึง K+ ออกทาง **ROMK** · Na/K-ATPase ด้าน basolateral ทำให้ K ในเซลล์สูงพร้อมขับ · **flow สูง** ดัด primary cilia → Ca เข้าเซลล์ → เปิด **BK channel** และพา K ในท่อออกไปเรื่อย ๆ ทำให้ gradient คงอยู่ (เหตุที่ loop/thiazide ทำให้ K ต่ำ) · **Mg ในเซลล์** อุด ROMK จากด้านใน — Mg ต่ำจึงขับ K ไม่หยุดและแก้ K ต่ำไม่ขึ้นจนกว่าจะให้ Mg · K-sparing (amiloride ปิด ENaC · spironolactone บล็อก MR) ตัดแรงขับนี้ (สไลด์ Factors affecting tubular K secretion)",
               svg(420, y + 6, "กลไกการขับโพแทสเซียมของ principal cell และปัจจัยหกข้อที่เพิ่มการขับ", *out))


# ═══════════════════════════════════════ 14 Ca / Pi / Mg — ดูดกลับที่ไหน
def div_segments():
    segs = [("PT", "ac"), ("TAL", "ok"), ("DT", "wa"), ("CD", "ms"), ("ขับทิ้ง", "bad")]
    rows = [("Ca", [65, 25, 8, 1, 1], ["65%", "25%", "8", "", ""]),
            ("Pi", [80, 0, 10, 0, 10], ["80% (NaPi-IIa/c)", "", "10", "", "10"]),
            ("Mg", [30, 60, 5, 0, 5], ["30%", "60% (paracellular)", "5", "", "5"])]
    out, y = _segbar(rows, segs, x0=50, y0=26, scale=3.5)
    out.insert(0, t(10, 14, "ร้อยละของที่กรองแล้ว ดูดกลับในแต่ละส่วน (สไลด์ · ขับทิ้งปัดเศษ)", "xs mu"))
    lx = 50
    for nm, c in segs:
        out += [rect(lx, y + 2, 14, 12, c, 2), t(lx + 18, y + 12, nm, "xs")]
        lx += 64
    notes = [("Ca", "DT = จุดที่ PTH + calcitriol คุม · thiazide ↑ ดูด Ca"),
             ("Pi", "PTH + FGF-23 ดึง NaPi-IIa ออกจากผิว PT → ขับ Pi"),
             ("Mg", "TAL อาศัย lumen บวกจาก NKCC2 → furosemide ↓ Mg")]
    y += 26
    for a, b in notes:
        out += [t(14, y + 12, a, "xs b"), t(44, y + 12, b, "xs i2")]
        y += 18
    return fig("Ca, Pi และ Mg — ดูดกลับคนละที่ จึงคุมด้วยฮอร์โมนและยาต่างกัน",
               "**Ca** ส่วนใหญ่ดูดกลับตาม Na และน้ำที่ PT และ TAL (paracellular) ส่วนที่ **DT ~8%** คือจุดปรับละเอียดด้วย PTH และ 1,25(OH)2D และเป็นเหตุที่ thiazide ลด Ca ในปัสสาวะ · **Pi** ดูดกลับที่ PT ผ่าน NaPi-IIa/IIc ซึ่ง PTH และ FGF-23 ดึงออก → ขับ Pi และ ~10% ที่เหลือในท่อเป็น **buffer ในปัสสาวะ (titratable acid)** · **Mg** ต่างจากตัวอื่น: ดูดมากที่สุดที่ **TAL ~60%** ผ่านช่องระหว่างเซลล์ อาศัยแรงดันไฟฟ้าบวกใน lumen จาก NKCC2 — loop diuretic จึงทำให้ Mg รั่ว · รายละเอียดทางคลินิก (สาเหตุ อาการ การรักษา) อยู่ในคาบ 05 Divalent",
               svg(420, y + 4, "แถบร้อยละการดูดกลับแคลเซียม ฟอสเฟต และแมกนีเซียมในแต่ละส่วนของ nephron", *out))


# ═══════════════════════════════════════ 15 แหล่งกรดและสามแนวป้องกัน
def defense():
    out = [box(10, 8, 196, 52, "wa", "CO2 (volatile)\n~15,000 mmol/วัน → ปอด", fs=11),
           box(214, 8, 196, 52, "bad", "fixed acid ~70 mEq/วัน\n(อาหาร 20 · GI 10 · เมตาบอลิซึม 40)", fs=10.5),
           t(312, 76, "→ ขับได้ทางไตเท่านั้น", "xs b mid tbad"),
           t(10, 100, "แนวป้องกัน pH (สไลด์ pH regulating systems)", "sm b")]
    X = lambda s: 110 + s * 50   # 0 วินาที … 6 วัน (ลอการิทึมแบบหยาบ)
    ticks = [(0, "วินาที"), (1.2, "นาที"), (2.6, "ชั่วโมง"), (3.8, "12–24 ชม."), (5.2, "3–5 วัน")]
    out.append(line(110, 238, 404, 238, "ln"))
    for s, lab in ticks:
        out += [line(X(s), 238, X(s), 242, "ln"), t(X(s), 254, lab, "xs mid")]
    bars = [("1 Buffer", 0, 0.9, "ac", "ทันที · ไม่ได้กำจัดกรด"),
            ("2 ปอด", 1.0, 3.8, "wa", "ปรับ PaCO2 · แก้ได้ ~50–60%"),
            ("3 ไต", 2.4, 5.8, "ok", "ช้าแต่แรงที่สุด · ขับ H + สร้าง HCO3")]
    y = 116
    for nm, a, b, c, note in bars:
        out += [t(102, y + 14, nm, "sm b end"), rect(X(a), y, X(b) - X(a), 18, c, 6),
                t(min(X(a), 404 - 6.2 * len(note)), y + 32, note, "xs b")]
        y += 40
    out += [rect(10, 264, 400, 46, "sk", 8),
            t(20, 282, "pH = 6.1 + log ( [HCO3] ÷ 0.03 × PaCO2 ) = 6.1 + log (24 ÷ 1.2)", "xs b"),
            t(20, 300, "= 6.1 + log 20 = 7.40 → ไตคุมตัวเศษ ปอดคุมตัวส่วน", "xs b tac")]
    return fig("กรดที่ต้องกำจัดทุกวัน และสามแนวป้องกัน pH",
               "ร่างกายสร้าง CO2 มหาศาลแต่ปอดหายใจทิ้งได้หมด ส่วน **fixed acid ~70 mEq/วัน** (กำมะถันจากกรดอะมิโน ฟอสเฟต กรดอินทรีย์ + H ที่เหลือจากการเสีย OH/HCO3 ทางอุจจาระ) ต้องขับทาง **ไตเท่านั้น** · **buffer** ทำงานทันทีแต่เพียงแค่ \"จับ\" H ไว้ · **ปอด** ปรับ PaCO2 ในไม่กี่นาที เต็มที่ 12–24 ชม. แก้ได้ราวครึ่งหนึ่ง · **ไต** ใช้เวลาหลายชั่วโมงถึงหลายวันแต่แก้ได้จริงเพราะขับ H ออกและคืน HCO3 · Henderson–Hasselbalch บอกว่า pH ขึ้นกับ **อัตราส่วน** HCO3 ต่อ PaCO2 ไม่ใช่ค่าใดค่าหนึ่ง",
               svg(420, 318, "แหล่งกรดต่อวันและเวลาตอบสนองของ buffer ปอด และไต พร้อมสมการ Henderson-Hasselbalch", *out))


# ═══════════════════════════════════════ 16 PT: HCO3 reclamation + ammoniagenesis
def pt_hco3():
    out = [rect(10, 30, 92, 240, "wa", 6), t(56, 22, "lumen", "sm b mid"),
           rect(110, 30, 196, 240, "bx", 12), t(208, 22, "proximal tubule cell", "sm b mid"),
           rect(314, 30, 96, 240, "sk", 6), t(362, 22, "เลือด", "sm b mid"),
           t(56, 78, "HCO3− (กรอง)", "xs b mid"), t(56, 92, "+ H+", "xs b mid tbad"),
           ar(56, 97, 56, 110, "ln", "ah"), t(56, 122, "H2CO3", "xs b mid"),
           ar(56, 127, 56, 142, "ln", "ah"), t(66, 138, "CA IV", "xs i2"), t(56, 156, "CO2 + H2O", "xs b mid"),
           ar(88, 152, 150, 152, "lmu w2", "ah-mu"), t(119, 166, "แพร่", "xs i2 mid"),
           t(186, 156, "CO2 + H2O", "xs b mid"), ar(186, 144, 186, 128, "ln", "ah"), t(194, 140, "CA II", "xs i2"),
           t(186, 124, "H2CO3", "xs b mid"), ar(186, 112, 186, 98, "ln", "ah"),
           t(186, 90, "H+  +  HCO3−", "xs b mid"),
           rect(104, 64, 12, 18, "acf", 3), t(116, 54, "NHE3 (Na เข้า/H ออก)", "xs b tac"),
           ar(166, 73, 120, 73, "lbad w2", "ah-bad"), ar(102, 74, 80, 86, "lbad", "ah-bad"),
           ar(214, 73, 296, 73, "lok w2", "ah-ok"), rect(298, 64, 12, 18, "okf", 3), t(294, 100, "NBCe1", "xs b end tok"),
           ar(316, 73, 400, 73, "lok w3", "ah-ok", "HCO3−", "xs b mid tok", dy=-9),
           t(362, 104, "(ตัวเดิมกลับคืน)", "xs mid i2"),
           line(110, 176, 306, 176, "lmu da"),
           box(130, 186, 156, 30, "ms", "glutamine", fs=12),
           ar(208, 216, 208, 228, "lms w2", "ah-ms"),
           t(208, 244, "2 NH4+  +  2 HCO3−", "sm b mid"),
           ar(146, 240, 104, 240, "lms w2", "ah-ms"), t(56, 260, "NH4+ → ปัสสาวะ", "xs b mid tms"),
           ar(272, 240, 400, 240, "lok w3", "ah-ok"), t(362, 228, "HCO3− ใหม่", "xs b mid tok"),
           t(208, 262, "↑ เมื่อ acidosis และ K ต่ำ", "xs mid i2")]
    return fig("Proximal tubule — เก็บ HCO3 ที่กรองคืน และสร้าง HCO3 ใหม่จาก glutamine",
               "**ครึ่งบน (reclamation)**: H+ ที่ขับออกทาง NHE3 จับ HCO3 ที่กรองมา → CO2 + H2O (carbonic anhydrase ที่ผิว lumen) → แพร่เข้าเซลล์ → แยกเป็น H+ (ส่งออกไปรอบใหม่) และ HCO3 (กลับเข้าเลือดทาง NBCe1) — **ได้ HCO3 ตัวเดิมคืนโดยไม่มีการขับ H สุทธิ** (PT เก็บ ~80% ของ HCO3 ~4,320 mmol/วัน) · ถ้า HCO3 ในพลาสมาเกิน ~25 mEq/L จะเกินกำลังดูดกลับและออกในปัสสาวะ · **ครึ่งล่าง (ammoniagenesis)**: glutamine → NH4+ ออกไปในท่อ + **HCO3 ใหม่เข้าเลือด** — เพิ่มขึ้นมากใน acidosis เรื้อรังและ hypokalemia (สไลด์ Ammonium salt excretion)",
               svg(420, 278, "การดูด bicarbonate กลับและการสร้าง ammonium ใน proximal tubule", *out))


# ═══════════════════════════════════════ 17 type A intercalated cell + NAE
def nae():
    out = [rect(10, 30, 120, 200, "wa", 6), t(70, 22, "lumen (ปัสสาวะ)", "sm b mid"),
           rect(138, 30, 160, 200, "bx", 12), t(218, 22, "type A intercalated", "sm b mid"),
           rect(306, 30, 104, 200, "sk", 6), t(358, 22, "เลือด", "sm b mid"),
           rect(132, 64, 12, 18, "badf", 3), t(150, 58, "H+-ATPase", "xs b tbad"),
           rect(132, 104, 12, 18, "badf", 3), t(150, 136, "H/K-ATPase", "xs b tbad"),
           path("M214 162 L214 73", "lbad w2"),
           ar(214, 73, 148, 73, "lbad w2", "ah-bad"), ar(214, 113, 148, 113, "lbad w2", "ah-bad"),
           ar(128, 73, 100, 73, "lbad w2", "ah-bad"), ar(128, 113, 100, 113, "lbad w2", "ah-bad"),
           t(70, 98, "H+", "sm b mid tbad"),
           t(236, 178, "H+ + HCO3−", "xs b mid"), ar(236, 204, 236, 186, "ln", "ah"), t(244, 198, "CA II", "xs i2"),
           t(236, 216, "CO2 + H2O", "xs b mid"),
           ar(266, 174, 296, 174, "lok w2", "ah-ok"), rect(298, 165, 12, 18, "okf", 3),
           ar(314, 174, 400, 174, "lok w3", "ah-ok", "HCO3− ใหม่", "xs b mid tok", dy=-11),
           t(358, 196, "AE1 (แลก Cl)", "xs mid i2"),
           box(16, 128, 108, 40, "ms", "HPO4 + H\n→ H2PO4 (TA) 40%", fs=10.5),
           box(16, 174, 108, 40, "ok", "NH3 + H\n→ NH4+ 60%", fs=10.5),
           t(70, 226, "ถูกขังไปกับปัสสาวะ", "xs mid i2")]
    out += [rect(10, 240, 400, 66, "ac", 9),
            t(20, 258, "1 H+ ที่ขับ (ผูกกับ buffer) = 1 HCO3− ใหม่เข้าเลือด", "xs b"),
            t(20, 276, "NAE = TA + NH4+ − HCO3− ในปัสสาวะ ≈ 70 mEq/วัน", "xs b tac"),
            t(20, 294, "urine pH ต่ำสุด 4.5 ([H] อิสระ 0.03 mEq/L) → ต้องมี buffer", "xs")]
    return fig("Type A intercalated cell — ขับ H จริง และทำไมต้องมี buffer ในปัสสาวะ",
               "ที่ late DT/collecting duct, type A-IC ปั๊ม H+ ออกด้วย **H+-ATPase** (aldosterone และ lumen ลบช่วย) และ **H/K-ATPase** (เพิ่มเมื่อ K ต่ำ) แล้วส่ง HCO3 ใหม่เข้าเลือดทาง AE1 · ปัสสาวะเป็นกรดได้ต่ำสุด pH 4.5 = H อิสระเพียง 0.03 mEq/L → ถ้าจะขับ 70 mEq เป็น H อิสระต้องใช้ปัสสาวะ ~2,300 L/วัน (สไลด์คำนวณ 2,667 L) · จึงต้องผูก H กับ **phosphate (titratable acid)** และ **NH3 (ammonium)** · NH4+ เพิ่มได้หลายเท่าใน acidosis ส่วน phosphate มีจำกัด · **distal RTA (type 1)** = เซลล์นี้ขับ H ไม่ได้ ปัสสาวะ pH > 5.5 แม้เลือดเป็นกรด",
               svg(420, 314, "การขับ H และสร้าง bicarbonate ใหม่ใน type A intercalated cell พร้อม titratable acid และ ammonium", *out))


# ═══════════════════════════════════════ 18 การชดเชย 4 แบบ
def comp():
    P = [("Metabolic acidosis", "↓", "", "bad", "ปอด: หายใจเร็ว-ลึก", "↓", "นาที–ชม."),
         ("Metabolic alkalosis", "↑", "", "ms", "ปอด: หายใจช้า-ตื้น", "↑", "นาที–ชม."),
         ("Respiratory acidosis", "", "↑", "bad", "ไต: ↑ ขับ H / สร้าง HCO3", "↑", "3–5 วัน"),
         ("Respiratory alkalosis", "", "↓", "wa", "ไต: ↓ ดูด HCO3", "↓", "2–3 วัน")]
    out = []
    for i, (nm, nh, dc, c, organ, ca, tm) in enumerate(P):
        x0, y0 = 8 + (i % 2) * 206, 8 + (i // 2) * 140
        out += [rect(x0, y0, 198, 132, c, 10), t(x0 + 99, y0 + 18, nm, "sm b mid")]
        fx = x0 + 60
        out += [t(fx, y0 + 52, "HCO3−", "sm b mid"), line(fx - 32, y0 + 62, fx + 32, y0 + 62, "ln w2"),
                t(fx, y0 + 80, "PaCO2", "sm b mid")]
        if nh:
            out.append(t(fx + 40, y0 + 54, nh, "lg b tbad"))
            out.append(t(fx + 40, y0 + 82, ca, "lg b tok"))
        else:
            out.append(t(fx + 40, y0 + 82, dc, "lg b tbad"))
            out.append(t(fx + 40, y0 + 54, ca, "lg b tok"))
        out += [t(x0 + 150, y0 + 52, "pH", "xs b mid"),
                t(x0 + 150, y0 + 72, "↓" if "acidosis" in nm else "↑", "lg b mid tbad"),
                t(x0 + 99, y0 + 106, organ, "xs b mid tok"), t(x0 + 99, y0 + 121, "เต็มที่ใน " + tm, "xs mid i2")]
    out += [t(14, 300, "แดง = ความผิดปกติหลัก · เขียว = การชดเชย (ไปทางเดียวกันเสมอ)", "xs b"),
            t(14, 316, "ชดเชยแค่ดึง pH เข้าหาปกติ ไม่เกิน · pH ปกติพอดี + ค่าผิดสองตัว = สงสัย mixed", "xs i2")]
    return fig("การชดเชยกรด-ด่าง — ร่างกายพยายามรักษา \"อัตราส่วน\" HCO3 ต่อ PaCO2",
               "เพราะ pH ขึ้นกับอัตราส่วน HCO3/PaCO2 ร่างกายจึงชดเชยโดย **เปลี่ยนอีกตัวไปทางเดียวกับตัวที่ผิด** · ความผิดปกติทาง metabolic → **ปอด** ชดเชยภายในนาทีถึงชั่วโมง · ความผิดปกติทางการหายใจ → ช่วงแรกมีแค่ buffer ในเซลล์ (HCO3 เปลี่ยนนิดเดียว = acute) แล้ว **ไต** ค่อย ๆ ชดเชยใน 3–5 วัน (chronic) · การชดเชยไม่เคยทำให้ pH กลับปกติสนิท (ยกเว้น chronic respiratory alkalosis ที่ชดเชยได้เกือบเต็ม) — สไลด์ Compensatory mechanisms และตาราง Primary disturbance",
               svg(420, 324, "ทิศทางของความผิดปกติหลักและการชดเชยในความผิดปกติกรดด่างทั้งสี่แบบ", *out))


# ═══════════════════════════════════════ 19 vomiting → metabolic alkalosis
def vomit():
    S = [("อาเจียน / NG suction: เสีย HCl + น้ำ", "bad", None),
         ("GENERATION: parietal cell สร้าง H ออก → HCO3 เข้าเลือด (alkaline tide)", "ms", None),
         ("ช่วงแรก: HCO3 ที่กรองเกินกำลังดูดกลับ → ปัสสาวะด่าง ลาก Na, K ทิ้ง", "wa", None),
         ("เสีย volume + Cl → Ang II + aldosterone (MAINTENANCE)", "ms", None),
         ("aldo + Na/flow ที่ปลาย + HCO3 ในท่อ → ขับ K มาก → K ต่ำ", "bad", None),
         ("volume ↓ + K ↓ + aldo → NHE3/H-ATPase/H-K-ATPase ทำงานเต็ม", "ms", None),
         ("ช่วงหลัง: ปัสสาวะเป็นกรดทั้งที่เลือดด่าง = paradoxical aciduria", "bad", None),
         ("แก้: 0.9% NaCl + KCl → คืน Cl/volume/K → ไตปล่อย HCO3 ทิ้งได้เอง", "ok", None)]
    out = []
    y = 8
    for i, (s, c, _) in enumerate(S):
        out.append(box(10, y, 400, 30, c, s, fs=10.5))
        if i < len(S) - 1:
            out.append(ar(210, y + 30, 210, y + 39, "ln", "ah"))
        y += 40
    out.append(t(14, y + 8, "urine Cl < 20 = saline-responsive (UNa อาจสูงช่วงแรกเพราะ HCO3 ลาก Na ออก)", "xs b tac"))
    return fig("อาเจียน → metabolic alkalosis + K ต่ำ + paradoxical aciduria",
               "แยกให้ออกเป็นสองขั้น: **generation** (เสีย H จากกระเพาะ HCO3 จึงเพิ่ม) และ **maintenance** (ไตที่ปกติจะขับ HCO3 ส่วนเกินทิ้งได้ง่าย ๆ แต่ในภาวะนี้ **ไม่ยอมขับ** เพราะปริมาตรลด Cl ต่ำ K ต่ำ และ aldosterone สูง) · K ที่ต่ำ **ส่วนใหญ่หายทางไต** ไม่ใช่ทางน้ำย่อย (น้ำย่อยมี K เพียง ~5–10 mmol/L) · ปัสสาวะที่เป็นกรดทั้งที่เลือดเป็นด่างเป็นสัญญาณว่าไตกำลังเลือก \"รักษาปริมาตร\" มากกว่า pH (สไลด์ Factors affecting HCO3 reabsorption · contraction alkalosis · luminal anion) — ส่วน urine Cl เติมจากตำรา",
               svg(420, y + 14, "ลำดับเหตุการณ์จากการอาเจียนถึงภาวะด่างเมตาบอลิก โพแทสเซียมต่ำ และปัสสาวะเป็นกรด", *out))


# ═══════════════════════════════════════ 20 DKA — Kussmaul + K
def dka():
    out = [box(10, 8, 400, 30, "bad", "ขาด insulin + glucagon สูง → lipolysis → ketoacid (β-OHB, AcAc)", fs=11),
           ar(110, 38, 110, 50, "ln", "ah"), ar(310, 38, 310, 50, "ln", "ah"),
           box(10, 52, 196, 54, "ms", "H+ ถูก HCO3 จับ → CO2\nHCO3 ↓ · keto-anion ค้าง\n→ anion gap กว้าง", fs=10.5),
           box(214, 52, 196, 54, "ms", "glucose สูง → osmotic diuresis\nเสียน้ำ Na K\n+ Posm สูง", fs=10.5),
           ar(110, 106, 110, 118, "ln", "ah"), ar(310, 106, 310, 118, "ln", "ah"),
           box(10, 120, 196, 54, "bad", "pH ↓ → peripheral (carotid)\n+ central chemoreceptor\n→ ศูนย์หายใจใน medulla", fs=10.5),
           box(214, 120, 196, 54, "bad", "ขาด insulin + Posm สูง\n→ K ออกนอกเซลล์\nK เลือดปกติ/สูง", fs=10.5),
           ar(110, 174, 110, 186, "ln", "ah"), ar(310, 174, 310, 186, "ln", "ah"),
           box(10, 188, 196, 54, "ok", "หายใจลึก (VT ↑↑) และเร็ว\n= Kussmaul\nPaCO2 ↓ ตาม Winter", fs=10.5),
           box(214, 188, 196, 54, "wa", "แต่ K ทั้งตัวขาด (ขับทางไต)\nให้ insulin → K เข้าเซลล์\n→ K ดิ่ง: ต้องเติม K", fs=10.5),
           rect(10, 252, 400, 44, "sk", 8),
           t(210, 270, "ลมหายใจกลิ่นผลไม้ = acetone ที่ระเหยได้", "xs mid"),
           t(210, 287, "ปวดท้อง/อาเจียน = ketone ระคายเคือง + กระเพาะเคลื่อนช้า", "xs mid")]
    return fig("DKA — Kussmaul breathing และ K ที่ \"ปกติหลอก\"",
               "**Kussmaul** คือการชดเชยทางการหายใจที่เห็นด้วยตา: H+ จาก ketoacid กระตุ้น chemoreceptor → ศูนย์หายใจเพิ่ม **tidal volume มากกว่าอัตรา** (หายใจลึก ยาว สม่ำเสมอ) เพื่อเป่า CO2 ทิ้ง · ด้าน K: สไลด์ย้ำว่า **กรดอินทรีย์ไม่ค่อยแลก H/K** — K ที่สูงใน DKA จึงมาจาก **ขาด insulin และ Posm สูง (solvent drag)** มากกว่า acidosis · ขณะเดียวกัน osmotic diuresis และ aldosterone ขับ K ทิ้งจน **K ทั้งร่างกายพร่อง** เมื่อให้ insulin K จะเข้าเซลล์และต่ำลงอย่างรวดเร็ว (ส่วน K/insulin เติมจากตำราและแนวทาง ADA)",
               svg(420, 304, "กลไก Kussmaul breathing และการเปลี่ยนแปลงโพแทสเซียมในภาวะ diabetic ketoacidosis", *out))


# ═══════════════════════════════════════ 21 Gamblegram — anion gap
def gamble():
    S = 1.35
    base = 230
    P = [("ปกติ", 104, 24, 12, "sk"), ("AG กว้าง (DKA)", 104, 10, 26, "bad"), ("AG ปกติ (ท้องเสีย)", 118, 10, 12, "ms")]
    out = [t(10, 16, "Na 140 = Cl + HCO3 + AG (anion ที่ไม่ได้วัด) · หน่วย mEq/L", "xs mu")]
    for i, (nm, cl, hc, ag, c) in enumerate(P):
        x0 = 14 + i * 136
        out += [rect(x0, base - 140 * S, 50, 140 * S, "ac", 3), t(x0 + 25, base - 70 * S + 4, "Na", "sm b mid"),
                t(x0 + 25, base - 70 * S + 18, "140", "xs mid")]
        y = base
        for lab, v, cls in (("Cl", cl, "wa"), ("HCO3", hc, "ok"), ("AG", ag, c)):
            out.append(rect(x0 + 56, y - v * S, 56, v * S, cls, 3))
            out.append(t(x0 + 84, y - v * S / 2 + 4, "%s %d" % (lab, v), "xs b mid"))
            y -= v * S
        out.append(t(x0 + 56, base + 18, nm, "xs b mid"))
    out += [rect(10, 258, 400, 50, "sk", 8),
            t(20, 276, "AG กว้าง: HCO3 หายไปแทนด้วย anion ของกรด (ketone, lactate, formate)", "xs"),
            t(20, 294, "AG ปกติ: เสีย HCO3 ไปเลย → ไตเก็บ Cl แทน → hyperchloremia", "xs")]
    return fig("Anion gap — กรดใหม่เพิ่ม anion ที่ไม่ได้วัด ส่วนการเสีย HCO3 ถูกแทนด้วย Cl",
               "ประจุบวกและลบในพลาสมาต้องเท่ากันเสมอ เครื่องวัดเพียง Na Cl HCO3 ส่วนที่ขาดคือ **anion gap** (ปกติ 10 ± 2 ตามสไลด์ — ส่วนใหญ่เป็น albumin) · เมื่อมี **กรดเติมเข้า** H จับ HCO3 ไปเป็น CO2 แต่ anion ของกรดยังค้าง → AG กว้าง Cl ปกติ · เมื่อ **เสีย HCO3** (ท้องเสีย CA inhibitor proximal RTA) หรือ **ไตขับ H ไม่ได้** (distal RTA hypoaldosteronism) ไม่มี anion ใหม่ ไตจึงเก็บ Cl แทน → AG ปกติ Cl > 110 · albumin ลด 1 g/dL ทำให้ AG แคบลง ~2.5 ต้องแก้ค่า (สไลด์ Differential diagnosis cause of metabolic acidosis)",
               svg(420, 316, "Gamblegram เทียบประจุในพลาสมาปกติ metabolic acidosis แบบ anion gap กว้าง และแบบ anion gap ปกติ", *out))


# ═══════════════════════════════════════ 22 stepwise
def steps():
    S = [("1 ดู pH", "< 7.35 acidemia · > 7.45 alkalemia", "ac"),
         ("2 หาตัวหลัก", "ตัวที่อธิบายทิศ pH: HCO3 = metabolic · PaCO2 = resp", "ac"),
         ("3 ชดเชยพอดีไหม", "Winter: PaCO2 = 1.5×HCO3 + 8 ± 2 (met. acidosis)", "ok"),
         ("4 anion gap", "Na − (Cl + HCO3) · + 2.5×(4 − albumin)", "ms"),
         ("5 ΔAG/ΔHCO3", "(AG − 12) ÷ (24 − HCO3): < 1 มี NAG · > 2 มี alk.", "ms"),
         ("6 osmolal gap", "วัด − (2Na + glu/18 + BUN/2.8) > 10 → methanol/EG", "bad"),
         ("7 ถ้า AG ปกติ", "urine AG = UNa + UK − UCl: ลบ = GI · บวก = RTA", "wa")]
    out = []
    y = 8
    for i, (a, b, c) in enumerate(S):
        out += [box(10, y, 112, 32, c, a, fs=11.5), box(128, y, 282, 32, "bx", b, fs=10.5)]
        if i < len(S) - 1:
            out.append(ar(66, y + 32, 66, y + 40, "ln", "ah"))
        y += 42
    return fig("แปลผลกรด-ด่างทีละขั้น (stepwise approach)",
               "ขั้น 1–3 และ anion gap มาจากสไลด์ (Stepwise approach · AG · corrected AG) · **Winter's formula, delta ratio, osmolal gap และ urine anion gap เติมจากตำรา** (Berend NEJM 2014 · Boron) เพื่อใช้ต่อกับคาบ chest 26 ABG · ใช้ HCO3 จาก **electrolyte (TCO2)** ที่เจาะเวลาเดียวกันในการคำนวณ AG และการชดเชย (สไลด์: ค่า HCO3 จาก ABG คำนวณจาก pH และ PaCO2 และควรต่างจาก TCO2 ไม่เกิน 10%)",
               svg(420, y, "ขั้นตอนการแปลผลกรดด่างเจ็ดขั้นพร้อมสูตรสำคัญ", *out))


# ═══════════════════════════════════════ 23 micturition innervation
def mict():
    out = [box(10, 8, 220, 30, "ac", "Cerebral cortex (prefrontal): อนุญาต/ห้าม", fs=11),
           box(10, 46, 220, 36, "ac", "Pons: PMC (สั่งปัสสาวะ)\nPSC (สั่งเก็บ) · ประสานหูรูด", fs=10.5),
           line(120, 38, 120, 46, "lac w2"), line(40, 82, 40, 92, "lac w2"),
           rect(22, 92, 36, 236, "sk", 10), t(40, 106, "cord", "xs b mid"),
           t(40, 144, "T10–", "xs b mid tms"), t(40, 157, "L2", "xs b mid tms"),
           t(40, 266, "S2–", "xs b mid tac"), t(40, 279, "S4", "xs b mid tac"),
           ell(256, 186, 70, 58, "wa"), t(256, 180, "detrusor", "sm b mid"), t(256, 196, "(smooth muscle)", "xs mid i2"),
           rect(242, 250, 28, 18, "ms", 4), t(278, 263, "internal sphincter (α1)", "xs"),
           rect(236, 290, 40, 12, "ok", 3), t(282, 300, "external sphincter (N)", "xs"),
           line(256, 268, 256, 330, "lmu w2"),
           path("M58 150 C120 150 150 150 192 156", "lms w3", "ah-ms"),
           t(96, 140, "hypogastric · NE", "xs b tms"), t(70, 176, "β3 คลาย · α1 บีบ", "xs tms"),
           path("M58 262 C120 262 160 240 196 220", "lac w3", "ah-ac"),
           t(70, 288, "pelvic · ACh (M3)", "xs b tac"),
           path("M58 300 C130 300 190 296 232 296", "lok w3", "ah-ok"),
           t(120, 318, "pudendal · ACh (N)", "xs b tok"),
           path("M190 200 C150 212 100 234 62 248", "lwa w2 da", "ah-wa"),
           t(112, 212, "Aδ afferent: ยืด", "xs b twa")]
    return fig("เส้นประสาทของกระเพาะปัสสาวะ — sympathetic เก็บ · parasympathetic ปล่อย · somatic กลั้น",
               "**Hypogastric (sympathetic T10–L2, NE)**: β3 → detrusor คลาย · α1 → คอกระเพาะ/หูรูดชั้นในบีบ → **ช่วงเก็บ** · **Pelvic (parasympathetic S2–S4, ACh)**: M3 → detrusor บีบ หูรูดชั้นในคลาย → **ช่วงขับ** · **Pudendal (somatic S2–S4, ACh)**: nicotinic → หูรูดชั้นนอก (กล้ามเนื้อลาย) บีบ = กลั้นได้ตามใจ · **Aδ afferent** ใน pelvic nerve ส่งสัญญาณการยืด · pons คือสวิตช์สลับเก็บ/ขับและประสานให้ detrusor บีบพร้อมหูรูดคลาย (สไลด์ CNS control · Innervation)",
               svg(420, 336, "แผนผังเส้นประสาท hypogastric pelvic pudendal และ afferent ของกระเพาะปัสสาวะกับศูนย์ควบคุมในสมอง", *out))


# ═══════════════════════════════════════ 24 รอยโรคแต่ละระดับ → แบบของกระเพาะ
def lesion():
    R = [("สมอง เหนือ pons\nstroke · dementia · NPH", "ขาดการยับยั้ง detrusor\nหูรูดยังประสานดี", "urge incontinence\nPVR ต่ำ", "ac"),
         ("ไขสันหลัง เหนือ S2\nSCI · MS · cord compression", "detrusor บีบเอง (reflex)\n+ DSD: หูรูดบีบสวน", "ค้าง + รั่ว\nความดันสูง → ไตเสีย", "bad"),
         ("S2–S4 / ส่วนปลาย\ncauda equina · DM neuropathy", "detrusor ไม่บีบ (atonic)\nไม่รู้สึกว่าเต็ม", "overflow\nPVR สูงมาก", "ms"),
         ("ทางออกอุด\nBPH · stricture", "detrusor สู้แรงต้าน\nไม่ไหว", "retention\n/overflow", "ms"),
         ("หูรูด/อุ้งเชิงกรานหย่อน\nหลังคลอด · ผ่าตัด prostate", "แรงดันช่องท้อง\n> แรงปิด", "stress incontinence\n(ไอ จาม ยกของ)", "wa")]
    out = [t(86, 16, "ตำแหน่ง", "sm b mid"), t(236, 16, "เกิดอะไรขึ้น", "sm b mid"), t(360, 16, "อาการ", "sm b mid")]
    y = 24
    for a, b, c, cls in R:
        out += [box(6, y, 160, 46, cls, a, fs=10.5), box(172, y, 128, 46, "bx", b, fs=10),
                box(306, y, 108, 46, "bx", c, fs=10),
                ar(166, y + 23, 171, y + 23, "lmu", "ah-mu"), ar(300, y + 23, 305, y + 23, "lmu", "ah-mu")]
        y += 54
    return fig("ระดับของรอยโรค → รูปแบบของกระเพาะปัสสาวะ → ชนิดของการกลั้นไม่ได้",
               "ใช้วงจรในสไลด์ทำนายอาการ: **เหนือ pons** — reflex ที่ sacral และการประสานงานที่ pons ยังอยู่ แต่ cortex ห้ามไม่ได้ → ปวดกลั้นไม่อยู่ (urge) ถ่ายหมด · **ระหว่าง pons กับ S2** — ตัดสวิตช์ pons: detrusor บีบเป็น reflex แต่หูรูดไม่คลายตาม (**detrusor–sphincter dyssynergia**) → ความดันสูงย้อนทำลายไต · **sacral/เส้นประสาทส่วนปลาย** — reflex arc ขาด detrusor ไม่บีบ → ปัสสาวะคั่งจนล้น (overflow) · ส่วน stress incontinence และ BPH เป็นปัญหาที่ \"ท่อ\" ไม่ใช่ประสาท (ตารางนี้เติมจากตำรา — สไลด์สอนเฉพาะวงจรปกติ)",
               svg(420, y + 2, "ตารางภาพเชื่อมตำแหน่งรอยโรคทางระบบประสาทกับรูปแบบกระเพาะปัสสาวะและอาการกลั้นไม่ได้", *out))
