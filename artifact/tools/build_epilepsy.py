#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""สร้างคาบ Epilepsy (23 ก.ย. 2569 · อ.พิมลพรรณ เลี่ยนเครือ) แล้ว append เข้า data/neuro.json"""
import json, os, sys

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
SLIDE = "สไลด์ อ.พิมลพรรณ — Epilepsy: Understanding and Navigating a Complex Neurological Condition"
NLN = ["2.3.6"]

S = []   # sections
def sec(sid, title, summary, minutes, md, pearls, items, nl=None):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})

def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, src="", nl=None):
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": src,
            "ref": ref, "nl": nl or NLN}

# ─────────────────────────────────────────────────────────────── 1
sec("neuro-ep-01", "ชัก ≠ โรคลมชัก — เริ่มที่นิยามให้ถูกก่อน",
    "seizure เป็นเหตุการณ์ · epilepsy เป็นโรค · เกณฑ์ ILAE สามข้อ", 8,
"""ความผิดพลาดที่พบบ่อยที่สุดในห้องฉุกเฉินคือ **เห็นคนชักหนึ่งครั้งแล้วเรียกว่าเป็นโรคลมชักทันที** ทั้งที่สองคำนี้อยู่คนละระดับกัน

**Seizure (อาการชัก)** = เหตุการณ์ชั่วคราวที่มีอาการและ/หรืออาการแสดงจาก **การทำงานไฟฟ้าในสมองที่มากเกินและพร้อมเพรียงกันผิดปกติ (abnormal excessive hypersynchronous activity)** ผลคือการเปลี่ยนแปลงหน้าที่สมองสั้น ๆ ซึ่งอาจออกมาเป็นชักเกร็งกระตุก ระดับการรู้ตัวเปลี่ยน ความรู้สึกผิดปกติ หรืออาการด้านความคิดและภาษา

**Epilepsy (โรคลมชัก)** = **โรคของสมอง** ที่ต้องเข้าเกณฑ์ข้อใดข้อหนึ่งต่อไปนี้

| ข้อ | เกณฑ์ |
|---|---|
| **1** | ชักแบบ **unprovoked (หรือ reflex) อย่างน้อย 2 ครั้ง ห่างกันเกิน 24 ชั่วโมง** |
| **2** | ชัก unprovoked **1 ครั้ง** ร่วมกับ **โอกาสชักซ้ำใน 10 ปีข้างหน้า ≥ 60%** (เท่ากับความเสี่ยงของคนที่ชักไปแล้ว 2 ครั้ง) |
| **3** | วินิจฉัยได้ว่าเป็น **epilepsy syndrome** |

> **คนทั่วโลกราว 10% เคยชักอย่างน้อยหนึ่งครั้งในชีวิต แต่ไม่ได้เป็นโรคลมชักทุกคน** — คำว่า *unprovoked* จึงสำคัญมาก ชักจากน้ำตาลต่ำ เกลือแร่ผิดปกติ ถอนสุรา หรือไข้สูงในเด็ก คือ **provoked (acute symptomatic) seizure** ไม่นับเข้าเกณฑ์ข้อ 1

### เกณฑ์ข้อ 2 ใช้จริงอย่างไร
ข้อนี้คือเหตุผลที่ผู้ป่วยบางคน **ชักครั้งเดียวก็วินิจฉัยและเริ่มยาได้เลย** เมื่อมีหลักฐานว่าความเสี่ยงชักซ้ำสูง ≥ 60% เช่น
- **MRI พบรอยโรคโครงสร้าง** ที่อธิบายการชักได้ (เนื้องอก, รอยแผลเป็นจากอุบัติเหตุ, hippocampal sclerosis)
- **EEG พบ epileptiform discharge** ชัดเจน
- ชักครั้งแรกเกิด **ขณะนอนหลับ**
- มีประวัติ **stroke หรือ CNS infection** มาก่อนแล้วมาชักภายหลัง (remote symptomatic)

### ระบาดวิทยาที่ออกสอบ
- ผู้ป่วยโรคลมชักทั่วโลก **ราว 50 ล้านคน** — เป็นโรคทางระบบประสาทที่พบบ่อยที่สุดกลุ่มหนึ่ง
- **เกือบ 80% อยู่ในประเทศรายได้ต่ำและปานกลาง** ซึ่งเข้าถึงยาได้น้อย
- **ความเสี่ยงเสียชีวิตก่อนวัยอันควรสูงกว่าคนทั่วไปถึง 3 เท่า**
- เกิดได้ทุกช่วงอายุ ตั้งแต่ทารกจนถึงผู้สูงอายุ

### ที่อาจารย์เน้นในสไลด์
- สไลด์เปิดคาบด้วยประโยคว่า **"Not everyone who has a seizure has epilepsy"** แล้วตามด้วยตัวเลข 10% ทันที — เป็นการวางกรอบทั้งคาบว่าโจทย์แรกคือ *แยกเหตุการณ์ออกจากโรค*
- ย้ำว่าเกณฑ์ ILAE มี **3 ข้อ ไม่ใช่ข้อเดียว** และข้อ 2 กับข้อ 3 คือเหตุผลที่ไม่ต้องรอให้ชักครบสองครั้งเสมอไป
""",
    ["ชัก 1 ครั้ง ≠ โรคลมชัก — ต้องเข้าเกณฑ์ ILAE ข้อใดข้อหนึ่งใน 3 ข้อ",
     "เกณฑ์ข้อ 2 (ชัก 1 ครั้ง + ความเสี่ยงซ้ำ ≥ 60%) ทำให้เริ่มยาได้ตั้งแต่ครั้งแรกเมื่อมี MRI หรือ EEG ผิดปกติ",
     "ชักจากน้ำตาลต่ำ เกลือแร่ผิดปกติ ถอนสุรา = provoked seizure ไม่นับเข้าเกณฑ์",
     "ผู้ป่วยโรคลมชักเสี่ยงตายก่อนวัยอันควรสูงกว่าคนทั่วไป 3 เท่า"],
    [
    mcq("NEU-EP-MCQ-01",
        "A 24-year-old man is brought to the emergency department after a witnessed generalized tonic-clonic seizure lasting 2 minutes. He has never had a seizure before. He denies alcohol or drug use. Capillary glucose 98 mg/dL, serum sodium 139 mEq/L, calcium normal. MRI of the brain shows a left mesial temporal lesion consistent with hippocampal sclerosis, and EEG shows left temporal epileptiform discharges. Which of the following is the most appropriate conclusion?",
        ["He has epilepsy and antiseizure medication may be started now",
         "He has a provoked seizure and requires no further follow-up",
         "He cannot be diagnosed with epilepsy until a second unprovoked seizure occurs",
         "He should be observed for 10 years before any diagnosis is made",
         "The diagnosis requires at least three unprovoked seizures"],
        0,
        """**เข้าเกณฑ์ ILAE ข้อ 2 — ชัก unprovoked 1 ครั้ง + ความเสี่ยงชักซ้ำ ≥ 60%**

ผู้ป่วยรายนี้มีทั้ง **รอยโรคโครงสร้างบน MRI (hippocampal sclerosis)** และ **epileptiform discharge บน EEG** ที่ตำแหน่งเดียวกัน สองอย่างนี้ทำให้ความเสี่ยงชักซ้ำภายใน 10 ปีสูงเทียบเท่าคนที่ชักไปแล้ว 2 ครั้ง จึง **วินิจฉัยโรคลมชักได้ตั้งแต่ครั้งแรกและเริ่มยาได้**

| เกณฑ์ ILAE | เนื้อหา | เคสนี้ |
|---|---|---|
| ข้อ 1 | unprovoked ≥ 2 ครั้ง ห่าง > 24 ชม. | ไม่เข้า (ชักครั้งเดียว) |
| **ข้อ 2** | **unprovoked 1 ครั้ง + เสี่ยงซ้ำ ≥ 60%** | **เข้า** ✓ |
| ข้อ 3 | เป็น epilepsy syndrome | ไม่ได้ระบุ |

**ทำไมข้ออื่นผิด**
- **"provoked seizure"** ผิด เพราะน้ำตาล โซเดียม แคลเซียมปกติหมด ไม่มีตัวกระตุ้นเฉียบพลัน — และรอยโรคเก่าบน MRI คือ *remote symptomatic* ซึ่งนับเป็น unprovoked
- **"ต้องรอครั้งที่สอง"** คือการจำเกณฑ์แค่ข้อ 1 ซึ่งเป็นกับดักที่พบบ่อยที่สุดของคำถามแนวนี้
- **"ต้องชัก 3 ครั้ง"** ไม่มีในนิยามใด ๆ""",
        "MRI มีรอยโรค + EEG มี epileptiform discharge หลังชักครั้งแรก = วินิจฉัยโรคลมชักได้เลยตามเกณฑ์ข้อ 2 ไม่ต้องรอครั้งที่สอง",
        "ILAE definition of epilepsy",
        ["ILAE Official Report: A practical clinical definition of epilepsy. Epilepsia 2014", "สไลด์ อ.พิมลพรรณ บท 1"]),
    mcq("NEU-EP-MCQ-02",
        "A 55-year-old man with type 2 diabetes on glipizide is found unresponsive with generalized convulsions. Capillary glucose is 28 mg/dL. He recovers fully after intravenous dextrose and has no further events over 6 months. Which of the following best classifies this event?",
        ["Acute symptomatic (provoked) seizure — this is not epilepsy",
         "Epilepsy, because a generalized tonic-clonic seizure occurred",
         "Epilepsy syndrome of adulthood",
         "Reflex epilepsy triggered by metabolic stimuli",
         "Developmental and epileptic encephalopathy"],
        0,
        """**น้ำตาลในเลือด 28 mg/dL คือสาเหตุเฉียบพลันที่ชัดเจน → acute symptomatic (provoked) seizure**

นิยามของโรคลมชักต้องการ **unprovoked seizure** การชักที่เกิดในช่วงเวลาใกล้ชิดกับความผิดปกติเฉียบพลันของระบบ (metabolic, toxic, structural เฉียบพลัน) **ไม่นับ**

**สาเหตุ provoked ที่ต้องคัดออกก่อนเสมอ**
- **Hypoglycemia** (รายนี้) · hyponatremia · hypocalcemia · hypomagnesemia
- **Alcohol withdrawal** และการถอนยากลุ่ม benzodiazepine
- **ยา/สารพิษ** เช่น tramadol, theophylline, isoniazid เกินขนาด
- **ภาวะเฉียบพลันของสมอง** — stroke ระยะเฉียบพลัน, CNS infection, traumatic brain injury ภายใน 7 วัน
- **Eclampsia**, uremia, hepatic encephalopathy

**ทำไมข้ออื่นผิด** — ชนิดของการชัก (tonic-clonic) ไม่ได้บอกว่าเป็นโรคลมชักหรือไม่ · **reflex epilepsy** หมายถึงชักที่ถูกกระตุ้นซ้ำ ๆ ด้วยสิ่งเร้าเฉพาะ เช่น แสงกะพริบ ไม่ใช่ความผิดปกติทางเมตาบอลิก · **DEE** เป็นกลุ่มโรครุนแรงที่เริ่มในวัยทารกและเด็กเล็ก""",
        "แก้เหตุแล้วไม่ชักอีก = provoked seizure ไม่ใช่โรคลมชัก — เจาะน้ำตาลปลายนิ้วทุกรายที่มาด้วยชัก",
        "Provoked vs unprovoked seizure",
        ["สไลด์ อ.พิมลพรรณ บท 1", "Harrison 21st ed., Seizures and Epilepsy"],
        nl=["2.3.6", "2.2.17"]),
    ])

# ─────────────────────────────────────────────────────────────── 2
sec("neuro-ep-02", "แยกจากภาวะที่เหมือนชัก (seizure mimics)",
    "convulsive syncope · PNES · movement disorder · TIA/TGA · sleep-related", 9,
"""สไลด์ตั้งคำถามไว้ตรง ๆ ว่า **"Seizure mimic?"** ก่อนจะเข้าเรื่องการจำแนก เพราะการวินิจฉัยผิดตั้งแต่ต้นทำให้ผู้ป่วยได้ยากันชักโดยไม่จำเป็นเป็นปี

### รายชื่อที่ต้องแยกให้ออก
- **Convulsive syncope** — เป็นลมแล้วมีกระตุก
- **Paroxysmal movement disorders**
- **TIA / TGA (transient global amnesia)**
- **Sleep-related events** — parasomnia, REM sleep behaviour disorder, cataplexy
- **Psychogenic non-epileptic spells (PNES)**
- **Migraine** (โดยเฉพาะ migraine with aura)

### ตัวช่วยแยกที่ใช้ได้จริงข้างเตียง

| | **Epileptic seizure** | **Convulsive syncope** | **PNES** |
|---|---|---|---|
| ท่าทางก่อนเกิด | ทำอะไรอยู่ก็เกิดได้ รวมทั้งขณะนอน | มักยืน/ลุกเร็ว ร้อน เจ็บ เห็นเลือด | มักมีคนอยู่ด้วย |
| อาการนำ | aura เฉพาะแบบ ซ้ำเดิมทุกครั้ง | หน้ามืด ตาลาย หูอื้อ เหงื่อแตก คลื่นไส้ | หลากหลาย ไม่คงที่ |
| ระยะเวลา | **1–2 นาที** | **กระตุกสั้น ๆ < 15 วินาที** | มัก **> 2–5 นาที** บางครั้งเป็นสิบนาที |
| ลักษณะการกระตุก | เกร็งก่อนแล้วกระตุกเป็นจังหวะ **ช้าลงเรื่อย ๆ** | กระตุกไม่เป็นจังหวะ จำนวนครั้งน้อย | **ขยับไม่เข้าจังหวะ เป็นพัก ๆ หยุดแล้วเริ่มใหม่**, ส่ายหัวซ้ายขวา, โก่งตัว (opisthotonus), ขยับเชิงกราน |
| ตาขณะชัก | **ลืมตา ค้าง เบือนไปข้างเดียว** | ลืมตา | **หลับตาแน่น ต้านเมื่อพยายามเปิด** |
| กัดลิ้น | **ด้านข้างลิ้น** | ไม่ค่อยมี หรือปลายลิ้น | ปลายลิ้น หรือไม่มี |
| ปัสสาวะราด | พบได้ | พบได้ | พบได้ (แยกไม่ได้ด้วยข้อนี้) |
| หลังเหตุการณ์ | **สับสนหลายนาทีถึงชั่วโมง (post-ictal)** | **รู้ตัวเร็วภายในวินาที** | รู้ตัวเร็ว บางรายร้องไห้ |
| Lactate / CK | **สูงขึ้นหลังชัก** | ไม่สูง | **ไม่สูง** |

### จุดที่คนพลาดบ่อย
- **"มีกระตุกแปลว่าชัก" ผิด** — convulsive syncope พบบ่อยมากและกระตุกได้จริง จุดแยกคือ *ระยะเวลาสั้น* และ *ไม่มี post-ictal confusion*
- **ปัสสาวะราดไม่ได้ช่วยแยกอะไรเลย** — เป็นตัวลวงคลาสสิกในข้อสอบ
- **PNES ไม่ใช่การแกล้ง** — เป็นความผิดปกติทางจิตเวช (functional neurological disorder) ที่ต้องส่งต่อจิตแพทย์ ไม่ใช่ตำหนิผู้ป่วย และ **การวินิจฉัยยืนยันต้องใช้ video-EEG**
- ผู้ป่วย PNES จำนวนหนึ่ง **มีทั้ง PNES และโรคลมชักจริงร่วมกัน**
""",
    ["ระยะเวลา + post-ictal confusion คือสองตัวแยกที่ดีที่สุดระหว่างชักจริงกับเป็นลม",
     "หลับตาแน่นและต้านการเปิดตา = PNES · ลืมตาค้าง = ชักจริง",
     "ปัสสาวะราดแยกอะไรไม่ได้เลย อย่าใช้เป็นเหตุผล",
     "PNES ยืนยันด้วย video-EEG และเป็นโรคทางจิตเวชที่ต้องรักษา ไม่ใช่การแกล้ง"],
    [
    mcq("NEU-EP-MCQ-03",
        "A 19-year-old woman has recurrent episodes of bilateral limb shaking lasting 8–15 minutes. During episodes her eyes are tightly closed and resist passive opening, the movements are irregular and wax and wane, and she sometimes cries afterwards. She is fully oriented immediately after each episode. Serum lactate measured 10 minutes after an episode is normal. Which of the following is the most likely diagnosis?",
        ["Generalized tonic-clonic seizure",
         "Convulsive syncope",
         "Psychogenic non-epileptic spells",
         "Juvenile myoclonic epilepsy",
         "Frontal lobe epilepsy"],
        2,
        """**ลักษณะที่ชี้ไป PNES ครบทุกข้อ**

| เบาะแส | ความหมาย |
|---|---|
| **นาน 8–15 นาที** | ชักจริงแบบ tonic-clonic มัก **1–2 นาที** |
| **หลับตาแน่นและต้านการเปิด** | ชักจริง **ลืมตาค้าง** — ข้อนี้มี specificity สูงมาก |
| **ขยับไม่เป็นจังหวะ เป็นพัก ๆ หยุดแล้วเริ่มใหม่** | ชักจริงกระตุกเป็นจังหวะและ**ค่อย ๆ ช้าลง** |
| **รู้ตัวทันทีหลังหยุด** | ชัก GTC จริงต้องมี **post-ictal confusion** |
| **lactate ไม่สูง** | หลัง GTC จริง lactate และ CK มักสูงขึ้น |

**การจัดการ** — ยืนยันด้วย **video-EEG** (มาตรฐาน) แล้ว **ส่งต่อจิตแพทย์/นักจิตวิทยา** อธิบายผู้ป่วยด้วยท่าทีที่ไม่ตำหนิ และ **ค่อย ๆ ลดยากันชักที่ไม่จำเป็นออก** เพราะไม่ได้ผลและมีผลข้างเคียง

**ทำไมข้ออื่นผิด** — **GTC** ต้องมี post-ictal confusion · **convulsive syncope** กระตุกสั้นมาก (< 15 วินาที) และมีอาการนำแบบหน้ามืด · **JME** เป็น myoclonic jerk สั้น ๆ ตอนตื่นนอน ไม่ใช่เหตุการณ์ยาวสิบนาที · **frontal lobe epilepsy** แม้จะมีท่าทางแปลกและ EEG มักปกติ แต่เหตุการณ์สั้น (< 1 นาที) เกิดถี่ และมักเกิดขณะหลับ""",
        "หลับตาแน่น + นานเกิน 5 นาที + รู้ตัวทันที + lactate ปกติ = PNES จนกว่าจะพิสูจน์เป็นอย่างอื่น",
        "Psychogenic non-epileptic spells",
        ["สไลด์ อ.พิมลพรรณ — Seizure mimic", "Continuum (Minneap Minn) 2025;31(1):Epilepsy"]),
    mcq("NEU-EP-MCQ-04",
        "A 20-year-old man collapsed while standing in a hot queue. Bystanders report he became pale and sweaty, then fell and had about 10 seconds of irregular limb jerking. He was fully alert within 20 seconds of the event. Which feature most strongly favours syncope over an epileptic seizure?",
        ["Urinary incontinence during the event",
         "Immediate return to full alertness without post-ictal confusion",
         "The presence of limb jerking",
         "Occurrence while standing",
         "A duration longer than 5 seconds"],
        1,
        """**การไม่มี post-ictal confusion คือตัวแยกที่มีน้ำหนักที่สุด**

หลังชัก **generalized tonic-clonic** สมองต้องใช้เวลาฟื้น ผู้ป่วยจึง **สับสน ง่วงซึม พูดไม่รู้เรื่อง นานหลายนาทีถึงเป็นชั่วโมง** ตรงข้ามกับเป็นลม ซึ่งเมื่อเลือดกลับไปเลี้ยงสมอง **รู้ตัวเต็มที่ภายในไม่กี่วินาที**

**ทำไมข้ออื่นผิด**
- **ปัสสาวะราด** เกิดได้ทั้งสองภาวะ — ไม่มีค่าในการแยก และเป็นตัวลวงที่ออกสอบบ่อยที่สุด
- **การกระตุก** เกิดได้ในเป็นลม เรียก **convulsive syncope** พบได้ถึงราวครึ่งหนึ่งของการเป็นลมที่มีคนเห็น กลไกคือสมองขาดเลือดชั่วคราวจนเกิด myoclonic jerk ไม่ใช่ไฟฟ้าสมองผิดปกติ
- **การยืน** เป็นตัวกระตุ้นที่เข้ากับ vasovagal syncope จริง แต่เป็นหลักฐานที่อ่อนกว่า เพราะชักก็เกิดขณะยืนได้
- **ระยะเวลา > 5 วินาที** ไม่ได้บอกอะไร — จุดตัดที่มีประโยชน์คือ **กระตุกสั้นกว่า 15 วินาที** เทียบกับชักจริงที่ยาว 1–2 นาที""",
        "รู้ตัวทันที = เป็นลม · สับสนหลังเหตุการณ์ = ชักจริง — และปัสสาวะราดใช้แยกไม่ได้",
        "Convulsive syncope vs seizure",
        ["สไลด์ อ.พิมลพรรณ — Differential diagnosis", "Harrison 21st ed., Syncope"]),
    ])

