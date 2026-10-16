# -*- coding: utf-8 -*-
"""ภาพประกอบ + กลไก คาบ id 25/9 Septicemia and antibiotic usage (ใส่ด้วย apply_figs.py)"""
import math
from svg import *

SET, LEC = "id", "25/9"

_SIGNS = """#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ไข้ หรือ ตัวเย็น < 36 °C** | IL-1, IL-6, TNF-α → **PGE₂ ที่ hypothalamus** → ตั้งจุดอุณหภูมิสูงขึ้น · ตัวเย็นเกิดเมื่อร่างกายตอบสนองไม่ไหว (ผู้สูงอายุ ช็อกหนัก) | **ตัวเย็นพยากรณ์แย่กว่าไข้** · ผู้สูงอายุและผู้ภูมิต่ำอาจไม่มีไข้เลย |
| **ชีพจรเร็ว** | ไข้เพิ่มความต้องการ O₂ + หลอดเลือดขยายและน้ำรั่ว → เลือดกลับหัวใจลด MAP ตก → **baroreceptor กระตุ้น sympathetic** | ยังเร็วหลังให้น้ำและลดไข้แล้ว → ยังขาดปริมาตรหรือยังช็อก |
| **หายใจเร็ว (RR ≥ 22, PaCO₂ < 32)** | **lactic acidosis → หายใจชดเชยไล่ CO₂** · cytokine กระตุ้นศูนย์หายใจ · ปอดมีน้ำจาก capillary leak | มักเป็นสัญญาณแรกที่ถูกมองข้าม → นับ RR ให้ครบ 1 นาที |
| **WBC สูง ต่ำ หรือ band > 10%** | cytokine (G-CSF) ดึง neutrophil ออกจากไขกระดูกเร็วจนตัวอ่อน (band) ออกมาด้วย · **ต่ำ** เมื่อถูกใช้ที่แหล่งติดเชื้อเร็วกว่าสร้าง | **WBC ต่ำพยากรณ์แย่** · เคยได้เคมีบำบัด → คิดถึง neutropenic sepsis |
| **สับสน ซึม (GCS ↓)** | cytokine + เลือดไปสมองลด + blood–brain barrier รั่ว → **septic encephalopathy** | ผู้สูงอายุสับสนเฉียบพลัน → คัดกรอง sepsis เสมอ · แยก hypoglycemia, stroke |
| **ผิวลาย (mottling) · CRT > 3 วินาที** | microthrombi + ร่างกายหดหลอดเลือดผิวหนังเพื่อเก็บเลือดไว้ให้อวัยวะสำคัญ → ผิวขาดเลือดก่อน | บอก hypoperfusion ได้ **ก่อนความดันตก** · ใช้ติดตามการกู้ชีพ (หัวข้อ 5) |
| **ปัสสาวะ < 0.5 mL/kg/h** | MAP ตก เลือดไปไตลด + การอักเสบทำร้ายท่อไตโดยตรง (septic AKI) | เป้าหมายการกู้ชีพที่วัดได้ทุกชั่วโมง |"""

_TROPIC = """#### กลไก: ทำไมโรคเขตร้อนแต่ละโรคมีอาการเฉพาะตัว
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Melioidosis: ฝีหลายแห่ง ฝีตับ/ม้าม** | *B. pseudomallei* **อยู่รอดและแบ่งตัวใน macrophage** → ลอยไปตามเลือดแล้วตั้งรกรากเป็นฝีหลายอวัยวะ · เบาหวานทำให้ neutrophil ฆ่าเชื้อได้น้อยลง | ไข้ + ฝีหลายแห่งในชาวนาเบาหวาน → **อัลตราซาวนด์หาฝีตับ/ม้ามเสมอ** |
| **Melioidosis: safety pin** | เชื้อติดสีเข้มที่สองปลายเซลล์ (bipolar staining) | เห็นจาก Gram stain ได้เร็ว ก่อนผลเพาะเชื้อ |
| **Lepto: ปวดน่องมาก** | เชื้อเข้ากล้ามเนื้อ → **myositis** (CPK ขึ้นได้) | กดเจ็บน่องชัด + ประวัติลุยน้ำ → นึกถึง lepto |
| **Lepto: ตาแดงไม่มีขี้ตา (conjunctival suffusion)** | **หลอดเลือดเยื่อบุตาขยาย** จาก endothelium บาดเจ็บ ไม่ใช่การอักเสบเป็นหนอง | ต่างจากตาแดงติดเชื้อที่มีขี้ตา |
| **Lepto: ตัวเหลืองมาก แต่ AST/ALT ขึ้นไม่มาก** | เชื้อทำให้รอยต่อระหว่างเซลล์ตับหลุด → **น้ำดีรั่วกลับเข้าเลือด** ทั้งที่เซลล์ตับตายน้อย | bilirubin สูงมาก + transaminase ขึ้นเล็กน้อย → ชี้ lepto มากกว่าตับอักเสบจากไวรัส |
| **Lepto: ไตวาย K ต่ำ ปัสสาวะไม่น้อย** | เชื้อเกาะท่อไต → **tubulointerstitial nephritis** → ท่อไตดูด Na กลับไม่ได้ Na ไปถึงท่อส่วนปลายมาก → **K รั่วทิ้ง** | AKI แบบ non-oliguric + hypokalemia เป็นลักษณะของ lepto |
| **Lepto: ไอเป็นเลือด** | endothelium หลอดเลือดฝอยในปอดเสียหาย → **เลือดออกในถุงลม** | ตายได้เร็ว · ไข้ + ไอเลือดหลังน้ำท่วม → ให้ยาทันที |
| **Scrub typhus: eschar** | ไรอ่อนกัด → *O. tsutsugamushi* **แบ่งตัวใน endothelium ตรงรอยกัด** → หลอดเลือดอักเสบ เนื้อตายเป็นสะเก็ดดำ → ต่อมน้ำเหลืองที่ระบายบริเวณนั้นโต | หาในที่ลับ (รักแร้ ขาหนีบ ใต้ราวนม ขอบกางเกง) · พบแล้วเกือบวินิจฉัยได้ |
| **Scrub typhus: ปอดอักเสบ สับสน** | เชื้อกระจายไปติด endothelium ทั่วตัว → **vasculitis หลายอวัยวะ** | ไข้ + ปอดอักเสบ + เข้าป่า/ไร่ → เติม doxycycline |
| **Dengue: ช็อกตอนไข้ลง** | **plasma leakage** ช่วงวิกฤต 24–48 ชม. รอบไข้ลง → Hct ขึ้น | ช็อกขณะไข้ลง + Hct สูง + เกล็ดต่ำ → dengue ไม่ใช่ sepsis จากแบคทีเรีย |"""

