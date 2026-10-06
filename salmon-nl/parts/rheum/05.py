from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Rheumato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 05-01 Septic arthritis dx
F_MONO = fig("rheum-05-01-f1", "Acute monoarthritis: เจาะข้อก่อนเสมอ แล้วอ่านผล", '''<svg viewBox="0 0 740 400">
 <defs><marker id="rheum-05-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="10" width="280" height="50" rx="10" class="acsoft"/>
 <text x="370" y="31" text-anchor="middle" class="tb">ข้อเดียว บวม แดง ร้อน เฉียบพลัน</text>
 <text x="370" y="50" text-anchor="middle" class="t3">± ไข้ · แม้เป็นผู้ป่วย RA/gout เดิม</text>
 <path d="M370 60V84" class="ln" marker-end="url(#rheum-05-01-a)"/>
 <rect x="200" y="86" width="340" height="50" rx="10" class="bad"/>
 <text x="370" y="107" text-anchor="middle" class="tw">Arthrocentesis (joint fluid analysis)</text>
 <text x="370" y="126" text-anchor="middle" class="tw">cell count · G/S · C/S · crystal · glucose</text>
 <path d="M250 136L110 170" class="ln" marker-end="url(#rheum-05-01-a)"/>
 <path d="M370 136V170" class="ln" marker-end="url(#rheum-05-01-a)"/>
 <path d="M490 136L630 170" class="ln" marker-end="url(#rheum-05-01-a)"/>
 <rect x="10" y="172" width="220" height="110" rx="10" class="badsoft"/>
 <text x="20" y="194" class="tb">Septic</text>
 <text x="20" y="214" class="t2">WBC &gt; 50,000 · PMN &gt; 90%</text>
 <text x="20" y="232" class="t2">G/S หรือ C/S บวก · glucose ↓</text>
 <text x="20" y="256" class="ta">→ drainage + IV ATB</text>
 <text x="20" y="274" class="t3">ส่ง hemoculture ด้วย</text>
 <rect x="260" y="172" width="220" height="110" rx="10" class="misssoft"/>
 <text x="270" y="194" class="tb">Crystal</text>
 <text x="270" y="214" class="t2">WBC 2,000–50,000</text>
 <text x="270" y="232" class="t2">เข็ม (−) = gout</text>
 <text x="270" y="250" class="t2">rhomboid (+) = CPPD</text>
 <text x="270" y="274" class="ta">→ colchicine/NSAID/steroid</text>
 <rect x="510" y="172" width="220" height="110" rx="10" class="c1soft"/>
 <text x="520" y="194" class="tb">Hemarthrosis</text>
 <text x="520" y="214" class="t2">น้ำสีแดง</text>
 <text x="520" y="232" class="t2">trauma, ligament injury,</text>
 <text x="520" y="250" class="t2">hemophilia, warfarin</text>
 <text x="520" y="274" class="ta">→ X-ray หา fracture</text>
 <rect x="10" y="300" width="720" height="88" rx="10" class="sunk"/>
 <text x="22" y="322" class="tb">กับดักในโจทย์</text>
 <text x="22" y="344" class="t2">• RA flare เป็น polyarthritis — RA ที่มีข้อเดียวบวมร้อนมีไข้ = septic จนกว่าจะพิสูจน์ได้ (RA และยากดภูมิเป็นปัจจัยเสี่ยง)</text>
 <text x="22" y="364" class="t2">• อย่าเพิ่มยากดภูมิ อย่าให้ colchicine ก่อนได้ผลเจาะข้อ · ESR/CRP/X-ray/uric acid ไม่ช่วยแยก septic</text>
 <text x="22" y="382" class="t2">• ผลึกพบได้พร้อมการติดเชื้อ — ต้องรอ G/S และ culture เสมอ (เสริม)</text>
</svg>''', "อ่านจากบนลงล่าง: acute monoarthritis ทุกรายต้องเจาะข้อ แล้วใช้ cell count, Gram stain/culture และผลึกแยก 3 กลุ่มหลัก (septic, crystal, hemarthrosis)")