# ─────────────────────────────────────────────────────────────── 3
sec("neuro-ep-03", "การจำแนกอาการชัก — focal, generalized, unknown",
    "จุดเริ่มต้นของไฟฟ้า + ระดับการรู้ตัว + semiology", 8,
"""ILAE จำแนกโดยเริ่มจากคำถามเดียวคือ **ไฟฟ้าเริ่มจากที่ไหน**

| Seizure onset | ความหมาย |
|---|---|
| **Focal onset** | เริ่มจากเครือข่ายในซีกเดียว |
| **Generalized onset** | เริ่มจากสองซีกพร้อมกัน |
| **Unknown onset** | ไม่มีข้อมูลพอจะระบุจุดเริ่ม |

สำหรับ **focal onset** ต้องระบุต่ออีกชั้นว่า **รู้ตัวหรือไม่**
- **Focal aware** (เดิมเรียก simple partial)
- **Focal impaired awareness** (เดิมเรียก complex partial)

แล้วจึงระบุ **อาการเด่นตอนเริ่ม (semiology)** ซึ่งสไลด์ไล่ไว้ 7 กลุ่ม

| กลุ่ม semiology | ตัวอย่าง |
|---|---|
| **Elementary motor** | กระตุกเป็นจังหวะ เกร็ง ตัวอ่อน myoclonus |
| **Complex motor** | automatism (เคี้ยวปาก คลำเสื้อ), hyperkinetic, ท่าทางซับซ้อน |
| **Sensory** | ชา เสียว เห็นแสง ได้ยินเสียง กลิ่นหรือรสผิดปกติ |
| **Cognitive and language** | déjà vu, jamais vu, พูดไม่ออก, ความคิดถูกบังคับ |
| **Autonomic** | ใจสั่น ขนลุก หน้าแดง จุกแน่นลิ้นปี่ลอยขึ้น |
| **Affective** | กลัวอย่างฉับพลัน วิตกกังวล หัวเราะ (gelastic) |
| **Indescribable aura** | รู้สึกแปลก ๆ บอกไม่ถูก |

> **Aura คือ focal aware seizure** ไม่ใช่ "สัญญาณเตือนก่อนชัก" ที่อยู่นอกการชัก — มันคือส่วนแรกของการชักที่ผู้ป่วยยังรู้ตัวอยู่ และเป็นข้อมูลชั้นดีสำหรับระบุตำแหน่งรอยโรค

### สิ่งที่ต้องถามให้ได้เสมอเมื่อซักประวัติคนชัก
1. **ก่อนชักรู้สึกอะไรไหม** และรู้สึกแบบเดียวกันทุกครั้งหรือไม่ (aura → focal onset)
2. **ตอนชักรู้ตัวไหม** ถามทั้งผู้ป่วยและคนเห็นเหตุการณ์
3. **เริ่มที่ส่วนไหนของร่างกายก่อน** และลามอย่างไร (Jacksonian march)
4. **หน้าหรือตาเบือนไปทางไหน** (version → ชี้ไปที่ซีกตรงข้าม)
5. **นานเท่าไร** และ **หลังชักสับสนนานแค่ไหน**
6. ชัก **ขณะหลับหรือตื่น**
""",
    ["คำถามแรกของการจำแนกคือ ไฟฟ้าเริ่มจากซีกเดียวหรือสองซีก",
     "focal onset ต้องระบุต่อว่า aware หรือ impaired awareness",
     "Aura = focal aware seizure ไม่ใช่สิ่งที่เกิดก่อนชัก — ใช้ระบุตำแหน่งรอยโรคได้",
     "ประวัติจากคนเห็นเหตุการณ์มีค่ามากกว่าประวัติจากผู้ป่วยเองเสมอ"],
    [
    mcq("NEU-EP-MCQ-05",
        "A 32-year-old woman describes episodes beginning with a rising sensation in the epigastrium and an intense feeling of familiarity, after which bystanders note she stares blankly and performs repetitive lip-smacking for about 60 seconds. She does not recall this part. How should this seizure be classified?",
        ["Focal onset with impaired awareness",
         "Generalized onset absence seizure",
         "Focal aware seizure only",
         "Generalized onset tonic-clonic seizure",
         "Unknown onset seizure"],
        0,
        """**เริ่มเป็น focal aware (epigastric rising + déjà vu) แล้วดำเนินต่อจนเสียการรู้ตัวพร้อม automatism → focal onset with impaired awareness**

การจำแนกใช้ **ระดับการรู้ตัวสูงสุดที่เสียไประหว่างการชัก** ดังนั้นแม้ช่วงแรกยังรู้ตัว เมื่อต่อมารู้ตัวลดลง ให้จัดเป็น **impaired awareness**

**อาการชุดนี้เป็นแบบฉบับของ mesial temporal lobe epilepsy**
- **Epigastric rising sensation** — autonomic aura ที่พบบ่อยที่สุดของ temporal lobe
- **Déjà vu / jamais vu** — cognitive aura
- **Oroalimentary automatism** (เคี้ยว ดูดปาก) และ manual automatism (คลำเสื้อ)
- ระยะเวลา **30 วินาที – 2 นาที** ตามด้วย post-ictal confusion

**ทำไมข้ออื่นผิด**
- **Absence seizure** นานเพียงไม่กี่วินาที **ไม่มี aura ไม่มี post-ictal confusion** และหยุดทันทีเหมือนปิดสวิตช์ — ต่างจากเคสนี้ที่นาน 60 วินาทีและมี aura นำ
- **Focal aware อย่างเดียว** ผิด เพราะผู้ป่วยจำช่วงหลังไม่ได้
- **GTC** ต้องมีเกร็งกระตุกทั้งตัว
- **Unknown onset** ใช้เมื่อไม่มีข้อมูลจุดเริ่ม ซึ่งเคสนี้มี aura บอกชัดเจนแล้ว""",
        "Epigastric rising + déjà vu + lip-smacking automatism = mesial temporal lobe seizure แบบ focal impaired awareness",
        "Seizure classification",
        ["ILAE Updated classification of epileptic seizures. Epilepsia 2025", "สไลด์ อ.พิมลพรรณ บท 2"]),
    mcq("NEU-EP-MCQ-06",
        "Which of the following statements about an aura in epilepsy is correct?",
        ["It is a warning symptom that occurs before the seizure begins",
         "It is itself a focal aware seizure and helps localize the epileptogenic zone",
         "It only occurs in generalized epilepsy",
         "Its presence excludes a structural brain lesion",
         "It always progresses to a bilateral tonic-clonic seizure"],
        1,
        """**Aura = focal aware seizure** — เป็น *ส่วนแรกของการชัก* ที่ไฟฟ้ายังจำกัดอยู่เฉพาะที่จนผู้ป่วยยังรู้ตัวและบอกเล่าได้ ไม่ใช่สัญญาณเตือนที่อยู่นอกการชัก

เพราะเป็นการชักที่จำกัดอยู่จุดเดียว **ชนิดของ aura จึงบอกตำแหน่ง (localizing value)**

| Aura | ตำแหน่งที่น่าจะเป็น |
|---|---|
| จุกแน่นลิ้นปี่ลอยขึ้น, déjà vu, กลัวฉับพลัน | **Mesial temporal** |
| ได้กลิ่นหรือรสแปลก ๆ | Uncus / insula |
| ชา เสียว ที่ส่วนใดส่วนหนึ่ง | **Parietal (postcentral)** |
| เห็นแสงวาบ สีสัน | **Occipital** |
| เสียงหรือเสียงพูด | Lateral temporal |

**ทำไมข้ออื่นผิด** — aura เกิดเฉพาะใน **focal** epilepsy ไม่ใช่ generalized · การมี aura **ไม่ได้ตัดรอยโรคโครงสร้างออก** ตรงกันข้าม มันเพิ่มเหตุผลที่ต้องทำ MRI · และ aura อาจจบแค่นั้นโดยไม่ลามไปเป็น bilateral tonic-clonic ก็ได้""",
        "Aura คือการชักแล้ว ไม่ใช่ก่อนชัก — ถามรายละเอียด aura ให้ละเอียดเพราะมันชี้ตำแหน่งรอยโรค",
        "Aura and localization",
        ["สไลด์ อ.พิมลพรรณ — Semiology", "ILAE 2025 classification"]),
    ])

