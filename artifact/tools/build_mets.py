#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Endo คาบ 01: Metabolic syndrome, Obesity, Dyslipidemia (อ.นวพร นภาทิวาอำนวย) → data/endo.json

สร้างชุดวิชา endo ใหม่ใน data/index.json ถ้ายังไม่มี
"""
import json, os

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
LEC = "01"
MS = ["2.3.4(6)", "B11.2.5(7)"]                       # metabolic syndrome
OB = ["2.3.4(7)", "B11.2.5(6)", "2.1.8"]              # obesity / weight gain
DLP = ["2.3.9(3)", "B7.2.5(6)", "B7.3(1)", "B7.4(8)"]  # dyslipidemia
SLIDE = "สไลด์ อ.นวพร"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None):
    if nl is None:  # รวมรหัส นล. ของข้อสอบในหัวข้อ เรียงตามลำดับที่พบ
        nl = list(dict.fromkeys(c for i in items for c in i["nl"]))
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes,
              "nl": nl, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl):
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}

# ───────────────────────────── 1 ─────────────────────────────
sec("endo-ms-01", "Metabolic syndrome — นิยามและกลไก",
    "กลุ่มปัจจัยเสี่ยงที่มีรากเดียวกันคือ insulin resistance และไขมันในช่องท้อง", 7,
"""**Metabolic syndrome (MetS)** คือ **กลุ่มปัจจัยเสี่ยงทางเมตาบอลิกที่เกิดร่วมกันและเชื่อมโยงกัน** ได้แก่
**อ้วนลงพุง · ความดันโลหิตสูง · ไตรกลีเซอไรด์สูง · HDL ต่ำ · น้ำตาลขณะอดอาหารสูง**
ซึ่งรวมกันแล้วเพิ่มความเสี่ยงของ **โรคหัวใจและหลอดเลือด โรคหลอดเลือดสมอง และเบาหวานชนิดที่ 2** อย่างมีนัยสำคัญ

### ตัวเลขความเสี่ยงที่สไลด์ให้ไว้

| ผลลัพธ์ | ความเสี่ยงที่เพิ่มขึ้น |
|---|---|
| **เบาหวานชนิดที่ 2** | **5–7 เท่า** |
| **โรคหัวใจและหลอดเลือด** | **3 เท่า** |
| **ตายจากทุกสาเหตุ** | **1.5 เท่า** |

### กลไกหลักสองอย่าง
สไลด์ระบุชัดว่ากลไกหลักของ MetS คือ **insulin resistance** และ **visceral adiposity**

**ทำไมไขมันในช่องท้องจึงอันตรายกว่าไขมันใต้ผิวหนัง**
- ไขมันในช่องท้อง **สลายตัว (lipolysis) ได้ไวกว่า** ปล่อยกรดไขมันอิสระ (FFA) ออกมามาก
- FFA เหล่านี้ **ไหลเข้าหลอดเลือดดำ portal ตรงสู่ตับ** ทันที
- ที่ตับ FFA ส่วนเกิน → **ตับสร้าง VLDL มากขึ้น** (TG สูง) และ **ตับดื้ออินซูลิน** (ผลิตกลูโคสไม่หยุด → FPG สูง)
- เนื้อเยื่อไขมันที่โตเกินยังหลั่ง **cytokine อักเสบ** (TNF-α, IL-6) และ **adiponectin ลดลง** → ดื้ออินซูลินทั่วร่างกาย

**ไล่ต่อให้ครบห้าองค์ประกอบ**

| องค์ประกอบ | เกิดจาก insulin resistance อย่างไร |
|---|---|
| **น้ำตาลสูง** | กล้ามเนื้อรับกลูโคสไม่ได้ + ตับผลิตกลูโคสไม่หยุด |
| **TG สูง** | ตับได้ FFA มาก → สร้าง VLDL มาก · LPL ทำงานลดลง |
| **HDL ต่ำ** | CETP แลก TG จาก VLDL เข้า HDL → HDL ที่อุดม TG ถูก hepatic lipase ย่อยและขับทิ้งเร็ว |
| **ความดันสูง** | อินซูลินสูงกระตุ้นการดูดกลับโซเดียมที่ไตและระบบประสาทซิมพาเทติก |
| **อ้วนลงพุง** | เป็นทั้งต้นเหตุและตัวขยายวงจร |

> MetS ไม่ใช่ "โรค" ที่ต้องรักษาด้วยยาตัวเดียว แต่เป็น **ป้ายเตือน** ว่าผู้ป่วยคนนี้มีรากปัญหาเดียวกันที่แสดงออกหลายทาง
> การรักษาที่ได้ผลกับทุกองค์ประกอบพร้อมกันจึงเป็น **การลดไขมันในช่องท้อง** ด้วยการปรับพฤติกรรม
""",
    ["กลไกหลักของ MetS = insulin resistance + visceral adiposity",
     "MetS เพิ่มความเสี่ยง T2D 5–7 เท่า · CVD 3 เท่า · ตายจากทุกสาเหตุ 1.5 เท่า",
     "ไขมันในช่องท้องส่ง FFA ผ่าน portal vein เข้าตับโดยตรง → VLDL สูง + ตับดื้ออินซูลิน",
     "HDL ต่ำใน MetS เกิดจาก CETP แลก TG เข้า HDL แล้ว HDL ถูกย่อยทิ้งเร็ว"],
    [
    mcq("END-MS-MCQ-01",
        "Which of the following best explains why visceral (intra-abdominal) fat is more strongly linked to insulin resistance than subcutaneous fat?",
        ["Visceral fat stores more triglyceride per adipocyte than subcutaneous fat",
         "Visceral adipocytes release free fatty acids directly into the portal circulation to the liver",
         "Visceral fat secretes more adiponectin than subcutaneous fat",
         "Visceral fat is metabolically inert and cannot undergo lipolysis",
         "Visceral fat increases insulin sensitivity of skeletal muscle"],
        1,
        """**ไขมันในช่องท้องระบาย FFA เข้า portal vein ตรงสู่ตับ** คือคำตอบ

**กลไก (portal hypothesis)**
- ไขมันในช่องท้องมี **lipolysis สูงกว่า** และตอบสนองต่อ catecholamine ไวกว่า
- FFA ที่ปล่อยออกมา **ไปถึงตับก่อนที่อื่น** ในความเข้มข้นสูง
- ตับที่ได้รับ FFA มาก → **ดื้ออินซูลิน · ผลิตกลูโคสมาก · สร้าง VLDL มาก** → น้ำตาลสูงและ TG สูง

**ทำไมข้ออื่นผิด**
- **adiponectin** เป็นฮอร์โมนที่ **เพิ่ม** ความไวต่ออินซูลิน และ **ลดลง** เมื่อไขมันในช่องท้องมาก
- ไขมันในช่องท้อง **ไม่ได้เฉื่อย** — ตรงข้าม มัน active ที่สุด
- ขนาดเซลล์หรือปริมาณ TG ต่อเซลล์ไม่ใช่กลไกที่อธิบายความต่าง""",
        "Visceral fat → FFA → portal vein → ตับ = รากของน้ำตาลสูงและ TG สูงใน MetS",
        "Pathophysiology of MetS",
        [SLIDE + " — Metabolic syndrome (MetS)", "Harrison's 21e — The metabolic syndrome"], MS),
    mcq("END-MS-MCQ-02",
        "Compared with individuals without metabolic syndrome, patients with metabolic syndrome have approximately what increase in risk of developing type 2 diabetes?",
        ["No increase", "1.5-fold", "2-fold", "5- to 7-fold", "20-fold"],
        3,
        """สไลด์ให้ตัวเลขไว้สามค่าที่ควรจำคู่กัน

| ผลลัพธ์ | ความเสี่ยง |
|---|---|
| **T2D** | **5–7 เท่า** ← สูงที่สุด |
| **CVD** | **3 เท่า** |
| **ตายจากทุกสาเหตุ** | **1.5 เท่า** |

ความเสี่ยงเบาหวานสูงที่สุด เพราะ MetS กับเบาหวานชนิดที่ 2 มี **รากเดียวกันคือ insulin resistance**
เมื่อ β-cell ชดเชยต่อไม่ไหว น้ำตาลจะข้ามเกณฑ์เบาหวาน

**1.5 เท่า** คือตัวเลขของการตายจากทุกสาเหตุ ส่วน **3 เท่า** คือของโรคหัวใจและหลอดเลือด — ตัวเลือกสองตัวนี้คือกับดักจากการจำสลับกัน""",
        "MetS: T2D 5–7× · CVD 3× · all-cause mortality 1.5×",
        "Risk associated with MetS",
        [SLIDE + " — Metabolic syndrome (MetS)"], MS),
    ])

# ───────────────────────────── 2 ─────────────────────────────
sec("endo-ms-02", "เกณฑ์วินิจฉัย MetS และการวัดรอบเอว",
    "ห้าองค์ประกอบกับตัวเลขที่ต้องจำ และรอบเอวที่ขึ้นกับเชื้อชาติ", 10,
"""### ห้าองค์ประกอบตามสไลด์

| องค์ประกอบ | เกณฑ์ |
|---|---|
| **อ้วนลงพุง (central obesity)** | **รอบเอวตามเกณฑ์เชื้อชาติ** — คนเอเชีย **ชาย ≥90 cm · หญิง ≥80 cm** |
| **ไตรกลีเซอไรด์สูง** | **≥150 mg/dL** หรือกำลังรักษาอยู่ |
| **HDL ต่ำ** | **<40 mg/dL ในชาย · <50 mg/dL ในหญิง** หรือกำลังรักษาอยู่ |
| **ความดันสูง** | **SBP ≥130 หรือ DBP ≥85 mmHg** หรือกำลังรักษาอยู่ |
| **น้ำตาลขณะอดอาหารสูง** | **FPG ≥100 mg/dL** หรือเคยได้รับการวินิจฉัย T2D |

### ต้องมีกี่ข้อ — สองสำนักที่ต้องแยกให้ออก
- **IDF (2005)** — **อ้วนลงพุงเป็นข้อบังคับ** แล้วต้องมีอีก **≥2 ข้อ** จากสี่ข้อที่เหลือ
- **Harmonized definition (IDF/AHA/NHLBI 2009)** — **≥3 ใน 5 ข้อ** โดยไม่มีข้อไหนบังคับ แต่ใช้รอบเอวตามเกณฑ์เชื้อชาติ

สไลด์เขียนไว้ว่ารอบเอว "**generally considered a required component, or highly associated**" ซึ่งก็คือการสะท้อนสองสำนักนี้
ในข้อสอบ ถ้าไม่ระบุ ให้ใช้ **≥3 ใน 5** เพราะเป็นเกณฑ์ปัจจุบันที่ใช้กันกว้างที่สุด

> **จำง่าย — "150 / 40-50 / 130-85 / 100"**
> TG กับ FPG ใช้เลขร้อยห้าสิบกับร้อย · HDL แยกชายหญิง · ความดันใช้เกณฑ์ต่ำกว่าเกณฑ์วินิจฉัยความดันสูงแบบเดิม

### รอบเอวตามเชื้อชาติ (IDF)

| กลุ่มประชากร | ชาย | หญิง |
|---|---|---|
| **Europid** | ≥94 cm | ≥80 cm |
| **เอเชียใต้ · จีน · ญี่ปุ่น** | **≥90 cm** | **≥80 cm** |
| **อเมริกาใต้และกลาง** | ใช้เกณฑ์เอเชียใต้ | |
| **แอฟริกาใต้ซาฮารา · ตะวันออกกลาง** | ใช้เกณฑ์ยุโรป | |
| **ATP III (สหรัฐฯ)** | ≥102 cm | ≥88 cm |

### เกณฑ์ไทยที่ใช้ง่ายในคลินิก — รอบเอวไม่เกินครึ่งหนึ่งของส่วนสูง
สไลด์ยกตัวอย่าง **สูง 170 cm → 170 / 2 = 85 → ถ้ารอบเอว >85 cm ถือว่าอ้วนลงพุง**
นี่คือ **waist-to-height ratio (WHtR) ≥0.5** ซึ่งใช้ได้ทั้งชายและหญิงโดยไม่ต้องจำตัวเลขแยก

### วิธีวัดรอบเอวให้ถูก
- วัด **ผ่านระดับสะดือ** (ตามแนวทางกรมอนามัยที่สไลด์ใช้) หรือ **กึ่งกลางระหว่างขอบซี่โครงล่างกับ iliac crest** (แนวทาง WHO)
- **สายวัดต้องขนานกับพื้น** ไม่รัดจนเนื้อบุ๋ม
- วัดตอน **หายใจออกสุดตามปกติ** ยืนตรง เท้าห่างกันเล็กน้อย

**Apple กับ pear** — รูปร่างแบบ **แอปเปิล** (ไขมันสะสมที่เอว) เสี่ยงทางเมตาบอลิกมากกว่ารูปร่างแบบ **ลูกแพร์** (ไขมันสะสมที่สะโพกและต้นขา)

### เมื่อเจอผู้ป่วยที่สงสัย MetS สไลด์ให้ตรวจสี่อย่าง
**วัดความดัน · วัดรอบเอว · fasting lipid profile · fasting glucose** — ทำเป็นกิจวัตรในการมาตรวจทุกครั้ง
เป้าหมายคือ **หาคนที่จะได้ประโยชน์จากการปรับพฤติกรรมอย่างเข้มข้น** ก่อนที่จะเกิดโรคหัวใจและหลอดเลือด
""",
    ["MetS (harmonized) = ≥3 ใน 5 · IDF = รอบเอวบังคับ + ≥2 ข้อ",
     "เกณฑ์: TG ≥150 · HDL <40 ชาย/<50 หญิง · BP ≥130/85 · FPG ≥100",
     "รอบเอวคนเอเชีย ชาย ≥90 · หญิง ≥80 cm",
     "รอบเอวเกินครึ่งหนึ่งของส่วนสูง (WHtR ≥0.5) = อ้วนลงพุง",
     "ตรวจสี่อย่าง: BP · รอบเอว · fasting lipid · fasting glucose"],
    [
    mcq("END-MS-MCQ-03",
        "A 48-year-old Thai man has waist circumference 92 cm, BP 128/82 mmHg (no treatment), fasting glucose 96 mg/dL, triglyceride 180 mg/dL and HDL-C 38 mg/dL. According to the harmonized criteria, how many components of metabolic syndrome does he have, and does he meet the definition?",
        ["2 components — does not meet the definition",
         "3 components — meets the definition",
         "4 components — meets the definition",
         "3 components — does not meet because fasting glucose is normal",
         "5 components — meets the definition"],
        1,
        """ไล่ทีละข้อตามเกณฑ์

| องค์ประกอบ | ค่าของผู้ป่วย | เกณฑ์ | เข้าหรือไม่ |
|---|---|---|---|
| รอบเอว (ชายเอเชีย) | 92 cm | ≥90 | ✅ |
| TG | 180 | ≥150 | ✅ |
| HDL (ชาย) | 38 | <40 | ✅ |
| BP | 128/82 | ≥130/85 | ❌ |
| FPG | 96 | ≥100 | ❌ |

**ได้ 3 ข้อ → เข้าเกณฑ์ MetS** (harmonized ต้องการ ≥3 ใน 5)
และยังเข้าเกณฑ์ IDF ด้วย เพราะมีรอบเอวเกิน + อีก 2 ข้อ

**กับดัก** — ตัวเลือก "ไม่เข้าเพราะน้ำตาลปกติ" ผิด เพราะ **ไม่มีองค์ประกอบใดเป็นข้อบังคับ** ในเกณฑ์ harmonized
และถ้าใช้เกณฑ์ ATP III เดิม (≥102 cm) ชายคนนี้จะ **หลุด** ข้อรอบเอว — จึงต้องใช้เกณฑ์ของคนเอเชียเสมอ""",
        "นับให้ครบห้าข้อ ใช้รอบเอวเกณฑ์เอเชีย แล้วดูว่าถึง 3 ข้อหรือไม่",
        "Diagnostic criteria of MetS",
        [SLIDE + " — MetS criteria / waist circumference cutoff", "Alberti KG et al. Circulation 2009;120:1640-5 (harmonized definition)"], MS),
    mcq("END-MS-MCQ-04",
        "A 35-year-old woman is 160 cm tall. Using the waist-to-height ratio criterion shown in the lecture, above what waist circumference is she classified as having central obesity?",
        ["70 cm", "80 cm", "88 cm", "90 cm", "94 cm"],
        1,
        """เกณฑ์ **รอบเอวไม่ควรเกินครึ่งหนึ่งของส่วนสูง** → 160 / 2 = **80 cm**

ผลลัพธ์บังเอิญตรงกับเกณฑ์รอบเอวหญิงเอเชีย (≥80 cm) พอดีสำหรับคนสูง 160 cm
แต่ถ้าหญิงคนนี้สูง 150 cm เกณฑ์ WHtR จะเป็น **75 cm** ซึ่งเข้มกว่า — WHtR จึง **ปรับตามรูปร่าง** ได้ดีกว่าตัวเลขคงที่

**ตัวเลือกอื่น** — 88 cm คือเกณฑ์หญิงของ ATP III (สหรัฐฯ) · 90 cm คือเกณฑ์ชายเอเชีย · 94 cm คือเกณฑ์ชาย Europid""",
        "WHtR ≥0.5 → รอบเอวเกิน ส่วนสูง/2 = อ้วนลงพุง",
        "Waist-to-height ratio",
        [SLIDE + " — เกณฑ์การวินิจฉัยอ้วนลงพุง"], MS + OB),
    mcq("END-MS-MCQ-05",
        "Which technique for measuring waist circumference is correct?",
        ["Measure at the level of the nipples during deep inspiration",
         "Measure at the narrowest point with the tape pulled tight enough to indent the skin",
         "Measure at the umbilicus (or midway between the lower rib margin and iliac crest) with the tape parallel to the floor at normal expiration",
         "Measure at the widest part of the buttocks",
         "Measure while the patient is lying supine"],
        2,
        """**วัดผ่านสะดือ (หรือกึ่งกลางระหว่างขอบซี่โครงล่างกับยอด iliac crest) สายวัดขนานพื้น ตอนหายใจออกปกติ** คือวิธีที่ถูก

**หลักสามข้อ**
- **ตำแหน่ง** — สไลด์ใช้แนว **ผ่านสะดือ** ส่วนแนวทาง WHO ใช้ **กึ่งกลางระหว่างขอบซี่โครงล่างกับ iliac crest**
- **สายวัดขนานกับพื้น** ไม่เอียงลงด้านหน้า
- **ไม่รัดจนเนื้อบุ๋ม** และวัดตอน **หายใจออกสุดตามปกติ**

**ทำไมข้ออื่นผิด** — วัดที่ **ส่วนกว้างสุดของสะโพก** คือการวัด **รอบสะโพก** ใช้คำนวณ waist-to-hip ratio ไม่ใช่รอบเอว ·
**นอนหงาย** ทำให้ไขมันหน้าท้องกระจายออกด้านข้าง ค่าจะต่ำกว่าจริง""",
        "รอบเอว: ผ่านสะดือ · ขนานพื้น · หายใจออกปกติ · ไม่รัด",
        "Waist circumference measurement",
        [SLIDE + " — Apple and pear body shapes / วิธีวัดรอบพุง"], MS + OB),
    ])

# ───────────────────────────── 3 ─────────────────────────────
sec("endo-ms-03", "การจัดการ MetS — ลดความเสี่ยงหัวใจที่แก้ไขได้",
    "ปรับพฤติกรรมอย่างเข้มข้นเป็นแกน แล้วรักษาแต่ละองค์ประกอบตามเป้า", 7,
"""สไลด์สรุปเป้าหมายไว้ว่า **จัดการปัจจัยเสี่ยงโรคหัวใจและหลอดเลือดที่แก้ไขได้** — รอบเอว · น้ำตาล · ไขมัน · ความดัน

### 1. Therapeutic lifestyle changes (TLC) — แกนของการรักษา

| ด้าน | เป้าหมายตามสไลด์ |
|---|---|
| **ออกกำลังกาย** | **ระดับปานกลาง 150–300 นาที/สัปดาห์** หรือ **ระดับหนัก 75–150 นาที/สัปดาห์** |
| **อาหาร** | ปรับเพื่อ **ลดไขมันในช่องท้อง** |
| **น้ำหนัก** | **ลดลง 5–10%** ของน้ำหนักตั้งต้น |

