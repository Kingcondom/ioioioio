from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Nephro"

# ---------------------------------------------------------------- 02-01 overview
F_MAP = fig("nephro-02-01-f1", "แผนที่ glomerular disease: nephritic ↔ nephrotic", '''<svg viewBox="0 0 740 360">
 <rect x="10" y="10" width="350" height="44" rx="10" class="bad"/>
 <text x="185" y="38" text-anchor="middle" class="tw">Nephritic (อักเสบ → เลือดออก)</text>
 <rect x="380" y="10" width="350" height="44" rx="10" class="c1"/>
 <text x="555" y="38" text-anchor="middle" class="tw">Nephrotic (รั่วโปรตีน)</text>
 <rect x="10" y="62" width="350" height="96" rx="10" class="badsoft"/>
 <text x="24" y="84" class="t2">↑BP, edema, hematuria, oliguria</text>
 <text x="24" y="104" class="t2">UA: dysmorphic RBC, RBC cast</text>
 <text x="24" y="124" class="t2">Proteinuria &lt; 3–3.5 g/day</text>
 <text x="24" y="144" class="t2">↑BUN, Cr</text>
 <rect x="380" y="62" width="350" height="96" rx="10" class="c1soft"/>
 <text x="394" y="84" class="t2">Edema, frothy urine, BP ปกติ/สูง</text>
 <text x="394" y="104" class="t2">Proteinuria &gt; 3–3.5 g/day, fatty cast</text>
 <text x="394" y="124" class="t2">Albumin ต่ำ, cholesterol สูง</text>
 <text x="394" y="144" class="t2">เสี่ยง thrombosis และติดเชื้อ</text>
 <rect x="10" y="172" width="720" height="34" rx="8" class="sunk"/>
 <text x="370" y="194" text-anchor="middle" class="t3">สเปกตรัม: ซ้าย = nephritic ล้วน · กลาง = mixed (nephritic + nephrotic-range proteinuria) · ขวา = nephrotic ล้วน</text>
 <rect x="10" y="216" width="160" height="62" rx="10" class="badsoft"/>
 <text x="90" y="240" text-anchor="middle" class="tb">APSGN</text>
 <text x="90" y="260" text-anchor="middle" class="t3">Anti-GBM · GPA</text>
 <rect x="180" y="216" width="160" height="62" rx="10" class="badsoft"/>
 <text x="260" y="240" text-anchor="middle" class="tb">IgA nephropathy</text>
 <text x="260" y="260" text-anchor="middle" class="t3">IgA vasculitis</text>
 <rect x="350" y="216" width="200" height="62" rx="10" class="c2soft"/>
 <text x="450" y="240" text-anchor="middle" class="tb">Lupus nephritis · MPGN</text>
 <text x="450" y="260" text-anchor="middle" class="t3">เป็นได้ทั้งสองแบบ/mixed</text>
 <rect x="560" y="216" width="170" height="62" rx="10" class="c1soft"/>
 <text x="645" y="240" text-anchor="middle" class="tb">MCD · FSGS · MN</text>
 <text x="645" y="260" text-anchor="middle" class="t3">Diabetic nephropathy</text>
 <text x="90" y="300" text-anchor="middle" class="t3">RBC cast เด่น</text>
 <text x="645" y="300" text-anchor="middle" class="t3">Fatty cast เด่น</text>
 <rect x="10" y="314" width="720" height="38" rx="8" class="box"/>
 <text x="370" y="338" text-anchor="middle" class="t2">Course: Acute GN (วัน–สัปดาห์) → RPGN (สัปดาห์–เดือน) → Chronic GN (&gt; 3 เดือน, broad waxy cast)</text>
</svg>''', "ซ้ายคือกลุ่มที่อักเสบเด่น (hematuria, RBC cast) ขวาคือกลุ่มที่รั่วโปรตีนเด่น ตรงกลางเป็นโรคที่มาได้ทั้งสองแบบ")

