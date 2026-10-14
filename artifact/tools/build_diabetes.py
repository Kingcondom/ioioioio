#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""คาบ 14/10 Diabetes mellitus (Inc. DKA) — ศ.นพ.ชัยชาญ ดีโรจนวงศ์ → data/endo.json
ต้นฉบับ: Drive 1FB1Oe9v_DWc46H1Y37gi7Gu1ZbPcWdtH "2026 Diabetes lecture Student.pdf"
โน้ตสไลด์: slides/diabetes_notes.md · ภาพประกอบ: figs_diabetes.py
ไม่มีคาบนี้ในคลัง Ward Drill → ผูก Mock หมวด Endocrinology/Cardiology ที่ตรงเรื่อง
สไลด์ไม่มี DKA/HHS/hypoglycemia → หัวข้อ 7–9 อิง ADA 2024 hyperglycemic crises consensus + ADA 2009 + ADA Standards of Care"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_mock import link_mock
from svg import fig
import figs_diabetes as F

SET, LEC = "endo", "14/10"
SRC = "สไลด์ ศ.นพ.ชัยชาญ — Diabetes mellitus"
SRC_ADD = "ADA 2024 hyperglycemic crises consensus · ADA 2009 · ADA Standards of Care (ไม่อยู่ในสไลด์)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl, figs=None, source=SRC):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": source,
              "nl": nl, "md": md, "pearls": pearls, "items": items, "figs": figs or {}})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}
N = lambda n: "END-DM-MCQ-%02d" % n
R = lambda p: ["สไลด์ ศ.นพ.ชัยชาญ — " + p]
DM, DM1 = "2.3.4(1)", "B11.2.5(4)"
CRI, CRI1, HYPO = "2.2.16", "B11.2.5(5)", "2.2.17"
LAB, DRUG = ["3.3.12", "B11.3(2)"], "B11.4(1)"

# ───────────────────────────── 1
sec("endo-dm-01", "เบาหวานคืออะไร — insulin ทำงานที่ไหน และแนวทาง 5 ขั้น",
    "hyperglycemia จากการหลั่งหรือการออกฤทธิ์ของ insulin บกพร่อง · ตับ กล้ามเนื้อ ไขมัน · ภาวะแทรกซ้อนเล็ก–ใหญ่", 7,
"""### นิยาม (สไลด์)
เบาหวานคือโรคเมตาบอลิกที่มี 3 องค์ประกอบ
1. **น้ำตาลในเลือดสูง (hyperglycemia)**
2. ปัญหาของ **การหลั่ง insulin**, **การออกฤทธิ์ของ insulin** หรือทั้งสองอย่าง
3. ภาวะแทรกซ้อน **microvascular** (จอตา ไต เส้นประสาท) และ **macrovascular** (หัวใจ หลอดเลือดสมอง หลอดเลือดส่วนปลาย)

### insulin ออกฤทธิ์ที่ไหน
[[fig:insulin_map]]

insulin หลั่งจาก **β cell ของตับอ่อน** แล้วไปออกฤทธิ์ที่ **ตับ กล้ามเนื้อ และไขมัน** (target cells ในสไลด์) — การรู้ว่าแต่ละอวัยวะทำอะไรเมื่อขาด insulin จะอธิบายอาการเกือบทั้งหมดของคาบนี้
| อวัยวะ | เมื่อมี insulin | เมื่อขาด/ดื้อ insulin | สิ่งที่ตรวจเจอ |
|---|---|---|---|
| **ตับ** | เก็บ glycogen · หยุดสร้างน้ำตาลใหม่ | ปล่อยน้ำตาลออกมาตลอดคืน (glycogenolysis + gluconeogenesis) | **น้ำตาลขณะอดอาหาร (FPG) สูง** |
| **กล้ามเนื้อ** | ย้าย **GLUT4** ขึ้นผิวเซลล์ ดึงน้ำตาลเข้า | น้ำตาลหลังอาหารค้างในเลือด · สลายโปรตีน | **น้ำตาลหลังอาหาร (PPG) สูง** · กล้ามเนื้อลีบ |
| **ไขมัน** | เก็บไขมัน หยุดสลายไขมัน | ปล่อย FFA → ตับเปลี่ยนเป็น **ketone** | ketone (ขาดมาก) · TG สูง |

### Approach to diabetes — คิด 5 ขั้นทุกครั้ง (สไลด์)
| ขั้น | ถามอะไร |
|---|---|
| 1 | **วินิจฉัย** — เป็นเบาหวานจริงไหม (หัวข้อ 3) |
| 2 | **ชนิด** — T1, T2, ชนิดจำเพาะ หรือ GDM (หัวข้อ 4–6) |
| 3 | **ระยะเวลา** ที่เป็น และประวัติการคุมน้ำตาล |
| 4 | **ภาวะแทรกซ้อนเฉียบพลัน** — hypoglycemia, DKA, HHS (หัวข้อ 7–9) |
| 5 | **ภาวะแทรกซ้อนเรื้อรังของหลอดเลือด** — micro และ macro (หัวข้อ 10–13) |
""",
    ["เบาหวาน = น้ำตาลสูง + insulin หลั่ง/ออกฤทธิ์บกพร่อง + ภาวะแทรกซ้อน micro/macro",
     "insulin ออกฤทธิ์ที่ ตับ (หยุดปล่อยน้ำตาล) · กล้ามเนื้อ (GLUT4 ดึงน้ำตาลเข้า) · ไขมัน (หยุดสลายไขมัน)",
     "FPG สูง = ตับปล่อยน้ำตาลตอนกลางคืน · PPG สูง = กล้ามเนื้อดึงน้ำตาลไม่ได้",
     "Approach 5 ขั้น: วินิจฉัย → ชนิด → ระยะเวลา → acute complication → chronic complication"],
    [mcq(N(1), "In a patient with type 2 diabetes, which mechanism contributes most to an elevated fasting (pre-breakfast) plasma glucose?",
         ["Reduced glucose uptake by skeletal muscle after meals", "Excess hepatic glucose output overnight from glycogenolysis and gluconeogenesis", "Increased intestinal glucose absorption", "Reduced renal glucose excretion", "Increased glucose uptake by the brain"], 1,
         "ช่วงอดอาหารกลางคืน น้ำตาลในเลือดมาจาก **ตับ** เป็นหลัก — insulin ปกติจะกดการปล่อยน้ำตาลของตับ เมื่อตับดื้อ insulin ตับจึงสร้างและปล่อยน้ำตาลออกมาเกินทั้งคืน **FPG จึงสูง** (เป็นเหตุผลที่ metformin ซึ่งลดการปล่อยน้ำตาลจากตับ ช่วย FPG ได้ดี)\n\n- กล้ามเนื้อดึงน้ำตาลไม่ได้อธิบาย **น้ำตาลหลังอาหาร**\n- ลำไส้ดูดซึมเกี่ยวกับช่วงหลังอาหาร\n- ไตกลับขับ glucose มากขึ้นเมื่อน้ำตาลสูงเกิน threshold\n- สมองใช้น้ำตาลโดยไม่ต้องพึ่ง insulin และไม่ได้เพิ่มขึ้น",
         "FPG = ตับ · PPG = กล้ามเนื้อ", "Insulin action", R("What is diabetes; insulin target cells"), [DM, DM1, "B11.1.2(3)a"])],
    [DM, DM1, "B11.1.2(3)a"],
    {"insulin_map": fig("insulin ออกฤทธิ์ที่ 3 อวัยวะ",
        "ตับอ่อนหลั่ง insulin ไปยัง **ตับ กล้ามเนื้อ และไขมัน** — บรรทัดสีเขียวคือสิ่งที่ insulin ทำ บรรทัดสีแดงคือผลเมื่อขาด insulin: ตับปล่อยน้ำตาลจน **FPG สูง** · กล้ามเนื้อดึงน้ำตาลไม่ได้จน **PPG สูง** · ไขมันสลายจนตับสร้าง **ketone**",
        F.insulin_map())})

