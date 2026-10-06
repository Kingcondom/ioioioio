from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Nephro"

# ---------------------------------------------------------------- 04-01 CKD dx
F_STAGE = fig("nephro-04-01-f1", "CKD staging: GFR (G) × albuminuria (A)", '''<svg viewBox="0 0 740 330">
 <text x="250" y="22" text-anchor="middle" class="tb">GFR category (mL/min/1.73 m²)</text>
 <text x="620" y="22" text-anchor="middle" class="tb">Albuminuria (UACR mg/g)</text>
 <rect x="20" y="36" width="70" height="38" rx="6" class="oksoft"/><text x="55" y="60" text-anchor="middle" class="tb">G1</text>
 <rect x="96" y="36" width="380" height="38" rx="6" class="oksoft"/><text x="108" y="60" class="t2">≥ 90 · ปกติ/สูง (ต้องมี kidney damage)</text>
 <rect x="20" y="80" width="70" height="38" rx="6" class="oksoft"/><text x="55" y="104" text-anchor="middle" class="tb">G2</text>
 <rect x="96" y="80" width="380" height="38" rx="6" class="oksoft"/><text x="108" y="104" class="t2">60–89 · ลดลงเล็กน้อย</text>
 <rect x="20" y="124" width="70" height="38" rx="6" class="misssoft"/><text x="55" y="148" text-anchor="middle" class="tb">G3a</text>
 <rect x="96" y="124" width="380" height="38" rx="6" class="misssoft"/><text x="108" y="148" class="t2">45–59 · ต่ำกว่า 60 = CKD ได้เลย</text>
 <rect x="20" y="168" width="70" height="38" rx="6" class="misssoft"/><text x="55" y="192" text-anchor="middle" class="tb">G3b</text>
 <rect x="96" y="168" width="380" height="38" rx="6" class="misssoft"/><text x="108" y="192" class="t2">30–44</text>
 <rect x="20" y="212" width="70" height="38" rx="6" class="badsoft"/><text x="55" y="236" text-anchor="middle" class="tb">G4</text>
 <rect x="96" y="212" width="380" height="38" rx="6" class="badsoft"/><text x="108" y="236" class="t2">15–29 · เริ่มให้คำแนะนำเรื่อง RRT</text>
 <rect x="20" y="256" width="70" height="38" rx="6" class="bad"/><text x="55" y="280" text-anchor="middle" class="tw">G5</text>
 <rect x="96" y="256" width="380" height="38" rx="6" class="badsoft"/><text x="108" y="280" class="t2">&lt; 15 · kidney failure (ESRD เมื่อได้ RRT)</text>
 <rect x="510" y="36" width="70" height="78" rx="6" class="oksoft"/><text x="545" y="80" text-anchor="middle" class="tb">A1</text>
 <rect x="586" y="36" width="140" height="78" rx="6" class="oksoft"/><text x="598" y="72" class="t2">&lt; 30</text><text x="598" y="92" class="t3">ปกติ</text>
 <rect x="510" y="124" width="70" height="78" rx="6" class="misssoft"/><text x="545" y="168" text-anchor="middle" class="tb">A2</text>
 <rect x="586" y="124" width="140" height="78" rx="6" class="misssoft"/><text x="598" y="160" class="t2">30–300</text><text x="598" y="180" class="t3">micro (เดิม)</text>
 <rect x="510" y="212" width="70" height="82" rx="6" class="badsoft"/><text x="545" y="258" text-anchor="middle" class="tb">A3</text>
 <rect x="586" y="212" width="140" height="82" rx="6" class="badsoft"/><text x="598" y="250" class="t2">&gt; 300</text><text x="598" y="270" class="t3">macro (เดิม)</text>
 <text x="370" y="318" text-anchor="middle" class="t3">ต้องผิดปกตินานกว่า 3 เดือน · เขียนรวมเช่น "CKD G3b A3" (เสริม: ตารางในสไลด์เป็นภาพ)</text>
</svg>''', "ซ้ายคือระดับ GFR หกขั้น ขวาคือระดับ albuminuria สามขั้น สีเข้มขึ้นแปลว่าเสี่ยงไตวายและโรคหัวใจมากขึ้น")

