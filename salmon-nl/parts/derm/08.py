from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Dermato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 08-01 Viral exanthem
F_FEVER = fig("derm-08-01-f1", "ไข้กับผื่น: measles vs rubella vs roseola", '''<svg viewBox="0 0 740 360">
 <text x="20" y="22" class="tb">วันที่</text>
 <text x="190" y="22" text-anchor="middle" class="t3">D1</text>
 <text x="260" y="22" text-anchor="middle" class="t3">D2</text>
 <text x="330" y="22" text-anchor="middle" class="t3">D3</text>
 <text x="400" y="22" text-anchor="middle" class="t3">D4</text>
 <text x="470" y="22" text-anchor="middle" class="t3">D5</text>
 <text x="540" y="22" text-anchor="middle" class="t3">D6</text>
 <text x="610" y="22" text-anchor="middle" class="t3">D7</text>
 <text x="680" y="22" text-anchor="middle" class="t3">D8</text>
 <rect x="10" y="34" width="720" height="100" rx="10" class="sunk"/>
 <text x="20" y="58" class="tb">Measles</text>
 <text x="20" y="76" class="t3">ไข้สูง + 3C</text>
 <rect x="155" y="46" width="350" height="16" rx="4" class="bad"/>
 <text x="330" y="58" text-anchor="middle" class="tw">ไข้สูง cough coryza conjunctivitis</text>
 <rect x="225" y="70" width="140" height="16" rx="4" class="c1soft"/>
 <text x="295" y="82" text-anchor="middle" class="t3">Koplik D2–3</text>
 <rect x="365" y="94" width="300" height="16" rx="4" class="badsoft"/>
 <text x="515" y="106" text-anchor="middle" class="t3">MP rash D3–4 หัว → เท้า</text>
 <text x="660" y="128" text-anchor="end" class="t3">หายทิ้งรอยดำ</text>
 <rect x="10" y="142" width="720" height="92" rx="10" class="sunk"/>
 <text x="20" y="166" class="tb">Rubella</text>
 <text x="20" y="184" class="t3">ไข้ต่ำ ± ไม่มี</text>
 <rect x="155" y="154" width="160" height="16" rx="4" class="misssoft"/>
 <text x="235" y="166" text-anchor="middle" class="t3">ไข้ต่ำ</text>
 <rect x="155" y="178" width="210" height="16" rx="4" class="badsoft"/>
 <text x="260" y="190" text-anchor="middle" class="t3">ผื่นวันเดียวกับไข้ หัว → เท้า</text>
 <rect x="155" y="202" width="420" height="16" rx="4" class="c2soft"/>
 <text x="365" y="214" text-anchor="middle" class="t3">LN หลังหู ท้ายทอย · Forchheimer · ปวดข้อ (ผู้ใหญ่)</text>
 <text x="660" y="228" text-anchor="end" class="t3">ไม่ทิ้งรอยดำ</text>
 <rect x="10" y="242" width="720" height="100" rx="10" class="sunk"/>
 <text x="20" y="266" class="tb">Roseola</text>
 <text x="20" y="284" class="t3">&lt; 2 ปี HHV-6/7</text>
 <rect x="155" y="254" width="210" height="16" rx="4" class="bad"/>
 <text x="260" y="266" text-anchor="middle" class="tw">ไข้สูง 3 วัน เด็กยังเล่นได้</text>
 <path d="M365 270V296" class="lnf"/>
 <text x="372" y="292" class="t3">ไข้ลง</text>
 <rect x="365" y="300" width="210" height="16" rx="4" class="badsoft"/>
 <text x="470" y="312" text-anchor="middle" class="t3">ผื่นขึ้น ลำตัว → หน้า แขนขา</text>
 <text x="660" y="334" text-anchor="end" class="t3">ไข้ลงแล้วผื่นขึ้น = จุดจำ</text>
</svg>''', "ความสัมพันธ์ไข้กับผื่นแยกสามโรคได้: measles ผื่นขึ้นตอนไข้สูงสุด · rubella ผื่นพร้อมไข้ต่ำ · roseola ผื่นขึ้นหลังไข้ลง")

