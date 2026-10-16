#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""คาบ 27 Valvular heart disease และ Acute rheumatic fever (พ.ญ.ชนัญญา) → data/cardio.json
ต้นฉบับ: Drive 1IVsvzRiGSfwCrfi6wcJt49fkwP4Zfzq2 "Lec 4 VHD student 4th year_modified" · บรรยาย อ. 6 ต.ค. 2569
โน้ตสไลด์: slides/vhd_arf_notes.md · สไลด์อิงแผนภูมิ ACC/AHA 2020
ผู้ใช้ขอให้อัปเดตการวินิจฉัย/รักษาตามแนวทางล่าสุด → ESC/EACTS 2025 (VHD) · WHO 2024 (RF/RHD) ·
ESC 2023 + Duke-ISCVID 2023 (IE — ไม่อยู่ในสไลด์ แต่มีในคลัง Ward Drill คาบ 27)
ข้อคลัง Ward Drill คาบ 27 (31 ข้อ) ผูกท้ายสคริปต์"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_bank import link

NLN = ["2.3.9-3(8)", "B7.2.3-3(1)"]
ARF = ["2.3.9-3(1)", "B7.2.2-3(1)"]
IE = ["2.3.9-3(5)", "B7.2.2-3(2)"]
SRC = "สไลด์ พ.ญ.ชนัญญา — Valvular heart disease and acute rheumatic fever"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None, src=SRC):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": src,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "CAR-VHD-MCQ-%02d" % n
R = lambda p: ["สไลด์ พ.ญ.ชนัญญา — " + p]
ESC25 = "ESC/EACTS 2025 Guidelines for the management of valvular heart disease"

# ───────────────────────────── 1
sec("cardio-vhd-01", "ตรวจร่างกายลิ้นหัวใจ — ดู คลำ เคาะ ฟัง",
    "apical impulse · heave · thrill = murmur ≥ 4/6 · สี่ตำแหน่งฟัง · บรรยาย murmur ให้ครบห้าองค์ประกอบ", 8,
"""### ลำดับที่สไลด์วางไว้: **ดู → คลำ → เคาะ → ฟัง**
| ขั้น | สิ่งที่หา | ความหมาย |
|---|---|---|
| **ดู (inspection)** | รูปทรงทรวงอก (pectus, หลังตรงผิดปกติ) · การเต้นที่มองเห็น | ทรวงอกผิดรูปพบร่วมกับ **MVP และ Marfan** |
| **คลำ (palpation)** | **apical impulse** · **heave** · **thrill** | ดูหัวข้อถัดไป |
| **เคาะ (percussion)** | ขอบความทึบของหัวใจ | ขนาดและรูปร่างหัวใจ |
| **ฟัง (auscultation)** | สี่ตำแหน่ง: **aortic (AVA) · pulmonic (PVA) · tricuspid (TVA) · mitral (MVA)** | S1 S2 เสียงเสริม murmur |

### การคลำ
- **Apical impulse ปกติ** — **ช่องซี่โครงที่ 5 ซ้าย แนว midclavicular ขนาดไม่เกิน 3 ซม.** · กว้างกว่า 3 ซม. = **diffuse apical impulse** · ย้ายออกด้านข้าง = ห้องล่างซ้ายโต
- apical impulse **ไม่ใช่** point of maximal impulse (PMI) เสมอไป — เช่นใน RV โต จุดที่เต้นแรงสุดอาจอยู่ข้างกระดูกอก
- **Heave** — ยกมือขึ้นเป็นจังหวะ = **LV หรือ RV หนาตัว/ขยาย** (RV heave คลำที่ข้างกระดูกอกซ้ายส่วนล่าง)
- **Thrill** — แรงสั่นที่คลำได้ = **murmur ระดับ ≥ 4/6** (นิยามของเกรด 4 คือมี thrill)

### เสียงหัวใจ
- **S1 ("lub") = M1 + T1** — ลิ้น mitral และ tricuspid ปิด → เริ่ม systole
- **S2 ("dub") = A2 + P2** — ลิ้น aortic และ pulmonic ปิด → เริ่ม diastole

### บรรยาย murmur ให้ครบ (สไลด์)
1. **systole หรือ diastole**
2. **รูปแบบและความถี่** (ejection/crescendo-decrescendo · pansystolic · decrescendo · rumbling)
3. **ความดัง** (เกรด 1–6 สำหรับ systolic · 1–4 สำหรับ diastolic)
4. **ตำแหน่งที่ดังสุดและการกระจาย**
ตัวอย่างของอาจารย์: **"pansystolic murmur grade II at MVA, radiation to axilla"**
""",
    ["ดู → คลำ → เคาะ → ฟัง",
     "Apical impulse ปกติ: ICS 5 ซ้าย MCL < 3 ซม. · > 3 ซม. = diffuse",
     "Heave = ห้องหัวใจหนา/ขยาย · thrill = murmur ≥ 4/6",
     "S1 = M1+T1 · S2 = A2+P2",
     "บรรยาย murmur: จังหวะ · รูปแบบ · ความดัง · ตำแหน่ง · การกระจาย"],
    [mcq(N(1), "On examination a harsh systolic murmur is accompanied by a palpable vibration over the same area. What is the minimum grade of this murmur?",
         ["Grade 1/6", "Grade 2/6", "Grade 3/6", "Grade 4/6", "Grade cannot be assigned when a thrill is present"], 3,
         "สไลด์: **thrill = palpable vibrations → murmur ≥ grade 4/6** — นิยามของเกรด 4 คือ murmur ที่ดังจนคลำได้เป็นแรงสั่น\n\nเกรด 1–3 ไม่มี thrill (1 = ต้องตั้งใจฟัง · 2 = เบาแต่ได้ยินชัด · 3 = ดังปานกลาง) · เกรด 5 ได้ยินเมื่อหูฟังแตะเพียงขอบ · เกรด 6 ได้ยินโดยหูฟังไม่แตะผิว",
         "มี thrill = murmur ≥ 4/6", "Murmur grading", R("Palpation"), NLN + ["B7.1.2(1)"]),
    ], NLN + ["B7.1.2(1)"])

# ───────────────────────────── 2
sec("cardio-vhd-02", "แยก murmur ตามจังหวะและรูปแบบ",
    "Ejection = AS/PS · Pansystolic = MR/TR/VSD · Blowing = AR/PR · Rumbling = MS/TS · Continuous = PDA", 9,
"""### ตารางหลักของสไลด์
| จังหวะ | รูปแบบ | ลิ้น |
|---|---|---|
| **Systolic** | **Ejection (crescendo–decrescendo)** | **AS · PS** |
| | **Pansystolic (holosystolic)** | **MR · TR** (และ VSD) |
| **Diastolic** | **Blowing (high-pitched decrescendo)** | **AR · PR** |
| | **Rumbling (low-pitched)** | **MS · TS** |
**ทำไมรูปแบบต่างกัน**
- **Ejection** — เลือดพุ่งผ่านลิ้นที่ตีบเฉพาะช่วงที่ห้องล่างบีบดันเลือดออก แรงสุดกลาง systole แล้วเบาลง
- **Pansystolic** — ห้องล่างความดันสูงกว่าห้องบน (หรือห้องขวา) ตลอด systole เลือดจึงรั่วย้อนตั้งแต่ S1 ถึง S2
- **Blowing** — aorta ความดันสูงกว่า LV มากที่สุดต้น diastole แล้วค่อยลดลง → ดังต้นแล้วเบา เสียงแหลม
- **Rumbling** — ความดันต่างระหว่าง LA กับ LV ไม่มาก เลือดไหลช้า → เสียงทุ้มต่ำ ฟังด้วย **bell** ท่านอนตะแคงซ้าย

### เสียงฟู่อื่นที่ออกสอบ (คลังข้อสอบเก่า)
| ลักษณะ | คิดถึง |
|---|---|
| **Continuous "machinery" murmur ใต้กระดูกไหปลาร้าซ้าย** | **PDA** — aorta ความดันสูงกว่า pulmonary artery ทั้ง systole และ diastole |
| **S2 แยกกว้างคงที่ (fixed wide split)** + systolic ejection murmur ที่ LUSB + RA/RV โต | **ASD** — เสียงฟู่เกิดจากเลือดไหลผ่านลิ้น pulmonic มากขึ้น ไม่ใช่จากรูรั่ว |
| **Pansystolic murmur ใหม่ + thrill ที่ LLSB 3–5 วันหลัง MI** + pulmonary edema | **Ventricular septal rupture** (ถ้าที่ apex ไม่มี thrill → papillary muscle rupture) |
| **P2 ดัง + JVP สูง + ตับโต + ขาบวม ปอดใส** | **Pulmonary hypertension กับหัวใจขวาวาย** |

### เทคนิคข้างเตียง
- **หายใจเข้า** → เลือดกลับหัวใจขวามากขึ้น → **murmur ด้านขวาดังขึ้น** (Carvallo's sign ของ TR)
- **ยืน/Valsalva** (preload ลด) → murmur ส่วนใหญ่เบาลง **ยกเว้น HOCM และ MVP ที่ดังหรือยาวขึ้น**
- **นั่งยองหรือกำมือ** (afterload เพิ่ม) → MR AR ดังขึ้น · HOCM เบาลง
""",
    ["Ejection = AS/PS · Pansystolic = MR/TR · Blowing = AR/PR · Rumbling = MS/TS",
     "Continuous machinery murmur ใต้ไหปลาร้าซ้าย = PDA",
     "Fixed wide split S2 = ASD",
     "Pansystolic ใหม่ + thrill LLSB หลัง MI = VSR",
     "หายใจเข้า → murmur ข้างขวาดังขึ้น · ยืน → HOCM/MVP ดังขึ้น"],
    [mcq(N(2), "Which murmur is characteristically low-pitched, heard best with the bell at the apex in the left lateral decubitus position?",
         ["Aortic regurgitation", "Mitral stenosis", "Aortic stenosis", "Tricuspid regurgitation", "Pulmonic stenosis"], 1,
         "สไลด์: **diastolic rumbling murmur = MS (และ TS)** — ความดันระหว่าง LA กับ LV ต่างกันไม่มาก เลือดไหลช้าจึงเป็นเสียงความถี่ต่ำ ต้องใช้ **bell** และให้ผู้ป่วย **นอนตะแคงซ้าย** เพื่อให้ apex ชิดผนังอก\n\nAR เป็น **diastolic blowing** เสียงแหลม · AS/PS เป็น **systolic ejection** · TR เป็น **pansystolic**",
         "Rumbling + bell + ตะแคงซ้าย = MS", "Murmur pattern", R("Valvular heart disease — murmurs"), NLN + ["B7.1.2(1)"]),
    ], NLN + ["B7.1.2(1)", "B7.1.2(2)"])

