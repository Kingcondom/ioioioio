from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Neuro"

# ---------------------------------------------------------------- 11-01 Myasthenia gravis
F_MU = fig("neuro-11-01-f1", "โรคตามตำแหน่งบน motor unit: GBS · MG · LES · botulism · myopathy", '''<svg viewBox="0 0 740 400">
 <defs><marker id="neuro-11-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <circle cx="50" cy="90" r="30" class="c1soft"/>
 <text x="50" y="95" text-anchor="middle" class="t3">AHC</text>
 <path d="M80 90H296" class="lnc1"/>
 <path d="M100 80H280M100 100H280" class="lnf"/>
 <text x="190" y="70" text-anchor="middle" class="t3">axon + myelin</text>
 <rect x="300" y="66" width="56" height="48" rx="8" class="c2soft"/>
 <text x="328" y="95" text-anchor="middle" class="t3">pre</text>
 <rect x="420" y="66" width="56" height="48" rx="8" class="misssoft"/>
 <text x="448" y="95" text-anchor="middle" class="t3">post</text>
 <path d="M356 90H420" class="lnf"/>
 <text x="388" y="84" text-anchor="middle" class="t3">ACh</text>
 <rect x="530" y="56" width="200" height="68" rx="14" class="oksoft"/>
 <text x="630" y="95" text-anchor="middle" class="tb">Muscle</text>
 <path d="M190 128V154" class="ln" marker-end="url(#neuro-11-01-a)"/>
 <path d="M328 118V154" class="ln" marker-end="url(#neuro-11-01-a)"/>
 <path d="M448 118V154" class="ln" marker-end="url(#neuro-11-01-a)"/>
 <path d="M630 128V154" class="ln" marker-end="url(#neuro-11-01-a)"/>
 <rect x="10" y="156" width="250" height="226" rx="10" class="c1soft"/>
 <text x="135" y="178" text-anchor="middle" class="tb">GBS (nerve)</text>
 <text x="22" y="202" class="t2">anti-myelin · ascending</text>
 <text x="22" y="222" class="t2"><tspan class="tb">ชา</tspan> glove-stocking</text>
 <text x="22" y="242" class="t2">areflexia · CN palsy</text>
 <text x="22" y="262" class="t2">autonomic ±</text>
 <text x="22" y="290" class="t3">CSF protein ↑ WBC ปกติ</text>
 <text x="22" y="308" class="t3">NCS ↓velocity</text>
 <text x="22" y="356" class="tb">IVIG / PLEX</text>
 <rect x="266" y="156" width="124" height="226" rx="10" class="c2soft"/>
 <text x="328" y="178" text-anchor="middle" class="tb">Presynaptic</text>
 <text x="276" y="200" class="t3">↓ปล่อย ACh</text>
 <text x="276" y="222" class="tb">LES</text>
 <text x="276" y="240" class="t3">anti-VGCC · SCLC</text>
 <text x="276" y="256" class="t3">ดีขึ้นเมื่อใช้</text>
 <text x="276" y="272" class="t3">RNS ↑ (increment)</text>
 <text x="276" y="296" class="tb">Botulism</text>
 <text x="276" y="314" class="t3">descending</text>
 <text x="276" y="330" class="t3">pupil โต</text>
 <text x="276" y="356" class="t3">ทั้งคู่: ↓DTR ไม่ชา</text>
 <rect x="396" y="156" width="124" height="226" rx="10" class="misssoft"/>
 <text x="458" y="178" text-anchor="middle" class="tb">MG</text>
 <text x="406" y="200" class="t3">anti-AChR</text>
 <text x="406" y="220" class="t3">ล้าเมื่อใช้งาน</text>
 <text x="406" y="240" class="t3">ptosis, diplopia</text>
 <text x="406" y="260" class="t3">DTR ปกติ</text>
 <text x="406" y="280" class="t3">sensory ปกติ</text>
 <text x="406" y="300" class="t3">thymoma</text>
 <text x="406" y="320" class="t3">RNS ↓ (decrement)</text>
 <text x="406" y="356" class="tb">pyridostigmine</text>
 <rect x="526" y="156" width="204" height="226" rx="10" class="oksoft"/>
 <text x="628" y="178" text-anchor="middle" class="tb">Muscle</text>
 <text x="538" y="202" class="t2">proximal &gt; distal</text>
 <text x="538" y="222" class="t2">sensory ปกติ</text>
 <text x="538" y="242" class="t2">DTR ปกติ/ลดเล็กน้อย</text>
 <text x="538" y="268" class="tb">Periodic paralysis</text>
 <text x="538" y="288" class="t3">เป็นพัก ๆ หลังอาหารแป้ง</text>
 <text x="538" y="304" class="t3">K ต่ำ/สูง</text>
 <text x="538" y="328" class="tb">Myopathy</text>
 <text x="538" y="348" class="t3">alcohol, steroid,</text>
 <text x="538" y="364" class="t3">inflammatory (CK ↑)</text>
</svg>''', "ไล่จากซ้ายไปขวาตามเส้นทางของสัญญาณ: เส้นประสาท (GBS) → ปลายประสาทปล่อย ACh (LES, botulism) → receptor (MG) → กล้ามเนื้อ — มีชาเฉพาะโรคที่เส้นประสาท")

