from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Hemato"

# ---------------------------------------------------------------- 03-01 Genetics & clinical
F_GENO = fig("hemato-03-01-f1", "แผนที่ genotype ธาลัสซีเมีย: α-chain vs β-chain", '''<svg viewBox="0 0 740 420">
 <rect x="20" y="12" width="340" height="40" rx="10" class="c1"/>
 <text x="190" y="38" text-anchor="middle" class="tw">α-globin (4 ยีน: αα/αα)</text>
 <rect x="380" y="12" width="340" height="40" rx="10" class="c2"/>
 <text x="550" y="38" text-anchor="middle" class="tw">β-globin (2 ยีน: β/β)</text>
 <text x="190" y="72" text-anchor="middle" class="t3">ยีนหายมาก → รุนแรงมาก</text>
 <text x="550" y="72" text-anchor="middle" class="t3">βo = ไม่สร้าง · βE = สร้างได้น้อย</text>
 <rect x="20" y="82" width="340" height="56" rx="10" class="oksoft"/>
 <text x="36" y="104" class="tb">-α/αα  α-thal 2 trait</text>
 <text x="36" y="126" class="t3">ปกติ/MCV ≥ 80 · เกือบไม่มีอาการ</text>
 <rect x="20" y="146" width="340" height="56" rx="10" class="oksoft"/>
 <text x="36" y="168" class="tb">--/αα  α-thal 1 trait</text>
 <text x="36" y="190" class="t3">ไม่ซีด/ซีดน้อย · MCV &lt; 75–80</text>
 <rect x="20" y="210" width="340" height="66" rx="10" class="misssoft"/>
 <text x="36" y="232" class="tb">--/-α  HbH disease</text>
 <text x="36" y="252" class="t3">ซีดปานกลาง ม้ามโต · HbH inclusion</text>
 <text x="36" y="268" class="t3">แตกเฉียบพลันเมื่อไข้/ยา (hemolytic crisis)</text>
 <rect x="20" y="284" width="340" height="66" rx="10" class="badsoft"/>
 <text x="36" y="306" class="tb">--/--  Hb Bart's hydrops fetalis</text>
 <text x="36" y="326" class="t3">ตายในครรภ์/หลังคลอดไม่นาน</text>
 <text x="36" y="342" class="t3">แม่เสี่ยง pre-eclampsia (เสริม)</text>
 <rect x="380" y="82" width="340" height="56" rx="10" class="oksoft"/>
 <text x="396" y="104" class="tb">βo/β  β-thal trait · βE/β HbE trait</text>
 <text x="396" y="126" class="t3">ไม่มีอาการ · MCV ต่ำ</text>
 <rect x="380" y="146" width="340" height="56" rx="10" class="oksoft"/>
 <text x="396" y="168" class="tb">βE/βE  Homozygous HbE</text>
 <text x="396" y="190" class="t3">ไม่ซีด/ซีดน้อย · MCV ต่ำ target cell มาก</text>
 <rect x="380" y="210" width="340" height="66" rx="10" class="misssoft"/>
 <text x="396" y="232" class="tb">βo/βE  β-thal/HbE disease</text>
 <text x="396" y="252" class="t3">พบบ่อยสุดในไทย · ซีดปานกลาง–มาก</text>
 <text x="396" y="268" class="t3">ม้ามโต · หลายรายต้องรับเลือด</text>
 <rect x="380" y="284" width="340" height="66" rx="10" class="badsoft"/>
 <text x="396" y="306" class="tb">βo/βo  Homozygous β-thal (major)</text>
 <text x="396" y="326" class="t3">ซีดมากตั้งแต่ขวบปีแรก</text>
 <text x="396" y="342" class="t3">ต้องรับเลือดประจำ</text>
 <rect x="20" y="364" width="700" height="46" rx="10" class="sunk"/>
 <text x="370" y="384" text-anchor="middle" class="tb">โรครุนแรงที่ต้องคัดกรองคู่สมรส (severe thalassemia)</text>
 <text x="370" y="402" text-anchor="middle" class="t2">Hb Bart's hydrops (--/--) · Homozygous β-thal (βo/βo) · β-thal/HbE (βo/βE)</text>
</svg>''', "ยิ่งสูญเสียยีนมาก (ลงล่าง) ยิ่งรุนแรง · แถวสีแดงล่างสุดคือ severe thalassemia ที่เป็นเป้าของการคัดกรองก่อนคลอด")

