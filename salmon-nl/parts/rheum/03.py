from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Rheumato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 03-01 IBP & SpA overview
F_SPA = fig("rheum-03-01-f1", "Seronegative SpA: แกนร่วม + จุดเด่นแต่ละโรค", '''<svg viewBox="0 0 740 390">
 <rect x="215" y="10" width="310" height="132" rx="12" class="acsoft"/>
 <text x="370" y="34" text-anchor="middle" class="tb">แกนร่วมของ SpA</text>
 <text x="370" y="56" text-anchor="middle" class="t2">RF ลบ · HLA-B27 · ชาย &gt; หญิง · อายุ &lt; 45</text>
 <text x="370" y="78" text-anchor="middle" class="t2">Inflammatory back pain + sacroiliitis</text>
 <text x="370" y="100" text-anchor="middle" class="t2">Asymmetric oligoarthritis (ขาเด่น)</text>
 <text x="370" y="122" text-anchor="middle" class="t2">Enthesitis · dactylitis · uveitis</text>
 <path d="M240 142L110 176" class="lnf"/>
 <path d="M320 142L290 176" class="lnf"/>
 <path d="M420 142L455 176" class="lnf"/>
 <path d="M500 142L632 176" class="lnf"/>
 <rect x="10" y="178" width="170" height="200" rx="10" class="c1soft"/>
 <text x="20" y="200" class="tb">Ankylosing</text>
 <text x="20" y="218" class="tb">spondylitis</text>
 <text x="20" y="240" class="t3">พบบ่อยสุด · ชายวัยรุ่น</text>
 <text x="20" y="258" class="t3">กระดูกสันหลัง + SI</text>
 <text x="20" y="276" class="t3">chest expansion ↓</text>
 <text x="20" y="300" class="t2">Anterior uveitis</text>
 <text x="20" y="318" class="t2">Aortic regurgitation</text>
 <text x="20" y="336" class="t2">Upper lobe fibrosis</text>
 <text x="20" y="362" class="ta">Bamboo spine</text>
 <rect x="195" y="178" width="170" height="200" rx="10" class="misssoft"/>
 <text x="205" y="200" class="tb">Reactive arthritis</text>
 <text x="205" y="222" class="t3">1–4 สัปดาห์หลัง</text>
 <text x="205" y="240" class="t3">GI/GU infection</text>
 <text x="205" y="258" class="t3">oligo ขา · ส้นเท้า</text>
 <text x="205" y="282" class="t2">Conjunctivitis</text>
 <text x="205" y="300" class="t2">Urethritis</text>
 <text x="205" y="318" class="t2">Uveitis</text>
 <text x="205" y="336" class="t2">Keratoderma</text>
 <text x="205" y="362" class="ta">หายเอง 6–12 เดือน</text>
 <rect x="380" y="178" width="170" height="200" rx="10" class="c2soft"/>
 <text x="390" y="200" class="tb">Psoriatic arthritis</text>
 <text x="390" y="222" class="t3">ชาย = หญิง · 35–45 ปี</text>
 <text x="390" y="240" class="t3">DIP + PIP · ข้อใดก็ได้</text>
 <text x="390" y="258" class="t3">dactylitis เด่น</text>
 <text x="390" y="282" class="t2">Psoriasis</text>
 <text x="390" y="300" class="t2">Nail pitting</text>
 <text x="390" y="318" class="t2">Onycholysis</text>
 <text x="390" y="362" class="ta">Pencil-in-cup</text>
 <rect x="565" y="178" width="165" height="200" rx="10" class="oksoft"/>
 <text x="575" y="200" class="tb">IBD-associated</text>
 <text x="575" y="222" class="t3">ชาย = หญิง</text>
 <text x="575" y="240" class="t3">ข้อใหญ่ที่ขา</text>
 <text x="575" y="258" class="t3">± sacroiliitis</text>
 <text x="575" y="282" class="t2">Crohn, UC</text>
 <text x="575" y="300" class="t2">ท้องเสีย ถ่ายเป็นเลือด</text>
 <text x="575" y="318" class="t2">Erythema nodosum</text>
 <text x="575" y="362" class="ta">ข้อขาตาม activity ลำไส้</text>
</svg>''', "กล่องบนคือสิ่งที่ทุกโรคในกลุ่มมีร่วมกัน · การ์ดล่างคือ 'คำใบ้' ที่ข้อสอบใช้แยกแต่ละโรค (erythema nodosum และความสัมพันธ์กับ activity ลำไส้เป็นส่วนเสริม)")