S1 = sec("derm-08-01", "Viral exanthem: measles, rubella, roseola, fifth disease, HFMD",
    "Measles = ไข้สูง 3C → Koplik D2–3 → ผื่น D3–4 หัว→เท้า ทิ้งรอยดำ, vitamin A · rubella = ไข้ต่ำ ผื่นวันเดียวกับไข้ LN หลังหู Forchheimer · roseola = ไข้ 3 วันลงแล้วผื่นขึ้น · 5th = slapped cheek · HFMD = ตุ่มปาก ฝ่ามือฝ่าเท้า",
    minutes=10, source=f"{D} หน้า 262–272", nl=["2.3.1(23)", "B4.2.2(7)", "2.3.16-3(1)"],
    md='''
### Measles (หัด, rubeola)

- **Measles (rubeola) virus** · **airborne** (ติดง่ายที่สุด)
- **ไข้สูง + 3C: cough, conjunctivitis, coryza**
- **ไข้วันที่ 2–3: Koplik spots** — จุดขาวเทาเล็กบนพื้นแดงที่กระพุ้งแก้มตรงฟันกราม (เสริม)
- **ไข้วันที่ 3–4: maculopapular rash เริ่มที่หน้า/ไรผม → ลงไปเท้า** ผื่นรวมกันเป็นปื้น ขณะที่ไข้ยังสูง
- **หายแล้วทิ้งรอยดำ (resolution with hyperpigmentation)** + ขุยละเอียด
- **Tx: supportive + vitamin A** · **Prevention: MMR**
- ภาวะแทรกซ้อน (เสริม): ปอดอักเสบ (สาเหตุตายหลัก), otitis media, encephalitis, SSPE

### Rubella (หัดเยอรมัน)

- **Rubella virus** · **respiratory droplet**
- **± ไข้ต่ำ** · **MP rash หัว → เท้า มักขึ้นวันเดียวกับไข้** (ลามเร็วหายใน 3 วัน (เสริม))
- **Lymphadenopathy** — **หลังหู (post-auricular), ท้ายทอย (suboccipital), posterior cervical** (เสริม)
- **Forchheimer spots = petechiae บนเพดานอ่อน**
- ผู้ใหญ่ (หญิง) มี **polyarthralgia/arthritis** (เสริม)
- **หายโดยไม่ทิ้งรอยดำ**
- **Tx: supportive** · **Prevention: MMR** · อันตรายสูงสุดคือ **congenital rubella syndrome** ถ้าติดช่วงตั้งครรภ์ไตรมาสแรก (เสริม)

### Roseola infantum (exanthem subitum, ไข้ผื่นกุหลาบ)

- **อายุ < 2 ปี** · **HHV-6, HHV-7** · respiratory droplet
- **ไข้สูง 3 วัน** (เด็กยังดูดี เล่นได้ อาจชักจากไข้ (เสริม))
- **ไข้ลงแล้วผื่นขึ้น**: MP rash สีชมพูเริ่ม **ลำตัว → หน้า แขนขา**
- **Tx: supportive**

[[fig:derm-08-01-f1]]

### Erythema infectiosum (fifth disease)

- **อายุ 4–10 ปี** · **parvovirus B19** · respiratory droplet
- **Slapped cheek** (แก้มแดงสดสองข้างเหมือนโดนตบ เว้นร่องจมูก-ปาก) → ตามด้วย **MP rash / ลายร่างแห (reticular, lacy) ที่ลำตัว แขนขา**
- **ผู้ใหญ่มักไม่มี slapped cheek แต่มีปวดข้อ** (มือ ข้อมือ เข่า สมมาตร)
- **Tx: supportive** · ระวัง aplastic crisis ในผู้ป่วย hemolytic anemia (thalassemia, sickle cell) และ hydrops fetalis ในหญิงตั้งครรภ์ (เสริม)

### Hand, foot, and mouth disease (HFMD)

- **อายุ < 5 ปี** · **Coxsackievirus A16, enterovirus 71** · respiratory droplet + **fecal-oral**
- **Vesicles และแผลในปากและรอบปาก** + **vesicle รูปรี/MP rash ที่ฝ่ามือ ฝ่าเท้า** (ก้นด้วย (เสริม))
- **ภาวะแทรกซ้อน (EV71): meningitis, encephalitis (brainstem), myocarditis, pulmonary hemorrhage/edema**
- **Tx: supportive**

| | Measles | Rubella | Roseola | 5th disease | HFMD |
|---|---|---|---|---|---|
| เชื้อ | measles virus | rubella virus | HHV-6/7 | parvovirus B19 | coxsackie A16, EV71 |
| อายุ | ทุกวัย | เด็ก-วัยรุ่น | **< 2 ปี** | **4–10 ปี** | **< 5 ปี** |
| ไข้ | **สูง + 3C** | ต่ำ/ไม่มี | **สูง 3 วัน** | ต่ำ | ต่ำ-ปานกลาง |
| จุดจำ | **Koplik** | **Forchheimer, LN หลังหู** | **ไข้ลงผื่นขึ้น** | **slapped cheek** | **ปาก + มือ + เท้า** |
| ผื่นเริ่ม | หน้า → เท้า | หน้า → เท้า | ลำตัว → หน้า | แก้ม → ลำตัว (ลายลูกไม้) | ฝ่ามือ ฝ่าเท้า |
| หลังหาย | **รอยดำ** | ไม่มี | ไม่มี | ไม่มี | ไม่มี |
''',
    figs=[F_FEVER],
    pearls=[
        "Measles: ไข้สูง + 3C → Koplik D2–3 → ผื่น D3–4 หัว→เท้า ทิ้งรอยดำ · ให้ vitamin A",
        "Rubella: ไข้ต่ำ ผื่นวันเดียวกับไข้ LN หลังหู Forchheimer (petechiae เพดานอ่อน)",
        "Roseola: < 2 ปี ไข้สูง 3 วัน ไข้ลงแล้วผื่นขึ้น",
        "5th disease: slapped cheek + ลายลูกไม้ · ผู้ใหญ่ปวดข้อ",
        "HFMD: < 5 ปี ตุ่มปาก + ฝ่ามือฝ่าเท้า · EV71 → encephalitis, myocarditis, pulmonary hemorrhage",
    ],
    items=[
        mcq("DERM-08-01-1", """A 23-year-old man has had a rash for 2 days that started on his face and upper trunk and spread downward. Three days before the rash, he had fever, sore throat and pain in multiple joints. He denies recent sexual activity. Temperature 39°C. Examination shows petechiae on the soft palate, a fine maculopapular rash on the body, and lymphadenopathy in the posterior auricular, neck and posterior cervical regions. There is no conjunctivitis or cough. What is the most likely diagnosis?""",
            "Rubella", ["Measles", "Infectious mononucleosis", "Acute retroviral syndrome", "Disseminated gonococcal infection"],
            explain="""ผื่น MP หัว→เท้า + **petechiae บนเพดานอ่อน (Forchheimer spots)** + **ต่อมน้ำเหลืองหลังหูและ posterior cervical** + ปวดหลายข้อในผู้ใหญ่ = **rubella** (สไลด์หน้า 264–265, 271–272)
- Measles ต้องมีไข้สูงร่วมกับ 3C (ไอ น้ำมูก ตาแดง) และ Koplik spots ซึ่งไม่มีในโจทย์
- Infectious mononucleosis มี petechiae ที่เพดานและ posterior cervical LN ได้ แต่เด่นที่ทอนซิลอักเสบมีหนอง ม้ามโต และผื่นมักขึ้นหลังได้ amoxicillin
- Acute retroviral syndrome ต้องมีความเสี่ยง (เพศสัมพันธ์ เข็ม) ซึ่งผู้ป่วยปฏิเสธ
- Disseminated gonorrhea เป็นตุ่มหนองเลือดออกไม่กี่ตุ่มที่แขนขา + tenosynovitis และต้องมีประวัติทางเพศ""",
            pearl="Forchheimer + LN หลังหู + ปวดข้อ = rubella",
            topic="Rubella", ref=[f"{D} หน้า 271–272"], nl=["2.3.1(23)"], kind="old", src=OLD),
        mcq("DERM-08-01-2", """A 4-year-old unvaccinated boy has had high fever, cough, coryza and red watery eyes for 3 days. Today a blotchy erythematous maculopapular rash began at the hairline and behind the ears and is spreading downward. Tiny gray-white spots on a red base are seen on the buccal mucosa opposite the molars. Besides supportive care, which treatment should be given?""",
            "Vitamin A", ["Oral acyclovir", "Oral amoxicillin", "Intravenous immunoglobulin", "Oral prednisolone"],
            explain="""ไข้สูง + **3C** + **Koplik spots** + ผื่นเริ่มไรผม → ลงล่าง = **measles** → **supportive + vitamin A** (ลดความรุนแรงและอัตราตาย) (สไลด์หน้า 262–263)
- Acyclovir ใช้กับ HSV/VZV ไม่ออกฤทธิ์ต่อ measles virus
- Amoxicillin ใช้เมื่อมีติดเชื้อแบคทีเรียแทรก (เช่น หูชั้นกลางอักเสบ ปอดอักเสบ) ไม่ใช่ทุกราย
- IVIG ใช้ป้องกันหลังสัมผัสในคนเสี่ยงสูง (ทารก ภูมิต่ำ) ไม่ใช่การรักษาเมื่อป่วยแล้ว (เสริม)
- Prednisolone ไม่มีบทบาทและกดภูมิ""",
            pearl="Measles → supportive + vitamin A",
            topic="Measles", ref=[f"{D} หน้า 262–263"], nl=["2.3.1(23)"]),
        mcq("DERM-08-01-3", """A 14-month-old girl had a temperature of 39.5–40°C for 3 days but remained playful. On day 4 the fever resolved abruptly, and a few hours later a rose-pink maculopapular rash appeared on her trunk and then spread to the face and arms. What is the most likely causative agent?""",
            "Human herpesvirus 6", ["Parvovirus B19", "Rubella virus", "Measles virus", "Coxsackievirus A16"],
            explain="""เด็ก **< 2 ปี** ไข้สูง 3 วัน **ไข้ลงแล้วผื่นขึ้น** เริ่มลำตัว → หน้า แขน = **roseola infantum** จาก **HHV-6** (หรือ HHV-7) (สไลด์หน้า 266)
- Parvovirus B19 ทำให้เกิด slapped cheek ในเด็กวัยเรียน 4–10 ปี
- Rubella ผื่นขึ้นวันเดียวกับไข้ต่ำ เริ่มที่หน้า
- Measles ผื่นขึ้นขณะไข้ยังสูงพร้อม 3C และเริ่มที่หน้า
- Coxsackie A16 ทำให้เกิด HFMD มีแผลในปากและตุ่มที่ฝ่ามือฝ่าเท้า""",
            pearl="< 2 ปี ไข้ 3 วัน ไข้ลงผื่นขึ้น = roseola (HHV-6)",
            topic="Roseola", ref=[f"{D} หน้า 266"], nl=["2.3.1(23)"]),
        mcq("DERM-08-01-4", """A 7-year-old boy has bright red cheeks that look as if he had been slapped, sparing the nasolabial folds. Two days later a lacy, reticular erythematous rash appears on his arms and trunk. His 35-year-old mother then develops symmetric pain and swelling of the small joints of both hands without a rash. What is the causative agent?""",
            "Parvovirus B19", ["Human herpesvirus 6", "Streptococcus pyogenes", "Rubella virus", "Enterovirus 71"],
            explain="""**Slapped cheek** ตามด้วยผื่นลายลูกไม้ (reticular) ในเด็กวัยเรียน และผู้ใหญ่มี **ปวดข้อสมมาตรโดยไม่มี slapped cheek** = **erythema infectiosum (fifth disease)** จาก **parvovirus B19** (สไลด์หน้า 269)
- HHV-6 ทำให้เกิด roseola ในเด็ก < 2 ปี ผื่นขึ้นหลังไข้ลง
- S. pyogenes ทำให้เกิด scarlet fever ผื่นกระดาษทรายและ perioral pallor ไม่ใช่แก้มแดงแบบโดนตบ
- Rubella ทำให้ปวดข้อในผู้ใหญ่ได้เช่นกัน แต่ในเด็กเป็นผื่น MP หัว→เท้าพร้อม LN หลังหู ไม่มี slapped cheek
- EV71 ทำให้เกิด HFMD""",
            pearl="Slapped cheek + ลายลูกไม้ + แม่ปวดข้อ = parvovirus B19",
            topic="5th disease", ref=[f"{D} หน้า 269"], nl=["2.3.1(23)"]),
        mcq("DERM-08-01-5", """A 3-year-old boy in a daycare outbreak has low-grade fever, painful oral ulcers on the tongue and buccal mucosa, and small oval grayish vesicles on the palms and soles. On day 3 he develops myoclonic jerks, ataxia and tachypnea. Which pathogen is most strongly associated with these neurologic and cardiopulmonary complications?""",
            "Enterovirus 71", ["Coxsackievirus A16", "Herpes simplex virus-1", "Varicella-zoster virus", "Parvovirus B19"],
            explain="""แผลในปาก + ตุ่มน้ำรูปรีที่ฝ่ามือฝ่าเท้า = **HFMD** · ภาวะแทรกซ้อน **encephalitis (brainstem — myoclonus, ataxia), myocarditis, pulmonary hemorrhage** สัมพันธ์กับ **enterovirus 71** มากที่สุด (สไลด์หน้า 270)
- Coxsackie A16 ทำให้เกิด HFMD ได้เช่นกัน แต่มักไม่รุนแรง
- HSV-1 ทำให้เกิด gingivostomatitis ที่เหงือกบวมมีเลือด ไม่มีตุ่มที่ฝ่ามือฝ่าเท้า
- VZV เป็นผื่นหลายระยะเริ่มที่ลำตัว ไม่ได้จำกัดที่ปาก มือ เท้า
- Parvovirus B19 ทำให้เกิด slapped cheek""",
            pearl="HFMD รุนแรง (encephalitis, myocarditis, pulmonary hemorrhage) = EV71",
            topic="HFMD", ref=[f"{D} หน้า 270"], nl=["2.3.1(23)"]),
    ])

