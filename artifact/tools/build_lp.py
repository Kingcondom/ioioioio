#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""หัตถการ: Lumbar puncture + Eye examination (อ.พิมลพรรณ เลี่ยนเครือ) → data/neuro.json"""
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

sec("neuro-lp-01", "ข้อบ่งชี้ของการเจาะหลัง",
    "แบ่งเป็นเพื่อวินิจฉัย กับเพื่อการรักษา", 8,
"""สไลด์แบ่งข้อบ่งชี้ออกเป็นสองกลุ่มใหญ่ — **เพื่อวินิจฉัย (diagnosis)** และ **เพื่อการรักษา (therapeutic maneuver)**

### เพื่อวินิจฉัย

**1) การติดเชื้อในระบบประสาท**
- **Meningitis / cerebritis** จาก **แบคทีเรีย ไวรัส เชื้อรา และปรสิต**
- **CNS syphilis**

**2) การอักเสบของระบบประสาทส่วนกลางและส่วนปลาย**
- **Autoimmune encephalitis**
- **Multiple sclerosis**
- **Guillain-Barré syndrome (GBS)**
- **Chronic inflammatory demyelinating polyneuropathy (CIDP)**
- **Paraneoplastic syndromes**
- **Neurosarcoidosis**
- **CNS vasculitis**

**3) มะเร็ง**
- **Carcinomatous meningitis**
- **CNS lymphoma**

**4) ข้อบ่งชี้อื่น**
- **สงสัย subarachnoid hemorrhage ในผู้ป่วยที่ CT เป็นลบ** ← ข้อบ่งชี้คลาสสิกที่ออกสอบบ่อย
- **Idiopathic intracranial hypertension (IIH)**
- **Intracranial hypotension**
- **Normal pressure hydrocephalus (NPH)**

### เพื่อการรักษา
- **Spinal anesthesia**
- **การให้ยาเคมีบำบัดหรือยาปฏิชีวนะเข้าช่องน้ำไขสันหลัง (intrathecal administration)**

### กรอบคิดที่สไลด์วางไว้ก่อนเข้าเรื่อง
ก่อนจะตัดสินใจเจาะหลัง ให้ตอบสองคำถามเสมอ
- **Where is the lesion?** — อยู่ที่ระบบประสาทกลาง (สมอง ไขสันหลัง) หรือส่วนปลาย (เส้นประสาทสมอง รากประสาท เส้นประสาทส่วนปลาย NMJ กล้ามเนื้อ)
- **What is the lesion?** — **Infection · Vascular · Inflammation · Tumor · Degeneration · Hereditary · Toxic/Metabolic**

น้ำไขสันหลังตอบได้ดีเป็นพิเศษกับกลุ่ม **infection, inflammation และ tumor** และตอบได้บางส่วนกับ **vascular (SAH)**
""",
    ["ข้อบ่งชี้แบ่งสองกลุ่ม: เพื่อวินิจฉัย กับเพื่อการรักษา",
     "สงสัย SAH แต่ CT เป็นลบ = ข้อบ่งชี้คลาสสิกของการเจาะหลัง",
     "LP ตอบได้ดีกับกลุ่ม infection, inflammation และ tumor",
     "GBS และ CIDP เป็นข้อบ่งชี้ของการเจาะหลังทั้งคู่ แม้เป็นโรคของเส้นประสาทส่วนปลาย"],
    [
    mcq("NEU-LP-MCQ-01",
        "A 44-year-old woman presents 8 hours after a sudden severe 'worst headache of my life'. Non-contrast CT brain is normal. Which of the following is the most appropriate next step?",
        ["Reassure and discharge because CT is normal",
         "Lumbar puncture to look for subarachnoid haemorrhage",
         "MRI brain without contrast in 1 week",
         "Start prophylactic nimodipine without further testing",
         "Repeat CT brain in 24 hours"],
        1,
        """**สงสัย subarachnoid hemorrhage ในผู้ป่วยที่ CT เป็นลบ = ข้อบ่งชี้ของการเจาะหลัง** ตามที่สไลด์ระบุไว้โดยตรง

**เหตุผล** — ความไวของ CT ต่อ SAH **ลดลงตามเวลา** สูงมากในช่วง 6 ชั่วโมงแรก แต่ลดลงเรื่อย ๆ หลังจากนั้น การที่ CT เป็นลบจึง **ไม่ตัด SAH ออก** โดยเฉพาะเมื่อประวัติเข้าได้ชัดเจน (thunderclap headache)

**สิ่งที่มองหาใน CSF**
- **Xanthochromia** — น้ำไขสันหลังสีเหลืองจากการสลายของฮีโมโกลบิน เป็นหลักฐานที่จำเพาะกว่า และ **ต้องใช้เวลาราว 12 ชั่วโมงหลังเลือดออกจึงจะตรวจพบ**
- **เม็ดเลือดแดงที่ไม่ลดลงระหว่างหลอดที่ 1 ถึงหลอดที่ 4** ซึ่งช่วยแยกจาก **traumatic tap** ที่เม็ดเลือดแดงจะลดลงเรื่อย ๆ

**ทำไมข้ออื่นผิด** — **ให้กลับบ้านเพราะ CT ปกติ** คือความผิดพลาดที่อันตรายที่สุดในเวชปฏิบัติฉุกเฉิน · **MRI ในอีก 1 สัปดาห์** ช้าเกินไปสำหรับภาวะที่เลือดออกซ้ำได้ · **nimodipine** ใช้หลังยืนยันการวินิจฉัยแล้ว · **CT ซ้ำใน 24 ชั่วโมง** ยิ่งทำให้ความไวลดลงไปอีก""",
        "Thunderclap headache + CT ปกติ = ต้องเจาะหลังหา xanthochromia อย่าให้กลับบ้าน",
        "LP for suspected SAH",
        ["สไลด์ อ.พิมลพรรณ — Lumbar puncture indications"]),
    mcq("NEU-LP-MCQ-02",
        "Which of the following is listed in the lecture as a THERAPEUTIC (rather than diagnostic) indication for lumbar puncture?",
        ["Suspected CNS lymphoma", "Guillain-Barré syndrome", "Intrathecal administration of chemotherapy", "Normal pressure hydrocephalus", "CNS vasculitis"],
        2,
        """สไลด์แบ่งข้อบ่งชี้ไว้สองกลุ่มชัดเจน

**Therapeutic maneuver — มีเพียงสองข้อ**
- **Spinal anesthesia**
- **Intrathecal administration of chemotherapy / antibiotics**

**Diagnosis — ที่เหลือทั้งหมด**

| กลุ่ม | ตัวอย่าง |
|---|---|
| **CNS infection** | meningitis/cerebritis จากแบคทีเรีย ไวรัส เชื้อรา ปรสิต · CNS syphilis |
| **CNS/PNS inflammation** | autoimmune encephalitis · MS · **GBS** · **CIDP** · paraneoplastic · neurosarcoidosis · **CNS vasculitis** |
| **Malignancy** | carcinomatous meningitis · **CNS lymphoma** |
| **Others** | **SAH ที่ CT เป็นลบ** · IIH · intracranial hypotension · **NPH** |

> **NPH เป็นข้อที่ลวงได้** — การเจาะระบายน้ำไขสันหลังออกใน NPH (large-volume tap) ดูเหมือนการรักษาเพราะผู้ป่วยเดินดีขึ้นชั่วคราว **แต่จุดประสงค์คือการวินิจฉัยและทำนายผลของการใส่ shunt** สไลด์จึงจัดไว้ในกลุ่ม diagnosis""",
        "Therapeutic มีแค่สองอย่าง: spinal anesthesia และ intrathecal drug — ที่เหลือคือเพื่อวินิจฉัย",
        "Indications for lumbar puncture",
        ["สไลด์ อ.พิมลพรรณ — Indications"]),
    ])

