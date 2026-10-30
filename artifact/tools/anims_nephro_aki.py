# -*- coding: utf-8 -*-
"""ภาพเคลื่อนไหวกลไก (section.anims) + หลักจำ (section.mnem) ของคาบ nephro 42 "Acute kidney injury" (พญ.วรรณิยา)
build_aki.py นำ ITEMS/MNEM ไปใส่ในหัวข้อ · รูปแบบตาม dashboard/learn_anim/SPEC.md
ตรวจ:  python3 anims_nephro_aki.py <out.json>  แล้ว  python3 ../../dashboard/anim_tool.py check <data ที่ยังไม่มี anims ของคาบนี้> <out.json>
แผนภาพเป็น "ภาพจำลองกลไก" ไม่ใช่สัดส่วนจริง · ใช้สีธีม (สลับโหมดมืดได้)"""
import json, re, sys
from svg import t, rect, circ, ell, line, ar, path, poly, esc


def S(k, *parts, x=None):
    a = ' data-s="%d"' % k + ((' data-x="%d"' % x) if x else "")
    return "<g%s>%s</g>" % (a, "".join(p for p in parts if p))


def X(k, *parts):
    return '<g data-x="%d">%s</g>' % (k, "".join(p for p in parts if p))


def G(c, *parts):
    return '<g class="%s">%s</g>' % (c, "".join(p for p in parts if p))


def mover(r, c, dur, d, begin="0s"):
    nums = [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", d)]
    x0, y0 = nums[0], nums[1]
    pts = [(nums[i] - x0, nums[i + 1] - y0) for i in range(0, len(nums), 2)]
    rel = "M0 0 " + " ".join("L%g %g" % p for p in pts[1:])
    return ('<circle cx="%g" cy="%g" r="%s" class="%s"><animateMotion dur="%s" begin="%s" repeatCount="indefinite" path="%s"/></circle>'
            % (x0, y0, r, c, dur, begin, rel))


def SVG(w, h, label, *parts):
    return ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg">' % (w, h, esc(label))
            + "".join(p for p in parts if p) + "</svg>")


def note(y, s1, s2=None, c="ac", h=None):
    h = h or (40 if s2 else 28)
    out = [rect(10, y, 420, h, c, 8), t(220, y + (17 if s2 else 18), s1, "sm b mid")]
    if s2:
        out.append(t(220, y + 33, s2, "xs mid"))
    return "".join(out)


# ───────────────────────── 1 · KDIGO: GFR ตกทันที แต่ Cr ค่อย ๆ ขึ้น
def a_crlag():
    p = [line(50, 30, 50, 230, "ln w2"), line(50, 230, 430, 230, "ln w2"),
         t(44, 26, "%", "xs end mu"), t(430, 248, "วัน 0 · 1 · 2 · 3 · 4 · 5", "xs end mu"),
         t(58, 44, "GFR", "sm b twa"),
         # GFR line: 100% then drop to 30% at day 0.5
         path("M52 60 L110 60", "lwa w3")]
    p.append(S(2, path("M110 60 L112 180 L428 180", "lwa w3"), t(118, 196, "GFR ตกทันที → 30%", "xs b twa")))
    # creatinine curve: x 110 -> 428, rising to 3.3x
    p.append(S(3, path("M52 214 L110 214 C170 200 220 150 280 112 C340 80 390 70 428 66", "lbad w3"),
               t(300, 100, "Cr ค่อย ๆ ขึ้น", "xs b tbad"), t(300, 114, "(สะสมทีละวัน)", "xs tbad")))
    for y, lab, c in ((172, "×1.5", "tms"), (140, "×2", "tbad"), (106, "×3", "tbad")):
        p.append(S(4, line(52, y, 428, y, "lmu da"), t(56, y - 3, lab, "xs b " + c)))
    p.append(S(4, t(214, 168, "วันที่ ~1", "xs mid"), t(240, 136, "วันที่ ~2", "xs mid"), t(318, 102, "~3–4", "xs mid")))
    p.append(S(5, rect(122, 36, 180, 40, "ac", 7), t(212, 52, "ปัสสาวะลดตั้งแต่ชั่วโมงแรก ๆ", "xs b mid"),
               t(212, 68, "✍️ biomarker / cystatin C เร็วกว่า Cr", "xs mid")))
    p.append(note(258, "Cr เป็น \"สัญญาณที่มาช้า\" ของ GFR", "stage ที่เห็นวันแรกอาจต่ำกว่าความจริง → ติดตาม Cr + UO ทุกวัน"))
    return SVG(440, 306, "ภาพเคลื่อนไหว: GFR ลดลงทันทีเมื่อไตบาดเจ็บ แต่ creatinine ค่อย ๆ สูงขึ้นทีละวัน "
               "จึงข้ามเกณฑ์ KDIGO ช้ากว่าการบาดเจ็บจริง ปัสสาวะและ biomarker เปลี่ยนเร็วกว่า", *p)


CRLAG_STEPS = [
    {"t": "ก่อนป่วย: GFR 100% · Cr คงที่",
     "cap": "creatinine ในเลือดคงที่เมื่อ **การสร้างจากกล้ามเนื้อ = การขับทางไต** (steady state)"},
    {"t": "ไตบาดเจ็บ: GFR ตกทันที",
     "cap": "เช่น ความดันตกช่วงผ่าตัด → GFR เหลือ 30% ภายในชั่วโมง แต่ **Cr วันนั้นยังเกือบปกติ** เพราะ creatinine ยังไม่ทันสะสม"},
    {"t": "Cr ค่อย ๆ ขึ้นจนถึง steady state ใหม่",
     "cap": "ขับได้น้อยกว่าที่สร้าง → creatinine สะสม **ทีละวัน** ใช้หลายวันกว่าจะนิ่ง · ✍️ ผู้สูงอายุ/กล้ามเนื้อน้อย/ขาดอาหาร สร้าง Cr น้อย → Cr ขึ้นช้าและต่ำกว่าความจริง"},
    {"t": "ข้ามเกณฑ์ KDIGO ×1.5 · ×2 · ×3 ทีละวัน",
     "cap": "การบาดเจ็บเท่าเดิม แต่ stage \"ดูเหมือน\" แย่ลงทุกวันเพราะ Cr กำลังไล่ตาม GFR · จึงจัด stage จาก **ค่าสูงสุด** และเทียบกับ baseline"},
    {"t": "สัญญาณที่เร็วกว่า: UO · cystatin C · biomarker",
     "cap": "ปัสสาวะลดได้ตั้งแต่ชั่วโมงแรก (เกณฑ์ UO ของ KDIGO) · ✍️ อาจารย์: urine biomarker ช่วยวินิจฉัยเร็ว · serum cystatin C ใช้ร่วมกับ Cr ในผู้ขาดอาหาร/ผู้สูงอายุ"},
]


# ───────────────────────── 2 · pre / intra / post — ปัญหาอยู่ตรงไหน
def a_where():
    p = [
        # heart
        ell(70, 70, 34, 30, "bad"), t(70, 74, "หัวใจ", "xs b mid"),
        path("M104 70 L170 70", "lbad w5 fl"), t(136, 62, "เลือด", "xs mid mu"),
        # kidney
        ell(220, 80, 46, 58, "ac"), t(220, 76, "ไต", "sm b mid"), t(220, 92, "glom·tubule", "xs mid"), t(220, 104, "interstitium", "xs mid"),
        # ureter, bladder, urethra
        path("M220 138 L220 200", "lwa w5 fl"), ell(220, 228, 40, 26, "wa"), t(220, 232, "กระเพาะ", "xs b mid"),
        path("M220 254 L220 288", "lwa w3 fl"), t(232, 284, "ท่อปัสสาวะ", "xs mu"),
    ]
    p.append(S(2, G("pl", circ(136, 70, 22, "ms")), t(136, 118, "PRE-RENAL", "sm b mid tms"),
               t(136, 132, "เลือดไปไตไม่พอ", "xs mid")))
    p.append(S(3, G("pl", circ(220, 80, 30, "bad")), rect(276, 50, 150, 58, "bad", 8),
               t(351, 68, "INTRINSIC (4 กลุ่ม)", "xs b mid"), t(351, 84, "vascular · GN", "xs mid"), t(351, 98, "AIN · ATN", "xs mid")))
    p.append(S(4, G("pl", circ(220, 200, 16, "ms")), rect(276, 196, 150, 58, "wa", 8),
               t(351, 214, "POST-RENAL", "xs b mid"), t(351, 230, "อุดทั้งสองข้าง", "xs mid"), t(351, 244, "(หรือไตข้างเดียว)", "xs mid")))
    p.append(S(5, note(300, "หาจาก \"ง่ายและแก้ได้เร็ว\" ก่อน", "pre-renal (ให้น้ำ) · post-renal (ระบาย) → แล้วจึงไล่ intrinsic")))
    return SVG(440, 348, "ภาพเคลื่อนไหว: ทางเดินจากหัวใจสู่ไตสู่กระเพาะปัสสาวะ แสดงตำแหน่งของ AKI แบบ pre-renal intrinsic และ post-renal", *p)


WHERE_STEPS = [
    {"t": "ทางเดิน: หัวใจ → ไต → กระเพาะปัสสาวะ",
     "cap": "ปัสสาวะต้องอาศัย 3 อย่าง: **เลือดไปไตพอ · เนื้อไตทำงาน · ทางระบายไม่อุด** — แต่ละจุดที่เสียคือกลุ่มสาเหตุหนึ่ง"},
    {"t": "Pre-renal: เลือดไปไตไม่พอ",
     "cap": "เนื้อไตปกติ แต่ renal blood flow ลด → GFR ลด · แก้ทันเวลา **กลับคืนได้** (สไลด์ p7)"},
    {"t": "Intrinsic: เนื้อไตเสีย 4 กลุ่ม",
     "cap": "สไลด์ p12: **renal vascular disorder · acute GN · AIN · ATN** — แยกด้วย UA เป็นหลัก"},
    {"t": "Post-renal: ทางระบายอุด",
     "cap": "ต้องอุด **ทั้งสองข้าง** (ท่อไตสองข้าง กระเพาะ ท่อปัสสาวะ) หรืออุดข้างเดียวในคนที่มีไตทำงานข้างเดียว · อาจารย์ยังจัด **crystal ในท่อไต** เป็น \"intrarenal obstruction\" ด้วย"},
    {"t": "ลำดับคิด: ตัด pre/post ที่แก้ง่ายก่อน",
     "cap": "ประเมินน้ำและการไหลเวียน → ultrasound/bladder scan ตัดการอุดตัน → ค่อยไล่ intrinsic ด้วย UA ดัชนีปัสสาวะ และแล็บเฉพาะ"},
]


