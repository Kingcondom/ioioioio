from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Neuro"

# ---------------------------------------------------------------- 09-01 Spinal cord localization
F_CORD = fig("neuro-09-01-f1", "Spinal cord cross-section: tracts, lamination และ intrinsic vs extrinsic", '''<svg viewBox="0 0 740 400">
 <defs><marker id="neuro-09-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <text x="190" y="44" text-anchor="middle" class="t3">posterior (dorsal)</text>
 <text x="190" y="388" text-anchor="middle" class="t3">anterior (ventral) · lamination ใน→นอก = C T L S</text>
 <ellipse cx="190" cy="210" rx="165" ry="150" class="box"/>
 <rect x="112" y="110" width="52" height="190" rx="26" class="sunk"/>
 <rect x="216" y="110" width="52" height="190" rx="26" class="sunk"/>
 <rect x="150" y="188" width="80" height="34" rx="8" class="sunk"/>
 <circle cx="190" cy="205" r="6" class="ac"/>
 <circle cx="248" cy="205" r="9" class="c2"/>
 <text x="190" y="246" text-anchor="middle" class="t3">IML →</text>
 <path d="M168 76Q190 68 212 76L208 150Q190 146 172 150Z" class="c2soft"/>
 <text x="190" y="118" text-anchor="middle" class="tb">PC</text>
 <path d="M276 120Q330 140 346 196L278 196Z" class="c1soft"/>
 <text x="318" y="186" text-anchor="middle" class="tb">CST</text>
 <text x="286" y="160" class="t3">C</text>
 <text x="304" y="160" class="t3">T</text>
 <text x="320" y="160" class="t3">L</text>
 <text x="336" y="172" class="t3">S</text>
 <path d="M278 216L346 216Q336 276 292 310L278 300Z" class="misssoft"/>
 <text x="314" y="262" text-anchor="middle" class="tb">STT</text>
 <text x="400" y="30" class="tb">Tracts</text>
 <text x="400" y="54" class="t2"><tspan class="tb">PC</tspan> posterior column: proprioception, vibration</text>
 <text x="400" y="74" class="t2"><tspan class="tb">CST</tspan> lateral corticospinal: motor</text>
 <text x="400" y="94" class="t2"><tspan class="tb">STT</tspan> spinothalamic: pain, temperature</text>
 <text x="400" y="114" class="t2"><tspan class="tb">IML</tspan> คุม bowel/bladder (ใกล้ central canal)</text>
 <text x="400" y="138" class="t3">Lamination ใน CST/STT: C อยู่ใน (ใกล้กลาง) → S อยู่นอกสุด</text>
 <rect x="390" y="156" width="340" height="110" rx="10" class="c1soft"/>
 <text x="404" y="178" class="tb">Intrinsic (จากใน เช่น syrinx, tumor ใน cord)</text>
 <text x="404" y="200" class="t2">โดน C → T → L → S (descending)</text>
 <text x="404" y="220" class="t2"><tspan class="tb">Sacral sparing</tspan> · bowel/bladder เสียเร็ว</text>
 <text x="404" y="240" class="t2">ปวดแสบ funicular pain</text>
 <text x="404" y="258" class="t3">IML อยู่ใกล้ central canal จึงโดนก่อน</text>
 <rect x="390" y="276" width="340" height="110" rx="10" class="badsoft"/>
 <text x="404" y="298" class="tb">Extrinsic (กดจากนอก เช่น disc, tumor, abscess)</text>
 <text x="404" y="320" class="t2">โดน S → L → T → C (ascending)</text>
 <text x="404" y="340" class="t2"><tspan class="tb">ไม่มี sacral sparing</tspan> · bowel/bladder เสียช้า</text>
 <text x="404" y="360" class="t2">ปวดกระดูก/ปวดร้าวตามราก (radicular)</text>
 <text x="404" y="378" class="t3">ตัวอย่างในสไลด์: อาการชาไล่จากเท้าขึ้นเข่า</text>
</svg>''', "ซ้าย: ภาพตัดขวาง cord — fiber ของส่วน sacral อยู่ขอบนอกสุดของ CST/STT ส่วน cervical อยู่ด้านใน · ขวา: ใช้ลำดับนี้แยกรอยโรคที่เริ่มจากด้านในกับที่กดจากด้านนอก")

