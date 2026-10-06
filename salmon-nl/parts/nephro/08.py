from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Nephro"

# ---------------------------------------------------------------- 08-01 approach
F_MA = fig("nephro-08-01-f1", "Metabolic acidosis: AG กว้าง vs AG ปกติ", '''<svg viewBox="0 0 740 400">
 <defs><marker id="nephro-08-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="10" width="280" height="48" rx="10" class="acsoft"/>
 <text x="370" y="31" text-anchor="middle" class="tb">Metabolic acidosis</text>
 <text x="370" y="49" text-anchor="middle" class="t3">AG = Na − Cl − HCO3 (± albumin)</text>
 <path d="M300 58L180 92" class="ln" marker-end="url(#nephro-08-01-a)"/>
 <path d="M440 58L560 92" class="ln" marker-end="url(#nephro-08-01-a)"/>
 <rect x="10" y="94" width="350" height="40" rx="10" class="bad"/>
 <text x="185" y="119" text-anchor="middle" class="tw">Wide AG (&gt; 12) — มีกรดใหม่เพิ่ม</text>
 <rect x="380" y="94" width="350" height="40" rx="10" class="c1"/>
 <text x="555" y="119" text-anchor="middle" class="tw">Normal AG — เสีย HCO3 / Cl ↑</text>
 <rect x="10" y="144" width="350" height="246" rx="10" class="badsoft"/>
 <text x="22" y="168" class="tb">STEP 1 · Endogenous acid</text>
 <text x="22" y="190" class="t2">Lactate: shock/sepsis → lactate</text>
 <text x="22" y="210" class="t2">Ketone: DKA, alcoholic, starvation</text>
 <text x="22" y="230" class="t2">Renal failure (ช่วงท้าย) → BUN, Cr</text>
 <text x="22" y="260" class="tb">STEP 2 · Exogenous acid (toxin)</text>
 <text x="22" y="282" class="t2">Methanol, ethylene glycol</text>
 <text x="22" y="302" class="t2">Salicylate</text>
 <text x="22" y="324" class="t2">→ toxicology screen</text>
 <text x="22" y="346" class="t2">→ osmolal gap ≥ 10 = toxic alcohol</text>
 <text x="22" y="372" class="t3">ถ้า AG กว้าง → delta ratio หาตัวที่สองซ้อน</text>
 <rect x="380" y="144" width="350" height="246" rx="10" class="c1soft"/>
 <text x="392" y="168" class="tb">สาเหตุ</text>
 <text x="392" y="190" class="t2">Diarrhea (เสีย HCO3 ทาง GI)</text>
 <text x="392" y="210" class="t2">RTA (type 1, 2, 4)</text>
 <text x="392" y="230" class="t2">Renal failure (ช่วงแรก)</text>
 <text x="392" y="250" class="t2">Excessive NSS</text>
 <text x="392" y="270" class="t2">Toluene (ส่วนใหญ่ normal gap)</text>
 <text x="392" y="300" class="tb">แยก GI vs ไต (เสริม)</text>
 <text x="392" y="322" class="t2">Urine AG = UNa + UK − UCl</text>
 <text x="392" y="344" class="t2">ติดลบ → diarrhea (ขับ NH4 ได้)</text>
 <text x="392" y="364" class="t2">บวก → RTA (ขับ NH4 ไม่ได้)</text>
</svg>''', "คำนวณ AG ก่อน ซ้ายคือกลุ่มที่มีกรดใหม่เพิ่ม (ไล่หาตามสองขั้นในสไลด์) ขวาคือกลุ่มที่เสีย HCO3 และ Cl ขึ้นแทน")

