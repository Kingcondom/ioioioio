from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Neuro"

# ---------------------------------------------------------------- 05-01 Approach to dementia
F_DEM = fig("neuro-05-01-f1", "Approach แยกชนิด dementia (ตามแผนภาพในสไลด์)", '''<svg viewBox="0 0 740 400">
 <defs><marker id="neuro-05-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="200" y="10" width="340" height="46" rx="10" class="acsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">สงสัยสมองเสื่อม (รบกวน ADL)</text>
 <text x="370" y="48" text-anchor="middle" class="t3">R/O delirium, depression, reversible cause แล้ว → ตรวจ neuro</text>
 <path d="M280 56L120 92" class="ln" marker-end="url(#neuro-05-01-a)"/>
 <path d="M370 56V92" class="ln" marker-end="url(#neuro-05-01-a)"/>
 <path d="M460 56L620 92" class="ln" marker-end="url(#neuro-05-01-a)"/>
 <rect x="20" y="94" width="200" height="40" rx="10" class="box"/>
 <text x="120" y="119" text-anchor="middle" class="tb">Neuro exam ปกติ</text>
 <rect x="270" y="94" width="200" height="40" rx="10" class="box"/>
 <text x="370" y="119" text-anchor="middle" class="tb">Parkinsonism</text>
 <rect x="520" y="94" width="200" height="40" rx="10" class="box"/>
 <text x="620" y="119" text-anchor="middle" class="tb">Focal neurodeficit</text>
 <path d="M70 134V170" class="ln" marker-end="url(#neuro-05-01-a)"/>
 <path d="M170 134V170" class="ln" marker-end="url(#neuro-05-01-a)"/>
 <rect x="10" y="172" width="110" height="72" rx="10" class="c1"/>
 <text x="65" y="198" text-anchor="middle" class="tw">Alzheimer</text>
 <text x="65" y="218" text-anchor="middle" class="tw">ความจำเด่น</text>
 <rect x="128" y="172" width="110" height="72" rx="10" class="c2"/>
 <text x="183" y="198" text-anchor="middle" class="tw">FTD</text>
 <text x="183" y="218" text-anchor="middle" class="tw">พฤติกรรม/</text>
 <text x="183" y="236" text-anchor="middle" class="tw">ภาษาเด่น</text>
 <rect x="270" y="150" width="200" height="56" rx="10" class="misssoft"/>
 <text x="370" y="172" text-anchor="middle" class="tb">Parkinsonism นำ</text>
 <text x="370" y="192" text-anchor="middle" class="tb">dementia &lt; 1 ปี?</text>
 <path d="M320 206L300 238" class="ln" marker-end="url(#neuro-05-01-a)"/>
 <path d="M420 206L440 238" class="ln" marker-end="url(#neuro-05-01-a)"/>
 <text x="304" y="226" text-anchor="end" class="t3">≤ 1 ปี</text>
 <text x="452" y="226" class="t3">&gt; 1 ปี</text>
 <rect x="240" y="240" width="120" height="64" rx="10" class="ac"/>
 <text x="300" y="266" text-anchor="middle" class="tw">Lewy body</text>
 <text x="300" y="286" text-anchor="middle" class="tw">(DLB)</text>
 <rect x="380" y="240" width="120" height="64" rx="10" class="miss"/>
 <text x="440" y="266" text-anchor="middle" class="tw">Parkinson</text>
 <text x="440" y="286" text-anchor="middle" class="tw">dementia</text>
 <rect x="520" y="150" width="200" height="56" rx="10" class="misssoft"/>
 <text x="620" y="172" text-anchor="middle" class="tb">Brain imaging อธิบาย</text>
 <text x="620" y="192" text-anchor="middle" class="tb">อาการสมองเสื่อม?</text>
 <path d="M580 206L575 238" class="ln" marker-end="url(#neuro-05-01-a)"/>
 <path d="M660 206L665 238" class="ln" marker-end="url(#neuro-05-01-a)"/>
 <rect x="520" y="240" width="105" height="64" rx="10" class="bad"/>
 <text x="572" y="266" text-anchor="middle" class="tw">Vascular</text>
 <text x="572" y="286" text-anchor="middle" class="tw">dementia</text>
 <rect x="633" y="240" width="97" height="64" rx="10" class="sunk"/>
 <text x="681" y="266" text-anchor="middle" class="t2">Other +</text>
 <text x="681" y="286" text-anchor="middle" class="t2">CVD</text>
 <text x="560" y="230" text-anchor="end" class="t3">ใช่</text>
 <text x="676" y="230" class="t3">ไม่</text>
 <rect x="10" y="322" width="720" height="68" rx="10" class="box"/>
 <text x="24" y="344" class="t2"><tspan class="tb">AD:</tspan> episodic memory, visuospatial, word-finding</text>
 <text x="390" y="344" class="t2"><tspan class="tb">FTD:</tspan> disinhibition, apathy</text>
 <text x="24" y="366" class="t2"><tspan class="tb">DLB:</tspan> visual hallucination ตั้งแต่แรก, RBD</text>
 <text x="390" y="366" class="t2"><tspan class="tb">VaD:</tspan> abrupt, stepwise, focal deficit</text>
 <text x="24" y="384" class="t3">MMSE/TMSE &lt; 24 · MoCA &lt; 25 สนับสนุน</text>
</svg>''', "เริ่มจากตรวจระบบประสาท: ปกติ → แยกด้วยอาการเด่น (ความจำ = AD, พฤติกรรม = FTD) · มี parkinsonism → ใช้กฎ 1 ปี · มี focal deficit → ดูว่า imaging อธิบายได้ไหม")