sec("neuro-lp-02", "ข้อห้ามและเทคนิคที่ลดภาวะแทรกซ้อน",
    "สี่ข้อเทคนิคที่สไลด์เน้น · 22G · 40 mL · ห้ามดูด · ใส่ stylet ก่อนถอนเข็ม", 9,
"""### ข้อห้ามที่ต้องคิดถึงก่อนเสมอ

| ข้อห้าม | เหตุผล |
|---|---|
| **ความดันในกะโหลกสูงจาก space-occupying lesion** | เสี่ยง **cerebral herniation** — ต้องทำภาพก่อนในผู้ที่มีข้อบ่งชี้ |
| **การแข็งตัวของเลือดผิดปกติ / เกล็ดเลือดต่ำ / ได้ยาต้านการแข็งตัวของเลือด** | เสี่ยง **spinal epidural hematoma** |
| **การติดเชื้อที่ผิวหนังตรงตำแหน่งที่จะแทงเข็ม** | เสี่ยงพาเชื้อเข้าช่องน้ำไขสันหลัง |
| **สงสัย spinal epidural abscess ที่ระดับนั้น** | เข็มอาจผ่านหนองเข้าสู่ช่อง subarachnoid |
| **ผู้ป่วยไม่ให้ความร่วมมือ** | เสี่ยงบาดเจ็บ ควรพิจารณาให้ยาระงับความรู้สึก |

> **ย้ำจากคาบ CNS infection** — ผู้ป่วยที่มี **อายุ > 60 ปี · ภูมิคุ้มกันบกพร่อง · ชักใกล้เวลาที่มา · ระดับการรู้ตัวเปลี่ยน · focal deficit** ต้อง **ทำ CT ก่อนเจาะหลัง** และใน **brain abscess สไลด์ระบุว่า CSF analysis is NOT recommended**

### สี่เทคนิคที่สไลด์ระบุไว้ตรง ๆ

1. **เข็มขนาดใหญ่ (22G) เป็นปัจจัยเสี่ยงของ post-LP headache ที่รุนแรง** → ใช้เข็มเล็กลงเมื่อทำได้
2. **ระบายน้ำไขสันหลังออกได้อย่างปลอดภัยถึง 40 mL**
3. **ห้ามใช้การดูด (aspiration)** เพราะ **เพิ่มความเสี่ยงเลือดออก** — ให้น้ำไขสันหลังไหลออกเองตามแรงโน้มถ่วง
4. **ต้องใส่ stylet กลับเข้าไปก่อนถอนเข็มออก** เพราะ **ลดความเสี่ยงของ post-LP headache**

### ข้อที่ 4 ทำไมถึงช่วย
ถ้าถอนเข็มโดยไม่ใส่ stylet กลับ **เส้นใยของ arachnoid อาจถูกดูดเข้าไปในรูเข็มและถูกดึงออกมาด้วย** ทำให้รูรั่วที่เยื่อดูราปิดไม่สนิท น้ำไขสันหลังรั่วต่อเนื่อง เกิด **intracranial hypotension** และปวดศีรษะ
""",
    ["22G = เข็มใหญ่ เพิ่มความเสี่ยง post-LP headache รุนแรง",
     "ระบายได้ปลอดภัยถึง 40 mL",
     "ห้ามดูดน้ำไขสันหลัง เพราะเพิ่มความเสี่ยงเลือดออก",
     "ใส่ stylet กลับก่อนถอนเข็มเสมอ ลด post-LP headache"],
    [
    mcq("NEU-LP-MCQ-03",
        "Which technique is recommended in the lecture to reduce the risk of post-lumbar-puncture headache?",
        ["Aspirating CSF gently with a syringe to shorten the procedure",
         "Replacing the stylet before withdrawing the spinal needle",
         "Using a larger 22G needle for faster flow",
         "Removing at least 60 mL of CSF",
         "Keeping the patient seated upright for 6 hours afterwards"],
        1,
        """สไลด์ระบุไว้ว่า *"The stylet should be replaced before the spinal needle is removed, as this can reduce the risk of post-LP headache"*

**กลไก** — ถ้าถอนเข็มโดยไม่ใส่ stylet กลับ **เส้นใยของ arachnoid อาจถูกดึงเข้าไปในรูเข็มและติดออกมาด้วย** ทำให้รูที่เยื่อดูราปิดไม่สนิท น้ำไขสันหลังรั่วต่อเนื่อง → **intracranial hypotension** → ปวดศีรษะเวลาลุกนั่งหรือยืน และดีขึ้นเมื่อนอนราบ

**ทำไมข้ออื่นผิด**

| ตัวเลือก | สไลด์ระบุว่า |
|---|---|
| **ดูดด้วย syringe** | **ห้ามทำ** — *"Aspiration of CSF should not be attempted, as it may increase the risk of bleeding"* |
| **ใช้เข็ม 22G เพราะไหลเร็ว** | **ตรงข้าม** — *"A large-bore needle diameter (22G) may be a risk factor for severe post-LP headache"* |
| **เอาออก 60 mL** | สไลด์ระบุว่าปลอดภัยถึง **40 mL** |
| **นั่งตัวตรง 6 ชั่วโมง** | การนอนราบหลังทำไม่ได้ลดอุบัติการณ์ตามหลักฐานปัจจุบัน และการนั่งตรงยิ่งทำให้อาการแย่ลงหากมีการรั่ว |""",
        "สี่ข้อของสไลด์: เข็มเล็กกว่า 22G · ไม่เกิน 40 mL · ห้ามดูด · ใส่ stylet ก่อนถอนเข็ม",
        "LP technique",
        ["สไลด์ อ.พิมลพรรณ — Lumbar puncture procedure"]),
    mcq("NEU-LP-MCQ-04",
        "Why does the lecture state that aspiration of CSF should not be attempted during lumbar puncture?",
        ["It slows the procedure unnecessarily",
         "It may increase the risk of bleeding",
         "It dilutes the CSF glucose measurement",
         "It causes false-positive Gram stains",
         "It prevents accurate opening pressure measurement"],
        1,
        """สไลด์ระบุเหตุผลไว้ตรง ๆ ว่า *"Aspiration of CSF should not be attempted, as it **may increase the risk of bleeding**"*

**กลไก** — การดูดสร้างแรงดันลบในช่อง subarachnoid ดึงให้ **หลอดเลือดดำเล็ก ๆ (epidural venous plexus) และรากประสาท** ถูกดูดเข้าหารูเข็ม เกิดการบาดเจ็บและเลือดออก นอกจากนี้ยังเพิ่มความเสี่ยงของ **traumatic tap** ซึ่งทำให้แปลผลเม็ดเลือดแดงใน CSF ยากขึ้น

**วิธีที่ถูกต้อง** — ปล่อยให้น้ำไขสันหลัง **ไหลออกเองตามแรงโน้มถ่วง** ทีละหยด ถ้าไหลช้าให้ปรับตำแหน่งเข็มหรือหมุน bevel แทนการดูด

**เทคนิคอื่นในชุดเดียวกัน**
- **เข็ม 22G เป็นปัจจัยเสี่ยงของ post-LP headache ที่รุนแรง**
- **ระบายได้ปลอดภัยถึง 40 mL**
- **ใส่ stylet กลับก่อนถอนเข็ม**

**ทำไมข้ออื่นผิด** — การดูดไม่ได้ทำให้น้ำตาลเจือจาง ไม่ทำให้ Gram stain เป็นบวกลวง และการวัด opening pressure ทำก่อนเก็บน้ำอยู่แล้ว""",
        "ปล่อยให้ไหลเอง อย่าดูด — การดูดเพิ่มความเสี่ยงเลือดออกและ traumatic tap",
        "LP technique — aspiration",
        ["สไลด์ อ.พิมลพรรณ — Lumbar puncture procedure"]),
    ])

