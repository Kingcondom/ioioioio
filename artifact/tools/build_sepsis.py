#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Septicemia and antibiotic usage (อ.พจน์ · ศ. 25 ก.ย. 2569) → data/id.json (ชุดใหม่ ID · Infectious Diseases)
สไลด์ "Sepsis _ Principle ATB medical student.pdf" (Drive 10qgsfnxQl7wacVkNBSAF5SXe8Bx4vPDc) เป็นภาพล้วน 175 MB
ดึงข้อความไม่ได้ → เรียบเรียงจาก Surviving Sepsis Campaign 2026 (ตรวจกับหน้า SCCM) + บทเรียน Sepsis ของผู้ใช้
ที่ทำคู่ lecture นี้ + หลักการใช้ยาปฏิชีวนะ · โน้ตที่ slides/sepsis_notes.md
ถ้าได้ภาพสไลด์จริงมา ให้เทียบแล้วแก้ไฟล์นี้"""
import json, os, random

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # artifact/
NLN = ["2.2.48", "2.2.7"]
SRC = "Surviving Sepsis Campaign 2026 + หลักการใช้ยาปฏิชีวนะ (คู่ lecture อ.พจน์)"
SSC = "Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2026 (CCM/ICM 2026)"
S = []

def sec(sid, title, summary, minutes, md, pearls, items, nl=None):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": SRC,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})

def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    order = list(range(5)); random.Random("own-" + iid).shuffle(order)   # กระจายตำแหน่งเฉลยแบบคงที่
    choices, answer = [choices[k] for k in order], order.index(answer)
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}

N = lambda n: "ID-SEP-MCQ-%02d" % n

# ───────────────────────────── 1
sec("id-sep-01", "นิยาม Sepsis-3 และคัดกรองด้วยอะไร",
    "ติดเชื้อ + อวัยวะล้มเหลวจากการตอบสนองที่เสียการควบคุม · SOFA ↑ ≥ 2 · septic shock · NEWS/MEWS/SIRS แทน qSOFA", 8,
"""> **หมายเหตุที่มา** — สไลด์ของ อ.พจน์ เป็นภาพล้วนที่ดึงข้อความไม่ได้ คาบนี้จึงเรียบเรียงจาก **Surviving Sepsis Campaign 2026** และหลักการใช้ยาปฏิชีวนะมาตรฐาน (ดูกล่อง *ครอบคลุมจุดประสงค์ นล.* ด้านบน)

### นิยาม (Sepsis-3, 2016 — SSC 2026 ใช้ต่อ)
| คำ | นิยาม |
|---|---|
| **Sepsis** | **ติดเชื้อ + อวัยวะล้มเหลวที่คุกคามชีวิต** จากการตอบสนองของร่างกายที่ **เสียการควบคุม** · ใช้งานจริง = **SOFA เพิ่ม ≥ 2 คะแนน** จากเดิม |
| **Septic shock** | sepsis ที่ต้องใช้ **vasopressor ให้ MAP ≥ 65** และ **lactate > 2 mmol/L** **ทั้งที่ให้สารน้ำพอแล้ว** — ตายมากกว่า 40% |

คำว่า "severe sepsis" และ SIRS-based sepsis **ยกเลิกไปแล้ว**

### SOFA หกระบบ
**ปอด** (PaO₂/FiO₂) · **เกล็ดเลือด** · **ตับ** (bilirubin) · **หัวใจหลอดเลือด** (MAP/vasopressor) · **สมอง** (GCS) · **ไต** (creatinine/ปัสสาวะ)

### คัดกรอง — SSC 2026 ชัดขึ้น
- ใช้ **NEWS/NEWS2, MEWS หรือ SIRS** คัดกรองผู้ป่วยในที่อาการหนัก **แทน qSOFA**
- **qSOFA** (RR ≥ 22 · สับสน · SBP ≤ 100) **ไวไม่พอเป็นตะแกรง** — ใช้ทำนายความเสี่ยงตาย ไม่ใช่คัดกรอง
- **ไม่มี biomarker ตัวเดียว** ยืนยันหรือตัด sepsis — เป็น **การวินิจฉัยทางคลินิก**
- คัดกรองบวกแล้วเรียกทีม (code sepsis/sepsis huddle) — ใหม่ในปี 2026

| SIRS (≥ 2 ข้อ) | |
|---|---|
| อุณหภูมิ | > 38 หรือ < 36 °C |
| ชีพจร | > 90/min |
| หายใจ | > 20/min หรือ PaCO₂ < 32 |
| WBC | > 12,000 หรือ < 4,000 หรือ band > 10% |""",
    ["Sepsis = ติดเชื้อ + SOFA ↑ ≥ 2 · septic shock = vasopressor ให้ MAP ≥ 65 + lactate > 2 หลังให้น้ำพอ",
     "SSC 2026: คัดกรองด้วย NEWS/MEWS/SIRS ไม่ใช่ qSOFA",
     "ไม่มีแล็บตัวเดียวยืนยัน/ตัด sepsis"],
    [mcq(N(1), "A 66-year-old woman with pyelonephritis remains hypotensive after 30 mL/kg of balanced crystalloid and requires norepinephrine to keep MAP at 65 mmHg. Lactate is 3.8 mmol/L. How should this be classified?",
         ["Sepsis without shock", "Severe sepsis", "Septic shock", "SIRS only", "Bacteraemia without sepsis"], 2,
         "นิยาม **septic shock (Sepsis-3)** = sepsis ที่ **ต้องใช้ vasopressor ให้ MAP ≥ 65** ร่วมกับ **lactate > 2 mmol/L** **ทั้งที่ให้สารน้ำเพียงพอแล้ว** — ผู้ป่วยเข้าทั้งสามข้อ\n\nคำว่า **severe sepsis ถูกยกเลิก** ตั้งแต่ Sepsis-3 · SIRS เป็นเครื่องมือคัดกรอง ไม่ใช่นิยาม",
         "Septic shock = vasopressor (MAP ≥ 65) + lactate > 2 หลังให้น้ำพอ", "Sepsis-3 definitions",
         ["Singer M et al. Sepsis-3. JAMA 2016;315:801", SSC], ["2.2.48", "2.2.7", "B7.2.5(4)"]),
     mcq(N(2), "A hospital wants a bedside tool for nurses to screen ward patients for possible sepsis. According to the Surviving Sepsis Campaign 2026, which approach is recommended?",
         ["qSOFA alone", "Serum procalcitonin on every febrile patient", "NEWS/NEWS2, MEWS or SIRS rather than qSOFA", "Lactate on every patient with a fever", "Blood cultures before any screening"], 2,
         "SSC 2026 **แนะนำ NEWS, NEWS2, MEWS หรือ SIRS แทน qSOFA** ในการคัดกรองผู้ป่วยที่อาการหนักในโรงพยาบาล และ **ไม่ใช้ qSOFA เป็นเครื่องมือคัดกรองเดี่ยว** เพราะไวไม่พอ (ผู้ป่วย sepsis จำนวนมาก qSOFA < 2)\n\nไม่มี biomarker ตัวเดียว (PCT, lactate) ใช้คัดกรองหรือยืนยัน sepsis ได้",
         "คัดกรอง sepsis = NEWS/MEWS/SIRS · qSOFA ไม่ใช่ตะแกรง", "Sepsis screening",
         [SSC + " – screening"], ["2.2.48", "2.1.1"])],
    ["2.2.48", "2.2.7", "B7.2.5(4)"])

# ───────────────────────────── 2
sec("id-sep-02", "กลไก — ท่อรั่ว ท่อขยาย ท่อตัน โรงงานดับ",
    "PAMPs/DAMPs → TLR → cytokine · glycocalyx หลุด + NO · DIC · mitochondria และ lactate · immunoparalysis", 9,
"""### หกขั้นจากเชื้อสู่อวัยวะล้มเหลว
1. **สัญญาณเตือนภัย** — ชิ้นส่วนเชื้อ (**PAMPs** เช่น **LPS** ของแกรมลบ) และเศษเซลล์ตาย (**DAMPs**) จับ **TLR** (เช่น TLR4) → **NF-κB** → หลั่ง **TNF-α, IL-1, IL-6**
2. **อักเสบเกินและกดภูมิพร้อมกัน** — ระยะต่อมาเกิด **immunoparalysis** จึงติดเชื้อซ้ำ (เชื้อในโรงพยาบาล ไวรัสกลับมา) ได้ง่ายในสัปดาห์ต่อไป
3. **ผนังหลอดเลือดพัง** — **glycocalyx** หลุด → **capillary leak** · **iNOS** สร้าง **nitric oxide** มาก → หลอดเลือดขยาย ความดันตก ระยะแรกมือเท้าอุ่น (*warm shock*)
4. **เลือดแข็งตัวผิดที่** — **tissue factor** ถูกกระตุ้น · **protein C และ antithrombin ลด** → ลิ่มเลือดเล็กอุดหลอดเลือดฝอย → **DIC**
5. **โรงงานในเซลล์ดับ** — mitochondria ใช้ O₂ ไม่ได้แม้ส่งถึง + adrenaline กระตุ้น **β2 เร่ง glycolysis** → **lactate สูง** (ไม่ได้แปลว่าขาดออกซิเจนเสมอไป)
6. **อวัยวะล้มเหลว** — AKI · ARDS · สับสน · ตับ · เกล็ดเลือดต่ำ

### หลักจำ (จากบทเรียนที่ทำคู่ lecture)
| กลไก | ผล | แก้ด้วย |
|---|---|---|
| **ท่อรั่ว** | capillary leak น้ำในหลอดเลือดหาย | **crystalloid ≥ 30 mL/kg ใน 3 ชม.** |
| **ท่อขยาย** | NO → vasodilation MAP ตกแม้ให้น้ำ | **norepinephrine** เป้า MAP 65 |
| **ท่อตัน** | microthrombi ผิวลาย CRT ช้า | ดู CRT + lactate ประเมินซ้ำ |
| **โรงงานดับ** | ต้นเหตุคือเชื้อยังอยู่ | **ยาปฏิชีวนะตามนาฬิกา + source control ≤ 6 ชม.** |