S1 = sec("neuro-05-01", "Dementia: นิยาม การแยกโรค และชนิด",
    "R/O delirium/depression → dementia (รบกวน ADL) vs MCI → reversible → type · TMSE <24, MoCA <25 · AD memory · VaD stepwise · DLB VH + parkinsonism <1 ปี · FTD behavior", minutes=9,
    source=f"{D} หน้า 190–197, 202–206, 220–227", nl=["2.3.5-3(5)", "B3.2.8-3(1)", "2.3.6-3(1)"],
    md='''
### ขั้นตอน (สไลด์)

1. **R/O delirium / depression**
2. **แยก dementia กับ MCI**
3. **R/O reversible dementia**
4. **แยกชนิด dementia**

### นิยาม

- **Dementia (major neurocognitive disorder)** = cognitive ลดลงใน domain ใดก็ได้ (complex attention, executive function, learning & memory, language, visuospatial, social cognition) **ที่รบกวนชีวิตประจำวันหรือการเข้าสังคม** (เช่น ต้องให้ช่วยจัดยา จ่ายบิล) และ **ไม่ใช่ delirium หรือโรคจิตเวช**
- Screening: **TMSE < 24**, **MoCA < 25**

| ภาวะ | ลักษณะ |
|---|---|
| **Normal aging** | คิดช้า นึกช้า สมาธิลด ทำหลายอย่างพร้อมกันแล้วพลาด แต่ **ใช้ชีวิตประจำวันได้ปกติ** |
| **MCI** | Cognitive ลดลงชัด แต่ **ไม่รบกวน ADL** |
| **Dementia** | **รบกวน ADL** |
| **Pseudodementia** | ร่วมกับ **major depression** — อาการหลังอารมณ์เศร้า |
| **Delirium** (เสริม) | **เฉียบพลัน**, attention/consciousness ผันผวน, มีสาเหตุทางกาย |

### ชนิดของ dementia

[[fig:neuro-05-01-f1]]

| ชนิด | ลักษณะเด่น |
|---|---|
| **Alzheimer (AD)** | **↓episodic memory** (ลืมเรื่องใหม่ วางของผิดที่แล้วโทษคนอื่น), ↓visuospatial (หลงทาง), word-finding difficulty · ค่อยเป็นค่อยไป · neuro exam ปกติ |
| **Vascular (VaD)** | **Abrupt** cognitive decline, **stepwise deterioration**, **focal neurodeficit** |
| **Dementia with Lewy bodies (DLB)** | **Visual hallucination** (ตั้งแต่แรก), **parkinsonism**, cognitive ลด **< 1 ปีหลัง** parkinsonism (หรือพร้อมกัน), ↓attention/executive/visuospatial, **REM sleep behavior disorder** |
| **Parkinson disease dementia** | Parkinsonism นำ **> 1 ปี** แล้วจึงสมองเสื่อม |
| **Frontotemporal (FTD)** | Behavioral variant (พบบ่อยสุด): **disinhibition, apathy**, พฤติกรรมไม่เหมาะสม · อายุน้อยกว่า AD |

### BPSD

- Depression anxiety agitation, psychosis (hallucination, delusion), apathy disinhibition, sleep problem
- **มักพบในระยะหลัง** ไม่ควรพบตั้งแต่แรก **ยกเว้น DLB** ที่ visual hallucination มาตั้งแต่ต้น
- (เสริม) DLB **ไวต่อ antipsychotic มาก** (rigidity รุนแรง, NMS) → เลี่ยง haloperidol
''',
    figs=[F_DEM],
    pearls=[
        "Dementia = cognitive ลดลงจน รบกวน ADL · MCI = ไม่รบกวน",
        "AD: ลืมเรื่องใหม่ + หลงทาง + หาคำพูดไม่เจอ, neuro exam ปกติ",
        "DLB: visual hallucination + parkinsonism ภายใน 1 ปี + RBD",
        "VaD: abrupt, stepwise, focal deficit",
        "FTD: พฤติกรรมเปลี่ยน disinhibition/apathy",
    ],
    items=[
        mcq("NEURO-05-01-1",
            "A 75-year-old woman has progressive forgetfulness. She can no longer recognize her friends, cannot dress herself, and gets lost on her way home. She is alert with normal attention. What is the most likely diagnosis?",
            "Dementia",
            ["Amnesia", "Delirium", "Dysthymia", "Normal aging"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 220–221)",
            explain='''เสียหลาย cognitive domain — **memory** (จำเพื่อนไม่ได้), **executive** (แต่งตัวเองไม่ได้), **visuospatial** (กลับบ้านไม่ได้) — และ **รบกวน ADL** = **dementia** (สไลด์เฉลยด้วยการแยก domain)
- Amnesia เสียเฉพาะความจำ ไม่เสีย executive/visuospatial
- Delirium จะเฉียบพลันและ attention/consciousness ผันผวน
- Dysthymia เป็นอารมณ์เศร้าเรื้อรัง
- Normal aging ยังใช้ชีวิตประจำวันได้''',
            pearl="หลาย domain + รบกวน ADL = dementia", topic="Definition",
            ref=[f"{D} หน้า 197, 220–221"], nl=["2.3.5-3(5)"]),
        mcq("NEURO-05-01-2",
            "A previously healthy 79-year-old woman has had forgetfulness for 8 months. She cannot remember where she keeps her money, forgets to turn off the stove, and once thought she was in someone else's house while at home. She is irritable and sleeps poorly. She is alert and attentive, but has impaired orientation to time, short- and long-term memory, calculation and language. What is the most likely diagnosis?",
            "Dementia",
            ["Normal age-related change", "Mild cognitive impairment", "Delirium", "Depression"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 222–223)",
            explain='''8 เดือน ค่อยเป็นค่อยไป เสียหลาย domain (memory, executive — ลืมปิดเตา, language, calculation) และ **รบกวนชีวิต/ความปลอดภัย** โดย mental status/attention ปกติ = **dementia**
- Normal aging ไม่ทำให้หลงว่าอยู่บ้านคนอื่นหรือลืมปิดเตาจนอันตราย
- MCI ไม่รบกวน ADL
- Delirium ต้องเฉียบพลันและ attention เสีย — ที่นี่ alert attentive
- Depression (pseudodementia) จะมีอารมณ์เศร้านำ หงุดหงิดและนอนไม่ดีเป็น BPSD ได้''',
            pearl="ลืมปิดเตา/ของมีค่า + หลายเดือน + attention ปกติ = dementia", topic="Dementia vs others",
            ref=[f"{D} หน้า 192, 195, 222–223"], nl=["2.3.5-3(5)"]),
        mcq("NEURO-05-01-3",
            "A 70-year-old man with diabetes has had progressive forgetfulness for 6 months. He misplaces his glasses in the kitchen cupboard and accuses his son of stealing his money. At night he cannot sleep and searches through his belongings; he speaks little and suspects his wife of infidelity. He is disoriented to place and person with impaired short- and long-term memory and calculation. There is no focal neurological deficit or parkinsonism. What is the most likely diagnosis?",
            "Alzheimer's disease",
            ["Age-related cognitive impairment", "Late-onset psychosis", "Vascular dementia", "Normal pressure hydrocephalus"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 224–225)",
            explain='''Dementia ค่อยเป็นค่อยไปที่เด่น **episodic memory** (วางของผิดที่แล้ว **โทษคนอื่นขโมย**) + delusion/BPSD + **neuro exam ปกติ** = **Alzheimer disease**
- Age-related cognitive change ไม่รบกวน ADL และไม่มี disorientation
- Late-onset psychosis จะมีอาการจิตเวชนำโดยไม่มี memory loss แบบนี้
- Vascular dementia ต้องมี stepwise/abrupt และ focal deficit — DM เป็นตัวหลอก
- NPH ต้องมี gait disturbance และ urinary incontinence''',
            pearl="ลืม + โทษคนอื่นขโมย + neuro exam ปกติ = AD", topic="Alzheimer disease",
            ref=[f"{D} หน้า 202–203, 224–225"], nl=["2.3.6-3(1)", "B3.2.8-3(1)"]),
        mcq("NEURO-05-01-4",
            "A 72-year-old man has had 9 months of fluctuating confusion and vivid visual hallucinations of children in his room. His wife reports he shouts and kicks during dreams. Examination shows mild bradykinesia and rigidity that began around the same time as the cognitive symptoms. He developed severe rigidity after a single dose of haloperidol. What is the most likely diagnosis?",
            "Dementia with Lewy bodies",
            ["Parkinson's disease dementia", "Alzheimer's disease", "Frontotemporal dementia", "Vascular dementia"],
            explain='''**Visual hallucination ตั้งแต่ต้น** + **parkinsonism เกิดพร้อม/ภายใน 1 ปีของ cognitive decline** + fluctuation + **REM sleep behavior disorder** + ไวต่อ antipsychotic = **DLB**
- Parkinson disease dementia ต้องมี parkinsonism นำ **> 1 ปี** ก่อนสมองเสื่อม
- Alzheimer ไม่มี parkinsonism และ hallucination มาระยะหลัง
- FTD เด่นพฤติกรรม/ภาษา
- Vascular dementia เด่น stepwise และ focal deficit''',
            pearl="VH + parkinsonism ภายใน 1 ปี + RBD = DLB", topic="DLB",
            ref=[f"{D} หน้า 202, 204–206"], nl=["2.3.5-3(5)"]),
        mcq("NEURO-05-01-5",
            "A 58-year-old man has had 1 year of personality change. He makes sexually inappropriate jokes to strangers, eats excessively, spends money impulsively and seems indifferent to his family. Memory and visuospatial skills are relatively preserved. Neurological examination is normal. What is the most likely diagnosis?",
            "Behavioral variant frontotemporal dementia",
            ["Alzheimer's disease", "Dementia with Lewy bodies", "Vascular dementia", "Pseudodementia"],
            explain='''อายุค่อนข้างน้อย + **พฤติกรรม/บุคลิกเปลี่ยนนำ (disinhibition, apathy, hyperorality)** ขณะความจำยังดี = **behavioral variant FTD** (ชนิดที่พบบ่อยสุดของ FTD ตามสไลด์)
- Alzheimer เด่นความจำ (episodic memory) ตั้งแต่แรก
- DLB มี visual hallucination และ parkinsonism
- Vascular dementia มี stepwise และ focal deficit
- Pseudodementia จะมีอารมณ์เศร้านำ ไม่ใช่ disinhibition''',
            pearl="พฤติกรรมเปลี่ยนนำ ความจำดี = FTD", topic="FTD",
            ref=[f"{D} หน้า 202, 204"], nl=["2.3.5-3(5)"]),
    ])