# ───────────────────────── 3 · Afferent/efferent — NSAID · ACEi · triple whammy
def a_glom():
    p = [t(220, 20, "glomerulus: แรงดันกรอง (P_GC) กำหนด GFR", "sm b mid"),
         path("M20 120 L150 120", "lbad w5 fl"), t(60, 108, "afferent", "xs mu"),
         circ(200, 120, 48, "bad"), t(200, 116, "P_GC", "sm b mid"),
         path("M248 120 L410 120", "lbad w3 fl"), t(330, 108, "efferent", "xs mu"),
         path("M200 168 L200 210", "lwa w5 fl"), t(212, 204, "GFR", "sm b twa")]
    # normal compensation
    p.append(S(2, rect(14, 146, 132, 38, "ok", 7), t(80, 162, "PG ขยาย afferent", "xs b mid"), t(80, 176, "(prostaglandin)", "xs mid"),
               rect(262, 146, 150, 38, "ok", 7), t(337, 162, "AngII หด efferent", "xs b mid"), t(337, 176, "พยุง P_GC", "xs mid"),
               t(220, 240, "เลือดน้อย แต่ GFR ยังพอ (autoregulation)", "xs b mid tok"), x=3))
    # NSAID
    p.append(S(3, rect(70, 112, 60, 16, "ms", 3), t(100, 100, "NSAID: afferent หด", "xs b mid tbad"),
               ar(100, 136, 100, 150, "lbad", "ah-bad")))
    # ACEi
    p.append(S(4, rect(290, 104, 90, 32, "wa", 6), t(335, 98, "ACEi/ARB: efferent คลาย", "xs b mid tbad")))
    p.append(S(5, rect(14, 226, 412, 56, "bad", 8),
               t(220, 246, "Triple whammy: ขาดน้ำ/diuretic + NSAID + ACEi/ARB", "sm b mid"),
               t(220, 266, "เข้าน้อย (afferent) + ออกง่าย (efferent) → P_GC ตก → GFR ตก", "xs mid")))
    p.append(S(5, G("pl", circ(200, 120, 20, "ms")), t(200, 124, "↓", "lg b mid")))
    return SVG(440, 292, "ภาพเคลื่อนไหว: ในภาวะเลือดไปไตน้อย prostaglandin ขยายหลอดเลือดขาเข้า angiotensin II หดหลอดเลือดขาออกเพื่อพยุงแรงดันกรอง "
               "NSAID ทำให้ขาเข้าหด ACE inhibitor ทำให้ขาออกคลาย เมื่อรวมกับการขาดน้ำแรงดันกรองและ GFR จึงตก", *p)


GLOM_STEPS = [
    {"t": "GFR ขึ้นกับแรงดันใน glomerulus (P_GC)",
     "cap": "P_GC ถูกคุมโดย **ขาเข้า (afferent)** และ **ขาออก (efferent)** — เปรียบเหมือนก๊อกน้ำเข้าและก๊อกน้ำออกของสายยาง"},
    {"t": "เลือดน้อย: ไตชดเชย 2 ทาง",
     "cap": "**prostaglandin ขยาย afferent** ให้เลือดเข้ามาก และ **angiotensin II หด efferent** ให้แรงดันค้าง → GFR ยังพอได้แม้ความดันต่ำ (ดูคาบ Physio1 เรื่อง autoregulation)"},
    {"t": "NSAID: ปิดก๊อกขาเข้า",
     "cap": "NSAID ยับยั้ง COX → ไม่มี prostaglandin มาขยาย afferent → เลือดเข้า glomerulus ลด · ✍️ อาจารย์วงไว้ว่าเป็นสาเหตุสำคัญของ severe renal vasoconstriction"},
    {"t": "ACEi/ARB: เปิดก๊อกขาออก",
     "cap": "ไม่มี angiotensin II หด efferent → แรงดันรั่วออกทางขาออก → P_GC ตก · ปกติ Cr ขึ้นได้เล็กน้อย (≤30%) แต่ในคนขาดน้ำ GFR จะตกมาก"},
    {"t": "Triple whammy",
     "cap": "**ขาดน้ำหรือ diuretic + NSAID + ACEi/ARB** = เลือดน้อย + ขาเข้าหด + ขาออกคลาย → GFR ตกรุนแรง · ป้องกัน: หยุดยาเหล่านี้ชั่วคราวเมื่อท้องเสีย/อาเจียน/กินไม่ได้ (sick day rule)"},
]


# ───────────────────────── 4 · Cardiorenal: แรงดันหลอดเลือดดำย้อนเข้าไต
def a_crs():
    p = [t(220, 20, "แรงดันกรองสุทธิ = แรงดันเข้า − แรงดันออก", "sm b mid"),
         ell(90, 120, 54, 48, "bad"), t(90, 116, "หัวใจ", "sm b mid"), t(90, 132, "EF ต่ำ", "xs mid"),
         ell(310, 120, 52, 62, "ac"), t(310, 116, "ไต", "sm b mid"), t(310, 132, "(มีแคปซูล)", "xs mid"),
         path("M144 104 L258 104", "lbad w3 fl"), t(200, 96, "เลือดแดงออก", "xs mid mu"),
         path("M258 140 L144 140", "lwa w3 fl"), t(200, 156, "เลือดดำกลับ", "xs mid mu")]
    p.append(S(2, rect(140, 98, 120, 12, "msf", 3), t(200, 84, "forward: CO ลด", "xs b mid tms")))
    p.append(S(3, rect(140, 134, 120, 14, "waf", 3), t(200, 176, "backward: CVP สูง (JVP 12)", "xs b mid twa"),
               G("pl", ell(310, 120, 60, 70, "lwa w3"))))
    p.append(S(4, rect(16, 196, 408, 54, "bad", 8),
               t(220, 216, "ความดันในหลอดเลือดดำไต + ในเนื้อไตสูง", "sm b mid"),
               t(220, 236, "แรงดันกรองสุทธิลด · RAAS/ADH ทำงาน → Na/น้ำคั่งต่อ", "xs mid")))
    p.append(S(5, rect(16, 258, 408, 54, "ok", 8),
               t(220, 278, "รักษา: ขับน้ำออก (IV loop diuretic) ไม่ใช่ให้น้ำ", "sm b mid"),
               t(220, 298, "Cr ขึ้นเล็กน้อยระหว่าง decongest มักยอมรับได้", "xs mid")))
    return SVG(440, 320, "ภาพเคลื่อนไหว: ใน cardiorenal syndrome แรงดันหลอดเลือดดำที่สูงย้อนเข้าไต ทำให้แรงดันกรองสุทธิลด "
               "การรักษาคือขับน้ำออกด้วยยาขับปัสสาวะ", *p)


CRS_STEPS = [
    {"t": "หัวใจกับไตเชื่อมกันทั้งขาไปและขากลับ",
     "cap": "GFR ขึ้นกับ **แรงดันที่ดันเลือดเข้า** และ **แรงดันที่ต้านขาออก** — ไม่ใช่แค่ cardiac output"},
    {"t": "Forward failure: cardiac output ลด",
     "cap": "สไลด์ p8: \"decrease cardiac output\" เป็นสาเหตุ pre-renal · ✍️ amphetamine และ alcohol ทำให้กล้ามเนื้อหัวใจเสีย"},
    {"t": "Backward failure: CVP สูงย้อนเข้าไต",
     "cap": "ในผู้ป่วย HF ที่บวมมาก **venous congestion** เป็นตัวขับที่สำคัญกว่า low output (cardiorenal type 1) · ไตมีแคปซูล ความดันในเนื้อไตจึงขึ้นตาม"},
    {"t": "ผล: แรงดันกรองลด + RAAS",
     "cap": "แรงดันฝั่งหลอดเลือดดำ/เนื้อไตสูง → แรงดันกรองสุทธิลด → GFR ลด · ไตคิดว่าขาดน้ำ (U Na ต่ำ) จึงเก็บ Na/น้ำเพิ่ม วนเป็นวงจร"},
    {"t": "รักษาที่ congestion",
     "cap": "**IV loop diuretic ให้ขับน้ำออก** ร่วมกับติดตามปัสสาวะ/Na ในปัสสาวะ · การให้น้ำเกลือทำให้แย่ลง (cardiorenal อิงตำรา/แนวทาง HF ไม่อยู่ในสไลด์)"},
]


