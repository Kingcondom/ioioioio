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

# ───────────────────────────── 6
sec("endo-dm-06", "Gestational diabetes — ทำไมทารกตัวโตแล้วน้ำตาลต่ำหลังคลอด",
    "ฮอร์โมนรกทำให้ดื้อ insulin · Pedersen · ผลต่อทารกและมารดา · เกณฑ์ 100 g / 75 g · คัดกรอง 24–28 สัปดาห์", 10,
"""### GDM คืออะไร (สไลด์)
- glucose tolerance ผิดปกติที่พบขณะตั้งครรภ์
- **ดื้อ insulin จากฮอร์โมนของรก** (human placental lactogen, progesterone, cortisol — เพิ่มขึ้นมากในไตรมาสที่ 2–3)
- ตับอ่อนของแม่สร้าง insulin เพิ่มได้ไม่พอกับความต้องการ
- **50% เป็นเบาหวานถาวรภายใน 10 ปี**

### ทำไมทารกถึงมีปัญหา — กลไก Pedersen
[[fig:pedersen]]

#### ทำไมถึงมีอาการนี้ (ภาวะแทรกซ้อนต่อทารกในสไลด์)
| ภาวะของทารก | กลไก |
|---|---|
| **ตัวโต (macrosomia)** | glucose ของแม่ผ่านรก แต่ insulin ไม่ผ่าน → ตับอ่อนทารกสร้าง insulin มาก · **insulin เป็นฮอร์โมนเร่งการเจริญเติบโต** ไขมันและอวัยวะโต (ไหล่กว้าง → ไหล่ติด) |
| **น้ำตาลต่ำหลังคลอด** | ตัดสายสะดือ glucose จากแม่หยุดทันที แต่ทารกยังมี **insulin สูงค้าง** |
| **RDS (ปอดไม่พร้อม)** | insulin สูงต้านการกระตุ้นของ cortisol ต่อการสร้าง **surfactant** |
| **Polycythemia → ตัวเหลือง** | ทารกเผาผลาญมาก ใช้ออกซิเจนมาก → ขาดออกซิเจนเรื้อรัง → EPO ↑ · เม็ดเลือดแดงมากแตกเป็น bilirubin |
| **Ca ต่ำ** | การทำงานของ parathyroid ในทารกยังไม่เต็มที่ (กลไกซับซ้อน) |

**ต่อมารดา (สไลด์)**: ครรภ์เป็นพิษ (toxemia) · ผ่าคลอด · กรวยไตอักเสบ · ครรภ์แฝดน้ำ (ทารกปัสสาวะมากจากน้ำตาลสูง) · เสียชีวิต
**ปัจจัยเสี่ยง (สไลด์)**: อายุ > 25 ปี · ครอบครัวเป็นเบาหวาน · อ้วน · เคยเป็น GDM หรือคลอดลูกตัวโต · ประวัติการตั้งครรภ์ไม่ดี

### การคัดกรองและวินิจฉัย (สไลด์)
**คัดกรอง**: หญิงเสี่ยงสูงตรวจตั้งแต่ ANC ครั้งแรก ถ้าปกติ **ตรวจซ้ำที่ 24–28 สัปดาห์** · **50-g glucose challenge** ถ้า 1 ชม. **≥ 130 (หรือ 140) mg/dL** → ทำ OGTT เต็ม
| การตรวจ | ขณะอด | 1 ชม. | 2 ชม. | 3 ชม. |
|---|---|---|---|---|
| **100 g — Carpenter & Coustan** | ≥ 95 | ≥ 180 | ≥ 155 | ≥ 140 |
| **100 g — NDDG** | ≥ 105 | ≥ 190 | ≥ 165 | ≥ 145 |
| **75 g — WHO (IADPSG)** | ≥ 92 | ≥ 180 | ≥ 153 | — |
การแปลผล (เกณฑ์มาตรฐาน — สไลด์ไม่ได้ระบุ): 100 g ต้องผิดปกติ **≥ 2 ค่า** · 75 g ผิดปกติ **≥ 1 ค่า** ก็วินิจฉัยได้

### หลังวินิจฉัย (ADA — ไม่อยู่ในสไลด์)
ควบคุมอาหารและออกกำลังกายก่อน · ถ้าไม่ถึงเป้า ยาแรกคือ **insulin** (metformin และ glibenclamide ผ่านรก) · หลังคลอด **OGTT ที่ 4–12 สัปดาห์** แล้วคัดกรองต่อทุก 1–3 ปีตลอดชีวิต (เพราะ 50% เป็นเบาหวานใน 10 ปี)
""",
    ["GDM = ดื้อ insulin จากฮอร์โมนรก + insulin ไม่พอ · 50% เป็นเบาหวานถาวรใน 10 ปี",
     "Pedersen: glucose ผ่านรก insulin ไม่ผ่าน → ทารก hyperinsulinemia → ตัวโต · น้ำตาลต่ำหลังคลอด · RDS · polycythemia",
     "คัดกรองหญิงเสี่ยงตั้งแต่ ANC แรก ซ้ำ 24–28 สัปดาห์ · 50-g GCT ≥ 130/140 → OGTT",
     "100 g C&C: 95/180/155/140 (≥ 2 ค่า) · 75 g: 92/180/153 (≥ 1 ค่า)",
     "หลังคลอด OGTT 4–12 สัปดาห์ แล้วคัดกรองตลอดชีวิต"],
    [mcq(N(10), "A baby born at 38 weeks to a mother with poorly controlled gestational diabetes weighs 4.4 kg. At 2 hours of age the baby is jittery with a capillary glucose of 28 mg/dL. What is the mechanism of the hypoglycemia?",
         ["Neonatal adrenal insufficiency", "Persistent fetal hyperinsulinemia after the maternal glucose supply stops at birth", "Transfer of maternal insulin across the placenta", "Congenital deficiency of glycogen storage", "Neonatal sepsis consuming glucose"], 1,
         "**Pedersen hypothesis** — glucose ของแม่ผ่านรก (insulin ไม่ผ่าน) ตับอ่อนทารกจึงสร้าง insulin มากตลอดการตั้งครรภ์ (ทำให้ตัวโต 4.4 กก.) เมื่อคลอด glucose จากแม่หยุดทันที แต่ **insulin ของทารกยังสูงค้าง** → น้ำตาลต่ำในไม่กี่ชั่วโมงแรก\n\n- **insulin ของแม่ไม่ผ่านรก**\n- ไม่มีข้อมูลสนับสนุนต่อมหมวกไตบกพร่องหรือโรคสะสม glycogen\n- sepsis เป็นไปได้เสมอแต่ไม่อธิบายตัวโต",
         "ทารกแม่ GDM: ตัวโต + น้ำตาลต่ำหลังคลอด = fetal hyperinsulinemia", "GDM", R("Gestational diabetes — complications to baby"), [DM, "2.3.15-3(11)", "2.3.16(5)"]),
     mcq(N(11), "A 30-year-old woman at 26 weeks has a 100-g OGTT: fasting 98, 1-hour 186, 2-hour 150 and 3-hour 128 mg/dL. Using the Carpenter–Coustan thresholds from the lecture, what is the interpretation?",
         ["Normal — only one value is abnormal", "Gestational diabetes — two values meet or exceed the thresholds", "Overt diabetes in pregnancy", "Impaired glucose tolerance only", "The test must be repeated with 75 g"], 1,
         "เกณฑ์ **Carpenter & Coustan** (สไลด์): ขณะอด ≥ 95 · 1 ชม. ≥ 180 · 2 ชม. ≥ 155 · 3 ชม. ≥ 140 — รายนี้ **ขณะอด 98 และ 1 ชม. 186 ผิดปกติ = 2 ค่า** จึงวินิจฉัย **GDM** (100-g ต้องผิดปกติอย่างน้อย 2 ค่า)\n\n- 2 ชม. 150 และ 3 ชม. 128 ยังปกติ\n- overt diabetes ต้องเข้าเกณฑ์ของคนไม่ตั้งครรภ์ (เช่น FPG ≥ 126)\n- ไม่จำเป็นต้องตรวจซ้ำด้วย 75 g",
         "100-g OGTT: ผิดปกติ ≥ 2 ค่า = GDM", "GDM", R("Diagnosis of GDM — Carpenter & Coustan"), [DM, "2.3.15-3(11)"] + LAB)],
    [DM, "2.3.15-3(11)", "B10.1.3(3)", "2.3.16(5)"] + LAB,
    {"pedersen": fig("กลไก Pedersen — ทำไมแม่น้ำตาลสูงแล้วทารกมีปัญหา",
        "glucose ของแม่ **ผ่านรก** แต่ **insulin ไม่ผ่าน** ทารกจึงสร้าง insulin เองมาก (fetal hyperinsulinemia) แล้วแตกเป็นสี่ผล: ตัวโต · น้ำตาลต่ำหลังคลอด · ปอดไม่พร้อม · เลือดข้นจนตัวเหลือง",
        F.pedersen())})

