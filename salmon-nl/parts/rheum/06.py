from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Rheumato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 06-01 IIM
F_IIM = fig("rheum-06-01-f1", "IIM: แยกชนิดจากรูปแบบกล้ามเนื้ออ่อนแรงและผื่น", '''<svg viewBox="0 0 740 360">
 <rect x="10" y="10" width="230" height="250" rx="12" class="badsoft"/>
 <rect x="255" y="10" width="230" height="250" rx="12" class="c1soft"/>
 <rect x="500" y="10" width="230" height="250" rx="12" class="misssoft"/>
 <text x="125" y="34" text-anchor="middle" class="tb">Dermatomyositis</text>
 <text x="370" y="34" text-anchor="middle" class="tb">Polymyositis</text>
 <text x="615" y="34" text-anchor="middle" class="tb">Inclusion-body myositis</text>
 <circle cx="125" cy="64" r="14" class="box"/>
 <rect x="105" y="80" width="40" height="70" rx="10" class="box"/>
 <rect x="77" y="84" width="26" height="12" rx="5" class="bad"/>
 <rect x="147" y="84" width="26" height="12" rx="5" class="bad"/>
 <rect x="71" y="98" width="10" height="48" rx="5" class="box"/>
 <rect x="169" y="98" width="10" height="48" rx="5" class="box"/>
 <rect x="107" y="152" width="14" height="28" rx="5" class="bad"/>
 <rect x="129" y="152" width="14" height="28" rx="5" class="bad"/>
 <rect x="107" y="182" width="14" height="30" rx="5" class="box"/>
 <rect x="129" y="182" width="14" height="30" rx="5" class="box"/>
 <path d="M112 62H138" class="lnc2"/>
 <circle cx="370" cy="64" r="14" class="box"/>
 <rect x="350" y="80" width="40" height="70" rx="10" class="box"/>
 <rect x="322" y="84" width="26" height="12" rx="5" class="bad"/>
 <rect x="392" y="84" width="26" height="12" rx="5" class="bad"/>
 <rect x="316" y="98" width="10" height="48" rx="5" class="box"/>
 <rect x="414" y="98" width="10" height="48" rx="5" class="box"/>
 <rect x="352" y="152" width="14" height="28" rx="5" class="bad"/>
 <rect x="374" y="152" width="14" height="28" rx="5" class="bad"/>
 <rect x="352" y="182" width="14" height="30" rx="5" class="box"/>
 <rect x="374" y="182" width="14" height="30" rx="5" class="box"/>
 <circle cx="615" cy="64" r="14" class="box"/>
 <rect x="595" y="80" width="40" height="70" rx="10" class="box"/>
 <rect x="567" y="84" width="26" height="12" rx="5" class="box"/>
 <rect x="637" y="84" width="26" height="12" rx="5" class="miss"/>
 <rect x="561" y="98" width="10" height="48" rx="5" class="miss"/>
 <rect x="659" y="98" width="10" height="48" rx="5" class="box"/>
 <rect x="597" y="152" width="14" height="28" rx="5" class="miss"/>
 <rect x="619" y="152" width="14" height="28" rx="5" class="box"/>
 <rect x="597" y="182" width="14" height="30" rx="5" class="box"/>
 <rect x="619" y="182" width="14" height="30" rx="5" class="miss"/>
 <text x="125" y="232" text-anchor="middle" class="t2">proximal สมมาตร + ผื่น</text>
 <text x="125" y="250" text-anchor="middle" class="t3">เส้นม่วง = heliotrope</text>
 <text x="370" y="232" text-anchor="middle" class="t2">proximal สมมาตร</text>
 <text x="370" y="250" text-anchor="middle" class="t3">ไม่มีผื่น</text>
 <text x="615" y="232" text-anchor="middle" class="t2">อสมมาตร proximal + distal</text>
 <text x="615" y="250" text-anchor="middle" class="t3">quadriceps, finger flexor (เสริม)</text>
 <rect x="10" y="272" width="230" height="78" rx="10" class="box"/>
 <text x="20" y="294" class="t2">Gottron papules</text>
 <text x="20" y="314" class="t2">Heliotrope rash</text>
 <text x="20" y="334" class="t2">Shawl sign · ระวังมะเร็ง</text>
 <rect x="255" y="272" width="230" height="78" rx="10" class="box"/>
 <text x="265" y="294" class="t2">ผู้ใหญ่ · CK สูง</text>
 <text x="265" y="314" class="t2">ต้องแยก drug myopathy</text>
 <text x="265" y="334" class="t2">และ hypothyroid (เสริม)</text>
 <rect x="500" y="272" width="230" height="78" rx="10" class="box"/>
 <text x="510" y="294" class="t2">ชาย &gt; 50 ปี · ค่อยเป็นค่อยไป</text>
 <text x="510" y="314" class="t2">ไม่ตอบสนอง steroid</text>
 <text x="510" y="334" class="ta">→ supportive tx</text>
</svg>''', "สีแดงคือกล้ามเนื้อที่อ่อนแรง (ต้นแขน ต้นขาสมมาตรใน DM และ PM) · สีเหลืองใน IBM คือการอ่อนแรงแบบอสมมาตรทั้งต้นและปลาย · DM ต่างจาก PM ตรงที่มีผื่น")