# ---------------------------------------------------------------- 08-02 Scarlet fever
S2 = sec("derm-08-02", "Scarlet fever",
    "S. pyogenes (erythrogenic toxin) · 5–15 ปี · ไข้ คออักเสบ → ผื่นกระดาษทราย, perioral pallor, strawberry tongue, Pastia's lines, ลอกที่ฝ่ามือฝ่าเท้า · throat culture · penicillin V/amoxicillin 10 วัน หรือ azithromycin 5 วัน",
    minutes=6, source=f"{D} หน้า 273–275, 281–284", nl=["2.3.1(23)", "2.1.50"],
    md='''
### ใครเป็น / เชื้อ

- **เด็กอายุ 5–15 ปี** · **S. pyogenes** (group A strep) ที่สร้าง pyrogenic (erythrogenic) exotoxin (เสริม)
- **Prodrome: ไข้, pharyngitis (คออักเสบ)**

### สิ่งที่เห็น

| สัญญาณ | ลักษณะ |
|---|---|
| **Sandpaper-like rash** | **ผื่นแดงละเอียด (fine erythematous MP rash) ลูบแล้วสากเหมือนกระดาษทราย** กดจาง อยู่ ~ **1 สัปดาห์** · เริ่มคอ-อก แล้วกระจาย (เสริม) |
| **Perioral (circumoral) pallor** | รอบปากซีด ขณะที่แก้มแดง |
| **Strawberry tongue** | ลิ้นแดง ตุ่มรับรสโต (ช่วงแรกเป็น white strawberry (เสริม)) |
| **Pastia's lines** | **จุดเลือดออกเป็นเส้นตามข้อพับ** (ข้อพับแขน รักแร้) |
| **Cervical lymphadenopathy** | |
| **Desquamation** | **ลอกที่ฝ่ามือฝ่าเท้า** ช่วงพักฟื้น |

### Investigation และภาวะแทรกซ้อน

- **Throat culture (confirm diagnosis)** · rapid strep antigen test
- **Complications: APSGN, rheumatic fever**

### การรักษา

- **Penicillin V หรือ amoxicillin นาน 10 วัน** (ครบ 10 วันเพื่อป้องกัน rheumatic fever)
- แพ้ penicillin: **azithromycin 5 วัน**

> Strawberry tongue พบได้ใน scarlet fever, Kawasaki disease และ TSS — แยก Kawasaki ด้วยไข้ ≥ 5 วัน ตาแดงไม่มีขี้ตา ปากแห้งแตก มือเท้าบวม และไม่ตอบสนองต่อยาปฏิชีวนะ (เสริม)
''',
    pearls=[
        "Scarlet fever = คออักเสบ + ผื่นกระดาษทราย + perioral pallor + strawberry tongue + Pastia's lines",
        "เด็ก 5–15 ปี · S. pyogenes · ยืนยันด้วย throat culture / rapid strep",
        "Penicillin V หรือ amoxicillin 10 วัน · แพ้ → azithromycin 5 วัน",
        "ภาวะแทรกซ้อน APSGN, rheumatic fever",
    ],
    items=[
        mcq("DERM-08-02-1", """A 10-year-old girl has a sore throat and a diffuse rash that has started to peel. Examination shows a diffuse, fine, erythematous rash on her trunk and extremities that feels rough like sandpaper, with circumoral pallor and linear petechial streaks in the antecubital fossae. What is the most likely diagnosis?""",
            "Scarlet fever", ["Measles", "Kawasaki disease", "Staphylococcal scalded skin syndrome", "Toxic shock syndrome"],
            explain="""คออักเสบ + **ผื่นกระดาษทราย + circumoral pallor + Pastia's lines** และเริ่มลอก = **scarlet fever** (สไลด์หน้า 273–274, 281–282)
- Measles มีไข้สูงกับ 3C และ Koplik spots ผื่นเป็นปื้น MP ไม่สากแบบกระดาษทราย
- Kawasaki ต้องมีไข้ ≥ 5 วัน ตาแดงไม่มีขี้ตา ปากแดงแตก มือเท้าบวม
- SSSS เป็นผิวแดงเจ็บแล้วลอกเป็นแผ่นใหญ่ Nikolsky บวก ในทารก ไม่มีคออักเสบ
- TSS มีความดันต่ำและอวัยวะล้มเหลว ไม่ใช่เด็กที่มีแค่คออักเสบและผื่น""",
            pearl="Sandpaper rash + perioral pallor + Pastia = scarlet fever",
            topic="Scarlet fever dx", ref=[f"{D} หน้า 281–282"], nl=["2.3.1(23)"], kind="old", src=OLD),
        mcq("DERM-08-02-2", """A 5-year-old boy has had sore throat and fever for 2 days and now a rash. Examination shows a diffuse, erythematous, sandpaper-like rash that blanches with pressure, and a beefy-red tongue with prominent papillae. A rapid streptococcal antigen test is positive. He has no drug allergy. What is the most appropriate treatment?""",
            "Oral amoxicillin for 10 days", ["Oral azithromycin for 3 days", "Oral amoxicillin for 5 days", "Intravenous vancomycin", "Supportive care only"],
            explain="""Scarlet fever (rapid strep บวก + ผื่นกระดาษทราย + strawberry tongue) → **penicillin V หรือ amoxicillin 10 วัน** (azithromycin 5 วันเฉพาะแพ้ penicillin) (สไลด์หน้า 275, 283–284)
- Azithromycin เป็นทางเลือกเมื่อแพ้ penicillin และสไลด์ให้ 5 วัน ไม่ใช่ 3 วัน
- Amoxicillin 5 วันสั้นเกินไปสำหรับการกำจัดเชื้อเพื่อป้องกัน rheumatic fever
- Vancomycin IV เกินจำเป็น S. pyogenes ยังไวต่อ penicillin
- ต้องให้ยาปฏิชีวนะเพื่อป้องกัน rheumatic fever และลดการแพร่เชื้อ""",
            pearl="Scarlet fever → penicillin V/amoxicillin 10 วัน",
            topic="Scarlet fever tx", ref=[f"{D} หน้า 275, 283–284"], nl=["2.3.1(23)"], kind="old", src=OLD),
        mcq("DERM-08-02-3", """Which complication is prevented by completing a full 10-day course of penicillin for streptococcal pharyngitis with scarlet fever, but is NOT reliably prevented by antibiotic therapy after streptococcal skin infection?""",
            "Antibiotics prevent acute rheumatic fever, but not post-streptococcal glomerulonephritis", ["Antibiotics prevent post-streptococcal glomerulonephritis, but not acute rheumatic fever", "Antibiotics prevent both rheumatic fever and glomerulonephritis equally", "Antibiotics prevent neither complication", "Antibiotics prevent only peritonsillar abscess, not rheumatic fever"],
            explain="""ภาวะแทรกซ้อนของ scarlet fever ตามสไลด์คือ **APSGN และ rheumatic fever** (สไลด์หน้า 273) · การให้ penicillin ครบภายใน 9 วันหลังเริ่มคออักเสบ **ป้องกัน rheumatic fever ได้** แต่ **ไม่ป้องกัน APSGN** (เสริม)
- การกลับข้างของสองภาวะนี้ผิด — ยาไม่ป้องกัน APSGN
- ยาไม่ได้ป้องกันทั้งสองอย่างเท่ากัน — APSGN เป็น immune complex ที่เกิดแม้กำจัดเชื้อแล้ว
- ข้อที่บอกว่ายาไม่ป้องกันอะไรเลยผิด เพราะการป้องกัน rheumatic fever เป็นเหตุผลหลักที่ให้ครบ 10 วัน
- Peritonsillar abscess ลดลงได้จากยา แต่ rheumatic fever ก็ป้องกันได้เช่นกัน""",
            pearl="Strep pharyngitis: ATB ป้องกัน RF ได้ ไม่ป้องกัน APSGN",
            topic="Strep complications", ref=[f"{D} หน้า 273"], nl=["2.3.1(23)", "B9.2.2(3)"]),
    ])