S1 = sec("nephro-04-01", "CKD: นิยาม สาเหตุ อาการ และการส่งตรวจ",
    "GFR <60 หรือ kidney damage >3 เดือน · DM > HT > GN · ESRD = GFR <15 + RRT", minutes=7,
    source=f"{D} หน้า 142–146", nl=["2.3.14(3)", "B9.2.7(2)", "B9.3(4)"],
    md='''
### สาเหตุ

1. **Diabetic nephropathy** (อันดับ 1)
2. **Hypertensive nephropathy**
3. **Glomerulonephritis**
4. อื่น ๆ: obstructive nephropathy, chronic analgesic misuse, polycystic kidney disease, amyloidosis

### นิยาม CKD — ข้อใดข้อหนึ่ง **นานกว่า 3 เดือน**

- **GFR < 60 mL/min/1.73 m²** หรือ
- **Kidney damage ≥ 1 ข้อ**
  - Albuminuria (**UACR ≥ 30 mg/g**)
  - Abnormal urine sediment (RBC, WBC/RBC cast, **broad waxy cast**)
  - Abnormal electrolyte (↑K, ↓Ca, ↑PO4) จาก tubular disorder
  - U/S ผิดปกติ (**thin cortex, ↓kidney size, hyperechoic, cyst**)
  - Renal biopsy ผิดปกติ
  - เคยปลูกถ่ายไต

### Staging

[[fig:nephro-04-01-f1]]

- **ESRD = GFR < 15 + ได้ RRT**

### อาการ

- **Early stages: asymptomatic** (ต้องคัดกรองในกลุ่มเสี่ยง DM/HT)
- **Late stages**
  - Nocturia (เข้มข้นปัสสาวะไม่ได้), oliguria
  - Hematuria, foamy urine
  - ↑BP, peripheral edema, pulmonary edema
  - Fatigue, N/V, pruritus (uremia)
  - **Uremic pericarditis/pleuritis** (เจ็บหน้าอก)
  - **Uremic encephalopathy** (AOC, seizure)
  - **Anemia, ↑bleeding risk** (↓platelet adhesion — uremic platelet dysfunction)

### Investigation

- BUN, Cr, CBC, electrolyte
- UA, UPCR, UACR
- **KUB ultrasound** (ไตเล็ก cortex บาง = เรื้อรัง)
- หาสาเหตุตามที่สงสัย: DM → FBS, HbA1c · GN → ANA, ANCA, anti-GBM, complement · multiple myeloma → SPEP
- **Renal biopsy มักไม่จำเป็น** ทำเมื่อ **GFR ลดลงเร็ว** หรือต้อง confirm สาเหตุ (เช่น GN)

> AKI vs CKD: ไตเล็ก + ซีด + Ca ต่ำ PO4 สูง + broad waxy cast = เรื้อรัง (ข้อยกเว้นไตไม่เล็ก: DM, amyloid, PKD, HIVAN (เสริม))
''',
    figs=[F_STAGE],
    pearls=[
        "CKD = GFR <60 หรือ kidney damage (UACR ≥30, sediment, imaging) นานกว่า 3 เดือน",
        "สาเหตุ CKD: DM > HT > GN",
        "ESRD = GFR <15 + RRT · เริ่มคุยเรื่อง RRT ตั้งแต่ CKD G4",
        "U/S ไตเล็ก cortex บาง = เรื้อรัง (ยกเว้น DM, amyloid, PKD, HIV ไตไม่เล็ก)",
    ],
    items=[
        mcq("NEPHRO-04-01-1",
            "A 58-year-old man with hypertension has an eGFR of 52 mL/min/1.73 m2 and a urine albumin-to-creatinine ratio of 45 mg/g, both confirmed on repeat testing 4 months later. Urinalysis is otherwise unremarkable. How should his kidney status be classified?",
            "CKD G3a A2",
            ["CKD G2 A1", "CKD G3b A3", "Acute kidney injury stage 1", "Normal kidney function for age"],
            explain='''eGFR 52 อยู่ในช่วง **45–59 = G3a** และ UACR 45 อยู่ในช่วง **30–300 = A2** และผิดปกติ **นานกว่า 3 เดือน** จึงเป็น CKD G3a A2
- G2 คือ GFR 60–89 และ A1 คือ UACR < 30
- G3b คือ 30–44 และ A3 คือ > 300
- AKI ต้องมี Cr ขึ้นเฉียบพลันใน 48 ชั่วโมง–7 วัน ไม่ใช่ค่าคงที่นานหลายเดือน
- GFR < 60 นาน 3 เดือนเป็น CKD ไม่ว่าอายุเท่าไร''',
            pearl="CKD = ผิดปกติ >3 เดือน · G3a 45–59 · A2 30–300", topic="CKD staging",
            ref=[f"{D} หน้า 143–144"], nl=["B9.2.7(2)"]),
        mcq("NEPHRO-04-01-2",
            "A 66-year-old woman is found to have Cr 3.4 mg/dL on routine testing; no previous results are available. Which finding most strongly favors chronic kidney disease over acute kidney injury?",
            "Bilateral small kidneys (8 cm) with thin, echogenic cortex on ultrasound",
            ["Urine output 0.3 mL/kg/hr for 8 hours", "Muddy brown granular casts", "FENa of 0.5%", "Potassium of 5.6 mEq/L"],
            explain='''ไตเล็กทั้งสองข้าง cortex บาง echogenic = เนื้อไตฝ่อจากโรคเรื้อรัง เป็นหนึ่งใน kidney damage ตามนิยาม CKD
- Oliguria บอกความรุนแรงของ AKI ไม่ได้บอกความเรื้อรัง
- Muddy brown cast บอก ATN (เฉียบพลัน)
- FENa < 1% บอก prerenal
- K สูงพบได้ทั้ง AKI และ CKD''',
            pearl="ไตเล็ก cortex บาง = CKD", topic="AKI vs CKD",
            ref=[f"{D} หน้า 143"], nl=["B9.2.7(2)"]),
        mcq("NEPHRO-04-01-3",
            "A 61-year-old man with long-standing diabetes and CKD stage 5 (not on dialysis) presents with chest pain that improves on leaning forward. BUN 160 mg/dL, Cr 11 mg/dL. A pericardial friction rub is heard. ECG shows diffuse ST elevation. What is the most appropriate treatment?",
            "Initiate hemodialysis",
            ["High-dose aspirin", "Oral colchicine and ibuprofen", "Emergency coronary angiography", "Intravenous heparin"],
            explain='''CKD ระยะท้าย + BUN สูงมาก + เจ็บหน้าอกดีขึ้นเมื่อโน้มตัวไปข้างหน้า + friction rub = **uremic pericarditis** ซึ่งเป็นข้อบ่งชี้เริ่ม **dialysis** (สไลด์: uremic pericarditis เป็นข้อบ่งชี้ RRT)
- Aspirin, NSAID และ colchicine เป็นการรักษา viral/idiopathic pericarditis — NSAID ทำไตแย่ลงและเลือดออกง่ายใน uremia
- Coronary angiography ใช้ contrast และอาการไม่ใช่ ACS
- Heparin เพิ่มความเสี่ยง hemorrhagic pericardial effusion/tamponade''',
            pearl="Uremic pericarditis → dialysis", topic="Uremic complications",
            ref=[f"{D} หน้า 145, 152"], nl=["2.3.14(3)"]),
    ])

