from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Rheumato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 01-01 Approach
F_APP = fig("rheum-01-01-f1", "Approach to joint pain: ตำแหน่ง → inflammatory? → จำนวนข้อ", '''<svg viewBox="0 0 730 424">
 <defs><marker id="rheum-01-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="255" y="8" width="220" height="44" rx="10" class="acsoft"/>
 <text x="365" y="28" text-anchor="middle" class="tb">ปวดข้อ / ข้อบวม</text>
 <text x="365" y="45" text-anchor="middle" class="t3">หาตำแหน่งที่เจ็บจริงก่อน</text>
 <path d="M300 52L150 90" class="ln" marker-end="url(#rheum-01-01-a)"/>
 <path d="M430 52L500 90" class="ln" marker-end="url(#rheum-01-01-a)"/>
 <rect x="10" y="92" width="240" height="78" rx="10" class="box"/>
 <text x="22" y="114" class="tb">Periarticular</text>
 <text x="22" y="134" class="t3">เจ็บจุดเดียว (focal)</text>
 <text x="22" y="150" class="t3">เจ็บเฉพาะ active ROM บางทิศ</text>
 <text x="22" y="166" class="t3">bursitis · tendinitis · enthesitis</text>
 <rect x="280" y="92" width="440" height="78" rx="10" class="box"/>
 <text x="292" y="114" class="tb">Articular: เจ็บทั่ว joint line ทั้ง active และ passive</text>
 <text x="292" y="138" class="ta">Inflammatory หรือไม่?</text>
 <text x="292" y="158" class="t3">AM stiffness &gt; 30 นาที · บวม แดง ร้อน · ↑ESR/CRP</text>
 <path d="M300 170L95 208" class="ln" marker-end="url(#rheum-01-01-a)"/>
 <path d="M420 170L275 208" class="ln" marker-end="url(#rheum-01-01-a)"/>
 <path d="M560 170L455 208" class="ln" marker-end="url(#rheum-01-01-a)"/>
 <path d="M680 170L635 208" class="ln" marker-end="url(#rheum-01-01-a)"/>
 <rect x="10" y="210" width="170" height="44" rx="10" class="ok"/>
 <text x="95" y="230" text-anchor="middle" class="tw">Non-inflammatory</text>
 <text x="95" y="246" text-anchor="middle" class="tw">(mechanical)</text>
 <rect x="190" y="210" width="170" height="44" rx="10" class="bad"/>
 <text x="275" y="230" text-anchor="middle" class="tw">Monoarthritis</text>
 <text x="275" y="246" text-anchor="middle" class="tw">1 ข้อ</text>
 <rect x="370" y="210" width="170" height="44" rx="10" class="miss"/>
 <text x="455" y="230" text-anchor="middle" class="tw">Oligoarthritis</text>
 <text x="455" y="246" text-anchor="middle" class="tw">2–4 ข้อ</text>
 <rect x="550" y="210" width="170" height="44" rx="10" class="c1"/>
 <text x="635" y="230" text-anchor="middle" class="tw">Polyarthritis</text>
 <text x="635" y="246" text-anchor="middle" class="tw">≥ 5 ข้อ</text>
 <rect x="10" y="262" width="170" height="150" rx="10" class="oksoft"/>
 <text x="20" y="284" class="tb">Osteoarthritis</text>
 <text x="20" y="304" class="t3">เข่า, DIP, varus</text>
 <text x="20" y="322" class="t3">AM stiffness &lt; 30 นาที</text>
 <text x="20" y="340" class="t3">ปวดเมื่อใช้ พักแล้วดีขึ้น</text>
 <text x="20" y="364" class="t2">Trauma, ligament</text>
 <text x="20" y="384" class="t3">SF WBC &lt; 2,000</text>
 <rect x="190" y="262" width="170" height="150" rx="10" class="badsoft"/>
 <text x="200" y="284" class="tb">Septic arthritis !!</text>
 <text x="200" y="304" class="t2">Gout (1st MTP)</text>
 <text x="200" y="322" class="t2">CPPD (เข่า ข้อมือ)</text>
 <text x="200" y="340" class="t2">Hemarthrosis</text>
 <text x="200" y="370" class="ta">→ Arthrocentesis</text>
 <text x="200" y="388" class="t3">ทุกรายที่ทำได้</text>
 <rect x="370" y="262" width="170" height="150" rx="10" class="misssoft"/>
 <text x="380" y="284" class="tb">Seronegative SpA</text>
 <text x="380" y="304" class="t2">Reactive arthritis</text>
 <text x="380" y="322" class="t2">Psoriatic arthritis</text>
 <text x="380" y="340" class="t2">AS (ข้อใหญ่ขา)</text>
 <text x="380" y="364" class="t2">DGI (migratory)</text>
 <text x="380" y="384" class="t3">อสมมาตร ขาเด่น</text>
 <rect x="550" y="262" width="170" height="150" rx="10" class="c1soft"/>
 <text x="560" y="284" class="tb">RA</text>
 <text x="560" y="302" class="t3">สมมาตร MCP PIP wrist</text>
 <text x="560" y="326" class="tb">SLE</text>
 <text x="560" y="344" class="t3">ไม่มี deformity/erosion</text>
 <text x="560" y="368" class="t2">Viral arthritis</text>
 <text x="560" y="388" class="t2">PsA แบบ poly</text>
</svg>''', "อ่านจากบนลงล่าง: แยก periarticular ออกก่อน จากนั้นดูว่า inflammatory หรือไม่ แล้วนับจำนวนข้อเพื่อจำกัดโรคที่เป็นไปได้ · monoarthritis เฉียบพลันต้องเจาะข้อแยก septic ทุกราย")

F_SF = fig("rheum-01-01-f2", "Synovial fluid analysis เป็นสเปกตรัมของ WBC", '''<svg viewBox="0 0 720 300">
 <text x="400" y="22" text-anchor="middle" class="tb">WBC ในน้ำไขข้อ (cells/µL) — มากขึ้นจากซ้ายไปขวา</text>
 <rect x="90" y="36" width="100" height="40" rx="6" class="oksoft"/>
 <text x="140" y="61" text-anchor="middle" class="tb">Normal</text>
 <rect x="190" y="36" width="150" height="40" rx="6" class="c1soft"/>
 <text x="265" y="61" text-anchor="middle" class="tb">Non-inflammatory</text>
 <rect x="340" y="36" width="180" height="40" rx="6" class="misssoft"/>
 <text x="430" y="61" text-anchor="middle" class="tb">Inflammatory</text>
 <rect x="520" y="36" width="190" height="40" rx="6" class="badsoft"/>
 <text x="615" y="61" text-anchor="middle" class="tb">Septic</text>
 <text x="190" y="96" text-anchor="middle" class="ta">200</text>
 <text x="340" y="96" text-anchor="middle" class="ta">2,000</text>
 <text x="520" y="96" text-anchor="middle" class="ta">50,000</text>
 <path d="M10 106H710" class="lnf"/>
 <text x="10" y="128" class="tb">PMN</text>
 <text x="140" y="128" text-anchor="middle">&lt; 25%</text>
 <text x="265" y="128" text-anchor="middle">&lt; 25%</text>
 <text x="430" y="128" text-anchor="middle">&gt; 50%</text>
 <text x="615" y="128" text-anchor="middle">&gt; 90%</text>
 <text x="10" y="154" class="tb">ลักษณะ</text>
 <text x="140" y="154" text-anchor="middle">ใส ไม่มีสี</text>
 <text x="265" y="154" text-anchor="middle">ใส สีเหลือง</text>
 <text x="430" y="154" text-anchor="middle">ขุ่น สีเหลือง</text>
 <text x="615" y="154" text-anchor="middle">ขุ่น สีเหลือง</text>
 <text x="10" y="180" class="tb">Crystal</text>
 <text x="140" y="180" text-anchor="middle" class="t3">ไม่มี</text>
 <text x="265" y="180" text-anchor="middle" class="t3">ไม่มี</text>
 <text x="430" y="180" text-anchor="middle" class="ta">พบได้</text>
 <text x="615" y="180" text-anchor="middle" class="t3">ไม่มี</text>
 <text x="10" y="206" class="tb">C/S</text>
 <text x="140" y="206" text-anchor="middle" class="t3">negative</text>
 <text x="265" y="206" text-anchor="middle" class="t3">negative</text>
 <text x="430" y="206" text-anchor="middle" class="t3">negative</text>
 <text x="615" y="206" text-anchor="middle" class="ta">positive</text>
 <text x="10" y="232" class="tb">พบใน</text>
 <text x="265" y="232" text-anchor="middle" class="t2">OA, trauma,</text>
 <text x="265" y="250" text-anchor="middle" class="t2">viral, drug-induced</text>
 <text x="430" y="232" text-anchor="middle" class="t2">Gout, CPPD, RA,</text>
 <text x="430" y="250" text-anchor="middle" class="t2">SLE, SpA</text>
 <text x="615" y="232" text-anchor="middle" class="t2">Bacterial</text>
 <text x="615" y="250" text-anchor="middle" class="t2">(glucose ↓)</text>
 <rect x="90" y="262" width="620" height="32" rx="6" class="sunk"/>
 <text x="400" y="283" text-anchor="middle" class="t2">Trauma: น้ำสีแดง (bloody) ขุ่น → fracture, ligament injury, hemophilia</text>
</svg>''', "จำเลขตัดสามตัว 200 · 2,000 · 50,000 และ PMN 25 · 50 · 90 · crystal พบเฉพาะกลุ่ม inflammatory · culture บวกเฉพาะ septic")