# ─────────────────────────────────────────────────────────────── 4
sec("neuro-ep-04", "Focal onset — อาการบอกตำแหน่งรอยโรค",
    "frontal · temporal · parietal · occipital และการลามเป็นสองซีก", 8,
"""**Focal onset epilepsy** คือไฟฟ้าเริ่มจากเครือข่ายที่จำกัดอยู่ใน **ซีกเดียว** จุดที่เริ่มเรียก **epileptic focus** ซึ่งอาจเป็น

- **Discretely localised** — จุดเล็ก ๆ ชัดเจนในซีกเดียว มักเป็นกลุ่มที่ **ผ่าตัดได้ผลดี**
- **Widely distributed** — กระจายเป็นเครือข่ายกว้างในซีกนั้น ระบุตำแหน่งและรักษายากกว่า

### อาการตามกลีบสมอง

| กลีบ | อาการเด่น |
|---|---|
| **Frontal** | อาการทางมอเตอร์, พฤติกรรมเปลี่ยน, ท่าทางแปลก (hyperkinetic), เกิดถี่ สั้น มักขณะหลับ, สับสนหลังชักน้อย |
| **Temporal** | ความจำรบกวน, **déjà vu**, aura ทางอารมณ์, automatism, post-ictal confusion เด่น |
| **Parietal** | ความรู้สึกผิดปกติ ชา เสียว |
| **Occipital** | การมองเห็นผิดปกติ เห็นแสงวาบ |

### การลามเป็นสองซีก (focal to bilateral tonic-clonic)
ในบางราย ไฟฟ้าที่เริ่มจากจุดเดียว **ลามไปทั้งสองซีก** กลายเป็นชักเกร็งกระตุกทั้งตัว ศัพท์เดิมเรียก *secondary generalization*

> **นี่คือจุดที่วินิจฉัยพลาดบ่อยที่สุด** — ญาติมักเห็นแค่ช่วงเกร็งกระตุกทั้งตัวแล้วเล่าว่า "ชักทั้งตัว" ถ้าไม่ถามย้อนว่า *ก่อนหน้านั้นมีอาการอะไรนำหรือไม่* หรือ *หันหน้าไปข้างไหนก่อน* จะจัดเป็น generalized onset ผิด แล้ว **เลือกยาผิดตามไปด้วย**

### เบาะแสว่าเป็น focal ที่ลามมา ไม่ใช่ generalized แต่แรก
- มี **aura** นำ
- **หันหน้าหรือตาไปข้างใดข้างหนึ่งก่อน** (forced version)
- แขนขาข้างหนึ่ง **เกร็งหรือกระตุกก่อน** อีกข้าง
- **Todd's paralysis** — แขนขาอ่อนแรงข้างเดียวหลังชัก อยู่ได้เป็นนาทีถึงชั่วโมง
- **MRI พบรอยโรคข้างเดียว**
""",
    ["ก่อนจะเชื่อว่าเป็น generalized ต้องถามหา aura และการหันหน้าเสมอ",
     "Todd's paralysis หลังชัก = หลักฐานว่าการชักเริ่มจากซีกเดียว",
     "Frontal lobe seizure สั้น ถี่ ขณะหลับ ท่าทางแปลก และ EEG ผิวหนังมักปกติ",
     "Focus เล็กและชัดเจน = กลุ่มที่ผ่าตัดแล้วได้ผลดีที่สุด"],
    [
    mcq("NEU-EP-MCQ-07",
        "A 28-year-old man is witnessed to have a convulsion described by his wife as 'whole body shaking'. On detailed questioning she recalls that his head and eyes first turned forcibly to the right for several seconds before the shaking began. After the event his right arm was weak for about 40 minutes. Which of the following is the most accurate classification and implication?",
        ["Generalized onset tonic-clonic seizure; valproate is first line",
         "Focal onset seizure evolving to bilateral tonic-clonic; brain MRI is indicated",
         "Absence seizure with secondary features; ethosuximide is indicated",
         "Psychogenic non-epileptic spell; no imaging needed",
         "Myoclonic seizure of juvenile myoclonic epilepsy"],
        1,
        """**Forced version (หันหน้าและตาไปทางขวาก่อน) + Todd's paralysis หลังชัก = จุดเริ่มอยู่ที่ซีกเดียว แล้วลามไปสองซีก**

- **Version** ชี้ว่าไฟฟ้าเริ่มจาก **ซีกตรงข้ามกับทิศที่หันไป** — หันไปขวา แปลว่าเริ่มที่ **ซีกซ้าย**
- **Todd's paralysis** คืออ่อนแรงชั่วคราวของแขนขาข้างที่สัมพันธ์กับ focus หลังชัก อยู่ได้เป็นนาทีถึงหลายชั่วโมง เป็นหลักฐานเพิ่มว่าเริ่มจากจุดเดียว

**ทำไมต้องแยกให้ออก** — เพราะ **เปลี่ยนทั้งการสืบค้นและการเลือกยา**
1. Focal onset ต้อง **ทำ MRI สมอง** เพื่อหารอยโรคโครงสร้าง (เนื้องอก, cortical dysplasia, hippocampal sclerosis, รอยแผลเป็นจาก stroke)
2. ยาตัวแรกของ focal onset ตาม ILAE คือกลุ่ม **carbamazepine, levetiracetam, lamotrigine, oxcarbazepine, phenytoin, zonisamide**

**ทำไมข้ออื่นผิด** — เรียกเป็น **generalized** แล้วให้ valproate เป็นการมองข้ามรอยโรคโครงสร้างที่อาจรักษาได้ · **absence** ไม่มีเกร็งกระตุกและไม่มี Todd's paralysis · **PNES** ไม่ทำให้เกิดอ่อนแรงข้างเดียวหลังเหตุการณ์ · **myoclonic seizure** เป็นสะดุ้งสั้น ๆ ไม่มีช่วงเกร็งกระตุกยาว""",
        "หันหน้าไปข้างหนึ่งก่อน + Todd's paralysis = focal onset เสมอ → สั่ง MRI และเลือกยาแบบ focal",
        "Focal to bilateral tonic-clonic seizure",
        ["สไลด์ อ.พิมลพรรณ — Focal onset", "Glauser T, et al. Epilepsia 2013;54:551-563"]),
    mcq("NEU-EP-MCQ-08",
        "A 35-year-old woman has brief nocturnal episodes lasting 20–30 seconds in which she suddenly sits up, makes bicycling movements of the legs and vocalizes, then returns to sleep with minimal confusion. Episodes occur up to 8 times per night. Interictal scalp EEG is normal. Which lobe is most likely involved?",
        ["Occipital lobe", "Parietal lobe", "Frontal lobe", "Mesial temporal lobe", "Cerebellum"],
        2,
        """**Frontal lobe epilepsy** มีลายเซ็นที่จำง่าย

| ลักษณะ | Frontal | Temporal |
|---|---|---|
| ระยะเวลา | **สั้นมาก < 30–60 วินาที** | 30 วินาที – 2 นาที |
| ความถี่ | **ถี่มาก หลายครั้งต่อคืน** | น้อยกว่า |
| เวลาที่เกิด | **มักขณะหลับ** | ได้ทั้งหลับและตื่น |
| ท่าทาง | **Hyperkinetic** — ปั่นจักรยาน ดิ้น โยกตัว เปล่งเสียง | Oroalimentary automatism |
| Post-ictal confusion | **น้อยหรือไม่มี** | **เด่นชัด** |
| Scalp EEG ระหว่างไม่ชัก | **มักปกติ** (focus อยู่ลึก) | มักพบ temporal spikes |

เพราะท่าทางดูแปลกและ EEG ปกติ **frontal lobe epilepsy จึงถูกวินิจฉัยผิดเป็น PNES หรือ parasomnia บ่อยมาก** จุดแยกคือ **เหตุการณ์สั้น เหมือนกันทุกครั้ง (stereotyped) และเกิดถี่** ซึ่งไม่เข้ากับ PNES

**ทำไมข้ออื่นผิด** — **occipital** ให้อาการทางการมองเห็น · **parietal** ให้อาการชาหรือเสียว · **mesial temporal** มี aura ลิ้นปี่และ post-ictal confusion เด่น · **cerebellum** ไม่ก่อให้เกิดการชัก""",
        "ชักกลางคืน สั้น ถี่ ท่าทางแปลก EEG ปกติ = frontal lobe epilepsy ไม่ใช่ฝันผวาหรือ PNES",
        "Frontal lobe epilepsy",
        ["สไลด์ อ.พิมลพรรณ — Focal Onset: One Hemisphere Affected", "Continuum 2025;31(1):Epilepsy"]),
    ])

# ─────────────────────────────────────────────────────────────── 5
sec("neuro-ep-05", "Generalized onset — ชักหกชนิดที่ต้องแยกให้ออก",
    "absence · myoclonic · tonic · atonic · clonic · tonic-clonic", 9,
"""**Generalized onset** คือไฟฟ้าเริ่มจาก **เครือข่ายสองซีกพร้อมกัน** ไม่มีจุดเริ่มจุดเดียว

สามข้อที่สไลด์เน้น
1. **Bilateral from the start** — ไม่มี focus
2. **EEG เห็น generalized spike-wave พร้อมกันทุก electrode** เป็นลายเซ็น
3. **การรู้ตัวเสียเสมอ** เพราะสมองทั้งสองซีกถูกกระทบ

ผู้ป่วย generalized epilepsy คนหนึ่ง **มักมีการชักมากกว่าหนึ่งชนิด** เช่น JME มีทั้ง myoclonic, absence และ tonic-clonic

### ชักหกชนิด

| ชนิด | ลักษณะ | จุดจำ |
|---|---|---|
| **Absence** | เหม่อลอย "ค้าง" ไม่กี่วินาที | เสียการรู้ตัวชั่วคราว **ฟื้นทันที ไม่มี post-ictal** พบมากในกลุ่มอาการวัยเด็ก |
| **Tonic-clonic** | เกร็งแล้วตามด้วยกระตุกเป็นจังหวะ | ชนิดที่คนรู้จักมากที่สุด เดิมเรียก *grand mal* มี **หมดสติและ post-ictal confusion** |
| **Myoclonic** | สะดุ้งคล้ายไฟช็อต สั้นมาก | **มักเกิดตอนเช้าหลังตื่นนอน** สัมพันธ์กับ **JME** |
| **Tonic** | เกร็งทั้งตัวทันที มักล้ม | สั้นแต่บาดเจ็บง่าย พบใน **Lennox-Gastaut** |
| **Atonic** | แรงตึงตัวหายไปทันที ล้มทรุด | เรียก **"drop attack"** เสี่ยงบาดเจ็บศีรษะสูง |
| **Clonic** | กระตุกเป็นจังหวะซ้ำ ๆ | พบน้อยกว่า tonic-clonic แต่อาจยาวนาน |

### จุดที่คนพลาดบ่อย
- **แยก absence กับ focal impaired awareness ให้ได้** — เป็นข้อสอบคลาสสิก

| | **Absence** | **Focal impaired awareness** |
|---|---|---|
| ระยะเวลา | **5–15 วินาที** | 30 วินาที – 2 นาที |
| Aura | **ไม่มี** | มักมี |
| Automatism | มีได้เล็กน้อย (กะพริบตา) | เด่น (เคี้ยว คลำ) |
| หลังหยุด | **กลับมาปกติทันที ทำงานต่อได้** | **สับสน** |
| ความถี่ | **มากถึงวันละเป็นร้อยครั้ง** | น้อยกว่ามาก |
| EEG | **3 Hz generalized spike-wave** | focal discharge |
| กระตุ้นด้วย hyperventilation | **ได้ผลดีมาก** | ไม่ |

- **Atonic กับ tonic ทำให้ล้มเหมือนกัน** แต่ atonic คือ *ตัวอ่อนทรุด* ส่วน tonic คือ *เกร็งแข็งแล้วล้ม*
""",
    ["Generalized = เริ่มสองซีกพร้อมกัน เสียการรู้ตัวเสมอ EEG เป็น generalized spike-wave",
     "Absence สั้น 5–15 วินาที ไม่มี aura ฟื้นทันที และกระตุ้นได้ด้วย hyperventilation",
     "Myoclonic jerk ตอนเช้าหลังตื่น = คิดถึง JME ก่อนเสมอ",
     "Drop attack ในเด็กที่พัฒนาการช้า = atonic seizure ของ Lennox-Gastaut"],
    [
    mcq("NEU-EP-MCQ-09",
        "An 8-year-old girl is referred for 'daydreaming' at school. Her teacher reports she stops mid-sentence, stares for about 8 seconds with slight eyelid fluttering, then immediately continues what she was doing without any confusion. This happens dozens of times daily. Three minutes of hyperventilation in clinic reproduces an episode. Which EEG finding is expected?",
        ["Left temporal sharp waves",
         "Generalized 3 Hz spike-and-wave discharges",
         "Generalized slow spike-and-wave at less than 2.5 Hz",
         "Centrotemporal spikes increasing in sleep",
         "Burst suppression pattern"],
        1,
        """**Childhood absence epilepsy (CAE)** — ลักษณะครบทุกอย่าง: อายุ 4–10 ปี, เหม่อสั้น ๆ ไม่กี่วินาที, **เกิดได้ถึงวันละ 100 ครั้ง**, **ฟื้นทันทีไม่มี post-ictal**, และ **hyperventilation กระตุ้นได้**

EEG ที่จำเพาะคือ **generalized 3 Hz spike-and-wave discharge** ขึ้นพร้อมกันทุก electrode

**ทำไมข้ออื่นผิด**

| ตัวเลือก | เป็นของโรคใด |
|---|---|
| Left temporal sharp waves | **Temporal lobe epilepsy** (focal) — จะมี aura และ post-ictal confusion |
| **Slow spike-wave < 2.5 Hz** | **Lennox-Gastaut syndrome** — เด็กจะมีพัฒนาการช้าและชักหลายชนิด |
| Centrotemporal spikes เพิ่มขึ้นตอนหลับ | **SeLECTS (Benign Rolandic)** — ชักที่ใบหน้า น้ำลายไหล พูดไม่ได้ ขณะหลับ |
| Burst suppression | **Early-infantile DEE** ในทารก |

> จุดที่ครูและพ่อแม่มักเข้าใจผิดว่าเป็น **ใจลอยหรือไม่ตั้งใจเรียน** ทำให้วินิจฉัยช้า ทั้งที่กระทบการเรียนมาก — สไลด์เน้นประเด็นนี้ไว้ชัด""",
        "เหม่อสั้น ๆ วันละหลายสิบครั้ง + hyperventilation กระตุ้นได้ = CAE, EEG 3 Hz spike-wave",
        "Childhood absence epilepsy",
        ["สไลด์ อ.พิมลพรรณ — Childhood Absence Epilepsy", "ILAE childhood syndromes. Epilepsia 2022;63:1398-1442"]),
    mcq("NEU-EP-MCQ-10",
        "A 6-year-old boy with developmental delay has multiple seizure types including sudden falls from loss of muscle tone, tonic stiffening during sleep, and atypical staring spells. EEG shows generalized slow spike-and-wave at 2 Hz. Which of the following is the most likely syndrome?",
        ["Childhood absence epilepsy",
         "Juvenile myoclonic epilepsy",
         "Lennox-Gastaut syndrome",
         "Self-limited epilepsy with centrotemporal spikes",
         "Dravet syndrome"],
        2,
        """**Lennox-Gastaut syndrome (LGS)** — สามขาหลักที่ต้องครบ

1. **เริ่มในวัยเด็กเล็ก ราว 1–7 ปี**
2. **ชักหลายชนิด** — tonic (โดยเฉพาะขณะหลับ), **atonic (drop attack)**, atypical absence
3. **EEG: slow spike-and-wave < 2.5 Hz**
4. พยากรณ์โรคไม่ดี — **พัฒนาการช้า/สติปัญญาบกพร่อง และดื้อยาในผู้ป่วยส่วนใหญ่**

**ทำไมข้ออื่นผิด**
- **CAE** มีการชักชนิดเดียว พัฒนาการปกติ EEG **3 Hz** ไม่ใช่ 2 Hz
- **JME** เริ่มวัยรุ่น (12–18 ปี) พัฒนาการปกติ อาการเด่นคือสะดุ้งตอนเช้า
- **SeLECTS** พัฒนาการปกติ ชักที่ใบหน้าขณะหลับ พยากรณ์โรคดีมาก หายเองเมื่ออายุ 16
- **Dravet** เริ่มในขวบปีแรก นำด้วย **ชักจากไข้ที่นานผิดปกติ** สัมพันธ์กับยีน **SCN1A**

> **ตัวเลขความถี่ของ spike-wave คือกุญแจ** — 3 Hz คิดถึง CAE, < 2.5 Hz คิดถึง LGS""",
        "Drop attack + ชักหลายชนิด + พัฒนาการช้า + slow spike-wave < 2.5 Hz = Lennox-Gastaut",
        "Lennox-Gastaut syndrome",
        ["สไลด์ อ.พิมลพรรณ — LGS", "Continuum (Minneap Minn) 2025;31(1):14-37"]),
    ])

# ─────────────────────────────────────────────────────────────── 6
sec("neuro-ep-06", "Epilepsy syndrome — ทำไมต้องแยกให้ได้",
    "นิยาม · สี่องค์ประกอบ · ประโยชน์สี่ข้อ", 7,
"""**Epilepsy syndrome** = *"กลุ่มลักษณะทางคลินิกและ EEG ที่จับคู่กันอย่างมีแบบแผน มักมีสาเหตุจำเพาะสนับสนุน"*

ส่วนใหญ่วินิจฉัยในวัยเด็ก แต่ **หลายกลุ่มอาการคงอยู่ถึงวัยรุ่นและผู้ใหญ่** และต้องติดตามระยะยาว

### สี่องค์ประกอบที่ใช้นิยามกลุ่มอาการ
1. **ชนิดของการชัก** — focal, generalized, absence, tonic-clonic หรือผสม
2. **อายุที่เริ่มเป็น** — เบาะแสที่มีน้ำหนักมากในการวินิจฉัย
3. **รูปแบบ EEG** — บางกลุ่มจำเพาะจนใช้วินิจฉัยได้เลย
4. **ภาพ MRI ผลแล็บ และการตรวจพันธุกรรม**

### ทำไมต้องจำแนกกลุ่มอาการ — ประโยชน์สี่ข้อ

| ประโยชน์ | รายละเอียด |
|---|---|
| **บอกสาเหตุ** | กลุ่มอาการชี้ทางไปหา aetiology ที่น่าจะเป็น |
| **เตือนโรคร่วม** | ความเสี่ยงต่อปัญหาการเรียน ADHD และพฤติกรรม |
| **นำทางการรักษาและพยากรณ์โรค** | เลือกยาได้ตรง และบอกได้ว่าจะหายเองหรือไม่ |
| **ใช้ในงานวิจัย** | สื่อสารมาตรฐานเดียวกันทั่วโลก ใช้ในการทดลองทางคลินิก |

### แบ่งกลุ่มอาการได้สองแกน

**แกนที่ 1 — ตามชนิดการชัก**
- **Generalized onset** เท่านั้น
- **Focal onset** เท่านั้น
- **Combined** มีทั้งสองแบบ
- **DEEs** — Developmental and Epileptic Encephalopathies

**แกนที่ 2 — ตามอายุที่เริ่ม**

| ช่วงอายุ | ตัวอย่าง |
|---|---|
| **ทารกแรกเกิดและวัยทารก** | Early-Infantile DEE, Migrating Focal Epilepsies of Infancy, **Dravet syndrome** — รุนแรงที่สุด มักมีสาเหตุทางพันธุกรรม |
| **วัยเด็กเล็ก** | **Lennox-Gastaut**, Panayiotopoulos, **SeLECTS (BECTS)** — มีตั้งแต่ไม่รุนแรงจนถึงรุนแรงมาก |
| **วัยรุ่น** | **JME**, Juvenile Absence Epilepsy — มักเป็นตลอดชีวิตแต่คุมได้ดีด้วยยา |
| **ผู้ใหญ่** | ไม่ค่อยมีกลุ่มอาการจำเพาะ ให้เน้นระบุ **ชนิดการชักและชนิดของโรคลมชัก** เพื่อวางแผนรักษา |

### Benign กับ Severe
- **Self-limited ("benign")** — ชักจำกัดช่วงเวลา เด็ก**หายเองเมื่อถึงอายุที่คาดได้** พยากรณ์โรคดีมาก **ไม่จำเป็นต้องให้ยาทุกราย**
- **Severe / pharmacoresistant** — คุมยาก ต้องใช้หลายกลยุทธ์ มักมาพร้อมปัญหาการเรียน พฤติกรรม และพัฒนาการ ต้องดูแลแบบสหวิชาชีพ
""",
    ["สี่องค์ประกอบของกลุ่มอาการ: ชนิดการชัก + อายุที่เริ่ม + EEG + ภาพและพันธุกรรม",
     "อายุที่เริ่มเป็นคือเบาะแสที่มีน้ำหนักที่สุดในการเดากลุ่มอาการ",
     "กลุ่ม self-limited ไม่จำเป็นต้องให้ยาทุกราย — ตัดสินใจร่วมกับครอบครัว",
     "ในผู้ใหญ่มักไม่มีกลุ่มอาการจำเพาะ ให้เน้นระบุชนิดการชักเพื่อเลือกยา"],
    [
    mcq("NEU-EP-MCQ-11",
        "Which of the following is NOT one of the four defining characteristics used to identify an epilepsy syndrome?",
        ["Seizure type(s)", "Age of onset", "EEG pattern", "Response to a therapeutic trial of benzodiazepine", "MRI findings, laboratory and genetic tests"],
        3,
        """สไลด์ระบุองค์ประกอบของ epilepsy syndrome ไว้ **สี่ข้อ**

1. **Seizure type(s)** — ชนิดของการชัก
2. **Age of onset** — อายุที่เริ่มมีอาการ
3. **EEG pattern** — รูปแบบคลื่นไฟฟ้าสมอง บางแบบจำเพาะจนใช้วินิจฉัยได้
4. **MRI findings, lab and genetic tests**

**การตอบสนองต่อยา benzodiazepine ไม่ใช่เกณฑ์** — benzodiazepine หยุดการชักได้แทบทุกชนิด รวมทั้ง **ทำให้เหตุการณ์ของ PNES ดูเหมือนดีขึ้นด้วย** จึงไม่มีค่าในการจำแนกกลุ่มอาการ และการใช้การตอบสนองต่อยาเป็นเครื่องวินิจฉัยเป็นกับดักที่อันตราย""",
        "สี่องค์ประกอบคือ ชนิดการชัก · อายุที่เริ่ม · EEG · MRI และพันธุกรรม — การตอบสนองต่อยาไม่ใช่เกณฑ์",
        "Definition of epilepsy syndrome",
        ["สไลด์ อ.พิมลพรรณ บท 3 — Key Characteristics of Epilepsy Syndromes"]),
    ])