sec("neuro-lp-03", "ภาวะแทรกซ้อนของการเจาะหลัง",
    "เจ็ดภาวะที่สไลด์ระบุ และภาวะที่อันตรายที่สุด", 7,
"""สไลด์ระบุภาวะแทรกซ้อนไว้ **เจ็ดข้อ**

| ภาวะแทรกซ้อน | หมายเหตุ |
|---|---|
| **Back pain** | พบบ่อยที่สุด มักหายเอง |
| **Post-LP headache** | ภาวะแทรกซ้อนที่มีนัยสำคัญที่พบบ่อยที่สุด |
| **Infection** | จากเทคนิคปลอดเชื้อที่ไม่ดีพอ |
| **Bleeding** | โดยเฉพาะในผู้ที่มีความผิดปกติของการแข็งตัวของเลือด |
| **Cerebral herniation** | **อันตรายที่สุดและถึงแก่ชีวิต** — ป้องกันด้วยการทำภาพก่อนในผู้ที่มีข้อบ่งชี้ |
| **อาการทางระบบประสาทเล็กน้อย** | เช่น **radicular pain หรือชา** จากเข็มไปสัมผัสรากประสาท |
| **Intracranial hypotension** | จากการรั่วของน้ำไขสันหลังต่อเนื่อง |

### Post-LP headache — ลักษณะที่ต้องจำ
- **ปวดศีรษะเวลาลุกนั่งหรือยืน และดีขึ้นชัดเจนเมื่อนอนราบ (postural/orthostatic headache)**
- มักเริ่มภายใน **24–48 ชั่วโมง** หลังทำ
- อาจมีคอแข็ง คลื่นไส้ หูอื้อ หรือมองเห็นภาพซ้อนร่วมด้วย
- **ปัจจัยเสี่ยง** — **เข็มขนาดใหญ่ (22G)**, ไม่ใส่ stylet กลับก่อนถอนเข็ม, อายุน้อย, เพศหญิง, ดัชนีมวลกายต่ำ
- **การรักษา** — นอนพัก ดื่มน้ำ ยาแก้ปวด คาเฟอีน และถ้าไม่ดีขึ้นให้พิจารณา **epidural blood patch**

### Cerebral herniation — ป้องกันได้ทั้งหมด
เกิดเมื่อเจาะหลังในผู้ป่วยที่มี **space-occupying lesion และความดันในกะโหลกสูง** การลดความดันที่ปลายล่างทำให้เนื้อสมองเคลื่อนลง

**วิธีป้องกัน** — **ทำ CT brain ก่อนในผู้ที่มีข้อบ่งชี้ห้าข้อ** (อายุ > 60 ปี · ภูมิคุ้มกันบกพร่อง · ชักใกล้เวลาที่มา · ระดับการรู้ตัวเปลี่ยน · focal deficit) และ **ห้ามเจาะหลังในผู้ป่วย brain abscess**
""",
    ["เจ็ดภาวะแทรกซ้อน: ปวดหลัง · post-LP headache · ติดเชื้อ · เลือดออก · herniation · radicular pain/ชา · intracranial hypotension",
     "Post-LP headache = ปวดตอนลุก ดีขึ้นตอนนอนราบ",
     "Cerebral herniation อันตรายที่สุด แต่ป้องกันได้ด้วยการทำภาพก่อนในผู้ที่มีข้อบ่งชี้",
     "ไม่ดีขึ้นด้วยการรักษาประคับประคอง ให้คิดถึง epidural blood patch"],
    [
    mcq("NEU-LP-MCQ-05",
        "Two days after a diagnostic lumbar puncture, a 26-year-old woman has a headache that is severe when she stands and resolves within minutes of lying flat. Which complication is this, and which technical factor most likely contributed?",
        ["Bacterial meningitis; inadequate skin antisepsis",
         "Post-LP headache from CSF leak; use of a large-bore 22G needle",
         "Cerebral herniation; removal of too much CSF",
         "Spinal epidural haematoma; underlying coagulopathy",
         "Radicular injury; needle contact with a nerve root"],
        1,
        """**ปวดศีรษะที่เป็นเวลาลุกยืนและหายเมื่อนอนราบ = post-LP headache** ซึ่งเกิดจาก **การรั่วของน้ำไขสันหลังที่รูเยื่อดูรา → intracranial hypotension**

**ปัจจัยทางเทคนิคที่สไลด์ระบุ**
- *"A large-bore needle diameter (**22G**) may be a risk factor for **severe post-LP headache**"* ← ข้อนี้
- *"The **stylet should be replaced before the spinal needle is removed**, as this can reduce the risk of post-LP headache"*

**ทำไมข้ออื่นผิด**

| ตัวเลือก | เหตุผลที่ไม่ใช่ |
|---|---|
| **Bacterial meningitis** | ต้องมีไข้ คอแข็ง และปวดศีรษะที่**ไม่ขึ้นกับท่าทาง** |
| **Cerebral herniation** | เป็นภาวะฉุกเฉินที่เกิดทันทีหรือภายในชั่วโมง มีระดับการรู้ตัวลดลง ไม่ใช่ปวดศีรษะตามท่าทาง 2 วันต่อมา |
| **Spinal epidural haematoma** | แสดงออกเป็น **ปวดหลังรุนแรง ขาอ่อนแรง ปัสสาวะไม่ออก** ไม่ใช่ปวดศีรษะ |
| **Radicular injury** | ให้อาการปวดร้าวหรือชาตามแนวราก ไม่ใช่ปวดศีรษะ |

**การรักษา** — นอนพัก ดื่มน้ำ ยาแก้ปวด คาเฟอีน และถ้าไม่ดีขึ้นพิจารณา **epidural blood patch**""",
        "ปวดหัวตอนลุก หายตอนนอน = post-LP headache — ป้องกันด้วยเข็มเล็กและใส่ stylet ก่อนถอน",
        "Post-LP headache",
        ["สไลด์ อ.พิมลพรรณ — Complications"]),
    ])