**ทำไมแค่ 5–10% ก็พอ** — ไขมันที่ลดลงช่วงแรกคือ **ไขมันในช่องท้องและไขมันในตับ** เป็นหลัก
ซึ่งเป็นแหล่งที่ขับเคลื่อน insulin resistance โดยตรง ผลทางเมตาบอลิกจึงดีขึ้นมากเกินสัดส่วนของน้ำหนักที่ลด

### 2. รักษาเฉพาะองค์ประกอบ

| ปัญหา | การรักษาตามสไลด์ |
|---|---|
| **ป้องกัน T2D** | ปรับพฤติกรรม **± metformin** |
| **ไขมันผิดปกติ** | **statin** |
| **ความดันสูง** | **ACEI หรือ ARB** |
| **น้ำหนัก / น้ำตาล** | **incretin-based therapy** (GLP-1RA) · **metabolic surgery** |

**ทำไม ACEI/ARB เป็นตัวเลือกแรกของความดันใน MetS** — เป็นกลางต่อเมตาบอลิซึม ไม่ทำให้น้ำตาลหรือไขมันแย่ลง
ต่างจาก **thiazide ขนาดสูง** และ **β-blocker รุ่นเก่า** ที่ทำให้ความไวต่ออินซูลินลดลงและน้ำหนักขึ้น

**Metformin ใน prediabetes** — ADA แนะนำให้พิจารณาเป็นพิเศษในผู้ที่ **BMI ≥35 · อายุ <60 ปี · เคยเป็นเบาหวานขณะตั้งครรภ์**
แต่ในการศึกษา DPP การปรับพฤติกรรมอย่างเข้มข้น **ลดการเกิดเบาหวานได้ 58%** มากกว่า metformin (31%)
— ยาจึงเป็น **ตัวเสริม** ไม่ใช่ตัวแทน

> ลำดับที่ถูกเสมอ: **ปรับพฤติกรรมก่อนและตลอดไป** แล้วค่อยเติมยาตามองค์ประกอบที่ยังไม่ถึงเป้า
""",
    ["ออกกำลังปานกลาง 150–300 นาที/สัปดาห์ หรือหนัก 75–150 นาที/สัปดาห์",
     "ลดน้ำหนัก 5–10% ก็ได้ผลทางเมตาบอลิกชัดเจน เพราะไขมันในช่องท้องลดก่อน",
     "ป้องกัน T2D: ปรับพฤติกรรม ± metformin · ไขมัน: statin · ความดัน: ACEI/ARB",
     "DPP: lifestyle ลดการเกิดเบาหวาน 58% · metformin 31%"],
    [
    mcq("END-MS-MCQ-06",
        "A 45-year-old man with metabolic syndrome (waist 98 cm, BP 142/90 mmHg, TG 220 mg/dL, HDL-C 36 mg/dL, FPG 110 mg/dL) asks what single intervention will improve all components of his condition. Which is the best answer?",
        ["Hydrochlorothiazide 50 mg daily",
         "Intensive lifestyle modification aiming for 5–10% weight loss and at least 150 minutes/week of moderate exercise",
         "Atenolol 50 mg daily",
         "Fish oil supplement",
         "Niacin"],
        1,
        """**การปรับพฤติกรรมอย่างเข้มข้นเพื่อลดน้ำหนัก 5–10% และออกกำลังปานกลาง ≥150 นาที/สัปดาห์** เป็นการรักษาเดียวที่ **แก้ที่ราก**
คือไขมันในช่องท้องและ insulin resistance จึงทำให้ **ทุกองค์ประกอบดีขึ้นพร้อมกัน** — รอบเอวลด ความดันลด TG ลด HDL เพิ่ม น้ำตาลลด

**ทำไมข้ออื่นผิด**
- **HCTZ ขนาดสูง** และ **atenolol** ลดความดันได้ แต่ **ทำให้น้ำตาลและ TG แย่ลง** จึงไม่ใช่ตัวเลือกแรกใน MetS
- **Fish oil** ลด TG ได้บ้างแต่ไม่แก้องค์ประกอบอื่น
- **Niacin** เพิ่ม HDL ได้แต่ทำให้ **ดื้ออินซูลินมากขึ้น** และไม่ลดเหตุการณ์หัวใจในการศึกษาที่ใช้ร่วมกับ statin""",
        "ลดไขมันในช่องท้อง = รักษาทุกองค์ประกอบของ MetS พร้อมกัน",
        "Management of MetS",
        [SLIDE + " — Manage modifiable cardiovascular risk factors", "Echouffo-Tcheugui JB et al. JAMA 2023;329:1206-16"], MS),
    mcq("END-MS-MCQ-07",
        "In a patient with metabolic syndrome and newly diagnosed stage 1 hypertension without other compelling indications, which antihypertensive class is preferred according to the lecture?",
        ["Non-selective beta-blocker", "High-dose thiazide diuretic", "ACE inhibitor or ARB", "Alpha-2 agonist", "Loop diuretic"],
        2,
        """สไลด์ระบุ **antihypertensive therapy (ACEIs, ARBs)** สำหรับ MetS

**เหตุผล**
- **เป็นกลางหรือดีต่อเมตาบอลิซึม** — ไม่ทำให้น้ำตาล ไขมัน หรือน้ำหนักแย่ลง และอาจลดการเกิดเบาหวานใหม่ได้เล็กน้อย
- **ปกป้องไต** ในผู้ที่มีแนวโน้มเป็นเบาหวาน

**ทำไมข้ออื่นไม่ใช่ตัวแรก**
- **Non-selective β-blocker** (propranolol) — ทำให้ **น้ำหนักขึ้น** (อยู่ในรายการยาที่ทำให้อ้วนของคาบนี้) ลดความไวต่ออินซูลิน และบังอาการน้ำตาลต่ำ
- **Thiazide ขนาดสูง** — เพิ่มน้ำตาลและ TG
- **Loop diuretic** ไม่ใช่ยาลดความดันหลักในผู้ที่ไตปกติ""",
        "ความดันใน MetS → ACEI/ARB เพราะเป็นกลางทางเมตาบอลิก",
        "Antihypertensive choice in MetS",
        [SLIDE + " — Manage modifiable cardiovascular risk factors"], MS),
    ])

# ───────────────────────────── 4 ─────────────────────────────
sec("endo-ms-04", "Obesity — นิยาม ระบาดวิทยา และการจัดระดับด้วย BMI",
    "โรคเรื้อรังที่กลับเป็นซ้ำ · BMI ของคนเอเชียใช้เกณฑ์ต่ำกว่า WHO", 11,
"""### นิยาม
**Obesity คือการสะสมไขมันที่ผิดปกติหรือมากเกินจนอาจเป็นอันตรายต่อสุขภาพ** (WHO)
สไลด์ย้ำว่าโรคอ้วนเป็น **โรคเรื้อรัง กลับเป็นซ้ำได้ และดำเนินโรคไปเรื่อย ๆ (chronic, relapsing, progressive disease)**
ที่มาพร้อมภาวะแทรกซ้อนและโรคร่วมที่รุนแรง — **ไม่ใช่ปัญหาของความตั้งใจหรือความขี้เกียจ**

### ระบาดวิทยาที่สไลด์ยกมา
- **เกือบ 1 ใน 4 ของคนทั้งโลกจะเป็นโรคอ้วนภายในปี 2035** (World Obesity Day)
- **ไทยปี 2025** — น้ำหนักเกินหรืออ้วน **~48–49%** ของผู้ใหญ่ · อ้วน (BMI ≥30) **17%**
- **มาเลเซีย** สูงที่สุดในอาเซียน ~54%
- **BMI สูงทำให้เสียชีวิตก่อนวัยอันควรจาก NCD ปีละ 1.6 ล้านคน**
- แนวโน้มในไทย — **เพิ่มเร็ว · ผู้หญิงมากกว่าผู้ชาย** · ขับเคลื่อนด้วยการกลายเป็นเมือง อาหารแปรรูป เครื่องดื่มหวาน และการใช้ชีวิตนั่งนิ่ง

### BMI = น้ำหนัก (kg) / ส่วนสูง (m)²

| ระดับ | WHO | Asia-Pacific (สไลด์ใช้เทียบ) |
|---|---|---|
| **ผอม** | <18.5 | <18.5 |
| **ปกติ** | 18.5–24.9 | **18.5–22.9** |
| **น้ำหนักเกิน** | 25–29.9 | **23–24.9** |
| **อ้วนระดับ 1** | 30–34.9 | **25–29.9** |
| **อ้วนระดับ 2** | 35–39.9 | **≥30** |
| **อ้วนระดับ 3** | ≥40 | — |

**ทำไมคนเอเชียใช้เกณฑ์ต่ำกว่า** — ที่ BMI เท่ากัน คนเอเชียมี **สัดส่วนไขมันในร่างกายและไขมันในช่องท้องมากกว่า**
และเริ่มเป็นเบาหวานและโรคหัวใจที่ BMI ต่ำกว่าคนยุโรป

**เกณฑ์เอเชียอีกชุดที่สไลด์แสดง (staging)** — WHO expert consultation 2004 เสนอจุดตัดสำหรับคนเอเชียที่
**23 · 27.5 · 32.5 · 37.5** → น้ำหนักเกิน 23–27.4 · อ้วน stage 1 **27.5–32.4** · stage 2 **32.5–37.4** · stage 3 **≥37.5**
ตัวเลขชุดนี้สำคัญเพราะ **เกณฑ์ผ่าตัดลดน้ำหนักของไทยใช้ 27.5 / 32.5 / 37.5** (ดูหัวข้อ 9)

### ข้อจำกัดของ BMI
BMI **วัดขนาด ไม่ได้วัดสุขภาพ** — ใช้คัดกรองรายบุคคลและประเมินระดับประชากรได้ดี แต่
- **แยกไขมันกับกล้ามเนื้อไม่ได้** — นักกีฬากล้ามใหญ่ BMI สูงแต่ไขมันต่ำ
- **ไม่บอกการกระจายของไขมัน** — ต้องใช้ **รอบเอว** คู่กันเสมอ

### รอบเอว — ใช้ร่วมกับ BMI
วัด **กึ่งกลางระหว่างขอบซี่โครงล่างกับ iliac crest** · เกณฑ์ **Caucasian ≥102/≥88 cm · Asian ≥90/≥80 cm**
รอบเอวที่มากขึ้นสัมพันธ์กับภาวะแทรกซ้อนและการเสียชีวิตที่เพิ่มขึ้น **แม้ BMI เท่ากัน**

### Bioelectrical impedance analysis (BIA)
ประเมิน **เปอร์เซ็นต์ไขมันในร่างกาย** จากความต้านทานไฟฟ้า
- **ข้อดี** — สะดวก ราคาไม่แพง เร็ว
- **ข้อเสีย** — ความแม่นยำ **แกว่งมาก** ตาม **ภาวะน้ำในร่างกาย · การออกกำลังกายเพิ่งเสร็จ · อาหารที่เพิ่งกิน · เครื่องและสมการที่ใช้**
  เครื่องชั่งตามบ้านแม่นน้อยกว่าเครื่องในคลินิก

### นิยามใหม่ปี 2025
- **Lancet Diabetes & Endocrinology Commission 2025** — แยก **clinical obesity** (มีไขมันเกินจน **อวัยวะทำงานผิดปกติ** หรือ **จำกัดกิจวัตรประจำวัน** แล้ว = เป็นโรค)
  ออกจาก **preclinical obesity** (ไขมันเกินแต่อวัยวะยังทำงานปกติ = มีความเสี่ยง) และให้ยืนยันไขมันเกินด้วยการวัดอย่างน้อยหนึ่งอย่างนอกเหนือจาก BMI
- **EASO** — วินิจฉัยโรคอ้วนเมื่อ **BMI ≥30** หรือ **BMI ≥25 ร่วมกับ WHtR ≥0.5** **และ** มีความบกพร่องทางการแพทย์ การทำงาน หรือจิตใจ
""",
    ["Obesity = โรคเรื้อรัง กลับเป็นซ้ำ ดำเนินโรคต่อเนื่อง ไม่ใช่เรื่องความตั้งใจ",
     "Asia-Pacific: ปกติ 18.5–22.9 · เกิน 23–24.9 · อ้วน I 25–29.9 · อ้วน II ≥30",
     "จุดตัด staging เอเชีย 27.5 / 32.5 / 37.5 — ใช้ในเกณฑ์ผ่าตัดของไทย",
     "BMI วัดขนาดไม่ได้วัดสุขภาพ ต้องใช้รอบเอวคู่กันเสมอ",
     "BIA แม่นยำแกว่งตามภาวะน้ำ การออกกำลังกาย และอาหาร",
     "Lancet 2025: clinical obesity = มีอวัยวะทำงานผิดปกติหรือจำกัดกิจวัตรแล้ว"],
    [
    mcq("END-OB-MCQ-01",
        "A 40-year-old Thai woman weighs 68 kg and is 1.60 m tall. Using the Asia-Pacific BMI classification, how is she classified?",
        ["Normal", "Overweight", "Obese class I", "Obese class II", "Obese class III"],
        2,
        """**BMI = 68 / (1.60)² = 68 / 2.56 = 26.6 kg/m²**

ตามเกณฑ์ **Asia-Pacific** — อ้วนระดับ 1 คือ **25–29.9** → **Obese class I**

**กับดัก** — ถ้าใช้เกณฑ์ **WHO** ค่า 26.6 จะเป็นแค่ **น้ำหนักเกิน** (25–29.9)
ในผู้ป่วยคนไทย ให้ใช้เกณฑ์เอเชียเสมอ เพราะคนเอเชียมีไขมันในช่องท้องมากกว่าและเกิดโรคแทรกซ้อนที่ BMI ต่ำกว่า

| เกณฑ์ | 26.6 จัดเป็น |
|---|---|
| WHO | Overweight |
| **Asia-Pacific** | **Obese I** |""",
        "คนไทย BMI ≥25 = อ้วนระดับ 1 ตามเกณฑ์ Asia-Pacific",
        "BMI classification",
        [SLIDE + " — BMI based on WHO criteria and Asian criteria"], OB),
    mcq("END-OB-MCQ-02",
        "A 25-year-old professional rugby player has BMI 31 kg/m², waist circumference 84 cm and body fat 12% by DEXA. Which statement best describes the limitation illustrated?",
        ["BMI overestimates adiposity because it cannot distinguish fat from lean mass",
         "BMI underestimates adiposity in muscular individuals",
         "Waist circumference is unreliable in men",
         "DEXA is less accurate than BMI for body fat",
         "He meets the EASO definition of obesity"],
        0,
        """**BMI แยกไขมันกับกล้ามเนื้อไม่ได้** — ในนักกีฬากล้ามเนื้อมาก BMI จะ **สูงเกินจริง** เมื่อเทียบกับไขมัน

สไลด์ย้ำว่า **BMI เป็นการวัดขนาด ไม่ใช่การวัดสุขภาพ** ใช้คัดกรองได้ แต่ต้องประเมินร่วมกับ
- **รอบเอว** — 84 cm ต่ำกว่าเกณฑ์ชายเอเชีย 90 cm
- **เปอร์เซ็นต์ไขมัน** — 12% อยู่ในช่วงนักกีฬา

**ทำไม "เข้าเกณฑ์ EASO" ผิด** — EASO ต้องมี **ความบกพร่องทางการแพทย์ การทำงาน หรือจิตใจ** ร่วมด้วย
ซึ่งนักกีฬาคนนี้ไม่มี และตามกรอบ Lancet 2025 ก็ **ไม่มีไขมันเกิน** ตั้งแต่ต้น""",
        "BMI สูงในคนกล้ามเยอะ ≠ อ้วน — ยืนยันไขมันด้วยรอบเอวหรือการวัดไขมันเสมอ",
        "Limitations of BMI",
        [SLIDE + " — BMI has well-documented limitations", "Rubino F et al. Lancet Diabetes Endocrinol 2025"], OB),
    mcq("END-OB-MCQ-03",
        "According to the 2025 Lancet Commission, which of the following distinguishes 'clinical obesity' from 'preclinical obesity'?",
        ["A BMI of 40 kg/m² or more",
         "The presence of objective organ dysfunction or limitation of daily activities caused by excess adiposity",
         "Waist circumference above the ethnic-specific cut-off",
         "Body fat percentage measured by bioelectrical impedance",
         "A family history of obesity"],
        1,
        """**Clinical obesity** = ไขมันเกินที่ทำให้ **อวัยวะทำงานผิดปกติแล้ว** หรือ **จำกัดความสามารถในการทำกิจวัตรประจำวัน**
เป็น **โรคที่ต้องรักษา** ในตัวมันเอง

**Preclinical obesity** = ไขมันเกิน แต่อวัยวะยังทำงานปกติ → เป็น **ภาวะเสี่ยง** ที่ต้องติดตามและป้องกัน

**ทำไมข้ออื่นผิด** — BMI · รอบเอว · % ไขมัน ใช้ **ยืนยันว่ามีไขมันเกิน** เท่านั้น แต่ **ไม่ได้แยก** ว่าเป็นโรคแล้วหรือยัง
การแยกต้องดูที่ **ผลต่ออวัยวะหรือกิจวัตร** — แนวคิดเดียวกับที่คาบนี้เน้นการตั้งเป้าแบบ **complication-centric** แทน BMI-centric""",
        "Clinical obesity = ไขมันเกิน + อวัยวะทำงานผิดปกติหรือจำกัดกิจวัตรแล้ว",
        "Definition of clinical obesity",
        [SLIDE + " — What is obesity? 2025 Lancet Commission"], OB),
    ])

# ───────────────────────────── 5 ─────────────────────────────
sec("endo-ms-05", "สาเหตุของโรคอ้วน และยาที่ทำให้น้ำหนักขึ้น",
    "สมดุลพลังงานถูกกำหนดด้วยหลายปัจจัย · ยาคือสาเหตุที่แก้ได้ง่ายที่สุด", 9,
"""### รากของโรคอ้วนลึกกว่า "กินเยอะ ขยับน้อย"
สไลด์ย้ำว่าสาเหตุ **ไม่ใช่ความขี้เกียจหรือขาดความตั้งใจ** แต่เป็นผลรวมของปัจจัย
**พันธุกรรม · จิตใจ · สังคมวัฒนธรรม · เศรษฐกิจ · สิ่งแวดล้อม** ที่ทำให้เกิด **ความไม่สมดุลของพลังงาน**

| กลุ่มปัจจัย | ตัวอย่าง |
|---|---|
| **ฮอร์โมน** | **leptin resistance** |
| **โรคที่พบบ่อย** | **hypothyroidism · Cushing's syndrome · ซึมเศร้า · นอนไม่พอหรือนอนผิดปกติ** |
| **ยา** | ดูตารางด้านล่าง |
| **พันธุกรรม** | การถ่ายทอด · epigenetic · ประสบการณ์ช่วงต้นของชีวิต |
| **พฤติกรรม** | นิสัยการกินที่ไม่ดี · ไม่ออกกำลังกาย |
| **จิตใจ** | ความเครียด · ปัญหาอารมณ์ · การกินผิดปกติ (eating disorder) |
| **สังคม การเมือง เศรษฐกิจ** | อาหารแปรรูปราคาถูก · เครื่องดื่มหวาน · เมืองที่ไม่เอื้อต่อการเดิน |

**Leptin resistance** — เลปตินหลั่งจากเซลล์ไขมันตามปริมาณไขมัน บอกสมองให้ **อิ่มและเผาผลาญมากขึ้น**
คนอ้วนส่วนใหญ่มี **เลปตินสูงแต่สมองไม่ตอบสนอง** การให้เลปตินเสริมจึงไม่ได้ผล (ยกเว้นผู้ขาดเลปตินแต่กำเนิดซึ่งพบน้อยมาก)

**โรคต่อมไร้ท่อที่ต้องนึกถึงเมื่อมีเบาะแส**
- **Cushing's syndrome** — อ้วนลงพุงแต่ **แขนขาลีบ** · หน้ากลม (moon face) · หนอกที่คอ (buffalo hump) ·
  **ท้องลายสีม่วงกว้าง >1 cm** · ฟกช้ำง่าย · กล้ามเนื้อต้นขาอ่อนแรง
- **Hypothyroidism** — น้ำหนักขึ้นเล็กน้อย (ส่วนใหญ่เป็นน้ำ) · ขี้หนาว · ท้องผูก · ผิวแห้ง · reflex คลายตัวช้า

### ยาที่ทำให้น้ำหนักขึ้นและยาทางเลือก (Canadian Adult Obesity CPG 2020)

