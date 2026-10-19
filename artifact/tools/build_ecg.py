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

# ───────────────────────────── 8
sec("cardio-ecg-08", "ขั้นที่ 3 Axis — lead I กับ aVF",
    "ปกติ −30° ถึง +90° · LAD · RAD · extreme · axis เอียงเข้าหากล้ามเนื้อหนา หนีกล้ามเนื้อตาย", 6,
"""### หา axis เร็วที่สุด
[[fig:hexaxial]]

| lead I | aVF | axis | สาเหตุที่พบบ่อย |
|---|---|---|---|
| + | + | **ปกติ** (0° ถึง +90°) | — |
| + | − | **ซ้าย** → ดู lead II: II บวก = ยังปกติ (−30° ถึง 0°) · II ลบ = **LAD** (< −30°) | **left anterior fascicular block** · LVH · inferior MI · LBBB |
| − | + | **RAD** (> +90°) | **RVH** (PE เฉียบพลัน, pulmonary HT, COPD) · lateral MI · left posterior fascicular block · คนผอมสูง/เด็ก |
| − | − | **extreme** (−90° ถึง ±180°) | VT · ติดสายแขนสลับ · hyperK รุนแรง |

#### ทำไม axis จึงเบี่ยง (ลายมือในสไลด์: hypertrophy · infarct)
QRS axis = **ทิศเฉลี่ยของไฟฟ้าทั้ง ventricle** ซึ่งถูกกำหนดโดย "ใครมีมวลมากกว่า"
- **Hypertrophy**: ข้างที่หนามีไฟฟ้ามากกว่า → axis **เอียงเข้าหา** ข้างนั้น (RVH → ขวา)
- **Infarction**: เนื้อตายไม่มีไฟฟ้า → แรงที่เหลือชี้ **หนีจาก** บริเวณนั้น (inferior MI → axis ชี้ขึ้น → ซ้าย)
- **Fascicular block**: ส่วนที่ fascicle ขาด depolarize ทีหลัง → แรงช่วงท้ายชี้ไปทางนั้น (LAFB → ซ้ายบน)

> สไลด์หน้า axis เป็นภาพ hexaxial ทั้งหมด — ตารางสาเหตุเติมจากตำรา""",
["axis ปกติ −30° ถึง +90°",
 "I + / aVF + = ปกติ · I + / aVF − ดู II · I − / aVF + = RAD · ลบทั้งคู่ = extreme",
 "axis เอียงเข้าหากล้ามเนื้อหนา หนีกล้ามเนื้อตาย",
 "RAD ใหม่ + tachycardia + หอบ → นึกถึง RV strain จาก PE"],
[mcq(N(15), "An ECG shows a predominantly positive QRS in lead I, a predominantly negative QRS in aVF and a predominantly negative QRS in lead II. What is the QRS axis?",
     ["Left axis deviation (more negative than −30°)", "Normal axis between 0° and +90°", "Normal axis between −30° and 0°",
      "Right axis deviation (more positive than +90°)", "Extreme axis deviation"], 0,
     "lead I บวก aVF ลบ → axis อยู่ระหว่าง 0° ถึง −90° · ต้องดู **lead II (+60°)**: ถ้า II ยัง **ลบ** แปลว่า axis ตั้งฉากกับ II เลยไปแล้ว คือ **ซ้ายกว่า −30°** = **LAD**\n\n"
     "- *0 ถึง +90* — ต้อง aVF บวก\n- *−30 ถึง 0* — I บวก aVF ลบ แต่ II ยังบวก\n- *RAD* — lead I ลบ\n- *extreme* — ลบทั้ง I และ aVF",
     "I บวก aVF ลบ → ตัดสินด้วย lead II", "QRS axis", R("Axis"), [ECG, ECGA]),
 mcq(N(16), "A 45-year-old woman with sudden dyspnoea and tachycardia has a new right axis deviation on her ECG compared with one year ago. Which mechanism best explains the new right axis?",
     ["Acute right ventricular pressure overload increases the electrical forces generated by the right ventricle",
      "Loss of left ventricular myocardium shifts forces toward the left",
      "Delayed activation of the anterior-superior LV wall (left anterior fascicular block)",
      "Hyperkalaemia shortening the action potential",
      "Lead placement one intercostal space too high"], 0,
     "axis เอียง **เข้าหา** ด้านที่มีแรงไฟฟ้ามาก · PE เฉียบพลันเพิ่มแรงดันใน RV → RV ยืดและทำงานหนัก → แรงไฟฟ้าทางขวาเด่นขึ้น → **RAD ใหม่** (ร่วมกับ sinus tachycardia, RBBB ใหม่, S1Q3T3)\n\n"
     "- *LV ตาย* — แรงที่เหลือชี้หนีบริเวณที่ตาย ไม่ได้ทำให้เกิด RAD ทั่วไป (ยกเว้น lateral MI)\n- *LAFB* — ทำให้ **LAD**\n- *hyperK* — เปลี่ยนรูปคลื่น ไม่ใช่สาเหตุทั่วไปของ RAD\n- *ติด lead สูง* — มีผลกับ chest leads ไม่ใช่ axis จาก limb leads",
     "RAD ใหม่ + หอบ + tachy → คิด PE/RV strain", "Axis deviation mechanism", ["ตำรา (สไลด์ axis เป็นภาพ)"], [ECGA, ECG])],
[ECG, ECGA], {"hexaxial": F.hexaxial()})