S1 = sec("rheum-05-01", "Septic arthritis: สาเหตุ เชื้อ และการวินิจฉัย acute monoarthritis",
    "Hematogenous พบบ่อยสุด · เสี่ยง DM IVDU HIV prosthesis RA · ผู้ใหญ่ S. aureus, strep, GC (เข่า) · < 2 ปี Kingella · ทารกแรกเกิด GBS (สะโพก) · ไข้ + acute monoarthritis → arthrocentesis: WBC > 50,000 PMN > 90% G/S C/S + glucose ↓", minutes=9,
    source=f"{D} หน้า 104–108, 110–119", nl=["2.3.13-3(6)", "B5.2.2-3(1)", "B5.3(3)"],
    md='''
### สาเหตุและปัจจัยเสี่ยง (สไลด์หน้า 104)
- **Hematogenous spread (พบบ่อยที่สุด)** เช่น septicemia, แผลติดเชื้อ
- **Direct contamination**: iatrogenic (ฉีดยาเข้าข้อ), trauma (แผลทะลุข้อ)
- **Contiguous spread**: osteomyelitis ที่อยู่ติดกัน
- **ปัจจัยเสี่ยง: DM, IVDU, HIV, ข้อเทียม (prosthetic implant), rheumatoid arthritis** (ข้อเดิมเสีย + ยากดภูมิ)

### เชื้อก่อโรคตามอายุ (สไลด์หน้า 105)

| กลุ่ม | เชื้อ | ข้อที่พบบ่อย |
|---|---|---|
| **ผู้ใหญ่ / เด็ก > 2 ปี** | **S. aureus** (พบบ่อยสุด), **Streptococci** · **N. gonorrhoeae** ในคนที่มีเพศสัมพันธ์ | **เข่า** |
| เด็ก < 2 ปี | **Kingella kingae** | |
| ทารก < 1 เดือน | **Group B Streptococcus**, S. aureus, N. gonorrhoeae, gram-negative bacilli | **สะโพก** |
| IVDU (เสริม) | S. aureus, **Pseudomonas** (ข้อแปลก ๆ เช่น sternoclavicular, SI) | |

### อาการ (สไลด์หน้า 106)
- **ไข้ + acute monoarthritis** (บวม แดง ร้อน กดเจ็บ **ขยับข้อได้น้อยทั้ง flexion และ extension**) · gonococcal เป็น polyarthritis ได้

### Investigation (สไลด์หน้า 107)
- **Arthrocentesis (สำคัญที่สุด)**: **WBC > 50,000/µL (PMN > 90%)**, **G/S และ C/S บวก**, **glucose ต่ำ**
- **CBC: WBC สูง left shift** (band form, metamyelocyte) · **ESR, CRP สูง**
- **Hemoculture** ทุกราย
- **X-ray**: ไม่ได้ช่วยวินิจฉัย septic แต่ใช้ R/O สาเหตุอื่น เช่น fracture

[[fig:rheum-05-01-f1]]

> Acute monoarthritis ต้อง R/O 3 อย่าง: **septic arthritis (!!!)**, **crystal-induced arthritis**, **hemarthrosis** → คำตอบของโจทย์ "next step" เกือบทุกข้อคือ **arthrocentesis / joint fluid analysis** (สไลด์หน้า 111)
> **RA flare เป็น polyarthritis ไม่ใช่ acute monoarthritis** — ผู้ป่วย RA ที่มีข้อเดียวบวมร้อน ต้องเจาะข้อ ไม่ใช่เพิ่มยา (สไลด์หน้า 117)
''',
    figs=[F_MONO],
    pearls=[
        "Septic arthritis: hematogenous พบบ่อยสุด · เสี่ยง DM, IVDU, HIV, ข้อเทียม, RA",
        "ผู้ใหญ่ S. aureus ที่เข่า · sexually active คิด GC · < 2 ปี Kingella · ทารกแรกเกิด GBS ที่สะโพก",
        "Acute monoarthritis → arthrocentesis แยก septic, crystal, hemarthrosis",
        "SF septic: WBC > 50,000, PMN > 90%, glucose ต่ำ, G/S C/S บวก",
        "RA flare = polyarthritis · RA + ข้อเดียวร้อนมีไข้ = เจาะข้อ",
    ],
    items=[
        mcq("RHEUM-05-01-1",
            "A 50-year-old woman with no underlying disease presents with left knee pain for 4 days. Temperature is 38.5°C, BP 130/80 mmHg, PR 92/min. The left knee is swollen, erythematous, and tender with a positive ballottement test. CBC: Hct 40%, WBC 18,000/mm3 (N 88%), platelets 200,000/mm3. What is the most appropriate management?",
            "Arthrocentesis",
            ["NSAIDs", "Colchicine", "Jones bandage", "Arthrotomy"],
            kind="old", src=OLD,
            explain='''**Acute monoarthritis + ไข้ + WBC สูง** → ต้อง R/O **septic arthritis** (และ crystal, hemarthrosis) ด้วย **arthrocentesis** ก่อนให้การรักษาใด ๆ (สไลด์หน้า 110–111)
- NSAID และ colchicine อาจกลบอาการและพลาด septic arthritis ที่ทำลายข้อเร็ว
- Jones bandage (พันข้อแน่น) ใช้กับการบาดเจ็บของเอ็นข้อเข่า ไม่ใช่ข้ออักเสบมีไข้
- Arthrotomy เป็นการระบายแบบเปิด ใช้เมื่อยืนยัน septic แล้วและเจาะระบายไม่ได้ผล — ยังไม่ถึงขั้นนี้''',
            pearl="Acute monoarthritis + ไข้ → arthrocentesis ก่อน", topic="Approach monoarthritis",
            ref=[f"{D} หน้า 110–111"], nl=["2.3.13-3(6)", "B5.3(3)"]),
        mcq("RHEUM-05-01-2",
            "A 50-year-old man presents with fever and right knee pain for 2 days. Temperature is 38.5°C. The right knee is warm, swollen, and tender, with limited movement in both flexion and extension. What is the most useful investigation?",
            "Joint fluid analysis",
            ["Serum uric acid", "Rheumatoid factor", "Plain radiograph of the knee", "Erythrocyte sedimentation rate"],
            kind="old", src=OLD,
            explain='''ข้อเดียวอักเสบเฉียบพลันมีไข้ → **joint fluid analysis** (cell count, G/S, C/S, crystal) แยก septic, gout/CPPD และ hemarthrosis ได้ในครั้งเดียว
- Serum uric acid อาจปกติระหว่าง gout attack และสูงได้ในคนที่ไม่เป็น gout จึงแยกไม่ได้
- RF ใช้ในโรคข้ออักเสบหลายข้อเรื้อรัง ไม่ช่วยในข้อเดียวเฉียบพลัน
- X-ray ระยะแรกปกติหรือเห็นแค่ข้อบวม ใช้ R/O fracture
- ESR สูงได้ทั้ง septic, gout และ RA ไม่จำเพาะ''',
            pearl="Most useful investigation ของ acute monoarthritis = joint fluid analysis", topic="Approach monoarthritis",
            ref=[f"{D} หน้า 107, 112–113"], nl=["B5.3(3)", "2.3.13-3(6)"]),
        mcq("RHEUM-05-01-3",
            "A 17-year-old boy injured his right knee playing football 1 week ago. Four days ago he developed fever and knee swelling, and since yesterday the pain has been so severe that he limps. What is the most appropriate investigation?",
            "Arthrocentesis",
            ["ASO titer", "Hemoculture alone", "Plain radiograph alone", "Serum uric acid"],
            kind="old", src=OLD,
            explain='''หลัง trauma แล้วมี **ไข้ + ข้อเข่าบวมปวดมากขึ้น** = สงสัย **septic arthritis** (trauma เป็นทาง direct contamination) หรือ hemarthrosis ที่ติดเชื้อ → **arthrocentesis** บอกได้ทั้งเลือด หนอง และเชื้อ
- ASO titer ใช้ช่วยวินิจฉัย rheumatic fever ซึ่งเป็น migratory polyarthritis หลังคออักเสบ ไม่ใช่ข้อเดียวหลังบาดเจ็บ
- Hemoculture ควรส่งร่วมด้วย แต่ไม่ได้บอกสภาพในข้อและไม่ใช่การตรวจที่สำคัญที่สุด
- X-ray ช่วย R/O fracture แต่ไม่บอกว่าติดเชื้อหรือไม่
- Uric acid ไม่เกี่ยวในวัยรุ่นหลังบาดเจ็บ''',
            pearl="Trauma + ไข้ + ข้อบวม → เจาะข้อ", topic="Septic arthritis",
            ref=[f"{D} หน้า 104, 114–115"], nl=["2.3.13-3(6)", "B5.3(3)"]),
        mcq("RHEUM-05-01-4",
            "A woman with rheumatoid arthritis for 6 months has been well controlled for 1 month on methotrexate, folic acid, and prednisolone. She now presents with right knee pain for 2 days. Temperature is 38°C. The right knee is swollen, warm, and tender; other joints are quiet. What is the most appropriate management?",
            "Right knee arthrocentesis",
            ["ESR and CRP", "Lateral and AP radiographs of the right knee", "Increase the methotrexate dose", "Increase the prednisolone dose"],
            kind="old", src=OLD,
            explain='''ผู้ป่วย RA ที่ใช้ **MTX + steroid (กดภูมิ)** มี **ข้อเดียว** บวมร้อน + ไข้ — **RA flare จะเป็น polyarthritis ไม่ใช่ acute monoarthritis** (สไลด์หน้า 117) → ต้องเจาะข้อแยก **septic arthritis**
- ESR/CRP สูงทั้ง RA flare และติดเชื้อ แยกไม่ได้
- X-ray ไม่บอกว่าติดเชื้อ
- เพิ่ม MTX หรือ prednisolone ทำให้การติดเชื้อแย่ลงถ้าเป็น septic''',
            pearl="RA + monoarthritis + ไข้ = septic จนกว่าจะพิสูจน์ได้ → เจาะข้อ", topic="Septic arthritis in RA",
            ref=[f"{D} หน้า 116–117"], nl=["2.3.13-3(6)", "2.3.13-3(12)"]),
        mcq("RHEUM-05-01-5",
            "A 50-year-old woman with rheumatoid arthritis for 10 years, well controlled with DMARDs, presents with left knee pain for 2 days. Temperature is 37°C. The left knee has a positive ballottement test; there is also tenderness and swelling of both wrists and the left second PIP joint. What is the most appropriate investigation?",
            "Joint aspiration of the left knee",
            ["ESR", "Plain radiograph", "Serum uric acid", "Rheumatoid factor"],
            kind="old", src=OLD,
            explain='''ผู้ป่วย RA มีน้ำในข้อเข่าใหม่ที่เด่นกว่าข้ออื่น → แม้ไม่มีไข้ (ยากดภูมิกลบไข้ได้) ก็ต้อง **เจาะข้อ** หา septic arthritis หรือ crystal ก่อนสรุปว่าเป็น flare (สไลด์เฉลย joint aspiration)
- ESR ไม่แยก flare กับการติดเชื้อ
- X-ray ไม่บอกการติดเชื้อหรือผลึก
- Uric acid ไม่ช่วยวินิจฉัย gout ในข้อนี้ — ต้องดูผลึกในน้ำไขข้อ
- RF ใช้วินิจฉัย RA ซึ่งรู้อยู่แล้ว และไม่บอก activity''',
            pearl="RA มีข้อบวมน้ำเด่นใหม่ → เจาะข้อ", topic="Septic arthritis in RA",
            ref=[f"{D} หน้า 118–119"], nl=["B5.3(3)", "2.3.13-3(6)"]),
    ])