# ───────────────────────────── 7
sec("endo-dm-07", "DKA และ HHS — กลไก อาการ และเกณฑ์วินิจฉัย",
    "ขาด insulin + ฮอร์โมนต้าน · ketone มาจากไขมัน · ทำไม HHS ไม่มี ketone · Kussmaul · corrected Na · osmolality", 13,
"""> สไลด์ระบุ DKA และ HHNS เป็นภาวะแทรกซ้อนเฉียบพลันในขั้นที่ 4 ของ approach แต่ **ไม่มีสไลด์รายละเอียด** (ปฏิทินเขียนว่า "Inc. DKA") — หัวข้อ 7–9 จึงเรียบเรียงจาก **ADA/EASD/JBDS/AACE/DTS consensus 2024** และ **ADA 2009 (Kitabchi)**

### DKA เกิดอย่างไร
[[fig:dka]]

#### ทำไมถึงมีอาการนี้
| อาการ / ผลตรวจ | กลไก |
|---|---|
| **หายใจหอบลึก (Kussmaul)** | กรด ketone ทำให้ pH ต่ำ → กระตุ้น chemoreceptor ให้หายใจลึกเร็ว ระบาย CO₂ ชดเชยภาวะกรด |
| **ลมหายใจกลิ่นผลไม้** | acetoacetate สลายเองเป็น **acetone** ที่ระเหยออกทางลมหายใจ |
| **ปวดท้อง อาเจียน** (อาจคล้ายท้องเสียแบบผ่าตัด) | ภาวะกรดและ ketone ทำให้กระเพาะลำไส้บีบตัวน้อย ยืด · อาเจียนยิ่งเสียน้ำ — ปวดท้องที่ไม่ดีขึ้นเมื่อแก้กรดแล้วต้องหาสาเหตุอื่น |
| **ขาดน้ำมาก ชีพจรเร็ว BP ต่ำ** | osmotic diuresis หลายวัน + อาเจียน — เสียน้ำราว **6 ลิตร** (HHS ราว **9 ลิตร**) |
| **ซึม สับสน** | สัมพันธ์กับ **osmolality สูง** มากกว่าความเป็นกรด — ถ้า effective osmolality ไม่สูงแต่ซึมมาก ให้หาสาเหตุอื่น |
| **Na ต่ำ** | glucose สูงดึงน้ำจากเซลล์ออกมาเจือจาง Na → ต้องดู **corrected Na** |
| **K ปกติหรือสูง แต่ร่างกายพร่อง** | ขาด insulin + กรด + osmolality สูง ดึง K ออกจากเซลล์ ขณะที่ปัสสาวะขับ K ทิ้ง (หัวข้อ 8) |
| WBC สูง · amylase สูง | ความเครียดและภาวะกรด — ไม่ได้แปลว่าติดเชื้อหรือตับอ่อนอักเสบเสมอไป แต่ต้องหาตัวกระตุ้น |
| **urine ketone อาจบวกมากขึ้นระหว่างรักษา** | strip (nitroprusside) วัดได้แค่ **acetoacetate** ไม่วัด **β-hydroxybutyrate** (ketone หลักใน DKA) เมื่อรักษา β-OHB ถูกเปลี่ยนเป็น acetoacetate — ติดตามด้วย **β-OHB ในเลือด** ไม่ใช่ urine ketone |

### ทำไม HHS ถึงไม่มี ketone
[[fig:dkahhs]]

HHS มักเป็นใน **T2 ผู้สูงอายุ** ที่ยังมี insulin อยู่บ้าง — insulin ปริมาณน้อยก็ **หยุดการสลายไขมันได้แล้ว** จึงไม่มี ketone แต่ไม่พอจะคุมน้ำตาล น้ำตาลจึงค่อย ๆ สูงเป็นวันถึงสัปดาห์ ปัสสาวะออกต่อเนื่องจนขาดน้ำรุนแรง osmolality สูงมาก และซึมจนหมดสติ

### เกณฑ์วินิจฉัย
| | **DKA** | **HHS** |
|---|---|---|
| Glucose | **≥ 200 mg/dL** หรือเคยเป็นเบาหวาน (ADA 2009 ใช้ > 250) | **≥ 600 mg/dL** |
| Ketone | **β-OHB ≥ 3.0 mmol/L** หรือ urine ketone ≥ 2+ | ไม่มีนัยสำคัญ (β-OHB < 3.0) |
| ความเป็นกรด | **pH < 7.3 และ/หรือ HCO₃ < 18** | pH ≥ 7.3 · HCO₃ ≥ 15 |
| Osmolality | แปรผัน | **effective > 300 mOsm/kg** (หรือ total > 320) |
| การเริ่ม | ชั่วโมง–1 วัน | หลายวัน–สัปดาห์ |
(ADA consensus 2024 — ผู้ป่วยบางรายมีลักษณะทั้งสองภาวะร่วมกัน)

**ความรุนแรงของ DKA (ADA 2009)**: mild pH 7.25–7.30 / HCO₃ 15–18 / ตื่นดี · moderate pH 7.00–7.24 / HCO₃ 10–< 15 / ง่วง · severe pH < 7.00 / HCO₃ < 10 / ซึม–หมดสติ

### สูตรที่ต้องคำนวณเป็น
| สูตร | ใช้ทำอะไร |
|---|---|
| **Anion gap** = Na − (Cl + HCO₃) | ปกติราว 12 ± 2 · ketone ทำให้สูง |
| **Corrected Na** = Na + 1.6 × (glucose − 100)/100 | บอก Na จริงเพื่อเลือกสารน้ำ |
| **Effective osmolality** = 2 × Na + glucose/18 | วินิจฉัย HHS · ติดตามไม่ให้ลดเร็วเกิน |

**ตัวกระตุ้นที่ต้องหาเสมอ**: ติดเชื้อ (พบบ่อยสุด) · หยุดหรือขาด insulin · T1 รายใหม่ · MI, stroke, ตับอ่อนอักเสบ · ยา (steroid, **SGLT2i** — ทำให้เกิด **euglycemic DKA** ที่น้ำตาล < 250 แต่มีกรด ketone) · ตั้งครรภ์
""",
    ["DKA: ขาด insulin + glucagon สูง → สลายไขมัน → ketone → กรด AG สูง · glucose สูง → ขาดน้ำ ~6 ลิตร",
     "Kussmaul = ชดเชยกรด · กลิ่นผลไม้ = acetone · ซึมสัมพันธ์กับ osmolality",
     "HHS: insulin น้อยก็พอหยุด ketone แต่ไม่พอคุมน้ำตาล → glucose ≥ 600 · osm > 300 · pH ≥ 7.3",
     "DKA 2024: glucose ≥ 200 (หรือเคยเป็น DM) · β-OHB ≥ 3 · pH < 7.3 และ/หรือ HCO₃ < 18",
     "Corrected Na = Na + 1.6 × (glucose − 100)/100 · eff osm = 2Na + glucose/18 · urine ketone ไม่วัด β-OHB"],
    [mcq(N(12), "A 22-year-old man with DKA has Na 128 mEq/L and glucose 700 mg/dL. What is his corrected sodium, and what does it imply?",
         ["About 118 mEq/L — true severe hyponatremia", "About 128 mEq/L — no correction is needed", "About 138 mEq/L — the low measured sodium is dilutional from hyperglycemia", "About 148 mEq/L — severe hypernatremia", "Sodium cannot be interpreted until glucose is normal"], 2,
         "**Corrected Na = 128 + 1.6 × (700 − 100)/100 = 128 + 9.6 ≈ 138 mEq/L** — Na ที่วัดได้ต่ำเพราะ glucose สูงดึงน้ำออกจากเซลล์มาเจือจาง ค่าแท้จริงปกติ → ใช้ค่า corrected เลือกสารน้ำหลังชั่วโมงแรก (corrected Na ปกติ/สูง → 0.45% NaCl)\n\n- ไม่ใช่ hyponatremia แท้\n- ต้องแก้ค่าเสมอเมื่อน้ำตาลสูง",
         "Corrected Na = Na + 1.6 ต่อ glucose ทุก 100 ที่เกิน 100", "DKA labs", [SRC_ADD], [CRI, CRI1, "B9.2.5(2)"]),
     mcq(N(13), "A 76-year-old woman with type 2 diabetes has been increasingly drowsy for 5 days. Glucose 980 mg/dL, Na 140 mEq/L, pH 7.36, HCO3 23 mEq/L, serum beta-hydroxybutyrate 0.8 mmol/L. Why is ketoacidosis absent despite severe hyperglycemia?",
         ["Ketones are excreted too quickly to accumulate", "Residual insulin is enough to suppress lipolysis but not enough to control glucose", "Glucagon secretion is absent in elderly patients", "Severe dehydration prevents ketone formation in the liver", "Hyperosmolality directly inhibits ketone synthesis"], 1,
         "ภาพนี้คือ **HHS** (glucose ≥ 600, effective osm = 2×140 + 980/18 ≈ 334 > 300, pH ≥ 7.3, β-OHB < 3) — **การยับยั้งการสลายไขมันต้องการ insulin น้อยกว่าการดึงน้ำตาลเข้าเซลล์มาก** ผู้ป่วย T2 ที่ยังมี insulin บ้างจึงไม่มี ketone แต่น้ำตาลสูงขึ้นเรื่อย ๆ จนขาดน้ำรุนแรงและซึม\n\n- ketone ไม่ได้ถูกขับเร็วผิดปกติ\n- glucagon ยังหลั่งได้\n- ภาวะขาดน้ำไม่ได้หยุดการสร้าง ketone (osmolality สูงมีส่วนบ้างแต่ไม่ใช่กลไกหลัก)",
         "HHS = insulin น้อยพอหยุดสลายไขมัน แต่ไม่พอคุมน้ำตาล", "HHS", [SRC_ADD], [CRI, CRI1]),
     mcq(N(14), "During treatment of DKA, the urine ketone dipstick changes from 2+ to 3+ while the patient is clinically improving and the anion gap is narrowing. What is the best explanation?",
         ["Treatment is failing and insulin should be doubled", "The nitroprusside test detects acetoacetate but not beta-hydroxybutyrate, which is being converted to acetoacetate", "Ketones are now being produced by the kidney", "The urine is becoming more concentrated", "A new infection has developed"], 1,
         "แผ่นตรวจ ketone ใช้ **nitroprusside** ซึ่งทำปฏิกิริยากับ **acetoacetate** (และ acetone) แต่ **ไม่วัด β-hydroxybutyrate** ซึ่งเป็น ketone หลักใน DKA เมื่อรักษา β-OHB ถูกออกซิไดซ์กลับเป็น acetoacetate ค่าแผ่นตรวจจึงดูแย่ลงทั้งที่ผู้ป่วยดีขึ้น — ติดตามด้วย **anion gap หรือ β-OHB ในเลือด**\n\n- ไม่ต้องเพิ่ม insulin เพราะ AG แคบลงแล้ว\n- ไตไม่ได้สร้าง ketone\n- ความเข้มข้นของปัสสาวะไม่ใช่เหตุหลัก",
         "ติดตาม DKA ด้วย AG/β-OHB ในเลือด ไม่ใช่ urine ketone", "DKA monitoring", [SRC_ADD], [CRI, CRI1])],
    [CRI, CRI1, DM, "B9.2.5(2)"],
    {"dka": fig("DKA เกิดอย่างไร",
        "ขาด insulin ร่วมกับฮอร์โมนต้าน (โดยเฉพาะ **glucagon**) แตกสองกิ่ง — ซ้าย: ตับปล่อยน้ำตาล กล้ามเนื้อใช้ไม่ได้ → glucose สูง → osmotic diuresis → **ขาดน้ำ** · ขวา: ไขมันสลาย FFA ไปตับ → **ketone** → กรด AG สูง → Kussmaul กลิ่นผลไม้ ปวดท้อง",
        F.dka()),
     "dkahhs": fig("ทำไม HHS ไม่มี ketone — insulin สองระดับ",
        "เส้นเขียว: การหยุดสลายไขมัน **ต้องการ insulin น้อย** · เส้นฟ้า: การคุมน้ำตาล **ต้องการ insulin มากกว่า** — **DKA** แทบไม่มี insulin จึงเสียทั้งสองอย่าง (ketone + น้ำตาลสูง) · **HHS** มี insulin บ้าง ไขมันไม่สลาย ไม่มี ketone แต่น้ำตาลสูงมาก (กราฟเชิงหลักการ)",
        F.dkahhs())},
    source=SRC_ADD)

# ───────────────────────────── 8
sec("endo-dm-08", "รักษา DKA/HHS — น้ำก่อน · ดู K ก่อน insulin · ระวังน้ำตาลและ osmolality ลดเร็ว",
    "0.9% NaCl 15–20 mL/kg ชั่วโมงแรก · K < 3.3 ห้ามเริ่ม insulin · insulin 0.1 U/kg/h · เติม dextrose · bicarbonate เมื่อ pH < 6.9", 12,
"""### ลำดับการรักษา (ADA 2009 — ยังเป็นแกนของการสอน · ปรับตาม consensus 2024)
| ขั้น | ทำอะไร | ทำไม |
|---|---|---|
| **1. สารน้ำ** | **0.9% NaCl 15–20 mL/kg/ชม. (1–1.5 ลิตร) ชั่วโมงแรก** · จากนั้นดู corrected Na: ปกติ/สูง → 0.45% NaCl · ต่ำ → 0.9% NaCl 250–500 mL/ชม. | แก้ volume ที่ขาด ~6–9 ลิตร · น้ำอย่างเดียวก็ลดน้ำตาลได้ (เจือจาง + ไตขับ glucose เมื่อเลือดไปไตดีขึ้น) |
| **2. ดู K ก่อนเริ่ม insulin** | K **< 3.3**: ให้ K ก่อน ยังไม่ให้ insulin · **3.3–5.2**: ผสม K 20–30 mEq ต่อสารน้ำ 1 ลิตร · **> 5.2**: ยังไม่ให้ เช็คทุก 2 ชม. | insulin ดัน K เข้าเซลล์ (ภาพด้านล่าง) |
| **3. Insulin** | **regular insulin IV 0.1 U/kg bolus แล้ว 0.1 U/kg/ชม.** (หรือ 0.14 U/kg/ชม. ไม่ต้อง bolus) · เป้าน้ำตาลลด 50–75 mg/dL/ชม. | หยุดการสร้าง ketone — insulin คือยาที่ **แก้กรด** น้ำตาลเป็นผลพลอยได้ |
| **4. เติม dextrose** | glucose ถึง **200 mg/dL (DKA)** หรือ **300 (HHS)** → เปลี่ยนเป็น **D5/0.45% NaCl** และลด insulin เหลือ 0.02–0.05 U/kg/ชม. (consensus 2024: เติม dextrose เมื่อ < 250) | น้ำตาลลดเร็วกว่ากรด ต้อง **ให้ insulin ต่อจนกรดหาย** โดยไม่ให้น้ำตาลต่ำ |
| **5. Bicarbonate** | เฉพาะ **pH < 6.9** | ให้เกินทำให้ K ต่ำ · กรดในสมองแย่ลง · ketone แก้ได้เองด้วย insulin |
| **6. Phosphate** | ไม่ให้เป็นประจำ (ให้เมื่อ < 1.0 mg/dL, หัวใจ/การหายใจแย่) | — |

### ทำไม K ถึงต้องระวังที่สุด
[[fig:kshift]]

### เมื่อไรถือว่าหาย และเปลี่ยนเป็น insulin ใต้ผิวหนัง
- **DKA หาย (ADA 2009)**: glucose < 200 ร่วมกับ 2 ใน 3 ข้อ — **HCO₃ ≥ 15 · venous pH > 7.3 · AG ≤ 12** (consensus 2024: β-OHB < 0.6 mmol/L และ pH ≥ 7.3 หรือ HCO₃ ≥ 18)
- **HHS หาย**: osmolality ปกติ และ **รู้สึกตัวดี**
- **ฉีด basal insulin ใต้ผิวหนัง 1–2 ชั่วโมงก่อนหยุด IV insulin** — insulin IV มีครึ่งชีวิตเพียงไม่กี่นาที ถ้าหยุดก่อนยาใต้ผิวหนังออกฤทธิ์ DKA จะกลับมา

### HHS ต่างจาก DKA ตรงไหน
สารน้ำสำคัญที่สุด (ขาดน้ำมากกว่า) · insulin เริ่มได้เมื่อน้ำตาลไม่ลดด้วยน้ำอย่างเดียว ขนาดต่ำกว่า · **ลด osmolality ช้า ๆ** (ไม่ให้ลดเร็วจนน้ำเข้าเซลล์สมอง) · ป้องกันลิ่มเลือด (เลือดข้น นอนนาน)

**ภาวะแทรกซ้อนจากการรักษา**: K ต่ำ · น้ำตาลต่ำ · **สมองบวม** (โดยเฉพาะเด็ก — osmolality ลดเร็วเกิน) · hyperchloremic acidosis จาก NaCl ปริมาณมาก
""",
    ["ขั้นแรก 0.9% NaCl 15–20 mL/kg (1–1.5 ลิตร) ชั่วโมงแรก · ต่อด้วย 0.45% หรือ 0.9% ตาม corrected Na",
     "K < 3.3 ให้ K ก่อนห้ามเริ่ม insulin · 3.3–5.2 ผสม K 20–30 mEq/L · > 5.2 เช็คทุก 2 ชม.",
     "Insulin 0.1 U/kg/h · glucose 200 (DKA)/300 (HHS) เติม dextrose ลด insulin แต่อย่าหยุดจนกรดหาย",
     "Bicarbonate เฉพาะ pH < 6.9 · หาย = glucose < 200 + HCO₃ ≥ 15, pH > 7.3, AG ≤ 12 (2 ใน 3)",
     "ฉีด basal SC 1–2 ชม. ก่อนหยุด IV insulin"],
    [mcq(N(15), "A 19-year-old with DKA (pH 7.10, glucose 520 mg/dL) has received 1 L of 0.9% saline. Serum potassium is 3.0 mEq/L. What is the most appropriate next step?",
         ["Start an IV insulin infusion at 0.1 U/kg/h immediately", "Give IV potassium and delay insulin until potassium is at least 3.3 mEq/L", "Give sodium bicarbonate", "Start subcutaneous insulin glargine", "Withhold fluids until potassium is corrected"], 1,
         "ใน DKA K ทั้งร่างกายพร่องอยู่แล้ว — **insulin จะดัน K เข้าเซลล์** ถ้าเริ่มตอน K 3.0 จะลดต่อจนเกิดหัวใจเต้นผิดจังหวะ จึงต้อง **ให้ K ก่อนจน ≥ 3.3** แล้วค่อยเริ่ม insulin (สารน้ำให้ต่อได้)\n\n- เริ่ม insulin ทันทีอันตราย\n- bicarbonate ใช้เฉพาะ pH < 6.9 และยิ่งทำให้ K ต่ำ\n- SC glargine ไม่ใช่การรักษาหลักของ DKA ระยะแรก\n- ไม่ควรหยุดสารน้ำ",
         "DKA: K < 3.3 → ให้ K ก่อน ยังไม่เริ่ม insulin", "DKA treatment", ["ADA 2009 hyperglycemic crises — ไม่อยู่ในสไลด์"], [CRI, CRI1, "B9.4(2)"]),
     mcq(N(16), "Six hours into DKA treatment, glucose is 190 mg/dL but bicarbonate is 12 mEq/L and the anion gap is 20. What should be done with the insulin infusion?",
         ["Stop insulin because glucose is normal", "Continue insulin (reduced dose) and add dextrose to the IV fluid until the ketoacidosis resolves", "Switch to oral metformin", "Double the insulin rate", "Give bicarbonate and stop insulin"], 1,
         "น้ำตาลลดเร็วกว่ากรด — insulin เป็นยาที่ **หยุดการสร้าง ketone** จึงต้อง **ให้ต่อจนกรดหาย** (HCO₃ ≥ 15, pH > 7.3, AG ≤ 12) โดย **ลดขนาด insulin และเติม dextrose** ในสารน้ำเพื่อไม่ให้น้ำตาลต่ำ\n\n- หยุด insulin ตอนนี้ DKA จะกลับมา\n- metformin ไม่มีบทบาทใน DKA\n- เพิ่ม insulin เป็นสองเท่าทำให้น้ำตาลต่ำ\n- bicarbonate ไม่จำเป็นที่ระดับนี้",
         "น้ำตาลลงแล้วแต่ AG ยังกว้าง → ลด insulin + เติม dextrose ห้ามหยุด", "DKA treatment", ["ADA 2009 hyperglycemic crises — ไม่อยู่ในสไลด์"], [CRI, CRI1, "B9.4(2)"])],
    [CRI, CRI1, "B9.4(2)", "B9.2.5(2)", DRUG],
    {"kshift": fig("K ใน DKA — ปกติในเลือด แต่พร่องทั้งร่างกาย",
        "ซ้าย: ขาด insulin กรด และ osmolality สูง ดึง K ออกจากเซลล์ K ในเลือดจึงดูปกติหรือสูง ขณะที่ปัสสาวะขับทิ้งไปมาก · ขวา: เมื่อให้ insulin และแก้กรด K ถูกดันกลับเข้าเซลล์ ระดับในเลือดดิ่ง — แถบล่างคือเกณฑ์ของ ADA 2009 (JBDS ของอังกฤษใช้ 3.5)",
        F.kshift())},
    source=SRC_ADD)

