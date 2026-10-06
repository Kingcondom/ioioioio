from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Hemato"

# ---------------------------------------------------------------- 04-01 Approach to bleeding
F_BLEED = fig("hemato-04-01-f1", "Approach to bleeding: primary vs secondary hemostasis", '''<svg viewBox="0 0 740 380">
 <defs><marker id="hemato-04-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="40" rx="10" class="acsoft"/>
 <text x="370" y="35" text-anchor="middle" class="tb">เลือดออกผิดปกติ</text>
 <path d="M310 50L190 82" class="ln" marker-end="url(#hemato-04-01-a)"/>
 <path d="M430 50L550 82" class="ln" marker-end="url(#hemato-04-01-a)"/>
 <rect x="20" y="84" width="340" height="120" rx="10" class="c1soft"/>
 <text x="190" y="106" text-anchor="middle" class="tb">Primary hemostasis (เกล็ดเลือด/หลอดเลือด)</text>
 <text x="36" y="130" class="t2">• ออก<tspan class="tb">ทันที</tspan> หลังบาดเจ็บ</text>
 <text x="36" y="152" class="t2">• Petechiae, ecchymosis ตื้น ๆ</text>
 <text x="36" y="174" class="t2">• Mucosal bleed: เลือดกำเดา เหงือก ประจำเดือนมาก</text>
 <text x="36" y="196" class="t3">ITP · vWD · APDE · aplastic anemia</text>
 <rect x="380" y="84" width="340" height="120" rx="10" class="c2soft"/>
 <text x="550" y="106" text-anchor="middle" class="tb">Secondary hemostasis (coagulation factor)</text>
 <text x="396" y="130" class="t2">• ออก<tspan class="tb">ช้า (delayed)</tspan> หลังหยุดไปแล้ว</text>
 <text x="396" y="152" class="t2">• Deep hematoma, ecchymosis ก้อนใหญ่</text>
 <text x="396" y="174" class="t2">• Hemarthrosis, intramuscular bleed</text>
 <text x="396" y="196" class="t3">Hemophilia · vit K def · warfarin · liver</text>
 <rect x="20" y="220" width="700" height="34" rx="8" class="sunk"/>
 <text x="190" y="242" text-anchor="middle" class="tb">การตรวจ</text>
 <text x="330" y="242" text-anchor="middle" class="tb">Vascular</text>
 <text x="490" y="242" text-anchor="middle" class="tb">Platelet</text>
 <text x="640" y="242" text-anchor="middle" class="tb">Coagulation</text>
 <text x="190" y="280" text-anchor="middle" class="t2">Tourniquet test</text>
 <text x="330" y="280" text-anchor="middle" class="ta">ผิดปกติ</text>
 <text x="490" y="280" text-anchor="middle" class="ta">ผิดปกติ</text>
 <text x="640" y="280" text-anchor="middle" class="t2">ปกติ</text>
 <text x="190" y="314" text-anchor="middle" class="t2">Bleeding time</text>
 <text x="330" y="314" text-anchor="middle" class="t2">ปกติ</text>
 <text x="490" y="314" text-anchor="middle" class="ta">ผิดปกติ</text>
 <text x="640" y="314" text-anchor="middle" class="t2">ปกติ</text>
 <text x="190" y="348" text-anchor="middle" class="t2">VCT / PT / aPTT</text>
 <text x="330" y="348" text-anchor="middle" class="t2">ปกติ</text>
 <text x="490" y="348" text-anchor="middle" class="t2">ปกติ</text>
 <text x="640" y="348" text-anchor="middle" class="ta">ผิดปกติ</text>
 <path d="M20 296H720M20 330H720" class="lnf"/>
</svg>''', "ซักลักษณะเลือดออกก่อนว่าเป็นแบบเกล็ดเลือด (ทันที ผิวตื้น เยื่อบุ) หรือแบบ factor (ช้า ลึก ข้อ) แล้วเลือกการตรวจให้ตรงชั้น")

F_COAG = fig("hemato-04-01-f2", "Coagulation cascade กับ PT / aPTT / TT", '''<svg viewBox="0 0 740 380">
 <defs><marker id="hemato-04-01-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="20" y="14" width="300" height="160" rx="12" class="c1soft"/>
 <text x="170" y="36" text-anchor="middle" class="ta">Intrinsic → aPTT</text>
 <rect x="110" y="48" width="120" height="28" rx="8" class="box"/>
 <text x="170" y="67" text-anchor="middle" class="tb">XII</text>
 <path d="M170 76V88" class="ln" marker-end="url(#hemato-04-01-b)"/>
 <rect x="110" y="90" width="120" height="28" rx="8" class="box"/>
 <text x="170" y="109" text-anchor="middle" class="tb">XI</text>
 <path d="M170 118V130" class="ln" marker-end="url(#hemato-04-01-b)"/>
 <rect x="80" y="132" width="180" height="30" rx="8" class="box"/>
 <text x="170" y="152" text-anchor="middle" class="tb">IX + VIII</text>
 <rect x="420" y="14" width="300" height="100" rx="12" class="c2soft"/>
 <text x="570" y="36" text-anchor="middle" class="ta">Extrinsic → PT/INR</text>
 <rect x="470" y="52" width="200" height="40" rx="8" class="box"/>
 <text x="570" y="70" text-anchor="middle" class="tb">VII + tissue factor</text>
 <text x="570" y="86" text-anchor="middle" class="t3">t½ สั้นสุด → PT ยาวก่อน</text>
 <path d="M240 162L320 186" class="ln" marker-end="url(#hemato-04-01-b)"/>
 <path d="M570 92L440 186" class="ln" marker-end="url(#hemato-04-01-b)"/>
 <rect x="220" y="190" width="300" height="146" rx="12" class="acsoft"/>
 <text x="370" y="208" text-anchor="middle" class="ta">Common pathway (ยาวทั้ง PT และ aPTT)</text>
 <rect x="320" y="216" width="100" height="28" rx="8" class="box"/>
 <text x="370" y="235" text-anchor="middle" class="tb">X + V</text>
 <path d="M370 244V256" class="ln" marker-end="url(#hemato-04-01-b)"/>
 <rect x="280" y="258" width="180" height="28" rx="8" class="box"/>
 <text x="370" y="277" text-anchor="middle" class="tb">II (prothrombin) → IIa</text>
 <path d="M370 286V298" class="ln" marker-end="url(#hemato-04-01-b)"/>
 <rect x="260" y="300" width="220" height="28" rx="8" class="box"/>
 <text x="370" y="319" text-anchor="middle" class="tb">Fibrinogen → fibrin</text>
 <rect x="540" y="296" width="180" height="36" rx="8" class="miss"/>
 <text x="630" y="319" text-anchor="middle" class="tw">TT = ขั้นนี้เท่านั้น</text>
 <path d="M538 314H482" class="lnf" marker-end="url(#hemato-04-01-b)"/>
 <rect x="20" y="196" width="180" height="136" rx="10" class="box"/>
 <text x="110" y="218" text-anchor="middle" class="tb">Vit K dependent</text>
 <text x="110" y="242" text-anchor="middle" class="ta">II, VII, IX, X</text>
 <text x="110" y="266" text-anchor="middle" class="t3">warfarin ยับยั้ง</text>
 <text x="110" y="288" text-anchor="middle" class="t3">PCC มีครบ 4 ตัว</text>
 <text x="110" y="314" text-anchor="middle" class="t3">(+ protein C, S)</text>
 <text x="370" y="360" text-anchor="middle" class="t3">ยา: UFH ยับยั้ง IIa/Xa (aPTT) · LMWH/fondaparinux/-xaban ยับยั้ง Xa · dabigatran ยับยั้ง IIa (TT ยาว)</text>
</svg>''', "PT วัดฝั่ง VII + common pathway · aPTT วัดฝั่ง XII–XI–IX–VIII + common pathway · TT วัดเฉพาะ fibrinogen → fibrin (ภาพสไลด์หน้า 175/194 เป็นภาพ วาดใหม่เป็นเสริม)")