| โรค | ยาที่ทำให้น้ำหนักขึ้น | ทางเลือกที่เป็นกลางหรือทำให้น้ำหนักลด |
|---|---|---|
| **เบาหวาน** | **insulin · sulfonylurea · meglitinide · pioglitazone (TZD)** | **GLP-1RA · SGLT2i** · amylin analog (metformin, DPP-4i เป็นกลาง) |
| **ความดันสูง** | **β-blocker ชนิดไม่เลือก** — propranolol · metoprolol · atenolol | **ACEI · ARB · CCB** · carvedilol |
| **ซึมเศร้า** | **TCA** (amitriptyline, imipramine) · **paroxetine** · **mirtazapine** · MAOI | **bupropion** · fluoxetine · sertraline |
| **โรคจิต** | **clozapine · olanzapine** · quetiapine · risperidone | **aripiprazole · ziprasidone · lurasidone** |
| **อารมณ์สองขั้ว** | **lithium · valproate** | **lamotrigine** |
| **ลมชัก / ปวดประสาท** | **valproate · gabapentin · pregabalin** · carbamazepine | **topiramate · zonisamide** |
| **คุมกำเนิด** | **DMPA (ยาฉีดคุมกำเนิด)** | ยาเม็ดคุมกำเนิดชนิดรวม · ห่วงอนามัย |
| **ต้านการอักเสบ** | **glucocorticoid** (prednisolone, dexamethasone) | NSAIDs · biologics |
| **แพ้** | **antihistamine รุ่นแรก** — diphenhydramine · cyproheptadine | **loratadine** (ไม่ผ่าน BBB) |

> **หลักคิด** — ยาที่ **เพิ่มอินซูลิน** (insulin, SU) · **กระตุ้นความอยากอาหารผ่าน H1 และ 5-HT2C** (antipsychotic, mirtazapine, antihistamine) ·
> หรือ **ทำให้คั่งน้ำ** (TZD) จะทำให้น้ำหนักขึ้น การทบทวนรายการยาจึงเป็น **ขั้นตอนแรกที่ทำได้ทันที** ในผู้ป่วยโรคอ้วนทุกคน
""",
    ["สาเหตุโรคอ้วน = พันธุกรรม + จิตใจ + สังคม + เศรษฐกิจ + สิ่งแวดล้อม ไม่ใช่ความขี้เกียจ",
     "คนอ้วนส่วนใหญ่มี leptin สูงแต่ดื้อ — การให้ leptin เสริมไม่ได้ผล",
     "Cushing: อ้วนลงพุง แขนขาลีบ ท้องลายสีม่วงกว้าง >1 cm",
     "เบาหวาน: เลี่ยง insulin/SU/TZD → เลือก GLP-1RA หรือ SGLT2i",
     "ซึมเศร้า: เลี่ยง mirtazapine/paroxetine/TCA → เลือก bupropion",
     "โรคจิต: olanzapine/clozapine ทำให้อ้วนมากที่สุด → aripiprazole/ziprasidone/lurasidone"],
    [
    mcq("END-OB-MCQ-04",
        "A 52-year-old woman with type 2 diabetes (HbA1c 8.4%) and BMI 32 kg/m² is currently taking metformin and glipizide. Which add-on agent would best improve glycaemia while promoting weight loss?",
        ["Pioglitazone", "Glibenclamide", "Basal insulin", "A GLP-1 receptor agonist", "Repaglinide"],
        3,
        """**GLP-1 receptor agonist** ลดน้ำตาลและ **ลดน้ำหนัก** ได้พร้อมกัน — อยู่ในคอลัมน์ "ทางเลือก" ของตารางยาในสไลด์

**กลไกที่ทำให้น้ำหนักลด** — ออกฤทธิ์ที่ hypothalamus ให้ **อิ่มเร็วและอิ่มนาน** · **ชะลอการบีบตัวของกระเพาะ**
และกระตุ้นอินซูลิน **เฉพาะเมื่อน้ำตาลสูง** จึงไม่ทำให้น้ำตาลต่ำและไม่กระตุ้นให้กินชดเชย

**ทำไมข้ออื่นผิด** — ทั้งหมดอยู่ในคอลัมน์ **ยาที่ทำให้น้ำหนักขึ้น**
- **Pioglitazone** — สร้างเซลล์ไขมันใต้ผิวหนังเพิ่ม + **คั่งน้ำ**
- **Glibenclamide · repaglinide** — กระตุ้นอินซูลินตลอดเวลา → น้ำตาลต่ำ → **กินชดเชย**
- **Insulin** — ฤทธิ์ anabolic โดยตรง

**SGLT2 inhibitor** ก็เป็นทางเลือกที่ดีเช่นกัน (น้ำหนักลด 2–3 kg จากการขับกลูโคสทิ้งทางปัสสาวะ) แต่ไม่อยู่ในตัวเลือกนี้""",
        "เบาหวาน + อ้วน → เติม GLP-1RA หรือ SGLT2i ไม่เติม SU/TZD/insulin",
        "Weight-neutral diabetes drugs",
        [SLIDE + " — Obesity: Iatrogenic medications (Canadian CPG 2020)"], OB),
    mcq("END-OB-MCQ-05",
        "A 30-year-old man with schizophrenia gained 14 kg in 6 months after starting an antipsychotic. Fasting glucose is now 118 mg/dL. Which antipsychotic is he most likely taking, and what is a lower-weight-gain alternative?",
        ["Aripiprazole; switch to olanzapine",
         "Olanzapine; switch to aripiprazole",
         "Haloperidol; switch to clozapine",
         "Ziprasidone; switch to quetiapine",
         "Lurasidone; switch to clozapine"],
        1,
        """**Olanzapine** (และ **clozapine**) ทำให้น้ำหนักขึ้นและเกิดความผิดปกติทางเมตาบอลิกมากที่สุดในกลุ่ม antipsychotic
ทางเลือกที่สไลด์ให้ไว้คือ **aripiprazole · ziprasidone · lurasidone**

**กลไก** — ยาต้าน **H1** และ **5-HT2C** ที่ hypothalamus → **ความอยากอาหารเพิ่มขึ้นมาก**
และยังทำให้ **ดื้ออินซูลินโดยตรง** แม้น้ำหนักยังไม่ขึ้น (น้ำตาลของผู้ป่วยรายนี้เริ่มสูงแล้ว)

**การดูแล** — ผู้ที่เริ่ม antipsychotic ต้องติดตาม **น้ำหนัก รอบเอว น้ำตาล และไขมัน** เป็นระยะ
การเปลี่ยนยาต้องทำร่วมกับจิตแพทย์ เพราะ **clozapine** มักใช้ในผู้ที่ดื้อต่อยาอื่นและเปลี่ยนไม่ได้เสมอไป

ตัวเลือกอื่นกลับด้านกันทั้งหมด — เปลี่ยน **ไปหา** ยาที่ทำให้อ้วนมากกว่า""",
        "Olanzapine/clozapine = อ้วนที่สุด · ทางเลือก aripiprazole, ziprasidone, lurasidone",
        "Antipsychotic-induced weight gain",
        [SLIDE + " — Drugs that cause weight gain / Iatrogenic medications"], OB),
    mcq("END-OB-MCQ-06",
        "Which clinical feature most reliably suggests Cushing's syndrome rather than simple obesity in a patient with central weight gain?",
        ["Acanthosis nigricans",
         "Pale, thin (<0.5 cm) abdominal striae",
         "Proximal muscle weakness with wide (>1 cm) purple abdominal striae and easy bruising",
         "Snoring and daytime sleepiness",
         "Knee osteoarthritis"],
        2,
        """**กล้ามเนื้อต้นแขนต้นขาอ่อนแรง + ท้องลายสีม่วงกว้าง >1 cm + ฟกช้ำง่าย** เป็นลักษณะที่ **จำเพาะ** ต่อ Cushing's syndrome
— สไลด์ระบุในการตรวจร่างกายว่าให้มองหา **purple abdominal striae wider than 1 cm**

**กลไก** — cortisol สูง **สลายโปรตีน** ทำให้ผิวหนังบางและเส้นใยคอลลาเจนขาด (ลายกว้าง สีม่วงเพราะเห็นหลอดเลือดใต้ผิว) ·
หลอดเลือดเปราะ (ฟกช้ำ) · กล้ามเนื้อลีบ (อ่อนแรงส่วนต้น)

**ทำไมข้ออื่นผิด**
- **Acanthosis nigricans** — บอก **insulin resistance** พบได้ในโรคอ้วนทั่วไป
- **ท้องลายสีขาวซีดแคบ** — ลายจากการยืดของผิวในคนอ้วนหรือหลังตั้งครรภ์
- **กรน ง่วงกลางวัน** — OSA · **เข่าเสื่อม** — ภาวะแทรกซ้อนเชิงกลของโรคอ้วน""",
        "ลายท้องสีม่วงกว้าง >1 cm + อ่อนแรงส่วนต้น + ฟกช้ำ → คิดถึง Cushing",
        "Secondary causes of obesity",
        [SLIDE + " — Key obesity-centered physical exam"], OB),
    ])

# ───────────────────────────── 6 ─────────────────────────────
sec("endo-ms-06", "ภาวะแทรกซ้อนของโรคอ้วน",
    "สามกลไก — กายภาพ เมตาบอลิก และจิตใจ · BMI สูงอายุสั้นลงได้ถึง 10 ปี", 8,
"""สไลด์แบ่งภาวะแทรกซ้อนตาม **กลไกที่ทำให้เกิด** ซึ่งช่วยให้จำได้เป็นระบบ

### 1. ผลเชิงกายภาพ (anatomical / mechanical) — จากน้ำหนักและปริมาตรของไขมัน
- **Obstructive sleep apnea (OSA)** และ **obesity hypoventilation syndrome (OHS)**
- **ข้อเข่าเสื่อม (OA)**
- **กรดไหลย้อน (GERD)** และ **Barrett's esophagus** — ความดันในช่องท้องสูงดันกระเพาะ

### 2. ผลเชิงเมตาบอลิก — จากเนื้อเยื่อไขมันที่ทำงานผิดปกติ
- **เบาหวานชนิดที่ 2** ← สัมพันธ์กับโรคอ้วนแรงที่สุด
- **หัวใจและหลอดเลือด** — โรคหลอดเลือดหัวใจ · stroke · หัวใจล้มเหลว · ความดันสูง
- **ตับ** — **MASLD** (metabolic dysfunction-associated steatotic liver disease — ชื่อใหม่ของ NAFLD) · นิ่วในถุงน้ำดี
- **ไขมันผิดปกติ · ไตเรื้อรัง · เกาต์ · หอบหืด**
- **มะเร็ง** — เต้านม (หลังหมดประจำเดือน) · เยื่อบุโพรงมดลูก · รังไข่ · ลำไส้ใหญ่ · ต่อมลูกหมาก · ตับ
- **เจริญพันธุ์** — **PCOS** · มีบุตรยาก · เบาหวานขณะตั้งครรภ์ · อสุจิลดลง
- **หลอดเลือดและผิวหนัง** — เส้นเลือดขอด · **DVT** · stasis dermatitis · **acanthosis nigricans** · psoriasis · ติดเชื้อราตามข้อพับ
- **ภูมิคุ้มกัน** — อักเสบเรื้อรังระดับต่ำ

### 3. ผลเชิงจิตใจ
**ซึมเศร้า · วิตกกังวล · ไม่พอใจรูปร่าง · ความนับถือตัวเองต่ำ** และการถูกตีตรา (weight stigma)

### อายุขัย (Prospective Studies Collaboration, Lancet 2009 — ผู้ใหญ่ 894,576 คน)

| BMI | โอกาสมีชีวิตถึงอายุ 70 ปี | อายุขัยที่ลดลง |
|---|---|---|
| **22.5–25** | **~80%** | — (ต่ำสุด) |
| **30–35** | | **~3 ปี** |
| **35–40** | **~60%** | |
| **40–50** | **~50%** | **8–10 ปี** (เทียบเท่าการสูบบุหรี่) |

### Metabolically healthy obesity (MHO)
คือคนอ้วนที่ **ยังไม่มีความผิดปกติทางเมตาบอลิก** (ความดัน น้ำตาล ไขมันปกติ)
แต่ **ไม่ใช่ภาวะที่ปลอดภัยถาวร** — ส่วนใหญ่จะ **เปลี่ยนเป็น metabolically unhealthy ภายในไม่กี่ปี**
และยังมีภาวะแทรกซ้อนเชิงกายภาพ (OA, OSA) ได้แม้เมตาบอลิกปกติ จึงยังต้องได้รับการดูแล
""",
    ["ภาวะแทรกซ้อนสามกลุ่ม: กายภาพ (OSA, OA, GERD) · เมตาบอลิก (T2D, CVD, MASLD) · จิตใจ",
     "OSA และ OHS = ภาวะแทรกซ้อนเชิงกายภาพที่ต้องคัดกรองเสมอ",
     "MASLD คือชื่อใหม่ของ NAFLD",
     "BMI 30–35 อายุสั้นลง ~3 ปี · BMI 40–50 สั้นลง 8–10 ปี",
     "MHO ไม่ใช่ภาวะถาวร ส่วนใหญ่เปลี่ยนเป็น unhealthy ในไม่กี่ปี"],
    [
    mcq("END-OB-MCQ-07",
        "Which of the following obesity-related complications is primarily caused by the mechanical (anatomical) effect of excess weight rather than by metabolic dysfunction of adipose tissue?",
        ["Type 2 diabetes", "Metabolic dysfunction-associated steatotic liver disease", "Obstructive sleep apnea", "Dyslipidemia", "Polycystic ovary syndrome"],
        2,
        """สไลด์แบ่งภาวะแทรกซ้อนเป็นสามกลุ่ม และ **OSA อยู่ในกลุ่มผลเชิงกายภาพ** ร่วมกับ **OHS · OA · GERD/Barrett's**

**กลไกของ OSA** — ไขมันสะสมรอบคอและลิ้น **ทำให้ทางเดินหายใจส่วนบนแคบ** เมื่อกล้ามเนื้อคลายตัวขณะหลับ ทางเดินหายใจจึงยุบ

**ตัวเลือกอื่นอยู่ในกลุ่มเมตาบอลิกทั้งหมด** — T2D · MASLD · ไขมันผิดปกติ · PCOS เกิดจาก **insulin resistance** และเนื้อเยื่อไขมันที่ทำงานผิดปกติ

**ความสำคัญทางคลินิก** — ภาวะแทรกซ้อนเชิงกายภาพต้องลดน้ำหนัก **มากกว่า** (มักต้อง >10–15%) จึงจะดีขึ้นชัด
ในขณะที่ภาวะเมตาบอลิกดีขึ้นตั้งแต่ลด 5–10%""",
        "ผลเชิงกายภาพ = OSA, OHS, OA, GERD · ผลเชิงเมตาบอลิก = T2D, MASLD, DLP, PCOS",
        "Complications of obesity",
        [SLIDE + " — Complications"], OB),
    mcq("END-OB-MCQ-08",
        "Based on the Prospective Studies Collaboration (Lancet 2009), by approximately how many years is median survival reduced in people with BMI 40–50 kg/m² compared with BMI 22.5–25 kg/m²?",
        ["Less than 1 year", "About 3 years", "8–10 years", "20 years", "No difference after adjusting for smoking"],
        2,
        """**BMI 40–50 → อายุขัยลดลง 8–10 ปี** ซึ่งใกล้เคียงกับผลของการสูบบุหรี่

| BMI | อายุขัยที่ลดลง |
|---|---|
| 30–35 | **~3 ปี** |
| 40–50 | **8–10 ปี** |

และ **โอกาสมีชีวิตถึงอายุ 70 ปี** ลดจาก **~80%** (BMI 22.5–25) เหลือ **~50%** (BMI 40–50)

ข้อมูลนี้เป็นเหตุผลที่สไลด์ย้ำว่า **โรคอ้วนเป็นโรคเรื้อรังที่มีผลต่ออายุขัยอย่างจริงจัง** ไม่ใช่เรื่องรูปลักษณ์""",
        "BMI 30–35: −3 ปี · BMI 40–50: −8 ถึง 10 ปี",
        "Obesity and life expectancy",
        [SLIDE + " — Increased BMI associated with decreased life expectancy", "Prospective Studies Collaboration. Lancet 2009;373:1083-96"], OB),
    ])

# ───────────────────────────── 7 ─────────────────────────────
sec("endo-ms-07", "การประเมินผู้ป่วยโรคอ้วน — ประวัติ ตรวจร่างกาย และแล็บ",
    "ประเมินแบบยึดโรคอ้วนเป็นศูนย์กลาง แล้วตั้งเป้าตามภาวะแทรกซ้อน ไม่ใช่ตาม BMI", 10,
"""### ประวัติที่ต้องถาม (Canadian Adult Obesity CPG 2020)

| หัวข้อ | สิ่งที่ถาม |
|---|---|
| **ประวัติน้ำหนัก** | เริ่มอ้วนเมื่อไร · เหตุการณ์ชีวิตที่เกี่ยวข้อง · น้ำหนักสูงสุดและต่ำสุด · ตอนนี้กำลังขึ้น ลด หรือคงที่ · เคยพยายามลดอย่างไรและได้ผลแค่ไหน |
| **อาหาร** | ความเข้าใจเรื่องอาหาร · พลังงานที่ได้รับ · **กินตามอารมณ์ · กินโดยไม่รู้ตัว** |
| **กิจกรรมทางกาย** | ทำอะไรอยู่ · อะไรเป็นอุปสรรค (ปวด เวลา แรงจูงใจ) |
| **สุขภาพจิต** | **คัดกรองซึมเศร้าและวิตกกังวล** · ADHD · ภาพลักษณ์ของตัวเอง |
| **การเสพติด** | บุหรี่ · สุรา · สารเสพติด · **เครื่องดื่มหวาน** |
| **การนอน** | ชั่วโมงการนอน · ยานอนหลับ · **คัดกรอง sleep apnea ด้วย STOP-BANG** |
| **ยา** | ยาที่มีผลต่อน้ำหนัก (หัวข้อ 5) |
| **สังคม** | ตารางงาน · **ทำงานเป็นกะ** · รายได้ · การเข้าถึงสถานที่ออกกำลังกาย |
| **ครอบครัว** | ญาติสายตรงอ้วนหรือมีภาวะแทรกซ้อน |
| **ความพร้อม** | แรงจูงใจ · ความมั่นใจ · **ความพร้อมที่จะเปลี่ยน** · ความคาดหวัง |

**STOP-BANG** — **S**noring · **T**iredness · **O**bserved apnea · high blood **P**ressure · **B**MI >35 · **A**ge >50 · **N**eck >40 cm · **G**ender ชาย
สไลด์ระบุว่า **STOP-BANG >4 → ส่งปรึกษาแพทย์โรคปอดเพื่อตรวจ sleep apnea**

### ตรวจร่างกาย

| ส่วน | สิ่งที่มองหา |
|---|---|
| **Vital signs** | ความดัน **ด้วย cuff ขนาดเหมาะกับแขน** (cuff เล็กเกินทำให้ค่าสูงเกินจริง) · ชีพจร |
| **สัดส่วนร่างกาย** | น้ำหนัก ส่วนสูง **รอบเอว** BMI |
| **ศีรษะและคอ** | **รอบคอ** · ต่อมไทรอยด์ · **ลักษณะ Cushing** (หน้ากลม ไขมันเหนือไหปลาร้า หนอก) · **ลักษณะ PCOS** (acanthosis, ขนดก, สิว) |
| **หัวใจและปอด** | จังหวะหัวใจ · **อาการหัวใจล้มเหลว** |
| **ท้อง** | **ขนาดตับ** · ไส้เลื่อน |
| **กล้ามเนื้อและข้อ** | ข้อเสื่อม · เกาต์ |
| **ผิวหนัง** | **เชื้อราแคนดิดาและกลากตามข้อพับ** · **ท้องลายสีม่วงกว้าง >1 cm** |
| **ขา** | หลอดเลือดดำไม่พอ · แผลจาก venous stasis |

### แล็บ

| ส่งในผู้ป่วยส่วนใหญ่ | ส่งเมื่อมีข้อบ่งชี้ |
|---|---|
| **FBS, HbA1c** | **TSH, FT4** |
| **Electrolytes, การทำงานของไต** | กรดยูริก |
| **Lipid profile** | ธาตุเหล็ก · วิตามินดี |
| **ALT** (คัดกรอง MASLD) | ปัสสาวะ |
| **CBC** | **หญิงที่มีอาการ PCOS** — LH, FSH, total testosterone, prolactin |
| **คัดกรองมะเร็งตามวัย** | |

