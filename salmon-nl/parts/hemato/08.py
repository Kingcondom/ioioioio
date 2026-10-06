from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Hemato"

# ---------------------------------------------------------------- 08-01 MPN overview & ET
F_MPN = fig("hemato-08-01-f1", "เปรียบเทียบ MPN: PV · CML · ET · PMF", '''<svg viewBox="0 0 740 360">
 <rect x="20" y="12" width="140" height="44" rx="8" class="sunk"/>
 <rect x="170" y="12" width="132" height="44" rx="8" class="bad"/>
 <text x="236" y="32" text-anchor="middle" class="tw">PV</text>
 <text x="236" y="48" text-anchor="middle" class="tw">JAK2</text>
 <rect x="310" y="12" width="132" height="44" rx="8" class="c2"/>
 <text x="376" y="32" text-anchor="middle" class="tw">CML</text>
 <text x="376" y="48" text-anchor="middle" class="tw">BCR-ABL</text>
 <rect x="450" y="12" width="132" height="44" rx="8" class="c1"/>
 <text x="516" y="32" text-anchor="middle" class="tw">ET</text>
 <text x="516" y="48" text-anchor="middle" class="tw">JAK2/CALR/MPL</text>
 <rect x="590" y="12" width="132" height="44" rx="8" class="miss"/>
 <text x="656" y="32" text-anchor="middle" class="tw">PMF</text>
 <text x="656" y="48" text-anchor="middle" class="tw">JAK2/CALR/MPL</text>
 <text x="90" y="88" text-anchor="middle" class="tb">Hb</text>
 <text x="236" y="88" text-anchor="middle" class="ta">↑↑</text>
 <text x="376" y="88" text-anchor="middle" class="t2">↓ / ↔</text>
 <text x="516" y="88" text-anchor="middle" class="t2">↔</text>
 <text x="656" y="88" text-anchor="middle" class="t2">↓ / ↔</text>
 <text x="90" y="130" text-anchor="middle" class="tb">WBC</text>
 <text x="236" y="130" text-anchor="middle" class="t2">↑ / ↔</text>
 <text x="376" y="130" text-anchor="middle" class="ta">↑↑↑</text>
 <text x="516" y="130" text-anchor="middle" class="t2">↔</text>
 <text x="656" y="130" text-anchor="middle" class="t2">แปรผัน</text>
 <text x="90" y="172" text-anchor="middle" class="tb">Platelet</text>
 <text x="236" y="172" text-anchor="middle" class="t2">↑ / ↔</text>
 <text x="376" y="172" text-anchor="middle" class="t2">แปรผัน</text>
 <text x="516" y="172" text-anchor="middle" class="ta">↑↑↑ (≥ 450k)</text>
 <text x="656" y="172" text-anchor="middle" class="t2">แปรผัน</text>
 <text x="90" y="214" text-anchor="middle" class="tb">ม้ามโต</text>
 <text x="236" y="214" text-anchor="middle" class="t2">+</text>
 <text x="376" y="214" text-anchor="middle" class="ta">++++</text>
 <text x="516" y="214" text-anchor="middle" class="t2">+</text>
 <text x="656" y="214" text-anchor="middle" class="ta">++++</text>
 <text x="90" y="250" text-anchor="middle" class="tb">BM</text>
 <text x="236" y="250" text-anchor="middle" class="t2">↑↑ ทุก line</text>
 <text x="376" y="250" text-anchor="middle" class="t2">↑↑↑ myeloid</text>
 <text x="516" y="250" text-anchor="middle" class="t2">↑↑ megakaryocyte</text>
 <text x="656" y="250" text-anchor="middle" class="t2">fibrosis, dry tap</text>
 <text x="90" y="296" text-anchor="middle" class="tb">จุดเด่น</text>
 <text x="236" y="288" text-anchor="middle" class="t3">คัน หน้าแดง</text>
 <text x="236" y="304" text-anchor="middle" class="t3">SpO2 ปกติ EPO ↓</text>
 <text x="376" y="288" text-anchor="middle" class="t3">Baso/Eo ↑ · LAP ↓</text>
 <text x="376" y="304" text-anchor="middle" class="t3">ม้ามโตตามสัดส่วน WBC</text>
 <text x="516" y="288" text-anchor="middle" class="t3">ปวดหัว ตามัว</text>
 <text x="516" y="304" text-anchor="middle" class="t3">thrombosis</text>
 <text x="656" y="288" text-anchor="middle" class="t3">tear drop + NRC</text>
 <text x="656" y="304" text-anchor="middle" class="t3">ม้ามโตเกินสัดส่วน</text>
 <text x="90" y="342" text-anchor="middle" class="tb">รักษา</text>
 <text x="236" y="342" text-anchor="middle" class="t2">Phlebotomy + ASA</text>
 <text x="376" y="342" text-anchor="middle" class="t2">Imatinib (TKI)</text>
 <text x="516" y="342" text-anchor="middle" class="t2">ASA ± HU</text>
 <text x="656" y="342" text-anchor="middle" class="t2">Ruxolitinib</text>
 <path d="M20 108H722M20 150H722M20 192H722M20 232H722M20 268H722M20 320H722" class="lnf"/>
</svg>''', "อ่านตามแนวตั้ง: แต่ละโรคมีเซลล์ที่เด่นต่างกัน (PV = Hb, CML = WBC, ET = platelet, PMF = fibrosis) · ม้ามโตมาก (++++) คือ CML และ PMF (ตารางสไลด์หน้า 317)")

