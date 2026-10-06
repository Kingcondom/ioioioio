from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Hemato"

# ---------------------------------------------------------------- 02-01 Hemolysis approach
F_HEM = fig("hemato-02-01-f1", "Hemolysis work-up: ยืนยัน → intra/extravascular → หาสาเหตุ", '''<svg viewBox="0 0 740 430">
 <defs><marker id="hemato-02-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="170" y="10" width="400" height="56" rx="10" class="acsoft"/>
 <text x="370" y="32" text-anchor="middle" class="tb">ซีด + เหลือง → ยืนยัน hemolysis</text>
 <text x="370" y="52" text-anchor="middle" class="t3">↑Retic/polychromasia · ↑LDH · ↑indirect bilirubin · ↑urine urobilinogen</text>
 <path d="M290 66L170 98" class="ln" marker-end="url(#hemato-02-01-a)"/>
 <path d="M450 66L570 98" class="ln" marker-end="url(#hemato-02-01-a)"/>
 <rect x="20" y="100" width="320" height="90" rx="10" class="badsoft"/>
 <text x="180" y="122" text-anchor="middle" class="tb">Intravascular</text>
 <text x="180" y="142" text-anchor="middle" class="t2">↓↓Haptoglobin · hemoglobinuria (ปัสสาวะสีโค้ก)</text>
 <text x="180" y="160" text-anchor="middle" class="t2">urine hemosiderin (เรื้อรัง)</text>
 <text x="180" y="180" text-anchor="middle" class="t3">G6PD · PNH · MAHA · AHTR · cold AIHA · malaria</text>
 <rect x="400" y="100" width="320" height="90" rx="10" class="c2soft"/>
 <text x="560" y="122" text-anchor="middle" class="tb">Extravascular (ม้าม)</text>
 <text x="560" y="142" text-anchor="middle" class="t2">ม้ามโต (กรณีเรื้อรัง) · gallstone</text>
 <text x="560" y="160" text-anchor="middle" class="t2">haptoglobin ลดเล็กน้อย</text>
 <text x="560" y="180" text-anchor="middle" class="t3">warm AIHA · HS · thalassemia</text>
 <path d="M370 190V216" class="ln" marker-end="url(#hemato-02-01-a)"/>
 <rect x="230" y="218" width="280" height="36" rx="8" class="box"/>
 <text x="370" y="241" text-anchor="middle" class="tb">PBS + DAT (Coombs) + MCV</text>
 <path d="M260 254L95 290" class="ln" marker-end="url(#hemato-02-01-a)"/>
 <path d="M320 254L272 290" class="ln" marker-end="url(#hemato-02-01-a)"/>
 <path d="M420 254L468 290" class="ln" marker-end="url(#hemato-02-01-a)"/>
 <path d="M480 254L645 290" class="ln" marker-end="url(#hemato-02-01-a)"/>
 <rect x="10" y="292" width="170" height="126" rx="10" class="box"/>
 <text x="95" y="314" text-anchor="middle" class="ta">Spherocyte</text>
 <text x="95" y="336" text-anchor="middle" class="t2">DAT + → AIHA</text>
 <text x="95" y="356" text-anchor="middle" class="t2">DAT − , ประวัติ</text>
 <text x="95" y="374" text-anchor="middle" class="t2">ครอบครัว → HS</text>
 <text x="95" y="400" text-anchor="middle" class="t3">OF test / EMA</text>
 <rect x="190" y="292" width="170" height="126" rx="10" class="box"/>
 <text x="275" y="314" text-anchor="middle" class="ta">Bite / ghost cell</text>
 <text x="275" y="336" text-anchor="middle" class="t2">Heinz body</text>
 <text x="275" y="356" text-anchor="middle" class="t2">ไข้/ยา/ถั่วปากอ้า</text>
 <text x="275" y="380" text-anchor="middle" class="tb">→ G6PD</text>
 <text x="275" y="400" text-anchor="middle" class="t3">enzyme ซ้ำที่ 2 เดือน</text>
 <rect x="370" y="292" width="170" height="126" rx="10" class="box"/>
 <text x="455" y="314" text-anchor="middle" class="ta">Schistocyte</text>
 <text x="455" y="336" text-anchor="middle" class="t2">+ platelet ต่ำ</text>
 <text x="455" y="356" text-anchor="middle" class="t2">= MAHA</text>
 <text x="455" y="380" text-anchor="middle" class="tb">TTP · HUS · DIC</text>
 <text x="455" y="400" text-anchor="middle" class="t3">ดู PT/aPTT</text>
 <rect x="550" y="292" width="180" height="126" rx="10" class="box"/>
 <text x="640" y="314" text-anchor="middle" class="ta">Microcytic + target</text>
 <text x="640" y="336" text-anchor="middle" class="t2">→ Thalassemia</text>
 <text x="640" y="356" text-anchor="middle" class="t2">(Hb typing)</text>
 <text x="640" y="380" text-anchor="middle" class="ta">Pancytopenia</text>
 <text x="640" y="400" text-anchor="middle" class="t2">+ เช้าปัสสาวะดำ → PNH</text>
</svg>''', "ยืนยัน hemolysis ด้วย retic/LDH/bilirubin แล้วแยก intra- กับ extravascular ก่อน จากนั้นใช้รูปร่างเซลล์ใน PBS ร่วมกับ DAT ชี้สาเหตุ")

