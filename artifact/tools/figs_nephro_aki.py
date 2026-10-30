# -*- coding: utf-8 -*-
"""ภาพประกอบนิ่ง (section.figs) ของคาบ nephro 42 "Acute kidney injury" (พญ.วรรณิยา มีนุ่น) — ใช้ใน build_aki.py

ทุกฟังก์ชันคืน fig(title, cap, svg) · กว้าง ≤ 420 (อ่านบนมือถือได้) · ภาพเป็น "แผนผัง" ไม่ใช่สัดส่วนจริง"""
from svg import *


def _rows(x, y, w, rows, h=30, gap=6, fs=None):
    """แถวกล่อง (ข้อความซ้าย, ข้อความขวา, คลาส)"""
    out = []
    for a, b, c in rows:
        out += [rect(x, y, w, h, c, 7), t(x + 10, y + h / 2 + 4, a, "sm b"), t(x + w - 10, y + h / 2 + 4, b, "xs end")]
        y += h + gap
    return out


# ═══════════════════════════════════════ 1 ไตทำอะไร → ไตวายเสียอะไร
def func_fail():
    L = [("ขับของเสีย", "BUN · creatinine · กรด", "ac"),
         ("รักษาสมดุล", "น้ำ · Na · K · กรด-ด่าง", "wa"),
         ("คุมความดัน", "renin · Na/น้ำ", "ms"),
         ("สร้างฮอร์โมน", "EPO · vitamin D (1α)", "ok")]
    R = [("BUN/Cr ↑ · uremia", "bad"), ("บวม น้ำท่วมปอด · K↑ · กรด", "bad"),
         ("ความดันสูง", "ms"), ("ซีด · กระดูกบาง (เรื้อรัง)", "sk")]
    out = [t(105, 18, "ไตปกติทำ", "sm b mid"), t(318, 18, "เมื่อไตวาย (สไลด์ p4)", "sm b mid")]
    y = 30
    for (a, b, c), (r, rc) in zip(L, R):
        out += [rect(10, y, 190, 50, c, 9), t(20, y + 21, a, "sm b"), t(20, y + 39, b, "xs i2"),
                ar(202, y + 25, 226, y + 25, "lbad w2", "ah-bad"),
                rect(228, y, 182, 50, rc, 9), t(319, y + 30, r, "xs b mid")]
        y += 60
    out += [rect(10, 274, 400, 46, "sk", 9),
            t(210, 293, "AKI: ขับของเสีย + รักษาสมดุล เสียภายในชั่วโมง–วัน", "xs b mid"),
            t(210, 311, "ส่วนการสร้างฮอร์โมน (ซีด/กระดูก) ต้องใช้เวลานาน → บอก CKD มากกว่า", "xs mid i2")]
    return fig("ไตทำอะไร — และเสียอะไรเมื่อไตวาย",
               "สไลด์ p3–p4 แบ่งหน้าที่ไตเป็น **ขับของเสีย** (waste product) · **รักษาสมดุล** น้ำ เกลือแร่ กรด-ด่าง · **คุมความดัน** · **สร้างฮอร์โมน** (erythropoietin, vitamin D) · ใน **AKI** สิ่งที่ฆ่าผู้ป่วยได้เร็วคือ \"regulation failure\" — **น้ำเกิน K สูง และกรด** ส่วน \"synthesis failure\" (ซีด, osteodystrophy) ต้องใช้เวลาเป็นเดือน จึงเป็นเบาะแสของ **CKD**",
               svg(420, 328, "ซ้ายคือหน้าที่ของไตสี่ด้าน ขวาคือผลเมื่อไตวาย", *out))


