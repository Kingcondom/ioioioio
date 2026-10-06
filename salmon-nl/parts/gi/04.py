from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-GI"
OLD = "ตัวอย่างข้อสอบในสไลด์ NL2-GI"

AP_DX = '''<svg viewBox="0 0 720 270">
 <defs><marker id="gi-04-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="220" height="86" rx="10" class="c1soft"/>
 <text x="120" y="34" text-anchor="middle" class="tb">1 · ปวดลิ้นปี่รุนแรง</text>
 <text x="120" y="56" text-anchor="middle" class="t3">เฉียบพลัน ร้าวไปหลัง</text>
 <text x="120" y="74" text-anchor="middle" class="t3">โน้มตัวไปหน้าดีขึ้น</text>
 <rect x="250" y="10" width="220" height="86" rx="10" class="c2soft"/>
 <text x="360" y="34" text-anchor="middle" class="tb">2 · Lipase/amylase</text>
 <text x="360" y="56" text-anchor="middle" class="tb">≥ 3 × UNL</text>
 <text x="360" y="74" text-anchor="middle" class="t3">lipase จำเพาะกว่า</text>
 <rect x="490" y="10" width="220" height="86" rx="10" class="misssoft"/>
 <text x="600" y="34" text-anchor="middle" class="tb">3 · Imaging (CT/MRI)</text>
 <text x="600" y="56" text-anchor="middle" class="t3">ใช้เมื่อ 2 ข้อแรกไม่ครบ</text>
 <text x="600" y="74" text-anchor="middle" class="t3">หรือวินิจฉัยไม่แน่</text>
 <path d="M120 96V116H600V96M360 96V116" class="ln"/>
 <path d="M360 116V136" class="ln" marker-end="url(#gi-04-01-a)"/>
 <rect x="220" y="138" width="280" height="44" rx="10" class="ac"/>
 <text x="360" y="166" text-anchor="middle" class="tw">≥ 2 ใน 3 = Acute pancreatitis</text>
 <rect x="10" y="200" width="340" height="62" rx="9" class="oksoft"/>
 <text x="180" y="222" text-anchor="middle" class="tb">U/S abdomen ทุกราย</text>
 <text x="180" y="244" text-anchor="middle" class="t3">หา gallstone · sludge · CBD dilatation</text>
 <rect x="370" y="200" width="340" height="62" rx="9" class="box"/>
 <text x="540" y="222" text-anchor="middle" class="tb">Acute abdomen series</text>
 <text x="540" y="244" text-anchor="middle" class="t3">sentinel loop · colon cut-off — ไม่ใช่เกณฑ์วินิจฉัย</text>
</svg>'''

AP_MX = '''<svg viewBox="0 0 720 380">
 <defs><marker id="gi-04-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="700" height="62" rx="9" class="acsoft"/>
 <text x="360" y="32" text-anchor="middle" class="tb">ทุกราย: IV fluid (LRS) · Pain control (morphine) · Early enteral feeding (low fat)</text>
 <text x="360" y="54" text-anchor="middle" class="t3">กินเองไม่ได้ → NG/NJ feeding · ไม่ต้อง NPO นาน · ไม่ต้องให้ PPI/somatostatin</text>
 <path d="M190 72V96" class="ln" marker-end="url(#gi-04-02-a)"/>
 <path d="M530 72V96" class="ln" marker-end="url(#gi-04-02-a)"/>
 <rect x="10" y="98" width="345" height="130" rx="9" class="oksoft"/>
 <text x="182" y="120" text-anchor="middle" class="tb">Mild (ไม่มี organ failure)</text>
 <text x="26" y="146">• ไม่ดีขึ้นใน 48–72 ชม. → CT</text>
 <text x="26" y="168">  ดู necrotizing pancreatitis</text>
 <text x="26" y="194">• Gallstone → cholecystectomy</text>
 <text x="26" y="214" class="tb">  ใน admission นี้ หรือ &lt; 2 wk</text>
 <rect x="365" y="98" width="345" height="130" rx="9" class="badsoft"/>
 <text x="537" y="120" text-anchor="middle" class="tb">Moderate–severe</text>
 <text x="381" y="146">• CT หลัง 5–7 วัน ประเมิน necrosis</text>
 <text x="381" y="168">• ERCP ถ้า GS + acute cholangitis</text>
 <text x="381" y="194">• Cholecystectomy</text>
 <text x="381" y="214" class="tb">  moderate หลัง 3 wk · severe หลัง 6 wk</text>
 <path d="M537 228V252" class="ln" marker-end="url(#gi-04-02-a)"/>
 <rect x="200" y="254" width="510" height="116" rx="9" class="bad"/>
 <text x="455" y="276" text-anchor="middle" class="tw">Infected necrotizing pancreatitis</text>
 <text x="455" y="298" text-anchor="middle" class="tw">ไข้ไม่ลง · ช็อก · WBC สูง · score สูงต่อเนื่อง</text>
 <text x="455" y="320" text-anchor="middle" class="tw">CT: extraluminal gas (ฟองอากาศในเนื้อตาย) · FNA ยืนยัน</text>
 <text x="455" y="346" text-anchor="middle" class="tw">IV carbapenem → ไม่ดีขึ้นจึง drainage</text>
 <rect x="10" y="254" width="180" height="116" rx="9" class="sunk"/>
 <text x="100" y="278" text-anchor="middle" class="tb">ATB carbapenem</text>
 <text x="100" y="298" text-anchor="middle" class="t3">ตามสไลด์ เมื่อ</text>
 <text x="100" y="316" text-anchor="middle" class="t3">necrosis &gt; 30% · OF</text>
 <text x="100" y="334" text-anchor="middle" class="t3">กิน enteral ไม่ได้</text>
 <text x="100" y="356" text-anchor="middle" class="t3">(ดูหมายเหตุในเนื้อหา)</text>
</svg>'''

