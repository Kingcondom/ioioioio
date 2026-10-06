from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Nephro"

# ---------------------------------------------------------------- 05-01 Osm & polyuria
F_POLY = fig("nephro-05-01-f1", "Approach to polyuria ด้วย urine osmolality", '''<svg viewBox="0 0 740 380">
 <defs><marker id="nephro-05-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="10" width="280" height="48" rx="10" class="acsoft"/>
 <text x="370" y="31" text-anchor="middle" class="tb">ปัสสาวะบ่อย</text>
 <text x="370" y="49" text-anchor="middle" class="t3">R/O frequency: UTI, BPH, overactive bladder</text>
 <path d="M370 58V78" class="ln" marker-end="url(#nephro-05-01-a)"/>
 <rect x="230" y="80" width="280" height="40" rx="10" class="box"/>
 <text x="370" y="105" text-anchor="middle" class="tb">Polyuria = UO &gt; 3 L/day → Urine Osm</text>
 <path d="M290 120L130 158" class="ln" marker-end="url(#nephro-05-01-a)"/>
 <path d="M370 120V158" class="ln" marker-end="url(#nephro-05-01-a)"/>
 <path d="M450 120L610 158" class="ln" marker-end="url(#nephro-05-01-a)"/>
 <rect x="10" y="160" width="230" height="44" rx="10" class="c1"/>
 <text x="125" y="181" text-anchor="middle" class="tw">Uosm &lt; 150</text>
 <text x="125" y="197" text-anchor="middle" class="tw">Water diuresis</text>
 <rect x="255" y="160" width="230" height="44" rx="10" class="miss"/>
 <text x="370" y="181" text-anchor="middle" class="tw">Uosm 150–300</text>
 <text x="370" y="197" text-anchor="middle" class="tw">Mixed diuresis</text>
 <rect x="500" y="160" width="230" height="44" rx="10" class="c2"/>
 <text x="615" y="181" text-anchor="middle" class="tw">Uosm &gt; 300</text>
 <text x="615" y="197" text-anchor="middle" class="tw">Solute diuresis</text>
 <rect x="10" y="214" width="230" height="156" rx="10" class="c1soft"/>
 <text x="22" y="238" class="tb">Primary polydipsia</text>
 <text x="22" y="258" class="tb">Diabetes insipidus</text>
 <text x="22" y="276" class="t3">central / nephrogenic</text>
 <text x="22" y="304" class="t2">→ Water deprivation test</text>
 <text x="22" y="326" class="t3">ขาดน้ำแล้ว Uosm ขึ้นได้ = polydipsia</text>
 <text x="22" y="344" class="t3">ไม่ขึ้น = DI → ให้ DDAVP แยก</text>
 <text x="22" y="362" class="t3">central (ขึ้น) / nephrogenic (ไม่ขึ้น)</text>
 <rect x="255" y="214" width="230" height="156" rx="10" class="misssoft"/>
 <text x="267" y="238" class="t2">Partial DI</text>
 <text x="267" y="260" class="t2">CKD</text>
 <text x="267" y="282" class="t2">ได้ NSS + water พร้อมกัน</text>
 <text x="267" y="304" class="t2">Post-obstructive diuresis</text>
 <rect x="500" y="214" width="230" height="156" rx="10" class="c2soft"/>
 <text x="512" y="238" class="tb">Non-electrolyte</text>
 <text x="512" y="258" class="t2">Glucose (DM)</text>
 <text x="512" y="278" class="t2">Urea, mannitol</text>
 <text x="512" y="306" class="tb">Electrolyte</text>
 <text x="512" y="326" class="t2">NSS, diuretic</text>
 <text x="512" y="346" class="t2">HCO3, ketone</text>
</svg>''', "เริ่มจากยืนยันว่าปัสสาวะมากจริง (> 3 L/วัน) ไม่ใช่แค่ถ่ายบ่อย แล้วใช้ Uosm แบ่งเป็นสามกลุ่มตามสไลด์")