# ═══════════════════════════════════════ 2 RIFLE (สไลด์) เทียบ KDIGO 2012
def rifle_kdigo():
    out = [t(112, 18, "RIFLE (สไลด์ p6)", "sm b mid"), t(318, 18, "KDIGO 2012 (ใช้ปัจจุบัน)", "sm b mid")]
    rows = [("Risk", "Cr ×1.5 · UO<0.5 ×6 ชม.", "Stage 1", "Cr ×1.5–1.9 หรือ ↑≥0.3\nใน 48 ชม. · UO<0.5 ×6–12 ชม.", "ms"),
            ("Injury", "Cr ×2 · UO<0.5 ×12 ชม.", "Stage 2", "Cr ×2.0–2.9\nUO<0.5 ≥12 ชม.", "bad"),
            ("Failure", "Cr ×3 · UO<0.3 ×24 ชม.\nหรือ anuria ×12 ชม.", "Stage 3", "Cr ×3 หรือ Cr ≥4.0 หรือเริ่ม RRT\nUO<0.3 ≥24 ชม. / anuria ≥12", "bad")]
    y = 30
    for a, b, c, d, k in rows:
        out += [rect(10, y, 200, 58, k, 8), t(20, y + 20, a, "sm b"), t(20, y + 36, b, "xs", 1.3),
                rect(216, y, 194, 58, k, 8), t(226, y + 20, c, "sm b"), t(226, y + 36, d, "xs", 1.3)]
        y += 64
    out += [rect(10, y, 200, 44, "sk", 8), t(20, y + 18, "Loss > 4 สัปดาห์", "xs b"), t(20, y + 34, "ESKD > 3 เดือน", "xs b"),
            rect(216, y, 194, 44, "sk", 8), t(226, y + 18, "AKD 7–90 วัน · CKD > 90 วัน", "xs b"), t(226, y + 34, "(KDIGO — ไม่อยู่ในสไลด์)", "xs mu"),
            rect(10, y + 52, 400, 40, "ac", 8),
            t(210, y + 69, "ใช้เกณฑ์ที่ \"รุนแรงกว่า\" ระหว่าง Cr กับ UO", "xs b mid"),
            t(210, y + 85, "✍️ UO คิดต่อ ideal body weight ≈ ส่วนสูง(ซม.) − 100", "xs mid")]
    return fig("RIFLE ในสไลด์ เทียบกับ KDIGO 2012",
               "สไลด์ใช้ **RIFLE** (Risk = high sensitivity, Failure = high specificity) · แนวทางปัจจุบันคือ **KDIGO 2012** ที่รวม AKIN เข้ามา: เพิ่มเกณฑ์ **Cr เพิ่ม ≥0.3 mg/dL ใน 48 ชม.** (เพราะแม้ Cr ขึ้นนิดเดียวก็สัมพันธ์กับอัตราตายที่สูงขึ้น) และ **Cr ≥4.0 หรือเริ่ม RRT = stage 3** · ตัด \"GFR ลด >25/50/75%\" ออก · ✍️ อาจารย์ให้คิด UO ต่อ **ideal body weight (ส่วนสูง − 100)** ไม่ใช่น้ำหนักจริงที่บวมน้ำ",
               svg(420, 352, "ตารางเทียบเกณฑ์ RIFLE ในสไลด์กับ KDIGO 2012 ทีละระดับ", *out))