# ───────────────────────────── 2
sec("endo-dm-02", "ทำไมถึงมีอาการ — ปัสสาวะมาก กระหายน้ำ น้ำหนักลด ตามัว",
    "renal threshold ~180 · osmotic diuresis · อดอยากท่ามกลางน้ำตาล · เลนส์บวม · ติดเชื้อง่าย · acanthosis", 9,
"""### อาการคลาสสิก 3P + น้ำหนักลด
[[fig:sx_hub]]

### ทำไมปัสสาวะมาก — glucose ล้นท่อไต
[[fig:renal_threshold]]

ปกติ glucose ที่ถูกกรองทั้งหมดถูก **SGLT2 (และ SGLT1) ที่ proximal tubule** ดูดกลับจนปัสสาวะไม่มีน้ำตาล แต่ตัวขนส่งมีขีดจำกัด เมื่อ glucose ในเลือดเกินราว **180 mg/dL (renal threshold)** ส่วนที่เกินจะหลุดไปในปัสสาวะ และ **ดึงน้ำตามไปด้วยแรงออสโมซิส (osmotic diuresis)**

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | ใช้แยกอย่างไร |
|---|---|---|
| **ปัสสาวะมาก ตื่นมาปัสสาวะกลางคืน** | glucose เกิน renal threshold → glucose ในปัสสาวะดึงน้ำออก | ปัสสาวะมีน้ำตาล — ต่างจาก diabetes insipidus ที่ปัสสาวะเจือจางไม่มีน้ำตาล |
| **กระหายน้ำ ดื่มน้ำมาก** | เสียน้ำมากกว่าเกลือ → osmolality ในเลือดสูง → กระตุ้นศูนย์กระหายใน hypothalamus | ถ้าดื่มน้ำหวานแก้กระหาย น้ำตาลยิ่งสูง เป็นวงจร |
| **หิวบ่อย แต่น้ำหนักลด** | เซลล์ใช้น้ำตาลไม่ได้ ("อดอยากท่ามกลางน้ำตาล") จึงหิว · ร่างกายสลายไขมันและกล้ามเนื้อมาใช้ · เสียแคลอรีเป็น glucose ทางปัสสาวะ | น้ำหนักลดเร็ว + ketone = ขาด insulin มาก (T1 หรือ T2 ที่คุมไม่ได้) |
| **อ่อนเพลีย** | ขาดน้ำ + เซลล์ขาดพลังงาน + กล้ามเนื้อสลาย | — |
| **ตามัวขึ้นลง** | น้ำตาลสูงทำให้ glucose และ **sorbitol** เข้าเลนส์ ดึงน้ำตามเข้าไป เลนส์บวม ค่าสายตาเปลี่ยน | ดีขึ้นเมื่อน้ำตาลคงที่ — **ไม่ควรตัดแว่นใหม่** ระหว่างที่น้ำตาลยังขึ้นลง |
| **ติดเชื้อง่าย แผลหายช้า** | น้ำตาลสูงทำให้ neutrophil เคลื่อนที่และฆ่าเชื้อได้แย่ · glucose ในปัสสาวะ/ผิวเป็นอาหารของเชื้อ · หลอดเลือดและเส้นประสาทเสีย | เชื้อราช่องคลอด/ปลายองคชาต · UTI · ฝีผิวหนัง · melioidosis ในคนไทย |
| **ผิวคอ รักแร้ ดำหนา (acanthosis nigricans)** | insulin ในเลือดสูงมาก (ดื้อ insulin) ไปจับ **IGF-1 receptor** ที่ keratinocyte กระตุ้นให้ผิวหนาตัว | บอกว่า **ดื้อ insulin** → นึกถึง T2, อ้วน, PCOS |

> สไลด์ย้ำว่า **30% ของ T2DM มีภาวะแทรกซ้อนแล้วตั้งแต่วันที่วินิจฉัย** — เพราะ T2 มักไม่มีอาการหลายปีก่อนน้ำตาลจะสูงพอให้เกิดอาการข้างต้น
""",
    ["Renal threshold ~180 mg/dL — เกินแล้ว glucose ออกในปัสสาวะ ดึงน้ำตาม (osmotic diuresis)",
     "หิวแต่น้ำหนักลด = เซลล์ใช้น้ำตาลไม่ได้ สลายไขมัน/กล้ามเนื้อ + เสียแคลอรีทางปัสสาวะ",
     "ตามัวขึ้นลง = glucose/sorbitol เข้าเลนส์ เลนส์บวม — ไม่ตัดแว่นจนน้ำตาลคงที่",
     "Acanthosis nigricans = insulin สูงกระตุ้น IGF-1 receptor ที่ผิว → ดื้อ insulin",
     "30% ของ T2DM มีภาวะแทรกซ้อนตั้งแต่วินิจฉัย"],
    [mcq(N(2), "A 45-year-old man with newly recognized hyperglycemia (random glucose 320 mg/dL) complains that his distance vision has fluctuated for 3 weeks and asks for new glasses. What is the best explanation and advice?",
         ["Proliferative retinopathy; urgent laser therapy", "Osmotic swelling of the lens from glucose and sorbitol; defer new glasses until glucose is stable", "Acute angle-closure glaucoma; check intraocular pressure today", "Diabetic third nerve palsy; MRI brain", "Cataract; refer for surgery now"], 1,
         "น้ำตาลสูงทำให้ glucose และ **sorbitol** สะสมในเลนส์ ดึงน้ำเข้าไป เลนส์บวม **ค่าสายตาเปลี่ยนตามระดับน้ำตาล** จึงมัวขึ้นลง เมื่อคุมน้ำตาลได้คงที่จะกลับมา — ถ้าตัดแว่นตอนนี้ค่าสายตาจะเปลี่ยนอีก\n\n- **PDR** ทำให้มัวทันทีจากเลือดออกในวุ้นตา ไม่ใช่มัวขึ้นลง\n- **ต้อหินมุมปิด** ปวดตา ตาแดง เห็นแสงรุ้ง\n- **CN III palsy** มีหนังตาตก เห็นภาพซ้อน\n- **ต้อกระจก** ค่อยเป็นค่อยไป ไม่ขึ้นลง",
         "ตามัวขึ้นลงตอนน้ำตาลสูง = เลนส์บวม → ไม่ตัดแว่นจนน้ำตาลคงที่", "Symptoms", ["หลักสรีรวิทยา — ไม่ได้อยู่ในสไลด์"], [DM]),
     mcq(N(3), "A 30-year-old woman has polyuria, polydipsia and 6 kg weight loss. Plasma glucose is 360 mg/dL. Which mechanism best explains her polyuria?",
         ["Deficient antidiuretic hormone secretion", "Filtered glucose exceeding proximal tubular reabsorptive capacity, causing osmotic diuresis", "Hypercalcemia impairing urinary concentration", "Primary polydipsia", "Increased GFR from hyperfiltration alone"], 1,
         "glucose ที่ถูกกรองเกินความสามารถของ **SGLT ที่ proximal tubule** (renal threshold ราว 180 mg/dL) จึงออกในปัสสาวะ และดึงน้ำตามไปด้วยแรงออสโมซิส = **osmotic diuresis**\n\n- **ADH ขาด** (central DI) ปัสสาวะเจือจาง ไม่มีน้ำตาล\n- **Ca สูง** ทำให้ nephrogenic DI ได้ แต่รายนี้น้ำตาล 360 อธิบายได้ครบ\n- **primary polydipsia** น้ำตาลปกติ\n- hyperfiltration เพิ่ม GFR เล็กน้อย ไม่ใช่สาเหตุหลักของปัสสาวะมาก",
         "glucose > 180 → glucosuria → osmotic diuresis → polyuria → polydipsia", "Symptoms", ["หลักสรีรวิทยาไต — ไม่ได้อยู่ในสไลด์"], [DM, "2.1.42"])],
    [DM, "2.1.42", "2.1.9", "B9.2.5(1)"],
    {"sx_hub": fig("อาการของเบาหวานและกลไก",
        "ทุกอาการโยงกลับไปที่ **ขาด insulin หรือดื้อ insulin** — กลไกสั้น ๆ อยู่ใต้ชื่ออาการ รายละเอียดอยู่ในตารางถัดไป",
        F.sx_hub()),
     "renal_threshold": fig("ทำไมปัสสาวะมาก — glucose ล้นท่อไต",
        "ซ้าย: glucose ที่ถูกกรอง (ฟ้า) เพิ่มตามระดับในเลือด แต่การดูดกลับ (เขียว) มีเพดาน เมื่อเกิน **renal threshold ราว 180 mg/dL** ส่วนเกินออกในปัสสาวะ (แดง) · ขวา: glucose ในปัสสาวะดึงน้ำตาม → ปัสสาวะมาก → กระหายน้ำ และเสียแคลอรีจนน้ำหนักลด",
        F.renal_threshold())})

