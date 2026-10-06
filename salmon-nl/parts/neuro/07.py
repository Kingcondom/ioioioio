from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Neuro"

# ---------------------------------------------------------------- 07-01 Approach / SNOOP4
F_HA = fig("neuro-07-01-f1", "Approach to headache: SNOOP4 red flags → โรคที่ต้องนึกถึง", '''<svg viewBox="0 0 740 440">
 <defs><marker id="neuro-07-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="40" rx="10" class="acsoft"/>
 <text x="370" y="35" text-anchor="middle" class="tb">ปวดศีรษะ → มี red flag?</text>
 <path d="M320 50L170 80" class="ln" marker-end="url(#neuro-07-01-a)"/>
 <path d="M420 50L570 80" class="ln" marker-end="url(#neuro-07-01-a)"/>
 <rect x="10" y="82" width="340" height="346" rx="12" class="badsoft"/>
 <text x="180" y="106" text-anchor="middle" class="tb">มี (SNOOP4) → secondary headache</text>
 <text x="26" y="134" class="tb">S</text><text x="46" y="134" class="t2">Systemic: ไข้ น้ำหนักลด · HIV, มะเร็ง</text>
 <text x="46" y="152" class="t3">→ meningitis, brain abscess, metastasis</text>
 <text x="26" y="178" class="tb">N</text><text x="46" y="178" class="t2">Neurological deficit</text>
 <text x="46" y="196" class="t3">→ mass, stroke, VST</text>
 <text x="26" y="222" class="tb">O</text><text x="46" y="222" class="t2">Onset sudden (thunderclap)</text>
 <text x="46" y="240" class="t3">→ SAH, ICH</text>
 <text x="26" y="266" class="tb">O</text><text x="46" y="266" class="t2">Older &gt; 50 ปี เริ่มปวดใหม่</text>
 <text x="46" y="284" class="t3">→ mass, temporal arteritis</text>
 <text x="26" y="310" class="tb">P</text><text x="46" y="310" class="t2">Pattern change · Positional</text>
 <text x="26" y="332" class="tb">P</text><text x="46" y="332" class="t2">Precipitated by Valsalva/exertion</text>
 <text x="46" y="350" class="t3">→ posterior fossa lesion, Chiari</text>
 <text x="26" y="376" class="tb">P</text><text x="46" y="376" class="t2">Papilledema / ↑ICP</text>
 <text x="46" y="394" class="t3">→ mass, IIH, VST</text>
 <text x="26" y="418" class="tb">→ CT/MRI ± LP ตามสงสัย</text>
 <rect x="390" y="82" width="340" height="190" rx="12" class="oksoft"/>
 <text x="560" y="106" text-anchor="middle" class="tb">ไม่มี → primary headache</text>
 <text x="406" y="136" class="t2"><tspan class="tb">Tension:</tspan> band-like สองข้าง</text>
 <text x="406" y="158" class="t3">ไม่มีอาการร่วม</text>
 <text x="406" y="186" class="t2"><tspan class="tb">Migraine:</tspan> ตุบ ๆ ข้างเดียว 4–72 ชม.</text>
 <text x="406" y="208" class="t3">N/V, แพ้แสง/เสียง ± aura</text>
 <text x="406" y="236" class="t2"><tspan class="tb">Cluster:</tspan> รอบตา 15 นาที–3 ชม.</text>
 <text x="406" y="258" class="t3">น้ำตา น้ำมูก Horner ข้างเดียวกัน</text>
 <rect x="390" y="288" width="340" height="140" rx="12" class="box"/>
 <text x="560" y="312" text-anchor="middle" class="tb">ปวดหน้า (facial pain)</text>
 <text x="406" y="340" class="t2"><tspan class="tb">Trigeminal neuralgia:</tspan> แปล๊บเหมือนไฟช็อต</text>
 <text x="406" y="362" class="t2">เป็นวินาที ตาม CN V · เคี้ยว/แปรงฟัน/</text>
 <text x="406" y="384" class="t2">สัมผัส กระตุ้น</text>
 <text x="406" y="410" class="t3">→ carbamazepine</text>
</svg>''', "ซ้าย: red flag แต่ละตัวพร้อมโรคที่ต้องหา (secondary) · ขวา: ถ้าไม่มี red flag ให้แยก primary headache สามชนิดและ trigeminal neuralgia")

