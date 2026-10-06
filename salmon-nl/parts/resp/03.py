from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-Respiratory"
OLD = "ข้อสอบเก่าในสไลด์ MedSalmon"

FIG_LIGHT = '''<svg viewBox="0 0 740 400">
 <defs><marker id="resp-03-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="240" y="10" width="260" height="46" rx="10" class="acsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">Pleural effusion → Thoracentesis</text>
 <text x="370" y="48" text-anchor="middle" class="t3">ส่ง protein, LDH คู่กับ serum ทุกครั้ง</text>
 <path d="M370 56V80" class="ln" marker-end="url(#resp-03-01-a)"/>
 <rect x="170" y="82" width="400" height="80" rx="10" class="box"/>
 <text x="370" y="104" text-anchor="middle" class="tb">Light's criteria — มี ≥ 1 ข้อ = Exudate</text>
 <text x="190" y="126" class="t2">1. Protein pleural/serum &gt; 0.5</text>
 <text x="190" y="144" class="t2">2. LDH pleural/serum &gt; 0.6</text>
 <text x="396" y="126" class="t2">3. LDH pleural &gt; 2/3 ULN</text>
 <text x="410" y="144" class="t3">ของ serum LDH</text>
 <path d="M260 162L140 194" class="ln" marker-end="url(#resp-03-01-a)"/>
 <path d="M480 162L560 194" class="ln" marker-end="url(#resp-03-01-a)"/>
 <text x="150" y="172" class="ta">ไม่มีเลย</text>
 <text x="530" y="176" class="ta">≥ 1 ข้อ</text>
 <rect x="20" y="196" width="230" height="130" rx="10" class="oksoft"/>
 <text x="135" y="218" text-anchor="middle" class="tb">Transudate</text>
 <text x="135" y="236" text-anchor="middle" class="t3">hydrostatic ↑ / oncotic ↓</text>
 <text x="34" y="260" class="t2">• Heart failure</text>
 <text x="34" y="280" class="t2">• Cirrhosis</text>
 <text x="34" y="300" class="t2">• Nephrotic, PD</text>
 <text x="34" y="318" class="t3">มักสองข้างพอ ๆ กัน</text>
 <rect x="270" y="196" width="450" height="194" rx="10" class="badsoft"/>
 <text x="495" y="218" text-anchor="middle" class="tb">Exudate → ดู cell differential + ตรวจเพิ่ม</text>
 <rect x="284" y="230" width="205" height="150" rx="8" class="box"/>
 <text x="386" y="250" text-anchor="middle" class="tb">Neutrophil &gt; 50%</text>
 <text x="296" y="274" class="t2">• Parapneumonic</text>
 <text x="296" y="294" class="t2">• Empyema</text>
 <text x="296" y="314" class="t2">• PE</text>
 <text x="296" y="340" class="t3">ดู pH, glucose, G/S,</text>
 <text x="296" y="356" class="t3">C/S → ต้อง drain ไหม</text>
 <rect x="501" y="230" width="205" height="150" rx="8" class="box"/>
 <text x="603" y="250" text-anchor="middle" class="tb">Lymphocyte &gt; 50%</text>
 <text x="513" y="274" class="t2">• TB → ADA &gt; 40</text>
 <text x="513" y="294" class="t2">• Malignancy → cytology</text>
 <text x="513" y="314" class="t2">• Chylothorax → TG &gt; 110</text>
 <text x="513" y="340" class="t3">(lupus/RA → ANA, RF)</text>
</svg>'''

FIG_PARA = '''<svg viewBox="0 0 720 270">
 <defs><marker id="resp-03-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <text x="360" y="22" text-anchor="middle" class="tb">Parapneumonic effusion: 3 ระยะ</text>
 <path d="M20 54H700" class="ln" marker-end="url(#resp-03-02-a)"/>
 <text x="690" y="44" text-anchor="end" class="t3">เวลา/ความรุนแรง →</text>
 <rect x="20" y="70" width="215" height="190" rx="10" class="oksoft"/>
 <text x="127" y="94" text-anchor="middle" class="tb">Simple</text>
 <text x="34" y="120" class="t2">free-flow</text>
 <text x="34" y="140" class="t2">&lt; ½ hemithorax</text>
 <text x="34" y="160" class="t2">pH &gt; 7.2 · glucose &gt; 60</text>
 <text x="34" y="180" class="t2">G/S, C/S ลบ</text>
 <rect x="34" y="206" width="187" height="40" rx="8" class="ok"/>
 <text x="127" y="231" text-anchor="middle" class="tw">ATB + observe</text>
 <rect x="252" y="70" width="215" height="190" rx="10" class="misssoft"/>
 <text x="359" y="94" text-anchor="middle" class="tb">Complicated</text>
 <text x="266" y="120" class="t2">&gt; ½ hemithorax</text>
 <text x="266" y="140" class="t2">septate / loculated</text>
 <text x="266" y="160" class="t2">pH &lt; 7.2 · glucose &lt; 60</text>
 <text x="266" y="180" class="t2">C/S ลบ</text>
 <rect x="266" y="206" width="187" height="40" rx="8" class="miss"/>
 <text x="359" y="231" text-anchor="middle" class="tw">ATB + drainage (ICD)</text>
 <rect x="485" y="70" width="215" height="190" rx="10" class="badsoft"/>
 <text x="592" y="94" text-anchor="middle" class="tb">Empyema</text>
 <text x="499" y="120" class="t2">frank pus</text>
 <text x="499" y="140" class="t2">หรือ G/S บวก</text>
 <text x="499" y="160" class="t2">หรือ C/S บวก</text>
 <rect x="499" y="206" width="187" height="40" rx="8" class="bad"/>
 <text x="592" y="231" text-anchor="middle" class="tw">ATB + drainage (ICD)</text>
</svg>'''