# ───────────────────────────── 9
sec("cardio-ecg-09", "ขั้นที่ 4 Infarction — เกณฑ์ STEMI · วัด ST · territory · reciprocal · วิวัฒนาการ",
    "ST ยกใน 2 lead ติดกัน (ชาย < 40: 2.5 mm · ≥ 40: 2 mm · หญิง 1.5 mm ใน V2–V3 · lead อื่น 1 mm) · วัดเทียบ PR/TP ที่ J+60–80 ms · ทำซ้ำทุก 15–30 นาที", 10,
"""### เกณฑ์ STEMI (สไลด์)
ST ยก **ที่ J point ใน 2 lead ที่ติดกัน (contiguous)** ของผนังเดียวกัน
| lead | ชาย < 40 ปี | ชาย ≥ 40 ปี | หญิง |
|---|---|---|---|
| **V2–V3** | ≥ 2.5 mm | ≥ 2.0 mm | ≥ 1.5 mm |
| lead อื่นทั้งหมด | ≥ 1 mm | ≥ 1 mm | ≥ 1 mm |

เกณฑ์ V2–V3 สูงกว่า lead อื่นเพราะคนปกติ (โดยเฉพาะชายหนุ่ม) มี ST ยกเล็กน้อยใน V2–V3 อยู่แล้ว

### วัด ST ให้ถูก (สไลด์)
[[fig:st_measure]]

- วิธีง่ายสุด: เทียบ ST กับ **PR segment**
- แต่ **atrial repolarization (Ta wave)** มีทิศตรงข้าม P อยู่นานถึง 40–80 ms หลัง QRS → กด PR segment ให้ต่ำลง → อาจทำให้ ST ดูยกเกินจริง
- ทางเลือก: เทียบกับ **TP segment** ที่จุด **60 หรือ 80 ms หลัง J point**

### lead บอกผนัง บอกหลอดเลือด
[[fig:territories]]

| ผนัง | ST ยกใน | reciprocal (ST กด) | หลอดเลือดที่มักอุดตัน |
|---|---|---|---|
| **Inferior** | II, III, aVF | I, aVL | RCA (ส่วนใหญ่) · LCx |
| **Anterior/anteroseptal** | V1–V4 | II, III, aVF | LAD |
| **Lateral** | I, aVL, V5–V6 | III, aVF | LCx / diagonal |
| **Anterolateral (ตัวอย่างสไลด์ p80)** | V2–V6, I, aVL | II, III, aVF | LAD proximal |
| **Posterior** | (ST กด + R สูงใน V1–V3) | — | RCA / LCx → ติด V7–V9 |

#### ทำไมต้องมี "reciprocal change" (ลายมือในสไลด์)
ผนังที่ขาดเลือดสร้างกระแส injury ชี้ **เข้าหา** lead ที่มองผนังนั้น (ST ยก) → lead ที่มองจาก **ฝั่งตรงข้าม** เห็นกระแสเดียวกันวิ่งหนี → **ST กด** · การเห็น reciprocal ช่วยแยก STEMI จากภาวะที่ ST ยกทั่วไป (pericarditis, early repolarization) ซึ่งไม่มี reciprocal

### วิวัฒนาการ (สไลด์) และ "dynamic change"
[[fig:stemi_evo]]

ลายมือในสไลด์: **dynamic change · repeat EKG** — ECG แรกปกติไม่ได้ตัด ACS · ทำซ้ำทุก **15–30 นาที** ในผู้ป่วยที่ยังเจ็บ (แนวทาง ESC 2023) · ST ที่ขึ้นลงตามอาการ = ischemia จริง

#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก |
|---|---|
| **Hyperacute T** (นาทีแรก) | K รั่วออกจากเซลล์ที่ขาดเลือดมาสะสมรอบเซลล์ → repolarize เร็ว T สูงกว้าง |
| **ST ยก** | เซลล์ขาดเลือดทั้งชั้น (transmural) ศักย์พักไม่ลบพอ → กระแส injury ระหว่างเซลล์ดี–เซลล์เสีย |
| **ST กด (NSTE-ACS)** | ขาดเลือดเฉพาะชั้นใน (subendocardium) กระแสชี้ออกจาก lead |
| **Q wave** (ชั่วโมง–วัน) | เนื้อตายไม่มีไฟฟ้า = "หน้าต่าง" lead มองทะลุเห็นไฟฟ้าของผนังตรงข้ามที่วิ่งหนี |""",
["STEMI: ST ยกใน 2 lead ติดกัน · V2–V3 ชาย < 40: 2.5 · ชาย ≥ 40: 2 · หญิง 1.5 mm · lead อื่น 1 mm",
 "วัด ST เทียบ PR (ง่าย) หรือ TP ที่ J + 60–80 ms (Ta wave กด PR)",
 "II, III, aVF = inferior (RCA) · V1–V4 = anterior (LAD) · I, aVL, V5–V6 = lateral (LCx)",
 "reciprocal change ช่วยยืนยัน STEMI · ECG แรกปกติ ทำซ้ำทุก 15–30 นาที",
 "ST กด V1–V3 + R สูง → posterior MI ติด V7–V9"],
[mcq(N(17), "A 45-year-old man (no prior ECG) has 1 hour of chest pain. His ECG shows 1.5 mm ST elevation in V2 and V3, 0.5 mm in V4, and no ST changes elsewhere. According to the criteria taught, how should this be interpreted?",
     ["Does not meet STEMI criteria — men aged 40 or older need at least 2 mm in V2–V3; repeat the ECG every 15–30 minutes while symptomatic",
      "Meets STEMI criteria — any ST elevation of 1 mm or more in two contiguous leads is diagnostic",
      "Meets STEMI criteria — the threshold in V2–V3 for men over 40 is 1.5 mm",
      "Diagnostic of acute pericarditis",
      "Normal — ST elevation in V2–V3 is always a normal variant in men"], 0,
     "เกณฑ์ V2–V3 สำหรับ **ชายอายุ ≥ 40 = 2 mm** → 1.5 mm ยัง **ไม่ถึงเกณฑ์** · แต่ยังเจ็บอยู่ → **ทำ ECG ซ้ำทุก 15–30 นาที** ดู dynamic change (ลายมือในสไลด์) + troponin\n\n"
     "- *1 mm ทุก lead* — V2–V3 ใช้เกณฑ์สูงกว่าเพราะคนปกติมี ST ยกตรงนี้อยู่แล้ว\n- *1.5 mm* — เป็นเกณฑ์ของ **ผู้หญิง**\n- *pericarditis* — ต้องเป็น ST ยกทั่ว + PR กด\n- *ปกติเสมอ* — ไม่ได้ ต้องตามซ้ำเมื่อมีอาการ",
     "V2–V3: ชาย < 40 = 2.5 · ชาย ≥ 40 = 2 · หญิง = 1.5 mm", "STEMI criteria", R("Criteria (STEMI)"), [ECGS, ACS]),
 mcq(N(18), "An ECG shows ST elevation in V2–V6, I and aVL with ST depression in II, III and aVF. What is the diagnosis and the most likely culprit artery?",
     ["Acute anterolateral STEMI with inferior reciprocal changes — proximal left anterior descending artery",
      "Acute inferior STEMI — right coronary artery",
      "Acute pericarditis — no culprit artery",
      "Posterior STEMI — left circumflex artery",
      "Left ventricular hypertrophy with strain — no culprit artery"], 0,
     "ST ยก **V2–V6 + I, aVL** = anterior + lateral (anterolateral) · ST กด **II, III, aVF** = **reciprocal** ของผนังตรงข้าม → ยืนยันว่าเป็น infarction · ผนังกว้างแบบนี้มาจาก **proximal LAD** (ตรงกับตัวอย่างในสไลด์ p80: \"NSR with anterior wall MI (acute)\")\n\n"
     "- *inferior STEMI* — ST ต้อง **ยก** ใน II, III, aVF\n- *pericarditis* — ไม่มี reciprocal\n- *posterior* — ST **กด** V1–V3 ไม่ใช่ยก\n- *LVH strain* — ST กดลาดใน lead ซ้าย ไม่ใช่ ST ยกเป็นผนัง",
     "ST ยกผนังหนึ่ง + กดฝั่งตรงข้าม = STEMI จริง", "Localizing STEMI", R("Putting it all together (p80) · Infarction"), [ECGS, ACS, "B7.2.6(1)"])],
[ECG, ECGS, ACS, "B7.2.6(1)", "2.3.9(6)"],
{"st_measure": F.st_measure(), "territories": F.territories(), "stemi_evo": F.stemi_evo()})

# ───────────────────────────── 10
sec("cardio-ecg-10", "ขั้นที่ 5 Hypertrophy — P pulmonale · P mitrale · RVH · LVH",
    "RA: P > 2.5 mm · LA: P > 0.12 s หยัก · RVH: RAD + R > S ใน V1 + S ลึกค้าง V5–V6 · LVH: S V1/V2 + R V5/V6 > 35 mm", 7,
"""### Atrial enlargement (สไลด์)
[[fig:p_waves]]

| | เกณฑ์ (สไลด์) | กลไก | พบใน |
|---|---|---|---|
| **RA enlargement (P pulmonale)** | P **สูง > 2.5 mm** (lead II) | RA depolarize ก่อน LA · RA ใหญ่ → ส่วนต้นของ P สูงขึ้นแต่เวลาไม่ยาวขึ้น | pulmonary HT, COPD, PE, tricuspid disease |
| **LA enlargement (P mitrale)** | P **กว้าง > 0.12 s (3 mm)** และ **หยัก (notched)** | LA depolarize ทีหลัง · LA ใหญ่ → ส่วนท้ายยาวออก แยกเป็นสองยอด | **mitral stenosis/regurgitation**, LV diastolic dysfunction (HT) |

### Ventricular hypertrophy (สไลด์)
[[fig:lvh]]

| | เกณฑ์ (สไลด์) | กลไก |
|---|---|---|
| **LVH** | **S ใน V1 หรือ V2 + R ใน V5 หรือ V6 > 35 mm** (Sokolow–Lyon) | LV หนา มวลมาก → แรงไฟฟ้าชี้ไปซ้ายหลังมากขึ้น → R ใน lead ซ้ายสูง S ใน lead ขวาลึก |
| **RVH** | **right axis deviation + R > S ใน V1 + S ลึกค้างใน V5–V6** | RV ปกติแรงน้อยกว่า LV มาก ต้องหนามากพอจะ "ชนะ" → แรงไฟฟ้าหันไปขวาหน้า |

#### ทำไม LVH บางรายมี ST กด T กลับ (strain pattern)
ผนังหนามาก → เลือดจาก epicardial coronary ไปไม่ถึง **subendocardium** พอ (ระยะไกล + แรงดันในผนังสูง) + repolarize ผิดลำดับ → **ST กดแบบลาดลงและ T กลับหัวใน lead ซ้าย** — บ่งว่า hypertrophy รุนแรง/นาน · อย่าสับสนกับ ischemia เฉียบพลัน (เทียบ ECG เก่า)

#### ข้อจำกัด
voltage criteria **ไว (sensitivity) ต่ำ** โดยเฉพาะคนอ้วน/ถุงลมโป่งพอง (ไฟฟ้าผ่านเนื้อเยื่อหนา) และ **ให้ผลบวกลวงในคนหนุ่มผอม** → ยืนยันด้วย echocardiography""",
["P pulmonale = สูง > 2.5 mm (RA) · P mitrale = กว้าง > 0.12 s หยัก (LA)",
 "LVH: S V1/V2 + R V5/V6 > 35 mm",
 "RVH: RAD + R > S ใน V1 + S ลึกค้าง V5–V6",
 "strain = ST กดลาด + T กลับใน lead ซ้าย (subendocardium ขาดเลือดสัมพัทธ์)"],
[mcq(N(19), "A 58-year-old man with long-standing poorly controlled hypertension has an ECG with an S wave of 18 mm in V1 and an R wave of 24 mm in V5, with down-sloping ST depression and T-wave inversion in V5–V6. What is the best interpretation?",
     ["Left ventricular hypertrophy with strain pattern", "Right ventricular hypertrophy", "Acute anterolateral STEMI",
      "Left atrial enlargement only", "Normal voltage for age"], 0,
     "S V1 + R V5 = 18 + 24 = **42 mm > 35** = **LVH** (Sokolow–Lyon ตามสไลด์) · ST กดลาดลง + T กลับใน lead ซ้าย = **strain** จาก subendocardium ขาดเลือดสัมพัทธ์ในผนังที่หนา · เข้ากับ HT เรื้อรัง\n\n"
     "- *RVH* — ต้องมี RAD และ R > S ใน V1\n- *STEMI* — ต้อง ST ยก ไม่ใช่กด\n- *LAE* — ดูจาก P ไม่ใช่ QRS voltage\n- *ปกติ* — เกิน 35 mm",
     "บวก S V1 + R V5 แล้วเทียบ 35", "LVH criteria", R("Left ventricle (S V1/V2 + R V5/V6 > 35 mm)"), [ECG, "2.3.9(4)"]),
 mcq(N(20), "A 32-year-old woman with rheumatic mitral stenosis has a P wave in lead II that is 0.14 s wide with two distinct humps, but only 1.5 mm tall. What does this indicate and why?",
     ["Left atrial enlargement — the enlarged left atrium depolarizes later and longer, prolonging and notching the terminal part of the P wave",
      "Right atrial enlargement — the right atrium depolarizes first, increasing P-wave height",
      "Atrial flutter — the two humps are flutter waves",
      "First-degree AV block — the P wave merges with the PR segment",
      "Junctional rhythm — the P wave is retrograde"], 0,
     "P **กว้าง > 0.12 s และหยัก** = **P mitrale (LAE)** · P คือผลรวมของ RA (มาก่อน) + LA (ตามมา) · LA โตจาก MS ที่ต้านการไหลออก → ส่วนหลังของ P ยาวขึ้นแยกเป็นยอดที่สอง\n\n"
     "- *RAE* — P **สูง > 2.5 mm** ไม่ได้กว้าง\n- *flutter* — คลื่นต่อเนื่องฟันเลื่อย 300/นาที\n- *1st degree* — PR ยาว ไม่ใช่ P กว้าง\n- *junctional* — P หัวกลับใน II",
     "P mitrale = กว้าง + หยัก (LA) · P pulmonale = สูง (RA)", "Atrial enlargement", R("Left atrium · Right atrium"), [ECG])],
[ECG, "2.3.9(4)"], {"p_waves": F.p_waves(), "lvh": F.lvh()})