INSERTS = [
    ("id-sep-01", "| WBC |", _SIGNS),
    ("id-sep-01", "**ปอด** (PaO₂/FiO₂)", "fig:sep_sofa"),
    ("id-sep-02", "6. **อวัยวะล้มเหลว**", "fig:sep_cascade"),
    ("id-sep-02", "| **โรงงานดับ** |", "fig:sep_vessel"),
    ("id-sep-03", "| Unlikely | รักษาเหตุ", "fig:sep_clock"),
    ("id-sep-04", "7. ประเมินซ้ำทุกชั่วโมง", "fig:sep_lactate"),
    ("id-sep-04", "| ตัดสินใจ **หยุด** ยา", "fig:sep_pct"),
    ("id-sep-05", "ตัวอย่าง: 60 kg × 30", "fig:sep_nss"),
    ("id-sep-05", "ผ่านช่วงกู้ชีพแล้ว", "fig:sep_starling"),
    ("id-sep-06", "| Dobutamine |", "fig:sep_pressors"),
    ("id-sep-07", "**Empirical** = ", "fig:sep_deesc"),
    ("id-sep-07", "**Gram-negative diplococci**", "fig:sep_gram"),
    ("id-sep-08", "| **AUC-dependent** |", "fig:sep_pkpd"),
    ("id-sep-09", "vancomycin กิน** หรือ fidaxomicin", "fig:sep_cdiff"),
    ("id-sep-10", "ยาปฏิชีวนะอย่างเดียว **ไม่หาย**", "fig:sep_source"),
    ("id-sep-10", "ไข้ช็อกในชาวนาเบาหวานจากอีสาน", _TROPIC),
    ("id-sep-11", "| สารน้ำหลังพ้นช่วงกู้ชีพ |", "fig:sep_rose"),
]


def sep_sofa():
    rows = [("ปอด", "capillary leak", "→ น้ำท่วมถุงลม (ARDS)", "PaO₂/FiO₂ ↓"),
            ("เกล็ดเลือด", "ถูกใช้ไปในลิ่มเลือดเล็ก", "ทั่วตัว (DIC)", "Platelet ↓"),
            ("ตับ", "เลือดเลี้ยงน้อย + อักเสบ", "→ ขับน้ำดีไม่ได้", "Bilirubin ↑"),
            ("หัวใจ\nหลอดเลือด", "NO → หลอดเลือดขยาย", "+ น้ำรั่วออกนอกหลอด", "MAP ↓ หรือ\nต้องใช้ยา"),
            ("สมอง", "cytokine + เลือดไปน้อย", "→ septic encephalopathy", "GCS ↓ สับสน"),
            ("ไต", "เลือดไปไตลด + อักเสบ", "ท่อไตบาดเจ็บ (AKI)", "Cr ↑\nปัสสาวะ ↓")]
    out = [box(70, 8, 280, 44, "ac", "ติดเชื้อ + ร่างกายตอบสนอง\nแบบเสียการควบคุม", "b", fs=12.5)]
    y0 = 70
    out.append(path("M70 30 H16 V%d" % (y0 + 5 * 54 + 23), "ln"))
    for k, (org, m1, m2, meas) in enumerate(rows):
        y = y0 + 54 * k
        out += [line(16, y + 23, 28, y + 23, "ln", "ah"), rect(30, y, 380, 46, "bx", 8),
                t(42, y + (19 if "\n" in org else 28), org, "sm b"),
                t(118, y + 19, m1, "xs i2"), t(118, y + 35, m2, "xs i2"),
                line(268, y + 23, 290, y + 23, "lmu", "ah-mu"),
                box(294, y + 5, 108, 36, "bad", meas, fs=11.5)]
    return fig("sepsis ทำอวัยวะไหนล้ม และ SOFA วัดอะไร",
               "SOFA ไม่ได้วัดเชื้อ แต่วัด **ผลของการตอบสนองที่เสียการควบคุม** ต่ออวัยวะหกระบบ แต่ละช่องคือกลไกที่ทำให้ค่าที่วัดได้เปลี่ยน · "
               "**SOFA เพิ่ม ≥ 2 จากเดิม** = sepsis",
               svg(420, 396, "การตอบสนองต่อการติดเชื้อที่เสียการควบคุมทำให้อวัยวะหกระบบล้มเหลว แต่ละระบบมีค่าที่ SOFA ใช้วัด", *out))


def sep_cascade():
    return fig("จากชิ้นส่วนเชื้อถึงอวัยวะล้มเหลว",
               "ตัวเชื้อไม่ได้ทำร้ายอวัยวะโดยตรงเป็นหลัก แต่ **cytokine ที่ร่างกายหลั่งออกมาเกินขนาด** ทำให้หลอดเลือดรั่ว ขยาย อุดตัน "
               "และเซลล์ใช้ออกซิเจนไม่ได้ · ในเวลาเดียวกันภูมิคุ้มกันถูกกดจนติดเชื้อซ้ำได้ง่าย",
               svg(420, 476, "PAMPs และ DAMPs จับ TLR ทำให้หลั่ง cytokine ซึ่งทำให้หลอดเลือดรั่ว ขยาย อุดตัน และ mitochondria ทำงานไม่ได้ จนอวัยวะล้มเหลว",
                   box(10, 8, 190, 44, "bad", "เชื้อ: PAMPs\n(เช่น LPS ของแกรมลบ)", fs=12),
                   box(220, 8, 190, 44, "ms", "เซลล์ตาย: DAMPs", fs=12),
                   line(105, 52, 170, 72, "ln", "ah"), line(315, 52, 250, 72, "ln", "ah"),
                   box(85, 74, 250, 44, "ac", "จับ TLR (เช่น TLR4) บน macrophage\n→ NF-κB เปิดยีนอักเสบ", fs=12),
                   line(210, 118, 210, 136, "ln", "ah"),
                   box(85, 138, 250, 38, "ac", "TNF-α · IL-1 · IL-6 ท่วมเลือด", "b", fs=12.5),
                   line(210, 176, 210, 196, "ln", "ah"),
                   rect(4, 198, 412, 146, "sk", 12),
                   t(14, 216, "ผลต่อหลอดเลือดและเซลล์", "xs b mu"),
                   box(12, 224, 194, 54, "wa", "ท่อรั่ว: glycocalyx หลุด\n→ capillary leak · บวม", fs=11.5),
                   box(214, 224, 194, 54, "ms", "ท่อขยาย: iNOS → NO\n→ หลอดเลือดขยาย MAP ↓", fs=11.5),
                   box(12, 284, 194, 54, "bad", "ท่อตัน: tissue factor ↑\nprotein C, AT ↓ → DIC", fs=11.5),
                   box(214, 284, 194, 54, "bad", "โรงงานดับ: mitochondria\nใช้ O₂ ไม่ได้ → lactate ↑", fs=11.5),
                   line(210, 344, 210, 364, "ln", "ah"),
                   box(85, 366, 250, 40, "bad", "อวัยวะล้มเหลว (SOFA ≥ 2)", "b", fs=12.5),
                   box(10, 420, 400, 46, "wa", "ระยะต่อมา: ภูมิถูกกด (immunoparalysis)\n→ ติดเชื้อซ้ำในโรงพยาบาล ไวรัสกลับมา", fs=11.5)))


def _vpanel(ox, oy, title, tc, cap1, cap2, body):
    return g(rect(ox, oy, 200, 184, "bx", 10), pill(ox + 8, oy + 8, title, tc, "sm b mid"),
             *body, t(ox + 100, oy + 158, cap1, "xs mid b"), t(ox + 100, oy + 173, cap2, "xs mid i2"))


def _walls(ox, top, bot, gaps=()):
    out = []
    x = ox + 10
    for gx in list(gaps) + [ox + 190]:
        out.append(rect(x, bot, gx - x - (4 if gx != ox + 190 else 0), 7, "ac", 3))
        x = gx + 4
    out.append(rect(ox + 10, top - 7, 180, 7, "ac", 3))
    return out


