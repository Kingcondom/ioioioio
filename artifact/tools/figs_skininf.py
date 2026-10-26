# -*- coding: utf-8 -*-
"""ภาพประกอบคาบ derm 26/10 Skin infection (อ.วรนิษฐ์) — ใช้ใน build_skininf.py
ทุกฟังก์ชันคืน fig(title, cap, svg) · กว้าง ≤ 420 · ใช้คลาสสีจาก svg.py เท่านั้น"""
from svg import *


# ───────────────────────────── 1. ชั้นผิวหนังกับระดับของการติดเชื้อ (ภาพหลักของคาบ)
def layers():
    W = 420
    rows = [  # (y, h, ชื่อชั้น, คลาสพื้น, โรคที่อยู่ชั้นนี้, คลาสข้อความโรค)
        (34, 26, "Epidermis", "sk", "Impetigo · Ecthyma", "tac"),
        (60, 30, "Upper dermis + superficial lymphatics", "ac", "Erysipelas", "tac"),
        (90, 36, "Deep dermis", "ms", "Cellulitis", "tms"),
        (126, 34, "Subcutaneous fat", "ms", "Cellulitis · Infective panniculitis", "tms"),
        (160, 30, "Fascia", "bad", "Necrotizing fasciitis", "tbad"),
        (190, 24, "Muscle", "bx", "", ""),
    ]
    out = [t(0, 14, "ลึกลงไปเท่าไร = โรคอะไร · ความลึกเป็นตัวกำหนดทั้งขอบรอยโรคและความเร็วที่ต้องรักษา", "xs i2")]
    for y, h, name, c, dis, dc in rows:
        out += [box(0, y, 216, h, c), t(6, y + h / 2 + 4, name, "xs b")]
        if dis:
            out += [t(226, y + h / 2 + 4, dis, "xs b " + dc)]
    # หมายเหตุ: ไม่วาดเส้นน้ำเหลืองซ้ำ เพราะชื่อชั้นระบุไว้แล้วและจะทับข้อความในกล่อง
    out += [t(0, 232, "ยิ่งลึก ยิ่งขอบไม่ชัด ยิ่งต้องรีบ — NF คือชั้นที่ลึกสุดและเป็นเหตุผลว่าทำไมต้องเข้าห้องผ่าตัด", "xs i2")]
    return fig("ความลึกของรอยโรค = ชื่อโรค",
               "**ใช้ภาพนี้เป็นแกนของคาบ** · *impetigo* อยู่แค่ **epidermis** จึงหายไม่เป็นแผลเป็น · "
               "*erysipelas* อยู่ **upper dermis** และกิน **superficial lymphatics** ทำให้ขอบ**ชัดและยกขึ้น** พร้อมไข้หนาวสั่น · "
               "*cellulitis* ลงถึง **deep dermis–subcutaneous** ขอบจึง**เบลอ** · "
               "*necrotizing fasciitis* ลงถึง **fascia** ซึ่งเลือดไปเลี้ยงน้อยและลุกลามเร็ว จึงเป็น**ภาวะฉุกเฉินทางศัลยกรรม**",
               svg(W, 244, "ชั้นผิวหนังและระดับความลึกของการติดเชื้อแต่ละโรค", *out))


# ───────────────────────────── 2. impetigo: non-bullous vs bullous
def impetigo():
    out = []
    # ซ้าย: non-bullous
    out += [t(76, 14, "Non-bullous ≈ 70%", "sm b mid tac"),
            circ(76, 60, 26, "sk"), circ(76, 60, 26, "lac"),
            t(76, 54, "honey-", "xs mid b tms"), t(76, 66, "yellow crust", "xs mid b tms"),
            ar(76, 94, 76, 110, "lac", "ah-ac"),
            t(76, 126, "vesicle แตก → ซึม", "xs mid i2"),
            t(76, 140, "→ ตกสะเก็ดสีน้ำผึ้ง", "xs mid i2")]
    # ขวา: bullous
    out += [t(300, 14, "Bullous ≈ 30%", "sm b mid tms"),
            ell(300, 58, 30, 20, "ms"), ell(300, 58, 30, 20, "lms"),
            t(300, 62, "bulla", "xs mid b tms"),
            ar(300, 84, 300, 102, "lms", "ah-ms"),
            t(300, 118, "staphylococcal toxin", "xs mid b tms"),
            t(300, 132, "แยกชั้นใน epidermis", "xs mid i2"),
            t(300, 146, "แตกแล้วเหลือ erosion", "xs mid i2")]
    out += [line(188, 24, 188, 152, "lru da")]
    out += [t(4, 176, "เชื้อเดียวกัน: S. aureus (± S. pyogenes)", "xs i2"),
            t(4, 190, "ต่างกันที่มี exotoxin แยกชั้นผิวหรือไม่", "xs i2")]
    return fig("Impetigo สองรูปแบบ",
               "สองรูปแบบนี้มาจาก**เชื้อเดียวกัน** ต่างกันที่ **exotoxin** · แบบ bullous เกิดเมื่อ *S. aureus* สร้าง toxin "
               "ที่ย่อยรอยต่อระหว่างเซลล์ใน epidermis จึงเกิด **bulla** ก่อนแตกเป็น **erosion** · "
               "ทั้งคู่ตื้นแค่ epidermis จึง **non-scarring** — ต่างจาก **ecthyma** ที่ลึกถึง dermis แล้ว**เป็นแผลเป็น**",
               svg(420, 200, "เปรียบเทียบ impetigo แบบ non-bullous กับ bullous", *out))


