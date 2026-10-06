from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Endocrine"

# ---------------------------------------------------------------- 06-01 HPA axis
F_AXIS = fig("endo-06-01-f1", "HPA axis กับการทดสอบ dynamic", '''<svg viewBox="0 0 740 420">
 <defs><marker id="endo-06-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="20" y="10" width="200" height="40" rx="10" class="box"/>
 <text x="120" y="35" text-anchor="middle" class="tb">Hypothalamus · CRH</text>
 <path d="M120 50V78" class="ln" marker-end="url(#endo-06-01-a)"/>
 <rect x="20" y="80" width="200" height="40" rx="10" class="c1soft"/>
 <text x="120" y="105" text-anchor="middle" class="tb">Pituitary · ACTH</text>
 <path d="M120 120V148" class="ln" marker-end="url(#endo-06-01-a)"/>
 <rect x="20" y="150" width="200" height="40" rx="10" class="c2soft"/>
 <text x="120" y="175" text-anchor="middle" class="tb">Adrenal cortex</text>
 <path d="M120 190V218" class="ln" marker-end="url(#endo-06-01-a)"/>
 <rect x="20" y="220" width="200" height="40" rx="10" class="acsoft"/>
 <text x="120" y="245" text-anchor="middle" class="tb">Cortisol</text>
 <path d="M220 240H252V30H222" class="lnbad" marker-end="url(#endo-06-01-a)"/>
 <path d="M252 100H222" class="lnbad" marker-end="url(#endo-06-01-a)"/>
 <text x="262" y="140" class="t3">negative</text>
 <text x="262" y="156" class="t3">feedback</text>
 <rect x="320" y="10" width="410" height="120" rx="10" class="sunk"/>
 <text x="332" y="34" class="tb">Dexamethasone suppression test (สงสัยเกิน)</text>
 <text x="332" y="58" class="t2">ปกติ: dexa กด ACTH → cortisol ↓↓ (suppress ได้)</text>
 <text x="332" y="80" class="t2">Endogenous Cushing: cortisol ไม่ลด (suppress ไม่ได้)</text>
 <text x="332" y="102" class="t3">1 mg dexa 23:00 → cortisol 08:00 &gt; 1.8 mcg/dL = ผิดปกติ</text>
 <text x="332" y="120" class="t3">dexa ไม่ถูกวัดใน cortisol assay จึงใช้ทดสอบได้</text>
 <rect x="320" y="140" width="410" height="120" rx="10" class="sunk"/>
 <text x="332" y="164" class="tb">ACTH stimulation test (สงสัยขาด)</text>
 <text x="332" y="188" class="t2">ปกติ: ฉีด ACTH → cortisol ขึ้น ≥ 18 mcg/dL</text>
 <text x="332" y="210" class="t2">1° AI: กระตุ้นไม่ขึ้น (ต่อมพัง)</text>
 <text x="332" y="232" class="t2">2° AI: ขึ้นได้ — แต่ถ้าเรื้อรังจนต่อมฝ่อ ก็ไม่ขึ้น</text>
 <text x="332" y="250" class="t3">cosyntropin 250 mcg IV/IM วัดที่ 30–60 นาที</text>
 <rect x="20" y="280" width="345" height="130" rx="10" class="badsoft"/>
 <text x="32" y="304" class="tb">ACTH ↑</text>
 <text x="32" y="328" class="t2">Cushing: ACTH-dependent (pituitary, ectopic)</text>
 <text x="32" y="350" class="t2">AI: 1° (Addison, ต่อมหมวกไตพัง) → คล้ำ</text>
 <text x="32" y="372" class="t3">Cushing ACTH ↑ → MRI pituitary / หา ectopic</text>
 <text x="32" y="392" class="t3">AI ACTH ↑ → CT adrenal, adrenal antibody</text>
 <rect x="385" y="280" width="345" height="130" rx="10" class="c1soft"/>
 <text x="397" y="304" class="tb">ACTH ↓</text>
 <text x="397" y="328" class="t2">Cushing: adrenal adenoma/CA (1°)</text>
 <text x="397" y="350" class="t2">AI: 2° (steroid เรื้อรัง, pituitary)</text>
 <text x="397" y="372" class="t3">Cushing ACTH ↓ → CT/MRI adrenal</text>
 <text x="397" y="392" class="t3">AI ACTH ↓ → MRI pituitary</text>
</svg>''', "Cortisol สูงจะกด ACTH เสมอ ยกเว้นต้นเหตุสร้าง ACTH เอง — DST ใช้พิสูจน์ว่ากดไม่ลง ACTH stim ใช้พิสูจน์ว่ากระตุ้นไม่ขึ้น")