S1 = sec("neuro-07-01", "Approach to headache & red flags (SNOOP4)",
    "Systemic/2° risk · Neuro deficit · Onset sudden · Older >50 · Pattern change · Positional · Precipitated by Valsalva/exertion · Papilledema → imaging", minutes=6,
    source=f"{D} หน้า 249–255", nl=["2.1.3", "2.2.35"],
    md='''
### SNOOP4 (สไลด์)

[[fig:neuro-07-01-f1]]

| ตัวอักษร | Red flag |
|---|---|
| **S** | **Systemic symptoms** (ไข้ น้ำหนักลด) หรือ **secondary risk factor** (HIV, มะเร็ง) |
| **N** | **Neurological deficits** |
| **O** | **Onset sudden** (thunderclap — ปวดสุดใน < 1 นาที) |
| **O** | **Older age at onset** (> 50 ปี) |
| **P** | **Pattern change** (ปวดเปลี่ยนไป แย่ลงเรื่อย ๆ) |
| **P** | **Positional** headache (นอนแล้วแย่ลง = ↑ICP · ลุกนั่งแย่ลง = low CSF pressure — เสริม) |
| **P** | **Precipitated by Valsalva or exertion** (ไอ จาม เบ่ง วิ่ง) |
| **P** | **Papilledema** & signs of ↑ICP |

- มี red flag → **brain imaging** (CT ในภาวะเฉียบพลัน/ฉุกเฉิน · MRI เห็น posterior fossa และ cervicomedullary junction ดีกว่า — เสริม)
- ปวดหัวตอนตื่นนอน + อาเจียน + ตามัว = **↑ICP** (mass, IIH, VST)
- ปวดหัวเมื่อออกแรง/Valsalva + เวียนหัว → หา **posterior fossa lesion/Chiari malformation** → **MRI brain (± cervical spine)** (เสริม)

> โจทย์ที่ "progressive headache หลายสัปดาห์ + อาเจียน + ตามัว" แต่ PE อื่นปกติ → ตอบ **intracranial hypertension** ไม่ใช่ migraine หรือ tension
''',
    figs=[F_HA],
    pearls=[
        "SNOOP4 = red flags ของ secondary headache",
        "ปวดหัวตอนเช้า + อาเจียน + ตามัว = ↑ICP",
        "ปวดเมื่อออกแรง/Valsalva = red flag → MRI (posterior fossa)",
        "เริ่มปวดหัวครั้งแรกหลังอายุ 50 = red flag",
    ],
    items=[
        mcq("NEURO-07-01-1",
            "A 30-year-old woman has had persistent, progressive headache for 2 weeks. She occasionally vomits and has blurred vision. The rest of the examination is unremarkable. What is the most likely diagnosis?",
            "Intracranial hypertension",
            ["Meningitis", "Migraine", "Tension-type headache", "Ocular (refractive) headache"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 250–251)",
            explain='''ปวดหัว **progressive** (pattern change) + **อาเจียน** + **ตามัว** = red flag ของ **↑ICP** (สไลด์เฉลย secondary headache)
- Meningitis ต้องมีไข้และคอแข็ง
- Migraine เป็นเป็นพัก ๆ 4–72 ชม. ไม่ progressive ต่อเนื่อง 2 สัปดาห์
- Tension headache ไม่มีอาเจียนหรือตามัว
- Ocular headache (สายตา) ไม่ทำให้อาเจียนและ progressive''',
            pearl="Progressive headache + อาเจียน + ตามัว = ↑ICP", topic="Red flags",
            ref=[f"{D} หน้า 249–251"], nl=["2.1.3", "2.2.35"]),
        mcq("NEURO-07-01-2",
            "A 30-year-old woman has severe morning headaches lasting about 30 minutes, associated with dizziness. The headaches are clearly triggered by running and by coughing. Neurological examination is normal. What is the most appropriate investigation?",
            "MRI brain",
            ["Lumbar puncture", "Non-contrast CT brain", "Myelogram", "Skull radiograph"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 252–253)",
            explain='''ปวดหัวที่ **ถูกกระตุ้นด้วยการออกแรง/Valsalva** = red flag (P ใน SNOOP4 — สไลด์เฉลย precipitated by Valsalva or exertion) → ต้องทำ imaging หา **posterior fossa lesion/Chiari malformation** ซึ่ง **MRI** เห็นได้ดีกว่า CT (เฉลยในสไลด์เป็นภาพ — เลือก MRI ตามเหตุผลนี้)
- LP ไม่ทำก่อน imaging เมื่อสงสัย structural lesion
- CT ดูโพรงสมองส่วนหลังและรอยต่อกะโหลก-คอได้ไม่ดี (bone artifact)
- Myelogram ไม่ใช้วินิจฉัยปวดหัว
- Skull X-ray ไม่มีประโยชน์''',
            pearl="ปวดหัวเมื่อออกแรง/ไอ → MRI brain", topic="Exertional headache",
            ref=[f"{D} หน้า 249, 252–253"], nl=["2.1.3"]),
        mcq("NEURO-07-01-3",
            "A 35-year-old woman has had headaches for 3 months that are worst on waking. During severe episodes she has blurred vision, vertigo, nausea and vomiting. Neurological and general examinations are normal. What is the most appropriate management?",
            "MRI brain including the cervical spine",
            ["Treat as migraine", "Treat as tension-type headache", "Lumbar puncture", "Reassure and follow up in 6 months"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 254–255)",
            explain='''ปวดหัวเรื้อรังที่ **แย่ตอนตื่นนอน + ตามัว + อาเจียน + vertigo** = red flag ของ ↑ICP/posterior fossa (cerebellar tumor, Chiari) → ต้อง **imaging** ซึ่ง MRI รวม craniocervical junction ครอบคลุมที่สุด (เฉลยในสไลด์เป็นภาพ — ตอบตามหลัก red flag; CT brain ก็เป็นตัวเลือกที่ยอมรับได้ถ้า MRI ไม่มี)
- รักษาแบบ migraine หรือ tension โดยไม่ตรวจ จะพลาด secondary cause
- LP ก่อน imaging อาจทำให้ herniation ถ้ามี mass
- นัดดู 6 เดือนไม่เหมาะเมื่อมี red flag''',
            pearl="Red flag → imaging ก่อนให้การวินิจฉัย primary headache", topic="Red flags",
            ref=[f"{D} หน้า 249, 254–255"], nl=["2.1.3"]),
    ])

# ---------------------------------------------------------------- 07-02 ↑ICP & herniation
F_HERN = fig("neuro-07-02-f1", "Herniation syndromes (coronal schematic)", '''<svg viewBox="0 0 740 400">
 <defs><marker id="neuro-07-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <path d="M90 230C90 90 170 30 260 30C350 30 430 90 430 230C430 300 380 340 330 350L190 350C140 340 90 300 90 230Z" class="sunk"/>
 <path d="M260 34V150" class="ln"/>
 <text x="268" y="62" class="t3">falx</text>
 <path d="M110 230Q180 210 236 236" class="ln"/>
 <path d="M410 230Q340 210 284 236" class="ln"/>
 <text x="352" y="210" class="t3">tentorium</text>
 <rect x="236" y="236" width="48" height="90" rx="12" class="box"/>
 <text x="260" y="286" text-anchor="middle" class="t3">BS</text>
 <circle cx="150" cy="140" r="34" class="badsoft"/>
 <text x="150" y="145" text-anchor="middle" class="tb">mass</text>
 <path d="M190 120L250 120" class="lnbad" marker-end="url(#neuro-07-02-a)"/>
 <text x="196" y="110" class="tb">1</text>
 <path d="M168 200L226 236" class="lnbad" marker-end="url(#neuro-07-02-a)"/>
 <text x="176" y="230" class="tb">2</text>
 <path d="M260 160V228" class="lnbad" marker-end="url(#neuro-07-02-a)"/>
 <text x="270" y="200" class="tb">3</text>
 <ellipse cx="225" cy="338" rx="22" ry="14" class="misssoft"/>
 <ellipse cx="295" cy="338" rx="22" ry="14" class="misssoft"/>
 <path d="M260 360V388" class="lnbad" marker-end="url(#neuro-07-02-a)"/>
 <text x="272" y="384" class="tb">4</text>
 <text x="96" y="80" class="tb">5</text>
 <path d="M104 86L114 104" class="lnbad"/>
 <rect x="460" y="20" width="270" height="62" rx="10" class="box"/>
 <text x="472" y="42" class="tb">1 Subfalcine (cingulate)</text>
 <text x="472" y="62" class="t3">ใต้ falx · อาจกด ACA → ขาอ่อนแรง</text>
 <rect x="460" y="90" width="270" height="92" rx="10" class="badsoft"/>
 <text x="472" y="112" class="tb">2 Uncal (transtentorial)</text>
 <text x="472" y="132" class="t2">CN3 กด: pupil โต fixed <tspan class="tb">ข้างเดียวกัน</tspan></text>
 <text x="472" y="152" class="t2">hemiparesis <tspan class="tb">ข้างตรงข้าม</tspan></text>
 <text x="472" y="172" class="t3">+ ซึมลง</text>
 <rect x="460" y="190" width="270" height="62" rx="10" class="box"/>
 <text x="472" y="212" class="tb">3 Central</text>
 <text x="472" y="232" class="t3">ซึมลง pupil เล็ก→กลาง · posturing</text>
 <rect x="460" y="260" width="270" height="62" rx="10" class="box"/>
 <text x="472" y="282" class="tb">4 Tonsillar</text>
 <text x="472" y="302" class="t3">กด medulla → หยุดหายใจ, Cushing triad</text>
 <rect x="460" y="330" width="270" height="62" rx="10" class="box"/>
 <text x="472" y="352" class="tb">5 Transcalvarial</text>
 <text x="472" y="372" class="t3">สมองยื่นผ่านรอยกะโหลกแตก/craniectomy</text>
</svg>''', "Mass ทางซ้ายดันสมองไปตามช่องทาง 5 แบบ — uncal (2) สำคัญที่สุดในข้อสอบ: รูม่านตาโตข้างเดียวกับก้อน และอ่อนแรงข้างตรงข้าม")

