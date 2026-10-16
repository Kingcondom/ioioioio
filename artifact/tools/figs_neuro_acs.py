# -*- coding: utf-8 -*-
"""ภาพประกอบ + กลไก คาบ neuro 21/10 Acute confusional state และภาวะการรู้สึกตัวเปลี่ยนแปลง (ใส่ด้วย apply_figs.py)"""
import math
from svg import *

SET, LEC = "neuro", "21/10"

HERN_WHY = """#### กลไก: herniation ทำให้เกิดอาการอย่างไร

| สิ่งตรวจพบ | กลไก | ใช้อย่างไร |
|---|---|---|
| **รูม่านตาข้างเดียวขยาย ไม่ตอบสนอง** | uncus ของ temporal lobe เคลื่อนลงผ่านขอบ tentorium กด **CN III ข้างเดียวกัน** — ใย parasympathetic ที่ทำให้รูม่านตาหดวิ่งอยู่ **ผิวนอกของเส้นประสาท** จึงเสียก่อนการกลอกตา | สัญญาณเตือนแรก ๆ ของ uncal herniation → ลดความดันในกะโหลกและปรึกษาศัลยแพทย์ทันที |
| **อ่อนแรงครึ่งซีก** | cerebral peduncle ถูกกด → อ่อนแรงซีกตรงข้าม · ถ้าก้านสมองถูกดันไปชนขอบ tentorium อีกด้าน (**Kernohan notch**) จะอ่อนแรงข้างเดียวกับรอยโรค | ข้างที่อ่อนแรงอาจหลอกตำแหน่ง → ดูรูม่านตาและ CT ร่วมกัน |
| **ซึมลงจนโคม่า** | midbrain ที่มี **ARAS** ถูกบีบและขาดเลือด | ระดับความรู้สึกตัวที่ลดลงในผู้ป่วยที่มีก้อน = herniation จนกว่าจะพิสูจน์เป็นอื่น |
| **ความดันสูง ชีพจรช้า หายใจผิดปกติ (Cushing)** | ก้านสมองขาดเลือด → sympathetic ดันความดันขึ้นเพื่อให้เลือดเข้าสมอง → baroreflex ทำให้ชีพจรช้า | เป็นสัญญาณระยะท้าย อย่ารอให้ครบสามอย่าง |"""

PUPIL_WHY = """#### กลไก: ทำไมรูม่านตาแต่ละแบบชี้ระดับรอยโรค
- **สองระบบดึงกันอยู่ตลอด** — **parasympathetic** จากนิวเคลียส Edinger–Westphal ที่ **midbrain** วิ่งไปกับ CN III ทำให้ **หด** · **sympathetic** เริ่มที่ **hypothalamus** ลงผ่านก้านสมองและไขสันหลัง แล้วย้อนขึ้นมาที่ตา ทำให้ **ขยาย**
- **Diencephalon หรือเมแทบอลิก** → sympathetic จาก hypothalamus ลดลงบางส่วน แต่วงจรแสงที่ midbrain ยังดี → **เล็กแต่ยังตอบสนอง**
- **Pons** → ทาง sympathetic ที่ลงผ่าน pons ขาด เหลือแต่ parasympathetic → **เล็กเท่าหัวเข็มหมุด** · opioid กระตุ้นฝั่ง parasympathetic จึงได้ภาพเดียวกัน
- **Midbrain** → เสียทั้งนิวเคลียสที่ทำให้หดและทางผ่านของ sympathetic → **ค้างขนาดกลาง 4–6 มม. ไม่ตอบสนอง**
- **CN III ถูกกด** → ใยที่ทำให้หดอยู่ผิวนอกของเส้นประสาท → **ขยายข้างเดียว** ก่อนที่ตาจะกลอกไม่ได้
- **ขาดออกซิเจนรุนแรง หรือ anticholinergic** → ก้านสมองเสียหายกว้างร่วมกับ catecholamine สูง หรือยาบล็อก muscarinic receptor ที่กล้ามเนื้อหดรูม่านตาโดยตรง → **ขยายทั้งสองข้าง**"""

DEL_WHY = """#### กลไก: โรคทางกายทำให้สมองสับสนได้อย่างไร

| อาการ | กลไก | ใช้อย่างไร |
|---|---|---|
| **สมาธิเสีย (อาการหลัก)** | เครือข่ายสมาธิ (prefrontal · parietal · thalamus · ARAS) อาศัย **acetylcholine** เป็นหลัก ภาวะทางกายแทบทุกชนิดลด ACh — ขาดออกซิเจนหรือน้ำตาล (การสร้าง ACh ต้องใช้ acetyl-CoA จากการเผาผลาญกลูโคส) · ยา anticholinergic · cytokine | สาเหตุต่างกันแต่ไปบรรจบที่เดียวกัน อาการจึงหน้าตาคล้ายกัน → **ต้องหาเหตุเสมอ** |
| **กระสับกระส่าย ประสาทหลอน (hyperactive)** | **dopamine เด่นเกิน** เทียบกับ ACh ที่ลดลง · ภาวะถอนสุราหรือ benzodiazepine ทำให้ **GABA ลดฉับพลัน** สมองถูกกระตุ้นเกิน | ยาต้าน dopamine ลดอาการได้ แต่ไม่ได้แก้เหตุ |
| **ซึม เฉื่อย (hypoactive)** | cytokine (IL-1, IL-6, TNF) จากการติดเชื้อส่งสัญญาณผ่าน BBB กระตุ้น **microglia** ให้อักเสบ กดการทำงานของเซลล์ประสาท · ยากดประสาท · สารพิษจากตับหรือไตวาย | ผู้สูงอายุที่ติดเชื้อมักเป็นชนิดนี้ จึงถูกมองข้าม |
| **อาการผันผวนระหว่างวัน** | ระดับการตื่นตัว (ARAS → thalamus) ขึ้นลงตามระดับยา สารพิษ ไข้ และการนอนที่พัง | ต้องประเมินหลายช่วงเวลา ไม่ใช่ครั้งเดียว |
| **ผู้สูงอายุและผู้ที่สมองเสื่อมเป็นง่าย** | เซลล์ประสาทและ ACh สำรองเหลือน้อย (brain reserve ต่ำ) สิ่งกระตุ้นเพียงเล็กน้อยก็ข้ามเกณฑ์ | ความสับสนที่เกิดใหม่ในผู้สูงอายุ = หาโรคทางกายก่อน |"""

INSERTS = [
    ("neuro-acs-01", "**Delirium คือความผิดปกติของ content", "fig:acs_aras"),
    ("neuro-acs-01", "**3) รอยโรคในโพรงสมองส่วนหลัง", "fig:acs_3lesion"),
    ("neuro-acs-01", "$", HERN_WHY),
    ("neuro-acs-02", "**หลักร่วมของทั้งสี่ภาวะ**", "fig:acs_mimic"),
    ("neuro-acs-03", "- **M3 decorticate งอศอก", "fig:acs_motorm"),
    ("neuro-acs-04", "**ประเด็นสุดท้ายนี้คือเหตุผลที่แท้จริง", "fig:acs_gcsfour"),
    ("neuro-acs-05", "**Prevent secondary brain injury", "fig:acs_secondary"),
    ("neuro-acs-05", "- **ในผู้ที่สงสัยภาวะทุพโภชนาการ", "fig:acs_thiamine"),
    ("neuro-acs-06", "| **ขยายทั้งสองข้างและไม่ตอบสนอง**", "fig:acs_pupils"),
    ("neuro-acs-06", "| **ขยายทั้งสองข้างและไม่ตอบสนอง**", PUPIL_WHY),
    ("neuro-acs-06", "- **การหายไปของรีเฟล็กซ์การไอคือ B0", "fig:acs_reflexarc"),
    ("neuro-acs-07", "| **Dysconjugated vertical eye position**", "fig:acs_gaze"),
    ("neuro-acs-07", "> **caloric testing เป็นสิ่งเร้าที่แรงกว่า", "fig:acs_vor"),
    ("neuro-acs-08", "- **ไม่ตอบสนองเลย (flaccid)**", "fig:acs_posture"),
    ("neuro-acs-08", "| **เมดัลลา** |", "fig:acs_rostro"),
    ("neuro-acs-09", "> **กฎที่ช่วยชีวิต", "fig:acs_causes"),
    ("neuro-acs-10", "osmotic demyelination syndrome** จึงต้อง", "fig:acs_ods"),
    ("neuro-acs-10", "**มาตรการลดความดันในกะโหลกที่ควรรู้", "fig:acs_icp"),
    ("neuro-acs-11", "| **การกลับคืน** |", "fig:acs_confuse3"),
    ("neuro-acs-11", "**สังเกตประโยคท้าย**", "fig:acs_threshold"),
    ("neuro-acs-12", "**ความจำระยะใกล้เสียเป็นหลัก", "fig:acs_attnfirst"),
    ("neuro-acs-12", "| **REM Overflow** |", "fig:acs_circadian"),
    ("neuro-acs-13", "> ### **อัลกอริทึม", "fig:acs_cam"),
    ("neuro-acs-14", "^", "fig:acs_delnt"),
    ("neuro-acs-14", "^", DEL_WHY),
    ("neuro-acs-15", "| **5. Management & Resolution**", "fig:acs_trajectory"),
    ("neuro-acs-15", "ล้วนทำให้วงจรกลางวันกลางคืนพัง", "fig:acs_iatro"),
]


def _eyes(cx, cy, rl, rr, dx=0):
    return [ell(cx - 24, cy, 17, 10, "bx"), circ(cx - 24 + dx, cy, rl, "inkf"),
            ell(cx + 24, cy, 17, 10, "bx"), circ(cx + 24 + dx, cy, rr, "inkf")]


