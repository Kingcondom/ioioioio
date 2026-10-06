from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Hemato"

# ---------------------------------------------------------------- 05-01 ITP
F_ITP = fig("hemato-05-01-f1", "ITP: วินิจฉัยแบบคัดออก แล้วรักษาตามระดับ platelet และเลือดออก", '''<svg viewBox="0 0 740 400">
 <defs><marker id="hemato-05-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="150" y="10" width="440" height="56" rx="10" class="acsoft"/>
 <text x="370" y="32" text-anchor="middle" class="tb">Isolated thrombocytopenia (&lt; 100,000)</text>
 <text x="370" y="52" text-anchor="middle" class="t3">WBC/Hb ปกติ · PBS ไม่มี schistocyte · coag ปกติ · ไม่มีตับม้ามโต</text>
 <path d="M370 66V90" class="ln" marker-end="url(#hemato-05-01-a)"/>
 <rect x="120" y="92" width="500" height="58" rx="10" class="box"/>
 <text x="370" y="114" text-anchor="middle" class="tb">R/O secondary ITP ทุกราย: Anti-HIV · HBsAg · Anti-HCV</text>
 <text x="370" y="136" text-anchor="middle" class="t3">ตามสงสัย: ANA/anti-dsDNA (SLE) · H. pylori · LN/BM biopsy (lymphoma, CLL)</text>
 <path d="M370 150V174" class="ln" marker-end="url(#hemato-05-01-a)"/>
 <rect x="230" y="176" width="280" height="36" rx="8" class="sunk"/>
 <text x="370" y="199" text-anchor="middle" class="tb">ต้องรักษาไหม?</text>
 <path d="M290 212L150 244" class="ln" marker-end="url(#hemato-05-01-a)"/>
 <path d="M370 212V244" class="ln" marker-end="url(#hemato-05-01-a)"/>
 <path d="M450 212L590 244" class="ln" marker-end="url(#hemato-05-01-a)"/>
 <rect x="20" y="246" width="230" height="140" rx="10" class="oksoft"/>
 <text x="135" y="270" text-anchor="middle" class="tb">Plt ≥ 30,000</text>
 <text x="135" y="290" text-anchor="middle" class="tb">และไม่มีเลือดออก</text>
 <text x="135" y="320" text-anchor="middle" class="t2">Observe</text>
 <text x="135" y="342" text-anchor="middle" class="t3">นัดติดตาม CBC</text>
 <rect x="260" y="246" width="220" height="140" rx="10" class="misssoft"/>
 <text x="370" y="270" text-anchor="middle" class="tb">Plt &lt; 30,000</text>
 <text x="370" y="290" text-anchor="middle" class="tb">หรือ mild bleeding</text>
 <text x="370" y="320" text-anchor="middle" class="ta">Steroid (1st line)</text>
 <text x="370" y="342" text-anchor="middle" class="t3">prednisolone / dexamethasone</text>
 <text x="370" y="362" text-anchor="middle" class="t3">IVIG ถ้าต้องการผลเร็ว</text>
 <rect x="490" y="246" width="230" height="140" rx="10" class="badsoft"/>
 <text x="605" y="270" text-anchor="middle" class="tb">Life-threatening bleed</text>
 <text x="605" y="290" text-anchor="middle" class="t3">ICH, GI bleed รุนแรง</text>
 <text x="605" y="316" text-anchor="middle" class="ta">IVIG + steroid</text>
 <text x="605" y="338" text-anchor="middle" class="ta">+ platelet transfusion</text>
 <text x="605" y="360" text-anchor="middle" class="t2">± emergency splenectomy</text>
</svg>''', "ITP เป็นการวินิจฉัยแบบคัดออก: CBC เหลือแค่ platelet ต่ำ แล้วตรวจไวรัสทุกราย · ตัดสินใจรักษาที่ platelet 30,000 หรือมีเลือดออก")

