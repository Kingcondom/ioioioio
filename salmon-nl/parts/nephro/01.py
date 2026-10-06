from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Nephro"

# ---------------------------------------------------------------- 01-01 UA
S1 = sec("nephro-01-01", "UA interpretation & urinary casts",
    "อ่าน UA ให้เป็นก่อน: sp.gr. · protein · RBC/WBC · cast บอกตำแหน่งโรคในไต", minutes=6,
    source=f"{D} หน้า 5–6, 17, 48", nl=["B9.3(2)", "2.1.43"],
    md='''
UA คือเครื่องมือแรกที่บอกได้ว่าปัญหาอยู่ **ก่อนไต ในไต หรือหลังไต** และถ้าอยู่ในไต อยู่ส่วนไหน (tubule · interstitium · glomerulus) — ข้อสอบ NL ให้ผล UA มาแทบทุกข้อในหมวดนี้

### UA 5 แบบที่ต้องจำ (ตามสไลด์)

| ภาวะ | Appearance | Sp.gr. | Protein | RBC | WBC | Cast |
|---|---|---|---|---|---|---|
| UTI | ขุ่น (cloudy, turbid) | อะไรก็ได้ | +/- | +/- | **+** | ไม่มี |
| Dehydrated (prerenal) | เหลืองเข้ม | **สูง** | +/- | - | - | **Hyaline cast** |
| ATN | เหลืองเข้ม | **ต่ำ (~1.010)** | +/- | +/- | +/- | **Muddy brown cast** |
| Nephrotic | เป็นฟอง (foamy) | สูง | **↑↑↑** | - | - | **Fatty cast** |
| Nephritic | แดง/น้ำตาล | สูง | ↑ ถึง ↑↑ | **+ dysmorphic RBC** | +/- | **RBC cast** |

### Cast บอกตำแหน่ง

Cast เกิดจาก Tamm–Horsfall protein จับตัวเป็นแท่งใน tubule แล้วห่อสิ่งที่อยู่ในท่อออกมา จึงบอกว่า "สิ่งนั้นมาจากในไต" (เสริม)

| Cast | ความหมาย |
|---|---|
| Hyaline cast | ปกติได้ · prerenal/dehydration |
| Muddy brown granular cast + renal tubular epithelial cell | **ATN** |
| RBC cast | **Glomerulonephritis** |
| WBC cast | **AIN** หรือ pyelonephritis |
| Fatty cast / oval fat body | **Nephrotic syndrome** |
| Broad (waxy) cast | **CKD** (ท่อที่ขยายและฝ่อ) |

> ข้อสอบชอบ: "Broad waxy cast" = เรื้อรัง → คิดถึง CKD/chronic GN ไม่ใช่ AKI

### Urine sp.gr. → Urine Osm (สูตรลัด)

เอา **เลขสองหลักท้ายของ sp.gr. × 30** ≈ Urine Osm (mOsm/kg)

- sp.gr. 1.003 → 3 × 30 = **90** (เจือจาง เช่น polydipsia/DI)
- sp.gr. 1.010 → 10 × 30 = **300** (isosthenuria เท่า plasma → ATN/CKD ที่ไตเข้มข้นปัสสาวะไม่ได้)
- sp.gr. 1.030 → 30 × 30 = **900** (เข้มข้นมาก → prerenal/dehydration)

> sp.gr. ใช้ประมาณได้เฉพาะเมื่อไม่มีสารโมเลกุลใหญ่ในปัสสาวะ เช่น glucose, contrast, protein มาก ซึ่งจะทำให้ sp.gr. สูงเกินจริง (เสริม)

### Glomerular vs Non-glomerular hematuria

| | Glomerular | Non-glomerular |
|---|---|---|
| RBC cast | อาจพบ | ไม่พบ |
| Dysmorphic RBC | อาจพบ | ไม่พบ |
| Proteinuria | อาจพบ | ไม่พบ |
| ลิ่มเลือด (clot) | **ไม่พบ** | อาจพบ |

- Glomerular → คิด GN (ไปหมวด nephritic)
- Non-glomerular (เลือดสด มี clot ไม่มี dysmorphic RBC) → นิ่ว เนื้องอกกระเพาะปัสสาวะ/ไต การติดเชื้อ — ผู้สูงอายุสูบบุหรี่ต้องคิดถึง bladder cancer (เสริม)
''',
    pearls=[
        "Muddy brown cast = ATN · RBC cast = GN · WBC cast = AIN/pyelonephritis · Fatty cast = nephrotic · Broad waxy cast = CKD",
        "Urine Osm ≈ เลขสองหลักท้ายของ sp.gr. × 30 (1.010 ≈ 300 = isosthenuria)",
        "Dysmorphic RBC/RBC cast/proteinuria = glomerular · มี clot = non-glomerular",
        "Sp.gr. สูง + hyaline cast = prerenal (dehydration)",
    ],
    items=[
        mcq("NEPHRO-01-01-1",
            "A 62-year-old man is admitted with septic shock from pneumonia. Blood pressure was below 80/50 mmHg for 10 hours before resuscitation. On day 3, urine output falls and creatinine rises from 1.0 to 3.4 mg/dL. Which urine sediment finding is most expected?",
            "Muddy brown granular casts with renal tubular epithelial cells",
            ["Hyaline casts only", "Red blood cell casts with dysmorphic RBC", "White blood cell casts with eosinophiluria", "Fatty casts and oval fat bodies"],
            explain='''ช็อกนานหลายชั่วโมงทำให้ renal blood flow ลดนานจน tubule ขาดเลือดตาย = **ischemic ATN** เซลล์ท่อไตที่หลุดลอกจับกับ Tamm–Horsfall protein เป็น **muddy brown granular cast** และพบ renal tubular epithelial cell
- Hyaline cast อย่างเดียว เป็นภาพของ prerenal ที่ tubule ยังดี ซึ่งในรายนี้ช็อกนานจนเลยระยะ prerenal ไปแล้ว
- RBC cast + dysmorphic RBC บอกว่า glomerulus อักเสบ (GN) ไม่เข้ากับประวัติช็อก
- WBC cast + eosinophil เป็นภาพของ AIN จากยา
- Fatty cast/oval fat body พบใน nephrotic syndrome ที่มี proteinuria หนัก''',
            pearl="ช็อกนาน → ischemic ATN → muddy brown granular cast", topic="Urinary casts",
            ref=[f"{D} หน้า 5, 19"], nl=["B9.3(2)"]),
        mcq_ordered("NEPHRO-01-01-2",
            "A 30-year-old woman has vomiting and poor oral intake for 3 days. Urinalysis shows specific gravity 1.025 with no glucose or protein. Approximately what urine osmolality (mOsm/kg) does this specific gravity represent?",
            ["250", "500", "750", "1,000", "1,250"], 2,
            explain='''ใช้สูตรลัดในสไลด์: เลขสองหลักท้ายของ sp.gr. × 30 → 25 × 30 = **750 mOsm/kg** แปลว่าไตเข้มข้นปัสสาวะได้ดีและมี ADH ทำงาน เข้ากับภาวะขาดน้ำ (prerenal)
- 250 ใกล้เคียง sp.gr. ประมาณ 1.008 ซึ่งเจือจางกว่ามาก
- 500 ตรงกับ sp.gr. ประมาณ 1.017
- 1,000 และ 1,250 ต้องใช้ sp.gr. ราว 1.033–1.042 ซึ่งสูงเกินที่ไตคนทั่วไปทำได้ ถ้าเห็นค่านี้ให้สงสัยสารแปลกปลอม เช่น glucose หรือ contrast''',
            pearl="Urine Osm ≈ (เลขท้ายของ sp.gr.) × 30", topic="Sp.gr. to osmolality",
            ref=[f"{D} หน้า 17"], nl=["B9.3(2)", "B9.3(3)"]),
        mcq("NEPHRO-01-01-3",
            "A 45-year-old woman with long-standing hypertension presents with fatigue and nausea for 2 weeks. BP 180/110 mmHg, pale conjunctivae. Cr 6.8 mg/dL. Urinalysis: sp.gr. 1.010, protein 2+, RBC 5–10/HPF, broad waxy casts 1–2/LPF. Which finding most strongly suggests a chronic rather than acute process?",
            "Broad waxy casts",
            ["Specific gravity 1.010", "Protein 2+", "Microscopic hematuria", "Blood pressure 180/110 mmHg"],
            explain='''**Broad waxy cast** เกิดใน tubule ที่ขยายและฝ่อจากโรคไตเรื้อรัง สไลด์เน้นว่า broad cast = CKD (ร่วมกับซีด = anemia of CKD)
- Sp.gr. 1.010 (isosthenuria) พบได้ทั้ง ATN และ CKD จึงแยกไม่ได้
- Protein 2+ และ microscopic hematuria พบได้ทั้ง AKI จาก GN และ CKD
- ความดันสูงมากพบได้ทั้ง AGN เฉียบพลันและ CKD''',
            pearl="Broad waxy cast = CKD", topic="AKI vs CKD",
            ref=[f"{D} หน้า 8, 81–82"], nl=["B9.3(2)", "2.3.14(3)"]),
        mcq("NEPHRO-01-01-4",
            "A 68-year-old man who has smoked for 40 years presents with painless gross hematuria with clots for 1 week. Vital signs are normal. Urinalysis: RBC numerous, isomorphic, no RBC casts, protein trace. Cr 0.9 mg/dL. What is the most appropriate next investigation?",
            "CT urography and cystoscopy",
            ["Renal biopsy", "Serum C3 and C4", "ASO titer", "24-hour urine protein"],
            explain='''มี clot, RBC รูปร่างปกติ (isomorphic), ไม่มี RBC cast และ proteinuria น้อย = **non-glomerular hematuria** ในชายสูงอายุสูบบุหรี่ต้องหามะเร็งทางเดินปัสสาวะ (bladder/upper tract urothelial cancer, RCC) ด้วย CT urography และ cystoscopy (เสริม)
- Renal biopsy ใช้กับ glomerular disease ไม่ใช่ hematuria ที่มี clot
- C3/C4 และ ASO ใช้แยกสาเหตุของ GN ซึ่งรายนี้ไม่มีลักษณะ glomerular
- 24-hour urine protein ใช้ประเมิน proteinuria ซึ่งมีเพียง trace''',
            pearl="Clot + isomorphic RBC = non-glomerular → หามะเร็งทางเดินปัสสาวะ", topic="Hematuria",
            ref=[f"{D} หน้า 48"], nl=["2.1.43", "B9.2.4-3(2)"]),
    ])