def sep_vessel():
    # ① ท่อรั่ว
    ox, oy = 6, 6
    p1 = _walls(ox, 52, 92, gaps=(ox + 60, ox + 120)) + [
        *[circ(ox + 30 + 26 * k, 66 + (k % 2) * 12, 3.5, "waf") for k in range(6)],
        line(ox + 58, 84, ox + 58, 116, "lwa w2", "ah-wa"), line(ox + 118, 84, ox + 118, 116, "lwa w2", "ah-wa"),
        *[circ(ox + x, 122 + dy, 3.5, "waf") for x, dy in ((30, 0), (58, 8), (88, 2), (118, 6), (146, 0))],
        t(ox + 186, 142, "เนื้อเยื่อบวม", "xs end twa b")]
    # ② ท่อขยาย
    ox2 = 214
    p2 = [rect(ox2 + 10, 48, 180, 7, "ac", 3), rect(ox2 + 10, 110, 180, 7, "ac", 3),
          *[ell(ox2 + 30 + 36 * k, 44, 12, 4, "ms") for k in range(5)],
          *[ell(ox2 + 30 + 36 * k, 121, 12, 4, "ms") for k in range(5)],
          line(ox2 + 30, 76, ox2 + 170, 76, "lbad w3", "ah-bad"),
          pill(ox2 + 150, 10, "NO", "ms", "xs b mid tms", w=40, h=18),
          line(ox2 + 170, 28, ox2 + 156, 40, "lms", "ah-ms"),
          t(ox2 + 100, 98, "เลือดไหลเร็ว แรงต้านต่ำ", "xs mid tbad"),
          t(ox2 + 100, 140, "กล้ามเนื้อเรียบคลาย", "xs mid tms")]
    # ③ ท่อตัน
    ox3, oy3 = 6, 196
    p3 = _walls(ox3, oy3 + 52, oy3 + 92) + [
        *[ell(ox3 + 28 + 16 * k, oy3 + 72 + (k % 2) * 6 - 3, 7, 4, "badf") for k in range(4)],
        path("M%d %d q10 -14 24 -4 q14 -6 18 10 q4 14 -10 18 q-12 8 -24 -2 q-14 -8 -8 -22 z" % (ox3 + 96, oy3 + 62), "inkf"),
        t(ox3 + 150, oy3 + 22, "microthrombus", "xs mid"), line(ox3 + 140, oy3 + 28, ox3 + 122, oy3 + 52, "lmu", "ah-mu"),
        rect(ox3 + 140, oy3 + 104, 46, 30, "sk", 6), t(ox3 + 163, oy3 + 123, "ซีด", "xs mid mu"),
        t(ox3 + 70, oy3 + 124, "ปลายทางขาดเลือด →", "xs mid i2")]
    # ④ โรงงานดับ
    ox4, oy4 = 214, 196
    p4 = [rect(ox4 + 66, oy4 + 40, 124, 96, "sk", 14),
          ell(ox4 + 104, oy4 + 74, 22, 11, "ok"), ell(ox4 + 152, oy4 + 106, 22, 11, "ok"),
          path("M%d %d q6 -8 12 0 q6 8 12 0 q6 -8 12 0" % (ox4 + 86, oy4 + 74), "lok"),
          path("M%d %d q6 -8 12 0 q6 8 12 0 q6 -8 12 0" % (ox4 + 134, oy4 + 106), "lok"),
          t(ox4 + 104, oy4 + 60, "✕", "b mid tbad"), t(ox4 + 152, oy4 + 92, "✕", "b mid tbad"),
          line(ox4 + 8, oy4 + 70, ox4 + 66, oy4 + 70, "lwa w2", "ah-wa"), t(ox4 + 10, oy4 + 62, "O₂ มาถึง", "xs twa b"),
          line(ox4 + 66, oy4 + 118, ox4 + 8, oy4 + 118, "lbad w2", "ah-bad"), t(ox4 + 8, oy4 + 136, "lactate", "xs tbad b")]
    return fig("ท่อรั่ว ท่อขยาย ท่อตัน โรงงานดับ",
               "สี่กลไกเกิดพร้อมกันในหลอดเลือดฝอยทั่วตัว · **ท่อรั่ว** แก้ด้วยสารน้ำ · **ท่อขยาย** แก้ด้วย norepinephrine · "
               "**ท่อตัน** ดูจาก CRT และผิวลาย · **โรงงานดับ** แก้ได้ทางเดียวคือกำจัดเชื้อ (ยาตามนาฬิกา + source control)",
               svg(420, 388, "หลอดเลือดฝอยใน sepsis สี่แบบ น้ำรั่วผ่านรอยแยก หลอดเลือดขยายจาก NO ลิ่มเลือดเล็กอุด และ mitochondria ใช้ออกซิเจนไม่ได้",
                   _vpanel(6, 6, "① ท่อรั่ว", "wa", "น้ำ + albumin รั่วออกนอกหลอด", "→ บวม · ปริมาตรในหลอดลด", p1),
                   _vpanel(214, 6, "② ท่อขยาย", "ms", "SVR ↓ → MAP ↓", "ระยะแรกมือเท้าอุ่น (warm shock)", p2),
                   _vpanel(6, 196, "③ ท่อตัน", "bad", "ผิวลาย CRT ช้า", "เกล็ดเลือดถูกใช้ → ต่ำ", p3),
                   _vpanel(214, 196, "④ โรงงานดับ", "bad", "O₂ ถึงแต่ใช้ไม่ได้", "→ lactate ↑ อวัยวะหยุดทำงาน", p4)))


def sep_clock():
    return fig("นาฬิกายาปฏิชีวนะ: ช็อกก่อน แล้วความมั่นใจ",
               "คำถามแรกคือ **ช็อกหรือไม่** เพราะในช็อกความเสี่ยงตายต่อชั่วโมงที่ช้าสูงมาก จึงให้ยาภายใน 1 ชม. แม้ยังไม่แน่ใจ · "
               "ถ้าไม่ช็อก ใช้ **ระดับความมั่นใจ** แยกคนที่ควรรอผลสืบค้นสั้น ๆ เพื่อไม่ให้ยากว้างกับคนที่ไม่ได้ติดเชื้อ",
               svg(420, 392, "ถ้าช็อก ให้ยาภายในหนึ่งชั่วโมงเมื่อ possible ขึ้นไป ถ้าไม่ช็อก definite และ probable ภายในหนึ่งชั่วโมง possible ภายในสามชั่วโมง unlikely ชะลอยา",
                   box(100, 8, 220, 36, "ac", "เริ่มสงสัย sepsis = นาทีที่ 0", "b", fs=12),
                   line(210, 44, 210, 58, "ln", "ah"),
                   box(150, 60, 120, 34, "sk", "ช็อกไหม?", "b"),
                   path("M180 94 V106 H8 V230", "ln"), path("M240 94 V106 H222 V256", "ln"),
                   t(100, 101, "มีช็อก", "sm b tbad mid"), t(316, 101, "ไม่มีช็อก", "sm b tok mid"),
                   line(8, 147, 16, 147, "ln", "ah"), box(18, 120, 188, 54, "bad", "Definite · Probable\n· Possible → ยา ≤ 1 ชม.", fs=11.5),
                   line(8, 211, 16, 211, "ln", "ah"), box(18, 186, 188, 50, "sk", "Unlikely → รักษาเหตุ\nของช็อกที่นำหน้า", fs=11.5),
                   line(222, 140, 230, 140, "ln", "ah"), box(232, 120, 180, 40, "bad", "Definite · Probable\n→ ยา ≤ 1 ชม.", fs=11.5),
                   line(222, 194, 230, 194, "ln", "ah"), box(232, 168, 180, 52, "ms", "Possible → สืบค้นเร็ว\nยังสงสัย → ยา ≤ 3 ชม.", fs=11.5),
                   line(222, 248, 230, 248, "ln", "ah"), box(232, 228, 180, 40, "ok", "Unlikely → ชะลอยา เฝ้าดู", fs=11.5),
                   line(10, 288, 410, 288, "lru da"),
                   t(210, 308, "ตาชั่งที่อยู่เบื้องหลัง", "sm b mid"),
                   box(10, 318, 196, 64, "bad", "ให้ช้า:\nช็อกตายเพิ่มทุกชั่วโมง", fs=11.5),
                   box(214, 318, 196, 64, "ms", "ให้ทุกคนทันที:\nC. difficile · เชื้อดื้อยา\nแพ้ยา ทั้งที่ไม่ได้ติดเชื้อ", fs=11.5)))


