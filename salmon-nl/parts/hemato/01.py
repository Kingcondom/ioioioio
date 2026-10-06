from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Hemato"

# ---------------------------------------------------------------- 01-01 Approach to anemia
F_APP = fig("hemato-01-01-f1", "Approach to anemia ด้วย MCV + reticulocyte", '''<svg viewBox="0 0 740 400">
 <defs><marker id="hemato-01-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="44" rx="10" class="acsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">Anemia → ดู MCV</text>
 <text x="370" y="46" text-anchor="middle" class="t3">ชาย Hb &lt; 13 · หญิง &lt; 12 g/dL</text>
 <path d="M300 54L130 88" class="ln" marker-end="url(#hemato-01-01-a)"/>
 <path d="M370 54V88" class="ln" marker-end="url(#hemato-01-01-a)"/>
 <path d="M440 54L612 88" class="ln" marker-end="url(#hemato-01-01-a)"/>
 <rect x="20" y="90" width="220" height="38" rx="10" class="c1"/>
 <text x="130" y="114" text-anchor="middle" class="tw">MCV &lt; 80 (microcytic)</text>
 <rect x="260" y="90" width="220" height="38" rx="10" class="ac"/>
 <text x="370" y="114" text-anchor="middle" class="tw">MCV 80–100 (normocytic)</text>
 <rect x="500" y="90" width="220" height="38" rx="10" class="c2"/>
 <text x="610" y="114" text-anchor="middle" class="tw">MCV &gt; 100 (macrocytic)</text>
 <rect x="20" y="140" width="220" height="130" rx="10" class="c1soft"/>
 <text x="34" y="164" class="tb">IDA</text>
 <text x="34" y="186" class="tb">Thalassemia</text>
 <text x="34" y="208" class="t2">ACD (ระยะหลัง)</text>
 <text x="34" y="230" class="t2">Lead poisoning</text>
 <text x="34" y="256" class="t3">→ ferritin / iron study / Hb typing</text>
 <path d="M370 128V148" class="ln" marker-end="url(#hemato-01-01-a)"/>
 <rect x="285" y="150" width="170" height="32" rx="8" class="box"/>
 <text x="370" y="171" text-anchor="middle" class="tb">Reticulocyte (cRC)</text>
 <path d="M330 182L318 210" class="ln" marker-end="url(#hemato-01-01-a)"/>
 <path d="M410 182L422 210" class="ln" marker-end="url(#hemato-01-01-a)"/>
 <rect x="252" y="212" width="116" height="118" rx="10" class="misssoft"/>
 <text x="310" y="232" text-anchor="middle" class="tb">&lt; 2%</text>
 <text x="310" y="252" text-anchor="middle" class="t3">ACD (ระยะแรก)</text>
 <text x="310" y="270" text-anchor="middle" class="t3">CKD · ตับ</text>
 <text x="310" y="288" text-anchor="middle" class="t3">ต่อมไร้ท่อ</text>
 <text x="310" y="306" text-anchor="middle" class="t3">BM disease</text>
 <rect x="374" y="212" width="116" height="118" rx="10" class="badsoft"/>
 <text x="432" y="232" text-anchor="middle" class="tb">&gt; 2%</text>
 <text x="432" y="252" text-anchor="middle" class="t3">Blood loss</text>
 <text x="432" y="270" text-anchor="middle" class="t3">Hemolysis</text>
 <text x="432" y="294" text-anchor="middle" class="t3">→ LDH, bilirubin</text>
 <text x="432" y="312" text-anchor="middle" class="t3">haptoglobin, DAT</text>
 <rect x="500" y="140" width="220" height="130" rx="10" class="c2soft"/>
 <text x="514" y="162" class="tb">MCV &gt; 110 มักเป็น</text>
 <text x="514" y="182" class="t2">Megaloblastic (B12/folate)</text>
 <text x="514" y="200" class="t2">RBC agglutination (cold AIHA)</text>
 <text x="514" y="224" class="tb">MCV 100–110</text>
 <text x="514" y="244" class="t2">Reticulocytosis · ตับ</text>
 <text x="514" y="262" class="t2">Hypothyroid · alcohol</text>
 <rect x="20" y="344" width="700" height="46" rx="10" class="sunk"/>
 <text x="370" y="364" text-anchor="middle" class="t2">Corrected RC = RC × (Hct ผู้ป่วย ÷ 45) · ปกติ 0.5–2.5%</text>
 <text x="370" y="382" text-anchor="middle" class="t3">retic ขึ้น = ไขกระดูกตอบสนอง (เสียเลือดเฉียบพลัน, hemolysis, กำลังฟื้นจากการรักษา IDA/B12/folate)</text>
</svg>''', "เริ่มจาก MCV แบ่งสามกลุ่ม แล้วในกลุ่ม normocytic ใช้ corrected reticulocyte แยกไขกระดูกสร้างไม่พอ (< 2%) กับเสีย/แตก (> 2%)")

