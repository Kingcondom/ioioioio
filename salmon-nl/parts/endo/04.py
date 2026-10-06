from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Endocrine"

# ---------------------------------------------------------------- 04-01 Hypothyroidism
F_HYPO = fig("endo-04-01-f1", "หาสาเหตุ hypothyroidism", '''<svg viewBox="0 0 740 340">
 <defs><marker id="endo-04-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="40" rx="10" class="acsoft"/>
 <text x="370" y="35" text-anchor="middle" class="tb">FT4 ต่ำ — ดู TSH</text>
 <path d="M310 50L180 84" class="ln" marker-end="url(#endo-04-01-a)"/>
 <path d="M430 50L560 84" class="ln" marker-end="url(#endo-04-01-a)"/>
 <rect x="60" y="86" width="240" height="44" rx="10" class="c1"/>
 <text x="180" y="106" text-anchor="middle" class="tw">TSH ↑</text>
 <text x="180" y="122" text-anchor="middle" class="tw">Primary (99%)</text>
 <rect x="440" y="86" width="240" height="44" rx="10" class="c2"/>
 <text x="560" y="106" text-anchor="middle" class="tw">TSH ต่ำ/ปกติ</text>
 <text x="560" y="122" text-anchor="middle" class="tw">Secondary (1%)</text>
 <path d="M560 130V162" class="ln" marker-end="url(#endo-04-01-a)"/>
 <rect x="440" y="164" width="240" height="60" rx="10" class="c2soft"/>
 <text x="560" y="188" text-anchor="middle" class="tb">MRI pituitary</text>
 <text x="560" y="208" text-anchor="middle" class="t3">ประเมิน cortisol ก่อนให้ LT4</text>
 <path d="M180 130V158" class="ln" marker-end="url(#endo-04-01-a)"/>
 <rect x="60" y="160" width="240" height="40" rx="10" class="box"/>
 <text x="180" y="185" text-anchor="middle" class="tb">เคยได้ RAI / ผ่าตัด?</text>
 <path d="M60 180H30V258" class="ln" marker-end="url(#endo-04-01-a)"/>
 <text x="40" y="226" class="t3">ใช่</text>
 <rect x="8" y="260" width="140" height="56" rx="10" class="misssoft"/>
 <text x="78" y="282" text-anchor="middle" class="tb">Post-ablative</text>
 <text x="78" y="300" text-anchor="middle" class="t3">hypothyroidism</text>
 <path d="M220 200V228" class="ln" marker-end="url(#endo-04-01-a)"/>
 <text x="232" y="220" class="t3">ไม่ใช่</text>
 <rect x="160" y="230" width="140" height="34" rx="8" class="box"/>
 <text x="230" y="252" text-anchor="middle" class="tb">Anti-TPO</text>
 <path d="M200 264L190 286" class="ln" marker-end="url(#endo-04-01-a)"/>
 <path d="M270 264L330 286" class="ln" marker-end="url(#endo-04-01-a)"/>
 <rect x="156" y="288" width="120" height="34" rx="8" class="c1soft"/>
 <text x="216" y="310" text-anchor="middle" class="tb">+ Hashimoto</text>
 <rect x="286" y="288" width="250" height="34" rx="8" class="sunk"/>
 <text x="411" y="310" text-anchor="middle" class="t2">− thyroiditis ระยะ hypo, ยา, iodine</text>
</svg>''', "เริ่มจาก TSH แยก primary กับ secondary ก่อน แล้วใช้ประวัติรักษาเดิมและ anti-TPO แยกสาเหตุของ primary (ตามสไลด์หน้า 200)")

