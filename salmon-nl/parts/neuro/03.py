from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Neuro"

# ---------------------------------------------------------------- 03-01 Seizure: causes, phases, workup
S1 = sec("neuro-03-01", "Seizure: สาเหตุ อาการ และการตรวจเบื้องต้น",
    "Provoked (metabolic, CNS) vs trigger ในคนเป็น epilepsy · aura → ictal → postictal (Todd's) · DTX ก่อนเสมอ · focal → CT/MRI", minutes=7,
    source=f"{D} หน้า 83–94, 104–105", nl=["B3.2.7(1)", "2.1.23", "2.3.6(9)"],
    md='''
### Trigger กับ cause ต่างกัน

- **Trigger (ปัจจัยกระตุ้นในคนที่เป็น epilepsy อยู่เดิม)**: ไข้, **อดนอน**, ดื่มสุรา, แสงกะพริบ, เสียงดัง, ความเครียด, รอบประจำเดือน, **ขาดยา** — นับเป็น trigger ได้ แต่ **ไม่นับเป็น provoked cause**
- **Cause ของ acute symptomatic (provoked) seizure**

| กลุ่ม | ตัวอย่าง |
|---|---|
| Systemic / metabolic | **Hypo/hyperglycemia**, hypo/hyperNa, hypo/hyperCa, febrile seizure ในเด็ก |
| CNS / toxic | **Alcohol withdrawal**, amphetamine, eclampsia, TBI, meningitis, encephalitis, stroke, uremic/hepatic encephalopathy, autoimmune encephalitis |

### ระยะของการชัก

- **Aura** (เฉพาะ **focal/partial seizure**) — ความรู้สึกผิดปกติตามตำแหน่งสมอง (เช่น déjà vu, epigastric rising ใน temporal lobe — เสริม) aura จริง ๆ คือ focal seizure ที่ยังไม่ลาม
- **Ictal**: motor (myoclonus, clonic, tonic, automatisms) · non-motor (autonomic, behavioral arrest, cognitive, emotional, absence)
- **Postictal**: ซึม หลับ สับสน ปวดหัว **อ่อนแรงชั่วคราว (Todd's paralysis)** พูด/เข้าใจภาษาไม่ได้ชั่วคราว

> **Seizure type ดูที่ onset** — เริ่มกระตุกที่หน้า/มือข้างเดียวแล้วลามทั้งตัว = **focal to bilateral tonic-clonic** ไม่ใช่ generalized · Todd's paralysis ข้างไหน บอก focus ฝั่งตรงข้าม

### Seizure mimics (เสริม — สไลด์เป็นภาพ)

| | Seizure | Syncope |
|---|---|---|
| ก่อนเกิด | Aura, ท่าใดก็ได้ (รวมนอน) | ยืนนาน ร้อน เจ็บปวด หน้ามืด เหงื่อออก |
| ระหว่าง | กระตุกนาน ตาเปิด **กัดลิ้นด้านข้าง** | กระตุกสั้น ๆ ได้ (< 15 วิ) ซีด |
| หลัง | **Postictal confusion** นาน | รู้สึกตัวเร็ว |

อื่น ๆ: psychogenic non-epileptic seizure, TIA, migraine aura, hypoglycemia, movement disorder

### Investigation (เสริมจากภาพสไลด์)

1. **DTX/CBG ก่อนเสมอ** แล้ว electrolytes (Na, Ca, Mg), BUN/Cr, LFT, toxicology ตามสงสัย
2. **CT brain** — ชักครั้งแรก, **focal seizure/focal deficit**, ไข้, trauma, กินยาต้านการแข็งตัวของเลือด, อายุมาก (MRI ดีกว่าสำหรับ epilepsy workup)
3. **LP** — ถ้ามีไข้/สงสัย CNS infection (หลัง CT ถ้ามีข้อบ่งชี้)
4. **EEG** — ช่วยยืนยันและจำแนก epilepsy syndrome ไม่ใช่การตรวจเร่งด่วนในห้องฉุกเฉิน
''',
    pearls=[
        "หมดสติ + กัดลิ้น/ปัสสาวะราด → DTX ก่อนทุกอย่าง",
        "Aura พบใน focal seizure เท่านั้น",
        "Todd's paralysis = อ่อนแรงหลังชักชั่วคราว บอกข้างของ focus",
        "Seizure type ดูที่ onset ไม่ใช่ตอนจบ",
        "Focal seizure ครั้งแรก → CT/MRI brain",
    ],
    items=[
        mcq("NEURO-03-01-1",
            "An 18-year-old man suddenly lost consciousness while eating lunch 2 hours ago. When he woke up he found he had been incontinent of urine and had bitten his tongue. He is now alert and the neurological examination is normal. What is the most appropriate initial investigation?",
            "Capillary blood glucose",
            ["CT brain", "Holter monitoring", "12-lead EKG", "Electroencephalography"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 104–105)",
            explain='''กัดลิ้น + ปัสสาวะราด ชวนคิดถึง seizure แต่การตรวจ **แรกสุด** คือ **DTX/blood glucose** เพราะ hypoglycemia เป็น provoked cause ที่แก้ได้ทันที (สไลด์เขียนว่า "DTX (CBG) ก่อน!" — ตัวเลือกเดิมคือ FBS)
- CT brain ทำภายหลังเมื่อ first seizure โดยเฉพาะถ้ามี focal sign
- Holter และ EKG ใช้เมื่อสงสัย cardiac syncope — ควรทำ EKG ด้วยแต่ไม่ก่อนน้ำตาล
- EEG ช่วยวินิจฉัย epilepsy syndrome ไม่ใช่การตรวจแรก''',
            pearl="หมดสติทุกราย → DTX ก่อน", topic="First seizure workup",
            ref=[f"{D} หน้า 104–105"], nl=["B3.2.7(1)", "2.1.23"]),
        mcq("NEURO-03-01-2",
            "A 52-year-old man who drinks a bottle of whisky daily stopped drinking 2 days ago when admitted for a leg fracture. He has a single generalized tonic-clonic seizure lasting 1 minute. He is tremulous and sweating; glucose, sodium and calcium are normal. CT brain is normal. Which best classifies this seizure?",
            "Acute symptomatic (provoked) seizure",
            ["Epilepsy requiring long-term antiepileptic drug", "Focal seizure with impaired awareness", "Psychogenic non-epileptic seizure", "Convulsive syncope"],
            explain='''ชักหลังหยุดสุรา 6–48 ชม. พร้อม tremor เหงื่อออก = **alcohol withdrawal seizure** ซึ่งสไลด์จัดเป็น CNS cause ของ **provoked (acute symptomatic) seizure** → รักษา withdrawal (benzodiazepine, thiamine) ไม่ต้องให้ AED ระยะยาว (เสริม)
- Epilepsy ต้องเป็น unprovoked seizure ≥ 2 ครั้งห่างกัน > 24 ชม.
- Focal seizure จะเริ่มที่ส่วนใดส่วนหนึ่งของร่างกาย/มี aura แต่รายนี้ generalized และมีสาเหตุชัด
- Psychogenic seizure ไม่สัมพันธ์กับการหยุดสุรา และไม่มี autonomic hyperactivity
- Convulsive syncope กระตุกสั้นมากและฟื้นเร็ว มักมีปัจจัยกระตุ้นเช่นยืนนาน''',
            pearl="Alcohol withdrawal seizure = provoked ไม่ใช่ epilepsy", topic="Provoked seizure",
            ref=[f"{D} หน้า 83, 91"], nl=["B3.2.5(4)", "B3.2.7(1)"]),
        mcq("NEURO-03-01-3",
            "A 25-year-old man has clonic jerking that starts in the right side of his face and right hand, then spreads to a generalized tonic-clonic seizure lasting 2 minutes. Afterward he has weakness of the right arm and leg for 6 hours, which then resolves completely. Glucose, electrolytes and calcium are normal. How should this event be classified?",
            "Focal to bilateral tonic-clonic seizure with postictal (Todd's) paralysis",
            ["Generalized tonic-clonic seizure with transient ischemic attack", "Absence seizure", "Myoclonic seizure", "Generalized seizure with conversion disorder"],
            explain='''**Seizure type ดูที่ onset**: เริ่มที่หน้าและมือขวา (focal จาก motor cortex ซ้าย) แล้วลามทั้งตัว = **focal to bilateral tonic-clonic** · อ่อนแรงซีกขวาชั่วคราวหลังชัก = **Todd's paralysis** ซึ่งช่วยยืนยันข้างของ focus → ต้องทำ **CT/MRI brain** หา structural lesion (สไลด์: ควร CT brain ก่อน โดยเฉพาะ focal seizure)
- เรียกว่า generalized ไม่ถูกเพราะ onset เป็น focal และอ่อนแรงหลังชักไม่ใช่ TIA
- Absence คือเหม่อสั้น ๆ ไม่มีกระตุกทั้งตัว
- Myoclonic คือกระตุกสั้น ๆ ไม่มี tonic-clonic ต่อเนื่อง
- Conversion disorder ไม่อธิบาย Todd's paralysis ที่เข้ากับ focus''',
            pearl="Onset ข้างเดียวแล้วลาม = focal to bilateral → imaging", topic="Seizure classification",
            ref=[f"{D} หน้า 84, 120–121"], nl=["B3.2.7(1)"]),
        mcq("NEURO-03-01-4",
            "A 25-year-old man had clonic jerking of the right face and hand that spread to a 2-minute generalized tonic-clonic seizure, followed by 6 hours of generalized weakness that resolved. Glucose, electrolytes and calcium are normal. CT brain shows a small calcified lesion in the left frontal cortex. What is the most appropriate long-term management?",
            "Phenytoin",
            ["Alprazolam", "Lorazepam", "Clonazepam", "No treatment and reassurance"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 120–121)",
            explain='''Focal seizure (onset ที่หน้า-มือขวา) ที่มี **structural lesion ที่ตรงกับอาการ** → ความเสี่ยงชักซ้ำสูง → เริ่ม AED สำหรับ focal seizure เช่น **phenytoin** (หรือ CBZ) — สไลด์เขียนเฉลยว่า "ควร CT brain ก่อน (โดยเฉพาะ focal seizure)" และ "seizure type ดูที่ onset" จึงเติมผล CT ในโจทย์ให้ตัดสินใจได้
- Alprazolam, lorazepam และ clonazepam เป็น benzodiazepine ใช้หยุดชักเฉียบพลันหรือเป็นยาเสริม ไม่ใช่ยาหลักระยะยาว
- ไม่ให้ยาเลยไม่เหมาะเมื่อมี epileptogenic lesion ที่อธิบาย focal seizure''',
            pearl="Focal seizure + lesion ใน CT → เริ่ม AED (PHT/CBZ)", topic="Focal seizure AED",
            ref=[f"{D} หน้า 112, 120–121"], nl=["B3.4(3)", "2.3.6(9)"]),
    ])