# ───────────────────────────── 11
sec("cardio-ecg-11", "AV block — 1st · Mobitz I · Mobitz II · high-grade · complete heart block",
    "PR > 200 ms · Wenckebach (AV node ล้า) · Mobitz II (His–Purkinje ล้มทันที) · P:QRS ≥ 3:1 · AV dissociation · conservative vs pacemaker", 12,
"""### AV block คืออะไร (สไลด์)
การนำไฟฟ้าผิดปกติ **ใน (intra) หรือใต้ (infra) AV node** · heart block มี 3 ระดับ: SA block · AV block · bundle branch block

[[fig:av_strips]]

| ชนิด | ECG (สไลด์) | ระดับที่ block | ความเสี่ยง |
|---|---|---|---|
| **1st degree** | **PR > 200 ms** (5 ช่องเล็ก) ทุก P ลงหมด · "marked" ถ้า > 300 ms | AV node | ต่ำ |
| **2nd Mobitz I (Wenckebach)** | PR **ยาวขึ้นเรื่อย ๆ** จน P ไม่ลง · PR ยาวสุดก่อนหลุด สั้นสุดหลังหลุด | AV node (กลับคืนได้) | ต่ำ |
| **2nd Mobitz II** | P หลุดเป็นช่วง โดย **PR คงที่** | **His–Purkinje** (โครงสร้างเสีย) | **สูง** → CHB ฉับพลัน |
| **High-grade** | P:QRS **≥ 3:1** rate ช้ามาก แต่ยังมีความสัมพันธ์ P–QRS | ได้ทั้งสองระดับ | สูง |
| **3rd (complete)** | **AV dissociation** P และ QRS มีอัตราของตัวเอง ไม่สัมพันธ์กัน (ลายมือ: own QRS · unrelated) | ได้ทั้งสองระดับ | สูง |

#### ทำไม Mobitz I PR ยาวขึ้นทีละน้อย แต่ Mobitz II ไม่เตือน (สไลด์)
[[fig:block_level]]

- **AV node** นำไฟฟ้าด้วย Ca channel ที่ฟื้นตัวช้า → แต่ละจังหวะที่มาเร็วเจอเซลล์ที่ "ยังไม่หายเหนื่อย" → นำช้าลงทีละน้อย (**decremental conduction**) จนส่งไม่ผ่าน 1 ตัว → ได้พัก → จังหวะถัดไปกลับเร็ว · สาเหตุมัก **functional/กลับคืนได้**: vagal สูง ยา (β-blocker, non-DHP CCB, digoxin) ischemia
- **His–Purkinje** ใช้ Na channel แบบ all-or-none → ส่งได้เต็มที่หรือไม่ได้เลย → P หลุด **โดยไม่มี PR ยาวนำ** · สาเหตุมัก **โครงสร้าง**: infarction (anterior MI) fibrosis (Lev–Lenègre) necrosis · มักมี **QRS กว้าง** (bundle เสียอยู่แล้ว)

#### Complete heart block: ระดับ block ตัดสินพยากรณ์ (สไลด์)
- เป็นจุดปลายของ Mobitz I หรือ II
- แบบ **AV node** เช่น vagal สูงช่วง **inferior MI** (RCA เลี้ยง AV node ใน ~90%) → escape จาก junction (QRS แคบ 40–60) · **ตอบ atropine และพยากรณ์ดีกว่า** มักหายใน 1–2 สัปดาห์
- แบบ **His–Purkinje** ล้มทั้งระบบ (anterior MI กว้าง, fibrosis) → escape จาก ventricle (QRS กว้าง 20–40) · atropine ไม่ช่วย · ต้อง pacing

#### ทำไมถึงมีอาการนี้
| อาการ/อาการแสดง | กลไก |
|---|---|
| **หน้ามืด หมดสติฉับพลัน (Stokes–Adams attack)** | Mobitz II/CHB: ventricle หยุดหรือช้ามากก่อน escape จะเริ่ม → เลือดไปสมองหยุดหลายวินาที |
| **เหนื่อยง่าย ใจเต้นช้า ความดันตก** | ventricular escape 20–40 → CO = HR × SV ต่ำ · SV เพิ่มชดเชยได้จำกัด |
| **Cannon a wave ที่คอ** (CHB) | บางจังหวะ atrium บีบตอน tricuspid ปิด (ventricle กำลังบีบ) → เลือดย้อนขึ้น jugular เป็นคลื่นใหญ่ไม่สม่ำเสมอ |
| **S1 ดังไม่เท่ากัน** (CHB) | PR สุ่มทุกจังหวะ → ลิ้นถูกปิดจากตำแหน่งต่างกัน |
| **pulse pressure กว้าง** | HR ช้า ventricle เติมนาน → SV ต่อจังหวะสูง |

### การรักษา (ลายมือในสไลด์: Mobitz I → conservative · Mobitz II → pacemaker)
| ภาวะ | การรักษา |
|---|---|
| 1st degree ไม่มีอาการ | ไม่ต้องรักษา · ทบทวนยาที่กด AV node · ติดตาม |
| Mobitz I ไม่มีอาการ | **conservative**: หายาสาเหตุ แก้ ischemia/electrolyte |
| **Mobitz II · high-grade · CHB** (โดยเฉพาะไม่มีสาเหตุที่กลับคืนได้) | **permanent pacemaker** |
| bradycardia มีอาการเฉียบพลัน (BP ตก สับสน เจ็บหน้าอก HF) | **atropine 1 mg IV ทุก 3–5 นาที (สูงสุด 3 mg)** → ไม่ได้ผล **transcutaneous pacing** หรือ dopamine 5–20 µg/kg/min / epinephrine 2–10 µg/min → temporary transvenous pacing → permanent (AHA ACLS 2020 — ไม่อยู่ในสไลด์) |""",
["1st: PR > 200 ms · Mobitz I: PR ยาวขึ้นจนหลุด · Mobitz II: PR คงที่แล้วหลุด · CHB: P กับ QRS แยกกัน",
 "Mobitz I = AV node ล้า (กลับคืนได้) → conservative · Mobitz II = His–Purkinje เสีย → pacemaker",
 "CHB ใน inferior MI = ระดับ AV node ตอบ atropine พยากรณ์ดี · ใน anterior MI = ใต้ AV node ต้อง pace",
 "bradycardia มีอาการ: atropine 1 mg (สูงสุด 3 mg) → TCP / dopamine / epinephrine",
 "cannon a wave + S1 ดังไม่เท่ากัน = AV dissociation"],
[mcq(N(21), "A 74-year-old woman has recurrent sudden syncope without warning. ECG shows sinus rhythm at 80/min, constant PR interval of 0.18 s in conducted beats, QRS 0.14 s with RBBB morphology, and intermittent non-conducted P waves without preceding PR prolongation. Where is the block and what is the definitive treatment?",
     ["Infranodal (His–Purkinje) block — permanent pacemaker",
      "AV nodal block — stop AV nodal blocking drugs and observe",
      "AV nodal block — oral theophylline",
      "Sinoatrial block — observation",
      "Infranodal block — intravenous atropine as long-term therapy"], 0,
     "P หลุดโดย **PR คงที่** = **Mobitz II** + QRS กว้าง (bundle เสียอยู่แล้ว) = block **ใต้ AV node (His–Purkinje)** ซึ่งเป็น **โครงสร้างเสีย** และเสี่ยงกลายเป็น CHB ฉับพลัน → หมดสติไม่มีสัญญาณเตือน (Stokes–Adams) → **permanent pacemaker** (ลายมือในสไลด์ Mobitz II → pacemaker)\n\n"
     "- *AV nodal + หยุดยา* — สำหรับ Mobitz I/1st degree\n- *theophylline* — ใช้บาง bradycardia หลังปลูกถ่ายหัวใจ/บาดเจ็บไขสันหลัง ไม่ใช่การรักษาหลัก\n"
     "- *SA block* — P เองหายไป ไม่ใช่ P มีแต่ไม่ลง\n- *atropine ระยะยาว* — atropine ออกฤทธิ์ที่ AV node ไม่ช่วย block ใต้ node และไม่ใช่การรักษาระยะยาว",
     "P หลุด + PR คงที่ (+ QRS กว้าง) = ใต้ AV node → pacemaker", "Mobitz II", R("Second degree AV block Mobitz II"), [ARR, ARR1, SYNC]),
 mcq(N(22), "Six hours after inferior STEMI from RCA occlusion, a patient develops complete heart block with a narrow-QRS escape rhythm at 48/min. BP 104/66 mmHg, alert. Which statement is correct?",
     ["The block is most likely at the AV node due to ischaemia and high vagal tone; it often responds to atropine and usually resolves",
      "The block is in the His–Purkinje system and requires immediate permanent pacemaker insertion",
      "Narrow-QRS escape indicates a ventricular origin and a poor prognosis",
      "Atropine is contraindicated because it will worsen the block",
      "This pattern carries a worse prognosis than complete heart block complicating anterior STEMI"], 0,
     "RCA เลี้ยง AV node ในคนส่วนใหญ่ + inferior wall มี vagal afferent มาก → CHB จาก **AV node** (ischemia + vagal) → escape จาก **junction QRS แคบ 40–60** ที่ค่อนข้างเสถียร · สไลด์: แบบนี้ **ตอบ atropine และพยากรณ์ดีกว่า** มักหายเอง (ให้ reperfusion · temporary pacing ถ้ามีอาการ)\n\n"
     "- *His–Purkinje + permanent pacing ทันที* — เป็นลักษณะของ CHB ใน **anterior** MI\n- *QRS แคบ = ventricle* — ผิด QRS แคบมาจากเหนือ His\n"
     "- *ห้าม atropine* — ห้ามเฉพาะ CHB ใต้ node ที่อาจทำให้ atrial rate เร็วขึ้นแต่ไม่ลง (ไม่ได้ผล) แต่ในระดับ node ใช้ได้\n- *แย่กว่า anterior* — ตรงข้าม",
     "CHB + inferior MI = AV node · QRS แคบ · ตอบ atropine · มักหาย", "CHB in inferior MI", R("Third degree AV block"), [ARR, ACS, "B7.2.6(1)"]),
 mcq(N(23), "Which ECG description is diagnostic of second-degree AV block Mobitz type I?",
     ["PR interval lengthens progressively until a P wave is not conducted; the PR after the dropped beat is the shortest",
      "Constant PR interval with sudden non-conducted P waves",
      "PR interval constant at 0.28 s with every P wave conducted",
      "P waves and QRS complexes at independent regular rates",
      "Two or more consecutive non-conducted P waves with a P:QRS ratio of 3:1"], 0,
     "นิยามในสไลด์: **PR ยาวขึ้นเรื่อย ๆ จน P ไม่ลง · PR ยาวสุดก่อนหลุด · สั้นสุดหลังหลุด** (AV node ได้พักหนึ่งจังหวะ)\n\n- *PR คงที่แล้วหลุด* — Mobitz II\n- *PR 0.28 ทุกตัวลง* — 1st degree\n- *อิสระต่อกัน* — 3rd degree\n- *3:1* — high-grade AV block",
     "Wenckebach = PR ยาวขึ้น → หลุด → รีเซ็ต", "Mobitz I", R("Second degree AV block Mobitz I"), [ECGR, ARR])],
[ARR, ARR1, ECGR, SYNC, COND], {"av_strips": F.av_strips(), "block_level": F.block_level()})