S2 = sec("neuro-07-02", "Increased intracranial pressure & herniation",
    "Cushing triad (หายใจผิดปกติ BP↑ HR↓) · papilledema · CN6 palsy · uncal herniation: pupil โตข้างเดียวกัน + hemiparesis ข้างตรงข้าม · Mx: head 30° → mannitol/hypertonic saline → hyperventilation เฉพาะ refractory", minutes=8,
    source=f"{D} หน้า 256–264", nl=["2.2.35", "B3.2.3(2)"],
    md='''
### อาการ ↑ICP

- **Cushing triad**: **หายใจช้า/ไม่สม่ำเสมอ, BP ↑, HR ↓** (ตรงข้ามกับ shock)
- ซึมลง ปวดหัว คลื่นไส้อาเจียน
- **Papilledema**
- **Diplopia จาก CN6 palsy** (false localizing sign)
- **Herniation syndrome**

### Herniation

[[fig:neuro-07-02-f1]]

- **Uncal herniation**: temporal lobe (uncus) เคลื่อนผ่าน tentorium กด **CN3** → **pupil โต ตอบสนองช้า/ไม่ตอบสนอง ข้างเดียวกับ lesion** + กด cerebral peduncle → **hemiparesis/Babinski ข้างตรงข้าม** + ซึมลง
- Pupil ปกติ **2–4 mm** ในที่สว่าง
- ตัวอย่างคลาสสิก: บาดเจ็บศีรษะ (epidural/subdural hematoma) → pupil ขวาโต + อ่อนแรงซีกซ้าย = **uncal herniation ขวา**

### Management (สไลด์)

| ขั้นตอน | รายละเอียด |
|---|---|
| Initial | **ABC** · ETT ถ้า **GCS < 8** หรือ respiratory failure |
| Position | **Head elevation 30°** (ศีรษะตรง ไม่กด jugular vein) |
| Sedation/analgesia | เช่น fentanyl |
| Temperature | Paracetamol, cooling ถ้ามีไข้ |
| Fluid | **Euvolemia** (NSS — หลีกเลี่ยง hypotonic fluid — เสริม) |
| Seizure | IV diazepam |
| Oxygenation/ventilation | **PaO2 > 60 mmHg, SpO2 > 92–94%, PaCO2 35–45 mmHg** |
| Medication | **IV mannitol** (0.5–1 g/kg — เสริม), **hypertonic saline** |
| Refractory | **Controlled hyperventilation** (ชั่วคราว) |
| Surgical | Decompression, EVD, เอา mass ออก |

- **Dexamethasone** ช่วยเฉพาะ **vasogenic edema จาก tumor/abscess** ไม่ใช้ใน trauma/stroke (เสริม)
- Hyperventilation ลด CO2 → vasoconstriction → ลด ICP เร็วแต่ทำให้ **cerebral ischemia** → ใช้เฉพาะ **refractory/bridge** ก่อนผ่าตัด
''',
    figs=[F_HERN],
    pearls=[
        "Cushing triad = หายใจผิดปกติ + BP สูง + HR ช้า",
        "Uncal herniation: pupil โตข้างเดียวกับ lesion + อ่อนแรงข้างตรงข้าม",
        "↑ICP: head up 30° + mannitol/hypertonic saline",
        "Hyperventilation เฉพาะ refractory ↑ICP",
        "Papilledema + CN6 palsy = ↑ICP",
    ],
    items=[
        mcq("NEURO-07-02-1",
            "A 65-year-old man is knocked over onto the road. He is disoriented, cannot correctly name where he is, and complains of nausea and severe headache. Examination shows a fixed, dilated right pupil and weakness of the left arm and leg. What is the most likely diagnosis?",
            "Uncal herniation",
            ["Central herniation", "Cerebellar tonsillar herniation", "Cingulate (subfalcine) herniation", "Transcalvarial herniation"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 259–260)",
            explain='''**Pupil ขวาโต fixed** (CN3 ขวาถูกกด) + **อ่อนแรงซีกซ้าย** (cerebral peduncle) + ซึมลง หลังบาดเจ็บศีรษะ = **uncal (transtentorial) herniation ขวา**
- Central herniation ทำให้ซึมมาก pupil เล็ก/ขนาดกลางสองข้าง ไม่ใช่ pupil โตข้างเดียว
- Tonsillar herniation กด medulla → หยุดหายใจ Cushing triad
- Cingulate herniation มักไม่มีอาการเฉพาะ (อาจกด ACA)
- Transcalvarial ต้องมีกะโหลกแตกเปิดหรือหลังผ่าตัด''',
            pearl="Pupil โตข้างหนึ่ง + อ่อนแรงอีกข้าง = uncal herniation", topic="Uncal herniation",
            ref=[f"{D} หน้า 256–257, 259–260"], nl=["B3.2.3(2)", "2.2.35"]),
        mcq("NEURO-07-02-2",
            "A drowsy patient with a known brain mass has a right pupil of 5 mm with sluggish reaction to light and a left pupil of 3 mm with brisk reaction. There is a left extensor plantar response. What is the most likely diagnosis?",
            "Right uncal herniation",
            ["Left uncal herniation", "Tonsillar herniation", "Central herniation", "Physiologic anisocoria"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 261–262)",
            explain='''Pupil ขวา 5 mm ตอบสนองช้า (ปกติ 2–4 mm) = CN3 ขวาถูกกด + **Babinski ซ้าย** (corticospinal ข้างตรงข้าม) = **uncal herniation ด้านขวา**
- Uncal ซ้ายจะทำให้ pupil ซ้ายโตและ Babinski ขวา
- Tonsillar ไม่ทำ CN3 palsy
- Central herniation ทำให้ pupil สองข้างเท่ากัน
- Physiologic anisocoria ต่างกัน < 1 mm และตอบสนองแสงปกติ ไม่มี Babinski''',
            pearl="Pupil ปกติ 2–4 mm — โตข้างไหน herniation ข้างนั้น", topic="Pupil in herniation",
            ref=[f"{D} หน้า 261–262"], nl=["B3.2.3(2)"]),
        mcq("NEURO-07-02-3",
            "A woman with a newly diagnosed intracranial mass presents with severe headache, nausea and vomiting. She is drowsy but protecting her airway (GCS 12) and has bilateral papilledema. Head elevation to 30° has been done. What is the most appropriate next management?",
            "IV mannitol",
            ["Intubation with hyperventilation to PaCO2 25 mmHg", "Lumbar puncture to relieve pressure", "Hypotonic (0.45%) saline infusion", "Observation with repeat CT in 24 hours"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 263–264)",
            explain='''↑ICP ที่มีอาการ → **osmotherapy (IV mannitol หรือ hypertonic saline)** ตามสไลด์ (และ dexamethasone จะช่วยถ้าเป็น tumor edema) — **hyperventilation ใช้เฉพาะ refractory ↑ICP** (สไลด์เฉลยอย่างนั้น)
- Intubation + hyperventilation ไม่ใช่ขั้นแรก GCS 12 ยังไม่ต้อง ETT และ hyperventilation ทำให้สมองขาดเลือด
- LP ห้ามทำเมื่อมี mass + ↑ICP เสี่ยง herniation
- Hypotonic saline ทำให้สมองบวมมากขึ้น
- รอดูไม่เหมาะเมื่อมีอาการ ↑ICP''',
            pearl="↑ICP: mannitol/hypertonic saline ก่อน · hyperventilation เมื่อ refractory", topic="ICP management",
            ref=[f"{D} หน้า 258, 263–264"], nl=["2.2.35"]),
        mcq("NEURO-07-02-4",
            "A 45-year-old man with a large cerebellar hemorrhage becomes progressively drowsy. BP 210/110 mmHg, pulse 48/min, and his breathing is slow and irregular. Which combination of findings is he showing?",
            "Cushing triad from raised intracranial pressure",
            ["Neurogenic shock", "Beck triad", "Autonomic dysreflexia", "Hypovolemic shock"],
            explain='''**BP สูง + HR ช้า + หายใจช้าไม่สม่ำเสมอ** = **Cushing triad** จาก ↑ICP/กด brainstem (posterior fossa lesion เสี่ยง tonsillar herniation) → ต้องลด ICP และปรึกษาศัลยแพทย์ด่วน
- Neurogenic shock = BP ต่ำ + HR ช้า (spinal cord injury)
- Beck triad = BP ต่ำ JVP สูง เสียงหัวใจเบา (cardiac tamponade)
- Autonomic dysreflexia เกิดใน cord injury เหนือ T6 มีปวดหัว หน้าแดง เหงื่อออก
- Hypovolemic shock = BP ต่ำ HR เร็ว''',
            pearl="Cushing triad = ↑BP + ↓HR + หายใจผิดปกติ (ตรงข้าม shock)", topic="Cushing triad",
            ref=[f"{D} หน้า 256"], nl=["2.2.35"]),
    ])

