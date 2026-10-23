# -*- coding: utf-8 -*-
"""ภาพประกอบคาบ chest "Thoracentesis" — หัตถการเจาะน้ำในช่องเยื่อหุ้มปอด + การแปลผลน้ำ (ใช้ใน build_thoracentesis.py)

ทุกฟังก์ชันคืน fig(title, cap, svg) · กว้าง ≤ 420 · ดูภาพ:
    python3 artifact/tools/preview_figs.py figs_thoracentesis --out <dir>"""
from svg import *


# ───────────────────────────── 1. ชั้นที่เข็มผ่าน
def thr_layers():
    layers = [("ผิวหนัง", "bx", 26), ("ไขมัน + superficial fascia", "ms", 26),
              ("External intercostal", "bad", 20), ("Internal intercostal", "bad", 20),
              ("Innermost intercostal", "bad", 20), ("Parietal pleura (ปวด — มีประสาท)", "ac", 14)]
    out, y = [], 22
    for name, c, h in layers:
        out += [rect(20, y, 230, h, c, 0), t(28, y + h / 2 + 4, name, "xs b")]
        y += h
    out += [rect(20, y, 230, 92, "wa", 0), t(28, y + 18, "น้ำในช่องเยื่อหุ้มปอด", "sm b twa"),
            t(28, y + 34, "(ปกติ ~10–20 mL)", "xs twa")]
    yf = y
    y += 92
    out += [rect(20, y, 230, 12, "ok", 0), t(28, y + 10, "Visceral pleura (ไม่มีประสาทรับปวด)", "xs b")]
    y += 12
    out += [rect(20, y, 230, 54, "sk", 0), t(28, y + 20, "เนื้อปอดถูกน้ำกดแฟบ", "xs b"),
            t(28, y + 36, "(compressive atelectasis)", "xs mu")]
    yb = y + 54
    # เข็ม
    out += [line(222, 6, 222, yf + 52, "lbad w3"), poly([(217, yf + 46), (227, yf + 46), (222, yf + 60)], "badf", True),
            t(214, 14, "เข็ม 90°", "xs b tbad end")]
    # ป้ายขวา
    out += [brace(258, 22, 22 + 26 + 26, "lmu"), t(276, 46, "ฉีดยาชาทีละชั้น", "xs b"), t(276, 60, "ดูดก่อนฉีดทุกครั้ง", "xs mu"),
            brace(258, 74, yf, "lmu"), t(276, 112, "ยาชาต้องถึง parietal", "xs b"), t(276, 126, "pleura — ชั้นที่เจ็บที่สุด", "xs b"),
            t(276, yf + 26, "ดูดได้น้ำ = ถึงช่องแล้ว", "xs b tok"), t(276, yf + 40, "จำความลึกไว้ ห้ามแทงลึกกว่า", "xs tok"),
            t(276, yb - 22, "ลึกเกิน → แทงปอด", "xs b tbad"), t(276, yb - 8, "→ pneumothorax", "xs tbad")]
    return fig("ชั้นที่เข็มผ่าน จากผิวหนังถึงน้ำ",
               "เข็มผ่าน **ผิวหนัง → ไขมัน → กล้ามเนื้อ intercostal 3 ชั้น → parietal pleura → ช่องที่มีน้ำ** · parietal pleura มีประสาท intercostal เลี้ยง "
               "จึงต้องฉีดยาชาให้ถึงชั้นนี้ (visceral pleura ไม่มีประสาทรับปวด) · ดูดก่อนฉีดทุกครั้ง: ได้เลือด = อยู่ในหลอดเลือด · ได้น้ำ = ถึงช่องแล้ว → "
               "ความลึกตรงนั้นคือความลึกที่สายต้องไป ไม่ต้องแทงต่อ เพราะใต้ชั้นน้ำคือปอดที่ถูกกดแฟบ",
               svg(420, yb + 10, "ภาพตัดขวางผนังอกแสดงชั้นที่เข็มผ่านจนถึงน้ำในช่องเยื่อหุ้มปอด", *out))


# ───────────────────────────── 1b. trachea ถูกดัน vs ถูกดึง
def _chest(x0, mode):
    out = [path("M%d 40 Q%d 30 %d 40 L%d 190 Q%d 205 %d 190 Z" % (x0 + 10, x0 + 95, x0 + 180, x0 + 182, x0 + 95, x0 + 8), "ln")]
    cx = x0 + 95
    if mode == "eff":
        out += [path("M%d 80 Q%d 70 %d 80 L%d 188 Q%d 196 %d 188 Z" % (x0 + 14, x0 + 50, x0 + 88, x0 + 92, x0 + 50, x0 + 12), "wa"),
                rect(x0 + 112, 60, 52, 110, "sk", 20), t(x0 + 50, 140, "น้ำ", "sm b mid twa")]
        tx = cx + 16
        out += [ar(cx - 4, 120, cx + 18, 120, "lwa w2", "ah-wa")]
    else:
        out += [rect(x0 + 20, 70, 50, 100, "bx", 10), t(x0 + 45, 112, "ปอด", "xs mid"), t(x0 + 45, 126, "แฟบ", "xs mid b tbad"),
                rect(x0 + 112, 60, 56, 112, "sk", 20)]
        tx = cx - 16
        out += [ar(cx + 4, 120, cx - 18, 120, "lbad w2", "ah-bad")]
    out += [line(cx, 8, cx, 40, "lmu da"), path("M%d 8 L%d 36 L%d 70" % (cx, tx, tx), "ln w3"),
            circ(tx, 72, 5, "acf")]
    return out


def thr_shift():
    out = _chest(10, "eff") + _chest(220, "col")
    out += [t(105, 224, "น้ำมาก → trachea ถูกดันไปฝั่งตรงข้าม", "xs mid b twa"),
            t(315, 224, "ปอดแฟบ (ก้อนอุดหลอดลม) → ถูกดึงเข้าหา", "xs mid b tbad"),
            t(105, 240, "เจาะระบายได้ผลดี", "xs mid"), t(315, 240, "เจาะระบาย → ปอดไม่ขยาย", "xs mid"),
            t(315, 254, "(คิดถึง bronchoscopy ก่อน)", "xs mid mu")]
    return fig("ฝ้าทั้งข้าง — mediastinum บอกว่าควรเจาะหรือไม่",
               "น้ำปริมาณมากเพิ่มปริมาตรข้างนั้นจึง **ดัน trachea/mediastinum ไปฝั่งตรงข้าม** — ระบายแล้วปอดขยายได้ · "
               "ถ้า trachea **ถูกดึงเข้าหา** ฝั่งที่ทึบ แปลว่ามีปอดแฟบ (เช่นก้อนอุดหลอดลม) ซึ่งการเจาะระบายจะไม่ทำให้ปอดขยาย "
               "และความดันในช่องอกจะติดลบเร็วมาก (เสี่ยง re-expansion edema และ pneumothorax ex vacuo) · ถ้า trachea อยู่กลางทั้งที่ฝ้าทั้งข้าง "
               "ให้คิดถึงปอดแฟบร่วมกับน้ำ หรือ mediastinum ถูกตรึงด้วยมะเร็ง",
               svg(420, 262, "เปรียบเทียบน้ำในช่องเยื่อหุ้มปอดปริมาณมากที่ดัน trachea ออก กับปอดแฟบที่ดึง trachea เข้าหา", *out))