def sep_lactate():
    return fig("lactate สูงได้สี่ทาง",
               "lactate เกิดจาก pyruvate ที่ **เข้า mitochondria ไม่ได้หรือเข้าไม่ทัน** · ใน sepsis เกิดได้ทั้งจาก O₂ ไม่พอ (①) "
               "และจากเหตุที่ไม่ใช่การขาด O₂ (②–④) จึง **ใช้ดูแนวโน้ม** ว่าลดลงหรือไม่ ไม่ต้องให้น้ำไล่จนปกติ",
               svg(420, 352, "glucose ถูกเปลี่ยนเป็น pyruvate ถ้าเข้า mitochondria ไม่ได้จะกลายเป็น lactate สาเหตุมีสี่ทาง",
                   box(150, 8, 120, 32, "sk", "Glucose"),
                   line(210, 40, 210, 66, "ln w2", "ah"), t(202, 58, "glycolysis", "xs i2 end"),
                   t(290, 30, "③ adrenaline", "xs b tms"), t(290, 44, "→ β2 เร่ง", "xs tms"),
                   line(288, 40, 222, 52, "lms da", "ah-ms"),
                   box(150, 68, 120, 34, "ac", "Pyruvate", "b"),
                   line(270, 90, 322, 118, "lok w2", "ah-ok"), t(306, 96, "PDH", "xs i2"),
                   t(276, 118, "①", "b tbad"), t(300, 118, "✕", "b tbad"),
                   box(280, 122, 130, 52, "ok", "Mitochondria\n(ใช้ O₂)", fs=12),
                   t(410, 116, "②", "b tbad end"),
                   t(345, 192, "→ ATP มาก + CO₂", "xs mid tok"),
                   line(150, 90, 98, 118, "lbad w2", "ah-bad"), t(110, 96, "LDH", "xs i2 end"),
                   box(20, 120, 150, 40, "bad", "Lactate ↑ ในเลือด", "b", fs=12),
                   line(95, 160, 95, 200, "lmu w2", "ah-mu"), t(105, 186, "④ ขจัดช้าลง", "xs b tbad"),
                   box(20, 202, 150, 44, "wa", "ตับเปลี่ยนกลับ\nเป็น glucose", fs=11.5),
                   line(10, 262, 410, 262, "lru da"),
                   t(14, 282, "① เลือด/O₂ ไปไม่ถึงเนื้อเยื่อ (hypoperfusion)", "xs"),
                   t(14, 300, "② mitochondria เสีย ใช้ O₂ ไม่ได้แม้ส่งถึง", "xs"),
                   t(14, 318, "③ adrenaline/NE กระตุ้น β2 → glycolysis เร็วเกิน mitochondria รับไหว", "xs"),
                   t(14, 336, "④ ตับได้เลือดน้อย → ขจัด lactate ลดลง", "xs")))


def sep_pct():
    X = lambda d: 52 + d * 48
    Y = lambda v: 196 - (math.log10(v) + 1.3) / 2.6 * 166
    pts = [(0, 0.06), (0.25, 0.08), (0.5, 0.3), (0.75, 1.5), (1, 4.5), (1.5, 8.5), (2, 10), (2.5, 7.1), (3, 5),
           (4, 2.5), (5, 1.25), (6, 0.62), (7, 0.31)]
    out = [rect(X(0), 30, X(0.6) - X(0), 166, "ms", 0),
           line(X(0), Y(0.05), X(7.2), Y(0.05), "lmu"), line(X(0), Y(0.05), X(0), 24, "lmu")]
    for v, s in ((0.1, "0.1"), (0.5, "0.5"), (2, "2"), (10, "10")):
        out += [line(X(0) - 4, Y(v), X(0), Y(v), "lmu"), t(X(0) - 7, Y(v) + 4, s, "xs end mu")]
    for d in range(8):
        out += [line(X(d), Y(0.05), X(d), Y(0.05) + 4, "lmu"), t(X(d), Y(0.05) + 17, str(d), "xs mid mu")]
    out += [t(X(7.2), Y(0.05) + 32, "วันหลังเริ่มติดเชื้อ", "xs end mu"), t(10, 18, "PCT (ng/mL, สเกล log)", "xs mu"),
            line(X(0), Y(0.5), X(7.2), Y(0.5), "lok da"), t(X(7.2), Y(0.5) - 6, "0.5", "xs end tok b"),
            poly([(X(a), Y(b)) for a, b in pts], "lbad w3"),
            line(X(2), Y(10), X(4), Y(10), "lmu dt"), line(X(4), Y(10), X(4), Y(2.5) - 6, "lmu dt", "ah-mu"),
            t(X(4) + 6, Y(5), "ลด ≥ 80%", "xs b tok"),
            t(X(2) + 6, Y(10) - 8, "ยอดสูงสุด 1–2 วัน", "xs b tbad"),
            t(X(4.4), Y(1.25) - 22, "ยาได้ผล → ลดราวครึ่งหนึ่งต่อวัน", "xs i2"),
            t(X(0.6) + 6, 176, "← ชั่วโมงแรก PCT ยังต่ำ", "xs b tms"),
            box(10, 240, 196, 50, "ms", "เริ่มยา: ไม่ใช้ PCT\nค่าแรกอาจยังต่ำ + ช้าเกินรอ", fs=11.5),
            box(214, 240, 196, 50, "ok", "หยุดยา: < 0.5 หรือลด ≥ 80%\n+ อาการดี → พิจารณาหยุด", fs=11.5)]
    return fig("Procalcitonin ขึ้นช้า ลงตามการควบคุมเชื้อ",
               "PCT ถูกสร้างจากเนื้อเยื่อทั่วตัวเมื่อถูก cytokine ของการติดเชื้อแบคทีเรียกระตุ้น จึง **ขึ้นหลังติดเชื้อหลายชั่วโมง** และ"
               "สูงได้จากเหตุอื่น (ผ่าตัดใหญ่ บาดเจ็บ) — ใช้ตัดสินใจเริ่มยาไม่ได้ · แต่ **ค่าที่ลดลงต่อเนื่อง** บอกว่าเชื้อถูกควบคุม ช่วยตัดสินใจหยุดยา "
               "(เกณฑ์ < 0.5 หรือลด ≥ 80% จากยอดเป็นเกณฑ์ที่ใช้ในงานวิจัยทั่วไป)",
               svg(420, 300, "procalcitonin ขึ้นหลังติดเชื้อหลายชั่วโมง สูงสุดหนึ่งถึงสองวัน แล้วลดราวครึ่งหนึ่งต่อวันเมื่อยาได้ผล", *out))