# ───────────────────────────── 12
sec("cardio-ecg-12", "Bundle branch block — RBBB · LBBB (WiLLiaM MaRRoW)",
    "QRS ≥ 120 ms · RBBB: rsR' ใน V1 S กว้างใน V6 · LBBB: QS/rS ลึกใน V1 R กว้างหยักใน V6 · RBBB พบในคนปกติได้", 7,
"""### กลไก (สไลด์)
bundle branch block = ทางไฟฟ้าในผนังหัวใจขาด **ทั้งหมดหรือบางส่วน** → ventricle ข้างที่ขาดไม่ได้รับไฟฟ้าจากทางด่วน ต้องรอไฟฟ้าซึมมาจากข้างที่ดี **ผ่านกล้ามเนื้อเซลล์ต่อเซลล์** → depolarize ช้าและเกิดทีหลัง → **QRS กว้าง ≥ 0.12 s** + รูปร่างที่บอกว่าข้างไหนมาทีหลัง

[[fig:bbb]]

| | RBBB | LBBB |
|---|---|---|
| ลำดับ | septum (ซ้าย→ขวา) ปกติ → LV → **RV มาทีหลัง** | **septum กลับทิศ (ขวา→ซ้าย)** → RV → **LV มาทีหลัง** |
| V1 (มองจากขวา) | **rsR' (M)** — R' คือ RV ที่มาทีหลังชี้เข้าหา V1 | **QS/rS ลึกกว้าง (W)** — ไฟฟ้าก้อนใหญ่วิ่งหนีไปซ้าย |
| V6 (มองจากซ้าย) | **S กว้าง (W)** | **R กว้างหยัก (M)** ไม่มี septal q |
| ST–T | กลับทิศกับส่วนท้ายของ QRS (secondary) | กลับทิศกับ QRS (secondary) |
| ความหมาย | **พบในคนปกติได้** · ถ้าเกิดใหม่: PE, RV strain · ร่วม MI = กล้ามเนื้อเสียหายมาก (สไลด์) | มักมีโรคหัวใจ (HT, CAD, cardiomyopathy, AS) · ทำให้อ่าน ST ของ MI ยาก |

คำจำ (ลายมือในสไลด์): **WiLLiaM MaRRoW** — **W**-L-**M** = LBBB (W ใน V1 · M ใน V6) · **M**-R-**W** = RBBB (M ใน V1 · W ใน V6)

#### LBBB กับเจ็บหน้าอก
LBBB ทำให้ ST–T ผิดปกติอยู่แล้ว → วินิจฉัย STEMI จาก ST ตามเกณฑ์ปกติไม่ได้ · แนวทางปัจจุบัน (ESC 2023) ให้ถือว่า **LBBB + อาการ ischemia ที่สงสัยมาก = จัดการเหมือน STEMI** (ส่ง reperfusion) และใช้ Sgarbossa criteria ช่วย""",
["BBB = QRS ≥ 120 ms + ventricle ข้างที่ขาดมาทีหลัง",
 "RBBB: M ใน V1 (rsR') W ใน V6 · LBBB: W ใน V1 M ใน V6 — WiLLiaM MaRRoW",
 "RBBB พบในคนปกติได้ · RBBB ใหม่ร่วม MI = เสียหายมาก",
 "LBBB + ischemic chest pain → จัดการเหมือน STEMI"],
[mcq(N(24), "An ECG shows QRS duration 0.14 s, an rsR' pattern in V1 and a broad slurred S wave in V6. What is the diagnosis and the order of ventricular activation?",
     ["Right bundle branch block — the left ventricle is activated normally and the right ventricle is activated late through myocardium",
      "Left bundle branch block — the septum is activated from right to left and the left ventricle late",
      "Left anterior fascicular block — delayed activation of the anterosuperior LV wall",
      "Ventricular pre-excitation — early activation through an accessory pathway",
      "Hyperkalaemia — slowed conduction in all myocardium"], 0,
     "QRS ≥ 0.12 + **M ใน V1 (rsR') + W/S กว้างใน V6** = **RBBB** (Ma**RR**oW) · LV depolarize ตามปกติผ่าน left bundle แล้ว RV ได้ไฟฟ้า **ทีหลัง** ผ่านกล้ามเนื้อ → แรงช่วงท้ายชี้ขวาหน้า = R' ใน V1 และ S ใน V6\n\n"
     "- *LBBB* — W/QS ใน V1 และ M ใน V6\n- *LAFB* — QRS ไม่กว้างถึง 0.12 ทำให้ LAD\n- *pre-excitation* — PR สั้น + delta wave\n- *hyperK* — QRS กว้างทั่ว ร่วม T สูงแหลม P แบน",
     "M ใน V1 = RBBB · W ใน V1 = LBBB", "RBBB", R("Bundle branch block (WiLLiaM MaRRoW)"), [ECG, ARR1]),
 mcq(N(25), "A 66-year-old man has 40 minutes of typical crushing chest pain with diaphoresis. ECG shows left bundle branch block; no previous ECG is available. What is the most appropriate approach?",
     ["Manage as a STEMI equivalent and activate urgent reperfusion while applying Sgarbossa criteria",
      "Discharge if the first troponin is normal because LBBB makes the ECG uninterpretable",
      "Diagnose acute pericarditis because of diffuse ST–T changes",
      "Treat with intravenous adenosine for a wide-complex rhythm",
      "Repeat the ECG in 24 hours before deciding"], 0,
     "LBBB เปลี่ยน ST–T อยู่แล้ว ใช้เกณฑ์ STEMI ปกติไม่ได้ · อาการ ischemia ชัดเจน + LBBB (โดยเฉพาะไม่ทราบว่าเป็นมาก่อน) → **จัดการเหมือน STEMI** ส่ง reperfusion ด่วน (ESC 2023) และใช้ Sgarbossa ช่วยยืนยัน\n\n"
     "- *กลับบ้านถ้า troponin แรกปกติ* — troponin ขึ้นช้า อันตรายมาก\n- *pericarditis* — ไม่มีลักษณะ\n- *adenosine* — ไม่ใช่ tachyarrhythmia\n- *รอ 24 ชม.* — เสียกล้ามเนื้อหัวใจ",
     "LBBB + เจ็บหน้าอกแบบ ischemia = STEMI equivalent", "LBBB and ACS", ["ESC 2023 ACS (ไม่อยู่ในสไลด์)"], [ACS, ECGS])],
[ECG, ARR1, COND], {"bbb": F.bbb()})