S1 = sec("rheum-06-01", "Idiopathic inflammatory myopathies (IIM)",
    "DM, PM, IBM, overlap, IMNM · มะเร็งและ ILD · proximal weakness สมมาตร ± dysphagia · DM: Gottron, heliotrope, shawl · CK, aldolase ↑ · EMG · muscle biopsy = gold standard · steroid + IS · cancer screening", minutes=9,
    source=f"{D} หน้า 145–158", nl=["2.3.13-3(10)", "B5.2.2-3(2)", "2.1.22"],
    md='''
### การจำแนก (สไลด์หน้า 145–146)

| ชนิด | กล้ามเนื้อ | ผื่น |
|---|---|---|
| **Dermatomyositis (DM)** | **proximal สมมาตร** | **มี** |
| **Polymyositis (PM)** | **proximal สมมาตร** | ไม่มี |
| **Inclusion-body myositis (IBM)** | **อสมมาตร ทั้ง proximal และ distal** | ไม่มี |
| Overlap myositis (OM) | ร่วมกับ CTD อื่น เช่น SLE, SSc | แล้วแต่โรค |
| Immune-mediated necrotizing myopathy (IMNM) | proximal รุนแรง CK สูงมาก (สัมพันธ์ statin, anti-HMGCR — เสริม) | ไม่มี |

- โรคที่สัมพันธ์: **มะเร็ง** (โดยเฉพาะ DM ในผู้ใหญ่ เช่น มะเร็งรังไข่ ปอด กระเพาะ โพรงหลังจมูก — เสริม) และ **interstitial lung disease (ILD)**
- กลไก (เสริม): DM = complement ทำลายหลอดเลือดฝอยในกล้ามเนื้อและผิวหนัง (perifascicular atrophy) · PM = CD8 T cell บุกเส้นใยกล้ามเนื้อ

[[fig:rheum-06-01-f1]]

### อาการ (สไลด์หน้า 147–148)
- **Symmetric proximal muscle weakness**: ลุกจากเก้าอี้ลำบาก ขึ้นบันไดลำบาก ยกแขนหวีผมลำบาก
- **Dysphagia, dysphonia** (กล้ามเนื้อคอหอย)
- ผื่นของ **DM**:
  - **Gottron papules** = ตุ่มแดงมีสะเก็ดบนด้าน extensor ของข้อนิ้ว (knuckles) — **pathognomonic**
  - **Heliotrope rash** = ผื่นสีม่วงแดงที่ **เปลือกตาบน** ± บวม
  - **Shawl sign** = ผื่นแดงที่หลังส่วนบน ต้นคอด้านหลัง และไหล่
- ระบบอื่น (เสริม): ILD (ไอแห้ง หอบ crackles) · mechanic's hands · Raynaud

### Investigation (สไลด์หน้า 149)
- **Muscle enzyme สูง: CPK/CK, aldolase** (AST, ALT, LDH สูงได้จากกล้ามเนื้อ — เสริม)
- **EMG**: myopathic pattern
- **Muscle biopsy = gold standard**
- **Autoantibodies: ANA, myositis-specific antibodies** (anti-Jo-1 → antisynthetase + ILD, anti-Mi-2 → DM ผื่นเด่น, anti-TIF1-γ → มะเร็ง — เสริม)
- หา ILD: HRCT, PFT (เสริม)

### การรักษา (สไลด์หน้า 150)
- **IBM**: **supportive** (physical therapy, speech therapy) — ไม่ตอบสนองยากดภูมิ
- **IIM อื่น**: **steroid + immunosuppressant** (เช่น prednisolone 1 mg/kg/d + MTX หรือ AZA — ขนาดเสริม)
- **Age-appropriate cancer screening** ทุกราย (โดยเฉพาะ DM)

> แยก myopathy อื่นในโจทย์: **statin myopathy** (ปวดกล้ามเนื้อ ไม่มีผื่น), **steroid myopathy** (CK ปกติ, ไม่มีผื่น), **hypothyroid myopathy** (TSH สูง) (เสริม)
''',
    figs=[F_IIM],
    pearls=[
        "DM = proximal weakness สมมาตร + Gottron/heliotrope/shawl · PM = ไม่มีผื่น · IBM = อสมมาตร proximal + distal",
        "IIM สัมพันธ์มะเร็งและ ILD → cancer screening ตามอายุทุกราย",
        "CK, aldolase สูง · EMG myopathic · muscle biopsy = gold standard",
        "Tx: steroid + immunosuppressant · IBM = supportive",
    ],
    items=[
        mcq("RHEUM-06-01-1",
            "A 50-year-old woman has had limb aches for 4 weeks with difficulty rising from a chair and climbing stairs. Examination shows purple-red discoloration of the forehead, cheeks, and eyelids and purplish papules over the elbows and knees. What is the most likely diagnosis?",
            "Dermatomyositis",
            ["Psoriasis", "Discoid lupus erythematosus", "Systemic lupus erythematosus", "Mixed connective tissue disease"],
            kind="old", src=OLD,
            explain='''**Proximal muscle weakness (ลุกนั่ง ขึ้นบันไดลำบาก) + ผื่นม่วงที่เปลือกตา (heliotrope) + ตุ่มม่วงด้าน extensor ของข้อ (Gottron sign)** = **dermatomyositis**
- Psoriasis เป็น plaque สะเก็ดเงิน ไม่มีกล้ามเนื้ออ่อนแรง
- Discoid lupus เป็นผื่นที่ผิวหนังอย่างเดียว หายแล้วเป็นแผลเป็น
- SLE มี malar rash ที่เว้น nasolabial fold แต่กล้ามเนื้ออ่อนแรงชัดและผื่นที่เปลือกตาไม่ใช่ลักษณะเด่น
- MCTD มี Raynaud มือบวม และ anti-U1 RNP สูง ภาพนี้ตรงกับ DM ชัดกว่า''',
            pearl="Heliotrope + Gottron + proximal weakness = DM", topic="Dermatomyositis",
            ref=[f"{D} หน้า 147–148, 151–152"], nl=["2.3.13-3(10)"]),
        mcq("RHEUM-06-01-2",
            "A 39-year-old woman has bilateral leg and thigh pain with weakness, redness around her eyes, and an erythematous rash over her upper back and shoulders. She takes simvastatin for dyslipidemia and recently completed a short course of steroids for an allergic reaction. Vital signs are normal. CK is 400 U/L and ESR is 70 mm/h. What is the most likely diagnosis?",
            "Dermatomyositis",
            ["Inclusion-body myositis", "Corticosteroid-induced myopathy", "Statin-induced myopathy", "Polymyositis"],
            kind="old", src=OLD,
            explain='''กล้ามเนื้ออ่อนแรง + **ผื่นรอบตา (heliotrope) + ผื่นที่หลังและไหล่ (shawl sign)** + CK และ ESR สูง = **dermatomyositis** — ยาที่ใช้เป็นตัวลวง
- IBM เป็นชายสูงอายุ อ่อนแรงอสมมาตรทั้งต้นและปลาย ไม่มีผื่น
- Steroid myopathy ใช้เวลานานและ CK ปกติ ไม่มีผื่น และเพิ่งใช้ระยะสั้น
- Statin myopathy ปวดกล้ามเนื้อ CK สูงได้ แต่ **ไม่มีผื่น heliotrope/shawl**
- Polymyositis ไม่มีผื่น''',
            pearl="ผื่น heliotrope/shawl แยก DM จาก statin หรือ steroid myopathy", topic="Dermatomyositis",
            ref=[f"{D} หน้า 147, 153–154"], nl=["2.3.13-3(10)", "2.3.13-3(7)"]),
        mcq("RHEUM-06-01-3",
            "A 48-year-old woman has had progressive weakness and shortness of breath for 1 year with an intermittent non-productive cough and difficulty raising her arms. SpO2 is 95%. Examination shows deltoid power grade 4 bilaterally, diffuse fine crackles in both lungs, and an erythematous rash on the periorbital area and elbows. Which test would confirm the diagnosis?",
            "Muscle biopsy",
            ["CT scan of the chest", "Pulmonary function tests", "Serum ANA titer", "Skin biopsy"],
            kind="old", src=OLD,
            explain='''Proximal weakness + ผื่นรอบตาและข้อศอก + **ILD** (ไอแห้ง crackles) = **dermatomyositis ที่มี ILD** → ยืนยันด้วย **muscle biopsy (gold standard)** (สไลด์หน้า 149)
- CT chest และ PFT ใช้ประเมินความรุนแรงของ ILD แต่ไม่ยืนยัน myositis
- ANA บวกได้ในหลายโรค ไม่จำเพาะ
- Skin biopsy ของ DM ดูเหมือน lupus (interface dermatitis) จึงไม่ยืนยันโรค''',
            pearl="ยืนยัน IIM = muscle biopsy", topic="IIM investigation",
            ref=[f"{D} หน้า 149, 155–156"], nl=["2.3.13-3(10)", "B1.6.1(1)"]),
        mcq("RHEUM-06-01-4",
            "A 12-year-old girl has had limb weakness for 6 months. Examination shows erythematous patches on both cheeks and the nose, purplish-red plaques over the knuckles of both hands, proximal muscle power grade 3, and distal muscle power grade 4. Which investigation is most helpful in establishing the diagnosis?",
            "Muscle biopsy",
            ["Urinalysis", "Antinuclear antibody", "Anti-dsDNA antibody", "Electromyography"],
            kind="old", src=OLD,
            explain='''**ผื่นม่วงแดงบน knuckles (Gottron) + proximal weakness** = **juvenile dermatomyositis** (ผื่นที่แก้มเป็น malar-like rash ใน DM ได้) → **muscle biopsy = gold standard** (สไลด์เฉลย)
- UA ใช้หา lupus nephritis ถ้าคิดว่าเป็น SLE แต่ Gottron ไม่ใช่ผื่นของ SLE
- ANA บวกได้ในหลายโรค ไม่จำเพาะ
- Anti-dsDNA ใช้สำหรับ SLE
- EMG ช่วยบอกว่าเป็น myopathy แต่ไม่จำเพาะเท่า biopsy (บางตำราให้ EMG เป็นขั้นแรกที่ไม่รุกล้ำ — ข้อสอบให้ยึด biopsy)''',
            pearl="Gottron + proximal weakness → muscle biopsy ยืนยัน", topic="Juvenile DM",
            ref=[f"{D} หน้า 149, 157–158"], nl=["2.3.13-3(10)", "B1.6.1(1)"]),
        mcq("RHEUM-06-01-5",
            "A 58-year-old woman is newly diagnosed with dermatomyositis confirmed by muscle biopsy. She has no respiratory symptoms. Apart from starting corticosteroids, which additional evaluation is most important?",
            "Age-appropriate cancer screening",
            ["HLA-B27 typing", "Serum uric acid", "Thyroid ultrasound", "Bone marrow biopsy"],
            explain='''IIM โดยเฉพาะ **dermatomyositis ในผู้ใหญ่ สัมพันธ์กับมะเร็ง** → ต้องทำ **age-appropriate cancer screening** ทุกราย (สไลด์หน้า 145, 150) เช่น ตรวจภายใน mammogram ส่องกล้องลำไส้ CT ตามความเหมาะสม (เสริม)
- HLA-B27 ใช้กับ spondyloarthropathy
- Uric acid ไม่เกี่ยวกับ IIM
- Thyroid ultrasound ไม่จำเป็น (ถ้าสงสัย hypothyroid myopathy ตรวจ TSH)
- Bone marrow biopsy ไม่มีข้อบ่งชี้ถ้า CBC ปกติ''',
            pearl="DM ผู้ใหญ่ → คัดกรองมะเร็งตามอายุทุกราย", topic="IIM and malignancy",
            ref=[f"{D} หน้า 145, 150"], nl=["2.3.13-3(10)"]),
    ])