# ───────────────────────────── 2. เมื่อไรต้องเจาะ
def thr_indic():
    out = [box(110, 8, 200, 34, "bx", "Pleural effusion ใหม่", "b"),
           ar(210, 42, 210, 58, "ln", "ah"),
           box(110, 58, 200, 40, "ms", "หนาพอเจาะไหม?\n> 10 mm (decubitus/US)", "", fs=12),
           ar(110, 78, 96, 78, "lmu", "ah-mu"), t(104, 54, "ไม่", "xs mid mu"), box(4, 58, 90, 40, "sk", "สังเกต/\nรักษาสาเหตุ", "", fs=10.5),
           ar(210, 98, 210, 116, "ln", "ah"), t(216, 110, "ใช่", "xs"),
           box(70, 116, 280, 46, "ms", "เข้าได้กับหัวใจล้มเหลวทั่วไป?\nสองข้าง เท่า ๆ กัน ไม่มีไข้ ไม่เจ็บอก", "", fs=11.5),
           ar(350, 139, 370, 139, "lmu", "ah-mu"), box(372, 116, 44, 46, "sk", "ให้\nยาขับ\nก่อน", "", fs=10.5),
           t(210, 176, "ไม่ใช่ หรือให้ยาแล้วไม่ลด", "xs mid"),
           box(8, 180, 196, 82, "ac", None), t(106, 200, "Diagnostic tap", "sm b mid tac"),
           t(106, 218, "ไม่รู้สาเหตุ · สงสัยติดเชื้อ", "xs mid"), t(106, 232, "สงสัยมะเร็ง · แยกหัวใจ/ไม่ใช่", "xs mid"),
           t(106, 250, "ดูด 20–60 mL", "xs mid b"),
           box(216, 180, 196, 82, "wa", None), t(314, 200, "Therapeutic tap", "sm b mid twa"),
           t(314, 218, "หอบจากน้ำมาก · เตรียม pleurodesis", "xs mid"), t(314, 232, "ระบาย empyema/hemothorax*", "xs mid"),
           t(314, 250, "≤ 1–1.5 L ต่อครั้ง + ส่งตรวจ", "xs mid b"),
           ar(150, 162, 106, 180, "ln", "ah"), ar(270, 162, 314, 180, "ln", "ah"),
           t(210, 282, "* empyema/hemothorax ส่วนใหญ่ต้องใส่ chest drain ต่อ", "xs mid mu")]
    return fig("Diagnostic หรือ therapeutic — ตัดสินใจอย่างไร",
               "สไลด์: เจาะเพื่อวินิจฉัยเมื่อ **น้ำใหม่หนา > 10 mm ใน lateral decubitus/US/CT** และไม่รู้สาเหตุ สงสัยติดเชื้อหรือมะเร็ง "
               "หรือต้องแยกว่าเป็นจากหัวใจหรือไม่ · diagnostic ดูดน้ำน้อย (สไลด์ 20–30 mL · ถ้าส่ง cytology ใช้ 25–50 mL ขึ้นไป) · "
               "therapeutic ระบายเป็นลิตรเมื่อหอบจากน้ำ — **ถ้ายังไม่รู้สาเหตุ ต้องแบ่งส่งตรวจด้วยทุกครั้ง** · "
               "น้ำสองข้างแบบหัวใจล้มเหลวทั่วไป ให้ยาขับปัสสาวะดูก่อน (ขั้นนี้อิง BTS 2023 และคาบ 17)",
               svg(420, 292, "แผนภูมิตัดสินใจเจาะน้ำในช่องเยื่อหุ้มปอดเพื่อวินิจฉัยหรือเพื่อรักษา", *out))


# ───────────────────────────── 3. relative contraindication → กลไกอันตราย → ทางแก้
def thr_contra():
    rows = [("เลือดออกง่าย", "INR · เกล็ดเลือด · ยา", "แทงโดน intercostal a.\n→ hemothorax", "แก้ค่าเลือดตามความเสี่ยง\nUS + แทงเหนือซี่โครง"),
            ("ผิวหนังติดเชื้อ", "cellulitis ตรงจุดเจาะ", "เข็มพาเชื้อเข้าช่อง\n→ empyema", "เลือกจุดอื่น\nที่ผิวปกติ"),
            ("ไอ/สะอึกคุมไม่ได้", "ผู้ป่วยขยับตัวตลอด", "ปอดเลื่อนมาชนปลายเข็ม\n→ pneumothorax", "รักษาไอก่อน\nใช้สายพลาสติกแทนเข็ม"),
            ("ใส่เครื่องช่วยหายใจ", "positive pressure", "รูเล็กที่ปอดกลายเป็น\ntension pneumothorax", "ผู้ชำนาญ + US\nเฝ้าระวังใกล้ชิด")]
    out = [t(10, 16, "ภาวะ (relative)", "xs b mu"), t(150, 16, "เกิดอะไรถ้าฝืนเจาะ", "xs b tbad"), t(290, 16, "ลดความเสี่ยง", "xs b tok")]
    for k, (a, b, c, d) in enumerate(rows):
        y = 26 + 70 * k
        out += [box(6, y, 128, 60, "ms", None), t(70, y + 24, a, "sm b mid"), t(70, y + 42, b, "xs mid mu"),
                ar(134, y + 30, 146, y + 30, "ln", "ah"),
                box(148, y, 130, 60, "bad", c, "", fs=11),
                ar(278, y + 30, 290, y + 30, "ln", "ah"),
                box(292, y, 122, 60, "ok", d, "", fs=10.5)]
    return fig("ข้อห้ามทุกข้อเป็น relative — เข้าใจกลไกแล้วแก้ได้",
               "ลายมือในสไลด์เขียนกำกับว่า **Relative** — ไม่มีข้อห้ามเด็ดขาด · ทุกข้อเพิ่มโอกาสเกิดภาวะแทรกซ้อนที่อธิบายได้ด้วยกลไก "
               "จึงชั่งประโยชน์กับความเสี่ยงและแก้ที่ต้นเหตุก่อน · ค่าที่ใช้กันทั่วไปคือ INR ≤ 1.5 และเกล็ดเลือด ≥ 50,000/µL "
               "แต่ข้อมูลปัจจุบันพบว่าการเจาะใต้อัลตราซาวด์เลือดออกน้อยมากแม้ค่าเลือดผิดปกติเล็กน้อย (ขึ้นกับนโยบายของโรงพยาบาล)",
               svg(420, 310, "ข้อห้ามสัมพัทธ์ของการเจาะน้ำในช่องเยื่อหุ้มปอด กลไกอันตราย และการลดความเสี่ยง", *out))


# ───────────────────────────── 4. ท่าผู้ป่วย
def thr_position():
    out = []
    # ภาพหลัง (นั่งโน้มตัว)
    x0 = 10
    out += [t(x0 + 95, 16, "ท่านั่งโน้มตัว — มองจากด้านหลัง", "xs b mid"),
            path("M%d 30 Q%d 22 %d 30 L%d 250 L%d 250 Z" % (x0 + 20, x0 + 95, x0 + 170, x0 + 180, x0 + 10), "ln"),
            line(x0 + 95, 34, x0 + 95, 248, "lmu da")]
    for k in range(9):
        y = 56 + 21 * k
        out += [path("M%d %d Q%d %d %d %d" % (x0 + 92, y, x0 + 60, y - 6, x0 + 24, y + 8), "lru"),
                path("M%d %d Q%d %d %d %d" % (x0 + 98, y, x0 + 130, y - 6, x0 + 166, y + 8), "lru")]
    out += [path("M%d 54 L%d 60 L%d 128 Z" % (x0 + 80, x0 + 34, x0 + 64), "sk"), line(x0 + 106, 70, x0 + 74, 76, "lmu"), t(x0 + 108, 72, "scapula", "xs mu"),
            path("M%d 170 Q%d 160 %d 172 L%d 248 L%d 248 Z" % (x0 + 14, x0 + 50, x0 + 90, x0 + 90, x0 + 12), "wa"),
            t(x0 + 30, 238, "น้ำ", "sm b mid twa"),
            line(x0 + 50, 60, x0 + 50, 248, "lac da"), t(x0 + 50, 268, "mid-scapular line", "xs mid tac"),
            circ(x0 + 50, 196, 7, "badf"), t(x0 + 62, 200, "จุดเจาะ", "xs b tbad"),
            t(x0 + 104, 176, "ขอบบนของน้ำ", "xs twa"), ar(x0 + 102, 172, x0 + 82, 168, "lwa", "ah-wa"),
            t(x0 + 104, 212, "ต่ำกว่า 1–2 ช่อง", "xs"), t(x0 + 104, 226, "ไม่ต่ำกว่า ICS 8–9", "xs b tbad")]
    # ภาพตัดขวาง (นอนหงาย มองจากปลายเท้า)
    x1 = 222
    cx, cy = x1 + 112, 104
    out += [t(x1 + 98, 16, "ท่านอนหงาย — ภาพตัดขวาง", "xs b mid"),
            rect(x1 + 20, 156, 180, 12, "sk", 4), t(x1 + 110, 184, "เตียง", "xs mid mu"),
            ell(cx, cy, 80, 50, "ln"),
            path("M%.1f 120 A 80 50 0 0 0 %d 153.8 L %d 120 Z" % (cx - 75.8, cx - 4, cx - 4), "wa"),
            t(x1 + 76, 142, "น้ำ", "sm b mid twa"),
            circ(cx, cy + 40, 6, "inkf"), t(cx + 10, cy + 44, "spine", "xs mu"),
            rect(cx - 6, cy - 52, 12, 10, "inkf", 2), t(cx, cy - 28, "sternum", "xs mid mu"),
            line(x1 + 32, 46, x1 + 32, 160, "lac da"), t(x1 + 36, 44, "mid-axillary", "xs tac"),
            ar(x1 + 2, 128, x1 + 44, 128, "lbad w3", "ah-bad"), t(x1 + 2, 120, "เจาะ", "xs b tbad"),
            t(x1 + 4, 206, "ยกแขนเหนือศีรษะ · ยกหัวเตียงเล็กน้อย", "xs"),
            t(x1 + 4, 222, "ใช้ใน ICU/ลุกนั่งไม่ได้", "xs"),
            t(x1 + 4, 238, "น้ำไหลไปด้านหลัง ชั้นบาง → ใช้ US เสมอ", "xs b tms")]
    return fig("ท่าผู้ป่วยและแนวที่เจาะ",
               "**ท่ามาตรฐาน: นั่งตัวตรงโน้มไปข้างหน้าเล็กน้อย** แขนวางบนโต๊ะข้างเตียง — น้ำอิสระไหลลงไปรวมที่ **ด้านหลังส่วนล่าง** (posterior costophrenic recess) "
               "และ scapula เลื่อนออกด้านข้าง ช่องซี่โครงด้านหลังถ่างกว้างขึ้น · สไลด์: นั่ง → แนว **posterior/mid-scapular** · นอน → **mid-axillary line** "
               "(ลายมือกำกับ Recommend) · ระดับ: ต่ำกว่าขอบบนของน้ำ 1–2 ช่องซี่โครง แต่ไม่ต่ำกว่า ICS 8–9 ด้านหลัง เพราะกะบังลม ตับ และม้ามอยู่ตรงนั้น "
               "(ภาพ ICS 9 ในสไลด์มาจาก atlas — ปัจจุบันให้อัลตราซาวด์เลือกจุด)",
               svg(420, 278, "ท่านั่งโน้มตัวมองจากด้านหลัง และท่านอนหงายมองจากด้านข้าง พร้อมตำแหน่งเจาะ", *out))