# ───────────────────────────── 13
sec("cardio-ecg-13", "ECG พิเศษ — pericarditis และ potassium",
    "pericarditis: ST ยกเว้าทั่วทุก lead + PR กด · hyperK: T แหลม → P แบน PR ยาว QRS กว้าง → sine wave · hypoK: T แบน ST กด U", 9,
"""### Acute pericarditis (สไลด์ · ลายมือ "PR depress")
[[fig:peri_vs_stemi]]

| | Pericarditis | STEMI |
|---|---|---|
| ST ยก | **ทั่วทุก lead** ไม่จำกัดผนัง · **เว้าหงาย** | เฉพาะผนัง · มักโค้งคว่ำ |
| reciprocal | ไม่มี (ยกเว้น **aVR** ที่ ST กด) | มี |
| PR segment | **กดลง** (aVR ยกขึ้น) | ปกติ |
| วิวัฒนาการ | T กลับหัว **หลัง** ST กลับลงแล้ว · ไม่เกิด Q | Q wave · T กลับขณะ ST ยังยก |

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก |
|---|---|
| **เจ็บหน้าอกแบบ pleuritic ดีขึ้นเมื่อโน้มตัวไปข้างหน้า** | parietal pericardium มีเส้นประสาทรับความเจ็บ (phrenic) · นอนราบ/หายใจลึกเยื่อที่อักเสบเสียดกัน · โน้มตัวลดแรงกด |
| **friction rub** | เยื่อสองชั้นที่หยาบเสียดสีกันตามจังหวะหัวใจ |
| **ST ยกทั่ว** | อักเสบที่ **epicardium รอบหัวใจ** → กระแส injury ชั้นผิวทุกผนัง |
| **PR กด** | อักเสบลามผิว **atrium** → atrial repolarization (Ta) แรงขึ้น กด PR |

(รายละเอียดการรักษาอยู่ในคาบ 04 IMPS)

### Potassium (สไลด์ HyperK / HypoK)
[[fig:potassium]]

| K | ECG | กลไก |
|---|---|---|
| **สูง ~5.5–6.5** | **T สูงแหลมฐานแคบ** (peaked) | K นอกเซลล์สูง → K channel (IKr) นำมากขึ้น → repolarize เร็ว |
| **~6.5–8** | P แบน/หาย · PR ยาว · **QRS กว้าง** | resting potential บวกขึ้น → Na channel ถูก inactivate บางส่วน → การนำไฟฟ้าช้าทั้ง atrium และ ventricle |
| **> 8** | QRS รวมกับ T เป็น **sine wave** → VF / asystole | การนำช้ามากจนเกิด re-entry หรือหยุด |
| **ต่ำ** | **T แบน · ST กด · U wave ชัด** · QT(U) ยาว | repolarization ช้าลง (IK ลด) |

ตัวเลขช่วง K เป็นค่าโดยประมาณ — ผู้ป่วยแต่ละรายเปลี่ยนไม่ตรงลำดับ และ **ECG ปกติไม่ได้ตัด hyperK อันตราย**

#### ทำไมถึงมีอาการนี้ (hyperK)
- **อ่อนแรงกล้ามเนื้อ/ปลายมือชา** — membrane ของกล้ามเนื้อลายถูก depolarize ค้าง → Na channel inactivate → กล้ามเนื้อกระตุ้นไม่ได้ (เหมือนที่หัวใจนำไฟฟ้าช้า)
- **bradycardia หรือหัวใจหยุด** — AV node และ His–Purkinje นำช้าจน block

### รักษา hyperK ที่มี ECG เปลี่ยน (แนวทาง — คลังข้อสอบถามบ่อย)
1. **Calcium gluconate 10% 10 mL IV** ใน 2–5 นาที (ทำซ้ำได้) — ไม่ได้ลด K แต่ **ทำให้ threshold ของ membrane กลับมาห่างจาก resting potential** → หัวใจเสถียรภายในนาที · ออกฤทธิ์ 30–60 นาที
2. **ย้าย K เข้าเซลล์**: regular insulin 10 U + glucose 25 g · salbutamol nebulized · (NaHCO3 ถ้ามี acidosis)
3. **ขับ K ออก**: loop diuretic · K binder · **hemodialysis** (ไตวาย/ดื้อการรักษา) · หยุดยาที่ทำให้ K สูง""",
["pericarditis: ST ยกเว้าทั่ว + PR กด · aVR ตรงข้าม · ไม่มี reciprocal",
 "hyperK: T แหลม → P แบน PR ยาว QRS กว้าง → sine wave → VF",
 "hypoK: T แบน ST กด U wave ชัด",
 "hyperK + ECG เปลี่ยน → calcium gluconate IV ก่อน (เสถียร membrane) แล้วค่อยลด K"],
[mcq(N(26), "A 61-year-old man on haemodialysis missed two sessions. K⁺ 7.4 mmol/L. ECG: tall peaked T waves, flattened P waves and QRS 0.14 s. What is the first drug to give and how does it act?",
     ["Intravenous calcium gluconate — it raises the threshold potential and stabilizes the myocardial membrane within minutes without lowering K⁺",
      "Intravenous insulin with glucose — it removes potassium from the body",
      "Oral sodium polystyrene sulfonate — it is the fastest way to lower serum K⁺",
      "Intravenous furosemide — it stabilizes the cardiac membrane",
      "Intravenous amiodarone — it treats the wide QRS"], 0,
     "ECG เปลี่ยนแล้ว (P แบน QRS กว้าง) = หัวใจเสี่ยง VF ทันที → **calcium gluconate IV** ก่อน: Ca ยก threshold potential กลับมาห่างจาก resting potential ที่บวกขึ้นจาก K สูง → **membrane เสถียรใน 1–3 นาที** แต่ **K ไม่ลด** · ตามด้วย insulin + glucose (ย้าย K เข้าเซลล์) และ **dialysis** (ขับออกจริงในรายนี้)\n\n"
     "- *insulin* — ย้าย K เข้าเซลล์ ไม่ได้ขับออก และช้ากว่า Ca\n- *resin* — ช้า (ชั่วโมง)\n- *furosemide* — ขับ K ได้น้อยในผู้ป่วยฟอกไต และไม่ได้เสถียร membrane\n- *amiodarone* — QRS กว้างจาก K ไม่ใช่ VT",
     "hyperK + ECG เปลี่ยน → Ca gluconate ก่อนเสมอ", "Hyperkalaemia ECG and treatment", R("Electrolyte abnormalities (HyperK)"), ["2.2.15", "B9.2.5(2)", ECG]),
 mcq(N(27), "A 26-year-old man has sharp chest pain worse on lying flat and relieved by leaning forward, 1 week after a viral illness. Which ECG finding best supports acute pericarditis rather than STEMI?",
     ["Widespread concave ST elevation with PR-segment depression and no reciprocal ST depression except in aVR",
      "ST elevation in II, III and aVF with ST depression in I and aVL",
      "Pathological Q waves in V1–V4",
      "Down-sloping ST depression with T inversion in V5–V6",
      "Prominent U waves with flat T waves"], 0,
     "อักเสบที่ epicardium ทั่วหัวใจ → ST ยก **ทุกผนังแบบเว้า** ไม่มี reciprocal (ยกเว้น aVR) · อักเสบลาม atrium → **PR กด** (ลายมือในสไลด์ \"PR depress\")\n\n"
     "- *ST ยก inferior + กด I/aVL* — inferior STEMI มี reciprocal\n- *Q wave V1–V4* — old anterior MI\n- *ST กดลาด + T กลับ V5–V6* — LVH strain\n- *U wave T แบน* — hypokalaemia",
     "ST ยกทั่ว + PR กด = pericarditis", "Pericarditis ECG", R("Pericarditis (ลายมือ: PR depress)"), ["2.3.9-3(6)", "B7.2.2-3(3)", ECG])],
[ECG, "2.2.15", "2.3.9-3(6)", "B7.2.2-3(3)", "B9.2.5(2)"], {"peri_vs_stemi": F.peri_vs_stemi(), "potassium": F.potassium()})