# ---------------------------------------------------------------- 06-02 IgA vasculitis
F_VASC = fig("rheum-06-02-f1", "Vasculitis แบ่งตามขนาดหลอดเลือด (เสริม)", '''<svg viewBox="0 0 740 330">
 <path d="M20 60H720" class="lnf"/>
 <text x="20" y="40" class="t3">ใหญ่</text>
 <text x="720" y="40" text-anchor="end" class="t3">เล็ก</text>
 <rect x="20" y="70" width="210" height="44" rx="10" class="c2"/>
 <text x="125" y="97" text-anchor="middle" class="tw">Large vessel</text>
 <rect x="265" y="70" width="210" height="44" rx="10" class="c1"/>
 <text x="370" y="97" text-anchor="middle" class="tw">Medium vessel</text>
 <rect x="510" y="70" width="210" height="44" rx="10" class="bad"/>
 <text x="615" y="97" text-anchor="middle" class="tw">Small vessel</text>
 <rect x="20" y="124" width="210" height="196" rx="10" class="c2soft"/>
 <text x="30" y="146" class="tb">Takayasu arteritis</text>
 <text x="30" y="164" class="t3">หญิง &lt; 40 · ชีพจรแขนเบา</text>
 <text x="30" y="182" class="t3">BP สองแขนต่างกัน</text>
 <text x="30" y="210" class="tb">Giant cell arteritis</text>
 <text x="30" y="228" class="t3">&gt; 50 ปี · ปวดขมับ jaw</text>
 <text x="30" y="246" class="t3">claudication · ตามัว</text>
 <text x="30" y="264" class="t3">ESR สูง → steroid ทันที</text>
 <rect x="265" y="124" width="210" height="196" rx="10" class="c1soft"/>
 <text x="275" y="146" class="tb">Polyarteritis nodosa</text>
 <text x="275" y="164" class="t3">HBV · mononeuritis</text>
 <text x="275" y="182" class="t3">multiplex · ไม่มี GN</text>
 <text x="275" y="210" class="tb">Kawasaki disease</text>
 <text x="275" y="228" class="t3">เด็ก &lt; 5 ปี ไข้ ≥ 5 วัน</text>
 <text x="275" y="246" class="t3">coronary aneurysm</text>
 <text x="275" y="264" class="t3">→ IVIG + aspirin</text>
 <rect x="510" y="124" width="210" height="196" rx="10" class="badsoft"/>
 <text x="520" y="146" class="tb">ANCA-associated</text>
 <text x="520" y="164" class="t3">GPA (c-ANCA/PR3)</text>
 <text x="520" y="182" class="t3">MPA, EGPA (p-ANCA/MPO)</text>
 <text x="520" y="210" class="tb">Immune complex</text>
 <text x="520" y="228" class="ta">IgA vasculitis (HSP)</text>
 <text x="520" y="246" class="t3">cryoglobulinemia (HCV)</text>
 <text x="520" y="264" class="t3">anti-GBM</text>
 <text x="520" y="292" class="t2">palpable purpura + GN</text>
 <text x="520" y="310" class="t2">เป็นลักษณะของกลุ่มนี้</text>
</svg>''', "เรียงจากหลอดเลือดใหญ่ไปเล็กตาม Chapel Hill 2012 · IgA vasculitis (ตัวสีหลัก) อยู่ในกลุ่ม small vessel immune complex ซึ่งให้ palpable purpura และ glomerulonephritis — ทั้งภาพเป็นเนื้อหาเสริมนอกสไลด์")