# ---------------------------------------------------------------- 03-02 Status epilepticus
F_SE = fig("neuro-03-02-f1", "Status epilepticus: ทำอะไรเมื่อไร", '''<svg viewBox="0 0 740 360">
 <defs><marker id="neuro-03-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <text x="370" y="20" text-anchor="middle" class="tb">เวลาที่ชักต่อเนื่อง (นาที)</text>
 <path d="M30 52H715" class="ln" marker-end="url(#neuro-03-02-a)"/>
 <path d="M30 44V60M140 44V60M250 44V60M470 44V60M560 44V60M700 44V60" class="ln"/>
 <text x="30" y="40" text-anchor="middle" class="t3">0</text>
 <text x="140" y="40" text-anchor="middle" class="t3">5</text>
 <text x="250" y="40" text-anchor="middle" class="t3">10</text>
 <text x="470" y="40" text-anchor="middle" class="t3">30</text>
 <text x="560" y="40" text-anchor="middle" class="t3">40</text>
 <text x="700" y="40" text-anchor="middle" class="t3">60</text>
 <rect x="30" y="72" width="108" height="270" rx="10" class="oksoft"/>
 <text x="84" y="96" text-anchor="middle" class="tb">Initial</text>
 <text x="84" y="114" text-anchor="middle" class="t3">0–5 min</text>
 <text x="84" y="146" text-anchor="middle" class="t2">มักหยุดเอง</text>
 <text x="84" y="170" text-anchor="middle" class="t2">จับตะแคง</text>
 <text x="84" y="190" text-anchor="middle" class="t2">กันกระแทก</text>
 <text x="84" y="214" class="t2" text-anchor="middle">จับเวลา</text>
 <rect x="142" y="72" width="106" height="270" rx="10" class="misssoft"/>
 <text x="195" y="96" text-anchor="middle" class="tb">Early SE</text>
 <text x="195" y="114" text-anchor="middle" class="t3">5–10 min</text>
 <text x="195" y="146" text-anchor="middle" class="t2">ABC, O2</text>
 <text x="195" y="166" text-anchor="middle" class="t2">DTX แก้ hypo</text>
 <text x="195" y="186" text-anchor="middle" class="t3">(thiamine ก่อน</text>
 <text x="195" y="202" text-anchor="middle" class="t3">glucose ถ้าเสี่ยง)</text>
 <rect x="150" y="218" width="90" height="56" rx="8" class="miss"/>
 <text x="195" y="240" text-anchor="middle" class="tw">IV diazepam</text>
 <text x="195" y="260" text-anchor="middle" class="tw">IM midazolam</text>
 <text x="195" y="296" text-anchor="middle" class="t3">ซ้ำได้ 1 ครั้ง</text>
 <text x="195" y="312" text-anchor="middle" class="t3">ใน 5–10 นาที</text>
 <rect x="252" y="72" width="216" height="270" rx="10" class="c1soft"/>
 <text x="360" y="96" text-anchor="middle" class="tb">Established SE</text>
 <text x="360" y="114" text-anchor="middle" class="t3">10–30 min · ยังไม่ต้องสนใจ seizure type</text>
 <rect x="268" y="130" width="184" height="36" rx="8" class="c1"/>
 <text x="360" y="153" text-anchor="middle" class="tw">IV loading 1st AED</text>
 <text x="268" y="190" class="t2">Phenytoin 20 mg/kg</text>
 <text x="268" y="212" class="t2">Phenobarbital 15–20 mg/kg</text>
 <text x="268" y="234" class="t2">Valproate 20–40 mg/kg</text>
 <text x="268" y="256" class="t2">Levetiracetam 60 mg/kg</text>
 <text x="268" y="278" class="t2">Lacosamide</text>
 <text x="268" y="306" class="t3">ขนาดยาเป็นส่วนเสริม</text>
 <text x="268" y="324" class="t3">PHT ≤ 50 mg/min · monitor EKG, BP</text>
 <rect x="472" y="72" width="250" height="270" rx="10" class="badsoft"/>
 <text x="597" y="96" text-anchor="middle" class="tb">Refractory SE</text>
 <text x="597" y="114" text-anchor="middle" class="t3">40–60 min (ไม่ตอบสนอง 2 ขั้นแรก)</text>
 <text x="488" y="144" class="t2">ETT · admit ICU</text>
 <text x="488" y="166" class="t2">continuous EEG</text>
 <text x="488" y="196" class="tb">2nd AED หรือ anesthetic</text>
 <rect x="488" y="210" width="218" height="94" rx="8" class="bad"/>
 <text x="597" y="234" text-anchor="middle" class="tw">IV midazolam infusion</text>
 <text x="597" y="254" text-anchor="middle" class="tw">Propofol</text>
 <text x="597" y="274" text-anchor="middle" class="tw">Thiopental</text>
 <text x="597" y="294" text-anchor="middle" class="tw">Ketamine</text>
 <text x="597" y="326" text-anchor="middle" class="t3">หา + แก้สาเหตุไปพร้อมกัน</text>
</svg>''', "อ่านจากซ้ายไปขวาตามนาทีที่ชัก: benzodiazepine ที่ 5 นาที → IV AED loading ที่ 10 นาที → anesthetic infusion เมื่อดื้อยา")