# ───────────────────────────── 5. อัลตราซาวด์หาจุด
def thr_us():
    out = [rect(150, 6, 120, 18, "inkf", 5), t(210, 19, "หัว probe", "xs mid tpa b"),
           path("M150 24 L40 240 L380 240 L270 24 Z", "sk"),
           path("M132 60 L288 60 L300 84 L120 84 Z", "ms"), t(210, 77, "ผนังอก", "xs mid b"),
           path("M112 100 Q210 92 308 100 L346 212 Q300 160 210 176 Q120 192 74 212 Z", "wa"),
           t(210, 132, "น้ำ — สีดำ (anechoic)", "sm mid b twa"),
           path("M74 212 Q120 192 210 176 Q300 160 346 212", "lms w3"), t(352, 210, "กะบังลม", "xs b tms"),
           t(210, 224, "ตับ/ม้าม (ใต้กะบังลม)", "xs mid b"),
           ell(244, 152, 26, 9, "bx", -18), t(244, 168, "ปอดลอยในน้ำ", "xs mid"),
           line(210, 84, 210, 112, "lok w2"), line(204, 84, 216, 84, "lok w2"), line(204, 112, 216, 112, "lok w2"),
           t(222, 104, "ลึก ≥ 1 cm", "xs b tok"),
           rect(120, 84, 22, 140, "ruf ns", 0), rect(278, 84, 22, 140, "ruf ns", 0),
           t(131, 252, "เงาซี่โครง", "xs mid mu"), t(289, 252, "เงาซี่โครง", "xs mid mu"),
           t(10, 272, "ทำในท่าเดียวกับที่จะเจาะ · ดูตลอดการหายใจ · เจาะทันทีหลังมาร์ก", "xs b"),
           t(10, 288, "จุดที่กะบังลมขึ้นมาถึงตอนหายใจออก = ห้ามเจาะ", "xs b tbad")]
    return fig("อัลตราซาวด์ก่อนเจาะ — หาแอ่งน้ำที่ปลอดภัย",
               "สไลด์: **ใช้อัลตราซาวด์หรือภาพถ่ายรังสีหาตำแหน่งน้ำ** · BTS 2023 แนะนำให้ใช้อัลตราซาวด์ทุกครั้ง (ลด pneumothorax และการแทงโดนอวัยวะ) · "
               "น้ำเห็นเป็นสีดำระหว่างผนังอกกับปอด/กะบังลม · มองหาแอ่งที่ลึกพอ (≥ 1 cm ตลอดการหายใจ) ไม่มีปอดหรือกะบังลมขึ้นมาแตะ · "
               "เจาะในท่าเดิมทันทีหลังมาร์ก — ขยับตัวแล้วน้ำและอวัยวะเลื่อนจากจุดที่มาร์ก · ภาพแนวคิด ไม่ใช่ภาพอัลตราซาวด์จริง",
               svg(420, 296, "แผนภาพอัลตราซาวด์ทรวงอกแสดงน้ำ ปอด กะบังลม และเงาซี่โครง", *out))


# ───────────────────────────── 6. neurovascular bundle
def thr_nvb():
    out = [rect(10, 20, 64, 230, "sk", 0), t(42, 268, "ผิวหนัง/ไขมัน", "xs mid mu"),
           rect(74, 20, 120, 230, "bad", 0), t(134, 268, "intercostal 3 ชั้น", "xs mid"),
           rect(194, 20, 12, 230, "ac", 0), rect(206, 20, 90, 230, "wa", 0), t(251, 268, "น้ำ", "xs mid b twa"),
           rect(296, 20, 114, 230, "bx", 0), t(353, 268, "ปอด", "xs mid"),
           # ซี่โครงบน/ล่าง
           path("M70 26 L200 26 L200 82 Q170 86 150 70 L150 82 L70 82 Z", "ruf"), t(110, 52, "ซี่โครงบน", "xs b mid tpa"),
           path("M70 190 L200 190 L200 246 L70 246 Z", "ruf"), t(134, 222, "ซี่โครงล่าง", "xs b mid tpa"),
           # VAN ใต้ซี่โครงบน (ในร่อง costal groove)
           circ(168, 92, 7, "waf"), t(168, 96, "V", "xs mid b tpa"),
           circ(168, 108, 6, "badf"), t(168, 112, "A", "xs mid b tpa"),
           circ(168, 123, 5, "msf"), t(168, 127, "N", "xs mid b"),
           # collateral เล็ก ๆ เหนือซี่โครงล่าง
           circ(176, 182, 3, "badf"), t(214, 200, "collateral (เล็ก)", "xs mu"),
           # เข็มถูก
           ar(0, 176, 240, 176, "lok w3", "ah-ok"), t(4, 170, "✓ ชิดขอบบนซี่โครงล่าง", "xs b tok"),
           # เข็มผิด
           ar(0, 100, 150, 100, "lbad w2 da", "ah-bad"), t(4, 94, "✗ ใต้ซี่โครงบน", "xs b tbad"),
           t(214, 102, "V-A-N ในร่อง", "xs b"), t(214, 116, "costal groove", "xs"), t(214, 130, "ขอบล่างซี่โครง", "xs"),
           t(10, 12, "ภาพตัดตามยาว (บน = ศีรษะ) · ด้านหลังกึ่งกลางระหว่าง angle of rib กับแนวรักแร้", "xs mu")]
    return fig("ทำไมต้องแทงชิดขอบบนของซี่โครงล่าง",
               "เส้นเลือดและประสาท intercostal (**V-A-N** เรียงจากบนลงล่าง) วิ่งใน **costal groove ใต้ขอบล่างของซี่โครงบน** ระหว่างกล้ามเนื้อ internal กับ innermost · "
               "แทงชิด **ขอบบนของซี่โครงล่าง** จึงไกลจากมัดหลัก (เหลือแค่ collateral branch เล็ก) → ลดเลือดออก/hemothorax และปวดจากประสาท · "
               "**ใกล้กระดูกสันหลัง (ใน ~6–10 cm จากแนวกลาง) ห้ามเจาะ** เพราะหลอดเลือดยังไม่เข้าร่อง วิ่งคดเคี้ยวกลางช่อง และในผู้สูงอายุคดมากขึ้น",
               svg(420, 278, "ภาพตัดช่องซี่โครงแสดงมัดเส้นเลือดและประสาทใต้ซี่โครงบน และแนวเข็มที่ถูกต้องเหนือซี่โครงล่าง", *out))