# ═══════════════════════════════════════ 3 UA หน้าตาแบบใด — แผนที่ตะกอนปัสสาวะ
def sediment():
    rows = [("Bland sediment", "ไม่มี cast/เซลล์", "pre / post / vascular", "sk"),
            ("Hyaline cast", "THP ล้วน", "pre-renal / ปกติ", "sk"),
            ("Muddy brown granular\n+ RTE cells", "เซลล์ท่อไตหลุดลอก", "ATN", "ms"),
            ("Dysmorphic RBC\n+ RBC cast", "เลือดออกจาก glomerulus", "GN / RPGN", "bad"),
            ("WBC cast · sterile pyuria\n± eosinophiluria", "อักเสบใน interstitium", "AIN (pyelo)", "wa"),
            ("Heme 3+ แต่ RBC 0–2", "myoglobin / hemoglobin", "pigment ATN", "bad"),
            ("Crystals", "uric · oxalate · ยา", "intrarenal obstruction", "ok")]
    out = [t(14, 18, "สิ่งที่เห็นในตะกอน", "xs b mu"), t(210, 18, "มาจากอะไร", "xs b mu"), t(406, 18, "นึกถึง", "xs b mu end")]
    y = 26
    for a, b, c, k in rows:
        n = a.count("\n") + 1
        h = 30 if n == 1 else 40
        out += [rect(10, y, 400, h, k, 7), t(18, y + (19 if n == 1 else 16), a, "xs b", 1.25),
                t(206, y + h / 2 + 4, b, "xs"), t(402, y + h / 2 + 4, c, "xs b end")]
        y += h + 5
    out += [t(210, y + 14, "UA ต้องส่งตรวจภายใน 2 ชม. (✍️) — cast/RBC สลายในปัสสาวะที่ตั้งทิ้ง", "xs mid i2")]
    return fig("UA หน้าตาแบบใด — ตะกอนปัสสาวะบอกตำแหน่งที่เสีย",
               "อาจารย์ถาม \"UA หน้าตาแบบใด\" ในทุกกลุ่มสาเหตุ: **pre-renal, vascular, crystal และ post-renal → typical bland sediment** (protein 1+–2+ ได้ แต่ <500 mg/วัน) · **GN → dysmorphic RBC + RBC cast** · **AIN → WBC, WBC cast ไม่มี RBC cast** · ATN สไลด์เขียน \"bland\" แต่ตำราและข้อสอบส่วนใหญ่ใช้ **muddy brown granular cast + renal tubular epithelial cell** เป็นลักษณะเด่น · **pigment ATN → dipstick blood 3+ แต่เห็น RBC น้อย**",
               svg(420, y + 24, "ตารางลักษณะตะกอนปัสสาวะแต่ละแบบกับกลุ่มสาเหตุของ AKI", *out))


# ═══════════════════════════════════════ 4 สาเหตุ pre-renal 4 กลไก (สไลด์ p8–10)
def prerenal_causes():
    bx = [(10, 28, "ECV ลด", "fluid loss: burn diarrhea diuretic\nsequestration: pancreatitis crush\ncirrhosis malnutrition", "wa"),
          (214, 28, "Cardiac output ลด", "HF · ✍️ amphetamine, alcohol\n(cardiomyopathy)\ncardiorenal", "ms"),
          (10, 128, "Vasodilatation", "✍️ sepsis (พบบ่อยสุด) · ยาลดความดัน\nadrenal insufficiency · Mg↑\nhypercapnia · hypoxemia", "bad"),
          (214, 128, "Renal vasoconstriction", "sepsis · ✍️ NSAIDs · α-agonist\nhepatorenal syndrome\n+ occlusion: thrombus, emboli", "bad")]
    out = []
    for x, y, a, b, c in bx:
        out += [rect(x, y, 196, 92, c, 9), t(x + 10, y + 20, a, "sm b"), t(x + 10, y + 40, b, "xs", 1.35)]
    out += [t(210, 18, "สาเหตุ pre-renal 4 กลไก", "sm b mid"),
            ar(108, 222, 190, 250, "lbad w2", "ah-bad"), ar(312, 222, 230, 250, "lbad w2", "ah-bad"),
            rect(110, 252, 200, 40, "ac", 9), t(210, 270, "เลือดไปไตลด (RBF ↓)", "sm b mid"), t(210, 286, "→ GFR ↓ · เนื้อไตยังดี", "xs mid"),
            rect(10, 302, 400, 40, "sk", 9),
            t(210, 320, "แก้สาเหตุทัน → กลับคืนใน 24–72 ชม.", "xs b mid tok"),
            t(210, 336, "ปล่อยนาน → ischemic ATN (หัวข้อ 9)", "xs b mid tbad")]
    return fig("Pre-renal — เลือดไปไตไม่พอ จาก 4 กลไก",
               "สไลด์ p8–10 แบ่ง pre-renal azotemia เป็น **effective ECV ลด** (เสียน้ำหรือน้ำไปอยู่ผิดที่) · **cardiac output ลด** · **หลอดเลือดส่วนปลายขยาย** (✍️ sepsis พบบ่อยสุด) · **หลอดเลือดไตหดตัวรุนแรง** (sepsis, ✍️ NSAIDs, α-agonist, hepatorenal) และ **การอุดของหลอดเลือด** — ทุกทางจบที่ **renal blood flow ลด → GFR ลด ขณะที่เนื้อไตยังปกติ** จึง \"if identified and treated, usually reversible\"",
               svg(420, 350, "สี่กลไกของ pre-renal azotemia ที่ทำให้เลือดไปไตลดและ GFR ลด", *out))