# ───────────────────────────── 3. ขอบรอยโรค: erysipelas vs cellulitis
def border():
    out = [t(4, 14, "มองจากด้านบน", "xs b i2"), t(4, 130, "ตัดขวาง", "xs b i2")]
    # ซ้าย erysipelas: ขอบคม
    out += [t(96, 32, "Erysipelas", "sm b mid tac"),
            circ(96, 78, 32, "ac"), circ(96, 78, 32, "lac w3"),
            t(96, 82, "ขอบคม", "xs mid b tac"),
            box(46, 152, 100, 12, "ac"), t(96, 178, "upper dermis", "xs mid i2"),
            t(96, 192, "ขอบยกขึ้นคลำได้", "xs mid b tac")]
    # ขวา cellulitis: ขอบเบลอ
    out += [t(312, 32, "Cellulitis", "sm b mid tms"),
            circ(312, 78, 34, "ms"), circ(312, 78, 34, "lms da"),
            t(312, 82, "ขอบเบลอ", "xs mid b tms"),
            box(258, 152, 108, 26, "ms"), t(312, 192, "deep dermis–subcut", "xs mid i2")]
    out += [line(204, 26, 204, 200, "lru da")]
    out += [t(4, 218, "คำถามข้างเตียง: ลากนิ้วจากผิวปกติเข้าหารอยโรค", "xs i2"),
            t(4, 232, "แล้วถามตัวเองว่า “สะดุดขอบ” ไหม", "xs i2")]
    return fig("ขอบรอยโรคบอกความลึก",
               "**ขอบคมและยกขึ้น = erysipelas** เพราะการอักเสบจำกัดอยู่ใน **upper dermis** และแพร่ไปตาม "
               "**superficial lymphatics** ซึ่งมีผนังกั้น ทำให้ขอบเขตชัด · "
               "**ขอบเบลอ = cellulitis** เพราะอยู่ใน **deep dermis และชั้นไขมัน** ที่เนื้อเยื่อหลวม การอักเสบจึงค่อย ๆ จางออก "
               "ไม่มีขอบให้คลำ · ข้างเตียงให้ใช้นิ้วลากเข้าหารอยโรคแล้วถามตัวเองว่าสะดุดขอบหรือไม่",
               svg(420, 244, "เปรียบเทียบขอบรอยโรคของ erysipelas กับ cellulitis ทั้งมองจากบนและตัดขวาง", *out))


