from lib import lecture, sec, mcq, fig

D = "สไลด์ Update ข้อสอบ 2025"
SRC = "NL2 2025 (update)"

def R(*p):
    return [f"{D} หน้า " + ", ".join(str(x) for x in p)]

# ---------------------------------------------------------------- 06-01 Hemolysis
F_HEM = fig("exam25-06-01-f1", "แยก hemolytic anemia จาก DAT และ PBS", '''<svg viewBox="0 0 720 300">
 <defs><marker id="exam25-06-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="210" y="10" width="300" height="44" rx="10" class="acsoft"/>
 <text x="360" y="30" text-anchor="middle" class="tb">Anemia + jaundice + retic สูง</text>
 <text x="360" y="47" text-anchor="middle" class="t3">± ปัสสาวะสีเข้ม (hemoglobinuria)</text>
 <path d="M360 54V74" class="ln" marker-end="url(#exam25-06-01-a)"/>
 <rect x="260" y="76" width="200" height="36" rx="10" class="box"/>
 <text x="360" y="99" text-anchor="middle" class="tb">DAT (Coombs test)</text>
 <path d="M300 112L150 140" class="ln" marker-end="url(#exam25-06-01-a)"/>
 <path d="M420 112L540 140" class="ln" marker-end="url(#exam25-06-01-a)"/>
 <rect x="20" y="142" width="250" height="148" rx="10" class="c1soft"/>
 <text x="145" y="166" text-anchor="middle" class="tb">DAT บวก = AIHA</text>
 <text x="145" y="190" text-anchor="middle" class="t2">PBS: spherocytes</text>
 <text x="145" y="210" text-anchor="middle" class="t2">± agglutination</text>
 <text x="145" y="240" text-anchor="middle" class="ta">Tx: prednisolone</text>
 <text x="145" y="262" text-anchor="middle" class="t3">+ หาสาเหตุ (SLE, CLL, ยา)</text>
 <rect x="300" y="142" width="400" height="148" rx="10" class="c2soft"/>
 <text x="500" y="166" text-anchor="middle" class="tb">DAT ลบ → ดู PBS และประวัติ</text>
 <text x="316" y="192" class="tb">Blister/bite cell</text>
 <text x="470" y="192" class="t2">→ G6PD (หลังติดเชื้อ/ยา)</text>
 <text x="316" y="216" class="tb">Schistocytes</text>
 <text x="470" y="216" class="t2">→ MAHA (TTP, HUS, DIC)</text>
 <text x="316" y="240" class="tb">Spherocyte + FHx</text>
 <text x="470" y="240" class="t2">→ HS (osmotic fragility)</text>
 <text x="316" y="264" class="tb">ไม่มีอะไร + Plt ต่ำ</text>
 <text x="470" y="264" class="t2">→ PNH (flow CD55/CD59)</text>
</svg>''', "DAT แบ่งทางแรก แล้วใช้รูปร่างเม็ดเลือดแดงบน PBS ร่วมกับประวัติแยกสาเหตุที่ DAT ลบ")