S1 = sec("neuro-09-01", "Spinal cord: localization, intrinsic vs extrinsic & cord compression",
    "Sensory level + UMN ใต้ระดับ + bowel/bladder · intrinsic: descending, sacral sparing, early autonomic · extrinsic: ascending, ไม่มี sacral sparing, radicular pain · อาการ cord ใหม่ → MRI spine ด่วน", minutes=9,
    source=f"{D} หน้า 11–12, 15, 325–332, 336–345", nl=["B3.1.1(3)", "2.2.38", "B3.2.3(3)"],
    md='''
### ลักษณะ spinal cord lesion

- อ่อนแรง **สองข้าง** (paraplegia/quadriplegia) · **sensory level** (cape-like/hanging ใน central cord) · **autonomic (bowel/bladder)** · ปวดหลัง
- **ใต้ระดับ lesion = UMN** (hyperreflexia, Babinski, spasticity) · **ที่ระดับ lesion = LMN** ของ segment นั้น (เช่น cervical cord: แขนอ่อนแรงแบบ LMN + ขาเกร็ง)
- ระยะแรก (spinal shock) เป็น flaccid areflexia ได้

### Intrinsic vs extrinsic

[[fig:neuro-09-01-f1]]

| | **Intrinsic cord** | **Extrinsic cord** |
|---|---|---|
| ลำดับอ่อนแรง/ชา | **Descending** (C→T→L→S) | **Ascending** (S→L→T→C) |
| Autonomic | **Early** bowel/bladder | **Late** |
| Pain | **Funicular** (แสบ เสียวซ่า) | **Bone pain, radicular pain** |
| Sensory | **Sacral sparing** (perianal sensation, rectal tone, great toe flexion ยังดี) | **No sacral sparing** |

- เหตุผล: ใน cord **fiber ของ sacral อยู่ขอบนอกสุด** ส่วน cervical อยู่ด้านใน · **IML column (คุม bowel/bladder) อยู่ใกล้ central canal** จึงโดนก่อนใน intrinsic lesion

### Spinal cord compression (เสริม)

- สาเหตุ: disc herniation, cervical spondylotic myelopathy, metastasis, **epidural abscess** (ไข้ ปวดหลัง), TB spine, trauma
- อาการ cord ใหม่/ลุกลาม → **MRI spine ทั้งแนวที่สงสัย (ด่วน)** — ไม่ใช่ plain film/CT brain/LP
- Metastatic cord compression: **dexamethasone + radiotherapy/surgery** · epidural abscess: drainage + ATB
- **Cervical myelopathy**: ปวดคอ มือทำงานไม่คล่อง เดินลำบาก + UMN ทั้งแขนและขา สมองปกติ → **MRI C-spine**

### Dermatome สำคัญ (เสริม — สไลด์เป็นภาพ)

C6 นิ้วโป้ง · C7 นิ้วกลาง · C8 นิ้วก้อย · **T4 หัวนม** · **T10 สะดือ** · L1 ขาหนีบ · L4 เข่า/ด้านในขา · L5 หลังเท้า · S1 ฝ่าเท้า/ส้นเท้าด้านข้าง

| Reflex | Root (เสริม) |
|---|---|
| Biceps | C5–6 |
| Triceps | C7 |
| Knee | L3–4 |
| Ankle | S1 |
''',
    figs=[F_CORD],
    pearls=[
        "Sensory level + UMN signs + bowel/bladder = spinal cord",
        "Intrinsic: descending, sacral sparing, early bladder",
        "Extrinsic: ascending, no sacral sparing, radicular/bone pain",
        "สะดือ = T10 · หัวนม = T4",
        "อาการ cord ใหม่ → MRI spine ด่วน",
    ],
    items=[
        mcq("NEURO-09-01-1",
            "A 28-year-old woman has needed urinary catheterization twice for urinary retention. She then developed bilateral leg weakness with numbness up to the level of the umbilicus. Examination: DTR 3+ in the legs and loss of anal sphincter tone. Where is the lesion?",
            "Thoracic spinal cord",
            ["Parasagittal (parafalcine) region", "Basal pons", "Lumbosacral nerve roots", "Conus medullaris"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 336–337)",
            explain='''อ่อนแรงขาสองข้าง + **sensory level ที่สะดือ (T10)** + **hyperreflexia (UMN)** + ปัสสาวะคั่งนำมาก่อน (early autonomic → intrinsic) = **thoracic spinal cord**
- Parasagittal lesion (เช่น meningioma) ทำให้ขาอ่อนแรงสองข้างได้แต่ไม่มี sensory level ที่ลำตัว
- Basal pons ทำให้ quadriparesis + CN palsy
- Lumbosacral root (cauda equina) เป็น LMN — reflex ลด
- Conus medullaris ทำ saddle anesthesia ไม่มีระดับชาที่สะดือ''',
            pearl="ระดับชาที่สะดือ + UMN = thoracic cord (T10)", topic="Cord localization",
            ref=[f"{D} หน้า 15, 327, 336–337"], nl=["B3.1.1(3)"]),
        mcq("NEURO-09-01-2",
            "A 30-year-old man has numbness from the shoulders down to the feet. Examination shows weakness of shoulder abduction with reduced biceps reflex, and spasticity with hyperreflexia in both legs. Where is the lesion?",
            "Cervical spinal cord",
            ["Cerebral cortex", "Cervical nerve roots", "Thoracic spinal cord", "Peripheral nerves"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 338–339)",
            explain='''ระดับชาจากไหล่ลงไป (C5) + **อ่อนแรงแบบ LMN ที่ระดับ** (deltoid C5) + **UMN ใต้ระดับ** (ขาเกร็ง reflex ไว) = **cervical cord** ระดับ C5
- Cerebral cortex ทำให้อ่อนแรงครึ่งซีก ไม่มี sensory level
- Cervical root ทำให้อ่อนแรง/ชาเฉพาะ root และ **ไม่มี** UMN ในขา
- Thoracic cord ไม่ทำให้แขนอ่อนแรง
- Peripheral neuropathy เป็น glove & stocking + reflex ลด''',
            pearl="LMN ที่แขน + UMN ที่ขา = cervical cord", topic="Cervical cord",
            ref=[f"{D} หน้า 15, 338–339"], nl=["B3.1.1(3)"]),
        mcq("NEURO-09-01-3",
            "A 54-year-old man has had difficulty walking for 9 months with mild neck pain. He has trouble standing up from a chair and his hand function is deteriorating. Examination: hypertonia and hyperreflexia in all four limbs, positive Babinski sign and clonus; cognition and cranial nerves are normal. What is the most appropriate investigation?",
            "MRI of the cervical spine",
            ["Plain radiograph of the cervical spine", "CT brain", "Nerve conduction study", "Referral for physiotherapy without imaging"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 340–341)",
            explain='''UMN ทั้งสี่แขนขา สมองและ CN ปกติ + ปวดคอ + มือใช้งานแย่ลง = **cervical myelopathy** (spondylosis) → **MRI C-spine** (สไลด์เฉลย cervical myelopathy)
- Plain film เห็นกระดูกเสื่อมแต่ไม่เห็น cord compression
- CT brain ไม่เกี่ยวเพราะ CN/cognition ปกติ
- NCS ใช้กับ peripheral neuropathy (LMN)
- Physiotherapy/chiropractic โดยไม่ตรวจอาจทำให้ cord บาดเจ็บมากขึ้น''',
            pearl="UMN 4 แขนขา + ปวดคอ + มือแย่ = cervical myelopathy → MRI C-spine", topic="Cervical myelopathy",
            ref=[f"{D} หน้า 340–341"], nl=["2.2.38", "B3.2.3(3)"]),
        mcq("NEURO-09-01-4",
            "A 24-year-old man has had low-grade fever and paraplegia for 4 days. BT 38.5°C. Examination: upper limb power 5/5, lower limb power 0/5, sensory loss below T4, bilateral extensor plantar responses. What is the most appropriate initial investigation?",
            "MRI of the thoracic spine",
            ["Lumbar puncture", "Plain radiograph of the thoracolumbar spine", "CT brain", "Nerve conduction study"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 342–343)",
            explain='''Paraplegia + **sensory level T4** + Babinski สองข้าง + ไข้ = acute myelopathy ระดับ thoracic (epidural abscess, TB spine, transverse myelitis) → **MRI T-spine ด่วน** เพื่อแยก compressive (ต้องผ่าตัด) กับ non-compressive
- LP ทำหลัง MRI (ถ้าไม่มี compression และสงสัย myelitis) — ก่อน MRI อาจทำให้ compression แย่ลง
- Plain film ไวต่ำ ไม่เห็น cord/abscess
- CT brain ไม่เกี่ยว (แขนปกติ มีระดับชาที่อก)
- NCS ใช้กับ peripheral nerve''',
            pearl="Paraplegia + sensory level → MRI spine ระดับนั้นทันที", topic="Acute myelopathy",
            ref=[f"{D} หน้า 342–343"], nl=["2.2.38"]),
        mcq("NEURO-09-01-5",
            "A 36-year-old man has had progressively worsening back pain for 4 days with tingling and burning rising from his feet to his knees bilaterally, and difficulty urinating. BT 36.3°C. Examination shows bilateral weakness of hip flexion and decreased anal sphincter tone. What is the best next step?",
            "MRI of the spine",
            ["CT brain", "Emergency surgery before imaging", "Lumbar puncture", "Pulmonary function tests"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 344–345)",
            explain='''ปวดหลัง + อาการชา **ไล่จากเท้าขึ้น (ascending)** + ปัสสาวะลำบาก + anal tone ลด = **extrinsic cord/cauda equina compression** (สไลด์เฉลย extrinsic cord lesion, L-spine level) → **MRI spine ด่วน** ก่อนวางแผนผ่าตัด
- CT brain ไม่เกี่ยว
- ผ่าตัดโดยไม่รู้ระดับและสาเหตุไม่ได้ — ต้องทำ MRI ก่อน
- LP ไม่ใช่ขั้นแรกเมื่อสงสัย compression (GBS ก็ ascending แต่ไม่มีปวดหลังเด่น + sphincter เสียเร็ว)
- PFT ใช้ติดตาม GBS ไม่ใช่วินิจฉัย''',
            pearl="ปวดหลัง + ascending + sphincter → MRI spine (compression)", topic="Extrinsic lesion",
            ref=[f"{D} หน้า 326, 328, 344–345"], nl=["2.2.38", "B3.2.3(3)"]),
    ])