def sep_nss():
    rows = [("พลาสมา", 140, 100), ("NSS 0.9%", 154, 154), ("Ringer's lactate", 130, 109)]
    out = [t(10, 18, "Na⁺ และ Cl⁻ (mmol/L)", "xs b mu")]
    for k, (name, na, cl) in enumerate(rows):
        y = 30 + 48 * k
        out += [t(10, y + 22, name, "sm b"),
                rect(122, y, na * 1.4, 14, "wa", 3), t(126 + na * 1.4, y + 11, "Na %d" % na, "xs twa b"),
                rect(122, y + 18, cl * 1.4, 14, "ms", 3), t(126 + cl * 1.4, y + 29, "Cl %d" % cl, "xs tms b")]
    out += [line(122 + 140, 26, 122 + 140, 176, "lmu dt"), t(122 + 140, 186, "Cl พลาสมา", "xs mid mu"),
            line(150, 196, 105, 216, "ln", "ah"), line(270, 196, 315, 216, "ln", "ah"),
            t(210, 204, "NSS ปริมาณมาก", "xs mid b"),
            box(10, 218, 196, 56, "ms", "Cl ในเลือด ↑ → HCO₃ ↓\nhyperchloremic acidosis", fs=11.5),
            box(214, 218, 196, 56, "bad", "Cl ↑ ที่ macula densa\n→ afferent หด → GFR ↓", fs=11.5),
            box(10, 284, 400, 46, "wa", "ข้อยกเว้น TBI: RL ค่อนข้าง hypotonic (≈ 273 mOsm/L)\nน้ำซึมเข้าสมองได้ → ใช้ NSS (≈ 308)", fs=11.5)]
    return fig("ทำไม balanced crystalloid ดีกว่า NSS",
               "NSS มี Cl⁻ เท่ากับ Na⁺ คือ 154 ซึ่ง **สูงกว่า Cl ในพลาสมามาก** · ให้ปริมาณมาก Cl ในเลือดสูงจึงดึง HCO₃⁻ ลง "
               "และ Cl ที่ไปถึง macula densa สั่งให้ afferent arteriole หด GFR ลด (tubuloglomerular feedback) · "
               "Ringer's lactate มี Cl ใกล้พลาสมา และ lactate ถูกตับเปลี่ยนเป็น HCO₃⁻",
               svg(420, 340, "NSS มีคลอไรด์สูงกว่าพลาสมามาก ทำให้เกิดภาวะกรดจากคลอไรด์สูงและไตทำงานลด ส่วน Ringer's lactate มีคลอไรด์ใกล้พลาสมา", *out))


def sep_starling():
    X = lambda p: 56 + p
    f = lambda p: 160 * (1 - math.exp(-p / 85))
    Y = lambda v: 210 - v
    curve = [(X(p), Y(f(p))) for p in range(0, 341, 10)]
    a0, a1, b0, b1 = 50, 95, 250, 295
    out = [line(X(0), Y(0), X(345), Y(0), "lmu"), line(X(0), Y(0), X(0), 20, "lmu"),
           t(X(345), Y(0) + 16, "preload (เลือดกลับหัวใจ)", "xs end mu"), t(14, 14, "stroke volume", "xs mu"),
           poly(curve, "lac w3"),
           line(X(a0), Y(f(a0)), X(a1), Y(f(a0)), "lwa w2", "ah-wa"),
           line(X(a1), Y(f(a0)), X(a1), Y(f(a1)) + 4, "lok w2", "ah-ok"),
           circ(X(a0), Y(f(a0)), 5, "okf"), t(X(a0) - 10, Y(f(a0)) + 5, "A", "b tok end"),
           t(X(a1) + 8, Y(f(a1)) + 30, "SV ↑ ≥ 10%", "sm b tok"), t(X(a1) + 8, Y(f(a1)) + 46, "= ยังตอบสนองต่อน้ำ", "xs tok"),
           line(X(b0), Y(f(b0)) + 10, X(b1), Y(f(b0)) + 10, "lwa w2", "ah-wa"),
           circ(X(b0), Y(f(b0)), 5, "badf"), t(X(b0) - 4, Y(f(b0)) - 12, "B", "b tbad"),
           t(X(b0) - 30, Y(f(b0)) + 44, "SV แทบไม่เพิ่ม", "sm b tbad"),
           t(X(b0) - 30, Y(f(b0)) + 60, "น้ำที่ให้ → รั่วไปปอด/เนื้อเยื่อ", "xs tbad"),
           t(X(a0) + 2, Y(f(a0)) + 18, "ให้น้ำ", "xs twa b"),
           # passive leg raise
           line(10, 312, 200, 312, "lru w2"),
           circ(26, 302, 8, "bx"), line(34, 304, 120, 304, "ln w3"), line(120, 304, 166, 258, "ln w3"),
           line(150, 266, 118, 296, "lbad w2", "ah-bad"), t(60, 282, "ยกขา 45°", "xs b"),
           box(214, 250, 196, 66, "wa", "Passive leg raise\nเทเลือดจากขากลับหัวใจชั่วคราว\n→ ทดสอบว่าอยู่จุด A หรือ B", fs=11),
           t(10, 334, "ไม่ต้องเสี่ยงให้น้ำจริงก่อนรู้คำตอบ · กลับคืนได้ทันทีเมื่อเอาขาลง", "xs i2")]
    return fig("Frank–Starling: ให้น้ำแล้ว SV เพิ่มไหม",
               "หัวใจที่อยู่ **ส่วนชันของกราฟ (A)** เพิ่ม stroke volume เมื่อได้น้ำ · ถ้าอยู่ **ส่วนราบ (B)** น้ำที่ให้ไม่เพิ่ม CO "
               "แต่เพิ่มแรงดันในหลอดเลือดฝอยที่รั่วอยู่แล้ว → ปอดบวมน้ำ · dynamic measures (PLR, SVV, PPV) จึงตอบได้ดีกว่า CVP ค่าเดียว",
               svg(420, 344, "กราฟ Frank Starling ที่จุด A การให้น้ำเพิ่ม stroke volume มาก ที่จุด B เพิ่มน้อย passive leg raise ใช้ทดสอบ", *out))