# ---------------------------------------------------------------- 04-02 CKD management
S2 = sec("nephro-04-02", "CKD management: ชะลอโรค ป้องกัน ASCVD และ RRT",
    "ACEI/ARB + SGLT2i · low protein/Na · statin · bicarbonate เมื่อ HCO3 <22 · RRT เมื่อแก้ด้วยยาไม่ได้", minutes=7,
    source=f"{D} หน้า 147–149, 151–152", nl=["2.3.14(3)", "B9.2.7(2)"],
    md='''
### 5 หัวข้อของการดูแล CKD

1. Tx underlying cause
2. Slow CKD progression
3. Primary prevention of ASCVD
4. Treat complications
5. Renal replacement therapy (RRT)

### Slow CKD progression

- **ACEI/ARB** (โดยเฉพาะเมื่อมี albuminuria) — Cr ขึ้นได้ไม่เกินราว 30% หลังเริ่มยาถือว่ายอมรับได้ (เสริม)
- **SGLT2i**
- Nutrition: **low protein, low Na diet**
- LSM: exercise, weight loss, smoking cessation
- **Avoid nephrotoxic drugs** (NSAID, contrast, aminoglycoside) และปรับขนาดยาตาม GFR

### Primary prevention of ASCVD

- HT: **ACEI/ARB**
- DM: **metformin** (ปรับ/หยุดเมื่อ eGFR < 30 (เสริม)), **SGLT2i**
- DLP: **statins**

### Treat complications (บางส่วน — รายละเอียดอยู่หัวข้อถัดไป)

| ปัญหา | การรักษา |
|---|---|
| Metabolic acidosis | **NaHCO3 เมื่อ HCO3 < 22** → keep 22–26 mEq/L |
| Anemia | แก้ IDA ก่อน → **ESA เมื่อ Hb < 10**, keep Hb 11–12 g/dL |
| CKD-MBD | Low PO4 diet, phosphate binder, vitamin D |
| Hyperkalemia | **Low K diet** (+ หยุดยาที่ทำ K สูงถ้าจำเป็น) |
| Volume overload | **Na & fluid restriction, diuretics** |
| Infection | Vaccine: **HBV, influenza, COVID, pneumococcal** |
| Malignancy | Screening ตามกลุ่มอายุ |

### Renal replacement therapy

- **ให้คำแนะนำตั้งแต่ CKD stage 4** (เตรียม vascular access ล่วงหน้า (เสริม))
- ทางเลือก: **hemodialysis, peritoneal dialysis, kidney transplant**
- เริ่มเมื่อ **failed medication** to control:
  - Volume overload/HT
  - Metabolic acidosis
  - Hyperkalemia
  - **Uremic pericarditis**
  - **Uremic encephalopathy**

> GFR ตัวเลขเดียวไม่ใช่ข้อบ่งชี้เริ่ม dialysis — ต้องมีอาการ/ภาวะที่แก้ด้วยยาไม่ได้ (เสริม)
''',
    pearls=[
        "ชะลอ CKD: ACEI/ARB + SGLT2i + low protein/low Na + หลีกเลี่ยง nephrotoxin",
        "CKD acidosis: NaHCO3 เมื่อ HCO3 <22 ให้อยู่ 22–26",
        "วัคซีน CKD: HBV, influenza, COVID, pneumococcal",
        "เตรียม RRT ตั้งแต่ CKD G4 · เริ่มเมื่อ volume/acidosis/K/uremia ดื้อยา",
    ],
    items=[
        mcq("NEPHRO-04-02-1",
            "A 60-year-old man with type 2 diabetes and CKD (eGFR 38 mL/min/1.73 m2, UACR 650 mg/g) is on maximum-dose losartan. BP 128/78 mmHg, HbA1c 7.2%. Which additional drug most effectively slows progression of his CKD?",
            "Empagliflozin",
            ["Glipizide", "Ibuprofen", "Hydralazine", "Allopurinol"],
            explain='''สไลด์: slow CKD progression = **ACEI/ARB + SGLT2i** ผู้ป่วยได้ ARB เต็มขนาดแล้ว จึงเพิ่ม **SGLT2 inhibitor (empagliflozin)** ซึ่งลด intraglomerular pressure ลด albuminuria และลดการเกิด ESRD
- Glipizide คุมน้ำตาลได้แต่ไม่ปกป้องไต และเสี่ยง hypoglycemia ใน CKD
- Ibuprofen เป็น nephrotoxin
- Hydralazine ลดความดันได้แต่ BP คุมได้แล้วและไม่ลด proteinuria
- Allopurinol ไม่ได้ชะลอ CKD ในการศึกษาใหญ่''',
            pearl="CKD + albuminuria: ACEI/ARB + SGLT2i", topic="Slow CKD progression",
            ref=[f"{D} หน้า 148–149"], nl=["2.3.14(3)"]),
        mcq("NEPHRO-04-02-2",
            "A 67-year-old woman has CKD stage 4 (eGFR 24). Venous HCO3 is 18 mEq/L on two occasions; she has no edema. What is the most appropriate management of her acid–base status?",
            "Oral sodium bicarbonate to keep HCO3 22–26 mEq/L",
            ["No treatment until HCO3 falls below 12 mEq/L", "Start hemodialysis immediately", "Intravenous 7.5% sodium bicarbonate bolus", "Acetazolamide"],
            explain='''สไลด์: CKD acidosis ให้ **NaHCO3 เมื่อ HCO3 < 22** และ keep **22–26 mEq/L** เพื่อลดการสลายกล้ามเนื้อ/กระดูกและชะลอโรค
- รอจนต่ำมากทำให้เกิดผลเสียต่อกระดูกและกล้ามเนื้อ
- Dialysis ใช้เมื่อ acidosis ดื้อต่อการรักษาด้วยยา
- IV bicarbonate bolus ใช้ในภาวะเฉียบพลันรุนแรง ไม่ใช่ chronic CKD
- Acetazolamide ทำให้เสีย HCO3 ทางปัสสาวะ ทำให้ acidosis แย่ลง''',
            pearl="CKD + HCO3 <22 → oral NaHCO3 (เป้า 22–26)", topic="CKD acidosis",
            ref=[f"{D} หน้า 150"], nl=["2.3.14(3)", "B9.4(2)"]),
        mcq("NEPHRO-04-02-3",
            "A 45-year-old man with CKD stage 4 due to IgA nephropathy asks about vaccines. He has never been vaccinated against hepatitis B. Which vaccination plan is most appropriate?",
            "Hepatitis B, influenza, COVID-19, and pneumococcal vaccines",
            ["No vaccines because CKD patients respond poorly", "Live attenuated influenza vaccine only", "Pneumococcal vaccine only after starting dialysis", "BCG vaccine"],
            explain='''สไลด์ระบุวัคซีนใน CKD: **HBV, influenza, COVID, pneumococcal** — HBV สำคัญเพราะอาจต้อง hemodialysis และควรฉีดตั้งแต่ GFR ยังดีเพราะตอบสนองดีกว่า
- ผู้ป่วย CKD ตอบสนองน้อยกว่าคนปกติแต่ยังได้ประโยชน์ (บางครั้งใช้ขนาดสูง)
- Influenza ควรใช้ชนิด inactivated
- รอจนเริ่ม dialysis ทำให้เสียโอกาส
- BCG ไม่ใช่วัคซีนที่แนะนำในผู้ใหญ่ CKD''',
            pearl="CKD: วัคซีน HBV, influenza, COVID, pneumococcal", topic="CKD vaccination",
            ref=[f"{D} หน้า 151"], nl=["2.3.14(3)"]),
    ])

