from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Endocrine"

# ---------------------------------------------------------------- 02-01 Hypoglycemia
F_HYPO = fig("endo-02-01-f1", "จัดการ hypoglycemia ตามความรุนแรง", '''<svg viewBox="0 0 740 400">
 <defs><marker id="endo-02-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="200" y="10" width="340" height="48" rx="10" class="acsoft"/>
 <text x="370" y="31" text-anchor="middle" class="tb">CBG &lt; 70 (DM) / &lt; 55 (non-DM)</text>
 <text x="370" y="49" text-anchor="middle" class="t3">+ อาการ autonomic / neuroglycopenia</text>
 <path d="M290 58L170 92" class="ln" marker-end="url(#endo-02-01-a)"/>
 <path d="M450 58L570 92" class="ln" marker-end="url(#endo-02-01-a)"/>
 <rect x="20" y="94" width="320" height="44" rx="10" class="oksoft"/>
 <text x="180" y="114" text-anchor="middle" class="tb">Mild–moderate</text>
 <text x="180" y="130" text-anchor="middle" class="t3">รู้ตัว ช่วยเหลือตัวเองได้</text>
 <rect x="400" y="94" width="320" height="44" rx="10" class="badsoft"/>
 <text x="560" y="114" text-anchor="middle" class="tb">Severe</text>
 <text x="560" y="130" text-anchor="middle" class="t3">AOC / ชัก / ช่วยตัวเองไม่ได้</text>
 <rect x="20" y="150" width="320" height="86" rx="10" class="box"/>
 <text x="32" y="170" class="tb">Oral glucose 15–30 g</text>
 <text x="32" y="191" class="t2">ลูกอม 3 เม็ด · น้ำอัดลมครึ่งกระป๋อง</text>
 <text x="32" y="212" class="t2">น้ำผลไม้กล่องเล็ก · ขนมปัง 1 แผ่น</text>
 <text x="32" y="230" class="t3">(rule of 15)</text>
 <rect x="400" y="150" width="320" height="86" rx="10" class="box"/>
 <text x="412" y="170" class="t3">เจาะ clot blood ก่อน (หาสาเหตุ/ยืนยัน)</text>
 <text x="412" y="190" class="tb">50% glucose 50 mL IV push</text>
 <text x="412" y="210" class="t2">แล้ว 10% D/W 60–100 mL/hr</text>
 <text x="412" y="228" class="t3">alcohol/ขาดอาหาร → thiamine ก่อน/พร้อม</text>
 <path d="M180 236V262" class="ln" marker-end="url(#endo-02-01-a)"/>
 <path d="M560 236V262" class="ln" marker-end="url(#endo-02-01-a)"/>
 <rect x="20" y="264" width="700" height="40" rx="10" class="sunk"/>
 <text x="370" y="289" text-anchor="middle" class="tb">ตรวจอาการ + CBG ซ้ำหลัง 15 นาที</text>
 <path d="M200 304L130 330" class="ln" marker-end="url(#endo-02-01-a)"/>
 <path d="M540 304L610 330" class="ln" marker-end="url(#endo-02-01-a)"/>
 <rect x="20" y="332" width="280" height="56" rx="10" class="misssoft"/>
 <text x="160" y="354" text-anchor="middle" class="tb">ยัง &lt; 70 / ไม่ดีขึ้น</text>
 <text x="160" y="374" text-anchor="middle" class="t2">ให้ซ้ำ</text>
 <rect x="420" y="332" width="300" height="56" rx="10" class="oksoft"/>
 <text x="570" y="354" text-anchor="middle" class="tb">&gt; 70 + ดีขึ้น</text>
 <text x="570" y="374" text-anchor="middle" class="t2">mild: snack/มื้ออาหาร · severe: admit</text>
</svg>''', "แบ่งที่ความสามารถช่วยเหลือตัวเอง — กินได้ให้ทางปาก กินไม่ได้ให้ 50% glucose IV แล้วตรวจซ้ำทุก 15 นาที")

