from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-GI"
OLD = "ตัวอย่างข้อสอบในสไลด์ NL2-GI"

FLOW = '''<svg viewBox="0 0 720 400">
 <defs><marker id="gi-02-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="20" y="10" width="220" height="48" rx="9" class="box"/>
 <text x="130" y="31" text-anchor="middle" class="tb">Hematemesis / Melena</text>
 <text x="130" y="49" text-anchor="middle" class="t3">ชัดว่าเป็น UGIB</text>
 <rect x="480" y="10" width="220" height="48" rx="9" class="box"/>
 <text x="590" y="31" text-anchor="middle" class="tb">Acute severe hematochezia</text>
 <text x="590" y="49" text-anchor="middle" class="t3">ยังไม่รู้ว่าบนหรือล่าง</text>
 <path d="M590 58V84" class="ln" marker-end="url(#gi-02-02-a)"/>
 <rect x="510" y="86" width="160" height="36" rx="9" class="misssoft"/>
 <text x="590" y="109" text-anchor="middle" class="tb">NG lavage</text>
 <text x="430" y="98" text-anchor="middle" class="t3">R/O massive UGIB</text>
 <path d="M510 104H352" class="ln" marker-end="url(#gi-02-02-a)"/>
 <path d="M130 58V104H248" class="ln" marker-end="url(#gi-02-02-a)"/>
 <rect x="250" y="80" width="100" height="48" rx="9" class="acsoft"/>
 <text x="300" y="100" text-anchor="middle" class="tb">ABC</text>
 <text x="300" y="118" text-anchor="middle" class="t3">+ risk (GBS)</text>
 <path d="M300 128V150M140 150H520M140 150V176M520 150V176" class="ln"/>
 <path d="M140 166V178" class="ln" marker-end="url(#gi-02-02-a)"/><path d="M520 166V178" class="ln" marker-end="url(#gi-02-02-a)"/>
 <rect x="40" y="180" width="200" height="50" rx="9" class="oksoft"/>
 <text x="140" y="201" text-anchor="middle" class="tb">Low risk</text>
 <text x="140" y="220" text-anchor="middle">GBS = 0</text>
 <rect x="420" y="180" width="200" height="50" rx="9" class="badsoft"/>
 <text x="520" y="201" text-anchor="middle" class="tb">High risk</text>
 <text x="520" y="220" text-anchor="middle">GBS ≥ 1</text>
 <path d="M140 230V318" class="ln" marker-end="url(#gi-02-02-a)"/>
 <path d="M520 230V246M420 246H620M420 246V262M620 246V262" class="ln"/>
 <path d="M420 258V264" class="ln" marker-end="url(#gi-02-02-a)"/><path d="M620 258V264" class="ln" marker-end="url(#gi-02-02-a)"/>
 <rect x="335" y="266" width="170" height="54" rx="9" class="c1soft"/>
 <text x="420" y="287" text-anchor="middle" class="tb">Non-variceal</text>
 <text x="420" y="307" text-anchor="middle">IV PPI high dose</text>
 <rect x="535" y="266" width="170" height="54" rx="9" class="c2soft"/>
 <text x="620" y="287" text-anchor="middle" class="tb">Variceal</text>
 <text x="620" y="307" text-anchor="middle">Vasoactive + ATB</text>
 <path d="M420 320V344" class="ln" marker-end="url(#gi-02-02-a)"/><path d="M620 320V344" class="ln" marker-end="url(#gi-02-02-a)"/>
 <rect x="335" y="348" width="370" height="40" rx="9" class="bad"/>
 <text x="520" y="373" text-anchor="middle" class="tw">Admit + EGD</text>
 <rect x="40" y="320" width="200" height="68" rx="9" class="ok"/>
 <text x="140" y="346" text-anchor="middle" class="tw">PPI +</text>
 <text x="140" y="368" text-anchor="middle" class="tw">elective EGD (OPD)</text>
</svg>'''

