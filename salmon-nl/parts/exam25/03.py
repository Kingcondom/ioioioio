from lib import lecture, sec, mcq, fig

D = "สไลด์ Update ข้อสอบ 2025"
SRC = "NL2 2025 (update)"

def R(*p):
    return [f"{D} หน้า " + ", ".join(str(x) for x in p)]

# ---------------------------------------------------------------- 03-01 Dyspepsia & esophagitis
F_DYS = fig("exam25-03-01-f1", "Uninvestigated dyspepsia (ตามสไลด์)", '''<svg viewBox="0 0 720 300">
 <defs><marker id="exam25-03-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="10" width="260" height="40" rx="10" class="acsoft"/>
 <text x="360" y="35" text-anchor="middle" class="tb">Uninvestigated dyspepsia</text>
 <path d="M360 50V70" class="ln" marker-end="url(#exam25-03-01-a)"/>
 <rect x="180" y="72" width="360" height="40" rx="10" class="box"/>
 <text x="360" y="97" text-anchor="middle" class="tb">อายุเริ่มเป็น ≥ 50 ปี หรือ alarm feature?</text>
 <path d="M260 112L150 150" class="ln" marker-end="url(#exam25-03-01-a)"/>
 <path d="M460 112L570 150" class="ln" marker-end="url(#exam25-03-01-a)"/>
 <text x="180" y="125" text-anchor="end" class="ta">ไม่</text>
 <text x="540" y="125" class="ta">ใช่</text>
 <rect x="20" y="152" width="280" height="66" rx="10" class="oksoft"/>
 <text x="160" y="176" text-anchor="middle" class="tb">PPI ± prokinetic 4–8 สัปดาห์</text>
 <text x="160" y="198" text-anchor="middle" class="t2">หรือ test-and-treat H. pylori</text>
 <rect x="420" y="152" width="280" height="66" rx="10" class="badsoft"/>
 <text x="560" y="180" text-anchor="middle" class="tb">EGD + H. pylori testing</text>
 <text x="560" y="202" text-anchor="middle" class="t3">ปกติ → functional dyspepsia</text>
 <path d="M300 200C360 230 380 230 418 205" class="lnf" marker-end="url(#exam25-03-01-a)"/>
 <text x="360" y="248" text-anchor="middle" class="t3">ไม่ตอบสนอง → EGD</text>
 <rect x="20" y="262" width="680" height="30" rx="8" class="sunk"/>
 <text x="360" y="282" text-anchor="middle" class="t2">Alarm: GI bleed · กลืนลำบาก/กลืนเจ็บ · อาเจียนมาก · น้ำหนักลด · ญาติสายตรงเป็นมะเร็ง · คลำก้อน · IDA</text>
</svg>''', "คัดคนที่ต้องส่องกล้องเลยด้วยอายุและ alarm feature ที่เหลือให้ PPI ก่อน และส่งส่องกล้องถ้ารักษาแล้วไม่ดีขึ้น")