# ───────────────────────────── 3
sec("cardio-vhd-03", "Mitral stenosis — กลไก อาการ และการตรวจร่างกาย",
    "เกือบทั้งหมดจากรูมาติก · ความดัน LA สูงไล่ย้อนไปปอดและหัวใจขวา · loud S1 · opening snap · diastolic rumble", 10,
"""### สาเหตุ
**ไข้รูมาติก — สาเหตุหลัก** (ในไทยเป็นผลระยะยาวที่พบบ่อยที่สุดของไข้รูมาติก) · พิการแต่กำเนิด · **mitral annular calcification** รุนแรง (ผู้สูงอายุ) · SLE, RA · **LA myxoma** · IE ที่มีก้อนใหญ่อุด

### กลไก — ความดันไล่ย้อนทีละขั้น
**ลิ้นตีบ → LA ความดันสูงและขยาย** → **AF** และลิ่มเลือด
→ **ความดันในหลอดเลือดดำปอดสูง** (เหนื่อย ไอเป็นเลือด pulmonary edema)
→ **pulmonary hypertension** → **RV โตและล้ม**
และเพราะเลือดเข้า LV ได้น้อย → **cardiac output ต่ำ**

**ทำไม AF หรือหัวใจเต้นเร็วทำให้ทรุดทันที** — เลือดต้องใช้เวลาไหลผ่านลิ้นที่ตีบ ช่วง diastole ที่สั้นลงทำให้ความดัน LA พุ่ง (ตั้งครรภ์ ไข้ ออกกำลังก็เช่นกัน)

### อาการ (สไลด์)
| อาการ | กลไก |
|---|---|
| **เหนื่อย** | ปอดคั่งน้ำ |
| **ไอเป็นเลือด** | หลอดเลือดดำหลอดลมที่โป่งพองแตก |
| **ลิ่มเลือดอุดตัน** | AF + LA ใหญ่ → stroke |
| **หัวใจล้มเหลว** | ทั้งซ้ายและขวา |
| **กลืนลำบาก** | LA โตกดหลอดอาหาร |
| **เสียงแหบ (Ortner's syndrome)** | LA หรือ pulmonary artery โตกด recurrent laryngeal nerve ซ้าย |

### ตรวจร่างกาย (สไลด์)
- **Malar flush** (mitral facies)
- **Loud S1** — ลิ้นที่แข็งปิดจากตำแหน่งที่เปิดกว้างสุดในจังหวะสุดท้ายของ diastole
- **Opening snap (OS)** — เสียงแหลมสั้นหลัง S2 เมื่อลิ้นที่แข็งเปิดสุดทาง · **ระยะ S2–OS ยิ่งสั้น = ยิ่งตีบมาก** (ความดัน LA สูงดันลิ้นเปิดเร็ว)
- **Low-pitched diastolic rumbling murmur** ที่ apex
- ถ้ามี PH: **loud P2, RV heave** · **TR** pansystolic ที่ LLSB ดังขึ้นตอนหายใจเข้า (**Carvallo's sign**) · **PR** diastolic blowing ที่ LUSB (**Graham Steell murmur**)
- RHD มักเป็นหลายลิ้น — มี AS AR TS ร่วมได้
""",
    ["MS: สาเหตุหลัก = ไข้รูมาติก (ผลระยะยาวที่พบบ่อยที่สุดในไทย)",
     "LA สูง → AF/ลิ่มเลือด → ปอดคั่ง → PH → RV ล้ม",
     "Loud S1 · opening snap · diastolic rumble · S2–OS สั้น = ตีบมาก",
     "Ortner's syndrome = เสียงแหบจากกด recurrent laryngeal nerve",
     "Carvallo's sign (TR) · Graham Steell (PR) เมื่อมี PH"],
    [mcq(N(3), "In mitral stenosis, which finding indicates more severe stenosis?",
         ["A softer first heart sound", "A shorter interval between S2 and the opening snap", "A longer interval between S2 and the opening snap",
          "Absence of atrial fibrillation", "A shorter diastolic rumble"], 1,
         "ยิ่งตีบมาก **ความดัน LA ยิ่งสูง** → ลิ้นถูกดันให้เปิดเร็วขึ้นหลังลิ้น aortic ปิด → **ระยะ S2–OS สั้นลง**\n\nเช่นเดียวกัน **diastolic rumble ยาวขึ้น** (ต้องใช้เวลาไหลผ่านนานขึ้น) · S1 จะเบาลงเมื่อลิ้นแข็งและมีหินปูนมากจนขยับไม่ได้ (ระยะท้าย) ไม่ใช่สัญญาณว่าโรคเบา",
         "S2–OS สั้น + rumble ยาว = MS รุนแรง", "MS severity at bedside", R("Mitral stenosis — physical findings"), NLN + ["B7.1.2(1)"]),
     mcq(N(4), "A 38-year-old woman with rheumatic mitral stenosis develops hoarseness. What is the mechanism?",
         ["Laryngeal oedema from heart failure", "Compression of the left recurrent laryngeal nerve by an enlarged left atrium or pulmonary artery (Ortner's syndrome)",
          "Vocal cord embolism", "Side effect of digoxin", "Rheumatic involvement of the larynx"], 1,
         "สไลด์อาการของ MS: **hoarseness = Ortner's syndrome** — **LA หรือ pulmonary artery ที่โตกด recurrent laryngeal nerve ซ้าย** ซึ่งอ้อมใต้ aortic arch\n\nอาการจากการกดอื่น: **กลืนลำบาก** (LA กดหลอดอาหาร — เห็นใน barium swallow) · CXR: carina กว้าง double contour",
         "เสียงแหบใน MS = Ortner's syndrome", "Ortner's syndrome", R("Mitral stenosis — clinical manifestations")),
    ], NLN + ["2.1.34", "2.1.33", "B7.1.2(1)"])

# ───────────────────────────── 4
sec("cardio-vhd-04", "Mitral stenosis — การตรวจ ความรุนแรง และการรักษา (อัปเดต ESC/EACTS 2025)",
    "Echo วัด MVA · MVA ≤ 1.5 cm² = มีนัยสำคัญ · PMBC เป็นหลัก · AF ใน MS ใช้ warfarin ไม่ใช้ NOAC", 11,
"""### การตรวจ (สไลด์)
| การตรวจ | สิ่งที่พบ |
|---|---|
| **ECG** | **LAE (P mitrale)** · **RVH** · **RAD** · **AF** |
| **CXR** | **LA และ LAA โต** — **carina กว้าง · double contour · LAA โป่ง** · หลอดอาหารถูกกด · PA RV RA โต (เมื่อมี PH) · **Kerley B lines** |
| **Echocardiography (TTE)** | ยืนยัน กลไก ความรุนแรง และ **ความเหมาะสมกับการขยายลิ้นด้วยบอลลูน (PMBC/PMBV)** · หาลิ่มเลือดใน LA ด้วย **TEE** ก่อนทำหัตถการ |

### ความรุนแรง
| | ACC/AHA 2020 (แผนภูมิในสไลด์) | **ESC/EACTS 2025** |
|---|---|---|
| ตีบมาก | **MVA ≤ 1.5 cm²** (T½ ≥ 150 ms) | **MVA ≤ 1.5 cm² = clinically significant MS** |
| ตีบรุนแรงมาก | **MVA ≤ 1.0 cm²** (T½ ≥ 220 ms) | — |
| Progressive | MVA > 1.5 cm² | — |
mean gradient ช่วยประเมินแต่ขึ้นกับอัตราการเต้นของหัวใจ จึงใช้คู่กับ MVA เสมอ

### การรักษาด้วยยา (สไลด์)
- **ป้องกันไข้รูมาติกซ้ำ (secondary prophylaxis)** — หัวข้อ 12
- **หัวใจล้มเหลว** — จำกัดเกลือ **ยาขับปัสสาวะ**
- **คุมอัตราการเต้นใน AF** — **β-blocker, CCB, digoxin** (ยืด diastole ให้เลือดไหลผ่านลิ้นได้)
- **ยาต้านการแข็งตัว** — **warfarin เมื่อมี AF หรือเคยมีลิ่มเลือดอุดตัน**

**อัปเดตสำคัญ — ห้ามใช้ NOAC ใน rheumatic MS ที่มี AF**
การศึกษา **INVICTUS (NEJM 2022)** ในผู้ป่วย AF จากโรคหัวใจรูมาติก พบว่า **rivaroxaban มีเหตุการณ์และการตายมากกว่า VKA** → ESC/EACTS 2025 และ ACC/AHA ให้ใช้ **VKA (warfarin เป้า INR 2–3)** ใน moderate–severe rheumatic MS (สอดคล้องกับคาบ AF)

### การรักษาด้วยหัตถการ
**หลักใหญ่ในสไลด์** — ทำเมื่อ **ตีบ/รั่วรุนแรง ร่วมกับมีอาการ** หรือ **ไม่มีอาการแต่มีปัจจัยพยากรณ์ไม่ดี**

**Percutaneous mitral balloon commissurotomy (PMBC/PMBV)** — ใช้บอลลูนแยก commissure ที่ติดกัน
เงื่อนไขที่เหมาะ: **รูปร่างลิ้นเหมาะ (ลิ้นยังยืดหยุ่น หินปูนน้อย) · ไม่มีลิ่มเลือดใน LA · MR ไม่เกินเล็กน้อย**

| สถานการณ์ | คำแนะนำ |
|---|---|
| **มีอาการ + MS มีนัยสำคัญ + ลิ้นเหมาะ** | **PMBC (Class I)** |
| มีอาการ + ลิ้นไม่เหมาะ | **ผ่าตัดเปลี่ยนลิ้น (MVR)** · ถ้าความเสี่ยงผ่าตัดสูงและ NYHA III–IV อาจลอง PMBC |
| **ไม่มีอาการ + MS มีนัยสำคัญ + ลิ้นเหมาะ** | **PMBC ควรพิจารณา (IIa)** โดยเฉพาะเมื่อ **PASP > 50 mmHg** · เสี่ยงลิ่มเลือดสูง · AF ใหม่ · วางแผนตั้งครรภ์ |
| ลิ่มเลือดใน LA | ให้ยาต้านการแข็งตัวจนลิ่มหายก่อน หรือผ่าตัด |
""",
    ["ECG: P mitrale, RVH, AF · CXR: double contour, carina กว้าง, Kerley B",
     "MVA ≤ 1.5 cm² = MS มีนัยสำคัญ · ≤ 1.0 = รุนแรงมาก",
     "PMBC เมื่อลิ้นเหมาะ + ไม่มีลิ่มใน LA + MR ไม่เกินเล็กน้อย",
     "มีอาการ + ลิ้นเหมาะ → PMBC (I) · ไม่มีอาการแต่ PASP > 50 → พิจารณา PMBC",
     "Rheumatic MS + AF → warfarin เท่านั้น (INVICTUS: rivaroxaban แย่กว่า)"],
    [mcq(N(5), "A 35-year-old woman with symptomatic rheumatic mitral stenosis has MVA 1.1 cm², pliable non-calcified leaflets, only mild MR and no left atrial thrombus on TEE. What is the recommended intervention?",
         ["Mitral valve replacement", "Percutaneous mitral balloon commissurotomy", "Medical therapy alone indefinitely",
          "Transcatheter edge-to-edge repair", "Surgical annuloplasty"], 1,
         "มีอาการ + **MS มีนัยสำคัญ (MVA ≤ 1.5 cm²)** + **ลิ้นเหมาะ (ยืดหยุ่น หินปูนน้อย) ไม่มีลิ่มใน LA และ MR ไม่เกินเล็กน้อย** → **PMBC เป็น Class I** (ทั้งแผนภูมิ ACC/AHA ในสไลด์และ ESC/EACTS 2025)\n\nMVR สำหรับลิ้นที่ไม่เหมาะกับบอลลูน · TEER ใช้รักษา MR ไม่ใช่ MS",
         "MS มีอาการ + ลิ้นเหมาะ → PMBC", "Indication for PMBC", R("Rheumatic MS algorithm") + [ESC25], NLN + ["3.3.23"]),
     mcq(N(6), "A woman with moderate–severe rheumatic mitral stenosis develops atrial fibrillation. Which anticoagulant is recommended?",
         ["Rivaroxaban 20 mg daily", "Apixaban 5 mg twice daily", "Aspirin 81 mg daily", "Warfarin with target INR 2.0–3.0", "No anticoagulation if CHA2DS2-VASc is 0"], 3,
         "**Rheumatic MS + AF → VKA (warfarin INR 2–3) เสมอ** โดยไม่ต้องคิดคะแนน CHA₂DS₂-VASc เพราะความเสี่ยงลิ่มเลือดสูงมาก\n\nการศึกษา **INVICTUS (NEJM 2022)** พบว่า rivaroxaban ในผู้ป่วย AF จากโรคหัวใจรูมาติกมีเหตุการณ์หลอดเลือดและการตาย **มากกว่า** VKA → ESC/EACTS 2025 ให้ใช้ VKA · aspirin ไม่ป้องกัน stroke ใน AF",
         "Rheumatic MS + AF = warfarin ไม่ใช่ NOAC", "Anticoagulation in rheumatic MS", R("Mitral stenosis — treatment") + [ESC25, "INVICTUS, NEJM 2022"], NLN + ["2.3.9(1)", "B2.4(3)"]),
    ], NLN + ["3.3.23"], SRC + " · อัปเดตตาม ESC/EACTS 2025")