S1 = sec("hemato-02-01", "Hemolytic anemia: approach",
    "↑retic ↑LDH ↑indirect bilirubin · intravascular = ↓haptoglobin + hemoglobinuria + urine hemosiderin · extravascular = ม้ามโต", minutes=5,
    source=f"{D} หน้า 10, 55", nl=["2.2.18", "2.3.3-3(6)", "3.3.27"],
    md='''
### หลักฐานว่ามี hemolysis (ทุกชนิด)

- **↑Reticulocyte, ↑polychromasia** (ไขกระดูกตอบสนอง)
- **↑LDH, ↑indirect bilirubin** → ตัวเหลือง
- **↑Urine urobilinogen**

### Intravascular vs extravascular

| | Intravascular | Extravascular |
|---|---|---|
| ที่แตก | ในหลอดเลือด | ใน macrophage ของม้าม/ตับ |
| Haptoglobin | **↓↓** | ↓ เล็กน้อย |
| ปัสสาวะ | **Hemoglobinuria** (สีโค้ก/ดำ) · **urine hemosiderin** (เรื้อรัง) | ปกติ |
| อื่น ๆ | ปวดหลัง/ปวดท้องเฉียบพลัน | **ม้ามโต** (เรื้อรัง), pigment gallstone |
| ตัวอย่าง | G6PD, PNH, MAHA, AHTR, malaria | Warm AIHA, HS, thalassemia |

### จัดกลุ่มสาเหตุตามสไลด์ (acute vs chronic)

| | Intrinsic ต่อ RBC | Extrinsic ต่อ RBC |
|---|---|---|
| **Chronic** | HS, HE, thalassemia, **PNH** | Chronic DIC, prosthetic heart valve dysfunction |
| **Acute** | **G6PD** (oxidative) · hemolytic crisis ใน HbH/HS/HE | **AIHA**, MAHA (DIC, TTP, HUS, HELLP), malaria |

(PNH เป็นความผิดปกติ intrinsic แต่ถูกทำลายด้วย complement — เสริม)

[[fig:hemato-02-01-f1]]

> ไข้ 2–3 วันแล้วปัสสาวะสีโค้ก + ซีดเหลือง ในผู้ชายไทย = นึกถึง **G6PD deficiency with acute hemolysis** ก่อน · ตรวจ **DAT** ทุกเคส hemolysis เพื่อแยก immune (AIHA) ออก
''',
    figs=[F_HEM],
    pearls=[
        "Hemolysis: ↑retic ↑LDH ↑indirect bilirubin ↑urobilinogen",
        "Intravascular: haptoglobin ↓↓ + hemoglobinuria + urine hemosiderin",
        "Extravascular เรื้อรัง → ม้ามโต + pigment gallstone",
        "PBS + DAT ชี้สาเหตุ: spherocyte, bite cell, schistocyte, target cell",
    ],
    items=[
        mcq("HEMATO-02-01-1",
            "A 30-year-old man has anemia with dark brown urine. Urinalysis shows a positive dipstick for blood but no red cells on microscopy. LDH and indirect bilirubin are elevated, and reticulocyte count is 9%. Which additional finding best indicates intravascular hemolysis?",
            "Markedly decreased serum haptoglobin",
            ["Splenomegaly", "Microspherocytes on blood smear", "Elevated urine urobilinogen", "Positive direct antiglobulin test"],
            explain='''Hemoglobin ที่หลุดในหลอดเลือดจับ haptoglobin จนหมด → **haptoglobin ↓↓** ร่วมกับ **hemoglobinuria** (dipstick blood บวกแต่ไม่เห็น RBC) และ urine hemosiderin = intravascular hemolysis
- Splenomegaly เป็นลักษณะ extravascular hemolysis เรื้อรัง
- Microspherocyte พบใน warm AIHA/HS ซึ่งแตกใน**ม้าม**เป็นหลัก
- Urine urobilinogen สูงได้ทั้ง intra- และ extravascular ไม่ช่วยแยก
- DAT บวกบอกว่าเป็น immune-mediated ไม่ได้บอกตำแหน่งที่แตก (warm AIHA ส่วนใหญ่ extravascular)''',
            pearl="Haptoglobin ↓↓ + hemoglobinuria = intravascular", topic="Intra vs extravascular",
            ref=[f"{D} หน้า 55"], nl=["2.2.18"]),
        mcq("HEMATO-02-01-2",
            "A 26-year-old woman has anemia and jaundice. Hb 8 g/dL, MCV 94 fL, reticulocyte 11%, LDH elevated, indirect bilirubin 3.8 mg/dL. PBS shows polychromasia and microspherocytes. What is the most appropriate next investigation?",
            "Direct antiglobulin (Coombs) test",
            ["Hemoglobin typing", "Serum ferritin", "Bone marrow aspiration", "Serum vitamin B12"],
            explain='''มีหลักฐาน hemolysis ชัด (retic สูง LDH สูง indirect bilirubin สูง) + **microspherocyte** → สองโรคหลักคือ **AIHA vs HS** แยกด้วย **DAT** (AIHA บวก, HS ลบ) — ตรวจ DAT ในทุกเคส hemolysis
- Hb typing ใช้กับ microcytic/target cell (thalassemia) แต่ MCV 94
- Serum ferritin ใช้กับ microcytic ที่สงสัย IDA
- Bone marrow ไม่จำเป็น ไขกระดูกตอบสนองดีอยู่แล้ว (retic 11%)
- Serum B12 ใช้กับ macrocytic + retic ต่ำ''',
            pearl="Spherocyte → DAT แยก AIHA กับ HS", topic="Hemolysis work-up",
            ref=[f"{D} หน้า 55, 81, 93"], nl=["3.3.27"]),
        mcq("HEMATO-02-01-3",
            "A 35-year-old man with a mechanical aortic valve replaced 8 years ago has progressive fatigue. Hb 9 g/dL, MCV 92 fL, reticulocyte 6%, LDH 900 U/L, haptoglobin undetectable, platelet 210,000/µL. Echocardiography shows a paravalvular leak. Which finding is most likely on the peripheral blood smear?",
            "Schistocytes",
            ["Bite cells", "Target cells", "Hypersegmented neutrophils", "Teardrop cells"],
            explain='''Prosthetic valve dysfunction (paravalvular leak) ทำให้ RBC ถูกเฉือนด้วยแรงเฉือน = **chronic intravascular (mechanical) hemolysis** ตามที่สไลด์จัดไว้ในกลุ่ม chronic extrinsic → PBS เห็น **schistocyte (fragmented RBC)** · platelet ปกติเพราะไม่ใช่ microthrombi ทั่วร่าง
- Bite cell เป็นของ G6PD (oxidative damage)
- Target cell เป็นของ thalassemia/โรคตับ
- Hypersegmented neutrophil เป็นของ megaloblastic
- Teardrop cell เป็นของ myelofibrosis/myelophthisis''',
            pearl="ลิ้นหัวใจเทียมรั่ว → schistocyte + haptoglobin ต่ำ", topic="Mechanical hemolysis",
            ref=[f"{D} หน้า 10"], nl=["2.3.3-3(6)"]),
    ])

