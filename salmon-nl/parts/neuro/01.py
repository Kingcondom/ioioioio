from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Neuro"

# ---------------------------------------------------------------- 01-01 Localization by level
F_LOC = fig("neuro-01-01-f1", "Localization ตามระดับของระบบประสาท", '''<svg viewBox="0 0 740 470">
 <rect x="10" y="40" width="90" height="178" rx="10" class="c1"/>
 <text x="55" y="112" text-anchor="middle" class="tw">UMN</text>
 <text x="55" y="132" text-anchor="middle" class="tw">↑DTR</text>
 <text x="55" y="150" text-anchor="middle" class="tw">Babinski +</text>
 <rect x="10" y="228" width="90" height="224" rx="10" class="c2"/>
 <text x="55" y="320" text-anchor="middle" class="tw">LMN /</text>
 <text x="55" y="338" text-anchor="middle" class="tw">motor unit</text>
 <text x="55" y="358" text-anchor="middle" class="tw">↓DTR</text>
 <text x="185" y="26" text-anchor="middle" class="tb">ระดับ lesion</text>
 <text x="480" y="26" text-anchor="middle" class="tb">ลักษณะเด่น (motor · sensory · อื่น ๆ)</text>
 <rect x="110" y="40" width="150" height="40" rx="8" class="c1soft"/>
 <text x="185" y="65" text-anchor="middle" class="tb">Cortex</text>
 <text x="272" y="57" class="t2">อ่อนแรงซีกตรงข้าม แขน ≠ ขา</text>
 <text x="272" y="74" class="t3">+ cortical sign (aphasia, neglect, eye deviation), ชัก</text>
 <rect x="110" y="86" width="150" height="40" rx="8" class="c1soft"/>
 <text x="185" y="111" text-anchor="middle" class="tb">Subcortical</text>
 <text x="272" y="103" class="t2">อ่อนแรงซีกตรงข้าม แขน = ขา</text>
 <text x="272" y="120" class="t3">fiber รวมกันแน่น (internal capsule) · ไม่มี cortical sign</text>
 <rect x="110" y="132" width="150" height="40" rx="8" class="c1soft"/>
 <text x="185" y="157" text-anchor="middle" class="tb">Brainstem</text>
 <text x="272" y="149" class="t2">CN palsy ข้างเดียวกัน + อ่อนแรงซีกตรงข้าม</text>
 <text x="272" y="166" class="t3">(crossed sign) · cerebellar sign · ชาซีกตรงข้าม</text>
 <rect x="110" y="178" width="150" height="40" rx="8" class="c1soft"/>
 <text x="185" y="203" text-anchor="middle" class="tb">Spinal cord</text>
 <text x="272" y="195" class="t2">มักเป็นสองข้าง (paraplegia/quadriplegia)</text>
 <text x="272" y="212" class="t3">sensory level · bowel/bladder · ปวดหลัง</text>
 <rect x="110" y="228" width="150" height="40" rx="8" class="c2soft"/>
 <text x="185" y="253" text-anchor="middle" class="tb">Anterior horn cell</text>
 <text x="272" y="245" class="t2">Pure motor · sensory ปกติ</text>
 <text x="272" y="262" class="t3">fasciculation, atrophy (เสริม)</text>
 <rect x="110" y="274" width="150" height="40" rx="8" class="c2soft"/>
 <text x="185" y="299" text-anchor="middle" class="tb">Nerve root</text>
 <text x="272" y="291" class="t2">ชาตาม dermatome</text>
 <text x="272" y="308" class="t3">ปวดร้าว (radicular pain)</text>
 <rect x="110" y="320" width="150" height="40" rx="8" class="c2soft"/>
 <text x="185" y="345" text-anchor="middle" class="tb">Peripheral nerve</text>
 <text x="272" y="337" class="t2">Motor + sensory (glove &amp; stocking)</text>
 <text x="272" y="354" class="t3">เด่นปลายมือปลายเท้า</text>
 <rect x="110" y="366" width="150" height="40" rx="8" class="c2soft"/>
 <text x="185" y="391" text-anchor="middle" class="tb">NMJ</text>
 <text x="272" y="383" class="t2">Pure motor · fluctuation (ล้าเมื่อใช้งาน)</text>
 <text x="272" y="400" class="t3">DTR มักปกติ (บางโรคลด เช่น LES, botulism)</text>
 <rect x="110" y="412" width="150" height="40" rx="8" class="c2soft"/>
 <text x="185" y="437" text-anchor="middle" class="tb">Muscle</text>
 <text x="272" y="429" class="t2">Pure motor · proximal &gt; distal</text>
 <text x="272" y="446" class="t3">ปวดกล้ามเนื้อได้ · DTR ปกติหรือลดเล็กน้อย</text>
</svg>''', "ไล่จากบนลงล่าง: สี่ระดับบนเป็น UMN (reflex ไว) ห้าระดับล่างเป็น motor unit (reflex ลด) แล้วใช้ลักษณะเด่นทางขวาแยกต่อ")