S2 = sec("neuro-03-02", "Status epilepticus",
    "SE = ชัก ≥5 นาที หรือไม่ฟื้นระหว่าง ≥2 ครั้ง · 5–10 นาที benzodiazepine · 10–30 นาที IV phenytoin/PB/VPA/LEV · refractory → ICU + anesthetic", minutes=8,
    source=f"{D} หน้า 95–103", nl=["2.2.37", "B3.4(3)", "B3.2.7(1)"],
    md='''
### นิยาม

**Status epilepticus** = ชัก **≥ 5 นาที** หรือ **ชัก ≥ 2 ครั้งโดยไม่ฟื้นสติเต็มที่ระหว่างครั้ง**

> ไม่ต้องรอ 30 นาที — ถ้าชักครบ 5 นาทีหรือมาถึงแล้วยังชัก/ไม่ฟื้นระหว่างครั้ง ให้รักษาเป็น SE ทันที

### Management ตามเวลา

[[fig:neuro-03-02-f1]]

| ระยะ | เวลา | การรักษา |
|---|---|---|
| Initial | 0–5 min | มักหยุดเอง (self-limited) |
| **Early SE** | 5–10 min | **ABC, แก้ hypoglycemia** · **IV diazepam / IM midazolam** ซ้ำได้ใน 5–10 นาทีถ้ายังไม่หยุด |
| **Established SE** | 10–30 min | **1st AED IV**: phenytoin, phenobarbital, valproic acid, levetiracetam, lacosamide |
| **Refractory SE** | 40–60 min | **ETT, ICU, continuous EEG** · 2nd AED หรือ anesthetic: IV midazolam, propofol, thiopental, ketamine |

- ระยะเฉียบพลัน **ยังไม่ต้องสนใจ seizure type** — เลือกยา IV ที่หยุดชักได้เร็ว
- ขนาดยา (เสริม): diazepam 0.15–0.2 mg/kg IV (max 10 mg/ครั้ง) · midazolam 10 mg IM (> 40 kg) · **phenytoin 20 mg/kg IV ไม่เร็วเกิน 50 mg/min** (ระวัง hypotension, arrhythmia, ห้ามผสม dextrose) · phenobarbital 15–20 mg/kg · valproate 40 mg/kg · levetiracetam 60 mg/kg (max 4,500 mg)
- ไข้ + ชัก/ซึม → หาสาเหตุ (meningitis/encephalitis) **หลังคุมชักและ airway** — CT/LP ไม่ใช่ขั้นแรกขณะยังชัก
- คนเสี่ยงขาด thiamine (สุรา ขาดอาหาร) → **thiamine ก่อน glucose**
''',
    figs=[F_SE],
    pearls=[
        "SE = ชัก ≥ 5 นาที หรือไม่ฟื้นระหว่าง 2 ครั้ง",
        "ขั้นแรก: ABC + DTX + IV diazepam/IM midazolam",
        "BZD 2 dose ไม่หยุด → IV phenytoin loading (established SE)",
        "Refractory → ETT, ICU, cEEG, midazolam/propofol/thiopental infusion",
        "ระยะเฉียบพลันไม่ต้องสนใจ seizure type",
    ],
    items=[
        mcq("NEURO-03-02-1",
            "A 50-year-old woman has had multiple generalized tonic-clonic seizures over 2 hours without regaining consciousness. BT 39°C, RR 8/min, BP 140/90 mmHg, GCS E1V3M1. While the ER team prepares to intubate her, she has another generalized tonic-clonic seizure. Capillary glucose is 110 mg/dL. What is the most appropriate initial management?",
            "IV diazepam",
            ["Lumbar puncture", "Emergency CT brain", "IV ceftriaxone", "IV phenytoin loading"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 98–99)",
            explain='''Status epilepticus ที่กำลังชักอยู่ — ยาตัวแรกต้องเป็น **benzodiazepine (IV diazepam)** ร่วมกับดูแล airway (เตรียม ETT เพราะ RR 8)
- LP และ CT เป็นการหาสาเหตุ (ไข้ → meningitis/encephalitis) ซึ่งทำหลังหยุดชักและ airway ปลอดภัย
- Ceftriaxone (± acyclovir) ควรให้เร็วถ้าสงสัย meningitis แต่ไม่ใช่สิ่งที่หยุดชักตรงหน้า
- Phenytoin เป็นขั้นที่สอง (established SE) หลังให้ benzodiazepine แล้วไม่หยุด''',
            pearl="SE กำลังชัก → benzodiazepine ก่อน", topic="Early SE",
            ref=[f"{D} หน้า 95–96, 98–99"], nl=["2.2.37"]),
        mcq("NEURO-03-02-2",
            "A 30-year-old woman had two seizures 20 minutes ago, each lasting 3 minutes, and did not regain consciousness between them. She received IV diazepam in the ER and the seizure has stopped. Which drug should be given next?",
            "IV phenytoin loading",
            ["Repeat IV diazepam", "Oral clonazepam", "Thiopental infusion", "Propofol infusion"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 100–101)",
            explain='''ชัก 2 ครั้งโดยไม่ฟื้นระหว่างครั้ง = **status epilepticus** · benzodiazepine ใช้หยุดชักได้ชั่วคราว ต้องตามด้วย **IV AED loading (phenytoin)** เพื่อป้องกันชักซ้ำ (ข้อสอบในสไลด์มี phenobarbital ด้วย ซึ่งก็เป็น 1st AED แต่กดการหายใจมากกว่าหลังได้ diazepam)
- ให้ diazepam ซ้ำเมื่อยังชักอยู่ — ตอนนี้หยุดแล้ว และฤทธิ์สั้น
- Clonazepam ทางปากไม่เหมาะในภาวะเฉียบพลันและผู้ป่วยยังไม่ตื่น
- Thiopental และ propofol ใช้ใน refractory SE เท่านั้น''',
            pearl="หลัง BZD ใน SE → ตามด้วย IV phenytoin loading", topic="Established SE",
            ref=[f"{D} หน้า 95–97, 100–101"], nl=["2.2.37", "B3.4(3)"]),
        mcq("NEURO-03-02-3",
            "A 70-year-old man with known epilepsy had a 30-minute generalized tonic-clonic seizure at home. In the ambulance he had two more seizures and received IV diazepam twice. On arrival he seizes again for 30 seconds, then stops but remains unresponsive. DTX is 140 mg/dL. What is the most appropriate management?",
            "Phenytoin",
            ["A third dose of diazepam", "Clonazepam", "Carbamazepine", "Propofol infusion"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 102–103)",
            explain='''ได้ benzodiazepine ครบ 2 ครั้งแล้วยังชัก = **established SE (10–30 นาที)** → **IV 1st AED loading** เช่น **phenytoin** (สไลด์: 1st AED phenytoin, phenobarbital, VPA, LEV, lacosamide — ยังไม่ต้องสนใจ seizure type)
- Diazepam ครั้งที่ 3 เพิ่มการกดการหายใจโดยไม่ช่วยควบคุมระยะยาว
- Clonazepam และ carbamazepine เป็นยารับประทาน ไม่เหมาะกับผู้ป่วยไม่รู้สึกตัวที่ชักต่อเนื่อง
- Propofol ใช้เมื่อเป็น refractory SE (ล้มเหลวจาก IV AED แล้ว) พร้อม ETT ใน ICU
(ตัวเลือก phenobarbital และ valproate ในสไลด์ถูกเปลี่ยนเป็นตัวลวงอื่นเพื่อให้มีคำตอบเดียว)''',
            pearl="BZD 2 ครั้งไม่หยุด → IV phenytoin/AED loading", topic="Established SE",
            ref=[f"{D} หน้า 96, 102–103"], nl=["2.2.37", "B3.4(3)"]),
        mcq("NEURO-03-02-4",
            "A 35-year-old man in status epilepticus received two doses of IV diazepam and a full loading dose of IV phenytoin, followed by IV valproate, but continues to have generalized convulsions 60 minutes after onset. He has been intubated. What is the most appropriate next step?",
            "Continuous IV midazolam infusion with continuous EEG monitoring in the ICU",
            ["Another 20 mg/kg bolus of phenytoin", "Oral levetiracetam via nasogastric tube", "Lumbar puncture", "Magnesium sulfate infusion"],
            explain='''ไม่ตอบสนองทั้ง benzodiazepine และ IV AED = **refractory SE** → **ICU, ETT, continuous EEG** + **anesthetic infusion** (midazolam, propofol, thiopental, ketamine) ตามสไลด์
- Phenytoin loading ซ้ำเต็มขนาดเสี่ยง toxicity (arrhythmia, hypotension) — ให้เสริมได้เพียงเล็กน้อยตามระดับยา
- Levetiracetam ทางปากออกฤทธิ์ช้า ไม่พอสำหรับ refractory SE
- LP เป็นการหาสาเหตุ ทำได้ภายหลัง ไม่หยุดชัก
- Magnesium ใช้ใน eclampsia หรือ hypomagnesemia''',
            pearl="Refractory SE → anesthetic infusion + cEEG ใน ICU", topic="Refractory SE",
            ref=[f"{D} หน้า 97"], nl=["2.2.37"]),
    ])

