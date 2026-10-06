from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Hemato"

# ---------------------------------------------------------------- 07-01 HL vs NHL
F_LYM = fig("hemato-07-01-f1", "Hodgkin vs non-Hodgkin lymphoma และ Ann Arbor staging", '''<svg viewBox="0 0 740 414">
 <rect x="20" y="10" width="340" height="40" rx="10" class="c1"/>
 <text x="190" y="35" text-anchor="middle" class="tw">Hodgkin lymphoma (HL)</text>
 <rect x="380" y="10" width="340" height="40" rx="10" class="c2"/>
 <text x="550" y="35" text-anchor="middle" class="tw">Non-Hodgkin lymphoma (NHL)</text>
 <rect x="20" y="58" width="340" height="150" rx="10" class="c1soft"/>
 <text x="36" y="82" class="t2">• ลาม <tspan class="tb">ต่อเนื่อง (contiguous)</tspan></text>
 <text x="36" y="104" class="t2">• Cervical, supraclavicular, mediastinum</text>
 <text x="36" y="126" class="t2">• Extranodal พบน้อย</text>
 <text x="36" y="148" class="t2">• Reed–Sternberg (owl-eye)</text>
 <text x="36" y="170" class="t2">• Risk: EBV, HIV</text>
 <text x="36" y="194" class="t3">วัยรุ่น–ผู้ใหญ่ตอนต้น (และ &gt; 55 ปี)</text>
 <rect x="380" y="58" width="340" height="150" rx="10" class="c2soft"/>
 <text x="396" y="82" class="t2">• ลาม <tspan class="tb">ไม่ต่อเนื่อง (noncontiguous)</tspan></text>
 <text x="396" y="104" class="t2">• <tspan class="tb">Extranodal</tspan>: GI, skin, BM, CNS</text>
 <text x="396" y="126" class="t2">• BM infiltration → cytopenia</text>
 <text x="396" y="148" class="t2">• Risk: EBV, HIV, H. pylori, autoimmune</text>
 <text x="396" y="170" class="t2">• พบบ่อยกว่า HL</text>
 <text x="396" y="194" class="t3">ผู้ใหญ่ อายุมากขึ้น</text>
 <rect x="20" y="218" width="700" height="34" rx="8" class="sunk"/>
 <text x="370" y="240" text-anchor="middle" class="tb">ทั้งคู่: painless LN · B symptoms · excisional biopsy (FNA ไม่พอ) · PET-CT staging · chemo ± RT</text>
 <text x="370" y="276" text-anchor="middle" class="ta">Ann Arbor staging (เสริม)</text>
 <rect x="20" y="288" width="170" height="100" rx="10" class="box"/>
 <text x="105" y="312" text-anchor="middle" class="tb">Stage I</text>
 <text x="105" y="336" text-anchor="middle" class="t2">LN 1 กลุ่ม</text>
 <rect x="200" y="288" width="170" height="100" rx="10" class="box"/>
 <text x="285" y="312" text-anchor="middle" class="tb">Stage II</text>
 <text x="285" y="336" text-anchor="middle" class="t2">≥ 2 กลุ่ม</text>
 <text x="285" y="356" text-anchor="middle" class="t2">ข้างเดียวของกะบังลม</text>
 <rect x="380" y="288" width="170" height="100" rx="10" class="box"/>
 <text x="465" y="312" text-anchor="middle" class="tb">Stage III</text>
 <text x="465" y="336" text-anchor="middle" class="t2">ทั้งสองข้าง</text>
 <text x="465" y="356" text-anchor="middle" class="t2">ของกะบังลม</text>
 <rect x="560" y="288" width="160" height="100" rx="10" class="badsoft"/>
 <text x="640" y="312" text-anchor="middle" class="tb">Stage IV</text>
 <text x="640" y="336" text-anchor="middle" class="t2">extranodal</text>
 <text x="640" y="356" text-anchor="middle" class="t2">กระจาย (BM, ตับ)</text>
 <text x="370" y="406" text-anchor="middle" class="t3">ต่อท้าย A = ไม่มี B symptoms · B = มีไข้ เหงื่อออกกลางคืน น้ำหนักลด &gt; 10%</text>
</svg>''', "HL ลามต่อเนื่องและแทบไม่ออกนอกต่อม · NHL กระโดดและออก extranodal บ่อย · staging ดูจำนวนกลุ่มต่อมและด้านของกะบังลม (สไลด์หน้า 297 เป็นภาพ วาดใหม่เป็นเสริม)")

