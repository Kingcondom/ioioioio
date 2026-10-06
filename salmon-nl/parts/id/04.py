from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Infectious"

# ---------------------------------------------------------------- 04-01 Anthrax
S1 = sec("id-04-01", "Anthrax",
    "B. anthracis จากสัตว์/ขนสัตว์ · cutaneous พบบ่อยสุด: eschar ใหญ่ไม่เจ็บ บวมรอบ ๆ · GPB ใหญ่เรียงสาย box-car · ciprofloxacin/doxycycline",
    minutes=5, source=f"{D} หน้า 145–149, 38–39", nl=["2.3.1-3(9)", "B1.5.2(8)"],
    md='''
### เชื้อและการติดต่อ

- **Bacillus anthracis** (Gram-positive, สร้าง spore)
- สัมผัส **ปศุสัตว์ที่ติดเชื้อ หรือผลิตภัณฑ์จากสัตว์** (ขนสัตว์ หนัง เนื้อ)
- Risk: ผู้สัมผัสสัตว์ — นายพราน คนตัดขนสัตว์ คนชำแหละเนื้อ (butcher) สัตวแพทย์
- **เคยใช้เป็น bioterrorism** (spore ทางจดหมาย)

### 3 รูปแบบ

| รูปแบบ | ลักษณะ |
|---|---|
| **Cutaneous (most common)** | papule → vesicle → **ulcer/eschar ดำขนาดใหญ่ ไม่เจ็บ** มี **surrounding edema มาก** · ที่ **มือ แขน หน้า** |
| Inhalation | flu-like → **hemorrhagic mediastinitis** (CXR **widened mediastinum**) → shock · ตายสูง |
| Gastrointestinal | กินเนื้อสัตว์ดิบ/ไม่สุก → **GI ulceration** เลือดออก ascites |

### Investigation

- Gram stain & culture: **large Gram-positive bacilli in chains — "box-car" appearance**
- PCR, serology

### Management

- **Cutaneous: ciprofloxacin หรือ doxycycline** (7–10 วัน (เสริม))
- **Antitoxin** (raxibacumab/obiltoxaximab) กรณี severe/systemic (เสริมชื่อยา)
- Inhalation/systemic: IV ciprofloxacin + ยาอื่นอีก 1–2 ตัว (เสริม)
- Prevention: **วัคซีนในสัตว์** · สวมถุงมือก่อนสัมผัสสัตว์/ผลิตภัณฑ์ · ล้างมือ · สวมหน้ากากถ้าต้องสูดละอองจากขนสัตว์

### Eschar: anthrax vs scrub typhus

| | Cutaneous anthrax | Scrub typhus |
|---|---|---|
| ขนาด | **ใหญ่** + **บวมรอบมาก** | เล็ก |
| ตำแหน่ง | มือ แขน หน้า | รักแร้ ขาหนีบ ใต้ราวนม |
| ประวัติ | สัมผัสสัตว์/ขนสัตว์ | เข้าป่า น้ำตก |
| ยา | Ciprofloxacin/doxycycline | Doxycycline/azithromycin |

> Butcher/คนเลี้ยงสัตว์ + **แผลดำที่มือไม่เจ็บ บวมมาก** + **GPB** = anthrax
''',
    pearls=[
        "Cutaneous anthrax พบบ่อยสุด: eschar ใหญ่ไม่เจ็บ + บวมรอบ ๆ มาก ที่มือ/หน้า",
        "Large GPB in chains = box-car appearance",
        "Inhalation anthrax = hemorrhagic mediastinitis (widened mediastinum)",
        "Cutaneous: ciprofloxacin หรือ doxycycline · severe เพิ่ม antitoxin",
    ],
    items=[
        mcq("ID-04-01-1",
            "A butcher presents with a painless black ulcer on his hand surrounded by marked non-pitting edema. Gram stain of the lesion shows large Gram-positive bacilli. What is the most likely pathogen?",
            "Bacillus anthracis",
            ["Corynebacterium diphtheriae", "Clostridium perfringens", "Pasteurella multocida", "Nocardia species"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''อาชีพสัมผัสเนื้อสัตว์ + **แผลดำไม่เจ็บที่มือ บวมมาก** + **GPB ขนาดใหญ่** = **cutaneous anthrax (B. anthracis)**
- C. diphtheriae เป็น GPB แต่ทำให้ pseudomembrane ในคอ (หรือแผลผิวหนังตื้น) ไม่ใช่ eschar จากสัตว์
- C. perfringens เป็น GPB ที่ทำให้ gas gangrene ซึ่งเจ็บมาก มี crepitus
- Pasteurella multocida เป็น Gram-negative ทำให้ cellulitis หลังสัตว์กัด/ข่วน
- Nocardia เป็น Gram-positive branching filament ทำให้ pneumonia/ฝีในคนภูมิต่ำ''',
            pearl="แผลดำไม่เจ็บ + สัมผัสสัตว์ + GPB = anthrax", topic="Anthrax pathogen",
            ref=[f"{D} หน้า 148–149"], nl=["2.3.1-3(9)"]),
        mcq("ID-04-01-2",
            "A 35-year-old wool sorter develops a painless papule on the forearm that becomes a black eschar with extensive surrounding edema. Gram stain shows large Gram-positive rods arranged in chains like box-cars. He is afebrile with stable vital signs. What is the most appropriate treatment?",
            "Oral ciprofloxacin",
            ["Oral doxycycline plus intravenous antitoxin", "Oral azithromycin", "Topical mupirocin", "Surgical excision of the eschar"],
            explain='''**Cutaneous anthrax ไม่รุนแรง** → **ciprofloxacin หรือ doxycycline** (ตามสไลด์)
- Antitoxin ให้เฉพาะ severe/systemic disease ซึ่งรายนี้ไม่มี
- Azithromycin ไม่ใช่ยาหลักของ anthrax
- Mupirocin ใช้กับ impetigo ไม่ครอบคลุม anthrax
- การผ่าตัดตัด eschar ไม่จำเป็นและอาจทำให้เชื้อกระจาย (เสริม)''',
            pearl="Cutaneous anthrax → ciprofloxacin/doxycycline", topic="Anthrax treatment",
            ref=[f"{D} หน้า 146–147"], nl=["2.3.1-3(9)"]),
        mcq("ID-04-01-3",
            "A patient has a black eschar with fever. Which feature favors cutaneous anthrax over scrub typhus?",
            "A large lesion on the hand with marked surrounding edema after handling animal hides",
            ["A small lesion in the axilla after hiking near a waterfall", "Regional tender lymphadenopathy with relative bradycardia", "A lesion hidden under the underwear line", "Rapid defervescence within 48 hours of doxycycline"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ดัดแปลงจากสไลด์หน้า 38–39)",
            explain='''Anthrax eschar **ใหญ่ มีบวมรอบมาก** อยู่ที่ **มือ แขน หน้า** (ส่วนที่สัมผัสสัตว์/ขนสัตว์)
- แผลเล็กที่รักแร้หลังไปน้ำตก เป็นลักษณะ scrub typhus
- LN โตกับ relative bradycardia เป็นลักษณะ scrub typhus/rickettsia
- แผลใต้ร่มผ้า (ขาหนีบ ใต้ราวนม) เป็นตำแหน่งที่ chigger mite ชอบกัด
- ไข้ลงเร็วภายใน 48 ชม. หลัง doxycycline เป็นลักษณะ scrub typhus''',
            pearl="Eschar ใหญ่บวมที่มือ = anthrax · เล็กใต้ร่มผ้า = scrub", topic="Eschar differential",
            ref=[f"{D} หน้า 38–39, 145"], nl=["2.3.1-3(9)", "B1.5.2(8)"]),
    ])

# ---------------------------------------------------------------- 04-02 Diphtheria
S2 = sec("id-04-02", "Diphtheria",
    "C. diphtheriae + toxin · ไม่ได้วัคซีน · grayish pseudomembrane เลยออกนอก tonsil ขูดแล้วเลือดออก · bull neck · myocarditis · DAT + penicillin G/erythromycin",
    minutes=6, source=f"{D} หน้า 150–156, 99", nl=["2.3.1(4)", "B6.2.2(6)"],
    md='''
### เชื้อและการติดต่อ

- **Corynebacterium diphtheriae** สร้าง **diphtheria toxin** (ยับยั้ง EF-2 → เซลล์ตาย (เสริม))
- **Respiratory droplets** · Risk: **ได้วัคซีนไม่ครบ** (ระบาดในชุมชนที่ครอบคลุมวัคซีนต่ำ)

### อาการ

- Prodrome: fever, malaise, sore throat
- **Grayish-white pseudomembrane** บน **tonsil, uvula, oropharynx** (ลามเลยขอบ tonsil) · **ขูดแล้วเลือดออก**
- **Cervical lymphadenopathy + soft tissue บวม = bull neck**
- Laryngeal diphtheria → **stridor**, airway obstruction
- Toxin กระจาย → **myocarditis, arrhythmia** (สัปดาห์ที่ 1–2) · neuropathy (palatal palsy) (เสริม)

### Investigation

- Nasal/throat swab → Gram stain, culture (Loeffler/tellurite (เสริม))
- **Gram-positive, club-shaped bacilli** เรียงแบบ **Chinese letter**
- **Elek test** ยืนยันการสร้าง toxin
- EKG/troponin ดู myocarditis (เสริม)

### Management

1. **Airway support** · **tracheostomy** กรณี airway บวมมาก หรือเสี่ยง pseudomembrane หลุดอุดทางเดินหายใจ
2. **Diphtheria antitoxin (DAT)** ให้เร็วที่สุดตามอาการ (ไม่ต้องรอผล culture)
3. **ATB: penicillin G หรือ erythromycin** (14 วัน (เสริม)) — **ไม่ได้รักษาอาการที่เกิดจาก toxin** แต่ลดจำนวนเชื้อไม่ให้สร้าง toxin เพิ่ม และลดการแพร่เชื้อ
4. แยกผู้ป่วย (droplet) · ผู้สัมผัสใกล้ชิด: เพาะเชื้อ + ให้ erythromycin/benzathine penicillin + วัคซีน (เสริม)

### Prevention (วัคซีน)

| วัคซีน | ใช้กับ |
|---|---|
| DTwP / DTaP | **เด็ก < 7 ปี** (D, P ตัวใหญ่ = ขนาดเต็ม) |
| Td / Tdap | **เด็ก ≥ 7 ปี และผู้ใหญ่** (**d** = ลดปริมาณ diphtheria · **p** = ลดปริมาณ pertussis) |

- ผู้ใหญ่ควรได้ Td กระตุ้นทุก 10 ปี (เสริม)

### DDx เจ็บคอมี exudate

| | Diphtheria | Strep group A | IM |
|---|---|---|---|
| Membrane | **Grayish pseudomembrane เลย tonsil ขูดแล้วเลือดออก** | Exudate บน tonsil | Exudate ขาว |
| LN | Bull neck | Anterior เท่านั้น | Anterior + posterior |
| HSM | ไม่มี | ไม่มี | มี |
''',
    pearls=[
        "Diphtheria: grayish pseudomembrane ลามเลย tonsil ขูดแล้วเลือดออก + bull neck",
        "GPB club-shaped Chinese letter · Elek test = ยืนยัน toxin",
        "รักษา: airway + DAT + penicillin G/erythromycin (ATB ไม่แก้ toxin)",
        "DTaP/DTwP < 7 ปี · Td/Tdap ≥ 7 ปีและผู้ใหญ่",
        "Toxin → myocarditis/arrhythmia ต้องติดตาม EKG",
    ],
    items=[
        mcq("ID-04-02-1",
            "A man has a sore throat. Examination shows enlarged tonsils with a grayish patch extending over the pharynx and tonsils, bilateral anterior cervical lymph node enlargement, and no hepatosplenomegaly. He did not complete childhood vaccination. What is the most likely diagnosis?",
            "Diphtheria",
            ["Infectious mononucleosis", "Streptococcal tonsillitis", "Oral candidiasis", "Vincent angina"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**Grayish patch ลามบน pharynx และ tonsil** + LN คอ + **ไม่มี HSM** + วัคซีนไม่ครบ = **diphtheria**
- IM มี HSM และ posterior cervical LN มี atypical lymphocyte
- Strep tonsillitis มี exudate บน tonsil แต่ไม่เป็นแผ่น grayish pseudomembrane ลามไป pharynx
- Oral candidiasis เป็นคราบขาวขูดออกได้ มักไม่มีไข้หรือ LN โต
- Vincent angina (anaerobe) เป็นแผลเน่าข้างเดียว กลิ่นเหม็น''',
            pearl="Grayish membrane ลามเลย tonsil = diphtheria", topic="Diphtheria diagnosis",
            ref=[f"{D} หน้า 150, 153–154"], nl=["2.3.1(4)"]),
        mcq("ID-04-02-2",
            "A 25-year-old man has fever and sore throat. Examination shows a dirty white membrane on the tonsil that bleeds when scraped. Diphtheria antitoxin has been requested. What is the most appropriate antibiotic?",
            "Penicillin G",
            ["Vancomycin", "Levofloxacin", "Ceftriaxone", "Ceftazidime"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Pseudomembrane ขูดแล้วเลือดออก = **diphtheria** → ATB คือ **penicillin G หรือ erythromycin** (ร่วมกับ airway support + DAT)
- Vancomycin ครอบ Gram-positive ได้ แต่ไม่ใช่ยามาตรฐานของ diphtheria
- Levofloxacin ไม่ใช่ยาที่แนะนำ
- Ceftriaxone ไม่อยู่ในสูตรมาตรฐาน
- Ceftazidime เน้น Gram-negative/Pseudomonas''',
            pearl="Diphtheria: DAT + penicillin G หรือ erythromycin", topic="Diphtheria treatment",
            ref=[f"{D} หน้า 152, 155–156"], nl=["2.3.1(4)"]),
        mcq("ID-04-02-3",
            "A 9-year-old unvaccinated boy with confirmed pharyngeal diphtheria has received antitoxin and penicillin. On day 8 he develops tachycardia, gallop rhythm and ST-T changes on ECG. What is the most likely cause?",
            "Toxin-mediated myocarditis",
            ["Acute rheumatic fever", "Penicillin-induced hypersensitivity", "Serum sickness from antitoxin", "Infective endocarditis"],
            explain='''Diphtheria toxin กระจายทางเลือด → **myocarditis/arrhythmia** มักเกิดสัปดาห์ที่ 1–2 แม้รักษาแล้ว — ATB ไม่ย้อนผลของ toxin ที่จับเนื้อเยื่อไปแล้ว
- Acute rheumatic fever เกิดหลัง strep 2–4 สัปดาห์ มี arthritis/carditis ตามเกณฑ์ Jones
- Penicillin hypersensitivity มีผื่น/anaphylaxis ไม่ใช่ gallop และ ST-T changes
- Serum sickness จาก antitoxin (ซีรั่มม้า) มีไข้ ผื่น ปวดข้อ ราว 7–10 วัน แต่ไม่ทำให้หัวใจวาย
- Infective endocarditis ต้องมี bacteremia และ murmur ใหม่''',
            pearl="Diphtheria + หัวใจเต้นผิดจังหวะ/หัวใจวาย = toxin myocarditis", topic="Diphtheria complication",
            ref=[f"{D} หน้า 150"], nl=["2.3.1(4)"]),
    ])

# ---------------------------------------------------------------- 04-03 Pertussis
S3 = sec("id-04-03", "Pertussis (whooping cough)",
    "B. pertussis · catarrhal (แพร่มากสุด) → paroxysmal (ไอเป็นชุด + whoop + อาเจียน) → convalescent · WBC สูง lymphocytosis · macrolide",
    minutes=5, source=f"{D} หน้า 157–162", nl=["2.3.1(6)", "B6.2.2(7)"],
    md='''
### เชื้อและการติดต่อ

- **Bordetella pertussis** (Gram-negative coccobacilli) สร้าง **pertussis toxin**
- **Respiratory droplets** · พบบ่อยในเด็ก แต่ผู้ใหญ่ที่ภูมิจากวัคซีนลดลงเป็นได้ (ไอเรื้อรัง) · Risk: วัคซีนไม่ครบ

### สามระยะ

| ระยะ | ระยะเวลา | อาการ |
|---|---|---|
| **Catarrhal** | **7–10 วัน** | ไข้ต่ำ ไอเล็กน้อย น้ำมูก — **ระยะที่แพร่เชื้อมากที่สุด** |
| **Paroxysmal** | **1–6 สัปดาห์** | **ไอรุนแรงเป็นชุด ๆ ชุดละ 20–50 ครั้ง** · **inspiratory whoop** · dyspnea · **post-tussive vomiting** |
| Convalescent | หลายสัปดาห์–เดือน | ค่อย ๆ หาย (ไอได้นานจึงเรียก "ไอร้อยวัน") |

- **Complications**: pneumonia, **apnea (ทารก)**, seizure, inguinal hernia · subconjunctival hemorrhage, rib fracture (เสริม)
- ระหว่างชุดไอผู้ป่วยดูปกติ ปอดฟังได้ปกติ

### Investigation

- CBC: **↑WBC with lymphocyte predominance** (lymphocytosis)
- **Nasopharyngeal aspiration/swab**: **culture = gold standard** · **PCR** (sensitivity สูง)

### Management

- **Supportive**: respiratory support, suctioning
- **ATB: oral macrolide (azithromycin, clarithromycin, erythromycin) หรือ TMP/SMX** (แพ้ macrolide)
  - ATB ในระยะ paroxysmal ไม่ค่อยลดอาการไอ แต่ **ลดการแพร่เชื้อ** (เสริม)
  - ให้ post-exposure prophylaxis (azithromycin) กับผู้สัมผัสใกล้ชิดโดยเฉพาะทารก/หญิงตั้งครรภ์ (เสริม)

### Prevention

- **Whole-cell vaccine (wP): DTwP** · **acellular (aP): DTaP, Tdap**
- **Tdap ในหญิงตั้งครรภ์ (27–36 สัปดาห์) ทุกครรภ์** เพื่อส่งภูมิให้ทารก (เสริม)

> ผู้ใหญ่ไอเป็นชุด ๆ จนหายใจเข้าดังวู้ป/อาเจียน ปอดปกติ + lymphocytosis = pertussis → **azithromycin**
''',
    pearls=[
        "Pertussis: catarrhal → paroxysmal (ไอเป็นชุด 20–50 ครั้ง whoop อาเจียน) → convalescent",
        "Catarrhal phase แพร่เชื้อมากที่สุด",
        "WBC สูง lymphocytosis เด่น",
        "Culture NP = gold standard · PCR ไวสูง",
        "Macrolide (azithro) หรือ TMP/SMX",
    ],
    items=[
        mcq("ID-04-03-1",
            "A 23-year-old man has paroxysms of coughing followed by gasping for air and occasional vomiting. Temperature 38.3 °C, BP 125/65 mmHg, PR 105 bpm, RR 14/min, SpO2 98% on room air. Lungs are clear. Hb 12 g/dL, WBC 13,500/mm3 with lymphocytosis, platelets 197,000/mm3. What is the most appropriate management?",
            "Azithromycin",
            ["Penicillin", "Inhaled bronchodilator", "Systemic corticosteroid", "Intravenous fluids"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไอเป็นชุด + หายใจเข้าเฮือก (whoop) + อาเจียนหลังไอ + ปอดปกติ + **WBC สูง lymphocytosis** = **pertussis** → **macrolide (azithromycin)**
- Penicillin ไม่ครอบคลุม B. pertussis ได้ดี
- Bronchodilator ใช้ใน asthma — ปอดปกติ SpO2 ปกติ
- Corticosteroid ไม่มีหลักฐานว่าช่วย pertussis
- IV fluid ไม่จำเป็น ไม่ได้ขาดน้ำ''',
            pearl="ไอเป็นชุด + whoop + lymphocytosis = pertussis → azithromycin", topic="Pertussis treatment",
            ref=[f"{D} หน้า 161–162"], nl=["2.3.1(6)"]),
        mcq_ordered("ID-04-03-2",
            "A 6-year-old child's mother asks during which stage of pertussis her child is most contagious.",
            ["Incubation period", "Catarrhal stage", "Paroxysmal stage", "Convalescent stage", "After 5 days of azithromycin"], 1,
            explain='''**Catarrhal stage (7–10 วันแรก)** เชื้อในทางเดินหายใจมากที่สุดและอาการคล้ายหวัดธรรมดา จึงแพร่เชื้อได้มากที่สุด (ตามสไลด์)
- Incubation period ยังไม่มีอาการ แพร่เชื้อน้อย
- Paroxysmal stage ยังแพร่ได้ แต่ปริมาณเชื้อลดลงเรื่อย ๆ แม้อาการเด่นที่สุด
- Convalescent stage ค่อย ๆ หาย แทบไม่แพร่เชื้อ
- หลังได้ azithromycin ครบ 5 วัน ถือว่าพ้นระยะแพร่เชื้อแล้ว (เสริม)''',
            pearl="Pertussis แพร่มากสุดใน catarrhal stage", topic="Pertussis stages",
            ref=[f"{D} หน้า 158"], nl=["2.3.1(6)"]),
        mcq("ID-04-03-3",
            "A 28-year-old woman at 30 weeks' gestation asks which vaccine she should receive during pregnancy to protect her newborn from whooping cough. Which is most appropriate?",
            "Tdap",
            ["DTwP", "DTaP", "Td only", "Oral azithromycin prophylaxis at delivery"],
            explain='''ผู้ใหญ่/หญิงตั้งครรภ์ใช้ **Tdap** (ขนาด diphtheria และ pertussis ลดลง) ฉีดช่วง 27–36 สัปดาห์ทุกครรภ์เพื่อส่ง antibody ให้ทารก (เสริม)
- DTwP และ DTaP เป็นสูตรขนาดเต็มสำหรับเด็ก < 7 ปี ไม่ใช้ในผู้ใหญ่
- Td ไม่มีส่วนของ pertussis จึงไม่ป้องกันไอกรน
- Azithromycin prophylaxis ใช้หลังสัมผัสผู้ป่วย ไม่ใช่การสร้างภูมิให้ทารกระยะยาว''',
            pearl="ผู้ใหญ่/ตั้งครรภ์ = Tdap · เด็ก < 7 ปี = DTaP/DTwP", topic="Pertussis vaccine",
            ref=[f"{D} หน้า 152, 160"], nl=["2.3.1(6)", "B1.4.8"]),
    ])

# ---------------------------------------------------------------- 04-04 Mucormycosis
F_MOLD = fig("id-04-04-f1", "Mucormycosis vs aspergillosis: hyphae ใต้กล้อง", '''<svg viewBox="0 0 740 300">
 <rect x="10" y="10" width="350" height="280" rx="12" class="badsoft"/>
 <text x="185" y="36" text-anchor="middle" class="tb">Mucorales (Rhizopus, Mucor)</text>
 <path d="M40 150C90 140 130 160 180 150C220 142 260 160 320 150" class="lnbad"/>
 <path d="M40 162C90 152 130 172 180 162C220 154 260 172 320 162" class="lnbad"/>
 <path d="M180 150C186 120 190 90 196 70" class="lnbad"/>
 <path d="M190 154C198 124 202 94 208 70" class="lnbad"/>
 <text x="215" y="90" class="t3">แตกแขนงมุมฉาก (90°)</text>
 <text x="40" y="200" class="t2">• Broad, ribbon-like (กว้าง 6–25 µm)</text>
 <text x="40" y="222" class="t2">• Nonseptate (ไม่มีผนังกั้น)</text>
 <text x="40" y="244" class="t2">• Wide/right-angle branching</text>
 <text x="40" y="270" class="tb">Amphotericin B (voriconazole ไม่ได้ผล)</text>
 <rect x="380" y="10" width="350" height="280" rx="12" class="c1soft"/>
 <text x="555" y="36" text-anchor="middle" class="tb">Aspergillus</text>
 <path d="M410 160L600 120" class="lnc1"/>
 <path d="M415 168L605 128" class="lnc1"/>
 <path d="M450 150L456 158M490 142L496 150M530 133L536 141M570 125L576 133" class="lnc1"/>
 <path d="M520 136L600 70" class="lnc1"/>
 <path d="M526 140L606 74" class="lnc1"/>
 <path d="M550 116L556 120M575 96L581 100" class="lnc1"/>
 <text x="612" y="90" class="t3">มุมแหลม 45°</text>
 <text x="410" y="200" class="t2">• Narrow, uniform (3–6 µm)</text>
 <text x="410" y="222" class="t2">• Septate (มีผนังกั้น)</text>
 <text x="410" y="244" class="t2">• Acute-angle (45°) branching</text>
 <text x="410" y="270" class="tb">Voriconazole (1st line)</text>
</svg>''', "Mucor: hyphae ใหญ่ ไม่มี septum แตกแขนงมุมกว้าง · Aspergillus: hyphae เล็ก มี septum แตกแขนงมุมแหลม 45° — ยาต่างกัน (สไลด์หน้า 166–167 เป็นภาพ วาดเสริม)")

S4 = sec("id-04-04", "Mucormycosis",
    "Rhizopus/Mucor · DM คุมไม่ได้ (DKA), ภูมิต่ำ · rhinocerebral: eschar ดำที่จมูก/เพดาน ตาโปน CN palsy · broad nonseptate right-angle · surgery + amphotericin B",
    minutes=6, source=f"{D} หน้า 163–170", nl=["2.3.1-3(7)"],
    md='''
### เชื้อและการติดต่อ

- **Mucorales (Rhizopus, Mucor spp.)**
- **สูด spore** · direct inoculation (บาดแผล) · ingestion
- Risk: **DM คุมไม่ได้ (โดยเฉพาะ DKA)**, immunosuppression (neutropenia, steroid, transplant), iron overload/deferoxamine (เสริม)

### รูปแบบ

- **Rhinocerebral** (พบบ่อยใน DKA): ไข้ คัดจมูก **ปวด/บวมหน้า** · **black eschar ที่หน้า/เพดาน/turbinate** · ตาบวม **proptosis, chemosis** · ตามัว เห็นภาพซ้อน **CN palsy** · **cavernous sinus thrombosis**
- **Pulmonary** (neutropenia/hematologic malignancy): ไข้ หอบ **hemoptysis**
- Cutaneous, gastrointestinal, disseminated
- กลไก: **hyphae รุกเข้าหลอดเลือด (angioinvasion) → thrombosis → เนื้อเยื่อตาย (necrosis)** → eschar ดำ

### Investigation

- **Tissue biopsy (confirm test)**: **irregular, broad, nonseptate hyphae** · **wide/right-angled branching**
- CT/MRI sinus-orbit-brain ดูขอบเขต (เสริม)

[[fig:id-04-04-f1]]

### Mucormycosis vs aspergillosis (สไลด์ 166–167 เป็นภาพ — สรุปเสริม)

| | Mucormycosis | Invasive aspergillosis |
|---|---|---|
| Risk เด่น | **DKA**, DM, iron overload | **Prolonged neutropenia**, transplant, steroid |
| Hyphae | **Broad, nonseptate, right-angle** | **Narrow, septate, acute-angle (45°)** |
| ภาพ | Eschar ดำ จมูก/เพดาน · reverse halo sign ใน CT ปอด | Halo sign, air-crescent · galactomannan + |
| ยา | **Amphotericin B** + surgery | **Voriconazole** |

### Management (ต้องทำทั้ง 3 อย่าง)

1. **Radical surgical debridement** ของเนื้อตาย (เร่งด่วน)
2. **Antifungal: IV amphotericin B (1st line, liposomal 5–10 mg/kg/d (เสริม))** → step down เป็น **oral posaconazole หรือ isavuconazole**
3. **แก้ underlying**: คุมน้ำตาล/แก้ DKA · ลด immunosuppressant

> **Voriconazole และ fluconazole ไม่ได้ผลกับ Mucorales** — ผู้ป่วยที่ได้ voriconazole prophylaxis แล้วยังติดเชื้อรา ให้นึกถึง mucor (เสริม)
''',
    figs=[F_MOLD],
    pearls=[
        "DKA + eschar ดำที่จมูก/เพดาน + ตาโปน = rhinocerebral mucormycosis",
        "Broad nonseptate ribbon-like hyphae แตกแขนงมุมฉาก",
        "Surgery + IV amphotericin B + คุมน้ำตาล · step down posaconazole/isavuconazole",
        "Aspergillus = septate 45° → voriconazole (ไม่ได้ผลกับ mucor)",
    ],
    items=[
        mcq("ID-04-04-1",
            "A young woman has persistent fever for 7 days after chemotherapy for acute leukemia despite broad-spectrum antibiotics. She develops dyspnea, hemoptysis and crepitations. Bronchoalveolar lavage shows broad, nonseptate hyphae with wide-angle branching. What is the most likely pathogen?",
            "Rhizopus species",
            ["Aspergillus fumigatus", "Candida albicans", "Pneumocystis jirovecii", "Cryptococcus neoformans"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ภาพ BAL บรรยายเป็นข้อความ)",
            explain='''**Broad, nonseptate hyphae + wide/right-angle branching** = **Mucorales (Rhizopus, Mucor)** → pulmonary mucormycosis (สไลด์เฉลย)
- Aspergillus ก็พบใน neutropenia แต่ hyphae แคบ **มี septum** แตกแขนงมุมแหลม 45° — ต้องดูลักษณะเชื้อ ไม่ใช่แค่บริบท
- Candida เป็น yeast + pseudohyphae ไม่ใช่ broad hyphae
- Pneumocystis เป็น cyst ย้อม GMS ไม่มี hyphae
- Cryptococcus เป็น yeast มี capsule''',
            pearl="Broad nonseptate right-angle = mucor · narrow septate 45° = aspergillus", topic="Mucor morphology",
            ref=[f"{D} หน้า 165, 169–170"], nl=["2.3.1-3(7)"]),
        mcq("ID-04-04-2",
            "A 52-year-old man with poorly controlled diabetes presents in diabetic ketoacidosis with facial pain, left periorbital swelling, proptosis and ophthalmoplegia. There is a black necrotic eschar on the hard palate. What is the most appropriate antifungal therapy?",
            "Intravenous liposomal amphotericin B",
            ["Intravenous voriconazole", "Oral fluconazole", "Intravenous caspofungin", "Oral itraconazole"],
            explain='''**DKA + eschar ดำที่เพดาน + ตาโปน CN palsy** = **rhinocerebral mucormycosis** → **IV amphotericin B (1st line)** ร่วมกับ radical surgical debridement และแก้ DKA
- Voriconazole ใช้กับ aspergillosis แต่ **ไม่ได้ผลกับ Mucorales**
- Fluconazole ไม่ครอบคลุมเชื้อราสาย mold
- Caspofungin (echinocandin) ไม่ได้ผลเดี่ยว ๆ กับ mucor
- Itraconazole ไม่ใช่ยามาตรฐาน ใช้ step down คือ posaconazole/isavuconazole''',
            pearl="Mucor → amphotericin B + surgery + คุมน้ำตาล", topic="Mucor treatment",
            ref=[f"{D} หน้า 163–164, 168"], nl=["2.3.1-3(7)"]),
        mcq("ID-04-04-3",
            "In the patient with rhinocerebral mucormycosis, intravenous amphotericin B has been started and glucose is being corrected. Imaging shows necrosis of the maxillary sinus and palate. What is the next most important intervention?",
            "Urgent radical surgical debridement",
            ["Hyperbaric oxygen as sole therapy", "Switch to oral posaconazole immediately", "Add intravenous high-dose corticosteroid for orbital swelling", "Repeat biopsy after 2 weeks of antifungal therapy"],
            explain='''Mucor ทำให้หลอดเลือดอุดตันและเนื้อตาย ยาเข้าไม่ถึง → ต้อง **radical surgery ตัดเนื้อตาย** ร่วมกับ amphotericin B และแก้ underlying (สไลด์ให้เป็นการรักษาหลักข้อแรก)
- Hyperbaric oxygen เป็นเพียงการรักษาเสริมในบางที่ ไม่ใช้แทนการผ่าตัด
- Posaconazole ใช้เป็น step down หลังอาการดีขึ้น ไม่ใช่เปลี่ยนทันที
- Corticosteroid กดภูมิคุ้มกันและทำให้น้ำตาลสูง แย่ลง
- การรอ 2 สัปดาห์เสียเวลา โรคลุกลามเข้าสมองเร็ว''',
            pearl="Mucor ต้องผ่าตัดเนื้อตายเสมอ", topic="Mucor surgery",
            ref=[f"{D} หน้า 168"], nl=["2.3.1-3(7)"]),
    ])

LECTURE = lecture("04", "Toxin-mediated & zoonotic infections, mucormycosis",
    "Anthrax · diphtheria · pertussis · mucormycosis",
    objectives=[
        "แยก eschar ของ anthrax กับ scrub typhus และให้ยา cutaneous anthrax ได้",
        "วินิจฉัย diphtheria จาก pseudomembrane และรักษาด้วย airway + DAT + ATB",
        "จำระยะของ pertussis ระยะแพร่เชื้อ และยาที่ใช้ได้",
        "วินิจฉัย mucormycosis จาก risk/ลักษณะ hyphae และรักษาครบ 3 ด้าน",
    ],
    sections=[S1, S2, S3, S4])