FIG_PTX = '''<svg viewBox="0 0 740 420">
 <defs><marker id="resp-03-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="40" rx="10" class="acsoft"/>
 <text x="370" y="35" text-anchor="middle" class="tb">Spontaneous pneumothorax</text>
 <path d="M370 50V72" class="ln" marker-end="url(#resp-03-03-a)"/>
 <rect x="200" y="74" width="340" height="50" rx="10" class="badsoft"/>
 <text x="370" y="95" text-anchor="middle" class="tb">BP ต่ำ · trachea เบี้ยวออก · JVP โป่ง ?</text>
 <text x="370" y="114" text-anchor="middle" class="t3">= Tension pneumothorax (Dx ทางคลินิก ไม่รอ CXR)</text>
 <path d="M540 99H590" class="ln" marker-end="url(#resp-03-03-a)"/>
 <rect x="592" y="70" width="140" height="58" rx="10" class="bad"/>
 <text x="662" y="94" text-anchor="middle" class="tw">Needle 4–5th ICS</text>
 <text x="662" y="114" text-anchor="middle" class="tw">ant. to MAL → ICD</text>
 <path d="M370 124V146" class="ln" marker-end="url(#resp-03-03-a)"/>
 <text x="380" y="140" class="t3">ไม่ใช่</text>
 <rect x="240" y="148" width="260" height="34" rx="10" class="box"/>
 <text x="370" y="170" text-anchor="middle" class="tb">มีอาการไหม?</text>
 <path d="M280 182L110 214" class="ln" marker-end="url(#resp-03-03-a)"/>
 <path d="M370 182V214" class="ln" marker-end="url(#resp-03-03-a)"/>
 <path d="M460 182L610 214" class="ln" marker-end="url(#resp-03-03-a)"/>
 <rect x="20" y="216" width="180" height="62" rx="10" class="oksoft"/>
 <text x="110" y="240" text-anchor="middle" class="tb">ไม่มีอาการ</text>
 <text x="110" y="262" text-anchor="middle" class="t2">Conservative</text>
 <rect x="230" y="216" width="280" height="110" rx="10" class="misssoft"/>
 <text x="370" y="238" text-anchor="middle" class="tb">มีอาการ + ไม่ high risk</text>
 <text x="246" y="262" class="t2">• Conservative หรือ</text>
 <text x="246" y="282" class="t2">• Ambulatory device หรือ</text>
 <text x="246" y="302" class="t2">• Needle aspiration</text>
 <text x="246" y="320" class="t3">ไม่ดีขึ้น → admit + ICD</text>
 <rect x="530" y="216" width="200" height="190" rx="10" class="badsoft"/>
 <text x="630" y="238" text-anchor="middle" class="tb">มีอาการ + high risk</text>
 <text x="630" y="258" text-anchor="middle" class="ta">Admit + ICD</text>
 <text x="542" y="282" class="t3">• hemodynamic compromise</text>
 <text x="542" y="300" class="t3">• significant hypoxemia</text>
 <text x="542" y="318" class="t3">• bilateral</text>
 <text x="542" y="336" class="t3">• underlying lung disease</text>
 <text x="542" y="354" class="t3">• อายุ ≥ 50 + สูบบุหรี่</text>
 <text x="542" y="372" class="t3">• hemopneumothorax</text>
 <text x="542" y="396" class="t3">ขนาด ไม่ใช่ข้อบ่งชี้</text>
 <rect x="20" y="340" width="490" height="66" rx="10" class="sunk"/>
 <text x="34" y="362" class="t2">Persistent air leak &gt; 5–7 วัน → ICD ใหญ่ขึ้น, pleurodesis,</text>
 <text x="34" y="380" class="t2">endobronchial valve, thoracic surgery</text>
 <text x="34" y="398" class="t3">ผ่าตัดป้องกันซ้ำ: อาชีพเสี่ยง · tension · เป็นซ้ำข้างเดิม/อีกข้าง</text>
</svg>'''