S1 = sec("rheum-03-01", "Inflammatory back pain & seronegative spondyloarthropathies",
    "IBP: AM stiffness > 30 นาที ดีขึ้นเมื่อขยับ ESR/CRP ↑ · SpA = RF ลบ, HLA-B27, ชาย, < 45 ปี · AS, PsA, ReA, IBD · oligoarthritis อสมมาตร enthesitis dactylitis", minutes=7,
    source=f"{D} หน้า 52–56", nl=["2.3.13-3(13)", "B5.2.2-3(3)", "2.1.27"],
    md='''
### Inflammatory vs mechanical back pain (สไลด์หน้า 52)

| | **Inflammatory** | Mechanical |
|---|---|---|
| Morning stiffness | **> 30 นาที** | < 30 นาที |
| เมื่อขยับ/ออกกำลัง | **ดีขึ้น** | แย่ลง |
| Constitutional feature | มี | ไม่มี |
| Sign of inflammation | มี | ไม่มี/เล็กน้อย |
| Acute phase reactant (ESR, CRP) | **สูง** | ปกติ |

> ปวดหลังตื่นมาแข็ง ขยับแล้วดีขึ้น ปวดช่วงครึ่งหลังของคืนจนตื่น ในชาย < 40 ปี = inflammatory back pain → คิด AS (ส่วนอาการกลางคืนเป็นเสริม)

### Seronegative spondyloarthropathies (SpA) (สไลด์หน้า 53–54)
- **RF ลบ** (จึงเรียก seronegative) · สัมพันธ์ **HLA-B27** · **ชาย > หญิง** · เริ่มก่อนอายุ **45 ปี**
- กลไก (เสริม): การอักเสบเริ่มที่ **enthesis** (จุดเกาะของเอ็นกับกระดูก) → กระดูกงอกใหม่เชื่อมข้อ (ต่างจาก RA ที่เริ่มที่ synovium แล้วกัดกร่อน)
- ประกอบด้วย 4 โรค: **ankylosing spondylitis (พบบ่อยสุด)**, **psoriatic arthritis**, **reactive arthritis**, **SpA associated with IBD**

### ลักษณะร่วม (สไลด์หน้า 54)
- **Inflammatory back pain + sacroiliitis** ค่อย ๆ เป็นมากขึ้น · ปวดตึงตอนเช้า > 30 นาที ดีขึ้นเมื่อขยับ · **ตอบสนองดีต่อ NSAID**
- **Asymmetrical peripheral oligoarthritis** (ข้อใหญ่ที่ขาเด่น)
- **Enthesopathy** (เช่น Achilles, plantar fascia = ปวดส้นเท้า)
- **Dactylitis** = นิ้วมือ/นิ้วเท้าบวมทั้งนิ้วแบบ **sausage digit**

### Extra-articular (สไลด์หน้า 55–56)

| | AS | PsA | ReA | IBD-associated |
|---|---|---|---|---|
| อายุเริ่ม | วัยรุ่นตอนปลาย–ผู้ใหญ่ตอนต้น | 35–45 ปี | วัยรุ่น–ผู้ใหญ่ตอนต้น | อายุใดก็ได้ |
| เพศ | **ชาย** | เท่ากัน | **ชาย** | เท่ากัน |
| ข้อที่เป็น | กระดูกสันหลังและ SI | **ข้อใดก็ได้** | **ข้อขา** | ข้อขา |
| Sacroiliitis | **พบบ่อยมาก** | พบบ่อย | พบบ่อย | พบบ่อย |
| Peripheral arthritis | บางครั้ง | พบบ่อย | พบบ่อย | พบบ่อย |
| Enthesitis | พบบ่อย | **พบบ่อยมาก** | **พบบ่อยมาก** | บางครั้ง |
| Dactylitis | ไม่บ่อย | พบบ่อย | พบบ่อย | ไม่บ่อย |
| อาการนอกข้อเด่น | **uveitis**, aortic regurgitation, upper lobe fibrosis | **psoriasis, nail pitting** | **uveitis, conjunctivitis, urethritis, keratoderma blenorrhagicum** | IBD (ท้องเสีย) |

[[fig:rheum-03-01-f1]]
''',
    figs=[F_SPA],
    pearls=[
        "Inflammatory back pain: AM stiffness > 30 นาที ดีขึ้นเมื่อขยับ ESR/CRP สูง ตอบสนอง NSAID",
        "SpA = RF ลบ + HLA-B27 + ชาย + < 45 ปี",
        "AS, PsA, ReA, IBD-associated · AS พบบ่อยที่สุด",
        "Enthesitis + dactylitis (sausage digit) + oligoarthritis อสมมาตร = นึกถึง SpA",
        "Uveitis = AS · psoriasis/nail pitting = PsA · conjunctivitis/urethritis/keratoderma = ReA",
    ],
    items=[
        mcq("RHEUM-03-01-1",
            "A 26-year-old man has had low back pain for 8 months. He wakes up with back stiffness lasting about 1 hour, and the pain improves after exercise but worsens with rest. He takes ibuprofen with good relief. ESR is 52 mm/h. Which feature of his history most strongly indicates an inflammatory rather than mechanical cause?",
            "Morning stiffness longer than 30 minutes that improves with exercise",
            ["Pain that worsens after lifting heavy objects", "Pain radiating below the knee in a dermatomal pattern", "Pain relieved by bed rest", "Sudden onset after a twisting injury"],
            explain='''ลักษณะ **inflammatory back pain** (สไลด์หน้า 52): **AM stiffness > 30 นาที, ดีขึ้นเมื่อขยับ**, ESR/CRP สูง, ตอบสนองต่อ NSAID → คิด SpA โดยเฉพาะ AS
- ปวดมากขึ้นหลังยกของหนักเป็น mechanical pain
- ปวดร้าวลงขาตาม dermatome เป็น radiculopathy เช่น หมอนรองกระดูกกดทับเส้นประสาท
- ดีขึ้นเมื่อนอนพักเป็นลักษณะ mechanical (inflammatory จะแย่ลงเมื่อพัก)
- เริ่มทันทีหลังบิดตัวเป็นการบาดเจ็บของกล้ามเนื้อ/เอ็น''',
            pearl="IBP = stiffness > 30 นาที + ดีขึ้นเมื่อขยับ + แย่ลงเมื่อพัก", topic="Inflammatory back pain",
            ref=[f"{D} หน้า 52"], nl=["2.3.13-3(13)"]),
        mcq("RHEUM-03-01-2",
            "A 32-year-old man has painful swelling of his entire right second toe and left third finger, giving a sausage-like appearance, plus pain at the Achilles tendon insertion. Rheumatoid factor is negative. Which group of disease is most likely?",
            "Seronegative spondyloarthropathy",
            ["Rheumatoid arthritis", "Systemic lupus erythematosus", "Calcium pyrophosphate deposition disease", "Osteoarthritis"],
            explain='''**Dactylitis (sausage digit) + enthesitis (Achilles) + RF ลบ** ในชายอายุน้อย = **seronegative SpA** (สไลด์หน้า 53–54) — ต่อไปหาว่าเป็น PsA, ReA หรือ AS
- RA เป็น synovitis สมมาตรของ MCP/PIP ไม่ทำให้ทั้งนิ้วบวม และมัก RF หรือ anti-CCP บวก
- SLE arthritis ไม่มี deformity และไม่มี enthesitis เด่น
- CPPD เป็นผู้สูงอายุ > 60 ปี เป็นข้อเข่า/ข้อมือ
- OA ไม่ทำให้นิ้วบวมทั้งนิ้วหรือ enthesitis''',
            pearl="Sausage digit + enthesitis + RF ลบ = SpA", topic="SpA features",
            ref=[f"{D} หน้า 53–54"], nl=["2.3.13-3(13)", "B5.2.2-3(3)"]),
        mcq("RHEUM-03-01-3",
            "A 24-year-old man with chronic inflammatory back pain develops acute pain and redness of the right eye with photophobia and blurred vision. Slit-lamp examination shows cells in the anterior chamber. Which genetic marker is most strongly associated with his condition?",
            "HLA-B27",
            ["HLA-DR4", "HLA-B5801", "HLA-DR3", "HLA-DQ2"],
            explain='''ปวดหลังแบบ inflammatory + **anterior uveitis** = ankylosing spondylitis ซึ่งอยู่ในกลุ่ม SpA ที่สัมพันธ์กับ **HLA-B27** (สไลด์หน้า 53, 55)
- HLA-DR4 สัมพันธ์กับ RA (เสริม)
- HLA-B5801 สัมพันธ์กับการแพ้ allopurinol รุนแรง (SJS/TEN) ไม่ใช่ตัวโรค
- HLA-DR3 สัมพันธ์กับ SLE, type 1 DM (เสริม)
- HLA-DQ2 สัมพันธ์กับ celiac disease (เสริม)''',
            pearl="SpA + anterior uveitis → HLA-B27", topic="HLA-B27",
            ref=[f"{D} หน้า 53, 55"], nl=["2.3.13-3(13)", "2.3.7-3(8)"]),
    ])