# ───────────────────────────── 9
sec("endo-dm-09", "Hypoglycemia — อาการเตือน สมองขาดน้ำตาล และ unawareness",
    "Whipple triad · ADA level 1–3 · adrenergic vs neuroglycopenic · SU/insulin/ไตเสื่อม · กฎ 15 · glucagon", 10,
"""> สไลด์ระบุ hypoglycemia เป็นภาวะแทรกซ้อนเฉียบพลัน และเป็นผลข้างเคียงของ **SU และ insulin** ในตารางยา — รายละเอียดเรียบเรียงจาก ADA Standards of Care

### นิยาม
**Whipple triad**: ① อาการเข้ากับน้ำตาลต่ำ ② วัดน้ำตาลได้ต่ำ ③ อาการหายเมื่อให้น้ำตาล
| ระดับ (ADA) | เกณฑ์ |
|---|---|
| **Level 1** | glucose **< 70 mg/dL** (และ ≥ 54) |
| **Level 2** | glucose **< 54 mg/dL** |
| **Level 3** | รุนแรง — สับสนหรือหมดสติจน **ต้องมีคนช่วย** (ไม่ขึ้นกับตัวเลข) |

### ร่างกายตอบสนองเป็นลำดับ
[[fig:hypo_ladder]]

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก |
|---|---|
| **ใจสั่น มือสั่น วิตกกังวล** | ระบบ sympathetic หลั่ง **adrenaline** (adrenergic) |
| **เหงื่อแตก หิว** | sympathetic ชนิด **cholinergic** — ยา β-blocker **บังใจสั่น/มือสั่น แต่ไม่บังเหงื่อ** |
| **สับสน พูดไม่ชัด พฤติกรรมแปลก ชัก หมดสติ** | สมองใช้ glucose เป็นพลังงานหลักและเก็บสำรองไม่ได้ (**neuroglycopenic**) |
| **Hypoglycemia unawareness** | น้ำตาลต่ำบ่อยทำให้เกณฑ์ที่ร่างกายหลั่ง adrenaline เลื่อนต่ำลง → สมองขาดน้ำตาลก่อนจะมีอาการเตือน · พบมากใน T1 นาน และ autonomic neuropathy · แก้ได้โดย **หลีกเลี่ยงน้ำตาลต่ำ 2–3 สัปดาห์** และผ่อนเป้าน้ำตาล |

### สาเหตุในผู้ป่วยเบาหวาน
| สาเหตุ | กลไก |
|---|---|
| **Insulin** · **sulfonylurea** (โดยเฉพาะ glibenclamide) | กระตุ้น insulin โดยไม่ขึ้นกับระดับน้ำตาล — SU ออกฤทธิ์ยาวและสะสมเมื่อไตเสื่อม → **น้ำตาลต่ำซ้ำนานหลายวัน** |
| อดอาหาร/กินน้อย · ออกกำลังมาก | ความต้องการ insulin ลดแต่ขนาดยาเท่าเดิม · กล้ามเนื้อดึงน้ำตาลเองได้ขณะออกกำลัง |
| **แอลกอฮอล์** | ยับยั้ง gluconeogenesis ของตับ |
| **ไตเสื่อม** | insulin ถูกกำจัดช้า · ไตสร้างน้ำตาลได้น้อยลง |

### การรักษา
- **รู้สึกตัว กลืนได้**: glucose **15–20 กรัม** (น้ำหวาน/ลูกอม/glucose tablet) **ตรวจซ้ำใน 15 นาที** ถ้ายังต่ำให้ซ้ำ ("กฎ 15") แล้วตามด้วยอาหารมื้อหลัก · ผู้ที่ใช้ acarbose ต้องใช้ **glucose** (ยายับยั้งการย่อย sucrose)
- **ไม่รู้สึกตัว**: **50% glucose 25–50 mL IV** หรือ **glucagon 1 mg IM/SC** (glucagon ใช้ไม่ได้ผลถ้า glycogen หมด เช่น ติดสุรา อดอาหารนาน)
- **น้ำตาลต่ำจาก SU**: รับไว้ในโรงพยาบาล ให้ dextrose ต่อเนื่อง เฝ้าระวัง 24–72 ชม. (พิจารณา octreotide) — ห้ามกลับบ้านทันทีแม้ฟื้นแล้ว
""",
    ["Whipple triad · level 1 < 70 · level 2 < 54 · level 3 ต้องมีคนช่วย",
     "ลำดับ: ~80 หยุดหลั่ง insulin → ~65–70 glucagon/adrenaline → ~55 อาการเตือน → < 50 สมองขาดน้ำตาล",
     "β-blocker บังใจสั่น/มือสั่น แต่ไม่บังเหงื่อ (cholinergic)",
     "Unawareness: เกณฑ์อาการเตือนเลื่อนลง — หลีกเลี่ยงน้ำตาลต่ำ 2–3 สัปดาห์",
     "รักษา: กฎ 15 (15–20 g, ตรวจซ้ำ 15 นาที) · ไม่รู้สึกตัว 50% glucose หรือ glucagon 1 mg · SU → admit"],
    [mcq(N(17), "A 74-year-old man with CKD (eGFR 25) taking glibenclamide is found confused with glucose 38 mg/dL. He wakes up after 50 mL of 50% glucose. What is the most appropriate disposition?",
         ["Discharge home with advice to eat more", "Admit for continuous dextrose infusion and monitoring for recurrent hypoglycemia over the next 24–72 hours", "Give glucagon and discharge", "Double the glibenclamide dose but take it with food", "Switch to insulin glargine and discharge"], 1,
         "**glibenclamide** ออกฤทธิ์ยาวและสาร/ยาสะสมเมื่อไตเสื่อม — หลังฟื้นจาก D50 น้ำตาล **จะต่ำซ้ำได้อีกหลายครั้งในวันถัด ๆ ไป** จึงต้อง **รับไว้ ให้ dextrose ต่อเนื่อง และเฝ้าระวัง 24–72 ชม.** (พิจารณา octreotide) แล้วหยุด SU\n\n- กลับบ้านทันทีอันตราย\n- glucagon ออกฤทธิ์สั้น และ SU กระตุ้น insulin ต่อ\n- เพิ่ม SU ผิดชัด\n- การเปลี่ยนยาทำหลังผ่านช่วงเสี่ยงแล้ว",
         "SU + ไตเสื่อม + hypoglycemia = admit เฝ้าระวัง 24–72 ชม.", "Hypoglycemia", ["ADA Standards of Care — ไม่อยู่ในสไลด์ · สไลด์: SU ทำให้ hypoglycemia"], [HYPO, DRUG]),
     mcq(N(18), "A patient with type 1 diabetes started propranolol for migraine prophylaxis. During a hypoglycemic episode, which symptom is most likely still preserved?",
         ["Palpitations", "Tremor", "Sweating", "Anxiety", "Tachycardia"], 2,
         "**เหงื่อ** ในภาวะน้ำตาลต่ำเกิดจาก sympathetic ชนิด **cholinergic** (acetylcholine ที่ต่อมเหงื่อ) β-blocker จึงไม่บัง — ส่วน **ใจสั่น มือสั่น ชีพจรเร็ว วิตกกังวล** เป็นผลของ adrenaline ผ่าน β receptor จึงถูกบังได้ ทำให้ผู้ป่วยรู้ตัวช้า\n\nสอนผู้ป่วยที่ใช้ β-blocker ว่า **เหงื่อแตกโดยไม่มีเหตุ = ให้เจาะน้ำตาล**",
         "β-blocker บัง adrenergic แต่ไม่บังเหงื่อ (cholinergic)", "Hypoglycemia", ["หลักสรีรวิทยา — ไม่ได้อยู่ในสไลด์"], [HYPO])],
    [HYPO, DRUG, "3.1.17", "B11.3(1)"],
    {"hypo_ladder": fig("เมื่อน้ำตาลลดลง ร่างกายตอบสนองเป็นลำดับ",
        "ราว **80** ตับอ่อนหยุดหลั่ง insulin → **65–70** glucagon และ adrenaline หลั่ง → **55–60** อาการเตือน (adrenergic) → **< 50** สมองขาดน้ำตาล → **~30** ชัก หมดสติ (ตัวเลขโดยประมาณตามสรีรวิทยา) · ลูกศรประ: ผู้ที่น้ำตาลต่ำบ่อย เกณฑ์อาการเตือนเลื่อนลงจนสมองขาดน้ำตาลก่อนรู้ตัว",
        F.hypo_ladder())},
    source="ADA Standards of Care · Cryer (ไม่อยู่ในสไลด์)")

# ───────────────────────────── 10
sec("endo-dm-10", "Diabetic retinopathy — จาก microaneurysm ถึงหลอดเลือดใหม่ที่เปราะ",
    "pericyte หาย → รั่ว → macular edema · ขาดเลือด → VEGF → PDR · ตรวจตา T2 ตั้งแต่วินิจฉัย T1 หลัง 5 ปี", 9,
"""### ปัจจัยเสี่ยงของภาวะแทรกซ้อนหลอดเลือดเล็ก (สไลด์)
ระยะเวลาที่เป็นเบาหวาน · น้ำตาลสูง · **ความดันสูง** · ประวัติครอบครัว

### Retinopathy (สไลด์)
- การเปลี่ยนแปลงจำเพาะของหลอดเลือดเล็กที่จอตา
- **ราว 20% ของผู้ป่วยเบาหวานรายใหม่มี retinopathy แล้วตอนวินิจฉัย**
- แบ่งเป็น **non-proliferative (NPDR)** และ **proliferative (PDR)**

[[fig:retina]]

#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก | ผลต่อการมองเห็น |
|---|---|---|
| **Microaneurysm** | น้ำตาลสูงทำลาย **pericyte** ที่ค้ำผนังหลอดเลือดฝอย ผนังอ่อนแอโป่งออก | ไม่มีอาการ |
| **จุดเลือด (dot–blot hemorrhage)** | ผนังที่โป่งแตก เลือดออกในชั้นลึกของจอตา | ไม่มีอาการ |
| **Hard exudate** | ผนังรั่ว ไขมันและโปรตีนตกค้าง | ถ้าอยู่ที่ macula ตามัว |
| **Macular edema** | น้ำรั่วสะสมที่ **macula** (จุดรับภาพชัด) | **ตามัว** ได้แม้เป็นแค่ NPDR — สไลด์: NPDR ไม่ทำให้ตามัวเว้นแต่ macula เสีย |
| **หลอดเลือดใหม่ (neovascularization)** | หลอดเลือดฝอยปิด จอตา **ขาดเลือด** → หลั่ง **VEGF** → หลอดเลือดใหม่งอก ซึ่ง **เปราะ** | — |
| **เลือดออกในวุ้นตา · จอตาลอก** | หลอดเลือดใหม่แตก · พังผืดที่งอกตามดึงจอตา | **ตามัวทันที เห็นเงาดำ** — สูญเสียการมองเห็น |

### รักษาและป้องกัน (สไลด์)
- **Laser** — หยุดหลอดเลือดงอก ป้องกันเลือดออก **แต่ไม่คืนการมองเห็นที่เสียไป** (หลักการ: ทำลายจอตาส่วนที่ขาดเลือดเพื่อลด VEGF)
- คุมน้ำตาลเข้มงวด **HbA1c < 6.5–7%** · คุมความดันให้ปกติ
- ปัจจุบัน **ยาฉีดเข้าวุ้นตา anti-VEGF** เป็นหลักของ macular edema และใช้ใน PDR (ไม่อยู่ในสไลด์)

### ตรวจคัดกรอง (สไลด์)
| ชนิด | เริ่มตรวจตา | จากนั้น |
|---|---|---|
| **Type 2** | **ตั้งแต่วินิจฉัย** | ทุกปี |
| **Type 1** | **5 ปีหลังวินิจฉัย** | ทุกปี |
ตรวจถี่ขึ้นถ้า retinopathy กำลังแย่ลง · T2 ต้องตรวจทันทีเพราะเป็นมาหลายปีก่อนรู้ตัว ส่วน T1 รู้วันเริ่มโรคชัดเจน
""",
    ["Risk factors micro: duration · hyperglycemia · HT · family history · 20% มี retinopathy ตอนวินิจฉัย",
     "NPDR: microaneurysm (pericyte หาย) · dot-blot · exudate · macular edema (ตามัวได้)",
     "PDR: ขาดเลือด → VEGF → หลอดเลือดใหม่เปราะ → เลือดออกในวุ้นตา จอตาลอก",
     "Laser หยุดหลอดเลือดงอก ไม่คืนการมองเห็น · คุม A1c < 6.5–7 + BP · ปัจจุบันมี anti-VEGF",
     "ตรวจตา: T2 ตั้งแต่วินิจฉัย · T1 หลัง 5 ปี · แล้วทุกปี"],
    [mcq(N(19), "Which mechanism directly drives the formation of new fragile vessels in proliferative diabetic retinopathy?",
         ["Loss of pericytes causing microaneurysms", "Retinal ischemia from capillary closure stimulating VEGF release", "Lipid deposition forming hard exudates", "Osmotic swelling of the lens", "Increased intraocular pressure"], 1,
         "หลอดเลือดฝอยปิดทำให้ **จอตาขาดเลือด** เซลล์ที่ขาดออกซิเจนหลั่ง **VEGF** กระตุ้นให้หลอดเลือดใหม่งอก ซึ่งเปราะและแตกง่าย = **PDR** (นี่คือเหตุผลที่ laser และ anti-VEGF ได้ผล)\n\n- **pericyte หาย** ทำให้เกิด microaneurysm ซึ่งเป็นระยะ NPDR\n- **hard exudate** เป็นผลของการรั่ว\n- เลนส์บวมทำให้ค่าสายตาเปลี่ยน\n- ความดันตาสูงไม่ใช่กลไกนี้ (แต่ neovascular glaucoma เป็นผลตามมาได้)",
         "PDR = ขาดเลือด → VEGF → หลอดเลือดใหม่", "Retinopathy", R("Proliferative retinopathy"), ["2.3.7-3(7)", "B3.2.10-3(3)"]),
     mcq(N(20), "When should retinal screening start in a 12-year-old diagnosed with type 1 diabetes today, compared with a 50-year-old diagnosed with type 2 diabetes today?",
         ["Both at diagnosis", "Type 1: 5 years after diagnosis; type 2: at diagnosis", "Type 1: at diagnosis; type 2: after 5 years", "Both after 5 years", "Only when visual symptoms appear"], 1,
         "สไลด์: **T2 ตรวจตาตั้งแต่วินิจฉัย** แล้วทุกปี (เพราะมักเป็นมาหลายปีก่อนรู้ตัว ~20% มี retinopathy แล้ว) · **T1 เริ่มตรวจ 5 ปีหลังวินิจฉัย** แล้วทุกปี (เริ่มโรคชัดเจน retinopathy ต้องใช้เวลา)\n\n- รอให้มีอาการไม่ได้ เพราะ NPDR ไม่มีอาการ",
         "ตรวจตา: T2 ตั้งแต่วินิจฉัย · T1 หลัง 5 ปี", "Retinopathy screening", R("Screening diabetic retinopathy"), ["2.3.7-3(7)", DM])],
    ["2.3.7-3(7)", "B3.2.10-3(3)", DM],
    {"retina": fig("จอประสาทตาในเบาหวาน — 4 ระยะ",
        "**ปกติ** · **NPDR** microaneurysm จุดเลือด exudate ยังมองเห็นปกติ · **macular edema** น้ำรั่วรอบ macula ทำให้ตามัวแม้ยังไม่ถึง PDR · **PDR** หลอดเลือดใหม่ (เส้นหยัก) เปราะ แตกเป็นเลือดออกก้อนใหญ่ (ภาพวาดเชิงหลักการ — ภาพจอตาจริงอยู่ในสไลด์)",
        F.retina())})

