from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-Respiratory"
OLD = "ข้อสอบเก่าในสไลด์ MedSalmon"

FIG_PE = '''<svg viewBox="0 0 740 400">
 <defs><marker id="resp-04-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="44" rx="10" class="acsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">สงสัย PE</text>
 <text x="370" y="47" text-anchor="middle" class="t3">ดู hemodynamic ก่อน (SBP &lt; 90 ?)</text>
 <path d="M300 54L160 86" class="ln" marker-end="url(#resp-04-02-a)"/>
 <path d="M440 54L580 86" class="ln" marker-end="url(#resp-04-02-a)"/>
 <text x="200" y="66" class="ta">Stable</text>
 <text x="520" y="66" class="ta">Shock / arrest</text>
 <rect x="30" y="88" width="260" height="44" rx="10" class="box"/>
 <text x="160" y="108" text-anchor="middle" class="tb">Simple Wells score</text>
 <text x="160" y="125" text-anchor="middle" class="t3">≥ 2 = PE likely</text>
 <path d="M110 132L70 168" class="ln" marker-end="url(#resp-04-02-a)"/>
 <path d="M210 132L250 168" class="ln" marker-end="url(#resp-04-02-a)"/>
 <text x="64" y="154" class="t3">Unlikely</text>
 <text x="238" y="154" class="t3">Likely</text>
 <rect x="10" y="170" width="150" height="82" rx="10" class="oksoft"/>
 <text x="85" y="192" text-anchor="middle" class="tb">D-dimer</text>
 <text x="85" y="212" text-anchor="middle" class="t3">ปกติ → R/O PE</text>
 <text x="85" y="230" text-anchor="middle" class="t3">สูง → CTPA</text>
 <rect x="175" y="170" width="170" height="82" rx="10" class="misssoft"/>
 <text x="260" y="192" text-anchor="middle" class="tb">SC LMWH</text>
 <text x="260" y="212" text-anchor="middle" class="t3">ระหว่างรอ แล้ว</text>
 <text x="260" y="230" text-anchor="middle" class="tb">CTPA confirm</text>
 <rect x="440" y="88" width="280" height="56" rx="10" class="badsoft"/>
 <text x="580" y="110" text-anchor="middle" class="tb">Bedside Echo</text>
 <text x="580" y="130" text-anchor="middle" class="t3">RV dilate · D-shaped LV · RV hypokinesia</text>
 <path d="M580 144V168" class="ln" marker-end="url(#resp-04-02-a)"/>
 <rect x="440" y="170" width="280" height="82" rx="10" class="bad"/>
 <text x="580" y="194" text-anchor="middle" class="tw">IV heparin + IV fluid &lt; 500 mL, NE</text>
 <text x="580" y="216" text-anchor="middle" class="tw">rt-PA (alteplase) ถ้าไม่มี C/I</text>
 <text x="580" y="238" text-anchor="middle" class="tw">มี C/I → embolectomy</text>
 <path d="M260 252V280" class="ln" marker-end="url(#resp-04-02-a)"/>
 <rect x="30" y="282" width="460" height="108" rx="10" class="box"/>
 <text x="260" y="304" text-anchor="middle" class="tb">PE ยืนยัน + stable</text>
 <text x="44" y="328" class="t2">• Bleeding risk ต่ำ: heparin / LMWH / fondaparinux</text>
 <text x="44" y="350" class="t2">• Bleeding risk สูง: IVC filter</text>
 <text x="44" y="372" class="t2">• ต่อด้วย DOAC / warfarin / LMWH 3–6 เดือน</text>
 <rect x="510" y="282" width="210" height="108" rx="10" class="sunk"/>
 <text x="522" y="304" class="tb">ใช้ UFH แทน LMWH</text>
 <text x="522" y="328" class="t2">• GFR &lt; 30</text>
 <text x="522" y="350" class="t2">• Severe obesity</text>
 <text x="522" y="372" class="t2">• unstable / อาจ lysis</text>
</svg>'''