# ---------------------------------------------------------------- 08-03 SSSS
S3 = sec("derm-08-03", "Staphylococcal scalded skin syndrome (SSSS)",
    "ทารก/เด็ก < 5 ปี, ผู้ใหญ่ไตเสื่อม/ภูมิต่ำ · exfoliative toxin ของ S. aureus · ไข้ ผิวเจ็บ erythroderma, สะเก็ดรอบปากตา, flaccid blister Nikolsky + ลอกทั่วตัวใน 48 ชม. · ไม่มี mucosa · IV cloxacillin + clindamycin",
    minutes=7, source=f"{D} หน้า 276–278, 285–286", nl=["2.3.12-3(12)", "B4.2.2-3(3)"],
    md='''
### กลไก

- **S. aureus** ติดเชื้อที่จุดหนึ่ง (สะดือ ตา จมูก) → สร้าง **exfoliative (epidermolytic) toxin** → toxin ตัด **desmoglein 1** ที่ชั้น granular → ผิวลอกตื้น (เสริม)
- **ทารกและเด็ก < 5 ปี** · **ผู้ใหญ่ที่ไตเสื่อม/ภูมิต่ำ** — **เพราะไตยังกำจัด toxin ได้ไม่ดี**

### สิ่งที่เห็น

| ระยะ | ลักษณะ |
|---|---|
| Prodrome | **ไข้, ผิวเจ็บ (skin tenderness)** — เด็กร้องเมื่อถูกอุ้ม |
| ผื่น | **erythematous patch → erythroderma** (เริ่มซอกพับ หน้า) |
| หน้า | **สะเก็ดรอบปากและรอบตา (perioral & periocular crusting)** เป็นแฉก |
| ตุ่มน้ำ | **flaccid blisters, Nikolsky +** |
| ลอก | **ลอกเป็นแผ่นทั่วตัวภายใน 48 ชม.** (คล้ายน้ำร้อนลวก) |
| **Mucosa** | **ไม่มี** (ต่างจาก SJS/TEN) |

### Investigation

- **Hemoculture** (ในเด็กมักลบ ผู้ใหญ่มักบวก (เสริม)), culture จากจุดติดเชื้อ (ไม่ใช่จากตุ่มน้ำ ซึ่งปลอดเชื้อ (เสริม))
- **Skin biopsy เมื่อแยกจาก SJS/TEN ไม่ได้** (SSSS แยกตื้นใต้ stratum corneum · TEN epidermis ตายทั้งชั้น)

### การรักษา (สไลด์หน้า 278)

- **MSSA: IV cloxacillin + clindamycin** (clindamycin ยับยั้งการสร้าง toxin)
- **MRSA: IV vancomycin + clindamycin**
- **IV fluid, wound care** (ห้ามให้ steroid (เสริม))
- หายโดยไม่มีแผลเป็น เพราะลอกตื้น (เสริม)

| | SSSS | TEN |
|---|---|---|
| อายุ | ทารก เด็กเล็ก | ผู้ใหญ่ |
| สาเหตุ | toxin S. aureus | ยา |
| Mucosa | **ไม่มี** | **มี (≥ 2)** |
| ระดับลอก | ตื้น (granular layer) | ลึก (ทั้ง epidermis) |
| Target lesion | ไม่มี | dusky target |
| รักษา | anti-staph IV | หยุดยา ICU |
''',
    pearls=[
        "SSSS = ทารก ไข้ ผิวเจ็บ erythroderma สะเก็ดรอบปากตา Nikolsky + ไม่มี mucosa",
        "ลอกทั่วตัวใน 48 ชม. · toxin ตัด desmoglein 1 (ลอกตื้น)",
        "เด็กเล็ก/ไตเสื่อมเสี่ยงเพราะขับ toxin ไม่ดี",
        "MSSA → IV cloxacillin + clindamycin · MRSA → vancomycin + clindamycin",
    ],
    items=[
        mcq("DERM-08-03-1", """A 10-day-old boy has fever, red skin and irritability. For the past few days he has refused feeds and had minimal urine output. Temperature 38.2°C. He cries when touched. Examination shows diffuse tender erythema, radial crusting around the mouth and eyes, superficial skin sloughing and multiple fragile flaccid bullae; the Nikolsky sign is positive. The oral mucosa and conjunctivae are normal. What is the most likely diagnosis?""",
            "Staphylococcal scalded skin syndrome", ["Toxic epidermal necrolysis", "Bullous impetigo", "Neonatal pemphigus", "Epidermolysis bullosa"],
            explain="""ทารก + ไข้ + **ผิวเจ็บ erythroderma** + **สะเก็ดรอบปากตา** + flaccid bullae Nikolsky + และ **ไม่มี mucosa** = **SSSS** (สไลด์หน้า 276–277, 285–286)
- TEN ต้องมี mucosa และส่วนใหญ่เกิดจากยาในผู้ใหญ่
- Bullous impetigo เป็นตุ่มน้ำเฉพาะที่ ไม่ทำให้ erythroderma ทั่วตัวพร้อมไข้
- Neonatal pemphigus ต้องมีแม่เป็น pemphigus และมักมีรอยโรคตั้งแต่แรกคลอด
- Epidermolysis bullosa เป็นโรคพันธุกรรม ตุ่มน้ำเกิดจากการเสียดสีตั้งแต่เกิด ไม่มีไข้และ erythroderma""",
            pearl="ทารก + ผิวเจ็บแดงทั่ว + สะเก็ดรอบปากตา + Nikolsky + ไม่มี mucosa = SSSS",
            topic="SSSS dx", ref=[f"{D} หน้า 285–286"], nl=["2.3.12-3(12)"], kind="old", src=OLD),
        mcq("DERM-08-03-2", """A 3-year-old girl with SSSS following a nasal staphylococcal infection is admitted. She is hemodynamically stable. The local hospital has a low MRSA prevalence. What is the most appropriate antibiotic regimen?""",
            "Intravenous cloxacillin plus clindamycin", ["Intravenous vancomycin alone", "Oral amoxicillin", "Topical mupirocin alone", "Intravenous ceftriaxone plus metronidazole"],
            explain="""SSSS จาก MSSA → **IV cloxacillin + clindamycin** (clindamycin ยับยั้งการสร้าง toxin) + IV fluid และ wound care (สไลด์หน้า 278, 286)
- Vancomycin ใช้กับ MRSA (คู่กับ clindamycin) ไม่ใช่ตัวแรกในพื้นที่ MRSA ต่ำ และเดี่ยว ๆ ไม่กด toxin
- Amoxicillin ถูก penicillinase ของ S. aureus ทำลาย
- Mupirocin ทาไม่ได้รักษาโรคที่เกิดจาก toxin ทั่วร่างกาย
- Ceftriaxone + metronidazole เป็นสูตรสำหรับ intra-abdominal/anaerobe ไม่ใช่ anti-staphylococcal ที่เหมาะสม""",
            pearl="SSSS (MSSA) → IV cloxacillin + clindamycin",
            topic="SSSS tx", ref=[f"{D} หน้า 278"], nl=["2.3.12-3(12)"]),
        mcq("DERM-08-03-3", """A 70-year-old man on hemodialysis has fever, painful generalized erythema and large areas of superficial flaccid peeling with a positive Nikolsky sign. There are no mucosal lesions, no target lesions and no new medications. Blood cultures grow Staphylococcus aureus. Why is he at risk of this toxin-mediated condition despite being an adult?""",
            "Impaired renal clearance of the exfoliative toxin", ["HLA-B1502 genotype", "Antibodies against desmoglein 3", "IgE-mediated mast cell degranulation", "Superantigen-mediated T-cell activation only"],
            explain="""นี่คือ SSSS ในผู้ใหญ่ — สไลด์ระบุว่าเกิดใน **ผู้ใหญ่ที่การทำงานของไตบกพร่อง/ภูมิต่ำ** **เนื่องจากไตยังกำจัด toxin ได้ไม่ดี** (สไลด์หน้า 276)
- HLA-B1502 เป็นปัจจัยเสี่ยงของ SJS/TEN จากยา ซึ่งผู้ป่วยไม่มียาใหม่และไม่มี mucosa
- Anti-desmoglein 3 antibody เป็นกลไกของ pemphigus vulgaris ไม่ใช่การติดเชื้อ
- IgE/mast cell เป็นกลไกของ urticaria/anaphylaxis
- Superantigen กระตุ้น T cell เป็นกลไกของ TSS ซึ่งเด่นที่ shock และอวัยวะล้มเหลว ไม่ใช่ผิวลอกตื้น Nikolsky +""",
            pearl="SSSS ในผู้ใหญ่ = ไตเสื่อม (ขับ toxin ไม่ได้) หรือภูมิต่ำ",
            topic="SSSS adult", ref=[f"{D} หน้า 276"], nl=["2.3.12-3(12)"]),
    ])

