from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Neuro"

# ---------------------------------------------------------------- 06-01 Parkinson's disease
F_PD = fig("neuro-06-01-f1", "Parkinson's disease: ตำแหน่งที่ยาออกฤทธิ์และการเลือกยา", '''<svg viewBox="0 0 740 420">
 <defs><marker id="neuro-06-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="20" y="14" width="330" height="230" rx="12" class="sunk"/>
 <text x="185" y="36" text-anchor="middle" class="tb">Nigrostriatal synapse</text>
 <rect x="40" y="52" width="130" height="40" rx="8" class="c1soft"/>
 <text x="105" y="77" text-anchor="middle" class="tb">Levodopa</text>
 <path d="M170 72H206" class="ln" marker-end="url(#neuro-06-01-a)"/>
 <text x="188" y="64" text-anchor="middle" class="t3">DDC</text>
 <rect x="208" y="52" width="120" height="40" rx="8" class="c1"/>
 <text x="268" y="77" text-anchor="middle" class="tw">Dopamine</text>
 <path d="M268 92V130" class="ln" marker-end="url(#neuro-06-01-a)"/>
 <rect x="208" y="132" width="120" height="40" rx="8" class="ok"/>
 <text x="268" y="157" text-anchor="middle" class="tw">D2 receptor</text>
 <path d="M208 72L150 120" class="lnbad" marker-end="url(#neuro-06-01-a)"/>
 <rect x="40" y="122" width="130" height="40" rx="8" class="badsoft"/>
 <text x="105" y="147" text-anchor="middle" class="t2">MAO-B สลาย</text>
 <rect x="40" y="188" width="130" height="44" rx="8" class="c2soft"/>
 <text x="105" y="207" text-anchor="middle" class="tb">DA agonist</text>
 <text x="105" y="225" text-anchor="middle" class="t3">pramipexole, ropinirole</text>
 <path d="M170 210L230 174" class="lnc2" marker-end="url(#neuro-06-01-a)"/>
 <text x="300" y="200" text-anchor="middle" class="t3">MAO-B inhibitor</text>
 <text x="300" y="218" text-anchor="middle" class="t3">selegiline, rasagiline</text>
 <text x="300" y="236" text-anchor="middle" class="t3">กันการสลาย</text>
 <text x="545" y="36" text-anchor="middle" class="tb">เลือกยาเริ่มต้น (สไลด์)</text>
 <rect x="370" y="50" width="350" height="34" rx="8" class="box"/>
 <text x="382" y="72" class="t3">อายุ →</text>
 <text x="545" y="72" text-anchor="middle" class="tb">&lt; 40–50 ปี</text>
 <text x="660" y="72" text-anchor="middle" class="tb">&gt; 40–50 ปี</text>
 <path d="M600 90V244" class="lnf"/>
 <rect x="370" y="90" width="350" height="72" rx="8" class="misssoft"/>
 <text x="382" y="114" class="tb">อาการ</text>
 <text x="382" y="134" class="tb">มาก</text>
 <text x="545" y="114" text-anchor="middle" class="t2">DA agonist</text>
 <text x="545" y="134" text-anchor="middle" class="t3">(เลี่ยง dyskinesia)</text>
 <text x="660" y="114" text-anchor="middle" class="tb">Levodopa</text>
 <text x="660" y="134" text-anchor="middle" class="t3">ได้ผลดีสุด</text>
 <rect x="370" y="168" width="350" height="76" rx="8" class="oksoft"/>
 <text x="382" y="192" class="tb">อาการ</text>
 <text x="382" y="212" class="tb">น้อย</text>
 <text x="545" y="200" text-anchor="middle" class="t2">MAO-B inhibitor</text>
 <text x="660" y="192" text-anchor="middle" class="t2">DA agonist</text>
 <text x="660" y="212" text-anchor="middle" class="t2">หรือ MAO-B</text>
 <rect x="20" y="262" width="700" height="146" rx="12" class="box"/>
 <text x="370" y="286" text-anchor="middle" class="tb">Parkinsonism ที่ "ไม่ใช่" PD — นึกถึงเมื่อ</text>
 <text x="36" y="312" class="t2"><tspan class="tb">Drug-induced</tspan> (ยา ↓dopamine): haloperidol, chlorpromazine, metoclopramide,</text>
 <text x="36" y="332" class="t2">flunarizine, cinnarizine, amiodarone → อาการ <tspan class="tb">สองข้างสมมาตร</tspan> เกิดเร็ว ตอบสนอง levodopa น้อย</text>
 <text x="36" y="358" class="t2"><tspan class="tb">Vascular parkinsonism</tspan>: ขาเด่น (lower-body), stepwise, มี stroke/white matter lesion</text>
 <text x="36" y="384" class="t3">ห้ามใช้ trihexyphenidyl ในผู้สูงอายุ (สับสน ปัสสาวะคั่ง) — ใช้ได้ในคนอายุน้อยที่ tremor เด่น (เสริม)</text>
</svg>''', "ซ้าย: levodopa เติมสารตั้งต้น DA agonist กระตุ้น receptor ตรง MAO-B inhibitor กันการสลาย · ขวา: เลือกยาตามความรุนแรงและอายุตามสไลด์ · ล่าง: ลักษณะที่ทำให้นึกถึงสาเหตุอื่น")