# ─────────────────────────────────────────────────────────────── 7
sec("neuro-ep-07", "สามกลุ่มอาการที่ต้องรู้จัก — SeLECTS, CAE, JME",
    "อายุเริ่ม · อาการ · EEG · พยากรณ์โรค · การให้ยา", 10,
"""### SeLECTS — Self-Limited Epilepsy with Centrotemporal Spikes
*(ชื่อเดิม Benign Rolandic Epilepsy / BECTS)*

- **ความชุก** — ราว **15% ของเด็กที่เป็นโรคลมชัก**
- **อายุเริ่ม** ประมาณ **3–13 ปี** และ **เกือบทั้งหมดหายเองเมื่ออายุ 16 ปี**
- **อาการ** — ชักแบบ focal ที่เด่นบริเวณใบหน้า มี **อาการทางความรู้สึกและการเคลื่อนไหวของใบหน้า กลืนลำบาก พูดไม่ได้ น้ำลายไหล** และ **มักเกิดขณะหลับหรือตอนตื่นนอน** บางรายลามเป็น tonic-clonic ทั้งตัว
- **การรักษา** — เพราะพยากรณ์โรคดีเยี่ยม **ไม่จำเป็นต้องให้ยาทุกราย** การตัดสินใจให้ยาควร **ทำร่วมกับครอบครัว**

### CAE — Childhood Absence Epilepsy
- **อายุเริ่ม 4–10 ปี** · **พบในเด็กหญิงมากกว่าเด็กชายเล็กน้อย** · คิดเป็น **สูงถึง 18%** ของเด็กวัยเรียนที่ได้รับวินิจฉัยโรคลมชัก
- **อาการ** — absence สั้น ๆ ไม่กี่วินาที **มากได้ถึงวันละ 100 ครั้ง** รบกวนการเรียนและสมาธิอย่างมาก **มักถูกเข้าใจผิดว่าใจลอย** ทำให้วินิจฉัยช้า
- **EEG** — generalized **3 Hz** spike-and-wave, **hyperventilation กระตุ้นได้**

### JME — Juvenile Myoclonic Epilepsy
- **ความชุก** — ราว **5–10% ของโรคลมชักทั้งหมด** เป็นกลุ่มอาการที่พบบ่อยที่สุดกลุ่มหนึ่ง
- **อายุเริ่ม** — ได้ตั้งแต่ **8–36 ปี** แต่ยอดอยู่ที่ **12–18 ปี** ค่าเฉลี่ยราว **15 ปี** ซึ่งตรงกับช่วงที่ฮอร์โมนเปลี่ยน นอนไม่เป็นเวลา และความเครียดทางสังคมเพิ่ม
- **อาการหลัก** — **myoclonic jerk**: กล้ามเนื้อกระตุกสั้น ๆ ครั้งเดียวหรือหลายครั้ง มักที่ **แขน ไหล่ คอ** เกิด **หลังตื่นนอน ช่วงเย็น หรือเมื่ออดนอน**
- **ลำดับการดำเนินโรค** — **myoclonic jerk มาก่อน GTC ครั้งแรกโดยเฉลี่ย 3.3 ปี** แล้วจึงได้รับวินิจฉัย JME
- **Absence** พบใน **10–40%** ของผู้ป่วย JME มักไม่ชัดและถูกมองข้าม

**ตัวกระตุ้นสำคัญของ JME**

| ตัวกระตุ้น | รายละเอียด |
|---|---|
| **อดนอน** | **ตัวกระตุ้นที่แรงและสม่ำเสมอที่สุด** |
| **แอลกอฮอล์** | โดยเฉพาะ rebound effect ในเช้าวันรุ่งขึ้น |
| **ความเครียด** | ทั้งทางอารมณ์และทางกาย ลด seizure threshold |
| **แสงกะพริบ** | **photosensitivity พบ 30–40%** ของผู้ป่วย JME |

> **เหตุผลที่ JME ถูกวินิจฉัยช้า** — ผู้ป่วยไม่คิดว่าอาการสะดุ้งทำแก้วน้ำหกตอนเช้าเป็นเรื่องผิดปกติ จึงไม่เล่าให้แพทย์ฟัง จนกระทั่งชักทั้งตัวครั้งแรก **ถ้าไม่ถามตรง ๆ ว่า "ตอนเช้าเคยสะดุ้งจนของหลุดมือไหม" จะพลาด**
""",
    ["ถามหา myoclonic jerk ตอนเช้าในวัยรุ่นทุกคนที่มาด้วย GTC ครั้งแรก — ไม่ถามจะไม่ได้คำตอบ",
     "SeLECTS หายเองเมื่ออายุ 16 จึงไม่จำเป็นต้องให้ยาทุกราย",
     "CAE: 3 Hz spike-wave, hyperventilation กระตุ้นได้, พบในเด็กหญิงมากกว่าเล็กน้อย",
     "JME: อดนอนคือตัวกระตุ้นที่แรงที่สุด และ 30–40% ไวต่อแสงกะพริบ"],
    [
    mcq("NEU-EP-MCQ-12",
        "A 16-year-old student is brought in after his first generalized tonic-clonic seizure, which occurred at 7 a.m. after a night of studying without sleep. On direct questioning he admits that for the past 3 years he has had brief jerks of both arms shortly after waking, occasionally spilling his morning drink. Which of the following is the most likely diagnosis?",
        ["Childhood absence epilepsy",
         "Juvenile myoclonic epilepsy",
         "Temporal lobe epilepsy",
         "Lennox-Gastaut syndrome",
         "Self-limited epilepsy with centrotemporal spikes"],
        1,
        """**JME ครบทุกองค์ประกอบ** — วัยรุ่น, **myoclonic jerk ตอนเช้าหลังตื่นมา 3 ปี**, แล้วตามด้วย **GTC ครั้งแรกหลังอดนอน**

ลำดับนี้คือแบบฉบับที่สไลด์วางไว้: **myoclonic jerk นำหน้า GTC ครั้งแรกโดยเฉลี่ย 3.3 ปี** ผู้ป่วยไม่เคยเล่าเพราะคิดว่าเป็นเรื่องปกติ **ต้องถามตรง ๆ จึงจะได้ประวัตินี้**

**สิ่งที่ต้องทำต่อ**
- **EEG** คาดว่าพบ **generalized 4–6 Hz polyspike-and-wave** และอาจมี photoparoxysmal response
- **คุมตัวกระตุ้น** — นอนให้พอเป็นอันดับแรก เลี่ยงแอลกอฮอล์ จัดการความเครียด
- **แจ้งว่ามักต้องกินยาระยะยาว** ต่างจาก SeLECTS ที่หายเอง

**ทำไมข้ออื่นผิด**
- **CAE** เริ่ม 4–10 ปี อาการเด่นคือเหม่อ ไม่ใช่สะดุ้ง
- **Temporal lobe epilepsy** เป็น focal มี aura และ automatism
- **LGS** เริ่มวัยเด็กเล็ก มีพัฒนาการช้าและ drop attack
- **SeLECTS** เป็น focal ที่ใบหน้าขณะหลับ และหายเองก่อนอายุ 16""",
        "วัยรุ่น + GTC หลังอดนอน + สะดุ้งตอนเช้า = JME — และ jerk มาก่อน GTC เฉลี่ย 3.3 ปี",
        "Juvenile myoclonic epilepsy",
        ["สไลด์ อ.พิมลพรรณ — JME", "ILAE syndromes at variable age. Epilepsia 2022;63:1443-1474"]),
    mcq("NEU-EP-MCQ-13",
        "Which single lifestyle factor is described as the most potent and consistent seizure trigger in juvenile myoclonic epilepsy?",
        ["High caffeine intake", "Sleep deprivation", "Dehydration", "High-protein diet", "Cold exposure"],
        1,
        """**การอดนอนคือตัวกระตุ้นที่แรงและสม่ำเสมอที่สุดใน JME** — สไลด์ระบุไว้ชัดว่า *"the most potent and consistent trigger"*

ตัวกระตุ้นอื่นตามลำดับที่สไลด์ให้ไว้

| ตัวกระตุ้น | หมายเหตุ |
|---|---|
| **Sleep deprivation** | **แรงที่สุด** |
| **แอลกอฮอล์** | โดยเฉพาะ **rebound ในเช้าวันถัดมา** ไม่ใช่ขณะดื่ม |
| **ความเครียด** | ทั้งทางอารมณ์และทางกาย |
| **แสงกะพริบ** | **30–40%** ของผู้ป่วย JME มี photosensitivity |

**นัยทางคลินิก** — การให้คำแนะนำเรื่องการนอนสำหรับวัยรุ่นที่เป็น JME **มีน้ำหนักเทียบเท่ากับการปรับยา** โดยเฉพาะช่วงสอบ ทำงานกะ หรือปาร์ตี้ และต้องเตือนเรื่องการขับขี่

ตัวเลือกอื่น (คาเฟอีน ขาดน้ำ อาหารโปรตีนสูง ความเย็น) **ไม่ใช่ตัวกระตุ้นที่มีหลักฐานใน JME**""",
        "คุมการนอนคือการรักษา JME ที่ไม่ต้องสั่งยา — ถามเรื่องการนอนทุกครั้งที่ติดตามอาการ",
        "JME triggers",
        ["สไลด์ อ.พิมลพรรณ — Common Seizure Triggers"]),
    ])

# ─────────────────────────────────────────────────────────────── 8
sec("neuro-ep-08", "DEEs — Dravet และ Lennox-Gastaut",
    "เมื่อไฟฟ้าที่ผิดปกติทำให้พัฒนาการแย่ลงเอง", 8,
"""**Developmental and Epileptic Encephalopathies (DEEs)** นิยามด้วย **พัฒนาการบกพร่อง ร่วมกับการชักที่ถี่และมักดื้อยา เริ่มตั้งแต่อายุน้อย**

หัวใจของแนวคิดนี้คือ **ตัวกิจกรรมไฟฟ้าที่ผิดปกติเองทำให้ผลลัพธ์ทางพัฒนาการแย่ลง** ไม่ใช่แค่โรคพื้นฐานอย่างเดียว — จึงเป็นเหตุผลที่ต้องพยายามคุมการชักให้ได้เร็วที่สุด

- เสี่ยงต่อ **สติปัญญาบกพร่อง ปัญหาพฤติกรรม และอายุขัยสั้นลง** อย่างมีนัยสำคัญ
- การประเมินต้องมี **การตรวจพันธุกรรม ภาพสมองขั้นสูง และ metabolic workup** เพื่อหาสาเหตุที่อาจรักษาตรงจุดได้

### Dravet syndrome

| หัวข้อ | รายละเอียด |
|---|---|
| **อายุเริ่ม** | **ขวบปีแรก** ในทารกที่แข็งแรงดีมาก่อน |
| **อาการนำ** | **ชักจากไข้ที่นานผิดปกติ** บางครั้งเป็น **unilateral clonic** |
| **ตัวกระตุ้น** | **ไข้หรืออุณหภูมิกายสูง** (อาบน้ำอุ่น อากาศร้อน) |
| **พันธุกรรม** | **SCN1A mutation** ในผู้ป่วยส่วนใหญ่ |
| **การดำเนินโรค** | พัฒนาการถดถอยและสติปัญญาบกพร่องตามมา |
| **ความเสี่ยง** | **SUDEP สูง** |
| **ข้อห้ามสำคัญ** | **ห้ามใช้ sodium channel blocker เช่น carbamazepine — ทำให้ชักแย่ลง** |

> **ข้อห้ามของ carbamazepine ใน Dravet คือจุดที่ออกสอบบ่อยที่สุดของหัวข้อนี้** เหตุผลเชิงกลไก: SCN1A ที่กลายพันธุ์ทำให้ช่องโซเดียมของ **inhibitory interneuron** ทำงานบกพร่องอยู่แล้ว การให้ยาที่ไปปิดช่องโซเดียมซ้ำจึงกดการยับยั้งลงไปอีก ทำให้ชักมากขึ้น ยากลุ่มเดียวกันที่ต้องเลี่ยงรวมถึง **phenytoin, oxcarbazepine, lamotrigine**

### Lennox-Gastaut syndrome (LGS)

| หัวข้อ | รายละเอียด |
|---|---|
| **อายุเริ่ม** | วัยเด็กเล็ก **1–7 ปี** |
| **ชนิดการชัก** | **tonic, atonic (drop attack), atypical absence** — หลายชนิดในคนเดียว |
| **EEG** | **slow spike-and-wave < 2.5 Hz** เป็นลายเซ็นวินิจฉัย |
| **พยากรณ์โรค** | **สติปัญญาบกพร่องชัดเจนและดื้อยาในผู้ป่วยส่วนใหญ่** |
""",
    ["DEE = ไฟฟ้าที่ผิดปกติเองทำให้พัฒนาการแย่ลง จึงต้องรีบคุมการชัก",
     "Dravet: ขวบปีแรก + ชักจากไข้ที่นาน + SCN1A — ห้าม carbamazepine เด็ดขาด",
     "LGS: 1–7 ปี + ชักหลายชนิด + slow spike-wave < 2.5 Hz",
     "DEE ทุกรายควรได้ตรวจพันธุกรรมและ metabolic workup"],
    [
    mcq("NEU-EP-MCQ-14",
        "A 14-month-old previously healthy infant has had several prolonged febrile seizures, some with unilateral clonic activity, often triggered by warm baths. Genetic testing reveals an SCN1A mutation. Which of the following medications is contraindicated?",
        ["Valproate", "Clobazam", "Carbamazepine", "Topiramate", "Stiripentol"],
        2,
        """**Dravet syndrome — sodium channel blocker เป็นข้อห้าม**

สไลด์ระบุไว้ตรง ๆ ว่า *"Sodium channel blockers (e.g., carbamazepine) are contraindicated in Dravet Syndrome and may worsen seizures"*

**กลไก** — การกลายพันธุ์ของ **SCN1A** ทำให้ช่องโซเดียมของ **inhibitory GABAergic interneuron** ทำงานบกพร่อง สมองจึงมีการยับยั้งน้อยอยู่แล้ว การให้ยาที่ปิดช่องโซเดียมเพิ่มจะไปกดการยับยั้งที่เหลือลงอีก → **ชักถี่และรุนแรงขึ้น**

**ยาที่ต้องเลี่ยงในกลุ่มเดียวกัน** — carbamazepine, **oxcarbazepine, phenytoin, lamotrigine**

**ยาที่ใช้ได้** — **valproate, clobazam, stiripentol, topiramate** และยาใหม่ เช่น fenfluramine, cannabidiol

**เบาะแสที่ชี้ Dravet ในเคสนี้**
- ทารกแข็งแรงดีมาก่อน แล้วชักในขวบปีแรก
- **ชักจากไข้ที่นานผิดปกติ** และบางครั้ง **เป็นข้างเดียว**
- **ถูกกระตุ้นด้วยความร้อน** — อาบน้ำอุ่นเป็นตัวกระตุ้นคลาสสิก
- ยืนยันด้วย **SCN1A**""",
        "Dravet + carbamazepine = ชักแย่ลง — จำคู่นี้ให้แม่น รวมถึง phenytoin, oxcarbazepine, lamotrigine",
        "Dravet syndrome",
        ["สไลด์ อ.พิมลพรรณ — Dravet Syndrome", "ILAE neonatal/infantile syndromes. Epilepsia 2022;63:1349-1397"]),
    ])

