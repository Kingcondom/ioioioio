#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""คาบ 36 Common cardiac arrhythmia and basic EKG (AL) — อ.สุรชาติ (Surachat Jaroonpipatkul, MD) → data/cardio.json
ต้นฉบับ: Drive 13UUiw9BU7zag_JNHWBmidA5gPoVhjTiu "Basic electrocardiography outline.pdf" (113 หน้า)
โน้ตสไลด์: slides/ecg_notes.md · ภาพประกอบ: figs_ecg.py (เครื่องวาด ECG บนกระดาษกราฟ)
คลัง Ward Drill คาบ 36: C-MCQ-29…34 · C-OSCE-02/03 · C-OLD-95…109 (23 ข้อ) ผูกท้ายสคริปต์
สไลด์ไม่มีการรักษา tachyarrhythmia/ACLS → หัวข้อ 7 อิง AHA ACLS 2020 (+2023 focused update) · ESC SVT 2019"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_bank import link
from svg import fig
import figs_ecg as F

SET, LEC = "cardio", "36"
SRC = "สไลด์ อ.สุรชาติ — Basic electrocardiography"
SRC_ADD = "AHA ACLS 2020 + 2023 focused update · ESC 2019 SVT · ACC/AHA/HRS 2018 bradycardia (ไม่อยู่ในสไลด์)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl, figs=None, source=SRC):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": source,
              "nl": nl, "md": md, "pearls": pearls, "items": items, "figs": figs or {}})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl):
    assert len(choices) == 5 and 0 <= answer <= 4 and len(set(choices)) == 5
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}
N = lambda n: "CAR-ECG-MCQ-%02d" % n
R = lambda p: ["สไลด์ อ.สุรชาติ — " + p]
ECG, ECGA, ECGR, ECGS = "3.1.12", "B7.3(3)a", "B7.3(3)b", "B7.3(3)c"
COND, ARR, ARR1, ACS = "B7.1.2(3)", "2.3.9(1)", "B7.2.5(5)", "2.2.1"
PALP, SYNC, ARREST, CPR = "2.1.36", "2.2.40", "2.2.3", "B7.4(6)"

# ───────────────────────────── 1
sec("cardio-ecg-01", "คลื่นพื้นฐานบนกระดาษ ECG — แต่ละคลื่นคือไฟฟ้าผ่านส่วนไหน",
    "P · PR · QRS · ST · T · QT · กระดาษ 25 mm/s · 10 mm = 1 mV · ค่าปกติที่ต้องจำ", 7,
"""### กระดาษ ECG (สไลด์)
- เครื่องเดินกระดาษ **25 mm/s** → 1 ช่องเล็ก (1 mm) = **0.04 s** · 1 ช่องใหญ่ (5 mm) = **0.20 s**
- Standardization **10 mm = 1 mV** → 1 ช่องเล็กแนวตั้ง = 0.1 mV · ตรวจ calibration mark ที่ต้นแถบทุกครั้ง (ถ้าตั้ง 5 mm/mV คลื่นจะดูเล็กกว่าจริงครึ่งหนึ่ง)

[[fig:beat_anatomy]]

### ไฟฟ้าเดินทางอย่างไร แล้วกลายเป็นคลื่นอะไร
[[fig:conduction]]

| คลื่น/ช่วง | เกิดจาก (กลไก) | ค่าปกติ (สไลด์) | ผิดปกติบอกอะไร |
|---|---|---|---|
| **P** | ไฟฟ้าจาก SA node กระจายทั่ว atrium (atrial depolarization) | กว้าง **< 2.5 ช่องเล็ก** (0.10 s) · สูง < 2.5 mm | ไม่มี P = ไม่ได้มาจาก sinus · P สูง/กว้าง = atrium โต |
| **PR interval** | ต้น P ถึงต้น QRS = เวลาเดินทาง atrium → ventricle ส่วนใหญ่คือ **การหน่วงใน AV node** | **0.12–0.20 s** (< 1 ช่องใหญ่) | ยาว = AV block · สั้น = มีทางลัด (pre-excitation) หรือจังหวะจาก junction |
| **QRS** | ventricle depolarize ผ่าน **His–Purkinje** (ทางด่วน) | **< 0.12 s** (< 3 ช่องเล็ก) | กว้าง = ไม่ได้ใช้ทางด่วน: bundle branch block · จังหวะจาก ventricle · K สูง |
| **ST segment** | ventricle depolarize ครบทุกเซลล์ ศักย์ไฟฟ้าเท่ากันหมด → ไม่มีกระแส | แบน ระดับเดียวกับ PR/TP | ยก/กด = มีกระแสรั่วจากเซลล์ที่บาดเจ็บ (ischemia/injury) |
| **T** | ventricle repolarize | ทิศเดียวกับ QRS ส่วนใหญ่ | สูงแหลม (K สูง, hyperacute) · กลับหัว (ischemia, strain) |
| **QT** | ventricle depolarize + repolarize ทั้งหมด | QTc ชาย < 450 · หญิง < 460 ms (แนวทาง) | ยาว → เสี่ยง torsades |

#### ทำไม ST ปกติต้อง "แบน"
ช่วง ST ทุกเซลล์ของ ventricle อยู่ใน plateau ของ action potential เดียวกัน → ไม่มีความต่างศักย์ระหว่างบริเวณ → เส้นเรียบ · ถ้ามีเซลล์บางกลุ่มขาดเลือด ศักย์พักของมันไม่ลบเท่าเพื่อน → เกิด **กระแส injury** ระหว่างเซลล์ดีกับเซลล์เสีย → เส้น ST ขยับขึ้นหรือลง (รายละเอียดหัวข้อ 9)

> ลายมือในสไลด์ (หน้า cardiac cycle): **PR ยาว → heart block** · สไลด์เขียน P = "atrial contraction" แต่ที่ถูกคือ P = atrial **depolarization** (การบีบตัวตามมาทีหลังเล็กน้อย)""",
["25 mm/s → ช่องเล็ก 0.04 s ช่องใหญ่ 0.2 s · 10 mm = 1 mV",
 "PR 0.12–0.20 s · QRS < 0.12 s · P < 2.5 ช่องเล็ก",
 "PR ยาว = AV node ช้า (block) · QRS กว้าง = ventricle ไม่ได้ใช้ทางด่วน His–Purkinje",
 "ST ควรแบนเพราะทุกเซลล์อยู่ใน plateau เดียวกัน — ยก/กด = กระแส injury"],
[mcq(N(1), "On a standard 12-lead ECG recorded at 25 mm/s, the PR interval measures 6 small squares and the QRS duration measures 2.5 small squares. Which interpretation is correct?",
     ["PR 0.24 s (prolonged, consistent with first-degree AV block); QRS 0.10 s (normal)",
      "PR 0.12 s (normal); QRS 0.05 s (normal)",
      "PR 0.30 s (marked first-degree AV block); QRS 0.125 s (bundle branch block)",
      "PR 0.24 s (normal for age over 60); QRS 0.10 s (normal)",
      "PR 0.24 s (prolonged); QRS 0.10 s (incomplete bundle branch block)"], 0,
     "1 ช่องเล็ก = 0.04 s → **PR = 6 × 0.04 = 0.24 s** (> 0.20 = ยาว = **1st-degree AV block** ตามเกณฑ์สไลด์ PR > 200 ms) · **QRS = 2.5 × 0.04 = 0.10 s** (< 0.12 ปกติ)\n\n"
     "- *0.12 / 0.05* — คิดเหมือนช่องละ 0.02 s (ใช้ได้เฉพาะเครื่องตั้ง 50 mm/s)\n- *0.30 / 0.125* — คิดช่องละ 0.05 s ผิด · 'marked' 1st degree ต้อง > 0.30 s\n"
     "- *ปกติตามอายุ* — เกณฑ์ PR > 0.20 s ใช้ทุกวัย\n- *incomplete BBB* — QRS 0.10–0.12 s และต้องมีรูปร่าง rsR' จึงจะเรียก QRS 0.10 ที่ไม่มีรายละเอียดอื่นถือว่าปกติ",
     "นับช่องเล็กแล้วคูณ 0.04 เสมอ · PR > 5 ช่องเล็ก = ยาว", "ECG paper and intervals", R("Cardiac cycle · Rate (25 mm/s)"), [ECG, ARR]),
 mcq(N(2), "Which statement best explains why the ST segment is normally isoelectric?",
     ["All ventricular myocytes are in the plateau phase of the action potential at nearly the same voltage, so no current flows between regions",
      "The atria are repolarizing during the ST segment and cancel the ventricular signal",
      "The AV node delays conduction during the ST segment",
      "Purkinje fibres stop conducting during the ST segment",
      "Coronary blood flow is maximal during the ST segment"], 0,
     "ECG บันทึก **ความต่างศักย์ระหว่างบริเวณ** ของหัวใจ · ช่วง ST ventricle ทั้งหมด depolarize ครบและอยู่ใน **plateau (phase 2)** ศักย์ใกล้เคียงกัน → ไม่มีกระแส → เส้นเรียบ · "
     "เซลล์ขาดเลือดศักย์เพี้ยน → มีกระแส injury → ST ขยับ\n\n- *atrial repolarization* — เกิดช่วง PR และต้น QRS (Ta wave) ทำให้ PR segment ต่ำลงได้ ไม่ได้ทำให้ ST แบน\n"
     "- *AV node delay* — อยู่ในช่วง PR segment\n- *Purkinje หยุดนำ* — ไม่จริง\n- *เลือดไหลมากสุด* — coronary flow มากช่วง diastole (T–P) และไม่ได้กำหนดรูปคลื่น",
     "ST ยก/กด = กระแส injury จากเซลล์ที่ศักย์ต่างจากเพื่อน", "ST segment physiology", R("Cardiac cycle"), [ECG, COND])],
[ECG, COND, "B7.1.2(1)"], {"beat_anatomy": F.beat_anatomy(), "conduction": F.conduction()})