# ───────────────────────────── 11
sec("endo-dm-11", "Diabetic nephropathy — hyperfiltration ถึงไตวาย และยาที่ลดแรงดันใน glomerulus",
    "5 ระยะ · microalbuminuria 30–300 · UACR ทุกปี · BP < 130/80 · ACEi/ARB · SGLT2i", 11,
"""### ภาพรวม (สไลด์)
- glomerulus เสื่อม → albumin/โปรตีนรั่ว
- **สาเหตุอันดับ 1 ของไตวายระยะสุดท้าย (35% ของ ESRD)**
- 20–30% ของผู้ป่วย T1/T2 มีหลักฐานของโรคไต แต่ใน T2 ส่วนน้อยกว่าที่ไปถึง ESRD
- **อัตราตาย 90% ถ้าอยู่ใน ESRD เกิน 10 ปี**

### 5 ระยะ (สไลด์)
[[fig:dn_stages]]

| ระยะ | เริ่มเมื่อ | ชื่อ | การเปลี่ยนแปลงที่ไต |
|---|---|---|---|
| 1 | ตอนวินิจฉัย | **Hyperfunction** | GFR ↑ |
| 2 | 2–3 ปี | **"Silent"** | GFR ↑ · **GBM หนาขึ้น** |
| 3 | > 5 ปี | **Incipient DN** | **Microalbuminuria** |
| 4 | > 10 ปี | **Overt DN** | **Clinical proteinuria** · GFR ↓ |
| 5 | > 15 ปี | **Uremia** | GFR < 10 mL/min |

#### ทำไมถึงเกิด — กลไกของแต่ละระยะ
| ระยะ | กลไก |
|---|---|
| **GFR สูงช่วงแรก** | glucose ที่ถูกกรองมาก ทำให้ proximal tubule ดูด glucose พร้อม Na ผ่าน **SGLT2 มากขึ้น** → Na ไปถึง **macula densa** น้อย → ไตเข้าใจว่าเลือดมาน้อย จึง **ขยาย afferent arteriole** (tubuloglomerular feedback) ร่วมกับ angiotensin II **หด efferent** → แรงดันใน glomerulus สูง |
| **GBM หนา · mesangium ขยาย** | น้ำตาลจับโปรตีนเป็น AGEs + แรงดันสูงกระตุ้น TGF-β → สร้าง matrix มาก → **Kimmelstiel–Wilson nodule** (nodular glomerulosclerosis) |
| **Albumin รั่ว** | podocyte บาดเจ็บจากแรงดันและ AGEs · ประจุลบของตะแกรงลดลง (ทวนคาบ glomerular — Nephro คาบ 14) |
| **GFR ลดจนไตวาย** | glomerulus กลายเป็นแผลเป็นทีละหน่วย nephron ที่เหลือกรองหนักขึ้นอีก — วงจรเดียวกับ FSGS แบบปรับตัว |

[[fig:renoprot]]

### Albuminuria (สไลด์)
- **Microalbuminuria = 30–300 mg/24 ชม.** · ตรวจปัสสาวะเช้าเป็น **UACR 30–300 mg albumin/g creatinine**
- **ทำนายการเกิด DN และการตายจากโรคหัวใจ**
- **ต้องตัด UTI ออกก่อน** วินิจฉัยว่าเป็นโรคไต (ไข้ ออกกำลังหนัก หัวใจล้มเหลว ก็ทำให้บวกชั่วคราว — ต้องผิดปกติ 2 ใน 3 ครั้งใน 3–6 เดือน)

### คัดกรอง (สไลด์)
T2 **ตั้งแต่วินิจฉัย** · T1 **หลังเป็น 3–5 ปี** · ตรวจ **UACR และ serum creatinine ทุกปี**

### รักษา
**สไลด์**: คุมความดัน **< 130/80 mmHg** · **ACEi หรือ ARB** — ใช้รักษา microalbuminuria, proteinuria และความดันสูง และ **ใช้ได้แม้ความดันปกติ** · HbA1c < 6.5–7% · โปรตีนปริมาณปานกลาง
**แนวทางปัจจุบัน (KDIGO 2022 / ADA — ไม่อยู่ในสไลด์)**: **SGLT2i** ใน T2 ที่มี CKD (เริ่มได้เมื่อ eGFR ≥ 20) · **finerenone** เมื่อยังมี albuminuria · GLP-1RA ช่วยเพิ่ม · metformin ลดขนาดเมื่อ eGFR 30–44 และหยุดเมื่อ < 30 · creatinine ขึ้นไม่เกิน 30% หลังเริ่ม ACEi/ARB หรือ SGLT2i **ไม่ต้องหยุดยา**
""",
    ["DN = สาเหตุ ESRD อันดับ 1 (35%) · ESRD > 10 ปี ตาย 90%",
     "5 ระยะ: hyperfunction (GFR ↑) → silent (GBM หนา) → microalbuminuria (> 5 ปี) → overt (> 10 ปี) → uremia (> 15 ปี)",
     "Hyperfiltration: SGLT2 ดูด Na มาก → macula densa → afferent ขยาย + Ang II หด efferent",
     "Microalbuminuria 30–300 mg/วัน (UACR 30–300 mg/g) · ตัด UTI ก่อน · คัดกรอง T2 ตั้งแต่วินิจฉัย T1 หลัง 3–5 ปี",
     "BP < 130/80 · ACEi/ARB แม้ BP ปกติ · ปัจจุบัน + SGLT2i (eGFR ≥ 20) · Cr ขึ้น ≤ 30% ไม่ต้องหยุด"],
    [mcq(N(21), "A 58-year-old man with type 2 diabetes and UACR 420 mg/g is started on losartan. Two weeks later creatinine rises from 1.20 to 1.40 mg/dL and potassium is 4.8 mEq/L. What is the best action?",
         ["Stop losartan because of acute kidney injury", "Continue losartan; a rise in creatinine of up to about 30% reflects reduced intraglomerular pressure", "Switch losartan to an ACE inhibitor plus ARB combination", "Add a thiazide to lower creatinine", "Order a renal biopsy"], 1,
         "creatinine ขึ้น **17%** (1.20 → 1.40) หลังเริ่ม ARB เป็นผลที่คาดได้ — ARB คลาย **efferent arteriole** แรงดันใน glomerulus ลด GFR จึงลดเล็กน้อยช่วงแรก ซึ่งเป็นกลไกเดียวกับที่ปกป้องไตระยะยาว — **ขึ้นไม่เกินราว 30% และ K ไม่สูงมาก ให้ยาต่อ**\n\n- หยุดยาจะเสียประโยชน์ป้องกันไต\n- ACEi + ARB ร่วมกันเพิ่ม AKI และ K สูงโดยไม่ได้ประโยชน์\n- thiazide ไม่ได้ลด creatinine\n- ไม่มีข้อบ่งชี้เจาะไต (ภาพเข้ากับ DN)",
         "Cr ขึ้น ≤ 30% หลัง ACEi/ARB/SGLT2i = แรงดันใน glomerulus ลด → ให้ยาต่อ", "Diabetic nephropathy", R("Treatment diabetic nephropathy — ACEI or ARB"), [DM, "2.3.14(3)", "B9.2.7(2)"]),
     mcq(N(22), "A woman with type 2 diabetes has a single spot UACR of 64 mg/g on a routine visit; urinalysis shows pyuria and nitrite positive and she has dysuria. What is the most appropriate approach?",
         ["Diagnose diabetic nephropathy and start an ACE inhibitor", "Treat the urinary tract infection and repeat the UACR later; confirm with 2 of 3 abnormal samples", "Order a kidney biopsy", "Ignore albuminuria in diabetes", "Start finerenone"], 1,
         "สไลด์ย้ำว่า **ต้องตัด UTI ออกก่อน** วินิจฉัย diabetic nephropathy — การติดเชื้อ (รวมถึงไข้ ออกกำลังหนัก HF) ทำให้ albumin รั่วชั่วคราว จึงรักษา UTI แล้วตรวจซ้ำ และวินิจฉัยเมื่อผิดปกติ **2 ใน 3 ครั้งในช่วง 3–6 เดือน**\n\n- เริ่มยาจากค่าครั้งเดียวที่มี UTI ยังเร็วเกิน\n- ไม่มีข้อบ่งชี้เจาะไต\n- albuminuria สำคัญมาก ไม่ควรละเลย",
         "UACR ผิดปกติ: ตัด UTI/ไข้/ออกกำลัง แล้วยืนยัน 2 ใน 3 ครั้ง", "Albuminuria", R("Albuminuria — rule out UTI"), [DM, "2.3.14(3)", "3.1.6"])],
    [DM, "2.3.14(3)", "B9.2.7(2)", "3.1.6"],
    {"dn_stages": fig("5 ระยะของ diabetic nephropathy",
        "เส้น GFR: **สูงขึ้นช่วงแรก** (hyperfiltration) คงที่ระยะเงียบ แล้ว **ลดเร็ว** หลังมี overt proteinuria จนถึง uremia · แถบล่าง: albumin ในปัสสาวะ ปกติ → **micro 30–300** → **overt > 300 mg/วัน** — ช่วงเวลาตามตารางในสไลด์",
        F.dn_stages()),
     "renoprot": fig("ทำไม ACEi/ARB และ SGLT2i ปกป้องไต",
        "**เบาหวาน**: afferent ขยาย (SGLT2 ดูด Na มาก macula densa เห็น Na น้อย) + efferent หด (angiotensin II) → แรงดันใน glomerulus สูง · **ACEi/ARB** คลาย efferent · **SGLT2i** ทำให้ Na ถึง macula densa มากขึ้น afferent หดกลับ — ทั้งสองลดแรงดัน Cr จึงขึ้นเล็กน้อยช่วงแรก",
        F.renoprot())})

