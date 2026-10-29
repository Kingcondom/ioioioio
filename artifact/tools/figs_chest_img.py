# -*- coding: utf-8 -*-
"""ภาพประกอบ SVG คาบ chest 21 "Image in chest" (อ.พจนี) — build_chestimg.py เรียก apply_figs กับโมดูลนี้
ภาพรังสีจริงจากสไลด์อยู่ใน artifact/img/chest/ (extract_chestimg.py) — ภาพในไฟล์นี้เป็นแผนภาพกลไก"""
from svg import *

SET, LEC = "chest", "21"

INSERTS = [
    ("chest-img-02", "### Rotation — นับระยะจาก spinous process", "fig:ci_rotation"),
    ("chest-img-07", "### Secondary pulmonary lobule — ทำไม pattern ต่างกัน", "fig:ci_lobule"),
    ("chest-img-08", "### ชนิดของ atelectasis ตามกลไก", "fig:ci_ateltypes"),
    ("chest-img-10", "### ก้อนอยู่ในปอดหรือนอกปอด — ดูมุม", "fig:ci_angle"),
    ("chest-img-16", "### การดูแลตาม BTS 2023 (ไม่อยู่ในสไลด์)", "fig:ci_ptxalgo"),
    ("chest-img-17", "### ILO classification — อ่านฟิล์ม pneumoconiosis อย่างไร", "fig:ci_ilo"),
]


def ci_rotation():
    p = []
    for x0, title, d1, d2, c in ((0, "ไม่หมุน", 40, 40, "ok"), (220, "หมุน", 60, 22, "bad")):
        cx = x0 + 110
        p.append(t(cx, 22, title, "b mid " + ("tok" if c == "ok" else "tbad")))
        p.append(rect(cx - 7, 40, 14, 170, "sk", 4))
        for k in range(5):
            p.append(rect(cx - 5, 56 + k * 32, 10, 10, "muf", 2))  # spinous processes
        sp = cx + (0 if c == "ok" else 8)
        # clavicles
        p.append(path("M%d 64 Q%d 50 %d 54" % (sp - d1, sp - d1 - 50, sp - d1 - 90), "ln w5"))
        p.append(path("M%d 64 Q%d 50 %d 54" % (sp + d2, sp + d2 + 50, sp + d2 + 90), "ln w5"))
        p.append(circ(sp - d1, 66, 6, "bx")); p.append(circ(sp + d2, 66, 6, "bx"))
        p.append(rect(sp - 3, 60, 6, 12, "inkf", 2))
        p.append(ar(sp - 4, 88, sp - d1 + 4, 88, c[0] == "o" and "lok w2" or "lbad w2", "ah-ok" if c == "ok" else "ah-bad"))
        p.append(ar(sp + 4, 88, sp + d2 - 4, 88, c[0] == "o" and "lok w2" or "lbad w2", "ah-ok" if c == "ok" else "ah-bad"))
        p.append(t(cx, 112, "ระยะ %s" % ("เท่ากัน" if c == "ok" else "ไม่เท่ากัน"), "sm mid"))
        p.append(rect(x0 + 30, 130, 160, 90, c))
        if c == "ok":
            p.append(t(cx, 156, "hila mediastinum", "sm mid"))
            p.append(t(cx, 176, "ความทึบสองข้าง", "sm mid"))
            p.append(t(cx, 196, "เทียบกันได้", "sm mid b tok"))
        else:
            p.append(t(cx, 156, "hilum/mediastinum", "sm mid"))
            p.append(t(cx, 176, "ดูไม่สมมาตรหลอก", "sm mid"))
            p.append(t(cx, 196, "อย่าเพิ่งแปลผล", "sm mid b tbad"))
    return fig("Rotation — วัดระยะ spinous process ถึงหัว clavicle",
               "สไลด์: \"ระยะระหว่าง spinous process และ medial end of head clavicle ทั้งสองข้าง\" ต้อง **เท่ากัน** · ถ้าไม่เท่า ผู้ป่วยหมุนตัว → "
               "hilum ข้างหนึ่งเด่น mediastinum ดูกว้าง ความทึบสองข้างต่างกันได้โดยไม่มีโรค (ข้อสอบคลัง CH-MCQ-25)",
               svg(440, 230, "แผนภาพเทียบฟิล์มที่ไม่หมุน ระยะจาก spinous process ถึงหัว clavicle สองข้างเท่ากัน กับฟิล์มที่หมุนระยะไม่เท่ากัน", *p))


