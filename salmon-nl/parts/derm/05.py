from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Dermato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 05-01 HSV
F_SMEAR = fig("derm-05-01-f1", "อ่าน smear จากตุ่มน้ำ/ผื่น: Tzanck vs KOH (ภาพ schematic)", '''<svg viewBox="0 0 740 300">
 <rect x="10" y="10" width="230" height="280" rx="10" class="box"/>
 <text x="125" y="34" text-anchor="middle" class="tb">Tzanck (Wright/Giemsa)</text>
 <circle cx="125" cy="120" r="56" class="c2soft"/>
 <circle cx="105" cy="105" r="13" class="c2"/><circle cx="130" cy="100" r="13" class="c2"/><circle cx="148" cy="122" r="13" class="c2"/><circle cx="118" cy="132" r="13" class="c2"/>
 <text x="125" y="200" text-anchor="middle" class="t2">Multinucleated giant cell</text>
 <text x="125" y="220" text-anchor="middle" class="t3">nuclei เบียดซ้อน (molding)</text>
 <text x="125" y="244" class="t3" text-anchor="middle">= HSV · varicella · zoster</text>
 <text x="125" y="264" class="t3" text-anchor="middle">(แยกสามโรคนี้ไม่ได้)</text>
 <rect x="255" y="10" width="230" height="280" rx="10" class="box"/>
 <text x="370" y="34" text-anchor="middle" class="tb">Tzanck: acantholytic cell</text>
 <circle cx="340" cy="110" r="26" class="c1soft"/><circle cx="340" cy="110" r="9" class="c1"/>
 <circle cx="400" cy="130" r="26" class="c1soft"/><circle cx="400" cy="130" r="9" class="c1"/>
 <text x="370" y="200" text-anchor="middle" class="t2">keratinocyte กลมหลุดเดี่ยว</text>
 <text x="370" y="220" text-anchor="middle" class="t3">ขาด desmosome</text>
 <text x="370" y="244" text-anchor="middle" class="t3">พบใน pemphigus</text>
 <text x="370" y="264" text-anchor="middle" class="t3">และ herpes (ร่วมกับ giant cell)</text>
 <rect x="500" y="10" width="230" height="280" rx="10" class="box"/>
 <text x="615" y="34" text-anchor="middle" class="tb">Tzanck ใน bullous pemphigoid</text>
 <circle cx="585" cy="110" r="16" class="badsoft"/><circle cx="579" cy="106" r="6" class="bad"/><circle cx="591" cy="114" r="6" class="bad"/>
 <circle cx="640" cy="130" r="16" class="badsoft"/><circle cx="634" cy="126" r="6" class="bad"/><circle cx="646" cy="134" r="6" class="bad"/>
 <text x="615" y="200" text-anchor="middle" class="t2">Eosinophil (2 lobes)</text>
 <text x="615" y="220" text-anchor="middle" class="t3">ไม่มี acantholytic cell</text>
 <text x="615" y="244" text-anchor="middle" class="t3">ไม่มี giant cell</text>
</svg>''', "Tzanck smear (ย้อม Wright/Giemsa) บอกได้แค่กลุ่ม — giant cell = กลุ่ม herpes ทั้งหมด, acantholysis = pemphigus (หรือ herpes), eosinophil เด่น = pemphigoid")

