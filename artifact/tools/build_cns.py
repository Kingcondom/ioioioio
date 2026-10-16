#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""สร้างคาบ CNS infection and CSF interpretation (อ.พิมลพรรณ เลี่ยนเครือ) → data/neuro.json"""
import json, os

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
NLN = ["2.3.6"]
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}

sec("neuro-cns-01", "CNS infection — เชื้อเข้าสมองได้อย่างไร",
    "สี่ขั้นของพยาธิกำเนิด และสามเส้นทางเข้าสู่ระบบประสาทกลาง", 6,
"""สไลด์วางกรอบพยาธิกำเนิดไว้ **สี่ขั้น** ซึ่งใช้เป็นโครงคิดได้ทั้งคาบ

1. **Colonize or enter the body** — เชื้อเข้าสู่ร่างกายและตั้งรกราก
2. **Travel to and gain access to the CNS** — เดินทางเข้าสู่ระบบประสาทกลาง
3. **Multiply or replicate** ภายใน CNS
4. **Incite an inflammatory response** — กระตุ้นการอักเสบ ซึ่งเป็นตัวก่ออาการส่วนใหญ่

### สามเส้นทางเข้าสู่ CNS

| เส้นทาง | กลไก | ตัวอย่าง |
|---|---|---|
| **Hematogenous** | ผ่านกระแสเลือด | bacterial meningitis จาก bacteremia, brain abscess จาก endocarditis หรือ ฝีในปอด |
| **Direct extension** | ลามจากอวัยวะข้างเคียง | ไซนัสอักเสบ หูชั้นกลางอักเสบ → **brain abscess** · กระดูกสันหลังติดเชื้อ → **epidural abscess** |
| **Neuronal spreading** | ไต่ไปตามเส้นประสาท | **HSV, rabies** |

### ทำไมต้องรู้เส้นทาง
เพราะมันบอก **ว่าต้องไปหาแหล่งต้นตอที่ไหน** — ผู้ป่วย brain abscess ที่เชื้อเป็น streptococcus ให้ไปหา **ไซนัสหรือฟัน**, ผู้ป่วยที่มี **โรคหัวใจพิการแต่กำเนิดแบบมี right-to-left shunt** เลือดดำข้ามปอดไปสมองโดยตรงจึงเสี่ยงสูง

### ตำแหน่งทางกายวิภาคที่ต้องแยกให้ออกก่อนเสมอ
- **Central nervous system** — สมอง และไขสันหลัง
- **Peripheral nervous system** — เส้นประสาทสมองและปมประสาท, รากประสาทไขสันหลัง, ระบบประสาทอัตโนมัติ, เส้นประสาทส่วนปลาย, **neuromuscular junction** และกล้ามเนื้อ

การระบุตำแหน่งก่อนเป็นนิสัยจะช่วยไม่ให้เผลอวินิจฉัย "ติดเชื้อในสมอง" ในผู้ป่วยที่จริง ๆ แล้วเป็นโรคของ NMJ หรือเส้นประสาทส่วนปลาย
""",
    ["สี่ขั้น: เข้าร่างกาย → เดินทางเข้า CNS → เพิ่มจำนวน → ก่อการอักเสบ",
     "สามเส้นทาง: hematogenous · direct extension · neuronal spreading",
     "เจอ brain abscess ต้องตามหาแหล่งต้นตอเสมอ โดยเฉพาะไซนัส หู ฟัน และหัวใจ"],
    [
    mcq("NEU-CNS-MCQ-01",
        "A 45-year-old man develops a solitary frontal lobe abscess. He has had chronic purulent nasal discharge for 2 months. Which route of CNS invasion is most likely?",
        ["Hematogenous spread", "Direct extension from an adjacent focus", "Neuronal spreading along cranial nerves", "Iatrogenic inoculation", "Transplacental transmission"],
        1,
        """**ฝีในสมองกลีบหน้าร่วมกับไซนัสอักเสบเรื้อรัง = direct extension (contiguous spread)**

สไลด์ระบุสามเส้นทางเข้าสู่ CNS ไว้ชัด และเน้นว่าเชื้อที่พบบ่อยที่สุดใน brain abscess ของผู้ที่ภูมิคุ้มกันปกติคือ **streptococcal species ทั้งชนิดใช้และไม่ใช้ออกซิเจน พบมากกว่าครึ่งหนึ่งของผู้ป่วย และมักสัมพันธ์กับการติดเชื้อในไซนัส**

**ความสัมพันธ์ตำแหน่งฝีกับแหล่งต้นตอ**

| ตำแหน่งฝี | แหล่งที่ต้องมองหา |
|---|---|
| **Frontal lobe** | **ไซนัสหน้าผากและเอทมอยด์ · ฟัน** |
| **Temporal lobe / cerebellum** | **หูชั้นกลางและ mastoid** |
| **หลายตำแหน่ง กระจาย** | **Hematogenous** — endocarditis, ฝีในปอด, right-to-left shunt |

**ทำไมข้ออื่นผิด** — **hematogenous** มักให้ฝีหลายตำแหน่งและอยู่ที่รอยต่อ gray-white · **neuronal spreading** เป็นทางของ HSV และ rabies ไม่ใช่แบคทีเรียสร้างฝี · **iatrogenic** ต้องมีประวัติผ่าตัดหรือหัตถการ · **transplacental** เป็นการติดเชื้อในทารกแรกเกิด""",
        "ฝีสมองกลีบหน้า → หาไซนัสและฟัน · กลีบขมับหรือสมองน้อย → หาหูชั้นกลาง",
        "Routes of CNS infection",
        ["สไลด์ อ.พิมลพรรณ — Pathophysiology of CNS infection", "Emerg Med Clin N Am 2010;28:535-570"]),
    ])

sec("neuro-cns-02", "Meningitis — อาการและการสืบค้น",
    "ไข้ ปวดศีรษะ คอแข็ง · เมื่อไรต้อง CT ก่อนเจาะหลัง", 9,
"""### อาการและอาการแสดง
สไลด์เน้นสามอาการหลัก
- **ไข้ (fever)**
- **ปวดศีรษะ (headache)**
- **คอแข็ง (neck stiffness)**
- **ระดับการรู้ตัวเปลี่ยน พบราว 40%**

> **classic triad ครบทั้งสามอย่างพบเพียงส่วนน้อย** — การไม่มีคอแข็งไม่ตัด meningitis ออก โดยเฉพาะในผู้สูงอายุ ผู้ป่วยภูมิคุ้มกันบกพร่อง และผู้ที่ได้ยาปฏิชีวนะมาก่อน

### การสืบค้น

| การตรวจ | รายละเอียด |
|---|---|
| **Lumbar puncture for CSF analysis and microbiology** | การตรวจที่ให้คำตอบ |
| **CT brain with contrast** | **มักทำก่อนเจาะหลัง เพื่อตัด space-occupying lesion** |
| **Blood cultures** | **ขึ้นเชื้อได้ถึง 70%** ของผู้ป่วย — ต้องเจาะทุกราย |

### เมื่อไรต้องทำ CT ก่อนเจาะหลัง — กลุ่มที่ต้องระวัง
สไลด์ระบุไว้ห้าข้อ
1. **อายุมากกว่า 60 ปี**
2. **ภูมิคุ้มกันบกพร่อง (immunocompromise)**
3. **มีการชักใกล้กับเวลาที่มาพบแพทย์**
4. **ระดับการรู้ตัวเปลี่ยน**
5. **ตรวจพบ focal deficit**

### ลำดับที่ถูกต้องเมื่อต้องรอ CT
> **ห้ามให้การรอ CT มาหน่วงการให้ยาปฏิชีวนะ** ลำดับที่ถูกคือ
> **เจาะ hemoculture → ให้ dexamethasone พร้อมหรือก่อนยาปฏิชีวนะ → ให้ยาปฏิชีวนะ empiric → แล้วจึงทำ CT → แล้วจึงเจาะหลัง**
> CSF ที่เจาะหลังได้ยาไปแล้วไม่กี่ชั่วโมงยังแปลผล cell count, protein, glucose ได้ และยังส่ง PCR ได้

### CT brain with contrast บอกอะไร
**Leptomeningeal enhancement** เกิดจาก **การรั่วของ blood-brain barrier** ทำให้สารน้ำและสารทึบรังสีซึมออกสู่ช่องระหว่างเซลล์ — พบได้ใน **เนื้องอกสมอง การติดเชื้อ และการบาดเจ็บ**
""",
    ["คอแข็งไม่ครบไม่ตัด meningitis โดยเฉพาะผู้สูงอายุและผู้ป่วยภูมิคุ้มกันบกพร่อง",
     "ห้าข้อที่ต้อง CT ก่อนเจาะหลัง: อายุ > 60 · ภูมิคุ้มกันบกพร่อง · ชัก · รู้ตัวเปลี่ยน · focal deficit",
     "รอ CT ได้ แต่ห้ามรอยาปฏิชีวนะ — เจาะ hemoculture แล้วให้ยาก่อน",
     "Blood culture ขึ้นเชื้อได้ถึง 70% ต้องเจาะทุกราย"],
    [
    mcq("NEU-CNS-MCQ-02",
        "A 68-year-old man presents with fever, headache and confusion. Examination shows neck stiffness and a right hemiparesis. Which of the following is the most appropriate sequence of management?",
        ["Lumbar puncture immediately, then antibiotics after CSF results",
         "Blood cultures, dexamethasone and empiric antibiotics first, then CT brain, then lumbar puncture",
         "CT brain first, then lumbar puncture, then antibiotics only if CSF is abnormal",
         "Start antibiotics only after a positive blood culture",
         "Lumbar puncture without imaging because neck stiffness confirms meningitis"],
        1,
        """ผู้ป่วยรายนี้มี **ข้อบ่งชี้ให้ทำ CT ก่อนเจาะหลังถึงสามข้อ** — **อายุมากกว่า 60 ปี**, **ระดับการรู้ตัวเปลี่ยน** และ **focal deficit (right hemiparesis)**

แต่สไลด์ย้ำว่า **bacterial meningitis เป็น neurologic emergency** และ *"Empiric antibiotics should be initiated as soon as the diagnosis of bacterial meningitis is considered"* — **DO NOT DELAY TREATMENT**

**ลำดับที่ถูกต้อง**
1. **เจาะ blood culture** (ขึ้นเชื้อได้ถึง 70%)
2. **ให้ dexamethasone ก่อนหรือพร้อมยาปฏิชีวนะโดสแรก**
3. **ให้ยาปฏิชีวนะ empiric ทันที**
4. **ทำ CT brain**
5. **เจาะหลังเมื่อปลอดภัย**

**ทำไมข้ออื่นผิด**
- **เจาะหลังทันทีโดยไม่ทำภาพ** ในผู้ป่วยที่มี focal deficit เสี่ยงต่อ **cerebral herniation**
- **รอผล CSF หรือรอ hemoculture ก่อนให้ยา** ทำให้เสียเวลาหลายชั่วโมง ซึ่งสัมพันธ์กับอัตราตายที่สูงขึ้นชัดเจน
- CSF ที่เจาะหลังได้ยาไปไม่กี่ชั่วโมง **ยังแปลผล cell count, protein, glucose และส่ง PCR ได้**""",
        "สงสัย bacterial meningitis = ให้ยาก่อน อย่ารอภาพหรือผลเพาะเชื้อ — hemoculture → dexamethasone → ยา → CT → LP",
        "Management sequence in suspected bacterial meningitis",
        ["สไลด์ อ.พิมลพรรณ — Meningitis investigation & treatment", "Continuum (Minneap Minn) 2021;27(4):818-835"]),
    mcq("NEU-CNS-MCQ-03",
        "Which of the following is NOT one of the features listed in the lecture that should prompt CT brain before lumbar puncture?",
        ["Age older than 60 years", "Immunocompromise", "A seizure proximate to presentation", "Neck stiffness on examination", "Focal deficits on examination"],
        3,
        """**คอแข็ง (neck stiffness) ไม่ใช่ข้อบ่งชี้ให้ทำ CT ก่อนเจาะหลัง** — ตรงกันข้าม มันเป็น **อาการแสดงของเยื่อหุ้มสมองอักเสบเอง** และไม่ได้บ่งบอกว่ามีก้อนหรือความดันในกะโหลกสูง

**ห้าข้อที่สไลด์ระบุ**
1. **อายุมากกว่า 60 ปี**
2. **ภูมิคุ้มกันบกพร่อง**
3. **การชักใกล้เวลาที่มาพบแพทย์**
4. **ระดับการรู้ตัวเปลี่ยน**
5. **Focal deficit จากการตรวจร่างกาย**

**เหตุผลเบื้องหลัง** — ทั้งห้าข้อเพิ่มความน่าจะเป็นของ **space-occupying lesion** ซึ่งถ้าเจาะหลังไปโดยไม่รู้ อาจทำให้เกิด **การเคลื่อนของเนื้อสมอง (herniation)**

> ข้อควรระวังที่ตามมาเสมอ — **การทำ CT ต้องไม่หน่วงการให้ยาปฏิชีวนะ** ให้เจาะ hemoculture แล้วให้ dexamethasone กับยาปฏิชีวนะไปก่อนระหว่างรอภาพ""",
        "คอแข็งคืออาการของโรค ไม่ใช่เหตุผลให้ทำ CT — จำห้าข้อจริง: อายุ ภูมิคุ้มกัน ชัก รู้ตัวเปลี่ยน focal deficit",
        "Indications for CT before LP",
        ["สไลด์ อ.พิมลพรรณ — Meningitis investigation"]),
    ])