# ───────────────────────────── 7. ขั้นตอน
def thr_steps():
    steps = [("1", "เตรียม + consent", "ยืนยันตัว · อธิบาย/ขอยินยอม · แพ้ยา · ค่าเลือด · V/S", "bx"),
             ("2", "ท่า + หาจุด", "นั่งโน้มตัว · US มาร์กจุด (ท่าเดิม)", "bx"),
             ("3", "ปลอดเชื้อ", "ล้างมือ ถุงมือ · ทาน้ำยา · ปูผ้า · ต่อสาย + 3-way", "ok"),
             ("4", "ยาชา", "ผิว → ใต้ผิว → parietal pleura · ดูดก่อนฉีด", "ac"),
             ("5", "แทงสาย", "90° ชิดขอบบนซี่โครง · ดูดเบา ๆ ขณะแทง", "ac"),
             ("6", "เห็นน้ำ", "ดันสายเข้า ถอยเข็ม · ปิด 3-way กันลมเข้า", "wa"),
             ("7", "เก็บ/ระบาย", "ส่งตรวจ · ระบาย ≤ 1–1.5 L · หยุดถ้าแน่น/ไอ", "wa"),
             ("8", "ถอด + ปิดแผล", "ถอดสาย · ปิด sterile dressing", "ok"),
             ("9", "เฝ้าระวัง", "V/S SpO₂ · เสียงหายใจ · แผล · CXR ถ้ามีอาการ", "ms")]
    out = []
    for k, (n, a, b, c) in enumerate(steps):
        y = 6 + 36 * k
        out += [rect(8, y, 404, 30, c, 7), circ(26, y + 15, 10, "inkf"), t(26, y + 19, n, "xs mid b tpa"),
                t(44, y + 19, a, "sm b"), t(150, y + 19, b, "xs")]
        if k < len(steps) - 1:
            out.append(line(26, y + 25, 26, y + 36, "ln"))
    return fig("ขั้นตอน thoracentesis ตามสไลด์",
               "เรียงตามสไลด์กลุ่ม 5: **Prepare/consent → Positioning → Identify location → Antiseptic → Local anesthesia → Catheter insertion → Drainage → Catheter removal + dressing → After care** · "
               "จุดที่ต้องทำให้ได้ทุกครั้ง: ดูดก่อนฉีดยาชา · ดูดเบา ๆ ขณะแทง (เห็นน้ำแล้วหยุดแทงลึกต่อ) · ปิด 3-way ทุกครั้งที่ถอดกระบอก เพื่อไม่ให้อากาศถูกดูดเข้าช่องอก",
               svg(420, 330, "ขั้นตอนการเจาะน้ำในช่องเยื่อหุ้มปอดเก้าขั้น", *out))


# ───────────────────────────── 8. ความดันในช่องอกขณะระบาย
def thr_pressure():
    X0, Y0, W, H = 52, 24, 340, 200
    def P(v, p):  # v ลิตร 0–2.5 · p cmH2O +5 … −30
        return X0 + v / 2.5 * W, Y0 + (5 - p) / 35 * H
    out = [line(X0, Y0, X0, Y0 + H, "ln"), line(X0, Y0 + H, X0 + W, Y0 + H, "ln")]
    for p in (0, -10, -20, -30):
        _, y = P(0, p)
        out += [line(X0 - 4, y, X0 + W, y, "lru da" if p else "lmu"), t(X0 - 8, y + 4, str(p), "xs end mu")]
    for v in (0.5, 1, 1.5, 2, 2.5):
        x, _ = P(v, 0)
        out += [t(x, Y0 + H + 16, str(v), "xs mid mu")]
    out += [t(X0 + W / 2, Y0 + H + 32, "ปริมาณที่ระบายออก (ลิตร)", "xs mid"),
            t(8, Y0 + 2, "cmH₂O", "xs mu")]
    _, y20 = P(0, -20)
    out += [rect(X0, y20, W, Y0 + H - y20, "bad ns", 0), t(P(1.55, 0)[0] + 4, y20 + 16, "< −20: เสี่ยงปอดบวมน้ำ", "xs b tbad")]
    norm = [P(v, 2 - 2.4 * v - (0.5 * (v - 1.2) ** 2 if v > 1.2 else 0)) for v in [i * 0.1 for i in range(26)]]
    trap = [P(v, 1 - 34 * v ** 1.25) for v in [i * 0.05 for i in range(14)] if 1 - 34 * v ** 1.25 > -30]
    out += [poly(norm, "lok w3"), poly(trap, "lbad w3")]
    xn, yn = norm[-1]
    out += [t(xn - 4, yn - 8, "ปอดขยายได้", "xs end b tok"),
            t(P(0.45, -27)[0] + 6, P(0.45, -27)[1], "trapped lung", "xs b tbad"),
            t(P(0.45, -27)[0] + 6, P(0.45, -27)[1] + 14, "ติดลบเร็ว + แน่นอก", "xs tbad"),
            line(P(1.5, 5)[0], Y0, P(1.5, 5)[0], Y0 + H, "lms w2 da"), t(P(1.5, 5)[0] + 4, Y0 + 12, "~1.5 L", "xs b tms")]
    return fig("ระบายมากแค่ไหน — ความดันในช่องอกตกลงเรื่อย ๆ",
               "ภาพแนวคิด (ค่าประมาณ) — ขณะระบาย ความดันในช่องเยื่อหุ้มปอดลดลง · ถ้า **ปอดขยายได้** ปอดพองเข้ามาแทนที่ ความดันลดช้า · "
               "ถ้า **ปอดขยายไม่ได้ (trapped lung)** ช่องว่างที่ไม่มีอะไรมาแทนทำให้ความดันติดลบเร็วมาก → ผู้ป่วย **แน่นอก/ไอ** (สัญญาณที่ต้องหยุด) "
               "และเสี่ยง re-expansion edema กับ pneumothorax ex vacuo · ตัวเลข **1–1.5 L ต่อครั้ง** (BTS) เป็นค่าปลอดภัยเมื่อไม่ได้วัดความดัน — อาการของผู้ป่วยสำคัญกว่าตัวเลข",
               svg(420, 262, "กราฟแนวคิดความดันในช่องเยื่อหุ้มปอดเทียบปริมาณที่ระบาย ระหว่างปอดขยายได้กับ trapped lung", *out))