S1 = sec("hemato-04-01", "Approach to bleeding & abnormal coagulogram",
    "Primary (ทันที mucosal) vs secondary (ช้า ลึก ข้อ) · isolated PT, isolated aPTT + mixing test, PT+aPTT ± TT", minutes=9,
    source=f"{D} หน้า 173–179, 194", nl=["2.1.58", "3.3.8", "B2.3(7)"],
    md='''
### Primary vs secondary hemostatic bleeding

| | Primary (platelet/vessel) | Secondary (coagulation) |
|---|---|---|
| Onset | **ทันที** | **Delayed** |
| ลักษณะ | **Petechiae**, superficial ecchymosis, **mucosal bleed** | **Deep hematoma**, large ecchymosis, **hemarthrosis**, intramuscular bleed |

| การตรวจ | Vascular | Platelet | Coagulation |
|---|---|---|---|
| Tourniquet test | ผิดปกติ | ผิดปกติ | ปกติ |
| Bleeding time | ปกติ | **ผิดปกติ** | ปกติ |
| VCT (venous clotting time) | ปกติ | ปกติ | **ผิดปกติ** |

[[fig:hemato-04-01-f1]]

### Coagulogram

[[fig:hemato-04-01-f2]]

#### Isolated PT prolong

- **Early vitamin K deficiency**, liver disease, early DIC
- **Warfarin**
- **Factor VII deficiency**
- เหตุผล: **factor VII มี half-life สั้นที่สุด** จึงลดก่อน

#### Isolated aPTT prolong

- **ไม่มีเลือดออก**: **antiphospholipid syndrome** (กลับมี thrombosis), **heparin contamination** (เจาะจากสาย heparin lock), **factor XII deficiency**
- **มีเลือดออก** → ทำ **mixing test** (ผสม plasma ปกติ 1:1)
  - **Correctable** (aPTT กลับปกติ) = **factor deficiency**: hemophilia A, B, vWD
  - **Uncorrectable** = **inhibitor** (acquired factor VIII inhibitor) หรือ heparin

#### PT + aPTT prolong → ดู TT

- **TT ปกติ**: **multiple factor deficiency** (vitamin K deficiency ระยะหลัง, warfarin เกินขนาด, liver disease, DIC, massive transfusion) หรือ common pathway deficiency (factor II, V, X)
- **TT ยาว**: **↓fibrinogen** (DIC, liver failure) หรือ **thrombin inhibitor** (heparin, dabigatran)

> mixing test ใช้กับ **aPTT ยาวที่มีเลือดออก**: แก้ได้ = ขาด factor · แก้ไม่ได้ = มี inhibitor
''',
    figs=[F_BLEED, F_COAG],
    pearls=[
        "Primary: ทันที petechiae mucosal · secondary: ช้า hematoma hemarthrosis",
        "Isolated PT: early vit K def, warfarin, liver, F VII def (t½ สั้นสุด)",
        "Isolated aPTT ไม่มีเลือดออก: APS, heparin contamination, F XII",
        "aPTT + bleeding → mixing: แก้ได้ = factor deficiency · แก้ไม่ได้ = inhibitor",
        "PT + aPTT + TT ยาว = fibrinogen ต่ำหรือ thrombin inhibitor",
    ],
    items=[
        mcq("HEMATO-04-01-1",
            "A 22-year-old man has easy bruising. PE: generalized ecchymoses and a 6-cm ecchymosis on the right arm. CBC: Hb 12.3 g/dL, WBC 7,900/µL, platelet 360,000/µL. Coagulogram: PT 20.4 s (10–13), aPTT 33.2 s (25–35). He takes no medication and liver function is normal. What is the most likely diagnosis?",
            "Factor VII deficiency",
            ["Factor VIII deficiency", "Factor IX deficiency", "Factor VIII inhibitor", "Antiphospholipid syndrome"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่ม no drug/LFT ปกติ)",
            explain='''**Isolated PT prolong** ในคนหนุ่มที่ไม่ได้ยาและตับปกติ = **factor VII deficiency** (PT วัด extrinsic pathway ซึ่งมี VII ตัวเดียว)
- Factor VIII และ IX deficiency (hemophilia A, B) ทำให้ **aPTT** ยาว PT ปกติ
- Factor VIII inhibitor ทำให้ aPTT ยาวและ mixing แก้ไม่ได้
- Antiphospholipid syndrome ทำให้ aPTT ยาวแต่กลับเป็น thrombosis ไม่ใช่ bleeding''',
            pearl="Isolated PT ยาวไม่มีสาเหตุอื่น = F VII deficiency", topic="Isolated PT",
            ref=[f"{D} หน้า 177, 190–191"], nl=["3.3.8"]),
        mcq("HEMATO-04-01-2",
            "A 60-year-old woman with acute pyelonephritis has been on IV antibiotics through a heparin lock for 7 days. Blood for coagulation tests was drawn from the heparin lock. She has no bleeding. CBC: platelet 160,000/µL. Coagulogram: PT 12 s (10–13), aPTT 75 s (25–35). Repeat sampling by direct venipuncture gives a normal aPTT. What explains the initial result?",
            "Heparin contamination of the sample",
            ["Vitamin K deficiency", "Factor VIII inhibitor", "Disseminated intravascular coagulation", "Factor XII deficiency"],
            explain='''aPTT ยาวแยกเดี่ยวโดย**ไม่มีเลือดออก** และเลือดเจาะจาก **heparin lock** แล้วเจาะใหม่ปกติ = **heparin contamination**
- Vitamin K deficiency ทำให้ PT ยาวก่อน (factor VII) ไม่ใช่ isolated aPTT
- Factor VIII inhibitor ทำให้เลือดออกมาก aPTT ยาวคงที่ แม้เจาะใหม่
- DIC จะมี platelet ต่ำ PT/aPTT ยาวพร้อม fibrinogen ต่ำ
- Factor XII deficiency เป็นสาเหตุ aPTT ยาวไม่มีเลือดออกเช่นกัน แต่จะยาว**ทุกครั้ง** ไม่หายเมื่อเจาะใหม่
(หมายเหตุ: ข้อสอบเก่าในสไลด์หน้า 184 ให้ PT 30 aPTT 25 เป็น isolated PT ซึ่งเฉลยคือ vitamin K deficiency — ดูข้อในหัวข้อ vitamin K)''',
            pearl="aPTT ยาว ไม่มีเลือดออก เจาะจากสาย heparin = contamination", topic="Isolated aPTT without bleeding",
            ref=[f"{D} หน้า 178"], nl=["3.3.8"]),
        mcq("HEMATO-04-01-3",
            "A 65-year-old man with no previous bleeding history develops large spontaneous ecchymoses and a thigh hematoma. Platelet 240,000/µL, PT 12 s (10–13), aPTT 72 s (25–35). A 1:1 mixing study with normal plasma gives aPTT 66 s after incubation. What is the most likely diagnosis?",
            "Acquired factor VIII inhibitor",
            ["Hemophilia A", "von Willebrand disease", "Factor XII deficiency", "Vitamin K deficiency"],
            explain='''aPTT ยาว + **เลือดออกรุนแรงแบบ secondary (hematoma)** + **mixing test แก้ไม่ได้** = มี **inhibitor** → ในผู้สูงอายุที่ไม่เคยมีประวัติเลือดออก คือ **acquired hemophilia (factor VIII inhibitor)**
- Hemophilia A และ vWD เป็น factor deficiency → mixing **แก้ได้** และมักมีประวัติตั้งแต่เด็ก
- Factor XII deficiency ไม่ทำให้เลือดออก
- Vitamin K deficiency ทำให้ PT ยาว''',
            pearl="aPTT ยาว + bleeding + mixing ไม่แก้ = inhibitor", topic="Mixing test",
            ref=[f"{D} หน้า 178"], nl=["3.3.8", "2.3.3(1)"]),
        mcq("HEMATO-04-01-4",
            "A 50-year-old man with alcoholic cirrhosis has diffuse oozing. Platelet 90,000/µL (no schistocytes), PT 21 s (10–13), aPTT 50 s (25–35), thrombin time 20 s (10–13). What does the prolonged thrombin time indicate?",
            "Low fibrinogen or dysfunctional fibrinogen",
            ["Factor VII deficiency", "Factor VIII deficiency", "Vitamin K deficiency alone", "Platelet dysfunction"],
            explain='''TT วัดเฉพาะขั้น **fibrinogen → fibrin** · PT + aPTT + **TT ยาว** = **↓fibrinogen** (ตับสร้างไม่พอ/DIC) หรือมี thrombin inhibitor → ในโรคตับให้ **cryoprecipitate**
- Factor VII deficiency ทำให้ PT ยาวอย่างเดียว
- Factor VIII deficiency ทำให้ aPTT ยาวอย่างเดียว
- Vitamin K deficiency ทำให้ PT/aPTT ยาวแต่ **TT ปกติ** (fibrinogen ไม่ขึ้นกับ vit K)
- Platelet dysfunction ไม่ทำให้ coagulogram ผิดปกติ''',
            pearl="TT ยาว = fibrinogen ต่ำ หรือ heparin/dabigatran", topic="Thrombin time",
            ref=[f"{D} หน้า 179, 346–347"], nl=["3.3.8"]),
    ])