def sep_pressors():
    drugs = [("Norepinephrine", 40), ("Vasopressin", 96), ("Epinephrine", 152), ("Dobutamine", 208)]
    recs = [("α1", 40), ("V1", 96), ("β1", 152), ("β2", 208)]
    effs = [("หลอดเลือดหด\nSVR ↑ → MAP ↑", "ac"), ("หลอดเลือดหด\nไม่ผ่าน adrenergic", "ac"),
            ("บีบแรง + เร็ว → CO ↑\n(arrhythmia)", "ms"), ("หลอดเลือดขยาย BP ↓\nglycolysis → lactate ↑", "bad")]
    out = [t(65, 22, "ยา", "sm b mid mu"), t(196, 22, "receptor", "sm b mid mu"), t(340, 22, "ผล", "sm b mid mu")]
    for (d, y) in drugs:
        out.append(box(8, y, 114, 36, "sk", d, fs=11.5))
    for (r, y), (e, c) in zip(recs, effs):
        out += [box(172, y + 4, 48, 28, "bx", r, "b"), line(220, y + 18, 266, y + 18, "ln", "ah"),
                box(268, y, 146, 36, "bx" if c == "ac" else c, e, fs=10.5)]
    L = lambda dy, ry, c: line(122, dy + 18, 170, ry + 18, c)
    out += [L(40, 40, "lac w3"), L(40, 152, "lmu"), L(96, 96, "lac w3"),
            L(152, 152, "lac w3"), L(152, 40, "lac w3"), L(152, 208, "lmu"),
            L(208, 152, "lac w3"), L(208, 208, "lmu"),
            line(130, 266, 160, 266, "lac w3"), t(166, 270, "ออกฤทธิ์หลัก", "xs i2"),
            line(250, 266, 280, 266, "lmu"), t(286, 270, "ออกฤทธิ์รอง", "xs i2"),
            box(8, 284, 404, 60, "wa", "ทำไมเติม vasopressin: septic shock มี vasopressin ในเลือด\nต่ำเกินสัมพัทธ์ + α1 ตอบสนองต่อ NE ลดลง\n→ V1 เป็นอีกประตูที่ยังเปิด จึงประหยัด NE", fs=11),
            box(8, 352, 404, 46, "ok", "Hydrocortisone: ต่อมหมวกไตตอบสนองไม่พอ + steroid\nทำให้หลอดเลือดไวต่อ catecholamine ขึ้น → หลุดจากยาเร็วขึ้น", fs=11)]
    return fig("ยาแต่ละตัวกด receptor ไหน",
               "**NE** กด α1 เป็นหลักจึงหดหลอดเลือดโดยหัวใจไม่เร็วมาก · **vasopressin** ใช้ V1 ซึ่งไม่ขึ้นกับ adrenergic receptor ที่ถูก down-regulate · "
               "**epinephrine** มี β2 ด้วย จึงทำ lactate ขึ้นโดยไม่ได้แปลว่าแย่ลง · **dobutamine** เพิ่มแรงบีบแต่ β2 ทำหลอดเลือดขยาย ความดันอาจตก",
               svg(420, 408, "norepinephrine กด alpha1 vasopressin กด V1 epinephrine กด beta1 alpha1 และ beta2 dobutamine กด beta1 แต่ละ receptor ให้ผลต่างกัน", *out))


def sep_deesc():
    return fig("Empirical กว้าง → definitive แคบ",
               "ช่วงแรกยังไม่รู้เชื้อ จึง **คลุมกว้างตามแหล่งติดเชื้อและความเสี่ยงเชื้อดื้อยา** · เมื่อผลเพาะเชื้อและความไวยาออก "
               "**ลดให้แคบที่สุดที่ยังได้ผล** เพื่อลดแรงกดดันที่คัดเลือกเชื้อดื้อยา ลด *C. difficile* และพิษจากยา",
               svg(420, 300, "ช่วงแรกให้ยาคลุมกว้าง เมื่อผลเพาะเชื้อออกที่ 48 ถึง 72 ชั่วโมง ปรับเป็นยาที่แคบที่สุดที่ได้ผล",
                   poly([(20, 40), (190, 40), (250, 98), (410, 98), (410, 142), (250, 142), (190, 200), (20, 200)], "ac", closed=True),
                   t(100, 104, "Empirical", "b mid tac"), t(100, 122, "คลุมเชื้อที่น่าจะเป็น", "xs mid"),
                   t(100, 138, "ทั้งหมดจากแหล่งติดเชื้อ", "xs mid"), t(100, 156, "ขนาดเต็ม ให้เร็ว", "xs mid"),
                   t(330, 118, "Definitive", "b mid tok"), t(330, 134, "แคบที่สุดที่ได้ผล", "xs mid"),
                   line(220, 26, 220, 214, "lms da"), t(220, 20, "ผลเพาะเชื้อ + ความไว", "xs mid b tms"),
                   line(20, 220, 410, 220, "lmu", "ah-mu"),
                   t(20, 236, "ชม. 0", "xs mu"), t(20, 250, "เพาะเชื้อ → ยา", "xs mu"),
                   t(220, 236, "48–72 ชม.", "xs mid mu"), t(220, 250, "de-escalate", "xs mid mu"),
                   t(410, 236, "ครบกำหนด → หยุด", "xs end mu"),
                   box(10, 262, 400, 32, "sk", "ตัวอย่าง: meropenem → ได้ E. coli ไว ceftriaxone → เปลี่ยนเป็น ceftriaxone", fs=11)))


def sep_gram():
    def panel(x, y, title, tc, draw, org, drug):
        return g(rect(x, y, 200, 128, "bx", 10), *draw,
                 t(x + 100, y + 70, title, "sm b mid " + tc), t(x + 100, y + 88, org, "xs mid b"),
                 t(x + 100, y + 104, drug[0], "xs mid i2"), t(x + 100, y + 118, drug[1], "xs mid i2"))
    cl = [(0, 0), (11, -3), (22, 1), (5, 10), (16, 9), (27, 11), (9, -12), (20, -13), (-6, 5), (12, 20)]
    p1 = [circ(78 + dx, 34 + dy, 5.2, "inkf") for dx, dy in cl]
    p2 = [circ(32 + 11 * k, 30 + 4 * k, 5.2, "inkf") for k in range(7)] + \
         [circ(130 + dx, 34 + dy, 5.2, "inkf") for dx, dy in ((0, 0), (11, 0), (24, 12), (35, 12))]
    p3 = [rect(240 + dx, 24 + dy, 22, 9, "badf", 4.5) for dx, dy in ((0, 0), (30, 10), (60, -2), (14, 24), (52, 22))] + \
         [rect(340, 30, 30, 12, "bad", 6), circ(345, 36, 4, "badf"), circ(365, 36, 4, "badf"), t(355, 58, "safety pin", "xs mid tbad")]
    p4 = [p for cx, cy in ((282, 168), (326, 160), (306, 186)) for p in
          (ell(cx - 6, cy, 6, 7, "badf"), ell(cx + 6, cy, 6, 7, "badf"))]
    return fig("Gram stain บอกกลุ่มเชื้อและยาตัวแรก",
               "ผนัง **peptidoglycan หนา** ของแกรมบวกกักสี crystal violet ไว้ได้หลังล้างด้วย alcohol จึงติด **ม่วง** · "
               "แกรมลบผนังบางและมีเยื่อหุ้มชั้นนอก สีม่วงหลุด จึงติดสี safranin เป็น **ชมพูแดง** · รูปร่างและการเรียงตัวบอกสกุลคร่าว ๆ ก่อนผลเพาะเชื้อ",
               svg(420, 286, "แกรมบวกเรียงเป็นพวงคือ staphylococcus เป็นสายคือ streptococcus แกรมลบรูปแท่งคือ enterobacterales pseudomonas burkholderia แกรมลบคู่คือ neisseria",
                   panel(6, 6, "GPC เป็นพวง", "", p1, "Staphylococcus", ("MSSA: cloxacillin/cefazolin", "MRSA: vancomycin")),
                   panel(214, 6, "GNB รูปแท่ง", "tbad", p3, "Enterobacterales · Pseudomonas", ("Burkholderia: ติดสองปลาย", "→ ceftazidime/meropenem")),
                   panel(6, 140, "GPC เป็นคู่/สาย", "", [g(*p2, tr="translate(0 134)")], "Strep · pneumococcus", ("Enterococcus (เป็นคู่/สายสั้น)", "")),
                   panel(214, 140, "GN diplococci", "tbad", p4, "Neisseria", ("รูปเมล็ดถั่วหันหน้าเข้าหากัน", "")),
                   t(210, 282, "ม่วง = แกรมบวก · แดง = แกรมลบ (ในภาพใช้สีเข้ม/แดงแทน)", "xs mid mu")))