# ───────────────────────────── 9. Re-expansion pulmonary oedema — Starling
def thr_rpe():
    out = []
    for k, (x0, ttl, tc) in enumerate(((8, "ก่อน: ปอดแฟบหลายวัน", "mu"), (216, "หลังระบายเร็ว/มาก", "tbad"))):
        out += [t(x0 + 98, 16, ttl, "sm b mid " + tc),
                rect(x0, 26, 196, 40, "sk", 6), t(x0 + 98, 44, "ช่องเยื่อหุ้มปอด", "xs mid b"),
                t(x0 + 98, 58, "≈ 0 cmH₂O" if k == 0 else "−20 ถึง −40 cmH₂O", "xs mid " + ("" if k == 0 else "tbad b")),
                rect(x0, 74, 196, 54, "bad" if k else "bx", 6), t(x0 + 98, 92, "หลอดเลือดฝอยปอด", "xs mid b"),
                t(x0 + 98, 108, "เลือดน้อย · O₂ ต่ำ" if k == 0 else "เลือดไหลกลับทันที", "xs mid"),
                t(x0 + 98, 121, "(ischemia)" if k == 0 else "(reperfusion)", "xs mid mu"),
                rect(x0, 136, 196, 40, "wa" if k else "bx", 6), t(x0 + 98, 154, "interstitium", "xs mid b"),
                t(x0 + 98, 168, "ปกติ" if k == 0 else "น้ำ + โปรตีนท่วม", "xs mid " + ("" if k == 0 else "twa b")),
                rect(x0, 184, 196, 40, "wa" if k else "bx", 6), t(x0 + 98, 202, "ถุงลม", "xs mid b"),
                t(x0 + 98, 216, "แฟบ surfactant ลด" if k == 0 else "น้ำท่วม → เสมหะฟองสีชมพู", "xs mid " + ("" if k == 0 else "tbad b"))]
    x = 216
    out += [t(x + 190, 44, "①", "sm b end tbad"), t(x + 190, 92, "②", "sm b end tbad"), t(x + 190, 202, "③", "sm b end tbad"),
            ar(x + 98, 128, x + 98, 140, "lwa w2", "ah-wa"), ar(x + 98, 176, x + 98, 188, "lwa w2", "ah-wa")]
    out += [t(8, 246, "① แรงดูด: ความดันรอบหลอดเลือดติดลบ → hydrostatic gradient ↑", "xs b"),
            t(8, 262, "② ผนังรั่ว: reperfusion → อนุมูลอิสระ + สารอักเสบ + ปอดถูกยืดเร็ว", "xs b"),
            t(8, 278, "③ surfactant ลดจากการแฟบนาน → ถุงลมแฟบง่าย น้ำเข้าง่าย", "xs b"),
            t(8, 296, "เสี่ยง: แฟบ > 3 วัน · ระบายเร็ว/มาก · ใช้แรงดูดสูง · อายุน้อย", "xs b tms")]
    return fig("Re-expansion pulmonary oedema — Starling forces เปลี่ยนสองทาง",
               "ปอดที่แฟบนานขาดเลือด ขาด O₂ และ surfactant ลดลง · เมื่อระบายเร็วจนปอดพองทันที **(1) ความดันรอบหลอดเลือดติดลบมาก** ดึงน้ำออกจาก capillary "
               "(hydrostatic gradient เพิ่ม) **(2) เลือดไหลกลับ (reperfusion)** ปล่อยอนุมูลอิสระและสารอักเสบ ผนัง capillary รั่ว น้ำที่ออกมาจึงมีโปรตีนสูง "
               "**(3) surfactant ต่ำ** ถุงลมจึงรับน้ำได้ง่าย → ไอ แน่นอก SpO₂ ตก เสมหะฟองชมพู crackles และฝ้าใหม่ **ข้างที่เจาะ** ภายในไม่กี่ชั่วโมง (ส่วนใหญ่ใน 1–2 ชม. ถึง 24 ชม.) · "
               "พบน้อย (< 1%) แต่ตายได้ · ป้องกัน: หยุดเมื่อมีอาการ ไม่เกิน ~1.5 L ไม่ใช้แรงดูดแรง",
               svg(420, 304, "กลไก re-expansion pulmonary edema เปรียบเทียบก่อนและหลังระบายน้ำ", *out))


# ───────────────────────────── 10. แยกภาวะแทรกซ้อน
def thr_comp():
    cols = [("Vasovagal", "ms", ["HR ↓ ช้า", "BP ↓", "ซีด เหงื่อ หน้ามืด", "ปอดฟังเท่าเดิม"], "นอนราบ ยกขา\n± atropine"),
            ("Pneumothorax", "bad", ["HR ↑ หอบ", "SpO₂ ↓", "เคาะโปร่ง", "เสียงหายใจหาย"], "CXR/US\nระบายถ้ามาก"),
            ("Hemothorax", "bad", ["HR ↑ (หดหลอดเลือด)", "BP ↓ ช้า ๆ", "ทึบเพิ่ม Hb ตก", "แผลซึมเลือด"], "chest drain\n± ผ่าตัด"),
            ("Re-expansion", "wa", ["ไอ แน่นอก", "SpO₂ ↓", "crackles ข้างเจาะ", "เสมหะฟองชมพู"], "O₂ ประคับประคอง\n± NIV/PEEP")]
    out = []
    for k, (h, c, signs, rx) in enumerate(cols):
        x = 6 + 104 * k
        out += [rect(x, 8, 100, 30, c, 6), t(x + 50, 28, h, "xs mid b")]
        for j, s in enumerate(signs):
            out += [t(x + 50, 58 + 18 * j, s, "xs mid")]
        out += [rect(x, 134, 100, 40, "ok", 6)]
        for j, s in enumerate(rx.split("\n")):
            out += [t(x + 50, 150 + 14 * j, s, "xs mid b tok")]
    out += [t(210, 196, "กุญแจแยก: ชีพจรช้า = vasovagal · ชีพจรเร็ว + เสียงหายใจหาย = ลม", "xs mid b"),
            t(210, 212, "ชีพจรเร็ว + ทึบเพิ่ม = เลือด · ไอหลังระบายเยอะ = ปอดบวมน้ำ", "xs mid b")]
    return fig("ระหว่าง/หลังเจาะ ผู้ป่วยแย่ลง — แยกสี่ภาวะจากชีพจรและเสียงปอด",
               "ลายมือในสไลด์: **Common = pneumothorax** · vasovagal reaction (**bradycardia**) · BP drop · **hyperresonance** · pulse ↑ tachycardia + vasoconstrict · "
               "re-expansion pulmonary edema · กลไก: vasovagal = กระตุ้น parasympathetic จากความกลัว/ปวด/แทง pleura → HR และ BP ตกพร้อมกัน · "
               "เสียเลือด = baroreceptor กระตุ้น sympathetic → HR เร็ว หลอดเลือดหด · pneumothorax = อากาศกั้นเสียงและสะท้อนการเคาะ",
               svg(420, 222, "ตารางภาพแยกภาวะแทรกซ้อนหลังเจาะน้ำในช่องเยื่อหุ้มปอดสี่ภาวะ", *out))


# ───────────────────────────── 11. หลอดส่งตรวจ
def thr_tubes():
    tubes = [("Syringe heparin", "ac", "pH (blood gas)", "ไล่ลมหมด\nส่งทันที"),
             ("EDTA (ม่วง)", "ms", "cell count/diff", "กันแข็งตัว\nนับเซลล์"),
             ("ขวดปลอดเชื้อ", "bx", "protein LDH glu\nalb ADA TG amy", "+ เลือดชุด\nเดียวกัน"),
             ("ขวด H/C", "bad", "aerobe/anaerobe", "+ Gram/AFB\nในขวดเปล่า"),
             ("ภาชนะใหญ่", "wa", "cytology", "≥ 25–50 mL\nยิ่งมากยิ่งดี")]
    out = [rect(150, 6, 120, 30, "inkf", 6), t(210, 26, "น้ำที่ดูดได้", "sm mid b tpa")]
    for k, (n, c, test, note) in enumerate(tubes):
        x = 6 + 82 * k
        cx = x + 39
        out += [ar(210, 36, cx, 62, "lmu", "ah-mu"),
                rect(x + 22, 64, 34, 70, c, 10), rect(x + 20, 58, 38, 10, "inkf", 3),
                t(cx, 152, n, "xs mid b")]
        for j, s in enumerate(test.split("\n")):
            out.append(t(cx, 170 + 13 * j, s, "xs mid tac"))
        for j, s in enumerate(note.split("\n")):
            out.append(t(cx, 206 + 13 * j, s, "xs mid mu"))
    out += [t(210, 246, "ส่ง serum protein · LDH · glucose · albumin เวลาเดียวกัน", "xs mid b"),
            t(210, 262, "หนองชัด: ไม่ต้องวัด pH (ต้องใส่สายอยู่แล้ว · ทำเครื่องเสีย)", "xs mid tbad")]
    return fig("หลอดส่งตรวจ — น้ำหนึ่งครั้งแบ่งไปห้าทาง",
               "**pH** ใส่ syringe heparin แบบ blood gas ไล่ลมหมด ปิดจุก ส่งทันที · **cell count** ใส่ EDTA · **ชีวเคมี** (protein, LDH, glucose, albumin, ADA, TG/cholesterol, amylase) ขวดปลอดเชื้อ "
               "+ เจาะเลือดส่ง protein/LDH/glucose/albumin พร้อมกันเพื่อคำนวณอัตราส่วน · **เพาะเชื้อ** ใส่ขวด hemoculture เพิ่มโอกาสพบเชื้อ (ร่วมกับขวดเปล่าสำหรับ Gram, AFB, TB culture/Xpert) · "
               "**cytology** ส่งปริมาณมาก (≥ 25–50 mL) · ชนิดหลอดตามแนวปฏิบัติทั่วไป (สไลด์ระบุเพียง specimen tube) — ตรวจกับห้องแล็บของโรงพยาบาล",
               svg(420, 270, "หลอดและภาชนะสำหรับส่งตรวจน้ำในช่องเยื่อหุ้มปอดแต่ละชนิด", *out))