S1 = sec("resp-04-01", "Pulmonary embolism: อาการและ investigation",
    "DVT → PE · เหนื่อยเฉียบพลัน ปอด clear · ECG sinus tachy, S1Q3T3 · ABG hypoxemia + resp alkalosis · CTPA confirm",
    minutes=7, source=f"{D} หน้า 92–96, 100–101, 104–105, 108–113", nl=["2.2.12", "B6.2.6(2)", "2.3.9(2)"],
    md='''
### กลไกและปัจจัยเสี่ยง
- ส่วนใหญ่มาจาก **DVT** ที่ขา → ลิ่มเลือดหลุดไปอุด pulmonary artery
- **Risk (Virchow)**: **immobilization** (เดินทางไกล, หลังผ่าตัด), hypercoagulable, **OCP**, **pregnancy**, **cancer**
- อุดหลอดเลือด → dead space + V/Q mismatch → hypoxemia → หายใจเร็ว → PaCO2 ต่ำ · RV afterload ↑ → RV failure → shock

### อาการและตรวจร่างกาย
- **เหนื่อยเฉียบพลัน**, เจ็บหน้าอกแบบ pleuritic, ไอ, hemoptysis, **syncope**
- **PR ↑, RR ↑, SpO2 ↓**, BP ↓ (PE ขนาดใหญ่)
- **Loud P2**, **ปอดฟังปกติ (clear)** — กุญแจสำคัญ: เหนื่อย + ออกซิเจนต่ำ แต่ปอด clear
- ± DVT: ขาบวมข้างเดียว กดเจ็บ

### Investigation
| การตรวจ | สิ่งที่พบ |
|---|---|
| ECG | **sinus tachycardia** (พบบ่อยสุด), RBBB, **S1Q3T3** |
| CXR | มักปกติ, pleural effusion, **Hampton hump** (wedge-shaped infarct), **Westermark sign** (avascular หลังจุดอุด) |
| ABG | **hypoxemia (PaO2 < 80)**, **acute respiratory alkalosis** (pH > 7.45, PaCO2 < 40) |
| Biomarker | troponin ↑, BNP ↑ (RV strain), **D-dimer ↑** |
| **CTPA** | **confirm Dx**: filling defect ใน pulmonary artery |
| Compression US / duplex ขา | ใช้เมื่อมีอาการ DVT: noncompressible deep vein, venous flow ผิดปกติ |
| Echo (เมื่อ unstable) | RV dilation, **D-shaped LV**, RV wall hypokinesia |

### Simple (modified) Wells score — ≥ 2 = PE likely (เกณฑ์รายข้อ — เสริม)
| ข้อ | คะแนน |
|---|---|
| อาการ/อาการแสดงของ DVT | 1 |
| PE น่าจะเป็นมากกว่าโรคอื่น | 1 |
| HR > 100 | 1 |
| Immobilization ≥ 3 วัน หรือผ่าตัดใน 4 สัปดาห์ | 1 |
| เคยเป็น DVT/PE | 1 |
| Hemoptysis | 1 |
| Active cancer | 1 |

> **D-dimer ใช้เพื่อ rule out เท่านั้น** ในกลุ่ม Wells unlikely — ถ้า PE likely ให้ไป CTPA เลย (ไม่ต้องรอ D-dimer)

> ถ้ามีอาการ DVT ชัด (ขาบวมแดงข้างเดียว) → **duplex ultrasound** ยืนยัน DVT ได้ทันที — ถ้าพบ DVT ก็รักษาด้วย anticoagulant ได้เลย เพราะการรักษาเหมือนกัน

> ABG ใน PE ต้องเป็น **pH สูง + PaCO2 ต่ำ** (หายใจเร็ว) — ถ้าเจอ PaCO2 สูงในโจทย์ PE ให้คิดว่ากำลังล้า หรือเป็น massive PE
''',
    pearls=["PE: เหนื่อยเฉียบพลัน + SpO2 ต่ำ + ปอด clear + tachycardia",
            "ECG ที่พบบ่อยสุด = sinus tachycardia · S1Q3T3 จำเพาะแต่พบน้อย",
            "ABG: hypoxemia + acute respiratory alkalosis",
            "Wells ≥ 2 = likely → CTPA · unlikely → D-dimer เพื่อ rule out",
            "มีอาการ DVT → duplex US ยืนยันได้"],
    items=[
        mcq("RESP-04-01-1", """A 42-year-old woman with breast cancer traveled 10 hours by bus for a follow-up visit. As she steps off the bus, she develops right-sided chest pain and dyspnea. HR 128/min, RR 30/min. Lungs are clear; the right leg is swollen and tender. What is the most likely diagnosis?""",
            "Pulmonary embolism",
            ["Pleurodynia", "Pneumonia", "Acute coronary syndrome", "Aortic dissection"],
            explain="""ผู้ป่วยมีปัจจัยเสี่ยงทั้งมะเร็งและการนั่งนาน มีอาการ DVT ที่ขาขวา เจ็บหน้าอก หายใจเร็ว หัวใจเต้นเร็ว และฟังปอดได้ clear เป็นภาพคลาสสิกของ PE
- Pleurodynia (Coxsackie) มีไข้และปวดกล้ามเนื้อหน้าอก ไม่มีขาบวม
- Pneumonia ควรมีไข้ เสมหะ และ crepitation
- ACS มีลักษณะเจ็บแน่นอก และไม่อธิบายขาบวมข้างเดียว
- Aortic dissection มีลักษณะเจ็บแบบฉีกทะลุหลัง ความดันสองแขนต่างกัน""",
            pearl="Risk + DVT + เหนื่อย ปอด clear = PE",
            topic="PE diagnosis", ref=[f"{D} หน้า 92, 100–101"], nl=["2.2.12"], kind="old", src=OLD),
        mcq("RESP-04-01-2", """A 65-year-old woman has had dyspnea and left leg pain for 2 days. BT 37.5°C, RR 24/min, HR 110/min, BP 110/70 mmHg, SpO2 90%. Breath sounds are normal. The left leg shows mild erythema and edema. Which is the most useful investigation?""",
            "Duplex ultrasound of the left leg",
            ["D-dimer", "Coagulogram", "Chest X-ray", "Fibrinogen level"],
            explain="""Simple Wells ≥ 2 (อาการ DVT, HR > 100, PE น่าเป็นที่สุด) จึงเป็น PE likely และมีอาการ DVT ชัด duplex US ของขาจะยืนยัน DVT ได้ทันทีและปลอดภัย ถ้าพบ DVT ก็ให้ anticoagulant ได้เลยเพราะการรักษาเหมือนกัน (ตามเฉลยในสไลด์) ส่วน CTPA เป็นการตรวจยืนยัน PE โดยตรง
- D-dimer ใช้ rule out ในกลุ่ม unlikely เท่านั้น
- Coagulogram และ fibrinogen ไม่ได้ช่วยวินิจฉัย VTE
- CXR ใน PE มักปกติ ช่วยได้แค่แยกโรคอื่น""",
            pearl="Wells likely + อาการ DVT → duplex US",
            topic="DVT duplex", ref=[f"{D} หน้า 95, 104–105"], nl=["2.3.9(2)", "2.2.12"], kind="old", src=OLD),
        mcq("RESP-04-01-3", """A 30-year-old woman taking combined oral contraceptives has had dyspnea for 2 hours. BT 37°C, RR 26/min, HR 110/min. Lungs are clear. ABG on room air: pH 7.49, PaCO2 30 mmHg, HCO3 22 mEq/L, PaO2 70 mmHg. What is the most appropriate investigation to confirm the diagnosis?""",
            "CT pulmonary angiography",
            ["Echocardiogram", "Electrocardiogram", "Chest X-ray", "Troponin level"],
            explain="""ผู้ป่วยใช้ OCP มีอาการเหนื่อยเฉียบพลัน ปอด clear และ ABG เป็น hypoxemia ร่วมกับ acute respiratory alkalosis (pH 7.49, PaCO2 30, HCO3 ยังปกติ แสดงว่าเกิดเฉียบพลัน) PE likely และ hemodynamic stable การตรวจยืนยันคือ CTPA
- Echo ใช้เมื่อ unstable และไม่สามารถไปทำ CT ได้
- ECG มักเห็นแค่ sinus tachycardia ซึ่งไม่จำเพาะ
- CXR มักปกติ ไม่ยืนยัน PE
- Troponin ใช้แบ่งความเสี่ยง ไม่ใช่การวินิจฉัย
หมายเหตุ: ข้อสอบเก่าต้นฉบับให้ pH 7.45 กับ PaCO2 45 ซึ่งขัดกับกลไกของ PE จึงปรับตัวเลขให้สอดคล้องกัน""",
            pearl="PE stable → CTPA เป็นการยืนยัน",
            topic="CTPA", ref=[f"{D} หน้า 94–95, 112–113"], nl=["2.2.12", "3.3.17"], kind="old", src=OLD),
        mcq("RESP-04-01-4", """A patient with lung cancer and brain metastasis develops sudden dyspnea on day 1 after chemotherapy. SpO2 90% on room air, HR 112/min, BP 118/72 mmHg; examination is otherwise normal. CXR is unchanged from before. What is the most useful investigation?""",
            "CT pulmonary angiography",
            ["D-dimer", "ABG", "Repeat CXR in 24 hours", "Sputum culture"],
            explain="""ผู้ป่วยมีมะเร็งระยะลุกลาม นอนโรงพยาบาลรับเคมีบำบัด แล้วเกิดเหนื่อยและ hypoxemia เฉียบพลันโดย CXR ไม่เปลี่ยนแปลง จัดเป็น PE likely จึงควรทำ CTPA
- D-dimer มักสูงอยู่แล้วในผู้ป่วยมะเร็งและผู้ป่วยใน จึงใช้ rule out ไม่ได้ และไม่ใช้ในกลุ่ม likely
- ABG ยืนยันว่ามี hypoxemia แต่ไม่ได้บอกสาเหตุ
- การรอ CXR ซ้ำทำให้วินิจฉัยช้า
- Sputum culture ไม่เกี่ยวข้อง เพราะไม่มีอาการติดเชื้อ""",
            pearl="มะเร็ง + เหนื่อยเฉียบพลัน + CXR ไม่เปลี่ยน → CTPA",
            topic="PE in cancer", ref=[f"{D} หน้า 97, 108–109"], nl=["2.2.12"], kind="old", src=OLD),
        mcq("RESP-04-01-5", """A 55-year-old man presents with sudden pleuritic chest pain and dyspnea 1 week after hip surgery. Which ECG finding is most commonly seen in acute pulmonary embolism?""",
            "Sinus tachycardia",
            ["S1Q3T3 pattern", "Complete right bundle branch block", "ST elevation in V1–V4", "Atrial fibrillation"],
            explain="""ECG ที่พบบ่อยที่สุดใน PE คือ sinus tachycardia ส่วน S1Q3T3 และ RBBB เป็นลักษณะของ RV strain ที่จำเพาะกว่าแต่พบน้อย
- S1Q3T3 เป็นข้อที่ข้อสอบชอบใช้หลอก แต่พบได้ส่วนน้อยของผู้ป่วยเท่านั้น
- RBBB พบใน PE ขนาดใหญ่
- ST elevation V1–V4 นึกถึง anterior STEMI
- AF พบได้แต่ไม่บ่อยเท่า sinus tachycardia""",
            pearl="PE ECG: sinus tachy พบบ่อยสุด · S1Q3T3 จำเพาะแต่น้อย",
            topic="ECG in PE", ref=[f"{D} หน้า 93"], nl=["2.2.12"]),
    ])