# ---------------------------------------------------------------- 07-03 IIH
S3 = sec("neuro-07-03", "Idiopathic intracranial hypertension (pseudotumor cerebri)",
    "หญิงอ้วน, tetracycline/isotretinoin, vit A · ปวดหัว ตามัวชั่วคราว pulsatile tinnitus papilledema CN6 palsy · CT/MRI ปกติ → LP OP >20 (25) cmH2O · ลดน้ำหนัก หยุดยา acetazolamide", minutes=6,
    source=f"{D} หน้า 265–271", nl=["2.2.35", "2.1.3"],
    md='''
### นิยาม

- ชื่ออื่น: **pseudotumor cerebri**, **benign intracranial hypertension**
- **↑ICP โดยไม่พบสาเหตุ** (imaging ปกติ ไม่มี mass/hydrocephalus/VST)

### ปัจจัยเสี่ยง (สไลด์)

- **Female, obesity**
- ยา: **tetracycline** (doxycycline, minocycline), **vitamin A** (isotretinoin — เสริม), **danazol**

### อาการ

- ปวดหัว คลื่นไส้อาเจียน **ตามัวชั่วคราว (transient visual obscuration)**
- **Pulsatile tinnitus**
- **Papilledema** (สองข้าง) · **CN6 palsy** (เห็นภาพซ้อนแนวนอน)
- ระดับความรู้สึกตัวปกติ ไม่มี focal deficit อื่น

### Investigation

- **CT/MRI brain: ปกติ** (MRV เพื่อ R/O VST — เสริม)
- **LP: ↑OP > 20 cmH2O** (เกณฑ์ปัจจุบันในผู้ใหญ่ ≥ 25 cmH2O — เสริม) · CSF composition ปกติ

### Treatment

- **หยุดยาที่สงสัย**, **ลดน้ำหนัก**
- **Diuretics: acetazolamide** (ลดการสร้าง CSF), furosemide
- (เสริม) ตามัวรุนแรง/ลุกลาม → optic nerve sheath fenestration หรือ CSF shunt — **ภาวะแทรกซ้อนที่สำคัญคือตาบอดถาวร** ต้องติดตามลานสายตา

> หญิงอ้วน/กิน tetracycline + ปวดหัว + papilledema + CT ปกติ → ขั้นต่อไปคือ **LP วัด OP** (หลัง imaging ปกติแล้วเท่านั้น)
''',
    pearls=[
        "IIH: หญิงอ้วน วัยเจริญพันธุ์ / tetracycline / vitamin A",
        "Papilledema + CN6 palsy + CT ปกติ = IIH",
        "ยืนยันด้วย LP: OP สูง CSF ปกติ",
        "Tx: ลดน้ำหนัก หยุดยา acetazolamide",
        "ภาวะแทรกซ้อนสำคัญ = สูญเสียการมองเห็น",
    ],
    items=[
        mcq("NEURO-07-03-1",
            "An 18-year-old woman has had severe headache, nausea and visual disturbance for 5 days. She has been taking tetracycline and isotretinoin for acne. BT 36.7°C, BP 130/70 mmHg. Examination shows bilateral papilledema, no neck stiffness, and is otherwise unremarkable. What is the most likely diagnosis?",
            "Benign (idiopathic) intracranial hypertension",
            ["Hydrocephalus", "Accelerated hypertension", "Psychiatric adverse effect of isotretinoin", "Small-vessel vasculitis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 266–267)",
            explain='''หญิงสาว + **tetracycline และ isotretinoin (vitamin A derivative)** + ปวดหัว ตามัว **papilledema** ไม่มีไข้/คอแข็ง/focal deficit = **IIH**
- Hydrocephalus ต้องมีสาเหตุและเห็นใน imaging — ยังไม่มีข้อมูล และยาไม่ทำให้เกิด
- Accelerated hypertension ต้อง BP สูงมาก (130/70 ปกติ)
- ผลข้างเคียงทางจิตของ isotretinoin ไม่ทำให้ papilledema
- Vasculitis จะมีอาการระบบอื่นและ focal deficit''',
            pearl="Tetracycline/isotretinoin + papilledema = IIH", topic="IIH risk",
            ref=[f"{D} หน้า 265–267"], nl=["2.2.35"]),
        mcq("NEURO-07-03-2",
            "A 28-year-old woman has had headache for 7 days. Examination shows a left abducens (CN6) palsy and bilateral papilledema; she is otherwise neurologically normal. CT brain is normal. What is the most likely diagnosis?",
            "Benign (idiopathic) intracranial hypertension",
            ["Glioma", "Meningioma", "Pituitary adenoma", "Cavernous sinus thrombosis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 268–269)",
            explain='''Papilledema + **CN6 palsy (false localizing sign ของ ↑ICP)** + **CT ปกติ** = **IIH**
- Glioma และ meningioma ที่ทำให้ ↑ICP จะเห็นใน CT
- Pituitary adenoma ทำให้ bitemporal hemianopia และเห็นใน CT/MRI
- Cavernous sinus thrombosis มีไข้ ตาโปน หลาย CN (3, 4, 5, 6) และมักมีการติดเชื้อที่ใบหน้า''',
            pearl="Papilledema + CN6 palsy + CT ปกติ = IIH", topic="IIH diagnosis",
            ref=[f"{D} หน้า 265, 268–269"], nl=["2.2.35"]),
        mcq("NEURO-07-03-3",
            "An obese woman has had a bilateral non-throbbing headache for 1 month. Examination shows papilledema and is otherwise normal. Contrast-enhanced CT brain is normal. What is the most appropriate next step?",
            "Lumbar puncture with opening pressure measurement",
            ["Cerebral angiography", "Prescribe amitriptyline", "Prescribe corticosteroid", "Reassure that headache is tension-type"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 270–271)",
            explain='''หญิงอ้วน + papilledema + **imaging ปกติ** → ยืนยัน IIH ด้วย **LP วัด opening pressure** (> 20 cmH2O ตามสไลด์) และตรวจว่า CSF ปกติ
- Cerebral angiography ไม่จำเป็น (ถ้าจะหา VST ใช้ MRV/CTV)
- Amitriptyline รักษา tension headache — papilledema ไม่ใช่ tension headache
- Corticosteroid ไม่ใช่การรักษามาตรฐานของ IIH (ทำให้อ้วนขึ้น)
- การ reassure จะพลาดภาวะที่เสี่ยงตาบอด''',
            pearl="Papilledema + imaging ปกติ → LP วัด OP", topic="IIH confirm",
            ref=[f"{D} หน้า 265, 270–271"], nl=["2.2.35"]),
        mcq("NEURO-07-03-4",
            "A 26-year-old woman with BMI 36 kg/m2 is diagnosed with idiopathic intracranial hypertension; LP opening pressure was 32 cmH2O with normal CSF. MRI and MR venography are normal. Visual acuity is normal with mild enlargement of the blind spots. What is the most appropriate treatment?",
            "Weight reduction plus acetazolamide",
            ["Ventriculoperitoneal shunt immediately", "High-dose prednisolone", "Propranolol", "Warfarin"],
            explain='''IIH ที่การมองเห็นยังดี → **ลดน้ำหนัก + acetazolamide** (สไลด์: discontinue drug, wt loss, diuretics acetazolamide/furosemide) และติดตามลานสายตา
- Shunt/optic nerve sheath fenestration สำหรับรายที่การมองเห็นแย่ลงแม้ได้ยา
- Steroid ไม่ใช่การรักษาหลักและทำให้น้ำหนักขึ้น
- Propranolol เป็นยาป้องกัน migraine
- Warfarin ใช้ใน VST ซึ่ง MRV ปกติ''',
            pearl="IIH → ลดน้ำหนัก + acetazolamide", topic="IIH treatment",
            ref=[f"{D} หน้า 265"], nl=["2.2.35"]),
    ])

# ---------------------------------------------------------------- 07-04 SAH
S4 = sec("neuro-07-04", "Subarachnoid hemorrhage",
    "Ruptured aneurysm พบบ่อยสุด · thunderclap ปวดสุดในชีวิต + คอแข็ง · CT non-contrast (hyperdense basal cistern) → ถ้าปกติ LP (xanthochromia) → CTA/DSA · nimodipine + aneurysm repair + คุม BP", minutes=8,
    source=f"{D} หน้า 272–281", nl=["B3.2.6(2)", "2.3.6(3)", "2.2.44"],
    md='''
### สาเหตุและอาการ

- Traumatic SAH (พบบ่อยที่สุดโดยรวม) · Non-traumatic: **ruptured aneurysm (พบบ่อยสุด)**, ruptured AVM
- Trigger: **ออกแรง** · Risk: **สูบบุหรี่, HT** (ประวัติครอบครัว, ADPKD — เสริม)
- **Sudden & severe headache — "ปวดที่สุดในชีวิต" (thunderclap)** + คลื่นไส้อาเจียน
- Signs of ↑ICP, **stiff neck**, อาจหมดสติชั่วคราว · มักไม่มี focal deficit (ต่างจาก ICH)

### Diagnosis

1. **CT brain non-contrast**: **hyperdensity ใน basal cisterns** (ไวมากใน 6 ชม.แรก — เสริม)
2. **Lumbar puncture** — ทำเมื่อ **CT ปกติแต่ยังสงสัย SAH**: **RBC สูงและไม่จางลงในหลอดหลัง** หรือ **xanthochromia** (≥ 12 ชม. หลังปวด — เสริม) · **traumatic tap จะแดงจางลง**
3. **Vascular imaging** หา aneurysm: **CTA/MRA**, **DSA** (gold standard)

### Management (สไลด์)

- **ETT** ถ้า GCS < 8 หรือ respiratory failure
- **BP control ป้องกัน rebleeding** เช่น ≤ 140/90 (ไม่มีเกณฑ์ตายตัว แต่ **SBP ไม่ควรเกิน 160–180**) — ยา **nicardipine, NTG, labetalol** · ไม่ลดต่ำเกินเพราะต้องรักษา cerebral blood flow
- **Reverse anticoagulant**
- **Antiepileptics** เมื่อมีชัก
- ICP management
- **Ruptured aneurysm**: **nimodipine** (ป้องกัน **vasospasm** — 60 mg PO q4h × 21 วัน — เสริม) + **aneurysm repair** (coiling/clipping ภายใน 24–72 ชม. — เสริม)

### ภาวะแทรกซ้อน (เสริม)

Rebleeding (วันแรก ๆ) · **vasospasm/delayed cerebral ischemia (วันที่ 3–14)** · hydrocephalus · hyponatremia (SIADH/cerebral salt wasting) · ชัก
''',
    pearls=[
        "Thunderclap + คอแข็ง = SAH จนกว่าจะพิสูจน์ได้ว่าไม่ใช่",
        "CT non-contrast ก่อน · ปกติแต่ยังสงสัย → LP (xanthochromia, RBC ไม่จางลง)",
        "Aneurysm → CTA/DSA → coiling/clipping",
        "Nimodipine ป้องกัน vasospasm",
        "คุม SBP < 160 ก่อน repair",
    ],
    items=[
        mcq("NEURO-07-04-1",
            "A 60-year-old woman has an abrupt onset of severe headache; she has never had headaches before. BT 37.5°C, BP 140/90 mmHg. Examination: neck stiffness, no neurological deficit, Babinski negative. What is the most likely diagnosis?",
            "Subarachnoid hemorrhage",
            ["Migraine", "Bacterial meningitis", "Subdural hemorrhage", "Intracerebral hematoma"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 276–277)",
            explain='''ปวดหัว **ทันทีรุนแรงครั้งแรก (thunderclap)** + **คอแข็ง** + ไม่มีไข้ ไม่มี focal deficit = **SAH**
- Migraine ไม่เกิดครั้งแรกตอนอายุ 60 แบบ thunderclap และไม่ทำให้คอแข็ง
- Bacterial meningitis ต้องมีไข้ (37.5 ไม่ใช่) และค่อยเป็นมากกว่า
- Subdural hemorrhage มักค่อยเป็น ตามหลัง trauma ไม่มีคอแข็ง
- Intracerebral hematoma มี focal deficit''',
            pearl="Thunderclap + คอแข็ง + ไม่มีไข้ = SAH", topic="SAH diagnosis",
            ref=[f"{D} หน้า 272, 276–277"], nl=["B3.2.6(2)"]),
        mcq("NEURO-07-04-2",
            "A 50-year-old Thai woman develops a sudden severe headache with nausea and vomiting while watching television. BP 150/110 mmHg, PR 80/min, RR 22/min. Motor power is grade 5 in all limbs, neck stiffness is positive, Babinski is negative and there is no papilledema. What is the most likely diagnosis?",
            "Subarachnoid hemorrhage",
            ["Migraine", "Viral encephalitis", "Bacterial meningitis", "Acute basal ganglia hemorrhage"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 278–279)",
            explain='''ปวดหัวทันทีรุนแรง + อาเจียน + **คอแข็ง** + **ไม่มี focal deficit** = **SAH** (ruptured aneurysm)
- Migraine ไม่ทำให้คอแข็ง
- Viral encephalitis มีไข้ ซึม/ชัก ค่อยเป็น
- Bacterial meningitis มีไข้
- Basal ganglia hemorrhage ทำให้ hemiparesis ชัด (ที่นี่ motor V ทุกแขนขา)''',
            pearl="SAH: ปวดหัวทันที + คอแข็ง + ไม่มี focal deficit", topic="SAH vs ICH",
            ref=[f"{D} หน้า 272, 278–279"], nl=["B3.2.6(2)"]),
        mcq("NEURO-07-04-3",
            "A 68-year-old man with hypertension was awakened by a sudden severe pulsating headache with nausea and vomiting 10 hours ago; it has eased by the time he arrives. He has never had such a headache before. BT 37°C, BP 150/90 mmHg. He is alert and oriented; neurological and fundoscopic examinations are normal. Non-contrast CT brain is normal. What is the most appropriate next step?",
            "Lumbar puncture",
            ["CT brain with contrast", "Propranolol", "Ergotamine", "Ibuprofen"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 280–281)",
            explain='''Thunderclap headache ครั้งแรกในผู้สูงอายุ = สงสัย **SAH** แม้ปวดลดลงแล้ว · **CT non-contrast ปกติแต่ยังสงสัย** → **LP** หา RBC ที่ไม่จางลงหรือ **xanthochromia** (สไลด์เฉลย SAH: LP กรณี CT normal แต่ยังสงสัย)
- CT with contrast ไม่ช่วยหาเลือดใน subarachnoid space
- Propranolol, ergotamine และ ibuprofen เป็นการรักษา migraine ซึ่งเป็นการวินิจฉัยที่ไม่ควรให้กับ thunderclap ครั้งแรกในวัย 68''',
            pearl="สงสัย SAH + CT ปกติ → LP", topic="CT-negative SAH",
            ref=[f"{D} หน้า 273, 280–281"], nl=["B3.2.6(2)", "B3.3(2)"]),
        mcq("NEURO-07-04-4",
            "A 52-year-old woman with SAH from a ruptured anterior communicating artery aneurysm is admitted to the ICU. GCS is 14 and BP is 185/100 mmHg. The neurosurgery team plans endovascular coiling the next morning. Which medication should be started to prevent delayed cerebral ischemia?",
            "Oral nimodipine",
            ["IV nitroprusside to keep SBP below 100 mmHg", "Tranexamic acid for 3 months", "Prophylactic IV heparin infusion", "IV dexamethasone"],
            explain='''Ruptured aneurysm → **nimodipine** ป้องกัน **vasospasm/delayed cerebral ischemia** (สไลด์) ร่วมกับคุม BP (nicardipine/labetalol ให้ SBP < 160) และ aneurysm repair
- ลด SBP ต่ำกว่า 100 ทำให้ cerebral perfusion ไม่พอ
- Tranexamic acid ระยะยาวเพิ่ม thrombosis/ischemia — ไม่แนะนำ
- Heparin เพิ่ม rebleeding ก่อนรักษา aneurysm
- Dexamethasone ไม่มีประโยชน์ใน SAH''',
            pearl="Aneurysmal SAH → nimodipine + repair + SBP < 160", topic="SAH management",
            ref=[f"{D} หน้า 274–275"], nl=["B3.2.6(2)"]),
    ])

# ---------------------------------------------------------------- 07-05 Venous sinus thrombosis
S5 = sec("neuro-07-05", "Cerebral venous sinus thrombosis",
    "Hypercoagulable (OCP, ตั้งครรภ์, มะเร็ง) หรือติดเชื้อใบหน้า/sinus · ปวดหัว ↑ICP papilledema ชัก CN palsy · MRV/CTV (empty delta) · anticoagulant แม้มีเลือดออก", minutes=6,
    source=f"{D} หน้า 282–285", nl=["2.3.9-3(3)", "2.1.3"],
    md='''
### สาเหตุ

- **Non-infectious: hypercoagulable state — OCP, pregnancy/postpartum, cancer** (thrombophilia, dehydration — เสริม)
- **Infectious: sinusitis, mid-facial infection, dental infection** (→ cavernous sinus thrombosis)

### อาการ

- **ปวดหัว** (พบบ่อยสุด) + **signs of ↑ICP**: papilledema, diplopia, vision loss, N/V
- **ชัก**, focal deficit, **CN palsy** (cavernous sinus: CN 3, 4, 5, 6)
- อาจมี venous infarct ที่มีเลือดออก (hemorrhagic) โดยเฉพาะ parasagittal (เสริม)

### Investigation

- **MRI with MRV** หรือ **CT with CTV**: **absence of flow**, intraluminal thrombus, **empty delta sign** (contrast)
- **CT non-contrast**: **hyperdense sinus** (cord sign) — แต่ CT ปกติได้บ่อย

### Treatment

- **Anticoagulant** (LMWH/UFH → warfarin/DOAC 3–12 เดือน — เสริม) **แม้มี hemorrhagic venous infarct** (เสริม)
- **รักษาสาเหตุ**: หยุด OCP, ATB สำหรับการติดเชื้อ

> หญิงกิน OCP + ปวดหัวใหม่ + อาเจียน (± ชัก/papilledema) → **imaging (CT/MRV)** ก่อนจะให้ยาแก้ปวดแบบ migraine
''',
    pearls=[
        "OCP/ตั้งครรภ์/หลังคลอด + ปวดหัวใหม่ → นึกถึง VST",
        "VST: ↑ICP + ชัก + focal deficit",
        "MRV/CTV ยืนยัน · empty delta sign",
        "Tx anticoagulant แม้มีเลือดออก + แก้สาเหตุ",
    ],
    items=[
        mcq("NEURO-07-05-1",
            "A 35-year-old woman with an anxiety disorder has had a new headache over the bitemporal and occipital areas, with vomiting. She has been taking an oral contraceptive pill for 6 months. Examination is otherwise unremarkable. What is the most appropriate management?",
            "CT brain with CT venography",
            ["Triptan", "Amitriptyline", "Ibuprofen", "Stop the oral contraceptive and reassure"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 284–285)",
            explain='''ปวดหัวแบบใหม่ + **อาเจียน** ในหญิงที่ **กิน OCP** → ต้อง **R/O venous sinus thrombosis** ด้วย imaging ก่อน (สไลด์เฉลย R/O VST; ตัวเลือกเดิม "CT brain" — เขียนให้ชัดว่ารวม venography)
- Triptan เป็นยา migraine และห้ามใช้ถ้าเป็นโรคหลอดเลือด/ลิ่มเลือด
- Amitriptyline/ibuprofen เป็นการรักษา tension headache โดยไม่หาสาเหตุ
- หยุด OCP อย่างเดียวโดยไม่ตรวจ อาจพลาด VST ที่ต้องให้ anticoagulant''',
            pearl="OCP + ปวดหัวใหม่ + อาเจียน → imaging หา VST", topic="VST suspicion",
            ref=[f"{D} หน้า 282–285"], nl=["2.3.9-3(3)"]),
        mcq("NEURO-07-05-2",
            "A 29-year-old woman, 2 weeks postpartum, presents with 4 days of worsening headache and a generalized seizure. She has bilateral papilledema and mild right leg weakness. Non-contrast CT shows a hyperdense superior sagittal sinus with a small left parasagittal hemorrhagic infarct. MR venography confirms superior sagittal sinus thrombosis. What is the most appropriate treatment?",
            "Anticoagulation with low-molecular-weight heparin",
            ["Withhold anticoagulation because of the hemorrhage", "IV alteplase", "Aspirin alone", "Emergency craniotomy for clot evacuation"],
            explain='''VST หลังคลอด (hypercoagulable) → **anticoagulant** เป็นการรักษาหลัก (สไลด์) — **ให้ได้แม้มี hemorrhagic venous infarct** เพราะเลือดออกเกิดจากความดันในหลอดเลือดดำที่สูงขึ้น ซึ่งการเปิดหลอดเลือดดำจะช่วยลด (เสริม) + AED สำหรับชัก
- งด anticoagulant ทำให้ลิ่มเลือดลามและแย่ลง
- Alteplase ไม่ใช่การรักษามาตรฐานของ VST
- Aspirin ไม่พอสำหรับ venous thrombosis
- Craniotomy สงวนไว้สำหรับ herniation จาก mass effect''',
            pearl="VST → anticoagulant แม้มีเลือดออก", topic="VST treatment",
            ref=[f"{D} หน้า 283"], nl=["2.3.9-3(3)", "B2.4(3)"]),
        mcq("NEURO-07-05-3",
            "A 40-year-old man has a 1-week history of a facial furuncle near the nose that he squeezed. He now has fever, headache, bilateral proptosis, chemosis and painful ophthalmoplegia with reduced sensation over the forehead. What is the most likely diagnosis?",
            "Septic cavernous sinus thrombosis",
            ["Orbital cellulitis without intracranial extension", "Idiopathic intracranial hypertension", "Ocular myasthenia gravis", "Migraine with aura"],
            explain='''ติดเชื้อที่ **mid-face (danger triangle)** → ลามเข้า **cavernous sinus** (สไลด์: infectious cause — mid-facial infection) → ไข้ ตาโปน **สองข้าง** chemosis **ophthalmoplegia (CN 3, 4, 6)** และชา V1 (เสริม) → MRI/MRV, IV ATB ± anticoagulant
- Orbital cellulitis มักเป็นข้างเดียวและไม่ลามไปตาอีกข้าง
- IIH ไม่มีไข้/ตาโปน
- Ocular MG ไม่มีไข้ ปวด หรือตาโปน
- Migraine with aura ไม่มี ophthalmoplegia ถาวรและตาโปน''',
            pearl="ฝีที่ใบหน้า + ตาโปนสองข้าง + ophthalmoplegia = cavernous sinus thrombosis", topic="Cavernous sinus thrombosis",
            ref=[f"{D} หน้า 282"], nl=["2.3.9-3(3)"]),
    ])

# ---------------------------------------------------------------- 07-06 Trigeminal neuralgia
S6 = sec("neuro-07-06", "Trigeminal neuralgia",
    "ปวดหน้าข้างเดียว แปล๊บเหมือนไฟช็อต เป็นวินาที ตามแขนง CN V · เคี้ยว พูด สัมผัส แปรงฟันกระตุ้น · carbamazepine 1st line → AED อื่น → surgery", minutes=5,
    source=f"{D} หน้า 286–294", nl=["B3.2.7-3(1)", "2.3.6-3(12)", "B3.4(7)"],
    md='''
### อาการ (สไลด์)

- **Unilateral facial pain**
- **Sharp, electric shock-like** ตามแขนงของ **CN V** (ส่วนใหญ่ V2, V3 — แก้ม กราม ฟัน — เสริม)
- **Duration: วินาที** (เป็นชุด ๆ)
- **Trigger: เคี้ยว พูด สัมผัส** (แปรงฟัน ล้างหน้า โกนหนวด)
- Neuro exam ปกติ (ถ้ามีชา/อายุน้อย/สองข้าง → หา secondary cause เช่น MS, tumor — เสริม)

### Treatment

1. **Carbamazepine (1st line)** (oxcarbazepine — เสริม)
2. **Other antiepileptics** (gabapentin, baclofen, lamotrigine, valproate — เสริม)
3. **Surgery** กรณี refractory (microvascular decompression — เสริม)

- ยาแก้ปวดทั่วไป (paracetamol, NSAID, tramadol) **ไม่ได้ผล**

| | Trigeminal neuralgia | Cluster headache | Post-herpetic neuralgia |
|---|---|---|---|
| ตำแหน่ง | แก้ม กราม (V2, V3) | รอบตา | ตาม dermatome ที่เคยเป็นงูสวัด |
| ระยะเวลา | **วินาที** | 15 นาที–3 ชม. | ปวดแสบต่อเนื่อง |
| Trigger | สัมผัส เคี้ยว | แอลกอฮอล์ (เสริม) | — |
| อาการร่วม | ไม่มี | น้ำตา น้ำมูก Horner | allodynia, แผลเป็น |
''',
    pearls=[
        "ปวดแปล๊บเป็นวินาทีที่แก้ม/กราม + สัมผัสกระตุ้น = trigeminal neuralgia",
        "Carbamazepine = 1st line",
        "ยาแก้ปวดทั่วไปไม่ได้ผล",
        "TN + ชาที่หน้า/อายุน้อย → MRI หา MS/tumor",
    ],
    items=[
        mcq("NEURO-07-06-1",
            "A 45-year-old woman has had 3 months of paroxysmal electric-shock-like pain lasting seconds in the left face and teeth. The pain is aggravated by chewing or rubbing the left cheek and does not respond to paracetamol. The ear is normal, there is no facial tenderness, and touching her left face triggers the pain. What is the most likely diagnosis?",
            "Trigeminal neuralgia",
            ["Migraine", "Cluster headache", "Tension-type headache", "Post-herpetic neuralgia"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 287–288)",
            explain='''ปวดหน้าข้างเดียว **เหมือนไฟช็อต เป็นวินาที** + **เคี้ยว/สัมผัสกระตุ้น** = **trigeminal neuralgia**
- Migraine ปวดตุบ ๆ นาน 4–72 ชม. มี N/V แพ้แสงเสียง
- Cluster ปวดรอบตา 15 นาที–3 ชม. มีน้ำตาน้ำมูก
- Tension ปวดตื้อ ๆ รอบศีรษะ
- Post-herpetic neuralgia ต้องมีประวัติงูสวัดที่ตำแหน่งนั้น ปวดแสบต่อเนื่อง''',
            pearl="ไฟช็อตเป็นวินาที + สัมผัสกระตุ้น = TN", topic="TN diagnosis",
            ref=[f"{D} หน้า 286–288"], nl=["B3.2.7-3(1)"]),
        mcq("NEURO-07-06-2",
            "A 50-year-old woman has episodic sharp stabbing pain at the left mandible radiating to the temporomandibular joint and deep into the left ear. Episodes are triggered by smiling and touching her face. There is no neurological deficit and no dental caries. What is the most appropriate treatment?",
            "Carbamazepine",
            ["Tramadol", "Ibuprofen", "Amitriptyline", "Prednisolone"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 289–290)",
            explain='''ปวดแปล๊บตามแขนง V3 (กราม) ถูกกระตุ้นด้วยการยิ้ม/สัมผัส ไม่มีปัญหาฟัน = **trigeminal neuralgia** → **carbamazepine (1st line)**
- Tramadol และ ibuprofen (ยาแก้ปวดทั่วไป) ได้ผลน้อยใน TN
- Amitriptyline ใช้กับ neuropathic pain/tension headache ไม่ใช่ 1st line ของ TN
- Prednisolone ไม่มีบทบาท''',
            pearl="TN → carbamazepine", topic="TN treatment",
            ref=[f"{D} หน้า 286, 289–290"], nl=["B3.2.7-3(1)", "B3.4(7)"]),
        mcq("NEURO-07-06-3",
            "A 60-year-old man has had electric-like pain in the right cheek for 6 months, triggered by brushing his teeth. He developed a severe rash on carbamazepine and is HLA-B1502 positive. Which is the most appropriate medication?",
            "Gabapentin",
            ["Vitamin B1-6-12", "Prednisolone", "Oxcarbazepine", "Phenytoin"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 291–292)",
            explain='''Trigeminal neuralgia ที่ **แพ้ carbamazepine (HLA-B1502)** → ใช้ **antiepileptic อื่นที่ไม่ใช่ aromatic** เช่น **gabapentin** (สไลด์: other antiepileptics; ตัวเลือกในสไลด์มี vit B, steroid, gabapentin — เติมประวัติแพ้ CBZ เพื่อให้ gabapentin เป็นคำตอบเดียว)
- Vitamin B รวมไม่รักษา TN
- Prednisolone ไม่มีบทบาท
- Oxcarbazepine และ phenytoin เสี่ยง cross-reactivity กับ CBZ ใน HLA-B1502''',
            pearl="TN แพ้ CBZ → gabapentin (เลี่ยง aromatic AED)", topic="TN alternative",
            ref=[f"{D} หน้า 127, 286, 291–292"], nl=["B3.2.7-3(1)", "B3.4(7)"]),
        mcq("NEURO-07-06-4",
            "A 55-year-old woman has had 1 month of stabbing pain in the left cheek and in front of the left ear, worse with chewing, not relieved by paracetamol. Neurological examination is normal. Carbamazepine is not available at her health center. Which of the following is the most appropriate alternative?",
            "Sodium valproate",
            ["Midazolam", "Alprazolam", "Chlorpromazine", "Codeine"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 293–294)",
            explain='''Trigeminal neuralgia → ยากลุ่ม **antiepileptic**; ในตัวเลือกมีเพียง **sodium valproate** (สไลด์: other antiepileptics — เติมว่าไม่มี CBZ เพื่อให้เหตุผลชัด)
- Midazolam และ alprazolam เป็น benzodiazepine ไม่รักษา TN และติดได้
- Chlorpromazine เป็น antipsychotic
- Codeine (opioid) ได้ผลน้อยใน neuropathic pain แบบนี้''',
            pearl="TN ใช้ยากันชัก ไม่ใช่ยาแก้ปวดทั่วไป", topic="TN treatment",
            ref=[f"{D} หน้า 286, 293–294"], nl=["B3.2.7-3(1)"]),
    ])

LECTURE = lecture("07", "Secondary headache", "SNOOP4 · ↑ICP & herniation · IIH · SAH · VST · trigeminal neuralgia",
    objectives=[
        "ใช้ SNOOP4 คัดผู้ป่วยปวดหัวที่ต้องทำ imaging ได้",
        "รู้อาการ ↑ICP และ herniation พร้อมจัดการตามลำดับได้",
        "วินิจฉัยและรักษา IIH, SAH และ venous sinus thrombosis ได้",
        "วินิจฉัย trigeminal neuralgia และเลือกยาได้",
    ],
    sections=[S1, S2, S3, S4, S5, S6])
