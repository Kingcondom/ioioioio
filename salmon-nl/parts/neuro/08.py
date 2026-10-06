from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Neuro"

# ---------------------------------------------------------------- 08-01 Tension-type headache (+ comparison figure)
F_PH = fig("neuro-08-01-f1", "Primary headache 3 ชนิด: ตำแหน่ง ระยะเวลา และยา", '''<svg viewBox="0 0 740 420">
 <ellipse cx="125" cy="110" rx="70" ry="80" class="box"/>
 <path d="M58 92Q125 70 192 92L192 116Q125 94 58 116Z" class="misssoft"/>
 <text x="125" y="216" text-anchor="middle" class="tb">Tension-type</text>
 <text x="125" y="236" text-anchor="middle" class="t3">band-like สองข้าง บีบรัด</text>
 <ellipse cx="370" cy="110" rx="70" ry="80" class="box"/>
 <path d="M370 30A70 80 0 0 1 370 190Z" class="c1soft"/>
 <text x="370" y="216" text-anchor="middle" class="tb">Migraine</text>
 <text x="370" y="236" text-anchor="middle" class="t3">ข้างเดียว &gt; สองข้าง ตุบ ๆ</text>
 <ellipse cx="615" cy="110" rx="70" ry="80" class="box"/>
 <circle cx="645" cy="100" r="20" class="badsoft"/>
 <circle cx="645" cy="100" r="5" class="bad"/>
 <text x="615" y="216" text-anchor="middle" class="tb">Cluster</text>
 <text x="615" y="236" text-anchor="middle" class="t3">รอบตาข้างเดียว แทง/แสบ</text>
 <text x="20" y="270" class="tb">ระยะเวลา</text>
 <path d="M120 262H720" class="ln"/>
 <text x="120" y="282" text-anchor="middle" class="t3">นาที</text>
 <text x="400" y="282" text-anchor="middle" class="t3">ชั่วโมง</text>
 <text x="700" y="282" text-anchor="middle" class="t3">วัน</text>
 <rect x="140" y="292" width="200" height="22" rx="6" class="bad"/>
 <text x="240" y="308" text-anchor="middle" class="tw">Cluster 15 นาที–3 ชม.</text>
 <rect x="360" y="320" width="320" height="22" rx="6" class="c1"/>
 <text x="520" y="336" text-anchor="middle" class="tw">Migraine 4–72 ชม.</text>
 <rect x="160" y="348" width="560" height="22" rx="6" class="miss"/>
 <text x="440" y="364" text-anchor="middle" class="tw">Tension: variable (30 นาที–7 วัน)</text>
 <rect x="20" y="380" width="700" height="34" rx="8" class="sunk"/>
 <text x="30" y="402" class="t2"><tspan class="tb">Abortive:</tspan> paracetamol/NSAID · triptan · 100% O2</text>
 <text x="400" y="402" class="t2"><tspan class="tb">Prophylaxis:</tspan> amitriptyline · β-blocker · verapamil</text>
</svg>''', "บน: บริเวณที่ปวดของแต่ละชนิด (แรเงา) · กลาง: ช่วงเวลาที่ปวดต่อครั้ง · ล่าง: ยาฉุกเฉินและยาป้องกันเรียงตามลำดับ tension / migraine / cluster")