sec("neuro-cns-03", "CSF interpretation — ตารางที่ต้องจำให้ขึ้นใจ",
    "opening pressure · cell · protein · glucose ratio ของสี่กลุ่มเชื้อ", 11,
"""สไลด์ระบุสิ่งที่ต้องส่งตรวจจากน้ำไขสันหลังไว้ครบชุด

- **Cell count and differential**
- **Colour and appearance**
- **Opening pressure และ closing pressure**
- **Protein และ sugar**
- **PCR for viral panel, Cryptococcal antigen, India ink stain**
- **Microbiology — Gram stain และ culture**

### ค่าปกติของน้ำไขสันหลังผู้ใหญ่

| ค่า | ปกติ |
|---|---|
| Opening pressure | **6–20 cmH₂O** |
| ลักษณะ | ใสเหมือนน้ำ (clear, colourless) |
| WBC | **0–5 cells/mm³** ส่วนใหญ่เป็น lymphocyte |
| Protein | **15–45 mg/dL** |
| Glucose | **≥ 60% ของระดับน้ำตาลในเลือด** (ราว 50–80 mg/dL) |

> **ต้องเจาะน้ำตาลในเลือดพร้อมกับเจาะหลังเสมอ** เพราะค่าที่ใช้แปลผลคือ **อัตราส่วน CSF/serum glucose** ไม่ใช่ตัวเลข CSF เดี่ยว ๆ

### ตารางแยกสี่กลุ่ม — หัวใจของคาบนี้

| | **Bacterial** | **Viral** | **TB** | **Cryptococcal** |
|---|---|---|---|---|
| **ลักษณะ** | ขุ่น | ใส | ใสหรือขุ่นเล็กน้อย, อาจมี fibrin web | ใส |
| **Opening pressure** | สูง | ปกติหรือสูงเล็กน้อย | สูง | **สูงมาก** |
| **WBC** | **1,000–5,000** | **10–500** | **50–500** | 20–200 |
| **ชนิดเซลล์เด่น** | **Neutrophil (PMN)** | **Lymphocyte** | **Lymphocyte** | **Lymphocyte** |
| **Protein** | **สูงมาก > 100** | ปกติหรือสูงเล็กน้อย | **สูงมาก** | สูง |
| **Glucose (CSF/serum)** | **ต่ำมาก < 0.4** | **ปกติ** | **ต่ำ** | ต่ำ |
| **การตรวจจำเพาะ** | Gram stain, culture | **PCR viral panel** | AFB, TB-PCR, culture | **India ink, CryptoAg** |

### จุดที่คนพลาดบ่อย
- **Viral pattern = เซลล์เป็น lymphocyte + น้ำตาลปกติ + โปรตีนปกติหรือสูงเล็กน้อย** สไลด์ระบุไว้ชัดในหัวข้อ encephalitis ว่า **mononuclear pleocytosis ได้ถึง 200 WBC/mm³, glucose ปกติ, protein ปกติหรือสูงเล็กน้อย**
- **น้ำตาลต่ำ = แบคทีเรีย เชื้อรา หรือวัณโรค** — ไวรัสมักไม่ทำให้น้ำตาลต่ำ ยกเว้นบางราย (mumps, LCMV)
- **ช่วงแรกของ bacterial meningitis อาจยังเป็น lymphocyte เด่นได้** และ **ช่วงแรกของ viral meningitis อาจเป็น neutrophil เด่นได้** — จึงต้องดูภาพรวมทั้งหมด ไม่ใช่ดูชนิดเซลล์อย่างเดียว
- **Cryptococcal meningitis มี opening pressure สูงมาก** และการระบายความดันซ้ำ ๆ มีผลต่อการรอดชีวิตพอ ๆ กับยาต้านเชื้อรา

*(หมายเหตุ: ตาราง CSF ในสไลด์ต้นฉบับอยู่ในรูปภาพ ค่าที่ใช้ที่นี่อ้างอิงเกณฑ์มาตรฐานที่ใช้ทั่วไป ควรเทียบกับสไลด์จริงอีกครั้ง)*
""",
    ["เจาะน้ำตาลในเลือดพร้อมเจาะหลังทุกครั้ง เพราะต้องใช้อัตราส่วน CSF/serum",
     "Neutrophil เด่น + น้ำตาลต่ำมาก + โปรตีนสูงมาก = bacterial",
     "Lymphocyte เด่น + น้ำตาลปกติ = viral",
     "Lymphocyte เด่น + น้ำตาลต่ำ + โปรตีนสูงมาก = TB หรือเชื้อรา",
     "Opening pressure สูงมาก + India ink บวก = cryptococcal"],
    [
    mcq("NEU-CNS-MCQ-04",
        "A 30-year-old man has fever, headache and neck stiffness. CSF shows opening pressure 28 cmH2O, WBC 2,400/mm3 with 92% neutrophils, protein 240 mg/dL, CSF glucose 18 mg/dL with simultaneous serum glucose 110 mg/dL. Which is the most likely diagnosis?",
        ["Viral meningitis", "Bacterial meningitis", "Tuberculous meningitis", "Cryptococcal meningitis", "Normal CSF"],
        1,
        """**รูปแบบนี้คือ bacterial meningitis แบบคลาสสิก**

| ค่า | ผู้ป่วย | แปลผล |
|---|---|---|
| WBC | **2,400** | สูงมาก อยู่ในช่วง 1,000–5,000 ของแบคทีเรีย |
| Differential | **92% neutrophil** | **PMN เด่น** |
| Protein | **240 mg/dL** | **สูงมาก (> 100)** |
| CSF/serum glucose | **18/110 = 0.16** | **ต่ำมาก (< 0.4)** |
| Opening pressure | 28 cmH₂O | สูง (ปกติ 6–20) |

**ทำไมข้ออื่นผิด**
- **Viral** — เซลล์เป็น **lymphocyte**, จำนวนน้อยกว่า (10–500), **น้ำตาลปกติ**, โปรตีนปกติหรือสูงเล็กน้อย
- **TB** — เซลล์ **lymphocyte** เด่น จำนวน 50–500 โปรตีนสูงมาก น้ำตาลต่ำ และอาการมักค่อยเป็นค่อยไปเป็นสัปดาห์
- **Cryptococcal** — **lymphocyte** เด่น จำนวนน้อย **opening pressure สูงมาก** มักอยู่ในผู้ป่วยภูมิคุ้มกันบกพร่อง

**สิ่งที่ต้องทำทันที** — ให้ **dexamethasone ก่อนหรือพร้อมยาปฏิชีวนะโดสแรก** แล้วให้ยาปฏิชีวนะ empiric โดยไม่รอผลเพาะเชื้อ""",
        "PMN เด่น + น้ำตาลต่ำมาก + โปรตีนสูงมาก = bacterial — อย่าลืมคำนวณอัตราส่วน CSF/serum glucose",
        "CSF interpretation — bacterial",
        ["สไลด์ อ.พิมลพรรณ — CSF analysis"]),
    mcq("NEU-CNS-MCQ-05",
        "A 24-year-old woman has 3 days of fever and headache. CSF shows WBC 120/mm3 with 88% lymphocytes, protein 52 mg/dL, CSF glucose 62 mg/dL with serum glucose 96 mg/dL. Which pattern does this represent and what is the most likely group of pathogens?",
        ["Bacterial pattern — Streptococcus pneumoniae",
         "Viral pattern — enterovirus, HSV-2 or VZV",
         "Tuberculous pattern — Mycobacterium tuberculosis",
         "Fungal pattern — Cryptococcus neoformans",
         "Malignant pattern — carcinomatous meningitis"],
        1,
        """**รูปแบบไวรัส** ตามที่สไลด์ระบุไว้ว่า typical viral CSF profile ประกอบด้วย

- **mononuclear pleocytosis ได้ถึง 200 WBC/mm³** ✓ (รายนี้ 120, lymphocyte 88%)
- **CSF glucose ปกติ** ✓ (62/96 = **0.65** ซึ่งสูงกว่า 0.6)
- **CSF protein ปกติหรือสูงเล็กน้อย** ✓ (52 mg/dL)

**เชื้อที่พบบ่อยที่สุดของ viral meningitis ตามสไลด์** — **Enterovirus, HSV-2 และ VZV**

**การรักษา**
- โดยทั่วไป **หายได้เอง (self-limited)** แต่ **อาจรุนแรงกว่าในผู้ป่วยภูมิคุ้มกันบกพร่อง**
- **HSV-2 และ VZV meningitis รักษาด้วย acyclovir 10 mg/kg IV วันละ 3 ครั้ง นาน 14–21 วัน**

**ทำไมข้ออื่นผิด** — แบคทีเรียต้องมี PMN เด่น น้ำตาลต่ำมาก · TB และ cryptococcus แม้จะเป็น lymphocyte เด่นเหมือนกัน แต่ **น้ำตาลต้องต่ำ** ซึ่งรายนี้ปกติ และดำเนินโรคช้ากว่า 3 วัน""",
        "Lymphocyte เด่น + น้ำตาลปกติ + โปรตีนเกือบปกติ = viral — HSV-2 และ VZV ให้ acyclovir 14–21 วัน",
        "CSF interpretation — viral",
        ["สไลด์ อ.พิมลพรรณ — Viral meningitis & Encephalitis CSF profile"]),
    mcq("NEU-CNS-MCQ-06",
        "A patient with advanced HIV has 3 weeks of headache. CSF opening pressure is 42 cmH2O, WBC 45/mm3 (lymphocyte predominant), protein 88 mg/dL, CSF glucose 34 mg/dL (serum 98 mg/dL). Which additional CSF test is most likely to confirm the diagnosis rapidly?",
        ["Gram stain", "India ink stain and cryptococcal antigen", "Acid-fast bacilli smear only", "Viral PCR panel", "Cytology for malignant cells"],
        1,
        """**Cryptococcal meningitis** — ผู้ป่วย HIV ระยะท้าย, อาการค่อยเป็นค่อยไปเป็นสัปดาห์, **opening pressure สูงมาก (42 cmH₂O)**, lymphocyte เด่น, น้ำตาลต่ำ (34/98 = 0.35)

สไลด์ระบุการตรวจ CSF ไว้ว่าต้องส่ง **"PCR for viral panel, CryptoAg, india ink stain"** — สองอย่างหลังคือการตรวจที่ยืนยัน cryptococcus ได้เร็ว

**การรักษาตามสไลด์**

| ระยะ | ยา |
|---|---|
| **Induction** | **Amphotericin B 0.7–1.0 mg/kg/d** หรือ **liposomal amphotericin B 3–4 mg/kg/d** **PLUS fluconazole 800 mg/d นาน 2 สัปดาห์** |
| **Consolidation** | **Fluconazole 400–800 mg/d นาน 8–10 สัปดาห์** |
| **Secondary prophylaxis** | **Fluconazole 200–400 mg/d นาน 1 ปี** |

**เชื้อ** — ส่วนใหญ่เป็น **C. neoformans** แต่ **C. gattii ก่อโรคในผู้ที่ภูมิคุ้มกันปกติได้**

> **อย่าลืมจัดการความดันในกะโหลก** — opening pressure ที่สูงมากต้องระบายน้ำไขสันหลังซ้ำ ๆ ซึ่งมีผลต่อการรอดชีวิตอย่างมีนัยสำคัญ""",
        "HIV + ปวดศีรษะเรื้อรัง + opening pressure สูงมาก = cryptococcus → India ink + CryptoAg และต้องระบายความดันด้วย",
        "Cryptococcal meningitis",
        ["สไลด์ อ.พิมลพรรณ — Fungal / Cryptococcal Meningitis"]),
    ])