S1 = sec("exam25-03-01", "Dyspepsia & drug-induced esophagitis",
    "Alarm feature (น้ำหนักลด, กลืนเจ็บ) หรือ PPI ไม่ได้ผล → EGD · ยาที่ทำให้ pill esophagitis", minutes=4,
    source=f"{D} หน้า 165–170", nl=["2.1.11", "2.3.11(5)", "2.3.11(6)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

[[fig:exam25-03-01-f1]]

**ข้อบ่งชี้ส่อง EGD ใน dyspepsia (สไลด์)**: อายุเริ่มเป็น **≥ 50 ปี** · **ยาไม่ได้ผล** · alarm features: GI bleeding, **odynophagia/dysphagia**, อาเจียน > 10 ครั้ง/วัน, **น้ำหนักลด**, ญาติสายตรงเป็นมะเร็งกระเพาะ/หลอดอาหาร, คลำก้อนที่ลิ้นปี่, IDA

**Drug-induced (pill) esophagitis**
- ยาที่พบบ่อย: **doxycycline, tetracycline, clindamycin** · NSAID, aspirin · **bisphosphonate** · iron, KCl · **isotretinoin**
- อาการ: **เจ็บเวลากลืน (odynophagia)** หลังอก แสบร้อน กลืนลำบาก เกิดเฉียบพลันหลังกินยา
- วินิจฉัย: **EGD** (มีข้อบ่งชี้เพราะ odynophagia/dysphagia) เห็นแผลตื้นที่ระดับ aortic arch (เสริม)
- รักษา: หยุดยา, PPI/sucralfate · ป้องกันด้วยดื่มน้ำตามเต็มแก้ว นั่ง/ยืน 30 นาทีหลังกินยา (เสริม)
''',
    figs=[F_DYS],
    pearls=[
        "Dyspepsia + น้ำหนักลด หรือ PPI ไม่ได้ผล → EGD",
        "กลืนเจ็บ (odynophagia) = alarm feature → EGD",
        "Pill esophagitis: doxycycline, bisphosphonate, NSAID, iron, isotretinoin",
    ],
    items=[
        mcq("EXAM25-03-01-1",
            "A 20-year-old woman taking isotretinoin for acne vulgaris reports 3 days of retrosternal pain on swallowing, heartburn and dysphagia. Vital signs are normal. There is no oral thrush, ulcer or pharyngeal inflammation. What is the most appropriate investigation?",
            "Esophagogastroduodenoscopy",
            ["24-hour esophageal pH monitoring", "Esophageal manometry", "12-lead ECG", "Chest X-ray (PA and lateral)"],
            kind="old", src=SRC,
            explain='''กินยาที่ทำให้เกิด **pill esophagitis** (isotretinoin) แล้วมี **odynophagia + dysphagia** เฉียบพลัน = drug-induced esophagitis · odynophagia/dysphagia เป็น alarm feature → **EGD** เพื่อดูแผลและแยกสาเหตุอื่น
- 24-hour pH monitoring ใช้ใน GERD ที่ไม่ตอบสนองต่อ PPI หรือก่อนผ่าตัด ไม่ใช่อาการเฉียบพลัน
- Manometry ใช้ใน motility disorder (achalasia) ที่กลืนลำบากเรื้อรังทั้งของแข็งและของเหลว
- ECG ใช้เมื่อสงสัยเจ็บอกจากหัวใจ แต่อาการนี้สัมพันธ์กับการกลืนในหญิงอายุ 20
- CXR ไม่เห็นแผลในหลอดอาหาร''',
            pearl="Odynophagia หลังกินยา → pill esophagitis → EGD", topic="Pill esophagitis",
            ref=R(165, 166), nl=["2.3.11(5)"]),
        mcq("EXAM25-03-01-2",
            "A 24-year-old woman reports 4 weeks of postprandial fullness and unintentional weight loss despite intermittent omeprazole and simethicone. Examination shows mild conjunctival pallor, LUQ tenderness and mild abdominal distension. She has no fever or vomiting. What is the most appropriate management?",
            "Esophagogastroduodenoscopy",
            ["Increase the omeprazole dose", "Empirical H. pylori eradication", "Sucralfate", "Abdominal ultrasound"],
            kind="old", src=SRC,
            explain='''Dyspepsia ที่ **ใช้ยาแล้วไม่ดีขึ้น** + **น้ำหนักลด** + **ซีด** (สงสัย IDA) = มี alarm features → **EGD** แม้อายุ < 50 (สไลด์: dyspepsia + weight loss → EGD)
- เพิ่ม omeprazole หรือเปลี่ยนเป็น sucralfate คือการรักษาต่อโดยยังไม่ได้ตัดโรคร้าย
- Empirical H. pylori eradication (test-and-treat) ใช้ในรายที่ไม่มี alarm feature
- U/S ช่องท้องไม่ได้ดูเยื่อบุกระเพาะ''',
            pearl="Dyspepsia + alarm feature (น้ำหนักลด, ซีด) → EGD", topic="Dyspepsia",
            ref=R(167, 168, 169, 170), nl=["2.3.11(6)", "2.1.11"]),
    ])

# ---------------------------------------------------------------- 03-02 UGIB
S2 = sec("exam25-03-02", "Upper GI bleeding",
    "อาเจียนก่อนแล้วเป็นเลือด = Mallory-Weiss · cirrhosis + UGIB → octreotide + IV PPI (+ ceftriaxone) · stable → EGD", minutes=5,
    source=f"{D} หน้า 171–176", nl=["2.1.16", "2.3.11-3(6)", "B8.4(2)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**สาเหตุ UGIB ที่แยกจากประวัติ**

| ประวัติ | คิดถึง |
|---|---|
| **อาเจียน/ขย้อนหลายครั้งก่อน** แล้วจึงมีเลือด (หลังดื่มหนัก) | **Mallory-Weiss tear** |
| ตับแข็ง (stigmata of CLD) | Esophageal/gastric varices |
| NSAID, ปวดท้องสัมพันธ์มื้ออาหาร | Peptic ulcer |
| ดื่มเหล้า ปวดแสบลิ้นปี่ ไม่มี retching นำ | Gastritis |

**ขั้นตอน (สไลด์ + เสริม)**
1. Resuscitation (IV fluid, PRC เป้า Hb 7–8)
2. ยา: **ตับแข็ง → IV vasoactive (octreotide/terlipressin) + IV PPI** (ยังไม่รู้ว่าเป็น varices หรือ ulcer) + **ceftriaxone** prophylaxis (เสริม)
3. **EGD ภายใน 12–24 ชม.** หลัง stabilize (ภายใน 12 ชม. ถ้าสงสัย variceal)
- Balloon tamponade = bridge เมื่อเลือดออกไม่หยุด · propranolol = secondary prophylaxis หลังหยุดเลือด **ห้ามให้ตอนเลือดออก**
''',
    pearls=[
        "ขย้อนหลายครั้งก่อน แล้วจึงอาเจียนเป็นเลือด = Mallory-Weiss",
        "Cirrhosis + UGIB → octreotide + IV PPI + ceftriaxone ก่อน EGD",
        "UGIB stable → EGD (ภายใน 24 ชม.)",
        "Propranolol ไม่ใช้ในช่วงเลือดออกเฉียบพลัน",
    ],
    items=[
        mcq("EXAM25-03-02-1",
            "A 28-year-old man reports three episodes of hematemesis after heavy alcohol consumption and recurrent vomiting. He has no stigmata of chronic liver disease. CBC is unremarkable. What is the most likely cause of the hematemesis?",
            "Mallory-Weiss tear",
            ["Esophageal varices", "Alcoholic gastritis", "Hemorrhagic peptic ulcer", "Erosive duodenitis"],
            kind="old", src=SRC,
            explain='''**อาเจียน/ขย้อนซ้ำ ๆ ก่อน** แล้วจึงอาเจียนเป็นเลือด หลังดื่มหนัก = **Mallory-Weiss tear** (ฉีกขาดตามยาวที่ gastroesophageal junction) ส่วนใหญ่หยุดเอง
- Esophageal varices ต้องมี portal hypertension/cirrhosis ซึ่งรายนี้ไม่มี stigmata
- Alcoholic gastritis ทำให้เลือดออกได้ แต่ไม่ได้อธิบาย sequence ที่อาเจียนก่อนแล้วจึงมีเลือด
- Peptic ulcer และ erosive duodenitis มักมีประวัติปวดท้อง/NSAID และไม่สัมพันธ์กับการขย้อน''',
            pearl="Retching ก่อนเลือด = Mallory-Weiss", topic="Mallory-Weiss tear",
            ref=R(171, 172), nl=["2.3.11-3(6)", "2.1.16"]),
        mcq("EXAM25-03-02-2",
            "A 60-year-old man with cirrhosis presents with hematemesis and melena and is resuscitated with intravenous fluids. BP is now 110/70 mmHg and pulse 90/min. Endoscopy is planned within 1 hour. What is the most appropriate pharmacologic management now?",
            "Intravenous octreotide plus intravenous proton pump inhibitor",
            ["Urgent esophagogastroduodenoscopy", "Intravenous vasopressin", "Balloon tamponade", "Oral propranolol"],
            kind="old", src=SRC,
            explain='''ผู้ป่วยตับแข็งที่มี UGIB อาจเป็นได้ทั้ง varices และ ulcer → ให้ **vasoactive drug (octreotide)** ลด portal pressure ร่วมกับ **IV PPI** ไปก่อนส่องกล้อง (ร่วมกับ ceftriaxone prophylaxis — เสริม)
- Urgent EGD นัดไว้แล้วภายใน 1 ชม. และไม่ใช่ยา — คำถามถามว่าให้ยาอะไรระหว่างรอ
- Vasopressin ลด portal pressure ได้ แต่ผลข้างเคียงสูง (ischemia หัวใจ/ลำไส้) จึงไม่ใช่ตัวเลือกแรก
- Balloon tamponade เป็น bridge เมื่อเลือดออกมากหยุดไม่ได้ ไม่ใช่ยาและไม่ใช้ในคน stable
- Propranolol ใช้ป้องกันเลือดออกซ้ำหลังหยุดเลือดแล้ว ห้ามให้ตอนเลือดออก (BP ลด บดบัง tachycardia)''',
            pearl="Cirrhosis + UGIB → octreotide + IV PPI (+ ceftriaxone)", topic="Variceal bleeding",
            ref=R(173, 174), nl=["B8.4(2)", "2.3.11-3(6)"]),
        mcq("EXAM25-03-02-3",
            "A 50-year-old man with a history of alcohol use presents with hematemesis and melena. He is hemodynamically stable after initial assessment. What is the most appropriate next step in management?",
            "Esophagogastroduodenoscopy",
            ["CT abdomen", "Proton pump inhibitor and discharge", "Exploratory laparotomy", "Reassurance and discharge"],
            kind="old", src=SRC,
            explain='''UGIB (hematemesis + melena) ที่ hemodynamics stable → **EGD** เพื่อวินิจฉัยและห้ามเลือด (ภายใน 24 ชม.)
- CT abdomen ไม่ใช่การตรวจหลักของ UGIB
- ให้ PPI อย่างเดียวแล้วกลับบ้านไม่ได้ เพราะคนดื่มสุราที่มี hematemesis + melena มีความเสี่ยงสูง (varices, ulcer)
- Exploratory laparotomy ใช้เมื่อห้ามเลือดทางกล้องไม่สำเร็จ
- Reassurance ไม่เหมาะกับ UGIB ที่มีทั้ง hematemesis และ melena''',
            pearl="UGIB stable → EGD", topic="UGIB",
            ref=R(175, 176), nl=["2.3.11-3(6)"]),
    ])

# ---------------------------------------------------------------- 03-03 Liver & pancreas
S3 = sec("exam25-03-03", "Liver & pancreas",
    "Pancreatitis → U/S หา gallstone · ดื่มเหล้า + paracetamol 4 g/วัน = toxicity · amebic abscess → metronidazole · ALP เด่น = cholestasis", minutes=6,
    source=f"{D} หน้า 163–164, 177–183", nl=["2.3.11(1)", "2.2.46", "2.3.11(8)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Acute pancreatitis — หาสาเหตุ**: **gallstone (40–70%)** > alcohol (25–35%) > hypertriglyceridemia · แม้คนดื่มเหล้าก็ต้อง **U/S ช่องท้องทุกราย** หา gallstone (ถ้าเป็นจะได้ทำ cholecystectomy)

**Paracetamol overdose (สไลด์)**

| แบบ | ขนาดที่เป็นพิษ |
|---|---|
| Acute | > 150 mg/kg (เด็ก) · **> 6–7.5 g** (ผู้ใหญ่) · > 30 g = massive |
| Chronic/repeated ใน 24–48 ชม. | > 150 mg/kg/วัน หรือ **> 6 g/วัน** |
| Chronic > 48 ชม. | > 100 mg/kg/วัน หรือ **> 4 g/วัน** |

- **ขนาดต่ำกว่านี้ก็เป็นพิษได้** ถ้า: **ดื่มสุราเรื้อรัง**, malnutrition, ใช้ยากระตุ้น CYP2E1 (phenobarbital, phenytoin, isoniazid, zidovudine) — glutathione ต่ำ + NAPQI มาก
- รักษา: **N-acetylcysteine** (เสริม)

**Amebic liver abscess**: ไข้ ปวด RUQ ตับโตกดเจ็บ ก้อนเดี่ยวกลีบขวา serology บวก → **metronidazole 7–10 วัน** แล้วตามด้วย **paromomycin** (luminal agent) · drainage เมื่อ **> 5 cm, กลีบซ้าย หรือไม่ดีขึ้นใน 5–7 วัน**

**รูปแบบ LFT (เสริม)**: AST/ALT สูงเด่น = hepatocellular · **ALP (± GGT) สูงเด่น, AST/ALT สูงเล็กน้อย = cholestasis** · AST:ALT > 2 = alcoholic
''',
    pearls=[
        "Pancreatitis ทุกราย (แม้ดื่มเหล้า) → U/S หา gallstone",
        "ดื่มสุราเรื้อรัง + paracetamol 4 g/วัน = เป็นพิษได้ → NAC",
        "Amebic abscess → metronidazole แล้วต่อ paromomycin · drain ถ้า > 5 cm/กลีบซ้าย/ไม่ดีขึ้น",
        "ALP เด่น + AST/ALT สูงเล็กน้อย = cholestatic pattern",
    ],
    items=[
        mcq("EXAM25-03-03-1",
            "A 55-year-old man with chronic alcohol use presents with severe epigastric pain radiating to the back, nausea and vomiting for 24 hours. There is epigastric tenderness and guarding. Serum amylase 1,200 U/L, lipase 900 U/L. CT abdomen shows pancreatic edema. What is the most appropriate investigation to identify the etiology?",
            "Abdominal ultrasound",
            ["Serum triglycerides", "MRCP", "ERCP", "Stool examination for parasites"],
            kind="old", src=SRC,
            explain='''สาเหตุที่พบบ่อยที่สุดของ acute pancreatitis คือ **gallstone** แม้ผู้ป่วยดื่มสุรา ก็ต้องทำ **U/S ช่องท้อง** หานิ่วในถุงน้ำดีทุกราย (เพราะการรักษาต่างกัน)
- Serum TG ควรตรวจด้วย แต่เป็นสาเหตุที่พบน้อยกว่าและไม่ได้ตอบคำถามว่าตรวจอะไรเป็นอันดับแรก
- MRCP ใช้เมื่อ U/S ไม่ชัดแต่ยังสงสัย CBD stone
- ERCP เป็นหัตถการรักษาเมื่อมี cholangitis/CBD obstruction ไม่ใช่การตรวจหาสาเหตุ
- Stool exam (Ascaris) เป็นสาเหตุที่พบน้อยมาก''',
            pearl="Pancreatitis → U/S หา gallstone ทุกราย", topic="Acute pancreatitis",
            ref=R(163, 164), nl=["2.3.11(1)"]),
        mcq("EXAM25-03-03-2",
            "A 30-year-old man presents with nausea and vomiting. He has drunk 1–2 bottles of whisky daily for 10 years. One week ago he took paracetamol 2 tablets (500 mg) four times a day for headache. Temperature 37 °C. There is mild pallor, jaundice, spider angiomata, palmar erythema, hepatomegaly and mild RUQ tenderness without guarding or ascites. What is the diagnosis?",
            "Acetaminophen toxicity",
            ["Alcoholic intoxication", "Acute viral hepatitis B", "Ascending cholangitis", "Acute pancreatitis"],
            kind="old", src=SRC,
            explain='''Paracetamol 4 g/วัน (500 mg × 2 × 4) เป็นขนาด "ปกติสูงสุด" แต่ในคน **ดื่มสุราเรื้อรัง** (CYP2E1 ถูกกระตุ้น + glutathione ต่ำ) จะเกิด NAPQI มากจนตับถูกทำลาย = **acetaminophen (paracetamol) hepatotoxicity** → ให้ NAC
- Alcoholic intoxication ทำให้ซึม เมา ไม่ได้อธิบายดีซ่านเฉียบพลัน
- Acute hepatitis B เป็นไปได้ แต่โจทย์ให้ประวัติยาที่เข้ากับช่วงเวลาชัดกว่า
- Cholangitis ต้องมี Charcot triad (ไข้ ปวด RUQ ดีซ่าน) — รายนี้ไม่มีไข้
- Pancreatitis ปวดลิ้นปี่ทะลุหลัง ไม่ทำให้ดีซ่านและตับโต''',
            pearl="ดื่มสุราเรื้อรัง: paracetamol 4 g/วัน ก็เป็นพิษได้", topic="Paracetamol toxicity",
            ref=R(177, 178, 179), nl=["2.2.46", "2.3.18(7)"]),
        mcq("EXAM25-03-03-3",
            "A 40-year-old man presents with fever, right upper quadrant pain and tender hepatomegaly. Ultrasound shows a single 4-cm hypoechoic lesion in the right hepatic lobe. Amebic serology is positive. What is the most appropriate initial treatment?",
            "Oral metronidazole",
            ["Ultrasound-guided percutaneous drainage", "Intravenous ceftriaxone", "Oral ciprofloxacin", "Intravenous amphotericin B"],
            kind="old", src=SRC,
            explain='''Amebic liver abscess (ก้อนเดี่ยวกลีบขวา + serology บวก) → **metronidazole 7–10 วัน** แล้วตามด้วย luminal agent (paromomycin) เพื่อกำจัด cyst ในลำไส้
- Drainage ใช้เมื่อก้อน > 5 cm, อยู่กลีบซ้าย (เสี่ยงแตกเข้าเยื่อหุ้มหัวใจ) หรือไม่ดีขึ้นใน 5–7 วัน — รายนี้ 4 cm กลีบขวา (สไลด์ไม่ได้ให้ขนาด จึงใส่ 4 cm เพื่อให้ตัวเลือก drainage ตัดสินได้)
- Ceftriaxone และ ciprofloxacin ใช้กับ pyogenic abscess (ร่วมกับ metronidazole) ไม่ครอบคลุม E. histolytica
- Amphotericin B เป็นยาเชื้อรา''',
            pearl="Amebic liver abscess → metronidazole + paromomycin", topic="Amebic liver abscess",
            ref=R(180, 181), nl=["2.3.11(8)"]),
        mcq("EXAM25-03-03-4",
            "A 50-year-old woman presents with jaundice and fever. Liver function tests show mildly elevated AST and ALT and an alkaline phosphatase of 300 U/L. What is the most likely diagnosis?",
            "Cholestasis",
            ["Acute viral hepatitis", "Alcoholic hepatitis", "Cirrhosis", "Non-alcoholic fatty liver disease"],
            kind="old", src=SRC,
            explain='''**ALP สูงเด่น** (300) โดย AST/ALT สูงเพียงเล็กน้อย = **cholestatic pattern** (ร่วมกับไข้และดีซ่าน ควรคิดถึงการอุดตันทางเดินน้ำดี/cholangitis และทำ U/S ต่อ)
- Acute viral hepatitis ให้ AST/ALT สูงมาก (หลักพัน) เด่นกว่า ALP
- Alcoholic hepatitis ให้ AST:ALT > 2 และ AST มักไม่เกิน 300–400
- Cirrhosis มักมี albumin ต่ำ INR ยาว ไม่ใช่ ALP สูงเด่น
- NAFLD มัก ALT สูงเล็กน้อย ไม่มีไข้หรือดีซ่าน''',
            pearl="ALP เด่น = cholestasis · AST/ALT เด่น = hepatocellular", topic="LFT pattern",
            ref=R(182, 183), nl=["2.1.13"]),
    ])

LECTURE = lecture("03", "GI", "dyspepsia · UGIB · pancreatitis · paracetamol · liver abscess",
    objectives=[
        "รู้ข้อบ่งชี้ส่อง EGD ใน dyspepsia และ pill esophagitis",
        "แยกสาเหตุ UGIB จากประวัติ และให้ยาก่อนส่องกล้องได้ถูก",
        "หาสาเหตุ pancreatitis, ประเมินพิษ paracetamol, รักษา amebic abscess",
        "อ่านรูปแบบ LFT แยก cholestasis กับ hepatocellular",
    ],
    sections=[S1, S2, S3])