# ───────────────────────────── 14
sec("cardio-ecg-14", "รวมทุกขั้น — อ่าน ECG แบบเขียนตอบ SAQ",
    "Rate · Rhythm · Axis · (ช่วงเวลา) · Infarction · Hypertrophy → Dx · ตัวอย่างอ่าน 3 แผ่นจากสไลด์", 6,
"""### Putting it all together (สไลด์)
[[fig:read_flow]]

| ตัวอย่างในสไลด์ | อ่านตามขั้น | Dx |
|---|---|---|
| p78 | NSR · rate 13 × 6 = 78 · normal axis · no infarction · no chamber enlargement · เห็น PVC สลับ | **NSR with bigeminy PVCs** |
| p79 | rate 150 · normal axis · no infarction · **LVH** | **Sinus tachycardia with LVH** |
| p80 | NSR · rate 80 · normal axis · **STE V2–V6, I, aVL + STD II, III, aVF** · no chamber enlargement | **NSR with acute anterior wall MI** |

### รูปแบบเขียนตอบ SAQ ที่ไม่ตกคะแนน
1. **Rate**: ___/นาที (วิธีที่ใช้)
2. **Rhythm**: สม่ำเสมอหรือไม่ · มี P ไหม รูปร่าง/ทิศ · P–QRS สัมพันธ์ไหม · ชื่อจังหวะ
3. **Axis**: ปกติ/LAD/RAD
4. **Intervals**: PR · QRS · QTc
5. **Infarction / ischemia**: ST ยก/กด T กลับ Q wave · lead ไหน · reciprocal
6. **Hypertrophy**: P (RAE/LAE) · voltage (LVH/RVH)
7. **Interpretation**: จังหวะ + ความผิดปกติทั้งหมด + สิ่งที่ต้องทำต่อ (เช่น ส่ง primary PCI)

#### ข้อผิดพลาดที่พบบ่อย
- หยุดอ่านเมื่อเจอสิ่งผิดปกติแรก (เช่น เห็น AF แล้วไม่ดู ST)
- ไม่ดู calibration (10 mm/mV, 25 mm/s) และชื่อ/เวลาของ ECG
- ไม่เทียบ ECG เก่า — strain/LBBB/Q เก่าอาจไม่ใช่เรื่องเฉียบพลัน""",
["อ่านครบ 5 ขั้นทุกครั้ง + intervals แล้วค่อยสรุป",
 "Dx = จังหวะ + ความผิดปกติทุกอย่าง (เช่น NSR with bigeminy PVCs)",
 "ตรวจ calibration และเทียบ ECG เก่าเสมอ"],
[mcq(N(28), "In an ECG interpretation station, which written report is the most complete according to the 5-step approach taught?",
     ["Rate 78/min, sinus rhythm with ventricular bigeminy, normal axis, PR 0.16 s and QRS 0.09 s in sinus beats, no ST–T changes of infarction, no chamber enlargement — NSR with ventricular bigeminy",
      "Ventricular bigeminy",
      "Rate 78/min, abnormal ECG, refer to cardiology",
      "Sinus rhythm, normal axis — normal ECG",
      "PVCs present; start amiodarone"], 0,
     "อาจารย์สอนอ่าน **Rate → Rhythm → Axis → Infarction → Hypertrophy** แล้วสรุป Dx ที่รวมทุกสิ่งที่พบ — ตัวเลือกแรกตรงกับตัวอย่างในสไลด์ p78\n\n"
     "- *บอกแค่ bigeminy* — ขาด rate axis และการตัด infarction/hypertrophy\n- *abnormal refer* — ไม่ได้แปลผล\n- *ปกติ* — มองข้าม PVC\n- *เริ่ม amiodarone* — PVC bigeminy ในคนไม่มีอาการไม่ต้องให้ยาต้าน arrhythmia",
     "SAQ ECG: เขียนครบทุกขั้นแล้วสรุปเป็นประโยคเดียว", "Systematic ECG reporting", R("Putting it all together"), [ECG, ECGR, ECGA])],
[ECG, ECGR, ECGA, ECGS], {"read_flow": F.read_flow()})