S1 = sec("neuro-06-01", "Parkinson's disease",
    "Bradykinesia (ต้องมี) + rest tremor/rigidity/postural instability · asymmetric, ตอบสนอง levodopa · R/O drug-induced (haloperidol, metoclopramide, flunarizine) · >40–50 ปีอาการมาก → levodopa · อายุน้อย → DA agonist/MAO-B", minutes=9,
    source=f"{D} หน้า 230–239, 241–242", nl=["B3.2.8-3(2)", "2.3.6-3(8)", "B3.4(2)"],
    md='''
### การวินิจฉัย (สไลด์)

1. **Parkinsonian syndrome** (≥ 2 ข้อ โดย **bradykinesia ต้องมี**): bradykinesia + **resting tremor** และ/หรือ **rigidity (cogwheel)** และ/หรือ postural instability
2. **R/O secondary cause** — drug-induced, vascular parkinsonism
3. **Supportive feature**: **unilateral onset/asymmetry**, resting tremor, progressive course, **response to levodopa**

### Drug-induced parkinsonism

- ยาที่ **↓dopamine**: typical antipsychotic (**haloperidol, chlorpromazine**), antiemetic (**metoclopramide**), CCB (**flunarizine, cinnarizine**), antiarrhythmic (amiodarone)
- นึกถึงเมื่อ: **bilateral/symmetric**, **acute/subacute onset**, **poor response to levodopa**
- Tx: หยุดยาที่เป็นสาเหตุ (หายใน 1–6 เดือน — เสริม)

### Non-motor signs

- Autonomic: **orthostatic hypotension**, urinary urgency, sexual dysfunction, ท้องผูก (เสริม)
- Neuropsychiatric: **depression**, (dementia, hallucination — เสริม)
- **Hyposmia/anosmia**, REM sleep behavior disorder (เสริม) — มักนำมาก่อน motor

### การรักษา

[[fig:neuro-06-01-f1]]

| ความรุนแรง | อายุ > 40–50 ปี | อายุ < 40–50 ปี |
|---|---|---|
| **Moderate–severe** | **Levodopa** | **Dopamine agonist** (pramipexole, ropinirole, rotigotine) |
| **Mild** | Dopamine agonist หรือ **MAO-B inhibitor** (selegiline, rasagiline) | **MAO-B inhibitor** |

- **Levodopa > 400 mg/day เพิ่มความเสี่ยง motor fluctuation/dyskinesia** (ตอบสนองยาไม่สม่ำเสมอ) — คนอายุน้อยจึงเริ่ม DA agonist
- Levodopa ให้ร่วมกับ carbidopa/benserazide (DDC inhibitor) ลด N/V (เสริม)
- DA agonist S/E (เสริม): **impulse control disorder** (พนัน ช้อปปิ้ง), ง่วงหลับฉับพลัน, ขาบวม, hallucination
- **Anticholinergic (trihexyphenidyl)**: ช่วย tremor ในคนอายุน้อย **ไม่ใช้ในผู้สูงอายุ** (สับสน ปัสสาวะคั่ง ท้องผูก) (เสริม)
''',
    figs=[F_PD],
    pearls=[
        "Parkinsonism ต้องมี bradykinesia + rest tremor หรือ rigidity",
        "PD: asymmetric + ตอบสนอง levodopa · drug-induced: symmetric + เกิดเร็ว",
        "Flunarizine, metoclopramide, haloperidol → drug-induced parkinsonism",
        "อายุมาก อาการมาก → levodopa · อายุน้อย → DA agonist/MAO-B",
        "Levodopa > 400 mg/day เพิ่ม motor fluctuation",
    ],
    items=[
        mcq("NEURO-06-01-1",
            "A 75-year-old patient has bradykinesia that is affecting daily activities. Examination shows cogwheel rigidity and a resting tremor, more prominent on the right. What is the most appropriate treatment?",
            "Levodopa",
            ["Trihexyphenidyl", "Diphenhydramine", "Propranolol", "Haloperidol"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 241–242)",
            explain='''Parkinson's disease ในผู้สูงอายุที่อาการรบกวนชีวิต (moderate–severe, อายุ > 40–50) → **levodopa** (สไลด์)
- Trihexyphenidyl (anticholinergic) ไม่ควรใช้ในผู้สูงอายุ — สับสน ปัสสาวะคั่ง ท้องผูก
- Diphenhydramine เป็น antihistamine ที่มีฤทธิ์ anticholinergic ไม่ใช่การรักษา PD
- Propranolol ใช้กับ essential/postural tremor
- Haloperidol ทำให้ parkinsonism แย่ลง''',
            pearl="PD ผู้สูงอายุ → levodopa", topic="PD treatment",
            ref=[f"{D} หน้า 239, 241–242"], nl=["B3.2.8-3(2)", "B3.4(2)"]),
        mcq("NEURO-06-01-2",
            "A 68-year-old woman has had 6 weeks of slowness, shuffling gait and symmetric rigidity of both arms with mild tremor. She has been taking flunarizine for dizziness for 2 months. What is the most appropriate next step?",
            "Discontinue flunarizine",
            ["Start levodopa", "Start pramipexole", "Start trihexyphenidyl", "MRI brain with DaT scan before any change"],
            explain='''Parkinsonism ที่ **สองข้างสมมาตร + เกิดเร็ว (subacute)** หลังได้ **flunarizine** (CCB ที่ลด dopamine) = **drug-induced parkinsonism** → **หยุดยาที่เป็นสาเหตุ** (สไลด์)
- Levodopa และ pramipexole มักตอบสนองไม่ดีใน drug-induced และไม่แก้สาเหตุ
- Trihexyphenidyl มีผลข้างเคียงมากในผู้สูงอายุ
- Imaging ไม่จำเป็นก่อนหยุดยา — ถ้าไม่ดีขึ้นหลังหยุดยาหลายเดือนจึงพิจารณา''',
            pearl="Parkinsonism สมมาตร + ยา flunarizine/metoclopramide → หยุดยา", topic="Drug-induced parkinsonism",
            ref=[f"{D} หน้า 233–234"], nl=["B3.2.5-3(1)", "2.3.6-3(8)"]),
        mcq("NEURO-06-01-3",
            "A 38-year-old man has early Parkinson's disease with a mild left-hand resting tremor and slight bradykinesia that does not interfere with work. What is the most appropriate initial treatment according to the slide algorithm?",
            "MAO-B inhibitor (e.g., rasagiline)",
            ["Levodopa–carbidopa", "Haloperidol", "Propranolol", "Deep brain stimulation"],
            explain='''อาการ **mild** + **อายุ < 40–50 ปี** → **MAO-B inhibitor** (selegiline, rasagiline) ตามสไลด์ — เลื่อนการใช้ levodopa เพื่อลด motor fluctuation ในระยะยาว
- Levodopa ใช้เมื่ออาการปานกลาง–รุนแรงในคนอายุมาก (ในคนอายุน้อยอาการมากเลือก DA agonist ก่อน)
- Haloperidol ทำให้แย่ลง
- Propranolol ไม่ช่วย rest tremor ของ PD
- DBS ใช้เมื่อมี motor fluctuation ที่คุมด้วยยาไม่ได้''',
            pearl="PD อายุน้อย อาการน้อย → MAO-B inhibitor", topic="PD in young",
            ref=[f"{D} หน้า 239"], nl=["B3.4(2)"]),
        mcq("NEURO-06-01-4",
            "A 62-year-old man with Parkinson's disease started on pramipexole 6 months ago. His wife reports that he has recently lost a large amount of money gambling online, which is completely out of character. What is the most likely explanation?",
            "Impulse control disorder caused by the dopamine agonist",
            ["Frontotemporal dementia", "Levodopa-induced dyskinesia", "Depression of Parkinson's disease", "Normal pressure hydrocephalus"],
            explain='''**Dopamine agonist** (pramipexole, ropinirole) ทำให้เกิด **impulse control disorder** — พนัน ช้อปปิ้ง กินมาก hypersexuality (เสริม) → ลดขนาด/หยุดยา
- FTD ทำพฤติกรรมเปลี่ยนแต่เกิดสัมพันธ์กับการเริ่มยาชัดเจนแบบนี้ไม่ได้
- Dyskinesia เป็นการเคลื่อนไหวผิดปกติ ไม่ใช่พฤติกรรม
- Depression จะลดแรงจูงใจ ไม่ใช่พนันมากขึ้น
- NPH ไม่ทำให้พฤติกรรมเสี่ยงแบบนี้''',
            pearl="DA agonist → พนัน/ช้อปปิ้งผิดปกติ", topic="DA agonist adverse effect",
            ref=[f"{D} หน้า 239"], nl=["B3.4(2)"]),
    ])

