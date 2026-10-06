from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Infectious"

# ---------------------------------------------------------------- 08-01 Oral lesions
S1 = sec("id-08-01", "Oral lesions in HIV: oral hairy leukoplakia vs oral candidiasis",
    "OHL = EBV ขาวเป็นริ้วข้างลิ้น ขูดไม่ออก ไม่ต้องรักษา · thrush = Candida ขูดออกได้ ข้างใต้แดง · KOH · clotrimazole troche/nystatin · esophageal → fluconazole",
    minutes=5, source=f"{D} หน้า 268–276", nl=["2.3.11(9)", "2.3.1(9)", "2.3.1-3(7)"],
    md='''
### Oral hairy leukoplakia (OHL)

- **Epstein-Barr virus (EBV)** · พบใน immunocompromised โดยเฉพาะ **HIV** (บ่งว่าภูมิเริ่มต่ำ)
- **Benign** · **painless, irregular white plaques with feathery/hairy (corrugated) appearance**
- พบบ่อยที่ **lateral border ของลิ้น** (เป็นริ้วแนวตั้ง)
- **Cannot be scraped off**
- **Tx: underlying disease (ART)** — ตัวรอยโรคไม่ต้องรักษา

### Oral thrush (oropharyngeal candidiasis)

- **Candida albicans**
- **White plaque, can be scraped off** · ข้างใต้เป็น **erythema** (เลือดซิบ)
- เจ็บคอ/กลืนเจ็บ · ถ้ากลืนเจ็บมากให้นึกถึง **esophageal candidiasis** (AIDS-defining) (เสริม)
- **Ix: KOH** preparation (budding yeast + pseudohyphae)
- **Tx: clotrimazole oral troche**, **nystatin oral suspension** (topical) · รุนแรง/esophageal → **oral fluconazole** (เสริม)
- Thrush ใน HIV = ข้อบ่งชี้ **TMP/SMX prophylaxis** และต้องเริ่ม ART

| | OHL | Oral candidiasis |
|---|---|---|
| Pathogen | **EBV** | **Candida albicans** |
| ตำแหน่ง | ข้างลิ้น | ทั่วปาก เพดาน คอ ลิ้น |
| Scraped off | **No** | **Yes** (underlying erythema) |
| Treatment | **No need** (รักษา HIV) | **Topical antifungal**: clotrimazole, nystatin |

> DDx ฝ้าขาวอื่น: leukoplakia (premalignant, คนสูบบุหรี่), lichen planus (ลายลูกไม้ Wickham striae) (เสริม)
''',
    pearls=[
        "OHL = EBV · ขาวเป็นริ้วข้างลิ้น ขูดไม่ออก ไม่ต้องรักษา",
        "Thrush = Candida · ขูดออกได้ ข้างใต้แดง · KOH",
        "Thrush เล็กน้อย → clotrimazole troche/nystatin · esophageal → fluconazole",
        "Thrush ใน HIV = เริ่ม ART + TMP/SMX prophylaxis",
    ],
    items=[
        mcq("ID-08-01-1",
            "A 30-year-old man has a non-painful, vertically corrugated whitish plaque along the lateral border of the tongue that cannot be scraped off. What is the most likely causative agent?",
            "Epstein-Barr virus",
            ["Candida albicans", "Staphylococcus aureus", "Poxvirus", "Human papillomavirus"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ฝ้าขาวเป็นริ้วแนวตั้ง **ข้างลิ้น ขูดไม่ออก ไม่เจ็บ** = **oral hairy leukoplakia** จาก **EBV** — ควรตรวจ anti-HIV
- Candida ขูดออกได้ และข้างใต้แดง
- S. aureus ไม่ทำให้รอยโรคลักษณะนี้
- Poxvirus (molluscum) เป็นตุ่มบุ๋มกลางที่ผิวหนัง
- HPV ทำให้หูดในปาก (papilloma) เป็นตุ่มนูน ไม่ใช่แผ่นขาวเป็นริ้ว''',
            pearl="ฝ้าขาวข้างลิ้นขูดไม่ออก = OHL (EBV)", topic="OHL",
            ref=[f"{D} หน้า 268, 271–272"], nl=["2.3.11(9)"]),
        mcq("ID-08-01-2",
            "A 27-year-old woman has had a sore throat for 2 weeks. White patches cover the pharynx and tongue and can be scraped off, leaving an erythematous base. What is the most appropriate investigation?",
            "KOH preparation of the scraping",
            ["Throat culture for group A Streptococcus", "Gram stain for diphtheria", "Biopsy of the lesion", "EBV viral capsid antigen IgM"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''คราบขาว **ขูดออกได้ ข้างใต้แดง** = **oral thrush** → ตรวจ **KOH** เห็น budding yeast + pseudohyphae แล้วรักษาด้วย clotrimazole troche/nystatin (และควรตรวจ anti-HIV)
- GAS culture ใช้กับ exudative tonsillitis ไข้สูง ไม่ใช่คราบทั่วปากและลิ้นนาน 2 สัปดาห์
- Diphtheria membrane ขูดแล้วเลือดออก ลอกไม่ออกง่าย
- Biopsy ใช้เมื่อสงสัยมะเร็ง/leukoplakia ที่ขูดไม่ออก
- EBV serology ใช้เมื่อสงสัย IM''',
            pearl="ฝ้าขาวขูดออกได้ → KOH", topic="Oral thrush investigation",
            ref=[f"{D} หน้า 269, 273–274"], nl=["2.3.11(9)", "2.3.1-3(7)"]),
        mcq("ID-08-01-3",
            "A 35-year-old man has had white patches on the tonsils for several months without fever or other symptoms. The patches scrape off easily. Anti-HIV is positive and CD4 count is 250 cells/mm3. What is the most appropriate management?",
            "Topical antifungal plus oral antiretroviral therapy",
            ["Oral antifungal plus oral antiretroviral therapy", "Oral antifungal alone", "Topical antifungal alone", "Oral antiretroviral therapy alone"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (เฉลยเป็นภาพ — ตอบตามแนวทาง)",
            explain='''Oropharyngeal candidiasis **ไม่รุนแรง** ไม่มีกลืนเจ็บ → **topical antifungal (clotrimazole troche/nystatin)** + HIV ที่ยังไม่ได้รักษา → **เริ่ม ART** (ไม่มี OI รุนแรงที่ต้องเลื่อน ART) และควรได้ TMP/SMX prophylaxis เพราะมี thrush
- Oral antifungal (fluconazole) ใช้เมื่อรุนแรงหรือ esophageal candidiasis — ใช้ได้แต่เกินความจำเป็นในรายนี้
- Antifungal อย่างเดียวไม่รักษาต้นเหตุ เชื้อราจะกลับมาอีก
- ART อย่างเดียวไม่ทำให้ thrush หายเร็ว''',
            pearl="HIV + thrush เล็กน้อย → topical antifungal + เริ่ม ART", topic="Thrush in HIV",
            ref=[f"{D} หน้า 269–270, 275–276"], nl=["2.3.11(9)", "2.3.1(9)"]),
    ])

# ---------------------------------------------------------------- 08-02 Dimorphic fungi / umbilicated papule
F_YEAST = fig("id-08-02-f1", "Umbilicated papule ใน HIV: แยกเชื้อจากรูปร่าง yeast", '''<svg viewBox="0 0 740 280">
 <rect x="10" y="10" width="236" height="260" rx="12" class="badsoft"/>
 <text x="128" y="36" text-anchor="middle" class="tb">Talaromyces marneffei</text>
 <ellipse cx="80" cy="96" rx="22" ry="13" class="box"/>
 <path d="M80 83V109" class="lnbad"/>
 <ellipse cx="140" cy="88" rx="14" ry="10" class="box"/>
 <path d="M140 78V98" class="lnbad"/>
 <ellipse cx="190" cy="104" rx="30" ry="12" class="box"/>
 <path d="M190 92V116" class="lnbad"/>
 <text x="22" y="150" class="t2">• เล็ก รูปร่างหลากหลาย</text>
 <text x="22" y="172" class="t2">• ขนาดไม่เท่ากัน</text>
 <text x="22" y="194" class="tb">• Central septation</text>
 <text x="34" y="214" class="t3">(binary fission ไม่ budding)</text>
 <text x="22" y="244" class="t3">ภาคเหนือ · papule กลางตาย</text>
 <rect x="252" y="10" width="236" height="260" rx="12" class="c2soft"/>
 <text x="370" y="36" text-anchor="middle" class="tb">Histoplasma capsulatum</text>
 <circle cx="320" cy="96" r="9" class="box"/>
 <circle cx="342" cy="96" r="9" class="box"/>
 <circle cx="364" cy="96" r="9" class="box"/>
 <circle cx="386" cy="96" r="9" class="box"/>
 <circle cx="331" cy="114" r="9" class="box"/>
 <circle cx="353" cy="114" r="9" class="box"/>
 <circle cx="375" cy="114" r="9" class="box"/>
 <text x="264" y="150" class="t2">• เล็ก รูปไข่ budding</text>
 <text x="264" y="172" class="tb">• ขนาดเท่ากัน</text>
 <text x="264" y="194" class="t2">• เกาะกลุ่มแบบพวงองุ่น</text>
 <text x="264" y="214" class="t3">(อยู่ใน macrophage)</text>
 <text x="264" y="244" class="t3">ไม่มี septum</text>
 <rect x="494" y="10" width="236" height="260" rx="12" class="c1soft"/>
 <text x="612" y="36" text-anchor="middle" class="tb">Cryptococcus neoformans</text>
 <circle cx="580" cy="100" r="30" class="lnc1"/>
 <circle cx="580" cy="100" r="16" class="box"/>
 <circle cx="660" cy="96" r="22" class="lnc1"/>
 <circle cx="660" cy="96" r="11" class="box"/>
 <circle cx="676" cy="84" r="5" class="box"/>
 <text x="506" y="150" class="t2">• ใหญ่ กลม budding</text>
 <text x="506" y="172" class="tb">• มี capsule หนา (halo)</text>
 <text x="506" y="194" class="t2">• ขนาดไม่เท่ากัน</text>
 <text x="506" y="214" class="t3">India ink · CrAg</text>
 <text x="506" y="244" class="t3">meningitis ใน CD4 &lt; 100</text>
</svg>''', "ทั้งสามทำ umbilicated papule ได้ใน HIV CD4 ต่ำ · แยกด้วยรูปร่าง: talaromyces มีผนังกั้นกลาง · histoplasma เล็กเท่ากันเป็นพวง · cryptococcus ใหญ่มี capsule (สไลด์หน้า 277–280)")

S2 = sec("id-08-02", "Umbilicated papules in HIV: talaromycosis, histoplasmosis, cryptococcosis",
    "CD4 < 100 + ไข้เรื้อรัง + papule กลางบุ๋ม/เนื้อตาย + LN + HSM · Talaromyces central septation · Histoplasma เล็กเท่ากัน · Cryptococcus capsule · amphotericin B → itraconazole/fluconazole",
    minutes=7, source=f"{D} หน้า 277–286", nl=["2.3.1-3(7)", "2.3.1(9)", "2.1.50"],
    md='''
### ภาพทางคลินิก

- HIV **CD4 < 100** · **ไข้เรื้อรัง (prolonged fever)** น้ำหนักลด ซีด
- **Umbilicated papules** (ตุ่มกลางบุ๋มคล้าย molluscum) หรือ papule **กลางเป็นเนื้อตาย** ที่หน้า ลำตัว แขนขา
- **Generalized lymphadenopathy, hepatosplenomegaly** · pneumonia ได้
- Ix: scraping/biopsy ผิวหนัง ไขกระดูก LN → **Wright/Giemsa stain**, culture · hemoculture (เชื้อรา) · CrAg (เสริม)

[[fig:id-08-02-f1]]

### แยกเชื้อจากรูป (สไลด์หน้า 277–280)

| เชื้อ | ลักษณะ yeast |
|---|---|
| **Talaromyces (Penicillium) marneffei** | **Small pleomorphic yeast**, **central septation (binary fission)**, **vary in size** · เด่นในภาคเหนือ |
| **Histoplasma capsulatum** | **Small oval budding yeast**, **grape-like** (เป็นกลุ่มใน macrophage), **same in size** |
| **Cryptococcus neoformans** | **Large round budding yeast**, **capsulated**, **vary in size** |

### การรักษา (เสริม — สไลด์ไม่ได้ให้ขนาดยา)

| โรค | Induction | ต่อเนื่อง |
|---|---|---|
| Talaromycosis | **Amphotericin B** 2 สัปดาห์ | **Itraconazole** 400 mg/d 10 สัปดาห์ → 200 mg/d (secondary prophylaxis) จน CD4 > 100 ≥ 6 เดือน |
| Histoplasmosis (disseminated) | Liposomal amphotericin B 1–2 สัปดาห์ | Itraconazole |
| Cryptococcal meningitis | **Amphotericin B + flucytosine** (หรือ + fluconazole) 2 สัปดาห์ + **therapeutic LP ลดความดัน** | Fluconazole 400–800 → 200 mg/d |

- เริ่ม ART หลังรักษา OI ~2 สัปดาห์ (ยกเว้น cryptococcal meningitis รอ 4–6 สัปดาห์)
''',
    figs=[F_YEAST],
    pearls=[
        "HIV CD4 < 100 + ไข้เรื้อรัง + umbilicated papule + HSM → คิดถึง talaromyces/histo/crypto",
        "Talaromyces = central septation (binary fission) ขนาดไม่เท่า",
        "Histoplasma = เล็ก ขนาดเท่ากัน เป็นพวงองุ่น",
        "Cryptococcus = ใหญ่ มี capsule",
        "รักษา: amphotericin B induction → azole (เสริม)",
    ],
    items=[
        mcq("ID-08-02-1",
            "A 35-year-old man with HIV has umbilicated papules on the face and oral thrush. Smear from a papule shows large round budding yeasts surrounded by a thick capsule. What is the most likely diagnosis?",
            "Cryptococcosis",
            ["Penicilliosis (talaromycosis)", "Taeniasis", "Toxoplasmosis", "Histoplasmosis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ภาพบรรยายเป็นข้อความ)",
            explain='''Yeast **ใหญ่ กลม budding มี capsule** = **Cryptococcus neoformans** → ต้องทำ LP หา cryptococcal meningitis ร่วมด้วย
- Talaromyces เป็น yeast เล็กรูปร่างหลากหลาย มี central septation ไม่มี capsule
- Taeniasis เป็นพยาธิตัวตืดในลำไส้ ไม่ทำให้ papule แบบนี้
- Toxoplasma เป็น protozoa ทำให้ ring-enhancing lesion ในสมอง
- Histoplasma เป็น yeast เล็กขนาดเท่ากันเป็นพวง ไม่มี capsule หนา''',
            pearl="Yeast ใหญ่มี capsule = Cryptococcus", topic="Cryptococcus morphology",
            ref=[f"{D} หน้า 277, 280–282"], nl=["2.3.1-3(7)"]),
        mcq("ID-08-02-2",
            "A 30-year-old man from Chiang Mai has had prolonged fever for 6 weeks. He has discrete papular skin lesions with central necrosis on the face, trunk and extremities, a few cervical lymph nodes and hepatomegaly. Wright stain of a skin scraping shows small, variably sized, oval yeast cells with a central transverse septum. What is the most likely diagnosis?",
            "Talaromycosis",
            ["Candidiasis", "Cryptococcosis", "Histoplasmosis", "Leishmaniasis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ภาพบรรยายเป็นข้อความ)",
            explain='''ไข้เรื้อรัง + papule กลางเนื้อตาย + LN + ตับโต + yeast **มี central septation (binary fission)** = **Talaromyces marneffei** (ภาคเหนือ)
- Candida เป็น budding yeast + pseudohyphae ไม่ทำ papule แบบนี้
- Cryptococcus ใหญ่และมี capsule
- Histoplasma เป็น budding yeast เล็ก ขนาดเท่ากัน ไม่มี septum
- Leishmania amastigote มี kinetoplast และไม่ใช่โรคเด่นในไทย''',
            pearl="Central septation = Talaromyces", topic="Talaromycosis",
            ref=[f"{D} หน้า 278, 283–284"], nl=["2.3.1-3(7)"]),
        mcq("ID-08-02-3",
            "A patient with HIV has prolonged high intermittent fever for 4 weeks, multiple papular skin lesions, generalized lymphadenopathy and hepatomegaly. Wright stain of a bone-marrow aspirate shows numerous small oval budding yeasts of uniform size clustered inside macrophages, without septa or capsules. What is the most likely pathogen?",
            "Histoplasma capsulatum",
            ["Talaromyces marneffei", "Leishmania donovani", "Cryptococcus neoformans", "Pneumocystis jirovecii"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ภาพบรรยายเป็นข้อความ — เฉลยในสไลด์เป็นภาพ)",
            explain='''Yeast **เล็ก รูปไข่ budding ขนาดเท่ากัน เป็นกลุ่มใน macrophage** ไม่มี septum/capsule = **Histoplasma capsulatum** (disseminated histoplasmosis)
- Talaromyces มี central septation ขนาดไม่เท่ากัน — ถ้าภาพในข้อสอบจริงเห็น septum ให้ตอบ penicilliosis
- Leishmania amastigote มี nucleus และ kinetoplast
- Cryptococcus ใหญ่มี capsule
- Pneumocystis เป็น cyst ในปอด ย้อม GMS''',
            pearl="Yeast เล็ก ขนาดเท่ากัน ใน macrophage = Histoplasma", topic="Histoplasmosis",
            ref=[f"{D} หน้า 279, 285–286"], nl=["2.3.1-3(7)"]),
    ])

# ---------------------------------------------------------------- 08-03 Chronic diarrhea in HIV
S3 = sec("id-08-03", "Chronic watery diarrhea in HIV (coccidian parasites)",
    "Cryptosporidium 4–5 µm · Cyclospora 8–10 µm · Cystoisospora ใหญ่รูปไข่ — modified acid-fast · Microsporidia — modified trichrome",
    minutes=5, source=f"{D} หน้า 287–291", nl=["2.3.1-3(6)", "2.1.18"],
    md='''
### เชื้อก่อโรคท้องเสียเรื้อรังแบบน้ำใน HIV (CD4 ต่ำ)

| เชื้อ | ขนาด oocyst | ย้อม | รักษา (เสริม) |
|---|---|---|---|
| **Cryptosporidium spp.** | **4–5 µm** (เล็กสุด กลม) | **Modified acid-fast** | **ART** (ฟื้นภูมิ) + supportive · nitazoxanide |
| **Cyclospora cayetanensis** | **8–10 µm** | Modified acid-fast (ติดสีไม่สม่ำเสมอ) · autofluorescence | **TMP/SMX** |
| **Cystoisospora (Isospora) belli** | ใหญ่ **20–30 µm รูปไข่** | Modified acid-fast | **TMP/SMX** |
| **Microsporidia** | spore เล็กมาก 1–2 µm | **Modified trichrome** | Albendazole + ART |

- อาการ: ท้องเสียเป็นน้ำปริมาณมาก > 1 เดือน น้ำหนักลด malabsorption (เสริม)
- Cryptosporidiosis และ cystoisosporiasis > 1 เดือน = **AIDS-defining** · พบเมื่อ CD4 < 100
- Cystoisospora มี **eosinophilia** ได้ (protozoa ตัวเดียวที่ทำให้ eosinophil สูง) (เสริม)

> ข้อสอบ: modified AFB เห็น oocyst **3–6 µm** = **Cryptosporidium** · 8–10 µm = Cyclospora · ใหญ่รูปไข่ = Cystoisospora · ต้องใช้ modified trichrome = Microsporidia
''',
    pearls=[
        "Modified AFB: Cryptosporidium 4–5 µm < Cyclospora 8–10 µm < Cystoisospora ใหญ่รูปไข่",
        "Microsporidia ย้อม modified trichrome",
        "Cyclospora/Cystoisospora → TMP/SMX · Cryptosporidium → ART เป็นหลัก",
        "Cryptosporidium พบเมื่อ CD4 < 100 (AIDS-defining ถ้า > 1 เดือน)",
    ],
    items=[
        mcq("ID-08-03-1",
            "A patient with HIV has watery diarrhea for 3 months. Modified acid-fast stain of stool shows round oocysts 3–6 micrometers in diameter. What is the most likely diagnosis?",
            "Cryptosporidium species",
            ["Cyclospora cayetanensis", "Cystoisospora belli", "Microsporidia", "Cryptococcus neoformans"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Oocyst **ติด modified AFB ขนาดเล็ก 4–5 µm** = **Cryptosporidium**
- Cyclospora ติด modified AFB แต่ใหญ่กว่า 8–10 µm
- Cystoisospora oocyst ใหญ่รูปไข่ 20–30 µm
- Microsporidia ต้องย้อม modified trichrome และเล็กมาก
- Cryptococcus เป็นเชื้อราที่ไม่ทำให้ท้องเสียเรื้อรังและไม่ใช่ oocyst''',
            pearl="Modified AFB 4–5 µm = Cryptosporidium", topic="Cryptosporidium",
            ref=[f"{D} หน้า 288, 290–291"], nl=["2.3.1-3(6)"]),
        mcq("ID-08-03-2",
            "A 38-year-old man with AIDS (CD4 40 cells/mm3) has chronic watery diarrhea and peripheral eosinophilia. Modified acid-fast stain shows large ellipsoidal oocysts about 25 micrometers long. What is the most appropriate treatment?",
            "Trimethoprim-sulfamethoxazole",
            ["Metronidazole", "Albendazole", "Praziquantel", "Fluconazole"],
            explain='''Oocyst **ใหญ่รูปไข่** ติด modified AFB + eosinophilia = **Cystoisospora belli** → **TMP/SMX** (เสริม)
- Metronidazole ใช้กับ Giardia และ E. histolytica
- Albendazole ใช้กับ microsporidia และพยาธิตัวกลม
- Praziquantel ใช้กับพยาธิใบไม้/ตัวตืด
- Fluconazole เป็นยาเชื้อรา''',
            pearl="Cystoisospora/Cyclospora → TMP/SMX", topic="Cystoisospora treatment",
            ref=[f"{D} หน้า 287–288"], nl=["2.3.1-3(6)"]),
        mcq("ID-08-03-3",
            "A 41-year-old man with AIDS has chronic diarrhea. Modified acid-fast and routine stool examinations are negative. Which stain is most useful to detect microsporidia?",
            "Modified trichrome stain",
            ["Modified acid-fast stain repeated", "India ink stain", "Gram stain", "Giemsa stain of blood"],
            explain='''**Microsporidia** spore เล็กมาก ต้องใช้ **modified trichrome stain** (สไลด์หน้า 289)
- Modified AFB ใช้กับ Cryptosporidium, Cyclospora, Cystoisospora
- India ink ใช้หา capsule ของ Cryptococcus ใน CSF
- Gram stain ไม่เห็น microsporidia ชัด
- Giemsa ของเลือดใช้หา malaria/blood parasite''',
            pearl="Microsporidia = modified trichrome", topic="Microsporidia",
            ref=[f"{D} หน้า 289"], nl=["2.3.1-3(6)"]),
    ])

LECTURE = lecture("08", "Opportunistic infections in HIV",
    "Oral lesions · dimorphic fungi & cryptococcus · chronic diarrhea",
    objectives=[
        "แยก oral hairy leukoplakia กับ oral candidiasis และรักษาได้",
        "แยก Talaromyces, Histoplasma, Cryptococcus จากลักษณะเชื้อ",
        "แยกเชื้อก่อท้องเสียเรื้อรังใน HIV จาก stain และขนาด oocyst",
    ],
    sections=[S1, S2, S3])