# ───────────────────────────── 5
sec("cardio-vhd-05", "Mitral regurgitation และ mitral valve prolapse",
    "Acute MR → pulmonary edema ทันที · chronic MR → LA/LV ขยายค่อยเป็นค่อยไป · primary กับ secondary รักษาต่างกัน", 10,
"""### สาเหตุ (สไลด์)
| **Acute** | **Chronic** |
|---|---|
| **Papillary muscle rupture หลัง MI** | **RHD** |
| อุบัติเหตุกระแทกหน้าอก | **Mitral valve prolapse (MVP)** |
| **Infective endocarditis** | พิการแต่กำเนิด (cleft mitral) |
| **Chordae ขาด** (acute-on-chronic ใน myxomatous) | **HOCM** · **DCM** |

### Primary กับ secondary MR — คำถามแรกที่ต้องตอบ
| | **Primary (degenerative/organic)** | **Secondary (functional)** |
|---|---|---|
| ปัญหาอยู่ที่ | **ตัวลิ้น** (RHD, MVP, IE) | **ห้องหัวใจ** — LV ขยาย (ischemic, DCM) หรือ LA/วงแหวนขยาย (AF) ดึงลิ้นให้ปิดไม่สนิท |
| รักษา | **แก้ลิ้น** — ผ่าตัดซ่อม (repair) ดีกว่าเปลี่ยน | **รักษาหัวใจก่อน** — GDMT, CRT, revascularization · แล้วจึงพิจารณาหัตถการ |

### Acute กับ chronic — ทำไมอาการต่างกันมาก
- **Acute** — LA ขนาดปกติ ยืดไม่ทัน → ความดันพุ่ง → **pulmonary edema และช็อกทันที** เสียงฟู่อาจสั้นและเบา (ความดันสองห้องเท่ากันเร็ว)
- **Chronic** — LA และ LV **ค่อย ๆ ขยายรับปริมาตร** → ไม่มีอาการนาน · เมื่อรุนแรงจึง **เหนื่อยง่าย หอบเมื่อออกแรง นอนราบไม่ได้** · ระวัง **LV เสื่อมเงียบ ๆ** ก่อนมีอาการ

### ตรวจร่างกาย chronic MR (สไลด์)
- **Apex ย้ายออกด้านข้าง** (LV ขยาย)
- **S1 เบาหรือหายไป** (ลิ้นปิดไม่สนิท)
- **Holosystolic murmur ที่ MVA กระจายไปรักแร้**
- ECG: LA/LV โต AF · CXR: LA LV โต อาจมีปอดคั่ง · **Echo: หาสาเหตุ วัดขนาดและการทำงานของ LV ประเมินว่าซ่อมได้ไหม**

### Mitral valve prolapse (สไลด์)
- **Mid/late systolic click + late systolic murmur** (เสียงแหลม)
- ลิ้นหนาแบบ **myxomatous** — ความผิดปกติของคอลลาเจน · พบร่วมกับ **ทรวงอกผิดรูปและ Marfan** · **หญิง > ชาย**
- ส่วนใหญ่ไม่มีอาการ หรือเจ็บหน้าอกไม่จำเพาะ ใจสั่น · บางรายเป็น MR รุนแรง
- **Maneuver** — **ยืน/Valsalva (LV เล็กลง) → click เร็วขึ้น murmur ยาวขึ้น** · **นั่งยอง (LV ใหญ่ขึ้น) → click ช้าลง murmur สั้นลง**
- **MR รุนแรงที่มีอาการ → ผ่าตัดซ่อมลิ้น (MV repair)**
""",
    ["Acute MR (papillary rupture, IE, chordae) → pulmonary edema ทันที",
     "Primary MR = ลิ้นเสีย → ซ่อมลิ้น · secondary = หัวใจขยาย → GDMT/CRT ก่อน",
     "Chronic MR: apex ย้ายด้านข้าง · S1 เบา · holosystolic ที่ apex กระจายไปรักแร้",
     "MVP: mid-systolic click + late systolic murmur · ยืน → click เร็ว murmur ยาว"],
    [mcq(N(7), "Three days after an inferior STEMI, a patient suddenly develops severe pulmonary oedema and hypotension. A new, soft, short apical systolic murmur is heard without a thrill. What is the most likely cause?",
         ["Ventricular septal rupture", "Papillary muscle rupture causing acute mitral regurgitation", "Acute aortic regurgitation", "Pericardial tamponade", "Pulmonary embolism"], 1,
         "**Acute MR จาก papillary muscle rupture** (มักเป็น posteromedial papillary muscle ซึ่งมีเลือดเลี้ยงเส้นเดียวจาก RCA → พบหลัง inferior MI) — LA ขนาดปกติรับปริมาตรไม่ทัน → **pulmonary edema และช็อกทันที** · เสียงฟู่ **อาจเบาและสั้น** เพราะความดัน LA สูงทันความดัน LV เร็ว\n\nแยกจาก **VSR**: pansystolic ดังพร้อม **thrill ที่ LLSB** · ทั้งสองต้องทำ echo ด่วนและผ่าตัด",
         "หลัง MI: murmur ที่ apex ไม่มี thrill + pulmonary edema = papillary rupture", "Acute MR after MI", R("Mitral regurgitation — acute"), NLN + ["2.2.1"]),
    ], NLN + ["B7.1.2(1)"])

# ───────────────────────────── 6
sec("cardio-vhd-06", "MR — เกณฑ์ความรุนแรงและเมื่อไรต้องผ่าตัด (อัปเดต ESC/EACTS 2025)",
    "Severe MR: VC ≥ 0.7 · RVol ≥ 60 · RF ≥ 50% · EROA ≥ 0.4 · ผ่าตัดก่อน LV เสีย: LVEF ≤ 60 หรือ LVESD ≥ 40", 9,
"""### เกณฑ์ MR รุนแรงทาง echo (สไลด์)
| ตัวแปร | Severe |
|---|---|
| **Vena contracta** | **≥ 0.7 ซม.** |
| **Regurgitant volume (RVol)** | **≥ 60 มล.** |
| **Regurgitant fraction (RF)** | **≥ 50%** |
| **EROA** | **≥ 0.4 ซม.²** (primary MR) |
| ร่วมกับ | LV และ LA ขยาย |

### Primary MR — เมื่อไรผ่าตัด
**หลักคิด** — LVEF ใน MR **สูงเกินจริง** (เลือดส่วนหนึ่งรั่วกลับเข้า LA ที่ความดันต่ำ) **LVEF 60% จึงถือว่าเริ่มเสื่อมแล้ว** ต้องผ่าตัดก่อน LV เสียถาวร

| สถานการณ์ | ACC/AHA 2020 (สไลด์) | **ESC/EACTS 2025** |
|---|---|---|
| **มีอาการ** | ผ่าตัด (I) | ผ่าตัด (I) — **ซ่อมลิ้นถ้าทำได้** |
| **ไม่มีอาการ + LV เริ่มเสื่อม** | **LVEF ≤ 60% หรือ LVESD ≥ 40 มม.** → ผ่าตัด (I) | เหมือนเดิม **+ เพิ่ม LVESD index ≥ 20 มม./ม.²** |
| **ไม่มีอาการ LV ยังดี** | ซ่อมได้ > 95% และเสี่ยงตาย < 1% → ซ่อม (IIa) · **AF ใหม่ หรือ PASP > 50** → (IIa) | **ซ่อมลิ้นแนะนำ (I) เมื่อมี ≥ 3 ข้อ: AF · PASP > 50 mmHg · LA volume index ≥ 60 มล./ม.² · secondary TR ปานกลางขึ้นไป** · น้อยกว่า 3 ข้อ → ควรพิจารณา (IIa) — ในศูนย์ที่ซ่อมได้ผลทนทาน |
| Progressive (ยังไม่รุนแรง) | ติดตามเป็นระยะ | ติดตามเป็นระยะ |
**ผู้สูงอายุ/เสี่ยงผ่าตัดสูง** — **TEER (transcatheter edge-to-edge repair, MitraClip)** เป็นทางเลือก

### Secondary MR
1. **รักษาหัวใจล้มเหลวเต็มที่ (GDMT)** · **CRT** ถ้าเข้าเกณฑ์ · **รักษาหลอดเลือดหัวใจ**
2. ยังมีอาการแม้ได้ GDMT เต็มที่ → **TEER** ในผู้ป่วยที่เลือกแล้ว (หลักฐาน COAPT) หรือผ่าตัดถ้าต้องผ่าตัดหัวใจอื่นอยู่แล้ว
""",
    ["Severe MR: VC ≥ 0.7 · RVol ≥ 60 · RF ≥ 50% · EROA ≥ 0.4",
     "ใน MR LVEF สูงเกินจริง → LVEF ≤ 60% = LV เริ่มเสื่อม",
     "ไม่มีอาการ: LVEF ≤ 60 หรือ LVESD ≥ 40 (หรือ LVESDi ≥ 20) → ผ่าตัด",
     "ESC 2025: AF · PASP > 50 · LAVi ≥ 60 · TR ≥ ปานกลาง — ≥ 3 ข้อ → ซ่อม (I)",
     "Secondary MR: GDMT/CRT ก่อน → TEER"],
    [mcq(N(8), "An asymptomatic 55-year-old man has severe primary mitral regurgitation from a flail posterior leaflet. LVEF is 58% and LVESD 42 mm. What is the recommended management?",
         ["Repeat echocardiography in 2 years", "Start ACE inhibitor and observe", "Mitral valve surgery (repair preferred)", "TEER as first-line regardless of surgical risk", "Wait until symptoms develop"], 2,
         "**Primary MR รุนแรงที่ไม่มีอาการแต่ LV เริ่มเสื่อม** — **LVEF ≤ 60% หรือ LVESD ≥ 40 มม.** (ESC/EACTS 2025 เพิ่ม LVESDi ≥ 20 มม./ม.²) → **ผ่าตัด (Class I) โดยซ่อมลิ้นถ้าทำได้**\n\nเหตุผล: ใน MR **LVEF สูงเกินจริง** การรอให้มีอาการหรือ LVEF ต่ำแบบปกติจะทำให้ LV เสียถาวร · ยาขยายหลอดเลือดไม่ได้ชะลอการผ่าตัดใน primary MR · TEER สำหรับผู้ที่เสี่ยงผ่าตัดสูง",
         "Primary MR ไม่มีอาการ + LVEF ≤ 60 หรือ LVESD ≥ 40 → ผ่าตัด", "Surgery timing in primary MR", R("Mitral regurgitation algorithm") + [ESC25], NLN + ["3.3.23"]),
    ], NLN + ["3.3.23"], SRC + " · อัปเดตตาม ESC/EACTS 2025")