S1 = sec("neuro-11-01", "Myasthenia gravis",
    "Anti-AChR · fatigable weakness (ptosis diplopia เป็นมากตอนเย็น) DTR/sensory ปกติ · Ix anti-AChR, RNS decrement, ice-pack/edrophonium, CT chest (thymoma) · pyridostigmine · crisis: ETT + IVIG/PLEX", minutes=10,
    source=f"{D} หน้า 383–401", nl=["2.3.6-3(7)", "B3.2.2-3(3)", "B3.4(1)"],
    md='''
### Pathophysiology

- **Autoantibody ต่อ acetylcholine receptor (AChR)** ที่ postsynaptic membrane
- สัมพันธ์กับ **thymoma, thymic hyperplasia** และโรค autoimmune อื่น (Graves — เสริม)

### อาการ

[[fig:neuro-11-01-f1]]

- **Fatigability**: แย่ลงเมื่อใช้กล้ามเนื้อ **ดีขึ้นเมื่อพัก** (เป็นมากตอนบ่าย/เย็น)
- **Ocular MG**: **ptosis (asymmetric), diplopia** — curtain sign/enhanced ptosis (ยกหนังตาข้างหนึ่ง อีกข้างตกลง — เสริม)
- **Generalized MG**: **bulbar** (dysarthria, dysphagia), **proximal weakness**, dyspnea
- **Sensation และ DTR ปกติ** · **ไม่มี autonomic dysfunction** · รูม่านตาปกติ
- **Myasthenic crisis**: กำเริบเฉียบพลัน → **respiratory failure (hypoventilation)**

### Investigation (สไลด์)

- **Anti-AChR antibody**
- **EMG: decremental response ต่อ repetitive nerve stimulation (RNS)** · single-fiber EMG ไวที่สุด (เสริม)
- **CT chest** R/O thymoma/thymic hyperplasia
- **Edrophonium (Tensilon) test**: short-acting AChEI → ↑ACh → ptosis ดีขึ้น
- **Ice-pack test**: ความเย็นลดการทำงานของ AChE → ptosis ดีขึ้น

### Management

- **Oral pyridostigmine (1st line)** (AChEI — รักษาอาการ)
- **Immunosuppressant** ถ้ายังไม่ดี (prednisolone, azathioprine — เสริม)
- **Thymectomy กรณี thymoma** (และ generalized MG anti-AChR+ อายุ < 65 — เสริม)

### Myasthenic crisis

- Trigger: **infection (พบบ่อยสุด)**, ยา (aminoglycoside, fluoroquinolone, magnesium, β-blocker — เสริม), ขาดยา, ผ่าตัด
- Mx: **ETT**, **หยุด pyridostigmine ชั่วคราว** (เพิ่ม secretion), **IVIG/plasmapheresis**, **high-dose steroid**

| | Myasthenic crisis | Cholinergic crisis |
|---|---|---|
| สาเหตุ | โรคกำเริบ/ยาไม่พอ | **AChEI เกินขนาด** |
| Heart rate | ↑ | ↓ |
| Fasciculation | ไม่มี | **มี** |
| Pupil | Dilated | **Constricted** |
| Skin | Cold | Warm |
| Secretion | ↔ | **↑** |
| Edrophonium test | ดีขึ้น | ไม่ดีขึ้น (แย่ลง) |
| รักษา | ETT + IVIG/PLEX | **Atropine** + หยุด AChEI |
''',
    figs=[F_MU],
    pearls=[
        "MG: ล้าเมื่อใช้งาน ptosis/diplopia เป็นมากตอนเย็น · sensory/DTR/pupil ปกติ",
        "Ix: anti-AChR · RNS decremental · CT chest หา thymoma",
        "Tx: pyridostigmine · thymectomy ถ้ามี thymoma",
        "Crisis: หายใจล้มเหลวจาก hypoventilation → ETT + IVIG/PLEX",
        "Cholinergic crisis: fasciculation, pupil เล็ก, secretion มาก → atropine",
    ],
    items=[
        mcq("NEURO-11-01-1",
            "A 40-year-old man has drooping eyelids that worsen in the evening. Examination shows asymmetric ptosis, weakness of the right lateral rectus, and a positive curtain sign. Pupils are equal and reactive, and limb strength is normal. What is the diagnosis?",
            "Ocular myasthenia gravis",
            ["Cavernous sinus syndrome", "Horner syndrome", "Oculomotor nerve palsy from aneurysm", "Thyroid eye disease"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 388–389)",
            explain='''Ptosis ไม่สมมาตร **เป็นมากตอนเย็น (fatigable)** + EOM weakness ที่ไม่ตรงกับเส้นประสาทเส้นใดเส้นหนึ่ง + **curtain sign** + pupil ปกติ = **ocular MG** → pyridostigmine (สไลด์)
- Cavernous sinus syndrome มีปวด ตาโปน ชา V1 และหลาย CN เป็นแบบคงที่
- Horner syndrome ptosis เล็กน้อย + miosis + anhidrosis ไม่ fluctuate
- CN3 palsy จาก aneurysm มีรูม่านตาโต และปวดหัว
- Thyroid eye disease มี lid retraction ไม่ใช่ ptosis''',
            pearl="Ptosis เป็นมากตอนเย็น + pupil ปกติ = MG", topic="Ocular MG",
            ref=[f"{D} หน้า 384, 388–389"], nl=["2.3.6-3(7)"]),
        mcq("NEURO-11-01-2",
            "A 35-year-old woman has fluctuating proximal muscle weakness that improves with rest. BT 37°C, BP 110/70 mmHg, RR 40/min with accessory muscle use. Proximal power is 2/5 in the arms and legs. Sensation and reflexes are normal. What is the most likely diagnosis?",
            "Myasthenia gravis (in crisis)",
            ["Lambert-Eaton syndrome", "Chronic inflammatory demyelinating polyradiculoneuropathy", "Guillain-Barré syndrome", "Hypokalemic periodic paralysis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 390–391)",
            explain='''อ่อนแรง **fluctuate ดีขึ้นเมื่อพัก** + sensory/reflex ปกติ + หายใจลำบาก (respiratory muscle) = **MG (myasthenic crisis)** → ETT + IVIG/PLEX
- LES อ่อนแรงที่ **ดีขึ้นเมื่อใช้** และ reflex ลด
- CIDP เรื้อรัง มีชาและ areflexia
- GBS มี areflexia และชา
- Hypokalemic PP ไม่ fluctuate ตามการใช้งาน และมักไม่ทำให้หายใจล้มเหลวแบบนี้''',
            pearl="Fluctuating + ดีขึ้นเมื่อพัก + reflex ปกติ = MG", topic="Generalized MG",
            ref=[f"{D} หน้า 384, 390–391"], nl=["2.3.6-3(7)"]),
        mcq("NEURO-11-01-3",
            "A 30-year-old woman has 3 weeks of bilateral ptosis, binocular diplopia, dysarthria and fatigable weakness on sustained upgaze and arm abduction. Examination: proximal weakness with normal deep tendon reflexes and sensation. Which electrodiagnostic test is most useful?",
            "Repetitive nerve stimulation test",
            ["Muscle biopsy", "Needle electromyography alone", "Nerve conduction velocity study", "Serum creatine kinase"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 396–397)",
            explain='''Fatigable ptosis/diplopia/bulbar/proximal weakness = **MG** → **repetitive nerve stimulation** เห็น **decremental response** (สไลด์: Ix RNS, single fibre EMG)
- Muscle biopsy และ CK ใช้กับ myopathy — ใน MG ปกติ
- Needle EMG ทั่วไปแยก myopathy/neuropathy แต่ไม่จำเพาะ MG
- NCS วัดความเร็วการนำกระแสซึ่งปกติใน MG (ใช้กับ GBS/neuropathy)''',
            pearl="MG → RNS decrement", topic="MG investigation",
            ref=[f"{D} หน้า 385, 396–397"], nl=["2.3.6-3(7)"]),
        mcq("NEURO-11-01-7",
            "A 50-year-old man has had weakness that worsens during work for 2 months. Examination: bilateral ptosis with enhanced ptosis, proximal muscle weakness, DTR 2+ and normal sensation. Which is the most appropriate confirmatory investigation?",
            "Serum anti-acetylcholine receptor antibody",
            ["CT brain", "Serum electrolytes", "Serum creatine kinase", "Serum anti-thyroglobulin antibody"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 392–393)",
            explain='''Fatigable weakness + ptosis + reflex/sensation ปกติ = **MG** → ยืนยันด้วย **anti-AChR antibody** (ร่วมกับ RNS; ice-pack/edrophonium test เป็น bedside test) แล้วทำ CT chest หา thymoma
- CT brain ไม่อธิบาย fatigable weakness ที่ไม่มี UMN sign
- Electrolytes ใช้เมื่อสงสัย periodic paralysis (เฉียบพลันเป็นพัก ๆ ไม่มี ptosis)
- CK ใช้กับ myopathy ซึ่งไม่มี ptosis เด่นและไม่ fluctuate
- Anti-thyroglobulin ใช้กับ autoimmune thyroiditis ไม่ใช่การยืนยัน MG''',
            pearl="สงสัย MG → anti-AChR + RNS", topic="MG serology",
            ref=[f"{D} หน้า 385, 392–395"], nl=["2.3.6-3(7)"]),
        mcq("NEURO-11-01-4",
            "A 50-year-old man has had motor weakness during work for 2 months. Examination: bilateral ptosis with enhanced ptosis, proximal muscle weakness, DTR 2+ and normal sensation. What is the most likely associated abnormality?",
            "Thymoma",
            ["Small cell lung carcinoma", "Sarcoidosis", "Vasculitis", "Pituitary adenoma"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 398–399)",
            explain='''Ptosis + enhanced ptosis + fatigable proximal weakness + reflex ปกติ = **MG** ซึ่งสัมพันธ์กับ **thymoma/thymic hyperplasia** → CT chest (สไลด์)
- Small cell lung carcinoma สัมพันธ์กับ **LES** (reflex ลด ดีขึ้นเมื่อใช้)
- Sarcoidosis และ vasculitis ไม่เป็น association หลักของ MG
- Pituitary adenoma ไม่เกี่ยว (ตัวเลือก Graves' ในสไลด์ก็สัมพันธ์กับ MG ได้แต่ไม่ใช่คำตอบหลัก จึงเปลี่ยนเป็นตัวลวงอื่น)''',
            pearl="MG ↔ thymoma · LES ↔ SCLC", topic="MG association",
            ref=[f"{D} หน้า 383, 398–399"], nl=["2.3.6-3(7)"]),
        mcq("NEURO-11-01-5",
            "A 25-year-old woman with myasthenia gravis who has been lost to follow-up for 1 month presents with dyspnea and cyanosis for 1 hour. BP 90/60 mmHg, PR 100/min, RR 30/min with shallow breathing; lungs are clear. What is the most likely mechanism of her hypoxemia?",
            "Hypoventilation",
            ["Shunt", "Dead space ventilation", "Diffusion defect", "Ventilation–perfusion mismatch"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 400–401)",
            explain='''Myasthenic crisis → **กล้ามเนื้อหายใจอ่อนแรง** → หายใจตื้น ปอดปกติ = **hypoventilation** (PaCO2 สูง, A-a gradient ปกติ) — สไลด์เฉลย respiratory muscle weakness
- Shunt พบใน pneumonia/ARDS ที่ฟังปอดผิดปกติ
- Dead space พบใน PE
- Diffusion defect พบใน ILD
- V/Q mismatch พบใน COPD/asthma/pneumonia''',
            pearl="MG crisis = hypoventilation (A-a gradient ปกติ)", topic="Myasthenic crisis",
            ref=[f"{D} หน้า 384, 400–401"], nl=["2.3.6-3(7)"]),
        mcq("NEURO-11-01-6",
            "A 40-year-old man with myasthenia gravis took extra pyridostigmine because of worsening weakness. He now has increased weakness with diffuse muscle fasciculations, abdominal cramps, profuse salivation and bronchial secretions, pinpoint pupils and a heart rate of 48/min. What is the most appropriate treatment?",
            "Atropine and withholding pyridostigmine",
            ["Additional pyridostigmine", "Edrophonium infusion", "High-dose prednisolone alone", "Neostigmine"],
            explain='''กิน AChEI เกิน → **cholinergic crisis**: fasciculation, secretion มาก, pupil เล็ก, HR ช้า, ปวดท้อง → **atropine + หยุด AChEI** (สไลด์) และดูแล airway
- เพิ่ม pyridostigmine หรือให้ neostigmine/edrophonium จะทำให้แย่ลง (edrophonium test ใน cholinergic crisis ไม่ดีขึ้น)
- Prednisolone ใช้ใน myasthenic crisis และอาจทำให้อ่อนแรงมากขึ้นช่วงแรก''',
            pearl="Fasciculation + secretion + miosis + bradycardia ในคนกิน AChEI = cholinergic crisis → atropine", topic="Cholinergic crisis",
            ref=[f"{D} หน้า 386–387"], nl=["B3.4(1)"]),
    ])

# ---------------------------------------------------------------- 11-02 LES & botulism
S2 = sec("neuro-11-02", "Lambert-Eaton syndrome & botulism",
    "LES: anti-VGCC (presynaptic) + SCLC · proximal weakness ดีขึ้นเมื่อใช้ ↓DTR autonomic · RNS incremental → amifampridine + หามะเร็ง · Botulism: canned food → descending paralysis pupil โต ↓DTR sensory ปกติ → antitoxin + ETT", minutes=8,
    source=f"{D} หน้า 402–411", nl=["2.3.1(3)", "B3.2.2(5)", "B3.1.2(5)"],
    md='''
### Lambert-Eaton syndrome (LES)

- **Autoantibody ต่อ presynaptic voltage-gated calcium channel (VGCC)** → ↓ACh release
- สัมพันธ์กับ **small-cell lung cancer** (paraneoplastic)
- **Proximal weakness** (ลุกจากเก้าอี้ ขึ้นบันได) ที่ **ดีขึ้นเมื่อใช้ซ้ำ**
- **↓/absent DTR ที่กลับมาหลังออกแรงสั้น ๆ** (post-exercise facilitation)
- **Autonomic**: dry mouth, orthostatic hypotension
- Ix: **EMG incremental response ต่อ RNS** (high-frequency) · **anti-VGCC (confirm)** · **cancer screening** (CT chest)
- Tx: **รักษามะเร็ง** · **amifampridine** (3,4-diaminopyridine)

| | MG | LES |
|---|---|---|
| Associated | **Thymoma** | **Small cell lung CA** |
| Weakness | เริ่มที่ตา · **แย่ลงเมื่อใช้** | เริ่มที่ proximal · **ดีขึ้นเมื่อใช้** |
| Reflex | ปกติ | **↓/absent** |
| RNS | **↓ (decrement)** | **↑ (increment)** |
| Autonomic | ไม่มี | **มี** |
| ตอบสนอง AChEI | ดี | น้อย |

### Botulism

- **Clostridium botulinum** toxin → **block ACh release จาก presynaptic**
- Transmission: **foodborne** (อาหารกระป๋อง/หน่อไม้ปี๊บที่ฆ่าเชื้อไม่ดี **กระป๋องบวม**) · **wound** (เข็มฉีดยา — เสริม)
- อาการ: **GI** (N/V, ท้องเสีย/ท้องผูก) → **descending paralysis**: **ตาพร่า (loss of accommodation), mydriasis, diplopia, ptosis** → **dysarthria, dysphagia** → แขนขา → หายใจ
- **↓/absent DTR**, **sensation ปกติ**, ไม่มีไข้ รู้สึกตัวดี
- Tx: **supportive + ETT** · **antitoxin** (ให้เร็ว) · foodborne: gastric lavage · wound: debridement + ATB
- Prevention: ปรุงสุก **เลี่ยงอาหารกระป๋องที่โป่ง**, wound care

> Botulism vs GBS: botulism **descending** + **รูม่านตาโต/ไม่ตอบสนอง** + **ไม่มีชา** · GBS ascending + มีชา + pupil ปกติ
''',
    pearls=[
        "LES: anti-VGCC + SCLC + ดีขึ้นเมื่อใช้ + reflex ลด + autonomic",
        "RNS: MG decrement · LES increment",
        "Botulism: อาหารกระป๋อง + descending paralysis + pupil โต + sensation ปกติ",
        "Botulism → ETT + antitoxin",
    ],
    items=[
        mcq("NEURO-11-02-1",
            "A 61-year-old man who smokes heavily has difficulty getting up from a chair and climbing stairs. Examination shows proximal weakness of the arms and legs, with recovery of muscle power and patellar reflexes after brief vigorous contraction. He also complains of a dry mouth. Chest radiograph shows a lung mass. What is the most likely tumor type?",
            "Small cell lung cancer",
            ["Squamous cell carcinoma", "Adenocarcinoma", "Large cell carcinoma", "Mesothelioma"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 405–406)",
            explain='''Proximal weakness + **กำลังและ reflex กลับมาหลังออกแรง** (post-exercise facilitation) + dry mouth = **Lambert-Eaton syndrome** ซึ่งเป็น paraneoplastic ของ **small cell lung cancer**
- Squamous cell carcinoma สัมพันธ์กับ hypercalcemia (PTHrP)
- Adenocarcinoma สัมพันธ์กับ hypertrophic osteoarthropathy, Trousseau
- Large cell carcinoma ไม่มี paraneoplastic เด่น
- Mesothelioma สัมพันธ์กับ asbestos''',
            pearl="LES = SCLC", topic="LES association",
            ref=[f"{D} หน้า 402–406"], nl=["B3.1.2(5)"]),
        mcq("NEURO-11-02-2",
            "A 64-year-old woman has 3 months of proximal leg weakness, a dry mouth and dizziness on standing. Deep tendon reflexes are absent at rest but appear after 10 seconds of maximal voluntary contraction. Which test result would confirm the diagnosis?",
            "Incremental response on high-frequency repetitive nerve stimulation with anti-VGCC antibody",
            ["Decremental response on repetitive nerve stimulation with anti-AChR antibody", "Albuminocytologic dissociation in CSF", "Elevated serum creatine kinase with myopathic EMG", "Positive edrophonium test with improvement of ptosis"],
            explain='''ภาพ **LES** (proximal weakness, autonomic, areflexia ที่ฟื้นหลังออกแรง) → ยืนยันด้วย **RNS incremental response** + **anti-VGCC** (สไลด์) แล้วหามะเร็ง
- Decrement + anti-AChR เป็นของ MG
- Albuminocytologic dissociation เป็นของ GBS
- CK สูง + myopathic EMG เป็นของ myopathy
- Edrophonium ตอบสนองดีใน MG''',
            pearl="LES → RNS increment + anti-VGCC", topic="LES investigation",
            ref=[f"{D} หน้า 403–404"], nl=["B3.1.2(5)"]),
        mcq("NEURO-11-02-3",
            "A patient has had generalized weakness for 1 day, with double vision, nausea, vomiting and diarrhea, followed by shortness of breath. Yesterday he ate home-canned food at a picnic. BT 36.9°C, HR 75/min, BP 122/84 mmHg, RR 25/min. Examination: bilateral LMN facial palsy, ptosis, fixed dilated pupils, limited eye movements, power 2/5 in all limbs, intact sensation, absent reflexes. What is the most likely diagnosis?",
            "Botulism",
            ["Guillain-Barré syndrome", "Myasthenic crisis", "Organophosphate poisoning", "Hypokalemic periodic paralysis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 410–411)",
            explain='''กินอาหารกระป๋อง + GI symptom + **descending paralysis** (ตา → หน้า → แขนขา → หายใจ) + **fixed dilated pupils** + **sensation ปกติ** + areflexia = **botulism**
- GBS เป็น ascending มีชา และรูม่านตาปกติ
- Myasthenic crisis ไม่มีรูม่านตาโตและ reflex ปกติ
- Organophosphate ทำให้ **pupil เล็ก** secretion มาก fasciculation
- Hypokalemic PP ไม่มี ophthalmoplegia/bulbar/pupil ผิดปกติ''',
            pearl="อาหารกระป๋อง + descending + pupil โต + ไม่ชา = botulism", topic="Botulism",
            ref=[f"{D} หน้า 407–411"], nl=["2.3.1(3)", "B3.2.2(5)"]),
        mcq("NEURO-11-02-4",
            "Several villagers develop blurred vision, ptosis, dysphagia and descending weakness 1–2 days after eating home-canned bamboo shoots. One patient has a vital capacity that is falling rapidly. Besides airway protection and mechanical ventilation, what is the most specific treatment?",
            "Botulinum antitoxin as early as possible",
            ["IV pyridostigmine", "High-dose IV methylprednisolone", "IV penicillin alone", "Atropine and pralidoxime"],
            explain='''Foodborne botulism (หน่อไม้ปี๊บ) → **ETT/ventilation + antitoxin ให้เร็วที่สุด** (สไลด์ Mx: supportive, ETT, gastric lavage, antitoxin) — antitoxin จับ toxin ที่ยังไม่เข้าปลายประสาท
- Pyridostigmine ไม่ได้ผลเพราะปัญหาคือ ACh ไม่ถูกปล่อย
- Steroid ไม่มีบทบาท
- Penicillin ใช้ใน wound botulism ร่วมกับ debridement ไม่ใช่ foodborne
- Atropine + pralidoxime ใช้ใน organophosphate poisoning''',
            pearl="Botulism → ETT + antitoxin", topic="Botulism treatment",
            ref=[f"{D} หน้า 409"], nl=["2.3.1(3)"]),
    ])

# ---------------------------------------------------------------- 11-03 Periodic paralysis & myopathy
F_PP = fig("neuro-11-03-f1", "Periodic paralysis 3 ชนิด (ตามตารางสไลด์)", '''<svg viewBox="0 0 740 330">
 <rect x="10" y="10" width="130" height="36" rx="6" class="sunk"/>
 <rect x="146" y="10" width="190" height="36" rx="6" class="c1"/>
 <text x="241" y="33" text-anchor="middle" class="tw">Hypokalemic PP</text>
 <rect x="342" y="10" width="190" height="36" rx="6" class="bad"/>
 <text x="437" y="33" text-anchor="middle" class="tw">Hyperkalemic PP</text>
 <rect x="538" y="10" width="192" height="36" rx="6" class="miss"/>
 <text x="634" y="33" text-anchor="middle" class="tw">Thyrotoxic PP</text>
 <text x="20" y="74" class="tb">สาเหตุ</text>
 <text x="241" y="74" text-anchor="middle" class="t2">AD channelopathy</text>
 <text x="437" y="74" text-anchor="middle" class="t2">AD channelopathy</text>
 <text x="634" y="74" text-anchor="middle" class="t2">Hyperthyroid (ชายเอเชีย)</text>
 <path d="M10 88H730" class="lnf"/>
 <text x="20" y="112" class="tb">Trigger</text>
 <text x="241" y="112" text-anchor="middle" class="t2">อาหารแป้งมื้อใหญ่</text>
 <text x="241" y="130" text-anchor="middle" class="t3">พักหลังออกกำลัง แอลกอฮอล์ เครียด</text>
 <text x="437" y="112" text-anchor="middle" class="t2">อาหาร K สูง</text>
 <text x="437" y="130" text-anchor="middle" class="t3">ออกกำลัง อากาศเย็น</text>
 <text x="634" y="112" text-anchor="middle" class="t2">อาหารแป้งมื้อใหญ่</text>
 <text x="634" y="130" text-anchor="middle" class="t3">ออกกำลัง เครียด</text>
 <path d="M10 144H730" class="lnf"/>
 <text x="20" y="168" class="tb">Lab</text>
 <text x="241" y="168" text-anchor="middle" class="tb">K ↓</text>
 <text x="437" y="168" text-anchor="middle" class="tb">K ↔/↑</text>
 <text x="634" y="168" text-anchor="middle" class="tb">K ↓ · TSH ↓ T3/T4 ↑</text>
 <path d="M10 182H730" class="lnf"/>
 <text x="20" y="206" class="tb">Acute</text>
 <text x="241" y="206" text-anchor="middle" class="t2">Oral KCl</text>
 <text x="241" y="224" text-anchor="middle" class="t3">ระวัง rebound hyperK</text>
 <text x="437" y="206" text-anchor="middle" class="t2">Inhaled β2 agonist</text>
 <text x="437" y="224" text-anchor="middle" class="t3">diuretic</text>
 <text x="634" y="206" text-anchor="middle" class="t2">Oral KCl + propranolol</text>
 <text x="634" y="224" text-anchor="middle" class="t3">ระวัง rebound</text>
 <path d="M10 238H730" class="lnf"/>
 <text x="20" y="262" class="tb">Prevention</text>
 <text x="241" y="262" text-anchor="middle" class="t2">Acetazolamide</text>
 <text x="241" y="280" text-anchor="middle" class="t3">K-sparing diuretic</text>
 <text x="437" y="262" text-anchor="middle" class="t2">Acetazolamide</text>
 <text x="437" y="280" text-anchor="middle" class="t3">HCTZ</text>
 <text x="634" y="262" text-anchor="middle" class="t2">Propranolol</text>
 <text x="634" y="280" text-anchor="middle" class="t3">รักษา hyperthyroid</text>
 <rect x="10" y="296" width="720" height="28" rx="6" class="sunk"/>
 <text x="370" y="315" text-anchor="middle" class="t2">ทุกชนิด: อ่อนแรงเฉียบพลัน proximal &gt; distal · DTR ลด · sensory/CN ปกติ · หายในชั่วโมง–วัน</text>
</svg>''', "อ่านตามคอลัมน์: ชนิดของ PP ต่างกันที่ trigger และระดับ K · thyrotoxic PP ต้องตรวจ TSH และ acetazolamide ไม่ช่วย")

S3 = sec("neuro-11-03", "Periodic paralysis & myopathy",
    "อ่อนแรงเฉียบพลันเป็นพัก ๆ หลังอาหารแป้ง/ตื่นนอน proximal DTR ลด sensory ปกติ → serum K · hypoK PP: oral KCl ระวัง rebound · thyrotoxic PP: propranolol + รักษา thyroid · alcoholic myopathy: proximal atrophy CK ไม่สูง", minutes=8,
    source=f"{D} หน้า 379–382, 412–418", nl=["2.3.6(7)", "B3.2.5(1)", "2.3.13-3(7)"],
    md='''
### Periodic paralysis (PP)

[[fig:neuro-11-03-f1]]

| | Hypokalemic PP | Hyperkalemic PP | Thyrotoxic PP |
|---|---|---|---|
| Etiology | Autosomal dominant channelopathy | Channelopathy | **Hyperthyroidism** |
| Trigger | **High-carb meal**, exercise (ช่วงพัก), alcohol, stress | High-K meal, exercise, cold | **High-carb meal**, exercise, stress |
| Lab | **↓K** | ↔/↑K | **↓K, ↓TSH, ↑T3/T4** |
| Acute | **Oral KCl** (ระวัง rebound) | Inhaled β2 agonist, diuretics | **Oral KCl** (ระวัง rebound) + propranolol (เสริม) |
| Prevention | **Acetazolamide**, K-sparing diuretic | Acetazolamide, HCTZ | **Propranolol, รักษา hyperthyroidism** |

- Clinical ทุกชนิด: **acute attack, proximal > distal weakness**, hours–days · **DTR ลด**, **sensation และ CN ปกติ**, ไม่มี sphincter
- ตื่นนอนตอนเช้าลุกไม่ขึ้น หรือหลังกินอาหารมื้อใหญ่ → **ตรวจ serum electrolytes (K) ทันที**
- Hypokalemia รุนแรง → **arrhythmia** → ตรวจ EKG (U wave)
- (เสริม) แก้ K ไม่ต้องมากเพราะเป็นการย้าย K เข้าเซลล์ ไม่ได้ขาดจริง → ระวัง **rebound hyperkalemia** · thyrotoxic PP พบบ่อยในชายเอเชีย

### Alcoholic myopathy

- ดื่มสุราเรื้อรัง (ตับแข็ง: parotid โต palmar erythema)
- **Proximal weakness + atrophy** (deltoid, quadriceps), ไม่ปวด ไม่ชา, sensory ปกติ, reflex ปกติหรือลดเล็กน้อย
- **Chronic alcoholic myopathy: CK ไม่สูง** (acute alcoholic rhabdomyolysis จะ CK สูงมาก — เสริม)

### ทบทวนอ่อนแรงในคนดื่มสุรา/กรรมกร

| ภาพ | คิดถึง |
|---|---|
| ชา glove-stocking + areflexia + ขาดอาหาร | **Thiamine deficiency (dry beriberi)** |
| Proximal atrophy ไม่ชา CK ไม่สูง | **Alcoholic myopathy** |
| อ่อนแรงทันทีหลังอาหารมื้อใหญ่ เป็นซ้ำ | **Hypokalemic PP** |
''',
    figs=[F_PP],
    pearls=[
        "อ่อนแรงทันทีหลังอาหารแป้ง/ตื่นนอน + sensory ปกติ → ตรวจ K",
        "HypoK PP: oral KCl ระวัง rebound · ป้องกัน acetazolamide",
        "Thyrotoxic PP: K ต่ำ + TSH ต่ำ → propranolol + รักษา thyroid",
        "Alcoholic myopathy: proximal atrophy ไม่ชา CK ไม่สูง",
    ],
    items=[
        mcq("NEURO-11-03-1",
            "A 20-year-old man developed weakness of all limbs 2 hours ago; after a large meal he lay down and could not get up. He has had similar episodes over the past year, each resolving within about 3 hours. Examination: cranial nerves intact, sensation intact, proximal power 3/5, DTR 1+, flexor plantar responses. What is the most likely diagnosis?",
            "Periodic paralysis",
            ["Myasthenia gravis", "Spinal cord compression", "Guillain-Barré syndrome", "Polymyositis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 413–414)",
            explain='''อ่อนแรง **เฉียบพลันเป็นพัก ๆ หลังอาหารมื้อใหญ่** หายเองภายในชั่วโมง + proximal + DTR ลด + sensory/CN ปกติ = **(hypokalemic) periodic paralysis**
- MG ไม่ใช่อาการทันทีหลังอาหาร มี ptosis/diplopia reflex ปกติ
- Cord compression มี sensory level, UMN และไม่หายเอง
- GBS ค่อยเป็นหลายวัน มีชา ไม่เป็นซ้ำ ๆ แบบนี้
- Polymyositis ค่อยเป็นค่อยไป CK สูง''',
            pearl="อ่อนแรงซ้ำ ๆ หลังอาหารมื้อใหญ่ = periodic paralysis", topic="PP diagnosis",
            ref=[f"{D} หน้า 412–414"], nl=["2.3.6(7)", "B3.2.5(1)"]),
        mcq("NEURO-11-03-2",
            "During hospitalization, a 30-year-old man wakes up in the morning unable to get out of bed with weakness of all limbs. He is alert and has quadriparesis that is proximal and more pronounced in the legs, with no respiratory distress. What is the most appropriate investigation?",
            "Serum electrolytes",
            ["CSF examination", "CT brain", "Nerve conduction studies", "MRI cervical spine"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 415–416)",
            explain='''ตื่นมาอ่อนแรง proximal ทั้งตัวเฉียบพลัน รู้สึกตัวดี = นึกถึง **hypokalemia (periodic paralysis)** → **serum electrolytes** ด่วน (+ EKG ดู arrhythmia) — สไลด์เฉลย hypokalemia, Ix E'lyte
- CSF ใช้เมื่อสงสัย GBS ซึ่งค่อยเป็นและมีชา
- CT brain ไม่อธิบายอ่อนแรงทั้งสี่แขนขาแบบ proximal
- NCS ไม่ใช่การตรวจแรกในภาวะเฉียบพลันนี้
- MRI C-spine ใช้เมื่อมี sensory level/UMN''',
            pearl="ตื่นมาอ่อนแรงทั้งตัว → E'lyte (K) ก่อน", topic="PP investigation",
            ref=[f"{D} หน้า 412, 415–416"], nl=["2.3.6(7)", "2.2.15"]),
        mcq("NEURO-11-03-3",
            "A 28-year-old Thai man has a sudden episode of flaccid weakness of all limbs after a large rice meal. He has lost 5 kg over 2 months, has palpitations and a fine tremor. HR 120/min. Serum K 2.2 mEq/L; TSH is suppressed and free T4 is high. Besides cautious oral potassium, which drug is most useful acutely and for preventing further attacks until he is euthyroid?",
            "Propranolol",
            ["Acetazolamide", "Hydrochlorothiazide", "Spironolactone alone", "Pyridostigmine"],
            explain='''**Thyrotoxic periodic paralysis** (ชายเอเชีย hyperthyroid + K ต่ำ หลังอาหารแป้ง) → oral KCl (ระวัง rebound) + **propranolol** (non-selective β-blocker ลดการย้าย K เข้าเซลล์) + **รักษา hyperthyroidism** — นี่คือการป้องกันที่ได้ผล (สไลด์)
- Acetazolamide ป้องกัน familial hypoK PP แต่ไม่ได้ผลใน thyrotoxic PP
- HCTZ เป็นยาป้องกัน hyperkalemic PP และทำให้ K ต่ำลงอีก
- Spironolactone เดี่ยวไม่แก้กลไก
- Pyridostigmine ใช้ใน MG''',
            pearl="Thyrotoxic PP → propranolol + รักษา thyroid", topic="Thyrotoxic PP",
            ref=[f"{D} หน้า 412"], nl=["2.3.6(7)", "2.3.4(9)"]),
        mcq("NEURO-11-03-4",
            "A 40-year-old man has had progressive weakness for 2 months without pain or numbness. He takes no medication but drinks alcohol heavily. PR 90/min, BP 140/80 mmHg. Examination: parotid enlargement, palmar erythema, atrophy of the deltoids and quadriceps, power 3/5 for shoulder abduction, hip flexion and knee extension, intact sensation, knee jerk 1+ and other reflexes 2+, flexor plantar responses. Serum CK is not elevated. What is the most likely diagnosis?",
            "Alcoholic myopathy",
            ["Polymyositis", "Myasthenia gravis", "Guillain-Barré syndrome", "Hypokalemic myopathy"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 417–418)",
            explain='''ดื่มสุราเรื้อรัง (ตับแข็ง) + **proximal weakness + atrophy** ค่อยเป็นค่อยไป ไม่ปวด ไม่ชา reflex ปกติ/ลดเล็กน้อย + **CK ไม่สูง** = **chronic alcoholic myopathy**
- Polymyositis มี CK สูงชัด และมักปวดกล้ามเนื้อ
- MG มี fluctuation, ptosis และไม่มี atrophy ชัด
- GBS เฉียบพลัน มีชาและ areflexia
- Hypokalemic myopathy ต้องมี K ต่ำ (และมัก CK สูง)''',
            pearl="สุรา + proximal atrophy + CK ปกติ = alcoholic myopathy", topic="Alcoholic myopathy",
            ref=[f"{D} หน้า 417–418"], nl=["2.3.13-3(7)"]),
        mcq("NEURO-11-03-5",
            "A 35-year-old construction worker who drinks daily develops generalized weakness 2 hours after a large meal. He also has hoarseness. Examination: power 2/5 in all limbs, areflexia, and mild paresthesia of the hands and feet. Serum potassium is 4.0 mEq/L. He has had similar but milder numbness for months and eats mainly white rice. What is the most appropriate treatment?",
            "IV thiamine",
            ["Oral potassium chloride", "Botulinum antitoxin", "Pyridostigmine", "IV immunoglobulin"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 379–382)",
            explain='''อ่อนแรง + **areflexia + ชาปลายมือเท้า (peripheral nerve)** ในกรรมกรที่ดื่มสุราและกินข้าวขาวเป็นหลัก + **K ปกติ** → **thiamine deficiency (beriberi)** → **thiamine** (สไลด์เฉลยหน้า 380 = peripheral nerve lesion และหน้า 381–382 = vitamin B1; สไลด์มีเครื่องหมาย "??" ที่ "after a large meal" — จึงเติม K ปกติและประวัติอาหารเพื่อให้คำตอบเดียว)
- Oral KCl ใช้กับ hypokalemic PP ซึ่งไม่มีชาและ K จะต่ำ
- Botulinum antitoxin สำหรับ botulism (descending, pupil โต ไม่ชา)
- Pyridostigmine สำหรับ MG
- IVIG สำหรับ GBS — รายนี้มีประวัติชาเรื้อรังเป็นเดือนและภาวะขาดสารอาหาร''',
            pearl="อ่อนแรง + ชา + areflexia ในคนดื่มสุรา/กินข้าวขาว → thiamine", topic="Beriberi vs PP",
            ref=[f"{D} หน้า 378–382"], nl=["2.3.6-3(9)"]),
    ])

LECTURE = lecture("11", "NMJ & muscle", "Myasthenia gravis · LES · botulism · periodic paralysis · myopathy",
    objectives=[
        "วินิจฉัย MG สั่งการตรวจ และรักษารวมถึง myasthenic/cholinergic crisis ได้",
        "แยก MG กับ LES และ botulism จากอาการ reflex pupil และ RNS ได้",
        "วินิจฉัยและรักษา periodic paralysis ทั้งสามชนิดได้",
        "แยกอ่อนแรงในคนดื่มสุรา: beriberi, alcoholic myopathy, hypokalemia ได้",
    ],
    sections=[S1, S2, S3])
