# -*- coding: utf-8 -*-
# หัวข้อ 12–15: รักษา ascites · SBP · HRS · รักษาตับแข็งโดยรวม ป้องกันภาวะแทรกซ้อน และเปลี่ยนตับ  (สไลด์หน้า 19–51)

sec("gi-cir-12", "รักษา ascites — เกลือ ยาขับปัสสาวะ LVP + albumin และ refractory ascites",
    "ไม่มี ascites: พิจารณาจำกัดเกลือ · uncomplicated: เกลือ + diuretic · tense: LVP · refractory: LVP + albumin → TIPS → PVS · LVP ไม่ให้ albumin → PCD",
    10, r"""
### ตามขั้น (สไลด์)
| ขั้น | การรักษา |
|---|---|
| **Portal hypertension ยังไม่มี ascites** | ไม่มียาเฉพาะ · **พิจารณาจำกัดเกลือ** |
| **Uncomplicated ascites** | **1) จำกัดเกลือ + ยาขับปัสสาวะ** · **2) Large volume paracentesis (LVP)** ในผู้ป่วยใน ที่ **ท้องตึงมาก (tense ascites)** |
| **Refractory ascites** | **1) LVP + albumin** · **2) TIPS** · **3) Peritoneovenous shunt (PVS)** ในผู้ที่ทำ TIPS และเปลี่ยนตับไม่ได้ |
| **Hepatorenal syndrome** | (หัวข้อ HRS) |

### รายละเอียดที่ใช้จริง (เพิ่มเติม — AASLD 2021 · EASL 2018 · ไม่ได้มาจากสไลด์)
| | ค่า |
|---|---|
| **เกลือ** | Na **2 g/วัน (88 mmol)** — ไม่ต่ำกว่านี้เพราะผู้ป่วยกินไม่ได้ ขาดอาหาร |
| **ยาขับปัสสาวะ** | **spironolactone 100 mg + furosemide 40 mg** เช้า (**อัตรา 100:40** คงที่) · เพิ่มทีละขั้นทุก 3–5 วัน สูงสุด **400:160** |
| **เป้าน้ำหนักลด** | **0.5 กก./วัน** ถ้าไม่บวม · **1 กก./วัน** ถ้าขาบวม |
| **หยุด/ลดยา** | Na < 125 · Cr สูง · HE · K ผิดปกติ · ตะคริวรุนแรง |
| **จำกัดน้ำดื่ม** | เฉพาะ **Na < 125** (ไม่ต้องจำกัดทุกราย) |
| **LVP** | เอาออก **> 5 ลิตร → ให้ albumin 6–8 g ต่อน้ำที่ออก 1 ลิตร** |
| **Refractory ascites** | ไม่ตอบสนองต่อยาขนาดสูงสุด หรือใช้ยาไม่ได้เพราะผลข้างเคียง · **หยุด NSBB ถ้า SBP < 90 หรือ Na < 130 หรือ AKI** |

### ทำไม LVP ต้องให้ albumin (สไลด์ — Ginès 1988)
LVP **โดยไม่ให้ albumin** → **plasma renin activity สูงขึ้นมาก** หลังเจาะ → เกิด **post-paracentesis circulatory dysfunction (PCD)** → **ไตวายและ Na ต่ำ** มากกว่ากลุ่มที่ได้ albumin

> กลไก: เอาน้ำออกเร็ว → แรงดันในช่องท้องลด → หลอดเลือดช่องท้อง **ขยายต่อ** → effective volume ยิ่งต่ำ → RAAS พุ่ง (ดูภาพเคลื่อนไหวในหัวข้อก่อน)

### ยาที่ต้องเลี่ยงในผู้ป่วย ascites (เพิ่มเติม)
**NSAIDs** (ไตวาย ลดผล diuretic) · **ACEI/ARB** (ความดันตก ไตวาย) · aminoglycoside · สารทึบรังสีโดยไม่จำเป็น
""",
    ["Uncomplicated: จำกัดเกลือ + diuretic · tense → LVP",
     "Spironolactone:furosemide = 100:40",
     "LVP > 5 L → albumin 6–8 g/L",
     "LVP ไม่ให้ albumin → PCD: renin ↑ ไตวาย Na ต่ำ",
     "Refractory: LVP + albumin → TIPS → PVS"],
    [mcq("GI-CIR-MCQ-30",
         "A cirrhotic patient with moderate ascites is starting diuretics. Which regimen is recommended?",
         ["Furosemide 80 mg alone", "Spironolactone 100 mg with furosemide 40 mg daily, titrated in the same ratio",
          "Hydrochlorothiazide 25 mg daily", "Spironolactone 25 mg weekly", "Acetazolamide 250 mg twice daily"],
         1,
         "สไลด์: uncomplicated ascites → **จำกัดเกลือ + ยาขับปัสสาวะ** · ขนาดตาม AASLD (เพิ่มเติม): **spironolactone 100 + furosemide 40 mg** คงอัตรา 100:40 เพิ่มได้ถึง 400:160\n\nspironolactone เป็นแกน เพราะ ascites ขับเคลื่อนด้วย **aldosterone ที่สูง** (hyperaldosteronism ทุติยภูมิ) · furosemide เดี่ยว ๆ ได้ผลน้อยและ K ต่ำ (เร่ง HE)",
         "Spiro:Furo = 100:40", "Ascites treatment",
         nl=["2.3.11(4)", "2.1.12"]),
     mcq("GI-CIR-MCQ-31",
         "Eight litres of ascites are drained from a patient with tense ascites. Why should intravenous albumin be given?",
         ["To prevent SBP", "To prevent post-paracentesis circulatory dysfunction with renal failure and hyponatraemia",
          "To correct coagulopathy", "To speed up ascites drainage", "Albumin is not indicated after paracentesis"],
         1,
         "สไลด์ (Ginès 1988): **LVP without albumin** → **plasma renin activity เพิ่ม** → **post-paracentesis circulatory dysfunction (PCD)** → **ไตวาย/Na ต่ำ** มากกว่ากลุ่มที่ได้ albumin\n\nขนาด (เพิ่มเติม): **6–8 g ต่อน้ำ 1 ลิตร** เมื่อเอาออก **> 5 ลิตร** → 8 ลิตรให้ albumin ราว **50–60 g**",
         "LVP > 5 L ต้องให้ albumin", "Paracentesis"),
     old("MOCK-147", nl=["2.3.11(4)", "2.1.12"], pearl="Spironolactone ต้าน aldosterone ที่ collecting duct")],
    nl=["2.3.11(4)", "2.1.12", "B8.3(4)"])


