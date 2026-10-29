# -*- coding: utf-8 -*-
"""ภาพประกอบ SVG คาบ chest 21 "Image in chest" (อ.พจนี) — build_chestimg.py เรียก apply_figs กับโมดูลนี้
ภาพรังสีจริงจากสไลด์อยู่ใน artifact/img/chest/ (extract_chestimg.py) — ภาพในไฟล์นี้เป็นแผนภาพกลไก"""
import math
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
        p.append(path("M%d 64 Q%d 52 %d 56" % (sp - d1, sp - d1 - 28, sp - d1 - 50), "ln w5"))
        p.append(path("M%d 64 Q%d 52 %d 56" % (sp + d2, sp + d2 + 28, sp + d2 + 50), "ln w5"))
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
    pts = [(190, 30), (300, 70), (320, 180), (250, 260), (120, 260), (60, 170), (80, 70)]
    p.append(poly(pts, "lbad w3", closed=True))
    p.append(t(326, 120, "interlobular septum", "xs b tbad"))
    p.append(t(326, 134, "vein + lymphatic", "xs tbad"))
    # center bronchiole + artery
    p.append(path("M190 10 L190 150 M190 150 L160 200 M190 150 L220 200", "lwa w3"))
    p.append(path("M200 10 L200 150 M200 150 L232 196", "lac w2"))
    p.append(t(150, 18, "bronchiole + artery", "xs b end"))
    p.append(t(150, 32, "(กลาง lobule)", "xs end"))
    for x, y in ((130, 110), (250, 120), (170, 222), (270, 200), (100, 190), (226, 84)):
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
    W, H = 210, 132
    pan = [(8, 8, "Resorption (obstructive)", "bad"), (222, 8, "Relaxation (passive)", "wa"),
           (8, 158, "Adhesive", "ms"), (222, 158, "Cicatricial", "ac")]
    for x0, y0, n, c in pan:
        p.append(rect(x0, y0, W, H, "bx", 10))
        p.append(t(x0 + 10, y0 + 18, n, "sm b"))
    # 1 resorption: หลอดลมอุด → ก๊าซถูกดูดเข้าเลือด
    x0, y0 = 8, 8
    p.append(line(x0 + 30, y0 + 30, x0 + 30, y0 + 72, "lwa w5"))
    p.append(rect(x0 + 22, y0 + 52, 16, 12, "inkf", 3))
    p.append(t(x0 + 44, y0 + 62, "เสมหะ/ก้อนอุด", "xs"))
    p.append(circ(x0 + 52, y0 + 92, 18, "lmu da")); p.append(circ(x0 + 52, y0 + 92, 9, "bad"))
    p.append(rect(x0 + 110, y0 + 81, 80, 22, "bad", 6)); p.append(t(x0 + 150, y0 + 96, "เลือด", "xs mid b"))
    p.append(ar(x0 + 64, y0 + 92, x0 + 108, y0 + 92, "lbad w2", "ah-bad"))
    p.append(t(x0 + 86, y0 + 80, "O₂ N₂", "xs mid tbad"))
    p.append(t(x0 + 10, y0 + 126, "ไม่มีลมเติม → ยุบ (เร็วขึ้นถ้าให้ O₂)", "xs"))
    # 2 relaxation: น้ำกด ปอดหดตาม recoil
    x0, y0 = 222, 8
    p.append(rect(x0 + 14, y0 + 28, 182, 84, "sk", 8))
    p.append(rect(x0 + 16, y0 + 80, 178, 30, "wa", 6)); p.append(t(x0 + 105, y0 + 100, "น้ำ / ลม / ก้อน", "xs mid b twa"))
    p.append(ell(x0 + 105, y0 + 56, 50, 18, "bx")); p.append(t(x0 + 105, y0 + 60, "ปอดหด", "xs mid"))
    p.append(ar(x0 + 40, y0 + 56, x0 + 58, y0 + 56, "lwa", "ah-wa")); p.append(ar(x0 + 170, y0 + 56, x0 + 152, y0 + 56, "lwa", "ah-wa"))
    p.append(t(x0 + 10, y0 + 126, "ถูกกด/ปอดหดตาม elastic recoil", "xs"))
    # 3 adhesive: ไม่มี surfactant
    x0, y0 = 8, 158
    p.append(circ(x0 + 52, y0 + 66, 26, "bx"))
    for k in range(10):
        a = k * math.pi / 5
        p.append(circ(x0 + 52 + 26 * math.cos(a), y0 + 66 + 26 * math.sin(a), 3, "okf"))
    p.append(t(x0 + 52, y0 + 108, "มี surfactant", "xs mid tok"))
    p.append(circ(x0 + 150, y0 + 66, 10, "bad"))
    p.append(ar(x0 + 150, y0 + 36, x0 + 150, y0 + 52, "lbad", "ah-bad")); p.append(ar(x0 + 180, y0 + 66, x0 + 164, y0 + 66, "lbad", "ah-bad"))
    p.append(t(x0 + 150, y0 + 108, "ไม่มี → แรงตึงผิวสูง", "xs mid tbad"))
    p.append(t(x0 + 10, y0 + 126, "ARDS · RDS ทารก · radiation", "xs"))
    # 4 cicatricial: พังผืดดึงรั้ง
    x0, y0 = 222, 158
    p.append(rect(x0 + 14, y0 + 28, 182, 84, "bx", 8))
    for k in range(4):
        p.append(path("M%d %d l14 -10 l12 12 l14 -8" % (x0 + 30 + k * 36, y0 + 60 + (k % 2) * 16), "lac w2"))
    p.append(ar(x0 + 105, y0 + 92, x0 + 105, y0 + 40, "lac w2", "ah-ac"))
    p.append(t(x0 + 114, y0 + 100, "ดึงขึ้น/เข้าหา", "xs tac"))
    p.append(t(x0 + 10, y0 + 126, "✍️ TB เก่า · fibrosis → volume ลดมาก", "xs"))
    return fig("ชนิดของ atelectasis ตามกลไก",
               "สไลด์ p101: **resorption** (✍️ common) เกิดภายใน 24 ชม. หลังหลอดลมอุด เร็วขึ้นเมื่อหายใจ O₂ · collateral ventilation อาจกันการยุบ · "
               "**relaxation** จาก effusion/pneumothorax/ก้อน · **adhesive** จากขาด surfactant · **cicatricial** จาก fibrosis (✍️ TB)",
               svg(440, 298, "แผนภาพสี่กลไกของ atelectasis หลอดลมอุดแล้วก๊าซถูกดูดซึม ปอดถูกน้ำกดจนหด ถุงลมยุบเพราะขาด surfactant และพังผืดดึงรั้ง", *p))


def ci_angle():
    p = []
    p.append(t(110, 22, "ในเนื้อปอด", "b mid tbad"))
    p.append(t(330, 22, "นอกปอด (pleura/ผนังอก)", "b mid tac"))
    for x0 in (0, 220):
        p.append(rect(x0 + 160, 36, 40, 220, "sk", 4))
        p.append(t(x0 + 180, 270, "ผนังอก", "xs mid mu"))
    # intraparenchymal: circle touching wall at acute angle
    p.append(circ(120, 146, 40, "bad"))
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
    p.append(box(240, 150, 190, 60, "ok", "มีอาการรบกวนมาก?", tc="sm"))
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