S1 = sec("endo-04-01", "Hypothyroidism: สาเหตุ อาการ วินิจฉัย และ levothyroxine",
    "Primary 99% (Hashimoto บ่อยสุด, post RAI/Sx) · TSH ขึ้นก่อน (screen) · ↑TSH ↓FT4 = primary · ไม่ต้องส่ง FT3 · LT4 ตลอดชีวิต กินก่อนอาหาร 1 ชม. แยกจาก Fe/Ca/PPI ≥4 ชม.", minutes=9,
    source=f"{D} หน้า 196–201, 204–211", nl=["2.3.4(4)", "B11.3(3)", "B11.4(2)"],
    md='''
### สาเหตุ (สไลด์หน้า 196)

| Primary (99%) | Secondary (1%) |
|---|---|
| **Hashimoto's thyroiditis** (บ่อยที่สุด) | **Pituitary adenoma**, Sheehan, ผ่าตัด/ฉายแสง pituitary |
| Thyroiditis ระยะ hypothyroid | |
| **Iatrogenic: หลังผ่าตัดไทรอยด์, หลัง RAI** | |
| **Iodine deficiency** | |
| **ยา: lithium, amiodarone** (ATD เกินขนาด, tyrosine kinase inhibitor — เสริม) | |

### อาการ (สไลด์หน้า 198)
- **ขี้หนาว** · ผิวแห้งเย็น ผมเปราะ · **ขนคิ้วด้านนอก 1/3 หาย** (เสริม)
- **Diastolic BP สูง**, **bradycardia** · pericardial effusion (เสริม)
- **น้ำหนักขึ้น** เบื่ออาหาร **ท้องผูก**
- เฉื่อยชา reflex ช้า (**delayed relaxation of ankle jerk**) · ง่วง อ่อนเพลีย
- **Proximal muscle weakness, CPK สูง**
- **Pretibial & periorbital edema (non-pitting myxedema)** · หน้าบวม (puffy face) · เสียงแหบ
- **Entrapment syndrome** เช่น **carpal tunnel syndrome**
- ประจำเดือนผิดปกติ (menorrhagia) · lab: **Na ต่ำ**, **macrocytic anemia**, LDL สูง (เสริม)

### การตรวจ (สไลด์หน้า 199–200)
- **TSH ขึ้นเป็นตัวแรก → ใช้ screen** และเป็นค่าที่ **sensitive ที่สุด** สำหรับ primary hypothyroidism
- **↑TSH + ↓FT4 → primary** · **↔/↓TSH + ↓FT4 → secondary** (→ MRI brain/pituitary)
- **FT3 อาจปกติ** เพราะ peripheral conversion (T4 → T3) เพิ่มขึ้น → **ไม่จำเป็นต้องส่ง**
- สงสัย autoimmune: **anti-TPO**, TgAb (และ TRAb ชนิด blocking)
- **Thyroid U/S** เมื่อคลำได้ nodule

[[fig:endo-04-01-f1]]

### การรักษา (สไลด์หน้า 201)
- **Levothyroxine (LT4) ตลอดชีวิต**
- ขนาดเต็ม ~ **1.6 mcg/kg/วัน** ในคนอายุน้อยไม่มีโรคหัวใจ · **ผู้สูงอายุ/CAD เริ่ม 12.5–25 mcg/วัน** แล้วค่อยเพิ่ม (กัน angina/arrhythmia) (เสริม)
- ติดตาม **FT4, TSH ทุก 4–6 สัปดาห์** หลังปรับขนาด (TSH ใช้เวลา ~6 สัปดาห์ถึง steady state)
- **LT4 ต้องใช้กรดในการดูดซึม** → กิน **ก่อนอาหาร 1 ชม.** หรือ **หลังอาหาร 3–4 ชม.**
- ยา/อาหารที่รบกวนการดูดซึม (กินห่าง **> 4 ชม.**): **iron, calcium, aluminium (antacid)** · **PPI** · **กาแฟ, ผลิตภัณฑ์ถั่วเหลือง**
- **Secondary hypothyroidism**: ติดตามด้วย **FT4** (TSH ใช้ไม่ได้) และ **ประเมิน/ให้ cortisol ก่อน LT4** (เสริม)

> ผู้ป่วยที่เคยคุม TSH ได้ แล้ว TSH ขึ้นใหม่ → ถามเรื่อง **การกินยา และยาใหม่ที่รบกวนการดูดซึม** (PPI, Fe, Ca) ก่อนเพิ่มขนาด
''',
    figs=[F_HYPO],
    pearls=[
        "Primary hypothyroidism 99% · Hashimoto บ่อยสุด · post RAI/Sx ตามมา",
        "TSH = sensitive ที่สุด · ↑TSH ↓FT4 = primary · ไม่ต้องส่ง FT3",
        "LT4 กินท้องว่าง 1 ชม. ก่อนอาหาร · ห่าง Fe/Ca/PPI/กาแฟ >4 ชม.",
        "ผู้สูงอายุ/CAD เริ่ม LT4 ขนาดต่ำ 12.5–25 mcg",
        "TSH ขึ้นใหม่บนยาเดิม → adherence + ยาใหม่ (PPI) ก่อนเพิ่มขนาด",
    ],
    items=[
        mcq("ENDO-04-01-1",
            "A 60-year-old man has gained 3 kg with cold intolerance for 6 months. He has a puffy face and eyelids; BMI 30 kg/m2. What is the most useful investigation to diagnose this condition?",
            "Thyroid function test",
            ["Urine albumin", "BUN and creatinine", "Urinalysis", "Plasma glucose"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ขี้หนาว น้ำหนักขึ้น **หน้าและหนังตาบวม (myxedema)** → **hypothyroidism** → ส่ง **TFT (TSH, FT4)**
- Albuminuria, BUN/Cr และ UA ใช้ประเมินไต (nephrotic syndrome ก็หน้าบวมได้ แต่ไม่อธิบายขี้หนาว)
- Plasma glucose ใช้คัดกรอง DM ไม่ได้อธิบายอาการ''',
            pearl="ขี้หนาว + น้ำหนักขึ้น + หน้าบวม → TFT", topic="Diagnosis",
            ref=[f"{D} หน้า 204–205"], nl=["2.3.4(4)", "B11.3(3)"]),
        mcq("ENDO-04-01-2",
            "A 70-year-old woman with Graves' disease treated with radioactive iodine ablation now has hoarseness, slow thinking and weight gain for 3 months. Which laboratory parameter is the most sensitive for her condition?",
            "TSH",
            ["Free T3", "Free T4", "Thyroid peroxidase antibody", "Antithyroglobulin antibody"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''หลัง RAI เกิด **primary hypothyroidism** · **TSH เปลี่ยนเป็นตัวแรกและ sensitive ที่สุด** (TSH ขึ้นแบบ log-linear เมื่อ FT4 ลดลงเพียงเล็กน้อย)
- FT3 อาจยังปกติจาก peripheral conversion
- FT4 ลดลงช้ากว่าและอยู่ในช่วงปกติได้ในระยะแรก (subclinical)
- Antibody บอกสาเหตุ autoimmune ไม่ได้บอกระดับการทำงานของต่อม''',
            pearl="Primary hypothyroid → TSH sensitive ที่สุด", topic="Most sensitive test",
            ref=[f"{D} หน้า 199, 206–207"], nl=["B11.3(3)"]),
        mcq("ENDO-04-01-3",
            "A 52-year-old woman previously treated with radioactive iodine has fatigue for 3 months. HR 48/min, BT 36°C. She has a puffy face, loss of the lateral third of the eyebrows, slow relaxation of ankle jerks and myoedema. Na 128 mmol/L, Hb 10 g/dL, MCV 102 fL. Which pair of tests is most appropriate to confirm the diagnosis?",
            "TSH and free T4",
            ["Free T3 and total T3", "Serum cortisol and ACTH", "Vitamin B12 and folate only", "Serum osmolality and urine sodium only"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''หลัง RAI + bradycardia, puffy face, ขนคิ้วนอกหาย, **ankle jerk relax ช้า**, myoedema, **Na ต่ำ, macrocytic anemia** = **hypothyroidism** → ยืนยันด้วย **TSH + FT4** (สไลด์: ไม่จำเป็นต้องส่ง FT3)
- FT3/total T3 อาจปกติจาก peripheral conversion ไม่ช่วยวินิจฉัย
- Cortisol/ACTH ใช้หา adrenal insufficiency ซึ่งไม่อธิบาย myoedema/delayed reflex
- B12/folate อธิบาย macrocytosis ได้ แต่ภาพรวมเป็น hypothyroid ซึ่งทำ MCV สูงเองได้
- Sosm/urine Na ใช้ work up hyponatremia แต่สาเหตุหลักชัดเจนแล้ว''',
            pearl="Hypothyroid + Na ต่ำ + MCV สูง → TSH, FT4", topic="Clinical diagnosis",
            ref=[f"{D} หน้า 198–199, 208–209"], nl=["2.3.4(4)", "B11.3(3)"]),
        mcq("ENDO-04-01-4",
            "A woman with Hashimoto thyroiditis (TSH >100 mU/L, FT4 0.2 ng/dL, anti-TPO positive 1 year ago) achieved a normal TSH on levothyroxine 75 mcg/day. Six months ago she was started on omeprazole and domperidone for dyspepsia. Now she is tired and sleepy; TSH is 28 mU/L. What is the most likely cause of the rising TSH?",
            "Omeprazole reducing levothyroxine absorption",
            ["Domperidone increasing levothyroxine clearance", "Progression of Hashimoto thyroiditis", "Development of a TSH-secreting pituitary adenoma", "Laboratory error from heterophile antibodies"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**LT4 ต้องใช้กรดในกระเพาะในการดูดซึม** → **PPI** (omeprazole) ลดการดูดซึม → TSH ขึ้นทั้งที่ขนาดยาเท่าเดิม · แก้โดยแยกเวลา เพิ่มขนาด หรือหยุด PPI
- Domperidone ไม่มีผลสำคัญต่อ clearance ของ LT4
- Hashimoto ที่ได้ replacement เต็มแล้วไม่ทำให้ TSH ขึ้นเร็วขนาดนี้
- TSH-oma ทำให้ FT4 **สูง** และพบน้อยมาก
- Heterophile antibody เป็นไปได้น้อยเมื่อมียาที่อธิบายได้ชัด''',
            pearl="On LT4 แล้ว TSH ขึ้น + เริ่ม PPI → การดูดซึมลด", topic="LT4 absorption",
            ref=[f"{D} หน้า 201, 210–211"], nl=["B11.4(2)"]),
        mcq("ENDO-04-01-5",
            "A 74-year-old man with stable angina is newly diagnosed with primary hypothyroidism: TSH 38 mU/L, FT4 0.4 ng/dL. What is the most appropriate initial levothyroxine regimen?",
            "12.5–25 mcg/day, increased gradually every 4–6 weeks",
            ["Full replacement 1.6 mcg/kg/day from the start", "300 mcg IV loading dose", "Liothyronine (T3) 25 mcg three times daily", "No treatment until angina is revascularized"],
            explain='''ผู้สูงอายุที่มี **coronary artery disease** → **เริ่ม LT4 ขนาดต่ำ 12.5–25 mcg/วัน** แล้วเพิ่มทีละน้อยทุก 4–6 สัปดาห์ตาม TSH เพื่อไม่ให้ความต้องการ O2 ของหัวใจเพิ่มเร็วจน angina/MI/arrhythmia
- ขนาดเต็มตั้งแต่แรกใช้กับคนอายุน้อยไม่มีโรคหัวใจ
- IV loading ใช้ใน myxedema coma
- T3 ออกฤทธิ์เร็วและแรง เสี่ยงต่อหัวใจ ไม่ใช่ยามาตรฐาน
- ไม่ต้องรอ revascularization — hypothyroid ที่ไม่รักษาก็ทำให้หัวใจแย่ลง''',
            pearl="สูงอายุ/CAD → LT4 start low go slow", topic="LT4 dosing",
            ref=[f"{D} หน้า 201"], nl=["B11.4(2)"]),
    ])

# ---------------------------------------------------------------- 04-02 Subclinical hypothyroidism & goiter
S2 = sec("endo-04-02", "Subclinical hypothyroidism และ non-nodular goiter",
    "TSH ↑ FT4 ปกติ · สาเหตุ Hashimoto, iodine, post Sx/RAI · รักษาเมื่อ TSH ≥10, ตั้งครรภ์/วางแผน, มีอาการ · goiter ไม่มี nodule → TFT + anti-TPO/anti-Tg · TFT ปกติ antibody ลบ → ติดตาม", minutes=7,
    source=f"{D} หน้า 202–203, 212–213, 237–242", nl=["2.3.4(4)", "2.3.4(3)", "B11.2.5(1)"],
    md='''
### Subclinical hypothyroidism (สไลด์หน้า 202)
- **TSH ↑ กับ FT4 ปกติ** · ไม่มีอาการหรืออาการน้อย · **อาจกลายเป็น overt** (โดยเฉพาะ anti-TPO บวก ~4%/ปี — เสริม)
- สาเหตุบ่อย: **Hashimoto thyroiditis**, **iodine deficiency**, **หลังผ่าตัด**, **หลัง RAI**
- ตรวจซ้ำใน 2–3 เดือนก่อนสรุป (TSH สูงชั่วคราวได้ เช่น ช่วงฟื้นจาก sick euthyroid) (เสริม)

### เมื่อไรควรรักษา (สไลด์หน้า 203 เป็นภาพ — ตามแนวทางสากล) (เสริม)

| สถานการณ์ | แนวทาง |
|---|---|
| **TSH ≥ 10 mU/L** | **รักษาด้วย LT4** |
| **ตั้งครรภ์ หรือวางแผนตั้งครรภ์/มีบุตรยาก** | รักษา (เป้า TSH < 2.5) |
| TSH 4.5–10 + มีอาการ, anti-TPO บวก, goiter, อายุน้อย | พิจารณารักษา |
| TSH 4.5–10 ไม่มีอาการ/ผู้สูงอายุ > 70 ปี | **ติดตาม TFT** ทุก 6–12 เดือน |

### Goiter ที่ไม่มี nodule (non-nodular/diffuse goiter) (สไลด์หน้า 237–242)

1. **ส่ง TFT ก่อนเสมอ** (แม้มี bruit หรือดูเหมือน Graves — ต้องรู้ภาวะการทำงานของต่อม)
2. TSH ปกติหรือสูง → ส่ง **thyroid antibody (anti-TPO, anti-Tg)** หา **Hashimoto thyroiditis**
3. **TFT ปกติ + antibody ลบ** = simple (colloid) goiter → **ติดตามอาการและ TFT** · ผ่าตัดเฉพาะเมื่อกดเบียด/ความงาม (เสริม)

> หญิงอายุน้อย คอโต ไม่เจ็บ **TSH สูง FT4 ปกติ** → **subclinical hypothyroidism จาก Hashimoto** (สาเหตุบ่อยที่สุดในพื้นที่ที่ได้ iodine พอ) · ไม่ให้ LT4 ใน simple goiter ที่ TFT ปกติ (LT4 suppressive ไม่แนะนำแล้ว — เสริม)
''',
    pearls=[
        "Subclinical hypo = TSH สูง FT4 ปกติ · ตรวจซ้ำก่อนสรุป",
        "รักษาเมื่อ TSH ≥10 หรือ ตั้งครรภ์/วางแผนตั้งครรภ์",
        "Goiter ไม่มี nodule → TFT ก่อน แล้ว anti-TPO/anti-Tg",
        "TFT ปกติ + antibody ลบ → ติดตาม ไม่ต้องให้ยา",
    ],
    items=[
        mcq("ENDO-04-02-1",
            "An 18-year-old woman has had painless neck enlargement for 3 months without other symptoms. The thyroid is diffusely enlarged and rubbery. TSH is high and FT4 is normal. What is the most likely diagnosis?",
            "Hashimoto thyroiditis",
            ["Simple colloid goiter", "Graves' disease", "Iodine deficiency goiter", "Subacute thyroiditis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''TSH สูง FT4 ปกติ = **subclinical hypothyroidism** · หญิงอายุน้อย คอโตแบบ **diffuse, rubbery, ไม่เจ็บ** → สาเหตุที่พบบ่อยที่สุดคือ **Hashimoto thyroiditis** (ยืนยันด้วย anti-TPO)
- Simple goiter มี TFT ปกติ
- Graves ทำให้ TSH ต่ำ
- Iodine deficiency เป็นได้ในพื้นที่ขาด iodine แต่ในข้อสอบ Hashimoto พบบ่อยกว่าและเข้ากับ rubbery goiter
- Subacute thyroiditis เจ็บ และมักมีระยะ thyrotoxic ก่อน''',
            pearl="หญิงสาวคอโต TSH สูง FT4 ปกติ → Hashimoto", topic="Subclinical hypothyroidism",
            ref=[f"{D} หน้า 202, 212–213"], nl=["2.3.4(4)", "2.3.4(3)"]),
        mcq("ENDO-04-02-5",
            "A 35-year-old woman is found to have a diffusely enlarged thyroid gland with a bruit on routine examination. She has no nodules. What is the most appropriate next investigation?",
            "Thyroid function test (TSH, FT4)",
            ["Thyroid peroxidase antibody", "Thyroid scan", "Fine-needle aspiration", "CT neck"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Goiter ทุกรายเริ่มที่ **TFT** เพื่อรู้ภาวะการทำงานของต่อม — แม้ thyroid bruit จะชวนนึกถึง Graves ก็ต้องยืนยัน thyrotoxicosis ก่อน แล้วค่อยเลือกตรวจต่อ (TRAb/RAIU ถ้า TSH ต่ำ, anti-TPO ถ้า TSH ปกติ/สูง)
- Antibody ส่งหลังรู้ผล TFT
- Thyroid scan ใช้เมื่อ TSH ต่ำร่วมกับ nodule
- FNA ใช้กับ nodule ที่เข้าเกณฑ์
- CT neck ไม่จำเป็น เว้นแต่ goiter ใหญ่ลงช่องอก/กดหลอดลม''',
            pearl="Goiter ทุกราย → TFT ก่อน", topic="Goiter first step",
            ref=[f"{D} หน้า 237–238"], nl=["2.3.4(3)", "B11.3(3)"]),
        mcq("ENDO-04-02-2",
            "A 14-year-old girl has a visible, non-tender diffuse neck enlargement without palpitations or weight loss. FT3, FT4 and TSH are normal. What is the most appropriate next investigation?",
            "Anti-thyroid peroxidase (anti-microsomal) and anti-thyroglobulin antibodies",
            ["Thyroid scan", "Fine-needle aspiration", "Empirical levothyroxine", "Subtotal thyroidectomy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Diffuse goiter ไม่มี nodule TSH ปกติ → ส่ง **thyroid antibody (anti-TPO = anti-microsomal, anti-Tg)** เพื่อ R/O **Hashimoto** ซึ่งเป็นสาเหตุ goiter ที่พบบ่อยในวัยรุ่นหญิง
- Thyroid scan ใช้เมื่อ TSH ต่ำและมี nodule
- FNA ใช้กับ nodule ที่มีลักษณะสงสัยมะเร็งตามเกณฑ์ U/S
- LT4 ไม่ต้องให้เมื่อ TFT ปกติ
- ผ่าตัดเฉพาะเมื่อกดเบียดหรือสงสัยมะเร็ง''',
            pearl="Diffuse goiter + TFT ปกติ → anti-TPO/anti-Tg", topic="Goiter work-up",
            ref=[f"{D} หน้า 239–240"], nl=["2.3.4(3)", "B11.2.5(1)"]),
        mcq("ENDO-04-02-3",
            "A 15-year-old girl has a diffusely enlarged thyroid (30 g) without nodules that has slowly increased over 6 months. She has no features of hyper- or hypothyroidism. TFT is normal; anti-TPO and TRAb are negative. What is the most appropriate management?",
            "Reassure and follow clinically with periodic TFT",
            ["Methimazole", "Levothyroxine suppressive therapy", "Total thyroidectomy", "Prednisolone"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Non-nodular goiter, **TFT ปกติ, antibody ลบ** = simple (colloid) goiter → **reassure และติดตามอาการ + TFT**
- Methimazole ไม่มีที่ใช้ เพราะไม่ได้ thyrotoxic
- LT4 suppressive therapy ไม่แนะนำแล้ว (ประโยชน์น้อย เสี่ยง subclinical hyperthyroidism)
- ผ่าตัดเฉพาะเมื่อกดเบียดหรือสงสัยมะเร็ง
- Prednisolone ใช้ในการอักเสบ (subacute thyroiditis) ซึ่งไม่ใช่กรณีนี้''',
            pearl="Simple goiter: TFT ปกติ Ab ลบ → ติดตาม", topic="Simple goiter",
            ref=[f"{D} หน้า 241–242"], nl=["2.3.4(3)"]),
        mcq("ENDO-04-02-4",
            "A 30-year-old woman planning pregnancy has TSH 6.8 mU/L (0.4–4.0) and normal FT4 on two occasions; anti-TPO is positive. She has no symptoms. What is the most appropriate management?",
            "Start levothyroxine aiming for TSH below 2.5 mU/L",
            ["No treatment; repeat TFT in 1 year", "Start methimazole", "Iodine supplementation alone", "Thyroid ultrasound and fine-needle aspiration"],
            explain='''Subclinical hypothyroidism ในผู้ที่ **วางแผนตั้งครรภ์** และ anti-TPO บวก → **ให้ LT4** เพราะ hypothyroid เล็กน้อยสัมพันธ์กับแท้ง/ผลต่อพัฒนาการสมองทารก เป้า TSH < 2.5 ก่อนตั้งครรภ์ (เสริม)
- ติดตามเฉย ๆ เหมาะกับผู้ที่ไม่ได้วางแผนตั้งครรภ์และ TSH < 10
- Methimazole ใช้รักษา hyperthyroidism
- Iodine อย่างเดียวไม่แก้ Hashimoto (เกินอาจทำให้แย่ลง)
- U/S/FNA ไม่จำเป็นเมื่อไม่มี nodule''',
            pearl="Subclinical hypo + วางแผนตั้งครรภ์ → LT4", topic="Subclinical hypo treatment",
            ref=[f"{D} หน้า 202–203"], nl=["2.3.4(4)", "B11.4(2)"]),
    ])

# ---------------------------------------------------------------- 04-03 Myxedema coma
S3 = sec("endo-04-03", "Myxedema coma",
    "Severe hypothyroidism ที่ซึม/โคม่า + hypothermia, bradycardia, hypoventilation, Na ต่ำ, glucose ต่ำ · มักมี adrenal insufficiency ร่วม → hydrocortisone ก่อน/พร้อม IV LT4 · ABC, warming แบบ passive", minutes=7,
    source=f"{D} หน้า 214–220", nl=["2.3.4(4)", "2.2.36", "B11.4(2)"],
    md='''
### นิยามและตัวกระตุ้น (สไลด์หน้า 214)
- **Severe hypothyroidism → life-threatening** (อัตราตาย 25–60% — เสริม) พบบ่อยในผู้สูงอายุ หน้าหนาว
- Precipitating factors: **ติดเชื้อ, ป่วยหนัก, trauma** · **ยา: sedatives, anesthetics, lithium** (opioid — เสริม) · **ขาดยา LT4**

### อาการ
- **ซึม/โคม่า (AOC)** · **hypothermia (↓BT)** · myxedema (บวมทั่วตัว หนังตาตก periorbital edema **ลิ้นโต**)
- **↓RR (hypoventilation, CO2 คั่ง)** · **↓BP** · **↓PR**
- Lab: **↓Glucose**, **↓Na**, **↓cortisol** · CK สูง (เสริม)
- **มักมี concomitant adrenal insufficiency!**

### การรักษา (สไลด์หน้า 216)
1. **Initial (ABC)**: **ใส่ ETT ถ้า respiratory failure** · **IV fluid resuscitation** (ระวัง hypotonic เพราะ Na ต่ำ — เสริม)
2. **Specific**: **High-dose LT4 (IV/oral) + hydrocortisone**
   - LT4 IV **200–400 mcg loading** แล้ว 50–100 mcg/วัน (ลดในผู้สูงอายุ/โรคหัวใจ) (เสริม)
   - **Hydrocortisone 100 mg IV q8h** — **ให้ก่อนหรือพร้อม LT4** เพราะ (1) มักมี adrenal insufficiency ร่วม (2) **thyroxine เพิ่ม cortisol clearance** → precipitate adrenal crisis
3. **Supportive**: **warming** (passive — ห่มผ้า; active external warming ทำให้ vasodilate → shock — เสริม) · **แก้ hypoglycemia**
4. **รักษา precipitating cause** (หา infection, ทบทวนยา)

> โจทย์ "นอกจากให้ thyroxine แล้ว ควรให้อะไร" → **Hydrocortisone** (สไลด์แก้เฉลยเป็นข้อนี้) · ABC, IV fluid, glucose เป็น initial/supportive · **Atropine/dopamine ไม่ใช่การรักษาหลัก** — bradycardia/hypotension ดีขึ้นเมื่อได้ฮอร์โมน
''',
    pearls=[
        "Myxedema coma: ซึม + hypothermia + bradycardia + hypoventilation + Na/glucose ต่ำ",
        "Trigger: ติดเชื้อ, sedative/anesthetic, หยุด LT4",
        "Hydrocortisone ก่อน/พร้อม IV LT4 (AI ร่วม + LT4 เร่ง cortisol clearance)",
        "ABC → IV fluid → LT4 + HC → passive warming → แก้ glucose → หา trigger",
    ],
    items=[
        mcq("ENDO-04-03-1",
            "A 60-year-old woman has progressive alteration of consciousness for 3 days and constipation. BT 36.8°C, RR 10/min, PR 52/min, BP 90/60 mmHg. She has a puffy face, slow reflex relaxation, thinning hair, goiter and non-pitting edema. Glucose 70 mg/dL, Na 128, K 4.0 mmol/L; FT4 low, TSH 150 mU/L. Besides thyroxine, what is the most appropriate management?",
            "IV hydrocortisone",
            ["0.9% NaCl loading only", "IV glucose bolus", "IV atropine", "Dopamine infusion"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (สไลด์แก้เฉลยเป็น hydrocortisone)",
            explain='''**Myxedema coma** มัก **มี adrenal insufficiency ร่วม** และ **thyroxine เพิ่ม cortisol clearance** → ต้องให้ **IV hydrocortisone ร่วมกับ LT4** (สไลด์แก้เฉลยว่า most appropriate คือ hydrocortisone + LT4)
- NSS เป็นส่วนของ initial resuscitation แต่ไม่ใช่การรักษาจำเพาะที่ขาดไม่ได้
- Glucose 70 ยังไม่ต่ำ แก้เมื่อ hypoglycemia (เป็น supportive)
- Atropine ไม่จำเป็น — bradycardia ดีขึ้นเมื่อได้ฮอร์โมน
- Dopamine ใช้เมื่อ shock ไม่ตอบสนองต่อ fluid และ hydrocortisone''',
            pearl="Myxedema coma: LT4 + hydrocortisone เสมอ", topic="Hydrocortisone",
            ref=[f"{D} หน้า 216, 219–220"], nl=["2.3.4(4)", "B11.4(3)"]),
        mcq("ENDO-04-03-2",
            "A drowsy patient has BT 36°C, BP 90/60 mmHg, PR 52/min, RR 12/min, a puffy face, no neck stiffness and slow-relaxing reflexes. Na 130, K 4, Cl 100, HCO3 24 mmol/L; BUN 20, Cr 1.1 mg/dL. FT4 0.4 ng/dL (0.9–1.9), TSH 150 mU/L. After securing the airway and starting IV fluid, which drug should be given first or together with thyroid hormone?",
            "Hydrocortisone",
            ["Atropine", "Dopamine", "Liothyronine alone without other hormones", "Furosemide"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Myxedema coma: หลัง ABC/IV fluid → **hydrocortisone ก่อนหรือพร้อม levothyroxine** เพื่อป้องกัน adrenal crisis (ถ้ามี AI ร่วม การให้ thyroxine อย่างเดียวจะเพิ่มการเผาผลาญ cortisol)
- Atropine และ dopamine แก้ตัวเลขชีพจร/BP ชั่วคราว ไม่ได้แก้สาเหตุ
- T3 อย่างเดียวโดยไม่ให้ steroid มีความเสี่ยงเดียวกันและเสี่ยงหัวใจ
- Furosemide ทำให้ขาดน้ำและความดันต่ำลง''',
            pearl="ให้ steroid ก่อน/พร้อม thyroid hormone ใน myxedema coma", topic="Order of therapy",
            ref=[f"{D} หน้า 216–218"], nl=["2.3.4(4)"]),
        mcq("ENDO-04-03-3",
            "A 78-year-old woman with long-standing untreated hypothyroidism was given diazepam for insomnia during admission for pneumonia. She becomes stuporous with BT 34.5°C, RR 8/min, PaCO2 68 mmHg, PR 48/min. What is the most appropriate immediate step?",
            "Endotracheal intubation and mechanical ventilation",
            ["Active external rewarming with a heating blanket", "Oral levothyroxine 50 mcg and observe", "Flumazenil and discharge planning", "Hypotonic fluid to correct dehydration"],
            explain='''Myxedema coma ที่มี **hypoventilation (RR 8, PaCO2 68)** → **ABC ก่อน: ใส่ ETT** แล้วจึงให้ IV LT4 + hydrocortisone และรักษา pneumonia (trigger: ติดเชื้อ + benzodiazepine)
- Active external rewarming ทำให้หลอดเลือดส่วนปลายขยาย → ความดันตก ใช้ passive warming
- LT4 กินขนาดต่ำดูดซึมไม่แน่นอนในภาวะนี้และช้าเกินไป
- Flumazenil อาจกระตุ้นชักและไม่ได้แก้ hypothyroid coma
- Hypotonic fluid ทำให้ Na ซึ่งต่ำอยู่แล้วต่ำลง''',
            pearl="Myxedema coma + CO2 คั่ง → intubate ก่อน", topic="ABC",
            ref=[f"{D} หน้า 214, 216"], nl=["2.3.4(4)", "2.2.9"]),
    ])

# ---------------------------------------------------------------- 04-04 Thyroid nodule
F_NOD = fig("endo-04-04-f1", "Approach to thyroid nodule", '''<svg viewBox="0 0 740 400">
 <defs><marker id="endo-04-04-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="240" y="10" width="260" height="44" rx="10" class="acsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">Thyroid nodule</text>
 <text x="370" y="46" text-anchor="middle" class="t3">TSH + thyroid U/S ทุกราย</text>
 <path d="M320 54L190 88" class="ln" marker-end="url(#endo-04-04-a)"/>
 <path d="M420 54L550 88" class="ln" marker-end="url(#endo-04-04-a)"/>
 <rect x="80" y="90" width="220" height="40" rx="10" class="c2"/>
 <text x="190" y="115" text-anchor="middle" class="tw">TSH ต่ำ</text>
 <rect x="440" y="90" width="220" height="40" rx="10" class="c1"/>
 <text x="550" y="115" text-anchor="middle" class="tw">TSH ปกติ / สูง</text>
 <path d="M190 130V156" class="ln" marker-end="url(#endo-04-04-a)"/>
 <rect x="80" y="158" width="220" height="40" rx="10" class="box"/>
 <text x="190" y="183" text-anchor="middle" class="tb">Thyroid scan</text>
 <path d="M140 198L90 232" class="ln" marker-end="url(#endo-04-04-a)"/>
 <path d="M240 198L290 232" class="ln" marker-end="url(#endo-04-04-a)"/>
 <rect x="10" y="234" width="170" height="90" rx="10" class="oksoft"/>
 <text x="95" y="256" text-anchor="middle" class="tb">Hot nodule</text>
 <text x="95" y="276" text-anchor="middle" class="t3">CA โอกาสน้อย</text>
 <text x="95" y="296" text-anchor="middle" class="t2">รักษา hyperthyroid</text>
 <text x="95" y="314" text-anchor="middle" class="t3">ไม่ต้อง FNA</text>
 <rect x="200" y="234" width="190" height="80" rx="10" class="misssoft"/>
 <text x="295" y="256" text-anchor="middle" class="tb">Cold / warm nodule</text>
 <text x="295" y="276" text-anchor="middle" class="t3">CA 5–15%</text>
 <text x="295" y="296" text-anchor="middle" class="t2">→ ประเมิน U/S/FNA</text>
 <path d="M550 130V156" class="ln" marker-end="url(#endo-04-04-a)"/>
 <rect x="420" y="158" width="260" height="40" rx="10" class="box"/>
 <text x="550" y="183" text-anchor="middle" class="tb">U/S: malignancy features?</text>
 <path d="M390 274H418" class="ln" marker-end="url(#endo-04-04-a)"/>
 <path d="M550 198V232" class="ln" marker-end="url(#endo-04-04-a)"/>
 <rect x="420" y="234" width="260" height="104" rx="10" class="badsoft"/>
 <text x="432" y="256" class="tb">FNA ตามขนาด + ความเสี่ยง</text>
 <text x="432" y="276" class="t2">microcalcification · hypoechoic</text>
 <text x="432" y="294" class="t2">irregular margin · solid</text>
 <text x="432" y="312" class="t2">taller-than-wide</text>
 <text x="432" y="330" class="t3">high suspicion ≥ 1 cm → FNA</text>
 <rect x="10" y="350" width="720" height="42" rx="10" class="sunk"/>
 <text x="22" y="376" class="t2">Red flags: โตเร็ว · เสียงแหบ · กลืน/หายใจลำบาก · ก้อนแข็งติดแน่น · LN โต · เคยฉายแสงคอ · FHx thyroid CA</text>
</svg>''', "เริ่มด้วย TSH เสมอ — TSH ต่ำไปทาง scan (hot nodule แทบไม่เป็นมะเร็ง) ส่วน TSH ปกติ/สูงไปทาง U/S แล้วตัดสิน FNA ตามลักษณะและขนาด")

S4 = sec("endo-04-04", "Thyroid nodule: TSH → scan หรือ U/S → FNA",
    "95% benign · Ix แรก TSH + U/S · TSH ต่ำ → thyroid scan (hot = CA น้อย) · TSH ปกติ/สูง → U/S หา malignancy features → FNA · MNG + hyperthyroid → scan", minutes=9,
    source=f"{D} หน้า 221–236", nl=["B11.2.4-3(1)", "B11.2.4-3(2)", "2.3.4(3)"],
    md='''
### ภาพรวม (สไลด์หน้า 221)
- Nodule ที่คลำได้หรือพบจาก imaging
- **Benign 95%**: thyroid adenoma (รวม toxic adenoma, toxic MNG), **thyroid cyst** · **Malignant 5%**
- **Risk**: **เคยฉายแสงศีรษะ/คอ**, **ประวัติครอบครัวเป็นมะเร็งไทรอยด์** (MEN2 — เสริม)
- **Red flags**: **โตเร็ว**, **เสียงแหบ**, กลืนลำบาก, หายใจลำบาก, ก้อน **แข็ง/ติดแน่น**, **cervical lymphadenopathy**

### Approach (สไลด์หน้า 221–223)

[[fig:endo-04-04-f1]]

- **Ix แรก: TSH และ thyroid U/S**
- **TSH ต่ำ → thyroid scan**
  - **Only hot nodule** → toxic adenoma/toxic MNG → **รักษา hyperthyroidism** (RAI/ผ่าตัด) — hot nodule **โอกาสมะเร็งน้อย** ไม่ต้อง FNA
  - **Hot + cold nodule** (เช่น Graves with cold nodule, toxic MNG with cold nodule) → cold nodule ต้องประเมินต่อ (U/S ± FNA) · **cold nodule โอกาส CA 5–15%**
  - Nodule กับ TSH ต่ำ **ไม่จำเป็นต้องเป็น toxic adenoma เสมอ** — อาจเป็น Graves ที่มี cold nodule
- **TSH ปกติ/สูง → U/S ดู malignancy features → FNA ตามเกณฑ์ขนาด** (ขึ้นกับความเสี่ยงจาก U/S)

### U/S malignancy features (สไลด์หน้า 224)
- **Microcalcification** · **Hypoechogenicity** · **Irregular margin** · **Solid** · **Taller than wide**

### เกณฑ์ FNA (สไลด์หน้า 225 เป็นภาพ — ตาม ATA 2015) (เสริม)

| U/S pattern | ทำ FNA เมื่อขนาด |
|---|---|
| **High suspicion** (solid hypoechoic + feature ข้างบน ≥ 1) | **≥ 1 cm** |
| Intermediate (solid hypoechoic เรียบ) | ≥ 1 cm |
| Low suspicion (isoechoic/hyperechoic solid, partially cystic มี solid eccentric) | ≥ 1.5 cm |
| Very low (spongiform, partially cystic) | ≥ 2 cm หรือติดตาม |
| Pure cyst | ไม่ต้อง FNA |

### ผล FNA — Bethesda (สไลด์หน้า 226 เป็นภาพ) (เสริม)

| Bethesda | ความหมาย | จัดการ |
|---|---|---|
| I | Nondiagnostic | **ทำ FNA ซ้ำ** (U/S-guided) |
| II | **Benign** | ติดตาม U/S |
| III | AUS/FLUS | FNA ซ้ำ/molecular test/lobectomy |
| IV | Follicular neoplasm | **Lobectomy** (FNA แยก follicular adenoma กับ carcinoma ไม่ได้) |
| V | Suspicious for malignancy | ผ่าตัด |
| VI | **Malignant** (papillary บ่อยสุด) | **Thyroidectomy** |

> Nodule + **hyperthyroid** → **thyroid scan** ไม่ใช่ FNA ก่อน · Nodule + **TSH สูง/ปกติ** → **U/S** · goiter ไม่มี nodule → TFT + antibody
''',
    figs=[F_NOD],
    pearls=[
        "Nodule ทุกก้อน → TSH + U/S ก่อน",
        "TSH ต่ำ → thyroid scan · hot nodule แทบไม่เป็นมะเร็ง ไม่ต้อง FNA",
        "Cold nodule CA 5–15% · Graves อาจมี cold nodule ได้",
        "U/S สงสัยมะเร็ง: microcalcification, hypoechoic, irregular, solid, taller-than-wide",
        "Bethesda IV (follicular) → lobectomy · VI → thyroidectomy",
    ],
    items=[
        mcq("ENDO-04-04-1",
            "A 26-year-old Thai woman has had a neck mass for 3 years and now has fatigue, palpitations and 3 kg weight loss. PR 98/min, fine moist skin, a palpable thyroid nodule. FT4 3.5 ng/dL (0.7–1.4), T3 314 ng/dL (60–180), TSH <0.01 mU/L. What should be done next to confirm the diagnosis?",
            "Thyroid scan",
            ["Thyroid antibody", "CT neck", "MRI neck", "Fine-needle aspiration"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Nodule + **TSH ต่ำ (hyperthyroid)** → **thyroid scan** เพื่อดูว่าก้อนเป็น **hot nodule (toxic adenoma)** หรือมี cold nodule ร่วม
- Thyroid antibody ช่วยแยก Graves/Hashimoto แต่ไม่ได้บอกว่าก้อนทำงานหรือไม่
- CT/MRI ไม่ได้ใช้ประเมินการทำงานของ nodule
- FNA ไม่ทำใน hot nodule (โอกาสมะเร็งต่ำ และ cytology ของ hyperfunctioning nodule แปลผลยาก)''',
            pearl="Nodule + TSH ต่ำ → thyroid scan", topic="Hyperfunctioning nodule",
            ref=[f"{D} หน้า 221–222, 227–228"], nl=["B11.2.4-3(1)", "2.3.4(9)"]),
        mcq("ENDO-04-04-2",
            "A 60-year-old man has a right thyroid lobe mass, fatigue and 5 kg weight loss. BP 160/110 mmHg, PR 90/min. FT4 normal, FT3 at the upper limit of normal, TSH <0.001 mU/L. What is the most appropriate investigation?",
            "Thyroid scan",
            ["Thyroid ultrasound with immediate FNA", "Serum iodine", "Thyroid antibodies", "CT chest"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Nodule + **TSH ถูกกด** (subclinical/T3 toxicosis) → ต้องรู้ว่าก้อนเป็น **autonomous (hot) nodule** หรือไม่ด้วย **thyroid scan**
- U/S ทำได้แต่การตัดสิน FNA ต้องรอผล scan — hot nodule ไม่ต้อง FNA
- Serum iodine ไม่มีบทบาท
- Antibody ไม่ได้บอกการทำงานของก้อน
- CT chest ไม่ใช่การตรวจขั้นแรกของ thyroid nodule''',
            pearl="TSH ต่ำ แม้ FT4 ปกติ + nodule → scan", topic="Scan indication",
            ref=[f"{D} หน้า 229–230"], nl=["B11.2.4-3(1)"]),
        mcq("ENDO-04-04-3",
            "A 68-year-old woman has had a neck mass for 10 years and now has fatigue, anorexia and 8 kg weight loss in 3 months. BP 160/80 mmHg, HR 112/min (irregularly irregular). The thyroid is enlarged four-fold with multiple nodules. FT4 2.4 ng/dL (0.7–1.4), T3 250 ng/dL, TSH 0.01 mU/L. What is the most appropriate next investigation?",
            "Thyroid scan",
            ["FNA of the largest nodule", "TSH receptor antibody", "CT neck with contrast", "Serum thyroglobulin"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Multinodular goiter + hyperthyroid + **TSH ต่ำ** → **thyroid scan**: hot nodule อย่างเดียว = **toxic MNG** · hot + cold = toxic MNG with cold nodule (cold ต้องประเมินต่อ)
- FNA ก่อน scan ไม่เหมาะ เพราะต้องรู้ก่อนว่าก้อนไหน cold
- TRAb ใช้ยืนยัน Graves ซึ่งต่อมเป็น diffuse ไม่ใช่หลายก้อน
- CT contrast มี iodine → อาจกระตุ้น thyrotoxicosis/storm ใน toxic MNG
- Thyroglobulin ใช้ติดตามมะเร็งหลังผ่าตัด/แยก exogenous''',
            pearl="MNG + TSH ต่ำ → scan", topic="Toxic MNG",
            ref=[f"{D} หน้า 231–232"], nl=["B11.2.4-3(1)", "2.3.4(9)"]),
        mcq("ENDO-04-04-4",
            "A 48-year-old woman with a 10-year history of goiter notices a new thyroid nodule for 2 months. She has no hoarseness or compressive symptoms. The gland is diffusely enlarged with a 2-cm hard nodule. Thyroid function tests are normal. What is the most appropriate next investigation?",
            "Thyroid ultrasonography",
            ["Thyroid antibody", "Thyroid scan", "CT neck", "Excisional biopsy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Nodule ที่ **TSH ปกติ** → **U/S** ประเมิน malignancy features และกำหนดว่าต้อง FNA หรือไม่ (ก้อนแข็ง 2 cm มีแนวโน้มต้อง FNA แต่ U/S ก่อนเพื่อเลือกก้อน/นำเข็ม)
- Antibody ไม่ได้ประเมินความเสี่ยงมะเร็ง
- Thyroid scan ใช้เมื่อ TSH ต่ำ
- CT neck ไม่ใช่การตรวจหลักของ nodule
- Excisional biopsy ไม่ใช่ขั้นแรก (FNA ก่อน)

(บางตำราตอบ FNA ได้ในก้อนแข็ง ≥ 1 cm — แต่แนวทางปัจจุบันให้ U/S ทุกรายก่อนตัดสิน FNA)''',
            pearl="Nodule + TSH ปกติ → U/S ก่อน FNA", topic="U/S first",
            ref=[f"{D} หน้า 221, 233–234"], nl=["B11.2.4-3(1)", "B11.2.4-3(2)"]),
        mcq("ENDO-04-04-5",
            "A patient presents with a thyroid nodule. FT4 is low and TSH is high. What is the most appropriate next investigation for the nodule?",
            "Thyroid ultrasound",
            ["Thyroid scan", "FNA without imaging", "Open biopsy", "Serum calcitonin"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Nodule กับ **TSH สูง** (hypothyroid, มักเป็น Hashimoto) → ไม่มีโอกาสเป็น hot nodule → **U/S** ดู malignancy features แล้วตัดสิน FNA
- Thyroid scan ใช้เฉพาะเมื่อ TSH ต่ำ
- FNA โดยไม่ทำ U/S ไม่แนะนำ ควรมี U/S ประเมินก่อนและนำเข็ม
- Open biopsy ไม่ใช่ขั้นตอนแรก
- Calcitonin ไม่ส่งตรวจ routine (สงสัย medullary CA จากประวัติครอบครัว/MEN2)''',
            pearl="Nodule + TSH สูง → U/S", topic="Nodule with hypothyroidism",
            ref=[f"{D} หน้า 235–236"], nl=["B11.2.4-3(1)"]),
        mcq("ENDO-04-04-6",
            "A 42-year-old woman has a 1.6-cm solid hypoechoic thyroid nodule with microcalcifications and a taller-than-wide shape on ultrasound. TSH is normal. FNA is reported as Bethesda VI (papillary carcinoma). What is the most appropriate management?",
            "Thyroidectomy",
            ["Repeat FNA in 6 months", "Radioactive iodine alone without surgery", "Levothyroxine suppression and observation", "Thyroid scan"],
            explain='''**Bethesda VI = malignant** (papillary carcinoma) → **ผ่าตัด (thyroidectomy/lobectomy ตามขนาดและความเสี่ยง)** แล้วพิจารณา RAI ตามความเสี่ยงหลังผ่าตัด
- FNA ซ้ำใช้กับ Bethesda I (nondiagnostic) หรือ III
- RAI ใช้ **หลัง** total thyroidectomy เพื่อทำลายเนื้อเยื่อที่เหลือ ไม่ใช่แทนการผ่าตัด
- LT4 suppression อย่างเดียวไม่ใช่การรักษามะเร็ง
- Thyroid scan ไม่มีบทบาทเมื่อ TSH ปกติและรู้ผลชิ้นเนื้อแล้ว''',
            pearl="Bethesda VI → ผ่าตัด", topic="FNA result",
            ref=[f"{D} หน้า 224–226"], nl=["B11.2.4-3(2)"]),
    ])

LECTURE = lecture("04", "Hypothyroidism, myxedema coma & thyroid nodule", "hypothyroid · subclinical · goiter · myxedema coma · nodule",
    objectives=[
        "วินิจฉัย hypothyroidism แยก primary/secondary และหาสาเหตุได้",
        "สั่ง levothyroxine ได้ถูกขนาด ถูกวิธีกิน และรู้ยาที่รบกวนการดูดซึม",
        "ตัดสินใจรักษา subclinical hypothyroidism และ work up goiter ได้",
        "รักษา myxedema coma ได้ครบ รวมถึงการให้ hydrocortisone",
        "ไล่ approach thyroid nodule จาก TSH → scan/U/S → FNA ได้",
    ],
    sections=[S1, S2, S3, S4])
