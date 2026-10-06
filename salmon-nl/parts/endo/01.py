from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Endocrine"

# ---------------------------------------------------------------- 01-01 Classification & diagnosis
F_DX = fig("endo-01-01-f1", "ช่วงค่าน้ำตาล: ปกติ → prediabetes → DM", '''<svg viewBox="0 0 740 300">
 <text x="20" y="28" class="tb">ค่าที่ใช้วินิจฉัย (mg/dL, %)</text>
 <text x="20" y="74" class="tb">FPG</text>
 <rect x="120" y="54" width="200" height="34" rx="6" class="oksoft"/>
 <rect x="320" y="54" width="200" height="34" rx="6" class="misssoft"/>
 <rect x="520" y="54" width="200" height="34" rx="6" class="badsoft"/>
 <text x="220" y="76" text-anchor="middle" class="t2">&lt; 100</text>
 <text x="420" y="76" text-anchor="middle" class="t2">100–125 = IFG</text>
 <text x="620" y="76" text-anchor="middle" class="tb">≥ 126</text>
 <text x="20" y="134" class="tb">2-hr OGTT</text>
 <rect x="120" y="114" width="200" height="34" rx="6" class="oksoft"/>
 <rect x="320" y="114" width="200" height="34" rx="6" class="misssoft"/>
 <rect x="520" y="114" width="200" height="34" rx="6" class="badsoft"/>
 <text x="220" y="136" text-anchor="middle" class="t2">&lt; 140</text>
 <text x="420" y="136" text-anchor="middle" class="t2">140–199 = IGT</text>
 <text x="620" y="136" text-anchor="middle" class="tb">≥ 200</text>
 <text x="20" y="194" class="tb">HbA1c</text>
 <rect x="120" y="174" width="200" height="34" rx="6" class="oksoft"/>
 <rect x="320" y="174" width="200" height="34" rx="6" class="misssoft"/>
 <rect x="520" y="174" width="200" height="34" rx="6" class="badsoft"/>
 <text x="220" y="196" text-anchor="middle" class="t2">&lt; 5.7%</text>
 <text x="420" y="196" text-anchor="middle" class="t2">5.7–6.4%</text>
 <text x="620" y="196" text-anchor="middle" class="tb">≥ 6.5%</text>
 <text x="20" y="254" class="tb">Random PG</text>
 <rect x="520" y="234" width="200" height="34" rx="6" class="badsoft"/>
 <text x="620" y="256" text-anchor="middle" class="tb">≥ 200 + อาการ</text>
 <text x="220" y="256" text-anchor="middle" class="t3">ใช้วินิจฉัยได้เฉพาะเมื่อมีอาการ</text>
 <text x="220" y="290" text-anchor="middle" class="tb">ปกติ</text>
 <text x="420" y="290" text-anchor="middle" class="tb">Prediabetes</text>
 <text x="620" y="290" text-anchor="middle" class="tb">Diabetes</text>
</svg>''', "อ่านแต่ละแถวจากซ้ายไปขวา — ไม่มีอาการต้องได้ค่าผิดปกติ 2 ครั้ง (ซ้ำค่าเดิมหรือคนละการตรวจ) จึงวินิจฉัย DM")