# ═══════════════════════════════════════ 5 Vascular disorders (สไลด์ p13 + ลายมือ)
def vascular():
    rows = [("① TTP / HUS (TMA)", "MAHA + เกล็ดเลือดต่ำ + ✍️ อาการทางสมอง", "plasma exchange", "bad"),
            ("② Scleroderma renal crisis", "SSc + ✍️ prednisolone ขนาดสูง · BP พุ่ง", "ACE inhibitor", "ms"),
            ("③ Renal vein thrombosis", "✍️ membranous nephropathy · APS\nปวดสีข้าง + hematuria", "anticoagulant", "wa"),
            ("④ Malignant HT", "BP ≥180/120 + จอตาเลือดออก/บวม", "ลด BP อย่างควบคุม", "ms"),
            ("APS", "หญิงอายุน้อย ลิ่มเลือด/แท้ง", "anticoagulant", "sk")]
    out = [t(14, 18, "โรค (✍️ ลำดับที่พบบ่อย)", "xs b mu"), t(406, 18, "รักษาหลัก", "xs b mu end")]
    y = 26
    for a, b, c, k in rows:
        n = b.count("\n") + 1
        h = 46 if n == 1 else 58
        out += [rect(10, y, 400, h, k, 8), t(20, y + 19, a, "sm b"), t(20, y + 36, b, "xs", 1.3),
                t(400, y + 19, c, "xs b end tac")]
        y += h + 6
    out += [rect(10, y, 400, 34, "sk", 8), t(210, y + 21, "UA: bland ได้ · RBC/dysmorphic ได้ แต่ \"ไม่มี RBC cast\"", "xs b mid")]
    return fig("Renal vascular disorders — โรคที่ทำลายหลอดเลือดเล็กในไต",
               "สไลด์ p13 + ลายมือ: อาจารย์เรียงความถี่ **① TTP/HUS (TMA) ② scleroderma renal crisis ③ renal vein thrombosis ④ malignant hypertension** · ✍️ \"หญิงอายุ 26 ปี AKI + MAHA → คิด TTP → หาสาเหตุรอง (SLE) → ต้องรีบทำ plasma exchange\" · UA (p14) มักเป็น bland หรือมี microscopic hematuria/dysmorphic RBC ได้ แต่ **ไม่มี RBC cast** ซึ่งช่วยแยกจาก GN · การรักษาในคอลัมน์ขวาอิงตำรา/แนวทาง (ISTH 2020 สำหรับ TTP)",
               svg(420, y + 42, "ตารางโรคหลอดเลือดไตห้าโรค พร้อมเบาะแสและการรักษาหลัก", *out))


# ═══════════════════════════════════════ 6 ATN 3 ระยะ
def atn_phases():
    out = [line(40, 40, 40, 236, "ln w2"), line(40, 236, 410, 236, "ln w2"),
           t(34, 34, "ระดับ", "xs end mu"), t(410, 254, "เวลา", "xs end mu"),
           # zone shading
           rect(42, 44, 70, 190, "ms", 0), rect(112, 44, 170, 190, "bad", 0), rect(282, 44, 126, 190, "ok", 0),
           t(77, 60, "เริ่มต้น", "xs b mid"), t(77, 74, "ชม.–วัน", "xs mid"),
           t(197, 60, "คงที่ (maintenance)", "xs b mid"), t(197, 74, "~1–3 สัปดาห์", "xs mid"),
           t(345, 60, "ฟื้นตัว", "xs b mid"), t(345, 74, "polyuria", "xs mid"),
           # creatinine curve
           path("M44 210 C90 206 110 170 150 120 C180 92 230 90 270 96 C300 102 330 150 406 196", "lbad w3"),
           t(160, 108, "Cr", "sm b tbad"),
           # urine output curve
           path("M44 120 C70 124 100 200 130 212 C180 222 240 220 280 200 C300 150 320 96 350 94 C380 96 395 120 406 136", "lwa w3 da"),
           t(352, 88, "UO", "sm b twa"),
           t(220, 272, "เส้นทึบ = creatinine · เส้นประ = ปริมาณปัสสาวะ", "xs mid mu")]
    return fig("ATN 3 ระยะ — ทำไมช่วงฟื้นตัวปัสสาวะออกมาก",
               "**ระยะเริ่มต้น** (initiation) — ขาดเลือดหรือได้สารพิษ เซลล์ท่อไตเริ่มบาดเจ็บ ยังป้องกันได้ · **ระยะคงที่** (maintenance) — GFR ต่ำ Cr ขึ้นต่อเนื่อง ปัสสาวะน้อย (หรือไม่น้อยใน non-oliguric ATN) ช่วงนี้ภาวะแทรกซ้อน K สูง น้ำเกิน กรด เกิดมากที่สุด · **ระยะฟื้นตัว** — เซลล์ใหม่ปกคลุมท่อแต่ **ยังดูดน้ำ/เกลือกลับไม่เก่ง** ร่วมกับ urea ที่คั่งดึงน้ำออก (solute diuresis) → **polyuria เสีย K Mg PO4** ต้องดู balance และเกลือแร่ทุกวัน (ส่วนระยะเป็นความรู้ตำรา ไม่อยู่ในสไลด์)",
               svg(420, 280, "กราฟ creatinine และปริมาณปัสสาวะตามสามระยะของ ATN", *out))