S1 = sec("exam25-06-01", "Hemolytic anemia",
    "Blister cell = G6PD · spherocyte + DAT = AIHA · Coombs ลบ + Plt ต่ำ + ปัสสาวะเข้ม = PNH", minutes=5,
    source=f"{D} หน้า 144–149", nl=["2.3.3(3)", "2.3.3(4)", "2.3.3-3(6)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

[[fig:exam25-06-01-f1]]

| โรค | จุดจำ (สไลด์) | ตรวจยืนยัน | รักษา |
|---|---|---|---|
| **G6PD deficiency** | trigger: ติดเชื้อ ถั่วปากอ้า ยา antimalarial sulfa · hemolysis เป็นพัก (ปวดหลัง/ท้อง ดีซ่าน ปัสสาวะเข้ม) · **blister cell, ghost cell** | G6PD level (หลังหาย hemolysis) | supportive, IV fluid, เลี่ยง trigger |
| **AIHA** | ซีด เหลือง · **spherocytes ± agglutination** | **DAT (Coombs)** | หาสาเหตุ + **prednisolone** |
| **PNH** | ปัสสาวะเข้ม **ตอนเช้า** · **Plt ต่ำ/pancytopenia** · polychromasia retic สูง · Coombs ลบ | **flow cytometry: CD55, CD59 ลดลง** | eculizumab (เสริม) |

> Spherocytes พบได้ทั้ง AIHA และ hereditary spherocytosis — ไม่มีประวัติครอบครัว เป็นผู้ใหญ่ เกิดเร็ว → ทำ DAT ก่อน
''',
    figs=[F_HEM],
    pearls=[
        "Blister/bite cell = G6PD (oxidative hemolysis)",
        "Spherocytes ในผู้ใหญ่ → DAT หา AIHA",
        "Hemolysis + Coombs ลบ + Plt ต่ำ + ปัสสาวะเข้มตอนเช้า = PNH → CD55/CD59",
    ],
    items=[
        mcq("EXAM25-06-01-1",
            "A 19-year-old man presents with 3 days of fever, fatigue and dark urine. He takes no medications. He is pale and jaundiced, without organomegaly. The peripheral blood smear shows blister cells. What is the most likely diagnosis?",
            "G6PD deficiency",
            ["Malaria", "Hb H disease", "Paroxysmal nocturnal hemoglobinuria", "Immune thrombocytopenia"],
            kind="old", src=SRC,
            explain='''ชายวัยรุ่น + **ติดเชื้อ (ไข้) เป็น trigger** → acute intravascular hemolysis (ซีด เหลือง ปัสสาวะเข้ม) + **blister cell** (Heinz body ถูกม้ามดึงออก) = **G6PD deficiency** (X-linked)
- Malaria ทำให้ไข้และ hemolysis ได้ แต่ PBS จะเห็นเชื้อในเม็ดเลือดแดง ไม่ใช่ blister cell
- Hb H disease เป็น microcytic เรื้อรังมีม้ามโต target cell และ Hb H inclusion
- PNH มีปัสสาวะเข้มตอนเช้า + Plt ต่ำ PBS ไม่มี blister cell
- ITP ทำให้เกล็ดเลือดต่ำ เลือดออก ไม่ทำให้ hemolysis''',
            pearl="ติดเชื้อ/ยา + hemolysis + blister cell = G6PD", topic="G6PD deficiency",
            ref=R(144, 145), nl=["2.3.3(3)", "2.2.18"]),
        mcq("EXAM25-06-01-2",
            "A 30-year-old woman presents with fatigue for 2 weeks. She has pale conjunctivae and mildly icteric sclerae. Hb 8 g/dL, WBC 5,000/mm³, platelets 200,000/mm³. The peripheral blood smear shows numerous spherocytes. She has no family history of anemia. Which investigation establishes the diagnosis?",
            "Direct antiglobulin test",
            ["Osmotic fragility test", "Hemoglobin typing", "Antinuclear antibody", "Serum protein electrophoresis"],
            kind="old", src=SRC,
            explain='''ผู้ใหญ่ที่ซีดเหลืองเกิดขึ้นใหม่ + **spherocytes** + ไม่มีประวัติครอบครัว = **autoimmune hemolytic anemia** (warm) → ยืนยันด้วย **DAT (Coombs test)** แล้วรักษาด้วย prednisolone + หาสาเหตุ
- Osmotic fragility ใช้กับ hereditary spherocytosis (เด็ก ม้ามโต ประวัติครอบครัว) และให้ผลบวกใน AIHA ด้วย จึงแยกไม่ได้
- Hb typing ใช้กับ thalassemia (microcytic, target cell)
- ANA ใช้หา SLE เป็นสาเหตุของ AIHA หลังยืนยัน AIHA แล้ว
- SPEP ใช้หา monoclonal protein (myeloma)''',
            pearl="Spherocytes ในผู้ใหญ่ → DAT", topic="AIHA",
            ref=R(146, 147), nl=["2.3.3(4)"]),
        mcq("EXAM25-06-01-3",
            "A 35-year-old woman presents with 2 weeks of fatigue and intermittent dark urine, most noticeable in the morning. She has moderate pallor and mild scleral icterus without hepatosplenomegaly. Hb 7 g/dL, platelets 80,000/μL, WBC 5,000/mm³, MCV 98 fL, reticulocytes 3%. Coombs test is negative and the smear shows no schistocytes. What is the most likely diagnosis?",
            "Paroxysmal nocturnal hemoglobinuria",
            ["Autoimmune hemolytic anemia", "G6PD deficiency", "Microangiopathic hemolytic anemia", "Hereditary spherocytosis"],
            kind="old", src=SRC,
            explain='''Hemolysis (ซีด เหลือง retic สูง) + **ปัสสาวะเข้มเป็นพัก ๆ ตอนเช้า** (intravascular hemolysis) + **Coombs ลบ** + **เกล็ดเลือดต่ำ** = **PNH** (ขาด GPI-anchored protein CD55/CD59 → complement ทำลายเซลล์) → ยืนยันด้วย flow cytometry
- AIHA ถูกตัดด้วย Coombs ลบ
- G6PD เกิดหลัง trigger PBS มี blister cell และเกล็ดเลือดไม่ต่ำ
- MAHA ต้องเห็น schistocytes ซึ่งโจทย์บอกว่าไม่มี
- HS มีประวัติครอบครัว ม้ามโต และ spherocytes''',
            pearl="Coombs ลบ + Plt ต่ำ + ปัสสาวะเข้มตอนเช้า = PNH", topic="PNH",
            ref=R(148, 149), nl=["2.3.3-3(6)"]),
    ])

# ---------------------------------------------------------------- 06-02 Megaloblastic & MM
S2 = sec("exam25-06-02", "Megaloblastic anemia & multiple myeloma",
    "หลังตัดกระเพาะ + MCV > 100 → B12 level · pancytopenia + hypersegmented → B12 + folate · CRAB + M spike = myeloma", minutes=5,
    source=f"{D} หน้า 150–154, 161–162", nl=["2.3.3(7)", "B2.2.4-3(4)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Megaloblastic anemia**
- ลักษณะ: ซีด **± ดีซ่านเล็กน้อย** (ineffective erythropoiesis) · **MCV สูง (> 100)** · **± pancytopenia** · PBS: **macro-ovalocyte, hypersegmented neutrophil**
- B12 ต้องจับกับ **intrinsic factor** (สร้างจาก parietal cell ของกระเพาะ) แล้วดูดซึมที่ **terminal ileum**
- สาเหตุขาด B12: **หลังตัดกระเพาะ**, pernicious anemia, ตัด/โรค terminal ileum, มังสวิรัติเคร่ง, metformin · ขาด folate: ดื่มสุรา, ตั้งครรภ์, กินน้อย, methotrexate/phenytoin
- ตรวจแรก: **serum B12 ± folate** · ไม่ต้องเจาะไขกระดูกถ้าภาพชัด
- B12 ต่ำ → อาการทางระบบประสาท (posterior column) ได้ · **ห้ามให้ folate อย่างเดียว** ถ้ายังไม่ได้ตัดภาวะขาด B12 (เสริม)

**Multiple myeloma — CRAB**
- **C**alcium สูง · **R**enal failure · **A**nemia (normocytic, rouleaux) · **B**one pain/lytic lesion + ติดเชื้อซ้ำ
- **SPEP: M spike** · ยืนยันด้วย bone marrow plasma cell ≥ 10% (เสริม)
''',
    pearls=[
        "หลังตัดกระเพาะ (ไม่มี IF) + MCV สูง → ขาด B12",
        "Hypersegmented neutrophil + MCV สูง → ตรวจ B12 และ folate",
        "CRAB + M spike = multiple myeloma",
    ],
    items=[
        mcq("EXAM25-06-02-1",
            "A 70-year-old woman who underwent partial gastrectomy for gastric cancer 5 years ago presents with progressive fatigue. She has pallor and mild scleral icterus. Hb 9 g/dL, MCV 115 fL, WBC 3,500/μL, platelets 100,000/μL. What is the most useful initial investigation?",
            "Serum vitamin B12 level",
            ["Serum folate level", "Serum ferritin", "Liver function tests", "Reticulocyte count"],
            kind="old", src=SRC,
            explain='''หลังตัดกระเพาะ → ขาด **intrinsic factor** → ดูดซึม B12 ไม่ได้ (ร่างกายมี B12 สำรองหลายปี จึงเกิดหลัง 3–5 ปี) · MCV 115 + pancytopenia + ดีซ่านเล็กน้อย = megaloblastic anemia → ตรวจ **serum B12** เป็นอันดับแรก
- Folate ขาดได้แต่ไม่สัมพันธ์กับการตัดกระเพาะเท่า B12
- Ferritin ใช้ประเมิน iron deficiency ซึ่งให้ MCV ต่ำ (แม้ตัดกระเพาะก็ขาดเหล็กได้ แต่ MCV 115 ไม่เข้า)
- LFT ช่วยอธิบายดีซ่าน แต่ดีซ่านรายนี้มาจาก ineffective erythropoiesis
- Reticulocyte count ไม่ได้บอกสาเหตุ''',
            pearl="หลังตัดกระเพาะ + macrocytic → B12", topic="B12 deficiency",
            ref=R(150, 151, 152), nl=["2.3.3(7)"]),
        mcq("EXAM25-06-02-2",
            "A 45-year-old woman has 2 months of fatigue and pallor. CBC shows pancytopenia with an MCV of 112 fL. The peripheral blood smear shows hypersegmented neutrophils. What is the most useful initial investigation?",
            "Serum vitamin B12 and folate levels",
            ["Bone marrow biopsy", "Reticulocyte count", "Coombs test", "Serum ferritin"],
            kind="old", src=SRC,
            explain='''Pancytopenia + **hypersegmented neutrophils** (+ MCV สูง) = megaloblastic anemia → ตรวจ **serum B12 และ folate** ก่อน (สไลด์ highlight ทั้งสองตัว จึงรวมเป็นตัวเลือกเดียว และเติม MCV 112 ในโจทย์ให้ภาพชัดขึ้น)
- Bone marrow biopsy ใช้เมื่อระดับวิตามินปกติหรือสงสัย MDS/marrow infiltration ไม่ใช่การตรวจแรก
- Reticulocyte count ช่วยแยก production กับ destruction แต่ไม่บอกสาเหตุ
- Coombs test ใช้หา AIHA ซึ่งไม่ทำให้ hypersegmented neutrophil
- Ferritin ใช้ใน microcytic anemia''',
            pearl="Hypersegmented neutrophil → ตรวจ B12 + folate", topic="Megaloblastic anemia",
            ref=R(153, 154), nl=["2.3.3(7)"]),
        mcq("EXAM25-06-02-3",
            "A 65-year-old man presents with bone pain, fatigue and recurrent infections. Laboratory studies show normocytic anemia, hypercalcemia and elevated creatinine. Serum protein electrophoresis reveals an M spike. What is the most likely diagnosis?",
            "Multiple myeloma",
            ["Waldenström macroglobulinemia", "Lymphoma", "Chronic lymphocytic leukemia", "Osteosarcoma"],
            kind="old", src=SRC,
            explain='''**CRAB** (hyperCalcemia, Renal failure, Anemia, Bone pain) + ติดเชื้อซ้ำ (immunoparesis) + **M spike** = **multiple myeloma**
- Waldenström มี IgM M spike แต่เด่นที่ hyperviscosity, lymphadenopathy, hepatosplenomegaly และไม่มี lytic bone lesion
- Lymphoma มาด้วยต่อมน้ำเหลืองโต B symptoms
- CLL มี lymphocytosis สูง smudge cell
- Osteosarcoma เป็นเนื้องอกกระดูกในวัยรุ่น ไม่ทำให้ M spike''',
            pearl="CRAB + M spike = myeloma", topic="Multiple myeloma",
            ref=R(161, 162), nl=["B2.2.4-3(4)"]),
    ])

# ---------------------------------------------------------------- 06-03 Thal & transfusion
S3 = sec("exam25-06-03", "Thalassemia & transfusion reactions",
    "Microcytic + target cell → Hb typing · ปฏิกิริยาระหว่างให้เลือดทุกชนิด → หยุดให้เลือดก่อน", minutes=5,
    source=f"{D} หน้า 155–160", nl=["2.3.3(8)", "2.2.21"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Thalassemia**: microcytic hypochromic anemia, anisopoikilocytosis, **target cell** → **Hb typing (Hb electrophoresis)** (แยก β-thal/Hb E/Hb H) · ferritin ใช้แยก IDA แต่ target cell 3+ ชี้ไป thalassemia

**Transfusion reactions — ขั้นแรกเหมือนกันทุกชนิด: หยุดให้เลือด**

| ปฏิกิริยา | อาการ | ทำต่อ |
|---|---|---|
| **AHTR** (ABO ไม่เข้ากัน) | ไข้ หนาวสั่น **BP ต่ำ** ปวดหลัง hemoglobinuria | **หยุด** + resuscitation + ส่งถุงเลือด/เลือดผู้ป่วยตรวจ |
| **Bacterial contamination** | ไข้สูง **BP ต่ำ** | **หยุด** + resuscitation + **ATB** + เพาะเชื้อถุงเลือด |
| FNHTR | ไข้/หนาวสั่นอย่างเดียว BP ปกติ | หยุด ให้ paracetamol (เสริม) |
| **Allergic (ATR)** | **คัน ลมพิษ** (± คลื่นไส้) ไม่มีไข้ BP ปกติ | **หยุด** → ตัด anaphylaxis → **antihistamine** → **ให้ต่อได้เมื่อดีขึ้น** |
| Anaphylaxis | BP ต่ำ หลอดลมตีบ | หยุด + **IM adrenaline** |
| TACO / TRALI | หอบ น้ำท่วมปอด | หยุด + furosemide (TACO) / supportive (TRALI) (เสริม) |

> ไข้ + BP ต่ำระหว่างให้เลือด = AHTR หรือ bacterial contamination จนกว่าจะพิสูจน์ได้ว่าไม่ใช่
''',
    pearls=[
        "Microcytic + target cell → Hb typing",
        "ปฏิกิริยาจากการให้เลือดทุกชนิด: ขั้นแรก = หยุดให้เลือด",
        "ไข้ + BP ต่ำ → AHTR/bacterial contamination: resuscitate + ATB",
        "Allergic reaction เล็กน้อย → antihistamine แล้วให้เลือดต่อได้",
    ],
    items=[
        mcq("EXAM25-06-03-1",
            "A 17-year-old girl with no family history of hematologic disorders presents with fatigue. Physical examination is normal. Hb 8.0 g/dL, MCV 70 fL. The peripheral smear shows 3+ target cells. What is the next investigation?",
            "Hemoglobin electrophoresis (Hb typing)",
            ["Serum ferritin", "DNA testing for α-thalassemia", "Abdominal ultrasound", "Chest X-ray"],
            kind="old", src=SRC,
            explain='''Microcytic anemia + **target cell 3+** = นึกถึง **thalassemia/hemoglobinopathy** → ตรวจ **Hb typing** หาชนิด Hb ผิดปกติ (Hb E, Hb H, β-thal)
- Serum ferritin ใช้แยก IDA ซึ่งไม่ทำให้ target cell มากขนาดนี้ (สไลด์เลือก Hb typing)
- DNA testing สำหรับ α-thal ใช้หลัง Hb typing เมื่อสงสัย α-thal trait ที่ Hb typing ปกติ
- U/S ช่องท้องดูม้ามโตได้ แต่ไม่ได้วินิจฉัยชนิดของโรค
- CXR ไม่เกี่ยว''',
            pearl="Microcytic + target cell → Hb typing", topic="Thalassemia",
            ref=R(155, 156), nl=["2.3.3(8)"]),
        mcq("EXAM25-06-03-2",
            "A 35-year-old woman with β-thalassemia/Hb E disease develops fever, chills and flushing during a routine blood transfusion. Temperature 38 °C, BP 80/60 mmHg, pulse 120/min. There is no wheezing, dyspnea or rash. What is the most appropriate initial management?",
            "Stop the transfusion",
            ["Normal saline intravenous bolus", "Oral paracetamol", "Intravenous hydrocortisone", "Intravenous chlorpheniramine"],
            kind="old", src=SRC,
            explain='''ไข้ + **BP ต่ำ** ระหว่างให้เลือด = **acute hemolytic transfusion reaction หรือ bacterial contamination** → สิ่งแรกคือ **หยุดให้เลือดทันที** แล้วจึง resuscitate (NSS) ให้ ATB และส่งถุงเลือด/เลือดผู้ป่วยตรวจ
- NSS bolus ต้องให้ แต่เป็นขั้นหลังหยุดเลือด ถ้ายังปล่อยเลือดไหลต่อ ปฏิกิริยาจะรุนแรงขึ้น
- Paracetamol รักษาแค่ไข้ (FNHTR) ไม่เหมาะเมื่อมี BP ต่ำ
- Hydrocortisone และ chlorpheniramine ใช้กับ allergic reaction ซึ่งไม่มีผื่น หลอดลมตีบ''',
            pearl="ไข้ + BP ต่ำระหว่างให้เลือด → หยุดให้เลือดก่อน", topic="AHTR",
            ref=R(157, 158), nl=["2.2.21"]),
        mcq("EXAM25-06-03-3",
            "A 25-year-old woman with β/βE thalassemia develops pruritus, nausea and vomiting immediately after starting leukocyte-depleted packed red cells. There is no fever, hemoglobinuria, wheezing or hypotension. What is the most appropriate initial management?",
            "Stop the transfusion",
            ["Intravenous chlorpheniramine", "Intravenous hydrocortisone", "Normal saline intravenous bolus", "Intravenous furosemide"],
            kind="old", src=SRC,
            explain='''คัน + คลื่นไส้ทันทีหลังเริ่มให้เลือด ไม่มีไข้ BP ปกติ = **allergic transfusion reaction** → ตามสไลด์ **หยุดให้เลือดก่อน** แล้วตัด anaphylaxis ให้ antihistamine และให้เลือดต่อได้เมื่ออาการดีขึ้น
- Chlorpheniramine เป็นขั้นถัดไปหลังหยุดเลือด (กับดักของข้อนี้ — ข้อสอบตอบหยุดให้เลือด)
- Hydrocortisone ไม่จำเป็นในปฏิกิริยาเล็กน้อย
- NSS bolus ใช้เมื่อ BP ต่ำ
- Furosemide ใช้ใน TACO (หอบ น้ำเกิน)''',
            pearl="ปฏิกิริยาระหว่างให้เลือดทุกชนิด → หยุดให้เลือดก่อน", topic="Allergic transfusion reaction",
            ref=R(159, 160), nl=["2.2.21"]),
    ])

LECTURE = lecture("06", "Hemato", "hemolysis · megaloblastic · myeloma · thalassemia · transfusion",
    objectives=[
        "แยก G6PD, AIHA และ PNH จาก PBS และ Coombs",
        "เลือกการตรวจแรกใน macrocytic anemia และจำ CRAB",
        "จัดการ transfusion reaction โดยเริ่มจากหยุดให้เลือด",
    ],
    sections=[S1, S2, S3])