# ───────────────────────────── 2
sec("cardio-ecg-02", "การติด lead และ lead พิเศษ — Brugada leads · Lewis lead · right-sided",
    "12 lead มองหัวใจ 12 มุม · ติดผิด 1 ICS คลื่นเปลี่ยน · Brugada leads ย้าย V1–V2 ขึ้น · Lewis lead หา P", 7,
"""### 12 lead คือกล้อง 12 ตัว
- **Limb leads** (I, II, III, aVR, aVL, aVF) มองหัวใจในแนว **ระนาบหน้า (frontal plane)** → ใช้หา axis และผนัง inferior/lateral
- **Chest leads** (V1–V6) มองใน **ระนาบแนวนอน** จากขวาไปซ้าย: V1–V2 ดู septum · V3–V4 ดู anterior · V5–V6 ดู lateral
- หลักเดียวที่ใช้ทั้งคาบ: **ไฟฟ้าวิ่งเข้าหา lead → คลื่นตั้ง · วิ่งหนี → คลื่นคว่ำ**

[[fig:chest_leads]]

| lead | ตำแหน่ง (แนวทาง) |
|---|---|
| V1 | ICS4 ขอบขวา sternum |
| V2 | ICS4 ขอบซ้าย sternum |
| V3 | กึ่งกลาง V2–V4 |
| V4 | ICS5 แนว midclavicular line ซ้าย |
| V5 | แนว anterior axillary ระดับเดียวกับ V4 |
| V6 | แนว mid-axillary ระดับเดียวกับ V4 |

### Anatomical correlation (สไลด์)
- ต้องติด lead **ตำแหน่งมาตรฐาน** และให้ผู้ป่วย **นอนหงาย**
- ติดสูง/ต่ำไป 1 ICS หรือให้นั่ง → **QRST เปลี่ยนได้มาก** (เช่น V1–V2 ติดสูงเกิน → เหมือน incomplete RBBB หรือ Brugada ปลอม · ติดต่ำ → R progression ผิด)

### Brugada leads (สไลด์)
limb leads ตามปกติ · V1/V2 ตำแหน่งมาตรฐาน · เพิ่ม **V1-1/V2-1 ที่ ICS3** (ใช้ขั้ว V3, V4) และ **V1-2/V2-2 ที่ ICS2** (ใช้ขั้ว V5, V6)
- เหตุผล: ความผิดปกติของ Brugada syndrome อยู่ที่ **RV outflow tract** ซึ่งอยู่สูงกว่าตำแหน่ง V1–V2 ปกติ → ขยับขึ้นเพิ่มโอกาสเห็น **coved ST elevation ≥ 2 mm** (type 1)

### Lewis lead (สไลด์)
[[fig:lewis]]

chest leads ตามปกติ · **RA = ICS2 ขวา (หรือ manubrium) · LA = ICS4 ขวา · RL ตำแหน่งปกติ · LL = ชายโครงขวา** · อ่านที่ **lead I** → P wave เด่นขึ้น
- ใช้เมื่อต้องการหา P ที่ซ่อนอยู่ เช่น wide complex tachycardia (เห็น P เดินอิสระจาก QRS = **AV dissociation → VT**) หรือ flutter ที่ซ่อนคลื่น

### lead เพิ่มที่ใช้บ่อยในข้อสอบ (แนวทาง — ไม่อยู่ในสไลด์)
- **Right-sided leads (V3R–V4R)** ใน inferior STEMI → ST ยก ≥ 1 mm ใน **V4R** = RV infarction (ระวังยาลด preload)
- **Posterior leads (V7–V9)** เมื่อ ST กดใน V1–V3 → หา posterior STEMI""",
["ไฟฟ้าวิ่งเข้าหา lead = คลื่นตั้ง · หนี = คว่ำ",
 "V1–V2 = ICS4 ข้าง sternum · V4 = ICS5 midclavicular",
 "Brugada leads ย้าย V1–V2 ขึ้น ICS3/ICS2 เพราะ RVOT อยู่สูง",
 "Lewis lead อ่าน lead I → P เด่น ใช้หา AV dissociation/flutter",
 "inferior STEMI ให้ติด V4R หา RV infarct"],
[mcq(N(3), "A 28-year-old man had an episode of syncope at rest. His standard 12-lead ECG shows a borderline incomplete right bundle branch pattern in V1–V2 with 1 mm ST elevation. Brugada syndrome is suspected. Which additional recording is most appropriate?",
     ["Move leads V1 and V2 up to the 3rd and 2nd intercostal spaces (high right precordial leads)",
      "Record right-sided leads V3R–V6R at the 5th intercostal space",
      "Record posterior leads V7–V9",
      "Place the limb electrodes in the Lewis configuration and read lead I",
      "Repeat the ECG with the patient sitting upright"], 0,
     "ความผิดปกติของ Brugada อยู่ที่ **RV outflow tract** ซึ่งอยู่สูง → สไลด์สอน **Brugada leads**: ย้าย V1/V2 ขึ้นไป **ICS3 (V1-1, V2-1) และ ICS2 (V1-2, V2-2)** เพิ่มความไวในการเห็น coved type 1\n\n"
     "- *V3R–V6R* — หา RV infarction ใน inferior STEMI\n- *V7–V9* — หา posterior MI\n- *Lewis lead* — ขยาย P wave หา atrial activity\n"
     "- *นั่ง* — สไลด์เตือนว่าท่านั่งทำให้ QRST เพี้ยน ไม่ใช่วิธีวินิจฉัย",
     "Brugada → ขยับ V1–V2 ขึ้น 1–2 ICS", "Brugada leads", R("Brugada leads"), [ECG, SYNC]),
 mcq(N(4), "During a regular wide-complex tachycardia at 170/min, the team wants to look for independent atrial activity that would support ventricular tachycardia. Which lead arrangement taught in this lecture is designed for this purpose?",
     ["Lewis lead: RA at the right 2nd intercostal space, LA at the right 4th intercostal space, LL at the right costal margin, then read lead I",
      "Brugada leads: V1 and V2 moved to the 2nd intercostal space",
      "Right-sided chest leads V3R and V4R",
      "Posterior leads V7–V9",
      "Standard 12-lead ECG at 50 mm/s paper speed only"], 0,
     "Lewis lead วางขั้วแขนตามแนวยาวของ atrium ด้านขวา → lead I วัดไฟฟ้าของ atrium ได้ใหญ่ขึ้น → เห็น P ชัด · ถ้า P เดินอิสระจาก QRS (**AV dissociation**) = หลักฐานสำคัญของ **VT**\n\n"
     "- *Brugada leads* — หา coved ST ใน RVOT\n- *V3R/V4R* — RV infarct\n- *V7–V9* — posterior MI\n- *50 mm/s* — ช่วยยืดคลื่นได้บ้าง แต่ไม่ได้ขยายแอมพลิจูดของ P เหมือน Lewis lead",
     "หา P ที่ซ่อน → Lewis lead (อ่าน lead I)", "Lewis lead", R("Lewis leads"), [ECG, ARR])],
[ECG, "B7.1.1(1)"], {"chest_leads": F.chest_leads(), "lewis": F.lewis()})