S1 = sec("neuro-01-01", "Localization: motor & sensory pathway ตามระดับ",
    "Cortex แขน≠ขา+cortical sign · subcortical แขน=ขา · brainstem crossed · cord sensory level · nerve glove-stocking · NMJ fluctuation · muscle proximal", minutes=8,
    source=f"{D} หน้า 5–18, 25", nl=["B3.1.2(5)", "2.1.22", "B3.1.1(3)"],
    md='''
### ทางเดินประสาทที่ต้องรู้

| Tract | หน้าที่ | ไขว้ที่ไหน |
|---|---|---|
| Corticospinal (descending) | Motor | **Medulla** (pyramidal decussation) |
| Posterior column (ascending) | Proprioception, vibration, fine touch | **Medulla** |
| Spinothalamic (ascending) | Pain, temperature | **ไขว้ทันทีใน spinal cord** (ใกล้ระดับที่เข้า) |

- ที่ **cortex** fiber กระจายตัว → lesion มักโดนบางส่วน จึงอ่อนแรง **แขนกับขาไม่เท่ากัน**
- ที่ **subcortical** (internal capsule) fiber รวมกันแน่น → lesion เล็กก็ทำให้อ่อนแรง **แขนเท่าขา**
- **ACA** เลี้ยงส่วนที่คุมขา (medial) → อ่อนแรง **ขา > แขน** · **MCA** เลี้ยงส่วนที่คุมหน้าและแขน (lateral) → **หน้าและแขน > ขา**

### ลักษณะตามระดับ (สรุปจากสไลด์)

[[fig:neuro-01-01-f1]]

| ระดับ | Motor | Sensory | DTR |
|---|---|---|---|
| Cortex | Hemiparesis ซีกตรงข้าม แขนขาไม่เท่ากัน | ชาซีกตรงข้าม | Hyperreflexia |
| Subcortical | Hemiparesis ซีกตรงข้าม แขนขาเท่ากัน | ชาซีกตรงข้าม | Hyperreflexia |
| Brainstem | CN palsy + hemiparesis ซีกตรงข้าม | Variable | Hyperreflexia |
| Spinal cord | ส่วนใหญ่สองข้าง (paraplegia/quadriplegia) | **Sensory level** (cape-like/hanging), ปวดหลัง | Hyperreflexia (ระยะ spinal shock ลด) |
| Anterior horn cell | อ่อนแรงอย่างเดียว | ปกติ | Hyporeflexia |
| Nerve root | ตาม myotome | ตาม **dermatome** + radiating pain | ลดเฉพาะราก |
| Peripheral nerve | Distal | **Glove & stocking** | Hyporeflexia |
| NMJ | **Fluctuation** | ปกติ | ปกติ (บางกรณีลด/หาย) |
| Muscle | **Proximal > distal** ± ปวดกล้ามเนื้อ | ปกติ | ปกติหรือลดเล็กน้อย |

> โจทย์อ่อนแรง ให้ถามสามข้อก่อนเสมอ: **UMN หรือ LMN (reflex/Babinski)** · **มี sensory ไหม และเป็น pattern ไหน** · **ข้างเดียว/สองข้าง/fluctuate ไหม**

### Brown-Séquard (เสริม)

ครึ่งซีกของ cord เสีย → **อ่อนแรง + เสีย proprioception ข้างเดียวกับ lesion** (corticospinal, posterior column ยังไม่ไขว้) แต่ **เสีย pain/temp ข้างตรงข้าม** (spinothalamic ไขว้แล้ว) — ใช้หลักการไขว้ในตารางข้างบน
''',
    figs=[F_LOC],
    pearls=[
        "Corticospinal และ posterior column ไขว้ที่ medulla · spinothalamic ไขว้ทันทีใน cord",
        "Cortex: แขน≠ขา + cortical sign · subcortical: แขน=ขา ไม่มี cortical sign",
        "ACA ขา>แขน · MCA หน้า+แขน>ขา",
        "Peripheral nerve = glove & stocking · NMJ = fluctuation · muscle = proximal",
        "Sensory level = spinal cord จนกว่าจะพิสูจน์ได้ว่าไม่ใช่",
    ],
    items=[
        mcq("NEURO-01-01-1",
            "A 66-year-old man with long-standing hypertension develops weakness of the right face, arm and leg of equal severity. He is alert, speaks normally, follows commands, and has no visual field defect or sensory loss. Where is the lesion most likely located?",
            "Posterior limb of the left internal capsule",
            ["Left frontal cortex", "Posterior limb of the right internal capsule", "Left lateral medulla", "Right cervical spinal cord"],
            explain='''อ่อนแรงซีกขวา **หน้า แขน ขา เท่ากัน** ไม่มี cortical sign (พูดปกติ ไม่มี neglect/field defect) = **subcortical** ที่ fiber รวมกันแน่น คือ **internal capsule ซีกซ้าย** (ฝั่งตรงข้ามกับอาการ) — ภาพของ pure motor lacunar stroke
- Left frontal cortex จะอ่อนแรงแขนขาไม่เท่ากัน และมักมี aphasia เพราะเป็น dominant hemisphere
- Internal capsule ซีกขวาจะทำให้อ่อนแรงซีก **ซ้าย** (corticospinal ไขว้ที่ medulla)
- Lateral medulla (Wallenberg) ไม่ทำให้อ่อนแรงครึ่งซีกเด่น แต่มี ataxia, Horner, ชา pain/temp แบบไขว้
- Cervical cord ซีกขวาไม่ทำให้หน้าอ่อนแรง และอาการจะอยู่ข้างเดียวกับ lesion''',
            pearl="แขน = ขา ไม่มี cortical sign → internal capsule ฝั่งตรงข้าม", topic="Subcortical lesion",
            ref=[f"{D} หน้า 5, 14, 25"], nl=["B3.1.1(7)", "B3.2.6(1)"]),
        mcq("NEURO-01-01-2",
            "A 48-year-old woman has 2 months of difficulty climbing stairs and combing her hair, with mild muscle aching. Sensation is normal, reflexes are 2+ and symmetric, and there is no ptosis or diurnal fluctuation. Plantar responses are flexor. At which level is the lesion most likely?",
            "Muscle",
            ["Anterior horn cell", "Peripheral nerve", "Neuromuscular junction", "Spinal cord"],
            explain='''อ่อนแรง **proximal (ขึ้นบันได หวีผม)** + ปวดกล้ามเนื้อ + sensory ปกติ + reflex ปกติ ไม่ fluctuate = **muscle (myopathy)**
- Anterior horn cell ทำให้อ่อนแรงแบบ LMN มี reflex ลด atrophy และ fasciculation
- Peripheral nerve จะมีชาแบบ glove & stocking และอ่อนแรงปลายมือเท้าเด่น reflex ลด
- NMJ (เช่น MG) อ่อนแรงแบบ **ล้าเมื่อใช้งาน ดีขึ้นเมื่อพัก** มักมีหนังตาตก/เห็นภาพซ้อน
- Spinal cord จะมี sensory level, reflex ไว, Babinski บวก และ bowel/bladder''',
            pearl="Proximal weakness + sensory ปกติ + ปวดกล้ามเนื้อ = muscle", topic="Weakness pattern",
            ref=[f"{D} หน้า 17, 25"], nl=["2.1.22", "B5.2.5-3(1)"]),
        mcq("NEURO-01-01-3",
            "A 55-year-old man with poorly controlled diabetes has 6 months of burning feet and numbness that has now reached the mid-shins and the fingertips. Examination shows weak toe dorsiflexion, absent ankle jerks and reduced pinprick in a stocking-and-glove distribution. Which level of the nervous system is primarily affected?",
            "Peripheral nerves",
            ["Spinal cord", "Nerve roots", "Anterior horn cells", "Neuromuscular junction"],
            explain='''ชา/ปวดแสบ **ปลายเท้าก่อนแล้วลามขึ้น จนถึงปลายนิ้วมือ (glove & stocking)** + อ่อนแรง distal + ankle jerk หาย = **peripheral nerve (length-dependent polyneuropathy)** เช่นจากเบาหวาน
- Spinal cord จะมี **sensory level** reflex ไว และ Babinski บวก
- Nerve root ชาตาม **dermatome** และมักปวดร้าว ไม่ใช่สมมาตรปลายมือปลายเท้า
- Anterior horn cell เป็น pure motor ไม่มีอาการชา
- NMJ เป็น pure motor และ fluctuate''',
            pearl="Glove & stocking + ↓DTR = peripheral neuropathy", topic="Peripheral nerve pattern",
            ref=[f"{D} หน้า 16, 25"], nl=["2.3.6-3(9)"]),
        mcq("NEURO-01-01-4",
            "A 28-year-old man is stabbed in the back. Examination shows weakness and loss of vibration and joint-position sense in the left leg, and loss of pain and temperature sensation in the right leg from below the umbilicus. Which lesion best explains these findings?",
            "Left hemisection of the thoracic spinal cord",
            ["Right hemisection of the thoracic spinal cord", "Anterior spinal cord syndrome", "Central cord syndrome", "Left L4 nerve root injury"],
            explain='''ใช้หลักการไขว้ในสไลด์: **corticospinal และ posterior column ไขว้ที่ medulla** จึงเสียข้างเดียวกับ lesion (ซ้าย) ส่วน **spinothalamic ไขว้ทันทีใน cord** จึงเสียข้างตรงข้าม (ขวา) = **Brown-Séquard ที่ cord ซีกซ้าย** ระดับ thoracic (ระดับสะดือ ≈ T10) (เสริม)
- Hemisection ซีกขวาจะทำให้อ่อนแรงขาขวาและเสีย pain/temp ขาซ้าย กลับกันกับผู้ป่วย
- Anterior cord syndrome เสีย motor และ pain/temp สองข้าง แต่ proprioception/vibration ดี
- Central cord syndrome เด่นที่แขนมากกว่าขา (มักเป็น cervical)
- L4 root ไม่ทำให้เสีย pain/temp ขาอีกข้าง''',
            pearl="Brown-Séquard: motor+proprioception ข้างเดียวกัน · pain/temp ข้างตรงข้าม", topic="Tract crossing",
            ref=[f"{D} หน้า 5–6"], nl=["B3.1.1(3)", "B3.2.3(3)"]),
    ])