S1 = sec("rheum-01-01", "Approach to arthritis & synovial fluid analysis",
    "แยก articular/periarticular → inflammatory/mechanical → mono/oligo/poly · SF WBC <200 ปกติ · <2,000 non-inflam · 2,000–50,000 inflam · >50,000 septic", minutes=7,
    source=f"{D} หน้า 4–5 (ซ้ำหน้า 80, 108)", nl=["2.1.27", "B5.3(3)", "3.1.7"],
    md='''
### ขั้นที่ 1: Articular หรือ Periarticular (สไลด์หน้า 4)

| | Articular | Periarticular |
|---|---|---|
| ตำแหน่งที่เจ็บ | ตาม **joint line**, กระจายทั่วข้อ | **เฉพาะจุด (focal)** |
| Sign of inflammation (บวม แดง ร้อน) | กระจายทั่วข้อ | เฉพาะจุด |
| Pain on movement | เจ็บทั้ง **active และ passive** ROM | เจ็บเมื่อ **active ROM บางทิศทาง** |
| ตัวอย่าง (เสริม) | arthritis ทุกชนิด | bursitis, tendinitis, enthesitis |

> passive ROM ไม่เจ็บแต่ active บางทิศเจ็บ = ปัญหาที่เส้นเอ็น/ถุงน้ำรอบข้อ ไม่ใช่ข้อ

### ขั้นที่ 2: Inflammatory หรือ Non-inflammatory (เสริม — ใช้หลักเดียวกับ back pain หน้า 52)
- **Inflammatory**: morning stiffness **> 30 นาที** ดีขึ้นเมื่อขยับ · บวม แดง ร้อน · มีอาการทั่วตัว · ESR/CRP สูง
- **Non-inflammatory (mechanical)**: stiffness **< 30 นาที** · ปวดมากขึ้นเมื่อใช้งาน ดีขึ้นเมื่อพัก · ตัวแทนคือ **OA**

### ขั้นที่ 3: นับจำนวนข้อ + เฉียบพลันหรือเรื้อรัง (เสริม)
- **Monoarthritis เฉียบพลัน** → septic arthritis, gout, CPPD, hemarthrosis → **ต้องเจาะข้อ (arthrocentesis)**
- **Oligoarthritis (2–4 ข้อ)** อสมมาตร ขาเด่น → seronegative SpA (reactive, psoriatic), DGI
- **Polyarthritis (≥ 5 ข้อ)** สมมาตร → RA, SLE, viral arthritis

[[fig:rheum-01-01-f1]]

### Synovial fluid analysis (สไลด์หน้า 5)

| | Normal | Non-inflammatory | Inflammatory | Septic | Trauma |
|---|---|---|---|---|---|
| Clarity | transparent | transparent | cloudy | cloudy | cloudy |
| Color | clear | yellow | yellow | yellow | **red** |
| WBC (/µL) | **< 200** | **< 2,000** | **2,000–50,000** | **> 50,000** | — |
| PMN | < 25% | < 25% | **> 50%** | **> 90%** | — |
| C/S | negative | negative | negative | **positive** | negative |
| Crystal | ไม่มี | ไม่มี | **มีได้** | ไม่มี | ไม่มี |
| พบใน | — | OA, trauma, viral infection, drug-induced | crystal-induced arthritis, RA, SLE, SpA | bacterial | fracture, ligament injury, hemophilia |

[[fig:rheum-01-01-f2]]

> ตัวเลขเป็นแนวทาง ไม่ใช่เส้นแบ่งเด็ดขาด — gout รุนแรงอาจ WBC > 50,000 ได้ และ septic ระยะแรกอาจต่ำกว่า 50,000 (เสริม) → **ส่ง Gram stain, culture และหา crystal ทุกครั้ง**
> น้ำไขข้อ septic มัก **glucose ต่ำ** (สไลด์หน้า 107)
''',
    figs=[F_APP, F_SF],
    pearls=[
        "Periarticular = focal + เจ็บเฉพาะ active ROM บางทิศ · articular = ทั้งข้อ ทั้ง active และ passive",
        "Inflammatory = AM stiffness > 30 นาที ดีขึ้นเมื่อขยับ · mechanical < 30 นาที แย่ลงเมื่อใช้",
        "SF WBC: < 200 ปกติ · < 2,000 non-inflam · 2,000–50,000 inflam · > 50,000 septic (PMN > 90%)",
        "Crystal พบในกลุ่ม inflammatory · culture บวกเฉพาะ septic · น้ำสีแดง = trauma/hemophilia",
        "Acute monoarthritis → arthrocentesis เสมอเพื่อ R/O septic arthritis",
    ],
    items=[
        mcq("RHEUM-01-01-1",
            "A 64-year-old woman has had bilateral knee pain for 3 years that worsens with walking and improves with rest. Morning stiffness lasts 10 minutes. Aspiration of the right knee effusion shows clear yellow fluid, WBC 800/µL, PMN 15%, no crystals, Gram stain negative. How should this synovial fluid be classified?",
            "Non-inflammatory",
            ["Normal", "Inflammatory", "Septic", "Hemorrhagic"],
            explain='''น้ำใส สีเหลือง **WBC < 2,000 และ PMN < 25%** = **non-inflammatory** ตรงกับ OA ซึ่งเข้ากับประวัติปวดตอนใช้งานและ stiffness สั้น
- Normal ต้อง WBC < 200 และไม่มีสี — ค่านี้สูงกว่า
- Inflammatory ต้อง WBC 2,000–50,000 และ PMN > 50% น้ำขุ่น
- Septic ต้อง WBC > 50,000 PMN > 90% และ culture/Gram stain บวก
- Hemorrhagic (trauma) น้ำจะเป็นสีแดง''',
            pearl="WBC < 2,000 PMN < 25% = non-inflammatory (OA, trauma, viral)", topic="Synovial fluid",
            ref=[f"{D} หน้า 5"], nl=["B5.3(3)", "2.3.13(5)"]),
        mcq("RHEUM-01-01-2",
            "A 52-year-old woman complains of right lateral hip pain for 1 month, worse when lying on the right side. There is point tenderness over the greater trochanter. Passive hip rotation is full and painless, but active hip abduction reproduces the pain. What is the most likely diagnosis?",
            "Greater trochanteric bursitis",
            ["Osteoarthritis of the hip", "Septic arthritis of the hip", "Avascular necrosis of the femoral head", "Acute gouty arthritis of the hip"],
            explain='''เจ็บ **เฉพาะจุด** ที่ greater trochanter และเจ็บเฉพาะ **active ROM บางทิศ** ส่วน passive ROM ไม่เจ็บ = ปัญหา **periarticular** → trochanteric bursitis (ส่วนวินิจฉัยโรคเป็นเนื้อหาเสริม)
- Hip OA เป็นโรคของข้อ จะเจ็บที่ขาหนีบและเจ็บเมื่อหมุนสะโพกแบบ passive โดยเฉพาะ internal rotation
- Septic arthritis ของสะโพก ขยับข้อแบบ passive ไม่ได้เลยเพราะเจ็บมาก และมักมีไข้
- Avascular necrosis เป็นพยาธิสภาพในข้อ เจ็บขาหนีบและ passive ROM ลดลง
- Gout ไม่ค่อยเป็นที่สะโพก และถ้าเป็นจะเจ็บทั้งข้อ''',
            pearl="Passive ROM ไม่เจ็บ + เจ็บจุดเดียว = periarticular", topic="Articular vs periarticular",
            ref=[f"{D} หน้า 4"], nl=["2.1.27"]),
        mcq("RHEUM-01-01-3",
            "A 58-year-old man with diabetes presents with a hot, swollen left knee for 2 days and fever of 38.8°C. Arthrocentesis yields cloudy yellow fluid, WBC 120,000/µL with 95% PMN, and low glucose. What is the most likely diagnosis?",
            "Septic arthritis",
            ["Acute gouty arthritis", "Rheumatoid arthritis flare", "Osteoarthritis with effusion", "Traumatic hemarthrosis"],
            explain='''WBC **> 50,000** และ **PMN > 90%** ร่วมกับ glucose ต่ำในน้ำไขข้อ = **septic arthritis** (เบาหวานเป็นปัจจัยเสี่ยง) → ส่ง Gram stain/culture และเริ่มยาฆ่าเชื้อกับระบายหนอง
- Gout มักอยู่ในช่วง inflammatory (2,000–50,000) และต้องพบผลึกรูปเข็ม — ถ้ายังไม่ได้เห็นผลึก ต้องถือว่าเป็น septic ไว้ก่อน
- RA flare เป็นหลายข้อ และน้ำไขข้อเป็นกลุ่ม inflammatory
- OA น้ำไขข้อเป็น non-inflammatory (< 2,000)
- Hemarthrosis น้ำจะเป็นสีแดง และต้องมีประวัติอุบัติเหตุหรือเลือดออกง่าย''',
            pearl="SF WBC > 50,000 + PMN > 90% + glucose ต่ำ = septic", topic="Synovial fluid",
            ref=[f"{D} หน้า 5, 107"], nl=["B5.3(3)", "2.3.13-3(6)"]),
        mcq("RHEUM-01-01-4",
            "A 19-year-old man twisted his right knee while playing football and the knee became markedly swollen within 2 hours. He is afebrile. Arthrocentesis yields frankly bloody fluid. What is the most likely underlying cause?",
            "Intra-articular ligament injury such as an anterior cruciate ligament tear",
            ["Septic arthritis", "Reactive arthritis", "Acute gouty arthritis", "Osteoarthritis"],
            explain='''น้ำไขข้อ **สีแดง** = กลุ่ม **trauma** ตามตารางในสไลด์ (fracture, ligament injury, hemophilia) · ข้อบวมเร็วภายในไม่กี่ชั่วโมงหลังบิดเข่า มักเป็น ACL tear หรือกระดูกในข้อหัก (เสริม)
- Septic arthritis มีไข้ เป็นหลายวัน และน้ำขุ่นสีเหลือง ไม่ใช่เลือด
- Reactive arthritis เกิด 1–4 สัปดาห์หลังติดเชื้อทางเดินอาหารหรือทางเดินปัสสาวะ และน้ำเป็นกลุ่ม inflammatory
- Gout พบในชายวัยกลางคน น้ำขุ่นเหลืองและพบผลึก
- OA เป็นเรื้อรัง ข้อไม่บวมทันทีหลังบาดเจ็บ''',
            pearl="น้ำเจาะข้อเป็นเลือด = fracture, ligament injury, hemophilia", topic="Hemarthrosis",
            ref=[f"{D} หน้า 5"], nl=["B5.3(3)", "2.3.18-3(9)"]),
    ])