# ═══════════════════════════════════════ 7 แผนที่ยา/สารพิษที่ทำร้ายไตตามตำแหน่ง nephron
def nephrotox_map():
    out = [
        # afferent + glomerulus + efferent
        path("M20 70 L84 70", "lbad w5"), t(20, 60, "afferent", "xs mu"),
        circ(110, 70, 26, "bad"), t(110, 74, "glom", "xs b mid"),
        path("M136 70 L190 70", "lbad w3"), t(150, 60, "efferent", "xs mu"),
        # tubule
        path("M110 96 C110 130 150 130 190 130 L300 130 C330 130 330 170 300 170 L170 170 C140 170 140 210 170 210 L330 210 C360 210 380 230 380 260", "lwa w5"),
        t(200, 122, "proximal tubule", "xs mu"), t(186, 162, "loop", "xs mu"), t(300, 202, "distal / collecting duct", "xs mu"),
        # labels
        rect(6, 84, 92, 46, "ms", 6), t(12, 100, "หด: NSAID", "xs b"), t(12, 113, "contrast · CNI", "xs"), t(12, 125, "α-agonist", "xs"),
        rect(196, 22, 100, 36, "ms", 6), t(204, 37, "ขยาย: ACEi/ARB", "xs b"), t(204, 51, "(GFR ตก)", "xs"),
        rect(310, 92, 104, 64, "bad", 6), t(316, 108, "เซลล์ PT ตาย", "xs b"), t(316, 121, "aminoglycoside", "xs"),
        t(316, 134, "contrast · cisplatin", "xs"), t(316, 147, "heme (rhabdo)", "xs"),
        rect(6, 176, 130, 50, "ok", 6), t(12, 192, "ตกผลึกในท่อ", "xs b"), t(12, 205, "acyclovir · MTX", "xs"), t(12, 218, "sulfa · uric acid", "xs"),
        rect(190, 232, 130, 50, "wa", 6), t(196, 248, "interstitium (AIN)", "xs b"), t(196, 261, "β-lactam · NSAID", "xs"), t(196, 274, "PPI · rifampicin", "xs"),
        rect(330, 270, 84, 36, "sk", 6), t(336, 285, "lithium →", "xs b"), t(336, 298, "NDI (CD)", "xs"),
    ]
    return fig("ยาและสารที่ทำร้ายไต — แต่ละตัวโจมตีตรงไหนของ nephron",
               "แบ่งตามตำแหน่งช่วยเดาได้ว่า UA และ FENa จะออกมาแบบไหน: **หลอดเลือด** (NSAID หด afferent · ACEi/ARB ขยาย efferent · contrast/calcineurin inhibitor หดหลอดเลือด) → ทำงานแบบ pre-renal FENa ต่ำ · **เซลล์ proximal tubule** (aminoglycoside, contrast, cisplatin, heme) → ATN · **ในท่อไต** (acyclovir, methotrexate, sulfonamide, uric acid) → crystal · **interstitium** (β-lactam, NSAID, PPI, rifampicin) → AIN · **lithium** ที่ collecting duct → nephrogenic DI (ปัสสาวะมาก ไม่ตอบ desmopressin) · สไลด์ระบุ aminoglycoside, radiocontrast, ✍️ acyclovir และยา crystal — ส่วนอื่นเติมจากตำรา",
               svg(420, 312, "แผนผัง nephron แสดงตำแหน่งที่ยาและสารพิษแต่ละกลุ่มทำร้ายไต", *out))