S1 = sec("endo-06-01", "Cushing syndrome",
    "Exogenous steroid บ่อยสุด · moon face, buffalo hump, purple striae >1 cm, proximal weakness, HT, DM, hypoK · 1) 8AM cortisol ต่ำ = exogenous 2) screen: 24-hr UFC / midnight salivary / 1 mg DST 3) confirm อีก test 4) ACTH ↑ MRI pituitary · ↓ CT adrenal", minutes=10,
    source=f"{D} หน้า 260–271, 282–285", nl=["2.3.4-3(1)", "B11.2.5-3(7)", "B11.3(4)"],
    md='''
### สาเหตุ (สไลด์หน้า 261)
- **Exogenous Cushing syndrome — พบบ่อยที่สุด** (glucocorticoid ทั้งยาแผนปัจจุบัน และ **ยาลูกกลอน/สมุนไพรที่ผสม steroid**)
- **Endogenous**:
  - **Primary hypercortisolism (ACTH-independent)**: adrenal adenoma/carcinoma
  - **Secondary hypercortisolism (ACTH-dependent)**: **pituitary ACTH (Cushing disease)** — บ่อยที่สุดของ endogenous · **ectopic ACTH** เช่น **small cell lung cancer**

### อาการ (สไลด์หน้า 262–263)
- **Moon face, facial plethora** · **central obesity, buffalo hump** (supraclavicular fat pad)
- **Purplish striae** (กว้าง > 1 cm — เสริม) · **ผิวบาง ช้ำง่าย**
- **HT**, **proximal muscle weakness**, **osteoporosis**
- ซึมเศร้า วิตกกังวล · ประจำเดือนผิดปกติ ความต้องการทางเพศลด
- **Glucose ↑, lipid ↑** · **Na ↑, K ↓, metabolic alkalosis** (cortisol จับ mineralocorticoid receptor)
- เฉพาะ **ACTH-dependent**: **hyperpigmentation** (ACTH กระตุ้น melanocyte) · **hirsutism, acne** (androgen เกิน)
- ลักษณะที่จำเพาะต่อ Cushing มากที่สุด: **proximal myopathy, purple striae กว้าง, ช้ำง่าย, plethora** (เสริม)

### Cortisol diurnal rhythm (สไลด์หน้า 264–266)
- ปกติ **cortisol สูงสุดตอนเช้า (~8 AM) ต่ำสุดเที่ยงคืน**
- **Endogenous Cushing**: **เสีย diurnal rhythm** — cortisol กลางคืนไม่ลด
- **Exogenous Cushing / adrenal insufficiency**: cortisol ของร่างกาย **ต่ำตลอด** (ต่อมถูกกด)

[[fig:endo-06-01-f1]]

### การตรวจวินิจฉัย (สไลด์หน้า 270–271)

1. **R/O exogenous Cushing**: ซักยา/สมุนไพร + **8 AM cortisol ต่ำ** (ร่างกายถูกกด) → exogenous
2. **Screen cortisol excess** (เลือก 1): **24-hr urine free cortisol ↑** · **midnight salivary cortisol ↑** · **low-dose (1 mg overnight) dexamethasone suppression test — กดไม่ลง**
3. **Confirm** ด้วยอีก test หนึ่ง
4. **ACTH**: **↑ → MRI pituitary** (ถ้าไม่เจอ/สงสัย ectopic → imaging หา tumor เช่น CT chest) · **↓ → CT/MRI adrenal**

> **ไม่ส่ง random/afternoon cortisol** เป็นตัว screen (ค่าแกว่งตาม diurnal) · **ไม่ทำ CT adrenal ก่อน** ยืนยัน biochemistry (incidentaloma พบบ่อย) · ACTH stim ใช้กับภาวะ **ขาด** ไม่ใช่เกิน

### การรักษา (เสริม)
- Exogenous: **ค่อย ๆ ลด steroid** (taper) ห้ามหยุดทันที (adrenal crisis)
- Cushing disease → transsphenoidal surgery · adrenal adenoma → adrenalectomy · ectopic → รักษามะเร็ง ± ยาลด cortisol (ketoconazole, metyrapone)
''',
    figs=[F_AXIS],
    pearls=[
        "Cushing ที่พบบ่อยสุด = exogenous steroid (รวมยาลูกกลอน)",
        "ขั้นแรก: 8 AM cortisol ต่ำ = exogenous (ร่างกายถูกกด)",
        "Screen endogenous: 24-hr UFC / midnight salivary / 1 mg DST",
        "ACTH ↑ → MRI pituitary (หรือหา ectopic) · ACTH ↓ → CT adrenal",
        "Hyperpigmentation = ACTH สูง (Cushing disease/ectopic, Addison)",
    ],
    items=[
        mcq("ENDO-06-01-1",
            "A 36-year-old woman has rapid weight gain and worsening acne for 6 months. She denies any regular medication or herbal use. BP 150/90 mmHg. She has a moon face, acne, purplish abdominal striae and proximal muscle weakness. What is the most appropriate investigation?",
            "1-mg overnight dexamethasone suppression test",
            ["4 p.m. serum cortisol", "8 p.m. serum cortisol", "ACTH stimulation test", "CT of the adrenal glands"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ลักษณะ Cushing ชัดและ **ปฏิเสธยา/สมุนไพร** → สงสัย **endogenous Cushing** → **screen** ด้วย **1 mg overnight DST** (หรือ 24-hr UFC/midnight salivary cortisol)
- Cortisol 4 pm/8 pm แบบสุ่มแปลผลไม่ได้ ค่าแกว่งตาม diurnal rhythm (midnight **salivary** cortisol เท่านั้นที่ validated)
- ACTH stimulation test ใช้วินิจฉัยภาวะ **ขาด** cortisol
- CT adrenal ทำหลังยืนยัน hypercortisolism และพบ ACTH ต่ำ''',
            pearl="สงสัย endogenous Cushing → 1 mg DST", topic="Screening",
            ref=[f"{D} หน้า 270, 284–285"], nl=["B11.3(4)", "2.3.4-3(1)"]),
        mcq("ENDO-06-01-2",
            "A 24-year-old woman has taken prednisolone 20 mg daily for 1 year for joint pain. Which abnormality is most likely to be found?",
            "Hypertension",
            ["Hypothyroidism", "Increased bone mass", "Diabetes insipidus", "Peripheral adipose tissue wasting with central fat loss"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Prednisolone ขนาดสูงระยะยาว = **exogenous Cushing syndrome** → **HT** (mineralocorticoid effect + ↑angiotensinogen), hyperglycemia, กระดูกพรุน, central obesity
- Glucocorticoid กด TSH ได้เล็กน้อยแต่ไม่ทำให้ hypothyroidism ทางคลินิก
- Steroid ทำให้มวลกระดูก **ลดลง** (osteoporosis)
- ไม่ทำให้ DI (cortisol ขาดต่างหากที่ทำให้ขับน้ำไม่ได้)
- Cushing ทำให้ไขมัน **สะสมที่แกนกลาง** (central obesity) ขณะที่แขนขาลีบ — ไม่ใช่ไขมันส่วนกลางหายไป''',
            pearl="Steroid ระยะยาว → HT, DM, osteoporosis, central obesity", topic="Exogenous Cushing",
            ref=[f"{D} หน้า 262, 282–283"], nl=["2.3.4-3(1)", "B11.4(3)"]),
        mcq("ENDO-06-01-3",
            "A 48-year-old woman has confirmed endogenous hypercortisolism (elevated 24-hour urine free cortisol and failure to suppress on 1-mg DST). Plasma ACTH is undetectable. What is the most appropriate next investigation?",
            "CT or MRI of the adrenal glands",
            ["MRI of the pituitary", "CT chest to look for small cell lung cancer", "ACTH stimulation test", "Repeat 24-hour urine free cortisol"],
            explain='''Hypercortisolism + **ACTH ต่ำ** = **ACTH-independent (primary)** → ต้นเหตุอยู่ที่ต่อมหมวกไต → **CT/MRI adrenal** (adenoma/carcinoma)
- MRI pituitary และหา ectopic tumor ใช้เมื่อ **ACTH สูง**
- ACTH stimulation test ใช้ในภาวะขาด cortisol
- ยืนยัน cortisol excess ด้วยสอง test แล้ว ไม่ต้องตรวจซ้ำ''',
            pearl="Cushing + ACTH ต่ำ → CT adrenal", topic="Localization",
            ref=[f"{D} หน้า 269–271"], nl=["B11.3(4)", "B11.2.5-3(7)"]),
        mcq("ENDO-06-01-4",
            "A 62-year-old man who smokes heavily has 2 months of proximal weakness, edema, marked hyperpigmentation and new hypertension. K 2.6 mmol/L, HCO3 34 mmol/L, glucose 260 mg/dL. Cortisol is very high and does not suppress; ACTH is markedly elevated. What is the most likely diagnosis?",
            "Ectopic ACTH syndrome from small cell lung cancer",
            ["Adrenal adenoma", "Exogenous glucocorticoid use", "Primary aldosteronism", "Addison disease"],
            explain='''ผู้สูบบุหรี่จัด อาการเกิดเร็ว + **hyperpigmentation** + **hypokalemic metabolic alkalosis รุนแรง** + cortisol สูงมาก + **ACTH สูงมาก** = **ectopic ACTH** (small cell lung CA) — ลักษณะ Cushing คลาสสิกมักยังไม่ทันเกิด
- Adrenal adenoma มี ACTH **ต่ำ** ไม่มี hyperpigmentation
- Exogenous steroid กด ACTH และ cortisol ภายในต่ำ
- Primary aldosteronism ทำ HT + hypoK แต่ cortisol ปกติ ไม่มี hyperpigmentation
- Addison มี hyperpigmentation แต่ cortisol **ต่ำ** และ K สูง''',
            pearl="Cushing + hyperpigmentation + hypoK รุนแรง + ACTH สูงมาก → ectopic ACTH", topic="Ectopic ACTH",
            ref=[f"{D} หน้า 261–262"], nl=["2.3.4-3(1)"]),
    ])

# ---------------------------------------------------------------- 06-02 Adrenal insufficiency
S2 = sec("endo-06-02", "Adrenal insufficiency และ adrenal crisis",
    "1° (Addison): cortisol + aldosterone ↓, ACTH ↑ → hyperpigmentation, K ↑ · 2° (steroid เรื้อรัง/pituitary): K ปกติ ไม่คล้ำ · BP/Na/glucose ต่ำไม่ทราบสาเหตุ → 8AM cortisol · crisis → IV hydrocortisone + fluid + glucose", minutes=10,
    source=f"{D} หน้า 272–281, 286–291", nl=["2.3.4-3(4)", "B11.2.5-3(8)", "B11.3(4)", "B11.4(3)"],
    md='''
### สาเหตุ (สไลด์หน้า 272–273)

| | **1° adrenal insufficiency (Addison)** | **2° adrenal insufficiency** |
|---|---|---|
| สาเหตุ | **Autoimmune** · **infection (TB**, CMV, HIV, fungal) · **adrenal hemorrhage** (anticoagulant, meningococcemia) · infiltration (metastasis) | **ใช้ steroid เรื้อรังแล้วหยุด** (บ่อยที่สุดในทางปฏิบัติ — รวมยาลูกกลอน) · **panhypopituitarism**: pituitary tumor, granuloma, infection, trauma, infarction (**Sheehan**) |
| ฮอร์โมนที่ขาด | **Cortisol + androgen + aldosterone** | **Cortisol + androgen** (aldosterone ปกติ — คุมด้วย RAAS) |
| ACTH | **↑** | ↓/ปกติ |

### อาการ (สไลด์หน้า 274)
- **Hypocortisolism**: อ่อนเพลีย น้ำหนักลด เบื่ออาหาร อ่อนแรง ปวดกล้ามเนื้อ คลื่นไส้อาเจียน ท้องเสีย · **↓BP, ↓glucose, ↓Na**
- **Hypoandrogenism**: libido ลด **ขนรักแร้/หัวหน่าวน้อยลง** (ชัดในผู้หญิง)
- **Hypoaldosteronism (เฉพาะ 1°)**: **อยากกินเค็ม**, ↓Na, **↑K**, **normal anion gap metabolic acidosis**
- **ACTH ↑ → hyperpigmentation** (เหงือก รอยพับฝ่ามือ แผลเป็น) — **เฉพาะ 1°**
- **เมื่อไรควรสงสัย**: **BP ต่ำ, Na ต่ำ, glucose ต่ำ ที่อธิบายไม่ได้**

> ผู้ป่วยกินยาลูกกลอน/สมุนไพร **หน้ากลม (Cushingoid)** แต่มา **อ่อนเพลีย เบื่ออาหาร BP ต่ำ Na ต่ำ glucose ต่ำ** = **2° AI จากหยุด/ขาด exogenous steroid** → ส่ง **8 AM cortisol** · Na ต่ำใน 2° AI เกิดจาก ADH สูง (เหมือน SIADH: Uosm สูง UNa สูง) ไม่ใช่จาก aldosterone (เสริม)

### การตรวจ (สไลด์หน้า 275–278)
1. **ยืนยัน cortisol ต่ำ**: **8 AM cortisol ต่ำ** (< 3–5 mcg/dL ยืนยัน · > 15–18 ตัดออก — เสริม) · **stress cortisol ต่ำ** (ขณะ BP/glucose ต่ำ) · **ACTH stimulation test** (cortisol peak < 18 mcg/dL = AI — เสริม)
2. **ACTH**: **↑ → CT/MRI adrenal, adrenal antibody** · **↓ → MRI pituitary**
- ACTH stim: **1° กระตุ้นไม่ขึ้น** · **2° กระตุ้นขึ้น** (แต่ถ้าเป็นนานจน adrenal atrophy ก็ไม่ขึ้น)

### การรักษา (สไลด์หน้า 279–280)
- **1°**: glucocorticoid (**hydrocortisone** 15–25 mg/วัน แบ่ง 2–3 ครั้ง — เสริม) **+ fludrocortisone** (0.05–0.2 mg/วัน — เสริม) แทน aldosterone
- **2°**: **hydrocortisone อย่างเดียว** (ไม่ต้อง fludrocortisone)
- **Stress-dose steroid (sick day rules)**: **เพิ่มขนาด steroid เมื่อป่วยเฉียบพลัน/ผ่าตัด** (เช่น 2–3 เท่า, ผ่าตัดใหญ่ให้ HC 100 mg IV) เพื่อ **ป้องกัน adrenal crisis**

### Corticosteroid equivalence (สไลด์หน้า 279 เป็นภาพ) (เสริม)

| ยา | ขนาดเทียบเท่า | Mineralocorticoid |
|---|---|---|
| Hydrocortisone | 20 mg | ++ |
| Prednisolone | 5 mg | + |
| Methylprednisolone | 4 mg | ± |
| Dexamethasone | 0.75 mg | 0 |
| Fludrocortisone | — | ++++ |

### Adrenal crisis (สไลด์หน้า 281)
- Trigger: **ป่วยเฉียบพลัน ติดเชื้อ ผ่าตัด stress** · **bilateral adrenal hemorrhage/infarction** · (หยุด steroid กะทันหัน — เสริม)
- **Shock (BP ต่ำ ไม่ตอบสนองต่อ fluid/vasopressor)**, ซึม · คลื่นไส้อาเจียน **ปวดท้อง** (เลียน acute abdomen) · **↓glucose, ↓Na, ↑K**, normal AG metabolic acidosis · cortisol ต่ำ
- **รักษาทันทีไม่ต้องรอผล**: เจาะ cortisol/ACTH เก็บไว้ → **fluid resuscitation (NSS ± dextrose)** + **IV hydrocortisone** (100 mg IV bolus แล้ว 50 mg q6h หรือ 200 mg/วัน — เสริม) + **50% glucose 50 mL IV push** ถ้า hypoglycemia
- Hydrocortisone ≥ 50 mg/วัน มี mineralocorticoid effect พอ ไม่ต้องให้ fludrocortisone ช่วง crisis (เสริม)
''',
    pearls=[
        "Addison: cortisol + aldosterone ↓ ACTH ↑ → hyperpigmentation, K ↑, NAGMA",
        "2° AI (หยุด steroid, pituitary): ไม่คล้ำ K ปกติ ไม่ต้อง fludrocortisone",
        "BP/Na/glucose ต่ำไม่ทราบสาเหตุ (± ยาลูกกลอน) → 8 AM cortisol",
        "ACTH stim: 1° ไม่ขึ้น · 2° ขึ้น (ยกเว้นต่อมฝ่อแล้ว)",
        "Crisis: fluid + IV hydrocortisone ทันทีไม่รอผล · sick day rules ป้องกัน",
    ],
    items=[
        mcq("ENDO-06-02-1",
            "A woman who has taken herbal medicine periodically for a year presents with anorexia and 5 kg weight loss. Weight 80 kg, BP 80/50 mmHg. She has a round, moon-shaped face. What is the most likely diagnosis?",
            "Adrenal insufficiency (secondary to exogenous steroid)",
            ["Insulinoma", "Hypothyroidism", "Panhypopituitarism from a pituitary tumor", "Primary aldosteronism"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ยาสมุนไพร/ลูกกลอนมัก **ผสม steroid** → moon face (exogenous Cushing) · เมื่อหยุด/กินไม่สม่ำเสมอ HPA axis ที่ถูกกดสร้าง cortisol ไม่ได้ → **adrenal insufficiency**: เบื่ออาหาร น้ำหนักลด **BP ต่ำ**
- Insulinoma ทำให้น้ำหนักขึ้น (กินบ่อยแก้น้ำตาลต่ำ) และไม่ทำ BP ต่ำ
- Hypothyroidism ทำให้น้ำหนักขึ้น หน้าบวม แต่ไม่ทำ BP 80/50 แบบนี้
- Panhypopituitarism ก็ทำ AI ได้ แต่ประวัติสมุนไพร + moon face อธิบายได้ตรงกว่า
- Primary aldosteronism ทำให้ BP **สูง**''',
            pearl="ยาลูกกลอน + moon face + BP ต่ำ = AI จาก exogenous steroid", topic="Steroid withdrawal",
            ref=[f"{D} หน้า 272, 286–287"], nl=["2.3.4-3(4)", "B11.4(3)"]),
        mcq("ENDO-06-02-2",
            "A 65-year-old woman with chronic knee pain who takes herbal medicine has fatigue, anorexia and 5 kg weight loss over 3 months. She is obese with a moon face and axillary acanthosis nigricans. FBS 60 mg/dL, BUN 10, Cr 0.8 mg/dL, Na 122, K 5.1, Cl 91, HCO3 22 mmol/L. What is the most useful investigation?",
            "Serum morning (8 a.m.) cortisol",
            ["Thyroid function test", "Dexamethasone suppression test", "Plasma aldosterone level", "Fractional excretion of sodium"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Herbal steroid + **glucose ต่ำ, Na ต่ำ** อ่อนเพลีย น้ำหนักลด → **adrenal insufficiency** → **8 AM cortisol** (ต่ำ) ตามสไลด์
- TFT ไม่อธิบาย hypoglycemia + hyponatremia ร่วมกับประวัติ steroid
- DST ใช้ **screen Cushing (cortisol เกิน)** — ผู้ป่วยรายนี้ปัญหาคือ cortisol ขาด แม้หน้าตาเป็น Cushingoid
- Aldosterone level ไม่ใช่การตรวจแรก (2° AI aldosterone ปกติ)
- FENa ใช้ใน AKI ไม่ช่วยวินิจฉัย AI''',
            pearl="Cushingoid + Na/glucose ต่ำ → 8 AM cortisol (ไม่ใช่ DST)", topic="AI investigation",
            ref=[f"{D} หน้า 275, 288–289"], nl=["B11.3(4)"]),
        mcq("ENDO-06-02-3",
            "A 50-year-old woman with chronic knee pain who has self-medicated for years presents with drowsiness and inability to eat for 2 weeks. BP 120/80 mmHg supine, 90/60 mmHg sitting. Moon face, purplish abdominal striae. Glucose 75 mg/dL, Na 115, K 4.5, Cl 85, HCO3 20 mmol/L; serum osmolality 250, urine osmolality 500 mOsm/kg, urine Na 65 mmol/L. What is the most appropriate investigation?",
            "Serum 8 a.m. cortisol",
            ["Water restriction trial for SIADH without further tests", "Plasma ADH level", "CT brain", "Plasma renin activity"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Hyponatremia ที่ดูเหมือน SIADH (Uosm สูง UNa สูง) ต้อง **R/O adrenal insufficiency และ hypothyroidism ก่อน** เสมอ · ประวัติซื้อยากินเอง (steroid) + orthostatic hypotension + กินไม่ได้ = **2° AI** → **8 AM cortisol** (cortisol ขาดทำให้ ADH หลั่งเพิ่ม → ภาพเหมือน SIADH)
- จำกัดน้ำแบบ SIADH โดยไม่ตรวจ cortisol อาจพลาดภาวะที่อันตรายและแก้ได้ (และมี orthostatic hypotension)
- ADH level ไม่ช่วยในทางปฏิบัติ
- CT brain ไม่ได้ตอบคำถาม
- Renin ใช้กับ 1° AI/aldosterone disorders แต่ K ปกติบ่งชี้ว่า aldosterone ไม่ได้ขาด''',
            pearl="SIADH-like hypoNa → R/O AI (8 AM cortisol) และ hypothyroid ก่อน", topic="AI and hyponatremia",
            ref=[f"{D} หน้า 274–275, 290–291"], nl=["B11.3(4)", "2.3.4-3(5)"]),
        mcq("ENDO-06-02-4",
            "A 34-year-old woman with fatigue, salt craving and darkening of the palmar creases and gums has BP 88/56 mmHg, Na 126, K 5.8 mmol/L, glucose 64 mg/dL. Morning cortisol is 2 mcg/dL with markedly elevated ACTH. In addition to hydrocortisone, which drug is required for long-term therapy?",
            "Fludrocortisone",
            ["Dexamethasone", "Spironolactone", "Desmopressin", "Levothyroxine"],
            explain='''Hyperpigmentation + **K สูง** + ACTH สูง = **primary AI (Addison)** ขาดทั้ง cortisol และ **aldosterone** → ต้องให้ **fludrocortisone** ร่วมกับ hydrocortisone
- Dexamethasone ไม่มี mineralocorticoid effect และไม่ใช่ยาหลักระยะยาว
- Spironolactone ต้าน aldosterone → K สูงขึ้น
- Desmopressin ใช้ใน central DI
- Levothyroxine ใช้เมื่อมี hypothyroid ร่วม (autoimmune polyglandular) — และต้องให้ steroid ก่อนเสมอ''',
            pearl="Addison → hydrocortisone + fludrocortisone", topic="Addison treatment",
            ref=[f"{D} หน้า 273–274, 280"], nl=["B11.2.5-3(8)", "B11.4(3)"]),
        mcq("ENDO-06-02-5",
            "A 58-year-old man who has taken prednisolone 15 mg daily for 2 years stopped it abruptly 5 days ago. He now presents with vomiting, abdominal pain, confusion and BP 70/40 mmHg despite 2 L of 0.9% NaCl. Glucose 52 mg/dL, Na 127 mmol/L. Blood for cortisol has been drawn. What is the most appropriate immediate treatment?",
            "Hydrocortisone 100 mg IV bolus with IV dextrose and saline",
            ["Wait for the cortisol result before giving steroids", "Dexamethasone 0.5 mg orally", "Fludrocortisone 0.1 mg orally alone", "Norepinephrine infusion alone"],
            explain='''หยุด steroid เรื้อรังทันที + shock ไม่ตอบสนองต่อ fluid + glucose ต่ำ Na ต่ำ = **adrenal crisis** → **รักษาทันทีไม่ต้องรอผล**: **IV hydrocortisone** + fluid + **dextrose** แก้ hypoglycemia
- รอผล cortisol ทำให้เสียชีวิตได้ — เจาะเก็บไว้แล้วให้ยาเลย
- Dexamethasone กินขนาดต่ำไม่พอและดูดซึมไม่ได้ในผู้ที่อาเจียน
- Fludrocortisone อย่างเดียวไม่ได้แก้การขาด cortisol
- Vasopressor อย่างเดียวไม่ได้ผลถ้าไม่ได้ cortisol''',
            pearl="Adrenal crisis → IV hydrocortisone ทันที + fluid + glucose", topic="Adrenal crisis",
            ref=[f"{D} หน้า 281"], nl=["2.3.4-3(4)", "B11.4(3)", "2.2.7"]),
    ])

# ---------------------------------------------------------------- 06-03 Sheehan
F_SHEE = fig("endo-06-03-f1", "Sheehan syndrome: ฮอร์โมนที่หายไปและอาการ", '''<svg viewBox="0 0 740 330">
 <defs><marker id="endo-06-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="56" rx="10" class="badsoft"/>
 <text x="370" y="32" text-anchor="middle" class="tb">Postpartum hemorrhage</text>
 <text x="370" y="52" text-anchor="middle" class="t3">pituitary ขยายตอนตั้งครรภ์ → ขาดเลือด</text>
 <path d="M370 66V92" class="ln" marker-end="url(#endo-06-03-a)"/>
 <rect x="250" y="94" width="240" height="40" rx="10" class="acsoft"/>
 <text x="370" y="119" text-anchor="middle" class="tb">Pituitary infarct → empty sella</text>
 <path d="M300 134L90 166" class="ln" marker-end="url(#endo-06-03-a)"/>
 <path d="M330 134L235 166" class="ln" marker-end="url(#endo-06-03-a)"/>
 <path d="M370 134V166" class="ln" marker-end="url(#endo-06-03-a)"/>
 <path d="M410 134L510 166" class="ln" marker-end="url(#endo-06-03-a)"/>
 <path d="M440 134L655 166" class="ln" marker-end="url(#endo-06-03-a)"/>
 <rect x="10" y="168" width="140" height="150" rx="10" class="c1soft"/>
 <text x="80" y="190" text-anchor="middle" class="tb">↓ Prolactin</text>
 <text x="22" y="216" class="t2">น้ำนมไม่มา</text>
 <text x="22" y="236" class="t3">(อาการแรกสุด)</text>
 <rect x="160" y="168" width="140" height="150" rx="10" class="c2soft"/>
 <text x="230" y="190" text-anchor="middle" class="tb">↓ FSH/LH</text>
 <text x="172" y="216" class="t2">ขาดประจำเดือน</text>
 <text x="172" y="236" class="t2">มีบุตรยาก</text>
 <text x="172" y="256" class="t2">ขนรักแร้/</text>
 <text x="172" y="274" class="t2">หัวหน่าวร่วง</text>
 <rect x="310" y="168" width="140" height="150" rx="10" class="misssoft"/>
 <text x="380" y="190" text-anchor="middle" class="tb">↓ TSH</text>
 <text x="322" y="216" class="t2">น้ำหนักขึ้น</text>
 <text x="322" y="236" class="t2">ขี้หนาว ท้องผูก</text>
 <text x="322" y="256" class="t2">ผิวแห้ง เฉื่อย</text>
 <text x="322" y="276" class="t3">FT4 ↓ TSH ไม่ขึ้น</text>
 <rect x="460" y="168" width="130" height="150" rx="10" class="badsoft"/>
 <text x="525" y="190" text-anchor="middle" class="tb">↓ ACTH</text>
 <text x="470" y="216" class="t2">อ่อนเพลีย</text>
 <text x="470" y="236" class="t2">BP ↓ Na ↓</text>
 <text x="470" y="256" class="t2">น้ำตาลต่ำ</text>
 <text x="470" y="276" class="t3">ไม่คล้ำ K ปกติ</text>
 <rect x="600" y="168" width="130" height="150" rx="10" class="oksoft"/>
 <text x="665" y="190" text-anchor="middle" class="tb">↓ ADH</text>
 <text x="612" y="216" class="t2">Central DI</text>
 <text x="612" y="236" class="t2">ปัสสาวะมาก</text>
 <text x="612" y="256" class="t2">กระหายน้ำ</text>
 <text x="612" y="276" class="t3">(posterior, พบน้อย)</text>
</svg>''', "ฮอร์โมนจาก anterior pituitary หายเกือบทั้งหมด — ให้ hydrocortisone ก่อนเสมอแล้วจึงให้ levothyroxine")

S3 = sec("endo-06-03", "Sheehan syndrome (panhypopituitarism หลังคลอด)",
    "PPH → pituitary infarct → empty sella · น้ำนมไม่มา ขาดประจำเดือน ขนร่วง + hypothyroid + 2° AI ± DI · ตรวจระดับฮอร์โมน · ให้ steroid ก่อน LT4", minutes=6,
    source=f"{D} หน้า 292–295", nl=["B11.2.5-3(2)", "2.3.4-3(4)", "B11.4(4)"],
    md='''
### กลไก (สไลด์หน้า 293)
- **Postpartum hemorrhage (+ hypotension) → ischemia ของ pituitary** (ซึ่งขยายใหญ่ขณะตั้งครรภ์จาก lactotroph hyperplasia) → **empty sella turcica**

[[fig:endo-06-03-f1]]

### อาการตามฮอร์โมนที่ขาด
| ฮอร์โมน | อาการ |
|---|---|
| **↓Prolactin** | **ไม่มีน้ำนม (lactation failure)** — อาการแรกที่พบ |
| **↓FSH/LH** | **ขาดประจำเดือน/ประจำเดือนไม่สม่ำเสมอ**, มีบุตรยาก, ขนรักแร้และหัวหน่าวน้อยลง |
| **↓TSH** | น้ำหนักขึ้น ขี้หนาว เฉื่อยชา ท้องผูก ผิวแห้ง (FT4 ต่ำ TSH ต่ำ/ปกติ) |
| **↓ACTH** | น้ำหนักลด อ่อนแรง **BP ต่ำ, Na ต่ำ, hypoglycemia** — **ไม่มี hyperpigmentation, K ปกติ** |
| **↓ADH** | **Central DI**: polyuria, polydipsia (พบน้อยกว่า) |

- อาจมาด้วยอาการเฉียบพลันหลังคลอด หรือ **เรื้อรังเป็นปี** (ไม่มีประจำเดือนตั้งแต่คลอดบุตรคนสุดท้าย) แล้ว **ทรุดเมื่อมี stress/ติดเชื้อ** (เสริม)

### การวินิจฉัยและรักษา
- **Ix: ระดับฮอร์โมน** (8 AM cortisol, FT4 + TSH, FSH/LH/estradiol, prolactin) · MRI pituitary (empty sella)
- **Tx: hormone replacement** — **hydrocortisone ก่อน**, แล้ว **levothyroxine** (ปรับตาม FT4), estrogen/progesterone, desmopressin ถ้ามี DI (เสริม: ให้ LT4 ก่อน steroid → เร่ง cortisol clearance → adrenal crisis)
''',
    figs=[F_SHEE],
    pearls=[
        "PPH + น้ำนมไม่มา + ขาดประจำเดือน = Sheehan",
        "ACTH ขาด → AI ที่ไม่คล้ำ K ปกติ · TSH ขาด → FT4 ต่ำ TSH ไม่ขึ้น",
        "ตรวจระดับฮอร์โมนทุกแกน + MRI (empty sella)",
        "Replace: hydrocortisone ก่อน levothyroxine เสมอ",
    ],
    items=[
        mcq("ENDO-06-03-1",
            "A 40-year-old Thai woman presents with drowsiness for 2 days and fatigue for 2 years. Her last menstrual period was 5 years ago, at the delivery of her last child. She takes no medication. BT 36°C, PR 56/min, BP 90/60 mmHg; drowsy, puffy eyelids, mild pallor, scanty pubic and axillary hair, dry skin. What is the most likely diagnosis?",
            "Panhypopituitarism (Sheehan syndrome)",
            ["Uremia", "Hypercalcemia", "Primary hypothyroidism", "Primary adrenal insufficiency"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**ไม่มีประจำเดือนตั้งแต่คลอดบุตรคนสุดท้าย** + **ขนรักแร้/หัวหน่าวร่วง** (↓gonadotropin + ↓ACTH) + hypothyroid features (bradycardia, hypothermia, หนังตาบวม ผิวแห้ง) + **BP ต่ำ** (↓ACTH) → **panhypopituitarism (Sheehan)**
- Uremia ไม่อธิบายการขาดประจำเดือนหลังคลอดและขนร่วง
- Hypercalcemia ไม่ได้ทำให้ขนร่วงหรือ hypothermia
- Primary hypothyroidism อธิบายได้บางส่วน แต่ไม่อธิบาย amenorrhea + ขนร่วง + BP ต่ำร่วมกัน
- Primary AI ต้องมี hyperpigmentation และไม่ทำให้ hypothyroid features''',
            pearl="ขาดประจำเดือนตั้งแต่คลอด + hypothyroid + BP ต่ำ + ขนร่วง = Sheehan", topic="Sheehan",
            ref=[f"{D} หน้า 293–295"], nl=["B11.2.5-3(2)"]),
        mcq("ENDO-06-03-2",
            "A 29-year-old woman had massive postpartum hemorrhage requiring transfusion 8 weeks ago. She was unable to breastfeed and now has fatigue and dizziness. Which laboratory pattern is most consistent with her condition?",
            "Low FT4 with low-normal TSH, low 8 a.m. cortisol with low ACTH, normal potassium",
            ["Low FT4 with high TSH, low cortisol with high ACTH, high potassium", "High FT4 with low TSH, high cortisol", "Normal FT4 and TSH, high prolactin", "Low FT4 with high TSH, normal cortisol"],
            explain='''Sheehan = **pituitary** เสีย → ฮอร์โมนต้นทาง (TSH, ACTH) **ต่ำหรือไม่ขึ้น** ทั้งที่ฮอร์โมนปลายทาง (FT4, cortisol) ต่ำ · aldosterone ยังคุมด้วย RAAS → **K ปกติ**
- TSH สูง + ACTH สูง + K สูง เป็นลักษณะ **primary** gland failure (Hashimoto + Addison)
- FT4 สูง/cortisol สูง ไม่เข้ากับภาวะขาดฮอร์โมน
- Prolactin สูงเป็นภาวะตรงข้าม (Sheehan → prolactin **ต่ำ** น้ำนมไม่มา)
- TSH สูงบ่งชี้ primary hypothyroidism''',
            pearl="Secondary failure: ฮอร์โมนปลายทางต่ำ + ฮอร์โมน pituitary ต่ำ/ปกติ", topic="Lab pattern",
            ref=[f"{D} หน้า 293"], nl=["B11.2.5-3(2)", "B11.1.2(3)b"]),
        mcq("ENDO-06-03-3",
            "A woman is diagnosed with Sheehan syndrome; 8 a.m. cortisol is 2.5 mcg/dL and FT4 is low with inappropriately normal TSH. Which hormone replacement should be started first?",
            "Hydrocortisone",
            ["Levothyroxine", "Estrogen–progestin", "Desmopressin", "Growth hormone"],
            explain='''ต้องให้ **glucocorticoid ก่อน** levothyroxine เพราะ thyroid hormone **เพิ่ม metabolism/clearance ของ cortisol** → ถ้าให้ LT4 ก่อนในผู้ที่ขาด cortisol อาจเกิด **adrenal crisis**
- Levothyroxine ให้ตามหลังเมื่อได้ steroid แล้ว
- Estrogen–progestin สำคัญระยะยาวแต่ไม่เร่งด่วน
- Desmopressin ให้เฉพาะเมื่อมี DI
- Growth hormone ไม่ใช่ลำดับแรก''',
            pearl="Panhypopit → hydrocortisone ก่อน LT4", topic="Order of replacement",
            ref=[f"{D} หน้า 293"], nl=["B11.4(3)", "B11.4(4)"]),
    ])

LECTURE = lecture("06", "Adrenal & pituitary", "HPA axis · Cushing · adrenal insufficiency · crisis · Sheehan",
    objectives=[
        "อธิบาย HPA axis และใช้ DST/ACTH stimulation test ได้ถูกสถานการณ์",
        "ไล่ work-up Cushing syndrome 4 ขั้นและแยก exogenous/ACTH-dependent/independent",
        "วินิจฉัยและรักษา adrenal insufficiency แยก 1° กับ 2° รวมถึงจากยาลูกกลอน",
        "รักษา adrenal crisis ทันทีและสอน sick day rules",
        "วินิจฉัย Sheehan syndrome และเรียงลำดับการให้ฮอร์โมนทดแทน",
    ],
    sections=[S1, S2, S3])