# ---------------------------------------------------------------- 01-02 AKI approach
F_AKI = fig("nephro-01-02-f1", "สาเหตุ AKI แบ่งตามตำแหน่ง", '''<svg viewBox="0 0 740 330">
 <defs><marker id="nephro-01-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <text x="120" y="24" text-anchor="middle" class="t3">เลือดไปไตลดลง</text>
 <text x="370" y="24" text-anchor="middle" class="t3">เนื้อไตเสีย</text>
 <text x="620" y="24" text-anchor="middle" class="t3">ทางออกปัสสาวะอุดตัน</text>
 <rect x="20" y="34" width="200" height="40" rx="10" class="c1"/>
 <text x="120" y="59" text-anchor="middle" class="tw">Pre-renal</text>
 <rect x="270" y="34" width="200" height="40" rx="10" class="ac"/>
 <text x="370" y="59" text-anchor="middle" class="tw">Renal (intrinsic)</text>
 <rect x="520" y="34" width="200" height="40" rx="10" class="c2"/>
 <text x="620" y="59" text-anchor="middle" class="tw">Post-renal</text>
 <path d="M222 54H266" class="ln" marker-end="url(#nephro-01-02-a)"/>
 <path d="M472 54H516" class="ln" marker-end="url(#nephro-01-02-a)"/>
 <rect x="20" y="86" width="200" height="226" rx="10" class="c1soft"/>
 <text x="32" y="108" class="tb">Hypovolemia</text>
 <text x="32" y="126" class="t3">เลือดออก อาเจียน ท้องเสีย burn</text>
 <text x="32" y="152" class="tb">↓BP</text>
 <text x="32" y="170" class="t3">sepsis, cardiogenic, anaphylaxis</text>
 <text x="32" y="196" class="tb">↓ECV</text>
 <text x="32" y="214" class="t3">cardiorenal (HF), hepatorenal</text>
 <text x="32" y="240" class="tb">Drugs</text>
 <text x="32" y="258" class="t3">NSAID, ACEI, ARB</text>
 <text x="32" y="276" class="t3">cyclosporine, tacrolimus</text>
 <rect x="270" y="86" width="200" height="226" rx="10" class="acsoft"/>
 <text x="282" y="108" class="tb">Tubule → ATN</text>
 <text x="282" y="126" class="t3">ischemic, contrast, AG, myoglobin</text>
 <text x="282" y="152" class="tb">Interstitium → AIN</text>
 <text x="282" y="170" class="t3">penicillin, PPI, NSAID</text>
 <text x="282" y="196" class="tb">Glomerulus</text>
 <text x="282" y="214" class="t3">GN, TTP/HUS, preeclampsia</text>
 <text x="282" y="240" class="tb">Large vessel</text>
 <text x="282" y="258" class="t3">bilateral RAS, renal artery/</text>
 <text x="282" y="276" class="t3">vein thrombosis, vasculitis</text>
 <rect x="520" y="86" width="200" height="226" rx="10" class="c2soft"/>
 <text x="532" y="108" class="tb">Ureter ทั้ง 2 ข้าง</text>
 <text x="532" y="126" class="t3">stone, tumor, blood clot</text>
 <text x="532" y="152" class="tb">Bladder neck</text>
 <text x="532" y="170" class="t3">BPH, stone, tumor</text>
 <text x="532" y="196" class="tb">Neurogenic bladder</text>
 <text x="532" y="222" class="tb">Urethra</text>
 <text x="532" y="240" class="t3">PUV, stricture, phimosis</text>
 <text x="532" y="266" class="tb">Drugs</text>
 <text x="532" y="284" class="t3">opioid, anticholinergic,</text>
 <text x="532" y="300" class="t3">sympathomimetics</text>
</svg>''', "ไล่จากซ้ายไปขวาตามทางเดินของเลือดเข้าไต → เนื้อไต → ทางออกปัสสาวะ แต่ละช่องคือกลุ่มสาเหตุตามสไลด์")

F_AKI2 = fig("nephro-01-02-f2", "Approach to AKI (ตามสไลด์)", '''<svg viewBox="0 0 740 400">
 <defs><marker id="nephro-01-02-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="38" rx="10" class="acsoft"/>
 <text x="370" y="34" text-anchor="middle" class="tb">AKI (Cr ↑ หรือ UO ↓)</text>
 <path d="M370 48V68" class="ln" marker-end="url(#nephro-01-02-b)"/>
 <rect x="200" y="70" width="340" height="48" rx="10" class="misssoft"/>
 <text x="370" y="90" text-anchor="middle" class="tb">สงสัย urinary retention?</text>
 <text x="370" y="108" text-anchor="middle" class="t3">→ single catheterization ก่อน</text>
 <path d="M370 118V138" class="ln" marker-end="url(#nephro-01-02-b)"/>
 <rect x="200" y="140" width="340" height="40" rx="10" class="box"/>
 <text x="370" y="165" text-anchor="middle" class="tb">U/S KUB · UA · FENa · review ยา</text>
 <path d="M260 180L110 212" class="ln" marker-end="url(#nephro-01-02-b)"/>
 <path d="M370 180V212" class="ln" marker-end="url(#nephro-01-02-b)"/>
 <path d="M480 180L630 212" class="ln" marker-end="url(#nephro-01-02-b)"/>
 <rect x="10" y="214" width="200" height="84" rx="10" class="c1soft"/>
 <text x="110" y="236" text-anchor="middle" class="tb">Pre-renal</text>
 <text x="110" y="256" text-anchor="middle" class="t3">BUN/Cr &gt; 20</text>
 <text x="110" y="272" text-anchor="middle" class="t3">FENa &lt; 1%</text>
 <text x="110" y="288" text-anchor="middle" class="t3">sp.gr. สูง, hyaline cast</text>
 <rect x="230" y="214" width="280" height="172" rx="10" class="acsoft"/>
 <text x="370" y="236" text-anchor="middle" class="tb">Renal</text>
 <text x="370" y="254" text-anchor="middle" class="t3">BUN/Cr &lt; 15 · FENa &gt; 1–2%</text>
 <text x="244" y="280" class="t2">sp.gr. 1.010 + muddy brown → ATN</text>
 <text x="244" y="302" class="t2">Blood + แต่ RBC น้อย → rhabdo/hemolysis</text>
 <text x="244" y="324" class="t2">Dysmorphic RBC, RBC cast → GN</text>
 <text x="244" y="346" class="t2">WBC cast, eosinophil → AIN</text>
 <text x="244" y="372" class="t3">ต่อด้วยประเมิน volume status</text>
 <rect x="530" y="214" width="200" height="84" rx="10" class="c2soft"/>
 <text x="630" y="236" text-anchor="middle" class="tb">Post-renal</text>
 <text x="630" y="256" text-anchor="middle" class="t3">Hydronephrosis</text>
 <text x="630" y="272" text-anchor="middle" class="t3">→ relieve obstruction</text>
 <rect x="10" y="314" width="200" height="72" rx="10" class="sunk"/>
 <text x="110" y="336" text-anchor="middle" class="tb">Volume status</text>
 <text x="110" y="356" text-anchor="middle" class="t3">Hypervolemic → diuretics</text>
 <text x="110" y="374" text-anchor="middle" class="t3">Eu/Hypovolemic → ลอง IV fluid</text>
 <path d="M110 298V312" class="ln" marker-end="url(#nephro-01-02-b)"/>
</svg>''', "เริ่มจากตัด retention ด้วยการสวนปัสสาวะ จากนั้นใช้ U/S + UA + FENa แยก 3 กลุ่ม แล้วจัดการ volume")