S2 = sec("resp-04-02", "Pulmonary embolism: การรักษา",
    "Unstable (SBP < 90) → IV heparin + rt-PA (C/I → embolectomy) · stable → LMWH/heparin · bleeding สูง → IVC filter · 3–6 เดือน",
    minutes=7, source=f"{D} หน้า 97–99, 102–103, 106–107, 114–115", nl=["2.2.12", "B2.4(3)", "B6.2.6(2)"],
    md='''
[[fig:resp-04-02-pe]]

### ระยะแรก (initial phase)
- **Resuscitation เมื่อ unstable (SBP < 90)**: O2, ETT เมื่อ respiratory failure, **IV fluid (< 500 mL)**, **vasopressor (NE)**
  - ให้สารน้ำน้อย เพราะ RV ที่ขยายอยู่แล้ว ถ้าได้น้ำมากจะดัน septum ไปกด LV (D-shape) → CO ลดลงอีก (เสริม)
- **Empirical anticoagulant ระหว่างรอผลตรวจ** (ถ้าสงสัยมากและไม่มีข้อห้าม)
  - Unstable: **IV heparin (UFH)** — ปรับขนาดหรือหยุดได้เร็ว และใช้ร่วมกับ lysis ได้
  - Stable: **SC LMWH** (เช่น enoxaparin)

### รักษาเฉพาะ
| สถานการณ์ | การรักษา |
|---|---|
| **Unstable (SBP < 90)** | **Thrombolysis: rt-PA (alteplase)** ถ้าไม่มีข้อห้าม · มีข้อห้าม → **embolectomy** |
| Stable + bleeding risk ต่ำ | anticoagulant: IV heparin, SC LMWH, SC fondaparinux |
| Stable + bleeding risk สูง (ใช้ anticoagulant ไม่ได้) | **IVC filter** |

### ระยะยาว
- **Anticoagulant 3–6 เดือน**: DOAC, warfarin, LMWH — ป้องกัน VTE ซ้ำ
- ต่อนานกว่านั้นในบางราย เช่น **active cancer**, ไม่มีปัจจัยกระตุ้นชัดเจน (เสริม)
- **ใช้ heparin (UFH) แทน LMWH เมื่อ GFR < 30 หรืออ้วนมาก**

> ยาที่ **ไม่ใช่** การรักษา PE: aspirin (antiplatelet ไม่พอสำหรับ venous clot), NSAIDs, warfarin เริ่มเดี่ยว ๆ (ต้อง bridge ด้วย heparin เพราะช่วงแรก warfarin ทำให้ protein C ลด → hypercoagulable — เสริม)

> rt-PA ให้เฉพาะ **unstable** — คนไข้ที่ BP ดี (stable) แม้ SpO2 ต่ำ ให้ LMWH ไม่ใช่ thrombolysis
''',
    figs=[fig("resp-04-02-pe", "แนวทาง PE ตาม hemodynamic", FIG_PE,
              "แยก stable/unstable ก่อน: unstable ให้ echo + heparin + rt-PA; stable ใช้ Wells แล้วเริ่ม LMWH ระหว่างรอ CTPA")],
    pearls=["Unstable PE (SBP < 90) → rt-PA (alteplase) · มีข้อห้าม → embolectomy",
            "Stable PE → LMWH (หรือ UFH/fondaparinux) แล้วต่อ DOAC/warfarin 3–6 เดือน",
            "Bleeding risk สูง ใช้ anticoagulant ไม่ได้ → IVC filter",
            "UFH แทน LMWH เมื่อ GFR < 30, อ้วนมาก หรืออาจต้อง lysis",
            "IV fluid ใน massive PE < 500 mL + norepinephrine"],
    items=[
        mcq("RESP-04-02-1", """A woman presents with acute dyspnea and left leg swelling. Vital signs are stable; SpO2 90%. Lungs have no adventitious sounds. PE is considered likely and CTPA is being arranged. What is the most appropriate management now?""",
            "Enoxaparin (SC LMWH)",
            ["Aspirin", "Warfarin alone", "rt-PA", "Surgical embolectomy"],
            explain="""PE likely และ hemodynamic stable ให้เริ่ม SC LMWH (enoxaparin) ทันทีระหว่างรอ CTPA ตามสไลด์
- Aspirin เป็น antiplatelet ไม่พอสำหรับรักษา venous thromboembolism
- Warfarin ออกฤทธิ์ช้า และช่วงแรกทำให้เลือดแข็งตัวง่ายขึ้น ต้องเริ่มร่วมกับ heparin
- rt-PA ใช้เฉพาะ unstable PE (SBP < 90)
- Embolectomy ใช้ใน unstable ที่มีข้อห้ามต่อ lysis""",
            pearl="PE likely + stable → LMWH ระหว่างรอ CTPA",
            topic="Stable PE", ref=[f"{D} หน้า 98, 102–103"], nl=["2.2.12", "B2.4(3)"], kind="old", src=OLD),
        mcq("RESP-04-02-2", """A 55-year-old woman with carcinoma of the pancreatic head has had dyspnea and chest discomfort for 3 hours. BP 110/65 mmHg, HR 110/min, RR 30/min, SpO2 90% on room air. Heart and lung examinations are normal; ECG shows only sinus tachycardia. What is the most appropriate management?""",
            "LMWH and arrange CTPA",
            ["Thrombolytic therapy", "Aspirin and nitroglycerin", "Observe and repeat ECG", "IV fluid loading"],
            explain="""มะเร็งตับอ่อนเป็นปัจจัยเสี่ยงสูงของ VTE ผู้ป่วยเหนื่อยเฉียบพลัน hypoxemia และปอด clear จัดเป็น PE likely ที่ยัง stable ให้ LMWH แล้วตามด้วย CTPA
- Thrombolysis ใช้เมื่อ SBP < 90 เท่านั้น
- Aspirin และ nitroglycerin เป็นการรักษา ACS ซึ่ง ECG ไม่สนับสนุน
- การสังเกตอาการและทำ ECG ซ้ำทำให้การรักษาช้า
- IV fluid loading อาจทำให้ RV ล้มเหลวมากขึ้น""",
            pearl="มะเร็ง + เหนื่อยเฉียบพลัน stable → LMWH + CTPA",
            topic="PE in cancer tx", ref=[f"{D} หน้า 106–107"], nl=["2.2.12"], kind="old", src=OLD),
        mcq("RESP-04-02-3", """A 60-year-old man with confirmed acute pulmonary embolism becomes hypotensive: BP 78/50 mmHg despite 500 mL of saline, HR 130/min. Bedside echocardiography shows a dilated, hypokinetic RV with a D-shaped LV. He has no bleeding history or recent surgery. What is the most appropriate treatment?""",
            "IV alteplase (rt-PA) with IV unfractionated heparin and norepinephrine",
            ["SC enoxaparin only", "Further IV fluid boluses of 2 L", "IVC filter insertion", "Oral rivaroxaban"],
            explain="""PE ที่มี SBP < 90 และ RV dysfunction คือ high-risk (massive) PE รักษาด้วย thrombolysis (rt-PA) เมื่อไม่มีข้อห้าม ร่วมกับ IV heparin และ vasopressor (NE)
- LMWH อย่างเดียวไม่เพียงพอในภาวะ shock
- การให้สารน้ำปริมาณมากทำให้ RV ขยายและกดทับ LV มากขึ้น สไลด์ให้ < 500 mL
- IVC filter ใช้เมื่อใช้ anticoagulant ไม่ได้ ไม่ได้ช่วยละลายลิ่มเลือดที่อุดอยู่
- Rivaroxaban เป็นยาระยะยาวใน PE ที่ stable""",
            pearl="PE + SBP < 90 → rt-PA + UFH + NE",
            topic="Massive PE", ref=[f"{D} หน้า 97–99"], nl=["2.2.12", "B2.4(3)"]),
        mcq("RESP-04-02-4", """A woman developed dyspnea 5 days after knee surgery and also has leg swelling. BT 36.4°C, BP 120/60 mmHg, RR 22/min, SpO2 90%. ECG shows normal sinus rhythm; CXR is normal. What is the most appropriate management?""",
            "Heparin (LMWH or unfractionated) anticoagulation",
            ["rt-PA", "NSAIDs", "Aspirin", "Observation only"],
            explain="""หลังผ่าตัดเข่า มีขาบวม เหนื่อย SpO2 ต่ำ และ CXR ปกติ นึกถึง PE โดย hemodynamic stable การรักษาคือ anticoagulant ด้วย LMWH หรือ heparin
- rt-PA ใช้เมื่อ unstable และผู้ป่วยเพิ่งผ่าตัดมา จึงมีความเสี่ยงเลือดออกสูงด้วย
- NSAIDs ไม่รักษาลิ่มเลือด
- Aspirin ไม่พอสำหรับ VTE
- การสังเกตอาการเฉย ๆ เสี่ยงต่อ PE ซ้ำที่รุนแรงขึ้น""",
            pearl="Post-op + DVT + เหนื่อย stable → heparin/LMWH",
            topic="Post-op PE", ref=[f"{D} หน้า 114–115"], nl=["2.2.12"], kind="old", src=OLD),
        mcq("RESP-04-02-5", """A 70-year-old man has an acute proximal DVT and a confirmed stable PE. Two days ago he had a hemorrhagic stroke. What is the most appropriate management to prevent further embolism?""",
            "Inferior vena cava filter placement",
            ["Full-dose LMWH", "Systemic thrombolysis", "Warfarin with INR target 2–3", "Dual antiplatelet therapy"],
            explain="""PE ที่ stable แต่มีความเสี่ยงเลือดออกสูงมาก (เพิ่งมี hemorrhagic stroke) ใช้ anticoagulant ไม่ได้ สไลด์ให้ใส่ IVC filter เพื่อดักลิ่มเลือดจากขา
- LMWH และ warfarin มีข้อห้ามเพราะเลือดออกในสมอง
- Thrombolysis มีข้อห้ามเด็ดขาด
- Antiplatelet ไม่ได้ป้องกัน VTE และยังเพิ่มความเสี่ยงเลือดออก""",
            pearl="VTE + ห้ามใช้ anticoagulant → IVC filter",
            topic="IVC filter", ref=[f"{D} หน้า 99"], nl=["2.2.12"]),
    ])

LECTURE = lecture("04", "Pulmonary embolism",
    subtitle="clinical · Wells score · CTPA · thrombolysis vs anticoagulation",
    objectives=["จำลักษณะทางคลินิก ECG CXR และ ABG ของ PE ได้",
                "ใช้ simple Wells score เลือกระหว่าง D-dimer และ CTPA ได้",
                "เลือกการรักษาตาม hemodynamic: rt-PA, heparin/LMWH, IVC filter ได้",
                "บอกระยะเวลา anticoagulant และข้อบ่งชี้ใช้ UFH แทน LMWH ได้"],
    sections=[S1, S2])