# ---------------------------------------------------------------- 01-02 SLE clinical
S2 = sec("rheum-01-02", "SLE: อาการและเกณฑ์ EULAR/ACR 2019",
    "หญิงวัยเจริญพันธุ์ · multi-organ · malar rash เว้น nasolabial fold · arthritis ไม่มี deformity · entry ANA ≥ 1:80 + ≥ 10 คะแนน", minutes=9,
    source=f"{D} หน้า 7–10, 18–21", nl=["2.3.13-3(15)", "B5.2.2-3(5)", "2.3.12-3(4)"],
    md='''
### นิยามและใครเป็น (สไลด์หน้า 7)
- **Systemic autoimmune disease** พบบ่อยใน **หญิงวัยเจริญพันธุ์**
- กลไก (เสริม): สูญเสีย self-tolerance ต่อ nuclear antigen → autoantibody + **immune complex** ไปตกตะกอนที่ไต ผิวหนัง ข้อ หลอดเลือด → กระตุ้น complement (ใช้ไปจน **C3, C4 ต่ำ**) = type III hypersensitivity
- ตัวกระตุ้น: **smoking, UV light, EBV infection, ยา (hydralazine, isoniazid, procainamide)**

### อาการหลายระบบ (สไลด์หน้า 8–9)

| ระบบ | อาการ |
|---|---|
| Constitutional | ไข้ อ่อนเพลีย น้ำหนักลด |
| ข้อ | arthritis/arthralgia **มักไม่มี deformity** (non-erosive) |
| ผิวหนัง | **malar rash**, **discoid rash**, **oral ulcer**, **non-scarring alopecia** |
| เลือด | petechiae, **WBC ต่ำ, platelet ต่ำ**, AIHA (Coombs บวก, spherocyte) |
| Serositis | pleuritis, pericarditis |
| ไต | **lupus nephritis** (proteinuria, hematuria, RBC cast) |
| ประสาท | delirium, seizure, psychosis |

- **Malar rash**: erythematous patch/plaque บนโหนกแก้มทั้งสองข้าง **เว้น nasolabial fold** (butterfly)
- **Discoid rash**: erythematous **scaly plaque** หายแล้วเป็นแผลเป็น/สีผิวเปลี่ยน (เสริม)

> โจทย์แนว NL: **หญิงอายุน้อย + ข้ออักเสบ + cytopenia (Hct ต่ำ WBC ต่ำ Plt ต่ำ) + proteinuria/hematuria** = SLE จนกว่าจะพิสูจน์ได้ว่าไม่ใช่

### EULAR/ACR 2019 classification criteria (สไลด์หน้า 10)
- **Entry criterion: ANA ≥ 1:80** (HEp-2) เคยบวกอย่างน้อยหนึ่งครั้ง — ถ้าไม่มี **ไม่ classify เป็น SLE**
- จัดเป็น SLE เมื่อ **≥ 10 คะแนน** และมี **clinical criterion ≥ 1 ข้อ** · แต่ละ domain นับเฉพาะข้อที่คะแนนสูงสุด · ไม่ต้องเกิดพร้อมกัน · ไม่นับข้อที่มีสาเหตุอื่นอธิบายได้ดีกว่า

| Clinical domain | เกณฑ์ (คะแนน) |
|---|---|
| Constitutional | fever (2) |
| Hematologic | leukopenia (3) · thrombocytopenia (4) · autoimmune hemolysis (4) |
| Neuropsychiatric | delirium (2) · psychosis (3) · seizure (5) |
| Mucocutaneous | non-scarring alopecia (2) · oral ulcer (2) · subacute cutaneous หรือ discoid lupus (4) · acute cutaneous lupus (6) |
| Serosal | pleural/pericardial effusion (5) · acute pericarditis (6) |
| Musculoskeletal | joint involvement (6) |
| Renal | proteinuria > 0.5 g/24 h (4) · biopsy class II หรือ V (8) · **class III หรือ IV (10)** |

| Immunology domain | เกณฑ์ (คะแนน) |
|---|---|
| Antiphospholipid Ab | anticardiolipin หรือ anti-β2GP1 หรือ lupus anticoagulant (2) |
| Complement | C3 **หรือ** C4 ต่ำ (3) · C3 **และ** C4 ต่ำ (4) |
| SLE-specific Ab | **anti-dsDNA หรือ anti-Smith (6)** |

> ANA บวก + biopsy LN class III/IV อย่างเดียวก็ได้ 10 คะแนน = SLE
''',
    pearls=[
        "SLE = หญิงวัยเจริญพันธุ์ · ตัวกระตุ้น smoking, UV, EBV, hydralazine/INH/procainamide",
        "Malar rash เว้น nasolabial fold · arthritis ของ SLE ไม่มี deformity/erosion",
        "ข้ออักเสบ + cytopenia + proteinuria ในหญิงอายุน้อย = คิดถึง SLE ก่อน",
        "EULAR/ACR 2019: entry ANA ≥ 1:80 แล้วต้อง ≥ 10 คะแนน + clinical ≥ 1",
        "คะแนนสูงสุด: LN class III/IV (10) · anti-dsDNA/Sm, joint, ACLE, pericarditis (6)",
    ],
    items=[
        mcq("RHEUM-01-02-1",
            "A 50-year-old woman presents with fatigue, joint pain, and 2-kg weight loss over 2 months. Examination shows moderate pallor, arthritis of both PIP joints, periungual erythema, and mild proximal weakness of both legs. CBC: Hct 22%, WBC 3,600/mm3 (N 70%, L 30%), platelets 90,000/mm3. Urinalysis: albumin 3+. What is the most likely diagnosis?",
            "Systemic lupus erythematosus",
            ["Inflammatory myositis", "Reactive arthritis", "Systemic sclerosis", "Rheumatoid arthritis"],
            kind="old", src=OLD,
            explain='''มีหลายระบบพร้อมกัน: **arthritis + ซีด + WBC ต่ำ + platelet ต่ำ (pancytopenia) + proteinuria** = **SLE** (periungual erythema และกล้ามเนื้ออ่อนแรงเล็กน้อยพบใน SLE ได้)
- Myositis เด่นที่กล้ามเนื้อต้นแขนต้นขาอ่อนแรงและ CK สูง ไม่อธิบาย cytopenia และ proteinuria
- Reactive arthritis เป็น oligoarthritis ที่ขาหลังติดเชื้อ ไม่มี cytopenia
- Systemic sclerosis ต้องมีผิวหนังหนาตึง Raynaud และ sclerodactyly
- RA ไม่ทำให้ pancytopenia และ proteinuria (ยกเว้น Felty syndrome หรือ amyloidosis ซึ่งไม่เข้ากับภาพนี้)''',
            pearl="Arthritis + cytopenia + proteinuria = SLE", topic="SLE diagnosis",
            ref=[f"{D} หน้า 18–19"], nl=["2.3.13-3(15)"]),
        mcq("RHEUM-01-02-2",
            "A 65-year-old woman presents with joint pain for 2 weeks. Examination shows arthritis of all PIP and MCP joints bilaterally. CBC: Hct 28%, WBC 3,500/mm3 (N 70%, L 30%), platelets 130,000/mm3. Peripheral smear shows microspherocytes. Urinalysis: albumin 2+, WBC 0–1/HPF, RBC 10–20/HPF. What is the most likely diagnosis?",
            "Systemic lupus erythematosus",
            ["Rheumatoid arthritis", "Reactive arthritis", "Autoimmune hemolytic anemia", "Disseminated gonococcal infection"],
            kind="old", src=OLD,
            explain='''Polyarthritis สมมาตร + **AIHA (microspherocyte)** + leukopenia + thrombocytopenia เล็กน้อย + **glomerular hematuria/proteinuria** = **SLE** แม้อายุมากก็เป็นได้
- RA มี polyarthritis ที่ MCP/PIP เหมือนกัน แต่ไม่อธิบาย AIHA, cytopenia และ nephritis
- Reactive arthritis เป็นข้อใหญ่ที่ขา หลังติดเชื้อ
- AIHA อธิบายได้แค่ภาวะซีด ไม่อธิบาย arthritis และไตอักเสบ — ในเคสนี้ AIHA เป็น **อาการหนึ่งของ SLE**
- DGI ต้องมีไข้ tenosynovitis และตุ่มหนองที่ผิว ในคนที่มีเพศสัมพันธ์''',
            pearl="AIHA + arthritis + nephritis = SLE ไม่ใช่ AIHA เดี่ยว", topic="SLE diagnosis",
            ref=[f"{D} หน้า 20–21"], nl=["2.3.13-3(15)", "2.3.3(4)"]),
        mcq("RHEUM-01-02-3",
            "A 24-year-old woman has a photosensitive malar rash, oral ulcers, and arthritis of both wrists. Before applying the 2019 EULAR/ACR classification criteria for SLE, which finding must be present?",
            "Antinuclear antibody titer of at least 1:80",
            ["Positive anti-dsDNA antibody", "Positive anti-Smith antibody", "Low C3 and C4", "Proteinuria more than 0.5 g/24 h"],
            explain='''เกณฑ์ EULAR/ACR 2019 มี **entry criterion = ANA ≥ 1:80** (เคยบวกครั้งใดก็ได้) ถ้าไม่มี ไม่ classify เป็น SLE · มี entry แล้วจึงรวมคะแนนให้ได้ ≥ 10
- Anti-dsDNA และ anti-Sm เป็น additive criteria (6 คะแนน) ไม่ใช่ entry
- C3/C4 ต่ำเป็น additive (3–4 คะแนน)
- Proteinuria > 0.5 g/24 h เป็น renal criterion 4 คะแนน''',
            pearl="EULAR/ACR 2019: ไม่มี ANA ≥ 1:80 = ไม่ classify SLE", topic="EULAR/ACR 2019",
            ref=[f"{D} หน้า 10, 23"], nl=["2.3.13-3(15)", "B5.3(5)"]),
        mcq("RHEUM-01-02-4",
            "A 30-year-old woman with SLE has had intermittent arthritis of both hands for 3 years. Examination shows mild tenderness of MCP and PIP joints without fixed deformity. Which plain radiograph finding of the hands is most expected?",
            "Normal joint spaces without erosions",
            ["Marginal erosions with periarticular osteopenia", "Pencil-in-cup deformity of DIP joints", "Punched-out lesions with overhanging edges", "Chondrocalcinosis of the triangular cartilage"],
            explain='''Arthritis ของ SLE **ไม่มี deformity และไม่มี erosion** (สไลด์หน้า 8) → ภาพรังสีมักปกติ · ถ้ามีข้อผิดรูปจะเป็นแบบดัดกลับได้ (Jaccoud arthropathy — เสริม)
- Marginal erosion กับ periarticular osteopenia เป็นลักษณะของ RA
- Pencil-in-cup ที่ DIP เป็นลักษณะของ psoriatic arthritis
- Punched-out lesion ที่ขอบยื่น (overhanging edge) เป็นลักษณะของ chronic gout
- Chondrocalcinosis เป็นลักษณะของ CPPD''',
            pearl="SLE arthritis = non-erosive, ไม่มี deformity", topic="SLE arthritis",
            ref=[f"{D} หน้า 8"], nl=["2.3.13-3(15)", "3.2.5"]),
    ])