# ---------------------------------------------------------------- 03-02 Reactive arthritis
S2 = sec("rheum-03-02", "Reactive arthritis (Reiter syndrome)",
    "1–4 สัปดาห์หลัง GI/GU infection · asymmetric oligoarthritis ขา · enthesitis dactylitis · conjunctivitis urethritis uveitis keratoderma · NSAID 1st line หายเอง 6–12 เดือน", minutes=6,
    source=f"{D} หน้า 57, 63–66", nl=["2.3.13-3(13)", "B5.2.2-3(3)", "2.3.1(19)"],
    md='''
### นิยามและกลไก (สไลด์หน้า 57)
- ข้ออักเสบที่ **ปลอดเชื้อ (sterile)** ตามหลัง **การติดเชื้อทางเดินอาหาร (GI) หรือทางเดินปัสสาวะ-สืบพันธุ์ (GU)** ประมาณ **1–4 สัปดาห์**
- เชื้อที่พบบ่อย (เสริม): GI — *Salmonella, Shigella, Campylobacter, Yersinia* · GU — *Chlamydia trachomatis*
- กลไก (เสริม): antigen ของเชื้อกระตุ้นภูมิคุ้มกันข้ามมาที่ข้อ ในคนที่มี HLA-B27 → น้ำไขข้อเป็นกลุ่ม inflammatory แต่ **Gram stain/culture ลบ**

### อาการ (สไลด์หน้า 57)
- **Asymmetrical oligoarthritis** เด่นที่ **ข้อขา** (เข่า ข้อเท้า)
- **Sacroiliitis, enthesitis** (ส้นเท้า Achilles, plantar fascia), **dactylitis**
- Extra-articular: **conjunctivitis, uveitis, urethritis** และผื่น **keratoderma blenorrhagicum** (ตุ่มหนาที่ฝ่ามือฝ่าเท้า) · circinate balanitis (เสริม)
- Triad เดิม "can't see, can't pee, can't climb a tree" (เสริม)

### Investigation
- **ESR, CRP สูง**
- น้ำไขข้อ: inflammatory (WBC 2,000–50,000, PMN สูง) **G/S, C/S ลบ ไม่มีผลึก**
- หาเชื้อต้นเหตุ: stool culture, urine NAAT สำหรับ Chlamydia (เสริม)

### การรักษา (สไลด์หน้า 57)
- **NSAID = 1st line** · ส่วนใหญ่ **หายเองใน 6–12 เดือน**
- ไม่ตอบสนอง: **intra-articular/systemic steroid, DMARD** (เช่น sulfasalazine — เสริม)
- ถ้ามี Chlamydia ที่ยังเป็นอยู่ รักษาการติดเชื้อนั้นด้วย (เสริม)

| แยกจาก | จุดแยก |
|---|---|
| **Septic arthritis** | ข้อเดียว WBC มัก > 50,000, G/S หรือ C/S บวก |
| **DGI** | migratory polyarthralgia + tenosynovitis + pustule, อาการเกิด **ระหว่าง** การติดเชื้อ ไม่ใช่หลังหาย |
| **Gout** | ผลึกรูปเข็มในน้ำไขข้อ, 1st MTP |
''',
    pearls=[
        "ReA = arthritis ขา 1–4 สัปดาห์หลังท้องเสียหรือปัสสาวะแสบขัด",
        "น้ำไขข้อ inflammatory แต่ Gram stain และ culture ลบ",
        "Conjunctivitis + urethritis + arthritis ± keratoderma blenorrhagicum",
        "NSAID 1st line · หายเองใน 6–12 เดือน",
    ],
    items=[
        mcq("RHEUM-03-02-1",
            "A 28-year-old man had diarrhea together with several students after a party. Three weeks later he develops aches, especially in the left knee, neck, and back. Examination shows swelling and tenderness of the left knee and limited range of motion of the neck and back due to pain. What is the most likely diagnosis?",
            "Reactive arthritis",
            ["Salmonellosis", "Septic arthritis", "Crystal-induced arthritis", "Rheumatoid arthritis"],
            kind="old", src=OLD,
            explain='''ท้องเสีย (GI infection) แล้ว **3 สัปดาห์ต่อมา** มี **oligoarthritis ที่เข่า + ปวดคอและหลัง (axial)** = **reactive arthritis**
- Salmonellosis เป็นการติดเชื้อต้นเหตุ ซึ่งหายไปแล้ว อาการข้อตอนนี้เป็นภูมิคุ้มกันที่ตามมา
- Septic arthritis มีไข้ ข้อเดียวเฉียบพลัน และไม่เกี่ยวกับกระดูกสันหลังแบบนี้
- Crystal-induced arthritis (gout) มักเป็นที่ 1st MTP ในชายวัยกลางคน ไม่มีอาการหลังและคอ
- RA เป็น polyarthritis สมมาตรของข้อเล็กมือ ไม่สัมพันธ์กับการติดเชื้อนำมาก่อน''',
            pearl="ท้องเสีย → 1–4 สัปดาห์ → oligoarthritis ขา ± หลัง = ReA", topic="Reactive arthritis",
            ref=[f"{D} หน้า 57, 63–64"], nl=["2.3.13-3(13)"]),
        mcq("RHEUM-03-02-2",
            "A 35-year-old man had dysuria 2 weeks ago, self-medicated for 3 days, and improved. One week later he developed pain in the right knee, left ankle, and left heel. Examination shows swelling and warmth of the right knee, left ankle, and left plantar area. Arthrocentesis: straw-colored fluid, WBC 3,500/mm3 (PMN 80%), no organisms on Gram stain, culture pending. Urinalysis: WBC 10–20/HPF, RBC 10–20/HPF. What is the most likely diagnosis?",
            "Reactive arthritis",
            ["Gram-negative septic arthritis", "Disseminated gonococcal infection", "Crystal-induced arthritis", "Rheumatoid arthritis"],
            kind="old", src=OLD,
            explain='''หลัง **urethritis** 1 สัปดาห์ เกิด **oligoarthritis ขาอสมมาตร + ปวดส้นเท้า/ฝ่าเท้า (enthesitis)** น้ำไขข้อเป็น inflammatory (WBC 3,500, PMN 80%) และ **Gram stain ไม่พบเชื้อ** = **reactive arthritis** (มักจาก Chlamydia)
- Gram-negative septic arthritis จะมี WBC สูงมาก (มัก > 50,000) และเป็นข้อเดียว
- DGI เกิด **ระหว่าง** การติดเชื้อหนองใน มี migratory polyarthralgia, tenosynovitis ของข้อมือ/มือ และตุ่มหนองที่ผิวหนัง
- Crystal-induced arthritis ต้องพบผลึก และไม่สัมพันธ์กับ urethritis
- RA เป็นข้อเล็กมือสมมาตร ไม่ใช่ข้อขาอสมมาตรกับ enthesitis''',
            pearl="Urethritis → arthritis ขา + enthesitis + SF inflammatory G/S ลบ = ReA", topic="Reactive arthritis",
            ref=[f"{D} หน้า 57, 65–66"], nl=["2.3.13-3(13)", "B5.3(3)"]),
        mcq("RHEUM-03-02-3",
            "A 30-year-old man develops asymmetric arthritis of the right knee and left ankle, bilateral conjunctivitis, and dysuria 3 weeks after an episode of bloody diarrhea. Synovial fluid culture is negative. What is the most appropriate initial treatment?",
            "Oral NSAID",
            ["Intravenous ceftriaxone", "Oral colchicine", "Methotrexate", "Adalimumab"],
            explain='''Reactive arthritis → **NSAID เป็น 1st line** และโรคมักหายเองใน 6–12 เดือน (สไลด์หน้า 57) · steroid หรือ DMARD ใช้เมื่อไม่ตอบสนอง
- Ceftriaxone ใช้กับ septic arthritis หรือ DGI — ReA เป็นการอักเสบแบบปลอดเชื้อ culture ลบ
- Colchicine ใช้กับ crystal arthritis
- Methotrexate และ adalimumab สำรองไว้สำหรับโรคที่เรื้อรังหรือดื้อต่อ NSAID ไม่ใช่การรักษาเริ่มต้น''',
            pearl="ReA: NSAID ก่อน · หายเอง 6–12 เดือน", topic="ReA treatment",
            ref=[f"{D} หน้า 57"], nl=["2.3.13-3(13)", "B5.4(1)"]),
    ])