# ───────────────────────── 5 · TMA: ลิ่มเกล็ดเลือดในหลอดเลือดเล็ก
def a_tma():
    p = [t(220, 20, "หลอดเลือดฝอยใน glomerulus", "sm b mid"),
         path("M20 70 L420 70", "ln w2"), path("M20 150 L420 150", "ln w2"),
         path("M20 110 L420 110", "lbad da fl"),
         mover(7, "badf", "4s", "M24 100 L416 100"), mover(7, "badf", "4.6s", "M24 122 L416 122", "1s")]
    p.append(S(2, G("pl", ell(210, 92, 34, 20, "ms"), ell(250, 132, 28, 16, "ms")),
               t(210, 96, "PLT", "xs b mid"), t(250, 136, "PLT", "xs b mid"), t(220, 172, "ลิ่มเกล็ดเลือดอุดหลอดเลือดเล็ก", "xs b mid tms")))
    p.append(S(3, path("M300 96 l8 -6 l6 8 z", "badf"), path("M330 120 l10 0 l-4 8 z", "badf"), path("M360 100 l6 6 l-9 3 z", "badf"),
               t(340, 60, "RBC ถูกเฉือน → schistocyte", "xs b mid tbad")))
    p.append(S(4, rect(14, 186, 200, 66, "bad", 8), t(114, 204, "MAHA", "sm b mid"), t(114, 222, "Hb ↓ LDH ↑ haptoglobin ↓", "xs mid"),
               t(114, 238, "schistocytes", "xs mid"),
               rect(226, 186, 200, 66, "ms", 8), t(326, 204, "PLT ต่ำ", "sm b mid"), t(326, 222, "ถูกใช้ไปในลิ่ม", "xs mid"),
               t(326, 238, "ห้ามให้ PLT ถ้าไม่เลือดออก", "xs mid")))
    p.append(S(5, rect(14, 260, 412, 56, "ac", 8), t(220, 280, "glomerulus ขาดเลือด → AKI · สมองขาดเลือด → ✍️ neuro", "xs b mid"),
               t(220, 300, "TTP (ADAMTS13 < 10%) → plasma exchange ด่วน", "sm b mid")))
    return SVG(440, 324, "ภาพเคลื่อนไหว: ลิ่มเกล็ดเลือดอุดหลอดเลือดฝอย เม็ดเลือดแดงถูกเฉือนเป็น schistocyte เกิด MAHA เกล็ดเลือดต่ำ และไตกับสมองขาดเลือด", *p)


TMA_STEPS = [
    {"t": "เลือดไหลผ่านหลอดเลือดฝอยปกติ",
     "cap": "ผนังหลอดเลือด (endothelium) ปกติเรียบ เม็ดเลือดแดงไหลผ่านได้"},
    {"t": "ลิ่มเกล็ดเลือดเกาะผนัง",
     "cap": "**TTP**: ขาดเอนไซม์ ADAMTS13 → vWF multimer ยาวจับเกล็ดเลือด · **HUS**: Shiga toxin ทำลาย endothelium · **aHUS**: complement · **scleroderma/malignant HT**: ผนังหนา (onion skin)"},
    {"t": "เม็ดเลือดแดงถูกเฉือน",
     "cap": "RBC ไหลผ่านเส้นใยไฟบรินและลิ่ม → แตกเป็นชิ้น **schistocyte** = microangiopathic hemolytic anemia"},
    {"t": "MAHA + เกล็ดเลือดต่ำ",
     "cap": "Hb ลด · LDH สูง · haptoglobin ต่ำ · indirect bilirubin สูง · Coombs ลบ · เกล็ดเลือดต่ำเพราะถูกใช้ในลิ่ม — **การให้เกล็ดเลือดอาจเติมเชื้อเพลิงให้ลิ่ม**"},
    {"t": "อวัยวะขาดเลือด: ไต + สมอง",
     "cap": "✍️ อาจารย์: TMA พบบ่อยสุดในกลุ่ม vascular · TTP เด่น **อาการทางสมอง** · หญิงอายุน้อย + MAHA → คิด TTP แล้วหาสาเหตุรอง (SLE) และ **รีบทำ plasma exchange**"},
]


# ───────────────────────── 6 · RBC cast: เลือดออกจาก glomerulus
def a_rbccast():
    p = [t(220, 20, "GBM ที่อักเสบ → RBC หลุดเข้าท่อไต", "sm b mid"),
         circ(100, 110, 60, "bad"), t(100, 64, "glomerulus", "xs mid mu"),
         path("M160 110 L420 110", "lwa w5"), path("M160 150 L420 150", "lwa w5"),
         t(290, 174, "tubule", "xs mid mu")]
    p.append(S(2, path("M140 80 l14 6 l-6 10 z", "ms"), t(100, 186, "ผนังฉีก/crescent", "xs b mid tms"),
               mover(6, "badf", "3s", "M120 100 L160 128 L300 130")))
    p.append(S(3, circ(220, 130, 7, "lbad w2"), circ(244, 128, 7, "lbad w2 da"),
               t(232, 100, "dysmorphic RBC (acanthocyte)", "xs b mid tbad")))
    p.append(S(4, rect(300, 116, 112, 28, "ms", 12), circ(320, 130, 6, "badf"), circ(340, 130, 6, "badf"), circ(360, 130, 6, "badf"), circ(380, 130, 6, "badf"),
               t(356, 196, "Tamm–Horsfall หุ้ม = RBC cast", "xs b mid")))
    p.append(S(5, note(214, "RBC cast = เลือดมาจาก glomerulus แน่นอน", "→ GN / RPGN · ส่ง serology + เจาะไตเร็ว")))
    return SVG(440, 262, "ภาพเคลื่อนไหว: เม็ดเลือดแดงหลุดผ่าน glomerular basement membrane ที่อักเสบ รูปร่างผิดปกติ แล้วถูก Tamm-Horsfall protein หุ้มเป็น RBC cast ในท่อไต", *p)


RBCC_STEPS = [
    {"t": "glomerulus กับ tubule ที่ต่อกัน",
     "cap": "ปกติ GBM กั้นเม็ดเลือดแดงไม่ให้ผ่าน"},
    {"t": "GBM อักเสบ ฉีก → RBC หลุด",
     "cap": "ใน GN/RPGN (anti-GBM, immune complex, ANCA) ผนังหลอดเลือดฝอยแตก เกิด crescent (ภาพ RPGN ในหัวข้อนี้)"},
    {"t": "RBC บิดเบี้ยว = dysmorphic",
     "cap": "RBC เบียดผ่านรูเล็ก ๆ และเจอ osmotic stress ตลอดท่อไต → รูปร่างผิด (acanthocyte) ต่างจากเลือดออกที่ทางเดินปัสสาวะซึ่ง RBC รูปร่างปกติ"},
    {"t": "Tamm–Horsfall หุ้ม = RBC cast",
     "cap": "โปรตีน Tamm–Horsfall (uromodulin) จาก thick ascending limb เป็นแม่พิมพ์ของ cast ทุกชนิด · RBC ที่ติดอยู่ในแม่พิมพ์ = **RBC cast**"},
    {"t": "สรุป",
     "cap": "**RBC cast จำเพาะต่อ GN** · malignant HT มี dysmorphic RBC ได้แต่ไม่มี RBC cast (สไลด์ p14) · AKI + RBC cast = **RPGN จนกว่าจะพิสูจน์ได้ว่าไม่ใช่**"},
]


# ───────────────────────── 7 · AIN: ยา → ภูมิแพ้ใน interstitium
def a_ain():
    p = [t(220, 20, "Acute interstitial nephritis — ปฏิกิริยาภูมิไวเกินต่อยา", "sm b mid"),
         rect(30, 50, 380, 40, "wa", 20), t(220, 75, "tubule", "xs mid mu"),
         rect(30, 160, 380, 40, "wa", 20), t(220, 185, "tubule", "xs mid mu"),
         t(220, 128, "interstitium", "xs mid mu")]
    p.append(S(2, circ(70, 125, 8, "ms"), t(70, 129, "D", "xs b mid"), t(70, 150, "ยา = hapten", "xs mid tms"),
               t(130, 126, "→ จับโปรตีนท่อไต", "xs")))
    p.append(S(3, *[circ(180 + 26 * i, 120 + (8 if i % 2 else -6), 9, "ac") for i in range(6)],
               t(260, 150, "T cell · eosinophil แทรก", "xs b mid tac")))
    p.append(S(4, G("pl", rect(30, 92, 380, 66, "lms w2 da", 6)), t(400, 108, "บวม", "xs b end tms"),
               mover(5, "acf", "2.6s", "M250 96 L250 70 L400 70")))
    p.append(S(5, rect(14, 210, 412, 64, "bad", 8),
               t(220, 228, "ปัสสาวะ: WBC, WBC cast, eosinophiluria", "xs b mid"),
               t(220, 245, "ไม่มี RBC cast · protein subnephrotic (NSAID → nephrotic ได้)", "xs mid"),
               t(220, 262, "ร่างกาย: ไข้ ผื่น eosinophilia (ครบ 3 ข้อ < 10–15%)", "xs mid")))
    p.append(S(6, note(282, "รักษา: หยุดยาที่สงสัย (สำคัญที่สุด)", "± steroid ถ้าไม่ดีขึ้นใน 3–7 วัน (อิงตำรา)")))
    return SVG(440, 330, "ภาพเคลื่อนไหว: ยาทำหน้าที่เป็น hapten กระตุ้นเม็ดเลือดขาวเข้าแทรกใน interstitium ทำให้บวมและเม็ดเลือดขาวหลุดลงท่อไตเป็น WBC cast", *p)


AIN_STEPS = [
    {"t": "Tubule สองท่อ และ interstitium ระหว่างกลาง",
     "cap": "AIN คือการอักเสบของ **เนื้อเยื่อรอบท่อไต** ไม่ใช่ glomerulus"},
    {"t": "ยาเป็น hapten",
     "cap": "ยา (✍️ penicillin/β-lactam, sulfonamide, rifampicin, cimetidine — สไลด์ p22) จับกับโปรตีนของท่อไต กลายเป็นแอนติเจนใหม่ · มักเกิด 7–10 วันหลังเริ่มยา (เร็วกว่านั้นถ้าเคยได้)"},
    {"t": "T cell และ eosinophil แทรกเข้ามา",
     "cap": "ภาพ histology ในหัวข้อนี้: interstitial infiltrate + eosinophil (✍️ \"eosinophil → จากยา\") · ติดเชื้อ (leptospirosis, hantavirus) ก็ทำได้"},
    {"t": "Interstitium บวม · WBC ลงท่อ",
     "cap": "เนื้อไตบวม ท่อไตถูกกดและอักเสบ (tubulitis) → GFR ลด · WBC หลุดเข้าท่อ → **sterile pyuria + WBC cast**"},
    {"t": "สิ่งที่ตรวจพบ",
     "cap": "สไลด์ p25: WBC, **WBC cast** · RBC ได้แต่ไม่เด่น · **ไม่มี RBC cast** · penicillin: Hansel stain บวก · NSAID: proteinuria แบบ nephrotic ได้ · eosinophiluria > 5% ชวนคิด AIN จากยา (p27)"},
    {"t": "รักษา",
     "cap": "**หยุดยาที่สงสัยทันที** · steroid เมื่อไม่ดีขึ้นหลังหยุดยาหรือเป็นรุนแรง (อิงตำรา ไม่อยู่ในสไลด์)"},
]