# ---------------------------------------------------------------- 01-03 SLE Ab
F_AB = fig("rheum-01-03-f1", "Autoantibody ↔ โรค: ตัวไหนไว ตัวไหนจำเพาะ", '''<svg viewBox="0 0 740 470">
 <defs><marker id="rheum-01-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <text x="370" y="20" text-anchor="middle" class="tb">SLE: จากตรวจคัดกรอง → ยืนยัน</text>
 <path d="M30 34H710" class="lna" marker-end="url(#rheum-01-03-a)"/>
 <text x="30" y="52" class="t3">sensitivity สูง</text>
 <text x="710" y="52" text-anchor="end" class="t3">specificity สูง</text>
 <rect x="30" y="60" width="200" height="44" rx="10" class="c1"/>
 <text x="130" y="80" text-anchor="middle" class="tw">ANA ≥ 1:80</text>
 <text x="130" y="96" text-anchor="middle" class="tw">คัดกรอง / entry</text>
 <rect x="270" y="60" width="200" height="44" rx="10" class="ac"/>
 <text x="370" y="80" text-anchor="middle" class="tw">Anti-dsDNA</text>
 <text x="370" y="96" text-anchor="middle" class="tw">จำเพาะ + ดู activity</text>
 <rect x="510" y="60" width="200" height="44" rx="10" class="c2"/>
 <text x="610" y="80" text-anchor="middle" class="tw">Anti-Sm</text>
 <text x="610" y="96" text-anchor="middle" class="tw">จำเพาะสุด sens ต่ำ</text>
 <rect x="10" y="118" width="172" height="160" rx="10" class="acsoft"/>
 <text x="20" y="140" class="tb">SLE</text>
 <text x="20" y="162" class="t3">ANA ≥ 1:80 = entry</text>
 <text x="20" y="180" class="t3">anti-dsDNA: LN, flare</text>
 <text x="20" y="198" class="t3">anti-Sm: จำเพาะสุด</text>
 <text x="20" y="216" class="t3">C3 ↓ C4 ↓: activity</text>
 <text x="20" y="234" class="t3">aPL: ร่วมกับ APS</text>
 <text x="20" y="256" class="ta">activity = dsDNA + C3/C4</text>
 <rect x="190" y="118" width="172" height="160" rx="10" class="misssoft"/>
 <text x="200" y="140" class="tb">Drug-induced lupus</text>
 <text x="200" y="162" class="t3">Antihistone (+ ANA)</text>
 <text x="200" y="180" class="t3">dsDNA มักลบ (เสริม)</text>
 <text x="200" y="198" class="t3">ไตและสมองไม่ค่อยเป็น</text>
 <text x="200" y="222" class="t2">Hydralazine, INH,</text>
 <text x="200" y="240" class="t2">procainamide</text>
 <rect x="370" y="118" width="172" height="160" rx="10" class="c2soft"/>
 <text x="380" y="140" class="tb">APS</text>
 <text x="380" y="162" class="t3">Lupus anticoagulant</text>
 <text x="380" y="180" class="t3">Anticardiolipin</text>
 <text x="380" y="198" class="t3">Anti-β2-glycoprotein I</text>
 <text x="380" y="222" class="t2">aPTT ยาว แต่เกิด</text>
 <text x="380" y="240" class="t2">ลิ่มเลือด ไม่ใช่เลือดออก</text>
 <rect x="550" y="118" width="180" height="160" rx="10" class="c1soft"/>
 <text x="560" y="140" class="tb">RA</text>
 <text x="560" y="162" class="t3">RF: sensitive ไม่จำเพาะ</text>
 <text x="560" y="180" class="t3">Anti-CCP: จำเพาะ</text>
 <text x="560" y="198" class="t3">บวกทั้งคู่ = erosive</text>
 <text x="560" y="216" class="t3">มากกว่า (เสริม)</text>
 <text x="560" y="240" class="t2">ESR, CRP ↑</text>
 <rect x="10" y="292" width="172" height="166" rx="10" class="box"/>
 <text x="20" y="314" class="tb">Seronegative SpA</text>
 <text x="20" y="336" class="t3">RF ลบ</text>
 <text x="20" y="354" class="t3">สัมพันธ์ HLA-B27</text>
 <text x="20" y="372" class="t3">ไม่มี autoantibody</text>
 <text x="20" y="390" class="t3">เฉพาะ</text>
 <text x="20" y="414" class="t2">AS, ReA, PsA, IBD</text>
 <rect x="190" y="292" width="172" height="166" rx="10" class="box"/>
 <text x="200" y="314" class="tb">IIM (DM/PM)</text>
 <text x="200" y="336" class="t3">ANA ±</text>
 <text x="200" y="354" class="t3">Myositis-specific Ab</text>
 <text x="200" y="372" class="t3">anti-Jo-1 → ILD (เสริม)</text>
 <text x="200" y="396" class="t2">ยืนยันด้วย</text>
 <text x="200" y="414" class="t2">muscle biopsy</text>
 <rect x="370" y="292" width="172" height="166" rx="10" class="badsoft"/>
 <text x="380" y="314" class="tb">ANCA vasculitis</text>
 <text x="380" y="336" class="t3">c-ANCA (PR3): GPA</text>
 <text x="380" y="354" class="t3">p-ANCA (MPO): MPA,</text>
 <text x="380" y="372" class="t3">EGPA</text>
 <text x="380" y="396" class="t2">(เสริม — ไม่มีในสไลด์)</text>
 <rect x="550" y="292" width="180" height="166" rx="10" class="oksoft"/>
 <text x="560" y="314" class="tb">IgA vasculitis (HSP)</text>
 <text x="560" y="336" class="t3">ไม่มี Ab เฉพาะ</text>
 <text x="560" y="354" class="t3">ANCA ลบ</text>
 <text x="560" y="372" class="t3">Plt, coag ปกติ</text>
 <text x="560" y="396" class="t2">วินิจฉัยทางคลินิก</text>
 <text x="560" y="414" class="t2">+ UA ดูไต</text>
</svg>''', "แถบบนคือการไล่ตรวจใน SLE (ANA ไวที่สุด anti-Sm จำเพาะที่สุด) · การ์ดด้านล่างจับคู่ antibody กับโรคที่ข้อสอบชอบถาม")