# ───────────────────────────── 12. pH artefact
def thr_ph():
    X0, W = 30, 360
    def X(ph): return X0 + (ph - 6.8) / (7.8 - 6.8) * W
    out = [rect(X0, 40, W, 16, "sk", 8)]
    for ph in (7.0, 7.2, 7.4, 7.6):
        out += [line(X(ph), 36, X(ph), 60, "lmu"), t(X(ph), 74, "%.1f" % ph, "xs mid mu")]
    out += [rect(X0, 40, X(7.2) - X0, 16, "bad ns", 8), t((X0 + X(7.2)) / 2, 30, "< 7.2 → ใส่สายระบาย", "xs mid b tbad"),
            line(X(7.2), 26, X(7.2), 64, "lbad w3"),
            circ(X(7.6), 48, 6, "okf"), t(X(7.6), 30, "ปกติ ~7.6", "xs mid b tok"),
            circ(X(7.1), 48, 6, "inkf"), t(X(7.1), 92, "ค่าจริง 7.10", "xs mid b")]
    rows = [("ฟองอากาศในกระบอก", "CO₂ หนีออกจากน้ำ → pH สูงขึ้นปลอม", "lms", "ah-ms", 7.1, 7.32, "อ่านได้ 7.32 → พลาด empyema", "tms"),
            ("ยาชา lidocaine ปน", "lidocaine เป็นกรด → pH ต่ำลงปลอม", "lbad", "ah-bad", 7.4, 7.15, "ใส่สายโดยไม่จำเป็น", "tbad"),
            ("heparin มากเกิน", "heparin เป็นกรด + เจือจาง → pH ต่ำปลอม", "lbad", "ah-bad", 7.4, 7.18, "", "tbad"),
            ("ทิ้งไว้นาน", "เซลล์/เชื้อยังกิน glucose สร้างกรด → pH ↓ glucose ↓", "lbad", "ah-bad", 7.3, 7.12, "", "tbad")]
    for k, (a, b, lc, m, p0, p1, note, tc) in enumerate(rows):
        y = 116 + 44 * k
        out += [t(8, y, a, "sm b"), t(8, y + 15, b, "xs"),
                ar(X(p0), y + 26, X(p1), y + 26, lc + " w2", m)]
        if note:
            out.append(t(X(max(p0, p1)) + 8, y + 30, note, "xs b " + tc))
    return fig("วัด pH ให้ถูก — สิ่งที่ทำให้ค่าเพี้ยน",
               "น้ำในช่องเยื่อหุ้มปอดปกติเป็นด่าง (**pH ~7.6** มี bicarbonate สูงกว่าเลือด) · ค่า **< 7.2 ใน parapneumonic = ต้องใส่สายระบาย** จึงต้องวัดให้แม่น · "
               "เก็บแบบ blood gas: syringe heparin ไม่มีฟองอากาศ ปิดจุก ส่งเครื่อง blood gas ทันที · **ฟองอากาศ** ทำให้ CO₂ หนี pH สูงปลอม (พลาด empyema) · "
               "**lidocaine และ heparin เกิน** เป็นกรด ทำให้ pH ต่ำปลอม — ใช้ syringe ใหม่ ไม่ใช่อันที่ฉีดยาชา · ทิ้งไว้นาน เซลล์ยังเผาผลาญ glucose เป็นกรด · "
               "ตัวเลขลูกศรเป็นตัวอย่างแนวคิด",
               svg(420, 290, "แถบค่า pH ของน้ำในช่องเยื่อหุ้มปอด และปัจจัยที่ทำให้ค่าสูงหรือต่ำปลอม", *out))


# ───────────────────────────── 13. 5 ขั้นการอ่านผล
def thr_stepwise():
    steps = [("1", "ดูด้วยตา", "ใส ฟาง · เลือด · ขุ่น/หนอง · ขาวขุ่นเหมือนนม · กลิ่นเหม็น", "bx"),
             ("2", "Light's criteria", "transudate หรือ exudate · สงสัยหลอก → albumin gradient", "ac"),
             ("3", "Cell count + diff", "neutrophil · lymphocyte · eosinophil · RBC", "ms"),
             ("4", "pH · glucose · LDH", "ต่ำ/ต่ำ/สูง = อักเสบรุนแรง · ต้องระบายไหม", "bad"),
             ("5", "ตรวจพิเศษ", "ADA · cytology · TG/chol · Hct · amylase · Gram/culture", "wa")]
    out = []
    for k, (n, a, b, c) in enumerate(steps):
        y = 6 + 54 * k
        out += [rect(8, y, 404, 44, c, 8), circ(30, y + 22, 13, "inkf"), t(30, y + 27, n, "sm mid b tpa"),
                t(52, y + 19, a, "sm b"), t(52, y + 36, b, "xs")]
        if k < 4:
            out.append(ar(30, y + 35, 30, y + 54, "ln", "ah"))
    out += [t(210, 290, "ทุกขั้นต้องตอบคำถามเดียว: น้ำนี้มาจากกลไกอะไร และต้องระบายหรือไม่", "xs mid b")]
    return fig("อ่านผลน้ำห้าขั้นตามสไลด์",
               "โครงของสไลด์กลุ่ม 5: **Step 1 gross appearance → Step 2 Light's criteria → Step 3 cell count & differential → Step 4 pH, glucose, LDH → Step 5 special tests** · "
               "ขั้น 1–2 บอกกลไก (Starling หรืออักเสบ) · ขั้น 3–4 บอกชนิดและความรุนแรงของการอักเสบ · ขั้น 5 ยืนยันสาเหตุเฉพาะ (ตารางในสไลด์เป็นภาพ — ค่าจุดตัดอิง BTS 2023 และตำรา)",
               svg(420, 300, "ห้าขั้นของการแปลผลน้ำในช่องเยื่อหุ้มปอด", *out))


# ───────────────────────────── 14. รูปลักษณ์น้ำ
def thr_appear():
    items = [("ใส/เหลืองฟาง", "bx", "transudate ส่วนใหญ่", "หัวใจ ตับ ไต"),
             ("แดง/มีเลือด", "badf", "RBC > 100,000/µL", "มะเร็ง PE บาดเจ็บ\nHct ≥ 50% = hemothorax"),
             ("ขุ่น/หนอง", "ms", "เซลล์ + โปรตีนมาก", "empyema\nหนองชัด = ใส่สาย"),
             ("ขาวขุ่นเหมือนนม", "paf", "ไขมันสูง", "chylothorax\nหรือ pseudochylothorax"),
             ("เหม็นเน่า", "msf", "anaerobe", "empyema จาก anaerobe"),
             ("ดำ/น้ำตาล", "inkf", "พบน้อย", "Aspergillus · amoebic\nliver abscess แตก")]
    out = []
    for k, (a, c, b, d) in enumerate(items):
        col, row = k % 2, k // 2
        x, y = 8 + 208 * col, 8 + 92 * row
        out += [rect(x, y, 200, 84, "bx", 8), rect(x + 10, y + 12, 26, 60, c, 8)]
        if c == "paf":
            out.append(rect(x + 10, y + 12, 26, 60, "sk", 8))
        out += [t(x + 46, y + 26, a, "sm b"), t(x + 46, y + 42, b, "xs mu")]
        for j, s in enumerate(d.split("\n")):
            out.append(t(x + 46, y + 58 + 13 * j, s, "xs"))
    return fig("Step 1 — ดูด้วยตาก่อนส่งแล็บ",
               "สไลด์ Step 1 แสดงภาพ **turbid** และ **high lipid-rich effusion** (ลายมือ: **milky white**) · ดูข้างเตียงได้ทันที: เลือดปน แค่ RBC 5,000–10,000/µL ก็ดูแดงแล้ว "
               "จึงต้องวัด **Hct** ไม่ใช่ตัดสินด้วยตา · ขุ่นอาจเป็นเซลล์ (หนอง) หรือไขมัน (chyle) — **ปั่นแล้วส่วนบนใส = เซลล์ (empyema)** · ยังขุ่น = ไขมัน · "
               "หนองชัด/เหม็น ใส่สายระบายได้เลยโดยไม่ต้องรอ pH",
               svg(420, 282, "ลักษณะน้ำในช่องเยื่อหุ้มปอดด้วยตาหกแบบ และโรคที่นึกถึง", *out))