# ───────────────────────── 8 · ATN: เซลล์ตาย → cast อุด + รั่วกลับ + TGF
def a_atn():
    p = [t(220, 20, "Acute tubular necrosis — ทำไม GFR ตกทั้งที่ความดันกลับมาแล้ว", "sm b mid"),
         circ(60, 110, 34, "bad"), t(60, 114, "glom", "xs b mid"),
         path("M94 96 L420 96", "lwa w3"), path("M94 136 L420 136", "lwa w3"),
         *[rect(110 + 34 * i, 84, 28, 12, "ok", 2) for i in range(9)],
         *[rect(110 + 34 * i, 136, 28, 12, "ok", 2) for i in range(9)],
         mover(5, "waf", "3s", "M96 116 L416 116")]
    p.append(S(2, X(3, rect(212, 84, 28, 12, "ms", 2), rect(246, 136, 28, 12, "ms", 2)),
               t(260, 72, "ขาดเลือด/สารพิษ → เซลล์บาดเจ็บ", "xs b mid tms")))
    p.append(S(3, rect(212, 98, 26, 12, "bad", 3), rect(250, 122, 22, 12, "bad", 3),
               t(260, 168, "เซลล์หลุดลอก (เห็น RTE cell)", "xs b mid tbad")))
    p.append(S(4, rect(290, 100, 70, 34, "ms", 10), t(325, 121, "cast", "xs b mid"),
               t(325, 186, "cast อุดท่อ → แรงดันย้อน", "xs b mid tms")))
    p.append(S(5, ar(230, 136, 230, 176, "lwa w2", "ah-wa"), ar(200, 96, 200, 62, "lwa w2", "ah-wa"),
               t(150, 200, "น้ำกรองรั่วกลับ (backleak)", "xs b mid twa")))
    p.append(S(6, G("pl", rect(20, 100, 46, 18, "ms", 4)), t(120, 230, "Na ถึง macula densa มาก → TGF หด afferent", "xs b mid")))
    p.append(S(6, rect(14, 244, 412, 50, "bad", 8),
               t(220, 263, "GFR ตก 3 ทาง: อุด · รั่วกลับ · afferent หด", "sm b mid"),
               t(220, 282, "ปัสสาวะ: FENa > 2% · Uosm ~300 · muddy brown granular cast", "xs mid")))
    return SVG(440, 302, "ภาพเคลื่อนไหว: เซลล์ท่อไตบาดเจ็บหลุดลอกเป็น cast อุดท่อ น้ำกรองรั่วกลับ และ tubuloglomerular feedback ทำให้หลอดเลือดขาเข้าหด GFR จึงตก", *p)


ATN_STEPS = [
    {"t": "ท่อไตปกติ — น้ำกรองไหลผ่าน",
     "cap": "เซลล์ proximal tubule และ thick ascending limb ใช้ออกซิเจนมาก จึงเสียหายง่ายที่สุดเมื่อขาดเลือด"},
    {"t": "ขาดเลือดนาน/สารพิษ",
     "cap": "สไลด์ p28: **renal ischemia (prolonged pre-renal) · nephrotoxins (aminoglycoside ✍️ gentamicin, radiocontrast, ✍️ acyclovir) · pigment (myoglobin, hemoglobin)**"},
    {"t": "เซลล์หลุดลอก",
     "cap": "เซลล์เสีย polarity (Na-K ATPase ย้ายที่) และหลุดจาก basement membrane ลงในท่อ → ดูด Na กลับไม่ได้ (**FENa สูง**) และทำปัสสาวะเข้มข้นไม่ได้"},
    {"t": "Cast อุดท่อ",
     "cap": "เซลล์ที่หลุด + Tamm–Horsfall = **granular (muddy brown) cast** · อุดท่อ → แรงดันในท่อสูง ต้านการกรอง"},
    {"t": "Backleak",
     "cap": "ผนังท่อที่ไม่มีเซลล์ปกคลุม ทำให้น้ำกรองรั่วกลับเข้าเลือด → GFR \"ที่ได้ผลจริง\" ต่ำลงอีก"},
    {"t": "TGF + สรุป",
     "cap": "Na ที่ไม่ถูกดูดกลับไปถึง macula densa มาก → **tubuloglomerular feedback** หด afferent · จึงเป็นเหตุผลว่าแก้ความดันแล้ว GFR ยังไม่กลับทันที ต้องรอเซลล์ใหม่ (1–3 สัปดาห์)"},
]


# ───────────────────────── 9 · Contrast-associated AKI
def a_contrast():
    p = [t(220, 20, "Contrast-associated AKI", "sm b mid"),
         rect(20, 40, 120, 40, "wa", 10), t(80, 65, "iodinated contrast", "xs b mid"),
         ell(310, 110, 92, 66, "ac"), t(310, 82, "ไต", "sm b mid"),
         ell(310, 126, 56, 30, "sk"), t(310, 130, "medulla", "xs mid")]
    p.append(S(2, path("M140 60 L218 92", "lwa w3 fl", "ah-wa"), t(170, 106, "หลอดเลือดหด", "xs b mid tbad"),
               G("pl", ell(310, 126, 56, 30, "lbad w2")), t(310, 172, "medulla ขาด O2", "xs b mid tbad")))
    p.append(S(3, rect(230, 196, 160, 30, "bad", 8), t(310, 215, "พิษตรงต่อเซลล์ PT", "xs b mid")))
    p.append(S(4, rect(14, 236, 200, 66, "ms", 8), t(114, 254, "เสี่ยงเมื่อ", "sm b mid"),
               t(114, 272, "eGFR < 30 (IV) · AKI อยู่แล้ว", "xs mid"), t(114, 288, "ขาดน้ำ · ยา nephrotoxic", "xs mid"),
               rect(226, 236, 200, 66, "ok", 8), t(326, 254, "ป้องกัน", "sm b mid"),
               t(326, 272, "IV isotonic fluid ก่อน–หลัง", "xs mid"), t(326, 288, "contrast น้อยที่สุด · หยุด NSAID", "xs mid")))
    p.append(S(5, note(310, "NAC · NaHCO3 · prophylactic HD: ไม่แนะนำ", "metformin: งดเมื่อ eGFR < 30 หรือมี AKI (ACR)")))
    return SVG(440, 360, "ภาพเคลื่อนไหว: สารทึบรังสีทำให้หลอดเลือดในไตหด medulla ขาดออกซิเจน และเป็นพิษตรงต่อท่อไต ความเสี่ยงและวิธีป้องกัน", *p)


CONTRAST_STEPS = [
    {"t": "สารทึบรังสีชนิด iodinated เข้าสู่ไต",
     "cap": "สไลด์ p28 จัด radiocontrast เป็น nephrotoxin ของ ATN · p50: contrast-induced nephropathy เป็น ATN ที่ **FENa อาจต่ำ** (มีส่วนของหลอดเลือดหด)"},
    {"t": "หลอดเลือดหด → medulla ขาด O2",
     "cap": "contrast เพิ่ม endothelin/adenosine ลด NO → หลอดเลือดในไตหด · outer medulla มี O2 น้อยอยู่แล้วจึงขาดเลือดง่าย"},
    {"t": "พิษตรงต่อเซลล์ท่อไต",
     "cap": "ทำให้เซลล์ proximal tubule บวมเป็นถุงน้ำและตาย · Cr มักขึ้นใน 24–72 ชม. หลังฉีด กลับคืนใน 1–2 สัปดาห์ส่วนใหญ่"},
    {"t": "ใครเสี่ยง · ป้องกันอย่างไร",
     "cap": "ACR–NKF 2020: เสี่ยงจริงเมื่อ **eGFR < 30** หรือมี AKI → ให้ **isotonic fluid ทาง IV** ก่อน–หลัง ใช้ contrast ขนาดน้อยที่สุด เลี่ยงยาที่ทำร้ายไต (ไม่อยู่ในสไลด์)"},
    {"t": "สิ่งที่ไม่ได้ผล",
     "cap": "N-acetylcysteine และ sodium bicarbonate ไม่ดีกว่าน้ำเกลือ (PRESERVE trial) · ฟอกเลือดป้องกันไม่ช่วย · การไม่ทำ CT ที่จำเป็นเพราะกลัวไตอาจอันตรายกว่า"},
]


# ───────────────────────── 10 · Rhabdomyolysis: heme toxicity
def a_rhabdo():
    p = [t(220, 20, "Rhabdomyolysis → pigment ATN", "sm b mid"),
         rect(14, 40, 140, 70, "bad", 10), t(84, 62, "กล้ามเนื้อสลาย", "sm b mid"),
         t(84, 80, "statin+fibrate · crush", "xs mid"), t(84, 96, "✍️ amphetamine · ชัก", "xs mid")]
    p.append(S(2, rect(14, 122, 140, 120, "sk", 8),
               t(84, 140, "ปล่อยออกมา", "xs b mid"), t(84, 158, "myoglobin", "xs b mid tbad"), t(84, 174, "K+ · PO4 · urate", "xs mid"),
               t(84, 190, "CK สูงมาก", "xs b mid"), t(84, 206, "Ca ไปเกาะกล้ามเนื้อ", "xs mid"), t(84, 222, "→ Ca ต่ำ", "xs mid"),
               mover(5, "badf", "2.5s", "M154 75 L250 75")))
    p.append(S(3, ell(320, 90, 92, 56, "ac"), t(320, 70, "ไต", "sm b mid"),
               t(320, 92, "① heme ดูด NO →", "xs mid"), t(320, 108, "หลอดเลือดหด", "xs mid")))
    p.append(S(4, rect(232, 156, 194, 40, "bad", 8), t(329, 172, "② iron → oxidative injury", "xs b mid"), t(329, 188, "เซลล์ PT ตาย", "xs mid")))
    p.append(S(5, rect(232, 204, 194, 40, "ms", 8), t(329, 220, "③ myoglobin + THP → cast", "xs b mid"), t(329, 236, "ในปัสสาวะกรด/น้อย", "xs mid")))
    p.append(S(6, note(254, "Dipstick blood 3+ แต่ RBC 0–2/HPF", "→ ส่ง CK · ให้ isotonic fluid เร็วและมาก (UO 200–300 mL/ชม.)", "ok")))
    return SVG(440, 302, "ภาพเคลื่อนไหว: กล้ามเนื้อสลายปล่อย myoglobin โพแทสเซียม ฟอสเฟต ทำให้ไตเสียสามทาง หลอดเลือดหด พิษจากเหล็ก และ cast อุดท่อ", *p)