# ───────────────────────────── 3
sec("cardio-ecg-03", "ขั้นที่ 1 Rate — 300 / 1500 / 6 วินาที และช่วงอัตราที่ใช้ตั้งชื่อ",
    "300 ÷ ช่องใหญ่ · 1500 ÷ ช่องเล็ก · golden number 300-150-100-75-60-50 · brady < 60 · tachy 101–250 · flutter 250–350 · fib > 350", 6,
"""### อ่าน ECG 5 ขั้นของอาจารย์
**Rate → Rhythm → Axis → Infarction → Hypertrophy** — หัวข้อ 3–10 ไล่ตามลำดับนี้ (สรุปรวมหัวข้อ 14)

### นับ rate (สไลด์)
[[fig:rate_count]]

| วิธี | ใช้เมื่อ | ทำไมได้ผล |
|---|---|---|
| **300 ÷ จำนวนช่องใหญ่** ระหว่าง R–R | จังหวะสม่ำเสมอ อ่านเร็ว | 1 นาที = 60 s ÷ 0.2 s = 300 ช่องใหญ่ |
| **1500 ÷ จำนวนช่องเล็ก** | จังหวะสม่ำเสมอ ต้องการละเอียด (tachycardia) | 60 ÷ 0.04 = 1500 ช่องเล็ก |
| **นับ QRS ใน 6 วินาที × 10** | จังหวะไม่สม่ำเสมอ (AF, PAC/PVC บ่อย) | 6 วินาที = 30 ช่องใหญ่ · แถบ rhythm 10 วินาทีนับแล้ว × 6 (ตัวอย่างสไลด์ 13 × 6 = 78) |

เลขจำ ("golden number" ในลายมือ): R ตกเส้นใหญ่ถัดไป **300 – 150 – 100 – 75 – 60 – 50**

### ตั้งชื่อตามอัตรา (สไลด์)
[[fig:rate_bands]]

| อัตรา | เรียก |
|---|---|
| < 60 | bradycardia |
| 101–250 | tachycardia |
| 250–350 | flutter (อัตราของ atrium) |
| > 350 | fibrillation |
| ไม่ใช่ sinus แต่เร็วกว่าอัตราประจำตัวของจุดนั้น (ยังไม่ถึง 100) | **accelerated** rhythm |

#### ทำไม flutter/fibrillation วัดจาก "อัตราของ atrium"
ใน flutter และ AF ห้องบนเต้น 250–600 ครั้ง แต่ AV node ส่งลง ventricle ได้จำกัด (มีระยะดื้อ) → ventricular rate มักแค่ 100–180 · ถ้านับแค่ QRS จะเรียกผิด จึงต้องดูคลื่น atrium ด้วย""",
["300/ช่องใหญ่ · 1500/ช่องเล็ก · ไม่สม่ำเสมอใช้ 6 วินาที × 10",
 "golden number 300-150-100-75-60-50",
 "brady < 60 · tachy 101–250 · flutter 250–350 · fib > 350",
 "accelerated = ไม่ใช่ sinus แต่เร็วกว่าอัตราประจำตัวของจุดกำเนิด"],
[mcq(N(5), "A regular rhythm strip recorded at 25 mm/s shows the distance between consecutive R waves is exactly 4 large squares. What is the heart rate?",
     ["75/min", "60/min", "100/min", "120/min", "150/min"], 0,
     "300 ÷ 4 ช่องใหญ่ = **75/นาที** (หรือ 1500 ÷ 20 ช่องเล็ก) · ลำดับ 300-150-100-**75**-60-50\n\n- *60* — 5 ช่องใหญ่\n- *100* — 3 ช่องใหญ่\n- *120* — 2.5 ช่องใหญ่\n- *150* — 2 ช่องใหญ่",
     "R ตกเส้นใหญ่ที่ 4 = 75", "Heart rate calculation", R("Rate (300 / large square)"), [ECG, ECGR]),
 mcq(N(6), "An ECG shows an irregularly irregular narrow-complex rhythm without discernible P waves. A 10-second rhythm strip contains 22 QRS complexes. What is the ventricular rate and the best method to calculate it?",
     ["132/min — count QRS complexes on the strip and multiply (22 × 6)",
      "300/min — divide 300 by the shortest R–R interval",
      "75/min — divide 300 by the longest R–R interval",
      "Cannot be estimated without P waves",
      "110/min — divide 1500 by the average number of small squares between two adjacent R waves"], 0,
     "จังหวะ **ไม่สม่ำเสมอ** ห้ามใช้ 300/1500 กับช่วง R–R คู่เดียว เพราะแต่ละช่วงไม่เท่ากัน → ต้อง **นับ QRS ในเวลาที่รู้** · แถบ 10 วินาที → × 6 = **22 × 6 = 132/นาที** (AF with RVR)\n\n"
     "- *R–R สั้นสุด/ยาวสุด* — ได้ค่าสุดโต่ง ไม่ใช่ค่าเฉลี่ย\n- *ไม่มี P นับไม่ได้* — ventricular rate นับจาก QRS ไม่ต้องใช้ P\n"
     "- *1500 ÷ ช่วงคู่เดียว* — ใช้กับจังหวะสม่ำเสมอเท่านั้น",
     "ไม่สม่ำเสมอ → นับ QRS ในแถบ (6 s × 10 · 10 s × 6)", "Rate in irregular rhythm", R("Rate · Putting it all together (13 × 6)"), [ECG, ECGR, ARR])],
[ECG, ECGR], {"rate_count": F.rate_count(), "rate_bands": F.rate_bands()})