### ทีมที่ควรส่งปรึกษา
นักกำหนดอาหาร · ผู้เชี่ยวชาญการออกกำลังกาย · จิตแพทย์หรือนักจิตวิทยา · แพทย์ต่อมไร้ท่อ ·
**แพทย์โรคปอด (STOP-BANG >4)** · แพทย์โรคหัวใจ · ศัลยแพทย์

### ตั้งเป้า — complication-centric ไม่ใช่ BMI-centric
เป้าหมายไม่ใช่การพา BMI กลับสู่ค่าปกติ แต่คือ **ลดน้ำหนักให้พอที่ภาวะแทรกซ้อนดีขึ้น**
ซึ่งส่งผลให้ **คุณภาพชีวิตดีขึ้นและอายุยืนขึ้น**

**ตัวอย่างจากสไลด์** — น้ำหนัก **100 kg** สูง **165 cm** → BMI **37**
- เป้าแรก: **ลด 3–10% = 3–10 kg ใน 6 เดือน** (เหลือ 90–97 kg)
- ถ้าจะให้ BMI ปกติ (22.9) ต้องเหลือ **63 kg** · ให้แค่ BMI น้ำหนักเกิน (27.4) ต้องเหลือ **75 kg** — **ไม่สมจริงเป็นเป้าแรก**

| น้ำหนักที่ลด | สิ่งที่ดีขึ้น (โดยประมาณ) |
|---|---|
| **5–10%** | น้ำตาล ความดัน TG · ป้องกันเบาหวาน · PCOS |
| **10–15%** | **MASLD** · **OSA** · ข้อเข่าเสื่อม · GERD · **เบาหวานเข้าสู่ระยะสงบ** |
| **>15%** | โรคหัวใจและหลอดเลือด · อัตราตาย |

### เบาหวานเข้าสู่ระยะสงบ (diabetes remission)
แนวทางไทย (2565) ใช้ **การปรับพฤติกรรมอย่างเข้มงวด** — อาหารพลังงานต่ำ · คาร์โบไฮเดรตต่ำ · อาหารจากพืช · การอดอาหารเป็นช่วงเวลา
กลไกตาม **twin cycle hypothesis** — ลดน้ำหนัก → **ไขมันในตับลด** (ตับกลับมาไวต่ออินซูลิน) → **ไขมันในตับอ่อนลด** (β-cell กลับมาทำงาน)
นิยามระยะสงบ (ADA 2021) — **HbA1c <6.5% อย่างน้อย 3 เดือนหลังหยุดยาลดน้ำตาล**
""",
    ["STOP-BANG >4 → ส่งแพทย์โรคปอดตรวจ sleep apnea",
     "วัดความดันด้วย cuff ขนาดเหมาะ — cuff เล็กเกินให้ค่าสูงเกินจริง",
     "แล็บพื้นฐาน: FBS/HbA1c · electrolytes · ไต · lipid · ALT · CBC · คัดกรองมะเร็ง",
     "TSH ส่งเมื่อมีข้อบ่งชี้เท่านั้น · PCOS ส่ง LH, FSH, testosterone, prolactin",
     "เป้าแรก = ลด 5–10% ใน 6 เดือน ไม่ใช่ BMI ปกติ",
     "Remission = HbA1c <6.5% ≥3 เดือนหลังหยุดยา"],
    [
    mcq("END-OB-MCQ-09",
        "A 44-year-old man, BMI 36 kg/m², neck circumference 44 cm, BP 146/92 mmHg, reports loud snoring and daytime sleepiness; his wife has seen him stop breathing at night. According to the lecture, what is the most appropriate next step?",
        ["Reassure — snoring is expected with obesity",
         "Prescribe a hypnotic to improve sleep quality",
         "Refer to a pulmonologist for evaluation of obstructive sleep apnea",
         "Order a thyroid function test first",
         "Start phentermine to reduce weight quickly"],
        2,
        """**คำนวณ STOP-BANG** — **S**noring ✅ · **T**iredness ✅ · **O**bserved apnea ✅ · **P**ressure สูง ✅ · **B**MI >35 ✅ · **A**ge >50 ❌ · **N**eck >40 ✅ · **G**ender ชาย ✅ = **7 คะแนน**

สไลด์ระบุว่า **STOP-BANG >4 → ส่งปรึกษาแพทย์โรคปอดเพื่อตรวจ sleep apnea** (polysomnography)

**ทำไมข้ออื่นผิด**
- **ปลอบใจว่ากรนเป็นเรื่องปกติ** — พลาด OSA ซึ่งเพิ่มความเสี่ยงความดันสูงดื้อยา หัวใจเต้นผิดจังหวะ และอุบัติเหตุ
- **ยานอนหลับ** — **กดการหายใจ** ทำให้ OSA แย่ลงและอันตราย
- **Phentermine** — เป็นยากระตุ้นซิมพาเทติก **ห้ามในความดันสูงที่คุมไม่ได้**
- **TSH** ส่งเมื่อมีข้อบ่งชี้ ไม่ใช่ขั้นตอนหลักของปัญหานี้""",
        "STOP-BANG >4 → ส่งตรวจ sleep study · ห้ามให้ยานอนหลับในผู้ที่สงสัย OSA",
        "OSA screening in obesity",
        [SLIDE + " — Key obesity-centered medical history / Consultation"], OB),
    mcq("END-OB-MCQ-10",
        "A 38-year-old woman weighs 100 kg, height 165 cm (BMI 37 kg/m²), with prediabetes and knee pain. What is the most appropriate initial weight-loss goal?",
        ["Reach normal BMI (about 63 kg) within 6 months",
         "Lose 3–10% of body weight (about 3–10 kg) over 6 months",
         "Lose 30 kg within 3 months with a very-low-calorie diet",
         "Maintain current weight; weight loss is unlikely to help",
         "Lose 1 kg per week indefinitely"],
        1,
        """ตัวอย่างนี้มาจากสไลด์โดยตรง — **เป้าแรก = ลด 3–10% ของน้ำหนักใน 6 เดือน** = 3–10 kg (เหลือ 90–97 kg)

**เหตุผล**
- ลดเพียง **5–10%** ก็ทำให้ **prediabetes ดีขึ้นและลดการเกิดเบาหวาน** ได้ชัดเจน
- เป้าที่ **ทำได้จริง** เพิ่มโอกาสสำเร็จและลดการกลับมาอ้วนซ้ำ
- ใช้แนวคิด **complication-centric** — ตั้งเป้าให้ภาวะแทรกซ้อนดีขึ้น ไม่ใช่ให้ BMI ปกติ

**ทำไมข้ออื่นผิด**
- **ให้ BMI ปกติ (63 kg)** = ต้องลด 37 kg — ไม่สมจริงเป็นเป้าแรก
- **ลด 30 kg ใน 3 เดือน** — เร็วเกิน เสี่ยงนิ่วในถุงน้ำดีและสูญเสียกล้ามเนื้อ
- **คงน้ำหนัก** — ผิด เพราะการลดน้ำหนักช่วยทั้งน้ำตาลและข้อเข่า""",
        "เป้าแรกของการลดน้ำหนัก = 5–10% ใน 6 เดือน",
        "Weight-loss goal setting",
        [SLIDE + " — Metabolic healthy obesity (MHO) example / Goal of weight loss"], OB),
    mcq("END-OB-MCQ-11",
        "Which set of laboratory tests should be considered for most patients presenting for obesity management according to the Canadian Adult Obesity CPG 2020 shown in the lecture?",
        ["TSH, FT4, cortisol, prolactin",
         "Fasting glucose/HbA1c, lipid profile, ALT, electrolytes and renal function, CBC",
         "Serum leptin and insulin levels",
         "Vitamin D, iron studies, uric acid",
         "LH, FSH, total testosterone for all women"],
        1,
        """**แล็บพื้นฐานที่ส่งในผู้ป่วยส่วนใหญ่** — **FBS/HbA1c · electrolytes และการทำงานของไต · lipid profile · ALT · CBC** และคัดกรองมะเร็งตามวัย

แต่ละตัวมีเหตุผล — น้ำตาลหาเบาหวาน · lipid หาไขมันผิดปกติ · **ALT หา MASLD** · ไตหา CKD

**ส่งเมื่อมีข้อบ่งชี้เท่านั้น** — **TSH/FT4** · กรดยูริก · ธาตุเหล็ก · วิตามินดี · ปัสสาวะ ·
และ **LH, FSH, testosterone, prolactin เฉพาะหญิงที่มีอาการของ PCOS**

**Leptin และ insulin** ไม่ใช้ในเวชปฏิบัติ เพราะไม่เปลี่ยนการรักษา""",
        "แล็บพื้นฐานโรคอ้วน: glucose/HbA1c · lipid · ALT · ไต · CBC — TSH ส่งตามข้อบ่งชี้",
        "Laboratory evaluation of obesity",
        [SLIDE + " — Laboratory and diagnostic tests to consider"], OB),
    ])

# ───────────────────────────── 8 ─────────────────────────────
sec("endo-ms-08", "รักษาโรคอ้วน — อาหาร การออกกำลังกาย และยาลดน้ำหนัก",
    "ปรับพฤติกรรมอย่างน้อย 3 เดือน · ยาเป็นตัวเสริม · ประเมินผลที่ 3–5 เดือน", 13,
"""### 1. อาหาร

| รูปแบบ | รายละเอียดตามสไลด์ |
|---|---|
| **Very-low-calorie diet (VLCD)** | **<800 kcal/วัน** — ใช้ช่วงสั้นภายใต้การดูแลของแพทย์ |
| **Balanced low-energy diet** | **1,000–1,200 kcal/วัน** · คาร์บ 50–55% · โปรตีน 15–20% · ไขมัน 30–35% |
| **Moderate energy แบบอื่น** | คาร์บสูงไขมันต่ำ · คาร์บต่ำไขมันสูง · ไขมัน 30% + โปรตีนสูง 25% |

**หลักสำคัญ** — สัดส่วนสารอาหารแบบไหนก็ลดน้ำหนักได้ใกล้เคียงกันในระยะยาว
สิ่งที่ตัดสินผลคือ **พลังงานที่ขาดดุล** และ **ความสามารถทำได้ต่อเนื่อง** ให้เลือกแบบที่ผู้ป่วยทำได้จริง
และลด **อาหารแปรรูปสูง (UPFs) · เครื่องดื่มหวาน** เพิ่มอาหารจากพืช

### 2. การออกกำลังกาย
**แอโรบิก + ต้านแรง (resistance)** — แอโรบิกเผาผลาญพลังงาน ส่วนการฝึกต้านแรง **รักษามวลกล้ามเนื้อ** ขณะลดน้ำหนัก
การออกกำลังกายอย่างเดียวลดน้ำหนักได้ไม่มาก แต่ **สำคัญที่สุดในการคงน้ำหนักหลังลด** และลดความเสี่ยงความดัน มะเร็ง กระดูกพรุน เบาหวาน stroke ซึมเศร้า

### 3. การปรับพฤติกรรมอย่างครบวงจร (comprehensive behavioral intervention)
ตั้งเป้า · จดบันทึก · สื่อสารสร้างแรงจูงใจ · ติดตามสม่ำเสมอ

### 4. ยาลดน้ำหนัก (anti-obesity medications, AOMs)

**กฎสามข้อจากสไลด์**
- ต้อง **ปรับพฤติกรรมอย่างน้อย 3 เดือน** ก่อน
- ถ้าปรับพฤติกรรมแล้ว **ลดได้ >10%** → **ไม่จำเป็นต้องเริ่มยา**
- ใช้ยาไป **3–5 เดือนแล้วลดได้ <5%** → **พิจารณาหยุดยา** (ถือว่าไม่ตอบสนอง)

**ข้อบ่งชี้** — ใช้ **เสริม** การปรับพฤติกรรมในผู้ที่มีแรงจูงใจ

| เกณฑ์ | BMI |
|---|---|
| **สากล** | **≥30** หรือ **≥27 ร่วมกับโรคร่วม** จากโรคอ้วน |
| **เอเชีย (สไลด์)** | **≥27** หรือ **≥25 ร่วมกับ T2D · ความดันสูง · ไขมันผิดปกติ** |

**ข้อห้ามทั่วไปของ AOMs** — **อายุ <12 ปี · ตั้งครรภ์ · ใช้โดยไม่อยู่ในความดูแลของแพทย์**

### ยาแต่ละตัว

| ยา | กลไก | ข้อควรรู้ |
|---|---|---|
| **Orlistat** | **ยับยั้ง pancreatic lipase** → ดูดซึมไขมันลด ~30% (**energy wastage** — ตัวเดียวที่ไม่ได้ลดความอยากอาหาร) | อุจจาระมันเยิ้ม ผายลมมีน้ำมัน · **ขาดวิตามินที่ละลายในไขมัน (A D E K)** · ห้ามใน malabsorption เรื้อรังและ cholestasis |
| **Phentermine** | กระตุ้น **norepinephrine** → ลดความอยากอาหาร | **ใช้ระยะสั้น** · ห้ามใน **โรคหัวใจและหลอดเลือด ความดันที่คุมไม่ได้** hyperthyroid ต้อหิน ใช้ MAOI |
| **Phentermine/topiramate** | + topiramate (**GABA**) | topiramate **ทำให้พิการแต่กำเนิด (ปากแหว่ง)** ต้องคุมกำเนิด · นิ่วไต · ชาปลายมือ |
| **Naltrexone/bupropion** | bupropion กระตุ้น **POMC** · naltrexone ตัดวง feedback ของ **opioid (MOP-R)** | ห้ามใน **ลมชัก** · ความดันที่คุมไม่ได้ · **ใช้ opioid** · bulimia/anorexia · เตือนเรื่องความคิดฆ่าตัวตาย |
| **Liraglutide 3.0 mg** | **GLP-1RA** ฉีดวันละครั้ง | คลื่นไส้อาเจียน · นิ่วถุงน้ำดี · ตับอ่อนอักเสบ |
| **Semaglutide 2.4 mg/สัปดาห์** | **GLP-1RA** ฉีดสัปดาห์ละครั้ง (FDA อนุมัติ **มิ.ย. 2021**) | ลดน้ำหนัก ~15% |
| **Tirzepatide** | **GIP + GLP-1 dual agonist** | ลดน้ำหนัก ~20% — มากที่สุดในกลุ่มยา |

**ข้อห้ามของกลุ่ม GLP-1RA** — **ประวัติตนเองหรือครอบครัวเป็น medullary thyroid carcinoma หรือ MEN2** · ตั้งครรภ์ · เคยเป็นตับอ่อนอักเสบ (ระวัง)

### Semaglutide 2.4 mg — รายละเอียดที่สไลด์ให้
- **ปากกา 5 สี 5 ขนาด** — **0.25 → 0.5 → 1.0 → 1.7 → 2.4 mg** เพิ่มทุก 4 สัปดาห์ (**Start · Step up · Stay**)
  เพิ่มช้าเพื่อลดอาการคลื่นไส้
- **เก็บในตู้เย็น 2–8°C** · หลังเปิดใช้เก็บที่อุณหภูมิห้อง **<30°C ได้นานสุด 6 สัปดาห์**
- **ลืมฉีด** — ถ้ายังไม่เกิน **5 วัน** ให้ฉีดทันที · ถ้า **เกิน 5 วัน ให้ข้ามเข็มนั้น** แล้วฉีดตามวันเดิมครั้งถัดไป
- ระหว่างใช้ยา ต้อง **ได้รับโปรตีนเพียงพอและฝึกต้านแรง** เพื่อรักษามวลกล้ามเนื้อ (Mozaffarian, Obesity 2025)
""",
    ["ปรับพฤติกรรม ≥3 เดือนก่อนให้ยา · ลดได้ >10% ไม่ต้องใช้ยา",
     "ใช้ยา 3–5 เดือนแล้วลด <5% → พิจารณาหยุด",
     "ข้อบ่งชี้ AOM: BMI ≥30 หรือ ≥27 + โรคร่วม (เอเชีย ≥25 + T2D/HT/DLP)",
     "Orlistat = lipase inhibitor · ตัวเดียวที่ไม่ลดความอยากอาหาร · ขาดวิตามิน ADEK",
     "Phentermine ห้ามในโรคหัวใจและความดันที่คุมไม่ได้",
     "Topiramate ทำให้ปากแหว่ง · bupropion ห้ามในลมชัก",
     "GLP-1RA ห้ามในประวัติ MTC/MEN2",
     "Semaglutide ลืมฉีด ≤5 วันฉีดทันที · >5 วันข้าม"],
    [
    mcq("END-OB-MCQ-12",
        "A 34-year-old woman with obesity asks about orlistat. Which adverse effect or precaution is specific to its mechanism of action?",
        ["Tachycardia and elevated blood pressure",
         "Increased risk of seizures",
         "Oily spotting, steatorrhoea and deficiency of fat-soluble vitamins",
         "Teratogenicity causing oral clefts",
         "Risk of medullary thyroid carcinoma in rodents"],
        2,
        """**Orlistat ยับยั้ง pancreatic lipase** ในลำไส้ → ไขมันจากอาหาร **~30% ไม่ถูกย่อยและถูกขับออกทางอุจจาระ**
สไลด์จัดกลไกนี้ว่า **energy wastage** ซึ่งเป็นยาตัวเดียวในตารางที่ **ไม่ได้ลดความอยากอาหาร**

**ผลที่ตามมาโดยตรงจากกลไก**
- **อุจจาระมันเยิ้ม · ผายลมมีน้ำมัน · กลั้นอุจจาระไม่อยู่** — ยิ่งกินไขมันมากยิ่งเป็นมาก (ทำหน้าที่เหมือน "ตัวลงโทษ" การกินไขมัน)
- **ดูดซึมวิตามิน A D E K ลดลง** → ควรให้วิตามินรวม **ห่างจากยาอย่างน้อย 2 ชั่วโมง**

**ตัวเลือกอื่นเป็นของยาตัวอื่น** — ใจสั่นความดันสูง = **phentermine** · ชัก = **bupropion** · ปากแหว่ง = **topiramate** · MTC = **GLP-1RA**""",
        "Orlistat = lipase inhibitor → อุจจาระมัน + ขาดวิตามิน ADEK",
        "Orlistat",
        [SLIDE + " — Pharmacological options for weight management / Mode of action"], OB),
    mcq("END-OB-MCQ-13",
        "A 29-year-old woman with BMI 33 kg/m² and a history of epilepsy on levetiracetam requests medication for weight loss. Which agent is contraindicated?",
        ["Orlistat", "Liraglutide 3.0 mg", "Semaglutide 2.4 mg", "Naltrexone/bupropion", "Tirzepatide"],
        3,
        """**Bupropion ลดเกณฑ์การชัก (lowers seizure threshold)** จึง **ห้ามใช้ในผู้ที่มีประวัติลมชัก**
รวมถึงผู้ที่เพิ่งหยุดสุราหรือ benzodiazepine และผู้ที่เป็น **bulimia หรือ anorexia nervosa** (อิเล็กโทรไลต์ผิดปกติ เสี่ยงชัก)

**ข้อห้ามอื่นของ naltrexone/bupropion** — ความดันที่คุมไม่ได้ · **ใช้ยากลุ่ม opioid** (naltrexone ทำให้ถอนยาเฉียบพลันและยาแก้ปวดไม่ได้ผล) · ใช้ MAOI

**ทางเลือกที่ปลอดภัยสำหรับผู้ป่วยรายนี้** — orlistat หรือกลุ่ม GLP-1RA (liraglutide, semaglutide, tirzepatide)
แต่ต้อง **คุมกำเนิด** เพราะ AOMs ทุกตัวห้ามใช้ในการตั้งครรภ์""",
        "Bupropion ห้ามในลมชัก · naltrexone ห้ามในผู้ใช้ opioid",
        "Naltrexone/bupropion contraindications",
        [SLIDE + " — Pharmacological options for weight management", "FDA prescribing information — Contrave"], OB),
    mcq("END-OB-MCQ-14",
        "A patient on semaglutide 2.4 mg once weekly (scheduled every Monday) realises on Sunday that she forgot Monday's dose. What should she do?",
        ["Inject immediately, then continue on Monday as usual",
         "Skip the missed dose and inject the next dose on Monday as scheduled",
         "Inject two doses on Monday to catch up",
         "Restart the titration from 0.25 mg",
         "Inject immediately and change her regular day to Saturday"],
        1,
        """จันทร์ถึงอาทิตย์ = **6 วันผ่านไปแล้ว** — เกิน 5 วัน