sec("neuro-cns-04", "Bacterial meningitis — ภาวะฉุกเฉินทางระบบประสาท",
    "ยาปฏิชีวนะทันที · dexamethasone ให้เมื่อไรและได้ผลกับเชื้อใด", 8,
"""> **Bacterial meningitis is a neurologic emergency**
> *"Empiric antibiotics should be initiated as soon as the diagnosis of bacterial meningitis is considered"* — **DO NOT DELAY TREATMENT**

### Dexamethasone — จุดที่ออกสอบมากที่สุด
สไลด์ระบุไว้สองประโยคที่ต้องจำแยกกัน

1. **ต้องให้ก่อนหรือพร้อมกับยาปฏิชีวนะโดสแรก** (initiated before or with the first dose of antibiotics)
2. **แสดงประโยชน์เฉพาะใน streptococcal meningitis เท่านั้น**

**ทำไมต้องให้ก่อนหรือพร้อมยา** — ยาปฏิชีวนะฆ่าเชื้อแล้วทำให้ผนังเซลล์แบคทีเรียแตก ปล่อยสารกระตุ้นการอักเสบออกมาเป็นระลอก **steroid ต้องอยู่ในตัวก่อนที่ระลอกนั้นจะเกิด** จึงจะลดการอักเสบและลดภาวะแทรกซ้อนได้ ถ้าให้ตามหลังไปหลายชั่วโมงก็ไม่มีประโยชน์

**เชื้อที่สไลด์ยกมาเป็นสาเหตุหลัก** — **Streptococcus pneumoniae** และ **Neisseria meningitidis**

### แนวทางเชิงปฏิบัติ
- ให้ **empiric antibiotic ครอบคลุม S. pneumoniae และ N. meningitidis** ทันทีที่คิดถึงโรคนี้
- ในผู้ป่วยกลุ่มเสี่ยง (อายุมาก ภูมิคุ้มกันบกพร่อง ตั้งครรภ์) ต้อง **ครอบคลุม Listeria** เพิ่มด้วย
- **ปรับยาตามผลเพาะเชื้อ** เมื่อได้ผล
- **เจาะ blood culture ทุกราย** เพราะขึ้นเชื้อได้ถึง **70%**
""",
    ["Dexamethasone ต้องให้ก่อนหรือพร้อมยาปฏิชีวนะโดสแรก ให้ช้ากว่านั้นไม่มีประโยชน์",
     "Dexamethasone แสดงประโยชน์เฉพาะใน streptococcal meningitis",
     "Bacterial meningitis = neurologic emergency ให้ยาทันทีที่คิดถึง",
     "S. pneumoniae และ N. meningitidis คือสองเชื้อหลักที่สไลด์เน้น"],
    [
    mcq("NEU-CNS-MCQ-07",
        "Regarding adjunctive dexamethasone in bacterial meningitis, which statement matches the lecture?",
        ["It should be given 24 hours after antibiotics to reduce rebound inflammation",
         "It should be initiated before or with the first dose of antibiotics, and shows benefit mainly in streptococcal meningitis",
         "It benefits all causes of bacterial meningitis equally",
         "It replaces the need for empiric antibiotics in mild cases",
         "It is contraindicated in all patients with bacterial meningitis"],
        1,
        """สไลด์ระบุไว้ตรง ๆ ว่า *"Dexamethasone should be **initiated before or with the first dose of antibiotics**, but show **benefit only in streptococcal meningitis**"*

**สองประเด็นที่ต้องแยกให้ขาด**

| ประเด็น | คำตอบ |
|---|---|
| **ให้เมื่อไร** | **ก่อนหรือพร้อมยาปฏิชีวนะโดสแรก** |
| **ได้ผลกับเชื้อใด** | **Streptococcal (S. pneumoniae) เป็นหลัก** |

**กลไก** — ยาปฏิชีวนะที่ฆ่าเชื้อทำให้ผนังเซลล์แตกและปล่อยสารกระตุ้นการอักเสบเป็นระลอกใหญ่ **steroid ต้องอยู่ในร่างกายก่อนระลอกนั้น** จึงจะลดการอักเสบในช่องใต้เยื่อหุ้มสมอง ลดการสูญเสียการได้ยินและภาวะแทรกซ้อนทางระบบประสาท

**ทำไมข้ออื่นผิด** — ให้หลังยา 24 ชั่วโมงถือว่าสายเกินไป · ประโยชน์ไม่เท่ากันในทุกเชื้อ · **steroid ไม่เคยใช้แทนยาปฏิชีวนะ** · และไม่ได้เป็นข้อห้ามในผู้ป่วยทั่วไป""",
        "Dexamethasone: ให้ก่อนหรือพร้อมยาโดสแรก และได้ผลกับ streptococcal เป็นหลัก",
        "Adjunctive dexamethasone",
        ["สไลด์ อ.พิมลพรรณ — Bacterial Meningitis treatment", "Continuum 2021;27(4):818-835"]),
    ])

sec("neuro-cns-05", "Tuberculous meningitis",
    "สูตร 2 IRZE / 10 IR · dexamethasone ลดขนาดใน 6–8 สัปดาห์ · สามภาวะแทรกซ้อน", 8,
"""### การรักษาตามสไลด์

**ยาต้านวัณโรค** — **isoniazid, rifampin, pyrazinamide และ ethambutol** ในสูตร **2 IRZE / 10 IR**
คือ **ระยะเข้มข้น 4 ตัว 2 เดือน แล้วต่อด้วย isoniazid + rifampin อีก 10 เดือน รวม 12 เดือน** ซึ่ง **ยาวกว่าวัณโรคปอด** ที่ใช้ 6 เดือน

**Dexamethasone ในระยะแรก แล้วค่อย ๆ ลดขนาดใน 6–8 สัปดาห์**

| สัปดาห์ | ขนาด |
|---|---|
| **1** | **0.4 mg/kg/day** |
| **2** | **0.3 mg/kg/day** |
| **3** | **0.2 mg/kg/day** |
| **4** | **0.1 mg/kg/day** |

> สังเกตว่า **steroid ใน TB meningitis ให้เป็นสัปดาห์และค่อย ๆ ลด** ต่างจาก bacterial meningitis ที่ให้สั้น ๆ พร้อมยาปฏิชีวนะโดสแรก — เป็นจุดที่สับสนกันบ่อย

### ภาวะแทรกซ้อนที่พบบ่อย — สไลด์ระบุสามข้อ
- **Vasculitis** → ทำให้เกิด **stroke** โดยเฉพาะบริเวณ basal ganglia
- **Hydrocephalus** → จาก exudate ที่ฐานสมองอุดทางเดินน้ำไขสันหลัง
- **Cranial neuropathies** → จาก exudate หุ้มเส้นประสาทสมองที่ฐานสมอง โดยเฉพาะ **CN VI, III, VII**

### เบาะแสทางคลินิกที่ทำให้คิดถึง TB meningitis
- อาการ **ค่อยเป็นค่อยไปเป็นสัปดาห์** ไม่ใช่เป็นวันแบบแบคทีเรียทั่วไป
- **CSF: lymphocyte เด่น, โปรตีนสูงมาก, น้ำตาลต่ำ**
- ภาพอาจพบ **basal meningeal enhancement, hydrocephalus, infarction**
- ประวัติสัมผัสวัณโรคหรือมีวัณโรคที่อวัยวะอื่น
""",
    ["TB meningitis ใช้ 2 IRZE / 10 IR รวม 12 เดือน ยาวกว่าวัณโรคปอด",
     "Dexamethasone ลดขนาดเป็นขั้น 0.4 → 0.3 → 0.2 → 0.1 mg/kg/day ใน 6–8 สัปดาห์",
     "สามภาวะแทรกซ้อน: vasculitis (stroke) · hydrocephalus · cranial neuropathy",
     "อาการค่อยเป็นค่อยไปเป็นสัปดาห์ + lymphocyte เด่น + น้ำตาลต่ำ = คิดถึง TB"],
    [
    mcq("NEU-CNS-MCQ-08",
        "A 35-year-old man has 3 weeks of progressive headache, low-grade fever and new left sixth nerve palsy. CSF shows 220 WBC/mm3 (lymphocyte predominant), protein 190 mg/dL, glucose ratio 0.28. Which treatment regimen matches the lecture?",
        ["2 months of isoniazid, rifampin, pyrazinamide and ethambutol, then 10 months of isoniazid and rifampin, with tapering dexamethasone",
         "Ceftriaxone for 14 days with dexamethasone for 4 days",
         "Acyclovir 10 mg/kg IV three times daily for 21 days",
         "Amphotericin B plus fluconazole for 2 weeks then fluconazole consolidation",
         "Vancomycin plus a third-generation cephalosporin for 6-8 weeks"],
        0,
        """**Tuberculous meningitis** — อาการค่อยเป็นค่อยไปเป็นสัปดาห์, **cranial neuropathy (CN VI palsy)**, CSF **lymphocyte เด่น โปรตีนสูงมาก น้ำตาลต่ำ**

**สูตรที่สไลด์ระบุ** — **2 IRZE / 10 IR**
- **ระยะเข้มข้น 2 เดือน**: isoniazid, rifampin, pyrazinamide, ethambutol
- **ระยะต่อเนื่อง 10 เดือน**: isoniazid, rifampin
- **รวม 12 เดือน**

**Dexamethasone ในระยะแรกแล้วค่อย ๆ ลดใน 6–8 สัปดาห์** — 0.4 → 0.3 → 0.2 → 0.1 mg/kg/day สัปดาห์ละขั้น

**CN VI palsy อธิบายด้วยอะไร** — เป็นหนึ่งใน **สามภาวะแทรกซ้อนที่สไลด์เน้น** คือ **vasculitis, hydrocephalus และ cranial neuropathies** ซึ่งเกิดจาก exudate หนาที่ฐานสมองไปหุ้มเส้นประสาทสมอง

**ทำไมข้ออื่นผิด** — ceftriaxone สั้น ๆ เป็นสูตรของ **bacterial** · acyclovir ของ **HSV/VZV** · amphotericin + fluconazole ของ **cryptococcus** · vancomycin + cephalosporin 6–8 สัปดาห์เป็นสูตรของ **spinal epidural abscess / spondylodiscitis**""",
        "TB meningitis = 2 IRZE/10 IR รวม 12 เดือน + dexamethasone ลดขนาด 6–8 สัปดาห์",
        "Tuberculous meningitis",
        ["สไลด์ อ.พิมลพรรณ — Tuberculous Meningitis"]),
    ])