> นี่คือ **distributive shock** ในคาบ Circulatory shock — **CO สูง SVR ต่ำมาก** CVP/PCWP ต่ำ · ระยะท้ายหัวใจบีบตัวลดได้ (septic cardiomyopathy)""",
    ["LPS → TLR4 → NF-κB → TNF-α/IL-1/IL-6",
     "NO → vasodilation · glycocalyx หลุด → leak · tissue factor ↑ protein C ↓ → DIC",
     "Lactate สูงจาก β2 + mitochondria ด้วย ไม่ใช่แค่ขาด O₂"],
    [mcq(N(3), "In early septic shock, a patient has warm extremities, bounding pulses and a wide pulse pressure despite hypotension. Which mediator is chiefly responsible for the vasodilation?",
         ["Endothelin-1 from damaged endothelium", "Nitric oxide produced by inducible nitric oxide synthase", "Angiotensin II", "Antidiuretic hormone excess", "Thromboxane A2"], 1,
         "Cytokine (TNF-α, IL-1) กระตุ้น **inducible NOS (iNOS)** ในผนังหลอดเลือดและเม็ดเลือดขาว → **NO ปริมาณมาก** → กล้ามเนื้อเรียบคลายตัว → **SVR ต่ำมาก** = distributive shock ระยะแรกที่มือเท้าอุ่น ชีพจรแรง pulse pressure กว้าง\n\nร่วมกับ **vasopressin ในเลือดต่ำเกินสัมพัทธ์** ในช็อกนาน ๆ จึงมีเหตุผลที่เติม vasopressin เมื่อ NE ขนาดสูงขึ้น",
         "Septic vasodilation = iNOS → NO", "Pathophysiology of septic shock",
         ["Harrison's 21e – Sepsis and septic shock", SSC], ["B1.4.6", "B7.2.5(4)", "2.2.7"]),
     mcq(N(4), "A septic patient on norepinephrine has a normal cardiac output and adequate oxygen saturation, yet lactate remains 4 mmol/L. Which statement about lactate in sepsis is correct?",
         ["Raised lactate always proves tissue hypoxia, so more fluid must be given until it normalises", "Lactate can be raised by β2-adrenergic stimulation of glycolysis and mitochondrial dysfunction; follow its trend rather than chasing a normal value",
          "Lactate has no prognostic value in sepsis", "Lactate is raised only in liver failure", "Lactate should be measured once only"], 1,
         "Lactate ใน sepsis มาจาก **หลายกลไก** — hypoperfusion จริง · **adrenaline/NE กระตุ้น β2 เร่ง glycolysis** · **mitochondria ใช้ O₂ ไม่ได้** · ตับกำจัดได้ลดลง\n\nจึง **ไม่ให้น้ำไล่จน lactate ปกติ** (เสี่ยงน้ำเกิน) แต่ใช้ **แนวโน้มที่ลดลง** ร่วมกับ CRT และ dynamic measures · SSC 2026 แนะนำ **วัด lactate ซ้ำ** เพื่อนำการกู้ชีพ · lactate > 2 เป็นส่วนหนึ่งของนิยาม septic shock และทำนายการตาย",
         "Lactate สูง ≠ ขาด O₂ เสมอ — ดูแนวโน้ม อย่าให้น้ำไล่", "Lactate in sepsis",
         [SSC + " – serial lactate"], ["2.2.48", "B7.2.5(4)"])],
    ["2.2.48", "B1.4.6", "B7.2.5(4)"])

# ───────────────────────────── 3
sec("id-sep-03", "สี่ระดับความมั่นใจ และนาฬิกายาปฏิชีวนะ 1·1·3·รอ",
    "definite · probable · possible · unlikely × มีช็อกหรือไม่ → เวลาเริ่มยา · ระดับเปลี่ยนได้ · โรคเลียนแบบ sepsis", 9,
"""### ทำไมต้องมีภาษากลาง
"suspected sepsis" กว้างเกินไป — คนหนึ่งหมายถึงโอกาส 90% อีกคน 30% SSC 2026 จึงกำหนด **4 ระดับ** แล้ว **ผูกเวลาเริ่มยาเข้ากับระดับ × ช็อก**

| ระดับ | ความหมาย |
|---|---|
| **Definite** | ยืนยันแล้ว — โรคอื่นแทบเป็นไปไม่ได้ |
| **Probable** | sepsis เป็นคำวินิจฉัย **อันดับหนึ่ง** |
| **Possible** | เป็นได้ แต่โรคอื่นก็พอ ๆ กัน |
| **Unlikely** | โรคอื่นน่าจะเป็นมากกว่า |

### นาฬิกา "1 · 1 · 3 · รอ" (นับจากตอนเริ่มสงสัย)
| ระดับ | **มีช็อก** | **ไม่มีช็อก** |
|---|---|---|
| Definite | **≤ 1 ชม.** | **≤ 1 ชม.** |
| Probable | **≤ 1 ชม.** | **≤ 1 ชม.** |
| Possible | **≤ 1 ชม.** | **สืบค้นเร็วแบบจำกัดเวลา → ถ้ายังสงสัย ให้ภายใน 3 ชม.** |
| Unlikely | รักษาเหตุของช็อกที่นำหน้า | **ชะลอยา เฝ้าดูใกล้ชิด** |

**ทำไมไม่ให้ทุกคนภายใน 1 ชม.** — ผู้ป่วยที่ถูกสงสัยจำนวนมากสุดท้ายไม่ได้ติดเชื้อ ยากว้างทุกรายได้ผลข้างเคียง *C. difficile* และเชื้อดื้อยาโดยไม่ได้ประโยชน์ · แต่เมื่อ **ช็อก** ความเสี่ยงตายต่อชั่วโมงที่ช้าสูงมาก ตาชั่งจึงเอียงไปทาง "ให้เลย"

> **ระดับไม่ใช่ป้ายถาวร** — ผลเพาะเชื้อหรือภาพรังสีเลื่อนขึ้นลงได้ · ถ้าพบสาเหตุอื่นชัดเจน **หยุดยาที่ให้แบบคาดการณ์**

### โรคเลียนแบบ sepsis — คิดก่อนติดป้าย probable
**PE · ตับอ่อนอักเสบ · MI/cardiogenic shock · GI bleed · adrenal crisis · DKA · thyroid storm · anaphylaxis · แพ้ยา/DRESS · TRALI · heat stroke · NMS/serotonin syndrome · vasculitis/SLE flare · tumor fever**""",
    ["ช็อก (ระดับใดก็ตามที่ไม่ใช่ unlikely) หรือ probable/definite → ยาปฏิชีวนะ ≤ 1 ชม.",
     "Possible ไม่ช็อก → สืบค้นเร็ว แล้วให้ภายใน 3 ชม. ถ้ายังสงสัย",
     "Unlikely ไม่ช็อก → ชะลอยา เฝ้าดู · เจอเหตุอื่นให้หยุดยา"],
    [mcq(N(5), "An 84-year-old nursing-home resident has 1 day of new confusion and a temperature of 37.9 °C. There is no obvious source. BP 124/66 mmHg, lactate 2.3 mmol/L. Dehydration, stroke and hyponatraemia are also being considered. According to SSC 2026, what is the most appropriate antimicrobial strategy?",
         ["Give broad-spectrum antibiotics within 1 hour", "Withhold antibiotics for 48 hours", "Take blood cultures and perform rapid, time-limited investigations; if infection is still suspected, start antimicrobials within 3 hours",
          "Start antifungal therapy", "Wait for procalcitonin before deciding"], 2,
         "**Possible sepsis ไม่มีช็อก** — เป็นได้แต่โรคอื่นก็มีโอกาสพอกัน\n\nSSC 2026: **เพาะเชื้อ + สืบค้นเร็วแบบจำกัดเวลา** (UA, CXR, electrolyte, glucose, CT สมองถ้าจำเป็น) → **ถ้ายังสงสัยติดเชื้อ ให้ยาภายใน 3 ชม.** นับจากเริ่มสงสัย · ถ้าความดันตกระหว่างนั้น → ย้ายไปแถว \"ช็อก\" ให้ยาภายใน 1 ชม.\n\n**PCT ไม่ใช้ตัดสินใจเริ่มยา**",
         "Possible + ไม่ช็อก → สืบค้นเร็ว → ยาภายใน 3 ชม.", "Antimicrobial timing by sepsis certainty",
         [SSC + " – timing of antimicrobials"], ["2.2.48", "2.1.1"]),
     mcq(N(6), "A 45-year-old man with heavy alcohol use has severe epigastric pain radiating to the back after a party. Lipase is 12 times the upper limit, temperature 37.8 °C, WBC 14,500/µL, blood pressure normal. Which approach is most appropriate?",
         ["Start meropenem within 1 hour for probable sepsis", "Classify as unlikely sepsis (inflammation from acute pancreatitis); give fluids and analgesia, defer antibiotics and monitor closely",
          "Start empirical fluconazole", "Give antibiotics within 3 hours as possible sepsis", "Give prophylactic antibiotics to prevent infected necrosis"], 1,
         "อาการและ lipase เข้ากับ **acute pancreatitis** ที่ทำให้ **SIRS** โดยไม่มีหลักฐานติดเชื้อ = **unlikely sepsis** และไม่มีช็อก → SSC 2026 **แนะนำชะลอยาปฏิชีวนะ เฝ้าดูใกล้ชิด**\n\nยาปฏิชีวนะป้องกันใน pancreatitis **ไม่แนะนำ** · ถ้าต่อมาสงสัย **infected necrosis** (ไข้สูงขึ้น อาการแย่ลงหลังสัปดาห์แรก แก๊สใน necrosis) ค่อยเลื่อนระดับ",
         "Pancreatitis + SIRS ไม่ช็อก = unlikely sepsis → ชะลอยา", "Sepsis mimics",
         [SSC + " – unlikely sepsis"], ["2.2.48"])],
    ["2.2.48", "2.1.1"])

# ───────────────────────────── 4
sec("id-sep-04", "ชั่วโมงแรก — เพาะเชื้อ วัด lactate และ procalcitonin ใช้ตอนไหน",
    "blood culture 2 ชุดก่อนยา (ถ้าไม่ทำให้ยาช้า) · lactate · PCT ไม่ใช้เริ่มยา ใช้ช่วยหยุด · ABCDE", 7,
"""### ลำดับการทำงานในชั่วโมงแรก
1. **ABCDE** · O₂ ตามเป้า · IV ขนาดใหญ่ 2 เส้น
2. **Blood culture อย่างน้อย 2 ชุด (aerobic + anaerobic) ก่อนยา** — เมื่อทำได้โดย **ไม่ทำให้ยาช้า** · เพาะเชื้อจากแหล่งที่สงสัย (ปัสสาวะ เสมหะ หนอง)
3. **Lactate** + CBC, BUN/Cr, LFT, coagulation, glucose, electrolyte · ABG ถ้าหอบ
4. **ยาปฏิชีวนะตามนาฬิกา** (หัวข้อก่อน)
5. **สารน้ำ** ถ้า hypoperfusion/ช็อก → **vasopressor** ถ้า MAP ยัง < 65
6. **หาแหล่งติดเชื้อและวางแผน source control** (ภาพรังสี US CT)
7. ประเมินซ้ำทุกชั่วโมง — BP, CRT, สติ, ปัสสาวะ ≥ 0.5 mL/kg/h, lactate