S1 = sec("resp-03-01", "Pleural effusion: approach และ Light's criteria",
    "Transudate vs exudate ด้วย Light's criteria (≥ 1 ข้อ = exudate) · แยกต่อด้วย cell diff, pH, glucose, ADA, cytology",
    minutes=9, source=f"{D} หน้า 160–171, 175–176, 179–192", nl=["2.3.10(7)", "B6.3(1)", "3.1.7"],
    md='''
### กลไก
| Transudate | Exudate |
|---|---|
| hydrostatic pressure ↑ / oncotic pressure ↓ | capillary permeability ↑ / lymphatic reabsorption ↓ |
| Heart failure, cirrhosis, nephrotic syndrome, peritoneal dialysis | Parapneumonic, malignancy, tuberculosis, pulmonary embolism |
| มักเป็นสองข้างพอ ๆ กัน | มักเด่นข้างเดียว ปริมาณมาก |

### ตรวจร่างกาย
- chest expansion ↓, tactile fremitus ↓, **dullness on percussion**, breath sounds ↓
- **Massive effusion → trachea และ mediastinum ถูกดันไปฝั่งตรงข้าม**

> **Massive effusion vs total lung atelectasis**: ทั้งคู่ทึบทั้งข้าง แต่ effusion ดัน trachea **ออกไปฝั่งตรงข้าม** ส่วน atelectasis ดึง trachea **เข้าหาฝั่งเดียวกัน**

### Imaging
- **CXR upright**: blunt costophrenic angle, **meniscus sign**, ทึบทั้งข้าง (total opacification)
- **CXR lateral decubitus** (นอนตะแคง **ทับข้างที่สงสัย**): เห็นน้ำปริมาณน้อย และดูว่าน้ำไหลอิสระ (free-flow)
- U/S chest (ใช้นำทางเจาะ — เสริม), CT chest

### Thoracentesis — ส่งตรวจอะไร
- พื้นฐาน: **cell count + differential, Gram stain, C/S, protein, albumin, LDH, pH, glucose**
- เพิ่มตามที่สงสัย: cancer → **cytology** · TB → **ADA** · autoimmune → **ANA, RF** · chylothorax → **TG** · pancreatitis/esophageal perforation → **amylase** · hemothorax → **Hct**

[[fig:resp-03-01-light]]

### Light's criteria — มี ≥ 1 ข้อ = Exudate
1. Pleural protein / serum protein **> 0.5**
2. Pleural LDH / serum LDH **> 0.6**
3. Pleural LDH **> 2/3 ของค่าสูงสุดปกติ** ของ serum LDH

### อ่านผล pleural fluid
| ค่าที่พบ | นึกถึง |
|---|---|
| ขุ่นขาวเหมือนนม | chylothorax (TG > 110 mg/dL) |
| เป็นหนอง | parapneumonic, empyema |
| มีเลือดปน | hemothorax, malignant, PE |
| Neutrophil > 50% | parapneumonic, PE |
| Lymphocyte > 50% | malignancy, **TB pleuritis**, chylothorax |
| WBC > 10,000 | parapneumonic, empyema, autoimmune, PE |
| RBC > 5,000 | hemothorax, malignant |
| Glucose < 60 mg/dL | malignant, parapneumonic, empyema, TB, autoimmune (RA) |
| pH < 7.2 | complicated parapneumonic, empyema, malignant |
| ADA > 40 U/L | **TB pleurisy** |
| Cytology ผิดปกติ | malignant effusion |
| Amylase > 200 | pancreatitis, esophageal perforation |
| ANA, RF บวก | autoimmune (lupus, RA) |

### Tuberculous pleuritis
- ไข้ เหงื่อออกกลางคืน น้ำหนักลด, ไอแห้ง, เจ็บหน้าอกแบบ pleuritic
- Exudate, **lymphocyte เด่น, ADA > 40 U/L**
- Sputum AFB (**50% มี pulmonary TB ร่วม**) · **AFB ในน้ำ pleural มักเป็นลบ** (pleural biopsy ให้ผลบวกสูงกว่า — เสริม)
- รักษา: therapeutic thoracentesis + **anti-TB (IRZE)**

### Malignant pleural effusion
- พบบ่อยจาก **lung cancer, breast cancer**
- Constitutional symptoms, cachexia, เหนื่อย, ไอ · มักเป็นเลือดปน lymphocyte เด่น
- **Pleural fluid cytology** ผิดปกติ · CT chest หามะเร็งต้นเหตุ
- รักษา: therapeutic thoracentesis, indwelling pleural catheter, **pleurodesis**, รักษามะเร็ง

> **Lupus pleuritis**: exudate, glucose ปกติ, ANA บวก, มักเป็นสองข้าง · **TB pleuritis**: ADA > 40, มักเป็นข้างเดียว
''',
    figs=[fig("resp-03-01-light", "Pleural fluid: transudate หรือ exudate แล้วไปต่อทางไหน", FIG_LIGHT,
              "ใช้ Light's criteria ก่อน ถ้าเป็น exudate ให้ดู cell differential: neutrophil เด่นนึกถึงการติดเชื้อ ส่วน lymphocyte เด่นนึกถึง TB หรือมะเร็ง")],
    pearls=["Light's: protein ratio > 0.5 · LDH ratio > 0.6 · LDH > 2/3 ULN — ข้อเดียวก็ exudate",
            "Lymphocytic exudate: TB (ADA > 40) vs malignancy (cytology)",
            "TB pleuritis: pleural AFB มักลบ · ADA เป็นตัวช่วยหลัก",
            "Lateral decubitus: นอนตะแคงทับข้างที่สงสัย",
            "Effusion ดัน trachea ออก · atelectasis ดึง trachea เข้า"],
    items=[
        mcq("RESP-03-01-1", """A 30-year-old woman has fever, progressive dyspnea and dry cough for 10 days. CXR: right pleural effusion without infiltrate. Pleural fluid: WBC 600 (lymphocytes 90%), protein 5 g/dL, LDH 190 U/L, glucose 30 mg/dL. Serum: total protein 7.9 g/dL, LDH 110 U/L, glucose 80 mg/dL. What is the most appropriate investigation?""",
            "Pleural fluid adenosine deaminase (ADA)",
            ["Pleural fluid cytology", "CT chest", "Tuberculin skin test", "Interferon-gamma release assay"],
            explain="""Protein ratio 5/7.9 = 0.63 (> 0.5) และ LDH ratio 190/110 = 1.7 (> 0.6) จึงเป็น exudate ที่ lymphocyte เด่น glucose ต่ำ ในหญิงอายุน้อยที่มีไข้ 10 วัน นึกถึง TB pleuritis มากที่สุด การตรวจที่ช่วยได้คือ pleural ADA (> 40 U/L สนับสนุน TB)
- Cytology ใช้เมื่อสงสัยมะเร็ง ซึ่งไม่เข้ากับอายุและอาการไข้เฉียบพลัน
- CT chest ไม่ได้ยืนยันว่าเป็น TB pleuritis
- TST และ IGRA บอกได้แค่ว่าเคยติดเชื้อ TB แยก active disease ไม่ได้ และในประเทศที่ TB ชุกมักให้ผลบวกอยู่แล้ว""",
            pearl="Lymphocytic exudate + ไข้ในคนอายุน้อย → pleural ADA",
            topic="TB pleuritis", ref=[f"{D} หน้า 171, 173, 187–188"], nl=["2.3.10(7)", "B6.3(1)"], kind="old", src=OLD),
        mcq("RESP-03-01-2", """A 74-year-old man has had dyspnea for 3 months and lost 10 kg. CXR: pleural effusion. Pleural fluid: WBC 1,250 (lymphocytes 90%), RBC 2,000, LDH 600 U/L, protein 5.5 g/dL. Serum: LDH 230 U/L, protein 7.0 g/dL. What is the most likely diagnosis?""",
            "Malignant pleural effusion from lung cancer",
            ["Cirrhosis with hepatic hydrothorax", "Chylothorax", "Empyema thoracis", "Simple parapneumonic effusion"],
            explain="""Light's criteria เป็น exudate (LDH ratio 600/230 = 2.6, protein ratio 5.5/7.0 = 0.79) lymphocyte เด่น มีเลือดปนเล็กน้อย ในผู้สูงอายุที่น้ำหนักลดมาก เข้ากับ malignant effusion (CA lung)
- Hepatic hydrothorax เป็น transudate
- Chylothorax มีลักษณะขุ่นขาวเหมือนนม และ TG > 110
- Empyema เป็นหนอง neutrophil เด่น
- Parapneumonic effusion เป็น neutrophil เด่น และมีไข้จาก pneumonia
(ข้อสอบเก่าต้นฉบับให้ serum protein 3.5 ซึ่งต่ำกว่า pleural จึงปรับให้สมเหตุสมผล)""",
            pearl="ผู้สูงอายุ น้ำหนักลด + lymphocytic bloody exudate → malignancy",
            topic="Malignant effusion", ref=[f"{D} หน้า 174, 191–192"], nl=["2.3.10(7)"], kind="old", src=OLD),
        mcq("RESP-03-01-3", """A 40-year-old woman with SLE has dyspnea not improved after 3 days of amoxicillin. CXR: right pleural effusion. Pleural fluid: straw-colored, WBC 600 (PMN 40%, L 60%), protein 4 g/dL, glucose 100 mg/dL, Gram stain negative, AFB negative. What is the most likely diagnosis?""",
            "Lupus pleuritis",
            ["Complicated parapneumonic effusion", "Tuberculous pleuritis", "Malignant pleuritis", "Hepatic hydrothorax"],
            explain="""ผู้ป่วยเป็น SLE น้ำ pleural เป็น exudate สีฟาง glucose ปกติ (100) ไม่พบเชื้อ เข้ากับ lupus pleuritis ซึ่ง ANA ในน้ำ pleural จะบวกและมักเป็นสองข้าง
- Complicated parapneumonic effusion ต้องมี pH < 7.2 และ glucose < 60 ส่วนใหญ่เป็น neutrophil
- TB pleuritis มักมี lymphocyte > 80–90% และ glucose ต่ำ ยืนยันด้วย ADA > 40
- Malignant pleuritis ต้องมีอาการ constitutional และ cytology ผิดปกติ
- Hepatic hydrothorax เป็น transudate (protein ต่ำ)""",
            pearl="SLE + exudate glucose ปกติ ไม่พบเชื้อ = lupus pleuritis (ANA บวก)",
            topic="Lupus pleuritis", ref=[f"{D} หน้า 171, 183–184"], nl=["2.3.10(7)"], kind="old", src=OLD),
        mcq("RESP-03-01-4", """A heavy smoker has low-grade fever and fatigue for 2 weeks. Examination: decreased breath sounds and dullness of the right lung with tracheal shift to the left. Thoracentesis: straw-colored, WBC 1,520 (mononuclear 80%), pH 7.30, glucose 30 mg/dL. What is the most appropriate investigation?""",
            "Pleural fluid cytology",
            ["Gram stain", "Modified AFB stain", "Pleural fluid culture", "Pleural fluid ADA"],
            explain="""ผู้สูบบุหรี่จัด มี effusion ปริมาณมากจนดัน trachea ไปฝั่งตรงข้าม น้ำเป็น mononuclear เด่น glucose ต่ำ นึกถึง malignant effusion (lung cancer) ข้อสอบเก่าข้อนี้เฉลยว่าตรวจ cytology
- Gram stain และ culture ใช้กับ effusion ที่ neutrophil เด่นจาก pneumonia
- Modified AFB ใช้หา Nocardia ไม่ใช่การตรวจหลักของ effusion
- ADA ช่วยวินิจฉัย TB ซึ่งก็ให้ภาพคล้ายกันได้ แต่ประวัติสูบบุหรี่จัด ร่วมกับ massive effusion ที่ดัน trachea ทำให้คิดถึงมะเร็งก่อน (ในทางปฏิบัติมักส่งทั้ง cytology และ ADA)""",
            pearl="Smoker + massive lymphocytic effusion → cytology",
            topic="Malignant effusion workup", ref=[f"{D} หน้า 174, 189–190"], nl=["B6.3(1)"], kind="old", src=OLD),
        mcq("RESP-03-01-5", """A 65-year-old man with hypertension has dyspnea. The physician suspects a small left pleural effusion and wants a chest radiograph that is most sensitive for a small amount of free fluid. Which view should be requested?""",
            "Left lateral decubitus view",
            ["Right lateral decubitus view", "Lordotic view", "Supine AP view", "Expiratory PA view"],
            explain="""Lateral decubitus ให้นอนตะแคงทับข้างที่สงสัย น้ำที่ไหลได้อิสระจะไหลลงไปตามผนังทรวงอกด้านล่าง จึงเห็นน้ำปริมาณน้อยได้ (สงสัยข้างซ้าย → left lateral decubitus)
- Right lateral decubitus ทำให้น้ำทางซ้ายไหลไปที่ mediastinum มองไม่เห็น (ใช้ดูเนื้อปอดข้างซ้ายใต้น้ำ)
- Lordotic view ใช้ดู apex ของปอด
- Supine AP ทำให้น้ำกระจายไปด้านหลัง เห็นแค่ความทึบจาง ๆ ไม่ไว
- Expiratory film ใช้หา pneumothorax ขนาดเล็ก""",
            pearl="Lateral decubitus: ตะแคงทับข้างที่สงสัย",
            topic="Decubitus view", ref=[f"{D} หน้า 163, 175–176"], nl=["3.2.1"], kind="old", src=OLD),
        mcq("RESP-03-01-6", """A 60-year-old Thai woman with no known underlying disease has had dyspnea for 3 months. Examination: decreased chest expansion, dullness and absent breath sounds over the entire left hemithorax, with the trachea shifted to the right. CXR: whiteout of the left lung. What is the most appropriate next investigation?""",
            "Thoracentesis",
            ["CT chest", "Serum CEA level", "Bronchoscopy", "Sputum cytology"],
            explain="""ปอดซ้ายทึบทั้งข้าง และ trachea ถูกดันไปทางขวา (ออกจากด้านที่ผิดปกติ) คือ massive pleural effusion ไม่ใช่ total atelectasis (ซึ่งจะดึง trachea เข้าหา) ขั้นต่อไปคือเจาะน้ำเพื่อวินิจฉัยและบรรเทาอาการ
- CT chest ทำได้หลังเจาะน้ำออกแล้ว เพื่อหาก้อนที่ถูกน้ำบังอยู่
- CEA ไม่จำเพาะ และไม่ได้ให้การวินิจฉัย
- Bronchoscopy เหมาะกับ total atelectasis จากก้อนอุดหลอดลม
- Sputum cytology มีความไวต่ำ และไม่ใช่การตรวจแรกของ effusion""",
            pearl="Whiteout + trachea ถูกดันออก = massive effusion → thoracentesis",
            topic="Massive effusion", ref=[f"{D} หน้า 165, 179–180"], nl=["2.3.10(7)"], kind="old", src=OLD),
    ])