# ---------------------------------------------------------------- 05-02 Septic arthritis tx
S2 = sec("rheum-05-02", "Septic arthritis: การรักษา — drainage + ยาฆ่าเชื้อตาม Gram stain",
    "Drainage (needle, arthroscopy, arthrotomy) + empirical IV ATB ตาม G/S 4–6 wk · G/S ไม่พบเชื้อ: ceftriaxone/cefotaxime · GPC: cloxacillin · GN: ceftriaxone · IVDU: cloxacillin + ceftazidime · IV 1–2 wk แล้ว oral", minutes=6,
    source=f"{D} หน้า 109, 128–131", nl=["2.3.13-3(6)", "B5.2.2-3(1)"],
    md='''
### หลักการ = Drainage + Antibiotic (สไลด์หน้า 109)
1. **Synovial fluid drainage / debridement**: **needle aspiration** (ซ้ำทุกวันได้), **arthroscopy**, **open arthrotomy**
2. **Empirical IV antibiotic ตามผล Gram stain** แล้วปรับตาม culture · รวม **4–6 สัปดาห์**
3. **IV 1–2 สัปดาห์** แล้วต่อด้วย **oral antibiotic** จนครบ

### เลือกยาตาม Gram stain (สไลด์หน้า 109)

| ผล Gram stain | ยาเริ่มต้น |
|---|---|
| **ไม่พบเชื้อ (G/S not found)** | **IV ceftriaxone / cefotaxime** |
| **Gram-positive cocci** | **IV cloxacillin** (สงสัย MRSA → vancomycin — เสริม) |
| **Gram-negative cocci/bacilli** | **IV ceftriaxone / cefotaxime** |
| **IVDU และ G/S ไม่พบเชื้อ** | **IV cloxacillin + ceftazidime** (ครอบคลุม Pseudomonas) |

### ถ้าให้ยาแล้วไม่ดีขึ้น (สไลด์หน้า 131)
1. ถ้ายัง **ไม่ได้เจาะระบาย → ต้อง aspiration** ก่อน
2. **ปรับยาตามผล C/S**
3. เจาะระบายซ้ำ 2–3 วันแล้วน้ำไขข้อยังไม่ดีขึ้น → **arthroscopy / open debridement**

> ไม่ดีขึ้นหลังให้ยา 2 วัน คำตอบคือ **ใช้ยาเดิมและระบายหนองให้มากที่สุด** ไม่ใช่เปลี่ยนยาหรือเพิ่มขนาดยา (หนองในข้อเป็นแหล่งเชื้อที่ยาเข้าไม่ถึง)
> ข้อเทียมติดเชื้อ (prosthetic joint infection) ต้องส่งออร์โธปิดิกส์ (เสริม)
''',
    pearls=[
        "Septic arthritis = drainage + IV antibiotic (รวม 4–6 สัปดาห์)",
        "G/S ไม่พบเชื้อ → ceftriaxone/cefotaxime · GPC → cloxacillin",
        "IVDU + G/S ไม่พบเชื้อ → cloxacillin + ceftazidime",
        "ให้ยาแล้วไม่ดีขึ้น → ยาเดิม + ระบายให้มากที่สุด → arthroscopy/arthrotomy",
    ],
    items=[
        mcq("RHEUM-05-02-1",
            "A 50-year-old woman presents with a 2-day history of high fever and right knee pain. Temperature is 40°C, BP 120/80 mmHg, PR 100/min. The right knee is swollen, red, and markedly tender. Joint fluid: WBC 50,000/mm3 with 90% neutrophils; Gram stain shows no organisms. Which is the most appropriate antibiotic?",
            "Ceftriaxone",
            ["Ceftazidime", "Levofloxacin", "Meropenem", "Vancomycin"],
            kind="old", src=OLD,
            explain='''Septic arthritis (ข้อเดียว ไข้สูง WBC ≥ 50,000 PMN 90%) ที่ **Gram stain ไม่พบเชื้อ** ในคนที่ไม่ใช่ IVDU → **IV ceftriaxone/cefotaxime** ร่วมกับ drainage (สไลด์หน้า 109, 128–129)
- Ceftazidime ไม่ครอบคลุม S. aureus ดีพอ ใช้ร่วมกับ cloxacillin เฉพาะใน IVDU ที่ต้องคลุม Pseudomonas
- Levofloxacin ไม่ใช่ยาเริ่มต้นมาตรฐานของ septic arthritis
- Meropenem กว้างเกินจำเป็น สำรองไว้สำหรับเชื้อดื้อยา
- Vancomycin ใช้เมื่อพบ GPC และสงสัย MRSA''',
            pearl="Septic arthritis G/S ไม่พบเชื้อ → ceftriaxone + drainage", topic="Septic arthritis ATB",
            ref=[f"{D} หน้า 109, 128–129"], nl=["2.3.13-3(6)"]),
        mcq("RHEUM-05-02-2",
            "A woman developed left knee pain after trauma and was diagnosed with septic arthritis of the left knee. Gram stain showed gram-positive cocci in clusters. After 2 days of IV cloxacillin she has not improved and the knee remains tense with effusion. No drainage has been performed. What is the most appropriate management?",
            "Continue cloxacillin and drain the joint as completely as possible",
            ["Switch to meropenem", "Increase the cloxacillin dose", "Add oral prednisolone", "Switch to oral amoxicillin-clavulanate"],
            kind="old", src=OLD,
            explain='''หลักรักษา septic arthritis คือ **drainage + ATB** · ผู้ป่วยยังไม่ได้ระบาย → **ใช้ยาเดิม (ตรงกับ GPC) แล้วระบายให้มากที่สุด** · ถ้าเจาะระบาย 2–3 วันแล้วยังไม่ดีขึ้น → arthroscopy/open debridement (สไลด์หน้า 131)
- เปลี่ยนเป็น meropenem ไม่จำเป็นเพราะยาเดิมตรงกับเชื้อ ปัญหาคือหนองที่ยังค้างในข้อ
- เพิ่มขนาด cloxacillin ไม่ช่วยถ้ายังไม่ระบายหนอง
- Prednisolone กดภูมิ ทำให้ติดเชื้อแย่ลง
- เปลี่ยนเป็นยากินเร็วเกินไป ต้องให้ IV 1–2 สัปดาห์ก่อน''',
            pearl="Septic arthritis ไม่ดีขึ้น → ระบายหนองก่อนเปลี่ยนยา", topic="Septic arthritis drainage",
            ref=[f"{D} หน้า 109, 130–131"], nl=["2.3.13-3(6)"]),
        mcq("RHEUM-05-02-3",
            "A 32-year-old man who injects heroin presents with fever and a hot, swollen right knee. Synovial fluid WBC is 85,000/mm3 (PMN 94%) and Gram stain shows no organisms. Cultures are pending. What is the most appropriate empirical antibiotic regimen along with joint drainage?",
            "IV cloxacillin plus ceftazidime",
            ["IV ceftriaxone alone", "Oral doxycycline", "IV penicillin G alone", "IV clindamycin plus gentamicin"],
            explain='''ใน **IVDU ที่ Gram stain ไม่พบเชื้อ** ต้องครอบคลุมทั้ง **S. aureus** และ **Pseudomonas** → **IV cloxacillin + ceftazidime** (สไลด์หน้า 109)
- Ceftriaxone เดี่ยวใช้ในผู้ป่วยทั่วไปที่ G/S ไม่พบเชื้อ แต่ไม่คลุม Pseudomonas
- Doxycycline ชนิดกินไม่เหมาะเป็นยาเริ่มต้นของ septic arthritis
- Penicillin G เดี่ยวไม่คลุม S. aureus ที่สร้าง penicillinase และ gram-negative
- Clindamycin + gentamicin ไม่ใช่สูตรมาตรฐาน และ aminoglycoside เข้าข้อได้ไม่ดี''',
            pearl="IVDU + G/S ไม่พบเชื้อ → cloxacillin + ceftazidime", topic="Septic arthritis IVDU",
            ref=[f"{D} หน้า 109"], nl=["2.3.13-3(6)"]),
    ])