# ───────────────────────────── 7
sec("cardio-vhd-07", "Aortic stenosis — อาการ ตรวจร่างกาย และการรักษา (อัปเดต ESC/EACTS 2025)",
    "Angina · syncope · HF · ESM ที่ RUSB ไป carotid · pulsus parvus et tardus · TAVI อายุ ≥ 70 ปี", 11,
"""### สาเหตุ (สไลด์)
**หินปูนเสื่อม (degenerative calcification)** — ผู้สูงอายุ · **ลิ้นสองแฉก (bicuspid)** หรือแฉกเดียวแต่กำเนิด — อายุน้อยกว่า · **รูมาติก** (มักมี MS ร่วม)

### อาการสามอย่าง — และความหมายต่อการพยากรณ์
| อาการ | กลไก |
|---|---|
| **Angina** | LV หนา ต้องการออกซิเจนมาก + ความดันในผนังสูงบีบหลอดเลือดใต้เยื่อหุ้ม |
| **Syncope เมื่อออกแรง** | กล้ามเนื้อหลอดเลือดขยาย แต่ cardiac output เพิ่มไม่ได้ผ่านลิ้นที่ตีบ |
| **Heart failure** | LV แข็งแล้วล้ม |
**เมื่อมีอาการแล้วการพยากรณ์แย่ลงทันที** โดยไม่ผ่าตัด — จึงเป็นข้อบ่งชี้หลักของการเปลี่ยนลิ้น

### ตรวจร่างกาย
- **Ejection systolic murmur ที่ช่องซี่โครงที่ 2 ขวา กระจายไปคอทั้งสองข้าง** (สไลด์) · ยิ่งรุนแรง **ยอดเสียงยิ่งช้า (late-peaking)**
- **Pulsus parvus et tardus** — ชีพจรเบาและขึ้นช้า · **pulse pressure แคบ** (ตรงข้ามกับ AR)
- **S2 เบาหรือเดี่ยว** (A2 หาย) · **LV heave** ยกค้าง
- ECG: **LVH with strain** · left axis deviation · CXR: หัวใจไม่ค่อยโต · **aorta ส่วนต้นขยาย** · หินปูนที่ลิ้น

### เกณฑ์ AS รุนแรง (echo)
**Vmax ≥ 4.0 ม./วินาที · mean gradient ≥ 40 mmHg · AVA ≤ 1.0 ซม.²**
ถ้า AVA เล็กแต่ gradient ต่ำ (low-flow low-gradient) → **dobutamine stress echo** หรือ **CT calcium score** เพื่อแยก AS จริงกับ pseudo-severe

### การรักษา — ESC/EACTS 2025
| สถานการณ์ | คำแนะนำ |
|---|---|
| **AS รุนแรง + มีอาการ** | **เปลี่ยนลิ้น (Class I)** |
| **ไม่มีอาการ + LVEF < 50%** ไม่มีสาเหตุอื่น | **เปลี่ยนลิ้น (Class I)** |
| ไม่มีอาการ + **LVEF < 55%** | ควรพิจารณา (IIa) |
| **ไม่มีอาการ + high-gradient AS + LVEF ปกติ + ความเสี่ยงหัตถการต่ำ** | **ใหม่ — แนวทาง 2025 สนับสนุนการเปลี่ยนลิ้นเร็วขึ้น** แทนการรอดูอาการ (หลักฐาน EARLY TAVR, AVATAR, EVOLVED) |

**เลือกวิธี (Heart Team)** — **TAVI สำหรับอายุ ≥ 70 ปี** (ลดจาก 75 ในแนวทางเดิม) ที่ทางเข้าหลอดเลือดเหมาะ · **SAVR สำหรับอายุ < 70 ปีที่ความเสี่ยงผ่าตัดต่ำ** · พิจารณาอายุขัยและแผนการรักษาตลอดชีวิตร่วมด้วย · ลิ้นสองแฉกที่ความเสี่ยงผ่าตัดสูงขึ้นอาจใช้ TAVI ได้ถ้ากายวิภาคเหมาะ

**ระหว่างรอ** (สไลด์) — **เลี่ยงกีฬาแข่งขันและภาวะขาดน้ำ** · ยาไม่ชะลอการตีบ · ระวังยาขยายหลอดเลือดแรง ๆ ที่ทำให้ความดันตก
""",
    ["AS: angina · syncope · HF — มีอาการแล้วพยากรณ์แย่ → เปลี่ยนลิ้น",
     "ESM RUSB → carotid · late-peaking · pulsus parvus et tardus · pulse pressure แคบ",
     "Severe AS: Vmax ≥ 4 · MG ≥ 40 · AVA ≤ 1.0",
     "ESC 2025: TAVI ≥ 70 ปี · SAVR < 70 ความเสี่ยงต่ำ",
     "ไม่มีอาการ: LVEF < 50 → I · < 55 → IIa · high-gradient ความเสี่ยงต่ำ → เปลี่ยนเร็วขึ้น"],
    [mcq(N(9), "A 78-year-old man has exertional syncope. A harsh late-peaking systolic murmur is heard at the right upper sternal border radiating to both carotids. Echo: Vmax 4.6 m/s, mean gradient 52 mmHg, AVA 0.7 cm², LVEF 60%. Transfemoral access is suitable. According to the 2025 ESC/EACTS guideline, what is the preferred treatment?",
         ["Medical therapy with a vasodilator", "Balloon aortic valvuloplasty as definitive therapy", "Transcatheter aortic valve implantation (TAVI)",
          "Watchful waiting until heart failure develops", "Surgical repair of the aortic valve"], 2,
         "**AS รุนแรง** (Vmax ≥ 4 · MG ≥ 40 · AVA ≤ 1.0) **ที่มีอาการ** (syncope เมื่อออกแรง) → **เปลี่ยนลิ้น (Class I)**\n\n**ESC/EACTS 2025 ลดเกณฑ์อายุของ TAVI จาก 75 เป็น 70 ปี** → ผู้ป่วย 78 ปีที่ทางเข้าหลอดเลือดเหมาะ → **TAVI** · SAVR สำหรับอายุ < 70 ที่ความเสี่ยงต่ำ\n\nยาไม่ชะลอโรค · balloon valvuloplasty ใช้เป็นสะพานชั่วคราวเท่านั้น",
         "AS รุนแรงมีอาการ อายุ ≥ 70 → TAVI (ESC 2025)", "AS intervention", R("Aortic stenosis") + [ESC25], NLN + ["2.1.5", "3.3.23"]),
    ], NLN + ["2.1.5", "3.3.23"], SRC + " · อัปเดตตาม ESC/EACTS 2025")

# ───────────────────────────── 8
sec("cardio-vhd-08", "Aortic regurgitation — ชีพจรกระแทก และเกณฑ์ผ่าตัดใหม่",
    "Diastolic blowing · ICS 3 ซ้าย = ลิ้น · ICS 2 ขวา = root · wide pulse pressure · ESC 2025 ใช้ค่า index", 10,
"""### สาเหตุ (สไลด์)
| **ที่ตัวลิ้น** | **ที่ราก aorta** |
|---|---|
| **รูมาติก** · ลิ้นสองแฉก · ลิ้นหย่อน · **IE** · อุบัติเหตุ · ซิฟิลิส · ankylosing spondylitis | **Marfan syndrome** · **aortic dissection** · ความดันสูง · aortitis |

### ตรวจร่างกาย
- **Diastolic blowing murmur (decrescendo เสียงแหลม)** — **ดังสุดที่ ICS 3 ซ้าย = โรคที่ลิ้น · ICS 2 ขวา = โรคที่ราก aorta** (สไลด์) · ฟังท่านั่งโน้มตัวไปข้างหน้า หายใจออกสุดแล้วกลั้น
- **LV heave · apex ย้ายลงล่างและออกด้านข้าง** (LV ขยายมาก)
- **Chronic severe AR — ชีพจรและความดันชีพจรกว้าง**: **water-hammer (Corrigan's pulse)** · **de Musset** (ศีรษะผงกตามจังหวะ) · **Quincke** (เส้นเลือดฝอยใต้เล็บเต้น) · **Müller** (ลิ้นไก่เต้น) · **Traube** (เสียง "pistol shot" ที่ femoral) · **Duroziez** (เสียงฟู่สองจังหวะเมื่อกด femoral)
**กลไก** — stroke volume ใหญ่มาก (รวมเลือดที่รั่วกลับ) ดันความดัน systolic สูง แล้วเลือดไหลกลับเข้า LV ทำให้ diastolic ตกต่ำ

### เกณฑ์ AR รุนแรง (สไลด์)
**Vena contracta > 0.6 ซม. · holodiastolic flow reversal ใน descending aorta · RVol ≥ 60 มล. · RF ≥ 50% · EROA ≥ 0.3 ซม.²** · LV ขยาย

### เมื่อไรผ่าตัด
| สถานการณ์ | ACC/AHA 2020 (สไลด์) | **ESC/EACTS 2025** |
|---|---|---|
| **มีอาการ** | AVR (I) | AVR (I) |
| ไม่มีอาการ + **LVEF < 50%** (2025: **≤ 50%**) | AVR (I) | AVR (I) |
| ไม่มีอาการ + **LVESD > 50 มม.** | AVR (IIa) | **LVESD > 50 มม. หรือ LVESDi > 25 มม./ม.²** → AVR |
| ไม่มีอาการ ความเสี่ยงผ่าตัดต่ำ | **LVEDD > 65 มม.** (IIb) | **ใหม่: อาจพิจารณาเมื่อ LVESDi > 22 มม./ม.² · LVESVi > 45 มล./ม.² · หรือ LVEF ≤ 55%** |
| ต้องผ่าตัดหัวใจอื่นอยู่แล้ว | AVR (I) | AVR (I) |
- **ESC 2025** — **TAVI อาจพิจารณาในผู้ป่วย AR ที่มีอาการแต่ผ่าตัดไม่ได้** และกายวิภาคเหมาะ
- **Acute AR** (IE, aortic dissection) → LV ปรับตัวไม่ทัน เกิด pulmonary edema/ช็อก → **ผ่าตัดด่วน** · ห้ามใส่ IABP
- **Marfan** — ผ่าตัดราก aorta ตามขนาด (ประมาณ ≥ 50 มม. หรือเล็กกว่านั้นถ้ามีปัจจัยเสี่ยง)
""",
    ["AR: diastolic blowing · ICS 3 ซ้าย = ลิ้น · ICS 2 ขวา = root",
     "Wide pulse pressure · water-hammer · Quincke · de Musset · Duroziez",
     "Severe AR: VC > 0.6 · holodiastolic reversal · RVol ≥ 60 · RF ≥ 50% · EROA ≥ 0.3",
     "ผ่าตัด: มีอาการ · LVEF ≤ 50 · LVESD > 50 หรือ LVESDi > 25",
     "ESC 2025: พิจารณาเร็วขึ้นถ้า LVESDi > 22 · LVESVi > 45 · LVEF ≤ 55 (เสี่ยงต่ำ)"],
    [mcq(N(10), "A diastolic blowing murmur of aortic regurgitation is heard loudest at the right second intercostal space rather than the left third intercostal space. What does this suggest?",
         ["Rheumatic valve disease", "Aortic root disease such as Marfan syndrome or dissection", "Coexisting mitral stenosis", "Pulmonary regurgitation", "A bicuspid aortic valve without root dilatation"], 1,
         "สไลด์: **diastolic blowing murmur ดังสุดที่ ICS 3 ซ้าย → โรคที่ตัวลิ้น · ICS 2 ขวา → โรคที่ราก aorta**\n\nราก aorta ที่ขยาย (Marfan, dissection, ความดันสูง, aortitis) ดันกระแสเลือดที่รั่วไปทางขวาของกระดูกอก · ต้องตรวจขนาดราก aorta ด้วย echo/CT เพราะการรักษาต่างกัน",
         "AR ดังที่ ICS 2 ขวา = root disease", "AR — valve vs root", R("Aortic regurgitation — clinical presentation"), NLN + ["B7.2.6-3(1)", "B7.1.2(1)"]),
     mcq(N(11), "An asymptomatic 46-year-old man has severe chronic aortic regurgitation. LVEF is 48% with no other cause. What is the recommended management?",
         ["Annual echocardiography only", "Vasodilator therapy to delay surgery", "Aortic valve replacement", "Wait for symptoms before any intervention", "Beta-blocker to reduce regurgitation"], 2,
         "AR รุนแรงที่ **ไม่มีอาการแต่ LVEF ≤ 50%** → **AVR (Class I)** ทั้ง ACC/AHA และ ESC/EACTS 2025 · LV เริ่มเสื่อมแล้ว รอต่อจะเสียถาวร\n\nยาขยายหลอดเลือดใช้ลดความดันในผู้ที่ความดันสูงหรือผ่าตัดไม่ได้ **ไม่ใช่ทางชะลอการผ่าตัด** · β-blocker ยืด diastole ทำให้รั่วมากขึ้น",
         "AR ไม่มีอาการ + LVEF ≤ 50% → AVR", "AR intervention", R("Aortic regurgitation algorithm") + [ESC25], NLN + ["3.3.23"]),
    ], NLN + ["3.3.23"], SRC + " · อัปเดตตาม ESC/EACTS 2025")