# ───────────────────────────── 12
sec("endo-dm-12", "Diabetic neuropathy และเท้าเบาหวาน — ทำไมแผลเกิดโดยไม่เจ็บ",
    "stocking–glove · autonomic · mononeuropathy · high-risk foot · Charcot · monofilament · ดูแลเท้าทุกวัน", 11,
"""### ชนิดของ neuropathy (สไลด์)
- **Peripheral** — พบบ่อยที่สุดของภาวะแทรกซ้อนเบาหวาน: polyneuropathy และ mononeuropathy
- **Autonomic** — มักมาพร้อม peripheral: ทางเดินอาหาร ทางเดินปัสสาวะ หัวใจและหลอดเลือด

### Peripheral neuropathy (สไลด์)
- แบบ **"stocking and glove"** สองข้าง · พบ **1 ใน 4** ของผู้ป่วยเบาหวาน
- ร่วมกับโรคหลอดเลือดทำให้เกิด **แผลและการตัดขา** · **5% เกิดแผลที่เท้า** · **ครึ่งหนึ่งของการตัดขาเกี่ยวกับเบาหวาน**

[[fig:neuro]]

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก |
|---|---|
| **ชาเป็นรูปถุงเท้า–ถุงมือ** | เส้นประสาทเสื่อมแบบ **ขึ้นกับความยาว** — แอกซอนที่ยาวที่สุด (ไปปลายเท้า) ต้องลำเลียงสารอาหารไกลที่สุด จึงเสียก่อน · เมื่อชาขึ้นถึงระดับเข่าจึงเริ่มที่ปลายนิ้วมือ (ความยาวพอกัน) |
| **ปวดแสบร้อน เข็มทิ่ม แย่ตอนกลางคืน** (สไลด์) | เส้นใยเล็ก (small fiber) เสียก่อนและส่งสัญญาณผิดปกติเอง · กลางคืนไม่มีสิ่งเร้าอื่นมากลบ |
| **รับรู้ความเจ็บและอุณหภูมิลดลง** | small fiber หายไป → เหยียบของมีคม รองเท้ากัด น้ำร้อนลวก โดยไม่รู้ตัว |
| **ตาปลา (callus) เท้าผิดรูป** (สไลด์) | motor neuropathy ทำให้กล้ามเนื้อเล็กในเท้าอ่อน นิ้วงอ (claw toe) น้ำหนักลงที่หัวกระดูกฝ่าเท้า → callus → แผลใต้ callus |
| **ผิวเท้าแห้ง แตก** | autonomic neuropathy ทำให้เหงื่อไม่ออก ผิวแตกเป็นทางให้เชื้อเข้า |
| **กลไกที่ทำให้เส้นประสาทเสีย** | น้ำตาลสูง → polyol (sorbitol) สะสม · AGEs · oxidative stress · หลอดเลือดเล็กที่เลี้ยงเส้นประสาท (vasa nervorum) ตีบ |

**Autonomic neuropathy**: กระเพาะบีบตัวช้า (อิ่มเร็ว อาเจียน น้ำตาลแกว่ง) · ท้องเสียกลางคืน · กระเพาะปัสสาวะไม่บีบตัว (ปัสสาวะค้าง ติดเชื้อ) · หย่อนสมรรถภาพทางเพศ · **ความดันตกเมื่อลุกยืน** · ชีพจรเร็วขณะพัก · **MI แบบไม่เจ็บ** · น้ำตาลต่ำโดยไม่รู้ตัว
**Mononeuropathy** (ไม่อยู่ในรายละเอียดสไลด์): carpal tunnel · **CN III palsy ที่รูม่านตาปกติ** — หลอดเลือดที่เลี้ยงแกนกลางเส้นประสาทอุดตัน ขณะที่ใยประสาทรูม่านตาอยู่ผิวนอกได้เลือดจากหลอดเลือดผิวจึงรอด (ต่างจากเส้นเลือดโป่งพองที่กดจากด้านนอกจนรูม่านตาขยาย)

### เท้าเสี่ยงสูง (high-risk foot — สไลด์)
**peripheral neuropathy · PVD · เคยเป็นแผล · เท้าผิดรูป** → ตรวจด้วย **monofilament 10 กรัม** (ร่วมกับ vibration 128 Hz, ankle reflex, คลำชีพจร, ABI)
- **Neuropathic ulcer**: ใต้หัวกระดูกฝ่าเท้า ส้นเท้า ขอบแผลมี callus ไม่เจ็บ ชีพจรคลำได้
- **Charcot arthropathy**: เท้าบวม แดง อุ่น มักไม่เจ็บ → กระดูกและข้อเท้ายุบ (rocker-bottom) — เพราะรับรู้ความเจ็บไม่ได้จึงลงน้ำหนักบนกระดูกที่หักซ้ำ ๆ ร่วมกับ autonomic neuropathy ทำให้เลือดไปกระดูกมากจนกระดูกบาง · ต้องแยกจาก cellulitis/osteomyelitis

### รักษาและป้องกัน (สไลด์)
- คุมน้ำตาลและความดัน · **ยาลดปวด**: tricyclic antidepressant · anticonvulsant · ยาทา (salicylate, **capsaicin**) — ปัจจุบัน ADA ให้ pregabalin, duloxetine, gabapentin เป็นยาแรก
- **ป้องกันแผลที่เท้า**: สอนดูแลเท้า · **ตรวจเท้าทุกวัน** · รองเท้าที่เหมาะสม · คุมเบาหวาน · **เลิกบุหรี่** · หาเท้าเสี่ยงสูงแต่เนิ่น ๆ
- **รองเท้าที่ดี 6 ข้อ**: มีเชือก/สายรัด · วัดขนาดพอดี · หัวกว้างและลึก · ส้นแข็งหุ้มกระชับ · ส้นเตี้ยกว้าง (≤ 1 นิ้ว) · พื้นแข็งแต่งอได้ตรงฝ่าเท้าและนุ่ม
- **ดูแลเท้าทุกวัน**: ล้างและเช็ดให้แห้ง (โดยเฉพาะซอกนิ้ว) · ทาครีมผิวแห้งโดยเฉพาะส้น · ตาปลาใช้หินขัด · **ตัดเล็บตรง ไม่สั้นเกิน** · ตรวจเท้าทุกวันเทียบขนาด สี อุณหภูมิ · **ห้ามเดินเท้าเปล่า** · ใส่รองเท้าพอดีและตรวจรองเท้าก่อนใส่ทุกวัน
""",
    ["Neuropathy พบบ่อยสุด · stocking–glove 1 ใน 4 · 5% เกิดแผลเท้า · ครึ่งหนึ่งของการตัดขา",
     "เส้นยาวสุดเสียก่อน (length-dependent) · small fiber → ปวดแสบร้อนกลางคืน และไม่รู้สึกเจ็บ",
     "Motor → claw toe → callus → แผล · Autonomic → ผิวแห้งแตก · PAD → หายช้า",
     "High-risk foot: neuropathy · PVD · เคยเป็นแผล · deformity → monofilament 10 g ทุกปี",
     "CN III palsy ในเบาหวาน รูม่านตาปกติ (ischemic core) · Charcot = เท้าบวมแดงอุ่นไม่เจ็บ → rocker-bottom"],
    [mcq(N(23), "A 62-year-old man with long-standing diabetes has sudden diplopia and ptosis of the left eye with the eye deviated down and out. The left pupil is equal and reactive. What is the most likely mechanism?",
         ["Compression of the third nerve by a posterior communicating artery aneurysm", "Ischemia of the central core of the third nerve with sparing of the peripheral pupillomotor fibers", "Myasthenia gravis", "Horner syndrome", "Raised intracranial pressure"], 1,
         "**Diabetic (ischemic) CN III palsy** — หลอดเลือดเล็กที่เลี้ยง **แกนกลาง** ของเส้นประสาทอุดตัน ใยประสาทที่ควบคุมรูม่านตาอยู่ **ผิวนอก** ได้เลือดจากหลอดเลือดที่ผิวจึงรอด → **รูม่านตาปกติ (pupil-sparing)** มักฟื้นเองใน 2–3 เดือน\n\n- **เส้นเลือดโป่งพอง** กดจากด้านนอก โดนใยรูม่านตาก่อน → รูม่านตาขยาย (ต้องทำ CTA ด่วน)\n- myasthenia ไม่มีรูม่านตาผิดปกติและอาการแปรผันตามความล้า\n- Horner มีหนังตาตกเล็กน้อยกับรูม่านตาเล็ก ไม่มีตาเหล่ลงล่างออกนอก",
         "CN III palsy + รูม่านตาปกติ ในเบาหวาน = ischemic core", "Mononeuropathy", ["หลักประสาทวิทยา — สไลด์ระบุ mononeuropathy"], ["2.3.6-3(9)", DM]),
     mcq(N(24), "A 55-year-old woman with diabetic neuropathy has a warm, swollen, red right foot without fever; she reports little pain. Pulses are bounding, and the midfoot looks flattened. What is the most likely diagnosis?",
         ["Acute gout", "Charcot neuroarthropathy", "Critical limb ischemia", "Deep vein thrombosis", "Plantar fasciitis"], 1,
         "**Charcot neuroarthropathy** — ผู้ป่วยรับรู้ความเจ็บไม่ได้จึงลงน้ำหนักบนกระดูกที่หักเล็ก ๆ ซ้ำ ๆ ร่วมกับ autonomic neuropathy ทำให้เลือดไปเท้ามากขึ้น (ชีพจรแรง) กระดูกถูกสลาย → เท้า **บวม แดง อุ่น เจ็บน้อย** และกลางเท้ายุบ (rocker-bottom) → ต้องงดลงน้ำหนัก (total contact cast) และแยกจาก cellulitis/osteomyelitis\n\n- **เกาต์** ปวดมาก\n- **ขาดเลือด** เท้าเย็น ชีพจรเบา\n- **DVT** บวมทั้งขา\n- plantar fasciitis ไม่ทำให้บวมแดงอุ่น",
         "เท้าเบาหวาน บวมแดงอุ่น เจ็บน้อย ชีพจรแรง = Charcot", "Diabetic foot", R("Charcot arthropathy"), ["2.3.6-3(9)", "2.3.12(13)"])],
    ["2.3.6-3(9)", "2.3.12(13)", "B3.4(7)", "2.3.9-3(7)", DM],
    {"neuro": fig("ทำไมเท้าเบาหวานถึงเป็นแผลโดยไม่รู้ตัว",
        "ซ้าย: เส้นประสาทที่ **ยาวที่สุด** เสียก่อน จึงชาเป็น **ถุงเท้า** แล้วจึงตามด้วย **ถุงมือ** · ขวา: sensory (ไม่เจ็บ) · motor (นิ้วงอ จุดกดทับ) · autonomic (ผิวแห้งแตก) · PAD (เลือดน้อย) รวมกับบาดเจ็บเล็กน้อย → **แผลที่เท้า** → ติดเชื้อ → ตัดขา",
        F.neuro())})

# ───────────────────────────── 13
sec("endo-dm-13", "Macrovascular และเป้าหมายการรักษาแบบองค์รวม",
    "โรคหัวใจ 70% ของการตาย · stroke · PVD ใต้เข่า ABI < 0.9 · holistic 9 ข้อ · HbA1c < 7 หรือปรับตามคน", 9,
"""### Macrovascular complications (สไลด์)
**โรคหัวใจและหลอดเลือด**
- **สาเหตุการตายอันดับ 1** — ราว **70% ของการตาย** ในผู้ป่วยเบาหวาน
- โรคกระจายกว้างและรุนแรงกว่า ผลลัพธ์หลังเกิดเหตุแย่กว่า · **เกิดตั้งแต่อายุน้อยกว่า**

**หลอดเลือดสมอง**
- **stroke 4%** ในผู้ป่วยเบาหวาน เทียบกับ **0.5%** ในคนทั่วไป · ตายมากกว่า ฟื้นตัวแย่กว่า กลับเป็นซ้ำบ่อย · ยาลดความดันป้องกันได้

**หลอดเลือดส่วนปลาย (PVD)**
- atherosclerosis ของหลอดเลือดขา · มัก **สองข้าง หลายตำแหน่ง และอยู่ส่วนปลายใต้เข่า**
- ร่วมกับ neuropathy เพิ่มการติดเชื้อ แผล และข้อถูกทำลาย · **พบมากกว่าคนทั่วไป 4 เท่า**
- คัดกรองด้วย **ankle–brachial index (ABI) < 0.9**

#### ทำไมเบาหวานทำให้หลอดเลือดใหญ่เสียเร็ว
น้ำตาลสูงจับโปรตีนเป็น AGEs ทำให้ผนังหลอดเลือดแข็งและอักเสบ · insulin resistance มาพร้อม **ไขมันผิดปกติ** (TG สูง HDL ต่ำ LDL เล็กหนาแน่น) และ **ความดันสูง** · เกล็ดเลือดเกาะง่าย และการสลายลิ่มเลือดลดลง — ปัจจัยเสี่ยงจึงซ้อนกันหลายตัว (สไลด์: dyslipidemia, HT, บุหรี่, อ้วน, น้ำตาลสูง, อายุ/เพศ/พฤติกรรม, พันธุกรรม, microalbuminuria)
**ทำไม MI ในเบาหวานมักไม่เจ็บ**: autonomic neuropathy ทำลายเส้นประสาทรับความรู้สึกจากหัวใจ → มาด้วยเหนื่อย หัวใจล้มเหลว หรือน้ำตาลแกว่งแทน

### Holistic management of T2DM (สไลด์)
1. เป้าหมายน้ำตาล 2. เป้าหมายความดัน 3. เป้าหมายไขมัน 4. **aspirin ในรายที่เลือก** 5. **ACEi/ARB ในรายที่เลือก** 6. **เลิกบุหรี่** 7. น้ำหนักเหมาะสม 8. ให้ความรู้และดูแลตนเอง 9. **คัดกรองภาวะแทรกซ้อนทุกปี**

### เป้าหมายน้ำตาล (สไลด์)
| | **ADA** | **IDF** |
|---|---|---|
| HbA1c (ปกติ 4.0–6.0%) | **< 7.0%** | < 6.5% |
| FPG (ก่อนอาหาร) | < 130 | < 110 |
| หลังอาหาร | < 180 | < 140 |

[[fig:glyc_target]]

**ประโยชน์ของการคุมเข้ม = ลด microvascular · ความเสี่ยง = hypoglycemia** (สไลด์)
- **เข้มงวด A1C < 6.5–7%**: วินิจฉัยใหม่ · อายุขัยยาว
- **ผ่อนปรน A1C ≥ 7.5%**: เด็กเล็ก · สูงอายุมาก · ภาวะแทรกซ้อนมาก

**เป้าความดันและไขมัน (ADA Standards of Care — ไม่อยู่ในสไลด์)**: BP < 130/80 · statin ทุกคนอายุ 40–75 ปี — มีโรคหัวใจแล้วเป้า **LDL < 55 mg/dL** · ยังไม่มีแต่มีปัจจัยเสี่ยง **LDL < 70** · aspirin ใช้ป้องกันซ้ำ (secondary) ส่วนป้องกันปฐมภูมิเฉพาะรายเสี่ยงสูงที่เลือดออกง่ายต่ำ
""",
    ["CVD = สาเหตุตายอันดับ 1 (~70%) · เป็นเร็วกว่า รุนแรงกว่า · stroke 4% vs 0.5%",
     "PVD 4 เท่า สองข้าง หลายตำแหน่ง ใต้เข่า · ABI < 0.9",
     "MI ไม่เจ็บเพราะ autonomic neuropathy",
     "Holistic 9 ข้อ: น้ำตาล ความดัน ไขมัน aspirin ACEi/ARB บุหรี่ น้ำหนัก education คัดกรองทุกปี",
     "ADA: A1c < 7 · FPG < 130 · PP < 180 · IDF 6.5/110/140 · เข้ม < 6.5–7 ในรายใหม่ · ผ่อน ≥ 7.5 ในสูงอายุ/เด็กเล็ก"],
    [mcq(N(25), "An 84-year-old woman with type 2 diabetes for 25 years, heart failure, CKD stage 4 and two recent hypoglycemic falls has HbA1c 7.1% on insulin. What is the most appropriate glycemic approach?",
         ["Intensify insulin to reach HbA1c below 6.5%", "Relax the HbA1c target to about 7.5–8% and reduce insulin to avoid hypoglycemia", "Stop all glucose-lowering therapy", "Add a sulfonylurea", "Target HbA1c below 6.0%"], 1,
         "สไลด์: **ผู้สูงอายุมาก มีภาวะแทรกซ้อนมาก** ควรใช้ **เป้าผ่อนปรน A1C ≥ 7.5%** เพราะประโยชน์ด้าน microvascular ต้องใช้เวลาหลายปี ขณะที่ **hypoglycemia** (หกล้ม หัวใจเต้นผิดจังหวะ) เป็นอันตรายทันที — A1c 7.1% กับประวัติน้ำตาลต่ำ แปลว่าคุมเข้มเกิน → ลด insulin\n\n- เพิ่ม insulin หรือเพิ่ม SU ยิ่งเสี่ยงน้ำตาลต่ำ (SU สะสมใน CKD)\n- หยุดยาทั้งหมดเสี่ยงน้ำตาลสูงจนมีอาการ/HHS",
         "สูงอายุมาก + ภาวะแทรกซ้อน + hypo บ่อย → เป้า A1c ผ่อน ≥ 7.5", "Glycemic goals", R("Benefit and risk of tight glycemic control"), [DM, HYPO])],
    [DM, "2.3.9(6)", "2.2.39", "2.3.9-3(7)", "B7.2.6-3(2)", "2.3.9(3)", "2.3.9(4)"],
    {"glyc_target": fig("เป้า HbA1c — ปรับตามผู้ป่วย",
        "ยิ่งเป้าต่ำ **ภาวะแทรกซ้อนหลอดเลือดเล็กยิ่งลด** (เขียว) แต่ **hypoglycemia ยิ่งเพิ่ม** (แดง) — เลือกเข้มงวด < 6.5–7% ในผู้ป่วยใหม่อายุขัยยาว และผ่อนปรน ≥ 7.5% ในเด็กเล็ก ผู้สูงอายุมาก หรือผู้ที่มีภาวะแทรกซ้อนมาก (สไลด์)",
        F.glyc_target())})