S1 = sec("hemato-03-01", "Thalassemia: genotypes & clinical features",
    "α vs β globin defect · trait → HbH/β-thal/HbE → major/Bart's · microcytic + target cell + HbH inclusion · ineffective erythropoiesis + hemolysis", minutes=7,
    source=f"{D} หน้า 97–98, 103, 108", nl=["2.3.3(8)", "B2.2.1(1)"],
    md='''
### กลไก

- Mutation/deletion ของยีน → สร้าง **α หรือ β globin ไม่พอ** → globin chain ไม่สมดุล
- chain ที่เกินตกตะกอนในเซลล์ → **ineffective erythropoiesis** (ตายในไขกระดูก) + **hemolysis** (ม้ามทำลาย) → ไขกระดูกขยาย, extramedullary hematopoiesis, ดูดเหล็กเพิ่ม (เสริม)

### ชนิดของ hemoglobin

| Hb | สายโกลบิน | หมายเหตุ |
|---|---|---|
| Hb A | α2β2 | ผู้ใหญ่ปกติ (หลัก) |
| Hb A2 | α2δ2 | ปกติ < 3.5% · สูงใน β-thal trait |
| Hb F | α2γ2 | ทารกในครรภ์ · สูงใน β-thal major |
| **Hb Bart's** | **γ4** | ขาด α ในทารก |
| **Hb H** | **β4** | ขาด α ในผู้ใหญ่ |
| Hb E | α2βE | βE สร้างได้น้อย (มีลักษณะ β-thal อ่อน ๆ) |

### Genotype

- **α-thalassemia**: α-thal 2 trait (-α/αα), α-thal 1 trait (--/αα), **HbH disease (--/-α)**, **Hb Bart's hydrops fetalis (--/--)**
- **β-thalassemia**: β-thal trait (βo/β), HbE trait (βE/β), homozygous HbE (βE/βE), **β-thal/HbE (βo/βE)**, **homozygous β-thal (βo/βo)**

[[fig:hemato-03-01-f1]]

### อาการ

- ตั้งแต่ไม่มีอาการ (trait) ถึง **severe hemolytic anemia**
- ซีด เหลือง **ตับม้ามโต**, **ตัวเตี้ยโตช้า**, **กระดูกผิดรูป** (thalassemic facies: โหนกแก้มสูง หน้าผากโหนก — เสริม)
- Hb Bart's → ตายในครรภ์หรือหลังคลอดไม่นาน
- HbH/β-thal/HbE ซีดลงเฉียบพลันเมื่อมีไข้หรือได้ยา (**acute hemolytic crisis**)

### การตรวจ

- CBC: **↓MCV, ↑RDW** (trait: MCV ต่ำมากเทียบกับ Hb ที่ค่อนข้างดี)
- PBS: **hypochromic microcytic**, **target cell**, anisocytosis, poikilocytosis, NRC, basophilic stippling · **HbH inclusion body** (supravital, ใน HbH)
- **Hb typing** (ดูหัวข้อถัดไป) · DNA analysis สำหรับ α-thal 1 trait

> ซีด microcytic + **ไข้แล้วซีดลงเร็ว** + ตับม้ามโต + ประวัติเหลืองเรื้อรัง = **HbH disease หรือ β-thal/HbE with acute hemolysis** — ต่างจาก G6PD ที่ MCV ปกติและไม่มีม้ามโต
''',
    figs=[F_GENO],
    pearls=[
        "HbH = β4 (--/-α) · Hb Bart's = γ4 (--/--)",
        "Severe thalassemia: Bart's hydrops, homozygous β, β-thal/HbE",
        "Thal: microcytic + target cell + ตับม้ามโต · HbH inclusion ใน supravital",
        "HbH/β-thal/HbE ไข้แล้วซีดลงเร็ว = acute hemolytic crisis",
    ],
    items=[
        mcq("HEMATO-03-01-1",
            "A 23-year-old man has fatigue and dark urine for 2 days after 3 days of fever. He has had intermittent jaundice since childhood. PE: moderate pallor, mild jaundice, liver and spleen just palpable. CBC: Hb 7 g/dL, MCV 58 fL, RDW 20%, WBC 4,500/µL, platelet 320,000/µL. PBS: hypochromic microcytic RBC 2+, anisopoikilocytosis 2+, target cells, few polychromasia. What is the most likely diagnosis?",
            "Thalassemia disease with acute hemolysis",
            ["G6PD deficiency", "Hereditary spherocytosis", "Autoimmune hemolytic anemia", "Paroxysmal nocturnal hemoglobinuria"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มประวัติเหลืองตั้งแต่เด็กและ target cell)",
            explain='''**Microcytic มาก (MCV 58) + RDW สูง + target cell + ตับม้ามโต** และเหลืองเป็นพัก ๆ มาตั้งแต่เด็ก = thalassemia disease (เช่น HbH, β-thal/HbE) ที่แตกเฉียบพลันเมื่อมีไข้
- G6PD ก็แตกตามไข้และปัสสาวะดำ แต่ **MCV ปกติ** ไม่มีตับม้ามโต PBS เป็น bite/ghost cell
- HS เป็น spherocyte MCV ปกติ
- AIHA เป็น spherocyte DAT บวก ไม่ microcytic
- PNH มีปัสสาวะดำตอนเช้า + pancytopenia ไม่มีม้ามโตและ target cell''',
            pearl="Microcytic + hemolysis + ม้ามโต = thalassemia disease", topic="Thalassemia vs other hemolysis",
            ref=[f"{D} หน้า 98, 131–132"], nl=["2.3.3(8)"]),
        mcq("HEMATO-03-01-2",
            "A 20-year-old man develops fatigue after taking amoxicillin for acute tonsillitis. PE: mild jaundice, pale conjunctivae, hepatosplenomegaly. CBC: Hb 7 g/dL, Hct 21%, WBC 9,600/µL, platelet 300,000/µL, MCV 65 fL. PBS: polychromasia 2+, hypochromic microcytic RBC, target cells. Supravital stain shows numerous inclusion bodies giving a golf-ball appearance. What is the most likely diagnosis?",
            "Hb H disease",
            ["G6PD deficiency", "Paroxysmal nocturnal hemoglobinuria", "Autoimmune hemolytic anemia", "Hereditary spherocytosis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มภาพ supravital ที่เป็นข้อความ)",
            explain='''Microcytic + ตับม้ามโต + hemolysis หลังติดเชื้อ + **HbH inclusion (golf-ball, β4 ตกตะกอน)** = **Hb H disease (--/-α)** with acute hemolytic crisis
- G6PD: Heinz body เป็นก้อนน้อยชิดขอบเซลล์ ไม่ใช่ golf-ball และ MCV ปกติ ไม่มีม้ามโต — amoxicillin ไม่ใช่ oxidant drug
- PNH ไม่ microcytic แบบมี target cell และไม่มีม้ามโต
- AIHA/HS เป็น spherocyte ไม่ใช่ microcytic hypochromic''',
            pearl="Microcytic + ม้ามโต + golf-ball inclusion = HbH", topic="HbH disease",
            ref=[f"{D} หน้า 98, 135–136"], nl=["2.3.3(8)"]),
        mcq("HEMATO-03-01-3",
            "A 28-year-old man presents with dyspnea on exertion and fever for 2 days. BT 38.5°C, PR 115/min. PE: marked pallor, mild jaundice, hepatomegaly. CBC: Hct 24%, Hb 7.1 g/dL, MCV 68 fL, WBC 14,000/µL, platelet 240,000/µL. PBS: hypochromia 2+, anisopoikilocytosis 2+, target cells, polychromasia, basophilic stippling. He works as an office clerk. What is the most likely diagnosis?",
            "Hb H disease",
            ["Lead poisoning", "Autoimmune hemolytic anemia", "G6PD deficiency", "Thalassemia trait"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มอาชีพเพื่อตัด lead)",
            explain='''ไข้ → ซีดมาก + เหลือง + **ตับโต** + microcytic + target cell + polychromasia = thalassemia disease with acute hemolysis → ตัวเลือกที่เข้าคือ **Hb H disease** (basophilic stippling พบใน thalassemia ได้)
- Lead poisoning มี basophilic stippling เช่นกัน แต่ต้องมีประวัติสัมผัส + ปวดท้อง/neuropathy ไม่มีตับโตและไข้
- AIHA และ G6PD เป็น normocytic
- Thalassemia **trait** ไม่ซีดมากขนาด Hb 7 และไม่มีตับโต/hemolysis''',
            pearl="Basophilic stippling: lead หรือ thalassemia — ดูบริบท", topic="Basophilic stippling",
            ref=[f"{D} หน้า 133–134"], nl=["2.3.3(8)"]),
    ])

# ---------------------------------------------------------------- 03-02 Hb typing
F_TYPE = fig("hemato-03-02-f1", "อ่านผล Hb typing", '''<svg viewBox="0 0 740 420">
 <rect x="20" y="10" width="700" height="34" rx="8" class="sunk"/>
 <text x="190" y="32" text-anchor="middle" class="tb">ผล Hb typing</text>
 <text x="540" y="32" text-anchor="middle" class="tb">แปลผล</text>
 <rect x="20" y="52" width="330" height="34" rx="8" class="box"/>
 <text x="36" y="74" class="t2">Bart's &gt; 80%</text>
 <rect x="360" y="52" width="360" height="34" rx="8" class="badsoft"/>
 <text x="376" y="74" class="tb">Hb Bart's hydrops fetalis</text>
 <rect x="20" y="92" width="330" height="34" rx="8" class="box"/>
 <text x="36" y="114" class="t2">A, A2, Bart's, H</text>
 <rect x="360" y="92" width="360" height="34" rx="8" class="misssoft"/>
 <text x="376" y="114" class="tb">Hb H disease</text>
 <rect x="20" y="132" width="330" height="74" rx="8" class="box"/>
 <text x="36" y="154" class="t2">A, A2 · A2 &lt; 3.5% (ดูเหมือนปกติ)</text>
 <text x="36" y="176" class="t3">ต้องดู MCV ประกอบ</text>
 <rect x="360" y="132" width="360" height="34" rx="8" class="oksoft"/>
 <text x="376" y="154" class="t2">MCV &gt; 80 → ปกติ หรือ α-thal 2 trait</text>
 <rect x="360" y="172" width="360" height="34" rx="8" class="c1soft"/>
 <text x="376" y="194" class="t2">MCV &lt; 75 → α-thal 1 trait (ส่ง DNA)</text>
 <rect x="20" y="212" width="330" height="34" rx="8" class="box"/>
 <text x="36" y="234" class="t2">A, A2 · A2 &gt; 3.5%</text>
 <rect x="360" y="212" width="360" height="34" rx="8" class="oksoft"/>
 <text x="376" y="234" class="tb">β-thal trait</text>
 <rect x="20" y="252" width="330" height="34" rx="8" class="box"/>
 <text x="36" y="274" class="t2">A2, F (ไม่มี A)</text>
 <rect x="360" y="252" width="360" height="34" rx="8" class="badsoft"/>
 <text x="376" y="274" class="tb">Homozygous β-thal</text>
 <rect x="20" y="292" width="330" height="34" rx="8" class="box"/>
 <text x="36" y="314" class="t2">E, F · E 80–100%</text>
 <rect x="360" y="292" width="360" height="34" rx="8" class="oksoft"/>
 <text x="376" y="314" class="tb">Homozygous HbE</text>
 <rect x="20" y="332" width="330" height="34" rx="8" class="box"/>
 <text x="36" y="354" class="t2">E, F · E 40–60%</text>
 <rect x="360" y="332" width="360" height="34" rx="8" class="misssoft"/>
 <text x="376" y="354" class="tb">β-thal/HbE disease</text>
 <rect x="20" y="372" width="330" height="40" rx="8" class="box"/>
 <text x="36" y="390" class="t2">A, E · E 25–35%</text>
 <text x="36" y="406" class="t3">A, E · E &lt; 25%</text>
 <rect x="360" y="372" width="360" height="40" rx="8" class="oksoft"/>
 <text x="376" y="390" class="t2">HbE trait (ไม่มี α-thal ร่วมแน่)</text>
 <text x="376" y="406" class="t3">HbE trait ± α-thal 1 trait ร่วม</text>
</svg>''', "อ่านจากซ้ายไปขวา: ชนิดและสัดส่วน Hb → genotype · ทุกแบบยกเว้น HbE trait ที่ E 25–35% ยังตัด α-thal 1 trait ที่ซ่อนอยู่ไม่ได้")

S2 = sec("hemato-03-02", "Hb typing interpretation",
    "Bart's >80% = hydrops · A A2 Bart's H = HbH · A2 >3.5% = β trait · A2F = homo β · EF: E 80–100 homo E, 40–60 β/E, 25–35 E trait", minutes=6,
    source=f"{D} หน้า 108–130, 139–142", nl=["3.3.5", "2.3.3(8)"],
    md='''
### หลักการ

- Hb typing (HPLC/electrophoresis) บอก **ชนิดและสัดส่วน** Hb — ใช้วินิจฉัย β-thal, HbE และ HbH/Bart's
- **ตรวจ α-thal trait ไม่ได้** (A, A2 ปกติ) → ต้องดู **MCV** ประกอบ และยืนยันด้วย **PCR/DNA analysis for α-thal 1**
- HbE แยกจาก A2 ไม่ได้ในบางวิธี จึงรายงานเป็น "A2/E" (เสริม)

[[fig:hemato-03-02-f1]]

### ตารางแปลผล (ตามสไลด์)

| ผล | แปลผล |
|---|---|
| Bart's > 80% | Hb Bart's hydrops fetalis |
| A A2 Bart's H | Hb H disease |
| A A2, A2 < 3.5%, **MCV > 80** | ปกติ หรือ α-thal 2 trait |
| A A2, A2 < 3.5%, **MCV < 75** | α-thal 1 trait |
| A A2, **A2 > 3.5%** | β-thal trait ± α-thal 1 trait |
| **A2 F** (ไม่มี A) | Homozygous β-thal ± α-thal 1 trait |
| E F, **E 80–100%** | Homozygous HbE ± α-thal 1 trait |
| A E, **E 25–35%** | HbE trait **(ไม่มี α-thal trait แน่)** |
| E F, **E 40–60%** | β-thal/HbE ± α-thal 1 trait |
| A E, **E < 25%** | HbE trait **± α-thal 1 trait** (α ขาด → βE จับ α ได้น้อยลง) |

> Hb typing แปลผลผิดได้ถ้ามี **IDA** ร่วม (A2 ต่ำลง) → R/O IDA ก่อน · ถ้าภาพซีดรุนแรงเกินกว่าที่ genotype อธิบายได้ (เช่น homo E แต่ Hct 19%) ให้หาสาเหตุอื่นร่วม เช่น **IDA**
''',
    figs=[F_TYPE],
    pearls=[
        "A2 > 3.5% = β-thal trait",
        "A2 F ไม่มี A = homozygous β-thal",
        "HbE: 80–100% homo E · 40–60% β/E · 25–35% E trait",
        "Hb typing ตรวจ α-thal trait ไม่ได้ → ดู MCV + PCR α-thal 1",
        "Homo E ไม่ควรซีดมาก — ถ้าซีดมาก หา IDA ร่วม",
    ],
    items=[
        mcq("HEMATO-03-02-1",
            "A 25-year-old woman comes for an annual check-up. She is healthy with no family history of hematologic disease. PE: unremarkable. CBC: Hb 11 g/dL, Hct 34%, WBC 6,000/µL, platelet 300,000/µL, MCV 65 fL, RDW 14%. PBS: microcytic 1+, hypochromic 2+, target cells 3+. Serum ferritin is 85 ng/mL. What is the most appropriate investigation?",
            "Hemoglobin typing",
            ["Serum vitamin B12", "Serum TIBC and transferrin", "Bone marrow aspiration", "Osmotic fragility test alone"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่ม ferritin ปกติ และปรับ Hb ให้เข้ากับ trait)",
            explain='''MCV ต่ำมาก (65) แต่ Hb เกือบปกติ, RDW ปกติ, **target cell เด่น**, ferritin ปกติ (ตัด IDA) = thalassemia trait/HbE → ตรวจ **Hb typing** เพื่อแยก β-thal trait, HbE, homozygous HbE (ถ้า typing ปกติ + MCV < 75 → ส่ง DNA α-thal 1)
- Serum B12 ใช้กับ macrocytic
- TIBC/transferrin ซ้ำซ้อน เพราะ ferritin ปกติแล้ว
- Bone marrow ไม่จำเป็นในคนที่สุขภาพดี
- OF test ใช้เป็นการคัดกรองเท่านั้น ไม่ได้บอกชนิด (สไลด์ใช้ร่วม DCIP ในการคัดกรองหญิงตั้งครรภ์)''',
            pearl="Microcytic + target cell + ferritin ปกติ → Hb typing", topic="Thal trait work-up",
            ref=[f"{D} หน้า 139–140"], nl=["3.3.5"]),
        mcq("HEMATO-03-02-2",
            "A 40-year-old woman has dyspnea on exertion for 1 month. PE: marked pallor, no jaundice, no hepatosplenomegaly. CBC: Hct 19%, WBC 7,300/µL, platelet 580,000/µL, MCV 52 fL, RDW 20%. Hb typing: A2/E 90%, F 6%. What is the most likely cause of her anemia?",
            "Iron deficiency anemia with homozygous HbE",
            ["HbH disease", "Beta-thalassemia/HbE disease", "Myelodysplastic syndrome", "Homozygous HbE alone"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Hb typing E 90% + F = **homozygous HbE** ซึ่งปกติ **ไม่ซีดหรือซีดน้อย** — แต่รายนี้ Hct 19% ซีดมาก, **platelet สูง, RDW สูง** ไม่มีม้ามโต → มี **IDA ร่วม** (สไลด์: "Severe anemia ขนาดนี้ไม่เหมือน Homo E")
- HbH disease จะเห็น Bart's และ H ใน typing
- β-thal/HbE ต้องมี E 40–60% และมักมีม้ามโต
- MDS ไม่อธิบาย E 90%
- Homozygous HbE อย่างเดียวไม่ทำให้ Hct 19% และ platelet 580,000''',
            pearl="Genotype อธิบายความรุนแรงไม่ได้ → หาสาเหตุร่วม (IDA)", topic="Homo E + IDA",
            ref=[f"{D} หน้า 141–142"], nl=["3.3.5", "2.3.3(8)"]),
        mcq("HEMATO-03-02-3",
            "A 30-year-old woman has Hb 12 g/dL and MCV 64 fL. Serum ferritin is normal. Hb typing shows Hb A 92% and Hb A2 6.1%. What is the most likely diagnosis?",
            "Beta-thalassemia trait",
            ["Alpha-thalassemia 1 trait", "HbE trait", "Homozygous beta-thalassemia", "Hb H disease"],
            explain='''Typing มี A และ **A2 > 3.5%** (6.1%) = **β-thal trait** (ไม่สร้าง β จึงจับ δ เป็น A2 แทน)
- α-thal 1 trait: A2 < 3.5% (typing ดูปกติ) ต้องอาศัย MCV < 75 + DNA
- HbE trait: จะเห็น Hb E 25–35%
- Homozygous β-thal: ไม่มี Hb A เลย มีแต่ A2 และ F และซีดมาก
- Hb H disease: จะเห็น Hb Bart's/H''',
            pearl="A2 > 3.5% = β-thal trait", topic="Hb typing pattern",
            ref=[f"{D} หน้า 121, 129"], nl=["3.3.5"]),
        mcq("HEMATO-03-02-4",
            "A 26-year-old pregnant woman has MCV 72 fL and normal ferritin. Hb typing: Hb A 97.6%, Hb A2 2.4%, no abnormal hemoglobin. What is the most appropriate interpretation and next step?",
            "Possible alpha-thalassemia 1 trait; send PCR for alpha-thalassemia 1",
            ["Normal result; no further testing", "Beta-thalassemia trait; test the husband for HbE only", "Iron deficiency; start oral iron", "Hb H disease; arrange transfusion"],
            explain='''Typing **A, A2 < 3.5%** ดูเหมือนปกติ แต่ **MCV < 75** และ ferritin ปกติ = สงสัย **α-thal 1 trait (--/αα)** ซึ่ง Hb typing มองไม่เห็น → ยืนยันด้วย **PCR for α-thal 1** (สำคัญเพราะถ้าสามีเป็นด้วย ลูกเสี่ยง Bart's hydrops 25%)
- สรุปว่าปกติผิด เพราะ MCV ต่ำแบบนี้ยังตัด α-thal 1 trait ไม่ได้
- β-thal trait ต้องมี A2 > 3.5%
- Ferritin ปกติ จึงไม่ใช่ IDA
- Hb H disease จะเห็น Bart's/H ใน typing และซีดชัด''',
            pearl="Typing ปกติ + MCV < 75 → PCR α-thal 1", topic="Detecting α-thal 1 trait",
            ref=[f"{D} หน้า 105, 129–130"], nl=["3.3.5", "B1.3.4(1)"]),
    ])

# ---------------------------------------------------------------- 03-03 Screening & counseling
F_SCR = fig("hemato-03-03-f1", "คัดกรอง severe thalassemia ในหญิงตั้งครรภ์", '''<svg viewBox="0 0 740 440">
 <defs><marker id="hemato-03-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="10" width="280" height="44" rx="10" class="acsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">หญิงตั้งครรภ์: MCV + DCIP</text>
 <text x="370" y="46" text-anchor="middle" class="t3">(OF test ใช้ร่วมได้)</text>
 <path d="M300 54L160 86" class="ln" marker-end="url(#hemato-03-03-a)"/>
 <path d="M440 54L580 86" class="ln" marker-end="url(#hemato-03-03-a)"/>
 <rect x="20" y="88" width="280" height="44" rx="10" class="oksoft"/>
 <text x="160" y="108" text-anchor="middle" class="tb">MCV ≥ 80 และ DCIP ลบ</text>
 <text x="160" y="124" text-anchor="middle" class="t3">ฝากครรภ์ตามปกติ</text>
 <rect x="440" y="88" width="280" height="44" rx="10" class="misssoft"/>
 <text x="580" y="108" text-anchor="middle" class="tb">MCV &lt; 80 หรือ DCIP บวก</text>
 <text x="580" y="124" text-anchor="middle" class="t3">→ ตรวจสามี (MCV + DCIP)</text>
 <path d="M520 132L400 164" class="ln" marker-end="url(#hemato-03-03-a)"/>
 <path d="M640 132V164" class="ln" marker-end="url(#hemato-03-03-a)"/>
 <rect x="250" y="166" width="230" height="44" rx="10" class="oksoft"/>
 <text x="365" y="186" text-anchor="middle" class="tb">สามีปกติ</text>
 <text x="365" y="202" text-anchor="middle" class="t3">non-couple at risk</text>
 <rect x="500" y="166" width="220" height="44" rx="10" class="misssoft"/>
 <text x="610" y="186" text-anchor="middle" class="tb">สามีผิดปกติด้วย</text>
 <text x="610" y="202" text-anchor="middle" class="t3">→ Hb typing ทั้งคู่</text>
 <path d="M560 210L250 246" class="ln" marker-end="url(#hemato-03-03-a)"/>
 <path d="M640 210V246" class="ln" marker-end="url(#hemato-03-03-a)"/>
 <rect x="20" y="248" width="380" height="64" rx="10" class="box"/>
 <text x="210" y="270" text-anchor="middle" class="tb">β-thal ทั้งคู่ หรือ β-thal + HbE</text>
 <text x="210" y="290" text-anchor="middle" class="t2">couple at risk: homo β / β-thal/HbE</text>
 <text x="210" y="306" text-anchor="middle" class="t3">ยืนยัน PCR β-globin</text>
 <rect x="420" y="248" width="300" height="64" rx="10" class="box"/>
 <text x="570" y="270" text-anchor="middle" class="tb">Typing ปกติ + MCV &lt; 75 ทั้งคู่</text>
 <text x="570" y="290" text-anchor="middle" class="t2">(หรือยังตัด α-thal 1 ไม่ได้)</text>
 <text x="570" y="306" text-anchor="middle" class="t3">→ PCR α-thal 1 ทั้งคู่</text>
 <path d="M640 312L640 344" class="ln" marker-end="url(#hemato-03-03-a)"/>
 <path d="M520 312L470 344" class="ln" marker-end="url(#hemato-03-03-a)"/>
 <rect x="560" y="346" width="160" height="44" rx="10" class="badsoft"/>
 <text x="640" y="366" text-anchor="middle" class="tb">บวกทั้งคู่</text>
 <text x="640" y="382" text-anchor="middle" class="t3">at risk Bart's hydrops</text>
 <rect x="380" y="346" width="170" height="44" rx="10" class="oksoft"/>
 <text x="465" y="366" text-anchor="middle" class="tb">ลบคนใดคนหนึ่ง</text>
 <text x="465" y="382" text-anchor="middle" class="t3">non-couple at risk</text>
 <path d="M170 312V394" class="ln" marker-end="url(#hemato-03-03-a)"/>
 <rect x="20" y="396" width="300" height="36" rx="10" class="bad"/>
 <text x="170" y="419" text-anchor="middle" class="tw">Couple at risk → PND (ตรวจทารก)</text>
 <path d="M640 390V414H324" class="ln" marker-end="url(#hemato-03-03-a)"/>
</svg>''', "เริ่มคัดกรองแม่ → ถ้าผิดปกติจึงตรวจพ่อ → ถ้าทั้งคู่ผิดปกติจึงทำ Hb typing/PCR เพื่อหา couple at risk ที่ต้องทำ prenatal diagnosis")

S3 = sec("hemato-03-03", "Thalassemia screening & genetic counseling",
    "MCV + DCIP คัดกรอง → ตรวจสามี → Hb typing / PCR α-thal 1 → couple at risk → PND · คำนวณความเสี่ยงลูกแบบ Mendel", minutes=8,
    source=f"{D} หน้า 103–105, 143–148", nl=["2.3.3(8)", "B1.3.4(1)", "2.3.15-3(11)"],
    md='''
### เป้าหมาย

ป้องกันการเกิด **severe thalassemia** 3 โรค: **Hb Bart's hydrops (--/--)**, **homozygous β-thal (βo/βo)**, **β-thal/HbE (βo/βE)**

### ขั้นตอนคัดกรอง (ตามสไลด์)

1. หญิงตั้งครรภ์ตรวจ **MCV และ DCIP** (DCIP = dichlorophenolindophenol ตรวจ HbE)
2. **MCV ≥ 80 และ DCIP ลบ** → ฝากครรภ์ตามปกติ
3. **MCV < 80 หรือ DCIP บวก** → **ตรวจเลือดสามี**
4. สามีผิดปกติด้วย → **Hb typing สามีและภรรยา**
   - มี **β-thal ทั้งคู่ หรือ β-thal + HbE** → couple at risk ต่อ homo β/β-thal/HbE → ยืนยัน PCR β-globin
   - **Typing ปกติ และ MCV < 75 ทั้งคู่** (หรือยัง R/O α-thal 1 ไม่ได้) → **PCR α-thal 1 ทั้งคู่**: บวกทั้งคู่ = couple at risk ต่อ Bart's hydrops · ลบคนใดคนหนึ่ง = non-couple at risk
5. **Couple at risk → prenatal diagnosis (PND)** (CVS/amniocentesis/cordocentesis — เสริม)

[[fig:hemato-03-03-f1]]

### คำนวณความเสี่ยงลูก (ยีนละครึ่งจากพ่อแม่)

- **α-thal**: ให้แต่ละคนส่ง "chromosome" ละ 1 ชุด เช่น HbH (--/-α) ส่ง -- หรือ -α ได้อย่างละ 50%
- **β-thal/HbE**: เช่น แม่ βo/βE × พ่อ β/βE → ลูก βo/β (trait), **βo/βE (disease)**, β/βE (E trait), βE/βE (homo E) อย่างละ 25% → เสี่ยง thalassemia disease **25%**

> ลูกเป็น HbH (--/-α) แสดงว่า **พ่อหรือแม่คนหนึ่งให้ --** (α-thal 1 trait มัก MCV < 80) และ **อีกคนให้ -α** (α-thal 2 trait MCV มักปกติ)
''',
    figs=[F_SCR],
    pearls=[
        "Severe thal ที่ต้องคัดกรอง: Bart's hydrops, homo β-thal, β-thal/HbE",
        "คัดกรองด้วย MCV < 80 หรือ DCIP บวก → ตรวจสามี",
        "β ทั้งคู่/β + E → couple at risk · α-thal 1 ทั้งคู่ → เสี่ยง Bart's 25%",
        "Couple at risk → prenatal diagnosis",
    ],
    items=[
        mcq("HEMATO-03-03-1",
            "A couple's first child has Hb H disease. Father: Hb 13 g/dL, MCV 76 fL. Mother: Hb 13 g/dL, MCV 87 fL. Neither parent has Hb H on typing. What are the most likely genotypes of the parents?",
            "Father --/αα, mother -α/αα",
            ["Father --/-α, mother -α/αα", "Father -α/-α, mother -α/αα", "Father -α/αα, mother --/αα", "Father --/αα, mother -α/-α"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''ลูก HbH = **--/-α** → ได้ "--" จากพ่อหรือแม่คนหนึ่ง และ "-α" จากอีกคน · พ่อ **MCV 76** เข้ากับ **α-thal 1 trait (--/αα)** · แม่ **MCV 87** เข้ากับ **α-thal 2 trait (-α/αα)** ซึ่ง MCV มักปกติ
- พ่อ --/-α คือ HbH disease เอง จะซีดและ typing พบ H — แต่ Hb 13 และ typing ไม่พบ H
- พ่อ -α/-α ไม่มี "--" ให้ลูก ทั้งสองคนจึงให้ได้แค่ -α → ลูกเป็น HbH ไม่ได้
- พ่อ -α/αα + แม่ --/αα ให้ลูกเป็น HbH ได้ แต่ขัดกับ MCV (แม่ MCV 87 ไม่เข้ากับ α-thal 1 trait ส่วนพ่อ MCV 76 ต่ำเกินสำหรับ α-thal 2 trait)
- แม่ -α/-α ไม่มี "--" และพ่อ --/αα ก็ทำให้ลูก HbH ได้ แต่ -α/-α มักมี MCV ต่ำแบบ α-thal 1 trait ไม่ใช่ 87''',
            pearl="ลูก HbH: คนหนึ่ง --/αα (MCV ต่ำ) อีกคน -α/αα (MCV ปกติ)", topic="α-thal inheritance",
            ref=[f"{D} หน้า 143–144"], nl=["2.3.3(8)"]),
        mcq_ordered("HEMATO-03-03-2",
            "A couple seeks counseling. The mother has Hb 8 g/dL, MCV 65 fL; Hb typing: Hb F 45%, Hb A2/E 51% (no Hb A). The father has Hb 15 g/dL, MCV 85 fL; Hb typing: Hb A 65%, Hb A2/E 30%. What is the risk that their child will have thalassemia disease (beta-thalassemia/HbE)?",
            ["0%", "25%", "50%", "75%", "100%"], 1,
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''แม่ E 51% + F ไม่มี A = **β-thal/HbE (βo/βE)** · พ่อ A + E 30% = **HbE trait (β/βE)**
ลูก: แม่ให้ βo หรือ βE × พ่อให้ β หรือ βE → βo/β (β-thal trait) · **βo/βE (β-thal/HbE disease)** · βE/β (HbE trait) · βE/βE (homozygous HbE ซึ่งไม่ใช่ thalassemia disease) อย่างละ 25%
→ เสี่ยง thalassemia disease **25%**
- 0% ผิดเพราะลูกได้ βo จากแม่และ βE จากพ่อได้
- 50% คือรวม homo E เข้าไปด้วย ซึ่งอาการน้อยไม่นับเป็นโรค
- 75% และ 100% สูงเกินตาม Mendel''',
            pearl="βo/βE × β/βE → β-thal/HbE 25%", topic="β-thal/HbE risk",
            ref=[f"{D} หน้า 147–148"], nl=["2.3.3(8)", "B1.3.4(1)"]),
        mcq("HEMATO-03-03-3",
            "A couple previously had a child with Hb H disease. Woman: Hb 9 g/dL, MCV 65 fL, Hb typing A2 A Bart's H. Man: Hb 15 g/dL, MCV 85 fL, Hb typing A2 A with A2 2.5%; DNA testing confirms -α/αα. Which statement about their next fetus is TRUE?",
            "The risk of Hb H disease is 25%",
            ["The risk of Hb Bart's hydrops fetalis is 25%", "The chance of a completely normal genotype (αα/αα) is 25%", "The risk of alpha-thalassemia 2 trait is 50%", "The risk of Hb H disease is 50%"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (ระบุ genotype พ่อให้ชัด)",
            explain='''แม่เป็น **HbH (--/-α)** ส่ง -- หรือ -α · พ่อ **-α/αα** ส่ง -α หรือ αα
ลูก 4 แบบ อย่างละ 25%: **--/-α (HbH)** · --/αα (α-thal 1 trait) · -α/-α (homozygous α-thal 2) · -α/αα (α-thal 2 trait) → **HbH 25%**
- Bart's hydrops (--/--) ต้องได้ -- จากทั้งพ่อและแม่ — พ่อไม่มี -- จึงเป็น 0%
- Genotype ปกติ (αα/αα) เป็น 0% เพราะแม่ไม่มี αα ให้
- α-thal 2 trait (-α/αα) เป็น 25% ไม่ใช่ 50%
- HbH 50% สูงเกินไป''',
            pearl="HbH × α-thal 2 trait → ลูก HbH 25%, Bart's 0%", topic="α-thal counseling",
            ref=[f"{D} หน้า 145–146"], nl=["2.3.3(8)"]),
        mcq("HEMATO-03-03-4",
            "A 27-year-old woman at 10 weeks of gestation has MCV 74 fL and a positive DCIP test. Her husband's MCV and DCIP are both normal. What is the most appropriate next step?",
            "Routine antenatal care; the couple is not at risk for severe thalassemia",
            ["Hb typing for both partners", "PCR for alpha-thalassemia 1 in both partners", "Prenatal diagnosis by amniocentesis", "Recommend termination of pregnancy"],
            explain='''ตาม flow คัดกรอง: แม่ผิดปกติ → ตรวจสามี → **สามี MCV ≥ 80 และ DCIP ลบ** → ไม่ใช่ couple at risk → **ฝากครรภ์ตามปกติ** (ลูกอาจเป็นพาหะได้แต่ไม่เป็น severe thalassemia)
- Hb typing ทั้งคู่ทำเมื่อ**สามีผิดปกติด้วย**
- PCR α-thal 1 ทั้งคู่ทำเมื่อ typing ปกติแต่ MCV < 75 ทั้งคู่
- PND ทำเฉพาะ couple at risk
- การยุติการตั้งครรภ์ไม่มีข้อบ่งชี้''',
            pearl="สามีปกติ → non-couple at risk → ฝากครรภ์ปกติ", topic="Antenatal thal screening",
            ref=[f"{D} หน้า 103–105"], nl=["2.3.3(8)", "2.3.15-3(11)"]),
    ])

# ---------------------------------------------------------------- 03-04 Management & complications
S4 = sec("hemato-03-04", "Thalassemia: transfusion, chelation & complications",
    "Hypertransfusion keep Hb >9–10 · chelate เมื่อ ferritin >1,000 · DFP → agranulocytosis · splenectomy + vaccine · cardiac siderosis · EMH", minutes=8,
    source=f"{D} หน้า 99–101, 149–158", nl=["2.3.3(8)", "B2.4(2)", "B2.4(1)"],
    md='''
### Transfusion

| แบบ | ใช้เมื่อ | เป้าหมาย |
|---|---|---|
| **Palliative transfusion** | Hb < 7 g/dL หรือมีอาการรุนแรง (เช่น ช่วง hemolytic crisis) | แก้อาการ |
| **Hypertransfusion** | Thalassemia major/transfusion-dependent | **keep Hb > 9–10 g/dL** กดการสร้างเม็ดเลือดของตัวเอง ลดกระดูกผิดรูปและ EMH |

ใช้ **leukocyte-poor PRC (LPRC)** เพื่อลด FNHTR (เสริม)

### Iron chelation

- ข้อบ่งชี้: **ferritin > 1,000 ng/mL** หรือ **hypertransfusion > 1 ปี**

| ยา | วิธีให้ | ผลข้างเคียงเด่น |
|---|---|---|
| **Deferoxamine (DFO)** | IV/SC | Local reaction, **visual & auditory impairment**, growth retardation |
| **Deferiprone (DFP)** | PO | **Agranulocytosis** (ต้องติดตาม CBC ทุกสัปดาห์ — เสริม), GI, transaminitis, arthralgia |
| **Deferasirox (DFX)** | PO | Visual & auditory impairment, GI, rash, transaminitis, **↑Cr** |

### Splenectomy

- ข้อบ่งชี้: **ต้องรับ LPRC > 180–200 mL/kg/ปี**, **hypersplenism** (ติดเชื้อ/เลือดออกบ่อยจาก cytopenia), **compressive symptom** (ม้ามโตกดเบียด)
- ฉีด **pneumococcal และ Hib vaccine ก่อนตัดม้าม**

### ภาวะแทรกซ้อน

- **Iron overload (hemochromatosis)** จาก hemolysis + transfusion + ดูดซึมเหล็กมากขึ้น
  - หัวใจ → **cardiac siderosis** (heart failure, arrhythmia) = สาเหตุตายอันดับแรก
  - ตับ → cirrhosis · ตับอ่อน → DM · ต่อมไร้ท่ออื่น (hypogonadism, hypothyroid — เสริม)
- **Extramedullary hematopoiesis (EMH)**: มักที่ **ซี่โครง, paravertebral** → **paraspinal mass → spinal cord compression**; กะโหลก → ชัก
  - รักษา EMH: **transfusion** (กดการสร้างเม็ดเลือด) ± radiation, surgery
- **Gallstone** (pigment)
- Thrombosis โดยเฉพาะหลังตัดม้าม (เสริม)

> ผู้ป่วย β-thal/HbE ได้รับเลือดไม่สม่ำเสมอ หลังตัดม้าม มี paraspinal mass + อาการไขสันหลังถูกกด + NRC สูง → **EMH → ให้เลือด** (สไลด์) ± radiation
''',
    pearls=[
        "Hypertransfusion: keep Hb > 9–10 · palliative เมื่อ Hb < 7",
        "Chelate เมื่อ ferritin > 1,000 หรือรับเลือด > 1 ปี",
        "DFP → agranulocytosis · DFO → ตา/หู · DFX → ↑Cr",
        "Thal major หัวใจล้ม/arrhythmia = cardiac siderosis",
        "Paraspinal mass ใน thal = EMH → transfusion",
    ],
    items=[
        mcq("HEMATO-03-04-1",
            "A 17-year-old man with thalassemia major receives blood transfusions 3–4 times per year without iron chelation. For 1 month he has had exertional dyspnea and bilateral leg swelling. BP 90/60 mmHg, PR 120/min irregular. PE: crepitations in both lungs, hepatosplenomegaly. Serum ferritin is 4,800 ng/mL. What is the most likely pathologic finding in his heart?",
            "Myocardial siderosis",
            ["Myocardial extramedullary hematopoiesis", "Myocardial hypertrophy from high-output state", "Immune-mediated myocarditis", "Hemophagocytosis of myocytes"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มค่า ferritin)",
            explain='''Thalassemia major ที่รับเลือดซ้ำโดยไม่ได้ chelate → **iron overload** สะสมที่กล้ามเนื้อหัวใจ = **cardiac siderosis** → heart failure + arrhythmia (สาเหตุตายสำคัญ)
- EMH เกิดที่ซี่โครง/paravertebral/กะโหลก ไม่ใช่ในกล้ามเนื้อหัวใจ
- Hypertrophy จาก high output อาจเกิดในซีดเรื้อรัง แต่ไม่อธิบาย arrhythmia + ferritin สูงมาก
- Immune myocarditis และ hemophagocytosis ไม่ใช่ภาวะแทรกซ้อนของ thalassemia''',
            pearl="Thal + HF/arrhythmia = cardiac siderosis", topic="Iron overload heart",
            ref=[f"{D} หน้า 101, 151–154"], nl=["2.3.3(8)"]),
        mcq("HEMATO-03-04-2",
            "A 20-year-old woman with beta-thalassemia/HbE disease receives regular transfusions and started deferiprone 3 months ago for iron overload. Which adverse effect requires the closest monitoring?",
            "Agranulocytosis",
            ["Visual and auditory toxicity", "Rising serum creatinine", "Injection-site reaction", "Growth retardation"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (ตัวเลือกเดิมไม่มี agranulocytosis ที่สไลด์ไฮไลต์ — ปรับตัวเลือกใหม่)",
            explain='''**Deferiprone (DFP, oral)** ผลข้างเคียงที่อันตรายที่สุดคือ **agranulocytosis** → ต้องตรวจ CBC/ANC สม่ำเสมอ และหยุดยาเมื่อไข้ + neutropenia (อื่น ๆ: GI, transaminitis, arthralgia)
- Visual/auditory toxicity เป็นของ **deferoxamine** (และ deferasirox)
- Serum creatinine สูงเป็นของ **deferasirox**
- Injection-site reaction เป็นของ deferoxamine ที่ให้ SC/IV
- Growth retardation เป็นของ deferoxamine ในเด็ก
(หมายเหตุ: ตัวเลือกในสไลด์เดิมคือ aplastic crisis / thrombocytopenia / hemolytic crisis / transaminitis / ARF โดยสไลด์เฉลยถัดไปไฮไลต์ "agranulocytosis" — ถ้าเจอตัวเลือกเดิม ให้เลือกตัวที่เป็นผลของยา คือ transaminitis)''',
            pearl="Deferiprone → agranulocytosis", topic="Iron chelator side effects",
            ref=[f"{D} หน้า 100, 157–158"], nl=["B2.4(2)"]),
        mcq("HEMATO-03-04-3",
            "A 35-year-old man with beta-thalassemia/HbE disease had splenectomy at age 7 and receives transfusions infrequently. He has back pain and intermittent claudication-like leg weakness. MRI spine: multiple paraspinal masses. CBC: Hb 5 g/dL, MCV 65 fL, WBC 25,000/µL, NRC 20/100 WBC, platelet 840,000/µL. What is the most appropriate management?",
            "Blood transfusion",
            ["Bone marrow aspiration and biopsy", "Needle aspiration biopsy of the mass", "Intravenous dexamethasone", "Emergency laminectomy before any other treatment"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''Thalassemia ที่ได้เลือดน้อย → ไขกระดูกทำงานหนักจนเกิด **extramedullary hematopoiesis (EMH)** เป็น paraspinal mass กดไขสันหลัง · NRC และ platelet สูงหลังตัดม้าม → รักษาด้วย **blood transfusion (hypertransfusion)** เพื่อกดการสร้างเม็ดเลือด ± radiation/surgery
- BM aspiration ไม่ช่วยการรักษาและไม่จำเป็นในการวินิจฉัย EMH
- Needle biopsy ก้อน EMH เสี่ยงเลือดออก และภาพเข้ากับ EMH อยู่แล้ว
- Dexamethasone ใช้กับ cord compression จากมะเร็ง (metastasis/lymphoma)
- ผ่าตัดเป็นทางเลือกเมื่อรักษาอื่นไม่ได้ผล ไม่ใช่ขั้นแรก''',
            pearl="EMH ใน thal → transfusion (± radiation)", topic="Extramedullary hematopoiesis",
            ref=[f"{D} หน้า 101, 155–156"], nl=["2.3.3(8)", "2.2.38"]),
        mcq("HEMATO-03-04-4",
            "A 14-year-old girl with beta-thalassemia/HbE disease requires leukocyte-poor red cells at about 220 mL/kg/year and has massive splenomegaly. Splenectomy is planned. Which vaccine should be given before the operation?",
            "Pneumococcal vaccine",
            ["BCG vaccine", "Oral polio vaccine", "Hepatitis A vaccine", "Varicella vaccine"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (เพิ่มรายละเอียดข้อบ่งชี้ตัดม้าม)",
            explain='''ข้อบ่งชี้ splenectomy ในสไลด์: ใช้ LPRC > 180–200 mL/kg/ปี, hypersplenism, compressive symptom → ต้องฉีด **pneumococcal (และ Hib, ± meningococcal)** ก่อนผ่าตัด เพราะม้ามเป็นด่านกำจัด encapsulated bacteria
- BCG, oral polio และ varicella เป็นวัคซีนเชื้อเป็นตามตารางทั่วไป ไม่เกี่ยวกับการตัดม้าม
- Hepatitis B ควรได้ในผู้รับเลือดบ่อย แต่ hepatitis A ไม่ใช่วัคซีนเฉพาะก่อนตัดม้าม''',
            pearl="ก่อนตัดม้าม: pneumococcal + Hib", topic="Splenectomy vaccine",
            ref=[f"{D} หน้า 99, 149–150"], nl=["2.3.3(8)", "2.3.3-3(5)"]),
        mcq("HEMATO-03-04-5",
            "A 9-year-old boy with homozygous beta-thalassemia is on a regular transfusion program. Which pre-transfusion hemoglobin target best describes hypertransfusion?",
            "Keep hemoglobin above 9–10 g/dL",
            ["Transfuse only when hemoglobin falls below 5 g/dL", "Keep hemoglobin above 7 g/dL", "Keep hemoglobin above 14 g/dL", "Transfuse only during hemolytic crisis"],
            explain='''**Hypertransfusion** = ให้เลือดสม่ำเสมอเพื่อ **keep Hb > 9–10 g/dL** กดการสร้างเม็ดเลือดของตัวเอง ทำให้โตได้ปกติ ลดกระดูกผิดรูป ม้ามโต และ EMH (ต้องคู่กับ iron chelation)
- รอ Hb < 5 อันตรายและไม่ใช่โปรแกรมใด ๆ
- Hb > 7 / ให้เฉพาะ crisis คือ **palliative transfusion** (Hb < 7 หรืออาการรุนแรง) สำหรับ non-transfusion-dependent
- Hb > 14 สูงเกินจำเป็น เพิ่ม iron overload และ hyperviscosity''',
            pearl="Hypertransfusion: Hb > 9–10", topic="Transfusion program",
            ref=[f"{D} หน้า 99"], nl=["2.3.3(8)", "B2.4(1)"]),
    ])

LECTURE = lecture("03", "Thalassemia",
    "Genotype · Hb typing · คัดกรองคู่สมรส · transfusion & chelation",
    objectives=[
        "อธิบาย genotype และความรุนแรงของ α- และ β-thalassemia ได้",
        "แปลผล Hb typing ร่วมกับ MCV ได้ และรู้ว่าเมื่อไรต้องส่ง PCR α-thal 1",
        "ไล่ขั้นตอนคัดกรอง severe thalassemia ในหญิงตั้งครรภ์และคำนวณความเสี่ยงของลูกได้",
        "เลือก transfusion/chelation/splenectomy และจำผลข้างเคียงของ chelator ได้",
        "จำภาวะแทรกซ้อนสำคัญ: cardiac siderosis, EMH, gallstone",
    ],
    sections=[S1, S2, S3, S4])