# ───────────────────────────── MEQ / OSCE
LECNAME = "Common cardiac arrhythmia and basic EKG (อ.สุรชาติ)"
MEQ = [{"id": "CAR-ECG-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
        "topic": "Inferior STEMI complicated by complete heart block",
        "nl": [ACS, ECGS, ARR, SYNC, "B7.2.6(1)"], "ref": R("Infarction · Third degree AV block") + ["AHA ACLS 2020 bradycardia algorithm"],
        "vignette": "ชายไทยอายุ 66 ปี มาห้องฉุกเฉินด้วยเจ็บแน่นหน้าอกเหมือนมีของหนักทับ ร้าวไปกรามซ้าย 2 ชั่วโมง เหงื่อออก คลื่นไส้ และเกือบหมดสติ 1 ครั้งขณะเดินเข้าห้องน้ำ\n"
                    "U/D: เบาหวาน 10 ปี ความดันโลหิตสูง 8 ปี สูบบุหรี่ 40 pack-year\n"
                    "V/S: BT 36.8 °C · BP 84/52 mmHg · PR 40/min สม่ำเสมอ · RR 22/min · SpO2 95% room air\n"
                    "PE: เหงื่อท่วมตัว มือเท้าเย็น · JVP สูง 8 cm เห็น **cannon a wave** เป็นบางจังหวะ · ปอดใส ไม่มี crepitation · S1 ดังไม่เท่ากันแต่ละจังหวะ\n"
                    "12-lead ECG: P wave สม่ำเสมอ อัตรา 84/min · QRS แคบ (0.09 s) สม่ำเสมอ อัตรา 40/min · PR ไม่คงที่ ไม่สัมพันธ์กับ QRS · "
                    "**ST ยก 3 mm ใน II, III, aVF · ST กด 2 mm ใน I, aVL** · ไม่มี Q wave",
        "questions": [
            {"q": "1. จงอ่าน ECG ตามลำดับ 5 ขั้นที่เรียน และให้การวินิจฉัย (4 คะแนน)",
             "a": "- **Rate**: atrial 84/min · ventricular 40/min\n- **Rhythm**: P สม่ำเสมอ QRS สม่ำเสมอ แต่ **ไม่สัมพันธ์กัน (AV dissociation)** PR สุ่ม → **3rd-degree (complete) AV block** · escape QRS แคบ 40/min = **junctional escape**\n"
                  "- **Axis**: ปกติ (ไม่ได้ให้ข้อมูลผิดปกติ)\n- **Infarction**: **ST ยก II, III, aVF + ST กด I, aVL (reciprocal)** = **acute inferior STEMI**\n- **Hypertrophy**: ไม่มี\n\n"
                  "**Dx: Acute inferior wall STEMI complicated by complete heart block with junctional escape rhythm and cardiogenic shock / hypotension**"},
            {"q": "2. หลอดเลือดใดน่าจะอุดตัน และอธิบายกลไกที่ทำให้เกิด complete heart block ในผู้ป่วยรายนี้ (3 คะแนน)",
             "a": "- **Right coronary artery (RCA)** — inferior wall + reciprocal ใน I/aVL (ST ยก III > II ชี้ RCA)\n"
                  "- **AV nodal artery แตกแขนงจาก RCA ใน ~90%** (right dominant) → AV node ขาดเลือด\n"
                  "- inferior wall มีปลายประสาท vagus มาก → **vagal tone สูง (Bezold–Jarisch reflex)** + adenosine จากเซลล์ขาดเลือด → กด AV node\n"
                  "- block จึงอยู่ **ระดับ AV node** → escape จาก junction **QRS แคบ** อัตรา 40–60 ค่อนข้างเสถียร"},
            {"q": "3. อธิบายอาการแสดง cannon a wave และ S1 ที่ดังไม่เท่ากัน (2 คะแนน)",
             "a": "- **Cannon a wave**: atrium กับ ventricle เต้นอิสระ → บางจังหวะ atrium บีบขณะ tricuspid **ปิด** (ventricle กำลังบีบ) → เลือดย้อนขึ้น jugular เป็นคลื่นใหญ่ไม่สม่ำเสมอ\n"
                  "- **S1 ดังไม่เท่ากัน**: PR ไม่คงที่ → ลิ้น AV ถูกปิดขณะที่เปิดกว้างไม่เท่ากันในแต่ละจังหวะ (PR สั้น ลิ้นเปิดกว้าง ปิดดัง)"},
            {"q": "4. ผู้ป่วยความดันต่ำ ปอดใส JVP สูง ควรตรวจอะไรเพิ่มทันที และต้องระวังยาอะไร (2 คะแนน)",
             "a": "- ติด **right-sided leads (V4R)** — ST ยก ≥ 1 mm ใน V4R = **RV infarction** (RCA proximal) อธิบาย hypotension + JVP สูง + ปอดใส\n"
                  "- RV ที่ตายต้องพึ่ง **preload** → **หลีกเลี่ยง nitrate, morphine ขนาดสูง, diuretic** · ให้ IV fluid bolus อย่างระวัง (250–500 mL) ถ้าไม่มี pulmonary congestion\n"
                  "- bradycardia/AV dissociation ทำให้ RV เสีย atrial kick ยิ่งทำให้ CO ตก"},
            {"q": "5. จงบอกการรักษาเร่งด่วนตามลำดับ (4 คะแนน)",
             "a": "1. ABC · O2 ถ้า SpO2 < 90% · monitor · เปิด IV 2 เส้น · **แผ่น pacing ติดไว้**\n"
                  "2. **Bradycardia ที่มีอาการ** (hypotension + shock): **atropine 1 mg IV** ทุก 3–5 นาที (สูงสุด 3 mg) — block ระดับ AV node จึงมีโอกาสตอบ · "
                  "ไม่ได้ผล → **transcutaneous pacing** หรือ dopamine 5–20 µg/kg/min / epinephrine 2–10 µg/min → temporary transvenous pacing\n"
                  "3. **Reperfusion เร็วที่สุด: primary PCI** (door-to-device ≤ 90 นาที · ถ้าไม่มี PCI ≤ 120 นาทีให้ fibrinolysis ใน 30 นาที)\n"
                  "4. **DAPT**: aspirin 300 mg เคี้ยว + P2Y12 inhibitor (ticagrelor 180 mg / clopidogrel 600 mg) + anticoagulant ระหว่าง PCI\n"
                  "5. สารน้ำถ้า RV infarct · หลีกเลี่ยง nitrate/β-blocker ในระยะนี้"},
            {"q": "6. พยากรณ์ของ complete heart block รายนี้ต่างจาก complete heart block ที่เกิดใน anterior STEMI อย่างไร (2 คะแนน)",
             "a": "| | Inferior MI (รายนี้) | Anterior MI |\n|---|---|---|\n| ระดับ block | AV node (ischemia + vagal) | ใต้ AV node (His–Purkinje ตายเป็นบริเวณกว้าง) |\n"
                  "| escape | junctional QRS แคบ 40–60 | ventricular QRS กว้าง 20–40 |\n| atropine | มักได้ผล | ไม่ได้ผล |\n"
                  "| การดำเนินโรค | มักหายใน 1–2 สัปดาห์ ส่วนน้อยต้อง permanent pacemaker | มักต้อง pacemaker · บ่งว่ากล้ามเนื้อตายมาก → mortality สูง |"}]}]

OSCE = [{"id": "CAR-ECG-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
         "topic": "OSCE – Recording a 12-lead ECG (with Brugada and right-sided leads)",
         "station": "OSCE (หัตถการ) 7 นาที",
         "nl": [ECG, "B7.3(3)"], "ref": R("EKG leads placement and special leads · Anatomical correlation"),
         "instruction": "ชายอายุ 32 ปี มาห้องฉุกเฉินด้วยหมดสติขณะนอนหลับ 1 ครั้ง ญาติเล่าว่าหายใจเสียงดังเฮือกก่อนหมดสติ ปัจจุบันรู้สึกตัวดี สัญญาณชีพปกติ พ่อเสียชีวิตกะทันหันตอนอายุ 40 ปี\n\n"
                        "**จงบันทึก 12-lead ECG ให้ผู้ป่วยรายนี้ (หุ่น/ผู้ป่วยมาตรฐาน) และบันทึก lead เพิ่มเติมที่เหมาะสมกับข้อสงสัย ภายใน 7 นาที** · มีเครื่อง ECG แผ่นอิเล็กโทรด แอลกอฮอล์ และมีดโกนวางไว้ให้",
         "answer": "**เกณฑ์ให้คะแนน (16 คะแนน)**\n\n| ข้อ | สิ่งที่ต้องทำ | คะแนน |\n|---|---|---|\n"
                   "| 1 | แนะนำตัว ยืนยันตัวผู้ป่วย อธิบายว่าไม่เจ็บ ไม่มีไฟฟ้าเข้าตัว ขออนุญาต จัดความเป็นส่วนตัว ล้างมือ | 2 |\n"
                   "| 2 | ให้ **นอนหงายราบ** แขนขาวางนิ่ง ถอดโลหะ · เตรียมผิว: เช็ดแอลกอฮอล์/โกนขนถ้าจำเป็น ผิวต้องแห้ง | 2 |\n"
                   "| 3 | **Limb leads** บนแขนขา (ไม่ติดบนลำตัว): RA แขนขวา · LA แขนซ้าย · RL ขาขวา · LL ขาซ้าย | 2 |\n"
                   "| 4 | **Chest leads** หาตำแหน่งถูก: คลำ **angle of Louis → ICS2** แล้วนับลงถึง **ICS4** · V1 ขวา sternum · V2 ซ้าย sternum · V4 ICS5 midclavicular · V3 กึ่งกลาง V2–V4 · V5 anterior axillary · V6 mid-axillary ระดับเดียวกับ V4 | 3 |\n"
                   "| 5 | ตั้งเครื่อง **25 mm/s · 10 mm/mV** · filter · ให้ผู้ป่วยนิ่ง หายใจปกติ · ดู calibration mark และ artifact ก่อนกดบันทึก · บันทึกแถบ rhythm (lead II) ยาว | 2 |\n"
                   "| 6 | ระบุว่าสงสัย **Brugada syndrome** (หมดสติขณะหลับ + ประวัติครอบครัวเสียชีวิตกะทันหัน) → บันทึก **Brugada leads**: ย้าย V1/V2 ขึ้น **ICS3 และ ICS2** (ใช้ขั้ว V3–V6) | 2 |\n"
                   "| 7 | เขียนชื่อ เวลา ตำแหน่ง lead ที่ย้ายบนกระดาษ ECG · ส่งให้แพทย์อ่านทันที | 1 |\n"
                   "| 8 | บอกข้อผิดพลาดที่ทำให้อ่านผิด: ติดสูง/ต่ำ 1 ICS · ให้นั่ง · สลับสายแขน (lead I กลับหัว, aVR บวก) | 1 |\n"
                   "| 9 | ถอดอิเล็กโทรด ทำความสะอาดผิว ขอบคุณผู้ป่วย | 1 |\n\n"
                   "**จุดตาย**: นับ ICS ผิด (เริ่มจากไหปลาร้าแทน angle of Louis) ทำให้ V1–V2 สูงเกิน → อาจเห็น ST ยกปลอมใน V1–V2 · ติด limb lead ที่ลำตัวในการบันทึกมาตรฐาน"}]