# ───────────────────────────── 14
sec("endo-dm-14", "ยาเม็ดและยากลุ่ม incretin — ออกฤทธิ์ที่ไหน และผลข้างเคียงมาจากไหน",
    "secretagogue · sensitizer · AGI · SGLT2i · GLP-1RA vs DPP-4i · ตารางเปรียบเทียบประสิทธิภาพ น้ำหนัก หัวใจ ไต", 13,
"""### 4 กลุ่มของยาเม็ด (สไลด์)
| กลุ่ม | ยา |
|---|---|
| **1. กระตุ้นการหลั่ง insulin (secretagogue)** | **sulfonylurea** (glipizide) · glinides · **gliptins (DPP-4 inhibitor)** · **glutides (GLP-1 RA)** |
| **2. เพิ่มความไวต่อ insulin (sensitizer)** | **metformin** · thiazolidinedione (**pioglitazone**) |
| **3. ยับยั้งการดูดซึมน้ำตาลจากลำไส้** | **α-glucosidase inhibitor** (acarbose) |
| **4. ขับน้ำตาลทางไต** | **SGLT2 inhibitor** (gliflozin) |

[[fig:drug_sites]]

### Incretin — GLP-1 receptor agonist เทียบ DPP-4 inhibitor (สไลด์)
[[fig:incretin]]

กินอาหาร → ลำไส้หลั่ง **GLP-1 และ GIP** → กระตุ้น insulin **เฉพาะเมื่อน้ำตาลสูง (glucose dependent)** และ GLP-1 ลด glucagon → ตับปล่อยน้ำตาลลด — แต่ถูกเอนไซม์ **DPP-4 ทำลายภายในไม่กี่นาที**
| | **GLP-1 RA** (liraglutide, semaglutide, tirzepatide*) | **DPP-4 inhibitor** (sitagliptin) |
|---|---|---|
| ระดับ GLP-1 | สูงเกินสรีรวิทยาต่อเนื่อง | เฉพาะหลังอาหาร (ของตัวเอง) |
| ศูนย์อิ่มในสมอง | ✓ | ไม่มีผล |
| ชะลอการบีบตัวของกระเพาะ | ✓ | ไม่มีผล |
| คลื่นไส้อาเจียน | พบบ่อย | ทนได้ดี |
| น้ำหนัก | **ลด** | คงที่ |
| รูปแบบ | ฉีดใต้ผิวหนัง · ชนิดกิน | กิน |
*tirzepatide เป็น dual GIP/GLP-1 receptor agonist

### SGLT2 inhibitor — ทิ้งน้ำตาลทางไต (สไลด์)
[[fig:sglt2]]

### ตารางเปรียบเทียบ (สไลด์)
| ยา | ประสิทธิภาพ | Hypo | น้ำหนัก | ASCVD | HF | ไต (DKD) | ราคา | ผลข้างเคียง |
|---|---|---|---|---|---|---|---|---|
| **Metformin** | สูง | ไม่ | คงที่ (ลด) | อาจได้ประโยชน์ | เป็นกลาง | เป็นกลาง | ถูก | GI · ขาด B12 |
| **SGLT2i** | ปานกลาง | ไม่ | ลด | **ประโยชน์** | **ประโยชน์** | **ประโยชน์** | แพง | ติดเชื้อทางเดินปัสสาวะ/อวัยวะเพศ · DKA · ขาดน้ำ |
| **GLP-1 RA** | สูง | ไม่ | ลด | **ประโยชน์** | เป็นกลาง | อาจได้ประโยชน์ | แพงมาก | คลื่นไส้อาเจียน · เสี่ยง C-cell tumor |
| **DPP-4i** | ปานกลาง | ไม่ | คงที่ | เป็นกลาง | เป็นกลาง | เป็นกลาง | แพง | ตับอ่อนอักเสบ? |
| **TZD** | สูง | ไม่ | เพิ่ม | อาจได้ประโยชน์ | **เพิ่มความเสี่ยง** | เป็นกลาง | ถูก | บวม · น้ำคั่ง · กระดูกหัก |
| **SU** | สูง | **ใช่** | เพิ่ม | เป็นกลาง | เป็นกลาง | เป็นกลาง | ถูก | **hypoglycemia** |
| **Insulin** | สูงสุด | **ใช่** | เพิ่ม | เป็นกลาง | เป็นกลาง | เป็นกลาง | ถูก | **hypoglycemia** |

#### ทำไมผลข้างเคียงถึงเป็นแบบนี้
| ผลข้างเคียง | กลไก |
|---|---|
| **SU → น้ำตาลต่ำ น้ำหนักขึ้น** | ปิด **K-ATP channel** ของ β cell ทำให้หลั่ง insulin **ไม่ว่าน้ำตาลจะเท่าไร** — ต่างจาก GLP-1/DPP-4i ที่หลั่งเฉพาะเมื่อน้ำตาลสูง |
| **TZD → บวม หัวใจล้มเหลวกำเริบ** | กระตุ้น PPAR-γ ซึ่งเพิ่มการดูด Na ที่ collecting duct (ENaC) → น้ำคั่ง · ห้ามใช้ใน HF ที่รุนแรง |
| **Metformin → ท้องเสีย ขาด B12** | ยาความเข้มข้นสูงในลำไส้ · รบกวนการดูดซึม B12 ที่ ileum → ตรวจ B12 เมื่อใช้นาน/มีชาปลายมือเท้า · ลดขนาดเมื่อ eGFR 30–44 หยุดเมื่อ < 30 |
| **SGLT2i → เชื้อราอวัยวะเพศ** | glucose ในปัสสาวะเป็นอาหารของเชื้อรา |
| **SGLT2i → euglycemic DKA** | น้ำตาลลดลงทำให้ร่างกายหลั่ง insulin น้อยลงและ glucagon มากขึ้น → สลายไขมันเป็น ketone ทั้งที่น้ำตาล < 250 · หยุดยา 3 วันก่อนผ่าตัดหรือเมื่อเจ็บป่วยเฉียบพลัน |
| **GLP-1 RA → คลื่นไส้** | ชะลอการบีบตัวของกระเพาะ + กระตุ้นศูนย์ในสมอง · ห้ามใน medullary thyroid carcinoma/MEN2 (C-cell tumor ในสัตว์ทดลอง) |
| **AGI → ท้องอืด ผายลม** | แป้งที่ไม่ถูกย่อยไปถึงลำไส้ใหญ่ให้แบคทีเรียหมัก · น้ำตาลต่ำต้องแก้ด้วย **glucose** ไม่ใช่น้ำตาลทราย |
""",
    ["4 กลุ่ม: secretagogue (SU, glinide, DPP-4i, GLP-1RA) · sensitizer (metformin, TZD) · AGI · SGLT2i",
     "SU ปิด K-ATP หลั่ง insulin ไม่ขึ้นกับน้ำตาล → hypo · GLP-1/DPP-4i หลั่งเฉพาะเมื่อน้ำตาลสูง",
     "GLP-1RA: อิ่ม ชะลอกระเพาะ น้ำหนักลด คลื่นไส้ · DPP-4i: น้ำหนักคงที่ ทนได้ดี",
     "SGLT2i: ประโยชน์ ASCVD + HF + ไต · AE ติดเชื้อราอวัยวะเพศ ขาดน้ำ euglycemic DKA",
     "TZD: น้ำคั่ง HF แย่ลง กระดูกหัก · metformin: GI, B12, หยุดเมื่อ eGFR < 30"],
    [mcq(N(26), "A 67-year-old man with type 2 diabetes and heart failure with reduced ejection fraction develops worsening leg edema and dyspnea after a new oral agent was added. Which drug is most likely responsible?",
         ["Metformin", "Pioglitazone", "Empagliflozin", "Sitagliptin", "Acarbose"], 1,
         "**Pioglitazone (TZD)** กระตุ้น PPAR-γ ที่ไต เพิ่มการดูด Na ที่ collecting duct → **น้ำคั่ง บวม และหัวใจล้มเหลวกำเริบ** (ตารางในสไลด์: HF = เพิ่มความเสี่ยง) จึงห้ามใช้ใน HF ที่มีอาการ\n\n- metformin เป็นกลางต่อ HF\n- **empagliflozin (SGLT2i) ให้ประโยชน์ใน HF** — ขับ Na/น้ำ\n- sitagliptin และ acarbose ไม่ทำให้น้ำคั่ง",
         "TZD = น้ำคั่ง HF แย่ลง · SGLT2i = ช่วย HF", "Oral agents", R("Comparison table of glucose-lowering agents"), [DRUG]),
     mcq(N(27), "A patient taking acarbose and gliclazide develops symptomatic hypoglycemia (glucose 52 mg/dL) but is awake. Which treatment is most appropriate?",
         ["A glass of sweetened condensed milk with table sugar (sucrose)", "Oral glucose tablets or glucose solution", "A slice of white bread", "Intramuscular glucagon only", "Wait 30 minutes and recheck"], 1,
         "acarbose ยับยั้ง **α-glucosidase** ที่ย่อยแป้งและ **sucrose** เป็นน้ำตาลโมเลกุลเดียว การแก้ด้วยน้ำตาลทราย ขนมปัง หรือนมหวาน จึงดูดซึมช้า → ต้องใช้ **glucose** โดยตรง (ส่วนน้ำตาลต่ำมาจาก gliclazide ซึ่งเป็น SU)\n\n- glucagon สงวนไว้เมื่อกลืนไม่ได้\n- การรอโดยไม่แก้อันตราย",
         "ใช้ acarbose แล้วน้ำตาลต่ำ → แก้ด้วย glucose ไม่ใช่ sucrose", "Oral agents", ["หลักเภสัชวิทยา — สไลด์: AGI ยับยั้งการดูดซึมน้ำตาล"], [DRUG, HYPO]),
     mcq(N(28), "A 52-year-old woman with type 2 diabetes on empagliflozin presents 2 days after laparoscopic cholecystectomy with nausea and abdominal pain. Glucose 186 mg/dL, pH 7.21, HCO3 12 mEq/L, anion gap 22, serum beta-hydroxybutyrate 4.8 mmol/L. What is the diagnosis?",
         ["Lactic acidosis from metformin", "Euglycemic diabetic ketoacidosis associated with SGLT2 inhibitor", "Hyperosmolar hyperglycemic state", "Starvation ketosis only", "Post-operative pancreatitis without acidosis"], 1,
         "กรด AG สูง + **β-OHB 4.8 mmol/L** ทั้งที่ **glucose < 250** ในผู้ที่ใช้ **SGLT2i** ช่วงผ่าตัดและกินได้น้อย = **euglycemic DKA** — SGLT2i ทิ้งน้ำตาลทางไต น้ำตาลจึงไม่สูงมาก ร่างกายหลั่ง insulin น้อยลงและ glucagon มากขึ้นจนสลายไขมันเป็น ketone → หยุดยา ให้สารน้ำที่มี dextrose ร่วมกับ insulin\n\n- lactic acidosis ต้องมี lactate สูง\n- HHS ต้อง glucose ≥ 600 ไม่มีกรด\n- starvation ketosis ไม่ทำให้ HCO₃ ต่ำขนาดนี้",
         "SGLT2i + ป่วย/ผ่าตัด + กรด ketone น้ำตาลไม่สูง = euglycemic DKA", "SGLT2i", ["สไลด์: SGLT2i AE = DKA · ADA 2024 consensus"], [DRUG, CRI])],
    [DRUG, DM],
    {"drug_sites": fig("ยาเบาหวานออกฤทธิ์ที่ไหน",
        "**สมอง/กระเพาะ** — GLP-1RA ทำให้อิ่มและกระเพาะบีบช้า · **ลำไส้** — AGI ชะลอย่อยแป้ง · **ตับ** — metformin ลดการปล่อยน้ำตาล · **ตับอ่อน** — SU/glinide บังคับหลั่ง insulin (จึงทำให้น้ำตาลต่ำได้) ส่วน GLP-1RA/DPP-4i หลั่งเฉพาะเมื่อน้ำตาลสูง · **กล้ามเนื้อ/ไขมัน** — TZD · **ไต** — SGLT2i",
        F.drug_sites()),
     "incretin": fig("Incretin — GLP-1 ถูก DPP-4 ทำลายในไม่กี่นาที",
        "อาหารกระตุ้นลำไส้หลั่ง GLP-1/GIP ซึ่งเพิ่ม insulin เฉพาะเมื่อน้ำตาลสูงและลด glucagon · ล่าง: GLP-1 ตามธรรมชาติอยู่ไม่กี่นาที · **DPP-4 inhibitor** ทำให้ GLP-1 ของตัวเองอยู่นานขึ้นหลังมื้ออาหาร · **GLP-1RA** ทนต่อ DPP-4 ให้ระดับสูงต่อเนื่องจึงอิ่มและน้ำหนักลด (เส้นเชิงหลักการ)",
        F.incretin()),
     "sglt2": fig("SGLT2 inhibitor — ทิ้งน้ำตาลทางไต",
        "ปกติ **SGLT2 ที่ proximal tubule ส่วนต้น** ดูด glucose กลับเกือบทั้งหมด (สไลด์: S1 SGLT2 · S3 SGLT1) · เมื่อยับยั้ง glucose และ Na หลุดไปในปัสสาวะ — ได้ประโยชน์เรื่องน้ำหนัก ความดัน ไต และหัวใจ แต่มีผลข้างเคียงที่มาจากกลไกเดียวกัน (แถบแดง)",
        F.sglt2())})

