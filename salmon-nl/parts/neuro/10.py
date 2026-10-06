from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Neuro"

# ---------------------------------------------------------------- 10-01 Facial nerve palsy
S1 = sec("neuro-10-01", "Facial nerve palsy: Bell's palsy & Ramsay Hunt",
    "LMN facial palsy: Bell's (idiopathic) → prednisolone ± acyclovir · vesicle ที่หู = Ramsay Hunt → acyclovir + prednisolone · eye care · UMN (หน้าผากรอด) = stroke/tumor", minutes=7,
    source=f"{D} หน้า 24, 348–357", nl=["2.3.6(2)", "B3.2.2(6)"],
    md='''
### สาเหตุ (สไลด์)

| LMN | UMN |
|---|---|
| **Idiopathic — Bell's palsy (พบบ่อยสุด)** | **Stroke** |
| Trauma (temporal bone fracture) | Brain tumor |
| Infection: **herpes zoster (Ramsay Hunt)**, **malignant otitis externa** | |

- UMN: อ่อนแรงเฉพาะครึ่งล่างของหน้า ฝั่งตรงข้าม lesion · LMN: ทั้งบนและล่าง ฝั่งเดียวกัน (ดูหมวด localization)

### Bell's palsy

- **Unilateral LMN facial palsy** เฉียบพลัน (ภายใน 72 ชม. — เสริม)
- ↓tearing, ↓saliva, **↓taste anterior 2/3**, (hyperacusis — เสริม)
- **Corneal drying/abrasion** จากหลับตาไม่สนิท
- **Tx: prednisolone ± acyclovir** (prednisolone 60 mg/day × 5 วัน แล้วลด หรือ 1 mg/kg — เริ่มภายใน 72 ชม. — เสริม)
- **Eye care**: artificial tears, eye ointment, eye patch
- ไม่ต้องทำ CT/MRI ถ้าเป็น LMN แบบทั่วไปและ neuro/หูปกติ

### Ramsay Hunt syndrome

- **Herpes zoster oticus** (painful vesicles ที่ใบหู/รูหู) **+ unilateral LMN facial palsy** (± hearing loss, vertigo)
- **Tx: acyclovir + prednisolone** + eye care

### Malignant otitis externa (เสริม)

- ผู้สูงอายุ **เบาหวาน** ปวดหูมาก หูน้ำหนวก granulation tissue → Pseudomonas → CN7 palsy → CT/MRI temporal bone + anti-pseudomonal ATB

> LMN palsy + **vesicles ที่หู** → Ramsay Hunt → ต้องมี **acyclovir** · LMN palsy + เบาหวาน + ปวดหูหนองไหล → คิด malignant otitis externa
''',
    pearls=[
        "Bell's palsy = idiopathic LMN → prednisolone (± acyclovir) + eye care",
        "LMN palsy + vesicles ที่หู = Ramsay Hunt → acyclovir + prednisolone",
        "Bell's: ↓taste anterior 2/3 ↓น้ำตา corneal exposure",
        "หน้าผากรอด = UMN → หา stroke ไม่ใช่ Bell's",
    ],
    items=[
        mcq("NEURO-10-01-1",
            "A 40-year-old man with hypertension has had asymmetric right facial expression for 1 day. Examination: incomplete closure of the right eye, drooping of the right corner of the mouth and inability to wrinkle the right forehead. Neuro-otological examination is otherwise normal. What is the most appropriate management?",
            "Oral prednisolone",
            ["Plasma glucose only", "CT brain", "MRI brain", "Oral aspirin 325 mg"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 352–353)",
            explain='''LMN facial palsy (หลับตาไม่สนิท + หน้าผากเสีย) โดยหูและ neuro อื่นปกติ = **Bell's palsy** → **prednisolone** (± acyclovir) + eye care
- Plasma glucose อาจตรวจเพราะเบาหวานเป็นปัจจัยเสี่ยง แต่ไม่ใช่การรักษา
- CT/MRI brain ไม่จำเป็นใน LMN palsy ทั่วไป — ต้องทำถ้าเป็น UMN pattern หรือมี deficit อื่น
- Aspirin ใช้กับ ischemic stroke ซึ่งจะเป็น UMN (หน้าผากรอด) — HT เป็นตัวหลอก''',
            pearl="LMN facial palsy แบบเดี่ยว → prednisolone", topic="Bell's palsy",
            ref=[f"{D} หน้า 350, 352–353"], nl=["2.3.6(2)", "B3.2.2(6)"]),
        mcq("NEURO-10-01-2",
            "A 60-year-old man has had an asymmetric smile for 3 days. BT 37°C. Examination: right facial drooping with drooling, inability to close the right eye or raise the right eyebrow, and vesicles on the right ear pinna. What is the most likely diagnosis?",
            "Ramsay Hunt syndrome",
            ["Bell's palsy", "Facial nerve neuritis", "Malignant otitis externa", "Facial nerve neuroma"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 354–355)",
            explain='''**LMN facial palsy + vesicles ที่ใบหู** = **Ramsay Hunt syndrome** (herpes zoster oticus + facial palsy) — ตัวเลือก "herpes zoster oticus" ในสไลด์ถูกเปลี่ยนเพราะเป็นส่วนหนึ่งของคำตอบ
- Bell's palsy ไม่มี vesicles
- Facial nerve neuritis เป็นคำกว้าง ไม่ระบุสาเหตุ
- Malignant otitis externa พบในเบาหวาน มีหนองและ granulation tissue ในรูหู ไม่ใช่ vesicles
- Neuroma ค่อยเป็นค่อยไปหลายเดือน''',
            pearl="Facial palsy + vesicles ที่หู = Ramsay Hunt", topic="Ramsay Hunt",
            ref=[f"{D} หน้า 351, 354–355"], nl=["2.3.6(2)"]),
        mcq("NEURO-10-01-3",
            "A 40-year-old woman with diabetes has had right ear pain and drooping of the right side of her face for 1 day. Examination: weakness of both orbicularis oculi and orbicularis oris on the right, and painful vesicles in the right external auditory canal and concha. DTX 134 mg/dL. What is the most appropriate management?",
            "Prednisolone plus acyclovir",
            ["Prednisolone alone", "Aspirin", "CT scan of the brain", "Gabapentin"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 356–357)",
            explain='''Ramsay Hunt syndrome (ภาพหูในสไลด์เป็น vesicles — บรรยายเป็นข้อความ) → **acyclovir + prednisolone** (สไลด์) + eye care
- Prednisolone เดี่ยวไม่ครอบคลุม VZV
- Aspirin สำหรับ stroke (UMN)
- CT ไม่จำเป็นเมื่อสาเหตุชัด
- Gabapentin ช่วยปวดได้แต่ไม่ใช่การรักษาหลัก''',
            pearl="Ramsay Hunt → acyclovir + prednisolone", topic="Ramsay Hunt treatment",
            ref=[f"{D} หน้า 351, 356–357"], nl=["2.3.6(2)"]),
        mcq("NEURO-10-01-4",
            "A 35-year-old woman with Bell's palsy cannot fully close her left eye. In addition to oral prednisolone, which measure is most important to prevent a complication?",
            "Artificial tears by day, eye ointment and taping or patching the eye at night",
            ["Topical corticosteroid eye drops", "Daily facial nerve conduction studies", "Prophylactic oral antibiotics", "Botulinum toxin injection to the orbicularis oculi"],
            explain='''หลับตาไม่สนิท → **corneal drying/abrasion** → ต้อง **eye care: artificial tears, eye ointment, eye patch** (สไลด์)
- Steroid หยอดตาไม่ป้องกัน exposure keratopathy และเสี่ยงติดเชื้อ
- NCS ไม่ป้องกันภาวะแทรกซ้อน
- ไม่มีข้อบ่งชี้ให้ ATB
- Botulinum toxin ทำให้หลับตาไม่ได้มากขึ้น (ใช้รักษา synkinesis ภายหลัง)''',
            pearl="Bell's palsy: อย่าลืม eye care", topic="Corneal protection",
            ref=[f"{D} หน้า 350"], nl=["2.3.6(2)"]),
    ])