# ───────────────────────────── 4. folliculitis → furuncle → carbuncle
def follicle():
    def unit(x, label, cy, r, n, c, lab=False):
        tc = "tac" if c == "ac" else "tms" if c == "ms" else "tbad"
        o = [t(x + 46, 16, label, "sm b mid " + tc)]
        o += [box(x, 24, 92, 16, "sk"), t(x + 46, 36, "epidermis", "xs mid")]
        o += [box(x, 40, 92, 62, "bx")]
        if lab:
            o += [t(x + 46, 97, "dermis", "xs mid mu")]
        for i in range(n):
            cx = x + 46 + (i - (n - 1) / 2) * 25
            o += [line(cx, 28, cx, cy - r, "lmu"), circ(cx, cy, r, c)]
        return o
    # ยิ่งขวา ยิ่งลึก (cy มากขึ้น) และยิ่งใหญ่ (r มากขึ้น)
    out = unit(6, "Folliculitis", 50, 6, 1, "ac", lab=True)
    out += unit(154, "Furuncle", 68, 13, 1, "ms") + [t(200, 90, "pus", "xs mid b tms")]
    out += unit(302, "Carbuncle", 72, 11, 3, "bad") + [t(348, 92, "pus หลายช่อง", "xs mid b tbad")]
    out += [ar(100, 66, 150, 66, "lmu", "ah-mu"), ar(248, 66, 298, 66, "lmu", "ah-mu")]
    out += [t(6, 128, "ลึกขึ้น + รวมหลายรูขุมขน = ชื่อเปลี่ยน", "xs i2"),
            t(6, 142, "และการรักษาเปลี่ยนจากยาทาเป็นกรีดระบาย", "xs i2")]
    return fig("Folliculitis → furuncle → carbuncle",
               "ทั้งสามอย่างคือเรื่องเดียวกันที่**ลึกลงและกว้างขึ้น** · **folliculitis** อักเสบแค่ปากรูขุมขน ใช้ยาทาได้ · "
               "**furuncle (ฝี)** การอักเสบลงไปถึงฐานรูขุมขนและเกิดหนองเป็นโพรง จึงเริ่ม**คลำได้นุ่มตรงกลาง (fluctuant)** · "
               "**carbuncle** คือหลายรูขุมขนติดกันเป็นกลุ่ม มีหนองหลายช่อง · "
               "เมื่อใดที่มี **fluctuance** การรักษาหลักเปลี่ยนเป็น **incision and drainage** ไม่ใช่ยาอย่างเดียว",
               svg(420, 154, "ลำดับความลึกจาก folliculitis เป็น furuncle และ carbuncle", *out))


# ───────────────────────────── 5. necrotizing fasciitis — สัญญาณและเวลา
def nf():
    out = [t(4, 12, "สัญญาณที่ต้องจับให้ได้", "sm b tbad")]
    items = [("Pain out of proportion", "ปวดมากเกินกว่าที่ตาเห็น ← สำคัญที่สุด", "bad"),
             ("Rapid progression", "ลุกลามเป็นชั่วโมง ไม่ใช่เป็นวัน", "bad"),
             ("Crepitus", "คลำได้กรอบแกรบ = แก๊สในเนื้อเยื่อ", "ms"),
             ("Hemorrhagic bullae", "ตุ่มน้ำมีเลือด ผิวคล้ำ", "ms"),
             ("Systemic toxicity", "ไข้ ความดันต่ำ สับสน", "ms")]
    y = 26
    for name, why, c in items:
        out += [box(4, y, 164, 24, c), t(10, y + 16, name, "xs b"), t(176, y + 16, why, "xs i2")]
        y += 28
    out += [line(4, y + 4, 412, y + 4, "lru da")]
    out += [t(4, y + 24, "สิ่งที่ต้องทำ — เรียงตามเวลา", "sm b tbad")]
    steps = [("สงสัย", "อย่ารอผลตรวจ", "ms"), ("ปรึกษาศัลยกรรม", "surgical exploration", "bad"),
             ("IV ยาฆ่าเชื้อกว้าง", "vanco + pip-tazo", "ac"),
             ("Debridement", "ตัดเนื้อตายซ้ำได้", "bad")]
    x = 4
    yy = y + 34
    for i, (nm, sub, c) in enumerate(steps):
        out += [box(x, yy, 92, 44, c), t(x + 46, yy + 18, nm, "xs mid b"), t(x + 46, yy + 32, sub, "xs mid")]
        if i < len(steps) - 1:
            out += [ar(x + 94, yy + 22, x + 100, yy + 22, "lbad", "ah-bad")]
        x += 102
    out += [t(4, yy + 62, "CT/MRI ช่วยยืนยันได้ แต่ห้ามให้การรอผลภาพทำให้การผ่าตัดช้าลง", "xs i2 b tbad")]
    return fig("Necrotizing fasciitis — จับสัญญาณแล้วนับเวลา",
               "โรคนี้แพ้ที่ **เวลา** ไม่ใช่ที่ยา · อาการนำที่ไวที่สุดคือ **ปวดเกินกว่าที่ตาเห็น** เพราะการติดเชื้อทำลาย "
               "**fascia และเส้นประสาทใต้ผิว** ก่อนที่ผิวด้านบนจะเปลี่ยนสี จึงมีช่วงที่คนไข้ปวดทรมานแต่ผิวยังดูเกือบปกติ · "
               "**crepitus และ hemorrhagic bullae มาช้า** ถ้ารอให้ครบจะสายเกินไป · "
               "การวินิจฉัยที่แน่นอนคือ **surgical exploration** ไม่ใช่ภาพถ่าย",
               svg(420, y + 110, "สัญญาณเตือนของ necrotizing fasciitis และลำดับการรักษาตามเวลา", *out))