S3 = sec("rheum-01-03", "SLE: Autoantibody, complement และ disease activity",
    "ANA ≥ 1:80 ไวแต่ไม่จำเพาะ · anti-dsDNA/anti-Sm จำเพาะ · activity ดูด้วย anti-dsDNA + C3/C4 · antihistone = drug-induced", minutes=7,
    source=f"{D} หน้า 11–12, 22–27", nl=["B5.3(5)", "2.3.13-3(15)", "B5.2.2-3(5)"],
    md='''
### Autoantibody ใน SLE (สไลด์หน้า 11–12)

| Antibody | Sensitivity | Specificity | ใช้ทำอะไร |
|---|---|---|---|
| **ANA** (บวกเมื่อ titer **≥ 1:80**) | **สูง** | ต่ำ | คัดกรอง · entry criterion · ถ้าลบแทบตัด SLE ได้ |
| **Anti-dsDNA** | ต่ำ | **สูง** | ยืนยันโรค · **สูงขึ้นช่วง flare** · สัมพันธ์กับ lupus nephritis |
| **Anti-Smith (Sm)** | ต่ำ | **สูง** | ยืนยันโรค (ไม่เปลี่ยนตาม activity — เสริม) |
| **Antiphospholipid Ab** (anticardiolipin, anti-β2-glycoprotein, lupus anticoagulant) | — | — | หา APS ร่วม |
| **Antihistone** | — | — | **drug-induced SLE** |

### Complement
- **C3, C4 ต่ำช่วง flare** เพราะถูกใช้ไปกับ immune complex

### ตัวที่ใช้ติดตาม disease activity
1. **Anti-dsDNA** (ขึ้นเมื่อโรคกำเริบ)
2. **C3, C4** (ลดลงเมื่อโรคกำเริบ)

> ข้อสอบชอบถามสามแบบ: "ตรวจอะไรเพื่อวินิจฉัย" → **ANA/anti-dsDNA** · "ตัวไหน **most specific**" → **anti-dsDNA** (หรือ anti-Sm ถ้ามีในตัวเลือก) · "น่าจะพบอะไร (เมื่อมี nephritis + dsDNA บวก)" → **hypocomplementemia**

[[fig:rheum-01-03-f1]]

### Antibody อื่นที่ควรรู้ (เสริม)
- **Anti-Ro/SSA**: Sjögren, subacute cutaneous lupus, **neonatal lupus (congenital heart block)** ในลูกของแม่ที่มี anti-Ro
- **Anti-U1 RNP**: mixed connective tissue disease
- **Anti-centromere**: limited systemic sclerosis · **anti-Scl-70**: diffuse systemic sclerosis
''',
    figs=[F_AB],
    pearls=[
        "ANA ≥ 1:80: sensitivity สูง specificity ต่ำ → ใช้คัดกรอง",
        "Anti-dsDNA และ anti-Sm: specificity สูง sensitivity ต่ำ",
        "Disease activity ดูจาก anti-dsDNA ↑ และ C3/C4 ↓",
        "Antihistone = drug-induced lupus",
    ],
    items=[
        mcq("RHEUM-01-03-1",
            "A 20-year-old woman presents with polyarthralgia for 1 month with morning stiffness of 30 minutes. Temperature is 38°C. There is mild tenderness without swelling of both knees, wrists, and PIP joints. CBC: Hct 35%, WBC 6,500/mm3, platelets 110,000/mm3. Urinalysis: protein 3+, RBC 5–10/HPF; UPCR 2.0. What is the most useful investigation for diagnosis?",
            "ANA and anti-dsDNA",
            ["Erythrocyte sedimentation rate", "Anti-CCP antibody", "Rheumatoid factor", "Plain radiographs of both hands"],
            kind="old", src=OLD,
            explain='''หญิงอายุน้อย ไข้ + polyarthralgia + **platelet ต่ำ** + **proteinuria ระดับ nephrotic-range (UPCR 2.0) กับ hematuria** = สงสัย SLE ที่มีไตอักเสบ → ส่ง **ANA (entry criterion) และ anti-dsDNA (SLE-specific)**
- ESR สูงได้ในการอักเสบทุกชนิด ไม่ช่วยวินิจฉัยโรคใดโรคหนึ่ง
- Anti-CCP และ RF ใช้สำหรับ RA ซึ่งไม่อธิบาย thrombocytopenia และ nephritis
- X-ray มือใน SLE มักปกติ ไม่ช่วยวินิจฉัย''',
            pearl="สงสัย SLE → ANA (entry) + anti-dsDNA/anti-Sm (specific)", topic="SLE investigation",
            ref=[f"{D} หน้า 22–23"], nl=["B5.3(5)", "2.3.13-3(15)"]),
        mcq("RHEUM-01-03-2",
            "A 30-year-old woman has had intermittent pain in her finger joints and wrists for 2 weeks and an erythematous rash on her face. Urinalysis shows protein 1+ with RBC casts; other laboratory results are normal. Which is the most specific investigation for diagnosis?",
            "Anti-dsDNA antibody",
            ["Antinuclear antibody", "Anti-CCP antibody", "Anti-histone antibody", "Anti-DNase B antibody"],
            kind="old", src=OLD,
            explain='''ผื่นที่หน้า + arthritis + **RBC cast (glomerulonephritis)** = SLE · คำถามคือ **most specific** → **anti-dsDNA** (specificity สูง)
- ANA ไวมากแต่ไม่จำเพาะ บวกได้ในโรค autoimmune อื่นและคนปกติ
- Anti-CCP จำเพาะต่อ RA ไม่ใช่ SLE
- Anti-histone ใช้สำหรับ drug-induced lupus ซึ่งมักไม่มีไตอักเสบ
- Anti-DNase B ใช้หาการติดเชื้อ streptococcus นำมาก่อน (post-strep GN) ซึ่งไม่มีผื่นที่หน้าและข้ออักเสบที่นิ้วแบบนี้''',
            pearl="Most specific ใน SLE = anti-dsDNA / anti-Sm", topic="SLE antibody",
            ref=[f"{D} หน้า 11, 24–25"], nl=["B5.3(5)", "2.3.13-3(15)"]),
        mcq("RHEUM-01-03-3",
            "A 20-year-old woman has polyarthralgia with 30 minutes of morning stiffness for 1 month and fever of 38°C. There is tenderness and swelling of the knees, wrists, and PIP joints bilaterally. Urinalysis: protein 3+, RBC 5–10/HPF. ANA is positive at 1:1,280 and anti-dsDNA is positive. Which additional finding is most likely in this patient?",
            "Hypocomplementemia",
            ["Thrombocytopenia", "Positive anti-Sm antibody", "Positive indirect Coombs test", "Marginal erosions on hand radiographs"],
            kind="old", src=OLD,
            explain='''SLE ที่กำลังกำเริบ มี nephritis และ **anti-dsDNA บวก** → immune complex ใช้ complement ไป = **C3/C4 ต่ำ** (ตัวที่ใช้ดู disease activity คู่กับ anti-dsDNA)
- Thrombocytopenia พบได้ใน SLE แต่ไม่ได้สัมพันธ์กับ anti-dsDNA และ nephritis โดยตรงเท่า complement
- Anti-Sm จำเพาะแต่ sensitivity ต่ำ (บวกเพียงส่วนน้อยของผู้ป่วย) จึงไม่ใช่สิ่งที่ "น่าจะพบมากที่สุด"
- Coombs test บวกเมื่อมี autoimmune hemolysis ซึ่งโจทย์ไม่ได้บอก (ใน SLE ใช้ direct Coombs ไม่ใช่ indirect)
- Marginal erosion เป็นลักษณะของ RA — SLE arthritis ไม่มี erosion''',
            pearl="Anti-dsDNA ↑ คู่กับ C3/C4 ↓ = SLE active", topic="Disease activity",
            ref=[f"{D} หน้า 12, 26–27"], nl=["B5.3(5)", "2.3.13-3(15)"]),
        mcq("RHEUM-01-03-4",
            "A healthy 28-year-old woman delivers a baby who is found to have complete heart block with bradycardia of 55/min. The mother has no symptoms, but on review she reports occasional dry eyes. Which maternal antibody is most likely responsible?",
            "Anti-Ro/SSA antibody",
            ["Anti-dsDNA antibody", "Anti-Smith antibody", "Anti-histone antibody", "Anti-centromere antibody"],
            explain='''**Neonatal lupus**: **anti-Ro/SSA** (และ anti-La) ของแม่ผ่านรกไปทำลายระบบนำไฟฟ้าหัวใจทารก → **congenital complete heart block** แม่อาจไม่มีอาการหรือเป็น Sjögren (ตาแห้ง) (เนื้อหาเสริม)
- Anti-dsDNA สัมพันธ์กับ SLE activity และ lupus nephritis ไม่ทำให้ heart block ในทารก
- Anti-Sm จำเพาะต่อ SLE แต่ไม่เกี่ยวกับ neonatal lupus
- Anti-histone ใช้สำหรับ drug-induced lupus
- Anti-centromere พบใน limited systemic sclerosis (CREST)''',
            pearl="ทารก congenital heart block → แม่มี anti-Ro/SSA (เสริม)", topic="Anti-Ro",
            ref=[f"{D} หน้า 11–12"], nl=["B5.3(5)"]),
    ])