# ---------------------------------------------------------------- 03-03 PsA
S3 = sec("rheum-03-03", "Psoriatic arthritis (PsA)",
    "Asymmetric oligoarthritis · DIP และ PIP · enthesitis dactylitis tenosynovitis · psoriasis + nail pitting/onycholysis · X-ray pencil-in-cup · NSAID, DMARD", minutes=5,
    source=f"{D} หน้า 58", nl=["2.3.13-3(13)", "2.3.12-3(11)"],
    md='''
### นิยามและใครเป็น
- ข้ออักเสบในผู้ป่วย **psoriasis** (ประมาณ 20–30% ของผู้ป่วย psoriasis — เสริม) · ชาย = หญิง อายุ 35–45 ปี
- ข้ออักเสบเกิดก่อนผื่นได้ (~15%) → ต้องหาผื่นที่ซ่อน เช่น หนังศีรษะ สะดือ ร่องก้น และ **เล็บ** (เสริม)

### อาการ (สไลด์หน้า 58)
- **Asymmetrical oligoarthritis** (เป็นรูปแบบหลักในสไลด์) · มีรูปแบบอื่นได้ เช่น polyarthritis สมมาตรคล้าย RA, arthritis mutilans, axial (เสริม)
- **DIP และ PIP joints** → ต่างจาก RA ที่เว้น DIP
- **Enthesitis, dactylitis, tenosynovitis**
- **Psoriasis** (erythematous plaque มี silvery scale)
- **Nail involvement: pitting, onycholysis** — พบบ่อยในคนที่ DIP อักเสบ

### Investigation
- **ESR, CRP สูง** · RF ลบ
- **X-ray: pencil-in-cup deformity ของ DIP** (ปลายกระดูกถูกกร่อนแหลมเสียบเข้าไปในฐานที่บานออก) · มีกระดูกงอกใหม่ (periostitis) ได้ (เสริม)

### การรักษา (สไลด์หน้า 58)
- **NSAID, DMARD** (methotrexate ช่วยทั้งผิวหนังและข้อ — เสริม) · biologic anti-TNF ถ้าไม่ตอบสนอง (เสริม)
- หลีกเลี่ยง systemic steroid ขนาดสูงในผู้ป่วย psoriasis เพราะผื่นกำเริบรุนแรงเมื่อหยุด (pustular flare — เสริม)

| | PsA | RA | OA |
|---|---|---|---|
| ข้อ | DIP, PIP อสมมาตร | MCP, PIP, wrist สมมาตร | DIP, PIP, 1st CMC |
| นิ้วบวมทั้งนิ้ว | **dactylitis** | ไม่มี | ไม่มี |
| เล็บ | **pitting, onycholysis** | ปกติ | ปกติ |
| X-ray | **pencil-in-cup** | marginal erosion + osteopenia | osteophyte + sclerosis |
| RF | ลบ | บวก (~70–80%) | ลบ |
''',
    pearls=[
        "PsA = DIP + nail pitting/onycholysis + psoriasis",
        "Dactylitis และ enthesitis พบบ่อยมากใน PsA",
        "X-ray: pencil-in-cup ที่ DIP",
        "Tx: NSAID, DMARD (MTX) · ข้ออักเสบอาจมาก่อนผื่น → หาผื่นและดูเล็บ",
    ],
    items=[
        mcq("RHEUM-03-03-1",
            "A 42-year-old man has pain and swelling of several DIP joints of both hands asymmetrically and diffuse swelling of the left fourth toe. Examination shows pitting and onycholysis of several fingernails and scaly erythematous plaques on both elbows. Rheumatoid factor is negative. What is the most likely diagnosis?",
            "Psoriatic arthritis",
            ["Rheumatoid arthritis", "Osteoarthritis", "Reactive arthritis", "Chronic tophaceous gout"],
            explain='''**DIP อสมมาตร + dactylitis (นิ้วเท้าบวมทั้งนิ้ว) + nail pitting/onycholysis + plaque ที่ข้อศอก (psoriasis)** = **psoriatic arthritis** (สไลด์หน้า 58)
- RA เว้น DIP เป็นสมมาตรและไม่มีเล็บผิดปกติ
- OA มี Heberden node ที่ DIP ได้ แต่ไม่มี dactylitis เล็บ pitting หรือผื่น
- Reactive arthritis เป็นข้อขาตามหลังการติดเชื้อ ผื่นคือ keratoderma ที่ฝ่ามือฝ่าเท้า
- Chronic gout มี tophi ที่ข้อและติ่งหู ไม่ใช่ผื่นสะเก็ดเงิน''',
            pearl="DIP + nail pitting + psoriasis = PsA", topic="PsA diagnosis",
            ref=[f"{D} หน้า 58"], nl=["2.3.13-3(13)", "2.3.12-3(11)"]),
        mcq("RHEUM-03-03-2",
            "A 50-year-old woman with long-standing psoriasis has painful deformities of several distal interphalangeal joints. Which radiographic finding is most characteristic of her joint disease?",
            "Pencil-in-cup deformity of the DIP joints",
            ["Marginal erosions with periarticular osteopenia at the MCP joints", "Punched-out erosions with overhanging edges", "Chondrocalcinosis of the knee menisci", "Bamboo spine with syndesmophytes"],
            explain='''PsA ที่ DIP → X-ray **pencil-in-cup** (สไลด์หน้า 58)
- Marginal erosion + periarticular osteopenia ที่ MCP เป็นของ RA
- Punched-out lesion ที่มีขอบยื่นเป็นของ chronic gout
- Chondrocalcinosis เป็นของ CPPD
- Bamboo spine เป็นของ ankylosing spondylitis (PsA มีกระดูกสันหลังอักเสบได้ แต่ไม่ใช่ลักษณะที่ DIP)''',
            pearl="Pencil-in-cup = PsA", topic="PsA X-ray",
            ref=[f"{D} หน้า 58"], nl=["2.3.13-3(13)", "3.2.5"]),
        mcq("RHEUM-03-03-3",
            "A 38-year-old man with plaque psoriasis covering 15% of his body surface has active oligoarthritis of the knees and dactylitis despite 4 weeks of full-dose NSAID. Which drug would best treat both his skin and joint disease as the next step?",
            "Methotrexate",
            ["High-dose oral prednisolone", "Allopurinol", "Hydroxychloroquine", "Colchicine"],
            explain='''PsA ที่ไม่ตอบสนองต่อ NSAID → เพิ่ม **DMARD** (สไลด์: NSAID, DMARD) โดย **methotrexate** ช่วยทั้งผิวหนังและข้อ (การเลือก MTX เป็นเสริม)
- Prednisolone ขนาดสูงทำให้ psoriasis กำเริบรุนแรง (pustular/erythrodermic) เมื่อลดยา จึงหลีกเลี่ยง
- Allopurinol เป็นยาลดกรดยูริก ไม่ช่วย PsA
- Hydroxychloroquine อาจทำให้ psoriasis กำเริบและไม่ใช่ DMARD หลักของ PsA (เสริม)
- Colchicine ใช้กับ crystal arthritis''',
            pearl="PsA ดื้อ NSAID → MTX (ช่วยผิวด้วย) · เลี่ยง steroid ขนาดสูง", topic="PsA treatment",
            ref=[f"{D} หน้า 58"], nl=["B5.4(3)", "2.3.13-3(13)"]),
    ])

