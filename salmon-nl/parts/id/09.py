from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Infectious"

# ---------------------------------------------------------------- 09-01 Helminth overview + trematodes
F_PARA = fig("id-09-01-f1", "แผนผังปรสิตและยาที่ใช้ (ตามสไลด์)", '''<svg viewBox="0 0 740 420">
 <defs><marker id="id-09-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="290" y="10" width="160" height="36" rx="10" class="acsoft"/>
 <text x="370" y="33" text-anchor="middle" class="tb">Parasite</text>
 <path d="M330 46L130 76" class="ln" marker-end="url(#id-09-01-a)"/>
 <path d="M410 46L590 76" class="ln" marker-end="url(#id-09-01-a)"/>
 <rect x="10" y="78" width="240" height="36" rx="10" class="c1soft"/>
 <text x="130" y="101" text-anchor="middle" class="tb">Protozoa (เซลล์เดียว)</text>
 <rect x="10" y="122" width="240" height="96" rx="10" class="box"/>
 <text x="22" y="144" class="t2">Giardia lamblia</text>
 <text x="22" y="164" class="t2">Entamoeba histolytica</text>
 <rect x="22" y="176" width="216" height="30" rx="8" class="c1"/>
 <text x="130" y="196" text-anchor="middle" class="tw">Metronidazole</text>
 <text x="22" y="236" class="t3">Coccidia (HIV) → ดูหัวข้อ 08-03</text>
 <rect x="270" y="78" width="460" height="36" rx="10" class="c2soft"/>
 <text x="500" y="101" text-anchor="middle" class="tb">Helminths (หนอนพยาธิ) — endoparasite</text>
 <rect x="270" y="122" width="148" height="34" rx="8" class="ok"/>
 <text x="344" y="144" text-anchor="middle" class="tw">Nematodes (กลม)</text>
 <rect x="426" y="122" width="148" height="34" rx="8" class="miss"/>
 <text x="500" y="144" text-anchor="middle" class="tw">Trematodes (ใบไม้)</text>
 <rect x="582" y="122" width="148" height="34" rx="8" class="bad"/>
 <text x="656" y="144" text-anchor="middle" class="tw">Cestodes (ตัวตืด)</text>
 <rect x="270" y="164" width="148" height="140" rx="8" class="oksoft"/>
 <text x="280" y="186" class="t2">Ascaris</text>
 <text x="280" y="206" class="t2">Hookworm</text>
 <text x="280" y="226" class="t2">Trichuris</text>
 <text x="280" y="246" class="t2">Capillaria</text>
 <text x="280" y="266" class="t2">Strongyloides</text>
 <text x="280" y="292" class="tb">Albendazole</text>
 <rect x="426" y="164" width="148" height="140" rx="8" class="misssoft"/>
 <text x="436" y="186" class="t2">Opisthorchis</text>
 <text x="436" y="206" class="t2">Paragonimus</text>
 <text x="436" y="226" class="t2">Fasciolopsis</text>
 <text x="436" y="246" class="t2">Schistosoma</text>
 <text x="436" y="292" class="tb">Praziquantel</text>
 <rect x="582" y="164" width="148" height="140" rx="8" class="badsoft"/>
 <text x="592" y="186" class="t2">Taenia spp.</text>
 <text x="592" y="206" class="t3">(T. solium, T. saginata)</text>
 <text x="592" y="270" class="tb">Praziquantel</text>
 <text x="592" y="292" class="t3">± albendazole</text>
 <rect x="270" y="314" width="460" height="96" rx="10" class="sunk"/>
 <text x="282" y="336" class="tb">ใบไม้ 4 ชนิด: กินอะไร → อยู่ที่ไหน</text>
 <text x="282" y="360" class="t2">ปู → ปอด (Paragonimus)</text>
 <text x="500" y="360" class="t2">ปลาดิบ → ตับ (Opisthorchis)</text>
 <text x="282" y="384" class="t2">แห้ว กระจับ → ลำไส้ (Fasciolopsis)</text>
 <text x="500" y="384" class="t2">ไชผิวหนัง → เลือด (Schistosoma)</text>
 <text x="282" y="404" class="t3">Strongyloides ใช้ ivermectin เป็นหลัก</text>
 <text x="10" y="270" class="t3">Ectoparasite (เหา หมัด ไร)</text>
 <text x="10" y="290" class="t3">เป็นอีกกลุ่ม ไม่ได้ลงรายละเอียด</text>
</svg>''', "จำง่าย: ตัวกลมใช้ albendazole · ใบไม้และตัวตืดใช้ praziquantel · protozoa ในลำไส้ใช้ metronidazole · ท่อง 'ปู ปอด ปลา ตับ แห้ว กระจับ ลำไส้ ไช เลือด'")

