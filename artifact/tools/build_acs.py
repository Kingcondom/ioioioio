#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Acute Confusional State and Alteration of Consciousness (อ.พิมลพรรณ เลี่ยนเครือ) → data/neuro.json"""
import json, os

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
LEC = "21/10"
SRC = "สไลด์ อ.พิมลพรรณ เลี่ยนเครือ — Acute Confusional State and Alteration of Consciousness"
NLN = ["2.1.78", "2.2.36"]
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}

sec("neuro-acs-01", "กายวิภาคของความรู้สึกตัว และรอยโรคที่ทำให้โคม่า",
    "ความรู้สึกตัวมีสององค์ประกอบ — arousal จาก ARAS และ content จากเปลือกสมอง รอยโรคที่ทำให้โคม่าต้องกดอย่างใดอย่างหนึ่ง", 10,
"""สไลด์เปิดด้วยโครงสร้างที่ควบคุมความรู้สึกตัว (อ้าง Wijdicks, *The Comatose Patient*, ฉบับที่ 2, 2014) สี่กลุ่ม

| โครงสร้าง | ตำแหน่ง | หน้าที่ |
|---|---|---|
| **Ascending reticular activating system (ARAS)** | **สมองส่วนกลาง (midbrain) และพอนส์ส่วนบน** | ปลุกให้ตื่น — เป็นสวิตช์ของ arousal |
| **Diencephalon** | **ทาลามัสและไฮโปทาลามัส** | สถานีส่งต่อของ ARAS ขึ้นสู่เปลือกสมอง |
| **Anterior cingulate cortex, association cortices** | precuneus, cuneus | ความตื่นรู้ต่อตนเองและสิ่งแวดล้อม |
| **The cortex** | เปลือกสมองทั้งสองซีก | เนื้อหาของความคิด (content) |

### สององค์ประกอบที่ต้องแยกให้ออก

- **Arousal (ความตื่น)** — ลืมตา ตอบสนองต่อสิ่งเร้า ขึ้นกับ **ARAS → diencephalon** เป็นหลัก
- **Content (เนื้อหาของการรู้ตัว)** — รู้ว่าตนเองเป็นใคร อยู่ที่ไหน คิดเป็นเรื่องเป็นราว ขึ้นกับ **เปลือกสมองทั้งสองซีก**

**Delirium คือความผิดปกติของ content เป็นหลัก โดย arousal อาจยังดีอยู่** ส่วน **coma คือความผิดปกติของ arousal**
ทั้งคู่จึงอยู่บนสเปกตรัมเดียวกันแต่คนละแกน และผู้ป่วยคนเดียวกันอาจเลื่อนไปมาระหว่างสองภาวะนี้ได้ในวันเดียว

### คำถามแรกที่สไลด์สั่งให้ถาม

> **"The first course of action is to determine whether the comatose patient is comatose from a lesion in one hemisphere causing mass effect, in both hemispheres or in the posterior fossa."**

แปลเป็นกรอบคิดทางคลินิกได้สามทาง

**1) รอยโรคที่สมองซีกเดียวแต่มี mass effect** — เนื้อสมองบวมหรือเลือดออกจนดันโครงสร้างข้ามเส้นกลาง
กดก้านสมองทางอ้อม (**herniation**) ผู้ป่วยกลุ่มนี้มัก **มีอาการเฉพาะที่นำมาก่อน แล้วค่อยซึมลง**
และเป็นกลุ่มที่ **การผ่าตัดช่วยได้** จึงต้องรีบทำ CT

**2) รอยโรคที่สมองทั้งสองซีก** — พบใน **ภาวะทางเมแทบอลิก สารพิษ ภาวะขาดออกซิเจน และการชักต่อเนื่อง**
กลุ่มนี้มัก **ซึมลงแบบค่อยเป็นค่อยไป ไม่มีอาการเฉพาะที่ และรูม่านตายังตอบสนองต่อแสง**

**3) รอยโรคในโพรงสมองส่วนหลัง (posterior fossa)** — กดหรือทำลาย **ARAS โดยตรง**
เช่น **pontine hemorrhage, basilar artery occlusion, cerebellar infarct ที่บวม**
กลุ่มนี้ **ซึมเร็วมาก มักมีความผิดปกติของก้านสมองร่วมด้วยตั้งแต่แรก** เช่น รูม่านตาผิดปกติ การกลอกตาเสีย

### ทำไมรอยโรคซีกเดียวที่ไม่มี mass effect จึงไม่ทำให้โคม่า

เพราะ **เปลือกสมองอีกซีกยังทำงานได้** ผู้ป่วยที่มีสมองขาดเลือดซีกซ้ายขนาดใหญ่จะ **พูดไม่ได้และอ่อนแรงซีกขวา
แต่ยังลืมตาและตื่นอยู่** ถ้าผู้ป่วยรายนั้น **ซึมลง** ให้คิดถึง **สมองบวมจนเกิด herniation, ชักที่ไม่แสดงอาการ (non-convulsive status),
หรือภาวะแทรกซ้อนทางเมแทบอลิก** ไม่ใช่ผลโดยตรงของรอยโรคเดิม — จุดนี้เป็นประเด็นที่ออกสอบและเจอจริงบ่อยในหอผู้ป่วย
""",
    ["ความรู้สึกตัว = arousal (ARAS/diencephalon) + content (เปลือกสมองสองซีก)",
     "Coma เสียที่ arousal · Delirium เสียที่ content",
     "โคม่าต้องมาจากรอยโรคสองซีก · ซีกเดียวที่มี mass effect · หรือโพรงสมองส่วนหลัง",
     "ผู้ป่วย stroke ซีกเดียวที่จู่ ๆ ซึมลง = สมองบวม ชักเงียบ หรือเหตุทางเมแทบอลิก จนกว่าจะพิสูจน์เป็นอื่น"],
    [
    mcq("NEU-ACS-MCQ-01",
        "A 58-year-old man with a large left middle cerebral artery infarct is awake but globally aphasic and hemiplegic on day 1. On day 3 he becomes progressively drowsy and no longer opens his eyes to voice. Which of the following best explains the new depression of consciousness?",
        ["Cerebral oedema from the infarct causing mass effect and brainstem compression",
         "Extension of the infarct into more of the same left hemisphere",
         "Direct destruction of the left ascending reticular activating system by the infarct",
         "Loss of cortical content from a single dominant hemisphere is sufficient to cause coma",
         "Aphasia itself has progressed and now prevents any response"],
        0,
        """**รอยโรคซีกเดียวไม่ทำให้โคม่าเว้นแต่จะเกิด mass effect** เพราะเปลือกสมองอีกซีกและ ARAS ยังทำงานได้ตามปกติ

**กลไกในผู้ป่วยรายนี้** — สมองขาดเลือดขนาดใหญ่จะบวมสูงสุดใน **วันที่ 2–5** เนื้อสมองที่บวมดันโครงสร้างข้ามเส้นกลาง
เกิด **uncal หรือ subfalcine herniation** ไปกด **ไดเอนเซฟาลอนและก้านสมองส่วนบน** ซึ่งเป็นที่อยู่ของ ARAS ผลคือ **arousal ถูกกด**
ภาวะนี้คือ **malignant MCA infarction** ซึ่งเป็นภาวะฉุกเฉินที่ **decompressive hemicraniectomy ลดอัตราตายได้**

**สิ่งที่ต้องทำทันที** — CT สมองซ้ำเพื่อดูขนาดของ midline shift · ตรวจรูม่านตาซ้ำถี่ ๆ · ประเมินภาวะที่แก้ได้ร่วมด้วย
(น้ำตาลในเลือด โซเดียม ไข้ การชักที่ไม่แสดงอาการ) · ปรึกษาประสาทศัลยแพทย์

**ทำไมข้ออื่นผิด** — **การขยายของรอยโรคในซีกเดิม** จะเพิ่มอาการเฉพาะที่ ไม่ได้กด arousal โดยตรง ·
**ARAS ไม่ได้อยู่ในสมองซีกใดซีกหนึ่ง** แต่อยู่ที่สมองส่วนกลางและพอนส์ส่วนบน และได้เลือดจากระบบ vertebrobasilar ·
**การเสีย content ของซีกเดียวไม่พอที่จะทำให้โคม่า** ตามหลักในสไลด์ ·
**aphasia อธิบายการไม่ตอบสนองทางวาจาได้ แต่อธิบายการไม่ลืมตาไม่ได้** ซึ่งเป็นความแตกต่างที่สำคัญที่สุดในข้อนี้""",
        "Stroke ซีกเดียวที่ซึมลงในวันที่ 2–5 = สมองบวมจนเกิด herniation จนกว่าจะพิสูจน์เป็นอื่น",
        "Anatomy of consciousness — unilateral lesion with mass effect",
        [SRC, "Wijdicks EF. The Comatose Patient, 2nd ed. Oxford University Press, 2014"],
        ["2.2.36", "2.2.39", "2.1.78"]),
    mcq("NEU-ACS-MCQ-02",
        "Which combination of findings best suggests that a comatose patient has a diffuse metabolic or toxic cause rather than a structural lesion?",
        ["Symmetrical examination with preserved pupillary light reflexes and roving eye movements",
         "A unilateral fixed dilated pupil with contralateral hemiparesis",
         "Ocular bobbing with pinpoint pupils",
         "Conjugate lateral eye deviation with a dense hemiplegia",
         "Decerebrate posturing confined to one side of the body"],
        0,
        """**หลักที่ใช้ได้เกือบทุกครั้ง — เหตุทางเมแทบอลิกและสารพิษทำให้สมองเสียหน้าที่อย่างสมมาตรและมักไว้ชีวิตรีเฟล็กซ์ของก้านสมอง โดยเฉพาะรีเฟล็กซ์รูม่านตา**

**เหตุผล** — ทางเดินของรีเฟล็กซ์รูม่านตาทนต่อความผิดปกติทางเมแทบอลิกได้ดีเป็นพิเศษ ผู้ป่วยที่โคม่าลึกจากยานอนหลับ
ตับวาย หรือไตวาย จึงมักยังมี **รูม่านตาเล็กแต่ตอบสนองต่อแสง** ส่วน **roving eye movements** ที่สไลด์ระบุว่า
*"slow, non rhythmic, conjugate, predominantly horizontal"* เป็นสัญญาณของ **เหตุทางเมแทบอลิกหรือสารพิษ
หรือรอยโรคสองข้างเหนือก้านสมอง** และการที่ตายังกลอกไปมาได้เองแปลว่า **ก้านสมองยังทำงาน**

**ข้อยกเว้นที่ต้องจำ** — สารพิษบางชนิดเลียนแบบรอยโรคโครงสร้างได้ เช่น **opioid ทำให้รูม่านตาเล็กมาก**,
**anticholinergic ทำให้รูม่านตาขยายและไม่ตอบสนอง**, **ยาต้านการเกร็งกล้ามเนื้อขนาดสูงและ barbiturate ขนาดสูงมาก
กดรีเฟล็กซ์ก้านสมองได้ทั้งหมด** จึงห้ามวินิจฉัยสมองตายในผู้ที่ยังมีสารเหล่านี้ในร่างกาย

**ทำไมข้ออื่นผิด** — ทุกข้อที่เหลือ **ไม่สมมาตรหรือชี้ตำแหน่งได้ชัด** จึงบ่งถึงรอยโรคโครงสร้าง
**รูม่านตาข้างเดียวขยายค้างร่วมกับอ่อนแรงซีกตรงข้าม** คือ **uncal herniation** กดเส้นประสาทสมองคู่ที่ 3 ·
**ocular bobbing ร่วมกับรูม่านตาเท่าหัวเข็มหมุด** จำเพาะต่อ **รอยโรคเฉียบพลันที่พอนส์** ·
**ตาเบนไปทางเดียวกันร่วมกับอัมพาตครึ่งซีก** บ่งถึงรอยโรคของสมองซีกนั้น (ตามองไปทางรอยโรค) ·
**decerebrate ข้างเดียว** เป็นความไม่สมมาตรที่บ่งรอยโรคโครงสร้างเช่นกัน""",
        "สมมาตร + รูม่านตายังตอบสนอง = คิดถึงเมแทบอลิก/สารพิษ · ไม่สมมาตร = คิดถึงรอยโรคโครงสร้าง",
        "Structural versus metabolic coma",
        [SRC, "Plum and Posner's Diagnosis of Stupor and Coma, 5th ed."],
        ["2.2.36", "2.2.46", "B3.1.2(11)"]),
    ])

