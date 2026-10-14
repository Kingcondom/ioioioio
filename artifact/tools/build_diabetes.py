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

# ═══════════════════════════ END SECTIONS