# ---------------------------------------------------------------- 04-03 Anemia & MBD
F_MBD = fig("nephro-04-03-f1", "กลไก CKD-mineral bone disorder", '''<svg viewBox="0 0 740 300">
 <defs><marker id="nephro-04-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="270" y="10" width="200" height="40" rx="10" class="bad"/>
 <text x="370" y="35" text-anchor="middle" class="tw">GFR ลดลง</text>
 <path d="M320 50L170 88" class="ln" marker-end="url(#nephro-04-03-a)"/>
 <path d="M420 50L570 88" class="ln" marker-end="url(#nephro-04-03-a)"/>
 <rect x="60" y="90" width="220" height="48" rx="10" class="misssoft"/>
 <text x="170" y="112" text-anchor="middle" class="tb">ขับ PO4 ไม่ได้</text>
 <text x="170" y="130" text-anchor="middle" class="t3">↑PO4 → จับ Ca</text>
 <rect x="460" y="90" width="220" height="48" rx="10" class="misssoft"/>
 <text x="570" y="112" text-anchor="middle" class="tb">1α-hydroxylase ลด</text>
 <text x="570" y="130" text-anchor="middle" class="t3">↓calcitriol → ดูด Ca ลด</text>
 <path d="M170 138L320 176" class="ln" marker-end="url(#nephro-04-03-a)"/>
 <path d="M570 138L420 176" class="ln" marker-end="url(#nephro-04-03-a)"/>
 <rect x="270" y="178" width="200" height="40" rx="10" class="c2soft"/>
 <text x="370" y="203" text-anchor="middle" class="tb">↓Ca</text>
 <path d="M370 218V238" class="ln" marker-end="url(#nephro-04-03-a)"/>
 <rect x="220" y="240" width="300" height="50" rx="10" class="c2"/>
 <text x="370" y="262" text-anchor="middle" class="tw">↑PTH (secondary HPT)</text>
 <text x="370" y="280" text-anchor="middle" class="tw">ดึง Ca จากกระดูก → renal osteodystrophy</text>
 <rect x="20" y="170" width="190" height="120" rx="10" class="oksoft"/>
 <text x="32" y="192" class="tb">แก้ที่ PO4</text>
 <text x="32" y="212" class="t2">งดอาหาร PO4 สูง</text>
 <text x="32" y="232" class="t2">Phosphate binder</text>
 <text x="32" y="250" class="t3">CaCO3, sevelamer,</text>
 <text x="32" y="268" class="t3">lanthanum, Al(OH)3</text>
 <rect x="530" y="170" width="190" height="120" rx="10" class="oksoft"/>
 <text x="542" y="192" class="tb">แก้ที่ vitamin D</text>
 <text x="542" y="212" class="t2">Vitamin D</text>
 <text x="542" y="232" class="t2">(calcitriol)</text>
 <text x="542" y="250" class="t3">ระวัง Ca และ PO4</text>
 <text x="542" y="268" class="t3">สูงขึ้นตาม</text>
</svg>''', "GFR ลดทำให้ PO4 คั่งและ calcitriol ลด ทั้งสองทางทำให้ Ca ต่ำ PTH จึงสูง กล่องเขียวคือจุดที่ยาเข้าไปแก้")