S1 = sec("neuro-08-01", "Tension-type headache",
    "Band-like บีบรัดสองข้าง ไม่มีอาการร่วม (ไม่แพ้แสง/เสียง ไม่อาเจียน) · pericranial tenderness · abortive paracetamol/NSAID · prophylaxis amitriptyline", minutes=7,
    source=f"{D} หน้า 295–296, 302–312", nl=["B3.2.7(2)", "2.3.6(8)", "2.1.3"],
    md='''
### ภาพรวม primary headache

[[fig:neuro-08-01-f1]]

| | Tension | Migraine | Cluster |
|---|---|---|---|
| Duration | Variable | **4–72 ชม.** | **15 นาที – 3 ชม.** |
| Location | **Band-like** | Unilateral > bilateral | **Unilateral, periorbital** |
| Character | **Dull, pressure** | **Throbbing** | Stab-like |
| อาการร่วม | **ไม่มี** | Photophobia, phonophobia, N/V ± aura | **Autonomic** (น้ำตา น้ำมูก Horner) |
| Abortive | NSAIDs, paracetamol | NSAIDs, **triptans**, ergot, metoclopramide | **100% O2** |
| Prophylaxis | **Amitriptyline** | **β-blocker** (และอื่น ๆ) | **Verapamil** |

### Tension-type headache (สไลด์)

- Trigger: **ความเหนื่อยล้า เครียด อดนอน**
- **Dull, pressure, band-like, bitemporal** (หน้าผาก ขมับ ท้ายทอย รอบศีรษะ)
- **Pericranial muscle tenderness**, myofascial trigger points (บ่า ต้นคอ)
- Duration variable · **ไม่มีอาการร่วม** (ไม่ตุบ ๆ ไม่อาเจียน ไม่แพ้แสง/เสียง — อาจมีอย่างใดอย่างหนึ่งเล็กน้อย — เสริม) · ไม่แย่ลงจากกิจกรรม
- **Abortive: paracetamol, NSAID**
- **Prophylaxis: amitriptyline** — เมื่อปวดบ่อย (chronic ≥ 15 วัน/เดือน หรือ episodic บ่อย — เสริม) หรือยาแก้ปวดไม่ได้ผล

> ระวัง **medication-overuse headache** ถ้ากินยาแก้ปวด ≥ 10–15 วัน/เดือน (เสริม)
''',
    figs=[F_PH],
    pearls=[
        "Tension: band-like บีบรัดสองข้าง ไม่มีอาการร่วม",
        "Pericranial muscle tenderness ช่วยวินิจฉัย",
        "Abortive: paracetamol/NSAID · prophylaxis: amitriptyline",
        "Migraine 4–72 ชม. · cluster 15 นาที–3 ชม.",
    ],
    items=[
        mcq("NEURO-08-01-1",
            "A 28-year-old man has headaches with a tightening quality on both sides of his forehead. He denies photophobia or phonophobia. Examination shows pericranial muscle tenderness. What is the most likely diagnosis?",
            "Tension-type headache",
            ["Migraine headache", "Cluster headache", "Trigeminal neuralgia", "Venous sinus thrombosis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 303–304)",
            explain='''ปวด **บีบรัด (tightening) สองข้าง** + **ไม่มี photophobia/phonophobia** + **pericranial muscle tenderness** = **tension-type headache**
- Migraine ปวดตุบ ๆ มักข้างเดียว มี N/V แพ้แสง/เสียง
- Cluster ปวดรอบตาข้างเดียวรุนแรง มีน้ำตาน้ำมูก
- Trigeminal neuralgia ปวดแปล๊บที่หน้าเป็นวินาที
- VST ปวดใหม่ มี ↑ICP ชัก ในคนมี hypercoagulable state''',
            pearl="บีบรัดสองข้าง + ไม่มีอาการร่วม = tension", topic="TTH diagnosis",
            ref=[f"{D} หน้า 296, 303–304"], nl=["B3.2.7(2)"]),
        mcq("NEURO-08-01-2",
            "A 31-year-old woman has chronic mild-to-moderate headache with a diffuse band-like quality. She has no photophobia, no phonophobia and no neurological deficits. Ibuprofen improves the pain but does not fully relieve it. What is the most likely diagnosis?",
            "Tension-type headache",
            ["Migraine", "Cluster headache", "Brain tumor", "Trigeminal neuralgia"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 305–306)",
            explain='''Band-like กระจาย ปวดเล็กน้อย–ปานกลาง ไม่มีอาการร่วม ไม่มี deficit = **tension-type headache**
- Migraine ต้องมีอาการร่วม (N/V, photo/phonophobia)
- Cluster รุนแรงมาก รอบตา มี autonomic symptom
- Brain tumor ต้องมี red flag (ปวดเช้า อาเจียน papilledema focal deficit)
- Trigeminal neuralgia เป็นปวดแปล๊บที่หน้า''',
            pearl="Chronic band-like ไม่มี red flag = tension", topic="TTH diagnosis",
            ref=[f"{D} หน้า 296, 305–306"], nl=["B3.2.7(2)"]),
        mcq("NEURO-08-01-3",
            "A 35-year-old man has had intermittent mild-to-moderate headache for 3 months, 2–3 times per week, mostly at the end of the day and improved by rest. The pain is bitemporal, occipital or affects the whole head. What is the most appropriate management?",
            "Paracetamol",
            ["Alprazolam", "Ergotamine plus caffeine", "Sumatriptan", "Tramadol"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 307–308)",
            explain='''Tension-type headache (ปลายวัน ดีขึ้นเมื่อพัก รอบศีรษะ) → **abortive: paracetamol** (หรือ NSAID) ตามสไลด์
- Alprazolam ไม่ใช่ยารักษาปวดหัวและติดได้
- Ergotamine + caffeine และ sumatriptan เป็นยา migraine
- Tramadol (opioid) เสี่ยง medication-overuse headache และติดยา (ตัวเลือก etoricoxib เดิมถูกเปลี่ยนเพื่อให้มีคำตอบเดียว — NSAID ก็ใช้ได้ใน TTH)''',
            pearl="TTH abortive = paracetamol/NSAID", topic="TTH abortive",
            ref=[f"{D} หน้า 296, 307–308"], nl=["B3.2.7(2)", "B3.4(7)"]),
        mcq("NEURO-08-01-4",
            "A 40-year-old accountant has had off-and-on headaches for 5 years, usually in the afternoon, mild to moderate in intensity, like a tight band around her head, sometimes radiating to the neck and shoulders. Paracetamol is no longer effective. Examination is unremarkable. What is the most appropriate management?",
            "Amitriptyline",
            ["Flunarizine", "Propranolol", "Tramadol", "Topiramate"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 309–310)",
            explain='''Chronic **tension-type headache** ที่ยาแก้ปวดไม่ได้ผล → **prophylaxis: amitriptyline** (สไลด์)
- Flunarizine, propranolol และ topiramate เป็นยาป้องกัน **migraine**
- Tramadol ไม่ใช่ยาป้องกัน และเสี่ยงติดยา/medication-overuse''',
            pearl="TTH เรื้อรัง → amitriptyline", topic="TTH prophylaxis",
            ref=[f"{D} หน้า 296, 309–310"], nl=["B3.2.7(2)"]),
        mcq("NEURO-08-01-5",
            "A 30-year-old woman has had intermittent bilateral dull pain and tightness around the forehead for 2 months. There is no nausea or photophobia. Each headache lasts about 6 hours and occurs twice a week. Neurological examination is normal. What is the most appropriate preventive medication?",
            "Amitriptyline",
            ["Fluoxetine", "Ibuprofen", "Alprazolam", "Propranolol"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 311–312)",
            explain='''Tension-type headache (สองข้าง ตื้อ บีบรัด ไม่มีอาการร่วม) ที่ต้องการ **ป้องกัน** → **amitriptyline**
- Fluoxetine (SSRI) ไม่ได้ผลดีในการป้องกัน TTH
- Ibuprofen เป็นยา abortive ไม่ใช่ยาป้องกัน
- Alprazolam ไม่ใช่ยาป้องกันปวดหัว
- Propranolol เป็นยาป้องกัน migraine''',
            pearl="ป้องกัน tension headache = amitriptyline", topic="TTH prophylaxis",
            ref=[f"{D} หน้า 296, 311–312"], nl=["B3.2.7(2)"]),
    ])

# ---------------------------------------------------------------- 08-02 Migraine
S2 = sec("neuro-08-02", "Migraine",
    "หญิง > ชาย · ตุบ ๆ ข้างเดียว 4–72 ชม. + N/V photo/phonophobia ± aura · mild NSAID ± metoclopramide · severe triptan · ergotamine 2nd (vasoconstriction, CYP3A4) · prophylaxis propranolol, amitriptyline, flunarizine, VPA/topiramate", minutes=9,
    source=f"{D} หน้า 297–299, 302, 315–324", nl=["B3.2.7(3)", "2.3.6(4)", "B3.4(7)"],
    md='''
### อาการ (สไลด์)

- **Female > male**
- Trigger: **แอลกอฮอล์, dairy, ช็อกโกแลต, อดอาหาร, เครียด, อดนอน, ประจำเดือน, OCP**
- **± Aura** เช่น **scintillating scotoma** (แสงวิบวับขยายออก — fully reversible ภายใน 5–60 นาที — เสริม)
- **Unilateral > bilateral, throbbing**, **4–72 ชม.**
- **N/V, photophobia, phonophobia** · แย่ลงเมื่อเคลื่อนไหว ดีขึ้นในห้องมืดเงียบ

### Abortive treatment

| ความรุนแรง | ยา |
|---|---|
| **Mild–moderate** | **NSAID ± metoclopramide** |
| **Severe (รบกวนชีวิตประจำวัน)** | **Triptans (1st line) ± metoclopramide** |
| 2nd line | **Ergotamine** |

- **Ergotamine S/E: vasoconstriction** → MI, limb/bowel ischemia (**ergotism**) — เสี่ยงมากเมื่อใช้ร่วม **CYP3A4 inhibitor** (**ritonavir**, clarithromycin, azole) (เสริม)
- ห้าม triptan/ergot ใน CAD, stroke, uncontrolled HT, ตั้งครรภ์ (เสริม)

### Prophylaxis

- ให้เมื่อปวดบ่อย/รุนแรงรบกวนชีวิต (เช่น ≥ 4 วันต่อเดือน หรือยา abortive ไม่ได้ผล — เสริม)
- **β-blocker: propranolol, metoprolol**
- **TCA: amitriptyline**
- **CCB: verapamil, flunarizine**
- **Anticonvulsant: valproate, topiramate**
- เลือกตามโรคร่วม (เสริม): HT/ใจสั่น → propranolol · นอนไม่หลับ/ซึมเศร้า/TTH ร่วม → amitriptyline · อ้วน → topiramate · **asthma ห้าม propranolol** · หญิงวัยเจริญพันธุ์เลี่ยง valproate

> Migraine ที่ปวดรุนแรงจนต้องหยุดงานและ **เป็นเกือบทุกสัปดาห์** → ต้องให้ **ทั้ง abortive (triptan) และ prophylaxis**
''',
    pearls=[
        "Migraine: ตุบ ๆ ข้างเดียว 4–72 ชม. + N/V + แพ้แสงเสียง ± aura",
        "Mild: NSAID ± metoclopramide · severe: triptan",
        "Ergotamine + ritonavir → ergotism (limb ischemia)",
        "Prophylaxis: propranolol, amitriptyline, flunarizine/verapamil, VPA/topiramate",
        "ปวดบ่อยรบกวนชีวิต → abortive + prophylaxis",
    ],
    items=[
        mcq("NEURO-08-02-1",
            "A 31-year-old woman has a throbbing right-sided headache with nausea and vomiting that began 8 hours ago. Before the pain started she saw a bright flickering light that progressively expanded and made it hard to see, lasting about 20 minutes. Sitting in a quiet dark room improves her symptoms. What is the most likely diagnosis?",
            "Migraine with aura",
            ["Cluster headache", "Tension-type headache", "Trigeminal neuralgia", "Transient ischemic attack"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 315–316)",
            explain='''**Scintillating scotoma** ที่ขยายออก (aura) ตามด้วยปวด **ตุบ ๆ ข้างเดียว** + N/V + ดีขึ้นในห้อง **มืดเงียบ** (photo/phonophobia) = **migraine with aura**
- Cluster ปวดรอบตาสั้นกว่า (≤ 3 ชม.) มีน้ำตาน้ำมูก และผู้ป่วยกระสับกระส่ายเดินไปมา
- Tension ไม่มี aura และ N/V
- Trigeminal neuralgia เป็นวินาที
- TIA ทำให้สูญเสียการมองเห็นแบบ negative (มืด) ทันที ไม่ใช่ positive phenomenon ที่ค่อย ๆ ขยาย และไม่ตามด้วยปวดหัวแบบนี้''',
            pearl="แสงวิบวับขยายออก → ปวดตุบ ๆ ข้างเดียว = migraine with aura", topic="Migraine diagnosis",
            ref=[f"{D} หน้า 297, 315–316"], nl=["B3.2.7(3)"]),
        mcq("NEURO-08-02-2",
            "A 25-year-old woman has had intermittent severe headaches with photophobia and vomiting for 3 months. The pain is unilateral over the temporal and occipital regions, lasts 4–24 hours, and is aggravated by physical activity. Neurological examination is normal. She has not taken any medication. What is the most appropriate management?",
            "NSAIDs",
            ["Amlodipine", "ESR and CRP", "Lumbar puncture", "CT brain with contrast"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 317–318)",
            explain='''เข้าเกณฑ์ **migraine without aura** (ข้างเดียว 4–24 ชม. แย่ลงเมื่อเคลื่อนไหว photophobia อาเจียน) ไม่มี red flag → เริ่ม **abortive ด้วย NSAIDs (± metoclopramide)**; ถ้าไม่ได้ผลจึงใช้ triptan
- Amlodipine ไม่ใช่ยา migraine (CCB ที่ใช้ป้องกันคือ flunarizine/verapamil)
- ESR/CRP ใช้เมื่อสงสัย temporal arteritis ในผู้สูงอายุ
- LP และ CT ไม่จำเป็นเมื่อไม่มี red flag''',
            pearl="Migraine ไม่มี red flag → NSAID ก่อน", topic="Migraine abortive",
            ref=[f"{D} หน้า 298, 317–318"], nl=["B3.2.7(3)", "B3.4(7)"]),
        mcq("NEURO-08-02-3",
            "A 34-year-old woman has had headaches for 6 months: throbbing around the left eye and temple (occasionally right), lasting 6 hours to 2 days, occurring almost every week. During attacks she cannot go to work. Paracetamol gives only partial relief. What is the most appropriate management?",
            "Zolmitriptan for attacks plus amitriptyline for prevention",
            ["Naproxen alone", "Sumatriptan alone", "Ergotamine tartrate alone", "Ibuprofen plus propranolol"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 319–320)",
            explain='''Migraine **รุนแรง** (ทำงานไม่ได้) → abortive ด้วย **triptan** และ **ปวดเกือบทุกสัปดาห์** → ต้องเพิ่ม **prophylaxis** → **zolmitriptan + amitriptyline** (เฉลยในสไลด์เป็นภาพ — ตอบตามหลัก)
- Naproxen อย่างเดียวเหมาะกับ mild–moderate และไม่ได้ป้องกัน
- Sumatriptan อย่างเดียวรักษาเฉพาะ attack ไม่ลดความถี่
- Ergotamine เป็น 2nd line และไม่ได้ป้องกัน
- Ibuprofen + propranolol มี prophylaxis แต่ abortive เป็น NSAID ซึ่งไม่พอสำหรับ attack รุนแรงที่ paracetamol ไม่ได้ผล''',
            pearl="Migraine รุนแรง + บ่อย → triptan + prophylaxis", topic="Migraine abortive + prophylaxis",
            ref=[f"{D} หน้า 298–299, 319–320"], nl=["B3.2.7(3)", "B3.4(7)"]),
        mcq("NEURO-08-02-4",
            "A 30-year-old woman has had intermittent headaches for 3 months over the left frontal, orbital and temporal areas, each lasting about 6 hours with nausea, occurring 6–8 days per month and affecting her work. BMI 21 kg/m2. She also has difficulty falling asleep. There is no papilledema or neurological deficit. What is the most appropriate preventive medication?",
            "Amitriptyline",
            ["Triptan", "Ergotamine", "Ibuprofen", "Paracetamol"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 321–322)",
            explain='''Migraine ที่ต้องการ **ยาป้องกัน** → ในตัวเลือกมีเพียง **amitriptyline (TCA)** ที่เป็น prophylaxis และเหมาะกับคนนอนไม่หลับ (สไลด์เฉลย migraine prophylaxis: β-blocker, TCA, CCB, anticonvulsants — เติมความถี่และอาการนอนไม่หลับในโจทย์)
- Triptan และ ergotamine เป็น abortive
- Ibuprofen และ paracetamol เป็น abortive และใช้บ่อยเสี่ยง medication-overuse headache''',
            pearl="Migraine prophylaxis: propranolol / amitriptyline / flunarizine / VPA-topiramate", topic="Migraine prophylaxis",
            ref=[f"{D} หน้า 299, 321–322"], nl=["B3.2.7(3)"]),
        mcq("NEURO-08-02-5",
            "A 30-year-old woman with HIV infection on lopinavir/ritonavir and zidovudine took a medication for a migraine attack. Afterward she developed burning pain in her hands and feet. Examination shows pale, cold extremities with absent pulses in all four limbs. Which medication did she most likely take?",
            "Ergotamine",
            ["Celecoxib", "Tramadol", "Paracetamol", "Metoclopramide"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 323–324)",
            explain='''**Ergotamine** ทำให้หลอดเลือดหดตัว และ **ritonavir ยับยั้ง CYP3A4** ทำให้ระดับ ergotamine สูงมาก → **ergotism**: แขนขาขาดเลือด ซีด เย็น ชีพจรหาย ปวดแสบ (สไลด์: ergotamine S/E vasoconstriction — MI, limb/bowel ischemia)
- Celecoxib เพิ่มความเสี่ยง CV เล็กน้อย แต่ไม่ทำ vasospasm ทั่วตัว
- Tramadol เด่นเรื่อง serotonin syndrome/ชัก
- Paracetamol ไม่ทำให้หลอดเลือดหดตัว
- Metoclopramide ทำให้เกิด EPS''',
            pearl="Ergotamine + ritonavir = ergotism", topic="Ergotamine toxicity",
            ref=[f"{D} หน้า 298, 323–324"], nl=["B3.4(7)"]),
    ])

# ---------------------------------------------------------------- 08-03 Cluster headache
S3 = sec("neuro-08-03", "Cluster headache",
    "ชาย > หญิง · ปวดรอบตาข้างเดียวรุนแรงมาก 15 นาที–3 ชม. 1–8 ครั้ง/วัน + น้ำตา น้ำมูก ตาแดง Horner ข้างเดียวกัน · abortive 100% O2 7–10 L/min · prophylaxis verapamil", minutes=5,
    source=f"{D} หน้า 300–302, 313–314", nl=["2.1.3", "B3.4(7)"],
    md='''
### อาการ (สไลด์)

- **Male > female**
- **Unilateral, periorbital** ปวด **แสบ แทง รุนแรงมาก** (excruciating, piercing)
- **15 นาที – 3 ชม.** · **1–8 ครั้ง/วัน** · มักเป็นช่วงเวลาเดิมของวัน เป็นชุด (cluster) หลายสัปดาห์ (เสริม)
- **Ipsilateral autonomic symptoms**: **conjunctival injection, lacrimation, rhinorrhea, Horner (ptosis, miosis)**
- ผู้ป่วยกระสับกระส่าย เดินไปมา (ต่างจาก migraine ที่อยากนอนนิ่ง — เสริม) · แอลกอฮอล์กระตุ้น (เสริม)

### Treatment

| | ยา |
|---|---|
| **Abortive** | **100% O2 (1st line)** ทาง **non-rebreather mask 7–10 L/min นาน 15–20 นาที** · **triptans** (sumatriptan SC/intranasal — เสริม) |
| **Prophylaxis** | **Verapamil (1st line)** (ตรวจ EKG — เสริม) · steroid ระยะสั้นเป็น bridge (เสริม) |
''',
    pearls=[
        "Cluster: ชาย ปวดรอบตาข้างเดียว 15 นาที–3 ชม. + น้ำตาน้ำมูก Horner",
        "Abortive = 100% O2 NRB 7–10 L/min 15–20 นาที",
        "Prophylaxis = verapamil",
        "ผู้ป่วย cluster กระสับกระส่าย ต่างจาก migraine ที่นอนนิ่ง",
    ],
    items=[
        mcq("NEURO-08-03-1",
            "A 36-year-old man has recurrent bouts of severe, stabbing left periorbital pain. The current attack began 20 minutes ago; attacks have occurred daily for several weeks. During attacks he has tearing and a runny nose. Examination shows left miosis, ptosis and conjunctival injection. What is the most likely diagnosis?",
            "Cluster headache",
            ["Migraine headache", "Tension-type headache", "Trigeminal neuralgia", "Temporal arteritis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 313–314)",
            explain='''ชายวัยกลางคน + ปวด **รอบตาข้างเดียวรุนแรง** เป็นช่วงสั้น ๆ ทุกวันหลายสัปดาห์ + **autonomic symptoms ข้างเดียวกัน** (น้ำตา น้ำมูก ตาแดง **Horner**) = **cluster headache**
- Migraine นาน 4–72 ชม. N/V แพ้แสง ไม่มี Horner/น้ำตาข้างเดียว
- Tension ไม่มี autonomic symptom
- Trigeminal neuralgia ปวดเป็นวินาทีที่แก้ม/กราม
- Temporal arteritis พบในอายุ > 50 ปวดขมับ กดเจ็บ jaw claudication ESR สูง''',
            pearl="ปวดรอบตา + น้ำตาน้ำมูก + Horner = cluster", topic="Cluster diagnosis",
            ref=[f"{D} หน้า 300, 313–314"], nl=["2.1.3"]),
        mcq("NEURO-08-03-2",
            "A 32-year-old man presents to the ER during his third attack this week of excruciating right periorbital pain with ipsilateral lacrimation and nasal congestion, which began 10 minutes ago. He is pacing restlessly. Vital signs are normal. What is the most appropriate immediate treatment?",
            "100% oxygen via non-rebreather mask at 7–10 L/min for 15–20 minutes",
            ["Oral verapamil", "IV metoclopramide", "Oral ibuprofen", "Oral amitriptyline"],
            explain='''Cluster attack → **abortive: 100% O2 (1st line)** ทาง non-rebreather 7–10 L/min 15–20 นาที (หรือ triptan) ตามสไลด์
- Verapamil เป็น **prophylaxis** ออกฤทธิ์ช้า ไม่ใช้หยุด attack
- Metoclopramide ใช้ร่วมกับ migraine
- Ibuprofen ช้าเกินและไม่ได้ผลกับ cluster
- Amitriptyline เป็นยาป้องกัน tension/migraine''',
            pearl="Cluster attack → 100% O2", topic="Cluster abortive",
            ref=[f"{D} หน้า 301"], nl=["B3.4(7)"]),
        mcq("NEURO-08-03-3",
            "A 38-year-old man has had daily attacks of severe left periorbital headache with lacrimation and rhinorrhea for 2 weeks, similar to bouts he had last year. Oxygen therapy aborts individual attacks. EKG is normal. Which medication is the first-line preventive treatment?",
            "Verapamil",
            ["Propranolol", "Amitriptyline", "Topiramate", "Ergotamine"],
            explain='''Cluster headache **prophylaxis 1st line = verapamil** (สไลด์) — ตรวจ EKG ก่อนและระหว่างเพิ่มขนาด (เสริม)
- Propranolol, amitriptyline และ topiramate เป็นยาป้องกัน migraine/tension
- Ergotamine เป็น abortive และเสี่ยง vasoconstriction''',
            pearl="Cluster prophylaxis = verapamil", topic="Cluster prophylaxis",
            ref=[f"{D} หน้า 301–302"], nl=["B3.4(7)"]),
    ])

LECTURE = lecture("08", "Primary headache", "Tension-type · migraine · cluster",
    objectives=[
        "แยก tension, migraine และ cluster จากตำแหน่ง ระยะเวลา และอาการร่วมได้",
        "เลือก abortive treatment ตามชนิดและความรุนแรงได้",
        "เลือก prophylaxis ที่เหมาะสมกับโรคและโรคร่วมได้",
        "รู้ผลข้างเคียงและ interaction ของ ergotamine ได้",
    ],
    sections=[S1, S2, S3])