RHABDO_STEPS = [
    {"t": "กล้ามเนื้อลายสลาย",
     "cap": "สาเหตุ: บาดเจ็บ/ถูกทับ ออกกำลังหนัก ชัก ยา (**statin + gemfibrozil**) ✍️ **amphetamine** (BP สูงมาก 220 → สงสัยไว้ก่อน) แอลกอฮอล์ ไข้สูง K/PO4 ต่ำ"},
    {"t": "ของในเซลล์ทะลักออกมา",
     "cap": "**myoglobin · K · PO4 · urate · CK · AST** (AST > ALT) · Ca ไปจับกับเนื้อที่ตาย → **Ca ต่ำช่วงแรก** แล้วสูงช่วงฟื้น"},
    {"t": "① heme จับ NO → หลอดเลือดไตหด",
     "cap": "ร่วมกับน้ำไปอยู่ในกล้ามเนื้อที่บวม (third space) → ไตขาดเลือด จึงมี FENa ต่ำได้ (สไลด์ p50)"},
    {"t": "② เหล็กใน heme ทำลายเซลล์ท่อไต",
     "cap": "iron กระตุ้น oxidative stress/lipid peroxidation ใน proximal tubule (ภาพ myoglobin deposit ในหัวข้อนี้)"},
    {"t": "③ cast อุดท่อ",
     "cap": "myoglobin จับ Tamm–Horsfall ตกตะกอนง่ายเมื่อ **ปัสสาวะกรดและน้อย** → อุดท่อ"},
    {"t": "จับได้จาก UA · รักษาด้วยน้ำ",
     "cap": "สไลด์ p32: **disproportion — blood 3+ แต่ RBC 2–3/HPF** · ยืนยันด้วย **CK** · รักษา: หยุดสาเหตุ ให้ isotonic fluid เร็ว แก้ K · dialysis ถ้า K/กรด/น้ำเกินดื้อยา (เป้าปัสสาวะอิงตำรา)"},
]


# ───────────────────────── 11 · Crystal: ตกผลึกในท่อไต
def a_crystal():
    p = [t(220, 20, "Intrarenal obstruction — ผลึกตกในท่อไต", "sm b mid"),
         path("M20 80 L420 80", "lwa w5"), path("M20 150 L420 150", "lwa w5"),
         mover(5, "waf", "3s", "M24 115 L416 115"), mover(4, "msf", "3.4s", "M24 104 L416 104", "0.6s")]
    p.append(S(2, rect(20, 160, 190, 56, "wa", 8), t(115, 180, "น้ำน้อย = เข้มข้น", "xs b mid"), t(115, 198, "ยา/สารเกินจุดอิ่มตัว", "xs mid")))
    p.append(S(3, rect(226, 160, 194, 56, "ms", 8), t(323, 178, "pH ปัสสาวะ", "xs b mid"),
               t(323, 194, "กรด: uric · MTX", "xs mid"), t(323, 208, "ด่าง: cipro · indinavir · CaP", "xs mid")))
    p.append(S(4, *[path("M%d %d l10 -14 l4 16 z" % (250 + 18 * i, 128 - (i % 2) * 18), "ms") for i in range(8)],
               t(320, 66, "ผลึกรวมตัว อุดท่อ", "xs b mid tms")))
    p.append(S(5, rect(14, 226, 412, 70, "ac", 8),
               t(220, 244, "Uric (TLS) · Oxalate (✍️ ethylene glycol มะเฟือง ตะลิงปลิง Vit C)", "xs b mid"),
               t(220, 262, "MTX · acyclovir · sulfonamide · triamterene · ✍️ ciprofloxacin", "xs mid"),
               t(220, 282, "ป้องกัน: ให้น้ำ · ปรับขนาดยา · (ปรับ pH ตามชนิด)", "xs b mid")))
    return SVG(440, 304, "ภาพเคลื่อนไหว: เมื่อปัสสาวะน้อยและเข้มข้น หรือ pH เหมาะ ยาและสารตกผลึกรวมตัวอุดท่อไต", *p)


CRYSTAL_STEPS = [
    {"t": "สารละลายไหลผ่านท่อไต",
     "cap": "ยาหรือสารที่ขับทางไตจะเข้มข้นขึ้นเรื่อย ๆ เมื่อน้ำถูกดูดกลับตามทาง"},
    {"t": "ปัจจัยที่ 1: ปัสสาวะน้อย/เข้มข้น",
     "cap": "ขาดน้ำ ยาขนาดสูง ฉีดเร็ว (เช่น acyclovir IV bolus) → ความเข้มข้นเกินจุดอิ่มตัว"},
    {"t": "ปัจจัยที่ 2: pH ปัสสาวะ",
     "cap": "**uric acid และ methotrexate ตกในปัสสาวะกรด** · **ciprofloxacin, indinavir, calcium phosphate ตกในปัสสาวะด่าง**"},
    {"t": "ผลึกรวมตัว อุดท่อ",
     "cap": "อุดท่อไตจากด้านใน + อักเสบรอบ ๆ → อาจารย์จัดเป็น **intrarenal obstruction (post-renal AKI)** · UA: bland + เห็นผลึก (ภาพในหัวข้อนี้)"},
    {"t": "สาเหตุที่ต้องรู้ + ป้องกัน",
     "cap": "สไลด์ p35: uric, oxalate, methotrexate, acyclovir, triamterene, sulfonamides · ✍️ oxalate จาก **ethylene glycol** มะเฟือง ตะลิงปลิง Vit C มาก · ป้องกันด้วยน้ำและปรับขนาดยาตาม GFR"},
]


# ───────────────────────── 12 · Post-renal: แรงดันย้อนกลับ
def a_post():
    p = [t(220, 20, "Post-renal — แรงดันย้อนจากทางออกที่อุด", "sm b mid"),
         ell(110, 90, 40, 52, "ac"), ell(330, 90, 40, 52, "ac"),
         t(110, 94, "ไต", "xs b mid"), t(330, 94, "ไต", "xs b mid"),
         path("M110 142 C120 190 190 210 206 226", "lwa w3"), path("M330 142 C320 190 250 210 234 226", "lwa w3"),
         ell(220, 250, 46, 30, "wa"), t(220, 254, "กระเพาะ", "xs b mid"),
         path("M220 280 L220 306", "lwa w3"), t(234, 302, "urethra", "xs mu")]
    p.append(S(2, G("pl", rect(206, 286, 28, 14, "bad", 4)), t(290, 296, "BPH/stricture อุด", "xs b tbad")))
    p.append(S(3, ell(220, 250, 62, 40, "lwa w3 da"), t(320, 248, "กระเพาะโป่ง", "xs b twa")))
    p.append(S(4, path("M110 142 C120 190 190 210 206 226", "lwa w5"), path("M330 142 C320 190 250 210 234 226", "lwa w5"),
               ell(110, 90, 22, 30, "waf"), ell(330, 90, 22, 30, "waf"), t(220, 70, "hydronephrosis", "xs b mid twa"),
               t(220, 86, "ทั้งสองข้าง", "xs mid twa")))
    p.append(S(5, rect(10, 316, 420, 44, "bad", 8), t(220, 334, "แรงดันใน Bowman's space ↑ → แรงดันกรองสุทธิ ↓", "xs b mid"),
               t(220, 350, "+ หลอดเลือดไตหด (AngII, TXA2) → GFR ↓", "xs mid")))
    p.append(S(6, rect(10, 366, 420, 44, "ok", 8), t(220, 384, "ระบาย: Foley / suprapubic / nephrostomy", "xs b mid"),
               t(220, 400, "ระวัง post-obstructive diuresis (ดูคาบ 22/10)", "xs mid")))
    return SVG(440, 418, "ภาพเคลื่อนไหว: ทางออกปัสสาวะอุด กระเพาะโป่ง แรงดันย้อนขึ้นท่อไตทั้งสองข้างเกิด hydronephrosis แรงดันใน Bowman's space สูงทำให้ GFR ลด", *p)


POST_STEPS = [
    {"t": "ทางเดินปัสสาวะปกติ",
     "cap": "ปัสสาวะไหลจากไตทั้งสองข้าง ผ่านท่อไต กระเพาะ และท่อปัสสาวะ"},
    {"t": "ทางออกอุด",
     "cap": "สไลด์ p41: bladder (stone, tumor, **neurogenic**, **BPH**, malignancy) · urethral stricture (✍️ จากฉีด paraffin/ฝังมุก) · ระดับท่อไต: นิ่ว ลิ่มเลือด ก้อน มะเร็งกดเบียด fibrosis ผูกท่อไตระหว่างผ่าตัด"},
    {"t": "กระเพาะโป่งตึง",
     "cap": "คลำ/เคาะทึบเหนือหัวหน่าว · bladder scan · ปัสสาวะไม่ออกหรือล้นเป็นหยด (overflow)"},
    {"t": "แรงดันย้อนขึ้นถึงไตสองข้าง",
     "cap": "ท่อไตและกรวยไตโป่ง = **hydronephrosis** บน ultrasound · AKI เกิดเมื่ออุด **ทั้งสองข้าง** หรือไตทำงานข้างเดียว"},
    {"t": "ทำไม GFR ตก",
     "cap": "แรงดันใน tubule/Bowman's space สูง ต้านแรงดันกรอง · ระยะแรกไตยังดูด Na ได้ (FENa ต่ำ) · อุดนานท่อไตเสีย FENa สูง (สไลด์ p50–51)"},
    {"t": "ระบายแล้วต้องเฝ้าดู",
     "cap": "ระบายเร็วไตมักกลับคืน · ระวัง **post-obstructive diuresis** เสียน้ำ Na K Mg มาก (รายละเอียดในคาบ 22/10 catheter)"},
]