# ───────────────────────────── 4
sec("cardio-ecg-04", "ขั้นที่ 2 Rhythm — 4 จังหวะพื้นฐาน: sinus · atrial · junctional · ventricular",
    "ใครเร็วกว่าคุมจังหวะ · NSR 5 ข้อ · junctional P หัวกลับ 40–60 · ventricular QRS กว้าง 20–40", 8,
"""### ทำไมหัวใจมี "จุดกำเนิดสำรอง"
[[fig:pacemaker_ladder]]

เซลล์ในระบบนำไฟฟ้ามี **automaticity** (phase 4 ค่อย ๆ ขึ้นเองจนถึง threshold) แต่ความชันต่างกัน → SA node ชันสุด ยิงก่อน แล้ว **รีเซ็ตทุกจุดที่ช้ากว่า** (overdrive suppression) · จุดล่างจะโผล่มาก็ต่อเมื่อจุดบนช้าลง/หยุด หรือจุดล่างถูกกระตุ้นให้เร็วผิดปกติ

### 4 จังหวะพื้นฐาน (สไลด์)
[[fig:four_rhythms]]

| | Sinus (NSR) | Atrial | Junctional | Ventricular |
|---|---|---|---|---|
| Rate | 60–100 | 60–100 | **40–60** | **20–40** |
| Rhythm | สม่ำเสมอ | สม่ำเสมอ | สม่ำเสมอ | สม่ำเสมอ |
| P | **ตั้งใน I, II, aVF** รูปเดียวกันทุกตัว | **ไม่ใช่ sinus P** (รูป/แกนต่าง) | **หัวกลับใน II, III, aVF** หรือมองไม่เห็น | ไม่เห็น |
| PR | 0.12–0.20 คงที่ | 0.12–0.20 คงที่ | สั้นมาก/มองไม่เห็น | ไม่มี |
| QRS | < 120 ms | < 120 ms | ส่วนใหญ่ < 120 ms | **> 120 ms** |

#### ทำไม P ของ sinus ตั้งใน II แต่ของ junctional หัวกลับ
[[fig:p_axis]]

- SA node อยู่บนขวาของ atrium → ไฟฟ้ากระจาย **ลงล่างซ้าย** ซึ่งเป็นทิศเดียวกับ lead II (+60°) → P ตั้งสูงใน II
- จังหวะจาก AV junction ต้องกระตุ้น atrium **ย้อนจากล่างขึ้นบน (retrograde)** → วิ่งหนี II, III, aVF → P หัวกลับ · เวลาที่ไฟฟ้าขึ้นไป atrium กับลงไป ventricle ใกล้กัน → P มาชิด QRS / ซ่อนใน QRS / ตามหลัง QRS

#### ทำไม junctional QRS ยังแคบ แต่ ventricular QRS กว้าง
- junctional เกิด **เหนือ** His bundle → ลงไปใช้ทางด่วน His–Purkinje ได้ตามปกติ → QRS แคบ
- ventricular เกิดในกล้ามเนื้อ ventricle → กระจาย **เซลล์ต่อเซลล์** ช้ากว่า Purkinje 4–6 เท่า → QRS กว้าง และ repolarize ผิดลำดับ → **T ชี้สวนทาง QRS** (ลายมือในสไลด์: "only this QRS" = ไม่มี P นำ)""",
["NSR: 60–100 · สม่ำเสมอ · P ตั้ง I/II/aVF รูปเดียวกัน · PR 0.12–0.20 คงที่ · QRS < 120",
 "junctional 40–60 · P หัวกลับใน II/III/aVF หรือไม่เห็น · QRS แคบ",
 "ventricular 20–40 · ไม่มี P · QRS > 120 · T สวนทาง",
 "จุดที่เร็วที่สุดคุมจังหวะ (overdrive suppression)"],
[mcq(N(7), "Which set of findings fulfils the criteria for normal sinus rhythm taught in this lecture?",
     ["Rate 72/min, regular, upright uniform P waves in I, II and aVF, constant PR 0.16 s, QRS 0.09 s",
      "Rate 72/min, regular, inverted P waves in II, III and aVF, PR 0.10 s, QRS 0.09 s",
      "Rate 72/min, irregular, no visible P waves, QRS 0.09 s",
      "Rate 72/min, regular, upright P waves in I, II and aVF, PR progressively lengthening, QRS 0.09 s",
      "Rate 52/min, regular, upright P waves in I, II and aVF, constant PR 0.16 s, QRS 0.09 s"], 0,
     "เกณฑ์ NSR ในสไลด์: **rate 60–100 · สม่ำเสมอ · P ตั้งใน I, II, aVF และรูปเดียวกัน · PR 0.12–0.20 คงที่ · QRS < 120 ms** — ครบทุกข้อเฉพาะตัวเลือกแรก\n\n"
     "- *P หัวกลับใน inferior + PR สั้น* — junctional/low atrial rhythm\n- *ไม่สม่ำเสมอ ไม่มี P* — AF\n- *PR ยาวขึ้นเรื่อย ๆ* — Mobitz I\n- *rate 52* — sinus bradycardia (ไม่ใช่ normal)",
     "NSR ต้องครบ 5 ข้อ — rate ต่ำกว่า 60 เรียก sinus bradycardia", "Normal sinus rhythm criteria", R("Normal sinus rhythm"), [ECG, ECGR]),
 mcq(N(8), "A 70-year-old woman taking digoxin has a regular narrow-complex rhythm at 50/min. P waves are inverted in leads II, III and aVF and immediately follow each QRS complex. What is the origin of this rhythm and why are the P waves inverted?",
     ["AV junction — the atria are depolarized retrogradely from below, so the impulse travels away from the inferior leads",
      "Sinus node — digoxin changes the P-wave axis",
      "Ectopic focus in the high right atrium — the impulse travels toward the inferior leads",
      "Ventricle — retrograde conduction produces wide QRS complexes",
      "Sinus node with first-degree AV block — the P wave is buried in the preceding T wave"], 0,
     "rate 40–60 · QRS แคบ (ใช้ His–Purkinje ได้ = เกิดเหนือ His) · P **หัวกลับใน II, III, aVF** และอยู่หลัง QRS = **junctional rhythm** · ไฟฟ้าขึ้นไป atrium **จากล่างขึ้นบน** → วิ่งหนี lead inferior → P คว่ำ\n\n"
     "- *sinus* — P ของ sinus ต้องตั้งใน II\n- *high right atrium* — จะให้ P ตั้งใน inferior\n- *ventricle* — QRS จะกว้าง rate 20–40\n- *1st degree* — P ยังต้องตั้งและอยู่ก่อน QRS\n\n"
     "digoxin เป็นสาเหตุคลาสสิกของ junctional rhythm / accelerated junctional (หัวข้อ 5)",
     "P คว่ำใน II/III/aVF + QRS แคบ + 40–60 = junctional", "Junctional rhythm", R("Junctional rhythm"), [ECG, ECGR, COND])],
[ECG, ECGR, COND], {"pacemaker_ladder": F.pacemaker_ladder(), "four_rhythms": F.four_rhythms(), "p_axis": F.p_axis()})