# ---------------------------------------------------------------- 01
def acs_aras():
    fans = [(62, 124), (88, 92), (124, 70), (210, 56), (296, 70), (332, 92), (358, 124)]
    out = [t(210, 16, "เปลือกสมองสองซีก — เนื้อหาของการรู้ตัว (content)", "sm mid b tac"),
           path("M30 196 Q30 44 210 40 Q390 44 390 196 Z", "bx"),
           path("M30 196 Q30 44 210 40 Q390 44 390 196", "lac w5"),
           *[ar(210, 148, x, y, "lac", "ah-ac") for x, y in fans],
           rect(194, 184, 32, 42, "sk", 6), ell(210, 246, 30, 24, "sk"), rect(198, 270, 24, 40, "sk", 6),
           line(210, 236, 210, 184, "lac w3"),
           *[circ(210, 196 + 10 * k, 3.4, "acf") for k in range(5)],
           ell(210, 166, 34, 18, "ms"), t(210, 170, "thalamus", "xs mid b"),
           t(252, 182, "สถานีส่งต่อ", "xs i2"),
           t(180, 204, "ARAS", "sm b tac end"), t(180, 220, "midbrain + pons บน", "xs end i2"),
           t(176, 234, "สวิตช์ปลุกให้ตื่น", "xs end i2"),
           t(246, 250, "pons", "xs mu"), t(230, 300, "medulla", "xs mu"),
           box(10, 322, 196, 64, "ac", "Arousal ↓\nARAS / thalamus หรือ\nเปลือกสมองทั้งสองซีก → Coma", fs=11.5),
           box(214, 322, 196, 64, "ms", "Content ↓ แต่ arousal ยังดี\nเปลือกสมองทำงานผิด\n→ Delirium", fs=11.5)]
    return fig("ARAS ปลุก เปลือกสมองคิด",
               "**ARAS** ที่ midbrain และ pons ส่วนบนเป็นสวิตช์ปลุก ส่งสัญญาณขึ้นผ่าน **thalamus** แล้วกระจายไปทั่ว **เปลือกสมองทั้งสองซีก** — โคม่าจึงเกิดได้สองทาง คือ **สวิตช์เสีย** (รอยโรคเล็ก ๆ ที่ ARAS ก็พอ) หรือ **เปลือกสมองเสียทั้งสองซีก** ส่วน delirium คือสวิตช์ยังเปิด แต่เปลือกสมองประมวลผลผิด",
               svg(420, 396, "ARAS ในก้านสมองส่งสัญญาณปลุกผ่าน thalamus ไปยังเปลือกสมองทั้งสองซีก ARAS เสียทำให้โคม่า เปลือกสมองทำงานผิดทำให้ delirium",
                   *out))


def _coronal(x0, y0, mode, title, l1, l2, coma):
    Lx, Rx, cy = x0 + 58, x0 + 142, y0 + 64
    lc = "ms" if mode == "bilat" else "bx"
    out = [t(x0 + 100, y0 + 14, title, "sm b mid"),
           ell(Lx, cy, 42, 36, lc), ell(Rx, cy, 42, 36, lc),
           rect(x0 + 90, y0 + 96, 20, 50, "bad" if mode == "pf" else "sk", 6),
           circ(x0 + 100, y0 + 112, 4.5, "acf")]
    if mode == "mass":
        out += [circ(Lx - 4, cy - 4, 20, "bad"), path("M%d %d Q%d %d %d %d" % (x0 + 100, y0 + 30, x0 + 116, cy, x0 + 104, y0 + 98), "lbad w2"),
                ar(Lx + 10, cy + 20, x0 + 90, y0 + 106, "lbad w2", "ah-bad"),
                t(x0 + 116, y0 + 116, "ARAS ✕", "xs tbad b")]
    elif mode == "bilat":
        out += [t(Lx, cy + 4, "สารพิษ", "xs mid"), t(Rx, cy + 4, "เมแทบอลิก", "xs mid")]
    elif mode == "pf":
        out += [t(x0 + 116, y0 + 116, "ARAS ✕", "xs tbad b"), t(x0 + 116, y0 + 134, "pons", "xs tbad")]
    else:
        out += [circ(Lx - 14, cy + 2, 13, "bad"), t(x0 + 116, y0 + 118, "ARAS ✓", "xs tok b")]
    tc = "tbad" if coma else "tok"
    out += [t(x0 + 100, y0 + 166, l1, "sm mid b " + tc), t(x0 + 100, y0 + 182, l2, "xs mid i2")]
    return out


def acs_3lesion():
    return fig("รอยโรคแบบไหนทำให้โคม่า",
               "① ก้อนซีกเดียวทำให้โคม่าได้ก็ต่อเมื่อ **บวมจนดันข้ามเส้นกลางและกดก้านสมอง** (herniation) — มีอาการเฉพาะที่นำมาก่อน · ② ภาวะเมแทบอลิก สารพิษ ขาดออกซิเจน ชัก ทำให้ **เปลือกสมองทั้งสองซีกทำงานลดลงพร้อมกัน** จึงไม่มีอาการเฉพาะที่ และรูม่านตายังตอบสนอง · ③ รอยโรคใน posterior fossa **ทำลาย ARAS โดยตรง** ซึมเร็วพร้อมความผิดปกติของก้านสมอง · ④ รอยโรคซีกเดียวที่ไม่มี mass effect ไม่ทำให้โคม่า เพราะ **อีกซีกและ ARAS ยังทำงาน**",
               svg(420, 404, "สี่แบบของรอยโรค ก้อนซีกเดียวที่ดันกดก้านสมอง ความผิดปกติสองซีก รอยโรคที่ก้านสมอง ทำให้โคม่า ส่วนรอยโรคซีกเดียวไม่มี mass effect ไม่ทำให้โคม่า",
                   *_coronal(10, 6, "mass", "① ซีกเดียว + mass effect", "โคม่า: focal นำ แล้วซึม", "รีบ CT · ผ่าตัดช่วยได้", True),
                   *_coronal(210, 6, "bilat", "② สมองทั้งสองซีก", "โคม่า: ค่อย ๆ ซึม", "ไม่มี focal · รูม่านตาตอบสนอง", True),
                   *_coronal(10, 206, "pf", "③ Posterior fossa", "โคม่าเร็ว", "รูม่านตา การกลอกตาผิดตั้งแต่แรก", True),
                   *_coronal(210, 206, "uni", "④ ซีกเดียว ไม่มี mass effect", "ไม่โคม่า: ยังตื่น", "พูดไม่ได้ อ่อนแรงครึ่งซีก", False),
                   line(210, 10, 210, 394, "lru da"), line(10, 200, 410, 200, "lru da")))


# ---------------------------------------------------------------- 02
def acs_mimic():
    rows = [(10, 44, "ok", "ARAS + เปลือกสมอง\nตื่นและรู้ตัวดี ✓", None),
            (72, 44, "sk", "Ventral pons\ncorticospinal · bulbar", ("① Locked-in syndrome", "basilar occlusion · ARAS ด้านหลังรอด")),
            (134, 38, "sk", "เส้นประสาทส่วนปลาย", ("② GBS (AIDP)", "อ่อนแรงไต่ขึ้น · reflex หาย · ชา")),
            (190, 54, "sk", "Neuromuscular\njunction", None),
            (262, 40, "bad", "กล้ามเนื้อขยับไม่ได้\nดูเหมือนโคม่า", None)]
    out = []
    for k, (y, h, c, s, les) in enumerate(rows):
        out.append(box(10, y, 170, h, c, s, fs=11.5))
        if k < 4:
            ny = rows[k + 1][0]
            out.append(ar(95, y + h, 95, ny - 2, "ln", "ah"))
        if les:
            out += [line(180, y + h / 2, 194, y + h / 2, "lbad w2"), t(198, y + h / 2 - 2, les[0], "sm b tbad"),
                    t(198, y + h / 2 + 14, les[1], "xs i2")]
    out += [line(180, 217, 194, 217, "lbad w2"),
            t(198, 204, "③ Myasthenic crisis", "sm b tbad"), t(198, 218, "หนังตาตก · ล้าเมื่อใช้ ดีขึ้นเมื่อพัก", "xs i2"),
            t(198, 238, "④ ยาหย่อนกล้ามเนื้อ", "sm b tbad"), t(198, 252, "ตื่นเต็มที่แต่ขยับไม่ได้", "xs i2"),
            line(10, 318, 410, 318, "lru da"),
            t(10, 340, "ภาคตัดขวาง pons ใน locked-in", "sm b"),
            ell(100, 384, 84, 40, "sk"), ell(100, 362, 52, 15, "ok"), t(100, 366, "ARAS", "xs mid b tok"),
            ell(100, 400, 66, 18, "bad"), t(100, 404, "basis pontis", "xs mid b tbad"),
            t(196, 364, "ด้านหลัง: ARAS ยังดี → รู้ตัวเต็มที่", "sm tok"),
            t(196, 402, "ด้านหน้า: ทางสั่งการขาด → อัมพาต", "sm tbad"),
            t(196, 420, "มองขึ้นลง กะพริบได้ (ศูนย์อยู่ที่ midbrain)", "xs i2")]
    return fig("ภาวะที่เลียนแบบโคม่า: ทางออกถูกตัด",
               "ทั้งสี่ภาวะ **ARAS และเปลือกสมองยังทำงาน** ผู้ป่วยจึงรู้ตัวและได้ยินทุกอย่าง แต่คำสั่งจากสมองไปไม่ถึงกล้ามเนื้อ เพราะขาดที่จุดใดจุดหนึ่งตลอดทางออก — ventral pons · เส้นประสาท · NMJ ใน locked-in รอยโรคทำลาย **ด้านหน้าของ pons** ที่มีทางสั่งการ แต่ ARAS อยู่ **ด้านหลัง** และศูนย์มองขึ้นลงอยู่ที่ midbrain ซึ่งรอดทั้งคู่",
               svg(420, 432, "สัญญาณสั่งการจากสมองผ่าน ventral pons เส้นประสาท และ NMJ ไปยังกล้ามเนื้อ ถ้าถูกตัดที่จุดใดผู้ป่วยจะรู้ตัวแต่ขยับไม่ได้",
                   *out))


# ---------------------------------------------------------------- 03
def acs_motorm():
    rows = [("M6", "Obeys commands", "เปลือกสมองเข้าใจและสั่งการได้"),
            ("M5", "Localizes", "รับรู้ตำแหน่ง มือข้ามเส้นกลางมาปัด"),
            ("M4", "Withdraws", "ดึงหนีแบบรีเฟล็กซ์ ไม่ตั้งเป้า"),
            ("M3", "Decorticate", "รอยโรคเหนือ red nucleus"),
            ("M2", "Decerebrate", "รอยโรค midbrain–pons ต่ำกว่า red nucleus"),
            ("M1", "None", "pons ล่าง / medulla · หรือยากดลึก")]
    lv = [(20, 82, "ok", "ไม่มี\nรอยโรค"), (108, 38, "sk", "เปลือกสมอง\nเสียบางส่วน"),
          (152, 38, "ms", "capsule /\nthalamus"), (196, 38, "ms", "midbrain\npons บน"), (240, 38, "bad", "pons ล่าง\nmedulla")]
    out = [t(55, 12, "รอยโรคอยู่ที่", "xs mid b")]
    for y, h, c, s in lv:
        out.append(box(10, y, 90, h, c, s, fs=11))
    for k, (m, en, th) in enumerate(rows):
        y = 20 + 44 * k
        c = "ok" if k < 2 else ("sk" if k == 2 else ("ms" if k < 5 else "bad"))
        out += [pill(124, y + 8, m, c, "sm b mid", w=40), t(174, y + 16, en, "sm b"), t(174, y + 32, th, "xs i2")]
    out += [ar(112, 22, 112, 274, "lbad w2", "ah-bad"),
            t(10, 300, "รอยโรคยิ่งลงต่ำ คะแนน M ยิ่งน้อย", "sm b tbad"),
            t(10, 316, "M ที่ลดลงระหว่างการตรวจสองครั้ง = กำลังทรุด (rostro-caudal)", "xs i2")]
    return fig("คะแนน M ของ GCS บอกระดับของรอยโรค",
               "การตอบสนองทางการเคลื่อนไหวคือ **ภาพสะท้อนว่าระบบประสาทยังทำงานลงไปถึงระดับไหน** — M6/M5 ต้องใช้เปลือกสมอง · M3 (decorticate) บอกว่าเสียเหนือ red nucleus · M2 (decerebrate) บอกว่าเสียลงถึง midbrain–pons · M1 อาจเป็นรอยโรคต่ำมาก หรือแค่ยากดลึก/โรคของเส้นประสาทส่วนปลายก็ได้ จึงต้องดู **ความไม่สมมาตรและการเปลี่ยนแปลง** มากกว่าตัวเลขเดี่ยว",
               svg(420, 326, "คะแนน M จาก 6 ถึง 1 สอดคล้องกับระดับรอยโรคจากเปลือกสมองลงไปถึง medulla", *out))