# ---------------------------------------------------------------- 01-04 SLE management
F_TX = fig("rheum-01-04-f1", "SLE: เลือกยาตามความรุนแรง", '''<svg viewBox="0 0 720 380">
 <rect x="10" y="10" width="700" height="40" rx="10" class="ok"/>
 <text x="360" y="28" text-anchor="middle" class="tw">ทุกราย: HCQ/CQ (ตรวจตา retinopathy ปีละครั้ง) + กันแดด + เลิกบุหรี่</text>
 <text x="360" y="44" text-anchor="middle" class="tw">ปวดข้อ: NSAID ช่วงสั้น</text>
 <rect x="10" y="62" width="225" height="44" rx="10" class="c1"/>
 <text x="122" y="89" text-anchor="middle" class="tw">Mild</text>
 <rect x="247" y="62" width="225" height="44" rx="10" class="miss"/>
 <text x="360" y="89" text-anchor="middle" class="tw">Moderate</text>
 <rect x="485" y="62" width="225" height="44" rx="10" class="bad"/>
 <text x="597" y="89" text-anchor="middle" class="tw">Severe / organ-threatening</text>
 <rect x="10" y="114" width="225" height="136" rx="10" class="c1soft"/>
 <text x="20" y="136" class="t3">ไข้ อ่อนเพลีย ปวดหัว</text>
 <text x="20" y="154" class="t3">arthritis, rash</text>
 <text x="20" y="172" class="t3">pleuritis/pericarditis เล็กน้อย</text>
 <text x="20" y="190" class="t3">effusion เล็กน้อย</text>
 <text x="20" y="208" class="t3">leukopenia, lymphopenia</text>
 <text x="20" y="226" class="t3">Plt 50–149 × 10^9/L</text>
 <rect x="247" y="114" width="225" height="136" rx="10" class="misssoft"/>
 <text x="257" y="136" class="t3">หลายระบบพร้อมกัน</text>
 <text x="257" y="154" class="t3">ผื่น ≤ 2/9 ของผิว</text>
 <text x="257" y="172" class="t3">arthritis, serositis ชัดขึ้น</text>
 <text x="257" y="190" class="t3">Plt 25–49 × 10^9/L</text>
 <rect x="485" y="114" width="225" height="136" rx="10" class="badsoft"/>
 <text x="495" y="136" class="t3">LN class III, IV, V</text>
 <text x="495" y="154" class="t3">AIHA, Plt &lt; 25 × 10^9/L</text>
 <text x="495" y="172" class="t3">Neuropsychiatric lupus</text>
 <text x="495" y="190" class="t3">Myocarditis, vasculitis</text>
 <text x="495" y="208" class="t3">Pneumonitis, lung hemorrhage</text>
 <text x="495" y="226" class="t3">Effusion ปริมาณมาก</text>
 <rect x="10" y="260" width="225" height="110" rx="10" class="box"/>
 <text x="20" y="282" class="tb">Topical steroid</text>
 <text x="20" y="300" class="t2">± Pred ≤ 20 mg/d สั้น ๆ</text>
 <text x="20" y="318" class="t2">± MTX 7.5–15 mg/wk</text>
 <text x="20" y="346" class="ta">HCQ ≤ 6.5 mg/kg/d</text>
 <rect x="247" y="260" width="225" height="110" rx="10" class="box"/>
 <text x="257" y="282" class="tb">Pred ≤ 0.5 mg/kg/d</text>
 <text x="257" y="300" class="t2">+ AZA หรือ MTX หรือ MMF</text>
 <text x="257" y="318" class="t2">(steroid-sparing)</text>
 <text x="257" y="346" class="ta">+ HCQ</text>
 <rect x="485" y="260" width="225" height="110" rx="10" class="box"/>
 <text x="495" y="282" class="tb">IV methylpred pulse</text>
 <text x="495" y="300" class="t2">500 mg × 1–3 วัน</text>
 <text x="495" y="318" class="t2">+ MMF หรือ CYC (AZA)</text>
 <text x="495" y="346" class="ta">+ HCQ</text>
</svg>''', "แถบเขียวบนคือสิ่งที่ผู้ป่วยทุกคนได้ · ไล่จากซ้ายไปขวาตามความรุนแรง ยิ่งกระทบอวัยวะสำคัญยิ่งต้องใช้ steroid ขนาดสูงร่วมกับ immunosuppressant")