# ───────────────────────────── 5
sec("cardio-ecg-05", "Premature beat · escape beat · accelerated rhythm",
    "มาก่อนกำหนด + pause vs มาหลัง pause ยาว · PAC/PJC/PVC · bigeminy · sick sinus · AIVR = reperfusion arrhythmia", 8,
"""### นิยาม (สไลด์)
- **Premature beat**: เกิด **ก่อน** จังหวะปกติ ตามด้วย **pause** ก่อนจังหวะปกติถัดไป
- **Escape beat**: เกิด **หลัง pause ยาว** ทำหน้าที่ **กันหัวใจหยุดเต้น**

### Premature beat
[[fig:premature]]

| | PAC | PJC | PVC |
|---|---|---|---|
| P | มาก่อนเวลา **รูปร่างแปลก** | หัวกลับ/ไม่เห็น | ไม่มี P นำ |
| QRS | แคบ (เหมือนปกติ) | แคบ | **กว้าง แปลกรูป T สวนทาง** |
| pause หลังจากนั้น | ไม่ครบ 2 RR (รีเซ็ต SA node) | — | **ครบ 2 RR พอดี (full compensatory)** |

#### ทำไม pause หลัง PVC จึง "ครบ" แต่หลัง PAC "ไม่ครบ"
- PAC ไฟฟ้าวิ่งเข้า SA node → SA node ถูกรีเซ็ตเริ่มนับใหม่ → จังหวะถัดไปมาเร็วกว่ากำหนดเดิม
- PVC ไฟฟ้าย้อนไม่ถึง SA node → SA node ยิงตามเวลาเดิม แต่ P ถัดไปตกช่วงที่ ventricle ยัง refractory ลงไม่ได้ → ต้องรอ P ตัวต่อไป → ช่วงห่างรวม = 2 RR

#### ทำไมผู้ป่วย PVC รู้สึก "ใจหวิว/ใจกระตุก"
PVC มาเร็ว ventricle ยังเติมเลือดไม่เต็ม → บีบเบา (ชีพจรหายไป 1 จังหวะ) → pause ยาว ventricle เติมเลือดมาก → **จังหวะถัดไปบีบแรง** ที่ผู้ป่วยรู้สึกเป็นการ "ตุ้บ"

[[fig:bigeminy]]

### Escape beat / escape rhythm
[[fig:escape]]

- เกิดเมื่อจุดบน **หยุดหรือช้า** — sinus pause/arrest, **sick sinus syndrome** (ลายมือในสไลด์), sinoatrial block, AV block
- **ห้ามกด escape** ด้วยยาต้าน arrhythmia เพราะเป็นตัวช่วยชีวิต — ต้องรักษาที่จุดบน (เช่น pacemaker ใน SSS ที่มีอาการ)

### Accelerated rhythm
[[fig:aivr]]

| จังหวะ | อัตรา | กลไก/บริบท |
|---|---|---|
| **AIVR** | ~50–110 (สูงกว่า 20–40 ของ ventricle) | automaticity ของ Purkinje เพิ่มขึ้นหลัง **reperfusion ใน STEMI** (ลายมือในสไลด์: "MI → treat → reperfusion arrhythmia") · มักหายเอง ไม่ต้องให้ยา |
| **Accelerated junctional** | 60–100 (สูงกว่า 40–60) | digoxin toxicity · inferior MI · หลังผ่าตัดหัวใจ · myocarditis (ลายมือ: P หาย/ลดลง) |""",
["premature = มาก่อน + pause · escape = มาหลัง pause ยาว (ช่วยชีวิต)",
 "PVC: QRS กว้าง ไม่มี P T สวนทาง + full compensatory pause",
 "ไม่ใช้ยากด escape rhythm — รักษาจุดบนที่หยุด",
 "AIVR หลังเปิดหลอดเลือด STEMI = reperfusion arrhythmia มักหายเอง"],
[mcq(N(9), "An ECG shows sinus rhythm at 75/min. After every sinus beat there is an early, wide (0.16 s), bizarre QRS complex not preceded by a P wave, with a T wave opposite in direction to the QRS. What is the diagnosis?",
     ["Sinus rhythm with ventricular bigeminy", "Sinus rhythm with atrial bigeminy", "Second-degree AV block, Mobitz II, 2:1",
      "Intermittent left bundle branch block", "Accelerated idioventricular rhythm"], 0,
     "QRS **มาก่อนเวลา กว้าง ไม่มี P นำ T สวนทาง** = PVC · มาสลับทุกจังหวะ = **bigeminy** (ตรงกับตัวอย่างอ่านในสไลด์ \"NSR with bigeminy PVCs\")\n\n"
     "- *atrial bigeminy* — PAC มี P แปลกรูปนำ และ QRS แคบ\n- *Mobitz II 2:1* — มี P หลุดไม่ใช่ QRS แปลกรูปเพิ่มขึ้นมา\n"
     "- *intermittent LBBB* — QRS กว้างแต่มี P นำและไม่ได้มาก่อนเวลา\n- *AIVR* — จังหวะกว้างต่อเนื่องหลายตัว อัตรา 50–110 ไม่สลับทีละตัว",
     "มาก่อน + กว้าง + ไม่มี P = PVC · ทุกตัวสลับ = bigeminy", "PVC and bigeminy", R("Premature beats · Putting it all together"), [ECG, ARR, ARR1]),
 mcq(N(10), "Thirty minutes after successful primary PCI of the LAD, a patient's monitor shows a regular wide-complex rhythm at 75/min without P waves, alternating with sinus rhythm at 70/min. Blood pressure is 124/76 mmHg and he is asymptomatic. What is the most appropriate management?",
     ["Observation — this is accelerated idioventricular rhythm, a benign reperfusion arrhythmia",
      "Intravenous amiodarone loading for ventricular tachycardia",
      "Immediate synchronized cardioversion",
      "Intravenous atropine 1 mg",
      "Urgent repeat coronary angiography for stent thrombosis"], 0,
     "QRS กว้าง ไม่มี P อัตรา **~75** (ช้ากว่า VT > 100 แต่เร็วกว่า ventricular escape 20–40) สลับกับ sinus หลังเปิดหลอดเลือด = **AIVR (reperfusion arrhythmia)** · เกิดจาก automaticity ของ Purkinje ที่เพิ่มชั่วคราว **มักหายเอง ไม่ต้องรักษา** ตราบใดที่ hemodynamics ดี\n\n"
     "- *amiodarone/cardioversion* — สำหรับ VT (> 100) และอาจกด escape ทำให้ bradycardia\n- *atropine* — ใช้ใน bradycardia ที่มีอาการ\n- *ฉีดสีซ้ำ* — ไม่มีอาการเจ็บ/ST ยกซ้ำ ไม่มีหลักฐาน stent thrombosis",
     "AIVR หลัง reperfusion = สัญญาณเปิดหลอดเลือดสำเร็จ · สังเกต", "AIVR", R("Accelerated idioventricular rhythm (ลายมือ: reperfusion arrhythmia)"), [ECG, ARR, ACS])],
[ECG, ARR, ARR1, PALP], {"premature": F.premature(), "bigeminy": F.bigeminy(), "escape": F.escape(), "aivr": F.aivr()})