# ───────────────────────────── 15
sec("endo-dm-15", "แนวทางรักษา T2 (Thai CPG 2020) และการใช้ insulin",
    "metformin → เลือกยาตามโรคหัวใจ ไต HF · เป้าตอนวินิจฉัย · UKPDS · insulin 4 ชนิด · basal–bolus · basal plus", 12,
"""### แนวทางเวชปฏิบัติเบาหวานไทย 2020 — อัลกอริทึม T2 (สไลด์)
**ไม่มี ASCVD, HF หรือ CKD**
1. ปรับพฤติกรรม → ไม่ถึงเป้า **เริ่ม metformin**
2. ไม่ถึงเป้า **เพิ่ม SU หรือ TZD** (ทางเลือก: DPP-4i, AGI, repaglinide)
3. ไม่ถึงเป้า **ยาเม็ด 3 ชนิด** (ทางเลือก: DPP-4i, SGLT2i, AGI, repaglinide, basal insulin, GLP-1 RA)
4. ไม่ถึงเป้า **ยาเม็ด ± GLP-1 RA ร่วมกับ insulin**

**มี ASCVD หรือ HF หรือ CKD (GFR < 60 และ/หรือ UACR > 200 mg/g)** — ไม่ว่าวินิจฉัยใหม่หรือเป็นอยู่แล้ว
| โรคร่วม | ยาที่เลือก |
|---|---|
| **ASCVD** | **GLP-1 RA หรือ SGLT2i** (ถ้าไม่ติดเรื่องค่าใช้จ่าย) · ถ้าติดเรื่องค่าใช้จ่าย metformin + SU หรือ TZD |
| **Heart failure** | **SGLT2i** |
| **CKD** | **SGLT2i** (ใช้ GLP-1 RA ถ้าใช้ SGLT2i ไม่ได้) |
†อาจใช้เดี่ยว หรือร่วมกับ metformin

**เลือกจุดเริ่มต้นจากระดับน้ำตาลตอนวินิจฉัย (สไลด์)**
| ตอนวินิจฉัย | เริ่มด้วย |
|---|---|
| FPG < 140 · HbA1c < 7% | ปรับพฤติกรรม |
| FPG 140–280 · HbA1c 7–8.5% | ยาเม็ด |
| FPG > 280 · HbA1c > 8.5% **มีอาการมาก** (หรือ FPG/casual > 350) | พิจารณา **insulin** |
**Master decision path**: ยาเดี่ยวไม่ถึงเป้าใน **4–8 สัปดาห์** → ยาผสม · ยาผสมขนาดสูงสุดไม่ถึงเป้าใน **4–8 สัปดาห์** → insulin

> **T2 เป็นโรคที่แย่ลงเรื่อย ๆ** — UKPDS พบ β-cell function ลดลงต่อเนื่องทุกปี ส่วนใหญ่สุดท้ายต้องใช้ insulin (ไม่ใช่ความล้มเหลวของผู้ป่วย)
> ADA Standards of Care ปัจจุบัน (ไม่อยู่ในสไลด์) ใช้หลักเดียวกัน: ให้ SGLT2i/GLP-1 RA ในผู้ที่มี ASCVD, HF, CKD **โดยไม่ขึ้นกับ HbA1c** · เมื่อต้องใช้ยาฉีด เลือก GLP-1 RA ก่อน insulin ถ้าไม่มีข้อห้าม

### Insulin (สไลด์)
ร่างกายปกติหลั่ง insulin 2 แบบ — **basal** ต่อเนื่องตลอดวัน และ **bolus** หลังอาหาร
| ชนิด | ตัวอย่าง | เริ่มออกฤทธิ์ | สูงสุด | อยู่นาน |
|---|---|---|---|---|
| Rapid-acting (prandial) | **lispro, aspart** | **10 นาที** | 1.5 ชม. | 4 ชม. |
| Short-acting (prandial) | **regular (RI)** | 30 นาที | 2 ชม. | 6 ชม. |
| Intermediate (basal) | **NPH** | 1–2 ชม. | **4–8 ชม.** | 14–18 ชม. |
| Long-acting (basal) | **glargine** | 1–2 ชม. | **ไม่มีจุดสูงสุด** | ~24 ชม. |
| Premixed | NPH/regular 70/30, 50/50 · lispro mix 75/25 · aspart mix 70/30 | | | |

[[fig:insulin_profiles]]

#### ทำไมต้องรู้รูปร่างของแต่ละตัว
| ปัญหา | กลไก | แก้ |
|---|---|---|
| **น้ำตาลต่ำตอนตี 2–3** ในผู้ที่ฉีด NPH ก่อนอาหารเย็น | NPH ออกฤทธิ์สูงสุด 4–8 ชม. หลังฉีด ตรงกับกลางดึกที่ไม่ได้กินอะไร | ย้าย NPH ไปฉีด **ก่อนนอน** หรือเปลี่ยนเป็น glargine |
| **น้ำตาลเช้าสูง** | ① ฤทธิ์ basal หมดก่อนเช้า ② **dawn phenomenon** — GH และ cortisol หลั่งช่วงเช้ามืด ③ น้ำตาลต่ำกลางดึกแล้วเด้งกลับ (Somogyi) | เจาะน้ำตาลตี 3 เพื่อแยก ก่อนจะเพิ่มขนาด |
| ต้องฉีด regular ก่อนอาหาร **30 นาที** แต่ rapid ฉีดก่อนกินได้เลย | regular รวมกันเป็น hexamer ต้องแยกตัวก่อนดูดซึม · analog ถูกดัดแปลงให้แยกเร็ว | — |

### รูปแบบการฉีด (สไลด์)
[[fig:basal_bolus]]

- **Type 1**: **basal–bolus** — RI/rapid ก่อนอาหาร 3 มื้อ + NPH หรือ glargine (ก่อนนอน) · หรือ regular + NPH วันละ 2 ครั้ง
- **Type 2**: ยาเม็ด 2 ชนิดไม่ถึงเป้า → **ยาเม็ด + basal insulin ก่อนนอน (basal plus)** → premixed วันละ 1–2 ครั้ง + ยาเม็ด
- เริ่ม basal ใน T2 (ADA — ไม่อยู่ในสไลด์): **10 ยูนิต หรือ 0.1–0.2 U/kg ก่อนนอน** ปรับเพิ่มทีละ 2 ยูนิตทุก 3 วันตามน้ำตาลเช้า
""",
    ["ไม่มีโรคร่วม: lifestyle → metformin → + SU/TZD → 3 ยา → + insulin",
     "มี ASCVD → GLP-1RA หรือ SGLT2i · HF หรือ CKD (GFR < 60 / UACR > 200) → SGLT2i",
     "ตอนวินิจฉัย: A1c < 7 lifestyle · 7–8.5 ยาเม็ด · > 8.5 มีอาการ/FPG > 350 → insulin · ไม่ถึงเป้า 4–8 สัปดาห์ เพิ่มขั้น",
     "Rapid 10 นาที/1.5/4 ชม. · regular 30 นาที/2/6 · NPH 1–2/4–8/14–18 · glargine flat 24 ชม.",
     "NPH ก่อนอาหารเย็น → hypo ตี 2–3 · T1 = basal–bolus · T2 = basal plus → premixed"],
    [mcq(N(29), "A 60-year-old man with type 2 diabetes (HbA1c 8.2% on metformin) has heart failure with reduced ejection fraction and eGFR 52. According to the Thai 2020 algorithm in the lecture, which add-on is preferred?",
         ["Pioglitazone", "Sulfonylurea", "SGLT2 inhibitor", "Acarbose", "Repaglinide"], 2,
         "อัลกอริทึม TH DM CPG 2020: ผู้ป่วยที่มี **heart failure หรือ CKD (GFR < 60)** ให้เลือก **SGLT2 inhibitor** (ตารางยา: ประโยชน์ทั้ง HF และ DKD)\n\n- **pioglitazone ทำให้ HF แย่ลง**\n- SU และ repaglinide ไม่ได้ประโยชน์ต่อหัวใจ/ไต และเสี่ยงน้ำตาลต่ำ\n- acarbose ไม่มีประโยชน์ด้านนี้",
         "T2 + HF หรือ CKD → SGLT2i", "Treatment algorithm", R("2020 TH DM CPG: T2D treatment algorithm"), [DM, DRUG]),
     mcq(N(30), "A woman with type 1 diabetes injects regular insulin before meals and NPH before dinner. She has recurrent sweating and nightmares around 2–3 a.m. with capillary glucose 50 mg/dL. What is the best adjustment?",
         ["Increase the dinner NPH dose", "Move the NPH injection from before dinner to bedtime (or switch to glargine)", "Add a bedtime dose of regular insulin", "Stop all insulin overnight", "Give a sulfonylurea at night"], 1,
         "สไลด์: **NPH ออกฤทธิ์สูงสุด 4–8 ชม.** หลังฉีด — ฉีดก่อนอาหารเย็น (~18.00) ฤทธิ์สูงสุดจะตกช่วง **ตี 2–3** ซึ่งไม่ได้กินอะไร → น้ำตาลต่ำกลางดึก (เหงื่อแตก ฝันร้าย) แก้โดย **ย้ายไปฉีดก่อนนอน** ให้จุดสูงสุดเลื่อนไปใกล้เช้า หรือเปลี่ยนเป็น **glargine ที่ไม่มีจุดสูงสุด**\n\n- เพิ่ม NPH ยิ่งต่ำ\n- regular ก่อนนอนเพิ่มน้ำตาลต่ำ\n- T1 หยุด insulin ทั้งคืนเสี่ยง DKA\n- SU ไม่มีบทบาทใน T1",
         "NPH ก่อนอาหารเย็น → hypo ตี 2–3 → ย้ายไปก่อนนอนหรือใช้ glargine", "Insulin", R("Insulin onset/peak/duration"), [DRUG, HYPO]),
     mcq(N(31), "A 38-year-old man has newly diagnosed type 2 diabetes with polyuria, 7 kg weight loss, FPG 380 mg/dL and HbA1c 12.5%; ketones are negative. Based on the lecture's starting thresholds, what is the most appropriate initial treatment?",
         ["Lifestyle modification alone for 3 months", "Metformin monotherapy and review in 6 months", "Start insulin (with lifestyle ± metformin)", "Acarbose", "DPP-4 inhibitor monotherapy"], 2,
         "สไลด์: ตอนวินิจฉัย **FPG > 280 หรือ HbA1c > 8.5% ที่มีอาการมาก** (และ FPG > 350) ควรเริ่ม **insulin** เพื่อแก้ภาวะ glucotoxicity ที่ทำให้ β cell ล้า — เมื่อน้ำตาลลงแล้วมักลดหรือเปลี่ยนเป็นยาเม็ดได้\n\n- lifestyle อย่างเดียวหรือยาเม็ดตัวเดียวไม่พอที่ระดับนี้ (น้ำหนักลดคือสัญญาณขาด insulin)\n- acarbose และ DPP-4i ลด A1c ได้น้อย",
         "วินิจฉัยใหม่ A1c > 8.5 + อาการมาก/FPG > 350 → insulin", "Treatment algorithm", R("Targets for glycemic control at diagnosis"), [DM, DRUG])],
    [DM, DRUG],
    {"insulin_profiles": fig("รูปแบบการออกฤทธิ์ของ insulin 4 ชนิด",
        "**Rapid** ขึ้นเร็วสูงสุด 1.5 ชม. หมดใน 4 ชม. · **Regular** สูงสุด 2 ชม. อยู่ 6 ชม. · **NPH** สูงสุด 4–8 ชม. อยู่ 14–18 ชม. (จุดสูงสุดนี้ทำให้น้ำตาลต่ำกลางดึก) · **Glargine** แบนราบราว 24 ชม. — ตัวเลขตามตารางในสไลด์",
        F.insulin_profiles()),
     "basal_bolus": fig("insulin ของร่างกาย เทียบกับการฉีดแบบ basal–bolus",
        "บน: ร่างกายหลั่ง insulin **ฐาน (basal)** ตลอดวัน และ **พุ่งขึ้นหลังอาหาร (bolus)** · ล่าง: **basal–bolus** ใช้ glargine/NPH ก่อนนอนแทนส่วนฐาน และ rapid/regular ก่อนอาหารแทนส่วนพุ่ง — เลียนแบบรูปแบบธรรมชาติ (T1) · T2 มักเริ่มด้วย basal อย่างเดียวร่วมกับยาเม็ด",
        F.basal_bolus())})