# ---------------------------------------------------------------- 10-02 GBS
F_GBS = fig("neuro-10-02-f1", "GBS: เส้นเวลาและการตัดสินใจให้ IVIG/plasmapheresis", '''<svg viewBox="0 0 740 360">
 <defs><marker id="neuro-10-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <path d="M30 70H710" class="ln" marker-end="url(#neuro-10-02-a)"/>
 <rect x="30" y="20" width="170" height="40" rx="8" class="sunk"/>
 <text x="115" y="38" text-anchor="middle" class="tb">URI / GI infection</text>
 <text x="115" y="54" text-anchor="middle" class="t3">C. jejuni (บ่อยสุด)</text>
 <text x="250" y="44" text-anchor="middle" class="t3">1–4 สัปดาห์</text>
 <rect x="300" y="20" width="200" height="40" rx="8" class="badsoft"/>
 <text x="400" y="38" text-anchor="middle" class="tb">อ่อนแรงขึ้นจากขา</text>
 <text x="400" y="54" text-anchor="middle" class="t3">areflexia · ชาปลายมือเท้า</text>
 <rect x="520" y="20" width="190" height="40" rx="8" class="sunk"/>
 <text x="615" y="38" text-anchor="middle" class="tb">แย่สุดใน ≤ 4 สัปดาห์</text>
 <text x="615" y="54" text-anchor="middle" class="t3">แล้วค่อยฟื้น (เสริม)</text>
 <rect x="30" y="92" width="330" height="104" rx="10" class="c1soft"/>
 <text x="195" y="114" text-anchor="middle" class="tb">วินิจฉัย</text>
 <text x="44" y="138" class="t2">LP: <tspan class="tb">protein ↑ + WBC &lt; 10</tspan></text>
 <text x="44" y="158" class="t3">(albuminocytologic dissociation — ปกติได้ในสัปดาห์แรก)</text>
 <text x="44" y="180" class="t2">NCS: ↓conduction velocity (demyelination)</text>
 <rect x="380" y="92" width="330" height="104" rx="10" class="misssoft"/>
 <text x="545" y="114" text-anchor="middle" class="tb">Admit ทุกราย · monitor</text>
 <text x="394" y="138" class="t2">หายใจ: FVC/NIF, ไอ กลืน → ETT</text>
 <text x="394" y="160" class="t2">Autonomic: cardiac monitor, BP</text>
 <text x="394" y="182" class="t3">arrhythmia, BP ขึ้นลง</text>
 <path d="M370 196V218" class="ln" marker-end="url(#neuro-10-02-a)"/>
 <rect x="120" y="220" width="500" height="40" rx="10" class="acsoft"/>
 <text x="370" y="245" text-anchor="middle" class="tb">มีข้อบ่งชี้ข้อใดข้อหนึ่ง?</text>
 <path d="M250 260L190 288" class="ln" marker-end="url(#neuro-10-02-a)"/>
 <path d="M490 260L560 288" class="ln" marker-end="url(#neuro-10-02-a)"/>
 <rect x="20" y="290" width="400" height="64" rx="10" class="bad"/>
 <text x="220" y="310" text-anchor="middle" class="tw">ใช่ → IVIG หรือ plasmapheresis</text>
 <text x="220" y="328" text-anchor="middle" class="tw">เดินเอง &gt; 10 m ไม่ได้ · autonomic รุนแรง</text>
 <text x="220" y="346" text-anchor="middle" class="tw">dysphagia · respiratory failure</text>
 <rect x="440" y="290" width="280" height="64" rx="10" class="oksoft"/>
 <text x="580" y="314" text-anchor="middle" class="tb">ไม่ → admit observe</text>
 <text x="580" y="336" text-anchor="middle" class="t3">supportive · steroid ไม่ได้ผล</text>
</svg>''', "บน: GBS ตามหลังการติดเชื้อ 1–4 สัปดาห์ · กลาง: ยืนยันด้วย CSF/NCS และ admit เฝ้าการหายใจกับ autonomic ทุกราย · ล่าง: ข้อบ่งชี้ immunotherapy ตามสไลด์ (เดินเองไม่ได้ > 10 m, autonomic รุนแรง, dysphagia, หายใจล้มเหลว) — steroid ไม่ได้ผล")