# ---------------------------------------------------------------- 05-02 Reversible: NPH & Wernicke
S2 = sec("neuro-05-02", "Reversible dementia: NPH & Wernicke–Korsakoff",
    "NPH: gait + dementia + incontinence · ventriculomegaly · LP OP ปกติ เดินดีขึ้นหลังระบาย CSF → shunt · Wernicke: confusion + ophthalmoplegia + ataxia → IV thiamine ก่อน glucose · Korsakoff: memory loss + confabulation", minutes=8,
    source=f"{D} หน้า 199–201, 210–219", nl=["B3.2.8-3(3)", "B3.2.5(2)", "2.3.6(6)"],
    md='''
### Potentially reversible dementia

ตรวจหาเสมอ (เสริม — สไลด์เป็นภาพ): **TSH, B12, folate**, electrolyte, Ca, glucose, LFT, BUN/Cr, **VDRL/HIV** ตามความเสี่ยง, **CT/MRI brain** (NPH, subdural hematoma, tumor), ทบทวนยา (anticholinergic, sedative), depression

### Normal pressure hydrocephalus (NPH)

- ↓CSF absorption · สาเหตุ: **idiopathic**, หลัง meningitis, SAH, IVH
- **Triad: gait disorder + dementia + urinary incontinence** ("wobbly, wacky, wet" — เสริม) · gait มักนำ (magnetic gait, ก้าวสั้น ฐานกว้าง)
- **CT/MRI: ventriculomegaly** (ไม่สมสัดส่วนกับ atrophy — DESH)
- **LP (confirm)**: OP **ปกติหรือสูงเล็กน้อย** + **เดินดีขึ้นหลังระบาย CSF** (tap test)
- **Tx: ventricular shunt** (VP shunt)

### Wernicke–Korsakoff

- สาเหตุ: **ขาด thiamine (vitamin B1) รุนแรง** — chronic alcoholism, ขาดอาหาร (อาเจียนนาน, bariatric — เสริม)

| | Wernicke encephalopathy | Korsakoff syndrome |
|---|---|---|
| ระยะ | **Acute, reversible** | **Chronic, irreversible** |
| อาการ | **Confusion, ophthalmoplegia/nystagmus, gait ataxia** | **Memory loss (anterograde), confabulation** (สร้างเรื่องแทนความจำที่หาย), personality change, hallucination |
| รักษา | **IV thiamine** (เช่น 200–500 mg IV tid — เสริม) | Oral thiamine ป้องกันการลุกลาม |

> ผู้ป่วยติดสุรา/ขาดอาหาร **ต้องให้ thiamine ก่อน IV glucose** — glucose ใช้ thiamine เป็น cofactor จะกระตุ้นให้เกิด Wernicke

- Triad ครบเพียงส่วนน้อย — สงสัยเมื่อมีอย่างใดอย่างหนึ่งในคนเสี่ยง (เสริม)
- Thiamine deficiency ทำ **peripheral neuropathy (dry beriberi)** และ **high-output HF (wet beriberi)** ได้ด้วย (ดูหมวด peripheral nerve)
''',
    pearls=[
        "NPH = เดินลำบาก + สมองเสื่อม + ปัสสาวะราด + ventriculomegaly",
        "NPH ยืนยันด้วย LP tap test (OP ปกติ เดินดีขึ้น) → VP shunt",
        "Wernicke = confusion + ophthalmoplegia/nystagmus + ataxia → IV thiamine",
        "Korsakoff = memory loss + confabulation (irreversible)",
        "คนติดสุรา: thiamine ก่อน glucose",
    ],
    items=[
        mcq("NEURO-05-02-1",
            "A 50-year-old man has had 1 month of memory loss, making up exaggerated stories, and difficulty walking. BT 37.5°C, PR 80/min, BP 140/70 mmHg. He is alert, with nystagmus, limited extraocular movements, gait ataxia, and decreased pinprick sensation in a glove-and-stocking distribution. What is the most appropriate management?",
            "Thiamine",
            ["Lorazepam", "Diazepam", "Haloperidol", "Sodium valproate"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 210–211)",
            explain='''Nystagmus/ophthalmoplegia + ataxia (**Wernicke**) + memory loss + **confabulation** (**Korsakoff**) + polyneuropathy (dry beriberi) = **thiamine deficiency** → **thiamine** (สไลด์เฉลย Wernicke acute + Korsakoff chronic)
- Lorazepam และ diazepam ใช้ใน alcohol withdrawal (สั่น เหงื่อ ชัก) ซึ่งไม่ใช่ภาพนี้
- Haloperidol ควบคุมอาการก้าวร้าว/โรคจิต ไม่รักษาสาเหตุ
- Valproate เป็นยากันชัก''',
            pearl="Ophthalmoplegia + ataxia + confabulation = thiamine", topic="Wernicke–Korsakoff",
            ref=[f"{D} หน้า 201, 210–211"], nl=["B3.2.5(2)", "2.3.6(6)"]),
        mcq("NEURO-05-02-2",
            "A 40-year-old man has been confused for 2 days. He has drunk a bottle of liquor almost daily since age 30; his last drink was this morning. Vital signs are stable without tremor or sweating. He has parotid enlargement, is disoriented to time, place and person, and has nystagmus and ataxia. What is the most likely diagnosis?",
            "Wernicke encephalopathy",
            ["Delirium tremens", "Alcohol withdrawal syndrome", "Chronic subdural hematoma", "Hepatic encephalopathy"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 212–213)",
            explain='''ดื่มสุราเรื้อรัง + **confusion + nystagmus (ophthalmoplegia) + ataxia** = **Wernicke encephalopathy** → IV thiamine (สไลด์) — เติมในโจทย์ว่ายังดื่มเมื่อเช้า และไม่มีสั่น/เหงื่อ เพื่อตัด withdrawal ออก
- Delirium tremens เกิด 48–96 ชม. หลังหยุดดื่ม มี autonomic hyperactivity (ชีพจรเร็ว ไข้ เหงื่อ) และ hallucination
- Alcohol withdrawal syndrome ต้องหยุดหรือลดการดื่ม มีสั่น เหงื่อ
- Chronic SDH ทำให้สับสนและอาจ focal deficit แต่ไม่ให้ nystagmus + ataxia คู่กัน
- Hepatic encephalopathy มี asterixis ไม่ใช่ nystagmus (ตัวลวง "delirium" เดิมถูกเปลี่ยนให้ชัด)''',
            pearl="ติดสุรา + สับสน + nystagmus + ataxia = Wernicke", topic="Wernicke encephalopathy",
            ref=[f"{D} หน้า 201, 212–215"], nl=["B3.2.5(2)", "2.3.5(1)"]),
        mcq("NEURO-05-02-3",
            "A 60-year-old man has memory impairment, gait disturbance and urinary incontinence. There are no cranial nerve deficits or weakness; he has increased tone in both legs and generalized hyperreflexia. MMSE shows a mild cognitive deficit. What will most likely be found on his CT scan?",
            "Hydrocephalus",
            ["Multiple infarctions", "Frontal lobe tumor", "Diffuse brain atrophy", "Frontotemporal atrophy"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 216–217)",
            explain='''**Triad: dementia + gait disorder + urinary incontinence** = **normal pressure hydrocephalus** → CT/MRI เห็น **ventriculomegaly (hydrocephalus)** (สไลด์)
- Multiple infarctions (vascular dementia) มี stepwise และ focal deficit
- Frontal lobe tumor อาจให้ incontinence และพฤติกรรมเปลี่ยน แต่โจทย์คลาสสิกของ triad คือ NPH
- Diffuse atrophy พบใน AD ซึ่งไม่มี gait และ incontinence ระยะแรก
- Frontotemporal atrophy ใน FTD เด่นพฤติกรรม''',
            pearl="Gait + dementia + incontinence = NPH → ventriculomegaly", topic="NPH",
            ref=[f"{D} หน้า 200, 216–217"], nl=["B3.2.8-3(3)", "2.3.6-3(5)"]),
        mcq("NEURO-05-02-4",
            "A 75-year-old man has progressive difficulty walking, urinary incontinence and memory loss. TMSE is 23/30. He has a broad-based, slow gait without focal deficits. Other laboratory tests are normal. Non-contrast CT shows ventriculomegaly with disproportionately enlarged subarachnoid spaces. Which test best confirms the diagnosis and predicts response to treatment?",
            "Lumbar puncture with CSF removal (tap test)",
            ["MRI brain", "Electroencephalography", "MRI of the lumbosacral spine", "CT brain with contrast"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 218–219)",
            explain='''NPH ยืนยันด้วย **LP**: OP ปกติ/สูงเล็กน้อย และ **เดินดีขึ้นหลังระบาย CSF** ซึ่งทำนายว่าจะตอบสนองต่อ **ventricular shunt** (สไลด์: LP confirm)
- MRI brain ให้ภาพละเอียดขึ้นแต่ไม่ยืนยันการตอบสนองต่อการระบาย CSF
- EEG ไม่ช่วย
- MRI L-S spine ใช้เมื่อสงสัย cauda equina/spinal stenosis
- CT with contrast ไม่เพิ่มข้อมูลสำหรับ NPH''',
            pearl="NPH: LP tap test ยืนยัน → VP shunt", topic="NPH confirmation",
            ref=[f"{D} หน้า 200, 218–219"], nl=["B3.2.8-3(3)"]),
    ])