# ───────────────────────────── 3
sec("endo-dm-03", "วินิจฉัย ภาวะก่อนเบาหวาน และใครต้องคัดกรอง",
    "FPG ≥ 126 · 2-h OGTT ≥ 200 · HbA1c ≥ 6.5 · อาการ + casual ≥ 200 · IFG/IGT · คัดกรองตั้งแต่ 35 ปี", 9,
"""### เกณฑ์วินิจฉัย (สไลด์)
| เกณฑ์ | ค่า |
|---|---|
| **มีอาการ** + casual plasma glucose | **≥ 200 mg/dL** |
| **Fasting plasma glucose** (อดอาหาร ≥ 8 ชม.) | **≥ 126 mg/dL** |
| **2-hour plasma glucose** ระหว่าง 75-g OGTT | **≥ 200 mg/dL** |
| **HbA1c** | **≥ 6.5%** (สไลด์พิมพ์ "> 6.5" — ADA ใช้ ≥) |
ถ้า **ไม่มีอาการ ต้องยืนยันซ้ำอีกวัน** (หรือได้ 2 การตรวจผิดปกติจากตัวอย่างเดียวกัน — ADA)

[[fig:dx_line]]

### Pre-diabetes (สไลด์)
| ชนิด | เกณฑ์ |
|---|---|
| **IFG** (impaired fasting glucose) | FPG **100–125 mg/dL** |
| **IGT** (impaired glucose tolerance) | FPG < 126 และ 2-h **140–199 mg/dL** |
| HbA1c (ADA เพิ่ม) | 5.7–6.4% |
**ทำไมสำคัญ**: ① เสี่ยงเป็นเบาหวานในอนาคต ② **เสี่ยง atherosclerosis** แล้ว — หลอดเลือดเริ่มเสียตั้งแต่ระยะนี้

#### ทำไม HbA1c ใช้วินิจฉัยได้ และเมื่อไรเชื่อไม่ได้
glucose จับกับ hemoglobin ใน RBC อย่างช้า ๆ และถาวรตลอดอายุ RBC (~120 วัน) → HbA1c สะท้อน **น้ำตาลเฉลี่ย 2–3 เดือน** ไม่ต้องอดอาหาร · แต่ค่าจะ **ต่ำปลอม** เมื่อ RBC อายุสั้น (hemolysis, เสียเลือด, ตั้งครรภ์, เพิ่งได้เลือด) และ **ผิดเพี้ยน** ใน **hemoglobinopathy** ซึ่งพบบ่อยในไทย (HbE, thalassemia) — กรณีนี้ใช้ glucose แทน

### ใครต้องคัดกรอง T2DM ทั้งที่ไม่มีอาการ (สไลด์)
1. **อายุ ≥ 35 ปี** — ถ้าปกติ ตรวจซ้ำทุก **3 ปี**
2. **อายุ < 35 ปี แต่ BMI > 25** ร่วมกับปัจจัยเสี่ยง: ญาติสายตรงเป็นเบาหวาน · ไม่ออกกำลังกาย · เคยคลอดลูก **> 4 กก.** · BP **> 140/90** · **HDL < 35 หรือ TG > 250** · เคยเป็น IGT/IFG · **PCOS**
3. **มีโรคหลอดเลือด** อยู่แล้ว

> ความชุกเบาหวานไทยจาก NHES ครั้งที่ 7 (2567–2568) อยู่ในสไลด์เป็นภาพ อ่านตัวเลขไม่ได้
""",
    ["FPG ≥ 126 · 2-h OGTT ≥ 200 · HbA1c ≥ 6.5 · อาการ + casual ≥ 200 — ไม่มีอาการต้องยืนยันอีกวัน",
     "IFG = FPG 100–125 · IGT = 2-h 140–199 · เสี่ยงทั้งเบาหวานและ atherosclerosis",
     "HbA1c = น้ำตาลเฉลี่ย 2–3 เดือน · ผิดเพี้ยนใน hemolysis, ตั้งครรภ์, HbE/thalassemia",
     "คัดกรองทุกคนอายุ ≥ 35 ปี ซ้ำทุก 3 ปี · < 35 ปีถ้า BMI > 25 + ปัจจัยเสี่ยง"],
    [mcq(N(4), "A 42-year-old asymptomatic man has a fasting plasma glucose of 131 mg/dL on a routine check-up. What is the most appropriate next step?",
         ["Diagnose diabetes and start metformin today", "Repeat a diagnostic test (FPG or HbA1c) on another day to confirm", "Reassure; this is impaired fasting glucose", "Order C-peptide and GAD antibodies", "Recheck in 3 years"], 1,
         "สไลด์: ถ้า **ไม่มีอาการของน้ำตาลสูง** ต้อง **ยืนยันซ้ำอีกวัน** ก่อนวินิจฉัยเบาหวาน (ค่า FPG ≥ 126 ครั้งเดียวอาจคลาดเคลื่อนจากการอดอาหารไม่ครบหรือความเครียด)\n\n- เริ่มยาทันทีโดยยังไม่ยืนยันยังไม่ควร\n- **IFG** คือ 100–125 ค่านี้เกินแล้ว\n- C-peptide/antibody ใช้แยกชนิดเมื่อสงสัย T1 ไม่ใช่ขั้นแรก\n- ตรวจซ้ำทุก 3 ปีใช้กับผู้ที่ผลปกติ",
         "ไม่มีอาการ → ยืนยันซ้ำอีกวันเสมอ", "Diagnosis", R("Diagnosis of diabetes"), [DM] + LAB),
     mcq(N(5), "A 50-year-old woman has FPG 112 mg/dL and a 2-hour glucose of 168 mg/dL on a 75-g OGTT. How should she be classified?",
         ["Normal glucose tolerance", "Impaired fasting glucose only", "Impaired glucose tolerance only", "Both impaired fasting glucose and impaired glucose tolerance (prediabetes)", "Diabetes mellitus"], 3,
         "FPG **112 อยู่ในช่วง IFG (100–125)** และ 2-h **168 อยู่ในช่วง IGT (140–199)** → เป็น **ทั้ง IFG และ IGT = prediabetes** ซึ่งเสี่ยงเป็นเบาหวานและ atherosclerosis → ปรับพฤติกรรม ลดน้ำหนัก และติดตาม\n\n- ยังไม่ถึงเกณฑ์เบาหวาน (FPG ≥ 126 หรือ 2-h ≥ 200)",
         "FPG 100–125 = IFG · 2-h 140–199 = IGT", "Prediabetes", R("Definition of pre-diabetes"), [DM] + LAB)],
    [DM, "2.3.4(6)"] + LAB,
    {"dx_line": fig("เกณฑ์วินิจฉัย — ปกติ · prediabetes · เบาหวาน",
        "แถบสีบอกช่วงของแต่ละการตรวจ — เขียว ปกติ · เหลือง **prediabetes** (IFG, IGT และช่วง HbA1c ของ ADA) · แดง **เบาหวาน** — ต้องยืนยันซ้ำอีกวันถ้าไม่มีอาการ",
        F.dx_line())})