sec("neuro-cns-06", "Encephalitis — เมื่อเนื้อสมองเองอักเสบ",
    "HSV-1 ที่ temporal lobe · JE ที่ thalamus สองข้าง · เริ่ม acyclovir ก่อนผลยืนยัน", 10,
"""### แยก meningitis กับ encephalitis

| | **Meningitis** | **Encephalitis** |
|---|---|---|
| อักเสบที่ | **เยื่อหุ้มสมอง** | **เนื้อสมอง** |
| อาการเด่น | **ไข้ ปวดศีรษะ คอแข็ง** | **ไข้ ปวดศีรษะ + ระดับการรู้ตัวเปลี่ยน** |
| Focal deficit | ไม่ค่อยมี | **มีได้** |
| ชัก | ไม่ค่อยมี | **มีได้** |

**อาการและอาการแสดงของ encephalitis ตามสไลด์** — **Headache · Fever · Altered mental status · Focal neurologic deficits · Seizures**

**สาเหตุ** — **ส่วนใหญ่เป็นไวรัส** เชื้อที่พบบ่อยที่สุดคือ **HSV-1, VZV, Japanese encephalitis (JE) และ Enterovirus**

### การสืบค้น

**1) Brain imaging — ภาพช่วยแยกเชื้อได้**

| เชื้อ | ลักษณะภาพ |
|---|---|
| **Herpes simplex encephalitis** | **asymmetric FLAIR hyperintensity และ restricted diffusion ที่ temporal lobe, insula และ cingulate gyrus** |
| **Japanese encephalitis** | **symmetric FLAIR hyperintensity ที่ thalamus สองข้าง** |

> จำคู่นี้ให้แม่น — **HSV = ไม่สมมาตร ที่ขมับ** · **JE = สมมาตร ที่ทาลามัสสองข้าง**

**2) CSF analysis + PCR viral panel**
รูปแบบ CSF ของไวรัสตามสไลด์
- **mononuclear pleocytosis ได้ถึง 200 WBC/mm³**
- **CSF glucose ปกติ**
- **CSF protein ปกติหรือสูงเล็กน้อย**

### การรักษา
- **เริ่ม acyclovir ทางหลอดเลือดดำทันทีที่สงสัย HSV encephalitis** โดย **ไม่ต้องรอผล PCR** เพราะการรักษาช้าสัมพันธ์กับความพิการและการเสียชีวิตอย่างชัดเจน
- **พิจารณาให้ยากันชักเมื่อมีการชัก** (สไลด์ระบุ *"Consider AED if seizure presents"*)
- ดูแลประคับประคอง เฝ้าระวังความดันในกะโหลกสูง
""",
    ["Encephalitis = ไข้ + ปวดศีรษะ + รู้ตัวเปลี่ยน ± focal deficit ± ชัก",
     "HSV = ไม่สมมาตรที่ temporal lobe, insula, cingulate · JE = สมมาตรที่ thalamus สองข้าง",
     "สงสัย HSV encephalitis ให้ acyclovir ทันที ห้ามรอผล PCR",
     "CSF ไวรัส: mononuclear ถึง 200 cells · น้ำตาลปกติ · โปรตีนปกติหรือสูงเล็กน้อย"],
    [
    mcq("NEU-CNS-MCQ-09",
        "A 52-year-old man presents with 3 days of fever, confusion and a witnessed seizure. MRI shows asymmetric FLAIR hyperintensity with restricted diffusion in the right temporal lobe, insula and cingulate gyrus. What is the most appropriate immediate action?",
        ["Await CSF PCR results before starting any antiviral therapy",
         "Start intravenous acyclovir immediately",
         "Start ceftriaxone and dexamethasone only",
         "Start antituberculous therapy",
         "Perform urgent brain biopsy before treatment"],
        1,
        """**ภาพนี้คือ herpes simplex encephalitis แบบตำรา** — สไลด์ระบุว่า HSE แสดง **asymmetric FLAIR hyperintensity และ restriction of diffusion ที่ temporal lobe, insula และ cingulate gyrus**

**ต้องเริ่ม acyclovir ทางหลอดเลือดดำทันที โดยไม่รอผล PCR** เพราะ
- HSE ที่ไม่ได้รักษามีอัตราตายสูงมาก
- **ทุกชั่วโมงที่ล่าช้าเพิ่มความพิการที่หลงเหลือ**
- acyclovir มีความปลอดภัยสูงพอที่จะให้ไปก่อนแล้วหยุดเมื่อผลออกว่าไม่ใช่

**การสืบค้นที่ทำคู่กันไป** — **CSF analysis + PCR viral panel** ซึ่งคาดว่าจะพบ **mononuclear pleocytosis ได้ถึง 200 WBC/mm³, น้ำตาลปกติ, โปรตีนปกติหรือสูงเล็กน้อย** และอาจพบเม็ดเลือดแดงจากลักษณะ hemorrhagic ของ HSE

**พิจารณายากันชัก** เพราะผู้ป่วยชักไปแล้ว ตามที่สไลด์ระบุ *"Consider AED if seizure presents"*

**ทำไมข้ออื่นผิด** — **รอผล PCR** คือความผิดพลาดที่อันตรายที่สุด · ceftriaxone อย่างเดียวไม่ครอบคลุมไวรัส (แม้จะให้ควบคู่ไปก่อนได้ขณะยังแยกจาก bacterial meningitis ไม่ออก) · ไม่มีอะไรชี้ไปวัณโรค · **brain biopsy ไม่ใช่ขั้นแรกในยุคที่มี PCR และ MRI**""",
        "MRI ขมับไม่สมมาตร + สับสน + ชัก = HSE → acyclovir ทันที อย่ารอ PCR",
        "Herpes simplex encephalitis",
        ["สไลด์ อ.พิมลพรรณ — Encephalitis imaging & treatment", "Continuum 2021;27(4):855-886"]),
    mcq("NEU-CNS-MCQ-10",
        "A 12-year-old boy from a rural rice-farming area develops fever, headache and altered consciousness in the rainy season. MRI shows symmetric FLAIR hyperintensity of both thalami. Which pathogen is most likely?",
        ["Herpes simplex virus type 1", "Japanese encephalitis virus", "Cryptococcus neoformans", "Mycobacterium tuberculosis", "Streptococcus pneumoniae"],
        1,
        """**ทาลามัสสองข้างสว่างแบบสมมาตร = Japanese encephalitis** ตามที่สไลด์ระบุว่า JE แสดง **symmetric FLAIR hyperintensity ใน bilateral thalamus**

**บริบทช่วยยืนยัน** — เด็กจากพื้นที่ทำนาในฤดูฝน เข้ากับวงจรการระบาดของ JE ซึ่งมี **ยุง Culex** เป็นพาหะ และมี **หมูกับนกลุยน้ำเป็นแหล่งรังโรค** — เป็นโรคที่ยังพบในประเทศไทยและ **ป้องกันได้ด้วยวัคซีน**

**เทียบภาพกับ HSV**

| | **HSV-1** | **JE** |
|---|---|---|
| ความสมมาตร | **ไม่สมมาตร** | **สมมาตร** |
| ตำแหน่ง | **temporal lobe, insula, cingulate gyrus** | **thalamus สองข้าง** |
| การรักษาจำเพาะ | **acyclovir** | ประคับประคอง ไม่มียาต้านไวรัสจำเพาะ |

> แม้ภาพจะเข้ากับ JE มาก **ในทางปฏิบัติยังควรให้ acyclovir ไปก่อน** จนกว่าจะตัด HSV ออกได้ เพราะ HSV เป็นเชื้อเดียวในกลุ่มนี้ที่มียารักษาจำเพาะและเสียหายมากถ้าพลาด

**ทำไมข้ออื่นผิด** — cryptococcus และ TB ดำเนินโรคเป็นสัปดาห์และให้ภาพที่ฐานสมองหรือ hydrocephalus · S. pneumoniae ทำให้เกิด meningitis ไม่ใช่ภาพทาลามัสสองข้าง""",
        "ทาลามัสสองข้างสมมาตร = JE · ขมับไม่สมมาตร = HSV — แต่ยังให้ acyclovir ไปก่อนจนกว่าจะตัด HSV ออก",
        "Japanese encephalitis",
        ["สไลด์ อ.พิมลพรรณ — Encephalitis imaging"]),
    ])