# ───────────────────────── 13 · Urine indices: pre-renal vs ATN
def a_indices():
    p = [t(220, 20, "ท่อไตยังดี vs ท่อไตเสีย", "sm b mid"),
         t(112, 44, "Pre-renal", "sm b mid tok"), t(328, 44, "ATN", "sm b mid tbad"),
         line(220, 34, 220, 300, "lmu da"),
         path("M30 70 L194 70 L194 110 L30 110", "lwa w3"), path("M246 70 L410 70 L410 110 L246 110", "lwa w3")]
    p.append(S(2, *[rect(40 + 30 * i, 58, 22, 12, "ok", 2) for i in range(5)],
               *[rect(256 + 30 * i, 58, 22, 12, "bad" if i % 2 else "ms", 2) for i in range(5)],
               t(112, 132, "เซลล์ทำงานครบ", "xs mid"), t(328, 132, "เซลล์ตาย/หลุด", "xs mid")))
    p.append(S(3, ar(112, 92, 112, 154, "lok w3", "ah-ok"), t(112, 168, "RAAS ดูด Na คืน", "xs b mid tok"),
               t(112, 184, "U Na < 20 · FENa < 1%", "xs b mid"),
               ar(328, 92, 380, 92, "lbad w3", "ah-bad"), t(328, 168, "Na หลุดออกไป", "xs b mid tbad"),
               t(328, 184, "U Na > 30 · FENa > 1–2%", "xs b mid")))
    p.append(S(4, t(112, 206, "ADH → Uosm > 400", "xs b mid"), t(112, 222, "SpGr > 1.020", "xs mid"),
               t(328, 206, "เข้มข้นไม่ได้ Uosm ~300", "xs b mid"), t(328, 222, "SpGr ~1.010–1.015", "xs mid")))
    p.append(S(5, t(112, 244, "urea ถูกดูดคืนตามน้ำ", "xs mid"), t(112, 260, "BUN/Cr > 20", "xs b mid"),
               t(328, 244, "U/P Cr < 20", "xs mid"), t(328, 260, "BUN/Cr ~10", "xs b mid")))
    p.append(S(6, note(276, "ดัชนีเชื่อได้เมื่อ \"ไม่ได้ diuretic\" และปัสสาวะน้อย", "ได้ diuretic → ใช้ FEurea (< 35% pre-renal)")))
    return SVG(440, 324, "ภาพเคลื่อนไหว: เปรียบเทียบดัชนีปัสสาวะใน pre-renal ที่ท่อไตยังดีดูด Na และน้ำคืน กับ ATN ที่ท่อไตเสีย", *p)


IND_STEPS = [
    {"t": "สองสถานการณ์ที่ GFR ตกเหมือนกัน",
     "cap": "ทั้ง pre-renal และ ATN มี Cr สูงและปัสสาวะน้อยได้ — ต่างกันที่ **เซลล์ท่อไตยังทำงานหรือไม่**"},
    {"t": "เซลล์ท่อไต: ครบ vs ตาย",
     "cap": "pre-renal เนื้อไตปกติ · ATN เซลล์ proximal tubule และ thick ascending limb หลุดลอก"},
    {"t": "Na: เก็บ vs รั่ว",
     "cap": "pre-renal: aldosterone/angiotensin II สั่งดูด Na คืนเต็มที่ → **U Na < 20, FENa < 1%** · ATN: ดูดไม่ได้ → **U Na > 30, FENa > 1%** (สไลด์ p48)"},
    {"t": "ความเข้มข้น: ทำได้ vs ทำไม่ได้",
     "cap": "pre-renal: ADH สูง → **Uosm > 400, SpGr > 1.024, U/P osm > 1.5** · ATN: medulla gradient และท่อเสีย → ปัสสาวะใกล้ plasma (**Uosm ~300, U/P osm ~1**)"},
    {"t": "Urea: ดูดคืน vs ไม่ดูดคืน",
     "cap": "น้ำไหลช้าใน pre-renal → urea ถูกดูดกลับตามน้ำ (+ ADH ที่ collecting duct) → **BUN/Cr > 20** · creatinine ไม่ถูกดูดกลับ → **U/P Cr > 40 vs < 20**"},
    {"t": "ข้อควรระวัง",
     "cap": "diuretic ทำให้ FENa สูงหลอก → ใช้ **FEurea** · ATN บางแบบ FENa ต่ำ (contrast, pigment, sepsis, burn) · pre-renal บางแบบ FENa สูง (**DMARD**) · ใช้ร่วมกับ UA และการตอบสนองต่อน้ำเสมอ"},
]


# ───────────────────────── 14 · Hyperkalemia: membrane → ECG
def a_hyperk():
    p = [t(220, 20, "K นอกเซลล์สูง → ไฟฟ้าหัวใจผิด", "sm b mid"),
         line(30, 60, 30, 170, "ln"), t(36, 64, "0 mV", "xs mu"), t(36, 168, "−90", "xs mu"),
         line(30, 150, 200, 150, "lok w3"), t(120, 144, "RMP ปกติ −90", "xs b mid tok"),
         line(30, 110, 200, 110, "lms da"), t(120, 104, "threshold", "xs mid tms")]
    p.append(S(2, line(30, 126, 200, 126, "lbad w3"), t(120, 140, "RMP ยกขึ้น (−75)", "xs b mid tbad")))
    # ECG traces x 230..430
    p.append(S(3, path("M230 100 L262 100 L266 96 L270 100 L282 100 L286 70 L290 110 L294 100 L306 100 L318 52 L330 100 L350 100", "lbad w2"),
               t(330, 50, "T สูงแหลม", "xs b tbad")))
    p.append(S(4, path("M230 170 L262 170 L282 170 L290 140 L304 186 L312 170 L326 132 L342 170 L360 170", "lbad w2"),
               t(330, 128, "P หาย · PR ยาว · QRS กว้าง", "xs b mid tbad"),
               t(120, 196, "Na channel inactivate", "xs b mid"), t(120, 212, "→ นำไฟฟ้าช้า", "xs mid")))
    p.append(S(5, path("M230 240 C250 200 270 200 290 240 C310 280 330 280 350 240 C370 200 390 200 410 240", "lbad w3"),
               t(320, 272, "sine wave → VF/asystole", "xs b mid tbad")))
    p.append(S(6, line(30, 96, 200, 96, "lac w3"), t(120, 90, "Ca ยก threshold", "xs b mid tac"),
               rect(10, 282, 420, 44, "ok", 8), t(220, 300, "Ca gluconate ทำให้ระยะ threshold–RMP กลับมา", "xs b mid"),
               t(220, 316, "แต่ไม่ลด K → ต้อง shift + remove ต่อ", "xs mid")))
    return SVG(440, 334, "ภาพเคลื่อนไหว: โพแทสเซียมนอกเซลล์สูงทำให้ resting membrane potential สูงขึ้น ECG เปลี่ยนจาก T สูงแหลม เป็น P หาย QRS กว้าง จนเป็น sine wave แคลเซียมยก threshold ปกป้องหัวใจ", *p)


HYPERK_STEPS = [
    {"t": "ปกติ: RMP −90 mV ห่างจาก threshold",
     "cap": "resting membrane potential ถูกกำหนดโดยสัดส่วน K ในเซลล์/นอกเซลล์ · ไตเป็นทางขับ K หลัก AKI จึงทำให้ K คั่ง (ร่วมกับกรดที่ดัน K ออกจากเซลล์ และเซลล์ที่ตาย)"},
    {"t": "K นอกเซลล์สูง → RMP ยกขึ้น",
     "cap": "สัดส่วน K ใน/นอกลดลง → เซลล์ \"ไม่ติดลบมากเท่าเดิม\" (depolarize บางส่วน)"},
    {"t": "Repolarize เร็ว → T สูงแหลม",
     "cap": "K สูงเพิ่ม conductance ของ K channel → phase 3 เร็วและชัน = **peaked T** (สไลด์ p60) · ✍️ ดู K จาก blood gas ได้เลยเพราะได้ผลเร็ว"},
    {"t": "Na channel ปิดค้าง → นำไฟฟ้าช้า",
     "cap": "RMP ที่สูงนานทำให้ Na channel inactivate → upstroke ช้า → **P แบน/หาย · PR ยาว · QRS กว้าง · bradycardia** (สไลด์ p60)"},
    {"t": "Sine wave",
     "cap": "QRS กว้างจนรวมกับ T = **sine wave** (สไลด์ p61) → VF หรือ asystole ได้ทุกเมื่อ · ECG สัมพันธ์กับระดับ K ไม่ดี — ECG ผิด = รักษาด่วนไม่ว่า K เท่าไร"},
    {"t": "Calcium ปกป้องหัวใจ",
     "cap": "Ca ยก threshold potential → ระยะห่างจาก RMP กลับมา เซลล์ไม่ไวเกิน · **ไม่ได้ลด K** จึงต้องตามด้วย insulin/glucose, β-agonist และเอา K ออก (binder, diuretic, dialysis)"},
]