# ───────────────────────────── 9
sec("cardio-vhd-09", "ลิ้นหัวใจด้านขวา — tricuspid และ pulmonic",
    "ส่วนใหญ่เป็นผลตามมาจาก pulmonary hypertension · primary จาก RHD, IE, carcinoid, พิการแต่กำเนิด", 6,
"""### สาเหตุ (สไลด์)
| ลิ้น | Primary | Secondary |
|---|---|---|
| **Tricuspid regurgitation** | **RHD · IE (ผู้ใช้ยาเสพติดฉีด) · carcinoid · อุบัติเหตุ · papillary muscle บาดเจ็บ** | **Pulmonary hypertension** (พบบ่อยที่สุด) · RV/วงแหวนขยาย · AF |
| **Tricuspid stenosis** | **RHD · พิการแต่กำเนิด** | — |
| **Pulmonic regurgitation** | **RHD · พิการแต่กำเนิด** | **Pulmonary hypertension · pulmonary artery ขยายไม่ทราบสาเหตุ · Marfan** |
| **Pulmonic stenosis** | **พิการแต่กำเนิด · carcinoid** | — |

### อาการและอาการแสดงของ TR
- **JVP สูง มี v wave ใหญ่** · ตับโตและเต้น (pulsatile liver) · ท้องมาน ขาบวม
- **Pansystolic murmur ที่ LLSB ดังขึ้นเมื่อหายใจเข้า = Carvallo's sign** — หายใจเข้าดึงเลือดกลับหัวใจขวามากขึ้น

### การรักษา (ESC/EACTS 2025)
- **TR รุนแรงที่มีอาการ** → ยาขับปัสสาวะ รักษาสาเหตุ (PH, AF, หัวใจซ้าย)
- **ซ่อมลิ้น tricuspid ระหว่างผ่าตัดลิ้นด้านซ้าย** เมื่อ TR รุนแรง หรือ TR ปานกลางที่วงแหวนขยาย
- **Transcatheter tricuspid therapy (T-TEER หรือเปลี่ยนลิ้นผ่านสายสวน)** — เป็นทางเลือกใหม่สำหรับผู้ที่มีอาการและเสี่ยงผ่าตัดสูง
""",
    ["Secondary TR/PR จาก PH พบบ่อยที่สุด",
     "Carvallo's sign: TR ดังขึ้นตอนหายใจเข้า",
     "TS: RHD/พิการแต่กำเนิด · PS: พิการแต่กำเนิด/carcinoid",
     "ซ่อม TR พร้อมผ่าตัดลิ้นซ้าย · transcatheter ในผู้เสี่ยงสูง"],
    [mcq(N(12), "A pansystolic murmur at the lower left sternal border becomes louder during inspiration. Which lesion is most likely?",
         ["Mitral regurgitation", "Tricuspid regurgitation", "Aortic stenosis", "Ventricular septal defect", "Hypertrophic cardiomyopathy"], 1,
         "**Carvallo's sign** — murmur ของ **TR ดังขึ้นเมื่อหายใจเข้า** เพราะความดันในช่องอกลดลงดึงเลือดกลับเข้าหัวใจขวามากขึ้น\n\nMR ฟังที่ apex กระจายไปรักแร้และไม่เปลี่ยนตามการหายใจ · ใน MS ที่มี PH จะพบ TR นี้ร่วมได้ (สไลด์)",
         "ดังขึ้นตอนหายใจเข้า = murmur ของหัวใจขวา", "Carvallo's sign", R("Mitral stenosis — associated lesions"), NLN + ["B7.1.2(1)"]),
    ], NLN + ["B7.1.2(2)"])


# ───────────────────────────── 10
sec("cardio-vhd-10", "Acute rheumatic fever — กลไกและเกณฑ์ Jones",
    "หลังคออักเสบจาก GAS 2–4 สัปดาห์ · molecular mimicry · 2 major หรือ 1 major + 2 minor + หลักฐาน GAS · Jones 2015 แยกตามความเสี่ยงของประชากร", 11,
"""### กลไก (สไลด์)
**ภูมิคุ้มกันทำลายตัวเองหลังติดเชื้อ Group A Streptococcus (GAS)** ที่คอหรือ scarlet fever ที่ **รักษาไม่เพียงพอ**
แอนติบอดีและ T-cell ต่อ **M protein** ของเชื้อ **จับข้ามกับโปรตีนของร่างกาย (molecular mimicry)** — myosin และ laminin ในหัวใจ/ลิ้น · ข้อ · ปมประสาทฐานสมอง (chorea) · ผิวหนัง
- อาการเริ่ม **2–4 สัปดาห์หลังคออักเสบ** · พบมากที่สุดอายุ **5–15 ปี**
- **ผลระยะยาวที่สำคัญคือ rheumatic heart disease** — ลิ้น mitral เสียบ่อยที่สุด (ในไทย MS เป็นผลระยะยาวที่พบบ่อยที่สุด)

### เกณฑ์ Jones (สไลด์)
**2 major หรือ 1 major + 2 minor** ร่วมกับ **หลักฐานการติดเชื้อ GAS ก่อนหน้า**

| **Major** — จำว่า "ขอบ-ข้อ-คอ-คำ-คว" (สไลด์) | **Minor** |
|---|---|
| **Erythema marginatum** (ผื่นขอบชัด ตรงกลางซีด ไม่คัน) | **ไข้** |
| **Polyarthritis** (ข้อใหญ่ ย้ายที่ ตอบสนองต่อ aspirin ดีมาก) | **ปวดข้อ (arthralgia)** |
| **Sydenham's chorea** (St. Vitus' dance) | **PR interval ยาว** |
| **Carditis** | **ESR หรือ CRP สูง** |
| **Subcutaneous nodules** (ไม่เจ็บ บนปุ่มกระดูก) | |

**หลักฐาน GAS** — throat culture หรือ rapid antigen บวก · **ASO** หรือ **anti-DNase B** สูงหรือเพิ่มขึ้น

### Revised Jones 2015 (AHA) — ที่แนวทาง WHO 2024 ใช้
**แยกเกณฑ์ตามความเสี่ยงของประชากร** — ประเทศที่มี RHD ชุกปานกลาง–สูง (รวมพื้นที่ในไทย) ใช้เกณฑ์ที่หลวมกว่า
| | **ประชากรเสี่ยงต่ำ** | **ประชากรเสี่ยงปานกลาง–สูง** |
|---|---|---|
| Carditis | ทางคลินิก **หรือ subclinical (พบจาก echo)** | ทางคลินิก **หรือ subclinical** |
| อาการข้อที่นับเป็น major | **polyarthritis เท่านั้น** | **monoarthritis หรือ polyarthritis หรือ polyarthralgia** |
| ข้อที่นับเป็น minor | polyarthralgia | monoarthralgia |
| ไข้ (minor) | **≥ 38.5°C** | **≥ 38.0°C** |
| ESR/CRP (minor) | **ESR ≥ 60** และ/หรือ CRP ≥ 3.0 มก./ดล. | **ESR ≥ 30** และ/หรือ CRP ≥ 3.0 มก./ดล. |
| PR ยาว (minor) | นับได้ถ้าไม่ได้ใช้ carditis เป็น major | เหมือนกัน |
- **ครั้งแรก** — 2 major หรือ 1 major + 2 minor
- **กลับเป็นซ้ำ** — 2 major · 1 major + 2 minor · **หรือ 3 minor**
- **Echo จำเป็นในทุกราย** — จับ **subclinical carditis** ที่ฟังไม่ได้ยิน

### ข้อยกเว้นของ WHO 2002–2003 (สไลด์)
- เคยมี RHD แล้วกลับเป็นซ้ำ → **2 minor + หลักฐาน GAS** ก็พอ
- **Chorea เดี่ยว หรือ indolent carditis** → **ไม่ต้องมี major อื่นหรือหลักฐาน GAS** (เพราะเกิดช้าหลังติดเชื้อนานจนแอนติบอดีลดแล้ว)

### Carditis (สไลด์)
พบ **40–60%** · เป็น **pancarditis**
| ชั้น | อาการแสดง |
|---|---|
| **Endocarditis/valvulitis** | **apical pansystolic murmur (MR)** · **apical short mid-diastolic murmur = Carey Coombs** · **basal diastolic blowing (AR)** |
| **Myocarditis** | หัวใจโต · หัวใจล้มเหลว |
| **Pericarditis** | pericardial friction rub · น้ำในเยื่อหุ้มหัวใจ |
""",
    ["ARF: 2–4 สัปดาห์หลัง GAS pharyngitis · อายุ 5–15 ปี · molecular mimicry",
     "Major: erythema marginatum · polyarthritis · chorea · carditis · nodules (ขอบ-ข้อ-คอ-คำ-คว)",
     "Minor: ไข้ · ปวดข้อ · PR ยาว · ESR/CRP สูง + หลักฐาน GAS (ASO, anti-DNase B)",
     "Jones 2015: ประชากรเสี่ยงสูงนับ monoarthritis/polyarthralgia เป็น major · echo ทุกราย",
     "Chorea เดี่ยวหรือ indolent carditis ไม่ต้องมีหลักฐาน GAS"],
    [mcq(N(13), "A 10-year-old girl from a high-RHD-prevalence area has fever 38.2°C and arthritis of the right knee only, 3 weeks after a sore throat. ESR is 45 mm/h and ASO titre is raised. Echocardiography shows pathological mitral regurgitation not audible on auscultation. Under the 2015 revised Jones criteria, how should she be classified?",
         ["Does not meet criteria because arthritis is monoarticular", "Acute rheumatic fever: two major (subclinical carditis, monoarthritis) plus GAS evidence",
          "Post-streptococcal reactive arthritis only", "Infective endocarditis", "Juvenile idiopathic arthritis"], 1,
         "**Revised Jones 2015** ในประชากร **เสี่ยงปานกลาง–สูง**: **monoarthritis นับเป็น major** และ **subclinical carditis จาก echo ก็นับเป็น carditis (major)** → **2 major + หลักฐาน GAS (ASO สูง) = ARF**\n\nนอกจากนี้ยังมี minor ครบ: **ไข้ ≥ 38.0** และ **ESR ≥ 30** · ในประชากรเสี่ยงต่ำ monoarthritis จะไม่นับเป็น major — จึงต้องรู้ว่าผู้ป่วยมาจากพื้นที่แบบไหน",
         "Jones 2015 ประชากรเสี่ยงสูง: monoarthritis + subclinical carditis นับเป็น major", "Revised Jones criteria", R("Revised Jones criteria ACC/AHA 2015") + ["Gewitz MH, et al. Circulation 2015 · WHO 2024"], ARF + ["2.1.27", "3.3.23"]),
     mcq(N(14), "Which finding is a MINOR rather than a major Jones criterion?",
         ["Sydenham's chorea", "Erythema marginatum", "Prolonged PR interval", "Subcutaneous nodules", "Carditis"], 2,
         "**Minor criteria** (สไลด์): **ไข้ · ปวดข้อ · PR interval ยาว · ESR/CRP สูง**\n\n**Major** จำว่า **ขอบ-ข้อ-คอ-คำ-คว**: erythema marginatum · polyarthritis · chorea · carditis · subcutaneous nodules\n\nPR ยาวไม่ใช่ carditis — เป็นการนำไฟฟ้าช้าจากการอักเสบ ไม่ทำนาย RHD จึงนับเป็นเพียง minor",
         "PR ยาว = minor ไม่ใช่ carditis", "Jones minor criteria", R("Minor criteria"), ARF),
    ], ARF + ["2.1.27", "2.1.50"], SRC + " · อัปเดตตาม revised Jones 2015 และ WHO 2024")