S2 = sec("rheum-06-02", "IgA vasculitis (Henoch–Schönlein purpura)",
    "เด็ก < 10 ปี หลัง URI · palpable purpura + arthritis + abdominal pain · ไต (IgAV nephritis) และ intussusception · plt และ coag ปกติ · UA ทุกราย · skin biopsy ถ้าไม่แน่ใจ · supportive · steroid เมื่อ nephritis/ปวดท้องรุนแรง/ถ่ายเป็นเลือด", minutes=7,
    source=f"{D} หน้า 159–163", nl=["2.3.13-3(2)", "2.3.13-3(16)", "2.1.58"],
    md='''
### นิยามและกลไก (สไลด์หน้า 159)
- **Small-vessel vasculitis** ที่พบบ่อยที่สุดในเด็ก · **เด็ก < 10 ปี** · มัก **ตามหลัง URI**
- กลไก (เสริม): IgA1 ที่ผิดปกติ (galactose-deficient) จับเป็น **immune complex** ตกที่ผนังหลอดเลือดเล็กของผิวหนัง ลำไส้ ไต (ดู IgA ที่ mesangium เหมือน IgA nephropathy)

### อาการ — tetrad (สไลด์หน้า 159)
1. **Palpable purpura** (ทุกราย) — ที่ **ขาและก้น** (ส่วนที่ห้อย) กดไม่จาง · **platelet ปกติ** (ต่างจาก ITP)
2. **Arthritis/arthralgia** — ข้อเข่า ข้อเท้า ไม่มี deformity
3. **Abdominal pain** (ปวดบิดรอบสะดือ ± ถ่ายเป็นเลือด)
4. **Renal involvement (IgAV nephritis)** — hematuria/proteinuria ถึง nephritic syndrome

### ภาวะแทรกซ้อน (สไลด์หน้า 159)
- **IgAV nephritis** (nephritic syndrome) — ตัวกำหนดพยากรณ์โรคระยะยาว
- **Intussusception** (ileo-ileal มากกว่า ileocolic — เสริม) → ปวดท้องรุนแรง อาเจียน ถ่ายเป็นเลือด → ultrasound ช่องท้อง

### Investigation (สไลด์หน้า 160)
- **วินิจฉัยทางคลินิก**
- **Platelet และ coagulogram ปกติ** (purpura ไม่ได้มาจากเกล็ดเลือดต่ำ)
- **BUN, Cr** อาจสูง
- **UA: proteinuria, hematuria, RBC cast, dysmorphic RBC** → **ต้องตรวจ UA ทุกราย** เพื่อหาไต (ติดตาม UA ต่อ ~6 เดือน — เสริม)
- **Skin biopsy** (leukocytoclastic vasculitis + IgA deposit) ใช้ยืนยัน — **มักไม่จำเป็น** ทำเมื่อวินิจฉัยไม่แน่ใจ · **renal biopsy** เมื่อมี nephritis รุนแรง (เสริม)

### การรักษา (สไลด์หน้า 161)
- **Supportive**: hydration, **NSAID/paracetamol** แก้ปวด (เลี่ยง NSAID ถ้ามีไตเสื่อม — เสริม)
- **Steroid** เมื่อ: **IgAV nephritis**, **ปวดท้องรุนแรง**, **rectal bleeding**
- ส่วนใหญ่หายเองใน 4 สัปดาห์ (เสริม)

[[fig:rheum-06-02-f1]]
''',
    figs=[F_VASC],
    pearls=[
        "IgAV = เด็ก < 10 ปีหลัง URI + palpable purpura ขา/ก้น + arthritis + ปวดท้อง",
        "Platelet และ coagulogram ปกติ → แยกจาก ITP",
        "UA ทุกราย หา IgAV nephritis (ตัวกำหนดพยากรณ์)",
        "ปวดท้องรุนแรงอาเจียนถ่ายเป็นเลือด → คิด intussusception",
        "Supportive · steroid เมื่อ nephritis, ปวดท้องรุนแรง, rectal bleeding",
    ],
    items=[
        mcq("RHEUM-06-02-1",
            "A 5-year-old boy presents with abdominal pain and right ankle pain for 2 days. Temperature is 37°C, PR 100/min. The abdomen is soft with mild periumbilical tenderness. There are multiple non-blanchable violaceous papules on both legs, and the right ankle is swollen and tender but not warm. What is the most appropriate investigation?",
            "Urinalysis",
            ["ESR", "CRP", "Skin biopsy", "ANCA"],
            kind="old", src=OLD,
            explain='''เด็ก + **palpable purpura ที่ขา + ข้ออักเสบ + ปวดท้อง** = **IgA vasculitis** ซึ่งวินิจฉัยทางคลินิกได้ → สิ่งสำคัญคือ **ดูว่าไตเกี่ยวหรือไม่** ด้วย **urinalysis** (สไลด์เฉลย: ดู renal involvement)
- ESR และ CRP ไม่จำเพาะ ไม่เปลี่ยนการดูแล
- Skin biopsy ใช้เฉพาะเมื่อวินิจฉัยไม่แน่ใจ
- ANCA ใช้ในกลุ่ม ANCA-associated vasculitis (GPA, MPA) ซึ่งพบในผู้ใหญ่ และ IgAV จะ ANCA ลบ''',
            pearl="IgAV → UA ทุกรายหา nephritis", topic="IgAV investigation",
            ref=[f"{D} หน้า 160, 162–163"], nl=["2.3.13-3(2)"]),
        mcq("RHEUM-06-02-2",
            "A 7-year-old girl developed a rash on both legs and buttocks 1 week after an upper respiratory infection. Examination shows palpable, non-blanchable purpura on the lower limbs and buttocks and swelling of both knees. What laboratory result is most expected?",
            "Normal platelet count and normal coagulation studies",
            ["Platelet count below 20,000/mm3", "Prolonged aPTT that corrects with mixing", "Positive c-ANCA", "Schistocytes with thrombocytopenia"],
            explain='''Purpura ใน **IgA vasculitis** เกิดจาก **หลอดเลือดอักเสบ** ไม่ใช่เกล็ดเลือดต่ำ → **platelet และ coagulogram ปกติ** (สไลด์หน้า 160)
- Platelet < 20,000 เป็นของ ITP — purpura ของ ITP เป็นจุดเรียบ ไม่นูน และกระจายทั่วตัว
- aPTT ยาวที่แก้ได้ด้วย mixing คือขาด factor เช่น hemophilia ซึ่งมีเลือดออกในข้อ
- c-ANCA บวกพบใน GPA ในผู้ใหญ่
- Schistocyte + platelet ต่ำ เป็น HUS/TTP (เด็กหลังท้องเสียเป็นเลือด → HUS)''',
            pearl="Palpable purpura + platelet ปกติ = vasculitis (IgAV) ไม่ใช่ ITP", topic="IgAV lab",
            ref=[f"{D} หน้า 160"], nl=["2.3.13-3(2)", "2.1.58"]),
        mcq("RHEUM-06-02-3",
            "A 6-year-old boy with IgA vasculitis diagnosed 4 days ago develops severe colicky abdominal pain, repeated vomiting, and red currant jelly stool. What is the most important complication to evaluate first?",
            "Intussusception, by abdominal ultrasonography",
            ["IgA vasculitis nephritis, by renal biopsy", "Acute pancreatitis, by serum lipase", "Acute appendicitis, by CT abdomen", "Meckel diverticulum, by technetium scan"],
            explain='''ภาวะแทรกซ้อนสำคัญของ IgAV คือ **intussusception** (สไลด์หน้า 159) — ปวดบิดเป็นพัก ๆ + อาเจียน + **อุจจาระเหมือนแยมลูกเกด** → **ultrasound ช่องท้อง** ทันที
- IgAV nephritis สำคัญระยะยาวแต่ไม่อธิบายอาการลำไส้อุดตัน และ renal biopsy ไม่ใช่การตรวจฉุกเฉิน
- Pancreatitis เกิดได้น้อยใน IgAV และไม่มีอุจจาระเป็นเลือดแบบแยม
- Appendicitis ปวดย้ายไปท้องขวาล่าง ไม่มีอุจจาระเป็นเลือด
- Meckel diverticulum ทำให้ถ่ายเป็นเลือดแบบไม่ปวด''',
            pearl="IgAV + ปวดบิด อาเจียน currant jelly stool → U/S หา intussusception", topic="IgAV complications",
            ref=[f"{D} หน้า 159"], nl=["2.3.13-3(2)", "2.1.11"]),
        mcq("RHEUM-06-02-4",
            "An 8-year-old boy with IgA vasculitis has palpable purpura and mild knee pain. Urinalysis shows protein 2+, RBC 20–30/HPF with RBC casts, and creatinine has risen from 0.4 to 0.8 mg/dL. Blood pressure is 125/85 mmHg. What is the most appropriate treatment?",
            "Systemic corticosteroid",
            ["Supportive care with ibuprofen only", "Intravenous immunoglobulin", "Platelet transfusion", "Ceftriaxone"],
            explain='''IgAV ที่มี **nephritis** (RBC cast, proteinuria, Cr สูงขึ้น) = ข้อบ่งชี้ของ **steroid** ตามสไลด์ (nephritis, ปวดท้องรุนแรง, rectal bleeding) · nephritis รุนแรงพิจารณา renal biopsy และ immunosuppressant (เสริม)
- Supportive + ibuprofen ใช้ในรายที่ไม่มีไต และ NSAID ควรเลี่ยงเมื่อไตเสื่อม
- IVIG ใช้ใน Kawasaki disease หรือ ITP
- Platelet ปกติใน IgAV ไม่ต้องให้เกล็ดเลือด
- Ceftriaxone ไม่มีบทบาท เพราะไม่ใช่การติดเชื้อ''',
            pearl="IgAV + nephritis/ปวดท้องรุนแรง/ถ่ายเป็นเลือด → steroid", topic="IgAV treatment",
            ref=[f"{D} หน้า 161"], nl=["2.3.13-3(2)", "2.3.14(2)"]),
    ])

LECTURE = lecture("06", "Inflammatory myopathy & IgA vasculitis", "DM · PM · IBM · muscle biopsy · HSP · palpable purpura",
    objectives=[
        "แยก DM, PM, IBM จากรูปแบบกล้ามเนื้ออ่อนแรงและผื่น",
        "เลือก muscle biopsy เป็นการยืนยัน IIM และคัดกรองมะเร็ง/ILD",
        "วินิจฉัย IgA vasculitis จาก tetrad และแยกจาก ITP",
        "ส่ง UA หา IgAV nephritis และเลือกเมื่อใดควรให้ steroid",
    ],
    sections=[S1, S2])