sec("gi-cir-13", "Spontaneous bacterial peritonitis — วินิจฉัย แยก secondary peritonitis และรักษา",
    "ติดเชื้อที่พบบ่อยที่สุดในตับแข็ง · PMN ≥ 250 = รักษา · MNB · CNNA · Runyon criteria ชี้ secondary · cefotaxime + albumin 1.5 g/kg วัน 1 และ 1 g/kg วัน 3 · ป้องกันหลังเคยเป็นและเมื่อเลือดออก",
    12, r"""
### ทำไมสำคัญ (สไลด์ — Fernández 2002)
**SBP เป็นการติดเชื้อที่พบบ่อยที่สุดในผู้ป่วยตับแข็งที่นอนโรงพยาบาล** ตามด้วย UTI · pneumonia · ติดเชื้อจากหัตถการ · bacteremia

อาการ (สไลด์): **ไข้ ปวดท้องทั่ว ๆ กดเจ็บหน้าท้อง** โดย **ไม่มีหลักฐานกระเพาะหรือลำไส้ทะลุ** — แต่หลายรายอาการน้อย มาด้วย **HE หรือไตวาย** เท่านั้น จึงต้อง **เจาะทุกรายที่นอนโรงพยาบาล**

### จำแนก (สไลด์)
| ชนิด | PMN | Culture | รักษา |
|---|---|---|---|
| ปกติ | < 250/mm³ | ลบ | ไม่ต้อง |
| **Monomicrobial non-neutrocytic bacterascites (MNB)** | < 250 | **บวก** | ติดตาม · ให้ยาถ้ามีอาการ |
| **Culture-negative neutrocytic ascites (CNNA)** | **≥ 250** | ลบ | **ยาปฏิชีวนะ 5–7 วัน** |
| **SBP** | **≥ 250** | **บวก** | **ยาปฏิชีวนะ 5–7 วัน** |

> **PMN ≥ 250/mm³ = ให้ยาทันที** ไม่ต้องรอผลเพาะเชื้อ (CNNA รักษาเหมือน SBP)

### Algorithm (สไลด์)
**Diagnostic paracentesis** → **PMN > 250?**
- **ใช่** → **รักษา**
- **ไม่ใช่** → culture บวก? → **ไม่** = ไม่ต้องรักษา · **บวก** → **เจาะซ้ำ** → PMN > 250 หรือ culture ยังบวก → รักษา

### สงสัย secondary peritonitis เมื่อ (สไลด์)
- **PMN > 10,000/mL**
- **เชื้อหลายชนิด (polymicrobial)** หรือเชื้อชนิดเดียวจำนวนมาก
- **2 ใน 3 ข้อ (Runyon criteria)**: **glucose < 50 mg/dL · protein > 1 g/dL · LDH > ค่าปกติของเลือด**
- **ไม่ตอบสนองต่อยาใน 48 ชม.**
- ความไว **100%** · ความจำเพาะ **45%** → ต้อง **CT ช่องท้อง** หาแผลทะลุ/ฝี และปรึกษาศัลยแพทย์

### รักษา (เพิ่มเติม — AASLD 2021 · ไม่ได้มาจากสไลด์ยกเว้นระยะเวลา 5–7 วัน)
| | |
|---|---|
| **ยาปฏิชีวนะ** | **Cefotaxime 2 g IV q8h** หรือ **ceftriaxone** · ติดเชื้อในโรงพยาบาล/ดื้อยา → piperacillin–tazobactam หรือ carbapenem |
| **Albumin** | **1.5 g/kg ภายใน 6 ชม. (วันที่ 1)** และ **1 g/kg วันที่ 3** → ลด HRS และอัตราตาย (สำคัญที่สุดเมื่อ **Cr > 1 · BUN > 30 · TB > 4**) |
| **เจาะซ้ำที่ 48 ชม.** | ถ้า PMN ไม่ลด ≥ 25% → คิดถึงเชื้อดื้อยาหรือ secondary peritonitis |
| **เลี่ยง** | NSBB ขนาดสูงเมื่อ BP ต่ำ · NSAIDs · aminoglycoside |

### ป้องกัน (สไลด์ — ตารางท้าย)
**ยาปฏิชีวนะป้องกันต่อเนื่อง** ใน **ผู้ที่เคยเป็น SBP** และ **ผู้ที่มีเลือดออกจาก varices** · เพิ่มเติม: secondary prophylaxis ด้วย **norfloxacin/ciprofloxacin** หรือ co-trimoxazole · ในเลือดออก varices ใช้ **ceftriaxone 1 g/วัน ≤ 7 วัน**
""",
    ["SBP = ติดเชื้อที่พบบ่อยที่สุดในตับแข็ง",
     "PMN ≥ 250 = ให้ยาเลย (SBP หรือ CNNA)",
     "Runyon: glucose < 50 · protein > 1 · LDH > ค่าเลือด → secondary",
     "Albumin 1.5 g/kg วัน 1 · 1 g/kg วัน 3",
     "ป้องกัน: เคยเป็น SBP · เลือดออก varices"],
    [old("MOCK-012", nl=["2.3.11(4)", "2.3.11-3(10)", "B8.3(4)"], pearl="PMN ≥ 250 → cefotaxime/ceftriaxone IV"),
     old("MOCK-164", nl=["2.3.11(4)", "2.3.11-3(10)"], pearl="SBP: albumin 1.5 g/kg วัน 1 + 1 g/kg วัน 3"),
     mcq("GI-CIR-MCQ-32",
         "A cirrhotic patient has ascitic PMN 380/mm³ and a negative ascitic culture at 48 hours. How should this be managed?",
         ["No treatment; the culture is negative", "Treat as SBP with antibiotics for 5–7 days",
          "Repeat paracentesis and treat only if the culture becomes positive", "Start antituberculous therapy",
          "Give albumin alone"],
         1,
         "สไลด์: PMN **≥ 250** + culture **ลบ** = **culture-negative neutrocytic ascites (CNNA)** → **ยาปฏิชีวนะ 5–7 วัน** เหมือน SBP\n\nเพาะเชื้อน้ำช่องท้องให้ผลลบได้มาก โดยเฉพาะถ้าไม่ได้ใส่ขวด hemoculture ข้างเตียง · **การตัดสินให้ยาใช้ PMN ไม่ใช่ผลเพาะเชื้อ**",
         "CNNA = รักษาเหมือน SBP", "SBP classification",
         nl=["2.3.11-3(10)", "B8.3(4)"]),
     mcq("GI-CIR-MCQ-33",
         "Ascitic fluid in a cirrhotic with fever shows PMN 6,500/mm³, glucose 32 mg/dL, total protein 2.3 g/dL, LDH above the serum upper limit, and Gram stain with mixed organisms. What is the next step?",
         ["Continue cefotaxime alone and recheck in 48 hours", "Urgent CT abdomen and surgical evaluation for secondary peritonitis",
          "Start rifaximin", "Large-volume paracentesis with albumin", "Discharge with oral norfloxacin"],
         1,
         "เข้าเกณฑ์ **secondary peritonitis** (สไลด์): **Runyon ครบ 3 ข้อ** (glucose < 50 · protein > 1 · LDH > ค่าปกติของเลือด) + **เชื้อหลายชนิด** → สงสัยแผลทะลุหรือฝี\n\nต้อง **CT ช่องท้องด่วน + ปรึกษาศัลยแพทย์** และขยายยาให้ครอบคลุม anaerobe (เช่น + metronidazole) · SBP เกิดจากเชื้อชนิดเดียว (E. coli, Klebsiella, Streptococcus) ผ่าตัดแล้วแย่ลง",
         "Polymicrobial + glucose ต่ำ = secondary → CT + ศัลย์", "Secondary peritonitis",
         nl=["2.3.11-3(10)", "B8.2.2-3(3)", "B8.3(4)"])],
    nl=["2.3.11(4)", "2.3.11-3(10)", "B8.2.2-3(3)", "B8.3(4)"],
    mnem=[{"name": "250 · 1.5 · 1", "what": "ตัวเลขที่ต้องจำของ SBP",
           "lines": [["250", "PMN ≥ 250/mm³ → ให้ยาเลย"], ["1.5", "albumin **1.5 g/kg** วันที่ 1"],
                     ["1", "albumin **1 g/kg** วันที่ 3"], ["50·1·LDH", "Runyon: glucose < **50** · protein > **1** · LDH > ค่าเลือด → secondary"]],
           "note": "ระยะเวลายาปฏิชีวนะ 5–7 วัน",
           "src": "สไลด์หน้า 46–47 + AASLD 2021"}])