# ---------------------------------------------------------------- 01-02 Cranial nerves & brainstem
F_CN = fig("neuro-01-02-f1", "CN nuclei ใน brainstem และ facial palsy แบบ UMN กับ LMN", '''<svg viewBox="0 0 740 360">
 <text x="150" y="24" text-anchor="middle" class="tb">CN nuclei ตามระดับ brainstem</text>
 <rect x="40" y="40" width="220" height="70" rx="12" class="c1soft"/>
 <text x="150" y="68" text-anchor="middle" class="tb">Midbrain</text>
 <text x="150" y="92" text-anchor="middle" class="ta">CN 3 · 4</text>
 <rect x="40" y="118" width="220" height="80" rx="12" class="c2soft"/>
 <text x="150" y="150" text-anchor="middle" class="tb">Pons</text>
 <text x="150" y="176" text-anchor="middle" class="ta">CN 5 · 6 · 7 · 8</text>
 <rect x="40" y="206" width="220" height="80" rx="12" class="oksoft"/>
 <text x="150" y="238" text-anchor="middle" class="tb">Medulla</text>
 <text x="150" y="264" text-anchor="middle" class="ta">CN 9 · 10 · 11 · 12</text>
 <text x="150" y="312" text-anchor="middle" class="t3">CN palsy ข้างเดียวกัน + อ่อนแรงซีกตรงข้าม</text>
 <text x="150" y="330" text-anchor="middle" class="t3">= ระดับเดียวกับ nucleus ของ CN นั้น</text>
 <text x="530" y="24" text-anchor="middle" class="tb">Facial palsy</text>
 <ellipse cx="420" cy="140" rx="62" ry="78" class="box"/>
 <path d="M420 140L482 140A62 78 0 0 1 420 218Z" class="badsoft"/>
 <path d="M358 140H482" class="lnf"/>
 <path d="M420 62V218" class="lnf"/>
 <text x="420" y="246" text-anchor="middle" class="tb">UMN type</text>
 <text x="420" y="266" text-anchor="middle" class="t2">อ่อนแรงเฉพาะครึ่งล่าง (ปาก)</text>
 <text x="420" y="284" text-anchor="middle" class="t2">ฝั่ง<tspan class="tb">ตรงข้าม</tspan>กับ lesion</text>
 <text x="420" y="304" text-anchor="middle" class="t3">หน้าผากรอด (เลี้ยงสองข้าง)</text>
 <text x="420" y="324" text-anchor="middle" class="t3">stroke, brain tumor</text>
 <ellipse cx="640" cy="140" rx="62" ry="78" class="box"/>
 <path d="M640 62A62 78 0 0 1 640 218Z" class="badsoft"/>
 <path d="M578 140H702" class="lnf"/>
 <path d="M640 62V218" class="lnf"/>
 <text x="640" y="246" text-anchor="middle" class="tb">LMN type</text>
 <text x="640" y="266" text-anchor="middle" class="t2">อ่อนแรงทั้งบนและล่าง</text>
 <text x="640" y="284" text-anchor="middle" class="t2">ฝั่ง<tspan class="tb">เดียวกับ</tspan> lesion</text>
 <text x="640" y="304" text-anchor="middle" class="t3">หลับตาไม่สนิท ยักคิ้วไม่ได้</text>
 <text x="640" y="324" text-anchor="middle" class="t3">Bell's palsy, Ramsay Hunt</text>
</svg>''', "ซ้าย: จำเป็นกลุ่ม 2–4–4 (3-4 / 5-8 / 9-12) ตามระดับ midbrain–pons–medulla · ขวา: บริเวณสีแดงคือส่วนที่อ่อนแรง UMN รอดหน้าผาก LMN เสียทั้งซีก")