# ---------------------------------------------------------------- 08-04 TSS
S4 = sec("derm-08-04", "Toxic shock syndrome (TSS)",
    "S. aureus (tampon, nasal packing, หลังผ่าคลอด/แท้ง, แผล/จุดฉีดยา) หรือ S. pyogenes (NF, myositis) · superantigen → ไข้สูง erythroderma shock MOF · ลอกที่ 1–2 สัปดาห์ · fluid vasopressor source control · ไม่ทราบเชื้อ vanco + clinda",
    minutes=7, source=f"{D} หน้า 279–280, 287–292", nl=["2.2.7", "2.2.48"],
    md='''
### เชื้อและแหล่ง

| เชื้อ | แหล่งติดเชื้อที่พบบ่อย |
|---|---|
| **S. aureus** | **tampon, nasal packing, หลังผ่าคลอด, หลังแท้ง, แผล/จุดฉีดยา** |
| **S. pyogenes** | **necrotizing fasciitis, myositis** |

- สร้าง **exotoxin (superantigen) → กระตุ้น T cell → cytokine ปล่อยมหาศาล**

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| ทั่วไป | **flu-like, ไข้สูง** · ท้องเสีย อาเจียน ปวดกล้ามเนื้อ (เสริม) |
| ผิว | **erythroderma** (diffuse macular blanching erythema — "sunburn-like") |
| Mucosa (เสริม) | ตาแดง (conjunctival hyperemia), strawberry tongue |
| ระบบ | **shock, multiple organ failure** (ซึม สับสน ไตวาย เกล็ดเลือดต่ำ) |
| ระยะหลัง | **ลอกที่ฝ่ามือฝ่าเท้า 1–2 สัปดาห์หลังเริ่มป่วย** |

- **Ix: hemoculture, culture จากแหล่งติดเชื้อ** (S. aureus TSS hemoculture มักลบ (เสริม))

### การรักษา (สไลด์หน้า 280)

- **Supportive: IV fluid resuscitation, vasopressors**
- **รักษาแหล่ง (source control)**: เอา tampon/packing ออก, **debridement ใน NF**
- **Empirical IV ATB** (ต้องมี **clindamycin** เพื่อกดการสร้าง toxin):

| เชื้อ | ยา |
|---|---|
| **ไม่ทราบเชื้อ** | **vancomycin + clindamycin** |
| **MSSA** | **cloxacillin + clindamycin** |
| **MRSA** | **vancomycin + clindamycin** |
| **S. pyogenes** | **penicillin G + clindamycin** |

> SSSS vs TSS: SSSS = เด็ก ผิวลอกตื้นทันที Nikolsky + ไม่ shock · TSS = ผู้ใหญ่ erythroderma + **shock + MOF** ลอกหลัง 1–2 สัปดาห์
''',
    pearls=[
        "TSS = ไข้สูง + erythroderma + shock + MOF · ลอกที่ฝ่ามือฝ่าเท้า 1–2 wk",
        "S. aureus: tampon, nasal packing, หลังคลอด/แท้ง, จุดฉีดยา · S. pyogenes: NF, myositis",
        "Fluid + vasopressor + source control + ATB ที่มี clindamycin",
        "ไม่ทราบเชื้อ/MRSA → vanco + clinda · MSSA → cloxa + clinda · strep → PGS + clinda",
    ],
    items=[
        mcq("DERM-08-04-1", """A 23-year-old woman has had fever, chills, myalgia and fatigue for 5 days. She is menstruating and using tampons. Temperature 38.9°C, BP 88/55 mmHg, HR 115/min. She is confused and has widespread macular blanching erythroderma. WBC is 17,000/mm3 with neutrophil predominance. What is the most likely diagnosis?""",
            "Toxic shock syndrome", ["Staphylococcal scalded skin syndrome", "Scarlet fever", "Dengue shock syndrome", "Toxic epidermal necrolysis"],
            explain="""ใช้ **tampon** + ไข้สูง + **erythroderma** + **shock** + สับสน (อวัยวะล้มเหลว) = **toxic shock syndrome** จาก S. aureus (สไลด์หน้า 279, 287–288)
- SSSS พบในเด็กเล็ก ผิวลอกตื้น Nikolsky + และไม่ shock รุนแรง
- Scarlet fever เป็นผื่นกระดาษทรายในเด็กหลังคออักเสบ ไม่มี shock
- Dengue shock syndrome เกิดหลังไข้ลง มี WBC ต่ำ เกล็ดเลือดต่ำ Hct สูง ไม่ใช่ neutrophilia
- TEN เป็นผิวหลุดลอกหลังยา มี mucosa และ Nikolsky +""",
            pearl="Tampon + ไข้ + erythroderma + shock = TSS",
            topic="TSS dx", ref=[f"{D} หน้า 287–288"], nl=["2.2.7"], kind="old", src=OLD),
        mcq("DERM-08-04-2", """A 20-year-old woman has fever and hypotension refractory to fluid resuscitation. Temperature 39°C, BP 86/52 mmHg, HR 110/min. Examination shows conjunctival injection, diffuse macular erythroderma and a strawberry tongue. Three days ago she had myalgia and diarrhea; her menstrual period started 4 days ago and she uses tampons. Besides removing the tampon, what is the most appropriate next step?""",
            "IV fluids with vasopressors plus empirical vancomycin and clindamycin", ["Oral penicillin V for 10 days", "IV ceftriaxone alone", "Oral prednisolone", "IV acyclovir"],
            explain="""นี่คือ **TSS** (tampon + ไข้ + erythroderma + shock ไม่ตอบสนองต่อน้ำ + mucosa) → **supportive (fluid + vasopressor) + source control + empirical ATB: ไม่ทราบเชื้อใช้ vancomycin + clindamycin** (สไลด์หน้า 280, 289–290)
- Penicillin V กินเป็นการรักษา scarlet fever ไม่พอสำหรับผู้ป่วย shock และไม่ครอบคลุม staph
- Ceftriaxone เดี่ยว ๆ ไม่ครอบคลุม MRSA และไม่มี clindamycin กด toxin
- Prednisolone ไม่ใช่การรักษาหลัก
- Acyclovir ใช้กับไวรัส herpes""",
            pearl="TSS ไม่ทราบเชื้อ → vancomycin + clindamycin + fluid/vasopressor + source control",
            topic="TSS tx", ref=[f"{D} หน้า 280, 289–290"], nl=["2.2.7", "2.2.48"], kind="old", src=OLD),
        mcq("DERM-08-04-3", """A 60-year-old man has had high fever and rash for 1 day. Four days ago he received an analgesic injection in the right buttock for back pain; the site is now red and swollen. Temperature 39.5°C, HR 130/min, BP 80/50 mmHg, RR 24/min. He is stuporous with fine crackles in both lungs, diffuse erythema of all extremities, and a few flaccid bullae on the trunk. WBC 19,000/mm3 (neutrophils 90%), platelets 100,000/µL. Gram stain of bulla fluid shows no organisms. What is the most appropriate antibiotic regimen?""",
            "Vancomycin plus clindamycin", ["Piperacillin-tazobactam", "Penicillin G plus clindamycin", "Ceftriaxone plus clindamycin", "Meropenem plus vancomycin"],
            explain="""ติดเชื้อที่ **จุดฉีดยา** (S. aureus) + **erythroderma + shock + อวัยวะล้มเหลว** = **TSS** · ยังไม่ทราบว่า MSSA หรือ MRSA → **vancomycin + clindamycin** (สไลด์หน้า 280, 291–292)
- Piperacillin-tazobactam ไม่ครอบคลุม MRSA และไม่มี clindamycin กด toxin
- Penicillin G + clindamycin เหมาะกับ S. pyogenes แต่จุดฉีดยาชี้ไปทาง S. aureus ซึ่งดื้อ penicillin
- Ceftriaxone + clindamycin ไม่ครอบคลุม MRSA
- Meropenem + vancomycin ครอบคลุมกว้างแต่ขาด clindamycin ซึ่งเป็นตัวยับยั้ง toxin ใน TSS""",
            pearl="TSS จาก staph ยังไม่ทราบความไว → vanco + clinda",
            topic="TSS tx", ref=[f"{D} หน้า 291–292"], nl=["2.2.7", "2.2.48"], kind="old", src=OLD),
    ])

LECTURE = lecture("08", "Viral exanthems & toxin-mediated rashes", subtitle="measles · rubella · roseola · fifth disease · HFMD · scarlet fever · SSSS · TSS",
    objectives=[
        "ใช้ลำดับไข้–ผื่นและ sign จำเพาะ (Koplik, Forchheimer, slapped cheek) แยก viral exanthem",
        "วินิจฉัย scarlet fever และให้ penicillin/amoxicillin 10 วัน",
        "แยก SSSS, TSS และ TEN ด้วยอายุ mucosa shock และสาเหตุ",
        "เลือก anti-staph/strep regimen ที่มี clindamycin สำหรับโรคจาก toxin",
    ],
    sections=[S1, S2, S3, S4])
