from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Neuro"

# ---------------------------------------------------------------- 02-01 Stroke syndromes by vessel
F_TERR = fig("neuro-02-01-f1", "หลอดเลือดสมอง → ส่วนของร่างกายที่อ่อนแรง", '''<svg viewBox="0 0 740 400">
 <defs><marker id="neuro-02-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <text x="370" y="22" text-anchor="middle" class="tb">Motor cortex (homunculus) จาก medial → lateral</text>
 <rect x="40" y="40" width="130" height="50" rx="8" class="c2soft"/>
 <text x="105" y="70" text-anchor="middle" class="tb">ขา · เท้า</text>
 <rect x="175" y="40" width="90" height="50" rx="8" class="c2soft"/>
 <text x="220" y="70" text-anchor="middle" class="t2">ลำตัว</text>
 <rect x="270" y="40" width="150" height="50" rx="8" class="c1soft"/>
 <text x="345" y="70" text-anchor="middle" class="tb">แขน · มือ</text>
 <rect x="425" y="40" width="150" height="50" rx="8" class="c1soft"/>
 <text x="500" y="70" text-anchor="middle" class="tb">หน้า</text>
 <rect x="580" y="40" width="120" height="50" rx="8" class="c1soft"/>
 <text x="640" y="62" text-anchor="middle" class="tb">ภาษา</text>
 <text x="640" y="80" text-anchor="middle" class="t3">(dominant)</text>
 <path d="M40 104H265" class="lnc2"/>
 <path d="M270 104H700" class="lnc1"/>
 <text x="152" y="124" text-anchor="middle" class="tb">ACA</text>
 <text x="485" y="124" text-anchor="middle" class="tb">MCA</text>
 <rect x="20" y="146" width="220" height="112" rx="10" class="box"/>
 <text x="130" y="170" text-anchor="middle" class="tb">ACA</text>
 <text x="32" y="194" class="t2">Hemiparesis ซีกตรงข้าม</text>
 <text x="32" y="214" class="t2"><tspan class="tb">ขา &gt; แขน</tspan> + sensory</text>
 <text x="32" y="234" class="t2">Urinary incontinence</text>
 <rect x="255" y="146" width="235" height="112" rx="10" class="box"/>
 <text x="372" y="170" text-anchor="middle" class="tb">MCA</text>
 <text x="272" y="194" class="t2">Hemiparesis ซีกตรงข้าม</text>
 <text x="272" y="214" class="t2"><tspan class="tb">หน้า + แขน &gt; ขา</tspan> + sensory</text>
 <text x="272" y="234" class="t2">Aphasia (dominant), gaze deviation</text>
 <rect x="500" y="146" width="220" height="112" rx="10" class="box"/>
 <text x="610" y="170" text-anchor="middle" class="tb">PCA</text>
 <text x="512" y="194" class="t2">Occipital lobe</text>
 <text x="512" y="214" class="t2">Contralateral homonymous</text>
 <text x="512" y="234" class="t2">hemianopia, <tspan class="tb">macular sparing</tspan></text>
 <rect x="20" y="276" width="700" height="112" rx="10" class="misssoft"/>
 <text x="370" y="300" text-anchor="middle" class="tb">PICA / vertebral a. → Lateral medullary (Wallenberg) syndrome</text>
 <text x="36" y="326" class="tb">ข้างเดียวกับ lesion</text>
 <text x="36" y="346" class="t2">กลืนลำบาก ↓gag เสียงแหบ (CN 9,10) · ataxia, dysmetria</text>
 <text x="36" y="366" class="t2">vertigo N/V nystagmus · Horner · เสีย pain/temp ที่หน้า</text>
 <text x="480" y="326" class="tb">ข้างตรงข้าม</text>
 <text x="480" y="346" class="t2">เสีย pain/temp ลำตัวและแขนขา</text>
 <text x="480" y="366" class="t3">ไม่มี hemiparesis เด่น</text>
</svg>''', "แถบบนคือ motor cortex เรียงจาก medial (ขา) ไป lateral (หน้า ภาษา): ACA เลี้ยงส่วนขา MCA เลี้ยงหน้า-แขน-ภาษา ส่วน PCA เลี้ยงสมองส่วนการมองเห็น")