sec("gi-cir-14", "Hepatorenal syndrome — นิยาม เกณฑ์วินิจฉัย และการรักษา",
    "ไตวายเชิงหน้าที่ในตับวายขั้นสูง · type I เร็ว < 2 สัปดาห์ · type II ช้า + ascites ดื้อยา · ตัดสาเหตุอื่น · ไม่ดีขึ้นหลังหยุด diuretic + albumin 1 g/kg 2 วัน · vasoconstrictor + albumin · เปลี่ยนตับ",
    11, r"""
### นิยาม (สไลด์)
**ไตวายเฉียบพลันในผู้ป่วยตับแข็งขั้นสูง** (หรือ alcoholic hepatitis รุนแรง · มะเร็งแพร่กระจายในตับ) เป็น **ขั้นสุดท้ายของการลด renal perfusion** จากตับเสียหายรุนแรง — ไตเองปกติ (ปลูกไตนี้ให้คนอื่นใช้ได้) · อาการ: **ปัสสาวะออกน้อย · creatinine ขึ้นเรื่อย ๆ**

### 2 แบบ (สไลด์ — นิยามดั้งเดิม)
| | **Type I** | **Type II** |
|---|---|---|
| ความเร็ว | **เร็ว** — creatinine clearance ลด 50% เหลือ < 20 mL/min หรือ **Cr เพิ่ม 2 เท่าจนเกิน 2.5 mg/dL ภายใน < 2 สัปดาห์** | ช้า ไตเสื่อมไม่รุนแรง |
| ลักษณะ | รุนแรงกว่า มักมีตัวกระตุ้น (**SBP** · เลือดออก · LVP ไม่ให้ albumin) | มาพร้อม **ascites ที่ดื้อต่อ diuretic** |

### เกณฑ์วินิจฉัย (สไลด์)
1. โรคตับเรื้อรังหรือเฉียบพลันที่มี **ตับวายขั้นสูงและ portal hypertension**
2. **Creatinine > 1.5 mg/dL**
3. **ไม่มีสาเหตุอื่น** — shock · bacterial infection · **ยาที่เป็นพิษต่อไต** · ไม่มีหลักฐานทางเดินปัสสาวะอุดตันหรือโรคเนื้อไตจาก US
4. **เม็ดเลือดแดงในปัสสาวะ < 50/HPF** · **โปรตีน < 500 mg/วัน**
5. **ไม่ดีขึ้นหลังขยาย volume** — **หยุด diuretic + albumin IV 1 g/kg/วัน (สูงสุด 100 g/วัน) อย่างน้อย 2 วัน**

**อัปเดต ICA 2015/2024 (ไม่ได้มาจากสไลด์)**: เปลี่ยนชื่อ type I เป็น **HRS-AKI** และ **ไม่ต้องรอ Cr > 2.5** — ใช้เกณฑ์ KDIGO (**Cr เพิ่ม ≥ 0.3 mg/dL ใน 48 ชม. หรือ ≥ 50% ใน 7 วัน**) เพื่อรักษาเร็วขึ้น · type II เรียก HRS-CKD/AKD

### แยกจาก ATN และ prerenal (เพิ่มเติม — เชื่อมคาบ AKI)
| | Prerenal | **HRS** | ATN |
|---|---|---|---|
| FENa | < 1% | **< 1%** | > 2% |
| ปัสสาวะ | ปกติ | **ปกติ (bland)** | muddy brown cast |
| หลังให้ albumin | **ดีขึ้น** | **ไม่ดีขึ้น** | ไม่ดีขึ้น |

### รักษา (สไลด์)
**1) Liver transplant** (รักษาหายจริง) · **2) Vasoconstrictor + albumin** · 3) TIPS? · 4) extracorporeal albumin dialysis? (ยังไม่พิสูจน์)

รายละเอียด (เพิ่มเติม — AASLD 2021): **terlipressin** 1 mg IV q4–6h (หรือ infusion) + **albumin 20–40 g/วัน** · ถ้าไม่มี terlipressin → **norepinephrine** ใน ICU · ทางเลือกนอก ICU: **midodrine + octreotide + albumin** (ได้ผลน้อยกว่า) · ระวัง terlipressin: **ขาดเลือดและน้ำท่วมปอด** (ห้ามใน SpO₂ < 90%)

### ป้องกัน (สไลด์)
**หลีกเลี่ยงยาที่เป็นพิษต่อไตหรือยาขับปัสสาวะมากเกินไป** · **แก้ภาวะเสียเลือดและสารน้ำ** · albumin หลัง LVP และใน SBP
""",
    ["HRS = ไตวายเชิงหน้าที่ ไตปกติ",
     "Type I เร็ว (< 2 สัปดาห์ Cr > 2.5) · Type II ช้า + ascites ดื้อยา",
     "วินิจฉัย: หยุด diuretic + albumin 1 g/kg 2 วันแล้วไม่ดีขึ้น · ตัด shock ยา obstruction",
     "รักษา: terlipressin + albumin · หายจริง = เปลี่ยนตับ",
     "ปัจจุบัน HRS-AKI ใช้ KDIGO ไม่ต้องรอ Cr 2.5"],
    [mcq("GI-CIR-MCQ-34",
         "A cirrhotic with ascites has creatinine rising from 1.0 to 2.1 mg/dL over 4 days. Urinalysis is bland, ultrasound is normal and he is not shocked. What is the first step before diagnosing hepatorenal syndrome?",
         ["Start haemodialysis", "Stop diuretics and give IV albumin 1 g/kg/day (max 100 g) for 2 days",
          "Give IV furosemide to promote diuresis", "Start terlipressin immediately without volume assessment",
          "Perform renal biopsy"],
         1,
         "สไลด์ (เกณฑ์ข้อสุดท้าย): ต้อง **ไม่ดีขึ้นหลังหยุด diuretic + ให้ albumin IV 1 g/kg/วัน สูงสุด 100 g/วัน อย่างน้อย 2 วัน** จึงวินิจฉัย HRS ได้ — ถ้าดีขึ้นคือ **prerenal**\n\nร่วมกับ **หาตัวกระตุ้น** (SBP · เลือดออก · ยา NSAIDs) · ถ้าไม่ดีขึ้น → **terlipressin + albumin**",
         "ก่อนเรียก HRS: หยุด diuretic + albumin 2 วัน", "Hepatorenal syndrome",
         nl=["2.3.11(4)", "2.3.11-3(7)"]),
     mcq("GI-CIR-MCQ-35",
         "Which finding is incompatible with a diagnosis of hepatorenal syndrome?",
         ["Urine sodium < 10 mmol/L", "Bland urine sediment", "Proteinuria of 1.8 g/day with 80 RBC/HPF",
          "Normal-sized kidneys on ultrasound", "Oliguria"],
         2,
         "สไลด์: เกณฑ์ HRS ต้องมี **RBC ในปัสสาวะ < 50/HPF** และ **โปรตีน < 500 mg/วัน** — โปรตีน 1.8 g + RBC 80 ชี้ **โรคเนื้อไต (glomerular disease)** เช่น IgA nephropathy ที่พบร่วมในตับแข็ง หรือ HBV/HCV-related GN\n\nHRS เป็นไตวายเชิงหน้าที่: ปัสสาวะ bland · Na ในปัสสาวะต่ำ · ไตขนาดปกติ",
         "Proteinuria > 500 หรือ RBC > 50 = ไม่ใช่ HRS", "Hepatorenal syndrome",
         nl=["2.3.11(4)", "2.3.11-3(7)"]),
     mcq("GI-CIR-MCQ-36",
         "What is the only definitive treatment for hepatorenal syndrome?",
         ["Haemodialysis", "TIPS", "Liver transplantation", "Terlipressin with albumin", "Kidney transplantation"],
         2,
         "สไลด์: รักษา HRS — **1) Liver transplant** · 2) vasoconstrictor + albumin · 3) TIPS? · 4) ECAD?\n\nไตใน HRS **ปกติโดยโครงสร้าง** ปัญหาอยู่ที่การไหลเวียนจากตับ → แก้ที่ตับจึงหาย · terlipressin + albumin เป็น **สะพาน** ไปสู่การเปลี่ยนตับ · dialysis ใช้รอเปลี่ยนตับเท่านั้น",
         "HRS หายจริง = เปลี่ยนตับ", "Hepatorenal syndrome",
         nl=["2.3.11(4)", "2.3.11-3(7)", "B8.2.5-3(1)"])],
    nl=["2.3.11(4)", "2.3.11-3(7)", "B8.2.5-3(1)"])