# ─────────────────────────────────────────────────────────────── 9
sec("neuro-ep-09", "การสืบค้น — EEG, MRI และการหาสาเหตุ",
    "EEG บอกการทำงาน MRI บอกโครงสร้าง — และข้อจำกัดของทั้งคู่", 9,
"""สไลด์สรุปไว้สั้นและคมว่า **EEG กับ MRI คือเสาหลักคู่ของการสืบค้นโรคลมชัก — อันหนึ่งบอกว่าสมองทำงานทางไฟฟ้าอย่างไร อีกอันบอกว่าสมองมีหน้าตาอย่างไร**

### EEG
- เป็น **เครื่องมือมาตรฐานสำหรับจับรูปแบบไฟฟ้าที่ผิดปกติ**
- แยก **focal discharge (จำกัดบริเวณเดียว)** ออกจาก **generalized spike-wave**

### MRI
- หา **สาเหตุเชิงโครงสร้างของ focal epilepsy** เช่น **hippocampal sclerosis, cortical dysplasia, เนื้องอก**

### ข้อจำกัดที่ต้องพูดให้ชัด — จุดที่คนพลาดมากที่สุด

> **EEG และ MRI เป็นเพียงตัวสนับสนุน ไม่ใช่ตัววินิจฉัย**
> - **EEG ปกติ ไม่ตัดโรคลมชักออก** — ผู้ป่วยโรคลมชักจำนวนมาก EEG ครั้งแรกปกติ เพราะบันทึกแค่ช่วงสั้นและ focus อาจอยู่ลึก (เช่น frontal)
> - **EEG ผิดปกติอย่างเดียวก็วินิจฉัยโรคลมชักไม่ได้** — คนปกติส่วนน้อยมี epileptiform discharge ได้
> - **การวินิจฉัยโรคลมชักยังเป็นการวินิจฉัยทางคลินิก** ที่อาศัยประวัติจากผู้ป่วยและผู้เห็นเหตุการณ์เป็นหลัก
> - ใน **generalized epilepsy นั้น MRI มักปกติ** ซึ่งเป็นการชี้ไปทางสาเหตุพันธุกรรมหรือเมตาบอลิก ไม่ใช่ว่าตรวจไม่ละเอียดพอ

**วิธีเพิ่มโอกาสจับ epileptiform discharge เมื่อ EEG ครั้งแรกปกติ**
- **Sleep-deprived EEG** หรือบันทึกขณะหลับ
- ทำ **activation procedure** — hyperventilation และ photic stimulation
- **บันทึกซ้ำ** หรือทำ **prolonged / video-EEG monitoring**

### สาเหตุของโรคลมชัก

| กลุ่มสาเหตุ | รายละเอียด |
|---|---|
| **Genetic** | มีประวัติครอบครัวส่งต่อยีน **หรือ de novo mutation ที่ไม่ได้รับถ่ายทอดจากพ่อแม่** |
| **Structural** | ความผิดปกติของพัฒนาการสมอง, **อุบัติเหตุทางสมอง, stroke, เนื้องอก** |
| **Metabolic, immune, infectious** | รวม autoimmune encephalitis และการติดเชื้อระบบประสาท |
| **Unknown** | **ราวหนึ่งในสามของผู้ป่วยทั้งหมด** — ยังหาสาเหตุไม่พบ |
""",
    ["EEG ปกติ ไม่ตัดโรคลมชัก และ EEG ผิดปกติอย่างเดียวก็วินิจฉัยไม่ได้",
     "การวินิจฉัยโรคลมชักเป็นการวินิจฉัยทางคลินิก — ประวัติจากผู้เห็นเหตุการณ์สำคัญที่สุด",
     "Generalized epilepsy มักมี MRI ปกติ ไม่ใช่ความผิดพลาดของการตรวจ",
     "ราวหนึ่งในสามของผู้ป่วยยังหาสาเหตุไม่พบ"],
    [
    mcq("NEU-EP-MCQ-15",
        "A 26-year-old woman has had three witnessed unprovoked convulsions over 8 months. Her routine 30-minute interictal EEG is normal and MRI of the brain is normal. Which of the following is the most appropriate interpretation?",
        ["Epilepsy is excluded by the normal EEG",
         "She has epilepsy; normal EEG and MRI do not exclude the diagnosis",
         "The diagnosis requires a repeat MRI with contrast before treatment",
         "Normal EEG confirms the events are psychogenic",
         "Antiseizure medication must be withheld until EEG becomes abnormal"],
        1,
        """**การวินิจฉัยโรคลมชักเป็นการวินิจฉัยทางคลินิก** ผู้ป่วยรายนี้มี **unprovoked seizure 3 ครั้ง** จึงเข้าเกณฑ์ ILAE ข้อ 1 ไปแล้ว ไม่ว่า EEG และ MRI จะเป็นอย่างไร

สไลด์ระบุไว้ชัดว่า *"EEG and MRI are supportive, but a normal EEG does not exclude epilepsy, and an abnormal EEG alone is not sufficient to diagnose it"*

**ทำไม EEG ถึงปกติได้ทั้งที่เป็นโรคลมชัก**
- Routine EEG บันทึกเพียง **20–30 นาที** ซึ่งอาจไม่ตรงกับช่วงที่มี discharge
- **Focus ที่อยู่ลึก** เช่น mesial frontal หรือ mesial temporal ตรวจจับจากหนังศีรษะได้ยาก
- ผู้ป่วยอาจได้รับยาที่กด discharge อยู่แล้ว

**สิ่งที่ควรทำต่อ** — **sleep-deprived EEG, บันทึกขณะหลับ, ทำ activation (hyperventilation, photic), บันทึกซ้ำ หรือ prolonged/video-EEG** และ **เริ่มยาได้ตามการวินิจฉัยทางคลินิก**

**ทำไมข้ออื่นผิด** — MRI ปกติเข้ากันได้ดีกับ **generalized epilepsy** ที่มักไม่พบรอยโรค จึงไม่จำเป็นต้องทำซ้ำด้วย contrast ทันที · และ **EEG ปกติไม่ได้ยืนยันว่าเป็น PNES** การยืนยัน PNES ต้องจับเหตุการณ์จริงด้วย **video-EEG**""",
        "EEG ปกติไม่เคยตัดโรคลมชักออก — วินิจฉัยด้วยประวัติ แล้วใช้ EEG/MRI เพื่อจำแนกและหาสาเหตุ",
        "Limitations of EEG and MRI",
        ["สไลด์ อ.พิมลพรรณ — Investigation for Established Epilepsy"]),
    mcq("NEU-EP-MCQ-16",
        "Approximately what proportion of epilepsy cases are classified as having an unknown cause?",
        ["About 5%", "About one-third", "About two-thirds", "About 90%", "Less than 1%"],
        1,
        """**ราวหนึ่งในสาม (about one-third)** ของผู้ป่วยโรคลมชักจัดอยู่ในกลุ่ม **unknown aetiology** ซึ่งหมายความว่า *อาจมีสาเหตุอยู่แต่ยังตรวจไม่พบ* ไม่ใช่ว่าไม่มีสาเหตุ

**กลุ่มสาเหตุตามสไลด์**

| กลุ่ม | ตัวอย่าง |
|---|---|
| **Genetic** | ยีนที่ถ่ายทอดในครอบครัว หรือ **de novo mutation** |
| **Structural** | ความผิดปกติของพัฒนาการสมอง, traumatic brain injury, stroke, เนื้องอก |
| **Metabolic / immune / infectious** | autoimmune encephalitis, การติดเชื้อระบบประสาท |
| **Unknown** | **~1/3** |

> อย่าสับสนกับตัวเลขอีกตัวของคาบนี้: **ประมาณ 2 ใน 3 ของผู้ป่วยคุมการชักได้ดีด้วยยา** และ **1 ใน 3 ดื้อยา** — คนละเรื่องกับสัดส่วนของสาเหตุที่ไม่ทราบ แม้เป็นเศษส่วนเดียวกัน""",
        "1/3 = สาเหตุไม่ทราบ · 2/3 = คุมได้ด้วยยา · 1/3 = ดื้อยา — สามตัวเลขนี้ห้ามสลับกัน",
        "Aetiology of epilepsy",
        ["สไลด์ อ.พิมลพรรณ — What Causes Epilepsy?"]),
    ])

# ─────────────────────────────────────────────────────────────── 10
sec("neuro-ep-10", "เลือกยากันชักให้ตรงชนิดการชัก",
    "ASM เป็นการรักษาหลัก · เกณฑ์เลือกยา · ILAE และ NICE", 10,
"""**ยากันชัก (ASM) คือการรักษาอันดับแรก** ทำงานโดยหยุดหรือลดความถี่ของการชักอย่างมีนัยสำคัญ กลไกโดยรวมคือการแก้ **ความไม่สมดุลระหว่าง excitation กับ inhibition**

### สิ่งที่กำหนดการเลือกยา
- **ชนิดของการชักและกลุ่มอาการ**
- **อายุและเพศของผู้ป่วย**
- **โรคร่วมและยาที่ใช้อยู่**
- **วิถีชีวิตและความต้องการของผู้ป่วย**

> **หลักที่สไลด์ย้ำ** — *"ASM choice should be matched to the seizure type, epilepsy type or epileptic syndrome"* การเลือกยาโดยดูแค่ "ชักก็ให้ยากันชัก" คือที่มาของการรักษาล้มเหลว

### แนวทางตามหลักฐาน

**Focal (partial) onset seizures**

| กลุ่มผู้ป่วย | ILAE 2013 — Level A | NICE 2020 |
|---|---|---|
| **ผู้ใหญ่** | **CBZ, PHT, LEV, ZNS** (Level B: VPA · Level C: GBP, LTG, OXC, PB, TPM, VGB) | 1st line **CBZ, LTG** · 2nd line **LEV, OXC, VPA** |
| **เด็ก** | **OXC** (Level C: CBZ, PB, PHT, TPM, VPA, VGB) | — |
| **ผู้สูงอายุ** | **GBP, LTG** (Level C: CBZ · Level D: TPM, VPA) | — |

**Generalized tonic-clonic seizures**

| กลุ่มผู้ป่วย | ILAE 2013 | NICE 2020 |
|---|---|---|
| **ผู้ใหญ่ GTC** | **ไม่มียาใดถึง Level A หรือ B** · Level C: CBZ, LTG, OXC, PB, PHT, TPM, VPA | 1st line **VPA** · 2nd line **CLB, LTG, LEV, TPM** |
| **เด็ก GTC** | ไม่มี Level A/B · Level C: CBZ, PB, PHT, TPM, VPA | — |

**ความหมายของ Level of evidence**

| ระดับ | ความหมาย |
|---|---|
| **A** | พิสูจน์แล้วว่าได้ผลในการใช้เป็น **monotherapy เริ่มต้น** |
| **B** | น่าจะได้ผล |
| **C** | อาจได้ผล |
| **D** | มีความเป็นไปได้ว่าได้ผล |

### จุดที่คนพลาดบ่อย
- **ให้ carbamazepine กับ generalized epilepsy** — โดยเฉพาะ **JME และ absence** จะทำให้ **myoclonic jerk และ absence แย่ลง** ยา sodium channel blocker (CBZ, OXC, PHT) และ gabapentin, pregabalin, vigabatrin, tiagabine ล้วนอาจทำให้ generalized seizure เลวลง
- **VPA เป็นยาที่ดีที่สุดสำหรับ GTC แต่มีข้อจำกัดหนักในผู้หญิงวัยเจริญพันธุ์** — teratogen ชัดเจน (neural tube defect) และกระทบพัฒนาการทางสติปัญญาของทารก จึงต้องเลี่ยงและใช้ทางเลือกอื่นพร้อมคุมกำเนิดที่ได้ผล
- **ILAE ไม่มียา Level A สำหรับ GTC ในผู้ใหญ่เลย** — เป็นรายละเอียดที่สไลด์แสดงไว้และมักถูกถาม
""",
    ["เลือกยาตามชนิดการชักเสมอ ไม่ใช่ตามความคุ้นเคย",
     "Focal onset ผู้ใหญ่: CBZ, PHT, LEV, ZNS อยู่ที่ Level A",
     "GTC ผู้ใหญ่ไม่มียาใดถึง Level A — NICE ให้ VPA เป็นตัวแรก",
     "ห้ามให้ CBZ/OXC/PHT ใน JME และ absence เพราะทำให้แย่ลง",
     "VPA เลี่ยงในผู้หญิงวัยเจริญพันธุ์เพราะเป็น teratogen ชัดเจน"],
    [
    mcq("NEU-EP-MCQ-17",
        "A 17-year-old girl with juvenile myoclonic epilepsy is started on carbamazepine by a non-specialist. Two weeks later her morning myoclonic jerks have become much more frequent and she has had a new absence seizure. What is the most likely explanation?",
        ["Carbamazepine dose is too low",
         "Carbamazepine can aggravate generalized seizure types including myoclonic and absence seizures",
         "She has developed carbamazepine hypersensitivity",
         "The diagnosis must be psychogenic",
         "Carbamazepine has caused hyponatremia leading to seizures"],
        1,
        """**Carbamazepine ทำให้การชักแบบ generalized แย่ลง** โดยเฉพาะ **myoclonic และ absence** — เป็นปรากฏการณ์ที่รู้จักกันดีในชื่อ *seizure aggravation*

**ยาที่ทำให้ generalized seizure แย่ลง**

| ยา | ชนิดการชักที่แย่ลง |
|---|---|
| **Carbamazepine, oxcarbazepine, phenytoin** | **myoclonic, absence** |
| **Gabapentin, pregabalin** | myoclonic, absence |
| **Vigabatrin, tiagabine** | absence (อาจกระตุ้น absence status) |
| Lamotrigine | myoclonic ในบางราย (แม้โดยรวมใช้ใน generalized ได้) |

**สิ่งที่ควรทำ** — หยุด carbamazepine แล้วเปลี่ยนไปใช้ยาที่เหมาะกับ **idiopathic generalized epilepsy** เช่น **valproate** (แต่ระวังในหญิงวัยเจริญพันธุ์ รายนี้อายุ 17 ปี ต้องพิจารณา **levetiracetam, lamotrigine หรือ topiramate** พร้อมคุมกำเนิดที่ได้ผลถ้าจะใช้ VPA)

**ทำไมข้ออื่นผิด** — เพิ่มขนาดยาจะยิ่งแย่ลง · **hypersensitivity** ของ CBZ แสดงออกเป็นผื่นหรือ DRESS ไม่ใช่ชักถี่ขึ้น · การชักที่แย่ลงหลังได้ยาผิดชนิดไม่ได้แปลว่าเป็น **PNES** · **hyponatremia จาก CBZ** เกิดได้จริงแต่มักไม่รุนแรงพอทำให้ชักในสองสัปดาห์ และไม่อธิบาย myoclonic jerk ที่ถี่ขึ้นจำเพาะเจาะจง""",
        "JME ห้าม carbamazepine — ยา sodium channel blocker ทำให้ myoclonic และ absence แย่ลง",
        "Seizure aggravation by ASM",
        ["สไลด์ อ.พิมลพรรณ — ASM choice matched to seizure type", "Glauser T, et al. Epilepsia 2013"]),
    mcq("NEU-EP-MCQ-18",
        "According to the ILAE 2013 evidence levels shown in the lecture, which statement about initial monotherapy for generalized tonic-clonic seizures in adults is correct?",
        ["Valproate is Level A",
         "Carbamazepine is Level A",
         "No agent reaches Level A or Level B; several are Level C",
         "Levetiracetam is Level A",
         "All listed agents are Level D"],
        2,
        """สไลด์แสดงตาราง ILAE 2013 ไว้ชัดว่า สำหรับ **adults with GTC seizures**

- **Level A: None**
- **Level B: None**
- **Level C: CBZ, LTG, OXC, PB, PHT, TPM, VPA**
- **Level D: GBP, LEV, VGB**

เหตุผลไม่ใช่ว่ายาใช้ไม่ได้ผล แต่เป็นเพราะ **ยังขาดการศึกษา monotherapy แบบสุ่มที่มีคุณภาพเพียงพอในกลุ่ม GTC** ต่างจาก focal onset ที่มีงานวิจัยมากกว่ามาก

**ในทางปฏิบัติจึงต้องอ่านคู่กับ NICE 2020** ซึ่งแนะนำ **valproate เป็นตัวแรก** และ **clobazam, lamotrigine, levetiracetam, topiramate เป็นตัวรอง** สำหรับ GTC

**เทียบกับ focal onset ในผู้ใหญ่** ซึ่งมี **Level A ถึงสี่ตัวคือ CBZ, PHT, LEV, ZNS** — ความต่างนี้คือสิ่งที่ตารางในสไลด์ต้องการให้เห็น

**ความหมายของ Level** — A = พิสูจน์แล้วว่าได้ผลเป็น monotherapy เริ่มต้น, B = น่าจะได้ผล, C = อาจได้ผล, D = มีความเป็นไปได้""",
        "Focal onset ผู้ใหญ่มี Level A สี่ตัว แต่ GTC ผู้ใหญ่ไม่มี Level A เลย — ต้องอ่าน ILAE คู่กับ NICE",
        "ILAE evidence levels",
        ["สไลด์ อ.พิมลพรรณ — ASM choice is directed by evidence-based guidelines", "Glauser A, et al. Epilepsia 2013;25:320-326"]),
    ])