S1 = sec("id-09-01", "Helminths overview & trematodes (Opisthorchis viverrini)",
    "กลม → albendazole · ใบไม้/ตืด → praziquantel · ปู-ปอด ปลา-ตับ แห้วกระจับ-ลำไส้ ไช-เลือด · OV จากปลาดิบ → cholangiocarcinoma · Giardia/amoeba → metronidazole",
    minutes=7, source=f"{D} หน้า 292–299, 315–316", nl=["2.3.1(12)", "B8.2.2(5)", "B1.5.5(1)"],
    md='''
### การแบ่งกลุ่มปรสิต (สไลด์หน้า 292)

- **Ectoparasite** (เหา หมัด ไร)
- **Endoparasite**: **Protozoa** (เซลล์เดียว) · **Helminths**: **nematodes (ตัวกลม)**, **trematodes (ใบไม้)**, **cestodes (ตัวตืด)**

### Trematodes (ใบไม้) — ท่อง "ปู ปอด · ปลา ตับ · แห้วกระจับ ลำไส้ · ไช เลือด"

| ติดจาก | ชนิด | ชื่อ |
|---|---|---|
| **ปู** (ดิบ เช่น ปูดอง) | **ปอด (lung fluke)** | **Paragonimus** — ไอเป็นเลือดเรื้อรังคล้าย TB |
| **ปลา** น้ำจืดเกล็ดขาวดิบ (ก้อยปลา ปลาร้าดิบ) | **ตับ (liver fluke)** | **Opisthorchis viverrini** |
| **แห้ว กระจับ** (พืชน้ำ) | **ลำไส้ (intestinal fluke)** | **Fasciolopsis buski** |
| **ไช** ผิวหนังจากน้ำ | **เลือด (blood fluke)** | **Schistosoma** |

### ยาตามกลุ่ม (สไลด์หน้า 296–298)

| เชื้อ | ยา |
|---|---|
| Ascaris lumbricoides · hookworm · Trichuris trichiura · Capillaria philippinensis | **Albendazole** |
| **Taenia spp.** | **Praziquantel** (± albendazole ในบางรายตามสไลด์) |
| **Opisthorchis viverrini** | **Praziquantel** (40 mg/kg ครั้งเดียว (เสริม)) |
| **Giardia** (duodenalis/intestinalis/lamblia) · **Entamoeba histolytica** | **Metronidazole** |

[[fig:id-09-01-f1]]

### Opisthorchis viverrini (พยาธิใบไม้ตับ) (เสริมรายละเอียด)

- ภาคอีสาน · กินปลาน้ำจืดดิบ/สุก ๆ ดิบ ๆ (ก้อยปลา ปลาส้ม)
- ส่วนใหญ่ไม่มีอาการ · ท้องอืด ปวดใต้ชายโครงขวา · เรื้อรัง → cholangitis, นิ่วในท่อน้ำดี
- **ภาวะแทรกซ้อนสำคัญ: cholangiocarcinoma**
- Stool exam: ไข่รูป **ขวดเหล้า มีฝาปิด (operculum) และไหล่ (shoulder)** ขนาดเล็ก
- Prevention: **งดกินปลาน้ำจืดดิบ**

> สไลด์หน้า 293–299 เป็นแผนภาพ/ภาพไข่พยาธิบางส่วน — รายละเอียดอาการและไข่ของแต่ละชนิดเป็นส่วนเสริม
''',
    figs=[F_PARA],
    pearls=[
        "ตัวกลม (Ascaris, hookworm, Trichuris, Capillaria) → albendazole",
        "ใบไม้ (OV) และตัวตืด (Taenia) → praziquantel",
        "ปู–ปอด (Paragonimus) · ปลา–ตับ (Opisthorchis) · แห้วกระจับ–ลำไส้ (Fasciolopsis) · ไช–เลือด (Schistosoma)",
        "OV → cholangiocarcinoma · งดปลาน้ำจืดดิบ",
        "Giardia, E. histolytica → metronidazole",
    ],
    items=[
        mcq("ID-09-01-1",
            "A 45-year-old man from Khon Kaen who regularly eats raw freshwater fish salad has eggs of Opisthorchis viverrini in his stool. What is the appropriate treatment?",
            "Praziquantel",
            ["Albendazole", "Mebendazole", "Ivermectin", "Metronidazole"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ภาพไข่บรรยายเป็นข้อความ)",
            explain='''**Opisthorchis viverrini เป็นพยาธิใบไม้ (trematode) → praziquantel**
- Albendazole และ mebendazole ใช้กับพยาธิตัวกลม ไม่ได้ผลดีกับพยาธิใบไม้ตับ
- Ivermectin ใช้กับ Strongyloides
- Metronidazole ใช้กับ protozoa (Giardia, amoeba)''',
            pearl="พยาธิใบไม้ตับ (OV) → praziquantel", topic="OV treatment",
            ref=[f"{D} หน้า 296, 315–316"], nl=["2.3.1(12)", "B8.2.2(5)"]),
        mcq("ID-09-01-2",
            "A 38-year-old man from northern Thailand who often eats raw crab has had chronic cough with hemoptysis for 3 months. Chest radiograph shows nodular and cystic lesions. Repeated sputum AFB smears are negative, but sputum shows operculated brown eggs. Which parasite is most likely?",
            "Paragonimus",
            ["Opisthorchis viverrini", "Fasciolopsis buski", "Schistosoma", "Strongyloides stercoralis"],
            explain='''**ปู → ปอด** = **Paragonimus (lung fluke)** ไอเป็นเลือดเรื้อรังคล้าย TB แต่ AFB ลบและพบไข่ที่มีฝาในเสมหะ → praziquantel (เสริม)
- Opisthorchis มาจากปลาดิบและอยู่ในท่อน้ำดี
- Fasciolopsis มาจากแห้ว/กระจับ อยู่ในลำไส้
- Schistosoma ติดจากตัวอ่อนไชผิวหนังในน้ำ อยู่ในหลอดเลือด
- Strongyloides ทำ Loeffler/hyperinfection ใน immunocompromised พบตัวอ่อน filariform ไม่ใช่ไข่มีฝา''',
            pearl="ปู → ปอด (Paragonimus)", topic="Trematodes",
            ref=[f"{D} หน้า 292–293"], nl=["B1.5.5(1)", "2.3.1-3(8)"]),
        mcq("ID-09-01-3",
            "A 25-year-old woman has foul-smelling, greasy, non-bloody diarrhea with bloating for 3 weeks after a trekking trip during which she drank stream water. Stool examination shows pear-shaped flagellated trophozoites. What is the most appropriate treatment?",
            "Metronidazole",
            ["Albendazole", "Praziquantel", "Ivermectin", "Ciprofloxacin"],
            explain='''ท้องเสียมันเหม็น ท้องอืด หลังดื่มน้ำลำธาร + trophozoite รูปลูกแพร์มี flagella = **Giardia lamblia** (protozoa) → **metronidazole** (ตามสไลด์)
- Albendazole ใช้กับพยาธิตัวกลม (และใช้กับ Giardia ได้บ้าง แต่ไม่ใช่ยาตามสไลด์)
- Praziquantel ใช้กับใบไม้/ตัวตืด
- Ivermectin ใช้กับ Strongyloides
- Ciprofloxacin เป็นยาแบคทีเรีย''',
            pearl="Giardia/amoeba → metronidazole", topic="Protozoa treatment",
            ref=[f"{D} หน้า 298"], nl=["2.3.1(12)"]),
    ])