# ═══════════════════════════════════════ 8 AKI vs CKD
def aki_ckd():
    rows = [("Cr เดิม", "ปกติเมื่อเร็ว ๆ นี้", "สูงมานาน", ""),
            ("ขนาดไต (U/S)", "ปกติ 10–12 ซม.", "เล็ก < 9 ซม.", ""),
            ("Echo · cortex", "ปกติ", "ขาวขึ้น · บาง · CMJ ไม่ชัด", ""),
            ("ซีด", "ไม่มี/จากสาเหตุอื่น", "normocytic (EPO ลด)", ""),
            ("Ca · PO4 · PTH", "PO4 สูงได้", "Ca ต่ำ PTH สูง กระดูก", ""),
            ("Cast", "ตามสาเหตุ", "broad / waxy", "")]
    out = [rect(10, 10, 400, 26, "ac", 6), t(20, 28, "เบาะแส", "xs b"), t(200, 28, "AKI", "xs b mid"), t(334, 28, "CKD", "xs b mid")]
    y = 42
    for a, b, c, _ in rows:
        out += [rect(10, y, 400, 28, "bx", 5), t(20, y + 18, a, "xs b"), t(200, y + 18, b, "xs mid"), t(334, y + 18, c, "xs mid tbad")]
        y += 32
    out += [rect(10, y + 4, 400, 52, "ms", 8),
            t(20, y + 22, "ไต \"ใหญ่\" แม้เป็น CKD: DM · amyloid · HIVAN · ADPKD · myeloma", "xs b"),
            t(20, y + 40, "✍️ ไตสองข้างต่างกัน > 1.5 ซม. → คิด renovascular / ข้างเดียวฝ่อ", "xs")]
    return fig("Step 2 — AKI หรือ CKD (หรือ AKI บน CKD)",
               "สไลด์ p46 ให้แยกด้วย **ประวัติ ตรวจร่างกาย และแล็บ** · เบาะแสที่ช่วยมากที่สุดคือ **creatinine เดิม** และ **ultrasound** (สไลด์ p58: kidney size, echogenicity, cortical thickness, corticomedullary junction) · ไตเล็ก ขาว cortex บาง = เรื้อรัง · แต่ **DM, amyloidosis, HIVAN, ADPKD, myeloma** ไตไม่เล็กแม้เป็น CKD · ✍️ ไตสองข้างขนาดต่างกันเกิน 1.5 ซม. ชวนคิดโรคหลอดเลือดแดงไตหรือไตข้างหนึ่งฝ่อ · ✍️ เจอก้อนสงสัย RCC → **ห้ามเจาะไต** ส่ง CT/MRI แล้วผ่าตัด (ตัวเลขขนาดไตอิงตำรา)",
               svg(420, y + 62, "ตารางเปรียบเทียบเบาะแสที่แยก AKI กับ CKD", *out))