S1 = sec("derm-05-01", "Herpes simplex virus (HSV) infection",
    "HSV-1 ปาก-หน้า · HSV-2 อวัยวะเพศ · primary: gingivostomatitis/genital ไข้ LN · recurrent: prodrome แสบ → กลุ่มตุ่มน้ำบนพื้นแดง · Tzanck = multinucleated giant cell · oral acyclovir/valacyclovir",
    minutes=8, source=f"{D} หน้า 138–148", nl=["2.3.1(8)", "B4.2.2(5)", "B4.3(2)"],
    md='''
### เชื้อและการติดต่อ

| | HSV-1 | HSV-2 |
|---|---|---|
| ที่เป็น | **orofacial** (ปาก หน้า) | **genital** |
| ติดต่อ | **สัมผัส mucosa/สารคัดหลั่งโดยตรง** | **เพศสัมพันธ์** |

- **Primary infection → แฝงใน ganglion neuron (dormant) → reactivation เมื่อมี trigger**

### Primary infection (ส่วนใหญ่ไม่มีอาการ แต่ถ้ามีมักรุนแรง)

| ชนิด | อาการ |
|---|---|
| **Primary herpetic gingivostomatitis** (เด็ก) | **ไข้ อ่อนเพลีย ต่อมน้ำเหลืองที่คอโต** + **กลุ่มตุ่มน้ำเจ็บบนพื้นแดง/ตุ่มหนอง/แผล** ที่เหงือก กระพุ้งแก้ม ริมฝีปาก |
| **Primary genital herpes** | **ไข้ อ่อนเพลีย ต่อมน้ำเหลืองขาหนีบโต** + กลุ่มตุ่มน้ำ/แผลเจ็บที่อวัยวะเพศ-ทวารหนัก ปากมดลูก + **ปัสสาวะแสบขัด** |

### Recurrent infection

- **Trigger: ความเครียด UV trauma ประจำเดือน ภูมิคุ้มกันต่ำ**
- **Prodrome: ปวด เสียวแปลบ แสบร้อน** ตรงจุดเดิมก่อนตุ่มขึ้น
- **กลุ่มตุ่มน้ำ/ตุ่มหนอง/แผลบนพื้นแดง** ที่เดิม · **อาการน้อยกว่า primary** ไม่มีไข้
- ตัวอย่าง: **recurrent herpes labialis**, **recurrent genital herpes**

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| Primary lesion | **grouped vesicles on erythematous base** (กลุ่มตุ่มน้ำใสเล็กบนพื้นแดง) |
| ต่อมา | ตุ่มหนอง → แผลตื้นขอบหยัก (scalloped/punched-out erosion) → สะเก็ด |
| อาการ | **เจ็บ/แสบ** มากกว่าคัน |
| ตำแหน่ง | ขอบริมฝีปาก (vermilion border), อวัยวะเพศ, นิ้ว (herpetic whitlow (เสริม)) |

### Investigation

- **Tzanck smear (ย้อม Wright/Giemsa): multinucleated giant cell** (+ acantholytic cell)
- **PCR** (ไวที่สุด) · **viral culture**
- ปกติวินิจฉัยทางคลินิก

[[fig:derm-05-01-f1]]

### การรักษา

- **Oral acyclovir, valacyclovir** (เริ่มเร็วใน 72 ชม. หรือช่วง prodrome (เสริม))
- **IV acyclovir** กรณี severe (เช่น disseminated, encephalitis, ภูมิต่ำ)
- **ไม่แนะนำ acyclovir cream** (ได้ผลน้อย)
- Recurrent บ่อย ≥ 6 ครั้ง/ปี → suppressive therapy (เสริม)
''',
    figs=[F_SMEAR],
    pearls=[
        "HSV-1 ปาก · HSV-2 อวัยวะเพศ · แฝงใน ganglion แล้ว reactivate",
        "Grouped vesicles on erythematous base + prodrome แสบ = HSV",
        "Tzanck (Wright/Giemsa): multinucleated giant cell + acantholytic cell",
        "Oral acyclovir/valacyclovir · IV ถ้ารุนแรง · ไม่แนะนำ acyclovir cream",
    ],
    items=[
        mcq("DERM-05-01-1", """A 20-year-old man complains of painful lesions that recently erupted on the right side of his mouth, preceded by a day of tingling. He has long-standing acne but has never experienced pain like this before. Examination shows a cluster of small vesicles on an erythematous base at the right vermilion border. What is the most likely causative organism?""",
            "Herpes simplex virus-1", ["Herpes simplex virus-2", "Methicillin-resistant Staphylococcus aureus", "Methicillin-sensitive Staphylococcus aureus", "Cutibacterium (Propionibacterium) acnes"],
            explain="""กลุ่มตุ่มน้ำบนพื้นแดงที่ขอบริมฝีปาก เจ็บ มี prodrome เสียวแปลบ = herpes labialis จาก **HSV-1** ซึ่งเป็นเชื้อหลักของ orofacial herpes (สไลด์หน้า 138, 143–144)
- HSV-2 เป็นสาเหตุหลักของ genital herpes ผ่านเพศสัมพันธ์
- MRSA ทำให้เกิดฝีหรือ folliculitis เป็นตุ่มหนองหรือก้อนบวม ไม่ใช่กลุ่ม vesicle ที่มี prodrome ทางประสาท
- MSSA ทำให้เกิด impetigo ซึ่งเป็นสะเก็ดสีน้ำผึ้ง ไม่ใช่กลุ่มตุ่มน้ำใสเจ็บ
- C. acnes ทำให้เกิดสิว ซึ่งผู้ป่วยบอกว่าไม่เคยเจ็บแบบนี้""",
            pearl="กลุ่มตุ่มน้ำเจ็บที่ริมฝีปาก = HSV-1",
            topic="HSV-1", ref=[f"{D} หน้า 143–144"], nl=["2.3.1(8)"], kind="old", src=OLD),
        mcq("DERM-05-01-2", """A patient has a group of vesicles on an erythematous base on the left upper lip. Which bedside investigation is most appropriate to support the diagnosis?""",
            "Wright stain of a scraping from the vesicle base (Tzanck smear)", ["KOH preparation", "Fresh wet preparation", "India ink preparation", "Gram stain"],
            explain="""กลุ่มตุ่มน้ำที่ริมฝีปาก สงสัย HSV — การตรวจข้างเตียงคือ **Tzanck smear (ขูดฐานตุ่มน้ำย้อม Wright/Giemsa)** ดู **multinucleated giant cell** (สไลด์หน้า 141, 145–146)
- KOH ใช้หาเชื้อรา (hyphae, yeast)
- Fresh wet preparation ใช้ดู Trichomonas หรือ clue cell ในตกขาว
- India ink ใช้ดู Cryptococcus ใน CSF
- Gram stain ใช้หาแบคทีเรีย ไม่เห็นการเปลี่ยนแปลงของเซลล์จากไวรัส""",
            pearl="สงสัย herpes → Tzanck (Wright/Giemsa) หา giant cell",
            topic="HSV Ix", ref=[f"{D} หน้า 145–146"], nl=["2.3.1(8)", "B4.3(2)"], kind="old", src=OLD),
        mcq("DERM-05-01-3", """A 45-year-old woman has had recurrent genital vesicles 5–6 times a year for 5 years, usually triggered by menstruation or stress. Examination shows multiple irregular ulcers 0.3–0.5 cm in size and vesicles on an erythematous base on the labia. Which finding is most likely on a scraping from the lesion?""",
            "Acantholytic cells, neutrophils and multinucleated giant cells on Wright stain", ["Intracellular Gram-negative diplococci", "Pseudohyphae on KOH", "Gram-negative coccobacilli in a school-of-fish pattern", "Neutrophils and acantholytic cells only, without giant cells"],
            explain="""ตุ่มน้ำและแผลที่อวัยวะเพศเป็นซ้ำตามประจำเดือนหรือความเครียด = **recurrent genital herpes** — scraping ย้อม Wright จะเห็น **multinucleated giant cell ร่วมกับ acantholytic cell และ neutrophil** (สไลด์หน้า 140–141, 147–148)
- Gram-negative intracellular diplococci เป็นของ gonorrhea ซึ่งทำให้เกิดหนองไหล ไม่ใช่กลุ่มตุ่มน้ำ
- Pseudohyphae บน KOH เป็นของ candida (ตกขาวเป็นคราบ คันแดง)
- School of fish เป็นของ Haemophilus ducreyi (chancroid) แผลลึกขอบไม่เรียบ เจ็บ มีหนอง ไม่มี vesicle
- การพบ acantholytic cell โดยไม่มี giant cell เข้ากับ pemphigus ซึ่งไม่ได้เป็นซ้ำเฉพาะที่อวัยวะเพศตามรอบเดือน""",
            pearl="Herpes: Tzanck = multinucleated giant cell + acantholysis",
            topic="Genital herpes", ref=[f"{D} หน้า 147–148"], nl=["2.3.1(8)", "B4.3(2)"], kind="old", src=OLD),
        mcq("DERM-05-01-4", """A 3-year-old girl has had fever of 39°C, drooling and refusal to eat for 3 days. Examination shows swollen bleeding gums, multiple painful grouped vesicles and shallow ulcers on the gingiva, tongue and lips, and tender cervical lymphadenopathy. She is drinking poorly. What is the most appropriate treatment?""",
            "Oral acyclovir with hydration and analgesia", ["Topical acyclovir cream alone", "Oral amoxicillin", "Oral nystatin suspension", "Reassurance only; antiviral therapy is contraindicated in children"],
            explain="""ไข้ + กลุ่มตุ่มน้ำ/แผลที่เหงือก ลิ้น ริมฝีปาก + ต่อมน้ำเหลืองคอโต = **primary herpetic gingivostomatitis** → **oral acyclovir** (เริ่มเร็วช่วยลดระยะโรค) + ดูแลการกินน้ำและแก้ปวด (สไลด์หน้า 139, 142)
- Acyclovir cream ไม่แนะนำ และทาในปากไม่ได้ผล
- Amoxicillin ใช้กับการติดเชื้อแบคทีเรีย (เช่น strep pharyngitis) ไม่ใช่ไวรัส
- Nystatin ใช้กับ oral thrush ซึ่งเป็นคราบขาวขูดออกได้ ไม่ใช่ตุ่มน้ำ
- Acyclovir ใช้ในเด็กได้ และเด็กกำลังขาดน้ำ จึงควรรักษา ไม่ใช่แค่ reassure""",
            pearl="Primary gingivostomatitis → oral acyclovir + hydration",
            topic="HSV gingivostomatitis", ref=[f"{D} หน้า 139, 142"], nl=["2.3.1(8)"]),
    ])