def _curve(doses, k, T, inf=0.0, step=0.1):
    pts, tt = [], 0.0
    while tt <= T + 1e-9:
        c = 0.0
        for td, c0 in doses:
            if tt < td: continue
            if inf > 0:
                r = c0 / (inf * k)
                c += r * (1 - math.exp(-k * (tt - td))) if tt - td <= inf else r * (1 - math.exp(-k * inf)) * math.exp(-k * (tt - td - inf))
            else:
                c += c0 * math.exp(-k * (tt - td))
        pts.append((tt, c)); tt += step
    return pts


def sep_pkpd():
    out = []
    # A: beta-lactam
    XA = lambda h: 50 + h * 22
    YA = lambda c: 176 - c * 1.4
    bol = _curve([(0, 100), (8, 100)], 0.46, 16)
    ext = [(a, b + 40 * math.exp(-0.46 * a)) for a, b in _curve([(0, 100), (8, 100)], 0.46, 16, inf=4)]
    out += [t(10, 18, "A · Beta-lactam (time-dependent): ตัวชี้วัด %fT > MIC", "sm b"),
            line(XA(0), YA(0), XA(16.4), YA(0), "lmu"), line(XA(0), YA(0), XA(0), 30, "lmu"),
            poly([(XA(a), YA(b)) for a, b in bol], "lmu w2"),
            poly([(XA(a), YA(b)) for a, b in ext], "lok w3"),
            line(XA(0), YA(10), XA(16.4), YA(10), "lbad da"), t(XA(16.4), YA(10) - 5, "MIC", "xs end tbad b"),
            t(XA(0.5), 40, "bolus: ยอดสูงแต่ต่ำกว่า MIC นาน", "xs i2"),
            t(XA(9.2), YA(64), "loading แล้วหยด 4 ชม.", "xs b tok"), t(XA(9.2), YA(64) + 14, "→ เหนือ MIC เกือบตลอด", "xs b tok"),
            t(XA(16.4), YA(0) + 16, "ชั่วโมง (ให้ทุก 8 ชม.)", "xs end mu")]
    # B: aminoglycoside
    XB = lambda h: 50 + h * 14.6
    YB = lambda c: 374 - c * 2.0
    once = _curve([(0, 60)], 0.277, 24)
    div = _curve([(0, 20), (8, 20), (16, 20)], 0.277, 24)
    out += [t(10, 216, "B · Aminoglycoside (concentration-dependent): Cmax/MIC", "sm b"),
            line(XB(0), YB(0), XB(24.4), YB(0), "lmu"), line(XB(0), YB(0), XB(0), 228, "lmu"),
            poly([(XB(a), YB(b)) for a, b in div], "lmu w2"),
            poly([(XB(a), YB(b)) for a, b in once], "lok w3"),
            line(XB(0), YB(6), XB(24.4), YB(6), "lbad da"), t(XB(24.4), YB(6) - 5, "MIC", "xs end tbad b"),
            t(XB(2), YB(62), "วันละครั้ง: ยอดสูง ≥ 8–10 × MIC", "xs b tok"),
            t(XB(9), YB(26) - 4, "แบ่งให้: ยอดต่ำ ระดับค้างทั้งวัน", "xs i2"),
            line(XB(10), YB(0) + 5, XB(23.6), YB(0) + 5, "lok w3"),
            t(XB(10), YB(0) + 19, "ช่วงยาต่ำนาน → ไต/หูได้พัก", "xs tok b"),
            t(XB(24.4), YB(0) + 19, "ชั่วโมง", "xs end mu")]
    return fig("PK/PD: ฆ่าเชื้อตามเวลา หรือตามความเข้มข้น",
               "**Beta-lactam** ฆ่าเชื้อได้เฉพาะช่วงที่ระดับยาเหนือ MIC ยอดสูงไม่ช่วย จึง **หยดนาน** ให้เส้นอยู่เหนือ MIC นานขึ้น · "
               "**Aminoglycoside** ฆ่าแรงตามยอด และมี post-antibiotic effect จึงให้ **ขนาดสูงวันละครั้ง** — ช่วงที่ระดับยาต่ำนานทำให้ "
               "ไตและหูชั้นในได้ขับยาที่สะสมออก พิษจึงน้อยลง (เส้นในภาพเป็นแผนภาพ ไม่ใช่ค่าจริงของยาตัวใด)",
               svg(420, 398, "beta lactam ให้แบบหยดนานทำให้ระดับยาเหนือ MIC นานกว่า bolus ส่วน aminoglycoside ให้วันละครั้งได้ยอดสูงและมีช่วงที่ระดับยาต่ำ", *out))


def sep_cdiff():
    import random
    rnd = random.Random(7)
    def blob(cx, cy, dots):
        return [ell(cx, cy, 44, 34, "sk")] + dots
    pos = [(rnd.uniform(-32, 32), rnd.uniform(-22, 22)) for _ in range(16)]
    before_l = [circ(58 + dx, 112 + dy, 3.5, "okf") for dx, dy in pos[:14]] + [rect(58 + 6, 112 + 8, 10, 5, "badf", 2.5)]
    after_l = [circ(156 + dx, 112 + dy, 3.5, "okf") for dx, dy in pos[:2]] + \
              [rect(156 + dx, 112 + dy, 12, 5, "badf", 2.5) for dx, dy in ((-24, -14), (-6, -6), (10, -16), (-20, 6), (4, 10), (18, 2), (-8, 18))]
    before_r = [circ(262 + dx, 112 + dy, 3.5, "okf") for dx, dy in pos[:13]] + [circ(262 + dx, 112 + dy, 3.5, "badf") for dx, dy in pos[13:15]]
    after_r = [circ(360 + dx, 112 + dy, 3.5, "badf") for dx, dy in pos[:11]]
    return fig("ยาเกินจำเป็น: ลำไส้เสียสมดุล และคัดเลือกเชื้อดื้อ",
               "จุลชีพปกติในลำไส้แย่งพื้นที่และอาหาร และเปลี่ยนกรดน้ำดีจนกัน *C. difficile* ไว้ (colonization resistance) · "
               "ยาปฏิชีวนะทำลายด่านนี้ spore ที่ทนยาจึงงอก **ปล่อย toxin A/B** ทำลาย cytoskeleton และรอยต่อของเยื่อบุลำไส้ใหญ่ → ท้องเสีย ไข้ pseudomembrane · "
               "ส่วนเชื้อที่ไวต่อยาตาย **เชื้อที่ดื้ออยู่เดิมจึงเพิ่มจำนวนแทนที่**",
               svg(420, 328, "ยาปฏิชีวนะที่เกินจำเป็นทำลายจุลชีพปกติทำให้ C difficile เพิ่มจำนวนและปล่อย toxin และคัดเลือกเชื้อดื้อยาให้เพิ่มจำนวน",
                   box(90, 8, 240, 36, "ms", "ยาปฏิชีวนะกว้าง / นานเกิน", "b", fs=12.5),
                   line(170, 44, 108, 64, "ln", "ah"), line(250, 44, 312, 64, "ln", "ah"),
                   t(107, 168, "ลำไส้ใหญ่", "xs mid b"), t(311, 168, "เชื้อในร่างกาย", "xs mid b"),
                   *blob(58, 112, before_l), line(104, 112, 110, 112, "ln", "ah"), *blob(156, 112, after_l),
                   *blob(262, 112, before_r), line(308, 112, 314, 112, "ln", "ah"), *blob(360, 112, after_r),
                   line(210, 66, 210, 300, "lru da"),
                   box(10, 178, 194, 52, "ms", "จุลชีพปกติหาย\nC. diff งอกจาก spore", fs=11.5),
                   line(107, 230, 107, 242, "ln", "ah"),
                   box(10, 244, 194, 56, "bad", "toxin A/B ทำลายเยื่อบุ\n→ ท้องเสีย pseudomembrane", fs=11.5),
                   box(216, 178, 194, 52, "ms", "เชื้อไวตาย\nเชื้อดื้อรอดและเพิ่มแทน", fs=11.5),
                   line(313, 230, 313, 242, "ln", "ah"),
                   box(216, 244, 194, 56, "bad", "ติดเชื้อครั้งหน้า\nต้องใช้ยากว้างกว่าเดิม", fs=11.5),
                   t(10, 320, "เขียว = ไวต่อยา/จุลชีพปกติ · แดง = C. diff หรือเชื้อดื้อ", "xs mu")))


