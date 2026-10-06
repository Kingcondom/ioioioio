from lib import lecture, sec, mcq, fig

D = "สไลด์ Update ข้อสอบ 2025"
SRC = "NL2 2025 (update)"

def R(*p):
    return [f"{D} หน้า " + ", ".join(str(x) for x in p)]

# ---------------------------------------------------------------- 08-01 Seizure, coma, stroke
F_SE = fig("exam25-08-01-f1", "Status epilepticus ตามระยะเวลา (แผนภูมิไทยในสไลด์)", '''<svg viewBox="0 0 720 250">
 <defs><marker id="exam25-08-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <path d="M20 40H700" class="ln" marker-end="url(#exam25-08-01-a)"/>
 <text x="20" y="28" class="t3">0 นาที</text>
 <text x="180" y="28" class="t3">5</text>
 <text x="360" y="28" class="t3">30</text>
 <text x="540" y="28" class="t3">60</text>
 <text x="660" y="28" class="t3">เวลา</text>
 <rect x="20" y="54" width="160" height="186" rx="10" class="oksoft"/>
 <text x="100" y="78" text-anchor="middle" class="tb">Initial</text>
 <text x="100" y="102" text-anchor="middle" class="t2">ABC, O2</text>
 <text x="100" y="122" text-anchor="middle" class="t2">DTX แก้น้ำตาลต่ำ</text>
 <text x="100" y="142" text-anchor="middle" class="t2">thiamine ก่อน glucose</text>
 <rect x="190" y="54" width="170" height="186" rx="10" class="acsoft"/>
 <text x="275" y="78" text-anchor="middle" class="tb">Early (5–10 นาที)</text>
 <text x="275" y="102" text-anchor="middle" class="ta">Benzodiazepine</text>
 <text x="275" y="124" text-anchor="middle" class="t2">IV diazepam</text>
 <text x="275" y="144" text-anchor="middle" class="t2">IM midazolam</text>
 <text x="275" y="164" text-anchor="middle" class="t2">IV lorazepam</text>
 <text x="275" y="196" text-anchor="middle" class="t3">ให้ซ้ำได้ 1 ครั้ง</text>
 <rect x="370" y="54" width="170" height="186" rx="10" class="misssoft"/>
 <text x="455" y="78" text-anchor="middle" class="tb">Established</text>
 <text x="455" y="96" text-anchor="middle" class="t3">(10–30 นาที)</text>
 <text x="455" y="120" text-anchor="middle" class="t2">IV phenytoin</text>
 <text x="455" y="140" text-anchor="middle" class="t2">valproate</text>
 <text x="455" y="160" text-anchor="middle" class="t2">levetiracetam</text>
 <text x="455" y="180" text-anchor="middle" class="t2">phenobarbital</text>
 <rect x="550" y="54" width="160" height="186" rx="10" class="badsoft"/>
 <text x="630" y="78" text-anchor="middle" class="tb">Refractory</text>
 <text x="630" y="96" text-anchor="middle" class="t3">(30–60 นาที)</text>
 <text x="630" y="120" text-anchor="middle" class="t2">ICU, intubate</text>
 <text x="630" y="140" text-anchor="middle" class="t2">anesthetic drip:</text>
 <text x="630" y="160" text-anchor="middle" class="t2">midazolam, propofol</text>
 <text x="630" y="180" text-anchor="middle" class="t2">+ continuous EEG</text>
</svg>''', "ชักครบ 5 นาที = status epilepticus ให้ benzodiazepine ก่อนเสมอ ถ้ายังชักจึงขยับไปยากันชักตัวที่สองและยาสลบตามลำดับ")