sec("gi-cir-15", "รักษาตับแข็งโดยรวม ป้องกันภาวะแทรกซ้อน คัดกรอง HCC และเปลี่ยนตับ",
    "4 เป้าหมาย · รักษาตามสาเหตุ · paracetamol ≤ 2 g/วัน · วัคซีน HAV HBV ไข้หวัดใหญ่ pneumococcus · US ± AFP ทุก 6 เดือน · hepatopulmonary syndrome · ข้อบ่งชี้เปลี่ยนตับ",
    11, r"""
### เป้าหมายการรักษา (สไลด์)
1. **หยุดหรือชะลอการดำเนินโรค**
2. **ป้องกันโรคหรือภาวะอื่นที่อันตรายต่อตับ**
3. **ป้องกันและรักษาภาวะแทรกซ้อน**
4. **พิจารณาผ่าตัดเปลี่ยนตับเมื่อมีข้อบ่งชี้**

### หยุด/ชะลอโรค — รักษาตามสาเหตุ (สไลด์)
| สาเหตุ | รักษา |
|---|---|
| สุรา | **หยุดดื่ม** (สำคัญที่สุด — decompensated ก็กลับมา compensated ได้) |
| Autoimmune hepatitis | **steroid** |
| ไวรัสตับอักเสบ | **ยาต้านไวรัส** (HBV: TDF/TAF/ETV · HCV: DAA) |
| Wilson | **ยาขับทองแดง** (penicillamine, trientine) |
| Hemochromatosis | **เจาะเลือดออก (phlebotomy)** |

### ป้องกันสิ่งที่ทำร้ายตับ (สไลด์)
- **เลี่ยงแอลกอฮอล์** · **เลี่ยงยาไม่จำเป็นรวมถึงสมุนไพร**
- **Acetaminophen ไม่เกิน 2 g/วัน** แบ่งให้ (ยาแก้ปวดที่ปลอดภัยที่สุดในตับแข็ง — **ห้าม NSAIDs**)
- **วัคซีนไวรัสตับอักเสบ A และ B** · **ไข้หวัดใหญ่ · pneumococcus**

### ภาวะแทรกซ้อนอื่น ๆ และการป้องกัน (สไลด์ — ตารางท้าย)
| ภาวะ | อาการ/วินิจฉัย | ป้องกัน |
|---|---|---|
| **HCC** | ปวดท้อง อิ่มง่าย ดีซ่าน คลำได้ก้อน **ตับทำงานแย่ลงฉับพลัน** · **AFP สูง + ภาพถ่ายรังสี** | **US ช่องท้องส่วนบน + AFP ทุก 6 เดือน** |
| **Hepatopulmonary syndrome** | **O₂ ต่ำ เหนื่อยมากขึ้นเมื่อลุกนั่ง (platypnea)** · orthodeoxia | วินิจฉัยด้วย **contrast-enhanced (bubble) echocardiography** หรือ albumin scan |
| **ติดเชื้อในโรงพยาบาล** | ปอด · ทางเดินปัสสาวะ · **C. difficile** | **เลี่ยงการใส่สายต่าง ๆ โดยไม่มีข้อบ่งชี้** |
| **Varices** | | ส่องกล้องประเมินความเสี่ยงและป้องกัน |
| **SBP** | | ยาป้องกันในผู้ที่เคยเป็นและเลือดออก varices |
| **HRS** | | เลี่ยงยาพิษต่อไต diuretic มากเกิน · แก้เสียเลือดเสียน้ำ |
| **HE** | | เลี่ยงตัวเร่ง: เลือดออก ติดเชื้อ ยากดสมอง ท้องผูก โปรตีนสูง K/Na ต่ำ |

**HPS กลไก (เพิ่มเติม)**: หลอดเลือดในปอดขยาย (NO) ที่ฐานปอด → ลุกนั่งเลือดไหลลงฐานปอดมากขึ้น → shunt เพิ่ม → O₂ ตก · ต่างจาก **portopulmonary hypertension** (หลอดเลือดปอดตีบ ความดันปอดสูง)

### ข้อบ่งชี้ส่งพิจารณาเปลี่ยนตับ (สไลด์)
- **Decompensated cirrhosis**
- **Child-Pugh B หรือ C**
- **MELD ≥ 15**
- มีภาวะแทรกซ้อน: **HE · เลือดออกจาก varices (หลอดอาหารหรือกระเพาะ) · ascites (± SBP) · HRS**

เพิ่มเติม: HCC ใน **Milan criteria** (ก้อนเดียว ≤ 5 ซม. หรือ ≤ 3 ก้อนแต่ละก้อน ≤ 3 ซม. ไม่ลุกลามหลอดเลือด) ก็เป็นข้อบ่งชี้ · ต้องหยุดสุราได้จริงก่อน
""",
    ["4 เป้า: ชะลอโรค · ป้องกันสิ่งทำร้ายตับ · ป้องกันภาวะแทรกซ้อน · เปลี่ยนตับ",
     "Paracetamol ≤ 2 g/วัน · ห้าม NSAIDs",
     "วัคซีน HAV HBV ไข้หวัดใหญ่ pneumococcus",
     "HCC: US + AFP ทุก 6 เดือน",
     "HPS = platypnea + orthodeoxia → bubble echo",
     "เปลี่ยนตับ: decompensated · Child B/C · MELD ≥ 15"],
    [mcq("GI-CIR-MCQ-37",
         "A patient with compensated cirrhosis asks which analgesic is safest for knee pain. What is the most appropriate advice?",
         ["Ibuprofen 400 mg three times daily", "Paracetamol, not exceeding 2 g per day in divided doses",
          "Diclofenac gel plus oral naproxen", "Tramadol at maximal dose", "Avoid all analgesics"],
         1,
         "สไลด์: **acetaminophen ไม่ควรเกิน 2 g ต่อวัน โดยแบ่งให้** · และ **หลีกเลี่ยงยาที่ไม่จำเป็น รวมทั้งสมุนไพร**\n\n**NSAIDs** ในตับแข็ง → ไตวาย (ไตพึ่ง prostaglandin) ลดผล diuretic และเลือดออกทางเดินอาหาร · opioid/tramadol เร่ง HE และท้องผูก",
         "ตับแข็ง: paracetamol ≤ 2 g/วัน · เลี่ยง NSAIDs", "General management",
         nl=["2.3.11(4)", "B8.2.5(4)"]),
     mcq("GI-CIR-MCQ-38",
         "How should a patient with cirrhosis be screened for hepatocellular carcinoma?",
         ["CT abdomen every year", "Ultrasound with or without AFP every 6 months", "AFP alone every 3 months",
          "Liver biopsy every 2 years", "MRI only when symptoms develop"],
         1,
         "สไลด์: **การตรวจคัดกรองมะเร็งตับ — อัลตราซาวนด์ช่องท้องส่วนบน + AFP ทุก 6 เดือน**\n\nช่วง 6 เดือนมาจาก **doubling time ของ HCC** · AFP เดี่ยว ๆ ไวต่ำ · CT/MRI ใช้ **ยืนยัน** เมื่อเจอก้อน (ภาพ arterial enhancement + washout)",
         "HCC: US ± AFP ทุก 6 เดือน", "HCC surveillance",
         nl=["2.3.11(4)", "B8.2.4-3(2)", "2.3.2-3(1)"]),
     mcq("GI-CIR-MCQ-39",
         "A cirrhotic patient becomes more breathless and his SpO2 drops from 95% to 88% when he sits up from lying flat. Chest radiograph is clear. Which investigation is most useful?",
         ["Pulmonary function tests", "Contrast-enhanced (bubble) echocardiography", "CT pulmonary angiography",
          "Ventilation–perfusion scan for PE only", "Bronchoscopy"],
         1,
         "**Platypnea (เหนื่อยเมื่อลุกนั่ง) + orthodeoxia (O₂ ตกเมื่อลุก)** ในตับแข็ง = **hepatopulmonary syndrome** · สไลด์: วินิจฉัยด้วย **contrast-enhanced echocardiography** (bubble ปรากฏในหัวใจซ้ายหลัง 3–6 จังหวะ = intrapulmonary shunt) หรือ albumin scan\n\nกลไก: หลอดเลือดที่ฐานปอดขยาย · รักษาจริง = **เปลี่ยนตับ**",
         "Platypnea + orthodeoxia + ตับแข็ง = HPS → bubble echo", "Hepatopulmonary syndrome",
         nl=["2.3.11(4)", "B8.2.5-3(1)"]),
     mcq("GI-CIR-MCQ-40",
         "Which patient with cirrhosis most clearly meets the lecture's criteria for referral for liver transplant evaluation?",
         ["Child A, MELD 8, no complications", "Child A cirrhosis with a single 6 cm HCC and portal vein invasion",
          "Child B, MELD 17, recurrent ascites after a variceal bleed", "Compensated HBV cirrhosis with suppressed HBV DNA",
          "Active daily alcohol use with Child C cirrhosis and no intention to stop"],
         2,
         "สไลด์: ข้อบ่งชี้ — **decompensated cirrhosis · Child-Pugh B/C · MELD ≥ 15 · มีภาวะแทรกซ้อน** (HE · varices bleed · ascites ± SBP · HRS) → ข้อ C ครบทุกข้อ\n\nHCC ที่ลุกลามหลอดเลือดอยู่นอก Milan criteria · การดื่มต่อเนื่องและไม่ตั้งใจเลิกเป็นข้อห้ามที่สำคัญ (เพิ่มเติม)",
         "เปลี่ยนตับ: decompensated · Child B/C · MELD ≥ 15", "Liver transplantation",
         nl=["2.3.11(4)", "2.3.11-3(7)", "B8.2.5-3(1)"])],
    nl=["2.3.11(4)", "B8.2.5(4)", "B8.2.4-3(2)", "B8.2.5-3(1)"])