# ───────────────────────────── 4
sec("endo-dm-04", "ชนิดของเบาหวาน และ T1 — ภูมิคุ้มกันทำลาย β cell",
    "T1 · T2 · ชนิดจำเพาะ · GDM · พันธุกรรม + ตัวกระตุ้น → insulitis → อาการเมื่อ β cell หาย > 80%", 9,
"""### 4 กลุ่มใหญ่ (สไลด์)
| ชนิด | กลไก |
|---|---|
| **Type 1** | ภูมิต้านตนเองทำลาย β cell → **ขาด insulin** |
| **Type 2** | **ดื้อ insulin** ร่วมกับ **insulin ไม่พอ** |
| **Other specific types** | ตารางถัดไป |
| **Gestational (GDM)** | หัวข้อ 6 |

**ชนิดจำเพาะ (other specific types) — สไลด์**
| กลุ่ม | ตัวอย่าง |
|---|---|
| ยีน β cell / การออกฤทธิ์ของ insulin | **MODY** |
| โรคของตับอ่อนส่วน exocrine | **ตับอ่อนอักเสบ** (type 3c), cystic fibrosis, **hemochromatosis** |
| โรคต่อมไร้ท่อ | **Cushing syndrome** (และ acromegaly, pheochromocytoma) |
| ยา/สารเคมี | **steroids**, niacin, α-interferon, phenytoin, protease inhibitor, **clozapine** |
| ติดเชื้อ · ภูมิคุ้มกันแบบไม่พบบ่อย · กลุ่มอาการทางพันธุกรรม | — |

### Type 1 — เกิดอย่างไร (สไลด์)
[[fig:t1_course]]

| ขั้น | เกิดอะไร |
|---|---|
| **พันธุกรรมเสี่ยง** | มียีนที่ทำให้ระบบภูมิคุ้มกันเสี่ยงหลงจำ β cell เป็นสิ่งแปลกปลอม |
| **ตัวกระตุ้นจากสิ่งแวดล้อม** | ไวรัส (**coxsackie, rubella, mumps**) · สารพิษ (nitrosourea) · อาหาร (โปรตีนนมวัว) |
| **ภูมิต้านตนเองทำงาน** | มี autoantigen → **autoantibody** ขึ้นในเลือด (GAD65, IA-2, ZnT8, insulin — ใช้ตรวจยืนยัน T1) |
| **Insulitis** | เซลล์อักเสบแทรกในเกาะตับอ่อน · **T lymphocyte ทำลาย β cell** |
| **เบาหวาน** | อาการเกิดเมื่อ **β cell ถูกทำลาย > 80%** |

#### ทำไม T1 ถึงมาแบบนี้
| ลักษณะ | กลไก |
|---|---|
| ช่วงก่อนวินิจฉัยเงียบนานหลายเดือน–ปี | β cell ที่เหลือ 20% ยังพอคุมน้ำตาลได้ จนกว่าจะหายไปเกินจุดวิกฤต |
| **เริ่มอาการเร็ว น้ำหนักลดมาก อาจมาด้วย DKA เป็นครั้งแรก** | ขาด insulin **เกือบสมบูรณ์** — ไขมันสลายไม่มีอะไรยับยั้ง จึงเกิด ketone (หัวข้อ 7) |
| ช่วงแรกหลังเริ่ม insulin ต้องการยาน้อยลง (honeymoon) | แก้น้ำตาลสูงแล้ว β cell ที่เหลือฟื้นทำงานชั่วคราว ก่อนถูกทำลายต่อ |
| มักมีโรคภูมิต้านตนเองอื่นร่วม | Hashimoto, Graves, Addison, celiac, vitiligo — รวมเรียก **polyglandular autoimmune syndrome** |
""",
    ["4 ชนิด: T1 (ขาด insulin จากภูมิทำลาย) · T2 (ดื้อ + ไม่พอ) · ชนิดจำเพาะ · GDM",
     "ชนิดจำเพาะ: MODY · ตับอ่อน (pancreatitis, hemochromatosis) · Cushing · steroids/clozapine/protease inhibitor",
     "T1: พันธุกรรม + ตัวกระตุ้น (coxsackie, rubella, mumps) → autoantibody → insulitis → อาการเมื่อ β cell หาย > 80%",
     "T1 มักมาเร็ว น้ำหนักลด หรือมาด้วย DKA ครั้งแรก · มีโรคภูมิต้านตนเองอื่นร่วมได้"],
    [mcq(N(6), "Which statement about the natural history of autoimmune type 1 diabetes is correct?",
         ["Hyperglycemia appears as soon as autoantibodies become detectable", "Symptoms typically appear only after more than about 80% of beta-cell mass has been destroyed", "Beta-cell destruction is mediated mainly by circulating insulin antibodies", "Environmental triggers are not involved", "C-peptide is usually high at diagnosis"], 1,
         "สไลด์: ภูมิต้านตนเองทำลาย β cell ทีละน้อยเป็นเดือนถึงปี (autoantibody ขึ้นมาก่อนนาน) และอาการเกิดเมื่อ **β cell ถูกทำลายมากกว่าราว 80%** ซึ่ง β cell ที่เหลือคุมน้ำตาลไม่ไหวแล้ว\n\n- autoantibody ขึ้นก่อนน้ำตาลสูงหลายปี\n- ผู้ทำลายคือ **T lymphocyte** — antibody เป็นตัวบ่งชี้\n- สไลด์ระบุตัวกระตุ้นจากไวรัส สารพิษ อาหาร\n- C-peptide ใน T1 **ต่ำหรือไม่มี**",
         "T1: อาการเกิดเมื่อ β cell หาย > 80% — T cell เป็นผู้ทำลาย", "Type 1 pathogenesis", R("Type 1 pathogenesis"), [DM, DM1]),
     mcq(N(7), "A 55-year-old man treated with high-dose prednisolone for 2 months for autoimmune hepatitis now has FPG 168 mg/dL on two occasions. How is his diabetes best classified?",
         ["Type 1 diabetes", "Type 2 diabetes", "Other specific type — drug-induced diabetes", "Gestational diabetes", "Maturity-onset diabetes of the young"], 2,
         "สไลด์จัด **เบาหวานจากยา (steroids, niacin, interferon, clozapine, protease inhibitor ฯลฯ)** ไว้ในกลุ่ม **other specific types** — glucocorticoid เพิ่มการสร้างน้ำตาลจากตับและทำให้กล้ามเนื้อดื้อ insulin น้ำตาลหลังอาหารช่วงบ่ายถึงเย็นจะสูงเด่น\n\n- ไม่มีลักษณะภูมิต้านตนเองของ T1\n- T2 เป็นการวินิจฉัยเมื่อไม่มีสาเหตุจำเพาะ\n- MODY เป็นโรคทางพันธุกรรมในคนอายุน้อยที่มีประวัติครอบครัวหลายรุ่น",
         "steroid-induced = other specific type", "Classification", R("Classification of diabetes — other specific types"), [DM])],
    [DM, DM1],
    {"t1_course": fig("T1DM — β cell ถูกทำลายทีละน้อยจนถึงจุดวิกฤต",
        "พันธุกรรม → ตัวกระตุ้น → ภูมิต้านตนเอง (autoantibody ขึ้น) → insulitis มวล β cell ลดลงต่อเนื่อง แต่ **อาการจะเริ่มเมื่อเหลือไม่ถึง 20%** (ถูกทำลาย > 80%) จึงดูเหมือนเป็นเฉียบพลัน ทั้งที่กระบวนการเริ่มมานานแล้ว",
        F.t1_course())})