sec("neuro-acs-02", "ระดับความรู้สึกตัว และภาวะที่เลียนแบบโคม่า",
    "Alert → lethargy → stupor → coma และสี่ภาวะที่ดูเหมือนโคม่าแต่ไม่ใช่", 10,
"""### สี่ระดับที่สไลด์ให้นิยามไว้

| ระดับ | นิยามตามสไลด์ |
|---|---|
| **Alert** | **Perfectly normal state of arousal** — ตื่นเต็มที่ตามปกติ |
| **Lethargy** | **State lies between alertness and stupor** — ง่วงซึม ปลุกตื่นง่ายแต่หลับกลับไปเมื่อปล่อยไว้ |
| **Stupor** | **State of baseline unresponsiveness that requires repeated application of vigorous stimuli to achieve arousal** — ต้องกระตุ้นแรงและซ้ำ ๆ จึงจะตื่น |
| **Coma** | **State of complete unresponsiveness to arousal** — ปลุกไม่ตื่นเลย ไม่ว่าจะกระตุ้นแรงแค่ไหน |

**ข้อควรระวังในการใช้คำ** — คำเหล่านี้คนละคนใช้ไม่เหมือนกัน เวชระเบียนที่ดีจึง **บรรยายสิ่งที่เห็นจริง**
เช่น *"ลืมตาเมื่อเรียกเสียงดัง หลับกลับใน 5 วินาที ไม่ทำตามสั่ง กดเล็บแล้วดึงแขนหนี"* **แทนการเขียนแค่คำว่า stupor**
แล้วค่อยแปลงเป็นคะแนน GCS หรือ FOUR ควบคู่ไปด้วย

### AVPU Scale — เครื่องมือคัดกรองเร็วที่สุด

| ตัวอักษร | ความหมาย |
|---|---|
| **A — Alert** | ตื่นรู้ตัวดี |
| **V — Voice** | ตอบสนองต่อเสียงเรียก |
| **P — Pain** | ตอบสนองเฉพาะต่อความเจ็บ |
| **U — Unresponsive** | ไม่ตอบสนองเลย |

ใช้ในนาทีแรกของการประเมิน ณ จุดเกิดเหตุหรือหน้าห้องฉุกเฉิน **โดยประมาณเทียบได้กับ GCS**
คือ A ≈ 15, V ≈ 12–13, P ≈ 8, U ≈ 3 และ **"P หรือแย่กว่า" มักเป็นจุดตัดคร่าว ๆ ที่ต้องพิจารณาป้องกันทางเดินหายใจ**

### CONDITIONS THAT MAY MIMIC COMA — สี่ภาวะที่สไลด์เตือน

**1) Locked-in syndrome** — รอยโรคที่ **พอนส์ส่วนหน้า (ventral pons)** มักจาก **basilar artery occlusion** หรือเลือดออก
ทำลาย corticospinal และ corticobulbar tract ทั้งสองข้าง ผู้ป่วย **อัมพาตทั้งตัว พูดไม่ได้ กลืนไม่ได้**
แต่ **ARAS ซึ่งอยู่ด้านหลังของพอนส์ยังดี** จึง **รู้ตัวเต็มที่** และ **ยังกลอกตาขึ้นลงและกะพริบตาได้** เพราะศูนย์ควบคุมการมองขึ้นลงอยู่ที่สมองส่วนกลาง
> **วิธีจับให้ได้ข้างเตียง — สั่งว่า "มองขึ้น มองลง กะพริบตาสองครั้ง" ในผู้ป่วยที่ดูเหมือนโคม่าทุกราย** ใช้เวลา 10 วินาที และเปลี่ยนการวินิจฉัยทั้งหมด

**2) Severe polyneuropathy; AIDP (Guillain-Barré syndrome)** — อ่อนแรงทั้งตัวจนหายใจเองไม่ได้ ดูเหมือนไม่ตอบสนอง แต่ **รู้ตัวดี**
เบาะแสคือ **อาการอ่อนแรงไต่ขึ้นจากขา รีเฟล็กซ์หายไป และมีอาการชา** มาก่อนหน้า

**3) Myasthenia gravis** — ในภาวะ **myasthenic crisis** กล้ามเนื้อทั้งหมดรวมทั้งกล้ามเนื้อลืมตาอ่อนแรงจนดูไม่ตอบสนอง
เบาะแสคือ **หนังตาตก เห็นภาพซ้อน อาการแย่ลงเมื่อใช้งาน และดีขึ้นเมื่อพัก**

**4) Poisoning with neuromuscular blocking agents** — ยาหย่อนกล้ามเนื้อที่ยังไม่ถูกสลายฤทธิ์ หรือการได้รับสารพิษกลุ่มนี้
ผู้ป่วย **ตื่นเต็มที่แต่ขยับไม่ได้เลย** เป็นสถานการณ์ที่โหดร้ายและป้องกันได้ด้วยการ **ให้ยานอนหลับควบคู่เสมอเมื่อใช้ยาหย่อนกล้ามเนื้อ**

**หลักร่วมของทั้งสี่ภาวะ** — ปัญหาอยู่ที่ **ทางออก (efferent pathway)** ไม่ใช่ที่ **ARAS หรือเปลือกสมอง**
การพลาดภาวะเหล่านี้หมายถึงการดูแลผู้ป่วยที่ **รู้สึกตัวและได้ยินทุกอย่าง** ราวกับว่าเขาไม่รับรู้
""",
    ["Alert → lethargy → stupor → coma · บรรยายสิ่งที่เห็นจริงดีกว่าใช้คำเหล่านี้ลอย ๆ",
     "AVPU ใช้ในนาทีแรก · ระดับ P หรือแย่กว่า ให้คิดถึงการป้องกันทางเดินหายใจ",
     "สี่ภาวะที่เลียนแบบโคม่า: locked-in · AIDP · MG crisis · ยาหย่อนกล้ามเนื้อ",
     "สั่ง 'มองขึ้น มองลง กะพริบตาสองครั้ง' กับผู้ป่วยที่ดูเหมือนโคม่าทุกราย เพื่อไม่พลาด locked-in"],
    [
    mcq("NEU-ACS-MCQ-03",
        "A 62-year-old hypertensive man is brought in unresponsive with quadriplegia. He does not respond to voice or pain, but the nurse notices he opens and closes his eyes and looks up when asked. Which lesion best explains this picture?",
        ["Bilateral thalamic infarction",
         "Ventral pontine lesion, typically from basilar artery occlusion",
         "Diffuse hypoxic-ischaemic injury of both hemispheres",
         "Bilateral medullary infarction",
         "Complete spinal cord transection at C2"],
        1,
        """**นี่คือ locked-in syndrome** ตามที่สไลด์ระบุไว้ในหัวข้อ *CONDITIONS THAT MAY MIMIC COMA*

**กายวิภาคที่ทำให้อธิบายได้ทุกอาการ**
- รอยโรคอยู่ที่ **พอนส์ด้านหน้า** ตัด **corticospinal tract** ทั้งสองข้าง → **อัมพาตแขนขาทั้งสี่**
- ตัด **corticobulbar tract** → **พูดไม่ได้ กลืนไม่ได้ สีหน้าไร้การเคลื่อนไหว**
- **ARAS อยู่ที่ tegmentum ด้านหลังของพอนส์และสมองส่วนกลาง จึงรอด** → **ผู้ป่วยรู้ตัวเต็มที่**
- **ศูนย์ควบคุมการมองในแนวดิ่งอยู่ที่สมองส่วนกลาง (rostral interstitial nucleus of MLF) ซึ่งอยู่เหนือรอยโรค** → **ยังมองขึ้นลงและกะพริบตาได้**
- สาเหตุที่พบบ่อยที่สุดคือ **basilar artery occlusion** ซึ่งเป็นภาวะที่ **ต้องรีบทำ CTA และพิจารณาการเปิดหลอดเลือด** ทันที

**ทำไมข้ออื่นผิด** — **ทาลามัสสองข้างขาดเลือด** (เช่นจาก artery of Percheron) ทำให้ซึมลงจริง แต่ **ไม่ทำให้อัมพาตทั้งสี่แขนขา
และมักมีการมองขึ้นลงผิดปกติ** · **สมองขาดออกซิเจนทั่วสมอง** จะเสียการรู้ตัวจริง ไม่ใช่รู้ตัวดี ·
**เมดัลลาขาดเลือดสองข้าง** จะกระทบการหายใจและการกลืนอย่างรุนแรงจนมักเสียชีวิต และ **ไม่ไว้ชีวิตการกลอกตา** ·
**ไขสันหลังขาดที่ระดับ C2** ทำให้อัมพาตทั้งสี่และหายใจเองไม่ได้ แต่ **การกลอกตาและการกะพริบตายังปกติทั้งหมด
และผู้ป่วยยังพูดได้ถ้ามีทางเดินหายใจ** ต่างจากรายนี้ที่พูดไม่ได้เลย""",
        "ดูเหมือนโคม่า + อัมพาตทั้งตัว + มองขึ้นลงและกะพริบตาได้ = locked-in จาก ventral pons ให้รีบหา basilar occlusion",
        "Locked-in syndrome",
        [SRC], ["2.2.36", "2.2.39"]),
    mcq("NEU-ACS-MCQ-04",
        "According to the AVPU scale used in the initial survey, a patient who withdraws his arm when the nail bed is compressed but does not open his eyes or respond to loud voice should be recorded as which level?",
        ["A", "V", "P", "U", "AVPU cannot be applied once the patient is intubated"],
        2,
        """**P = Pain** — ผู้ป่วยตอบสนองเฉพาะต่อสิ่งเร้าที่เจ็บเท่านั้น

**AVPU ทั้งสี่ระดับ** — **A** ตื่นรู้ตัวดี · **V** ตอบสนองต่อเสียง · **P** ตอบสนองต่อความเจ็บ · **U** ไม่ตอบสนองเลย

**ทำไมระดับ P สำคัญทางคลินิก** — เทียบได้กับ **GCS ราว 8** ซึ่งเป็นจุดที่ผู้ป่วย **มักป้องกันทางเดินหายใจของตนเองไม่ได้**
ควรประเมินรีเฟล็กซ์การกลืนและการไอ ดูดเสมหะ จัดท่า และ **พิจารณาใส่ท่อช่วยหายใจ** โดยไม่รอให้เกิดการสำลัก
พร้อมกับ **เจาะน้ำตาลปลายนิ้วทันที** ตามลำดับที่สไลด์ย้ำไว้

**ทำไมข้ออื่นผิด** — **A** ใช้กับผู้ที่ตื่นเองและรู้ตัว · **V** ใช้เมื่อยังตอบสนองต่อเสียงเรียก ซึ่งรายนี้ไม่มี ·
**U** ใช้เมื่อไม่ตอบสนองต่อความเจ็บเลย · **AVPU ใช้ได้ในผู้ป่วยใส่ท่อช่วยหายใจ** เพราะไม่ต้องอาศัยการพูด
ซึ่งต่างจาก GCS ที่มีข้อจำกัดตรงนี้พอดี""",
        "AVPU ระดับ P ≈ GCS 8 = จุดที่ต้องคิดเรื่องป้องกันทางเดินหายใจ",
        "AVPU scale",
        [SRC], ["2.2.36"]),
    ])