# ───────────────────────────── 6. Wood lamp — erythrasma
def wood():
    out = [box(0, 20, 120, 54, "bx", None), t(60, 42, "Corynebacterium", "xs mid b"), t(60, 56, "minutissimum", "xs mid b"),
           ar(122, 46, 150, 46, "lac", "ah-ac", "สร้าง"),
           box(152, 20, 110, 54, "ac"), t(207, 42, "Coproporphyrin", "xs mid b tac"), t(207, 56, "III", "xs mid b tac"),
           ar(264, 46, 292, 46, "lwa", "ah-wa"),
           box(294, 20, 126, 54, "wa"), t(357, 36, "Wood lamp", "xs mid b twa"), t(357, 50, "UV 365 nm", "xs mid twa"),
           t(357, 64, "→ coral-red", "xs mid b tbad")]
    out += [t(0, 98, "ตำแหน่งที่ต้องส่องเสมอ", "sm b i2")]
    out += [box(0, 108, 200, 26, "sk"), t(8, 125, "ซอกนิ้วเท้า 4–5 (พบบ่อยสุด)", "xs b"),
            box(210, 108, 210, 26, "sk"), t(218, 125, "ขาหนีบ รักแร้ ใต้ราวนม", "xs b")]
    out += [t(0, 156, "เรืองแสงสีแดงปนส้ม = erythrasma ไม่ใช่เชื้อรา → ยาที่ใช้คือยาต้านแบคทีเรีย", "xs i2 b")]
    return fig("ทำไม erythrasma เรืองแสงสีแดงส้ม",
               "*Corynebacterium minutissimum* สร้าง **coproporphyrin III** ซึ่งเป็นสาร **fluorophore** "
               "พอโดนแสง **Wood lamp (UV ~365 nm)** จึงเปล่งแสงกลับมาเป็น **coral-red** · "
               "ประโยชน์จริงคือ**แยกจากเชื้อรา** ที่หน้าตาคล้ายกันมากในซอกพับ เพราะถ้าเป็น erythrasma "
               "ต้องให้ยาต้านแบคทีเรีย (erythromycin, clindamycin, benzoyl peroxide) ไม่ใช่ยาฆ่าเชื้อรา",
               svg(420, 168, "กลไกการเรืองแสงสีแดงส้มของ erythrasma ใต้ Wood lamp", *out))


# ───────────────────────────── 7. HSV vs zoster — รูปแบบการกระจาย
def hsvvzv():
    out = [t(0, 12, "HSV — grouped vesicles", "sm b tac"),
           ell(70, 62, 46, 30, "ac"), ell(70, 62, 46, 30, "lac")]
    for dx, dy in ((-18, -8), (-4, 4), (12, -6), (24, 6), (2, -12), (18, 10)):
        out += [circ(70 + dx, 62 + dy, 6, "wa")]
    out += [t(70, 106, "กลุ่มตุ่มน้ำบนพื้นแดง", "xs mid i2"), t(70, 120, "ตำแหน่งเดิมซ้ำ ๆ", "xs mid b tac")]
    out += [line(150, 24, 150, 164, "lru da")]
    out += [t(176, 12, "Zoster — dermatomal", "sm b tbad")]
    out += [path("M176,46 C230,34 290,40 330,62", "lbad w3")]
    for i in range(9):
        x = 180 + i * 18
        y = 46 - 10 * (1 - abs(i - 4) / 4.5) + i * 1.6
        out += [circ(x, y + 6, 5, "bad")]
    out += [t(254, 100, "แถบเดียว ข้างเดียว", "xs mid b tbad"), t(254, 114, "ไม่ข้ามแนวกลางลำตัว", "xs mid i2"),
            t(254, 132, "ปวดนำมาก่อนผื่นเป็นวัน", "xs mid b tms")]
    out += [t(0, 184, "คำถามเดียวที่แยกได้: รอยโรคเป็น “กลุ่ม” หรือ “แถบตาม dermatome”", "xs i2")]
    return fig("HSV กับ zoster — ดูการกระจาย ไม่ใช่ดูตุ่ม",
               "ตุ่มน้ำของทั้งสองโรคหน้าตา**เหมือนกัน** เพราะเป็น herpesvirus ทั้งคู่ · ที่แยกได้คือ**การกระจาย** · "
               "**HSV** อยู่ที่ **mucocutaneous junction** เป็น**กลุ่มเล็ก ๆ** และกลับมาที่**ตำแหน่งเดิม**เพราะไวรัสหลับอยู่ใน "
               "ganglion ที่เลี้ยงผิวบริเวณนั้น · **zoster** ออกเป็น**แถบเดียวข้างเดียวตาม dermatome** และ**ไม่ข้ามแนวกลาง** "
               "เพราะไวรัสหลับใน **dorsal root ganglion เดียว** แล้ววิ่งออกมาตามเส้นประสาทเส้นนั้นเส้นเดียว",
               svg(340, 196, "เปรียบเทียบการกระจายของรอยโรค HSV แบบกลุ่ม กับ zoster แบบแถบ dermatome", *out))