LECTURE = {
 "lec": LEC, "date": "จ. 19 ต.ค.", "title": "Basic ECG และ arrhythmia ที่พบบ่อย",
 "subtitle": "อ่าน ECG 5 ขั้น Rate · Rhythm · Axis · Infarction · Hypertrophy · lead พิเศษ · premature/escape · tachyarrhythmia + ACLS · STEMI · AV block · BBB · pericarditis · potassium",
 "objectives": [
   "บอกที่มาของแต่ละคลื่นบน ECG และค่าปกติของ P, PR, QRS ได้ แล้วใช้กลไกนั้นอธิบายความผิดปกติ",
   "ติด 12-lead ECG ได้ถูกตำแหน่ง และรู้ว่าเมื่อใดใช้ Brugada leads, Lewis lead และ right-sided leads",
   "อ่าน ECG ครบ 5 ขั้น: นับ rate ได้ 3 วิธี บอก rhythm หา axis จาก lead I/aVF",
   "แยก sinus, atrial, junctional, ventricular rhythm และบอก premature, escape, accelerated rhythm ได้",
   "จำหน้าตา sinus tachycardia, flutter, AF, VT, VF และเลือกการรักษาเฉียบพลันตามชีพจร ความเสถียร และความกว้าง QRS",
   "วินิจฉัย STEMI ตามเกณฑ์ วัด ST ให้ถูก บอกผนังและหลอดเลือดจาก lead ที่ ST ยก",
   "แยก AV block ทุกชนิด บอกระดับที่ block ความเสี่ยง และการรักษา (conservative vs pacemaker)",
   "บอก RBBB/LBBB, atrial/ventricular hypertrophy, pericarditis และ hyper/hypokalemia จาก ECG"],
 "nlGap": "เกณฑ์ฯ ครอบคลุมการอ่าน ECG (`นล. 3.1.12`, `B7.3(3)a–c`) arrhythmia (`2.3.9(1)`, `B7.2.5(5)`) ACS (`2.2.1`) และ hyperK (`2.2.15`) ครบ · "
          "แต่ **สไลด์เป็นภาพ ECG เกือบทั้งหมดและไม่มีเนื้อหาการรักษา tachyarrhythmia/ACLS** (มีแค่หน้าตาคลื่น) — หัวข้อ 7 และการรักษาใน AV block/hyperK อิงแนวทางด้านล่าง · "
          "ภาพ ECG ในบทเรียนวาดขึ้นใหม่ให้ตรงเกณฑ์ ไม่ใช่ภาพจากสไลด์",
 "guidelines": [
   "**AHA Guidelines for CPR and ECC 2020 (Adult BLS/ALS) + 2023 Focused Update on Adult Advanced Cardiovascular Life Support** — tachycardia/bradycardia algorithm, ขนาดยาและพลังงานไฟฟ้า",
   "**2019 ESC Guidelines for the management of patients with supraventricular tachycardia** — vagal maneuver, adenosine",
   "**2018 ACC/AHA/HRS Guideline on the Evaluation and Management of Patients With Bradycardia and Cardiac Conduction Delay** — ข้อบ่งชี้ pacemaker",
   "**Fourth Universal Definition of Myocardial Infarction (2018)** — เกณฑ์ ST elevation ตามเพศและอายุ (ตรงกับสไลด์)",
   "**2023 ESC Guidelines for the management of acute coronary syndromes** — ECG ซ้ำ, LBBB, posterior/right-sided leads",
   "**AHA/ACCF/HRS Recommendations for the Standardization and Interpretation of the ECG (2009)** — เกณฑ์ BBB, hypertrophy, QTc"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ───────────────────────────── กระจายตำแหน่งคำตอบ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น) · ตัวเลือกเรียงตามธรรมชาติไม่สลับ
ORDERED = {N(5), N(15)}
_slot = 0
for s_ in S:
    for it in s_["items"]:
        if it["id"] in ORDERED:
            continue
        tgt = [2, 4, 1, 3, 0][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt
for s_ in S:   # ข้อที่เรียงตามธรรมชาติ: เรียงตัวเลือกใหม่ให้คำตอบไม่อยู่ A
    for it in s_["items"]:
        if it["id"] == N(5):
            it["choices"] = ["60/min", "75/min", "100/min", "120/min", "150/min"]; it["answer"] = 1
        if it["id"] == N(15):
            it["choices"] = ["Normal axis between 0° and +90°", "Normal axis between −30° and 0°", "Left axis deviation (more negative than −30°)",
                             "Right axis deviation (more positive than +90°)", "Extreme axis deviation"]; it["answer"] = 2

# ───────────────────────────── เขียนลงไฟล์ แล้วผูกข้อคลัง Ward Drill คาบ 36
path = os.path.join(BUILD, "data", SET + ".json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LEC]
pos = next((i for i, l in enumerate(data) if l["lec"] not in ("04", "10", "13", "24", "27")), len(data))
data.insert(pos, LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
BANK_MAP = {
    "cardio-ecg-07": ["C-MCQ-32", "C-MCQ-33", "C-OLD-100", "C-OLD-101", "C-OLD-102"],
    "cardio-ecg-09": ["C-OLD-104", "C-OLD-105"],
    "cardio-ecg-11": ["C-MCQ-29", "C-MCQ-30", "C-MCQ-31", "C-MCQ-34", "C-OLD-95", "C-OLD-96", "C-OLD-97", "C-OLD-98", "C-OLD-99"],
    "cardio-ecg-13": ["C-OLD-103", "C-OLD-107", "C-OLD-108", "C-OLD-109"],
    "cardio-ecg-14": ["C-OLD-106"],
}
added = link(SET, LEC, BANK_MAP, meq=[], osce=["C-OSCE-02", "C-OSCE-03"])

data = json.load(open(path, encoding="utf-8"))
L = [l for l in data if l["lec"] == LEC][0]
seen = set()
for f in os.listdir(os.path.join(BUILD, "data")):
    if f.endswith(".json") and f not in ("nl.json", "index.json"):
        for l in json.load(open(os.path.join(BUILD, "data", f), encoding="utf-8")):
            for x in [i for s_ in l["sections"] for i in s_["items"]] + l["meq"] + l["osce"] + [{"id": s_["id"]} for s_ in l["sections"]]:
                assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
                seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = ({c for s_ in L["sections"] for c in s_["nl"]} | {c for s_ in L["sections"] for i in s_["items"] for c in i.get("nl", [])}
         | {c for m in L["meq"] + L["osce"] for c in m.get("nl", [])})
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
for s_ in L["sections"]:
    assert "```" not in s_["md"], s_["id"]
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == SET: m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print("sections %d | ข้อใหม่ %d + คลัง %d = %d | meq %d | osce %d | ภาพ %d | nl %d" % (
    len(S), sum(1 for s_ in S for i in s_["items"] if i["id"].startswith("CAR-ECG")), added,
    sum(len(s_["items"]) for s_ in L["sections"]), len(L["meq"]), len(L["osce"]), sum(len(s_["figs"]) for s_ in S), len(codes)))
print("ตำแหน่งคำตอบข้อใหม่:", dict(sorted(Counter(i["answer"] for s_ in S for i in s_["items"] if i["id"].startswith("CAR-ECG")).items())))
print("%s.json มี %d คาบ: %s" % (SET, len(data), [l["lec"] for l in data]))