S3 = sec("nephro-04-03", "CKD complications: anemia & CKD-MBD",
    "แก้ IDA ก่อน → ESA เมื่อ Hb <10 (เป้า 11–12) · ↑PO4 ↓Ca ↑PTH → low PO4 diet + phosphate binder + vit D", minutes=7,
    source=f"{D} หน้า 150, 153–156", nl=["2.3.14(3)", "B9.1.2(8)", "B2.4(4)"],
    md='''
### Anemia of CKD

- กลไก: ไตสร้าง **erythropoietin (EPO) ลดลง** + ขาดเหล็ก + uremia กดไขกระดูก (เสริม)
- Normocytic normochromic anemia มักเริ่มเด่นเมื่อ GFR < 30–45 (เสริม)
- แนวทาง (ตามสไลด์)
  1. **Work up anemia และแก้ IDA ก่อน** (เป้า ferritin > 100–200, TSAT > 20% (เสริม))
  2. ถ้ายัง **Hb < 10 g/dL → ESA** (erythropoiesis-stimulating agent — erythropoietin)
  3. **Keep Hb 11–12 g/dL** (สูงเกิน 13 เพิ่ม stroke/thrombosis (เสริม))

### CKD–mineral bone disorder (CKD-MBD)

[[fig:nephro-04-03-f1]]

ลักษณะ: **↑PO4, ↓Ca, ↑PTH, ↓vitamin D**

การรักษา (ตามสไลด์)
- **Avoid high-PO4 diet** (นม ไข่แดง เครื่องใน น้ำอัดลมสีเข้ม อาหารแปรรูป (เสริม))
- **Phosphate binder** (กินพร้อมอาหาร)
  - **Calcium-containing: CaCO3** (calcium carbonate) — ใช้เมื่อ Ca ไม่สูง
  - **Non-calcium: sevelamer carbonate, lanthanum carbonate, Al(OH)3**
- **Vitamin D supplement**
- เป้าหมาย: **keep PO4, Ca, PTH ใกล้ปกติ, avoid hypercalcemia**

| Binder | ข้อดี | ข้อควรระวัง (เสริม) |
|---|---|---|
| CaCO3 | ถูก หาง่าย แก้ Ca ต่ำได้ | Hypercalcemia, vascular calcification |
| Sevelamer | ไม่มี Ca/Al ลด LDL ได้ | แพง ท้องอืด |
| Lanthanum | แรง เม็ดน้อย | แพง |
| Al(OH)3 | แรงมาก | **Aluminium toxicity** (encephalopathy, osteomalacia) ใช้ระยะสั้นเท่านั้น |

> Calcitriol เพิ่มการดูด **ทั้ง Ca และ PO4** จากลำไส้ — ถ้า PO4 สูงอยู่ ต้องลด PO4 ก่อน ไม่ใช่ให้ calcitriol
''',
    figs=[F_MBD],
    pearls=[
        "Anemia CKD: แก้เหล็กก่อน → ESA เมื่อ Hb <10 → เป้า Hb 11–12",
        "CKD-MBD: ↑PO4 ↓Ca ↑PTH ↓vit D",
        "PO4 สูง Ca ปกติ/ต่ำ → CaCO3 (binder) · Ca สูง → non-calcium binder",
        "Al(OH)3 ใช้สั้น ๆ เท่านั้น (aluminium toxicity)",
    ],
    items=[
        mcq("NEPHRO-04-03-1",
            "A 65-year-old man with advanced CKD (GFR 20 mL/min/1.73 m2) has serum calcium 9 mg/dL (reference 9–10.2) and phosphate 5 mg/dL (reference 2.8–4.5). Which agent is most appropriate to correct his electrolyte abnormality?",
            "Calcium carbonate with meals",
            ["Calcitriol", "Hydrochloric acid", "Aluminium hydroxide long term", "Sodium bicarbonate"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ปัญหาหลักคือ **PO4 สูง** โดย Ca อยู่ขอบล่างของปกติ → ใช้ **phosphate binder ชนิดมี calcium (CaCO3)** กินพร้อมอาหาร ซึ่งยังช่วยยก Ca ขึ้นเล็กน้อย
- Calcitriol เพิ่มการดูด PO4 จากลำไส้ ทำให้ PO4 สูงขึ้น
- HCl ไม่ใช่ยาที่ใช้รักษาภาวะนี้
- Al(OH)3 จับ PO4 ได้แต่ใช้ระยะยาวทำ aluminium toxicity (สไลด์จัดเป็น non-calcium binder แต่ CaCO3 เหมาะกว่าในรายนี้)
- NaHCO3 แก้ acidosis ไม่ได้ลด PO4
หมายเหตุ: โจทย์ในสไลด์เขียน "ESRD (GFR 20)" แต่ GFR 20 คือ CKD G4 ไม่ใช่ ESRD''',
            pearl="CKD + ↑PO4 + Ca ไม่สูง → CaCO3", topic="Phosphate binder",
            ref=[f"{D} หน้า 150, 153–154"], nl=["2.3.14(3)"]),
        mcq("NEPHRO-04-03-2",
            "A 70-year-old woman with diabetes presents with nausea and vomiting. She has moderate pallor and pitting edema of both legs. Hct 20%, BUN 53 mg/dL, Cr 3.2 mg/dL. Iron studies are normal. Which agent would best improve her anemia?",
            "Erythropoietin",
            ["Renin", "Angiotensin II", "Aldosterone", "Prostaglandin E2"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''DM + CKD (Cr 3.2) + ซีดมาก (Hct 20%) = **anemia of CKD** จากไตสร้าง EPO ไม่พอ เมื่อแก้/ตัด IDA แล้วและ Hb < 10 → ให้ **ESA (erythropoietin)** เป้า Hb 11–12
- Renin, angiotensin II และ aldosterone เป็นฮอร์โมนควบคุมความดัน/เกลือ ไม่กระตุ้นการสร้างเม็ดเลือดแดง
- Prostaglandin E2 ควบคุมการไหลเวียนเลือดในไต ไม่ใช่ฮอร์โมนสร้างเม็ดเลือด''',
            pearl="CKD anemia → แก้เหล็ก แล้ว ESA ถ้า Hb <10", topic="Anemia of CKD",
            ref=[f"{D} หน้า 150, 155–156"], nl=["B9.1.2(8)", "B2.4(4)"]),
        mcq("NEPHRO-04-03-3",
            "A 52-year-old man with CKD stage 5 has Hb 8.6 g/dL, ferritin 40 ng/mL, and transferrin saturation 12%. He is not yet on dialysis. What is the most appropriate first step in managing his anemia?",
            "Iron supplementation",
            ["Start erythropoietin and target Hb 14 g/dL", "Transfuse to Hb 12 g/dL", "Vitamin B12 injections", "Start erythropoietin without iron"],
            explain='''Ferritin < 100 และ TSAT < 20% = **ขาดเหล็ก** สไลด์ให้ **correct IDA ก่อน** แล้วค่อยให้ ESA ถ้า Hb ยัง < 10 (ESA ไม่ได้ผลถ้าเหล็กไม่พอ)
- เป้า Hb 14 สูงเกินไป แนวทางให้ 11–12 เพราะ Hb สูงเพิ่มความเสี่ยง stroke
- Transfusion ใช้เมื่อมีอาการรุนแรง และเพิ่ม sensitization ต่อการปลูกถ่ายไต
- ไม่มีข้อมูลชี้ว่าขาด B12
- ให้ ESA โดยไม่แก้เหล็กจะตอบสนองไม่ดี''',
            pearl="CKD anemia: ferritin/TSAT ต่ำ → ให้เหล็กก่อน ESA", topic="Iron before ESA",
            ref=[f"{D} หน้า 150"], nl=["2.3.14(3)", "B2.4(2)"]),
    ])

LECTURE = lecture("04", "Chronic kidney disease", "นิยาม · staging · ชะลอโรค · anemia · CKD-MBD · RRT",
    objectives=[
        "วินิจฉัยและจัด stage CKD (G และ A) ได้",
        "บอกแนวทางชะลอ CKD และป้องกัน ASCVD ได้",
        "รักษา acidosis, anemia, CKD-MBD, hyperkalemia ใน CKD ตามเป้าหมายในสไลด์ได้",
        "บอกเวลาที่ต้องคุยเรื่อง RRT และข้อบ่งชี้เริ่ม dialysis ได้",
    ],
    sections=[S1, S2, S3])