# ───────────────────────── 15 · AEIOU
def a_aeiou():
    rows = [("A", "Acidosis", "metabolic acidosis รุนแรงที่ดื้อต่อ NaHCO3", "bad"),
            ("E", "Electrolyte", "K สูงที่ไม่ตอบสนองต่อยาเต็มที่", "bad"),
            ("I", "Intoxication", "สารพิษที่ dialyze ได้: methanol, ethylene glycol, lithium, salicylate", "ms"),
            ("O", "Overload", "น้ำเกิน/น้ำท่วมปอดที่ไม่ตอบสนองต่อ diuretic", "bad"),
            ("U", "Uremia", "pericarditis · encephalopathy · เลือดออก (= ✍️ ช้าไปแล้ว)", "ms")]
    p = [t(220, 22, "ข้อบ่งชี้ dialysis เร่งด่วน — AEIOU", "sm b mid")]
    y = 36
    for i, (k, w, d, c) in enumerate(rows):
        p.append(S(i + 1, rect(10, y, 420, 50, c, 9), circ(36, y + 25, 17, "bx"), t(36, y + 31, k, "lg b mid"),
                   t(62, y + 20, w, "sm b"), t(62, y + 39, d, "xs")) if i else
                 "".join([rect(10, y, 420, 50, c, 9), circ(36, y + 25, 17, "bx"), t(36, y + 31, k, "lg b mid"),
                          t(62, y + 20, w, "sm b"), t(62, y + 39, d, "xs")]))
        y += 56
    p.append(S(6, rect(10, y + 2, 420, 44, "ok", 9), t(220, y + 20, "หัวใจของสไลด์ p72: \"ไม่ตอบสนองต่อยาเต็มที่\"", "xs b mid"),
               t(220, y + 37, "รอจนเกิด uremic encephalopathy/pericarditis = Too late", "xs mid")))
    return SVG(440, y + 54, "ภาพเคลื่อนไหว: หลักจำ AEIOU ข้อบ่งชี้การฟอกเลือดเร่งด่วน acidosis electrolyte intoxication overload uremia", *p)


AEIOU_STEPS = [
    {"t": "A — Acidosis",
     "cap": "severe metabolic acidosis ที่ไม่ตอบสนองต่อการรักษา (สไลด์ให้ NaHCO3 เพื่อรักษา HCO3 > 15 หรือ pH > 7.2 ก่อน) · ✍️ ระวังให้ NaHCO3 ถ้า CO2 ในเลือดสูงอยู่แล้ว"},
    {"t": "E — Electrolyte (K)",
     "cap": "**hyperkalemia ที่ไม่ตอบสนองต่อยาเต็มที่** — สไลด์ p71 ข้อแรก"},
    {"t": "I — Intoxication",
     "cap": "สารที่โมเลกุลเล็ก จับโปรตีนน้อย: methanol, ethylene glycol, lithium, salicylate, metformin (lactic acidosis) — ข้อนี้ไม่อยู่ในสไลด์ AKI แต่อยู่ในหลักจำ"},
    {"t": "O — Overload",
     "cap": "**volume overload ที่ไม่ตอบสนองต่อ diuretic** — อาจารย์เน้นเป็น key ข้อ 1 ของการเริ่ม RRT ใน AKI (p72)"},
    {"t": "U — Uremia",
     "cap": "uremic symptom, **uremic pericarditis**, encephalopathy, เลือดออกจากเกล็ดเลือดทำงานผิด · สไลด์ p72 กากบาทว่า **Too late** ✍️ \"End stage\" · เกณฑ์ BUN > 100/Cr > 10 (non-catabolic) หรือ BUN > 70/Cr > 7 (hypercatabolic) ใน p71"},
    {"t": "สรุป: เริ่มก่อนสายเกินไป",
     "cap": "ใน AKI เริ่ม dialysis เมื่อ **น้ำเกินหรือกรด-ด่าง/K ดื้อต่อยาเต็มที่** · ไม่จำเป็นต้องเริ่มเร็วในผู้ป่วยที่ยังคุมได้ (การศึกษา STARRT-AKI 2020 — ไม่อยู่ในสไลด์)"},
]


# ───────────────────────── 16 · 4 ขั้นของการวินิจฉัย AKI (สไลด์ p43–47)
def a_steps():
    rows = [("Step 1", "ไตวายจริงไหม?", "BUN/Cr ขึ้นจากสาเหตุนอกไต (GI bleed, steroid,\nrhabdo, trimethoprim, cimetidine)", "sk"),
            ("Step 2", "AKI หรือ CKD?", "ประวัติ Cr เดิม · ตรวจร่างกาย · ซีด Ca/PO4\nultrasound ขนาดไต", "wa"),
            ("Step 3", "ตัด post-renal", "bladder scan / Foley · ultrasound หา hydronephrosis", "ms"),
            ("Step 4", "ประเมิน intrinsic", "UA + ตะกอน · FENa/FEurea · serology/biopsy", "bad")]
    p = [t(220, 22, "Once BUN/Cr rising ± oliguria", "sm b mid")]
    y = 36
    for i, (a, b, c, k) in enumerate(rows):
        body = [rect(10, y, 420, 64, k, 9), t(22, y + 22, a, "sm b"), t(90, y + 22, b, "sm b"), t(22, y + 42, c, "xs", 1.3)]
        p.append(S(i + 1, *body) if i else "".join(body))
        if i < 3:
            p.append(S(i + 2, ar(220, y + 64, 220, y + 72, "ln w2", "ah")))
        y += 74
    p.append(S(5, rect(10, y, 420, 40, "ok", 9), t(220, y + 17, "ทุกขั้น: หา pre-renal ที่แก้ได้ (ประเมินน้ำ หยุดยา)", "xs b mid"),
               t(220, y + 33, "+ ดูภาวะแทรกซ้อนที่ต้องแก้ทันที (K น้ำเกิน กรด)", "xs mid")))
    return SVG(440, y + 48, "ภาพเคลื่อนไหว: สี่ขั้นของการวินิจฉัย AKI ตามสไลด์ ไตวายจริงไหม AKI หรือ CKD ตัด post-renal และประเมิน intrinsic", *p)


STEPS_STEPS = [
    {"t": "Step 1 — ไตวายจริงไหม",
     "cap": "สไลด์ p44–45: BUN สูงได้จาก **hypercatabolism, โปรตีนสูง, amino acid infusion, GI bleeding (✍️ เลือดในลำไส้ = โปรตีน), steroid, tetracycline** · Cr สูงได้จาก **rhabdomyolysis** และยาที่ **ยับยั้งการหลั่ง Cr: cimetidine, trimethoprim** โดย GFR ไม่เปลี่ยน"},
    {"t": "Step 2 — AKI หรือ CKD",
     "cap": "ประวัติ ตรวจร่างกาย แล็บ (p46) · ภาพ ultrasound ในหัวข้อนี้ — ไตเล็ก ขาว cortex บาง = เรื้อรัง"},
    {"t": "Step 3 — ตัด post-renal",
     "cap": "เพราะ **แก้ได้เร็วและกลับคืนได้** — คลำกระเพาะ bladder scan ใส่สาย และ ultrasound (p47)"},
    {"t": "Step 4 — ประเมิน intrinsic",
     "cap": "UA \"หน้าตาแบบใด\" · diagnostic indices (p48) · FENa (p49–51) · แล็บเฉพาะโรค (CK, smear, complement, ANCA) · เจาะไตเมื่อสงสัย GN/AIN ที่ไม่ชัด"},
    {"t": "ระหว่างทาง: ช่วยชีวิตก่อน",
     "cap": "ทุกขั้นต้องประเมิน **น้ำ (ขาด/เกิน) K และกรด** และหยุดยาที่ทำร้ายไต — ไม่ต้องรอวินิจฉัยครบ"},
]


ITEMS = [
    {"sec": "nephro-aki-02", "after": "ข้อจำกัดของ creatinine",
     "anim": {"key": "aki-crlag", "title": "Creatinine มาช้า — GFR ตกทันทีแต่ Cr ไล่ตามทีละวัน", "svg": a_crlag(), "steps": CRLAG_STEPS}},
    {"sec": "nephro-aki-03", "after": "สามตำแหน่งที่ทำให้ปัสสาวะไม่ออก",
     "anim": {"key": "aki-where", "title": "Pre-renal · intrinsic · post-renal — ปัญหาอยู่ตรงไหน", "svg": a_where(), "steps": WHERE_STEPS}},
    {"sec": "nephro-aki-04", "after": "กลไก: ไตพยุง GFR อย่างไร และยาไปทำลายตรงไหน",
     "anim": {"key": "aki-glom", "title": "Afferent/efferent — NSAID, ACEi และ triple whammy", "svg": a_glom(), "steps": GLOM_STEPS}},
    {"sec": "nephro-aki-05", "after": "Cardiorenal syndrome",
     "anim": {"key": "aki-crs", "title": "Cardiorenal — แรงดันหลอดเลือดดำย้อนเข้าไต", "svg": a_crs(), "steps": CRS_STEPS}},
    {"sec": "nephro-aki-06", "after": "Thrombotic microangiopathy (TTP/HUS)",
     "anim": {"key": "aki-tma", "title": "TMA — ลิ่มเกล็ดเลือดเฉือนเม็ดเลือดแดงและทำให้ไตขาดเลือด", "svg": a_tma(), "steps": TMA_STEPS}},
    {"sec": "nephro-aki-07", "after": "UA ใน acute GN",
     "anim": {"key": "aki-rbccast", "title": "RBC cast — หลักฐานว่าเลือดมาจาก glomerulus", "svg": a_rbccast(), "steps": RBCC_STEPS}},
    {"sec": "nephro-aki-08", "after": "กลไก AIN",
     "anim": {"key": "aki-ain", "title": "AIN — ยากระตุ้นภูมิแพ้ใน interstitium", "svg": a_ain(), "steps": AIN_STEPS}},
    {"sec": "nephro-aki-09", "after": "ทำไม GFR ตกใน ATN",
     "anim": {"key": "aki-atn", "title": "ATN — cast อุด รั่วกลับ และ TGF", "svg": a_atn(), "steps": ATN_STEPS}},
    {"sec": "nephro-aki-10", "after": "Contrast-associated AKI",
     "anim": {"key": "aki-contrast", "title": "Contrast-associated AKI — กลไกและการป้องกัน", "svg": a_contrast(), "steps": CONTRAST_STEPS}},
    {"sec": "nephro-aki-11", "after": "Rhabdomyolysis — กลไก 3 ทาง",
     "anim": {"key": "aki-rhabdo", "title": "Rhabdomyolysis — heme ทำร้ายไต 3 ทาง", "svg": a_rhabdo(), "steps": RHABDO_STEPS}},
    {"sec": "nephro-aki-12", "after": "ทำไมผลึกถึงตกในท่อไต",
     "anim": {"key": "aki-crystal", "title": "Crystal nephropathy — ผลึกอุดท่อไตจากด้านใน", "svg": a_crystal(), "steps": CRYSTAL_STEPS}},
    {"sec": "nephro-aki-13", "after": "กลไก: แรงดันย้อน",
     "anim": {"key": "aki-post", "title": "Post-renal — แรงดันย้อนจนกรองไม่ได้", "svg": a_post(), "steps": POST_STEPS}},
    {"sec": "nephro-aki-14", "after": "",
     "anim": {"key": "aki-steps", "title": "4 ขั้นของการวินิจฉัย AKI (สไลด์ p43–47)", "svg": a_steps(), "steps": STEPS_STEPS}},
    {"sec": "nephro-aki-15", "after": "Diagnostic indices (สไลด์ p48)",
     "anim": {"key": "aki-indices", "title": "ดัชนีปัสสาวะ — ท่อไตยังดี vs ท่อไตเสีย", "svg": a_indices(), "steps": IND_STEPS}},
    {"sec": "nephro-aki-16", "after": "Hyperkalemia — กลไกและ ECG",
     "anim": {"key": "aki-hyperk", "title": "Hyperkalemia — จาก membrane potential สู่ ECG", "svg": a_hyperk(), "steps": HYPERK_STEPS}},
    {"sec": "nephro-aki-17", "after": "ข้อบ่งชี้ในสไลด์",
     "anim": {"key": "aki-aeiou", "title": "AEIOU — ข้อบ่งชี้ dialysis เร่งด่วน", "svg": a_aeiou(), "steps": AEIOU_STEPS}},
]

