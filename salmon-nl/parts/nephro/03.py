from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Nephro"

# ---------------------------------------------------------------- 03-01 Nephrotic syndrome
F_NS = fig("nephro-03-01-f1", "Proteinuria หนัก → ผลตามมาของ nephrotic syndrome", '''<svg viewBox="0 0 740 300">
 <defs><marker id="nephro-03-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="56" rx="10" class="c1"/>
 <text x="370" y="34" text-anchor="middle" class="tw">Podocyte/GBM เสีย</text>
 <text x="370" y="54" text-anchor="middle" class="tw">Proteinuria &gt; 3.5 g/day</text>
 <path d="M290 66L110 118" class="ln" marker-end="url(#nephro-03-01-a)"/>
 <path d="M340 66L290 118" class="ln" marker-end="url(#nephro-03-01-a)"/>
 <path d="M400 66L450 118" class="ln" marker-end="url(#nephro-03-01-a)"/>
 <path d="M450 66L630 118" class="ln" marker-end="url(#nephro-03-01-a)"/>
 <rect x="10" y="120" width="190" height="64" rx="10" class="c1soft"/>
 <text x="105" y="146" text-anchor="middle" class="tb">เสีย albumin</text>
 <text x="105" y="166" text-anchor="middle" class="t3">Albumin &lt; 2.5–3 g/dL</text>
 <rect x="210" y="120" width="160" height="64" rx="10" class="badsoft"/>
 <text x="290" y="146" text-anchor="middle" class="tb">เสีย antithrombin</text>
 <text x="290" y="166" text-anchor="middle" class="t3">+ ตับสร้าง fibrinogen ↑</text>
 <rect x="380" y="120" width="160" height="64" rx="10" class="misssoft"/>
 <text x="460" y="146" text-anchor="middle" class="tb">เสีย IgG</text>
 <text x="460" y="166" text-anchor="middle" class="t3">และ complement</text>
 <rect x="550" y="120" width="180" height="64" rx="10" class="c2soft"/>
 <text x="640" y="146" text-anchor="middle" class="tb">ตับสร้าง lipoprotein ↑</text>
 <text x="640" y="166" text-anchor="middle" class="t3">ชดเชย oncotic ที่ลด</text>
 <path d="M105 184V218" class="ln" marker-end="url(#nephro-03-01-a)"/>
 <path d="M290 184V218" class="ln" marker-end="url(#nephro-03-01-a)"/>
 <path d="M460 184V218" class="ln" marker-end="url(#nephro-03-01-a)"/>
 <path d="M640 184V218" class="ln" marker-end="url(#nephro-03-01-a)"/>
 <rect x="10" y="220" width="190" height="70" rx="10" class="box"/>
 <text x="105" y="244" text-anchor="middle" class="tb">Edema</text>
 <text x="105" y="264" text-anchor="middle" class="t3">หนังตาบวม ascites</text>
 <text x="105" y="280" text-anchor="middle" class="t3">pleural effusion</text>
 <rect x="210" y="220" width="160" height="70" rx="10" class="box"/>
 <text x="290" y="244" text-anchor="middle" class="tb">Thrombosis</text>
 <text x="290" y="264" text-anchor="middle" class="t3">renal vein (MN)</text>
 <text x="290" y="280" text-anchor="middle" class="t3">DVT, PE</text>
 <rect x="380" y="220" width="160" height="70" rx="10" class="box"/>
 <text x="460" y="244" text-anchor="middle" class="tb">ติดเชื้อง่าย</text>
 <text x="460" y="264" text-anchor="middle" class="t3">pneumococcus</text>
 <text x="460" y="280" text-anchor="middle" class="t3">SBP ในเด็ก</text>
 <rect x="550" y="220" width="180" height="70" rx="10" class="box"/>
 <text x="640" y="244" text-anchor="middle" class="tb">Hyperlipidemia</text>
 <text x="640" y="264" text-anchor="middle" class="t3">lipiduria: oval fat body</text>
 <text x="640" y="280" text-anchor="middle" class="t3">fatty cast</text>
</svg>''', "ทุกอาการของ nephrotic syndrome สืบมาจากการรั่วโปรตีน: เสีย albumin, antithrombin และ IgG ส่วนตับพยายามชดเชยจนไขมันสูง")