def sep_source():
    import random
    rnd = random.Random(3)
    dots = []
    while len(dots) < 34:
        dx, dy = rnd.uniform(-76, 76), rnd.uniform(-46, 46)
        if (dx / 78) ** 2 + (dy / 48) ** 2 < 0.9: dots.append(circ(120 + dx, 96 + dy, 3, "badf"))
    return fig("ทำไมต้อง source control",
               "ในโพรงหนอง **ไม่มีหลอดเลือด** ยาจากกระแสเลือดซึมเข้าได้น้อย · หนองเป็นกรดและเต็มไปด้วยเศษเซลล์ที่จับ aminoglycoside · "
               "เชื้อจำนวนมหาศาลแบ่งตัวช้า beta-lactam ซึ่งฆ่าเชื้อที่กำลังสร้างผนังจึงได้ผลน้อย · สายสวนมี **biofilm** ที่ยาซึมไม่ผ่าน · "
               "การระบายหรือเอาออกจึงลดจำนวนเชื้อให้ยาจัดการส่วนที่เหลือได้",
               svg(420, 330, "โพรงหนองไม่มีหลอดเลือด ยาเข้าไม่ถึง หนองเป็นกรด เชื้อจำนวนมาก การระบายหนองลดจำนวนเชื้อให้ยาทำงานได้",
                   ell(120, 96, 98, 66, "ln w3"), ell(120, 96, 90, 58, "ms"), *dots,
                   t(120, 22, "ผนังฝี (ไม่มีหลอดเลือดเข้า)", "xs mid i2"),
                   path("M10 186 C 80 170, 160 200, 240 180", "lbad w5"),
                   t(14, 206, "หลอดเลือด", "xs tbad"),
                   *[circ(x, y, 4, "acf") for x, y in ((60, 180), (120, 186), (180, 186))],
                   line(120, 180, 120, 162, "lac w2", "ah-ac"), t(132, 172, "✕", "b tbad"),
                   t(234, 52, "① ยาซึมเข้าได้น้อย", "xs b"),
                   t(234, 80, "② หนองเป็นกรด + เศษ DNA", "xs b"), t(246, 94, "→ aminoglycoside ไม่ทำงาน", "xs i2"),
                   t(234, 122, "③ เชื้อมาก แบ่งตัวช้า", "xs b"), t(246, 136, "→ beta-lactam ฆ่าได้น้อย", "xs i2"),
                   t(234, 164, "④ สายสวน: biofilm", "xs b"),
                   line(210, 214, 210, 232, "ln w2", "ah"),
                   box(80, 234, 260, 36, "ok", "Source control ภายใน 6 ชม.", "b", fs=12.5),
                   t(210, 290, "ระบายหนอง · แก้ท่อปัสสาวะ/ท่อน้ำดีอุดตัน", "xs mid"),
                   t(210, 306, "ตัดเนื้อตาย · ถอดสายสวน · ผ่าตัดลำไส้ทะลุ", "xs mid"),
                   t(210, 322, "→ เชื้อเหลือน้อย ยาจัดการส่วนที่เหลือได้", "xs mid b tok")))


def sep_rose():
    X0, X1, X2, X3, X4 = 40, 118, 196, 290, 410
    Y = lambda v: 200 - v
    curve = path("M%d %d C 70 %d, 100 %d, %d %d S 180 %d, %d %d L %d %d C 330 %d, 380 %d, %d %d" % (
        X0, Y(0), Y(30), Y(80), X1, Y(90), Y(118), X2, Y(120), X3, Y(120), Y(118), Y(50), X4, Y(40)), "lwa w3")
    out = [rect(X0, 30, X1 - X0, 170, "bad", 0), rect(X1, 30, X2 - X1, 170, "ms", 0),
           rect(X2, 30, X3 - X2, 170, "sk", 0), rect(X3, 30, X4 - X3, 170, "ok", 0),
           t((X0 + X1) / 2, 46, "กู้ชีพ", "sm b mid"), t((X1 + X2) / 2, 46, "ปรับ", "sm b mid"),
           t((X2 + X3) / 2, 46, "คงที่", "sm b mid"), t((X3 + X4) / 2, 46, "ดึงน้ำออก", "sm b mid"),
           t((X0 + X1) / 2, 62, "นาที–ชม.", "xs mid mu"), t((X1 + X2) / 2, 62, "ชม.", "xs mid mu"),
           t((X2 + X3) / 2, 62, "วัน", "xs mid mu"), t((X3 + X4) / 2, 62, "วัน–สัปดาห์", "xs mid mu"),
           line(X0, Y(0), X4, Y(0), "lmu"), line(X0, Y(0), X0, 24, "lmu"),
           t(12, 18, "สมดุลน้ำสะสม (+)", "xs mu"), curve,
           t((X0 + X1) / 2, 222, "ให้น้ำเร็ว", "xs mid"), t((X0 + X1) / 2, 236, "30 mL/kg", "xs mid"),
           t((X1 + X2) / 2, 222, "ให้ตามการ", "xs mid"), t((X1 + X2) / 2, 236, "ตอบสนอง", "xs mid"),
           t((X2 + X3) / 2, 222, "ให้เท่าที่", "xs mid"), t((X2 + X3) / 2, 236, "จำเป็น", "xs mid"),
           t((X3 + X4) / 2, 222, "diuretic / RRT", "xs mid"), t((X3 + X4) / 2, 236, "ให้สมดุลติดลบ", "xs mid"),
           box(10, 252, 400, 46, "wa", "ท่อหายรั่วแล้ว น้ำที่ค้างใน interstitium ของปอด ลำไส้ ไต\nทำให้ใส่ท่อนาน ท้องอืด ไตฟื้นช้า → ต้องเอาออก", fs=11)]
    return fig("สี่ระยะของสารน้ำ: เติม แล้วต้องถอน",
               "ช่วงกู้ชีพ capillary leak ทำให้ต้องให้น้ำมาก สมดุลน้ำสะสมเป็นบวก · เมื่อการอักเสบสงบ **น้ำส่วนเกินไม่ได้ช่วย perfusion อีกแล้ว** "
               "แต่ทำให้อวัยวะบวมทำงานแย่ จึงต้องดึงออก (de-resuscitation) · สมดุลน้ำบวกสะสมมาก สัมพันธ์กับการตายที่สูงขึ้น",
               svg(420, 308, "สี่ระยะของสารน้ำใน sepsis กู้ชีพ ปรับ คงที่ และดึงน้ำออก สมดุลน้ำสะสมขึ้นแล้วต้องลดลง", *out))