CP = '''<svg viewBox="0 0 720 270">
 <defs><marker id="gi-04-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="220" height="50" rx="9" class="acsoft"/>
 <text x="360" y="32" text-anchor="middle" class="tb">Chronic pancreatitis</text>
 <text x="360" y="50" text-anchor="middle" class="t3">alcohol ที่พบบ่อยสุด</text>
 <path d="M300 60V90H150V108" class="ln" marker-end="url(#gi-04-03-a)"/>
 <path d="M420 60V90H570V108" class="ln" marker-end="url(#gi-04-03-a)"/>
 <rect x="20" y="110" width="260" height="48" rx="9" class="c1soft"/>
 <text x="150" y="131" text-anchor="middle" class="tb">Exocrine insufficiency</text>
 <text x="150" y="149" text-anchor="middle" class="t3">↓lipase · amylase · protease</text>
 <rect x="440" y="110" width="260" height="48" rx="9" class="c2soft"/>
 <text x="570" y="131" text-anchor="middle" class="tb">Endocrine insufficiency</text>
 <text x="570" y="149" text-anchor="middle" class="t3">β-cell ถูกทำลาย → ↓insulin</text>
 <path d="M150 158V182" class="ln" marker-end="url(#gi-04-03-a)"/>
 <path d="M570 158V182" class="ln" marker-end="url(#gi-04-03-a)"/>
 <rect x="20" y="184" width="260" height="76" rx="9" class="box"/>
 <text x="150" y="206" text-anchor="middle">Steatorrhea · malabsorption · wt loss</text>
 <text x="150" y="228" text-anchor="middle" class="tb">ขาด vitamin A, D, E, K</text>
 <text x="150" y="248" text-anchor="middle" class="t3">vit D ↓ → ↓Ca ↓PO4 ↑ALP ↑PTH</text>
 <rect x="440" y="184" width="260" height="76" rx="9" class="box"/>
 <text x="570" y="214" text-anchor="middle" class="tb">Diabetes mellitus</text>
 <text x="570" y="236" text-anchor="middle" class="t3">(type 3c / pancreatogenic)</text>
 <rect x="296" y="184" width="128" height="76" rx="9" class="sunk"/>
 <text x="360" y="208" text-anchor="middle" class="tb">Imaging</text>
 <text x="360" y="228" text-anchor="middle" class="t3">calcification</text>
 <text x="360" y="246" text-anchor="middle" class="t3">duct dilatation</text>
</svg>'''