sec("neuro-lp-04", "สิ่งที่ต้องส่งตรวจจากน้ำไขสันหลัง",
    "เจ็ดรายการที่สไลด์สรุปไว้", 6,
"""สไลด์สรุปรายการส่งตรวจไว้ครบและใช้เป็น checklist ข้างเตียงได้เลย

| ลำดับ | รายการ |
|---|---|
| 1 | **Colour and appearance** — ใส ขุ่น หรือเหลือง (xanthochromia) |
| 2 | **Opening pressure และ closing pressure** |
| 3 | **Cell count และ differential** |
| 4 | **Protein และ sugar** |
| 5 | **Microbiology** — Gram stain, culture |
| 6 | **PCR for viral panel, CryptoAg, India ink stain** |
| 7 | **Cytology** — เมื่อสงสัยมะเร็ง (carcinomatous meningitis, CNS lymphoma) |

### จุดที่คนพลาดบ่อย
- **ต้องเจาะน้ำตาลในเลือดพร้อมกันเสมอ** เพราะค่าที่ใช้แปลผลคือ **อัตราส่วน CSF/serum glucose** (ปกติ ≥ 0.6) ไม่ใช่ตัวเลข CSF เดี่ยว ๆ — สำคัญมากในผู้ป่วยเบาหวาน
- **ต้องวัด opening pressure ก่อนปล่อยน้ำออก** และต้องให้ผู้ป่วย **นอนตะแคงเหยียดขา** จึงจะได้ค่าที่แปลผลได้ (วัดในท่านั่งจะได้ค่าสูงเกินจริง)
- **Cytology ต้องส่งปริมาณมากและอาจต้องส่งซ้ำหลายครั้ง** เพราะความไวต่ำในการตรวจครั้งเดียว
- **xanthochromia ต้องใช้เวลาราว 12 ชั่วโมงหลังเลือดออก** จึงจะตรวจพบ — เจาะเร็วเกินไปอาจได้ผลลบลวงใน SAH

### กรอบสรุปของทั้งคาบ
สไลด์ปิดท้ายด้วยคำถามเดิมสองข้อ — **Where and what is the lesion?** น้ำไขสันหลังคือเครื่องมือที่ช่วยตอบคำถามที่สอง โดยเฉพาะกลุ่ม **infection, inflammation และ tumor**
""",
    ["เจ็ดรายการ: สี/ลักษณะ · opening+closing pressure · cell count+diff · protein+sugar · microbiology · PCR/CryptoAg/India ink · cytology",
     "เจาะน้ำตาลในเลือดพร้อมกันเสมอ เพื่อคำนวณอัตราส่วน CSF/serum",
     "วัด opening pressure ในท่านอนตะแคงเหยียดขา ก่อนปล่อยน้ำออก",
     "Xanthochromia ต้องรอราว 12 ชั่วโมงหลังเลือดออกจึงจะพบ"],
    [
    mcq("NEU-LP-MCQ-06",
        "A patient with suspected carcinomatous meningitis has a lumbar puncture. Which CSF test listed in the lecture is specifically needed for this indication?",
        ["India ink stain", "Cryptococcal antigen", "Cytology", "Viral PCR panel", "Acid-fast bacilli smear"],
        2,
        """**Cytology** คือการตรวจที่สไลด์ระบุไว้ในรายการส่งตรวจ และเป็นการตรวจที่ใช้ยืนยัน **carcinomatous meningitis** และ **CNS lymphoma** ซึ่งเป็นสองข้อบ่งชี้ในกลุ่ม **malignancy** ของการเจาะหลัง

**ข้อควรรู้ในทางปฏิบัติ** — **ความไวของ cytology ในการเจาะครั้งเดียวค่อนข้างต่ำ** จึงมักต้อง
- **ส่งปริมาณน้ำไขสันหลังให้มาก** (สไลด์ระบุว่าระบายได้ปลอดภัยถึง **40 mL**)
- **ส่งซ้ำหลายครั้ง** จึงจะเพิ่มโอกาสพบเซลล์มะเร็ง
- ส่งตรวจ **flow cytometry** ร่วมด้วยเมื่อสงสัย lymphoma

**การตรวจอื่นในรายการมีไว้สำหรับ**

| การตรวจ | ใช้กับ |
|---|---|
| **India ink, CryptoAg** | **Cryptococcal meningitis** |
| **Viral PCR panel** | **Viral meningitis/encephalitis** — enterovirus, HSV, VZV |
| **AFB smear** | **Tuberculous meningitis** |
| **Gram stain, culture** | **Bacterial meningitis** |""",
        "สงสัยมะเร็งแพร่สู่เยื่อหุ้มสมอง = ส่ง cytology ปริมาณมากและอาจต้องส่งซ้ำ",
        "CSF cytology",
        ["สไลด์ อ.พิมลพรรณ — CSF analysis"]),
    ])