# ───────────────────────────── 8. VZV: latency → reactivation
def zoster():
    out = [box(0, 24, 96, 40, "sk"), t(48, 42, "Varicella", "xs mid b"), t(48, 56, "(ติดครั้งแรก)", "xs mid"),
           ar(98, 44, 126, 44, "lmu", "ah-mu"),
           box(128, 24, 110, 40, "ac"), t(183, 40, "หลับใน", "xs mid b tac"), t(183, 54, "dorsal root ganglion", "xs mid b tac"),
           ar(240, 44, 268, 44, "lbad", "ah-bad", "ภูมิตก"),
           box(270, 24, 110, 40, "bad"), t(325, 40, "Zoster", "xs mid b tbad"), t(325, 54, "(กลับมาอีก)", "xs mid tbad")]
    out += [t(0, 92, "ตัวกระตุ้นให้กลับมา", "sm b i2")]
    for i, s in enumerate(["อายุมากขึ้น", "ยากดภูมิ", "มะเร็ง / HIV", "ความเครียด เจ็บป่วย"]):
        out += [pill(4 + i * 100, 102, s, "ms", "xs b mid tms", 92)]
    out += [t(0, 150, "ไวรัสเดินกลับออกมาตามเส้นประสาทรับความรู้สึก", "xs b i2"),
            ar(10, 164, 370, 164, "lbad", "ah-bad"),
            t(190, 182, "จึงปวดก่อนมีผื่น และผื่นออกเฉพาะผิวที่เส้นประสาทนั้นเลี้ยง", "xs mid i2")]
    return fig("ทำไม zoster ออกเป็นแถบและปวดก่อนผื่น",
               "หลังเป็น**สุกใส** ไวรัสไม่ได้หายไป แต่ไป**หลับใน dorsal root ganglion** · "
               "เมื่อภูมิคุ้มกันระดับเซลล์ตกลง ไวรัสจึง**กลับมาแบ่งตัวและเดินออกมาตาม axon ของเส้นประสาทรับความรู้สึก** · "
               "สองผลที่ตามมาคือ **ปวด/แสบ/ซ่านำมาก่อนผื่นเป็นวัน** (ไวรัสทำลายเส้นประสาทก่อนถึงผิว) และ "
               "**ผื่นออกเฉพาะ dermatome ของ ganglion นั้น** · ความเสียหายของเส้นประสาทที่ค้างอยู่คือที่มาของ "
               "**postherpetic neuralgia (ปวดเกิน 90 วัน)**",
               svg(400, 194, "วงจรจาก varicella ไปหลับใน ganglion แล้วกลับมาเป็น zoster", *out))