# ---------------------------------------------------------------- 09-02 Transverse myelitis
S2 = sec("neuro-09-02", "Transverse myelitis",
    "Inflammatory myelopathy (idiopathic, post-infection/vaccine, MS, SLE) · acute spinal shock → UMN + sensory level + bladder · MRI brain & spine + LP pleocytosis · high-dose IV steroid → PLEX", minutes=6,
    source=f"{D} หน้า 333–335, 346–347", nl=["B3.2.2(3)", "2.3.6(1)"],
    md='''
### สาเหตุ

- **Idiopathic (พบบ่อยสุด)**
- **Post-infectious**, **post-vaccination**
- **CNS demyelinating disorder** (เช่น **multiple sclerosis**, NMOSD — เสริม)
- **Autoimmune** (เช่น **SLE**)

### อาการ

- **Acute/subacute onset** (ชั่วโมง–วัน)
- **ระยะแรก: spinal shock** — flaccid, areflexic paralysis (อาจดูคล้าย GBS)
- ต่อมา: **อ่อนแรงและชาสองข้างใต้ระดับ lesion** (sensory level), **↑DTR, spasticity**
- **Autonomic dysfunction, bowel/bladder involvement** (ปัสสาวะคั่ง)

### Investigation

- **MRI brain & spine** — เห็น lesion ใน spinal cord · **MRI brain เพื่อ R/O MS**
- **LP: pleocytosis (↑WBC), ↑IgG index**

### Treatment

- **High-dose IV corticosteroid (1st line)** (methylprednisolone 1 g/day × 3–5 วัน — เสริม)
- **Plasma exchange (2nd line)**

### ATM vs GBS (สำคัญในข้อสอบ)

| | Acute transverse myelitis | GBS |
|---|---|---|
| Sensory | **Sensory level** | Glove & stocking |
| Sphincter | **เสียเร็ว** | ไม่ค่อยเสีย |
| Plantar | **Extensor** (อาจช้าในระยะ shock) | Flexor |
| CSF | Pleocytosis | Albuminocytologic dissociation |
''',
    pearls=[
        "TM: อ่อนแรงสองขา + sensory level + ปัสสาวะคั่ง หลังติดเชื้อ/วัคซีน",
        "ระยะแรก spinal shock (flaccid areflexia) อาจหลอกเป็น GBS — ดู sensory level และ sphincter",
        "MRI brain + spine (R/O MS) + LP pleocytosis",
        "Tx: high-dose IV steroid → PLEX",
    ],
    items=[
        mcq("NEURO-09-02-1",
            "A 30-year-old man has difficulty urinating and weakness of both legs that started after 5 days of fever and rhinorrhea. Vital signs are stable. Examination: distal leg power 2/5, absent ankle and knee reflexes, bilateral extensor plantar responses, numbness of both legs up to the umbilicus, and lax anal sphincter tone. What is the most likely diagnosis?",
            "Acute transverse myelitis",
            ["Acute poliomyelitis", "Guillain-Barré syndrome", "Myasthenia gravis", "Acute polymyositis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 346–347)",
            explain='''หลังติดเชื้อ + **sensory level ที่สะดือ** + **sphincter เสีย** + **Babinski บวก** แม้ reflex หายในระยะแรก (**spinal shock**) = **acute transverse myelitis**
- Poliomyelitis เป็น pure motor ไม่มีชาหรือ sensory level
- GBS ทำ areflexia ได้แต่ชาแบบ glove & stocking ไม่มี sensory level และ plantar flexor sphincter มักปกติ
- MG ไม่มีชาและ sphincter ปกติ
- Polymyositis เป็น proximal weakness ไม่มีชา''',
            pearl="Areflexia + sensory level + sphincter + Babinski = TM (spinal shock)", topic="TM vs GBS",
            ref=[f"{D} หน้า 334, 346–347"], nl=["B3.2.2(3)"]),
        mcq("NEURO-09-02-2",
            "A 26-year-old woman develops leg weakness, a T8 sensory level and urinary retention over 3 days, 2 weeks after an influenza vaccination. MRI shows a T2-hyperintense lesion in the thoracic cord without compression; CSF shows 30 lymphocytes/mm3 with an elevated IgG index. What is the most appropriate first-line treatment?",
            "High-dose IV methylprednisolone",
            ["IV acyclovir", "Plasma exchange as first-line", "Emergency decompressive laminectomy", "Oral prednisolone 10 mg/day"],
            explain='''Transverse myelitis หลังวัคซีน ยืนยันด้วย MRI (ไม่มี compression) + CSF pleocytosis → **high-dose IV corticosteroid (1st line)** ตามสไลด์
- Acyclovir สำหรับ viral (HSV/VZV) myelitis ไม่ใช่ภาพนี้
- Plasma exchange เป็น **2nd line** เมื่อไม่ตอบสนองต่อ steroid
- Laminectomy สำหรับ compressive lesion เท่านั้น
- Prednisolone ขนาดต่ำไม่เพียงพอ''',
            pearl="TM → IV methylprednisolone ก่อน แล้วค่อย PLEX", topic="TM treatment",
            ref=[f"{D} หน้า 333–335"], nl=["B3.2.2(3)"]),
        mcq("NEURO-09-02-3",
            "A 29-year-old woman has acute transverse myelitis at T6. Eighteen months ago she had an episode of painful monocular visual loss that recovered. Which investigation is most important to look for an underlying cause?",
            "MRI brain",
            ["Nerve conduction study", "Serum creatine kinase", "Edrophonium test", "Chest radiograph"],
            explain='''TM + ประวัติ **optic neuritis** → ต้องหา **CNS demyelinating disease (MS/NMOSD)** → **MRI brain** (สไลด์: ทำ MRI brain ด้วยเพื่อ R/O multiple sclerosis) ± anti-AQP4 (เสริม)
- NCS ใช้กับ peripheral nerve
- CK ใช้กับ myopathy
- Edrophonium test ใช้กับ MG
- CXR ไม่ใช่การตรวจหลักในการหา demyelination (อาจใช้หา sarcoidosis/TB ภายหลัง)''',
            pearl="TM → MRI brain หา MS", topic="TM workup",
            ref=[f"{D} หน้า 333–334"], nl=["B3.2.2(3)"]),
    ])

LECTURE = lecture("09", "Spinal cord", "Localization · intrinsic vs extrinsic · cord compression · transverse myelitis",
    objectives=[
        "บอกระดับ cord lesion จาก sensory level และ UMN/LMN signs ได้",
        "แยก intrinsic กับ extrinsic cord lesion ได้",
        "สั่ง MRI spine อย่างเหมาะสมในผู้ป่วยสงสัย cord compression ได้",
        "วินิจฉัยและรักษา transverse myelitis และแยกจาก GBS ได้",
    ],
    sections=[S1, S2])