# ═══════════════════════════════════════ 9 FENa — คิดทีละขั้น
def fena():
    out = [rect(10, 10, 400, 66, "ac", 9),
           t(210, 32, "FENa = (U Na × P Cr) / (P Na × U Cr) × 100", "sm b mid"),
           t(210, 52, "= Na ที่ถูกขับ ÷ Na ที่ถูกกรอง", "xs mid"),
           t(210, 68, "(creatinine ถูกกรองแต่แทบไม่ถูกดูดกลับ = ตัวแทน GFR)", "xs mid i2"),
           rect(10, 86, 196, 112, "ok", 9), t(108, 106, "ท่อไตยังดี", "sm b mid"),
           t(108, 126, "RAAS ดูด Na กลับ", "xs mid"), t(108, 142, "U Na < 20 · FENa < 1%", "xs b mid"),
           t(108, 158, "ADH → Uosm > 400–500", "xs mid"), t(108, 174, "= pre-renal", "sm b mid tok"),
           rect(214, 86, 196, 112, "bad", 9), t(312, 106, "ท่อไตเสีย", "sm b mid"),
           t(312, 126, "ดูด Na ไม่ได้", "xs mid"), t(312, 142, "U Na > 30–40 · FENa > 2%", "xs b mid"),
           t(312, 158, "ทำเข้มข้นไม่ได้ Uosm ~300", "xs mid"), t(312, 174, "= ATN", "sm b mid tbad"),
           rect(10, 208, 400, 76, "ms", 9),
           t(20, 226, "ตัวอย่าง: U Na 68, P Na 136, U Cr 40, P Cr 4.0", "xs b"),
           t(20, 244, "(68/136) ÷ (40/4.0) = 0.5 ÷ 10 = 0.05 → × 100 = 5%  → ATN", "xs"),
           t(20, 262, "กับดัก: ได้ยาขับปัสสาวะ → FENa สูงหลอก → ใช้ FEurea", "xs b tbad"),
           t(20, 278, "FEurea < 35% = pre-renal · > 50% = ATN", "xs")]
    return fig("FENa — คำนวณทีละขั้น และกับดักที่พบบ่อย",
               "สไลด์ p49: **FENa = (U Na / P Na) ÷ (U Cr / P Cr) × 100** · ใช้แปลผลเฉพาะ **AKI ที่ปัสสาวะน้อย** · pre-renal: ท่อไตยังดีและ RAAS กับ ADH ทำงานเต็มที่ → **FENa < 1%** · ATN: ดูด Na กลับไม่ได้ → **> 1–2%** · ข้อยกเว้นในสไลด์ p50–51: ATN ที่ FENa ต่ำ (contrast, rhabdomyolysis, hemolysis, sepsis, burn, non-oliguric) และ pre-renal ที่ FENa สูง (\"DMARD\") · **ผู้ได้ diuretic ใช้ FEurea** (urea ดูดกลับที่ proximal ไม่ขึ้นกับ loop/thiazide — เกณฑ์ FEurea อิงตำรา ไม่อยู่ในสไลด์)",
               svg(420, 292, "สูตร FENa และการแปลผลแยก pre-renal กับ ATN พร้อมตัวอย่างคำนวณ", *out))


# ═══════════════════════════════════════ 10 Hyperkalemia — ทำ 3 ขั้น
def hyperk_tx():
    cols = [("1 ปกป้องหัวใจ", "bad", ["Ca gluconate 10%", "10 mL (1 g) IV", "ฉีด 2–3 นาที", "ออกฤทธิ์ 1–3 นาที", "ซ้ำได้ถ้า ECG ยังผิด"]),
            ("2 ดัน K เข้าเซลล์", "ms", ["RI 10 U IV +", "50% glucose 50 mL", "✍️ glucose > 250", "→ RI อย่างเดียว", "salbutamol · NaHCO3*"]),
            ("3 เอา K ออก", "ok", ["loop diuretic", "Kalimate/Dekales", "(ช้า หลายชม.)", "Lokelma (~1 ชม.)", "dialysis ถ้าดื้อยา"])]
    out = []
    x = 10
    for h, c, ls in cols:
        out += [rect(x, 10, 128, 30, c, 8), t(x + 64, 30, h, "xs b mid")]
        y = 52
        for s in ls:
            out += [t(x + 4, y, s, "xs")]
            y += 17
        x += 136
    out += [ar(138, 25, 146, 25, "ln", "ah"), ar(274, 25, 282, 25, "ln", "ah"),
            rect(10, 128, 400, 82, "sk", 8),
            t(20, 146, "ไม่ลด K ในเลือด: Ca (แค่กันหัวใจ) · insulin/β2 (แค่ย้ายที่ ~4–6 ชม.)", "xs b"),
            t(20, 163, "ลด K จริง: ขับทางปัสสาวะ ลำไส้ หรือ dialysis", "xs b tok"),
            t(20, 180, "หยุด K supplement · K-sparing diuretic · ACEi/ARB · NSAID", "xs"),
            t(20, 197, "*NaHCO3 เฉพาะมี metabolic acidosis · ✍️ ระวังถ้า CO2 สูงอยู่แล้ว", "xs i2")]
    return fig("รักษา hyperkalemia ใน AKI — ปกป้อง ย้าย แล้วเอาออก",
               "ตามตารางสไลด์ p66: **calcium gluconate/chloride 1 g** กันหัวใจ · **insulin 10 units regular + glucose 50 mL ของ 50% dextrose** · **inhaled β-agonist** · **K binder** (Kalimate/Dekales = calcium polystyrene sulfonate · Lokelma = sodium zirconium cyclosilicate เร็วกว่า ราคา ~300–400 บาท/ซอง) · **loop diuretic** · **dialysis** · ✍️ insulin ต้องให้ทาง IV และถ้าน้ำตาลสูงเกิน 250 mg/dL ให้ RI อย่างเดียว · เวลาออกฤทธิ์ของแต่ละตัวอิงตำรา",
               svg(420, 218, "สามขั้นของการรักษาภาวะโพแทสเซียมสูง ปกป้องหัวใจ ย้ายเข้าเซลล์ และเอาออกจากร่างกาย", *out))