# ---------------------------------------------------------------- 04
def acs_gcsfour():
    levels = ["เปลือกสมอง", "diencephalon · midbrain", "pons", "medulla"]
    gcs = {"E": [1], "V": [0], "M": [0, 1, 2]}
    four = {"E": [0, 1], "M": [0, 1, 2], "B": [1, 2, 3], "R": [1, 2, 3]}
    out = [t(212, 16, "GCS", "sm b mid"), t(340, 16, "FOUR", "sm b mid tok"),
           line(272, 8, 272, 160, "lru da")]
    for k, lv in enumerate(levels):
        y = 52 + 28 * k
        out += [t(10, y + 4, lv, "sm"), line(10, y + 14, 410, y + 14, "lru")]
    for j, comp in enumerate("EVM"):
        x = 186 + 26 * j
        out.append(t(x, 38, comp, "sm b mid"))
        for k in gcs[comp]:
            out.append(circ(x, 52 + 28 * k, 6, "inkf"))
    out += [t(212, 52 + 28 * 3 + 4, "มองไม่เห็นเลย", "xs mid tbad b"), t(212, 172, "V ใส่ท่อ = 1T", "xs mid tbad")]
    for j, comp in enumerate("EMBR"):
        x = 300 + 27 * j
        out.append(t(x, 38, comp, "sm b mid tok"))
        for k in four[comp]:
            out.append(circ(x, 52 + 28 * k, 6, "okf"))
    X = lambda d: 90 + (d - 1) * 110
    Y = lambda v: 334 - 7.5 * v
    out += [t(10, 206, "Floor effect — ผู้ป่วยที่แย่ที่สุด 3 วัน", "sm b"),
            line(70, Y(0), 380, Y(0), "lmu"), line(70, Y(0), 70, Y(16), "lmu"),
            *[p for v in (0, 4, 8, 12, 16) for p in (t(64, Y(v) + 4, str(v), "xs end mu"),)],
            t(X(1), Y(0) + 16, "วันที่ 1", "xs mid mu"), t(X(3), Y(0) + 16, "วันที่ 3", "xs mid mu"),
            poly([(X(1), Y(3)), (X(3), Y(3))], "lbad w3"), circ(X(1), Y(3), 4, "badf"), circ(X(3), Y(3), 4, "badf"),
            poly([(X(1), Y(4)), (X(3), Y(9))], "lok w3"), circ(X(1), Y(4), 4, "okf"), circ(X(3), Y(9), 4, "okf"),
            t(X(3) + 10, Y(3) + 4, "GCS 3 → 3", "sm b tbad"), t(X(3) + 10, Y(9) + 4, "FOUR 4 → 9", "sm b tok"),
            t(X(2), Y(12), "รีเฟล็กซ์ก้านสมองกลับมา", "xs mid i2"), t(X(2), Y(12) + 14, "GCS มองไม่เห็น", "xs mid i2")]
    return fig("GCS กับ FOUR มองระบบประสาทได้ลึกแค่ไหน",
               "แต่ละองค์ประกอบของคะแนน **สุ่มตรวจระดับของระบบประสาทคนละชั้น** — GCS ใช้การพูดที่หายไปทันทีเมื่อใส่ท่อ และ **ไม่มีส่วนใดตรวจ pons ล่างหรือ medulla เลย** ส่วน FOUR เพิ่มรีเฟล็กซ์ก้านสมอง (B) และรูปแบบการหายใจ (R) ที่ไล่ลงไปถึง medulla ผู้ป่วยที่ GCS ติดพื้นที่ 3 จึงยังแยกความเปลี่ยนแปลงได้ด้วย FOUR",
               svg(420, 356, "ตารางระดับระบบประสาทที่ GCS และ FOUR ตรวจ GCS ไม่ครอบคลุม medulla และกราฟที่ GCS ติดที่ 3 ขณะที่ FOUR เพิ่มจาก 4 เป็น 9",
                   *out))