# ─────────────────────────────────────────────────────────────── 11
sec("neuro-ep-11", "เมื่อยาตัวแรกไม่ได้ผล — คัดกรอง pseudoresistance ก่อนเสมอ",
    "หกสาเหตุของการดื้อยาเทียม · replacement กับ add-on", 9,
"""สไลด์วาง decision framework ไว้ชัดเจน และขั้นแรกสุดไม่ใช่การเพิ่มยา แต่คือ **ยืนยันว่าล้มเหลวจริงหรือไม่**

> **ลำดับที่สไลด์วางไว้** — ยาตัวแรกล้มเหลว → **คัดกรอง pseudoresistance ก่อนเป็นอันดับแรก** → แล้วจึงแยกตามสาเหตุ

| สาเหตุที่ยาตัวแรกล้มเหลว | สิ่งที่ควรทำ |
|---|---|
| **ไม่ได้ผล (inefficacy)** | Replace **หรือ** add-on |
| **ทนผลข้างเคียงไม่ได้** | **Switch** เป็นยาตัวใหม่ (replacement) |
| **ทั้งสองอย่างร่วมกัน** | **Prefer replacement** |

### Pseudoresistance — หกข้อที่ต้องคัดออกก่อน

| สาเหตุ | สิ่งที่ต้องทำ |
|---|---|
| **กินยาไม่สม่ำเสมอ (poor adherence)** | ถามแบบไม่ตัดสิน ตรวจ **serum concentration** |
| **เหตุการณ์ไม่ใช่การชักจริง (nonepileptic events)** | ทบทวนประวัติ พิจารณา **video-EEG** |
| **วินิจฉัยโรคลมชักผิดตั้งแต่ต้น** | กลับไปทบทวน semiology และประวัติจากผู้เห็นเหตุการณ์ |
| **เลือกยาผิดชนิดการชัก** | เช่นให้ CBZ ใน JME |
| **ขนาดยาไม่พอ** | ไต่ขนาดจนถึงขนาดสูงสุดที่ทนได้ ไม่ใช่แค่ถึงขนาดมาตรฐาน |
| **ปัจจัยวิถีชีวิต** | **อดนอน แอลกอฮอล์** |

> **การวัดระดับยาในเลือดช่วยบอกว่าไปถึงขนาดที่ออกฤทธิ์จริงหรือยัง** — สไลด์ระบุประโยคนี้ไว้ตรง ๆ และมีประโยชน์ที่สุดในสองสถานการณ์คือ สงสัยว่ากินยาไม่ครบ และสงสัยว่าขนาดยายังไม่พอ

### Replacement กับ Add-on

| | **Replacement monotherapy** | **Add-on therapy** |
|---|---|---|
| **เลือกเมื่อ** | ยาตัวแรก **ทนไม่ได้** หรือ **ไม่ได้ผลเลย** · ผู้ป่วยกินยาหลายตัวอยู่แล้ว · **ผู้ป่วยวัยเจริญพันธุ์** · มีปัญหาเรื่องการกินยาสม่ำเสมอ · ข้อจำกัดด้านค่าใช้จ่าย | ยาตัวแรก **ทนได้ดีและได้ผลบางส่วน** · ยาตัวใหม่ยังไม่มีข้อมูลใช้เป็น monotherapy |
| **ข้อสังเกต** | ต้องมี **ช่วงที่ใช้ยาสองตัวทับกันระหว่างเปลี่ยน** | เลือกยา **คนละกลไก** และ **เภสัชจลนศาสตร์เข้ากันได้** |

**ข้อห้ามที่สไลด์เน้น** — **อย่าใช้ sodium channel blocker สองตัวร่วมกัน** เพราะ **ผลข้างเคียงเพิ่มขึ้นแต่ประสิทธิผลลดลง**
""",
    ["ยาตัวแรกไม่ได้ผล ให้คัดกรอง pseudoresistance ก่อนเสมอ — หกข้อ",
     "วัดระดับยาในเลือดเพื่อดูว่าถึงขนาดที่ออกฤทธิ์จริงหรือกินยาไม่ครบ",
     "ทนยาไม่ได้ → เปลี่ยนตัว · ได้ผลบางส่วนแต่ทนได้ดี → เพิ่มตัวที่สอง",
     "ห้ามจับคู่ sodium channel blocker สองตัว — ผลข้างเคียงเพิ่ม ประสิทธิผลลด"],
    [
    mcq("NEU-EP-MCQ-19",
        "A 30-year-old man with focal epilepsy continues to have seizures on carbamazepine monotherapy at a modest dose. He reports no side effects. Before concluding that the drug has failed, which of the following should be done FIRST?",
        ["Add a second sodium channel blocker",
         "Systematically exclude pseudoresistance, including adherence, correct diagnosis, correct drug choice and adequate dosing",
         "Refer immediately for epilepsy surgery",
         "Start a ketogenic diet",
         "Implant a vagus nerve stimulator"],
        1,
        """สไลด์วางลำดับไว้ชัดว่า **"Rule Out Pseudoresistance First !!"** ก่อนจะสรุปว่ายาตัวแรกล้มเหลว

**หกข้อที่ต้องคัดออก**
1. **กินยาไม่สม่ำเสมอ** — สาเหตุที่พบบ่อยที่สุด ตรวจ **serum concentration** ช่วยได้
2. **เหตุการณ์ไม่ใช่การชักจริง**
3. **วินิจฉัยโรคลมชักผิด**
4. **เลือกยาผิดชนิดการชัก**
5. **ขนาดยาไม่พอ** — รายนี้ยังใช้ *modest dose* และ **ไม่มีผลข้างเคียง** แปลว่ายังไต่ขนาดขึ้นได้อีก
6. **ปัจจัยวิถีชีวิต** — อดนอน แอลกอฮอล์

**เคสนี้ชี้ชัดไปที่ข้อ 5** — ยังไม่ถึงขนาดสูงสุดที่ทนได้ จะเรียกว่าดื้อยายังไม่ได้

**ทำไมข้ออื่นผิด**
- **เพิ่ม sodium channel blocker ตัวที่สอง** ขัดกับคำแนะนำโดยตรง — *"Avoid: two sodium channel blockers together"*
- **ผ่าตัด, ketogenic diet, VNS** สงวนไว้สำหรับ **drug-resistant epilepsy** ซึ่งนิยามว่าล้มเหลวจาก **ยาที่เหมาะสม 2 ตัว ในขนาดที่เพียงพอ** — รายนี้ยังไม่ถึงเกณฑ์""",
        "ก่อนเรียกว่าดื้อยา ต้องแน่ใจว่า กินยาครบ · วินิจฉัยถูก · ยาถูกชนิด · ขนาดพอ",
        "Pseudoresistance",
        ["สไลด์ อ.พิมลพรรณ — After First ASM Fails: Decision Framework"]),
    mcq("NEU-EP-MCQ-20",
        "A woman of childbearing potential has focal epilepsy that is completely uncontrolled on her first ASM, which she also tolerates poorly. According to the framework presented, which strategy is preferred?",
        ["Add-on therapy with a second agent",
         "Replacement monotherapy with a different agent",
         "Triple therapy from the outset",
         "Continue the same drug at a lower dose",
         "Add a second sodium channel blocker"],
        1,
        """**Replacement monotherapy** คือทางเลือกที่สไลด์ระบุว่าเหมาะกว่า เมื่อมีข้อใดข้อหนึ่งต่อไปนี้

- ยาตัวแรก **ทนได้ไม่ดี** ✓ (รายนี้มี)
- ยาตัวแรก **ไม่ได้ผลเลย** ✓ (รายนี้มี)
- ผู้ป่วย **กินยาหลายตัวอยู่แล้ว**
- **ผู้ป่วยวัยเจริญพันธุ์** ✓ (รายนี้มี)
- มีปัญหาเรื่อง **การกินยาสม่ำเสมอ**
- **ข้อจำกัดด้านค่าใช้จ่าย**

รายนี้เข้าเงื่อนไขถึงสามข้อ จึงควรเปลี่ยนตัวยา ไม่ใช่เพิ่มตัวที่สอง โดย **ต้องมีช่วงที่ใช้ยาสองตัวทับกันระหว่างเปลี่ยน** เพื่อไม่ให้ชักกำเริบขณะลดยาเดิม

**เหตุผลเพิ่มเติมในผู้หญิงวัยเจริญพันธุ์** — การใช้ยาตัวเดียวลดความเสี่ยงความพิการแต่กำเนิดเมื่อเทียบกับหลายตัวร่วมกัน และต้องเลี่ยง **valproate** พร้อมให้ **folic acid** และวางแผนคุมกำเนิดที่ได้ผล

**ทำไมข้ออื่นผิด** — **add-on** เหมาะเมื่อยาตัวแรก *ทนได้ดีและได้ผลบางส่วน* ซึ่งตรงข้ามกับเคสนี้ · **triple therapy ตั้งแต่ต้น** ไม่มีที่ใช้ · **ลดขนาดยาเดิม** ยิ่งทำให้คุมการชักแย่ลง · **สอง sodium channel blocker** เป็นสิ่งที่สไลด์บอกให้หลีกเลี่ยง""",
        "ทนยาไม่ได้ + ไม่ได้ผลเลย + วัยเจริญพันธุ์ = เปลี่ยนตัวยาแบบ monotherapy ไม่ใช่เพิ่มยา",
        "Replacement vs add-on therapy",
        ["สไลด์ อ.พิมลพรรณ — Replacement vs Add-On Therapy", "Chen Z, et al. JAMA Neurol 2018;75(3):279-286"]),
    ])