# ───────────────────────────── 11
sec("cardio-vhd-11", "รักษาไข้รูมาติก และป้องกันการกลับเป็นซ้ำ (อัปเดต WHO 2024)",
    "กำจัด GAS · ลดการอักเสบ · benzathine penicillin G ทุก 4 สัปดาห์ · ระยะเวลาตามความรุนแรงของหัวใจ", 10,
"""### สามเป้าหมาย (สไลด์)
1. **บรรเทาอาการ**  2. **กำจัด Group A Streptococcus**  3. **ป้องกันการติดเชื้อซ้ำ**

### รักษาคออักเสบจาก GAS (primary prevention)
| ยา | ขนาด |
|---|---|
| **Benzathine penicillin G (BPG)** | **1.2 ล้านยูนิต IM ครั้งเดียว** · **600,000 ยูนิตถ้า < 27 กก.** |
| **Penicillin V หรือ amoxicillin** | เด็ก 250 มก. วันละ 2 ครั้ง · ผู้ใหญ่ 500 มก. วันละ 2 ครั้ง **นาน 10 วัน** · **WHO 2024: amoxicillin 50 มก./กก./วัน (ไม่เกิน 1,000 มก.) วันละครั้งได้ ครบ 10 วัน** |
| แพ้ penicillin | cephalosporin หรือ macrolide **ครบ 10 วัน** |
**ต้องครบ 10 วัน** — ยาสั้นกว่านั้นกำจัดเชื้อไม่หมดและไม่ป้องกันไข้รูมาติก

### ลดการอักเสบ (สไลด์)
| อาการ | ยา |
|---|---|
| **Arthritis** | **Salicylate 75 มก./กก./วัน 4–6 สัปดาห์** |
| **Carditis ไม่มีหัวใจโต** | **Salicylate 90–100 มก./กก./วัน 4–8 สัปดาห์** |
| **Carditis มีหัวใจโตหรือ CHF** | **Prednisolone 2 มก./กก./วัน × 2 สัปดาห์** แล้วต่อ **salicylate 90–100 มก./กก./วัน × 6 สัปดาห์** |
- **WHO 2024** — ยาต้านการอักเสบ (aspirin, NSAID เช่น naproxen, steroid, IVIG) **ใช้บรรเทาอาการได้** แต่ **ไม่มีหลักฐานว่าป้องกันการเกิด RHD** จึงไม่แนะนำทั้งให้และไม่ให้เพื่อจุดประสงค์นั้น
- **Chorea** — ส่วนใหญ่หายเอง · รุนแรงใช้ยา (เช่น carbamazepine หรือ valproate)
- **หัวใจล้มเหลว** — รักษามาตรฐาน (ยาขับปัสสาวะ) · พักตามอาการ

### ป้องกันการกลับเป็นซ้ำ (secondary prophylaxis)
**การกลับเป็นซ้ำแต่ละครั้งทำลายลิ้นเพิ่ม** — นี่คือมาตรการที่ป้องกัน RHD ได้ดีที่สุด
| ยา | ขนาด |
|---|---|
| **BPG** (ทางเลือกแรก) | **1.2 ล้านยูนิต IM ทุก 3–4 สัปดาห์** (สไลด์) · **WHO 2024: ทุก 4 สัปดาห์ ดีกว่ายากิน** · **ผสมยาชาเฉพาะที่ (lidocaine) ลดความเจ็บได้** |
| Penicillin V | 250 มก. กิน วันละ 2 ครั้ง |
| Erythromycin (แพ้ penicillin) | 250 มก. กิน วันละ 2 ครั้ง |

### ระยะเวลา (สไลด์ — AHA)
| กลุ่ม | ระยะเวลา |
|---|---|
| **มี carditis และยังมีโรคลิ้นหัวใจหลงเหลือ** | **อย่างน้อย 10 ปีหลังครั้งสุดท้าย และอย่างน้อยถึงอายุ 40 ปี** บางรายตลอดชีวิต |
| **มี carditis แต่ไม่มีโรคลิ้นหลงเหลือ** | **10 ปี หรือถึงอายุ 21 ปี** (แล้วแต่อันไหนนานกว่า) |
| **ไม่มี carditis** | **5 ปี หรือถึงอายุ 21 ปี** (แล้วแต่อันไหนนานกว่า) |
**WHO 2024 เพิ่ม** — เด็กและวัยรุ่นที่ **ตรวจคัดกรองด้วย echo แล้วพบ RHD ขั้นต่ำ** ควรได้ยาป้องกันเพื่อชะลอการดำเนินโรค · และต้องมีระบบช่วยให้ผู้ป่วยมารับยาสม่ำเสมอ
""",
    ["คออักเสบ GAS: BPG 1.2 MU IM ครั้งเดียว (600,000 ถ้า < 27 กก.) หรือ penicillin/amoxicillin 10 วัน",
     "Arthritis: salicylate 75 มก./กก./วัน · carditis + หัวใจโต/CHF: prednisolone 2 มก./กก./วัน",
     "Secondary prophylaxis: BPG 1.2 MU ทุก 4 สัปดาห์ (WHO 2024) ดีกว่ายากิน",
     "Carditis + ลิ้นเสีย: ≥ 10 ปี และถึงอายุ ≥ 40 · carditis ไม่มีลิ้นเสีย: 10 ปี/21 ปี · ไม่มี carditis: 5 ปี/21 ปี",
     "ยาต้านการอักเสบช่วยอาการ แต่ไม่ป้องกัน RHD"],
    [mcq(N(15), "A 16-year-old had acute rheumatic fever with carditis and now has residual moderate mitral regurgitation. How long should secondary prophylaxis continue?",
         ["5 years or until age 21, whichever is longer", "10 years or until age 21, whichever is longer",
          "At least 10 years after the last episode and at least until age 40, sometimes lifelong", "Only until the ESR normalises", "1 year"], 2,
         "ตารางในสไลด์: **ไข้รูมาติกที่มี carditis และยังมีโรคลิ้นหัวใจหลงเหลือ → อย่างน้อย 10 ปีหลังครั้งสุดท้าย และอย่างน้อยถึงอายุ 40 ปี บางรายตลอดชีวิต**\n\nCarditis ที่ไม่มีลิ้นเสียหลงเหลือ → 10 ปีหรือถึงอายุ 21 · ไม่มี carditis → 5 ปีหรือถึงอายุ 21\n\nยาที่ใช้: **BPG 1.2 ล้านยูนิต IM ทุก 4 สัปดาห์** (WHO 2024)",
         "Carditis + ลิ้นเสีย → ≥ 10 ปี และถึงอายุ ≥ 40", "Duration of secondary prophylaxis", R("Duration of secondary rheumatic fever prophylaxis") + ["WHO 2024"], ARF),
     mcq(N(16), "According to the WHO 2024 guideline, what is the preferred agent for secondary prophylaxis of rheumatic fever?",
         ["Oral penicillin V twice daily", "Intramuscular benzathine benzylpenicillin every 4 weeks", "Oral azithromycin weekly", "Aspirin long term", "Oral amoxicillin only during sore throat episodes"], 1,
         "WHO 2024: **benzathine benzylpenicillin IM ทุก 4 สัปดาห์** เป็นยาป้องกันที่ได้ผลดีที่สุดและ **ดีกว่ายากิน** · อาจผสมยาชาเฉพาะที่เพื่อลดความเจ็บและช่วยให้ผู้ป่วยมารับยาต่อเนื่อง\n\nยากิน (penicillin V, erythromycin) เป็นทางเลือกเมื่อฉีดไม่ได้ · aspirin เป็นยาลดการอักเสบ ไม่ได้ป้องกันการติดเชื้อซ้ำ",
         "Secondary prophylaxis: BPG IM ทุก 4 สัปดาห์", "WHO 2024 secondary prophylaxis", ["WHO guideline on the prevention and diagnosis of RF and RHD, 2024"] + R("Secondary prophylaxis"), ARF + ["B6.2.2(3)"]),
    ], ARF + ["B6.2.2(3)"], SRC + " · อัปเดตตาม WHO 2024")