# ---------------------------------------------------------------- 03-03 Epilepsy diagnosis & AED choice
F_AED = fig("neuro-03-03-f1", "เลือก AED ตาม seizure type และกลุ่มผู้ป่วย", '''<svg viewBox="0 0 740 330">
 <defs><marker id="neuro-03-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="220" y="10" width="300" height="50" rx="10" class="acsoft"/>
 <text x="370" y="31" text-anchor="middle" class="tb">Unprovoked seizure ≥ 2 ครั้ง ห่าง &gt; 24 ชม.</text>
 <text x="370" y="50" text-anchor="middle" class="t3">= epilepsy → เริ่ม AED</text>
 <path d="M300 60L130 98" class="ln" marker-end="url(#neuro-03-03-a)"/>
 <path d="M370 60V98" class="ln" marker-end="url(#neuro-03-03-a)"/>
 <path d="M440 60L610 98" class="ln" marker-end="url(#neuro-03-03-a)"/>
 <rect x="20" y="100" width="220" height="150" rx="10" class="c1soft"/>
 <text x="130" y="124" text-anchor="middle" class="tb">Focal seizure</text>
 <text x="36" y="150" class="t2">Carbamazepine</text>
 <text x="36" y="172" class="t2">Phenytoin</text>
 <text x="36" y="194" class="t2">Valproic acid</text>
 <text x="36" y="216" class="t2">Phenobarbital</text>
 <text x="36" y="238" class="t3">(LEV, LTG ก็ใช้ได้ — เสริม)</text>
 <rect x="260" y="100" width="220" height="150" rx="10" class="c2soft"/>
 <text x="370" y="124" text-anchor="middle" class="tb">Generalized / อื่น ๆ</text>
 <text x="276" y="150" class="t2">Valproic acid</text>
 <text x="276" y="176" class="t3">CBZ/PHT ทำให้ absence และ</text>
 <text x="276" y="194" class="t3">myoclonic แย่ลงได้ (เสริม)</text>
 <text x="276" y="222" class="t3">แพ้ CBZ → เลี่ยง PHT, PB</text>
 <text x="276" y="238" class="t3">(HLA-B1502 cross-reactivity)</text>
 <rect x="500" y="100" width="220" height="150" rx="10" class="oksoft"/>
 <text x="610" y="124" text-anchor="middle" class="tb">หญิงวัยเจริญพันธุ์/ตั้งครรภ์</text>
 <text x="516" y="150" class="tb">ควรใช้</text>
 <text x="516" y="172" class="t2">Levetiracetam, Lamotrigine</text>
 <text x="516" y="202" class="tb">ไม่ควรใช้</text>
 <text x="516" y="224" class="t2">CBZ, PHT, VPA, PB</text>
 <text x="516" y="242" class="t3">(VPA teratogen มากสุด)</text>
 <rect x="20" y="266" width="700" height="54" rx="10" class="box"/>
 <text x="370" y="288" text-anchor="middle" class="tb">พิจารณาหยุดยา: ไม่ชัก ≥ 2 ปี + neuro exam และ CT/MRI ปกติ</text>
 <text x="370" y="308" text-anchor="middle" class="t3">Resolved epilepsy = ไม่ชัก 10 ปี โดยหยุดยามาแล้ว 5 ปี</text>
</svg>''', "เริ่มจากยืนยันว่าเป็น epilepsy แล้วเลือกยาตาม seizure type (ซ้าย/กลาง) เว้นแต่เป็นหญิงวัยเจริญพันธุ์ให้เลือกยาจากกล่องขวา")