def ci_lobule():
    p = []
    # polygon lobule
    pts = [(220, 30), (330, 70), (350, 180), (280, 260), (150, 260), (90, 170), (110, 70)]
    p.append(poly(pts, "lbad w3", closed=True))
    p.append(t(360, 120, "interlobular septum", "xs b tbad"))
    p.append(t(360, 134, "vein + lymphatic", "xs tbad"))
    # center bronchiole + artery
    p.append(path("M220 10 L220 150 M220 150 L190 200 M220 150 L250 200", "lwa w3"))
    p.append(path("M230 10 L230 150 M230 150 L262 196", "lac w2"))
    p.append(t(240, 30, "bronchiole + artery", "xs b"))
    p.append(t(240, 44, "(กลาง lobule)", "xs"))
    for x, y in ((160, 110), (280, 120), (200, 220), (300, 200), (130, 190), (250, 90)):
        p.append(circ(x, y, 9, "bx"))
    p.append(t(110, 290, "septum หนา → Kerley B, reticular", "sm"))
    p.append(t(110, 310, "รอบหลอดลมกลาง → centrilobular / tree-in-bud", "sm"))
    p.append(t(110, 330, "ถุงลมเต็ม → consolidation / GGO", "sm"))
    return fig("Secondary pulmonary lobule — หน่วยที่ใช้แยก pattern",
               "สไลด์ p57–58: lobule รูปหลายเหลี่ยม **1–2.5 ซม.** มี **bronchiole + pulmonary artery อยู่กลาง** และ **pulmonary vein กับท่อน้ำเหลืองวิ่งใน interlobular septa** · "
               "✍️ อาจารย์เขียน \"lesion → airway / artery / lymphatic\" — รอยโรคอยู่ส่วนไหนของ lobule จะให้รูปแบบต่างกัน (ภาพจำลอง)",
               svg(440, 340, "แผนภาพ secondary pulmonary lobule มี bronchiole และ artery อยู่ตรงกลาง ล้อมด้วย interlobular septum ที่มีหลอดเลือดดำและท่อน้ำเหลือง", *p))


def ci_ateltypes():
    p = []
    rows = [("Resorption (obstructive)", "หลอดลมอุด → ลมถูกดูดซึม", "พบบ่อยสุด · volume ลด · ไม่มี air bronchogram", "bad"),
            ("Relaxation (passive)", "น้ำ/ลม/ก้อนกดปอด", "ปอดหดตาม recoil · ความทึบอาจไม่มาก", "wa"),
            ("Adhesive", "ขาด surfactant", "ARDS · RDS ทารก · radiation", "ms"),
            ("Cicatricial", "พังผืดดึงรั้ง", "✍️ TB เก่า · volume ลดมาก", "ac")]
    for i, (n, mech, res, c) in enumerate(rows):
        y = 14 + i * 74
        p.append(rect(10, y, 420, 64, c))
        p.append(t(22, y + 22, n, "b"))
        p.append(t(22, y + 42, mech, "sm"))
        p.append(t(22, y + 58, res, "xs i2"))
    return fig("ชนิดของ atelectasis ตามกลไก",
               "สไลด์ p101: **resorption** (✍️ common) เกิดภายใน 24 ชม. หลังหลอดลมอุด เร็วขึ้นเมื่อหายใจ O₂ · collateral ventilation อาจกันการยุบ · "
               "**relaxation** จาก effusion/pneumothorax/ก้อน · **adhesive** จากขาด surfactant · **cicatricial** จาก fibrosis (✍️ TB)",
               svg(440, 310, "ตารางภาพสี่ชนิดของ atelectasis resorption relaxation adhesive และ cicatricial พร้อมกลไกและลักษณะ", *p))


def ci_angle():
    p = []
    p.append(t(110, 22, "ในเนื้อปอด", "b mid tbad"))
    p.append(t(330, 22, "นอกปอด (pleura/ผนังอก)", "b mid tac"))
    for x0 in (0, 220):
        p.append(rect(x0 + 160, 36, 40, 220, "sk", 4))
        p.append(t(x0 + 180, 270, "ผนังอก", "xs mid mu"))
    # intraparenchymal: circle touching wall at acute angle
    p.append(circ(120, 146, 40, "bad"))
    p.append(path("M148 118 L160 108", "lbad w2")); p.append(path("M148 174 L160 184", "lbad w2"))
    p.append(t(70, 214, "มุมแหลมกับผนัง", "sm b tbad"))
    p.append(t(70, 232, "ขอบรอบก้อนครบ", "xs"))
    # extrapulmonary: lens shape with tapering edges
    p.append(path("M380 70 C340 100 330 190 380 222 Z", "ac"))
    p.append(t(260, 214, "มุมป้าน ขอบเรียว", "sm b tac"))
    p.append(t(260, 232, "ขอบด้านนอกหาย (incomplete)", "xs"))
    p.append(t(260, 250, "ดูซี่โครงกร่อนข้างใต้", "xs"))
    return fig("ก้อนในปอด vs นอกปอด — มุมกับผนังอก",
               "สไลด์ p126–128: **intraparenchymal** — ก้อนกลมขอบคม **มุมแหลม (acute)** กับ pleura · **extrapulmonary** (pleura ผนังอก ซี่โครง) — ก้อนเรียบนูนเข้าปอด "
               "**ขอบเรียว (tapering) มุมป้าน (obtuse)** ✍️ \"มุมป้านกับ chest wall\" และขอบไม่ครบรอบเพราะด้านที่ติดผนังไม่มีลมล้อม · สไลด์มีตัวอย่าง lytic anterior rib",
               svg(440, 280, "แผนภาพเทียบก้อนในเนื้อปอดทำมุมแหลมกับผนังอก กับก้อนนอกปอดทำมุมป้านขอบเรียว", *p))