sec("neuro-cns-07", "Brain abscess — ระยะ เชื้อ และภาพ",
    "cerebritis → encapsulation · streptococci > ครึ่ง · ring enhancement · ห้ามเจาะหลัง", 10,
"""### อาการและอาการแสดง
- **ปวดศีรษะแบบค่อยเป็นค่อยไป (subacute onset headache)** — อาการที่พบบ่อยที่สุด
- **ไข้พบน้อยกว่า 50%** ← จุดที่ทำให้พลาดบ่อยที่สุด **ไม่มีไข้ไม่ตัดฝีในสมองออก**
- **ระดับการรู้ตัวเปลี่ยน**
- **Focal neurologic deficits**
- **ชัก**

### ชนิดตามตำแหน่ง
**Subdural empyema · Epidural abscess · Intracerebral abscess**

### สามระยะของการเกิดฝี

| ระยะ | สิ่งที่เกิดขึ้น |
|---|---|
| **Early cerebritis** | เชื้อเข้าสู่ CNS เกิดการอักเสบเฉพาะที่ — **เนื้อตายระยะแรก บวมน้ำ และมี neutrophil มารวมตัว** |
| **Late cerebritis** | **macrophage และ lymphocyte แทรกเข้ามา เกิดเนื้อตายตรงกลาง** |
| **Encapsulation** | **ภายในไม่กี่สัปดาห์ รอยโรคถูกล้อมด้วยผนังพังผืดที่มีหลอดเลือดเลี้ยงชัดเจน** ซึ่งจำกัดการลุกลามและปกป้องเนื้อสมองรอบข้าง |

> ระยะนี้สำคัญเพราะ **กำหนดว่าจะรักษาด้วยยาอย่างเดียวได้หรือไม่**

### เชื้อก่อโรค
- **ผู้ที่ภูมิคุ้มกันปกติ: streptococcal species ทั้งชนิดใช้และไม่ใช้ออกซิเจน** พบ **มากกว่าครึ่งหนึ่งของผู้ป่วย** และ **มักสัมพันธ์กับการติดเชื้อในไซนัส**
- ส่วนใหญ่เป็นแบคทีเรีย แต่เกิดจาก **เชื้อราและปรสิต** ได้
- **Cryptic brain abscess — หาแหล่งต้นตอไม่พบ พบ 20–30% ของฝีในสมองทั้งหมด**

### ภาพวินิจฉัย

**CT brain with contrast** — **hypodensity mass-like lesion ที่มี contrast-enhancing ring**

**MRI brain with Gd — bacterial brain abscess**
- **รอยโรคใหญ่ ขอบเขตชัด มีขอบ hypointense และบวมน้ำรอบ ๆ มาก**
- **ขอบ enhancement เรียบและบาง บน postcontrast T1W**
- **ตรงกลางรอยโรค restrict diffusion อย่างชัดเจน** ← จุดแยกสำคัญจากเนื้องอก

**MRI — cerebral toxoplasmosis**
- **รอยโรค hypointense หลายจุด เด่นที่ basal ganglia และรอยต่อ corticomedullary**
- **ขอบ enhancement บาง หรือ enhance แบบ nodular**

### การสืบค้น
- **Brain imaging**
- **Blood culture**
- **Pus aspiration / excision**
- **CSF analysis is NOT recommended** ← **ห้ามเจาะหลัง** เพราะเสี่ยง herniation และไม่ช่วยวินิจฉัย
""",
    ["ไข้พบน้อยกว่า 50% ในฝีสมอง — ไม่มีไข้ไม่ตัดออก",
     "Streptococci พบมากกว่าครึ่ง และมักมาจากไซนัส",
     "ฝีสมอง restrict diffusion ตรงกลาง ต่างจากเนื้องอกที่มักไม่ restrict",
     "ห้ามเจาะหลังในผู้ป่วยฝีในสมอง — CSF analysis is NOT recommended",
     "Cryptic abscess หาต้นตอไม่พบ 20–30%"],
    [
    mcq("NEU-CNS-MCQ-11",
        "A 40-year-old man has 2 weeks of worsening headache, mild left arm weakness and one seizure. He is afebrile. CT with contrast shows a ring-enhancing hypodense lesion in the right frontal lobe. Which of the following should NOT be performed?",
        ["Blood cultures", "MRI brain with gadolinium", "Lumbar puncture for CSF analysis", "Search for a sinus or dental source", "Neurosurgical consultation for aspiration"],
        2,
        """สไลด์ระบุไว้ชัดในหัวข้อ investigation ของ brain abscess ว่า **"CSF analysis is NOT recommended"**

**เหตุผล**
1. **เสี่ยงต่อ cerebral herniation** เพราะฝีเป็น space-occupying lesion ที่มีสมองบวมรอบ ๆ มาก
2. **ไม่ช่วยวินิจฉัย** — CSF มักแสดงเพียงการอักเสบแบบไม่จำเพาะ และเพาะเชื้อมักไม่ขึ้นเพราะฝีถูกล้อมด้วยผนัง

**สิ่งที่ควรทำแทน** — **brain imaging · blood culture · และ pus aspiration/excision** ซึ่งเป็นการตรวจที่ให้เชื้อก่อโรคจริง

**อย่าให้การไม่มีไข้หลอก** — สไลด์ระบุว่า **ไข้พบน้อยกว่า 50%** ในผู้ป่วยฝีในสมอง อาการที่พบบ่อยที่สุดคือ **ปวดศีรษะแบบค่อยเป็นค่อยไป** ร่วมกับ **focal deficit และชัก**

**และต้องตามหาแหล่งต้นตอเสมอ** — ฝีที่กลีบหน้ามักมาจาก **ไซนัสหรือฟัน** สอดคล้องกับที่ streptococci **สัมพันธ์กับการติดเชื้อในไซนัส**""",
        "เห็น ring-enhancing lesion อย่าเจาะหลัง — ส่ง blood culture และปรึกษาประสาทศัลยแพทย์เพื่อดูดหนอง",
        "Brain abscess workup",
        ["สไลด์ อ.พิมลพรรณ — Brain abscess investigations"]),
    mcq("NEU-CNS-MCQ-12",
        "On MRI, which feature best distinguishes a pyogenic brain abscess from a cystic or necrotic brain tumour?",
        ["Surrounding vasogenic oedema", "Ring enhancement after gadolinium", "Marked restricted diffusion in the centre of the lesion", "Mass effect on adjacent structures", "Hypointensity on T1-weighted images"],
        2,
        """**การ restrict diffusion อย่างชัดเจนที่ใจกลางรอยโรค** คือจุดแยกที่ดีที่สุด

สไลด์ระบุลักษณะของ bacterial brain abscess บน MRI ไว้สามข้อ
1. **รอยโรคใหญ่ ขอบเขตชัด มีขอบ hypointense และบวมน้ำรอบ ๆ มาก**
2. **ขอบ enhancement เรียบและบาง บน postcontrast T1W**
3. **ตรงกลางรอยโรค restrict diffusion อย่างชัดเจน**

**เหตุผลเชิงกลไก** — ใจกลางฝีคือ **หนองที่หนืดและเต็มไปด้วยเซลล์และเศษเนื้อตาย** โมเลกุลน้ำจึงเคลื่อนที่ไม่ได้ ตรงข้ามกับ **เนื้องอกที่เป็นถุงน้ำหรือเนื้อตาย ซึ่งมีของเหลวใสและน้ำเคลื่อนที่ได้อิสระ จึงไม่ restrict**

**ทำไมข้ออื่นผิด** — **บวมน้ำรอบรอยโรค, ring enhancement, mass effect และ T1 hypointense** พบได้ทั้งในฝีและเนื้องอก จึงแยกไม่ได้ อย่างไรก็ตาม **ขอบที่เรียบและบางสม่ำเสมอ** ช่วยสนับสนุนฝี ส่วนเนื้องอกมักมีขอบ **หนาและไม่สม่ำเสมอ**

> เทียบกับ **cerebral toxoplasmosis** ซึ่งสไลด์บรรยายว่าเป็น **รอยโรคหลายจุด เด่นที่ basal ganglia และรอยต่อ corticomedullary ขอบ enhancement บางหรือแบบ nodular**""",
        "ใจกลาง restrict diffusion = ฝี · ถุงน้ำของเนื้องอกไม่ restrict",
        "MRI of brain abscess",
        ["สไลด์ อ.พิมลพรรณ — MRI brain with Gd, bacterial brain abscess"]),
    ])

sec("neuro-cns-08", "Brain abscess — การรักษา",
    "ยาอย่างเดียวได้เมื่อไร · ดูดหรือผ่า · ระยะเวลา 6–8 สัปดาห์", 8,
"""### ใช้ยาอย่างเดียวได้เมื่อไร
สไลด์ระบุเงื่อนไขไว้สองข้อ **ต้องเข้าได้จึงจะรักษาด้วยยาอย่างเดียว**
- **ฝีขนาดเล็ก เส้นผ่านศูนย์กลางน้อยกว่า 2.5 ซม.**
- **อยู่ในระยะ early cerebritis**

**ระยะเวลาการให้ยา — 6–8 สัปดาห์**

### เมื่อไรต้องพึ่งประสาทศัลยแพทย์

| วิธี | ข้อบ่งชี้ |
|---|---|
| **Aspiration (ดูดหนอง)** | **ฝีขนาดใหญ่กว่า 1 ซม.** |
| **Surgical excision (ผ่าตัดเอาออก)** | **ฝีเดี่ยว (solitary)** · **อยู่ตื้น (superficial)** · **มีหลายช่อง (multi-loculated) ที่เสี่ยงระบายไม่หมด** · หรือ **ฝีใน posterior fossa ที่อาการทรุดเฉียบพลันจาก mass effect** |

> **สังเกตความต่างของตัวเลข** — ใช้ยาอย่างเดียวได้เมื่อ **< 2.5 ซม.** แต่ **ดูดหนองได้เมื่อ > 1 ซม.** ช่วงระหว่าง 1–2.5 ซม. จึงเป็นพื้นที่ที่ต้องใช้ดุลยพินิจร่วมกับระยะของโรคและตำแหน่ง

### Cerebral toxoplasmosis
**ระยะเวลาการรักษา 6 สัปดาห์**

### หลักที่ใช้ได้จริง
1. **เก็บหนองส่งเพาะเชื้อก่อนหรือพร้อมเริ่มยาเมื่อทำได้** เพราะเป็นโอกาสเดียวที่จะได้เชื้อจริง
2. **ตามหาและจัดการแหล่งต้นตอ** — ไซนัส หู ฟัน ลิ้นหัวใจ — มิฉะนั้นฝีจะกลับมา
3. **ติดตามด้วยภาพซ้ำ** เพื่อดูว่าฝียุบลงจริง
4. **ระวังการชัก** เพราะฝีเป็นจุดกำเนิดการชักที่พบบ่อย
""",
    ["ยาอย่างเดียวได้เมื่อฝี < 2.5 ซม. และอยู่ในระยะ early cerebritis เท่านั้น",
     "ดูดหนองได้เมื่อฝี > 1 ซม. · ผ่าตัดเอาออกเมื่อเดี่ยว ตื้น หลายช่อง หรือ posterior fossa ที่ทรุด",
     "ให้ยานาน 6–8 สัปดาห์ · toxoplasmosis 6 สัปดาห์",
     "ต้องจัดการแหล่งต้นตอ ไม่งั้นฝีกลับมา"],
    [
    mcq("NEU-CNS-MCQ-13",
        "According to the lecture, antimicrobial therapy alone (without surgery) may be appropriate for a brain abscess in which situation?",
        ["Any abscess smaller than 5 cm regardless of stage",
         "A small abscess less than 2.5 cm in diameter in the early cerebritis stage",
         "Any multi-loculated abscess",
         "A posterior fossa abscess with mass effect",
         "Any abscess in an immunocompetent patient"],
        1,
        """สไลด์ระบุเงื่อนไขของ **medical therapy alone** ไว้สองข้อ ซึ่ง **ต้องเข้าทั้งคู่**
- **ฝีขนาดเล็กกว่า 2.5 ซม.**
- **อยู่ในระยะ early cerebritis**

เหตุผลคือในระยะ early cerebritis **ยังไม่มีผนังพังผืดล้อม** ยาปฏิชีวนะจึงเข้าถึงรอยโรคได้ดี ตรงข้ามกับระยะ **encapsulation** ที่มี *"well-defined vascularized fibrotic capsule"* ซึ่งกั้นยาไม่ให้เข้าถึงหนองข้างใน

**ข้อบ่งชี้ผ่าตัดตามสไลด์**

| วิธี | เงื่อนไข |
|---|---|
| **Aspiration** | ฝี **> 1 ซม.** |
| **Excision** | **solitary · superficial · multi-loculated ที่เสี่ยงระบายไม่หมด · posterior fossa ที่ทรุดจาก mass effect** |

**ทำไมข้ออื่นผิด** — ขนาดอย่างเดียวไม่พอ ต้องดูระยะด้วย · **multi-loculated เป็นข้อบ่งชี้ให้ผ่าตัด** ไม่ใช่ให้ยาอย่างเดียว · **posterior fossa ที่มี mass effect เป็นภาวะฉุกเฉินทางศัลยกรรม** · และภูมิคุ้มกันปกติไม่ได้เป็นเกณฑ์ตัดสิน

**ระยะเวลาให้ยา 6–8 สัปดาห์**""",
        "ยาอย่างเดียวได้เฉพาะ ฝีเล็กกว่า 2.5 ซม. + ระยะ early cerebritis — พ้นจากนั้นต้องระบายหนอง",
        "Brain abscess treatment",
        ["สไลด์ อ.พิมลพรรณ — Brain abscess medical & neurosurgery approaches"]),
    ])