S3 = sec("neuro-03-03", "Epilepsy: การวินิจฉัยและการเลือก AED",
    "Unprovoked ≥2 ครั้งห่าง >24 ชม. → AED · focal: CBZ/PHT/VPA/PB · generalized: VPA · หญิงวัยเจริญพันธุ์ LEV/LTG · แพ้ CBZ (HLA-B1502) เลี่ยง PHT/PB · หยุดยาเมื่อไม่ชัก ≥2 ปี", minutes=8,
    source=f"{D} หน้า 106–113, 120–127", nl=["2.3.6(9)", "B3.4(3)", "B3.2.7(1)"],
    md='''
### ขั้นตอนวินิจฉัย

1. **แยก seizure type** (focal / generalized / unknown onset)
2. **วินิจฉัย epilepsy**
3. **วินิจฉัย epilepsy syndrome** — จาก seizure type, อายุที่เริ่ม, EEG pattern, brain imaging

- โดยทั่วไป **unprovoked seizure 2 ครั้ง ห่างกัน > 24 ชม.** → วินิจฉัย epilepsy และ **เริ่ม AED**
- (เสริม) unprovoked 1 ครั้งแต่ความเสี่ยงชักซ้ำ ≥ 60% (เช่น EEG epileptiform, structural lesion) หรือเป็น epilepsy syndrome ก็นับเป็น epilepsy ได้

### การเลือก AED (สไลด์)

[[fig:neuro-03-03-f1]]

| สถานการณ์ | ยาที่เลือก |
|---|---|
| **Focal seizure** | Carbamazepine, phenytoin, valproic acid, phenobarbital |
| **Generalized / อื่น ๆ** | **Valproic acid** |
| **หญิงตั้งครรภ์/วัยเจริญพันธุ์** | **Levetiracetam, lamotrigine** · ไม่ควรใช้ CBZ, PHT, VPA, PB |
| แพ้ CBZ (SJS/rash) | เลี่ยง **phenytoin, phenobarbital, oxcarbazepine, lamotrigine** (cross-reactivity ใน **HLA-B1502**) → ใช้ VPA หรือ LEV |

- ผู้ป่วย epilepsy เดิมที่ **ขาดยา** แล้วชัก (ตอนนี้หยุดชักแล้ว) → **กลับมาเริ่ม AED เดิม** (ปกติ phenytoin) — ถ้าขาดยาไปนานระดับยาเป็นศูนย์ ให้ loading ใหม่ (oral loading ถ้าไม่ได้ชักอยู่, IV ถ้ายังชัก/SE) (เสริม)
- **Neurocysticercosis** เป็นสาเหตุ symptomatic epilepsy ที่พบบ่อยในไทย (ดูหมวด infection)

### การหยุดยา

- พิจารณาหยุด AED เมื่อ **ไม่ชัก ≥ 2 ปี** และ **neuro exam + CT/MRI brain ปกติ** (ค่อย ๆ ลดยา)
- **Epilepsy resolved** = **seizure-free 10 ปี โดยหยุด AED แล้ว 5 ปี**
''',
    figs=[F_AED],
    pearls=[
        "Epilepsy: unprovoked ≥ 2 ครั้งห่าง > 24 ชม. → เริ่ม AED",
        "Focal: CBZ/PHT · generalized: VPA",
        "หญิงวัยเจริญพันธุ์/ตั้งครรภ์: LEV, LTG",
        "แพ้ CBZ → เลี่ยง PHT, PB, OXC, LTG (HLA-B1502) → VPA",
        "หยุดยาได้เมื่อไม่ชัก ≥ 2 ปี + exam/imaging ปกติ",
    ],
    items=[
        mcq("NEURO-03-03-1",
            "A 30-year-old man has had two unprovoked generalized tonic-clonic seizures, one month ago and last week. He previously developed a severe rash on carbamazepine. Neuroimaging and blood tests are normal. What is the most appropriate drug to prevent recurrent seizures?",
            "Valproic acid",
            ["Phenytoin", "Clonazepam", "Phenobarbital", "Ketogenic diet"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 126–127)",
            explain='''Unprovoked GTC 2 ครั้งห่าง > 24 ชม. = **epilepsy** → เริ่ม AED · generalized seizure → **valproic acid** และไม่ cross-react กับ CBZ
- Phenytoin และ phenobarbital เป็น aromatic AED ที่ **cross-reactivity กับ carbamazepine** (โดยเฉพาะ HLA-B1502) ตามสไลด์
- Clonazepam ใช้เป็นยาเสริมระยะสั้น ไม่ใช่ยาหลักป้องกัน GTC
- Ketogenic diet ใช้ใน drug-resistant epilepsy (ส่วนใหญ่ในเด็ก)''',
            pearl="แพ้ CBZ → เลี่ยง PHT/PB → VPA", topic="AED in CBZ allergy",
            ref=[f"{D} หน้า 112, 126–127"], nl=["B3.4(3)", "2.3.6(9)"]),
        mcq("NEURO-03-03-2",
            "A 24-year-old man had a generalized tonic-clonic seizure 1 hour ago. He has had seizures since age 15, about 3–4 per year, but stopped his medication 1 year ago. He is now fully awake with a normal examination. What is the most appropriate management?",
            "Restart maintenance phenytoin",
            ["IV diazepam", "IV midazolam", "Gabapentin", "Observation without antiepileptic drug"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 122–123)",
            explain='''เป็น **epilepsy** (ชักซ้ำหลายปี) ที่ชักเพราะ **ขาดยา** และตอนนี้หยุดชักแล้ว → ต้อง **กลับมากิน AED (phenytoin)** — สไลด์เฉลย "antiepileptics ขึ้นกับ seizure type"
- Diazepam/midazolam ใช้หยุดชักขณะกำลังชักหรือ SE — ตอนนี้หยุดแล้ว
- Gabapentin ไม่ใช่ยาหลักสำหรับ GTC (เป็น add-on สำหรับ focal)
- ไม่ให้ยาเลยไม่เหมาะเพราะชัก 3–4 ครั้ง/ปีและจะชักซ้ำ''',
            pearl="Epilepsy ขาดยาแล้วชัก (หยุดแล้ว) → เริ่ม AED เดิม", topic="Breakthrough seizure",
            ref=[f"{D} หน้า 111–112, 122–123"], nl=["2.3.6(9)", "B3.4(3)"]),
        mcq("NEURO-03-03-3",
            "A 20-year-old man with neurocysticercosis-related epilepsy had been seizure-free on phenytoin 300 mg/day for 5 years but stopped it himself 1 month ago. Today he had an episode of staring with jerking of the right arm and leg for 2–3 minutes and has now fully recovered. What is the most appropriate management?",
            "Phenytoin 300 mg/day with an oral phenytoin loading dose",
            ["Phenytoin 300 mg/day without a loading dose", "Phenytoin 300 mg/day with an IV phenytoin loading dose", "Phenytoin 300 mg/day with a diazepam loading dose", "Phenytoin 300 mg/day plus clobazam 10 mg/day"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 124–125)",
            explain='''หยุดยามา 1 เดือน ระดับ phenytoin ในเลือดเป็นศูนย์ ถ้าเริ่ม 300 mg/day เฉย ๆ ต้องใช้ราว 1–3 สัปดาห์กว่าจะถึง steady state (half-life ยาวและ non-linear) → ควร **loading** และเมื่อผู้ป่วย **หยุดชักและรู้สึกตัวดี** ใช้ **oral loading** ได้ (เสริม — สไลด์ไม่มีคำเฉลยเป็นข้อความ)
- ไม่ loading จะเสี่ยงชักซ้ำในช่วงที่ระดับยายังต่ำ
- IV loading ใช้เมื่อยังชักอยู่หรือเป็น SE (ต้อง monitor EKG/BP)
- Diazepam ไม่ใช่ "loading" ของ phenytoin ใช้หยุดชักขณะชักเท่านั้น
- Clobazam เป็น add-on ไม่จำเป็นเพราะเดิมคุมได้ด้วย phenytoin ตัวเดียว''',
            pearl="ขาด PHT นาน + หยุดชักแล้ว → oral loading แล้วต่อ maintenance", topic="Restarting phenytoin",
            ref=[f"{D} หน้า 124–125"], nl=["B3.4(3)"]),
        mcq("NEURO-03-03-4",
            "A 26-year-old woman with juvenile myoclonic epilepsy is well controlled on valproate. She plans to become pregnant within the next year. What is the most appropriate change to her antiepileptic therapy?",
            "Switch to levetiracetam (or lamotrigine) before conception",
            ["Continue valproate and add folic acid only", "Switch to phenytoin", "Switch to carbamazepine", "Stop all antiepileptic drugs during pregnancy"],
            explain='''หญิงวัยเจริญพันธุ์/ตั้งครรภ์ → **levetiracetam หรือ lamotrigine** (สไลด์) โดยเปลี่ยนก่อนตั้งครรภ์ และให้ folic acid (เสริม)
- Valproate มีความเสี่ยง neural tube defect และ neurodevelopmental สูงสุด — folic acid ลดได้ไม่หมด
- Phenytoin และ carbamazepine เป็น teratogen และ CBZ/PHT ทำให้ myoclonic seizure แย่ลงได้
- หยุดยาทั้งหมดเสี่ยงชัก GTC ซึ่งอันตรายต่อแม่และทารกมากกว่า''',
            pearl="วางแผนตั้งครรภ์ → LEV/LTG", topic="AED in pregnancy",
            ref=[f"{D} หน้า 112"], nl=["B3.4(3)"]),
        mcq("NEURO-03-03-5",
            "A 28-year-old man with focal epilepsy has been seizure-free on carbamazepine for 3 years. His neurological examination and MRI brain are normal. He asks whether he can stop the medication. What is the most appropriate advice?",
            "Gradually taper carbamazepine with follow-up",
            ["He must continue the drug for life", "Stop carbamazepine abruptly today", "Continue until he has been seizure-free for 10 years", "Switch to phenobarbital before stopping"],
            explain='''ตามสไลด์ พิจารณาหยุด AED เมื่อ **ไม่ชัก ≥ 2 ปี และ neuro exam + CT/MRI ปกติ** → รายนี้เข้าเกณฑ์ → **ค่อย ๆ ลดยา** (เช่น 2–3 เดือน) และนัดติดตาม
- ไม่จำเป็นต้องกินตลอดชีวิตทุกราย
- หยุดทันทีเสี่ยง withdrawal seizure/SE
- "10 ปี" เป็นเกณฑ์ของ **epilepsy resolved** (ไม่ชัก 10 ปี โดยหยุดยามา 5 ปี) ไม่ใช่เกณฑ์เริ่มหยุดยา
- เปลี่ยนเป็น phenobarbital ไม่มีประโยชน์และเพิ่ม sedation''',
            pearl="ไม่ชัก ≥ 2 ปี + exam/imaging ปกติ → ค่อย ๆ หยุดยา", topic="Stopping AED",
            ref=[f"{D} หน้า 113"], nl=["2.3.6(9)"]),
    ])