S1 = sec("hemato-01-01", "Anemia: definition, CBC & approach",
    "นิยาม anemia ตามอายุ/ครรภ์ · ค่าปกติ CBC · corrected reticulocyte · แบ่งตาม MCV และ retic", minutes=7,
    source=f"{D} หน้า 6–11", nl=["2.1.56", "3.3.2", "3.3.3"],
    md='''
### นิยาม anemia (WHO)

| กลุ่ม | Hb ต่ำกว่า (g/dL) |
|---|---|
| ชาย | **13** |
| หญิง (ไม่ตั้งครรภ์) | **12** |
| เด็ก 6 เดือน–5 ปี | 11 |
| เด็ก 5–11 ปี | 11.5 |
| เด็ก 12–14 ปี | 12 |
| ตั้งครรภ์ไตรมาส 1 / 2 / 3 | **11 / 10.5 / 11** |

### ค่าปกติที่ต้องจำ

| ค่า | ปกติ |
|---|---|
| MCV | 80–100 fL |
| RDW | 12–15% |
| WBC | 4,000–11,000/µL (N 40–60%, L 20–40%, M 2–8%, E 1–4%, B 0.5–1%) |
| Platelet | 150,000–450,000/µL |
| Reticulocyte | 0.5–2.5% |

### Reticulocyte = polychromasia

- **Polychromasia** ใน Wright stain (เม็ดเลือดแดงสีม่วงอมฟ้า ตัวใหญ่) คือ **reticulocyte** ที่เห็นชัดใน supravital stain
- ขึ้นเมื่อ **ไขกระดูกตอบสนอง**: hemolytic anemia, acute hemorrhage, ระยะฟื้นตัวหลังให้ B12/folate/iron
- ถ้าซีดมาก retic % จะสูงเกินจริง → ต้อง **corrected reticulocyte count (cRC) = RC × (Hct ÷ 45)**
- ตัวอย่างในสไลด์: Hct 22%, RC 3% → cRC = 3 × 22/45 = **1.5%** (จริง ๆ แล้วไขกระดูกตอบสนองไม่พอ)

### แบ่งสาเหตุตามระยะเวลา

- **Acute**: blood loss, hemolysis, dilution
- **Chronic**: hemolysis หรือ **underproductive** (nutritional, ACD, CKD/ตับ/ต่อมไร้ท่อ, BM disease)
- Hemolysis แบ่ง intrinsic/extrinsic ต่อ RBC (ดูหมวด hemolytic anemia)

[[fig:hemato-01-01-f1]]

> MCV สูงมาก (> 110) อย่าเพิ่งฟันว่า megaloblastic — ต้องดู PBS เพราะ **RBC agglutination** (AIHA โดยเฉพาะ cold type) ทำให้เครื่องอ่าน MCV สูงเกินจริงได้
''',
    figs=[F_APP],
    pearls=[
        "Anemia: ชาย Hb <13 · หญิง <12 · ครรภ์ไตรมาส 2 <10.5",
        "Polychromasia = reticulocyte → บอกว่าไขกระดูกตอบสนอง",
        "cRC = RC × Hct/45 · <2% = สร้างไม่พอ · >2% = เสียเลือด/แตก",
        "MCV <80: IDA, thal, ACD ระยะหลัง, lead · MCV >110: megaloblastic หรือ RBC agglutination",
    ],
    items=[
        mcq_ordered("HEMATO-01-01-1",
            "A 30-year-old woman has fatigue. CBC: Hb 7.3 g/dL, Hct 22%, MCV 88 fL. The laboratory reports a reticulocyte count of 3%. What is her corrected reticulocyte count?",
            ["0.7%", "1.5%", "2.2%", "3.0%", "6.1%"], 1,
            explain='''Corrected RC = RC × (Hct ÷ 45) = 3 × (22 ÷ 45) ≈ **1.5%** ตรงกับตัวอย่างในสไลด์ — แปลว่าแท้จริงไขกระดูก **ตอบสนองไม่พอ** (< 2%) แม้ตัวเลขดิบดูสูง
- 0.7% ได้จากการหารซ้ำสองรอบ (คิด maturation time ซ้อน) ไม่ใช่สูตรในสไลด์
- 2.2% และ 3.0% ไม่ได้ปรับ หรือปรับด้วยค่า Hct อ้างอิงผิด
- 6.1% คือคูณกลับด้าน (45/22) ทำให้ดูเหมือนตอบสนองดีเกินจริง''',
            pearl="cRC = RC × Hct/45", topic="Corrected reticulocyte",
            ref=[f"{D} หน้า 9"], nl=["3.3.3"]),
        mcq("HEMATO-01-01-2",
            "A 24-year-old woman at 24 weeks of gestation has a routine antenatal CBC. Which hemoglobin level is the threshold below which she is defined as anemic?",
            "10.5 g/dL",
            ["11.5 g/dL", "12 g/dL", "13 g/dL", "9 g/dL"],
            explain='''GA 24 สัปดาห์ = **ไตรมาสที่ 2** เกณฑ์ anemia คือ **Hb < 10.5 g/dL** (ไตรมาส 1 และ 3 ใช้ < 11) เพราะช่วงกลางครรภ์ plasma volume เพิ่มมากกว่า red cell mass (dilution) สูงสุด
- 11.5 g/dL เป็นเกณฑ์ของเด็ก 5–11 ปี
- 12 g/dL เป็นเกณฑ์หญิงไม่ตั้งครรภ์ (และเด็ก 12–14 ปี)
- 13 g/dL เป็นเกณฑ์ผู้ชาย
- 9 g/dL ไม่ใช่เกณฑ์นิยาม (ใช้แบ่งความรุนแรงบางระบบ)''',
            pearl="ครรภ์: T1 และ T3 <11, T2 <10.5", topic="Anemia definition",
            ref=[f"{D} หน้า 6"], nl=["2.1.56"]),
        mcq("HEMATO-01-01-3",
            "A 52-year-old man has fatigue for 2 months. He has no jaundice. CBC: Hb 8.5 g/dL, Hct 26%, MCV 90 fL, RDW 14%, WBC 6,500/µL, platelet 230,000/µL. Corrected reticulocyte count is 0.6%. Serum creatinine is 5.8 mg/dL. Which mechanism best explains his anemia?",
            "Decreased red cell production",
            ["Intravascular hemolysis", "Acute blood loss", "Impaired DNA synthesis", "Defective globin chain synthesis"],
            explain='''Normocytic anemia + **cRC < 2%** = ไขกระดูกสร้างไม่พอ (underproductive) — สาเหตุในสไลด์ได้แก่ ACD ระยะแรก, **renal failure** (ขาด EPO), โรคตับ, ต่อมไร้ท่อ และ BM disease · Cr 5.8 จึงเข้ากับ anemia of CKD
- Intravascular hemolysis และ acute blood loss ต้องมี retic สูง (> 2%) และ hemolysis มีตัวเหลือง LDH สูง
- Impaired DNA synthesis (megaloblastic) ให้ MCV > 100 มักมี hypersegmented neutrophil
- Defective globin synthesis (thalassemia) ให้ microcytic MCV < 80''',
            pearl="Normocytic + retic ต่ำ = underproductive (CKD, ACD, BM)", topic="Approach to normocytic anemia",
            ref=[f"{D} หน้า 10–11"], nl=["2.1.56", "3.3.3"]),
        mcq("HEMATO-01-01-4",
            "A 45-year-old woman has anemia and mild jaundice after cold exposure, with acrocyanosis of the fingers. The automated CBC reports Hb 8 g/dL and MCV 128 fL. What is the most appropriate next step to interpret the high MCV?",
            "Review the peripheral blood smear",
            ["Measure serum vitamin B12", "Start oral folic acid", "Bone marrow aspiration", "Thyroid function test"],
            explain='''MCV สูงมาก (> 110) มีสองสาเหตุหลักคือ megaloblastic และ **RBC agglutination** — ผู้ป่วยรายนี้มีอาการหลังโดนความเย็นและ acrocyanosis ชวนนึกถึง **cold AIHA** ที่ RBC จับกลุ่มกันจนเครื่องอ่านเป็นเซลล์ใหญ่ ต้อง **ดู PBS** ยืนยัน agglutination ก่อน
- Serum B12 และการให้ folic acid เหมาะเมื่อ PBS เป็น macro-ovalocyte + hypersegmented neutrophil ไม่ใช่ขั้นแรกในเคสที่ชวนนึกถึง agglutination
- Bone marrow aspiration ยังไม่จำเป็น เพราะ PBS + DAT น่าจะตอบได้
- Thyroid function ทำให้ MCV สูงเล็กน้อย (100–110) ไม่อธิบาย 128 และ acrocyanosis''',
            pearl="MCV >110 ต้องดู PBS เสมอ (agglutination vs megaloblastic)", topic="Macrocytosis",
            ref=[f"{D} หน้า 11, 28"], nl=["3.1.2", "3.3.2"]),
    ])