S1 = sec("endo-01-01", "DM: classification, diagnosis & type 1 vs type 2",
    "FPG ≥126 · 2-hr OGTT ≥200 · HbA1c ≥6.5% · RPG ≥200 + อาการ · ไม่มีอาการต้องยืนยันซ้ำ · สงสัย T1 → C-peptide, anti-GAD", minutes=8,
    source=f"{D} หน้า 5–10, 32–38, 52–53", nl=["2.3.4(1)", "B11.3(2)", "3.3.12"],
    md='''
### Classification (สไลด์หน้า 5 เป็นภาพ — เรียบเรียงตามมาตรฐาน) (เสริม)

| ชนิด | กลไก | ตัวอย่าง |
|---|---|---|
| **Type 1 DM** | autoimmune ทำลาย β-cell → **absolute insulin deficiency** | เด็ก/วัยรุ่น ผอม มาด้วย DKA ได้ |
| **Type 2 DM** | **insulin resistance** + β-cell เสื่อมทีละน้อย (relative deficiency) | ผู้ใหญ่ อ้วน ประวัติครอบครัว |
| Gestational DM | วินิจฉัยครั้งแรกใน 2nd–3rd trimester | — |
| Specific types | MODY, โรคตับอ่อน (chronic pancreatitis, pancreatectomy), ยา (steroid), endocrinopathy (Cushing, acromegaly) | — |

### Diagnosis (สไลด์หน้า 6–8 เป็นภาพ — ใช้เกณฑ์ ADA/สมาคมโรคเบาหวานฯ) (เสริม)

ข้อใดข้อหนึ่ง:
1. **FPG ≥ 126 mg/dL** (อดอาหาร ≥ 8 ชม.)
2. **2-hr plasma glucose ≥ 200 mg/dL** ระหว่าง 75-g OGTT
3. **HbA1c ≥ 6.5%** (วิธีมาตรฐาน NGSP)
4. **Random plasma glucose ≥ 200 mg/dL ร่วมกับอาการ** (polyuria, polydipsia, น้ำหนักลด) หรือ hyperglycemic crisis

> ถ้า **ไม่มีอาการ** ต้องได้ค่าผิดปกติ **2 ครั้ง** — ตรวจซ้ำแบบเดิม หรือ 2 การตรวจต่างชนิดในตัวอย่างเดียวกันก็ได้ · ค่าเดียวที่ผิดปกติในคนไม่มีอาการ = **ยังวินิจฉัยไม่ได้ ต้องตรวจซ้ำ**

[[fig:endo-01-01-f1]]

**Prediabetes**: IFG = FPG 100–125 · **IGT = 2-hr OGTT 140–199** · HbA1c 5.7–6.4% → lifestyle modification, ติดตามทุกปี (เสริม)

> ข้อสอบ OGTT: ดูแค่ **ค่า 0 นาที** (fasting) และ **ค่า 120 นาที** — ค่า 30/60/90 นาทีไม่ได้ใช้วินิจฉัยในผู้ใหญ่ที่ไม่ตั้งครรภ์

### DM type 1 vs type 2 (สไลด์หน้า 9)

| | Type 1 | Type 2 |
|---|---|---|
| Onset | **Sudden** | Gradual |
| อายุเริ่ม | ส่วนใหญ่อายุน้อย | ผู้ใหญ่ |
| รูปร่าง | ผอม/ปกติ | อ้วน |
| Antibody | **มี (เช่น anti-GAD)** | ไม่มี |

- **สงสัย DM type 1** (อายุน้อย BMI ต่ำ น้ำหนักลดเร็ว) → ส่ง **C-peptide** (ต่ำ = สร้าง insulin เองไม่ได้) และ **anti-GAD antibody** (สไลด์หน้า 10, 53)
- T1DM ต้อง **เริ่ม insulin เลย** ไม่ใช้ยากินเป็นหลัก

### Screening (เสริม)
- คัดกรองผู้ใหญ่อายุ **≥ 35 ปี** หรือที่มีปัจจัยเสี่ยง (BMI ≥ 25 หรือรอบเอวเกิน, ประวัติครอบครัว, HT, DLP, เคยเป็น GDM/prediabetes) ด้วย FPG หรือ HbA1c ถ้าปกติตรวจซ้ำทุก 1–3 ปี
''',
    figs=[F_DX],
    pearls=[
        "FPG ≥126 · 2-hr OGTT ≥200 · HbA1c ≥6.5% · RPG ≥200 + อาการ",
        "ไม่มีอาการ + ค่าผิดปกติครั้งเดียว → ตรวจซ้ำก่อน ห้ามรีบเริ่มยา",
        "IFG 100–125 · IGT (2-hr) 140–199 · HbA1c 5.7–6.4% = prediabetes",
        "อายุน้อย ผอม น้ำหนักลด น้ำตาลสูง → คิด T1DM ส่ง C-peptide + anti-GAD และเริ่ม insulin",
    ],
    items=[
        mcq("ENDO-01-01-1",
            "A 45-year-old man undergoes a 75-g oral glucose tolerance test. Plasma glucose: 0 min 96, 30 min 180, 60 min 160, 90 min 155, 120 min 145 mg/dL. What is the most likely diagnosis?",
            "Impaired glucose tolerance",
            ["Normal glucose tolerance", "Impaired fasting glucose", "Diabetes mellitus", "Transient stress hyperglycemia"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''แปลผล OGTT ด้วย **ค่า fasting** และ **ค่าที่ 2 ชั่วโมง** เท่านั้น: fasting 96 (< 100 ปกติ) ส่วน 2-hr = 145 อยู่ในช่วง **140–199 = impaired glucose tolerance (IGT)**
- Normal glucose tolerance ต้องมีค่า 2-hr < 140
- Impaired fasting glucose ต้องมี FPG 100–125 แต่รายนี้ fasting 96 ปกติ
- Diabetes ต้องมีค่า 2-hr ≥ 200 หรือ FPG ≥ 126 — ค่า 30 นาที 180 ไม่ได้ใช้วินิจฉัย
- Stress hyperglycemia เกิดในคนป่วยหนัก/ติดเชื้อ ไม่ได้วินิจฉัยจาก OGTT ในคนปกติ''',
            pearl="OGTT ดูค่า 0 และ 120 นาที · 2-hr 140–199 = IGT", topic="OGTT interpretation",
            ref=[f"{D} หน้า 32–33"], nl=["B11.3(2)", "3.3.12"]),
        mcq("ENDO-01-01-2",
            "A healthy 70-year-old man (height 170 cm, weight 70 kg) without symptoms has a fasting plasma glucose of 130 mg/dL at an annual check-up. In addition to lifestyle advice, what is the most appropriate management?",
            "Repeat fasting plasma glucose to confirm the diagnosis",
            ["Start metformin today", "Follow up in 1 year without further testing", "Perform a 75-g OGTT instead of repeating the FPG", "Start a sulfonylurea because he is elderly"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''FPG 130 ≥ 126 แต่ผู้ป่วย **ไม่มีอาการ** และผิดปกติ **ครั้งเดียว** → ต้อง **ยืนยันด้วยการตรวจซ้ำ** ก่อนวินิจฉัย DM (ตรวจ FPG ซ้ำเป็นวิธีที่ตรงและง่ายที่สุด)
- เริ่ม metformin ทันทีเร็วเกินไป ยังไม่ได้วินิจฉัย
- นัดอีก 1 ปีโดยไม่ตรวจซ้ำ ทำให้พลาดการวินิจฉัย เพราะค่าเกินเกณฑ์ DM แล้ว
- OGTT ทำได้แต่ยุ่งยากกว่าและไม่จำเป็น เมื่อ FPG ครั้งแรกเกินเกณฑ์อยู่แล้วการตรวจ FPG ซ้ำก็ยืนยันได้
- Sulfonylurea เสี่ยง hypoglycemia ในผู้สูงอายุ และยังไม่มีการวินิจฉัย''',
            pearl="ไม่มีอาการ + ค่าผิดปกติครั้งเดียว = ตรวจยืนยันซ้ำ", topic="Confirm diagnosis",
            ref=[f"{D} หน้า 34–35"], nl=["2.3.4(1)", "B11.3(2)"]),
        mcq("ENDO-01-01-3",
            "A 17-year-old boy presents with fatigue and weight loss of 10 kg in 2 months. BMI 16 kg/m2. Physical examination is normal. Random plasma glucose is 400 mg/dL; electrolytes and venous blood gas are normal. What is the most appropriate management?",
            "Start insulin",
            ["Lifestyle modification and recheck in 3 months", "Repeat fasting plasma glucose before treatment", "Start a sulfonylurea", "Start metformin monotherapy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''อายุน้อย **BMI ต่ำ น้ำหนักลดเร็ว** + RPG 400 ร่วมกับอาการ = วินิจฉัย DM ได้เลย และลักษณะเข้าได้กับ **type 1 DM** (absolute insulin deficiency) → **เริ่ม insulin** แล้วส่ง C-peptide, anti-GAD ยืนยันชนิด
- Lifestyle อย่างเดียวไม่พอและเสี่ยงเกิด DKA
- ไม่ต้องตรวจซ้ำ เพราะ RPG ≥ 200 + อาการ ถือว่าวินิจฉัยแล้ว
- Sulfonylurea และ metformin เป็นยาสำหรับ T2DM ที่ยังมี β-cell ไม่เพียงพอใน T1DM''',
            pearl="วัยรุ่นผอม น้ำหนักลด น้ำตาลสูง → insulin + C-peptide/anti-GAD", topic="Suspected T1DM",
            ref=[f"{D} หน้า 9–10, 52–53"], nl=["2.3.4(1)", "B11.4(1)"]),
        mcq("ENDO-01-01-4",
            "A 19-year-old woman, BMI 18 kg/m2, has newly diagnosed diabetes with fasting plasma glucose 260 mg/dL. Her physician wants to confirm whether this is autoimmune type 1 diabetes. Which pair of tests is most appropriate?",
            "Serum C-peptide and anti-GAD antibody",
            ["HbA1c and fructosamine", "Fasting insulin level and HOMA-IR", "75-g OGTT and urine glucose", "Thyroid peroxidase antibody and TSH"],
            explain='''T1DM = autoimmune ทำลาย β-cell → **C-peptide ต่ำ** (สร้าง insulin เองได้น้อย) และ **anti-GAD antibody บวก**
- HbA1c และ fructosamine บอกระดับน้ำตาลเฉลี่ย ไม่ได้แยกชนิด DM
- Fasting insulin/HOMA-IR ใช้ประเมิน insulin resistance (ลักษณะ T2DM) และแปลผลยากเมื่อน้ำตาลสูง
- OGTT ไม่จำเป็นเพราะวินิจฉัย DM แล้ว และไม่ได้บอกชนิด
- Anti-TPO/TSH ใช้คัดกรอง autoimmune thyroid ที่มักพบร่วมกับ T1DM แต่ไม่ได้ยืนยัน T1DM''',
            pearl="C-peptide ต่ำ + anti-GAD บวก = T1DM", topic="T1DM work-up",
            ref=[f"{D} หน้า 10"], nl=["2.3.4(1)"]),
    ])

# ---------------------------------------------------------------- 01-02 Antidiabetic drugs
S2 = sec("endo-01-02", "Antidiabetic drugs: กลไก ผลข้างเคียง และ CKD",
    "SU = hypoglycemia, sulfa allergy · MFM ห้าม GFR <30 · TZD = HF, edema · SGLT2i = HF/CKD/ASCVD แต่ euglycemic DKA · GLP-1 RA = ASCVD/obesity · acarbose = ท้องอืด", minutes=9,
    source=f"{D} หน้า 11–17, 56–65", nl=["B11.4(1)", "2.3.4(1)"],
    md='''
### รายชื่อยา (สไลด์หน้า 16–17)

| กลุ่ม | ตัวอย่าง | กลไก (เสริม) |
|---|---|---|
| Biguanide | **Metformin** | ↓hepatic gluconeogenesis, ↑insulin sensitivity |
| Sulfonylurea (SU) | Glipizide, Glibenclamide, Gliclazide, Glimepiride | ปิด K-ATP channel ที่ β-cell → ↑หลั่ง insulin |
| Glinide | Repaglinide, Mitiglinide | เหมือน SU แต่ออกฤทธิ์สั้น กินก่อนอาหาร |
| Thiazolidinedione (TZD) | **Pioglitazone** | PPAR-γ agonist → ↑insulin sensitivity |
| α-glucosidase inhibitor | **Acarbose** | ชะลอการย่อย carbohydrate ที่ลำไส้ |
| DPP-4 inhibitor | Sitagliptin, Vildagliptin, Saxagliptin, Linagliptin, Alogliptin, Gemigliptin | ↑incretin ที่มีอยู่ |
| SGLT2 inhibitor | Empagliflozin, Dapagliflozin, Canagliflozin | ขับ glucose ทาง proximal tubule |
| GLP-1 RA (ฉีด) | Liraglutide, Dulaglutide, Semaglutide | ↑insulin ตามน้ำตาล, ↓glucagon, อิ่มเร็ว |
| Insulin | basal / bolus / premix | ดูหัวข้อ insulin |

### ผลข้างเคียงและข้อดีที่ออกสอบ (สไลด์หน้า 11–14)

| ยา | ผลข้างเคียงสำคัญ | ข้อดี/ข้อบ่งชี้เด่น |
|---|---|---|
| **Sulfonylurea** | **Hypoglycemia**, **wt gain**, ห้ามใน **sulfa allergy** | ถูก ลดน้ำตาลแรง |
| **Metformin** | **GI** (N/V, diarrhea, flatulence), **lactic acidosis (MALA)** → **ห้ามเมื่อ GFR < 30**, B12 deficiency (เสริม) | first-line, ไม่ทำ hypoglycemia, น้ำหนักไม่ขึ้น |
| **Pioglitazone** | **Heart failure**, edema, wt gain, **osteoporosis** (กระดูกหัก) | ใช้ใน severe CKD ได้ |
| **DPP-4 inhibitor** | **Pancreatitis** | ไม่ทำ hypoglycemia, ใช้ใน CKD ได้ |
| **SGLT2 inhibitor** | **Euglycemic DKA**, genital mycotic infection, volume depletion (เสริม) | ลด **HF, CKD progression, ASCVD**, น้ำหนักลด |
| **GLP-1 RA** | GI, **pancreatitis**, **ห้ามในประวัติ medullary thyroid CA**/MEN2 | ลด **ASCVD**, น้ำหนักลดมาก |
| **Acarbose** | **ท้องอืด flatulence bloating abdominal discomfort** (เด่นสุด) | — |
| **Insulin** | **Hypoglycemia**, wt gain | ลดน้ำตาลได้แรงที่สุด |

> ท้องอืด มีลม แน่นท้อง → **acarbose** (เด่นที่ flatulence) · คลื่นไส้ ถ่ายเหลว → **metformin**

### ยาในผู้ป่วยไตเสื่อม (สไลด์หน้า 15, 63)
- ยาที่ใช้ได้ใน **severe CKD**: **Glipizide** (ยกเว้น dialysis), **DPP-4 inhibitor** (ปรับขนาด ยกเว้น linagliptin), **Glinide**, **Pioglitazone**, **Insulin**
- **Metformin ห้ามเมื่อ eGFR < 30** (เสริม: eGFR 30–45 ลดขนาด ไม่เริ่มใหม่)
- **Glibenclamide** ออกฤทธิ์ยาว ขับทางไต → hypoglycemia นานในผู้สูงอายุ/CKD — เลี่ยง (เสริม)
- ผู้สูงอายุที่ hypoglycemia บ่อยจาก SU และ Cr สูงขึ้น → **หยุด SU เปลี่ยนเป็น insulin** (ต้องดู GFR ก่อนว่าให้ metformin ได้หรือไม่)
''',
    pearls=[
        "SU = hypoglycemia + wt gain + ห้ามใน sulfa allergy",
        "Metformin ห้ามเมื่อ eGFR <30 (lactic acidosis)",
        "Pioglitazone → HF, edema, กระดูกพรุน · ใช้ใน CKD ได้",
        "SGLT2i ดีต่อ HF/CKD/ASCVD แต่ระวัง euglycemic DKA",
        "Acarbose = flatulence/bloating · GLP-1 RA ห้ามใน medullary thyroid CA",
    ],
    items=[
        mcq("ENDO-01-02-1",
            "A 60-year-old woman with type 2 diabetes presents with progressive dyspnea for 1 week. PR 120/min, RR 30/min. She has bilateral fine crepitations, engorged jugular veins, a displaced apex beat, hepatomegaly and pitting edema 2+. Which antidiabetic drug most likely precipitated this problem?",
            "Pioglitazone",
            ["Metformin", "Glipizide", "Insulin glargine", "Acarbose"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ภาพเป็น **congestive heart failure** · **Pioglitazone (TZD)** ทำให้ **ไตดูด Na และน้ำกลับมากขึ้น → fluid retention, edema → precipitate HF** จึงห้ามใช้ใน HF NYHA III–IV
- Metformin ห้ามใน HF ที่ไม่ stable/hypoperfusion เพราะเสี่ยง lactic acidosis แต่ไม่ได้ทำให้เกิดน้ำเกิน
- Glipizide ทำให้ hypoglycemia/น้ำหนักขึ้น ไม่ใช่ HF
- Insulin glargine อาจทำบวมเล็กน้อยได้แต่ไม่ใช่คำตอบคลาสสิก
- Acarbose มีผลข้างเคียงทาง GI ไม่ได้ทำให้เกิด HF''',
            pearl="DM + HF ใหม่ → นึกถึง pioglitazone", topic="TZD & heart failure",
            ref=[f"{D} หน้า 12, 60–61"], nl=["B11.4(1)"]),
        mcq("ENDO-01-02-2",
            "A 47-year-old woman with type 2 diabetes comes for her antidiabetic prescription. Serum creatinine is 2.4 mg/dL and eGFR is 20 mL/min/1.73 m2. Which drug is contraindicated?",
            "Metformin",
            ["Pioglitazone", "Sitagliptin", "Insulin glargine", "Insulin lispro"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**Metformin ห้ามเมื่อ eGFR < 30** เพราะขับทางไต สะสมแล้วเสี่ยง **metformin-associated lactic acidosis (MALA)**
- Pioglitazone เผาผลาญที่ตับ ใช้ใน severe CKD ได้ (ระวังบวม)
- Sitagliptin (DPP-4 inhibitor) ใช้ได้โดยปรับลดขนาด
- Insulin glargine และ lispro ใช้ได้ทุกระดับไต แค่อาจต้องลดขนาดเพราะ insulin ถูกกำจัดช้าลง''',
            pearl="eGFR <30 = หยุด metformin", topic="Metformin & CKD",
            ref=[f"{D} หน้า 15, 62–63"], nl=["B11.4(1)"]),
        mcq("ENDO-01-02-3",
            "A 52-year-old woman with type 2 diabetes on several oral agents complains of abdominal discomfort, bloating and flatulence for 1 month. Which drug is the most likely cause?",
            "Acarbose",
            ["Glipizide", "Metformin", "Pioglitazone", "Sitagliptin"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**Acarbose** ยับยั้ง α-glucosidase → carbohydrate ที่ย่อยไม่หมดไปถึงลำไส้ใหญ่ แบคทีเรียหมักเกิดแก๊ส → **flatulence, bloating, abdominal discomfort** เด่นที่สุด
- Metformin ก็มี GI side effect แต่เด่นที่ **คลื่นไส้ อาเจียน ถ่ายเหลว** มากกว่าท้องอืดมีลม
- Glipizide ผลข้างเคียงหลักคือ hypoglycemia และน้ำหนักขึ้น
- Pioglitazone ทำบวม น้ำหนักขึ้น HF
- Sitagliptin โดยทั่วไปทนได้ดี ผลข้างเคียงสำคัญคือ pancreatitis (ปวดท้องรุนแรง ไม่ใช่ท้องอืดเรื้อรัง)''',
            pearl="ท้องอืดมีลม = acarbose · ถ่ายเหลวคลื่นไส้ = metformin", topic="GI side effects",
            ref=[f"{D} หน้า 64–65"], nl=["B11.4(1)"]),
        mcq("ENDO-01-02-4",
            "A patient with type 2 diabetes has a documented severe allergy to sulfonamide antibiotics. Which antidiabetic agent is the most appropriate choice?",
            "Metformin",
            ["Glipizide", "Glibenclamide", "Gliclazide", "Glimepiride"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ยากลุ่ม **sulfonylurea มีโครงสร้าง sulfonamide** → หลีกเลี่ยงในผู้ที่แพ้ sulfa ทั้งกลุ่ม · **Metformin** ไม่มีโครงสร้างนี้และเป็น first-line อยู่แล้ว
- Glipizide, glibenclamide, gliclazide และ glimepiride ล้วนเป็น sulfonylurea จึงไม่เหมาะเท่ากัน''',
            pearl="แพ้ sulfa → เลี่ยง sulfonylurea", topic="Sulfa allergy",
            ref=[f"{D} หน้า 11, 58–59"], nl=["B11.4(1)"]),
        mcq("ENDO-01-02-5",
            "An elderly man with type 2 diabetes on glipizide has had recurrent hypoglycemic episodes. His serum creatinine has been rising and his eGFR is now 25 mL/min/1.73 m2. What is the most appropriate management?",
            "Stop glipizide and switch to insulin",
            ["Continue glipizide at the same dose", "Switch glipizide to metformin", "Switch to glibenclamide", "Add metformin to glipizide"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Hypoglycemia ซ้ำ ๆ จาก **sulfonylurea** ในผู้สูงอายุที่ไตแย่ลง → **หยุด SU และเปลี่ยนเป็น insulin** ซึ่งปรับขนาดได้ละเอียดและใช้ได้ทุกระดับไต
- ให้ glipizide ต่อ hypoglycemia จะเกิดซ้ำ
- Metformin ห้ามเมื่อ eGFR < 30 (สไลด์เน้นว่าต้องดู GFR ก่อนเสมอ)
- Glibenclamide ออกฤทธิ์ยาวและขับทางไต เสี่ยง hypoglycemia มากกว่า glipizide
- เติม metformin ไม่ได้ทั้งเพราะ GFR และไม่ได้แก้ปัญหา hypoglycemia''',
            pearl="SU + hypoglycemia ซ้ำ + ไตแย่ → insulin", topic="Hypoglycemia on SU",
            ref=[f"{D} หน้า 56–57"], nl=["B11.4(1)", "2.2.17"]),
    ])

# ---------------------------------------------------------------- 01-03 Treatment approach
F_STEP = fig("endo-01-03-f1", "เลือกการรักษา T2DM ที่วินิจฉัยใหม่", '''<svg viewBox="0 0 740 420">
 <defs><marker id="endo-01-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="220" y="10" width="300" height="46" rx="10" class="acsoft"/>
 <text x="370" y="31" text-anchor="middle" class="tb">T2DM วินิจฉัยใหม่</text>
 <text x="370" y="48" text-anchor="middle" class="t3">Lifestyle modification ทุกราย</text>
 <path d="M370 56V78" class="ln" marker-end="url(#endo-01-03-a)"/>
 <rect x="170" y="80" width="400" height="40" rx="10" class="box"/>
 <text x="370" y="105" text-anchor="middle" class="tb">มี ASCVD / HF / CKD / BMI ≥ 30 ?</text>
 <path d="M570 100H620V140" class="ln" marker-end="url(#endo-01-03-a)"/>
 <text x="632" y="96" class="t3">มี</text>
 <rect x="530" y="142" width="200" height="74" rx="10" class="c2soft"/>
 <text x="540" y="164" class="tb">MFM + ยาที่มีหลักฐาน</text>
 <text x="540" y="184" class="t2">HF/CKD → SGLT2i</text>
 <text x="540" y="204" class="t2">ASCVD/อ้วน → GLP-1 RA</text>
 <path d="M300 120V150" class="ln" marker-end="url(#endo-01-03-a)"/>
 <text x="312" y="140" class="t3">ไม่มี → ดูระดับน้ำตาล/อาการ</text>
 <rect x="10" y="154" width="160" height="100" rx="10" class="oksoft"/>
 <text x="90" y="176" text-anchor="middle" class="tb">FPG &lt; 200</text>
 <text x="90" y="194" text-anchor="middle" class="t3">HbA1c &lt; 8–9%</text>
 <text x="90" y="222" text-anchor="middle" class="tb">Metformin</text>
 <text x="90" y="240" text-anchor="middle" class="t3">ยาเดียว</text>
 <rect x="180" y="154" width="170" height="100" rx="10" class="misssoft"/>
 <text x="265" y="176" text-anchor="middle" class="tb">FPG ≥ 200</text>
 <text x="265" y="194" text-anchor="middle" class="t3">ไม่มีอาการ catabolic</text>
 <text x="265" y="222" text-anchor="middle" class="tb">MFM + ยาตัวที่ 2</text>
 <text x="265" y="240" text-anchor="middle" class="t3">เช่น SU / DPP-4i / TZD</text>
 <rect x="360" y="230" width="160" height="100" rx="10" class="badsoft"/>
 <text x="440" y="252" text-anchor="middle" class="tb">น้ำตาลสูงมาก</text>
 <text x="440" y="270" text-anchor="middle" class="t3">FPG &gt; 250–300, A1c ≥ 10%</text>
 <text x="440" y="288" text-anchor="middle" class="t3">+ น้ำหนักลด / อาการ</text>
 <text x="440" y="314" text-anchor="middle" class="tb">Insulin</text>
 <path d="M300 254V280H356" class="ln" marker-end="url(#endo-01-03-a)"/>
 <rect x="10" y="300" width="340" height="110" rx="10" class="sunk"/>
 <text x="22" y="324" class="tb">ติดตามทุก 3 เดือน (HbA1c)</text>
 <text x="22" y="346" class="t2">ไม่ถึงเป้า → ประเมิน adherence/อาหาร ก่อน</text>
 <text x="22" y="368" class="t2">แล้วจึงเพิ่มขนาด/เพิ่มยาทีละขั้น</text>
 <text x="22" y="392" class="t3">→ 2 ยา → 3 ยา → basal insulin</text>
 <rect x="530" y="240" width="200" height="90" rx="10" class="c1soft"/>
 <text x="630" y="264" text-anchor="middle" class="tb">T1DM</text>
 <text x="630" y="286" text-anchor="middle" class="t2">Insulin ตั้งแต่แรก</text>
 <text x="630" y="306" text-anchor="middle" class="t3">basal-bolus</text>
</svg>''', "ตัวเลขเกณฑ์ FPG ≥200 → MFM + ยาตัวที่ 2 มาจากสไลด์หน้า 48 · กล่อง comorbidity เรียบเรียงจากสไลด์หน้า 13, 20 (ภาพ)")

S3 = sec("endo-01-03", "DM: การรักษาตามระดับน้ำตาล เป้าหมาย และการคัดกรองภาวะแทรกซ้อน",
    "เป้า FBS 80–130, HbA1c <7% · FPG ≥200 → MFM + ยาตัวที่ 2 · น้ำตาลสูงมาก/มีอาการ → insulin · คุมไม่ได้ → ถาม adherence ก่อน · ตา ไต เท้า: T2 ทันที, T1 หลัง 5 ปี", minutes=9,
    source=f"{D} หน้า 20–25, 30–31, 36–55", nl=["2.3.4(1)", "B11.4(1)"],
    md='''
### หลักเลือกการรักษา T2DM (สไลด์หน้า 20–21 เป็นภาพ — เรียบเรียงจากข้อเฉลยในสไลด์)

- **ทุกรายเริ่ม lifestyle modification** (ลดน้ำหนัก 5–10%, ออกกำลังกาย 150 นาที/สัปดาห์, อาหาร) แต่ **ไม่ใช่การรักษาเดียว** เมื่อวินิจฉัย DM แล้ว
- **Metformin = first-line** ถ้าไม่มีข้อห้าม
- สไลด์หน้า 48: **FBS ≥ 200 mg/dL → Metformin + ยากินตัวที่ 2**
- **น้ำตาลสูงมาก** (เช่น FBS ~300–400, HbA1c ≥ 10%) หรือมี **อาการ catabolic** (น้ำหนักลดเร็ว, polyuria/polydipsia ชัด) → **Insulin**
- มี **ASCVD / heart failure / CKD / BMI ≥ 30** → เลือกยาที่มีหลักฐานลด outcome: **SGLT2 inhibitor** (HF, CKD) หรือ **GLP-1 RA** (ASCVD, อ้วน) ร่วมกับ metformin
- **T1DM → เริ่ม insulin เลย** (สไลด์หน้า 22)

[[fig:endo-01-03-f1]]

> ผู้ป่วยที่เคยคุมได้ดีแล้วน้ำตาลสูงขึ้น → **ซักการกินยา (adherence) อาหาร ยาอื่น ๆ ก่อน** แล้วจึงปรับยา

### เป้าหมายการรักษา (สไลด์หน้า 23–25)

| กลุ่ม | FBS | HbA1c |
|---|---|---|
| ทั่วไป (เป็นไม่นาน ไม่มีโรคร่วม) | **80–130 mg/dL** | **< 7%** |
| เข้มงวดมาก (อายุน้อย ไม่เสี่ยง hypoglycemia) (เสริม) | — | < 6.5% |
| **ผู้สูงอายุ/โรคร่วมมาก** | ผ่อนลง | **7.0–8.0%** (ยิ่งเปราะบางยิ่งผ่อน) (เสริม) |

> อายุมาก โรคร่วมมาก เสี่ยง hypoglycemia → **เข้มงวดน้อยลง** (สไลด์หน้า 24)

### เป้าหมายอื่นที่ใช้ร่วม (เสริม)
- BP < 130/80 mmHg · LDL ตามความเสี่ยง (ดูหมวด Dyslipidemia) · เลิกบุหรี่

### คัดกรองภาวะแทรกซ้อน (สไลด์หน้า 30–31)

- **ตา ไต เท้า** ปีละครั้ง: ตรวจจอประสาทตา (fundus), urine albumin–creatinine ratio + eGFR, ตรวจเท้า (monofilament, ชีพจร, แผล)
- **T2DM คัดกรองทันทีที่วินิจฉัย** (เพราะมักเป็นมานานก่อนรู้ตัว)
- **T1DM เริ่มคัดกรองหลังวินิจฉัย 5 ปี**
''',
    figs=[F_STEP],
    pearls=[
        "เป้าทั่วไป FBS 80–130, HbA1c <7% · ผู้สูงอายุผ่อนได้",
        "FBS ≥200 → metformin + ยากินตัวที่ 2 (ตามสไลด์)",
        "น้ำตาลสูงมาก + น้ำหนักลด/อาการ → insulin",
        "เคยคุมดีแล้วน้ำตาลขึ้น → ถาม adherence/อาหารก่อนเพิ่มยา",
        "Screen ตา ไต เท้า: T2 ทันที · T1 หลัง 5 ปี",
    ],
    items=[
        mcq("ENDO-01-03-1",
            "A 48-year-old obese man with a family history of diabetes has fasting plasma glucose 142 mg/dL, and a repeat measurement is 148 mg/dL. HbA1c is 6.0%. He has no symptoms. What is the most appropriate management?",
            "Lifestyle modification plus metformin",
            ["Repeat FPG and HbA1c in 6 months", "Lifestyle modification alone and reassess in 1 year", "Sitagliptin monotherapy", "Pioglitazone monotherapy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''FPG ≥ 126 **สองครั้ง** = **วินิจฉัย DM แล้ว** แม้ HbA1c 6.0% (เมื่อผลสองการตรวจไม่ตรงกัน ให้ยึดค่าที่ผิดปกติซึ่งยืนยันซ้ำแล้ว) → เริ่ม **lifestyle modification ร่วมกับ metformin** ซึ่งเป็น first-line
- ตรวจซ้ำอีก 6 เดือนไม่จำเป็น เพราะยืนยันแล้ว
- Lifestyle อย่างเดียวเป็นแนวทางของ prediabetes — แนวทางปัจจุบันแนะนำ metformin ตั้งแต่วินิจฉัยในคนอ้วนที่ไม่มีข้อห้าม
- Sitagliptin และ pioglitazone ใช้เป็นยาตัวที่ 2 หรือเมื่อใช้ metformin ไม่ได้

(ตัวเลือกในสไลด์คือ "Metformin" และ "Exercise and lifestyle modification" แยกกัน — คำตอบตามแนวทางปัจจุบันคือ metformin ควบคู่ lifestyle)''',
            pearl="FPG ≥126 สองครั้ง = DM แม้ HbA1c ไม่ถึง · เริ่ม metformin", topic="Initial therapy",
            ref=[f"{D} หน้า 36–38"], nl=["2.3.4(1)", "B11.4(1)"]),
        mcq("ENDO-01-03-2",
            "A 50-year-old man, BMI 26 kg/m2, has been unable to lose weight. FPG is 170 mg/dL and HbA1c 8.5%; BUN 8, Cr 0.5 mg/dL. He has no osmotic symptoms or weight loss. What is the most appropriate initial drug therapy?",
            "Metformin",
            ["Basal insulin", "Sulfonylurea monotherapy", "Pioglitazone monotherapy", "Metformin plus sulfonylurea"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''T2DM ไตปกติ **FPG < 200** ไม่มีอาการ → **metformin** เป็น first-line ตามสไลด์ (เกณฑ์เพิ่มยาตัวที่ 2 คือ FBS ≥ 200)
- Insulin สงวนไว้เมื่อน้ำตาลสูงมากหรือมีอาการ catabolic
- Sulfonylurea และ pioglitazone เดี่ยว ๆ ไม่ใช่ first-line และมีผลข้างเคียงน้ำหนักขึ้น
- Metformin + SU เป็นขั้นต่อไปเมื่อ FBS ≥ 200 หรือคุมด้วยยาเดียวไม่ได้

(บางแนวทาง เช่น ADA ใช้ HbA1c ≥ 1.5% เหนือเป้าเป็นเกณฑ์ให้ยาสองตัว — ข้อสอบชุดนี้ยึด FBS ตามสไลด์)''',
            pearl="FPG <200 ไม่มีอาการ → metformin เดี่ยว", topic="Monotherapy",
            ref=[f"{D} หน้า 39–41"], nl=["B11.4(1)"]),
        mcq("ENDO-01-03-3",
            "A 45-year-old woman, BMI 26 kg/m2, has lost 5 kg in 2 months with polyuria. FPG is 250 mg/dL and HbA1c 10%; BUN 8, Cr 0.5 mg/dL. Urine ketone is negative. What is the most appropriate management?",
            "Insulin",
            ["Metformin monotherapy", "Sulfonylurea monotherapy", "Pioglitazone", "Lifestyle modification alone"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''น้ำตาลสูงมาก (FPG 250, **HbA1c 10%**) ร่วมกับ **น้ำหนักลดเร็ว + polyuria (อาการ catabolic/glucotoxicity)** → **insulin** ลดน้ำตาลได้เร็วและแก้ glucotoxicity เมื่อคุมได้แล้วค่อยลดลงเป็นยากิน
- Metformin เดี่ยวลด HbA1c ได้ราว 1–1.5% ไม่พอเมื่อ HbA1c 10% และมีอาการ
- Sulfonylurea และ pioglitazone เดี่ยวไม่พอและไม่ใช่ทางเลือกเมื่อมี catabolic state
- Lifestyle อย่างเดียวไม่เหมาะเมื่อน้ำตาลสูงขนาดนี้

(เฉลยในสไลด์เป็นภาพ — ตอบตามหลัก "น้ำหนักลด/มีอาการ + HbA1c ≥ 10% → insulin" ต่างจากข้อคล้ายกันที่ "น้ำหนักไม่ลด" ซึ่งตอบ metformin; ถ้าไม่มีอาการ การให้ metformin + ยาตัวที่ 2 ก็เป็นทางเลือกได้)''',
            pearl="HbA1c ≥10% + น้ำหนักลด/อาการ → insulin", topic="When to start insulin",
            ref=[f"{D} หน้า 42–44"], nl=["B11.4(1)"]),
        mcq("ENDO-01-03-4",
            "A 50-year-old man has lost 3 kg in 4 months. BMI 28 kg/m2, waist 100 cm. FBS 220 mg/dL. Lipids: total cholesterol 190, TG 300, HDL 40, LDL 95 mg/dL. Besides diet control, which is the most appropriate treatment to start now?",
            "Metformin plus a second oral antidiabetic drug",
            ["Fibrate", "Fish oil", "Acarbose monotherapy", "Lifestyle modification alone, recheck in 3 months"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**FBS ≥ 200** → สไลด์สรุปว่าให้ **metformin + ยากินตัวที่ 2** · ไขมัน: อายุ ≥ 40 มี DM LDL < 190 → ควรได้ **statin** (เป้า LDL < 100 และลด ≥ 30%) แต่ตัวเลือกที่ตรงปัญหาหลักที่สุดคือการคุมน้ำตาล
- Fibrate ใช้เมื่อ TG > 500 เพื่อป้องกัน pancreatitis — TG 300 ยังไม่ถึง และคุมน้ำตาลได้ TG จะลดเอง
- Fish oil ไม่ใช่การรักษาหลัก
- Acarbose เดี่ยวลดน้ำตาลได้น้อย ไม่พอเมื่อ FBS 220
- Lifestyle อย่างเดียวไม่พอเมื่อวินิจฉัย DM ที่น้ำตาลสูงขนาดนี้

(ตัวเลือกในสไลด์มี "Statin" และ "Metformin" แยกกัน — ผู้ป่วยรายนี้ควรได้ทั้งสองอย่าง)''',
            pearl="DM + TG 300: คุมน้ำตาล + statin ก่อน fibrate", topic="DM with dyslipidemia",
            ref=[f"{D} หน้า 45–48"], nl=["B11.4(1)", "2.3.9(3)"]),
        mcq("ENDO-01-03-5",
            "A 55-year-old woman with type 2 diabetes for 5 years had good glycemic control until the last 6 months, when her FBS rose to 200–280 mg/dL. What is the most appropriate next step?",
            "Assess changes in diet and medication adherence",
            ["Increase the dose of her antidiabetic drug", "Refer to an endocrinologist", "Advise more exercise only", "Switch all oral drugs to basal-bolus insulin"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ผู้ที่ **เคยคุมได้ดีแล้วน้ำตาลสูงขึ้น** ต้อง **หาสาเหตุก่อน**: กินยาไม่สม่ำเสมอ อาหารเปลี่ยน ยาใหม่ (steroid) โรคแทรก (ติดเชื้อ) แล้วจึงตัดสินใจปรับยา
- เพิ่มขนาดยาเลยโดยไม่ถาม อาจเกิด hypoglycemia เมื่อผู้ป่วยกลับมากินยาครบ
- ส่งต่อแพทย์ต่อมไร้ท่อเกินความจำเป็นในขั้นนี้
- แนะนำออกกำลังกายอย่างเดียวไม่ได้แก้สาเหตุ
- เปลี่ยนเป็น basal-bolus ทันทีเกินจำเป็นและยังไม่รู้สาเหตุ''',
            pearl="คุมเคยดีแล้วแย่ลง → adherence/อาหาร/ยาอื่นก่อน", topic="Loss of control",
            ref=[f"{D} หน้า 54–55"], nl=["2.3.4(1)"]),
        mcq("ENDO-01-03-6",
            "A previously healthy man has a fasting blood sugar of 400 mg/dL at an annual check-up. On questioning he has had polyuria, polydipsia and some weight loss. Urine ketone is trace and venous bicarbonate is normal. What is the most appropriate management?",
            "Start insulin",
            ["Exercise and diet, recheck in 3 months", "Start metformin monotherapy", "Start a sulfonylurea monotherapy", "Repeat FBS before any treatment"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''FBS **400** ร่วมกับ **อาการ (polyuria, polydipsia, น้ำหนักลด)** = วินิจฉัย DM ได้เลยและเป็น **glucotoxicity/catabolic state** → **insulin** (ไม่ถึง DKA เพราะ HCO3 ปกติ)
- Lifestyle อย่างเดียวไม่พอและเสี่ยงเกิด hyperglycemic crisis
- Metformin หรือ SU เดี่ยวลดน้ำตาลได้ไม่พอเมื่อ FBS 400 และมีอาการ
- ไม่ต้องตรวจซ้ำเพราะมีอาการแล้ว

(สไลด์ให้ตัวเลือกเพียง exercise / oral drug / insulin — สอดคล้องกับหลัก "น้ำตาลสูงมาก → insulin"; screening ตา ไต เท้าใน T2DM ให้เริ่มทันทีที่วินิจฉัย)''',
            pearl="FBS ~400 + อาการ → insulin", topic="Very high glucose",
            ref=[f"{D} หน้า 49–51"], nl=["B11.4(1)", "2.3.4(1)"]),
    ])

# ---------------------------------------------------------------- 01-04 Insulin
F_INS = fig("endo-01-04-f1", "Time–action ของ insulin แต่ละชนิด", '''<svg viewBox="0 0 740 330">
 <path d="M70 270H720" class="ln"/>
 <path d="M70 270V30" class="ln"/>
 <text x="395" y="318" text-anchor="middle" class="t2">ชั่วโมงหลังฉีด</text>
 <text x="70" y="290" text-anchor="middle" class="t3">0</text>
 <text x="178" y="290" text-anchor="middle" class="t3">4</text>
 <text x="287" y="290" text-anchor="middle" class="t3">8</text>
 <text x="395" y="290" text-anchor="middle" class="t3">12</text>
 <text x="503" y="290" text-anchor="middle" class="t3">16</text>
 <text x="612" y="290" text-anchor="middle" class="t3">20</text>
 <text x="720" y="290" text-anchor="middle" class="t3">24</text>
 <text x="40" y="150" text-anchor="middle" class="t2" transform="rotate(-90 40 150)">ฤทธิ์ insulin</text>
 <path d="M70 270C85 120 100 60 115 70C135 85 150 200 180 262L190 270" class="lnbad"/>
 <text x="122" y="52" class="t3">Rapid (aspart, lispro)</text>
 <path d="M70 270C100 170 120 100 140 100C170 105 200 210 240 268" class="lnc2"/>
 <text x="170" y="118" class="t3">Regular insulin (RI)</text>
 <path d="M70 270C130 230 170 140 220 140C270 140 330 220 420 262L450 270" class="lnc1"/>
 <text x="262" y="132" class="t3">NPH (peak 4–10 hr)</text>
 <path d="M70 270C90 215 110 205 140 205H690L715 240" class="lnok"/>
 <text x="460" y="196" class="t3">Glargine / Detemir / Degludec — ไม่มี peak</text>
 <rect x="470" y="40" width="240" height="96" rx="8" class="sunk"/>
 <text x="482" y="62" class="tb">Bolus: rapid / RI</text>
 <text x="482" y="82" class="t3">คุมน้ำตาลหลังมื้อ ฉีดก่อนอาหาร</text>
 <text x="482" y="104" class="tb">Basal: NPH / analog</text>
 <text x="482" y="124" class="t3">คุม FBS และระหว่างมื้อ</text>
</svg>''', "เส้นยิ่งสูงยิ่งออกฤทธิ์มาก — NPH ที่ฉีดเช้าจะ peak ช่วงบ่าย จึงเป็นสาเหตุ hypoglycemia ช่วงบ่ายในผู้ใช้ premix")

S4 = sec("endo-01-04", "Insulin: ชนิด regimen และการปรับขนาด",
    "Basal (NPH, glargine) คุม FBS · bolus (RI, rapid) คุมหลังมื้อ · regimen basal / basal-plus / basal-bolus / premix · hypoglycemia ช่วงบ่ายบน premix → ลดมื้อเช้า", minutes=8,
    source=f"{D} หน้า 17–19, 26–29, 83–85", nl=["B11.4(1)", "2.3.4(1)"],
    md='''
### ชนิดของ insulin (สไลด์หน้า 17)

| กลุ่ม | ตัวอย่าง | onset / peak / duration (เสริม) |
|---|---|---|
| **Rapid acting** (bolus) | Aspart, Lispro, Glulisine | 15 นาที / 1–2 ชม. / 3–5 ชม. |
| **Short acting** (bolus) | **Regular insulin (RI)** | 30–60 นาที / 2–4 ชม. / 6–8 ชม. |
| **Intermediate** (basal) | **NPH** | 1–2 ชม. / **4–10 ชม.** / 12–16 ชม. |
| **Long acting** (basal) | Glargine U100, Detemir | ไม่มี peak / ~24 ชม. |
| **Ultra-long** (basal) | Glargine U300, Degludec | ไม่มี peak / > 24 ชม. |
| **Premixed** | **30% RI + 70% NPH** (เช่น Mixtard 70/30) | มีทั้งสอง peak |

[[fig:endo-01-04-f1]]

### Regimen (สไลด์หน้า 26)

| Regimen | ตัวอย่างตามสไลด์ | เขียนย่อ |
|---|---|---|
| **Basal** | NPH 6 U sc hs | 0-0-0-NPH 6 |
| **Basal plus** | NPH 30 U hs + RI 4 U ac เช้า | RI 4-0-0-NPH 30 |
| **Basal bolus** | NPH 30 U hs + RI 6 U ac เช้า กลางวัน เย็น | RI 6-6-6-NPH 30 |
| **Premix** | Mixtard 20 U ac เช้า + 10 U ac เย็น | Mixtard 20-0-10-0 |

- เริ่ม basal ใน T2DM: **10 U/วัน หรือ 0.1–0.2 U/kg/วัน** ก่อนนอน แล้วปรับเพิ่ม 2 U ทุก 3 วันจน FBS ถึงเป้า (เสริม)
- T1DM ต้องใช้ **basal-bolus** (หรือ insulin pump) ราว 0.4–1 U/kg/วัน ครึ่งหนึ่งเป็น basal (เสริม)

### การปรับ insulin ตามเวลาที่น้ำตาลผิดปกติ (สไลด์หน้า 27–29 เป็นภาพ) (เสริม)

หลัก: **ดูว่าช่วงเวลานั้นเป็นผลของ insulin ตัวไหน แล้วปรับตัวนั้น**

| น้ำตาลผิดปกติช่วง | insulin ที่รับผิดชอบ (regimen 2 เข็ม RI+NPH) |
|---|---|
| ก่อนอาหารเช้า (FBS) | **NPH มื้อเย็น/ก่อนนอน** |
| ก่อนอาหารกลางวัน | **RI มื้อเช้า** |
| **บ่าย/ก่อนอาหารเย็น** | **NPH มื้อเช้า** |
| ก่อนนอน | **RI มื้อเย็น** |

> ใช้ premix 2 เข็มแล้ว **ใจสั่น เหงื่อออกช่วง 14:00–15:00** = peak ของ NPH มื้อเช้า → **ลด insulin มื้อเช้า**
> FBS สูงตอนเช้า: แยก **Somogyi** (hypoglycemia ตี 2–3 แล้ว rebound → ลด NPH เย็น) กับ **dawn phenomenon** (น้ำตาลตี 3 ไม่ต่ำ → เพิ่ม/เลื่อน NPH ไปก่อนนอน) ด้วยการเจาะ CBG ตี 3 (เสริม)
''',
    figs=[F_INS],
    pearls=[
        "Basal = NPH/glargine คุม FBS · bolus = RI/rapid คุมหลังมื้อ",
        "Premix = 30% RI + 70% NPH ฉีดก่อนเช้าและเย็น",
        "Hypo ช่วงบ่ายบน premix → ลดมื้อเช้า (NPH เช้า peak บ่าย)",
        "FBS สูง → ปรับ NPH มื้อเย็น/ก่อนนอน · เจาะตี 3 แยก Somogyi กับ dawn",
    ],
    items=[
        mcq("ENDO-01-04-1",
            "A 20-year-old woman with diabetes (HbA1c 8%) uses premixed NPH/regular insulin 70/30, 30 units before breakfast and 10 units before dinner. For 2 days she has had palpitations and sweating at about 14:00–15:00. What is the most appropriate adjustment?",
            "Reduce the pre-breakfast insulin dose",
            ["Reduce the pre-dinner insulin dose", "Reduce both doses equally", "Change to three injections of regular insulin before meals only", "Add a once-daily NPH dose at bedtime"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ช่วงบ่าย 14–15 น. เป็น **peak ของ NPH ที่ฉีดตอนเช้า** (NPH peak 4–10 ชม.) → hypoglycemia ช่วงนี้แก้โดย **ลดขนาดเข็มเช้า**
- ลดเข็มเย็นจะกระทบน้ำตาลกลางคืนและเช้า ไม่ใช่ช่วงบ่าย
- ลดทั้งสองเข็มทำให้น้ำตาลช่วงอื่นสูงโดยไม่จำเป็น
- เปลี่ยนเป็น RI สามมื้ออย่างเดียวจะขาด basal insulin
- เพิ่ม NPH ก่อนนอนยิ่งเพิ่ม insulin และไม่ได้แก้ปัญหาช่วงบ่าย''',
            pearl="Hypo บ่าย + premix = ลดเข็มเช้า", topic="Insulin adjustment",
            ref=[f"{D} หน้า 83–84"], nl=["B11.4(1)", "2.2.17"]),
        mcq("ENDO-01-04-2",
            "A man with type 2 diabetes uses NPH insulin at bedtime and regular insulin before each meal. His fasting (pre-breakfast) glucose is consistently 190–210 mg/dL, while pre-lunch, pre-dinner and bedtime values are at target. A 3 a.m. glucose is 150 mg/dL. What is the most appropriate change?",
            "Increase the bedtime NPH dose",
            ["Increase the pre-breakfast regular insulin", "Increase the pre-dinner regular insulin", "Decrease the bedtime NPH dose", "Add a sulfonylurea in the morning"],
            explain='''FBS ถูกคุมโดย **basal ช่วงกลางคืน (NPH ก่อนนอน)** · CBG ตี 3 = 150 **ไม่ต่ำ** → ไม่ใช่ Somogyi effect แต่เป็น basal ไม่พอ/dawn phenomenon → **เพิ่ม NPH ก่อนนอน**
- RI ก่อนอาหารเช้าคุมน้ำตาลก่อนมื้อกลางวัน ไม่ใช่ FBS
- RI ก่อนอาหารเย็นคุมน้ำตาลก่อนนอน
- ลด NPH จะใช้เมื่อ CBG ตี 3 ต่ำ (Somogyi) ซึ่งรายนี้ไม่ใช่
- เพิ่ม SU ไม่ใช่วิธีปรับในผู้ที่ใช้ basal-bolus อยู่และเสี่ยง hypoglycemia''',
            pearl="FBS สูง + ตี 3 ไม่ต่ำ → เพิ่ม NPH ก่อนนอน", topic="Fasting hyperglycemia",
            ref=[f"{D} หน้า 26–29"], nl=["B11.4(1)"]),
        mcq("ENDO-01-04-3",
            "A 62-year-old man with type 2 diabetes on maximum-dose metformin and glipizide has HbA1c 9.2% and FBS 210 mg/dL. He is reluctant to inject more than once a day. What is the most appropriate regimen to start?",
            "Bedtime basal insulin about 10 units (0.1–0.2 U/kg) and titrate to fasting glucose",
            ["Regular insulin 6 units before each meal", "Premixed insulin 70/30 three times daily", "Basal-bolus insulin with stopping all oral drugs", "Rapid-acting insulin at bedtime"],
            explain='''T2DM ที่คุมด้วยยากินไม่ได้ → ขั้นแรกคือ **basal insulin วันละครั้ง** (NPH ก่อนนอนหรือ glargine) เริ่ม ~10 U หรือ 0.1–0.2 U/kg แล้ว **ปรับตาม FBS** (เพิ่ม 2 U ทุก 3 วัน) ใช้ร่วมกับ metformin ต่อ
- RI ก่อนอาหาร 3 มื้อเป็น bolus อย่างเดียว ไม่มี basal และต้องฉีดหลายครั้ง
- Premix 3 ครั้ง/วันไม่ใช่ regimen เริ่มต้นและเสี่ยง hypoglycemia
- Basal-bolus ต้องฉีด 4 ครั้ง ใช้เมื่อ basal plus แล้วยังไม่ถึงเป้า
- Rapid-acting ก่อนนอนไม่ได้คุม FBS และเสี่ยง hypoglycemia กลางคืน''',
            pearl="เริ่ม insulin ใน T2DM = basal 10 U ก่อนนอน ปรับตาม FBS", topic="Starting basal insulin",
            ref=[f"{D} หน้า 26"], nl=["B11.4(1)"]),
    ])

LECTURE = lecture("01", "Diabetes mellitus", "วินิจฉัย · ยาเบาหวาน · เลือกการรักษา · insulin",
    objectives=[
        "วินิจฉัย DM และ prediabetes จาก FPG, OGTT, HbA1c และรู้ว่าเมื่อไรต้องตรวจซ้ำ",
        "แยก DM type 1 กับ type 2 และส่งตรวจ C-peptide/anti-GAD ได้",
        "เลือกยาเบาหวานตามระดับน้ำตาล โรคร่วม และไต และบอกผลข้างเคียงเด่นของแต่ละกลุ่มได้",
        "เริ่มและปรับ insulin ตามช่วงเวลาที่น้ำตาลผิดปกติได้",
    ],
    sections=[S1, S2, S3, S4])