# ---------------------------------------------------------------- 05-02 Varicella
S2 = sec("derm-05-02", "Varicella (chickenpox)",
    "VZV ติดทาง airborne + สัมผัส · prodrome → ผื่นหลายระยะพร้อมกัน (papule vesicle pustule crust) เริ่มหน้า หนังศีรษะ ลำตัว → แขนขา · เด็กปกติ < 12 ปี supportive · antiviral เมื่อมีความเสี่ยง",
    minutes=7, source=f"{D} หน้า 149–155", nl=["2.3.1(22)", "B4.2.2(6)"],
    md='''
### เชื้อและการติดต่อ

- **Varicella-zoster virus (VZV)**
- **Airborne droplets (ติดง่ายมาก)** + **สัมผัสน้ำในตุ่ม**
- ติดต่อได้ตั้งแต่ 1–2 วันก่อนผื่นจนตุ่มตกสะเก็ดหมด (เสริม)

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| Prodrome | **ไข้ อ่อนเพลีย ปวดหัว** |
| Primary lesion | **multistage**: papule → vesicle ("dewdrop on a rose petal" (เสริม)) → pustule → crust **อยู่พร้อมกันในบริเวณเดียว** |
| การกระจาย | **เริ่มที่หน้า หนังศีรษะ ลำตัว → แขนขา** (centripetal — ลำตัวหนาแน่นกว่าแขนขา) |
| อาการ | **คัน** |
| Mucosa | อาจมีตุ่ม/แผลในปาก (เสริม) |

> ผื่นหลายระยะพร้อมกัน = chickenpox · ผื่นระยะเดียวกันหมด หนาแน่นที่แขนขา-หน้า = smallpox (เสริม)

### Investigation

- **Tzanck: multinucleated giant cell** (+ acantholytic) · **PCR · viral culture** — **เหมือนกันหมดทั้ง HSV, chickenpox, zoster**
- ปกติวินิจฉัยทางคลินิก · ส่งตรวจเมื่อผื่นไม่ทั่วไปหรือติดเชื้อรุนแรง

### การรักษา (สไลด์หน้า 151)

- **Supportive: paracetamol, antihistamine** — **ห้ามให้ aspirin** (Reye syndrome (เสริม))
- **Antiviral เมื่อ severe หรือมี risk factor**:
  - **อายุ > 12 ปี**
  - **ภูมิคุ้มกันต่ำ**
  - **ตั้งครรภ์**
  - **โรคผิวหนัง/ปอดเรื้อรัง**
  - **ได้ aspirin อยู่**
  - **ทารกแรกเกิด/คลอดก่อนกำหนด**
- **Immunocompromised/severe → IV acyclovir** · **immunocompetent → oral acyclovir, valacyclovir** (ภายใน 24 ชม. หลังผื่นขึ้นได้ผลดีสุด (เสริม))
- **Prevention: varicella vaccine**
- ภาวะแทรกซ้อน (เสริม): ติดเชื้อแบคทีเรียซ้ำที่ผิว (S. aureus, S. pyogenes) ปอดอักเสบ (ผู้ใหญ่ ตั้งครรภ์) cerebellar ataxia
''',
    pearls=[
        "Chickenpox = ผื่นหลายระยะพร้อมกัน เริ่มหน้า-ลำตัว แล้วแขนขา คัน",
        "เด็กปกติ < 12 ปี → paracetamol + antihistamine (ห้าม aspirin)",
        "Antiviral: > 12 ปี, ภูมิต่ำ, ตั้งครรภ์, โรคผิว/ปอดเรื้อรัง, ได้ ASA, ทารกแรกเกิด",
        "Immunocompromised → IV acyclovir · ปกติ → oral acyclovir/valacyclovir",
    ],
    items=[
        mcq("DERM-05-02-1", """A 25-year-old man has had myalgia and low-grade fever for 2 days, followed by an itchy rash that began on his face and trunk and spread to the arms. Examination shows multiple discrete papules, clear vesicles, pustules and hemorrhagic crusts present at the same time, most dense on the trunk. What is the most likely diagnosis?""",
            "Chickenpox", ["Smallpox", "Disseminated herpes zoster", "Hand, foot and mouth disease", "Impetigo"],
            explain="""Prodrome แล้วผื่นคัน **หลายระยะพร้อมกัน** (papule, vesicle, pustule, crust) เริ่มหน้า-ลำตัวแล้วลงแขน หนาแน่นที่ลำตัว = **chickenpox** (สไลด์หน้า 149, 152–153)
- Smallpox ผื่นอยู่ระยะเดียวกันทั้งตัวและหนาแน่นที่หน้าและแขนขา (ถูกกำจัดแล้ว)
- Disseminated zoster มักเริ่มจากผื่นตาม dermatome ก่อนแล้วกระจาย และเกิดในผู้ป่วยภูมิต่ำ
- HFMD เป็นตุ่มน้ำรูปรีที่ฝ่ามือฝ่าเท้าและแผลในปากในเด็กเล็ก
- Impetigo เป็นสะเก็ดสีน้ำผึ้งเฉพาะที่รอบจมูกปาก ไม่มี prodrome""",
            pearl="ผื่นหลายระยะพร้อมกัน centripetal = chickenpox",
            topic="Varicella dx", ref=[f"{D} หน้า 152–153"], nl=["2.3.1(22)"], kind="old", src=OLD),
        mcq("DERM-05-02-2", """A previously healthy 6-year-old girl has had fever and a generalized rash for 3 days. Temperature is 38°C. Examination shows generalized papules, clear vesicles and pustules on the face, trunk and proximal limbs. She is alert and eating well. What is the most appropriate management?""",
            "Paracetamol and oral antihistamine", ["Oral acyclovir", "Aspirin for fever", "Topical mupirocin", "Oral cloxacillin"],
            explain="""Chickenpox ใน **เด็กสุขภาพดีอายุ < 12 ปี** ไม่มีปัจจัยเสี่ยง → **supportive: paracetamol + antihistamine** (สไลด์หน้า 151, 154–155)
- Oral acyclovir สงวนไว้สำหรับรายที่รุนแรงหรือมีปัจจัยเสี่ยง (> 12 ปี, ภูมิต่ำ, ตั้งครรภ์, โรคผิว/ปอดเรื้อรัง, ได้ aspirin, ทารกแรกเกิด) และเกิน 24 ชม. หลังผื่นขึ้นแล้วได้ประโยชน์น้อย
- Aspirin ห้ามในเด็กที่เป็นไข้จากไวรัส เพราะเสี่ยง Reye syndrome
- Mupirocin ใช้เมื่อมีติดเชื้อแบคทีเรียซ้ำ (สะเก็ดสีน้ำผึ้ง) ซึ่งโจทย์ไม่มี
- Cloxacillin ใช้กับ cellulitis/impetigo กว้าง ไม่มีข้อบ่งชี้ตอนนี้""",
            pearl="เด็กปกติ < 12 ปีเป็นอีสุกอีใส → paracetamol + antihistamine",
            topic="Varicella tx", ref=[f"{D} หน้า 154–155"], nl=["2.3.1(22)"], kind="old", src=OLD),
        mcq("DERM-05-02-3", """A 9-year-old boy receiving maintenance chemotherapy for acute lymphoblastic leukemia develops fever and a crop of vesicles and pustules on the face and trunk that is spreading rapidly. His brother had chickenpox 2 weeks ago. What is the most appropriate treatment?""",
            "Intravenous acyclovir", ["Oral acyclovir", "Paracetamol and antihistamine only", "Varicella vaccine now", "Topical calamine lotion only"],
            explain="""Chickenpox ใน **ผู้ป่วยภูมิคุ้มกันต่ำ** (ได้ chemotherapy) เสี่ยงปอดอักเสบ ตับอักเสบ และ disseminated → **IV acyclovir** (สไลด์หน้า 151)
- Oral acyclovir ใช้ในผู้ที่ภูมิคุ้มกันปกติ ดูดซึมไม่พอสำหรับผู้ป่วยภูมิต่ำ
- Supportive อย่างเดียวไม่พอในกลุ่มเสี่ยง
- Varicella vaccine เป็นวัคซีนเชื้อเป็น ห้ามในผู้ป่วยภูมิต่ำ และไม่รักษาการติดเชื้อที่เกิดแล้ว
- Calamine บรรเทาคันอย่างเดียว ไม่ได้รักษาการติดเชื้อที่อันตราย""",
            pearl="Varicella + immunocompromised → IV acyclovir",
            topic="Varicella IC", ref=[f"{D} หน้า 151"], nl=["2.3.1(22)"]),
        mcq("DERM-05-02-4", """A 22-year-old previously healthy man has had a typical chickenpox rash for 18 hours with fever of 38.5°C. He has no lung or skin disease and is not immunocompromised. What is the most appropriate management?""",
            "Oral valacyclovir (or acyclovir)", ["Intravenous acyclovir", "Supportive care only because he is immunocompetent", "Oral amoxicillin-clavulanate", "Varicella-zoster immune globulin alone"],
            explain="""ผู้ป่วยอายุ **> 12 ปี** เป็นปัจจัยเสี่ยงให้โรครุนแรง (ปอดอักเสบในผู้ใหญ่) → ให้ antiviral · ภูมิคุ้มกันปกติจึงใช้ **oral acyclovir/valacyclovir** (สไลด์หน้า 151) · เริ่มใน 24 ชม. หลังผื่นขึ้นได้ผลดีที่สุด (เสริม)
- IV acyclovir ใช้กับผู้ป่วยภูมิต่ำหรือโรครุนแรง (ปอดอักเสบ สมองอักเสบ)
- Supportive อย่างเดียวเหมาะกับเด็ก < 12 ปีที่ไม่มีปัจจัยเสี่ยง
- Amoxicillin-clavulanate ไม่ออกฤทธิ์ต่อไวรัส
- VZIG ใช้ป้องกันหลังสัมผัสในคนเสี่ยงสูงที่ยังไม่ป่วย ไม่ใช่การรักษาเมื่อผื่นขึ้นแล้ว (เสริม)""",
            pearl="Varicella อายุ > 12 ปี ภูมิปกติ → oral acyclovir/valacyclovir",
            topic="Varicella adult", ref=[f"{D} หน้า 151"], nl=["2.3.1(22)"]),
    ])