# ───────────────────────────── 9. HZO และ Hutchinson's sign
def hzo():
    out = [t(0, 12, "Trigeminal nerve (CN V) — แขนง V1", "sm b tac")]
    out += [path("M40,120 C70,70 120,44 180,40", "lac w3", None, None),
            t(44, 136, "ganglion", "xs tac"),
            box(176, 26, 96, 28, "ac"), t(224, 44, "V1 ophthalmic", "xs mid b tac"),
            box(176, 62, 96, 26, "sk"), t(224, 78, "V2 maxillary", "xs mid"),
            box(176, 96, 96, 26, "sk"), t(224, 112, "V3 mandibular", "xs mid")]
    out += [t(286, 20, "V1 เลี้ยงอะไร", "xs b i2")]
    for i, s in enumerate(["หน้าผาก", "เปลือกตาบน", "ตา (cornea)", "ปลายจมูก"]):
        out += [pill(284, 30 + i * 24, s, "ac", "xs b mid tac", 128)]
    out += [line(0, 146, 420, 146, "lru da")]
    out += [t(0, 168, "Hutchinson's sign", "sm b tbad"),
            circ(40, 196, 14, "bad"), t(40, 200, "!", "sm mid b tbad"),
            t(62, 192, "ตุ่มน้ำที่ปลายจมูก", "xs b"),
            t(62, 206, "= แขนง nasociliary ถูก involve", "xs i2"),
            t(62, 220, "แขนงเดียวกันเลี้ยง cornea → เสี่ยงตาเสีย", "xs b tbad"),
            box(0, 234, 420, 26, "bad"), t(8, 251, "เจอ Hutchinson's sign → ส่งจักษุแพทย์ด่วน ไม่ใช่รอดูอาการ", "xs b")]
    return fig("Herpes zoster ophthalmicus และ Hutchinson's sign",
               "**V1 (ophthalmic)** แตกแขนงเป็น **nasociliary nerve** ซึ่งเลี้ยงทั้ง **ปลายจมูก** และ **cornea** · "
               "ดังนั้นตุ่มน้ำที่ปลายจมูก (**Hutchinson's sign**) จึงเป็นหลักฐานว่าแขนงที่เลี้ยงตาถูก involve ไปด้วย "
               "และทำนายการเกิด **keratitis/uveitis** ได้ · นี่คือเหตุผลที่สัญญาณเล็ก ๆ ที่ปลายจมูกเปลี่ยนการดูแลทั้งหมด "
               "จาก “ให้ยาแล้วนัดดูอาการ” เป็น **ส่งจักษุแพทย์ด่วน**",
               svg(420, 272, "แขนงของ trigeminal nerve กับความหมายของ Hutchinson's sign", *out))


# ───────────────────────────── 10. ชนิดของหูดกับ HPV type
def warts():
    rows = [("Verruca vulgaris", "common wart", "มือ นิ้ว เข่า", "2, 4", "ac"),
            ("Verruca plana", "flat wart", "ใบหน้า หลังมือ แข้ง", "3, 10", "ac"),
            ("Verruca plantaris", "plantar wart", "ฝ่าเท้า", "1", "ms"),
            ("Filiform wart", "เป็นติ่งยื่น", "หน้า คอ เปลือกตา", "1, 2", "sk"),
            ("Butcher's wart", "อาชีพสัมผัสเนื้อสัตว์", "มือ", "7", "sk"),
            ("Epidermodysplasia", "verruciformis · เสี่ยง SCC", "ผิวที่โดนแดด", "5, 8", "bad")]
    out = [t(10, 12, "ชื่อ", "xs b mu"), t(166, 12, "ลักษณะ / บริบท", "xs b mu"),
           t(286, 12, "ตำแหน่ง", "xs b mu"), t(384, 12, "HPV", "xs b mu")]
    y = 20
    for nm, feat, site, hpv, c in rows:
        out += [box(4, y, 412, 28, c),
                t(10, y + 18, nm, "xs b"), t(166, y + 18, feat, "xs"),
                t(286, y + 18, site, "xs"), t(384, y + 18, hpv, "xs b tac")]
        y += 30
    out += [t(4, y + 20, "จุดที่ออกสอบ: black puncta ใน common wart = thrombosed capillaries", "xs i2"),
            t(4, y + 34, "mosaic pattern = plantar wart ที่โตมาเชื่อมกัน", "xs i2"),
            t(4, y + 52, "Histology hallmark: koilocytosis (+ hypergranulosis, papillomatosis)", "xs b tac")]
    return fig("หูดแต่ละชนิดกับ HPV type",
               "ตารางนี้คือชุดตัวเลขที่ข้อสอบชอบถามตรง ๆ · เคล็ดการจำคือ **ยิ่งเลขน้อยยิ่งลงที่เท้า** "
               "(HPV 1 = plantar) และ **HPV 5, 8 = epidermodysplasia verruciformis** ซึ่งเป็นกลุ่มเดียวที่ "
               "**เสี่ยงกลายเป็น squamous cell carcinoma** จึงต้องกันแดดและคัดกรองมะเร็ง · "
               "ภาพทางพยาธิที่เป็น hallmark ของ HPV ทุกชนิดคือ **koilocyte** (เซลล์ที่มีวงใสรอบนิวเคลียส)",
               svg(420, y + 64, "ตารางชนิดของหูดกับ HPV type ตำแหน่ง และลักษณะเฉพาะ", *out))