# ───────────────────────────── 12
sec("cardio-vhd-12", "Infective endocarditis — สงสัยเมื่อไร และวินิจฉัยตาม Duke-ISCVID 2023",
    "ไข้ + murmur = IE จนกว่าจะพิสูจน์ว่าไม่ใช่ · เพาะเชื้อ 3 ชุดก่อนให้ยา · echo · เกณฑ์ใหม่เพิ่ม CT/PET-CT และผลผ่าตัด", 10,
"""สไลด์ของคาบนี้ไม่มีหัวข้อ IE แต่ **คลังข้อสอบ Ward Drill คาบ 27 มี IE 7 ข้อ** และ IE เป็นภาวะแทรกซ้อนสำคัญของโรคลิ้นหัวใจรูมาติก — เนื้อหาส่วนนี้อิง **ESC 2023 Guidelines for the management of endocarditis** และ **2023 Duke-ISCVID criteria**

### เมื่อไรต้องคิดถึง IE
**ไข้ + เสียงฟู่ (โดยเฉพาะใหม่) = IE จนกว่าจะพิสูจน์ว่าไม่ใช่** — ยิ่งมี **ลิ้นหัวใจผิดปกติ (RHD) ลิ้นเทียม เคยเป็น IE ใช้ยาฉีด หรือมีอุปกรณ์ในหัวใจ**
อาการกึ่งเฉียบพลัน (viridans streptococci) — ไข้เรื้อรังเป็นสัปดาห์ถึงเดือน อ่อนเพลีย น้ำหนักลด ปวดหลัง ม้ามโต ซีด

| อาการแสดง | กลไก |
|---|---|
| **Splinter hemorrhage · conjunctival hemorrhage** | ลิ่มเชื้อเล็ก ๆ/หลอดเลือดอักเสบ |
| **Janeway lesion** (ไม่เจ็บ ฝ่ามือฝ่าเท้า) | emboli |
| **Osler node** (เจ็บ ปลายนิ้ว) | immune complex |
| **Roth spot** — **เลือดออกที่จอตามีจุดซีดตรงกลาง** | immune complex |
| Glomerulonephritis · RF บวก | immune complex |
| Stroke · ไตหรือม้ามตาย · mycotic aneurysm | ก้อนเชื้อหลุด |

### การตรวจ
1. **เพาะเชื้อจากเลือดอย่างน้อย 3 ชุด จากตำแหน่งต่างกัน ก่อนให้ยาปฏิชีวนะ** — สำคัญที่สุด
2. **Echocardiography** — TTE ก่อน · **TEE** เมื่อสงสัยมากแต่ TTE ไม่ชัด ลิ้นเทียม หรือหาฝี

### 2023 Duke-ISCVID criteria (สรุป)
| **Major** | **Minor** |
|---|---|
| **จุลชีววิทยา** — เชื้อทั่วไปของ IE ขึ้น ≥ 2 ชุด (viridans strep, S. gallolyticus, HACEK, S. aureus, **E. faecalis** และอื่น ๆ ที่เพิ่มเข้ามา) · PCR/sequencing จากลิ้น · Coxiella | **มีปัจจัยเสี่ยง** (ลิ้นผิดปกติ ลิ้นเทียม ยาฉีด เคยเป็น IE) |
| **ภาพถ่าย** — echo พบ vegetation ฝี ลิ้นทะลุ ลิ้นเทียมหลวม · **ใหม่: cardiac CT และ FDG-PET/CT** | **ไข้ ≥ 38.0°C** |
| **ใหม่: พบหลักฐานจากการผ่าตัดโดยตรง** (major clinical) | **ปรากฏการณ์หลอดเลือด** — emboli (รวมที่พบจากภาพถ่ายโดยไม่มีอาการ) · Janeway · เลือดออกในสมอง · mycotic aneurysm · conjunctival hemorrhage |
| | **ปรากฏการณ์ภูมิคุ้มกัน** — Osler · Roth · GN · RF บวก |
| | จุลชีววิทยาที่ไม่ถึงเกณฑ์ major |
**Definite IE** = **2 major · หรือ 1 major + 3 minor · หรือ 5 minor** · เกณฑ์ใหม่ไวกว่าเกณฑ์ modified Duke เดิม
""",
    ["ไข้ + murmur = IE จนกว่าจะพิสูจน์ว่าไม่ใช่",
     "เพาะเชื้อ ≥ 3 ชุดต่างตำแหน่งก่อนให้ยา · echo (TEE ถ้าจำเป็น)",
     "Roth spot = เลือดออกที่จอตาจุดซีดกลาง · Osler เจ็บ · Janeway ไม่เจ็บ",
     "Duke-ISCVID 2023: เพิ่ม CT/PET-CT · ผลผ่าตัดเป็น major · E. faecalis เป็นเชื้อทั่วไป",
     "Definite: 2 major · 1 major + 3 minor · 5 minor"],
    [mcq(N(17), "A 42-year-old woman with known rheumatic mitral regurgitation has 4 weeks of fever, weight loss and new splenomegaly. What is the single most important first step before starting antibiotics?",
         ["Start empirical ceftriaxone immediately and then culture", "Obtain at least three sets of blood cultures from separate venepunctures",
          "Order a CT abdomen", "Check ASO titre", "Perform bone marrow biopsy"], 1,
         "**ไข้เรื้อรัง + ลิ้นหัวใจผิดปกติ + ม้ามโต = สงสัย IE** → ขั้นแรกคือ **เพาะเชื้อจากเลือดอย่างน้อย 3 ชุดจากตำแหน่งต่างกันก่อนให้ยาปฏิชีวนะ** · การให้ยาก่อนทำให้เพาะเชื้อไม่ขึ้นและเลือกยาไม่ได้\n\nในผู้ป่วยที่อาการไม่รุนแรง (กึ่งเฉียบพลัน) รอผลเพาะเชื้อได้ · ถ้าอาการหนักให้เก็บเชื้อให้ครบอย่างรวดเร็วแล้วเริ่มยาทันที",
         "สงสัย IE → blood culture ≥ 3 ชุดก่อนยา", "IE diagnosis", ["ESC 2023 endocarditis guidelines", "2023 Duke-ISCVID criteria"], IE + ["2.1.1"]),
    ], IE + ["2.1.1", "3.3.23"], "ESC 2023 Endocarditis guidelines · 2023 Duke-ISCVID criteria (ไม่อยู่ในสไลด์ — เพิ่มตามคลังข้อสอบ)")

# ───────────────────────────── 13
sec("cardio-vhd-13", "Infective endocarditis — รักษา ผ่าตัด และป้องกัน (ESC 2023)",
    "Viridans strep: penicillin G/ceftriaxone 4 สัปดาห์ หรือ 2 สัปดาห์ + gentamicin · oral step-down · ผ่าตัดเมื่อ HF ติดเชื้อคุมไม่ได้ หรือป้องกัน emboli", 9,
"""### ยาปฏิชีวนะ — ตัวอย่างที่ออกสอบ
**Viridans streptococci ที่ไวต่อ penicillin บนลิ้นธรรมชาติ**
- **Penicillin G หรือ ceftriaxone ทางหลอดเลือด 4 สัปดาห์**
- หรือ **2 สัปดาห์ร่วมกับ gentamicin** ในรายที่ไม่มีภาวะแทรกซ้อนและไตปกติ
ลิ้นเทียม → **6 สัปดาห์** · S. aureus และเชื้ออื่นใช้สูตรต่างกัน

### Oral step-down (ใหม่ใน ESC 2023)
ผู้ป่วย **IE ด้านซ้ายที่อาการคงที่** จาก **streptococci, E. faecalis, S. aureus หรือ CoNS** ที่ได้ยาทางหลอดเลือดแล้ว **≥ 10 วัน** (หรือ ≥ 7 วันหลังผ่าตัด) ไม่มีไข้ ไม่มีฝี และ TEE ไม่มีปัญหา → **เปลี่ยนเป็นยากินจนครบได้ (IIa)** — หลักฐานจาก **POET trial**

### ผ่าตัดเมื่อไร (สามเหตุผลหลัก)
| เหตุผล | ตัวอย่าง |
|---|---|
| **หัวใจล้มเหลว** | ลิ้นรั่วหรือทะลุจนเกิด pulmonary edema/ช็อก → ผ่าตัดด่วน |
| **ติดเชื้อคุมไม่ได้** | **ฝี** · เชื้อในเลือดไม่หายแม้ได้ยาเหมาะสม · เชื้อรา หรือเชื้อดื้อยา |
| **ป้องกัน emboli** | **vegetation ≥ 10 มม. ร่วมกับเคยมี emboli** · vegetation ใหญ่มาก |

### ป้องกันก่อนทำฟัน (ESC 2023 / AHA)
**ให้เฉพาะกลุ่มเสี่ยงสูง** ที่ทำ **หัตถการฟันที่มีการจับเหงือกหรือรอบปลายรากฟัน**
- กลุ่มเสี่ยงสูง: **ลิ้นหัวใจเทียม (รวม TAVI และวัสดุซ่อมลิ้น)** · **เคยเป็น IE** · โรคหัวใจพิการแต่กำเนิดชนิดเขียวที่ยังไม่แก้ไข หรือแก้ด้วยวัสดุเทียม · อุปกรณ์ช่วยการทำงานของหัวใจ (VAD)
- ยา: **amoxicillin 2 ก. กิน 30–60 นาทีก่อนทำ**
- **แพ้ penicillin: azithromycin หรือ clarithromycin 500 มก. หรือ doxycycline 100 มก.**
- **อัปเดต** — **clindamycin ไม่แนะนำแล้ว** (AHA 2021 และ ESC 2023) เพราะเสี่ยง C. difficile และแพ้ยารุนแรง ทั้งที่ข้อสอบเก่าบางข้อยังใช้เป็นคำตอบ
- **RHD ที่ไม่มีลิ้นเทียมหรือไม่เคยเป็น IE ไม่ต้องให้ยาป้องกันเป็นกิจวัตร** — สุขภาพช่องปากที่ดีสำคัญกว่า
""",
    ["Viridans strep ลิ้นธรรมชาติ: penicillin G/ceftriaxone 4 สัปดาห์ หรือ 2 สัปดาห์ + gentamicin",
     "ESC 2023: oral step-down หลัง IV ≥ 10 วันในรายที่คงที่ (POET)",
     "ผ่าตัด: HF · ติดเชื้อคุมไม่ได้/ฝี · vegetation ≥ 10 มม. + emboli",
     "ป้องกันก่อนทำฟันเฉพาะเสี่ยงสูง: ลิ้นเทียม · เคยเป็น IE · CHD บางชนิด",
     "แพ้ penicillin: azithromycin/clarithromycin/doxycycline — clindamycin ไม่แนะนำแล้ว"],
    [mcq(N(18), "A patient with a mechanical mitral valve and a documented penicillin allergy (urticaria) is scheduled for a dental extraction. According to current AHA (2021) and ESC (2023) guidance, which prophylaxis is most appropriate?",
         ["No prophylaxis is needed", "Clindamycin 600 mg orally before the procedure", "Azithromycin 500 mg orally 30–60 minutes before the procedure",
          "Amoxicillin 2 g orally", "Vancomycin for 7 days after the procedure"], 2,
         "ลิ้นหัวใจเทียม = **กลุ่มเสี่ยงสูง** + ถอนฟัน (จับเหงือก) → **ต้องให้ยาป้องกัน** · แพ้ penicillin → **azithromycin หรือ clarithromycin 500 มก.** (หรือ doxycycline 100 มก.) **ครั้งเดียว 30–60 นาทีก่อนทำ**\n\n**Clindamycin ไม่แนะนำแล้ว** ตั้งแต่ AHA 2021 และ ESC 2023 เพราะเสี่ยง **C. difficile** และแพ้ยารุนแรงมากกว่าประโยชน์ — ข้อสอบเก่าบางข้อยังใช้ clindamycin เป็นคำตอบ ให้ตอบตามแนวทางใหม่ถ้ามีตัวเลือกให้\n\nAmoxicillin ห้ามในผู้ที่แพ้ penicillin",
         "แพ้ penicillin → azithromycin/clarithromycin/doxycycline (ไม่ใช่ clindamycin แล้ว)", "IE prophylaxis update", ["ESC 2023 endocarditis guidelines", "AHA Scientific Statement 2021: Prevention of viridans group streptococcal IE"], IE),
    ], IE, "ESC 2023 Endocarditis guidelines (ไม่อยู่ในสไลด์ — เพิ่มตามคลังข้อสอบ)")