S2 = sec("resp-03-02", "Parapneumonic effusion และ empyema",
    "Simple (pH > 7.2, glu > 60) → ATB · complicated (pH < 7.2, glu < 60, loculated) หรือ empyema → ATB + ICD",
    minutes=6, source=f"{D} หน้า 172, 177–178, 193–196", nl=["2.3.10(7)", "2.3.10-3(2)"],
    md='''
### กลไก
Pneumonia ทำให้ capillary ของเยื่อหุ้มปอดรั่ว → **simple** effusion (ปลอดเชื้อ) → เชื้อเข้าช่องเยื่อหุ้มปอด เกิด fibrin และ septation → **complicated** → เป็นหนอง = **empyema**

[[fig:resp-03-02-para]]

| ระยะ | X-ray | pH | Glucose (mg/dL) | C/S | รักษา |
|---|---|---|---|---|---|
| Simple | free-flow, small–moderate (< ½ hemithorax) | > 7.2 | > 60 | ลบ | ATB, observe |
| Complicated | large (> ½ hemithorax), septate/loculated | < 7.2 | < 60 | ลบ | ATB + **drainage** |
| Empyema | frank pus หรือ G/S/C/S บวก | — | — | บวก | ATB + **drainage** |

### หลักปฏิบัติ
- Pneumonia + effusion ที่หนาพอเจาะได้ (≥ 10 mm บน decubitus/US — เสริม) → **เจาะ (pleural fluid aspiration) ทุกราย** เพื่อดูว่าต้อง drain หรือไม่
- ให้ ATB แล้วไข้ไม่ลง + มี effusion → คิดว่า effusion ติดเชื้อ ต้อง **drain (ICD)** ไม่ใช่เปลี่ยน ATB ให้แรงขึ้น
- ยาไม่สามารถเข้าไปถึงหนองที่เป็นช่อง ๆ ได้ดี → หลักคือ **source control**

> ข้อสอบเก่า: pneumonia ให้ augmentin 3 วันแล้วไม่ดีขึ้น effusion: WBC 2,500 (N 90%) LDH 900 → ข้อมูลยังไม่ครบ ต้องดู **pH, glucose, G/S, C/S, หนองไหม, ขนาด/septation** ก่อนตัดสินใจใส่ ICD

> Pneumonia + effusion + sputum/pleural G/S เห็น WBC มาก + mixed organism + ให้ ATB 3 วันไข้ไม่ลง → **ICD**
''',
    figs=[fig("resp-03-02-para", "Simple → complicated → empyema", FIG_PARA,
              "เมื่อ pH ต่ำกว่า 7.2, glucose ต่ำกว่า 60, มี loculation หรือเป็นหนอง/เพาะเชื้อขึ้น ต้องใส่ท่อระบายร่วมกับให้ ATB")],
    pearls=["Pneumonia + effusion → เจาะดู profile ทุกราย",
            "Complicated: pH < 7.2, glucose < 60, loculated, > ½ hemithorax → ATB + ICD",
            "Empyema = frank pus หรือ G/S/C/S บวก → ICD",
            "ATB แล้วไข้ไม่ลงเพราะมี effusion ติดเชื้อ → drain ไม่ใช่เปลี่ยนยา"],
    items=[
        mcq("RESP-03-02-1", """A 24-year-old man has had high fever for 4 days despite self-medicated amoxicillin. BT 39°C, vital signs otherwise stable. There is dullness and decreased breath sounds over the left lower lung. CXR: patchy infiltration with a left pleural effusion. What is the most appropriate investigation for diagnosis?""",
            "Diagnostic pleural fluid aspiration",
            ["Mycoplasma antibody titer", "Sputum culture only", "CT chest", "Bronchoscopy with BAL"],
            explain="""Pneumonia ที่มี effusion ต้องเจาะน้ำออกมาตรวจ (pH, glucose, cell, G/S, C/S) เพื่อแยกว่าเป็น simple หรือ complicated/empyema ซึ่งกำหนดว่าต้องใส่ท่อระบายหรือไม่
- Mycoplasma titer ใช้เวลานาน และไม่ได้เปลี่ยนการจัดการ effusion
- Sputum culture อย่างเดียวไม่บอกสถานะของช่องเยื่อหุ้มปอด
- CT chest ช่วยดู loculation ได้ แต่ไม่ได้ให้การวินิจฉัยทางชีวเคมี
- Bronchoscopy ไม่จำเป็นใน CAP ทั่วไป""",
            pearl="Pneumonia + effusion → thoracentesis",
            topic="Parapneumonic workup", ref=[f"{D} หน้า 177–178"], nl=["2.3.10(7)"], kind="old", src=OLD),
        mcq("RESP-03-02-2", """A 50-year-old man has had fever and foul-smelling green sputum for 7 days. CXR: RLL infiltration with moderate pleural effusion. Sputum and pleural fluid Gram stains show numerous WBC with mixed organisms. After 3 days of ceftriaxone plus clindamycin, he remains febrile. What is the most appropriate management?""",
            "Intercostal chest drainage (ICD)",
            ["Postural drainage", "Bronchoscopy", "Repeat diagnostic pleural tap only", "Change antibiotic to imipenem"],
            explain="""Pleural fluid ที่ Gram stain เห็นเชื้อคือ empyema ซึ่งต้องระบายออก (ICD) ร่วมกับให้ ATB การที่ไข้ไม่ลงเกิดจากหนองที่ค้างอยู่ ไม่ได้เป็นเพราะ ATB ไม่ครอบคลุม
- Postural drainage ใช้ระบายเสมหะในหลอดลม ไม่ได้ระบายช่องเยื่อหุ้มปอด
- Bronchoscopy ไม่ช่วย empyema
- การเจาะซ้ำแค่เพื่อตรวจ ระบายหนองไม่พอ
- การเปลี่ยนเป็น imipenem ไม่ได้แก้หนองที่ค้างอยู่""",
            pearl="Empyema = ATB + ICD (source control)",
            topic="Empyema", ref=[f"{D} หน้า 172, 193–194"], nl=["2.3.10-3(2)"], kind="old", src=OLD),
        mcq("RESP-03-02-3", """A 58-year-old man with right lower lobe pneumonia has a moderate free-flowing effusion. Thoracentesis: turbid fluid, pH 7.05, glucose 35 mg/dL, LDH 1,200 U/L, Gram stain negative. What is the most appropriate management?""",
            "Continue antibiotics and insert a chest drain",
            ["Continue antibiotics and observe", "Switch to antifungal therapy",
             "Repeat thoracentesis in 1 week", "Start anti-tuberculosis drugs"],
            explain="""pH < 7.2 และ glucose < 60 คือ complicated parapneumonic effusion แม้ Gram stain จะลบ ก็ต้องระบายด้วย ICD ร่วมกับให้ ATB ต่อ
- การให้ ATB แล้วเฝ้าดูอย่างเดียวใช้กับ simple effusion (pH > 7.2 และ glucose > 60)
- ไม่มีข้อบ่งชี้ว่าเป็นเชื้อรา
- การรอ 1 สัปดาห์ทำให้เกิด loculation และ fibrothorax
- TB pleuritis มี lymphocyte เด่น ไม่ได้มีภาพแบบนี้ที่สัมพันธ์กับ pneumonia เฉียบพลัน""",
            pearl="pH < 7.2 หรือ glucose < 60 → drain",
            topic="Complicated parapneumonic", ref=[f"{D} หน้า 172"], nl=["2.3.10(7)", "B6.3(1)"]),
        mcq("RESP-03-02-4", """A woman with pneumonia (sputum: pleomorphic gram-positive cocci) has not improved after 3 days of amoxicillin/clavulanate. Repeat CXR shows a new pleural effusion. Pleural fluid: WBC 2,500 (neutrophils 90%), LDH 900 U/L. Other results are pending. Before deciding on chest drainage, which additional pleural fluid results are most needed?""",
            "pH, glucose, Gram stain and culture, gross appearance and presence of loculation",
            ["ADA and lymphocyte count", "Triglyceride and cholesterol", "Amylase and lipase", "Hematocrit and RBC count"],
            explain="""ข้อมูลที่มีบอกได้แค่ว่าเป็น exudate ที่ neutrophil เด่น ซึ่งเข้ากับ parapneumonic effusion แต่การตัดสินใจว่าจะใส่ ICD ต้องอาศัย pH, glucose, G/S, C/S, ลักษณะว่าเป็นหนองหรือไม่ และขนาดหรือ septation ตามที่ข้อสอบเก่าในสไลด์เฉลยไว้
- ADA และ lymphocyte ใช้แยก TB ซึ่งไม่เข้ากับภาพ neutrophilic
- TG ใช้วินิจฉัย chylothorax
- Amylase ใช้เมื่อสงสัย pancreatitis หรือ esophageal rupture
- Hct ใช้ยืนยัน hemothorax""",
            pearl="ตัดสินใจ drain จาก pH, glucose, G/S/C/S, pus, loculation",
            topic="Drainage decision", ref=[f"{D} หน้า 195–196"], nl=["B6.3(1)"], kind="old", src=OLD),
    ])