sec("neuro-lp-05", "การตรวจสายตา — Snellen, pinhole และ near chart",
    "อ่านค่าอย่างไร · เมื่ออ่านแถวบนสุดไม่ได้ · pinhole บอกอะไร", 8,
"""### Snellen chart
- ใช้ที่ระยะ **20 ฟุต = 6 เมตร**
- ค่าที่บันทึกเป็นเศษส่วน เช่น **20/40** หมายถึง **ผู้ป่วยต้องอยู่ที่ 20 ฟุตจึงอ่านตัวอักษรที่คนสายตาปกติอ่านได้จากระยะ 40 ฟุต** — **ตัวส่วนยิ่งมาก สายตายิ่งแย่**

### เมื่อผู้ป่วยอ่านแถวบนสุดไม่ได้ — ลำดับการลดระดับ
สไลด์ไล่ลำดับไว้ดังนี้

| ระดับ | วิธีทดสอบ |
|---|---|
| **5 ฟุต = 5/200** | ให้เข้าใกล้แผ่นป้ายจนถึง 5 ฟุต |
| **Counting fingers (CF) @ 2 feet** | นับนิ้วที่ระยะ 2 ฟุต |
| **Hand motions (HM)** | เห็นการโบกมือ |
| **Light perception (LP)** | รับรู้แสง — ถ้าไม่รับรู้เลยคือ **no light perception (NLP)** |

> **ต้องบันทึกระยะที่ทดสอบเสมอ** เช่น *CF @ 2 ft* เพราะ *CF @ 1 ft* กับ *CF @ 3 ft* ไม่เท่ากัน

### Pinhole test — ตรวจง่ายแต่บอกได้มาก
สไลด์ระบุหน้าที่ไว้สั้น ๆ ว่า **"correct refractive error"**

**หลักการ** — รูเข็มยอมให้เฉพาะลำแสงที่ขนานกับแกนสายตาผ่านเข้าไป จึงตัดผลของความผิดปกติของการหักเหแสงออกไป

**การแปลผล — จุดที่มีค่าทางคลินิกมากที่สุด**

| ผล | ความหมาย |
|---|---|
| **มองผ่าน pinhole แล้วดีขึ้น** | สาเหตุคือ **refractive error** (สายตาสั้น ยาว เอียง) — แก้ด้วยแว่น |
| **มองผ่าน pinhole แล้วไม่ดีขึ้น** | สาเหตุอยู่ที่ **สื่อนำแสงขุ่น (ต้อกระจก) จอประสาทตา หรือเส้นประสาทตา** — ต้องหาสาเหตุต่อ |

> ในทางอายุรกรรม **ข้อนี้สำคัญมาก** เพราะผู้ป่วยที่ตามัวแล้ว **pinhole ไม่ช่วย** คือกลุ่มที่ต้องรีบหาสาเหตุทางระบบประสาทหรือจอประสาทตา เช่น **optic neuritis, ischemic optic neuropathy, retinal artery occlusion**

### Near chart
- ใช้ที่ระยะ **33 ซม. = 14 นิ้ว**
- มีประโยชน์เมื่อ **ไม่มีพื้นที่ 6 เมตร** เช่น ข้างเตียงผู้ป่วย
- **ต้องให้ผู้ป่วยใส่แว่นสำหรับอ่านหนังสือถ้ามี** มิฉะนั้นจะประเมินผิดในผู้สูงอายุที่มีสายตายาวตามวัย
""",
    ["20/40 = ต้องอยู่ 20 ฟุตเพื่ออ่านสิ่งที่คนปกติอ่านได้จาก 40 ฟุต — ตัวส่วนยิ่งมากยิ่งแย่",
     "ลำดับเมื่ออ่านไม่ได้: 5/200 → CF → HM → LP → NLP และต้องบันทึกระยะเสมอ",
     "Pinhole ดีขึ้น = refractive error · ไม่ดีขึ้น = สื่อนำแสง จอประสาทตา หรือเส้นประสาทตา",
     "Near chart ใช้ที่ 33 ซม. และต้องใส่แว่นอ่านหนังสือด้วย"],
    [
    mcq("NEU-LP-MCQ-07",
        "A 62-year-old man reports blurred vision in the right eye. Visual acuity is 20/100 in that eye and does not improve with a pinhole. Which conclusion is best supported?",
        ["The cause is almost certainly an uncorrected refractive error",
         "The cause is likely in the ocular media, retina or optic nerve rather than refractive",
         "The test is invalid and should be repeated with a near chart",
         "The patient has no visual impairment",
         "The finding confirms cataract specifically"],
        1,
        """**Pinhole ทำหน้าที่ "correct refractive error"** ตามที่สไลด์ระบุ โดยยอมให้เฉพาะลำแสงที่ขนานกับแกนสายตาผ่านเข้าไป จึงตัดผลของสายตาสั้น ยาว หรือเอียงออก

**การแปลผล**

| ผล pinhole | ความหมาย |
|---|---|
| **ดีขึ้น** | สาเหตุคือ **refractive error** → แก้ด้วยแว่น |
| **ไม่ดีขึ้น** (รายนี้) | สาเหตุอยู่ที่ **สื่อนำแสงขุ่น จอประสาทตา หรือเส้นประสาทตา** |

**สิ่งที่ต้องทำต่อในผู้ป่วยรายนี้** — ตรวจ **pupillary reflex หา relative afferent pupillary defect (RAPD)** ซึ่งบ่งชี้โรคของเส้นประสาทตา และ **ส่อง fundus** ดู **optic disc (papilledema, disc pallor), cotton wool spot, cherry red spot** ตามที่สไลด์สอนในหัวข้อ fundoscopy

**ทำไมข้ออื่นผิด** — การที่ pinhole ไม่ช่วย **ตัด refractive error ออก** ไม่ใช่ยืนยัน · การทดสอบไม่ได้ผิดพลาดและไม่ต้องเปลี่ยนไปใช้ near chart · **20/100 คือความบกพร่องทางการมองเห็นที่ชัดเจน** · และ **ยังยืนยันต้อกระจกไม่ได้** เพราะจอประสาทตาและเส้นประสาทตาก็ให้ผลแบบเดียวกัน ต้องตรวจเพิ่ม""",
        "Pinhole ไม่ช่วย = ปัญหาไม่ได้อยู่ที่ค่าสายตา ให้รีบหาสาเหตุที่สื่อนำแสง จอประสาทตา หรือเส้นประสาทตา",
        "Pinhole test",
        ["สไลด์ อ.พิมลพรรณ — Visual acuity test"]),
    mcq("NEU-LP-MCQ-08",
        "A bedbound patient cannot read the top line of the Snellen chart even at 5 feet, but can correctly count the examiner's fingers held at 2 feet. How should the visual acuity be recorded?",
        ["20/200", "5/200", "Counting fingers at 2 feet", "Hand motions", "Light perception"],
        2,
        """เมื่อผู้ป่วยอ่านแผ่นป้ายไม่ได้ สไลด์ให้ลำดับการลดระดับไว้

1. **5 ฟุต = 5/200** — ให้เข้าใกล้จนถึง 5 ฟุต
2. **Counting fingers (CF) @ 2 feet** ← ผู้ป่วยรายนี้อยู่ระดับนี้
3. **Hand motions (HM)**
4. **Light perception (LP)** และถ้าไม่รับรู้แสงเลยคือ **no light perception (NLP)**

ผู้ป่วยรายนี้ **อ่านแถวบนสุดที่ 5 ฟุตไม่ได้** จึงต่ำกว่า 5/200 แต่ **นับนิ้วที่ 2 ฟุตได้** จึงบันทึกเป็น **CF @ 2 ft**

> **ต้องระบุระยะทางเสมอ** — *CF @ 2 ft* ไม่เท่ากับ *CF @ 1 ft* หรือ *CF @ 3 ft* การบันทึกแค่ "CF" ลอย ๆ ทำให้เปรียบเทียบการเปลี่ยนแปลงในครั้งถัดไปไม่ได้

**ทำไมข้ออื่นผิด** — **20/200 และ 5/200** ต้องอ่านตัวอักษรบนแผ่นป้ายได้ ซึ่งรายนี้ทำไม่ได้ · **HM และ LP** เป็นระดับที่ **แย่กว่า** การนับนิ้ว จึงบันทึกต่ำเกินจริง""",
        "บันทึก CF/HM/LP พร้อมระยะทางเสมอ ไม่งั้นติดตามการเปลี่ยนแปลงไม่ได้",
        "Recording low visual acuity",
        ["สไลด์ อ.พิมลพรรณ — Snellen chart"]),
    ])

