from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Hemato"

# ---------------------------------------------------------------- 09-01 Febrile neutropenia
S1 = sec("hemato-09-01", "Febrile neutropenia",
    "BT ≥38.3 ครั้งเดียว หรือ ≥38 นาน 1 ชม. + ANC <500 (หรือคาดว่าจะ <500 ใน 48 ชม.) · empirical anti-pseudomonal ทันที · G-CSF ป้องกันใน high risk", minutes=5,
    source=f"{D} หน้า 330–335", nl=["2.3.3(2)", "2.2.48"],
    md='''
### นิยาม

- **Fever**: BT **≥ 38.3°C ครั้งเดียว** หรือ **≥ 38°C ต่อเนื่องอย่างน้อย 1 ชั่วโมง**
- **Neutropenia**: **ANC < 500/µL** หรือ **คาดว่าจะลดลงต่ำกว่า 500 ภายใน 48 ชั่วโมง**
- พบบ่อย**หลังเคมีบำบัด** (nadir ราววันที่ 7–14 — เสริม)
- ANC = WBC × (% neutrophil + % band) (เสริม)

### การตรวจ

- W/U หาแหล่งติดเชื้อตามสงสัย: hemoculture อย่างน้อย 2 ขวด (รวมจาก central line), UA/urine culture, CXR (เสริม)
- อาการอักเสบอาจไม่ชัดเพราะไม่มี neutrophil

### การรักษา

- **Empirical antibiotic ที่คลุม Pseudomonas ทันที** (ภายใน 1 ชั่วโมง — เสริม)
  - **Piperacillin/tazobactam**
  - **Carbapenem** (meropenem, imipenem)
  - **Ceftazidime**
  - **Cefepime**
- เพิ่ม vancomycin เมื่อสงสัย catheter/skin/MRSA หรือ hemodynamic ไม่คงที่ · antifungal เมื่อไข้ไม่ลงหลัง 4–7 วัน (เสริม)
- **Prophylaxis: G-CSF กรณี high risk** (G-CSF ไม่ใช่การรักษาหลักเมื่อมีไข้แล้ว)

### ปัญหาเชิงจริยธรรม/การสื่อสาร

- ผู้ป่วยมะเร็งที่ได้เคมีบำบัดแล้วกินสมุนไพรร่วม → **แนะนำงดสมุนไพร** (อาจกดไขกระดูก/ตีกับยา) อธิบายเหตุผลด้วยความเคารพ (ข้อสอบเก่าในสไลด์)

> โจทย์หลังเคมีบำบัด 7–14 วัน + ไข้สูง + WBC < 1,000 → **ceftazidime/cefepime/pip-tazo/carbapenem** · cefazolin ไม่คลุม Pseudomonas · amphotericin B ไม่ใช่ยาเริ่มต้น
''',
    pearls=[
        "FN: ไข้ ≥38.3 ครั้งเดียว หรือ ≥38 นาน 1 ชม. + ANC <500",
        "Empirical anti-pseudomonal: pip/tazo, carbapenem, ceftazidime, cefepime",
        "G-CSF = ป้องกันใน high risk ไม่ใช่ยารักษาหลัก",
    ],
    items=[
        mcq("HEMATO-09-01-1",
            "A 60-year-old man with stage IIB lymphoma completed his second cycle of chemotherapy 10 days ago. He now has high fever with chills. BT 40°C, RR 24/min, PR 100/min, BP 118/70 mmHg. PE: unremarkable. CBC: Hb 10.5 g/dL, Hct 32%, WBC 400/µL, platelet 70,000/µL. After blood cultures, what is the most appropriate management?",
            "Intravenous ceftazidime",
            ["G-CSF alone", "Intravenous cefazolin", "Intravenous amphotericin B", "PRC transfusion"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ไข้หลังเคมีบำบัด + WBC 400 (ANC < 500) = **febrile neutropenia** → **empirical antibiotic คลุม Pseudomonas ทันที** เช่น **ceftazidime** (หรือ cefepime, pip/tazo, carbapenem)
- G-CSF เป็น prophylaxis ใน high risk ไม่ใช่การรักษาเดี่ยวเมื่อมีไข้แล้ว
- Cefazolin เป็น 1st-gen cephalosporin ไม่คลุม Pseudomonas/gram-negative ดื้อยา
- Amphotericin B ใช้เมื่อไข้ไม่ลงหลังยาปฏิชีวนะ 4–7 วันหรือสงสัยเชื้อรา
- PRC ไม่จำเป็น (Hb 10.5)''',
            pearl="FN → anti-pseudomonal β-lactam ทันที", topic="FN treatment",
            ref=[f"{D} หน้า 331–333"], nl=["2.3.3(2)"]),
        mcq("HEMATO-09-01-2",
            "A 45-year-old woman receiving chemotherapy for breast cancer has an oral temperature of 38.1°C sustained over 90 minutes. CBC: WBC 1,200/µL with neutrophils 30% and bands 5%. Which statement is correct?",
            "She meets the definition of febrile neutropenia",
            ["She does not have fever because the temperature is below 38.3°C", "She does not have neutropenia because WBC is above 1,000/µL", "Antibiotics should wait until blood culture results return", "Oral amoxicillin is adequate empirical therapy"],
            explain='''ไข้: **≥ 38°C ต่อเนื่อง ≥ 1 ชั่วโมง** ✓ · ANC = 1,200 × (30% + 5%) = **420 < 500** ✓ → **febrile neutropenia** ต้องให้ anti-pseudomonal ทันที
- 38.3°C เป็นเกณฑ์สำหรับวัด**ครั้งเดียว** ส่วนกรณีนี้ใช้เกณฑ์ ≥ 38 นาน 1 ชม.
- ต้องดู ANC ไม่ใช่ WBC รวม
- การรอผลเพาะเชื้อเพิ่มอัตราตาย
- Amoxicillin ไม่คลุม Pseudomonas''',
            pearl="คำนวณ ANC = WBC × (%N + %band)", topic="FN definition",
            ref=[f"{D} หน้า 330"], nl=["2.3.3(2)"]),
        mcq("HEMATO-09-01-3",
            "A patient with cancer receiving chemotherapy develops leukopenia. You learn he has also been taking an unregistered herbal remedy throughout treatment. What is the most appropriate action?",
            "Advise him to stop the herbal remedy and explain why",
            ["Continue chemotherapy together with the herbal remedy", "Report the patient to the Food and Drug Administration", "Stop chemotherapy permanently", "Ignore it because herbs are natural"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เฉลยเป็นภาพ — ตอบตามหลักเวชปฏิบัติ)",
            explain='''สมุนไพรที่ไม่ทราบส่วนประกอบอาจ**กดไขกระดูก ตีกับยาเคมีบำบัด หรือปนเปื้อน** → **แนะนำให้งดและอธิบายเหตุผล** อย่างเคารพการตัดสินใจของผู้ป่วย แล้วประเมิน neutropenia/ปรับเคมีบำบัดตามแนวทาง
- ให้เคมีบำบัดร่วมกับสมุนไพรต่อเสี่ยงพิษเพิ่ม
- การแจ้ง อย. เกี่ยวกับผลิตภัณฑ์ ไม่ใช่การจัดการผู้ป่วยตรงหน้า (และไม่ใช่การ "รายงานผู้ป่วย")
- หยุดเคมีบำบัดถาวรเกินเหตุ
- เพิกเฉยไม่ปลอดภัย''',
            pearl="ผู้ป่วยเคมีบำบัดกินสมุนไพร → แนะนำงด + อธิบาย", topic="Herbal use in chemotherapy",
            ref=[f"{D} หน้า 334–335"], nl=["2.3.19(2)"]),
    ])

# ---------------------------------------------------------------- 09-02 Blood products
F_BP = fig("hemato-09-02-f1", "เลือกส่วนประกอบเลือดให้ตรงกับสิ่งที่ขาด", '''<svg viewBox="0 0 740 360">
 <rect x="20" y="12" width="220" height="160" rx="12" class="badsoft"/>
 <text x="130" y="36" text-anchor="middle" class="ta">PRC / LPRC / LD-PRC</text>
 <text x="34" y="62" class="t2">• Hemorrhagic shock</text>
 <text x="48" y="78" class="t3">(Hb เท่าไรก็ได้)</text>
 <text x="34" y="100" class="t2">• Hb &lt; 7 g/dL</text>
 <text x="34" y="120" class="t2">• Hb &lt; 8 ใน CAD</text>
 <text x="34" y="142" class="t3">LPRC/LD: ↓WBC → ↓FNHTR</text>
 <text x="34" y="160" class="t3">ฉุกเฉินไม่รู้กรุ๊ป → group O</text>
 <rect x="260" y="12" width="220" height="160" rx="12" class="c1soft"/>
 <text x="370" y="36" text-anchor="middle" class="ta">Platelet (SDP/PC/LPPC)</text>
 <text x="274" y="62" class="t2">• &lt; 50,000 + active bleeding</text>
 <text x="274" y="88" class="tb">ป้องกัน:</text>
 <text x="274" y="108" class="t2">&lt; 10,000 ทั่วไป</text>
 <text x="274" y="128" class="t2">&lt; 20,000 + ไข้/DIC</text>
 <text x="274" y="148" class="t2">&lt; 50,000 + หัตถการ</text>
 <text x="274" y="166" class="t2">&lt; 100,000 + neurosurgery</text>
 <rect x="500" y="12" width="220" height="160" rx="12" class="c2soft"/>
 <text x="610" y="36" text-anchor="middle" class="ta">FFP (ทุก factor)</text>
 <text x="514" y="62" class="t2">• Multiple factor deficiency</text>
 <text x="528" y="82" class="t3">cirrhosis, DIC, massive Tx</text>
 <text x="514" y="106" class="t2">• Warfarin (ไม่มี PCC)</text>
 <text x="514" y="128" class="t2">• Plasma exchange ใน TTP</text>
 <text x="514" y="150" class="t2">• Hemophilia B (ไม่มี F IX)</text>
 <rect x="20" y="186" width="340" height="160" rx="12" class="misssoft"/>
 <text x="190" y="210" text-anchor="middle" class="ta">Cryoprecipitate</text>
 <text x="190" y="232" text-anchor="middle" class="tb">Fibrinogen · F VIII · F XIII · vWF</text>
 <text x="34" y="262" class="t2">• Fibrinogen &lt; 100 mg/dL (DIC, liver) — TT ยาว</text>
 <text x="34" y="286" class="t2">• Hemophilia A (ไม่มี F VIII concentrate)</text>
 <text x="34" y="310" class="t2">• vWD (ไม่มี vWF concentrate)</text>
 <text x="34" y="334" class="t3">ไม่มี F IX และ vitamin K-dependent factors</text>
 <rect x="380" y="186" width="340" height="160" rx="12" class="oksoft"/>
 <text x="550" y="210" text-anchor="middle" class="ta">Concentrates</text>
 <text x="394" y="240" class="tb">PCC = F II, VII, IX, X</text>
 <text x="394" y="262" class="t2">→ warfarin overdose (เร็ว ปริมาตรน้อย)</text>
 <text x="394" y="292" class="tb">Specific factor</text>
 <text x="394" y="314" class="t2">F VIII → hemophilia A</text>
 <text x="394" y="334" class="t2">F IX → hemophilia B</text>
</svg>''', "จับคู่สิ่งที่ขาดกับส่วนประกอบเลือด: RBC → PRC · เกล็ดเลือด → platelet · หลาย factor → FFP · fibrinogen/VIII/vWF → cryo · vitamin K-dependent → PCC")

S2 = sec("hemato-09-02", "Blood products & indications",
    "PRC: shock หรือ Hb <7 (<8 CAD) · Platelet: <50k bleed, <10k ป้องกัน · FFP: multiple factor · Cryo: fibrinogen <100, VIII, XIII, vWF · PCC: II VII IX X", minutes=7,
    source=f"{D} หน้า 336–347", nl=["B2.4(1)", "2.2.44"],
    md='''
### RBC

| ชนิด | หมายเหตุ |
|---|---|
| Packed red cell (PRC) | มาตรฐาน |
| **Leukocyte-poor PRC (LPRC)** / **leukocyte-depleted PRC (LD-PRC)** | **↓WBC → ↓risk FNHTR**, ใช้ในผู้รับเลือดประจำ (thalassemia) |

- ข้อบ่งชี้: **hemorrhagic shock (Hb เท่าไรก็ได้)**, **Hb < 7 g/dL** (**Hb < 8** ใน coronary artery disease)
- ฉุกเฉินเลือดออกมากและไม่ทราบกรุ๊ป → **PRC group O** (เสริม: O Rh-negative ในหญิงวัยเจริญพันธุ์) ระหว่างรอ crossmatch

### Platelet

- Single donor platelet (SDP), platelet concentrate (PC), leukocyte-poor PC (LPPC)
- ข้อบ่งชี้

| สถานการณ์ | ให้เมื่อ platelet ต่ำกว่า |
|---|---|
| **Active bleeding** | **50,000** |
| ป้องกันเลือดออกทั่วไป | **10,000** |
| มีไข้ หรือ DIC | **20,000** |
| ทำหัตถการ invasive | **50,000** |
| **Neurosurgery** | **100,000** |

### Plasma products

- **FFP**: มี**ทุก coagulation factor** และ plasma protein → multiple factor deficiency (**cirrhosis, DIC, massive transfusion**), warfarin overdose (ไม่มี PCC), **plasma exchange ใน TTP**, hemophilia B (ไม่มี factor IX)
- **Cryoprecipitate**: **fibrinogen, factor VIII, factor XIII, vWF** → **fibrinogen < 100 mg/dL** (DIC, liver disease), hemophilia A/vWD เมื่อไม่มี concentrate
- **Specific factor concentrate**: factor VIII (hemophilia A), factor IX (hemophilia B)
- **PCC**: vitamin K-dependent factors **II, VII, IX, X** → **warfarin overdose**

[[fig:hemato-09-02-f1]]

> ตับแข็งเลือดออก ได้ PRC + FFP แล้วไม่หยุด + **TT ยาว** → fibrinogen ต่ำ → **cryoprecipitate** · ตับแข็ง UGIB + PT/aPTT ยาว (TT ไม่ได้ให้) → **FFP**
''',
    figs=[F_BP],
    pearls=[
        "PRC: shock หรือ Hb < 7 (< 8 ใน CAD) · ฉุกเฉินไม่รู้กรุ๊ป → group O",
        "Platelet: < 50k + bleed · < 10k ป้องกัน · < 20k + ไข้/DIC · < 100k neurosurgery",
        "FFP = ทุก factor · cryo = fibrinogen, VIII, XIII, vWF · PCC = II VII IX X",
        "TT ยาว/fibrinogen < 100 → cryo",
    ],
    items=[
        mcq("HEMATO-09-02-1",
            "At the emergency department, a 45-year-old man arrives after a severe car accident with massive ongoing bleeding and hypotension. His blood group is unknown. What is the most appropriate initial transfusion management?",
            "Transfuse group O packed red cells as soon as possible",
            ["IV fluid loading with albumin", "IV fluid loading with dextran", "Transfuse group AB packed red cells as soon as possible", "NSS at 80 mL/hr while waiting for cross-matched PRC"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Hemorrhagic shock ต้องให้เลือดทันที (สไลด์: hemorrhagic shock ให้ PRC ที่ Hb เท่าไรก็ได้) · ไม่รู้กรุ๊ป → **PRC group O** (universal donor ของ red cell) ระหว่างรอ crossmatch
- Albumin และ dextran ไม่ขนออกซิเจน และ dextran รบกวนการแข็งตัวของเลือด
- Group AB เป็น universal **recipient** ของ RBC (และ universal donor ของ plasma) — ให้ RBC AB กับผู้ป่วยกรุ๊ปอื่นจะเกิด AHTR
- NSS 80 mL/hr ช้าเกินไปสำหรับ shock และการรอ crossmatch เสียเวลา''',
            pearl="Massive bleed ไม่รู้กรุ๊ป → PRC group O", topic="Emergency transfusion",
            ref=[f"{D} หน้า 337, 342–343"], nl=["B2.4(1)", "2.2.47"]),
        mcq("HEMATO-09-02-2",
            "A man with cirrhosis presents with hematemesis. PE: marked ascites and crepitations in both lungs. Hct 35%, platelet 60,000/µL. PT and aPTT are both prolonged; fibrinogen is 180 mg/dL. Which blood product is most appropriate?",
            "Fresh frozen plasma",
            ["Packed red cells", "Platelet concentrate", "Cryoprecipitate", "Cryo-removed plasma"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มค่า fibrinogen)",
            explain='''Cirrhosis = **multiple factor deficiency** → PT/aPTT ยาว + มีเลือดออก → **FFP** (มีทุก factor)
- PRC: Hct 35% ยังไม่ถึงเกณฑ์ และน้ำเกิน (crepitation) จึงไม่ควรเพิ่มปริมาตรโดยไม่จำเป็น
- Platelet: 60,000 สูงกว่าเกณฑ์ 50,000 สำหรับ active bleeding
- Cryoprecipitate ใช้เมื่อ fibrinogen < 100 — ที่นี่ 180
- Cryo-removed plasma ขาด fibrinogen/VIII/vWF ใช้ในบาง plasma exchange ไม่ใช่ตัวเลือกแรก''',
            pearl="ตับแข็ง + PT/aPTT ยาว + เลือดออก → FFP", topic="FFP indication",
            ref=[f"{D} หน้า 339, 344–345"], nl=["B2.4(1)", "2.2.44"]),
        mcq("HEMATO-09-02-3",
            "A 50-year-old man with cirrhosis develops a large left thigh hematoma after a motorcycle accident without fracture. Two units of PRC and FFP were given, but bleeding continues. Platelet 91,000/µL (no MAHA), aPTT 50 s (25–35), PT 21 s (10–13), INR 1.87, thrombin time 20 s (10–13). What is the most useful treatment to stop the bleeding?",
            "Cryoprecipitate",
            ["Single-donor platelets", "More fresh frozen plasma", "Recombinant factor VIIa", "Cryo-removed plasma"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''**TT ยาว** หลังได้ FFP แล้ว = **fibrinogen ต่ำ** (ตับสร้างไม่ได้) → **cryoprecipitate** (fibrinogen, VIII, XIII, vWF) — สไลด์ใช้ใน fibrinogen < 100
- Platelet 91,000 สูงกว่าเกณฑ์ 50,000 สำหรับ active bleeding
- FFP มี fibrinogen แต่ความเข้มข้นต่ำ ต้องให้ปริมาณมาก
- rFVIIa แพงและเสี่ยง thrombosis ไม่ใช่ตัวเลือกแรก และไม่แก้ fibrinogen ต่ำ
- Cryo-removed plasma ไม่มี fibrinogen''',
            pearl="TT ยาว → cryoprecipitate", topic="Cryoprecipitate indication",
            ref=[f"{D} หน้า 340, 346–347"], nl=["B2.4(1)"]),
        mcq("HEMATO-09-02-4",
            "A 68-year-old woman with stable coronary artery disease is admitted for a non-bleeding gastric ulcer. Her Hb is 7.6 g/dL and she has exertional chest discomfort. Vital signs are stable. What is the most appropriate transfusion decision?",
            "Transfuse packed red cells because Hb is below 8 g/dL in coronary artery disease",
            ["No transfusion because Hb is above 7 g/dL", "Transfuse fresh frozen plasma", "Transfuse platelets", "Transfuse only after Hb falls below 6 g/dL"],
            explain='''เกณฑ์ PRC ในสไลด์: **Hb < 7** ทั่วไป แต่ **Hb < 8 ในผู้ป่วย CAD** (โดยเฉพาะมีอาการเจ็บหน้าอก) → Hb 7.6 จึง**ให้ PRC**
- ใช้เกณฑ์ 7 สำหรับผู้ป่วยที่ไม่มีโรคหัวใจเท่านั้น
- FFP และ platelet ไม่เพิ่มการขนส่งออกซิเจน
- รอ Hb < 6 เสี่ยง myocardial ischemia''',
            pearl="CAD → transfuse เมื่อ Hb < 8", topic="PRC threshold",
            ref=[f"{D} หน้า 337"], nl=["B2.4(1)"]),
        mcq("HEMATO-09-02-5",
            "A 45-year-old man with platelet count 60,000/µL from chronic liver disease is scheduled for an elective craniotomy for a meningioma. He has no active bleeding. What is the most appropriate platelet management?",
            "Transfuse platelets to achieve at least 100,000/µL before surgery",
            ["No platelet transfusion because count is above 50,000/µL", "Transfuse only if count falls below 10,000/µL", "Give cryoprecipitate instead of platelets", "Transfuse only if fever develops"],
            explain='''เกณฑ์ platelet สำหรับ **neurosurgery คือ < 100,000** (ตำแหน่งที่เลือดออกเล็กน้อยก็อันตราย) → ต้องให้ platelet ก่อนผ่าตัด
- 50,000 เป็นเกณฑ์สำหรับหัตถการ invasive ทั่วไปและ active bleeding
- 10,000 เป็นเกณฑ์ป้องกันในผู้ป่วยทั่วไปที่ไม่มีเลือดออก
- Cryoprecipitate ไม่ได้เพิ่ม platelet
- 20,000 เป็นเกณฑ์เมื่อมีไข้/DIC''',
            pearl="Neurosurgery → platelet ≥ 100,000", topic="Platelet thresholds",
            ref=[f"{D} หน้า 338"], nl=["B2.4(1)"]),
    ])

# ---------------------------------------------------------------- 09-03 Transfusion reactions
F_TR = fig("hemato-09-03-f1", "ปฏิกิริยาจากการให้เลือดแบบเฉียบพลัน แยกตามอาการนำ", '''<svg viewBox="0 0 740 400">
 <defs><marker id="hemato-09-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="200" y="10" width="340" height="44" rx="10" class="bad"/>
 <text x="370" y="30" text-anchor="middle" class="tw">ปฏิกิริยาระหว่างให้เลือด (&lt; 24 ชม.)</text>
 <text x="370" y="46" text-anchor="middle" class="tw">→ หยุดให้เลือดทันทีทุกกรณี</text>
 <path d="M260 54L120 88" class="ln" marker-end="url(#hemato-09-03-a)"/>
 <path d="M370 54V88" class="ln" marker-end="url(#hemato-09-03-a)"/>
 <path d="M480 54L620 88" class="ln" marker-end="url(#hemato-09-03-a)"/>
 <rect x="20" y="90" width="210" height="36" rx="8" class="c2"/>
 <text x="125" y="113" text-anchor="middle" class="tw">ไข้</text>
 <rect x="265" y="90" width="210" height="36" rx="8" class="miss"/>
 <text x="370" y="113" text-anchor="middle" class="tw">ผื่น/แพ้</text>
 <rect x="510" y="90" width="210" height="36" rx="8" class="c1"/>
 <text x="615" y="113" text-anchor="middle" class="tw">เหนื่อย</text>
 <rect x="20" y="134" width="210" height="80" rx="8" class="badsoft"/>
 <text x="32" y="154" class="tb">AHTR (ABO)</text>
 <text x="32" y="172" class="t3">หนาวสั่น BP ต่ำ ปวดหลัง/สีข้าง</text>
 <text x="32" y="188" class="t3">ปัสสาวะสีเข้ม · DAT บวก</text>
 <text x="32" y="206" class="t2">→ IV fluid, ดู urine output</text>
 <rect x="20" y="220" width="210" height="80" rx="8" class="badsoft"/>
 <text x="32" y="240" class="tb">Bacterial contamination</text>
 <text x="32" y="258" class="t3">ไข้สูง septic shock ± DIC</text>
 <text x="32" y="274" class="t3">H/C บวกทั้งคนและถุง</text>
 <text x="32" y="292" class="t2">→ resuscitate + ATB</text>
 <rect x="20" y="306" width="210" height="84" rx="8" class="box"/>
 <text x="32" y="326" class="tb">FNHTR</text>
 <text x="32" y="344" class="t3">cytokine จาก WBC ในถุง</text>
 <text x="32" y="360" class="t3">ไม่มี hemolysis</text>
 <text x="32" y="378" class="t2">→ paracetamol, ให้ต่อได้</text>
 <rect x="265" y="134" width="210" height="110" rx="8" class="misssoft"/>
 <text x="277" y="154" class="tb">Allergic (mild)</text>
 <text x="277" y="172" class="t3">ผื่น คัน หน้าแดง</text>
 <text x="277" y="190" class="t2">→ antihistamine</text>
 <text x="277" y="208" class="t2">ให้เลือดต่อได้</text>
 <rect x="265" y="252" width="210" height="138" rx="8" class="badsoft"/>
 <text x="277" y="272" class="tb">Anaphylaxis</text>
 <text x="277" y="290" class="t3">BP ต่ำ wheeze AOC</text>
 <text x="277" y="308" class="t2">→ IM epinephrine</text>
 <text x="277" y="332" class="t3">ป้องกัน: premed</text>
 <text x="277" y="348" class="t3">antihistamine</text>
 <text x="277" y="366" class="t3">washed blood ถ้าเคยรุนแรง</text>
 <rect x="510" y="134" width="210" height="122" rx="8" class="c1soft"/>
 <text x="522" y="154" class="tb">TACO</text>
 <text x="522" y="174" class="t2">JVP ↑ · BP ↑</text>
 <text x="522" y="192" class="t3">pulmonary edema</text>
 <text x="522" y="208" class="t3">effusion · BNP ↑</text>
 <text x="522" y="230" class="ta">→ O2 + diuretic</text>
 <rect x="510" y="264" width="210" height="126" rx="8" class="c2soft"/>
 <text x="522" y="284" class="tb">TRALI</text>
 <text x="522" y="304" class="t2">JVP ปกติ · BP ↓ · ไข้</text>
 <text x="522" y="322" class="t3">non-cardiogenic edema</text>
 <text x="522" y="338" class="t3">มักหลัง FFP/plasma</text>
 <text x="522" y="362" class="ta">→ O2 + ventilation</text>
 <text x="522" y="380" class="t3">ห้าม diuretic</text>
</svg>''', "หยุดให้เลือดก่อนเสมอ แล้วแยกตามอาการนำ — ไข้: แยก AHTR/bacterial ออกก่อนจึงเรียก FNHTR · เหนื่อย: ดู JVP และ BP แยก TACO กับ TRALI")

S3 = sec("hemato-09-03", "Transfusion reactions & massive transfusion",
    "AHTR (ABO) stop + IV fluid · DHTR (minor antigen) DAT/IAT บวก · FNHTR paracetamol · TACO (JVP↑ BP↑) diuretic · TRALI (JVP ปกติ BP↓) ventilation · massive: ↓Ca ↑K", minutes=9,
    source=f"{D} หน้า 348–371", nl=["2.2.21", "B2.2.2(4)", "B2.4(1)"],
    md='''
### ประเภท

| | Acute (< 24 ชม.) | Delayed (> 24 ชม.) |
|---|---|---|
| Hemolytic | **AHTR** | **DHTR** |
| Non-hemolytic | FNHTR, bacterial contamination, TACO, TRALI, allergic/anaphylaxis | Post-transfusion purpura, TA-GVHD |

[[fig:hemato-09-03-f1]]

### Acute hemolytic transfusion reaction (AHTR)

- สาเหตุ: **ABO incompatibility** (ส่วนใหญ่จาก human error ติดฉลากผิดคน — เสริม) → **intravascular hemolysis**
- **ไข้หนาวสั่น, BP ต่ำ, ปวดสีข้าง/หลัง, hemoglobinuria** (เลือดออกในปัสสาวะ/สีน้ำตาล) ภายในไม่กี่นาทีแรก · ± DIC, AKI
- **DAT บวก**
- Mx: **หยุดให้เลือดทันที**, **IV fluid**, monitor V/S และ **urine output** (ส่งถุงเลือด + เลือดผู้ป่วยตรวจซ้ำ — เสริม)

### Bacterial contamination

- ไข้หนาวสั่น **septic shock** (BP ต่ำ HR เร็ว) ± DIC · **H/C บวกทั้งจากผู้ป่วยและถุงเลือด** (platelet เสี่ยงสุดเพราะเก็บที่อุณหภูมิห้อง — เสริม)
- Mx: หยุดให้เลือด, resuscitation, **antibiotic**

### Febrile non-hemolytic transfusion reaction (FNHTR)

- สาเหตุ: **cytokine จาก WBC ในถุงเลือด** · ไข้ ไม่มีหลักฐาน hemolysis
- Mx: หยุดให้เลือด → **R/O AHTR และ bacterial contamination** → **paracetamol** → **ให้ต่อได้เมื่อดีขึ้น**
- ป้องกัน: **leukocyte-depleted products**

### TRALI vs TACO

| | TRALI | TACO |
|---|---|---|
| กลไก | Anti-HLA/anti-neutrophil Ab ใน plasma ผู้บริจาค → **non-cardiogenic pulmonary edema** (มักหลัง FFP/platelet) | ให้เลือดเร็ว/มากเกิน → **cardiogenic pulmonary edema** (ผู้สูงอายุ หัวใจ/ไตไม่ดี) |
| JVP | **ปกติ** | **↑** |
| BP | **↓** | **↑** |
| ไข้ | มีได้ | ไม่มี |
| CXR | bilateral infiltration | infiltration + **pleural effusion** + cardiomegaly · **↑BNP** |
| ตอบสนองต่อ diuretic | ไม่ (อาจแย่ลง) | **ดี** |
| Mx | หยุดให้เลือด + **O2/ventilation support** | หยุดให้เลือด + O2 + **diuretic** |

### Allergic / anaphylaxis

- **Hypersensitivity type I** ต่อ protein ใน plasma (IgA deficiency — เสริม)
- Mild: ผื่น คัน หน้าแดง → **antihistamine, ให้เลือดต่อได้**
- Severe: BP ต่ำ HR เร็ว หอบ wheeze คลื่นไส้ ถ่ายเหลว ซึม → resuscitation + **IM epinephrine**
- ป้องกัน: premedication antihistamine · **washed blood** ถ้าเคยรุนแรง

### Delayed hemolytic transfusion reaction (DHTR)

- สาเหตุ: **minor blood group incompatibility** (Kidd, Rh — เสริม) ใน anamnestic response
- **Onset หลายวัน–สัปดาห์** หลังให้เลือด: ไข้, ซีดลง, ตัวเหลือง, retic สูง
- **DAT บวก + indirect Coombs (antibody screen) บวก**
- Mx: **supportive**

### Massive transfusion complications

- **Dilutional coagulopathy & thrombocytopenia**
- **Hyperkalemia** (K รั่วจาก RBC เก่า)
- **Citrate toxicity** (สารกันเลือดแข็งในถุง จับ Ca) → **hypocalcemia (QT prolong, หัวใจหยุดเต้น)** และ **metabolic alkalosis** (citrate → bicarbonate)
- **Hypothermia**

> TRALI vs TACO จำง่าย: **TACO = น้ำเกิน (JVP ↑ BP ↑) → furosemide** · **TRALI = ปอดอักเสบ (JVP ปกติ BP ↓ ไข้) → ventilator**
''',
    figs=[F_TR],
    pearls=[
        "AHTR: ABO · ไข้ หนาวสั่น BP ต่ำ ปวดสีข้าง hemoglobinuria → stop + IV fluid",
        "DHTR: วัน–สัปดาห์หลังให้เลือด + DAT และ IAT บวก → supportive",
        "FNHTR: R/O AHTR/sepsis → paracetamol → ให้ต่อได้ · ป้องกันด้วย LD product",
        "TACO: JVP↑ BP↑ → diuretic · TRALI: JVP ปกติ BP↓ → ventilation",
        "Massive transfusion: ↑K, ↓Ca (citrate), alkalosis, hypothermia, dilutional coagulopathy",
    ],
    items=[
        mcq("HEMATO-09-03-1",
            "A 43-year-old man with upper GI bleeding develops fever with chills and flank pain during the first 20 minutes of a PRC transfusion. BT 39°C, PR 120/min, RR 32/min, BP 90/60 mmHg. His urine becomes dark red. What is the most likely cause?",
            "Acute hemolytic transfusion reaction",
            ["Anaphylaxis", "Transfusion-associated sepsis", "Febrile non-hemolytic transfusion reaction", "Transfusion-related acute lung injury"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มปัสสาวะสีเข้ม)",
            explain='''เกิดใน**ไม่กี่นาทีแรก** + ไข้หนาวสั่น + **ปวดสีข้าง** + BP ต่ำ + **hemoglobinuria** = **AHTR** (ABO incompatibility) → หยุดให้เลือด + IV fluid
- Anaphylaxis เด่นผื่น wheeze ไม่มีไข้และปวดสีข้าง
- Transfusion-associated sepsis มีไข้และ shock ได้ แต่ไม่มีปวดสีข้าง/hemoglobinuria (ยืนยันด้วย H/C)
- FNHTR มีไข้แต่ไม่มี hemolysis และ V/S ไม่ทรุด
- TRALI เด่นหายใจลำบาก/hypoxia และ CXR infiltrate''',
            pearl="ไข้ + ปวดสีข้าง + ปัสสาวะแดง ช่วงแรกของการให้เลือด = AHTR", topic="AHTR",
            ref=[f"{D} หน้า 350, 356–357"], nl=["2.2.21"]),
        mcq("HEMATO-09-03-2",
            "A 60-year-old woman received 5 units of PRC after surgery. One week later she has anemia and mild jaundice without hepatosplenomegaly. Hb 8 g/dL, Hct 24%, WBC 8,000/µL, platelet 230,000/µL, reticulocyte 14%. Direct Coombs test 1+, indirect Coombs test 3+. What is the most likely diagnosis?",
            "Delayed hemolytic transfusion reaction",
            ["Acute hemolytic transfusion reaction", "Bacterial contamination", "Febrile non-hemolytic transfusion reaction", "Anaphylaxis"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Hemolysis (ซีด เหลือง retic สูง) **1 สัปดาห์หลังให้เลือด** + **DAT บวก** (antibody เกาะ RBC ที่ได้รับ) + **IAT บวก** (มี alloantibody ใน serum) = **DHTR** จาก minor blood group incompatibility → supportive
- AHTR เกิดภายในนาที–ชั่วโมงระหว่างให้เลือด
- Bacterial contamination ทำให้ไข้/shock ระหว่างให้เลือด
- FNHTR เป็นไข้ระหว่างให้เลือด ไม่มี hemolysis
- Anaphylaxis เกิดทันที ไม่มี hemolysis''',
            pearl="Hemolysis วัน–สัปดาห์หลังให้เลือด + DAT/IAT บวก = DHTR", topic="DHTR",
            ref=[f"{D} หน้า 348, 362–363"], nl=["2.2.21", "B2.2.2(4)"]),
        mcq("HEMATO-09-03-3",
            "A woman with hemolytic anemia receives 2 units of PRC over 2 hours. During the transfusion she becomes dyspneic. BP 160/95 mmHg, PR 96/min, RR 24/min, BT 37°C. PE: JVP 6 cm above the sternal angle, coarse crepitations with wheeze at both lungs, liver 2 cm below the costal margin. After stopping the transfusion, what is the most appropriate management?",
            "Furosemide",
            ["Adrenaline", "Dexamethasone", "Chlorpheniramine", "Salbutamol nebulizer"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (ปรับ BP ให้เห็นความดันสูงแบบ TACO)",
            explain='''หอบระหว่างให้เลือดเร็ว + **JVP สูง + BP สูง** + crepitation (pulmonary edema) + ตับโต = **TACO** → หยุดให้เลือด + O2 + **diuretic (furosemide)**
- Adrenaline ใช้กับ anaphylaxis (BP ต่ำ ผื่น)
- Dexamethasone และ chlorpheniramine ใช้ในปฏิกิริยาแพ้
- Salbutamol แก้ bronchospasm แต่ wheeze ที่นี่เป็น cardiac asthma จากน้ำเกิน''',
            pearl="TACO (JVP ↑ BP ↑) → furosemide", topic="TACO",
            ref=[f"{D} หน้า 352, 366–367"], nl=["2.2.21", "2.2.5"]),
        mcq("HEMATO-09-03-4",
            "A 44-year-old man with upper GI bleeding received 1 unit of RBC and 3 units of FFP. During the last unit of FFP he develops dyspnea and hypoxemia with fever. BP 88/56 mmHg. PE: fine crepitations both lungs, no neck vein engorgement; urine output 100 mL/hr. CXR: bilateral infiltrates, no cardiomegaly. After stopping the transfusion, what is the most appropriate management?",
            "Oxygen and aggressive ventilatory support",
            ["Intravenous furosemide", "Intravenous antihistamine", "Intravenous dexamethasone", "Intramuscular epinephrine"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่ม BP ต่ำและไข้)",
            explain='''หอบ + hypoxia ระหว่างให้ **FFP** + **JVP ปกติ** + BP ต่ำ + ไข้ + CXR infiltrate ไม่มีหัวใจโต = **TRALI** (non-cardiogenic pulmonary edema) → **O2 และ ventilation support**
- Furosemide เป็นการรักษา TACO — ใน TRALI ผู้ป่วยไม่ได้น้ำเกินและ BP ต่ำ อาจแย่ลง
- Antihistamine, dexamethasone, epinephrine ใช้กับปฏิกิริยาแพ้/anaphylaxis ซึ่งเด่นผื่น wheeze ไม่ใช่ infiltrate ทั้งสองข้าง''',
            pearl="TRALI (JVP ปกติ BP ↓) → ventilation, ห้าม diuretic", topic="TRALI",
            ref=[f"{D} หน้า 352, 368–369"], nl=["2.2.21", "2.2.9"]),
        mcq("HEMATO-09-03-5",
            "A patient with a femoral fracture receives 10 units of PRC, 6 units of FFP, and 5 units of platelets rapidly. He develops perioral numbness, then hypotension; ECG shows QT prolongation followed by bradycardia and cardiac arrest. Which mechanism is most likely responsible?",
            "Hypocalcemia from citrate in the transfused products",
            ["ABO-incompatible transfusion", "Fat embolism", "Hypothermia alone", "Metabolic acidosis from lactate in stored blood"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (ปรับ ECG ให้ชี้ hypocalcemia — สไลด์เดิมบรรยาย ECG แบบ hyperkalemia ซึ่งก็เป็นภาวะแทรกซ้อนของ massive transfusion)",
            explain='''Massive transfusion → **citrate** (สารกันเลือดแข็งในถุง) จับ Ca → **hypocalcemia**: ชารอบปาก **QT ยาว** BP ต่ำ หัวใจหยุดเต้น · ป้องกันด้วยการให้ calcium ระหว่าง massive transfusion
- ABO incompatibility จะมีไข้ ปวดสีข้าง hemoglobinuria
- Fat embolism เกิดหลังกระดูกยาวหัก 24–72 ชม. มีสับสน หอบ petechiae
- Hypothermia ทำให้หัวใจเต้นช้าและ coagulopathy แต่ QT ยาว + ชารอบปากชี้ไปที่ Ca ต่ำ
- Citrate ถูกเปลี่ยนเป็น bicarbonate → **metabolic alkalosis** ไม่ใช่ acidosis
(หมายเหตุ: ถ้า ECG เป็น peaked T, QRS กว้าง P หาย → hyperkalemia ซึ่งก็เป็นภาวะแทรกซ้อนของ massive transfusion เช่นกัน)''',
            pearl="Massive transfusion: citrate → Ca ต่ำ (QT ยาว) · RBC เก่า → K สูง", topic="Massive transfusion",
            ref=[f"{D} หน้า 355, 370–371"], nl=["2.2.21", "2.2.15"]),
        mcq("HEMATO-09-03-6",
            "A 50-year-old man with massive bleeding develops slight hematuria shortly after starting a blood transfusion. BP 130/80 mmHg, RR 16/min, BT 37°C, PR 90/min. PE is unremarkable. What is the most appropriate first step?",
            "Stop the blood transfusion",
            ["Sodium bicarbonate infusion", "NSS loading", "Furosemide", "Dexamethasone"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Hematuria/hemoglobinuria หลังเริ่มให้เลือด = สงสัย **AHTR** → ขั้นแรก**หยุดให้เลือดทันที** (จากนั้น IV fluid, ตรวจถุงเลือดและผู้ป่วย, ติดตาม V/S และ urine output)
- Sodium bicarbonate (urine alkalinization) ไม่ใช่ขั้นแรกและไม่แนะนำเป็นมาตรฐาน
- NSS เป็นขั้นต่อไปหลังหยุดเลือด
- Furosemide ใช้เมื่อ volume เพียงพอแล้วและปัสสาวะน้อย
- Dexamethasone ไม่มีบทบาทใน AHTR''',
            pearl="สงสัย transfusion reaction → หยุดให้เลือดก่อนเสมอ", topic="Transfusion reaction first step",
            ref=[f"{D} หน้า 350, 360–361"], nl=["2.2.21"]),
    ])

LECTURE = lecture("09", "Febrile neutropenia & transfusion medicine",
    "FN · blood products · transfusion reactions · massive transfusion",
    objectives=[
        "นิยาม febrile neutropenia และเริ่ม empirical anti-pseudomonal ได้",
        "เลือก PRC, platelet, FFP, cryoprecipitate, PCC ตามข้อบ่งชี้และเกณฑ์ตัวเลข",
        "แยก AHTR, DHTR, FNHTR, bacterial, allergic, TACO และ TRALI และจัดการได้",
        "จำภาวะแทรกซ้อนของ massive transfusion (↓Ca, ↑K, alkalosis, hypothermia)",
    ],
    sections=[S1, S2, S3])