S1 = sec("hemato-07-01", "Lymphoma: Hodgkin & non-Hodgkin",
    "Painless LN + B symptoms · HL contiguous, Reed–Sternberg · NHL noncontiguous + extranodal · excisional biopsy (FNA ไม่พอ) · PET-CT · SVC syndrome", minutes=8,
    source=f"{D} หน้า 293–297, 300–303", nl=["B2.2.4-3(3)", "2.1.57", "2.2.13"],
    md='''
### Hodgkin lymphoma (HL)

- Risk: **EBV, HIV**
- **Painless lymphadenopathy** ลามแบบ **contiguous** (ต่อมข้างเคียงกันเป็นลำดับ)
  - Cervical, supraclavicular, axillary, inguinal
  - **Mediastinal LN → SVC syndrome**
- Hepatosplenomegaly · **extranodal involvement พบน้อย**
- **B symptoms**: night sweats, น้ำหนักลด, ไข้ (Pel–Ebstein — เสริม)
- วินิจฉัย: **excisional หรือ incisional biopsy** (**FNA ไม่พอ** เพราะต้องดูโครงสร้างต่อม) → **Reed–Sternberg cell (owl-eye)**
- Staging: **PET-CT/CT scan**
- Tx: chemotherapy (ABVD — เสริม), radiation

### Non-Hodgkin lymphoma (NHL)

- Risk: **EBV, HIV, H. pylori (MALT lymphoma), autoimmune disease**
- Painless lymphadenopathy ลามแบบ **noncontiguous**
- **Extranodal involvement**: GI tract, skin, bone marrow, CNS
- Hepatosplenomegaly, B symptoms
- CBC: ↓Hb, ↓platelet, lymphocytosis (กรณี **BM infiltration**)
- วินิจฉัย: **excisional lymph node/tissue biopsy** · staging: PET-CT/CT
- Tx: chemotherapy (R-CHOP — เสริม), radiation

[[fig:hemato-07-01-f1]]

### SVC syndrome (ภาวะฉุกเฉิน)

- ก้อนใน mediastinum (lymphoma, มะเร็งปอด, thymoma, germ cell tumor) กด SVC → **หน้า แขน อกบวม**, หลอดเลือดดำที่คอและอกโป่ง, หายใจลำบาก
- ในคนอายุน้อยที่มี **ต่อมน้ำเหลืองโตหลายกลุ่ม + ตับม้ามโต** + SVC syndrome → **lymphoma**

> วัยรุ่นต่อมน้ำเหลืองโตหลายแห่ง ไม่เจ็บ + ไข้กลางคืน + น้ำหนักลด → **lymph node biopsy** (excisional) ไม่ใช่ FNA, CXR หรือ BM เป็นการตรวจแรกเพื่อวินิจฉัย
''',
    figs=[F_LYM],
    pearls=[
        "Lymphoma: painless LN + B symptoms → excisional LN biopsy (FNA ไม่พอ)",
        "HL: contiguous, Reed–Sternberg (owl-eye), extranodal น้อย",
        "NHL: noncontiguous, extranodal (GI, skin, BM, CNS), H. pylori → MALT",
        "Mediastinal LN → SVC syndrome",
        "Staging: PET-CT",
    ],
    items=[
        mcq("HEMATO-07-01-1",
            "A 15-year-old boy has neck and groin masses for 3 months with night fever and weight loss. PE: multiple 2–4 cm painless, rubbery cervical and inguinal lymph nodes. Hb 11.5 g/dL, WBC 12,000/µL (N 60%, L 40%), platelet 250,000/µL. What is the most useful investigation for diagnosis?",
            "Excisional lymph node biopsy",
            ["Chest x-ray", "CT of the head and neck", "Gastric lavage for AFB", "Bone marrow study"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Painless lymphadenopathy หลายกลุ่ม + **B symptoms** (ไข้กลางคืน น้ำหนักลด) = **lymphoma** → การวินิจฉัยต้องใช้ **lymph node biopsy** (excisional ดีที่สุด เห็นโครงสร้างต่อม)
- CXR ช่วยดู mediastinal mass/staging แต่ไม่ให้การวินิจฉัย
- CT head and neck ใช้ประเมินขอบเขต ไม่ได้ชิ้นเนื้อ
- Gastric lavage for AFB ใช้หา TB ในเด็กที่เสมหะไม่ได้ — TB lymphadenitis ก็ต้องใช้ชิ้นเนื้อเช่นกัน
- BM study ใช้ staging ไม่ใช่วินิจฉัยหลัก''',
            pearl="LN โต + B symptoms → excisional biopsy", topic="Lymphoma diagnosis",
            ref=[f"{D} หน้า 294, 300–301"], nl=["B2.2.4-3(3)", "2.1.57"]),
        mcq("HEMATO-07-01-2",
            "A 20-year-old woman has facial and chest swelling for 2 weeks. BT 37°C, RR 30/min, BP 110/90 mmHg. PE: edema of the face, arms, and chest wall with distended chest wall veins; bilateral cervical, axillary, and inguinal lymphadenopathy; hepatosplenomegaly. What is the most likely diagnosis?",
            "Lymphoma",
            ["Thymoma", "Germ cell tumor", "Teratoma", "Lung cancer"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''**SVC syndrome** (หน้า แขน อกบวม) จาก mediastinal mass + **ต่อมน้ำเหลืองโตทั่วร่าง** (คอ รักแร้ ขาหนีบ) + **ตับม้ามโต** = **lymphoma** (ในคนอายุน้อย)
- Thymoma อยู่ anterior mediastinum ได้ แต่ไม่ทำให้ต่อมน้ำเหลืองโตทั่วตัวและตับม้ามโต (สัมพันธ์กับ myasthenia gravis)
- Germ cell tumor/teratoma อยู่ anterior mediastinum ในคนหนุ่ม แต่ไม่อธิบาย generalized lymphadenopathy
- Lung cancer ทำให้ SVC syndrome ได้บ่อยในผู้สูงอายุที่สูบบุหรี่ ไม่ใช่หญิงอายุ 20 ที่มีตับม้ามโต''',
            pearl="SVC syndrome + LN ทั่วตัว + HSM = lymphoma", topic="SVC syndrome",
            ref=[f"{D} หน้า 294, 302–303"], nl=["2.2.13", "B2.2.4-3(3)"]),
        mcq("HEMATO-07-01-3",
            "A 22-year-old man has a painless left supraclavicular lymph node and a mediastinal mass. An excisional biopsy shows large binucleate cells with prominent eosinophilic nucleoli (owl-eye appearance) in a mixed inflammatory background. Disease is confined to the neck and mediastinum. Which statement about this disease is correct?",
            "It typically spreads to contiguous lymph node groups",
            ["Extranodal involvement is usually present at diagnosis", "Fine-needle aspiration is sufficient for diagnosis", "It is strongly associated with H. pylori infection", "Bone marrow biopsy is the preferred diagnostic test"],
            explain='''Reed–Sternberg cell (owl-eye) = **Hodgkin lymphoma** ซึ่ง**ลามต่อเนื่องเป็นกลุ่มต่อมข้างเคียง (contiguous)** — จึงพบคอ → mediastinum
- Extranodal involvement พบ**น้อย**ใน HL (เด่นใน NHL)
- FNA **ไม่พอ** ต้อง excisional/incisional biopsy
- H. pylori สัมพันธ์กับ gastric MALT lymphoma (NHL)
- BM biopsy ใช้ staging ในบางราย ไม่ใช่การวินิจฉัย''',
            pearl="HL = contiguous spread + RS cell", topic="Hodgkin lymphoma",
            ref=[f"{D} หน้า 294"], nl=["B2.2.4-3(3)"]),
        mcq("HEMATO-07-01-4",
            "A 58-year-old man has epigastric pain and weight loss. Endoscopy shows a gastric mass; biopsy reveals a low-grade B-cell lymphoma of mucosa-associated lymphoid tissue. Which infection is most strongly associated with this lymphoma?",
            "Helicobacter pylori",
            ["Epstein–Barr virus", "Hepatitis B virus", "Human T-lymphotropic virus type 1", "Cytomegalovirus"],
            explain='''Gastric **MALT lymphoma** เป็น extranodal NHL ที่สัมพันธ์กับ **H. pylori** (สไลด์ระบุ H. pylori เป็น risk ของ NHL) — ระยะแรกกำจัด H. pylori แล้วโรคถอยได้ (เสริม)
- EBV สัมพันธ์กับ HL, Burkitt, NK/T-cell lymphoma
- HBV ไม่ใช่ตัวหลักของ gastric lymphoma (HCV สัมพันธ์กับ splenic marginal zone — เสริม)
- HTLV-1 สัมพันธ์กับ adult T-cell leukemia/lymphoma
- CMV ไม่สัมพันธ์''',
            pearl="Gastric MALT lymphoma ↔ H. pylori", topic="NHL risk factors",
            ref=[f"{D} หน้า 296"], nl=["B2.2.4-3(3)"]),
    ])

# ---------------------------------------------------------------- 07-02 CLL
S2 = sec("hemato-07-02", "Chronic lymphocytic leukemia (CLL)",
    "ผู้สูงอายุ lymphocytosis > 5,000 · small mature lymphocyte + smudge cell · flow cytometry · LN/HSM, AIHA/ITP, ติดเชื้อง่าย · targeted therapy", minutes=6,
    source=f"{D} หน้า 298–299", nl=["B2.2.4-3(1)", "B2.2.4-3(3)"],
    md='''
### ลักษณะ

- มะเร็งของ **mature B lymphocyte** — พบบ่อยในผู้สูงอายุ (เสริม)
- ส่วนใหญ่ **asymptomatic** เจอจาก CBC

### อาการ

- **Painless lymphadenopathy**, B symptoms
- **Hepatosplenomegaly**
- Anemia, bleeding (BM infiltration หรือ **autoimmune: AIHA, ITP**)
- **Immunocompromise** (hypogammaglobulinemia → ติดเชื้อซ้ำ), **chronic pruritus**

### การตรวจ

- CBC/PBS: **lymphocytosis (> 5,000/µL)** ต่อเนื่อง
- **Small mature lymphocyte** + **smudge cell (basket cell)** = lymphocyte ที่เปราะแตกขณะทำสไลด์
- **Flow cytometry**: clonal B cell (CD5+, CD19+, CD23+ — เสริม)
- Staging Rai/Binet ตาม LN, ตับม้าม, anemia, thrombocytopenia (เสริม)

### การรักษา

- Early asymptomatic → **watch and wait** (เสริม)
- มีข้อบ่งชี้ (cytopenia, B symptoms, LN/ม้ามโตมาก) → **targeted therapy** (BTK inhibitor เช่น ibrutinib, venetoclax), **chemoimmunotherapy**

> ผู้สูงอายุ lymphocyte สูงมาก + **smudge cell** = CLL · ต่างจาก acute leukemia ที่เป็น **blast** และ CML ที่เป็น **granulocyte ทุกระยะ**
''',
    pearls=[
        "CLL: ผู้สูงอายุ + lymphocytosis > 5,000 + smudge cell",
        "ยืนยันด้วย flow cytometry",
        "ภาวะแทรกซ้อน: AIHA, ITP, ติดเชื้อง่าย (hypogammaglobulinemia)",
        "ไม่มีอาการ → watch and wait · มีอาการ → targeted therapy",
    ],
    items=[
        mcq("HEMATO-07-02-1",
            "A 70-year-old man is found to have an abnormal CBC on routine check-up. He is asymptomatic. PE: small painless cervical lymph nodes, no hepatosplenomegaly. CBC: Hb 13 g/dL, WBC 48,000/µL (lymphocytes 85%), platelet 190,000/µL. PBS: small mature-appearing lymphocytes with many smudge cells. What is the most appropriate investigation to confirm the diagnosis?",
            "Peripheral blood flow cytometry",
            ["Bone marrow biopsy for blast count", "BCR-ABL testing", "Monospot test", "Lymph node fine-needle aspiration"],
            explain='''ผู้สูงอายุ + lymphocytosis (> 5,000) ของ small mature lymphocyte + **smudge cell** = **CLL** → ยืนยันด้วย **flow cytometry** (clonal B cell) จากเลือดได้เลย
- BM biopsy ไม่จำเป็นในการวินิจฉัย CLL และไม่มี blast
- BCR-ABL ใช้กับ CML (granulocyte ทุกระยะ)
- Monospot ใช้กับ infectious mononucleosis (atypical lymphocyte ในคนหนุ่ม)
- FNA ต่อมน้ำเหลืองไม่จำเป็นเมื่อวินิจฉัยจากเลือดได้''',
            pearl="Smudge cell → flow cytometry (CLL)", topic="CLL diagnosis",
            ref=[f"{D} หน้า 298"], nl=["B2.2.4-3(1)"]),
        mcq("HEMATO-07-02-2",
            "A 72-year-old woman with known CLL develops fatigue and jaundice over 2 weeks. Hb 7.2 g/dL, reticulocyte 9%, WBC 62,000/µL (lymphocytes 90%), platelet 140,000/µL, LDH and indirect bilirubin elevated. PBS: spherocytes and smudge cells. What is the most likely cause of her worsening anemia?",
            "Autoimmune hemolytic anemia",
            ["Bone marrow failure from CLL infiltration", "Richter transformation to acute leukemia", "Iron deficiency from GI bleeding", "Hypersplenism"],
            explain='''CLL สัมพันธ์กับ **autoimmune** (AIHA, ITP) — ซีดลงเร็ว + **retic สูง** + LDH/indirect bilirubin สูง + **spherocyte** = **warm AIHA** (ตรวจ DAT ยืนยัน, รักษาด้วย steroid)
- BM infiltration ทำให้ซีดแต่ **retic ต่ำ** ไม่มี hemolysis
- Richter transformation คือเปลี่ยนเป็น aggressive lymphoma (LN โตเร็ว ไข้ LDH สูง) ไม่ใช่ spherocyte
- IDA ให้ microcytic retic ต่ำ
- Hypersplenism ต้องมีม้ามโตมาก และไม่ทำให้ spherocyte เด่น''',
            pearl="CLL + ซีด retic สูง + spherocyte = AIHA", topic="CLL complications",
            ref=[f"{D} หน้า 218, 298"], nl=["B2.2.4-3(1)", "2.3.3(4)"]),
        mcq("HEMATO-07-02-3",
            "Which peripheral blood smear finding is most characteristic of chronic lymphocytic leukemia?",
            "Smudge cells",
            ["Auer rods", "Teardrop cells", "Rouleaux formation", "Atypical reactive lymphocytes"],
            explain='''**Smudge (basket) cell** คือ lymphocyte ที่เปราะแตกระหว่างทำสไลด์ — เด่นใน **CLL** ร่วมกับ small mature lymphocyte จำนวนมาก
- Auer rod = AML (myeloblast)
- Teardrop cell = myelofibrosis/myelophthisis
- Rouleaux = multiple myeloma
- Atypical reactive lymphocyte = infectious mononucleosis/dengue''',
            pearl="Smudge cell = CLL", topic="CLL smear",
            ref=[f"{D} หน้า 298"], nl=["3.1.2"]),
    ])

LECTURE = lecture("07", "Lymphoma & CLL",
    "Hodgkin · non-Hodgkin · SVC syndrome · chronic lymphocytic leukemia",
    objectives=[
        "นึกถึง lymphoma จาก painless LN + B symptoms และเลือก excisional biopsy ได้",
        "แยก Hodgkin กับ non-Hodgkin lymphoma จากรูปแบบการลามและ extranodal",
        "จำ SVC syndrome จาก mediastinal lymphoma",
        "วินิจฉัย CLL จาก lymphocytosis + smudge cell และรู้ภาวะแทรกซ้อน autoimmune",
    ],
    sections=[S1, S2])