S2 = sec("nephro-01-02", "AKI: นิยาม สาเหตุ และ approach",
    "KDIGO: Cr ↑ ≥0.3 ใน 48 ชม. / ≥1.5 เท่าใน 7 วัน / UO <0.5 ml/kg/hr ≥6 ชม. · แยก prerenal–renal–postrenal", minutes=9,
    source=f"{D} หน้า 7–17, 28–29", nl=["2.3.14(3)", "B9.2.7(1)", "2.1.44"],
    md='''
### นิยาม AKI (ข้อใดข้อหนึ่ง)

- Creatinine เพิ่ม **≥ 0.3 mg/dL ภายใน 48 ชั่วโมง** หรือ
- Creatinine เพิ่ม **≥ 1.5 เท่าของ baseline ภายใน 7 วัน** หรือ
- Urine output **< 0.5 ml/kg/hr นาน ≥ 6 ชั่วโมง**

> AKI vs CKD: ถ้ามี broad cast, ไตเล็ก cortex บาง, ซีดจาก ↓EPO, Ca ต่ำ PO4 สูง → คิดว่าเป็น CKD เดิม (R/O CKD ก่อนเสมอ)

### สาเหตุแบ่ง 3 กลุ่ม

[[fig:nephro-01-02-f1]]

**Pre-renal** — ไตปกติ แต่เลือดไปเลี้ยงไม่พอ
- Hypovolemia: hemorrhage, vomiting, diarrhea, burns, diuretics, dehydration
- ↓BP: sepsis, cardiogenic shock, anaphylactic shock
- ↓Effective circulating volume: cardiorenal syndrome (CHF), hepatorenal syndrome (cirrhosis)
- **Drugs**: NSAID (หด afferent arteriole), ACEI/ARB (ขยาย efferent arteriole), calcineurin inhibitor (cyclosporine, tacrolimus)

**Renal (intrinsic)**
- Tubule: **ATN** — ischemic (prerenal ที่นานเกิน, ↓BP) หรือ nephrotoxic (radiocontrast, aminoglycoside, cisplatin, amphotericin B, tenofovir, hemoglobin, myoglobin)
- Interstitium: **AIN** — ยา (penicillin, PPI, NSAID), infection, infiltrative (lymphoma, sarcoidosis, amyloidosis)
- Glomerulus/microvascular: GN, TTP/HUS, preeclampsia
- Large renal vessel: bilateral renal artery stenosis, bilateral renal artery/vein thrombosis, vasculitis

**Post-renal** — การอุดตันต้องเป็น **ทั้งสองข้าง** (หรือข้างเดียวในคนที่มีไตข้างเดียว)
- Bilateral ureteral obstruction: stone, tumor, blood clot
- Bladder neck obstruction: stone, tumor, BPH · neurogenic bladder
- Urethral obstruction: posterior urethral valve, tumor, stricture, phimosis
- Drugs: opioid, sympathomimetics, anticholinergic (ทำให้ retention)

### Approach

[[fig:nephro-01-02-f2]]

### ตารางแยก 3 กลุ่ม (ท่องให้ขึ้นใจ)

| | Prerenal | Renal (ATN) | Postrenal |
|---|---|---|---|
| BUN/Cr ratio | **> 20** | **< 15** | แล้วแต่ |
| FENa | **< 1%** | **> 1–2%** | |
| FEUrea | **< 35%** | **> 50%** | |
| Urine Na (mEq/L) | **< 20** | **> 40** | |
| Urine Osm | **> 500** | **< 350** | < 350 |
| Sediment | Hyaline cast | Muddy brown (ATN) · RBC cast (GN) · WBC cast (AIN) · fatty cast (NS) | Hematuria (นิ่ว เนื้องอก ลิ่มเลือด) |

- FENa = (Urine Na × Plasma Cr) ÷ (Plasma Na × Urine Cr) × 100 (เสริม)
- **FEUrea ใช้แทน FENa เมื่อผู้ป่วยได้ diuretic** เพราะ diuretic ทำให้ FENa สูงเกินจริง แต่ urea ดูดกลับที่ proximal tubule ไม่ค่อยถูกกระทบ (เสริม)
- Prerenal: tubule ยังดี ดูด Na และน้ำกลับเต็มที่ → urine Na ต่ำ Uosm สูง และ urea ถูกดูดกลับมากขึ้น → BUN/Cr สูง
- ATN: tubule เสีย ดูด Na ไม่ได้ เข้มข้นปัสสาวะไม่ได้ → urine Na สูง sp.gr. ~1.010

> สไลด์เน้น: ถ้า **Cr สูงมาก (> 2.5)** โอกาสเป็น prerenal ล้วน ๆ น้อย มักเลยไปเป็น ATN แล้ว

### ยาที่ทำ Cr ขึ้นบ่อยในข้อสอบ

ผู้ป่วยใช้ ACEI อยู่เดิม แล้วเพิ่งเริ่ม **NSAID (naproxen, ibuprofen, diclofenac)** → prerenal AKI จาก NSAID (afferent หด + efferent ขยายจาก ACEI = "triple whammy" ถ้ามี diuretic ด้วย) (เสริม)
''',
    figs=[F_AKI, F_AKI2],
    pearls=[
        "AKI = Cr ↑ ≥0.3 ใน 48 ชม. หรือ ≥1.5 เท่าใน 7 วัน หรือ UO <0.5 ml/kg/hr ≥6 ชม.",
        "Prerenal: BUN/Cr >20, FENa <1%, UNa <20, Uosm >500, hyaline cast",
        "ATN: BUN/Cr <15, FENa >2%, sp.gr. 1.010, muddy brown cast",
        "ได้ diuretic อยู่ → ใช้ FEUrea (<35% = prerenal)",
        "สงสัย retention → single catheterization ก่อนทุกอย่าง",
    ],
    items=[
        mcq("NEPHRO-01-02-1",
            "A 68-year-old woman with hypertension on enalapril and amlodipine for 5 years recently started tramadol and naproxen for knee osteoarthritis. Her creatinine rose from 1.2 to 2.4 mg/dL over 1 week. Which drug is the most likely cause of the rising creatinine?",
            "Naproxen",
            ["Enalapril", "Amlodipine", "Tramadol", "Paracetamol"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ยาที่ **เพิ่งเริ่ม** และสัมพันธ์กับเวลาที่ Cr ขึ้นคือ **naproxen (NSAID)** ซึ่งยับยั้ง prostaglandin ที่ขยาย afferent arteriole → GFR ลดเป็น **prerenal AKI** โดยเฉพาะในคนที่ใช้ ACEI อยู่แล้ว
- Enalapril ทำ Cr ขึ้นได้ แต่ใช้มา 5 ปีโดย Cr คงที่ ตัวกระตุ้นใหม่คือ NSAID
- Amlodipine (CCB) ไม่ทำให้ GFR ลดลง
- Tramadol เป็น opioid ไม่มีพิษต่อไตโดยตรง (ถ้าทำให้ retention จะเป็น postrenal แต่โจทย์ไม่มีอาการปัสสาวะไม่ออก)
- Paracetamol ขนาดปกติไม่ทำให้ไตเสีย และผู้ป่วยไม่ได้กิน''',
            pearl="ACEI เดิม + เริ่ม NSAID → prerenal AKI", topic="Drug-induced prerenal AKI",
            ref=[f"{D} หน้า 28–29"], nl=["2.3.14(3)"]),
        mcq("NEPHRO-01-02-2",
            "Which of the following patients meets the KDIGO definition of acute kidney injury?",
            "Creatinine rises from 0.9 to 1.3 mg/dL within 36 hours",
            ["Creatinine rises from 1.0 to 1.25 mg/dL within 48 hours",
             "Creatinine rises from 1.0 to 1.4 mg/dL over 10 days",
             "Urine output 0.4 mL/kg/hr for 4 hours",
             "Creatinine stable at 2.0 mg/dL with eGFR 35 for 4 months"],
            explain='''Cr เพิ่ม 0.4 mg/dL ภายใน 36 ชั่วโมง ผ่านเกณฑ์ **เพิ่ม ≥ 0.3 mg/dL ภายใน 48 ชั่วโมง**
- 1.0 → 1.25 เพิ่มแค่ 0.25 ยังไม่ถึง 0.3
- 1.0 → 1.4 คือ 1.4 เท่า และใช้เวลา 10 วัน เกินกรอบ 7 วันของเกณฑ์ 1.5 เท่า
- UO < 0.5 ml/kg/hr ต้องนานอย่างน้อย 6 ชั่วโมง 4 ชั่วโมงยังไม่พอ
- Cr คงที่และ eGFR < 60 นาน > 3 เดือน คือ CKD ไม่ใช่ AKI''',
            pearl="AKI: +0.3 ใน 48 ชม. · ×1.5 ใน 7 วัน · UO <0.5 ≥6 ชม.", topic="KDIGO AKI definition",
            ref=[f"{D} หน้า 7"], nl=["B9.2.7(1)"]),
        mcq("NEPHRO-01-02-3",
            "A 75-year-old man has had diarrhea for 4 days. BP 96/60 mmHg, HR 108/min, dry mucosa. BUN 60 mg/dL, Cr 2.0 mg/dL. Urine Na 12 mEq/L, FENa 0.4%, urine osmolality 620 mOsm/kg, urinalysis shows hyaline casts only. What is the most appropriate management?",
            "Isotonic crystalloid infusion",
            ["Intravenous furosemide", "Urgent hemodialysis", "Renal biopsy", "Start low-dose dopamine infusion"],
            explain='''BUN/Cr = 30 (> 20), FENa < 1%, urine Na < 20, Uosm > 500, hyaline cast = **prerenal AKI** จาก hypovolemia → แก้ hemodynamics ด้วย **IV isotonic fluid** แล้ว Cr ควรลดลงภายใน 24–72 ชั่วโมง
- Furosemide ใช้เมื่อ hypervolemic จะทำให้รายนี้ขาดน้ำมากขึ้น
- Hemodialysis ไม่มีข้อบ่งชี้ (ไม่มี refractory hyperK, acidosis, overload หรือ uremic complication)
- Renal biopsy ไม่จำเป็นใน prerenal ที่ชัดเจน
- Low-dose dopamine ไม่ช่วยป้องกันหรือรักษา AKI (เสริม)''',
            pearl="Prerenal + hypovolemic → IV fluid", topic="Prerenal AKI",
            ref=[f"{D} หน้า 15–16, 25"], nl=["2.3.14(3)", "B9.4(2)"]),
        mcq("NEPHRO-01-02-4",
            "A 74-year-old man with benign prostatic hyperplasia was given chlorpheniramine for a cold 2 days ago. He now has lower abdominal discomfort and has passed only dribbles of urine. A tender suprapubic mass is palpable. Cr 2.6 mg/dL (baseline 1.0). What is the most appropriate initial step?",
            "Bladder catheterization",
            ["Intravenous normal saline 1 L bolus", "Intravenous furosemide", "CT abdomen with contrast", "Calculate fractional excretion of sodium"],
            explain='''ชายสูงอายุ BPH + ยา anticholinergic (chlorpheniramine) + คลำได้กระเพาะปัสสาวะโป่ง = **acute urinary retention → postrenal AKI** สไลด์ให้ทำ **single catheterization** ก่อนเป็นอย่างแรก ทั้งเพื่อวินิจฉัยและรักษา
- Bolus NSS ไม่แก้การอุดตันและทำให้กระเพาะปัสสาวะยิ่งโป่ง
- Furosemide เพิ่มปัสสาวะในระบบที่ทางออกอุดตัน ไม่ช่วย
- CT with contrast เสี่ยง contrast nephropathy และไม่จำเป็นก่อนสวนปัสสาวะ
- FENa ไม่ช่วยแยกในภาวะ retention ที่เห็นชัดแล้ว และไม่ใช่การรักษา''',
            pearl="สงสัย retention → single cath ก่อน", topic="Postrenal AKI",
            ref=[f"{D} หน้า 14–15"], nl=["2.2.29", "2.1.45"]),
        mcq("NEPHRO-01-02-5",
            "A 70-year-old woman with heart failure on furosemide develops AKI. BUN 72 mg/dL, Cr 2.4 mg/dL. FENa is 3.1% and fractional excretion of urea (FEUrea) is 24%. Urinalysis shows hyaline casts only. What is the most likely type of AKI?",
            "Prerenal AKI",
            ["Ischemic acute tubular necrosis", "Acute interstitial nephritis", "Postrenal AKI", "Acute glomerulonephritis"],
            explain='''ผู้ป่วยได้ **furosemide** ทำให้ FENa สูงเกินจริง ต้องดู **FEUrea < 35% = prerenal** ร่วมกับ BUN/Cr = 30 และ sediment มีแค่ hyaline cast → prerenal จาก ↓effective circulating volume (cardiorenal)
- ATN จะมี FEUrea > 50%, BUN/Cr < 15 และ muddy brown cast
- AIN จะมี WBC, WBC cast, eosinophil
- Postrenal ต้องเห็น hydronephrosis/ประวัติอุดตัน
- AGN จะมี dysmorphic RBC, RBC cast''',
            pearl="ได้ diuretic → ดู FEUrea (<35% prerenal, >50% ATN)", topic="FEUrea",
            ref=[f"{D} หน้า 16"], nl=["B9.3(4)"]),
    ])

# ---------------------------------------------------------------- 01-03 ATN
S3 = sec("nephro-01-03", "Acute tubular necrosis (ATN) & contrast nephropathy",
    "Ischemic vs nephrotoxic ATN · muddy brown cast · FENa >2% · ป้องกัน CIN ด้วย NSS ก่อนและหลังฉีด", minutes=7,
    source=f"{D} หน้า 18–20, 30–31, 36–39", nl=["2.3.14(3)", "B9.2.7(1)"],
    md='''
ATN = เซลล์ท่อไตบาดเจ็บ/ตาย → หลุดลอกอุดท่อ + ดูด Na/น้ำกลับไม่ได้ เป็นสาเหตุ intrinsic AKI ที่พบบ่อยที่สุดในโรงพยาบาล

### สาเหตุ

**Ischemic ATN** — renal blood flow ลดลงนาน (prerenal ที่ไม่ได้แก้ทัน, ช็อก, sepsis, ผ่าตัดใหญ่)

**Nephrotoxic ATN**

| Exogenous | Endogenous |
|---|---|
| Radiocontrast | Hemoglobin (intravascular hemolysis) |
| Aminoglycosides (gentamicin, amikacin) | Myoglobin (rhabdomyolysis) |
| Cisplatin, methotrexate | Uric acid (tumor lysis syndrome) |
| Amphotericin B | Immunoglobulin light chain (multiple myeloma) |
| Tenofovir | |

- Aminoglycoside: สะสมใน proximal tubule มักเกิด AKI หลังได้ยา 5–10 วัน (non-oliguric) และทำให้ hypoK/hypoMg ได้ (เสริม)

### การวินิจฉัย

- ↑BUN, Cr, **BUN/Cr ratio < 15**
- **FENa > 2%** (tubule ดูด Na ไม่ได้), urine sp.gr. ต่ำ ~1.010
- UA: **muddy brown granular cast**, renal tubular epithelial cell
- **Blood + บน dipstick** แต่ RBC น้อย → คิดถึง myoglobinuria/hemoglobinuria

### การรักษา

**Supportive** — หยุดยาที่เป็นพิษต่อไต ปรับขนาดยา แก้ volume/electrolyte และรักษาสาเหตุ (ส่วนใหญ่ฟื้นภายใน 1–3 สัปดาห์) · ให้ RRT ถ้ามีข้อบ่งชี้

### Contrast-induced nephropathy (CIN)

- AKI ภายหลังได้ IV contrast (มัก Cr ขึ้นใน 24–72 ชั่วโมง) (เสริม)
- กลุ่มเสี่ยง: CKD (โดยเฉพาะ eGFR < 45), DM, อายุมาก, volume depletion, contrast ปริมาณมาก (เสริม)
- รักษา: supportive, IV fluid, แก้ electrolyte
- **ป้องกัน: NSS ก่อนและหลังได้ contrast** (ตามสไลด์) · หยุด NSAID/diuretic ชั่วคราว ใช้ contrast น้อยที่สุด (เสริม)

> N-acetylcysteine และ sodium bicarbonate ไม่ได้ดีกว่า NSS ในการศึกษาใหญ่ (PRESERVE trial) — ข้อสอบตอบ **NSS** (เสริม)

> ข้อสอบชอบ: hypovolemia นาน + BUN 80 / Cr 8 (ratio 10) + sp.gr. 1.010 → **ischemic ATN** ไม่ใช่ prerenal
''',
    pearls=[
        "ATN: BUN/Cr <15, FENa >2%, sp.gr. 1.010, muddy brown granular cast",
        "Nephrotoxin ที่ออกสอบ: contrast, aminoglycoside, cisplatin, amphotericin B, tenofovir, myoglobin, hemoglobin",
        "ป้องกัน contrast nephropathy = NSS ก่อนและหลังฉีด",
        "Cr สูงมาก (>2.5) + sp.gr. ต่ำ → เลย prerenal ไปเป็น ATN แล้ว",
    ],
    items=[
        mcq("NEPHRO-01-03-1",
            "A 50-year-old man presents with hypovolemia and oliguria after several days of vomiting and poor intake. BUN 80 mg/dL, Cr 8 mg/dL. Urinalysis: specific gravity 1.010. What is the most likely diagnosis?",
            "Acute tubular necrosis",
            ["Acute interstitial nephritis", "Acute glomerulonephritis", "Prerenal azotemia", "Postrenal azotemia"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Hypovolemia ที่นานพอจะทำให้ tubule ขาดเลือดเป็น **ischemic ATN**: BUN/Cr = 10 (< 15), sp.gr. 1.010 (เข้มข้นปัสสาวะไม่ได้) และ Cr สูงถึง 8 ซึ่งสไลด์บอกว่า Cr > 2.5 โอกาสเป็น prerenal ล้วนน้อย
- Prerenal azotemia ไตยังเข้มข้นปัสสาวะได้ จะมี sp.gr. สูง และ BUN/Cr > 20
- AIN ต้องมีประวัติยา/ผื่น/ไข้ และ WBC, WBC cast, eosinophil
- AGN ต้องมี hematuria, dysmorphic RBC, RBC cast, ความดันสูง
- Postrenal ต้องมีประวัติหรือภาพการอุดตัน''',
            pearl="Hypovolemia นาน + BUN/Cr <15 + sp.gr. 1.010 = ischemic ATN", topic="Ischemic ATN",
            ref=[f"{D} หน้า 30–31"], nl=["2.3.14(3)"]),
        mcq("NEPHRO-01-03-2",
            "A 50-year-old woman with diabetes and hypertension for 10 years was treated with intravenous gentamicin 240 mg daily for pyelonephritis. On day 7 her fever has resolved but she has nausea and vomiting. BUN rose from 17 to 45 mg/dL and Cr from 1 to 3 mg/dL. What is the most likely cause?",
            "Gentamicin-induced acute tubular necrosis",
            ["Diabetic nephropathy", "Hypertensive nephrosclerosis", "Ongoing pyelonephritis", "Prerenal azotemia from vomiting"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Cr ขึ้นจาก 1 เป็น 3 ภายในหนึ่งสัปดาห์หลังได้ **aminoglycoside** ซึ่งเป็น nephrotoxic ATN ที่เกิดหลังได้ยาประมาณ 5–10 วัน คลื่นไส้อาเจียนเป็นอาการของ uremia
- Diabetic nephropathy และ hypertensive nephrosclerosis เป็นโรคเรื้อรัง ไม่ทำ Cr เพิ่มสามเท่าในหนึ่งสัปดาห์ และ Cr baseline ปกติ
- การติดเชื้อดีขึ้นแล้ว (ไข้ลง) จึงไม่น่าเป็นสาเหตุ
- อาเจียนเกิดตามหลัง Cr ที่สูงขึ้น เป็นผลมากกว่าเหตุ และ BUN/Cr = 15 ไม่ใช่ภาพ prerenal''',
            pearl="Aminoglycoside → nephrotoxic ATN หลังได้ยาราว 1 สัปดาห์", topic="Nephrotoxic ATN",
            ref=[f"{D} หน้า 36–37"], nl=["2.3.14(3)", "B1.7.1(4)"]),
        mcq("NEPHRO-01-03-3",
            "A 70-year-old man with diabetes and chronic kidney disease (Cr 1.4 mg/dL, eGFR 48) has stable angina and is scheduled for coronary angiography. Vital signs are stable. What should be administered to prevent contrast-induced nephropathy?",
            "Intravenous normal saline before and after the procedure",
            ["Oral enalapril", "Oral N-acetylcysteine", "Intravenous low-dose dopamine", "Intravenous sodium bicarbonate"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''สไลด์: ป้องกัน CIN ด้วย **NSS ก่อนและหลังได้ contrast** เพื่อให้มี volume เพียงพอ เจือจาง contrast และลด vasoconstriction ใน medulla
- Enalapril ลด GFR ชั่วคราว ไม่ป้องกัน และมักแนะนำให้งดช่วงทำหัตถการ
- N-acetylcysteine และ sodium bicarbonate ไม่ได้ดีกว่า NSS ในการศึกษาใหญ่
- Low-dose dopamine ไม่มีประโยชน์ในการป้องกัน AKI''',
            pearl="CIN prevention = NSS", topic="Contrast nephropathy",
            ref=[f"{D} หน้า 20, 38–39"], nl=["2.3.14(3)"]),
        mcq("NEPHRO-01-03-4",
            "A 58-year-old man develops AKI 3 days after emergency surgery complicated by hypotension. BUN 56 mg/dL, Cr 4.0 mg/dL. Which set of urine indices is most consistent with his condition?",
            "Urine Na 55 mEq/L, FENa 3%, urine osmolality 310 mOsm/kg",
            ["Urine Na 10 mEq/L, FENa 0.5%, urine osmolality 650 mOsm/kg",
             "Urine Na 15 mEq/L, FEUrea 25%, urine osmolality 560 mOsm/kg",
             "Urine Na 12 mEq/L, FENa 0.6%, urine osmolality 700 mOsm/kg",
             "Urine Na 18 mEq/L, FENa 0.8%, urine osmolality 520 mOsm/kg"],
            explain='''ความดันต่ำช่วงผ่าตัดแล้ว Cr ขึ้นเป็น 4 และ BUN/Cr = 14 (< 15) = **ischemic ATN** tubule ดูด Na กลับไม่ได้ → **urine Na > 40, FENa > 2%** และเข้มข้นปัสสาวะไม่ได้ → **Uosm < 350**
- ชุดที่ urine Na 10–18, FENa < 1%, Uosm 520–700 ล้วนเป็นภาพ prerenal ที่ tubule ยังทำงานดี
- FEUrea 25% (< 35%) ก็บอก prerenal เช่นกัน''',
            pearl="ATN: UNa >40, FENa >2%, Uosm <350", topic="Urine indices",
            ref=[f"{D} หน้า 16, 19"], nl=["B9.3(4)"]),
    ])

# ---------------------------------------------------------------- 01-04 Rhabdo / TLS
F_TLS = fig("nephro-01-04-f1", "กลไก Tumor lysis syndrome → AKI", '''<svg viewBox="0 0 740 300">
 <defs><marker id="nephro-01-04-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="20" y="110" width="170" height="70" rx="10" class="acsoft"/>
 <text x="105" y="138" text-anchor="middle" class="tb">Chemotherapy</text>
 <text x="105" y="158" text-anchor="middle" class="t3">เซลล์มะเร็งแตกจำนวนมาก</text>
 <path d="M190 128L262 52" class="ln" marker-end="url(#nephro-01-04-a)"/>
 <path d="M190 145H262" class="ln" marker-end="url(#nephro-01-04-a)"/>
 <path d="M190 162L262 238" class="ln" marker-end="url(#nephro-01-04-a)"/>
 <rect x="266" y="24" width="190" height="56" rx="10" class="badsoft"/>
 <text x="361" y="48" text-anchor="middle" class="tb">↑K ≥ 6</text>
 <text x="361" y="66" text-anchor="middle" class="t3">arrhythmia</text>
 <rect x="266" y="118" width="190" height="56" rx="10" class="misssoft"/>
 <text x="361" y="142" text-anchor="middle" class="tb">↑PO4 ≥ 4.5</text>
 <text x="361" y="160" text-anchor="middle" class="t3">จับ Ca → ↓Ca ≤ 7</text>
 <rect x="266" y="212" width="190" height="56" rx="10" class="misssoft"/>
 <text x="361" y="236" text-anchor="middle" class="tb">↑Uric acid ≥ 8</text>
 <text x="361" y="254" text-anchor="middle" class="t3">จาก nucleic acid</text>
 <path d="M456 146H520" class="ln" marker-end="url(#nephro-01-04-a)"/>
 <path d="M456 240L520 168" class="ln" marker-end="url(#nephro-01-04-a)"/>
 <rect x="524" y="110" width="200" height="74" rx="10" class="bad"/>
 <text x="624" y="136" text-anchor="middle" class="tw">ผลึกอุด tubule</text>
 <text x="624" y="156" text-anchor="middle" class="tw">Ca-PO4, uric acid</text>
 <text x="624" y="176" text-anchor="middle" class="tw">→ AKI</text>
 <text x="624" y="214" text-anchor="middle" class="t3">Tx: IV fluid ให้ UO &gt; 2 ml/kg/hr</text>
 <text x="624" y="232" text-anchor="middle" class="t3">allopurinol / rasburicase</text>
 <text x="624" y="250" text-anchor="middle" class="t3">แก้ electrolyte, RRT ถ้าจำเป็น</text>
</svg>''', "เซลล์มะเร็งแตก ปล่อย K, PO4 และ nucleic acid (→ uric acid) ออกมา PO4 จับ Ca ทำให้ Ca ต่ำ ผลึกตกตะกอนใน tubule ทำให้เกิด AKI")

S4 = sec("nephro-01-04", "Rhabdomyolysis & Tumor lysis syndrome",
    "Pigment/crystal ATN · dipstick blood + แต่ไม่มี RBC = myoglobin · TLS: K ≥6, PO4 ≥4.5, Ca ≤7, uric ≥8", minutes=7,
    source=f"{D} หน้า 21–22, 32–35", nl=["2.3.14(3)", "B9.2.7(1)"],
    md='''
ทั้งสองภาวะเป็น **endogenous nephrotoxic ATN** และทำให้ **K สูงอันตราย** — ข้อสอบชอบให้ lab มาแล้วถามวินิจฉัยหรือการรักษาเริ่มแรก

### Rhabdomyolysis

กล้ามเนื้อลายสลาย → ปล่อย **myoglobin, K, PO4, CPK** ออกสู่เลือด myoglobin กรองผ่านไต ทำลาย tubule (heme toxicity + อุดท่อ + หดหลอดเลือด)

- สาเหตุ (เสริม): ออกกำลังหนัก ภาวะ crush injury ชัก heat stroke ยา (statin) แอลกอฮอล์ นอนนิ่งนาน
- อาการ: **myalgia, generalized weakness, dark (cola-colored) urine**
- LAB: **↑CPK** (มักเกิน 5 เท่าของค่าปกติ (เสริม)), ↑BUN, Cr, **↑K**, ↑PO4, ↓Ca ช่วงแรก (เสริม)
- UA: **dipstick blood +** แต่กล้องจุลทรรศน์พบ RBC น้อย/ไม่พบ → แปลว่าเป็น **myoglobinuria** (dipstick อ่าน heme ไม่ใช่เม็ดเลือด)
- Tx: **supportive, IV fluid** (isotonic saline ปริมาณมาก ให้ปัสสาวะออกดี), แก้ electrolyte

> Dipstick blood 3+ แต่ RBC 0–2/HPF = myoglobin (rhabdo) หรือ hemoglobin (intravascular hemolysis)

### Tumor lysis syndrome (TLS)

[[fig:nephro-01-04-f1]]

การทำลายเซลล์มะเร็งจำนวนมากอย่างรวดเร็ว (ส่วนใหญ่ **ตามหลัง chemotherapy** ในมะเร็งที่โตเร็ว/ก้อนใหญ่ เช่น ALL, Burkitt lymphoma, AML ที่ WBC สูง) → ปล่อยสารในเซลล์ออกมา

| Lab ของ TLS (ตามสไลด์) | เกณฑ์ |
|---|---|
| ↑Phosphate | **≥ 4.5 mg/dL** |
| ↑Potassium | **≥ 6 mEq/L** |
| ↓Calcium | **≤ 7 mg/dL** |
| ↑Uric acid | **≥ 8 mg/dL** |
| ผลทางคลินิก | AKI, arrhythmia, ชัก (เสริม) |

การรักษา
- **IV fluid ให้ urine output > 2 ml/kg/hr**
- Hyperuricemia → **allopurinol** (ลดการสร้าง ใช้ป้องกัน) หรือ **rasburicase** (ย่อย uric acid ที่มีอยู่แล้ว ใช้เมื่อเสี่ยงสูง/uric สูงแล้ว; ห้ามในผู้ป่วย G6PD deficiency (เสริม))
- แก้ electrolyte (hyperK ตามขั้นตอน) · RRT ถ้า refractory
''',
    figs=[F_TLS],
    pearls=[
        "Dark urine + myalgia + CPK สูง + dipstick blood + แต่ไม่มี RBC = rhabdomyolysis → IV fluid",
        "TLS: K ≥6, PO4 ≥4.5, Ca ≤7, uric ≥8 หลัง chemo วันแรก ๆ",
        "TLS: IV fluid ให้ UO >2 ml/kg/hr + allopurinol/rasburicase",
        "Rasburicase ห้ามใน G6PD deficiency (เสริม)",
    ],
    items=[
        mcq("NEPHRO-01-04-1",
            "A 30-year-old woman with acute lymphoblastic leukemia (WBC 198,000/mm3, blasts 98%, Cr 1.0 mg/dL) starts induction chemotherapy. One day later, her urine output decreases to 50 mL/day. Labs: Na 132, K 6.0, Cl 99, HCO3 19 mEq/L, Cr 2.5 mg/dL, Ca 7.5 mg/dL, PO4 7 mg/dL. What is the most likely diagnosis?",
            "Tumor lysis syndrome",
            ["Rhabdomyolysis", "Obstructive nephropathy", "Contrast-induced nephropathy", "Drug-induced interstitial nephritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''มะเร็งเม็ดเลือดที่ WBC สูงมาก + เริ่มเคมีบำบัด 1 วัน แล้วมี **↑K (6), ↑PO4 (7), ↓Ca (7.5)** และ AKI = **tumor lysis syndrome** (PO4 จับ Ca จึงทำให้ Ca ต่ำ)
- Rhabdomyolysis ไม่มีประวัติกล้ามเนื้อบาดเจ็บหรือปวดเมื่อย และจะเด่นที่ CPK สูง
- Obstructive nephropathy ต้องมีหลักฐานการอุดตัน
- Contrast nephropathy ไม่มีประวัติได้ contrast
- Drug-induced interstitial nephritis มักเกิดหลังได้ยาเป็นสัปดาห์ และไม่ทำให้ PO4 สูงคู่กับ Ca ต่ำแบบนี้''',
            pearl="หลัง chemo + ↑K ↑PO4 ↓Ca + AKI = TLS", topic="Tumor lysis syndrome",
            ref=[f"{D} หน้า 22, 34–35"], nl=["2.3.14(3)"]),
        mcq("NEPHRO-01-04-2",
            "A 24-year-old military recruit completes an intensive 20-km march in hot weather. He complains of diffuse muscle soreness and dark urine and is unable to void much. CPK 48,000 U/L, K 5.8 mEq/L, Cr 2.2 mg/dL. Urine dipstick: blood 3+; microscopy shows RBC 0–2/HPF. What is the most appropriate initial treatment?",
            "Aggressive intravenous isotonic saline",
            ["Oral sodium bicarbonate only", "Intravenous furosemide", "Immediate hemodialysis", "Oral prednisolone"],
            explain='''ออกกำลังหนัก + ปวดกล้ามเนื้อ + ปัสสาวะสีเข้ม + **CPK สูงมาก** + dipstick blood 3+ แต่ RBC แทบไม่มี (= myoglobinuria) = **rhabdomyolysis** ซึ่งรักษาแบบ supportive ด้วย **IV fluid ปริมาณมาก** เพื่อเจือจางและขับ myoglobin ป้องกัน ATN
- Sodium bicarbonate เป็นทางเลือกเสริมที่หลักฐานไม่ชัด และให้กินอย่างเดียวไม่พอ
- Furosemide ทำให้ปริมาตรลดลง ไม่ใช่การรักษาหลัก
- Hemodialysis ยังไม่มีข้อบ่งชี้ (K 5.8 ไม่ refractory ยังไม่มี overload หรือ acidosis รุนแรง)
- Steroid ไม่มีบทบาทใน rhabdomyolysis''',
            pearl="Rhabdomyolysis → IV fluid ปริมาณมาก", topic="Rhabdomyolysis",
            ref=[f"{D} หน้า 21, 32–33"], nl=["2.3.14(3)", "B9.4(2)"]),
        mcq("NEPHRO-01-04-3",
            "A 45-year-old man with bulky Burkitt lymphoma is about to begin chemotherapy. Uric acid is 11 mg/dL and Cr is 1.6 mg/dL. He has known G6PD deficiency. In addition to aggressive IV hydration, which agent is most appropriate to control the hyperuricemia?",
            "Allopurinol",
            ["Rasburicase", "Probenecid", "Colchicine", "Hydrochlorothiazide"],
            explain='''ผู้ป่วยเสี่ยง TLS สูงและ uric acid สูงอยู่แล้ว ปกติ rasburicase เป็นตัวเลือกที่ลด uric acid ได้เร็ว แต่ **G6PD deficiency เป็นข้อห้ามของ rasburicase** (H2O2 ที่เกิดขึ้นทำให้ hemolysis และ methemoglobinemia) จึงใช้ **allopurinol** ร่วมกับ IV fluid ให้ UO > 2 ml/kg/hr (เสริม)
- Rasburicase ห้ามใช้ใน G6PD deficiency
- Probenecid เพิ่มการขับ uric acid ทางปัสสาวะ ทำให้ผลึกตกในท่อไตมากขึ้น
- Colchicine ใช้ลดการอักเสบของ gout ไม่ลด uric acid
- Thiazide ลดการขับ uric acid และทำให้ขาดน้ำ''',
            pearl="TLS + G6PD deficiency → allopurinol (ห้าม rasburicase)", topic="TLS treatment",
            ref=[f"{D} หน้า 22"], nl=["2.3.14(3)"]),
    ])

# ---------------------------------------------------------------- 01-05 AIN
S5 = sec("nephro-01-05", "Acute interstitial nephritis (AIN)",
    "ยา (penicillin, NSAID, PPI) + ไข้ ผื่น eosinophilia + WBC cast → หยุดยา ± steroid", minutes=6,
    source=f"{D} หน้า 23–24, 40–43", nl=["2.3.14-3(8)", "2.3.14(3)"],
    md='''
AIN = การอักเสบของ interstitium ของไต ส่วนใหญ่เป็น **hypersensitivity reaction ต่อยา** (type IV) — เกิดได้ทุกขนาดยา ไม่ขึ้นกับ dose (เสริม)

### สาเหตุ (ตามสไลด์)

- **Drugs** (พบบ่อยสุด): antibiotic (**penicillins, cephalosporins**), **NSAID**, **PPI**, diuretics, rifampin
- Infection
- Autoimmune

### อาการ

- **Fever, rash (maculopapular), arthralgias** — triad ไข้ ผื่น eosinophilia พบครบไม่บ่อย (เสริม)
- Flank pain, oliguria
- มักเกิดหลังเริ่มยาประมาณ 1–3 สัปดาห์ (เสริม)

### การวินิจฉัย

- ↑BUN, Cr, **BUN/Cr ratio < 15**, **FENa > 2%**
- CBC: **↑Eosinophil**
- UA: **WBC, WBC cast, eosinophiluria**, RBC และ proteinuria เล็กน้อย (มักไม่ถึง nephrotic range)

> NSAID ทำให้เกิดได้ทั้ง prerenal AKI, AIN และ nephrotic syndrome (MCD/MN) — ดูผล UA ช่วยแยก: มี WBC/eosinophil = AIN

### การรักษา

- **Supportive**: **หยุดยาที่เป็นสาเหตุ** หรือรักษาโรคต้นเหตุ
- IV fluid และแก้ electrolyte
- **± Steroid** กรณี supportive แล้วไม่ดีขึ้น

| AIN | ATN | AGN |
|---|---|---|
| ประวัติยา ไข้ ผื่น | ช็อก/nephrotoxin | หลังติดเชื้อ/autoimmune |
| WBC cast, eosinophil | Muddy brown cast | RBC cast, dysmorphic RBC |
| Eosinophilia ในเลือด | — | Complement อาจต่ำ |
| หยุดยา ± steroid | Supportive | รักษาตามสาเหตุ |
''',
    pearls=[
        "AIN = ยา (penicillin, cephalosporin, NSAID, PPI, rifampin) + ไข้ ผื่น + eosinophilia + WBC cast",
        "AIN: หยุดยาก่อน ให้ steroid เมื่อหยุดยาแล้วไม่ดีขึ้น",
        "WBC cast พบได้ทั้ง AIN และ pyelonephritis — แยกด้วยไข้สูง CVA tenderness และแบคทีเรีย",
    ],
    items=[
        mcq("NEPHRO-01-05-1",
            "A 50-year-old man presents with swelling of both legs for 2 weeks. He has been taking over-the-counter medication for knee pain. BP 130/80 mmHg, mild leg edema. Cr 3.0 mg/dL. Urinalysis: sp.gr. 1.010, protein 1+, WBC 10–20/HPF with eosinophils, RBC 2–3/HPF. What is the most likely diagnosis?",
            "Acute interstitial nephritis",
            ["Nephrotic syndrome", "Acute papillary necrosis", "Acute tubular necrosis", "Acute glomerulonephritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ยาแก้ปวดเข่าซื้อเอง (NSAID) + Cr สูง + **WBC ในปัสสาวะที่เป็น eosinophil** + proteinuria เล็กน้อย = **AIN จากยา**
- Nephrotic syndrome ต้องมี proteinuria 3–4+ (> 3.5 g/day), albumin ต่ำ, fatty cast
- Papillary necrosis จาก analgesic มักมาด้วยปวดเอว hematuria และมีเนื้อเยื่อหลุดออกมาในปัสสาวะ
- ATN ต้องมีประวัติช็อก/nephrotoxin และ muddy brown cast ไม่ใช่ eosinophiluria
- AGN ต้องมี RBC มาก dysmorphic RBC RBC cast และความดันสูง''',
            pearl="NSAID + eosinophiluria + WBC = AIN", topic="Drug-induced AIN",
            ref=[f"{D} หน้า 40–41"], nl=["2.3.14-3(8)"]),
        mcq("NEPHRO-01-05-2",
            "A 40-year-old man had fever and sore throat 3 weeks ago and bought antibiotics from a pharmacy. One week ago he developed low-grade fever and an itchy rash. For 3 days he has had fatigue, decreased urine output, and edema. BUN 88 mg/dL, Cr 6.4 mg/dL. Urinalysis: sp.gr. 1.010, albumin 2+, RBC 5–10/HPF, WBC 5–10/HPF. Blood eosinophils 6%. What is the most likely cause of the acute kidney injury?",
            "Acute interstitial nephritis",
            ["Acute tubular necrosis", "Acute poststreptococcal glomerulonephritis", "Rapidly progressive glomerulonephritis", "IgA nephropathy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ประเด็นสำคัญคือ **ได้ยาปฏิชีวนะ (มักเป็น penicillin) แล้วตามด้วยไข้ ผื่นคัน และ eosinophilia** ก่อนเกิด AKI = **AIN จาก hypersensitivity ต่อยา** ส่วน UA มี WBC และ RBC ปน
- ATN ไม่มีไข้ ผื่น eosinophilia
- APSGN ก็มีประวัติเจ็บคอก่อน 1–3 สัปดาห์ (ตัวลวงหลัก) แต่จะมาด้วย hematuria เด่น ความดันสูง RBC cast ไม่ใช่ผื่นคันกับ eosinophilia
- RPGN ต้องมี RBC cast และ nephritic sediment ชัด
- IgA nephropathy มี gross hematuria ภายใน 1–5 วันหลังติดเชื้อ ไม่มีผื่นและ eosinophilia''',
            pearl="ซื้อยาปฏิชีวนะกิน → ผื่น + ไข้ + eosinophilia + AKI = AIN", topic="AIN vs APSGN",
            ref=[f"{D} หน้า 42–43"], nl=["2.3.14-3(8)"]),
        mcq("NEPHRO-01-05-3",
            "A 66-year-old woman on omeprazole for 6 weeks develops AKI with Cr rising from 0.9 to 2.8 mg/dL. Urinalysis shows WBC 10–20/HPF, WBC casts, and no bacteria. Urine culture is negative. What is the most appropriate first step in management?",
            "Discontinue omeprazole",
            ["Start oral ciprofloxacin", "Start high-dose prednisolone and continue omeprazole", "Arrange urgent hemodialysis", "Start intravenous cyclophosphamide"],
            explain='''PPI เป็นสาเหตุ AIN ที่พบบ่อยในผู้สูงอายุ WBC cast + เพาะเชื้อไม่ขึ้น = **AIN** ขั้นแรกคือ **หยุดยาที่เป็นสาเหตุ** แล้วให้ supportive ส่วน steroid ให้เมื่อหยุดยาแล้วไม่ดีขึ้น
- Ciprofloxacin ใช้รักษา pyelonephritis แต่รายนี้ไม่มีไข้ เพาะเชื้อไม่ขึ้น
- ให้ steroid ทั้งที่ยังใช้ยาต้นเหตุอยู่ผิดหลัก ต้องหยุดยาก่อนเสมอ
- Hemodialysis ไม่มีข้อบ่งชี้เร่งด่วน
- Cyclophosphamide ใช้ใน GN รุนแรง/vasculitis ไม่ใช่ AIN''',
            pearl="AIN: หยุดยาก่อน ± steroid", topic="AIN management",
            ref=[f"{D} หน้า 24"], nl=["2.3.14-3(8)"]),
    ])

# ---------------------------------------------------------------- 01-06 AKI management
F_RRT = fig("nephro-01-06-f1", "ข้อบ่งชี้ RRT ใน AKI (AEIOU)", '''<svg viewBox="0 0 740 250">
 <rect x="10" y="10" width="136" height="196" rx="12" class="badsoft"/>
 <rect x="156" y="10" width="136" height="196" rx="12" class="misssoft"/>
 <rect x="302" y="10" width="136" height="196" rx="12" class="c2soft"/>
 <rect x="448" y="10" width="136" height="196" rx="12" class="c1soft"/>
 <rect x="594" y="10" width="136" height="196" rx="12" class="acsoft"/>
 <circle cx="78" cy="52" r="24" class="bad"/><text x="78" y="58" text-anchor="middle" class="tw">A</text>
 <circle cx="224" cy="52" r="24" class="miss"/><text x="224" y="58" text-anchor="middle" class="tw">E</text>
 <circle cx="370" cy="52" r="24" class="c2"/><text x="370" y="58" text-anchor="middle" class="tw">I</text>
 <circle cx="516" cy="52" r="24" class="c1"/><text x="516" y="58" text-anchor="middle" class="tw">O</text>
 <circle cx="662" cy="52" r="24" class="ac"/><text x="662" y="58" text-anchor="middle" class="tw">U</text>
 <text x="78" y="100" text-anchor="middle" class="tb">Acidemia</text>
 <text x="78" y="124" text-anchor="middle" class="t2">refractory</text>
 <text x="78" y="142" text-anchor="middle" class="t2">pH &lt; 7.1</text>
 <text x="224" y="100" text-anchor="middle" class="tb">Electrolyte</text>
 <text x="224" y="124" text-anchor="middle" class="t2">refractory</text>
 <text x="224" y="142" text-anchor="middle" class="t2">K &gt; 6.5</text>
 <text x="370" y="100" text-anchor="middle" class="tb">Intoxication</text>
 <text x="370" y="124" text-anchor="middle" class="t2">methanol</text>
 <text x="370" y="142" text-anchor="middle" class="t2">ethylene glycol</text>
 <text x="370" y="160" text-anchor="middle" class="t2">lithium, salicylate</text>
 <text x="370" y="178" text-anchor="middle" class="t2">metformin</text>
 <text x="516" y="100" text-anchor="middle" class="tb">Overload</text>
 <text x="516" y="124" text-anchor="middle" class="t2">refractory</text>
 <text x="516" y="142" text-anchor="middle" class="t2">pulmonary edema</text>
 <text x="662" y="100" text-anchor="middle" class="tb">Uremia</text>
 <text x="662" y="124" text-anchor="middle" class="t2">encephalopathy</text>
 <text x="662" y="142" text-anchor="middle" class="t2">pericarditis</text>
 <text x="662" y="160" text-anchor="middle" class="t2">pleuritis</text>
 <text x="370" y="234" text-anchor="middle" class="t3">"refractory" = แก้ด้วยยาแล้วไม่ดีขึ้น</text>
</svg>''', "ห้าช่อง A-E-I-O-U คือข้อบ่งชี้ทำ dialysis ใน AKI ตามสไลด์ ส่วนใหญ่ต้องเป็นภาวะที่ดื้อต่อการรักษาด้วยยา")

S6 = sec("nephro-01-06", "AKI management & renal replacement therapy",
    "แก้ตามกลุ่ม: prerenal = hemodynamics · renal = รักษาสาเหตุ · postrenal = เอาสิ่งอุดตันออก · RRT เมื่อ AEIOU", minutes=6,
    source=f"{D} หน้า 25–27, 44–47", nl=["2.3.14(3)", "B9.2.7(1)", "2.3.14-3(9)"],
    md='''
### รักษาตามกลุ่มสาเหตุ

| กลุ่ม | การรักษา |
|---|---|
| **Prerenal** | Correct hemodynamics — hypovolemic → **IV fluid, vasopressors** · hypervolemic (HF) → **diuretics** |
| **Renal** | รักษาสาเหตุ — ATN: หยุดยาที่เป็นพิษ · AIN: หยุดยา ± steroid · GN: รักษาตามโรค |
| **Postrenal** | **Relieve obstruction** — Foley catheter, PCN, ureteric stent (เสริม) |

### ป้องกันไม่ให้ไตเสียเพิ่ม (ทุกราย)

- หยุดยาที่เป็นพิษต่อไต (NSAID, aminoglycoside, contrast) และ **ปรับขนาดยาตาม GFR**
- Volume management: hypovolemic → IV fluid · hypervolemic → diuretics
- แก้ acidosis และ electrolyte disturbance (โดยเฉพาะ hyperK)
- Nutrition

### ข้อบ่งชี้ Renal replacement therapy (RRT)

[[fig:nephro-01-06-f1]]

- **A**cidemia: refractory acidosis **pH < 7.1**
- **E**lectrolyte: refractory hyperK **> 6.5**
- **I**ntoxication: methanol, ethylene glycol, lithium, salicylate, metformin (MFM)
- **O**verload: refractory pulmonary edema
- **U**remia complication: encephalopathy, **pericarditis**, pleuritis

> Cr หรือ BUN สูงอย่างเดียว ไม่ใช่ข้อบ่งชี้ทำ dialysis ฉุกเฉิน ต้องมีภาวะแทรกซ้อนข้างบน

### Postrenal ในข้อสอบ

- ผู้ป่วยไตข้างเดียว (เคยตัดไตออก) แล้วมีนิ่วอุดท่อไตข้างที่เหลือ → anuria + hydronephrosis = postrenal แม้อุดข้างเดียว
- ผู้ป่วยไม่มีปัสสาวะ สวนแล้วได้ปัสสาวะน้อยมาก (ไม่ใช่ bladder outlet obstruction) → ต้องดูว่าอุดที่ ureter หรือไม่ ด้วย **ultrasound** (ไม่ใช้ contrast) เช่น ผู้ป่วย HIV ที่ได้ ARV บางตัว (indinavir, atazanavir) เกิดนิ่วจากผลึกยา (เสริม)
''',
    figs=[F_RRT],
    pearls=[
        "RRT ใน AKI = AEIOU: pH <7.1, K >6.5 refractory, toxin, pulmonary edema refractory, uremic pericarditis/encephalopathy",
        "Postrenal → relieve obstruction; ไตข้างเดียวอุดข้างเดียวก็ anuria ได้",
        "Imaging แรกของ AKI = ultrasound KUB (ไม่ใช้ contrast)",
        "AKI ทุกราย: หยุด nephrotoxin + ปรับขนาดยาตาม GFR",
    ],
    items=[
        mcq("NEPHRO-01-06-1",
            "A 50-year-old patient who had a left nephrectomy years ago presents with right flank pain radiating to the groin for 3 days, urine output 50 mL/day, and dyspnea. BP 150/100 mmHg, RR 24/min, engorged neck veins, basal crepitations, pitting edema 2+. BUN 65 mg/dL, Cr 5 mg/dL. UA: sp.gr. 1.010, albumin trace, RBC 10–20, WBC 3–5. Ultrasound: right hydronephrosis. What is the diagnosis?",
            "Postrenal azotemia",
            ["Prerenal azotemia", "Acute tubular necrosis", "Acute interstitial nephritis", "Acute glomerulonephritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ผู้ป่วยมี **ไตข้างเดียว** ปวดเอวร้าวลงขาหนีบ (renal colic จากนิ่ว) + anuria + **hydronephrosis ข้างขวา** = **postrenal AKI** มี volume overload ตามมาเพราะไม่มีปัสสาวะ ต้อง relieve obstruction (PCN/stent)
- Prerenal ต้องมี hypovolemia/↓perfusion แต่รายนี้ overload
- ATN ไม่มี hydronephrosis และไม่มีปวดแบบ colic
- AIN ไม่มีประวัติยา/ผื่น และ WBC ไม่มาก
- AGN ต้องมี RBC cast, dysmorphic RBC, proteinuria มากกว่านี้ ส่วน RBC ในรายนี้มาจากนิ่ว''',
            pearl="ไตข้างเดียว + colic + hydronephrosis = postrenal", topic="Postrenal AKI",
            ref=[f"{D} หน้า 44–45"], nl=["2.3.14-3(9)", "2.3.14-3(15)"]),
        mcq("NEPHRO-01-06-2",
            "A patient with HIV who started antiretroviral therapy 2 years ago presents with nausea, vomiting, and no urine for 1 day. The abdomen is soft and non-tender; bladder catheterization yields only 20 mL of urine. Serum creatinine is 4.5 mg/dL. What is the most appropriate investigation?",
            "Ultrasound of the kidneys and urinary tract",
            ["CT abdomen with intravenous contrast", "Cystography", "Intravenous pyelography", "Renal biopsy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Anuria ทันทีต้องคิดถึงการอุดตันเสมอ สวนแล้วไม่มีปัสสาวะค้าง แปลว่าไม่ได้อุดที่ bladder outlet จึงต้องดูว่ามี **hydronephrosis** จากการอุดที่ ureter ทั้งสองข้างหรือไม่ (เช่น นิ่วจากผลึกยา ARV) ด้วย **ultrasound** ซึ่งปลอดภัยและไม่ต้องใช้ contrast
- CT with contrast และ IVP ใช้ contrast ซึ่งไม่ควรให้ในขณะ Cr 4.5
- Cystography ดูกระเพาะปัสสาวะและ reflux ซึ่งไม่ตอบคำถามเรื่องการอุดที่ ureter
- Renal biopsy ทำหลังตัด postrenal แล้วเท่านั้น''',
            pearl="AKI/anuria → U/S KUB เป็น imaging แรก", topic="AKI investigation",
            ref=[f"{D} หน้า 46–47"], nl=["2.3.14(3)", "2.1.44"]),
        mcq("NEPHRO-01-06-3",
            "A 64-year-old man with AKI from septic ATN is being managed in the ward. Which finding is an indication for urgent renal replacement therapy?",
            "Pericardial friction rub with BUN 140 mg/dL",
            ["Potassium 5.8 mEq/L with a normal ECG", "Creatinine 6.5 mg/dL without symptoms", "Arterial pH 7.28 with HCO3 15 mEq/L", "Urine output 300 mL/day without pulmonary edema"],
            explain='''**Uremic pericarditis** (friction rub ร่วมกับ BUN สูง) เป็นภาวะแทรกซ้อนของ uremia ที่เป็นข้อบ่งชี้ RRT (U ใน AEIOU)
- K 5.8 โดย ECG ปกติ รักษาด้วยยาได้ ข้อบ่งชี้คือ K > 6.5 ที่ดื้อต่อยา
- Cr สูงโดยไม่มีอาการไม่ใช่ข้อบ่งชี้เร่งด่วน
- pH 7.28 ยังไม่ถึงเกณฑ์ pH < 7.1 ที่ดื้อต่อการรักษา
- Oliguria โดยไม่มี overload ยังจัดการ volume ได้''',
            pearl="Uremic pericarditis = ข้อบ่งชี้ dialysis", topic="RRT indications",
            ref=[f"{D} หน้า 26"], nl=["2.3.14(3)"]),
        mcq("NEPHRO-01-06-4",
            "A 72-year-old man with heart failure (EF 25%) is admitted with dyspnea, bilateral crackles, raised JVP, and leg edema. Cr has risen from 1.4 to 2.3 mg/dL. BP 128/76 mmHg. What is the most appropriate management of his kidney injury?",
            "Intravenous loop diuretic",
            ["Intravenous normal saline 1 L bolus", "Start ibuprofen for edema-related pain", "Urgent renal biopsy", "Add oral gentamicin"],
            explain='''Cardiorenal syndrome = **prerenal จาก ↓effective circulating volume** ผู้ป่วยเป็น **hypervolemic** ตามสไลด์ให้ **diuretics** เพื่อลด congestion (venous congestion ของไตดีขึ้น → GFR ดีขึ้น)
- IV fluid bolus ใช้กับ hypovolemic จะทำให้น้ำท่วมปอดแย่ลง
- NSAID ทำ prerenal AKI แย่ลงและทำให้คั่งน้ำ
- Renal biopsy ไม่จำเป็นในสาเหตุที่ชัดเจน
- Aminoglycoside เป็น nephrotoxin ต้องหลีกเลี่ยง''',
            pearl="Prerenal แบบ hypervolemic (HF) → diuretics", topic="Cardiorenal AKI",
            ref=[f"{D} หน้า 25, 27"], nl=["2.3.14(3)", "B9.4(2)"]),
    ])

LECTURE = lecture("01", "Acute kidney injury", "UA · AKI approach · ATN · rhabdo/TLS · AIN · RRT",
    objectives=[
        "อ่าน UA และ urinary cast แล้วบอกตำแหน่งโรคในไตได้",
        "วินิจฉัย AKI ตาม KDIGO และแยก prerenal–renal–postrenal ด้วย BUN/Cr, FENa, FEUrea, Uosm",
        "จำสาเหตุ ATN, AIN, rhabdomyolysis, TLS และการรักษา/ป้องกันได้",
        "บอกข้อบ่งชี้ renal replacement therapy (AEIOU) ได้",
    ],
    sections=[S1, S2, S3, S4, S5, S6])