def ci_ptxalgo():
    p = []
    p.append(box(120, 10, 200, 40, "sk", "Primary spontaneous PTX", "b"))
    p.append(ar(220, 50, 220, 70, "ln", "ah"))
    p.append(box(70, 70, 300, 52, "ms", "มี high-risk ไหม?\nความดันไม่คงที่ · SpO₂ ต่ำ · ทั้งสองข้าง · hemothorax", tc="sm"))
    p.append(ar(150, 122, 110, 150, "lbad", "ah-bad", "มี", "xs mid tbad", dx=-12))
    p.append(ar(290, 122, 330, 150, "lok", "ah-ok", "ไม่มี", "xs mid tok", dx=14))
    p.append(box(10, 150, 190, 60, "bad", "chest drain\n(tension → needle ก่อน)", tc="sm"))
    p.append(box(240, 150, 190, 60, "ok", "หอบมากจนทนไม่ได้?", tc="sm"))
    p.append(ar(290, 210, 260, 236, "lok", "ah-ok", "ไม่", "xs mid", dx=-12))
    p.append(ar(380, 210, 400, 236, "lbad", "ah-bad", "ใช่", "xs mid", dx=14))
    p.append(box(180, 236, 160, 64, "ok", "conservative\nนัดติดตาม\n(ไม่ขึ้นกับขนาด)", tc="sm"))
    p.append(box(350, 236, 84, 64, "ms", "aspiration\n/ ambulatory\ndevice", tc="xs"))
    return fig("Primary spontaneous pneumothorax — BTS 2023 (ย่อ)",
               "สไลด์ให้เกณฑ์ขนาด **> 2 ซม. ที่ระดับ hilum ≈ 50%** · แนวทาง **BTS 2023** เปลี่ยนให้ตัดสินตาม **อาการและ high-risk features** มากกว่าขนาด — ผู้ไม่มีอาการมากรักษาแบบ conservative ได้ "
               "แม้ปอดยุบมาก · secondary PTX (มีโรคปอดเดิม เช่น COPD) และ tension ต้องใส่สาย · ภาพนี้ไม่อยู่ในสไลด์",
               svg(440, 310, "แผนภูมิการดูแล primary spontaneous pneumothorax ตาม BTS 2023 แบบย่อ แยกตาม high-risk features และอาการ", *p))


def ci_ilo():
    p = []
    p.append(box(10, 10, 420, 40, "sk", "ILO 2022 — เทียบกับฟิล์มมาตรฐาน (standard radiographs)", "b"))
    p.append(box(10, 60, 136, 110, "ac", "Small opacities\nรูป: กลม p q r\nเส้น s t u\nprofusion 0–3", tc="sm"))
    p.append(box(152, 60, 136, 110, "bad", "Large opacities\n> 10 มม.\nA B C\n(= PMF)", tc="sm"))
    p.append(box(294, 60, 136, 110, "ms", "Pleural\nplaque\ndiffuse thickening\ncalcification", tc="sm"))
    p.append(t(20, 196, "p < 1.5 · q 1.5–3 · r 3–10 มม. (กลม) → silica/coal", "sm"))
    p.append(t(20, 216, "s t u (เส้น) ปอดล่าง → asbestosis", "sm"))
    p.append(t(20, 236, "ใช้คัดกรองและติดตามคนงาน ไม่ใช่การวินิจฉัยโรคเดี่ยว ๆ", "xs mu"))
    return fig("ILO classification — ภาษากลางของฟิล์ม pneumoconiosis",
               "อ่านฟิล์ม PA โดยเทียบกับชุดฟิล์มมาตรฐานของ **International Labour Organization (ILO, ฉบับปรับปรุง 2022)** · บันทึกขนาด/รูปร่าง (p q r · s t u) "
               "ความหนาแน่น (profusion 0/– ถึง 3/+) โซนที่พบ ก้อนใหญ่ (A B C) และความผิดปกติของเยื่อหุ้มปอด · ส่วนนี้ **ไม่อยู่ในสไลด์**",
               svg(440, 246, "แผนภาพสรุปหมวดของ ILO classification small opacities large opacities และ pleural abnormalities", *p))