S3 = sec("resp-03-03", "Pneumothorax",
    "PSP (tall thin, blebs) vs SSP · tension → needle 4–5th ICS ant. MAL แล้ว ICD · high-risk → ICD · ขนาดไม่ใช่ข้อบ่งชี้",
    minutes=8, source=f"{D} หน้า 78–91", nl=["2.3.10(6)", "2.2.14", "B6.2.6(1)"],
    md='''
### ชนิด
| ชนิด | ลักษณะ |
|---|---|
| **Primary spontaneous (PSP)** | ไม่มีโรคปอดเดิม · subpleural apical bleb แตก · **ชายผอมสูง** (สูบบุหรี่เพิ่มเสี่ยง — เสริม) |
| **Secondary spontaneous (SSP)** | ภาวะแทรกซ้อนของโรคปอดเดิม เช่น **COPD, TB, PCP** |
| Traumatic | บาดเจ็บ/หัตถการ (รวมถึง barotrauma จาก ventilator — เสริม) |

### อาการและตรวจร่างกาย
- เจ็บหน้าอกแบบ pleuritic ข้างเดียว **เกิดทันที**, เหนื่อย
- Subcutaneous emphysema
- chest expansion ↓, tactile fremitus ↓, **hyperresonance**, breath sounds ↓
- CXR: ปอดยุบ เห็น **visceral pleural line** และไม่มี lung marking ด้านนอกเส้น

### Tension pneumothorax — วินิจฉัยทางคลินิก ไม่ต้องรอ CXR
- **BP ↓, PR ↑**, trachea เบี้ยวไป **ฝั่งตรงข้าม**, **JVP โป่ง**
- รักษา: **needle decompression ทันที ที่ ICS 4–5 ด้านหน้าต่อ midaxillary line** (ATLS ปัจจุบันในผู้ใหญ่ — เดิมใช้ 2nd ICS MCL) → แล้วใส่ **ICD**
- คนไข้ใช้ ventilator (positive pressure) แล้ว BP ตกทันที + hyperresonance ข้างเดียว = tension จนกว่าจะพิสูจน์ได้ว่าไม่ใช่

[[fig:resp-03-03-ptx]]

### การรักษา spontaneous pneumothorax (สไลด์ 81–83 เป็นภาพ algorithm สรุปจาก 84–86)
- **ไม่มีอาการ** → conservative
- **มีอาการ + high risk** → **admit + ICD**
  - high risk: hemodynamic compromise (tension), significant hypoxemia, **bilateral**, **underlying lung disease**, อายุ ≥ 50 + สูบบุหรี่มาก, hemopneumothorax
  - **ขนาดของ pneumothorax ไม่ใช่ข้อบ่งชี้ในการใส่ ICD**
- **มีอาการ + ไม่ high risk** → conservative หรือ ambulatory device หรือ **needle aspiration** → ไม่ดีขึ้น (อาการ/CXR) → admit + ICD
- **Persistent air leak** (ลมยังรั่วหลัง 5–7 วัน) → ICD ใหญ่ขึ้น, chemical pleurodesis, endobronchial valve, thoracic surgery

### ผ่าตัดเพื่อป้องกันการเป็นซ้ำ
- อาชีพเสี่ยง (นักดำน้ำ นักบิน ทหาร)
- เคยเป็น tension pneumothorax
- เป็นซ้ำข้างเดิมครั้งที่สอง หรือเป็นครั้งแรกของอีกข้าง

### Re-expansion pulmonary edema
- **Pulmonary edema ข้างเดียว** เกิดภายใน **< 24 ชม.** หลังปอดที่ยุบอยู่ถูกขยายเร็ว ๆ (pneumothorax ขนาดใหญ่, ระบาย effusion ปริมาณมาก)
- เหนื่อย SpO2 ต่ำ ไอ **เสมหะเป็นฟองสีชมพู**, crepitation
- รักษา: O2 support (ประคับประคอง)
- ป้องกัน: **ระบายน้ำ < 1–1.5 L ต่อครั้ง**, หลีกเลี่ยง pleural pressure **< −20 cmH2O**
''',
    figs=[fig("resp-03-03-ptx", "การจัดการ spontaneous pneumothorax", FIG_PTX,
              "แยก tension ออกก่อนด้วยอาการทางคลินิก แล้วตัดสินใจจากอาการกับกลุ่ม high risk ไม่ใช่จากขนาดของ pneumothorax")],
    pearls=["PSP = ชายผอมสูง apical bleb · SSP = COPD, TB, PCP",
            "Tension: BP ต่ำ + trachea เบี้ยวออก + JVP โป่ง → needle ทันที (4–5th ICS ant. to MAL) แล้ว ICD",
            "มีอาการ + high risk (bilateral, underlying lung dz, อายุ ≥ 50 + สูบ, hypoxemia) → ICD",
            "ขนาด pneumothorax ไม่ใช่ข้อบ่งชี้ใส่ ICD (ตามสไลด์)",
            "Re-expansion edema: < 24 ชม. หลังระบาย ป้องกันโดยระบาย < 1–1.5 L"],
    items=[
        mcq("RESP-03-03-1", """A 70-year-old man with COPD is on a ventilator for an acute exacerbation. He suddenly develops worsening dyspnea. BP 90/70 mmHg, HR 128/min. Breath sounds are decreased on the right with hyperresonance, and the trachea is shifted to the left. What is the most appropriate immediate management?""",
            "Immediate needle decompression followed by intercostal chest drain on the right",
            ["Portable chest X-ray to confirm the diagnosis", "Normal saline bolus", "Dobutamine infusion", "Increase PEEP"],
            explain="""ผู้ป่วยที่ได้รับ positive pressure ventilation แล้วความดันต่ำ trachea ถูกดันไปฝั่งตรงข้าม และมี hyperresonance คือ tension pneumothorax ซึ่งวินิจฉัยทางคลินิก ต้อง decompress ทันทีแล้วตามด้วย ICD (ข้อสอบเก่าเฉลย ICD)
- การรอ CXR ทำให้การรักษาช้าจนอาจเกิด cardiac arrest
- NSS bolus ไม่ได้แก้การกดทับ venous return
- Dobutamine ไม่ได้แก้สาเหตุ
- การเพิ่ม PEEP ทำให้ลมรั่วมากขึ้นและอาการแย่ลง""",
            pearl="Tension pneumothorax = clinical dx → decompress ก่อน CXR",
            topic="Tension pneumothorax", ref=[f"{D} หน้า 80, 88–89"], nl=["2.2.14"], kind="old", src=OLD),
        mcq("RESP-03-03-2", """A patient with a large hydropneumothorax has an intercostal drain inserted, and fluid is drained rapidly. A few hours later, he develops dyspnea, crackles over the ipsilateral lung and pink frothy sputum. What is the most likely diagnosis?""",
            "Re-expansion pulmonary edema",
            ["Hospital-acquired pneumonia", "Lung laceration from the chest drain", "Atelectasis", "Acute cardiogenic pulmonary edema"],
            explain="""การระบายลมหรือน้ำปริมาณมากอย่างรวดเร็ว แล้วเกิด pulmonary edema ข้างเดียวกันภายใน 24 ชม. (เสมหะเป็นฟองสีชมพู crepitation) คือ re-expansion pulmonary edema ป้องกันโดยระบายไม่เกิน 1–1.5 L ต่อครั้ง (ข้อสอบเก่าใช้คำว่า reperfusion pulmonary edema)
- HAP ต้องเกิดหลัง admit > 48 ชม. และมีไข้
- การบาดเจ็บจาก ICD ทำให้ไอเป็นเลือดหรือ hemothorax ไม่ใช่เสมหะเป็นฟอง
- Atelectasis ไม่ทำให้เสมหะเป็นฟองสีชมพู
- Cardiogenic edema มักเป็นสองข้าง และมีประวัติโรคหัวใจ""",
            pearl="ระบายเร็ว + edema ข้างเดียว < 24 ชม. = re-expansion edema",
            topic="Re-expansion edema", ref=[f"{D} หน้า 87, 90–91"], nl=["B6.2.6(1)"], kind="old", src=OLD),
        mcq("RESP-03-03-3", """A 22-year-old tall, thin man has sudden right pleuritic chest pain while resting. He is mildly dyspneic, SpO2 97%, BP 120/78 mmHg, HR 92/min. CXR shows a right apical pneumothorax with a visible visceral pleural line. He has no lung disease. Which management is appropriate per the lecture?""",
            "Conservative management, ambulatory device or needle aspiration, with ICD if not improving",
            ["Immediate ICD because pneumothorax size determines the need for drainage",
             "Immediate thoracotomy and bullectomy",
             "Discharge without follow-up",
             "Needle decompression at the 2nd intercostal space for tension"],
            explain="""PSP ที่มีอาการเล็กน้อย ไม่เข้าเกณฑ์ high risk (hemodynamic ดี ไม่มี hypoxemia ไม่มีโรคปอดเดิม อายุ < 50) ให้ conservative หรือ ambulatory device หรือ needle aspiration ถ้าไม่ดีขึ้นจึง admit + ICD
- สไลด์ระบุชัดว่าขนาดของ pneumothorax ไม่ใช่ข้อบ่งชี้ในการใส่ ICD
- การผ่าตัดเก็บไว้ใช้เมื่อเป็นซ้ำ หรือมีอาชีพเสี่ยง
- การ D/C โดยไม่นัดติดตาม อาจพลาดกรณีที่ pneumothorax ขยายใหญ่ขึ้น
- ผู้ป่วยไม่มี tension (BP ปกติ trachea ไม่เบี้ยว)""",
            pearl="PSP ไม่ high risk → conservative/aspiration ก่อน",
            topic="PSP management", ref=[f"{D} หน้า 84–85"], nl=["2.3.10(6)"]),
        mcq("RESP-03-03-4", """A 64-year-old man with COPD who smokes 40 pack-years presents with sudden dyspnea. SpO2 86% on room air, BP 130/80 mmHg. CXR shows a left pneumothorax with a 2-cm rim. What is the most appropriate management?""",
            "Admit and insert an intercostal chest drain",
            ["Observe at home because the rim is less than 3 cm", "Needle aspiration and discharge",
             "Thoracic surgery as the first step", "Supplemental oxygen alone and repeat CXR in 1 week"],
            explain="""นี่คือ secondary spontaneous pneumothorax ในผู้ป่วยที่มีโรคปอดเดิม อายุ ≥ 50 สูบบุหรี่จัด และมี hypoxemia ชัดเจน เข้าเกณฑ์ high risk ทุกข้อ จึงต้อง admit และใส่ ICD ไม่ว่าขนาดจะเป็นเท่าไร
- การสังเกตอาการที่บ้านไม่ปลอดภัย และขนาดไม่ใช่ตัวตัดสินตามสไลด์
- Needle aspiration แล้วให้กลับบ้าน ใช้กับคนที่ไม่ high risk
- การผ่าตัดเป็นขั้นต่อมาเมื่อมี persistent air leak หรือเพื่อป้องกันการเป็นซ้ำ
- O2 อย่างเดียวแล้วรอ 1 สัปดาห์ไม่เหมาะกับคนที่ hypoxemia""",
            pearl="SSP / underlying lung disease = high risk → ICD",
            topic="SSP management", ref=[f"{D} หน้า 78, 84"], nl=["2.3.10(6)"]),
        mcq("RESP-03-03-5", """A 30-year-old commercial airline pilot has had his first episode of right primary spontaneous pneumothorax treated successfully with a chest drain. What is the most appropriate recommendation regarding recurrence prevention?""",
            "Refer for thoracic surgery (e.g., VATS pleurodesis/bullectomy) now",
            ["No intervention unless he has a second ipsilateral episode",
             "Long-term inhaled corticosteroid",
             "Prophylactic needle aspiration before each flight",
             "Avoid flying for 1 week only"],
            explain="""สไลด์ระบุว่าผู้ที่มีอาชีพเสี่ยง (นักบิน นักดำน้ำ ทหาร) ควรได้รับการผ่าตัดป้องกันการเป็นซ้ำตั้งแต่ครั้งแรก เพราะถ้าเป็นซ้ำระหว่างทำงานจะอันตรายมาก
- การรอให้เป็นซ้ำข้างเดิมเป็นเกณฑ์ของคนทั่วไป ไม่ใช่อาชีพเสี่ยง
- ICS ไม่ช่วยป้องกัน pneumothorax
- การเจาะดูดก่อนบินไม่มีหลักฐานรองรับ และไม่ป้องกันการเป็นซ้ำ
- การงดบินแค่ 1 สัปดาห์ไม่ได้แก้ความเสี่ยงระยะยาว""",
            pearl="อาชีพเสี่ยง / tension / เป็นซ้ำ → ผ่าตัดป้องกัน",
            topic="Recurrence prevention", ref=[f"{D} หน้า 86"], nl=["2.3.10(6)"]),
    ])

LECTURE = lecture("03", "Pleural diseases",
    subtitle="pleural effusion · parapneumonic/empyema · pneumothorax",
    objectives=["ใช้ Light's criteria แยก transudate/exudate และอ่านผล pleural fluid หาสาเหตุได้",
                "แยก TB, malignant, lupus pleuritis จาก profile น้ำได้",
                "จัดระยะ parapneumonic effusion และบอกข้อบ่งชี้ ICD ได้",
                "วินิจฉัยและรักษา tension pneumothorax และ spontaneous pneumothorax ตามความเสี่ยงได้",
                "รู้จักและป้องกัน re-expansion pulmonary edema ได้"],
    sections=[S1, S2, S3])