S1 = sec("neuro-02-01", "Stroke: ชนิดและอาการตามหลอดเลือด",
    "Ischemic 80% · hemorrhagic 20% · ACA ขา>แขน · MCA หน้า+แขน>ขา+aphasia · PCA hemianopia macular sparing · Wallenberg = PICA/VA", minutes=8,
    source=f"{D} หน้า 7, 26–28, 43–54", nl=["B3.2.6(1)", "2.2.39", "B3.1.1(10)"],
    md='''
### ชนิดของ stroke

- **Ischemic stroke (80%)** — รวม **TIA** = focal neurological deficit ชั่วคราว (ตามสไลด์ < 1 ชั่วโมง) แล้วหายสนิท
- **Hemorrhagic stroke (20%)** — **intracerebral hemorrhage (ICH)** และ **subarachnoid hemorrhage (SAH)** (SAH ดูหมวด headache)

### อาการตามหลอดเลือด

[[fig:neuro-02-01-f1]]

| หลอดเลือด | อาการเด่น |
|---|---|
| **ACA** | Hemiparesis + sensory ซีกตรงข้าม **ขา > แขน**, incontinence |
| **MCA** | Hemiparesis + sensory ซีกตรงข้าม **หน้าและแขน > ขา**, **aphasia** (ถ้า dominant hemisphere), eye deviation ไปด้าน lesion |
| **PCA** | **Contralateral homonymous hemianopia with macular sparing** |
| **PICA / vertebral a.** | **Lateral medullary (Wallenberg)**: ipsilateral dysphagia ↓gag hoarseness, ataxia dysmetria dysdiadochokinesia, vertigo N/V nystagmus, **Horner**, เสีย pain/temp ที่หน้า · contralateral เสีย pain/temp ที่ลำตัวแขนขา |
| **Basilar** (เสริม) | ซึม/coma, bilateral CN palsy (เช่น CN6), quadriparesis — locked-in ได้ |
| **Lenticulostriate** | Lacunar syndrome (ดูหัวข้อถัดไป) |

- **Vertebral artery dissection** ถูกกระตุ้นได้จากการ **นวด/บิดคอ** หรือ trauma → ปวดคอ + อาการ posterior circulation (Wallenberg, cerebellar)

### Hypertensive ICH

- ความดันสูงเรื้อรัง → หลอดเลือดเล็ก (lenticulostriate) แตก
- **Common site: putamen (basal ganglia) > thalamus, pons, cerebellum**
- อาการ: ปวดศีรษะรุนแรง คลื่นไส้อาเจียน (↑ICP) + อ่อนแรงซีกตรงข้ามรุนแรง ความดันสูงมาก
- CT non-contrast เห็น **hyperdense lesion**

> โจทย์ "ปวดหัวมาก + อาเจียน + hemiplegia + BP สูง" = **ICH (basal ganglia)** ไม่ใช่ ischemic stroke ทั่วไปที่มักไม่ปวดหัว
''',
    figs=[F_TERR],
    pearls=[
        "Ischemic 80% · hemorrhagic 20% (ICH, SAH)",
        "ACA ขา>แขน + incontinence · MCA หน้า+แขน>ขา + aphasia",
        "PCA = homonymous hemianopia with macular sparing",
        "Wallenberg: Horner + ataxia + ชาหน้าข้างเดียวกัน/ชาตัวข้างตรงข้าม",
        "Hypertensive ICH ที่พบบ่อยสุด: putamen",
    ],
    items=[
        mcq("NEURO-02-01-1",
            "An elderly Thai man with diabetes and hypertension has numbness and weakness of one side of the body lasting 10 minutes, followed by complete recovery. Neurological examination is now normal. What is the most likely diagnosis?",
            "Transient ischemic attack",
            ["Temporal lobe ischemia", "Cerebellar ischemia", "Bell's palsy", "Todd's paralysis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 43–44)",
            explain='''Focal deficit (ชา + อ่อนแรงครึ่งซีก) ที่หายสนิทภายในเวลาสั้น (< 1 ชั่วโมงตามสไลด์) ในคนมี vascular risk = **TIA** ซึ่งต้องดูแลเหมือน ischemic stroke (หาสาเหตุ + secondary prevention) แต่ไม่ต้อง thrombolysis
- Temporal lobe ischemia ไม่ทำให้อ่อนแรงครึ่งซีกเป็นอาการหลัก (จะเด่นด้านความจำ/ภาษา/ชัก)
- Cerebellar ischemia ทำให้เดินเซ ataxia ไม่ใช่ hemiparesis + ชา
- Bell's palsy เป็น LMN facial palsy ไม่มีแขนขาอ่อนแรง
- Todd's paralysis ต้องเกิดหลังชัก (ตัวลวงเสริม)''',
            pearl="Deficit หายสนิทเร็ว = TIA → workup เหมือน stroke", topic="TIA",
            ref=[f"{D} หน้า 26, 41, 43–44"], nl=["B3.2.6(1)"]),
        mcq("NEURO-02-01-2",
            "A 60-year-old man presents with right hemiparesis, loss of sensation over the right face, and expressive aphasia. Which artery is most likely occluded?",
            "Left middle cerebral artery",
            ["Left anterior cerebral artery", "Left posterior cerebral artery", "Left lenticulostriate artery", "Right middle cerebral artery"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 47–48)",
            explain='''อ่อนแรง + ชาที่ **หน้าและแขน** ซีกขวา + **aphasia** (dominant hemisphere ซ้าย) = **MCA ซ้าย** (ในสไลด์ตัวเลือกเป็น ACA/MCA/PCA/lenticulostriate เฉลย MCA)
- ACA จะเด่นที่ **ขา > แขน** และไม่ค่อยมี aphasia
- PCA ทำให้ homonymous hemianopia ไม่ใช่ hemiparesis + aphasia
- Lenticulostriate (lacunar) ไม่มี cortical sign เช่น aphasia
- MCA ขวาทำให้อาการซีก **ซ้าย** และมักมี neglect แทน aphasia''',
            pearl="Hemiparesis หน้า-แขน + aphasia = MCA (dominant)", topic="MCA syndrome",
            ref=[f"{D} หน้า 27, 47–48"], nl=["B3.2.6(1)", "B3.1.1(10)"]),
        mcq("NEURO-02-01-3",
            "A 40-year-old woman develops neck pain, dizziness and veering to the left after a masseur forcefully twisted her neck. Examination shows a left Horner syndrome, left dysdiadochokinesia and a wide-based ataxic gait. What is the most likely diagnosis?",
            "Vertebral artery dissection",
            ["Cervical disc herniation", "Cerebellar hemorrhage", "Subarachnoid hemorrhage", "Cerebral venous thrombosis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 49–50)",
            explain='''ปวดคอหลัง **บิด/นวดคอ** + อาการ posterior circulation ด้านซ้าย (Horner, ataxia, dysdiadochokinesia — เข้ากับ Wallenberg/cerebellar ischemia) = **vertebral artery dissection** → อุด PICA/vertebral a.
- Cervical disc herniation ทำให้ปวดร้าวตาม dermatome/myelopathy ไม่ทำให้ Horner + cerebellar sign
- Cerebellar hemorrhage มักสัมพันธ์กับความดันสูง ปวดหัวรุนแรง อาเจียน ไม่ได้ตามหลังการบิดคอ
- SAH จะมีปวดหัวรุนแรงทันที คอแข็ง มากกว่า focal cerebellar sign
- Cerebral venous thrombosis เด่นที่ปวดหัว ↑ICP ชัก ในคนมี hypercoagulable state''',
            pearl="ปวดคอหลังนวด/บิดคอ + posterior circulation sign = vertebral a. dissection", topic="Arterial dissection",
            ref=[f"{D} หน้า 28, 37, 49–50"], nl=["B3.2.6(1)"]),
        mcq("NEURO-02-01-4",
            "A 60-year-old woman develops a sudden severe headache with nausea and vomiting, followed by weakness of the right arm and leg. BP 190/100 mmHg. Motor power on the right is grade 0/5. What is the most likely diagnosis?",
            "Left basal ganglia hemorrhage",
            ["Venous sinus thrombosis", "Subarachnoid hemorrhage", "Acute left MCA occlusion", "Left frontal lobe hemorrhage"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 53–54)",
            explain='''ปวดหัวรุนแรง + อาเจียน (↑ICP) + hemiplegia + ความดันสูงมาก = **hypertensive ICH** ซึ่งตำแหน่งที่พบบ่อยที่สุดคือ **putamen (basal ganglia)** (สไลด์เฉลย hypertensive ICH, common site putamen, thalamus, pons, cerebellum)
- Venous sinus thrombosis ไม่ทำให้ hemiplegia ทันทีพร้อมความดันสูง มักมีปัจจัยเสี่ยงลิ่มเลือด
- SAH ปวดหัวรุนแรงแต่มักไม่มี hemiplegia (มีคอแข็ง)
- MCA occlusion มักไม่ปวดหัวรุนแรงและอาเจียน
- Frontal lobe hemorrhage (lobar) ไม่ใช่ตำแหน่งที่พบบ่อยของ hypertensive ICH และมักอ่อนแรงแขนขาไม่เท่ากัน''',
            pearl="ปวดหัว+อาเจียน+hemiplegia+BP สูง = ICH ที่ putamen", topic="Hypertensive ICH",
            ref=[f"{D} หน้า 53–54"], nl=["B3.2.6(2)", "2.3.6(3)"]),
        mcq("NEURO-02-01-5",
            "A 68-year-old man suddenly develops vertigo, vomiting, hoarseness and difficulty swallowing. Examination shows a right Horner syndrome, right limb ataxia, loss of pain and temperature sensation on the right side of the face and on the left side of the body. Strength is normal. Which artery is most likely occluded?",
            "Right posterior inferior cerebellar artery",
            ["Left posterior inferior cerebellar artery", "Right middle cerebral artery", "Basilar artery", "Right posterior cerebral artery"],
            explain='''ครบชุด **lateral medullary (Wallenberg) syndrome** ด้านขวา: ipsilateral (ขวา) dysphagia เสียงแหบ Horner ataxia ชา pain/temp ที่หน้า · contralateral (ซ้าย) ชา pain/temp ที่ตัว → **PICA/vertebral a. ขวา**
- PICA ซ้ายจะทำให้ Horner และชาหน้าด้าน **ซ้าย**
- MCA ขวาทำให้อ่อนแรงซีกซ้ายและ neglect ไม่ทำให้ dysphagia + Horner
- Basilar มักทำให้ซึม quadriparesis และ CN palsy สองข้าง
- PCA ทำให้ hemianopia''',
            pearl="ชาหน้าข้างหนึ่ง + ชาตัวอีกข้าง + Horner + ataxia = Wallenberg (PICA)", topic="Wallenberg syndrome",
            ref=[f"{D} หน้า 28"], nl=["B3.2.6(1)", "B3.1.1(4)"]),
    ])

# ---------------------------------------------------------------- 02-02 Investigation & TOAST
S2 = sec("neuro-02-02", "Stroke investigation & etiology (TOAST)",
    "CBG ก่อน → CT non-contrast R/O hemorrhage · early ischemic sign · TOAST: large artery · cardioembolic · small vessel (lacunar) · other · undetermined", minutes=9,
    source=f"{D} หน้า 29–37, 57–60, 67–70, 77–78", nl=["B3.2.6(1)", "2.3.9-3(3)"],
    md='''
### Investigation เบื้องต้น

1. **CBG — R/O hypoglycemia!** (เลียนแบบ stroke ได้)
2. **CT brain non-contrast** (หรือ MRI) — เพื่อ **R/O hemorrhagic stroke (hyperdense lesion)** ก่อนตัดสินใจให้ยาละลายลิ่มเลือด
   - Ischemic stroke ระยะแรก CT **มักปกติ** · early sign: **hyperdense MCA**, loss of grey-white differentiation, basal ganglia obscuration, **loss of insular ribbon**, sulcal effacement → ต่อมาเป็น hypodense parenchyma
   - **MRI (DWI) เห็นได้เร็วกว่า** CT
3. ต่อด้วยหาสาเหตุ: EKG/Holter, echo, CTA/MRA, lipid, glucose, coagulogram (เสริม)

> ผู้ป่วยซึมที่แก้น้ำตาลแล้วยังไม่ดีขึ้น โดยเฉพาะคนกิน **anticoagulant** → **CT brain** (หาเลือดออก เช่น subdural/ICH)

### TOAST classification

| ชนิด | Risk/กลไก | อาการ | Imaging |
|---|---|---|---|
| **Large artery atherosclerosis** | HT DM DLP obesity smoking · artery-to-artery emboli, fixed stenosis (hypoperfusion) | รอยโรคใหญ่: cortical sign (aphasia, eye deviation) แขน≠ขา · cortex+subcortex: cortical sign + แขน=ขา · brainstem: ↓consciousness | CT lesion > 1.5–2 cm, **watershed infarct** · CTA/MRA: stenosis, plaque |
| **Cardioembolic** | **AF**, acute MI + LV thrombus, cardiomyopathy, **rheumatic mitral disease** | รอยโรคใหญ่ **deficit maximal at onset** | **Wedge-shaped cortical infarcts ในหลาย territory** · EKG/Holter AF · echo thrombus |
| **Small vessel (lacunar)** | **Long-standing HT** · lenticulostriate (basal ganglia, thalamus, pons, cerebellum) | **Lacunar syndrome** · รู้สึกตัวดี · **ไม่มี cortical sign** | CT ปกติ หรือ hypodense **< 1.5 cm** ใน deep subcortical |
| **Other determined** | Arterial dissection, vasculitis, hypercoagulable (APS) | ตามสาเหตุ | ตามสาเหตุ |
| **Undetermined** | หาสาเหตุไม่เจอ | | |

#### Lacunar syndromes (4 แบบ)
- **Pure motor hemiparesis** (internal capsule) — พบบ่อยสุด
- **Pure sensory stroke** (thalamus)
- **Ataxic hemiparesis**
- **Dysarthria–clumsy hand**

> Hypercoagulable state: coagulogram ผิดปกติ (เช่น **aPTT ยาว**) ในคนอายุน้อย → ตรวจ antithrombin III, protein C, protein S, **lupus anticoagulant, anticardiolipin** → รักษาด้วย anticoagulant
''',
    pearls=[
        "Stroke: เจาะ CBG ก่อนทุกครั้ง แล้ว CT non-contrast",
        "CT ระยะแรกของ ischemic stroke ปกติได้ · hyperdense MCA = early sign",
        "AF + wedge-shaped cortical infarct = cardioembolic",
        "Lacunar: HT นาน, ไม่มี cortical sign, lesion < 1.5 cm",
        "Pure motor hemiparesis = lacune ที่ internal capsule",
    ],
    items=[
        mcq("NEURO-02-02-1",
            "An 80-year-old man with atrial fibrillation on an anticoagulant and diabetes on oral agents has had 5 days of increasing drowsiness, poor intake and one episode of vomiting. Vital signs are stable, pulse 90/min regular. Motor power is grade 3 in all extremities. Electrolytes, calcium and magnesium are normal. Capillary glucose is 65 mg/dL, but after 50 mL of IV glucose he remains drowsy. What is the most appropriate next step?",
            "CT brain",
            ["EKG", "IV thiamine", "Lumbar puncture", "Observation"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 57–58)",
            explain='''คนสูงอายุที่ **กิน anticoagulant** ซึมลงหลายวัน + อาเจียน และ **แก้น้ำตาลแล้วยังซึม** → ต้องหา **intracranial hemorrhage (เช่น subdural/ICH)** ด้วย **CT brain** ก่อน
- EKG ช่วยเรื่อง arrhythmia แต่ชีพจรสม่ำเสมอและไม่อธิบายการซึม
- Thiamine เหมาะกับคนดื่มสุรา/ขาดอาหารที่มี Wernicke triad ซึ่งโจทย์ไม่ได้ชี้
- LP ห้ามทำก่อน CT ในคนซึม (เสี่ยง herniation) และกำลังได้ anticoagulant
- Observe ไม่เหมาะเพราะอาจมีเลือดออกในสมองที่ต้องแก้ทันที''',
            pearl="On anticoagulant + ซึมที่ไม่ใช่น้ำตาล → CT brain", topic="Stroke investigation",
            ref=[f"{D} หน้า 29, 57–58"], nl=["B3.2.6(2)", "2.2.36"]),
        mcq("NEURO-02-02-2",
            "A patient with a previous self-limited ischemic stroke now presents with acute hemiparesis. BP is 150/95 mmHg and capillary glucose is 110 mg/dL. What is the most appropriate next step?",
            "Non-contrast CT brain",
            ["Streptokinase infusion", "Intravenous antihypertensive drug", "Aspirin 325 mg", "Carotid duplex ultrasound"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 59–60)",
            explain='''Acute focal deficit หลังตรวจน้ำตาลแล้ว ต้อง **CT non-contrast** เพื่อแยก hemorrhage ก่อนให้ยาใด ๆ ที่มีผลต่อการแข็งตัวของเลือด
- Streptokinase ไม่ใช้ใน acute ischemic stroke (เพิ่มเลือดออก) — ยาที่ใช้คือ alteplase และต้องมี CT ก่อน
- BP 150/95 ต่ำกว่าเกณฑ์ทั้งกรณีให้ rt-PA (185/110) และไม่ให้ (220/120) จึงยังไม่ต้องลดความดัน
- Aspirin ต้องรอ R/O hemorrhage ก่อน
- Carotid duplex เป็น workup หาสาเหตุภายหลัง ไม่ใช่ขั้นแรก''',
            pearl="Stroke: CBG → CT non-contrast ก่อนยาใด ๆ", topic="Initial imaging",
            ref=[f"{D} หน้า 29, 59–60"], nl=["B3.2.6(1)"]),
        mcq("NEURO-02-02-3",
            "A 60-year-old man develops sudden weakness of the right arm and leg. BP 180/90 mmHg, pulse 95/min irregular. He follows commands, pupils are 3 mm and reactive, and he has right hemiplegia. EKG shows atrial fibrillation. What is the most likely diagnosis?",
            "Cerebral embolism",
            ["Central transtentorial herniation", "Ruptured cerebral aneurysm", "Brainstem hemorrhage", "Basilar artery thrombosis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 67–68)",
            explain='''Hemiplegia เฉียบพลัน + **AF** + รู้สึกตัวดี รูม่านตาปกติ = **cardioembolic stroke (cerebral embolism)**
- Central herniation ทำให้ซึมลงมาก รูม่านตาเล็ก/ผิดปกติ และหายใจผิดปกติ
- Ruptured aneurysm (SAH) จะปวดหัวรุนแรงทันที คอแข็ง มักไม่มี hemiplegia
- Brainstem (pontine) hemorrhage มักโคม่า pinpoint pupils quadriplegia
- Basilar thrombosis ทำให้ซึม CN palsy สองข้าง quadriparesis ไม่ใช่ hemiplegia ล้วนที่รู้สึกตัวดี''',
            pearl="AF + hemiplegia ทันที = cardioembolic", topic="Cardioembolic stroke",
            ref=[f"{D} หน้า 35, 67–68"], nl=["B3.2.6(1)"]),
        mcq("NEURO-02-02-4",
            "A 60-year-old man with 10 years of untreated hypertension has sudden difficulty speaking: speech is non-fluent, but comprehension is preserved. EKG shows a totally irregular rhythm. CT shows a wedge-shaped infarct in the left inferior frontal lobe. What is the most likely etiology?",
            "Cardiac embolism",
            ["Lipohyalinosis", "Atherosclerotic plaque embolism", "Large-vessel hypoperfusion (watershed) infarction", "Small vessel disease"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 69–70)",
            explain='''**AF (totally irregular)** + **wedge-shaped cortical infarct** (inferior frontal = Broca area → non-fluent aphasia) = **cardioembolic** ตาม TOAST
- Lipohyalinosis และ small vessel disease เป็นกลไก lacunar stroke จาก HT นาน แต่จะ **ไม่มี cortical sign** อย่าง aphasia และ lesion < 1.5 cm ใน deep structure — ประวัติ HT ในโจทย์เป็นตัวหลอก
- Atherosclerotic plaque emboli (artery-to-artery) เป็นไปได้ แต่ไม่มีหลักฐาน stenosis และมี AF ชัดกว่า
- Watershed infarct เกิดจาก fixed stenosis + hypoperfusion อยู่ตรงรอยต่อ territory ไม่ใช่ wedge cortical''',
            pearl="Wedge-shaped cortical infarct + AF = cardiac emboli แม้มี HT", topic="TOAST",
            ref=[f"{D} หน้า 34–36, 69–70"], nl=["B3.2.6(1)"]),
        mcq("NEURO-02-02-5",
            "A 70-year-old woman with diabetes and hypertension for 10 years wakes up with weakness of the right arm and leg. She has no numbness, speaks and understands normally, and is fully alert. BP is mildly elevated, CBC is normal and FBS is 200 mg/dL. What is the most likely diagnosis?",
            "Lacunar infarction",
            ["Left frontal lobe infarction", "Pontine hemorrhage", "Cerebellar hemorrhage", "Left parietal lobe hemorrhage"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 77–78)",
            explain='''HT + DM นาน + **pure motor hemiparesis** (ไม่ชา) รู้สึกตัวดี **ไม่มี cortical sign** = **lacunar infarction (small vessel occlusion)** (สไลด์เฉลย SVO, lacunar syndrome pure motor hemiparesis)
- Frontal lobe infarction เป็น cortical จะมี aphasia/eye deviation และแขนขาไม่เท่ากัน
- Pontine hemorrhage มักโคม่า pinpoint pupils quadriplegia
- Cerebellar hemorrhage ทำให้เวียนหัว อาเจียน ataxia ไม่ใช่ hemiparesis
- Parietal hemorrhage จะมีอาการชา/cortical sensory loss และปวดหัว''',
            pearl="Pure motor hemiparesis + no cortical sign + HT = lacunar", topic="Lacunar stroke",
            ref=[f"{D} หน้า 36, 77–78"], nl=["B3.2.6(1)"]),
    ])

# ---------------------------------------------------------------- 02-03 Acute management
F_ACUTE = fig("neuro-02-03-f1", "Acute ischemic stroke: ลำดับการดูแลและเกณฑ์ BP", '''<svg viewBox="0 0 740 470">
 <defs><marker id="neuro-02-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="20" y="14" width="150" height="54" rx="10" class="acsoft"/>
 <text x="95" y="38" text-anchor="middle" class="tb">ABC</text>
 <text x="95" y="56" text-anchor="middle" class="t3">ETT ถ้า GCS ≤ 8</text>
 <path d="M170 41H198" class="ln" marker-end="url(#neuro-02-03-a)"/>
 <rect x="200" y="14" width="150" height="54" rx="10" class="acsoft"/>
 <text x="275" y="38" text-anchor="middle" class="tb">CBG</text>
 <text x="275" y="56" text-anchor="middle" class="t3">R/O hypoglycemia</text>
 <path d="M350 41H378" class="ln" marker-end="url(#neuro-02-03-a)"/>
 <rect x="380" y="14" width="150" height="54" rx="10" class="acsoft"/>
 <text x="455" y="38" text-anchor="middle" class="tb">CT non-contrast</text>
 <text x="455" y="56" text-anchor="middle" class="t3">R/O hemorrhage</text>
 <path d="M530 41H558" class="ln" marker-end="url(#neuro-02-03-a)"/>
 <rect x="560" y="14" width="160" height="54" rx="10" class="c1"/>
 <text x="640" y="38" text-anchor="middle" class="tw">เวลา last seen well</text>
 <text x="640" y="56" text-anchor="middle" class="tw">+ contraindication?</text>
 <text x="370" y="104" text-anchor="middle" class="tb">นับเวลาจาก last seen well (ชั่วโมง)</text>
 <path d="M60 170H700" class="ln" marker-end="url(#neuro-02-03-a)"/>
 <path d="M60 162V178M160 162V178M330 162V178M440 162V178M680 162V178" class="ln"/>
 <text x="60" y="196" text-anchor="middle" class="t3">0</text>
 <text x="160" y="196" text-anchor="middle" class="t3">1.5</text>
 <text x="330" y="196" text-anchor="middle" class="t3">4.5</text>
 <text x="440" y="196" text-anchor="middle" class="t3">6</text>
 <text x="680" y="196" text-anchor="middle" class="t3">24</text>
 <rect x="60" y="120" width="270" height="34" rx="6" class="ok"/>
 <text x="195" y="142" text-anchor="middle" class="tw">IV rt-PA (alteplase) &lt; 4.5 hr</text>
 <rect x="60" y="206" width="380" height="30" rx="6" class="c2soft"/>
 <text x="250" y="226" text-anchor="middle" class="t2">Mechanical thrombectomy (LVO) &lt; 6 hr (เสริม)</text>
 <rect x="440" y="206" width="240" height="30" rx="6" class="sunk"/>
 <text x="560" y="226" text-anchor="middle" class="t3">6–24 hr ถ้า imaging เข้าเกณฑ์ (เสริม)</text>
 <rect x="20" y="256" width="340" height="104" rx="10" class="oksoft"/>
 <text x="190" y="280" text-anchor="middle" class="tb">ให้ rt-PA</text>
 <text x="34" y="304" class="t2">ก่อนให้: BP <tspan class="tb">&lt; 185/110</tspan></text>
 <text x="34" y="326" class="t2">หลังให้ (24 ชม.): BP <tspan class="tb">&lt; 180/105</tspan></text>
 <text x="34" y="348" class="t3">Alteplase 0.9 mg/kg (max 90) · 10% bolus ที่เหลือ 1 ชม.</text>
 <rect x="380" y="256" width="340" height="104" rx="10" class="misssoft"/>
 <text x="550" y="280" text-anchor="middle" class="tb">ไม่ให้ rt-PA</text>
 <text x="394" y="304" class="t2">ยอมให้ BP สูงได้ถึง <tspan class="tb">&lt; 220/120</tspan></text>
 <text x="394" y="326" class="t2">(permissive HT เพื่อ penumbra)</text>
 <text x="394" y="348" class="t3">ASA ภายใน 24–48 ชม. (เสริม)</text>
 <rect x="20" y="376" width="700" height="80" rx="10" class="box"/>
 <text x="370" y="398" text-anchor="middle" class="tb">ลดความดันด้วย IV labetalol หรือ IV nicardipine · supportive ทุกราย</text>
 <text x="36" y="424" class="t2">DTX 140–180 · normothermia · dysphagia assessment ก่อนป้อนอาหาร</text>
 <text x="36" y="446" class="t2">early rehabilitation · F/U V/S และ neuro sign</text>
</svg>''', "บน: ลำดับในห้องฉุกเฉิน · กลาง: เส้นเวลานับจาก last seen well (แถบเขียว rt-PA ตามสไลด์ แถบม่วงเป็นส่วนเสริม) · ล่าง: เกณฑ์ BP แยกตามว่าให้ rt-PA หรือไม่")

S3 = sec("neuro-02-03", "Acute ischemic stroke management (rt-PA, BP)",
    "ABC → CBG → CT · rt-PA <4.5 hr จาก last seen well: alteplase 0.9 mg/kg (10% bolus) · BP <185/110 ก่อน, <180/105 หลัง · ไม่ให้ rt-PA ยอม <220/120", minutes=9,
    source=f"{D} หน้า 38–39, 55–56, 61–66", nl=["B3.2.6(1)", "2.2.39", "B2.4(3)"],
    md='''
### Initial

- **ABC** — ใส่ท่อช่วยหายใจถ้า **GCS ≤ 8**, หายใจไม่พอ หรือ bulbar dysfunction (ไม่ป้องกัน airway ได้)
- **CBG** และ **CT non-contrast** (ดูหัวข้อก่อน)

[[fig:neuro-02-03-f1]]

### BP management

| สถานการณ์ | เป้าหมาย BP |
|---|---|
| จะให้ rt-PA — **ก่อนให้** | **< 185/110 mmHg** |
| ให้ rt-PA แล้ว — **หลังให้** | **< 180/105 mmHg** |
| ไม่ให้ rt-PA | ลดเมื่อ **≥ 220/120 mmHg** (permissive hypertension) |

- ยา: **IV labetalol, IV nicardipine**
- ถ้า BP สูงเกินเกณฑ์แต่อยู่ในเวลาให้ rt-PA → **ลดความดันก่อน แล้วค่อยให้ rt-PA**

### Specific treatment: rt-PA

- **< 4.5 ชั่วโมง** นับจาก **last seen well** (ไม่ใช่เวลาที่พบอาการ — ตื่นนอนมาอ่อนแรง ให้นับจากเวลาเข้านอน) **และไม่มี contraindication**
- **Alteplase IV 0.9 mg/kg** (max 90 mg — เสริม) **ให้ใน 1 ชม. โดย 10% IV bolus ใน 1 นาที**
- Contraindication สำคัญ (เสริม): เคยมี ICH, stroke/head injury รุนแรงใน 3 เดือน, BP คุมไม่ได้ > 185/110, platelet < 100,000, INR > 1.7 หรือได้ DOAC ใน 48 ชม., glucose < 50, ผ่าตัดใหญ่ใน 14 วัน, GI bleed ใน 21 วัน, CT เห็น hypodensity กว้าง
- **ไม่ใช้ heparin/warfarin/streptokinase ในระยะเฉียบพลัน** แม้เป็น AF (เพิ่ม hemorrhagic transformation)
- ปัจจุบัน (เสริม): **tenecteplase 0.25 mg/kg bolus** ใช้แทนได้ · **mechanical thrombectomy** ใน large vessel occlusion ภายใน 6 ชม. (ถึง 24 ชม. ในรายที่เลือกด้วย imaging) — ข้อสอบตามสไลด์ยังยึด alteplase < 4.5 ชม.

### Supportive (neuroprotective measures)

- **Euglycemia: DTX 140–180 mg/dL**
- **Normothermia**
- **Dysphagia assessment** ก่อนให้กินทางปาก (ลด aspiration pneumonia)
- **Early rehabilitation**
- F/U V/S, neuro sign (ระวัง hemorrhagic transformation, brain edema)
''',
    figs=[F_ACUTE],
    pearls=[
        "rt-PA: < 4.5 ชม. จาก last seen well + ไม่มี contraindication",
        "Alteplase 0.9 mg/kg ใน 1 ชม. แบ่ง 10% bolus ใน 1 นาที",
        "BP ก่อน rt-PA < 185/110 · หลัง < 180/105 · ไม่ให้ rt-PA ยอมถึง 220/120",
        "BP เกินเกณฑ์แต่อยู่ในเวลา → IV nicardipine/labetalol ก่อน แล้วให้ rt-PA",
        "AF + acute stroke: ไม่ให้ heparin/warfarin ระยะแรก",
    ],
    items=[
        mcq("NEURO-02-03-1",
            "A 60-year-old man with type 2 diabetes who smokes presents with right hemiparesis that began 2 hours ago. Medications: metformin, simvastatin, enalapril. BP 200/100 mmHg. CT brain shows no hemorrhage (a small hypodensity in the left internal capsule is noted). FBS 120 mg/dL, LDL 110 mg/dL, creatinine 0.8 mg/dL. What is the most appropriate initial management?",
            "IV nicardipine",
            ["rt-PA immediately", "Warfarin", "Add glipizide", "Change simvastatin to atorvastatin"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 61–62)",
            explain='''อยู่ในเวลา (2 ชม.) และ CT ไม่มีเลือดออก จึงเป็นผู้ที่ควรได้ rt-PA แต่ **BP 200/100 เกินเกณฑ์ก่อนให้ rt-PA (< 185/110)** → ต้อง **ลดความดันด้วย IV nicardipine (หรือ labetalol) ก่อน** แล้วจึงให้ rt-PA (สไลด์เฉลยพร้อมเกณฑ์ BP ของ rt-PA)
- ให้ rt-PA ทันทีขณะ BP > 185/110 เพิ่มความเสี่ยง ICH
- Warfarin ไม่ใช้ในระยะเฉียบพลัน และไม่มีข้อบ่งชี้ (ไม่มี AF)
- Glipizide: น้ำตาล 120 อยู่ในเป้าแล้ว
- เปลี่ยน statin เป็น secondary prevention ระยะยาว ไม่ใช่ initial management''',
            pearl="อยู่ใน window แต่ BP > 185/110 → nicardipine ก่อน rt-PA", topic="BP before rt-PA",
            ref=[f"{D} หน้า 38, 61–62"], nl=["B3.2.6(1)"]),
        mcq("NEURO-02-03-2",
            "A 60-year-old man with diabetes and hypertension presents with right hemiparesis and mutism that started 3 hours ago. Pulse 90/min totally irregular, BP 155/90 mmHg. Examination: global aphasia, right UMN facial palsy, right motor power 2/5. Capillary glucose 95 mg/dL. Non-contrast CT brain is normal. What is the most appropriate management?",
            "IV rt-PA",
            ["Oral aspirin", "Oral warfarin", "IV glucose", "IV heparin"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 63–64)",
            explain='''Acute ischemic stroke (MCA ซ้าย) **3 ชม. < 4.5 ชม.** CT ไม่มีเลือดออก BP 155/90 < 185/110 น้ำตาลปกติ → **IV rt-PA** (สไลด์: rt-PA กรณี last well seen < 4.5 hr และไม่มี contraindication)
- Aspirin ให้เมื่อไม่ได้ rt-PA หรือหลัง rt-PA 24 ชม. — ไม่ใช่ตัวเลือกแรกในคนที่ให้ rt-PA ได้
- Warfarin และ heparin ไม่ให้ในระยะเฉียบพลันแม้มี AF (เสี่ยง hemorrhagic transformation) — AF เป็นตัวหลอก
- IV glucose ไม่จำเป็นเพราะ CBG 95 ปกติ''',
            pearl="< 4.5 ชม. + CT ไม่มีเลือด + BP < 185/110 → rt-PA", topic="rt-PA indication",
            ref=[f"{D} หน้า 39, 63–64"], nl=["B3.2.6(1)", "B2.4(3)"]),
        mcq("NEURO-02-03-3",
            "A 60-year-old man has had right arm and leg weakness for 1 hour. BP 170/100 mmHg, pulse 100/min irregular. Examination: left gaze deviation, right hemiparesis, aphasia, unable to follow simple commands. Non-contrast CT shows no intracerebral hemorrhage. Laboratory tests are normal. What is the most appropriate management?",
            "Alteplase",
            ["Aspirin", "Aspirin plus clopidogrel", "Nicardipine", "Enoxaparin"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 65–66)",
            explain='''Large MCA stroke ซ้าย (eye deviation ไปด้าน lesion, aphasia) **1 ชม.** CT ไม่มีเลือดออก และ **BP 170/100 < 185/110** → **alteplase** ได้เลย
- Aspirin ไม่ใช่ทางเลือกแรกเมื่อเข้าเกณฑ์ rt-PA
- DAPT (aspirin + clopidogrel) ใช้ใน minor stroke (NIHSS ≤ 3) หรือ high-risk TIA ซึ่งรายนี้รุนแรง
- Nicardipine ไม่จำเป็นเพราะ BP ต่ำกว่าเกณฑ์ 185/110 แล้ว
- Enoxaparin (anticoagulant) ห้ามในระยะเฉียบพลัน''',
            pearl="BP 170/100 ไม่ต้องลดก่อน rt-PA (เกณฑ์ 185/110)", topic="Alteplase",
            ref=[f"{D} หน้า 38–39, 65–66"], nl=["B3.2.6(1)"]),
        mcq("NEURO-02-03-4",
            "A 40-year-old woman with rheumatic heart disease suddenly loses consciousness 1 hour ago. BP 200/110 mmHg. Examination: cardiomegaly with right ventricular heave, grade 3/6 diastolic rumbling murmur at the apex, GCS E4V1M1, bilateral lateral gaze limitation and quadriparesis. She has pooled secretions in the mouth. What is the most appropriate management before referral to the stroke center?",
            "Endotracheal intubation",
            ["Aspirin 325 mg", "Intravenous nicardipine", "Unfractionated heparin", "Low-molecular-weight heparin"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 55–56)",
            explain='''Mitral stenosis → emboli อุด **basilar/pons** (CN6 สองข้าง + quadriparesis) · **GCS = 6 (≤ 8)** + bulbar dysfunction → ต้อง **protect airway ด้วย ETT ก่อนส่งต่อ** (ABC มาก่อนทุกอย่าง)
- Aspirin ยังไม่ให้ก่อน CT และผู้ป่วยอาจเข้าเกณฑ์ rt-PA/thrombectomy
- Nicardipine ใช้ลด BP ให้ < 185/110 ถ้าจะให้ rt-PA — ทำได้ แต่สำคัญรองจาก airway
- Heparin ทั้ง UFH และ LMWH ไม่ให้ในระยะเฉียบพลันแม้เป็น cardioembolic
(เฉลยในสไลด์เป็นภาพ — คำตอบนี้ยึดหลัก ABC; โจทย์เติม "เสมหะคั่งในปาก" เพื่อให้ชัดขึ้น)''',
            pearl="Posterior circulation stroke + GCS ≤ 8 → intubate ก่อนส่งต่อ", topic="Airway in stroke",
            ref=[f"{D} หน้า 38, 55–56"], nl=["2.2.39", "2.2.36"]),
        mcq_ordered("NEURO-02-03-5",
            "A 65-kg man with acute ischemic stroke 2 hours from onset is eligible for intravenous alteplase. Using the standard dose, how much alteplase should be given as the initial IV bolus over 1 minute?",
            ["2.9 mg", "5.9 mg", "8.8 mg", "29 mg", "58.5 mg"], 1,
            explain='''Alteplase **0.9 mg/kg** → 0.9 × 65 = **58.5 mg** · **10% เป็น bolus ใน 1 นาที = 5.85 ≈ 5.9 mg** ที่เหลือ 52.6 mg หยดใน 1 ชม.
- 2.9 mg คิด bolus เป็น 5%
- 8.8 mg คิด bolus เป็น 15% ของขนาดรวม
- 29 mg คือครึ่งหนึ่งของขนาดรวม
- 58.5 mg คือขนาดรวมทั้งหมด ไม่ใช่ bolus''',
            pearl="Alteplase 0.9 mg/kg: 10% bolus 1 นาที + 90% drip 1 ชม.", topic="Alteplase dose",
            ref=[f"{D} หน้า 39"], nl=["B2.4(3)"]),
    ])

# ---------------------------------------------------------------- 02-04 Secondary prevention
F_SEC = fig("neuro-02-04-f1", "Secondary prevention แยกตามสาเหตุ (TOAST)", '''<svg viewBox="0 0 740 380">
 <defs><marker id="neuro-02-04-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="10" width="280" height="40" rx="10" class="acsoft"/>
 <text x="370" y="35" text-anchor="middle" class="tb">Ischemic stroke / TIA → หาสาเหตุ</text>
 <path d="M370 50V70M95 70H645" class="ln"/>
 <path d="M95 70V90" class="ln" marker-end="url(#neuro-02-04-a)"/>
 <path d="M280 70V90" class="ln" marker-end="url(#neuro-02-04-a)"/>
 <path d="M465 70V90" class="ln" marker-end="url(#neuro-02-04-a)"/>
 <path d="M645 70V90" class="ln" marker-end="url(#neuro-02-04-a)"/>
 <rect x="10" y="92" width="170" height="160" rx="10" class="c1soft"/>
 <text x="95" y="114" text-anchor="middle" class="tb">Large artery</text>
 <text x="22" y="138" class="t2">ASA + atorvastatin</text>
 <text x="22" y="158" class="t2">คุม HT DM DLP</text>
 <text x="22" y="178" class="t2">ลดน้ำหนัก งดบุหรี่</text>
 <text x="22" y="204" class="tb">Extracranial ICA</text>
 <text x="22" y="222" class="t2">stenosis &gt; 70%</text>
 <text x="22" y="240" class="t2">→ CEA / stent</text>
 <rect x="195" y="92" width="170" height="160" rx="10" class="c2soft"/>
 <text x="280" y="114" text-anchor="middle" class="tb">Cardioembolic</text>
 <text x="207" y="138" class="t2">AF, LV thrombus,</text>
 <text x="207" y="158" class="t2">rheumatic MS</text>
 <text x="207" y="190" class="tb">Anticoagulant</text>
 <text x="207" y="210" class="t2">warfarin / DOAC</text>
 <text x="207" y="236" class="t3">(MS/ลิ้นเทียม → warfarin)</text>
 <rect x="380" y="92" width="170" height="160" rx="10" class="oksoft"/>
 <text x="465" y="114" text-anchor="middle" class="tb">Small vessel</text>
 <text x="392" y="138" class="t2">ASA</text>
 <text x="392" y="164" class="tb">BP &lt; 130/80</text>
 <text x="392" y="190" class="t2">คุม DM DLP</text>
 <text x="392" y="210" class="t2">งดบุหรี่</text>
 <rect x="565" y="92" width="165" height="160" rx="10" class="misssoft"/>
 <text x="647" y="114" text-anchor="middle" class="tb">Other / undetermined</text>
 <text x="577" y="138" class="t2">Dissection: ASA</text>
 <text x="577" y="156" class="t2">หรือ anticoagulant</text>
 <text x="577" y="180" class="t2">APS: anticoagulant</text>
 <text x="577" y="204" class="t2">Vasculitis: steroid</text>
 <text x="577" y="228" class="t2">Undetermined: ASA</text>
 <rect x="10" y="270" width="720" height="98" rx="10" class="box"/>
 <text x="370" y="294" text-anchor="middle" class="tb">Non-cardioembolic + minor stroke (NIHSS ≤ 3) หรือ high-risk TIA (ABCD2 ≥ 4)</text>
 <rect x="120" y="310" width="230" height="40" rx="8" class="c1"/>
 <text x="235" y="335" text-anchor="middle" class="tw">DAPT ASA + clopidogrel 21 วัน</text>
 <path d="M350 330H398" class="ln" marker-end="url(#neuro-02-04-a)"/>
 <rect x="400" y="310" width="220" height="40" rx="8" class="ok"/>
 <text x="510" y="335" text-anchor="middle" class="tw">ASA ตลอดชีวิต</text>
</svg>''', "เลือกยาตามกลไก: ลิ่มเลือดจากหัวใจใช้ anticoagulant ส่วนจากหลอดเลือดแดงใช้ antiplatelet + คุมปัจจัยเสี่ยง และ minor stroke/high-risk TIA ใช้ DAPT ช่วงสั้น")

S4 = sec("neuro-02-04", "Secondary prevention ของ ischemic stroke/TIA",
    "Non-cardioembolic: ASA ± statin · DAPT 21 วันใน minor stroke/high-risk TIA · cardioembolic: anticoagulant · ICA >70%: CEA · lacunar: BP <130/80", minutes=8,
    source=f"{D} หน้า 40–42, 45–46, 71–82", nl=["B3.2.6(1)", "B2.4(3)"],
    md='''
### ตามสาเหตุ (สไลด์)

[[fig:neuro-02-04-f1]]

| สาเหตุ | Secondary prevention |
|---|---|
| **Large artery — intracranial stenosis** | **ASA + atorvastatin** + คุม HT DM DLP, ลดน้ำหนัก, งดบุหรี่ |
| **Large artery — extracranial ICA stenosis** | **Carotid endarterectomy/angioplasty** เมื่อ **stenosis > 70%** (symptomatic) และความเสี่ยงผ่าตัดต่ำ + ยาเหมือนข้างบน |
| **Small vessel occlusion** | **ASA** + คุม HT DM DLP + **BP < 130/80 mmHg** |
| **Cardioembolic** (AF, STEMI → LV thrombus, rheumatic MS) | **Anticoagulant: warfarin/DOAC** (ไม่ใช่ antiplatelet) |
| **Arterial dissection** | ASA หรือ anticoagulant |
| **Antiphospholipid syndrome** | Anticoagulant (warfarin) |
| **Vasculitis** | Steroid, immunosuppressant |
| **Undetermined** | ASA + คุมปัจจัยเสี่ยง |

### DAPT

- **Non-cardioembolic** stroke ที่เป็น **minor stroke (NIHSS ≤ 3)** หรือ **high-risk TIA (ABCD2 ≥ 4)**
- **ASA + clopidogrel 21 วันแรก** แล้วต่อด้วย **ASA ตลอดชีวิต**
- ใช้นานกว่านี้เพิ่ม bleeding โดยไม่ลด stroke เพิ่ม (เสริม)

### TIA

- Acute, transient focal neurological symptoms (**< 1 ชม.**)
- ดูแล **เหมือน acute ischemic stroke** (หาสาเหตุ + secondary prevention) **แต่ไม่ต้อง thrombolysis**
- TIA + AF = cardioembolic → **anticoagulant** แม้อาการหายแล้ว

> กับดัก: AF/STEMI แล้วเกิด stroke → ตอบ **warfarin/DOAC** ไม่ใช่ aspirin หรือ enoxaparin · lacunar stroke ซ้ำทั้งที่คุมโรคอยู่ → คุม **BP < 130/80** ให้ถึงเป้า (เช่น เพิ่ม ACEI) ไม่ใช่เพิ่มขนาด aspirin
''',
    figs=[F_SEC],
    pearls=[
        "Cardioembolic (AF, LV thrombus หลัง STEMI) → warfarin/DOAC",
        "Symptomatic extracranial ICA stenosis > 70% → carotid endarterectomy",
        "Minor stroke NIHSS ≤ 3 / TIA ABCD2 ≥ 4 → DAPT 21 วัน แล้ว ASA",
        "Lacunar → ASA + BP < 130/80",
        "aPTT ยาวในคนอายุน้อยที่มี stroke → lupus anticoagulant/anticardiolipin",
    ],
    items=[
        mcq("NEURO-02-04-1",
            "A previously healthy 70-year-old Thai woman had weakness of the left arm lasting 5 minutes that resolved completely. EKG shows atrial fibrillation. Non-contrast CT brain is normal. Which drug should be used to prevent recurrence?",
            "Warfarin or a direct oral anticoagulant",
            ["Aspirin", "Aspirin plus clopidogrel for 21 days", "Clopidogrel", "Dipyridamole"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 45–46, 71–72)",
            explain='''TIA ที่มี **AF** = กลไก **cardioembolic** → secondary prevention คือ **anticoagulant (warfarin/NOAC)** (สไลด์เฉลย Cardioembolic: anticoagulant) — แม้อาการหายแล้วก็ต้องให้
- Aspirin และ clopidogrel ป้องกัน cardioembolic stroke จาก AF ได้น้อยกว่า anticoagulant มาก
- DAPT 21 วันใช้กับ minor stroke/high-risk TIA ที่ **ไม่ใช่** cardioembolic
- Dipyridamole เป็น antiplatelet ไม่ใช่ทางเลือกสำหรับ AF''',
            pearl="TIA/stroke + AF → anticoagulant", topic="Cardioembolic prevention",
            ref=[f"{D} หน้า 42, 45–46, 71–72"], nl=["B3.2.6(1)", "B2.4(3)"]),
        mcq("NEURO-02-04-2",
            "A 70-year-old woman develops left arm and leg weakness. EKG shows ST-segment elevation in the anterior leads and echocardiography shows an apical left ventricular thrombus. After the acute phase, which drug should be given to prevent recurrent stroke?",
            "Warfarin",
            ["Aspirin", "Enoxaparin", "Clopidogrel", "Dipyridamole"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 73–74)",
            explain='''**STEMI → LV thrombus (หรือ AF)** → embolic stroke = **cardioembolic** → **anticoagulant (warfarin/DOAC)** ตามสไลด์
- Aspirin และ clopidogrel ให้ต่อสำหรับ MI ได้ แต่ป้องกัน emboli จาก LV thrombus ไม่พอ
- Enoxaparin ใช้ bridging ระยะสั้น ไม่ใช่ยาป้องกันระยะยาว
- Dipyridamole เป็น antiplatelet ไม่ใช่ข้อบ่งชี้นี้''',
            pearl="STEMI + stroke = LV thrombus → warfarin", topic="LV thrombus",
            ref=[f"{D} หน้า 35, 73–74"], nl=["B3.2.6(1)", "B2.4(3)"]),
        mcq("NEURO-02-04-3",
            "A 65-year-old woman had sudden right arm weakness and slurred speech 1 week ago that lasted 30 minutes and resolved. Pulse is 80/min regular, BP 140/90 mmHg, and there is a left carotid bruit. She has no deficit. CT brain is normal; CT angiography shows 80% stenosis of the left extracranial internal carotid artery. Which is the most appropriate management to prevent recurrence?",
            "Carotid endarterectomy",
            ["Aspirin alone", "Clopidogrel alone", "Warfarin", "Rivaroxaban"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 75–76)",
            explain='''Symptomatic (TIA ตรงด้าน) **extracranial ICA stenosis 80% (> 70%)** → **carotid endarterectomy** (หรือ stenting) ร่วมกับ antiplatelet และ statin
- Aspirin/clopidogrel อย่างเดียวไม่พอสำหรับ stenosis รุนแรงที่มีอาการ — ต้องให้ร่วมกับการผ่าตัด
- Warfarin และ rivaroxaban ใช้ใน cardioembolic (ชีพจรสม่ำเสมอ ไม่มี AF)''',
            pearl="Symptomatic ICA stenosis > 70% → CEA", topic="Carotid stenosis",
            ref=[f"{D} หน้า 40, 75–76"], nl=["B3.2.6(1)"]),
        mcq("NEURO-02-04-4",
            "A 48-year-old man with diabetes, hypertension and dyslipidemia had a right lacunar infarct 4 months ago with full recovery. He takes aspirin, metformin, atorvastatin and amlodipine; his HbA1c and LDL are at goal and he does not smoke. He now presents with a recurrent pure motor left hemiparesis. BP is 160/90 mmHg; carotid imaging is normal. What should be done to prevent another recurrence?",
            "Add enalapril",
            ["Double the dose of aspirin", "Add eicosapentaenoic acid (EPA)", "Smoking cessation program", "Carotid angioplasty and stenting"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 79–80)",
            explain='''Lacunar stroke ซ้ำ (small vessel occlusion) โดย **BP 160/90 ยังไม่ถึงเป้า < 130/80** → เพิ่มยาลดความดัน เช่น **enalapril** (สไลด์เฉลย SVO: control BP < 130/80)
- เพิ่มขนาด aspirin ไม่ลด recurrence แต่เพิ่ม bleeding
- EPA ไม่ใช่การป้องกันหลักใน stroke
- ผู้ป่วยไม่สูบบุหรี่
- Carotid stenting ไม่มีข้อบ่งชี้เพราะ lacunar และ carotid ปกติ''',
            pearl="Lacunar ซ้ำ → คุม BP < 130/80 ให้ถึงเป้า", topic="BP target after lacunar stroke",
            ref=[f"{D} หน้า 40, 79–80"], nl=["B3.2.6(1)"]),
        mcq("NEURO-02-04-5",
            "A 49-year-old woman with no vascular risk factors presents with left hemiparesis from an ischemic stroke. Coagulation tests: PT 12 seconds (normal), aPTT 45 seconds (prolonged), not corrected by mixing study. What is the most appropriate investigation?",
            "Anticardiolipin antibody",
            ["Antinuclear antibody", "Anti-dsDNA", "ANCA", "Factor VIII level"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 81–82)",
            explain='''Stroke ในคนอายุน้อยไม่มี risk + **aPTT ยาวที่ mixing ไม่แก้** = มี inhibitor แบบ **lupus anticoagulant** → **antiphospholipid syndrome** → ตรวจ **anticardiolipin** (ร่วมกับ lupus anticoagulant, anti-β2GPI) และรักษาด้วย anticoagulant (สไลด์: hypercoagulable states, Ix anticardiolipin)
- ANA และ anti-dsDNA ใช้วินิจฉัย SLE ไม่ได้อธิบาย aPTT ยาวโดยตรง
- ANCA ใช้กับ small vessel vasculitis
- Factor VIII level ใช้เมื่อสงสัย hemophilia ซึ่งจะเลือดออก ไม่ใช่ลิ่มเลือดอุดตัน และ mixing study จะแก้ได้ (mixing study เป็นส่วนเสริม)''',
            pearl="Stroke + aPTT ยาว = APS → anticardiolipin → warfarin", topic="Hypercoagulable stroke",
            ref=[f"{D} หน้า 37, 42, 81–82"], nl=["B3.2.6(1)"]),
        mcq("NEURO-02-04-6",
            "A 63-year-old man has a transient episode of right hand weakness and dysarthria lasting 20 minutes. He is 63 years old, BP 150/90 mmHg, and has diabetes (ABCD2 score 5). Pulse is regular, EKG shows sinus rhythm, CT brain and carotid duplex are unremarkable. What is the most appropriate antithrombotic regimen?",
            "Aspirin plus clopidogrel for 21 days, then aspirin alone",
            ["Aspirin alone", "Aspirin plus clopidogrel for 12 months", "Warfarin with target INR 2–3", "Intravenous alteplase"],
            explain='''**High-risk TIA (ABCD2 ≥ 4)** ที่ไม่ใช่ cardioembolic → **DAPT (ASA + clopidogrel) 21 วันแรก** แล้วต่อ **ASA ตลอดชีวิต** ตามสไลด์
- Aspirin อย่างเดียวใช้ได้ใน TIA ความเสี่ยงต่ำ แต่รายนี้ ABCD2 = 5
- DAPT นาน 12 เดือนเพิ่ม bleeding โดยไม่ลด stroke เพิ่ม
- Warfarin สำหรับ cardioembolic (ไม่มี AF)
- TIA อาการหายแล้วไม่ต้อง thrombolysis''',
            pearl="High-risk TIA/minor stroke → DAPT 21 วัน → ASA", topic="DAPT",
            ref=[f"{D} หน้า 41"], nl=["B3.2.6(1)", "B2.4(3)"]),
    ])

LECTURE = lecture("02", "Stroke", "อาการตามหลอดเลือด · TOAST · rt-PA · secondary prevention",
    objectives=[
        "บอกหลอดเลือดที่อุดจากอาการ (ACA, MCA, PCA, Wallenberg, lacunar) ได้",
        "เรียงลำดับ CBG → CT และแยกสาเหตุตาม TOAST ได้",
        "ตัดสินใจให้ rt-PA ตามเวลา BP และ contraindication พร้อมคำนวณขนาดยาได้",
        "เลือก secondary prevention ให้ตรงกลไก (antiplatelet, DAPT, anticoagulant, CEA, BP) ได้",
    ],
    sections=[S1, S2, S3, S4])