S1 = sec("nephro-05-01", "Serum osmolality, polyuria & diabetes insipidus",
    "Sosm ปกติ 285–295 · polyuria >3 L/d · Uosm <150 water diuresis (DI/polydipsia) · >300 solute diuresis", minutes=8,
    source=f"{D} หน้า 157–166", nl=["2.1.42", "B11.2.5-3(6)", "B9.3(3)"],
    md='''
### Serum osmolality

- ปกติ **285–295 mOsm/kg**
- Calculated Sosm = 2 × Na + glucose/18 + BUN/2.8 (เสริม)
- น้ำในร่างกายถูกควบคุมด้วย **ADH**: Sosm ↑ (หรือ ECV ลดมาก) → ADH ↑ → ดูดน้ำกลับที่ collecting duct → Uosm ↑ · Sosm ↓ → ADH ↓ → Uosm ↓ (ปัสสาวะเจือจาง)

### Polyuria

- นิยาม: **urine output > 3 L/day**
- ต้อง **แยก frequency ก่อน** (UTI, BPH, overactive bladder) — ปัสสาวะบ่อยแต่ปริมาณรวมไม่มาก → ใช้ **voiding diary** (บันทึกเวลาและปริมาณ)

[[fig:nephro-05-01-f1]]

### Diabetes insipidus (DI)

| | Central DI | Nephrogenic DI | Primary polydipsia |
|---|---|---|---|
| ปัญหา | สร้าง/หลั่ง ADH ไม่ได้ | ไตไม่ตอบสนอง ADH | ดื่มน้ำมากเกิน |
| สาเหตุ | Head injury, ผ่าตัด/ฉายแสงบริเวณ pituitary–hypothalamus, tumor | **Lithium**, hypercalcemia, hypokalemia, สมุนไพร/ยาที่ต้านฤทธิ์ ADH | จิตเวช |
| Serum Na/Osm | ปกติสูง–สูง | ปกติสูง–สูง | **ต่ำ** |
| Uosm | ต่ำ (< Sosm) | ต่ำ | ต่ำมาก |
| Water deprivation | Uosm ไม่ขึ้น | Uosm ไม่ขึ้น | Uosm ขึ้น |
| ให้ desmopressin | **Uosm ขึ้น** | ไม่ขึ้น | — |
| รักษา | **Desmopressin (DDAVP)** | หยุดยาสาเหตุ, thiazide, low-solute diet | ลดการดื่มน้ำ |

(ตาราง DI เป็นส่วนเสริม — สไลด์ water deprivation test เป็นภาพ)

> Uosm < Sosm ทั้งที่ Sosm สูง = ADH ไม่ทำงาน (DI) · ผู้ป่วยหลังฉายแสง nasopharynx/ผ่าตัด pituitary → central DI
''',
    figs=[F_POLY],
    pearls=[
        "Sosm ปกติ 285–295 · polyuria = UO >3 L/day",
        "ปัสสาวะบ่อย UA ปกติ → voiding diary แยก frequency กับ polyuria",
        "Uosm <150 = water diuresis (DI, polydipsia) · >300 = solute diuresis (glucose, mannitol, NSS)",
        "Sosm สูง + Uosm ต่ำ = DI · ตอบสนอง DDAVP = central",
        "Lithium = nephrogenic DI ที่ออกสอบบ่อย (เสริม)",
    ],
    items=[
        mcq("NEPHRO-05-01-1",
            "A 40-year-old woman complains of frequent urination at all times of day. Physical examination is unremarkable. Urinalysis: specific gravity 1.013, glucose negative, protein negative, WBC 0–1/HPF, RBC 0–1/HPF. What is the most appropriate investigation?",
            "Voiding diary",
            ["Serum ADH level", "Urodynamic study", "24-hour urine protein", "24-hour pad test"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ขั้นแรกคือ **แยก frequency กับ polyuria** ด้วย **voiding diary** (บันทึกเวลาและปริมาณแต่ละครั้ง/24 ชม.) ถ้าปริมาณรวม > 3 L/วัน จึงเป็น polyuria แล้วค่อยวัด Uosm
- Serum ADH ไม่ใช้เป็นการตรวจแรก แปลผลยากและไม่ได้แยก frequency
- Urodynamic study ใช้เมื่อสงสัยปัญหากระเพาะปัสสาวะหลังเก็บข้อมูลพื้นฐานแล้ว
- 24-hour urine protein ไม่เกี่ยว เพราะ protein ลบ
- Pad test ใช้วัดปัสสาวะเล็ด (incontinence) ไม่ใช่ปัสสาวะบ่อย''',
            pearl="ปัสสาวะบ่อย → voiding diary ก่อน", topic="Frequency vs polyuria",
            ref=[f"{D} หน้า 159, 161–162"], nl=["2.1.41", "2.1.42"]),
        mcq("NEPHRO-05-01-2",
            "A 16-year-old patient develops polyuria of 8 L/day after radiation therapy for nasopharyngeal carcinoma. Urine osmolality is 200 mOsm/kg and serum osmolality is 300 mOsm/kg. What is the most likely diagnosis?",
            "Central diabetes insipidus",
            ["Adrenal insufficiency", "Cerebral salt wasting", "SIADH", "Primary polydipsia"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ฉายแสงบริเวณ nasopharynx กระทบ hypothalamus–pituitary → สร้าง ADH ไม่ได้ = **central DI**: ปัสสาวะมาก Uosm (200) ต่ำกว่า Sosm (300) ทั้งที่ Sosm สูง
- Adrenal insufficiency, cerebral salt wasting และ SIADH ทำให้ **hyponatremia และ Sosm ต่ำ** (สไลด์เฉลยไว้ว่าตัวเลือกเหล่านี้ = HypoNa, ↓SerumOsm)
- Primary polydipsia ทำให้ Sosm ต่ำ–ปกติต่ำ ไม่ใช่ 300''',
            pearl="ฉายแสง/ผ่าตัด pituitary + Sosm สูง + Uosm ต่ำ = central DI", topic="Central DI",
            ref=[f"{D} หน้า 163–164"], nl=["B11.2.5-3(6)"]),
        mcq("NEPHRO-05-01-3",
            "A 60-year-old woman presents with polyuria after taking a herbal medicine for several weeks. Urine osmolality is 100 mOsm/kg. Serum sodium is 146 mEq/L. Which mechanism of the herbal medicine best explains her findings?",
            "Inhibition of ADH action at the collecting duct",
            ["Inhibition of renin secretion", "Inhibition of NaCl reabsorption in the distal tubule", "Osmotic diuresis from glucose", "Stimulation of ADH release"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Uosm 100 (< 150) = **water diuresis** ร่วมกับ Na ค่อนสูง → ไตขับน้ำเปล่าออกเพราะ ADH ใช้ไม่ได้ = กลไกแบบ **nephrogenic DI (ยับยั้งการออกฤทธิ์ของ ADH)**
- ยับยั้ง renin ลด aldosterone ไม่ทำให้ปัสสาวะเจือจางขนาดนี้
- ยับยั้งการดูด NaCl (แบบ diuretic) ทำให้เป็น **solute diuresis** Uosm > 300
- Glucose ก็เป็น solute diuresis เช่นกัน
- กระตุ้นการหลั่ง ADH จะทำให้ปัสสาวะเข้มข้นและ Na ต่ำ''',
            pearl="Uosm <150 = water diuresis (ADH ไม่ทำงาน)", topic="Nephrogenic DI",
            ref=[f"{D} หน้า 159, 165–166"], nl=["B11.2.5-3(6)", "B9.1.2(5)"]),
        mcq("NEPHRO-05-01-4",
            "A 34-year-old man has polyuria of 6 L/day. Serum Na 144 mEq/L, serum osmolality 296 mOsm/kg, urine osmolality 110 mOsm/kg. After 8 hours of water deprivation, urine osmolality remains 120 mOsm/kg. After subcutaneous desmopressin, urine osmolality rises to 420 mOsm/kg. What is the most appropriate long-term treatment?",
            "Desmopressin",
            ["Hydrochlorothiazide", "Fluid restriction alone", "Demeclocycline", "Tolvaptan"],
            explain='''อดน้ำแล้ว Uosm ไม่ขึ้น (ไม่มี ADH) แต่ให้ desmopressin แล้ว Uosm ขึ้นมากกว่า 50% = **central DI** รักษาด้วย **desmopressin (DDAVP)** (เสริม)
- Thiazide ใช้ใน nephrogenic DI ซึ่งจะไม่ตอบสนองต่อ desmopressin
- จำกัดน้ำเป็นการรักษา primary polydipsia — ใน DI จะทำให้ hypernatremia
- Demeclocycline และ tolvaptan ต้านฤทธิ์ ADH ใช้ใน SIADH ซึ่งจะทำให้รายนี้แย่ลง''',
            pearl="Water deprivation ไม่ขึ้น + DDAVP ขึ้น = central DI → DDAVP", topic="Water deprivation test",
            ref=[f"{D} หน้า 159–160"], nl=["B11.2.5-3(6)"]),
    ])

# ---------------------------------------------------------------- 05-02 Hyponatremia approach + SIADH
F_HYPO = fig("nephro-05-02-f1", "Approach to hyponatremia (ตามสไลด์)", '''<svg viewBox="0 0 740 420">
 <defs><marker id="nephro-05-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="270" y="10" width="200" height="38" rx="10" class="acsoft"/>
 <text x="370" y="34" text-anchor="middle" class="tb">Na &lt; 135 → Serum Osm</text>
 <path d="M320 48L170 80" class="ln" marker-end="url(#nephro-05-02-a)"/>
 <path d="M420 48L560 80" class="ln" marker-end="url(#nephro-05-02-a)"/>
 <rect x="40" y="82" width="260" height="54" rx="10" class="sunk"/>
 <text x="170" y="104" text-anchor="middle" class="tb">Sosm &gt; 280: pseudo-hypoNa</text>
 <text x="170" y="124" text-anchor="middle" class="t3">glucose สูง, protein/lipid สูง</text>
 <rect x="440" y="82" width="250" height="54" rx="10" class="c1"/>
 <text x="565" y="104" text-anchor="middle" class="tw">True hypoNa</text>
 <text x="565" y="124" text-anchor="middle" class="tw">Sosm &lt; 280 → Urine Osm</text>
 <path d="M500 136L330 168" class="ln" marker-end="url(#nephro-05-02-a)"/>
 <path d="M600 136L600 168" class="ln" marker-end="url(#nephro-05-02-a)"/>
 <rect x="170" y="170" width="250" height="54" rx="10" class="oksoft"/>
 <text x="295" y="192" text-anchor="middle" class="tb">Uosm &lt; 100 (ไม่มี ADH)</text>
 <text x="295" y="212" text-anchor="middle" class="t3">Polydipsia, low solute intake</text>
 <rect x="470" y="170" width="260" height="54" rx="10" class="c1soft"/>
 <text x="600" y="192" text-anchor="middle" class="tb">Uosm &gt; 100 (ADH effect)</text>
 <text x="600" y="212" text-anchor="middle" class="t3">→ ประเมิน volume status</text>
 <path d="M520 224L130 266" class="ln" marker-end="url(#nephro-05-02-a)"/>
 <path d="M580 224L370 266" class="ln" marker-end="url(#nephro-05-02-a)"/>
 <path d="M640 224L620 266" class="ln" marker-end="url(#nephro-05-02-a)"/>
 <rect x="10" y="268" width="230" height="140" rx="10" class="c2soft"/>
 <text x="125" y="290" text-anchor="middle" class="tb">Hypervolemic</text>
 <text x="22" y="314" class="t2">Heart failure</text>
 <text x="22" y="334" class="t2">Cirrhosis</text>
 <text x="22" y="354" class="t2">Nephrotic syndrome</text>
 <text x="22" y="374" class="t2">Renal failure</text>
 <rect x="255" y="268" width="230" height="140" rx="10" class="acsoft"/>
 <text x="370" y="290" text-anchor="middle" class="tb">Euvolemic</text>
 <text x="267" y="314" class="t2">SIADH</text>
 <text x="267" y="334" class="t2">Adrenal insufficiency</text>
 <text x="267" y="354" class="t2">Hypothyroid</text>
 <text x="267" y="380" class="t3">UNa &gt; 20–30</text>
 <rect x="500" y="268" width="230" height="140" rx="10" class="misssoft"/>
 <text x="615" y="290" text-anchor="middle" class="tb">Hypovolemic</text>
 <text x="512" y="314" class="t2">Extrarenal loss</text>
 <text x="512" y="332" class="t3">UNa &lt; 30: V/D, burn</text>
 <text x="512" y="358" class="t2">Renal loss</text>
 <text x="512" y="376" class="t3">UNa &gt; 30: diuretic (thiazide),</text>
 <text x="512" y="394" class="t3">salt wasting, mineralocorticoid ↓</text>
</svg>''', "ไล่สามคำถาม: Sosm ต่ำจริงไหม → Uosm บอกว่ามี ADH ทำงานไหม → volume status แล้วดู urine Na ช่วยแยก")

S2 = sec("nephro-05-02", "Hyponatremia: approach & SIADH",
    "Sosm <280 → Uosm >100 → volume · SIADH = euvolemic, Sosm <275, Uosm >100, UNa >20–30, ตัด AI/hypothyroid", minutes=9,
    source=f"{D} หน้า 167–170, 178–185", nl=["2.3.4(2)", "2.3.4-3(5)", "B9.3(3)"],
    md='''
### นิยามและอาการ

- **Na < 135 mEq/L**
- **Severe symptoms**: AOC, seizures, **vomiting**, respiratory distress (จาก cerebral edema)
- **Mild–moderate**: nausea (ไม่อาเจียน), headache, fatigue, muscle weakness, spasm, cramps
- อาการขึ้นกับ **ความเร็ว** มากกว่าระดับ (acute < 48 ชม. อันตรายกว่า) (เสริม)

### Approach (สไลด์)

[[fig:nephro-05-02-f1]]

1. **R/O pseudohyponatremia** — Sosm > 280: น้ำตาลสูง (ดึงน้ำออกนอกเซลล์ — Na ลด ~1.6 ทุก glucose ที่เพิ่ม 100 mg/dL (เสริม)), protein/lipid สูงมาก (ผลแลป artifact)
2. **True hypoNa (Sosm < 280)** → ดู **Uosm**
   - **Uosm < 100** = ไตขับน้ำได้ดี (ไม่มี ADH) → **primary polydipsia, low solute intake** (beer potomania, tea & toast)
   - **Uosm > 100** = มี ADH effect → ประเมิน volume
3. Volume status + urine Na
   - **Hypervolemic**: HF, cirrhosis, nephrotic, renal failure
   - **Euvolemic**: **SIADH**, adrenal insufficiency, hypothyroid
   - **Hypovolemic**: extrarenal loss (**UNa < 30**) · renal loss (**UNa > 30**: diuretic โดยเฉพาะ thiazide, salt-wasting)

### SIADH — เกณฑ์ (diagnosis of exclusion)

- Serum Na **< 135**
- Serum Osm **< 275–280**
- Urine Osm **> 100**
- **Euvolemic**
- Urine Na **> 20–30**
- **Exclude adrenal insufficiency, hypothyroid** (และไม่ได้ใช้ diuretic)

สาเหตุ (สไลด์เป็นภาพ — สรุปเสริม)

| กลุ่ม | ตัวอย่าง |
|---|---|
| Malignancy | **Small cell lung cancer**, head & neck |
| Lung | **Pneumonia (PCP), TB**, empyema, mechanical ventilation |
| CNS | Meningitis, SAH, stroke, head injury |
| Drugs | SSRI, carbamazepine, cyclophosphamide, vincristine, MDMA |
| อื่น ๆ | ปวดมาก คลื่นไส้มาก หลังผ่าตัด, HIV |

เบาะแสเสริมของ SIADH: **uric acid ต่ำ (< 4)**, BUN ต่ำ (dilution) (เสริม)

> หลุมพราง: ผู้ป่วยมะเร็งปอด Na 129 แต่ **Uosm 50** → ไม่ใช่ SIADH (ADH ไม่ได้ทำงาน) แต่เป็น polydipsia
''',
    figs=[F_HYPO],
    pearls=[
        "HypoNa: Sosm (pseudo?) → Uosm (<100 = polydipsia) → volume + UNa",
        "SIADH: euvolemic, Sosm <275–280, Uosm >100, UNa >20–30, ตัด AI/hypothyroid",
        "Uosm <100 ไม่ใช่ SIADH",
        "Hypovolemic: UNa <30 extrarenal · >30 renal (thiazide)",
        "SIADH มักมาจาก small cell lung CA, pneumonia/TB, CNS, ยา",
    ],
    items=[
        mcq("NEPHRO-05-02-1",
            "A 60-year-old woman who has smoked for 30 years has a persistent cough. CXR shows a right upper lung mass. Serum Na 129 mmol/L, serum osmolality 268 mOsm/kg, urine osmolality 50 mOsm/kg. What is the most likely cause of her hyponatremia?",
            "Primary polydipsia",
            ["SIADH", "Adrenal insufficiency", "Hypothyroidism", "Thiazide-induced hyponatremia"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''แม้มีก้อนที่ปอดซึ่งชวนให้คิดถึง SIADH แต่ **Uosm 50 (< 100)** แปลว่าไตขับน้ำเปล่าได้เต็มที่ — ไม่มี ADH ทำงาน → **primary polydipsia** (สไลด์เฉลย: SIADH ต้อง Uosm > 100)
- SIADH ต้องมีปัสสาวะเข้มข้นเกินควร (Uosm > 100)
- Adrenal insufficiency และ hypothyroidism ทำให้ ADH ทำงานเช่นกัน Uosm จึงสูง
- Thiazide ลดความสามารถในการเจือจางปัสสาวะ Uosm จะไม่ต่ำขนาดนี้''',
            pearl="Uosm <100 = polydipsia/low solute ไม่ใช่ SIADH", topic="Uosm in hyponatremia",
            ref=[f"{D} หน้า 168, 178–179"], nl=["2.3.4(2)", "2.3.4-3(5)"]),
        mcq("NEPHRO-05-02-2",
            "A man with HIV and Pneumocystis pneumonia has severe vomiting but is clinically euvolemic. Serum osmolality 246 mOsm/kg, urine osmolality 453 mOsm/kg, urine Na 68 mmol/L, BUN 12 mg/dL, Cr 0.7 mg/dL, Na 111, K 3.6, Cl 78, HCO3 22 mmol/L, glucose 184 mg/dL. Thyroid function and cortisol are normal. What is the most likely diagnosis?",
            "SIADH",
            ["Pseudohyponatremia", "Cerebral salt wasting", "Salt-wasting nephropathy", "Volume depletion-induced hyponatremia"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ปรับค่า Cl ให้ anion gap สอดคล้อง)",
            explain='''Sosm 246 (< 275) = true hypoNa · Uosm 453 (> 100) · **euvolemic** · UNa 68 (> 30) · TFT/cortisol ปกติ = **SIADH** จาก PCP (โรคปอด) และคลื่นไส้อาเจียน
- Pseudohyponatremia ต้องมี Sosm ปกติ/สูง — glucose 184 ทำให้ Na ลดลงแค่ราว 1–2 mEq/L
- Cerebral salt wasting ต้องมีโรคสมองและผู้ป่วย **hypovolemic**
- Salt-wasting nephropathy ก็ hypovolemic และต้องมีโรคไต (Cr ปกติ)
- Volume depletion จากอาเจียนจะมี UNa ต่ำ (< 30) และตรวจพบขาดน้ำ
หมายเหตุ: ในสไลด์ให้ Cl 96 ซึ่งทำให้ anion gap ติดลบ (111 − 96 − 22 = −7) ข้อนี้ปรับเป็น Cl 78 (AG = 11)''',
            pearl="Euvolemic + Uosm >100 + UNa >30 + ตัด AI/hypothyroid = SIADH", topic="SIADH diagnosis",
            ref=[f"{D} หน้า 169, 180–181"], nl=["2.3.4-3(5)"]),
        mcq("NEPHRO-05-02-3",
            "A 15-year-old boy has chronic cough, dyspnea, and 6-kg weight loss over 3 months. BP 110/72 mmHg, cachectic, no edema, decreased breath sounds over the right lung. Na 126, K 3.5, Cl 91, HCO3 24 mEq/L, BUN 6 mg/dL, Cr 0.7 mg/dL, uric acid 3.5 mg/dL, albumin 3.6 g/dL. Serum osmolality 250 mOsm/kg, urine osmolality 305 mOsm/kg, urine Na 60 mEq/L. CXR: right pleural effusion. What is the cause of his hyponatremia?",
            "SIADH",
            ["Hyperlipidemia", "Hyperglycemia", "Reset osmostat", "Adrenal insufficiency"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''โรคปอดเรื้อรัง (น่าจะเป็น TB) + Sosm 250 + Uosm 305 + UNa 60 + euvolemic + **BUN และ uric acid ต่ำ** (จาก dilution) = **SIADH**
- Hyperlipidemia และ hyperglycemia ทำให้ pseudo/translocational hypoNa ซึ่ง Sosm จะไม่ต่ำ
- Reset osmostat เป็น SIADH ชนิดหนึ่งที่ Na คงที่ราว 125–135 และไตยังเจือจางปัสสาวะได้เมื่อได้น้ำ — ตัวเลือกทั่วไปที่ถูกที่สุดตามเกณฑ์คือ SIADH
- Adrenal insufficiency มักมี K สูง ความดันต่ำ และต้องตัดออกด้วย cortisol (สไลด์ให้คำตอบ SIADH)''',
            pearl="SIADH: BUN และ uric acid ต่ำจาก dilution", topic="SIADH",
            ref=[f"{D} หน้า 169, 182–183"], nl=["2.3.4-3(5)"]),
        mcq("NEPHRO-05-02-4",
            "A 72-year-old woman started hydrochlorothiazide 2 weeks ago. She now has dizziness and dry mucous membranes; BP drops from 128/76 to 104/60 mmHg on standing. Na 122 mEq/L, serum osmolality 256 mOsm/kg, urine osmolality 420 mOsm/kg, urine Na 54 mEq/L. What is the most likely mechanism of her hyponatremia?",
            "Renal sodium loss from diuretic with hypovolemia",
            ["SIADH", "Primary polydipsia", "Extrarenal sodium loss", "Pseudohyponatremia"],
            explain='''Hypotonic hypoNa + Uosm > 100 + **hypovolemic** (postural drop, ปากแห้ง) + **UNa > 30** = เสีย Na ทาง **ไต** จาก thiazide (thiazide เป็น diuretic ที่ทำ hypoNa บ่อยกว่า loop) (เสริม)
- SIADH ต้อง euvolemic
- Polydipsia จะมี Uosm < 100
- Extrarenal loss (ท้องเสีย อาเจียน) จะมี UNa < 30
- Pseudohyponatremia มี Sosm ปกติ''',
            pearl="Hypovolemic + UNa >30 = renal loss (thiazide)", topic="Hypovolemic hyponatremia",
            ref=[f"{D} หน้า 168"], nl=["2.3.4(2)"]),
    ])

# ---------------------------------------------------------------- 05-03 HypoNa management + ODS
F_RATE = fig("nephro-05-03-f1", "เพดานการแก้ Na: ช้าดีกว่าเร็ว", '''<svg viewBox="0 0 740 300">
 <defs><marker id="nephro-05-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <path d="M80 250H700" class="ln" marker-end="url(#nephro-05-03-a)"/>
 <path d="M80 250V30" class="ln" marker-end="url(#nephro-05-03-a)"/>
 <text x="40" y="40" text-anchor="middle" class="t3">Na</text>
 <text x="720" y="292" text-anchor="end" class="t3">ชั่วโมง</text>
 <text x="80" y="268" text-anchor="middle" class="t3">0</text>
 <text x="380" y="268" text-anchor="middle" class="t3">24</text>
 <text x="680" y="268" text-anchor="middle" class="t3">48</text>
 <path d="M380 246V254" class="ln"/><path d="M680 246V254" class="ln"/>
 <text x="70" y="234" text-anchor="end" class="t3">110</text>
 <text x="70" y="114" text-anchor="end" class="t3">+10–12</text>
 <text x="70" y="74" text-anchor="end" class="t3">+18</text>
 <path d="M80 110H700" class="lnf"/>
 <path d="M80 70H700" class="lnf"/>
 <path d="M80 230L380 110L680 70" class="lnbad"/>
 <path d="M80 230L380 150L680 110" class="lnok"/>
 <rect x="420" y="160" width="250" height="70" rx="10" class="box"/>
 <path d="M436 182H470" class="lnbad"/><text x="478" y="187" class="t2">เพดานสูงสุด (ห้ามเกิน)</text>
 <path d="M436 212H470" class="lnok"/><text x="478" y="217" class="t2">กลุ่มเสี่ยง ODS: 6–8/วัน</text>
 <text x="230" y="100" text-anchor="middle" class="t3">ไม่เกิน 10–12 ใน 24 ชม.</text>
 <text x="530" y="60" text-anchor="middle" class="t3">ไม่เกิน 18 ใน 48 ชม.</text>
</svg>''', "เส้นแดงคือเพดานสูงสุดที่ยอมให้ Na ขึ้น เส้นเขียวคือเป้าในผู้ป่วยเสี่ยง ODS (ขาดสารอาหาร ตับแข็ง สูงอายุ ติดสุรา hypokalemia)")

S3 = sec("nephro-05-03", "Hyponatremia management & osmotic demyelination",
    "อาการรุนแรง → 3% NaCl · chronic: hypo NSS / eu (SIADH) จำกัดน้ำ / hyper จำกัดน้ำ ± loop · เพดาน 10–12 ใน 24 ชม.", minutes=8,
    source=f"{D} หน้า 171–172, 177, 184–189", nl=["2.3.4(2)", "B9.4(2)", "2.3.4-3(5)"],
    md='''
### Severe symptomatic hyponatremia (AOC, seizure, อาเจียน, หายใจลำบาก)

- **3% NaCl IV drip 1–2 ml/kg/hr** (ตามสไลด์)
- **F/U อาการ และ serum Na ทุก 2–3 ชั่วโมง**
- อาการไม่ดีขึ้นและ Na เพิ่ม < 5 mEq/L → **repeat**
- อาการดีขึ้น → **หยุด 3% NaCl** แล้วรักษาสาเหตุ
- (เสริม) แนวทางยุโรป 2014: **3% NaCl 150 ml IV ใน 20 นาที** ซ้ำได้ 2–3 ครั้ง จนอาการดีขึ้นหรือ Na ขึ้น 5 mEq/L

ตัวอย่างประมาณการ (เสริม, Adrogué–Madias): Na เปลี่ยนต่อสารน้ำ 1 L = (Na ในสารน้ำ − Na ผู้ป่วย) ÷ (TBW + 1)
- หญิง 60 kg (TBW = 0.5 × 60 = 30 L), Na 115, ให้ 3% NaCl (Na 513) → (513 − 115) ÷ 31 ≈ **+12.8 mEq/L ต่อ 1 L** ดังนั้นให้ ~400 ml จะขึ้นราว 5 mEq/L

### Chronic hyponatremia — รักษาตาม volume

| Volume | การรักษา |
|---|---|
| Hypovolemic | **NSS IV** (คืน volume → ADH หยุดหลั่ง) |
| Euvolemic (SIADH) | **Fluid restriction**, salt/urea tablet, furosemide, vaptans |
| Hypervolemic (HF, cirrhosis) | **Fluid restriction ± loop diuretic** |

+ รักษาสาเหตุเสมอ

> ห้ามให้ NSS ใน SIADH: ไตขับ Na ออกหมดแต่เก็บน้ำไว้ (Uosm สูง) → Na อาจ **ต่ำลง** (เสริม)

### ความเร็วในการแก้ (สำคัญมาก)

[[fig:nephro-05-03-f1]]

- **Max 10–12 mEq/L ใน 24 ชั่วโมง**
- **Max 18 mEq/L ใน 48 ชั่วโมง**
- กลุ่มเสี่ยง ODS (malnutrition, cirrhosis, old age, alcoholism, hypokalemia) → ไม่เกิน **6–8 mEq/L ต่อวัน**

### Osmotic demyelination syndrome (ODS)

- ชื่อเดิม **central pontine myelinolysis**
- เกิดจาก Na/Sosm เปลี่ยนเร็วเกินไป (มักแก้ hypoNa เรื้อรังเร็วเกิน) — อาการตามหลัง 2–6 วัน (เสริม)
- อาการ: seizures, AOC, dysarthria/dysphagia (เสริม), **locked-in syndrome** (กล้ามเนื้ออ่อนแรงทั้งตัวแต่ยังกระพริบตาได้)
- Ix: **MRI brain**
- Tx: **supportive**, monitor electrolyte (ถ้าแก้เกิน อาจ re-lower ด้วย D5W + DDAVP (เสริม))

> Water intoxication (ดื่มน้ำปริมาณมากในเวลาสั้น เช่น รับน้อง แข่งดื่มน้ำ, MDMA) → acute hypoNa → **cerebral edema** → ซึม ปวดหัว อาเจียน ชัก → **3% NaCl**
''',
    figs=[F_RATE],
    pearls=[
        "อาการรุนแรง → 3% NaCl (สไลด์ 1–2 ml/kg/hr; แนวทางใหม่ 150 ml ใน 20 นาที) เป้า +5 mEq/L",
        "Chronic: hypovolemic NSS · SIADH จำกัดน้ำ · hypervolemic จำกัดน้ำ ± loop",
        "เพดาน: ≤10–12 ใน 24 ชม. · ≤18 ใน 48 ชม. · กลุ่มเสี่ยง ≤6–8/วัน",
        "ODS = locked-in syndrome · MRI · supportive",
        "ห้ามให้ NSS ใน SIADH",
    ],
    items=[
        mcq("NEPHRO-05-03-1",
            "A 60-year-old man with well-controlled diabetes has fatigue for 1 week. HR 60/min, BP 120/80 mmHg, JVP 4 cm above the sternal angle, no edema. Na 126, K 4, Cl 92, HCO3 24 mEq/L, BUN 10 mg/dL, Cr 1 mg/dL, serum osmolality 262 mOsm/kg, FBS 140 mg/dL, HbA1c 6%. TFT and cortisol are normal. Urine Na 60 mEq/L, urine osmolality 500 mOsm/kg. CXR: lung nodules. He is alert and has no neurological symptoms. What is the most appropriate management?",
            "Restrict fluid intake",
            ["NaCl tablets alone", "Intravenous 0.9% NaCl", "Intravenous 3% NaCl", "Insulin"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ปรับค่า Cl และ osmolality ให้สอดคล้อง)",
            explain='''Euvolemic + Sosm ต่ำ + Uosm 500 + UNa 60 + ตัด AI/hypothyroid แล้ว + lung nodule = **SIADH แบบ chronic ไม่มีอาการรุนแรง** → **fluid restriction** เป็นการรักษาแรก (สไลด์เฉลย)
- NaCl tablet ใช้เสริมเมื่อจำกัดน้ำแล้วไม่ได้ผล ไม่ใช่ขั้นแรก
- 0.9% NaCl ทำให้ Na ใน SIADH ไม่ขึ้นหรือต่ำลง เพราะไตขับ Na ออกแต่เก็บน้ำ
- 3% NaCl ใช้เมื่อมีอาการรุนแรง (ซึม ชัก อาเจียน)
- Insulin ไม่จำเป็น HbA1c 6% และน้ำตาลไม่ได้ทำให้ Na ต่ำมีนัยสำคัญ
หมายเหตุ: ในสไลด์ให้ Cl 84 (AG = 18) และ osmolarity 250 ซึ่งต่ำกว่าค่าที่คำนวณได้ ข้อนี้ปรับเป็น Cl 92 และ Sosm 262''',
            pearl="SIADH ไม่มีอาการรุนแรง → จำกัดน้ำ", topic="SIADH treatment",
            ref=[f"{D} หน้า 172, 184–185"], nl=["2.3.4-3(5)"]),
        mcq("NEPHRO-05-03-2",
            "During a university hazing event, a 19-year-old student was forced to drink a large volume of plain water within 2 hours. He becomes drowsy with headache, nausea, and repeated vomiting, then has a generalized seizure. Serum Na is 118 mEq/L. What is the most appropriate immediate treatment?",
            "Intravenous 3% NaCl",
            ["Fluid restriction alone", "Intravenous 0.9% NaCl at maintenance rate", "Oral desmopressin", "Intravenous furosemide alone"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ดื่มน้ำปริมาณมากในเวลาสั้น = **water intoxication → acute severe symptomatic hyponatremia** (ซึม อาเจียน ชัก จาก cerebral edema) ต้องให้ **3% NaCl IV** ทันที เป้าเพิ่ม Na ราว 4–6 mEq/L ให้อาการดีขึ้น (สไลด์เฉลย)
- จำกัดน้ำอย่างเดียวช้าเกินไปสำหรับผู้ป่วยที่ชัก
- 0.9% NaCl ไม่พอแก้ cerebral edema
- Desmopressin ทำให้เก็บน้ำมากขึ้น Na ยิ่งต่ำ
- Furosemide อย่างเดียวไม่เพิ่ม Na ได้เร็วพอ''',
            pearl="Water intoxication + ชัก → 3% NaCl", topic="Acute hyponatremia",
            ref=[f"{D} หน้า 171, 188–189"], nl=["2.3.4(2)", "B9.4(2)"]),
        mcq_ordered("NEPHRO-05-03-3",
            "A 70-year-old malnourished man with alcohol use disorder has chronic asymptomatic hyponatremia with serum Na 112 mEq/L. Treatment is started. To minimize the risk of osmotic demyelination, what is the maximum serum Na he should reach at 24 hours?",
            ["114 mEq/L", "120 mEq/L", "124 mEq/L", "130 mEq/L", "135 mEq/L"], 1,
            explain='''ผู้ป่วยเป็น **กลุ่มเสี่ยง ODS** (malnutrition, alcoholism, สูงอายุ) สไลด์ให้แก้ไม่เกิน **6–8 mEq/L ต่อวัน** → 112 + 8 = **120 mEq/L**
- 114 คือเพิ่มเพียง 2 ซึ่งช้าเกินจำเป็น
- 124 (เพิ่ม 12) เป็นเพดานของผู้ป่วยที่ไม่เสี่ยง ODS
- 130 และ 135 เพิ่ม 18–23 ใน 24 ชั่วโมง เสี่ยง ODS สูงมาก''',
            pearl="กลุ่มเสี่ยง ODS: แก้ Na ≤ 6–8 mEq/L/วัน", topic="Correction rate",
            ref=[f"{D} หน้า 172, 177"], nl=["2.3.4(2)"]),
        mcq("NEPHRO-05-03-4",
            "A 45-year-old woman with chronic hyponatremia (Na 110 mEq/L) had her Na raised to 132 mEq/L within 24 hours. Three days later she develops dysarthria, dysphagia, and quadriparesis; she is awake and can communicate only by blinking. What is the most appropriate investigation?",
            "MRI of the brain",
            ["CT angiography of the neck", "Lumbar puncture", "Nerve conduction study", "Electroencephalography"],
            explain='''Na ขึ้น 22 mEq/L ใน 24 ชั่วโมง (เกินเพดาน 10–12) แล้วเกิด **locked-in syndrome** หลัง 2–6 วัน = **osmotic demyelination syndrome (central pontine myelinolysis)** ยืนยันด้วย **MRI brain** และรักษาแบบ supportive
- CTA คอใช้หา basilar artery occlusion ซึ่งเกิดเฉียบพลันไม่สัมพันธ์กับการแก้ Na
- Lumbar puncture ใช้หา meningitis/SAH
- Nerve conduction study ใช้กับโรคเส้นประสาทส่วนปลาย (เช่น GBS) ซึ่งตากระพริบได้และไม่สัมพันธ์กับ Na
- EEG ใช้ประเมินชัก''',
            pearl="แก้ Na เร็วเกิน → locked-in → MRI (ODS)", topic="ODS",
            ref=[f"{D} หน้า 177"], nl=["2.3.4(2)"]),
        mcq("NEPHRO-05-03-5",
            "A 66-year-old woman with SIADH from a newly diagnosed small cell lung cancer has Na 121 mmol/L. She is alert with mild fatigue and no nausea, vomiting, confusion, or seizure. What is the most appropriate initial treatment?",
            "Restrict water intake",
            ["Intravenous 3% NaCl", "Desmopressin (DDAVP)", "Intravenous 0.9% NaCl", "Hydrochlorothiazide"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (เพิ่มอาการให้ชัด)",
            explain='''สไลด์สรุป: **severe symptomatic hypoNa → 3% NaCl** ส่วน **chronic hypoNa จาก SIADH → fluid restriction** ผู้ป่วยรายนี้ไม่มีอาการรุนแรง จึงเริ่มด้วย **จำกัดน้ำ**
- 3% NaCl ใช้เมื่อมีอาการรุนแรง (ซึม ชัก อาเจียน)
- DDAVP เป็น ADH analog ทำให้เก็บน้ำมากขึ้น Na ยิ่งต่ำ
- 0.9% NaCl ทำให้ Na ใน SIADH ไม่ขึ้นหรือต่ำลง
- Thiazide ทำให้ hypoNa แย่ลง
หมายเหตุ: โจทย์ในสไลด์ให้แค่ "SIADH Na 121 treatment?" โดยไม่บอกอาการ — ถ้ามีอาการรุนแรงคำตอบจะเปลี่ยนเป็น 3% NaCl''',
            pearl="SIADH: อาการรุนแรง → 3% NaCl · ไม่รุนแรง → จำกัดน้ำ", topic="SIADH treatment",
            ref=[f"{D} หน้า 186–187"], nl=["2.3.4-3(5)"]),
    ])

# ---------------------------------------------------------------- 05-04 Hypernatremia
S4 = sec("nephro-05-04", "Hypernatremia",
    "Na >145 · hypo (extrarenal/renal) · eu (DI) · hyper (NaCl/NaHCO3, Conn, Cushing) · แก้ด้วย free water ช้า ๆ", minutes=7,
    source=f"{D} หน้า 173–176", nl=["2.3.4(2)", "B9.4(2)", "B11.2.5-3(6)"],
    md='''
### นิยามและอาการ

- **Na > 145 mEq/L** — เกิดเมื่อเสียน้ำมากกว่า Na และ **ดื่มน้ำไม่ได้** (กลไกกระหายน้ำปกติป้องกันได้) → พบในผู้สูงอายุ ติดเตียง ทารก ผู้ป่วยหมดสติ (เสริม)
- **Acute (< 48 ชม.)**: signs of dehydration, irritability, restlessness, confusion, AOC, muscle weakness, focal neurodeficit, seizure (เซลล์สมองหดตัว อาจมี intracranial hemorrhage (เสริม))
- **Chronic (> 48 ชม.)**: ไม่มีอาการหรืออาการน้อย

### สาเหตุแบ่งตาม volume (สไลด์)

| Volume | Extrarenal (Uosm > 600) | Renal (Uosm < 600) |
|---|---|---|
| **Hypovolemic** | GI loss (diarrhea, vomiting), skin loss (burns, sweating) | Diuretics, osmotic diuresis (hyperglycemia, mannitol) |
| **Euvolemic** | Impaired thirst, ไม่สามารถเข้าถึงน้ำ | **Diabetes insipidus** (central, nephrogenic) |
| **Hypervolemic** | Excessive NaCl/NaHCO3 infusion | Primary hyperaldosteronism (Conn), Cushing |

> Uosm > 600 = ไตตอบสนอง ADH ดี (ปัญหาอยู่นอกไต) · Uosm < 600 (โดยเฉพาะ < Sosm) = ไตเสียน้ำเอง

### การรักษา

1. **Shock → IV isotonic solution (NSS)** ก่อน
2. รักษาสาเหตุ (เช่น DDAVP ใน central DI)
3. Hypernatremia correction
   - Hypo/euvolemic → **oral free water** หรือ **IV hypotonic solution**
   - Hypervolemic → **furosemide + (oral free water หรือ IV hypotonic)**
   - สารน้ำ: **5% dextrose in water (D5W)** หรือ **0.45% NaCl**
4. ความเร็ว
   - **Acute hyperNa แก้เร็วได้ 1–2 mEq/L/hr**
   - **Chronic hyperNa แก้ 0.5 mEq/L/hr (max 10–12 mEq/L ใน 24 ชม.)** — แก้เร็วเกินเสี่ยง **cerebral edema**

### Free water deficit (เสริม)

Free water deficit = TBW × (Na ÷ 140 − 1)

ตัวอย่าง: ชาย 70 kg (TBW = 0.6 × 70 = 42 L), Na 160 → 42 × (160 ÷ 140 − 1) = 42 × 0.143 ≈ **6 L** — ให้ไม่ให้ Na ลดเกิน 10 ใน 24 ชม. จึงให้ราวครึ่งหนึ่ง (~3 L) ในวันแรก บวกกับน้ำที่ยังเสียต่อเนื่อง
''',
    pearls=[
        "HyperNa = ขาดน้ำ + ดื่มน้ำไม่ได้ (ผู้สูงอายุ ติดเตียง)",
        "Uosm >600 = extrarenal loss · <600 = renal (diuretic, osmotic, DI)",
        "ช็อกให้ NSS ก่อน แล้วค่อย free water (D5W หรือ 0.45% NaCl)",
        "Chronic hyperNa: ลด ≤0.5 mEq/L/hr (≤10–12/24 ชม.) — เร็วเกิน = cerebral edema",
        "Free water deficit = TBW × (Na/140 − 1) (เสริม)",
    ],
    items=[
        mcq("NEPHRO-05-04-1",
            "An 85-year-old bedridden woman from a nursing home presents with lethargy after 4 days of fever and poor oral intake. BP 118/70 mmHg (no orthostatic data), dry mucosa. Na 162 mEq/L, glucose 110 mg/dL, urine osmolality 780 mOsm/kg. What is the most likely mechanism of her hypernatremia?",
            "Insensible and inadequately replaced water loss with intact ADH response",
            ["Central diabetes insipidus", "Nephrogenic diabetes insipidus", "Osmotic diuresis from hyperglycemia", "Hypertonic saline administration"],
            explain='''Uosm 780 (> 600) = ไตเข้มข้นปัสสาวะได้ดี ADH ทำงาน → ปัญหาอยู่ **นอกไต**: เสียน้ำทางผิว/หายใจตอนมีไข้ + ติดเตียงเข้าถึงน้ำไม่ได้
- Central และ nephrogenic DI จะมี Uosm ต่ำ (< Sosm)
- Osmotic diuresis ต้องมีน้ำตาลสูงมาก (glucose 110 ปกติ) และ Uosm มักไม่เกิน 600
- ไม่มีประวัติได้ hypertonic saline และผู้ป่วยไม่ได้ hypervolemic''',
            pearl="HyperNa + Uosm >600 = extrarenal water loss", topic="Hypernatremia approach",
            ref=[f"{D} หน้า 174–175"], nl=["2.3.4(2)"]),
        mcq("NEPHRO-05-04-2",
            "A 78-year-old man presents with confusion after 5 days of diarrhea. BP 76/40 mmHg, HR 128/min, cold extremities. Na 165 mEq/L. What is the most appropriate initial fluid?",
            "0.9% NaCl bolus",
            ["5% dextrose in water bolus", "0.45% NaCl at maintenance rate", "3% NaCl", "Oral free water only"],
            explain='''ผู้ป่วย **ช็อก** สไลด์: **shock → IV isotonic solution (NSS)** ก่อนเพื่อคืน perfusion (NSS มี Na 154 ซึ่งต่ำกว่า Na ผู้ป่วยอยู่แล้ว) จากนั้นจึงเปลี่ยนเป็น hypotonic fluid แก้ free water deficit ช้า ๆ
- D5W bolus ไม่อยู่ใน intravascular space นานพอแก้ช็อก และลด Na เร็วเกินไป
- 0.45% NaCl อัตรา maintenance ช้าเกินสำหรับช็อก
- 3% NaCl เพิ่ม Na ซึ่งสูงอยู่แล้ว
- น้ำทางปากอย่างเดียวไม่พอและผู้ป่วยสับสน''',
            pearl="HyperNa + shock → NSS ก่อน", topic="Hypernatremia treatment",
            ref=[f"{D} หน้า 176"], nl=["B9.4(2)"]),
        mcq_ordered("NEPHRO-05-04-3",
            "A 70-kg man has chronic hypernatremia (Na 160 mEq/L) from poor water intake, with stable hemodynamics. Using total body water of 60% of body weight, what is his estimated free water deficit?",
            ["2 L", "4 L", "6 L", "8 L", "10 L"], 2,
            explain='''Free water deficit = TBW × (Na ÷ 140 − 1) = (0.6 × 70) × (160 ÷ 140 − 1) = 42 × 0.143 ≈ **6 L** (สูตรเสริม)
- 2 และ 4 L ต่ำเกินเพราะใช้ TBW หรือส่วนต่าง Na ผิด
- 8 และ 10 L สูงเกิน (เช่นคิด TBW เป็น 100% ของน้ำหนัก)
แนวทาง: chronic hyperNa ให้ Na ลดไม่เกิน 10–12 mEq/L ใน 24 ชั่วโมง (≈ 0.5 mEq/L/hr) จึงให้ deficit ราวครึ่งหนึ่งในวันแรก บวกกับน้ำที่ยังเสียต่อเนื่อง''',
            pearl="FWD = TBW × (Na/140 − 1)", topic="Free water deficit",
            ref=[f"{D} หน้า 176"], nl=["B9.4(2)"]),
        mcq("NEPHRO-05-04-4",
            "A 52-year-old woman has resistant hypertension, Na 147 mEq/L, K 2.9 mEq/L, and HCO3 31 mEq/L. She is mildly volume expanded. Plasma renin activity is suppressed and aldosterone is high. What is the most likely cause of her hypernatremia?",
            "Primary hyperaldosteronism",
            ["Central diabetes insipidus", "Diarrhea", "Osmotic diuresis", "Impaired thirst"],
            explain='''ความดันสูงดื้อยา + hypoK + metabolic alkalosis + Na ค่อนสูง + **renin ต่ำ aldosterone สูง** = **primary hyperaldosteronism (Conn)** — ในสไลด์จัดเป็น hypervolemic hyperNa ที่สาเหตุมาจากไต (aldosterone ดูด Na กลับ)
- Central DI เป็น euvolemic และไม่มี hypoK/alkalosis/ความดันสูง
- Diarrhea ทำให้ hypovolemic และ metabolic acidosis
- Osmotic diuresis ทำให้ hypovolemic
- Impaired thirst ไม่อธิบายความดันสูงและ hypoK''',
            pearl="HyperNa + HT + hypoK + alkalosis = Conn", topic="Hypervolemic hypernatremia",
            ref=[f"{D} หน้า 174–175"], nl=["2.3.4(2)"]),
    ])

LECTURE = lecture("05", "Polyuria & sodium disorders", "Serum osm · DI · hyponatremia · SIADH · ODS · hypernatremia",
    objectives=[
        "แยก frequency กับ polyuria และใช้ Uosm แบ่ง water/solute diuresis ได้",
        "ไล่ approach hyponatremia (Sosm → Uosm → volume → UNa) และวินิจฉัย SIADH ได้",
        "เลือกการรักษา hyponatremia ตามอาการ/volume และกำหนดความเร็วการแก้ไม่ให้เกิด ODS ได้",
        "หาสาเหตุและแก้ hypernatremia ด้วย free water อย่างปลอดภัยได้",
    ],
    sections=[S1, S2, S3, S4])