# ---------------------------------------------------------------- 05-03 Gonococcal / DGI
S3 = sec("rheum-05-03", "Gonococcal arthritis และ disseminated gonococcal infection (DGI)",
    "คนที่มีเพศสัมพันธ์ · Gram-negative intracellular diplococci · DGI triad: migratory polyarthralgia + tenosynovitis + dermatitis (pustule/vesicle) · ceftriaxone + azithromycin", minutes=6,
    source=f"{D} หน้า 105–106, 120–127", nl=["2.3.13-3(6)", "2.3.1(19)", "B10.2.2(1)"],
    md='''
### ใครเป็นและกลไก
- **N. gonorrhoeae** เป็นสาเหตุ septic arthritis ที่พบบ่อยใน **คนหนุ่มสาวที่มีเพศสัมพันธ์** (สไลด์หน้า 105) · ผู้หญิงมากกว่า (ช่วงมีประจำเดือน/ตั้งครรภ์) และการติดเชื้อที่อวัยวะเพศมักไม่มีอาการ (เสริม)
- เชื้อเข้ากระแสเลือด (bacteremia) → กระจายไปผิวหนัง เส้นเอ็น และข้อ

### สองรูปแบบ (สไลด์หน้า 106)

| | **DGI (arthritis-dermatitis syndrome)** | **Purulent gonococcal arthritis** |
|---|---|---|
| ข้อ | **migratory polyarthralgia** | **monoarthritis/oligoarthritis** (เข่า ข้อมือ ข้อเท้า) |
| เส้นเอ็น | **tenosynovitis** (หลังมือ ข้อมือ ข้อเท้า) | ไม่เด่น |
| ผิวหนัง | **dermatitis**: ตุ่มหนอง/ตุ่มน้ำ (pustule, vesicle) บนฐานแดง จำนวนน้อย ไม่เจ็บ ที่แขนขา | ไม่มี |
| เพาะเชื้อ (เสริม) | hemoculture บวกบ่อยกว่า น้ำไขข้อมักลบ | น้ำไขข้อบวกบ่อยกว่า |

- จำ triad ของ DGI: **migratory polyarthralgia + tenosynovitis + dermatitis**

### Investigation
- น้ำไขข้อ: **Gram-negative intracellular diplococci**
- ส่ง NAAT/culture จากคอ ทวารหนัก และอวัยวะเพศ + hemoculture (เสริม)
- ตรวจโรคติดต่อทางเพศสัมพันธ์อื่น (HIV, syphilis) (เสริม)

### การรักษา (สไลด์หน้า 106, 121)
- **Ceftriaxone + azithromycin** (หรือ doxycycline เพื่อคลุม Chlamydia)
- ขนาดยา (เสริม): ceftriaxone 1 g IV วันละครั้ง จนดีขึ้น 24–48 ชั่วโมง แล้วเปลี่ยนเป็นยากินจนครบ ≥ 7 วัน · ระบายข้อถ้ามีหนอง · รักษาคู่นอน
- CDC 2020 (เสริม): แนะนำ ceftriaxone เดี่ยว และให้ doxycycline เฉพาะเมื่อยังไม่ตัด Chlamydia — **ข้อสอบตามสไลด์ใช้ ceftriaxone + azithromycin**
''',
    pearls=[
        "หนุ่มสาวที่มีเพศสัมพันธ์ + ข้ออักเสบ → คิด N. gonorrhoeae",
        "DGI triad: migratory polyarthralgia + tenosynovitis + pustule/vesicle",
        "น้ำไขข้อ: Gram-negative intracellular diplococci",
        "Tx: ceftriaxone + azithromycin (หรือ doxycycline)",
    ],
    items=[
        mcq("RHEUM-05-03-1",
            "A 35-year-old woman presents with left knee pain and swelling for 3 days. The left knee is swollen and tender with limited range of motion and a positive ballottement test. Arthrocentesis: WBC 89,000/mm3 (PMN 90%); Gram stain shows gram-negative intracellular diplococci. What is the most appropriate antibiotic?",
            "Ceftriaxone",
            ["Penicillin G", "Clindamycin", "Gentamicin", "Doxycycline alone"],
            kind="old", src=OLD,
            explain='''**Gram-negative intracellular diplococci** ในน้ำไขข้อ = **gonococcal septic arthritis** → **ceftriaxone** (+ azithromycin หรือ doxycycline ตามสไลด์หน้า 121)
- Penicillin G ใช้ไม่ได้เพราะ N. gonorrhoeae ส่วนใหญ่ดื้อ penicillin
- Clindamycin ไม่ครอบคลุม Neisseria
- Gentamicin ไม่ใช่ยามาตรฐานและเข้าข้อได้ไม่ดี
- Doxycycline เดี่ยวใช้คลุม Chlamydia เป็นยาเสริม ไม่พอสำหรับ gonococcal arthritis''',
            pearl="GN intracellular diplococci ในข้อ → ceftriaxone", topic="Gonococcal arthritis",
            ref=[f"{D} หน้า 120–121"], nl=["2.3.13-3(6)", "2.3.1(19)"]),
        mcq("RHEUM-05-03-2",
            "A 30-year-old woman has had arthritis of the right ankle and left knee for 1 week. Examination shows multiple vesicles near the right ankle and tenosynovitis over the dorsum of the right hand. What is the most likely causative pathogen?",
            "Neisseria gonorrhoeae",
            ["Staphylococcus aureus", "Streptococcus agalactiae", "Chlamydia trachomatis", "Borrelia burgdorferi"],
            kind="old", src=OLD,
            explain='''หญิงวัยเจริญพันธุ์ + **oligo/polyarthritis + ตุ่มน้ำ (dermatitis) + tenosynovitis หลังมือ** = triad ของ **DGI** จาก **N. gonorrhoeae** (สไลด์หน้า 122–123)
- S. aureus ทำให้ septic arthritis ข้อเดียว ไม่มี tenosynovitis ร่วมกับตุ่มน้ำแบบนี้
- S. agalactiae (GBS) เป็นสาเหตุในทารกแรกเกิด
- Chlamydia ทำให้ reactive arthritis หลังติดเชื้อ ไม่ใช่ tenosynovitis + pustule ระหว่างติดเชื้อ
- Borrelia (Lyme) มี erythema migrans และไม่พบในไทย''',
            pearl="Arthritis + tenosynovitis + pustule/vesicle = DGI", topic="DGI",
            ref=[f"{D} หน้า 106, 122–123"], nl=["2.3.1(19)", "2.3.13-3(6)"]),
        mcq("RHEUM-05-03-3",
            "A 28-year-old woman presents with fever and left knee pain. She initially had left ankle pain and tenderness that has now resolved. The left knee is now warm, red, and tender. Examination shows small pustules on her right calf and swelling and tenderness along the extensor tendon of her left middle finger. What is the most likely diagnosis?",
            "Disseminated gonococcal infection",
            ["Systemic lupus erythematosus", "Reactive arthritis", "Adult-onset Still disease", "Acute rheumatic fever"],
            kind="old", src=OLD,
            explain='''**Migratory arthritis (ข้อเท้าหายแล้วย้ายไปเข่า) + pustule + tenosynovitis ของเส้นเอ็นนิ้ว** ในหญิงวัยเจริญพันธุ์ = **DGI**
- SLE มี arthritis ได้แต่ไม่มีตุ่มหนองและ tenosynovitis แบบติดเชื้อ
- Reactive arthritis เกิดหลังการติดเชื้อหาย ผื่นเป็น keratoderma ที่ฝ่ามือฝ่าเท้า ไม่ใช่ pustule เดี่ยว ๆ
- Adult-onset Still มีไข้สูงเป็นพัก ๆ ผื่น salmon-colored ที่หายตามไข้ ferritin สูงมาก
- Acute rheumatic fever เป็น migratory polyarthritis ได้ แต่ต้องมีคออักเสบนำ มี carditis, erythema marginatum ไม่ใช่ pustule''',
            pearl="Migratory arthritis + pustule + tenosynovitis = DGI", topic="DGI",
            ref=[f"{D} หน้า 124–125"], nl=["2.3.1(19)"]),
        mcq("RHEUM-05-03-4",
            "A 20-year-old sexually active woman has had fever for 4 days with pain in both wrists, the right elbow, both knees, and the left ankle. Examination shows mild swelling of the affected joints, tenosynovitis of the left foot, and necrotic pustules on an erythematous base on both hands and the left foot. What is the most appropriate treatment?",
            "Ceftriaxone plus azithromycin",
            ["Levofloxacin", "Cefazolin plus doxycycline", "Clindamycin plus gentamicin", "Penicillin G plus amikacin"],
            kind="old", src=OLD,
            explain='''Polyarthritis + tenosynovitis + **pustule ที่มีเนื้อตายตรงกลางบนฐานแดง** ในหญิงที่มีเพศสัมพันธ์ = **DGI** → **ceftriaxone + azithromycin** (สไลด์หน้า 106, 126–127)
- Levofloxacin (quinolone) ไม่แนะนำเพราะ N. gonorrhoeae ดื้อสูง
- Cefazolin เป็น cephalosporin รุ่นแรก ไม่คลุม N. gonorrhoeae
- Clindamycin + gentamicin ไม่ใช่สูตรสำหรับหนองใน
- Penicillin G + amikacin ไม่ได้ผลเพราะเชื้อดื้อ penicillin''',
            pearl="DGI → ceftriaxone + azithromycin", topic="DGI treatment",
            ref=[f"{D} หน้า 106, 126–127"], nl=["2.3.1(19)", "B10.2.2(1)"]),
    ])