# ───────────────────────────── 6
sec("cardio-ecg-06", "Tachyarrhythmia ที่ต้องจำหน้าตา — sinus tachy · flutter · AF · VT · VF",
    "re-entry 3 เงื่อนไข · flutter ฟันเลื่อย 300 → 2:1 = 150 · AF ไม่มี P RR สุ่ม · VT QRS กว้าง · VF ไม่มี QRS", 9,
"""### หน้าตาบน ECG (สไลด์ p42–46)
[[fig:tachy]]

| จังหวะ | atrial activity | QRS | RR | กลไก |
|---|---|---|---|---|
| **Sinus tachycardia** | P ปกตินำทุก QRS | แคบ | สม่ำเสมอ | SA node เร็วตามร่างกายต้องการ (ไข้ ซีด hypovolemia hyperthyroid ปวด) |
| **Atrial flutter** | **ฟันเลื่อย ~300/นาที** ใน II, III, aVF | แคบ | สม่ำเสมอ (2:1 → **150**) | macro re-entry วนรอบ tricuspid annulus (cavotricuspid isthmus) |
| **Atrial fibrillation** | ไม่มี P · เส้นฐานสั่น > 350 | แคบ | **ไม่สม่ำเสมอแบบสุ่ม** | micro re-entry หลายวง (ต้นเหตุมักอยู่ที่ pulmonary vein) |
| **VT** | P เดินอิสระ (AV dissociation) ถ้าเห็น | **กว้าง** | สม่ำเสมอ (monomorphic) | re-entry รอบแผลเป็นใน ventricle (old MI) |
| **VF** | — | **ไม่มี QRS** ยุ่งเหยิง | — | หลายวงใน ventricle → ไม่บีบ = cardiac arrest |

### Re-entry — กลไกร่วมของ tachycardia ส่วนใหญ่
[[fig:reentry]]

ต้องมีครบ 3 อย่าง: **(1) สองทาง** ที่นำไฟฟ้าและฟื้นตัวต่างกัน **(2) block ทางเดียวชั่วคราว** (มักจาก beat ที่มาก่อนเวลา) **(3) ทางวนยาว/ช้าพอ** ให้ทางแรกฟื้น · เข้าใจข้อนี้แล้วจะเข้าใจการรักษา: ยาหรือไฟฟ้าที่ทำให้ส่วนใดของวง "ดื้อ" พร้อมกันจะตัดวงได้

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | ใช้แยกอย่างไร |
|---|---|---|
| **ใจสั่น** เริ่ม–หยุดทันที | re-entry เริ่มด้วย premature beat และหยุดเมื่อวงถูกตัด | sinus tachy ค่อย ๆ เร็วขึ้นและค่อย ๆ ช้าลง |
| **คอตุบ (neck pounding) ใน AVNRT** | atrium กับ ventricle บีบพร้อมกัน → atrium บีบใส่ tricuspid ที่ปิด → เลือดย้อนขึ้น jugular (cannon a wave) | เด่นใน AVNRT |
| **ชีพจรไม่สม่ำเสมอแบบไม่มีรูปแบบ + pulse deficit** | AF: RR สุ่ม จังหวะที่ RR สั้น ventricle เติมไม่เต็ม แรงดันไม่ถึงข้อมือ | นับ apical > radial |
| **ความดันตก มึน หมดสติ** | VT: ventricle เร็วจนเติมเลือดไม่ทัน + ไม่ประสานกับ atrium → CO ตก | VT มักมีโรคหัวใจเดิม (old MI, EF ต่ำ) |
| **หมดสติ ไม่มีชีพจรทันที** | VF: ไม่มีการบีบ CO = 0 | ต้อง defibrillate |

### Wide QRS tachycardia — ให้คิดว่าเป็น VT ก่อน
QRS กว้าง + เร็ว อาจเป็น VT หรือ SVT ที่นำผิดปกติ (aberrancy/BBB เดิม) · ในผู้ป่วยที่มี **โรคหัวใจโครงสร้าง/old MI** VT เป็นไปได้สูงสุด · หลักฐานชี้ VT: **AV dissociation** (P เดินอิสระ — หาด้วย Lewis lead), fusion/capture beat · การให้ยา SVT (เช่น verapamil) ใน VT ทำให้ความดันตกได้ จึง **ถือว่าเป็น VT จนกว่าจะพิสูจน์ได้**""",
["HR 150 สม่ำเสมอ QRS แคบ → นึกถึง flutter 2:1 เสมอ",
 "AF = ไม่มี P + RR ไม่สม่ำเสมอแบบสุ่ม",
 "re-entry: 2 ทาง + block ทางเดียว + วนช้าพอ",
 "wide complex tachycardia → คิดว่า VT จนกว่าจะพิสูจน์ (โดยเฉพาะ old MI)",
 "VF = ไม่มี QRS ไม่มีชีพจร → defibrillate"],
[mcq(N(11), "A 64-year-old man has palpitations. ECG shows a regular narrow-complex tachycardia at exactly 150/min. In leads II, III and aVF there is a continuous saw-tooth baseline at about 300/min. What is the diagnosis and mechanism?",
     ["Atrial flutter with 2:1 AV conduction — macro re-entry around the tricuspid annulus",
      "Sinus tachycardia — enhanced automaticity of the sinus node",
      "Atrial fibrillation — multiple wavelets in the atria",
      "AV nodal re-entrant tachycardia — re-entry within the AV node",
      "Ventricular tachycardia — re-entry around a ventricular scar"], 0,
     "คลื่น **ฟันเลื่อย 300/นาที** ใน inferior leads + ventricular rate **150 พอดี** (AV node ปล่อยลงทุก 2 คลื่น) = **atrial flutter 2:1** · กลไก macro re-entry วนรอบ tricuspid annulus ผ่าน cavotricuspid isthmus (จุดที่ ablation ตัด)\n\n"
     "- *sinus tachy* — มี P ปกตินำ ไม่มีฟันเลื่อย\n- *AF* — RR ไม่สม่ำเสมอ\n- *AVNRT* — ไม่มีคลื่น atrium ต่อเนื่อง (P มักซ่อนใน QRS)\n- *VT* — QRS กว้าง",
     "HR 150 พอดี + QRS แคบ → หาฟันเลื่อย (flutter 2:1)", "Atrial flutter", R("Atrial flutter"), [ECG, ECGR, ARR]),
 mcq(N(12), "Which combination is required for a re-entrant tachycardia such as AVNRT to start?",
     ["Two pathways with different conduction and refractory properties, unidirectional block in one pathway, and slow enough conduction for the blocked pathway to recover",
      "A single pathway with very rapid conduction and no refractory period",
      "Increased automaticity of the sinus node due to catecholamines",
      "Complete block in both pathways at the same time",
      "Triggered activity caused by early afterdepolarizations during a long QT interval"], 0,
     "re-entry ต้องมี **2 ทาง · block ทางเดียว · วนช้าพอให้ทางที่ block ฟื้น** → ไฟฟ้าวนต่อไม่รู้จบ · AVNRT: PAC ลงทางช้าเพราะทางเร็วยังดื้อ แล้วย้อนขึ้นทางเร็วที่ฟื้นแล้ว\n\n"
     "- *ทางเดียวไม่มี refractory* — วนไม่ได้\n- *sinus automaticity* — กลไกของ sinus tachycardia\n- *block ทั้งสองทาง* — คือการ **ตัด** วง (สิ่งที่ adenosine ทำ)\n"
     "- *EAD/long QT* — triggered activity → torsades ไม่ใช่ re-entry แบบ AVNRT",
     "ตัดวง re-entry = ทำให้จุดใดจุดหนึ่งของวงดื้อ (vagal, adenosine, shock)", "Re-entry mechanism", ["ESC 2019 SVT (กลไก — ไม่อยู่ในสไลด์)"], [ARR, ARR1, COND])],
[ECG, ECGR, ARR, ARR1, PALP], {"tachy": F.tachy(), "reentry": F.reentry()})