sec("neuro-acs-03", "Glasgow Coma Scale และข้อจำกัดที่สไลด์ชี้ไว้",
    "E4 V5 M6 รวม 3–15 · จุดบอดสองข้อคือผู้ป่วยใส่ท่อช่วยหายใจ และการมองไม่เห็นรีเฟล็กซ์ก้านสมอง", 10,
"""### ตารางคะแนน

| องค์ประกอบ | คะแนน | เกณฑ์ |
|---|---|---|
| **Eye opening (E)** | **4** | Spontaneous — ลืมตาเอง |
| | **3** | To speech — ลืมตาเมื่อเรียก |
| | **2** | To pain — ลืมตาเมื่อเจ็บ |
| | **1** | None |
| **Best verbal response (V)** | **5** | Oriented — บอกชื่อ สถานที่ เวลาได้ถูก |
| | **4** | Confused — พูดเป็นประโยคแต่สับสน |
| | **3** | Inappropriate words — พูดเป็นคำ ๆ ไม่เข้าเรื่อง |
| | **2** | Incomprehensible sounds — ส่งเสียงไม่เป็นคำ |
| | **1** | None |
| **Best motor response (M)** | **6** | Obeys commands |
| | **5** | Localizes pain — ยกมือมาปัดที่เจ็บ |
| | **4** | Withdraws to pain — ดึงหนี |
| | **3** | Abnormal flexion (**decorticate**) |
| | **2** | Abnormal extension (**decerebrate**) |
| | **1** | None |

**คะแนนรวม = E + V + M มีค่า 3 ถึง 15** และ **ต้องรายงานแยกเป็นองค์ประกอบเสมอ** เช่น *E2 V2 M4 = 8*
เพราะ **คะแนนรวมเท่ากันอาจมาจากคนละภาวะ** — ผู้ป่วย **E4 V1 M3 (8)** กับ **E1 V2 M5 (8)** มีการพยากรณ์โรคและสาเหตุต่างกันมาก

### กติกาที่มักทำผิด

- **ใช้ "best response" เสมอ** — ถ้าแขนขวาทำตามสั่งได้แต่แขนซ้ายไม่ขยับ ให้คิด **M6** แล้วบันทึกความไม่สมมาตรแยกไว้
  (**ความไม่สมมาตรมีค่าในการระบุตำแหน่งรอยโรคมากกว่าตัวคะแนนเสียอีก**)
- **สิ่งเร้าที่เจ็บต้องเป็นมาตรฐาน** — กดเหนือเบ้าตา กด trapezius หรือกดโคนเล็บ **ห้ามใช้วิธีที่ทำให้บาดเจ็บ**
- **การดึงหนี (M4) กับการปัดที่เจ็บ (M5) ต่างกันตรงที่ M5 มือต้องข้ามเส้นกลางตัวมาหาจุดที่เจ็บ**
- **M3 decorticate งอศอก · M2 decerebrate เหยียดศอก** — จำง่าย ๆ ว่า *"งอเข้าหาแกนกลาง (core) = decorticate"*
- ถ้าตาบวมปิดจนลืมไม่ได้ให้บันทึก **E1c (closed)** ถ้าใส่ท่อช่วยหายใจให้บันทึก **V1T**

### สองข้อจำกัดที่สไลด์เน้น

**1) Blind Spot — ใช้กับผู้ป่วยที่ใส่ท่อช่วยหายใจไม่ได้ เพราะองค์ประกอบด้านการพูดล้มเหลวทั้งหมด**
ในหอผู้ป่วยวิกฤต **ผู้ป่วยส่วนใหญ่ใส่ท่อช่วยหายใจ** เครื่องมือที่พึ่งการพูด **1 ใน 3 ส่วน** จึงใช้ไม่ได้จริงในกลุ่มที่ต้องการติดตามมากที่สุด

**2) Missed Signals — ตรวจไม่พบรีเฟล็กซ์ก้านสมองและ locked-in syndrome**
> **"Patients with a GCS of 3 often still have intact brainstem function."**

นี่คือประโยคที่สำคัญที่สุดของหัวข้อนี้ — **GCS 3 ไม่ได้แปลว่าก้านสมองตาย** ผู้ป่วยที่ได้ยานอนหลับขนาดสูง
ผู้ป่วย locked-in และผู้ป่วยที่อ่อนแรงจากโรคของเส้นประสาทส่วนปลาย **ได้ GCS 3 ได้ทั้งนั้นทั้งที่รีเฟล็กซ์ก้านสมองยังครบ**
การพยากรณ์โรคและการตัดสินใจถอนการรักษาจึง **ห้ามอาศัย GCS เพียงอย่างเดียว**
""",
    ["รายงาน GCS แยกเป็น E, V, M เสมอ — คะแนนรวมเท่ากันมาจากคนละภาวะได้",
     "M5 localize ต้องข้ามเส้นกลางตัวมาหาจุดเจ็บ · M4 แค่ดึงหนี",
     "GCS ใช้ไม่ได้เต็มที่ในผู้ป่วยใส่ท่อช่วยหายใจ เพราะเสียองค์ประกอบด้านการพูด",
     "GCS 3 ไม่เท่ากับก้านสมองตาย — ผู้ป่วยจำนวนมากยังมีรีเฟล็กซ์ก้านสมองครบ"],
    [
    mcq("NEU-ACS-MCQ-05",
        "An intubated patient opens his eyes to painful stimulation only and brings his right hand across the midline to the supraorbital notch when pressure is applied there. How should his Glasgow Coma Scale be recorded?",
        ["E2 V1T M5 = 8T", "E2 V1T M4 = 7T", "E2 V2 M5 = 9", "E1 V1T M5 = 7T", "GCS cannot be scored in an intubated patient"],
        0,
        """**E2** — ลืมตาเฉพาะเมื่อเจ็บ · **V1T** — ใส่ท่อช่วยหายใจ ให้ลงคะแนนต่ำสุดพร้อมกำกับตัว **T** · **M5** — **ปัดมือข้ามเส้นกลางตัวมาหาจุดที่เจ็บ คือ localizing**
รวม **8T**

**จุดตัดสินที่ข้อนี้ทดสอบ** — **การแยก M5 จาก M4**
- **M5 (localizes)** — มือ **เคลื่อนข้ามเส้นกลางตัว** มาหาตำแหน่งที่ถูกกระตุ้น แสดงว่ายังมีการรับรู้ตำแหน่งและวงจรที่ซับซ้อนกว่า
- **M4 (withdraws)** — แค่ **ดึงแขนหนี** จากสิ่งเร้า เป็นปฏิกิริยาระดับไขสันหลังที่ง่ายกว่า

**ทำไม M5 สำคัญ** — เป็น **ตัวทำนายผลลัพธ์ที่ดีที่สุดในบรรดาองค์ประกอบทั้งสามของ GCS**
ผู้ป่วยที่ localize ได้มีการพยากรณ์โรคดีกว่าผู้ป่วยที่ทำได้แค่ดึงหนีอย่างมีนัยสำคัญ

**เรื่องตัว T** — เมื่อใส่ท่อช่วยหายใจ ให้บันทึก **V1T** และรายงานคะแนนรวมพร้อมตัว T กำกับ
แต่ตามที่สไลด์ชี้ นี่คือ **จุดบอดของ GCS** ที่ **FOUR score แก้ได้โดยตัดองค์ประกอบด้านการพูดทิ้งทั้งหมด**

**ทำไมข้ออื่นผิด** — **M4** ต่ำไปเพราะผู้ป่วยข้ามเส้นกลางตัวได้ · **V2** ให้ไม่ได้ในผู้ป่วยใส่ท่อช่วยหายใจ ·
**E1** ผิดเพราะผู้ป่วยลืมตาเมื่อเจ็บ · **GCS ยังใช้ได้ในผู้ป่วยใส่ท่อช่วยหายใจ** เพียงแต่เสียองค์ประกอบด้านการพูดไป""",
        "ข้ามเส้นกลางตัวมาหาจุดเจ็บ = M5 localize · แค่ดึงหนี = M4 · ใส่ท่อ = V1T",
        "GCS scoring in the intubated patient",
        [SRC], ["2.2.36"]),
    mcq("NEU-ACS-MCQ-06",
        "Which statement about the Glasgow Coma Scale is emphasised as a limitation in this lecture?",
        ["A GCS of 3 reliably indicates absent brainstem function",
         "A GCS of 3 is compatible with entirely intact brainstem reflexes",
         "The verbal component is the strongest predictor of outcome",
         "GCS detects locked-in syndrome better than the FOUR score",
         "GCS includes an assessment of respiratory pattern"],
        1,
        """สไลด์เขียนไว้ตรง ๆ ว่า **"Patients with a GCS of 3 often still have intact brainstem function."**

**ทำไมเรื่องนี้ถึงสำคัญถึงชีวิต** — GCS ประเมินเพียง **การลืมตา การพูด และการเคลื่อนไหว** ซึ่งทั้งสามอย่าง
**ต้องอาศัยทางออกของระบบประสาทที่ทำงานได้** ถ้าทางออกถูกปิดกั้น ไม่ว่าจะจาก **ยาหย่อนกล้ามเนื้อ ยานอนหลับ
รอยโรคที่พอนส์ด้านหน้า หรือโรคของเส้นประสาทส่วนปลาย** ผู้ป่วยก็ได้ **GCS 3** ได้ทั้งที่ **ก้านสมองยังทำงานครบถ้วน
และในบางรายรู้ตัวเต็มที่**

**ผลทางปฏิบัติ** — ก่อนใช้คะแนนต่ำในการพยากรณ์โรคหรือคุยเรื่องการจำกัดการรักษา ต้อง
**ตรวจรีเฟล็กซ์ก้านสมองโดยตรง** (รูม่านตา กระจกตา doll's eye การไอ) · **ตัดผลของยาที่ยังคงค้างออกไปก่อน** ·
และ **สั่งให้มองขึ้นลงหรือกะพริบตา** เพื่อไม่ให้พลาด locked-in syndrome

**ทำไมข้ออื่นผิด** — **การบอกว่า GCS 3 แปลว่าก้านสมองตาย** เป็นความเข้าใจผิดที่สไลด์เตือนไว้โดยเฉพาะ ·
**องค์ประกอบด้านการเคลื่อนไหว (M) ไม่ใช่การพูด ที่ทำนายผลลัพธ์ได้ดีที่สุด** ·
**FOUR score ต่างหากที่จับ locked-in ได้ดีกว่า** เพราะให้คะแนน E4 แก่ผู้ที่กะพริบตาหรือมองตามคำสั่ง ·
**GCS ไม่มีการประเมินรูปแบบการหายใจ** ซึ่งเป็นสิ่งที่ FOUR score เพิ่มเข้ามา""",
        "GCS 3 ≠ ก้านสมองตาย — ต้องตรวจรีเฟล็กซ์ก้านสมองเองเสมอก่อนพยากรณ์โรค",
        "Limitations of the GCS",
        [SRC], ["2.2.36"]),
    ])

