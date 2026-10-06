from lib import lecture, sec, mcq, fig

D = "สไลด์ Update ข้อสอบ 2025"
SRC = "NL2 2025 (update)"

def R(*p):
    return [f"{D} หน้า " + ", ".join(str(x) for x in p)]

# ---------------------------------------------------------------- 02-01 TB
S1 = sec("exam25-02-01", "Tuberculosis & its sequelae",
    "Cavity upper lobe → sputum AFB · optic neuritis = ethambutol · post-TB → bronchiectasis · Pott disease", minutes=6,
    source=f"{D} หน้า 78–88, 97–98", nl=["2.3.1(20)", "B6.2.2(4)", "2.3.13-3(9)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

- **Pulmonary TB**: ไอ ≥ 2 สัปดาห์ น้ำหนักลด ไข้ต่ำ ๆ เหงื่อออกกลางคืน ไอเป็นเลือด · CXR: **cavity**, consolidation/reticulonodular ที่ **upper lobe**, hilar node, pleural effusion
- **ขั้นตอนถัดไปเมื่อสงสัย = sputum AFB smear** (ร่วมกับ molecular test เช่น Xpert MTB/RIF ตามแนวทางประเทศไทย) — ไม่ต้อง CT ไม่ต้องลองยาปฏิชีวนะ

**ผลข้างเคียงของยา TB (ตารางสไลด์ + เสริม)**

| ยา | ผลข้างเคียงที่ออกสอบ |
|---|---|
| **H** (isoniazid) | peripheral neuropathy (ให้ **pyridoxine** 50–75 mg/วัน), hepatitis, ง่วง |
| **R** (rifampicin) | ปัสสาวะ/น้ำตาสีส้มแดง, flu-like, hepatitis, drug interaction (CYP inducer) |
| **Z** (pyrazinamide) | ปวดข้อ/**hyperuricemia** (ให้ NSAID/paracetamol), hepatitis มากสุด |
| **E** (ethambutol) | **optic neuritis** (ตามัว ตาบอดสีแดง–เขียว) |
| S (streptomycin) | ototoxicity, nephrotoxicity |

**ผลตามหลังและ extrapulmonary TB**
- **Post-TB bronchiectasis**: ไอมีเสมหะเรื้อรัง ติดเชื้อซ้ำ clubbing · CXR/HRCT: **tram-track, cystic lesion, signet ring** · AFB ลบ
- **TB spondylitis (Pott disease)**: ปวดหลังเรื้อรัง + constitutional symptoms · **ทำลายตัวกระดูกสันหลัง + disc space แคบ + paraspinal (cold) abscess** · kyphosis/paraplegia
''',
    pearls=[
        "สงสัย pulmonary TB → sputum AFB (± Xpert) เป็นขั้นแรก",
        "E = Eye (optic neuritis) · H = neuropathy → pyridoxine · Z = ข้อ/uric acid · R = สีส้ม",
        "เคยเป็น TB + เสมหะเรื้อรัง + cystic lesion + clubbing = bronchiectasis",
        "ปวดหลัง + disc space แคบ + paraspinal abscess = Pott disease",
    ],
    items=[
        mcq("EXAM25-02-01-1",
            "A 40-year-old man has low-grade fever, cough and occasional blood-streaked sputum for 1 month. Temperature 39 °C. There are coarse crepitations over the left upper lobe. Chest X-ray shows fibronodular infiltration with a cavity in the left upper lobe. What is the next step in management?",
            "Sputum for acid-fast bacilli",
            ["CT chest", "Amoxicillin-clavulanate", "Azithromycin", "Sputum bacterial culture"],
            kind="old", src=SRC,
            explain='''ไอ 1 เดือน + ไอเป็นเลือด + ไข้ + **fibronodular infiltration และ cavity ที่ upper lobe** = pulmonary TB จนกว่าจะพิสูจน์ได้ว่าไม่ใช่ → ตรวจ **sputum AFB** (ร่วมกับ molecular test ตามแนวทาง) เป็นขั้นแรก
- CT chest ไม่จำเป็น เพราะ CXR บอกแล้วและไม่ได้ยืนยันเชื้อ
- Amoxicillin-clavulanate และ azithromycin เป็นการรักษา CAP ซึ่งไม่เข้ากับอาการ 1 เดือนที่มี cavity และ fluoroquinolone/macrolide บางตัวอาจบดบังการวินิจฉัย TB
- Sputum bacterial culture ธรรมดาไม่ขึ้นเชื้อ M. tuberculosis''',
            pearl="Cavity upper lobe + ไอเรื้อรัง → sputum AFB", topic="Pulmonary TB",
            ref=R(78, 79, 81, 82), nl=["2.3.1(20)"]),
        mcq("EXAM25-02-01-2",
            "A 30-year-old man on first-line antituberculosis therapy develops blurred vision and impaired red–green color discrimination consistent with optic neuritis. Which drug is most likely responsible?",
            "Ethambutol",
            ["Isoniazid", "Rifampicin", "Pyrazinamide", "Streptomycin"],
            kind="old", src=SRC,
            explain='''**Ethambutol** ทำให้ **optic (retrobulbar) neuritis** ขึ้นกับขนาดยา อาการตามัวและแยกสีแดง–เขียวไม่ได้ ต้องหยุดยาทันที
- Isoniazid ทำให้ peripheral neuropathy และ hepatitis (ป้องกันด้วย pyridoxine)
- Rifampicin ทำให้สารคัดหลั่งสีส้มแดง hepatitis และ drug interaction
- Pyrazinamide ทำให้ปวดข้อ hyperuricemia และ hepatitis
- Streptomycin ทำให้ ototoxicity และ nephrotoxicity''',
            pearl="E = Eye: ethambutol → optic neuritis", topic="Anti-TB side effects",
            ref=R(83, 85, 86), nl=["2.3.1(20)"]),
        mcq("EXAM25-02-01-3",
            "A 50-year-old man treated for pulmonary tuberculosis 5 years ago presents with 5 days of productive cough and fever. Temperature 38.5 °C. There are fine crepitations at both lung bases and finger clubbing. Sputum AFB smear is negative. Chest X-ray shows diffuse cystic lesions in both lower lobes. What is the most likely diagnosis?",
            "Infected bronchiectasis",
            ["Recurrent tuberculosis", "Aspergilloma", "Lung abscess", "Necrotizing pneumonia"],
            kind="old", src=SRC,
            explain='''ประวัติ TB (ทำลายหลอดลม) + ไอมีเสมหะ + **clubbing** (บอกว่าเป็นเรื้อรัง) + **cystic lesions** ทั้งสองข้าง + AFB ลบ = **bronchiectasis ที่ติดเชื้อซ้ำ**
- Recurrent TB มักเป็นที่ upper lobe ไอเรื้อรังหลายสัปดาห์ และ AFB มักบวก
- Aspergilloma เป็นก้อนในโพรงเดิมของ TB (air-crescent sign) มักมาด้วยไอเป็นเลือด
- Lung abscess เป็นโพรงเดี่ยวมี air-fluid level ไม่ใช่ cystic lesion กระจายสองข้าง
- Necrotizing pneumonia เป็นเฉียบพลัน ป่วยหนัก ไม่อธิบาย clubbing''',
            pearl="Post-TB + clubbing + cystic lesion = bronchiectasis", topic="Bronchiectasis",
            ref=R(87, 88), nl=["B6.2.2(4)", "2.3.10(5)"]),
        mcq("EXAM25-02-01-4",
            "A 45-year-old man presents with 3 months of back pain, night sweats and weight loss. He immigrated from a TB-endemic area. Spinal radiograph shows vertebral body destruction, loss of disc space and a paraspinal abscess. What is the most likely diagnosis?",
            "Tuberculous spondylitis",
            ["Metastatic cancer", "Pyogenic vertebral osteomyelitis", "Ankylosing spondylitis", "Osteoporotic vertebral fracture"],
            kind="old", src=SRC,
            explain='''ปวดหลังเรื้อรัง 3 เดือน + constitutional symptoms + มาจากพื้นที่ระบาด + **ทำลาย vertebral body + disc space แคบ + paraspinal (cold) abscess** = **TB spondylitis (Pott disease)**
- Metastasis มักทำลาย pedicle/vertebral body แต่ **disc space ปกติ** และไม่มี paraspinal abscess
- Pyogenic osteomyelitis เป็นเฉียบพลันกว่า ไข้สูง ไม่ใช่ 3 เดือน
- Ankylosing spondylitis เป็นชายอายุน้อย ปวดหลังแบบ inflammatory มี syndesmophyte (bamboo spine) ไม่มีการทำลายกระดูก
- Osteoporotic fracture เกิดเฉียบพลันในผู้สูงอายุ ไม่มีไข้ น้ำหนักลด หรือ abscess''',
            pearl="Disc space แคบ + paraspinal abscess + constitutional = Pott disease", topic="TB spondylitis",
            ref=R(97, 98), nl=["2.3.13-3(9)", "2.3.1(20)"]),
    ])

# ---------------------------------------------------------------- 02-02 Pleural effusion
F_PL = fig("exam25-02-02-f1", "แปลผล pleural fluid ที่ข้อสอบชอบถาม", '''<svg viewBox="0 0 720 330">
 <defs><marker id="exam25-02-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="10" width="260" height="44" rx="10" class="acsoft"/>
 <text x="360" y="30" text-anchor="middle" class="tb">Pleural fluid: exudate</text>
 <text x="360" y="47" text-anchor="middle" class="t3">(Light's criteria บวกข้อใดข้อหนึ่ง)</text>
 <path d="M300 54L170 92" class="ln" marker-end="url(#exam25-02-02-a)"/>
 <path d="M420 54L550 92" class="ln" marker-end="url(#exam25-02-02-a)"/>
 <rect x="20" y="94" width="300" height="44" rx="10" class="c1"/>
 <text x="170" y="121" text-anchor="middle" class="tw">Lymphocyte เด่น</text>
 <rect x="400" y="94" width="300" height="44" rx="10" class="c2"/>
 <text x="550" y="121" text-anchor="middle" class="tw">Neutrophil เด่น (parapneumonic)</text>
 <rect x="20" y="148" width="300" height="168" rx="10" class="c1soft"/>
 <text x="36" y="174" class="tb">ADA &gt; 40 U/L</text>
 <text x="36" y="194" class="t2">→ TB pleuritis → anti-TB</text>
 <text x="36" y="226" class="tb">Cytology ผิดปกติ</text>
 <text x="36" y="246" class="t2">→ malignant effusion</text>
 <text x="36" y="280" class="t3">ADA สูงเล็กน้อยพบใน empyema ได้</text>
 <text x="36" y="298" class="t3">ต้องดู cell type ประกอบเสมอ</text>
 <path d="M500 138L470 172" class="ln" marker-end="url(#exam25-02-02-a)"/>
 <path d="M600 138L630 172" class="ln" marker-end="url(#exam25-02-02-a)"/>
 <rect x="350" y="174" width="180" height="142" rx="10" class="oksoft"/>
 <text x="440" y="198" text-anchor="middle" class="tb">Simple</text>
 <text x="440" y="222" text-anchor="middle" class="t2">pH &gt; 7.2</text>
 <text x="440" y="242" text-anchor="middle" class="t2">glucose &gt; 60</text>
 <text x="440" y="262" text-anchor="middle" class="t2">G/S, C/S ลบ</text>
 <text x="440" y="296" text-anchor="middle" class="ta">ATB อย่างเดียว</text>
 <rect x="540" y="174" width="170" height="142" rx="10" class="badsoft"/>
 <text x="625" y="198" text-anchor="middle" class="tb">Complicated</text>
 <text x="625" y="216" text-anchor="middle" class="tb">/ Empyema</text>
 <text x="625" y="240" text-anchor="middle" class="t2">pH &lt; 7.2, glu &lt; 60</text>
 <text x="625" y="260" text-anchor="middle" class="t2">loculated, หนอง,</text>
 <text x="625" y="278" text-anchor="middle" class="t2">G/S หรือ C/S บวก</text>
 <text x="625" y="300" text-anchor="middle" class="ta">ATB + ICD</text>
</svg>''', "ดู cell type ก่อน แล้วใช้ ADA/cytology ในฝั่ง lymphocyte และใช้ pH–glucose–เชื้อในฝั่ง neutrophil ตัดสินว่าต้องใส่สายระบายหรือไม่")

S2 = sec("exam25-02-02", "Pleural effusion",
    "Lymphocytic exudate + ADA >40 = TB · parapneumonic pH >7.2, glucose >60 = simple → ATB อย่างเดียว", minutes=4,
    source=f"{D} หน้า 89–96", nl=["2.3.10(7)", "2.3.10-3(2)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

[[fig:exam25-02-02-f1]]

**ค่าพิเศษใน pleural fluid (สไลด์)**

| ค่า | บอกอะไร |
|---|---|
| **pH < 7.2** | complicated parapneumonic/empyema, malignant |
| **ADA > 40 U/L** | **TB pleurisy** |
| Cytology ผิดปกติ | malignant effusion |
| Amylase > 200 | pancreatitis, esophageal rupture |
| RF, ANA บวก | autoimmune |
| **TG > 110 mg/dL** | chylothorax |

**Parapneumonic effusion (สไลด์)**

| ระยะ | ภาพ | pH | Glucose | C/S | รักษา |
|---|---|---|---|---|---|
| Simple | free-flow, < ½ hemithorax | **> 7.2** | **> 60** | ลบ | **ATB, observe** |
| Complicated | > ½ hemithorax, septate/loculated | < 7.2 | < 60 | ลบ | ATB + drainage |
| Empyema | frank pus หรือ G/S/C/S บวก | — | — | บวก | ATB + drainage |
''',
    figs=[F_PL],
    pearls=[
        "Lymphocytic exudate + ADA > 40 = TB pleuritis",
        "Parapneumonic: pH > 7.2 และ glucose > 60 = simple → ATB อย่างเดียว",
        "pH < 7.2, glucose < 60, loculated หรือหนอง → ใส่ ICD",
        "TG > 110 = chylothorax · amylase สูง = pancreatitis/esophageal rupture",
    ],
    items=[
        mcq("EXAM25-02-02-1",
            "A 45-year-old woman presents with a unilateral pleural effusion. She reports night sweats and weight loss. Pleural fluid is an exudate with lymphocyte predominance and adenosine deaminase (ADA) of 85 U/L. What is the most likely diagnosis?",
            "Tuberculous pleuritis",
            ["Malignant pleural effusion", "Parapneumonic effusion", "Heart failure", "Pulmonary embolism"],
            kind="old", src=SRC,
            explain='''**Exudate + lymphocyte เด่น + ADA > 40 U/L** (85) ร่วมกับเหงื่อออกกลางคืนและน้ำหนักลด = **TB pleuritis**
- Malignant effusion เป็น lymphocytic exudate ได้และน้ำหนักลดได้ แต่ ADA มักต่ำ ต้องอาศัย cytology
- Parapneumonic effusion เป็น neutrophil เด่น มีไข้เฉียบพลันจาก pneumonia
- Heart failure ให้ transudate และมักเป็นสองข้าง
- PE ให้ effusion เล็ก ๆ อาจเป็น exudate ได้ แต่ ADA ไม่สูงและมาด้วยหอบเฉียบพลัน''',
            pearl="Lymphocytic exudate + ADA > 40 = TB", topic="TB pleuritis",
            ref=R(89, 92, 93), nl=["2.3.10(7)", "2.3.1(20)"]),
        mcq("EXAM25-02-02-2",
            "A 40-year-old man presents with fever, cough and left-sided pleuritic chest pain. Temperature 38 °C, RR 24/min. Chest X-ray shows a moderate free-flowing left pleural effusion. Pleural fluid: pH 7.4, WBC 2,500/mm³ (90% neutrophils, 10% lymphocytes), ADA 45 U/L, glucose 60% of the serum level, Gram stain negative. What is the most appropriate management?",
            "Empirical antibiotics",
            ["Insertion of an intercostal chest drain", "Anti-tuberculosis therapy", "Pleural biopsy", "CT chest"],
            kind="old", src=SRC,
            explain='''Pneumonia + effusion ที่ **neutrophil เด่น** = parapneumonic · **pH 7.4 (> 7.2)** และ glucose ไม่ต่ำ (60% ของ serum) + G/S ลบ = **simple parapneumonic effusion** → **empirical antibiotics** แล้วติดตาม
- ICD ใช้เมื่อเป็น complicated (pH < 7.2, glucose < 60, loculated) หรือ empyema
- Anti-TB ไม่ใช่ เพราะ TB จะเป็น lymphocyte เด่น — ADA 45 สูงเล็กน้อยพบได้ใน parapneumonic/empyema (กับดักของข้อนี้)
- Pleural biopsy ใช้เมื่อสงสัย TB/malignancy ที่การตรวจน้ำไม่ได้คำตอบ
- CT chest ใช้เมื่อสงสัย loculation หรือไม่ตอบสนองต่อยา''',
            pearl="Simple parapneumonic (pH > 7.2) → ATB อย่างเดียว", topic="Parapneumonic effusion",
            ref=R(94, 95, 96), nl=["2.3.10(7)", "2.3.10-3(2)"]),
    ])

LECTURE = lecture("02", "Respiratory", "TB · anti-TB side effects · bronchiectasis · pleural effusion",
    objectives=[
        "เลือกการตรวจแรกเมื่อสงสัย pulmonary TB",
        "จำผลข้างเคียงหลักของยา TB แต่ละตัว",
        "แปลผล pleural fluid: ADA, pH, glucose แล้วตัดสินใจใส่ ICD",
    ],
    sections=[S1, S2])