sec("neuro-lp-06", "Fundoscopy — สิ่งที่ต้องดูให้เป็น",
    "direct กับ indirect ophthalmoscope · papilledema · cotton wool spot · cherry red spot", 8,
"""### เครื่องมือสองชนิด

| | **Direct ophthalmoscope** | **Indirect ophthalmoscope** |
|---|---|---|
| ภาพที่เห็น | **หัวกลับ? ไม่ — เห็นภาพตั้ง** | **ภาพกลับหัว** |
| กำลังขยาย | **สูง (ราว 15 เท่า)** | ต่ำกว่า |
| ขอบเขตที่เห็น | **แคบ** | **กว้าง เห็นขอบจอประสาทตาได้** |
| ใช้โดย | **อายุรแพทย์ แพทย์ทั่วไป ข้างเตียง** | จักษุแพทย์ |

**สำหรับนักศึกษาแพทย์และอายุรแพทย์ เครื่องมือที่ต้องใช้ให้เป็นคือ direct ophthalmoscope**

### เทคนิคที่ทำให้ส่องเห็น
- **ทำในห้องที่มืด** เพื่อให้รูม่านตาขยายเอง
- **ใช้ตาขวาของผู้ตรวจส่องตาขวาของผู้ป่วย** และตาซ้ายส่องตาซ้าย
- ให้ผู้ป่วย **มองไปไกล ๆ จุดใดจุดหนึ่ง** และไม่ขยับตาม
- เริ่มที่ระยะราว 30 ซม. หา **red reflex** ก่อน แล้วค่อย ๆ เข้าใกล้
- **หาขั้วประสาทตาโดยเดินตามหลอดเลือดไปทางที่แขนงมาบรรจบกัน**

### สิ่งที่ต้องดูตามลำดับ
1. **Optic disc** — ขอบชัดหรือไม่ สีซีดหรือไม่ cup/disc ratio
2. **หลอดเลือด** — ขนาด การไขว้ของหลอดเลือดแดงกับดำ เลือดออก
3. **จอประสาทตาโดยรอบ** — exudate, cotton wool spot
4. **Macula และ fovea**

### ภาพผิดปกติสามอย่างที่สไลด์ยกมา

| ภาพ | ความหมายทางคลินิก |
|---|---|
| **Papilledema** | **ขั้วประสาทตาบวม ขอบไม่ชัด จาก ความดันในกะโหลกสูง ทั้งสองข้าง** — เจอแล้วต้องหาสาเหตุ เช่น ก้อนในสมอง, IIH, venous sinus thrombosis และ **เป็นสัญญาณเตือนว่าอาจห้ามเจาะหลังก่อนทำภาพ** |
| **Cotton wool spot** | ปื้นขาวขอบฟุ้ง จาก **การขาดเลือดของชั้นใยประสาท (microinfarct)** — พบใน **เบาหวาน ความดันโลหิตสูง HIV และโรคหลอดเลือดอื่น ๆ** |
| **Cherry red spot** | จุดแดงที่ macula ตัดกับจอประสาทตารอบ ๆ ที่ซีด — คลาสสิกของ **central retinal artery occlusion** และพบใน **โรคสะสมบางชนิด** |

### กายวิภาคที่ต้องรู้จักชื่อ
**Cornea · anterior chamber (aqueous humour) · posterior chamber · pupil · iris และ ciliary body (รวมเป็น uvea) · suspensory ligament of lens · lens · choroid · sclera · vitreous humour · hyaloid canal · retinal blood vessels · macula และ fovea · optic nerve และ optic disc**

> **ความเชื่อมโยงกับคาบนี้** — การเห็น **papilledema** ก่อนเจาะหลังคือหนึ่งในวิธีคัดกรองความดันในกะโหลกสูงข้างเตียง และเชื่อมกับข้อบ่งชี้เรื่อง **idiopathic intracranial hypertension** ที่เป็นข้อบ่งชี้ของการเจาะหลังทั้งเพื่อวินิจฉัยและลดความดัน
""",
    ["อายุรแพทย์ต้องใช้ direct ophthalmoscope ให้เป็น — กำลังขยายสูงแต่เห็นแคบ",
     "ตาขวาส่องตาขวา ตาซ้ายส่องตาซ้าย ในห้องมืด",
     "Papilledema = ความดันในกะโหลกสูง → ต้องหาสาเหตุและระวังก่อนเจาะหลัง",
     "Cotton wool spot = ขาดเลือดชั้นใยประสาท · Cherry red spot = CRAO"],
    [
    mcq("NEU-LP-MCQ-09",
        "A 28-year-old obese woman has daily headaches and transient visual obscurations. Fundoscopy shows bilateral swollen optic discs with blurred margins. Which statement is most appropriate?",
        ["This is a cotton wool spot indicating retinal ischaemia",
         "This is papilledema; raised intracranial pressure must be evaluated and imaging obtained before lumbar puncture",
         "This is a cherry red spot indicating central retinal artery occlusion",
         "Lumbar puncture is contraindicated in all circumstances here",
         "The finding is a normal variant in obesity"],
        1,
        """**ขั้วประสาทตาบวมสองข้างขอบไม่ชัด = papilledema** ซึ่งสไลด์ยกเป็นภาพผิดปกติที่ต้องรู้จัก และหมายถึง **ความดันในกะโหลกสูง**

**บริบทของผู้ป่วย** — หญิงอายุน้อย น้ำหนักเกิน ปวดศีรษะทุกวัน และมี **transient visual obscuration** เข้าได้กับ **idiopathic intracranial hypertension (IIH)** ซึ่งสไลด์ระบุไว้เป็น **ข้อบ่งชี้ของการเจาะหลัง** ทั้งเพื่อ **วัด opening pressure เพื่อวินิจฉัย** และ **ระบายน้ำเพื่อลดความดัน**

**ลำดับที่ถูกต้อง**
1. **ทำภาพสมอง (MRI/MRV) ก่อน** เพื่อตัด **space-occupying lesion และ venous sinus thrombosis**
2. เมื่อภาพไม่พบก้อน **จึงเจาะหลังวัด opening pressure** ซึ่งใน IIH จะสูง
3. ส่ง **CSF analysis** ซึ่งต้องปกติจึงจะเข้าเกณฑ์ IIH

**ทำไมข้ออื่นผิด**
- **Cotton wool spot** เป็นปื้นขาวในจอประสาทตาจาก microinfarct ไม่ใช่ขั้วประสาทตาบวม
- **Cherry red spot** อยู่ที่ macula และเป็นของ **CRAO** ซึ่งทำให้ตาบอดเฉียบพลันข้างเดียว
- **ห้ามเจาะหลังในทุกกรณี** ไม่ถูก — เมื่อภาพตัดก้อนออกแล้ว การเจาะหลังคือขั้นตอนที่จำเป็นในการวินิจฉัย IIH
- **ไม่ใช่ภาวะปกติ** ในคนน้ำหนักเกิน""",
        "Papilledema สองข้าง = ความดันในกะโหลกสูง → ทำภาพก่อน แล้วค่อยเจาะหลังวัดความดัน",
        "Papilledema and IIH",
        ["สไลด์ อ.พิมลพรรณ — Fundoscopy / Indications"]),
    mcq("NEU-LP-MCQ-10",
        "Which fundoscopic finding is classically associated with central retinal artery occlusion?",
        ["Papilledema", "Cotton wool spot", "Cherry red spot at the macula", "Optic disc cupping", "Hard exudates in a macular star"],
        2,
        """**Cherry red spot ที่ macula** คือภาพคลาสสิกของ **central retinal artery occlusion (CRAO)** ซึ่งเป็นหนึ่งในสามภาพผิดปกติที่สไลด์ยกมา

**กลไก** — เมื่อหลอดเลือดแดงจอประสาทตาอุดตัน จอประสาทตาที่หนาและมีหลายชั้นจะ **ซีดบวม** แต่ **fovea บางมากจนมองทะลุเห็นสี choroid ที่ยังมีเลือดจาก ciliary artery มาเลี้ยงอยู่** จึงเห็นเป็น **จุดแดงตัดกับพื้นที่ซีดรอบ ๆ**

**ทางคลินิก** — CRAO คือ **"stroke ของตา"** ผู้ป่วยตาบอดข้างเดียวเฉียบพลันไม่เจ็บ **เป็นภาวะฉุกเฉิน** ต้องประเมินหาแหล่งลิ่มเลือดเหมือนผู้ป่วย stroke — carotid, หัวใจ และในผู้สูงอายุต้องคัดกรอง **giant cell arteritis** ด้วย ESR/CRP

**ภาพอื่นในตัวเลือก**

| ภาพ | พบใน |
|---|---|
| **Papilledema** | **ความดันในกะโหลกสูง** (สองข้าง) |
| **Cotton wool spot** | **microinfarct ของชั้นใยประสาท** — เบาหวาน ความดันสูง HIV |
| **Optic disc cupping** | **ต้อหิน (glaucoma)** |
| **Macular star** | ความดันโลหิตสูงรุนแรง, neuroretinitis |""",
        "Cherry red spot = CRAO = stroke ของตา ต้องประเมินหาแหล่งลิ่มเลือดเหมือน stroke",
        "Abnormal retina",
        ["สไลด์ อ.พิมลพรรณ — Abnormal retina"]),
    ])