### Procalcitonin — ใช้ให้ถูกจังหวะ
| สถานการณ์ | SSC 2026 |
|---|---|
| ตัดสินใจ **เริ่ม** ยา | **ไม่แนะนำ** — ใช้การประเมินทางคลินิก |
| ตัดสินใจ **หยุด** ยา เมื่อระยะเวลาที่เหมาะไม่ชัด | **ใช้ร่วมกับการประเมินทางคลินิกได้** |

### เพาะเชื้อเลือดขึ้น — อ่านอย่างไร
- **เชื้อก่อโรคจริงแม้ขวดเดียว** — *S. aureus*, *Streptococcus pneumoniae*, แกรมลบ (E. coli, Klebsiella, *Burkholderia pseudomallei*), *Candida*
- **มักเป็นเชื้อปนเปื้อนถ้าขึ้นขวดเดียว** — coagulase-negative staphylococci, *Corynebacterium*, *Bacillus*, *Cutibacterium* (ยกเว้นมีสายสวน/อุปกรณ์เทียม)
- **S. aureus bacteremia** → ต้องหา source เสมอ ทำ echocardiography และให้ยาฉีดอย่างน้อย 14 วัน""",
    ["Hemoculture ≥ 2 ชุดก่อนยา — ถ้าไม่ทำให้ยาช้า",
     "PCT: ไม่ใช้เริ่มยา · ใช้ช่วยหยุดได้",
     "CoNS ขวดเดียว = มักปนเปื้อน · S. aureus ขวดเดียว = ของจริง"],
    [mcq(N(7), "A 60-year-old man with community-acquired pneumonia is hypotensive (BP 82/50 mmHg). The phlebotomist cannot obtain blood cultures after two attempts over 30 minutes. What should be done?",
         ["Keep trying until two sets of blood cultures are obtained before giving antibiotics", "Give the first dose of antibiotics now and continue attempts to obtain cultures",
          "Wait for an arterial line to be placed", "Send procalcitonin and decide after the result", "Give only fluids until cultures are obtained"], 1,
         "SSC — เพาะเชื้อเลือด **ก่อนยา เมื่อทำได้โดยไม่ทำให้ยาช้าอย่างมีนัยสำคัญ** · ผู้ป่วยรายนี้ **ช็อก** = นาฬิกา **≤ 1 ชั่วโมง** ทุกชั่วโมงที่ช้าเพิ่มการตาย\n\nจึง **ให้ยาเลย** แล้วพยายามเก็บเพาะเชื้อต่อ (และเก็บเสมหะ/ปัสสาวะ) · PCT ไม่ใช้ตัดสินใจเริ่มยา",
         "ช็อก: อย่าให้การเก็บเพาะเชื้อทำให้ยาช้า", "Blood cultures and antibiotic timing",
         [SSC + " – cultures before antimicrobials"], ["2.2.48", "2.2.7", "3.3.9"]),
     mcq(N(8), "A patient admitted for urinary sepsis grows coagulase-negative staphylococci in 1 of 2 blood culture sets after 48 hours. He has no intravascular catheter or prosthetic device and is improving on ceftriaxone. What is the most likely interpretation?",
         ["Staphylococcal endocarditis; start vancomycin for 6 weeks", "Probable skin contaminant; no anti-staphylococcal therapy is needed",
          "Methicillin-resistant S. aureus bacteraemia", "Treatment failure; switch to meropenem", "Indication for transoesophageal echocardiography"], 1,
         "**Coagulase-negative staphylococci (CoNS) ขึ้นเพียง 1 ใน 2 ชุด** ในผู้ป่วยที่ไม่มีสายสวนหลอดเลือดหรืออุปกรณ์เทียม และอาการดีขึ้น = **เชื้อปนเปื้อนจากผิวหนัง** มากที่สุด\n\nเหตุผลที่ต้องเก็บ **อย่างน้อย 2 ชุด** คือแยกปนเปื้อนออกจากเชื้อจริงแบบนี้ · ต่างจาก **S. aureus** ที่ขึ้นขวดเดียวก็ถือเป็นของจริงเสมอ",
         "CoNS 1 ใน 2 ชุด ไม่มีอุปกรณ์ = ปนเปื้อน", "Interpreting blood cultures",
         ["IDSA – blood culture interpretation", "Harrison's 21e"], ["3.3.9", "B1.5.2(6)"])],
    ["2.2.48", "3.3.9", "3.3.10"])

# ───────────────────────────── 5
sec("id-sep-05", "สารน้ำ — 30 mL/kg ใน 3 ชั่วโมง และเลือกชนิดให้ถูก",
    "balanced > NSS · albumin เฉพาะบางราย · ห้าม starch/gelatin · dynamic measures · CRT · อย่าให้น้ำไล่ lactate", 7,
"""### ปริมาณ
- Hypoperfusion หรือช็อก → **crystalloid อย่างน้อย 30 mL/kg ใน 3 ชม. แรก** (ปรับตามผู้ป่วย — หัวใจล้มเหลว ไตวาย)
- **BMI > 30** คิดจาก adjusted/ideal body weight
- ตัวอย่าง: 60 kg × 30 = **1,800 mL ใน 3 ชม.** แล้ว **ประเมินซ้ำ** (BP, CRT, ปอด, ปัสสาวะ)