# ---------------------------------------------------------------- 05
def acs_secondary():
    X = lambda m: 60 + m * 1.7
    Y = lambda f: 176 - f * 1.9
    def norm(m):
        if m < 60: return 50 * m / 60
        if m <= 150: return 50
        return 50 + (m - 150) * 0.7
    ms_ = list(range(0, 201, 5))
    out = [line(X(0), Y(0), X(200), Y(0), "lmu"), line(X(0), Y(0), X(0), Y(78), "lmu"),
           t(X(0) - 6, Y(72), "เลือด", "xs end mu"), t(X(0) - 6, Y(72) + 13, "ไปสมอง", "xs end mu"),
           *[p for m in (0, 50, 100, 150, 200) for p in (line(X(m), Y(0), X(m), Y(0) + 4, "lmu"), t(X(m), Y(0) + 16, str(m), "xs mid mu"))],
           t(X(200), Y(0) + 30, "MAP (มม.ปรอท)", "xs end mu"),
           rect(X(0), Y(78), X(65) - X(0), Y(0) - Y(78), "bad", 0),
           t(X(32), Y(70), "BP ต่ำ", "xs mid b tbad"),
           line(X(65), Y(0), X(65), Y(78), "lbad da"), t(X(65) + 4, Y(74), "MAP 65", "xs tbad b"),
           poly([(X(m), Y(norm(m))) for m in ms_ if m <= 190], "lok w3"),
           poly([(X(m), Y(m * 50 / 90.0)) for m in ms_ if m <= 140], "lbad w3"),
           line(10, 226, 32, 226, "lok w3"), t(38, 230, "สมองปกติ: เลือดไหลคงที่", "xs b tok"),
           line(210, 226, 232, 226, "lbad w3"), t(238, 230, "สมองบาดเจ็บ: ไหลตามความดัน", "xs b tbad"),
           t(X(65) + 6, Y(20) + 18, "BP ตกนิดเดียว → ขาดเลือด", "xs tbad")]
    pillars = [("wa", "Oxygen: SpO₂ 94–98%\nขาด → ATP ↓ · เกิน → อนุมูลอิสระ"),
               ("bad", "Perfusion: MAP ≥ 65\nไม่มี autoregulation คุ้มกัน"),
               ("ms", "Glucose ปกติ\nต่ำ = ไม่มีเชื้อเพลิง · สูง = lactate ↑"),
               ("ok", "อุณหภูมิปกติ\nไข้ → สมองใช้พลังงานและ O₂ มากขึ้น")]
    for k, (c, s) in enumerate(pillars):
        out.append(box(10 + 204 * (k % 2), 242 + 58 * (k // 2), 196, 50, c, s, fs=10.5))
    return fig("สมองที่บาดเจ็บเสีย autoregulation",
               "สมองปกติปรับขนาดหลอดเลือดเองให้ **เลือดไหลคงที่** แม้ความดันขึ้นลงในช่วงกว้าง สมองที่บาดเจ็บเสียกลไกนี้ เลือดที่ไปเลี้ยงจึง **ขึ้นลงตามความดันโดยตรง** — ความดันต่ำเพียงช่วงสั้นก็ทำให้เนื้อสมองรอบรอยโรคที่กำลังจะตายขาดเลือดซ้ำ นี่คือ **secondary brain injury** ที่สี่เสา (ออกซิเจน ความดัน น้ำตาล อุณหภูมิ) มีไว้ป้องกัน",
               svg(420, 356, "กราฟเลือดไปสมองเทียบความดัน สมองปกติคงที่ สมองบาดเจ็บไหลตามความดัน และสี่เสาป้องกันการบาดเจ็บซ้ำ",
                   *out))


def acs_thiamine():
    return fig("ทำไมต้องให้ thiamine ก่อนหรือพร้อมกลูโคส",
               "thiamine เป็น coenzyme ของ **pyruvate dehydrogenase (PDH)** ที่พากลูโคสเข้าสู่ Krebs cycle ผู้ดื่มสุราหรือขาดอาหารมี thiamine เหลือน้อย ถ้าให้กลูโคสก้อนใหญ่ **pyruvate จะคั่งและกลายเป็น lactate** ATP ไม่พอ เซลล์ที่ใช้พลังงานสูง — **mammillary body · thalamus ด้านใน · รอบ aqueduct** — ตายก่อน เกิด **Wernicke encephalopathy** (สับสน ตากลอกผิดปกติ เดินเซ)",
               svg(420, 312, "กลูโคสเปลี่ยนเป็น pyruvate แล้วต้องใช้ thiamine ผ่าน PDH เพื่อสร้างพลังงาน ถ้าขาด thiamine pyruvate กลายเป็น lactate เซลล์สมองบางส่วนตาย เกิด Wernicke",
                   t(80, 16, "มี thiamine", "sm b mid tok"), t(310, 16, "ขาด thiamine", "sm b mid tbad"),
                   box(20, 26, 120, 34, "sk", "กลูโคส", "b"), ar(80, 60, 80, 78, "ln", "ah"),
                   box(20, 80, 120, 34, "sk", "pyruvate", "b"),
                   ar(80, 114, 80, 150, "lok w3", "ah-ok"), t(96, 132, "PDH", "xs b tok"), t(96, 144, "ใช้ thiamine", "xs tok"),
                   box(20, 152, 120, 40, "ok", "acetyl-CoA\n→ Krebs cycle", fs=11.5), ar(80, 192, 80, 210, "ln", "ah"),
                   box(20, 212, 120, 34, "ok", "ATP พอ", "b"),
                   ar(140, 97, 210, 97, "lbad w2", "ah-bad"), t(176, 90, "ทางตัน", "xs mid tbad b"),
                   box(212, 76, 198, 42, "bad", "pyruvate → lactate ↑\nATP ↓", fs=11.5), ar(310, 118, 310, 136, "ln", "ah"),
                   box(212, 138, 198, 56, "bad", "เซลล์ที่ใช้พลังงานสูงตาย\nmammillary · thalamus ใน\nรอบ aqueduct", fs=11), ar(310, 194, 310, 212, "ln", "ah"),
                   box(212, 214, 198, 46, "bad", "Wernicke: สับสน\nตากลอกผิดปกติ · เดินเซ", fs=11.5),
                   t(10, 284, "กลูโคสก้อนใหญ่ = ดันน้ำตาลเข้าทางตันมากขึ้น ใช้ thiamine ที่เหลือหมด", "xs i2"),
                   t(10, 302, "→ ให้ thiamine ก่อนหรือพร้อมกลูโคสเสมอในผู้ที่เสี่ยง", "sm b tok")))


# ---------------------------------------------------------------- 06
def acs_pupils():
    rows = [(40, "diencephalon\n(hypothalamus)", 2.6, 2.6, "เล็ก แต่ตอบสนอง", "sympathetic ลดบางส่วน · เมแทบอลิก"),
            (100, "midbrain\nEW nucleus", 5.5, 5.5, "กลาง 4–6 มม. คงที่", "เสียทั้งฝั่งหดและทาง sympathetic"),
            (160, "pons", 1.3, 1.3, "เท่าหัวเข็มหมุด", "sympathetic ขาด เหลือแต่หด · opioid"),
            (230, None, 8.5, 3.0, "ข้างเดียวขยาย ไม่ตอบสนอง", "uncus กด CN III · ใยหดอยู่ผิวนอก"),
            (290, None, 8.5, 8.5, "ขยายสองข้าง คงที่", "ขาด O₂ รุนแรง · anticholinergic")]
    out = [t(10, 14, "sympathetic: ลงจาก hypothalamus → ขยาย", "xs b tbad"),
           t(10, 28, "parasympathetic: EW (midbrain) → CN III → หด", "xs b tok"),
           path("M114 46 V206", "lbad da w2", "ah-bad"), line(10, 220, 410, 220, "lru da")]
    for y, lv, rl, rr, a, b in rows:
        if lv:
            out.append(box(16, y, 90, 52, "sk", lv, fs=11))
        out += _eyes(170, y + 26, rl, rr)
        out += [t(220, y + 22, a, "sm b"), t(220, y + 38, b, "xs i2")]
    out += [line(16, 266, 104, 266, "ln w3"), t(60, 282, "CN III", "xs mid"),
            ell(56, 240, 22, 11, "bad"), t(56, 244, "uncus", "xs mid b"), ar(56, 252, 56, 263, "lbad w2", "ah-bad"),
            box(16, 296, 90, 40, "sk", "ก้านสมองเสีย\nกว้าง / ยา", fs=11),
            ]
    return fig("รูม่านตาบอกระดับของรอยโรค",
               "รูม่านตาเป็นผลรวมของสองระบบ — **sympathetic** (ขยาย) ลงมาจาก hypothalamus ผ่านทั้งก้านสมอง และ **parasympathetic** (หด) ออกจาก midbrain ไปกับ CN III รอยโรคตัดระบบไหนได้ขนาดตามนั้น: diencephalon = เล็กแต่ตอบสนอง · midbrain = กลางและคงที่ · pons = pinpoint ส่วน **CN III ที่ถูก uncus กด** เสียใยหดที่อยู่ผิวนอกก่อน จึงขยายข้างเดียว เพราะวงจรนี้ทนต่อภาวะเมแทบอลิกสูง รูม่านตาที่ผิดปกติจึงมักหมายถึงรอยโรคโครงสร้าง",
               svg(420, 348, "ระดับรอยโรคในก้านสมองกับขนาดรูม่านตา diencephalon เล็ก midbrain กลางคงที่ pons เท่าหัวเข็มหมุด CN III ถูกกดขยายข้างเดียว",
                   *out))


def acs_reflexarc():
    rows = [(20, "midbrain", "แสงเข้าตา", "CN II", "CN III", "รูม่านตาหด"),
            (92, "pons", "แตะกระจกตา", "CN V₁", "CN VII", "กะพริบตา"),
            (164, "medulla", "ดูดเสมหะลึก", "CN IX", "CN X", "ไอ / ขย้อน")]
    out = []
    for k, (y, lv, s_in, n_in, n_out, s_out) in enumerate(rows):
        c = "sk"
        out += [rect(170, y, 80, 64, c, 8), t(210, y + 14, lv, "xs mid b"),
                t(10, y + 30, s_in, "sm b"), t(10, y + 46, n_in + " (รับ)", "xs i2"),
                ar(104, y + 38, 168, y + 38, "lwa w2", "ah-wa"),
                path("M172 %d Q210 %d 248 %d" % (y + 38, y + 62, y + 38), "lac w2"),
                ar(252, y + 38, 312, y + 38, "lok w2", "ah-ok"),
                t(318, y + 30, s_out, "sm b"), t(318, y + 46, n_out + " (สั่ง)", "xs i2")]
    out += [t(210, 252, "หายไล่จากบนลงล่าง = ก้านสมองเสียไล่ลงมา", "sm mid b tbad"),
            t(210, 270, "เป็นแกนของ B ใน FOUR score (B4 → B0)", "xs mid i2")]
    return fig("สามรีเฟล็กซ์ = สามชั้นของก้านสมอง",
               "รีเฟล็กซ์แต่ละอันมี **ทางรับและทางสั่งที่มาพบกันในก้านสมองคนละชั้น** — รูม่านตา (II → III) ที่ midbrain · กระจกตา (V₁ → VII) ที่ pons · ไอและขย้อน (IX → X) ที่ medulla เมื่อตรวจครบทั้งสามจึงบอกได้ว่าก้านสมองยังทำงานลงไปถึงชั้นไหน ซึ่งเป็นข้อมูลที่ GCS ไม่มี",
               svg(420, 282, "รีเฟล็กซ์รูม่านตาที่ midbrain รีเฟล็กซ์กระจกตาที่ pons รีเฟล็กซ์ไอและขย้อนที่ medulla", *out))


# ---------------------------------------------------------------- 07
def _gazepanel(x0, mode):
    Lx, Rx = x0 + 48, x0 + 92
    out = [ell(Lx, 60, 24, 34, "bx"), ell(Rx, 60, 24, 34, "bx"), rect(x0 + 60, 96, 20, 22, "sk", 6),
           circ(Lx, 36, 4, "acf"), circ(Rx, 36, 4, "acf")]
    if mode == "lesion":
        out += [ell(Rx, 62, 20, 28, "bad"), circ(Rx, 36, 4, "acf"),
                ar(Lx + 4, 42, Lx + 30, 48, "lac w2", "ah-ac")]
        look, l1, l2, l3 = 1, "รอยโรคซีกขวา", "ตามองเข้าหารอยโรค", "(หนีข้างอ่อนแรง)"
    elif mode == "seizure":
        out += [poly([(Rx - 10, 30), (Rx - 2, 38), (Rx - 8, 44), (Rx + 4, 50)], "lms w3"),
                ar(Rx - 4, 42, Rx - 30, 48, "lms w2", "ah-ms")]
        look, l1, l2, l3 = -1, "ชักจากซีกขวา", "ตามองหนีจุดชัก", ""
    else:
        out += [rect(x0 + 70, 96, 10, 22, "bad", 3)]
        look, l1, l2, l3 = -1, "รอยโรค pons ขวา", "ตามองไปข้างอ่อนแรง", "(มองขวาไม่ได้)"
    out += [ell(x0 + 52, 146, 13, 8, "bx"), circ(x0 + 52 + 6 * look, 146, 3.4, "inkf"),
            ell(x0 + 88, 146, 13, 8, "bx"), circ(x0 + 88 + 6 * look, 146, 3.4, "inkf"),
            ar(x0 + 70 - 12 * look, 166, x0 + 70 + 14 * look, 166, "ln w2", "ah"),
            t(x0 + 70, 190, l1, "sm b mid"), t(x0 + 70, 206, l2, "xs mid tac b"), t(x0 + 70, 220, l3, "xs mid i2")]
    return out


def acs_gaze():
    return fig("ตาเบนไปทางไหน บอกตำแหน่งรอยโรค",
               "frontal eye field (จุดสีม่วง) ของแต่ละซีก **ดันตาไปฝั่งตรงข้าม** ตาจึงอยู่ตรงกลางได้เพราะแรงสองข้างหักล้างกัน — ซีกขวาเสีย ซีกซ้ายดันตาไปทางขวาโดยไม่มีแรงต้าน ตาจึง **มองเข้าหารอยโรค** · ซีกขวาชัก frontal eye field ขวาทำงานเกิน ตาจึง **มองหนีจุดชัก** · ที่ pons ศูนย์มองด้านข้าง (PPRF) ดันตาไปข้างเดียวกัน รอยโรค pons ขวาจึงทำให้ **มองขวาไม่ได้ ตาเบนไปซ้ายซึ่งเป็นข้างที่อ่อนแรง**",
               svg(420, 230, "สามสถานการณ์ รอยโรคซีกขวาตามองขวา ชักจากซีกขวาตามองซ้าย รอยโรคที่ pons ขวาตามองซ้าย มองจากด้านบน",
                   *_gazepanel(0, "lesion"), *_gazepanel(140, "seizure"), *_gazepanel(280, "pons"),
                   line(140, 10, 140, 224, "lru da"), line(280, 10, 280, 224, "lru da"),
                   t(4, 14, "มองจากด้านบน", "xs mu")))


def _head(cx, cy, face, gaze, r=26, ray=0):
    s = lambda a: math.sin(math.radians(a))
    c = lambda a: math.cos(math.radians(a))
    out = [ell(cx + (r + 1) * s(face + 90), cy - (r + 1) * c(face + 90), 5, 9, "sk", face),
           ell(cx + (r + 1) * s(face - 90), cy - (r + 1) * c(face - 90), 5, 9, "sk", face),
           circ(cx, cy, r, "bx"),
           poly([(cx + (r + 9) * s(face), cy - (r + 9) * c(face)), (cx + (r - 1) * s(face - 15), cy - (r - 1) * c(face - 15)),
                 (cx + (r - 1) * s(face + 15), cy - (r - 1) * c(face + 15))], "bx", True)]
    for sd in (-1, 1):
        a = face + sd * 34
        ex, ey = cx + (r - 9) * s(a), cy - (r - 9) * c(a)
        px, py = ex + 3.6 * s(gaze), ey - 3.6 * c(gaze)
        if ray:
            out.append(line(px, py, px + ray * s(gaze), py - ray * c(gaze), "lmu da"))
        out += [circ(ex, ey, 7, "paf"), circ(ex, ey, 7, "ln"), circ(px, py, 3, "inkf")]
    return out


def acs_vor():
    out = [t(10, 18, "Doll's eye — หันศีรษะไปทางขวาอย่างเร็ว", "sm b"),
           *_head(110, 92, 35, 0, ray=30), *_head(310, 92, 35, 35, ray=30),
           path("M60 70 Q66 52 84 46", "lmu w2", "ah-mu"), path("M260 70 Q266 52 284 46", "lmu w2", "ah-mu"),
           t(110, 140, "ตายังมองที่เดิมในห้อง", "sm mid"), t(110, 156, "ก้านสมองดี ✓", "sm mid b tok"),
           t(310, 140, "ตาหมุนไปพร้อมหัว", "sm mid"), t(310, 156, "ก้านสมองเสีย / ยากดลึก", "sm mid b tbad"),
           line(10, 168, 410, 168, "lru da"),
           t(10, 188, "Cold caloric — หยอดน้ำเย็นหูขวา", "sm b")]
    cy = 254
    for k, (cx, gz, a, b, tc) in enumerate(((72, 0, "รู้สึกตัว", "ช้า → หูเย็น · เร็ว ← กลับ", "i2"),
                                          (210, 70, "โคม่า ก้านสมองดี", "เบนช้ามาหูเย็นแล้วค้าง", "tok"),
                                          (348, 0, "ก้านสมองเสีย / ยา", "ไม่ขยับเลย", "tbad"))):
        out += _head(cx, cy, 0, gz, ray=18 if k == 1 else 0)
        out += [circ(cx + 40, cy - 6, 3, "waf"), circ(cx + 44, cy + 3, 3, "waf"), circ(cx + 38, cy + 10, 3, "waf")]
        out += [t(cx, cy + 46, a, "sm mid b " + tc), t(cx, cy + 62, b, "xs mid i2")]
    out += [ar(58, 200, 86, 200, "lmu w2", "ah-mu"), t(92, 204, "ช้า", "xs i2"),
            ar(86, 212, 58, 212, "lac w3", "ah-ac"), t(92, 216, "เร็ว", "xs tac b"),
            t(348, 210, "✕", "b mid tbad"),
            t(118, 276, "น้ำเย็น", "xs twa")]
    chain = [("wa", "น้ำเย็นหูขวา\nendolymph ไหล"), ("sk", "ประสาททรงตัวขวา\nส่งสัญญาณลดลง"),
             ("ok", "ก้านสมองดันตา\nไปทางขวา (ช้า)"), ("ac", "เปลือกสมองดีด\nกลับซ้าย (เร็ว)")]
    for k, (c, s_) in enumerate(chain):
        x = 10 + 102 * k
        out.append(box(x, 334, 96, 44, c, s_, fs=10.5))
        if k < 3: out.append(line(x + 96, 356, x + 102, 356, "ln", "ah"))
    return fig("Doll's eye และ cold caloric ตรวจทางเดินเดียวกัน",
               "ทั้งสองวิธีทดสอบ **vestibulo-ocular reflex** ที่วิ่งจากหูชั้นใน → vestibular nuclei (medulla) → MLF → นิวเคลียส CN VI และ III (pons–midbrain) ตาที่ยังมองที่เดิมขณะหันหัว หรือเบนมาทางหูที่หยอดน้ำเย็น จึงยืนยันว่า **ก้านสมองต่อกันครบตั้งแต่ medulla ถึง midbrain** ส่วน fast phase ต้องใช้เปลือกสมอง ผู้ป่วยโคม่าจึงมีแต่ slow phase (COWS พูดถึงทิศของ fast phase) · ภาพมองจากด้านบน จมูกชี้ขึ้น เส้นประคือทิศที่ตามอง",
               svg(420, 386, "doll's eye ปกติตามองที่เดิมเมื่อหันหัว ถ้าก้านสมองเสียตาหมุนตามหัว และ cold caloric ในคนรู้สึกตัวเกิด nystagmus ในโคม่าที่ก้านสมองดีตาเบนมาทางหูเย็น ถ้าก้านสมองเสียไม่ขยับ",
                   *out))


# ---------------------------------------------------------------- 08
def _stick(cx, mode):
    out = [circ(cx, 48, 11, "bx"), line(cx, 59, cx, 128, "ln w3"), line(cx - 12, 70, cx + 12, 70, "ln w3"),
           line(cx - 8, 128, cx + 8, 128, "ln w3"),
           poly([(cx - 8, 128), (cx - 10, 190), (cx - 12, 204)], "ln w3"),
           poly([(cx + 8, 128), (cx + 10, 190), (cx + 12, 204)], "ln w3")]
    for sd in (-1, 1):
        if mode == "dc":
            out.append(poly([(cx + 12 * sd, 70), (cx + 17 * sd, 102), (cx + 5 * sd, 84), (cx - 1 * sd, 92)], "lms w3"))
        else:
            out.append(poly([(cx + 12 * sd, 70), (cx + 18 * sd, 104), (cx + 22 * sd, 138), (cx + 15 * sd, 146)], "lbad w3"))
    return out


def acs_posture():
    out = [box(26, 16, 124, 34, "ac", "เปลือกสมอง", fs=12),
           box(26, 58, 124, 40, "sk", "internal capsule\n· thalamus", fs=11),
           line(8, 106, 158, 106, "lms da w2"), pill(4, 96, "A", "ms", "sm b mid tms", w=20, h=20),
           box(26, 114, 124, 40, "sk", "midbrain\n● red nucleus", fs=11),
           line(8, 162, 158, 162, "lbad da w2"), pill(4, 152, "B", "bad", "sm b mid tbad", w=20, h=20),
           box(26, 170, 124, 44, "sk", "pons · medulla\n● vestibular · reticular", fs=10.5),
           t(26, 236, "rubrospinal → กระตุ้นงอแขน", "xs b tms"),
           t(26, 252, "vestibulo- / reticulospinal", "xs b twa"), t(26, 266, "→ กระตุ้นเหยียดแขนขา", "xs b twa"),
           t(240, 16, "A · Decorticate", "sm b mid tms"), t(356, 16, "B · Decerebrate", "sm b mid tbad"),
           *_stick(240, "dc"), *_stick(356, "dr"),
           line(298, 30, 298, 270, "lru da"),
           t(240, 224, "เหลือ rubrospinal", "xs mid"), t(240, 238, "→ แขนงอเข้าแกนกลาง", "xs mid b"),
           t(240, 258, "GCS M3 · FOUR M2", "xs mid i2"),
           t(356, 224, "เหลือแต่ทางเหยียด", "xs mid"), t(356, 238, "→ เหยียด แขนบิดเข้าใน", "xs mid b"),
           t(356, 258, "GCS M2 · FOUR M1", "xs mid i2")]
    return fig("Decorticate vs decerebrate: เส้นตัดอยู่ที่ red nucleus",
               "เมื่อเปลือกสมองที่คอยยับยั้งหายไป ท่าจะถูกกำหนดโดยทางเดินจากก้านสมองที่ **ยังเหลืออยู่** — รอยโรค **A (เหนือ red nucleus)** ยังมี rubrospinal ที่กระตุ้นกล้ามเนื้องอแขน จึง **งอแขน เหยียดขา** · รอยโรค **B (ต่ำกว่า red nucleus)** เสีย rubrospinal เหลือแต่ vestibulospinal/reticulospinal ที่กระตุ้นกล้ามเนื้อเหยียด จึง **เหยียดทั้งแขนและขา** การเปลี่ยนจาก A เป็น B จึงแปลว่ารอยโรคลามลงต่ำ",
               svg(420, 278, "รอยโรคเหนือ red nucleus ทำให้ท่า decorticate แขนงอ รอยโรคต่ำกว่า red nucleus ทำให้ท่า decerebrate เหยียดทั้งตัว",
                   *out))


def acs_rostro():
    W, X0 = 160, 106
    def trace(kind, y):
        pts = []
        for i in range(W + 1):
            tt = i / float(W)
            if kind == "cs":
                ph = (tt % 0.5) / 0.5
                env = math.sin(math.pi * ph / 0.7) if ph < 0.7 else 0
                v = env * math.sin(2 * math.pi * tt * 16)
            elif kind == "cnh":
                v = 0.8 * math.sin(2 * math.pi * tt * 14)
            elif kind == "ap":
                ph = (tt % 0.25) / 0.25
                v = ph / 0.15 if ph < 0.15 else (1 if ph < 0.55 else (1 - (ph - 0.55) / 0.15 if ph < 0.7 else 0))
                v = v * 0.9
            else:
                v = 0
                for s0, d, a in ((0.02, 0.07, 0.5), (0.14, 0.05, 0.9), (0.3, 0.1, 0.3), (0.5, 0.06, 0.7), (0.6, 0.04, 0.4)):
                    if s0 <= tt <= s0 + d: v = a * math.sin(math.pi * (tt - s0) / d)
            pts.append((X0 + i, y - 18 * v))
        return poly(pts, "lwa w2")
    rows = [("ms", "Diencephalon\nCheyne-Stokes", "cs", 2.4, "Decorticate"),
            ("ms", "Midbrain\nCNH", "cnh", 5.2, "Decerebrate"),
            ("bad", "Pons\nApneustic", "ap", 1.2, "Decerebrate\n/ flaccid"),
            ("bad", "Medulla\nAtaxic → apnea", "at", 7.5, "Flaccid")]
    out = [t(53, 20, "ระดับ · การหายใจ", "xs mid b"), t(186, 20, "รูปแบบการหายใจ", "xs mid b"),
           t(310, 20, "รูม่านตา", "xs mid b"), t(378, 20, "ท่า", "xs mid b")]
    for k, (c, lv, kind, pr, post) in enumerate(rows):
        y = 30 + 68 * k
        out += [box(10, y, 90, 56, c, lv, fs=10.5), line(X0, y + 28, X0 + W, y + 28, "lru"), trace(kind, y + 28),
                ell(292, y + 28, 12, 8, "bx"), circ(292, y + 28, pr, "inkf"),
                ell(326, y + 28, 12, 8, "bx"), circ(326, y + 28, pr, "inkf"),
                t(378, y + 32 if "\n" not in post else y + 24, post, "xs mid b")]
        if k < 3:
            out.append(line(55, y + 56, 55, y + 66, "lbad w2", "ah-bad"))
    out += [t(10, 318, "เลื่อนลงทีละขั้น = rostro-caudal deterioration → ตรวจซ้ำและรายงานทันที", "xs b tbad")]
    return fig("ไล่ระดับรอยโรคจากบนลงล่าง",
               "เมื่อความดันกดก้านสมองไล่ลงมา ศูนย์ควบคุมแต่ละชั้นเสียตามลำดับ — **Cheyne-Stokes** (ศูนย์หายใจตอบสนอง CO₂ ช้าเกินจึงหายใจแรงสลับหยุด) → **central neurogenic hyperventilation** (หายใจเร็วลึกสม่ำเสมอ) → **apneustic** (หายใจเข้าแล้วค้าง) → **ataxic** ไม่เป็นจังหวะแล้วหยุดหายใจ รูม่านตาและท่าเปลี่ยนไปพร้อมกัน สิ่งที่มีค่าคือ **การเห็นผู้ป่วยเลื่อนลงบันได** ระหว่างการตรวจสองครั้ง",
               svg(420, 328, "การหายใจ รูม่านตา และท่า ที่ระดับ diencephalon midbrain pons และ medulla", *out))


# ---------------------------------------------------------------- 09
def acs_causes():
    return fig("หาสาเหตุโคม่าเป็นลำดับ",
               "หลังทำให้คงที่และแก้น้ำตาลแล้ว คำถามแรกคือ **มีหลักฐานของรอยโรคโครงสร้างไหม** — อาการเฉพาะที่ รูม่านตาไม่เท่ากัน หรือสัญญาณก้านสมอง ชี้ไปที่ก้อน เลือดออก หรือ stroke ที่ต้องทำ CT ทันที ส่วนโคม่าแบบสมมาตรที่รูม่านตายังตอบสนอง ชี้ไปที่ภาวะที่กดเปลือกสมองทั้งสองซีกพร้อมกัน ถ้าตรวจครบแล้วยังอธิบายไม่ได้ ให้นึกถึง **NCSE และ basilar occlusion** ซึ่ง CT ธรรมดามักปกติ",
               svg(420, 388, "แผนผังหาสาเหตุโคม่า ถ้ามีอาการเฉพาะที่ทำ CT หาเหตุโครงสร้าง ถ้าไม่มีหาเหตุเมแทบอลิก สารพิษ ติดเชื้อ ถ้ายังไม่พบคิดถึงการชักแบบไม่แสดงอาการและหลอดเลือด basilar อุดตัน",
                   box(80, 8, 260, 34, "ok", "ABC · น้ำตาลปลายนิ้ว · thiamine/naloxone", fs=11.5),
                   line(210, 42, 210, 58, "ln", "ah"),
                   box(70, 60, 280, 48, "ac", "มีอาการเฉพาะที่ · รูม่านตาไม่เท่า\nหรือสัญญาณก้านสมอง?", fs=12),
                   line(140, 108, 105, 132, "ln", "ah"), line(280, 108, 315, 132, "ln", "ah"),
                   t(112, 122, "มี", "sm b end"), t(308, 122, "ไม่มี · สมมาตร", "sm b"),
                   box(10, 134, 190, 64, "bad", "STRUCTURAL\nCT ไม่ฉีดสีทันที\nเลือดออก · ก้อน · stroke", fs=11.5),
                   box(220, 134, 190, 64, "ms", "METABOLIC · TOXIC · INFECTION\nเลือด · ABG · tox screen\nไข้/คอแข็ง → ยา แล้ว LP", fs=10.5),
                   line(105, 198, 160, 224, "ln", "ah"), line(315, 198, 260, 224, "ln", "ah"),
                   box(60, 226, 300, 40, "sk", "ตรวจครบแล้วยังอธิบายไม่ได้?", fs=12.5),
                   line(150, 266, 105, 290, "ln", "ah"), line(270, 266, 315, 290, "ln", "ah"),
                   box(10, 292, 190, 62, "bad", "Non-convulsive SE\nกระตุกเล็ก ๆ ที่ตา ปาก นิ้ว\n→ EEG", fs=11),
                   box(220, 292, 190, 62, "bad", "Basilar artery occlusion\nก้านสมองผิดปกติ\n→ CTA", fs=11),
                   t(210, 378, "ทั้งคู่ CT ธรรมดามักปกติ และรักษาได้ถ้าจับได้ทัน", "sm mid b tbad")))


# ---------------------------------------------------------------- 10
def acs_icp():
    def bar(x, fr, title, sub, tc):
        out, y = [], 170
        cols = [("ruf", "brain"), ("ms", "mass"), ("bad", "blood"), ("wa", "CSF")]
        for (c, _), f in zip(cols, fr):
            h = 140 * f
            if h > 0:
                y -= h
                out.append(rect(x, y, 66, h, c, 2))
        out += [rect(x - 4, 26, 74, 148, "lmu w3", 10), t(x + 33, 190, title, "sm mid b"), t(x + 33, 206, sub, "xs mid " + tc)]
        return out
    out = [t(10, 16, "กะโหลกมีปริมาตรคงที่ (Monro–Kellie)", "sm b"),
           *bar(18, (0.76, 0, 0.12, 0.12), "ปกติ", "ICP ปกติ", "i2"),
           *bar(122, (0.76, 0.14, 0.05, 0.05), "มีก้อน", "บีบ CSF/เลือดออก", "tok"),
           *bar(226, (0.76, 0.24, 0.0, 0.0), "เกินชดเชย", "ICP ↑↑ → herniation", "tbad"),
           ar(259, 22, 259, 8, "lbad w2", "ah-bad"),
           rect(318, 40, 14, 14, "ruf", 2), t(338, 52, "เนื้อสมอง", "xs"),
           rect(318, 64, 14, 14, "ms", 2), t(338, 76, "ก้อน/บวม", "xs"),
           rect(318, 88, 14, 14, "bad", 2), t(338, 100, "เลือด", "xs"),
           rect(318, 112, 14, 14, "wa", 2), t(338, 124, "CSF", "xs"),
           t(318, 156, "CPP = MAP − ICP", "sm b"), t(318, 172, "ICP ↑ → CPP ↓", "xs i2"), t(318, 186, "เลือดเข้าสมองลด", "xs i2"),
           line(10, 222, 410, 222, "lru da"), t(10, 242, "แต่ละมาตรการลดส่วนไหน", "sm b")]
    ms_ = [("ok", "ยกหัวเตียง 30° · ศีรษะตรง", "เลือดดำไหลออกง่าย → blood ↓", "bad"),
           ("ok", "ยาระงับปวด ยานอนหลับ", "ลดการเผาผลาญและการเบ่ง → blood ↓", "bad"),
           ("ms", "Hyperosmolar therapy", "ดึงน้ำออกจากเนื้อสมอง → brain ↓", "bx"),
           ("ms", "Hyperventilation ชั่วคราว", "CO₂ ↓ หลอดเลือดหด → blood ↓ (เสี่ยงขาดเลือด)", "bad"),
           ("bad", "ผ่าตัด / ระบาย CSF", "เอาก้อนหรือน้ำออก → mass / CSF ↓", "ms")]
    for k, (c, a, b, chip) in enumerate(ms_):
        y = 252 + 34 * k
        out += [rect(10, y, 12, 26, chip, 2), t(30, y + 12, a, "sm b"), t(30, y + 26, b, "xs i2")]
    return fig("Monro–Kellie: ปริมาตรคงที่ ต้องมีอะไรถูกบีบออก",
               "กะโหลกเป็นกล่องแข็ง เมื่อมีก้อนหรือสมองบวม ร่างกาย **ชดเชยโดยบีบ CSF และเลือดดำออก** ICP จึงยังปกติช่วงแรก เมื่อชดเชยหมด ปริมาตรเพิ่มเพียงเล็กน้อยก็ทำให้ ICP พุ่ง และ **CPP = MAP − ICP** ลดลงจนสมองขาดเลือด มาตรการลดความดันแต่ละอย่างจึงออกแบบมาเพื่อ **ลดส่วนใดส่วนหนึ่ง** ของกล่องนี้",
               svg(420, 422, "กะโหลกมีปริมาตรคงที่ ประกอบด้วยเนื้อสมอง เลือด และน้ำไขสันหลัง เมื่อมีก้อนต้องบีบส่วนอื่นออก เมื่อชดเชยไม่ได้ความดันในกะโหลกสูง และมาตรการลดความดันแต่ละอย่างลดส่วนใดส่วนหนึ่ง",
                   *out))


def acs_ods():
    def cell(cx, r, n, label, tc, shrunk=False):
        out = []
        if shrunk:
            pts = []
            for i in range(24):
                a = 2 * math.pi * i / 24
                rr = r + (3 if i % 2 else -2)
                pts.append((cx + rr * math.cos(a), 92 + rr * math.sin(a)))
            out.append(poly(pts, "bad", True))
        else:
            out.append(circ(cx, 92, r, "wa"))
        for i in range(n):
            a = 2 * math.pi * i / max(n, 1) + 0.4
            out.append(circ(cx + 0.5 * r * math.cos(a), 92 + 0.5 * r * math.sin(a), 2.6, "inkf"))
        out.append(t(cx, 160, label[0], "xs mid b " + tc))
        out.append(t(cx, 174, label[1], "xs mid i2"))
        return out
    out = [*cell(50, 26, 8, ("ปกติ", "osmolyte ครบ"), ""),
           *cell(150, 38, 8, ("Na ต่ำ: น้ำเข้า", "เซลล์บวม"), "twa"),
           *cell(250, 26, 3, ("ผ่าน ~48 ชม.", "ขับ osmolyte ออก"), "tok"),
           *cell(350, 16, 3, ("แก้ Na เร็ว", "น้ำออก เซลล์เหี่ยว"), "tbad", True),
           ar(80, 92, 108, 92, "lwa w2", "ah-wa"), ar(190, 92, 222, 92, "ln", "ah"), ar(278, 92, 330, 92, "lbad w2", "ah-bad"),
           t(304, 84, "เร็ว", "xs mid tbad b"),
           t(206, 84, "ปรับตัว", "xs mid tok"),
           box(10, 194, 400, 44, "bad", "เซลล์เหี่ยว → oligodendrocyte ตาย → myelin ที่ pons หลุด\n→ พูดไม่ชัด กลืนลำบาก อ่อนแรงทั้งตัว จนถึง locked-in", fs=11.5),
           box(10, 248, 400, 34, "ok", "แก้ ≤ 8–10 mmol/L ใน 24 ชม. → เซลล์ดึง osmolyte กลับได้ทัน", fs=11.5)]
    return fig("Osmotic demyelination: เซลล์ปรับตัวแล้ว อย่าดึงกลับเร็ว",
               "เมื่อโซเดียมต่ำเรื้อรัง เซลล์สมองป้องกันตัวเองจากการบวมโดย **ขับ osmolyte (K⁺ glutamate myo-inositol) ออก** จนขนาดกลับปกติ ถ้าแก้โซเดียมเร็ว น้ำนอกเซลล์เข้มข้นขึ้นทันทีแต่เซลล์ **ดึง osmolyte กลับไม่ทัน** น้ำจึงไหลออก เซลล์เหี่ยว โดยเฉพาะ oligodendrocyte ที่ pons ทำให้ myelin หลุด อาการมักโผล่หลังแก้ไปแล้วหลายวัน",
               svg(420, 290, "เซลล์สมองในโซเดียมต่ำบวม แล้วปรับตัวโดยขับ osmolyte ออก ถ้าแก้โซเดียมเร็วเซลล์เหี่ยว ทำให้ myelin ที่ pons หลุด",
                   *out))


# ---------------------------------------------------------------- 11
def acs_confuse3():
    def plot(y0, kind):
        X0, X1, top, bot = 112, 300, y0 + 12, y0 + 66
        pts = []
        for i in range(0, 101):
            tt = i / 100.0
            if kind == "aph":
                v = 1 if tt < 0.3 else 0.35
            elif kind == "del":
                if tt < 0.25: v = 1
                elif tt < 0.35: v = 1 - (tt - 0.25) / 0.1 * 0.6
                elif tt < 0.7: v = 0.4 + 0.22 * math.sin((tt - 0.35) * 40)
                elif tt < 0.85: v = 0.4 + (tt - 0.7) / 0.15 * 0.6
                else: v = 1
            else:
                v = 1 - 0.65 * tt
            pts.append((X0 + (X1 - X0) * tt, bot - (bot - top) * v))
        c = {"aph": "lac w3", "del": "lbad w3", "dem": "lms w3"}[kind]
        return [line(X0, bot, X1, bot, "lmu"), line(X0, top - 4, X0, bot, "lmu"), poly(pts, c)]
    rows = [(20, "aph", "Aphasia", "ทันที (นาที)", "tac", "สมาธิปกติ", "ภาษาเสียอย่างเดียว"),
            (110, "del", "Delirium", "ชั่วโมง–วัน", "tbad", "สมาธิเสีย ผันผวน", "แก้เหตุแล้วกลับคืน"),
            (200, "dem", "Dementia", "เดือน–ปี", "tms", "สมาธิดีช่วงแรก", "ถาวร ค่อย ๆ แย่ลง")]
    out = []
    for y, k, name, onset, tc, a, b in rows:
        out += plot(y, k)
        out += [t(10, y + 30, name, "sm b " + tc), t(10, y + 46, onset, "xs i2"),
                t(312, y + 30, a, "xs b"), t(312, y + 46, b, "xs i2")]
    out += [t(206, 292, "แกนตั้ง = การทำงานของสมองด้านที่เสีย · แกนนอน = เวลา", "xs mid mu")]
    return fig("สามแบบของ \"สับสน\" ดูจากรูปร่างของเวลา",
               "**Aphasia** มาทันทีแบบขั้นบันได (หลอดเลือดอุดหรือแตก) และสมาธิยังดี · **Delirium** ตกลงในชั่วโมงถึงวัน **ขึ้นลงทั้งวัน** และกลับคืนเมื่อแก้เหตุ เพราะเซลล์ประสาทแค่ทำงานผิดชั่วคราว · **Dementia** ค่อย ๆ ลดลงเป็นเดือนถึงปีจากเซลล์ประสาทที่ตายไปเรื่อย ๆ ผู้ป่วยสมองเสื่อมที่ **ตกลงเร็วผิดปกติ** จึงต้องคิดถึง delirium ซ้อน",
               svg(420, 302, "กราฟการทำงานของสมองตามเวลา aphasia ลดลงทันทีแล้วคงที่ delirium ลดลงเร็ว ผันผวน แล้วกลับคืน dementia ค่อย ๆ ลดลง",
                   *out))


def acs_threshold():
    X0, X1, Y0, Y1 = 64, 404, 236, 30
    us = [0.1 + 0.02 * i for i in range(46)]
    curve = [(X0 + (X1 - X0) * u, Y0 - (Y0 - Y1) * min(1.0, 0.1 / u)) for u in us]
    return fig("Delirium เกิดเมื่อสมองเปราะบาง + สิ่งกระตุ้น ข้ามเกณฑ์",
               "ความเสี่ยงคือ **ผลรวมของสองแกน** — สมองที่เปราะบางอยู่เดิม (อายุมาก สมองเสื่อม มองไม่เห็น ได้ยินไม่ชัด) ต้องการสิ่งกระตุ้นเพียงเล็กน้อยเช่น UTI ที่ไม่มีไข้ ก็ข้ามเส้นเกณฑ์ ส่วนคนหนุ่มสาวแข็งแรงต้องเจอสิ่งกระตุ้นรุนแรงอย่าง septic shock ใน ICU นี่คือเหตุที่ **ภาวะสมองเสื่อมเดิมเป็นปัจจัยเสี่ยงที่แรงที่สุด** และไม่ควรคิดว่าอาการที่แย่ลงเร็วเป็นแค่โรคเดิม",
               svg(420, 280, "กราฟสองแกน ความเปราะบางของสมองเดิมกับความรุนแรงของสิ่งกระตุ้น เส้นเกณฑ์โค้ง จุดที่อยู่เหนือเส้นเกิด delirium",
                   line(X0, Y0, X1, Y0, "lmu"), line(X0, Y0, X0, Y1 - 6, "lmu"),
                   t(X1, Y0 + 18, "ความเปราะบางของสมองเดิม →", "xs end mu"),
                   t(X0 - 6, Y1 + 4, "สิ่ง", "xs end mu"), t(X0 - 6, Y1 + 18, "กระตุ้น", "xs end mu"), t(X0 - 6, Y1 + 32, "แรง", "xs end mu"),
                   t(X0 - 6, Y0 - 4, "เบา", "xs end mu"),
                   poly(curve, "lbad w3"), t(X1, Y0 - 8, "เส้นเกณฑ์", "xs end tbad b"),
                   t(300, 70, "เกิด delirium", "b mid tbad"),
                   t(250, 228, "ไม่เกิด", "sm mid tok b"),
                   circ(96, 50, 6, "badf"), t(108, 48, "หนุ่มสาวแข็งแรง", "xs b"), t(108, 62, "+ septic shock · ICU", "xs i2"),
                   circ(362, 184, 6, "badf"), t(352, 158, "ผู้สูงอายุสมองเสื่อม", "xs b end"), t(352, 172, "+ UTI ไม่มีไข้", "xs end i2"),
                   circ(110, 196, 6, "okf"), t(122, 190, "หนุ่มสาว + UTI", "xs b"), t(122, 204, "ไม่สับสน", "xs i2")))


# ---------------------------------------------------------------- 12
def acs_attnfirst():
    def row(y, bad):
        out = []
        for k in range(3):
            yy = y + 12 + 16 * k
            if bad and k != 1:
                out += [line(10, yy, 52, yy, "lmu", "ah-mu"), t(60, yy + 4, "✕", "b mid tbad")]
            else:
                out.append(line(10, yy, 64, y + 28, "ln", "ah"))
        out += [box(66, y, 82, 56, "bad" if bad else "ok", "สมาธิ\n(ตัวกรอง)", "b", fs=12),
                ar(148, y + 28, 168, y + 28, "lmu" if bad else "ln", "ah-mu" if bad else "ah"),
                box(170, y, 96, 56, "sk" if bad else "bx", "ลงทะเบียน\nข้อมูล", fs=12),
                ar(266, y + 28, 286, y + 28, "lmu" if bad else "ln", "ah-mu" if bad else "ah"),
                box(288, y, 122, 56, "sk" if bad else "bx", "ความจำ · ภาษา\n· การคิด", fs=12)]
        return out
    return fig("ทำไมต้องตรวจสมาธิก่อนความจำ",
               "ข้อมูลทุกอย่างต้อง **ผ่านตัวกรองของสมาธิ** ก่อนจึงจะถูกลงทะเบียนและเก็บเป็นความจำ ใน delirium ตัวกรองนี้เสีย ข้อมูลส่วนใหญ่จึง **ไม่เคยเข้าไปตั้งแต่แรก** — ผู้ป่วยจำไม่ได้ ตอบผิด หรือดูเหมือนภาษาเสีย ทั้งที่ระบบความจำยังดี ผลการทดสอบส่วนอื่นจึงแปลผลไม่ได้ถ้าสมาธิเสีย และเป็นเหตุที่ผู้ป่วยมักจำช่วงที่ป่วยไม่ได้เลย",
               svg(420, 220, "ข้อมูลผ่านสมาธิไปสู่การลงทะเบียนและความจำ ใน delirium สมาธิเสีย ข้อมูลส่วนใหญ่ไม่เข้า ทำให้ดูเหมือนความจำเสีย",
                   t(10, 16, "ปกติ", "sm b tok"), *row(24, False),
                   t(10, 112, "Delirium", "sm b tbad"), *row(120, True),
                   t(349, 196, "ดูเหมือนความจำเสีย", "xs mid tbad b"), t(349, 210, "ทั้งที่ข้อมูลไม่เคยเข้า", "xs mid i2")))


def acs_circadian():
    X0, X1 = 82, 404
    X = lambda h: X0 + (X1 - X0) * (h - 6) / 24.0
    lv = {"agi": 44, "alert": 82, "drowsy": 124, "sleep": 160}
    def sig(x, a, w): return 1 / (1 + math.exp(-(x - a) / w))
    hs = [6 + 0.25 * i for i in range(97)]
    def norm(h):
        day = sig(h, 7, 0.4) * (1 - sig(h, 22.5, 0.4))
        return lv["sleep"] + (lv["alert"] - lv["sleep"]) * day
    def deli(h):
        base = 118 + 6 * math.sin(h * 1.7)
        bump = 72 * math.exp(-((h - 22) / 2.6) ** 2)
        dip = 22 * math.exp(-((h - 4.5 - 24) / 1.6) ** 2) if h > 26 else 0
        return base - bump + dip
    out = [rect(X0, lv["alert"] - 12, X1 - X0, 24, "ok", 0),
           t(X0 - 6, lv["agi"] + 4, "กระสับกระส่าย", "xs end mu"), t(X0 - 6, lv["alert"] + 4, "ตื่นปกติ", "xs end mu"),
           t(X0 - 6, lv["drowsy"] + 4, "ง่วงซึม", "xs end mu"), t(X0 - 6, lv["sleep"] + 4, "หลับ", "xs end mu"),
           line(X0, 172, X1, 172, "lmu"),
           *[p for h in (6, 12, 18, 24, 30) for p in (line(X(h), 172, X(h), 176, "lmu"), t(X(h), 188, "%02d:00" % (h % 24), "xs mid mu"))],
           poly([(X(h), norm(h)) for h in hs], "lok w3"),
           poly([(X(h), deli(h)) for h in hs], "lbad w3"),
           line(X(8), 30, X(8), 172, "lmu da"), t(X(8) + 4, 26, "ราวด์เช้า: ดูปกติ?", "xs b"),
           line(X(26), 30, X(26), 172, "lmu da"), t(X(26) - 4, 26, "ตีสอง: สับสนเต็มขั้น", "xs b end"),
           t(X(13), 142, "ง่วงกลางวัน", "xs mid tbad b"), t(X(20.5), 40, "sundowning", "xs end tbad b"),
           line(X0, 210, X0 + 22, 210, "lok w3"), t(X0 + 28, 214, "ปกติ", "xs"),
           line(X0 + 80, 210, X0 + 102, 210, "lbad w3"), t(X0 + 108, 214, "delirium", "xs")]
    return fig("วงจรกลางวัน–กลางคืนที่พังใน delirium",
               "นาฬิกาชีวภาพ (suprachiasmatic nucleus และ melatonin) ต้องอาศัย **แสงกลางวัน ความมืดกลางคืน และกิจวัตร** ในหอผู้ป่วยสัญญาณเหล่านี้หายไป ร่วมกับยาและการอักเสบ — ผู้ป่วยจึง **ง่วงซึมกลางวัน** แล้ว **ตื่นตัวเกินและสับสนหนักตอนเย็นถึงกลางคืน** (sundowning) และช่วงหลับฝัน (REM) ล้นออกมาปนกับความจริง ผู้ป่วยที่ดูปกติตอนราวด์เช้าจึงอาจเป็น delirium เต็มขั้นตอนตีสอง",
               svg(420, 222, "กราฟระดับการตื่นตัวตลอด 24 ชั่วโมง คนปกติตื่นกลางวันหลับกลางคืน ผู้ป่วย delirium ง่วงกลางวันและกระสับกระส่ายตอนเย็นถึงกลางคืน",
                   *out))


# ---------------------------------------------------------------- 13
def acs_cam():
    return fig("CAM: ต้องมี 1 และ 2 ร่วมกับ 3 หรือ 4",
               "ข้อ 1 และ 2 คือแก่นของ delirium — **การเปลี่ยนแปลงเฉียบพลันที่ผันผวน** และ **สมาธิเสีย** ต้องมีทั้งคู่ จากนั้นต้องมีหลักฐานว่าสมองประมวลผลผิดอย่างใดอย่างหนึ่ง คือ ความคิดสับสน (ข้อ 3) หรือระดับการตื่นตัวเปลี่ยน (ข้อ 4) — ข้อ 4 ทำให้ผู้ป่วยที่ **แค่ซึมเงียบ ๆ** (hypoactive) เข้าเกณฑ์ได้ ข้อ 2 ต้องได้จาก **การทดสอบจริง** เช่น ท่องเดือนถอยหลัง ไม่ใช่ความรู้สึก",
               svg(420, 300, "แผนผัง CAM ข้อ 1 และข้อ 2 ต้องมีทั้งคู่ แล้วมีข้อ 3 หรือข้อ 4 อย่างใดอย่างหนึ่ง จึงเป็น delirium",
                   box(10, 10, 190, 60, "ac", "① เฉียบพลัน + ผันผวน\nถามญาติ / พยาบาล", fs=11.5),
                   box(220, 10, 190, 60, "ac", "② สมาธิเสีย\nท่องเดือนถอยหลัง", fs=11.5),
                   line(105, 70, 196, 94, "ln", "ah"), line(315, 70, 224, 94, "ln", "ah"),
                   circ(210, 104, 18, "ac"), t(210, 108, "และ", "sm mid b tac"),
                   line(210, 122, 210, 134, "ln"), line(105, 134, 315, 134, "ln"),
                   line(105, 134, 105, 148, "ln", "ah"), line(315, 134, 315, 148, "ln", "ah"),
                   pill(180, 124, "หรือ", "ms", "sm b mid tms", w=60, h=20),
                   box(10, 150, 190, 56, "bx", "③ ความคิดสับสน\nพูดวกวน เปลี่ยนเรื่อง", fs=11.5),
                   box(220, 150, 190, 56, "bx", "④ ระดับการตื่นตัวเปลี่ยน\nซึม หรือ ตื่นตัวเกิน", fs=11.5),
                   line(105, 206, 180, 232, "ln", "ah"), line(315, 206, 240, 232, "ln", "ah"),
                   box(120, 234, 180, 40, "bad", "Delirium", "b", fs=14),
                   t(210, 292, "แล้วต้องหาเหตุต่อเสมอ (เกณฑ์ข้อ E)", "xs mid i2")))


# ---------------------------------------------------------------- 14
def acs_delnt():
    causes = [("ติดเชื้อ", "cytokine → microglia อักเสบ"), ("ขาด O₂ / น้ำตาล", "สร้าง ACh ไม่ได้"),
              ("ยา anticholinergic", "บล็อก ACh โดยตรง"), ("ถอนสุรา / benzo", "GABA ลดฉับพลัน"),
              ("ตับ / ไตวาย", "สารพิษคั่ง (NH₃ ยูเรีย)")]
    out = []
    for k, (a, b) in enumerate(causes):
        y = 10 + 52 * k
        out += [rect(10, y, 178, 44, "sk", 8), t(20, y + 18, a, "sm b"), t(20, y + 35, b, "xs i2"),
                line(188, y + 22, 218, 128, "ln", "ah")]
    out += [box(220, 84, 190, 88, "bad", "ACh ↓ · dopamine ↑\nเครือข่ายสมาธิล้ม\nprefrontal · thalamus\n· ARAS", fs=11.5),
            line(315, 172, 315, 196, "ln", "ah"),
            box(220, 198, 190, 62, "ms", "สมาธิเสีย · ตื่นตัวขึ้นลง\nคิดสับสน · ประสาทหลอน", fs=11.5)]
    return fig("หลายสาเหตุ ทางสุดท้ายร่วมกัน",
               "สาเหตุของ delirium ต่างกันมาก แต่ส่วนใหญ่ไปกระทบจุดเดียวกัน คือ **เครือข่ายสมาธิที่อาศัย acetylcholine** (prefrontal · thalamus · ARAS) — ACh ลดลงและ dopamine เด่นขึ้น ร่วมกับการอักเสบของ microglia จาก cytokine อาการจึงหน้าตาคล้ายกันไม่ว่าต้นเหตุคืออะไร และ **ยาที่ลดอาการไม่ได้แก้ต้นเหตุ**",
               svg(420, 270, "ห้ากลุ่มสาเหตุ ติดเชื้อ ขาดออกซิเจน ยา ภาวะถอน อวัยวะวาย มาบรรจบที่ acetylcholine ลดและ dopamine เพิ่ม ทำให้สมาธิเสีย",
                   *out))


# ---------------------------------------------------------------- 15
def acs_trajectory():
    X0, X1 = 30, 404
    def cog(x):
        if x < 120: return 50
        if x < 160: return 50 + (x - 120) / 40.0 * 110
        if x < 250: return 160 + 10 * math.sin((x - 160) / 7.0)
        if x < 330: return 160 - (x - 250) / 80.0 * 110
        return 50
    xs = list(range(X0, X1 + 1, 2))
    marks = [(75, "1", "ปกติ", "ช่วยตัวเองได้", 0), (124, "2", "UTI", "ระบบ+เมแทบอลิก", 1),
             (165, "3", "สับสน", "เฉียบพลัน", 0), (215, "4", "ตรวจหาเหตุ", "พบ UTI", 1),
             (300, "5", "ยา + สารน้ำ", "กลับระดับเดิม", 0)]
    out = [rect(X0, 38, X1 - X0, 24, "ok", 0), t(X1 - 4, 34, "ระดับการรู้คิดเดิม", "xs end tok"),
           line(X0, 180, X1, 180, "lmu"), t(X1, 196, "เวลา →", "xs end mu"),
           poly([(x, cog(x)) for x in xs], "lbad w3"),
           line(240, 46, 240, 180, "lok da"), t(244, 104, "เริ่มรักษา", "xs tok b")]
    for x, n, a, b, alt in marks:
        y = 214 if not alt else 250
        out += [circ(x, cog(x), 9, "paf"), circ(x, cog(x), 9, "lac w2"), t(x, cog(x) + 4, n, "xs mid b tac"),
                t(x, y, a, "xs mid b"), t(x, y + 14, b, "xs mid i2")]
    out += [t(110, 130, "ไม่มีไข้ ไม่ปวดแสบขัด", "xs end tbad b"), t(110, 144, "มีแต่ความสับสน", "xs end tbad")]
    return fig("เส้นทางของ delirium จาก UTI",
               "สมองของผู้สูงอายุมี reserve น้อย เมื่อเกิดการติดเชื้อ cytokine และภาวะเมแทบอลิกที่ตามมา **กดการทำงานของสมองก่อนที่อวัยวะต้นเหตุจะแสดงอาการชัด** ความสับสนจึงอาจเป็นอาการเดียว เมื่อแก้เหตุ (ยาปฏิชีวนะ + สารน้ำ) เซลล์ประสาทที่แค่ทำงานผิดชั่วคราวก็ **กลับมาทำงานได้** — ต่างจาก stroke หรือสมองเสื่อมที่เซลล์ตายไปแล้ว",
               svg(420, 276, "กราฟการรู้คิดตามเวลา ปกติ แล้วติดเชื้อทางเดินปัสสาวะ สับสนเฉียบพลัน ตรวจหาเหตุ รักษา แล้วกลับสู่ระดับเดิม",
                   *out))


def acs_iatro():
    out = [box(135, 14, 150, 46, "bad", "Delirium\nกระสับกระส่าย / ซึม", fs=11.5),
           box(260, 112, 150, 46, "ms", "ผูกยึด · ใส่สาย\nให้ benzodiazepine", fs=11.5),
           box(135, 210, 150, 46, "ms", "ขยับไม่ได้ · ติดเชื้อ\nนอนไม่หลับ ดึงสาย", fs=11.5),
           box(10, 112, 150, 46, "ms", "สมาธิและการตื่นตัว\nแย่ลงอีก", fs=11.5),
           path("M286 40 Q336 44 336 108", "lbad w2", "ah-bad"),
           path("M336 160 Q336 226 288 232", "lbad w2", "ah-bad"),
           path("M133 232 Q84 226 84 162", "lbad w2", "ah-bad"),
           path("M84 110 Q84 44 132 40", "lbad w2", "ah-bad"),
           t(210, 132, "วงจรที่", "sm mid b tbad"), t(210, 148, "เราสร้างเอง", "sm mid b tbad"),
           t(10, 288, "จุดตัดวงจร", "sm b tok")]
    cuts = [("ถอดสายที่ไม่จำเป็น", 10, 298, 118), ("ไม่ผูกยึด", 134, 298, 70), ("แว่น · เครื่องช่วยฟัง", 210, 298, 124),
            ("กลางวันสว่าง กลางคืนมืดเงียบ", 10, 326, 168), ("ลุกเดินเร็ว", 184, 326, 76), ("เลี่ยง benzo", 266, 326, 84)]
    for s, x, y, w in cuts:
        out.append(pill(x, y, s, "ok", "xs b mid tok", w=w))
    return fig("อันตรายจากการรักษา: วงจรที่ทำให้ delirium ยืดเยื้อ",
               "สิ่งที่ทำเพื่อ **ควบคุม** ผู้ป่วยมักทำให้ delirium แย่ลง — การผูกยึดและสายต่าง ๆ ตรึงผู้ป่วยไว้กับเตียง เป็นทางเข้าของเชื้อ และเป็นสิ่งที่ผู้ป่วยจะดึง · benzodiazepine กดสมาธิเพิ่ม · เสียงและแสงทั้งคืนทำลายการนอน ทั้งหมดวนกลับมาทำให้สมาธิและการตื่นตัวแย่ลง มาตรการที่ไม่ใช้ยาคือการ **ตัดวงจรนี้** จึงเป็นสิ่งเดียวที่ลดทั้งระยะเวลาและอัตราตาย",
               svg(420, 356, "วงจร delirium ทำให้ผูกยึดและให้ยา ทำให้ขยับไม่ได้ ติดเชื้อ นอนไม่หลับ ทำให้สมาธิแย่ลง และวนกลับมาเป็น delirium พร้อมจุดตัดวงจร",
                   *out))