S4 = sec("rheum-01-04", "SLE: การรักษา, lupus nephritis และ drug-induced lupus",
    "HCQ ทุกราย (ตรวจตาปีละครั้ง) · mild: topical/PO pred · severe: IV high-dose steroid + AZA/MMF/CYC · LN III/IV = steroid + IS · hydralazine → drug-induced", minutes=10,
    source=f"{D} หน้า 13–17, 28–31", nl=["2.3.13-3(15)", "B1.7.4", "B1.7.1(4)"],
    md='''
### แบ่งความรุนแรง (สไลด์หน้า 13)

| Mild | Severe (vital organ) |
|---|---|
| fever, arthritis, rash, fatigue, headache | **massive** pleural/pericardial effusion |
| pericarditis/pleuritis เล็กน้อย, effusion เล็กน้อย | **lupus nephritis class III, IV, V** |
| leukopenia, lymphopenia | **AIHA, platelet ต่ำมาก** |
| | **neuropsychiatric lupus**, vasculitis, myocarditis |
| | lupus pneumonitis, **lung hemorrhage** |

### หลักการรักษา (สไลด์หน้า 17)
- **ทั่วไป**: เลิกบุหรี่ · หลีกเลี่ยงแสง UV
- **Symptomatic**: NSAID คุมปวด
- **ทุกราย: hydroxychloroquine/chloroquine** → ต้อง **ตรวจตาหา retinopathy, maculopathy ปีละครั้ง**
- **Mild–moderate**: **topical steroid / PO prednisolone ± immunosuppressant**
- **Severe/organ-threatening**: **IV high-dose steroid + immunosuppressant** (azathioprine, mycophenolate mofetil, cyclophosphamide)

[[fig:rheum-01-04-f1]]

### ขนาดยาตาม EULAR (สไลด์หน้า 14–15)

| | Mild | Moderate | Severe (non-renal) |
|---|---|---|---|
| Steroid เริ่ม | topical หรือ pred **≤ 20 mg/d** 1–2 สัปดาห์ (หรือ IM/IA methylpred 80–120 mg) | pred **≤ 0.5 mg/kg/d** หรือ IV methylpred ≤ 250 mg × 1–3 | pred ≤ 0.5 mg/kg/d และ/หรือ **IV methylpred 500 mg × 1–3** หรือ pred 0.75–1 mg/kg/d |
| ยาร่วม | **HCQ ≤ 6.5 mg/kg/d** ± MTX 7.5–15 mg/wk ± NSAID ไม่กี่วัน | AZA 1.5–2 mg/kg/d หรือ MTX 10–25 mg/wk หรือ MMF 2–3 g/d หรือ ciclosporin + HCQ | AZA หรือ MMF 2–3 g/d หรือ **CYC IV** หรือ ciclosporin + HCQ |
| Maintenance | pred **≤ 7.5 mg/d** + HCQ 200 mg/d | pred ≤ 7.5 mg/d + AZA/MTX/MMF + HCQ | pred ≤ 7.5 mg/d + MMF/AZA + HCQ |

- เป้าหมาย (EULAR 2023, สไลด์หน้า 15): **remission หรือ low disease activity** (SLEDAI ≤ 4) โดย **steroid ≤ 5 mg/d** · ค่อย ๆ หยุดทุกตัว **ยกเว้น HCQ**
- ยาใหม่: belimumab, anifrolumab (moderate–severe), rituximab (severe) · ผู้ที่มี aPL บวก: aspirin/VKA

### Lupus nephritis (สไลด์หน้า 16)

| Class | Pattern | ตะกอนปัสสาวะ | Proteinuria/24 h | Anti-dsDNA, C3/C4 |
|---|---|---|---|---|
| I | normal (minimal mesangial) | bland | < 200 mg | ปกติ |
| II | mesangial | RBC หรือ bland | 200–500 mg | ปกติ |
| **III** | **focal** proliferative | RBC, WBC | 500–3,500 mg | **dsDNA บวก, C3/C4 ต่ำ** |
| **IV** | **diffuse** proliferative | RBC, WBC, **RBC cast** | 1,000 ถึง > 3,500 mg | **dsDNA สูง, C3/C4 ต่ำ**, BP สูง, Cr อาจถึงต้องฟอกไต |
| V | membranous | bland | **> 3,000 mg** (nephrotic) | dsDNA ต่ำ–ปานกลาง, C3/C4 ปกติ |

> **LN class III/IV (จากผล biopsy) → steroid + immunosuppressant** · SLE ที่มี proteinuria/active sediment ใหม่ → **renal biopsy** เพื่อแยก class (เสริม)

### Drug-induced SLE (สไลด์หน้า 7, 30–31)
- ยาที่ข้อสอบชอบ: **hydralazine**, **isoniazid**, **procainamide** (อื่น ๆ: minocycline, anti-TNF — เสริม)
- อาการมักเป็น ไข้ ผื่น ข้อ **serositis** · ไตและสมองไม่ค่อยเป็น (เสริม)
- Lab: **antihistone** บวก · หยุดยาแล้วดีขึ้น
''',
    figs=[F_TX],
    pearls=[
        "HCQ/CQ ให้ทุกราย → ตรวจ retinopathy/maculopathy ปีละครั้ง",
        "Mild–moderate: topical/PO pred ± IS · severe: IV high-dose steroid + AZA/MMF/CYC",
        "LN class III/IV จาก biopsy → steroid + immunosuppressant",
        "ผู้สูงอายุ HT + ไข้ ผื่นแก้ม pericarditis cytopenia → hydralazine (antihistone)",
        "เป้าหมาย steroid ≤ 5 mg/d และหยุดยาทุกตัวยกเว้น HCQ",
    ],
    items=[
        mcq("RHEUM-01-04-1",
            "A 20-year-old woman has had a skin rash and joint pain for 3 months. Examination shows a raised erythematous patch over the malar area and mild tenderness and swelling of the 2nd–5th PIP joints bilaterally. CBC: Hb 11 g/dL, WBC 3,500/mm3 (N 75%, L 10%), platelets 120,000/mm3. Urinalysis: protein 1+, RBC 1–2/HPF; UPCR 0.5 g/g. ANA is positive at 1:640. What is the proper management?",
            "Topical steroid, oral prednisolone, and chloroquine",
            ["Topical steroid and ibuprofen", "Ibuprofen and chloroquine", "Topical steroid and chloroquine", "Pulse methylprednisolone"],
            kind="old", src=OLD,
            explain='''SLE ระดับ **mild–moderate** (ผื่น ข้อ leukopenia/lymphopenia, platelet ต่ำเล็กน้อย, proteinuria น้อย ไม่มี active sediment) → **antimalarial (CQ/HCQ) ทุกราย + topical steroid สำหรับผื่น + PO prednisolone ขนาดต่ำ–ปานกลาง** คุม arthritis และ cytopenia
- Topical steroid กับ ibuprofen ขาด antimalarial ซึ่งต้องให้ผู้ป่วยทุกคน
- Ibuprofen กับ chloroquine ไม่ได้รักษาผื่นและ cytopenia และ NSAID ควรระวังเมื่อมี proteinuria
- Topical steroid กับ chloroquine ยังไม่พอคุม arthritis และ cytopenia ที่มีอยู่
- Pulse methylprednisolone ใช้ในโรครุนแรงที่กระทบอวัยวะสำคัญ เช่น LN class III/IV, NPSLE — เคสนี้ยังไม่ถึง''',
            pearl="SLE mild–moderate: CQ/HCQ + topical steroid + PO pred", topic="SLE treatment",
            ref=[f"{D} หน้า 17, 28–29"], nl=["2.3.13-3(15)", "B1.7.4"]),
        mcq("RHEUM-01-04-2",
            "A 75-year-old woman with well-controlled hypertension for 10 years presents with fever and malaise for 1 month. Examination shows a rash on both cheeks and a pericardial friction rub. CBC: Hct 28%, WBC 2,800/mm3 (N 80%, L 20%), platelets 80,000/mm3. Electrolytes are normal. Which antihypertensive drug is most likely responsible?",
            "Hydralazine",
            ["Atenolol", "Losartan", "Enalapril", "Hydrochlorothiazide"],
            kind="old", src=OLD,
            explain='''ผู้สูงอายุที่มีอาการแบบ lupus (ไข้ ผื่นแก้ม **pericarditis** cytopenia) หลังใช้ยาลดความดันนาน = **drug-induced SLE** ยาตัวที่เป็นสาเหตุคลาสสิกคือ **hydralazine** (พร้อม isoniazid, procainamide) → ตรวจ antihistone และหยุดยา
- Atenolol, losartan และ enalapril ไม่ใช่สาเหตุที่รู้จักของ drug-induced lupus
- Hydrochlorothiazide ทำให้เกิด subacute cutaneous lupus (ผื่นที่โดนแดด) ได้บ้าง แต่ไม่ทำ systemic lupus ที่มี serositis และ cytopenia แบบนี้ ผลข้างเคียงหลักคือ Na ต่ำ, K ต่ำ, กรดยูริกสูง''',
            pearl="Drug-induced lupus: hydralazine, INH, procainamide → antihistone", topic="Drug-induced SLE",
            ref=[f"{D} หน้า 7, 30–31"], nl=["B1.7.1(4)", "2.3.13-3(15)"]),
        mcq("RHEUM-01-04-3",
            "A 28-year-old woman with SLE controlled on hydroxychloroquine develops new leg edema. Blood pressure is 150/95 mmHg. Urinalysis shows protein 3+, RBC 20–30/HPF with RBC casts; 24-hour urine protein is 2.5 g. Serum creatinine has risen from 0.7 to 1.3 mg/dL. Anti-dsDNA titer is high and C3 is low. What is the most appropriate next step to guide therapy?",
            "Renal biopsy",
            ["Increase hydroxychloroquine dose and recheck in 3 months", "Start ACE inhibitor alone and observe", "Repeat ANA titer", "Renal ultrasound only"],
            explain='''SLE ที่มี **active nephritis** (RBC cast, proteinuria 2.5 g, Cr ขึ้น, dsDNA สูง C3 ต่ำ) → ทำ **renal biopsy** เพื่อแยก class เพราะ **class III/IV ต้องได้ steroid + immunosuppressant** (เนื้อหาการตัดสินใจ biopsy เป็นส่วนเสริม)
- เพิ่ม HCQ ไม่พอสำหรับ LN ที่รุนแรง และ HCQ ไม่ควรเกิน 6.5 mg/kg/d (ตามสไลด์) / 5 mg/kg/d (แนวทางปัจจุบัน)
- ACE inhibitor ช่วยลด proteinuria แต่ใช้เป็นยาเสริม ไม่ใช่การรักษาหลักของ proliferative LN
- ANA ไม่ใช้ติดตาม activity — ตัวที่ใช้คือ anti-dsDNA และ C3/C4
- Ultrasound ไตบอกขนาดไตแต่ไม่บอก class''',
            pearl="SLE + active sediment/proteinuria → renal biopsy แยก class (เสริม)", topic="Lupus nephritis",
            ref=[f"{D} หน้า 16"], nl=["2.3.13-3(15)", "2.3.14(2)"]),
        mcq("RHEUM-01-04-4",
            "A 35-year-old woman with SLE has taken hydroxychloroquine for 5 years and is in remission. Which monitoring is specifically required because of this drug?",
            "Annual eye examination for retinopathy and maculopathy",
            ["Monthly complete blood count", "Liver function tests every 3 months", "Annual pulmonary function tests", "Annual audiometry"],
            explain='''Antimalarial (HCQ/CQ) สะสมที่จอตา → **retinopathy/maculopathy** → สไลด์ให้ **ตรวจตาปีละครั้ง**
- CBC รายเดือนจำเป็นกับยากดภูมิ เช่น azathioprine, cyclophosphamide ไม่ใช่ HCQ
- LFT ทุก 3 เดือนใช้ติดตาม methotrexate
- Pulmonary function test ไม่ใช่การติดตามประจำของ HCQ (ใช้เมื่อสงสัย ILD หรือ MTX pneumonitis)
- Audiometry ใช้กับยาที่เป็นพิษต่อหู เช่น aminoglycoside''',
            pearl="HCQ/CQ → ตรวจตาปีละครั้ง", topic="Antimalarial toxicity",
            ref=[f"{D} หน้า 17"], nl=["B1.7.1(4)"]),
    ])

