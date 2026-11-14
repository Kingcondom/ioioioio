# -*- coding: utf-8 -*-
"""ภาพนิ่ง (FIGS → section.figs) · ภาพเคลื่อนไหว (ITEMS → section.anims) · หลักจำ (MNEM → section.mnem)
ของคาบ chest "AST" Asthma (อ. 3 พ.ย. 2569 · คาบ active learning — โน้ต slides/asthma_plaud_notes.md)
build_asthma.py นำไปใส่ · รูปแบบภาพเคลื่อนไหวตาม dashboard/learn_anim/SPEC.md
ตรวจ:  python3 artifact/tools/anims_chest_ast.py <out.json>  แล้ว  python3 dashboard/anim_tool.py check <data ที่ยังไม่มี anims ของคาบนี้> <out.json>
แผนภาพทั้งหมดเป็น "ภาพจำลองกลไก" ไม่ใช่สัดส่วนจริง · ใช้คลาสสีของธีม (สลับโหมดมืดได้)"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg import fig, svg, t, rect, circ, ell, line, ar, path, esc, pill  # noqa: E402


def S(k, *parts, x=None):
    a = ' data-s="%d"' % k + ((' data-x="%d"' % x) if x else "")
    return "<g%s>%s</g>" % (a, "".join(p for p in parts if p))


def G(c, *parts):
    return '<g class="%s">%s</g>' % (c, "".join(p for p in parts if p))


def SVG(w, h, label, *parts):
    return ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg">' % (w, h, esc(label))
            + "".join(p for p in parts if p) + "</svg>")


def bx(x, y, w, h, c, lines, cls="xs", first="sm b", lh=15):
    """กล่อง + ข้อความหลายบรรทัดกึ่งกลาง (บรรทัดแรกตัวหนา)"""
    lines = lines if isinstance(lines, (list, tuple)) else [lines]
    n = len(lines)
    y0 = y + h / 2 - (n - 1) * lh / 2 + 4
    out = [rect(x, y, w, h, c, 8)]
    for i, s in enumerate(lines):
        out.append(t(x + w / 2, y0 + i * lh, s, ("mid " + (first if i == 0 else cls)).strip()))
    return "".join(out)


def note(y, s1, s2=None, c="ac", w=420, x=10):
    h = 40 if s2 else 28
    out = [rect(x, y, w, h, c, 8), t(x + w / 2, y + (17 if s2 else 18), s1, "sm b mid")]
    if s2:
        out.append(t(x + w / 2, y + 33, s2, "xs mid"))
    return "".join(out)


# ═════════════════════════════════════════════ ภาพนิ่ง
def f_endotype():
    cols = [(10, "Allergic eosinophilic", "ms", "allergen (ไรฝุ่น แมว เกสร)", "DC → Th2", "IL-4 → IgE · IL-5 · IL-13",
             "เริ่มวัยเด็ก · ภูมิแพ้ร่วม", ["anti-IgE · anti-IL-5", "anti-IL-4R"]),
            (155, "Non-allergic eosinophilic", "wa", "ไวรัส มลพิษ ควัน", "เยื่อบุ → alarmin → ILC2", "IL-5 · IL-13 (IgE ไม่เด่น)",
             "ผู้ใหญ่ · ไซนัส/ริดสีดวงจมูก", ["anti-IL-5 · anti-IL-4R", "anti-TSLP"]),
            (300, "T2-low", "sk", "ควัน มลพิษ ติดเชื้อ อ้วน", "Th1 · Th17", "neutrophil เด่น",
             "eos และ FeNO ไม่สูง", ["ตอบสนอง ICS น้อย", "anti-TSLP"])]
    p = [t(220, 16, "T2-high (eosinophil เด่น)", "sm b mid tac"), line(20, 22, 285, 22, "lac w2"),
         t(370, 16, "T2-low", "sm b mid mu"), line(300, 22, 430, 22, "lmu w2")]
    for x, title, c, trig, mid, cyt, clin, bio in cols:
        cx = x + 65
        p += [bx(x, 30, 130, 34, c, [title], first="xs b"),
              t(cx, 84, "ตัวกระตุ้น", "xs mid mu"), t(cx, 98, trig, "xs mid"),
              ar(cx, 104, cx, 120, "ln w2", "ah"),
              bx(x, 122, 130, 30, "bx", [mid], first="xs b"),
              ar(cx, 152, cx, 168, "ln w2", "ah"),
              bx(x, 170, 130, 30, c, [cyt], first="xs b"),
              t(cx, 220, clin, "xs mid"),
              t(cx, 246, "เป้ายา (เกินระดับ NL)", "xs mid mu"), t(cx, 260, bio[0], "xs mid tac"), t(cx, 274, bio[1], "xs mid tac")]
    p.append(t(220, 304, "อ.: บล็อกทางหนึ่ง การอักเสบ \"เหมือนน้ำ\" หาทางไปอีกทาง — คนไข้จริงจึงไม่แยกขาด 100%", "xs mid i2"))
    return fig("Endotype 3 แบบของ asthma (แผนภาพที่อาจารย์ให้จดในคาบ)",
               "phenotype = ลักษณะที่ผู้ป่วยแสดงออก · endotype = กลไกการอักเสบที่อยู่เบื้องหลัง · สองแบบแรกคือ **T2-high** "
               "(IL-4/IL-5/IL-13 · eosinophil · FeNO สูง · ตอบสนอง ICS ดี) ต่างกันที่ต้นทาง: allergen → Th2 กับ epithelium → alarmin (TSLP, IL-33, IL-25) → ILC2 · "
               "**T2-low** ไม่ได้แปลว่าไม่มี T2 เลย (อาจารย์ย้ำว่าไม่ใช้คำว่า non-T2) · ภาพแนวคิดดัดแปลงจาก GINA 2024 (severe asthma guide)",
               svg(440, 314, "แผนภาพสามคอลัมน์ allergic eosinophilic non-allergic eosinophilic และ T2-low แสดงตัวกระตุ้น เซลล์ต้นทาง ไซโตไคน์ ลักษณะคลินิก และเป้ายา biologic", *p))


def f_pefvar():
    X = lambda d: 50 + d * 26
    Y = lambda v: 210 - (v - 300) * 1.2
    am = [330, 340, 320, 350, 335, 325, 345, 330, 320, 340, 335, 330, 325, 340]
    pm = [395, 400, 390, 410, 400, 385, 405, 395, 390, 400, 395, 400, 390, 405]
    pts = []
    for d in range(14):
        pts += [(X(d), Y(am[d])), (X(d + 0.5), Y(pm[d]))]
    p = [line(44, 40, 44, 214, "ln w2"), line(44, 214, 420, 214, "ln w2"), t(48, 34, "PEF (L/min)", "xs b"),
         t(420, 232, "วัน (เช้า ● · เย็น ○) 2 สัปดาห์", "xs end mu")]
    for v in (300, 350, 400):
        p += [line(40, Y(v), 420, Y(v), "lmu da"), t(38, Y(v) + 4, str(v), "xs end mu")]
    p.append(path("M" + " L".join("%.1f %.1f" % q for q in pts), "lac w2"))
    for i, (x, y) in enumerate(pts):
        p.append(circ(x, y, 3.5, "acf" if i % 2 == 0 else "bx"))
    p += [rect(60, 246, 360, 50, "ac", 8), t(240, 264, "รายวัน = (สูงสุด − ต่ำสุด) ÷ ค่าเฉลี่ยของสองค่า × 100", "xs b mid"),
          t(240, 282, "วันแรก (395 − 330) ÷ 362.5 = 17.9% · เฉลี่ยทุกวัน > 10% = เกิน", "xs mid")]
    return fig("PEF diary — วัดเช้าเย็น 2 สัปดาห์ แล้วคิด diurnal variability",
               "ใช้เมื่อ spirometry ในวันตรวจยังไม่ยืนยัน (อาจารย์: \"ให้คนไข้ไปเป่าที่บ้าน 6 โมงเช้า 6 โมงเย็น record มา 2 อาทิตย์\") · "
               "**GINA: ค่าเฉลี่ย daily diurnal PEF variability > 10% ในผู้ใหญ่** (เด็ก > 13%) วัดวันละ 2 ครั้งนาน 1–2 สัปดาห์ · ERS 2022 และ BTS/NICE ใช้เกณฑ์ ≥ 20% "
               "— ตอบข้อสอบต้องบอกว่าใช้เกณฑ์ของใคร · ข้อมูลในกราฟเป็นตัวอย่างสมมุติ",
               svg(440, 300, "กราฟ PEF เช้าและเย็นตลอดสองสัปดาห์ ค่าเช้าต่ำกว่าค่าเย็นทุกวัน พร้อมสูตรคำนวณ diurnal variability", *p))


def f_formo():
    X = lambda h: 50 + h * 30
    Y = lambda e: 200 - e * 1.5
    def curve(onset, peak_h, dur, c):
        pts = [(0, 0), (onset, 40), (peak_h, 100), (dur * 0.7, 80), (dur, 30), (min(dur * 1.15, 12.4), 0)]
        return path("M" + " L".join("%.1f %.1f" % (X(h), Y(e)) for h, e in pts), c)
    p = [line(50, 40, 50, 204, "ln w2"), line(50, 204, 430, 204, "ln w2"), t(54, 34, "ผลขยายหลอดลม", "xs b"),
         t(430, 34, "ชั่วโมงหลังพ่น →", "xs end mu")]
    for h in (0, 2, 4, 6, 8, 10, 12):
        p.append(t(X(h), 218, str(h), "xs mid mu"))
    p += [curve(0.08, 0.5, 5, "lwa w3"), curve(0.1, 1.0, 12, "lok w3"), curve(1.0, 3, 11.2, "lms w3 da")]
    p += [t(X(4.6), Y(52), "salbutamol (SABA)", "xs b twa"), t(X(6.7), Y(96), "formoterol: เร็ว + นาน", "xs b tok"),
          t(X(5.5), Y(64), "salmeterol: ช้า", "xs b tms")]
    p += [rect(60, 238, 360, 46, "ac", 8), t(240, 256, "formoterol ออกฤทธิ์ใน 1–3 นาที → ใช้เป็น reliever ได้", "xs b mid"),
          t(240, 274, "จึงเป็นตัวเดียวที่ใช้ใน MART / AIR (Track 1)", "xs mid")]
    return fig("ทำไม Track 1 ต้องเป็น formoterol",
               "อาจารย์: \"LABA ใน Track 1 บังคับต้องเป็น formoterol\" เพราะเป็น LABA ตัวเดียวที่ **เริ่มออกฤทธิ์เร็วพอ ๆ กับ salbutamol** แต่อยู่ได้ราว 12 ชั่วโมง · "
               "salmeterol ออกฤทธิ์ช้า (10–20 นาที) จึงใช้บรรเทาอาการไม่ได้ · ภาพแนวคิด ไม่ใช่สัดส่วนจริง",
               svg(440, 290, "กราฟผลขยายหลอดลมตามเวลา salbutamol เร็วแต่สั้น formoterol เร็วและนาน salmeterol ช้าแต่นาน", *p))


def f_control():
    qs = [("D", "Day — อาการกลางวัน > 2 ครั้ง/สัปดาห์"), ("N", "Night — ตื่นกลางคืนเพราะหืด"),
          ("R", "Reliever — ใช้ยาบรรเทา > 2 ครั้ง/สัปดาห์"), ("A", "Activity — ทำกิจกรรมได้น้อยลงเพราะหืด")]
    p = [t(220, 18, "ใน 4 สัปดาห์ที่ผ่านมา มีข้อใดบ้าง", "sm b mid")]
    for i, (k, s) in enumerate(qs):
        y = 30 + i * 34
        p += [rect(10, y, 420, 28, "sk", 7), circ(30, y + 14, 10, "acf"), t(30, y + 18, k, "xs b mid"), t(48, y + 18, s, "xs")]
    y = 176
    for x, c, a, b in ((10, "ok", "0 ข้อ", "well controlled"), (152, "ms", "1–2 ข้อ", "partly controlled"), (294, "bad", "3–4 ข้อ", "uncontrolled")):
        p.append(bx(x, y, 136, 42, c, [a, b]))
    p += [rect(10, 230, 420, 54, "wa", 8), t(220, 248, "+ ประเมิน \"ความเสี่ยงในอนาคต\" แยกต่างหาก", "xs b mid"),
          t(220, 264, "exacerbation (เคย ICU/ใส่ท่อ · SABA ≥ 3 กระบอก/ปี · ไม่ใช้ ICS · FEV1 ต่ำ)", "xs mid"),
          t(220, 278, "· persistent airflow limitation · ผลข้างเคียงยา", "xs mid")]
    return fig("ประเมินการควบคุมโรค — 4 คำถาม (GINA)",
               "**อาจารย์: \"จำแค่ 4 ข้อ\"** (ACQ/ACT ไม่ต้องจำตัวเลข) · well controlled คือ **เกณฑ์ขั้นต่ำ** (ยังยอมให้มีอาการ ≤ 2 ครั้ง/สัปดาห์) — เป้าปัจจุบันคือไม่มีเลยสักข้อ (total control → remission) · "
               "อาการคุมได้ดีแต่ยังมีความเสี่ยงสูง (เช่น เพิ่งนอน ICU) ก็ยังต้องจัดการ · ตัวย่อ D-N-R-A ย่อเองเพื่อช่วยจำ",
               svg(440, 292, "สี่คำถามประเมินการควบคุมโรคหืด และการแปลผลเป็น well partly uncontrolled พร้อมกล่องความเสี่ยงในอนาคต", *p))


def f_severity():
    rows = [("", "Mild–moderate", "Severe", "Life-threatening"),
            ("การพูด", "เป็นประโยค/วลี", "เป็นคำ ๆ", "ซึม สับสน"),
            ("ท่าทาง", "นั่งได้ นอนราบได้", "โน้มตัว กระสับกระส่าย", "หมดแรง"),
            ("RR", "เพิ่ม แต่ ≤ 30", "> 30/นาที", "หายใจแผ่ว"),
            ("SpO2 RA", "≥ 92%", "< 92%", "เขียว"),
            ("PEF", "> 50%", "≤ 50%", "< 33% หรือวัดไม่ได้"),
            ("ฟังปอด", "wheeze", "air entry ลด", "silent chest")]
    xs, ws = (10, 82, 198, 314), (72, 116, 116, 116)
    cs = ("sk", "ok", "ms", "bad")
    p = []
    for r, row in enumerate(rows):
        y = 10 + r * 32
        for c in range(4):
            if r == 0 and c == 0:
                continue
            cls = cs[c] if r == 0 else ("bx" if c else "sk")
            p += [rect(xs[c], y, ws[c], 28, cls, 6), t(xs[c] + ws[c] / 2, y + 18, row[c], "xs mid" + (" b" if r == 0 or c == 0 else ""))]
    p += [rect(10, 238, 420, 44, "bad", 8), t(220, 256, "PaCO2 \"ปกติ\" (≈ 40) หรือสูง ในคนที่หอบหนัก = กำลังจะหยุดหายใจ", "xs b mid"),
          t(220, 273, "→ ICU · เตรียมใส่ท่อช่วยหายใจ (ดูภาพเคลื่อนไหวด้านล่าง)", "xs mid")]
    return fig("แบ่งความรุนแรงของ exacerbation ด้วยข้างเตียง",
               "ตัวเลขตามที่นำเสนอในคาบ (GINA primary care) — พูด/ท่าทาง/RR/SpO2/PEF · ช่อง life-threatening รวมเกณฑ์ที่ข้อสอบ Ward Drill ใช้ (BTS/SIGN: PEF < 33%, SpO2 < 92%, PaCO2 ปกติ, silent chest, เขียว, หมดแรง, arrhythmia, ความดันต่ำ, ซึม) · "
               "**ประเมินจากข้างเตียงก่อน ไม่ต้องรอ ABG**",
               svg(440, 290, "ตารางแบ่งความรุนแรงของการกำเริบ mild moderate severe และ life-threatening ตามการพูด ท่าทาง อัตราการหายใจ SpO2 PEF และเสียงปอด", *p))


FIGS = {"chest-ast-02": {"endotype": f_endotype()}, "chest-ast-04": {"pefvar": f_pefvar()},
        "chest-ast-06": {"formo": f_formo()}, "chest-ast-08": {"control": f_control()},
        "chest-ast-10": {"severity": f_severity()}}


# ═════════════════════════════════════════════ ภาพเคลื่อนไหว
# 1 · T2 cascade
def a_cascade():
    p = [bx(10, 10, 130, 46, "ms", ["Allergen", "ไรฝุ่น · แมว · เกสร"]),
         ar(140, 33, 153, 33, "ln w2", "ah"),
         bx(155, 10, 130, 46, "sk", ["Dendritic cell", "+ TSLP จากเยื่อบุ"]),
         ar(285, 33, 298, 33, "ln w2", "ah"),
         bx(300, 10, 130, 46, "ac", ["naive T → Th2", "sensitization"])]
    p.append(S(2, ar(365, 56, 365, 84, "lac w2", "ah-ac"), t(372, 74, "IL-4", "xs b tac"),
               bx(300, 86, 130, 46, "wa", ["B cell → IgE", "class switch"]),
               ar(300, 109, 287, 109, "lwa w2", "ah-wa"),
               bx(155, 86, 130, 46, "ms", ["Mast cell", "เคลือบด้วย IgE"])))
    p.append(S(3, bx(10, 86, 130, 46, "ms", ["สัมผัสซ้ำ", "allergen จับ IgE"]),
               ar(140, 109, 153, 109, "lms w2", "ah-ms"),
               ar(190, 132, 190, 160, "lbad w2", "ah-bad"),
               bx(10, 162, 200, 56, "bad", ["Early phase (นาที)", "histamine · LTC4 · PGD2"]),
               ar(210, 190, 228, 190, "lbad w2", "ah-bad"),
               bx(230, 162, 200, 56, "bad", ["หลอดลมหดเกร็ง บวม", "→ wheeze ใน 15 นาที"])))
    p.append(S(4, t(220, 240, "Late phase (4–8 ชม.)", "sm b mid tac"),
               bx(10, 248, 200, 56, "ac", ["IL-5 → eosinophil", "MBP ทำลายเยื่อบุ"]),
               bx(230, 248, 200, 56, "wa", ["IL-13 → goblet cell", "เมือกเหนียว + AHR"])))
    p.append(S(5, ar(220, 304, 220, 318, "ln w2", "ah"),
               bx(10, 320, 420, 46, "sk", ["อักเสบซ้ำ ๆ → airway remodeling", "กล้ามเนื้อเรียบหนา · พังผืดใต้เยื่อบุ · หลอดเลือดเพิ่ม"]),
               note(376, "ICS ระงับขั้น 2–5 · SABA แก้ได้แค่ผลของขั้น 3", "เหตุผลที่อาจารย์ย้ำว่า \"หอบทุกครั้งต้องได้ ICS คู่เสมอ\"")))
    return SVG(440, 420, "ภาพเคลื่อนไหว: การอักเสบแบบ T2 ใน asthma จาก allergen ผ่าน dendritic cell Th2 IgE mast cell "
               "สู่ early phase late phase และ airway remodeling", *p)


CASCADE_STEPS = [
    {"t": "Sensitization: allergen → dendritic cell → Th2",
     "cap": "dendritic cell ในเยื่อบุจับ allergen แล้วนำเสนอให้ naive T cell · **TSLP** ที่เยื่อบุหลั่งเมื่อถูกกระตุ้นช่วยดันให้เป็น **Th2** · ยังไม่มีอาการ"},
    {"t": "IL-4 → B cell สร้าง IgE → เกาะ mast cell",
     "cap": "**IL-4** ทำให้ B cell เปลี่ยนเป็น plasma cell สร้าง **IgE** ซึ่งไปเกาะบนผิว mast cell — ร่างกาย \"จำ\" allergen ได้แล้ว"},
    {"t": "สัมผัสซ้ำ → early phase ภายในนาที",
     "cap": "allergen จับ IgE บน mast cell → degranulation หลั่ง **histamine, leukotriene C4, PGD2** → กล้ามเนื้อเรียบหดตัว หลอดเลือดรั่ว เยื่อบุบวม · กลับคืนได้ด้วย SABA"},
    {"t": "Late phase 4–8 ชม.: eosinophil และเมือก",
     "cap": "**IL-5** เรียกและยืดอายุ eosinophil ซึ่งหลั่ง **major basic protein** ทำลายเยื่อบุ · **IL-13** เพิ่ม goblet cell เมือกเหนียว และทำให้หลอดลม **ไวเกิน (AHR)** · อาจารย์: \"ที่ต้องจำ IL-4, 5, 13\""},
    {"t": "อักเสบเรื้อรัง → remodeling",
     "cap": "กล้ามเนื้อเรียบหนา พังผืดใต้ basement membrane goblet cell เพิ่ม หลอดเลือดใหม่ → lumen แคบถาวร (persistent airflow limitation) · **ICS** ยับยั้งการอักเสบตั้งแต่ขั้น 2 ส่วน SABA แค่คลายกล้ามเนื้อในขั้น 3"},
]


# 2 · หน้าตัดหลอดลม
def a_airway():
    cx, cy = 120, 150
    p = [circ(cx, cy, 96, "sk"), t(cx, 36, "ผนังหลอดลม", "xs mid mu")]
    p.append('<g data-x="2">%s%s</g>' % (circ(cx, cy, 66, "bx"), t(cx, cy - 30, "lumen ปกติ", "xs mid")))
    p.append(S(2, circ(cx, cy, 70, "lac w5"), circ(cx, cy, 44, "bx"), t(cx, cy + 24, "หดเกร็ง", "xs b mid tac"), x=3))
    p.append(S(3, circ(cx, cy, 70, "lac w5"), circ(cx, cy, 54, "lwa w5"), circ(cx, cy, 30, "bx"),
               ell(cx + 8, cy + 10, 14, 9, "msf"), t(cx, cy - 8, "บวม+เมือก", "xs b mid"), x=4))
    p.append(S(4, circ(cx, cy, 86, "lms w5"), circ(cx, cy, 70, "lac w5"), circ(cx, cy, 54, "lwa w5"), circ(cx, cy, 24, "bx"),
               ell(cx, cy + 6, 9, 6, "msf"), t(cx, 266, "lumen แคบถาวร", "xs b mid tbad")))
    labels = [(1, "ปกติ: ผนังบาง ลมผ่านสะดวก", "tok"), (2, "1 กล้ามเนื้อเรียบหดเกร็ง", "tac"),
              (3, "2 เยื่อบุบวม + เมือกอุด", "twa"), (4, "3 remodeling: ผนังหนาถาวร", "tms"),
              (5, "4 หายใจออก: ช่องแคบ → ผนังสั่น", "tbad")]
    for k, s, c in labels:
        y = 40 + (k - 1) * 34
        node = t(236, y, s, "xs b " + c)
        p.append(node if k == 1 else S(k, node))
    p.append(S(5, path("M30 286 C90 266 150 306 210 286", "lbad w3 fl"), t(120, 312, "ลมเร็วผ่านช่องแคบ = wheeze ตอนหายใจออก", "xs mid tbad"),
               rect(236, 196, 194, 72, "bad", 8), t(333, 214, "ลมน้อยมาก", "xs b mid"), t(333, 230, "→ ไม่มีเสียง wheeze", "xs mid"),
               t(333, 246, "= silent chest", "xs b mid"), t(333, 262, "อันตราย ไม่ใช่ดีขึ้น", "xs mid")))
    return SVG(440, 326, "ภาพเคลื่อนไหว: หน้าตัดหลอดลมจากปกติ สู่กล้ามเนื้อหดเกร็ง เยื่อบุบวมและเมือกอุด remodeling "
               "และการเกิด wheeze กับ silent chest", *p)


AIRWAY_STEPS = [
    {"t": "หลอดลมปกติ", "cap": "แรงต้านทานแปรผกผันกับ **รัศมียกกำลังสี่** (Poiseuille) — รัศมีลดลงครึ่งหนึ่ง แรงต้านเพิ่ม 16 เท่า จึงตีบนิดเดียวก็เหนื่อยมาก"},
    {"t": "กล้ามเนื้อเรียบหดเกร็ง (นาที)", "cap": "จาก mediator ของ mast cell และ vagal reflex · ส่วนนี้ **กลับคืนได้เร็ว** ด้วย β2 agonist → พื้นฐานของ bronchodilator reversibility test"},
    {"t": "เยื่อบุบวม + เมือกอุด (ชั่วโมง–วัน)", "cap": "late phase: eosinophil, IL-13 → เมือกเหนียวอุด · SABA แก้ส่วนนี้ไม่ได้ ต้องใช้ **corticosteroid** — เหตุผลที่ attack รุนแรงต้องให้ systemic steroid เร็ว"},
    {"t": "Remodeling (ปี)", "cap": "อักเสบซ้ำโดยไม่ได้ ICS → ผนังหนาถาวร · reversibility ลดลง กลายเป็น **persistent airflow limitation** ซึ่งไม่จำเพาะกับ COPD"},
    {"t": "Wheeze และ silent chest", "cap": "หายใจออก ความดันในช่องอกกดหลอดลมที่แคบอยู่แล้ว ลมเร็วทำให้ผนังสั่น = **wheeze** · ถ้าตีบมากจนลมแทบไม่ผ่าน เสียงจะหาย = **silent chest** ต้องรักษาด่วน"},
]


# 3 · Flow–volume loop + reversibility
def a_flowvol():
    X = lambda v: 40 + v * 52        # volume L → x
    Y = lambda f: 210 - f * 18        # flow L/s → y
    def loop(pk, vpk, fvc, c, extra=""):
        d = "M%.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f" % (X(0), Y(0), X(vpk), Y(pk), X(fvc * 0.45), Y(pk * 0.25), X(fvc), Y(0))
        return path(d, c + extra)
    p = [line(40, 30, 40, 214, "ln w2"), line(40, 210, 300, 210, "ln w2"), t(44, 26, "Flow (L/s)", "xs b"),
         t(300, 228, "Volume (L)", "xs end mu"), t(X(1.6), Y(7.6), "ปกติ", "xs mu"),
         path("M%.1f %.1f L%.1f %.1f L%.1f %.1f" % (X(0), Y(0), X(0.35), Y(9), X(4.6), Y(0)), "lmu da")]
    p.append(S(2, loop(5.2, 0.35, 3.6, "lbad w3"), t(170, 44, "— ก่อนยา: เว้า (scooped)", "xs b tbad")))
    p.append(S(3, loop(7.0, 0.35, 3.9, "lok w3"), t(170, 60, "— หลัง salbutamol 15 นาที", "xs b tok")))
    p.append(S(4, rect(306, 30, 126, 120, "ok", 8), t(369, 48, "FEV1", "sm b mid"), t(369, 66, "2.10 → 2.45 L", "xs mid"),
               t(369, 84, "+350 mL", "xs b mid"), t(369, 100, "350 ÷ 2100 = 16.7%", "xs mid"),
               t(369, 118, "> 12% และ > 200 mL", "xs b mid tok"), t(369, 136, "= BD test บวก", "xs b mid")))
    p.append(S(5, rect(306, 160, 126, 66, "ms", 8), t(369, 178, "ratio ไม่ใช่", "xs b mid"), t(369, 194, "เกณฑ์วินิจฉัย", "xs b mid"),
               t(369, 210, "asthma", "xs b mid")))
    p.append(S(6, note(240, "ไม่ผ่านเกณฑ์ ≠ ไม่ใช่ asthma", "ทำซ้ำตอนมีอาการ · PEF diary · challenge test · ICS 4 สัปดาห์แล้ววัดซ้ำ")))
    return SVG(440, 290, "ภาพเคลื่อนไหว: flow-volume loop ก่อนและหลังยาขยายหลอดลม พร้อมการคำนวณ FEV1 ที่เพิ่มขึ้นร้อยละ 16.7 และ 350 mL", *p)


FLOWVOL_STEPS = [
    {"t": "Flow–volume loop ปกติ", "cap": "เป่าแรงเต็มที่ ลมพุ่งถึง peak เร็วแล้วลดลงเป็นเส้นเกือบตรง · FEV1 = ปริมาตรที่เป่าออกได้ใน 1 วินาทีแรก"},
    {"t": "ก่อนยา: ช่วงท้ายเว้าลง", "cap": "หลอดลมเล็กตีบ ลมช่วงท้ายไหลช้า เส้นจึง **เว้า (scooped)** · FEV1 ลดมากกว่า FVC"},
    {"t": "หลังพ่น salbutamol 200–400 mcg รอ 10–15 นาที", "cap": "กล้ามเนื้อเรียบคลาย เส้นขยับเข้าหาปกติ · นี่คือ **variable expiratory airflow limitation** ที่ GINA ใช้นิยามโรค"},
    {"t": "คำนวณ: (หลัง − ก่อน) ÷ ก่อน × 100", "cap": "อาจารย์เน้น: ต้อง **> 12% และ > 200 mL ทั้งคู่** (ใน FEV1 หรือ FVC) · ตัวอย่าง 2.10 → 2.45 L = +350 mL, 16.7% → บวก"},
    {"t": "FEV1/FVC < 0.70 ไม่ใช่เกณฑ์ของ asthma", "cap": "อาจารย์: \"ratio จะ 80 จะ 90 จะ 100% ก็ทำ reversibility ได้\" · ratio บอกว่ามี obstruction (ใช้วินิจฉัย COPD) · AI ที่ใช้ข้อมูลเก่ามักตอบผิดตรงนี้"},
    {"t": "ผลลบครั้งแรกไม่ตัดโรค", "cap": "ถ้ายังสงสัย: ตรวจซ้ำตอนมีอาการ · PEF diary 2 สัปดาห์ · methacholine/exercise challenge · ให้ ICS 4 สัปดาห์แล้ววัดซ้ำ (FEV1 > 12% + 200 mL หรือ PEF > 20%)"},
]


# 4 · GINA Track 1 ladder
def a_ladder():
    rows = [(1, 2, "Step 1–2", "AIR: ICS-formoterol ขนาดต่ำ เมื่อมีอาการเท่านั้น", "อาการ < 3–5 วัน/สัปดาห์", "ok"),
            (2, 3, "Step 3", "MART ขนาดต่ำ: เช้า–เย็น + เมื่อมีอาการ", "อาการเกือบทุกวัน / ตื่นกลางคืน / FEV1 ต่ำ", "wa"),
            (3, 4, "Step 4", "MART ขนาดกลาง (ไม่ใช่ high dose แล้ว)", "อาการทุกวัน + FEV1 ต่ำ / มาด้วย exacerbation", "ms"),
            (4, 5, "Step 5", "+ LAMA · ส่งประเมิน phenotype ± biologic", "ยังคุมไม่ได้หลังแก้ทุกปัจจัย", "bad")]
    p = [t(10, 20, "GINA Track 1 (preferred) — ยาหลอดเดียว budesonide-formoterol", "sm b"),
         line(10, 330, 430, 330, "ln w2")]
    for i, k, step, rx, who, c in rows:
        x, y = 10 + (i - 1) * 24, 266 - (i - 1) * 62
        p.append(S(k, rect(x, y, 390 - (i - 1) * 24, 56, c, 8), t(x + 10, y + 18, step, "sm b"),
                   t(x + 10, y + 34, rx, "xs b"), t(x + 10, y + 49, who, "xs i2")))
    p.append(S(6, ar(418, 84, 418, 318, "lok w3", "ah-ok"), t(434, 72, "step down เมื่อคุมดี ≥ 3 เดือน ↓", "xs b end tok"),
               rect(10, 338, 420, 40, "ac", 8), t(220, 355, "ทุก step ไม่มี SABA เดี่ยว · Track 2 = ICS(-LABA) + reliever แยกหลอด", "xs b mid"),
               t(220, 371, "ไทยไม่มี ICS-SABA หลอดเดียว → Track 2 ต้องใช้ 3 หลอด (อาจารย์)", "xs mid")))
    return SVG(440, 384, "ภาพเคลื่อนไหว: บันไดการรักษา GINA Track 1 จาก step 1-2 AIR ถึง step 5 add-on พร้อมลูกศร step down", *p)


LADDER_STEPS = [
    {"t": "ยาหลอดเดียวทุกขั้น: budesonide-formoterol", "cap": "Track 1 ใช้ ICS-formoterol เป็นทั้งยาบรรเทาและยาควบคุม · ลด severe exacerbation ได้มากกว่าแนวทางที่ใช้ SABA เป็น reliever"},
    {"t": "Step 1–2: AIR (anti-inflammatory reliever)", "cap": "พ่นเฉพาะเมื่อมีอาการ — ทุกครั้งที่ได้ formoterol ก็ได้ budesonide ไปด้วย · อาจารย์: \"ทุกครั้งที่คนไข้หอบ ต้องได้ ICS low dose คู่เสมอ\""},
    {"t": "Step 3: MART ขนาดต่ำ", "cap": "budesonide-formoterol 200/6 วันละ 1 สูดเช้า–เย็น + 1 สูดเมื่อมีอาการ (รวมไม่เกิน 12 สูด/วัน) · ใช้ได้เฉพาะ ICS-formoterol"},
    {"t": "Step 4: MART ขนาดกลาง", "cap": "2 สูดเช้า–เย็น + เมื่อมีอาการ · อาจารย์: step 4 ไม่ใช้ high-dose ICS แล้ว เพราะผลข้างเคียงมาก ประสิทธิภาพเพิ่มน้อย · ผู้ป่วยใหม่ที่มาด้วย exacerbation เริ่มที่ step 4 + OCS สั้น ๆ"},
    {"t": "Step 5: add-on", "cap": "เพิ่ม LAMA · ส่งผู้เชี่ยวชาญประเมิน phenotype (eos, FeNO, IgE) เพื่อ biologic · high-dose ICS อยู่ขั้นนี้เท่านั้น"},
    {"t": "Step down + Track 2", "cap": "คุมได้ดี 2–3 เดือน (GINA 3 เดือน) ลดทีละขั้น แต่ไม่หยุด ICS · Track 2 (ICS หรือ ICS-LABA + reliever แยก) ใช้ได้ แต่ในไทยไม่มี ICS-SABA หลอดเดียว จึงยุ่งยากกว่า"},
]


# 5 · pMDI + spacer
def a_inhaler():
    p = [rect(20, 40, 26, 54, "wa", 6), path("M20 94 L20 112 L70 112 L70 100 L46 100 L46 94 Z", "ln w2"),
         t(33, 128, "pMDI", "xs b mid"),
         path("M70 96 L100 84 L240 84 L270 98 L270 106 L240 120 L100 120 L70 108 Z", "lac w2"), t(170, 106, "spacer", "xs mid tac"),
         circ(320, 102, 34, "sk"), circ(310, 92, 3, "inkf"), t(320, 150, "ผู้ป่วย", "xs mid mu")]
    p.append(S(2, path("M30 30 L36 20 M40 30 L46 20", "lac w2"), t(70, 24, "เขย่า · เปิดฝา", "xs b tac")))
    p.append(S(3, path("M352 96 L410 80", "lmu w2 da"), t(436, 62, "หายใจออกนอก spacer", "xs b end mu")))
    p.append(S(4, '<g class="pl">%s</g>' % ell(170, 102, 60, 12, "waf"),
               path("M110 102 L282 102", "lwa w3 fl"), t(170, 76, "กด 1 ครั้ง → สูดช้า ลึก 3–5 วินาที", "xs b mid twa")))
    p.append(S(5, rect(286, 158, 144, 30, "ms", 7), t(358, 177, "กลั้นหายใจ ~10 วินาที", "xs b mid")))
    steps = [(2, "1 เขย่า เปิดฝา ต่อ spacer"), (3, "2 หายใจออกให้สุด นอกปากกระบอก"),
             (4, "3 อมให้สนิท กด 1 ครั้ง สูดช้า ลึก (หรือหายใจปกติ 4–5 ครั้ง)"),
             (5, "4 กลั้นหายใจ ~10 วินาที · พ่นซ้ำรอ 30–60 วินาที"),
             (6, "5 มี ICS → บ้วนปาก กลั้วคอ · ให้ผู้ป่วยทำให้ดู (teach-back)")]
    for k, s in steps:
        y = 210 + (k - 2) * 26
        p.append(S(k, rect(10, y, 420, 22, "bx", 6), t(18, y + 15, s, "xs")))
    p.append(S(6, rect(10, 342, 420, 26, "bad", 7), t(220, 359, "สูดเร็วจนมีเสียงหวีดใน spacer = ผิด (นั่นคือท่าของ DPI)", "xs b mid")))
    return SVG(440, 374, "ภาพเคลื่อนไหว: ขั้นตอนพ่นยา pMDI ผ่าน spacer ตั้งแต่เขย่า หายใจออก กดหนึ่งครั้งแล้วสูดช้า กลั้นหายใจ และบ้วนปาก", *p)


INHALER_STEPS = [
    {"t": "pMDI + spacer", "cap": "spacer ทำให้ละอองช้าลงและเล็กลง ไม่ต้องประสานมือกับการสูด · ยาค้างในคอน้อยลง → ผลข้างเคียงเฉพาะที่ของ ICS ลดลง"},
    {"t": "เขย่า เปิดฝา ต่อ spacer", "cap": "pMDI เป็นยาแขวนตะกอน ต้องเขย่าก่อนทุกครั้ง · หลอดใหม่หรือไม่ได้ใช้นานให้พ่นทิ้งตามเอกสารกำกับ"},
    {"t": "หายใจออกให้สุด — ไม่เป่าเข้าอุปกรณ์", "cap": "เตรียมปอดให้ว่างเพื่อสูดได้ลึก · เป่าเข้า spacer ทำให้ยาเปียกติดผนัง"},
    {"t": "กด 1 ครั้ง สูดช้าและลึก", "cap": "pMDI ต้องสูด **ช้า 3–5 วินาที** (ต่างจาก DPI ที่ต้องสูดแรงเร็ว) หรือหายใจปกติ 4–5 ครั้งผ่าน spacer · กดครั้งเดียวต่อการสูดหนึ่งชุด"},
    {"t": "กลั้นหายใจ ~10 วินาที", "cap": "ให้ละอองตกตะกอนในหลอดลมเล็ก · ถ้าต้องพ่นซ้ำ รอ 30–60 วินาทีแล้วเขย่าใหม่"},
    {"t": "บ้วนปาก + teach-back", "cap": "ยาที่มี ICS → บ้วนปากกลั้วคอ ลด **oral candidiasis และเสียงแหบ** · ข้อผิดพลาดที่พบบ่อย: สูดเร็วเกิน กดหลายครั้ง ไม่กลั้นหายใจ · ตรวจท่าพ่นทุกครั้งก่อน step up"},
]


# 6 · PaCO2 ใน acute severe asthma
def a_paco2():
    X = lambda m: 50 + m * 1.3          # นาที 0–280 → x
    Y = lambda c: 230 - (c - 20) * 4.2  # PaCO2 → y
    p = [line(50, 40, 50, 234, "ln w2"), line(50, 230, 420, 230, "ln w2"), t(54, 34, "PaCO2 (mmHg)", "xs b"),
         t(420, 248, "เวลาตั้งแต่เริ่มหอบ", "xs end mu"),
         rect(50, Y(45), 370, Y(35) - Y(45), "ok", 0), t(416, Y(40) + 4, "ช่วงปกติ 35–45", "xs end tok")]
    for c in (20, 30, 40, 50, 60):
        p.append(t(46, Y(c) + 4, str(c), "xs end mu"))
    p.append(S(2, path("M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (X(0), Y(40), X(30), Y(28), X(80), Y(28)), "lwa w3"),
               t(X(40), Y(24), "หายใจเร็ว → PaCO2 ต่ำ (คาดได้)", "xs b twa")))
    p.append(S(3, path("M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (X(80), Y(28), X(130), Y(29), X(165), Y(38)), "lms w3"),
               t(X(120), Y(52), "air trapping + กล้ามเนื้อล้า", "xs b tms")))
    p.append(S(4, '<g class="pl">%s</g>' % circ(X(172), Y(40), 7, "badf"),
               t(X(172) - 12, Y(42) + 2, "PaCO2 \"ปกติ\" = อันตราย!", "xs b end tbad")))
    p.append(S(5, path("M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (X(165), Y(38), X(210), Y(46), X(270), Y(62)), "lbad w3"),
               t(X(262), Y(60), "type 2 respiratory failure", "xs b end tbad"),
               note(258, "ICU · ตามแพทย์อาวุโส · เตรียมใส่ท่อช่วยหายใจ", "MgSO4 2 g IV · ventilator: RR ต่ำ expiratory time ยาว permissive hypercapnia")))
    return SVG(440, 306, "ภาพเคลื่อนไหว: กราฟ PaCO2 ระหว่างหอบหืดรุนแรง เริ่มต่ำจากหายใจเร็ว แล้วไต่กลับสู่ค่าปกติเมื่อกล้ามเนื้อล้า และสูงเกินในระยะหายใจล้มเหลว", *p)


PACO2_STEPS = [
    {"t": "ค่าปกติ 35–45 mmHg", "cap": "ในหอบหืดกำเริบ ร่างกายควรหายใจเร็วจากความรู้สึกเหนื่อยและ hypoxemia — PaCO2 จึง **ควรต่ำ**"},
    {"t": "ช่วงแรก: PaCO2 ต่ำ = respiratory alkalosis", "cap": "เป็นสิ่งที่คาดได้ · hypoxemia มาจาก V/Q mismatch (ถุงลมหลังหลอดลมตีบได้ลมน้อย) แก้ได้ด้วย O2 ไม่มาก"},
    {"t": "PaCO2 ไต่ขึ้น", "cap": "air trapping ทำให้ปอดพอง กะบังลมแบน กล้ามเนื้อหายใจทำงานเสียเปรียบจนล้า · tidal volume ลด dead space เพิ่ม → ขับ CO2 ไม่ทัน"},
    {"t": "PaCO2 \"ปกติ\" ในคนที่หอบหนัก = สัญญาณอันตราย", "cap": "ไม่ใช่ดีขึ้น แต่เป็นจุดข้ามสู่การหายใจล้มเหลว · พบร่วมกับ silent chest, ซึม, พูดไม่ได้ · ข้อสอบ Ward Drill ชอบออกจุดนี้"},
    {"t": "PaCO2 สูง → ICU / ใส่ท่อ", "cap": "ให้ MgSO4 IV · ตามแพทย์อาวุโส/ICU · ถ้าใส่ท่อ ตั้ง RR ต่ำ expiratory time ยาว ยอมให้ CO2 สูง (permissive hypercapnia) เพื่อไม่ให้ลมค้างจนเกิด auto-PEEP"},
]


ITEMS = [
    {"sec": "chest-ast-02", "after": "การอักเสบแบบ T2 ทีละขั้น",
     "anim": {"key": "ast-cascade", "title": "T2 cascade — จาก allergen ถึง remodeling", "svg": a_cascade(), "steps": CASCADE_STEPS}},
    {"sec": "chest-ast-03", "after": "ทำไมถึงมีอาการนี้",
     "anim": {"key": "ast-airway", "title": "หน้าตัดหลอดลม — หดเกร็ง บวม เมือก remodeling และ wheeze", "svg": a_airway(), "steps": AIRWAY_STEPS}},
    {"sec": "chest-ast-04", "after": "Spirometry และ bronchodilator responsiveness",
     "anim": {"key": "ast-flowvol", "title": "Flow–volume loop ก่อน–หลังยาขยายหลอดลม", "svg": a_flowvol(), "steps": FLOWVOL_STEPS}},
    {"sec": "chest-ast-07", "after": "Track 1 — ทางที่แนะนำ",
     "anim": {"key": "ast-ladder", "title": "บันได GINA Track 1 — AIR → MART → add-on", "svg": a_ladder(), "steps": LADDER_STEPS}},
    {"sec": "chest-ast-09", "after": "pMDI กับ spacer",
     "anim": {"key": "ast-inhaler", "title": "พ่นยา pMDI ผ่าน spacer ทีละขั้น", "svg": a_inhaler(), "steps": INHALER_STEPS}},
    {"sec": "chest-ast-10", "after": "PaCO2 ปกติ = อันตราย",
     "anim": {"key": "ast-paco2", "title": "PaCO2 ระหว่างหอบรุนแรง — ค่า \"ปกติ\" ที่อันตราย", "svg": a_paco2(), "steps": PACO2_STEPS}},
]

MNEM = [
    {"sec": "chest-ast-04", "name": "12 + 200 ทั้งคู่", "what": "เกณฑ์ bronchodilator responsiveness ในผู้ใหญ่ (GINA)",
     "lines": [["12", "FEV1 หรือ FVC เพิ่ม **> 12%** จากค่าก่อนยา"], ["200", "และเพิ่ม **> 200 mL**"],
               ["ไม่มี 0.7", "FEV1/FVC < 0.70 **ไม่ใช่** เกณฑ์ของ asthma"]],
     "note": "อาจารย์ย้ำ \"ต้องมีทั้ง 2 ข้อ\" · PEF ก่อน–หลังยาใช้เกณฑ์ > 20% · หลัง ICS 4 สัปดาห์ใช้เกณฑ์เดียวกัน",
     "src": "ย่อเพิ่มเพื่อช่วยจำ — ไม่ใช่หลักจำมาตรฐาน (ตัวเลขจาก GINA 2024)"},
    {"sec": "chest-ast-08", "name": "D-N-R-A", "what": "4 คำถามประเมิน symptom control ใน 4 สัปดาห์",
     "lines": [["D", "**D**ay — อาการกลางวัน > 2 ครั้ง/สัปดาห์"], ["N", "**N**ight — ตื่นกลางคืนเพราะหืด"],
               ["R", "**R**eliever — ใช้ยาบรรเทา > 2 ครั้ง/สัปดาห์"], ["A", "**A**ctivity — กิจกรรมถูกจำกัด"]],
     "note": "0 ข้อ = well · 1–2 = partly · 3–4 = uncontrolled",
     "src": "ย่อเพิ่มเพื่อช่วยจำ — ไม่ใช่หลักจำมาตรฐาน (คำถามจาก GINA symptom control tool)"},
    {"sec": "chest-ast-10", "name": "33-92-CHEST", "what": "ลักษณะของ life-threatening asthma",
     "lines": [["33", "PEF **< 33%** ของค่าดีที่สุด/คาดการณ์"], ["92", "SpO2 **< 92%**"], ["C", "**C**yanosis"],
               ["H", "**H**ypotension"], ["E", "**E**xhaustion · ซึม สับสน"], ["S", "**S**ilent chest · หายใจแผ่ว"],
               ["T", "**T**achy-/bradyarrhythmia"]],
     "note": "เกณฑ์ BTS/SIGN · เพิ่ม: PaCO2 \"ปกติ\" (35–45 mmHg) ในผู้ป่วยหอบหนัก · GINA ใช้คำว่า drowsy/confused/silent chest",
     "src": "หลักจำที่ใช้กันแพร่หลายในโรงเรียนแพทย์สหราชอาณาจักร อิงเกณฑ์ BTS/SIGN British guideline on the management of asthma"},
    {"sec": "chest-ast-11", "name": "O SHIT ME", "what": "ลำดับยาใน acute severe asthma ที่โรงพยาบาล",
     "lines": [["O", "**O**xygen — เป้า SpO2 93–95% (GINA)"], ["S", "**S**albutamol พ่นซ้ำ/ต่อเนื่อง"],
               ["H", "**H**ydrocortisone IV หรือ prednisolone กิน"], ["I", "**I**pratropium (รายรุนแรง)"],
               ["T", "**T**heophylline/aminophylline — ไม่แนะนำเป็นยาประจำแล้ว"], ["M", "**M**agnesium sulfate 2 g IV"],
               ["E", "**E**scalate — ICU/วิสัญญี ถ้าไม่ดีขึ้น"]],
     "note": "GINA ไม่แนะนำ aminophylline (ผลข้างเคียงมาก ประโยชน์น้อย) · steroid กินได้ผลเท่า IV ถ้ากลืนได้",
     "src": "หลักจำที่นักศึกษาแพทย์ใช้กันทั่วไป (UK — acute asthma management \"O SHIT ME\")"},
    {"sec": "chest-ast-12", "name": "Samter's triad", "what": "Aspirin-exacerbated respiratory disease (AERD/N-ERD)",
     "lines": [["1", "**Asthma** (มักเริ่มวัยผู้ใหญ่ รุนแรง)"], ["2", "**Chronic rhinosinusitis with nasal polyps** · ได้กลิ่นลดลง"],
               ["3", "**Aspirin/NSAID** → หอบ คัดจมูก หน้าแดง ใน 30–120 นาที"]],
     "note": "กลไก: ยับยั้ง COX-1 → arachidonic acid ไปทาง 5-lipoxygenase → cysteinyl leukotriene สูง + PGE2 ต่ำ · paracetamol (ขนาดต่ำ) และ COX-2 inhibitor มักใช้ได้",
     "src": "First Aid for the USMLE Step 1 (Respiratory — aspirin-exacerbated respiratory disease) · ตำราอายุรศาสตร์มาตรฐาน"},
    {"sec": "chest-ast-08", "name": "Remission 4 ไม่", "what": "เกณฑ์ clinical remission ตามที่อาจารย์สอน",
     "lines": [["ไม่มีอาการ", "ไม่ใช่ \"มีนิดหน่อย\" — ต้องไม่มีเลย"], ["ไม่กำเริบ", "ไม่มี exacerbation"],
               ["ไม่ใช้ OCS", "ทั้งกินประจำและกินเป็นคอร์ส"], ["ปอดไม่แย่", "lung function ปกติ/คงที่"]],
     "note": "complete remission = 4 ข้อ + biomarker (eos, FeNO) กลับปกติ + หลอดลมไม่ไวเกินแล้ว · remission ≠ หายขาด",
     "src": "ย่อเพิ่มเพื่อช่วยจำ — ไม่ใช่หลักจำมาตรฐาน (เนื้อหาจากคาบ · GINA 2024 / Menzies-Gow 2020 consensus)"},
    {"sec": "chest-ast-13", "name": "Biologic → เป้า", "what": "จับคู่ยา biologic กับเป้าหมาย (อ่านเพิ่มเติม)",
     "lines": [["Omalizumab", "anti-**IgE**"], ["Mepolizumab · Reslizumab", "anti-**IL-5**"], ["Benralizumab", "anti-**IL-5 receptor α**"],
               ["Dupilumab", "anti-**IL-4 receptor α** (บล็อก IL-4 และ IL-13)"], ["Tezepelumab", "anti-**TSLP** (alarmin ต้นทาง)"]],
     "note": "ชื่อที่มี \"-li-/-lu-\" ไม่ได้บอกเป้า ต้องจำคู่ · อาจารย์ชี้ว่าปัจจุบันเน้นบล็อก \"ต้นทาง\" (TSLP, IL-4R) มากกว่า IgE อย่างเดียว",
     "src": "ตารางช่วยจำ ย่อเอง — ไม่ใช่หลักจำมาตรฐาน (ข้อมูลยาจาก GINA 2024 severe asthma guide)"},
]


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "anims_chest_ast.json"
    json.dump({"set": "chest", "items": ITEMS, "mnem": MNEM}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("anims %d · mnem %d · figs %d → %s" % (len(ITEMS), len(MNEM), sum(len(v) for v in FIGS.values()), out))