# ---------------------------------------------------------------- 06-02 Tremor
S2 = sec("neuro-06-02", "Tremor: resting vs postural vs intention",
    "Resting = PD · postural (ยกแขนค้าง) = essential tremor, hyperthyroid · intention (ใกล้เป้าหมาย) = cerebellar · essential tremor: สองข้าง หัว เสียง ดีขึ้นเมื่อดื่ม ประวัติครอบครัว → propranolol", minutes=6,
    source=f"{D} หน้า 240, 243–248", nl=["2.1.24", "B3.4(7)"],
    md='''
### ชนิดของ tremor

| ชนิด | สั่นเมื่อ | สาเหตุ |
|---|---|---|
| **Resting** | ขณะพัก ดีขึ้นเมื่อขยับ | **Parkinson's disease** |
| **Postural** | **ยกแขนค้าง** | **Essential tremor**, **hyperthyroidism**, physiologic, ยา (salbutamol, VPA, lithium — เสริม) |
| **Intention (kinetic)** | **Finger-to-nose สั่นมากขึ้นเมื่อใกล้เป้าหมาย** | **Cerebellar lesion** (มี dysmetria, ataxia ร่วม) |

### Essential tremor

- **สองข้าง**, มือ (± **หัว, เสียง**) — postural/kinetic tremor ถือแก้ว ใช้ช้อน
- **ดีขึ้นเมื่อดื่มแอลกอฮอล์**
- **ประวัติครอบครัว** (autosomal dominant)
- neuro exam อื่นปกติ (ไม่มี bradykinesia/rigidity/cerebellar sign)
- **Tx: propranolol** (หรือ primidone — เสริม)

### Hyperthyroidism

- Fine postural tremor + น้ำหนักลด ใจสั่น คอพอก
- **Tx: propranolol (คุมอาการ) + รักษา hyperthyroidism (เช่น MMI)**

> แยก **ET กับ PD**: ET = สองข้าง สั่นตอนใช้งาน มีหัว/เสียง ดีขึ้นกับเหล้า · PD = ข้างเดียวเริ่มก่อน สั่นตอนพัก มี bradykinesia/rigidity
''',
    pearls=[
        "Resting tremor = PD · postural = ET/hyperthyroid · intention = cerebellum",
        "ET: สองข้าง + หัว/เสียง + ดีขึ้นเมื่อดื่มเหล้า + ประวัติครอบครัว",
        "ET → propranolol",
        "Postural tremor + คอพอก → propranolol + รักษา thyroid",
    ],
    items=[
        mcq("NEURO-06-02-1",
            "A 50-year-old man has had 2 years of hand shaking that makes it difficult to pick up objects and use utensils. The shaking improves after drinking alcohol, and his mother has similar symptoms. PR 64/min, BP 120/70 mmHg. Extraocular movements are full without nystagmus; there is tremor of both hands with arms outstretched; cerebellar signs are absent and gait is normal. What is the most appropriate management?",
            "Propranolol",
            ["Levodopa", "Lorazepam", "Amitriptyline", "Trihexyphenidyl"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 245–246)",
            explain='''**Postural tremor สองข้าง** + **ดีขึ้นกับแอลกอฮอล์** + **ประวัติครอบครัว** + ไม่มี cerebellar sign/parkinsonism = **essential tremor** → **propranolol** (สไลด์)
- Levodopa และ trihexyphenidyl ใช้กับ Parkinson's disease (resting tremor + bradykinesia)
- Lorazepam ลดสั่นชั่วคราวแต่เสพติดได้ ไม่ใช่ยาหลัก
- Amitriptyline ไม่รักษา tremor''',
            pearl="Postural tremor + ดีขึ้นกับเหล้า + FHx = ET → propranolol", topic="Essential tremor",
            ref=[f"{D} หน้า 240, 245–246"], nl=["2.1.24"]),
        mcq("NEURO-06-02-2",
            "A man has tremor of both hands that worsens as he reaches for his whisky glass; his mother had a similar tremor. He has also lost weight and has palpitations. Examination shows a diffusely enlarged thyroid gland and a fine tremor of the outstretched hands. What is the most appropriate management?",
            "Propranolol plus treatment of hyperthyroidism",
            ["Levodopa", "Trihexyphenidyl", "Thyroidectomy without medical preparation", "Clonazepam alone"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 243–244)",
            explain='''Postural tremor + **คอพอก** (และอาการ thyrotoxicosis ที่เติมในโจทย์) → **hyperthyroidism** → **propranolol คุมอาการสั่น + รักษา hyperthyroidism (เช่น MMI)** (สไลด์เฉลย postural tremor, hyperthyroidism → propranolol, Tx hyperthyroidism)
- Levodopa และ trihexyphenidyl ใช้กับ PD
- ผ่าตัดไทรอยด์โดยไม่เตรียมยาก่อนเสี่ยง thyroid storm
- Clonazepam ไม่แก้สาเหตุ''',
            pearl="Postural tremor + คอพอก → propranolol + antithyroid", topic="Hyperthyroid tremor",
            ref=[f"{D} หน้า 240, 243–244"], nl=["2.1.24", "2.3.4(9)"]),
        mcq("NEURO-06-02-3",
            "An elderly patient has hand shaking when holding objects such as a cup. Gait is normal, and there is no rigidity, bradykinesia or cerebellar sign. Thyroid function is normal. What is the appropriate management?",
            "Propranolol",
            ["Levodopa", "Diazepam", "Trihexyphenidyl", "Haloperidol"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 247–248)",
            explain='''สั่นเมื่อถือของ (postural/kinetic) โดยไม่มีอาการอื่น = **essential tremor** → **propranolol**
- Levodopa และ trihexyphenidyl ใช้กับ PD — trihexyphenidyl ยิ่งไม่เหมาะในผู้สูงอายุ
- Diazepam ไม่ใช่ยาหลัก และเพิ่มความเสี่ยงหกล้มในผู้สูงอายุ
- Haloperidol ไม่รักษา tremor และทำให้เกิด parkinsonism''',
            pearl="สั่นตอนถือแก้ว ไม่มีอาการอื่น → propranolol", topic="Essential tremor",
            ref=[f"{D} หน้า 247–248"], nl=["2.1.24"]),
        mcq("NEURO-06-02-4",
            "A 45-year-old man who drinks heavily has a tremor of the right hand that is absent at rest and with arms outstretched but becomes coarser as his finger approaches the examiner's finger. He also has past-pointing, dysdiadochokinesia of the right hand and a wide-based gait. Where is the lesion most likely located?",
            "Right cerebellar hemisphere",
            ["Left cerebellar hemisphere", "Substantia nigra", "Left internal capsule", "Thyroid gland (systemic cause)"],
            explain='''**Intention tremor** (สั่นมากขึ้นเมื่อใกล้เป้าหมาย) + dysmetria + dysdiadochokinesia = **cerebellar lesion** · cerebellum คุมแขนขา **ข้างเดียวกัน** → **cerebellar hemisphere ขวา**
- Cerebellum ซ้ายจะทำให้อาการข้างซ้าย
- Substantia nigra (PD) ให้ resting tremor
- Internal capsule ทำ hemiparesis ไม่ใช่ intention tremor
- Thyroid ให้ fine postural tremor สองข้าง''',
            pearl="Intention tremor = cerebellum ข้างเดียวกัน", topic="Intention tremor",
            ref=[f"{D} หน้า 240"], nl=["B3.1.1(6)", "2.1.24"]),
    ])

LECTURE = lecture("06", "Parkinson's disease & tremor", "Parkinsonism · drug-induced · เลือกยา · ชนิดของ tremor",
    objectives=[
        "วินิจฉัย Parkinson's disease และแยก drug-induced parkinsonism ได้",
        "เลือกยาเริ่มต้นตามอายุและความรุนแรงตามสไลด์ได้",
        "แยก resting, postural และ intention tremor และรักษา essential tremor ได้",
    ],
    sections=[S1, S2])