S2 = sec("neuro-01-02", "Cranial nerves, brainstem & facial palsy (UMN vs LMN)",
    "Midbrain 3-4 · pons 5-8 · medulla 9-12 · pupil reflex เข้า 2 ออก 3 · gag เข้า 9 ออก 10 · UMN facial palsy รอดหน้าผาก", minutes=7,
    source=f"{D} หน้า 19–24, 51–52", nl=["B3.1.1(5)", "B3.1.1(4)", "B3.1.2(8)"],
    md='''
### ตำแหน่ง nucleus ใน brainstem

- **Midbrain**: CN 3, 4 · **Pons**: CN 5, 6, 7, 8 · **Medulla**: CN 9, 10, 11, 12
- Brainstem lesion = **CN palsy ข้างเดียวกับ lesion + hemiparesis ซีกตรงข้าม** (corticospinal ยังไม่ไขว้จนถึง medulla) → ใช้ CN ที่เสียบอกระดับ

[[fig:neuro-01-02-f1]]

### หน้าที่ CN (สไลด์)

| CN | หน้าที่หลัก |
|---|---|
| I Olfactory | ดมกลิ่น |
| II Optic | การมองเห็น · **afferent** ของ pupillary light reflex |
| III Oculomotor | ลืมตา (levator) · กลอกตาทุกมัดยกเว้น LR, SO · **pupil constriction** · accommodation |
| IV Trochlear | Superior oblique |
| V Trigeminal | ความรู้สึกที่หน้า · กล้ามเนื้อเคี้ยว |
| VI Abducens | Lateral rectus |
| VII Facial | แสดงสีหน้า · รับรส **anterior 2/3** ของลิ้น · น้ำลาย น้ำตา |
| VIII Vestibulocochlear | การทรงตัว (vestibular) · การได้ยิน (cochlear) |
| IX Glossopharyngeal | รับรส posterior 1/3 · **afferent** ของ gag reflex · กลืน น้ำลาย |
| X Vagus | กลืน · **efferent** ของ gag reflex |
| XI Accessory | หันหน้า (SCM) · ยักไหล่ (trapezius) |
| XII Hypoglossal | แลบลิ้น |

- จำ **LR6 SO4** (ที่เหลือ CN3) · pupillary reflex **"เข้า 2 ออก 3"** · gag reflex **"เข้า 9 ออก 10"**
- CN6 palsy = ตามองออกด้านข้างไม่ได้ (lateral gaze palsy) — เป็น false localizing sign ของ ↑ICP ได้ (ดูหมวด headache)

### Facial palsy: UMN vs LMN

| | UMN type | LMN type |
|---|---|---|
| ส่วนที่อ่อนแรง | **ครึ่งล่างของหน้า (ปาก)** | **ทั้งบนและล่าง** (หลับตา ยักคิ้วไม่ได้) |
| ข้าง | **ตรงข้าม** lesion | **เดียวกับ** lesion |
| สาเหตุ | Stroke, brain tumor | Bell's palsy, trauma, Ramsay Hunt, malignant otitis externa |

- เหตุผล: กล้ามเนื้อหน้าผากได้ UMN จาก cortex **ทั้งสองข้าง** จึงรอดใน UMN lesion (เสริม)

> โจทย์ "bilateral lateral gaze palsy + quadriparesis + ซึม" (เช่น embolus จาก mitral stenosis ไปอุด basilar) → **pons**
''',
    figs=[F_CN],
    pearls=[
        "Midbrain 3,4 · pons 5,6,7,8 · medulla 9–12",
        "Light reflex เข้า 2 ออก 3 · gag reflex เข้า 9 ออก 10",
        "LR6 SO4 ที่เหลือ CN3 (รวม levator และ pupil)",
        "UMN facial palsy: ปากเบี้ยวฝั่งตรงข้าม หน้าผากรอด · LMN: ทั้งซีกฝั่งเดียวกัน",
        "CN palsy ข้างหนึ่ง + hemiparesis อีกข้าง = brainstem ที่ระดับ CN นั้น",
    ],
    items=[
        mcq("NEURO-01-02-1",
            "A 50-year-old woman with known rheumatic heart disease suddenly loses consciousness. BP 180/100 mmHg. Examination: GCS E4V1M1, cardiomegaly, a grade 3/6 diastolic rumbling murmur at the apex, inability to abduct either eye (bilateral lateral gaze palsy), and quadriparesis. Where is the lesion?",
            "Pons",
            ["Midbrain", "Uncus of the temporal lobe", "Frontal lobe", "Basal ganglia"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 51–52)",
            explain='''Diastolic rumble ที่ apex = **mitral stenosis** → emboli ไปอุด basilar artery · ตามองออกด้านข้างไม่ได้สองข้าง = **CN6 สองข้าง** ซึ่ง nucleus อยู่ที่ **pons** + quadriparesis (corticospinal ทั้งสองข้างผ่าน basis pontis) → **pons** (สไลด์เฉลยด้วยแผนภาพ CN 5 6 7 8 อยู่ใน pons)
- Midbrain มี CN3, 4 จะเห็นรูม่านตาขยาย/หนังตาตก ตามองขึ้นลงผิดปกติ ไม่ใช่ lateral gaze palsy
- Uncal herniation ทำให้ CN3 palsy ข้างเดียว (รูม่านตาโต) ร่วมกับอ่อนแรงซีกตรงข้าม
- Frontal lobe ไม่ทำให้ CN6 palsy สองข้าง และไม่ทำให้ quadriparesis ทันที
- Basal ganglia ทำให้อ่อนแรงครึ่งซีก ไม่ใช่สองข้างพร้อม CN6''',
            pearl="Bilateral CN6 + quadriparesis = pons (basilar)", topic="Brainstem localization",
            ref=[f"{D} หน้า 19, 51–52"], nl=["B3.1.1(4)", "B3.2.6(1)"]),
        mcq("NEURO-01-02-2",
            "A 62-year-old man suddenly develops a drooping left eyelid. Examination shows a dilated left pupil, the left eye deviated down and out, and weakness of the right arm and leg with a right extensor plantar response. Where is the lesion?",
            "Left midbrain",
            ["Right midbrain", "Left pons", "Left medulla", "Left internal capsule"],
            explain='''**CN3 palsy ซ้าย** (หนังตาตก รูม่านตาโต ตาลงล่าง-ออกนอก) + **อ่อนแรงซีกขวา** = crossed sign → lesion อยู่ที่ระดับ nucleus/fascicle ของ CN3 คือ **midbrain ซีกซ้าย** (Weber syndrome — ชื่อเสริม)
- Midbrain ขวาจะทำให้ CN3 palsy ข้างขวาและอ่อนแรงซีกซ้าย
- Pons ซ้ายจะเห็น CN6 หรือ CN7 palsy ซ้าย ไม่ใช่ CN3
- Medulla ซ้ายเกี่ยวกับ CN9–12 (กลืนลำบาก เสียงแหบ ลิ้นเบี้ยว)
- Internal capsule ไม่ทำให้ CN3 palsy''',
            pearl="CN3 palsy + hemiparesis ซีกตรงข้าม = midbrain", topic="Crossed brainstem sign",
            ref=[f"{D} หน้า 15, 19–20"], nl=["B3.1.1(4)", "B3.1.1(5)"]),
        mcq("NEURO-01-02-3",
            "A 70-year-old woman wakes up with drooping of the right corner of her mouth and weakness of the right arm. She can wrinkle her forehead and close both eyes tightly. Which is the most likely site and type of facial weakness?",
            "Upper motor neuron lesion in the left cerebral hemisphere",
            ["Lower motor neuron lesion of the right facial nerve", "Upper motor neuron lesion in the right cerebral hemisphere", "Lower motor neuron lesion of the left facial nerve", "Right-sided pontine facial nucleus lesion"],
            explain='''อ่อนแรงเฉพาะ **ครึ่งล่างของหน้า** โดยหน้าผาก/การหลับตายังดี = **UMN facial palsy** ซึ่งอยู่ **ฝั่งตรงข้ามกับ lesion** และมีแขนขวาอ่อนแรงร่วม → lesion ที่ **ซีกสมองซ้าย** (เช่น MCA stroke)
- LMN ของ CN7 ขวา (Bell's palsy) จะหลับตาไม่สนิทและยักคิ้วไม่ได้ และไม่ทำให้แขนอ่อนแรง
- UMN ที่สมองซีกขวาจะทำให้ปากเบี้ยวด้าน **ซ้าย**
- LMN CN7 ซ้ายทำให้หน้าซีกซ้ายอ่อนแรงทั้งซีก
- Facial nucleus ที่ pons เป็น LMN-type คือเสียทั้งซีกข้างเดียวกัน''',
            pearl="หน้าผากรอด = UMN · ฝั่งตรงข้ามกับ lesion", topic="Facial palsy UMN vs LMN",
            ref=[f"{D} หน้า 24"], nl=["2.3.6(2)", "B3.1.1(5)"]),
        mcq("NEURO-01-02-4",
            "During examination of an unconscious trauma patient, shining light in the right eye produces no constriction of either pupil, whereas shining light in the left eye produces constriction of both pupils. Which structure is damaged?",
            "Right optic nerve",
            ["Right oculomotor nerve", "Left optic nerve", "Left oculomotor nerve", "Right trochlear nerve"],
            explain='''Pupillary light reflex **เข้า CN2 ออก CN3** · ส่องตาขวาแล้ว **ไม่หดทั้งสองข้าง** แต่ส่องตาซ้ายแล้ว **หดทั้งสองข้าง** (รวมตาขวา) แปลว่า efferent CN3 ขวายังดี ปัญหาอยู่ที่ขาเข้าของตาขวา = **right optic nerve** (afferent defect)
- Right CN3 เสียจะทำให้ตาขวาไม่หดไม่ว่าส่องข้างไหน
- Left optic nerve เสียจะไม่หดเมื่อส่องตาซ้าย
- Left CN3 เสียตาซ้ายจะไม่หดเลย
- CN4 ไม่เกี่ยวกับ pupil''',
            pearl="Light reflex: เข้า 2 ออก 3 — ส่องข้างไหนไม่หดทั้งคู่ = CN2 ข้างนั้น", topic="Pupillary reflex",
            ref=[f"{D} หน้า 20"], nl=["B3.1.2(8)", "B3.1.1(5)"]),
    ])

LECTURE = lecture("01", "Neuro localization", "UMN vs LMN · tracts · CN · facial palsy",
    objectives=[
        "บอกระดับ lesion จาก pattern อ่อนแรง ชา และ reflex ได้",
        "ใช้หลักการไขว้ของ tract อธิบาย crossed sign และ Brown-Séquard ได้",
        "จำตำแหน่ง CN nuclei และใช้ CN palsy บอกระดับ brainstem ได้",
        "แยก facial palsy แบบ UMN กับ LMN ได้",
    ],
    sections=[S1, S2])