# ---------------------------------------------------------------- 05-03 Zoster
F_DERM = fig("derm-05-03-f1", "Herpes zoster: กลุ่มตุ่มน้ำตาม dermatome ข้างเดียว ไม่ข้ามแนวกลาง", '''<svg viewBox="0 0 740 340">
 <rect x="250" y="20" width="240" height="300" rx="50" class="box"/>
 <path d="M370 24V316" class="lnf"/>
 <text x="370" y="14" text-anchor="middle" class="t3">midline</text>
 <path d="M370 120C410 126 450 140 488 160" class="lnf"/>
 <path d="M370 150C410 156 450 170 488 190" class="lnf"/>
 <path d="M372 132C410 138 450 152 486 172" class="lnbad"/>
 <g>
  <circle cx="392" cy="138" r="5" class="badsoft"/><circle cx="402" cy="142" r="4" class="badsoft"/><circle cx="397" cy="132" r="4" class="badsoft"/>
  <circle cx="428" cy="148" r="5" class="badsoft"/><circle cx="438" cy="152" r="4" class="badsoft"/><circle cx="432" cy="142" r="4" class="badsoft"/>
  <circle cx="462" cy="162" r="5" class="badsoft"/><circle cx="472" cy="168" r="4" class="badsoft"/><circle cx="466" cy="156" r="4" class="badsoft"/>
 </g>
 <text x="510" y="130" class="tb">dermatome เดียว (เช่น T7)</text>
 <text x="510" y="150" class="t2">กลุ่มตุ่มน้ำบนพื้นแดง</text>
 <text x="510" y="170" class="t2">เป็นแถบจากหลังอ้อมมาหน้า</text>
 <text x="510" y="190" class="t2">หยุดที่ midline</text>
 <text x="20" y="70" class="tb">ลำดับเวลา</text>
 <text x="20" y="96" class="t2">1. prodrome 1–5 วัน</text>
 <text x="34" y="114" class="t3">ปวด แสบ เสียว คัน</text>
 <text x="20" y="140" class="t2">2. ผื่นแดง → กลุ่ม vesicle</text>
 <text x="20" y="166" class="t2">3. pustule → crust</text>
 <text x="34" y="184" class="t3">ใน 7–10 วัน (เสริม)</text>
 <text x="20" y="210" class="t2">4. ปวดค้าง &gt; 3 เดือน</text>
 <text x="34" y="228" class="t3">= postherpetic neuralgia</text>
 <rect x="20" y="256" width="210" height="64" rx="8" class="misssoft"/>
 <text x="30" y="278" class="tb">ตำแหน่งพิเศษ</text>
 <text x="30" y="298" class="t3">V1 → HZ ophthalmicus (ปลายจมูก)</text>
 <text x="30" y="314" class="t3">geniculate+CN8 → Ramsay Hunt</text>
 <rect x="510" y="230" width="210" height="80" rx="8" class="badsoft"/>
 <text x="520" y="252" class="tb">Disseminated</text>
 <text x="520" y="272" class="t3">&gt; 20 ตุ่มนอก dermatome หรือ</text>
 <text x="520" y="290" class="t3">≥ 3 dermatome (เสริม)</text>
 <text x="520" y="306" class="t3">→ IV acyclovir</text>
</svg>''', "ปวดนำก่อนผื่นหลายวัน แล้วขึ้นเป็นกลุ่มตุ่มน้ำเรียงตามแนวเส้นประสาทเส้นเดียว ข้างเดียว — ตำแหน่งตา (V1) และหู (Ramsay Hunt) ต้องส่งต่อ")