OSCE = [{
 "id": "NEU-OSCE-04", "part": "OSCE/SAQ", "lec": "9/10",
 "lecture": "หัตถการ: Lumbar puncture + Eye examination",
 "topic": "OSCE – อธิบายและขอความยินยอมทำ lumbar puncture",
 "station": "สถานีสื่อสารกับผู้ป่วยจำลอง 8 นาที",
 "instruction": """ชายอายุ 34 ปี มาด้วยไข้และปวดศีรษะ 2 วัน ตรวจพบคอแข็ง แพทย์วางแผนเจาะหลังเพื่อวินิจฉัย ผู้ป่วยรู้สึกตัวดี ไม่มี focal deficit และ CT brain ปกติ
คำสั่ง: จงอธิบายหัตถการและขอความยินยอมจากผู้ป่วย (ไม่ต้องทำหัตถการจริง)

หมายเหตุสำหรับผู้ป่วยจำลอง: กังวลมากว่า "เจาะหลังแล้วจะเป็นอัมพาต" เพราะเคยได้ยินมาจากญาติ และถามว่าจะเจ็บไหม ต้องนอนโรงพยาบาลนานไหม""",
 "answer": """**เกณฑ์การให้คะแนน (เต็ม 20)**

**1. เปิดการสนทนาและประเมินความเข้าใจเดิม (3 คะแนน)**
- แนะนำตัว ระบุชื่อผู้ป่วยให้ถูกต้อง หาที่เป็นส่วนตัว
- **ถามก่อนว่าผู้ป่วยเข้าใจอะไรมาแล้วบ้าง และกังวลเรื่องอะไร** — จับประเด็น "กลัวเป็นอัมพาต" ให้ได้ตั้งแต่ต้น
- ถามว่าต้องการให้ญาติร่วมฟังด้วยหรือไม่

**2. อธิบายว่าทำไมต้องทำ (3 คะแนน)**
- อธิบายด้วยภาษาชาวบ้านว่าสงสัย **เยื่อหุ้มสมองอักเสบ** ซึ่งเป็นภาวะที่ **ต้องรีบรักษา**
- **การเจาะหลังเป็นการตรวจเดียวที่บอกได้ว่าเกิดจากเชื้ออะไร** — แบคทีเรีย ไวรัส เชื้อรา หรือวัณโรค ซึ่ง **ยาที่ใช้ต่างกันสิ้นเชิง**
- อธิบายว่าถ้าไม่ทำ จะต้องให้ยาแบบเดาไปก่อนซึ่งอาจไม่ตรงเชื้อ

**3. อธิบายขั้นตอนอย่างเป็นรูปธรรม (4 คะแนน)**
- **ท่า** — นอนตะแคงงอเข่าชิดอก หรือ นั่งโน้มตัวไปข้างหน้า
- **ตำแหน่ง** — **หลังส่วนล่าง ต่ำกว่าระดับที่ไขสันหลังสิ้นสุดแล้ว** ← จุดสำคัญที่ใช้คลายความกลัวอัมพาต
- **ฉีดยาชาเฉพาะที่ก่อน** — จะรู้สึกแสบตอนฉีดยาชาประมาณ 5–10 วินาที หลังจากนั้นจะรู้สึกแค่ **ตื้อ ๆ หรือดันหลัง** ไม่ใช่ปวดแหลม
- **ใช้เวลาประมาณ 15–30 นาที**
- **ปล่อยให้น้ำไขสันหลังไหลออกเอง ไม่ใช้การดูด**
- ระหว่างทำต้อง **อยู่นิ่ง ๆ** และบอกแพทย์ได้ตลอดถ้ามีอาการผิดปกติ

**4. ตอบคำถามเรื่องอัมพาตอย่างตรงประเด็น (4 คะแนน)** ← หัวใจของสถานีนี้
- **ยอมรับความกังวลก่อน ไม่ปัดตก** — "เป็นคำถามที่คนถามบ่อยมากครับ"
- **อธิบายด้วยกายวิภาค** — **ไขสันหลังสิ้นสุดที่ระดับเอวส่วนบน แต่เราแทงเข็มต่ำกว่านั้นลงไป บริเวณที่มีเพียงเส้นประสาทฝอย ๆ ลอยอยู่ในน้ำ ซึ่งจะหลบเข็มได้** จึงไม่ได้แทงโดนไขสันหลัง
- อธิบายว่าอาการที่อาจเกิดได้จริงคือ **ปวดร้าวหรือชาที่ขาชั่วคราว** ซึ่งเป็น **minor neurologic symptom** และหายได้
- **ไม่รับปากว่าไม่มีความเสี่ยงเลย** แต่ให้ภาพที่ถูกต้องตามสัดส่วน

**5. แจ้งภาวะแทรกซ้อนให้ครบตามความสำคัญ (3 คะแนน)**
ต้องกล่าวถึงอย่างน้อย **ปวดหลัง · ปวดศีรษะหลังเจาะ · เลือดออก · ติดเชื้อ · อาการชาหรือปวดร้าวชั่วคราว**
- เน้น **post-LP headache** ว่าเป็นภาวะที่พบบ่อยที่สุดที่มีความสำคัญ **ปวดเวลาลุกนั่งและดีขึ้นเมื่อนอนราบ** มักหายเองใน 2–3 วัน และมีวิธีรักษาถ้าไม่หาย
- อธิบายว่าได้ทำ **CT สมองมาแล้วและปกติ** จึงได้ตัดภาวะที่อันตรายที่สุดออกไปแล้ว

**6. ตอบคำถามที่ผู้ป่วยถามให้ครบ (2 คะแนน)**
- **"จะเจ็บไหม"** — ตอบตามข้อ 3
- **"ต้องนอนโรงพยาบาลนานไหม"** — ระยะเวลานอนโรงพยาบาลขึ้นกับ **ผลการตรวจและชนิดของเชื้อ** ไม่ได้ขึ้นกับตัวหัตถการ · หลังทำให้ **นอนราบพักสักระยะ**

**7. ปิดการสนทนา (1 คะแนน)**
- **ถามว่ามีคำถามอะไรอีกไหม** และ **ให้ผู้ป่วยทวนความเข้าใจกลับ (teach-back)**
- **ขอความยินยอมอย่างเป็นทางการและลงนามในเอกสาร**
- บอกว่า **ผู้ป่วยมีสิทธิ์ปฏิเสธหรือขอเวลาคิดได้**

**ข้อที่ทำให้เสียคะแนนมาก**
- ใช้ศัพท์แพทย์โดยไม่อธิบาย เช่น "จะเจาะ CSF ส่ง cell count กับ culture"
- **บอกว่า "ไม่มีความเสี่ยงอะไรเลย"** ซึ่งไม่จริงและทำลายความไว้วางใจ
- ไม่ตอบคำถามเรื่องอัมพาตโดยตรง หรือปัดว่า "ไม่ต้องกังวล"
- ไม่ขอความยินยอมอย่างเป็นทางการก่อนจบ""",
 "ref": ["สไลด์ อ.พิมลพรรณ — Lumbar puncture: indications, procedure, complications"],
 "nl": ["2.3.6"], "years": [], "_kind": "meq", "_set": "neuro"}]

