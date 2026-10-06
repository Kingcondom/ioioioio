from lib import lecture, sec, mcq, fig

D = "สไลด์ Update ข้อสอบ 2025"
SRC = "NL2 2025 (update)"

def R(*p):
    return [f"{D} หน้า " + ", ".join(str(x) for x in p)]

# ---------------------------------------------------------------- 05-01 Hyperthyroid
S1 = sec("exam25-05-01", "Hyperthyroidism & antithyroid drugs",
    "First-line = MMI · ไข้ เจ็บคอ หลังเริ่ม ATD → CBC (agranulocytosis) · storm → PTU ก่อน แล้วจึงให้ iodine", minutes=5,
    source=f"{D} หน้า 99–105", nl=["2.3.4(9)", "2.3.4-3(3)", "2.3.3(2)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**เลือก antithyroid drug (ATD)**
- **Methimazole (MMI) = first-line** (กินวันละครั้ง ผลต่อตับน้อยกว่า)
- **PTU** ใช้เมื่อ: **ไตรมาสแรกของการตั้งครรภ์**, **thyroid storm**, แพ้ MMI (ที่ไม่รุนแรง)

**ผลข้างเคียงรุนแรงของ ATD (สไลด์)**

| ผลข้างเคียง | อาการ | ตรวจ |
|---|---|---|
| **Agranulocytosis** (มักใน 3 เดือนแรก) | **ไข้ + เจ็บคอ/แผลในปาก** | **CBC (ANC < 500)** |
| Hepatitis (PTU > MMI) | ดีซ่าน ปวดท้อง | LFT |

- ถ้ามี major S/E → หยุดยา แล้วเปลี่ยนเป็น **RAI (กลืนแร่) หรือผ่าตัด** — ห้ามเปลี่ยน MMI ↔ PTU เพราะ cross-reactivity (เสริม)

**Thyroid storm — ลำดับยา (สไลด์)**
1. ยับยั้งการสร้าง: **PTU > MMI** (PTU ยับยั้ง T4 → T3 ที่ peripheral ด้วย)
2. ยับยั้งการหลั่ง: **Lugol/SSKI ให้หลัง thionamide ≥ 1 ชม.** (Wolff–Chaikoff)
3. ยับยั้ง T4 → T3 และคุมอาการ: **propranolol** · **hydrocortisone/dexamethasone** (relative adrenal insufficiency)
''',
    pearls=[
        "Hyperthyroid ทั่วไป → MMI · ไตรมาสแรก/storm → PTU",
        "กิน ATD แล้วไข้ + เจ็บคอ → CBC หา agranulocytosis",
        "Storm: PTU ก่อน แล้วจึงให้ iodine อย่างน้อย 1 ชม.",
        "Major S/E ของ ATD → เปลี่ยนเป็น RAI/ผ่าตัด",
    ],
    items=[
        mcq("EXAM25-05-01-1",
            "A 24-year-old woman is diagnosed with new-onset Graves hyperthyroidism. She is not pregnant and has no liver disease. Which medication is preferred as first-line therapy?",
            "Methimazole",
            ["Propylthiouracil", "Radioactive iodine", "Total thyroidectomy", "Beta-blocker alone"],
            kind="old", src=SRC,
            explain='''**Methimazole** เป็นยา first-line ของ hyperthyroidism (กินวันละครั้ง hepatotoxicity น้อยกว่า PTU)
- PTU สงวนไว้สำหรับไตรมาสแรกของการตั้งครรภ์ thyroid storm หรือแพ้ MMI เพราะเสี่ยง hepatitis รุนแรง
- RAI เป็นทางเลือกได้ แต่ไม่ใช่ "first-line medication" และในหญิงวัยเจริญพันธุ์ต้องคุมกำเนิดหลังกลืนแร่
- Thyroidectomy ใช้เมื่อคอพอกใหญ่กดเบียด สงสัยมะเร็ง หรือรักษาอื่นไม่ได้
- Beta-blocker คุมอาการ แต่ไม่ได้ลดการสร้างฮอร์โมน''',
            pearl="Hyperthyroid ไม่ตั้งครรภ์ → MMI", topic="Antithyroid drugs",
            ref=R(99, 100), nl=["2.3.4(9)"]),
        mcq("EXAM25-05-01-2",
            "A 36-year-old woman with hyperthyroidism, on methimazole and propranolol for 2 months, presents with a 3-day history of high-grade fever and severe sore throat. There are multiple ulcerative lesions in the oropharynx. She appears toxic and tachycardic and has no cough. What is the best initial investigation?",
            "Complete blood count",
            ["Blood culture", "Throat swab for bacterial culture", "Rapid streptococcal antigen test", "Epstein-Barr virus serology"],
            kind="old", src=SRC,
            explain='''ไข้สูง + เจ็บคอ + **แผลในช่องปาก** ในผู้ที่เพิ่งเริ่ม **MMI 2 เดือน** = ต้องคิดถึง **agranulocytosis** เป็นอันดับแรก → **CBC ด่วน** (ANC < 500) แล้วหยุดยาทันที ให้ broad-spectrum ATB ตามแนวทาง febrile neutropenia
- Blood culture ต้องเก็บด้วย แต่ไม่ได้ให้การวินิจฉัยหลัก
- Throat swab และ rapid strep test มองหา strep pharyngitis ซึ่งจะพลาดภาวะที่อันตรายถึงชีวิต
- EBV serology ไม่ใช่ลำดับแรก และ IM ไม่ทำให้แผลในปากหลายแห่งแบบนี้''',
            pearl="กิน MMI/PTU แล้วไข้ + เจ็บคอ → CBC", topic="Agranulocytosis",
            ref=R(101, 102), nl=["2.3.3(2)", "2.3.4(9)"]),
        mcq("EXAM25-05-01-3",
            "A 40-year-old man presents with acute confusion, agitation and fever. Temperature 38.9 °C, irregularly irregular pulse 130/min. He has a diffuse goiter and moist skin. Free T4 8.0 ng/dL, TSH < 0.001 mIU/L. What is the most appropriate initial management?",
            "Propylthiouracil",
            ["Methimazole", "Lugol's solution", "Propranolol", "Haloperidol"],
            kind="old", src=SRC,
            explain='''ไข้ + สับสน + AF + thyrotoxicosis = **thyroid storm** → ยาตัวแรกคือ **thionamide โดยเลือก PTU** เพราะนอกจากยับยั้งการสร้างแล้วยังยับยั้ง T4 → T3 ที่ peripheral
- MMI ใช้ได้ใน storm แต่สไลด์ (และข้อสอบ) เลือก PTU เพราะลด T3 ได้เร็วกว่า
- Lugol's solution ต้องให้ **หลัง** thionamide อย่างน้อย 1 ชม. ถ้าให้ก่อนจะกลายเป็นวัตถุดิบสร้างฮอร์โมนเพิ่ม
- Propranolol ให้ร่วมเพื่อคุมอาการ แต่ไม่ได้หยุดการสร้างฮอร์โมน (ตัวเลือกนี้ถูกบางส่วน — ข้อสอบตอบ PTU)
- Haloperidol ไม่ได้รักษาสาเหตุของความสับสน''',
            pearl="Thyroid storm → PTU ก่อน แล้วจึง iodine", topic="Thyroid storm",
            ref=R(103, 104, 105), nl=["2.3.4-3(3)"]),
    ])

# ---------------------------------------------------------------- 05-02 Goiter & nodule
S2 = sec("exam25-05-02", "Goiter & thyroid nodule",
    "Goiter + euthyroid + anti-TPO สูง = Hashimoto · nodule + TSH ต่ำ → thyroid scan (hot nodule โอกาสมะเร็งน้อย)", minutes=4,
    source=f"{D} หน้า 106–110", nl=["2.3.4-3(2)", "2.3.4(3)", "B11.2.4-3(1)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Hashimoto thyroiditis (euthyroid phase)**: คอพอกโตทั่วไป **ไม่เจ็บ เนื้อหยุ่น (rubbery)** · TFT ปกติ · **anti-TPO/anti-Tg สูง** → ไม่ต้องรักษา **ติดตาม TSH** เพราะจะกลายเป็น hypothyroid

| โรค | ลักษณะ |
|---|---|
| Hashimoto | คอพอกไม่เจ็บ anti-TPO สูง TFT ปกติหรือ hypo |
| Graves | TSH ต่ำ FT4 สูง TRAb บวก exophthalmos |
| Subacute (de Quervain) | **ต่อมเจ็บมาก** หลังหวัด ESR สูง uptake ต่ำ |
| Simple goiter | TFT ปกติ antibody ลบ |
| Thyroid lymphoma | คอโตเร็วในผู้สูงอายุที่มี Hashimoto เดิม |

**Thyroid nodule (สไลด์)**
1. ตรวจ **TSH** ก่อน
2. **TSH ต่ำ** → **thyroid scan & uptake**: **hot nodule** = ทำงานเอง โอกาสมะเร็งน้อย → รักษา hyperthyroid (ไม่ต้อง FNA) · cold/warm → U/S + พิจารณา FNA
3. **TSH ปกติ/สูง** → **thyroid U/S** → FNA ตามขนาดและลักษณะที่เสี่ยงมะเร็ง · cold nodule โอกาสมะเร็ง 5–15%
''',
    pearls=[
        "คอพอกไม่เจ็บ + TFT ปกติ + anti-TPO สูง = Hashimoto → ติดตาม TSH",
        "Nodule + TSH ต่ำ → thyroid scan ก่อน (hot nodule ไม่ต้อง FNA)",
        "Nodule + TSH ปกติ/สูง → U/S แล้ว FNA ตามเกณฑ์",
    ],
    items=[
        mcq("EXAM25-05-02-1",
            "A 40-year-old woman has a diffuse, non-tender, rubbery goiter. Free T3 3.5 pg/mL (normal), TSH 2.0 mIU/L (normal), anti-TPO antibody 350 IU/mL (high). What is the diagnosis?",
            "Hashimoto thyroiditis",
            ["Simple goiter", "Graves disease", "Subacute thyroiditis", "Thyroid lymphoma"],
            kind="old", src=SRC,
            explain='''คอพอกโตทั่วไป ไม่เจ็บ + **TFT ปกติ** + **anti-TPO สูง** = **Hashimoto thyroiditis ระยะ euthyroid** → ไม่ต้องให้ยา ติดตาม TSH เป็นระยะ (เสี่ยงกลายเป็น hypothyroid)
- Simple goiter ไม่มี antibody ต่อต่อมไทรอยด์
- Graves มี TSH ต่ำ FT3/FT4 สูง และ TRAb บวก
- Subacute thyroiditis ต่อมจะเจ็บมาก มีไข้ ESR สูง มักมี thyrotoxic phase
- Thyroid lymphoma เกิดใน Hashimoto ได้ แต่จะมาด้วยก้อนโตเร็ว กดเบียด ในผู้สูงอายุ''',
            pearl="Goiter + euthyroid + anti-TPO สูง = Hashimoto", topic="Hashimoto thyroiditis",
            ref=R(106, 107), nl=["2.3.4-3(2)", "2.3.4(3)"]),
        mcq("EXAM25-05-02-2",
            "A 40-year-old woman presents with 6 months of palpitations and unintentional weight loss. BMI 18 kg/m², pulse 120/min. There is a 2-cm left thyroid nodule. FT3 10.2 pg/mL (high), FT4 4.6 ng/dL (high), TSH 0.01 μIU/mL (low). What is the most appropriate next diagnostic step?",
            "Thyroid scan and uptake study",
            ["Fine-needle aspiration", "Thyroid ultrasound", "TSH receptor antibody", "Anti-TPO antibody"],
            kind="old", src=SRC,
            explain='''Thyroid nodule ที่มี **TSH ต่ำ (hyperthyroid)** → ขั้นต่อไปคือ **thyroid scan & uptake** เพื่อดูว่าเป็น **hot (autonomous/toxic) nodule** หรือไม่ ถ้า hot โอกาสมะเร็งต่ำมาก ไม่ต้อง FNA และรักษา hyperthyroid
- FNA ทำใน cold/indeterminate nodule หลังรู้ผล scan และ U/S
- Thyroid U/S เป็นขั้นแรกเมื่อ TSH ปกติหรือสูง
- TRAb ช่วยวินิจฉัย Graves แต่ไม่ได้บอกว่า nodule ทำงานเองหรือไม่
- Anti-TPO ใช้ใน autoimmune thyroiditis ไม่ช่วยตัดสินใจเรื่อง nodule''',
            pearl="Nodule + TSH ต่ำ → thyroid scan", topic="Thyroid nodule",
            ref=R(108, 109, 110), nl=["B11.2.4-3(1)", "2.3.4(9)"]),
    ])

# ---------------------------------------------------------------- 05-03 DLP
S3 = sec("exam25-05-03", "Dyslipidemia & statin myopathy",
    "LDL สูง → statin · ปวดกล้ามเนื้อ + CPK สูงเล็กน้อย = statin myopathy (rhabdo ต้อง CPK > 5×ULN หรือ > 1,000)", minutes=4,
    source=f"{D} หน้า 111–115", nl=["2.3.9(3)", "2.3.13-3(7)", "B7.4(8)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Primary prevention (ไม่มี DM ไม่มี CKD — แผนภูมิสไลด์)**
- **LDL-C ≥ 190 mg/dL** (อายุ ≥ 21) → **moderate-intensity statin** เป้า **LDL < 100** และลด ≥ 50% · ไม่ถึงเป้า → high-intensity statin
- **Familial hypercholesterolemia** → **high-intensity statin** เป้า **LDL < 70** และลด ≥ 50% → ไม่ถึง + **ezetimibe** → ไม่ถึง + **PCSK9 inhibitor**
- **Statin เป็นยาตัวแรกเสมอ** ในการลด LDL · fibrate ใช้เมื่อ TG สูงมาก (> 500) · ezetimibe เป็นยาเสริม

**Statin-associated muscle symptoms**

| ภาวะ | CPK | อาการ |
|---|---|---|
| Myalgia | ปกติ | ปวดเมื่อย |
| **Myopathy/myositis** | สูง **< 5×ULN** | ปวด/ล้า สองข้าง ต้นขา น่อง |
| **Rhabdomyolysis** | **> 5×ULN หรือ > 1,000 IU/L** (ตามสไลด์; บางแนวทางใช้ > 10×ULN) | ปัสสาวะสีโคล่า AKI |

- ปัจจัยเสี่ยง: **simvastatin ขนาดสูงร่วมกับ amlodipine** (จำกัด simvastatin ≤ 20 mg/วัน), CYP3A4 inhibitor (macrolide, azole), hypothyroid, CKD (เสริม)
''',
    pearls=[
        "LDL สูงทุกกรณี → statin เป็นยาตัวแรก",
        "LDL ≥ 190 → statin, FH → high-intensity statin เป้า < 70",
        "Simvastatin + amlodipine → myopathy (จำกัด simva ≤ 20 mg)",
        "Rhabdo: CPK > 5×ULN หรือ > 1,000 (ตามสไลด์)",
    ],
    items=[
        mcq("EXAM25-05-03-1",
            "A 55-year-old man with hypertension is found to have high LDL cholesterol and elevated total cholesterol on routine laboratory testing. He has no diabetes or cardiovascular disease. Which drug is most appropriate to control his lipid profile?",
            "Statin",
            ["Fibrate", "Ezetimibe", "Niacin", "Bile acid sequestrant"],
            kind="old", src=SRC,
            explain='''การลด LDL เพื่อป้องกันโรคหัวใจและหลอดเลือดใช้ **statin เป็นยาตัวแรก** (มีหลักฐานลดเหตุการณ์และการตาย) — สไลด์แสดงแผนภูมิ primary prevention ที่เริ่มด้วย statin ทุกเส้นทาง
- Fibrate ลด TG เป็นหลัก ใช้เมื่อ TG > 500 กันตับอ่อนอักเสบ
- Ezetimibe ใช้เสริมเมื่อ statin ไม่ถึงเป้าหรือทนไม่ได้
- Niacin ไม่ลด CV events เพิ่มเมื่อให้ร่วมกับ statin และผลข้างเคียงมาก
- Bile acid sequestrant ลด LDL ได้น้อยและเพิ่ม TG ใช้เป็นตัวสำรอง''',
            pearl="LDL สูง → statin", topic="Dyslipidemia",
            ref=R(111, 112, 113), nl=["2.3.9(3)", "B7.4(8)"]),
        mcq("EXAM25-05-03-2",
            "A 58-year-old man with hypertension and dyslipidemia has had progressive bilateral leg pain for 1 month: a deep, aching discomfort in the thighs and calves that is unrelated to exertion. Current medications are amlodipine 10 mg and simvastatin 40 mg daily. BP 130/80 mmHg, pulse 72/min. There is no muscle weakness, rash or joint swelling. CPK 300 U/L (normal 30–200); electrolytes, TSH and renal function are normal. What is the most likely cause of his leg pain?",
            "Drug-induced myopathy",
            ["Rhabdomyolysis", "Polymyositis", "Hypothyroidism", "Peripheral arterial disease"],
            kind="old", src=SRC,
            explain='''ปวดกล้ามเนื้อต้นขาและน่องทั้งสองข้าง + **CPK สูงเล็กน้อย (1.5×ULN)** ขณะใช้ **simvastatin 40 mg ร่วมกับ amlodipine** (amlodipine ยับยั้ง CYP3A4 → ระดับ simvastatin สูง; FDA จำกัด simvastatin ≤ 20 mg เมื่อใช้คู่กัน) = **statin-induced myopathy** → หยุด/ลดขนาด simvastatin
- Rhabdomyolysis ต้อง CPK > 5×ULN หรือ > 1,000 IU/L (สไลด์) มี AKI/ปัสสาวะสีเข้ม
- Polymyositis มี proximal weakness ชัดและ CPK สูงมาก
- Hypothyroidism ถูกตัดด้วย TSH ปกติ
- PAD ปวดน่องเวลาเดินและหายเมื่อพัก (claudication) แต่อาการรายนี้ไม่สัมพันธ์กับการออกแรง
(โจทย์ในสไลด์เขียน amlodipine 20 mg ซึ่งเกินขนาดสูงสุด 10 mg จึงแก้เป็น 10 mg)''',
            pearl="Simvastatin + amlodipine + ปวดกล้ามเนื้อ + CPK สูงเล็กน้อย = statin myopathy", topic="Statin myopathy",
            ref=R(114, 115), nl=["2.3.13-3(7)", "2.3.19(2)"]),
    ])

LECTURE = lecture("05", "Endocrine", "ATD · agranulocytosis · storm · Hashimoto · thyroid nodule · statin",
    objectives=[
        "เลือก MMI หรือ PTU ตามสถานการณ์ และรู้จัก agranulocytosis",
        "จัดลำดับยาใน thyroid storm",
        "เลือกการตรวจ thyroid nodule ตามค่า TSH",
        "ใช้ statin และแยก statin myopathy จาก rhabdomyolysis",
    ],
    sections=[S1, S2, S3])