# ───────────────────────────── 15. Light's decision tree
def thr_light():
    out = [box(100, 6, 220, 40, "bx", "Pleural protein, LDH\n+ serum protein, LDH", "", fs=12),
           ar(210, 46, 210, 62, "ln", "ah"),
           rect(30, 62, 360, 74, "ac", 8),
           t(210, 80, "เข้าเกณฑ์ข้อใดข้อหนึ่ง?", "sm b mid tac"),
           t(48, 98, "① protein น้ำ/เลือด > 0.5", "xs b"),
           t(48, 113, "② LDH น้ำ/เลือด > 0.6", "xs b"),
           t(48, 128, "③ LDH น้ำ > 2/3 ของค่าสูงสุดปกติ (ULN) ในเลือด", "xs b"),
           ar(120, 136, 80, 158, "ln", "ah"), t(84, 150, "ไม่เลย", "xs end"),
           ar(300, 136, 340, 158, "ln", "ah"), t(334, 150, "≥ 1 ข้อ", "xs"),
           box(8, 158, 150, 44, "wa", "TRANSUDATE\nStarling เสีย", "b", fs=12),
           box(262, 158, 150, 44, "bad", "EXUDATE\nอักเสบ/ระบายอุด", "b", fs=12),
           ar(337, 202, 337, 218, "ln", "ah"),
           box(196, 218, 216, 52, "ms", "แต่ประวัติเป็นหัวใจล้มเหลว\nได้ยาขับปัสสาวะ · เกินเกณฑ์เล็กน้อย?", "", fs=11),
           ar(304, 270, 304, 286, "ln", "ah"),
           box(196, 286, 216, 44, "ms", "Albumin เลือด − น้ำ > 1.2 g/dL\n(หรือ protein gradient > 3.1)", "", fs=11),
           ar(196, 308, 160, 308, "lwa w2", "ah-wa"), t(156, 300, "= transudate จริง", "xs end b twa"),
           t(156, 316, "(false exudate)", "xs end twa"),
           t(8, 350, "ไวต่อ exudate ~98% แต่เรียก transudate ผิดเป็น exudate ~25%", "xs mu")]
    return fig("Step 2 — Light's criteria และ false exudate",
               "สไลด์: **exudate ถ้าเข้าอย่างน้อย 1 ข้อ · transudate ไม่เข้าเลย** · สงสัยว่าเป็น exudate หลอก → **serum albumin − pleural albumin > 1.2 g/dL ยืนยัน transudate** · "
               "ยาขับปัสสาวะดึงน้ำออกจากช่องเร็วกว่าโปรตีนและ LDH จึงทำให้น้ำ \"เข้มข้น\" จนเกินเกณฑ์ · ข้อ ③ ใช้ **ULN ของห้องแล็บ** (ไม่ใช่ LDH ของผู้ป่วย) · "
               "รายละเอียดสาเหตุแต่ละชนิดเรียนในคาบ 17 หัวข้อ Light's criteria",
               svg(420, 358, "แผนภูมิ Light's criteria แยก transudate กับ exudate และการตรวจ albumin gradient เมื่อสงสัย false exudate", *out))


# ───────────────────────────── 16. Cell differential
def thr_cell():
    groups = [("Neutrophil เด่น", "bad", "กระบวนการเฉียบพลัน", ["parapneumonic/empyema", "pancreatitis · PE", "TB ระยะแรก (วันแรก ๆ)"]),
              ("Lymphocyte > 50%", "ac", "เรื้อรัง/ภูมิคุ้มกันเซลล์", ["TB (ADA สูง)", "มะเร็ง · lymphoma", "chylothorax · หลัง CABG"]),
              ("Eosinophil > 10%", "ms", "มีลมหรือเลือดในช่อง", ["หลังเจาะ/pneumothorax", "hemothorax · ยา", "พยาธิ · EGPA · asbestos"])]
    out = []
    for k, (h, c, sub, causes) in enumerate(groups):
        x = 6 + 138 * k
        out += [rect(x, 8, 132, 46, c, 8), t(x + 66, 28, h, "xs mid b"), t(x + 66, 44, sub, "xs mid")]
        for j, s in enumerate(causes):
            out += [t(x + 66, 74 + 16 * j, s, "xs mid")]
    out += [line(6, 130, 414, 130, "lru"),
            t(8, 150, "WBC น้อย < 1,000/µL → เข้ากับ transudate (Case 1: 133/µL)", "xs b"),
            t(8, 166, "WBC > 10,000/µL + neutrophil → parapneumonic/empyema", "xs b"),
            t(8, 182, "Lymphocyte เด่น + mesothelial < 5% → สนับสนุน TB (เยื่อหุ้มถูกคลุมด้วย fibrin)", "xs b"),
            t(8, 198, "Macrophage/mesothelial เด่น = ไม่อักเสบ (เหมือนน้ำปกติ)", "xs mu")]
    return fig("Step 3 — เซลล์ชนิดไหนเด่น บอกกลไก",
               "ตาราง Step 3 ในสไลด์เป็นภาพ (อ่านไม่ได้) — สรุปจากตำรา/BTS 2023 · **neutrophil** ถูกเรียกมาที่การอักเสบเฉียบพลัน (แบคทีเรีย ตับอ่อน PE) · "
               "**lymphocyte** เด่นเมื่อการอักเสบเรื้อรังหรือเป็น cell-mediated immunity (TB) และมะเร็ง · **eosinophil** ตอบสนองต่อลมหรือเลือดในช่องเยื่อหุ้มปอด "
               "จึงพบบ่อยหลังเจาะซ้ำ — เป็นสาเหตุที่พบบ่อยที่สุด ไม่ใช่โรคใหม่",
               svg(420, 206, "ชนิดเซลล์เด่นในน้ำในช่องเยื่อหุ้มปอดและโรคที่นึกถึง", *out))


# ───────────────────────────── 17. pH/glucose ต่ำ
def thr_lowglu():
    causes = [("Complicated parapneumonic / empyema", "แบคทีเรีย + neutrophil กิน glucose แบบ anaerobic → lactate, CO₂ ค้าง", "bad"),
              ("Rheumatoid pleuritis", "เยื่อหุ้มหนาขัดการขนส่ง glucose เข้า → glucose ต่ำมาก < 30", "ms"),
              ("Tuberculous pleuritis", "เซลล์อักเสบจำนวนมากใช้ glucose · pH ต่ำเล็กน้อย", "ac"),
              ("Malignancy (ก้อนมาก)", "เซลล์มะเร็งใช้ glucose + ระบายกรดไม่ได้ → พยากรณ์แย่ pleurodesis ไม่ติด", "ac"),
              ("Esophageal rupture (Boerhaave)", "น้ำย่อย/น้ำลายเข้าช่อง → pH ต่ำมาก ~6 + amylase สูง", "bad"),
              ("Lupus pleuritis", "อักเสบ immune complex (glucose มักปกติกว่า RA)", "bx")]
    out = [t(8, 16, "pH < 7.2 · glucose < 60 mg/dL (3.3 mmol/L) · LDH > 1,000 U/L", "sm b tbad")]
    for k, (a, b, c) in enumerate(causes):
        y = 28 + 42 * k
        out += [rect(8, y, 404, 36, c, 6), t(16, y + 15, a, "xs b"), t(16, y + 29, b, "xs")]
    return fig("Step 4 — pH ต่ำ glucose ต่ำ LDH สูง: นึกถึงหกโรค",
               "ลายมือในสไลด์ Step 4 เขียน **Rheumatoid · complicated parapneumonic effusion · Boerhaave syndrome · pH ↓ parapneumonic** (ตารางเป็นภาพ) · "
               "กลไกร่วม: **มีเซลล์/เชื้อใช้ glucose มาก** แล้วสร้างกรด ร่วมกับ **เยื่อหุ้มอักเสบหนาจนกรดระบายออกและ glucose ซึมเข้าได้น้อย** · LDH สูงจากเซลล์ที่ตายแตก · "
               "ในบริบท parapneumonic ค่าเหล่านี้คือข้อบ่งชี้ใส่สาย (คาบ 17 หัวข้อ parapneumonic) · จุดตัดอิง BTS 2023/ตำรา",
               svg(420, 284, "สาเหตุของน้ำในช่องเยื่อหุ้มปอดที่ pH ต่ำ glucose ต่ำ และกลไก", *out))