# ───────────────────────────── 7
sec("cardio-ecg-07", "รักษา tachyarrhythmia เฉียบพลัน — ชีพจร · เสถียร · QRS (ACLS)",
    "ไม่มีชีพจร → defibrillate (unsync) · ไม่เสถียร → synchronized cardioversion · แคบสม่ำเสมอ → vagal → adenosine 6 → 12 · กว้าง → amiodarone", 9,
"""> หัวข้อนี้ **ไม่อยู่ในสไลด์** (สไลด์สอนการอ่าน) แต่คลังข้อสอบคาบ 36 ถามการรักษาหลายข้อ — อิง **AHA ACLS 2020** (+ 2023 focused update) และ **ESC 2019 SVT**

[[fig:acls]]

### คำถาม 3 ข้อตามลำดับ
1. **มีชีพจรไหม** — ไม่มี (pulseless VT/VF) = cardiac arrest → CPR + **defibrillation แบบ unsynchronized** ทันที (biphasic 120–200 J ตามเครื่อง · ถ้าไม่ทราบใช้สูงสุด) + epinephrine 1 mg ทุก 3–5 นาที · ยังเป็น VF/pVT หลังช็อกครั้งที่ 3 → **amiodarone 300 mg** (ครั้งต่อไป 150 mg)
2. **เสถียรไหม** — สัญญาณไม่เสถียร: **hypotension · ซึม/สับสน · ischemic chest pain · acute heart failure · shock** → **synchronized cardioversion** (narrow regular 50–100 J · AF 120–200 J · monomorphic VT 100 J)
3. **เสถียร → ดู QRS**
   - **แคบ + สม่ำเสมอ** (AVNRT/AVRT): **vagal maneuver** (modified Valsalva) → **adenosine 6 mg IV push เร็ว + flush 20 mL** → ไม่หาย 12 mg
   - **แคบ + ไม่สม่ำเสมอ** (AF/flutter แปรผัน): คุม rate (β-blocker, non-DHP CCB) + ประเมิน anticoagulation (คาบ 24)
   - **กว้าง**: ถือเป็น VT → **amiodarone 150 mg IV ใน 10 นาที** (หรือ procainamide) เตรียม synchronized cardioversion · ปรึกษาผู้เชี่ยวชาญ

#### ทำไมต้อง "sync" ใน cardioversion แต่ "ไม่ sync" ใน VF
ช็อกที่ตกช่วง **T wave (vulnerable period)** ซึ่งเซลล์บางส่วนฟื้นบางส่วนยังดื้อ อาจเหนี่ยวนำ **VF** → เครื่อง sync จะรอช็อกตรง R · แต่ VF/pulseless VT **ไม่มี R ชัดให้ sync** และต้องการช็อกทันที → ใช้แบบ unsync

#### ทำไม adenosine หยุด AVNRT ได้ — และทำไมต้องฉีดเร็ว
adenosine จับ **A1 receptor ที่ AV node** → เปิด K channel → AV node **ไม่นำไฟฟ้าชั่วขณะ (ไม่กี่วินาที)** → วง re-entry ที่ต้องผ่าน AV node ถูกตัด · ถูกทำลายในเลือดเร็วมาก (half-life < 10 วินาที) จึงต้อง **push เร็วทางหลอดเลือดใหญ่แล้ว flush ตาม** · ใน flutter/AF ไม่หาย แต่ช่วงที่ AV block ชั่วคราวจะ **เผยคลื่นฟันเลื่อย** ช่วยวินิจฉัย
- เตือนผู้ป่วย: แน่นหน้าอก หน้าแดง รู้สึก "หัวใจหยุด" ไม่กี่วินาที · ระวังใน asthma รุนแรง""",
["คำถามแรก: มีชีพจรไหม → ไม่มี = defibrillate (unsync) + CPR",
 "ไม่เสถียร (BP ตก สับสน เจ็บหน้าอก HF) → synchronized cardioversion",
 "แคบสม่ำเสมอเสถียร → vagal → adenosine 6 → 12 mg push เร็ว + flush",
 "wide complex เสถียร → amiodarone 150 mg/10 นาที เตรียม cardioversion",
 "sync เพื่อไม่ให้ช็อกตกช่วง T (vulnerable) แล้วเกิด VF"],
[mcq(N(13), "A 35-year-old woman has sudden palpitations for 30 minutes. BP 118/74 mmHg, alert, no chest pain. ECG: regular narrow-complex tachycardia at 186/min without visible P waves. A modified Valsalva manoeuvre fails. What is the next step and why must it be given rapidly?",
     ["Adenosine 6 mg rapid IV push followed by a saline flush — it is metabolised within seconds and transiently blocks the AV node, breaking the re-entry circuit",
      "Adenosine 6 mg slow IV infusion over 10 minutes — to avoid transient asystole",
      "Synchronized cardioversion at 50–100 J — because the rate is over 150/min",
      "Amiodarone 150 mg IV over 10 minutes — first-line for all regular tachycardias",
      "Atropine 1 mg IV — to increase AV nodal conduction"], 0,
     "เสถียร + QRS แคบ สม่ำเสมอ (น่าจะเป็น AVNRT) → vagal ไม่หาย → **adenosine 6 mg push เร็ว + flush** (ไม่หาย 12 mg) · ออกฤทธิ์ที่ **A1 receptor ของ AV node** ทำให้ AV node ไม่นำไฟฟ้าชั่วขณะ ตัดวง re-entry · half-life < 10 วินาทีจึงต้องฉีดเร็ว\n\n"
     "- *infusion ช้า* — ยาสลายก่อนถึงหัวใจ ไม่ได้ผล\n- *cardioversion* — ใช้เมื่อ **ไม่เสถียร** ไม่ได้ตัดสินด้วย rate\n- *amiodarone* — สำหรับ wide complex/VT\n- *atropine* — เพิ่มการนำผ่าน AV node ตรงข้ามกับที่ต้องการ",
     "AVNRT เสถียร: vagal → adenosine 6 → 12 mg push เร็ว", "SVT management", ["AHA ACLS 2020 · ESC 2019 SVT (ไม่อยู่ในสไลด์)"], [ARR, ARR1, "B7.4(7)"]),
 mcq(N(14), "A 70-year-old man with a previous anterior MI has a regular wide-complex tachycardia at 190/min. BP 76/40 mmHg, he is drowsy but has a palpable carotid pulse. What is the most appropriate immediate treatment?",
     ["Synchronized cardioversion", "Unsynchronized defibrillation", "Intravenous adenosine 6 mg", "Intravenous verapamil 5 mg",
      "Intravenous amiodarone 150 mg over 10 minutes before any electrical therapy"], 0,
     "QRS กว้างใน old MI = VT จนกว่าจะพิสูจน์ · **มีชีพจร** แต่ **ไม่เสถียร** (BP 76/40 ซึม) → **synchronized cardioversion** ทันที (sync ให้ช็อกตรง R)\n\n"
     "- *unsync defibrillation* — สำหรับ **pulseless** VT/VF\n- *adenosine* — ไม่ช่วย VT และเสียเวลาในผู้ป่วยไม่เสถียร\n"
     "- *verapamil* — ห้ามใน wide complex tachycardia: ถ้าเป็น VT จะกดหัวใจ ความดันตกรุนแรง\n- *amiodarone ก่อน* — ใช้ใน VT ที่ **เสถียร**",
     "มีชีพจร + ไม่เสถียร = synchronized cardioversion", "Unstable VT", ["AHA ACLS 2020 (ไม่อยู่ในสไลด์)"], [ARR, ARREST, CPR])],
[ARR, ARR1, ARREST, CPR, "B7.4(7)"], {"acls": F.acls()}, source=SRC_ADD)

# ===== SECTIONS 8-14 =====

# ===== FOOTER =====