# ─────────────────────────────────────────────────────────────── 12
sec("neuro-ep-12", "ดื้อยา การรักษาที่ไม่ใช่ยา และ SUDEP",
    "2 ใน 3 คุมได้ · ketogenic diet · VNS · ผ่าตัด · ลดความเสี่ยงตาย", 10,
"""### ตัวเลขที่ต้องจำ
- **ราว 2 ใน 3** ของผู้ป่วยโรคลมชักที่ยัง active **คุมการชักได้เป็นที่น่าพอใจด้วยยา**
- **ราว 1 ใน 3 ไม่สามารถคุมได้ด้วยยาเพียงอย่างเดียว** → **drug-resistant epilepsy** ซึ่งเป็นเหตุผลที่ยังต้องมีทางเลือกอื่น

### สามลำดับของการรักษา
1. **Monotherapy** — ยาตัวเดียวเลือกตามชนิดการชัก
2. **Combination therapy** — เพิ่มตัวที่สองเมื่อ monotherapy ล้มเหลว
3. **Advanced interventions** — ผ่าตัด, neurostimulation หรืออาหาร

### การรักษาที่ไม่ใช่ยา

**Ketogenic diet**
- อาหาร **ไขมันสูง คาร์โบไฮเดรตต่ำมาก** ทำให้เกิดภาวะ **ketosis**
- มีหลักฐานสนับสนุนใน **NICE guidelines** ว่าลดความถี่การชักใน drug-resistant epilepsy
- **ได้ผลดีเป็นพิเศษในเด็ก** แต่ผู้ใหญ่ก็ได้ประโยชน์
- **ต้องมีนักกำหนดอาหารเฉพาะทางดูแลและติดตาม**

**Vagus nerve stimulation (VNS)**
- อุปกรณ์ฝังคล้ายเครื่องกระตุ้นหัวใจ ส่งกระแสไฟฟ้าอ่อน ๆ ไปยังสมองผ่าน **เส้นประสาทเวกัส**
- **AAN guidelines รับรอง** ในผู้ป่วยที่เหมาะสม
- **ลดความถี่การชักได้ถึง 50% ในผู้ป่วยบางราย**
- **ไม่ได้ทำให้หายขาด** แต่เพิ่มคุณภาพชีวิตอย่างมีนัยสำคัญ

**Epilepsy surgery**
- สำหรับ **focal epilepsy ที่ดื้อยา** การผ่าตัดเอา focus ออกอาจทำให้ **หายจากการชักหรือลดลงมาก**
- **ใครได้ประโยชน์** — ผู้ที่มี **focus ชัดเจนและตัดออกได้อย่างปลอดภัยโดยไม่กระทบหน้าที่สำคัญของระบบประสาท**
- มี systematic review และ guideline สนับสนุนการส่งประเมินผ่าตัดในผู้ป่วยที่คัดเลือกมาอย่างเหมาะสม

### SUDEP — Sudden Unexpected Death in Epilepsy

**นิยาม** — การเสียชีวิต **ฉับพลัน ไม่คาดคิด ไม่ได้เกิดจากอุบัติเหตุหรือจมน้ำ** ในผู้ป่วยโรคลมชัก **โดยจะมีหรือไม่มีหลักฐานว่าเกิดการชักก็ได้ และไม่รวม status epilepticus**

**SUDEP เป็นสาเหตุการตายที่เกี่ยวข้องกับโรคลมชักที่พบบ่อยที่สุด**

**ปัจจัยเสี่ยงที่แก้ไขได้**

| ปัจจัยเสี่ยง | การจัดการ |
|---|---|
| **ชักตอนกลางคืน (nocturnal seizures)** | ปรับยาให้คุมการชักกลางคืน พิจารณาอุปกรณ์เฝ้าระวัง |
| **คุมการชักได้ไม่ดี** | เป็นปัจจัยที่แก้ไขได้มากที่สุด — เร่งปรับการรักษา |
| **นอนคนเดียว** | พิจารณาให้มีคนอยู่ด้วยหรือใช้ seizure alarm |

> **แพทย์ควรพูดเรื่อง SUDEP กับผู้ป่วยและผู้ดูแลอย่างเปิดเผย** ให้คำแนะนำความปลอดภัยที่เหมาะกับแต่ละราย และแนะนำแหล่งสนับสนุน — การไม่พูดถึงเพราะกลัวผู้ป่วยตกใจทำให้เสียโอกาสลดความเสี่ยงที่แก้ไขได้

### เป้าหมายสุดท้ายของการดูแล
สไลด์ปิดท้ายว่า **เป้าหมายของการดูแลโรคลมชักไม่ใช่แค่การคุมการชัก แต่คือการทำให้ผู้ป่วยทุกคนใช้ชีวิตได้อย่างเต็มที่ ปลอดภัย และมีความหมาย** ซึ่งต้องอาศัย

- **ทีมสหวิชาชีพ** — neurologist, epileptologist, พยาบาลเฉพาะทาง, นักกำหนดอาหาร, ศัลยแพทย์, นักจิตวิทยา
- **การตัดสินใจร่วมกับผู้ป่วยและผู้ดูแล**
- **ยึดแนวทางตามหลักฐาน** — NICE, ILAE, AAN, AES
- ดูแล **สุขภาพจิต** (ผู้ป่วยโรคลมชักมีภาวะซึมเศร้าและวิตกกังวลสูงกว่าคนทั่วไปชัดเจน) **การศึกษาและการทำงาน** และ **ความเป็นอยู่ของครอบครัวและผู้ดูแล**
""",
    ["2 ใน 3 คุมได้ด้วยยา · 1 ใน 3 ดื้อยา — กลุ่มหลังคือผู้ที่ต้องส่งประเมินทางเลือกอื่น",
     "Ketogenic diet ได้ผลดีเป็นพิเศษในเด็ก และต้องมีนักกำหนดอาหารดูแล",
     "VNS ลดการชักได้ถึง 50% ในบางราย แต่ไม่ทำให้หายขาด",
     "ผ่าตัดเหมาะกับ focal epilepsy ที่มี focus ชัดเจนและตัดออกได้ปลอดภัย",
     "SUDEP: ปัจจัยเสี่ยงที่แก้ได้คือ ชักกลางคืน คุมชักไม่ดี และนอนคนเดียว — ต้องพูดกับผู้ป่วยตรง ๆ"],
    [
    mcq("NEU-EP-MCQ-21",
        "Which of the following best describes the proportion of people with active epilepsy who achieve satisfactory seizure control with antiseizure medication?",
        ["About one-tenth", "About one-third", "About two-thirds", "Nearly all", "Fewer than 10%"],
        2,
        """**ประมาณสองในสาม (about two-thirds)** ของผู้ป่วยโรคลมชักที่ยัง active **คุมการชักได้เป็นที่น่าพอใจด้วยยา**

ส่วนที่เหลือ **ราวหนึ่งในสาม** จัดเป็น **drug-resistant (pharmacoresistant) epilepsy** ซึ่งเป็นเหตุผลที่ต้องมี **ketogenic diet, VNS และการผ่าตัด**

**นิยาม drug-resistant epilepsy (ILAE)** — ล้มเหลวจากการใช้ยากันชัก **ที่เลือกมาอย่างเหมาะสมและทนได้ จำนวน 2 สูตร** (ไม่ว่าจะเป็น monotherapy หรือ combination) **ในขนาดที่เพียงพอ** แล้วยังไม่ปลอดการชัก

> อย่าสับสนกับอีกเศษส่วนของคาบนี้: **ราว 1 ใน 3 ของผู้ป่วยหาสาเหตุไม่พบ (unknown aetiology)** — เป็นคนละเรื่อง""",
        "2/3 คุมได้ด้วยยา · 1/3 ดื้อยา และ 1/3 (คนละชุด) หาสาเหตุไม่พบ",
        "Drug-resistant epilepsy",
        ["สไลด์ อ.พิมลพรรณ — Treatment Strategies", "Kwan P, et al. Epilepsia 2010;51:1069-1077"]),
    mcq("NEU-EP-MCQ-22",
        "Which of the following is a recognised MODIFIABLE risk factor for sudden unexpected death in epilepsy (SUDEP)?",
        ["Male sex",
         "Poorly controlled seizures, particularly nocturnal seizures",
         "Age at epilepsy onset",
         "Family history of epilepsy",
         "Presence of an aura before seizures"],
        1,
        """สไลด์ระบุปัจจัยเสี่ยงที่ **แก้ไขได้** ของ SUDEP ไว้สามข้อ

1. **Nocturnal seizures** — ชักตอนกลางคืน
2. **Poor seizure control** — คุมการชักได้ไม่ดี
3. **Sleeping alone** — นอนคนเดียว

ทั้งสามข้อนี้ชี้ไปทางเดียวกันคือ **การคุมการชักให้ได้ดีขึ้น โดยเฉพาะการชักกลางคืน คือมาตรการลดความเสี่ยงที่ทำได้จริง** ร่วมกับการพิจารณาให้มีคนอยู่ด้วยหรือใช้ seizure alarm

**นิยาม SUDEP** — เสียชีวิต **ฉับพลัน ไม่คาดคิด ไม่ใช่จากอุบัติเหตุหรือจมน้ำ** ในผู้ป่วยโรคลมชัก **จะมีหรือไม่มีหลักฐานว่าเกิดการชักก็ได้ และไม่รวม status epilepticus** — เป็น **สาเหตุการตายที่เกี่ยวกับโรคลมชักที่พบบ่อยที่สุด**

**ทำไมข้ออื่นผิด** — เพศ อายุที่เริ่มเป็น และประวัติครอบครัว เป็นปัจจัยที่ **แก้ไขไม่ได้** ส่วน **การมี aura ไม่ใช่ปัจจัยเสี่ยงของ SUDEP**

**สิ่งที่แพทย์ต้องทำ** — สไลด์ย้ำว่าควร **พูดเรื่อง SUDEP กับผู้ป่วยและผู้ดูแลอย่างเปิดเผย** พร้อมให้คำแนะนำความปลอดภัยเฉพาะราย""",
        "ลดความเสี่ยง SUDEP = คุมการชักให้ได้ โดยเฉพาะชักกลางคืน — และต้องพูดเรื่องนี้กับผู้ป่วยตรง ๆ",
        "SUDEP",
        ["สไลด์ อ.พิมลพรรณ — Reducing Risk of Mortality, Including SUDEP"]),
    mcq("NEU-EP-MCQ-23",
        "A 29-year-old man has drug-resistant focal epilepsy. MRI shows a well-defined right mesial temporal sclerosis and video-EEG confirms all seizures arise from the same region. Neuropsychological testing suggests resection would not impair critical function. Which option offers the greatest chance of seizure freedom?",
        ["Adding a third antiseizure medication",
         "Vagus nerve stimulation",
         "Ketogenic diet",
         "Resective epilepsy surgery",
         "Increasing the dose of the current regimen beyond tolerability"],
        3,
        """**ผู้ป่วยรายนี้คือ "ตัวเลือกที่ดีที่สุด" สำหรับการผ่าตัด** — สไลด์ระบุเงื่อนไขไว้ว่า *"Patients with a clearly identifiable seizure focus that can be safely removed without affecting critical neurological function"*

เคสนี้ครบทุกข้อ
- **ดื้อยาแล้ว** (drug-resistant focal epilepsy)
- **focus ชัดเจนข้างเดียว** — right mesial temporal sclerosis บน MRI
- **video-EEG ยืนยันว่าการชักทุกครั้งมาจากตำแหน่งเดียวกัน**
- **ตัดออกได้ปลอดภัย** ตามผลประเมิน neuropsychology

**ทำไมทางเลือกอื่นด้อยกว่า**

| ทางเลือก | ข้อจำกัด |
|---|---|
| **เพิ่มยาตัวที่สาม** | เมื่อล้มเหลวจากยาที่เหมาะสม 2 สูตรแล้ว **โอกาสปลอดการชักจากยาตัวถัดไปต่ำมาก** |
| **VNS** | **ไม่ทำให้หายขาด** ลดความถี่ได้ถึง 50% ในบางราย — ใช้เมื่อ**ไม่ใช่ผู้ที่ผ่าตัดได้** |
| **Ketogenic diet** | เป็น adjunct **ได้ผลดีเป็นพิเศษในเด็ก** ไม่ใช่ทางไปสู่การหายขาดในเคสนี้ |
| **เพิ่มขนาดยาเกินที่ทนได้** | ขัดหลักการรักษา ทำให้เกิดพิษจากยา |

> การส่งประเมินผ่าตัดมัก **ช้าเกินไปหลายปี** ทั้งที่ผู้ป่วยเข้าเกณฑ์แล้ว — เมื่อยาสองสูตรล้มเหลว ให้คิดถึงการส่งต่อศูนย์โรคลมชักทันที""",
        "ดื้อยา + focus ชัดเจนข้างเดียว + ตัดออกได้ปลอดภัย = ส่งประเมินผ่าตัด อย่ารอเพิ่มยาไปเรื่อย ๆ",
        "Epilepsy surgery",
        ["สไลด์ อ.พิมลพรรณ — Epilepsy Surgery: A Potential Solution"]),
    ])

# ─────────────────────────────────────────────────────────── MEQ
MEQ = [{
 "id": "NEU-MEQ-02", "part": "MEQ", "lec": "23/9", "lecture": "Epilepsy",
 "topic": "First unprovoked seizure — classification, workup and counselling",
 "vignette": """ชายไทยอายุ 19 ปี นักศึกษาชั้นปีที่ 1 ถูกเพื่อนนำส่งห้องฉุกเฉินหลังชักเกร็งกระตุกทั้งตัว 1 ครั้ง
PI: 1 ชั่วโมงก่อนมาโรงพยาบาล ขณะนั่งอ่านหนังสือในห้องสมุดช่วงเช้า เพื่อนเห็นผู้ป่วยแขนสองข้างสะดุ้งขึ้นสองสามครั้ง หนังสือหลุดมือ จากนั้นล้มลง เกร็งทั้งตัวประมาณ 20 วินาที แล้วกระตุกเป็นจังหวะทั้งสี่แขนขานานประมาณ 1 นาที มีน้ำลายฟูมปาก กัดลิ้นด้านข้าง ปัสสาวะราด หลังหยุดชักผู้ป่วยหลับและปลุกตื่นยาก สับสนพูดไม่รู้เรื่องอยู่ประมาณ 20 นาที
ประวัติเพิ่มเติม: คืนก่อนหน้าอ่านหนังสือสอบทั้งคืนไม่ได้นอนเลย และดื่มเบียร์กับเพื่อนเมื่อสองคืนก่อน เมื่อซักลึกผู้ป่วยยอมรับว่า 2 ปีที่ผ่านมา มักมีอาการ "สะดุ้ง" ที่แขนทั้งสองข้างในช่วง 1-2 ชั่วโมงแรกหลังตื่นนอน บางครั้งทำแปรงสีฟันหรือแก้วน้ำหล่น เป็นอยู่ไม่กี่วินาทีแล้วหาย ไม่เคยบอกใครเพราะคิดว่าเป็นเรื่องปกติของคนง่วง ไม่เคยหมดสติมาก่อน
U/D: ปฏิเสธโรคประจำตัว ไม่ได้ใช้ยาใด ๆ ปฏิเสธการใช้สารเสพติด
FHx: ลูกพี่ลูกน้องฝ่ายมารดาเคยชักตอนวัยรุ่น ไม่ทราบรายละเอียด
PE: GA: ง่วงซึมเล็กน้อยแต่ปลุกตื่น ตอบคำถามได้ถูกต้องแล้ว
V/S: BT 37.2 C, PR 92/min, RR 18/min, BP 124/76 mmHg, SpO2 98% room air
HEENT: มีรอยกัดที่ด้านข้างลิ้นซ้าย
Neuro: รู้สึกตัวดี ไม่มี neck stiffness, cranial nerves ปกติ, motor power grade V ทั้งสี่แขนขาเท่ากันสองข้าง, DTR ปกติ, Babinski negative ทั้งสองข้าง, ไม่มี focal deficit
Lab แรกรับ: capillary glucose 104 mg/dL, Na 140, K 3.9, Ca และ Mg ปกติ, CBC ปกติ, urine toxicology negative""",
 "questions": [
  {"q": "1. จงจำแนกการชักครั้งนี้และให้การวินิจฉัยกลุ่มอาการที่น่าจะเป็นมากที่สุด พร้อมเหตุผล",
   "a": """**การจำแนก** — เริ่มเป็น **myoclonic seizure (generalized onset)** ที่แขนสองข้าง แล้วดำเนินต่อเป็น **generalized tonic-clonic seizure**

**การวินิจฉัย** — **Juvenile Myoclonic Epilepsy (JME)**

**เหตุผลที่สนับสนุน**
- **อายุ 19 ปี** อยู่ในช่วงยอดของ JME (12–18 ปี เฉลี่ย ~15 ปี แต่เริ่มได้ถึง 36 ปี)
- **ประวัติ myoclonic jerk ที่แขนสองข้างในช่วงเช้าหลังตื่นนอนมา 2 ปี** — เป็นอาการหลักของ JME และตรงกับที่สไลด์ระบุว่า **myoclonic jerk นำหน้า GTC ครั้งแรกโดยเฉลี่ย 3.3 ปี**
- **วันนี้มี myoclonic jerk นำก่อนแล้วจึงเกิด GTC** ซึ่งเป็นลำดับแบบฉบับ
- **ตัวกระตุ้นครบ** — **อดนอนทั้งคืน** (ตัวกระตุ้นที่แรงและสม่ำเสมอที่สุด) ร่วมกับ **แอลกอฮอล์** เมื่อสองคืนก่อน (rebound effect)
- **เกิดในช่วงเช้า** ซึ่งเป็นเวลาที่ JME มักมีอาการ
- **ประวัติครอบครัวชักในวัยรุ่น** เข้ากับสาเหตุทางพันธุกรรม
- **ตรวจร่างกายระบบประสาทปกติ ไม่มี focal deficit** และ **ไม่มี Todd's paralysis** สนับสนุน generalized onset

**เข้าเกณฑ์โรคลมชักข้อใด** — เข้า **เกณฑ์ ILAE ข้อ 3 (วินิจฉัยเป็น epilepsy syndrome)** จึงวินิจฉัยโรคลมชักได้แม้ GTC เพิ่งเกิดครั้งแรก เพราะ **myoclonic jerk ที่เป็นมา 2 ปีก็คือการชัก** ผู้ป่วยจึงมีการชัก unprovoked หลายครั้งอยู่แล้ว (เข้าเกณฑ์ข้อ 1 ด้วย)"""},
  {"q": "2. จงระบุการสืบค้นที่ควรทำ พร้อมบอกผลที่คาดว่าจะพบ และอธิบายว่าจะแปลผลอย่างไรหากผลออกมาปกติ",
   "a": """**1) EEG — การตรวจที่สำคัญที่สุด**
- ผลที่คาดว่าจะพบใน JME: **generalized 4–6 Hz polyspike-and-wave discharge** ขึ้นพร้อมกันทุก electrode
- ควรทำร่วมกับ **activation procedures** — **photic stimulation** (JME มี photosensitivity **30–40%**) และ hyperventilation
- ถ้า EEG ครั้งแรกปกติ ให้ทำ **sleep-deprived EEG** หรือบันทึกขณะหลับ หรือบันทึกซ้ำ

**2) MRI สมอง**
- ผลที่คาดว่าจะพบใน JME: **ปกติ** ซึ่ง **เข้ากันได้กับ generalized epilepsy** ตามที่สไลด์ระบุว่า *"In generalized epilepsy, MRI is often normal, pointing towards genetic or metabolic etiologies"*
- ยังควรทำเพื่อ **ตัดรอยโรคโครงสร้าง** ออก เพราะประวัติจากผู้เห็นเหตุการณ์อาจพลาด focal onset ที่ลามเป็นสองซีก

**3) การตรวจที่ทำไปแล้วและต้องมีเสมอในผู้ป่วยชักครั้งแรก**
- **capillary glucose** (ทำแล้ว 104) · **electrolytes: Na, Ca, Mg** (ปกติ) · **CBC** · **urine toxicology** (negative)
- การตรวจชุดนี้มีไว้เพื่อ **คัดกรอง provoked (acute symptomatic) seizure** ซึ่งรายนี้ตัดออกไปแล้วทั้งหมด

**การแปลผลเมื่อผลปกติ — ประเด็นที่สำคัญที่สุด**
> **EEG ปกติ ไม่ตัดโรคลมชักออก** และ **EEG ผิดปกติอย่างเดียวก็วินิจฉัยโรคลมชักไม่ได้** — ทั้ง EEG และ MRI เป็นเพียง **ตัวสนับสนุน** การวินิจฉัยโรคลมชัก **ยังคงเป็นการวินิจฉัยทางคลินิกจากประวัติ** โดยเฉพาะประวัติจากผู้เห็นเหตุการณ์

ดังนั้นแม้ EEG และ MRI จะปกติทั้งคู่ **ก็ยังวินิจฉัย JME และเริ่มการรักษาได้** จากประวัติ myoclonic jerk 2 ปี + GTC"""},
  {"q": "3. จงวางแผนการรักษาด้วยยา โดยระบุยาที่เลือก ยาที่ต้องหลีกเลี่ยง และเหตุผลเชิงกลไก",
   "a": """**หลักการ** — สไลด์ย้ำว่า **"ASM choice should be matched to the seizure type, epilepsy type or epileptic syndrome"** JME เป็น **idiopathic generalized epilepsy** ที่มีการชักหลายชนิดร่วมกัน (myoclonic + GTC ± absence) จึงต้องเลือกยาที่ครอบคลุม **broad spectrum**

**ยาที่เลือก**
- **Valproate (VPA)** — ได้ผลดีที่สุดใน JME ครอบคลุมทั้ง myoclonic, GTC และ absence · NICE 2020 ให้ **VPA เป็นตัวแรกของ GTC**
- **ทางเลือกอื่น** — **levetiracetam** (ได้ผลดีกับ myoclonic) หรือ **topiramate** · **lamotrigine** ใช้ได้กับ GTC แต่ **อาจทำให้ myoclonic jerk แย่ลงในบางราย** จึงต้องเฝ้าระวัง
- ผู้ป่วยรายนี้เป็น **ชาย** จึงใช้ VPA ได้โดยไม่ติดข้อจำกัดเรื่อง teratogenicity แต่ต้องแจ้งผลข้างเคียง (น้ำหนักขึ้น ผมร่วง ตับ เกล็ดเลือด อาการสั่น)

**ยาที่ต้องหลีกเลี่ยงเด็ดขาด — และเหตุผล**

| ยา | ผลเสีย |
|---|---|
| **Carbamazepine, oxcarbazepine, phenytoin** | **ทำให้ myoclonic และ absence แย่ลง** (seizure aggravation) |
| **Gabapentin, pregabalin** | ทำให้ generalized seizure แย่ลง |
| **Vigabatrin, tiagabine** | อาจกระตุ้น absence status |

**กลไก** — ยา **sodium channel blocker** ออกฤทธิ์ดีกับ focal seizure ที่มีจุดกำเนิดเฉพาะที่ แต่ใน idiopathic generalized epilepsy ซึ่งพยาธิสภาพอยู่ที่ **thalamocortical circuit** การปิดช่องโซเดียมไม่ได้แก้ที่กลไกหลัก และยังไปลดการยับยั้งในวงจรดังกล่าว ทำให้ **myoclonic jerk และ absence ถี่ขึ้น**

**ระยะเวลา** — ต้องอธิบายว่า **JME มักต้องใช้ยาระยะยาว** ต่างจาก SeLECTS ที่หายเองเมื่ออายุ 16"""},
  {"q": "4. จงให้คำแนะนำก่อนจำหน่าย ครอบคลุมการปรับวิถีชีวิต ความปลอดภัย และการติดตาม",
   "a": """**1) ควบคุมตัวกระตุ้น — มีน้ำหนักเทียบเท่าการปรับยาในผู้ป่วย JME**
- **นอนให้พอและเป็นเวลาทุกคืน** — **อดนอนคือตัวกระตุ้นที่แรงและสม่ำเสมอที่สุด** ย้ำเป็นพิเศษช่วงสอบ ห้ามอ่านหนังสือทั้งคืน
- **งดหรือจำกัดแอลกอฮอล์** — อันตรายอยู่ที่ **rebound effect ในเช้าวันถัดมา** ไม่ใช่ขณะดื่ม
- **จัดการความเครียด** ทั้งทางอารมณ์และทางกาย
- **ระวังแสงกะพริบ** — ผู้ป่วย JME **30–40% มี photosensitivity** เลี่ยงเกมหรือผับที่มีไฟกะพริบ นั่งห่างจอ ใช้แสงสว่างในห้องเพียงพอ

**2) ความปลอดภัยในชีวิตประจำวัน**
- **ห้ามขับรถ** จนกว่าจะปลอดการชักตามระยะเวลาที่กำหนด และปรึกษาแพทย์ก่อนกลับไปขับ
- **ห้ามว่ายน้ำคนเดียว** ควรอาบน้ำด้วยฝักบัวแทนการแช่อ่าง
- เลี่ยง **ทำงานที่สูง ใกล้เครื่องจักร หรือใกล้ไฟ** ขณะยังไม่ปลอดการชัก
- **สอนเพื่อนและครอบครัววิธีปฐมพยาบาลขณะชัก** — จับนอนตะแคง ป้องกันศีรษะกระแทก **ห้ามงัดปากหรือใส่อะไรเข้าปาก** จับเวลา และโทร 1669 เมื่อชักนานเกิน 5 นาทีหรือชักซ้ำโดยไม่ฟื้น

**3) การกินยา**
- **ต้องกินสม่ำเสมอ ห้ามหยุดยาเอง** — การขาดยาเป็นสาเหตุที่พบบ่อยที่สุดของการชักซ้ำและของ **pseudoresistance**
- อธิบายผลข้างเคียงที่ต้องมาพบแพทย์ทันที

**4) SUDEP**
- **พูดเรื่อง SUDEP อย่างเปิดเผย** ตามที่สไลด์แนะนำ โดยเน้นว่า **ปัจจัยเสี่ยงที่แก้ไขได้คือ การคุมการชักให้ดี โดยเฉพาะการชักกลางคืน และการนอนคนเดียว**
- สำหรับนักศึกษาที่อยู่หอพักคนเดียว ควรพิจารณา **ให้มีคนรู้เรื่องและติดต่อได้** หรือใช้ seizure alarm

**5) สุขภาพจิตและการเรียน**
- คัดกรอง **ภาวะซึมเศร้าและวิตกกังวล** ซึ่งพบในผู้ป่วยโรคลมชักสูงกว่าคนทั่วไปชัดเจน
- ให้ข้อมูลเรื่องผลกระทบต่อการเรียนและการทำงาน และแหล่งสนับสนุน

**6) การติดตาม**
- นัด **EEG และประเมินผลการรักษา** ติดตามความถี่ของ myoclonic jerk เป็นตัวชี้วัด
- **ให้ผู้ป่วยจดบันทึกการชัก (seizure diary)** รวมทั้งชั่วโมงการนอน"""}],
 "ref": ["สไลด์ อ.พิมลพรรณ เลี่ยนเครือ — Epilepsy: Understanding and Navigating a Complex Neurological Condition",
         "ILAE classification and definition of epilepsy syndromes at variable age. Epilepsia 2022;63:1443-1474",
         "NICE guideline NG217 Epilepsies in children, young people and adults (2022)"],
 "nl": ["2.3.6"], "years": [], "_kind": "meq", "_set": "neuro"}]