กฎที่สไลด์ให้ไว้
- **ลืมไม่เกิน 5 วัน** → **ฉีดทันที** แล้วกลับไปตามวันเดิม
- **เกิน 5 วัน** → **ข้ามเข็มนั้น** แล้วฉีดครั้งถัดไป **ตามวันที่กำหนดเดิม**

ถ้าฉีดวันอาทิตย์แล้วต้องฉีดอีกทีวันจันทร์ **สองเข็มจะห่างกันแค่ 1 วัน**
นี่คือเหตุผลของกฎ 5 วัน — **ป้องกันไม่ให้สองเข็มห่างกันน้อยกว่า 2 วัน** ซึ่งทำให้ระดับยาสูงเกินและคลื่นไส้อาเจียนมาก
ผู้ป่วยรายนี้จึงต้อง **ข้ามเข็มนั้นแล้วฉีดวันจันทร์ตามปกติ** (ถ้านึกได้วันเสาร์ซึ่งยังอยู่ในกรอบ 5 วัน ให้ฉีดทันที)

**ทำไมข้ออื่นผิด** — **ฉีดสองเข็มชดเชย** อันตรายชัดเจน · **เริ่ม titrate ใหม่** จำเป็นเฉพาะเมื่อขาดยาหลายสัปดาห์ (โดยทั่วไป ≥2 สัปดาห์)""",
        "Semaglutide ลืมฉีด: ≤5 วันฉีดทันที · >5 วันข้าม ห้ามฉีดชดเชยสองเข็ม",
        "Semaglutide missed dose",
        [SLIDE + " — Semaglutide dose escalation / Misses a dose"], OB),
    mcq("END-OB-MCQ-15",
        "A 46-year-old man (BMI 31 kg/m²) completed 3 months of lifestyle therapy and then started liraglutide 3.0 mg. After 4 months at the maintenance dose he has lost only 3% of body weight. What is the most appropriate action?",
        ["Continue indefinitely — any weight loss is beneficial",
         "Double the dose to 6 mg daily",
         "Consider stopping the drug and reassessing treatment options",
         "Add phentermine to liraglutide",
         "Stop all lifestyle interventions as they have failed"],
        2,
        """สไลด์ให้กฎไว้ชัด — **ใช้ยา 3–5 เดือนแล้วลดได้ <5% → พิจารณาหยุดยา** เพราะถือว่า **ไม่ตอบสนอง**
และการใช้ยาต่อจะมีแต่ค่าใช้จ่ายและผลข้างเคียงโดยไม่ได้ประโยชน์

**ขั้นต่อไป** — ทบทวนการกินและการออกกำลังกายใหม่ · เปลี่ยนเป็นยาที่กลไกต่างออกไป ·
หรือถ้า BMI และโรคร่วมเข้าเกณฑ์ ให้พิจารณา **metabolic and bariatric surgery**

**ทำไมข้ออื่นผิด**
- **เพิ่มขนาดเป็น 6 mg** — ขนาดสูงสุดของ liraglutide คือ 3.0 mg
- **เติม phentermine** — ไม่มีข้อมูลสนับสนุนการใช้ร่วมกับ GLP-1RA
- **หยุดปรับพฤติกรรม** — ผิดหลัก การปรับพฤติกรรมต้องทำตลอดไม่ว่าจะใช้ยาหรือผ่าตัด""",
        "AOM 3–5 เดือนแล้วลด <5% = ไม่ตอบสนอง → หยุดและทบทวนแผน",
        "Stopping rule for AOM",
        [SLIDE + " — Antiobesity medications"], OB),
    ])

# ───────────────────────────── 9 ─────────────────────────────
sec("endo-ms-09", "ผ่าตัดลดน้ำหนัก (metabolic and bariatric surgery)",
    "เกณฑ์สากล ASMBS/IFSO 2022 และเกณฑ์ไทย 2564 ที่ใช้จุดตัด 27.5 / 32.5 / 37.5", 8,
"""### เกณฑ์สากล — ASMBS/IFSO 2022

| BMI | คำแนะนำ |
|---|---|
| **≥35** | **แนะนำอย่างยิ่ง** ไม่ว่าจะมีโรคร่วมหรือไม่ |
| **≥30 ร่วมกับ T2D** | **แนะนำ** |
| **30–34.9** | **ควรพิจารณา** ในผู้ที่ลดน้ำหนักหรือคุมโรคร่วมด้วยวิธีที่ไม่ผ่าตัดไม่สำเร็จ |
| **คนเอเชีย >27.5** | **ควรเสนอ** การผ่าตัด |

การเปลี่ยนแปลงสำคัญจากเกณฑ์ NIH 1991 เดิม (≥40 หรือ ≥35 + โรคร่วม) คือ **ลดเกณฑ์ลงหนึ่งระดับ**
เพราะหลักฐานระยะยาวแสดงว่าผ่าตัดปลอดภัยและได้ผลกว่าการรักษาแบบไม่ผ่าตัด

### เกณฑ์ไทย — แนวทางเวชปฏิบัติการผ่าตัดรักษาโรคอ้วน พ.ศ. 2564

| BMI | เงื่อนไข |
|---|---|
| **≥37.5** | **ผ่าตัดได้โดยไม่ต้องมีโรคร่วม** |
| **≥32.5** | ร่วมกับ **โรคร่วม** ที่คุมได้ไม่ดีแม้รักษาอย่างเต็มที่ |
| **≥30** | ร่วมกับ **T2D หรือ MetS** ที่คุมไม่ได้ด้วยการปรับพฤติกรรมและการรักษามาตรฐาน — **เป็นทางเลือก** |
| **27.5–30** | ร่วมกับ T2D หรือ MetS ที่คุมไม่ได้ — **ทำได้เฉพาะในงานวิจัย** ภายใต้การดูแลเข้มงวด ผู้ป่วยยินยอม และผ่านคณะกรรมการจริยธรรม |

**สังเกตว่าเกณฑ์ไทยใช้จุดตัดเอเชีย 27.5 / 32.5 / 37.5** (หัวข้อ 4) ซึ่งเท่ากับเกณฑ์ตะวันตก 30 / 35 / 40 ขยับลง 2.5

**เงื่อนไขอื่นของเกณฑ์ไทย**
- **อายุ 18–65 ปี** (นอกช่วงนี้พิจารณาเป็นรายบุคคล)
- ผู้ป่วยต้องมี **ความตั้งใจจริง** และ **เข้าใจกระบวนการผ่าตัดและการดูแลหลังผ่าตัด** อย่างละเอียด
- ควร **ลดน้ำหนักให้ได้ 5–10% ก่อนผ่าตัด** — ตับเล็กลงทำให้ผ่าตัดส่องกล้องง่ายขึ้น และเป็นการพิสูจน์ความตั้งใจ
- ช่วงเตรียมตัว ต้อง **มาตามนัดทุกครั้ง หรืออย่างน้อย 80%** ของนัดทั้งหมด

**วิธีผ่าตัดที่แนะนำ** — **Roux-en-Y gastric bypass (RYGB)** และ **sleeve gastrectomy**

| | Sleeve gastrectomy | RYGB |
|---|---|---|
| **หลักการ** | ตัดกระเพาะออก ~80% เหลือเป็นท่อ | กระเพาะเล็ก + ต่อข้ามลำไส้ส่วนต้น |
| **เด่นเรื่อง** | ทำง่ายกว่า ขาดสารอาหารน้อยกว่า | **เบาหวานเข้าสู่ระยะสงบดีกว่า** · **ช่วย GERD** |
| **ข้อเสีย** | **GERD แย่ลงได้** | ขาดธาตุเหล็ก B12 แคลเซียม · dumping · ลำไส้อุดตันจาก internal hernia |

**ทำไมการผ่าตัดได้ผลเกินกว่าการ "จำกัดปริมาณอาหาร"** — การผ่าตัดเปลี่ยน **ฮอร์โมนลำไส้** (GLP-1 และ PYY เพิ่ม · ghrelin ลดหลัง sleeve)
น้ำตาลของผู้ป่วยเบาหวานจึงมักดีขึ้น **ภายในไม่กี่วัน ก่อนที่น้ำหนักจะลดมาก** — จึงเรียกว่า **metabolic** surgery
""",
    ["สากล 2022: BMI ≥35 แนะนำเสมอ · ≥30 + T2D แนะนำ · เอเชีย >27.5 ควรเสนอ",
     "ไทย 2564: ≥37.5 ไม่ต้องมีโรคร่วม · ≥32.5 + โรคร่วม · ≥30 + T2D/MetS เป็นทางเลือก",
     "BMI 27.5–30 ผ่าตัดได้เฉพาะในงานวิจัย",
     "อายุ 18–65 · ลดน้ำหนัก 5–10% ก่อนผ่าตัด · มาตามนัด ≥80%",
     "วิธีที่แนะนำ: RYGB และ sleeve gastrectomy · sleeve ทำให้ GERD แย่ลงได้"],
    [
    mcq("END-OB-MCQ-16",
        "A 42-year-old Thai woman with BMI 38 kg/m² has no diabetes, hypertension or other obesity-related co-morbidities. She has tried supervised lifestyle therapy for 1 year without success. According to the Thai 2021 guideline, is she eligible for bariatric surgery?",
        ["No — surgery requires at least one co-morbidity",
         "No — surgery requires BMI ≥40 kg/m²",
         "Yes — BMI ≥37.5 kg/m² qualifies regardless of co-morbidities",
         "Only in a research setting",
         "No — she must first fail anti-obesity medication for 2 years"],
        2,
        """เกณฑ์ไทย 2564 — **BMI ≥37.5 ผ่าตัดได้โดยไม่ต้องมีโรคร่วม** → ผู้ป่วย BMI 38 **เข้าเกณฑ์**

อายุ 42 ปีอยู่ในช่วง **18–65 ปี** และเคยลองปรับพฤติกรรมอย่างมีผู้ดูแลแล้ว

**ทำไมข้ออื่นผิด**
- **ต้องมีโรคร่วม** — ใช้กับ BMI ≥32.5 แต่ <37.5 เท่านั้น
- **ต้อง BMI ≥40** — คือเกณฑ์ NIH 1991 ของคนตะวันตก ซึ่งเก่าและไม่ปรับตามเชื้อชาติ
- **เฉพาะในงานวิจัย** — ใช้กับ BMI 27.5–30
- **ต้องลองยาก่อน 2 ปี** — ไม่มีในเกณฑ์

**ก่อนผ่าตัด** — ควรลดน้ำหนักให้ได้ 5–10% และมาตามนัดอย่างน้อย 80%""",
        "ไทย: BMI ≥37.5 ผ่าตัดได้เลยโดยไม่ต้องมีโรคร่วม",
        "Bariatric surgery indications (Thai)",
        [SLIDE + " — Indication for MBS (แนวทางไทย พ.ศ. 2564)"], OB),
    mcq("END-OB-MCQ-17",
        "A 50-year-old man with long-standing type 2 diabetes (HbA1c 9.1% despite three agents), severe erosive GERD, and BMI 36 kg/m² is referred for metabolic surgery. Which procedure is generally preferred for him?",
        ["Sleeve gastrectomy, because it improves GERD",
         "Roux-en-Y gastric bypass, because it improves GERD and achieves higher diabetes remission rates",
         "Adjustable gastric banding",
         "Intragastric balloon",
         "No surgery — GERD is a contraindication to all bariatric procedures"],
        1,
        """**RYGB** เหมาะกับผู้ป่วยรายนี้ด้วยเหตุผลสองข้อ

1. **GERD** — RYGB สร้างกระเพาะเล็กที่ผลิตกรดน้อยและเบี่ยงน้ำดีออกไป **อาการกรดไหลย้อนจึงดีขึ้น**
   ขณะที่ **sleeve gastrectomy เพิ่มความดันในกระเพาะรูปท่อ → GERD มักแย่ลงหรือเกิดใหม่**
2. **เบาหวาน** — RYGB ให้ **อัตราเบาหวานเข้าสู่ระยะสงบสูงกว่า** sleeve ในการศึกษาส่วนใหญ่

สไลด์ระบุว่าวิธีที่แนะนำคือ **RYGB และ sleeve** — การเลือกระหว่างสองวิธีขึ้นกับโรคร่วมแบบนี้

**ทำไมข้ออื่นผิด** — **Gastric banding** ผลระยะยาวไม่ดีและต้องผ่าตัดซ้ำบ่อย จึงแทบเลิกใช้ ·
**Intragastric balloon** ใช้ชั่วคราว · **GERD ไม่ใช่ข้อห้าม** แต่เป็นตัวช่วยเลือกวิธีผ่าตัด""",
        "มี GERD → เลือก RYGB ไม่ใช่ sleeve · RYGB ทำให้เบาหวานสงบได้มากกว่า",
        "Choice of bariatric procedure",
        [SLIDE + " — Indication for MBS", "Eisenberg D et al. SOARD 2022 (ASMBS/IFSO)"], OB),
    ])

# ───────────────────────────── 10 ─────────────────────────────
sec("endo-ms-10", "Lipoprotein metabolism — exogenous กับ endogenous pathway",
    "ไขมันจากอาหารเดินทางด้วย chylomicron · ไขมันจากตับเดินทางด้วย VLDL → IDL → LDL", 11,
"""สไลด์เปิดส่วน dyslipidemia ด้วยหลักว่า **คอเลสเตอรอลในเลือดมาจากสองทาง** และ **ถูกบรรจุในอนุภาค lipoprotein เสมอ**
โดยแต่ละอนุภาคมี **apolipoprotein** ประจำตัวที่กำหนดว่าจะไปที่ไหน

### Apolipoprotein ที่ต้องรู้

| Apo | อยู่บน | หน้าที่ |
|---|---|---|
| **B-48** | chylomicron | โครงสร้าง (ผลิตจากลำไส้) |
| **B-100** | VLDL · IDL · LDL | โครงสร้าง + **จับกับ LDL receptor** |
| **C-II** | chylomicron · VLDL | **กระตุ้น lipoprotein lipase (LPL)** |
| **E** | chylomicron remnant · IDL | **ให้ตับจับและเก็บ remnant กลับ** |
| **A-I** | HDL | โครงสร้าง + **กระตุ้น LCAT** |

### Exogenous pathway — ไขมันจากอาหาร (ลำไส้ → ตับ)
1. ลำไส้เล็กดูดซึม TG และคอเลสเตอรอลจากอาหาร → บรรจุเป็น **chylomicron (apoB-48)**
2. ออกทาง **ท่อน้ำเหลือง** เข้ากระแสเลือด → รับ **apoC-II และ apoE** จาก HDL
3. **LPL** บนผนังหลอดเลือดฝอยของกล้ามเนื้อและไขมัน (ถูกกระตุ้นด้วย apoC-II) ย่อย TG → **กรดไขมันเข้าเนื้อเยื่อ**
4. เหลือเป็น **chylomicron remnant** ที่อุดมคอเลสเตอรอล → **ตับจับเก็บผ่าน apoE**

### Endogenous pathway — ไขมันที่ตับสร้าง (ตับ → เนื้อเยื่อ)
1. ตับบรรจุ TG และคอเลสเตอรอลเป็น **VLDL (apoB-100)**
2. **LPL** ย่อย TG ใน VLDL → กลายเป็น **IDL**
3. IDL ส่วนหนึ่ง **กลับเข้าตับ** (ผ่าน apoE) ส่วนที่เหลือถูก **hepatic lipase** ย่อยต่อเป็น **LDL**
4. **LDL** (อุดมคอเลสเตอรอลที่สุด) ถูกดึงออกจากเลือดโดย **LDL receptor** ที่ตับ (~70%) และเนื้อเยื่ออื่น ผ่าน **apoB-100**

### Reverse cholesterol transport — HDL
HDL (apoA-I) รับคอเลสเตอรอลส่วนเกินจากเซลล์ผ่าน **ABCA1** → **LCAT** เปลี่ยนเป็น cholesteryl ester → ส่งคืนตับ
**CETP** แลกเปลี่ยน cholesteryl ester จาก HDL กับ TG จาก VLDL/LDL

### LDL receptor กับ PCSK9 — กุญแจของการรักษา
- เซลล์ตับที่ **คอเลสเตอรอลภายในลดลง** (เช่นจาก statin) → กระตุ้น **SREBP-2** → **สร้าง LDL receptor มากขึ้น** → ดึง LDL ออกจากเลือดมากขึ้น
- **PCSK9** จับกับ LDL receptor แล้วพาเข้าไป **ถูกทำลายใน lysosome** แทนที่จะวนกลับมาใช้ใหม่
- ยา **PCSK9 inhibitor** จึงทำให้ LDL receptor อยู่ได้นานขึ้น และเสริมฤทธิ์ statin

### จาก LDL สู่ plaque (Moore & Tabas 2011)
1. **LDL แทรกเข้าผนังหลอดเลือดชั้น intima** โดยเฉพาะจุดที่ endothelium เสียหาย แล้วถูก **ออกซิไดซ์**
2. endothelium แสดง adhesion molecule → **monocyte เข้ามา กลายเป็น macrophage** กิน oxidized LDL → **foam cell** → **fatty streak**
3. **smooth muscle cell ย้ายเข้ามา** สร้างคอลลาเจนเป็น **fibrous cap** ห่อ **necrotic lipid core** → established plaque
4. การอักเสบและ T cell ทำให้ cap **บางลง** → **vulnerable plaque** → แตก → ลิ่มเลือด → **ACS หรือ stroke**

> ทุกขั้นตอนเริ่มจาก **อนุภาคที่มี apoB** เข้าไปในผนังหลอดเลือด — นี่คือเหตุผลที่ **LDL-C เป็นเป้าหลักของการรักษา** และ "ยิ่งต่ำยิ่งดี"
""",
    ["Exogenous: ลำไส้ → chylomicron (apoB-48) → LPL → remnant → ตับ (apoE)",
     "Endogenous: ตับ → VLDL (apoB-100) → IDL → LDL → LDL receptor",
     "apoC-II กระตุ้น LPL · apoE ให้ตับเก็บ remnant · apoB-100 จับ LDL receptor",
     "PCSK9 พา LDL receptor ไปทำลาย — ยับยั้ง PCSK9 แล้ว LDL ลด",
     "Plaque: LDL เข้า intima → oxidized → macrophage → foam cell → fatty streak → fibrous cap"],
    [
    mcq("END-DLP-MCQ-01",
        "Which apolipoprotein is required to activate lipoprotein lipase and allow hydrolysis of triglyceride in chylomicrons and VLDL?",
        ["ApoA-I", "ApoB-48", "ApoB-100", "ApoC-II", "ApoE"],
        3,
        """**ApoC-II เป็นตัวกระตุ้น (cofactor) ของ lipoprotein lipase**

ถ้าขาด apoC-II หรือขาด LPL เอง → ย่อย TG ใน chylomicron ไม่ได้ → **TG สูงมาก (มักเกิน 1,000 mg/dL)**
= **familial chylomicronemia syndrome** ซึ่งมาด้วย **ตับอ่อนอักเสบ · eruptive xanthoma · lipemia retinalis**

**หน้าที่ของ apo อื่น**

| Apo | หน้าที่ |
|---|---|
| **A-I** | โครงสร้าง HDL · กระตุ้น LCAT |
| **B-48** | โครงสร้าง chylomicron |
| **B-100** | จับ LDL receptor |
| **E** | ให้ตับจับ remnant — ความผิดปกติของ apoE (E2/E2) ทำให้เกิด **dysbetalipoproteinemia** |""",
        "ApoC-II กระตุ้น LPL — ขาดแล้ว chylomicron ค้าง TG สูงมาก",
        "Apolipoproteins",
        [SLIDE + " — Exogenous and endogenous biosynthetic lipid pathways", "Harrison's 21e — Disorders of lipoprotein metabolism"], DLP),
    mcq("END-DLP-MCQ-02",
        "Statins lower plasma LDL-C mainly by which mechanism?",
        ["Blocking intestinal cholesterol absorption via NPC1L1",
         "Inhibiting HMG-CoA reductase, lowering hepatocyte cholesterol and up-regulating LDL receptors",
         "Activating PPAR-α to increase lipoprotein lipase activity",
         "Binding bile acids in the intestine",
         "Inhibiting PCSK9 binding to the LDL receptor"],
        1,
        """**Statin ยับยั้ง HMG-CoA reductase** (เอนไซม์กำหนดอัตราการสร้างคอเลสเตอรอล) → **คอเลสเตอรอลในเซลล์ตับลด**