# ---------------------------------------------------------------- 03-04 AED adverse effects & interactions
S4 = sec("neuro-03-04", "AED: ผลข้างเคียงและ drug interaction",
    "VPA: tremor alopecia pancreatitis wt gain · CBZ: SIADH agranulocytosis SJS · PHT: gum hyperplasia hirsutism nystagmus ataxia · PB: กดหายใจ · inducer ลดระดับยาอื่น", minutes=7,
    source=f"{D} หน้า 114–119, 128–131", nl=["B3.4(3)", "B3.2.5(3)"],
    md='''
### ผลข้างเคียงสำคัญ (สไลด์)

| ยา | ผลข้างเคียง |
|---|---|
| **Valproate** | **Tremor, alopecia, pancreatitis, weight gain**, teratogenicity (+ hepatotoxicity, hyperammonemia — เสริม) |
| **Carbamazepine** | **SIADH (hyponatremia), agranulocytosis**, teratogenicity, ataxia, hepatotoxicity, **SJS** (HLA-B1502) |
| **Phenytoin** | **Hirsutism, gingival hyperplasia, nystagmus**, SJS, drug-induced SLE, DRESS, sedation, diplopia, **ataxia**, arrhythmias (IV), teratogenicity |
| **Phenobarbital** | **Cardiorespiratory depression**, sedation, SJS |
| **Benzodiazepine** | Sedation, dependence, respiratory depression |

- Phenytoin toxicity เรียงตามระดับยา (เสริม): nystagmus → ataxia/dysarthria → ซึม/สับสน
- Lamotrigine: rash/SJS ถ้าเพิ่มขนาดเร็ว (เสริม) · Levetiracetam: หงุดหงิด อารมณ์แปรปรวน (เสริม)

### Drug interaction

| กลุ่ม | ยา | ผล |
|---|---|---|
| **Enzyme inducer** | **Phenytoin, carbamazepine, phenobarbital** | **ลดระดับยาอื่น** — OCP (คุมกำเนิดล้มเหลว), warfarin, antibiotic บางตัว, ARV, steroid |
| **Enzyme inhibitor** | **Valproate** | **เพิ่มระดับยาอื่น** (เช่น lamotrigine, phenobarbital) |

> ผู้ป่วยกิน phenytoin แล้วติดเชื้อรุนแรงขึ้นทั้งที่ได้ยาปฏิชีวนะ → คิดถึง **ระดับยาปฏิชีวนะไม่พอ** จาก enzyme induction

### AED overdose (เสริมจากข้อสอบในสไลด์)

- **Phenobarbital (barbiturate)**: โคม่าลึก **หายใจช้า (RR ต่ำ)**, **ความดันต่ำ**, hypothermia, pupil เล็ก/ปกติ ตอบสนองช้า, **areflexia**, อาจมีตุ่มน้ำตามจุดกดทับ → supportive, multiple-dose activated charcoal, urine alkalinization
- Ddx: **opioid toxidrome** (pinpoint pupils, RR ต่ำ — ตอบสนอง naloxone) · benzodiazepine เดี่ยว ๆ มักไม่ทำให้กดการหายใจรุนแรงหรือ hypotension มาก
''',
    pearls=[
        "CBZ: hyponatremia (SIADH), agranulocytosis, SJS",
        "PHT: gingival hyperplasia, hirsutism, nystagmus, ataxia",
        "VPA: tremor, alopecia, weight gain, pancreatitis, teratogen",
        "PHT/CBZ/PB = inducer ↓ระดับยาอื่น · VPA = inhibitor ↑ระดับยาอื่น",
        "โคม่า + RR ต่ำ + BP ต่ำ + areflexia ในคนกิน AED → phenobarbital overdose",
    ],
    items=[
        mcq("NEURO-03-04-1",
            "A 25-year-old man with epilepsy has taken phenytoin for 5 years. One day ago he developed fever, cough and sore throat, and a clinic prescribed an oral antibiotic. His illness worsened with high fever and rigors, and he was diagnosed with bacteremia. What is the most likely reason for treatment failure?",
            "Subtherapeutic antibiotic levels from phenytoin enzyme induction",
            ["Increased risk of aspiration pneumonia from epilepsy", "Inappropriate choice of antibiotic class", "Phenytoin-induced neutropenia", "Infection with an unusually virulent organism"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 128–129)",
            explain='''Phenytoin เป็น **enzyme inducer** → **ลดระดับยาอื่น** รวมถึงยาปฏิชีวนะบางชนิด ทำให้ระดับยาไม่พอรักษา (สไลด์เฉลยด้วยตาราง ↓ระดับยาอื่น / ↑ระดับยาอื่น — ตัวเลือกเดิมคือ "ATB ไม่พอ")
- Aspiration จากการชักไม่ได้อยู่ในโจทย์ (ไม่มีชักครั้งนี้)
- โจทย์ไม่ได้ชี้ว่ายาผิดชนิด
- Agranulocytosis เป็นผลข้างเคียงเด่นของ **carbamazepine** ไม่ใช่ phenytoin
- ไม่มีข้อมูลเชื้อดื้อ/รุนแรงพิเศษ''',
            pearl="PHT/CBZ/PB ลดระดับยาอื่น", topic="AED interaction",
            ref=[f"{D} หน้า 115, 128–129"], nl=["B3.4(3)"]),
        mcq("NEURO-03-04-2",
            "A 30-year-old man with epilepsy and polysubstance use is found unresponsive in bed; he was last seen well 8 hours ago. Pupils 2 mm with sluggish reaction, RR 8/min, BP 90/60 mmHg, pulse 80/min, mild cyanosis, no response to deep pain, generalized areflexia, no neck stiffness. Which drug is most likely responsible?",
            "Phenobarbital",
            ["Benzodiazepine", "Phenytoin", "Valproate", "Carbamazepine"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 130–131)",
            explain='''โคม่าลึก + **หายใจช้า + ความดันต่ำ + areflexia** pupil เล็กแต่ยังตอบสนอง = **barbiturate (phenobarbital) overdose** — สไลด์ระบุ PB S/E cardiorespiratory depression (และให้ Ddx opioid toxidrome)
- Benzodiazepine เดี่ยว ๆ มักง่วงแต่ไม่กดการหายใจและความดันรุนแรงขนาดนี้
- Phenytoin เกินขนาดเด่น nystagmus, ataxia ซึม ไม่ค่อยกดการหายใจ (ยกเว้น IV เร็ว → arrhythmia)
- Valproate เกินขนาดทำให้ซึมจาก hyperammonemia แต่ไม่เด่นเรื่อง RR 8 และ areflexia
- Carbamazepine เกินขนาดเด่น nystagmus, ataxia, anticholinergic, ชัก, QRS กว้าง''',
            pearl="AED + โคม่า RR ต่ำ BP ต่ำ areflexia = phenobarbital", topic="AED overdose",
            ref=[f"{D} หน้า 119, 130–131"], nl=["B3.2.5(3)", "B3.4(3)"]),
        mcq("NEURO-03-04-3",
            "A 45-year-old woman on an antiepileptic drug for focal seizures for 1 year presents with confusion. Serum sodium is 124 mEq/L, serum osmolality 260 mOsm/kg, urine osmolality 450 mOsm/kg, and she is clinically euvolemic. Which antiepileptic drug is she most likely taking?",
            "Carbamazepine",
            ["Phenytoin", "Valproate", "Levetiracetam", "Phenobarbital"],
            explain='''Euvolemic hyponatremia + Sosm ต่ำ + Uosm สูง = **SIADH** ซึ่งเป็นผลข้างเคียงเด่นของ **carbamazepine** (และ oxcarbazepine) ตามสไลด์ — และ CBZ เป็นยา focal seizure
- Phenytoin ยับยั้งการหลั่ง ADH ไม่ทำ SIADH
- Valproate เด่น tremor, alopecia, weight gain, pancreatitis
- Levetiracetam เด่นผลทางอารมณ์
- Phenobarbital เด่น sedation และกดการหายใจ''',
            pearl="AED + hyponatremia (SIADH) = carbamazepine", topic="CBZ adverse effect",
            ref=[f"{D} หน้า 119"], nl=["B3.4(3)"]),
        mcq("NEURO-03-04-4",
            "A 22-year-old woman who has taken an antiepileptic drug for 3 years complains of coarse facial hair and swollen, overgrown gums. Examination also shows horizontal nystagmus and mild gait ataxia. Which drug is she taking?",
            "Phenytoin",
            ["Valproate", "Carbamazepine", "Lamotrigine", "Levetiracetam"],
            explain='''**Hirsutism + gingival hyperplasia + nystagmus + ataxia** = **phenytoin** (ครบตามตารางในสไลด์)
- Valproate ทำให้ **ผมร่วง** (ตรงข้ามกับขนดก) น้ำหนักขึ้น tremor
- Carbamazepine เด่น SIADH, agranulocytosis, SJS (ataxia/diplopia ได้แต่ไม่มีเหงือกโต)
- Lamotrigine เด่น rash/SJS
- Levetiracetam เด่นหงุดหงิด/อารมณ์ผิดปกติ''',
            pearl="เหงือกโต + ขนดก + nystagmus = phenytoin", topic="Phenytoin adverse effect",
            ref=[f"{D} หน้า 119"], nl=["B3.4(3)"]),
    ])

LECTURE = lecture("03", "Seizure & epilepsy", "สาเหตุ · status epilepticus · เลือก AED · ผลข้างเคียง",
    objectives=[
        "แยก provoked seizure จาก epilepsy และเรียงลำดับการตรวจ (DTX ก่อน) ได้",
        "รักษา status epilepticus ตามเวลา (BZD → IV AED → anesthetic) ได้",
        "เลือก AED ตาม seizure type, เพศ/การตั้งครรภ์ และประวัติแพ้ CBZ ได้",
        "จำผลข้างเคียงและ interaction ของ AED ที่ออกสอบบ่อยได้",
    ],
    sections=[S1, S2, S3, S4])