# ═══════════════════════════════════════ 11 เริ่ม dialysis เมื่อไร — "Too late"
def rrt_timing():
    out = [rect(10, 10, 400, 30, "ac", 8), t(210, 30, "Key for initiating RRT in AKI (สไลด์ p72)", "sm b mid"),
           rect(10, 48, 400, 64, "ok", 9),
           t(20, 68, "1. น้ำเกินที่ไม่ตอบสนองต่อยาเต็มที่", "sm b"),
           t(20, 88, "2. กรด-ด่าง (และ K) ที่ไม่ตอบสนองต่อยาเต็มที่", "sm b"),
           t(20, 104, "→ เริ่ม \"ก่อน\" อวัยวะอื่นเสีย", "xs tok b"),
           rect(10, 120, 400, 84, "bad", 9),
           t(20, 140, "รอจนมีอาการ uremia = สายเกินไป (Too late)", "sm b tbad"),
           t(20, 160, "early: เบื่ออาหาร คลื่นไส้ อาเจียน คัน", "xs"),
           t(20, 177, "uremic encephalopathy · uremic pericarditis", "xs"),
           t(20, 194, "✍️ \"End stage\" — เป็นภาวะท้าย ๆ แล้ว", "xs b"),
           rect(10, 212, 400, 60, "sk", 9),
           t(20, 231, "เกณฑ์ตัวเลขในสไลด์ p71 (ใช้ประกอบ ไม่ใช่ตัวตัดสินเดี่ยว):", "xs b"),
           t(20, 248, "BUN > 100 หรือ Cr > 10 (non-catabolic)", "xs"),
           t(20, 264, "BUN > 70 หรือ Cr > 7 (hypercatabolic)", "xs")]
    return fig("เริ่ม dialysis ใน AKI เมื่อไร — ก่อน \"too late\"",
               "สไลด์ p71 ให้ข้อบ่งชี้: **hyperkalemia, volume overload, severe metabolic acidosis ที่ไม่ตอบสนองต่อยาเต็มที่ · uremic symptom · uremic pericarditis · BUN/Cr สูงตามเกณฑ์** · p72 อาจารย์กากบาทอาการ uremia ว่า **\"Too late\"** และเน้น **2 ข้อหลัก: น้ำเกินกับกรด-ด่างที่ดื้อยา** · KDIGO 2012 ก็ให้เริ่ม RRT เร่งด่วนเมื่อมีความผิดปกติของน้ำ เกลือแร่ กรด-ด่างที่คุกคามชีวิต และให้ดูภาพรวมทางคลินิกมากกว่าค่า BUN/Cr เพียงอย่างเดียว",
               svg(420, 280, "หลักการเริ่มการบำบัดทดแทนไตในผู้ป่วย AKI ตามสไลด์", *out))