S1 = sec("exam25-08-01", "Status epilepticus, coma & stroke",
    "SE (≥ 5 นาที) → benzodiazepine ก่อน · pinpoint pupil + decerebrate + HT = pontine hemorrhage · GCS ≤ 8 → intubate", minutes=5,
    source=f"{D} หน้า 2–4, 22–25", nl=["2.2.37", "2.3.6(3)", "2.2.39"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Status epilepticus (สไลด์)** = ชัก **≥ 5 นาที** หรือชัก **≥ 2 ครั้งโดยไม่ฟื้นระหว่างครั้ง**

[[fig:exam25-08-01-f1]]

**ตำแหน่งเลือดออกในสมองจาก HT — ดูจากตา**

| ตำแหน่ง | ลักษณะเด่น |
|---|---|
| **Pons** | **pinpoint pupils** (ยังมี light reflex), **quadriplegia**, **decerebrate (extensor) posturing**, doll's eye หาย, coma เร็ว |
| Putamen | hemiparesis ตรงข้าม + ตามองไปด้านรอยโรค |
| Thalamus | ตามองลงล่าง (upgaze palsy), รูม่านตาเล็กไม่ตอบสนอง, ชาครึ่งซีก |
| Cerebellum | เวียน อาเจียน เดินเซ ไม่มีอัมพาต (ต้องผ่าตัดถ้า > 3 cm) |

- Pinpoint pupil แยกจาก **opioid overdose**: opioid จะหายใจช้า และไม่มี decerebrate/BP สูง

**Airway ในผู้ป่วยหมดสติ**: **GCS ≤ 8 → ใส่ท่อช่วยหายใจ (ETT) ก่อน** ทุกอย่าง (A ก่อน B C) · หลังจากนั้นค่อยทำ CT, คุม BP, ตัดสินใจเรื่อง thrombolysis
''',
    figs=[F_SE],
    pearls=[
        "SE = ชัก ≥ 5 นาที → benzodiazepine (IV diazepam / IM midazolam / IV lorazepam)",
        "Pinpoint pupil + quadriplegia + decerebrate + HT = pontine hemorrhage",
        "GCS ≤ 8 → intubate ก่อน (airway first)",
    ],
    items=[
        mcq("EXAM25-08-01-1",
            "A 20-year-old man with epilepsy who has stopped taking his phenytoin presents with an ongoing generalized tonic-clonic seizure that has lasted 10 minutes. He is unresponsive. Airway, breathing and capillary glucose have been addressed and intravenous access is available. What is the most appropriate immediate treatment?",
            "Intravenous diazepam",
            ["Intravenous phenytoin", "Intravenous levetiracetam", "Intravenous phenobarbital", "Oral lorazepam"],
            kind="old", src=SRC,
            explain='''ชักต่อเนื่อง > 5 นาที = **early status epilepticus** → หลังดู ABC และแก้น้ำตาลต่ำ ให้ **benzodiazepine เป็นยาตัวแรก** — สไลด์เฉลย **IV diazepam** (แผนภูมิไทยให้ IV diazepam, IM midazolam หรือ IV lorazepam)
- IV phenytoin, levetiracetam และ phenobarbital เป็นยาระยะ **established SE** ให้หลัง benzodiazepine ไม่ได้ผล
- Oral lorazepam กินไม่ได้ในคนที่กำลังชัก
(สไลด์มี "Lorazepam" เป็นตัวเลือกด้วย ซึ่ง IV lorazepam ก็ถูกตามแนวทางสากล จึงเปลี่ยนเป็น oral lorazepam เพื่อให้มีคำตอบที่ดีที่สุดเพียงข้อเดียว — ถ้าเจอทั้งสองตัวในสนามจริง ให้ยึด IV diazepam ตามแนวทางไทย)''',
            pearl="SE → benzodiazepine ก่อน (IV diazepam)", topic="Status epilepticus",
            ref=R(2, 3, 4), nl=["2.2.37"]),
        mcq("EXAM25-08-01-2",
            "A 40-year-old man with well-controlled focal seizures (on phenytoin for 5 years) and long-standing untreated hypertension is found unconscious. Temperature 37.5 °C, BP 180/100 mmHg, pulse 110/min. He has pinpoint pupils, absent oculocephalic reflexes and repeated extensor posturing of all four limbs. What is the most likely diagnosis?",
            "Pontine hemorrhage",
            ["Opioid overdose", "Phenytoin toxicity", "Epidural hematoma", "Thalamic infarction"],
            kind="old", src=SRC,
            explain='''**Pinpoint pupils + doll's eye หาย (brainstem) + decerebrate posturing ทั้งสี่แขนขา + BP สูง** = **pontine hemorrhage** (risk: HT เรื้อรัง — สไลด์สรุปไว้ เติมในโจทย์ให้ชัด)
- Opioid overdose ให้ pinpoint pupil ได้ แต่จะหายใจช้า BP ไม่สูง ไม่มี decerebrate posturing และ doll's eye มักยังอยู่
- Phenytoin toxicity ให้ nystagmus, ataxia, ซึม ไม่ใช่ pinpoint pupil + posturing
- Epidural hematoma มีประวัติ trauma, lucid interval และรูม่านตา**ขยาย**ข้างเดียว
- Thalamic infarct ให้ upgaze palsy ชาครึ่งซีก ไม่ทำ quadriplegia + decerebrate''',
            pearl="Pinpoint + decerebrate + HT = pontine hemorrhage", topic="Pontine hemorrhage",
            ref=R(22, 23), nl=["2.3.6(3)", "2.2.39"]),
        mcq("EXAM25-08-01-3",
            "A 40-year-old previously healthy woman presents with sudden loss of consciousness. BP 200/110 mmHg. There is a right ventricular heave and a grade 3/6 diastolic rumbling murmur at the apex. GCS is E4V1M1 with bilateral lateral gaze palsy and quadriparesis. What is the most urgent intervention?",
            "Endotracheal intubation",
            ["Intravenous rt-PA", "Intravenous nicardipine", "Aspirin", "Low-molecular-weight heparin"],
            kind="old", src=SRC,
            explain='''ผู้ป่วย stroke (MS + AF เสี่ยง cardioembolic ไปยัง basilar artery → gaze palsy + quadriparesis) ที่ **GCS 6 (≤ 8)** → สิ่งที่เร่งด่วนที่สุดคือ **protect airway ด้วย ETT** (A มาก่อนเสมอ)
- IV rt-PA ต้องทำ CT ก่อนเพื่อตัดเลือดออก และ BP 200/110 ต้องลดให้ < 185/110 ก่อน
- IV nicardipine ใช้ลด BP แต่เป็นขั้นตอนหลัง airway
- Aspirin ต้องรอผล CT ว่าไม่ใช่เลือดออก และผู้ป่วยกลืนไม่ได้
- LMWH ไม่ใช่การรักษาระยะเฉียบพลันของ stroke''',
            pearl="GCS ≤ 8 → intubate ก่อนทุกอย่าง", topic="Airway in stroke",
            ref=R(24, 25), nl=["2.2.39"]),
    ])

# ---------------------------------------------------------------- 08-02 PD & dementia
F_DEM = fig("exam25-08-02-f1", "แยกชนิดของ dementia (ตามแผนภูมิสไลด์)", '''<svg viewBox="0 0 720 300">
 <defs><marker id="exam25-08-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="220" y="10" width="280" height="38" rx="10" class="acsoft"/>
 <text x="360" y="34" text-anchor="middle" class="tb">สงสัย dementia → neuro exam</text>
 <path d="M280 48L120 82" class="ln" marker-end="url(#exam25-08-02-a)"/>
 <path d="M360 48V82" class="ln" marker-end="url(#exam25-08-02-a)"/>
 <path d="M440 48L600 82" class="ln" marker-end="url(#exam25-08-02-a)"/>
 <rect x="20" y="84" width="200" height="34" rx="8" class="oksoft"/>
 <text x="120" y="106" text-anchor="middle" class="tb">ปกติ (WNL)</text>
 <rect x="260" y="84" width="200" height="34" rx="8" class="c1soft"/>
 <text x="360" y="106" text-anchor="middle" class="tb">Parkinsonism</text>
 <rect x="500" y="84" width="200" height="34" rx="8" class="c2soft"/>
 <text x="600" y="106" text-anchor="middle" class="tb">Focal neuro deficit</text>
 <path d="M80 118L70 150" class="ln" marker-end="url(#exam25-08-02-a)"/>
 <path d="M160 118L170 150" class="ln" marker-end="url(#exam25-08-02-a)"/>
 <rect x="10" y="152" width="120" height="60" rx="8" class="box"/>
 <text x="70" y="174" text-anchor="middle" class="t3">เด่นความจำ</text>
 <text x="70" y="198" text-anchor="middle" class="ta">Alzheimer</text>
 <rect x="140" y="152" width="110" height="60" rx="8" class="box"/>
 <text x="195" y="174" text-anchor="middle" class="t3">พฤติกรรม/ภาษา</text>
 <text x="195" y="198" text-anchor="middle" class="ta">FTD</text>
 <rect x="260" y="152" width="200" height="34" rx="8" class="box"/>
 <text x="360" y="174" text-anchor="middle" class="t3">Parkinsonism นำ dementia &lt; 1 ปี?</text>
 <path d="M320 186L310 214" class="ln" marker-end="url(#exam25-08-02-a)"/>
 <path d="M400 186L410 214" class="ln" marker-end="url(#exam25-08-02-a)"/>
 <rect x="260" y="216" width="100" height="72" rx="8" class="box"/>
 <text x="310" y="238" text-anchor="middle" class="t3">ใช่ (หรือพร้อมกัน)</text>
 <text x="310" y="262" text-anchor="middle" class="ta">Lewy body</text>
 <rect x="370" y="216" width="100" height="72" rx="8" class="box"/>
 <text x="420" y="238" text-anchor="middle" class="t3">ไม่ (PD นาน)</text>
 <text x="420" y="262" text-anchor="middle" class="ta">PD dementia</text>
 <rect x="500" y="152" width="200" height="34" rx="8" class="box"/>
 <text x="600" y="174" text-anchor="middle" class="t3">Imaging อธิบายอาการได้?</text>
 <path d="M560 186L550 214" class="ln" marker-end="url(#exam25-08-02-a)"/>
 <path d="M640 186L650 214" class="ln" marker-end="url(#exam25-08-02-a)"/>
 <rect x="490" y="216" width="105" height="72" rx="8" class="box"/>
 <text x="542" y="238" text-anchor="middle" class="t3">ใช่</text>
 <text x="542" y="262" text-anchor="middle" class="ta">Vascular</text>
 <rect x="605" y="216" width="105" height="72" rx="8" class="box"/>
 <text x="657" y="238" text-anchor="middle" class="t3">ไม่</text>
 <text x="657" y="256" text-anchor="middle" class="t2">dementia อื่น</text>
 <text x="657" y="274" text-anchor="middle" class="t3">ร่วม CVD</text>
</svg>''', "ตรวจระบบประสาทแบ่งเป็นสามทาง ทางที่ตรวจปกติให้ดูว่าเด่นความจำ (Alzheimer) หรือเด่นพฤติกรรม/ภาษา (FTD)")

S2 = sec("exam25-08-02", "Parkinson disease & dementia",
    "PD = dopaminergic neuron ใน SNpc ตาย · ความจำเสื่อมค่อยเป็น + neuro exam ปกติ + กระวนกระวายตอนเย็น = Alzheimer + BPSD", minutes=5,
    source=f"{D} หน้า 14–19", nl=["B3.2.8-3(2)", "2.3.6-3(1)", "2.3.5-3(5)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Parkinson disease (สไลด์)**
1. Parkinsonism: **bradykinesia (ต้องมี)** + อย่างน้อย 1 ใน resting tremor / rigidity (+ postural instability)
2. ตัดสาเหตุ secondary (drug-induced, vascular parkinsonism)
3. Supportive: เริ่มข้างเดียว/ไม่สมมาตร, resting tremor, ค่อย ๆ แย่ลง, **ตอบสนองต่อ levodopa**
- พยาธิกำเนิด: **dopaminergic neuron ใน substantia nigra pars compacta เสื่อม** (Lewy body, α-synuclein)

| พยาธิกำเนิด | โรค |
|---|---|
| β-amyloid plaque + neurofibrillary tangle | Alzheimer |
| Anti-AChR ที่ NMJ | Myasthenia gravis |
| Demyelination ใน CNS | Multiple sclerosis |
| GABAergic neuron ใน striatum (caudate) เสื่อม | Huntington |

**Dementia**

[[fig:exam25-08-02-f1]]

- **Alzheimer + BPSD**: ความจำระยะสั้นเสียแบบค่อยเป็นค่อยไป, neuro exam ปกติ, **sundowning** (สับสน กระวนกระวายตอนเย็น/กลางคืน)
- **Delirium** ต่างกันที่ **เฉียบพลัน (ชั่วโมง–วัน)** อาการขึ้นลงในวันเดียว ระดับความรู้สึกตัวเปลี่ยน มีสาเหตุกระตุ้น
''',
    figs=[F_DEM],
    pearls=[
        "PD: bradykinesia ต้องมี + tremor หรือ rigidity · SNpc dopaminergic neuron",
        "Dementia neuro exam ปกติ เด่นความจำ = Alzheimer",
        "Sundowning = BPSD ใน dementia ไม่ใช่ delirium ถ้าค่อยเป็นหลายเดือน",
        "Parkinsonism นำ/พร้อม dementia < 1 ปี = Lewy body",
    ],
    items=[
        mcq("EXAM25-08-02-1",
            "An elderly man presents with classic features of Parkinson disease, including bradykinesia, resting tremor, cogwheel rigidity and postural instability. Which of the following best describes the pathogenesis of this condition?",
            "Degeneration of dopaminergic neurons in the substantia nigra pars compacta",
            ["Accumulation of β-amyloid plaques and neurofibrillary tangles in the cerebral cortex",
             "Autoantibodies against the acetylcholine receptor at the neuromuscular junction",
             "Demyelination of neurons in the central nervous system",
             "Degeneration of GABAergic neurons in the striatum"],
            kind="old", src=SRC,
            explain='''Parkinson disease เกิดจาก **dopaminergic neuron ใน substantia nigra pars compacta เสื่อม** (มี Lewy body/α-synuclein) → dopamine ใน striatum ลดลง → bradykinesia, rigidity, tremor
- β-amyloid plaque และ neurofibrillary tangle = Alzheimer
- Anti-AChR antibody = myasthenia gravis
- CNS demyelination = multiple sclerosis
- GABAergic neuron ใน striatum เสื่อม = Huntington disease (chorea)''',
            pearl="PD = SNpc dopaminergic neuron เสื่อม", topic="Parkinson disease",
            ref=R(14, 15, 16), nl=["B3.2.8-3(2)"]),
        mcq("EXAM25-08-02-2",
            "A 70-year-old woman presents with progressive forgetfulness, daytime inattention and nocturnal confusion over 3 months. Cognitive testing shows deficits in attention and short-term recall. She has no focal neurological signs or parkinsonism but becomes increasingly agitated in the evenings. Laboratory screening is unremarkable. What is the most likely diagnosis?",
            "Alzheimer disease",
            ["Delirium", "Lewy body dementia", "Vascular dementia", "Age-related forgetfulness"],
            kind="old", src=SRC,
            explain='''ความจำระยะสั้นเสื่อม **ค่อยเป็นค่อยไป 3 เดือน** + neuro exam ปกติ ไม่มี parkinsonism + **กระวนกระวาย/สับสนตอนเย็น (sundowning = BPSD)** = **Alzheimer disease with BPSD** (สไลด์เฉลย)
- Delirium เป็นเฉียบพลันเป็นชั่วโมง–วัน ระดับความรู้สึกตัวขึ้นลง และมีสาเหตุ (ติดเชื้อ ยา) — ไม่ใช่ 3 เดือนที่ค่อย ๆ แย่ลง (เติม "lab ปกติ" ในโจทย์เพื่อช่วยตัด)
- Lewy body dementia ต้องมี parkinsonism, visual hallucination, fluctuation เด่น
- Vascular dementia มี focal deficit หรือ stepwise decline และ imaging พบ infarct
- Age-related forgetfulness ไม่กระทบการใช้ชีวิตและไม่มี BPSD''',
            pearl="ความจำเสื่อมค่อยเป็น + neuro ปกติ + sundowning = Alzheimer + BPSD", topic="Alzheimer disease",
            ref=R(17, 18, 19), nl=["2.3.6-3(1)", "2.3.5-3(5)"]),
    ])

# ---------------------------------------------------------------- 08-03 Bell & MG
S3 = sec("exam25-08-03", "Bell palsy & myasthenia gravis",
    "LMN facial palsy (รวมหน้าผาก) ไม่มีผื่น/หูปกติ = Bell → prednisolone · อ่อนแรงเมื่อใช้งาน + diplopia ตอนเย็น = MG", minutes=4,
    source=f"{D} หน้า 26–29", nl=["2.3.6(2)", "2.3.6-3(7)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Facial palsy — UMN vs LMN**

| | UMN (stroke) | **LMN (Bell)** |
|---|---|---|
| หน้าผาก | **รอด** (bilateral cortical supply) | **ย่นไม่ได้** · ปิดตาไม่สนิท |
| ร่วม | แขนขาอ่อนแรงด้านเดียวกัน | อาจรับรสเสีย ได้ยินเสียงดัง |

- **Bell palsy** = idiopathic LMN palsy ข้างเดียว → **prednisolone ภายใน 72 ชม.** + ป้องกันกระจกตา (น้ำตาเทียม ปิดตา)
- **Ramsay Hunt** (VZV): มี **ตุ่มน้ำที่หู/ใบหู** หูอื้อ เวียน → prednisolone + **acyclovir**

**Myasthenia gravis (สไลด์)**
- **Fatigable weakness**: แย่ลงเมื่อใช้งาน ดีขึ้นเมื่อพัก · **ptosis, diplopia** (ตอนเย็นมากขึ้น) · เคี้ยว/กลืนลำบาก · **reflex ปกติ** · ไม่มีชา
- ตรวจ: **repetitive nerve stimulation (decremental), single-fiber EMG**, anti-AChR Ab · CT chest หา thymoma (เสริม)
- รักษา: **pyridostigmine**

| แยกจาก | จุดต่าง |
|---|---|
| Lambert–Eaton | proximal ขา **ดีขึ้นเมื่อใช้งาน**, reflex ลดลง, SCLC |
| GBS | ascending, **areflexia** |
| MS | อาการหลายตำแหน่งหลายเวลา, UMN sign |
| ALS | UMN + LMN, fasciculation, ไม่มีอาการตา |
''',
    pearls=[
        "LMN facial palsy (หน้าผากด้วย) ไม่มีผื่นที่หู = Bell → prednisolone",
        "มีตุ่มน้ำที่หู = Ramsay Hunt → เพิ่ม acyclovir",
        "อ่อนแรงเมื่อใช้งาน + ptosis/diplopia + reflex ปกติ = MG → pyridostigmine",
    ],
    items=[
        mcq("EXAM25-08-03-1",
            "A 25-year-old man develops acute left facial weakness involving both the upper face (unable to close the eye or wrinkle the forehead) and the lower face (drooping mouth). Vital signs are normal. Ear examination is unremarkable, and there is no rash or hearing loss. What is the appropriate treatment?",
            "Oral prednisolone",
            ["Acyclovir alone", "Reassurance only", "Carbamazepine", "Gabapentin"],
            kind="old", src=SRC,
            explain='''อัมพาตใบหน้าครึ่งซีก **ทั้งบนและล่าง (LMN)** เฉียบพลัน ไม่มีผื่น/ตุ่มน้ำที่หู ไม่มีหูอื้อ = **Bell palsy** → **prednisolone** ภายใน 72 ชม. (เพิ่มโอกาสหายสมบูรณ์) + ดูแลกระจกตา
- Acyclovir เดี่ยว ๆ ไม่ได้ผล ใช้ร่วมกับ steroid เมื่อสงสัย Ramsay Hunt (มีตุ่มน้ำที่หู)
- Reassurance อย่างเดียวพลาดประโยชน์ของ steroid (แม้ส่วนใหญ่จะหายเองได้)
- Carbamazepine ใช้กับ trigeminal neuralgia
- Gabapentin ใช้กับ neuropathic pain''',
            pearl="Bell palsy → prednisolone ภายใน 72 ชม.", topic="Bell palsy",
            ref=R(26, 27), nl=["2.3.6(2)"]),
        mcq("EXAM25-08-03-2",
            "A 30-year-old woman presents with fluctuating muscle weakness that worsens with activity and improves with rest. She has difficulty chewing and experiences diplopia in the evenings. Reflexes and sensation are normal. What is the most likely diagnosis?",
            "Myasthenia gravis",
            ["Lambert-Eaton syndrome", "Guillain-Barré syndrome", "Multiple sclerosis", "Amyotrophic lateral sclerosis"],
            kind="old", src=SRC,
            explain='''**Fatigable weakness** (แย่ลงเมื่อใช้งาน ดีขึ้นเมื่อพัก) + กล้ามเนื้อเคี้ยว + **diplopia ตอนเย็น** + reflex ปกติ = **myasthenia gravis** (anti-AChR) → ตรวจ repetitive stimulation/SFEMG รักษาด้วย pyridostigmine
- Lambert–Eaton อ่อนแรง proximal ขา **ดีขึ้นหลังออกแรงสั้น ๆ** reflex ลดลง มักร่วมกับ SCLC
- GBS อ่อนแรงขึ้นจากขา **reflex หาย** ไม่ fluctuate
- MS มีอาการหลายระบบ ชา ตามัว UMN sign
- ALS มี fasciculation, UMN + LMN และไม่ทำให้ diplopia''',
            pearl="Fatigable + ptosis/diplopia + reflex ปกติ = MG", topic="Myasthenia gravis",
            ref=R(28, 29), nl=["2.3.6-3(7)"]),
    ])

# ---------------------------------------------------------------- 08-04 Headache
S4 = sec("exam25-08-04", "Headache & facial pain",
    "บีบรัดสองข้าง ไม่มี photophobia = TTH · ข้างเดียวรอบตา + น้ำตา + เป็นช่วง ๆ = cluster · migraine prophylaxis = propranolol · ปวดช็อตเป็นวินาทีใน V2/V3 = TN", minutes=5,
    source=f"{D} หน้า 32–39", nl=["2.3.6(8)", "2.3.6(4)", "2.3.6-3(12)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

| | Tension-type | Migraine | Cluster | Trigeminal neuralgia |
|---|---|---|---|---|
| ตำแหน่ง | **สองข้าง** หน้าผาก ขมับ รัดเป็นแถบ | **ข้างเดียว** ตุบ ๆ | **ข้างเดียว รอบตา** | ตามแขนง CN V (V2/V3) |
| ลักษณะ | ตื้อ ๆ บีบรัด | throbbing | แสบ แทง รุนแรงมาก | **ช็อตไฟฟ้า** |
| ระยะเวลา | 30 นาที–7 วัน | **4–72 ชม.** | 15–180 นาที วันละหลายครั้ง **เป็นช่วง (cluster period)** | **วินาที** |
| ร่วม | **ไม่มี** photophobia/N/V | **photophobia, phonophobia, N/V** ± aura | **autonomic ข้างเดียวกัน**: น้ำตา น้ำมูก ตาแดง Horner | trigger: เคี้ยว พูด แปรงฟัน สัมผัส |
| Acute Tx | **paracetamol, NSAID** | NSAID, **triptan**, ergotamine | **100% O2**, triptan | — |
| Prevention | **amitriptyline** (chronic) | **propranolol, topiramate, amitriptyline** | **verapamil** | **carbamazepine** (ยาหลัก) |

> Migraine prophylaxis: สไลด์เลือก **propranolol** · topiramate ก็ first-line แต่ **ทำให้พิการแต่กำเนิด** และลดฤทธิ์ยาคุม — หญิงที่วางแผนตั้งครรภ์ควรเลี่ยง (เสริม)
''',
    pearls=[
        "ปวดสองข้างแบบบีบรัด ไม่มี photophobia/N/V = tension-type",
        "ปวดรอบตาข้างเดียว + น้ำตาน้ำมูก + เป็นช่วง ๆ = cluster → 100% O2, verapamil",
        "Migraine prophylaxis: propranolol (topiramate, amitriptyline)",
        "ปวดช็อตไฟฟ้าเป็นวินาทีใน V2/V3 = trigeminal neuralgia → carbamazepine",
    ],
    items=[
        mcq("EXAM25-08-04-1",
            "A 29-year-old woman reports recurrent headaches localized to the forehead and temples, occurring on several afternoons each week. She describes a band-like pressure. The pain resolves with sleep. There is no photophobia, nausea or aura. Neurological examination is normal. What is the most likely diagnosis?",
            "Tension-type headache",
            ["Migraine without aura", "Cluster headache", "Sinusitis-related headache", "Medication-overuse headache"],
            kind="old", src=SRC,
            explain='''ปวด **สองข้าง** หน้าผาก/ขมับ แบบ**บีบรัด** ไม่มี photophobia คลื่นไส้ หรือ aura neuro exam ปกติ = **tension-type headache** → paracetamol/NSAID · ถ้าเรื้อรังให้ amitriptyline ป้องกัน
- Migraine without aura เป็นข้างเดียว ตุบ ๆ มี photophobia/คลื่นไส้
- Cluster ปวดรอบตาข้างเดียวรุนแรงมาก มีน้ำตาน้ำมูก
- Sinusitis มีน้ำมูกข้น ไข้ ปวดใบหน้าเมื่อก้ม
- Medication-overuse ต้องมีประวัติใช้ยาแก้ปวด ≥ 10–15 วัน/เดือน''',
            pearl="สองข้าง บีบรัด ไม่มี photophobia/N/V = TTH", topic="Tension-type headache",
            ref=R(32, 33), nl=["2.3.6(8)"]),
        mcq("EXAM25-08-04-2",
            "A 30-year-old man presents with recurrent, severe, unilateral periorbital headaches. Each episode lasts about an hour and is associated with ipsilateral tearing of the eye and nasal congestion. The headaches occur daily for several weeks and then remit for months. What is the most likely diagnosis?",
            "Cluster headache",
            ["Migraine", "Tension-type headache", "Trigeminal neuralgia", "Acute sinusitis"],
            kind="old", src=SRC,
            explain='''ปวดรุนแรง **รอบตาข้างเดียว** + **autonomic ข้างเดียวกัน** (น้ำตาไหล คัดจมูก) + เป็นทุกวันหลายสัปดาห์แล้วหาย (**cluster period**) = **cluster headache** → acute: **100% O2** · ป้องกัน: **verapamil**
- Migraine ปวด 4–72 ชม. มี photophobia/N/V ไม่มี autonomic เด่นและไม่เป็นช่วงแบบนี้
- Tension-type เป็นสองข้าง ไม่รุนแรง ไม่มี autonomic
- Trigeminal neuralgia ปวดช็อตเป็นวินาที ไม่มีน้ำตา
- Sinusitis ไม่มีรูปแบบเป็นช่วงแล้วหายหลายเดือน''',
            pearl="รอบตาข้างเดียว + น้ำตา/น้ำมูก + เป็นช่วง = cluster", topic="Cluster headache",
            ref=R(34, 35), nl=["2.1.3"]),
        mcq("EXAM25-08-04-3",
            "A 28-year-old woman has recurrent left-sided throbbing headaches involving the retro-orbital, frontal and temporal regions, with photophobia and nausea. Episodes last 6–24 hours and occur 5 times a month despite appropriate acute treatment. She is planning a pregnancy next year. Neurological examination is normal. What is the most appropriate prophylactic medication?",
            "Propranolol",
            ["Topiramate", "Sumatriptan", "Ibuprofen", "Acetaminophen"],
            kind="old", src=SRC,
            explain='''Migraine without aura ที่เป็นบ่อย (≥ 4 วัน/เดือน) → ให้ยาป้องกัน · สไลด์เฉลย **propranolol** (beta-blocker เป็น first-line)
- Topiramate ก็เป็น first-line prophylaxis แต่ **teratogenic** (ปากแหว่ง) และลดฤทธิ์ยาคุม จึงไม่เหมาะในหญิงที่วางแผนตั้งครรภ์ (เติมข้อมูลนี้ในโจทย์เพื่อให้มีคำตอบเดียว)
- Sumatriptan, ibuprofen และ acetaminophen เป็น **acute (abortive) treatment** ไม่ใช่ prophylaxis''',
            pearl="Migraine prophylaxis → propranolol (topiramate ห้ามในผู้วางแผนตั้งครรภ์)", topic="Migraine prophylaxis",
            ref=R(36, 37), nl=["2.3.6(4)", "B3.4(7)"]),
        mcq("EXAM25-08-04-4",
            "A 70-year-old man experiences sharp, electric shock-like pain in the right V2/V3 distribution, triggered by tooth brushing. Each attack lasts seconds. Neurological examination is normal. What is the most likely diagnosis?",
            "Trigeminal neuralgia",
            ["Temporal arteritis", "Dental abscess", "Cluster headache", "Migraine"],
            kind="old", src=SRC,
            explain='''ปวด**แบบช็อตไฟฟ้า** ตามแขนง **V2/V3** นาน**เป็นวินาที** มี **trigger** (แปรงฟัน เคี้ยว พูด สัมผัส) neuro exam ปกติ = **trigeminal neuralgia** → **carbamazepine** (ถ้ามี neuro deficit หรืออายุน้อย ต้อง MRI หาสาเหตุ secondary)
- Temporal arteritis ปวดขมับตลอดเวลา jaw claudication ESR สูง ในผู้สูงอายุ
- Dental abscess ปวดตุบ ๆ ต่อเนื่อง ฟันกดเจ็บ บวม
- Cluster ปวดรอบตานาน 15–180 นาที มีน้ำตา
- Migraine ปวดนานหลายชั่วโมง''',
            pearl="ช็อตไฟฟ้าเป็นวินาทีใน CN V + trigger = TN → carbamazepine", topic="Trigeminal neuralgia",
            ref=R(38, 39), nl=["2.3.6-3(12)"]),
    ])

LECTURE = lecture("08", "Neuro", "status epilepticus · pontine bleed · PD · dementia · Bell · MG · headache",
    objectives=[
        "ให้ยาใน status epilepticus ตามระยะเวลา",
        "บอกตำแหน่งเลือดออกในสมองจากลักษณะตาและท่าทาง และจัดการ airway",
        "แยก Alzheimer จาก delirium และ dementia ชนิดอื่น",
        "แยก Bell palsy, MG และปวดศีรษะแต่ละชนิด พร้อมการรักษา",
    ],
    sections=[S1, S2, S3, S4])