# ---------------------------------------------------------------- 02-02 G6PD
S2 = sec("hemato-02-02", "G6PD deficiency",
    "X-linked · ↓GSH → oxidative hemolysis หลังไข้/ยา/ถั่วปากอ้า · bite/ghost cell + Heinz body · enzyme อาจปกติช่วงแตก → ตรวจซ้ำ 2 เดือน · AKI", minutes=7,
    source=f"{D} หน้า 56–70", nl=["2.3.3(3)", "B2.2.1(3)", "2.2.18"],
    md='''
### กลไก

- **X-linked recessive** → ชาย > หญิง (พบบ่อยในไทย)
- G6PD สร้าง NADPH เพื่อคง **reduced glutathione (GSH)** ซึ่งเป็นตัวป้องกัน oxidative stress
- ขาด G6PD → ↓GSH → Hb ถูก oxidize ตกตะกอนเป็น **Heinz body** → **acute intravascular + extravascular hemolysis**

### ตัวกระตุ้น (trigger)

- **Infection (พบบ่อยที่สุด)** เช่น ไข้ไวรัส
- **Fava beans** (ถั่วปากอ้า)
- **ยา**: antimalarial (**primaquine**), sulfa (**dapsone**, **nitrofurantoin**, co-trimoxazole)

### อาการ

- เกิดฉับพลันหลัง trigger 1–3 วัน: **ปวดหลัง/ปวดท้อง**, ซีด, ตัวเหลือง, **ปัสสาวะสีโค้ก/ดำ**
- ทารก: **neonatal jaundice**
- ตับม้ามมักไม่โต (ต่างจาก thalassemia)

### การตรวจ

| การตรวจ | ผล |
|---|---|
| PBS (Wright) | **Contracted RBC (eccentrocyte/blister cell)**, **bite cell**, **ghost cell**, Hb leakage, polychromasia |
| Supravital stain | **Heinz bodies** |
| Retic | ↑ |
| **G6PD enzyme activity** | **↓ = confirm** |

> G6PD activity **อาจปกติในช่วง acute hemolysis** เพราะเซลล์แก่ที่ขาดเอนไซม์แตกไปหมดแล้ว เหลือ reticulocyte ใหม่ที่มีเอนไซม์มาก → **ตรวจซ้ำหลัง 2 เดือน**

### การรักษา

- **หลีกเลี่ยงและรักษา trigger** (หยุดยา รักษาไข้/การติดเชื้อ)
- **IV fluid** (ป้องกัน AKI จาก hemoglobinuria), **transfusion กรณีรุนแรง**
- ภาวะแทรกซ้อนสำคัญของ acute intravascular hemolysis คือ **AKI** (pigment nephropathy)

> โจทย์ชายหนุ่ม ไข้ 2–3 วัน ได้ยาไม่ทราบชนิด แล้วปัสสาวะดำ + bite cell/ghost cell/Heinz body = G6PD · ไม่ต้องตรวจ Ham test/Coombs/OF test
''',
    pearls=[
        "G6PD: X-linked · trigger = ติดเชื้อ (บ่อยสุด), ถั่วปากอ้า, primaquine, dapsone, nitrofurantoin",
        "Bite cell, ghost cell, blister cell + Heinz body (supravital) = G6PD",
        "Enzyme อาจปกติช่วงแตก (retic เยอะ) → ตรวจซ้ำ 2 เดือน",
        "ภาวะแทรกซ้อนที่ต้องระวัง: AKI → ให้ IV fluid",
    ],
    items=[
        mcq("HEMATO-02-02-1",
            "A 30-year-old man has had fever for 2 days, followed by jaundice and dark urine. PE: pallor, icteric sclerae, no hepatosplenomegaly. CBC: Hb 7.5 g/dL, MCV 90 fL, WBC 12,000/µL, platelet 260,000/µL. PBS: normochromic normocytic RBC, bite cells 1+, ghost cells. What is the most likely diagnosis?",
            "G6PD deficiency",
            ["Autoimmune hemolytic anemia", "Thalassemia", "Paroxysmal nocturnal hemoglobinuria", "Iron deficiency anemia"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ชายหนุ่ม **ไข้ (trigger) → ซีดเหลืองเฉียบพลัน + ปัสสาวะดำ (intravascular)** + PBS **bite cell, ghost cell** = G6PD deficiency with acute hemolysis
- AIHA เด่น **microspherocyte** และ DAT บวก ไม่ใช่ bite/ghost cell
- Thalassemia มี microcytic + target cell + ตับม้ามโต แต่ MCV 90
- PNH มีปัสสาวะดำตอนเช้าเป็นพัก ๆ เรื้อรัง + pancytopenia ไม่ได้สัมพันธ์กับไข้ และไม่มี bite cell
- IDA เป็น microcytic ไม่มี hemolysis''',
            pearl="ไข้ → ปัสสาวะดำ + bite/ghost cell = G6PD", topic="G6PD diagnosis",
            ref=[f"{D} หน้า 61–62"], nl=["2.3.3(3)"]),
        mcq("HEMATO-02-02-2",
            "A 20-year-old man has fatigue for 2 days. PE: pallor, jaundice, no hepatosplenomegaly. CBC: Hb 5.8 g/dL, Hct 18%, WBC 7,500/µL (N 88%), platelet 240,000/µL, MCV 88 fL. PBS: normochromic normocytic RBC with bite cells; supravital stain shows Heinz bodies. What is the most appropriate investigation?",
            "G6PD enzyme activity",
            ["Ham test", "Direct Coombs test", "Osmotic fragility test", "Hemoglobin typing"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Bite cell + **Heinz bodies (supravital)** = oxidative hemolysis → ยืนยันด้วย **G6PD enzyme activity** (ถ้าผลปกติในช่วงแตก ต้องตรวจซ้ำหลัง 2 เดือน)
- Ham test เป็นการตรวจ PNH แบบเก่า (ปัจจุบันใช้ flow cytometry CD55/CD59)
- Direct Coombs test ใช้ยืนยัน AIHA (microspherocyte)
- Osmotic fragility test ใช้กับ HS (spherocyte, ประวัติครอบครัว)
- Hb typing ใช้กับ thalassemia (microcytic)''',
            pearl="Heinz body → ตรวจ G6PD activity", topic="G6PD investigation",
            ref=[f"{D} หน้า 58–59, 67–68"], nl=["2.3.3(3)"]),
        mcq("HEMATO-02-02-3",
            "A 19-year-old man has fever and fatigue for 3 days and takes no medication. PE: pale conjunctivae, moderate jaundice, no hepatosplenomegaly. CBC: Hb 8 g/dL, Hct 24%, WBC 4,200/µL, platelet 154,000/µL. PBS shows blister cells, bite cells, and ghost cells. Urine is cola-colored. Which complication is most likely in this patient?",
            "Acute kidney injury",
            ["Gallstone", "Chronic leg ulcer", "Venous thrombosis", "Opportunistic infection"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''G6PD deficiency with **acute intravascular hemolysis** → hemoglobinuria → **pigment nephropathy/AKI** จึงต้องให้ IV fluid และติดตาม urine output
- Gallstone (pigment) เกิดจาก **chronic** extravascular hemolysis เช่น HS, thalassemia — ไม่ใช่ภาวะเฉียบพลันแบบนี้
- Chronic leg ulcer เป็นของ sickle cell/thalassemia เรื้อรัง
- Venous thrombosis เป็นภาวะแทรกซ้อนเด่นของ **PNH**
- Opportunistic infection เป็นของภูมิคุ้มกันบกพร่อง/neutropenia ไม่เกี่ยว''',
            pearl="G6PD acute hemolysis → ระวัง AKI", topic="G6PD complication",
            ref=[f"{D} หน้า 60, 69–70"], nl=["2.2.18", "2.3.3(3)"]),
        mcq("HEMATO-02-02-4",
            "A 25-year-old man develops pallor, jaundice, and cola-colored urine 2 days after a febrile illness. BT 38°C. CBC: Hb 6.5 g/dL, Hct 19.5%, MCV 90 fL, reticulocyte 8%. Blister cells and Heinz bodies are seen. His G6PD activity measured today is within the normal range. What is the most appropriate interpretation?",
            "Repeat G6PD activity about 2 months after recovery",
            ["G6PD deficiency is excluded", "Perform a direct Coombs test to confirm AIHA", "Diagnose hereditary spherocytosis", "Start prednisolone for presumed immune hemolysis"],
            explain='''ช่วง acute hemolysis เซลล์แก่ที่ขาดเอนไซม์แตกไปแล้ว เหลือ **reticulocyte ใหม่ (retic 8%) ที่มี G6PD สูง** → ผล enzyme อาจปกติลวง → ต้อง **ตรวจซ้ำที่ราว 2 เดือน** ตามสไลด์
- สรุปว่าตัด G6PD ออกแล้วผิด เพราะผลลบลวงพบบ่อยในช่วงนี้
- ภาพ blister cell + Heinz body ชี้ oxidative hemolysis ไม่ใช่ AIHA (ซึ่งเด่น microspherocyte)
- HS ไม่ได้แตกตามไข้แบบเฉียบพลันแล้วปัสสาวะดำ และ PBS เป็น spherocyte
- Prednisolone ไม่มีบทบาทใน G6PD — รักษาด้วย IV fluid หลีกเลี่ยง trigger และให้เลือดถ้ารุนแรง''',
            pearl="G6PD ปกติช่วงแตก ≠ ไม่เป็น → ตรวจซ้ำ 2 เดือน", topic="G6PD false normal",
            ref=[f"{D} หน้า 58, 65–66"], nl=["2.3.3(3)"]),
    ])

# ---------------------------------------------------------------- 02-03 PNH
S3 = sec("hemato-02-03", "Paroxysmal nocturnal hemoglobinuria (PNH)",
    "PIGA → ขาด GPI anchor (CD55, CD59) → complement ทำลาย RBC · ปัสสาวะดำตอนเช้า + pancytopenia + venous thrombosis · flow cytometry", minutes=6,
    source=f"{D} หน้า 71–78", nl=["2.3.3-3(6)", "B2.2.5-3(1)"],
    md='''
### กลไก

- **Acquired** mutation ของ **PIGA gene** ใน hematopoietic stem cell → สร้าง **GPI anchor** ไม่ได้
- โปรตีนที่ยึดด้วย GPI คือ **CD55 (DAF) และ CD59 (MIRL)** ทำหน้าที่ปกป้องเซลล์จาก complement (สไลด์หน้า 71 พิมพ์ "CD99" — ที่ถูกคือ **CD59**)
- ขาด → RBC ถูก complement ทำลาย = **chronic intravascular hemolysis**
- สัมพันธ์กับ **aplastic anemia** และ **MDS** (stem cell disorder)

### อาการ

- ซีด ตัวเหลือง
- **ปัสสาวะสีเข้ม/ดำเป็นพัก ๆ ตอนเช้า** (ปัสสาวะแรกของวัน)
- **Venous thrombosis** (ตำแหน่งแปลก เช่น hepatic vein/Budd–Chiari, mesenteric, cerebral — เสริม) เป็นสาเหตุตายสำคัญ
- **IDA ร่วม** จากเสียเหล็กทางปัสสาวะต่อเนื่อง → MCV อาจต่ำได้

### การตรวจ

- CBC/PBS: **pancytopenia**, polychromasia, ↑retic
- หลักฐาน intravascular hemolysis: LDH สูงมาก, haptoglobin ต่ำ, **urine hemosiderin**
- **Flow cytometry: ↓CD55, CD59 (confirm)** · Ham's test (acidified serum) เป็นวิธีสมัยก่อน
- DAT ลบ

### การรักษา

- อาการน้อย: **observe** + folic acid/iron/transfusion ตามจำเป็น
- **Complement inhibition** (C5 inhibitor: eculizumab, ravulizumab — เสริม)
- Anticoagulation เมื่อมี thrombosis และ HSCT ในบางราย (เสริม)

> โจทย์ pancytopenia + hemolysis + ปัสสาวะดำตอนเช้า ± MCV ต่ำ (IDA ร่วม) = PNH · ถามกลไก → **RBC sensitivity to complement / impaired synthesis of cell surface (GPI) protein**
''',
    pearls=[
        "PNH = PIGA → ขาด GPI anchor → ขาด CD55/CD59 → complement lysis",
        "ปัสสาวะดำตอนเช้า + pancytopenia + venous thrombosis",
        "Confirm: flow cytometry CD55/CD59 (Ham test เป็นของเก่า)",
        "PNH เสียเหล็กทางปัสสาวะ → IDA ร่วม MCV ต่ำได้",
        "สัมพันธ์กับ aplastic anemia และ MDS",
    ],
    items=[
        mcq("HEMATO-02-03-1",
            "A 35-year-old man has passed black urine almost every morning for 6 months without bleeding tendency. PE: moderately pale conjunctivae, mild icteric sclerae, no hepatosplenomegaly. CBC: Hb 6 g/dL, WBC 3,500/µL, platelet 110,000/µL, MCV 102 fL, reticulocyte 10%. Total bilirubin 4.1 mg/dL, direct bilirubin 0.7 mg/dL. Direct Coombs test is negative. What is the most useful investigation?",
            "Flow cytometry for CD55 and CD59",
            ["Hemoglobin typing", "Serum folate level", "G6PD activity", "Osmotic fragility test"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (ปรับ CBC: สไลด์เดิม WBC 5,500 Plt 160,000 MCV 115 — ปรับให้มี cytopenia และ MCV สอดคล้องกับ retic สูง)",
            explain='''ปัสสาวะดำ**ตอนเช้า**เรื้อรัง + hemolysis (retic สูง, indirect bilirubin สูง) + DAT ลบ + cytopenia = **PNH** → confirm ด้วย **flow cytometry ↓CD55/CD59**
- Hb typing ใช้กับ thalassemia (microcytic, target cell) ไม่เข้ากับภาพ
- Serum folate: MCV สูงเล็กน้อยในเคสนี้อธิบายได้จาก reticulocytosis ไม่ใช่ megaloblastic
- G6PD: hemolysis เป็นพัก ๆ ตามไข้/ยา ไม่ใช่ทุกเช้าเป็นเดือน
- OF test ใช้กับ HS ซึ่งเป็น extravascular ไม่มีปัสสาวะดำ''',
            pearl="ปัสสาวะดำทุกเช้า + DAT ลบ → CD55/CD59", topic="PNH diagnosis",
            ref=[f"{D} หน้า 72, 77–78"], nl=["2.3.3-3(6)"]),
        mcq("HEMATO-02-03-2",
            "A 25-year-old man has abdominal pain and dark urine. PE: mild pallor, mild icteric sclerae, no hepatosplenomegaly. CBC: Hb 8 g/dL, Hct 24.2%, MCV 69 fL, RDW 18%, WBC 3,500/µL (N 44%, L 45%), platelet 80,000/µL. Serum ferritin is 9 ng/mL. What is the mechanism of this disease?",
            "Red cell sensitivity to complement",
            ["Red cell enzyme defect", "Hemoglobinopathy", "Defect of the red cell cytoskeleton", "Antibody against red cells"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่ม ferritin ให้เห็น IDA ร่วม)",
            explain='''ปวดท้อง (thrombosis ของหลอดเลือดในช่องท้อง) + ปัสสาวะดำ + **pancytopenia** + microcytic จาก **IDA (เสียเหล็กทางปัสสาวะ)** = PNH → กลไกคือ RBC ขาด CD55/CD59 จึง **ไวต่อ complement**
- Enzyme defect (G6PD) ไม่ทำให้ WBC/platelet ต่ำ
- Hemoglobinopathy (thalassemia) microcytic ได้ แต่ ferritin จะไม่ต่ำและไม่มี pancytopenia
- Cytoskeleton defect (HS) เป็น extravascular มีม้ามโต ไม่มีปัสสาวะดำ
- Antibody ต่อ RBC (AIHA) ไม่อธิบาย pancytopenia และ IDA''',
            pearl="PNH = RBC ไวต่อ complement", topic="PNH mechanism",
            ref=[f"{D} หน้า 71, 73–74"], nl=["2.3.3-3(6)", "B2.2.5-3(1)"]),
        mcq("HEMATO-02-03-3",
            "A 25-year-old man complains of fatigue and dyspnea. He notices red-brown urine at the first void each morning. Which statement best describes the pathogenesis of his condition?",
            "Impaired synthesis of a cell-surface anchor protein",
            ["Cytoskeleton defect", "Ineffective erythropoiesis", "Impaired nuclear maturation", "Valine substituted for glutamate in the beta-globin chain"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ปัสสาวะสีแดงน้ำตาล**ตอนเช้า** = PNH — mutation ของ PIGA ทำให้ **สร้าง GPI anchor ไม่ได้** โปรตีนผิวเซลล์ CD55/CD59 จึงหายไป
- Cytoskeleton defect = HS
- Ineffective erythropoiesis = thalassemia/megaloblastic (เซลล์ตายในไขกระดูก)
- Impaired nuclear maturation = megaloblastic anemia (B12/folate)
- Valine แทน glutamate ใน β-globin = sickle cell disease (HbS)''',
            pearl="PNH: ขาดโปรตีนผิวเซลล์ที่ยึดด้วย GPI", topic="PNH pathogenesis",
            ref=[f"{D} หน้า 71, 75–76"], nl=["2.3.3-3(6)"]),
        mcq("HEMATO-02-03-4",
            "A 32-year-old woman with known PNH presents with abdominal distension, right upper quadrant pain, and rapidly accumulating ascites. Which complication is most likely?",
            "Hepatic vein thrombosis (Budd–Chiari syndrome)",
            ["Pigment gallstone with cholecystitis", "Extramedullary hematopoiesis of the liver", "Hepatic iron overload", "Hepatosplenic lymphoma"],
            explain='''ภาวะแทรกซ้อนเด่นของ PNH ตามสไลด์คือ **venous thrombosis** ซึ่งมักเกิดตำแหน่งแปลก โดยเฉพาะ **hepatic vein (Budd–Chiari)** → ปวด RUQ + ascites เร็ว (เสริมรายละเอียดตำแหน่ง)
- Pigment gallstone เกิดจาก chronic extravascular hemolysis (HS, thalassemia) และไม่ทำให้ ascites
- Extramedullary hematopoiesis พบใน thalassemia/myelofibrosis
- Iron overload พบในผู้ที่รับเลือดบ่อย — PNH กลับเสียเหล็กทางปัสสาวะ
- Lymphoma ไม่เกี่ยว''',
            pearl="PNH + ปวดท้อง/ascites → hepatic vein thrombosis", topic="PNH thrombosis",
            ref=[f"{D} หน้า 71"], nl=["2.3.3-3(6)"]),
    ])

# ---------------------------------------------------------------- 02-04 AIHA
F_AIHA = fig("hemato-02-04-f1", "Warm vs cold AIHA", '''<svg viewBox="0 0 720 300">
 <rect x="20" y="14" width="330" height="44" rx="10" class="bad"/>
 <text x="185" y="42" text-anchor="middle" class="tw">Warm AIHA · IgG · 37°C</text>
 <rect x="370" y="14" width="330" height="44" rx="10" class="c1"/>
 <text x="535" y="42" text-anchor="middle" class="tw">Cold AIHA · IgM · ความเย็น</text>
 <rect x="20" y="66" width="330" height="222" rx="10" class="badsoft"/>
 <text x="36" y="92" class="tb">Extravascular (ม้าม)</text>
 <text x="36" y="116" class="t2">ซีด เหลือง ม้ามโตเล็กน้อย</text>
 <text x="36" y="140" class="t2">PBS: ↑↑microspherocyte, polychromasia</text>
 <text x="36" y="164" class="t2">DAT (IgG ± C3) บวก</text>
 <text x="36" y="192" class="ta">รักษา</text>
 <text x="36" y="214" class="t2">1st: prednisolone</text>
 <text x="36" y="236" class="t2">2nd: rituximab, splenectomy</text>
 <text x="36" y="258" class="t2">folic acid · ให้เลือดเมื่อรุนแรง</text>
 <text x="36" y="278" class="t3">(Hb &lt; 6 หรือ V/S ไม่คงที่)</text>
 <rect x="370" y="66" width="330" height="222" rx="10" class="c1soft"/>
 <text x="386" y="92" class="tb">Extravascular ± intravascular</text>
 <text x="386" y="116" class="t2">อาการเมื่อโดนเย็น · ปัสสาวะสีเข้ม</text>
 <text x="386" y="140" class="t2">Acrocyanosis, livedo reticularis</text>
 <text x="386" y="164" class="t2">PBS: RBC agglutination (MCV สูงลวง)</text>
 <text x="386" y="186" class="t2">DAT (C3) บวก · cold agglutinin titer</text>
 <text x="386" y="214" class="ta">รักษา</text>
 <text x="386" y="236" class="t2">หลีกเลี่ยงความเย็น, folic acid, ให้เลือด</text>
 <text x="386" y="258" class="t2">Rituximab ใน cold agglutinin disease</text>
 <text x="386" y="278" class="t3">steroid มักไม่ได้ผล (เสริม)</text>
</svg>''', "สองชนิดต่างกันที่ชนิดแอนติบอดี ตำแหน่งที่ RBC แตก ภาพ PBS และยาที่ใช้")

S4 = sec("hemato-02-04", "Autoimmune hemolytic anemia (AIHA)",
    "Warm IgG: microspherocyte + DAT บวก → prednisolone · cold IgM: agglutination, acrocyanosis → หลีกเลี่ยงเย็น/rituximab", minutes=7,
    source=f"{D} หน้า 79–92", nl=["2.3.3(4)", "B2.2.2(1)", "3.3.27"],
    md='''
### นิยาม

- **Antibody-mediated hemolysis** — autoantibody จับ RBC
- **Warm-type (IgG)** พบบ่อยกว่า · **cold-type (IgM)**
- สาเหตุทุติยภูมิ (เสริม): SLE, CLL/lymphoma, ยา, การติดเชื้อ (Mycoplasma, EBV สำหรับ cold)

### Warm-type AIHA

- **Extravascular hemolysis** (macrophage ในม้ามกินเซลล์ที่ IgG เกาะ) → ซีด เหลือง **ม้ามโตเล็กน้อย**
- PBS: **↑↑microspherocyte**, polychromasia · ↑retic
- **Direct Coombs test (DCT) = direct antiglobulin test (DAT) บวก**
- รักษา
  - **Prednisolone (1st line)** (เสริม: 1 mg/kg/day)
  - **Rituximab, splenectomy (2nd line)**
  - Supportive: **folic acid**, **transfusion กรณีรุนแรง** (เช่น **Hb < 6 g/dL** หรือ V/S ไม่คงที่)

### Cold-type AIHA

- Extravascular **± intravascular** hemolysis · สัมพันธ์กับ **การโดนความเย็น**
- ซีด เหลือง **ปัสสาวะสีเข้ม**, **acrocyanosis, livedo reticularis**
- PBS: **RBC agglutination**, polychromasia ± microspherocyte · ↑retic · **MCV สูงลวง** (เครื่องนับก้อนเป็นเซลล์ใหญ่)
- DCT บวก + **cold agglutinin titer บวก**
- รักษา: supportive (**หลีกเลี่ยงความเย็น**, folic acid, transfusion) · **rituximab** ใน cold agglutinin disease

[[fig:hemato-02-04-f1]]

### Evans syndrome

- **AIHA + ITP** (ดูหมวด ITP) — รักษาด้วย steroid เช่นกัน

> AIHA vs HS: ทั้งคู่มี microspherocyte — **AIHA ไม่มีประวัติครอบครัว + DCT บวก** · HS มีประวัติครอบครัว + DCT ลบ · โจทย์ MCV 140 + เหลือง + ม้ามโต → ไม่ใช่ megaloblastic (ไม่มีม้ามโต) แต่เป็น **AIHA ที่มี agglutination** → ตรวจ DCT
''',
    figs=[F_AIHA],
    pearls=[
        "Microspherocyte + DAT บวก = AIHA (DAT ลบ + ครอบครัว = HS)",
        "Warm AIHA → prednisolone 1st line · rituximab/splenectomy 2nd",
        "Cold AIHA: acrocyanosis + agglutination + MCV สูงลวง",
        "ให้เลือดใน AIHA เมื่อ Hb < 6 หรือ V/S ไม่คงที่",
    ],
    items=[
        mcq("HEMATO-02-04-1",
            "A 25-year-old Thai man had fever for 1 week that resolved with antipyretics 3 days ago. He now has fatigue. V/S stable. PE: pale conjunctivae, icteric sclerae, otherwise normal. CBC: Hct 25%, WBC 5,000/µL (N 40%, L 60%), platelet 400,000/µL, MCV 96 fL. PBS: microspherocytes 2+, polychromasia 1+. What is the most likely diagnosis?",
            "Autoimmune hemolytic anemia",
            ["G6PD deficiency", "Paroxysmal nocturnal hemoglobinuria", "Thalassemia", "Hereditary spherocytosis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เรียบเรียง PBS ใหม่ให้เด่น microspherocyte)",
            explain='''ผู้ใหญ่ไม่มีประวัติเดิม เกิด hemolysis หลังติดเชื้อ + **microspherocyte** เด่น = **AIHA (warm)** → ยืนยันด้วย DAT
- G6PD ก็เกิดหลังไข้ได้ แต่ PBS เด่น bite/ghost/blister cell และปัสสาวะดำ
- PNH มีปัสสาวะดำตอนเช้าเรื้อรัง + pancytopenia (platelet ที่นี่ 400,000)
- Thalassemia เป็น microcytic + target cell
- HS มี microspherocyte ได้เหมือนกัน แต่เป็นตั้งแต่เด็ก มีประวัติครอบครัว ม้ามโต และ DAT ลบ''',
            pearl="Spherocyte ในผู้ใหญ่ที่ไม่มีประวัติครอบครัว = AIHA จนกว่าจะพิสูจน์", topic="AIHA diagnosis",
            ref=[f"{D} หน้า 83–84"], nl=["2.3.3(4)"]),
        mcq("HEMATO-02-04-2",
            "A 25-year-old woman has anemia and jaundice for 1 week. PE: moderate pallor, mild jaundice, spleen just palpable. CBC: Hb 7 g/dL, Hct 21%, WBC 10,000/µL, platelet 350,000/µL, MCV 140 fL, RDW 22%. What is the most helpful investigation for diagnosis?",
            "Direct Coombs test",
            ["Serum cobalamin level", "Red blood cell folate", "Bone marrow study", "Liver function test"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''MCV 140 สูงเกินจริงจาก **RBC agglutination** + ตัวเหลือง + **ม้ามโต** = AIHA (สไลด์ย้ำว่า megaloblastic **ไม่มี organomegaly**) → ตรวจ **direct Coombs test**
- Serum cobalamin/RBC folate เหมาะกับ megaloblastic ซึ่งมักมี pancytopenia ไม่มีม้ามโต
- Bone marrow study ไม่ใช่ขั้นแรกเมื่อสงสัย immune hemolysis
- LFT ช่วยดูตัวเหลืองแต่ไม่วินิจฉัยสาเหตุของ hemolysis''',
            pearl="MCV สูงมาก + เหลือง + ม้ามโต → DCT (AIHA agglutination)", topic="AIHA with high MCV",
            ref=[f"{D} หน้า 87–88"], nl=["3.3.27"]),
        mcq("HEMATO-02-04-3",
            "A 38-year-old woman has fatigue, moderate pallor, and mild jaundice. Hb 8 g/dL, WBC 9,000/µL, platelet 163,000/µL, MCV 106 fL, reticulocyte 10%. PBS: microspherocytes 1+, polychromasia 2+. Direct antiglobulin test is positive for IgG. Vital signs are stable. What is the most appropriate treatment?",
            "Prednisolone",
            ["PRC transfusion", "Vitamin B12", "Cyclophosphamide", "Intravenous immunoglobulin"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มผล DAT, ปรับ MCV ให้เข้ากับ retic สูง)",
            explain='''Warm AIHA (microspherocyte + DAT IgG บวก) ที่ V/S คงที่ Hb 8 → **prednisolone เป็น 1st line**
- PRC transfusion สำรองไว้กรณีรุนแรง (Hb < 6 หรือ V/S ไม่คงที่) และ crossmatch ยากใน AIHA
- Vitamin B12: MCV สูงจาก reticulocytosis ไม่ใช่ megaloblastic
- Cyclophosphamide เป็นยากดภูมิรุ่นหลังในรายดื้อยา ไม่ใช่ยาแรก
- IVIG ได้ผลน้อยใน AIHA (ใช้ใน ITP มากกว่า)''',
            pearl="Warm AIHA → prednisolone ก่อน", topic="AIHA treatment",
            ref=[f"{D} หน้า 81, 91–92"], nl=["2.3.3(4)"]),
        mcq("HEMATO-02-04-4",
            "A 30-year-old Thai man has pallor. PE: mild pallor, moderate jaundice. CBC: Hct 25%, Hb 8 g/dL, WBC 8,500/µL, platelet 250,000/µL. PBS: polychromasia, microspherocytes. DAT is positive. He has no family history of anemia and stable vital signs. What is the most appropriate management?",
            "Corticosteroid",
            ["Splenectomy", "Intravenous immunoglobulin", "Blood transfusion", "Rituximab"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มผล DAT และประวัติครอบครัว)",
            explain='''Warm AIHA (DAT บวก ไม่มีประวัติครอบครัว จึงไม่ใช่ HS) → **corticosteroid** เป็นยาแรก
- Splenectomy และ rituximab เป็น **2nd line** เมื่อดื้อหรือต้องใช้ steroid ขนาดสูงนาน
- IVIG ไม่ใช่ยาหลักของ AIHA
- Blood transfusion ใช้เมื่อ Hb < 6 หรือ V/S ไม่คงที่ — รายนี้ Hb 8 V/S คงที่''',
            pearl="AIHA: steroid → rituximab/splenectomy", topic="AIHA treatment ladder",
            ref=[f"{D} หน้า 89–90"], nl=["2.3.3(4)"]),
    ])

# ---------------------------------------------------------------- 02-05 HS
S5 = sec("hemato-02-05", "Hereditary spherocytosis (HS)",
    "AD cytoskeleton defect · extravascular · ม้ามโต + pigment gallstone · spherocyte + DAT ลบ · OF test แตกง่าย · splenectomy", minutes=5,
    source=f"{D} หน้า 93–96", nl=["2.3.3-3(3)", "B2.2.1-3(1)"],
    md='''
### กลไก

- **RBC membrane cytoskeletal defect** (spectrin, ankyrin, band 3 — เสริม) → เยื่อหุ้มหลุดเป็นเศษ → RBC กลม (spherocyte) ยืดหยุ่นน้อย → ติดและถูกทำลายในม้าม = **extravascular hemolysis**
- **Autosomal dominant** → **มีประวัติครอบครัว**

### อาการ

- ซีด ตัวเหลือง **ม้ามโต**
- **Pigment gallstone → cholecystitis** (คนอายุน้อยมีนิ่วถุงน้ำดี + ซีด → นึกถึง hemolysis เรื้อรัง)
- Aplastic crisis เมื่อติด parvovirus B19 (เสริม)

### การตรวจ

| การตรวจ | ผล |
|---|---|
| PBS | **Microspherocyte**, polychromasia |
| Retic | ↑ |
| MCV | ปกติ (MCHC สูง — เสริม) |
| **Osmotic fragility (OF) test** | **แตกง่าย (↑fragility)** |
| **EMA binding test** | ลดลง |
| **Direct Coombs test** | **ลบ** |

**OF test**: ใส่ RBC ในน้ำเกลือเจือจางลำดับต่าง ๆ — **HS แตกง่าย** (ทรงกลมพองรับน้ำได้น้อย) · **thalassemia แตกยาก** (เซลล์แบน รับน้ำเข้าได้มาก) — ใช้หลักนี้ใน **DCIP/OF screening ธาลัสซีเมีย**

### การรักษา

- **Folic acid**
- **RBC transfusion** เมื่อซีดมาก
- **Splenectomy** ในรายรุนแรง (ฉีด pneumococcal/Hib/meningococcal vaccine ก่อน — เสริมรายละเอียด)

> **Chronic extravascular hemolysis + นิ่วถุงน้ำดี**: MCV ปกติ → **HS** · MCV ต่ำ → **thalassemia** · AIHA จะไม่มีประวัติครอบครัวและ DCT บวก
''',
    pearls=[
        "HS: AD · microspherocyte + DCT ลบ + ประวัติครอบครัว",
        "OF test: HS แตกง่าย · thalassemia แตกยาก",
        "ซีด + ม้ามโต + นิ่วถุงน้ำดีในคนหนุ่ม → MCV ปกติคิด HS, MCV ต่ำคิด thal",
        "รักษา: folic acid, transfusion, splenectomy",
    ],
    items=[
        mcq("HEMATO-02-05-1",
            "A 32-year-old man has fever with acute RUQ pain. PE: moderately pale conjunctivae, mild icteric sclerae, Murphy sign positive, spleen 3 fingerbreadths below the left costal margin. CBC: Hb 8 g/dL, Hct 24%, WBC 15,000/µL (N 90%), platelet 250,000/µL, MCV 90 fL, RDW 19%. Ultrasound: thickened gallbladder wall with multiple gallstones. What is the most likely cause of his anemia?",
            "Hereditary spherocytosis",
            ["Hb H disease", "Autoimmune hemolytic anemia", "G6PD deficiency with acute hemolysis", "Disseminated intravascular coagulation"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ชายหนุ่มมี **chronic extravascular hemolysis** (ซีด เหลือง ม้ามโต 3 FB) จนเกิด **pigment gallstone + cholecystitis** และ **MCV ปกติ (90)** → HS (สไลด์: ↔MCV → HS, ↓MCV → thalassemia)
- Hb H disease ก็มีม้ามโตและนิ่วได้ แต่ **MCV ต่ำ** (microcytic)
- AIHA เป็นแบบเฉียบพลัน/กึ่งเฉียบพลัน ไม่ค่อยทำให้ม้ามโตมากและมีนิ่วจากการแตกเรื้อรังนาน
- G6PD เป็น intravascular เฉียบพลัน ไม่มีม้ามโต
- DIC เป็นภาวะ consumptive coagulopathy platelet ต่ำ ไม่ใช่สาเหตุของนิ่วและม้ามโต''',
            pearl="ม้ามโต + นิ่วถุงน้ำดี + MCV ปกติ = HS", topic="HS diagnosis",
            ref=[f"{D} หน้า 95–96"], nl=["2.3.3-3(3)"]),
        mcq("HEMATO-02-05-2",
            "A 12-year-old boy has intermittent jaundice and splenomegaly. His mother had a splenectomy for anemia. Hb 9.5 g/dL, MCV 86 fL, reticulocyte 8%. PBS shows many microspherocytes. Direct antiglobulin test is negative. Which test best supports the diagnosis?",
            "Osmotic fragility test",
            ["Hemoglobin typing", "G6PD activity", "Flow cytometry for CD55/CD59", "Cold agglutinin titer"],
            explain='''Spherocyte + **DAT ลบ** + **ประวัติครอบครัว (AD)** + ม้ามโต = HS → ยืนยันด้วย **osmotic fragility test** (แตกง่าย) หรือ EMA binding test
- Hb typing ใช้กับ thalassemia (microcytic, target cell; OF จะ**ลดลง**)
- G6PD activity ใช้เมื่อเห็น bite/ghost cell หลัง trigger
- Flow CD55/CD59 สำหรับ PNH (intravascular, pancytopenia)
- Cold agglutinin titer สำหรับ cold AIHA ซึ่ง DAT จะบวก''',
            pearl="Spherocyte + DAT ลบ + ครอบครัว → OF test/EMA", topic="HS investigation",
            ref=[f"{D} หน้า 93–94"], nl=["2.3.3-3(3)"]),
        mcq("HEMATO-02-05-3",
            "A 20-year-old woman with hereditary spherocytosis requires frequent transfusions and has symptomatic splenomegaly. Splenectomy is planned. Which preparation is most important before surgery?",
            "Vaccination against encapsulated bacteria such as pneumococcus",
            ["Start long-term iron supplementation", "Begin prednisolone 1 mg/kg/day", "Perform bone marrow biopsy", "Start warfarin prophylaxis"],
            explain='''หลังตัดม้ามเสี่ยง **overwhelming post-splenectomy infection** จาก encapsulated bacteria → ฉีด **pneumococcal, Hib (± meningococcal)** อย่างน้อย 2 สัปดาห์ก่อนผ่าตัด (สไลด์ thalassemia ระบุ pneumococcal + Hib ก่อนตัดม้าม)
- Iron supplementation ไม่จำเป็น ผู้ที่รับเลือดบ่อยเสี่ยง iron overload มากกว่า
- Prednisolone ใช้ใน warm AIHA ไม่ใช่ HS
- Bone marrow biopsy ไม่จำเป็นก่อน splenectomy ใน HS (ต่างจาก ITP ที่สไลด์ให้ทำก่อนตัดม้าม)
- Warfarin ไม่ใช่การเตรียมมาตรฐาน''',
            pearl="ก่อน splenectomy: pneumococcal + Hib vaccine", topic="Splenectomy preparation",
            ref=[f"{D} หน้า 93, 99"], nl=["2.3.3-3(3)", "2.3.3-3(5)"]),
    ])

LECTURE = lecture("02", "Hemolytic anemia",
    "Approach · G6PD · PNH · AIHA · hereditary spherocytosis",
    objectives=[
        "ยืนยัน hemolysis และแยก intravascular กับ extravascular จาก lab ได้",
        "วินิจฉัย G6PD deficiency จาก trigger และ PBS และรู้ข้อจำกัดของ enzyme assay ช่วงแตก",
        "นึกถึง PNH เมื่อ hemolysis + pancytopenia + thrombosis และส่ง flow cytometry ได้",
        "แยก AIHA กับ HS ด้วย DAT/ประวัติครอบครัว และเลือกการรักษา AIHA ได้",
    ],
    sections=[S1, S2, S3, S4, S5])