S1 = sec("nephro-02-01", "Glomerular syndromes: nephritic vs nephrotic",
    "5 กลุ่มอาการของ glomerulus · AGN / RPGN / chronic GN · mixed nephritic–nephrotic", minutes=7,
    source=f"{D} หน้า 48–54, 75–82", nl=["2.3.14(2)", "2.3.14-3(1)", "2.1.43"],
    md='''
โรค glomerulus มาได้ 5 แบบ (glomerular syndrome) — ขั้นแรกในข้อสอบคือจัดเข้ากลุ่มให้ได้จาก **อาการ + UA + ระยะเวลา**

| Syndrome | Clinical | LAB |
|---|---|---|
| Asymptomatic hematuria/proteinuria | ไม่มีอาการ | UA: RBC, protein |
| **Nephrotic syndrome** | Edema, BP ปกติ (สูงบางกรณี), ascites, pleural effusion | Protein **> 3–3.5 g/d**, oval fat body, fatty cast, albumin ต่ำ, cholesterol สูง |
| **Acute GN** | Edema, ↑BP, pulmonary edema | UA: RBC, dysmorphic RBC, **RBC cast**, protein · ไตวายใน **วัน–สัปดาห์** |
| **RPGN** | Edema, ↑BP | UA เหมือน AGN · ไตวายใน **สัปดาห์–เดือน** |
| **Chronic GN** | ความดันสูงเรื้อรัง | UA เหมือน AGN · ไตวาย **> 3 เดือน** |

[[fig:nephro-02-01-f1]]

### Nephritic vs Nephrotic

| Nephritic | Nephrotic |
|---|---|
| ↑BP, edema | ↔/↑BP, edema |
| Hematuria, oliguria | Frothy urine |
| ↑BUN, Cr | ↑Thromboembolism risk, ↑infection risk |
| UA: RBC cast, dysmorphic RBC, proteinuria | Hypoalbuminemia, hyperlipidemia |
| Proteinuria **< 3–3.5 g/day** | Heavy proteinuria **> 3–3.5 g/day**, fatty cast |

**Mixed nephritic–nephrotic syndrome** = nephritic syndrome + proteinuria ระดับ nephrotic (> 3–3.5 g/day) → คิดถึง lupus nephritis, MPGN (และ IgAN/APSGN บางราย)

### สาเหตุของ nephritic syndrome แบ่งตามกลไก (immunofluorescence)

| กลุ่ม | โรค | IF pattern (เสริม) |
|---|---|---|
| **Immune complex GN** | Lupus nephritis, APSGN, IgA nephropathy/IgA vasculitis, MPGN | Granular |
| **Anti-GBM disease** | Goodpasture syndrome | **Linear** IgG |
| **Pauci-immune GN (ANCA)** | GPA, MPA, EGPA | แทบไม่มี deposit |

### RPGN

- Cr เพิ่มขึ้นเร็วในหลายสัปดาห์ถึงเดือน + nephritic sediment
- พยาธิสภาพคือ **crescent** ใน glomerulus (เสริม)
- สาเหตุ 3 กลุ่มเดียวกับข้างบน: anti-GBM, immune complex, pauci-immune → ต้องส่ง **anti-GBM, ANCA, C3/C4, ANA** และทำ **renal biopsy เร็ว** เพราะรักษาช้าไตเสียถาวร (เสริม)

### Chronic GN — เบาะแสในโจทย์

- มีประวัติ gross hematuria/บวมเมื่อหลายปีก่อน
- ซีด (↓EPO), Ca ต่ำ PO4 สูง, nocturia (เข้มข้นปัสสาวะไม่ได้)
- **Broad waxy cast** และไตเล็กใน U/S
''',
    figs=[F_MAP],
    pearls=[
        "Nephritic = ↑BP + hematuria + RBC cast + proteinuria <3.5 g/d",
        "Nephrotic = proteinuria >3.5 g/d + albumin ต่ำ + cholesterol สูง + fatty cast",
        "AGN วัน–สัปดาห์ · RPGN สัปดาห์–เดือน · Chronic GN >3 เดือน",
        "RPGN แบ่ง 3 กลุ่มตาม IF: linear (anti-GBM) · granular (immune complex) · pauci-immune (ANCA)",
        "ประวัติเก่า + ซีด + Ca ต่ำ PO4 สูง + broad waxy cast = chronic GN/CKD",
    ],
    items=[
        mcq("NEPHRO-02-01-1",
            "A 25-year-old woman presents with oliguria and edema. BP 160/110 mmHg, pitting edema 4+. Na 130, K 4.8, Cl 100, HCO3 22 mEq/L. Urinalysis: sp.gr. 1.025, pH 5.5, WBC 10–20/HPF, RBC 30–50/HPF, protein 3+. What is the most likely diagnosis?",
            "Acute glomerulonephritis",
            ["Prerenal azotemia", "Renal artery stenosis", "Acute tubular necrosis", "Acute interstitial nephritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ความดันสูง + บวม + oliguria + **RBC 30–50 ร่วมกับ protein 3+** = nephritic picture → **acute glomerulonephritis** (sp.gr. สูงเพราะ tubule ยังดีและมีโปรตีน)
- Prerenal จะไม่มี hematuria และ proteinuria มากขนาดนี้ และผู้ป่วยไม่ได้ขาดน้ำ (บวม 4+)
- Renal artery stenosis ทำให้ความดันสูงได้แต่ UA มักปกติ
- ATN จะมี sp.gr. ต่ำ ~1.010 และ muddy brown cast
- AIN จะเด่นที่ WBC/eosinophil และมีประวัติยา''',
            pearl="HT + edema + hematuria + proteinuria = AGN", topic="Acute GN",
            ref=[f"{D} หน้า 75–76"], nl=["2.3.14(2)"]),
        mcq("NEPHRO-02-01-2",
            "A 30-year-old woman has generalized edema for 6 weeks and decreased urine output for 2 weeks. BP 160/100 mmHg, puffy eyelids, engorged neck veins, pitting edema 2+. Urinalysis: albumin 3+, RBC 10–20/HPF, WBC 5–10/HPF, RBC casts 1–2/LPF. Cr 3.2 mg/dL (normal 1 year ago). What is the most likely diagnosis?",
            "Rapidly progressive glomerulonephritis",
            ["Acute tubular necrosis", "Minimal change disease", "Chronic glomerulonephritis", "Acute interstitial nephritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Nephritic sediment (RBC cast, proteinuria) + ไตวายที่เกิดภายใน **หลายสัปดาห์** (6 สัปดาห์) = **RPGN** ต้องหาสาเหตุใน 3 กลุ่ม: anti-GBM, immune complex (LN, IgAN, APSGN, MPGN), pauci-immune (GPA, MPA, EGPA)
- ATN ไม่มี RBC cast และไม่ได้เป็นต่อเนื่องหลายสัปดาห์โดยไม่มีเหตุกระตุ้น
- MCD เป็น nephrotic ล้วน ไม่มี RBC cast ความดันมักไม่สูง
- Chronic GN ต้องเป็น > 3 เดือน มีซีด ไตเล็ก broad cast — รายนี้ Cr ปกติเมื่อ 1 ปีก่อนและไม่ซีด
- AIN เด่น WBC cast/eosinophil''',
            pearl="Nephritic + Cr ขึ้นในหลายสัปดาห์ = RPGN", topic="RPGN",
            ref=[f"{D} หน้า 77–78"], nl=["2.3.14(2)"]),
        mcq("NEPHRO-02-01-3",
            "A patient presents with fatigue and nocturia for 3 months and reports an episode of gross hematuria 2 years ago. BP 170/100 mmHg, pale, pitting edema 2+. Urinalysis: albumin 3+, sp.gr. 1.015, RBC 10–15/HPF. Ca 7 mg/dL, PO4 6 mg/dL, BUN 70 mg/dL, Cr 7 mg/dL. What is the most likely diagnosis?",
            "Chronic glomerulonephritis",
            ["Acute poststreptococcal glomerulonephritis", "Multiple myeloma", "Renal cell carcinoma", "Renal calculi"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ประวัติ **gross hematuria เมื่อ 2 ปีก่อน** (อาจเป็น IgAN) + อาการนาน 3 เดือน + ซีด + **Ca ต่ำ PO4 สูง** + nocturia = โรค glomerulus ที่ดำเนินมาเป็น **chronic GN/CKD**
- APSGN เป็นเฉียบพลันหลังติดเชื้อ ไม่ทำให้ซีดและ Ca ต่ำ PO4 สูง
- Multiple myeloma ทำให้ Ca **สูง** ไม่ใช่ต่ำ และมักอายุมาก ปวดกระดูก
- RCC มาด้วย hematuria ก้อนที่เอว แต่ไม่ทำ proteinuria 3+ และไตวายรุนแรงแบบนี้
- นิ่วมาด้วยปวดแบบ colic''',
            pearl="อาการเรื้อรัง + ซีด + Ca ต่ำ PO4 สูง → CKD/chronic GN", topic="Chronic GN",
            ref=[f"{D} หน้า 79–80"], nl=["2.3.14-3(1)"]),
        mcq("NEPHRO-02-01-4",
            "A 45-year-old woman has fatigue, pallor, and vomiting with edema for 2 weeks. Two years ago she had generalized edema. BP 180/110 mmHg, pale conjunctivae, bilateral basal crepitations, pitting edema 2+. Urinalysis: sp.gr. 1.010, albumin 2+, WBC 5–10/HPF, RBC 10–20/HPF, broad waxy casts 1–2/LPF. What is the most likely diagnosis?",
            "Chronic glomerulonephritis",
            ["Acute glomerulonephritis", "Acute tubular necrosis", "Rapidly progressive glomerulonephritis", "Chronic tubulointerstitial nephritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''สไลด์สรุปสองเบาะแส: **onset 2 ปีก่อน** และ **broad waxy cast = CKD** ร่วมกับ hematuria + proteinuria (ต้นเหตุจาก glomerulus) + ซีด → **chronic GN**
- AGN และ RPGN เป็นเฉียบพลัน/กึ่งเฉียบพลัน ไม่มี broad waxy cast และประวัติ 2 ปี
- ATN ไม่มี proteinuria 2+ และ hematuria แบบนี้ และไม่เรื้อรัง
- Chronic tubulointerstitial nephritis มี proteinuria น้อยและไม่มี hematuria เด่น''',
            pearl="Broad waxy cast + ประวัติหลายปี = chronic GN", topic="Chronic GN",
            ref=[f"{D} หน้า 81–82"], nl=["2.3.14-3(1)"]),
        mcq("NEPHRO-02-01-5",
            "A 32-year-old man has leg edema and dark urine. BP 150/95 mmHg. Urinalysis: protein 2+, RBC 50–100/HPF (dysmorphic), RBC casts present. 24-hour urine protein is 1.8 g. Serum C3 and C4 are normal. Among the following, which is the most likely diagnosis?",
            "IgA nephropathy",
            ["Minimal change disease", "Focal segmental glomerulosclerosis", "Membranous nephropathy", "Diabetic nephropathy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (เพิ่มรายละเอียดให้ตัดสินได้)",
            explain='''ภาพเด่นคือ **hematuria มาก (RBC 50–100, dysmorphic, RBC cast)** โดย proteinuria ไม่ถึง nephrotic range และ complement ปกติ = nephritic → ในตัวเลือก มีแต่ **IgA nephropathy** ที่เป็นโรค nephritic
- MCD, FSGS และ MN เป็นสาเหตุ **nephrotic** ที่ hematuria น้อยหรือไม่มี (FSGS มี hematuria ได้เล็กน้อย แต่ไม่มี RBC cast เด่น)
- Diabetic nephropathy ต้องมีประวัติเบาหวานและ sediment ไม่ active
หมายเหตุ: โจทย์ในสไลด์สั้นมาก (ขาบวม protein 2+ RBC 50–100) และไม่ได้แสดงเฉลย''',
            pearl="Hematuria เด่น + complement ปกติ → IgAN", topic="Nephritic vs nephrotic causes",
            ref=[f"{D} หน้า 99–100"], nl=["2.3.14(2)"]),
    ])

# ---------------------------------------------------------------- 02-02 APSGN
F_LAT = fig("nephro-02-02-f1", "ระยะแฝงหลังติดเชื้อ: APSGN vs IgA nephropathy", '''<svg viewBox="0 0 740 240">
 <defs><marker id="nephro-02-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <path d="M60 180H720" class="ln" marker-end="url(#nephro-02-02-a)"/>
 <text x="720" y="230" text-anchor="end" class="t3">สัปดาห์หลังติดเชื้อ</text>
 <path d="M60 172V188" class="ln"/><text x="60" y="204" text-anchor="middle" class="t3">0</text>
 <path d="M160 172V188" class="ln"/><text x="160" y="204" text-anchor="middle" class="t3">1</text>
 <path d="M260 172V188" class="ln"/><text x="260" y="204" text-anchor="middle" class="t3">2</text>
 <path d="M360 172V188" class="ln"/><text x="360" y="204" text-anchor="middle" class="t3">3</text>
 <path d="M460 172V188" class="ln"/><text x="460" y="204" text-anchor="middle" class="t3">4</text>
 <path d="M560 172V188" class="ln"/><text x="560" y="204" text-anchor="middle" class="t3">5</text>
 <path d="M660 172V188" class="ln"/><text x="660" y="204" text-anchor="middle" class="t3">6</text>
 <rect x="60" y="22" width="72" height="34" rx="8" class="c2"/>
 <text x="96" y="44" text-anchor="middle" class="tw">IgAN</text>
 <text x="142" y="36" class="t2">&lt; 5 วัน (synpharyngitic)</text>
 <text x="142" y="52" class="t3">ผู้ใหญ่ · gross hematuria · C3 ปกติ</text>
 <rect x="160" y="74" width="200" height="34" rx="8" class="ac"/>
 <text x="260" y="96" text-anchor="middle" class="tw">APSGN หลังคออักเสบ</text>
 <text x="370" y="96" class="t2">1–3 สัปดาห์</text>
 <rect x="360" y="124" width="300" height="34" rx="8" class="acsoft"/>
 <text x="510" y="146" text-anchor="middle" class="tb">APSGN หลังติดเชื้อผิวหนัง 3–6 สัปดาห์</text>
</svg>''', "ดูระยะห่างระหว่างการติดเชื้อกับปัสสาวะเป็นเลือด: ไม่ถึง 5 วันนึกถึง IgAN ส่วน 1–6 สัปดาห์นึกถึง APSGN (C3 ต่ำ)")

S2 = sec("nephro-02-02", "Acute poststreptococcal GN (APSGN)",
    "เด็ก/ผู้สูงอายุ หลัง GAS pharyngitis 1–3 สัปดาห์ หรือผิวหนัง 3–6 สัปดาห์ · ↓C3 C4 ปกติ · ASO ↑ · รักษา supportive", minutes=8,
    source=f"{D} หน้า 56–60, 85–90", nl=["B9.2.2(3)", "2.3.14(2)"],
    md='''
### ใครเป็น / กลไก

- **เด็กและผู้สูงอายุ**
- เกิดตามหลังติดเชื้อ **Group A β-hemolytic Streptococcus (GAS)** ชนิด nephritogenic
  - **Pharyngitis → 1–3 สัปดาห์**
  - **Skin infection (impetigo, pustule) → 3–6 สัปดาห์**
- กลไก: immune complex ของ antigen streptococcus ไปตกที่ glomerulus → กระตุ้น complement ทาง alternative pathway → **C3 ต่ำ** (เสริม)

[[fig:nephro-02-02-f1]]

### อาการ (Acute GN, บางรายเป็น RPGN)

- **↑BP, headache** (บางรายเป็น hypertensive encephalopathy)
- **Edema โดยเฉพาะหน้า/หนังตาบวม** (puffy eyelids)
- **Hematuria (ปัสสาวะสีโค้ก/น้ำล้างเนื้อ), oliguria**
- Flank pain
- อาจมี volume overload: engorged neck vein, pulmonary edema

### Investigation

- ↑BUN, Cr
- UA: RBC, dysmorphic RBC, **RBC cast**, proteinuria
- **↓C3, C4 ปกติ** (C3 กลับปกติภายใน ~6–8 สัปดาห์ ถ้ายังต่ำนานกว่านั้นให้คิดถึง MPGN/LN (เสริม))
- **↑ASO, ↑anti-DNase B** (anti-DNase B ไวกว่าหลังติดเชื้อผิวหนัง (เสริม))
- **Renal biopsy มักไม่จำเป็น** ทำเฉพาะ RPGN หรือ atypical presentation

### Renal biopsy (ถ้าทำ)

| | ลักษณะ |
|---|---|
| Light microscopy | **Diffuse endocapillary proliferation** (diffuse proliferative GN) |
| Immunofluorescence | **Granular** subepithelial IgG, IgM, C3 ("starry sky") |
| Electron microscopy | **Subepithelial humps** |

### การรักษา (supportive)

- **Edema & BP**: low-sodium diet, fluid restriction, **loop diuretic (furosemide)**
- ยาความดัน: **CCB (nifedipine)**, ACEI/ARB (**หลีกเลี่ยงถ้ามี AKI หรือ K สูง**)
- **Hypertensive encephalopathy** (headache, vomiting, confusion, seizure, blurry vision, papilledema) → **IV nicardipine, sodium nitroprusside**
- **Antibiotic: penicillin V หรือ amoxicillin เฉพาะกรณียังมี active infection** (ไม่ได้ช่วยไตหายเร็วขึ้น แต่ตัดการแพร่เชื้อ (เสริม))

> พยากรณ์โรคในเด็กดีมาก หายเองเกือบทั้งหมด — ข้อลวงในข้อสอบเก่า: "พยากรณ์ไม่ดี", "pauci-immune", "Streptococcus viridans", "nephrotic range + RPGN บ่อย" ล้วนผิด
''',
    figs=[F_LAT],
    pearls=[
        "APSGN: เจ็บคอ 1–3 สัปดาห์ / ผิวหนัง 3–6 สัปดาห์ ก่อนบวม ความดันสูง ปัสสาวะสีโค้ก",
        "APSGN = ↓C3, C4 ปกติ, ↑ASO/anti-DNase B",
        "Biopsy: diffuse endocapillary proliferation · granular IF · subepithelial humps",
        "รักษา: จำกัดเกลือ/น้ำ + furosemide + CCB · ATB เฉพาะยังติดเชื้อ",
        "C3 ต่ำนานเกิน 8 สัปดาห์ → คิด MPGN หรือ lupus (เสริม)",
    ],
    items=[
        mcq("NEPHRO-02-02-1",
            "A 9-year-old boy has facial and leg swelling for 7 days with decreased urine output. He had impetigo-like pustules on his arms 2 weeks earlier. BT 37.3 °C, BP 150/110 mmHg, puffy eyelids, leg edema. Urinalysis: sp.gr. 1.020, albumin 2+, RBC 30–50/HPF, WBC 3–5/HPF, RBC casts 1–2/LPF. Which renal histopathology is most likely?",
            "Diffuse proliferative glomerulonephritis",
            ["Focal proliferative glomerulonephritis", "Focal and segmental glomerulosclerosis", "Diffuse thickening of the glomerular capillary wall", "Fusion of foot processes of visceral epithelial cells"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ติดเชื้อผิวหนังก่อน 2 สัปดาห์ + nephritic syndrome ในเด็ก = **APSGN** พยาธิสภาพคือ **diffuse endocapillary proliferation** (diffuse proliferative GN) ทุก glomerulus มีเซลล์เพิ่ม
- Focal proliferative GN พบใน IgAN หรือ lupus class III ไม่ใช่ APSGN
- FSGS เป็นสาเหตุ nephrotic ไม่ใช่ nephritic หลังติดเชื้อ
- Diffuse capillary wall thickening คือ membranous nephropathy
- Foot process fusion เพียงอย่างเดียวคือ minimal change disease''',
            pearl="APSGN = diffuse (endocapillary) proliferative GN", topic="APSGN pathology",
            ref=[f"{D} หน้า 59, 89–90"], nl=["B9.2.2(3)"]),
        mcq("NEPHRO-02-02-2",
            "A 16-year-old boy has had swelling for 1 week; 2 weeks before the swelling he had a sore throat. BP 150/100 mmHg, puffy eyelids, engorged neck veins, leg edema. BUN 28 mg/dL, Cr 1.8 mg/dL, ASO titer 1:640. Urinalysis: albumin 3+, RBC 10–20, RBC casts 1–2. Which statement about this condition is correct?",
            "Serum complement (C3) is low",
            ["It is caused by viridans streptococci", "Nephrotic-range proteinuria and RPGN are common", "The mechanism is pauci-immune", "Most patients progress to chronic kidney failure"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''APSGN เป็น immune complex GN ที่กระตุ้น complement จึงพบ **C3 ต่ำ (C4 ปกติ)** — สไลด์เฉลย ↓C3 normal C4
- สาเหตุคือ Group A β-hemolytic streptococcus ไม่ใช่ viridans
- ส่วนใหญ่มาเป็น acute GN proteinuria ไม่ถึง nephrotic range และ RPGN พบน้อย
- กลไกเป็น immune complex (granular deposit) ไม่ใช่ pauci-immune ซึ่งเป็นของ ANCA vasculitis
- พยากรณ์โรคดี โดยเฉพาะในเด็ก ส่วนใหญ่หายสนิท''',
            pearl="APSGN = ↓C3 + C4 ปกติ + ASO สูง", topic="APSGN complement",
            ref=[f"{D} หน้า 58, 87–88"], nl=["B9.2.2(3)"]),
        mcq("NEPHRO-02-02-3",
            "An 8-year-old boy with APSGN develops severe headache, vomiting, blurred vision, and a generalized seizure. BP 190/120 mmHg. Fundoscopy shows papilledema. What is the most appropriate antihypertensive treatment?",
            "Intravenous nicardipine",
            ["Oral enalapril", "Oral hydrochlorothiazide", "Intravenous normal saline", "Oral propranolol"],
            explain='''ความดันสูงมากร่วมกับปวดศีรษะ อาเจียน ตามัว ชัก papilledema = **hypertensive encephalopathy** จาก APSGN ต้องลดความดันด้วยยาฉีด **IV nicardipine** หรือ sodium nitroprusside ตามสไลด์
- Enalapril กินออกฤทธิ์ช้า และควรเลี่ยง ACEI เมื่อมี AKI/K สูง
- Thiazide ออกฤทธิ์ช้าและได้ผลน้อยเมื่อ GFR ลด (ใช้ loop diuretic ดีกว่า)
- NSS เพิ่ม volume ทำให้ความดันสูงขึ้น
- Propranolol กินไม่เหมาะกับภาวะฉุกเฉิน''',
            pearl="APSGN + hypertensive encephalopathy → IV nicardipine/SNP", topic="APSGN management",
            ref=[f"{D} หน้า 60"], nl=["B9.2.2(3)"]),
        mcq("NEPHRO-02-02-4",
            "A boy presents with edema and hypertension (nephritic syndrome). Examination shows healing pustular lesions on both legs. What is the most likely diagnosis?",
            "Acute poststreptococcal glomerulonephritis",
            ["Lupus nephritis", "IgA nephropathy", "Minimal change disease", "Anti-GBM disease"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''เด็ก + nephritic syndrome + **pustule ที่ผิวหนัง (impetigo จาก GAS)** = **APSGN** ระยะแฝงหลังติดเชื้อผิวหนัง 3–6 สัปดาห์
- Lupus nephritis พบในผู้หญิงวัยเจริญพันธุ์ มีอาการ SLE อื่น
- IgAN สัมพันธ์กับ URI/GI infection และเกิดภายใน 5 วัน มักในผู้ใหญ่
- MCD เป็น nephrotic syndrome ไม่มีความดันสูงและ hematuria
- Anti-GBM มาด้วย RPGN + ไอเป็นเลือดในผู้ใหญ่''',
            pearl="Nephritic + impetigo ในเด็ก = APSGN", topic="APSGN",
            ref=[f"{D} หน้า 85–86"], nl=["B9.2.2(3)"]),
        mcq("NEPHRO-02-02-5",
            "A 17-year-old girl presents with malaise, sore throat, and visible hematuria that began during the same week as the sore throat. BP 160/70 mmHg. Cholesterol 200 mg/dL, Cr 1.8 mg/dL (baseline 0.8). Urinalysis: RBC 10–15/HPF (dysmorphic), WBC 20–30/HPF, protein 3+. Serum C3 is normal. What is the most likely diagnosis?",
            "IgA nephropathy",
            ["Post-streptococcal glomerulonephritis", "Urolithiasis", "Acute hemorrhagic cystitis", "Acute interstitial nephritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (เพิ่ม C3 ปกติให้ตัดสินได้)",
            explain='''Hematuria เกิด **พร้อมกับ** อาการเจ็บคอ (synpharyngitic) + dysmorphic RBC + proteinuria + Cr ขึ้น + **C3 ปกติ** = **IgA nephropathy**
- APSGN ต้องมีระยะแฝง 1–3 สัปดาห์หลังเจ็บคอ และ C3 ต่ำ
- นิ่วทำให้ปวด colic และ RBC ไม่ dysmorphic ไม่มี proteinuria 3+
- Hemorrhagic cystitis มี dysuria เลือดสด RBC ไม่ dysmorphic
- AIN เด่นที่ WBC/eosinophil และประวัติยา (WBC ในรายนี้มาจากการอักเสบของ glomerulus)
หมายเหตุ: สไลด์ไม่ได้แสดงเฉลยและไม่ได้ให้ค่า C3 — ข้อนี้เพิ่ม C3 ปกติเพื่อให้มีคำตอบเดียว''',
            pearl="Hematuria พร้อมเจ็บคอ + C3 ปกติ = IgAN", topic="IgAN vs APSGN",
            ref=[f"{D} หน้า 83–84, 91–92"], nl=["2.3.14(2)"]),
    ])

# ---------------------------------------------------------------- 02-03 IgAN
S3 = sec("nephro-02-03", "IgA nephropathy & IgA vasculitis (HSP)",
    "Hematuria ภายใน 5 วันหลัง URI · C3 C4 ปกติ · mesangial IgA · ACEI/ARB เมื่อ proteinuria >0.5 g", minutes=8,
    source=f"{D} หน้า 61–64, 83–84, 93–104", nl=["2.3.14(2)", "2.3.13-3(2)", "2.1.43"],
    md='''
**IgA nephropathy (Berger disease)** = GN ที่พบบ่อยที่สุดในโลก (เสริม) เกิดจาก IgA1 ที่ glycosylation ผิดปกติจับเป็น immune complex ไปตกที่ **mesangium**

### IgA nephropathy

- **ผู้ใหญ่** (มักเป็นแค่ไต)
- Presentation หลัก: **asymptomatic hematuria, chronic GN** · ส่วนน้อยเป็น acute GN, RPGN, nephrotic syndrome
- อาการเกิด **< 5 วันหลัง URI หรือ GI infection** (synpharyngitic hematuria)
  - Gross/microscopic hematuria (ปัสสาวะสีน้ำล้างเนื้อเป็นพัก ๆ)
  - Flank pain, low-grade fever, ↑BP

### IgA vasculitis (Henoch–Schönlein purpura)

- **พบบ่อยในเด็ก**, multiple organ involvement
- **Palpable purpura** (ขา/ก้น), **arthritis/arthralgia**, **abdominal pain**
- Renal involvement (IgAV nephritis) — พยาธิสภาพเหมือน IgAN

> IgA nephropathy มักเจอใน adult และเป็นแค่ไต · IgA vasculitis มักเจอใน children และหลายระบบ

### Investigation

- ± ↑BUN, Cr
- UA: RBC, dysmorphic RBC, RBC cast, proteinuria
- **Normal C3, C4** (จุดแยกจาก APSGN)
- **↑Serum IgA** (พบประมาณครึ่งหนึ่ง จึงไม่ใช้วินิจฉัย (เสริม))
- **Renal biopsy** (วินิจฉัยแน่นอน) ทำเมื่อโรคไตรุนแรง: ↑Cr, **proteinuria > 0.5–1 g/24 hr**, secondary HT

| Biopsy | ลักษณะ |
|---|---|
| LM | **Mesangial proliferation** |
| IF | **Mesangial IgA deposits** |
| EM | Mesangial immune deposits |

### การรักษา

- คุม BP และ proteinuria (> 0.5 g/24 h) → **ACEI/ARB**
- Severe/RPGN → **steroid + cyclophosphamide**
- (เสริม) แนวทางปัจจุบัน (KDIGO 2021/2025) เพิ่ม SGLT2i และพิจารณา steroid เป็นราย ๆ ในผู้ที่ proteinuria ยังสูงแม้ได้ ACEI/ARB เต็มที่ — ข้อสอบ NL ยึด ACEI/ARB เป็นหลัก

### แยกจากโรคคล้ายกันในข้อสอบ

| | IgAN | APSGN |
|---|---|---|
| ระยะหลังติดเชื้อ | **< 5 วัน** (ระหว่างป่วย) | **1–3 สัปดาห์** (คอ), 3–6 สัปดาห์ (ผิวหนัง) |
| อายุ | ผู้ใหญ่ | เด็ก (และผู้สูงอายุ) |
| C3 | **ปกติ** | **ต่ำ** |
| Course | เป็นซ้ำ ๆ อาจไปเป็น CKD | หายเองส่วนใหญ่ |

> หญิงตั้งครรภ์ **GA 12 สัปดาห์** มีความดันสูง + dysmorphic RBC → เป็นโรคไตเดิม (เช่น IgAN) ไม่ใช่ preeclampsia เพราะ preeclampsia เกิดหลัง 20 สัปดาห์
''',
    pearls=[
        "IgAN = gross hematuria ภายใน 1–5 วันหลัง URI/GI infection ในผู้ใหญ่ · C3 C4 ปกติ",
        "IgAV (HSP) = เด็ก + palpable purpura + ปวดข้อ + ปวดท้อง + hematuria",
        "Biopsy IgAN/HSP: mesangial proliferation + mesangial IgA",
        "Proteinuria >0.5 g/day → ACEI/ARB · severe/RPGN → steroid + cyclophosphamide",
        "Nephritic-nephrotic + complement ปกติ → IgAN",
    ],
    items=[
        mcq("NEPHRO-02-03-1",
            "A 30-year-old woman notices meat-wash colored urine. Three days earlier she had fever, cough, and sore throat and bought medication herself. Urinalysis: RBC 100/HPF (dysmorphic), WBC 5–10/HPF. What is the most likely diagnosis?",
            "IgA nephropathy",
            ["Acute poststreptococcal glomerulonephritis", "Ureteric stone", "Acute pyelonephritis", "Acute interstitial nephritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ปัสสาวะเป็นเลือดเกิด **เพียง 3 วันหลังเริ่ม URI** (synpharyngitic) ในผู้ใหญ่ = **IgA nephropathy** (เกิด < 5 วัน)
- APSGN ต้องมีระยะแฝง 1–3 สัปดาห์หลังคออักเสบ
- Ureteric stone มาด้วยปวด colic ไม่มีความสัมพันธ์กับ URI และ RBC ไม่ dysmorphic
- Acute pyelonephritis ต้องมีไข้สูง ปวดเอว WBC มากและแบคทีเรีย
- AIN จากยาที่ซื้อกินมักเกิดหลังได้ยา 1–3 สัปดาห์และเด่นที่ WBC/eosinophil''',
            pearl="Hematuria ภายใน 5 วันหลัง URI = IgAN", topic="IgA nephropathy",
            ref=[f"{D} หน้า 61, 97–98"], nl=["2.3.14(2)", "2.1.43"]),
        mcq("NEPHRO-02-03-2",
            "A 15-year-old boy has abdominal pain and a red rash on both legs. BP 110/60 mmHg, no edema. The rash is palpable purpura on the buttocks and legs. Urinalysis: albumin 1+, RBC 20–30/HPF, WBC 1–3/HPF. Which renal histopathologic finding is most likely?",
            "Mesangial cell proliferation",
            ["Capillary wall thickening", "Segmental glomerulosclerosis", "Crescent formation", "Endothelial cell proliferation"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ปวดท้อง + palpable purpura ที่ขา + hematuria ในวัยรุ่น = **IgA vasculitis (HSP) nephritis** ซึ่งพยาธิสภาพเหมือน IgAN คือ **mesangial proliferation + mesangial IgA deposit**
- Capillary wall thickening คือ membranous nephropathy
- Segmental sclerosis คือ FSGS
- Crescent พบใน RPGN (anti-GBM, ANCA) — รายนี้ไตยังดี ไม่มีบวม/ความดันสูง
- Endocapillary (endothelial) proliferation แบบ diffuse คือ APSGN''',
            pearl="HSP nephritis = mesangial proliferation + IgA", topic="IgA vasculitis",
            ref=[f"{D} หน้า 61, 63, 103–104"], nl=["2.3.13-3(2)"]),
        mcq("NEPHRO-02-03-3",
            "A pregnant woman at 12 weeks' gestation is found to have BP 150/90 mmHg. BUN 30 mg/dL, Cr 0.4 mg/dL. Urinalysis: RBC 20–30/HPF with dysmorphic RBC, WBC 1–2/HPF. What is the most likely cause of her hypertension?",
            "IgA nephropathy",
            ["Preeclampsia", "Acute tubulointerstitial nephritis", "Renal artery stenosis", "Essential hypertension"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ความดันสูงตั้งแต่ **GA 12 สัปดาห์** ร่วมกับ **dysmorphic RBC** (glomerular hematuria) → มีโรค glomerulus อยู่เดิม ในหญิงอายุน้อยที่พบบ่อยคือ **IgA nephropathy** (ความดันสูงก่อน 20 สัปดาห์ = chronic HT)
- Preeclampsia เกิดหลัง GA 20 สัปดาห์และเด่นที่ proteinuria ไม่ใช่ dysmorphic RBC
- AIN ไม่ได้ทำให้ความดันสูงเด่นและจะมี WBC มาก
- Renal artery stenosis ทำความดันสูงได้แต่ไม่มี glomerular hematuria
- Essential HT ไม่อธิบาย dysmorphic RBC''',
            pearl="HT ก่อน 20 สัปดาห์ + dysmorphic RBC = โรคไตเดิม (เช่น IgAN) ไม่ใช่ preeclampsia", topic="IgAN in pregnancy",
            ref=[f"{D} หน้า 93–94"], nl=["2.3.14(2)"]),
        mcq("NEPHRO-02-03-4",
            "A patient's urinalysis shows a mixed nephritic–nephrotic picture (dysmorphic RBC, RBC casts, and proteinuria 4 g/day). Serum C3 and C4 are both normal. Which diagnosis is most likely?",
            "IgA nephropathy",
            ["Systemic lupus erythematosus", "Minimal change disease", "Membranous nephropathy", "Acute poststreptococcal glomerulonephritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''มี nephritic component (dysmorphic RBC, RBC cast) ร่วมกับ proteinuria ระดับ nephrotic และ **complement ปกติ** → ในตัวเลือก มีเพียง **IgA nephropathy** ที่เป็น nephritic ได้โดย complement ปกติ (ส่วนน้อยมาเป็น nephrotic)
- SLE (lupus nephritis) จะมี C3 และ C4 ต่ำ
- APSGN มี C3 ต่ำ
- MCD และ MN เป็น nephrotic ล้วน ไม่มี RBC cast''',
            pearl="Nephritic + complement ปกติ → IgAN, anti-GBM, ANCA", topic="Complement-guided diagnosis",
            ref=[f"{D} หน้า 74, 101–102"], nl=["2.3.14(2)"]),
        mcq("NEPHRO-02-03-5",
            "A 20-year-old man develops visible hematuria 1 day after the onset of fever and sore throat. He has never had edema or hematuria before. BP 130/110 mmHg, puffy eyelids. Urinalysis: dysmorphic RBC 100–200/HPF, protein 1+. Among the following, which test best supports the most likely diagnosis?",
            "Serum IgA level",
            ["ASO titer", "Antinuclear antibody", "Anti-dsDNA", "ANCA"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Hematuria เกิด **1 วันหลังเจ็บคอ** ในผู้ใหญ่ = IgA nephropathy ในตัวเลือก **serum IgA** สนับสนุนการวินิจฉัย (สไลด์ระบุ ↑serum IgA) แม้การวินิจฉัยแน่นอนต้องใช้ renal biopsy
- ASO ใช้สนับสนุน APSGN ซึ่งต้องมีระยะแฝง 1–3 สัปดาห์ ถ้าส่งในวันที่ 1 จะยังไม่ขึ้น
- ANA และ anti-dsDNA ใช้กับ lupus ซึ่งไม่มีอาการทางระบบอื่น
- ANCA ใช้กับ pauci-immune vasculitis ที่มักมาเป็น RPGN และอาการปอด/ไซนัส''',
            pearl="IgAN: serum IgA ช่วยสนับสนุน แต่ biopsy คือตัวยืนยัน", topic="IgAN investigation",
            ref=[f"{D} หน้า 62, 95–96"], nl=["2.3.14(2)"]),
    ])

# ---------------------------------------------------------------- 02-04 Lupus nephritis
S4 = sec("nephro-02-04", "Lupus nephritis",
    "หญิงวัยกลางคน + อาการ SLE · ↓C3 ↓C4 · ANA/anti-dsDNA · biopsy แยก class · class III/IV ให้ steroid + immunosuppressant", minutes=6,
    source=f"{D} หน้า 64–68, 105–108", nl=["2.3.13-3(15)", "2.3.14(2)", "2.3.14(12)"],
    md='''
### ใครเป็น / อาการ

- **Adult female middle age** (หญิงวัยเจริญพันธุ์)
- เป็นได้ทุกแบบ: **acute GN, chronic GN, RPGN, nephrotic** (และ mixed)
- ↑BP, edema, hematuria + **อาการ SLE ระบบอื่น**: malar rash, oral ulcer (เพดานแข็ง), arthritis, serositis, cytopenia (เสริม)

### Investigation

- ↑BUN, Cr
- UA: nephritic หรือ nephrotic sediment
- **UPCR ≥ 0.5 g/g หรือ 24-hr urine protein ≥ 0.5 g** → ถือว่ามี LN ต้องประเมิน/biopsy
- **↓C3, ↓C4 (hallmark)** — complement ต่ำทั้งคู่จาก classical pathway
- **ANA, anti-dsDNA positive** (ANA ไวมาก ใช้ตรวจคัดกรอง · anti-dsDNA จำเพาะและสัมพันธ์กับ LN (เสริม))
- **Kidney biopsy** = confirm dx และบอก class

### ISN/RPS classification (สไลด์เป็นภาพ — สรุปเสริม)

| Class | ชื่อ | จำง่าย |
|---|---|---|
| I | Minimal mesangial | ไม่มีอาการ |
| II | Mesangial proliferative | hematuria เล็กน้อย |
| III | **Focal** proliferative (< 50% glomeruli) | nephritic |
| IV | **Diffuse** proliferative (≥ 50%) | รุนแรงสุด พบบ่อยสุด wire-loop |
| V | **Membranous** | nephrotic |
| VI | Advanced sclerosing (≥ 90%) | ESRD |

### การรักษา

- Tx SLE (hydroxychloroquine ทุกราย (เสริม)) + CKD management (ACEI/ARB คุม proteinuria)
- **LN class III/IV: steroid + immunosuppressants** (mycophenolate หรือ IV cyclophosphamide เป็น induction (เสริม))

> โจทย์ "ผู้ชาย/ผู้หญิงอายุน้อย บวม ฉี่เป็นฟอง + ผื่นแดงที่แก้มข้ามสันจมูก" → ส่ง **ANA** ก่อน (คัดกรอง SLE)
''',
    pearls=[
        "Lupus nephritis = ↓C3 + ↓C4 (ต่ำทั้งคู่)",
        "UPCR ≥0.5 g/g ใน SLE → ประเมิน lupus nephritis / biopsy",
        "Class IV diffuse proliferative = รุนแรงสุด · class V = membranous (nephrotic)",
        "Class III/IV → steroid + immunosuppressant",
    ],
    items=[
        mcq("NEPHRO-02-04-1",
            "A woman of reproductive age has fever, dyspnea, and knee pain for 2 months. Vital signs are stable. There is an oral ulcer on the hard palate and both knees are red and swollen. Urinalysis: many RBC and WBC, proteinuria, RBC casts. What is the most likely diagnosis?",
            "Systemic lupus erythematosus with lupus nephritis",
            ["Polyarteritis nodosa", "Juvenile rheumatoid arthritis", "Acute poststreptococcal glomerulonephritis", "Gonococcal arthritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''หญิงวัยเจริญพันธุ์ + **oral ulcer ที่ hard palate + arthritis + serositis (เหนื่อย)** + nephritic sediment (RBC cast) = **SLE with lupus nephritis**
- Polyarteritis nodosa เป็น vasculitis หลอดเลือดขนาดกลาง ไม่ทำ GN (ไม่มี RBC cast) และไม่มี oral ulcer
- JRA เป็นโรคเด็กอายุ < 16 ปี และไม่ทำ GN
- APSGN ไม่มี oral ulcer/arthritis นาน 2 เดือน
- Gonococcal arthritis มี tenosynovitis/ผื่น pustule ไม่ทำ GN''',
            pearl="Oral ulcer + arthritis + nephritic UA ในหญิงสาว = SLE", topic="Lupus nephritis",
            ref=[f"{D} หน้า 65, 105–106"], nl=["2.3.13-3(15)"]),
        mcq("NEPHRO-02-04-2",
            "A 30-year-old man has generalized swelling and foamy urine. Vital signs are normal. Examination shows pitting edema 2+, puffy eyelids, and an erythematous rash over both cheeks across the nasal bridge sparing the nasolabial folds. What is the most appropriate initial investigation?",
            "Antinuclear antibody (ANA)",
            ["ASO titer", "Anti-CCP antibody", "Anti-GBM antibody", "Serum IgA"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''บวม ฉี่เป็นฟอง (nephrotic) + **malar rash** → สงสัย **SLE (lupus nephritis class V หรือ mixed)** การตรวจคัดกรองเริ่มต้นคือ **ANA** (ไวสูง ถ้าลบแทบตัด SLE ออก) แล้วตามด้วย anti-dsDNA, C3/C4 และ biopsy
- ASO ใช้กับ APSGN ซึ่งไม่มีผื่นที่หน้า
- Anti-CCP ใช้วินิจฉัย rheumatoid arthritis
- Anti-GBM ใช้ใน RPGN + ไอเป็นเลือด
- Serum IgA ใช้กับ IgAN ไม่อธิบาย malar rash
หมายเหตุ: complement level ก็ช่วยได้ แต่ไม่จำเพาะเท่า ANA ในการคัดกรอง SLE''',
            pearl="Nephrotic + malar rash → ANA ก่อน", topic="SLE screening",
            ref=[f"{D} หน้า 65, 107–108"], nl=["2.3.13-3(15)", "2.3.14(12)"]),
        mcq("NEPHRO-02-04-3",
            "A 28-year-old woman with SLE has new edema and hypertension. Cr 1.9 mg/dL, UPCR 3.2 g/g, urinalysis shows RBC casts. Serum C3 and C4 are low and anti-dsDNA is high. Kidney biopsy shows endocapillary proliferation involving 70% of glomeruli with subendothelial deposits. What is the most appropriate treatment?",
            "Corticosteroids plus mycophenolate mofetil or cyclophosphamide",
            ["ACE inhibitor alone", "Hydroxychloroquine alone", "Plasmapheresis alone", "Rituximab alone without steroid"],
            explain='''Proliferative lesion ≥ 50% ของ glomeruli = **lupus nephritis class IV (diffuse)** สไลด์: class III/IV → **steroid + immunosuppressant** (induction ด้วย MMF หรือ cyclophosphamide)
- ACEI ลด proteinuria เป็นการรักษาเสริม แต่ไม่พอสำหรับ class IV
- Hydroxychloroquine ควรให้ทุกราย แต่ไม่พอเดี่ยว ๆ
- Plasmapheresis เป็นการรักษาหลักของ anti-GBM ไม่ใช่ LN
- Rituximab อาจใช้ในรายดื้อยา ไม่ใช่ first-line เดี่ยว ๆ''',
            pearl="LN class III/IV = steroid + MMF/cyclophosphamide", topic="LN treatment",
            ref=[f"{D} หน้า 67–68"], nl=["2.3.13-3(15)"]),
    ])

# ---------------------------------------------------------------- 02-05 Anti-GBM & GPA
F_RPGN = fig("nephro-02-05-f1", "RPGN: แยกด้วย immunofluorescence + serology", '''<svg viewBox="0 0 740 300">
 <defs><marker id="nephro-02-05-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="50" rx="10" class="bad"/>
 <text x="370" y="32" text-anchor="middle" class="tw">RPGN (crescentic GN)</text>
 <text x="370" y="50" text-anchor="middle" class="tw">Cr ↑ ในสัปดาห์–เดือน</text>
 <path d="M300 60L130 98" class="ln" marker-end="url(#nephro-02-05-a)"/>
 <path d="M370 60V98" class="ln" marker-end="url(#nephro-02-05-a)"/>
 <path d="M440 60L610 98" class="ln" marker-end="url(#nephro-02-05-a)"/>
 <rect x="10" y="100" width="230" height="190" rx="10" class="c1soft"/>
 <text x="125" y="124" text-anchor="middle" class="tb">Anti-GBM</text>
 <text x="125" y="146" text-anchor="middle" class="ta">IF: linear IgG</text>
 <text x="22" y="174" class="t2">Anti-GBM Ab +</text>
 <text x="22" y="194" class="t2">C3, C4 ปกติ</text>
 <text x="22" y="214" class="t2">ไอเป็นเลือด (Goodpasture)</text>
 <text x="22" y="240" class="t3">Tx: plasmapheresis</text>
 <text x="22" y="258" class="t3">+ steroid + cyclophosphamide</text>
 <rect x="255" y="100" width="230" height="190" rx="10" class="c2soft"/>
 <text x="370" y="124" text-anchor="middle" class="tb">Immune complex</text>
 <text x="370" y="146" text-anchor="middle" class="ta">IF: granular</text>
 <text x="267" y="174" class="t2">LN (↓C3 ↓C4, ANA)</text>
 <text x="267" y="194" class="t2">APSGN (↓C3, ASO)</text>
 <text x="267" y="214" class="t2">MPGN (↓C3)</text>
 <text x="267" y="234" class="t2">IgAN (C3 ปกติ)</text>
 <text x="267" y="258" class="t3">Tx ตามโรค</text>
 <rect x="500" y="100" width="230" height="190" rx="10" class="misssoft"/>
 <text x="615" y="124" text-anchor="middle" class="tb">Pauci-immune</text>
 <text x="615" y="146" text-anchor="middle" class="ta">IF: ไม่มี/น้อยมาก</text>
 <text x="512" y="174" class="t2">ANCA + · C3, C4 ปกติ</text>
 <text x="512" y="194" class="t2">GPA: c-ANCA (PR3)</text>
 <text x="512" y="214" class="t2">MPA: p-ANCA (MPO)</text>
 <text x="512" y="234" class="t2">EGPA: asthma, eosinophil</text>
 <text x="512" y="258" class="t3">Tx: steroid + immunosuppressant</text>
</svg>''', "เมื่อได้ RPGN ให้แยกสามกลุ่มด้วยรูปแบบ immunofluorescence และ serology: linear = anti-GBM, granular = immune complex, ไม่มี deposit = ANCA")

S5 = sec("nephro-02-05", "Anti-GBM disease & GPA (pulmonary–renal syndrome)",
    "RPGN + ไอเป็นเลือด · anti-GBM = linear IgG, plasmapheresis · GPA = ไซนัส ปอด ไต c-ANCA · complement ปกติทั้งคู่", minutes=7,
    source=f"{D} หน้า 69–71, 109–110", nl=["2.3.14(2)", "2.3.13-3(16)"],
    md='''
ทั้งสองโรคมาด้วย **RPGN + pulmonary–renal syndrome** (ไอเป็นเลือด + ไตวายเร็ว) และ **C3, C4 ปกติ** — แยกกันด้วย serology และ IF

[[fig:nephro-02-05-f1]]

### Anti-GBM disease (Goodpasture syndrome)

- Antibody ต่อ type IV collagen (α3 chain) ของ basement membrane ทั้งใน glomerulus และ alveolus (เสริม) — สัมพันธ์กับการสูบบุหรี่/สารระเหย (เสริม)
- Present: **RPGN**
- **Pulmonary–renal syndrome**: pulmonary hemorrhage & **hemoptysis**, CXR pulmonary infiltrates
- ↑BUN, Cr · UA: RBC, dysmorphic RBC, RBC cast, proteinuria
- **Normal C3, C4**
- **Anti-GBM antibody positive**
- Bronchoalveolar lavage (เลือดออกในถุงลม), renal biopsy
- Biopsy: LM **crescent, necrosis** · IF **linear IgG deposition**
- Tx: **steroid + immunosuppressants + plasmapheresis** (เอา antibody ออก)

### Granulomatosis with polyangiitis (GPA)

- เดิมชื่อ Wegener granulomatosis · necrotizing granulomatous vasculitis ของหลอดเลือดเล็ก
- Present: **RPGN**
- **Upper airway**: rhinitis/sinusitis (น้ำมูกปนเลือด, saddle nose (เสริม))
- **Lung**: hemoptysis, CXR pulmonary **infiltrates/nodule (อาจมี cavity (เสริม))**
- ↑BUN, Cr · UA nephritic · **Normal C3, C4**
- **Positive c-ANCA (anti-PR3)**
- Kidney biopsy: **necrotizing crescentic GN** (pauci-immune)
- Tx: **steroid + immunosuppressants** (cyclophosphamide หรือ rituximab (เสริม))

| | Anti-GBM | GPA | MPA (เสริม) |
|---|---|---|---|
| ปอด | Alveolar hemorrhage | Nodule/cavity, hemorrhage | Hemorrhage |
| ไซนัส/จมูก | ไม่มี | **มี** | ไม่มี |
| Serology | Anti-GBM | **c-ANCA (PR3)** | p-ANCA (MPO) |
| IF | **Linear** IgG | Pauci-immune | Pauci-immune |
| Complement | ปกติ | ปกติ | ปกติ |
''',
    figs=[F_RPGN],
    pearls=[
        "Hemoptysis + RPGN + linear IgG = anti-GBM (Goodpasture) → plasmapheresis + steroid + IS",
        "Sinusitis + lung nodule + RPGN + c-ANCA = GPA",
        "Anti-GBM และ ANCA GN: C3, C4 ปกติ",
        "Crescent = RPGN · linear = anti-GBM · ไม่มี deposit = pauci-immune",
    ],
    items=[
        mcq("NEPHRO-02-05-1",
            "A 25-year-old man came to the emergency department because of bloody sputum for a few weeks. He has now developed significant hematuria and hypertension. Renal biopsy immunofluorescence shows a linear pattern. Which additional finding would be seen on the renal biopsy?",
            "Crescent formation",
            ["Spike formation", "Kimmelstiel–Wilson nodules", "Diffuse endocapillary proliferation", "Subepithelial immune deposits on electron microscopy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไอเป็นเลือด + hematuria + **IF linear** = **anti-GBM disease (Goodpasture)** ซึ่งมาเป็น RPGN และ LM พบ **crescent, necrosis**
- Spike formation (spike and dome) เป็นของ membranous nephropathy
- Kimmelstiel–Wilson nodule เป็นของ diabetic nephropathy
- Diffuse endocapillary proliferation เป็นของ APSGN
- Subepithelial deposit (humps) บน EM เป็นของ APSGN/MN — anti-GBM ไม่มี immune complex deposit''',
            pearl="Linear IF + hemoptysis = anti-GBM → crescent", topic="Anti-GBM pathology",
            ref=[f"{D} หน้า 69–70, 109–110"], nl=["2.3.14(2)"]),
        mcq("NEPHRO-02-05-2",
            "A 48-year-old man has chronic bloody nasal discharge and sinusitis for 3 months, then cough with hemoptysis. Cr rose from 1.0 to 3.6 mg/dL over 4 weeks. Urinalysis: dysmorphic RBC, RBC casts, protein 2+. CXR shows multiple bilateral nodules, some cavitating. C3 and C4 are normal. Which test is most likely to be positive?",
            "c-ANCA (anti-proteinase 3)",
            ["Anti-GBM antibody", "Anti-dsDNA", "Antistreptolysin O", "Cryoglobulin"],
            explain='''Upper airway (sinusitis, เลือดกำเดา) + ปอด (nodule มี cavity) + ไต (RPGN) + complement ปกติ = **GPA** ซึ่งพบ **c-ANCA (PR3)**
- Anti-GBM ทำ pulmonary–renal ได้ แต่ไม่มี sinusitis และไม่ทำ nodule/cavity
- Anti-dsDNA เป็นของ SLE ซึ่ง complement จะต่ำ
- ASO สัมพันธ์กับ APSGN (C3 ต่ำ ไม่มีอาการปอด)
- Cryoglobulin สัมพันธ์กับ HCV/MPGN และ complement มักต่ำ''',
            pearl="Sinus + lung nodule + kidney = GPA → c-ANCA", topic="GPA",
            ref=[f"{D} หน้า 71"], nl=["2.3.13-3(16)"]),
        mcq("NEPHRO-02-05-3",
            "A 30-year-old smoker presents with hemoptysis and acute kidney injury. Cr 5.2 mg/dL, urinalysis shows RBC casts. CXR shows bilateral alveolar infiltrates. Anti-GBM antibody is strongly positive; ANCA is negative. In addition to high-dose corticosteroids and cyclophosphamide, which treatment is most appropriate?",
            "Plasmapheresis",
            ["Intravenous immunoglobulin", "Hydroxychloroquine", "Penicillin V", "ACE inhibitor alone"],
            explain='''Anti-GBM disease ต้องเอา antibody ที่ไหลเวียนออกเร็วที่สุด → **plasmapheresis** ร่วมกับ steroid + immunosuppressant (ตามสไลด์)
- IVIG ไม่ใช่การรักษามาตรฐานของ anti-GBM
- Hydroxychloroquine ใช้ใน SLE
- Penicillin ใช้กำจัดเชื้อใน APSGN
- ACEI อย่างเดียวไม่หยุดการทำลายจาก antibody''',
            pearl="Anti-GBM → plasmapheresis + steroid + cyclophosphamide", topic="Anti-GBM treatment",
            ref=[f"{D} หน้า 69"], nl=["2.3.14(2)"]),
    ])

# ---------------------------------------------------------------- 02-06 MPGN + complement/Ix
F_C3 = fig("nephro-02-06-f1", "Complement level ช่วย guide โรค", '''<svg viewBox="0 0 740 260">
 <defs><marker id="nephro-02-06-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="40" rx="10" class="acsoft"/>
 <text x="370" y="35" text-anchor="middle" class="tb">Nephritic syndrome → C3, C4</text>
 <path d="M310 50L130 88" class="ln" marker-end="url(#nephro-02-06-a)"/>
 <path d="M370 50V88" class="ln" marker-end="url(#nephro-02-06-a)"/>
 <path d="M430 50L610 88" class="ln" marker-end="url(#nephro-02-06-a)"/>
 <rect x="10" y="90" width="230" height="40" rx="10" class="bad"/>
 <text x="125" y="115" text-anchor="middle" class="tw">↓C3, ↓C4</text>
 <rect x="255" y="90" width="230" height="40" rx="10" class="miss"/>
 <text x="370" y="115" text-anchor="middle" class="tw">↓C3, C4 ปกติ</text>
 <rect x="500" y="90" width="230" height="40" rx="10" class="ok"/>
 <text x="615" y="115" text-anchor="middle" class="tw">C3, C4 ปกติ</text>
 <rect x="10" y="140" width="230" height="110" rx="10" class="badsoft"/>
 <text x="125" y="164" text-anchor="middle" class="tb">Lupus nephritis</text>
 <text x="125" y="184" text-anchor="middle" class="t3">ANA, anti-dsDNA</text>
 <text x="125" y="210" text-anchor="middle" class="t2">(MPGN จาก</text>
 <text x="125" y="228" text-anchor="middle" class="t2">cryoglobulin/HCV)</text>
 <rect x="255" y="140" width="230" height="110" rx="10" class="misssoft"/>
 <text x="370" y="164" text-anchor="middle" class="tb">APSGN</text>
 <text x="370" y="184" text-anchor="middle" class="t3">ASO, anti-DNase B</text>
 <text x="370" y="210" text-anchor="middle" class="tb">MPGN</text>
 <text x="370" y="230" text-anchor="middle" class="t3">HBV, HCV, autoimmune</text>
 <rect x="500" y="140" width="230" height="110" rx="10" class="oksoft"/>
 <text x="615" y="164" text-anchor="middle" class="tb">IgA nephropathy</text>
 <text x="615" y="186" text-anchor="middle" class="tb">Anti-GBM</text>
 <text x="615" y="204" text-anchor="middle" class="t3">anti-GBM Ab</text>
 <text x="615" y="226" text-anchor="middle" class="tb">Pauci-immune (ANCA)</text>
 <text x="615" y="244" text-anchor="middle" class="t3">ANCA</text>
</svg>''', "ส่ง C3/C4 ก่อน แล้วแยกสามกลุ่ม จากนั้นเลือก serology ที่ตรงกับกลุ่มนั้น (ตัวเล็กใต้ชื่อโรค)")

S6 = sec("nephro-02-06", "MPGN & การส่งตรวจ nephritic syndrome",
    "MPGN: ↓C3 · tram-track · มักมี secondary cause (HBV, HCV) · ใช้ complement guide serology และ biopsy", minutes=7,
    source=f"{D} หน้า 72–74, 111–112", nl=["2.3.14(2)", "2.3.14(12)"],
    md='''
### Membranoproliferative GN (MPGN)

- Present ได้ทุกแบบ: acute GN, chronic GN, RPGN, nephrotic, **nephritic–nephrotic syndrome**
- **Primary** (ส่วนใหญ่ในเด็ก) · **Secondary**: infection (**HBV, HCV** — cryoglobulinemia), autoimmune, malignancy, drugs
- ↑BUN, Cr · UA: nephritic/nephrotic sediment
- **↓C3, ↔/↓C4**
- Kidney biopsy: **double-contour "tram-track" ของ GBM**, **subendothelial deposits**
- Tx: steroid, immunosuppressants (และรักษาสาเหตุ เช่น antiviral ใน HCV (เสริม))

> MPGN ส่วนใหญ่มักมี secondary cause — ผู้ใหญ่ที่เป็น MPGN ต้องตรวจ HBsAg, anti-HCV, cryoglobulin (เสริม)

### Investigation ของ nephritic syndrome (ตามสไลด์)

- BUN, Cr
- UA: RBC, dysmorphic RBC, RBC cast, proteinuria
- UPCR/24-hr urine protein
- CBC
- **C3, C4 complement level** (ใช้ guide โรค)
- Further Ix ตามที่สงสัย
- **Renal biopsy** (definitive dx, prognosis, F/U) — ยกเว้นบางกรณีไม่จำเป็น เช่น **typical APSGN**, no specific tx

[[fig:nephro-02-06-f1]]

| Complement | โรค | Serology ต่อ |
|---|---|---|
| **↓C3, ↓C4** | Lupus nephritis | ANA, anti-dsDNA |
| **↓C3, C4 ปกติ** | APSGN (MPGN) | ASO, anti-DNase B |
| **C3, C4 ปกติ** | IgAN, anti-GBM, pauci-immune GN | (serum IgA), anti-GBM, ANCA |

### การรักษา nephritic syndrome ทั่วไป (supportive)

- จำกัดเกลือ/น้ำ + **loop diuretic (furosemide)** เมื่อบวม/ความดันสูงจาก volume overload
- ยาความดัน · รักษาโรคต้นเหตุตาม biopsy
''',
    figs=[F_C3],
    pearls=[
        "MPGN = ↓C3 + tram-track GBM + subendothelial deposit · หาสาเหตุ HBV/HCV",
        "↓C3↓C4 = LN · ↓C3 C4 ปกติ = APSGN (MPGN) · ปกติ = IgAN, anti-GBM, ANCA",
        "Typical APSGN ไม่ต้อง biopsy",
        "Nephritic + volume overload/HT → จำกัดเกลือน้ำ + furosemide",
    ],
    items=[
        mcq("NEPHRO-02-06-1",
            "A 42-year-old man with chronic hepatitis C presents with edema, hypertension, palpable purpura, and arthralgia. Urinalysis: RBC casts, protein 3.8 g/day. C3 is low and C4 is low. Rheumatoid factor is positive. Kidney biopsy shows thickened capillary walls with a double-contour (tram-track) appearance and subendothelial deposits. What is the diagnosis?",
            "Membranoproliferative glomerulonephritis",
            ["Membranous nephropathy", "IgA vasculitis", "Focal segmental glomerulosclerosis", "Anti-GBM disease"],
            explain='''HCV + cryoglobulinemia (purpura, arthralgia, RF +) + mixed nephritic–nephrotic + complement ต่ำ + **tram-track + subendothelial deposit** = **MPGN** (secondary จาก HCV)
- Membranous nephropathy ก็สัมพันธ์กับ HBV/HCV ได้ แต่เป็น nephrotic ล้วน มี spike (subepithelial) ไม่ใช่ tram-track และ complement ปกติ
- IgA vasculitis มี purpura เหมือนกัน แต่ complement ปกติ และพยาธิสภาพอยู่ที่ mesangium
- FSGS เป็น nephrotic มี segmental sclerosis
- Anti-GBM เป็น linear IgG และ complement ปกติ''',
            pearl="HCV + cryoglobulin + low C3 + tram-track = MPGN", topic="MPGN",
            ref=[f"{D} หน้า 72"], nl=["2.3.14(2)", "2.3.14(12)"]),
        mcq("NEPHRO-02-06-2",
            "A 20-year-old man presents with dark urine for 2 days. BP 140/100 mmHg, mild periorbital edema. Urinalysis: RBC > 100/HPF, WBC 10/HPF, RBC casts, protein 1+. Cr is mildly elevated. What is the most appropriate initial management?",
            "Furosemide with salt and fluid restriction",
            ["Norfloxacin", "Ceftriaxone", "High-dose prednisolone", "Intravenous sodium nitroprusside"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''RBC cast + ความดันสูง + บวม = nephritic syndrome ความดันสูงที่นี่เกิดจาก **Na และน้ำคั่ง** การรักษาเบื้องต้นแบบ supportive คือ **จำกัดเกลือ/น้ำ + loop diuretic (furosemide)** ระหว่างหาสาเหตุ (หมายเหตุ: สไลด์ไม่ได้แสดงเฉลย ข้อนี้ตอบตามหลักการรักษาในสไลด์ APSGN)
- Norfloxacin และ ceftriaxone ใช้รักษา UTI แต่ RBC cast บอกว่าเป็นโรค glomerulus ไม่ใช่การติดเชื้อ
- Prednisolone ไม่ควรให้ก่อนรู้สาเหตุ (เช่น APSGN ไม่ตอบสนองต่อ steroid)
- Sodium nitroprusside ใช้เมื่อเป็น hypertensive emergency (มี encephalopathy) แต่ BP 140/100 ไม่มีอาการ''',
            pearl="Nephritic + HT/edema → จำกัดเกลือน้ำ + furosemide", topic="Nephritic supportive care",
            ref=[f"{D} หน้า 60, 111–112"], nl=["2.3.14(2)"]),
        mcq("NEPHRO-02-06-3",
            "A 12-year-old girl develops facial edema, hypertension, and cola-colored urine 2 weeks after a streptococcal sore throat. C3 is low, C4 normal, ASO high. She improves with supportive care. In which situation would a renal biopsy be indicated?",
            "C3 remains low and proteinuria persists 3 months later",
            ["The ASO titer is 1:800", "Gross hematuria lasts for 5 days", "Blood pressure is 140/90 mmHg on admission", "Edema requires furosemide"],
            explain='''APSGN แบบ typical ไม่ต้อง biopsy สไลด์ให้ทำเมื่อ **RPGN หรือ atypical** เช่น **C3 ยังต่ำเกิน 6–8 สัปดาห์** หรือ proteinuria/ไตวายไม่ดีขึ้น ซึ่งต้องคิดถึง **MPGN หรือ lupus** แทน (เสริม: เกณฑ์ 8 สัปดาห์)
- ASO สูงมากยิ่งสนับสนุน APSGN ไม่ใช่ข้อบ่งชี้ biopsy
- Gross hematuria ไม่กี่วันพบได้ใน APSGN
- ความดันสูงและบวมที่ต้องใช้ furosemide เป็นภาพปกติของ APSGN''',
            pearl="APSGN ที่ C3 ต่ำนาน > 8 สัปดาห์ = atypical → biopsy (MPGN/LN)", topic="When to biopsy",
            ref=[f"{D} หน้า 58, 73"], nl=["B9.2.2(3)"]),
    ])

LECTURE = lecture("02", "Nephritic syndrome", "APSGN · IgAN/HSP · lupus · anti-GBM · GPA · MPGN",
    objectives=[
        "แยก 5 glomerular syndromes และ nephritic vs nephrotic จากอาการ + UA ได้",
        "ใช้ระยะแฝงหลังติดเชื้อ + complement แยก APSGN, IgAN, LN, MPGN ได้",
        "จำ biopsy pattern ที่ข้อสอบชอบ (endocapillary, mesangial IgA, linear, crescent, tram-track) ได้",
        "เลือก serology และการรักษาเฉพาะโรคของ RPGN ได้",
    ],
    sections=[S1, S2, S3, S4, S5, S6])