S1 = sec("hemato-08-01", "Myeloproliferative neoplasms & essential thrombocythemia (ET)",
    "MPN: BCR-ABL (+) CML · (−) PV, ET, PMF · ET: plt ≥450,000, vasomotor sx, thrombosis, JAK2/CALR/MPL · ASA ± hydroxyurea", minutes=6,
    source=f"{D} หน้า 304–307, 317", nl=["B2.2.4-3(2)"],
    md='''
### Myeloproliferative neoplasms (MPN)

- Clonal stem cell disorder ที่**สร้างเซลล์ myeloid เกินแต่เซลล์โตเต็มที่**
- **BCR-ABL positive**: **chronic myeloid leukemia (CML)**
- **BCR-ABL negative**: **essential thrombocythemia (ET)**, **polycythemia vera (PV)**, **primary myelofibrosis (PMF)** — driver mutation **JAK2, CALR, MPL**
- ทุกตัวเปลี่ยนเป็น myelofibrosis/AML ได้

[[fig:hemato-08-01-f1]]

### Essential thrombocythemia (ET)

- **Platelet ≥ 450,000/µL** (ต่อเนื่อง) จาก megakaryocyte ทำงานเกิน
- อาการ
  - **Asymptomatic** (เจอจาก CBC)
  - **Vasomotor symptoms**: ปวดศีรษะ, ตามัว, erythromelalgia (จากการอุดตันหลอดเลือดขนาดเล็ก)
  - **Thromboembolic events** และ petechiae/เลือดออก (platelet ทำงานผิดปกติ; acquired vWD เมื่อ plt > 1 ล้าน — เสริม)
- CBC/PBS: ↑platelet, **large hypogranular platelet**
- **JAK2, CALR, MPL mutation**
- BM biopsy: **↑mature megakaryocytes**
- ต้องแยก **reactive thrombocytosis** ก่อน: IDA, การอักเสบ/ติดเชื้อ, หลังตัดม้าม, มะเร็ง (เสริม)
- **Mx: ป้องกัน thrombosis** — **aspirin**, **hydroxyurea** (high risk: อายุ > 60 หรือเคย thrombosis — เสริม), **IFN-α** (ตั้งครรภ์ — เสริม)
- Complication: เปลี่ยนเป็น **myelofibrosis, AML**

> platelet สูงมาก **อย่าลืม IDA** ซึ่งเป็นสาเหตุ reactive thrombocytosis ที่พบบ่อย — ตรวจ ferritin ก่อนคิด ET
''',
    figs=[F_MPN],
    pearls=[
        "MPN: CML = BCR-ABL (+) · PV, ET, PMF = BCR-ABL (−), JAK2/CALR/MPL",
        "ET: platelet ≥ 450,000 + vasomotor symptoms + thrombosis",
        "ET: aspirin ± hydroxyurea · แยก reactive thrombocytosis (IDA) ก่อน",
    ],
    items=[
        mcq("HEMATO-08-01-1",
            "A 58-year-old woman has recurrent headaches and transient blurred vision. She has no bleeding and no inflammatory disease. Hb 13.2 g/dL, MCV 88 fL, WBC 8,600/µL, platelet 1,050,000/µL on repeated tests. Serum ferritin and CRP are normal. Spleen tip is palpable. BCR-ABL is negative and JAK2 V617F is positive. What is the most likely diagnosis?",
            "Essential thrombocythemia",
            ["Reactive thrombocytosis", "Chronic myeloid leukemia", "Polycythemia vera", "Immune thrombocytopenia"],
            explain='''Platelet ≥ 450,000 ต่อเนื่อง + **vasomotor symptoms** (ปวดหัว ตามัว) + ferritin/CRP ปกติ (ตัด reactive) + **JAK2 บวก BCR-ABL ลบ** + Hb ปกติ = **ET**
- Reactive thrombocytosis ต้องมีสาเหตุ (IDA, อักเสบ, หลังตัดม้าม) — ferritin และ CRP ปกติ
- CML ต้องมี BCR-ABL และ WBC สูงมาก
- PV ต้องมี Hb สูง (> 16–16.5)
- ITP เป็น platelet ต่ำ''',
            pearl="Plt ≥ 450k + JAK2 + Hb/WBC ปกติ = ET", topic="ET diagnosis",
            ref=[f"{D} หน้า 305–306"], nl=["B2.2.4-3(2)"]),
        mcq("HEMATO-08-01-2",
            "A 67-year-old man with essential thrombocythemia (platelet 1,100,000/µL, JAK2 positive) had a transient ischemic attack last year. What is the most appropriate management?",
            "Aspirin plus hydroxyurea",
            ["Observation only", "Platelet apheresis as long-term therapy", "Imatinib", "Phlebotomy to keep hematocrit below 45%"],
            explain='''เป้าหมายรักษา ET คือ**ป้องกัน thrombosis** · ผู้ป่วย **high risk** (อายุ > 60 และเคยมี thrombosis) → **aspirin + cytoreduction ด้วย hydroxyurea** ตามสไลด์ (ASA, hydroxyurea, IFN-α)
- Observation เหมาะกับ low risk ที่ไม่มีอาการเท่านั้น
- Platelet apheresis ใช้ชั่วคราวในภาวะฉุกเฉิน ไม่ใช่ระยะยาว
- Imatinib ใช้กับ CML (BCR-ABL)
- Phlebotomy ใช้กับ PV ที่ Hct สูง''',
            pearl="ET high risk → ASA + hydroxyurea", topic="ET treatment",
            ref=[f"{D} หน้า 306"], nl=["B2.2.4-3(2)", "B2.4(3)"]),
        mcq("HEMATO-08-01-3",
            "A patient has marked leukocytosis with immature granulocytes and splenomegaly. Which test best distinguishes chronic myeloid leukemia from the other myeloproliferative neoplasms?",
            "BCR-ABL (Philadelphia chromosome) testing",
            ["JAK2 V617F mutation", "Serum erythropoietin level", "Bone marrow reticulin stain", "Leukocyte count alone"],
            explain='''MPN แบ่งด้วย **BCR-ABL**: บวก = **CML** · ลบ = PV, ET, PMF (ตามสไลด์หน้า 305)
- JAK2 พบใน PV (~95%) และ ET/PMF (~50–60%) ไม่ใช่ CML
- Serum EPO ใช้แยก PV (ต่ำ) กับ secondary polycythemia
- Reticulin/fibrosis เป็นลักษณะ PMF
- จำนวน WBC อย่างเดียวแยกไม่ได้ (PMF ระยะแรกก็ WBC สูงได้)''',
            pearl="MPN แยก CML ด้วย BCR-ABL", topic="MPN classification",
            ref=[f"{D} หน้า 305"], nl=["B2.2.4-3(2)"]),
    ])