# ────────────────────────────────────────────────────────── OSCE
OSCE = [{
 "id": "NEU-OSCE-02", "part": "OSCE/SAQ", "lec": "23/9", "lecture": "Epilepsy",
 "topic": "OSCE – ซักประวัติผู้ป่วยที่มาด้วยเหตุการณ์หมดสติ เพื่อแยกชักจริงออกจากภาวะที่เหมือนชัก",
 "station": "สถานีซักประวัติผู้ป่วยจำลอง 8 นาที",
 "instruction": """ชายอายุ 22 ปี มาที่แผนกผู้ป่วยนอกพร้อมมารดา ด้วยเรื่อง "วูบหมดสติ" เมื่อสัปดาห์ก่อน
คำสั่ง: จงซักประวัติจากผู้ป่วยและผู้เห็นเหตุการณ์ เพื่อแยกว่าเป็นการชักจริงหรือภาวะที่เหมือนชัก และสรุปแนวทางให้ผู้ป่วยฟังในช่วงท้าย (ไม่ต้องตรวจร่างกาย)

หมายเหตุสำหรับผู้ป่วยจำลอง: ขณะยืนเข้าแถวรอซื้ออาหารในวันที่อากาศร้อนจัด รู้สึกหน้ามืด ตาลาย หูอื้อ เหงื่อแตก คลื่นไส้ ประมาณ 15 วินาที แล้วทรุดลง มารดาซึ่งอยู่ด้วยเห็นว่าตัวกระตุกไม่เป็นจังหวะประมาณ 5-10 วินาที ตาเปิดค้าง ไม่มีกัดลิ้น มีปัสสาวะเล็ดเล็กน้อย ลุกขึ้นนั่งได้และคุยรู้เรื่องภายในประมาณ 15 วินาที ไม่สับสน ไม่ปวดเมื่อยตัวในวันถัดมา เคยเป็นลักษณะนี้มาแล้ว 2 ครั้งในรอบ 3 ปี ทุกครั้งขณะยืนนาน ๆ หรือเห็นเข็มฉีดยา""",
 "answer": """**สิ่งที่ต้องซักให้ได้ (คะแนนเต็ม 20)**

**1. บริบทและอาการนำก่อนเหตุการณ์ (5 คะแนน)**
- **กำลังทำอะไรอยู่** — ยืน นั่ง นอน ออกแรง หรือขณะหลับ (**ยืนนาน อากาศร้อน = เข้าได้กับ vasovagal**)
- **มีอาการนำหรือไม่ และเป็นแบบใด**
  - **หน้ามืด ตาลาย หูอื้อ เหงื่อแตก คลื่นไส้ = presyncope** ✓ รายนี้มี
  - **จุกแน่นลิ้นปี่ลอยขึ้น, déjà vu, ได้กลิ่นแปลก, กลัวฉับพลัน = aura ของการชัก** — ต้องถามหาโดยเฉพาะ
- **อาการนำเหมือนกันทุกครั้งหรือไม่** (stereotyped → ชัก)
- **ตัวกระตุ้น** — ยืนนาน อากาศร้อน เจ็บ เห็นเลือดหรือเข็ม ไอ ถ่ายปัสสาวะ (syncope) เทียบกับ **อดนอน แอลกอฮอล์ แสงกะพริบ** (ชัก)

**2. รายละเอียดขณะเกิดเหตุ — ต้องถามจากผู้เห็นเหตุการณ์ (6 คะแนน)**
- **ระยะเวลาของการกระตุก** — **< 15 วินาที เข้าได้กับ convulsive syncope** เทียบกับ **1–2 นาที ของ GTC** ✓ รายนี้ 5–10 วินาที
- **ลักษณะการกระตุก** — **ไม่เป็นจังหวะ จำนวนครั้งน้อย (syncope)** เทียบกับ **เกร็งก่อนแล้วกระตุกเป็นจังหวะและช้าลงเรื่อย ๆ (ชัก)** ✓
- **ตาเปิดหรือปิด** — **ชักจริงลืมตาค้าง · PNES หลับตาแน่นและต้านการเปิด** ✓ รายนี้ตาเปิด
- **หน้าหรือตาเบือนไปข้างใดข้างหนึ่งก่อนหรือไม่** (version → focal onset)
- **เริ่มกระตุกที่ส่วนใดของร่างกายก่อน** และลามอย่างไร
- **สีหน้า** — ซีดเหงื่อแตก (syncope) เทียบกับ เขียวคล้ำ (ชัก)

**3. อาการหลังเหตุการณ์ — ตัวแยกที่มีน้ำหนักที่สุด (4 คะแนน)**
- **ฟื้นเร็วแค่ไหน** — **รู้ตัวเต็มที่ภายในวินาที = syncope** ✓ เทียบกับ **สับสน ง่วงซึม หลายนาทีถึงชั่วโมง = post-ictal ของ GTC**
- **มี Todd's paralysis หรือไม่** — แขนขาอ่อนแรงข้างเดียวหลังฟื้น
- **ปวดเมื่อยกล้ามเนื้อในวันถัดมาหรือไม่** ✓ รายนี้ไม่มี (หลัง GTC มักปวดเมื่อยและ CK สูง)
- **กัดลิ้นหรือไม่ และตรงไหน** — **ด้านข้างลิ้นมี specificity สูงสำหรับการชักจริง** ✓ รายนี้ไม่มี

**4. ประวัติซ้ำและประวัติเพิ่มเติม (3 คะแนน)**
- **เคยเป็นมากี่ครั้ง ในสถานการณ์เดียวกันหรือไม่** ✓ รายนี้ 2 ครั้ง ทุกครั้งขณะยืนนานหรือเห็นเข็ม
- **ประวัติสะดุ้งตอนเช้า (myoclonic jerk)** และ **เหม่อค้าง (absence)** — ต้องถามตรง ๆ เพราะผู้ป่วยไม่เล่าเอง
- **ประวัติชักในวัยเด็ก ชักจากไข้ อุบัติเหตุทางสมอง การติดเชื้อระบบประสาท stroke**
- **ประวัติครอบครัว** — โรคลมชัก และ **การเสียชีวิตเฉียบพลันในคนอายุน้อย** (คัดกรองสาเหตุหัวใจของ syncope)
- **ยาและสารที่ใช้** — ยาลดความดัน ยาจิตเวช แอลกอฮอล์ สารเสพติด

**5. คัดกรองสาเหตุจากหัวใจ — ข้อที่ห้ามลืม (2 คะแนน)**
- **วูบขณะออกแรงหรือขณะนอนราบหรือไม่**
- **ใจสั่น เจ็บหน้าอก เหนื่อยง่าย ก่อนวูบหรือไม่**
- **ไม่มีอาการนำเลยแล้ววูบทันที** (คิดถึง arrhythmia)
- **ประวัติครอบครัวเสียชีวิตกะทันหันอายุน้อยกว่า 40 ปี**

**สรุปที่ควรบอกผู้ป่วยในช่วงท้าย**
- ลักษณะทั้งหมดเข้าได้กับ **convulsive syncope (เป็นลมแล้วมีกระตุก) จากกลไก vasovagal** **ไม่ใช่การชักจากโรคลมชัก** โดยเหตุผลหลักคือ **มีอาการนำแบบหน้ามืด กระตุกสั้นมาก และรู้ตัวเต็มที่ทันทีโดยไม่สับสน**
- อธิบายว่า **การกระตุกเกิดได้ในคนเป็นลม** เพราะสมองขาดเลือดชั่วคราว **ไม่ได้แปลว่าเป็นโรคลมชัก** และ **การปัสสาวะเล็ดก็เกิดได้ทั้งสองภาวะ จึงใช้แยกไม่ได้**
- **ยังต้องตรวจเพิ่ม** — วัดความดันท่านอนและท่ายืน (orthostatic) และ **ตรวจคลื่นไฟฟ้าหัวใจ (EKG)** เพื่อคัดกรองสาเหตุจากหัวใจซึ่งเป็นกลุ่มที่อันตราย
- **คำแนะนำป้องกัน** — ดื่มน้ำให้พอ ไม่ยืนนานในที่ร้อน **รู้จักอาการเตือนแล้วรีบนั่งหรือนอนยกขาสูงทันที** และทำ counter-pressure manoeuvre (เกร็งกล้ามเนื้อขา ไขว้ขา บีบมือ)
- **บอกอาการที่ต้องกลับมาพบแพทย์** — วูบขณะออกแรง วูบโดยไม่มีอาการนำ ใจสั่นนำ สับสนนานหลังฟื้น หรือกัดลิ้นด้านข้าง
- **ยังไม่ต้องเริ่มยากันชัก** และอธิบายเหตุผลให้ผู้ป่วยและมารดาเข้าใจ""",
 "ref": ["สไลด์ อ.พิมลพรรณ — Seizure mimic / Differential diagnosis",
         "Harrison 21st ed., Syncope and Seizures"],
 "nl": ["2.3.6", "2.1.4"], "years": [], "_kind": "meq", "_set": "neuro"}]

LECTURE = {
 "lec": "23/9",
 "title": "Epilepsy — จำแนก วินิจฉัย และเลือกยาให้ตรงชนิดการชัก",
 "subtitle": "ชักกับโรคลมชักต่างกันอย่างไร · seizure mimics · focal กับ generalized · กลุ่มอาการ SeLECTS, CAE, JME · DEEs · EEG และ MRI · เลือก ASM ตามชนิดการชัก · pseudoresistance · ketogenic diet, VNS, ผ่าตัด · SUDEP",
 "objectives": [
   "แยก seizure (เหตุการณ์) ออกจาก epilepsy (โรค) และใช้เกณฑ์ ILAE ทั้งสามข้อได้ถูกต้อง",
   "แยกการชักจริงออกจาก convulsive syncope และ PNES ด้วยระยะเวลา ลักษณะตา และ post-ictal confusion",
   "จำแนกการชักเป็น focal / generalized / unknown onset และระบุ semiology ที่บอกตำแหน่งรอยโรคได้",
   "จดจำกลุ่มอาการที่พบบ่อย — SeLECTS, CAE, JME — และ DEEs ที่สำคัญคือ Dravet และ Lennox-Gastaut",
   "แปลผล EEG และ MRI โดยเข้าใจว่าทั้งคู่เป็นตัวสนับสนุน ไม่ใช่ตัววินิจฉัย",
   "เลือกยากันชักให้ตรงกับชนิดการชัก และรู้ว่ายาใดทำให้ generalized seizure แย่ลง",
   "คัดกรอง pseudoresistance ก่อนสรุปว่าดื้อยา และเลือกระหว่าง replacement กับ add-on ได้",
   "ระบุผู้ป่วยที่ควรส่งประเมินการผ่าตัด และให้คำแนะนำเรื่องความเสี่ยง SUDEP ที่แก้ไขได้"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ───────────────────────────────────────────────────────── merge
path = os.path.join(BUILD, "data", "neuro.json")
data = json.load(open(path, encoding="utf-8"))
data = [l for l in data if l.get("lec") != LECTURE["lec"]]      # idempotent
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "neuro":
        m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

n_items = sum(len(s["items"]) for s in S)
print("sections %d | items %d | meq %d | osce %d" % (len(S), n_items, len(MEQ), len(OSCE)))
print("neuro.json ตอนนี้มี %d คาบ · %d bytes" % (len(data), os.path.getsize(path)))