### ชนิด
| สารน้ำ | SSC 2026 |
|---|---|
| **Balanced crystalloid** (Ringer's lactate/acetate) | **ดีกว่า NSS** — NSS ปริมาณมากทำ hyperchloremic acidosis และ AKI · ยกเว้น **TBI ใช้ NSS** |
| Albumin | **เฉพาะ** ได้ crystalloid ไปมากแล้ว หรือ **ตับแข็ง** |
| **Starch (HES)** | **ห้าม** (ไตวาย ตายเพิ่ม) |
| Gelatin | **ไม่แนะนำ** |

### ประเมินว่าให้น้ำต่อหรือพอ
- **Dynamic measures** — **passive leg raise** (ยกขา 45° ดู SV/CO เพิ่ม ≥ 10%), SVV, PPV (ใช้ได้เมื่อใส่เครื่องช่วยหายใจ จังหวะสม่ำเสมอ)
- **Capillary refill time** — ทำซ้ำง่าย ใช้นำการกู้ชีพได้
- **Lactate** ดูแนวโน้มลดลง — **อย่าให้น้ำไล่จนปกติ**
- สัญญาณน้ำเกิน: crackles ปอด SpO₂ ตก JVP สูง B-lines บน US
- ช็อกไม่เสถียร (ผิวลาย ซึม) **ให้ vasopressor พร้อมน้ำได้เลย** ไม่ต้องรอให้น้ำครบ
- ผ่านช่วงกู้ชีพแล้ว → ดึงน้ำออก (de-resuscitation)""",
    ["Crystalloid ≥ 30 mL/kg ใน 3 ชม. · balanced > NSS (ยกเว้น TBI)",
     "ห้าม starch · albumin เฉพาะได้น้ำมากแล้ว/ตับแข็ง",
     "ประเมินด้วย PLR, CRT, lactate trend — อย่าให้น้ำไล่ lactate"],
    [mcq(N(9), "A 70-kg woman with septic shock from cholangitis has received 1 L of 0.9% saline. Which fluid plan best follows SSC 2026?",
         ["Hydroxyethyl starch 1 L to restore volume faster", "Continue to a total of at least about 2.1 L of crystalloid in the first 3 hours, preferring a balanced crystalloid such as Ringer's lactate, with frequent reassessment",
          "Stop fluids and start dopamine", "Give 20% albumin as the first-line fluid", "Give fluid boluses until lactate is completely normal"], 1,
         "30 mL/kg × 70 kg = **2,100 mL ใน 3 ชั่วโมงแรก** · SSC 2026 แนะนำ **balanced crystalloid มากกว่า 0.9% saline** · ประเมินซ้ำบ่อยด้วย BP, CRT, PLR, ปัสสาวะ\n\n**Starch ห้ามใช้** · albumin สงวนไว้เมื่อได้ crystalloid ไปมากแล้วหรือมีตับแข็ง · **dopamine ไม่ใช่ยาตัวแรก** · ไม่ให้น้ำไล่จน lactate ปกติ",
         "30 mL/kg × น้ำหนัก ใน 3 ชม. · balanced crystalloid", "Initial fluid resuscitation",
         [SSC + " – fluids"], ["2.2.7", "2.2.48", "B7.2.5(4)"])],
    ["2.2.7", "B7.2.5(4)"])

# ───────────────────────────── 6
sec("id-sep-06", "ยากระตุ้นความดันและ steroid",
    "norepinephrine ตัวแรก ทางหลอดเลือดส่วนปลายได้ · MAP 65 (≥ 65 ปี 60–65) · vasopressin → epinephrine · hydrocortisone", 8,
"""### Vasopressor ตามลำดับ (SSC 2026)
1. **Norepinephrine เป็นตัวแรก** — **เริ่มทางหลอดเลือดส่วนปลายได้เลย** ไม่ต้องรอ central line (ใหม่ปี 2026 — ใช้เส้นใหญ่ใกล้ข้อศอก ตรวจการรั่วบ่อย)
2. **เป้า MAP 65 mmHg** (คุม ± 5) · **อายุ ≥ 65 ปี ใช้ 60–65**
3. NE ขนาดสูงขึ้นเรื่อย ๆ → **เติม vasopressin** (ไม่เพิ่ม NE ไปเรื่อย ๆ)
4. ยังไม่ถึงเป้า → **เติม epinephrine**
5. **หัวใจบีบตัวอ่อน + ยัง hypoperfusion** → **dobutamine + NE** หรือ epinephrine เดี่ยว
6. **ไม่ใช้** dopamine เป็นตัวแรก (arrhythmia มาก) · **ไม่ใช้ terlipressin**

| ยา | Receptor | เหตุผล |
|---|---|---|
| **Norepinephrine** | **α1 > β1** | หดหลอดเลือดเป็นหลัก รักษา CO ไว้ได้ |
| **Vasopressin** | **V1** | septic shock มี vasopressin ในเลือดต่ำเกินสัมพัทธ์ · ประหยัด NE |
| Epinephrine | β1 + α1 (+ β2) | เพิ่ม CO ด้วย · lactate สูงขึ้นจาก β2 |
| Dobutamine | β1 (+ β2) | inotrope · ความดันอาจตก |

### Corticosteroid
**Septic shock → IV corticosteroid** (เช่น **hydrocortisone 200 mg/วัน** แบ่งให้) เมื่อ vasopressor ยังจำเป็น — ช่วยให้หลุดจากยากระตุ้นความดันเร็วขึ้น

### สิ่งที่ SSC 2026 แนะนำ **ไม่ให้**
vitamin C · IVIG · vitamin D · probiotics · β-blocker (esmolol/landiolol) · terlipressin · levosimendan · blood purification/polymyxin B hemoperfusion · ยาลดไข้เพื่อหวังลดการตาย (ให้เพื่อความสบายได้)""",
    ["NE ตัวแรก ทางหลอดเลือดส่วนปลายได้ · MAP 65 · อายุ ≥ 65 → 60–65",
     "NE ขึ้นเรื่อย ๆ → vasopressin → epinephrine · หัวใจอ่อน → dobutamine",
     "Septic shock → hydrocortisone · ไม่ใช้ dopamine ตัวแรก ไม่ให้ vitamin C"],
    [mcq(N(10), "A 72-year-old woman with septic shock remains hypotensive (MAP 55 mmHg) after 30 mL/kg of crystalloid. Central venous access is not yet available. What is the most appropriate next step?",
         ["Wait for central line insertion before starting any vasopressor", "Start dopamine through a peripheral cannula",
          "Start norepinephrine through a large proximal peripheral cannula, targeting MAP about 60–65 mmHg", "Give another 3 L of crystalloid before any vasopressor", "Start terlipressin"], 2,
         "SSC 2026 — **norepinephrine เป็นตัวแรก** และ **แนะนำเริ่มทางหลอดเลือดส่วนปลาย** แทนการรอ central line (ใหม่ปี 2026) · เป้า **MAP 65** แต่ใน **ผู้ป่วยอายุ ≥ 65 ปี ใช้ 60–65**\n\nDopamine ไม่ใช่ยาตัวแรก (arrhythmia มากกว่า) · terlipressin แนะนำไม่ให้ · ให้น้ำต่อโดยไม่ประเมินเสี่ยงน้ำเกิน",
         "Septic shock + MAP ต่ำหลังให้น้ำ → NE ทางส่วนปลายได้เลย", "Vasopressors in septic shock",
         [SSC + " – vasopressors"], ["2.2.7", "B7.2.5(4)"]),
     mcq(N(11), "A patient with septic shock requires norepinephrine at a steadily escalating dose to maintain MAP 65 mmHg. What does SSC 2026 suggest adding next?",
         ["Dopamine", "Phenylephrine", "Vasopressin", "Esmolol", "Vitamin C"], 2,
         "SSC 2026 — เมื่อ **NE ขนาดสูงขึ้นเรื่อย ๆ ให้เติม vasopressin** (receptor V1) แทนการเพิ่ม NE ต่อไป · เหตุผลคือ septic shock มี **vasopressin ในเลือดต่ำเกินสัมพัทธ์** และช่วยลดขนาด NE\n\nถ้า NE + vasopressin ยังไม่ถึงเป้า → **เติม epinephrine** · ร่วมกับ **IV corticosteroid** · esmolol และ vitamin C แนะนำไม่ให้",
         "NE ขึ้นเรื่อย ๆ → เติม vasopressin", "Second-line vasopressor",
         [SSC + " – vasopressin"], ["2.2.7", "B7.2.5(4)"])],
    ["2.2.7", "B7.2.5(4)", "2.2.48"])

# ───────────────────────────── 7
sec("id-sep-07", "หลักการใช้ยาปฏิชีวนะ 1 — empirical ให้ตรงแหล่ง แล้วค่อยแคบลง",
    "คิดสามคำถาม: ติดที่ไหน · เชื้ออะไร · ผู้ป่วยเป็นใคร · Gram stain ช่วยเลือก · ยาหลักแต่ละกลุ่มครอบคลุมอะไร", 10,
"""*(ส่วน \"Principle ATB\" ของ lecture — เรียบเรียงจากหลักการมาตรฐาน)*

### สามคำถามก่อนเลือกยา
1. **ติดเชื้อที่ไหน** (ปอด ทางเดินปัสสาวะ ช่องท้อง ผิวหนัง สมอง สายสวน) → เชื้อที่น่าจะเป็น
2. **ติดจากที่ไหน** — ชุมชน / โรงพยาบาล / เคยได้ยากว้าง → **เสี่ยงเชื้อดื้อยา**
3. **ผู้ป่วยเป็นใคร** — ภูมิคุ้มกัน การทำงานของไตตับ แพ้ยา ตั้งครรภ์ ภูมิลำเนาและอาชีพ

### Empirical → definitive
- **Empirical** = คลุมเชื้อที่น่าจะเป็นที่สุดจากแหล่งติดเชื้อ ให้เร็วและขนาดเต็ม
- ผลเพาะเชื้อ/ความไวยาออก (48–72 ชม.) → **de-escalate** ให้แคบที่สุดที่ได้ผล → **definitive therapy**
- **Bactericidal** (beta-lactam, aminoglycoside, FQ, vancomycin) จำเป็นใน endocarditis, meningitis, neutropenia · **bacteriostatic** (macrolide, tetracycline, clindamycin, linezolid) ใช้ได้ในการติดเชื้อทั่วไป

### ยาหลักแต่ละกลุ่ม — ครอบคลุมอะไร
| ยา | แกรมบวก | แกรมลบ | Anaerobe | จุดเด่น |
|---|---|---|---|---|
| Penicillin G/ampicillin | Strep, Enterococcus (amp) | น้อย | ปากบน | leptospirosis รุนแรง (PGS) |
| **Amoxicillin-clavulanate** | ✔ | ✔ ชุมชน | **✔** | ปอดสำลัก แผลกัด |
| Cloxacillin/cefazolin | **MSSA**, Strep | — / บางส่วน | — | ผิวหนัง MSSA bacteremia |
| **Ceftriaxone** | Strep (pneumococcus) | **Enterobacterales ชุมชน** | — | CAP, UTI, meningitis |
| **Ceftazidime** | อ่อน | **Pseudomonas, *B. pseudomallei*** | — | **melioidosis** |
| **Piperacillin-tazobactam** | ✔ | **Pseudomonas** | **✔** | ติดเชื้อโรงพยาบาล ช่องท้อง |
| **Meropenem** | ✔ | **ESBL**, Pseudomonas | **✔** | เชื้อดื้อยา septic shock หนัก |
| **Vancomycin** | **MRSA** | — | — | MRSA, *C. difficile* (กิน) |
| Metronidazole | — | — | **✔** | ช่องท้อง *C. difficile* |
| **Doxycycline** | ✔ | บางส่วน | — | **scrub typhus, leptospirosis, rickettsia** |
| Azithromycin | atypical | — | — | Mycoplasma, Legionella |
| Aminoglycoside | — | ✔ (ไม่ใช่ anaerobe) | — | เสริม gram-negative · ไม่ทำงานในหนอง/กรด |

### Gram stain ช่วยเลือก
- **Gram-positive cocci in clusters** → *Staphylococcus* → MSSA cloxacillin/cefazolin · เสี่ยง MRSA vancomycin
- **GPC in pairs/chains** → *Streptococcus*/pneumococcus/Enterococcus
- **Gram-negative bacilli** → Enterobacterales · Pseudomonas · *Burkholderia* (safety pin)
- **Gram-negative diplococci** → *Neisseria*""",
    ["เลือกยา: ติดที่ไหน · ติดจากที่ไหน (เสี่ยงดื้อยา) · ผู้ป่วยเป็นใคร",
     "Empirical ให้เร็วและเต็มขนาด → de-escalate เมื่อรู้เชื้อ",
     "Ceftazidime/meropenem = melioidosis · doxycycline = scrub typhus/lepto · vancomycin = MRSA"],
    [mcq(N(12), "Blood cultures from a septic patient with a cellulitis-associated abscess grow Gram-positive cocci in clusters at 18 hours. The patient has had multiple hospital admissions and haemodialysis via a catheter. Pending identification, which empirical agent should be included?",
         ["Ceftriaxone", "Metronidazole", "Vancomycin", "Gentamicin alone", "Doxycycline"], 2,
         "**Gram-positive cocci in clusters = *Staphylococcus*** · ผู้ป่วยมีปัจจัยเสี่ยง **MRSA** (นอนโรงพยาบาลบ่อย ฟอกเลือดผ่านสายสวน) → empirical ต้องมี **vancomycin**\n\nเมื่อผลออกเป็น **MSSA** ให้ **de-escalate เป็น cloxacillin หรือ cefazolin** ซึ่งฆ่า MSSA ได้ดีกว่า vancomycin · S. aureus bacteremia ต้องหา source ทำ echocardiography และให้ยาฉีดอย่างน้อย 14 วัน",
         "GPC clusters + เสี่ยง MRSA → vancomycin → MSSA ค่อยเปลี่ยน cloxacillin", "Empirical therapy by Gram stain",
         ["Harrison's 21e – Staphylococcal infections", SSC + " – MRSA coverage when high risk"], ["B1.7.2", "B1.5.2(5)", "3.1.9"]),
     mcq(N(13), "Which statement about empirical versus definitive antimicrobial therapy is correct?",
         ["Once started, broad-spectrum antibiotics should be continued for 14 days to prevent resistance", "Empirical therapy should be narrowed (de-escalated) once the pathogen and susceptibilities are known",
          "Empirical therapy should be given at reduced doses until cultures return", "Definitive therapy is chosen before cultures are taken", "De-escalation increases mortality and should be avoided"], 1,
         "**Empirical** ให้ **เร็ว ขนาดเต็ม ครอบคลุมเชื้อที่น่าจะเป็น** · เมื่อรู้เชื้อและความไวยา → **de-escalate** ให้แคบลง = **definitive therapy** · SSC สนับสนุนการ de-escalate ทุกวันเมื่อทำได้ ไม่เพิ่มการตาย และลดเชื้อดื้อยา/C. difficile\n\nการให้ยาขนาดลดในช่วงแรกเป็นความผิดพลาดที่พบบ่อย — dose แรกต้อง **เต็มหรือ loading** แม้ไตเสื่อม",
         "Empirical เต็มขนาด → de-escalate เมื่อรู้เชื้อ", "Antimicrobial stewardship",
         [SSC + " – de-escalation"], ["B1.7.2", "3.3.10", "B1.5.2(7)"])],
    ["B1.7.2", "3.3.10", "B1.5.2(7)"])

# ───────────────────────────── 8
sec("id-sep-08", "หลักการใช้ยาปฏิชีวนะ 2 — PK/PD ขนาดยา และไต",
    "time-dependent vs concentration-dependent · beta-lactam prolonged infusion · loading dose · aminoglycoside วันละครั้ง · ปรับตามไต", 9,
"""### ยาฆ่าเชื้อแบบไหน ให้แบบนั้น
| แบบ | ตัวชี้วัด | ยา | วิธีให้ |
|---|---|---|---|
| **Time-dependent** | **%fT > MIC** (เวลาที่ระดับยาอิสระเหนือ MIC) | **beta-lactam** (penicillin, cephalosporin, carbapenem) | **หยดนาน (prolonged/extended infusion)** หรือแบ่งให้ถี่ |
| **Concentration-dependent** | **Cmax/MIC** + post-antibiotic effect | **aminoglycoside**, (FQ) | **ขนาดสูงวันละครั้ง** |
| **AUC-dependent** | **AUC/MIC** | **vancomycin** (เป้า AUC 400–600), FQ | ปรับตามระดับยา |

**SSC 2026** — beta-lactam **ให้ loading dose แล้วตามด้วย prolonged infusion** ดีกว่า bolus (เพิ่มเวลาที่ยาเหนือ MIC)

### ขนาดยาใน sepsis
- **Dose แรก = เต็มหรือ loading เสมอ** แม้ไตเสื่อม — volume of distribution เพิ่มจาก capillary leak และสารน้ำที่ให้
- **Augmented renal clearance** ในผู้ป่วยหนุ่ม/ไข้ → ขับยาเร็ว ระดับยาต่ำ
- ปรับ **maintenance dose** ตาม CrCl หลัง 24–48 ชม. (AKI จาก sepsis มักฟื้นเร็ว)
- **ไม่ต้องปรับตามไต** — ceftriaxone, doxycycline, azithromycin, metronidazole (ส่วนใหญ่), cloxacillin
- **ต้องปรับ** — aminoglycoside, vancomycin, carbapenem, pip-tazo, ceftazidime, cefazolin, co-trimoxazole

### Aminoglycoside — ทำไมวันละครั้ง
ฆ่าเชื้อตามความเข้มข้น + **post-antibiotic effect** · พิษต่อไตและหู สัมพันธ์กับ **ระดับต่ำสุด (trough) ที่ค้างนาน** → ขนาดสูงวันละครั้งได้ผลดีขึ้นและพิษน้อยลง · **ไม่ทำงานในหนองและสภาพกรด** · ไม่ครอบคลุม anaerobe""",
    ["Beta-lactam = time-dependent → loading + prolonged infusion",
     "Aminoglycoside = concentration-dependent → ขนาดสูงวันละครั้ง",
     "Dose แรกต้องเต็มเสมอแม้ไตวาย · ปรับ maintenance ตามไตทีหลัง"],
    [mcq(N(14), "Why does SSC 2026 recommend administering beta-lactam antibiotics as a prolonged infusion (after a loading dose) rather than as intermittent boluses?",
         ["Beta-lactams kill bacteria in proportion to peak concentration", "Beta-lactam killing depends on the time that free drug concentration remains above the MIC",
          "Prolonged infusion reduces the total daily dose needed by half", "Bolus dosing causes nephrotoxicity", "Prolonged infusion prevents allergic reactions"], 1,
         "Beta-lactam เป็นยา **time-dependent** — ประสิทธิภาพขึ้นกับ **%fT > MIC** (สัดส่วนเวลาที่ระดับยาอิสระอยู่เหนือ MIC) ไม่ใช่ระดับสูงสุด\n\nการให้แบบ **หยดนาน** ทำให้ระดับยาเหนือ MIC นานกว่า bolus ที่ขนาดรวมเท่ากัน · **loading dose** ก่อนเพื่อให้ถึงระดับเร็ว · ตรงข้ามกับ **aminoglycoside** ที่เป็น concentration-dependent จึงให้ขนาดสูงวันละครั้ง",
         "Beta-lactam: %T > MIC → หยดนาน", "PK/PD of beta-lactams",
         [SSC + " – prolonged infusion of beta-lactams"], ["B1.7.2"]),
     mcq(N(15), "A 68-year-old man with septic shock from pneumonia has creatinine 3.2 mg/dL (baseline 1.0). Meropenem is to be started. How should the first dose be chosen?",
         ["Give a reduced first dose adjusted to his current creatinine clearance", "Give a full (loading) first dose, then adjust subsequent doses to renal function",
          "Withhold meropenem until creatinine improves", "Use oral amoxicillin instead", "Give half the dose by bolus only"], 1,
         "ใน sepsis **volume of distribution เพิ่ม** (capillary leak + สารน้ำปริมาณมาก) ระดับยาจึงมักต่ำเกินในวันแรก → **dose แรกต้องเต็ม/loading เสมอ แม้ไตวาย**\n\nค่อย **ปรับ maintenance dose** ตาม CrCl หลัง 24–48 ชั่วโมง (AKI จาก sepsis มักฟื้นเร็ว การลดยาเร็วเกินเสี่ยงรักษาไม่หาย) · การลดขนาดตั้งแต่ dose แรกเป็นความผิดพลาดที่พบบ่อย",
         "ไตวายใน sepsis: dose แรกเต็ม ปรับทีหลัง", "Antibiotic dosing in AKI",
         ["Sanford Guide – renal dose adjustment", SSC], ["B1.7.2", "2.2.48"])],
    ["B1.7.2"])

# ───────────────────────────── 9
sec("id-sep-09", "Stewardship — คลุมเท่าที่จำเป็น และหยุดให้เป็น",
    "MDR เฉพาะเสี่ยงสูง · anaerobe เฉพาะห้าแหล่ง · ไม่ให้ antifungal เป็นกิจวัตร · ระยะสั้นเมื่อคุมแหล่งได้ · C. difficile", 7,
"""### ครอบคลุมเชื้อดื้อยา (MDR) เมื่อไร
เฉพาะ **ความเสี่ยงสูง** — เคยติด/มีเชื้อนั้นมาก่อน · นอนโรงพยาบาลนาน · ได้ยากว้างใน 90 วัน · อยู่ ICU · ฟอกไต · มาจากสถานดูแลระยะยาว
- **MRSA** → vancomycin
- **ESBL** → carbapenem
- **Pseudomonas** → pip-tazo, ceftazidime, cefepime, meropenem

### Anaerobe — SSC 2026 ระบุชัด (ใหม่)
**คลุม anaerobe เฉพาะ** แหล่ง **ในช่องท้อง · อุ้งเชิงกราน/สูติกรรมลึก · necrotizing soft-tissue · หัวและคอ · CNS (ฝีในสมอง)** · **ไม่ต้องคลุม** ใน pneumonia ทั่วไปและทางเดินปัสสาวะ

### Antifungal
**ไม่ให้แบบคาดการณ์เป็นกิจวัตร** — พิจารณารายบุคคลในผู้ภูมิคุ้มกันต่ำมาก (neutropenia นาน, TPN, ผ่าตัดช่องท้องซ้ำ, Candida หลายตำแหน่ง)

### ระยะเวลาและการหยุด
- **ประเมินทุกวัน** ว่ายังต้องใช้ แคบลงได้ หรือหยุดได้
- คุมแหล่งได้ดี → **ระยะสั้น** (เช่น intra-abdominal 4 วันหลัง source control · pyelonephritis 7 วัน · CAP 5 วันถ้าดีขึ้น)
- **PCT ช่วยตัดสินใจหยุด** เมื่อระยะเวลาไม่ชัด
- **พบสาเหตุอื่นที่ไม่ใช่ติดเชื้อ → หยุดยา**
- เปลี่ยนเป็น **ยากิน** เมื่ออาการคงที่ กินได้ และมียากินที่เหมาะ

### ผลเสียของยาเกินจำเป็น
***C. difficile* colitis** (ท้องเสียหลังยาปฏิชีวนะ → **vancomycin กิน** หรือ fidaxomicin) · เชื้อดื้อยา · พิษไต (vancomycin + pip-tazo) · แพ้ยา""",
    ["Anaerobe เฉพาะ: ช่องท้อง · อุ้งเชิงกรานลึก · necrotizing soft tissue · หัว-คอ · CNS",
     "MDR และ antifungal เฉพาะความเสี่ยงสูง",
     "ประเมินทุกวัน · ระยะสั้นเมื่อคุมแหล่งได้ · เจอเหตุอื่นให้หยุด"],
    [mcq(N(16), "A 55-year-old man with septic shock from community-acquired pneumonia has no recent hospitalisation or antibiotic exposure. Which addition to ceftriaxone plus azithromycin is NOT recommended by SSC 2026?",
         ["Blood cultures before antibiotics", "Routine metronidazole for anaerobic coverage", "Norepinephrine for persistent hypotension", "Serial lactate measurement", "Hydrocortisone for septic shock"], 1,
         "SSC 2026 **แนะนำไม่ให้คลุม anaerobe** เมื่อไม่มีข้อบ่งชี้ — คลุมเฉพาะแหล่ง **ช่องท้อง อุ้งเชิงกราน/สูติกรรมลึก necrotizing soft-tissue หัวและคอ และ CNS** · pneumonia ชุมชนทั่วไป (ไม่ใช่ปอดเป็นฝีหรือ empyema จากการสำลัก) ไม่ต้องเติม metronidazole\n\nตัวเลือกอื่นเป็นสิ่งที่แนะนำให้ทำทั้งหมด",
         "Pneumonia/UTI ไม่ต้องคลุม anaerobe", "Anaerobic coverage in sepsis",
         [SSC + " – anaerobic coverage"], ["B1.7.2", "2.3.10(5)"]),
     mcq(N(17), "A woman with pyelonephritis-related sepsis improves on ceftriaxone. On day 3, blood and urine cultures grow E. coli susceptible to ceftriaxone, ciprofloxacin and co-trimoxazole. She is afebrile, eating, and haemodynamically stable. What is the best plan?",
         ["Escalate to meropenem for 14 days", "Add vancomycin", "Switch to an appropriate oral agent (e.g. ciprofloxacin or co-trimoxazole) to complete about 7 days in total",
          "Continue IV ceftriaxone for 6 weeks", "Stop all antibiotics today"], 2,
         "อาการคงที่ ไม่มีไข้ กินได้ รู้เชื้อและความไวยาแล้ว → **de-escalate และเปลี่ยนเป็นยากิน** ที่เชื้อไวและเข้าเนื้อไตได้ดี (FQ หรือ co-trimoxazole) ให้ครบ **ราว 7 วัน** สำหรับ pyelonephritis\n\nการ escalate หรือให้ยานานเกินไม่มีประโยชน์ เพิ่ม *C. difficile* และเชื้อดื้อยา · หยุดยาวันที่ 3 สั้นเกินไป",
         "รู้เชื้อ + อาการคงที่ → แคบลง + ยากิน + ระยะสั้น", "De-escalation and IV-to-oral switch",
         [SSC + " – de-escalation, duration"], ["B1.7.2", "3.3.10", "B1.5.2(7)"])],
    ["B1.7.2", "B1.5.1(7)", "3.3.10"])

# ───────────────────────────── 10
sec("id-sep-10", "Source control และ sepsis เขตร้อนในประเทศไทย",
    "source control ≤ 6 ชม. · melioidosis · leptospirosis · scrub typhus · ไข้ช็อกในชาวนาเบาหวาน", 9,
"""### Source control
**ภายใน 6 ชม.** หลังวินิจฉัย เมื่อทำได้ — ระบายหนอง (ฝี empyema), **ระบายทางเดินปัสสาวะ/ท่อน้ำดีที่อุดตัน**, ตัดเนื้อตาย (necrotizing fasciitis), เอาสายสวนที่ติดเชื้อออก, ผ่าตัดลำไส้ทะลุ · ยาปฏิชีวนะอย่างเดียว **ไม่หาย** ถ้าแหล่งยังอยู่

### Sepsis เขตร้อนที่ต้องคิดในประเทศไทย
| โรค | ใครเสี่ยง | ลักษณะ | ยา |
|---|---|---|---|
| **Melioidosis** (*Burkholderia pseudomallei*) | **ชาวนาอีสาน เบาหวาน** ไตวายเรื้อรัง ดื่มสุรา สัมผัสดิน/น้ำ ฤดูฝน | pneumonia, **ฝีตับ/ม้าม**, ฝีหลายแห่ง, ต่อมลูกหมาก, bacteremia ช็อก · Gram-neg bacilli แบบ **safety pin** | **ceftazidime** หรือ **meropenem** (ช็อก/รุนแรง) ≥ 10–14 วัน → **co-trimoxazole 3–6 เดือน** (eradication) |
| **Leptospirosis** | ลุยน้ำ ท่วม ทำนา หนู | ไข้ **ปวดน่องมาก** ตาแดง (conjunctival suffusion) **ตัวเหลือง + ไตวาย** (Weil) **ปอดเลือดออก** | รุนแรง: **penicillin G** หรือ **ceftriaxone** · ไม่รุนแรง: **doxycycline** |
| **Scrub typhus** (*Orientia tsutsugamushi*) | เข้าป่า ไร่ ทุ่งหญ้า (ไรอ่อน) | ไข้ ปวดศีรษะ **eschar** (แผลไหม้บุหรี่) ต่อมน้ำเหลืองโต ปอดอักเสบ | **doxycycline** (ตั้งครรภ์/เด็ก: azithromycin) |
| ไข้เลือดออก (dengue) | ทุกคน | ช็อกระยะไข้ลง เกล็ดเลือดต่ำ Hct สูง | ประคับประคอง — **ไม่ใช่ sepsis จากแบคทีเรีย** ระวังให้น้ำเกิน |

> ไข้ช็อกในชาวนาเบาหวานจากอีสาน → **ceftazidime/meropenem ตั้งแต่แรก** เพราะ ceftriaxone และ aminoglycoside **ไม่ครอบคลุม** *B. pseudomallei* · ไม่รู้ว่า lepto หรือ scrub → ceftriaxone + doxycycline คลุมทั้งคู่""",
    ["Source control ≤ 6 ชม. — ยาอย่างเดียวไม่หายถ้าแหล่งยังอยู่",
     "ชาวนาเบาหวาน + ไข้ช็อก/ฝีหลายแห่ง → melioidosis → ceftazidime/meropenem",
     "Lepto: ปวดน่อง ตาแดง เหลือง ไตวาย → PGS/ceftriaxone · scrub typhus: eschar → doxycycline"],
    [mcq(N(18), "A 52-year-old rice farmer from north-eastern Thailand with poorly controlled diabetes presents in the rainy season with fever, cough and hypotension. CT shows multiple small hypodense lesions in the liver and spleen. Gram stain of blood culture shows Gram-negative bacilli with bipolar ('safety-pin') staining. Which empirical regimen is most appropriate?",
         ["Ceftriaxone plus gentamicin", "Meropenem (or ceftazidime), followed later by oral co-trimoxazole eradication therapy", "Doxycycline alone", "Amoxicillin-clavulanate", "Vancomycin plus metronidazole"], 1,
         "ชาวนาอีสาน + **เบาหวาน** + ฤดูฝน + ปอดอักเสบ + **ฝีเล็กหลายแห่งในตับและม้าม** + Gram-negative bacilli แบบ **safety pin** = **melioidosis** (*Burkholderia pseudomallei*)\n\nIntensive phase: **ceftazidime** หรือ **meropenem** (เลือก meropenem ในช็อก/รุนแรง) อย่างน้อย 10–14 วัน → **eradication: co-trimoxazole 3–6 เดือน** ป้องกันการกลับเป็นซ้ำ\n\n**Ceftriaxone และ aminoglycoside ไม่ครอบคลุม** *B. pseudomallei* (ดื้อโดยธรรมชาติ)",
         "ชาวนาเบาหวาน + ฝีตับม้าม → melioidosis → ceftazidime/meropenem → co-trimoxazole", "Melioidosis",
         ["แนวทางการวินิจฉัยและรักษาโรคเมลิออยโดสิส (กรมควบคุมโรค)", "Wiersinga WJ et al. Melioidosis. Nat Rev Dis Primers 2018"], ["2.3.1(16)", "2.2.48", "B1.7.2"]),
     mcq(N(19), "A 35-year-old man cleaned his flooded house 10 days ago. He now has high fever, severe calf pain, conjunctival suffusion, jaundice, oliguria and haemoptysis. BP 88/50 mmHg. Which antimicrobial is most appropriate for this severe illness?",
         ["Oral doxycycline only", "Intravenous penicillin G or ceftriaxone", "Oral amoxicillin", "Metronidazole", "Fluconazole"], 1,
         "ลุยน้ำท่วม + ไข้สูง **ปวดน่องมาก ตาแดง (conjunctival suffusion)** + **ตัวเหลือง ไตวาย (Weil's disease)** + **ไอเป็นเลือด (pulmonary hemorrhage)** = **severe leptospirosis**\n\nรุนแรง → **IV penicillin G หรือ ceftriaxone** · ไม่รุนแรง → doxycycline กิน · ร่วมกับประคับประคองไต (มักต้องฟอกไต) และการหายใจ\n\nถ้ายังแยกจาก scrub typhus ไม่ได้ → เติม doxycycline คลุมทั้งคู่",
         "Lepto รุนแรง (เหลือง ไตวาย ปอดเลือดออก) → PGS/ceftriaxone IV", "Severe leptospirosis",
         ["แนวทางเวชปฏิบัติโรคเลปโตสไปโรสิส (กรมควบคุมโรค)", "Harrison's 21e – Leptospirosis"], ["2.3.1(13)", "2.2.48", "B1.7.2"])],
    ["2.2.48", "2.3.1(16)", "2.3.1(13)"])

# ───────────────────────────── 11
sec("id-sep-11", "ดูแลต่อใน ICU และการสื่อสาร",
    "glucose ≥ 180 → insulin · LMWH · restrictive transfusion · ARDS Vt 6 · NaHCO₃ เฉพาะบางราย · goals of care ใน 72 ชม.", 6,
"""### มาตรการต่อเนื่อง (SSC 2026)
| เรื่อง | คำแนะนำ |
|---|---|
| น้ำตาล | **เริ่ม insulin เมื่อ glucose ≥ 180 mg/dL** (เป้า 144–180) |
| ป้องกัน VTE | **LMWH มากกว่า UFH** |
| ให้เลือด | **restrictive** (Hb < 7 g/dL ในส่วนใหญ่) |
| ARDS | **Vt 6 mL/kg PBW, Pplat ≤ 30** · prone ใน ARDS รุนแรง |
| หายใจล้มเหลวที่ยังไม่ใส่ท่อ | **HFNC ก่อน NIV** |
| NaHCO₃ | เฉพาะ **pH ≤ 7.2 ร่วมกับ AKI ระยะ 2–3** |
| RRT | ไม่ทำเมื่อยังไม่มีข้อบ่งชี้ชัด |
| สารน้ำหลังพ้นช่วงกู้ชีพ | ดึงน้ำออก |
| โภชนาการ | เริ่มให้อาหารทางลำไส้เร็ว |
| **Goals of care** | **คุยกับผู้ป่วย/ญาติภายใน 72 ชม.** · ประสานการดูแลประคับประคอง |
| หลังจำหน่าย | ติดตามผลระยะยาว (post-sepsis syndrome — อ่อนแรง ความจำ อารมณ์) |

### คุยกับญาติ (NL3)
1. บอกสิ่งที่สงสัยเป็นภาษาง่าย — *"หมอสงสัยว่าคุณแม่ติดเชื้อที่ทางเดินปัสสาวะ และเชื้อเริ่มกระทบความดันกับไต ซึ่งเป็นภาวะรุนแรง"*
2. บอกสิ่งที่กำลังทำ — เพาะเชื้อแล้ว ให้ยาฆ่าเชื้อในชั่วโมงนี้ น้ำเกลือ และยาพยุงความดัน
3. บอกช่วงที่อาการเปลี่ยนเร็ว (6–24 ชม. แรก) และถามความต้องการ/สิ่งที่ผู้ป่วยเคยบอกไว้""",
    ["Insulin เมื่อ glucose ≥ 180 · LMWH · ให้เลือดแบบ restrictive",
     "ARDS: Vt 6 mL/kg Pplat ≤ 30 · HFNC ก่อน NIV",
     "คุย goals of care ภายใน 72 ชม."],
    [mcq(N(20), "On day 2 of septic shock, a patient's blood glucose readings are 190–230 mg/dL. Haemoglobin is 8.2 g/dL without bleeding or ischaemia. Which combination of management follows SSC 2026?",
         ["Start insulin infusion targeting 80–110 mg/dL and transfuse to Hb 10", "Start insulin when glucose is ≥ 180 mg/dL (target about 144–180) and avoid transfusion at this haemoglobin",
          "No insulin until glucose exceeds 300 mg/dL; transfuse 2 units", "Give oral hypoglycaemics and erythropoietin", "Give dextrose-free fluids only and transfuse to Hb 9"], 1,
         "SSC — **เริ่ม insulin เมื่อ glucose ≥ 180 mg/dL** เป้าราว **144–180** (การคุมเข้ม 80–110 เพิ่ม hypoglycemia และการตาย) · ให้เลือดแบบ **restrictive** — Hb 8.2 ไม่มีเลือดออกหรือหัวใจขาดเลือด **ไม่ต้องให้เลือด** (เกณฑ์ทั่วไป Hb < 7)",
         "Sepsis: insulin เมื่อ ≥ 180 · ให้เลือดเมื่อ Hb < 7", "Supportive care in sepsis",
         [SSC + " – glucose, transfusion"], ["2.2.48", "2.2.7"])],
    ["2.2.48", "2.2.7"])


LECNAME = "Septicemia and antibiotic usage (อ.พจน์)"
MEQ = [{"id": "ID-MEQ-01", "part": "MEQ", "lec": "25/9", "lecture": LECNAME,
 "topic": "Septic shock from obstructive pyelonephritis — first hour, resuscitation, source control and de-escalation",
 "vignette": """ผู้ป่วยหญิงไทยอายุ 58 ปี น้ำหนัก 60 kg มาห้องฉุกเฉินด้วยไข้สูงหนาวสั่น 2 วัน
PI: 3 วันก่อน ปัสสาวะแสบขัด ปวดเอวซ้าย 2 วันก่อน ไข้สูงหนาวสั่น วันนี้ซึมลง ปัสสาวะออกน้อย
PH: เบาหวาน 10 ปี ใช้ metformin · เคยเป็นนิ่วไตซ้าย
PE: BT 39.4 C, PR 124/min, BP 82/48 mmHg (MAP 59), RR 26/min, SpO2 96% RA
GA: drowsy but arousable, GCS E3V4M6 · mottled knees, capillary refill 4 sec
Abdomen: left CVA tenderness
Lab: WBC 22,000 (N 90%), Plt 92,000, Cr 2.4 mg/dL (baseline 0.8), lactate 4.6 mmol/L, glucose 286 mg/dL
UA: WBC numerous, nitrite positive""",
 "questions": [
  {"q": "1. จงบอกการวินิจฉัย ระดับความมั่นใจตาม SSC 2026 และเหตุผล (3 คะแนน)",
   "a": """**การวินิจฉัย: Septic shock จาก acute pyelonephritis ซ้าย (สงสัย obstructive จากนิ่ว)**
- แหล่งติดเชื้อชัด: ปัสสาวะแสบขัด ปวดเอว CVA tenderness UA เม็ดเลือดขาวเต็ม nitrite บวก
- อวัยวะล้มเหลว (SOFA ↑ ≥ 2): **สับสน (GCS 13) · ไต (Cr 2.4) · เกล็ดเลือดต่ำ (92,000) · ความดันต่ำ**
- **Hypoperfusion**: MAP 59, mottling, CRT 4 วินาที, **lactate 4.6**
- **ระดับ: Probable sepsis → ถ้าเพาะเชื้อขึ้นตรงแหล่ง = definite** · **มีช็อก** → นาฬิกา **≤ 1 ชม.**
(จะเรียกว่า septic shock เต็มนิยามเมื่อยังต้องใช้ vasopressor ให้ MAP ≥ 65 หลังให้น้ำพอและ lactate > 2)"""},
  {"q": "2. จงเขียนการดูแลในชั่วโมงแรก พร้อมปริมาณสารน้ำและชนิดยาปฏิชีวนะ (5 คะแนน)",
   "a": """1. **ABCDE** · O₂ ตามเป้า · IV ขนาดใหญ่ 2 เส้น
2. **Hemoculture 2 ชุด + urine culture ก่อนยา** (ไม่ให้ยาช้า)
3. **ยาปฏิชีวนะภายใน 1 ชม.** — **ceftriaxone 2 g IV** (UTI ชุมชน ไม่มีปัจจัยเสี่ยงเชื้อดื้อยา) · ถ้าเคยได้ยากว้าง/นอนโรงพยาบาลบ่อย/เคยมี ESBL → **meropenem** · ให้ **dose เต็ม** แม้ Cr สูง · ไม่ต้องคลุม anaerobe
4. **Balanced crystalloid ≥ 30 mL/kg = 1,800 mL ใน 3 ชม.** ประเมินซ้ำทุก 15–30 นาที (BP, CRT, ปอด, ปัสสาวะ)
5. **MAP ยัง < 65 → norepinephrine** ทางหลอดเลือดส่วนปลายได้เลย ไม่ต้องรอ central line
6. **Lactate ซ้ำ** ใน 2–4 ชม. · ใส่สายสวนปัสสาวะวัด urine output
7. **หยุด metformin** · insulin เมื่อ glucose ≥ 180
8. **ส่ง US ไต (bedside) หาภาวะอุดตัน** — เพื่อวางแผน source control"""},
  {"q": "3. US พบ hydronephrosis ซ้ายจากนิ่วที่ท่อไตส่วนบน จะทำอะไรต่อและภายในเมื่อไร (2 คะแนน)",
   "a": """**Source control ภายใน 6 ชั่วโมง** — **ระบายไตที่อุดตัน** ด้วย **percutaneous nephrostomy (PCN)** หรือ **ใส่ ureteric (DJ) stent**
- **ไม่ผ่าตัดเอานิ่วออกตอนนี้** (ทำทีหลังเมื่อหายติดเชื้อ)
- ยาปฏิชีวนะอย่างเดียวไม่หายเพราะหนองค้างในไตที่อุดตัน (obstructive pyelonephritis/pyonephrosis)"""},
  {"q": "4. หลังให้น้ำ 1,800 mL และ NE 0.25 µg/kg/min ยัง MAP 62 จะปรับการรักษาอย่างไร (2 คะแนน)",
   "a": """- **เติม vasopressin** (NE ขนาดสูงขึ้นเรื่อย ๆ) · ถ้ายังไม่ถึงเป้า → **เติม epinephrine**
- **ให้ hydrocortisone** (เช่น 200 mg/วัน) เพราะยังต้องใช้ vasopressor
- ประเมิน fluid responsiveness ด้วย **passive leg raise** ก่อนให้น้ำเพิ่ม · echo ดูการบีบตัว (ถ้าบีบอ่อน → dobutamine)
- เป้า MAP 65 (อายุ 58 ปี)"""},
  {"q": "5. วันที่ 3 hemoculture ขึ้น E. coli ไวต่อ ceftriaxone, ciprofloxacin ผู้ป่วยไม่มีไข้ หยุด vasopressor แล้ว กินได้ จงวางแผนยาปฏิชีวนะ (2 คะแนน)",
   "a": """- **De-escalate**: คง ceftriaxone หรือ **เปลี่ยนเป็นยากิน** (ciprofloxacin) เมื่ออาการคงที่และกินได้
- **ระยะเวลา ~7 วัน** (bacteremic pyelonephritis ที่ระบายแล้วและตอบสนองดี — บางแนวทาง 7–14 วัน)
- ไม่ต้อง escalate เป็น carbapenem · ไม่ต้อง repeat hemoculture เป็นกิจวัตรสำหรับ gram-negative ที่ดีขึ้นชัด
- นัดผ่าตัดนิ่วเมื่อหายติดเชื้อ · คุมเบาหวาน"""}],
 "ref": [SSC, "บทเรียน Sepsis SSC 2026 (คู่ lecture อ.พจน์) – เคส 1"],
 "nl": ["2.2.48", "2.2.7", "B7.2.5(4)", "B1.7.2", "3.3.9", "2.1.1"], "years": [], "_kind": "meq", "_set": "id"}]

OSCE = [{"id": "ID-OSCE-01", "part": "OSCE/SAQ", "lec": "25/9", "lecture": LECNAME,
 "topic": "OSCE – First-hour management of sepsis: present the case, order, and talk to the family",
 "station": "สถานีสถานการณ์จำลอง 8 นาที (ใช้ผู้ป่วยจำลอง + ญาติจำลอง)",
 "instruction": """ชายอายุ 70 ปี น้ำหนัก 50 kg ไข้ ไอเสมหะเขียว 2 วัน ซึมลงวันนี้
V/S: BT 39 C, PR 118, BP 84/50 (MAP 61), RR 30, SpO₂ 89% RA · ฟังปอดได้ crackles ปอดขวาล่าง
CXR: consolidation RLL · lab ยังไม่ออก

คำสั่ง
1. นำเสนอเคสต่ออาจารย์ใน 60 วินาที โดยระบุระดับความมั่นใจของ sepsis และการมีช็อก (2 คะแนน)
2. สั่งการรักษาในชั่วโมงแรกให้ครบ (ระบุปริมาณสารน้ำและยา) (4 คะแนน)
3. อธิบายอาการและแผนการรักษาให้ลูกสาวของผู้ป่วยฟัง (2 คะแนน)""",
 "answer": """**1. นำเสนอ** — *\"ชาย 70 ปี ไข้ ไอเสมหะ 2 วัน ซึมลง ตรวจพบ RLL pneumonia ร่วมกับ hypoxemia, ความดันต่ำ MAP 61 และสับสน — **probable sepsis from community-acquired pneumonia with shock** · แผนคือเพาะเชื้อ ให้ยาภายใน 1 ชั่วโมง ให้ balanced crystalloid 30 mL/kg และ norepinephrine ถ้า MAP ยังต่ำ\"*

**2. ชั่วโมงแรก**
| สั่ง | รายละเอียด |
|---|---|
| O₂ | nasal cannula/HFNC เป้า SpO₂ 92–96% |
| IV 2 เส้น | + blood culture 2 ชุด, sputum Gram stain/culture, CBC, BUN/Cr, LFT, **lactate**, glucose, ABG |
| **ยาปฏิชีวนะ ≤ 1 ชม.** | **ceftriaxone 2 g IV + azithromycin 500 mg** (CAP รุนแรง) · เสี่ยง Pseudomonas/MRSA จึงขยาย · ชาวนาเบาหวาน → ceftazidime/meropenem (melioidosis) |
| **สารน้ำ** | **balanced crystalloid 30 mL/kg = 1,500 mL ใน 3 ชม.** ประเมินซ้ำ (ระวังปอด) |
| **Vasopressor** | MAP < 65 หลังให้น้ำ → **norepinephrine** ทางส่วนปลายได้ เป้า MAP 60–65 (อายุ ≥ 65) |
| ติดตาม | สายสวนปัสสาวะ · ปัสสาวะ ≥ 0.5 mL/kg/h · CRT · lactate ซ้ำ · ประเมิน ICU |

**3. คุยกับญาติ**
- แนะนำตัว ถามว่าญาติรู้อะไรแล้ว
- *\"คุณพ่อมีปอดอักเสบที่เชื้อเริ่มกระทบความดันและการรู้สึกตัว เป็นภาวะติดเชื้อในกระแสเลือดที่รุนแรง\"*
- บอกสิ่งที่ทำ: เพาะเชื้อ ยาฆ่าเชื้อทางหลอดเลือดในชั่วโมงนี้ น้ำเกลือ ยาพยุงความดัน ออกซิเจน อาจต้องย้าย ICU/ใส่ท่อช่วยหายใจ
- ช่วง 24–72 ชม.แรกอาการเปลี่ยนได้เร็ว · ถามความต้องการของผู้ป่วยที่เคยพูดไว้ (goals of care) · เปิดให้ถาม แสดงความเห็นใจ

**ข้อที่ทำให้เสียคะแนน**: รอผล lab ก่อนให้ยา · ลืมเพาะเชื้อ · ให้น้ำไม่ระบุปริมาณ · เลือก dopamine · ใช้ศัพท์แพทย์กับญาติ""",
 "ref": [SSC, "บทเรียน Sepsis SSC 2026 – NL3"],
 "nl": ["2.2.48", "2.2.7", "2.3.10(5)", "B1.7.2"], "years": [], "_kind": "meq", "_set": "id"}]

LECTURE = {
 "lec": "25/9",
 "date": "ศ. 25 ก.ย.",
 "title": "Septicemia and antibiotic usage",
 "subtitle": "นิยาม Sepsis-3 และการคัดกรอง · กลไก · สี่ระดับความมั่นใจและนาฬิกายาปฏิชีวนะ · ชั่วโมงแรก · สารน้ำ · vasopressor และ steroid · หลักการเลือกยาปฏิชีวนะ PK/PD และ stewardship · source control และ sepsis เขตร้อน · ดูแลต่อใน ICU",
 "objectives": [
   "ให้นิยาม sepsis และ septic shock ตาม Sepsis-3 และเลือกเครื่องมือคัดกรองตาม SSC 2026",
   "อธิบายกลไกของ sepsis ตั้งแต่ PAMPs/DAMPs จนถึงอวัยวะล้มเหลว และความหมายของ lactate",
   "จัดระดับความมั่นใจ (definite/probable/possible/unlikely) และกำหนดเวลาเริ่มยาปฏิชีวนะตามระดับและการมีช็อก",
   "ทำการดูแลชั่วโมงแรกได้ครบ: เพาะเชื้อ ยาปฏิชีวนะ สารน้ำ 30 mL/kg และ norepinephrine ตามเป้า MAP",
   "เลือกยาปฏิชีวนะ empirical ตามแหล่งติดเชื้อและความเสี่ยงเชื้อดื้อยา และ de-escalate เมื่อรู้เชื้อ",
   "ประยุกต์หลัก PK/PD กับการให้ยา (prolonged infusion, loading dose, aminoglycoside วันละครั้ง, ปรับตามไต)",
   "วินิจฉัยและรักษา sepsis เขตร้อนที่พบในประเทศไทย (melioidosis, leptospirosis, scrub typhus) และวาง source control ภายใน 6 ชม."],
 "nlGap": "**สไลด์ของ อ.พจน์ (\"Sepsis / Principle ATB\") เป็นภาพล้วน 175 MB ดึงข้อความไม่ได้เลย** — คาบนี้จึงไม่ได้สรุปจากสไลด์โดยตรง แต่เรียบเรียงจาก **Surviving Sepsis Campaign 2026** (ตรวจกับหน้า SCCM) ร่วมกับ **บทเรียน Sepsis ที่ผู้ใช้ทำไว้คู่ lecture นี้** และหลักการใช้ยาปฏิชีวนะมาตรฐาน ถ้าได้ภาพสไลด์มา ให้เทียบแล้วแก้ `build_sepsis.py` · เกณฑ์ฯ มีรหัส `นล. 2.2.48 Sepsis` และ `2.2.7 Shock` แต่ **ไม่มีรหัสของหลัก PK/PD, stewardship หรือ source control** โดยตรง (ใกล้ที่สุดคือ `B1.7.2` ยาต้านจุลชีพ และ `B1.5.1(7)` เชื้อดื้อยา) และ **scrub typhus ไม่มีรหัสแยก** จึงอิงแนวทางด้านล่าง",
 "guidelines": [
   "**Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2026** (Prescott HC, Antonelli M et al. Crit Care Med / Intensive Care Med, มี.ค. 2026) — สี่ระดับความมั่นใจ เวลาเริ่มยา สารน้ำ vasopressor stewardship",
   "**Singer M et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA 2016;315:801**",
   "**แนวทางการวินิจฉัยและรักษาโรคเมลิออยโดสิส** และ **แนวทางเวชปฏิบัติโรคเลปโตสไปโรสิส** (กรมควบคุมโรค)",
   "**Sanford Guide to Antimicrobial Therapy** — ขนาดยาและการปรับตามไต",
   "**Harrison's Principles of Internal Medicine 21e** — Sepsis and septic shock · Principles of antimicrobial therapy"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

ID_SET = {
 "set": "id",
 "title": "ID · โรคติดเชื้อ",
 "intro": "เริ่มจากคาบ **Septicemia and antibiotic usage ของ อ.พจน์ (25 ก.ย.)** — ภาวะติดเชื้อในกระแสเลือดตาม Surviving Sepsis Campaign 2026 ตั้งแต่นิยาม การคัดกรอง สี่ระดับความมั่นใจที่กำหนดเวลาเริ่มยาปฏิชีวนะ การกู้ชีพด้วยสารน้ำและยากระตุ้นความดัน ไปจนถึงหลักการเลือกยาปฏิชีวนะ PK/PD และ sepsis เขตร้อนที่พบบ่อยในประเทศไทย จบแต่ละหัวข้อมีข้อสอบเช็คความเข้าใจทันที",
 "howto": "**วิธีใช้** — อ่านเนื้อหาให้จบแล้วตอบข้อสอบท้ายหัวข้อ ระบบเฉลยพร้อมคำอธิบายกลไกทันทีที่ตอบ · ตอบครบทุกข้อแล้วหัวข้อจะถูกทำเครื่องหมายว่าเรียนจบ · ข้อที่ตอบผิดรวมอยู่ในแท็บ **ทบทวนข้อที่ผิด** · จบคาบแล้วไปฝึก **MEQ** และ **OSCE/SAQ** ต่อได้เลย\n\n**ลำดับที่แนะนำ** — หัวข้อ 3 (นาฬิกา **1 · 1 · 3 · รอ**) คือแกนของทั้งคาบ · ตัวเลขที่ต้องจำ **30 mL/kg ใน 3 ชม.** · **MAP 65 (≥ 65 ปี 60–65)** · **source control ≤ 6 ชม.** · เรียนต่อจากคาบ Circulatory shock ของชุด Cardio ได้ดี\n\n**หมายเหตุ** — สไลด์ของคาบนี้เป็นภาพล้วนที่ดึงข้อความไม่ได้ เนื้อหาจึงอิง SSC 2026 เป็นหลัก (รายละเอียดในกล่อง *ครอบคลุมจุดประสงค์ นล.*) · ชุด ID เพิ่งเริ่ม ยังไม่มีคลังข้อสอบเก่า MED28–MED35 ของระบบนี้ และคาบอื่น (malaria · leptospirosis/melioidosis · typhoid · typhus · HIV) ยังไม่ได้ทำ",
 "label": "ID",
 "thai": "โรคติดเชื้อ",
 "accent": {"light": "#a3402a", "soft": "#f6e6e1", "ink": "#7f2f1e",
            "dark": "#ff9b7a", "darkSoft": "#2a1712", "darkInk": "#ffbfa8"},
 "file": "data/id.json",
 "lectureCount": 0,
}

# ── ตรวจก่อนเขียน
path = os.path.join(BUILD, "data", "id.json")
data = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
data = [l for l in data if l.get("lec") != LECTURE["lec"]]
seen = set()
for l in data + [LECTURE]:
    for x in [i for s in l["sections"] for i in s["items"]] + l.get("meq", []) + l.get("osce", []) + [{"id": s["id"]} for s in l["sections"]]:
        assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
        seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = {c for s in S for c in s["nl"]} | {c for s in S for i in s["items"] for c in i["nl"]} | {c for m in MEQ + OSCE for c in m["nl"]}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบในพจนานุกรม: %s" % missing
for s in S:
    assert "```" not in s["md"], s["id"]

data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
if not any(m["set"] == "id" for m in idx):
    idx.append(ID_SET)
for m in idx:
    if m["set"] == "id": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | items %d | meq %d | osce %d | nl codes %d" % (len(S), sum(len(s["items"]) for s in S), len(MEQ), len(OSCE), len(codes)))
print("id.json มี %d คาบ · %d bytes" % (len(data), os.path.getsize(path)))