MNEM = [
    {"sec": "nephro-aki-02", "name": "RIFLE", "what": "ระดับความรุนแรงของ AKI ตามสไลด์ (Bellomo 2004)",
     "lines": [["R", "**R**isk — Cr ×1.5 หรือ UO < 0.5 mL/kg/h × 6 ชม."],
               ["I", "**I**njury — Cr ×2 หรือ UO < 0.5 × 12 ชม."],
               ["F", "**F**ailure — Cr ×3 หรือ UO < 0.3 × 24 ชม. หรือ anuria 12 ชม."],
               ["L", "**L**oss — ไตไม่กลับมาทำงาน > 4 สัปดาห์"],
               ["E", "**E**SKD — > 3 เดือน"]],
     "note": "ปัจจุบันใช้ KDIGO 2012 (stage 1–3) ซึ่งเพิ่มเกณฑ์ Cr ขึ้น ≥ 0.3 mg/dL ใน 48 ชม. — R/I/F ≈ stage 1/2/3",
     "src": "สไลด์ อ.วรรณิยา p6 · ADQI RIFLE criteria (Bellomo R, et al. Crit Care 2004)"},
    {"sec": "nephro-aki-04", "name": "Triple whammy", "what": "ยาสามกลุ่มที่รวมกันแล้วทำ GFR ตก",
     "lines": [["1", "**ACEi / ARB** — คลาย efferent"], ["2", "**Diuretic** — ลด volume"],
               ["3", "**NSAID** — หด afferent (ไม่มี prostaglandin)"]],
     "note": "ใช้ร่วมกับ \"sick day rules\": หยุดยาเหล่านี้ชั่วคราวเมื่อท้องเสีย อาเจียน หรือกินไม่ได้",
     "src": "หลักจำทั่วไป (Thomas MC. Med J Aust 2000 — \"triple whammy\" AKI)"},
    {"sec": "nephro-aki-06", "name": "FAT RN", "what": "pentad คลาสสิกของ TTP",
     "lines": [["F", "**F**ever"], ["A", "**A**nemia — MAHA (schistocytes)"], ["T", "**T**hrombocytopenia"],
               ["R", "**R**enal dysfunction"], ["N", "**N**eurologic symptoms (✍️ เด่นใน TTP)"]],
     "note": "ครบ 5 ข้อพบน้อย (< 10%) — MAHA + เกล็ดเลือดต่ำโดยไม่มีสาเหตุอื่น เพียงพอที่จะเริ่ม plasma exchange",
     "src": "หลักจำทั่วไป (First Aid for the USMLE Step 1 — TTP pentad)"},
    {"sec": "nephro-aki-08", "name": "5 P's ของ AIN จากยา", "what": "ยาที่ทำให้เกิด acute interstitial nephritis",
     "lines": [["P", "**P**ee — diuretics (furosemide, thiazide)"], ["P", "**P**ain-free — NSAIDs"],
               ["P", "**P**enicillins และ cephalosporins (β-lactam)"], ["P", "**P**roton pump inhibitors"],
               ["P", "rifam**P**in"]],
     "note": "สไลด์ p22 เน้น β-lactam (✍️ penicillin), sulfonamide, rifampicin, cimetidine · ✍️ \"จำ\" กลุ่มยาและติดเชื้อ (leptospirosis, hantavirus)",
     "src": "First Aid for the USMLE Step 1 (Renal — acute interstitial nephritis \"5 P's\")"},
    {"sec": "nephro-aki-07", "name": "Cast บอกที่มา", "what": "ชนิดของ cast ในปัสสาวะกับตำแหน่งโรค",
     "lines": [["RBC cast", "glomerulonephritis"], ["WBC cast", "AIN · pyelonephritis"],
               ["Muddy brown granular", "ATN"], ["Fatty cast / oval fat body", "nephrotic syndrome"],
               ["Waxy / broad cast", "CKD ระยะท้าย"], ["Hyaline cast", "ปกติ · ขาดน้ำ (pre-renal)"]],
     "note": "สไลด์ p32 เขียน ATN ว่า \"typical: bland sediment\" — ในทางปฏิบัติ granular cast + renal tubular epithelial cell พบได้บ่อยและเป็นคำตอบมาตรฐานของข้อสอบ",
     "src": "First Aid for the USMLE Step 1 (Renal — urinary casts)"},
    {"sec": "nephro-aki-15", "name": "DMARD", "what": "pre-renal ที่ FENa \"สูง\" (> 2%) — กับดักของ FENa",
     "lines": [["D", "**D**iuretic use"], ["M", "**M**ineralocorticoid deficiency"], ["A", "**A**lkalosis (metabolic) — bicarbonaturia ลาก Na"],
               ["R", "**R**enal salt wasting"], ["D", "**D**M — glycosuria (osmotic diuresis)"]],
     "note": "เพิ่ม: CKD เดิม และ pre-renal ที่ได้น้ำเกลือมาแล้ว ก็ทำให้ FENa สูงได้",
     "src": "สไลด์ อ.วรรณิยา p51 (ARF with high FENa)"},
    {"sec": "nephro-aki-11", "name": "Heme+ ไม่มี RBC", "what": "dipstick blood บวกแต่กล้องไม่เห็น RBC",
     "lines": [["Myoglobin", "plasma ใส · CK สูงมาก → rhabdomyolysis"], ["Hemoglobin", "plasma ชมพู · haptoglobin ต่ำ LDH สูง → hemolysis"],
               ["หลอก", "RBC แตกในปัสสาวะที่ตั้งนาน/เจือจาง (✍️ ส่ง UA ใน 2 ชม.)"]],
     "note": "dipstick ใช้ peroxidase activity ของ heme จึงไม่แยก RBC, hemoglobin และ myoglobin",
     "src": "หลักจำทั่วไป · สไลด์ p32–33 (ดัดแปลงจาก UpToDate: approach to red or brown urine)"},
    {"sec": "nephro-aki-16", "name": "C BIG K DROP", "what": "ลำดับยาแก้ hyperkalemia",
     "lines": [["C", "**C**alcium gluconate — ปกป้องหัวใจ"], ["B", "**B**icarbonate (เมื่อมี acidosis) / **B**eta-agonist"],
               ["I G", "**I**nsulin + **G**lucose"], ["K", "**K**ayexalate/K binder (Kalimate, Lokelma)"],
               ["DROP", "**D**iuretic (loop) · **D**ialysis"]],
     "note": "✍️ อาจารย์: insulin ให้ทาง IV · ถ้าน้ำตาล > 250 mg/dL ให้ RI อย่างเดียวไม่ต้องให้ glucose",
     "src": "หลักจำทั่วไปของนักศึกษาแพทย์ (C BIG K DROP)"},
    {"sec": "nephro-aki-17", "name": "AEIOU", "what": "ข้อบ่งชี้การฟอกเลือดเร่งด่วน",
     "lines": [["A", "**A**cidosis — รุนแรง ดื้อต่อการรักษา"], ["E", "**E**lectrolyte — K สูงดื้อต่อยา"],
               ["I", "**I**ntoxication — methanol, ethylene glycol, lithium, salicylate"],
               ["O", "**O**verload — น้ำเกินดื้อต่อ diuretic"], ["U", "**U**remia — pericarditis, encephalopathy, bleeding"]],
     "note": "สไลด์ p72: อาการ uremia = \"Too late\" — key คือน้ำเกินและกรด-ด่างที่ไม่ตอบสนองต่อยาเต็มที่",
     "src": "หลักจำทั่วไป (First Aid / ตำราอายุรศาสตร์ — indications for urgent dialysis)"},
]


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "anims_nephro_aki.json"
    json.dump({"set": "nephro", "items": ITEMS, "mnem": MNEM}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("anims %d · mnem %d → %s" % (len(ITEMS), len(MNEM), out))
