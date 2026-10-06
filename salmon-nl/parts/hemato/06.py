from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Hemato"

# ---------------------------------------------------------------- 06-01 Multiple myeloma
S1 = sec("hemato-06-01", "Multiple myeloma",
    "CRAB: ↑Ca, renal failure, anemia, bone pain · rouleaux · globulin สูง · SPEP + BM · hypercalcemia → NSS ก่อน", minutes=6,
    source=f"{D} หน้า 276–278", nl=["B2.2.4-3(4)", "2.3.4(2)"],
    md='''
### นิยาม

- มะเร็งของ **plasma cell** ในไขกระดูก สร้าง monoclonal immunoglobulin (M-protein) — พบในผู้สูงอายุ (เสริม)

### CRAB

| | อาการ/lab |
|---|---|
| **C** – Calcium | **Hypercalcemia** (ซึม สับสน ท้องผูก ปัสสาวะมาก ขาดน้ำ) |
| **R** – Renal failure | Cast nephropathy (light chain), hypercalcemia, ขาดน้ำ |
| **A** – Anemia | Normocytic, BM infiltration |
| **B** – Bone pain | **Osteolytic lesion** (punched-out กะโหลก กระดูกสันหลัง), pathologic fracture |

### การตรวจ

- PBS: **rouleaux formation**, plasma cell
- Lab: **↑Ca, ↑Cr, ↓Hb, ↑globulin** (albumin:globulin กลับข้าง — protein gap กว้าง)
- X-ray: **osteolytic lesion**
- **Serum protein electrophoresis (SPEP)** → M-spike (+ immunofixation, serum free light chain — เสริม)
- **BM biopsy**: clonal plasma cell ≥ 10% (เสริม)

### การรักษา

- **Chemotherapy**, **stem cell transplantation** (เสริม: bortezomib–lenalidomide–dexamethasone)
- **จัดการภาวะแทรกซ้อน**: AKI, hypercalcemia, bone lesion
  - Hypercalcemia: **IV fluid (NSS) เป็นอันดับแรก** → bisphosphonate (zoledronic acid)/calcitonin → steroid (เสริมลำดับหลัง NSS)
  - Bone: bisphosphonate, radiation สำหรับปวด/กดไขสันหลัง (เสริม)

> ผู้ป่วย myeloma ซึม ขาดน้ำ Ca 13.5 Cr สูง → **NSS infusion ก่อน** (แก้ volume depletion ที่ hypercalcemia ทำให้เกิด) · furosemide ให้หลัง volume พอแล้วเท่านั้น
''',
    pearls=[
        "Myeloma: CRAB + rouleaux + globulin สูง",
        "Ix: SPEP + BM biopsy + skeletal survey (osteolytic)",
        "Hypercalcemia จาก myeloma: NSS ก่อน แล้วค่อย bisphosphonate",
    ],
    items=[
        mcq("HEMATO-06-01-1",
            "A 59-year-old man with multiple myeloma has had altered consciousness for 3 days. RR 18/min, PR 100/min, BP 120/70 mmHg. PE: dry lips, poor skin turgor, mild pallor. Labs: Na 135, K 4, Cl 110, HCO3 25 mmol/L, Ca 13.5 mg/dL, PO4 6 mg/dL, BUN 40 mg/dL, Cr 2.2 mg/dL, albumin 3 g/dL, globulin 8 g/dL. What is the next most appropriate management?",
            "Normal saline infusion",
            ["Furosemide", "Bisphosphonate", "Dexamethasone", "Calcitonin"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (สไลด์เขียน Ca 13.5 PO4 6 'mmol/L' — ปรับหน่วยเป็น mg/dL ให้สมเหตุผล)",
            explain='''Hypercalcemia (Ca 13.5) ทำให้ diuresis → **ขาดน้ำ** (ปากแห้ง skin turgor ลด BUN/Cr สูง) → ขั้นแรกคือ **NSS infusion** เพื่อคืน volume และเพิ่มการขับ Ca (สไลด์: complication Mx → 1st IV fluid)
- Furosemide ให้หลังให้น้ำเพียงพอแล้วเท่านั้น ให้ก่อนจะยิ่งขาดน้ำ
- Bisphosphonate ได้ผลใน 2–4 วัน ใช้ตามหลัง NSS (และระวังเมื่อ Cr สูง)
- Dexamethasone ช่วยลด Ca ใน myeloma และเป็นส่วนหนึ่งของเคมีบำบัด แต่ไม่ใช่ขั้นแรก
- Calcitonin ออกฤทธิ์เร็วแต่อ่อน ใช้ร่วมหลังให้น้ำ
(หมายเหตุ: Ca 13.5 mmol/L เป็นไปไม่ได้ทางสรีรวิทยา จึงอ่านเป็น mg/dL)''',
            pearl="HyperCa → NSS ก่อนเสมอ", topic="Myeloma hypercalcemia",
            ref=[f"{D} หน้า 277–278"], nl=["B2.2.4-3(4)", "2.3.4(2)"]),
        mcq("HEMATO-06-01-2",
            "A 68-year-old woman has back pain for 3 months and fatigue. Hb 8.8 g/dL, MCV 92 fL, creatinine 2.1 mg/dL, calcium 11.6 mg/dL, total protein 10.2 g/dL, albumin 3.0 g/dL. Spine x-ray shows multiple lytic lesions. PBS shows rouleaux formation. What is the most appropriate initial investigation to confirm the diagnosis?",
            "Serum protein electrophoresis",
            ["Hemoglobin typing", "Direct antiglobulin test", "Serum PTH level", "Bone scintigraphy"],
            explain='''CRAB (hyperCa, Cr สูง, ซีด, ปวดหลัง + lytic lesion) + **globulin สูง (protein 10.2 – albumin 3.0)** + rouleaux = multiple myeloma → ตรวจ **SPEP** หา M-spike ร่วมกับ BM biopsy
- Hb typing ใช้กับ thalassemia
- DAT ใช้กับ AIHA — rouleaux เกิดจาก globulin สูง ไม่ใช่ agglutination จากแอนติบอดีต่อ RBC
- PTH ใช้ในการหาสาเหตุ hypercalcemia แต่ภาพนี้ชี้ไปที่ myeloma (PTH จะถูกกด)
- Bone scan มักเป็นลบในรอยโรค lytic ของ myeloma (ไม่มี osteoblastic activity — เสริม)''',
            pearl="CRAB + globulin สูง → SPEP", topic="Myeloma diagnosis",
            ref=[f"{D} หน้า 276"], nl=["B2.2.4-3(4)"]),
        mcq("HEMATO-06-01-3",
            "Which peripheral blood smear finding is most characteristic of multiple myeloma?",
            "Rouleaux formation",
            ["Smudge cells", "Teardrop cells", "Basophilic stippling", "Hypersegmented neutrophils"],
            explain='''Immunoglobulin (M-protein) ปริมาณมากลดแรงผลักระหว่าง RBC → RBC เรียงซ้อนกันเป็นตั้งเหรียญ = **rouleaux formation** (ร่วมกับ plasma cell ใน PBS)
- Smudge cell = CLL
- Teardrop cell = myelofibrosis/myelophthisis
- Basophilic stippling = lead poisoning, thalassemia
- Hypersegmented neutrophil = megaloblastic anemia''',
            pearl="Rouleaux = myeloma", topic="Myeloma PBS",
            ref=[f"{D} หน้า 276"], nl=["B2.2.4-3(4)", "3.1.2"]),
    ])

# ---------------------------------------------------------------- 06-02 Aplastic anemia
F_PAN = fig("hemato-06-02-f1", "Pancytopenia: แยกด้วยตับม้าม MCV PBS และ bone marrow", '''<svg viewBox="0 0 740 340">
 <defs><marker id="hemato-06-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="240" y="10" width="260" height="40" rx="10" class="acsoft"/>
 <text x="370" y="35" text-anchor="middle" class="tb">Pancytopenia → BM study</text>
 <path d="M280 50L95 90" class="ln" marker-end="url(#hemato-06-02-a)"/>
 <path d="M330 50L278 90" class="ln" marker-end="url(#hemato-06-02-a)"/>
 <path d="M410 50L462 90" class="ln" marker-end="url(#hemato-06-02-a)"/>
 <path d="M460 50L645 90" class="ln" marker-end="url(#hemato-06-02-a)"/>
 <rect x="10" y="92" width="170" height="236" rx="10" class="c1soft"/>
 <text x="95" y="114" text-anchor="middle" class="tb">Aplastic anemia</text>
 <text x="22" y="140" class="t2">ไม่มีตับม้ามโต</text>
 <text x="22" y="160" class="t2">Relative</text>
 <text x="22" y="178" class="t2">lymphocytosis</text>
 <text x="22" y="198" class="t2">Retic ต่ำมาก</text>
 <text x="22" y="218" class="t2">MCV ปกติ</text>
 <text x="22" y="252" class="ta">BM biopsy:</text>
 <text x="22" y="272" class="t2">hypocellular</text>
 <text x="22" y="292" class="t2">fatty marrow</text>
 <rect x="190" y="92" width="170" height="236" rx="10" class="badsoft"/>
 <text x="275" y="114" text-anchor="middle" class="tb">Acute leukemia</text>
 <text x="202" y="140" class="t2">ไข้ ปวดกระดูก</text>
 <text x="202" y="160" class="t2">ตับม้าม/LN โต</text>
 <text x="202" y="180" class="t2">± blast ใน PBS</text>
 <text x="202" y="200" class="t2">WBC ↓/↔/↑</text>
 <text x="202" y="252" class="ta">BM:</text>
 <text x="202" y="272" class="t2">blast &gt; 20%</text>
 <text x="202" y="292" class="t2">hypercellular</text>
 <rect x="370" y="92" width="170" height="236" rx="10" class="misssoft"/>
 <text x="455" y="114" text-anchor="middle" class="tb">MDS</text>
 <text x="382" y="140" class="t2">ผู้สูงอายุ</text>
 <text x="382" y="160" class="t2">MCV สูงได้</text>
 <text x="382" y="180" class="t2">Pseudo-Pelger-Huët</text>
 <text x="382" y="200" class="t2">hypogranular PMN</text>
 <text x="382" y="220" class="t2">large plt</text>
 <text x="382" y="252" class="ta">BM:</text>
 <text x="382" y="272" class="t2">dysplasia</text>
 <text x="382" y="292" class="t2">blast &lt; 20%</text>
 <rect x="550" y="92" width="180" height="236" rx="10" class="c2soft"/>
 <text x="640" y="114" text-anchor="middle" class="tb">Myelophthisis</text>
 <text x="562" y="140" class="t2">มะเร็งแพร่กระจาย</text>
 <text x="562" y="160" class="t2">TB, myelofibrosis</text>
 <text x="562" y="186" class="t2">Leukoerythroblastic:</text>
 <text x="562" y="206" class="t2">NRC + myelocyte</text>
 <text x="562" y="226" class="t2">+ tear drop cell</text>
 <text x="562" y="252" class="ta">BM biopsy:</text>
 <text x="562" y="272" class="t2">infiltration</text>
 <text x="562" y="292" class="t2">/ fibrosis</text>
</svg>''', "ทุกกรณีของ pancytopenia ที่ไม่มีสาเหตุชัด (เช่น B12) ต้องจบที่ bone marrow · ภาพ PBS และตับม้ามช่วยเดาก่อนว่าจะเจออะไร")

S2 = sec("hemato-06-02", "Aplastic anemia",
    "Stem cell ↓ · pancytopenia + relative lymphocytosis + retic ต่ำ · ไม่มีตับม้ามโต · BM biopsy hypocellular fatty · immunosuppression/BMT", minutes=7,
    source=f"{D} หน้า 159–172, 286", nl=["2.3.3-3(1)", "B2.2.2-3(1)"],
    md='''
### กลไก

- **↓Hematopoietic stem cells** (ส่วนใหญ่ immune-mediated T-cell ทำลาย — เสริม) → ไขกระดูกฝ่อ
- กระทบ **myeloid cell line** (RBC, granulocyte, platelet) — **lymphoid ไม่โดน** → **relative lymphocytosis**

### สาเหตุ

- **Idiopathic** (ส่วนใหญ่)
- **Drugs** (chloramphenicol, carbamazepine, gold — เสริมตัวอย่าง), **benzene**, **insecticides**, **radiation**
- **Virus** (hepatitis, parvovirus, EBV — เสริม)
- **Fanconi anemia** (inherited)
- สัมพันธ์กับ PNH (ดูหมวด hemolysis)

### อาการ

- **Anemia** (ซีด เหนื่อย SEM จาก high output)
- **Mucosal bleeding, petechiae** (platelet ต่ำ)
- **Infection** (neutropenia)
- **ไม่มีตับม้ามโต ไม่มีต่อมน้ำเหลืองโต** (สำคัญในการแยกจาก leukemia/lymphoma)

### การตรวจ

- CBC/PBS: **pancytopenia + relative lymphocytosis** (L 60–90%), NCNC RBC, **↓reticulocyte** (มัก < 1%)
- **BM biopsy: hypocellularity with fatty infiltration** — **ต้องทำ BM biopsy** เพื่อ R/O สาเหตุ pancytopenia อื่น (leukemia, MDS, myelophthisis)

[[fig:hemato-06-02-f1]]

### การรักษา

- **Transfusion** (PRC, platelet) แบบประคับประคอง · รักษา/หยุดสาเหตุ
- **Immunosuppressants** (ATG + cyclosporine ± eltrombopag — เสริม)
- **BM transplant** (อายุน้อยที่มี matched donor)

> Pancytopenia + **lymphocyte 70–90%** + retic ต่ำมาก + **ไม่มีตับม้ามโต** ในคนหนุ่มสาว = aplastic anemia · ขั้นต่อไปคือ **bone marrow (biopsy)**
''',
    figs=[F_PAN],
    pearls=[
        "Aplastic anemia: pancytopenia + relative lymphocytosis + retic ต่ำ + ไม่มีตับม้ามโต",
        "ต้องทำ BM biopsy: hypocellular, fatty marrow",
        "สาเหตุ: idiopathic, ยา, benzene, insecticide, radiation, virus, Fanconi",
        "รักษา: transfusion, immunosuppression, BMT",
    ],
    items=[
        mcq("HEMATO-06-02-1",
            "A 30-year-old woman has fatigue, exertional dyspnea, and gum bleeding. PE: moderate pallor, no jaundice, no hepatosplenomegaly, no lymphadenopathy. CBC: Hb 7.2 g/dL, MCV 90 fL, WBC 2,100/µL (N 20%, L 73%, M 5%, E 2%), platelet 3,000/µL, reticulocyte 0.1%. PBS: normochromic normocytic RBC; WBC and platelets decreased; no blasts. What is the most likely diagnosis?",
            "Aplastic anemia",
            ["Myelodysplastic syndrome", "Multiple myeloma", "Megaloblastic anemia", "Paroxysmal nocturnal hemoglobinuria"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''**Pancytopenia + relative lymphocytosis (L 73%) + retic ต่ำมาก + ไม่มีตับม้ามโต** ในหญิงอายุน้อย = aplastic anemia
- MDS พบในผู้สูงอายุ มี dysplasia (pseudo-Pelger-Huët, hypogranular) และ MCV มักสูง
- Myeloma: CRAB, rouleaux, ผู้สูงอายุ
- Megaloblastic: MCV > 100, hypersegmented PMN, retic ต่ำแต่มีเหลืองเล็กน้อย
- PNH มี pancytopenia ได้แต่ต้องมี hemolysis (retic สูง LDH สูง ปัสสาวะดำ)''',
            pearl="Pancytopenia + lymphocytosis + retic 0.1% = AA", topic="Aplastic anemia diagnosis",
            ref=[f"{D} หน้า 159, 161–162"], nl=["2.3.3-3(1)"]),
        mcq("HEMATO-06-02-2",
            "A 30-year-old woman has pallor and fatigue for 1 month without fever. PE: moderately pale conjunctivae, no jaundice, liver and spleen not palpable, no lymphadenopathy. CBC: Hb 7 g/dL, Hct 20%, MCV 92 fL, WBC 2,600/µL (N 40%, L 57%, M 3%), platelet 30,000/µL, reticulocyte 0.2%. What is the underlying pathophysiology?",
            "Hematopoietic stem cell deficiency",
            ["Nutritional deficiency", "Splenic sequestration", "Antibody against blood cells", "Defect in DNA synthesis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่ม MCV และ retic)",
            explain='''Pancytopenia + MCV ปกติ + retic ต่ำ + ไม่มีม้ามโต + lymphocyte เด่น = aplastic anemia → กลไกคือ **hematopoietic stem cell ลดลง**
- Nutritional deficiency (B12/folate) = defect in DNA synthesis → MCV สูง hypersegmented PMN
- Splenic sequestration ต้องมีม้ามโต
- Antibody ต่อเซลล์เม็ดเลือด (Evans/ITP/AIHA) จะมี retic สูงถ้า RBC ถูกทำลาย
- Defect in DNA synthesis เป็นกลไกของ megaloblastic''',
            pearl="AA = stem cell deficiency", topic="AA pathophysiology",
            ref=[f"{D} หน้า 159, 165–166"], nl=["2.3.3-3(1)", "B2.2.2-3(1)"]),
        mcq("HEMATO-06-02-3",
            "A 25-year-old man has fatigue for 6 months and frequent epistaxis for 1 month. He takes no regular medication. PE: moderate pallor, no jaundice, petechiae on both legs, no hepatosplenomegaly or lymphadenopathy. CBC: Hb 8.5 g/dL, MCV 90 fL, WBC 2,500/µL (N 10%, L 88%, M 2%), platelet 18,000/µL, reticulocyte 0.1%. What is the most appropriate investigation to confirm the diagnosis?",
            "Bone marrow biopsy",
            ["Flow cytometry of peripheral blood for leukemia", "Serum vitamin B12", "Anti-HIV only, then treat as ITP", "Direct antiglobulin test"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เปลี่ยนคำถามจากการวินิจฉัยเป็นการตรวจยืนยัน)",
            explain='''ภาพ aplastic anemia (pancytopenia + lymphocyte 88% + retic 0.1% + ไม่มีตับม้ามโต) → **BM biopsy** เพื่อยืนยัน hypocellular fatty marrow และ R/O สาเหตุ pancytopenia อื่น (leukemia, MDS, myelophthisis)
- Flow cytometry ของเลือดช่วยในมะเร็งเม็ดเลือดที่มี blast/lymphocyte ผิดปกติ แต่ไม่ยืนยัน AA
- Serum B12 ใช้เมื่อ MCV สูง
- ITP มีแค่ platelet ต่ำ — WBC และ Hb ต่ำด้วยจึงไม่ใช่ ITP
- DAT ใช้กับ hemolysis''',
            pearl="AA ต้องยืนยันด้วย BM biopsy", topic="AA investigation",
            ref=[f"{D} หน้า 160, 163–164"], nl=["2.3.3-3(1)"]),
        mcq("HEMATO-06-02-4",
            "A 60-year-old woman has fatigue for 1 month. V/S stable. PE: pallor, anicteric sclerae, petechiae and purpura on both legs, no hepatosplenomegaly. CBC: Hb 6.5 g/dL, MCV 94 fL, WBC 3,500/µL (N 25%, L 65%, M 8%), platelet 15,000/µL. What is the most appropriate investigation?",
            "Bone marrow study",
            ["Coagulogram", "ESR and CRP", "Hemoglobin typing", "Serum ferritin"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Pancytopenia ในผู้สูงอายุโดยไม่มีสาเหตุชัด → ต้อง **R/O bone marrow disease** (aplastic anemia, MDS, acute leukemia, infiltration) ด้วย **BM aspiration/biopsy**
- Coagulogram ไม่ช่วยหาสาเหตุ — petechiae อธิบายได้จาก platelet ต่ำ
- ESR/CRP ไม่จำเพาะ
- Hb typing และ ferritin ใช้กับ microcytic anemia — MCV 94 และ WBC/platelet ต่ำด้วย''',
            pearl="Pancytopenia ไม่ทราบสาเหตุ → bone marrow", topic="Pancytopenia work-up",
            ref=[f"{D} หน้า 167–172"], nl=["2.3.3-3(1)", "B2.1.1(1)"]),
    ])

# ---------------------------------------------------------------- 06-03 Acute leukemia
F_HM = fig("hemato-06-03-f1", "แผนที่มะเร็งเม็ดเลือด (overview)", '''<svg viewBox="0 0 740 330">
 <rect x="270" y="10" width="200" height="40" rx="10" class="ac"/>
 <text x="370" y="35" text-anchor="middle" class="tw">Hematologic malignancy</text>
 <path d="M300 50L120 82M340 50L300 82M400 50L460 82M440 50L630 82" class="ln"/>
 <rect x="20" y="84" width="200" height="40" rx="10" class="c1"/>
 <text x="120" y="109" text-anchor="middle" class="tw">Lymphoid (mature)</text>
 <rect x="230" y="84" width="140" height="40" rx="10" class="bad"/>
 <text x="300" y="109" text-anchor="middle" class="tw">Acute leukemia</text>
 <rect x="380" y="84" width="160" height="40" rx="10" class="c2"/>
 <text x="460" y="109" text-anchor="middle" class="tw">MPN</text>
 <rect x="550" y="84" width="170" height="40" rx="10" class="miss"/>
 <text x="635" y="109" text-anchor="middle" class="tw">MDS</text>
 <rect x="20" y="134" width="200" height="186" rx="10" class="c1soft"/>
 <text x="36" y="158" class="tb">Hodgkin lymphoma</text>
 <text x="36" y="176" class="t3">Reed–Sternberg, ลามต่อเนื่อง</text>
 <text x="36" y="204" class="tb">Non-Hodgkin lymphoma</text>
 <text x="36" y="222" class="t3">ลามข้ามกลุ่ม, extranodal</text>
 <text x="36" y="250" class="tb">CLL</text>
 <text x="36" y="268" class="t3">lymphocytosis, smudge cell</text>
 <text x="36" y="296" class="tb">Multiple myeloma</text>
 <text x="36" y="312" class="t3">plasma cell (เสริมจัดกลุ่ม)</text>
 <rect x="230" y="134" width="140" height="186" rx="10" class="badsoft"/>
 <text x="300" y="158" text-anchor="middle" class="tb">ALL</text>
 <text x="300" y="176" text-anchor="middle" class="t3">เด็ก</text>
 <text x="300" y="206" text-anchor="middle" class="tb">AML</text>
 <text x="300" y="224" text-anchor="middle" class="t3">ผู้ใหญ่</text>
 <text x="300" y="262" text-anchor="middle" class="t2">blast &gt; 20%</text>
 <text x="300" y="282" text-anchor="middle" class="t2">ใน BM/PB</text>
 <rect x="380" y="134" width="160" height="186" rx="10" class="c2soft"/>
 <text x="396" y="158" class="tb">BCR-ABL +</text>
 <text x="396" y="178" class="t2">CML</text>
 <text x="396" y="210" class="tb">BCR-ABL −</text>
 <text x="396" y="230" class="t2">PV (Hb ↑)</text>
 <text x="396" y="250" class="t2">ET (Plt ↑)</text>
 <text x="396" y="270" class="t2">PMF (fibrosis)</text>
 <text x="396" y="300" class="t3">JAK2/CALR/MPL</text>
 <rect x="550" y="134" width="170" height="186" rx="10" class="misssoft"/>
 <text x="566" y="158" class="t2">ผู้สูงอายุ</text>
 <text x="566" y="178" class="t2">Cytopenia</text>
 <text x="566" y="198" class="t2">Dysplasia</text>
 <text x="566" y="218" class="t2">Pseudo-Pelger-Huët</text>
 <text x="566" y="246" class="t2">blast &lt; 20%</text>
 <text x="566" y="276" class="t3">เปลี่ยนเป็น AML ได้</text>
</svg>''', "แบ่งตามเซลล์ต้นกำเนิดและความเจริญ: lymphoid ที่โตเต็มที่ · acute (blast > 20%) · MPN (สร้างเกินแต่เซลล์โตเต็มที่) · MDS (สร้างผิดรูป) ตามสไลด์หน้า 279")

S3 = sec("hemato-06-03", "Acute leukemia (AML & ALL)",
    "Blast >20% · AML ผู้ใหญ่ (gum hypertrophy, leukemia cutis) · ALL เด็ก (ปวดกระดูก LN mediastinum CNS) · hyperleukocytosis · tumor lysis", minutes=8,
    source=f"{D} หน้า 279–285, 289–292", nl=["B2.2.4-3(1)", "2.3.3(2)"],
    md='''
### นิยามและกลไก

- **Proliferation of immature WBC (blast)** ในไขกระดูก → เบียดการสร้างเซลล์ปกติ → **pancytopenia** (แม้ WBC รวมอาจสูง)
- **AML** พบบ่อยใน**ผู้ใหญ่** · **ALL** พบบ่อยใน**เด็ก**

[[fig:hemato-06-03-f1]]

### อาการ

| กลุ่ม | อาการ |
|---|---|
| Common | **Anemia** (↓RBC), **bleeding** (↓platelet), **infection/ไข้** (↓mature WBC), **hepatosplenomegaly** (leukemic infiltration) |
| **ALL** | **Bone pain**, lymphadenopathy, **mediastinal mass** (T-ALL), **leukemic meningitis** (CNS) |
| **AML** | **Leukemia cutis (myeloid sarcoma)**, **gum hypertrophy** (M4, M5 monocytic) · DIC ใน APL (M3 — เสริม) |

### การตรวจ

- CBC/PBS: ↓Hb, ↓platelet, **WBC ↓/↔/↑ (± blast)**
- **Diagnosis: blast > 20% ใน BM หรือ PBS** (เกณฑ์ WHO)
- **BM biopsy (confirm)** — ช่วงแรก blast อาจยังไม่ออกมาในเลือด PBS จึงอาจเห็นแค่ pancytopenia
- **Immunophenotype และ genetic studies** → แยก subtype และเลือกการรักษา

### การรักษา

- **Chemotherapy**
- **Supportive**: transfusion, ป้องกันการติดเชื้อ
- **ภาวะแทรกซ้อน**
  - **Hyperleukocytosis (WBC > 100,000)** → leukostasis: สมอง (ซึม) ปอด (เหนื่อย) → **leukapheresis, hydroxyurea**
  - **Tumor lysis syndrome**: AKI, **↑PO4, ↑uric acid, ↑K, ↓Ca** → **IV fluid** (+ allopurinol/rasburicase — เสริม)
  - Febrile neutropenia (ดูหมวด FN)

### Differential diagnosis

- **Aplastic anemia**: ไม่มีตับม้ามโต, pancytopenia + relative lymphocytosis, BM hypocellular fatty
- **Myelophthisis**, **MDS** (หัวข้อถัดไป)

> เด็กไข้ 3 สัปดาห์ + ซีด + **ตับม้ามโต** + pancytopenia (lymphocyte เด่น) = **acute leukemia** · ถ้าไม่มีตับม้ามโตเลยให้นึกถึง aplastic anemia
''',
    figs=[F_HM],
    pearls=[
        "Acute leukemia: blast > 20% ใน BM/PB · BM biopsy ยืนยัน",
        "ALL เด็ก: ปวดกระดูก LN mediastinal mass CNS · AML ผู้ใหญ่: gum hypertrophy, leukemia cutis",
        "Hyperleukocytosis (>100,000) → leukapheresis, hydroxyurea",
        "TLS: ↑K ↑PO4 ↑uric ↓Ca + AKI → IV fluid",
        "Pancytopenia + ตับม้ามโต → leukemia · ไม่มี → aplastic",
    ],
    items=[
        mcq("HEMATO-06-03-1",
            "A 7-year-old girl has had fever for 3 weeks. PE: pallor, systolic ejection murmur grade 2/6, hepatosplenomegaly, bone tenderness of the tibiae. CBC: Hb 7 g/dL, WBC 4,000/µL (N 30%, L 70%), platelet 50,000/µL. What is the most likely diagnosis?",
            "Acute leukemia",
            ["Aplastic anemia", "Infective endocarditis", "Acute rheumatic fever", "Systemic lupus erythematosus"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่ม bone tenderness)",
            explain='''เด็ก + ไข้นาน + ซีด + **ตับม้ามโต** + ปวดกระดูก + pancytopenia (lymphocyte เด่น) = **acute leukemia (ALL)** — SEM เป็น flow murmur จากซีด
- Aplastic anemia **ไม่มีตับม้ามโต** และไม่มีปวดกระดูก
- Infective endocarditis มีไข้ murmur ม้ามโตได้ แต่ไม่ทำให้ pancytopenia แบบนี้ และ WBC มักสูง
- Acute rheumatic fever: ปวดข้อ carditis ไม่มี cytopenia
- SLE มี cytopenia ได้แต่ไม่ค่อยมีตับม้ามโตมากและปวดกระดูก''',
            pearl="เด็ก ไข้ + ตับม้ามโต + pancytopenia = acute leukemia", topic="ALL presentation",
            ref=[f"{D} หน้า 281, 289–290"], nl=["B2.2.4-3(1)"]),
        mcq("HEMATO-06-03-2",
            "A 30-year-old woman has palpitations for 1 month. PE: spleen 1 cm below the left costal margin. CBC: Hb 6.8 g/dL, Hct 22%, MCV 85 fL, WBC 2,300/µL (N 20%, L 73%, M 5%, E 2%), platelet 28,000/µL, nRBC 1/100 WBC. PBS: normochromic normocytic RBC; WBC and platelets decreased. What is the most likely diagnosis?",
            "Acute leukemia",
            ["Aplastic anemia", "Multiple myeloma", "Megaloblastic anemia", "Hereditary spherocytosis"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Pancytopenia + **ม้ามโต** + **NRC** ในเลือด (บ่งว่าไขกระดูกถูกแทรก) = นึกถึง **acute leukemia** (ระยะแรก blast อาจยังไม่ออกในเลือด) → BM biopsy
- Aplastic anemia ไม่มีม้ามโตและไม่มี NRC
- Myeloma: ผู้สูงอายุ CRAB rouleaux
- Megaloblastic: MCV สูง hypersegmented PMN
- HS: hemolysis + spherocyte ไม่มี WBC/platelet ต่ำ''',
            pearl="Pancytopenia + ม้ามโต/NRC → นึกถึง leukemia ไม่ใช่ AA", topic="Leukemia vs AA",
            ref=[f"{D} หน้า 283, 286, 291–292"], nl=["B2.2.4-3(1)"]),
        mcq("HEMATO-06-03-3",
            "A 52-year-old man has fatigue, fever, and swollen bleeding gums for 3 weeks. PE: gingival hypertrophy, several violaceous skin nodules, splenomegaly. CBC: Hb 7.6 g/dL, WBC 46,000/µL with 62% blasts, platelet 22,000/µL. Which diagnosis is most likely?",
            "Acute myeloid leukemia with monocytic differentiation",
            ["Acute lymphoblastic leukemia", "Chronic lymphocytic leukemia", "Chronic myeloid leukemia in chronic phase", "Scurvy"],
            explain='''ผู้ใหญ่ + blast > 20% + **gum hypertrophy** + **leukemia cutis** (skin nodule) = **AML subtype monocytic (M4/M5)** ตามสไลด์
- ALL พบในเด็ก เด่นปวดกระดูก LN mediastinal mass CNS
- CLL เป็น mature lymphocyte ไม่มี blast
- CML chronic phase มี granulocyte ทุกระยะ blast น้อย (< 10%)
- Scurvy ทำให้เหงือกบวมเลือดออก แต่ไม่มี blast''',
            pearl="Gum hypertrophy + leukemia cutis = AML M4/M5", topic="AML features",
            ref=[f"{D} หน้า 281–282"], nl=["B2.2.4-3(1)"]),
        mcq("HEMATO-06-03-4",
            "A 22-year-old man with newly diagnosed acute lymphoblastic leukemia (WBC 180,000/µL) receives induction chemotherapy. On day 2, he has decreased urine output and muscle cramps. Labs: K 6.4 mEq/L, phosphate 8.9 mg/dL, uric acid 14 mg/dL, calcium 6.8 mg/dL, creatinine 3.0 mg/dL. What is the most important initial management?",
            "Aggressive intravenous fluid hydration",
            ["Calcium gluconate infusion to normalize calcium", "Urine alkalinization with sodium bicarbonate", "Oral phosphate binder alone", "Stop all chemotherapy permanently"],
            explain='''**Tumor lysis syndrome**: ↑K, ↑PO4, ↑uric acid, ↓Ca + AKI หลังเคมีบำบัดใน leukemia ที่ WBC สูง → การรักษาหลักตามสไลด์คือ **IV fluid** (+ rasburicase, จัดการ hyperK, dialysis ตามข้อบ่งชี้ — เสริม)
- Calcium ให้เฉพาะเมื่อ hypocalcemia มีอาการรุนแรง/arrhythmia เพราะ Ca × PO4 สูงเสี่ยงตกตะกอน
- Urine alkalinization ไม่แนะนำแล้ว ทำให้ calcium phosphate ตกตะกอนในไต
- Phosphate binder อย่างเดียวไม่พอ
- ไม่ต้องหยุดเคมีบำบัดถาวร''',
            pearl="TLS → IV fluid เป็นหลัก", topic="Tumor lysis syndrome",
            ref=[f"{D} หน้า 285"], nl=["B2.2.4-3(1)", "2.3.4(2)"]),
        mcq("HEMATO-06-03-5",
            "A 35-year-old woman with newly diagnosed AML has WBC 165,000/µL. She becomes drowsy and dyspneic with SpO2 88% on room air; chest x-ray shows diffuse infiltrates. What is the most appropriate immediate management for this complication?",
            "Leukapheresis and hydroxyurea",
            ["Packed red cell transfusion to Hb 10 g/dL", "High-dose furosemide", "Intravenous immunoglobulin", "Platelet transfusion to 100,000/µL"],
            explain='''**Hyperleukocytosis (WBC > 100,000)** → blast อุดหลอดเลือดเล็ก (**leukostasis**) ที่สมอง (ซึม) และปอด (เหนื่อย) → ลดจำนวน blast เร็วด้วย **leukapheresis + hydroxyurea** (ตามด้วยเคมีบำบัด)
- PRC ทำให้ความหนืดเลือดเพิ่ม ควรหลีกเลี่ยงให้มากในช่วง leukostasis
- Furosemide ไม่แก้ leukostasis
- IVIG ไม่เกี่ยว
- Platelet transfusion ให้ตามข้อบ่งชี้ (เช่น < 10,000–20,000) ไม่ได้แก้ปัญหานี้''',
            pearl="WBC > 100k + ซึม/เหนื่อย → leukapheresis + hydroxyurea", topic="Hyperleukocytosis",
            ref=[f"{D} หน้า 285"], nl=["B2.2.4-3(1)"]),
    ])

# ---------------------------------------------------------------- 06-04 MDS & myelophthisis
S4 = sec("hemato-06-04", "Myelodysplastic syndrome & myelophthisis",
    "MDS: ผู้สูงอายุ cytopenia + pseudo-Pelger-Huët + BM blast <20% · myelophthisis: leukoerythroblastic + tear drop → BM biopsy", minutes=5,
    source=f"{D} หน้า 286–288", nl=["B2.2.4-3(1)", "B2.2.4-3(2)"],
    md='''
### Myelodysplastic syndrome (MDS)

- Clonal stem cell disorder → สร้างเม็ดเลือด**ผิดรูป (dysplasia)** และไม่ได้ผล (ineffective) — พบใน**ผู้สูงอายุ**
- PBS: **cytopenia ขึ้นกับ cell line ที่ผิดปกติ** (MCV มักสูง — เสริม)
  - **Pseudo–Pelger-Huët anomaly** (hyposegmented neutrophil, นิวเคลียสสองพู), **hypogranular neutrophil**
  - **Large, hypogranular platelet**
- **BM biopsy: myeloblast < 20%** (≥ 20% = AML) + dysplasia
- เปลี่ยนเป็น AML ได้ · รักษา (เสริม): supportive transfusion, hypomethylating agent, HSCT

### Myelophthisis

- ไขกระดูกถูกแทนที่ด้วยสิ่งแปลกปลอม: **metastatic cancer**, **infection** (TB, fungus), **myelofibrosis**
- CBC: ↓Hb, platelet ↑/↓, WBC ↑/↓
- PBS: **leukoerythroblastic blood picture** = พบตัวอ่อนทุกชนิดในเลือด (polychromasia, **NRC**, **myelocyte**, large platelet) + **tear drop cell**
- **BM biopsy** ยืนยัน (fibrosis ใน myelofibrosis)

| | Aplastic anemia | MDS | Myelophthisis |
|---|---|---|---|
| อายุ | หนุ่มสาว–ทุกวัย | **ผู้สูงอายุ** | มีมะเร็ง/ติดเชื้อเรื้อรัง |
| PBS | pancytopenia + lymphocytosis | **dysplasia (pseudo-Pelger)** | **leukoerythroblastic + tear drop** |
| BM | hypocellular fatty | hyper/normocellular, blast < 20% | infiltration/fibrosis (dry tap) |

> หญิง 65 ปี ซีด 5 เดือน + WBC/platelet ต่ำเล็กน้อย + RDW สูง ไม่มีตับม้ามโต → pancytopenia ในผู้สูงอายุ ต้อง **bone marrow aspiration** (R/O MDS)
''',
    pearls=[
        "MDS: ผู้สูงอายุ + pseudo-Pelger-Huët + hypogranular + blast < 20%",
        "Leukoerythroblastic (NRC + myelocyte) + tear drop = myelophthisis/myelofibrosis",
        "Pancytopenia ในผู้สูงอายุ → BM (R/O MDS)",
    ],
    items=[
        mcq("HEMATO-06-04-1",
            "A 65-year-old woman has anemia for 5 months and was previously healthy. PE: moderate pallor, no hepatosplenomegaly or lymphadenopathy. CBC: Hb 7 g/dL, Hct 20%, MCV 104 fL, RDW 20%, WBC 3,800/µL (PMN 55%), platelet 110,000/µL. PBS: bilobed hypogranular neutrophils and large hypogranular platelets. Serum B12 and folate are normal. What is the most appropriate investigation?",
            "Bone marrow aspiration and biopsy",
            ["Hemoglobin typing", "Direct antiglobulin test", "Liver function tests", "Repeat CBC in 6 months"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่ม PBS dysplasia และ B12/folate ปกติ)",
            explain='''ผู้สูงอายุ + cytopenia หลาย line + macrocytic ที่ B12/folate ปกติ + **pseudo-Pelger-Huët (bilobed hypogranular PMN)** และ large hypogranular platelet = สงสัย **MDS** → ยืนยันด้วย **BM aspiration/biopsy** (dysplasia, นับ blast < 20%)
- Hb typing ใช้กับ microcytic/thalassemia
- DAT ใช้กับ hemolysis — ไม่มีตัวเหลือง/retic สูง
- LFT อธิบาย MCV สูงเล็กน้อยได้ แต่ไม่อธิบาย dysplasia และ cytopenia
- รอ 6 เดือนจะพลาดการวินิจฉัยที่อาจกลายเป็น AML''',
            pearl="Pseudo-Pelger-Huët ในผู้สูงอายุ → BM (MDS)", topic="MDS work-up",
            ref=[f"{D} หน้า 167–168, 288"], nl=["B2.2.4-3(1)"]),
        mcq("HEMATO-06-04-2",
            "A 62-year-old woman with a history of breast cancer has fatigue and back pain. CBC: Hb 8.2 g/dL, WBC 5,400/µL, platelet 92,000/µL. PBS: nucleated red cells, myelocytes and metamyelocytes, teardrop cells, and large platelets. What is the most likely mechanism of her cytopenia?",
            "Bone marrow infiltration by metastatic cancer",
            ["Autoimmune destruction of blood cells", "Vitamin B12 deficiency", "Hypersplenism", "Primary hematopoietic stem cell aplasia"],
            explain='''**Leukoerythroblastic blood picture (NRC + myelocyte) + tear drop cell** ในผู้ป่วยมะเร็งเต้านมที่ปวดหลัง = **myelophthisis** จากมะเร็งแพร่กระจายเข้าไขกระดูก → BM biopsy ยืนยัน
- Autoimmune destruction (ITP/AIHA) ไม่ทำให้ตัวอ่อนออกมาในเลือด
- B12 deficiency ให้ macro-ovalocyte + hypersegmented PMN
- Hypersplenism ต้องมีม้ามโตและไม่ทำให้เกิด leukoerythroblastic picture
- Aplastic anemia ไม่มี NRC/myelocyte และไม่มี tear drop''',
            pearl="NRC + myelocyte + tear drop = myelophthisis", topic="Myelophthisis",
            ref=[f"{D} หน้า 287"], nl=["3.1.2"]),
        mcq("HEMATO-06-04-3",
            "In a patient with suspected myelodysplastic syndrome, which bone marrow finding distinguishes MDS from acute myeloid leukemia?",
            "Myeloblasts fewer than 20%",
            ["Hypocellular fatty marrow", "Myeloblasts more than 20%", "Increased plasma cells more than 10%", "Reed–Sternberg cells"],
            explain='''MDS: ไขกระดูกมี dysplasia แต่ **myeloblast < 20%** · ถ้า **≥ 20%** = AML (MDS เปลี่ยนเป็น AML ได้)
- Hypocellular fatty marrow = aplastic anemia
- Myeloblast > 20% = acute leukemia
- Plasma cell > 10% = multiple myeloma
- Reed–Sternberg cell = Hodgkin lymphoma (ในต่อมน้ำเหลือง)''',
            pearl="Blast < 20% = MDS · ≥ 20% = AML", topic="MDS vs AML",
            ref=[f"{D} หน้า 283, 288"], nl=["B2.2.4-3(1)"]),
    ])

LECTURE = lecture("06", "Bone marrow failure, myeloma & acute leukemia",
    "Multiple myeloma · aplastic anemia · AML/ALL · MDS · myelophthisis",
    objectives=[
        "จำ CRAB และจัดการ hypercalcemia ใน myeloma ได้",
        "แยก pancytopenia จาก aplastic anemia, acute leukemia, MDS และ myelophthisis และรู้ว่าเมื่อไรต้องทำ BM",
        "วินิจฉัย acute leukemia (blast > 20%) และแยก AML กับ ALL จากอาการ",
        "จัดการ hyperleukocytosis และ tumor lysis syndrome ได้",
    ],
    sections=[S1, S2, S3, S4])