# ---------------------------------------------------------------- 09-02 Strongyloidiasis
S2 = sec("id-09-02", "Strongyloidiasis",
    "ตัวอ่อนไชผิวหนัง · HIV/HTLV, steroid, transplant, alcohol · larva currens, Loeffler, GI · rhabditiform ในอุจจาระ · hyperinfection: filariform ในเสมหะ · ivermectin",
    minutes=6, source=f"{D} หน้า 300–308", nl=["2.3.1(12)", "2.3.1-3(6)"],
    md='''
### เชื้อและ risk

- **Strongyloides stercoralis** (ตัวกลม)
- **Percutaneous penetration of larvae** (filariform larva ไชผิวหนังจากดิน) → ปอด → ลำไส้ · มี **autoinfection** ทำให้อยู่ในตัวได้หลายสิบปี (เสริม)
- Risk ของโรครุนแรง: **HIV** (HTLV-1 สำคัญกว่า (เสริม)), **ได้ steroid** (สำคัญสุด เช่น SLE, nephrotic, COPD exacerbation), **organ transplant**, alcoholism

### อาการ — ขึ้นกับ larva เดินทางไปที่ไหน

- **Skin**: pruritus, บวม แดง MP rash · **serpiginous lesion ที่เคลื่อนเร็ว (larva currens)**
- **Lung**: dry cough, wheeze, hemoptysis, pneumonia (**Loeffler syndrome** — eosinophilic infiltrate)
- **GI**: anorexia, N/V, ปวดท้อง ท้องเสีย
- **Hyperinfection syndrome/disseminated** (immunocompromised): larva จำนวนมากไปทั่วร่างกาย → **gram-negative sepsis/meningitis** (ตัวอ่อนพาเชื้อลำไส้ออกมา) (เสริม) ตายสูง

### Investigation

- **Stool exam: rhabditiform larvae** (ไม่ใช่ไข่)
- **Hyperinfection/disseminated**: stool, **sputum/BAL: filariform larvae**
- Eosinophilia (อาจไม่มีในคนได้ steroid) · serology (เสริม)

### Management

- **Ivermectin** (200 µg/kg/d 2 วัน (เสริม)), albendazole
- **Hyperinfection/disseminated: ivermectin** (ให้ทุกวันจน stool/sputum ลบ ≥ 2 สัปดาห์ + ลด immunosuppression (เสริม))
- **ก่อนให้ steroid ขนาดสูงในคนจากพื้นที่ระบาด** → ตรวจ/ให้ ivermectin ป้องกัน (เสริม)
- Prevention: **สวมรองเท้าเมื่อสัมผัสดิน** · ล้างมือก่อนกินข้าว · ล้างผัก ดื่มน้ำสะอาด · **งดอุจจาระลงดิน**
''',
    pearls=[
        "Strongyloides: ตัวอ่อนไชผิวหนังจากดิน · autoinfection อยู่ได้นานหลายปี",
        "Steroid/HIV/HTLV/transplant → hyperinfection: filariform larva ในเสมหะ + GN sepsis",
        "อุจจาระพบ rhabditiform larva · larva currens ที่ผิวหนัง",
        "Ivermectin เป็นยาหลัก (albendazole ทางเลือก)",
    ],
    items=[
        mcq("ID-09-02-1",
            "A 35-year-old woman with SLE on high-dose prednisolone presents with fever, hemoptysis and dyspnea. Sputum examination shows filariform larvae. What is the most likely causative pathogen?",
            "Strongyloides stercoralis",
            ["Ascaris lumbricoides", "Ancylostoma duodenale", "Enterobius vermicularis", "Paragonimus westermani"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ได้ **steroid ขนาดสูง** + **filariform larvae ในเสมหะ** = **Strongyloides hyperinfection syndrome** → ivermectin
- Ascaris ผ่านปอดในระยะ larva (Loeffler) แต่ไม่ทำ hyperinfection ใน immunocompromised
- Hookworm (Ancylostoma) ผ่านปอดได้ แต่ไม่มี autoinfection จึงไม่เพิ่มจำนวนในคนได้ steroid
- Enterobius อยู่ที่รอบทวาร ไม่ไปปอด
- Paragonimus ทำให้ไอเป็นเลือด แต่พบไข่มีฝา ไม่ใช่ตัวอ่อน และติดจากปู''',
            pearl="Steroid + filariform larva ในเสมหะ = Strongyloides hyperinfection", topic="Strongyloides hyperinfection",
            ref=[f"{D} หน้า 303, 305–306"], nl=["2.3.1(12)", "2.3.1-3(6)"]),
        mcq("ID-09-02-2",
            "A 50-year-old man from Ubon Ratchathani with nephrotic syndrome is to start long-term high-dose prednisolone. He has mild eosinophilia. Infection with which parasite carries the greatest risk of disseminated larval disease during therapy?",
            "Strongyloides stercoralis",
            ["Opisthorchis viverrini", "Trichuris trichiura", "Taenia saginata", "Giardia lamblia"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Strongyloides มี **autoinfection** ทำให้เพิ่มจำนวนในร่างกายได้เอง เมื่อได้ steroid → **hyperinfection/disseminated** (สไลด์เฉลย) · ควรตรวจหรือให้ ivermectin ก่อนเริ่ม steroid (เสริม)
- Opisthorchis เป็นพยาธิใบไม้ตับ ไม่เพิ่มจำนวนในคน
- Trichuris อยู่ในลำไส้ใหญ่ ไม่มี larva แพร่กระจาย
- Taenia saginata เป็นตัวตืดวัว ไม่ทำ disseminated (T. solium ทำ cysticercosis ได้แต่ไม่ใช่จาก steroid)
- Giardia เป็น protozoa ไม่มี larva''',
            pearl="ก่อนให้ steroid นาน → นึกถึง Strongyloides", topic="Strongyloides risk",
            ref=[f"{D} หน้า 300, 307–308"], nl=["2.3.1(12)"]),
        mcq("ID-09-02-3",
            "A 42-year-old farmer has intermittent abdominal pain, diarrhea and a rapidly migrating, intensely pruritic serpiginous rash on the buttocks. Eosinophil count is 1,800/mm3. Stool examination shows rhabditiform larvae. What is the most appropriate treatment?",
            "Ivermectin",
            ["Praziquantel", "Metronidazole", "Pyrantel pamoate single dose", "Prednisolone"],
            explain='''**Larva currens** (ผื่นเคลื่อนเร็วที่ก้น) + eosinophilia + **rhabditiform larvae ในอุจจาระ** = **strongyloidiasis** → **ivermectin** (หรือ albendazole)
- Praziquantel ใช้กับใบไม้/ตืด
- Metronidazole ใช้กับ protozoa
- Pyrantel ใช้กับ Ascaris/Enterobius/hookworm ไม่ได้ผลกับ Strongyloides
- Prednisolone จะกระตุ้น hyperinfection ห้ามให้''',
            pearl="Larva currens + rhabditiform larva → ivermectin", topic="Strongyloides treatment",
            ref=[f"{D} หน้า 302–304"], nl=["2.3.1(12)"]),
    ])

# ---------------------------------------------------------------- 09-03 Capillariasis
S3 = sec("id-09-03", "Capillariasis",
    "Capillaria philippinensis จากปลาน้ำจืดดิบ · ท้องเสียเรื้อรัง ท้องร้องโครกคราก protein-losing → บวม ผอม · ไข่รูปถั่วลิสง bipolar plug · albendazole/mebendazole",
    minutes=5, source=f"{D} หน้า 309–314", nl=["2.3.1(12)", "2.1.18"],
    md='''
### เชื้อและการติดต่อ

- **Capillaria philippinensis** (ตัวกลม)
- **กินปลาน้ำจืดดิบ/ปรุงไม่สุก** (มี autoinfection ทำให้จำนวนพยาธิเพิ่มในลำไส้ (เสริม))

### อาการ

- ปวดท้อง · **chronic watery diarrhea**
- **Borborygmus** (ท้องร้องโครกคราก)
- **Malabsorption → severe protein loss** (protein-losing enteropathy) → **weight loss, muscle wasting, edema** (albumin ต่ำ) · ซีด ลิ้นอักเสบได้
- ไม่รักษา → เสียชีวิตจาก cachexia/electrolyte imbalance ได้ (เสริม)

### Investigation

- **Stool exam: ไข่รูป peanut shape มี bipolar flattened plug** (คล้าย Trichuris แต่ plug แบนกว่าและไม่ยื่น)

### Management

- **Hydration, nutrition** (แก้ protein/electrolyte)
- **Oral mebendazole, albendazole** (ให้นาน 10–20 วัน เพราะ relapse บ่อย (เสริม))
- Prevention: **เลี่ยงการกินปลาน้ำจืดปรุงไม่สุก**

> ท้องเสียเรื้อรัง + บวม + ผอมมาก + ท้องร้อง ในคนกินปลาดิบ = capillariasis — ต่างจาก OV ที่มาจากปลาดิบเหมือนกันแต่ไม่ทำให้ท้องเสียเรื้อรัง/protein loss
''',
    pearls=[
        "Capillaria = ปลาน้ำจืดดิบ → ท้องเสียเรื้อรัง + protein-losing → บวม ผอม",
        "Borborygmus เป็น clue",
        "ไข่ peanut shape + bipolar flattened plug",
        "Albendazole/mebendazole + hydration/nutrition",
    ],
    items=[
        mcq("ID-09-03-1",
            "A 40-year-old male farmer has had watery diarrhea for 2 months. Examination shows anemia, glossitis, hyperactive bowel sounds and pitting edema 1+. Serum albumin is 2.0 g/dL. He often eats raw freshwater fish. What is the most likely diagnosis?",
            "Capillariasis",
            ["Amoebiasis", "Strongyloidiasis", "Isosporiasis", "Opisthorchiasis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ท้องเสียเรื้อรัง + **ท้องร้อง (active bowel sound)** + **บวม ซีด ลิ้นอักเสบ (malabsorption, protein loss)** ในเกษตรกรที่กินปลาดิบ = **capillariasis**
- Amoebiasis ทำให้ถ่ายเป็นมูกเลือด ไม่ใช่ protein-losing enteropathy
- Strongyloidiasis มักมีผื่น larva currens/eosinophilia และ protein loss ไม่เด่นในคนปกติ
- Isosporiasis พบใน HIV เป็นหลัก
- Opisthorchiasis มาจากปลาดิบเหมือนกัน แต่ส่วนใหญ่ไม่มีอาการหรือมีอาการทางเดินน้ำดี ไม่ทำให้ท้องเสียเรื้อรังและบวม''',
            pearl="ท้องเสียเรื้อรัง + บวม + ท้องร้อง + ปลาดิบ = capillariasis", topic="Capillariasis diagnosis",
            ref=[f"{D} หน้า 310–312"], nl=["2.3.1(12)"]),
        mcq("ID-09-03-2",
            "A 30-year-old man has non-bloody diarrhea for 3 months with cachexia and muscle wasting. Stool examination shows peanut-shaped eggs with flattened bipolar plugs. What is the best way to prevent this infection?",
            "Avoid eating raw freshwater fish",
            ["Avoid eating raw crab", "Avoid eating raw water caltrop and water chestnut", "Avoid walking barefoot in rice fields", "Avoid eating raw snails"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไข่ **รูปถั่วลิสง bipolar flattened plug** + ท้องเสียเรื้อรังผอม = **Capillaria philippinensis** → ป้องกันโดย **งดกินปลาน้ำจืดดิบ**
- ปูดิบ → Paragonimus (ปอด)
- แห้ว/กระจับดิบ → Fasciolopsis (ลำไส้)
- เดินเท้าเปล่า → hookworm/Strongyloides (ไชผิวหนัง)
- หอยดิบ → Angiostrongylus (eosinophilic meningitis)''',
            pearl="Capillaria ป้องกันด้วยการงดปลาน้ำจืดดิบ", topic="Capillariasis prevention",
            ref=[f"{D} หน้า 310, 313–314"], nl=["2.3.1(12)"]),
        mcq("ID-09-03-3",
            "A 52-year-old man is diagnosed with intestinal capillariasis. He is dehydrated with serum albumin 1.8 g/dL. Besides fluid and nutritional support, which drug is most appropriate?",
            "Albendazole",
            ["Praziquantel", "Metronidazole", "Ivermectin single dose", "Niclosamide"],
            explain='''Capillaria เป็นพยาธิตัวกลม → **albendazole (หรือ mebendazole)** ร่วมกับ hydration และ nutrition
- Praziquantel ใช้กับใบไม้และตัวตืด
- Metronidazole ใช้กับ protozoa
- Ivermectin ใช้กับ Strongyloides ไม่ใช่ยาหลักของ Capillaria
- Niclosamide ใช้กับตัวตืด''',
            pearl="Capillaria → albendazole/mebendazole นาน", topic="Capillariasis treatment",
            ref=[f"{D} หน้า 296, 310"], nl=["2.3.1(12)"]),
    ])

# ---------------------------------------------------------------- 09-04 Misc: candidemia & pneumococcal vaccine
S4 = sec("id-09-04", "Miscellaneous: candidemia (CRBSI) & pneumococcal vaccine",
    "ไข้ใหม่ขณะได้ broad-spectrum ATB + TPN + central line → candidemia → empirical antifungal (fluconazole ตามสไลด์; echinocandin ในรายหนัก) · pneumococcal vaccine ≥ 65 ปี",
    minutes=5, source=f"{D} หน้า 317–324", nl=["2.3.1-3(7)", "B1.4.8"],
    md='''
### Catheter-related bloodstream infection จาก Candida

- Risk ของ **candidemia**: **TPN**, **central venous catheter**, **broad-spectrum antibiotics นาน** (เช่น meropenem), ผ่าตัดช่องท้อง (ลำไส้ทะลุ), ICU, neutropenia, ไตวาย (เสริม)
- ไข้ใหม่ทั้งที่ได้ carbapenem อยู่ และไม่มี source อื่น (CT ไม่มี collection, UA ปกติ) → นึกถึง **Candida CRBSI**
- **Empirical treatment: fluconazole** (ตามสไลด์) · ผู้ป่วยหนัก/ช็อก/เคยได้ azole → **echinocandin (caspofungin/micafungin)** เป็น first line ตามแนวทาง IDSA (เสริม)
- **ถอดสาย central line** · ตรวจตา (endophthalmitis) · H/C ซ้ำจนลบ แล้วรักษาต่อ 14 วันหลัง H/C ลบ (เสริม)

### Pneumococcal vaccine (สไลด์หน้า 319–324)

- **แนะนำในผู้สูงอายุ ≥ 65 ปี** (50–64 ปีพิจารณาให้ได้)
- กลุ่มเสี่ยงอื่น (เสริม): asplenia/sickle cell, HIV/ภูมิคุ้มกันต่ำ, CSF leak, cochlear implant, โรคหัวใจ ปอด ตับ ไต เรื้อรัง, DM, สูบบุหรี่, alcoholism
- ไม่ใช่ข้อบ่งชี้: หญิงตั้งครรภ์ปกติ, เด็กโตสุขภาพดี (ได้ตาม EPI แล้ว), G6PD deficiency, HT ที่คุมได้
- สูตรผู้ใหญ่ (เสริม): PCV20 1 เข็ม หรือ PCV15 ตามด้วย PPSV23
''',
    pearls=[
        "TPN + central line + broad-spectrum ATB + ไข้ใหม่ = นึกถึง Candida CRBSI",
        "Candidemia: antifungal (fluconazole/echinocandin) + ถอดสาย + ตรวจตา",
        "Pneumococcal vaccine: ≥ 65 ปีทุกคน · 50–64 พิจารณา · กลุ่มเสี่ยงทุกอายุ",
    ],
    items=[
        mcq("ID-09-04-1",
            "A 50-year-old man underwent laparotomy for a stab wound with bowel perforation and was treated with meropenem and TPN through a subclavian catheter. Ten days later he develops a new high fever. CT abdomen shows no collection and urinalysis shows no WBC or RBC. After blood cultures are drawn, which empirical antimicrobial should be added?",
            "Fluconazole",
            ["Cefepime", "Clindamycin", "Metronidazole", "Tetracycline"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไข้ใหม่ทั้งที่ได้ **meropenem** + **TPN ทาง central line** + ไม่มี source อื่น = **Candida CRBSI** → เพิ่ม antifungal (สไลด์เฉลย **fluconazole**; แนวทางปัจจุบันในผู้ป่วยหนักนิยม echinocandin) และถอดสาย
- Cefepime แคบกว่า meropenem ไม่เพิ่ม coverage
- Clindamycin และ metronidazole ครอบ anaerobe ซึ่ง meropenem ครอบอยู่แล้ว
- Tetracycline ไม่ใช่ยาสำหรับ nosocomial sepsis''',
            pearl="ไข้ใหม่ขณะได้ carbapenem + TPN = candidemia → antifungal", topic="Candidemia",
            ref=[f"{D} หน้า 317–318"], nl=["2.3.1-3(7)"]),
        mcq("ID-09-04-2",
            "A 35-year-old pregnant woman asks about pneumococcal vaccination for her family. Who in her family most needs the pneumococcal vaccine?",
            "Her healthy 68-year-old grandmother",
            ["Herself", "Her healthy 8-year-old daughter", "Her 15-year-old son with G6PD deficiency", "Her 40-year-old husband with well-controlled hypertension"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Pneumococcal vaccine **แนะนำในผู้สูงอายุ ≥ 65 ปี** (สไลด์) → ยายอายุ 68 ปีจำเป็นที่สุด
- หญิงตั้งครรภ์สุขภาพดีไม่ใช่ข้อบ่งชี้ (ควรได้ influenza, Tdap มากกว่า)
- เด็ก 8 ปีสุขภาพดีไม่ใช่กลุ่มเสี่ยง
- G6PD deficiency ไม่ใช่ภาวะ asplenia หรือภูมิคุ้มกันต่ำ
- HT ที่คุมได้ไม่ใช่ข้อบ่งชี้ (โรคหัวใจเรื้อรังจึงจะเป็น)''',
            pearl="Pneumococcal vaccine: อายุ ≥ 65 ปี", topic="Pneumococcal vaccine",
            ref=[f"{D} หน้า 319–324"], nl=["B1.4.8"]),
    ])

LECTURE = lecture("09", "Parasitic infections & miscellaneous",
    "Helminths & trematodes · Strongyloides · Capillaria · candidemia · pneumococcal vaccine",
    objectives=[
        "จัดกลุ่มพยาธิ (กลม/ใบไม้/ตืด/protozoa) และเลือกยาได้",
        "จับคู่อาหารดิบกับพยาธิใบไม้ 4 ชนิดได้",
        "ระวัง Strongyloides hyperinfection ในผู้ได้ steroid และรักษาด้วย ivermectin",
        "วินิจฉัย capillariasis และ candidemia จากบริบท และรู้ข้อบ่งชี้ pneumococcal vaccine",
    ],
    sections=[S1, S2, S3, S4])