sec("neuro-acs-04", "FOUR Score — เครื่องมือที่ออกแบบมาแก้จุดบอดของ GCS",
    "Full Outline of UnResponsiveness · E, M, B, R อย่างละ 0–4 รวม 0–16 · ใช้ได้แม้ใส่ท่อช่วยหายใจ", 12,
"""**FOUR = Full Outline of UnResponsiveness** เป็นมาตรวัด **17 ระดับ (0 ถึง 16)** พัฒนาที่ **Mayo Clinic (2005)**
ประกอบด้วยสี่องค์ประกอบ **อย่างละ 0–4 คะแนน** โดย **ไม่มีองค์ประกอบด้านการพูดเลย**

### E — Eye Response

| คะแนน | เกณฑ์ |
|---|---|
| **4** | **eyelids open or opened, tracking, or blinking to command** — ลืมตาและมองตามหรือกะพริบตาตามสั่ง |
| **3** | eyelids open but not tracking — ลืมตาแต่ไม่มองตาม |
| **2** | eyelids closed but open to loud voice |
| **1** | eyelids closed but open to pain |
| **0** | eyelids remain closed with pain |

> **E4 คือคำสั่ง "look up, look down, blink twice" ที่ปรากฏในสไลด์** — องค์ประกอบนี้เองที่ทำให้ **FOUR score จับ locked-in syndrome ได้**

### M — Motor Response

| คะแนน | เกณฑ์ |
|---|---|
| **4** | **thumbs-up, fist, or peace sign** — ทำท่าตามสั่งได้สามท่า |
| **3** | localizing to pain |
| **2** | flexion response to pain (**decorticate**) |
| **1** | extension response to pain (**decerebrate**) |
| **0** | **no response to pain or generalized myoclonus status** |

> **M0 รวม generalized myoclonus status ไว้ด้วย** ซึ่งเป็นสัญญาณพยากรณ์โรคที่เลวร้ายหลังภาวะหัวใจหยุดเต้น — GCS ไม่มีช่องให้บันทึกสิ่งนี้เลย

### B — Brainstem Reflexes

| คะแนน | เกณฑ์ |
|---|---|
| **4** | pupillary and corneal reflexes present |
| **3** | **one pupil wide and fixed** |
| **2** | pupillary **or** corneal reflexes absent |
| **1** | pupillary **and** corneal reflexes absent |
| **0** | absent pupillary, corneal, **and cough** reflex |

> **B3 ให้ค่ากับรูม่านตาข้างเดียวที่ขยายค้าง** ซึ่งเป็นสัญญาณของ **uncal herniation** ที่ต้องลงมือทันที

### R — Respiration

| คะแนน | เกณฑ์ |
|---|---|
| **4** | not intubated, regular breathing pattern |
| **3** | not intubated, **Cheyne-Stokes** breathing pattern |
| **2** | not intubated, irregular breathing pattern |
| **1** | **intubated, breathes above ventilator rate** |
| **0** | intubated, breathes at ventilator rate or apnea |

> **R1 กับ R0 แยกผู้ป่วยที่ยังมี respiratory drive ของตนเองออกจากผู้ที่ไม่มี** ซึ่งเป็นข้อมูลก้านสมองที่สำคัญและ **หาไม่ได้จาก GCS**

### FOUR Score Advantages — สี่ข้อตามสไลด์

| ข้อดี | สาระ |
|---|---|
| **Meaning** | Full Outline of UnResponsiveness (17-point scale, 0 to 16) |
| **Intubation Proof** | **ตัดความจำเป็นของการตอบสนองด้านการพูดออกไปทั้งหมด** |
| **Neurological Granularity** | **รวมรีเฟล็กซ์ก้านสมองที่สำคัญและรูปแบบการหายใจที่จำเพาะเข้าไว้ด้วย** |
| **Predictive Power** | **AUROC สูงกว่าในการทำนายอัตราตายในหอผู้ป่วยวิกฤต และจับการเปลี่ยนแปลงที่มีความหมายในผู้ป่วยที่ระดับความรู้สึกตัวต่ำได้ดีกว่า** |

**ประเด็นสุดท้ายนี้คือเหตุผลที่แท้จริงที่ควรใช้ FOUR score** — ผู้ป่วยที่ **GCS ติดอยู่ที่ 3 มาสามวัน**
อาจมี **FOUR score เปลี่ยนจาก 4 เป็น 9** เพราะรีเฟล็กซ์ก้านสมองกลับมา **GCS ตกพื้น (floor effect)
แต่ FOUR score ยังแยกความต่างได้** ซึ่งสำคัญมากในกลุ่มผู้ป่วยที่แย่ที่สุดและตัดสินใจยากที่สุด
""",
    ["FOUR = E + M + B + R อย่างละ 0–4 รวม 0–16 และไม่มีองค์ประกอบด้านการพูด",
     "E4 = กะพริบตาหรือมองตามคำสั่ง จึงจับ locked-in syndrome ได้",
     "B3 = รูม่านตาข้างเดียวขยายค้าง = สัญญาณ uncal herniation",
     "R1 vs R0 แยกผู้ที่ยังมี respiratory drive — ข้อมูลที่ GCS ไม่มี",
     "จุดแข็งจริงคือไม่มี floor effect ที่ปลายล่างของสเกล"],
    [
    mcq("NEU-ACS-MCQ-07",
        "A ventilated patient in the ICU opens his eyes to loud voice but does not track, shows flexion to pain, has absent corneal reflexes with reactive pupils, and triggers breaths above the set ventilator rate. What is his FOUR score?",
        ["E2 M2 B2 R1 = 7", "E2 M2 B4 R1 = 9", "E3 M2 B2 R1 = 8", "E2 M1 B2 R0 = 5", "E2 M2 B3 R1 = 8"],
        0,
        """**E2** — ตาปิดแต่ลืมเมื่อเรียกเสียงดัง · **M2** — งอแขนตอบสนองต่อความเจ็บ (decorticate) ·
**B2** — **รีเฟล็กซ์รูม่านตาหรือกระจกตาอย่างใดอย่างหนึ่งหายไป** ในรายนี้กระจกตาหายแต่รูม่านตายังดี ·
**R1** — **ใส่ท่อช่วยหายใจและหายใจเองเหนืออัตราที่ตั้งไว้**
รวม **2 + 2 + 2 + 1 = 7**

**จุดที่ข้อนี้ทดสอบ — บันไดของ B**
- **B4** รีเฟล็กซ์รูม่านตาและกระจกตาอยู่ครบ
- **B3** **รูม่านตาข้างเดียวขยายค้าง** (คะแนนแยกออกมาเพราะเป็นสัญญาณ herniation)
- **B2** **เสียอย่างใดอย่างหนึ่ง** ← รายนี้
- **B1** เสียทั้งสองอย่าง
- **B0** เสียทั้งรูม่านตา กระจกตา และรีเฟล็กซ์การไอ

**ความหมายทางคลินิกของ R1** — การที่ผู้ป่วยหายใจ **เหนืออัตราที่เครื่องตั้งไว้** แปลว่า **ศูนย์หายใจในก้านสมองยังทำงาน**
เป็นข้อมูลก้านสมองที่มีค่าและ **GCS บันทึกไม่ได้เลย** ถ้าวันต่อมาผู้ป่วยหายใจตามเครื่องพอดีหรือหยุดหายใจ
คะแนนจะตกเป็น **R0** ซึ่งเป็น **การเปลี่ยนแปลงที่มีความหมายและตรวจจับได้ทันที**

**ทำไมข้ออื่นผิด** — **B4** ผิดเพราะรีเฟล็กซ์กระจกตาหายไปแล้ว · **E3** ใช้กับผู้ที่ลืมตาอยู่แล้วแต่ไม่มองตาม
ซึ่งต่างจากรายนี้ที่ตาปิดจนกว่าจะเรียก · **M1** คือท่าเหยียด ไม่ใช่ท่างอ · **B3** สงวนไว้สำหรับรูม่านตาข้างเดียวที่ขยายค้าง""",
        "FOUR score: E ตามการลืมตา/มองตาม · M ตามท่าทาง · B ตามรีเฟล็กซ์ · R ตามการหายใจกับเครื่อง",
        "FOUR score calculation",
        [SRC, "Wijdicks EFM et al. Validation of a new coma scale: The FOUR score. Ann Neurol 2005;58:585-593"],
        ["2.2.36"]),
    mcq("NEU-ACS-MCQ-08",
        "Which advantage of the FOUR score over the GCS is most relevant when following a deeply comatose, intubated patient from day to day?",
        ["It avoids a floor effect and still discriminates change at the bottom of the scale",
         "It is faster to perform than the GCS",
         "It replaces the need for neuroimaging",
         "It can be scored by family members at the bedside",
         "It gives a single number that determines prognosis with certainty"],
        0,
        """สไลด์ระบุข้อดีข้อสุดท้ายว่า **"Predictive Power: Statistically higher AUROC for predicting ICU mortality
and detecting clinically meaningful changes in low-consciousness states."**

**ปัญหา floor effect ของ GCS** — เมื่อผู้ป่วยถึง **GCS 3 (E1 V1 M1)** ก็ไม่มีที่ให้ลงต่ำกว่านั้นและไม่มีที่ให้ขยับขึ้น
จนกว่าจะเริ่มขยับตัวได้ ผู้ป่วยหอผู้ป่วยวิกฤตจำนวนมาก **ค้างอยู่ที่ 3 หรือ 3T หลายวัน** ทั้งที่ภาวะจริงเปลี่ยนไปมาก

**FOUR score แก้ปัญหานี้ได้อย่างไร** — เพราะยัง **วัดรีเฟล็กซ์ก้านสมอง (B) และการหายใจ (R) ต่อไปได้**
ผู้ป่วยที่ **GCS 3T คงที่** อาจมีคะแนน FOUR เปลี่ยนจาก **E0 M0 B1 R0 = 1** เป็น **E1 M1 B3 R1 = 6**
ซึ่งเป็นการดีขึ้นที่ **มีความหมายและตรวจจับได้** หรือในทางกลับกัน **B4 → B2 → B1** คือการทรุดลงของก้านสมองที่ต้องรีบหาเหตุ

**ทำไมข้ออื่นผิด** — **ไม่ได้เร็วกว่า** อันที่จริง **ใช้เวลานานกว่าเล็กน้อย** เพราะต้องตรวจรีเฟล็กซ์ก้านสมอง ·
**ไม่มีมาตรวัดใดแทนภาพสมองได้** โดยเฉพาะเมื่อสงสัยรอยโรคโครงสร้าง ·
**ต้องใช้ผู้ที่ฝึกตรวจรีเฟล็กซ์กระจกตาและรูม่านตามาแล้ว** ไม่ใช่ญาติผู้ป่วย ·
**ไม่มีคะแนนเดี่ยวใดทำนายผลลัพธ์ได้อย่างแน่นอน** — การพยากรณ์โรคต้องอาศัยหลายตัวแปรร่วมกันและต้องรอให้พ้นผลของยา""",
        "จุดแข็งของ FOUR score คือยังแยกความต่างได้ที่ก้นสเกล ซึ่งเป็นจุดที่ GCS ตัน",
        "Why FOUR score beats GCS in the ICU",
        [SRC], ["2.2.36"]),
    ])