# ---------------------------------------------------------------- 05-04 OA
F_XR = fig("rheum-05-04-f1", "X-ray ข้อ: OA เทียบ RA เทียบ gout", '''<svg viewBox="0 0 740 330">
 <text x="125" y="22" text-anchor="middle" class="tb">Osteoarthritis</text>
 <text x="370" y="22" text-anchor="middle" class="tb">Rheumatoid arthritis</text>
 <text x="615" y="22" text-anchor="middle" class="tb">Chronic gout</text>
 <path d="M60 40H190V110Q125 124 60 110Z" class="c1soft"/>
 <path d="M60 210H190V140Q150 132 125 138Q100 132 60 140Z" class="c1soft"/>
 <path d="M60 104L42 122L66 112Z" class="bad"/>
 <path d="M190 104L208 122L184 112Z" class="bad"/>
 <path d="M60 146L42 128L66 138Z" class="bad"/>
 <path d="M190 146L208 128L184 138Z" class="bad"/>
 <path d="M70 108Q125 120 180 108" class="lnbad"/>
 <path d="M70 140Q100 134 125 140" class="lnbad"/>
 <circle cx="150" cy="162" r="7" class="box"/>
 <text x="125" y="192" text-anchor="middle" class="t3">sclerosis · cyst</text>
 <path d="M305 40H435V110Q370 124 305 110Z" class="sunk"/>
 <path d="M305 210H435V140Q370 128 305 140Z" class="sunk"/>
 <circle cx="309" cy="104" r="8" class="badsoft"/>
 <circle cx="431" cy="104" r="8" class="badsoft"/>
 <circle cx="309" cy="146" r="8" class="badsoft"/>
 <circle cx="431" cy="146" r="8" class="badsoft"/>
 <text x="370" y="80" text-anchor="middle" class="t3">กระดูกจาง</text>
 <text x="370" y="180" text-anchor="middle" class="t3">erosion ที่ขอบ</text>
 <path d="M550 40H680V110Q615 124 550 110Z" class="c1soft"/>
 <path d="M550 210H680V140Q615 128 550 140Z" class="c1soft"/>
 <circle cx="570" cy="172" r="16" class="badsoft"/>
 <path d="M550 152L540 146" class="lnbad"/>
 <path d="M550 192L540 198" class="lnbad"/>
 <ellipse cx="514" cy="172" rx="22" ry="28" class="misssoft"/>
 <text x="514" y="176" text-anchor="middle" class="t3">tophus</text>
 <text x="630" y="176" text-anchor="middle" class="t3">หลุม</text>
 <text x="10" y="240" class="t2">• osteophyte (ปลายแหลมแดง)</text>
 <text x="10" y="260" class="t2">• subchondral sclerosis/cyst</text>
 <text x="10" y="280" class="t2">• JSN ไม่สม่ำเสมอ (medial)</text>
 <text x="10" y="300" class="t3">ไม่มี osteopenia</text>
 <text x="260" y="240" class="t2">• marginal erosion (ขอบข้อ)</text>
 <text x="260" y="260" class="t2">• periarticular osteopenia (จาง)</text>
 <text x="260" y="280" class="t2">• JSN สม่ำเสมอทั้งข้อ</text>
 <text x="260" y="300" class="t3">MCP, PIP, wrist, ulnar styloid</text>
 <text x="500" y="240" class="t2">• punched-out erosion</text>
 <text x="500" y="260" class="t2">• overhanging edge</text>
 <text x="500" y="280" class="t2">• lumpy soft tissue (tophi)</text>
 <text x="500" y="300" class="t3">joint space คงอยู่ได้นาน (เสริม)</text>
</svg>''', "ภาพ schematic ของข้อ: OA สร้างกระดูกเพิ่ม (osteophyte, sclerosis) · RA กัดกร่อนขอบข้อและกระดูกจาง · gout กัดเป็นหลุมมีขอบยื่นข้าง tophus")