# ───────────────────────────── MEQ (ใหม่) — ส่วน MEQ/OSCE ของคลังผูกท้ายสคริปต์
LECNAME = "Valvular heart disease and acute rheumatic fever (พ.ญ.ชนัญญา)"
MEQ = [{"id": "CAR-VHD-MEQ-01", "part": "MEQ", "lec": "27", "lecture": LECNAME,
 "topic": "Acute rheumatic fever with carditis — Jones criteria, treatment and secondary prophylaxis",
 "vignette": """เด็กชายไทยอายุ 11 ปี ภูมิลำเนาจังหวัดในภาคตะวันออกเฉียงเหนือ มาด้วยไข้และปวดข้อ 6 วัน
PI: 3 สัปดาห์ก่อนเจ็บคอ มีไข้ 2 วัน ซื้อยาลดไข้กินเอง ไม่ได้รับยาปฏิชีวนะ · 6 วันก่อนปวดบวมข้อเข่าขวา 2 วันต่อมาย้ายไปข้อเท้าซ้ายและข้อมือขวา · 2 วันก่อนเหนื่อยเวลาเดิน
PE: BT 38.6 C, PR 128/min, RR 26/min, BP 100/60 mmHg
ข้อมือขวาบวมแดงร้อน กดเจ็บมาก · ผื่นวงแหวนสีชมพูขอบชัดตรงกลางซีดที่ลำตัว ไม่คัน
Heart: apex ที่ ICS 6 แนว anterior axillary line · pansystolic murmur grade III/VI ที่ apex ไปรักแร้ · short mid-diastolic murmur ที่ apex
Lungs: fine crepitations ทั้งสองข้างล่าง · ตับโต 2 ซม.
Lab: CBC WBC 14,200 · ESR 92 mm/h · CRP 12 mg/dL · ASO 800 Todd units (สูง)
ECG: sinus tachycardia, PR 0.22 s · CXR: cardiomegaly, pulmonary congestion""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัย และแสดงเกณฑ์ที่ใช้ (4 คะแนน)",
   "a": """**Acute rheumatic fever with carditis (และหัวใจล้มเหลว)** — เกณฑ์ Jones
- **Major**: **carditis** (MR + Carey Coombs murmur + หัวใจโต + CHF) · **migratory polyarthritis** · **erythema marginatum**
- **Minor**: **ไข้** · **ESR/CRP สูง** · (PR ยาว — นับไม่ได้เพราะใช้ carditis เป็น major แล้ว)
- **หลักฐาน GAS**: **ASO สูง** + เจ็บคอ 3 สัปดาห์ก่อนที่ไม่ได้ยาปฏิชีวนะ
→ 3 major + minor + หลักฐาน GAS · ควรทำ **echocardiography** ประเมินลิ้นและ carditis"""},
  {"q": "2. จงอธิบายกลไกการเกิดโรค และบอกว่าเสียงฟู่ที่ apex ทั้งสองเสียงเกิดจากอะไร (3 คะแนน)",
   "a": """- **Molecular mimicry** — แอนติบอดี/T-cell ต่อ **M protein** ของ GAS จับข้ามกับโปรตีนในหัวใจ (myosin, ลิ้น) ข้อ ผิวหนัง → **pancarditis**
- **Pansystolic murmur ที่ apex → MR** จาก valvulitis (วงแหวนขยาย ลิ้นบวม)
- **Short mid-diastolic murmur ที่ apex → Carey Coombs murmur** — เลือดปริมาณมากไหลผ่านลิ้น mitral ที่อักเสบบวม (ไม่ใช่ MS ที่ตีบจริง)"""},
  {"q": "3. จงเขียนการรักษาในโรงพยาบาล (4 คะแนน)",
   "a": """- **กำจัด GAS**: **benzathine penicillin G 1.2 ล้านยูนิต IM** (น้ำหนัก ≥ 27 กก.) หรือ penicillin V/amoxicillin 10 วัน
- **Carditis ที่มีหัวใจโตและ CHF → prednisolone 2 มก./กก./วัน × 2 สัปดาห์** แล้วต่อ **salicylate 90–100 มก./กก./วัน × 6 สัปดาห์** (สไลด์)
- **รักษาหัวใจล้มเหลว**: จำกัดเกลือ **furosemide** · นอนพัก
- ติดตาม echo · ESR/CRP"""},
  {"q": "4. หลังจำหน่าย จะป้องกันการกลับเป็นซ้ำอย่างไร นานเท่าใด และถ้าผู้ปกครองถามว่าทำไมต้องฉีดยานานขนาดนี้จะตอบอย่างไร (4 คะแนน)",
   "a": """- **Benzathine penicillin G 1.2 ล้านยูนิต IM ทุก 4 สัปดาห์** (WHO 2024 — ดีกว่ายากิน · ผสมยาชาลดเจ็บได้) · แพ้ penicillin → erythromycin
- **ระยะเวลา**: เป็น carditis — ถ้า **มีโรคลิ้นหลงเหลือ → อย่างน้อย 10 ปีหลังครั้งสุดท้ายและถึงอายุอย่างน้อย 40 ปี** (บางรายตลอดชีวิต) · ถ้าลิ้นหายเป็นปกติ → 10 ปีหรือถึงอายุ 21 แล้วแต่อันไหนนานกว่า
- **อธิบายผู้ปกครอง**: การติดเชื้อที่คอซ้ำแต่ละครั้งทำให้ไข้รูมาติกกลับมาและ **ลิ้นหัวใจเสียเพิ่มทุกครั้ง** จนเป็นลิ้นตีบหรือรั่วถาวรที่ต้องผ่าตัด · การฉีดยาสม่ำเสมอเป็นวิธีที่ได้ผลที่สุดในการป้องกัน
- ดูแลฟันให้ดี · แจ้งแพทย์ว่ามีโรคหัวใจรูมาติกทุกครั้ง"""}],
 "ref": ["สไลด์ พ.ญ.ชนัญญา — ARF, Jones criteria, treatment", "WHO 2024 RF/RHD guideline"],
 "nl": ARF + ["2.1.27", "2.1.50", "2.3.9(5)"], "years": [], "_kind": "meq", "_set": "cardio"}]

LECTURE = {
 "lec": "27", "date": "อ. 6 ต.ค.",
 "title": "Valvular heart disease และ acute rheumatic fever",
 "subtitle": "ตรวจร่างกายลิ้นหัวใจ · แยก murmur · MS MR AS AR และลิ้นด้านขวา · เกณฑ์ผ่าตัดตาม ESC/EACTS 2025 · ไข้รูมาติก — Jones 2015 การรักษาและการป้องกันตาม WHO 2024 · infective endocarditis ตาม Duke-ISCVID 2023 และ ESC 2023",
 "objectives": [
   "ตรวจร่างกายระบบหัวใจตามลำดับ ดู คลำ เคาะ ฟัง และบรรยาย murmur ได้ครบองค์ประกอบ",
   "แยกชนิดของ murmur ตามจังหวะและรูปแบบ และอธิบายกลไกที่ทำให้แต่ละเสียงต่างกัน",
   "อธิบายกลไก อาการ อาการแสดง และผลตรวจของ MS MR AS และ AR",
   "บอกเกณฑ์ความรุนแรงทาง echo และข้อบ่งชี้ของหัตถการแต่ละลิ้นตามแนวทาง ESC/EACTS 2025",
   "เลือกยาต้านการแข็งตัวที่ถูกต้องใน rheumatic MS ที่มี AF",
   "วินิจฉัยไข้รูมาติกด้วยเกณฑ์ Jones ฉบับปรับปรุง 2015",
   "รักษาไข้รูมาติก และกำหนดยาและระยะเวลาการป้องกันการกลับเป็นซ้ำ",
   "สงสัยและวินิจฉัย infective endocarditis และให้ยาป้องกันได้ถูกกลุ่มตามแนวทางปัจจุบัน"],
 "nlGap": "เกณฑ์ฯ มีรหัส `นล. 2.3.9-3(8)` Valvular heart diseases · `2.3.9-3(1)` Acute rheumatic fever · `2.3.9-3(5)` Infective endocarditis (กลุ่ม 3 — วินิจฉัยแล้วส่งต่อ) แต่ **ไม่ได้ระบุเกณฑ์หัตถการแต่ละลิ้น** — ผู้ใช้ขอให้อัปเดตการวินิจฉัยและรักษาตามแนวทางล่าสุด จึงเทียบแผนภูมิ ACC/AHA 2020 ในสไลด์กับแนวทางด้านล่าง",
 "guidelines": [
   "**2025 ESC/EACTS Guidelines for the management of valvular heart disease** (Eur Heart J 2025) — TAVI อายุ ≥ 70 · เปลี่ยนลิ้นเร็วขึ้นใน AS ไม่มีอาการ · LVESDi ใน MR/AR · ซ่อม MR เมื่อมี AF/PH/LA โต/TR",
   "**2020 ACC/AHA Guideline for the management of patients with valvular heart disease** — แผนภูมิ MS MR AR ในสไลด์",
   "**WHO guideline on the prevention and diagnosis of rheumatic fever and rheumatic heart disease (2024)** — BPG ทุก 4 สัปดาห์ · amoxicillin วันละครั้ง · ยาป้องกันในผู้ที่พบ RHD จาก echo",
   "**Revision of the Jones criteria (AHA Scientific Statement, Circulation 2015)**",
   "**2023 ESC Guidelines for the management of endocarditis** และ **2023 Duke-ISCVID criteria** (Clin Infect Dis 2023)",
   "**INVICTUS trial (NEJM 2022)** — VKA ดีกว่า rivaroxaban ใน AF จากโรคหัวใจรูมาติก"],
 "sections": S, "meq": MEQ, "osce": [],
}

# กระจายตำแหน่งคำตอบของข้อใหม่ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น)
ORDERED = {N(1)}
_slot = 0
for s_ in S:
    for it in s_["items"]:
        if it["id"] in ORDERED:
            continue
        tgt = [0, 2, 4, 1, 3][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", "cardio.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LECTURE["lec"]]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

BANK_MAP = {
    "cardio-vhd-02": ["C-OLD-82", "C-OLD-91", "C-OLD-81", "C-OLD-83"],
    "cardio-vhd-03": ["C-MCQ-23", "C-OLD-72", "C-OLD-73", "C-OLD-74", "C-OLD-94"],
    "cardio-vhd-04": ["C-OLD-92", "C-OLD-93"],
    "cardio-vhd-05": ["C-MCQ-28", "C-OLD-79", "C-OLD-80"],
    "cardio-vhd-07": ["C-MCQ-25", "C-OLD-77", "C-OLD-78"],
    "cardio-vhd-08": ["C-MCQ-24", "C-OLD-75", "C-OLD-76"],
    "cardio-vhd-10": ["C-MCQ-26", "C-OLD-84", "C-OLD-85"],
    "cardio-vhd-12": ["C-OLD-86", "C-OLD-88", "C-OLD-90"],
    "cardio-vhd-13": ["C-MCQ-27", "C-OLD-87", "C-OLD-89"],
}
added = link("cardio", "27", BANK_MAP, meq=["C-MEQ-02"], osce=["C-OSCE-04"])

data = json.load(open(path, encoding="utf-8"))
L = [l for l in data if l["lec"] == "27"][0]
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = {c for s_ in L["sections"] for c in s_["nl"]} | {c for s_ in L["sections"] for i in s_["items"] for c in i["nl"]} | {c for m in L["meq"] + L["osce"] for c in m.get("nl", [])}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
data.sort(key=lambda l: (0, int(l["lec"])) if l["lec"].isdigit() else (1, l["lec"]))
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "cardio": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
new = sum(1 for s_ in S for i in s_["items"])
print("sections %d | ข้อใหม่ %d + คลัง %d = %d | meq %d | osce %d | nl %d" % (
    len(S), new, added, sum(len(s_["items"]) for s_ in L["sections"]), len(L["meq"]), len(L["osce"]), len(codes)))
print("cardio.json มี %d คาบ: %s" % (len(data), [l["lec"] for l in data]))