→ กระตุ้น **SREBP-2** → **สร้าง LDL receptor มากขึ้น** → **ดึง LDL ออกจากเลือด** ← นี่คือกลไกหลักที่ทำให้ LDL ในเลือดลด

**ยาอื่นในตัวเลือก**

| ตัวเลือก | ยา |
|---|---|
| ยับยั้ง NPC1L1 | **ezetimibe** |
| กระตุ้น PPAR-α | **fibrate** |
| จับกรดน้ำดี | **bile acid sequestrant** (cholestyramine) |
| ยับยั้ง PCSK9 | **evolocumab · alirocumab · inclisiran** |

**ข้อสังเกต** — statin ได้ผลน้อยใน **homozygous FH ที่ไม่มี LDL receptor ทำงานเลย** เพราะกลไกหลักของ statin ต้องอาศัย receptor""",
        "Statin → คอเลสเตอรอลในตับลด → LDL receptor เพิ่ม → LDL ในเลือดลด",
        "Mechanism of statins",
        [SLIDE + " — Exogenous and endogenous biosynthetic lipid pathways", "Harrison's 21e — Disorders of lipoprotein metabolism"], DLP),
    ])

# ───────────────────────────── 11 ─────────────────────────────
sec("endo-ms-11", "สาเหตุของ dyslipidemia — primary (FH) และ secondary",
    "หา secondary cause ก่อนเสมอ · LDL ≥190 ให้นึกถึง familial hypercholesterolemia", 12,
"""สไลด์แบ่งสาเหตุเป็นสองกลุ่ม
- **Primary dyslipidemia** — เกิดจาก **ความผิดปกติทางพันธุกรรม** ของเมตาบอลิซึมไขมัน
- **Secondary dyslipidemia** — เกิดจากโรคอื่นหรือยา

### Secondary causes — ต้องหาก่อนเริ่มยาลดไขมันทุกครั้ง

| ผลที่เกิด | สาเหตุ |
|---|---|
| **LDL สูง** | **hypothyroidism** · **nephrotic syndrome** · **cholestasis** (primary biliary cholangitis) · anorexia nervosa · ตั้งครรภ์ · ยา: **thiazide · glucocorticoid · cyclosporine · progestin · anabolic steroid** |
| **TG สูง** | **โรคอ้วน · T2D ที่คุมไม่ได้** · **สุรา** · CKD · ตั้งครรภ์ · ยา: **estrogen ชนิดกิน · glucocorticoid · β-blocker · thiazide · retinoid · protease inhibitor · atypical antipsychotic · tamoxifen** |
| **HDL ต่ำ** | โรคอ้วน · T2D · สูบบุหรี่ · ไม่ออกกำลังกาย · anabolic steroid |

**แล็บคัดกรอง secondary cause ขั้นต่ำ** — **TSH · FPG/HbA1c · creatinine · UA (โปรตีน) · liver function (ALP, bilirubin)**
โดยเฉพาะ **TSH** — hypothyroidism ทำให้ LDL สูง (LDL receptor ลด) **และเพิ่มความเสี่ยงกล้ามเนื้ออักเสบจาก statin** จึงต้องรักษาไทรอยด์ก่อน

### Primary dyslipidemia ที่ต้องรู้

| โรค | ความผิดปกติ | ลักษณะเด่น |
|---|---|---|
| **Familial hypercholesterolemia (FH)** | **LDLR** (พบมากสุด) · APOB · PCSK9 gain-of-function · autosomal dominant | **LDL สูงมาก** · **tendon xanthoma** (เอ็นร้อยหวาย ข้อนิ้ว) · **corneal arcus ก่อนอายุ 45** · หลอดเลือดหัวใจตีบก่อนวัย |
| **Familial combined hyperlipidemia** | polygenic · พบบ่อยที่สุด | LDL และ/หรือ TG สูง **รูปแบบเปลี่ยนไปมา** ในคนเดียวกันและในครอบครัว · apoB สูง |
| **Familial dysbetalipoproteinemia (type III)** | **apoE2/E2** + ปัจจัยที่สอง | **TC และ TG สูงพอ ๆ กัน** · **palmar (striata) xanthoma** · tuberoeruptive xanthoma |
| **Familial chylomicronemia syndrome** | **LPL หรือ apoC-II** ขาด · autosomal recessive | **TG >1,000** ตั้งแต่เด็ก · **ตับอ่อนอักเสบซ้ำ** · eruptive xanthoma · lipemia retinalis |

**Heterozygous vs homozygous FH**
- **Heterozygous** (~1 ใน 250) — LDL ~190–400 mg/dL · CAD ในชายอายุ 40–50 ปี
- **Homozygous** (~1 ใน 300,000) — LDL **>500 mg/dL** · xanthoma ตั้งแต่เด็ก · MI ได้ตั้งแต่วัยรุ่น

### Dutch Lipid Clinic Network (DLCN) criteria สำหรับ FH

สไลด์ปิดส่วนสาเหตุด้วยเกณฑ์นี้ (รายละเอียดตัวเลขอิงตามเกณฑ์ต้นฉบับ)

| หมวด | เกณฑ์ | คะแนน |
|---|---|---|
| **ประวัติครอบครัว** | ญาติสายตรงเป็น **CAD ก่อนวัย** หรือ LDL > percentile 95 | 1 |
| | ญาติสายตรงมี **tendon xanthoma/arcus** หรือเด็กในครอบครัว LDL > percentile 95 | 2 |
| **ประวัติตนเอง** | **CAD ก่อนวัย** | 2 |
| | **หลอดเลือดสมองหรือหลอดเลือดส่วนปลายตีบก่อนวัย** | 1 |
| **ตรวจร่างกาย** | **Tendon xanthoma** | **6** |
| | **Corneal arcus ก่อนอายุ 45** | 4 |
| **LDL-C (mg/dL)** | **≥330** | **8** |
| | 250–329 | 5 |
| | 190–249 | 3 |
| | 155–189 | 1 |
| **DNA** | พบ mutation ที่ทำให้เกิดโรค (LDLR, APOB, PCSK9) | **8** |

**"ก่อนวัย"** = **ชาย <55 ปี · หญิง <60 ปี** · ใช้ค่าสูงสุดของแต่ละหมวดเพียงข้อเดียว

| คะแนนรวม | การวินิจฉัย |
|---|---|
| **>8** | **Definite FH** |
| **6–8** | **Probable FH** |
| 3–5 | Possible FH |
| <3 | Unlikely |

**เมื่อวินิจฉัย FH** — ผู้ป่วยจัดเป็น **ความเสี่ยงสูงทันที** ไม่ต้องใช้ risk score · เริ่ม **high-intensity statin** · และ **คัดกรองญาติสายตรงทุกคน (cascade screening)**
""",
    ["หา secondary cause ก่อนเริ่มยาเสมอ — TSH, glucose, creatinine, UA, LFT",
     "LDL สูงจาก hypothyroid · nephrotic · cholestasis · thiazide · steroid",
     "TG สูงจากอ้วน · T2D คุมไม่ได้ · สุรา · estrogen กิน · retinoid · β-blocker",
     "FH: LDLR มากสุด · tendon xanthoma · arcus <45 · CAD ก่อนวัย",
     "DLCN: tendon xanthoma 6 · LDL ≥330 = 8 · >8 definite · 6–8 probable",
     "Palmar xanthoma = dysbetalipoproteinemia (apoE2/E2) · eruptive xanthoma = TG สูงมาก",
     "วินิจฉัย FH แล้วต้องคัดกรองญาติสายตรง"],
    [
    mcq("END-DLP-MCQ-03",
        "A 38-year-old man has LDL-C 280 mg/dL, thickened Achilles tendons with nodules, and his father had a myocardial infarction at age 46. TSH, glucose, creatinine and liver tests are normal. Using the Dutch Lipid Clinic Network criteria, what is his score category?",
        ["Unlikely FH", "Possible FH", "Probable FH", "Definite FH", "Cannot be scored without genetic testing"],
        3,
        """**คำนวณ DLCN**

| หมวด | ข้อมูล | คะแนน |
|---|---|---|
| ครอบครัว | พ่อ MI อายุ 46 (ชาย <55 = ก่อนวัย) | **1** |
| ตรวจร่างกาย | **tendon xanthoma ที่เอ็นร้อยหวาย** | **6** |
| LDL | 280 (250–329) | **5** |
| **รวม** | | **12** |

**>8 = Definite FH** — ไม่จำเป็นต้องตรวจยีนเพื่อวินิจฉัย (ตรวจได้ถ้าต้องการยืนยันและใช้คัดกรองญาติ)

**การดูแลต่อ** — เป็นกลุ่ม **ความเสี่ยงสูง** ทันที → **high-intensity statin** เป้า LDL **<70 mg/dL และลดลง ≥50%**
ถ้ายังไม่ถึงเป้าเติม **ezetimibe** แล้วจึง **PCSK9 inhibitor** · และ **คัดกรองลูกและพี่น้องทุกคน**""",
        "Tendon xanthoma (6) + LDL 250–329 (5) = definite FH ได้เลย",
        "DLCN criteria for FH",
        [SLIDE + " — Dutch Lipid Clinic Network diagnostic criteria for FH", "Nordestgaard BG et al. Eur Heart J 2013;34:3478-90"], DLP),
    mcq("END-DLP-MCQ-04",
        "A 55-year-old woman is found to have LDL-C 238 mg/dL on routine screening. Her previous LDL-C two years ago was 120 mg/dL. She reports fatigue, weight gain, constipation and cold intolerance. What is the most appropriate next step?",
        ["Start high-intensity statin immediately",
         "Measure TSH",
         "Start ezetimibe",
         "Genetic testing for familial hypercholesterolaemia",
         "Repeat lipid profile in 1 year"],
        1,
        """**LDL ที่สูงขึ้นมากในเวลาสั้น ในคนที่เคยปกติ + อาการ hypothyroidism** → ต้อง **ตรวจ TSH** ก่อน

**ทำไม hypothyroid ทำให้ LDL สูง** — thyroid hormone กระตุ้นการสร้าง **LDL receptor** ที่ตับ เมื่อขาด → receptor ลด → LDL ค้างในเลือด

**ทำไมต้องรักษาไทรอยด์ก่อนเริ่ม statin**
- LDL มักลดลงเองมากเมื่อให้ **levothyroxine** จนไทรอยด์ปกติ
- **Hypothyroid เพิ่มความเสี่ยงกล้ามเนื้ออักเสบจาก statin** (myopathy)

**ทำไมข้ออื่นผิด**
- **เริ่ม statin/ezetimibe ทันที** — ข้ามการหา secondary cause
- **ตรวจยีน FH** — ประวัติ LDL เคยปกติเมื่อ 2 ปีก่อน **ไม่เข้ากับ FH** ซึ่ง LDL สูงมาตั้งแต่เกิด""",
        "LDL สูงขึ้นใหม่ + อาการ hypothyroid → ตรวจ TSH ก่อนเริ่ม statin",
        "Secondary dyslipidemia",
        [SLIDE + " — Etiology: primary vs secondary", "Harrison's 21e — Secondary disorders of lipoprotein metabolism"], DLP + ["B11.3(3)"]),
    mcq("END-DLP-MCQ-05",
        "A 45-year-old man has total cholesterol 390 mg/dL and triglyceride 420 mg/dL of roughly equal magnitude, with yellow-orange deposits in the palmar creases. Which genotype is most likely?",
        ["LDL receptor mutation", "ApoE2/E2 homozygosity", "Lipoprotein lipase deficiency", "PCSK9 loss-of-function", "ApoA-I deficiency"],
        1,
        """**Palmar (striata) xanthoma** — ไขมันสีเหลืองส้มตามรอยพับฝ่ามือ — เป็นลักษณะ **pathognomonic** ของ **familial dysbetalipoproteinemia (type III)**
ร่วมกับ **TC และ TG สูงพอ ๆ กัน** (มัก 300–500 mg/dL ทั้งคู่)

**กลไก** — **apoE2** จับกับ receptor ที่ตับได้ไม่ดี → **chylomicron remnant และ IDL ค้าง** ในเลือด
ต้องมี **apoE2/E2** ร่วมกับปัจจัยที่สอง (อ้วน เบาหวาน hypothyroid) จึงแสดงอาการ

**ทำไมข้ออื่นผิด**
- **LDLR mutation (FH)** — LDL สูงเด่น TG ปกติ · **tendon** xanthoma
- **LPL deficiency** — TG >1,000 เด่นกว่ามาก · **eruptive** xanthoma
- **PCSK9 loss-of-function** — LDL **ต่ำ** และป้องกันโรคหัวใจ (ที่มาของยา PCSK9 inhibitor)
- **ApoA-I deficiency** — HDL ต่ำมาก""",
        "Palmar xanthoma + TC ≈ TG = dysbetalipoproteinemia (apoE2/E2)",
        "Primary dyslipidemias",
        [SLIDE + " — Primary dyslipidemia", "Harrison's 21e — Disorders of lipoprotein metabolism"], DLP),
    ])

# ───────────────────────────── 12 ─────────────────────────────
sec("endo-ms-12", "รักษา LDL สูง — ประเมินความเสี่ยง เป้า LDL และยา",
    "เป้า LDL ขึ้นกับระดับความเสี่ยง · statin เป็นยาหลัก · เติม ezetimibe แล้ว PCSK9 inhibitor", 13,
"""> ข้อความในสไลด์ส่วนการรักษา dyslipidemia ดึงออกมาไม่ได้ หัวข้อนี้จึงเรียบเรียงจาก **ESC/EAS 2019** (และ focused update 2025)
> กับ **แนวทางเวชปฏิบัติการใช้ยารักษาภาวะไขมันผิดปกติ** ของไทยที่อิงหลักเดียวกัน — ดูรายการอ้างอิงท้ายคาบ

### 1. คำนวณ LDL
**Friedewald** — **LDL-C = TC − HDL-C − (TG / 5)** (หน่วย mg/dL)
**ใช้ไม่ได้เมื่อ TG >400 mg/dL** → ต้องวัด LDL โดยตรง หรือใช้ **non-HDL-C (= TC − HDL-C)** แทน

### 2. จัดระดับความเสี่ยงก่อน แล้วจึงตั้งเป้า (ESC/EAS 2019)

| ระดับความเสี่ยง | ตัวอย่าง | เป้า LDL-C |
|---|---|---|
| **สูงมาก** | **เป็นโรคหลอดเลือดแข็งแล้ว (ASCVD)** — ACS, stable CAD, stroke/TIA, PAD · เบาหวานที่มี target organ damage · CKD รุนแรง (eGFR <30) · FH + ASCVD | **<55 mg/dL** และ **ลดลง ≥50%** |
| **สูง** | **FH** · **LDL ≥190** · **เบาหวาน ≥10 ปี** ไม่มี target organ damage · CKD eGFR 30–59 · ความดัน ≥180/110 | **<70 mg/dL** และ **ลดลง ≥50%** |
| **ปานกลาง** | เบาหวานอายุน้อย (T1D <35 ปี, T2D <50 ปี) เป็นมา <10 ปี ไม่มีปัจจัยอื่น | **<100 mg/dL** |
| **ต่ำ** | คำนวณความเสี่ยงได้ต่ำ | **<116 mg/dL** |

เกิด **เหตุการณ์หลอดเลือดซ้ำภายใน 2 ปี** ทั้งที่ใช้ statin ขนาดสูงสุดแล้ว → พิจารณาเป้า **<40 mg/dL**
ผู้ที่ไม่มีโรคหลอดเลือด ใช้ **SCORE2 / SCORE2-OP** (หรือ Thai CV risk score) ประเมินความเสี่ยง 10 ปี

**หลัก "ยิ่งต่ำยิ่งดี"** — ทุก **1 mmol/L (~39 mg/dL) ของ LDL ที่ลดได้ ลดเหตุการณ์หลอดเลือดหลัก ~22%** (CTT meta-analysis)
โดยยังไม่พบระดับต่ำสุดที่ประโยชน์หยุดลง

### 3. Statin — ยาหลัก

| ความแรง | ขนาดยา | LDL ลดลง |
|---|---|---|
| **High-intensity** | **atorvastatin 40–80 mg · rosuvastatin 20–40 mg** | **≥50%** |
| **Moderate-intensity** | atorvastatin 10–20 · rosuvastatin 5–10 · simvastatin 20–40 · pravastatin 40–80 | 30–49% |

**ผลข้างเคียงและการติดตาม**
- **ปวดกล้ามเนื้อ (SAMS)** — พบบ่อยที่สุด ส่วนใหญ่ **CK ปกติ** · วัด CK เมื่อมีอาการ ·
  **CK >10 เท่าของค่าปกติ → หยุดยา** (ระวัง rhabdomyolysis) · ส่วนใหญ่กลับมาใช้ statin ตัวอื่นหรือขนาดต่ำกว่าได้
- **ALT** — วัดก่อนเริ่มยา · **ALT >3 เท่าต่อเนื่อง → หยุดหรือลดยา**
- **เบาหวานใหม่เพิ่มขึ้นเล็กน้อย** — ประโยชน์ด้านหัวใจมากกว่าชัดเจน **ไม่ใช่เหตุผลให้หยุดยา**
- **ปัจจัยเสี่ยง myopathy** — อายุมาก · hypothyroid · CKD · **ยาที่ยับยั้ง CYP3A4** (clarithromycin, azole, protease inhibitor, **gemfibrozil**)
- **ข้อห้าม** — **ตั้งครรภ์และให้นมบุตร** · โรคตับที่กำลังดำเนินอยู่

### 4. ไม่ถึงเป้า → ไล่ขั้น

| ขั้น | ยา | LDL ลดเพิ่ม |
|---|---|---|
| 1 | **statin ขนาดสูงสุดที่ทนได้** | 30–50% |
| 2 | **+ ezetimibe** (ยับยั้ง NPC1L1 ที่ลำไส้) | ~20–25% |
| 3 | **+ PCSK9 inhibitor** (evolocumab, alirocumab · inclisiran เป็น siRNA ฉีดปีละ 2 ครั้ง) | ~50–60% |
| ทางเลือก | **bempedoic acid** (ยับยั้ง ACL เหนือ HMG-CoA reductase — ไม่ทำงานในกล้ามเนื้อ จึงเหมาะกับผู้ที่ทน statin ไม่ได้) | ~20% |

ติดตาม lipid profile **4–12 สัปดาห์หลังเริ่มหรือปรับยา** แล้วทุก 6–12 เดือน

### 5. การปรับพฤติกรรมที่ช่วยลด LDL
ลด **ไขมันอิ่มตัว (<10% ของพลังงาน) และไขมันทรานส์** · เพิ่ม **ใยอาหารชนิดละลายน้ำ** · ลดน้ำหนัก · ออกกำลังกาย · เลิกบุหรี่
""",
    ["Friedewald: LDL = TC − HDL − TG/5 · ใช้ไม่ได้เมื่อ TG >400",
     "ASCVD = ความเสี่ยงสูงมาก → LDL <55 และลด ≥50%",
     "FH, LDL ≥190, DM ≥10 ปี = ความเสี่ยงสูง → LDL <70 และลด ≥50%",
     "High-intensity: atorvastatin 40–80 · rosuvastatin 20–40 → LDL ลด ≥50%",
     "ไม่ถึงเป้า: statin สูงสุด → + ezetimibe → + PCSK9 inhibitor",
     "CK >10 เท่า → หยุด statin · statin ห้ามในการตั้งครรภ์",
     "LDL ลดทุก 1 mmol/L → เหตุการณ์หลอดเลือดลด ~22%"],
    [
    mcq("END-DLP-MCQ-06",
        "A 58-year-old man is discharged after an NSTEMI. His LDL-C is 142 mg/dL and he has never taken lipid-lowering therapy. According to ESC/EAS guidance, what is the most appropriate lipid-lowering plan?",
        ["Simvastatin 10 mg with a target LDL-C below 130 mg/dL",
         "Diet alone for 3 months, then reassess",
         "High-intensity statin (e.g. atorvastatin 80 mg) aiming for LDL-C below 55 mg/dL and at least 50% reduction",
         "Fenofibrate 160 mg daily",
         "Ezetimibe monotherapy"],
        2,
        """ผู้ป่วยหลัง ACS = **ASCVD = ความเสี่ยงสูงมาก**