# ---------------------------------------------------------------- 03-04 AS
F_AS = fig("rheum-03-04-f1", "AS: การอักเสบเริ่มที่ enthesis → กระดูกงอกเชื่อมกัน (bamboo spine)", '''<svg viewBox="0 0 720 330">
 <defs><marker id="rheum-03-04-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <text x="110" y="22" text-anchor="middle" class="tb">ปกติ</text>
 <rect x="60" y="36" width="100" height="56" rx="6" class="box"/>
 <rect x="60" y="112" width="100" height="56" rx="6" class="box"/>
 <rect x="60" y="188" width="100" height="56" rx="6" class="box"/>
 <rect x="66" y="94" width="88" height="16" rx="4" class="sunk"/>
 <rect x="66" y="170" width="88" height="16" rx="4" class="sunk"/>
 <text x="110" y="270" text-anchor="middle" class="t3">หมอนรองกระดูกมีช่องว่าง</text>
 <text x="110" y="288" text-anchor="middle" class="t3">ขอบ vertebra ตรง</text>
 <path d="M200 140H250" class="ln" marker-end="url(#rheum-03-04-a)"/>
 <text x="350" y="22" text-anchor="middle" class="tb">AS ระยะแรก</text>
 <rect x="300" y="36" width="100" height="56" rx="6" class="box"/>
 <rect x="300" y="112" width="100" height="56" rx="6" class="box"/>
 <rect x="300" y="188" width="100" height="56" rx="6" class="box"/>
 <rect x="306" y="94" width="88" height="16" rx="4" class="sunk"/>
 <rect x="306" y="170" width="88" height="16" rx="4" class="sunk"/>
 <circle cx="300" cy="92" r="7" class="bad"/>
 <circle cx="400" cy="92" r="7" class="bad"/>
 <circle cx="300" cy="168" r="7" class="bad"/>
 <circle cx="400" cy="168" r="7" class="bad"/>
 <text x="350" y="270" text-anchor="middle" class="t3">enthesitis ที่มุม vertebra</text>
 <text x="350" y="288" text-anchor="middle" class="t3">(Romanus lesion — เสริม)</text>
 <path d="M440 140H490" class="ln" marker-end="url(#rheum-03-04-a)"/>
 <text x="590" y="22" text-anchor="middle" class="tb">Bamboo spine</text>
 <rect x="540" y="36" width="100" height="56" rx="6" class="box"/>
 <rect x="540" y="112" width="100" height="56" rx="6" class="box"/>
 <rect x="540" y="188" width="100" height="56" rx="6" class="box"/>
 <rect x="546" y="94" width="88" height="16" rx="4" class="sunk"/>
 <rect x="546" y="170" width="88" height="16" rx="4" class="sunk"/>
 <path d="M541 86Q535 102 541 118" class="lnbad"/>
 <path d="M639 86Q645 102 639 118" class="lnbad"/>
 <path d="M541 162Q535 178 541 194" class="lnbad"/>
 <path d="M639 162Q645 178 639 194" class="lnbad"/>
 <text x="590" y="270" text-anchor="middle" class="t3">syndesmophyte เชื่อมข้อ</text>
 <text x="590" y="288" text-anchor="middle" class="t3">กระดูกสันหลังเป็นแท่งเดียว</text>
 <rect x="20" y="300" width="680" height="26" rx="6" class="sunk"/>
 <text x="360" y="318" text-anchor="middle" class="t2">มักเริ่มที่ sacroiliac joint (sacroiliitis สองข้าง) แล้วลามขึ้น lumbar → thoracic → cervical</text>
</svg>''', "อ่านซ้ายไปขวา: กระดูกสันหลังปกติ → enthesitis ที่มุมกระดูก → syndesmophyte เชื่อมระหว่างข้อจนเห็นเป็นปล้องไผ่ (เส้นแดง) · ตรงข้ามกับ RA ที่กัดกร่อนกระดูก")