S3 = sec("derm-05-03", "Herpes zoster (shingles)",
    "VZV แฝงใน ganglion → reactivate เมื่อภูมิต่ำ/สูงอายุ · prodrome ปวดแสบ → กลุ่มตุ่มน้ำตาม dermatome ข้างเดียว · HZO (V1), Ramsay Hunt · PHN · oral acyclovir/valacyclovir · IV ถ้าภูมิต่ำ/disseminated",
    minutes=9, source=f"{D} หน้า 156–172", nl=["2.3.1(22)", "B4.2.2(6)", "B4.3(2)"],
    md='''
### กลไก

- หลังเป็น chickenpox → VZV **แฝงใน dorsal root/cranial nerve ganglion** → **reactivation เมื่อภูมิคุ้มกันลด**: **อายุมาก, มะเร็ง, HIV, ยากดภูมิ, ขาดสารอาหาร, เครียดเรื้อรัง**
- ติดต่อได้ทาง **respiratory droplets** และ **สัมผัสน้ำในตุ่ม** → คนที่ไม่เคยเป็นจะเป็น **chickenpox** (ไม่ใช่งูสวัด)

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| Prodrome | **คัน เสียวแปลบ แสบร้อน** ตามแนวเส้นประสาท |
| Primary lesion | **painful, unilateral, grouped vesicles on erythematous base along dermatome** |
| การกระจาย | ข้างเดียว 1–2 dermatome ไม่ข้ามแนวกลาง · บ่อยสุดที่ทรวงอก (เสริม) |
| ต่อมา | ตุ่มหนอง → สะเก็ด |

[[fig:derm-05-03-f1]]

### ตำแหน่งพิเศษ

- **Herpes zoster ophthalmicus (HZO)**: **ophthalmic branch ของ CN V (V1)** — ผื่นหน้าผาก-เปลือกตา ตามัว · **ผื่นที่ปลายจมูก (Hutchinson sign) = nasociliary nerve → เสี่ยงตาอักเสบ** (เสริม) → ปรึกษาจักษุแพทย์
- **Herpes zoster oticus (Ramsay Hunt syndrome)**: **geniculate ganglion + CN VIII** — ตุ่มน้ำในช่องหู/ใบหู + **facial palsy (LMN)** + หูอื้อ เวียนหัว (เสริม)

### ภาวะแทรกซ้อน (สไลด์หน้า 158)

- **Postherpetic neuralgia (PHN)** — **ปวดแสบร้อนต่อเนื่องแม้ผื่นหายแล้ว** (> 3 เดือน (เสริม)) · allodynia (สัมผัสเบา ๆ แล้วปวด)
- **Disseminated disease** · **pneumonitis, hepatitis** · **meningoencephalitis**

### Investigation

- **Tzanck: multinucleated giant cell** · **PCR · viral culture** — เหมือน HSV และ chickenpox
- ส่วนใหญ่วินิจฉัยทางคลินิก

### การรักษา (สไลด์หน้า 160)

- **Immunocompetent → oral acyclovir, valacyclovir** (ภายใน 72 ชม. หลังผื่นขึ้น (เสริม))
- **Immunocompromised / disseminated → IV acyclovir**
- **Supportive: wet compression, pain control**
- **PHN: TCA (amitriptyline), gabapentin, pregabalin**
- **Prevention: zoster vaccine ในคนอายุ > 50–60 ปี**
''',
    figs=[F_DERM],
    pearls=[
        "Zoster = prodrome ปวดแสบ → กลุ่มตุ่มน้ำตาม dermatome ข้างเดียว",
        "HZO = V1 (ผื่นปลายจมูกเสี่ยงตา) · Ramsay Hunt = geniculate + CN VIII (facial palsy)",
        "PHN = ปวดแสบค้างหลังผื่นหาย → TCA, gabapentin, pregabalin",
        "ภูมิปกติ oral acyclovir/valacyclovir · ภูมิต่ำ/disseminated IV acyclovir",
        "Zoster vaccine อายุ > 50–60 ปี",
    ],
    items=[
        mcq("DERM-05-03-1", """A 60-year-old man has had burning pain on the right side of his back for 3 days, followed by clusters of vesicles on an erythematous base in a band extending from the back to below the right costal margin. The lesions do not cross the midline. What is the most likely cause?""",
            "Varicella-zoster virus infection", ["Herpes simplex virus infection", "Cellulitis", "Allergic contact dermatitis", "Dermatitis herpetiformis"],
            explain="""ปวดแสบนำ แล้วตามด้วย **กลุ่มตุ่มน้ำเป็นแถบตาม dermatome ข้างเดียว** ในผู้สูงอายุ = **herpes zoster** จาก varicella-zoster virus reactivation (สไลด์หน้า 157, 163–164)
- HSV เป็นกลุ่มตุ่มน้ำกลุ่มเดียวขนาดเล็ก (ปาก อวัยวะเพศ) ไม่เป็นแถบยาวตาม dermatome
- Cellulitis เป็นผื่นแดงร้อนบวมขอบไม่ชัด ไม่มีกลุ่มตุ่มน้ำตามแนวเส้นประสาท
- Contact dermatitis มีรูปร่างตามของที่สัมผัส คันเด่น ไม่ใช่ปวดแสบนำแบบ neuropathic
- Dermatitis herpetiformis เป็นตุ่มน้ำเล็กคันมาก สมมาตรที่ข้อศอก เข่า ก้น สัมพันธ์ celiac""",
            pearl="Prodrome ปวด + กลุ่มตุ่มน้ำตาม dermatome ข้างเดียว = zoster",
            topic="Zoster dx", ref=[f"{D} หน้า 163–164"], nl=["2.3.1(22)"], kind="old", src=OLD),
        mcq("DERM-05-03-2", """A 70-year-old man has fever, rash and burning pain on the left side of his chest. Examination shows grouped vesicles and pustules on an erythematous base following the left T5 dermatome. What would most likely be found on microscopic examination of a scraping from the base of a vesicle?""",
            "Multinucleated giant cells", ["Spaghetti-and-meatball appearance", "Intracytoplasmic inclusion bodies (Henderson-Patterson bodies)", "Gram-negative coccobacilli", "Basophilic stippling of red cells"],
            explain="""Herpes zoster → Tzanck smear จากฐานตุ่มน้ำจะเห็น **multinucleated giant cell** เหมือน HSV และ chickenpox (สไลด์หน้า 159, 165–166)
- Spaghetti and meatballs คือ hyphae สั้นกับยีสต์ของ Malassezia ใน pityriasis versicolor
- Henderson-Patterson (molluscum) bodies เป็น inclusion ใน molluscum contagiosum ที่เป็นตุ่มเนื้อสะดือบุ๋ม (เสริม)
- Gram-negative coccobacilli ไม่ใช่เชื้อก่อตุ่มน้ำตาม dermatome
- Basophilic stippling เป็นลักษณะเม็ดเลือดแดงในพิษตะกั่ว/thalassemia ไม่ใช่ smear ผิวหนัง""",
            pearl="Tzanck ของ zoster = multinucleated giant cell",
            topic="Zoster Ix", ref=[f"{D} หน้า 165–166"], nl=["2.3.1(22)", "B4.3(2)"], kind="old", src=OLD),
        mcq("DERM-05-03-3", """A 45-year-old woman with SLE on long-term corticosteroids has a very painful vesicular rash on the right forehead, upper eyelid and the tip of her nose, with blurred vision and a red right eye. What is the most likely diagnosis?""",
            "Herpes zoster ophthalmicus", ["Ramsay Hunt syndrome", "Herpes simplex keratitis without skin involvement", "Periorbital cellulitis", "Malar rash of SLE"],
            explain="""ตุ่มน้ำปวดมากตามแขนง **ophthalmic (V1)** หน้าผาก เปลือกตา **ปลายจมูก (Hutchinson sign)** + ตามัวตาแดง ในผู้ป่วยกดภูมิ = **herpes zoster ophthalmicus** (สไลด์หน้า 157, 167–168) → ต้อง antiviral + ส่งจักษุแพทย์
- Ramsay Hunt เป็น zoster ที่ geniculate ganglion และ CN VIII มีตุ่มในหูและ facial palsy
- HSV keratitis ไม่ทำให้เกิดตุ่มน้ำกว้างตามแนว V1 บนหน้าผาก
- Periorbital cellulitis เป็นบวมแดงร้อนรอบตา ไม่มีกลุ่มตุ่มน้ำตาม dermatome
- Malar rash ของ SLE เป็นผื่นแดงรูปผีเสื้อสองข้างไม่มีตุ่มน้ำ ไม่ปวดและไม่ทำให้ตามัว""",
            pearl="ตุ่มน้ำตาม V1 + ปลายจมูก + ตามัว = HZO → ส่งจักษุ",
            topic="HZO", ref=[f"{D} หน้า 167–168"], nl=["2.3.1(22)"], kind="old", src=OLD),
        mcq("DERM-05-03-4", """A 56-year-old man had burning pain on his right arm; 3–4 days later grouped clear vesicles appeared on a red base in the same area. Over 1–2 days some became pustular. There is no itch and no fever. He is otherwise healthy and the rash began 2 days ago. What is the most appropriate treatment?""",
            "Oral acyclovir", ["Oral itraconazole", "Oral metronidazole", "Oral prednisolone", "Oral cloxacillin"],
            explain="""ปวดแสบนำแล้วเป็นกลุ่มตุ่มน้ำบนพื้นแดงที่แขนข้างเดียว = **herpes zoster** ในคนภูมิปกติ → **oral acyclovir (หรือ valacyclovir)** เริ่มภายใน 72 ชม. (สไลด์หน้า 160, 169–170)
- Itraconazole ใช้กับเชื้อรา ไม่ออกฤทธิ์ต่อไวรัส
- Metronidazole ใช้กับเชื้อ anaerobe และโปรโตซัว
- Prednisolone เดี่ยว ๆ ไม่แนะนำ และอาจทำให้ไวรัสกระจาย
- Cloxacillin ใช้กับติดเชื้อ S. aureus ตุ่มหนองที่เกิดเป็นวิวัฒนาการปกติของตุ่มน้ำ zoster ไม่ใช่ติดเชื้อแบคทีเรีย""",
            pearl="Zoster ภูมิปกติ → oral acyclovir/valacyclovir",
            topic="Zoster tx", ref=[f"{D} หน้า 169–170"], nl=["2.3.1(22)"], kind="old", src=OLD),
        mcq("DERM-05-03-5", """A 65-year-old man's herpes zoster on the left flank resolved 4 months ago. He still has constant burning pain and pain to light touch of clothing in the same area, but the skin looks normal except for faint scars. What is this complication, and which drug is most appropriate?""",
            "Postherpetic neuralgia; start gabapentin or pregabalin (or a TCA)", ["Recurrent zoster; start oral acyclovir", "Secondary bacterial infection; start oral cephalexin", "Ramsay Hunt syndrome; start prednisolone", "Acute herpetic neuralgia; continue valacyclovir for 3 months"],
            explain="""ปวดแสบร้อนและ allodynia ค้างที่เดิม **หลังผื่นหายแล้ว** = **postherpetic neuralgia** → รักษาด้วย **TCA, gabapentin, pregabalin** (สไลด์หน้า 158, 160, 171–172)
- Recurrent zoster ต้องมีตุ่มน้ำขึ้นใหม่ ซึ่งผิวตอนนี้ปกติ
- Secondary bacterial infection จะมีหนอง แดง บวม ร้อน ไม่ใช่ปวดแสบในผิวปกติ
- Ramsay Hunt เป็น zoster ที่หูและเส้นประสาทใบหน้า ไม่ใช่ที่สีข้าง
- Acute herpetic neuralgia คือปวดช่วงที่ยังมีผื่น และ antiviral ไม่ช่วยเมื่อผ่านไป 4 เดือนแล้ว""",
            pearl="ปวดค้างหลังผื่นหาย = PHN → gabapentin/pregabalin/TCA",
            topic="PHN", ref=[f"{D} หน้า 171–172"], nl=["2.3.1(22)"], kind="old", src=OLD),
    ])