sec("neuro-cns-09", "Spine และ spinal cord infection",
    "spondylodiscitis · spinal epidural abscess · MRI with contrast · ภาวะฉุกเฉิน", 10,
"""### อาการและอาการแสดง
- **ปวดหลัง (back pain)** — **อาการที่พบบ่อยที่สุด และตรวจพบได้จากการเคาะกระดูกสันหลัง (spinal percussion)**
- **ไข้**
- **อาการอ่อนแรง**
- **ความรู้สึกเปลี่ยนแปลง**
- **การขับถ่ายผิดปกติ (bowel/bladder dysfunction)** และ **saddle anesthesia**

### ตำแหน่งที่ติดเชื้อได้
- **กระดูกสันหลัง (osteomyelitis)**
- **หมอนรองกระดูก (discitis)**
- **ช่อง epidural / subdural (abscess)**
- **เนื้อไขสันหลังเอง (infectious myelitis)**

**นิยามที่ต้องแยก**
- **Spondylodiscitis** = การติดเชื้อของ **กระดูกสันหลัง ข้อต่อระหว่างกระดูกสันหลัง หรือหมอนรองกระดูก**
- **Epidural abscess** = หนองที่สะสมใน **ช่องระหว่างโครงสร้างกระดูกสันหลังกับเยื่อดูรา**

### สาเหตุ (เส้นทางเข้าสู่ตำแหน่ง)
- **Hematogenous spread** จากแหล่งที่อยู่ไกล
- **Direct inoculation** จากหัตถการ
- **Contiguous spread** จากการติดเชื้อข้างเคียง

### เชื้อก่อโรค
- **ส่วนใหญ่เป็นแบคทีเรียก่อหนอง โดยเฉพาะ Staphylococcus aureus**
- Pseudomonas aeruginosa
- Coagulase-negative staphylococci
- Bartonella henselae (cat-scratch disease)
- **Mycobacterium tuberculosis** — เป็นสาเหตุของ **spondylodiscitis** (วัณโรคกระดูกสันหลัง)

### การสืบค้น — **MRI of the spine with contrast**

| ภาวะ | ลักษณะภาพ |
|---|---|
| **Spondylodiscitis** | **T2 hyperintensity และ contrast enhancement ที่หมอนรองกระดูก** อาจลามถึง endplate บนและล่าง |
| **Spinal epidural abscess** | **T2 hyperintensity ที่มีแกนกลาง T1 hypointense และขอบ enhance ด้วย gadolinium** |

### การรักษา

**ยาปฏิชีวนะ — ระยะเวลา 6–8 สัปดาห์**

| สูตร | เมื่อไร |
|---|---|
| **Vancomycin 15–20 mg/kg IV ทุก 8–12 ชม. + cephalosporin รุ่นที่ 3 ขนาด 2 g IV ทุก 24 ชม.** | สูตรมาตรฐาน |
| **Vancomycin + cefepime 2 g IV ทุก 8 ชม. หรือ ceftazidime 2 g IV ทุก 8 ชม. หรือ meropenem 1 g IV ทุก 8 ชม.** | **ผู้ที่เสี่ยง Pseudomonas** — เบาหวาน, เพิ่งได้ยาปฏิชีวนะ, เคยใส่อุปกรณ์ที่กระดูกสันหลัง, นอนโรงพยาบาล |

**การผ่าตัด — สไลด์กำกับว่า EMERGENCY !!**
1. **ระบายหนองและคลายการกดทับ (surgical drainage and decompression)**
2. **ผ่าตัดยึดตรึงกระดูกสันหลัง (surgical stabilization)**

> **ปวดหลัง + ไข้ + อาการทางระบบประสาท = ต้องคิดถึง spinal epidural abscess และส่ง MRI ทันที** ความล่าช้าแม้ไม่กี่ชั่วโมงอาจทำให้อัมพาตถาวร
""",
    ["ปวดหลัง + ไข้ + อาการทางระบบประสาท = spinal epidural abscess จนกว่าจะพิสูจน์เป็นอย่างอื่น",
     "S. aureus เป็นเชื้อหลัก · TB เป็นสาเหตุของ spondylodiscitis",
     "MRI spine with contrast คือการตรวจที่ต้องส่ง ไม่ใช่ X-ray หรือ CT",
     "การผ่าตัดระบายหนองและคลายกดทับเป็นภาวะฉุกเฉิน",
     "ยา 6–8 สัปดาห์ · vancomycin + cephalosporin รุ่น 3 · เพิ่มยาคลุม Pseudomonas ในกลุ่มเสี่ยง"],
    [
    mcq("NEU-CNS-MCQ-14",
        "A 58-year-old man with diabetes has 10 days of severe thoracic back pain and fever, and today developed leg weakness and urinary retention. Tenderness is elicited on spinal percussion. Which is the most appropriate immediate investigation and why?",
        ["Plain radiographs of the spine, because they detect early discitis",
         "MRI of the spine with contrast, because it demonstrates epidural abscess and cord compression",
         "Lumbar puncture, to analyse CSF for infection",
         "CT of the abdomen, to find the primary source first",
         "Bone scan, to localise the level before imaging"],
        1,
        """**ปวดหลัง + ไข้ + อาการทางระบบประสาท (ขาอ่อนแรง ปัสสาวะไม่ออก) = spinal epidural abscess จนกว่าจะพิสูจน์เป็นอย่างอื่น** และสไลด์ระบุการสืบค้นไว้ชัดว่าคือ **MRI of the spine with contrast**

**ลักษณะภาพที่คาดว่าจะพบ**
- **Spinal epidural abscess** — **T2 hyperintensity ที่มีแกนกลาง T1 hypointense และขอบ enhance ด้วย gadolinium**
- ถ้ามี **spondylodiscitis** ร่วม จะเห็น **T2 hyperintensity และ enhancement ที่หมอนรองกระดูก** ลามถึง endplate

**ทำไมต้องรีบ** — สไลด์กำกับการผ่าตัดไว้ว่า **EMERGENCY !!** คือ **ระบายหนองและคลายการกดทับ** ตามด้วย **ยึดตรึงกระดูกสันหลัง** ความล่าช้าทำให้เกิดอัมพาตถาวร

**ยาที่ควรเริ่ม** — ผู้ป่วยรายนี้ **เป็นเบาหวาน จึงจัดอยู่ในกลุ่มเสี่ยง Pseudomonas** ตามสไลด์ ควรใช้ **vancomycin + cefepime หรือ ceftazidime หรือ meropenem** นาน **6–8 สัปดาห์**

**ทำไมข้ออื่นผิด** — **ภาพรังสีธรรมดาปกติในระยะแรก** จึงตัดโรคไม่ได้ · **การเจาะหลังเป็นข้อห้ามสัมพัทธ์** เพราะเข็มอาจผ่านหนองและพาเชื้อเข้าช่องใต้เยื่อหุ้มสมอง · **CT ช่องท้องและ bone scan** ทำให้เสียเวลาโดยไม่ตอบคำถามเรื่องการกดทับไขสันหลัง""",
        "ปวดหลัง + ไข้ + neuro deficit = สั่ง MRI spine with contrast ทันที และอย่าเจาะหลัง",
        "Spinal epidural abscess",
        ["สไลด์ อ.พิมลพรรณ — Spondylodiscitis & Spinal epidural abscess"]),
    mcq("NEU-CNS-MCQ-15",
        "Which organism is the most common cause of pyogenic spondylodiscitis and spinal epidural abscess?",
        ["Escherichia coli", "Staphylococcus aureus", "Streptococcus pneumoniae", "Cryptococcus neoformans", "Neisseria meningitidis"],
        1,
        """สไลด์ระบุว่าการติดเชื้อกลุ่มนี้ **"Most often caused by pyogenic bacteria (Staphylococcus aureus)"**

**เชื้ออื่นที่สไลด์ระบุไว้**
- **Pseudomonas aeruginosa** — สำคัญในกลุ่มเสี่ยงที่ต้องปรับยา
- **Coagulase-negative staphylococci** — มักสัมพันธ์กับอุปกรณ์ที่ใส่ไว้
- **Bartonella henselae** (cat-scratch disease)
- **Mycobacterium tuberculosis** — เป็นสาเหตุของ **spondylodiscitis** ซึ่งในไทยต้องคิดถึงเสมอเมื่ออาการค่อยเป็นค่อยไปเป็นเดือน

**ทำไมสูตรยา empiric จึงเป็น vancomycin + cephalosporin รุ่นที่ 3** — vancomycin ครอบคลุม **MRSA** ซึ่งเป็นเชื้อหลัก ส่วน cephalosporin ครอบคลุมแบคทีเรียแกรมลบ

**และทำไมต้องเปลี่ยนเป็น cefepime, ceftazidime หรือ meropenem ในบางราย** — เพราะผู้ที่ **เป็นเบาหวาน เพิ่งได้ยาปฏิชีวนะ เคยใส่อุปกรณ์ที่กระดูกสันหลัง หรือนอนโรงพยาบาล** มีความเสี่ยงต่อ **Pseudomonas** สูงขึ้น

**เส้นทางการติดเชื้อสามทาง** — **hematogenous spread · direct inoculation จากหัตถการ · contiguous spread จากการติดเชื้อข้างเคียง**""",
        "S. aureus คือเชื้อหลัก → empiric ต้องมี vancomycin เสมอ · เบาหวานหรือเคยผ่าตัดหลังให้คลุม Pseudomonas ด้วย",
        "Microbiology of spinal infection",
        ["สไลด์ อ.พิมลพรรณ — Spondylodiscitis & Spinal epidural abscess"]),
    ])