→ เป้า **LDL-C <55 mg/dL และลดลง ≥50% จากค่าตั้งต้น** — เริ่ม **high-intensity statin ทันทีขณะอยู่โรงพยาบาล**

**ตัวเลขของผู้ป่วยรายนี้** — ลด 50% จาก 142 = 71 · เป้าสัมบูรณ์ <55 → ต้องใช้ **ค่าที่ต่ำกว่า คือ <55**
atorvastatin 80 mg ลดได้ ~50% (เหลือ ~71) **จึงมีโอกาสสูงที่ต้องเติม ezetimibe** — ตรวจซ้ำใน 4–6 สัปดาห์

**ทำไมข้ออื่นผิด**
- **Simvastatin 10 mg** — ความแรงต่ำ เป้า 130 ล้าสมัย
- **คุมอาหารอย่างเดียว** — ผิดใน ASCVD ต้องเริ่มยาทันที
- **Fenofibrate** — ลด TG ไม่ได้ลด LDL มาก และไม่ลดเหตุการณ์หัวใจเมื่อใช้แทน statin
- **Ezetimibe เดี่ยว** — ใช้เมื่อทน statin ไม่ได้เท่านั้น""",
        "หลัง ACS → high-intensity statin ทันที เป้า LDL <55 และลด ≥50%",
        "Lipid targets in ASCVD",
        ["Mach F et al. 2019 ESC/EAS Guidelines for dyslipidaemias. Eur Heart J 2020;41:111-88"], DLP),
    mcq("END-DLP-MCQ-07",
        "Lipid profile: total cholesterol 240 mg/dL, HDL-C 40 mg/dL, triglyceride 250 mg/dL. What is the calculated LDL-C using the Friedewald equation?",
        ["150 mg/dL", "160 mg/dL", "175 mg/dL", "190 mg/dL", "Cannot be calculated because TG is above 200 mg/dL"],
        0,
        """**Friedewald: LDL-C = TC − HDL-C − (TG / 5)**
= 240 − 40 − (250 / 5)
= 240 − 40 − 50
= **150 mg/dL**

**TG / 5** คือการประมาณ **VLDL-cholesterol** เพราะใน VLDL สัดส่วน TG ต่อคอเลสเตอรอลประมาณ 5 ต่อ 1

**ข้อจำกัด** — ใช้ **ไม่ได้เมื่อ TG >400 mg/dL** (ไม่ใช่ 200) เพราะอนุภาคที่อุดม TG (chylomicron, remnant) ทำให้สัดส่วน 5:1 ไม่จริง
ในกรณีนั้นให้วัด LDL โดยตรงหรือใช้ **non-HDL-C** (ในโจทย์นี้ = 200 mg/dL)""",
        "LDL = TC − HDL − TG/5 · ใช้ไม่ได้ถ้า TG >400",
        "Friedewald equation",
        ["Friedewald WT et al. Clin Chem 1972;18:499-502"], DLP),
    mcq("END-DLP-MCQ-08",
        "A 64-year-old woman on atorvastatin 40 mg develops diffuse muscle pain and dark urine one week after starting clarithromycin. CK is 18 times the upper limit of normal. What is the most appropriate management?",
        ["Continue atorvastatin and add coenzyme Q10",
         "Reduce atorvastatin to 20 mg and continue clarithromycin",
         "Stop atorvastatin (and clarithromycin), give IV fluids and monitor renal function",
         "Switch to simvastatin 40 mg",
         "Add gemfibrozil"],
        2,
        """**CK >10 เท่าของค่าปกติ + ปัสสาวะสีเข้ม** = สงสัย **rhabdomyolysis** → **หยุด statin ทันที** · ให้สารน้ำทางหลอดเลือด · ติดตามไตและโพแทสเซียม

**สาเหตุ** — **clarithromycin ยับยั้ง CYP3A4** → ระดับ atorvastatin ในเลือดสูงขึ้นมาก
(simvastatin, lovastatin, atorvastatin ใช้ CYP3A4 · **rosuvastatin และ pravastatin ไม่ใช้** จึงมีปฏิกิริยาน้อยกว่า)

**ทำไมข้ออื่นผิด**
- **ใช้ต่อ + CoQ10** หรือ **ลดขนาด** — ไม่ปลอดภัยเมื่อ CK >10 เท่าและมีปัสสาวะสีเข้ม
- **เปลี่ยนเป็น simvastatin** — ใช้ CYP3A4 เหมือนกันและเสี่ยง myopathy มากกว่า
- **Gemfibrozil** — **ยับยั้ง glucuronidation ของ statin** เพิ่มความเสี่ยง myopathy มาก — ถ้าต้องใช้ fibrate คู่กับ statin ให้ใช้ **fenofibrate**

**ภายหลัง** เมื่อหายดีแล้ว ส่วนใหญ่กลับมาใช้ statin ขนาดต่ำหรือตัวที่ไม่ผ่าน CYP3A4 ได้ โดยเลี่ยงยาที่มีปฏิกิริยา""",
        "CK >10× + ปัสสาวะเข้ม → หยุด statin · CYP3A4 inhibitor และ gemfibrozil เพิ่มความเสี่ยง",
        "Statin-associated muscle symptoms",
        ["Mach F et al. 2019 ESC/EAS Guidelines for dyslipidaemias", "Harrison's 21e — Lipid-lowering drugs"], DLP),
    mcq("END-DLP-MCQ-09",
        "A 60-year-old man with prior ischaemic stroke has LDL-C 84 mg/dL despite 3 months of rosuvastatin 40 mg with good adherence. What is the next step?",
        ["Increase rosuvastatin to 80 mg", "Add ezetimibe 10 mg", "Add fenofibrate", "Switch to pravastatin", "No change — LDL-C below 100 is adequate"],
        1,
        """ผู้ป่วยมี **ischemic stroke = ASCVD = ความเสี่ยงสูงมาก** → เป้า **LDL <55**
LDL 84 **ยังไม่ถึงเป้า** ทั้งที่ใช้ **statin ขนาดสูงสุดแล้ว** (rosuvastatin 40 mg) → ขั้นต่อไปคือ **เติม ezetimibe**

ezetimibe ยับยั้ง **NPC1L1** ที่ลำไส้ → ลด LDL เพิ่มอีก **~20–25%** → คาดว่าเหลือ ~63–67
ถ้ายังไม่ถึงเป้าอีก จึงเติม **PCSK9 inhibitor**

**ทำไมข้ออื่นผิด**
- **Rosuvastatin 80 mg** — เกินขนาดสูงสุด
- **Fenofibrate** — ไม่ได้ลด LDL เป็นหลัก
- **Pravastatin** — ความแรงต่ำกว่า
- **LDL <100 พอแล้ว** — เป้าเก่า ไม่ใช่สำหรับความเสี่ยงสูงมาก""",
        "Statin ขนาดสูงสุดแล้วยังไม่ถึงเป้า → + ezetimibe → + PCSK9 inhibitor",
        "Stepwise LDL lowering",
        ["Mach F et al. 2019 ESC/EAS Guidelines for dyslipidaemias"], DLP),
    ])

# ───────────────────────────── 13 ─────────────────────────────
sec("endo-ms-13", "ไตรกลีเซอไรด์สูง",
    "TG สูงมากเสี่ยงตับอ่อนอักเสบ · หา secondary cause และแก้ก่อน · ≥500 ใช้ fibrate", 8,
"""> เช่นเดียวกับหัวข้อ 12 — เรียบเรียงจาก ESC/EAS 2019 และตำราหลัก เพราะดึงข้อความส่วนนี้จากสไลด์ไม่ได้

### ระดับ TG และความหมาย

| TG (mg/dL) | ความหมาย |
|---|---|
| **<150** | ปกติ |
| **150–499** | สูงปานกลาง — **ความเสี่ยงหลอดเลือด** (remnant ที่มี apoB) |
| **≥500** | สูงมาก — **เริ่มเสี่ยงตับอ่อนอักเสบ** |
| **>1,000** | **เสี่ยงตับอ่อนอักเสบสูง** · มัก chylomicronemia |

### ขั้นตอนดูแล
1. **หาและแก้ secondary cause ก่อนเสมอ** — **เบาหวานที่คุมไม่ได้ · สุรา · โรคอ้วน** · hypothyroid · CKD ·
   ยา (**estrogen ชนิดกิน · retinoid · steroid · thiazide · β-blocker · protease inhibitor · atypical antipsychotic**)
2. **ปรับพฤติกรรม** — **งดสุรา** · ลดน้ำตาลและคาร์โบไฮเดรตขัดสี · ลดน้ำหนัก · ออกกำลังกาย
3. **ยาตามระดับ TG**

| สถานการณ์ | ยา |
|---|---|
| **TG ≥500 (โดยเฉพาะ >880–1,000)** | **Fibrate** (fenofibrate) เพื่อ **ป้องกันตับอ่อนอักเสบ** · ± omega-3 ขนาดสูง · ไขมันในอาหาร <10–15% |
| **TG 150–499 และมีความเสี่ยงสูง** | **statin ก่อน** (ลดทั้ง LDL และ TG) · ถ้ายังสูงแม้ LDL ถึงเป้า พิจารณา **icosapent ethyl 2 g วันละ 2 ครั้ง** (REDUCE-IT) |
| **ใช้ fibrate ร่วมกับ statin** | ใช้ **fenofibrate** · **ห้ามใช้ gemfibrozil** (myopathy) |

**Fibrate** — กระตุ้น **PPAR-α** → เพิ่มการสร้าง **LPL** และการเผาผลาญกรดไขมัน · ลด TG 30–50%
ผลข้างเคียง: **นิ่วในถุงน้ำดี** · creatinine สูงขึ้น (ไม่ใช่ไตเสียจริง) · myopathy เมื่อใช้คู่ statin

### TG สูงมากจนเกิดตับอ่อนอักเสบ
- งดอาหารทางปาก · สารน้ำ · ควบคุมปวด
- **Insulin infusion** (± glucose) — กระตุ้น LPL ลด TG ได้เร็ว โดยเฉพาะในผู้ป่วยเบาหวาน
- **Plasmapheresis** ในรายรุนแรงบางราย
- หลังพ้นระยะเฉียบพลัน → fibrate + งดสุรา + คุมเบาหวาน + ไขมันในอาหารต่ำมาก

### อาการแสดงของ TG สูงมาก
**Eruptive xanthoma** (ตุ่มเหลืองฐานแดงที่ก้นและแขนด้านนอก) · **lipemia retinalis** (หลอดเลือดจอตาสีขาวครีม) ·
**เลือดขุ่นเหมือนนม** · **hepatosplenomegaly** · ปวดท้องซ้ำ ๆ
""",
    ["TG ≥500 เริ่มเสี่ยงตับอ่อนอักเสบ · >1,000 เสี่ยงสูง",
     "แก้ secondary cause ก่อน — เบาหวาน สุรา อ้วน ยา",
     "TG ≥500 → fenofibrate ป้องกันตับอ่อนอักเสบ",
     "Statin + fibrate → ใช้ fenofibrate ห้าม gemfibrozil",
     "TG pancreatitis → insulin infusion กระตุ้น LPL ลด TG เร็ว",
     "Eruptive xanthoma + lipemia retinalis = TG สูงมาก"],
    [
    mcq("END-DLP-MCQ-10",
        "A 42-year-old man with poorly controlled type 2 diabetes (HbA1c 11%) who drinks heavily presents with epigastric pain radiating to the back. Serum lipase is 5 times normal and the serum is milky; triglyceride is 2,400 mg/dL. Besides supportive care, which therapy lowers triglyceride most rapidly in this setting?",
        ["Oral atorvastatin 80 mg", "Intravenous insulin infusion", "Oral ezetimibe", "Oral niacin", "Bile acid sequestrant"],
        1,
        """**Insulin infusion ทางหลอดเลือดดำ** — อินซูลินเป็น **ตัวกระตุ้น lipoprotein lipase** → ย่อย TG ใน chylomicron และ VLDL ได้เร็ว
และแก้น้ำตาลสูงที่เป็นสาเหตุในผู้ป่วยรายนี้ไปพร้อมกัน (ให้ glucose ร่วมถ้าน้ำตาลไม่สูงมาก) · รายรุนแรงบางรายใช้ **plasmapheresis**

**ต้นเหตุในผู้ป่วยรายนี้** — **เบาหวานที่คุมไม่ได้ + สุรา** = secondary causes ที่พบบ่อยที่สุดของ TG สูงมาก

**ทำไมข้ออื่นผิด**
- **Statin · ezetimibe** — ลด LDL เป็นหลัก ลด TG ได้น้อยและช้า
- **Niacin** — ลด TG ได้แต่ช้า และทำให้น้ำตาลแย่ลง
- **Bile acid sequestrant** — **ทำให้ TG สูงขึ้น** ห้ามใช้เมื่อ TG สูง

**หลังพ้นระยะเฉียบพลัน** — **fenofibrate** · **งดสุราเด็ดขาด** · คุมเบาหวาน · อาหารไขมันต่ำ""",
        "TG-induced pancreatitis → insulin infusion กระตุ้น LPL · bile acid sequestrant ทำให้ TG สูงขึ้น",
        "Hypertriglyceridemia-induced pancreatitis",
        ["Harrison's 21e — Disorders of lipoprotein metabolism", "Mach F et al. 2019 ESC/EAS Guidelines for dyslipidaemias"], DLP + ["2.3.11(1)"]),
    mcq("END-DLP-MCQ-11",
        "A patient on rosuvastatin 20 mg has persistent triglyceride of 620 mg/dL despite diet, alcohol abstinence and good glycaemic control. A fibrate is to be added. Which choice is most appropriate?",
        ["Gemfibrozil, because it lowers triglyceride the most", "Fenofibrate", "Stop rosuvastatin and use gemfibrozil alone", "Cholestyramine", "No treatment is needed below 1,000 mg/dL"],
        1,
        """**TG ≥500 ทั้งที่แก้ secondary cause แล้ว** → เติม fibrate เพื่อ **ป้องกันตับอ่อนอักเสบ**
และเมื่อใช้ร่วมกับ statin ต้องเลือก **fenofibrate**

**ทำไมห้าม gemfibrozil คู่กับ statin** — gemfibrozil **ยับยั้ง glucuronidation (OATP1B1/UGT) ของ statin** → ระดับ statin สูงมาก → **myopathy และ rhabdomyolysis**
fenofibrate ไม่มีปฏิกิริยานี้ในระดับที่มีนัยสำคัญ

**ทำไมข้ออื่นผิด**
- **หยุด statin** — เสียประโยชน์ด้านหลอดเลือดโดยไม่จำเป็น
- **Cholestyramine** — **เพิ่ม TG**
- **รอจนถึง 1,000** — ความเสี่ยงตับอ่อนอักเสบเริ่มที่ ≥500""",
        "Statin + fibrate → fenofibrate เสมอ ไม่ใช้ gemfibrozil",
        "Fibrate choice with statin",
        ["Mach F et al. 2019 ESC/EAS Guidelines for dyslipidaemias"], DLP),
    ])

# ───────────────────────────── MEQ ─────────────────────────────
TITLE = "Metabolic Syndrome, Obesity และ Dyslipidemia"
MEQ = [{
 "id": "END-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": TITLE,
 "topic": "Obesity with metabolic syndrome — diagnosis, evaluation and stepwise management",
 "vignette": """ชายไทยอายุ 46 ปี อาชีพพนักงานบริษัท มาตรวจสุขภาพประจำปี

PI: น้ำหนักขึ้นประมาณ 15 kg ใน 5 ปีหลังเปลี่ยนงานมานั่งโต๊ะและทำงานเป็นกะ ดื่มชานมเย็นวันละ 2 แก้ว
เคยลองอดอาหารเย็นเองได้ 2 เดือน ลดได้ 3 kg แล้วกลับขึ้นมาเท่าเดิม
ภรรยาบอกว่านอนกรนเสียงดัง บางครั้งเหมือนหยุดหายใจ ตื่นมาไม่สดชื่น ง่วงระหว่างประชุม

U/D: ไม่เคยตรวจสุขภาพมาก่อน · ยาที่ใช้: ไม่มี · ไม่สูบบุหรี่ · ดื่มเบียร์สัปดาห์ละ 2–3 วัน
FH: บิดาเป็นเบาหวาน เสียชีวิตจากกล้ามเนื้อหัวใจตายเฉียบพลันเมื่ออายุ 62 ปี

PE: น้ำหนัก 94 kg · ส่วนสูง 170 cm · รอบเอว 104 cm · รอบคอ 43 cm
BP 146/94 mmHg (วัดซ้ำ 144/92) · PR 84/min
Skin: ผิวคล้ำหนาที่ด้านหลังคอและรักแร้ · ไม่มีท้องลายสีม่วง · ไม่มี xanthoma
Abdomen: ตับโตเล็กน้อย ขอบเรียบ ไม่กดเจ็บ

Lab (อดอาหาร 10 ชม.): FPG 118 mg/dL · HbA1c 6.1% · TC 236 · TG 280 · HDL-C 36 · ALT 68 U/L · AST 42 U/L
Creatinine 0.9 mg/dL · TSH ปกติ""",
 "questions": [
  {"q": "1.1 จงคำนวณ BMI และจัดระดับตามเกณฑ์คนเอเชีย พร้อมระบุว่าผู้ป่วยเข้าเกณฑ์ metabolic syndrome หรือไม่ ด้วยองค์ประกอบใดบ้าง (5 คะแนน)",
   "a": """**BMI = 94 / (1.70)² = 94 / 2.89 = 32.5 kg/m²**
→ เกณฑ์ **Asia-Pacific** = **Obese class II (≥30)** · ถ้าใช้ staging เอเชีย 27.5/32.5/37.5 = **stage 2** (1 คะแนน)

**Metabolic syndrome — เข้าเกณฑ์** มีครบ **5 ใน 5** (≥3 ข้อก็เข้าเกณฑ์แล้ว) (4 คะแนน — องค์ประกอบละ ~1)

| องค์ประกอบ | ผู้ป่วย | เกณฑ์ |
|---|---|---|
| รอบเอว | **104 cm** | ชายเอเชีย ≥90 ✅ (และเกินครึ่งหนึ่งของส่วนสูง 85 cm) |
| TG | **280** | ≥150 ✅ |
| HDL | **36** | ชาย <40 ✅ |
| BP | **146/94** | ≥130/85 ✅ |
| FPG | **118** | ≥100 ✅ |"""},
  {"q": "1.2 จงบอกภาวะแทรกซ้อนหรือโรคร่วมของโรคอ้วนที่พบหรือสงสัยในผู้ป่วยรายนี้ พร้อมหลักฐาน (อย่างน้อย 5 ข้อ) (5 คะแนน)",
   "a": """| ภาวะ | หลักฐาน |
|---|---|
| **Prediabetes** (IFG + HbA1c 5.7–6.4%) | FPG 118 · HbA1c 6.1% |
| **ความดันโลหิตสูง** | 146/94 และ 144/92 ซ้ำสองครั้ง |
| **Atherogenic dyslipidemia** | TG 280 · HDL 36 |
| **สงสัย OSA** | กรน · หยุดหายใจ · ง่วงกลางวัน · **STOP-BANG** = S T O P B(BMI 32.5 ไม่เกิน 35 ✗) A(46 ✗) N(43 ✅) G(ชาย ✅) = **6 คะแนน** |
| **สงสัย MASLD** | ตับโต · **ALT 68 > AST** · มี MetS |
| **Insulin resistance** | **acanthosis nigricans** ที่คอและรักแร้ |

ควรกล่าวด้วยว่าผู้ป่วยมี **ความเสี่ยงหัวใจและหลอดเลือดสูง** (MetS + บิดาเป็น MI — แม้อายุ 62 จะไม่เข้าเกณฑ์ "ก่อนวัย" ของชาย <55)"""},
  {"q": "1.3 จงบอกการตรวจเพิ่มเติมที่ควรส่ง พร้อมเหตุผล (4 คะแนน)",
   "a": """- **Polysomnography (sleep study)** — **STOP-BANG >4 → ส่งปรึกษาแพทย์โรคปอด** ตามสไลด์ · OSA ที่ไม่รักษาทำให้ความดันคุมยากและลดน้ำหนักยาก (1)
