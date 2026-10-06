from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Endocrine"
NLT = ["2.3.4(9)", "B11.3(3)"]

# ---------------------------------------------------------------- 03-01 Thyrotoxicosis: TFT & causes
F_TFT = fig("endo-03-01-f1", "อ่าน TFT ด้วยตาราง TSH × FT4", '''<svg viewBox="0 0 740 420">
 <text x="420" y="22" text-anchor="middle" class="tb">FT4 (และ FT3)</text>
 <text x="235" y="48" text-anchor="middle" class="t2">↓ ต่ำ</text>
 <text x="420" y="48" text-anchor="middle" class="t2">↔ ปกติ</text>
 <text x="605" y="48" text-anchor="middle" class="t2">↑ สูง</text>
 <text x="22" y="240" text-anchor="middle" class="tb" transform="rotate(-90 22 240)">TSH</text>
 <text x="78" y="118" text-anchor="middle" class="t2">↑ สูง</text>
 <text x="78" y="238" text-anchor="middle" class="t2">↔ ปกติ</text>
 <text x="78" y="358" text-anchor="middle" class="t2">↓ ต่ำ</text>
 <rect x="145" y="60" width="180" height="112" rx="10" class="c1soft"/>
 <text x="235" y="104" text-anchor="middle" class="tb">Primary</text>
 <text x="235" y="122" text-anchor="middle" class="tb">hypothyroidism</text>
 <text x="235" y="146" text-anchor="middle" class="t3">Hashimoto, post RAI/Sx</text>
 <rect x="330" y="60" width="180" height="112" rx="10" class="c1soft"/>
 <text x="420" y="104" text-anchor="middle" class="tb">Subclinical</text>
 <text x="420" y="122" text-anchor="middle" class="tb">hypothyroidism</text>
 <text x="420" y="146" text-anchor="middle" class="t3">TSH ขึ้นก่อน FT4 ลด</text>
 <rect x="515" y="60" width="180" height="112" rx="10" class="c2soft"/>
 <text x="605" y="104" text-anchor="middle" class="tb">Secondary</text>
 <text x="605" y="122" text-anchor="middle" class="tb">hyperthyroidism</text>
 <text x="605" y="146" text-anchor="middle" class="t3">TSH-oma → MRI pituitary</text>
 <rect x="145" y="180" width="180" height="112" rx="10" class="c2soft"/>
 <text x="235" y="224" text-anchor="middle" class="tb">Secondary</text>
 <text x="235" y="242" text-anchor="middle" class="tb">hypothyroidism</text>
 <text x="235" y="266" text-anchor="middle" class="t3">TSH ไม่ขึ้นตาม → pituitary</text>
 <rect x="330" y="180" width="180" height="112" rx="10" class="oksoft"/>
 <text x="420" y="242" text-anchor="middle" class="tb">Euthyroid</text>
 <rect x="515" y="180" width="180" height="112" rx="10" class="c2soft"/>
 <text x="605" y="224" text-anchor="middle" class="tb">Secondary hyper</text>
 <text x="605" y="242" text-anchor="middle" class="t2">(TSH ไม่ถูกกด)</text>
 <text x="605" y="266" text-anchor="middle" class="t3">หรือเพิ่งกิน LT4 ก่อนเจาะ</text>
 <rect x="145" y="300" width="180" height="112" rx="10" class="c2soft"/>
 <text x="235" y="344" text-anchor="middle" class="tb">Central hypo /</text>
 <text x="235" y="362" text-anchor="middle" class="tb">sick euthyroid</text>
 <text x="235" y="386" text-anchor="middle" class="t3">หรือช่วงฟื้นจาก hyper</text>
 <rect x="330" y="300" width="180" height="112" rx="10" class="misssoft"/>
 <text x="420" y="344" text-anchor="middle" class="tb">Subclinical</text>
 <text x="420" y="362" text-anchor="middle" class="tb">hyperthyroidism</text>
 <text x="420" y="386" text-anchor="middle" class="t3">FT3 ↑ = T3 toxicosis</text>
 <rect x="515" y="300" width="180" height="112" rx="10" class="badsoft"/>
 <text x="605" y="344" text-anchor="middle" class="tb">Primary</text>
 <text x="605" y="362" text-anchor="middle" class="tb">thyrotoxicosis</text>
 <text x="605" y="386" text-anchor="middle" class="t3">Graves, TMNG, TA, thyroiditis</text>
</svg>''', "ใช้ TSH เป็นแกนหลัก: ใน primary disease TSH เปลี่ยนสวนทางกับ FT4 เสมอ ถ้า TSH ไม่สวนทาง (ช่องสีม่วง) ให้คิดถึงต่อมใต้สมอง")

