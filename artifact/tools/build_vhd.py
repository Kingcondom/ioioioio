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

# ═══ ต่อส่วนที่ 2 ด้านล่าง ═══