S4 = sec("rheum-05-04", "Osteoarthritis (OA)",
    "ปวดเมื่อใช้ พักแล้วดีขึ้น · crepitus · AM stiffness < 30 นาที · varus · อสมมาตร · DIP ได้ · X-ray osteophyte, subchondral sclerosis/cyst, JSN ไม่สม่ำเสมอ · LSM + quadriceps → paracetamol/NSAID → IA steroid → joint replacement", minutes=8,
    source=f"{D} หน้า 132–144", nl=["2.3.13(5)", "B5.2.7(1)", "3.2.5"],
    md='''
### นิยามและกลไก
- โรคข้อเสื่อมจาก **กระดูกอ่อนผิวข้อสึก** + กระดูกใต้ผิวข้อปรับตัว (sclerosis, cyst, osteophyte) · ไม่ใช่การอักเสบทั้งตัว → **ไม่มีไข้ ESR ปกติ** (กลไกเสริม)
- ปัจจัยเสี่ยง (เสริม): อายุมาก หญิง อ้วน การบาดเจ็บข้อเดิม ใช้งานข้อหนัก

### อาการ (สไลด์หน้า 132)
- **ปวดระหว่าง/หลังใช้งาน ดีขึ้นเมื่อพัก**
- **Crepitus** เมื่อขยับข้อ
- **Morning stiffness < 30 นาที** (มักไม่กี่นาที)
- **Varus deformity** (ขาโก่ง genu varum เพราะ medial compartment สึกก่อน)
- **อสมมาตร** · **เป็นที่ DIP ได้** (Heberden node) และ PIP (Bouchard node — เสริม) — **RA จะไม่มี DIP**
- ข้อที่พบบ่อย (เสริม): เข่า สะโพก กระดูกสันหลัง DIP PIP **1st CMC** — ไม่ค่อยเป็น MCP ข้อมือ ข้อศอก ไหล่

### X-ray (สไลด์หน้า 132–133)
- **Osteophyte** · **subchondral sclerosis / cyst** · **joint space narrowing ไม่สม่ำเสมอ**
- Kellgren–Lawrence grade 0–4 (สไลด์หน้า 133): 1 = สงสัย osteophyte · 2 = osteophyte ชัด · 3 = JSN ปานกลาง · 4 = JSN มาก sclerosis ข้อผิดรูป (รายละเอียดเกรดเป็นเสริม)
- โจทย์ hand OA "ควรส่งตรวจอะไร" → **film both hands** (RF, ANA, ESR, anti-CCP ไม่ช่วย)

[[fig:rheum-05-04-f1]]

### การรักษา (สไลด์หน้า 134)

| ขั้น | วิธี |
|---|---|
| 1. ไม่ใช้ยา (ทุกราย) | **LSM**, **quadriceps exercise**, **ลดน้ำหนัก** · ใช้ไม้เท้า (เสริม) |
| 2. ยา | **paracetamol** → **topical NSAID / oral NSAID** → **opioid** (เช่น tramadol) |
| 3. ฉีดเข้าข้อ | **intra-articular steroid** (ช่วยช่วงสั้นเมื่อมีน้ำในข้อ) |
| 4. ผ่าตัด | **joint replacement** เมื่อ **conservative ล้มเหลว** |

> Glucosamine ไม่ได้อยู่ในสไลด์และหลักฐานไม่ชัด — ในโจทย์ไม่ใช่คำตอบ (สไลด์หน้า 139–140 เฉลย lifestyle modification) · ผู้ป่วยที่ใช้ยาลดความดัน/โรคไต → **paracetamol** ปลอดภัยกว่า NSAID (สไลด์หน้า 143–144)
''',
    figs=[F_XR],
    pearls=[
        "OA: ปวดเมื่อใช้ ดีขึ้นเมื่อพัก · crepitus · stiffness < 30 นาที · varus",
        "OA เป็น DIP ได้ (Heberden) · RA ไม่เป็น DIP",
        "X-ray OA: osteophyte, subchondral sclerosis/cyst, JSN ไม่สม่ำเสมอ",
        "Tx: LSM + quadriceps + ลดน้ำหนัก → paracetamol/NSAID → IA steroid → TKA",
        "ผู้ป่วยกิน ACEI/โรคไต → paracetamol ก่อน NSAID",
    ],
    items=[
        mcq("RHEUM-05-04-1",
            "A 68-year-old woman has had chronic pain in both knees for 10 years. Morning stiffness lasts less than 10 minutes. Examination shows genu varum and crepitation of both knees. What is the most likely diagnosis?",
            "Osteoarthritis",
            ["Septic arthritis", "Rheumatoid arthritis", "Gouty arthritis", "Lateral collateral ligament injury"],
            kind="old", src=OLD,
            explain='''หญิงสูงอายุ ปวดเข่าเรื้อรัง **stiffness < 10 นาที + genu varum + crepitus** = **OA** (สไลด์หน้า 132, 135–136)
- Septic arthritis เป็นเฉียบพลัน มีไข้ ข้อเดียว
- RA มี AM stiffness > 30 นาที เป็นข้อเล็กมือสมมาตร
- Gouty arthritis เป็นการอักเสบเฉียบพลันเป็นพัก ๆ (1st MTP)
- LCL injury มีประวัติบาดเจ็บ และทดสอบ varus stress แล้วหลวม ไม่ใช่ข้อเสื่อมสองข้าง''',
            pearl="ปวดเข่าเรื้อรัง + stiffness สั้น + varus + crepitus = OA", topic="OA diagnosis",
            ref=[f"{D} หน้า 132, 135–136"], nl=["2.3.13(5)"]),
        mcq("RHEUM-05-04-2",
            "A 70-year-old woman has had persistent right knee pain for 2 years. The pain worsens with weight-bearing and walking and improves with rest. She reports brief morning stiffness and intermittent swelling of the knee. Examination shows crepitus and a positive ballottement test at the right knee without signs of acute inflammation. What is the most likely diagnosis?",
            "Osteoarthritis",
            ["Rheumatoid arthritis", "Reactive arthritis", "Gout", "Pseudogout"],
            kind="old", src=OLD,
            explain='''ปวดเมื่อ **ลงน้ำหนัก/เดิน ดีขึ้นเมื่อพัก** + crepitus + มีน้ำในข้อเป็นพัก ๆ แต่ **ไม่มีการอักเสบเฉียบพลัน** = **OA** (น้ำไขข้อเป็นแบบ non-inflammatory)
- RA เป็นหลายข้อสมมาตร stiffness นาน
- Reactive arthritis เป็นเฉียบพลันหลังติดเชื้อ
- Gout เป็น attack เฉียบพลัน บวมแดงร้อน แล้วหายสนิทระหว่าง attack
- Pseudogout เป็นการอักเสบเฉียบพลันของเข่า/ข้อมือ — แม้ CPPD เรื้อรังเลียนแบบ OA ได้ แต่ภาพนี้ตรงกับ OA มากที่สุด''',
            pearl="Mechanical knee pain + effusion ไม่อักเสบ = OA", topic="OA diagnosis",
            ref=[f"{D} หน้า 137–138"], nl=["2.3.13(5)"]),
        mcq("RHEUM-05-04-3",
            "A 70-year-old woman has right knee pain without red-flag symptoms. Examination shows palpable osteophytes with pain at the medial joint line and no limitation of range of motion. What is the most appropriate management?",
            "Lifestyle modification with quadriceps exercise and weight control",
            ["Oral glucosamine", "Opioid", "Arthroplasty", "Intra-articular glucosamine"],
            kind="old", src=OLD,
            explain='''OA ระยะต้น ยังขยับข้อได้เต็ม → เริ่มด้วย **conservative: lifestyle modification, quadriceps exercise, ลดน้ำหนัก** (สไลด์หน้า 134, 139–140: "try conservative tx ก่อน")
- Glucosamine ชนิดกินหลักฐานไม่ชัดและไม่อยู่ในแนวทางของสไลด์
- Opioid เป็นขั้นท้าย ๆ ของยาแก้ปวด ไม่ใช่ขั้นแรก
- Arthroplasty ทำเมื่อ conservative ล้มเหลว ข้อผิดรูปหรือทำงานไม่ได้
- ไม่มีการฉีด glucosamine เข้าข้อเป็นมาตรฐาน''',
            pearl="OA ระยะต้น → LSM + quadriceps + ลดน้ำหนักก่อน", topic="OA treatment",
            ref=[f"{D} หน้า 134, 139–140"], nl=["2.3.13(5)"]),
        mcq("RHEUM-05-04-4",
            "A 60-year-old woman has had tenderness of the finger joints of both hands for many years. Morning stiffness lasts 1–2 minutes. Examination shows no signs of inflammation. What is the most appropriate investigation?",
            "Plain radiographs of both hands",
            ["Rheumatoid factor", "Antinuclear antibody", "Erythrocyte sedimentation rate", "Anti-cyclic citrullinated peptide antibody"],
            kind="old", src=OLD,
            explain='''ปวดนิ้วเรื้อรังหลายปี **stiffness 1–2 นาที ไม่มีการอักเสบ** = **hand OA** → ยืนยันด้วย **X-ray มือทั้งสองข้าง** (osteophyte, JSN) (สไลด์หน้า 141–142)
- RF และ anti-CCP ใช้เมื่อสงสัย RA (stiffness > 30 นาที synovitis) — ในผู้สูงอายุ RF บวกปลอมได้
- ANA ใช้คัดกรอง SLE/CTD
- ESR ไม่จำเพาะ และปกติใน OA''',
            pearl="Hand pain + stiffness สั้น ไม่อักเสบ → film both hands", topic="Hand OA",
            ref=[f"{D} หน้า 141–142"], nl=["2.3.13(5)", "3.2.5"]),
        mcq("RHEUM-05-04-5",
            "A 56-year-old woman has had intermittent finger pain for 2 years, worse briefly after waking and in the evening. She has hypertension treated with enalapril. Examination shows bony swelling of the 2nd–5th DIP joints of both hands. What is the most appropriate management?",
            "Paracetamol",
            ["Glucosamine sulfate", "Allopurinol", "Indomethacin", "Naproxen"],
            kind="old", src=OLD,
            explain='''**DIP บวมแข็ง (Heberden node)** + stiffness สั้น = **hand OA** (RA ไม่เป็น DIP) → ยาแก้ปวดขั้นแรกที่ปลอดภัยคือ **paracetamol** โดยเฉพาะผู้ป่วยที่ใช้ **ACEI** (NSAID + ACEI เสี่ยงไตเสื่อม ความดันสูงขึ้น) (สไลด์หน้า 143–144)
- Glucosamine หลักฐานไม่ชัด
- Allopurinol เป็นยาลด uric acid ใช้กับ gout
- Indomethacin และ naproxen เป็น oral NSAID ที่มีผลเสียต่อไตและความดันเมื่อใช้ร่วม ACEI (topical NSAID ใช้ได้ดีใน hand OA — เสริม)''',
            pearl="Hand OA + ใช้ ACEI → paracetamol", topic="OA treatment",
            ref=[f"{D} หน้า 134, 143–144"], nl=["2.3.13(5)", "B3.4(7)"]),
    ])

LECTURE = lecture("05", "Septic arthritis & osteoarthritis", "acute monoarthritis · Gram stain-guided antibiotics · gonococcal/DGI · OA",
    objectives=[
        "เข้าหา acute monoarthritis ด้วย arthrocentesis และแปลผล septic/crystal/hemarthrosis",
        "รู้เชื้อก่อโรคตามอายุและปัจจัยเสี่ยง และเลือกยาตาม Gram stain รวมถึงกรณี IVDU",
        "จัดการ septic arthritis ที่ไม่ตอบสนอง (drainage ก่อนเปลี่ยนยา)",
        "วินิจฉัยและรักษา DGI (triad + ceftriaxone + azithromycin)",
        "วินิจฉัย OA จากอาการและ X-ray และเลือกการรักษาเป็นขั้น",
    ],
    sections=[S1, S2, S3, S4])