# ───────────────────────────── 5
sec("endo-dm-05", "Type 2 — ดื้อ insulin + β cell ล้า · แยก T1/T2 · C-peptide",
    "อ้วน ไม่ออกกำลัง อายุ พันธุกรรม · ชดเชยด้วย insulin สูงจนล้า · น้ำตาลหลังอาหารขึ้นก่อน · C-peptide บอก insulin ของตัวเอง", 9,
"""### กลไก T2 (สไลด์ อ้าง DeFronzo)
ปัจจัย: **อ้วน · ไม่ออกกำลังกาย · อายุมาก · พันธุกรรม · glucotoxicity · FFA สูง** → **insulin resistance ↑** ร่วมกับ **β-cell function ↓**
- ถ้าตับอ่อน **หลั่ง insulin ชดเชยได้พอ** → น้ำตาลยังปกติ
- ถ้า **ชดเชยไม่พอ** → เป็น T2DM

### ธรรมชาติของโรค
[[fig:t2_natural]]

#### ทำไมถึงเป็นแบบนี้
| สิ่งที่เห็น | กลไก |
|---|---|
| **ดื้อ insulin มาก่อนน้ำตาลสูงหลายปี** | ไขมันในช่องท้องและ FFA ทำให้ตับและกล้ามเนื้อตอบสนอง insulin น้อยลง ตับอ่อนจึงต้องหลั่งเพิ่ม (hyperinsulinemia) |
| **น้ำตาลหลังอาหารสูงก่อน FPG** | ช่วงหลังอาหารต้องการ insulin มากที่สุด β cell ที่เริ่มล้าตามไม่ทันก่อน · ตับยังกดการปล่อยน้ำตาลตอนกลางคืนได้อยู่ |
| **โรคแย่ลงเรื่อย ๆ แม้คุมดี** | β cell ล้าจาก glucotoxicity และ lipotoxicity — UKPDS พบ β-cell function ลดต่อเนื่อง ส่วนใหญ่สุดท้ายต้องใช้ insulin (หัวข้อ 15) |
| **ไม่มี ketone** | ยังมี insulin พอยับยั้งการสลายไขมัน (กลไกเดียวกับ HHS หัวข้อ 7) |

### แยก T1 กับ T2 (สไลด์)
| ลักษณะ | **Type 1** | **Type 2** |
|---|---|---|
| Ketone | ketonuria / ketoacidosis | ไม่มี |
| อาการ | ปานกลาง–รุนแรง | น้อยหรือไม่มีอาการ |
| การเริ่ม | เร็ว | ช้า |
| รูปร่าง | ผอม น้ำหนักลด | น้ำหนักเกิน |
| อายุ | < 30 ปี | > 30 ปี |
| Antibody | บวก | ลบ |
| **C-peptide** | **ต่ำหรือไม่มี** | **ปกติหรือสูง** |

### C-peptide คืออะไร ทำไมใช้แยกได้
[[fig:proinsulin]]

β cell สร้าง **proinsulin** แล้วตัดเป็น **insulin + C-peptide** ในปริมาณเท่ากัน (สไลด์: C-peptide คือส่วนที่ถูกตัดทิ้ง จึงบอกว่าตับอ่อนสร้าง insulin เท่าไร) — วัด C-peptide ดีกว่าวัด insulin เพราะ ① **insulin ที่ฉีดไม่มี C-peptide** จึงใช้ได้แม้ผู้ป่วยฉีด insulin อยู่ ② insulin ถูกตับดึงทิ้งรอบแรกมาก แต่ C-peptide ไม่ถูกดึง
""",
    ["T2 = insulin resistance ↑ + β-cell function ↓ · ชดเชยได้ = ปกติ · ไม่ได้ = เบาหวาน",
     "น้ำตาลหลังอาหารขึ้นก่อน FPG · โรคแย่ลงเรื่อย ๆ จาก β cell ล้า (UKPDS)",
     "T1: ketone · เร็ว · ผอม · < 30 ปี · antibody + · C-peptide ต่ำ",
     "T2: ไม่มี ketone · ช้า · อ้วน · > 30 ปี · antibody − · C-peptide ปกติ/สูง",
     "C-peptide ตัดจาก proinsulin เท่ากับ insulin · ไม่มีใน insulin ฉีด → ใช้วัดได้แม้ฉีด insulin อยู่"],
    [mcq(N(8), "A 24-year-old woman has been on insulin since diabetes was diagnosed 6 months ago. Her physician wants to know whether she still produces endogenous insulin. Which test is most appropriate?",
         ["Serum insulin level", "Fasting C-peptide", "HbA1c", "Proinsulin-to-insulin ratio", "Serum fructosamine"], 1,
         "**C-peptide** ถูกตัดออกจาก proinsulin เท่ากับ insulin ที่ตับอ่อนสร้างเอง และ **ไม่มีอยู่ใน insulin ที่ฉีด** จึงสะท้อน insulin ของร่างกายได้แม้ผู้ป่วยฉีด insulin อยู่ (สไลด์: C-peptide บอกว่าตับอ่อนสร้าง insulin เท่าไร)\n\n- **ระดับ insulin** ปนกับ insulin ที่ฉีด\n- **HbA1c, fructosamine** บอกการคุมน้ำตาล ไม่บอกการสร้าง insulin\n- proinsulin ratio ไม่ใช้ในเวชปฏิบัติทั่วไป",
         "ผู้ป่วยฉีด insulin อยากรู้ว่าสร้างเองได้ไหม → C-peptide", "C-peptide", R("C-peptide"), [DM, DM1] + LAB),
     mcq(N(9), "Over the 10 years before type 2 diabetes is diagnosed, which pattern is typically seen?",
         ["Insulin levels are low from the start and fasting glucose rises first", "Insulin resistance and compensatory hyperinsulinemia precede the rise in glucose, and post-meal glucose rises before fasting glucose", "Fasting and post-meal glucose rise at the same time", "Beta-cell function improves as insulin resistance increases", "Autoantibodies appear before hyperglycemia"], 1,
         "ใน T2 **insulin resistance** เกิดก่อนหลายปี ตับอ่อน **ชดเชยด้วย insulin สูง** น้ำตาลจึงยังปกติ เมื่อ β cell เริ่มล้า **น้ำตาลหลังอาหาร** (ช่วงที่ต้องการ insulin มากที่สุด) จะขึ้นก่อน แล้ว FPG จึงตามมา (กราฟ natural history ในสไลด์)\n\n- insulin ต่ำตั้งแต่ต้นเป็นลักษณะ T1\n- β cell ไม่ได้ดีขึ้น — ล้าลงเรื่อย ๆ\n- autoantibody เป็นของ T1",
         "T2: ดื้อ insulin + insulin สูงชดเชย → PPG ขึ้นก่อน FPG", "Type 2 natural history", R("Natural history of type 2 diabetes"), [DM, DM1])],
    [DM, DM1, "2.3.4(7)"],
    {"t2_natural": fig("ธรรมชาติของ T2DM",
        "**insulin resistance** (ส้ม) สูงขึ้นตั้งแต่ก่อนวินิจฉัยหลายปี ตับอ่อนชดเชยด้วย **insulin สูง** (เขียว) จนล้าและลดลง · **น้ำตาลหลังอาหาร** (แดงทึบ) ขึ้นก่อน **น้ำตาลขณะอดอาหาร** (แดงประ) — กราฟเชิงหลักการตามสไลด์ (ตัวเลขแกนตั้งเป็นสัดส่วน)",
        F.t2_natural()),
     "proinsulin": fig("Proinsulin → insulin + C-peptide",
        "β cell ตัด proinsulin ได้ insulin (สาย A + B) และ **C-peptide** จำนวนเท่ากัน — C-peptide จึงเป็นตัวแทนของ insulin ที่ร่างกายสร้างเอง ใช้แยก T1 (ต่ำ) กับ T2 (ปกติ/สูง)",
        F.proinsulin())})

# ═══════════════════════════ END SECTIONS