MEQ = [{
 "id": "NEU-MEQ-03", "part": "MEQ", "lec": "15/10", "lecture": "CNS infection and CSF interpretation",
 "topic": "Acute bacterial meningitis — sequence, CSF interpretation and complications",
 "vignette": """ชายไทยอายุ 64 ปี ถูกนำส่งห้องฉุกเฉินด้วยไข้สูงและซึมลง 1 วัน
PI: 3 วันก่อนมาโรงพยาบาล มีไข้ ปวดศีรษะทั่วศีรษะรุนแรงขึ้นเรื่อย ๆ ปวดเมื่อยตามตัว 1 วันก่อนมาโรงพยาบาล ญาติสังเกตว่าซึมลง เรียกแล้วลืมตาช้า พูดสับสน เช้าวันนี้ปลุกตื่นยาก จึงนำส่งโรงพยาบาล ปฏิเสธอาการชัก ปฏิเสธอุบัติเหตุ
U/D: เบาหวานชนิดที่ 2 มา 12 ปี กินยา metformin และ glipizide · ไม่มีประวัติผ่าตัดสมองหรือกระดูกสันหลัง
PE: GA: ซึม ปลุกตื่นแต่หลับกลับทันที
V/S: BT 39.4 C, PR 116/min, RR 24/min, BP 104/62 mmHg, SpO2 95% room air
HEENT: ไม่มีผื่นจ้ำเลือดตามตัว
Neuro: E3V4M6 (GCS 13), neck stiffness positive, Kernig sign positive, pupils 3 mm ทั้งสองข้าง reactive, **ตรวจพบแขนขาซีกขวาอ่อนแรง grade IV**, DTR ปกติ, Babinski negative
Lab แรกรับ: capillary glucose 186 mg/dL, WBC 21,400 /mm3 (N 88%), Cr 1.2 mg/dL, Na 133 mEq/L""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัยที่น่าจะเป็นมากที่สุด และระบุว่าผู้ป่วยรายนี้มีข้อบ่งชี้ให้ทำ CT brain ก่อนเจาะหลังหรือไม่ พร้อมเหตุผล",
   "a": """**การวินิจฉัย** — **Acute bacterial meningitis**

เหตุผล: **ไข้สูง + ปวดศีรษะ + คอแข็ง (neck stiffness, Kernig positive)** ซึ่งเป็นสามอาการหลักที่สไลด์เน้น ร่วมกับ **ระดับการรู้ตัวเปลี่ยน** ซึ่งพบได้ราว **40%** ของผู้ป่วย และ **WBC 21,400 โดยมี neutrophil เด่น**

**มีข้อบ่งชี้ให้ทำ CT brain ก่อนเจาะหลัง — เข้าเกณฑ์ถึง 3 ข้อจาก 5 ข้อที่สไลด์ระบุ**

| ข้อบ่งชี้ตามสไลด์ | ผู้ป่วยรายนี้ |
|---|---|
| **อายุมากกว่า 60 ปี** | ✓ อายุ 64 ปี |
| **ภูมิคุ้มกันบกพร่อง** | (เบาหวานควบคุมไม่ดีถือเป็นปัจจัยเสี่ยง) |
| **ชักใกล้เวลาที่มาพบแพทย์** | ✗ ไม่มี |
| **ระดับการรู้ตัวเปลี่ยน** | ✓ GCS 13 ซึม |
| **Focal deficit จากการตรวจร่างกาย** | ✓ **อ่อนแรงซีกขวา grade IV** |

**เหตุผลเบื้องหลัง** — ทั้งสามข้อนี้เพิ่มความน่าจะเป็นของ **space-occupying lesion** เช่น ฝีในสมองหรือ subdural empyema ซึ่งถ้าเจาะหลังโดยไม่รู้ อาจทำให้เกิด **cerebral herniation**"""},
  {"q": "2. จงเรียงลำดับการรักษาและการสืบค้นที่ต้องทำใน 1 ชั่วโมงแรก ให้ครบและถูกลำดับ",
   "a": """**หลักการที่ต้องยึด** — สไลด์ระบุว่า **bacterial meningitis เป็น neurologic emergency** และ *"Empiric antibiotics should be initiated as soon as the diagnosis is considered"* — **DO NOT DELAY TREATMENT** การรอ CT ต้องไม่หน่วงการให้ยา

**ลำดับที่ถูกต้อง**

1. **ประเมินและดูแล ABC** — ผู้ป่วย GCS 13 ต้องเฝ้าระวังทางเดินหายใจ และมี BP 104/62 กับ PR 116 ซึ่งเข้าได้กับ sepsis ให้สารน้ำ
2. **เจาะ blood culture อย่างน้อย 2 ชุด ทันที** — สไลด์ระบุว่า **ขึ้นเชื้อได้ถึง 70%** และเป็นโอกาสเดียวที่จะได้เชื้อก่อนให้ยา
3. **ให้ dexamethasone ก่อนหรือพร้อมยาปฏิชีวนะโดสแรก** — ตามสไลด์ *"initiated before or with the first dose of antibiotics"* เพราะ steroid ต้องอยู่ในตัวก่อนที่ยาจะทำให้ผนังเซลล์แบคทีเรียแตกและปล่อยสารอักเสบ
4. **ให้ยาปฏิชีวนะ empiric ทันที** — ครอบคลุม **S. pneumoniae และ N. meningitidis** ซึ่งเป็นสองเชื้อที่สไลด์เน้น และ **เพิ่มการครอบคลุม Listeria เพราะอายุเกิน 50 ปี**
5. **ส่งตรวจอื่นควบคู่** — CBC, electrolytes, BUN/Cr, coagulogram, blood sugar (ต้องเจาะพร้อมกันเพื่อใช้คำนวณอัตราส่วน CSF/serum glucose)
6. **ทำ CT brain with contrast** — เพื่อตัด space-occupying lesion ตามข้อบ่งชี้ในข้อ 1
7. **เจาะหลังเมื่อ CT ปลอดภัย** — ส่ง **cell count และ differential, สี/ลักษณะ, opening และ closing pressure, protein และ sugar, Gram stain และ culture** และพิจารณา **PCR viral panel, CryptoAg, India ink** ตามบริบท

> **CSF ที่เจาะหลังได้ยาไปไม่กี่ชั่วโมงยังแปลผล cell count, protein, glucose ได้ และยังส่ง PCR ได้** การให้ยาก่อนจึงไม่ทำให้เสียการวินิจฉัย"""},
  {"q": "3. ผล CSF เป็นดังนี้ — opening pressure 30 cmH2O, ลักษณะขุ่น, WBC 3,100/mm3 (PMN 90%), protein 280 mg/dL, CSF glucose 22 mg/dL (serum glucose ขณะเจาะ 180 mg/dL) จงแปลผลและเทียบกับรูปแบบอื่นที่ต้องแยก",
   "a": """**แปลผล — เข้าได้กับ bacterial meningitis อย่างชัดเจน**

| ค่า | ผู้ป่วย | ค่าปกติ | แปลผล |
|---|---|---|---|
| Opening pressure | **30 cmH₂O** | 6–20 | **สูง** |
| ลักษณะ | **ขุ่น** | ใส | ผิดปกติ |
| WBC | **3,100** | 0–5 | **สูงมาก** อยู่ในช่วง 1,000–5,000 |
| Differential | **PMN 90%** | lymphocyte | **neutrophil เด่น** |
| Protein | **280 mg/dL** | 15–45 | **สูงมาก** |
| **CSF/serum glucose** | **22/180 = 0.12** | ≥ 0.6 | **ต่ำมาก** |

**ตารางเทียบกับรูปแบบอื่น**

| | **Bacterial (รายนี้)** | **Viral** | **TB** | **Cryptococcal** |
|---|---|---|---|---|
| ลักษณะ | **ขุ่น** | ใส | ใส อาจมี fibrin web | ใส |
| Opening pressure | สูง | ปกติ/สูงเล็กน้อย | สูง | **สูงมาก** |
| WBC | **1,000–5,000** | 10–500 | 50–500 | 20–200 |
| เซลล์เด่น | **PMN** | **Lymphocyte** | **Lymphocyte** | **Lymphocyte** |
| Protein | **สูงมาก** | ปกติ/สูงเล็กน้อย | **สูงมาก** | สูง |
| Glucose ratio | **ต่ำมาก** | **ปกติ** | ต่ำ | ต่ำ |
| ตรวจจำเพาะ | **G/S, C/S** | PCR viral panel | AFB, TB-PCR | **India ink, CryptoAg** |

**จุดที่ต้องระวังในการแปลผล**
- **ต้องใช้อัตราส่วน CSF/serum glucose ไม่ใช่ตัวเลข CSF เดี่ยว ๆ** — ผู้ป่วยรายนี้เป็นเบาหวาน น้ำตาลในเลือด 180 ถ้าดูแต่ CSF glucose 22 อาจประเมินความรุนแรงต่ำไป แต่เมื่อคิดเป็นอัตราส่วนได้ **0.12 ซึ่งต่ำมาก**
- **ระยะแรกของ bacterial meningitis อาจยังเป็น lymphocyte เด่นได้** และ **ระยะแรกของ viral meningitis อาจเป็น neutrophil เด่นได้** จึงต้องดูภาพรวมทุกค่า ไม่ใช่ชนิดเซลล์อย่างเดียว

**สิ่งที่ต้องทำต่อ** — ส่ง **Gram stain และ culture** เพื่อระบุเชื้อ และ **ปรับยาตามผลเพาะเชื้อ** เมื่อได้ผล · ถ้าเชื้อเป็น **S. pneumoniae** การให้ dexamethasone จะเป็นประโยชน์ตามที่สไลด์ระบุว่า **benefit only in streptococcal meningitis**"""},
  {"q": "4. จงอธิบายว่า focal deficit ที่ตรวจพบในผู้ป่วยรายนี้อาจเกิดจากอะไรได้บ้าง และจะติดตามภาวะแทรกซ้อนอะไร",
   "a": """**สาเหตุของอ่อนแรงซีกขวาในผู้ป่วย meningitis**

1. **ภาวะแทรกซ้อนทางหลอดเลือด (cerebrovascular complication)** — การอักเสบลามไปที่ผนังหลอดเลือดที่ทอดผ่านช่องใต้เยื่อหุ้มสมอง เกิด **vasculitis และ infarction** เป็นกลไกเดียวกับที่สไลด์ระบุเป็นภาวะแทรกซ้อนของ **TB meningitis**
2. **มีรอยโรคกินที่ร่วมด้วย** — **brain abscess หรือ subdural empyema** ซึ่งเป็นเหตุผลที่ต้องทำ CT ก่อนเจาะหลัง
3. **Postictal (Todd's) paralysis** — ถ้ามีการชักที่ไม่มีคนเห็น
4. **Cerebral venous sinus thrombosis** — ภาวะแทรกซ้อนที่พบได้และมักถูกมองข้าม
5. **สมองบวมและความดันในกะโหลกสูง** จนเกิดการเคลื่อนของเนื้อสมอง

**ภาวะแทรกซ้อนที่ต้องติดตาม**

| ภาวะแทรกซ้อน | การเฝ้าระวัง |
|---|---|
| **Hydrocephalus** | ระดับการรู้ตัวแย่ลง ปวดศีรษะมากขึ้น อาเจียน — ทำภาพซ้ำ |
| **Vasculitis / infarction** | ตรวจระบบประสาทซ้ำเป็นระยะ |
| **Cranial neuropathies** | โดยเฉพาะ **การสูญเสียการได้ยิน** ซึ่งพบบ่อยหลัง pneumococcal meningitis — ควรตรวจการได้ยินก่อนจำหน่าย |
| **ชัก** | เฝ้าระวังและให้ยากันชักเมื่อมีการชัก |
| **ความดันในกะโหลกสูง** | ระดับการรู้ตัว ขนาดรูม่านตา ความดันและชีพจร |
| **SIADH / hyponatremia** | ผู้ป่วยรายนี้ Na 133 อยู่แล้ว ต้องติดตามซ้ำ |
| **Septic shock และ DIC** | BP 104/62, PR 116 — ต้องเฝ้าระวังต่อเนื่อง |

> **สามภาวะแทรกซ้อนที่สไลด์ระบุไว้สำหรับ TB meningitis — vasculitis, hydrocephalus และ cranial neuropathies — ใช้เป็นกรอบเฝ้าระวังใน bacterial meningitis ได้เช่นกัน** เพราะกลไกร่วมกันคือ exudate และการอักเสบที่ฐานสมอง

**การติดตามภาพ** — ทำภาพซ้ำเมื่ออาการทางระบบประสาทแย่ลง ไข้ไม่ลงหลังได้ยาที่เหมาะสม หรือมีอาการใหม่"""}],
 "ref": ["สไลด์ อ.พิมลพรรณ เลี่ยนเครือ — CNS infection and CSF interpretation",
         "Continuum (Minneap Minn) 2021;27(4, Neuroinfectious Disease):818-835"],
 "nl": ["2.3.6"], "years": [], "_kind": "meq", "_set": "neuro"}]

OSCE = [{
 "id": "NEU-OSCE-03", "part": "OSCE/SAQ", "lec": "15/10", "lecture": "CNS infection and CSF interpretation",
 "topic": "SAQ – แปลผลน้ำไขสันหลังสี่ราย",
 "station": "SAQ (เขียนตอบ) 10 นาที",
 "instruction": """ผู้ป่วยสี่รายมาด้วยไข้และปวดศีรษะ ผลน้ำไขสันหลังเป็นดังนี้ (ค่าน้ำตาลในเลือดขณะเจาะอยู่ในวงเล็บ)

| ราย | ลักษณะ | OP (cmH₂O) | WBC/mm³ | เซลล์เด่น | Protein (mg/dL) | CSF glucose (serum) |
|---|---|---|---|---|---|---|
| **A** | ขุ่น | 26 | 2,800 | PMN 91% | 260 | 20 (120) |
| **B** | ใส | 14 | 160 | Lymphocyte 90% | 48 | 60 (94) |
| **C** | ใส | 22 | 280 | Lymphocyte 85% | 210 | 30 (105) |
| **D** | ใส | 40 | 40 | Lymphocyte 80% | 90 | 32 (100) |

1.1 จงระบุการวินิจฉัยที่น่าจะเป็นของแต่ละราย พร้อมเหตุผลสั้น ๆ (8 คะแนน)
1.2 จงระบุการตรวจจำเพาะเพิ่มเติมที่ควรส่งในแต่ละราย (4 คะแนน)
1.3 รายใดที่ต้องให้การรักษาเร่งด่วนที่สุด และให้ยาอะไรก่อนอะไร (4 คะแนน)
1.4 ผู้ป่วยรายหนึ่งมีอ่อนแรงซีกซ้ายร่วมด้วย จะเปลี่ยนแผนการตรวจอย่างไร (4 คะแนน)""",
 "answer": """**1.1 การวินิจฉัย (8 คะแนน — รายละ 2 คะแนน)**

**ราย A — Bacterial meningitis**
น้ำไขสันหลัง**ขุ่น**, **WBC 2,800 โดย PMN เด่น 91%**, **protein สูงมาก 260**, **glucose ratio 20/120 = 0.17 ซึ่งต่ำมาก** — ครบทุกข้อของรูปแบบแบคทีเรีย

**ราย B — Viral meningitis**
**ใส**, **WBC 160 lymphocyte เด่น** (อยู่ในช่วง mononuclear pleocytosis ที่ได้ถึง 200), **protein 48 ซึ่งปกติหรือสูงเล็กน้อย**, **glucose ratio 60/94 = 0.64 ซึ่งปกติ** — ตรงกับ typical viral CSF profile ที่สไลด์ระบุ

**ราย C — Tuberculous meningitis**
**lymphocyte เด่น**, **protein สูงมาก 210**, **glucose ratio 30/105 = 0.29 ซึ่งต่ำ**, opening pressure สูง — รูปแบบ lymphocyte + โปรตีนสูงมาก + น้ำตาลต่ำ คือลายเซ็นของวัณโรค (แยกจาก viral ด้วยน้ำตาลที่ต่ำและโปรตีนที่สูงมาก)

**ราย D — Cryptococcal meningitis**
**opening pressure สูงมาก 40 cmH₂O** ซึ่งเป็นลักษณะเด่นที่สุด, **เซลล์น้อยเพียง 40 แต่เป็น lymphocyte**, **glucose ratio 32/100 = 0.32 ซึ่งต่ำ** — เซลล์น้อยแต่ความดันสูงมากในผู้ที่มักมีภูมิคุ้มกันบกพร่อง

**1.2 การตรวจจำเพาะเพิ่มเติม (4 คะแนน — รายละ 1 คะแนน)**

| ราย | การตรวจ |
|---|---|
| **A** | **Gram stain และ culture** + **blood culture** (ขึ้นเชื้อได้ถึง 70%) |
| **B** | **PCR viral panel** (enterovirus, HSV, VZV) |
| **C** | **AFB smear, TB-PCR (Xpert MTB/RIF), mycobacterial culture** · พิจารณาภาพสมองหา basal enhancement และ hydrocephalus |
| **D** | **India ink stain และ cryptococcal antigen (CryptoAg)** · ตรวจ **anti-HIV** |

**1.3 รายที่เร่งด่วนที่สุดและลำดับยา (4 คะแนน)**

**ราย A เร่งด่วนที่สุด** — **bacterial meningitis เป็น neurologic emergency** สไลด์ระบุว่า *"Empiric antibiotics should be initiated as soon as the diagnosis of bacterial meningitis is considered"* — **DO NOT DELAY TREATMENT**

**ลำดับ**
1. **เจาะ blood culture**
2. **ให้ dexamethasone ก่อนหรือพร้อมยาปฏิชีวนะโดสแรก** — ให้ช้ากว่านั้นไม่มีประโยชน์ และ **แสดงประโยชน์เฉพาะใน streptococcal meningitis**
3. **ให้ยาปฏิชีวนะ empiric ครอบคลุม S. pneumoniae และ N. meningitidis** (เพิ่มการครอบคลุม Listeria ในผู้สูงอายุ ผู้ตั้งครรภ์ และผู้ที่ภูมิคุ้มกันบกพร่อง)
4. ปรับยาตามผลเพาะเชื้อ

*(หมายเหตุ: ราย D ก็เร่งด่วนในแง่ของ **การระบายความดันในกะโหลก** ซึ่งมีผลต่อการรอดชีวิต และต้องเริ่ม induction ด้วย amphotericin B + fluconazole 800 mg/d 2 สัปดาห์)*

**1.4 เมื่อมีอ่อนแรงซีกซ้ายร่วมด้วย (4 คะแนน)**

- **ต้องทำ CT brain (with contrast) ก่อนเจาะหลัง** เพราะ **focal deficit เป็นหนึ่งในห้าข้อบ่งชี้ที่สไลด์ระบุ** ร่วมกับ อายุ > 60 ปี, ภูมิคุ้มกันบกพร่อง, การชักใกล้เวลาที่มา และระดับการรู้ตัวเปลี่ยน
- **เหตุผล** — เพื่อตัด **space-occupying lesion** (brain abscess, subdural empyema, เนื้องอก) ซึ่งการเจาะหลังอาจทำให้เกิด **cerebral herniation**
- **แต่ห้ามให้การรอภาพหน่วงการรักษา** — ให้ **เจาะ hemoculture → dexamethasone → ยาปฏิชีวนะ empiric** ไปก่อน แล้วจึงทำ CT และเจาะหลังภายหลัง
- **ถ้าภาพพบ ring-enhancing lesion** ให้คิดถึง **brain abscess** ซึ่ง **ห้ามเจาะหลัง** (สไลด์ระบุ *"CSF analysis is NOT recommended"*) และเปลี่ยนไปเก็บเชื้อด้วย **blood culture และ pus aspiration** แทน
- พิจารณา **MRI with gadolinium** เพื่อดู **restricted diffusion ที่ใจกลางรอยโรค** ซึ่งช่วยแยกฝีออกจากเนื้องอก""",
 "ref": ["สไลด์ อ.พิมลพรรณ — CSF analysis / Meningitis / Brain abscess",
         "Continuum (Minneap Minn) 2021;27(4):818-835"],
 "nl": ["2.3.6"], "years": [], "_kind": "meq", "_set": "neuro"}]

LECTURE = {
 "lec": "15/10",
 "title": "CNS infection และการแปลผลน้ำไขสันหลัง",
 "subtitle": "สามเส้นทางเข้าสู่ CNS · meningitis และเมื่อไรต้อง CT ก่อนเจาะหลัง · ตาราง CSF สี่กลุ่ม · dexamethasone · TB meningitis · encephalitis (HSV กับ JE) · brain abscess · spondylodiscitis และ spinal epidural abscess",
 "objectives": [
   "อธิบายพยาธิกำเนิดสี่ขั้นและสามเส้นทางที่เชื้อเข้าสู่ระบบประสาทกลางได้",
   "ระบุข้อบ่งชี้ห้าข้อที่ต้องทำ CT brain ก่อนเจาะหลัง และจัดลำดับการรักษาโดยไม่หน่วงยาปฏิชีวนะ",
   "แปลผลน้ำไขสันหลังแยก bacterial, viral, tuberculous และ cryptococcal ได้ด้วยอัตราส่วน CSF/serum glucose",
   "ระบุเวลาที่ต้องให้ dexamethasone และเชื้อที่ได้ประโยชน์จริง",
   "จดจำสูตรและระยะเวลาการรักษา TB meningitis รวมถึงสามภาวะแทรกซ้อน",
   "แยก encephalitis จาก meningitis และใช้ภาพแยก HSV จาก JE พร้อมเริ่ม acyclovir ทันทีเมื่อสงสัย",
   "ระบุระยะของ brain abscess ที่ใช้ยาอย่างเดียวได้ และรู้ว่าห้ามเจาะหลัง",
   "วินิจฉัย spinal epidural abscess จากสามอาการหลัก และส่ง MRI spine with contrast เป็นภาวะฉุกเฉิน"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

path = os.path.join(BUILD, "data", "neuro.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LECTURE["lec"]]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "neuro": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | items %d | meq %d | osce %d" % (len(S), sum(len(s["items"]) for s in S), len(MEQ), len(OSCE)))
print("neuro.json มี %d คาบ · %d bytes" % (len(data), os.path.getsize(path)))