# ---------------------------------------------------------------- 01-05 APS
S5 = sec("rheum-01-05", "Antiphospholipid syndrome (APS)",
    "Idiopathic หรือร่วม SLE · venous/arterial thrombosis + recurrent miscarriage · aPTT ยาว · LA, aCL, anti-β2GP · primary ASA · secondary warfarin/LMWH/UFH", minutes=5,
    source=f"{D} หน้า 32", nl=["2.3.9(2)", "B2.3(7)", "2.3.15(1)"],
    md='''
### นิยามและกลไก
- สาเหตุ: **idiopathic (primary)** หรือ **ร่วมกับ SLE (secondary)** (สไลด์หน้า 32)
- กลไก (เสริม): antiphospholipid antibody จับ β2-glycoprotein I บนเยื่อหุ้มเซลล์ endothelium/เกล็ดเลือด/รก → กระตุ้น coagulation และ complement → **ลิ่มเลือดทั้งหลอดเลือดดำและแดง**

### อาการ (สไลด์หน้า 32)
- **Clinical thrombosis**
  - **Venous**: DVT, PE, livedo reticularis
  - **Arterial**: stroke, MI (คนอายุน้อยไม่มีปัจจัยเสี่ยง — เสริม)
- **Recurrent miscarriage** (pregnancy morbidity)

### การวินิจฉัย
- Coagulogram: **aPTT ยาว** — ในหลอดทดลองดูเหมือนเลือดออกง่าย แต่ในร่างกาย **เกิดลิ่มเลือด** (lupus anticoagulant แย่ง phospholipid ในน้ำยา) · mixing study ไม่แก้ (เสริม)
- **Antiphospholipid antibodies**: **lupus anticoagulant**, **anticardiolipin**, **anti-β2-glycoprotein I**
- ต้องบวกซ้ำห่างกัน **≥ 12 สัปดาห์** (เสริม)

### การรักษา (สไลด์หน้า 32)

| สถานการณ์ | ยา |
|---|---|
| **Primary prophylaxis** (aPL บวก ยังไม่เคยมีลิ่มเลือด) | **Aspirin (ASA)** ขนาดต่ำ |
| **Secondary prophylaxis** (เคยมี thrombosis) | **Warfarin** (INR 2–3 — เสริม), **LMWH, UFH** |
| ตั้งครรภ์ (เสริม) | LMWH + low-dose aspirin (warfarin ห้ามในครรภ์) |

> DOAC (โดยเฉพาะ rivaroxaban) **ไม่แนะนำ** ใน APS ที่บวกสามตัว (triple positive) หรือมี arterial thrombosis — ใช้ warfarin (เสริม)
''',
    pearls=[
        "APS = thrombosis (venous/arterial) + recurrent miscarriage + aPL บวก",
        "aPTT ยาวแต่เกิดลิ่มเลือด = lupus anticoagulant",
        "aPL: lupus anticoagulant, anticardiolipin, anti-β2-glycoprotein I",
        "Primary prophylaxis = ASA · secondary = warfarin/LMWH/UFH",
    ],
    items=[
        mcq("RHEUM-01-05-1",
            "A 30-year-old woman has had three consecutive first-trimester miscarriages. Examination shows livedo reticularis. Platelets are 110,000/mm3, PT is normal, and aPTT is prolonged and does not correct with a 1:1 mixing study. She has no history of abnormal bleeding. What is the most likely diagnosis?",
            "Antiphospholipid syndrome",
            ["Hemophilia A", "von Willebrand disease", "Disseminated intravascular coagulation", "Vitamin K deficiency"],
            explain='''**Recurrent miscarriage + livedo reticularis + aPTT ยาวที่ mixing ไม่แก้ (มี inhibitor) + ไม่มีเลือดออก** = lupus anticoagulant ใน **APS**
- Hemophilia A ทำให้ aPTT ยาวแต่ mixing แก้ได้ (ขาด factor) และมีเลือดออกในข้อ/กล้ามเนื้อ พบในผู้ชาย
- von Willebrand disease มีเลือดออกตามเยื่อบุ และ aPTT ยาวแบบแก้ได้ด้วย mixing
- DIC ต้องมีโรคตั้งต้นรุนแรง PT ยาวด้วย และ fibrinogen ต่ำ
- Vitamin K deficiency ทำให้ PT ยาวเด่นก่อน''',
            pearl="aPTT ยาว mixing ไม่แก้ + แท้งซ้ำ/ลิ่มเลือด = APS", topic="APS diagnosis",
            ref=[f"{D} หน้า 32"], nl=["B2.3(7)", "2.3.15(1)"]),
        mcq("RHEUM-01-05-2",
            "A 34-year-old woman with SLE develops an acute left femoral deep vein thrombosis. Lupus anticoagulant, anticardiolipin, and anti-β2-glycoprotein I antibodies are all persistently positive 12 weeks apart. After initial heparin therapy, what is the most appropriate long-term anticoagulant?",
            "Warfarin",
            ["Low-dose aspirin alone", "Rivaroxaban", "Clopidogrel", "No long-term anticoagulation"],
            explain='''APS ที่เกิด thrombosis แล้ว = **secondary prophylaxis** → **warfarin** (สไลด์: warfarin, LMWH, UFH) ระยะยาว · ผู้ป่วยรายนี้บวกทั้งสามตัว (triple positive) ซึ่งเสี่ยงสูง
- Aspirin เดี่ยวใช้สำหรับ primary prophylaxis ในคนที่ aPL บวกแต่ยังไม่เคยมีลิ่มเลือด
- Rivaroxaban/DOAC มีลิ่มเลือดซ้ำมากกว่า warfarin ใน triple-positive APS จึงไม่แนะนำ (เสริม)
- Clopidogrel เป็น antiplatelet ไม่พอสำหรับ venous thrombosis
- APS มีโอกาสเกิดซ้ำสูง จึงต้องให้ยาต้านการแข็งตัวของเลือดระยะยาว''',
            pearl="APS + thrombosis → warfarin ระยะยาว", topic="APS treatment",
            ref=[f"{D} หน้า 32"], nl=["2.3.9(2)"]),
        mcq("RHEUM-01-05-3",
            "A 26-year-old woman with newly diagnosed SLE is found to have persistently positive lupus anticoagulant. She has never had thrombosis or pregnancy loss. What is the most appropriate prophylaxis?",
            "Low-dose aspirin",
            ["Warfarin", "Therapeutic low-molecular-weight heparin", "High-dose prednisolone", "Rivaroxaban"],
            explain='''aPL บวกแต่ **ยังไม่เคยมีเหตุการณ์ลิ่มเลือด** = **primary prophylaxis → aspirin** (สไลด์หน้า 32)
- Warfarin และ therapeutic LMWH สำหรับ secondary prophylaxis หลังเกิด thrombosis แล้ว
- Prednisolone ไม่ช่วยป้องกันลิ่มเลือดจาก aPL
- Rivaroxaban ไม่ใช่ยาป้องกันปฐมภูมิ และไม่แนะนำใน APS เสี่ยงสูง''',
            pearl="aPL บวก ยังไม่มี thrombosis → ASA", topic="APS prophylaxis",
            ref=[f"{D} หน้า 32"], nl=["2.3.13-3(15)"]),
    ])

LECTURE = lecture("01", "Approach to arthritis, SLE & APS", "articular vs periarticular · synovial fluid · SLE · autoantibody · lupus nephritis · APS",
    objectives=[
        "แยก articular/periarticular และ inflammatory/mechanical แล้วจัดกลุ่ม mono/oligo/polyarthritis ได้",
        "แปลผล synovial fluid ตามจุดตัด WBC 200 · 2,000 · 50,000",
        "วินิจฉัย SLE ด้วยเกณฑ์ EULAR/ACR 2019 และเลือก autoantibody ให้ตรงคำถาม (screen, specific, activity)",
        "เลือกการรักษา SLE ตามความรุนแรง รู้ class ของ lupus nephritis และยาที่ทำให้เกิด drug-induced lupus",
        "วินิจฉัยและเลือกการป้องกันลิ่มเลือดใน APS ได้",
    ],
    sections=[S1, S2, S3, S4, S5])