F_LOC = fig("nephro-03-01-f2", "ตำแหน่งรอยโรคใน glomerular capillary", '''<svg viewBox="0 0 740 330">
 <rect x="20" y="20" width="420" height="44" rx="6" class="c1soft"/>
 <text x="230" y="47" text-anchor="middle" class="tb">Capillary lumen (เลือด)</text>
 <rect x="20" y="70" width="420" height="16" rx="3" class="sunk"/>
 <text x="230" y="83" text-anchor="middle" class="t3">Endothelium</text>
 <rect x="20" y="92" width="420" height="10" rx="2" class="miss"/>
 <text x="140" y="127" class="t3">subendothelial</text>
 <rect x="20" y="132" width="420" height="30" rx="4" class="acsoft"/>
 <text x="230" y="152" text-anchor="middle" class="tb">GBM</text>
 <text x="140" y="182" class="t3">subepithelial</text>
 <rect x="20" y="188" width="420" height="10" rx="2" class="c2"/>
 <rect x="40" y="204" width="60" height="22" rx="8" class="box"/>
 <rect x="110" y="204" width="60" height="22" rx="8" class="box"/>
 <rect x="180" y="204" width="60" height="22" rx="8" class="box"/>
 <rect x="250" y="204" width="60" height="22" rx="8" class="box"/>
 <rect x="320" y="204" width="60" height="22" rx="8" class="box"/>
 <text x="230" y="248" text-anchor="middle" class="t3">Podocyte foot processes</text>
 <rect x="20" y="268" width="420" height="44" rx="6" class="sunk"/>
 <text x="230" y="295" text-anchor="middle" class="tb">Bowman space (ปัสสาวะ)</text>
 <rect x="470" y="20" width="250" height="56" rx="10" class="sunk"/>
 <text x="482" y="42" class="tb">Mesangium</text>
 <text x="482" y="62" class="t2">IgAN, HSP: mesangial IgA</text>
 <rect x="470" y="84" width="250" height="40" rx="10" class="misssoft"/>
 <text x="482" y="109" class="t2">Subendothelial: MPGN, LN</text>
 <rect x="470" y="132" width="250" height="40" rx="10" class="acsoft"/>
 <text x="482" y="157" class="t2">GBM linear IgG: anti-GBM</text>
 <rect x="470" y="180" width="250" height="40" rx="10" class="c2soft"/>
 <text x="482" y="198" class="t2">Subepithelial: MN (spike),</text>
 <text x="482" y="214" class="t2">APSGN (humps)</text>
 <rect x="470" y="228" width="250" height="48" rx="10" class="c1soft"/>
 <text x="482" y="248" class="t2">Foot process effacement:</text>
 <text x="482" y="266" class="t2">MCD (LM ปกติ), FSGS</text>
 <rect x="470" y="284" width="250" height="40" rx="10" class="box"/>
 <text x="482" y="309" class="t2">Nodular sclerosis: DM (KW)</text>
</svg>''', "ซ้ายคือภาพตัดขวางของผนัง capillary จากเลือดลงไปสู่ปัสสาวะ ขวาคือโรคที่มีรอยโรคในแต่ละชั้น (สีกรอบตรงกับชั้นทางซ้าย)")