# ---------------------------------------------------------------- 05-03 Treatment of dementia
S3 = sec("neuro-05-03", "Dementia management",
    "1st line: cholinesterase inhibitor (donepezil, rivastigmine, galantamine) และ memantine · BPSD: non-drug ก่อน · เลี่ยง benzodiazepine/haloperidol (โดยเฉพาะ DLB)", minutes=5,
    source=f"{D} หน้า 206–207, 226–229", nl=["B3.2.8-3(1)", "B3.4(4)"],
    md='''
### ยาหลัก (สไลด์)

| กลุ่ม | ยา | หมายเหตุ |
|---|---|---|
| **Cholinesterase inhibitor (1st line)** | **Donepezil, rivastigmine, galantamine** | Mild–moderate AD, DLB, PDD · S/E: N/V/diarrhea, **bradycardia**, ฝันร้าย (เสริม) |
| **NMDA receptor antagonist (1st line)** | **Memantine** | Moderate–severe AD, ใช้ร่วม ChEI ได้ |
| อื่น ๆ | Vitamin E, Ginkgo biloba extract (EGb 761) | หลักฐานน้อย ไม่ใช่ยาหลัก |

### BPSD (เสริม)

- หาสาเหตุกระตุ้นก่อน (ปวด ติดเชื้อ ท้องผูก ยา สิ่งแวดล้อม)
- **Non-pharmacologic** ก่อน: กิจวัตรสม่ำเสมอ แสงสว่าง ลดสิ่งกระตุ้น
- ChEI ช่วย hallucination/apathy ได้ โดยเฉพาะ **DLB**
- ถ้ารุนแรงจนอันตราย → **atypical antipsychotic ขนาดต่ำระยะสั้น** (quetiapine) · **เลี่ยง haloperidol** (โดยเฉพาะ DLB, PDD) และ **benzodiazepine** (สับสน หกล้ม)

> โจทย์ AD ที่มี hallucination/โวยวาย แต่ยังไม่เคยได้ยาเฉพาะ → ตอบ **donepezil** (รักษาโรคหลัก) มากกว่า diazepam หรือ haloperidol
''',
    pearls=[
        "Dementia 1st line: donepezil/rivastigmine/galantamine หรือ memantine",
        "ChEI ระวัง bradycardia",
        "BPSD: แก้สาเหตุ + non-drug ก่อน",
        "เลี่ยง benzodiazepine และ haloperidol ในผู้ป่วยสมองเสื่อม (โดยเฉพาะ DLB)",
    ],
    items=[
        mcq("NEURO-05-03-1",
            "A 79-year-old man has had forgetfulness for 5 years. He no longer recognizes his children, becomes agitated, sleeps poorly and sees hallucinations of his deceased wife. He is disoriented with impaired short- and long-term memory, calculation and language. He has not received any treatment. What is the most appropriate treatment?",
            "Donepezil",
            ["Vitamin E", "Ginkgo biloba", "Diazepam", "Haloperidol"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 228–229)",
            explain='''AD ระยะปานกลาง–รุนแรงที่ยังไม่เคยได้ยา + BPSD → เริ่ม **cholinesterase inhibitor (donepezil)** ซึ่งเป็น 1st line และช่วย hallucination/agitation ได้บางส่วน (เฉลยในสไลด์เป็นภาพ — ตอบตามแนวทาง)
- Vitamin E และ ginkgo หลักฐานน้อย ไม่ใช่ยาหลัก
- Diazepam ทำให้สับสนมากขึ้นและหกล้ม
- Haloperidol ใช้ระยะสั้นเมื่ออันตรายเท่านั้น เสี่ยง EPS และเพิ่มอัตราตายในผู้สูงอายุสมองเสื่อม''',
            pearl="AD ที่ยังไม่ได้ยา → donepezil", topic="Dementia drug",
            ref=[f"{D} หน้า 207, 228–229"], nl=["B3.2.8-3(1)", "B3.4(4)"]),
        mcq("NEURO-05-03-2",
            "An elderly woman cannot perform activities of daily living by herself; she needs a caregiver to bathe her. At night she becomes disoriented to time and place. On cognitive testing she cannot recall 3 words or copy a drawing. These problems have progressed gradually over several years. What is the most likely diagnosis?",
            "Alzheimer's disease",
            ["Delirium", "Korsakoff syndrome", "Mild cognitive impairment", "Normal pressure hydrocephalus"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 226–227)",
            explain='''ค่อยเป็นค่อยไปหลายปี + **ต้องพึ่งพาผู้อื่นใน ADL** + ความจำ (จำ 3 คำไม่ได้) + visuospatial (วาดรูปไม่ได้) = **dementia ชนิด Alzheimer** · สับสนกลางคืน (sundowning) เป็น BPSD ได้ (เติม "หลายปี" ในโจทย์เพื่อแยก delirium)
- Delirium เฉียบพลันและมีสาเหตุทางกาย
- Korsakoff ต้องมีประวัติสุรา/ขาด thiamine และ confabulation
- MCI ไม่รบกวน ADL
- NPH ต้องมี gait และ incontinence''',
            pearl="ADL เสีย + ความจำ + visuospatial ค่อยเป็น = AD", topic="AD",
            ref=[f"{D} หน้า 203, 226–227"], nl=["2.3.6-3(1)"]),
        mcq("NEURO-05-03-3",
            "A 76-year-old woman with moderate Alzheimer's disease is started on donepezil. Three weeks later she reports dizziness and has a near-syncopal episode. Which adverse effect of the drug most likely explains this?",
            "Bradycardia from increased vagal tone",
            ["Orthostatic hypotension from alpha-blockade", "Hypoglycemia", "QT prolongation with torsades de pointes as the usual effect", "Anticholinergic tachycardia"],
            explain='''Cholinesterase inhibitor เพิ่ม acetylcholine → **vagal tone ↑ → bradycardia, AV block, syncope** (เสริม) — ควรตรวจชีพจร/EKG ก่อนและระหว่างให้ยา
- Alpha-blockade เป็นกลไกของ prazosin/บาง antipsychotic ไม่ใช่ donepezil
- Donepezil ไม่ทำให้น้ำตาลต่ำ
- QT prolongation มีรายงานได้แต่ไม่ใช่ผลข้างเคียงหลัก
- Anticholinergic tachycardia เป็นผลตรงข้ามกับกลไกของยา''',
            pearl="ChEI → bradycardia/syncope", topic="ChEI adverse effect",
            ref=[f"{D} หน้า 207"], nl=["B3.4(4)"]),
    ])

LECTURE = lecture("05", "Dementia", "approach · ชนิด · NPH · Wernicke–Korsakoff · การรักษา",
    objectives=[
        "แยก dementia จาก normal aging, MCI, delirium และ depression ได้",
        "บอกชนิด dementia (AD, VaD, DLB, PDD, FTD) จากอาการเด่นได้",
        "วินิจฉัยและรักษา NPH และ Wernicke–Korsakoff ได้",
        "เลือกยารักษา dementia และหลักการดูแล BPSD ได้",
    ],
    sections=[S1, S2, S3])