- **คำนวณ LDL-C** — Friedewald = 236 − 36 − 280/5 = **144 mg/dL** (TG <400 ใช้ได้) · และ **non-HDL-C = 200** (1)
- **ประเมิน MASLD** — **ultrasound ตับ** · **FIB-4** (อายุ × AST / (เกล็ดเลือด × √ALT)) เพื่อคัดกรองพังผืด · ตรวจ **HBsAg, anti-HCV** และประเมินปริมาณสุราเพื่อแยกสาเหตุอื่น (1)
- **ประเมินอวัยวะเป้าหมายของความดัน** — **UA (albuminuria/UACR) · ECG** · electrolytes (1)

**ไม่จำเป็นต้องส่ง** cortisol หรือ dexamethasone suppression test เพราะไม่มีลักษณะ Cushing (ไม่มีท้องลายสีม่วง ไม่มีกล้ามเนื้อลีบ) และ TSH ปกติแล้ว"""},
  {"q": "1.4 จงวางแผนการรักษาแบบเป็นขั้นตอน ครอบคลุมเป้าหมายน้ำหนัก การปรับพฤติกรรม และการใช้ยาสำหรับแต่ละปัญหา (6 คะแนน)",
   "a": """**1. เป้าหมายน้ำหนัก (1)** — ลด **5–10% ใน 6 เดือน** = ประมาณ **5–9 kg** (เหลือ 85–89 kg) แบบ **complication-centric**
และต่อไปตั้งเป้า **>10%** เพื่อให้ **MASLD และ OSA** ดีขึ้นชัดเจน

**2. ปรับพฤติกรรม (2)**
- อาหาร **พลังงานต่ำแบบสมดุล** (~1,200–1,500 kcal/วันสำหรับชาย) · **เลิกชานมหวาน** · ลดคาร์บขัดสีและอาหารแปรรูป
- **ลด/งดเบียร์** — ช่วยทั้ง TG ความดัน และตับ
- ออกกำลัง **ปานกลาง 150–300 นาที/สัปดาห์** + **ฝึกต้านแรง** 2 วัน/สัปดาห์
- **จัดการการนอน** และการทำงานเป็นกะ · ติดตามสม่ำเสมอ ตั้งเป้าที่วัดได้

**3. ความดัน (1)** — **ACEI หรือ ARB** (เป็นกลางทางเมตาบอลิก) เป้า **<130/80** · เลี่ยง β-blocker ชนิดไม่เลือกและ thiazide ขนาดสูง

**4. ไขมัน (1)** — ประเมินความเสี่ยงหัวใจด้วย risk score (ไม่มี ASCVD, ไม่ใช่เบาหวาน) → ความเสี่ยงมักอยู่ระดับ **ปานกลางถึงสูง**
→ เริ่ม **moderate-to-high-intensity statin** (เช่น atorvastatin 20–40 mg) ร่วมกับปรับพฤติกรรม · TG 280 ยังไม่ถึงเกณฑ์ใช้ fibrate (≥500)

**5. Prediabetes และน้ำหนัก (1)**
- ปรับพฤติกรรมเป็นหลัก **± metformin**
- ถ้าปรับพฤติกรรม **≥3 เดือน** แล้วลดได้ไม่ถึงเป้า → เข้าเกณฑ์ **ยาลดน้ำหนัก** (BMI ≥27 + โรคร่วม) — เลือก **GLP-1RA** (semaglutide 2.4 mg) ซึ่งช่วยทั้งน้ำหนักและน้ำตาล
  **หยุดยาถ้าใช้ 3–5 เดือนแล้วลด <5%**
- ถ้ายังไม่สำเร็จ — BMI 32.5 + โรคร่วมที่คุมไม่ได้ **เข้าเกณฑ์ผ่าตัดลดน้ำหนักของไทย** (≥32.5 + โรคร่วม)

**6. OSA** — ถ้ายืนยัน ให้ **CPAP** ร่วมด้วย"""},
 ],
 "ref": [SLIDE + " — MetS criteria / Obesity evaluation / AOMs / MBS",
         "Mach F et al. 2019 ESC/EAS Guidelines for dyslipidaemias"],
 "nl": MS + OB + DLP, "years": [], "_kind": "meq", "_set": "endo"}]

# ───────────────────────────── OSCE ─────────────────────────────
OSCE = [{
 "id": "END-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": TITLE,
 "topic": "OSCE – ให้คำปรึกษาเรื่องการลดน้ำหนักและการเริ่มยาลดน้ำหนัก",
 "station": "สถานีสื่อสารกับผู้ป่วยจำลอง 8 นาที",
 "instruction": """หญิงอายุ 36 ปี น้ำหนัก 84 kg ส่วนสูง 158 cm (BMI 33.6 kg/m²) รอบเอว 98 cm
เป็นความดันโลหิตสูงรักษาด้วย amlodipine · HbA1c 6.0% · มีบุตร 2 คน ใช้ยาฉีดคุมกำเนิด (DMPA) มา 3 ปี
พยายามลดน้ำหนักด้วยตนเองหลายครั้งแต่ไม่สำเร็จ มาขอ "ยาฉีดลดความอ้วนที่ดาราใช้"

คำสั่ง: จงให้คำปรึกษาผู้ป่วยเรื่องการลดน้ำหนักและการใช้ยาลดน้ำหนัก (ไม่ต้องตรวจร่างกาย)

หมายเหตุสำหรับผู้ป่วยจำลอง: รู้สึกอายและคิดว่าตัวเอง "ไม่มีวินัย" · อยากได้ยาเลยวันนี้ · ถ้าถูกถามจะบอกว่าอาจอยากมีลูกอีกคนในอีก 1–2 ปี""",
 "answer": """**เกณฑ์การให้คะแนน (เต็ม 20)**

**1. เปิดการสนทนาอย่างไม่ตัดสิน (3 คะแนน)**
- แนะนำตัว **ขออนุญาตพูดคุยเรื่องน้ำหนัก** ก่อน
- ใช้ภาษาที่ไม่ตีตรา เช่น "ผู้ที่มีภาวะโรคอ้วน" ไม่ใช่ "คนอ้วน"
- **แก้ความเชื่อ "ไม่มีวินัย"** — อธิบายว่าโรคอ้วนเป็น **โรคเรื้อรังที่เกิดจากหลายปัจจัย** ทั้งพันธุกรรม ฮอร์โมน ยา และสิ่งแวดล้อม **ไม่ใช่ความผิดของผู้ป่วย**

**2. ประเมินประวัติที่สำคัญ (4 คะแนน)**
- **ประวัติน้ำหนัก** — เริ่มขึ้นเมื่อไร สัมพันธ์กับการตั้งครรภ์หรือเริ่มยาหรือไม่ · วิธีที่เคยลอง
- **อาหาร การออกกำลังกาย การนอน** · คัดกรอง **ซึมเศร้าและการกินผิดปกติ**
- **ยา** — จับได้ว่า **DMPA ทำให้น้ำหนักขึ้น** (1 คะแนนเต็มสำหรับข้อนี้)
- **แผนการมีบุตร** ← สำคัญต่อการเลือกยา
- **แรงจูงใจและความพร้อมที่จะเปลี่ยน**

**3. อธิบายเป้าหมายที่สมจริง (3 คะแนน)**
- **ลด 5–10% ใน 6 เดือน** = ประมาณ **4–8 kg**
- อธิบายประโยชน์ที่จับต้องได้ — ความดันดีขึ้น **ลดโอกาสเป็นเบาหวาน** (HbA1c 6.0% = prediabetes) · การตั้งครรภ์ครั้งหน้าปลอดภัยขึ้น

**4. แผนปรับพฤติกรรมที่เป็นรูปธรรม (3 คะแนน)**
- อาหารพลังงานต่ำแบบสมดุล 1,000–1,200 kcal/วัน · ลดเครื่องดื่มหวาน
- ออกกำลังปานกลาง 150 นาที/สัปดาห์ + ฝึกต้านแรง
- เสนอส่งพบ **นักกำหนดอาหาร**

**5. ให้ข้อมูลเรื่องยาอย่างถูกต้อง (5 คะแนน)**
- **เข้าเกณฑ์ใช้ยา** (BMI ≥30 และมีโรคร่วม) แต่ยาเป็น **ตัวเสริม** การปรับพฤติกรรม ไม่ใช่ตัวแทน (1)
- ยาฉีดที่ผู้ป่วยถามถึงคือ **GLP-1RA** เช่น **semaglutide** — อธิบายกลไก (อิ่มเร็ว อิ่มนาน) · ฉีดสัปดาห์ละครั้ง · **เพิ่มขนาดทีละขั้นทุก 4 สัปดาห์** (1)
- ผลข้างเคียง — **คลื่นไส้ อาเจียน ท้องผูก** มักดีขึ้นเมื่อใช้ไปสักระยะ · ถามประวัติ **มะเร็งไทรอยด์ชนิด medullary หรือ MEN2 ในครอบครัว** (1)
- **ห้ามใช้ขณะตั้งครรภ์** → ต้อง **คุมกำเนิดที่ได้ผล** ระหว่างใช้ยา และ **หยุด semaglutide อย่างน้อย 2 เดือนก่อนตั้งครรภ์** · เสนอเปลี่ยน DMPA เป็นวิธีคุมกำเนิดที่ไม่ทำให้น้ำหนักขึ้น เช่น **ห่วงอนามัย** (1)
- **ประเมินผลที่ 3–5 เดือน — ถ้าลด <5% จะพิจารณาหยุดยา** · ค่าใช้จ่ายและการเก็บยาในตู้เย็น (1)

**6. ปิดการสนทนา (2 คะแนน)**
- ให้ผู้ป่วย **ทวนแผน (teach-back)** · ถามคำถาม · **ตกลงนัดติดตาม** (เช่น 4 สัปดาห์)
- แสดงความเข้าใจและให้กำลังใจ

**ข้อที่ทำให้เสียคะแนนมาก**
- ตำหนิหรือพูดว่า "แค่กินน้อยลง ออกกำลังมากขึ้น"
- สั่งยาทันทีโดยไม่ถามเรื่อง **การตั้งครรภ์และการคุมกำเนิด**
- ไม่จับได้ว่า **DMPA** เป็นยาที่ทำให้น้ำหนักขึ้น
- สัญญาว่ายาจะทำให้ลดน้ำหนักได้แน่นอนโดยไม่ต้องปรับพฤติกรรม""",
 "ref": [SLIDE + " — Drugs that cause weight gain / Antiobesity medications / Semaglutide",
         "Canadian Adult Obesity Clinical Practice Guidelines 2020"],
 "nl": OB + MS, "years": [], "_kind": "meq", "_set": "endo"}]

# กระจายตำแหน่งคำตอบ — สลับคำตอบที่ถูกไปยังตำแหน่งเป้าหมาย (เฉพาะข้อที่ตัวเลือกไม่ได้เรียงตามลำดับตัวเลข)
MOVE = {"END-MS-MCQ-01": 4, "END-MS-MCQ-06": 4, "END-OB-MCQ-09": 4, "END-OB-MCQ-14": 4,
        "END-DLP-MCQ-02": 4, "END-DLP-MCQ-09": 4, "END-DLP-MCQ-11": 4,
        "END-MS-MCQ-07": 0, "END-OB-MCQ-11": 0, "END-DLP-MCQ-04": 0,
        "END-OB-MCQ-10": 3, "END-DLP-MCQ-08": 3}
for _s in S:
    for _i in _s["items"]:
        t = MOVE.get(_i["id"])
        if t is not None and t != _i["answer"]:
            c = _i["choices"]; a = _i["answer"]
            c[a], c[t] = c[t], c[a]
            _i["answer"] = t

# ───────────────────────────── LECTURE ─────────────────────────────
LECTURE = {
 "lec": LEC,
 "title": TITLE,
 "subtitle": "เกณฑ์ MetS · BMI เกณฑ์เอเชีย · สาเหตุและยาที่ทำให้อ้วน · ภาวะแทรกซ้อน · ประเมินผู้ป่วย · ยาลดน้ำหนัก · ผ่าตัด · lipoprotein pathway · FH · เป้า LDL · TG สูง — อ.นวพร นภาทิวาอำนวย",
 "objectives": [
   "วินิจฉัย metabolic syndrome ด้วยเกณฑ์ห้าองค์ประกอบ และใช้รอบเอวตามเกณฑ์คนเอเชียได้ถูกต้อง",
   "อธิบายกลไก insulin resistance และไขมันในช่องท้องที่เชื่อมองค์ประกอบของ MetS เข้าด้วยกัน",
   "จัดระดับโรคอ้วนด้วย BMI เกณฑ์ WHO และเกณฑ์เอเชีย และบอกข้อจำกัดของ BMI",
   "ระบุยาที่ทำให้น้ำหนักขึ้นและเลือกยาทางเลือกได้",
   "ซักประวัติ ตรวจร่างกาย ส่งแล็บ และตั้งเป้าลดน้ำหนักแบบยึดภาวะแทรกซ้อนเป็นศูนย์กลาง",
   "บอกข้อบ่งชี้ ข้อห้าม และเกณฑ์หยุดยาลดน้ำหนัก รวมถึงข้อบ่งชี้ผ่าตัดลดน้ำหนักตามเกณฑ์ไทย",
   "อธิบาย exogenous และ endogenous lipoprotein pathway และการเกิด plaque",
   "แยก primary และ secondary dyslipidemia และใช้ Dutch Lipid Clinic Network criteria วินิจฉัย FH",
   "ตั้งเป้า LDL ตามระดับความเสี่ยง และเลือกยาลดไขมันเป็นขั้นตอน",
   "ดูแลภาวะไตรกลีเซอไรด์สูงและป้องกันตับอ่อนอักเสบ"],
 "sections": S, "meq": MEQ, "osce": OSCE,
 "nlGap": "**เกณฑ์ฯ ครอบคลุมทั้งสามโรคของคาบนี้โดยตรง** — `นล. 2.3.4(6)` Metabolic syndrome · `นล. 2.3.4(7)` Obesity · "
          "`นล. 2.3.9(3)` Disorders of lipoprotein metabolism and lipidemia (ทั้งสามเป็น **กลุ่ม 2 = ดูแลเองได้**) · "
          "`นล. B11.2.5(6–7)` · `นล. B7.2.5(6)` · `นล. B7.3(1)` Lipid profile · `นล. B7.4(8)` ยาลดไขมัน "
          "**แต่ไม่มีรหัสจำเพาะสำหรับยาลดน้ำหนักและการผ่าตัดลดน้ำหนัก** (หมวด `B11.4` ครอบคลุมเฉพาะยาเบาหวาน ไทรอยด์ steroid และฮอร์โมนต่อมใต้สมอง) "
          "ส่วนนี้จึงอิงแนวทางไทยและสากลที่สไลด์อ้างอิง · และ **ข้อความในสไลด์ส่วนการรักษา dyslipidemia ดึงออกมาไม่ได้** "
          "หัวข้อ 11 (ตัวเลข DLCN) หัวข้อ 12 และหัวข้อ 13 จึงเรียบเรียงจากแนวทาง ESC/EAS และตำราตามรายการด้านล่าง",
 "guidelines": [
   "**Alberti KG et al. Harmonizing the metabolic syndrome. Circulation 2009;120:1640-5** — เกณฑ์ ≥3 ใน 5 และรอบเอวตามเชื้อชาติ",
   "**Canadian Adult Obesity Clinical Practice Guidelines 2020** — ประวัติ ตรวจร่างกาย แล็บ และตารางยาที่ทำให้น้ำหนักขึ้น (ตามที่สไลด์อ้างอิง)",
   "**Rubino F et al. Definition and diagnostic criteria of clinical obesity. Lancet Diabetes Endocrinol 2025** — clinical vs preclinical obesity",
   "**แนวทางในการวินิจฉัยและรักษาโรคอ้วน พ.ศ. 2568** (สมาคมโรคอ้วนแห่งประเทศไทย) — อาหาร กิจกรรมทางกาย และยา",
   "**Eisenberg D et al. 2022 ASMBS/IFSO Indications for Metabolic and Bariatric Surgery. SOARD 2022** — เกณฑ์ผ่าตัดสากล",
   "**แนวทางเวชปฏิบัติการผ่าตัดรักษาโรคอ้วนแห่งประเทศไทย พ.ศ. 2564** — เกณฑ์ BMI 37.5 / 32.5 / 30 / 27.5",
   "**แนวทางการดูแลผู้ป่วยเบาหวานชนิดที่ 2 ให้เข้าสู่โรคเบาหวานระยะสงบ (2565)** — intensive lifestyle intervention",
   "**Mach F et al. 2019 ESC/EAS Guidelines for the management of dyslipidaemias. Eur Heart J 2020;41:111-88** (+ focused update 2025) — ระดับความเสี่ยง เป้า LDL และยา",
   "**Nordestgaard BG et al. Familial hypercholesterolaemia. Eur Heart J 2013;34:3478-90** — Dutch Lipid Clinic Network criteria",
   "**Harrison's Principles of Internal Medicine, 21st ed.** — Disorders of lipoprotein metabolism · The metabolic syndrome"],
}

# ───────────────────────────── merge ─────────────────────────────
ENDO = {
 "set": "endo",
 "title": "Endo · ต่อมไร้ท่อและเมตาบอลิซึม",
 "intro": "เริ่มจากคาบ 01 ของ อ.นวพร นภาทิวาอำนวย (Division of Diabetes and Metabolism รพ.ราชวิถี) — Metabolic syndrome, Obesity และ Dyslipidemia ซึ่งเป็นสามโรคที่มีรากเดียวกันคือ insulin resistance และไขมันในช่องท้อง เนื้อเยื่อไขมันที่ผิดปกติทำให้เกิดทั้งกลุ่มอาการเมตาบอลิก โรคอ้วนและภาวะแทรกซ้อน และไขมันในเลือดผิดปกติที่นำไปสู่หลอดเลือดแข็ง เนื้อหาเรียบเรียงจากสไลด์บรรยายจริง ร่วมกับแนวทางไทยและสากลที่อาจารย์อ้างอิง จบแต่ละหัวข้อมีข้อสอบเช็คความเข้าใจทันที",
 "howto": "**วิธีใช้** — อ่านเนื้อหาให้จบแล้วตอบข้อสอบท้ายหัวข้อ ระบบเฉลยพร้อมคำอธิบายกลไกทันทีที่ตอบ · ตอบครบทุกข้อแล้วหัวข้อจะถูกทำเครื่องหมายว่าเรียนจบ · ข้อที่ตอบผิดรวมอยู่ในแท็บ **ทบทวนข้อที่ผิด** · จบคาบแล้วไปฝึก **MEQ** และ **OSCE/SAQ** ต่อได้เลย\n\n**ลำดับที่แนะนำ** — หัวข้อ 1–3 (MetS) → 4–9 (โรคอ้วน) → 10–13 (ไขมันผิดปกติ) · ตัวเลขที่ต้องจำให้แม่นคือ **150 / 40-50 / 130-85 / 100** ของ MetS · **BMI เกณฑ์เอเชีย 23 / 25 / 30** · **จุดตัดผ่าตัดของไทย 27.5 / 32.5 / 37.5** และ **เป้า LDL 55 / 70 / 100**\n\n**หมายเหตุ** — ชุด Endo เพิ่งเริ่ม ข้อสอบทั้งหมดเป็นข้อที่เขียนใหม่จากสไลด์และแนวทางเวชปฏิบัติ ยังไม่มีคลังข้อสอบเก่า MED28–MED35 ของระบบนี้ และคาบอื่นของ Endo (เบาหวาน ไทรอยด์ ต่อมใต้สมอง ต่อมหมวกไต แคลเซียม) ยังไม่ได้ทำ",
 "label": "Endo",
 "thai": "ต่อมไร้ท่อและเมตาบอลิซึม",
 "accent": {"light": "#56661a", "soft": "#eef0e0", "ink": "#434f14",
            "dark": "#c6de6a", "darkSoft": "#1c2110", "darkInk": "#d9eb9a"},
 "file": "data/endo.json",
 "lectureCount": 0,
}

path = os.path.join(BUILD, "data", "endo.json")
data = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
data = [l for l in data if l.get("lec") != LECTURE["lec"]]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
if not any(m["set"] == "endo" for m in idx):
    idx.append(ENDO)
for m in idx:
    if m["set"] == "endo": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | items %d | meq %d | osce %d" % (len(S), sum(len(s["items"]) for s in S), len(MEQ), len(OSCE)))
print("endo.json มี %d คาบ · %d bytes" % (len(data), os.path.getsize(path)))