# ---------------------------------------------------------------- 08-02 PV
S2 = sec("hemato-08-02", "Polycythemia vera (PV)",
    "Hb ชาย >16.5 หญิง >16 · SpO2 ปกติ EPO ↓ JAK2 · plethora, aquagenic pruritus, splenomegaly, thrombosis · phlebotomy + ASA ± hydroxyurea", minutes=6,
    source=f"{D} หน้า 308", nl=["B2.2.4-3(2)"],
    md='''
### นิยาม

- MPN ที่ **red cell mass เพิ่ม** โดยไม่ขึ้นกับ EPO (JAK2 V617F ~95% — เสริม)
- **Hb > 16.5 g/dL (ชาย), > 16 g/dL (หญิง)**

### อาการ

- Asymptomatic หรือ **hyperviscosity syndrome**: mucosal bleeding, อาการทางระบบประสาท (ปวดหัว มึน), **ตามัว**
- **Plethora** (หน้าแดงก่ำ), **pruritus** (โดยเฉพาะหลังอาบน้ำอุ่น — aquagenic, เสริม), ความดันสูง, **splenomegaly**
- **Thrombosis** (arterial และ venous เช่น Budd–Chiari) และเลือดออก
- **SpO2 ปกติ**

### การตรวจ

- CBC: **↑Hb**, platelet ↑/↔, WBC ↑/↔ (มักสูงทั้งสาม line)
- **↓EPO**, **JAK2 mutation**
- BM biopsy: **hypercellularity (↑erythropoiesis, ↑granulopoiesis, ↑megakaryopoiesis)** — panmyelosis

### PV vs secondary polycythemia

| | PV | Secondary (เช่น chronic hypoxia) |
|---|---|---|
| SpO2 | **ปกติ** | **↓** (COPD, OSA, cyanotic heart, high altitude) |
| EPO | **↓** | **↑** (หรือปกติสูง; EPO-secreting tumor เช่น RCC — เสริม) |
| WBC/Plt/ม้าม | มักสูง/โต | ปกติ |

### การรักษา (ป้องกัน thrombosis)

- **Phlebotomy** (เป้า Hct < 45% — เสริม)
- **Aspirin** ขนาดต่ำ
- **Hydroxyurea** ใน high risk (อายุ > 60 หรือเคย thrombosis — เสริม)
- Complication: เปลี่ยนเป็น **myelofibrosis, AML**
''',
    pearls=[
        "PV: Hb ชาย >16.5 หญิง >16 + SpO2 ปกติ + EPO ต่ำ + JAK2",
        "Plethora + คันหลังอาบน้ำ + ม้ามโต + thrombosis",
        "Secondary polycythemia: SpO2 ต่ำ EPO สูง",
        "รักษา: phlebotomy + aspirin ± hydroxyurea",
    ],
    items=[
        mcq("HEMATO-08-02-1",
            "A 55-year-old man has headache, dizziness, and generalized itching after warm showers. He does not smoke. PE: facial plethora, BP 150/95 mmHg, spleen 3 cm below the left costal margin. SpO2 98% on room air. CBC: Hb 19.5 g/dL, Hct 59%, WBC 14,000/µL, platelet 620,000/µL. What is the most appropriate next investigation?",
            "JAK2 mutation and serum erythropoietin level",
            ["Arterial blood gas to look for hypoxemia", "BCR-ABL testing", "Hemoglobin electrophoresis", "Bone marrow aspiration for blast count"],
            explain='''Hb สูง + **SpO2 ปกติ** + plethora + **aquagenic pruritus** + **ม้ามโต** + WBC/platelet สูงด้วย = สงสัย **PV** → ตรวจ **JAK2 mutation** และ **serum EPO (ต่ำ)**
- ABG ไม่จำเป็นเมื่อ SpO2 98% ไม่มีโรคปอด (secondary polycythemia จะ SpO2 ต่ำ)
- BCR-ABL ใช้กับ CML ซึ่ง Hb มักต่ำ
- Hb electrophoresis ใช้หา high-affinity Hb ในรายที่เป็นตั้งแต่เด็ก/ครอบครัว (เสริม) ไม่ใช่ขั้นแรก
- Blast count ใช้กับ acute leukemia''',
            pearl="Hb สูง + SpO2 ปกติ + ม้ามโต → JAK2 + EPO", topic="PV work-up",
            ref=[f"{D} หน้า 308"], nl=["B2.2.4-3(2)"]),
        mcq("HEMATO-08-02-2",
            "A 62-year-old man with long-standing COPD has Hb 18.6 g/dL and Hct 56%. SpO2 is 86% on room air. WBC and platelet counts are normal, and there is no splenomegaly. Which pattern is expected?",
            "Elevated serum erythropoietin with no JAK2 mutation",
            ["Low serum erythropoietin with JAK2 mutation", "Low erythropoietin with BCR-ABL fusion", "Normal erythropoietin with panmyelosis in bone marrow", "Elevated erythropoietin with marked splenomegaly"],
            explain='''COPD → **chronic hypoxia (SpO2 86%)** → ไตหลั่ง **EPO ↑** → **secondary polycythemia**: WBC/platelet ปกติ ไม่มีม้ามโต ไม่มี JAK2
- EPO ต่ำ + JAK2 = PV
- BCR-ABL = CML
- Panmyelosis ใน BM เป็นของ PV
- Secondary polycythemia ไม่ทำให้ม้ามโตมาก''',
            pearl="Secondary polycythemia: SpO2 ↓ EPO ↑", topic="PV vs secondary",
            ref=[f"{D} หน้า 308"], nl=["B2.2.4-3(2)"]),
        mcq("HEMATO-08-02-3",
            "A 50-year-old woman is diagnosed with polycythemia vera (Hb 18 g/dL, Hct 55%, JAK2 positive). She has no prior thrombosis. What is the most appropriate initial treatment?",
            "Phlebotomy and low-dose aspirin",
            ["Imatinib", "Ruxolitinib as first-line therapy", "Erythropoietin injection", "Observation until thrombosis occurs"],
            explain='''PV เป้าหมายคือ**ป้องกัน thrombosis** → **phlebotomy** (ลด Hct ให้ < 45%) + **aspirin** ขนาดต่ำ · hydroxyurea เพิ่มในกลุ่ม high risk (อายุ > 60 หรือเคย thrombosis)
- Imatinib ใช้กับ CML
- Ruxolitinib (JAK inhibitor) ใช้ใน PMF หรือ PV ที่ดื้อ/ทนยา hydroxyurea ไม่ได้
- EPO ยิ่งทำให้ Hb สูง
- รอให้เกิด thrombosis ไม่เหมาะ เพราะ thrombosis เป็นสาเหตุตายหลัก''',
            pearl="PV: phlebotomy + aspirin", topic="PV treatment",
            ref=[f"{D} หน้า 308"], nl=["B2.2.4-3(2)"]),
    ])