# ───────────────────────────── MEQ / OSCE
LECNAME = "Diabetes mellitus (ศ.นพ.ชัยชาญ)"
MEQ = [{"id": "END-DM-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Diabetic ketoacidosis as the first presentation of type 1 diabetes",
 "vignette": """ผู้ป่วยหญิงไทยอายุ 19 ปี นักศึกษา มาด้วยอาเจียนและปวดท้อง 1 วัน
PI: 3 สัปดาห์ก่อน ปัสสาวะบ่อย ตื่นกลางคืน 3–4 ครั้ง กระหายน้ำมาก น้ำหนักลด 6 กก. ทั้งที่กินจุขึ้น 2 วันก่อน เจ็บคอ มีไข้ต่ำ ๆ 1 วันก่อน อาเจียนหลายครั้ง ปวดท้องทั่ว ๆ หายใจเหนื่อย
PH: ไม่มีโรคประจำตัว มารดาเป็นไทรอยด์เป็นพิษ
PE: BT 37.8 C, PR 124/min, RR 32/min หายใจลึก, BP 96/60 mmHg · ซึมเล็กน้อย ตอบคำถามได้ · ปากแห้ง ลมหายใจมีกลิ่นผลไม้ · ท้องกดเจ็บทั่ว ๆ ไม่มี guarding
Lab: capillary glucose 486 mg/dL
Na 129, K 5.6, Cl 95, HCO₃ 8 mEq/L · BUN 32, Cr 1.6 mg/dL
venous pH 7.12 · serum β-hydroxybutyrate 6.2 mmol/L · urine ketone 3+
CBC: WBC 16,800/mm³""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัย ระบุความรุนแรง และเกณฑ์ที่ใช้ (3 คะแนน)",
   "a": """**Diabetic ketoacidosis (DKA) ระดับ moderate** เป็นอาการแรกของเบาหวาน — น่าจะเป็น **type 1** (อายุน้อย น้ำหนักลด เริ่มเร็ว ครอบครัวมีโรคภูมิต้านตนเอง)
เกณฑ์ (ADA consensus 2024): glucose **≥ 200** (486) · **β-OHB ≥ 3.0** (6.2) · **pH < 7.3 และ/หรือ HCO₃ < 18** (7.12 / 8)
ความรุนแรง (ADA 2009): pH 7.00–7.24 = moderate (HCO₃ 8 < 10 เข้าเกณฑ์ severe — ประเมินร่วมกับระดับความรู้สึกตัว)"""},
  {"q": "2. จงคำนวณ anion gap และ corrected Na และอธิบายว่าทำไม K 5.6 แต่ผู้ป่วยยังมี K ทั้งร่างกายพร่อง (3 คะแนน)",
   "a": """- **AG = 129 − (95 + 8) = 26** → high anion gap metabolic acidosis จาก ketone
- **Corrected Na = 129 + 1.6 × (486 − 100)/100 ≈ 129 + 6.2 = 135** → Na จริงปกติ (ต่ำจากการเจือจางของ glucose)
- **K สูงในเลือด** เพราะขาด insulin + ภาวะกรด + osmolality สูง ดึง K ออกจากเซลล์ ขณะที่ osmotic diuresis และอาเจียน **ขับ K ทิ้ง** → K ทั้งร่างกายพร่อง จะลดลงเร็วเมื่อเริ่ม insulin"""},
  {"q": "3. จงเขียนการรักษาใน 2 ชั่วโมงแรก (4 คะแนน)",
   "a": """- **0.9% NaCl 15–20 mL/kg (≈ 1–1.5 ลิตร) ในชั่วโมงแรก** แล้วปรับตาม corrected Na (135 ปกติ → 0.45% NaCl 250–500 mL/ชม.)
- **ดู K ก่อนเริ่ม insulin**: K 5.6 > 5.2 → ยังไม่ให้ K เช็คทุก 2 ชม.
- **Regular insulin IV 0.1 U/kg bolus แล้ว 0.1 U/kg/ชม.** (หรือ 0.14 U/kg/ชม.) เป้า glucose ลด 50–75 mg/dL/ชม.
- **ไม่ให้ bicarbonate** (pH 7.12 > 6.9)
- เฝ้าระวัง: glucose ทุก 1 ชม. · electrolyte, venous pH, AG ทุก 2–4 ชม. · ปัสสาวะ · ความรู้สึกตัว
- หาตัวกระตุ้น: เจ็บคอมีไข้ → ตรวจหาการติดเชื้อ (throat, CXR, UA, hemoculture) · β-hCG"""},
  {"q": "4. 4 ชั่วโมงต่อมา glucose 230 mg/dL, K 3.1 mEq/L, HCO₃ 13, AG 18 — จะปรับการรักษาอย่างไร (3 คะแนน)",
   "a": """- **K 3.1 < 3.3** → **ให้ K ทดแทนทันที และหยุด insulin ชั่วคราว** จน K ≥ 3.3 (insulin ดัน K เข้าเซลล์)
- glucose ใกล้ 200–250 แต่ **กรดยังไม่หาย** (HCO₃ 13, AG 18) → เมื่อเริ่ม insulin ต่อให้ **ลดขนาด (0.02–0.05 U/kg/ชม.) และเติม dextrose (D5/0.45% NaCl)** รักษา glucose 150–200 จนกรดหาย
- **ห้ามหยุด insulin ถาวร** เพียงเพราะน้ำตาลลง"""},
  {"q": "5. จะประเมินว่า DKA หายแล้วอย่างไร และเปลี่ยนเป็น insulin ใต้ผิวหนังอย่างไร (3 คะแนน)",
   "a": """- **หาย (ADA 2009)**: glucose < 200 ร่วมกับ 2 ใน 3 ข้อ — **HCO₃ ≥ 15 · venous pH > 7.3 · AG ≤ 12** (consensus 2024: β-OHB < 0.6 และ pH ≥ 7.3 หรือ HCO₃ ≥ 18) และกินได้
- เริ่ม **basal–bolus** (เช่น ราว 0.5–0.6 U/kg/วัน แบ่ง basal ครึ่งหนึ่ง bolus ครึ่งหนึ่งก่อนอาหาร 3 มื้อ)
- **ฉีด basal insulin ใต้ผิวหนัง 1–2 ชม. ก่อนหยุด IV insulin** เพราะ IV insulin หมดฤทธิ์ในไม่กี่นาที"""},
  {"q": "6. ก่อนกลับบ้าน จะให้คำแนะนำอะไรบ้างเพื่อป้องกัน DKA ซ้ำ และตรวจอะไรเพิ่มเพื่อยืนยันชนิดของเบาหวาน (2 คะแนน)",
   "a": """- **Sick-day rules**: **ห้ามหยุด insulin แม้กินไม่ได้** · เจาะน้ำตาลบ่อยขึ้น (ทุก 2–4 ชม.) · ตรวจ ketone ถ้าน้ำตาล > 250 หรือคลื่นไส้อาเจียน · ดื่มน้ำมาก · มาโรงพยาบาลถ้าอาเจียนต่อเนื่อง หายใจหอบ ketone สูง
- สอนฉีดยา เก็บยา หมุนตำแหน่งฉีด · **อาการและการแก้ hypoglycemia** (กฎ 15)
- ยืนยัน T1: **autoantibody (GAD65, IA-2, ZnT8)** · **C-peptide** (ต่ำ) · คัดกรองไทรอยด์ (TSH) และ celiac เพราะโรคภูมิต้านตนเองพบร่วม"""}],
 "ref": ["ADA/EASD/JBDS/AACE/DTS consensus on hyperglycemic crises 2024", "ADA 2009 (Kitabchi) hyperglycemic crises", "สไลด์ ศ.นพ.ชัยชาญ — T1 vs T2, C-peptide"],
 "nl": [CRI, CRI1, DM, "B9.2.5(2)", "B9.4(2)"], "years": [], "_kind": "meq", "_set": SET}]

OSCE = [{"id": "END-DM-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "OSCE – Diabetic foot examination and foot-care counselling",
 "station": "OSCE (ตรวจร่างกาย + ให้คำแนะนำ) 8 นาที",
 "instruction": """ชายอายุ 64 ปี เป็นเบาหวานชนิดที่ 2 มา 15 ปี สูบบุหรี่ มาตรวจติดตามประจำปี บ่นชาปลายเท้าทั้งสองข้าง ปวดแสบร้อนตอนกลางคืน

**จงตรวจเท้าผู้ป่วยเพื่อคัดกรองเท้าเสี่ยงสูง แล้วให้คำแนะนำการดูแลเท้า ภายใน 8 นาที** (ผู้ป่วยมาตรฐานมีอุปกรณ์ monofilament 10 กรัม และส้อมเสียง 128 Hz วางไว้ให้)""",
 "answer": """**เกณฑ์ให้คะแนน (16 คะแนน)**

| ข้อ | สิ่งที่ต้องทำ | คะแนน |
|---|---|---|
| 1 | แนะนำตัว ขออนุญาต ถอดรองเท้าถุงเท้าทั้งสองข้าง ล้างมือ | 1 |
| 2 | **ดู**: ผิวแห้ง แตก ตาปลา (callus) แผล เชื้อราซอกนิ้ว เล็บ · **รูปเท้า**: claw/hammer toe, bunion, Charcot · สี · **ดูรองเท้าและถุงเท้า** | 2 |
| 3 | **คลำ**: อุณหภูมิเทียบสองข้าง · ชีพจร **dorsalis pedis และ posterior tibial** ทั้งสองข้าง | 2 |
| 4 | **Monofilament 10 g**: สาธิตที่มือก่อน ให้หลับตา กดตั้งฉากจนเส้นงอ ค้างราว 1–2 วินาที หลายตำแหน่ง (ปลายนิ้วโป้ง หัวกระดูกฝ่าเท้า) เลี่ยงแผล/callus · ถามว่ารู้สึกไหมและที่ไหน | 3 |
| 5 | **Vibration 128 Hz** ที่ข้อปลายนิ้วโป้ง และ/หรือ **ankle reflex** | 1 |
| 6 | สรุปผล: มี neuropathy (ไม่รู้สึก monofilament) ± ชีพจรเบา → **high-risk foot** · แนะนำวัด **ABI** (< 0.9 = PAD) | 2 |
| 7 | **ดูแลเท้าทุกวัน**: ตรวจเท้าทุกวัน (ใช้กระจก) · ล้างและเช็ดให้แห้งโดยเฉพาะซอกนิ้ว · ทาครีมผิวแห้งแต่ไม่ทาซอกนิ้ว · **ตัดเล็บตรง ไม่สั้นเกิน** · ตาปลาใช้หินขัด ไม่ตัดเอง | 2 |
| 8 | **ห้ามเดินเท้าเปล่า** · ตรวจในรองเท้าก่อนใส่ · **รองเท้าพอดี** หัวกว้างลึก ส้นเตี้ย มีสายรัด · ระวังน้ำร้อน/กระเป๋าน้ำร้อน | 2 |
| 9 | **เลิกบุหรี่** · คุมน้ำตาล ความดัน ไขมัน · ถ้ามีแผล บวมแดง หรือเท้าอุ่นผิดปกติให้มาทันที · นัดตรวจเท้าบ่อยขึ้น · ยาลดปวดปลายประสาท | 1 |

**ข้อที่ทำให้เสียคะแนน**: ตรวจเท้าข้างเดียว · ไม่ถอดถุงเท้า · ใช้ monofilament ลากหรือกดบน callus · ไม่ให้คำแนะนำเรื่องรองเท้าและการตรวจเท้าทุกวัน""",
 "ref": ["สไลด์ ศ.นพ.ชัยชาญ — prevention diabetic foot ulcer, high risk foot, monofilament, good footwear, daily footcare", "IWGDF 2023"],
 "nl": ["2.3.6-3(9)", "2.3.12(13)", "2.3.9-3(7)", DM], "years": [], "_kind": "meq", "_set": SET}]

LECTURE = {
 "lec": LEC, "date": "พ. 14 ต.ค.",
 "title": "Diabetes mellitus — ตั้งแต่วินิจฉัยถึง DKA",
 "subtitle": "insulin ทำงานที่ไหน · ทำไมปัสสาวะมาก น้ำหนักลด ตามัว · วินิจฉัยและคัดกรอง · T1 · T2 และ C-peptide · GDM · DKA/HHS กลไกและการรักษา · hypoglycemia · retinopathy · nephropathy · neuropathy และเท้า · macrovascular และเป้าหมาย · ยาเม็ด/GLP-1/SGLT2 · Thai CPG 2020 และ insulin",
 "objectives": [
   "อธิบายการออกฤทธิ์ของ insulin ที่ตับ กล้ามเนื้อ และไขมัน และใช้อธิบายกลไกของอาการเบาหวาน (ปัสสาวะมาก กระหายน้ำ น้ำหนักลด ตามัว ติดเชื้อง่าย)",
   "วินิจฉัยเบาหวานและภาวะก่อนเบาหวาน และบอกได้ว่าใครต้องคัดกรอง",
   "แยกเบาหวานชนิดที่ 1 ชนิดที่ 2 ชนิดจำเพาะ และ GDM จากกลไกและลักษณะทางคลินิก รวมถึงการใช้ C-peptide",
   "อธิบายกลไก Pedersen ของภาวะแทรกซ้อนในทารกของแม่ที่เป็น GDM และแปลผล OGTT ในหญิงตั้งครรภ์",
   "อธิบายกลไกของ DKA และ HHS วินิจฉัย คำนวณ AG/corrected Na/osmolality และสั่งการรักษาโดยเฉพาะสารน้ำ insulin และ K",
   "รู้จักอาการและการรักษา hypoglycemia รวมถึง unawareness",
   "อธิบายกลไกและการคัดกรองภาวะแทรกซ้อนทางตา ไต เส้นประสาท เท้า และหลอดเลือดใหญ่",
   "เลือกยาลดน้ำตาลตามกลไก ผลข้างเคียง และโรคร่วมตามแนวทางเวชปฏิบัติไทย 2020 และใช้ insulin ได้ถูกต้อง"],
 "nlGap": "เกณฑ์ฯ ครอบคลุมเบาหวาน (`นล. 2.3.4(1)`, `B11.2.5(4)`) hyperglycemic crisis (`2.2.16`) hypoglycemia (`2.2.17`) retinopathy polyneuropathy และยาเบาหวาน (`B11.4(1)`) ครบ — แต่ **สไลด์ไม่มีเนื้อหา DKA/HHS/hypoglycemia** (มีแค่ชื่อในขั้นที่ 4 ของ approach) และหลายส่วนเป็นภาพ (ความชุก NHES7 กราฟ natural history ภาพจอตา/เท้า) หัวข้อ 7–9 และส่วนที่ระบุในแต่ละหัวข้อจึงอิงแนวทางด้านล่าง",
 "guidelines": [
   "**แนวทางเวชปฏิบัติสำหรับโรคเบาหวาน 2020 (TH DM CPG 2020)** — อัลกอริทึมการรักษา T2 และเป้าหมายตอนวินิจฉัย (อาจารย์อ้างในสไลด์)",
   "**ADA/EASD/JBDS/AACE/DTS — Hyperglycemic Crises in Adults With Diabetes: A Consensus Report (2024)** — เกณฑ์ DKA/HHS และเกณฑ์หายใหม่",
   "**ADA — Hyperglycemic Crises in Adult Patients With Diabetes (Kitabchi 2009)** — ขั้นตอนสารน้ำ insulin K bicarbonate ที่ยังใช้สอน",
   "**ADA Standards of Care in Diabetes** — hypoglycemia levels, การคัดกรอง, เป้าความดัน/ไขมัน, GDM หลังคลอด, เลือกยาตามโรคร่วม",
   "**KDIGO 2022 Clinical Practice Guideline for Diabetes Management in CKD** — SGLT2i, metformin ตาม eGFR, finerenone",
   "**IWGDF 2023 guidelines on the prevention and management of diabetes-related foot disease**",
   "**WHO/IADPSG และ Carpenter–Coustan/NDDG** — เกณฑ์ GDM (อาจารย์อ้างในสไลด์)"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ───────────────────────────── กระจายตำแหน่งคำตอบ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น) · ตัวเลือกเรียงตามธรรมชาติไม่สลับ
ORDERED = {N(5), N(12)}
_slot = 0
for s_ in S:
    for it in s_["items"]:
        if it["id"] in ORDERED:
            continue
        tgt = [2, 4, 0, 3, 1][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

# ───────────────────────────── เขียนลงไฟล์ แล้วผูกข้อ Mock
path = os.path.join(BUILD, "data", SET + ".json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LEC]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
added_m = link_mock(SET, LEC, {"endo-dm-04": ["MOCK-192"], "endo-dm-07": ["MOCK-190"], "endo-dm-08": ["MOCK-189"],
                               "endo-dm-11": ["MOCK-191", "MOCK-124"], "endo-dm-12": ["MOCK-188"]})

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
print("sections %d | ข้อใหม่ %d + mock %d = %d | meq %d | osce %d | ภาพ %d | nl %d" % (
    len(S), sum(1 for s_ in S for i in s_["items"] if i["id"].startswith("END-DM")), added_m,
    sum(len(s_["items"]) for s_ in L["sections"]), len(L["meq"]), len(L["osce"]), sum(len(s_["figs"]) for s_ in S), len(codes)))
print("ตำแหน่งคำตอบข้อใหม่:", dict(sorted(Counter(i["answer"] for s_ in S for i in s_["items"] if i["id"].startswith("END-DM")).items())))
print("%s.json มี %d คาบ: %s" % (SET, len(data), [l["lec"] for l in data]))