S1 = sec("endo-02-01", "Hypoglycemia",
    "DM <70 · non-DM <55 + Whipple triad · กินได้ → glucose 15–30 g · หมดสติ → 50% glucose 50 mL IV แล้ว 10% D/W · alcohol → thiamine ก่อน/พร้อม glucose", minutes=8,
    source=f"{D} หน้า 66–84", nl=["2.2.17", "B11.4(1)", "2.2.36"],
    md='''
### นิยาม (สไลด์หน้า 66)
- ระดับน้ำตาล: **ผู้ป่วย DM < 70 mg/dL** · **ไม่เป็น DM < 55 mg/dL**
- **Whipple triad**: (1) มีอาการ hypoglycemia (2) plasma glucose ต่ำขณะมีอาการ (3) **อาการหายเมื่อน้ำตาลกลับปกติ**

### อาการ
- **Autonomic (adrenergic/cholinergic)**: ใจสั่น ชีพจรเร็ว **เหงื่อออก** มือสั่น กระสับกระส่าย หิว คลื่นไส้
- **Neuroglycopenia**: ปวดศีรษะ สับสน พฤติกรรมเปลี่ยน **hemiparesis** (เลียนแบบ stroke ได้) ซึม หมดสติ ชัก

> ผู้ป่วยซึม/หมดสติ/อ่อนแรงครึ่งซีกทุกราย → **เจาะ CBG ก่อนเสมอ** (ตรวจเร็ว แก้ได้ทันที) ผู้ใช้ beta-blocker หรือเป็น DM นาน (hypoglycemia unawareness) อาจไม่มีอาการเตือน (เสริม)

### สาเหตุ (สไลด์หน้า 67)

| กลุ่ม | สาเหตุ |
|---|---|
| **ผู้ป่วย DM** (พบบ่อยสุด) | **ยาเกิน (insulin, sulfonylurea)**, กินน้อย/อดมื้อ, ออกกำลังกายหนัก, ไตเสื่อม (ยาค้าง), แอลกอฮอล์ (เสริม) |
| Non-DM ที่ป่วย | critical illness, **sepsis**, **adrenal insufficiency**, ตับ/ไตวาย, non-islet cell tumor |
| Non-DM ที่ดูแข็งแรง | **Insulinoma**, autoimmune hypoglycemia, แอบใช้ insulin/SU (factitious) |

### ความรุนแรง (สไลด์หน้า 68)
- **Severe** = อาการรุนแรง (AOC, ชัก) **หรือแก้ไขด้วยตัวเองไม่ได้** ต้องมีคนช่วย

### การรักษา (สไลด์หน้า 70–71)

[[fig:endo-02-01-f1]]

- **Mild/moderate**: oral glucose **15–30 g** → ตรวจอาการ + CBG ซ้ำ **15 นาที** · ยัง < 70 ให้ซ้ำ · > 70 ให้กินขนม/อาหารมื้อหลัก
- **Severe**: เจาะ **clot blood** (หาสาเหตุ/ยืนยัน plasma glucose) → **50% glucose 50 mL IV push** → ตามด้วย **10% D/W 60–100 mL/hr** → ตรวจซ้ำ 15 นาที → ดีขึ้นแล้ว **admit** ติดตาม CBG
- **Thiamine IV ก่อนหรือพร้อม glucose** ในผู้ที่ขาดอาหารหรือ **ติดสุราเรื้อรัง** เพื่อป้องกัน **Wernicke encephalopathy** — แต่ **ห้ามรอ** thiamine จนช้าการให้ glucose
- ไม่มีเส้นเลือด → **glucagon 1 mg IM/SC** (เสริม)
- Hypoglycemia จาก **sulfonylurea** (โดยเฉพาะ glibenclamide) อยู่นานและกลับซ้ำได้ → admit สังเกตอาการ ≥ 24 ชม. (เสริม)

### หาสาเหตุ (สไลด์หน้า 72)

| สงสัย | ส่งตรวจ |
|---|---|
| ตับ/ไตวาย | BUN, Cr, LFT |
| Sepsis | CBC, CXR, UA, hemoculture |
| Adrenal insufficiency | **cortisol ต่ำ** |
| ยา | **ระดับ sulfonylurea, insulin** |
| **Insulinoma** | **↑C-peptide, ↑proinsulin, ↑insulin** |

| ขณะน้ำตาลต่ำ (เสริม) | Insulin | C-peptide | SU screen |
|---|---|---|---|
| ฉีด insulin เอง | **↑** | **↓** | ลบ |
| Sulfonylurea | ↑ | ↑ | **บวก** |
| Insulinoma | ↑ | ↑ | ลบ |
''',
    figs=[F_HYPO],
    pearls=[
        "Hypoglycemia: DM <70 · non-DM <55 · Whipple triad",
        "หมดสติทุกราย → เจาะ CBG ก่อน",
        "Severe: 50% glucose 50 mL IV push → 10% D/W 60–100 mL/hr → recheck 15 นาที",
        "สุรา/ขาดอาหาร → thiamine ก่อนหรือพร้อม glucose (Wernicke)",
        "Insulin ↑ C-peptide ↓ = ฉีด insulin เอง · ทั้งคู่ ↑ = insulinoma หรือ SU",
    ],
    items=[
        mcq("ENDO-02-01-1",
            "A 50-year-old woman with diabetes on oral hypoglycemic medication is brought in unconscious. For 2 days she had a common cold and poor appetite but continued her medication. RR normal, PR 100/min, BP 100/50 mmHg; generalized weakness of all four limbs, no lateralizing signs. What is the most likely diagnosis?",
            "Hypoglycemia",
            ["Lactic acidosis", "Diabetic ketoacidosis", "Hyperosmolar hyperglycemic state", "Septic shock"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ผู้ป่วย DM ที่ **กินอาหารได้น้อยแต่ยังกินยาลดน้ำตาลเท่าเดิม** แล้วหมดสติ ชีพจรเร็ว (autonomic) **หายใจปกติ** → **hypoglycemia** เป็นสาเหตุที่พบบ่อยและแก้ได้ทันที
- Lactic acidosis และ DKA ทำให้ **หายใจหอบลึก (Kussmaul)** แต่รายนี้ RR ปกติ
- HHS มักเกิดช้าหลายวันในผู้ที่ **หยุดยา** หรือติดเชื้อรุนแรง มีภาวะขาดน้ำมาก ไม่ใช่คนที่ยังกินยาแต่กินข้าวไม่ได้
- Septic shock ต้องมีไข้/แหล่งติดเชื้อและความดันต่ำชัด BP 100/50 ไม่ใช่ shock''',
            pearl="กินน้อย + กินยาเบาหวานเท่าเดิม + ซึม = hypoglycemia", topic="Diagnosis",
            ref=[f"{D} หน้า 73–74"], nl=["2.2.17", "2.2.36"]),
        mcq("ENDO-02-01-2",
            "A 55-year-old man with diabetes, hypertension and an old stroke is found unconscious in the bathroom by his relatives. Vital signs and physical examination are otherwise unremarkable. What is the most appropriate initial investigation?",
            "Capillary blood glucose",
            ["Serum electrolytes", "Serum ketone", "Urine drug screen", "CT brain"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ผู้ป่วยหมดสติทุกราย โดยเฉพาะผู้เป็น DM ต้อง **เจาะน้ำตาลปลายนิ้วทันที** เพราะทำได้ข้างเตียงในไม่กี่วินาที และ hypoglycemia แก้ได้ทันทีและเลียนแบบ stroke ได้
- Electrolyte และ serum ketone สำคัญแต่ใช้เวลานานกว่า ทำตามหลังได้
- Urine drug screen ไม่ใช่การตรวจแรก
- CT brain ทำหลัง exclude hypoglycemia แล้ว (มีประวัติ stroke เดิมยิ่งต้องแยก hypoglycemia ที่ทำให้อาการเก่ากำเริบ)''',
            pearl="หมดสติ → CBG ก่อนทุกอย่าง", topic="Initial investigation",
            ref=[f"{D} หน้า 75–76"], nl=["2.2.17", "2.2.36", "B11.3(1)"]),
        mcq("ENDO-02-01-3",
            "A 50-year-old man with chronic alcohol use presents with acute confusion. Capillary glucose is 45 mg/dL. What is the most appropriate initial management?",
            "Thiamine IV given before or together with 50% glucose IV",
            ["Send serum glucose and wait for the result", "Repeat capillary glucose in 15 minutes", "50% glucose IV bolus, then thiamine the next day", "Send serum electrolytes before any treatment"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Severe hypoglycemia (สับสน) ในผู้ **ติดสุรา** → ให้ **thiamine IV ก่อนหรือพร้อม glucose** เพราะ glucose ใช้ thiamine เป็น cofactor ถ้าขาดอยู่จะกระตุ้น **Wernicke encephalopathy** แล้วให้ **50% glucose 50 mL IV** ทันที
- รอผล serum glucose ทำให้ช้า ควรเจาะเลือดเก็บไว้แล้วรักษาเลย
- ตรวจ CBG ซ้ำโดยไม่ให้การรักษาไม่เหมาะเมื่อมีอาการทางสมอง
- ให้ glucose แล้วค่อยให้ thiamine วันรุ่งขึ้น เสี่ยง Wernicke
- Electrolyte ส่งได้แต่ไม่ใช่สิ่งที่ต้องทำก่อนแก้น้ำตาล''',
            pearl="สุรา + น้ำตาลต่ำ → thiamine + glucose", topic="Thiamine",
            ref=[f"{D} หน้า 71, 77–78"], nl=["2.2.17"]),
        mcq("ENDO-02-01-4",
            "A woman with diabetes on premixed insulin 70/30, 20 units before breakfast and 20 units before dinner, injected her usual evening dose but skipped dinner. She is now drowsy and responds only to pain. PR 100/min, RR 18/min. Capillary glucose is 26 mg/dL. What is the most appropriate initial management?",
            "50% glucose 50 mL IV push",
            ["Send serum glucose to confirm before treating", "0.9% NaCl 1,000 mL/hr", "Regular insulin 0.1 U/kg IV bolus then 0.1 U/kg/hr", "5% D/N/2 at 80 mL/hr"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ฉีด insulin แต่ไม่กินข้าว → **severe hypoglycemia** (ตอบสนองต่อความเจ็บปวดเท่านั้น) → **50% glucose 50 mL IV push** ทันที แล้วต่อด้วย 10% D/W
- การยืนยันด้วย serum glucose ทำโดยเจาะ clot blood ไปพร้อมกัน ไม่ต้องรอผลก่อนรักษา
- NSS ไม่ได้แก้น้ำตาลต่ำ
- Insulin drip เป็นการรักษา DKA/HHS ทำให้แย่ลงอย่างรุนแรง
- 5% D/N/2 80 mL/hr ให้ glucose น้อยและช้าเกินไปสำหรับ CBG 26 ที่ซึม''',
            pearl="Severe hypoglycemia = 50% glucose 50 mL IV push", topic="Severe hypoglycemia",
            ref=[f"{D} หน้า 71, 79–80"], nl=["2.2.17", "B11.4(1)"]),
        mcq("ENDO-02-01-6",
            "A 75-year-old man with diabetes, hypertension and dyslipidemia is brought to the ER because he was found unresponsive 1 hour ago. This morning he had fever and myalgia and ate little. BT 37.8°C, BP 110/70 mmHg, PR 100/min, RR 24/min, SpO2 95%; lungs clear, examination otherwise normal. Capillary glucose is 40 mg/dL. What is the most appropriate immediate management?",
            "50% glucose IV push",
            ["0.9% NaCl loading", "Empirical IV antibiotics", "Endotracheal intubation", "Emergency CT brain"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ผู้ป่วยหมดสติ **CBG 40** → **severe hypoglycemia** ต้องแก้ทันทีด้วย **50% glucose 50 mL IV push** (trigger = ป่วยไข้ กินน้อยแต่ยังใช้ยาเบาหวาน)
- NSS: BP 110/70 ไม่ shock และไม่ได้แก้น้ำตาล
- Antibiotic อาจต้องให้ภายหลังเมื่อหาแหล่งติดเชื้อ แต่ไม่ใช่สิ่งแรก
- ใส่ท่อช่วยหายใจไม่จำเป็น — SpO2 95% หายใจได้ และจะตื่นเมื่อได้ glucose
- CT brain ทำเมื่อแก้น้ำตาลแล้วยังไม่ฟื้นหรือมี focal sign''',
            pearl="หมดสติ + CBG ต่ำ → glucose IV ก่อนทุกอย่าง", topic="Severe hypoglycemia",
            ref=[f"{D} หน้า 81–82"], nl=["2.2.17", "2.2.36"]),
        mcq("ENDO-02-01-5",
            "A 32-year-old nurse without diabetes has recurrent episodes of confusion. During an episode: plasma glucose 38 mg/dL, insulin markedly elevated, C-peptide undetectable, sulfonylurea screen negative. What is the most likely cause?",
            "Surreptitious injection of exogenous insulin",
            ["Insulinoma", "Sulfonylurea ingestion", "Adrenal insufficiency", "Non-islet cell tumor hypoglycemia"],
            explain='''Insulin ที่ฉีดจากภายนอกไม่มี C-peptide (C-peptide หลั่งพร้อม insulin จาก β-cell เท่านั้น) และ insulin จากภายนอกกด β-cell → **insulin สูง แต่ C-peptide ต่ำ = exogenous insulin** (factitious) พบในบุคลากรการแพทย์
- Insulinoma หลั่ง insulin เอง → **C-peptide และ proinsulin สูง** ด้วย
- Sulfonylurea กระตุ้น β-cell → C-peptide สูงและ SU screen บวก
- Adrenal insufficiency ทำให้ hypoglycemia โดย insulin ต่ำอย่างเหมาะสม
- Non-islet cell tumor (หลั่ง IGF-2) insulin และ C-peptide ต่ำทั้งคู่''',
            pearl="Insulin ↑ + C-peptide ↓ = ฉีด insulin เอง", topic="Hypoglycemia work-up",
            ref=[f"{D} หน้า 72"], nl=["2.2.17"]),
    ])

# ---------------------------------------------------------------- 02-02 DKA & HHS
S2 = sec("endo-02-02", "Hyperglycemic crises: DKA, euglycemic DKA และ HHS",
    "DKA = absolute insulin deficiency (T1) → ketone + acidosis เร็ว <24 ชม. · HHS = relative (T2) → glucose >600, Osm สูง ซึมช้าเป็นวัน · trigger 5I · urine ketone ลบไม่ตัด DKA → serum β-OHB", minutes=8,
    source=f"{D} หน้า 85–92, 101–102", nl=["2.2.16", "B11.2.5(5)"],
    md='''
### กลไก (สไลด์หน้า 85–86)
- **DKA = absolute insulin deficiency** (มักเป็น **T1DM**) → ไม่มี insulin ยับยั้ง lipolysis → free fatty acid ไปตับ → **ketone (β-hydroxybutyrate, acetoacetate)** → **high anion gap metabolic acidosis** + glucose สูง → osmotic diuresis
- **HHS = relative insulin deficiency** (มักเป็น **T2DM**) → insulin ที่เหลือ **ยังพอยับยั้ง lipolysis** → ketone น้อย แต่ glucose สูงมาก → **ขาดน้ำรุนแรง + hyperosmolality → ซึม**
- Counter-regulatory hormones (glucagon, cortisol, catecholamine) ↑ ทั้งสองภาวะ (เสริม)

### Trigger "5I" (สไลด์หน้า 87)
1. **Infection** — พบบ่อยที่สุด (pneumonia, UTI)
2. **Ignorance** — ขาดยา/หยุด insulin (non-compliance)
3. **Ischemia/infarction** — MI, stroke
4. **Intoxication** — alcohol
5. **Illness** อื่น ๆ — pancreatitis, ยา (steroid, SGLT2i) (เสริม)

### อาการ (สไลด์หน้า 88)
- ทั้งคู่: **polyuria polydipsia น้ำหนักลด** · คลื่นไส้อาเจียน · **ขาดน้ำ** · ซึม
- **เฉพาะ DKA**: เกิด **เร็ว < 24 ชม.** · **กลิ่นผลไม้** · **Kussmaul breathing** · **ปวดท้อง**
- **HHS**: ค่อยเป็นค่อยไป **หลายวัน** · ซึม/ชักมากกว่า

### เกณฑ์วินิจฉัย (สไลด์หน้า 89–92 เป็นภาพ — ตามเกณฑ์ ADA) (เสริม)

| | DKA | HHS |
|---|---|---|
| Glucose | **> 250** (consensus 2024: ≥ 200 หรือเคยเป็น DM) | **> 600 mg/dL** |
| pH | **≤ 7.30** | > 7.30 |
| HCO3 | **≤ 18** | > 18 (2024: ≥ 15) |
| Ketone | **บวก** (serum β-OHB ≥ 3 mmol/L) | น้อย/ลบ |
| Anion gap | **> 10–12** | แปรผัน |
| Effective Osm | แปรผัน | **> 320** (2024: > 300) |
| ความรู้สึกตัว | ตามความรุนแรง | **ซึม/โคม่า** บ่อย |

- Effective Osm = **2 × Na + glucose/18** · Corrected Na = Na + **1.6 × (glucose − 100)/100** (เสริม)
- ความรุนแรง DKA: mild pH 7.25–7.30 · moderate 7.00–7.24 · severe < 7.00 หรือซึม (เสริม)

> **Urine ketone (nitroprusside) ตรวจได้แค่ acetoacetate** ไม่เห็น **β-hydroxybutyrate** ซึ่งเป็น ketone หลักใน DKA รุนแรง → urine ketone ลบ/บวกน้อยแต่ wide AG acidosis → ส่ง **serum β-hydroxybutyrate**

### Euglycemic DKA (สไลด์หน้า 90)
- DKA ที่ **glucose < 250 mg/dL** — พบใน **SGLT2 inhibitor**, ตั้งครรภ์, อดอาหาร/กินน้อย, แอลกอฮอล์ (เสริม)
- หยุด SGLT2i, รักษาเหมือน DKA แต่ **ให้ dextrose ตั้งแต่แรก** ร่วมกับ insulin (สไลด์หน้า 94)

> DKA + ยา SGLT2i + น้ำตาลไม่สูงมาก → euglycemic DKA ตรวจ ketone ทุกรายที่ป่วยและใช้ SGLT2i
''',
    pearls=[
        "DKA = absolute insulin deficiency (T1) · HHS = relative (T2) ยังยับยั้ง lipolysis ได้",
        "Trigger 5I: infection (บ่อยสุด), ignorance, ischemia, intoxication, illness",
        "DKA: glucose >250, pH ≤7.3, HCO3 ≤18, ketone + · HHS: glucose >600, Osm >320",
        "Urine ketone ไม่เห็น β-OHB → wide AG แต่ urine ketone ลบ ให้ส่ง serum β-OHB",
        "SGLT2i → euglycemic DKA (glucose <250)",
    ],
    items=[
        mcq("ENDO-02-02-1",
            "A 60-year-old woman with poorly controlled diabetes presents with altered consciousness and hyperpnea. PR 100/min, RR 28/min, BP 120/80 mmHg. Blood glucose 500 mg/dL. ABG shows a high anion gap metabolic acidosis. Urinalysis: protein 4+, sugar 2+, ketone negative. What is the most appropriate investigation?",
            "Serum beta-hydroxybutyrate",
            ["Serum anion gap", "Serum electrolytes only", "Urine anion gap", "Urine electrolytes"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Wide AG metabolic acidosis + glucose สูง แต่ **urine ketone ลบ** — urine dipstick (nitroprusside) ตรวจได้เฉพาะ **acetoacetate** ส่วน DKA รุนแรง ketone ส่วนใหญ่เป็น **β-hydroxybutyrate** → ส่ง **serum β-OHB** ยืนยัน DKA
- Serum anion gap รู้แล้วว่ากว้าง ไม่ได้บอกสาเหตุ
- Serum electrolyte อย่างเดียวคำนวณ AG ได้แต่ไม่ได้ยืนยัน ketoacidosis
- Urine anion gap ใช้แยก **normal** AG metabolic acidosis (RTA vs diarrhea)
- Urine electrolytes ไม่ช่วยวินิจฉัย ketoacidosis''',
            pearl="Urine ketone ลบไม่ตัด DKA → serum β-OHB", topic="Ketone testing",
            ref=[f"{D} หน้า 101–102"], nl=["2.2.16", "B11.2.5(5)"]),
        mcq("ENDO-02-02-2",
            "A 54-year-old man with type 2 diabetes started empagliflozin 3 months ago. He presents with nausea, vomiting and abdominal pain after 3 days of poor intake. Glucose 190 mg/dL, pH 7.12, HCO3 9 mmol/L, anion gap 26, serum beta-hydroxybutyrate 6 mmol/L. What is the most likely diagnosis?",
            "Euglycemic diabetic ketoacidosis",
            ["Starvation ketosis", "Hyperosmolar hyperglycemic state", "Lactic acidosis from metformin", "Alcoholic ketoacidosis"],
            explain='''ใช้ **SGLT2 inhibitor** + กินน้อย → ketone สูงมาก (β-OHB 6) + **severe high AG acidosis** แต่ glucose **< 250** = **euglycemic DKA** · SGLT2i ขับ glucose ทางปัสสาวะ ทำให้ insulin ต่ำลงและ glucagon สูง → ketogenesis
- Starvation ketosis ทำให้ ketone สูงเล็กน้อยและ HCO3 มักไม่ต่ำกว่า 18
- HHS ต้องมี glucose > 600 และ ketone น้อย
- Metformin lactic acidosis จะมี lactate สูง ไม่ใช่ ketone สูง
- Alcoholic ketoacidosis ต้องมีประวัติดื่มหนัก และ glucose มักต่ำหรือปกติ ไม่มีประวัติ SGLT2i''',
            pearl="SGLT2i + กินน้อย + acidosis แม้ glucose ไม่สูง → euglycemic DKA", topic="Euglycemic DKA",
            ref=[f"{D} หน้า 13, 90"], nl=["2.2.16", "B11.4(1)"]),
        mcq("ENDO-02-02-3",
            "A 72-year-old woman with type 2 diabetes has had progressive drowsiness for 5 days with fever and dysuria. BP 96/60 mmHg, PR 116/min, RR 20/min, very dry mucosa. Glucose 920 mg/dL, Na 148, K 4.6, Cl 110, HCO3 22 mmol/L, BUN 60, Cr 2.1 mg/dL, serum ketone trace. What is the most likely diagnosis?",
            "Hyperosmolar hyperglycemic state",
            ["Diabetic ketoacidosis", "Euglycemic diabetic ketoacidosis", "Septic encephalopathy without metabolic derangement", "Central diabetes insipidus"],
            explain='''T2DM ผู้สูงอายุ + ติดเชื้อ (UTI) + ซึมลง **ค่อยเป็นหลายวัน** + glucose 920 + effective Osm = 2(148) + 920/18 ≈ **347** (> 320) + HCO3 22 และ ketone เพียง trace = **HHS**
- DKA ต้องมี acidosis (HCO3 ≤ 18) และ ketone สูง
- Euglycemic DKA มี glucose < 250
- Septic encephalopathy อาจร่วมด้วย แต่ hyperosmolality ระดับนี้อธิบายการซึมได้และต้องแก้ก่อน
- Central DI ทำให้ Na สูงและปัสสาวะมากแต่ glucose ไม่สูง''',
            pearl="T2 ผู้สูงอายุ ซึมหลายวัน glucose >600 Osm >320 ketone น้อย = HHS", topic="HHS diagnosis",
            ref=[f"{D} หน้า 86–88, 91"], nl=["2.2.16", "B11.2.5(5)"]),
    ])

# ---------------------------------------------------------------- 02-03 Management
F_DKA = fig("endo-02-03-f1", "DKA/HHS: fluid → K → insulin", '''<svg viewBox="0 0 750 560">
 <defs><marker id="endo-02-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="175" y="8" width="400" height="44" rx="10" class="badsoft"/>
 <text x="375" y="28" text-anchor="middle" class="tb">ABC ก่อน: O2 · ใส่ ETT ถ้า respiratory failure</text>
 <text x="375" y="44" text-anchor="middle" class="t3">หา trigger (5I) · เจาะ E'lyte, BUN/Cr, VBG, ketone, UA, H/C</text>
 <path d="M125 52V74" class="ln" marker-end="url(#endo-02-03-a)"/>
 <path d="M375 52V74" class="ln" marker-end="url(#endo-02-03-a)"/>
 <path d="M625 52V74" class="ln" marker-end="url(#endo-02-03-a)"/>
 <rect x="8" y="76" width="236" height="36" rx="8" class="c1"/>
 <text x="126" y="99" text-anchor="middle" class="tw">1 · IV fluid</text>
 <rect x="257" y="76" width="236" height="36" rx="8" class="miss"/>
 <text x="375" y="99" text-anchor="middle" class="tw">2 · Potassium</text>
 <rect x="506" y="76" width="236" height="36" rx="8" class="c2"/>
 <text x="624" y="99" text-anchor="middle" class="tw">3 · Insulin (RI IV)</text>
 <rect x="8" y="122" width="236" height="64" rx="8" class="c1soft"/>
 <text x="18" y="142" class="tb">Shock → NSS เต็มที่</text>
 <text x="18" y="162" class="t2">ไม่ shock: ชม.แรก NSS</text>
 <text x="18" y="178" class="t2">1,000–1,500 mL</text>
 <rect x="8" y="196" width="236" height="96" rx="8" class="box"/>
 <text x="18" y="216" class="tb">ต่อมาตาม corrected Na</text>
 <text x="18" y="238" class="t2">&lt; 135 → NSS</text>
 <text x="18" y="256" class="t2">≥ 135 → 0.45% NaCl</text>
 <text x="18" y="276" class="t3">250–500 mL/hr ตาม volume</text>
 <rect x="8" y="302" width="236" height="96" rx="8" class="box"/>
 <text x="18" y="322" class="tb">CBG ≤ 250 →</text>
 <text x="18" y="342" class="t2">5–10% D/N/2</text>
 <text x="18" y="360" class="t2">150–250 mL/hr</text>
 <text x="18" y="380" class="t3">หรือ two-bag method</text>
 <rect x="257" y="122" width="236" height="56" rx="8" class="badsoft"/>
 <text x="267" y="142" class="tb">K ≤ 3.3</text>
 <text x="267" y="162" class="t2">KCl 10–20 mEq/hr · งด insulin</text>
 <rect x="257" y="188" width="236" height="56" rx="8" class="misssoft"/>
 <text x="267" y="208" class="tb">K 3.3–5.2</text>
 <text x="267" y="228" class="t2">KCl 20–30 mEq/L + insulin</text>
 <rect x="257" y="254" width="236" height="56" rx="8" class="oksoft"/>
 <text x="267" y="274" class="tb">K ≥ 5.2</text>
 <text x="267" y="294" class="t2">ยังไม่ให้ K · ให้ insulin ได้</text>
 <rect x="257" y="320" width="236" height="78" rx="8" class="sunk"/>
 <text x="267" y="342" class="t2">ดู urine output ก่อนให้ KCl</text>
 <text x="267" y="362" class="t2">เจาะ K ซ้ำทุก 2–4 ชม.</text>
 <text x="267" y="382" class="t3">insulin ดัน K เข้าเซลล์</text>
 <rect x="506" y="122" width="236" height="88" rx="8" class="c2soft"/>
 <text x="516" y="142" class="t2">0.1 U/kg bolus + 0.1 U/kg/hr</text>
 <text x="516" y="162" class="t2">หรือ 0.14 U/kg/hr ไม่ bolus</text>
 <text x="516" y="182" class="t2">หรือ 0.1 U/kg/hr + basal เดิม</text>
 <text x="516" y="202" class="t3">(เลือกแบบใดแบบหนึ่ง)</text>
 <rect x="506" y="220" width="236" height="78" rx="8" class="box"/>
 <text x="516" y="240" class="tb">ให้ glucose ↓ 50–75 /ชม.</text>
 <text x="516" y="260" class="t2">ไม่ถึง → ↑ rate ≥ 1 U/hr</text>
 <text x="516" y="280" class="t2">CBG ≤ 250 → 0.02–0.05 U/kg/hr</text>
 <rect x="506" y="308" width="236" height="90" rx="8" class="box"/>
 <text x="516" y="328" class="tb">เป้า CBG 140–180</text>
 <text x="516" y="348" class="t2">จนหาย: AG ปิด, pH ≥ 7.3,</text>
 <text x="516" y="366" class="t2">HCO3 ≥ 18 (DKA)</text>
 <text x="516" y="386" class="t3">→ SC insulin overlap ก่อนหยุด IV</text>
 <rect x="8" y="414" width="734" height="62" rx="10" class="sunk"/>
 <text x="20" y="436" class="tb">NaHCO3</text>
 <text x="90" y="436" class="t2">เฉพาะ pH &lt; 6.9 หลังให้ fluid + insulin แล้ว</text>
 <text x="20" y="460" class="tb">Monitor</text>
 <text x="90" y="460" class="t2">CBG ทุก 1 ชม. · VBG, ketone, E'lyte, AG ทุก 2–4 ชม. · urine output</text>
 <rect x="8" y="486" width="734" height="64" rx="10" class="acsoft"/>
 <text x="20" y="510" class="tb">Euglycemic DKA</text>
 <text x="150" y="510" class="t2">ให้ dextrose ตั้งแต่แรกพร้อม insulin (กัน hypoglycemia)</text>
 <text x="20" y="534" class="tb">Transition</text>
 <text x="150" y="534" class="t2">ฉีด SC insulin ก่อนหยุด IV drip 30–60 นาที (แนวทางใหม่ 1–2 ชม.)</text>
</svg>''', "อ่านจากซ้ายไปขวาตามลำดับความสำคัญ — fluid ก่อนเสมอ, K ต้องรู้ค่าก่อนเริ่ม insulin, insulin ปรับตามอัตราการลดของน้ำตาล")

S3 = sec("endo-02-03", "Hyperglycemic crises: การรักษา (fluid → K → insulin)",
    "ABC → NSS 1–1.5 L ชม.แรก → ตาม corrected Na · K ≤3.3 ให้ K ก่อน insulin · RI 0.1 U/kg/hr · CBG ≤250 เติม dextrose · NaHCO3 เฉพาะ pH <6.9", minutes=10,
    source=f"{D} หน้า 93–112", nl=["2.2.16", "B11.2.5(5)", "B9.4(2)"],
    md='''
### ลำดับการรักษา (สไลด์หน้า 93–100)

[[fig:endo-02-03-f1]]

#### 0. Initial — ABC
- **O2**, **ใส่ ETT ถ้า respiratory failure** (เช่น pneumonia ที่ SpO2 ไม่ขึ้นแม้ให้ O2 เต็มที่)
- **Shock → isotonic saline (NSS)** เต็มที่ก่อน

#### 1. IV fluid
- ไม่ shock: **ชั่วโมงแรก NSS 1,000–1,500 mL**
- 24–48 ชม.ต่อมา ตาม **corrected Na**: **< 135 → NSS** · **≥ 135 → 0.45% NaCl** อัตรา **250–500 mL/hr**
- fluid อย่างเดียวลด CBG ได้ **50–80 mg/dL** (จาก dilution + ไตขับ glucose)
- **CBG ≤ 250 mg/dL** (HHS: ≤ 300 เสริม) → เปลี่ยนเป็น **5–10% D/N/2 150–250 mL/hr** หรือ **two-bag method** (ถุงที่ 1 NSS/0.45% NaCl, ถุงที่ 2 5–10% dextrose in NSS/0.45% NaCl ปรับสัดส่วนเพื่อคุม glucose) — เพื่อ **ให้ insulin ต่อจนหาย ketoacidosis โดยไม่เกิด hypoglycemia**
- **Euglycemic DKA ให้ dextrose ตั้งแต่แรก**

#### 2. Potassium (สไลด์หน้า 95)
- ผู้ป่วย DKA มี **total body K ต่ำ** แม้ serum K ปกติ/สูง (K ออกจากเซลล์จาก acidosis + insulin deficiency) — insulin จะดัน K เข้าเซลล์ → K ดิ่ง (เสริม)

| Serum K (mmol/L) | การให้ K | Insulin |
|---|---|---|
| **≤ 3.3** | **KCl 10–20 mEq/hr** (สไลด์: 40 mmol/L) | **งด insulin จนกว่า K > 3.3** (เสริม) |
| **3.3–5.2** | **KCl 20–30 mEq ต่อ fluid 1 L** | ให้ได้ |
| **≥ 5.2** | ยังไม่ต้องให้ K เจาะซ้ำ | ให้ได้เลย |

- **ตรวจ urine output ก่อนให้ KCl**

#### 3. Insulin (สไลด์หน้า 95–96) — เลือก 1 แบบ
- **RI 0.1 U/kg IV bolus → 0.1 U/kg/hr**
- หรือ **RI 0.14 U/kg/hr** ตั้งแต่แรก (ไม่ bolus)
- หรือ RI 0.1 U/kg/hr + basal insulin ขนาดเดิม
- **เป้า CBG 140–180 mg/dL** โดยให้ลด **50–75 mg/dL/hr** · ไม่ถึง → **เพิ่ม ≥ 1 U/hr**
- **CBG ≤ 250 → ลด RI เป็น 0.02–0.05 U/kg/hr** (ร่วมกับเติม dextrose)
- **DKA resolution** (เสริม): glucose < 200 + อย่างน้อย 2 ใน HCO3 ≥ 15–18, pH > 7.3, AG ≤ 12 (หรือ β-OHB < 0.6) · HHS: Osm ปกติ + รู้สึกตัวดี

#### อื่น ๆ
- **NaHCO3 เฉพาะ pH < 6.9** หลังให้ fluid และ insulin แล้ว
- **รักษา precipitating cause** (antibiotic, ฯลฯ)
- **Monitor**: clinical, urine output · **CBG ทุก 1 ชม.** · **venous pH, ketone, E'lyte, AG ทุก 2–4 ชม.**
- **Transition IV → SC**: ฉีด SC insulin **ก่อนหยุด IV drip 30–60 นาที** (overlap) — ADA 2024 แนะนำ 1–2 ชม. (เสริม) · หยุด IV ทันทีโดยไม่ overlap → rebound DKA

> **กับดัก**: (1) ให้ insulin ก่อน fluid ใน shock → BP ตก (2) ให้ insulin ทั้งที่ K < 3.3 → hypokalemia → arrhythmia (3) ไม่เติม dextrose เมื่อ CBG ≤ 250 → hypoglycemia (4) ลด glucose/Osm เร็วเกินในเด็ก → cerebral edema (เสริม)
''',
    figs=[F_DKA],
    pearls=[
        "ลำดับ: ABC → NSS → เช็ก K → insulin",
        "ชม.แรก NSS 1–1.5 L · ต่อไปตาม corrected Na (<135 NSS, ≥135 0.45%)",
        "K ≤3.3 → ให้ KCl และงด insulin · 3.3–5.2 → KCl 20–30 mEq/L + insulin",
        "RI 0.1 U/kg/hr · ลด 50–75/ชม. · CBG ≤250 → เติม dextrose + ลด RI",
        "NaHCO3 เฉพาะ pH <6.9 · overlap SC insulin ก่อนหยุด drip",
    ],
    items=[
        mcq("ENDO-02-03-1",
            "A 46-year-old woman with diabetes and hypertension has fever, cough and dyspnea. On a 100% oxygen mask with reservoir bag, SpO2 is 90% and she is tiring. ABG: pH 7.22, PaO2 65 mmHg, PaCO2 26 mmHg. Blood glucose 487 mg/dL. What is the most appropriate immediate management?",
            "Endotracheal intubation",
            ["IV sodium bicarbonate", "IV regular insulin infusion", "Nebulized salbutamol", "0.45% NaCl infusion"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ภาวะวิกฤตทุกชนิดเริ่มที่ **ABC** — SpO2 90% ทั้งที่ใช้ mask with bag 100% และเหนื่อยล้า = **hypoxemic respiratory failure** (น่าจะ pneumonia เป็น trigger ของ DKA) → **ใส่ท่อช่วยหายใจ** ก่อน
- NaHCO3 ไม่ได้ข้อบ่งชี้ (pH 7.22 > 6.9)
- Insulin สำคัญแต่ทำหลังแก้ airway/breathing และหลังให้ fluid
- Salbutamol ไม่ได้แก้ปัญหา pneumonia/ARDS ที่ไม่มี bronchospasm
- 0.45% NaCl ไม่ใช่ fluid เริ่มต้น และไม่ได้แก้ภาวะหายใจล้มเหลว''',
            pearl="Hyperglycemic crisis ก็ต้อง ABC ก่อน", topic="ABC first",
            ref=[f"{D} หน้า 93, 103–104"], nl=["2.2.16", "2.2.9"]),
        mcq("ENDO-02-03-2",
            "A 70-year-old woman with type 2 diabetes has had fever, cloudy urine, left flank pain and decreasing consciousness for 4 days; her family stopped her diabetes medication. BT 38°C, BP 80/50 mmHg, PR 110/min, RR 28/min, left CVA tenderness. Glucose 900 mg/dL, BUN 40, Cr 2.0 mg/dL, electrolytes normal. What is the most appropriate initial management?",
            "0.9% NaCl IV bolus",
            ["Gentamicin IV", "NPH insulin subcutaneously", "Regular insulin subcutaneously", "Regular insulin IV infusion"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''HHS + **shock** (BP 80/50) จาก severe dehydration ร่วมกับ pyelonephritis → **สิ่งแรกคือ resuscitation ด้วย isotonic saline (0.9% NaCl)** fluid อย่างเดียวยังลดน้ำตาลได้ 50–80 mg/dL
- Antibiotic จำเป็นและควรให้เร็ว แต่ gentamicin เป็นพิษต่อไตในผู้ที่มี AKI และไม่ใช่สิ่งแรกก่อนแก้ shock
- NPH และ RI ใต้ผิวหนังดูดซึมไม่แน่นอนในภาวะ shock
- RI IV ให้หลัง fluid — ให้ก่อนจะดึงน้ำเข้าเซลล์ตาม glucose ทำให้ความดันตกมากขึ้น''',
            pearl="Shock + hyperglycemic crisis → NSS ก่อน insulin", topic="Fluid first",
            ref=[f"{D} หน้า 93, 105–106"], nl=["2.2.16", "2.2.7"]),
        mcq("ENDO-02-03-3",
            "A 30-year-old man with diabetes presents with dyspnea and polyuria. BP 80/60 mmHg, PR 120/min. Glucose 500 mg/dL; Na 128, K 4.8, Cl 100, HCO3 8 mmol/L. What is the most appropriate initial management?",
            "0.9% NaCl IV loading",
            ["Regular insulin IV loading", "7.5% NaHCO3 IV", "KCl IV", "0.45% NaCl at 250 mL/hr"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''DKA (AG = 128 − 108 = 20, HCO3 8) + **hypotension** → เริ่ม **NSS loading** ก่อน
- Insulin ให้ตามหลัง fluid และหลังรู้ K (K 4.8 ให้ได้) แต่ไม่ใช่ขั้นแรกในผู้ป่วยความดันต่ำ
- NaHCO3 ใช้เมื่อ pH < 6.9 หลังให้ fluid + insulin แล้ว
- KCl ยังไม่จำเป็นตอน K 4.8 และยังไม่รู้ urine output — จะเริ่มเมื่อ K < 5.2 พร้อม insulin
- 0.45% NaCl เป็น hypotonic ไม่เหมาะ resuscitate shock และ corrected Na ≈ 134 ยังต่ำกว่า 135 ควรใช้ NSS''',
            pearl="DKA + BP ต่ำ → NSS loading เป็นขั้นแรก", topic="Initial fluid",
            ref=[f"{D} หน้า 93, 107–108"], nl=["2.2.16"]),
        mcq("ENDO-02-03-4",
            "A 25-year-old man has polyuria and polydipsia for 3 weeks and deep, rapid breathing. BP 118/72 mmHg. Glucose 300 mg/dL, Na 130, K 2.5 mmol/L, serum ketone 8 mmol/L. He is passing urine. What is the most appropriate initial management?",
            "0.9% NaCl with IV KCl, withholding insulin until K is above 3.3",
            ["Regular insulin 0.1 U/kg IV bolus, then add KCl", "IV sodium bicarbonate", "Potassium phosphate alone without fluid", "0.9% NaCl and regular insulin infusion together immediately"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''DKA ไม่ shock → **NSS ในชั่วโมงแรก** และเพราะ **K 2.5 (≤ 3.3)** ต้อง **ให้ KCl 10–20 mEq/hr ก่อน และงด insulin** จน K > 3.3 (สไลด์: "ถ้ารู้ผล K แล้วก็ควรแก้ KCl ด้วย")
- ให้ insulin ก่อน → K ถูกดันเข้าเซลล์ → hypokalemia รุนแรง หัวใจเต้นผิดจังหวะ/หายใจล้มเหลว
- NaHCO3 ไม่ได้ข้อบ่งชี้ และยิ่งทำให้ K ต่ำลง
- Potassium phosphate อย่างเดียวไม่ได้แก้ภาวะขาดน้ำ ใช้เฉพาะเมื่อ PO4 < 1.0 mg/dL หรือมีภาวะแทรกซ้อน
- เริ่ม insulin พร้อม NSS ทันทีผิดเพราะ K ยังต่ำกว่า 3.3''',
            pearl="K ≤3.3 → KCl ก่อน งด insulin", topic="Potassium rule",
            ref=[f"{D} หน้า 95, 109–110"], nl=["2.2.16", "2.2.15", "B9.4(2)"]),
        mcq("ENDO-02-03-5",
            "A 22-year-old man has nausea, vomiting and severe fatigue for 2 days. BP 80/60 mmHg, PR 140/min, RR 32/min, drowsy and dehydrated. After 1,000 mL of 0.9% NaCl, BP is 100/70 mmHg. Glucose 850 mg/dL, Na 129, K 2.8, Cl 90, HCO3 10, PO4 4.2 mg/dL, BUN 42, Cr 1.2 mg/dL. What is the most appropriate next step?",
            "Continue 0.9% NaCl and add KCl",
            ["Start regular insulin infusion now", "Add potassium phosphate", "Give IV sodium bicarbonate", "Switch to 5% D/N/2"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''หลัง NSS 1 L ความดันดีขึ้นแต่ยังขาดน้ำ → **ให้ NSS ต่อ** (corrected Na ≈ 129 + 1.6 × 7.5 ≈ 141 แต่ยังอยู่ช่วง resuscitation) และ **K 2.8 < 3.3 → เติม KCl ก่อน** แล้วค่อยเริ่ม insulin เมื่อ K > 3.3
- เริ่ม insulin ตอน K 2.8 อันตราย
- Phosphate 4.2 ปกติ ไม่ต้องให้ K-phosphate
- NaHCO3 ใช้เมื่อ pH < 6.9
- Dextrose เติมเมื่อ CBG ≤ 250 แต่ตอนนี้ 850''',
            pearl="หลัง bolus แล้ว K <3.3 → NSS ต่อ + KCl ก่อน insulin", topic="Next step",
            ref=[f"{D} หน้า 93–96, 111–112"], nl=["2.2.16", "2.2.15"]),
        mcq("ENDO-02-03-6",
            "A 19-year-old woman with type 1 diabetes is on an IV regular insulin infusion at 0.1 U/kg/hr for DKA. After 6 hours: glucose 240 mg/dL, pH 7.21, HCO3 12 mmol/L, anion gap 20, K 4.1 mmol/L. What is the most appropriate adjustment?",
            "Add 5–10% dextrose to IV fluid and reduce insulin to 0.02–0.05 U/kg/hr",
            ["Stop the insulin infusion and start subcutaneous insulin", "Keep the same insulin rate and fluid without dextrose", "Increase insulin to 0.2 U/kg/hr", "Give IV sodium bicarbonate"],
            explain='''CBG ลงถึง **≤ 250** แต่ **ketoacidosis ยังไม่หาย** (pH 7.21, AG 20) → ต้อง **ให้ insulin ต่อเพื่อหยุด ketogenesis** และป้องกัน hypoglycemia ด้วย **การเติม dextrose + ลด RI เป็น 0.02–0.05 U/kg/hr**
- หยุด insulin drip ตอนนี้ทำให้ DKA กลับเป็นซ้ำ — เปลี่ยนเป็น SC เมื่อ DKA หาย (AG ปิด pH > 7.3) และต้อง overlap
- คงอัตราเดิมโดยไม่มี dextrose จะเกิด hypoglycemia
- เพิ่ม insulin ทำให้น้ำตาลดิ่งและ K ต่ำ
- NaHCO3 ไม่ได้ข้อบ่งชี้ (pH > 6.9)''',
            pearl="CBG ≤250 แต่ AG ยังไม่ปิด → dextrose + ลด RI ไม่ใช่หยุด", topic="Dextrose when CBG ≤250",
            ref=[f"{D} หน้า 94, 96"], nl=["2.2.16"]),
    ])

LECTURE = lecture("02", "Hypoglycemia & hyperglycemic crises", "hypoglycemia · DKA · euglycemic DKA · HHS",
    objectives=[
        "วินิจฉัยและรักษา hypoglycemia ตามความรุนแรง รวมถึงการให้ thiamine",
        "แปลผล insulin/C-peptide เพื่อหาสาเหตุ hypoglycemia ในคนไม่เป็นเบาหวาน",
        "แยก DKA, euglycemic DKA และ HHS จากอาการและค่า lab",
        "สั่งการรักษา hyperglycemic crisis ตามลำดับ fluid → K → insulin และรู้ข้อบ่งชี้ NaHCO3",
    ],
    sections=[S1, S2, S3])