VAR = '''<svg viewBox="0 0 720 300">
 <defs><marker id="gi-02-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <path d="M30 150H700" class="lna" marker-end="url(#gi-02-03-a)"/>
 <text x="690" y="172" text-anchor="end" class="t3">เวลา</text>
 <circle cx="80" cy="150" r="7" class="ac"/>
 <circle cx="270" cy="150" r="7" class="ac"/>
 <circle cx="460" cy="150" r="7" class="ac"/>
 <circle cx="630" cy="150" r="7" class="ac"/>
 <text x="80" y="176" text-anchor="middle" class="ta">ER (0 ชม.)</text>
 <text x="270" y="176" text-anchor="middle" class="ta">EGD ≤ 12 ชม.</text>
 <text x="460" y="176" text-anchor="middle" class="ta">วันที่ 3–5</text>
 <text x="630" y="176" text-anchor="middle" class="ta">กลับบ้าน</text>
 <rect x="10" y="10" width="160" height="122" rx="9" class="acsoft"/>
 <text x="90" y="32" text-anchor="middle" class="tb">Resuscitation</text>
 <text x="90" y="52" text-anchor="middle" class="t3">ABC · ETT ถ้า AOC</text>
 <text x="90" y="70" text-anchor="middle" class="t3">PRC keep Hb ≥ 7</text>
 <text x="90" y="88" text-anchor="middle" class="t3">Somatostatin/</text>
 <text x="90" y="104" text-anchor="middle" class="t3">octreotide/terlipressin</text>
 <text x="90" y="122" text-anchor="middle" class="t3">Ceftriaxone 1 g OD</text>
 <rect x="190" y="10" width="160" height="122" rx="9" class="c1soft"/>
 <text x="270" y="32" text-anchor="middle" class="tb">EGD</text>
 <text x="270" y="54" text-anchor="middle" class="t3">EVL (หรือ sclerotherapy)</text>
 <text x="270" y="74" text-anchor="middle" class="t3">Gastric varix → ES</text>
 <text x="270" y="98" text-anchor="middle" class="t3">ยังเลือดออกมาก →</text>
 <text x="270" y="116" text-anchor="middle" class="t3">SB tube เป็นสะพาน</text>
 <rect x="380" y="10" width="160" height="122" rx="9" class="c2soft"/>
 <text x="460" y="32" text-anchor="middle" class="tb">หลังส่อง</text>
 <text x="460" y="54" text-anchor="middle" class="t3">Vasoactive ต่อ 3–5 วัน</text>
 <text x="460" y="74" text-anchor="middle" class="t3">ATB ครบ 7 วัน</text>
 <text x="460" y="98" text-anchor="middle" class="t3">EGD failed →</text>
 <text x="460" y="116" text-anchor="middle" class="t3">TIPS</text>
 <rect x="560" y="10" width="150" height="122" rx="9" class="oksoft"/>
 <text x="635" y="32" text-anchor="middle" class="tb">Secondary</text>
 <text x="635" y="50" text-anchor="middle" class="tb">prophylaxis</text>
 <text x="635" y="76" text-anchor="middle">Propranolol</text>
 <text x="635" y="96" text-anchor="middle">+ EVL ซ้ำ</text>
 <text x="635" y="118" text-anchor="middle" class="t3">จน varix หมด</text>
 <rect x="10" y="200" width="700" height="88" rx="9" class="sunk"/>
 <text x="24" y="224" class="tb">ขนาดยาตามสไลด์</text>
 <text x="24" y="246">Somatostatin 250 mcg IV bolus → 250 mcg/hr · Octreotide 50 mcg IV bolus → 50 mcg/hr</text>
 <text x="24" y="266">Terlipressin 1 mg IV q 8 hr (สไลด์) · Ceftriaxone 1 g IV OD 7 วัน หรือ Norfloxacin 400 mg bid 7 วัน</text>
 <text x="24" y="282" class="t3">EGD ≤ 12 ชม. และ terlipressin 2 mg q 4 hr = แนวทางสากล (เสริม)</text>
</svg>'''