S1 = sec("nephro-08-01", "Metabolic acidosis: สาเหตุและ approach",
    "↑H+ (lactate, ketone, toxin) · ↓HCO3 (diarrhea, RTA) · ขับกรดไม่ได้ (AKI/CKD) · แยกด้วย AG", minutes=6,
    source=f"{D} หน้า 260–261, 263, 266", nl=["2.3.4(2)", "B9.2.5(2)", "B9.1.2(6)"],
    md='''
### กลไก 3 แบบ (สไลด์)

| กลไก | ตัวอย่าง |
|---|---|
| **↑H+** | Endogenous: lactic acidosis, ketosis · Exogenous: methanol, salicylate, **excessive NSS** |
| **↓HCO3** | GI: **diarrhea** · Renal: **type 2 RTA** |
| **Poor excretion** | AKI, CKD (GFR < 20) |

### อาการ

- CNS: headache, confusion, AOC
- Respiratory: **tachypnea / Kussmaul breathing** (หายใจเร็วลึกชดเชย)
- Cardio: arrhythmia (และ myocardial contractility ลด vasodilation ถ้า pH < 7.1 (เสริม))
- GI: N/V, diarrhea
- Muscle weakness

### Approach

[[fig:nephro-08-01-f1]]

**Wide AG MA** — จำง่าย "สไลด์ 4 กลุ่ม": **Renal failure (ช่วงท้าย) · Toxin · Ketone · Lactate**
- STEP 1 หา endogenous acid: lactate level · serum/urine ketone · BUN, Cr
- STEP 2 ถ้าไม่เจอ หา exogenous: toxicology screen + **osmolal gap ≥ 10 mOsm/kg** (สงสัย toxic alcohol)

**Normal AG MA**: diarrhea · RTA · renal failure ช่วงแรก · excessive NSS · toluene (ส่วนใหญ่ normal gap)

### Osmolal gap (เสริมสูตร)

- Osmolal gap = **measured Sosm − calculated Sosm**
- Calculated Sosm = 2 × Na + glucose/18 + BUN/2.8 (+ ethanol/3.7 ถ้าดื่ม)
- ≥ 10 → มีสารออสโมติกที่ไม่ได้วัด: methanol, ethylene glycol, isopropanol, ethanol, mannitol

> Saline excess: ให้ NSS ปริมาณมาก (Cl 154) → hyperchloremic normal AG MA — พบบ่อยใน ICU (เสริม)
''',
    figs=[F_MA],
    pearls=[
        "Wide AG = Renal failure (late), Toxin, Ketone, Lactate",
        "Normal AG = diarrhea, RTA, early renal failure, NSS ปริมาณมาก, toluene",
        "Wide AG ไม่พบ lactate/ketone/ไตวาย → osmolal gap ≥10 = toxic alcohol",
        "Urine AG ติดลบ = diarrhea · บวก = RTA (เสริม)",
    ],
    items=[
        mcq("NEPHRO-08-01-1",
            "A 45-year-old Thai man presents with dyspnea for 2 days. BT 37 °C, RR 28/min, PR 92/min, BP 120/80 mmHg, Kussmaul breathing. Na 132, Cl 92, K 4, HCO3 10 mEq/L. Glucose, creatinine, and other tests are within normal limits. He drinks alcohol heavily and has eaten little for several days. What is the most likely cause of his acid–base abnormality?",
            "Alcoholic ketoacidosis",
            ["Acute diarrhea", "Renal tubular acidosis", "Toluene ingestion", "Tricyclic antidepressant overdose"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (เพิ่มประวัติดื่มสุราให้ชัด)",
            explain='''AG = 132 − 92 − 10 = **30** → **wide AG metabolic acidosis** ที่น้ำตาลและไตปกติ ในคนดื่มสุรามากและกินน้อย = **alcoholic ketoacidosis** (ketone ตัวหลักคือ β-hydroxybutyrate จึงอาจตรวจ ketone แบบ nitroprusside ได้น้อย (เสริม))
- Acute diarrhea และ RTA ทำให้ **normal AG** MA
- Toluene ส่วนใหญ่ทำ normal AG (hippurate ถูกขับทางปัสสาวะเร็ว)
- TCA overdose เด่นที่ anticholinergic, QRS กว้าง, ชัก ไม่ได้ทำ AG 30 เป็นลักษณะหลัก
หมายเหตุ: โจทย์ในสไลด์ไม่ได้ให้ประวัติดื่มสุรา (คำตอบอาศัย AG กว้าง + ตัดตัวเลือกอื่นที่เป็น normal gap)''',
            pearl="AG กว้าง + น้ำตาลปกติ + ดื่มสุรา = AKA", topic="Wide AG MA",
            ref=[f"{D} หน้า 261–262, 269–270"], nl=["2.3.4(2)"]),
        mcq("NEPHRO-08-01-2",
            "A 62-year-old man undergoing major abdominal surgery received 8 L of 0.9% NaCl over 24 hours. Postoperatively: Na 142, K 4.0, Cl 120, HCO3 18 mEq/L; lactate is normal and creatinine is unchanged. What is the most likely cause of his acid–base abnormality?",
            "Hyperchloremic acidosis from large-volume normal saline",
            ["Lactic acidosis from hypoperfusion", "Ketoacidosis from fasting", "Type 4 renal tubular acidosis", "Ethylene glycol ingestion"],
            explain='''AG = 142 − 120 − 18 = **4** (ปกติ/ต่ำ) + Cl สูงมากหลังได้ NSS 8 L (Cl 154 mEq/L) → **hyperchloremic normal AG MA จาก excessive NSS** (สไลด์จัดเป็นสาเหตุ normal AG)
- Lactic acidosis และ ketoacidosis ทำให้ AG กว้าง และ lactate ปกติ
- Type 4 RTA ต้องมี K สูงและ hypoaldosteronism
- Ethylene glycol ทำให้ AG กว้างและ osmolal gap สูง''',
            pearl="NSS ปริมาณมาก → hyperchloremic normal AG MA", topic="Saline acidosis",
            ref=[f"{D} หน้า 260, 266"], nl=["2.3.4(2)", "B9.4(2)"]),
        mcq("NEPHRO-08-01-3",
            "A 30-year-old woman has profuse watery diarrhea for 3 days. Na 136, K 3.0, Cl 114, HCO3 14 mEq/L. Urine Na 30, urine K 25, urine Cl 75 mEq/L. Which statement best explains her acid–base disorder?",
            "Normal anion gap metabolic acidosis from GI bicarbonate loss with appropriate renal ammonium excretion",
            ["Normal anion gap metabolic acidosis from distal renal tubular acidosis", "High anion gap metabolic acidosis from lactic acid", "Metabolic alkalosis from volume contraction", "Normal anion gap metabolic acidosis from hypoaldosteronism"],
            explain='''AG = 136 − 114 − 14 = **8** (normal AG MA) · urine AG = 30 + 25 − 75 = **−20 (ติดลบ)** → ไตขับ NH4+ (มากับ Cl) ได้ดี แปลว่าไตปกติ สาเหตุจึงเป็น **เสีย HCO3 ทาง GI (diarrhea)** (เสริม)
- Distal RTA จะมี urine AG **บวก** เพราะขับ NH4 ไม่ได้
- AG ไม่กว้าง จึงไม่ใช่ lactic acidosis
- HCO3 ต่ำ ไม่ใช่ alkalosis
- Hypoaldosteronism (type 4 RTA) ทำให้ K **สูง** ไม่ใช่ต่ำ''',
            pearl="Normal AG MA + urine AG ติดลบ = diarrhea", topic="Urine anion gap",
            ref=[f"{D} หน้า 260, 266"], nl=["2.3.4(2)", "B9.1.2(6)"]),
    ])

# ---------------------------------------------------------------- 08-02 wide AG specifics
F_TOX = fig("nephro-08-02-f1", "Toxic alcohol: ทำไม ethanol/fomepizole ช่วยได้", '''<svg viewBox="0 0 740 280">
 <defs><marker id="nephro-08-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="40" width="150" height="48" rx="10" class="box"/>
 <text x="85" y="69" text-anchor="middle" class="tb">Methanol</text>
 <rect x="10" y="170" width="150" height="48" rx="10" class="box"/>
 <text x="85" y="199" text-anchor="middle" class="tb">Ethylene glycol</text>
 <path d="M160 64H318" class="ln" marker-end="url(#nephro-08-02-a)"/>
 <path d="M160 194H318" class="ln" marker-end="url(#nephro-08-02-a)"/>
 <rect x="180" y="110" width="128" height="48" rx="10" class="acsoft"/>
 <text x="244" y="131" text-anchor="middle" class="tb">ADH (ตับ)</text>
 <text x="244" y="149" text-anchor="middle" class="t3">alcohol dehydrog.</text>
 <path d="M244 110V72" class="lnf"/>
 <path d="M244 158V186" class="lnf"/>
 <rect x="320" y="40" width="190" height="48" rx="10" class="badsoft"/>
 <text x="415" y="61" text-anchor="middle" class="tb">Formic acid</text>
 <text x="415" y="79" text-anchor="middle" class="t3">wide AG MA</text>
 <rect x="320" y="170" width="190" height="48" rx="10" class="badsoft"/>
 <text x="415" y="191" text-anchor="middle" class="tb">Glycolic, oxalic acid</text>
 <text x="415" y="209" text-anchor="middle" class="t3">wide AG MA</text>
 <path d="M510 64H538" class="ln" marker-end="url(#nephro-08-02-a)"/>
 <path d="M510 194H538" class="ln" marker-end="url(#nephro-08-02-a)"/>
 <rect x="540" y="30" width="190" height="68" rx="10" class="bad"/>
 <text x="635" y="54" text-anchor="middle" class="tw">ตา: optic neuropathy</text>
 <text x="635" y="72" text-anchor="middle" class="tw">papilledema</text>
 <text x="635" y="90" text-anchor="middle" class="tw">macular edema</text>
 <rect x="540" y="160" width="190" height="68" rx="10" class="bad"/>
 <text x="635" y="184" text-anchor="middle" class="tw">ไต: Ca oxalate</text>
 <text x="635" y="202" text-anchor="middle" class="tw">crystal → AKI</text>
 <text x="635" y="220" text-anchor="middle" class="tw">(Ca ต่ำได้)</text>
 <rect x="10" y="236" width="720" height="38" rx="8" class="oksoft"/>
 <text x="370" y="260" text-anchor="middle" class="t2">Tx: ethanol (แย่ง ADH) หรือ fomepizole (ยับยั้ง ADH) + hemodialysis (เอาทั้งสารแม่และกรดออก)</text>
</svg>''', "สารแม่ไม่ค่อยมีพิษ แต่ enzyme alcohol dehydrogenase ในตับเปลี่ยนเป็นกรดพิษ การให้ ethanol หรือ fomepizole จึงตัดเส้นทางนี้ (เส้นประ = จุดที่ enzyme ทำงาน)")

S2 = sec("nephro-08-02", "Wide AG MA: ketoacidosis, toxic alcohols, salicylate",
    "Lactate · ketone (DKA/AKA/starvation) · methanol (ตามัว) · ethylene glycol (oxalate crystal) · salicylate (resp alk + AGMA)", minutes=9,
    source=f"{D} หน้า 261–265, 271–274", nl=["2.3.4(2)", "2.2.46", "2.3.18(7)"],
    md='''
### Endogenous acids

| | สาเหตุ | Ix | หลักการรักษา (เสริม) |
|---|---|---|---|
| **Lactic acidosis** | Shock/sepsis (type A), metformin, ตับวาย | **Lactate level** | แก้ perfusion รักษาสาเหตุ |
| **Ketoacidosis** | **DKA**, **alcoholic ketoacidosis**, starvation | **Serum/urine ketone** | DKA: fluid + insulin + K · AKA: fluid + **dextrose + thiamine** |
| **Renal failure** (ช่วงท้าย) | AKI, CKD | BUN, Cr | RRT ตามข้อบ่งชี้ |

### Toxic alcohols

[[fig:nephro-08-02-f1]]

**Methanol** (เหล้าเถื่อน/เหล้าต้ม/moonshine, น้ำยาล้างกระจก)
- Methanol → **formic acid**
- **Optic neuropathy, papilledema, macular edema** — ตามัว "เหมือนมองในพายุหิมะ" (เสริม)
- Wide AG MA + **osmolal gap สูง**

**Ethylene glycol** (antifreeze — น้ำยาหม้อน้ำ)
- Ethylene glycol → **glycolic/oxalic acids**
- **Calcium oxalate crystal** ตกที่ไต → **AKI** · UA: calcium oxalate crystal (ทำให้ Ca ต่ำได้ (เสริม))

**การรักษา (ตามสไลด์)**
- Supportive
- **Ethanol** (กรณีระดับ ethanol ในเลือดยังไม่สูง) — แย่ง alcohol dehydrogenase · fomepizole เป็นทางเลือกมาตรฐาน (เสริม)
- **Hemodialysis** (กรด/AG สูง ตามัว ไตวาย ระดับสารสูง (เสริม))
- Methanol: ให้ folic/folinic acid ช่วยกำจัด formate (เสริม)

> คนที่ดื่มเหล้าแล้ว **ซึม/หมดสติ + AG กว้างมาก** → ส่ง **serum osmolality** เพื่อคำนวณ osmolal gap หา toxic alcohol (ส่วน ethanol อย่างเดียวไม่ทำ AG กว้าง)

### Salicylate intoxication

- สาเหตุ: aspirin, **ยาทาแก้ปวด (methyl salicylate), น้ำมันมวย**
- **Tinnitus**, N/V
- กระตุ้น respiratory center โดยตรง → **tachypnea → early respiratory alkalosis**
- ต่อมา uncoupling oxidative phosphorylation → **wide AG metabolic acidosis** (เสริม)
- AOC, seizures, **hyperthermia**
- ABG คลาสสิก: **mixed respiratory alkalosis + wide AG metabolic acidosis** (pH มักใกล้ปกติ/ด่าง)
- Tx: **supportive** (urine alkalinization ด้วย NaHCO3 (เสริม)), **hemodialysis** ในรายรุนแรง

| ABG ตัวอย่าง (เสริม) | ค่า |
|---|---|
| Na 140 · Cl 104 · HCO3 15 | AG = 21 (กว้าง) |
| pH 7.46 · PaCO2 22 | Winter = 1.5 × 15 + 8 = 30.5 ± 2 → PaCO2 22 **ต่ำกว่าคาด** = + resp alkalosis |
''',
    figs=[F_TOX],
    pearls=[
        "Wide AG: lactate → ketone → BUN/Cr → toxin (osmolal gap ≥10)",
        "Methanol = formic acid → ตามัว papilledema macular edema",
        "Ethylene glycol = oxalate crystal → AKI",
        "Toxic alcohol Tx: ethanol/fomepizole + HD",
        "Salicylate = tinnitus + หายใจเร็ว + resp alkalosis + wide AG MA (ยาทา น้ำมันมวย)",
    ],
    items=[
        mcq("NEPHRO-08-02-1",
            "A 30-year-old man has dyspnea and blurred vision 1 hour after a party with friends. Hyperpnea RR 30/min, SpO2 98%. Fundoscopy shows macular edema in both eyes; the rest of the examination is normal. ABG: pH 7.22, PaO2 88 mmHg, PaCO2 25 mmHg, HCO3 10 mEq/L. Which toxin is most likely responsible?",
            "Methanol",
            ["Cyanide", "Paraquat", "Zinc phosphide", "Organophosphate"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ปรับ HCO3 ให้สอดคล้องกับ pH)",
            explain='''ดื่มสังสรรค์ + **ตามัว + macular edema** + metabolic acidosis ที่หายใจชดเชย = **methanol** (formic acid ทำลาย optic nerve/retina)
- Cyanide ทำให้ lactic acidosis รุนแรง ช็อก ชักเร็ว แต่ไม่มี macular edema เฉพาะ
- Paraquat ทำให้แผลในปาก ปอดเป็นพังผืด ไตวาย
- Zinc phosphide ทำให้ช็อก หัวใจ ตับ (phosphine gas) ไม่ทำตามัวเฉพาะ
- Organophosphate ทำ cholinergic crisis (รูม่านตาเล็ก น้ำลาย หลอดลมหดเกร็ง)
หมายเหตุ: สไลด์ให้ pH 7.21, PCO2 26, HCO3 12 ซึ่งตาม Henderson–Hasselbalch ไม่สอดคล้องกัน (จะได้ pH ~7.29) ข้อนี้ปรับเป็น HCO3 10, PaCO2 25, pH 7.22 (Winter's 1.5 × 10 + 8 = 23 ± 2 จึง compensated)''',
            pearl="ดื่มเหล้า + ตามัว + AG MA = methanol", topic="Methanol",
            ref=[f"{D} หน้า 264, 273–274"], nl=["2.2.46", "2.3.18(7)"]),
        mcq("NEPHRO-08-02-2",
            "A 22-year-old man drank a large amount of alcohol at a graduation party and is brought to the hospital stuporous. Na 135, K 5, Cl 98, HCO3 8 mmol/L, glucose 90 mg/dL, BUN 14 mg/dL. What is the best investigation to identify the emergency condition?",
            "Serum osmolality",
            ["CBC with platelets", "Urine anion gap", "Liver function tests", "Serum amylase"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''AG = 135 − 98 − 8 = **29** (wide AG MA รุนแรง) ในคนดื่มสุรามาก ต้องรีบหา **toxic alcohol** (methanol/ethylene glycol) ด้วย **serum osmolality → osmolal gap** (≥ 10 = สงสัย) เพราะต้องรักษาด้วย ethanol/fomepizole + HD ทันที
- CBC ไม่ช่วยบอกสาเหตุ acidosis
- Urine anion gap ใช้กับ **normal AG** MA เพื่อแยก diarrhea กับ RTA
- LFT และ amylase ไม่ตอบคำถามเรื่อง AG กว้างแบบฉุกเฉิน''',
            pearl="ดื่มเหล้า + AG กว้าง + ซึม → serum osm (osmolal gap)", topic="Osmolal gap",
            ref=[f"{D} หน้า 263, 271–272"], nl=["2.2.46", "B9.3(3)"]),
        mcq_ordered("NEPHRO-08-02-3",
            "A 40-year-old man is found confused. Na 135 mEq/L, glucose 90 mg/dL, BUN 14 mg/dL, measured serum osmolality 320 mOsm/kg, ethanol undetectable. What is his osmolal gap (mOsm/kg)?",
            ["0", "10", "20", "40", "60"], 3,
            explain='''Calculated Sosm = 2 × 135 + 90/18 + 14/2.8 = 270 + 5 + 5 = **280** → osmolal gap = 320 − 280 = **40** (≥ 10 = มีสารออสโมติกแปลกปลอม เช่น methanol/ethylene glycol)
- 0 และ 10 เกิดจากลืมคูณ Na ด้วย 2 หรือใช้ค่าปกติ 290 แทนค่าที่คำนวณ
- 20 เกิดจากไม่รวม glucose/BUN หรือคิดผิดหลัก
- 60 เกิดจากใช้ calculated Sosm แค่ 2 × Na − ...''',
            pearl="Osmolal gap = measured − (2Na + glu/18 + BUN/2.8)", topic="Osmolal gap calculation",
            ref=[f"{D} หน้า 263"], nl=["B9.3(3)"]),
        mcq("NEPHRO-08-02-4",
            "A 35-year-old man who works as a car mechanic is found drunk-appearing and confused. He develops oliguric AKI. Na 138, Cl 100, HCO3 10 mEq/L; osmolal gap is 28. Urinalysis shows numerous envelope-shaped crystals. Besides supportive care and hemodialysis, which treatment is most appropriate?",
            "Fomepizole or ethanol",
            ["Intravenous N-acetylcysteine", "Intravenous naloxone", "Atropine", "Methylene blue"],
            explain='''AG = 138 − 100 − 10 = **28** + osmolal gap สูง + **calcium oxalate crystal (รูปซองจดหมาย)** + AKI = **ethylene glycol (antifreeze)** → ให้ **ethanol (ตามสไลด์) หรือ fomepizole** ยับยั้ง alcohol dehydrogenase ร่วมกับ hemodialysis
- N-acetylcysteine ใช้กับ paracetamol overdose
- Naloxone ใช้กับ opioid
- Atropine ใช้กับ organophosphate
- Methylene blue ใช้กับ methemoglobinemia''',
            pearl="Oxalate crystal + AG กว้าง + osmolal gap = ethylene glycol", topic="Ethylene glycol",
            ref=[f"{D} หน้า 264"], nl=["2.2.46", "2.3.18(7)"]),
        mcq("NEPHRO-08-02-5",
            "A 60-year-old woman rubbed large amounts of a methyl salicylate liniment and boxing oil on her joints for days. She has tinnitus, vomiting, and fever. RR 32/min. Na 140, Cl 104, HCO3 15 mEq/L. ABG: pH 7.46, PaCO2 22 mmHg. Which acid–base disorder is present?",
            "Respiratory alkalosis with high anion gap metabolic acidosis",
            ["High anion gap metabolic acidosis with appropriate compensation", "Pure respiratory alkalosis", "Normal anion gap metabolic acidosis with respiratory acidosis", "Metabolic alkalosis with respiratory alkalosis"],
            explain='''AG = 140 − 104 − 15 = **21** (กว้าง) · ถ้าเป็น MA ล้วน Winter's คาด PaCO2 = 1.5 × 15 + 8 = 30.5 ± 2 แต่จริง 22 **ต่ำกว่าคาด** → มี **respiratory alkalosis** ซ้อน (salicylate กระตุ้นศูนย์หายใจ) = ภาพคลาสสิกของ **salicylate intoxication** (pH จึงปกติ/ค่อนด่าง)
- Compensated AGMA จะมี PaCO2 ราว 29–33
- Pure resp alkalosis จะไม่มี AG กว้าง
- AG กว้าง ไม่ใช่ normal AG และ PaCO2 ต่ำไม่ใช่ resp acidosis
- HCO3 ต่ำ ไม่ใช่ metabolic alkalosis
(ตรวจ: 6.1 + log(15 ÷ 0.66) ≈ 7.46)''',
            pearl="Salicylate = resp alkalosis + wide AG MA", topic="Salicylate",
            ref=[f"{D} หน้า 265"], nl=["2.2.46", "2.3.4(2)"]),
    ])

# ---------------------------------------------------------------- 08-03 normal AG & RTA
S3 = sec("nephro-08-03", "Normal AG MA & renal tubular acidosis (RTA)",
    "Diarrhea vs RTA · distal RTA (type 1) พบบ่อยในภาคอีสาน: hypoK + นิ่ว · proximal (type 2) · type 4 (hyperK, DM)", minutes=8,
    source=f"{D} หน้า 266–268, 275–276", nl=["2.3.14-3(12)", "2.3.4(2)", "2.3.6(7)"],
    md='''
### Normal AG metabolic acidosis (สไลด์)

- **Diarrhea**
- **RTA**
- **Renal failure (ช่วงแรก)** — ช่วงท้ายจะกลายเป็น wide AG
- **Excessive NSS**
- **Toluene** (ดมกาว — ส่วนใหญ่ normal gap)
- อื่น ๆ (เสริม): acetazolamide, ureteral diversion

### RTA (ตารางในสไลด์เป็นภาพ — สรุปเสริม)

| | Type 1 (distal) | Type 2 (proximal) | Type 4 (hypoaldo) |
|---|---|---|---|
| ปัญหา | ขับ H+ ที่ collecting duct ไม่ได้ | ดูด HCO3 กลับที่ PCT ไม่ได้ | Aldosterone ต่ำ/ดื้อ → ขับ H+ และ K ไม่ได้ |
| **K** | **ต่ำ** | **ต่ำ** | **สูง** |
| Urine pH | **> 5.5** เสมอ | < 5.5 เมื่อ HCO3 ต่ำมาก | < 5.5 |
| Urine AG | บวก | แล้วแต่ | บวก |
| ลักษณะเด่น | **นิ่ว/nephrocalcinosis**, กระดูกพรุน | **Fanconi** (glucosuria ที่น้ำตาลปกติ, phosphaturia, aminoaciduria) | DM, CKD เล็กน้อย |
| สาเหตุ | Sjögren, SLE, **amphotericin B**, **endemic ในภาคอีสาน** | Multiple myeloma, **tenofovir**, acetazolamide, ifosfamide | **DM (hyporeninemic hypoaldo)**, ACEI/ARB, spironolactone, TMP/SMX, heparin |
| รักษา | Alkali (**K citrate**) | Alkali ขนาดสูง + K | ลด K, fludrocortisone, loop diuretic |

> **ชาย/หญิงวัยหนุ่มสาวในภาคอีสาน + proximal muscle weakness + hypoK + normal AG metabolic acidosis** (± อัมพาตเป็นพัก ๆ, นิ่ว) → **distal RTA** — ต่างจาก hypokalemic periodic paralysis ที่ acid–base ปกติ และ thyrotoxic paralysis ที่มีอาการ hyperthyroid

> ผู้ป่วยเบาหวาน ไตเสื่อมเล็กน้อย + **K สูง** + normal AG MA → **type 4 RTA**
''',
    pearls=[
        "Normal AG MA: diarrhea, RTA, early CKD, NSS ปริมาณมาก, toluene",
        "Distal RTA (type 1): hypoK + urine pH >5.5 + นิ่ว · พบบ่อยภาคอีสาน · Tx K citrate",
        "Proximal RTA (type 2): Fanconi, myeloma, tenofovir",
        "Type 4 RTA: hyperK + DM (hyporeninemic hypoaldosteronism)",
    ],
    items=[
        mcq("NEPHRO-08-03-1",
            "A 25-year-old man from northeastern Thailand presents with weakness. He has proximal muscle weakness. Labs: Na 138, K 2.4, Cl 116, HCO3 14 mEq/L, Cr 1.6 mg/dL (rising). Urine pH 6.8. Ultrasound shows bilateral medullary nephrocalcinosis. What is the most likely diagnosis?",
            "Distal renal tubular acidosis",
            ["Graves disease with thyrotoxic periodic paralysis", "Hypokalemic periodic paralysis", "Gitelman syndrome", "Primary hyperaldosteronism"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (เพิ่ม lab ให้ครบ)",
            explain='''ชายภาคอีสาน + อ่อนแรง + **hypoK + metabolic acidosis** (AG = 138 − 116 − 14 = 8 normal AG) + urine pH > 5.5 + nephrocalcinosis + Cr ขึ้น = **distal RTA (type 1)** ซึ่งเป็นโรคประจำถิ่นในภาคอีสาน
- Thyrotoxic และ hypokalemic periodic paralysis เป็น **shift** — acid–base ปกติ ไม่มีนิ่ว ไม่มีไตเสื่อม
- Gitelman และ hyperaldosteronism ทำให้ hypoK แต่มี **metabolic alkalosis**''',
            pearl="อีสาน + hypoK + normal AG MA + นิ่ว = distal RTA", topic="Distal RTA",
            ref=[f"{D} หน้า 266–268, 275–276"], nl=["2.3.14-3(12)"]),
        mcq("NEPHRO-08-03-2",
            "A 64-year-old man with type 2 diabetes for 15 years (eGFR 50 mL/min/1.73 m2) has persistent K 5.9 mEq/L. Na 138, Cl 110, HCO3 18 mEq/L. Urine pH 5.0. Plasma renin and aldosterone are both low. He takes no medications that affect potassium. What is the most likely diagnosis?",
            "Type 4 renal tubular acidosis",
            ["Type 1 (distal) renal tubular acidosis", "Type 2 (proximal) renal tubular acidosis", "Diabetic ketoacidosis", "Primary adrenal insufficiency"],
            explain='''Normal AG MA (AG = 138 − 110 − 18 = 10) + **K สูง** + urine pH < 5.5 + renin และ aldosterone ต่ำในคนเบาหวาน = **type 4 RTA (hyporeninemic hypoaldosteronism)** (เสริม)
- Type 1 และ type 2 RTA ทำให้ K **ต่ำ**
- DKA ทำให้ AG กว้างและน้ำตาลสูงมาก
- Primary adrenal insufficiency มี renin **สูง** (aldosterone ต่ำ) ร่วมกับ Na ต่ำ ความดันต่ำ ผิวคล้ำ''',
            pearl="DM + hyperK + normal AG MA = type 4 RTA", topic="Type 4 RTA",
            ref=[f"{D} หน้า 266–268"], nl=["2.3.14-3(12)"]),
        mcq("NEPHRO-08-03-3",
            "A 38-year-old man with HIV has been on a tenofovir-containing regimen for 3 years. He now has bone pain. Labs: K 3.0, Cl 112, HCO3 16 mEq/L, Na 138, serum glucose 92 mg/dL, phosphate 1.8 mg/dL. Urinalysis: glucose 2+, protein 1+. Which renal disorder is most likely?",
            "Proximal (type 2) renal tubular acidosis with Fanconi syndrome",
            ["Distal (type 1) renal tubular acidosis", "Type 4 renal tubular acidosis", "Diabetic nephropathy", "Acute interstitial nephritis"],
            explain='''**Glucosuria ทั้งที่น้ำตาลในเลือดปกติ** + **phosphate ต่ำ** (ปวดกระดูก — osteomalacia) + hypoK + normal AG MA (AG = 10) ในผู้ที่ใช้ **tenofovir** = **Fanconi syndrome กับ proximal RTA** (PCT ดูดกลับ HCO3, glucose, phosphate ไม่ได้) (สไลด์ระบุ tenofovir เป็น nephrotoxin)
- Distal RTA ไม่ทำให้มี glucosuria/phosphaturia
- Type 4 RTA ทำให้ K สูง
- Diabetic nephropathy ต้องมีน้ำตาลสูง
- AIN มี WBC/eosinophil และไม่ทำ Fanconi เป็นลักษณะหลัก''',
            pearl="Tenofovir → Fanconi + proximal RTA", topic="Proximal RTA",
            ref=[f"{D} หน้า 12, 266–268"], nl=["2.3.14-3(12)"]),
    ])

LECTURE = lecture("08", "Metabolic acidosis", "Approach · ketoacidosis · toxic alcohols · salicylate · RTA",
    objectives=[
        "แบ่งสาเหตุ metabolic acidosis ตามกลไกและ AG ได้",
        "ไล่หา wide AG MA ตามขั้น lactate → ketone → ไต → toxin (osmolal gap) ได้",
        "จำลักษณะ methanol, ethylene glycol, salicylate และการรักษาได้",
        "แยก diarrhea กับ RTA และแยก RTA type 1, 2, 4 ได้",
    ],
    sections=[S1, S2, S3])