# ---------------------------------------------------------------- 01-02 IDA
S2 = sec("hemato-01-02", "Iron deficiency anemia (IDA)",
    "เสียเลือดเรื้อรังเป็นหลัก · ↓MCV ↑RDW ↑Plt · ferritin < 30 · ชาย/วัยหมดประจำเดือนต้องส่อง GI · retic ขึ้นก่อนใน 3–5 วัน", minutes=8,
    source=f"{D} หน้า 12–24", nl=["2.3.3(7)", "3.3.26", "B2.4(2)"],
    md='''
### สาเหตุ

- **Blood loss** (พบบ่อยสุด): ประจำเดือนมาก, GI bleeding, PNH (เสียเหล็กทางปัสสาวะ)
- **Poor intake / ↓absorption**: gastrectomy, IBD
- **↑Demand**: ตั้งครรภ์ ให้นมบุตร

### อาการและตรวจร่างกาย

- อาการซีดทั่วไป + **pica** (อยากกินของแปลก เช่น น้ำแข็ง ดิน)
- Glossitis, angular stomatitis, **koilonychia** (เล็บช้อน) เล็บเปราะ
- Esophageal web (Plummer–Vinson)

### การตรวจ

| การตรวจ | IDA |
|---|---|
| CBC | ↓Hb, **↓MCV, ↑RDW**, **↑platelet** (reactive) |
| PBS | Hypochromic microcytic, **pencil cell** · aniso/poikilocytosis ไม่เด่นมาก |
| Serum iron | ↓ |
| TIBC | **↑** |
| Transferrin saturation | ↓ |
| Ferritin | **↓ (< 30 ng/mL)** — ตัวที่ไวและจำเพาะที่สุด |

> ซีด microcytic + **platelet สูง** + RDW สูง ในหญิงวัยเจริญพันธุ์ = IDA จนกว่าจะพิสูจน์ได้ว่าไม่ใช่ → ตรวจ **serum ferritin**

### การรักษา

- **Iron replacement** เช่น ferrous sulfate รับประทาน (เสริม: ธาตุเหล็ก 60–65 mg ต่อเม็ด 300–325 mg วันละครั้ง ให้ต่อ 3 เดือนหลัง Hb ปกติ เพื่อเติม store)
- **หาสาเหตุเสมอ**
  - หญิงวัยเจริญพันธุ์ → ซักประวัติประจำเดือนมาก
  - **ชาย หรือหญิงวัยหมดประจำเดือน → colonoscopy ร่วมกับ EGD** (R/O GI bleeding/มะเร็ง) แม้ stool occult blood ลบ

### การตอบสนองต่อการรักษา (ออกสอบบ่อย)

| เวลา | สิ่งที่ดีขึ้น |
|---|---|
| 1–2 วัน | อาการ (รู้สึกดีขึ้น) |
| **3–5 วัน** | **Reticulocyte ↑ (ค่าแรกที่ขึ้น)** |
| 3 สัปดาห์ | Hb ↑ (ราว 1–2 g/dL ต่อ 3 สัปดาห์) |
| 1–3 เดือน | Ferritin ↑ (store เต็ม) |

> ข้อสอบเก่า: ผู้ป่วย cirrhosis ซีด MCV 70, retic 1%, platelet 400,000 → ไม่ใช่ hypersplenism (จะได้ platelet ต่ำ) แต่เป็น **IDA** จากเสียเลือดทาง GI
''',
    pearls=[
        "IDA: ↓MCV ↑RDW ↑Plt · ↓Fe ↑TIBC ↓TSAT · ferritin <30",
        "ชาย/วัยหมดประจำเดือนที่เป็น IDA → colonoscopy + EGD",
        "หลังให้เหล็ก: retic ขึ้น 3–5 วัน → Hb 3 สัปดาห์ → ferritin 1–3 เดือน",
        "Pencil cell, koilonychia, pica, esophageal web = IDA",
    ],
    items=[
        mcq("HEMATO-01-02-1",
            "A 60-year-old man with alcoholic liver cirrhosis has had pallor and fatigue for 1 month. PE: moderate pallor, mild jaundice, spider nevi, palmar erythema, spleen 2 cm below the left costal margin. CBC: Hb 6 g/dL, Hct 18%, MCV 70 fL, WBC 6,000/µL, platelet 400,000/µL. Reticulocyte count 1%. What is the most likely cause of his anemia?",
            "Iron deficiency anemia",
            ["Hypersplenism", "Thalassemia", "Folate deficiency", "Chronic myeloproliferative disease"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''**Microcytic (MCV 70) + retic ปกติ/ต่ำ (ไม่มี BM response) + platelet สูง (reactive)** = IDA — ในผู้ป่วย cirrhosis มักเสียเลือดเรื้อรังทาง GI (portal hypertensive gastropathy, varices)
- Hypersplenism จะทำให้ **platelet และ WBC ต่ำ** ไม่ใช่ 400,000
- Thalassemia ก็ microcytic แต่ไม่อธิบาย platelet สูง และมักมีประวัติตั้งแต่เด็ก
- Folate deficiency (พบบ่อยในคนติดเหล้า) ให้ **macrocytic** ไม่ใช่ MCV 70
- Chronic MPN จะมี WBC/platelet สูงมากและม้ามโตมาก ไม่ใช่ microcytic anemia เป็นหลัก''',
            pearl="Microcytic + platelet สูง + retic ไม่ขึ้น = IDA", topic="IDA diagnosis",
            ref=[f"{D} หน้า 15–16"], nl=["2.3.3(7)"]),
        mcq("HEMATO-01-02-2",
            "A 40-year-old Thai woman presents with dyspnea on exertion. PE: pale conjunctivae, anicteric sclerae. CBC: Hb 7.5 g/dL, Hct 24%, MCV 55 fL, RDW 21%, WBC 7,500/µL (PMN 70%), platelet 550,000/µL. PBS: hypochromic microcytic RBC with pencil cells. What is the most appropriate investigation?",
            "Serum ferritin",
            ["Hemoglobin typing", "Direct antiglobulin test", "Bone marrow biopsy", "Serum haptoglobin"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''หญิงวัยเจริญพันธุ์ ซีด **hypochromic microcytic + RDW สูง + platelet สูง + pencil cell** ไม่เหลือง = ภาพ IDA → ตรวจยืนยันด้วย **serum ferritin** (< 30 ng/mL)
- Hemoglobin typing ใช้เมื่อสงสัย thalassemia (RDW มักไม่สูงมากใน trait, platelet ไม่สูง, target cell เด่น) และควร R/O IDA ก่อนเพราะ IDA ทำให้ HbA2 ต่ำลงแปลผลผิด
- Direct antiglobulin test และ haptoglobin ใช้เมื่อสงสัย hemolysis — ผู้ป่วยไม่มีตัวเหลือง
- Bone marrow biopsy ไม่จำเป็น เป็นหัตถการ invasive ทั้งที่ ferritin ตอบได้''',
            pearl="Microcytic + Plt สูง + pencil cell → serum ferritin", topic="IDA investigation",
            ref=[f"{D} หน้า 19–20"], nl=["3.3.26"]),
        mcq("HEMATO-01-02-3",
            "A 40-year-old woman with menorrhagia has fatigue. CBC: Hb 7 g/dL, Hct 21%, MCV 70 fL, WBC 7,500/µL, platelet 180,000/µL. Serum ferritin is 6 ng/mL. She is started on oral ferrous sulfate. Which parameter is expected to increase first?",
            "Reticulocyte count",
            ["Hemoglobin level", "MCV", "Serum ferritin", "Transferrin saturation"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ลำดับการตอบสนองต่อเหล็กตามสไลด์: อาการดีขึ้น 1–2 วัน → **reticulocyte ขึ้นใน 3–5 วัน (สูงสุดราววันที่ 7–10)** → Hb ขึ้นชัดใน 3 สัปดาห์ → ferritin ขึ้นใน 1–3 เดือน
- Hemoglobin ขึ้นช้ากว่า retic (สัปดาห์)
- MCV ค่อย ๆ ปกติตามการแทนที่เม็ดเลือดแดงเก่า ใช้เวลาหลายสัปดาห์
- Serum ferritin เป็นค่าสุดท้ายที่ขึ้น (store เต็ม) 1–3 เดือน
- Transferrin saturation ขึ้นชั่วคราวหลังกินยาแต่ไม่ใช่ตัวชี้วัดการตอบสนองที่สไลด์สอน''',
            pearl="ให้เหล็กแล้ว retic ขึ้นก่อน (3–5 วัน)", topic="Response to iron",
            ref=[f"{D} หน้า 14, 23–24"], nl=["2.3.3(7)", "3.3.3"]),
        mcq("HEMATO-01-02-4",
            "A 62-year-old man has fatigue for 3 months. He has no overt bleeding. CBC: Hb 8.8 g/dL, Hct 27%, MCV 70 fL, RDW 19%, platelet 470,000/µL. Serum ferritin is 8 ng/mL. A guaiac-based fecal occult blood test is negative. What is the most appropriate next step?",
            "Colonoscopy and esophagogastroduodenoscopy",
            ["Repeat fecal occult blood test for 3 days", "Oral iron and recheck CBC in 3 months without further work-up", "Hemoglobin typing", "Bone marrow aspiration"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เรียบเรียงใหม่: เพิ่มค่า ferritin ให้ยืนยัน IDA)",
            explain='''ชายสูงอายุเป็น **IDA ยืนยันแล้ว (ferritin 8)** สาเหตุที่ต้องนึกถึงก่อนคือ **GI blood loss รวมถึงมะเร็งลำไส้** → ตามสไลด์ "postmenopause/male → **colonoscopy with EGD**" แม้ stool occult blood ลบ เพราะเลือดออกเป็นพัก ๆ และ guaiac มี false negative สูง
- ตรวจ occult blood ซ้ำ 3 วัน ถึงผลลบก็ไม่ได้ตัด GI lesion ออก จึงไม่ควรใช้เป็นขั้นต่อไป
- ให้เหล็กอย่างเดียวโดยไม่หาสาเหตุ อาจพลาดมะเร็ง
- Hb typing ใช้แยก thalassemia — ferritin ต่ำยืนยัน IDA แล้ว
- Bone marrow aspiration ไม่จำเป็นเมื่อ iron study ชัด
(สไลด์เดิมให้ตัวเลือก colonoscope / guaiac 3 วัน / CBC ferritin โดยเฉลยเป็นภาพ — ข้อนี้เติม ferritin เพื่อให้คำตอบชัดตามแนวทางปัจจุบัน)''',
            pearl="IDA ในชาย/หญิงหมดประจำเดือน → colonoscopy + EGD แม้ FOBT ลบ", topic="IDA work-up",
            ref=[f"{D} หน้า 14, 21–22"], nl=["2.3.3(7)"]),
    ])

# ---------------------------------------------------------------- 01-03 Megaloblastic
F_B12 = fig("hemato-01-03-f1", "B12 vs folate: ดูดซึมที่ไหน ขาดเพราะอะไร", '''<svg viewBox="0 0 720 300">
 <defs><marker id="hemato-01-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="20" y="20" width="150" height="56" rx="10" class="box"/>
 <text x="95" y="44" text-anchor="middle" class="tb">กระเพาะ</text>
 <text x="95" y="62" text-anchor="middle" class="t3">parietal cell สร้าง IF</text>
 <path d="M170 48H200" class="ln" marker-end="url(#hemato-01-03-a)"/>
 <rect x="202" y="20" width="150" height="56" rx="10" class="box"/>
 <text x="277" y="44" text-anchor="middle" class="tb">Jejunum</text>
 <text x="277" y="62" text-anchor="middle" class="t3">ดูดซึม folate</text>
 <path d="M352 48H382" class="ln" marker-end="url(#hemato-01-03-a)"/>
 <rect x="384" y="20" width="150" height="56" rx="10" class="box"/>
 <text x="459" y="44" text-anchor="middle" class="tb">Terminal ileum</text>
 <text x="459" y="62" text-anchor="middle" class="t3">ดูดซึม B12–IF</text>
 <path d="M534 48H564" class="ln" marker-end="url(#hemato-01-03-a)"/>
 <rect x="566" y="20" width="134" height="56" rx="10" class="acsoft"/>
 <text x="633" y="44" text-anchor="middle" class="tb">DNA synthesis</text>
 <text x="633" y="62" text-anchor="middle" class="t3">ขาด → megaloblast</text>
 <rect x="20" y="100" width="330" height="186" rx="10" class="c2soft"/>
 <text x="36" y="124" class="tb">ขาด Vitamin B12 (สะสมได้ 3–4 ปี)</text>
 <text x="36" y="148" class="t2">• Gastrectomy (ไม่มี IF)</text>
 <text x="36" y="170" class="t2">• Pernicious anemia (Ab ต่อ parietal cell/IF)</text>
 <text x="36" y="192" class="t2">• Ileal resection, Crohn's ที่ ileum</text>
 <text x="36" y="214" class="t2">• Vegan (ไม่กินเนื้อ นม ไข่)</text>
 <text x="36" y="244" class="ta">มี neuropathy / ataxia / proprioception เสีย</text>
 <text x="36" y="266" class="t3">รักษา: B12 IM หรือ oral high dose</text>
 <rect x="370" y="100" width="330" height="186" rx="10" class="c1soft"/>
 <text x="386" y="124" class="tb">ขาด Folate (สะสมได้ไม่กี่เดือน)</text>
 <text x="386" y="148" class="t2">• Alcoholism, กินไม่ได้ (poor intake)</text>
 <text x="386" y="170" class="t2">• Jejunal resection, IBD</text>
 <text x="386" y="192" class="t2">• ↑Demand: ตั้งครรภ์, ให้นม, hemolysis</text>
 <text x="386" y="214" class="t2">• ยา: methotrexate</text>
 <text x="386" y="244" class="ta">ไม่มี neuropathy</text>
 <text x="386" y="266" class="t3">รักษา: folic acid oral/IV</text>
</svg>''', "ไล่ตามทางเดินอาหาร: ตัดกระเพาะ/ileum → ขาด B12 (มีอาการทางประสาท) · ติดเหล้า กินน้อย ตั้งครรภ์ → ขาด folate")

S3 = sec("hemato-01-03", "Megaloblastic anemia (B12 & folate deficiency)",
    "↓DNA synthesis → macro-ovalocyte + hypersegmented PMN ± pancytopenia · B12 มี neuropathy · gastrectomy → B12 IM", minutes=8,
    source=f"{D} หน้า 25–47", nl=["2.3.3(7)", "B2.2.5(1)"],
    md='''
### กลไก

- **↓DNA synthesis** แต่ RNA/ฮีโมโกลบินสร้างได้ → นิวเคลียสแก่ช้ากว่าไซโทพลาซึม → **megaloblast**
- เซลล์ตายในไขกระดูก = **ineffective hematopoiesis** → LDH และ indirect bilirubin สูงได้ (ตัวเหลืองเล็กน้อย) และกระทบทุก cell line (pancytopenia)
- B12 จับกับ **intrinsic factor (IF)** จาก parietal cell แล้วดูดซึมที่ **terminal ileum**

### สาเหตุ

| Vitamin B12 deficiency | Folate deficiency |
|---|---|
| ↓Absorption: **gastrectomy**, ileal resection, **pernicious anemia** | Poor intake: **alcoholism**, คนสูงอายุกินแต่ข้าวต้ม/ผักต้ม |
| Poor intake: ไม่กินเนื้อสัตว์ นม ไข่ (vegan) | ↓Absorption: IBD, jejunal resection |
| สะสมในตับมาก → **ใช้เวลา 3–4 ปี** กว่าจะซีด | ↑Demand: ตั้งครรภ์ ให้นม · ยา **MTX** |

**Pernicious anemia**: autoantibody ต่อ **parietal cell และ IF** · สัมพันธ์กับ autoimmune อื่น เช่น **autoimmune thyroiditis, vitiligo**

[[fig:hemato-01-03-f1]]

### อาการ

- ซีด ± **ตัวเหลืองเล็กน้อย** (ineffective erythropoiesis)
- **Beefy red tongue**, glossitis
- **Peripheral neuropathy, ataxia, เสีย proprioception/vibration** (subacute combined degeneration) — **เฉพาะ B12** ไม่พบใน folate
- ไม่มีตับม้ามโต (ช่วยแยกจาก AIHA/hemolysis)

### การตรวจ

- CBC: ↓Hb, **↑MCV (มัก > 110)**, ↑RDW ± ↓WBC ↓platelet (pancytopenia)
- PBS: **macro-ovalocyte, hypersegmented neutrophil**
- **↓Serum B12, ↓serum folate**
- Retic ต่ำ, LDH/indirect bilirubin สูงได้ (เสริม)

> MCV สูงมากต้องดู PBS เสมอ เพราะ **RBC agglutination (AIHA)** ก็ทำให้ MCV > 110 ได้ — AIHA จะมีม้ามโต retic สูง DAT บวก

### การรักษา

- **B12 deficiency**: vitamin B12 **IM** หรือ **oral high dose** — ผู้ป่วย gastrectomy/pernicious (ไม่มี IF) ควรให้ IM (เสริม: เช่น 1,000 µg IM ทุกวันสัปดาห์แรก → ทุกสัปดาห์ → ทุกเดือนตลอดชีวิต)
- **Folate deficiency**: **folic acid** oral/IV (เสริม: 1–5 mg/วัน)
- อย่าให้ folate อย่างเดียวในคนที่ขาด B12 — ซีดดีขึ้นแต่อาการทางประสาทแย่ลง (เสริม)
''',
    figs=[F_B12],
    pearls=[
        "Macro-ovalocyte + hypersegmented neutrophil = megaloblastic",
        "B12 ขาด → มีอาการทางประสาท (neuropathy, เสีย proprioception) · folate ไม่มี",
        "Total gastrectomy/pernicious → vitamin B12 IM",
        "คนติดเหล้า MCV สูง → folate deficiency",
        "B12 ใช้ 3–4 ปีกว่าจะซีดหลังตัดกระเพาะ",
    ],
    items=[
        mcq("HEMATO-01-03-1",
            "A 70-year-old woman has dyspnea on exertion for 3 months, gait difficulty, and paresthesia of both feet. PE: marked pallor, no jaundice, no hepatosplenomegaly, impaired proprioception of both feet. CBC: Hb 6.2 g/dL, Hct 20%, MCV 115 fL, RDW 25%, WBC 3,500/µL (N 52%, L 35%), platelet 80,000/µL. What is the most appropriate investigation for definitive diagnosis?",
            "Serum vitamin B12 level",
            ["Serum folate level", "Serum iron and TIBC", "Urine hemosiderin", "Bone marrow aspiration"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Macrocytic (MCV 115) + pancytopenia + **อาการทางประสาท (paresthesia, เสีย proprioception, เดินเซ)** = megaloblastic anemia จาก **B12 deficiency** → ตรวจ **serum B12** (ในหญิงสูงอายุนึกถึง pernicious anemia)
- Serum folate: folate deficiency ก็ macrocytic ได้ แต่ **ไม่ทำให้เกิด neuropathy/subacute combined degeneration**
- Serum iron/TIBC ใช้กับ microcytic anemia
- Urine hemosiderin ใช้ดู chronic intravascular hemolysis เช่น PNH — ผู้ป่วยไม่เหลือง
- Bone marrow aspiration เห็น megaloblast ได้ แต่ไม่บอกว่าขาดอะไร และ invasive กว่าการตรวจระดับวิตามิน''',
            pearl="Macrocytic + neuropathy → serum B12", topic="B12 deficiency",
            ref=[f"{D} หน้า 40–41"], nl=["2.3.3(7)"]),
        mcq("HEMATO-01-03-2",
            "A 70-year-old woman who lost all her teeth eats only rice porridge, fish, and well-boiled vegetables. She has fatigue for 3 months. CBC: Hb 8 g/dL, Hct 24%, MCV 112 fL, WBC 4,500/µL, platelet 110,000/µL. PBS: macro-ovalocytes with hypersegmented neutrophils. Neurological examination is normal. What is the most likely diagnosis?",
            "Folate deficiency",
            ["Iron deficiency anemia", "Anemia of chronic disease", "Myelodysplastic syndrome", "Aplastic anemia"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Macro-ovalocyte + hypersegmented neutrophil = **megaloblastic** · ประวัติกินแต่ **ผักต้มเปื่อย** (ความร้อนทำลาย folate) และ store ของ folate อยู่ได้ไม่กี่เดือน → **folate deficiency** · ตรวจระบบประสาทปกติสนับสนุนว่าไม่ใช่ B12 (ยังกินปลาได้)
- Iron deficiency ให้ microcytic hypochromic ไม่ใช่ macro-ovalocyte
- Anemia of chronic disease เป็น normocytic/microcytic
- MDS ก็ macrocytic ได้ แต่ PBS เด่น **hypogranular/hyposegmented (pseudo-Pelger-Huët)** ไม่ใช่ hypersegmented และไม่มีประวัติขาดอาหาร
- Aplastic anemia ไม่มี hypersegmented neutrophil และ MCV มักปกติ''',
            pearl="ผักต้มเปื่อย/เหล้า + megaloblastic → folate", topic="Folate deficiency",
            ref=[f"{D} หน้า 32–33"], nl=["2.3.3(7)"]),
        mcq("HEMATO-01-03-3",
            "A 60-year-old man underwent total gastrectomy 7 years ago for massive upper GI bleeding. He has fatigue for 6 months. CBC: Hb 7.3 g/dL, Hct 23%, MCV 123 fL, RDW 20%, WBC 3,400/µL, platelet 110,000/µL. What is the most appropriate management?",
            "Intramuscular vitamin B12",
            ["Oral folic acid", "Oral ferrous sulfate", "Intravenous immunoglobulin", "Intravenous dexamethasone"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Total gastrectomy → ไม่มี parietal cell สร้าง **intrinsic factor** → ดูดซึม B12 ไม่ได้ · store หมดใน 3–4 ปี → macrocytic + pancytopenia 7 ปีหลังผ่าตัด → ให้ **vitamin B12 แบบฉีด (IM)** ตลอดชีวิต
- Folic acid แก้ซีดได้บางส่วนแต่ไม่แก้สาเหตุ และอาจทำให้อาการทางประสาทของ B12 แย่ลง
- Ferrous sulfate: หลัง gastrectomy ขาดเหล็กได้ แต่ภาพนี้ macrocytic (MCV 123)
- IVIG และ dexamethasone ใช้กับ ITP/AIHA ไม่เกี่ยว''',
            pearl="Total gastrectomy → B12 IM ตลอดชีวิต", topic="B12 replacement",
            ref=[f"{D} หน้า 26, 29, 46–47"], nl=["2.3.3(7)", "B2.4(2)"]),
        mcq("HEMATO-01-03-4",
            "A woman presents with proximal muscle weakness of all limbs, pallor, and mild jaundice. PE: mild pallor, moderately icteric sclerae, deep tendon reflexes 1+, no hepatosplenomegaly. CBC: Hb 8 g/dL, MCV 113 fL, WBC 3,500/µL, platelet 45,000/µL. What is the most likely diagnosis?",
            "Megaloblastic anemia",
            ["Aplastic anemia", "Myelodysplastic syndrome", "Pure red cell aplasia", "Autoimmune hemolytic anemia"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''**Pancytopenia + MCV > 110 + ตัวเหลือง (ineffective erythropoiesis) + อาการทางระบบประสาท (reflex ลด, อ่อนแรง)** = megaloblastic anemia (โดยเฉพาะ B12)
- Aplastic anemia เป็น pancytopenia แต่ **ไม่เหลือง** MCV ปกติหรือสูงเล็กน้อย และไม่มีอาการทางประสาท
- MDS พบในผู้สูงอายุ macrocytic ได้ แต่ไม่อธิบายตัวเหลืองและ neuropathy
- Pure red cell aplasia กระทบเฉพาะเม็ดเลือดแดง WBC/platelet ปกติ
- AIHA มีเหลืองได้ แต่ platelet/WBC ไม่ต่ำ (ยกเว้น Evans) และไม่มี neuropathy''',
            pearl="Pancytopenia + MCV สูง + เหลือง + neuro = B12 deficiency", topic="Megaloblastic vs pancytopenia",
            ref=[f"{D} หน้า 30–31"], nl=["2.3.3(7)"]),
        mcq("HEMATO-01-03-5",
            "A 45-year-old man with long-standing heavy alcohol use has mild jaundice. CBC: Hb 9 g/dL, Hct 27%, MCV 110 fL, WBC 5,200/µL, platelet 120,000/µL. Which nutritional deficiency most likely explains these findings?",
            "Folate deficiency",
            ["Vitamin B1 deficiency", "Vitamin B6 deficiency", "Vitamin B2 deficiency", "Iron deficiency"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''คนติดเหล้ากินอาหารน้อยและแอลกอฮอล์รบกวน folate metabolism → **folate deficiency** ให้ macrocytic anemia ± platelet ต่ำ
- Vitamin B1 (thiamine) deficiency ทำให้ Wernicke/beriberi ไม่ทำให้ macrocytic anemia
- Vitamin B6 deficiency สัมพันธ์กับ sideroblastic anemia ซึ่งเป็น **microcytic**
- Vitamin B2 deficiency ทำให้ angular stomatitis ไม่ใช่สาเหตุหลักของ MCV สูง
- Iron deficiency ให้ microcytic''',
            pearl="Alcohol + MCV สูง → folate", topic="Alcohol & macrocytosis",
            ref=[f"{D} หน้า 34–35"], nl=["2.3.3(7)"]),
    ])

# ---------------------------------------------------------------- 01-04 ACD
F_IRON = fig("hemato-01-04-f1", "Iron study: IDA vs ACD vs thalassemia trait", '''<svg viewBox="0 0 720 270">
 <rect x="20" y="16" width="170" height="40" rx="8" class="sunk"/>
 <text x="105" y="41" text-anchor="middle" class="tb">ค่า</text>
 <rect x="200" y="16" width="160" height="40" rx="8" class="c1"/>
 <text x="280" y="41" text-anchor="middle" class="tw">IDA</text>
 <rect x="370" y="16" width="160" height="40" rx="8" class="c2"/>
 <text x="450" y="41" text-anchor="middle" class="tw">ACD</text>
 <rect x="540" y="16" width="160" height="40" rx="8" class="ac"/>
 <text x="620" y="41" text-anchor="middle" class="tw">Thal trait</text>
 <text x="105" y="86" text-anchor="middle" class="tb">Serum iron</text>
 <text x="105" y="122" text-anchor="middle" class="tb">TIBC</text>
 <text x="105" y="158" text-anchor="middle" class="tb">Transferrin sat</text>
 <text x="105" y="194" text-anchor="middle" class="tb">Ferritin</text>
 <text x="105" y="230" text-anchor="middle" class="tb">RDW · Plt</text>
 <rect x="200" y="66" width="160" height="188" rx="8" class="c1soft"/>
 <text x="280" y="86" text-anchor="middle" class="tb">↓</text>
 <text x="280" y="122" text-anchor="middle" class="ta">↑</text>
 <text x="280" y="158" text-anchor="middle" class="tb">↓</text>
 <text x="280" y="194" text-anchor="middle" class="ta">↓ (&lt; 30)</text>
 <text x="280" y="230" text-anchor="middle" class="t2">RDW ↑ · Plt ↑</text>
 <rect x="370" y="66" width="160" height="188" rx="8" class="c2soft"/>
 <text x="450" y="86" text-anchor="middle" class="tb">↓</text>
 <text x="450" y="122" text-anchor="middle" class="ta">↓</text>
 <text x="450" y="158" text-anchor="middle" class="tb">↓</text>
 <text x="450" y="194" text-anchor="middle" class="ta">↑ / ปกติ</text>
 <text x="450" y="230" text-anchor="middle" class="t2">retic ↓</text>
 <rect x="540" y="66" width="160" height="188" rx="8" class="acsoft"/>
 <text x="620" y="86" text-anchor="middle" class="tb">ปกติ</text>
 <text x="620" y="122" text-anchor="middle" class="tb">ปกติ</text>
 <text x="620" y="158" text-anchor="middle" class="tb">ปกติ</text>
 <text x="620" y="194" text-anchor="middle" class="tb">ปกติ / ↑</text>
 <text x="620" y="230" text-anchor="middle" class="t2">MCV ↓↓ แต่ Hb ดี</text>
</svg>''', "ตัวแยก IDA กับ ACD คือ TIBC และ ferritin ที่ไปทางตรงข้ามกัน · thal trait iron study ปกติ (ACD/thal เป็นส่วนเสริมเทียบ)")

S4 = sec("hemato-01-04", "Anemia of chronic disease (ACD)",
    "Inflammation → hepcidin ↑ → เหล็กติดใน macrophage · ↓Fe ↓TIBC ↑ferritin · normocytic → microcytic · รักษาที่สาเหตุ", minutes=5,
    source=f"{D} หน้า 48–50", nl=["2.3.3(7)", "3.3.26"],
    md='''
### สาเหตุ

- **Chronic inflammation** เช่น RA, SLE, IBD
- **Malignancy**
- **Chronic infection** (TB, HIV, osteomyelitis)

### กลไก (เสริม)

- Cytokine (IL-6) → ตับสร้าง **hepcidin ↑** → ปิด ferroportin → เหล็กถูกกักใน macrophage และลำไส้ไม่ดูดซึม → ไขกระดูกได้เหล็กไม่พอ แม้ store เต็ม
- EPO ตอบสนองน้อยและ RBC อายุสั้นลงเล็กน้อย

### การตรวจ

- CBC/PBS: **normocytic (ระยะแรก) → microcytic (ระยะหลัง)** · ซีดไม่มาก (Hb มัก 8–10)
- **↓Serum iron, ↓TIBC, ↓transferrin saturation**
- **↑Serum ferritin** (acute phase reactant + store เต็ม)
- **↓Reticulocyte**

[[fig:hemato-01-04-f1]]

> โจทย์ microcytic + โรคอักเสบเรื้อรัง + **ferritin สูง** = ACD · ถ้า ferritin < 30 = IDA ร่วมด้วย (ในภาวะอักเสบ ferritin 30–100 ยังอาจมี IDA ซ่อน — เสริม)

### การรักษา

- **รักษาโรคต้นเหตุ** (ควบคุมการอักเสบ/ติดเชื้อ/มะเร็ง)
- ไม่ต้องให้เหล็กถ้าไม่มี IDA ร่วม · EPO ในบางกลุ่ม เช่น CKD/มะเร็งที่ได้เคมีบำบัด (เสริม)
''',
    figs=[F_IRON],
    pearls=[
        "ACD: ↓Fe ↓TIBC ↑ferritin (IDA: ↓Fe ↑TIBC ↓ferritin)",
        "ACD ระยะแรก normocytic → ระยะหลัง microcytic",
        "รักษา ACD = รักษาโรคต้นเหตุ ไม่ใช่ให้เหล็ก",
    ],
    items=[
        mcq("HEMATO-01-04-1",
            "A 28-year-old woman has poorly controlled inflammatory bowel disease for 1 year. CBC: Hb 8.5 g/dL, Hct 26%, MCV 76 fL. Serum ferritin is 200 µg/L. What is the most likely cause of her anemia?",
            "Anemia of chronic inflammation",
            ["Iron deficiency", "Folate deficiency", "Vitamin B12 deficiency", "Combined iron and folate deficiency"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''IBD ที่ควบคุมไม่ได้ + microcytic เล็กน้อย + **ferritin สูง (200)** = **ACD (inflammation)** — hepcidin สูงกักเหล็ก ferritin ขึ้นตามการอักเสบ
- Iron deficiency: IBD เสียเลือดได้ แต่ ferritin จะต่ำ (< 30) ไม่ใช่ 200
- Folate และ B12 deficiency (IBD ที่ jejunum/ileum) ให้ **macrocytic** ไม่ใช่ MCV 76
- Combined iron + folate deficiency อาจให้ MCV ปกติและ RDW สูงมาก แต่ ferritin ก็ยังต้องต่ำ''',
            pearl="Microcytic + โรคอักเสบ + ferritin สูง = ACD", topic="ACD vs IDA",
            ref=[f"{D} หน้า 49–50"], nl=["2.3.3(7)", "3.3.26"]),
        mcq("HEMATO-01-04-2",
            "A 55-year-old woman with active rheumatoid arthritis has Hb 9.5 g/dL, MCV 79 fL, and reticulocyte count 0.6%. Which iron study pattern is most consistent with anemia of chronic disease?",
            "Low serum iron, low TIBC, high ferritin",
            ["Low serum iron, high TIBC, low ferritin", "High serum iron, normal TIBC, high ferritin", "Normal serum iron, normal TIBC, normal ferritin", "Low serum iron, high TIBC, high ferritin"],
            explain='''ACD: hepcidin ↑ กักเหล็กใน macrophage → **serum iron ↓, TIBC ↓ (ตับสร้าง transferrin น้อยลง), ferritin ↑** และ retic ต่ำ
- Low iron + high TIBC + low ferritin = แบบแผนของ **IDA**
- High iron + high ferritin = iron overload (hemochromatosis, thalassemia ที่ได้เลือดบ่อย)
- ค่าปกติทั้งหมด + MCV ต่ำมากเทียบกับ Hb = thalassemia trait
- Low iron + high TIBC + high ferritin ขัดกันเอง (TIBC สูงคือร่างกายขาดเหล็ก แต่ ferritin สูงคือ store เต็ม)''',
            pearl="IDA กับ ACD ต่างกันที่ TIBC และ ferritin", topic="Iron study patterns",
            ref=[f"{D} หน้า 13, 48"], nl=["3.3.26"]),
        mcq("HEMATO-01-04-3",
            "A 62-year-old man with pulmonary tuberculosis on treatment for 2 months has Hb 9.8 g/dL, MCV 84 fL, ferritin 450 ng/mL, TIBC low, and reticulocyte count 0.8%. There is no bleeding. What is the most appropriate management of his anemia?",
            "Continue treating the tuberculosis and observe the anemia",
            ["Start oral ferrous sulfate", "Transfuse packed red cells", "Start oral folic acid", "Bone marrow aspiration"],
            explain='''ACD จาก chronic infection (TB) — ferritin สูง TIBC ต่ำ retic ต่ำ ซีดไม่มาก → **รักษาโรคต้นเหตุ** ตามสไลด์ (Mx: Tx underlying cause) ซีดจะดีขึ้นเมื่อการอักเสบลดลง
- Ferrous sulfate ไม่ช่วยเพราะเหล็กถูก hepcidin กักไว้ และ store เต็มอยู่แล้ว
- PRC transfusion ใช้เมื่อ Hb < 7 หรือมีอาการรุนแรง — Hb 9.8 ไม่มีข้อบ่งชี้
- Folic acid ใช้เมื่อขาด folate (macrocytic)
- Bone marrow aspiration ไม่จำเป็น ภาพเข้ากับ ACD ชัด''',
            pearl="ACD → รักษาสาเหตุ", topic="ACD management",
            ref=[f"{D} หน้า 48"], nl=["2.3.3(7)"]),
    ])

# ---------------------------------------------------------------- 01-05 Lead
S5 = sec("hemato-01-05", "Lead poisoning",
    "ทำงานโรงงานแบตเตอรี่ · ↓heme synthesis · microcytic + basophilic stippling · wrist/foot drop · ปวดท้อง · lead line", minutes=4,
    source=f"{D} หน้า 51–54", nl=["2.3.18(7)", "2.3.19(3)"],
    md='''
### กลไกและการสัมผัส

- สัมผัสตะกั่วจากอาชีพ เช่น **โรงงานผลิต/รีไซเคิลแบตเตอรี่**, หลอมโลหะ, สีทาบ้านเก่า
- ตะกั่วยับยั้งเอนไซม์สร้าง heme (ALA dehydratase, ferrochelatase) → **↓heme synthesis** → microcytic anemia และยับยั้ง pyrimidine 5′-nucleotidase → RNA ค้างเป็น basophilic stippling (เสริม)

### อาการหลายระบบ

| ระบบ | อาการ |
|---|---|
| CNS/PNS | Encephalopathy, ปวดศีรษะ, ความจำแย่ · **peripheral motor neuropathy: wrist drop / foot drop** |
| Hematology | ซีด |
| GI | **ปวดท้อง (lead colic)** ท้องผูก |
| Renal | Acute interstitial nephritis |
| อื่น ๆ | **Lead line** (เส้นสีม่วงน้ำเงินที่เหงือก) |

### การตรวจ

- PBS: **hypochromic microcytic + basophilic stippling** (coarse)
- **↑Blood lead level** (ยืนยัน)

### การรักษา

- **ลด/หยุดการสัมผัส** (ย้ายงาน ป้องกันส่วนบุคคล)
- **Chelation therapy** (เสริม: CaNa2EDTA, dimercaprol กรณี encephalopathy, succimer oral)

> โจทย์ที่ให้ซีด + ปวดท้อง + **foot/wrist drop** + อาชีพแบตเตอรี่ + **basophilic stippling** = lead poisoning · ระวังสับสนกับ thalassemia ที่ก็มี basophilic stippling ได้
''',
    pearls=[
        "แบตเตอรี่ + ซีด + ปวดท้อง + wrist/foot drop = lead",
        "PBS: microcytic + coarse basophilic stippling",
        "รักษา: หยุดสัมผัส + chelation",
    ],
    items=[
        mcq("HEMATO-01-05-1",
            "A 56-year-old man has fatigue, pallor, and abdominal pain. He reports memory loss and works at a battery recycling plant. PE: bilateral foot drop. CBC: Hb 9 g/dL, MCV 74 fL. PBS shows hypochromic microcytic RBCs with coarse basophilic stippling. What is the most likely diagnosis?",
            "Lead poisoning",
            ["Thalassemia trait", "Autoimmune hemolytic anemia", "Vitamin B12 deficiency", "Iron deficiency anemia"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''อาชีพ **รีไซเคิลแบตเตอรี่** + ซีด microcytic + **basophilic stippling** + ปวดท้อง + ความจำแย่ + **foot drop (motor neuropathy)** = lead poisoning
- Thalassemia trait มี basophilic stippling และ microcytic ได้ แต่ไม่อธิบายปวดท้อง ความจำเสีย และ foot drop
- AIHA เป็น hemolysis มี microspherocyte เหลือง ไม่ใช่ microcytic + neuropathy
- B12 deficiency มี neuropathy ได้ แต่เป็น macrocytic และเป็น sensory/proprioception มากกว่า foot drop
- IDA ไม่มี basophilic stippling และไม่มีอาการระบบประสาท''',
            pearl="Microcytic + basophilic stippling + foot drop + แบตเตอรี่ = lead", topic="Lead poisoning",
            ref=[f"{D} หน้า 51–54"], nl=["2.3.18(7)"]),
        mcq("HEMATO-01-05-2",
            "A 38-year-old battery factory worker is diagnosed with lead poisoning after presenting with colicky abdominal pain, wrist drop, and microcytic anemia with basophilic stippling. His blood lead level is markedly elevated. Besides chelation therapy, what is the most important management?",
            "Remove him from further lead exposure",
            ["Oral iron supplementation", "Regular red cell transfusion", "Oral prednisolone", "Splenectomy"],
            explain='''หลักการรักษาตามสไลด์คือ **↓exposure** (เอาออกจากแหล่งตะกั่ว) ร่วมกับ **chelation therapy** — ถ้ายังสัมผัสต่อ การ chelate จะไม่ได้ผลระยะยาว
- Oral iron ไม่แก้กลไก (ปัญหาคือ heme synthesis ถูกยับยั้ง ไม่ใช่ขาดเหล็ก) เว้นแต่มี IDA ร่วม
- Regular transfusion ไม่จำเป็น ซีดมักไม่รุนแรงและดีขึ้นเมื่อระดับตะกั่วลด
- Prednisolone ใช้กับ immune-mediated disease ไม่เกี่ยว
- Splenectomy ไม่มีบทบาท''',
            pearl="Lead: หยุดสัมผัส + chelation", topic="Lead management",
            ref=[f"{D} หน้า 52"], nl=["2.3.18(7)", "2.3.19(3)"]),
    ])

LECTURE = lecture("01", "Anemia approach & hypoproliferative anemia",
    "CBC · reticulocyte · IDA · megaloblastic · ACD · lead",
    objectives=[
        "นิยาม anemia ตามเพศ อายุ และอายุครรภ์ และคำนวณ corrected reticulocyte ได้",
        "แยกสาเหตุซีดด้วย MCV และ reticulocyte ได้",
        "แปลผล iron study แยก IDA กับ ACD และรู้ลำดับการตอบสนองต่อเหล็ก",
        "แยก B12 กับ folate deficiency จากประวัติและอาการทางประสาท และเลือกการรักษาได้",
        "จำลักษณะ lead poisoning (basophilic stippling + neuropathy) ได้",
    ],
    sections=[S1, S2, S3, S4, S5])