# ---------------------------------------------------------------- 05-04 Warts
S4 = sec("derm-05-04", "Warts (verrucae) และ anogenital warts",
    "HPV · common wart = ตุ่มสีเนื้อผิวขรุขระที่มือ · plantar wart ต้องแยก callus (เฉือนแล้วเห็นจุดเลือด) · 1st line salicylic acid, cryotherapy · condyloma (HPV 6, 11) ก้อนเล็ก imiquimod/podophyllotoxin · ก้อนใหญ่ cryo/TCA/จี้/ผ่าตัด",
    minutes=7, source=f"{D} หน้า 173–180", nl=["2.3.12(15)", "B4.2.2(8)", "B4.4(4)"],
    md='''
### Cutaneous warts (verrucae)

- เชื้อ **human papillomavirus (HPV)** ติดต่อทาง **สัมผัสผิวโดยตรง**

| ชนิด | สิ่งที่เห็น | ตำแหน่ง |
|---|---|---|
| **Common wart (verruca vulgaris)** | **papule/plaque สีเนื้อ หนา (hyperkeratotic) ผิวขรุขระ** มีจุดดำเล็ก (thrombosed capillary (เสริม)) | **มือ นิ้ว** ลำตัว |
| **Plantar wart** | **hyperkeratotic papule/plaque ที่ฝ่าเท้า** กดเจ็บ | ฝ่าเท้า |
| Flat wart (เสริม) | ตุ่มแบนเล็กสีเนื้อ เรียงตามรอยเกา | หน้า หลังมือ |

- **Plantar wart vs callus**: **ใช้มีดเฉือนผิวแล้วเห็นจุดเลือดออก = wart** · callus เห็นเป็นชั้น keratin ใสไม่มีจุดเลือด และลายผิวยังผ่านต่อเนื่อง (เสริม)
- **Ix: skin biopsy กรณีวินิจฉัยไม่แน่ใจ**

**การรักษา** (สไลด์หน้า 175)
- **หายเองได้ใน 2 ปี**
- **1st line: topical salicylic acid, cryotherapy**
- **Refractory: laser, electrocauterization/curettage**

### Anogenital warts (condyloma acuminata)

- **HPV types 6, 11** · ติดต่อทาง **เพศสัมพันธ์**
- สิ่งที่เห็น: **ก้อนนูนยื่น (exophytic) คล้ายดอกกะหล่ำ (cauliflower-like)** สีเนื้อ-ชมพู ที่อวัยวะเพศ รอบทวารหนัก

| ขนาด | การรักษา |
|---|---|
| **รอยโรคเล็ก** → **patient-applied therapy** | **imiquimod cream, podophyllotoxin** |
| **รอยโรคใหญ่** → **provider-administered** | **cryotherapy, trichloroacetic acid (TCA), electrocautery, laser, surgical removal** |

- **Prevention: HPV vaccine** · ตรวจคัดกรอง STI อื่นและคู่นอน (เสริม) · podophyllin/imiquimod ห้ามในตั้งครรภ์ (เสริม)
''',
    pearls=[
        "Common wart = ตุ่มสีเนื้อผิวขรุขระที่มือนิ้ว · หายเองใน 2 ปี",
        "Plantar wart vs callus: เฉือนแล้วเห็นจุดเลือด = wart",
        "Wart 1st line: salicylic acid, cryotherapy · ดื้อ → laser, electrocautery",
        "Condyloma = HPV 6, 11 · ก้อนเล็ก imiquimod/podophyllotoxin · ก้อนใหญ่ cryo/TCA/จี้/ผ่าตัด",
    ],
    items=[
        mcq("DERM-05-04-1", """A 20-year-old man has a 6-mm, skin-colored, hyperkeratotic papule with a rough, cauliflower-like surface and tiny black dots on his right thumb. It is painless and has been present for 4 months. What is the most appropriate first-line management?""",
            "Topical salicylic acid or cryotherapy", ["20% urea cream", "0.1% triamcinolone acetonide cream", "Incisional biopsy", "Electrocauterization"],
            explain="""ตุ่มสีเนื้อผิวขรุขระมีจุดดำเล็กที่นิ้ว = **common wart** → **1st line: salicylic acid หรือ cryotherapy** (สไลด์หน้า 173, 175, 177–178) · ในสไลด์ตัวเลือกไม่มี salicylic/cryo เฉลยในสไลด์เป็นภาพ — ถ้าตัวเลือกไม่มี first line ตัวที่ใช้รักษาได้คือ electrocauterization (refractory)
- Urea cream ช่วยลดผิวหนาแต่ไม่ใช่การรักษามาตรฐานของหูด
- Triamcinolone เป็น steroid ไม่ออกฤทธิ์ต่อ HPV
- Incisional biopsy ใช้เมื่อวินิจฉัยไม่แน่ใจ หูดที่ลักษณะชัดไม่ต้องตัดชิ้นเนื้อ
- Electrocauterization ใช้กับหูดที่ดื้อการรักษา เจ็บกว่าและเสี่ยงแผลเป็น""",
            pearl="Common wart → salicylic acid/cryotherapy ก่อน",
            topic="Common wart tx", ref=[f"{D} หน้า 175, 177–178"], nl=["2.3.12(15)", "B4.4(4)"], kind="old", src=OLD),
        mcq("DERM-05-04-2", """A 28-year-old man has perianal itching and a protruding mass. He has had several male partners. Examination shows several small (2–4 mm) soft cauliflower-like papules around the anus with mucoid discharge. He prefers to treat himself at home. What is the most appropriate management?""",
            "Topical imiquimod cream applied by the patient", ["HPV vaccine as the treatment", "Cryoablation", "Surgical excision", "Oral acyclovir"],
            explain="""ก้อนดอกกะหล่ำเล็กรอบทวาร = **anogenital warts (condyloma acuminata, HPV 6/11)** · รอยโรค **เล็ก** → **patient-applied therapy: imiquimod cream หรือ podophyllotoxin** (สไลด์หน้า 176, 179–180)
- HPV vaccine ใช้ป้องกัน ไม่ได้รักษาหูดที่เป็นแล้ว
- Cryoablation เป็น provider-administered ใช้เมื่อรอยโรคใหญ่หรือคนไข้ทายาเองไม่ได้
- Surgical excision สงวนไว้สำหรับรอยโรคใหญ่จำนวนมาก
- Acyclovir รักษา herpes ไม่ออกฤทธิ์ต่อ HPV""",
            pearl="Condyloma เล็ก → imiquimod/podophyllotoxin ทาเอง",
            topic="Anogenital wart", ref=[f"{D} หน้า 179–180"], nl=["2.3.12(15)", "2.3.1(19)"], kind="old", src=OLD),
        mcq("DERM-05-04-3", """A 35-year-old runner has a painful 8-mm hyperkeratotic lesion on the ball of her foot. You pare it with a scalpel. Which finding best distinguishes a plantar wart from a callus?""",
            "Multiple pinpoint bleeding dots after paring", ["Translucent yellow keratin core after paring", "Skin lines (dermatoglyphics) passing uninterrupted through the lesion", "Pain on direct pressure only", "Location on a weight-bearing area"],
            explain="""**เฉือนผิวแล้วเห็นจุดเลือดออก** (thrombosed capillary ใน dermal papilla) = **plantar wart** — สไลด์ใช้จุดนี้แยกจาก callus (สไลด์หน้า 174)
- แกน keratin ใสสีเหลืองเป็นลักษณะของ corn/callus (เสริม)
- ลายผิวที่ผ่านต่อเนื่องเป็นลักษณะของ callus หูดจะทำให้ลายผิวขาด (เสริม)
- การกดเจ็บพบได้ทั้งสองอย่าง (หูดเจ็บเมื่อบีบด้านข้าง corn เจ็บเมื่อกดตรง) จึงแยกได้ไม่ชัด
- ทั้งหูดและ callus เกิดที่จุดลงน้ำหนักได้""",
            pearl="Plantar wart: เฉือนแล้วมีจุดเลือด · callus ไม่มี",
            topic="Plantar wart vs callus", ref=[f"{D} หน้า 174"], nl=["2.3.12(15)", "2.3.12(5)"]),
    ])

LECTURE = lecture("05", "Viral skin infections", subtitle="HSV · chickenpox · herpes zoster · warts",
    objectives=[
        "วินิจฉัย HSV primary/recurrent และเลือก Tzanck/PCR กับ oral acyclovir ได้",
        "บอกข้อบ่งชี้ antiviral ใน chickenpox และแยก oral กับ IV acyclovir",
        "วินิจฉัย herpes zoster, HZO, Ramsay Hunt และรักษา PHN",
        "แยก plantar wart จาก callus และเลือกการรักษา wart/condyloma ตามขนาด",
    ],
    sections=[S1, S2, S3, S4])