S1 = sec("nephro-03-01", "Nephrotic syndrome: approach & management",
    "Proteinuria >3–3.5 g/d + albumin <2.5–3 + lipid สูง + edema · หา secondary cause · supportive + specific tx", minutes=9,
    source=f"{D} หน้า 113–121, 128–131, 138–141", nl=["2.3.14(12)", "B9.2.2(4)", "2.1.39"],
    md='''
### นิยาม

- **Heavy proteinuria > 3–3.5 g/day** (หรือ **UPCR > 3–3.5 g/g**), dipstick 3–4+
- **Hypoalbuminemia < 2.5–3 g/dL**
- **Hyperlipidemia**
- **Generalized edema** (หนังตาบวมตอนเช้า ascites pleural effusion), BP ปกติ/สูงได้
- Frothy urine · UA: **oval fat bodies, fatty casts** (Maltese cross ใต้ polarized light (เสริม))
- **↑Thromboembolism risk, ↑infection risk**

[[fig:nephro-03-01-f1]]

### สาเหตุ

| Primary | Secondary |
|---|---|
| Minimal change disease (MCD) | **Diabetic nephropathy** (พบบ่อยสุดในผู้ใหญ่) |
| Membranous nephropathy (MN) | Autoimmune (lupus nephritis) |
| FSGS | Infection (HBV, HCV, HIV, syphilis) |
| MPGN (ส่วนใหญ่มัก secondary) | Malignancy, drugs (heroin, interferon, NSAIDs, pamidronate), hereditary, amyloid |

> วินิจฉัย primary NS ได้ต่อเมื่อ **R/O secondary cause** แล้ว

### เปรียบเทียบ primary NS (ตามสไลด์)

| | MCD | FSGS | MN | MPGN |
|---|---|---|---|---|
| Onset | **Abrupt** (วัน–สัปดาห์) | สัปดาห์–เดือน | **ช้า** (เดือน–ปี) | แล้วแต่ |
| Age | Bimodal เด็ก & ผู้สูงอายุ | เด็กโต–กลางคน | **กลางคน–สูงอายุ** | แล้วแต่ |
| Protein | ↑↑↑↑ | ↑↑ | ↑↑↑↑ | ↑ |
| HT | - | ↑↑ | ↑ | ↑↑ |
| RBC, dysmorphic | - | ↑ | - | ↑↑↑ |
| Renal failure | - | ↑↑ | ↑ | ↑↑↑ |
| ตอบสนอง steroid | **++++** | ++ | + | + |

[[fig:nephro-03-01-f2]]

### Investigation

- BUN, Cr, UA, **UPCR/24-hr urine protein**
- Lipid profile, CBC, CXR
- หา secondary cause ตามที่สงสัย
  - DM: serum glucose, HbA1c
  - Lupus: ANA, anti-dsDNA, C3, C4
  - Multiple myeloma: SPEP
  - Infection: HBsAg, anti-HCV, anti-HIV, syphilis serology
  - Malignancy screening ตามกลุ่มอายุ
- **Renal biopsy ทำเป็นส่วนใหญ่** ยกเว้น **primary MCD (เด็ก)** และ **typical diabetic nephropathy**

### การรักษา

**Specific**
- Secondary NS → รักษาโรคต้นเหตุ
- MCD → **prednisolone** (ตอบสนองดีมาก)
- FSGS → prednisolone
- MN → **prednisolone + immunosuppressants**

**Supportive (ทุกราย)**
- Edema: **จำกัด Na และน้ำ + furosemide**
- BP & proteinuria: **ACEI/ARB** (ลด intraglomerular pressure)
- DLP: **statins**
- **Prophylactic anticoagulation** เมื่อ **albumin < 2 g/dL** หรือมีประวัติ thrombosis
- **Pneumococcal, influenza vaccine**

> Steroid-resistant (ให้ prednisolone ครบแล้วไม่ดีขึ้น) และมีผลข้างเคียงของ steroid (moon face, striae) → **ลด steroid + เพิ่ม immunosuppressant ชนิดกิน** (เช่น calcineurin inhibitor (เสริม)) และ biopsy ถ้ายังไม่ได้ทำ (เสริม)
''',
    figs=[F_NS, F_LOC],
    pearls=[
        "NS: protein >3.5 g/d (UPCR >3.5) + albumin <3 + lipid สูง + edema + fatty cast",
        "ผู้ใหญ่ NS → หา secondary cause (DM, SLE, HBV/HCV/HIV, myeloma, มะเร็ง) แล้ว biopsy",
        "ไม่ต้อง biopsy: เด็ก MCD ทั่วไป และ typical diabetic nephropathy",
        "Supportive: Na/fluid restriction + furosemide · ACEI/ARB · statin · anticoag ถ้า albumin <2 · วัคซีน",
        "Steroid-resistant + cushingoid → ลด steroid + เพิ่ม oral immunosuppressant",
    ],
    items=[
        mcq("NEPHRO-03-01-1",
            "A 23-year-old woman has facial and leg swelling for 2 months. BP 130/80 mmHg, generalized edema. Urinalysis: protein 4+, WBC 0–1/HPF, RBC 2–3/HPF, fine granular casts 0–2/LPF, oval fat bodies 2–3/HPF. BUN 12 mg/dL, Cr 0.8 mg/dL. What is the most likely diagnosis?",
            "Nephrotic syndrome",
            ["Acute glomerulonephritis", "Rapidly progressive glomerulonephritis", "Chronic glomerulonephritis", "Acute tubular necrosis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''บวมทั่วตัว + **protein 4+ + oval fat body** + ความดันปกติ + RBC น้อย + Cr ปกติ = **nephrotic syndrome**
- AGN และ RPGN ต้องมีความดันสูง hematuria เด่น RBC cast และไตวาย
- Chronic GN ต้องมีไตวายเรื้อรัง ซีด broad cast
- ATN ไม่มี proteinuria 4+ และ Cr จะสูง''',
            pearl="Protein 4+ + oval fat body + BP/Cr ปกติ = NS", topic="Nephrotic syndrome",
            ref=[f"{D} หน้า 113, 128–129"], nl=["2.3.14(12)"]),
        mcq("NEPHRO-03-01-2",
            "A patient presents with leg edema; urinalysis shows protein 4+. Which laboratory finding is most likely to be associated?",
            "Elevated serum cholesterol",
            ["Elevated serum bilirubin", "Elevated white blood cell count", "Elevated AST/ALT", "Elevated blood glucose"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ใน nephrotic syndrome oncotic pressure ที่ลดลงกระตุ้นตับให้สร้าง lipoprotein เพิ่ม → **hypercholesterolemia** เป็นส่วนหนึ่งของนิยาม
- Bilirubin และ AST/ALT สูงบอกโรคตับ ซึ่งทำให้ albumin ต่ำได้แต่ไม่ทำ proteinuria 4+
- WBC สูงไม่ใช่ลักษณะของ NS
- Glucose สูงพบเมื่อสาเหตุเป็นเบาหวาน แต่ไม่ใช่ผลที่ตามมาของ NS เอง''',
            pearl="NS = proteinuria + albumin ต่ำ + cholesterol สูง + edema", topic="NS features",
            ref=[f"{D} หน้า 113, 130–131"], nl=["2.3.14(12)"]),
        mcq("NEPHRO-03-01-3",
            "A 45-year-old man with membranous nephropathy has 9 g/day of proteinuria and serum albumin 1.7 g/dL. He has no history of bleeding. Besides an ACE inhibitor, statin, and diuretic, which additional supportive measure is most appropriate?",
            "Prophylactic anticoagulation",
            ["Intravenous albumin infusion every day", "Prophylactic ciprofloxacin", "High-protein diet of 2 g/kg/day", "Platelet transfusion"],
            explain='''สไลด์: **prophylactic anticoagulation เมื่อ albumin < 2 g/dL** หรือมีประวัติ thrombosis เพราะ NS เสีย antithrombin ทางปัสสาวะ (MN เสี่ยง renal vein thrombosis สูงสุด (เสริม))
- Albumin IV ทุกวันจะรั่วออกทางปัสสาวะหมดในไม่กี่ชั่วโมง ใช้เฉพาะกรณีพิเศษ
- ยาปฏิชีวนะป้องกันไม่ใช่มาตรฐาน — ป้องกันติดเชื้อด้วยวัคซีน pneumococcal/influenza
- โปรตีนสูงเพิ่ม proteinuria ทำให้ไตเสียเร็วขึ้น
- Platelet transfusion ไม่มีข้อบ่งชี้''',
            pearl="NS + albumin <2 g/dL → prophylactic anticoagulation", topic="NS supportive care",
            ref=[f"{D} หน้า 121"], nl=["2.3.14(12)"]),
        mcq("NEPHRO-03-01-4",
            "A 10-year-old boy with nephrotic syndrome was treated with prednisolone 60 mg/m2/day for 6 weeks without remission. He now has a moon face and purplish striae. What is the most appropriate management?",
            "Taper prednisolone and add an oral immunosuppressive agent",
            ["Switch to intravenous methylprednisolone and continue for 6 more weeks", "Double the prednisolone dose", "Stop all treatment and observe", "Start oral cyclophosphamide while keeping full-dose prednisolone indefinitely"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไม่ตอบสนองหลังได้ prednisolone ครบ 6 สัปดาห์ = **steroid-resistant NS** และมีผลข้างเคียงของ steroid แล้ว → สไลด์: **ลด steroid + เพิ่ม oral immunosuppressive agent** (ส่วนใหญ่เป็น calcineurin inhibitor และควร biopsy หา FSGS (เสริม))
- เปลี่ยนเป็น methylprednisolone ต่อหรือเพิ่มขนาดยา ยังเป็น steroid ที่ไม่ได้ผลและเพิ่มผลข้างเคียง
- หยุดรักษาทั้งหมดปล่อยให้ proteinuria หนักต่อไปเสี่ยงไตเสียและ thrombosis
- ให้ steroid เต็มขนาดต่อไปเรื่อย ๆ ทำให้ cushingoid แย่ลง''',
            pearl="Steroid-resistant NS → ลด steroid + เพิ่ม immunosuppressant", topic="Steroid-resistant NS",
            ref=[f"{D} หน้า 140–141"], nl=["2.3.14(12)"]),
        mcq("NEPHRO-03-01-5",
            "A 7-year-old girl presents with generalized edema, ascites, and frothy urine. BP 100/60 mmHg. Urine protein 4+, no hematuria, albumin 1.9 g/dL, Cr 0.4 mg/dL, normal C3. Besides sodium restriction, what is the most appropriate specific treatment?",
            "Oral prednisolone",
            ["Renal biopsy before any treatment", "Intravenous cyclophosphamide", "Plasmapheresis", "Paracentesis alone"],
            kind="old", src="ดัดแปลงจากตัวอย่างข้อสอบในสไลด์",
            explain='''เด็กอายุ 1–10 ปี nephrotic ล้วน ความดันปกติ ไม่มี hematuria complement ปกติ = **MCD** ให้ **prednisolone** ได้เลยเป็น specific treatment ร่วมกับ supportive (จำกัดเกลือ ± diuretic) ascites จะยุบเมื่อ proteinuria หาย
- Biopsy ไม่จำเป็นใน MCD เด็กแบบ typical ทำเมื่อไม่ตอบสนอง
- Cyclophosphamide เป็นยาลำดับถัดไปในรายดื้อ/กลับเป็นซ้ำบ่อย
- Plasmapheresis ใช้ใน anti-GBM
- เจาะท้องอย่างเดียวไม่แก้สาเหตุ ทำเฉพาะเมื่อ ascites ทำให้หายใจลำบาก
หมายเหตุ: สไลด์ถามสั้น ๆ ว่า "NS with ascites treatment?" โดยไม่ได้แสดงเฉลย — ข้อนี้เรียบเรียงใหม่ให้ชัด''',
            pearl="เด็ก NS typical → prednisolone เลย ไม่ต้อง biopsy", topic="Childhood NS",
            ref=[f"{D} หน้า 119–121, 138–139"], nl=["2.3.14(12)", "B9.2.2(4)"]),
    ])

# ---------------------------------------------------------------- 03-02 Diabetic nephropathy
S2 = sec("nephro-03-02", "Diabetic nephropathy (diabetic kidney disease)",
    "สาเหตุ CKD อันดับ 1 · มักมี retinopathy · microalbuminuria → nephrotic · KW nodule · biopsy เมื่อ atypical", minutes=7,
    source=f"{D} หน้า 122–124, 132–135", nl=["2.3.14(12)", "2.3.4(1)", "2.3.14(3)"],
    md='''
### ภาพรวม

- **Most common cause of CKD** (และ ESRD)
- Onset
  - **Type 1 DM: > 10–15 ปีหลังวินิจฉัย**
  - **Type 2 DM: พบได้ตั้งแต่วินิจฉัย** (เพราะเป็นเบาหวานมานานก่อนรู้ตัว)
- **ส่วนใหญ่มักมี diabetic retinopathy ร่วม** (microvascular เหมือนกัน)
- Progression: **microalbuminuria → nephrotic-range proteinuria** ในหลายปี + ↑BP + ↓GFR

### ระยะ albuminuria (เสริม)

| UACR (mg/g) | ชื่อเดิม | ความหมาย |
|---|---|---|
| < 30 | Normal | |
| 30–300 | Microalbuminuria (A2) | ระยะเริ่มต้น ตรวจคัดกรองทุกปี |
| > 300 | Macroalbuminuria (A3) | overt nephropathy → nephrotic ได้ |

### Pathology

- GBM หนา, mesangial expansion → **nodular glomerulosclerosis (Kimmelstiel–Wilson nodules)** (LM)
- Hyaline arteriolosclerosis ทั้ง afferent และ efferent (เสริม)

### Kidney biopsy — มักไม่จำเป็น ยกเว้น (atypical)

- **Active sediment** (RBC, RBC casts)
- **Rapidly progressive albuminuria**
- **GFR ลดลงเร็ว / GFR < 30**
- **ไม่มี diabetic retinopathy ใน T1DM**

> ข้อสอบชอบ: DM + retinopathy แต่ **RBC 10–20 + proteinuria เพิ่มเร็ว + Cr ขึ้นเร็วใน 1 เดือน** = atypical → **renal biopsy** หาโรคไตอื่นซ้อน

### การรักษา

- **คุมน้ำตาล + ACEI** (หรือ ARB) — ลด intraglomerular pressure และ proteinuria
- CKD management (SGLT2i, statin, คุมความดัน)
- (เสริม) แนวทางปัจจุบัน (KDIGO 2022/ADA): **SGLT2 inhibitor** ทุกรายที่ eGFR ≥ 20 และพิจารณา finerenone/GLP-1 RA
''',
    pearls=[
        "Diabetic nephropathy = สาเหตุ CKD อันดับ 1 · มักมี retinopathy ร่วม",
        "T1DM เกิดหลัง 10–15 ปี · T2DM เกิดได้ตั้งแต่วินิจฉัย",
        "LM: nodular glomerulosclerosis (Kimmelstiel–Wilson)",
        "Biopsy เมื่อ: active sediment, albuminuria/GFR ลดเร็ว, GFR <30, T1DM ไม่มี retinopathy",
        "Tx: คุมน้ำตาล + ACEI/ARB (+ SGLT2i)",
    ],
    items=[
        mcq("NEPHRO-03-02-1",
            "A 50-year-old man with diabetes for 15 years has bilateral leg swelling for 2 months. BP 150/80 mmHg. Fundoscopy shows diabetic retinopathy. Urinalysis: glucose 2+, protein 4+, RBC 2–3/HPF, granular casts 1–2/LPF. Which renal pathology is most likely?",
            "Nodular glomerulosclerosis",
            ["Minimal change glomerulopathy", "Membranous nephropathy", "Membranoproliferative glomerulonephritis", "Focal segmental glomerulosclerosis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''DM 15 ปี + **diabetic retinopathy** + nephrotic-range proteinuria โดย sediment ไม่ active = **diabetic nephropathy** พยาธิสภาพคือ **nodular glomerulosclerosis (Kimmelstiel–Wilson nodule)**
- Minimal change และ FSGS เป็น primary NS ที่ไม่สัมพันธ์กับเบาหวาน
- Membranous nephropathy พบในวัยนี้ได้ แต่เมื่อมี retinopathy ร่วมให้นึกถึง DN ก่อน
- MPGN จะมี hematuria และ complement ต่ำ''',
            pearl="DM + retinopathy + NS = KW nodule", topic="Diabetic nephropathy pathology",
            ref=[f"{D} หน้า 124, 132–133"], nl=["2.3.14(12)", "2.3.4(1)"]),
        mcq("NEPHRO-03-02-2",
            "A patient with type 2 diabetes and known diabetic retinopathy has urinalysis showing albumin 2+ and RBC 10–20/HPF (dysmorphic). The 24-hour urine protein is 22 g/day, and creatinine increased from 1.8 to 2.6 mg/dL over 1 month. What is the most appropriate next step?",
            "Renal biopsy",
            ["Hemodialysis", "CT abdomen", "Conclude diabetic nephropathy and no further investigation", "ANA only"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''แม้มี retinopathy แต่มีลักษณะ **atypical**: active sediment (dysmorphic RBC), proteinuria หนักมาก และ **Cr เพิ่มเร็วใน 1 เดือน** → ต้อง **renal biopsy** หาโรคไตอื่นที่รักษาได้ (สไลด์: atypical DN = active urine sediment, rapid ↑Cr)
- Hemodialysis ยังไม่มีข้อบ่งชี้ (ไม่มี AEIOU)
- CT abdomen ไม่ช่วยวินิจฉัยโรค glomerulus และ contrast เป็นอันตราย
- สรุปเป็น DN เลยผิด เพราะมีข้อบ่งชี้ biopsy ครบ
- ANA ช่วยได้บางส่วน แต่ไม่ครอบคลุมสาเหตุอื่นเท่า biopsy''',
            pearl="DM + active sediment หรือ Cr ขึ้นเร็ว → biopsy", topic="Atypical DN",
            ref=[f"{D} หน้า 124, 134–135"], nl=["2.3.14(12)"]),
        mcq("NEPHRO-03-02-3",
            "A 55-year-old woman with type 2 diabetes for 8 years has BP 142/88 mmHg, HbA1c 7.6%, eGFR 58 mL/min/1.73 m2, and urine albumin-to-creatinine ratio 420 mg/g. Which medication most directly slows progression of her kidney disease?",
            "Losartan",
            ["Amlodipine", "Hydrochlorothiazide", "Atenolol", "Glipizide"],
            explain='''DN ที่มี albuminuria (UACR > 300) → **ACEI/ARB** (losartan) ลด intraglomerular pressure ลด proteinuria และชะลอไตเสื่อม ตามสไลด์ (Tx: control blood sugar, ACEI) — ปัจจุบันเพิ่ม SGLT2i ด้วย (เสริม)
- Amlodipine ลดความดันได้ แต่ไม่ลด proteinuria เท่า RAS blocker
- Thiazide และ atenolol ลดความดันแต่ไม่มีผลปกป้องไตเฉพาะ
- Glipizide คุมน้ำตาลได้ แต่ไม่มีผลปกป้องไตโดยตรงและเสี่ยง hypoglycemia เมื่อไตเสื่อม''',
            pearl="DN + albuminuria → ACEI/ARB (+ SGLT2i)", topic="DN treatment",
            ref=[f"{D} หน้า 122, 148"], nl=["2.3.4(1)", "2.3.14(3)"]),
    ])

# ---------------------------------------------------------------- 03-03 MCD
S3 = sec("nephro-03-03", "Minimal change disease (MCD)",
    "NS ที่พบบ่อยที่สุดในเด็ก · onset เฉียบพลัน · LM ปกติ EM foot process effacement · ตอบสนอง prednisolone ดีมาก", minutes=5,
    source=f"{D} หน้า 125, 136–137", nl=["2.3.14(12)", "B9.2.2(4)"],
    md='''
### ลักษณะ

- **Most common nephrotic syndrome in children** (ราว 80–90% ของเด็ก 1–10 ปี (เสริม))
- **Bimodal age**: เด็ก และผู้สูงอายุ
- **Abrupt onset** (วัน–สัปดาห์) — เด็กบวมหนังตา บวมอัณฑะ (scrotal edema)
- Proteinuria หนักมาก (selective — albumin เป็นหลัก (เสริม)), ไม่มี hematuria ความดันปกติ Cr ปกติ
- สาเหตุ secondary ที่ข้อสอบชอบ (เสริม): **NSAID**, Hodgkin lymphoma

### พยาธิสภาพ

- **LM: no changes** (จึงเรียก minimal change)
- IF: negative (เสริม)
- **EM: effacement of podocyte foot processes**

### การรักษา

- **Prednisolone — responds well** (เด็กส่วนใหญ่ remission ใน 4–8 สัปดาห์)
- **Kidney biopsy กรณี not response** (steroid-resistant → คิด FSGS)
- กลับเป็นซ้ำได้บ่อย (เสริม)

> โจทย์คลาสสิก: เด็ก 8 ปี บวม scrotal edema, protein 4+, RBC 0–1, Cr ปกติ ให้ prednisone แล้วดีขึ้นใน 2–3 สัปดาห์ → MCD
''',
    pearls=[
        "MCD = NS ที่พบบ่อยที่สุดในเด็ก · บวมเร็ว · ไม่มี hematuria · BP/Cr ปกติ",
        "MCD: LM ปกติ · EM foot process effacement",
        "ตอบสนอง prednisolone ดีมาก ไม่ต้อง biopsy ก่อนในเด็ก",
        "NSAID และ Hodgkin lymphoma ทำ MCD ได้ (เสริม)",
    ],
    items=[
        mcq("NEPHRO-03-03-1",
            "An 8-year-old boy presents with bilateral ankle swelling for 1 day. Vital signs are normal. He has scrotal edema and pitting edema 2+ of both legs. Cr 0.8 mg/dL, albumin 2.6 g/dL. Urinalysis: protein 4+, RBC 0–1/HPF, WBC 0–1/HPF, fatty casts. Prednisone is started, and over the following weeks the edema and urinalysis improve significantly. What is the most likely diagnosis?",
            "Minimal change disease",
            ["Membranoproliferative glomerulonephritis", "IgA nephropathy", "Focal segmental glomerulosclerosis", "Membranous nephropathy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''เด็ก + nephrotic ล้วน (ไม่มี hematuria BP/Cr ปกติ) + onset เร็ว + **ตอบสนองดีต่อ prednisone** = **MCD**
- MPGN มี hematuria ความดันสูง complement ต่ำ และตอบสนอง steroid น้อย
- IgA nephropathy เด่นที่ hematuria
- FSGS มักมีความดันสูง hematuria และตอบสนอง steroid เพียงบางส่วน
- MN พบในผู้ใหญ่กลางคน–สูงอายุ onset ช้า''',
            pearl="เด็ก NS + ตอบสนอง steroid = MCD", topic="MCD",
            ref=[f"{D} หน้า 125, 136–137"], nl=["2.3.14(12)"]),
        mcq("NEPHRO-03-03-2",
            "A 68-year-old man develops abrupt-onset nephrotic syndrome 3 weeks after starting regular ibuprofen for back pain. Kidney biopsy shows normal glomeruli on light microscopy and negative immunofluorescence. Which electron microscopic finding is expected?",
            "Diffuse effacement of podocyte foot processes",
            ["Subepithelial deposits with spikes of basement membrane", "Subendothelial deposits with GBM duplication", "Mesangial electron-dense deposits", "Subepithelial humps"],
            explain='''LM ปกติ + IF ลบ + nephrotic เฉียบพลันหลังใช้ NSAID = **MCD** (bimodal age — ผู้สูงอายุก็เป็นได้) EM พบ **foot process effacement**
- Subepithelial deposit + spike เป็น membranous nephropathy ซึ่ง LM จะเห็น GBM หนา
- Subendothelial deposit + GBM duplication (tram-track) เป็น MPGN
- Mesangial deposit เป็น IgAN
- Subepithelial humps เป็น APSGN''',
            pearl="MCD: LM ปกติ IF ลบ EM effacement", topic="MCD pathology",
            ref=[f"{D} หน้า 125"], nl=["B9.2.2(4)"]),
    ])

# ---------------------------------------------------------------- 03-04 FSGS
S4 = sec("nephro-03-04", "Focal segmental glomerulosclerosis (FSGS)",
    "วัยหนุ่มสาว–กลางคน · onset สัปดาห์–เดือน · มี HT/hematuria/ไตเสื่อมได้ · segmental sclerosis · steroid ตอบสนองบางส่วน", minutes=5,
    source=f"{D} หน้า 126, 117", nl=["2.3.14(12)"],
    md='''
### ลักษณะ

- **Age: young–middle** · **Onset: สัปดาห์–เดือน**
- Proteinuria (↑↑) ร่วมกับ **HT (↑↑), hematuria (↑), renal failure (↑↑)** มากกว่า MCD
- ตอบสนอง steroid **บางส่วน (++)**
- สาเหตุ (เสริม): primary (podocyte injury), secondary — **HIV (collapsing variant), heroin**, obesity, reflux nephropathy, nephron mass ลด, APOL1 (เชื้อสายแอฟริกัน)

### พยาธิสภาพ

- **LM: segmental sclerosis** (บางส่วนของบาง glomerulus — focal & segmental)
- **EM: effacement of podocyte foot processes (~MCD)**

> FSGS กับ MCD อาจเป็น spectrum เดียวกัน: เด็ก NS ที่ไม่ตอบสนอง steroid → biopsy มักเจอ FSGS (เสริม)

### การรักษา

- **Prednisolone** (ตามสไลด์) ± calcineurin inhibitor ถ้าดื้อ (เสริม)
- Supportive: ACEI/ARB, statin, diuretic
- Secondary FSGS → รักษาสาเหตุ (เช่น ARV ใน HIV) ไม่ให้ steroid (เสริม)
''',
    pearls=[
        "FSGS: ผู้ใหญ่ตอนต้น NS + HT + hematuria + Cr ขึ้น · ตอบสนอง steroid ไม่ดีเท่า MCD",
        "LM segmental sclerosis · EM effacement (เหมือน MCD)",
        "HIV/heroin → FSGS (HIV = collapsing) (เสริม)",
    ],
    items=[
        mcq("NEPHRO-03-04-1",
            "A 32-year-old man with untreated HIV infection presents with nephrotic syndrome (proteinuria 9 g/day) and Cr 2.1 mg/dL. Ultrasound shows enlarged echogenic kidneys. What is the most likely glomerular lesion?",
            "Focal segmental glomerulosclerosis (collapsing variant)",
            ["Minimal change disease", "Membranous nephropathy", "IgA nephropathy", "Diabetic nodular glomerulosclerosis"],
            explain='''HIV-associated nephropathy (HIVAN) = **collapsing FSGS** มาด้วย nephrotic-range proteinuria ไตวายเร็ว ไตขนาดใหญ่และ echogenic (เสริม — สไลด์ระบุ HIV เป็นสาเหตุ secondary NS)
- MCD ไม่ทำให้ไตวายเร็วและไตโต
- Membranous สัมพันธ์กับ HBV/มะเร็งมากกว่า HIV
- IgAN เด่นที่ hematuria
- KW nodule เป็นของเบาหวาน''',
            pearl="HIV + NS + ไตโต = collapsing FSGS (HIVAN)", topic="Secondary FSGS",
            ref=[f"{D} หน้า 114, 126"], nl=["2.3.14(12)"]),
        mcq("NEPHRO-03-04-2",
            "A 26-year-old woman has edema for 2 months. BP 150/95 mmHg. Urinalysis: protein 3+, RBC 5–10/HPF. 24-hour urine protein 5.2 g, Cr 1.5 mg/dL. Serology for SLE, hepatitis B/C, and HIV is negative; C3 and C4 are normal. Kidney biopsy shows sclerosis in portions of some glomeruli, and electron microscopy shows diffuse foot-process effacement. What is the most appropriate initial specific therapy?",
            "Prednisolone",
            ["Plasmapheresis", "Penicillin V", "Observation without treatment", "Intravenous cyclophosphamide plus plasmapheresis"],
            explain='''Segmental sclerosis ใน glomerulus บางส่วน + foot-process effacement + secondary cause ลบหมด = **primary FSGS** สไลด์ให้ **prednisolone** (ตอบสนองได้ราวครึ่งหนึ่ง) ร่วมกับ ACEI/ARB
- Plasmapheresis เป็นการรักษา anti-GBM (หรือ FSGS ที่กลับเป็นซ้ำหลังปลูกถ่ายไต (เสริม))
- Penicillin ใช้ใน APSGN ที่ยังติดเชื้อ
- ปล่อยไว้เฉย ๆ ไม่เหมาะกับ proteinuria > 3.5 g และ Cr ขึ้น
- Cyclophosphamide + plasmapheresis เป็นสูตรของ anti-GBM/vasculitis''',
            pearl="Primary FSGS → prednisolone", topic="FSGS treatment",
            ref=[f"{D} หน้า 120, 126"], nl=["2.3.14(12)"]),
    ])

# ---------------------------------------------------------------- 03-05 MN
S5 = sec("nephro-03-05", "Membranous nephropathy (MN)",
    "NS ในผู้ใหญ่กลางคน–สูงอายุ · onset ช้า · GBM หนา spike & dome · anti-PLA2R · หามะเร็ง/HBV · pred + immunosuppressant", minutes=5,
    source=f"{D} หน้า 127, 117", nl=["2.3.14(12)", "B9.2.2(4)"],
    md='''
### ลักษณะ

- **Age: middle–old** — สาเหตุ primary NS ที่พบบ่อยในผู้ใหญ่ (เสริม)
- **Slow onset (เดือน–ปี)**, proteinuria หนักมาก (↑↑↑↑), RBC มักไม่มี ไตเสื่อมช้า
- **เสี่ยง renal vein thrombosis มากที่สุดในกลุ่ม NS** (เสริม) — ปวดเอว hematuria ฉับพลัน, PE
- Primary: antibody ต่อ **PLA2R** บน podocyte (~70%) (เสริม)
- Secondary (เสริม): **solid tumor (ปอด ลำไส้ เต้านม)**, **HBV**, HCV, SLE class V, ยา (NSAID, gold, penicillamine)

### พยาธิสภาพ

- **LM: diffuse thickened glomerular capillary loops & basement membrane**, **spike & dome appearance** (silver stain)
- IF: granular IgG + C3 ตามผนัง capillary (เสริม)
- EM: **subepithelial deposits** (เสริม)

### การรักษา

- **Prednisolone + immunosuppressants** (cyclophosphamide หรือ calcineurin inhibitor, rituximab ในแนวทางปัจจุบัน (เสริม))
- Supportive: ACEI/ARB, statin, anticoagulation ถ้า albumin < 2 g/dL
- ผู้สูงอายุ → ตรวจหามะเร็งตามอายุ (สไลด์: malignancy screening ตาม age group)
''',
    pearls=[
        "MN: ผู้ใหญ่กลางคน–สูงอายุ NS onset ช้า · GBM หนา spike & dome · subepithelial deposit",
        "MN → หามะเร็ง HBV SLE · เสี่ยง renal vein thrombosis สูง",
        "Tx: prednisolone + immunosuppressant",
    ],
    items=[
        mcq("NEPHRO-03-05-1",
            "A 62-year-old man has progressive leg edema over 6 months. BP 135/85 mmHg. Urinalysis: protein 4+, no RBC. Albumin 2.2 g/dL, cholesterol 380 mg/dL, Cr 1.1 mg/dL. Kidney biopsy shows diffusely thickened glomerular capillary walls with spikes on silver stain. Which associated condition should be actively searched for?",
            "Solid organ malignancy",
            ["Recent streptococcal pharyngitis", "Upper respiratory infection within 5 days", "Anti-GBM antibody", "Recent heavy exercise"],
            explain='''ผู้ใหญ่สูงอายุ NS onset ช้า + **GBM หนา + spike** = **membranous nephropathy** ซึ่ง secondary cause สำคัญในผู้สูงอายุคือ **มะเร็ง solid organ** (ปอด ลำไส้ เต้านม) ต้อง screening ตามอายุ (ร่วมกับ HBV, HCV, SLE)
- Streptococcal pharyngitis นำไปสู่ APSGN ซึ่งเป็น nephritic
- URI ภายใน 5 วันสัมพันธ์กับ IgAN
- Anti-GBM ให้ภาพ crescent + linear IgG
- ออกกำลังหนักทำ rhabdomyolysis ไม่ใช่ NS''',
            pearl="MN ในผู้สูงอายุ → หามะเร็ง", topic="Secondary MN",
            ref=[f"{D} หน้า 119, 127"], nl=["2.3.14(12)"]),
        mcq("NEPHRO-03-05-2",
            "A 55-year-old woman with nephrotic syndrome due to membranous nephropathy (albumin 1.8 g/dL) develops sudden left flank pain, gross hematuria, and a rise in Cr from 1.0 to 1.9 mg/dL. Which complication is most likely?",
            "Renal vein thrombosis",
            ["Acute pyelonephritis", "Ureteric stone", "Acute interstitial nephritis from furosemide", "Transformation to IgA nephropathy"],
            explain='''NS เสีย antithrombin ทางปัสสาวะ ทำให้เลือดแข็งตัวง่าย และ **MN เสี่ยง renal vein thrombosis มากที่สุด** โดยเฉพาะ albumin < 2 g/dL → ปวดเอวฉับพลัน hematuria Cr ขึ้น (เสริม) — นี่คือเหตุผลที่สไลด์ให้ anticoagulant ป้องกันเมื่อ albumin < 2
- Pyelonephritis ต้องมีไข้ pyuria
- นิ่วปวดแบบ colic แต่ไม่สัมพันธ์กับ NS และไม่ใช่ภาวะแทรกซ้อนที่คาดได้จากโรคนี้
- AIN จาก furosemide เป็นไปได้น้อยและไม่ทำปวดเอวฉับพลันกับ gross hematuria
- MN ไม่เปลี่ยนเป็น IgAN''',
            pearl="MN + albumin <2 + ปวดเอว hematuria = renal vein thrombosis", topic="NS complication",
            ref=[f"{D} หน้า 113, 121"], nl=["2.3.14(12)"]),
    ])

LECTURE = lecture("03", "Nephrotic syndrome", "NS approach · diabetic nephropathy · MCD · FSGS · MN",
    objectives=[
        "วินิจฉัย nephrotic syndrome และบอกกลไกของ edema, lipid สูง, thrombosis, infection ได้",
        "แยก MCD, FSGS, MN, MPGN จากอายุ onset UA การตอบสนอง steroid และพยาธิสภาพได้",
        "บอกข้อบ่งชี้ renal biopsy ใน NS และใน diabetic nephropathy ได้",
        "สั่ง supportive และ specific treatment ของ NS ได้",
    ],
    sections=[S1, S2, S3, S4, S5])