# ---------------------------------------------------------------- 08-03 PMF
S3 = sec("hemato-08-03", "Primary myelofibrosis (PMF)",
    "Fibrosis → EMH → ม้ามโตมากเกินสัดส่วน WBC · leukoerythroblastic + tear drop · BM dry tap · ระยะแรกคล้าย CML · ruxolitinib", minutes=6,
    source=f"{D} หน้า 309–312, 318–319", nl=["B2.2.4-3(2)"],
    md='''
### กลไก

- MPN ที่ megakaryocyte ผิดปกติหลั่ง cytokine → **fibrosis ในไขกระดูก** → ไขกระดูกสร้างไม่ได้ → **extramedullary hematopoiesis** ที่ม้ามและตับ → **ม้ามโตมาก**
- **Secondary myelofibrosis**: จาก MPN อื่น (post-PV/ET), metastasis, infection

### อาการ

- Asymptomatic · **anemia** · **constitutional symptoms** (ไข้ เหงื่อออก น้ำหนักลด)
- **Hepatosplenomegaly** (LUQ discomfort, **early satiety**) — **ม้ามโตไม่ได้สัดส่วนกับ WBC** (ม้ามโตมากทั้งที่ WBC ไม่สูงมาก)
- Thromboembolic events, petechiae
- เปลี่ยนเป็น acute leukemia ได้

### การตรวจ

- **↑LDH**, **JAK2, CALR, MPL mutation**
- **Prefibrotic stage**: CBC/PBS ↓Hb, ↑platelet, ↑WBC (immature) — **คล้าย CML** · BM hypercellular (↑granulopoiesis), ↓erythropoiesis, ↑atypical megakaryocyte
- **Fibrotic stage (overt PMF)**: ↓Hb, platelet/WBC ↑ หรือ ↓
  - **Leukoerythroblastic blood picture** (polychromasia, **NRC**, **myelocyte**, large platelet) + **tear drop cell**
  - BM biopsy: **dry tap**, severe fibrosis

### การรักษา

- ป้องกัน thrombosis (aspirin), **hydroxyurea**, **transfusion**
- **JAK2 inhibitor (ruxolitinib)** ลดม้ามและอาการ
- (HSCT เป็นทางรักษาหายขาด — เสริม)

> **ม้ามใหญ่มาก (15 cm) + WBC แค่ 25,000 + NRC + tear drop** = PMF · ถ้า **WBC สูงมาก (> 50,000–100,000) ตามสัดส่วนม้าม + basophil ↑** = CML
''',
    pearls=[
        "PMF: ม้ามโตมากไม่ได้สัดส่วนกับ WBC",
        "Leukoerythroblastic + tear drop + BM dry tap = myelofibrosis",
        "ระยะ prefibrotic คล้าย CML → แยกด้วยขนาดม้ามเทียบ WBC และ BCR-ABL",
        "รักษา: ruxolitinib, hydroxyurea, transfusion",
    ],
    items=[
        mcq("HEMATO-08-03-1",
            "A 71-year-old man has LUQ discomfort, early satiety, and fatigue for 1 month. PE: moderate pallor, liver 4 cm and spleen 15 cm below the costal margins. Hct 21%, WBC 25,000/µL (PMN 40%, band 7%, myeloblast 3%, promyelocyte 10%, myelocyte 15%, metamyelocyte 7%, basophil 5%, eosinophil 5%), platelet 950,000/µL, NRC 5/100 WBC. PBS shows many teardrop cells. What is the most likely diagnosis?",
            "Primary myelofibrosis",
            ["Chronic myeloid leukemia", "Essential thrombocythemia", "Myelodysplastic syndrome", "Chronic lymphocytic leukemia"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่ม teardrop cell)",
            explain='''**ม้ามโตมาก (15 cm) แต่ WBC แค่ 25,000** (ไม่ได้สัดส่วน) + ซีด + **NRC + immature granulocyte (leukoerythroblastic)** + tear drop = **primary (idiopathic) myelofibrosis** ตามสไลด์
- CML: ม้ามโตตามสัดส่วนกับ WBC ที่สูงมาก (มัก > 100,000) และ Hb ไม่ต่ำมาก
- ET: platelet สูงแต่ไม่มี leukoerythroblastic picture และม้ามโตเล็กน้อย
- MDS: cytopenia + dysplasia ไม่ใช่ม้ามโตมาก
- CLL: lymphocytosis + smudge cell''',
            pearl="ม้ามโตมาก + WBC ไม่สูงมาก + NRC/tear drop = PMF", topic="PMF vs CML",
            ref=[f"{D} หน้า 309–310, 318–319"], nl=["B2.2.4-3(2)"]),
        mcq("HEMATO-08-03-2",
            "A 66-year-old woman has massive splenomegaly and anemia. PBS shows teardrop cells, nucleated red cells, and myelocytes. Bone marrow aspiration yields a dry tap. JAK2 is positive and BCR-ABL is negative. She has symptomatic splenomegaly with early satiety and night sweats. Which drug is most appropriate to reduce spleen size and symptoms?",
            "Ruxolitinib",
            ["Imatinib", "All-trans retinoic acid", "Prednisolone", "Rituximab"],
            explain='''PMF (dry tap + leukoerythroblastic + tear drop + JAK2) ที่มีม้ามโตและ constitutional symptoms → **JAK2 inhibitor (ruxolitinib)** ตามสไลด์
- Imatinib เป็น TKI สำหรับ BCR-ABL (CML)
- ATRA ใช้ใน APL (AML M3)
- Prednisolone ใช้ใน AIHA/ITP
- Rituximab ใช้ใน B-cell lymphoma/CLL/AIHA''',
            pearl="PMF → ruxolitinib (JAK inhibitor)", topic="PMF treatment",
            ref=[f"{D} หน้า 312"], nl=["B2.2.4-3(2)"]),
        mcq("HEMATO-08-03-3",
            "Which peripheral blood picture is most characteristic of overt primary myelofibrosis?",
            "Leukoerythroblastic picture with teardrop cells",
            ["Small mature lymphocytes with smudge cells", "Macro-ovalocytes with hypersegmented neutrophils", "Microspherocytes with polychromasia", "Bite cells and blister cells"],
            explain='''ไขกระดูกเป็นพังผืด → เซลล์สร้างนอกไขกระดูกและหลุดออกมาเร็ว → **NRC + myelocyte (leukoerythroblastic)** และ RBC ถูกบีบผ่านพังผืดเป็น **tear drop cell**
- Smudge cell = CLL
- Macro-ovalocyte + hypersegmented = megaloblastic
- Microspherocyte = AIHA/HS
- Bite/blister cell = G6PD''',
            pearl="Tear drop + leukoerythroblastic = myelofibrosis", topic="PMF smear",
            ref=[f"{D} หน้า 310–311"], nl=["3.1.2"]),
    ])