LECTURE = {
 "lec": "9/10",
 "title": "หัตถการ: Lumbar puncture และการตรวจตาทางระบบประสาท",
 "subtitle": "ข้อบ่งชี้เพื่อวินิจฉัยและเพื่อการรักษา · ข้อห้าม · สี่เทคนิคที่ลดภาวะแทรกซ้อน · เจ็ดภาวะแทรกซ้อน · รายการส่งตรวจน้ำไขสันหลัง · Snellen และ pinhole · fundoscopy และจอประสาทตาผิดปกติ",
 "objectives": [
   "แยกข้อบ่งชี้ของการเจาะหลังระหว่างเพื่อวินิจฉัยกับเพื่อการรักษาได้",
   "ระบุข้อห้ามและกลุ่มผู้ป่วยที่ต้องทำภาพสมองก่อนเจาะหลัง",
   "อธิบายสี่เทคนิคที่ลดภาวะแทรกซ้อน — ขนาดเข็ม ปริมาณที่ระบาย การห้ามดูด และการใส่ stylet ก่อนถอนเข็ม",
   "จดจำเจ็ดภาวะแทรกซ้อน และรู้จักลักษณะของ post-LP headache",
   "ระบุรายการส่งตรวจน้ำไขสันหลังให้ครบและรู้ว่าต้องเจาะน้ำตาลในเลือดพร้อมกัน",
   "วัดและบันทึกระดับการมองเห็นได้ถูกต้อง รวมถึงแปลผล pinhole test",
   "ส่องจอประสาทตาด้วย direct ophthalmoscope และแยก papilledema, cotton wool spot และ cherry red spot ได้"],
 "sections": S, "meq": [], "osce": OSCE,
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
print("sections %d | items %d | osce %d" % (len(S), sum(len(s["items"]) for s in S), len(OSCE)))
print("neuro.json มี %d คาบ · %d bytes" % (len(data), os.path.getsize(path)))