S1 = sec("hemato-05-01", "Immune thrombocytopenia (ITP)",
    "Autoantibody · isolated thrombocytopenia · Anti-HIV/HBsAg/Anti-HCV ทุกราย · รักษาเมื่อ plt <30,000 หรือเลือดออก → steroid 1st line · BM เฉพาะ atypical", minutes=9,
    source=f"{D} หน้า 218–244", nl=["2.3.3(5)", "B2.2.2(3)", "2.1.58"],
    md='''
### กลไก

- **Autoantibody ต่อ platelet** → ถูกทำลายในม้าม (และกดการสร้าง — เสริม)
- **Primary ITP (80%)** — มักตามหลัง viral/bacterial infection
- **Secondary ITP**
  - Autoimmune: **SLE**, antiphospholipid syndrome
  - Infection: **HIV, HBV, HCV, H. pylori**
  - Lymphoproliferative: lymphoma, CLL
  - Drugs
  - **Evans syndrome = AIHA + ITP**

### อาการ

- ไม่มีอาการ (เจอจาก CBC)
- **Mucocutaneous bleeding**: bruise, petechiae, purpura, epistaxis, gum bleeding, ประจำเดือนมาก
- รุนแรง: GI bleeding, **CNS bleeding**
- Clue secondary: ผื่น ปวดข้อ ผมร่วง → SLE · constitutional symptoms, ต่อมน้ำเหลืองโต, ตับม้ามโต → lymphoproliferative
- **ITP ไม่ทำให้ม้ามโต** — ถ้าม้ามโตให้หาสาเหตุอื่น (เสริม)

### การตรวจ

- CBC/PBS: **platelet < 100,000/mm³**, **WBC และ RBC ปกติ, ไม่มี schistocyte** (large platelet ได้)
  - เสียเลือดเฉียบพลัน → ซีด retic สูงได้ · **เสียเลือดเรื้อรัง → IDA ร่วม** (microcytic)
  - Evans syndrome → มี spherocyte, DAT บวก
- **Coagulogram ปกติ**
- **R/O secondary ITP: Anti-HIV, HBsAg, Anti-HCV ทุกราย**
- เพิ่มตามสงสัย: ANA/anti-dsDNA (SLE), urea breath test/stool antigen (H. pylori), LN/BM biopsy
- **Bone marrow ไม่จำเป็นโดยทั่วไป** ทำเฉพาะ: **atypical** features, R/O BM disease (เช่น อายุมาก cytopenia อื่น), **refractory to steroid/IVIG**, **ก่อน splenectomy**

[[fig:hemato-05-01-f1]]

### การรักษา

- **ข้อบ่งชี้: platelet < 30,000/mm³ หรือมีเลือดออก**
- **Mild bleeding: steroid (1st line)** (เสริม: prednisolone 1 mg/kg/วัน หรือ dexamethasone 40 mg/วัน × 4 วัน), IVIG
- **Life-threatening bleeding: IVIG + steroid + platelet transfusion ± emergency splenectomy**
- Second line (เสริม): TPO receptor agonist (eltrombopag), rituximab, splenectomy

### Gestational thrombocytopenia (แยกจาก ITP)

- **GA ≥ 20 wk**, dilutional · platelet **100,000–150,000** · ไม่มีเลือดออก → **observe**
- ถ้า platelet ต่ำกว่า 100,000 หรือพบตั้งแต่ไตรมาสแรก → คิดถึง ITP

> โจทย์ "ITP + Hct ต่ำ MCV ต่ำ" = **ITP with IDA** จากประจำเดือนมาก — ยังรักษา ITP ด้วย steroid · platelet transfusion ไม่ใช่การรักษาหลักใน ITP ที่ไม่มีเลือดออกคุกคามชีวิต
''',
    figs=[F_ITP],
    pearls=[
        "ITP: platelet ต่ำอย่างเดียว PBS ไม่มี schistocyte coag ปกติ ไม่มีม้ามโต",
        "ทุกราย: Anti-HIV, HBsAg, Anti-HCV",
        "รักษาเมื่อ plt <30,000 หรือเลือดออก → steroid ก่อน",
        "Life-threatening: IVIG + steroid + platelet transfusion ± splenectomy",
        "Gestational thrombocytopenia: GA ≥20 wk, plt 100–150k → observe",
    ],
    items=[
        mcq("HEMATO-05-01-1",
            "A 30-year-old woman has had petechiae for 3 weeks and occasional gum bleeding. PE: not pale, no jaundice, petechiae and purpura on trunk and extremities, no hepatosplenomegaly. CBC: Hb 12 g/dL, Hct 36%, MCV 82 fL, WBC 4,600/µL (N 65%), platelet 26,000/µL. PBS: decreased platelets, otherwise normal. Anti-HIV, HBsAg, and anti-HCV are negative. What is the most appropriate management?",
            "Prednisolone",
            ["Platelet transfusion", "Splenectomy", "Intravenous cyclophosphamide", "Observation without treatment"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (ปรับ plt จาก 36,000 เป็น 26,000 และเพิ่มผล serology)",
            explain='''Isolated thrombocytopenia + mucocutaneous bleeding + ตัด secondary แล้ว = **primary ITP** · มีข้อบ่งชี้รักษา (**plt < 30,000 และมีเลือดออก**) แต่ไม่คุกคามชีวิต → **steroid (1st line)**
- Platelet transfusion สำรองไว้กรณีเลือดออกรุนแรงคุกคามชีวิต (platelet ถูกทำลายเร็ว)
- Splenectomy เป็น second line/ฉุกเฉิน
- Cyclophosphamide ไม่ใช่ยาแรก
- สังเกตอาการได้เมื่อ plt ≥ 30,000 และไม่มีเลือดออก''',
            pearl="ITP มีเลือดออก/plt <30k → steroid", topic="ITP treatment",
            ref=[f"{D} หน้า 222, 227–228"], nl=["2.3.3(5)"]),
        mcq("HEMATO-05-01-2",
            "A 30-year-old woman has gum bleeding. PE: purpura and ecchymoses; no lymphadenopathy or splenomegaly. CBC: Hb 13 g/dL, WBC 6,800/µL with normal differential, platelet 30,000/µL. PBS: normal except thrombocytopenia. What is the most appropriate investigation?",
            "Anti-HIV",
            ["Dengue serology", "Direct Coombs test", "Bleeding time", "Bone marrow aspiration"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ภาพ ITP (isolated thrombocytopenia, PBS ปกติ) → ต้อง **R/O secondary ITP ทุกราย ด้วย Anti-HIV, HBsAg, Anti-HCV**
- Dengue serology: ไม่มีไข้ จึงไม่ใช่บริบท dengue
- Direct Coombs ใช้เมื่อมี hemolysis (Evans) — Hb ปกติ
- Bleeding time ยาวแน่นอนเมื่อ platelet ต่ำ ไม่ช่วยวินิจฉัย
- Bone marrow ไม่จำเป็นใน ITP ทั่วไป ทำเฉพาะ atypical/refractory/ก่อนตัดม้าม''',
            pearl="ITP → Anti-HIV, HBsAg, Anti-HCV ทุกราย", topic="ITP work-up",
            ref=[f"{D} หน้า 220, 233–234"], nl=["2.3.3(5)"]),
        mcq("HEMATO-05-01-3",
            "A 30-year-old pregnant woman (G1P0) at 8 weeks of gestation attends her first antenatal visit. PE is normal with no bleeding. CBC: Hb 11.5 g/dL, WBC 9,000/µL, platelet 50,000/µL. What is the most likely diagnosis?",
            "Immune thrombocytopenia",
            ["Gestational thrombocytopenia", "HELLP syndrome", "Thrombotic thrombocytopenic purpura", "Dead fetus syndrome"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Platelet **50,000 ตั้งแต่ GA 8 สัปดาห์** = **ITP** (ไม่ใช่ gestational)
- Gestational thrombocytopenia เกิด **GA ≥ 20 สัปดาห์** และ platelet มัก **100,000–150,000**
- HELLP เกิดไตรมาสสาม ร่วมกับ preeclampsia, hemolysis, LFT สูง
- TTP ต้องมี MAHA (schistocyte) + อาการทางระบบประสาท
- Dead fetus syndrome (chronic DIC) เกิดหลังทารกตายในครรภ์นาน และมี coagulopathy''',
            pearl="Plt <100k ตั้งแต่ไตรมาสแรก = ITP ไม่ใช่ gestational", topic="ITP in pregnancy",
            ref=[f"{D} หน้า 223–224"], nl=["2.3.3(5)", "2.3.15-3(11)"]),
        mcq("HEMATO-05-01-4",
            "A 25-year-old woman has dyspnea for 7 days and purpura with gum bleeding for 2 days. PE: moderate pallor, mild icteric sclerae, petechiae on both legs. CBC: Hb 6.5 g/dL, Hct 19%, WBC 5,200/µL, platelet 40,000/µL, reticulocyte 12%. PBS: normochromic normocytic RBC, polychromasia 2+, microspherocytes 2+, no schistocytes. Direct antiglobulin test is positive. What is the most appropriate management?",
            "Dexamethasone",
            ["Plasmapheresis", "Platelet transfusion", "IVIG alone", "Splenectomy"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่ม retic/DAT ให้ชัด)",
            explain='''Warm AIHA (microspherocyte, DAT บวก) **ร่วมกับ** ITP = **Evans syndrome** → รักษาด้วย **corticosteroid** (dexamethasone/prednisolone) ตามสไลด์
- Plasmapheresis ใช้ใน TTP ซึ่งต้องมี **schistocyte** และอาการทางระบบประสาท
- Platelet transfusion ไม่ช่วยและไม่มีเลือดออกคุกคามชีวิต
- IVIG ช่วย ITP ได้แต่ไม่ใช่ตัวหลักสำหรับ AIHA
- Splenectomy เป็นทางเลือกหลังดื้อยา''',
            pearl="Evans (AIHA + ITP) → steroid", topic="Evans syndrome",
            ref=[f"{D} หน้า 218, 237–238"], nl=["2.3.3(5)", "2.3.3(4)"]),
        mcq("HEMATO-05-01-5",
            "A 25-year-old woman has had menses lasting 10 days for 2 months and gum bleeding for 2 weeks. PE: mild pallor, no hepatosplenomegaly or lymphadenopathy, petechiae on all extremities. CBC: Hb 10 g/dL, Hct 30%, WBC 6,000/µL, MCV 71 fL, platelet 10,000/µL. Viral serology is negative. What is the most appropriate management?",
            "Dexamethasone",
            ["Platelet transfusion", "Vincristine", "Azathioprine", "Oral iron alone"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''**ITP with IDA** (เสียเลือดประจำเดือนเรื้อรัง → MCV 71) · platelet 10,000 + มีเลือดออก → รักษา ITP ด้วย **corticosteroid** (dexamethasone) และให้เหล็กเสริมด้วย
- Platelet transfusion ไม่ใช่การรักษาหลักใน ITP ที่ไม่มีเลือดออกคุกคามชีวิต
- Vincristine และ azathioprine เป็นยาสำหรับ refractory ITP
- เหล็กอย่างเดียวไม่แก้ thrombocytopenia ที่เป็นต้นเหตุของการเสียเลือด''',
            pearl="ITP + IDA → steroid (+ เหล็ก)", topic="ITP with IDA",
            ref=[f"{D} หน้า 239–240, 243–244"], nl=["2.3.3(5)"]),
    ])

# ---------------------------------------------------------------- 05-02 APDE
S2 = sec("hemato-05-02", "Acquired platelet dysfunction with eosinophilia (APDE)",
    "เด็ก · bruise/epistaxis · eosinophil สูง · platelet count ปกติ แต่ BT ยาว · หาพยาธิ · หายเองใน 6–12 เดือน", minutes=4,
    source=f"{D} หน้า 245–249", nl=["B2.2.5-3(2)", "2.3.3-3(2)"],
    md='''
### ลักษณะ

- โรคที่พบในไทย/เอเชียตะวันออกเฉียงใต้ (เสริม) **พบบ่อยในเด็ก**
- **Easy bruise, ecchymosis, epistaxis** (primary hemostatic bleeding) โดยที่ร่างกายแข็งแรงดี
- สัมพันธ์กับการติดพยาธิ (เสริม: สารจากพยาธิ/eosinophil ทำให้ platelet ทำงานผิดปกติ)

### การตรวจ

- CBC/PBS: **↑eosinophil**
- **Platelet count ปกติ** · บางตัว **pale stain/giant platelet**
- **↑Bleeding time**
- **Stool for parasite**
- PT/aPTT ปกติ (เสริม)

### การรักษา

- **Self-limited ใน 6–12 เดือน**
- **Antiparasite** กรณีตรวจพบพยาธิ
- **Platelet transfusion กรณี severe bleeding**

> เด็กมี bruise ตามแขนขา + **eosinophil สูง** + **platelet ปกติ** = APDE · ข้อสอบเก่าในสไลด์ (หญิง 35 ปี เลือดออกนานหลังถอนฟัน platelet ปกติ มี eosinophil) ถามการรักษา — ตามแนวสไลด์ถ้าเลือดออกรุนแรงคือ **platelet transfusion** (ตัวเลือก DDAVP ใช้กับ vWD)
''',
    pearls=[
        "APDE: เด็ก + bruise + eosinophilia + platelet count ปกติ + BT ยาว",
        "ตรวจ stool parasite → ให้ยาถ่ายพยาธิ",
        "หายเองใน 6–12 เดือน · เลือดออกรุนแรงให้ platelet transfusion",
    ],
    items=[
        mcq("HEMATO-05-02-1",
            "A 5-year-old boy has spontaneous bruises on the upper and lower extremities for 2 weeks. PE is otherwise normal. CBC: Hb 12 g/dL, WBC 12,000/µL with eosinophils 25%, platelet 280,000/µL. PBS shows some pale-staining giant platelets. PT and aPTT are normal; bleeding time is prolonged. What is the most likely diagnosis?",
            "Acquired platelet dysfunction with eosinophilia",
            ["Immune thrombocytopenia", "Hemophilia A", "Acute lymphoblastic leukemia", "Henoch–Schönlein purpura"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เขียนผล PBS เป็นข้อความ)",
            explain='''เด็กมี bruise + **eosinophilia** + **platelet count ปกติ** แต่ **BT ยาว** + pale/giant platelet = **APDE** → ตรวจ stool parasite
- ITP ต้อง platelet ต่ำ
- Hemophilia A ทำให้ aPTT ยาว BT ปกติ และเด่น hemarthrosis
- ALL มี cytopenia/blast และตับม้ามโต ต่อมน้ำเหลืองโต
- HSP เป็น palpable purpura ที่ขา + ปวดท้อง ปวดข้อ platelet และ BT ปกติ''',
            pearl="Bruise + eosinophilia + platelet ปกติ = APDE", topic="APDE diagnosis",
            ref=[f"{D} หน้า 245–247"], nl=["B2.2.5-3(2)"]),
        mcq("HEMATO-05-02-2",
            "A 7-year-old girl is diagnosed with acquired platelet dysfunction with eosinophilia after presenting with easy bruising. She has no active bleeding. Stool examination shows hookworm ova. What is the most appropriate management?",
            "Give an antihelminthic drug and reassure that it is usually self-limited",
            ["Platelet transfusion now", "Prednisolone 1 mg/kg/day", "Intravenous immunoglobulin", "Bone marrow aspiration"],
            explain='''APDE **หายเองใน 6–12 เดือน** · พบพยาธิจึงให้ **ยาถ่ายพยาธิ** · platelet transfusion สำรองไว้กรณีเลือดออกรุนแรงเท่านั้น
- Platelet transfusion ตอนนี้ไม่จำเป็นเพราะไม่มีเลือดออก
- Prednisolone และ IVIG เป็นการรักษา ITP (immune) ไม่ใช่ APDE ซึ่ง platelet count ปกติ
- Bone marrow ไม่จำเป็นเพราะ CBC ไม่มี cytopenia/blast''',
            pearl="APDE: ถ่ายพยาธิ + รอหาย 6–12 เดือน", topic="APDE management",
            ref=[f"{D} หน้า 245"], nl=["B2.2.5-3(2)"]),
        mcq("HEMATO-05-02-3",
            "A 35-year-old woman has prolonged bleeding after a tooth extraction that continues despite local pressure, and new ecchymoses on her legs. Platelet count 250,000/µL with 15% eosinophils; PT, aPTT, vWF antigen and activity are normal. Bleeding time is prolonged. What is the most appropriate management to control the bleeding?",
            "Platelet transfusion",
            ["Fresh frozen plasma", "Factor VIII concentrate", "Desmopressin (DDAVP)", "Cryoprecipitate"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มผล vWF ปกติให้ตัด vWD ออก — เฉลยเดิมเป็นภาพ)",
            explain='''Platelet count ปกติแต่**ทำงานผิดปกติ** (BT ยาว) ร่วมกับ eosinophilia = **APDE** · เลือดออกไม่หยุด → ให้ **platelet transfusion** ตามสไลด์ (เกล็ดเลือดใหม่ทำงานได้)
- FFP และ cryoprecipitate แก้ปัญหา factor/fibrinogen ซึ่ง PT/aPTT ปกติ
- Factor VIII concentrate ใช้ใน hemophilia A
- DDAVP เพิ่ม vWF/VIII ใช้ใน vWD และ mild hemophilia A — vWF ปกติในรายนี้
(สไลด์เฉลยเป็นภาพ อ่านไม่ได้ — ข้อนี้ตอบตามแนวสไลด์ APDE)''',
            pearl="APDE เลือดออกมาก → platelet transfusion", topic="APDE bleeding",
            ref=[f"{D} หน้า 245, 248–249"], nl=["B2.2.5-3(2)", "B2.4(1)"]),
    ])

# ---------------------------------------------------------------- 05-03 MAHA, TTP, HUS
F_TMA = fig("hemato-05-03-f1", "ITP vs TTP vs HUS vs DIC", '''<svg viewBox="0 0 740 330">
 <rect x="20" y="12" width="150" height="40" rx="8" class="sunk"/>
 <rect x="180" y="12" width="128" height="40" rx="8" class="c1"/>
 <text x="244" y="37" text-anchor="middle" class="tw">ITP</text>
 <rect x="316" y="12" width="128" height="40" rx="8" class="c2"/>
 <text x="380" y="37" text-anchor="middle" class="tw">TTP</text>
 <rect x="452" y="12" width="128" height="40" rx="8" class="miss"/>
 <text x="516" y="37" text-anchor="middle" class="tw">HUS</text>
 <rect x="588" y="12" width="132" height="40" rx="8" class="bad"/>
 <text x="654" y="37" text-anchor="middle" class="tw">DIC</text>
 <text x="95" y="84" text-anchor="middle" class="tb">↓Platelet</text>
 <text x="244" y="84" text-anchor="middle" class="ta">ใช่</text>
 <text x="380" y="84" text-anchor="middle" class="ta">ใช่</text>
 <text x="516" y="84" text-anchor="middle" class="ta">ใช่</text>
 <text x="654" y="84" text-anchor="middle" class="ta">ใช่</text>
 <text x="95" y="122" text-anchor="middle" class="tb">MAHA</text>
 <text x="95" y="138" text-anchor="middle" class="t3">(schistocyte)</text>
 <text x="244" y="128" text-anchor="middle" class="t2">ไม่มี</text>
 <text x="380" y="128" text-anchor="middle" class="ta">มี</text>
 <text x="516" y="128" text-anchor="middle" class="ta">มี</text>
 <text x="654" y="128" text-anchor="middle" class="ta">มี</text>
 <text x="95" y="172" text-anchor="middle" class="tb">↑PT / aPTT</text>
 <text x="95" y="188" text-anchor="middle" class="t3">↓fibrinogen ↑D-dimer</text>
 <text x="244" y="178" text-anchor="middle" class="t2">ไม่</text>
 <text x="380" y="178" text-anchor="middle" class="t2">ไม่</text>
 <text x="516" y="178" text-anchor="middle" class="t2">ไม่</text>
 <text x="654" y="178" text-anchor="middle" class="ta">ใช่</text>
 <text x="95" y="230" text-anchor="middle" class="tb">Clue</text>
 <text x="244" y="222" text-anchor="middle" class="t2">CBC อื่นปกติ</text>
 <text x="244" y="240" text-anchor="middle" class="t3">หลังติดเชื้อ</text>
 <text x="380" y="222" text-anchor="middle" class="t2">ไข้ + ซึม/อ่อนแรง</text>
 <text x="380" y="240" text-anchor="middle" class="t3">ADAMTS13 ↓</text>
 <text x="516" y="222" text-anchor="middle" class="t2">เด็ก + ท้องเสียเป็นเลือด</text>
 <text x="516" y="240" text-anchor="middle" class="t3">ไตวายเด่น</text>
 <text x="654" y="222" text-anchor="middle" class="t2">Sepsis, OB, trauma</text>
 <text x="654" y="240" text-anchor="middle" class="t3">เลือดซึมทุกที่</text>
 <text x="95" y="290" text-anchor="middle" class="tb">รักษา</text>
 <text x="244" y="290" text-anchor="middle" class="t2">Steroid</text>
 <text x="380" y="282" text-anchor="middle" class="ta">Plasma exchange</text>
 <text x="380" y="300" text-anchor="middle" class="t3">(ด้วย FFP)</text>
 <text x="516" y="282" text-anchor="middle" class="t2">Supportive</text>
 <text x="516" y="300" text-anchor="middle" class="t3">IV fluid, RRT</text>
 <text x="654" y="282" text-anchor="middle" class="t2">รักษาสาเหตุ</text>
 <text x="654" y="300" text-anchor="middle" class="t3">+ blood product</text>
 <path d="M20 104H720M20 152H720M20 202H720M20 260H720" class="lnf"/>
</svg>''', "ไล่จากบนลงล่าง: ทุกโรค platelet ต่ำ → มี schistocyte ไหม (ITP ไม่มี) → PT/aPTT ยาวไหม (เฉพาะ DIC) → แยก TTP กับ HUS ด้วยอาการนำ")

S3 = sec("hemato-05-03", "MAHA: TTP & HUS",
    "Schistocyte + ↓plt + coag ปกติ · TTP: ADAMTS13 ↓, pentad, ซึม → plasma exchange (ห้าม platelet) · HUS: เด็ก EHEC O157:H7 ท้องเสียเป็นเลือด → supportive", minutes=8,
    source=f"{D} หน้า 250–252, 255, 266–275", nl=["2.3.3-3(6)", "B2.2.5-3(1)"],
    md='''
### Microangiopathic hemolytic anemia (MAHA)

- **Microthrombi อุดหลอดเลือดเล็ก** → RBC ถูกเฉือน → **intravascular hemolysis + schistocyte + ↓platelet (ถูกใช้)**
- สาเหตุ: **TTP, HUS, DIC**, HELLP syndrome, hypertensive emergency
- อาการ: ซีด เหลือง **อวัยวะล้มเหลวจาก microthrombi**, petechiae
- CBC/PBS: ↓Hb, ↓platelet, **↑schistocyte** (+ LDH สูง haptoglobin ต่ำ)

### Thrombotic thrombocytopenic purpura (TTP)

- **ADAMTS13 deficiency/inhibition** (ส่วนใหญ่เป็น autoantibody — เสริม) — ปกติ ADAMTS13 ตัด **vWF multimer** ให้สั้น
- ขาด → **ultra-large vWF** → platelet เกาะ → microthrombi → schistocyte
- **Pentad**: **fever, neurologic symptoms (ซึม สับสน อ่อนแรงครึ่งซีก), ↓platelet, MAHA, ↓renal function** (ไม่จำเป็นต้องครบ)
- **Coagulogram ปกติ** · **↓ADAMTS13 activity** (< 10% — เสริม)
- **Tx: plasma exchange with FFP** (ฉุกเฉิน) ± steroid, caplacizumab (เสริม)
- **ห้ามให้ platelet transfusion** ถ้าไม่มีเลือดออกคุกคามชีวิต (เพิ่ม thrombosis — เสริม)

### Hemolytic uremic syndrome (HUS)

- **เด็ก** · **Shiga-like toxin จาก EHEC O157:H7**
- นำด้วย **bloody diarrhea 5–10 วัน** ก่อน
- **Triad: MAHA, ↓platelet, ↓renal function (AKI)**
- **Coagulogram ปกติ**
- **Tx: supportive** — IV fluid, **RRT ถ้ามีข้อบ่งชี้** (ไม่ให้ยาปฏิชีวนะใน EHEC — เสริม)

[[fig:hemato-05-03-f1]]

> Schistocyte + platelet ต่ำ + **PT/aPTT ปกติ** = TTP/HUS · ถ้า **PT/aPTT ยาว** = DIC · มี **ซึม/อ่อนแรงครึ่งซีก + ไข้** → TTP → plasma exchange
''',
    figs=[F_TMA],
    pearls=[
        "MAHA = schistocyte + platelet ต่ำ: TTP, HUS, DIC, HELLP, HT emergency",
        "TTP: ADAMTS13 ↓ · ไข้ + neuro + MAHA + plt ต่ำ + ไต · coag ปกติ",
        "TTP → plasma exchange with FFP (ไม่ให้ platelet)",
        "HUS: เด็ก + bloody diarrhea (EHEC O157:H7) + AKI → supportive",
    ],
    items=[
        mcq("HEMATO-05-03-1",
            "A 45-year-old man presents with confusion. BT 39°C, other vital signs stable. PE: petechiae, purpura, subtle right-sided weakness. CBC: Hb 7 g/dL, Hct 21%, WBC 10,200/µL, platelet 20,000/µL. PT/INR and aPTT are normal. PBS: numerous schistocytes and polychromasia. What is the most likely diagnosis?",
            "Thrombotic thrombocytopenic purpura",
            ["Disseminated intravascular coagulation", "Immune thrombocytopenic purpura", "Hemolytic uremic syndrome", "Evans syndrome"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เขียนผล PBS เป็นข้อความ)",
            explain='''**Fever + neurologic deficit + thrombocytopenia + MAHA (schistocyte) + coag ปกติ** = **TTP**
- DIC มี schistocyte ได้แต่ **PT/aPTT ยาว** และมีสาเหตุนำ (sepsis)
- ITP ไม่มี schistocyte/hemolysis และไม่มีอาการทางสมองจาก microthrombi
- HUS พบในเด็กหลังท้องเสียเป็นเลือด เด่นไตวาย
- Evans syndrome เป็น AIHA + ITP — spherocyte DAT บวก ไม่ใช่ schistocyte''',
            pearl="ไข้ + ซึม/อ่อนแรง + schistocyte + coag ปกติ = TTP", topic="TTP diagnosis",
            ref=[f"{D} หน้า 251, 266–267"], nl=["2.3.3-3(6)"]),
        mcq("HEMATO-05-03-2",
            "A 40-year-old woman has confusion, anemia, and mild jaundice for 3 days. CBC: Hb 7 g/dL, Hct 21%, WBC 18,000/µL, platelet 7,000/µL, MCV 95 fL, RDW 29%. PBS: schistocytes 2+. PT and aPTT are normal. LDH is 1,450 U/L. What is the most appropriate management?",
            "Plasma exchange",
            ["Platelet transfusion", "Prednisolone alone", "Intravenous immunoglobulin", "Fresh frozen plasma transfusion only after ADAMTS13 results"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ภาพ **TTP** (ซึม + MAHA + platelet ต่ำมาก + coag ปกติ) → **plasma exchange with FFP ทันที** (เอา autoantibody ออก และเติม ADAMTS13) ไม่ต้องรอผล ADAMTS13
- Platelet transfusion อาจทำให้ thrombosis แย่ลง หลีกเลี่ยงถ้าไม่มีเลือดออกคุกคามชีวิต
- Prednisolone ใช้ร่วมได้แต่ไม่ใช่การรักษาหลัก
- IVIG ใช้ใน ITP
- FFP infusion ใช้ชั่วคราวได้ถ้าเปลี่ยน plasma ไม่ได้ทันที แต่การรอผล ADAMTS13 ก่อนรักษาผิดหลัก (TTP ไม่รักษาตายสูง)''',
            pearl="สงสัย TTP → plasma exchange เลย", topic="TTP treatment",
            ref=[f"{D} หน้า 251, 270–271"], nl=["2.3.3-3(6)", "B2.4(1)"]),
        mcq("HEMATO-05-03-3",
            "A 6-year-old girl presents with fever, abdominal pain, and bloody diarrhea that began 7 days ago, now with decreased urine output. CBC: Hb 6.8 g/dL, MCV 90 fL, RDW 20%, WBC 11,000/µL, platelet 40,000/µL. PT 11 s, aPTT 28 s (normal). PBS: anisocytosis 3+, polychromasia, schistocytes 1+. Creatinine 3.2 mg/dL. What is the most likely diagnosis?",
            "Hemolytic uremic syndrome",
            ["Thrombotic thrombocytopenic purpura", "Disseminated intravascular coagulation", "Immune thrombocytopenia", "Henoch–Schönlein purpura"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เปลี่ยนเป็นเด็กและเพิ่ม Cr ตามบริบท HUS)",
            explain='''**เด็ก + bloody diarrhea นำ 5–10 วัน + MAHA + platelet ต่ำ + AKI + coag ปกติ** = **HUS** (Shiga-like toxin จาก EHEC O157:H7)
- TTP พบในผู้ใหญ่ เด่นอาการทางระบบประสาท
- DIC มี PT/aPTT ยาว
- ITP ไม่มี hemolysis/schistocyte และไม่มี AKI
- HSP เป็น vasculitis มี palpable purpura ที่ขา ปวดท้อง ไตอักเสบ แต่ **platelet ปกติ** ไม่มี schistocyte''',
            pearl="เด็ก + ท้องเสียเป็นเลือด + schistocyte + AKI = HUS", topic="HUS diagnosis",
            ref=[f"{D} หน้า 252, 272–275"], nl=["2.3.3-3(6)"]),
        mcq("HEMATO-05-03-4",
            "A 50-year-old man has fatigue and fluctuating consciousness for 2 weeks with fever and hematuria. LDH 800 U/L. CBC: anemia, leukocytosis, thrombocytopenia. PBS: MAHA picture. PT and PTT are normal. Which laboratory finding would best confirm the most likely diagnosis?",
            "Severely reduced ADAMTS13 activity",
            ["Elevated D-dimer with low fibrinogen", "Positive direct antiglobulin test", "Positive stool culture for E. coli O157:H7", "Reduced CD55 and CD59 on flow cytometry"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เปลี่ยนคำถามจากการวินิจฉัย TTP เป็นการตรวจยืนยัน)",
            explain='''ไข้ + ซึม + MAHA + platelet ต่ำ + coag ปกติ ในผู้ใหญ่ = **TTP** → ยืนยันด้วย **ADAMTS13 activity ↓** (แต่ห้ามรอผลก่อนเริ่ม plasma exchange)
- D-dimer สูง + fibrinogen ต่ำเป็นของ DIC ซึ่ง PT/PTT จะยาว
- DAT บวกเป็นของ AIHA/Evans
- Stool culture EHEC ใช้กับ HUS ในเด็กที่มีท้องเสียเป็นเลือด
- CD55/CD59 ลดลงเป็นของ PNH''',
            pearl="TTP confirm = ADAMTS13 activity ↓", topic="TTP investigation",
            ref=[f"{D} หน้า 251, 268–269"], nl=["2.3.3-3(6)"]),
    ])

# ---------------------------------------------------------------- 05-04 DIC
S4 = sec("hemato-05-04", "Disseminated intravascular coagulation (DIC)",
    "Sepsis/OB/trauma/malignancy/งูแมวเซา/AAA · เลือดซึมทุกที่ · ↓plt ↑PT ↑aPTT ↓fibrinogen ↑D-dimer + schistocyte · รักษาสาเหตุก่อน", minutes=7,
    source=f"{D} หน้า 253–265", nl=["2.2.20", "B2.2.2(8)", "2.2.48"],
    md='''
### กลไก

- **Systemic activation of clotting cascade** → microthrombi ทั่วร่าง → **ใช้ platelet และ clotting factor จนหมด** (consumptive coagulopathy) + fibrinolysis ทุติยภูมิ
- ผล: **ทั้ง thrombosis (อวัยวะล้มเหลว) และ bleeding**

### สาเหตุ

- **Sepsis** (บ่อยสุด), **trauma**, **malignancy** (APL, adenocarcinoma — เสริม)
- **OB complication**: septic abortion, abruptio placentae, amniotic fluid embolism, dead fetus
- Organ failure (ตับอ่อนอักเสบรุนแรง, ตับวาย)
- **Russell's viper venom** (งูแมวเซา)
- **Aortic aneurysm** (chronic DIC — เสริม)

### อาการ

- เลือดออก: purpura, petechiae, ecchymosis, **GI bleeding, hematuria**, **blood oozing ที่ตำแหน่งแทงสาย/เจาะเลือด**
- **Multiorgan failure**

### การตรวจ (ไม่มี gold standard — ใช้ร่วมกันหลายค่า)

| การตรวจ | ผล |
|---|---|
| CBC/PBS | ↓Hct, **↓platelet**, **schistocyte** |
| Coagulogram | **↑PT, ↑aPTT** (TT ยาวเมื่อ fibrinogen ต่ำ) |
| **Fibrinogen** | **↓** |
| **D-dimer** | **↑** |
| Bleeding time | ↑ |

(ISTH DIC score รวม platelet, D-dimer, PT, fibrinogen — เสริม)

### การรักษา

- **รักษาสาเหตุเป็นหลัก** (เช่น **ยาปฏิชีวนะใน sepsis**, ขูดมดลูก/คลอด, ผ่าตัด)
- **Transfusion ตามข้อบ่งชี้เมื่อมีเลือดออก**: platelet (< 50,000 + bleeding), **FFP** (PT/aPTT ยาว), **cryoprecipitate** (fibrinogen < 100 mg/dL)

> โจทย์ sepsis + เลือดออกหลายที่ + PT/aPTT ยาว + platelet ต่ำ แล้วถาม **management** → **IV antibiotic** (รักษาสาเหตุ) เป็นคำตอบหลักในสไลด์ — blood product เป็นการรักษาประคับประคอง
''',
    pearls=[
        "DIC: ↓plt + ↑PT/aPTT + ↓fibrinogen + ↑D-dimer + schistocyte",
        "สาเหตุ: sepsis, OB (septic abortion), trauma, malignancy, งูแมวเซา, AAA",
        "รักษาสาเหตุก่อน (sepsis → antibiotic) + blood product ตามข้อบ่งชี้",
        "Cryo เมื่อ fibrinogen < 100 · FFP เมื่อ PT/aPTT ยาว · plt <50k + bleeding",
    ],
    items=[
        mcq("HEMATO-05-04-1",
            "A 77-year-old woman is admitted to the ICU with septic shock from pyelonephritis. She develops gross hematuria in her urinary catheter and petechiae on her legs. Hb 7.8 g/dL, WBC 55,000/µL (N 90%), platelet 15,000/µL. PT 30 s, aPTT 60 s. What is the most likely cause of bleeding?",
            "Disseminated intravascular coagulation",
            ["Immune thrombocytopenia", "Thrombotic thrombocytopenic purpura", "Heparin-induced thrombocytopenia", "Drug-induced thrombocytopenia"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''**Sepsis + เลือดออกหลายตำแหน่ง + platelet ต่ำ + PT และ aPTT ยาว** = DIC (consumptive coagulopathy)
- ITP ทำให้ platelet ต่ำแต่ **coagulogram ปกติ**
- TTP: MAHA + neuro แต่ PT/aPTT ปกติ
- HIT ทำให้ platelet ลดลง ~50% หลังได้ heparin 5–10 วัน และเด่น **thrombosis** ไม่ใช่ PT/aPTT ยาว
- Drug-induced thrombocytopenia ไม่ทำให้ PT/aPTT ยาว''',
            pearl="Sepsis + plt ต่ำ + PT/aPTT ยาว = DIC", topic="DIC diagnosis",
            ref=[f"{D} หน้า 253–257"], nl=["2.2.20"]),
        mcq("HEMATO-05-04-2",
            "A woman underwent an illegal abortion 3 days ago. One day ago she developed fever, abdominal pain, and drowsiness. PE: abdominal tenderness with guarding, purulent vaginal discharge, enlarged tender uterus. Hct 30%, WBC 12,500/µL (N 90%), platelet 50,000/µL, BUN 40 mg/dL, Cr 1.2 mg/dL. What is the most likely cause of the thrombocytopenia?",
            "Disseminated intravascular coagulation",
            ["Thrombotic thrombocytopenic purpura", "Hemolytic uremic syndrome", "Immune thrombocytopenia", "Dilution from massive bleeding"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''**Septic abortion** เป็น OB complication + sepsis ซึ่งเป็นสาเหตุ DIC ที่พบบ่อย → platelet ถูกใช้ไปในการสร้าง microthrombi
- TTP ไม่มีสาเหตุนำแบบ sepsis และ coag ปกติ
- HUS พบในเด็กหลังท้องเสียเป็นเลือด
- ITP ไม่สัมพันธ์กับ sepsis เฉียบพลันแบบนี้
- ไม่มีประวัติเสียเลือดจำนวนมากหรือได้เลือดหลายยูนิต จึงไม่ใช่ dilutional''',
            pearl="Septic abortion → DIC", topic="DIC causes",
            ref=[f"{D} หน้า 253, 260–261"], nl=["2.2.20", "2.2.48"]),
        mcq("HEMATO-05-04-3",
            "A 60-year-old woman with sepsis from a urinary source develops ecchymoses and upper GI bleeding. PE: mild pallor, mild jaundice, petechiae on the limbs. Hct 30%, platelet 30,000/µL, PT 30 s, aPTT 60 s, fibrinogen 160 mg/dL. Blood products have been ordered. What is the most important management?",
            "Intravenous antibiotics",
            ["Platelet transfusion as the definitive treatment", "Cryoprecipitate", "Heparin infusion", "Tranexamic acid"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่ม fibrinogen; ตัวเลือก blood product ปรับเป็นเชิงหลักการ)",
            explain='''DIC จาก sepsis → **การรักษาที่สำคัญที่สุดคือรักษาสาเหตุ = IV antibiotics** (สไลด์: Tx cause) · blood product (platelet, FFP) เป็นการประคับประคองเมื่อมีเลือดออก
- Platelet transfusion ช่วยระหว่างมีเลือดออกแต่ไม่ใช่การรักษาที่ทำให้ DIC หยุด
- Cryoprecipitate ให้เมื่อ fibrinogen < 100 mg/dL — รายนี้ 160
- Heparin ใช้เฉพาะ DIC ที่เด่น thrombosis ไม่ใช่เมื่อเลือดออก GI
- Tranexamic acid ห้ามใน DIC ทั่วไปเพราะเพิ่ม thrombosis''',
            pearl="DIC → รักษาสาเหตุ (sepsis → ATB)", topic="DIC management",
            ref=[f"{D} หน้า 254, 264–265"], nl=["2.2.20", "2.2.48"]),
        mcq("HEMATO-05-04-4",
            "A 65-year-old man with a known large abdominal aortic aneurysm has multiple ecchymoses. Hb 10 g/dL, WBC 7,200/µL, platelet 30,000/µL. PT, aPTT, and thrombin time are all prolonged; fibrinogen is decreased. What is the most appropriate investigation?",
            "D-dimer",
            ["Euglobulin lysis time", "Bone marrow aspiration", "ADAMTS13 activity", "Mixing study"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Aortic aneurysm เป็นสาเหตุ **chronic DIC** (การแข็งตัวในถุงโป่งพอง) → platelet ต่ำ + PT/aPTT/TT ยาว + fibrinogen ต่ำ · ตรวจ **D-dimer** (fibrin degradation) เพื่อยืนยันว่ามีการสร้างและสลาย fibrin
- Euglobulin lysis time ใช้ดู primary hyperfibrinolysis เป็นการตรวจที่ไม่ค่อยใช้แล้ว
- Bone marrow ไม่ช่วยในภาวะ consumptive
- ADAMTS13 ใช้กับ TTP ซึ่ง coag ปกติ
- Mixing study ใช้แยก factor deficiency กับ inhibitor ใน isolated aPTT''',
            pearl="AAA + coagulopathy → DIC → D-dimer", topic="Chronic DIC",
            ref=[f"{D} หน้า 253, 262–263"], nl=["2.2.20", "3.3.8"]),
        mcq("HEMATO-05-04-5",
            "A 65-year-old woman has been hospitalized with severe pneumonia for 5 days. BT 39°C, RR 30/min. PE: drowsy, mild pallor, crepitations in both lungs. Hb 10 g/dL, MCV 85 fL, WBC 30,000/µL (N 90%), platelet 30,000/µL. PT 17 s (10–13), PTT 42 s (25–35). PBS: polychromasia and schistocytes. What is the etiology of her hematologic condition?",
            "Disseminated intravascular coagulation",
            ["Thrombotic thrombocytopenic purpura", "Hemolytic uremic syndrome", "Evans syndrome", "Leukemoid reaction"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Severe pneumonia (sepsis) + platelet ต่ำ + schistocyte + **PT และ PTT ยาว** = DIC — การซึมอธิบายได้จาก sepsis
- TTP มีซึมและ schistocyte ได้แต่ **PT/PTT ปกติ** และไม่มีสาเหตุนำแบบ sepsis
- HUS: เด็ก ท้องเสียเป็นเลือด ไตวาย
- Evans: spherocyte + DAT บวก
- Leukemoid reaction อธิบาย WBC สูงแต่ไม่อธิบาย coagulopathy และ schistocyte''',
            pearl="Schistocyte + PT/PTT ยาว = DIC (ไม่ใช่ TTP)", topic="DIC vs TTP",
            ref=[f"{D} หน้า 255, 258–259"], nl=["2.2.20"]),
    ])

LECTURE = lecture("05", "Platelet disorders & thrombotic microangiopathy",
    "ITP · APDE · MAHA · TTP · HUS · DIC",
    objectives=[
        "วินิจฉัย ITP แบบคัดออก ส่งตรวจ secondary cause และตัดสินใจรักษาตามระดับ platelet ได้",
        "แยก gestational thrombocytopenia และ Evans syndrome ออกจาก ITP ได้",
        "นึกถึง APDE เมื่อเด็ก bruise ง่ายแต่ platelet count ปกติ + eosinophilia",
        "แยก TTP, HUS, DIC จาก schistocyte และ coagulogram และเลือกการรักษาได้",
    ],
    sections=[S1, S2, S3, S4])