LECTURE = lecture("02", "Upper GI bleeding",
    subtitle="สาเหตุ · risk score · resuscitation · variceal vs non-variceal",
    objectives=[
        "แยก variceal กับ non-variceal bleeding จากประวัติและตรวจร่างกายได้",
        "ใช้ Glasgow-Blatchford score ตัดสินใจ admit/EGD และรู้ว่า Rockall ใช้ประเมิน mortality",
        "ทำ initial resuscitation ได้ถูกลำดับ: ABC, ETT, PRC/FFP/platelet ตามเกณฑ์",
        "สั่ง high-dose PPI, vasoactive agents และ antibiotic prophylaxis ได้ถูกขนาด",
        "วางแผน post-endoscopic care และ secondary prophylaxis ของ variceal bleeding ได้",
    ],
    sections=[
    sec("gi-02-01", "UGIB: สาเหตุ ลักษณะทางคลินิก และ risk score",
        "PU · varices · gastritis · MW tear — ใช้ clue จากประวัติ; GBS = 0 กลับบ้านได้, Rockall ดู mortality", minutes=6,
        source=f"{D} หน้า 25–30, 47–48", nl=["2.3.11-3(6)", "2.1.16", "2.1.20"],
        md='''
### นิยามและอาการ
UGIB = เลือดออกเหนือ ligament of Treitz อาการ: **hematemesis** (เลือดสด) หรือ **coffee-ground**, **melena**, บางรายเลือดออกเร็วมากเป็น hematochezia; ร่วมกับ ↓BP ↑PR และ anemia

### สาเหตุ
Peptic ulcer · Esophageal varices · Erosive gastritis/duodenitis · Esophagitis · Mallory-Weiss tear · Malignancy

| สาเหตุ | Clue จากประวัติ |
|---|---|
| Mallory-Weiss tear | **อาเจียน/ขย้อนก่อน** แล้วจึงมีเลือด |
| Esophageal ulcer | GERD, odynophagia |
| Peptic ulcer | ปวดท้อง, NSAIDs, ASA |
| Stress-related gastritis | ผู้ป่วย ICU |
| Varices | CLD, HBV, alcohol, hematemesis, **signs of portal HT** |
| Malignancy | cachexia, wt loss, เบื่ออาหาร |
| Aortoenteric fistula | ประวัติ aortic aneurysm/ผ่าตัด graft |

### Variceal vs non-variceal
| | Variceal | Non-variceal |
|---|---|---|
| ปวด | ไม่ปวด | ปวดหรือไม่ปวด |
| ลักษณะเลือด | มักเป็น hematemesis | hematemesis, coffee ground, melena |
| V/S | มัก V/S เปลี่ยน (> 90%) | แล้วแต่ราย |
| Signs portal HT/CLD | **มี** | ไม่มี |

> โจทย์ที่ให้ icteric sclera, parotid gland enlargement, shifting dullness, spider nevi, splenomegaly → คิดถึง **variceal bleeding** ก่อน

### Risk assessment
ใช้ **Rockall score, Glasgow-Blatchford score (GBS), AIMS65** เพื่อตัดสินใจ admission และทำนาย rebleeding/mortality

**Rockall score — ประเมิน mortality** (ต้องรู้ผล endoscopy)
| ตัวแปร | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| อายุ | < 60 | 60–79 | ≥ 80 | |
| Shock | SBP > 100, PR < 100 | PR > 100 | SBP < 100 | |
| Comorbidity | ไม่มี | | HF, IHD, major | renal/liver failure, metastatic CA |
| Diagnosis | MW tear, ไม่พบรอยโรค | อื่น ๆ | upper GI malignancy | |
| Major SRH | ไม่มี/dark spot | | เลือดในทางเดินอาหาร, adherent clot, visible/spurting vessel | |

**Glasgow-Blatchford score — ประเมินว่าต้อง admit/EGD ไหม** (ใช้ได้ก่อนส่อง)
- ตัวแปร: BUN, Hb (แยกชาย/หญิง), SBP, pulse ≥ 100, melena, syncope, hepatic disease, cardiac failure
- **Score = 0** → ไม่ต้อง admit เลือดมีโอกาสหยุดเอง นัด **elective EGD**
- **Score ≥ 1** → ควร **admit และ EGD**

> แนวทางสากลบางฉบับยอมให้ GBS ≤ 1 รักษาแบบผู้ป่วยนอก (เสริม) — ข้อสอบตามสไลด์ใช้ 0
''',
        pearls=[
            "อาเจียนหลายครั้งแล้วค่อยมีเลือด = Mallory-Weiss tear",
            "Hematemesis + signs of CLD/portal HT = variceal bleeding",
            "GBS = 0 → elective EGD ไม่ต้อง admit; GBS ≥ 1 → admit + EGD",
            "Rockall = ทำนาย mortality (ต้องใช้ผลส่อง), GBS = ทำนายความจำเป็นต้อง intervention",
        ],
        items=[
            mcq("GI-02-01-1", "A 45-year-old woman presents with hematemesis of about 100 mL in the past hour. Examination shows mildly pale conjunctivae, icteric sclerae, bilateral parotid gland enlargement and a distended abdomen with shifting dullness. What is the most likely cause of her bleeding?",
                "Variceal bleeding", ["Esophagitis", "Mallory-Weiss tear", "Bleeding peptic ulcer", "Hemorrhagic gastritis"],
                explain='''ผู้ป่วยมี **signs of chronic liver disease และ portal hypertension** (icteric sclera, parotid enlargement จาก alcohol, ascites) ร่วมกับ hematemesis → variceal bleeding
- Esophagitis จะมีประวัติ GERD/odynophagia และเลือดออกไม่มาก
- Mallory-Weiss tear ต้องมีอาเจียน/ขย้อนนำมาก่อน
- Bleeding peptic ulcer พบบ่อยที่สุดโดยรวม แต่โจทย์ให้ clue ตับแข็งชัดเจน
- Hemorrhagic gastritis พบใน ICU/alcohol binge/NSAIDs ไม่ได้อธิบาย ascites''',
                pearl="UGIB + parotid/jaundice/ascites → varices", topic="Variceal vs non-variceal",
                ref=[f"{D} หน้า 47–48"], nl=["2.3.11-3(6)", "B8.2.2-3(7)"], kind="old", src=OLD),
            mcq("GI-02-01-2", "A 28-year-old man drank heavily at a party, vomited forcefully several times, and then vomited bright red blood about 50 mL. Pulse is 88/min and BP 124/76 mmHg. Abdomen is soft. What is the most likely diagnosis?",
                "Mallory-Weiss tear", ["Esophageal varices", "Boerhaave syndrome", "Aortoenteric fistula", "Gastric carcinoma"],
                explain='''Clue สำคัญคือ **อาเจียน/ขย้อนรุนแรงก่อน** แล้วจึงมีเลือดออกปริมาณไม่มาก V/S stable → Mallory-Weiss tear (mucosal tear บริเวณ GE junction) ส่วนใหญ่หยุดเอง รักษาด้วย PPI
- Esophageal varices ต้องมีพื้นตับแข็ง/portal HT และมักเลือดออกมาก
- Boerhaave syndrome เป็นการฉีกขาดทะลุทุกชั้น มีเจ็บหน้าอกรุนแรง subcutaneous emphysema ช็อก มากกว่าการอาเจียนเป็นเลือด
- Aortoenteric fistula ต้องมีประวัติผ่าตัด aortic graft
- Gastric carcinoma จะมีน้ำหนักลด เบื่ออาหาร อาการเรื้อรัง''',
                pearl="อาเจียนก่อน แล้วเลือดตาม = Mallory-Weiss tear → PPI", topic="Mallory-Weiss tear",
                ref=[f"{D} หน้า 26, 35"], nl=["2.3.11-3(6)", "2.1.16"]),
            mcq("GI-02-01-3", "A 30-year-old man vomited a small amount of coffee-ground material once this morning after taking ibuprofen for 3 days. He has no melena or syncope and is now asymptomatic. Pulse 76/min, BP 128/80 mmHg, Hb 14.5 g/dL, BUN 12 mg/dL. He has no liver or heart disease. Which is the most appropriate management?",
                "Discharge on oral PPI with elective outpatient EGD",
                ["Admit to ICU for urgent EGD within 12 hours", "Transfuse 2 units of PRC", "Start IV octreotide infusion", "Insert a Sengstaken-Blakemore tube"],
                explain='''คำนวณ **Glasgow-Blatchford score**: BUN ปกติ, Hb ชาย ≥ 13, SBP > 110, ชีพจร < 100, ไม่มี melena/syncope/โรคตับ/โรคหัวใจ → **GBS = 0** (hematemesis เองไม่มีคะแนนใน GBS) ตามสไลด์ไม่ต้อง admit เลือดมีโอกาสหยุดเอง ให้ PPI แล้วนัด **elective EGD**
- ICU และ urgent EGD สงวนไว้สำหรับ high risk/V/S ไม่คงที่
- PRC ให้เมื่อ Hb < 7 g/dL หรือ V/S unstable
- Octreotide ใช้เมื่อสงสัย variceal bleeding (มีโรคตับ/portal HT)
- SB tube ใช้เป็นสะพานใน variceal bleeding ที่ยังออกมากหลังให้ vasoactive''',
                pearl="GBS = 0 → PPI + elective EGD แบบ OPD ไม่ต้อง admit", topic="Glasgow-Blatchford score",
                ref=[f"{D} หน้า 29, 34"], nl=["2.3.11-3(6)"]),
        ]),

    sec("gi-02-02", "UGIB: initial management & transfusion",
        "ABC → ETT ถ้า AOC/hematemesis มาก · Hb ≥ 7 · INR < 2.5 · Plt ≥ 50,000 · IV PPI 80 mg → 8 mg/hr", minutes=7,
        source=f"{D} หน้า 31–34, 37–46", nl=["2.3.11-3(6)", "2.2.7", "B8.4(2)"],
        md='''
### ลำดับการดูแลเบื้องต้น
1. **Initial resuscitation (ABC) ก่อนเสมอ**
   - **ETT** เพื่อ protect airway ในผู้ป่วย **alteration of consciousness** หรือ **severe hematemesis** เพื่อป้องกัน aspiration
   - IV LRS/NSS loading
2. **Blood transfusion**
   - PRC: keep **Hb ≥ 7 g/dL** (≥ 8 g/dL ถ้ามี CVD); V/S unstable → ให้ PRC ได้เลย
   - เลือดออกมากและรอ crossmatch ไม่ได้ → **PRC group O** (uncrossmatched)
   - Correct coagulopathy: FFP, platelet concentrate — keep **INR < 2.5, Plt ≥ 50,000**
3. **NG tube** ใส่เฉพาะเมื่อ **ประวัติ UGIB ไม่ชัด** เช่น acute severe hematochezia → NG lavage เพื่อ R/O massive UGIB
4. แยก variceal/non-variceal แล้วเริ่มยา

### เกณฑ์ transfusion (สรุปจากเฉลยในสไลด์)
| สถานการณ์ | ให้อะไร |
|---|---|
| V/S unstable | PRC เลย |
| V/S stable, Hb < 7 g/dL | PRC |
| INR > 2.5 | FFP |
| Plt < 50,000 | Platelet |

> Hct 27% (Hb ~9), Plt 85,000, INR 1.7, V/S stable → **ไม่ต้อง transfuse อะไร** — ข้อสอบชอบหลอกด้วยค่าที่ผิดปกติเล็กน้อย

### ยาเริ่มต้น
**Non-variceal**: high-dose PPI
- Omeprazole / Pantoprazole / Esomeprazole **80 mg IV bolus แล้ว 8 mg/hr**

**Variceal**: vasoactive agents + antibiotic prophylaxis (รายละเอียดหัวข้อถัดไป)

[[fig:gi-02-02-flow]]

> ทราเน็กซามิก (tranexamic acid) ไม่ใช่การรักษามาตรฐานของ UGIB (HALT-IT trial ไม่ลด mortality) (เสริม)
''',
        figs=[fig("gi-02-02-flow", "แนวทาง UGIB ตั้งแต่ ER ถึง EGD", FLOW,
                  "Hematochezia รุนแรงที่ยังไม่รู้ตำแหน่งให้ NG lavage ก่อน แล้วทุกรายประเมิน GBS เพื่อแยก OPD กับ admit")],
        pearls=[
            "UGIB ทุกข้อ: ABC ก่อน — ซึม/เลือดเต็มปาก → ETT",
            "PRC keep Hb ≥ 7 (≥ 8 ถ้ามีโรคหัวใจ) · FFP เมื่อ INR > 2.5 · Plt เมื่อ < 50,000",
            "Massive bleeding รอ crossmatch ไม่ได้ → PRC group O",
            "Non-variceal: PPI 80 mg IV bolus → 8 mg/hr",
            "NG lavage ใช้เฉพาะ acute severe hematochezia เพื่อ R/O UGIB",
        ],
        items=[
            mcq("GI-02-02-1", "A 59-year-old man with alcoholic cirrhosis presents with hematemesis. Pulse 120/min, BP 90/60 mmHg. He is drowsy and his oral cavity is full of blood. Besides IV fluid resuscitation, what is the most appropriate next step?",
                "Endotracheal intubation", ["IV proton pump inhibitor", "Esophagogastroduodenoscopy", "Sengstaken-Blakemore tube", "Nasogastric lavage"],
                explain='''ABC มาก่อนเสมอ — ผู้ป่วย **ซึม (AOC) และมีเลือดเต็มปาก** เสี่ยง aspiration สูง ต้อง **ใส่ ETT เพื่อ protect airway** ก่อนทำอย่างอื่น
- IV PPI และ vasoactive เป็นยา แต่ไม่ช่วยทางหายใจที่กำลังจะอุดตัน
- EGD ต้องทำหลัง airway ปลอดภัยแล้ว
- SB tube ใส่ได้หลังใส่ ETT แล้วเท่านั้น และใช้เมื่อยาไม่ได้ผล
- NG lavage ไม่จำเป็นเพราะชัดว่าเป็น UGIB และกระตุ้นอาเจียนเพิ่ม aspiration''',
                pearl="UGIB + AOC/เลือดเต็มปาก → ETT ก่อน", topic="Airway in UGIB",
                ref=[f"{D} หน้า 31, 37–38"], nl=["2.3.11-3(6)", "2.1.16"], kind="old", src=OLD),
            mcq("GI-02-02-2", "A 40-year-old man with alcoholic cirrhosis vomited about 2 liters of blood 1 hour ago. Temperature 36.8 °C, pulse 100/min, BP 80/40 mmHg. Crossmatched blood is not yet available. Which is the most appropriate management during resuscitation?",
                "Transfuse uncrossmatched group O packed red cells", ["Vitamin K IV", "Norepinephrine infusion", "Wait for crossmatched PRC", "Fresh frozen plasma alone"],
                explain='''เลือดออก 2 ลิตรร่วมกับ hemorrhagic shock (BP 80/40) ต้องทดแทน oxygen-carrying capacity ทันที เมื่อยังไม่มีเลือดที่ crossmatch ให้ใช้ **PRC group O** (uncrossmatched)
- Vitamin K ไม่ได้ผลในตับแข็งที่การสร้าง clotting factor บกพร่องและออกฤทธิ์ช้า
- Norepinephrine ไม่ใช่การรักษา hypovolemic shock จากเลือดออก ต้องเติม volume/เลือด
- การรอ crossmatch ทำให้ช็อกนานขึ้น
- FFP อย่างเดียวไม่ได้เพิ่ม Hb และให้เมื่อ INR > 2.5''',
                pearl="Massive UGIB + shock รอเลือดไม่ได้ → PRC group O", topic="Emergency transfusion",
                ref=[f"{D} หน้า 39–40"], nl=["2.3.11-3(6)", "2.2.7"], kind="old", src=OLD),
            mcq("GI-02-02-3", "A 60-year-old man is brought in near-comatose with passage of large amounts of blood per rectum for 1 day. Capillary glucose 105 mg/dL, Hb 8 g/dL. After IV fluid resuscitation and airway protection, what is the most appropriate next step?",
                "Insert a nasogastric tube for lavage", ["Colonoscopy", "CT angiography of the abdomen", "Tagged red blood cell scan", "Sigmoidoscopy"],
                explain='''**Acute severe hematochezia** ที่ hemodynamic ไม่ดี อาจมาจาก **massive UGIB** ได้ (~10–15%) ตามสไลด์ให้ใส่ **NG lavage เพื่อ R/O UGIB** ก่อนส่องลำไส้ใหญ่ ถ้าได้เลือดหรือ coffee-ground → EGD
- Colonoscopy/sigmoidoscopy ต้องเตรียมลำไส้และจะพลาดถ้าเป็น UGIB
- CT angiography/tagged RBC scan ใช้หลังแยก UGIB แล้วและยังหาตำแหน่งไม่ได้
> แนวทางปัจจุบันหลายฉบับแนะนำส่อง EGD โดยตรงใน hematochezia ที่ช็อก (เสริม) แต่ในตัวเลือกนี้ NG lavage คือคำตอบตามสไลด์''',
                pearl="Acute severe hematochezia → NG lavage R/O massive UGIB", topic="NG lavage indication",
                ref=[f"{D} หน้า 31, 41–42"], nl=["2.3.11-3(6)", "2.1.20"], kind="old", src=OLD),
            mcq("GI-02-02-4", "A 50-year-old man with alcoholic cirrhosis presents with hematemesis. BP 100/60 mmHg, pulse 102/min. He has moderate pallor, mild jaundice, minimal ascites, and a spleen palpable 3 cm below the left costal margin. Hct 27%, platelets 85,000/mm³, aPTT 42 s, INR 1.7. EGD is scheduled. What is the most appropriate transfusion strategy?",
                "No transfusion is required at this time", ["PRC transfusion", "FFP transfusion", "Platelet transfusion", "PRC and FFP transfusion"],
                explain='''V/S stable พอ, Hct 27% (Hb ~9 g/dL > 7), Plt 85,000 (> 50,000), INR 1.7 (< 2.5) → **ยังไม่ถึงเกณฑ์ transfusion ใด ๆ**
- PRC ให้เมื่อ Hb < 7 หรือ V/S unstable — การให้เลือดเกินใน variceal bleeding เพิ่ม portal pressure และ rebleeding
- FFP ให้เมื่อ INR > 2.5
- Platelet ให้เมื่อ < 50,000
- การให้ PRC + FFP ร่วมกันเกินความจำเป็นทั้งสองอย่าง''',
                pearl="Hb ≥ 7, INR < 2.5, Plt ≥ 50,000, V/S stable → ไม่ต้อง transfuse", topic="Restrictive transfusion",
                ref=[f"{D} หน้า 43–44"], nl=["2.3.11-3(6)"], kind="old", src=OLD),
            mcq("GI-02-02-5", "A man with alcoholic cirrhosis has hematemesis and hematochezia for 2 days. He has pale conjunctivae, icteric sclerae, spider nevi and shifting dullness. Hct 24%, platelets 95,000/mm³, PT 20 s (control 12 s), aPTT 36 s, TT 21 s. Which is the most appropriate blood product to correct his coagulopathy?",
                "Fresh frozen plasma", ["Recombinant activated factor VII", "Vitamin K", "Factor VIII concentrate", "Platelet concentrate"],
                explain='''PT ยาวจาก **ตับสร้าง clotting factor ไม่ได้** (factor VII ครึ่งชีวิตสั้นที่สุดจึงยืด PT ก่อน) ในผู้ป่วยที่กำลังเลือดออก คำตอบตามสไลด์คือ **FFP** ซึ่งมี clotting factor ครบ
- Recombinant FVIIa แพงมากและไม่ลด mortality ใน variceal bleeding
- Vitamin K ไม่ได้ผลเมื่อเซลล์ตับเสีย (ต่างจาก vitamin K deficiency)
- Factor VIII ไม่ได้ลดลงในตับแข็ง (สร้างจาก endothelium) และ aPTT ปกติ
- Platelet 95,000 ยังสูงกว่าเกณฑ์ 50,000
> เกณฑ์ในสไลด์คือให้ FFP เมื่อ INR > 2.5 และแนวทางปัจจุบัน (Baveno VII) ไม่แนะนำ FFP เพื่อแก้ INR ใน variceal bleeding — ข้อนี้ถามว่า "ถ้าจะแก้ coagulopathy ใช้อะไร" จึงตอบ FFP''',
                pearl="Coagulopathy จากตับแข็ง + กำลังเลือดออก → FFP (vitamin K ไม่ช่วย)", topic="Coagulopathy in cirrhosis",
                ref=[f"{D} หน้า 45–46"], nl=["2.3.11-3(6)", "2.3.3(1)"], kind="old", src=OLD),
        ]),

    sec("gi-02-03", "Variceal bleeding & specific/post-endoscopic treatment",
        "Vasoactive + ceftriaxone ก่อน EGD → EVL → vasoactive 3–5 วัน → propranolol + EVL", minutes=7,
        source=f"{D} หน้า 33, 35–36, 49–54", nl=["B8.2.2-3(7)", "B8.4(2)", "2.3.11-3(6)"],
        md='''
### ก่อนส่อง (initial)
**Vasoactive agents** — ลด splanchnic blood flow → ลด portal pressure ให้ทันทีที่สงสัย variceal bleeding ไม่ต้องรอ EGD
| ยา | ขนาด (ตามสไลด์) |
|---|---|
| Somatostatin | 250 mcg IV bolus → 250 mcg/hr |
| Octreotide | 50 mcg IV bolus → 50 mcg/hr |
| Terlipressin | 1 mg IV q 8 hr |

> Terlipressin ในแนวทางสากลใช้ 2 mg IV q 4 hr ช่วง 48 ชม.แรก แล้วลดเป็น 1 mg q 4 hr (เสริม) — ถ้าข้อสอบถามขนาดให้ยึดตามตัวเลือกที่มี

**Antibiotic prophylaxis** (ป้องกัน SBP/infection ใน cirrhosis และลด rebleeding/mortality)
- **Ceftriaxone 1 g IV OD 7 วัน** หรือ Norfloxacin 400 mg PO bid 7 วัน

**Sengstaken-Blakemore tube** — ใช้เมื่อได้ vasoactive 1–2 ชม.แล้วยังเลือดออกมากระหว่างรอ EGD (เป็นสะพาน ต้องใส่ ETT ก่อน)

[[fig:gi-02-03-var]]

### Specific treatment (EGD เพื่อวินิจฉัยและรักษา)
| รอยโรค | การรักษา |
|---|---|
| Peptic ulcer | Endoscopic hemostasis + PPI + **H. pylori testing** |
| Mallory-Weiss tear | PPI |
| Esophageal varices | Vasoactive + **EVL** (หรือ endoscopic sclerotherapy, ES); EGD ล้มเหลว → **TIPS** |
| Gastric varices | Vasoactive + ES (glue injection) |

### Post-endoscopic management
- **Non-variceal**: IV/oral PPI ต่อจนครบ **72 ชม.**; PU ที่ H. pylori positive → eradication therapy
- **Variceal**: vasoactive ต่อจนครบ **3–5 วัน**
- **Secondary prophylaxis** (ทุกรายที่เคย bleed): **Propranolol + EVL** ซ้ำจน varices หมด

> ข้อสอบ "EGD พบ varix หยุดเลือดแล้ว ควรให้อะไรต่อ" → **non-selective beta-blocker (propranolol)** ร่วมกับ EVL — ห้ามสับสนกับ PPI ที่ใช้ใน non-variceal
''',
        figs=[fig("gi-02-03-var", "เส้นเวลาการดูแล acute variceal bleeding", VAR,
                  "ไล่จากซ้ายไปขวา: ยาเริ่มที่ ER ก่อนส่อง, EVL ที่ EGD, ให้ยาต่อหลังส่อง แล้วจบด้วย secondary prophylaxis")],
        pearls=[
            "สงสัย variceal bleed → เริ่ม somatostatin/octreotide/terlipressin ทันทีก่อน EGD",
            "Cirrhosis + UGIB → ceftriaxone 1 g IV OD 7 วัน",
            "EVL คือ endoscopic therapy หลักของ esophageal varices; ล้มเหลว → TIPS",
            "Secondary prophylaxis = propranolol + EVL",
            "Non-variceal หลังส่อง: PPI ครบ 72 ชม. + ตรวจ H. pylori",
        ],
        items=[
            mcq("GI-02-03-1", "A 50-year-old man with alcoholic cirrhosis presents with hematemesis. He has splenomegaly. After IV resuscitation and blood transfusion his vital signs are stable. What is the most appropriate next step in management?",
                "IV somatostatin infusion", ["IV proton pump inhibitor", "Esophagogastroduodenoscopy immediately without drug therapy", "Sengstaken-Blakemore tube", "Endotracheal intubation"],
                explain='''ตับแข็ง + splenomegaly + hematemesis → สงสัย **variceal bleeding** หลัง resuscitation แล้ว ให้ **vasoactive agent (somatostatin)** ทันทีเพื่อลด portal pressure ก่อนพา EGD
- IV PPI เป็นยาหลักของ non-variceal bleeding
- EGD ต้องทำ แต่ควรเริ่ม vasoactive ก่อน ไม่ใช่ส่องโดยไม่ให้ยา
- SB tube ใช้เมื่อให้ vasoactive 1–2 ชม.แล้วยังออกมาก
- ETT ไม่จำเป็นเมื่อรู้สึกตัวดี V/S stable''',
                pearl="Variceal bleed หลัง resuscitation → somatostatin ก่อนส่อง", topic="Vasoactive in variceal bleeding",
                ref=[f"{D} หน้า 33, 49–50"], nl=["B8.4(2)", "B8.2.2-3(7)"], kind="old", src=OLD),
            mcq("GI-02-03-2", "A 65-year-old man with hepatitis B cirrhosis presents with massive hematemesis. He denies alcohol use. Vital signs are stable. He has pale conjunctivae and multiple dilated veins and telangiectasia on the trunk and abdomen. Besides resuscitation with NSS and a PPI, which other initial management is most important?",
                "IV somatostatin", ["IV tranexamic acid", "Sengstaken-Blakemore tube", "Blood transfusion regardless of hemoglobin", "Vitamin K IV"],
                explain='''HBV cirrhosis + caput medusae/telangiectasia + massive hematemesis → variceal bleeding ต้องเพิ่ม **vasoactive agent (somatostatin)** เป็น initial management
- Tranexamic acid ไม่ลด mortality ใน GI bleeding และเพิ่ม thrombosis
- SB tube สำหรับเลือดออกไม่หยุดหลังให้ยา
- Blood transfusion ให้ตามเกณฑ์ Hb < 7 หรือ V/S unstable ไม่ใช่ทุกราย
- Vitamin K ไม่ได้ผลในตับแข็งและไม่หยุดเลือดจาก varix''',
                pearl="Initial UGIB: IV fluid/transfusion; non-variceal → PPI; variceal → somatostatin", topic="Variceal initial management",
                ref=[f"{D} หน้า 51–52"], nl=["B8.4(2)", "B8.2.2-3(7)"], kind="old", src=OLD),
            mcq("GI-02-03-3", "A 45-year-old man vomited fresh blood and received 4 units of PRC. EGD shows esophageal varices 3 mm in size that are no longer bleeding, together with mild gastritis. Which medication is most appropriate to prevent rebleeding?",
                "Non-selective beta-blocker (propranolol)", ["Long-term proton pump inhibitor", "Vasopressin", "Isosorbide mononitrate alone", "Surgical portosystemic shunt"],
                explain='''ผู้ป่วยมี variceal bleeding แล้ว ต้องได้ **secondary prophylaxis = propranolol ร่วมกับ EVL** จนกว่า varix หมด (เฉลยในสไลด์คือ beta-blocker)
- PPI ระยะยาวใช้กับ peptic ulcer/gastritis ไม่ลด portal pressure
- Vasopressin เป็น vasoactive ระยะเฉียบพลัน ไม่ใช้ป้องกันระยะยาว และมีผลข้างเคียงหัวใจขาดเลือด
- Isosorbide mononitrate เดี่ยว ๆ ไม่แนะนำเพราะไม่ได้ผลและอาจทำให้ความดันต่ำ
- Surgical shunt ไม่ใช่ first line เพิ่มความเสี่ยง hepatic encephalopathy''',
                pearl="Secondary prophylaxis variceal bleed = propranolol + EVL", topic="Secondary prophylaxis",
                ref=[f"{D} หน้า 36, 53–54"], nl=["B8.4(2)", "B8.2.2-3(7)"], kind="old", src=OLD),
            mcq("GI-02-03-4", "A 52-year-old man with HBV cirrhosis is admitted for acute variceal bleeding and has been started on octreotide infusion. He has no fever and no abdominal pain. Which additional medication should be given now?",
                "Ceftriaxone 1 g IV once daily for 7 days", ["Lactulose enema twice daily", "IV metronidazole for 14 days", "Oral rifaximin", "No antibiotic unless fever develops"],
                explain='''Cirrhosis + UGIB ทุกรายต้องได้ **antibiotic prophylaxis** เพื่อป้องกัน SBP/bacterial infection ซึ่งลด rebleeding และ mortality — สูตรตามสไลด์คือ **ceftriaxone 1 g IV OD 7 วัน** หรือ norfloxacin 400 mg bid 7 วัน
- Lactulose ใช้รักษา/ป้องกัน hepatic encephalopathy ไม่ใช่ป้องกันติดเชื้อ
- Metronidazole ไม่ครอบคลุม gram-negative enteric ที่ก่อ SBP
- Rifaximin ใช้ใน HE
- การรอให้มีไข้ก่อนเป็นข้อผิดพลาดที่พบบ่อย เพราะ prophylaxis ต้องให้ตั้งแต่แรก''',
                pearl="Cirrhosis + UGIB → ceftriaxone prophylaxis 7 วัน แม้ไม่มีไข้", topic="Antibiotic prophylaxis",
                ref=[f"{D} หน้า 33"], nl=["B8.4(2)", "2.3.11(4)"]),
        ]),
    ])