S2 = sec("neuro-10-02", "Guillain-Barré syndrome",
    "หลัง URI/GI (C. jejuni) 1–4 สัปดาห์ · ascending flaccid weakness + areflexia + glove-stocking + CN (facial) + autonomic · CSF protein ↑ WBC <10 · admit ทุกราย · IVIG/PLEX ถ้าเดิน >10 m ไม่ได้ dysphagia หายใจล้มเหลว autonomic · ไม่ใช้ steroid", minutes=9,
    source=f"{D} หน้า 358–376", nl=["2.3.6-3(4)", "B3.2.2-3(2)", "2.1.22"],
    md='''
### Pathophysiology

- **Acute immune-mediated polyneuropathy** — autoantibody ต่อ **myelin sheath** (molecular mimicry)
- Risk: **Campylobacter jejuni (พบบ่อยสุด)** (bloody diarrhea), URI, CMV, EBV, Zika, วัคซีน (เสริม)

### อาการ

[[fig:neuro-10-02-f1]]

- **Preceding URI/GI infection** (1–4 สัปดาห์ก่อน)
- **Bilateral ascending flaccid paresis** เริ่มจากขา (proximal อาจเด่นได้)
- **Sensory loss (glove & stocking)**, ชาเสียว (paresthesia), อาจเสีย proprioception/vibration
- **↓/absent DTR** (areflexia)
- **Autonomic dysfunction**: arrhythmia, BP ต่ำ/สูงสลับ
- **CN palsy** — **facial palsy (มักสองข้าง)**, bulbar (↓gag, dysphagia), ophthalmoplegia (Miller Fisher — เสริม)
- Respiratory muscle weakness → **paradoxical breathing**, respiratory failure
- Sphincter มักปกติ, plantar flexor (ต่างจาก cord)

### Investigation

- **LP: albuminocytologic dissociation** — **protein ↑, WBC ปกติ (< 10/mm3)** (อาจปกติในสัปดาห์แรก — เสริม)
- **Nerve conduction study: ↓nerve conduction velocity** (demyelination)
- (เสริม) FVC/NIF เป็นระยะ — FVC < 20 mL/kg = เตรียม ETT

### Management (สไลด์)

- **Admit observe ทุกราย + supportive**
- **Respiratory distress → ventilation support**
- **Autonomic → cardiac monitoring**
- **IVIG (0.4 g/kg/day × 5 วัน — เสริม) หรือ plasmapheresis** เมื่อมีข้อใดข้อหนึ่ง:
  - **Inability to walk > 10 m unaided**
  - **Severe autonomic dysfunction** (เช่น arrhythmia)
  - **Dysphagia**
  - **Respiratory failure**
- **Corticosteroid ไม่ได้ผลใน GBS** (เสริม)

### Ddx: beriberi (thiamine deficiency)

- **Dry beriberi**: symmetrical peripheral neuropathy (sensorimotor, areflexia) — คนดื่มสุรา ขาดอาหาร กินข้าวขาวอย่างเดียว (กรรมกร — เสริม)
- **Wet beriberi**: high-output cardiac failure
- Tx: **thiamine** (vitamin B1)
''',
    figs=[F_GBS],
    pearls=[
        "GBS: หลังท้องเสีย/หวัด + อ่อนแรงขึ้นจากขา + areflexia",
        "CSF protein สูง WBC < 10 = albuminocytologic dissociation",
        "Facial palsy สองข้าง + areflexia = นึกถึง GBS",
        "IVIG/PLEX เมื่อเดินเอง > 10 m ไม่ได้ / dysphagia / หายใจล้มเหลว / autonomic",
        "Steroid ไม่ได้ผลใน GBS",
    ],
    items=[
        mcq("NEURO-10-02-1",
            "A 10-year-old girl had a common cold 1 week ago. She now has symmetrical weakness for 2 days. Examination: facial palsy, motor power 2/5 in the arms and 1/5 in the legs, symmetrical loss of pinprick and proprioception, and areflexia. What is the most likely diagnosis?",
            "Guillain-Barré syndrome",
            ["Poliomyelitis", "Transverse myelitis", "Myasthenia gravis", "Toxic neuropathy from heavy metal"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 361–362)",
            explain='''หลังหวัด + อ่อนแรงสมมาตร (ขามากกว่าแขน) + **areflexia** + **ชา** + **facial palsy** = **GBS**
- Poliomyelitis เป็น pure motor ไม่สมมาตร ไม่มีชา
- Transverse myelitis มี sensory level และ sphincter
- MG ไม่มีชาและ reflex ปกติ
- Toxic neuropathy (เช่น arsenic) มักค่อยเป็นค่อยไปและมีประวัติสัมผัส''',
            pearl="หลังหวัด + ascending + areflexia + facial palsy = GBS", topic="GBS diagnosis",
            ref=[f"{D} หน้า 359, 361–362"], nl=["2.3.6-3(4)"]),
        mcq("NEURO-10-02-2",
            "An 18-year-old man visited a child-care center 2 weeks ago where several children had diarrhea. He now has progressive weakness of the limbs. Examination: upper limb power 4/5, lower limb power 1/5, absent deep tendon reflexes, flexor plantar responses, normal sphincter tone. What is the most likely diagnosis?",
            "Guillain-Barré syndrome",
            ["Transverse myelitis", "Myasthenia gravis", "Neurosyphilis", "Hypokalemic periodic paralysis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 363–364)",
            explain='''ติดเชื้อนำมาก่อน 2 สัปดาห์ + อ่อนแรง **ขามากกว่าแขน (ascending)** + **areflexia** + plantar flexor sphincter ปกติ = **GBS** (เติมข้อมูลท้องเสีย plantar และ sphincter ในโจทย์)
- Transverse myelitis มี sensory level, sphincter เสีย และ Babinski
- MG ไม่ทำ areflexia
- Neurosyphilis (tabes dorsalis) เรื้อรัง เสีย proprioception
- Hypokalemic PP เป็นซ้ำ ๆ หลังกินอาหาร ไม่มีประวัติติดเชื้อนำ''',
            pearl="Ascending + areflexia + sphincter ปกติ = GBS", topic="GBS diagnosis",
            ref=[f"{D} หน้า 359, 363–364"], nl=["2.3.6-3(4)"]),
        mcq("NEURO-10-02-3",
            "A 25-year-old man had bloody diarrhea 2 weeks ago and now has limb weakness. Examination: bilateral facial palsy, proximal muscle power 1/5, distal power 4/5, decreased sensation in a glove-and-stocking distribution and areflexia. What is the most appropriate investigation?",
            "Lumbar puncture",
            ["MRI spine", "Serum creatine kinase", "Serum electrolytes", "Thyroid function tests"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 365–366)",
            explain='''**Bloody diarrhea (C. jejuni)** + bilateral facial palsy + areflexia + ชา glove-stocking = **GBS** → **LP** หา **albuminocytologic dissociation** (± NCS)
- MRI spine ใช้เมื่อสงสัย cord (sensory level, sphincter)
- CK ใช้กับ myopathy ซึ่งไม่มีชาและไม่มี facial palsy
- Electrolytes ใช้กับ periodic paralysis (ไม่มีชา)
- Thyroid function ใช้กับ thyrotoxic PP/myopathy''',
            pearl="สงสัย GBS → LP (protein ↑ WBC ปกติ)", topic="GBS investigation",
            ref=[f"{D} หน้า 358–359, 365–366"], nl=["2.3.6-3(4)", "B3.3(2)"]),
        mcq("NEURO-10-02-4",
            "A 15-year-old developed muscle weakness and inability to walk 2 weeks after a flu-like illness. Examination: bilateral facial palsy, quadriparesis, areflexia; vital signs normal. CSF: protein 80 mg/dL, cells 0–2/mm3. What is the most likely diagnosis?",
            "Guillain-Barré syndrome",
            ["Poliomyelitis", "Polymyositis", "Acute transverse myelitis", "Botulism"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 369–370)",
            explain='''หลังไข้หวัด + quadriparesis + areflexia + bilateral facial palsy + **CSF protein สูง เซลล์ปกติ** = **GBS**
- Poliomyelitis CSF มี pleocytosis และเป็น asymmetric pure motor
- Polymyositis ไม่มี facial palsy/areflexia และ CSF ปกติ
- Transverse myelitis มี sensory level และ CSF pleocytosis
- Botulism เป็น **descending** เริ่มจากตา/bulbar มีรูม่านตาขยาย CSF ปกติ''',
            pearl="CSF protein ↑ + cells ปกติ = GBS", topic="Albuminocytologic dissociation",
            ref=[f"{D} หน้า 359, 369–370"], nl=["2.3.6-3(4)"]),
        mcq("NEURO-10-02-5",
            "A 58-year-old woman had a cold 2 weeks ago and has had weakness for 2 days. Examination: facial palsy, proximal muscle power 4/5 (she can walk unaided across the ward), impaired vibration and proprioception, and impaired pinprick sensation in the hands and feet. Swallowing and breathing are normal; FVC is normal. What is the most appropriate management?",
            "Admit for observation with respiratory and cardiac monitoring",
            ["Reassure and discharge", "Oral corticosteroid", "IV immunoglobulin", "Plasmapheresis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 371–372)",
            explain='''GBS ระยะแรกที่ยัง **เดินได้เอง (> 10 m)** ไม่มี dysphagia/หายใจล้มเหลว/autonomic รุนแรง → **admit observe + supportive** เฝ้าระวังการหายใจและหัวใจ (สไลด์เฉลยด้วยเกณฑ์ IVIG/PLEX)
- ส่งกลับบ้านไม่ได้ เพราะ GBS อาจลุกลามจนหายใจล้มเหลวภายในชั่วโมง–วัน
- Corticosteroid ไม่ได้ผลใน GBS
- IVIG/plasmapheresis ใช้เมื่อเข้าเกณฑ์ ซึ่งรายนี้ยังไม่เข้า''',
            pearl="GBS เดินได้ ไม่มี bulbar/หายใจ → admit observe", topic="GBS management",
            ref=[f"{D} หน้า 360, 371–372"], nl=["2.3.6-3(4)"]),
        mcq("NEURO-10-02-6",
            "A 21-year-old man developed weakness of both legs that spread to his whole body over 3 days. Examination: total ophthalmoplegia, bilateral facial palsy, paradoxical breathing, generalized motor power 2–3/5, areflexia and loss of vibration sense in all fingers and toes. What is the most appropriate management?",
            "IV immunoglobulin",
            ["Azathioprine", "Interferon beta-1a", "Cyclophosphamide", "IV methylprednisolone"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 373–374)",
            explain='''GBS รุนแรง (**paradoxical breathing = respiratory muscle weakness**, เดินไม่ได้, bulbar/ophthalmoplegia) → **IVIG** (หรือ plasmapheresis) พร้อมเตรียม ventilatory support
- Azathioprine และ cyclophosphamide เป็น immunosuppressant ระยะยาว ไม่ใช้ใน GBS
- Interferon beta ใช้ใน multiple sclerosis
- Methylprednisolone ไม่ได้ผลใน GBS''',
            pearl="GBS รุนแรง → IVIG/PLEX (ไม่ใช่ steroid)", topic="GBS IVIG",
            ref=[f"{D} หน้า 360, 373–374"], nl=["2.3.6-3(4)"]),
        mcq("NEURO-10-02-7",
            "A 35-year-old construction worker with a long history of heavy alcohol use and a BMI of 18 kg/m2 has had progressive weakness for 2 weeks. Examination: spider naevi, palmar erythema, ascites; alert but disoriented; motor power 3/5 in all limbs, areflexia and paresthesia of the hands and feet. What is the most likely diagnosis?",
            "Thiamine deficiency",
            ["Periodic paralysis", "Myasthenia gravis", "Alcoholic myopathy", "Cannabis intoxication"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 377–378)",
            explain='''ดื่มสุราเรื้อรัง ขาดอาหาร + **symmetrical sensorimotor polyneuropathy** (อ่อนแรง areflexia ชาปลายมือเท้า) + สับสน = **thiamine (B1) deficiency** — **dry beriberi** ± Wernicke (สไลด์เฉลย vitamin B1 deficiency)
- Periodic paralysis เป็นพัก ๆ และไม่มีชา
- MG ไม่มีชาหรือ areflexia
- Alcoholic myopathy เป็น proximal weakness ไม่มีชาและ reflex มักปกติ
- Cannabis intoxication ไม่ทำ neuropathy''',
            pearl="ติดสุรา + ขาดอาหาร + polyneuropathy = dry beriberi", topic="Beriberi",
            ref=[f"{D} หน้า 377–378"], nl=["2.3.6-3(9)", "B3.2.5(2)"]),
    ])

LECTURE = lecture("10", "Peripheral nerve", "Facial nerve palsy · Bell's · Ramsay Hunt · GBS · beriberi",
    objectives=[
        "แยก Bell's palsy, Ramsay Hunt และ UMN facial palsy พร้อมรักษาได้",
        "วินิจฉัย GBS จากประวัติ ตรวจร่างกาย และ CSF ได้",
        "บอกข้อบ่งชี้ IVIG/plasmapheresis และการเฝ้าระวังใน GBS ได้",
        "นึกถึง thiamine deficiency neuropathy ในคนดื่มสุรา/ขาดอาหารได้",
    ],
    sections=[S1, S2])