# ---------------------------------------------------------------- 08-04 CML
S4 = sec("hemato-08-04", "Chronic myeloid leukemia (CML)",
    "WBC สูงมาก + granulocyte ทุกระยะ + basophil/eosinophil ↑ + ม้ามโตตามสัดส่วน · Ph t(9;22) BCR-ABL · LAP ↓ · imatinib · แยก leukemoid reaction", minutes=8,
    source=f"{D} หน้า 313–329", nl=["B2.2.4-3(1)", "B2.2.4-3(2)"],
    md='''
### กลไก

- **Philadelphia chromosome t(9;22) → BCR-ABL fusion gene** → tyrosine kinase ทำงานตลอด → granulocyte เพิ่มจำนวนทุกระยะ

### อาการและระยะ

- Asymptomatic (เจอ WBC สูงจาก check-up) · anemia · constitutional symptoms
- **Hepatosplenomegaly** (LUQ discomfort, early satiety) — **ม้ามโตตามสัดส่วนกับ WBC**
- ระยะโรค: **chronic phase → accelerated phase → blastic phase** (คล้าย acute leukemia; blast ≥ 20% — เสริม)

### การตรวจ

- CBC/PBS: ↓Hb, **↑↑↑WBC** (มัก > 50,000–100,000) เห็น **granulocyte ทุกระยะ** (myeloblast, promyelocyte, **myelocyte**, metamyelocyte, band, PMN) — myelocyte มากกว่า metamyelocyte (myelocyte bulge — เสริม)
- **↑Basophils, ↑eosinophils** (ช่วยแยกจาก leukemoid reaction)
- Platelet ↑/↔/↓
- **Philadelphia chromosome / BCR-ABL** (ยืนยัน)
- **↓Leukocyte alkaline phosphatase (LAP)**
- BM: hypercellular, ↑myelopoiesis (granulopoiesis เด่น)

### การรักษา

- **Tyrosine kinase inhibitor: imatinib** (รุ่นใหม่ dasatinib, nilotinib — เสริม)
- Hydroxyurea (ลด WBC ระหว่างรอผล), transfusion

### CML vs leukemoid reaction vs PMF

| | CML | Leukemoid reaction | PMF (prefibrotic) |
|---|---|---|---|
| สาเหตุ | BCR-ABL | ติดเชื้อรุนแรง, **hemolysis**, เสียเลือด | JAK2/CALR/MPL |
| Basophil/eosinophil | **↑** | ปกติ | อาจ ↑ |
| LAP | **↓** | **↑** | ปกติ/↑ |
| ม้าม | โต**ตามสัดส่วน** WBC | ไม่โต/เล็กน้อย | โต**เกินสัดส่วน** |

> ข้อสอบเก่า: ชายหนุ่มไข้ 1 วัน ซีด เหลือง WBC 12,000 มี band + metamyelocyte (left shift) — ไม่ใช่ CML แต่เป็น **leukemoid reaction จาก acute hemolysis (G6PD)** → PBS จะพบ **bite cell**
''',
    pearls=[
        "CML: WBC สูงมาก + granulocyte ทุกระยะ + basophil/eosinophil ↑",
        "Ph t(9;22) BCR-ABL · LAP ↓ · imatinib",
        "CML ม้ามโตตามสัดส่วน WBC · PMF เกินสัดส่วน",
        "Leukemoid reaction: LAP ↑ ไม่มี basophilia มีสาเหตุ (ติดเชื้อ, hemolysis)",
    ],
    items=[
        mcq("HEMATO-08-04-1",
            "A 45-year-old man is referred for an abnormal CBC from an annual check-up. PE: spleen 4 cm below the left costal margin. CBC: Hb 12 g/dL, WBC 80,000/µL (N 60%, L 10%, mono 5%, basophil 5%, eosinophil 3%, myelocyte 10%, promyelocyte 5%, myeloblast 2%), platelet 700,000/µL. What is the most likely diagnosis?",
            "Chronic myeloid leukemia",
            ["Leukemoid reaction", "Acute myeloid leukemia", "Essential thrombocythemia", "Non-Hodgkin lymphoma"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ไม่มีอาการ + **WBC 80,000 ที่มี granulocyte ทุกระยะ** + **basophil/eosinophil สูง** + ม้ามโต + platelet สูง = **CML (chronic phase)**
- Leukemoid reaction มีสาเหตุชัด (ติดเชื้อรุนแรง) ไม่มี basophilia และม้ามไม่โต
- AML ต้องมี blast > 20% — ที่นี่แค่ 2%
- ET มี platelet สูงแต่ WBC ไม่สูงขนาดนี้และไม่มี immature granulocyte
- NHL ไม่ทำให้ granulocyte ทุกระยะเพิ่ม''',
            pearl="WBC สูง + myelocyte + basophilia + ม้ามโต = CML", topic="CML diagnosis",
            ref=[f"{D} หน้า 315, 322–323"], nl=["B2.2.4-3(2)"]),
        mcq("HEMATO-08-04-2",
            "A 60-year-old man has fatigue and abdominal fullness. PE: huge splenomegaly. CBC: Hb 10.5 g/dL, WBC 175,000/µL with myelocytes, promyelocytes, metamyelocytes, and band forms; basophils 6%; platelet 480,000/µL. Which test confirms the diagnosis?",
            "BCR-ABL fusion or Philadelphia chromosome",
            ["JAK2 V617F mutation", "Leukocyte alkaline phosphatase score showing high value", "Flow cytometry for CD5/CD23", "Serum protein electrophoresis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เปลี่ยนคำถามจากการวินิจฉัยเป็นการตรวจยืนยัน; เพิ่ม basophil)",
            explain='''ม้ามโตมากตามสัดส่วน + WBC สูงมาก granulocyte ทุกระยะ + basophilia = **CML** → ยืนยันด้วย **BCR-ABL / Philadelphia chromosome t(9;22)**
- JAK2 ใช้กับ PV/ET/PMF
- CML จะมี LAP **ต่ำ** (LAP สูง = leukemoid reaction)
- CD5/CD23 flow ใช้กับ CLL
- SPEP ใช้กับ myeloma''',
            pearl="CML confirm = BCR-ABL", topic="CML investigation",
            ref=[f"{D} หน้า 315, 324–325"], nl=["B2.2.4-3(2)"]),
        mcq("HEMATO-08-04-3",
            "A 48-year-old woman is diagnosed with chronic-phase chronic myeloid leukemia with BCR-ABL positivity. What is the most appropriate first-line therapy?",
            "Imatinib",
            ["Ruxolitinib", "All-trans retinoic acid", "Rituximab", "Phlebotomy"],
            explain='''CML เกิดจาก BCR-ABL tyrosine kinase → รักษาด้วย **tyrosine kinase inhibitor (imatinib)** ตามสไลด์ (hydroxyurea ใช้ลด WBC ชั่วคราว)
- Ruxolitinib เป็น JAK inhibitor สำหรับ PMF
- ATRA ใช้ใน APL
- Rituximab ใช้ใน B-cell malignancy/AIHA
- Phlebotomy ใช้ใน PV''',
            pearl="CML → imatinib", topic="CML treatment",
            ref=[f"{D} หน้า 315"], nl=["B2.2.4-3(2)"]),
        mcq("HEMATO-08-04-4",
            "A 40-year-old man has fatigue and petechiae. PE: splenomegaly 8 cm. CBC: Hct 30%, WBC 128,000/µL (myeloblast 5%, myelocyte 15%, metamyelocyte 25%, band 10%, basophil 8%, lymphocyte 10%, monocyte 4%, neutrophil 23%), platelet 20,000/µL. What is the most likely diagnosis?",
            "Chronic myeloid leukemia",
            ["Acute myeloid leukemia", "Chronic lymphocytic leukemia", "Primary myelofibrosis", "Leukemoid reaction"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (ปรับ differential ให้รวม 100% และเพิ่ม basophil)",
            explain='''WBC สูงมาก (128,000) + **granulocyte ทุกระยะ** + basophilia + ม้ามโต = **CML** · blast 5% (< 20%) จึงยังไม่ใช่ blast crisis/AML · platelet ต่ำอาจบ่งว่าโรคเข้าสู่ระยะลุกลาม (เสริม)
- AML ต้อง blast > 20%
- CLL เป็น mature lymphocyte เด่น
- PMF มี WBC ไม่สูงเท่านี้เทียบกับม้าม และมี NRC/tear drop
- Leukemoid reaction ไม่มี basophilia และไม่มีม้ามโต''',
            pearl="Blast < 20% + granulocyte ทุกระยะ = CML ไม่ใช่ AML", topic="CML vs AML",
            ref=[f"{D} หน้า 313, 326–327"], nl=["B2.2.4-3(2)"]),
        mcq("HEMATO-08-04-5",
            "A 20-year-old man has fever and fatigue for 1 day. BT 38.5°C. PE: mild pallor, mild jaundice, no splenomegaly. CBC: Hb 7 g/dL, Hct 20%, MCV 94 fL, WBC 12,000/µL (neutrophil 69%, band 6%, metamyelocyte 15%, lymphocyte 10%), platelet 240,000/µL. Urine is cola-colored. Which finding is most likely on his peripheral blood smear?",
            "Bite cells",
            ["Blast cells", "Pencil cells", "Basophilic stippling", "Smudge cells"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มปัสสาวะสีโค้ก)",
            explain='''ชายหนุ่มไข้ → ซีด เหลือง ปัสสาวะสีโค้ก MCV ปกติ ไม่มีม้ามโต = **G6PD deficiency with acute hemolysis** · การมี band/metamyelocyte เป็นเพียง **leukemoid reaction/left shift** จาก hemolysis เฉียบพลัน ไม่ใช่ CML → PBS พบ **bite cell**
- Blast cell บ่งบอก acute leukemia — WBC แค่ 12,000 ไม่มีม้ามโต platelet ปกติ
- Pencil cell พบใน IDA (microcytic)
- Basophilic stippling พบใน lead/thalassemia
- Smudge cell พบใน CLL''',
            pearl="Left shift + acute hemolysis = leukemoid reaction (ไม่ใช่ CML)", topic="Leukemoid reaction",
            ref=[f"{D} หน้า 328–329"], nl=["2.3.3(3)"]),
    ])

LECTURE = lecture("08", "Myeloproliferative neoplasms",
    "ET · PV · primary myelofibrosis · CML",
    objectives=[
        "จัดกลุ่ม MPN ตาม BCR-ABL และ driver mutation ได้",
        "วินิจฉัย ET และ PV และแยกจาก reactive thrombocytosis/secondary polycythemia ได้",
        "แยก PMF กับ CML จากขนาดม้ามเทียบ WBC และ PBS (tear drop, basophilia)",
        "เลือกการรักษาหลักของแต่ละ MPN (aspirin/HU, phlebotomy, ruxolitinib, imatinib)",
    ],
    sections=[S1, S2, S3, S4])