# ---------------------------------------------------------------- 04-02 Vitamin K deficiency
S2 = sec("hemato-04-02", "Vitamin K deficiency",
    "Factor II VII IX X · ทารกแรกเกิด, fat malabsorption, ยาปฏิชีวนะนาน · early = isolated PT · late = PT+aPTT · vitamin K IV", minutes=5,
    source=f"{D} หน้า 180–191", nl=["2.3.3(1)", "B2.2.5(2)", "2.3.16(3)"],
    md='''
### Vitamin K-dependent factors

- **Factor II, VII, IX, X** (+ protein C, S — เสริม) ต้องใช้วิตามินเคในการ γ-carboxylation

### สาเหตุ

| สาเหตุ | กลไก |
|---|---|
| **Vitamin K deficiency bleeding (VKDB) of the newborn** (hemorrhagic disease of the newborn) | ทารกยังไม่มี gut flora สร้างวิตามินเค · ป้องกันด้วย **vitamin K IM ตอนคลอด** |
| **Fat malabsorption** (obstructive jaundice, pancreatic insufficiency) | Vitamin K เป็น fat-soluble (A, D, E, K) |
| **Prolonged broad-spectrum antibiotics** (เช่น cefoperazone, ผู้ป่วย ICU กินไม่ได้) | ทำลาย gut flora ที่สร้างวิตามินเค |

### Lab

- **Early: isolated PT prolong** (factor VII t½ สั้นสุด ลดก่อน)
- **Late: PT + aPTT prolong** · TT และ fibrinogen ปกติ · platelet ปกติ

### การรักษา

- **Vitamin K IV** (เสริม: 10 mg IV ช้า ๆ; PT ดีขึ้นใน 12–24 ชม.)
- เลือดออกรุนแรง → เพิ่ม FFP/PCC (เสริม)

> ผู้สูงอายุ admit ICU ได้ยาปฏิชีวนะนาน เกิด ecchymosis ที่จุดเจาะเลือด + PT/aPTT ยาว + platelet ปกติ = vitamin K deficiency (ไม่ใช่ DIC เพราะ platelet ปกติ)
''',
    pearls=[
        "Vit K dependent: II, VII, IX, X",
        "Early vit K def = isolated PT · late = PT + aPTT",
        "ยาปฏิชีวนะนาน (cefoperazone) / ICU / fat malabsorption / ทารกแรกเกิด",
        "รักษา vitamin K IV · ทารกได้ vitamin K IM ตอนคลอด",
    ],
    items=[
        mcq("HEMATO-04-02-1",
            "A 76-year-old man with hospital-acquired pneumonia has been treated with cefoperazone/sulbactam for 2 weeks with poor oral intake. He develops large ecchymoses at venipuncture sites. Platelet 195,000/µL. Coagulogram: PT 89 s (11–15), aPTT 76 s (25–38). Fibrinogen is normal. What is the most likely diagnosis?",
            "Vitamin K deficiency",
            ["Disseminated intravascular coagulation", "Acquired hemophilia", "Liver failure", "Hyperfibrinolysis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่ม fibrinogen ปกติ)",
            explain='''ยาปฏิชีวนะ broad-spectrum นาน (cefoperazone) + กินไม่ได้ → **vitamin K deficiency ระยะหลัง** → PT + aPTT ยาว, **platelet และ fibrinogen ปกติ**
- DIC จะมี platelet ต่ำ fibrinogen ต่ำ D-dimer สูง ในบริบท sepsis
- Acquired hemophilia ทำให้ aPTT ยาวอย่างเดียว PT ปกติ
- Liver failure ทำให้ PT/aPTT ยาวได้ แต่ไม่มีข้อมูลโรคตับ และมักมี platelet ต่ำ fibrinogen ต่ำ
- Hyperfibrinolysis จะมี fibrinogen ต่ำ''',
            pearl="ATB นาน + PT/aPTT ยาว + Plt ปกติ = vit K deficiency", topic="Vitamin K deficiency",
            ref=[f"{D} หน้า 181, 186–187"], nl=["2.3.3(1)"]),
        mcq("HEMATO-04-02-2",
            "A 60-year-old woman with acute pyelonephritis has received IV antibiotics for 7 days with poor intake. She develops purpura for 2 days without other bleeding. CBC: Hb 12 g/dL, WBC 4,400/µL, platelet 160,000/µL. Coagulogram: PT 30 s (10–13), aPTT 30 s (25–35). What is the most likely cause of this purpura?",
            "Vitamin K deficiency",
            ["Heparin contamination", "Factor VIII inhibitor", "Chronic kidney disease", "Disseminated intravascular coagulation"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''**Isolated PT prolong** หลังได้ยาปฏิชีวนะและกินไม่ได้ 1 สัปดาห์ = **early vitamin K deficiency** (factor VII t½ สั้นสุดลดก่อน)
- Heparin contamination ทำให้ **aPTT** ยาว ไม่ใช่ PT
- Factor VIII inhibitor ทำให้ aPTT ยาว
- CKD ทำให้ platelet dysfunction (uremic) แต่ไม่ทำให้ PT ยาว
- DIC มี platelet ต่ำและมักยาวทั้ง PT/aPTT''',
            pearl="ATB + isolated PT ยาว = early vit K deficiency", topic="Early vitamin K deficiency",
            ref=[f"{D} หน้า 184–185"], nl=["2.3.3(1)"]),
        mcq("HEMATO-04-02-3",
            "A 10-day-old breastfed infant born at home presents with generalized bruising and oozing from the umbilical stump. Hb 8 g/dL, platelet 280,000/µL. PT and aPTT are prolonged, INR 2.2. What is the most likely diagnosis?",
            "Vitamin K deficiency bleeding of the newborn",
            ["Hemophilia A", "von Willebrand disease", "Hemolytic disease of the newborn", "Neonatal alloimmune thrombocytopenia"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มประวัติคลอดที่บ้าน)",
            explain='''ทารกแรกเกิดยังไม่มี gut flora + นมแม่มีวิตามินเคน้อย + คลอดที่บ้าน (ไม่ได้ vitamin K IM) → **VKDB** → PT/aPTT ยาว platelet ปกติ
- Hemophilia A ทำให้ aPTT ยาวอย่างเดียว PT/INR ปกติ
- vWD ทำให้ primary bleeding และ aPTT อาจยาวเล็กน้อย PT ปกติ
- Hemolytic disease of the newborn ทำให้ซีดเหลือง ไม่ทำให้ INR ยาว
- Alloimmune thrombocytopenia ทำให้ platelet ต่ำ''',
            pearl="ทารกไม่ได้ vit K IM + INR ยาว = VKDB", topic="VKDB",
            ref=[f"{D} หน้า 181, 188–189"], nl=["2.3.3(1)", "2.3.16(3)"]),
        mcq("HEMATO-04-02-4",
            "An elderly patient has been in the ICU on broad-spectrum antibiotics for 1 month with nil per oral intake. Which vitamin deficiency is this patient most likely to develop?",
            "Vitamin K",
            ["Vitamin C", "Vitamin D", "Vitamin B2", "Vitamin B6"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ยาปฏิชีวนะ broad-spectrum นานทำลาย **gut flora ที่สร้าง vitamin K2** ร่วมกับไม่ได้รับอาหาร → ขาด **vitamin K** เร็วที่สุด (store น้อย)
- Vitamin C ขาดได้ในคนกินไม่ได้นาน แต่ไม่สัมพันธ์กับยาปฏิชีวนะ และ scurvy ใช้เวลาหลายเดือน
- Vitamin D store อยู่ได้นาน
- Vitamin B2 และ B6 ไม่ได้ขึ้นกับ gut flora แบบนี้''',
            pearl="ICU + ATB นาน → vitamin K", topic="Antibiotics & vitamin K",
            ref=[f"{D} หน้า 182–183"], nl=["2.3.3(1)"]),
    ])

# ---------------------------------------------------------------- 04-03 Anticoagulants & warfarin overdose
F_WARF = fig("hemato-04-03-f1", "Warfarin overdose: เลือกการแก้ตาม bleeding และ INR", '''<svg viewBox="0 0 720 300">
 <defs><marker id="hemato-04-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="240" y="10" width="240" height="40" rx="10" class="acsoft"/>
 <text x="360" y="35" text-anchor="middle" class="tb">INR สูงจาก warfarin</text>
 <path d="M300 50L170 82" class="ln" marker-end="url(#hemato-04-03-a)"/>
 <path d="M420 50L550 82" class="ln" marker-end="url(#hemato-04-03-a)"/>
 <rect x="20" y="84" width="300" height="206" rx="10" class="badsoft"/>
 <text x="170" y="108" text-anchor="middle" class="tb">Major bleeding (INR เท่าไรก็ได้)</text>
 <text x="170" y="126" text-anchor="middle" class="t3">ICH, GI bleed ที่ V/S ไม่ดี, ต้องผ่าตัดด่วน</text>
 <text x="40" y="156" class="t2">1. Hold warfarin</text>
 <text x="40" y="182" class="ta">2. Vitamin K 10 mg IV (ช้า)</text>
 <text x="40" y="208" class="ta">3. PCC (เร็ว)</text>
 <text x="58" y="228" class="t3">ไม่มี PCC → FFP</text>
 <text x="40" y="262" class="t3">ต้องให้ทั้งตัวเร็วและตัวช้า</text>
 <text x="40" y="280" class="t3">(PCC/FFP หมดฤทธิ์ใน 6–8 ชม.)</text>
 <rect x="340" y="84" width="360" height="206" rx="10" class="oksoft"/>
 <text x="520" y="108" text-anchor="middle" class="tb">ไม่มี/เลือดออกเล็กน้อย</text>
 <rect x="356" y="122" width="328" height="40" rx="8" class="box"/>
 <text x="372" y="147" class="t2">INR &lt; 5 → ลดขนาด หรืองด 1 มื้อ</text>
 <rect x="356" y="170" width="328" height="40" rx="8" class="box"/>
 <text x="372" y="195" class="t2">INR 5–10 → งดยา (omit dose)</text>
 <rect x="356" y="218" width="328" height="56" rx="8" class="misssoft"/>
 <text x="372" y="240" class="tb">INR &gt; 10 → oral vitamin K 5–10 mg</text>
 <text x="372" y="262" class="t3">+ งดยา ติดตาม INR</text>
</svg>''', "แยกก่อนว่ามี major bleeding หรือไม่ — ถ้ามีให้ทั้ง vitamin K IV และ PCC ทันทีไม่สน INR · ถ้าไม่มี ดู INR เป็นช่วง (ตามสไลด์หน้า 195)")

S3 = sec("hemato-04-03", "Anticoagulants & warfarin overdose",
    "Warfarin INR 2–3 · DOAC ไม่ต้อง monitor · UFH aPTT 1.5–2.5 + protamine · major bleed: vit K 10 mg IV + PCC · INR >10 ไม่มีเลือดออก: oral vit K 5–10 mg", minutes=8,
    source=f"{D} หน้า 192–203", nl=["B2.4(3)", "2.3.3(1)", "2.2.44"],
    md='''
### Oral anticoagulants

| ยา | กลไก | Monitor | Antidote |
|---|---|---|---|
| **Warfarin** | ยับยั้ง vitamin K epoxide reductase → ↓II, VII, IX, X | **INR 2–3** | **Vitamin K** (ช้า) · **FFP, PCC** (เร็ว) |
| **Dabigatran** | Direct thrombin (IIa) inhibitor | ไม่ต้อง | Idarucizumab (เสริม) |
| **Rivaroxaban, apixaban, edoxaban** | Factor Xa inhibitor | ไม่ต้อง | Andexanet alfa/PCC (เสริม) |

- Warfarin ออกฤทธิ์ช้า และช่วงแรกลด protein C ก่อน (procoagulant ชั่วคราว) → **ต้องให้ heparin ร่วมในช่วงแรก** (bridging จน INR ได้เป้า)

### Parenteral anticoagulants

| ยา | Monitor | Antidote | หมายเหตุ |
|---|---|---|---|
| **UFH IV** | **aPTT ratio 1.5–2.5**, platelet (HIT) | **Protamine sulfate** | ใช้ได้ใน **GFR < 30**, อ้วน |
| **LMWH (enoxaparin) SC** | ไม่ต้อง | Protamine (**partial reversal**) | ลดขนาดเมื่อไตเสื่อม |
| **Fondaparinux SC** | ไม่ต้อง | ไม่มี specific antidote (สไลด์ระบุ aPCC/rFVIIa) | |

- ใช้ heparin ต้อง **ติดตาม platelet เพื่อดู heparin-induced thrombocytopenia (HIT)**

### Warfarin overdose (ตามสไลด์)

[[fig:hemato-04-03-f1]]

| สถานการณ์ | การจัดการ |
|---|---|
| **Major bleeding (INR เท่าไรก็ได้)** | **Hold warfarin + vitamin K 10 mg IV + PCC** (ไม่มี PCC ใช้ **FFP**) |
| ไม่มีเลือดออกสำคัญ, INR < 5 | ลดขนาด/งด 1 มื้อ |
| ไม่มีเลือดออกสำคัญ, INR 5–10 | งดยา (omit dose) |
| ไม่มีเลือดออกสำคัญ, **INR > 10** | **Oral vitamin K 5–10 mg** (สไลด์) — แนวทาง ACCP ปัจจุบันใช้ 2.5–5 mg (เสริม) |

> ICH ในผู้ป่วยกิน warfarin → **vitamin K IV + PCC** (ตัวเลือกไม่มี PCC → FFP) · ห้ามตอบ cryoprecipitate (ไม่มี factor II VII IX X) หรือ protamine (แก้ heparin)
> ต้องผ่าตัดใน 24 ชั่วโมงและไม่มีเลือดออก INR 3 → **vitamin K** (ออกฤทธิ์ทันภายใน 12–24 ชม.) ไม่จำเป็นต้องใช้ FFP
''',
    figs=[F_WARF],
    pearls=[
        "Warfarin: INR 2–3 · ช่วงแรกให้ heparin ร่วม",
        "Major bleed บน warfarin: vitamin K 10 mg IV + PCC (หรือ FFP)",
        "ไม่มีเลือดออก: INR <5 ลด/งด 1 มื้อ · 5–10 งดยา · >10 oral vit K 5–10 mg",
        "UFH: aPTT 1.5–2.5 · antidote protamine · ใช้ได้ใน GFR <30",
        "Dabigatran = IIa · -xaban = Xa · DOAC ไม่ต้อง monitor",
    ],
    items=[
        mcq("HEMATO-04-03-1",
            "A 70-year-old man with a previous ischemic stroke takes warfarin. He presents with new right hemiparesis. CT brain shows intracerebral hemorrhage. INR is 3.8. In addition to holding warfarin and giving intravenous vitamin K, what is the next most appropriate step?",
            "Prothrombin complex concentrate",
            ["Cryoprecipitate", "Platelet transfusion", "Protamine sulfate", "Intravenous thrombolysis"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ICH = **major bleeding** → hold warfarin + **vitamin K 10 mg IV (ช้า)** + **PCC** ซึ่งมี factor II, VII, IX, X เข้มข้น แก้ INR ได้ภายในไม่กี่นาที (ดีกว่า FFP ที่ต้องให้ปริมาตรมากและช้ากว่า)
- Cryoprecipitate มี fibrinogen, VIII, XIII, vWF ไม่มี vitamin K-dependent factors
- Platelet transfusion ไม่ช่วย ปัญหาไม่ใช่เกล็ดเลือด
- Protamine แก้ heparin ไม่ใช่ warfarin
- Thrombolysis ห้ามเด็ดขาดใน ICH''',
            pearl="ICH บน warfarin: vit K IV + PCC", topic="Warfarin reversal in ICH",
            ref=[f"{D} หน้า 195–197"], nl=["2.2.44", "B2.4(3)"]),
        mcq("HEMATO-04-03-2",
            "A 35-year-old man with mechanical valve on warfarin develops sudden headache and left hemiplegia. CT: right parietal intracerebral hemorrhage. PT 20 s, INR 5. Warfarin has been stopped. Prothrombin complex concentrate is not available in the hospital. Besides intravenous vitamin K, what is the most appropriate immediate treatment?",
            "Fresh frozen plasma",
            ["Cryoprecipitate", "Tranexamic acid", "Protamine sulfate", "Platelet transfusion"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มว่าไม่มี PCC ให้คำตอบตรงแนวทาง)",
            explain='''Major bleeding (ICH) → vitamin K IV ร่วมกับตัวแก้ที่ออกฤทธิ์เร็ว — **ไม่มี PCC ให้ใช้ FFP** (มีทุก factor) ตามสไลด์
- Cryoprecipitate ไม่มี factor II, VII, IX, X
- Tranexamic acid เป็น antifibrinolytic ไม่แก้ฤทธิ์ warfarin
- Protamine ใช้แก้ heparin
- Platelet ไม่เกี่ยว
(สไลด์เดิมมีตัวเลือก IV vitamin K ด้วย — vitamin K อย่างเดียวช้าเกินสำหรับ ICH ต้องคู่กับ PCC/FFP)''',
            pearl="ไม่มี PCC → FFP", topic="Warfarin reversal without PCC",
            ref=[f"{D} หน้า 195, 198–199"], nl=["2.2.44", "B2.4(1)"]),
        mcq("HEMATO-04-03-3",
            "A 70-year-old man with hypertension, type 2 diabetes, and atrial fibrillation has taken warfarin for years. He has easy bruising and mild gum bleeding for 3 days. Vital signs are stable and Hb is unchanged. PE: several ecchymoses on both legs. INR is 14. In addition to holding warfarin, what is the most appropriate management according to the slide algorithm?",
            "Oral vitamin K 5 mg",
            ["No additional treatment", "Intravenous vitamin K 10 mg with PCC", "Fresh frozen plasma infusion", "Cryoprecipitate"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''INR **> 10** โดย **ไม่มี significant bleeding** (เลือดออกเล็กน้อย V/S คงที่ Hb ไม่ลด) → งด warfarin + **oral vitamin K 5–10 mg** ตามสไลด์ (แนวทาง ACCP ใช้ 2.5–5 mg — ทั้งสองแบบได้ oral)
- ไม่ทำอะไรเพิ่ม เหมาะกับ INR 5–10 ที่ไม่มีเลือดออก แต่ INR 14 เสี่ยงเลือดออกรุนแรง
- Vitamin K IV + PCC สำรองไว้สำหรับ major bleeding
- FFP ใช้เมื่อ major bleeding และไม่มี PCC
- Cryoprecipitate ไม่มี vitamin K-dependent factors''',
            pearl="INR > 10 ไม่มีเลือดออกหนัก → oral vit K", topic="Warfarin overdose no major bleed",
            ref=[f"{D} หน้า 195, 200–201"], nl=["B2.4(3)", "2.3.3(1)"]),
        mcq("HEMATO-04-03-4",
            "A 25-year-old woman on warfarin for deep vein thrombosis after a femur fracture is scheduled for surgery in 24 hours. She has a small ecchymosis on one limb without active bleeding. INR is 3. What is the most appropriate management?",
            "Intravenous vitamin K",
            ["Fresh frozen plasma", "Cryoprecipitate", "Prothrombin complex concentrate now", "Continue warfarin and operate as scheduled"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ไม่มีเลือดออกสำคัญ และ**มีเวลา 24 ชั่วโมง**ก่อนผ่าตัด → หยุด warfarin + **vitamin K IV** ซึ่งลด INR ได้ภายใน 12–24 ชม. เพียงพอโดยไม่ต้องใช้ blood product
- FFP และ PCC เป็นตัวแก้เร็ว ใช้เมื่อ major bleeding หรือผ่าตัดด่วนภายในไม่กี่ชั่วโมง — เสี่ยง volume overload/thrombosis โดยไม่จำเป็น
- Cryoprecipitate ไม่มี vitamin K-dependent factors
- ผ่าตัดทั้งที่ INR 3 เสี่ยงเลือดออกมาก''',
            pearl="ผ่าตัดใน 24 ชม. ไม่มีเลือดออก → vit K IV พอ", topic="Pre-operative warfarin reversal",
            ref=[f"{D} หน้า 202–203"], nl=["B2.4(3)"]),
        mcq("HEMATO-04-03-5",
            "A 58-year-old man with acute pulmonary embolism and an eGFR of 22 mL/min/1.73 m² needs initial parenteral anticoagulation. Which agent and monitoring are most appropriate?",
            "Unfractionated heparin monitored by aPTT ratio 1.5–2.5",
            ["Enoxaparin without monitoring", "Fondaparinux without monitoring", "Warfarin alone targeting INR 2–3", "Dabigatran without monitoring"],
            explain='''**UFH IV** ไม่ขับทางไต จึง **ใช้ได้เมื่อ GFR < 30** (และในคนอ้วนมาก) ติดตามด้วย **aPTT ratio 1.5–2.5** และ platelet (HIT) · antidote protamine
- Enoxaparin (LMWH) และ fondaparinux ขับทางไต สะสมเมื่อ GFR < 30 เสี่ยงเลือดออก
- Warfarin อย่างเดียวช่วงแรกไม่ได้ เพราะออกฤทธิ์ช้าและช่วงแรก procoagulant ต้อง bridge ด้วย heparin
- Dabigatran ขับทางไตมาก ห้ามใช้เมื่อ GFR ต่ำ''',
            pearl="GFR < 30 → UFH (aPTT 1.5–2.5)", topic="Choice of anticoagulant",
            ref=[f"{D} หน้า 192–193"], nl=["B2.4(3)"]),
    ])

# ---------------------------------------------------------------- 04-04 vWD
S4 = sec("hemato-04-04", "von Willebrand disease (vWD)",
    "AD · primary bleeding (เลือดกำเดา ประจำเดือนมาก) · platelet ปกติ BT ยาว aPTT ยาว correctable · ↓vWF Ag ↓FVIII · DDAVP", minutes=6,
    source=f"{D} หน้า 204–211", nl=["2.3.3-3(4)", "B2.2.1-3(2)"],
    md='''
### กลไก

- **Autosomal dominant** (ส่วนใหญ่) → เป็นได้ทั้งชายหญิง แต่หญิงแสดงอาการมากกว่า (ประจำเดือน)
- **vWF ลดลงหรือทำงานผิดปกติ** — vWF มีสองหน้าที่
  1. **Platelet adhesion** (ยึดเกล็ดเลือดกับ subendothelium) → ขาด = **primary hemostatic bleeding**
  2. **ยืด half-life ของ factor VIII** → ขาด = factor VIII ต่ำ → **aPTT ยาว**

### อาการ (primary hemostatic bleeding)

- **Epistaxis, gingival bleeding**, petechiae, easy bruising
- **Heavy menstruation (hypermenorrhea)**
- เลือดออกนานหลังถอนฟัน/ผ่าตัด

### การตรวจ

| การตรวจ | vWD |
|---|---|
| Platelet count + PBS | **ปกติ** |
| **Bleeding time** | **↑** |
| aPTT | **↑ (แก้ได้ด้วย mixing test)** |
| PT | ปกติ |
| Factor VIII | ↓ |
| **vWF antigen, vWF activity (ristocetin cofactor)** | **↓ (ยืนยัน)** |

### การรักษา

- **Desmopressin (DDAVP)**: กระตุ้นการหลั่ง vWF จาก endothelial cell (ได้ผลใน type 1)
- **vWF concentrate**, factor VIII replacement (ที่มี vWF)
- **Cryoprecipitate** (มี vWF) เมื่อไม่มี concentrate
- **Antifibrinolytic (tranexamic acid)** สำหรับเลือดออกจากเยื่อบุ/ถอนฟัน/ประจำเดือนมาก

> vWD vs hemophilia A: ทั้งคู่ aPTT ยาวแก้ได้ด้วย mixing แต่ **vWD = primary bleeding + BT ยาว + AD (หญิงเป็นได้, พ่อเป็นได้)** · hemophilia = hemarthrosis + BT ปกติ + X-linked (ชาย, ลุงฝั่งแม่)
''',
    pearls=[
        "vWD: AD · หญิงเลือดกำเดา + ประจำเดือนมาก",
        "Platelet ปกติ + BT ยาว + aPTT ยาว (mixing แก้ได้) = vWD",
        "Ix ยืนยัน: vWF antigen + activity",
        "รักษา: DDAVP, vWF concentrate, cryo, tranexamic acid",
    ],
    items=[
        mcq("HEMATO-04-04-1",
            "An 18-year-old woman has excessive bleeding after tooth extraction. Her father also has frequent epistaxis. Platelet count is normal. aPTT 48 s (28–38; control 30 s), PT 12 s (10–14). 1:1 mixing with normal plasma corrects aPTT to 34 s. What is the most likely diagnosis?",
            "von Willebrand disease",
            ["Hemophilia A", "Factor XII deficiency", "Antiphospholipid syndrome", "Prothrombin complex deficiency"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Mucosal bleeding หลังถอนฟัน + **ผู้หญิง** + **พ่อเป็นด้วย (AD)** + aPTT ยาวที่ mixing **แก้ได้** + platelet ปกติ = **vWD**
- Hemophilia A ก็ aPTT ยาวแก้ได้ แต่เป็น **X-linked** (ผู้หญิงแทบไม่แสดงอาการ และพ่อไม่ถ่ายยีนให้ลูกสาวแบบที่พ่อเป็นโรค) และเด่น hemarthrosis
- Factor XII deficiency ไม่ทำให้เลือดออก
- APS ทำให้ thrombosis และ mixing แก้ไม่ได้
- Prothrombin complex (vit K-dependent) deficiency ทำให้ **PT** ยาว''',
            pearl="หญิง + mucosal bleed + พ่อเป็น + aPTT แก้ได้ = vWD", topic="vWD diagnosis",
            ref=[f"{D} หน้า 206–207"], nl=["2.3.3-3(4)"]),
        mcq("HEMATO-04-04-2",
            "A 13-year-old girl has hypermenorrhea since menarche and recurrent epistaxis. CBC is normal. PT is normal, aPTT is prolonged, and bleeding time is prolonged. What is the most appropriate investigation?",
            "vWF antigen and activity",
            ["Factor VIII and IX levels only", "Venous clotting time", "Fibrinogen level", "Platelet aggregation test"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Primary bleeding (epistaxis, ประจำเดือนมาก) + platelet ปกติ + **BT ยาว** + **aPTT ยาว** = vWD (vWF ช่วยทั้ง platelet adhesion และพยุง factor VIII) → ยืนยันด้วย **vWF antigen และ activity**
- Factor VIII/IX levels อย่างเดียว: factor VIII จะต่ำใน vWD ด้วย อาจถูกวินิจฉัยผิดเป็น hemophilia A ถ้าไม่ตรวจ vWF
- VCT เป็นการตรวจ coagulation แบบหยาบ ไม่จำเพาะ
- Fibrinogen ต่ำจะทำให้ PT และ TT ยาวด้วย
- Platelet aggregation ใช้กับ platelet function disorder แต่ aPTT ยาวชี้ไปที่ vWD มากกว่า''',
            pearl="BT ยาว + aPTT ยาว → vWF Ag/activity", topic="vWD investigation",
            ref=[f"{D} หน้า 205, 210–211"], nl=["2.3.3-3(4)"]),
        mcq("HEMATO-04-04-3",
            "A 16-year-old girl has recurrent mucosal bleeding and hypermenorrhea. There is no family history of bleeding. Hb 12.3 g/dL, WBC 8,000/µL, platelet 300,000/µL. PT 12 s; aPTT is prolonged but corrects with mixing. What is the most likely diagnosis?",
            "von Willebrand disease",
            ["Hemophilia A", "Factor VII deficiency", "Antiphospholipid syndrome", "Factor VIII inhibitor"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''เด่น **primary hemostatic bleeding** (mucosal, ประจำเดือนมาก) ในผู้หญิง + platelet ปกติ + aPTT ยาวที่ mixing แก้ได้ = **vWD** (ไม่มีประวัติครอบครัวไม่ได้ตัด vWD — penetrance ไม่เต็มที่)
- Hemophilia A: X-linked, secondary bleeding (hemarthrosis), BT ปกติ
- Factor VII deficiency ทำให้ PT ยาว
- APS: thrombosis และ mixing ไม่แก้
- Factor VIII inhibitor: mixing ไม่แก้''',
            pearl="Primary bleeding + aPTT แก้ได้ = vWD", topic="vWD vs hemophilia",
            ref=[f"{D} หน้า 208–209"], nl=["2.3.3-3(4)"]),
        mcq("HEMATO-04-04-4",
            "A 24-year-old woman with type 1 von Willebrand disease needs a dental extraction. What is the most appropriate prophylactic treatment?",
            "Desmopressin (DDAVP) with tranexamic acid",
            ["Platelet transfusion", "Vitamin K", "Fresh frozen plasma alone", "Prednisolone"],
            explain='''Type 1 vWD (ปริมาณ vWF ลด แต่ทำงานได้) → **DDAVP** กระตุ้นการหลั่ง vWF จาก endothelium + **tranexamic acid** ลดเลือดออกจากเยื่อบุช่องปาก ตามสไลด์ (ถ้าไม่ตอบสนองใช้ vWF concentrate/cryo)
- Platelet transfusion ไม่แก้ เพราะเกล็ดเลือดปกติ ขาด vWF
- Vitamin K ไม่เกี่ยว (vWF/VIII ไม่ขึ้นกับ vit K)
- FFP มี vWF น้อย ต้องให้ปริมาตรมาก ไม่ใช่ตัวเลือกแรก
- Prednisolone ใช้ใน ITP''',
            pearl="vWD type 1 → DDAVP + TXA", topic="vWD treatment",
            ref=[f"{D} หน้า 205"], nl=["2.3.3-3(4)", "B2.4(3)"]),
    ])

# ---------------------------------------------------------------- 04-05 Hemophilia
S5 = sec("hemato-04-05", "Hemophilia A & B",
    "X-linked · ชาย · hemarthrosis · BT ปกติ aPTT ยาว correctable · A ↓FVIII → F8 concentrate/cryo · B ↓FIX → F9 concentrate/FFP", minutes=6,
    source=f"{D} หน้า 212–217", nl=["2.3.3-3(4)", "B2.2.1(4)"],
    md='''
### พันธุกรรม

- **X-linked recessive** → ผู้ชายเป็น ผู้หญิงเป็นพาหะ (ประวัติลุง/น้าฝั่งแม่เลือดออกผิดปกติ)
- **Hemophilia A: ↓factor VIII** (พบมากกว่า) · **Hemophilia B: ↓factor IX**

### อาการ (secondary hemostatic bleeding)

- **Hemarthrosis (พบบ่อยที่สุด)** — ข้อเข่าบวมเฉียบพลันหลังบาดเจ็บเล็กน้อย คล้าย acute monoarthritis
- **Intramuscular hematoma** (iliopsoas — เสริม)
- Mucosal bleeding, **CNS bleeding**
- เลือดออกนานหลังผ่าตัด/ขลิบ

### การตรวจ

- **Bleeding time ปกติ**, platelet ปกติ, PT ปกติ
- **aPTT ยาว แก้ได้ด้วย mixing test** (ถ้าแก้ไม่ได้ = factor inhibitor)
- **↓Specific factor level** (VIII หรือ IX) — ระดับบอกความรุนแรง (< 1% severe — เสริม)

### การรักษา

- Hemarthrosis: **พักข้อ, ประคบเย็น, ยกสูง** (RICE) ร่วมกับให้ factor
- **Hemophilia A**: **factor VIII concentrate** · ไม่มี → **cryoprecipitate**, FFP
- **Hemophilia B**: **factor IX concentrate** · ไม่มี → **FFP** (**cryoprecipitate ไม่มี factor IX**)
- Cryoprecipitate มี **factor VIII, XIII, vWF, fibrinogen**
- หลีกเลี่ยงฉีดยาเข้ากล้าม, aspirin/NSAIDs (เสริม)

> เด็กชายเข่าบวมหลังล้ม มี bruise ง่าย ลุงตายจากเลือดออกหลังผ่าตัด + aPTT ยาว BT ปกติ = hemophilia · ถ้า aPTT แก้ได้ด้วย mixing แต่ยังต้องแยก A กับ B ด้วย factor assay
''',
    pearls=[
        "Hemophilia: X-linked · hemarthrosis พบบ่อยสุด",
        "BT ปกติ + aPTT ยาว (mixing แก้ได้) + ↓F VIII/IX",
        "Hemophilia B ห้ามตอบ cryo (ไม่มี F IX) → F IX concentrate หรือ FFP",
        "Cryo = F VIII, XIII, vWF, fibrinogen",
    ],
    items=[
        mcq("HEMATO-04-05-1",
            "A 5-year-old boy develops rapid swelling of the right knee after falling while playing. He has always bruised easily, and a maternal uncle died of bleeding after minor surgery. PE: multiple ecchymoses; right knee swollen, warm, and tender. Arthrocentesis: bloody fluid. Bleeding time normal, aPTT 67 s, PT 10 s. What is the most likely diagnosis?",
            "Hemophilia",
            ["Septic arthritis", "Juvenile idiopathic arthritis", "von Willebrand disease", "Immune thrombocytopenia"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''เด็กชาย + **hemarthrosis** หลังบาดเจ็บเล็กน้อย + bruise ง่าย + **ลุงฝั่งแม่** เลือดออกตาย (X-linked) + **BT ปกติ aPTT ยาว PT ปกติ** = hemophilia (A หรือ B — แยกด้วย factor assay; ถ้า mixing ไม่แก้ ต้องคิดถึง inhibitor)
- Septic arthritis มีไข้ น้ำในข้อเป็นหนอง ไม่ใช่เลือด และ aPTT ปกติ
- JIA ไม่ทำให้น้ำในข้อเป็นเลือดและ aPTT ยาว
- vWD เด่น mucosal bleeding และ BT ยาว
- ITP จะ platelet ต่ำ และไม่ค่อยมี hemarthrosis''',
            pearl="เด็กชาย hemarthrosis + aPTT ยาว + ลุงฝั่งแม่ = hemophilia", topic="Hemophilia diagnosis",
            ref=[f"{D} หน้า 212, 214–215"], nl=["2.3.3-3(4)", "B2.2.1(4)"]),
        mcq("HEMATO-04-05-2",
            "A 20-year-old man has right knee swelling after minor trauma. He has no previous abnormal bleeding or surgery. Arthrocentesis: unclotted blood. Platelet count normal. aPTT 58 s (25–38), PT 11.2 s (10–13), 1:1 mixing aPTT 35 s. Bleeding time 5 min (normal < 7). Factor VIII activity is 85% and factor IX activity is 4%. What is the most likely diagnosis?",
            "Hemophilia B",
            ["von Willebrand disease", "Factor XII deficiency", "Vitamin K deficiency", "Liver disease"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มผล factor assay ให้แยก A/B ได้)",
            explain='''Hemarthrosis + **BT ปกติ** + aPTT ยาวที่ **mixing แก้ได้** + PT ปกติ = factor deficiency ใน intrinsic pathway · **factor IX 4%** = **hemophilia B** (mild ทำให้ไม่มีอาการจนบาดเจ็บ)
- vWD: BT ยาว และเด่น mucosal bleeding
- Factor XII deficiency ไม่ทำให้เลือดออกเลย
- Vitamin K deficiency และ liver disease ทำให้ **PT** ยาวด้วย''',
            pearl="aPTT ยาว + BT ปกติ + ↓F IX = hemophilia B", topic="Hemophilia B",
            ref=[f"{D} หน้า 213, 216–217"], nl=["2.3.3-3(4)"]),
        mcq("HEMATO-04-05-3",
            "A 12-year-old boy with known severe hemophilia B presents with acute hemarthrosis of the left knee. Factor IX concentrate is not available at this hospital. Which blood product is most appropriate?",
            "Fresh frozen plasma",
            ["Cryoprecipitate", "Platelet concentrate", "Packed red cells", "Albumin"],
            explain='''Hemophilia B ขาด **factor IX** · ไม่มี factor IX concentrate → ใช้ **FFP** (มีทุก factor) ตามสไลด์ ร่วมกับ RICE
- **Cryoprecipitate ไม่มี factor IX** (มี VIII, XIII, vWF, fibrinogen) ใช้แทน factor VIII ใน hemophilia A
- Platelet concentrate ไม่แก้ปัญหา factor
- PRC ให้เมื่อซีดมาก ไม่ได้แก้การแข็งตัว
- Albumin ไม่มี coagulation factor''',
            pearl="Hemophilia B ไม่มี F IX conc → FFP (ไม่ใช่ cryo)", topic="Hemophilia B treatment",
            ref=[f"{D} หน้า 213, 339–340"], nl=["2.3.3-3(4)", "B2.4(1)"]),
    ])

LECTURE = lecture("04", "Coagulation disorders",
    "Approach to bleeding · coagulogram · vitamin K · anticoagulants · vWD · hemophilia",
    objectives=[
        "แยก primary กับ secondary hemostatic bleeding จากประวัติและเลือกการตรวจได้",
        "แปลผล PT, aPTT, TT และ mixing test เป็นกลุ่มสาเหตุได้",
        "จัดการ warfarin overdose ตามการมีเลือดออกและระดับ INR ได้",
        "แยก vWD กับ hemophilia และเลือก blood product/ยาได้ถูก",
    ],
    sections=[S1, S2, S3, S4, S5])