S1 = sec("endo-03-01", "Thyrotoxicosis: สาเหตุ อาการ และการแปลผล TFT/RAIU/scan",
    "Thyrotoxicosis = ฮอร์โมนสูงจากสาเหตุใดก็ได้ · hyperthyroidism = ต่อมทำงานเกิน · TSH เปลี่ยนก่อน (screen) · RAIU ↑ = hyperthyroidism, ↓ = thyroiditis/exogenous · scan เมื่อมี nodule", minutes=10,
    source=f"{D} หน้า 113–120, 139–142", nl=NLT + ["B11.2.5(2)"],
    md='''
### นิยาม (สไลด์หน้า 113)
- **Thyrotoxicosis** = thyroid hormone สูงจาก **สาเหตุใดก็ตาม** (รวม thyroiditis ที่ follicle แตก และกินฮอร์โมนเอง)
- **Hyperthyroidism** = thyroid hormone สูงจาก **ต่อมไทรอยด์สร้างมากขึ้น** (Graves, toxic MNG, toxic adenoma) → **RAIU สูง**

### สาเหตุ

| กลุ่ม | สาเหตุ | RAIU |
|---|---|---|
| Hyperthyroidism | **Graves' disease** (บ่อยสุด), **Toxic MNG**, **Toxic adenoma** | ↑ |
| Destruction | **Thyroiditis** (subacute, painless, postpartum, drug: amiodarone, interferon) | ↓ |
| Exogenous | กิน thyroid hormone / ยาลดน้ำหนัก/สมุนไพร | ↓ |
| hCG-mediated | **Gestational transient thyrotoxicosis**, **molar pregnancy** | ↑ (ห้ามทำในครรภ์) |
| TSH-mediated | TSH-producing pituitary adenoma | ↑ |

### อาการ (สไลด์หน้า 114)
- **ขี้ร้อน** เหงื่อออก ผิวอุ่นชื้น · **ใจสั่น ชีพจรเร็ว** BP systolic สูง **AF** (ผู้สูงอายุ) · เหนื่อย
- **น้ำหนักลดทั้งที่กินเก่ง** · ถ่ายบ่อย
- **Fine tremor** · ตื่นตัว · **reflex ไว** · **proximal muscle weakness**, **periodic paralysis**
- ประจำเดือนน้อย (oligomenorrhea) · **กระดูกพรุน และ hypercalcemia**

### การตรวจ (สไลด์หน้า 115–119)

[[fig:endo-03-01-f1]]

- **TSH เปลี่ยนเป็นตัวแรก → ใช้ screen** · แนะนำส่ง **TSH, FT3, FT4**
- Graves/toxic nodule สร้าง T3 มาก: **FT3 (pg/mL) / FT4 (ng/dL) > 4.4** หรือ **T3 (ng/dL) / T4 (mcg/dL) > 20** · thyroiditis ปล่อยฮอร์โมนที่เก็บไว้ (T4 เด่น) ratio ต่ำกว่า
- **TRAb (TSH receptor antibody)** → Graves
- **Anti-TPO** → autoimmune thyroiditis (Hashimoto, painless thyroiditis)
- **Thyroglobulin ต่ำ** → **exogenous** thyroid hormone (ต่อมไม่ได้ปล่อยฮอร์โมนเอง)
- **RAIU** (รายงานเป็น **ตัวเลข %**): แยก **hyperthyroidism (↑)** กับ **thyroiditis/exogenous (↓)** และใช้คำนวณขนาด I-131
- **Thyroid scan** (รายงานเป็น **ภาพ**): ข้อบ่งชี้ **thyrotoxicosis ที่มี nodule** → แยก **hot nodule** (toxic adenoma/TMNG) กับ **cold nodule**
- **Thyroid U/S**: เมื่อพบ cold nodule เพื่อดู malignancy features

### เปรียบเทียบสาเหตุ (สไลด์หน้า 120)

| | Graves | Toxic MNG | Toxic adenoma | Thyroiditis |
|---|---|---|---|---|
| Goiter | **Diffuse, smooth** | **หลาย nodule** | **nodule เดียว** | Diffuse, **firm** |
| เจ็บ | ไม่เจ็บ | ไม่เจ็บ | ไม่เจ็บ | เจ็บ (subacute) / ไม่เจ็บ |
| RAIU | ↑ | ↑ | ↑ | **↓** |
| Scan | ติดทั่วต่อม (diffuse) | หลายจุด | **จุดเดียว** ส่วนอื่นถูกกด | **ไม่ติด** |
| Antibody | **TRAb** (± anti-TPO, anti-Tg) | ไม่มี | ไม่มี | **Anti-TPO** |

### การรักษาแบบ definitive (สไลด์หน้า 121)
- **Graves**: **anti-thyroid drug (first line)** · radioactive iodine ablation (RAIA, I-131) · thyroid surgery
- **Toxic adenoma / Toxic MNG**: **RAIA หรือ surgery** (ATD ไม่ทำให้หายขาด ใช้ระหว่างรอ definitive)
- ทุกสาเหตุ: **beta-blocker** คุมอาการ
''',
    figs=[F_TFT],
    pearls=[
        "Thyrotoxicosis ≠ hyperthyroidism: thyroiditis/exogenous มี RAIU ต่ำ",
        "TSH เปลี่ยนก่อน FT4 → ใช้ screen",
        "FT3/FT4 >4.4 หรือ T3/T4 >20 → Graves/toxic nodule",
        "Tg ต่ำ + RAIU ต่ำ = กินฮอร์โมนเอง",
        "Toxic adenoma/TMNG รักษาหายด้วย RAI หรือผ่าตัด ไม่ใช่ ATD",
    ],
    items=[
        mcq("ENDO-03-01-1",
            "A 65-year-old man has dyspnea, palpitations and tremor for 5 months. PR 120/min, totally irregular. The thyroid is diffusely enlarged to three times normal size with a bruit. T4 13.6 mcg/dL (5–12), T3 325 ng/dL (60–180), TSH 0.005 mU/L. What is the most likely diagnosis?",
            "Graves' disease",
            ["Painful subacute thyroiditis", "Levothyroxine ingestion", "Toxic adenoma", "Toxic multinodular goiter"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''อาการ **> 3 เดือน**, **diffuse goiter + thyroid bruit** (specific sign ของ Graves) + T3/T4 = 325/13.6 ≈ **24 (> 20)** → **Graves' disease** มาด้วย AF ซึ่งพบบ่อยในผู้สูงอายุ
- Subacute thyroiditis มีคอเจ็บ อาการ < 3 เดือน ไม่มี bruit และ T3/T4 ratio ต่ำ
- กิน LT4 ไม่มี goiter และ T4 เด่นกว่า T3
- Toxic adenoma คลำได้ก้อนเดียว ไม่ใช่ต่อมโตทั่ว ๆ มี bruit
- Toxic MNG คลำได้หลายก้อน''',
            pearl="Diffuse goiter + bruit = Graves", topic="Graves diagnosis",
            ref=[f"{D} หน้า 122, 139–140"], nl=NLT),
        mcq("ENDO-03-01-2",
            "A 22-year-old woman has palpitations, hand tremor and 1 kg weight loss for 1 month. BT 36.6°C, PR 90/min. Thyroid is enlarged to 25 g, firm and non-tender, without bruit; no exophthalmos or onycholysis. T3 200 ng/dL, FT4 3.4 ng/dL, TSH 0.01 mU/L. What is the most appropriate investigation?",
            "Thyroid peroxidase antibody",
            ["Erythrocyte sedimentation rate", "TSH receptor antibody", "Thyroid-stimulating immunoglobulin", "Fine-needle aspiration of the thyroid"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''อาการ **สั้น (1 เดือน)**, ต่อม **firm ไม่เจ็บ**, **ไม่มี** bruit/exophthalmos (ไม่มี specific sign ของ Graves) และ T3 ไม่เด่น → นึกถึง **painless (subacute lymphocytic) thyroiditis** ซึ่งสไลด์ให้ตรวจ **anti-TPO** (ร่วมกับ RAIU ต่ำ)
- ESR สูงช่วยใน **painful** subacute granulomatous thyroiditis ซึ่งต่อมต้องเจ็บ
- TRAb และ TSI คือ antibody ตัวเดียวกันที่ใช้ยืนยัน Graves — ตัวเลือกสองข้อนี้มีความหมายเหมือนกันจึงไม่น่าใช่คำตอบเดียว และภาพทางคลินิกไม่เข้ากับ Graves
- FNA ใช้กับ nodule ที่สงสัยมะเร็ง ไม่ใช่ต่อมโตทั่ว ๆ

(ในเวชปฏิบัติจริง RAIU หรือ TRAb เป็นการตรวจที่แยก Graves กับ thyroiditis ได้ตรงที่สุด แต่ไม่มีในตัวเลือก)''',
            pearl="Thyrotoxicosis สั้น ต่อม firm ไม่เจ็บ ไม่มี Graves sign → painless thyroiditis (anti-TPO, RAIU ↓)", topic="Painless thyroiditis",
            ref=[f"{D} หน้า 131, 141–142"], nl=NLT + ["2.3.4-3(2)"]),
        mcq("ENDO-03-01-3",
            "A 34-year-old woman has thyrotoxic symptoms for 2 months. Thyroid is mildly enlarged and non-tender without nodules or eye signs. TSH <0.01 mU/L, FT4 2.8 ng/dL. Which test best distinguishes Graves' disease from painless thyroiditis?",
            "24-hour radioactive iodine uptake",
            ["Thyroid scan to look for hot nodules", "Thyroid ultrasound for malignancy features", "Serum thyroglobulin level", "Serum cortisol"],
            explain='''Graves = **hyperthyroidism** (ต่อมสร้างเพิ่ม) → **RAIU สูง** · painless thyroiditis = follicle แตกปล่อยฮอร์โมนที่เก็บไว้ ต่อมหยุดจับ iodine → **RAIU ต่ำ** (รายงานเป็นตัวเลข %)
- Thyroid scan (ภาพ) ใช้เมื่อมี nodule เพื่อแยก hot/cold ไม่ใช่โจทย์นี้
- U/S ใช้ดู malignancy features ของ nodule
- Thyroglobulin ใช้แยก **exogenous** thyrotoxicosis (Tg ต่ำ) — thyroiditis Tg สูง Graves ก็สูงได้ จึงแยกสองโรคนี้ไม่ได้
- Cortisol ไม่เกี่ยว (TRAb เป็นอีกทางเลือกที่ดี — เสริม)''',
            pearl="แยก Graves กับ thyroiditis → RAIU (↑ vs ↓)", topic="RAIU",
            ref=[f"{D} หน้า 116, 118"], nl=NLT),
        mcq("ENDO-03-01-4",
            "A 30-year-old woman has palpitations and fatigue. Thyroid is diffusely enlarged. FT4 high, FT3 high, TSH low. What is the most likely diagnosis?",
            "Graves' disease",
            ["Subacute thyroiditis", "Hashimoto thyroiditis", "Toxic adenoma", "Secondary hyperthyroidism from a TSH-secreting adenoma"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Primary thyrotoxicosis (TSH ต่ำ ฮอร์โมนสูง) + **diffuse goiter ไม่เจ็บ** ในหญิงวัยเจริญพันธุ์ = **Graves' disease** ซึ่งเป็นสาเหตุที่พบบ่อยที่สุด
- Subacute thyroiditis มักมีคอเจ็บ ไข้ นำด้วย URI
- Hashimoto โดยทั่วไปทำให้ **hypo**thyroidism (TSH สูง)
- Toxic adenoma คลำได้ก้อนเดียว ไม่ใช่ diffuse
- TSH-oma ต้องมี TSH ปกติหรือสูง ไม่ใช่ต่ำ''',
            pearl="TSH ต่ำ + diffuse goiter ในหญิงอายุน้อย = Graves จนกว่าจะพิสูจน์ได้ว่าไม่ใช่", topic="Graves",
            ref=[f"{D} หน้า 145–146"], nl=NLT),
    ])

# ---------------------------------------------------------------- 03-02 Graves disease
S2 = sec("endo-03-02", "Graves' disease: วินิจฉัยและเลือกการรักษา",
    "TRAb กระตุ้น TSH-R · diffuse smooth goiter + bruit, exophthalmos, pretibial myxedema · ATD first line 12–18 เดือน (MMI; PTU ใน storm/ไตรมาสแรก) · RAI ห้ามในครรภ์ · ผ่าตัดเมื่อคอโต >80 g/สงสัยมะเร็ง", minutes=10,
    source=f"{D} หน้า 121–127, 157–168", nl=NLT + ["B11.4(2)"],
    md='''
### กลไกและอาการ (สไลด์หน้า 122)
- **TSH receptor antibody (TRAb/TSI)** กระตุ้น TSH receptor → ต่อมโต + สร้างฮอร์โมนมาก
- อาการ thyrotoxicosis **นาน > 3 เดือน**
- ต่อม **diffuse, painless, smooth** (25% ไม่โต)
- **Specific signs** (มีข้อใดข้อหนึ่ง = Graves): **exophthalmos** (Graves ophthalmopathy) · **thyroid bruit** · **pretibial myxedema** · **thyroid acropachy** (clubbing)

### การวินิจฉัย (สไลด์หน้า 124)
- TFT: **TSH ↓, T3/FT3 ↑↑, T4/FT4 ↑** · FT3/FT4 > 4.4 หรือ T3/T4 > 20
- **TRAb ↑** · **RAIU ↑** · scan ติดทั่วต่อม (diffuse increased activity)
- มี specific sign ชัดเจนแล้ว วินิจฉัยทางคลินิกได้ไม่ต้องตรวจเพิ่ม

### เลือกการรักษา (สไลด์หน้า 125–126)

| | Anti-thyroid drug (ATD) | Radioactive iodine (RAIA, I-131) | Thyroid surgery |
|---|---|---|---|
| เลือกเมื่อ | **first line** · โรคไม่รุนแรง **goiter เล็ก (< 80 g)** · **ตั้งครรภ์** · ผ่าตัดไม่ได้ · **ophthalmopathy ปานกลาง–รุนแรง** | ผ่าตัดไม่ได้ · **ATD มี major side effect** · วางแผนตั้งครรภ์ **> 6 เดือน** ข้างหน้า | ophthalmopathy ปานกลาง–รุนแรง · **goiter ใหญ่ (> 80 g)/มีอาการกดเบียด** · **สงสัยมะเร็ง** · วางแผนตั้งครรภ์ **< 6 เดือน** |
| ข้อห้าม/ผลเสีย | ดู side effect | **ห้าม: ตั้งครรภ์/ให้นมบุตร, อายุ < 5 ปี** · **permanent hypothyroidism** · **ophthalmopathy แย่ลง** | permanent hypothyroidism · **hypoparathyroidism** · recurrent laryngeal nerve injury (เสริม) · ต้องกิน LT4 ตลอดชีวิต |

### Anti-thyroid drug (สไลด์หน้า 127)
- ให้นาน **12–18 เดือน** แล้วหยุดดู remission (relapse ~50% — เสริม)
- **Methimazole (MMI) = first line** — กินวันละครั้ง ขนาดเริ่ม 10–30 mg/วัน (เสริม)
- **PTU** ใช้เมื่อ: **thyroid storm** (ยับยั้ง T4 → T3 ด้วย) · **ไตรมาสแรกของการตั้งครรภ์** (MMI ทำ aplasia cutis, embryopathy) · **minor side effect จาก MMI**
- ATD ออกฤทธิ์ช้า **2–4 สัปดาห์** (ต้องรอฮอร์โมนที่เก็บไว้หมด) → ระหว่างนี้ให้ **beta-blocker** (propranolol, atenolol, metoprolol) หรือ **CCB (verapamil, diltiazem)** ถ้าใช้ BB ไม่ได้ — **ออกฤทธิ์ทันที**
- ติดตาม **FT3/FT4 ทุก 4–6 สัปดาห์** ช่วงแรก → ปกติแล้ว **ทุก 2–3 เดือน** · **TSH ใช้ติดตามหลัง 6 เดือน** (TSH ถูกกดนานแม้ FT4 ปกติแล้ว)

> ปรับขนาด ATD ด้วย **FT4/FT3** ไม่ใช่ TSH ในช่วงแรก: FT3/FT4 **ต่ำ** = ยาเกิน → **ลดขนาด** · FT3/FT4 **ยังสูง** = **เพิ่มขนาด**

### กลุ่มพิเศษ (เสริม)
- **ตั้งครรภ์**: ไตรมาสแรกใช้ **PTU** (ผู้ที่กิน MMI อยู่แล้วรู้ว่าตั้งครรภ์ → **เปลี่ยนเป็น PTU**) · หลังไตรมาสแรกพิจารณากลับเป็น MMI (PTU เสี่ยงตับ) · ให้ FT4 อยู่ขอบบนของค่าปกติ · ห้าม RAI
- **เด็ก**: ATD (MMI) เป็นหลัก · RAI ห้ามอายุ < 5 ปี
- **Graves ophthalmopathy**: เลิกบุหรี่ · รุนแรงใช้ IV steroid · RAI อาจทำให้แย่ลง (ให้ prednisolone ป้องกัน)
''',
    pearls=[
        "Graves specific signs: exophthalmos, bruit, pretibial myxedema, acropachy",
        "ATD first line 12–18 เดือน · MMI ก่อน · PTU = storm, ไตรมาสแรก, minor SE ของ MMI",
        "ATD ออกฤทธิ์ 2–4 สัปดาห์ → ให้ beta-blocker คุมอาการทันที",
        "ปรับ ATD ตาม FT4/FT3 · ใช้ TSH ติดตามหลัง 6 เดือน",
        "RAI ห้ามในครรภ์/ให้นม/อายุ <5 ปี · ผ่าตัดเมื่อ goiter >80 g หรือสงสัยมะเร็ง",
    ],
    items=[
        mcq("ENDO-03-02-1",
            "A middle-aged woman has palpitations, tremor, fatigue and neck swelling. The thyroid is diffusely enlarged with a bruit. FT4 high, FT3 high, TSH low. What is the most appropriate definitive management to start?",
            "Methimazole",
            ["Propylthiouracil", "Propranolol alone", "Lugol's iodine solution", "Total thyroidectomy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Diffuse goiter + bruit = **Graves** → definitive first line คือ **anti-thyroid drug** และ **methimazole** เป็นตัวแรก (กินวันละครั้ง ตับปลอดภัยกว่า PTU)
- PTU สงวนไว้สำหรับ thyroid storm, ไตรมาสแรกของการตั้งครรภ์ หรือแพ้ MMI แบบ minor
- Propranolol คุมอาการได้ทันทีแต่ไม่ได้ลดการสร้างฮอร์โมน ใช้เสริมไม่ใช่ตัวหลัก
- Lugol's solution ใช้ใน thyroid storm หรือเตรียมผ่าตัด ไม่ใช่การรักษาระยะยาว
- ผ่าตัดใช้เมื่อ goiter ใหญ่ > 80 g สงสัยมะเร็ง หรือ ophthalmopathy รุนแรง''',
            pearl="Graves ทั่วไป → MMI (+ BB คุมอาการ)", topic="First-line ATD",
            ref=[f"{D} หน้า 125, 127, 157–158"], nl=["B11.4(2)"]),
        mcq("ENDO-03-02-2",
            "A 10-year-old girl (weight 30 kg) has lost 4 kg in 1 month with palpitations. PR 150/min, moist skin, tremor and a diffuse neck mass. FT4 high, TSH very low. What is the most appropriate management?",
            "Methimazole",
            ["Levothyroxine", "Radioactive iodine (I-131) ablation", "Near-total thyroidectomy", "Propylthiouracil as first-line long-term therapy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''เด็กที่เป็น **Graves** → **methimazole** เป็นการรักษาหลัก (ร่วมกับ beta-blocker คุม HR 150)
- Levothyroxine ใช้รักษา hypothyroidism ทำให้แย่ลง
- I-131 ในเด็กเล็กหลีกเลี่ยง (ห้ามอายุ < 5 ปี และไม่ใช่ทางเลือกแรกในเด็ก)
- ผ่าตัดใช้เมื่อยาไม่ได้ผล/แพ้ยา หรือ goiter ใหญ่มาก
- PTU ในเด็ก **เสี่ยง fulminant hepatitis** — ไม่แนะนำเป็นยาระยะยาว''',
            pearl="Graves ในเด็ก → MMI (หลีกเลี่ยง PTU)", topic="Graves in children",
            ref=[f"{D} หน้า 125, 161–162"], nl=["B11.4(2)"]),
        mcq("ENDO-03-02-3",
            "A woman with Graves' disease on methimazole for 6 months comes for her first antenatal visit; her last menstrual period was 8 weeks ago. She is clinically stable, there is no goiter, and thyroid function tests are normal. What is the most appropriate management?",
            "Switch methimazole to propylthiouracil",
            ["Discontinue methimazole", "Decrease the methimazole dose", "Increase the methimazole dose", "Continue methimazole at the same dose"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ช่วง **ไตรมาสแรก** (organogenesis) MMI เสี่ยง **methimazole embryopathy** (aplasia cutis, choanal/esophageal atresia) → **เปลี่ยนเป็น PTU** ตามสไลด์ แล้วพิจารณากลับเป็น MMI หลังไตรมาสแรกเพราะ PTU เป็นพิษต่อตับ
- หยุดยาทันทีเสี่ยง relapse ระหว่างตั้งครรภ์ (แนวทาง ATA 2017 ให้พิจารณาหยุดได้เฉพาะผู้ที่ใช้ MMI ขนาดต่ำมาก euthyroid และติดตาม TFT ใกล้ชิด — ข้อสอบยึดการเปลี่ยนเป็น PTU)
- ลด/เพิ่ม/คงขนาด MMI ไม่ได้แก้ปัญหาความเสี่ยงต่อทารก''',
            pearl="Graves + ตั้งครรภ์ไตรมาสแรก → PTU", topic="Pregnancy",
            ref=[f"{D} หน้า 127, 163–164"], nl=["B11.4(2)"]),
        mcq("ENDO-03-02-4",
            "A patient with hyperthyroidism has taken methimazole for about 6 months and feels well. Heart rate is normal and regular. FT3 low, FT4 low, TSH normal. What is the most appropriate management?",
            "Decrease the methimazole dose",
            ["Increase the methimazole dose", "Maintain the same methimazole dose", "Change to propylthiouracil", "Refer for radioactive iodine"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**FT3 และ FT4 ต่ำ** = ได้ยา **เกินขนาด** (iatrogenic hypothyroidism) → **ลดขนาด MMI** · TSH ที่ยังไม่ขึ้นเพราะ TSH ถูกกดมานานและฟื้นช้า จึงปรับยาตาม FT4/FT3 เป็นหลัก
- เพิ่มยาจะยิ่ง hypothyroid
- คงขนาดเดิมจะเกิด hypothyroidism ชัดเจนตามมา
- เปลี่ยนเป็น PTU ไม่มีเหตุผล (ไม่มี side effect)
- RAI ไม่จำเป็นเมื่อโรคตอบสนองต่อยาดี''',
            pearl="On ATD + FT4 ต่ำ = ยาเกิน → ลดขนาด", topic="ATD titration",
            ref=[f"{D} หน้า 127, 165–166"], nl=["B11.4(2)"]),
        mcq("ENDO-03-02-5",
            "A middle-aged woman with hyperthyroidism has taken methimazole for 1 year with good adherence. Vital signs are normal; the thyroid is diffusely enlarged without eye signs. TSH low, FT3 high, FT4 at the upper limit of normal. What is the most appropriate management?",
            "Increase the methimazole dose",
            ["Switch to propylthiouracil", "Add lithium to methimazole", "Total thyroidectomy now", "Stop methimazole and observe for remission"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ยัง **FT3 สูง TSH ต่ำ** = คุมไม่ได้ (T3-predominant) ทั้งที่กินยาสม่ำเสมอและไม่มีผลข้างเคียง → **เพิ่มขนาด MMI**
- เปลี่ยนเป็น PTU ใช้เมื่อมี minor side effect หรือไตรมาสแรก
- Lithium เป็นยาเสริมในกรณีพิเศษ (แพ้ ATD/เตรียม RAI) ไม่ใช่ขั้นแรก
- ผ่าตัดเป็น definitive เมื่อ goiter ใหญ่ สงสัยมะเร็ง หรือยาไม่ได้ผลแม้ขนาดสูง — ยังไม่ถึงขั้นนั้น
- หยุดยาขณะยังมี thyrotoxicosis ไม่ได้ remission''',
            pearl="On ATD ยัง FT3 สูง → เพิ่ม MMI", topic="ATD titration",
            ref=[f"{D} หน้า 167–168"], nl=["B11.4(2)"]),
    ])

# ---------------------------------------------------------------- 03-03 ATD adverse effects
S3 = sec("endo-03-03", "Anti-thyroid drug: ผลข้างเคียง (agranulocytosis, hepatitis)",
    "Minor (rash, arthralgia, GI) → เปลี่ยน ATD อีกตัว · Major (agranulocytosis ANC <500, hepatitis, vasculitis) → หยุดยา ห้ามสลับ → RAI/ผ่าตัด · ไข้ + เจ็บคอ → CBC ทันที", minutes=7,
    source=f"{D} หน้า 128, 169–182", nl=["B11.4(2)", "2.3.4(9)"],
    md='''
### ผลข้างเคียงของ MMI/PTU (สไลด์หน้า 128)

| | ผลข้างเคียง | การจัดการ |
|---|---|---|
| **Minor** | **Rash, arthralgia, GI disturbance** | **เปลี่ยนเป็น ATD อีกตัว** (MMI ↔ PTU) หรือให้ antihistamine ถ้าผื่นเล็กน้อย (เสริม) |
| **Major** | **Agranulocytosis (ANC < 500/mm3)** · **Hepatitis** · **Vasculitis** (ANCA, มักจาก PTU) | **หยุดยา ห้ามสลับไปอีกตัว** (cross-reactivity) → **RAIA (I-131) หรือ thyroid surgery** |

- **MMI = dose-dependent** · **PTU = idiosyncratic**
- **Agranulocytosis**: มักเกิด **ใน 3 เดือนแรก** (เสริม) มาด้วย **ไข้สูง เจ็บคอ แผลในปาก/ทอนซิล** → **CBC ทันที** · หยุดยา + **broad-spectrum antibiotic** (febrile neutropenia) ± G-CSF (เสริม)
- **Hepatitis**: คลื่นไส้อาเจียน ปวดท้อง ตัวตาเหลือง → **LFT** · PTU = hepatocellular necrosis (อาจ fulminant) · MMI = cholestatic (เสริม)
- ก่อนเริ่มยาควรตรวจ CBC และ LFT baseline และ **สอนผู้ป่วยให้หยุดยาและมาโรงพยาบาลทันทีเมื่อมีไข้ เจ็บคอ** (เสริม)

> โจทย์ "Graves กินยา ATD → ไข้ เจ็บคอ" = **agranulocytosis** จนกว่าจะพิสูจน์ได้ว่าไม่ใช่ · ปวดข้อหลายข้อหลังเริ่ม ATD โดยไม่มีข้ออักเสบ = **drug-induced arthralgia** (minor) · ข้อมูลที่สนับสนุนคือ **อาการสัมพันธ์กับการกินยา**
''',
    pearls=[
        "ATD + ไข้ + เจ็บคอ → CBC ทันที (agranulocytosis ANC <500)",
        "Major SE (agranulocytosis, hepatitis, vasculitis) → หยุดยา ไม่สลับ → RAI/ผ่าตัด",
        "Minor SE (rash, arthralgia, GI) → สลับไป ATD อีกตัวได้",
        "MMI = dose-dependent · PTU = idiosyncratic, hepatotoxic",
    ],
    items=[
        mcq("ENDO-03-03-1",
            "A 23-year-old woman with Graves' disease treated with PTU for 3 months presents with high-grade fever and severe sore throat for 2 days. Tonsils are injected with white patches; the thyroid is diffusely enlarged. What is the most likely diagnosis?",
            "Agranulocytosis",
            ["Thyroid storm", "Subacute thyroiditis", "Acute suppurative thyroiditis", "Infectious mononucleosis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ผู้ป่วยที่ได้ **ATD** แล้วมี **ไข้สูง + เจ็บคอ/ทอนซิลอักเสบ** = **agranulocytosis** (major side effect ส่วนใหญ่ใน 3 เดือนแรก) ต้องตรวจ CBC ทันที
- Thyroid storm มีไข้ได้แต่ต้องมี tachycardia รุนแรง สับสน หัวใจล้มเหลว และไม่ได้มาด้วยทอนซิลอักเสบ
- Subacute thyroiditis คอ (ต่อมไทรอยด์) เจ็บ ไม่ใช่เจ็บคอจากทอนซิล
- Acute suppurative thyroiditis พบน้อยมาก มีก้อนบวมแดงร้อนที่ต่อม
- Infectious mononucleosis เป็นได้ แต่ในบริบทที่กิน PTU ต้องคิด agranulocytosis ก่อนเพราะอันตรายถึงชีวิต''',
            pearl="On ATD + ไข้ เจ็บคอ = agranulocytosis", topic="Agranulocytosis",
            ref=[f"{D} หน้า 128, 169–170"], nl=["B11.4(2)"]),
        mcq("ENDO-03-03-2",
            "A 30-year-old woman diagnosed with Graves' disease 1 month ago, treated with PTU 200 mg/day and propranolol, develops acute fever and painful sore throat for 3 days. What is the most appropriate investigation?",
            "Complete blood count",
            ["Thyroid function test", "TSH receptor antibody", "Throat swab culture only", "Liver function test"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ต้องแยก **agranulocytosis** ทันทีด้วย **CBC (ANC)** — ผลกำหนดว่าจะหยุดยาและให้ antibiotic แบบ febrile neutropenia หรือไม่
- TFT ไม่ได้บอกสาเหตุของไข้เจ็บคอ
- TRAb ใช้วินิจฉัย/พยากรณ์ Graves ไม่เกี่ยว
- Throat swab ทำได้แต่ไม่ใช่สิ่งที่สำคัญที่สุด
- LFT ใช้เมื่อสงสัย hepatitis (คลื่นไส้ ตัวเหลือง)''',
            pearl="ไข้ เจ็บคอ บน ATD → CBC · คลื่นไส้ ตัวเหลือง → LFT", topic="Investigation",
            ref=[f"{D} หน้า 171–172"], nl=["B11.4(2)"]),
        mcq("ENDO-03-03-3",
            "A 30-year-old woman with Graves' disease (thyroid 60 g) started PTU 2 months ago. She now has high fever, chills and sore throat with pharyngeal ulcers. WBC is 400/mm3. In addition to broad-spectrum antibiotics, what is the most appropriate management of her antithyroid therapy?",
            "Stop PTU permanently and plan radioactive iodine or surgery",
            ["Decrease the PTU dose", "Switch to methimazole", "Continue PTU and add prednisolone", "Continue PTU and add G-CSF"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (รวมหน้า 173–176)",
            explain='''**Agranulocytosis** (WBC 400) = **major side effect** → **หยุด PTU** และ **ห้ามเปลี่ยนเป็น MMI** (cross-reactivity) → รักษาให้หายขาดด้วย **RAI หรือ thyroidectomy** เมื่อพ้นภาวะติดเชื้อ (สไลด์: Mx switch to RAIA/Sx)
- ลดขนาด PTU ไม่ปลอดภัยเพราะเป็น idiosyncratic ไม่ขึ้นกับขนาด
- เปลี่ยนเป็น MMI เสี่ยงเกิด agranulocytosis ซ้ำ
- Prednisolone ไม่ได้แก้ agranulocytosis
- G-CSF อาจให้ร่วมได้ แต่ต้องหยุด PTU เสมอ''',
            pearl="Agranulocytosis → หยุด ATD ไม่สลับ → RAI/ผ่าตัด", topic="Management of major SE",
            ref=[f"{D} หน้า 128, 173–176"], nl=["B11.4(2)"]),
        mcq("ENDO-03-03-4",
            "A patient with Graves' disease on methimazole develops nausea, vomiting, abdominal pain and jaundice. Liver enzymes and bilirubin are markedly elevated. What is the most appropriate management?",
            "Stop methimazole and plan radioactive iodine or thyroidectomy",
            ["Switch to propylthiouracil", "Reduce the methimazole dose by half", "Continue methimazole and add ursodeoxycholic acid", "Add Lugol's solution and continue methimazole"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**Hepatitis จาก ATD = major side effect** → **หยุด MMI** และเปลี่ยนไปรักษาแบบ **definitive (RAI หรือผ่าตัด)**
- เปลี่ยนเป็น PTU อันตรายกว่าเพราะ PTU เป็นพิษต่อตับรุนแรงกว่า (fulminant hepatic necrosis)
- ลดขนาดไม่พอเมื่อเป็น major side effect
- ให้ยาต่อร่วมกับ UDCA ไม่ได้แก้สาเหตุ
- Lugol's solution ใช้ระยะสั้น ไม่ใช่การรักษาระยะยาว''',
            pearl="ATD hepatitis → หยุดยา → RAI/ผ่าตัด", topic="Hepatitis",
            ref=[f"{D} หน้า 128, 177–178"], nl=["B11.4(2)"]),
        mcq("ENDO-03-03-5",
            "An 18-year-old woman with Graves' disease treated with PTU for 2 months develops pain in all finger joints and both wrists with low-grade fever. Examination shows no joint swelling or redness. Which finding most strongly supports drug-induced arthralgia?",
            "The pain began after starting PTU and improves when the drug is withheld",
            ["Morning stiffness lasting more than 1 hour", "A family history of rheumatoid arthritis", "Pain is related to eating certain foods", "Pain improves with NSAIDs and recurs when NSAIDs are stopped"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (รวมหน้า 179–182)",
            explain='''**Drug-induced arthralgia** เป็น minor side effect ของ ATD — หลักฐานที่ดีที่สุดคือ **ความสัมพันธ์ทางเวลากับยา** (เริ่มหลังให้ยา ดีขึ้นเมื่อหยุด) จัดการโดย **เปลี่ยนเป็น ATD อีกตัว**
- Morning stiffness > 1 ชม. บ่งชี้ inflammatory arthritis เช่น RA
- ประวัติครอบครัวไม่ได้ยืนยันว่าเกิดจากยา
- สัมพันธ์กับอาหารชวนคิด gout
- ตอบสนองต่อ NSAIDs ไม่จำเพาะ เกิดได้กับข้อปวดทุกสาเหตุ

(ข้อสอบจริงถามการวินิจฉัย: drug-induced arthralgia ไม่ใช่ reactive arthritis, Reiter, septic arthritis หรือ SLE เพราะไม่มีข้ออักเสบ/การติดเชื้อนำ — แต่ถ้ามีผื่น ไตอักเสบ ให้นึกถึง PTU-induced ANCA vasculitis/lupus-like)''',
            pearl="ปวดข้อหลังเริ่ม ATD ไม่มีข้ออักเสบ → drug-induced arthralgia → สลับ ATD", topic="Arthralgia",
            ref=[f"{D} หน้า 179–182"], nl=["B11.4(2)"]),
    ])

# ---------------------------------------------------------------- 03-04 TPP
F_TPP = fig("endo-03-04-f1", "ทำไม thyrotoxicosis ทำให้ K ต่ำจนอัมพาต", '''<svg viewBox="0 0 720 300">
 <defs><marker id="endo-03-04-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="20" width="200" height="50" rx="10" class="badsoft"/>
 <text x="110" y="42" text-anchor="middle" class="tb">Thyroxine ↑</text>
 <text x="110" y="60" text-anchor="middle" class="t3">เพิ่มจำนวน pump</text>
 <rect x="10" y="90" width="200" height="50" rx="10" class="misssoft"/>
 <text x="110" y="112" text-anchor="middle" class="tb">Insulin ↑</text>
 <text x="110" y="130" text-anchor="middle" class="t3">มื้อคาร์โบไฮเดรตสูง</text>
 <rect x="10" y="160" width="200" height="50" rx="10" class="misssoft"/>
 <text x="110" y="182" text-anchor="middle" class="tb">β2-adrenergic ↑</text>
 <text x="110" y="200" text-anchor="middle" class="t3">ออกกำลังกาย, stress</text>
 <path d="M210 45L300 100" class="ln" marker-end="url(#endo-03-04-a)"/>
 <path d="M210 115H298" class="ln" marker-end="url(#endo-03-04-a)"/>
 <path d="M210 185L300 130" class="ln" marker-end="url(#endo-03-04-a)"/>
 <rect x="300" y="20" width="260" height="210" rx="16" class="c1soft"/>
 <text x="430" y="44" text-anchor="middle" class="tb">MUSCLE CELL</text>
 <circle cx="380" cy="115" r="34" class="box"/>
 <text x="380" y="111" text-anchor="middle" class="t3">Na/K</text>
 <text x="380" y="127" text-anchor="middle" class="t3">ATPase</text>
 <path d="M414 115H448" class="lnc2" marker-end="url(#endo-03-04-a)"/>
 <text x="380" y="168" text-anchor="middle" class="t3">K+ ถูกดูดเข้าเซลล์</text>
 <text x="454" y="96" class="t2">K+ ในเซลล์ ↑</text>
 <text x="454" y="118" class="t2">→ hyperpolarize</text>
 <text x="454" y="140" class="t2">→ กล้ามเนื้อ</text>
 <text x="454" y="158" class="t2">ไม่ตอบสนอง</text>
 <text x="430" y="210" text-anchor="middle" class="t3">K รวมในร่างกายไม่ได้ขาด (shift)</text>
 <path d="M560 120H598" class="ln" marker-end="url(#endo-03-04-a)"/>
 <rect x="600" y="70" width="112" height="100" rx="10" class="bad"/>
 <text x="656" y="102" text-anchor="middle" class="tw">Serum K ↓</text>
 <text x="656" y="124" text-anchor="middle" class="tw">อ่อนแรง</text>
 <text x="656" y="146" text-anchor="middle" class="tw">proximal</text>
 <rect x="10" y="240" width="700" height="50" rx="10" class="sunk"/>
 <text x="22" y="262" class="tb">รักษา</text>
 <text x="80" y="262" class="t2">KCl ขนาดน้อย (ระวัง rebound hyperK) · propranolol ยับยั้ง β · รักษา hyperthyroidism ให้หาย</text>
 <text x="80" y="282" class="t3">ป้องกัน: propranolol + เลี่ยงมื้อแป้งหนัก ดื่มสุรา ออกกำลังหักโหม</text>
</svg>''', "TPP คือ K ย้ายเข้าเซลล์ ไม่ใช่ K หาย — ตัวกระตุ้นทั้งสามเร่ง Na/K-ATPase เหมือนกัน")

S4 = sec("endo-03-04", "Thyrotoxic periodic paralysis (TPP)",
    "ชายเอเชียหนุ่ม อ่อนแรง proximal เฉียบพลันหลังมื้อแป้ง/ออกกำลังกาย + K ต่ำ → ส่ง TFT · แก้ K ระวัง rebound · ป้องกันด้วย propranolol + รักษา hyperthyroid", minutes=6,
    source=f"{D} หน้า 129, 183–188", nl=["2.3.6(7)", "B3.2.5(1)", "2.3.4(9)"],
    md='''
### กลไก (สไลด์หน้า 129)
- สาเหตุ: **hyperthyroidism** (ส่วนใหญ่ Graves) · พบมากใน **ชายเอเชีย อายุ 20–40 ปี** (เสริม)
- Thyroid hormone เพิ่ม **Na/K-ATPase** ที่กล้ามเนื้อ → เมื่อมีตัวกระตุ้นเพิ่ม (insulin, β2) → **K ย้ายเข้าเซลล์เฉียบพลัน** → hypokalemia → อัมพาต

[[fig:endo-03-04-f1]]

### อาการ
- **Trigger**: **มื้อคาร์โบไฮเดรตสูง** (insulin) · **ออกกำลังกาย, stress** (catecholamine) · สุรา
- **อ่อนแรงเฉียบพลันเป็นพัก ๆ** มักตื่นนอน/กลางคืน หลังมื้อเย็น · **proximal > distal** · ขา > แขน · ไม่มีความผิดปกติของ sensory/cranial nerve · reflex ลดลง
- อาจมีอาการ thyrotoxicosis ชัดหรือไม่ชัดก็ได้

### การตรวจ
- **Serum K ต่ำ** (มักไม่มี acid–base ผิดปกติ, urine K ต่ำ — shift ไม่ใช่สูญเสีย) (เสริม)
- **TFT: TSH ↓, FT3/FT4 ↑** → อ่อนแรง + K ต่ำ ส่ง **E'lyte + TFT** เสมอ

### การรักษา
- **Correct hypokalemia** — ให้ KCl **ขนาดน้อย** (เช่น ≤ 10 mEq/hr รวม < 50–90 mEq) เพราะ K จะกลับออกจากเซลล์ → **rebound hyperkalemia** (เสริม)
- **Non-selective beta-blocker (propranolol)** ช่วยให้หายเร็วและ **ป้องกัน**การเกิดซ้ำ
- **รักษา hyperthyroidism** ให้ euthyroid → อาการไม่กลับเป็นซ้ำ
- **Prevention**: **propranolol** และ **หลีกเลี่ยง trigger**

> ATD ใช้เวลา 2–4 สัปดาห์กว่าจะออกฤทธิ์ → ช่วงแรกที่ยังเป็นซ้ำได้ ตัวป้องกันคือ **propranolol** ไม่ใช่ glucose (ยิ่งกระตุ้น insulin) หรือ KCl ล่วงหน้า
''',
    figs=[F_TPP],
    pearls=[
        "อ่อนแรง proximal เฉียบพลัน + K ต่ำ → ส่ง TFT",
        "Trigger: มื้อแป้งหนัก, ออกกำลังกาย, stress",
        "TPP = K shift → ให้ KCl ขนาดน้อย ระวัง rebound hyperkalemia",
        "ป้องกันซ้ำ = propranolol + รักษา hyperthyroid",
    ],
    items=[
        mcq("ENDO-03-04-1",
            "A 30-year-old man develops leg weakness 2 hours after dinner and cannot get up from the floor. BT 37°C, PR 100/min, BP 120/80 mmHg. Proximal muscle power grade III, no cranial nerve involvement, intact sensation, DTR 1+. What is the most useful investigation (besides serum potassium)?",
            "Thyroid function test",
            ["Chest radiograph", "Electromyography", "Serum creatine kinase", "Acetylcholine receptor antibody"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ชายหนุ่ม อ่อนแรง **proximal เฉียบพลันหลังมื้อเย็น** ไม่มี sensory/cranial nerve ผิดปกติ ชีพจรเร็ว → **periodic paralysis** ซึ่งสไลด์ให้ตรวจ **E'lyte และ TFT** หา **thyrotoxic periodic paralysis**
- CXR ใช้หา thymoma (myasthenia) หรือมะเร็งปอด ไม่ใช่กรณีนี้
- EMG ไม่จำเป็นในภาวะเฉียบพลันที่อธิบายได้ด้วย metabolic cause
- CK ใช้สำหรับ myopathy/rhabdomyolysis ซึ่งไม่เกิดเฉียบพลันใน 2 ชม. หลังมื้ออาหาร
- AChR antibody ใช้กับ myasthenia gravis ซึ่งมัก fatigable และมี ptosis/diplopia''',
            pearl="Periodic paralysis → E'lyte + TFT", topic="TPP work-up",
            ref=[f"{D} หน้า 183–184"], nl=["2.3.6(7)", "B11.3(3)"]),
        mcq("ENDO-03-04-2",
            "A 32-year-old man with palpitations and weight loss has difficulty climbing stairs. BP 150/100 mmHg, PR 120/min. Proximal weakness grade 1/5 in all limbs, normal sensation, reflexes 2+. Na 136, K 2.5, Cl 102, HCO3 22 mmol/L. What is the most appropriate investigation to find the cause of weakness?",
            "Thyroid function test",
            ["Plasma glucose", "CT brain", "CSF profile", "Plasma renin and aldosterone"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ใจสั่น น้ำหนักลด ชีพจรเร็ว + **hypokalemia ที่ไม่มี metabolic alkalosis/acidosis** (HCO3 22) + อัมพาตแบบ proximal → **thyrotoxic periodic paralysis** → ส่ง **TFT**
- Plasma glucose ไม่ได้อธิบาย K ต่ำและอ่อนแรงทั้งตัว
- CT brain ไม่ช่วยเพราะเป็นอ่อนแรงทั้งสี่ระยางค์แบบ proximal ไม่มี UMN sign
- CSF ใช้ใน GBS แต่ GBS reflex หายและ K ไม่ต่ำ
- Renin/aldosterone ใช้หา primary aldosteronism ซึ่งมักมี HT + **metabolic alkalosis** + K ต่ำเรื้อรัง ไม่มีใจสั่นน้ำหนักลด''',
            pearl="K ต่ำ + HCO3 ปกติ + อาการ thyrotoxic → TPP (shift)", topic="TPP vs other hypoK",
            ref=[f"{D} หน้า 185–186"], nl=["2.3.6(7)", "2.2.15"]),
        mcq("ENDO-03-04-3",
            "A woman with newly diagnosed hyperthyroidism (thyroid 50 g) started methimazole 1 week ago. This morning she could not get out of bed because of leg weakness; serum potassium was 2.4 mmol/L and recovered after treatment. Which medication best prevents recurrence while waiting for methimazole to take effect?",
            "Propranolol",
            ["Oral glucose before bedtime", "Prophylactic oral KCl", "Diltiazem", "Spironolactone"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**Non-selective beta-blocker (propranolol)** ยับยั้งการกระตุ้น Na/K-ATPase ทาง β2 → ป้องกัน TPP ได้ระหว่างรอ ATD ออกฤทธิ์ (2–4 สัปดาห์)
- Glucose กระตุ้น insulin → ดัน K เข้าเซลล์ → **กระตุ้น** TPP
- KCl ล่วงหน้าไม่ได้ป้องกัน (K รวมในร่างกายไม่ได้ขาด) และเสี่ยง hyperkalemia
- Diltiazem คุมชีพจรได้แต่ไม่ได้ป้องกัน K shift
- Spironolactone ใช้กับ K ต่ำจาก aldosterone ซึ่งไม่ใช่กลไกนี้''',
            pearl="ป้องกัน TPP = propranolol", topic="TPP prevention",
            ref=[f"{D} หน้า 129, 187–188"], nl=["2.3.6(7)"]),
    ])

# ---------------------------------------------------------------- 03-05 Thyroiditis
F_PHASE = fig("endo-03-05-f1", "Thyroiditis 3 ระยะ", '''<svg viewBox="0 0 720 300">
 <path d="M70 240H700" class="ln"/>
 <path d="M70 240V30" class="ln"/>
 <text x="385" y="290" text-anchor="middle" class="t2">เวลา (เดือน)</text>
 <text x="70" y="258" text-anchor="middle" class="t3">0</text>
 <text x="230" y="258" text-anchor="middle" class="t3">~1–3</text>
 <text x="460" y="258" text-anchor="middle" class="t3">~3–6</text>
 <text x="660" y="258" text-anchor="middle" class="t3">≤ 12</text>
 <path d="M70 140H700" class="lnf"/>
 <text x="698" y="130" text-anchor="end" class="t3">ค่าปกติ</text>
 <path d="M70 140C110 140 130 50 180 50C230 50 250 140 300 150C360 160 400 225 460 225C520 225 560 145 620 140H700" class="lnbad"/>
 <path d="M70 140C110 140 130 220 180 222C240 225 270 160 320 140C370 120 410 60 460 62C520 64 560 135 620 140H700" class="lnc1"/>
 <rect x="560" y="36" width="140" height="56" rx="8" class="sunk"/>
 <path d="M572 54H600" class="lnbad"/>
 <text x="608" y="58" class="t3">FT4/FT3</text>
 <path d="M572 78H600" class="lnc1"/>
 <text x="608" y="82" class="t3">TSH</text>
 <rect x="120" y="150" width="120" height="26" rx="6" class="badsoft"/>
 <text x="180" y="168" text-anchor="middle" class="t3">Thyrotoxic</text>
 <rect x="400" y="148" width="120" height="26" rx="6" class="c1soft"/>
 <text x="460" y="166" text-anchor="middle" class="t3">Hypothyroid</text>
 <rect x="590" y="160" width="100" height="26" rx="6" class="oksoft"/>
 <text x="640" y="178" text-anchor="middle" class="t3">Euthyroid</text>
 <text x="180" y="40" text-anchor="middle" class="t3">follicle แตก</text>
 <text x="460" y="196" text-anchor="middle" class="t3">ฮอร์โมนที่เก็บไว้หมด</text>
</svg>''', "ฮอร์โมนพุ่งช่วงแรกเพราะ follicle แตก (RAIU ต่ำ) แล้วต่ำลงจนกว่าต่อมจะฟื้น — ส่วนใหญ่กลับปกติ ส่วนน้อยเป็น hypothyroid ถาวร")

S5 = sec("endo-03-05", "Thyroiditis: subacute (de Quervain), painless และ postpartum",
    "Follicle แตก → thyrotoxic → hypothyroid → euthyroid · RAIU ต่ำ · painful (de Quervain): หลัง URI, ESR สูง → NSAID/pred · ไม่ให้ ATD · ใช้ beta-blocker", minutes=8,
    source=f"{D} หน้า 130–134, 143–152", nl=["2.3.4-3(2)", "2.3.4(9)"],
    md='''
### กลไกและระยะ (สไลด์หน้า 130, 132)
- **Transient inflammation** ของต่อม → follicle แตก → **ปล่อยฮอร์โมนที่เก็บไว้** (ไม่ได้สร้างเพิ่ม) → **RAIU ต่ำ**
- 3 ระยะ: **Thyrotoxicosis** (TSH ↓ FT3/FT4 ↑) → **Hypothyroidism** (TSH ↑ FT3/FT4 ↓) → **Euthyroid**
- **ส่วนใหญ่กลับเป็นปกติ** ส่วนน้อยเป็น **permanent hypothyroidism**

[[fig:endo-03-05-f1]]

### ชนิด (สไลด์หน้า 131)

| | Subacute **granulomatous** (de Quervain) | Subacute **lymphocytic** (painless) |
|---|---|---|
| ตัวอย่าง | หลัง viral infection | **Postpartum thyroiditis** (ภายใน 1 ปีหลังคลอด), autoimmune, **drug** (amiodarone, lithium, interferon, immune checkpoint inhibitor — เสริม) |
| นำ | **URI นำมาก่อน** · prodrome ไข้ อ่อนเพลีย | ไม่มี prodrome |
| ต่อม | **เจ็บมาก** (ปวดร้าวไปหู/กราม), firm | **ไม่เจ็บ** |
| Ix | TFT, **RAIU ↓**, **ESR ↑**, anti-TPO | TFT, **RAIU ↓**, **anti-TPO** (+ บ่อย) |

### Graves vs subacute thyroiditis (สไลด์หน้า 133)

| | Graves | Subacute thyroiditis |
|---|---|---|
| ระยะเวลา | **> 3 เดือน** | **< 3 เดือน** |
| เจ็บ | ไม่เจ็บ | เจ็บ/ไม่เจ็บ |
| Goiter | **นุ่ม (soft)** | **แข็ง (firm)** |
| Specific sign | มี | ไม่มี |
| FT3/FT4 ratio | **> 4.4** | **< 4.4** |
| RAIU | ↑ | ↓ |

### การรักษา (สไลด์หน้า 134)
- **Thyrotoxic phase**: **beta-blocker** คุมอาการ · ปวด: **NSAID** (เริ่ม) → **prednisolone** ถ้าปวดมาก/NSAID ไม่ได้ผล (เช่น 15–40 mg/วัน แล้ว taper — เสริม) · **ไม่ให้ anti-thyroid drug** (ต่อมไม่ได้สร้างฮอร์โมนเพิ่ม)
- **Hypothyroid phase**: ไม่มีอาการ/อาการน้อย → ไม่ต้องรักษา · อาการมาก → **LT4** ชั่วคราว
- ติดตาม **TFT ทุก 4–8 สัปดาห์** จน euthyroid · โดยมาก **หายเองใน < 12 เดือน**

> คอเจ็บ + เคยเป็นหวัดมาก่อน + ต่อม firm กดเจ็บ = de Quervain · ATD **ไม่ได้ผล** เพราะไม่ใช่การสร้างฮอร์โมนเกิน
''',
    figs=[F_PHASE],
    pearls=[
        "Thyroiditis: thyrotoxic → hypo → euthyroid · RAIU ต่ำ",
        "de Quervain: URI นำ ไข้ ต่อมเจ็บ ESR สูง",
        "Painless/postpartum: ไม่เจ็บ anti-TPO บวก",
        "รักษา: beta-blocker + NSAID/pred · ห้ามให้ ATD",
        "Graves >3 เดือน soft goiter ratio >4.4 · thyroiditis <3 เดือน firm ratio <4.4",
    ],
    items=[
        mcq("ENDO-03-05-1",
            "A 35-year-old man has dyspnea, palpitations and tremor for 1 month. PR 120/min. The thyroid is diffusely enlarged and tender; no exophthalmos or pretibial myxedema. T4 13.6 mcg/dL (5–12), T3 195 ng/dL (60–180), TSH 0.005 mU/L. What is the most likely diagnosis?",
            "Subacute thyroiditis",
            ["Graves' disease", "Levothyroxine ingestion", "Toxic adenoma", "Hashimoto thyroiditis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''อาการ **< 3 เดือน** + ต่อม **กดเจ็บ** + **T3/T4 = 195/13.6 ≈ 14 (< 20)** + ไม่มี specific sign → **subacute (painful) thyroiditis**
- Graves ไม่เจ็บ อาการ > 3 เดือน T3/T4 > 20 และมักมี bruit/exophthalmos
- กิน LT4 ไม่มี goiter และไม่เจ็บ
- Toxic adenoma คลำได้ก้อนเดียว ไม่เจ็บ
- Hashimoto ไม่เจ็บ และส่วนใหญ่มาด้วย hypothyroidism''',
            pearl="Thyrotoxic + ต่อมเจ็บ <3 เดือน + T3/T4 <20 = subacute thyroiditis", topic="Diagnosis",
            ref=[f"{D} หน้า 133, 143–144"], nl=["2.3.4-3(2)"]),
        mcq("ENDO-03-05-2",
            "A 30-year-old woman presents with a painful anterior neck, low-grade fever and palpitations for 2 weeks after a cold. The thyroid is normal in size, firm and tender, without bruit. What is the most likely diagnosis?",
            "Subacute granulomatous (de Quervain) thyroiditis",
            ["Graves' disease", "Toxic adenoma", "Hashimoto thyroiditis", "Factitious thyrotoxicosis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**คอเจ็บ + ไข้ต่ำ ๆ + ใจสั่น** ตามหลังหวัด ต่อม **firm กดเจ็บ** = **de Quervain thyroiditis** (ESR สูง RAIU ต่ำ)
- Graves ไม่เจ็บ มี bruit/exophthalmos
- Toxic adenoma เป็นก้อนเดียวไม่เจ็บ
- Hashimoto ไม่เจ็บ ทำให้ hypothyroid เป็นหลัก
- Factitious thyrotoxicosis ไม่มีต่อมโตหรือเจ็บ''',
            pearl="หลังหวัด + คอเจ็บ + ใจสั่น = de Quervain", topic="de Quervain",
            ref=[f"{D} หน้า 131, 147–148"], nl=["2.3.4-3(2)"]),
        mcq("ENDO-03-05-3",
            "A 50-year-old woman has hand tremor and palpitations. Two weeks ago she had fever and anterior neck pain, now subsided. Vital signs are normal; the thyroid is enlarged (25 g), non-tender, without bruit. TSH is suppressed and FT4 elevated. What is the most appropriate management?",
            "Propranolol",
            ["Methimazole", "Propylthiouracil", "Radioactive iodine", "Levothyroxine"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ประวัติไข้ + คอเจ็บนำมาก่อน = **painful thyroiditis ในระยะ thyrotoxic** → รักษาอาการด้วย **beta-blocker** (และ NSAID/pred ถ้ายังปวด)
- Methimazole และ PTU ยับยั้งการ **สร้าง** ฮอร์โมน แต่ thyroiditis เป็นการ **รั่ว** ของฮอร์โมนที่เก็บไว้ → ไม่ได้ผล
- RAI ใช้ไม่ได้เพราะต่อมจับ iodine ต่ำและโรคหายเอง
- Levothyroxine ใช้ในระยะ hypothyroid ที่มีอาการมาก ไม่ใช่ระยะ thyrotoxic''',
            pearl="Thyroiditis thyrotoxic phase → beta-blocker ไม่ใช่ ATD", topic="Treatment",
            ref=[f"{D} หน้า 134, 149–150"], nl=["2.3.4-3(2)"]),
        mcq("ENDO-03-05-4",
            "A 14-year-old girl presents with fever and neck pain. The thyroid is mildly enlarged and tender. Thyroid function tests are normal and she has no symptoms of hyper- or hypothyroidism. What is the most appropriate management?",
            "Ibuprofen",
            ["Prednisolone as first-line therapy", "Methimazole", "Amoxicillin", "Iodine solution"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Painful (subacute) thyroiditis ในระยะ **euthyroid** → รักษาอาการปวดด้วย **NSAID (ibuprofen)** เป็นขั้นแรก ใช้ prednisolone เมื่อปวดรุนแรงหรือ NSAID ไม่ได้ผล
- Prednisolone ได้ผลดีแต่เป็นทางเลือกที่สองในอาการไม่รุนแรง (สไลด์ให้ NSAID, prednisolone)
- Methimazole ไม่มีที่ใช้ — TFT ปกติและเป็นโรคอักเสบ
- Amoxicillin ใช้ใน acute suppurative thyroiditis (บวมแดงร้อน มีหนอง) ซึ่งพบน้อยมาก
- Iodine ไม่ได้รักษาการอักเสบ''',
            pearl="Subacute thyroiditis ปวด → NSAID ก่อน แล้วค่อย prednisolone", topic="Pain control",
            ref=[f"{D} หน้า 134, 151–152"], nl=["2.3.4-3(2)"]),
        mcq("ENDO-03-05-5",
            "A 29-year-old woman, 4 months postpartum, has palpitations and anxiety. The thyroid is slightly enlarged and non-tender. TSH <0.01 mU/L, FT4 2.6 ng/dL, anti-TPO positive, TRAb negative, 24-hour RAIU 2%. She is breastfeeding. What is the most appropriate management?",
            "Propranolol and repeat thyroid function tests in 4–8 weeks",
            ["Methimazole for 12–18 months", "Radioactive iodine ablation", "Total thyroidectomy", "Prednisolone 40 mg/day"],
            explain='''**Postpartum (painless) thyroiditis**: เกิดภายใน 1 ปีหลังคลอด ไม่เจ็บ **anti-TPO บวก TRAb ลบ RAIU ต่ำ** → ระยะ thyrotoxic รักษาด้วย **beta-blocker** (propranolol ใช้ได้ขณะให้นม) แล้วติดตาม TFT ทุก 4–8 สัปดาห์ เพราะจะตามด้วยระยะ hypothyroid
- Methimazole ไม่ได้ผลเพราะไม่ได้สร้างฮอร์โมนเพิ่ม
- RAI ห้ามขณะให้นม และ uptake ต่ำอยู่แล้ว
- ผ่าตัดไม่จำเป็นในโรคที่หายเอง
- Prednisolone ใช้ใน painful thyroiditis ที่ปวดมาก ไม่ใช่ painless''',
            pearl="Postpartum thyroiditis = painless, anti-TPO+, RAIU ต่ำ → BB + ติดตาม", topic="Postpartum thyroiditis",
            ref=[f"{D} หน้า 131, 134"], nl=["2.3.4-3(2)"]),
    ])

# ---------------------------------------------------------------- 03-06 Exogenous / secondary / subclinical / gestational
S6 = sec("endo-03-06", "Exogenous thyrotoxicosis, secondary & subclinical hyperthyroidism, hCG-mediated",
    "กินฮอร์โมนเอง: ไม่มี goiter, Tg ↓, RAIU ↓ · TSH-oma: FT4 ↑ TSH ไม่ถูกกด + mass effect → MRI/ผ่าตัด · subclinical: TSH ↓ FT4 ปกติ รักษาบางกรณี · GTT: ไตรมาสแรก hCG สูง", minutes=8,
    source=f"{D} หน้า 113, 135–138, 153–156", nl=["2.3.4(9)", "B11.3(3)", "B11.2.4-3(1)"],
    md='''
### Exogenous thyrotoxicosis (factitious) (สไลด์หน้า 135)
- กิน thyroid hormone เกิน (ยาลดน้ำหนัก สมุนไพร/ยาลูกกลอน หรือจงใจ) — มักเป็นบุคลากรการแพทย์/คนอยากผอม (เสริม)
- อาการ thyrotoxicosis แต่ **ไม่มี goiter**
- TFT: **TSH ↓, FT4 ↑↑, FT3 ↔/↑** (ถ้ากิน LT4) · **Thyroglobulin ↓** (ต่อมถูกกด) · **RAIU ↓**
- รักษา: **ลดและหยุดฮอร์โมนที่กิน** · beta-blocker คุมอาการ

### Secondary hyperthyroidism (สไลด์หน้า 136)
- **TSH-producing pituitary adenoma** (TSH-oma) — พบน้อย
- TFT: **FT4/FT3 ↑ กับ TSH ปกติหรือสูง** (TSH ไม่ถูกกดตามที่ควร)
- อาการ thyrotoxicosis + **mass effect**: ปวดศีรษะ **bitemporal hemianopia**
- Ix: MRI pituitary · รักษา: **ผ่าตัด** (transsphenoidal)
- ต้องแยก **thyroid hormone resistance** และการรบกวนของ assay (biotin, heterophile Ab) (เสริม)

### Subclinical hyperthyroidism (สไลด์หน้า 137–138)
- **TSH ↓ กับ FT4/FT3 ปกติ** · ไม่มีอาการหรืออาการน้อย · อาจกลายเป็น overt
- สาเหตุบ่อย: **Graves, toxic MNG, toxic adenoma** (และกิน LT4 เกิน — เสริม)
- ผลเสีย: **AF**, กระดูกพรุน (โดยเฉพาะผู้สูงอายุ หญิงหมดประจำเดือน)
- **รักษาบางกรณี** (สไลด์หน้า 138 เป็นภาพ — ตามแนวทาง ATA/ETA) (เสริม):

| TSH | รักษาเมื่อ |
|---|---|
| **< 0.1 mU/L** | **อายุ ≥ 65 ปี**, โรคหัวใจ/AF, กระดูกพรุน, หญิงหมดประจำเดือน, มีอาการ |
| 0.1–0.4 (ต่ำเล็กน้อย) | พิจารณาเมื่ออายุ ≥ 65 ร่วมกับโรคหัวใจ/กระดูกพรุน/อาการ · อื่น ๆ ติดตาม |

- ก่อนรักษา **ตรวจ TFT ซ้ำใน 6–12 สัปดาห์** เพราะ TSH ต่ำชั่วคราวได้ (เสริม)

### hCG-mediated (สไลด์หน้า 113)
- **Gestational transient thyrotoxicosis (GTT)**: hCG คล้าย TSH กระตุ้น TSH receptor → **ไตรมาสแรก** (สูงสุด 10–12 สัปดาห์) มักร่วมกับ **hyperemesis gravidarum** · TSH ต่ำ FT4 สูงเล็กน้อย **ไม่มี goiter, TRAb ลบ** → **รักษาตามอาการ** (สารน้ำ ± BB) หายเองเมื่อ hCG ลดลง ไม่ให้ ATD (เสริม)
- **Molar pregnancy** (hydatidiform mole, choriocarcinoma): hCG สูงมาก → thyrotoxicosis ชัด → รักษาที่ mole
- **ในครรภ์ไตรมาส 2–3** hCG ลดลง TSH กลับปกติ · total T4 สูงจาก TBG เพิ่ม (estrogen) เป็นเรื่องปกติ — ใช้ **trimester-specific TSH** ในการแปลผล (เสริม)
''',
    pearls=[
        "ไม่มี goiter + Tg ต่ำ + RAIU ต่ำ = กินฮอร์โมนเอง",
        "FT4 สูง แต่ TSH ไม่ถูกกด = secondary (TSH-oma) → MRI pituitary",
        "Subclinical hyper (TSH <0.1) ในผู้สูงอายุ/โรคหัวใจ/กระดูกพรุน → รักษา",
        "ไตรมาสแรก + แพ้ท้องมาก + TSH ต่ำ ไม่มี goiter TRAb ลบ = GTT รักษาตามอาการ",
    ],
    items=[
        mcq("ENDO-03-06-1",
            "A 19-year-old woman has dyspnea and palpitations for 1 month. PR 116/min, tremor; no goiter, exophthalmos or pretibial myxedema. FT4 2.6 ng/dL (0.7–1.4), T3 167 ng/dL (60–180), TSH 0.005 mU/L. What is the most likely diagnosis?",
            "Levothyroxine ingestion (exogenous thyrotoxicosis)",
            ["Graves' disease", "Painful subacute thyroiditis", "Toxic adenoma", "TSH-secreting pituitary adenoma"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Thyrotoxicosis ที่ **ไม่มี goiter** และ **FT4 สูงเด่นแต่ T3 ปกติ** → เข้าได้กับ **กิน LT4** (exogenous) — ยืนยันด้วย **thyroglobulin ต่ำ** และ RAIU ต่ำ
- Graves มี T3 เด่น (ratio สูง) มัก goiter และ specific sign
- Painful thyroiditis มีคอเจ็บและต่อมโต
- Toxic adenoma คลำได้ก้อนและมัก T3 เด่น
- TSH-oma ต้องมี TSH ปกติหรือสูง''',
            pearl="ไม่มี goiter + FT4 สูง T3 ไม่สูง = นึกถึง LT4 ingestion", topic="Exogenous",
            ref=[f"{D} หน้า 135, 153–154"], nl=["2.3.4(9)"]),
        mcq("ENDO-03-06-2",
            "A 26-year-old woman taking a herbal slimming product has palpitations and weight loss. There is no goiter. TSH <0.01 mU/L, FT4 3.0 ng/dL. Which result best confirms the source of thyroid hormone?",
            "Low serum thyroglobulin",
            ["High TSH receptor antibody", "High radioactive iodine uptake", "Positive anti-TPO antibody", "High ESR"],
            explain='''ฮอร์โมนจากภายนอกกด TSH → ต่อมหยุดทำงาน → **thyroglobulin ต่ำ** (ต่างจาก thyroiditis ที่ follicle แตกจน Tg สูง) และ RAIU ต่ำ
- TRAb สูงบ่งชี้ Graves
- RAIU **ต่ำ** ไม่ใช่สูง ในภาวะกินฮอร์โมน
- Anti-TPO บวกบ่งชี้ autoimmune thyroiditis
- ESR สูงบ่งชี้ subacute granulomatous thyroiditis''',
            pearl="Tg ต่ำ แยก exogenous ออกจาก thyroiditis (Tg สูง)", topic="Thyroglobulin",
            ref=[f"{D} หน้า 119, 135"], nl=["B11.3(3)"]),
        mcq("ENDO-03-06-3",
            "A 41-year-old man has palpitations, headache and bitemporal visual field loss. The thyroid is mildly enlarged. FT4 3.1 ng/dL (0.7–1.4), FT3 6.8 pg/mL (2.3–4.2), TSH 4.2 mU/L (0.3–4.5). What is the most appropriate next investigation?",
            "MRI of the pituitary",
            ["Thyroid scan", "TSH receptor antibody", "Thyroid ultrasound with FNA", "Serum thyroglobulin"],
            explain='''FT4/FT3 สูงแต่ **TSH ไม่ถูกกด** (ปกติหรือสูง) = **secondary hyperthyroidism** + ปวดศีรษะ **bitemporal hemianopia** (กดทับ optic chiasm) → **TSH-producing pituitary adenoma** → **MRI pituitary** แล้วผ่าตัด
- Thyroid scan, TRAb, U/S/FNA ใช้กับโรคที่ต่อมไทรอยด์เอง (primary) ซึ่ง TSH ต้องถูกกด
- Thyroglobulin ใช้แยก exogenous thyrotoxicosis''',
            pearl="FT4 สูง + TSH ไม่ต่ำ + bitemporal hemianopia → MRI pituitary", topic="TSH-oma",
            ref=[f"{D} หน้า 136"], nl=["B11.2.4-3(1)", "B11.3(3)"]),
        mcq("ENDO-03-06-4",
            "A 72-year-old woman with osteoporosis has a toxic multinodular goiter. She feels well. On two occasions 8 weeks apart: TSH 0.05 mU/L, FT4 and FT3 within normal limits. What is the most appropriate management?",
            "Treat the hyperthyroidism (e.g., radioactive iodine or antithyroid drug)",
            ["Reassure and repeat thyroid tests in 5 years", "Start levothyroxine", "Prescribe propranolol alone indefinitely", "Thyroid fine-needle aspiration of the largest nodule"],
            explain='''**Subclinical hyperthyroidism** ที่ **TSH < 0.1** ยืนยันซ้ำแล้ว ใน **อายุ ≥ 65 ปี + กระดูกพรุน** → มีข้อบ่งชี้รักษาเพื่อลดความเสี่ยง AF และกระดูกหัก · toxic MNG รักษาให้หายด้วย RAI/ผ่าตัด
- ติดตามห่าง 5 ปีปล่อยความเสี่ยงไว้ (จะติดตามเมื่อ TSH 0.1–0.4 และไม่มีปัจจัยเสี่ยง)
- Levothyroxine ทำให้แย่ลง
- Propranolol ลดอาการหัวใจแต่ไม่ได้ป้องกันกระดูกพรุน
- FNA ทำตามเกณฑ์ U/S ของ nodule ไม่ใช่การรักษา hyperthyroidism และ hot nodule มีโอกาสมะเร็งต่ำ''',
            pearl="Subclinical hyper TSH <0.1 + อายุ ≥65/กระดูกพรุน/หัวใจ → รักษา", topic="Subclinical hyperthyroidism",
            ref=[f"{D} หน้า 137–138"], nl=["2.3.4(9)"]),
        mcq("ENDO-03-06-5",
            "A 24-year-old woman at 9 weeks' gestation has severe nausea and vomiting with mild palpitations. No goiter or eye signs. TSH 0.02 mU/L, FT4 2.0 ng/dL (0.7–1.5), TRAb negative. Pelvic ultrasound shows a normal singleton pregnancy. What is the most likely diagnosis?",
            "Gestational transient thyrotoxicosis",
            ["Graves' disease", "Molar pregnancy", "Toxic multinodular goiter", "Gestational goiter"],
            kind="old", src="ดัดแปลงจากตัวอย่างข้อสอบในสไลด์ หน้า 155",
            explain='''**ไตรมาสแรก + แพ้ท้องรุนแรง** + TSH ต่ำ FT4 สูงเล็กน้อย + **ไม่มี goiter, TRAb ลบ** = **gestational transient thyrotoxicosis** (hCG กระตุ้น TSH receptor) → รักษาตามอาการ หายเองเมื่อ hCG ลดลงหลัง 12–14 สัปดาห์
- Graves มี TRAb บวก goiter/eye sign และอาการก่อนตั้งครรภ์
- Molar pregnancy ตัดได้จาก U/S ที่ปกติ
- Toxic MNG ต้องคลำได้ก้อนหลายก้อน
- Gestational goiter ไม่ใช่คำวินิจฉัยของ thyrotoxicosis

(ข้อในสไลด์ให้ข้อมูล "ครรภ์ 20 สัปดาห์ FT4/FT3 สูงเล็กน้อย TSH ปกติ" ซึ่งเป็นรูปแบบ secondary hyperthyroidism และไม่ตรงกับตัวเลือกใด — จึงเรียบเรียงใหม่ให้มีคำตอบเดียว)''',
            pearl="ไตรมาสแรก + hyperemesis + TSH ต่ำ ไม่มี goiter TRAb ลบ = GTT", topic="Gestational thyrotoxicosis",
            ref=[f"{D} หน้า 113, 155–156"], nl=["2.3.4(9)"]),
    ])

# ---------------------------------------------------------------- 03-07 Thyroid storm
F_STORM = fig("endo-03-07-f1", "Thyroid storm: ยาแต่ละตัวออกฤทธิ์ที่ไหน", '''<svg viewBox="0 0 740 380">
 <defs><marker id="endo-03-07-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="40" width="260" height="190" rx="16" class="c1soft"/>
 <text x="140" y="64" text-anchor="middle" class="tb">ต่อมไทรอยด์</text>
 <rect x="30" y="80" width="220" height="40" rx="8" class="box"/>
 <text x="140" y="105" text-anchor="middle" class="t2">I⁻ → organification → T4/T3</text>
 <rect x="30" y="160" width="220" height="40" rx="8" class="box"/>
 <text x="140" y="185" text-anchor="middle" class="t2">หลั่ง T4 (และ T3) ออกเลือด</text>
 <path d="M140 120V158" class="ln" marker-end="url(#endo-03-07-a)"/>
 <path d="M270 180H340" class="ln" marker-end="url(#endo-03-07-a)"/>
 <rect x="342" y="40" width="200" height="190" rx="16" class="c2soft"/>
 <text x="442" y="64" text-anchor="middle" class="tb">เนื้อเยื่อส่วนปลาย</text>
 <rect x="362" y="80" width="160" height="40" rx="8" class="box"/>
 <text x="442" y="105" text-anchor="middle" class="t2">T4 → T3 (deiodinase)</text>
 <rect x="362" y="160" width="160" height="40" rx="8" class="box"/>
 <text x="442" y="185" text-anchor="middle" class="t2">T3 + β-adrenergic</text>
 <path d="M442 120V158" class="ln" marker-end="url(#endo-03-07-a)"/>
 <path d="M542 180H600" class="ln" marker-end="url(#endo-03-07-a)"/>
 <rect x="602" y="140" width="128" height="80" rx="10" class="bad"/>
 <text x="666" y="172" text-anchor="middle" class="tw">ไข้ HR สูง</text>
 <text x="666" y="194" text-anchor="middle" class="tw">สับสน HF</text>
 <circle cx="30" cy="80" r="11" class="ac"/><text x="30" y="85" text-anchor="middle" class="tw">1</text>
 <circle cx="250" cy="80" r="11" class="ac"/><text x="250" y="85" text-anchor="middle" class="tw">2</text>
 <circle cx="250" cy="160" r="11" class="ac"/><text x="250" y="165" text-anchor="middle" class="tw">2</text>
 <circle cx="362" cy="80" r="11" class="ac"/><text x="362" y="85" text-anchor="middle" class="tw">3</text>
 <circle cx="522" cy="80" r="11" class="ac"/><text x="522" y="85" text-anchor="middle" class="tw">4</text>
 <circle cx="522" cy="160" r="11" class="ac"/><text x="522" y="165" text-anchor="middle" class="tw">4</text>
 <rect x="10" y="246" width="176" height="64" rx="8" class="acsoft"/>
 <text x="22" y="268" class="tb">1 · PTU &gt; MMI</text>
 <text x="22" y="290" class="t3">หยุดการสร้าง (PTU ↓T4→T3)</text>
 <rect x="192" y="246" width="176" height="64" rx="8" class="acsoft"/>
 <text x="204" y="268" class="tb">2 · KI / Lugol</text>
 <text x="204" y="290" class="t3">หยุดสร้างและหลั่ง</text>
 <rect x="374" y="246" width="176" height="64" rx="8" class="acsoft"/>
 <text x="386" y="268" class="tb">3 · HC / dexa</text>
 <text x="386" y="290" class="t3">↓T4→T3 + relative AI</text>
 <rect x="556" y="246" width="174" height="64" rx="8" class="acsoft"/>
 <text x="568" y="268" class="tb">4 · Propranolol</text>
 <text x="568" y="290" class="t3">β-block + ↓T4→T3</text>
 <rect x="10" y="322" width="720" height="50" rx="10" class="sunk"/>
 <text x="22" y="344" class="t2">Iodine ให้ ≥ 1 ชม. หลัง PTU/MMI (ไม่งั้นเป็นวัตถุดิบสร้างฮอร์โมน) · Wolff–Chaikoff effect ยับยั้งการสร้างและหลั่ง</text>
 <text x="22" y="364" class="t3">Supportive: IV fluid · cooling + paracetamol (ห้าม aspirin) · รักษา precipitant · refractory → plasmapheresis</text>
</svg>''', "ยาแต่ละตัวทำงานคนละจุดจึงให้ร่วมกัน — PTU ดีกว่า MMI เพราะยับยั้งทั้งการสร้างในต่อมและการแปลง T4 → T3 ส่วนปลาย")

S7 = sec("endo-03-07", "Thyroid storm",
    "Acute exacerbation ของ thyrotoxicosis อันตรายถึงชีวิต · ไข้ HR สูงมาก สับสน HF · BWPS ≥45 · PTU + iodine (≥1 ชม. หลัง PTU) + steroid + propranolol + supportive · definitive หลัง stable", minutes=8,
    source=f"{D} หน้า 189–195", nl=["2.3.4-3(3)", "B11.2.5-3(4)", "B11.4(2)"],
    md='''
### นิยามและตัวกระตุ้น (สไลด์หน้า 189)
- **Acute exacerbation of hyperthyroidism — life-threatening!** (อัตราตาย 10–30% — เสริม)
- Precipitating factors: **ผ่าตัด, RAIA** · **exogenous iodine (contrast, amiodarone)** · **หยุดยา ATD** · **คลอด** · **ป่วยเฉียบพลัน** (ติดเชื้อบ่อยที่สุด, DKA, trauma)

### การวินิจฉัย — ทางคลินิก (สไลด์หน้า 190–191 เป็นภาพ) (เสริม)
- อาการเด่น: **ไข้สูง**, **tachycardia มาก (> 140)/AF**, **CNS** (กระสับกระส่าย สับสน ชัก โคม่า), **GI–hepatic** (ท้องเสีย อาเจียน ดีซ่าน), **heart failure**
- **Burch–Wartofsky Point Scale (BWPS)**: **≥ 45 = highly suggestive (storm)** · 25–44 = impending · < 25 = unlikely — ให้คะแนนจาก อุณหภูมิ, CNS, GI-hepatic, HR, HF, AF, precipitant
- **Japan Thyroid Association (JTA) criteria**: thyrotoxicosis + CNS manifestation + ≥ 1 ของ ไข้/tachycardia/HF/GI-hepatic
- ระดับ FT4 **ไม่ได้แยก** storm จาก thyrotoxicosis ธรรมดา

### การรักษา (สไลด์หน้า 192–193)

[[fig:endo-03-07-f1]]

| เป้า | ยา | หมายเหตุ / ขนาด (เสริม) |
|---|---|---|
| **ยับยั้งการสร้าง** | **PTU > MMI** | PTU ยับยั้ง **peripheral T4 → T3** ด้วย · PTU 500–1,000 mg loading แล้ว 250 mg q4h (หรือ MMI 60–80 mg/วัน) |
| **ยับยั้งการสร้างและหลั่ง** | **Potassium iodide (SSKI)/Lugol's solution** | **Wolff–Chaikoff effect** · ให้ **≥ 1 ชม. หลัง thionamide** |
| **ยับยั้ง T4 → T3** | **Propranolol** | 60–80 mg q4h · คุม HR |
| | **Hydrocortisone / dexamethasone** | ยับยั้ง T4 → T3 + แก้ **relative adrenal insufficiency** (hypermetabolism สร้าง cortisol ไม่ทัน) · HC 300 mg load แล้ว 100 mg q8h |

- **Symptomatic**: BP ต่ำ → **IV fluid** · ไข้ → **cooling + paracetamol** (**ห้าม aspirin** เพราะแย่ง T4 จาก TBG → free hormone ↑ — เสริม) · HR สูง → **propranolol** (esmolol ถ้า HF — เสริม)
- **รักษา precipitating cause**
- **Refractory → plasmapheresis**
- **Definitive (RAIA/surgery) หลัง stable**
''',
    figs=[F_STORM],
    pearls=[
        "Thyroid storm = thyrotoxicosis + ไข้ HR สูง สับสน HF · BWPS ≥45",
        "PTU ดีกว่า MMI ใน storm (ยับยั้ง T4 → T3 ด้วย)",
        "Iodine ให้หลัง PTU ≥1 ชม. (Wolff–Chaikoff)",
        "Steroid: ↓T4→T3 + relative adrenal insufficiency",
        "ไข้ใช้ paracetamol ห้าม aspirin · definitive หลัง stable",
    ],
    items=[
        mcq("ENDO-03-07-1",
            "A 50-year-old man is brought in with disorientation. BT 38.9°C, BP 130/80 mmHg, RR 28/min, PR 153/min. He is agitated with an enlarged thyroid and warm, moist skin. FT4 8.0 ng/dL, TSH 0.001 mU/L. Which treatment regimen is most appropriate?",
            "PTU, Lugol's solution and dexamethasone (with propranolol)",
            ["PTU and propranolol only", "Methimazole and propranolol only", "PTU and haloperidol", "Methimazole, haloperidol and dexamethasone"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไข้ + HR 153 + **สับสน** + thyrotoxicosis = **thyroid storm** → ต้องให้ยาหลายจุดพร้อมกัน: **PTU** (หยุดสร้าง + ยับยั้ง T4 → T3) + **iodine (Lugol)** หลัง PTU ≥ 1 ชม. (หยุดการหลั่ง) + **steroid** (ยับยั้ง T4 → T3, relative AI) + **propranolol**
- PTU + propranolol อย่างเดียวขาด iodine และ steroid ไม่พอสำหรับ storm
- MMI + propranolol ยิ่งไม่พอ และ MMI ไม่ได้ยับยั้ง peripheral conversion
- Haloperidol ไม่ได้รักษาสาเหตุของการสับสน (เกิดจาก thyrotoxicosis) และลด seizure threshold
- MMI + haloperidol + dexamethasone ขาด iodine และใช้ MMI แทน PTU''',
            pearl="Storm: PTU → iodine → steroid → propranolol", topic="Storm regimen",
            ref=[f"{D} หน้า 192–195"], nl=["2.3.4-3(3)", "B11.4(2)"]),
        mcq("ENDO-03-07-2",
            "A 36-year-old woman with Graves' disease who stopped methimazole 2 months ago presents with pneumonia. BT 40°C, HR 160/min (atrial fibrillation), agitation, vomiting and diarrhea, bilateral crackles. She is started on PTU. When should potassium iodide be given?",
            "At least 1 hour after the first dose of PTU",
            ["Immediately, before PTU", "Only after the patient becomes euthyroid", "Never; iodine is contraindicated in Graves' disease", "Only if PTU fails after 2 weeks"],
            explain='''Iodine ขนาดสูงยับยั้งการสร้างและหลั่งฮอร์โมน (Wolff–Chaikoff) แต่ถ้าให้ **ก่อน** thionamide ต่อมจะใช้ iodine เป็น **วัตถุดิบสร้างฮอร์โมนเพิ่ม** → ให้ **หลัง PTU อย่างน้อย 1 ชม.**
- ให้ก่อน PTU ทำให้ storm แย่ลงได้
- รอจน euthyroid หรือรอ 2 สัปดาห์ ช้าเกินไปสำหรับภาวะวิกฤต
- Iodine ไม่ได้ห้าม ใช้เป็นส่วนสำคัญของการรักษา storm และเตรียมผ่าตัด Graves''',
            pearl="Iodine หลัง thionamide ≥1 ชม.", topic="Timing of iodine",
            ref=[f"{D} หน้า 192"], nl=["2.3.4-3(3)"]),
        mcq("ENDO-03-07-3",
            "A patient with untreated Graves' disease develops fever 39.8°C, tachycardia 150/min and confusion after an emergency appendectomy. Which antipyretic should be avoided?",
            "Aspirin",
            ["Paracetamol", "Cooling blanket", "Ice packs to axillae and groin", "Tepid sponging"],
            explain='''**Aspirin (salicylate) แย่ง T4/T3 ออกจาก thyroxine-binding globulin** → free hormone สูงขึ้น ทำให้ storm แย่ลง จึงใช้ **paracetamol** ร่วมกับ cooling
- Paracetamol เป็นยาลดไข้ที่แนะนำ
- Cooling blanket, ice packs และ tepid sponge เป็นวิธีลดอุณหภูมิทางกายภาพที่ใช้ได้''',
            pearl="Storm ลดไข้ด้วย paracetamol ห้าม aspirin", topic="Supportive care",
            ref=[f"{D} หน้า 193"], nl=["2.3.4-3(3)"]),
        mcq("ENDO-03-07-4",
            "Which precipitating factor is most likely to trigger thyroid storm in a patient with poorly controlled Graves' disease?",
            "Iodinated contrast for a CT scan",
            ["Starting propranolol", "Taking levothyroxine in the morning", "Low-iodine diet before radioiodine", "Calcium carbonate supplementation"],
            explain='''**Exogenous iodine** (contrast, amiodarone) เป็นวัตถุดิบให้ต่อมที่ทำงานเกินสร้างฮอร์โมนมากขึ้น (Jod-Basedow) → precipitate storm ร่วมกับ surgery, RAI, หยุด ATD, คลอด, ติดเชื้อ
- Propranolol เป็นยารักษา ไม่ได้กระตุ้น
- Levothyroxine ไม่ได้ใช้ใน Graves ที่ยังไม่ได้รักษา (ถ้ากินจะทำให้ thyrotoxic แต่ไม่ใช่ precipitant คลาสสิก)
- Low-iodine diet ช่วยให้ RAI ได้ผล ไม่ได้กระตุ้น storm
- Calcium carbonate ไม่เกี่ยว (รบกวนการดูดซึม LT4)''',
            pearl="Contrast/amiodarone (iodine) → precipitate storm", topic="Precipitants",
            ref=[f"{D} หน้า 189"], nl=["2.3.4-3(3)"]),
    ])

LECTURE = lecture("03", "Thyrotoxicosis", "TFT · Graves · ATD side effects · TPP · thyroiditis · storm",
    objectives=[
        "แปลผล TFT, RAIU, thyroid scan และ antibody เพื่อหาสาเหตุ thyrotoxicosis ได้",
        "เลือกการรักษา Graves (ATD/RAI/ผ่าตัด) รวมถึงในหญิงตั้งครรภ์และเด็ก และปรับขนาด ATD ได้",
        "รู้จักและจัดการผลข้างเคียงรุนแรงของ ATD",
        "วินิจฉัยและรักษา TPP, thyroiditis, exogenous/secondary/subclinical hyperthyroidism",
        "สั่งการรักษา thyroid storm ครบทุกกลไกได้",
    ],
    sections=[S1, S2, S3, S4, S5, S6, S7])