S4 = sec("rheum-03-04", "Ankylosing spondylitis (AS)",
    "Axial SpA · IBP + AM stiffness > 30 นาที · spine mobility ↓, SI tenderness, chest expansion ↓, FABER · anterior uveitis · X-ray sacroiliitis, bamboo spine · NSAID 1st line → anti-TNF", minutes=7,
    source=f"{D} หน้า 59–62", nl=["2.3.13-3(13)", "B5.2.2-3(3)", "2.3.7-3(8)"],
    md='''
### นิยามและใครเป็น
- **Axial spondyloarthritis** ที่พบบ่อยที่สุดในกลุ่ม SpA · **ชาย** วัยรุ่นตอนปลายถึงผู้ใหญ่ตอนต้น · HLA-B27 บวก ~90% (เสริม)

### อาการ (สไลด์หน้า 59)
- **Inflammatory back pain**: **morning stiffness > 30 นาที**, **ดีขึ้นเมื่อขยับ**
- **Restricted spine mobility** (ก้มหลังได้น้อย — Schober test ผิดปกติ, เสริม)
- **Sacroiliac joint tenderness** · **FABER test** (Flexion-ABduction-External Rotation ของสะโพก) เป็น **provocation test** ของ SI joint
- **Enthesitis** (Achilles, plantar fascia)
- Extra-articular:
  - **Anterior uveitis** (ตาแดง ปวด สู้แสงไม่ได้ ข้างเดียว เป็นซ้ำ)
  - **Restrictive lung disease** (**chest expansion ลดลง** จากข้อซี่โครงติด) · upper lobe fibrosis
  - **Aortic regurgitation** (สไลด์หน้า 56)

### Investigation (สไลด์หน้า 60–61)
- **ESR, CRP สูง** · RF ลบ
- **X-ray SI joint: sacroiliitis** (ขอบข้อไม่เรียบ **density ที่ SI joint เพิ่มขึ้น** sclerosis) → **ankylosis** (ข้อเชื่อมติดกัน)
- **X-ray spine: bamboo spine** = **syndesmophyte** เชื่อมระหว่าง vertebral body ที่อยู่ติดกัน
- X-ray ยังปกติในระยะแรก → MRI เห็น bone marrow edema ที่ SI joint ได้ก่อน (เสริม)

[[fig:rheum-03-04-f1]]

### การรักษา (สไลด์หน้า 62)
1. **NSAID = 1st line** (ใช้เต็มขนาด) + **กายภาพ/ออกกำลังยืดกระดูกสันหลัง** (เสริม)
2. ไม่ตอบสนองต่อ NSAID อย่างน้อย 2 ตัว → **TNF-α inhibitor** (etanercept, adalimumab)
3. **DMARD** (เช่น sulfasalazine) ช่วยเฉพาะ **peripheral arthritis** ไม่ช่วยอาการ axial (เสริม)

> Systemic steroid ไม่ช่วยอาการ axial ของ AS (เสริม)
''',
    figs=[F_AS],
    pearls=[
        "AS = ชายอายุน้อย + IBP + SI tenderness + chest expansion ↓",
        "FABER test = provocation test ของ SI joint",
        "X-ray: sacroiliitis (SI density ↑) → bamboo spine (syndesmophyte)",
        "Extra-articular: anterior uveitis, restrictive lung, aortic regurgitation",
        "NSAID 1st line → anti-TNF · DMARD ช่วยแค่ข้อปลาย (เสริม)",
    ],
    items=[
        mcq("RHEUM-03-04-1",
            "A 23-year-old man has had low back and buttock pain for 1 year. He has stiffness for over an hour each morning that improves with exercise. Examination shows reduced lumbar flexion, sacroiliac joint tenderness, a positive FABER test bilaterally, and chest expansion of 2 cm. ESR is 45 mm/h. What is the most appropriate investigation to support the diagnosis?",
            "Plain radiograph of the sacroiliac joints",
            ["Rheumatoid factor", "Antinuclear antibody", "Nerve conduction study", "Bone scan for metastasis"],
            explain='''ชายอายุน้อย + **inflammatory back pain + SI tenderness + FABER บวก + chest expansion ลดลง + ESR สูง** = **ankylosing spondylitis** → ยืนยันด้วย **X-ray SI joint หา sacroiliitis** (สไลด์หน้า 60–61)
- RF จะลบใน SpA (seronegative) จึงไม่ช่วยยืนยัน
- ANA ใช้คัดกรอง SLE/CTD
- Nerve conduction ใช้เมื่อสงสัยรากประสาทหรือเส้นประสาทผิดปกติ ซึ่งไม่มีอาการชาหรืออ่อนแรง
- Bone scan หามะเร็งกระจายไม่เหมาะกับชายอายุ 23 ที่มีอาการเรื้อรังแบบ inflammatory 1 ปี''',
            pearl="สงสัย AS → X-ray SI joint", topic="AS investigation",
            ref=[f"{D} หน้า 59–61"], nl=["2.3.13-3(13)", "3.2.5"]),
        mcq("RHEUM-03-04-2",
            "A 30-year-old man with ankylosing spondylitis has a lateral lumbar spine radiograph showing thin vertical bony bridges between adjacent vertebral bodies, giving the spine a smooth, continuous outline. What is the name of this radiographic appearance?",
            "Bamboo spine",
            ["Rugger-jersey spine", "Codfish vertebrae", "Ivory vertebra", "Picture-frame vertebra"],
            explain='''**Syndesmophyte** เชื่อมระหว่าง vertebral body ที่อยู่ติดกันจนดูเป็นปล้องไผ่ = **bamboo spine** ของ AS (สไลด์หน้า 60–61)
- Rugger-jersey spine คือแถบ sclerosis บน-ล่างของ vertebra ใน renal osteodystrophy (secondary hyperparathyroidism)
- Codfish vertebrae คือ vertebra เว้าสองด้านใน osteoporosis หรือ sickle cell
- Ivory vertebra คือ vertebra ทึบทั้งชิ้น เช่น มะเร็งต่อมลูกหมากกระจาย, lymphoma, Paget
- Picture-frame vertebra คือขอบ vertebra หนาใน Paget disease''',
            pearl="Syndesmophyte เชื่อมกัน = bamboo spine = AS", topic="AS X-ray",
            ref=[f"{D} หน้า 60–61"], nl=["2.3.13-3(13)", "3.2.5"]),
        mcq("RHEUM-03-04-3",
            "A 27-year-old man with ankylosing spondylitis has persistent inflammatory back pain and morning stiffness despite regular full-dose naproxen followed by full-dose celecoxib for a total of 3 months. He has no peripheral arthritis. What is the most appropriate next treatment?",
            "TNF-α inhibitor such as adalimumab",
            ["Sulfasalazine", "Long-term oral prednisolone", "Hydroxychloroquine", "Colchicine"],
            explain='''AS ที่ไม่ตอบสนองต่อ NSAID (ใช้แล้ว 2 ตัว เต็มขนาด) → **TNF-α inhibitor** (สไลด์หน้า 62: NSAID 1st line, TNF-α inhibitor, DMARD)
- Sulfasalazine เป็น DMARD ที่ช่วยเฉพาะ peripheral arthritis ไม่ช่วยอาการ axial ซึ่งผู้ป่วยนี้มีแต่ axial (เสริม)
- Prednisolone ระยะยาวไม่ช่วย axial disease และมีผลข้างเคียงมาก
- Hydroxychloroquine ไม่มีบทบาทใน AS
- Colchicine ใช้กับ gout/CPPD''',
            pearl="AS ดื้อ NSAID → anti-TNF (axial ไม่ตอบสนอง DMARD)", topic="AS treatment",
            ref=[f"{D} หน้า 62"], nl=["B5.4(3)", "2.3.13-3(13)"]),
        mcq("RHEUM-03-04-4",
            "A 34-year-old man with known ankylosing spondylitis presents with a painful red left eye, photophobia, and blurred vision for 2 days. There is circumcorneal injection and a small irregular pupil. What is the most likely diagnosis of the eye condition?",
            "Acute anterior uveitis",
            ["Bacterial conjunctivitis", "Acute angle-closure glaucoma", "Episcleritis", "Keratoconjunctivitis sicca"],
            explain='''AS + ตาแดงข้างเดียว ปวด **สู้แสงไม่ได้ ตามัว** + **ciliary (circumcorneal) injection + รูม่านตาเล็ก** = **acute anterior uveitis** ซึ่งเป็น extra-articular ที่พบบ่อยที่สุดของ AS (สไลด์หน้า 55, 59) → ส่งจักษุแพทย์ให้ steroid หยอดตา + cycloplegic (เสริม)
- Bacterial conjunctivitis มีขี้ตาเป็นหนอง ไม่ปวดมาก การมองเห็นปกติ
- Acute angle-closure glaucoma รูม่านตาขยายกลางค้าง ปวดศีรษะ คลื่นไส้ ตาแข็ง
- Episcleritis ไม่ปวดมาก ไม่ตามัว ไม่สู้แสงได้ปกติ
- Keratoconjunctivitis sicca (ตาแห้ง) พบใน RA/Sjögren''',
            pearl="AS + ตาแดง ปวด photophobia รูม่านตาเล็ก = anterior uveitis", topic="AS extra-articular",
            ref=[f"{D} หน้า 55, 59"], nl=["2.3.7-3(8)", "2.3.13-3(13)"]),
    ])

LECTURE = lecture("03", "Seronegative spondyloarthropathies", "inflammatory back pain · reactive arthritis · psoriatic arthritis · ankylosing spondylitis",
    objectives=[
        "แยก inflammatory กับ mechanical back pain",
        "บอกลักษณะร่วมของ SpA (RF ลบ, HLA-B27, enthesitis, dactylitis, oligoarthritis อสมมาตร)",
        "วินิจฉัย reactive arthritis จากประวัติติดเชื้อ GI/GU นำมาก่อน และแยกจาก septic/DGI",
        "จำ PsA จาก DIP + nail pitting + pencil-in-cup",
        "วินิจฉัย AS จาก IBP + SI + X-ray และเลือก NSAID → anti-TNF",
    ],
    sections=[S1, S2, S3, S4])