# ───────────────────────────── 18. chylo vs pseudochylo vs empyema
def thr_chylo():
    cols = [("Chylothorax", "wa", ["thoracic duct ฉีก", "chylomicron เข้าช่อง", "TG > 110 mg/dL", "cholesterol < 200", "เป็นไม่นาน"], "ปั่นแล้วยังขุ่น"),
            ("Pseudochylothorax", "ms", ["น้ำค้างนานหลายปี", "เซลล์สลาย → cholesterol", "cholesterol > 200", "ผลึก cholesterol", "TB เก่า · RA · เยื่อหนา"], "ปั่นแล้วยังขุ่น"),
            ("Empyema", "bad", ["แบคทีเรีย", "neutrophil จำนวนมาก", "pH ↓ glucose ↓", "Gram/culture +", "ไข้"], "ปั่นแล้วส่วนบนใส")]
    out = []
    for k, (h, c, rows, spin) in enumerate(cols):
        x = 6 + 138 * k
        out += [rect(x, 8, 132, 28, c, 6), t(x + 66, 27, h, "xs mid b")]
        for j, s in enumerate(rows):
            out += [t(x + 66, 54 + 16 * j, s, "xs mid" + (" b" if j in (2, 3) else ""))]
        # หลอดปั่น
        tx = x + 50
        out += [rect(tx, 140, 32, 62, "bx", 6)]
        if k < 2:
            out.append(rect(tx + 2, 150, 28, 50, "sk", 5))
        else:
            out += [rect(tx + 2, 184, 28, 16, "ms", 4), rect(tx + 2, 150, 28, 32, "wa", 0)]
        out += [t(x + 66, 220, spin, "xs mid b " + ("tbad" if k == 2 else "tms"))]
    out += [t(210, 244, "TG 50–110 → ส่ง lipoprotein electrophoresis หา chylomicron", "xs mid"),
            t(210, 260, "TG < 50 แทบตัด chylothorax ออก", "xs mid")]
    return fig("น้ำขาวขุ่น — chylothorax · pseudochylothorax · empyema",
               "สไลด์ Step 1/5 มีภาพ **lipid-rich (milky white)** และลายมือคำว่า chylous/pseudochylous ใน Step 5 (อ่านไม่ชัด) · **chylothorax** = chyle จาก thoracic duct ที่ฉีก "
               "(มะเร็ง/lymphoma ผ่าตัด บาดเจ็บ) มี chylomicron → **TG > 110 mg/dL** · **pseudochylothorax** = น้ำค้างนานหลายปีในเยื่อหุ้มหนา เซลล์สลายปล่อย cholesterol → "
               "**cholesterol > 200 mg/dL**/ผลึก cholesterol TG ต่ำ · **ปั่น**: ความขุ่นจากเซลล์ (หนอง) ตกตะกอน ส่วนบนใส · ความขุ่นจากไขมันไม่ตกตะกอน",
               svg(420, 268, "เปรียบเทียบ chylothorax pseudochylothorax และ empyema พร้อมผลการปั่น", *out))


# ───────────────────────────── 19. Hct rule
def thr_hct():
    X0, W = 30, 360
    def X(r): return X0 + r * W
    out = [t(210, 16, "Hct น้ำ ÷ Hct เลือด", "sm b mid"),
           rect(X0, 30, W, 18, "sk", 9),
           rect(X0, 30, X(0.01) - X0 + 4, 18, "wa ns", 4),
           rect(X(0.5), 30, X0 + W - X(0.5), 18, "bad ns", 9),
           line(X(0.5), 24, X(0.5), 54, "lbad w3")]
    for r in (0, 0.25, 0.5, 0.75, 1.0):
        out += [t(X(r), 66, "%g" % r, "xs mid mu")]
    out += [t(X(0.5) + 6, 84, "≥ 0.5 = HEMOTHORAX", "xs b tbad"),
            t(X(0.5) + 6, 98, "→ chest drain ขนาดใหญ่", "xs tbad"),
            t(X(0.5) + 6, 112, "→ หาแหล่งเลือด/ผ่าตัด", "xs tbad"),
            t(X0, 84, "< 0.01 = แค่ \"เลือดปน\"", "xs b twa"),
            t(X0, 98, "ไม่สำคัญทางคลินิก", "xs twa"),
            t(X0, 112, "(เช่นเข็มถูกเส้นเลือดเล็ก)", "xs twa"),
            t(130, 140, "0.01–0.5 = bloody effusion: มะเร็ง PE TB หลังบาดเจ็บ", "xs mid")]
    out += [rect(8, 156, 404, 60, "bx", 8),
            t(16, 176, "ทำไมตาเชื่อไม่ได้: RBC เพียง 5,000–10,000/µL ก็ทำให้น้ำดูแดง", "xs b"),
            t(16, 192, "แต่เลือดจริงมี RBC ~5,000,000/µL → Hct น้ำแดง ๆ ส่วนมาก < 1%", "xs"),
            t(16, 208, "เลือดในช่องอกถูกปอดเคลื่อนไหวกวน → defibrinate ไม่ค่อยแข็งตัว", "xs mu")]
    return fig("Hemothorax — ใช้ Hct ไม่ใช่สีของน้ำ",
               "สไลด์ระบุ hemothorax ในข้อบ่งชี้ therapeutic (drainage of empyema or hemothorax) และภาวะแทรกซ้อน bleeding/haemothorax · "
               "เกณฑ์ **Hct ของน้ำ ≥ 50% ของ Hct เลือด = hemothorax** (ตำรา/BTS) → ใส่ chest drain ขนาดใหญ่ ประเมินเลือดออกต่อเนื่อง · "
               "น้ำที่ดูแดงส่วนใหญ่ Hct ต่ำมาก เป็นเพียง bloody effusion (มะเร็ง PE TB) · หลังเจาะ ถ้าน้ำใสกลายเป็นแดงขึ้นเรื่อย ๆ พร้อมชีพจรเร็ว = แทงโดน intercostal artery",
               svg(420, 224, "แถบอัตราส่วน Hct ของน้ำต่อเลือด แยกเลือดปนเล็กน้อยกับ hemothorax", *out))


# ───────────────────────────── 20. Case 1
def thr_case1():
    rows = [("Protein น้ำ/เลือด", 1.7 / 6.9, 0.5, "1.7 / 6.9 = 0.25"),
            ("LDH น้ำ/เลือด", 83 / 308, 0.6, "83 / 308 = 0.27"),
            ("LDH น้ำ ÷ (2/3 × LDH อ้างอิง)", 83 / 205.33, 1.0, "83 < 205 (สไลด์ใช้ 2/3 × 308)")]
    X0, W = 160, 230
    out = [t(8, 16, "Case 1 — ชาย 59 ปี HF + CKD V น้ำสองข้าง", "sm b")]
    for k, (a, v, cut, s) in enumerate(rows):
        y = 34 + 50 * k
        sc = W / (cut * 2)
        out += [t(8, y + 14, a, "xs b"), rect(X0, y + 2, W, 18, "sk", 4),
                rect(X0, y + 2, v * sc, 18, "wa ns", 4),
                line(X0 + cut * sc, y - 4, X0 + cut * sc, y + 26, "lbad w2"),
                t(X0 + cut * sc + 4, y - 4, "เกณฑ์ exudate", "xs tbad"),
                t(X0, y + 36, s, "xs")]
    out += [rect(8, 186, 404, 76, "wa", 8),
            t(16, 206, "ไม่เข้าเกณฑ์ข้อใดเลย → TRANSUDATE", "sm b twa"),
            t(16, 224, "สีเหลือง · WBC 133 · RBC 200 · ADA 2.5 · Gram ไม่พบเชื้อ · culture ไม่ขึ้น", "xs"),
            t(16, 240, "= cardiac pleural effusion จาก decompensated HF", "xs b"),
            t(16, 256, "WBC/LDH ต่ำ + ADA ต่ำ → ไม่คิดถึง TB pleuritis", "xs")]
    return fig("Case 1 ในสไลด์ — คำนวณ Light's criteria",
               "ผลจากสไลด์: pleural protein 1.7 / serum 6.9 g/dL · pleural LDH 83 / serum 308 U/L · ADA 2.5 U/L · ทุกอัตราส่วนต่ำกว่าเกณฑ์ → **transudate** "
               "เข้ากับหัวใจล้มเหลว (S3 gallop, crepitation, บวมทั้งตัว, cardiomegaly) · สไลด์คำนวณ 2/3 จาก LDH ในเลือดของผู้ป่วย (205) — "
               "เกณฑ์จริงใช้ **ULN ของห้องแล็บ** (เช่น ULN 250 → 167) ผลสรุปไม่เปลี่ยน · แถบสีฟ้าแสดงค่าของผู้ป่วยเทียบเส้นเกณฑ์สีแดง",
               svg(420, 270, "กราฟแท่งเทียบค่า Light's criteria ของผู้ป่วย Case 1 กับเกณฑ์ exudate", *out))