LECTURE = lecture("04", "Pancreatitis",
    subtitle="Acute pancreatitis: diagnosis · severity · management · complications · Chronic pancreatitis",
    objectives=[
        "วินิจฉัย acute pancreatitis ด้วยเกณฑ์ 2 ใน 3 และเลือก imaging ที่เหมาะสม (U/S หา gallstone, CT เมื่อไร)",
        "ประเมินความรุนแรงด้วย revised Atlanta/SIRS และรู้ว่า organ failure = severe",
        "สั่ง LRS, morphine และ early enteral feeding และกำหนดเวลาผ่าตัดถุงน้ำดีตามความรุนแรง",
        "วินิจฉัย infected necrotizing pancreatitis และรักษาด้วย carbapenem ± drainage",
        "อธิบายผลของ chronic pancreatitis ต่อ exocrine/endocrine function และ vitamin D deficiency",
    ],
    sections=[
    sec("gi-04-01", "Acute pancreatitis: cause, clinical, diagnosis & severity",
        "Gallstone/alcohol · ปวดลิ้นปี่ร้าวหลัง · ≥ 2 ใน 3 (pain, lipase ≥ 3×, imaging) · organ failure = severe", minutes=7,
        source=f"{D} หน้า 89–94, 99–102, 111–112", nl=["2.3.11(1)", "2.2.43"],
        md='''
### สาเหตุ
- **Gallstone (40–70%)** — พบบ่อยสุด
- **Alcohol (25–35%)**
- Hypertriglyceridemia (มักต้อง TG > 1,000 mg/dL — เสริม), hypercalcemia
- Drugs, post-ERCP
- Malignancy, infection

### อาการและตรวจร่างกาย
- **ปวดลิ้นปี่รุนแรงเฉียบพลัน ร้าวไปหลัง ดีขึ้นเมื่อโน้มตัวไปข้างหน้า**
- คลื่นไส้อาเจียน ไข้
- กดเจ็บลิ้นปี่ bowel sound ลดลง (ileus)
- ตัวเหลือง (ถ้ามี acute cholangitis ร่วม)
- Crepitation / pleural effusion (มักซ้าย)
- **Grey Turner sign** = ecchymosis ที่สีข้าง (flank) · **Cullen sign** = ecchymosis รอบสะดือ → hemorrhagic pancreatitis

### การวินิจฉัย — ≥ 2 ใน 3 ข้อ
[[fig:gi-04-01-dx]]

1. ปวดลิ้นปี่รุนแรงเข้าได้
2. **Lipase หรือ amylase ≥ 3 เท่าของค่าปกติ** (**lipase ดีกว่า** — จำเพาะกว่าและสูงนานกว่า)
3. Imaging (CT/MRI) เข้าได้

> ระดับ amylase/lipase **ไม่บอกความรุนแรง**

### Imaging
- **Acute abdomen series**: colon cut-off sign, sentinel loop (local ileus: ลำไส้เล็กขยายตำแหน่งเดิม) — **ไม่ใช้ในเกณฑ์วินิจฉัย** ใช้ exclude โรคอื่น เช่น perforation (free air)
- **U/S abdomen** — ทำทุกราย: ตับอ่อนโต hypoechoic, peripancreatic fluid/ascites; ที่สำคัญคือหา **gallstone, sludge, biliary dilatation** (gallstone pancreatitis)
- **CT abdomen** ข้อบ่งชี้:
  - วินิจฉัยไม่แน่นอน
  - อาการไม่ดีขึ้นใน 48–72 ชม.
  - Severe pancreatitis หลัง 5–7 วัน เพื่อประเมิน **necrotizing pancreatitis** และ complication

> CT ตั้งแต่วันแรกไม่จำเป็นถ้าวินิจฉัยได้แล้ว เพราะ necrosis ยังไม่ปรากฏ

### ความรุนแรง
เครื่องมือ: **Revised Atlanta**, Modified Marshall, BISAP, APACHE II, Ranson, **SIRS**

| Revised Atlanta | ลักษณะ |
|---|---|
| Mild | ไม่มี organ failure ไม่มี local/systemic complication |
| Moderately severe | Organ failure ที่หายใน 48 ชม. (transient) หรือมี local/systemic complication |
| Severe | **Persistent organ failure > 48 ชม.** (single หรือ multiple) |

> **มี organ failure = severe** · SIRS (≥ 2 ใน 4: T > 38 หรือ < 36, HR > 90, RR > 20, WBC > 12,000 หรือ < 4,000) ที่คงอยู่บ่งชี้ความรุนแรง
''',
        figs=[fig("gi-04-01-dx", "เกณฑ์วินิจฉัย acute pancreatitis (2 ใน 3)", AP_DX,
                  "วงกลมสามวงคือเกณฑ์สามข้อ ต้องเข้าอย่างน้อย 2 ข้อ — U/S ทำทุกรายเพื่อหานิ่ว ส่วน X-ray ไม่ใช่เกณฑ์")],
        pearls=[
            "AP: gallstone > alcohol; ปวดลิ้นปี่ร้าวหลัง โน้มตัวไปหน้าดีขึ้น",
            "Dx ≥ 2 ใน 3: pain, lipase/amylase ≥ 3×ULN, imaging — lipase ดีกว่า",
            "U/S upper abdomen ทุกราย เพื่อ R/O gallstone pancreatitis",
            "CT เมื่อ dx ไม่ชัด, ไม่ดีขึ้น 48–72 ชม., หรือ severe หลัง 5–7 วัน",
            "Organ failure > 48 ชม. = severe; Grey Turner = flank, Cullen = รอบสะดือ",
        ],
        items=[
            mcq("GI-04-01-1", "A 50-year-old man with long-term heavy alcohol use has had epigastric pain radiating to the back for 5 days. The pain is relieved by bending forward. There is epigastric tenderness and guarding, and liver dullness is preserved. What is the most likely diagnosis?",
                "Acute pancreatitis", ["Perforated peptic ulcer", "Acute cholecystitis", "Gastroenteritis", "Inferior wall myocardial infarction"],
                explain='''ปวดลิ้นปี่ **ร้าวไปหลัง ดีขึ้นเมื่อโน้มตัว/งอตัว** ในคนดื่มสุราเรื้อรัง = acute pancreatitis
- Perforated PU จะปวดทั่วท้องทันที ท้องแข็ง และ **liver dullness หายไป** (free air) ซึ่งโจทย์บอกว่ายังปกติ
- Acute cholecystitis ปวด RUQ, Murphy sign
- Gastroenteritis มีถ่ายเหลวเด่น ไม่ร้าวหลัง
- MI ต้องคิดถึงเสมอในปวดลิ้นปี่ แต่ท่าทางที่ทำให้ดีขึ้นและ guarding ไม่เข้ากับ MI''',
                pearl="ปวดลิ้นปี่ร้าวหลัง โน้มตัวดีขึ้น + alcohol = acute pancreatitis", topic="AP clinical",
                ref=[f"{D} หน้า 90, 99–100"], nl=["2.3.11(1)", "2.2.43"], kind="old", src=OLD),
            mcq("GI-04-01-2", "A 46-year-old woman is diagnosed clinically with acute pancreatitis. Serum lipase is 430 U/L (normal 10–140) and triglyceride is 230 mg/dL. An acute abdomen series shows dilated bowel in the right upper quadrant without free air. Which is the most appropriate next investigation?",
                "Ultrasound of the upper abdomen", ["Urine amylase", "Serum lactate", "CT of the upper abdomen", "MRI of the upper abdomen"],
                explain='''วินิจฉัย AP ได้แล้ว (อาการ + lipase > 3 เท่า) TG 230 ไม่สูงพอจะเป็นสาเหตุ ขั้นต่อไปคือ **U/S upper abdomen เพื่อหา gallstone** ซึ่งเป็นสาเหตุที่พบบ่อยที่สุดและเปลี่ยนการรักษา (ERCP/cholecystectomy)
- Urine amylase ไม่จำเป็นเพราะวินิจฉัยได้แล้ว
- Serum lactate ไม่ได้บอกสาเหตุ
- CT ตั้งแต่แรกไม่จำเป็นเมื่อวินิจฉัยได้ และไม่ไวต่อนิ่วถุงน้ำดีเท่า U/S
- MRI/MRCP ใช้เมื่อสงสัยนิ่วใน CBD ที่ U/S ไม่เห็น ไม่ใช่ first line''',
                pearl="AP วินิจฉัยได้แล้ว → U/S หา gallstone", topic="AP imaging",
                ref=[f"{D} หน้า 93, 101–102"], nl=["2.3.11(1)"], kind="old", src=OLD),
            mcq("GI-04-01-3", "A 45-year-old man has severe epigastric pain radiating to the back, relieved by leaning forward. Temperature 38 °C, RR 28/min, pulse 120/min. Breath sounds are normal. Hct 38%, WBC 1,400/mm³, platelets 400,000/mm³, amylase 2,000 U/L, BUN 20 mg/dL, Cr 0.9 mg/dL, AST 70, ALT 65, ALP 130, total bilirubin 2.5 mg/dL. Which finding in this patient indicates disease severity?",
                "Systemic inflammatory response syndrome (SIRS)", ["Serum amylase level", "BUN level", "Hematocrit", "Agitation"],
                explain='''ผู้ป่วยเข้าเกณฑ์ **SIRS** ครบ 4 ข้อ (T 38, HR 120, RR 28, WBC < 4,000) ซึ่งเป็นตัวบ่งชี้ความรุนแรงที่อยู่ในรายการ score ตามสไลด์ (Revised Atlanta, Marshall, BISAP, APACHE II, Ranson, SIRS)
- **Amylase ไม่บอกความรุนแรง** ไม่ว่าสูงเท่าไร
- BUN 20 ยังไม่สูง (BISAP ใช้ BUN > 25)
- Hct 38% ไม่ได้สูง (hemoconcentration > 44% จึงบ่งชี้)
- Agitation/AOC ใช้ใน BISAP แต่ผู้ป่วยไม่ได้มีอาการนี้''',
                pearl="Amylase/lipase ไม่บอก severity; SIRS/organ failure บอก", topic="AP severity",
                ref=[f"{D} หน้า 94, 111–112"], nl=["2.3.11(1)"], kind="old", src=OLD),
            mcq("GI-04-01-4", "A 52-year-old man with acute pancreatitis develops hypotension requiring vasopressors and a rising creatinine that persist for 72 hours despite fluid resuscitation. According to the revised Atlanta classification, how is his pancreatitis classified?",
                "Severe acute pancreatitis", ["Mild acute pancreatitis", "Moderately severe acute pancreatitis", "Chronic pancreatitis", "Interstitial edematous pancreatitis without severity grading"],
                explain='''**Persistent organ failure > 48 ชม.** (ระบบหัวใจไหลเวียน + ไต) = **severe** acute pancreatitis ตาม revised Atlanta
- Mild คือไม่มี organ failure และไม่มี complication
- Moderately severe คือ organ failure ที่หายภายใน 48 ชม. หรือมี local complication โดยไม่มี persistent OF
- Chronic pancreatitis เป็นโรคต่างหาก ไม่ใช่ระดับความรุนแรง
- Interstitial edematous เป็นชนิดตาม morphology ไม่ใช่การแบ่งความรุนแรง''',
                pearl="Organ failure > 48 ชม. = severe AP", topic="Revised Atlanta",
                ref=[f"{D} หน้า 94"], nl=["2.3.11(1)", "2.2.7"]),
        ]),

    sec("gi-04-02", "Acute pancreatitis: management & complications",
        "LRS + morphine + early enteral (low fat) · ERCP เมื่อมี cholangitis · cholecystectomy ตามความรุนแรง · infected necrosis → carbapenem", minutes=7,
        source=f"{D} หน้า 95–98, 103–110, 113–116", nl=["2.3.11(1)", "2.3.11-3(3)"],
        md='''
### การรักษาหลัก (ทุกระดับ)
- **IV fluid: LRS** (ดีกว่า NSS ลด SIRS)
- **Pain control: morphine**
- **Nutrition: early enteral feeding (low fat)** — เริ่มกินทางปากเมื่อปวดลดลง ไม่ต้อง NPO รอ lipase ปกติ ถ้ากินเองไม่ได้ → **NG/NJ tube feeding**

[[fig:gi-04-02-mx]]

### Mild
- LRS, morphine, early enteral feeding (low fat)
- CT abdomen ถ้าอาการ **ไม่ดีขึ้นใน 48–72 ชม.** → ดู necrotizing pancreatitis

### Moderate to severe
- LRS, morphine
- **NG/NJ + early enteral feeding**
- **CT abdomen หลัง 5–7 วัน** ประเมิน necrosis
- **ATB: carbapenem** ตามสไลด์ เมื่อ pancreatic necrosis > 30%, organ failure, หรือ not tolerate enteral feeding
- **ERCP** เมื่อเป็น gallstone pancreatitis ร่วมกับ **acute cholangitis**

> แนวทางปัจจุบัน (ACG 2024/AGA) **ไม่แนะนำ prophylactic antibiotics** ใน sterile necrosis ไม่ว่าจะกว้างเท่าไร — ให้ ATB เฉพาะเมื่อสงสัยหรือยืนยัน infected necrosis หรือมีการติดเชื้อนอกตับอ่อน (เสริม) ถ้าโจทย์ไม่มีหลักฐานติดเชื้อ ให้เลือกตอบการรักษาประคับประคอง

> ยาที่ **ไม่มีประโยชน์** ใน AP: PPI, somatostatin/octreotide, ceftriaxone แบบ prophylaxis — ข้อสอบชอบเอามาเป็นตัวลวง

### Gallstone pancreatitis — cholecystectomy เมื่อไร
| ความรุนแรง | เวลาผ่าตัด |
|---|---|
| Mild | **ใน admission นี้** หรือภายใน < 2 สัปดาห์ |
| Moderate | หลัง 3 สัปดาห์ |
| Severe | หลัง 6 สัปดาห์ |

### Complication: necrotizing & infected necrotizing pancreatitis
- **Necrotizing pancreatitis** — เนื้อตับอ่อนตาย เห็นจาก CT (non-enhancing)
- **Infected necrosis** — สงสัยเมื่อ
  - ไข้ไม่ลง, BP ต่ำ, HR/RR เร็ว
  - severity score สูงต่อเนื่อง
  - Hb ลด, WBC สูง
  - CT พบ **extraluminal gas** (ฟองอากาศ/air-fluid ในเนื้อตาย)
  - ยืนยันด้วย percutaneous FNA (ปัจจุบันไม่จำเป็นทุกราย — เสริม)
- **Tx: IV ATB (carbapenem)** → ไม่ดีขึ้นจึง **drainage** (step-up approach, รอให้ walled-off ≥ 4 สัปดาห์ถ้าทำได้ — เสริม)

> Pseudocyst = ถุงน้ำมีผนัง ≥ 4 สัปดาห์ ไม่มีเนื้อตาย ไม่มีแก๊ส (เสริม) — ต่างจาก infected necrosis ที่มีไข้ WBC สูงและแก๊ส
''',
        figs=[fig("gi-04-02-mx", "การดูแล acute pancreatitis ตามความรุนแรง", AP_MX,
                  "แถบบนคือสิ่งที่ทุกรายได้ แล้วแยกตามความรุนแรงเพื่อกำหนดเวลา CT และผ่าตัด กล่องแดงล่างคือภาวะแทรกซ้อนที่ต้องให้ยาฆ่าเชื้อ")],
        pearls=[
            "AP ทุกราย: LRS + morphine + early enteral feeding (low fat)",
            "กินไม่ได้ → NG/NJ feeding ไม่ใช่ TPN หรือ NPO นาน",
            "Gallstone AP + cholangitis → ERCP",
            "Cholecystectomy: mild ใน admission นี้, moderate หลัง 3 wk, severe หลัง 6 wk",
            "Infected necrosis (ไข้ WBC สูง แก๊สใน CT) → carbapenem ± drainage",
        ],
        items=[
            mcq("GI-04-02-1", "A 45-year-old man with 10 years of alcohol use presented with severe epigastric pain radiating to the back and vomiting for 1 day. Initial pain score was 8/10. Temperature 37 °C, pulse 90/min, RR 18/min; epigastric tenderness and hypoactive bowel sounds; serum amylase 2,000 U/L. After 1 day of hydration, the pain score has declined to 5/10 and he feels hungry. What is the most appropriate dietary management?",
                "Low-fat diet", ["Continue NPO until amylase normalizes", "Clear fluid only for 3 days", "Total parenteral nutrition", "Regular diet"],
                explain='''Mild AP ที่ปวดลดลงและหิว → เริ่ม **early oral feeding ด้วย low-fat diet** ได้ทันที ช่วยลด bacterial translocation และ infection
- NPO รอ amylase ปกติไม่มีประโยชน์และเพิ่มภาวะแทรกซ้อน
- Clear fluid ก่อนไม่จำเป็น (การเริ่มด้วย low-fat solid ปลอดภัยเท่ากัน)
- TPN ใช้เฉพาะเมื่อให้ทางเดินอาหารไม่ได้เลย
- Regular diet มีไขมันสูงกระตุ้นตับอ่อน (สไลด์เน้น low fat)''',
                pearl="AP ปวดลดลง → early oral low-fat diet", topic="AP nutrition",
                ref=[f"{D} หน้า 95, 107–108"], nl=["2.3.11(1)"], kind="old", src=OLD),
            mcq("GI-04-02-2", "A 50-year-old man who drinks heavily has had epigastric pain radiating to the back with mild nausea and no fever for 1 day. There is epigastric tenderness without peritoneal signs. He has received IV fluid and IV analgesics while kept NPO, but cannot yet tolerate oral intake because of nausea. What is the most appropriate next step?",
                "Start enteral feeding via nasogastric tube", ["IV ceftriaxone", "IV omeprazole", "IV somatostatin analogue", "ERCP with sphincterotomy"],
                explain='''หลังให้สารน้ำและยาแก้ปวดแล้ว ขั้นต่อไปคือ **early enteral nutrition** — ถ้ากินทางปากไม่ไหวให้ทาง **NG/NJ tube** (เฉลยในสไลด์: NG)
- Ceftriaxone prophylaxis ไม่มีประโยชน์ใน AP ที่ไม่มีการติดเชื้อ
- Omeprazole ไม่ได้ช่วย pancreatitis
- Somatostatin analogue เคยมีการศึกษาแต่ไม่ได้ผล ไม่แนะนำ
- ERCP ทำเมื่อเป็น gallstone pancreatitis ร่วมกับ cholangitis — ผู้ป่วยนี้เป็น alcoholic และไม่มีไข้/ตัวเหลือง''',
                pearl="AP กินเองไม่ได้ → NG/NJ enteral feeding", topic="AP enteral feeding",
                ref=[f"{D} หน้า 96, 105–106"], nl=["2.3.11(1)"], kind="old", src=OLD),
            mcq("GI-04-02-3", "A 40-year-old woman was admitted with mild acute pancreatitis 5 days ago. Her abdominal pain has resolved and she is eating well. Ultrasound shows multiple gallstones without bile duct dilatation. What is the most appropriate management?",
                "Laparoscopic cholecystectomy during this admission", ["Oral ursodeoxycholic acid and follow-up ultrasound", "Discharge and schedule cholecystectomy after 6 weeks", "Extracorporeal shock wave lithotripsy", "No intervention because gallstones are unrelated"],
                explain='''Mild gallstone pancreatitis → **cholecystectomy ใน admission เดียวกัน** (หรือภายใน < 2 สัปดาห์) เพื่อป้องกัน pancreatitis ซ้ำ ซึ่งเกิดได้สูงถ้ารอ
- Ursodeoxycholic acid สลายนิ่วได้ช้าและไม่ป้องกัน pancreatitis ซ้ำ
- รอ 6 สัปดาห์ใช้กับ severe pancreatitis
- ESWL ไม่ใช้กับนิ่วถุงน้ำดีในบริบทนี้
- Gallstone คือสาเหตุของ pancreatitis ครั้งนี้ ไม่ใช่สิ่งที่ไม่เกี่ยวข้อง''',
                pearl="Mild gallstone AP → cholecystectomy ใน admission นี้", topic="Timing of cholecystectomy",
                ref=[f"{D} หน้า 97, 113–114"], nl=["2.3.11(1)", "2.3.11-3(3)"], kind="old", src=OLD),
            mcq("GI-04-02-4", "A 35-year-old man admitted with acute pancreatitis 7 days ago develops persistent abdominal pain. Temperature 37.8 °C, BP 110/80 mmHg, pulse 90/min. WBC 22,000/mm³ (PMN 90%). CT shows edema of the pancreatic tail with gas bubbles and an air-fluid level within a peripancreatic collection. What is the most likely diagnosis?",
                "Infected necrotizing pancreatitis", ["Sterile necrotizing pancreatitis", "Pancreatic pseudocyst", "Pancreatic abscess from perforated duodenal ulcer", "Splenic vein thrombosis"],
                explain='''หลัง AP ~1 สัปดาห์ มีไข้ WBC สูงมาก และ CT พบ **extraluminal gas/air-fluid level ในบริเวณตับอ่อน** = **infected necrotizing pancreatitis** → IV carbapenem และ drainage ถ้าไม่ดีขึ้น
- Sterile necrosis ไม่มีแก๊สและไม่มี leukocytosis สูงขนาดนี้
- Pseudocyst ต้องใช้เวลา ≥ 4 สัปดาห์ มีผนังชัดและไม่มีแก๊ส
- Perforated duodenal ulcer จะมี free air ใต้กระบังลมและ peritonitis ทันที
- Splenic vein thrombosis เป็นภาวะแทรกซ้อนทางหลอดเลือด ไม่ทำให้เกิดแก๊สใน collection''',
                pearl="AP + ไข้ WBC สูง + แก๊สใน CT = infected necrosis", topic="Infected necrosis",
                ref=[f"{D} หน้า 98, 115–116"], nl=["2.3.11(1)"], kind="old", src=OLD),
            mcq("GI-04-02-5", "A 39-year-old man with heavy alcohol use has acute abdominal pain and anorexia for 2 days. Temperature 37.2 °C, BP 100/68 mmHg, pulse 135/min, RR 20/min, SpO2 100%. There is epigastric tenderness and flank ecchymosis. Which therapy should be the mainstay now?",
                "Aggressive IV fluid hydration and analgesia", ["ERCP", "Chlordiazepoxide only", "EGD with variceal banding", "Percutaneous transhepatic cholangiography"],
                explain='''Acute pancreatitis ที่มี **Grey Turner sign (flank ecchymosis)** = hemorrhagic pancreatitis และ tachycardia/BP ค่อนข้างต่ำจาก third spacing → หัวใจของการรักษาคือ **IV fluid (LRS) และยาแก้ปวด**
- ERCP ใช้เมื่อมี gallstone + cholangitis
- Chlordiazepoxide ใช้ป้องกัน alcohol withdrawal เป็นการรักษาเสริม ไม่ใช่หลัก
- Variceal banding ใช้ใน variceal bleeding ซึ่งไม่มี hematemesis
- PTC ใช้ระบาย biliary obstruction เมื่อ ERCP ทำไม่ได้''',
                pearl="Grey Turner sign → severe/hemorrhagic AP → fluid + analgesia", topic="AP initial management",
                ref=[f"{D} หน้า 90, 109–110"], nl=["2.3.11(1)"], kind="old", src=OLD),
        ]),

    sec("gi-04-03", "Chronic pancreatitis",
        "Alcohol · ปวดหลังกิน · steatorrhea + ADEK deficiency + DM · calcification ใน CT/AXR · enzyme replacement", minutes=5,
        source=f"{D} หน้า 117–121", nl=["2.3.11-3(2)", "2.3.4(10)"],
        md='''
### นิยามและสาเหตุ
การอักเสบเรื้อรังแบบ **progressive** ของตับอ่อน → fibrosis ถาวร
- **Alcohol (พบบ่อยสุด)**
- Pancreatic ductal obstruction (stricture, stone)
- Smoking
- Systemic diseases (SLE, hypertriglyceridemia)

### อาการ
- **ปวดลิ้นปี่** ร้าวไปหลัง ดีขึ้นเมื่อโน้มตัว **ปวดมากขึ้นหลังกินอาหาร**
- **Pancreatic insufficiency**
  - Exocrine: ↓amylase, lipase, protease → **steatorrhea**, malabsorption, น้ำหนักลด, ขาด **fat-soluble vitamins (A, D, E, K)**
  - Endocrine: ↓insulin → **DM**

[[fig:gi-04-03-cp]]

### การตรวจ
- **CT abdomen / MRCP**: **pancreatic calcification**, pancreatic duct dilatation และ stricture (chain of lakes — เสริม)
- **Abdominal X-ray**: pancreatic calcification
- Lab: **amylase/lipase มักปกติ** (เนื้อตับอ่อนเหลือน้อย)
- Pancreatic function tests (เช่น fecal elastase — เสริม)

### การรักษา
- **หยุด alcohol และบุหรี่**
- **Pancreatic enzyme replacement**
- Pain control: NSAIDs, opioid
- รักษาสาเหตุ
- ติดตามและรักษาภาวะแทรกซ้อน (vitamin supplement, antidiabetics)

### Vitamin D deficiency จาก chronic pancreatitis (ข้อสอบ)
ขาด vit D → ดูดซึม Ca ลดลง → **↓Ca, ↓PO4, ↑ALP, ↑PTH** (secondary hyperparathyroidism)
- อาการ hypocalcemia: **Chvostek sign**, ตะคริว, ชา
- **Osteomalacia** (ผู้ใหญ่) / rickets (เด็ก) → ปวดกระดูก

| ภาวะ | Ca | PO4 | ALP | PTH |
|---|---|---|---|---|
| Vitamin D deficiency | ↓ | **↓** | ↑ | ↑ |
| Hypoparathyroidism | ↓ | **↑** | ปกติ | ↓ |
''',
        figs=[fig("gi-04-03-cp", "Chronic pancreatitis: exocrine และ endocrine insufficiency", CP,
                  "ซ้ายคือผลจากขาดเอนไซม์ (ไขมันไม่ถูกย่อย → ขาด vitamin A D E K) ขวาคือผลจาก β-cell ถูกทำลาย (DM)")],
        pearls=[
            "Chronic pancreatitis: alcohol, ปวดหลังกิน, steatorrhea, DM",
            "CT/AXR เห็น pancreatic calcification; amylase/lipase มักปกติ",
            "Tx: หยุดเหล้า/บุหรี่ + pancreatic enzyme replacement + analgesic",
            "CP + Chvostek + ↓Ca ↓PO4 ↑ALP = vitamin D deficiency (osteomalacia)",
        ],
        items=[
            mcq("GI-04-03-1", "A 26-year-old man has had recurrent chronic pancreatitis for 5 years. He reports bone pain and frequent muscle cramps. Chvostek sign is positive. Hct 30%, FPG 160 mg/dL, Ca 4 mg/dL (8.5–10.6), PO4 1.2 mg/dL (2.5–5.1), albumin 2 g/dL, ALP 800 U/L. What is the most likely cause of his bone pain and cramps?",
                "Vitamin D deficiency", ["Anemia", "Hypoalbuminemia", "Hypoparathyroidism", "Diabetic neuropathy"],
                explain='''Chronic pancreatitis → fat malabsorption → **ขาด vitamin D** → Ca และ **PO4 ต่ำทั้งคู่** ร่วมกับ **ALP สูงมาก** (osteomalacia, secondary hyperparathyroidism) → ปวดกระดูกและตะคริว/Chvostek จาก hypocalcemia
- Anemia ไม่ทำให้ Ca/PO4 ต่ำหรือ Chvostek
- Hypoalbuminemia ทำให้ total Ca ต่ำ แต่ corrected Ca = 4 + 0.8 × (4 − 2) = 5.6 mg/dL ยังต่ำมาก และไม่อธิบาย PO4 ต่ำ ALP สูง
- Hypoparathyroidism จะมี **PO4 สูง** และ ALP ปกติ
- Diabetic neuropathy ไม่ทำให้ Chvostek หรือปวดกระดูก''',
                pearl="↓Ca ↓PO4 ↑ALP = vitamin D deficiency; ↓Ca ↑PO4 = hypoparathyroidism", topic="CP vitamin D deficiency",
                ref=[f"{D} หน้า 120–121"], nl=["2.3.4(10)", "2.3.11-3(2)"], kind="old", src=OLD),
            mcq("GI-04-03-2", "A 48-year-old man with 20 years of heavy drinking has recurrent epigastric pain after meals, bulky greasy foul-smelling stools and a 10-kg weight loss. Plain abdominal radiograph shows scattered calcifications in the epigastrium. Serum lipase is normal. What is the most likely diagnosis?",
                "Chronic pancreatitis", ["Acute pancreatitis", "Celiac disease", "Pancreatic pseudocyst", "Crohn disease"],
                explain='''ปวดลิ้นปี่หลังกิน + **steatorrhea** + น้ำหนักลด ในคนดื่มเหล้านาน และ **AXR เห็น pancreatic calcification** โดย **lipase ปกติ** = chronic pancreatitis
- Acute pancreatitis ต้องมี lipase ≥ 3 เท่าและเป็นเฉียบพลัน
- Celiac disease มี malabsorption แต่ไม่มี calcification ของตับอ่อน และพบน้อยในไทย
- Pseudocyst เป็นถุงน้ำ ไม่ใช่ calcification กระจาย
- Crohn disease ถ่ายเหลวเรื้อรัง ปวดท้องน้อยขวา ไม่มี pancreatic calcification''',
                pearl="Steatorrhea + pancreatic calcification + lipase ปกติ = chronic pancreatitis", topic="CP diagnosis",
                ref=[f"{D} หน้า 117–118"], nl=["2.3.11-3(2)"]),
            mcq("GI-04-03-3", "A 50-year-old man with alcohol-related chronic pancreatitis has steatorrhea and weight loss. He stopped drinking 6 months ago. Which treatment best addresses his steatorrhea?",
                "Pancreatic enzyme replacement taken with meals", ["Long-term oral metronidazole", "Loperamide", "Low-dose oral prednisolone", "Cholestyramine"],
                explain='''Steatorrhea ใน chronic pancreatitis เกิดจาก **exocrine insufficiency** (ขาด lipase) รักษาด้วย **pancreatic enzyme replacement** กินพร้อมอาหาร ร่วมกับเสริม fat-soluble vitamins
- Metronidazole ใช้ใน bacterial overgrowth/giardiasis ไม่ได้แก้การขาดเอนไซม์
- Loperamide ลดความถี่ถ่ายแต่ไม่แก้การดูดซึมไขมัน
- Prednisolone ใช้ใน autoimmune pancreatitis ไม่ใช่ alcoholic
- Cholestyramine ใช้ใน bile acid diarrhea และอาจทำให้ขาด fat-soluble vitamin มากขึ้น''',
                pearl="CP steatorrhea → pancreatic enzyme replacement", topic="CP management",
                ref=[f"{D} หน้า 119"], nl=["2.3.11-3(2)"]),
        ]),
    ])
