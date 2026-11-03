# -*- coding: utf-8 -*-
# หัวข้อ 1–5: นิยาม สาเหตุ อาการ ตรวจร่างกาย แล็บ ภาพถ่ายรังสี  (สไลด์หน้า 1–17)

FIG_ROOTS = {
 "title": "ตับแข็งมีสองราก — ความดันพอร์ทัลสูง กับ ตับทำงานไม่พอ",
 "cap": "สไลด์หน้า 22 แบ่งภาวะแทรกซ้อนของตับแข็งเป็นสองราก · **Portal hypertension** (พังผืดและก้อน regenerative nodule ต้านการไหลของเลือดพอร์ทัล) → เลือดหาทางลัด **varices** · **ascites** · ม้ามโต · **Liver insufficiency** (เซลล์ตับเหลือน้อย) → **เหลือง** · **INR ยาว albumin ต่ำ** · **HE** · ภาวะแทรกซ้อนที่อันตรายที่สุด (**ascites · SBP · HE · HRS**) อาศัย **ทั้งสองรากร่วมกัน**",
 "svg": """<svg viewBox="0 0 440 300" role="img" aria-label="ตับแข็งแยกเป็นสองราก portal hypertension ทำให้ varices ascites ม้ามโต และ liver insufficiency ทำให้เหลือง INR ยาว albumin ต่ำ ภาวะแทรกซ้อนที่ใช้ทั้งสองรากคือ ascites SBP HE HRS" xmlns="http://www.w3.org/2000/svg">
<rect x="150" y="10" width="140" height="40" rx="10" class="ac"/><text x="220" y="35" class="b mid tac">Cirrhosis</text>
<line x1="190" y1="50" x2="110" y2="80" class="ln" marker-end="url(#ah)"/><line x1="250" y1="50" x2="330" y2="80" class="ln" marker-end="url(#ah)"/>
<rect x="10" y="82" width="200" height="44" rx="8" class="wa"/><text x="110" y="100" class="sm b mid">Portal hypertension</text><text x="110" y="117" class="xs mid i2">“ถนนตัน” — ต้านการไหลในตับ</text>
<rect x="230" y="82" width="200" height="44" rx="8" class="ms"/><text x="330" y="100" class="sm b mid">Liver insufficiency</text><text x="330" y="117" class="xs mid i2">“โรงงานพัง” — เซลล์ตับเหลือน้อย</text>
<rect x="10" y="140" width="200" height="66" rx="8" class="bx"/>
<text x="22" y="160" class="xs">• Varices → อาเจียนเป็นเลือด</text><text x="22" y="177" class="xs">• ม้ามโต → เกล็ดเลือดต่ำ</text><text x="22" y="194" class="xs">• Caput medusae · collaterals</text>
<rect x="230" y="140" width="200" height="66" rx="8" class="bx"/>
<text x="242" y="160" class="xs">• เหลือง (bilirubin ↑)</text><text x="242" y="177" class="xs">• INR ยาว · albumin ต่ำ</text><text x="242" y="194" class="xs">• Estrogen ค้าง → spider, gynecomastia</text>
<line x1="110" y1="206" x2="190" y2="232" class="lac" marker-end="url(#ah-ac)"/><line x1="330" y1="206" x2="250" y2="232" class="lac" marker-end="url(#ah-ac)"/>
<rect x="80" y="234" width="280" height="54" rx="10" class="bad"/><text x="220" y="256" class="sm b mid tbad">ใช้ทั้งสองราก</text><text x="220" y="276" class="xs mid">Ascites · SBP · Hepatic encephalopathy · HRS</text>
</svg>"""}

sec("gi-cir-01", "ตับแข็งคืออะไร — พังผืด ก้อน regenerative และสาเหตุในไทย",
    "พังผืดลุกลาม + โครงสร้างบิดเบี้ยว + regenerative nodule · ระยะแรกย้อนกลับได้ · micro vs macronodular · สุรา HBV HCV",
    9, r"""
### นิยาม (สไลด์)
**Cirrhosis** = ผลสุดท้ายของโรคตับเรื้อรัง ประกอบด้วย 3 อย่างพร้อมกัน
- **progressive hepatic fibrosis** — พังผืดลุกลาม
- **distortion of the hepatic architecture** — โครงสร้าง lobule และหลอดเลือดในตับบิดเบี้ยว
- **formation of regenerative nodules** — ตับพยายามสร้างเซลล์ใหม่ แต่เซลล์ **ผิดรูปและเรียงตัวไม่เป็นระเบียบ**

สไลด์ย้ำว่า **ระยะแรกย้อนกลับได้ (reversal in earlier stages)** แต่ **ระยะท้ายย้อนไม่ได้** → การรักษาสาเหตุเร็วจึงสำคัญที่สุด

### พยาธิสรีรวิทยา (สไลด์)
1. เซลล์ตับถูกทำลาย **ช้า ๆ ต่อเนื่อง เรื้อรัง**
2. **แถบพังผืด** แทนที่โครงสร้างปกติ
3. เซลล์ที่สร้างใหม่ผิดรูป → **การไหลของเลือดและน้ำเหลืองผิดปกติ** → กระตุ้นพังผืดเพิ่ม (วงจรเลวร้าย)

[[fig:cir_roots]]

### พยาธิวิทยา 2 แบบ (สไลด์)
| ประเภท | ลักษณะ | สาเหตุที่พบบ่อย |
|---|---|---|
| **Micronodular** | nodule **< 3 มม.** ขนาดเท่า ๆ กัน มักไม่มีเส้นเลือดและท่อน้ำดีอยู่ภายใน | **สุรา** · ภาวะเหล็กเกิน · ท่อน้ำดีอุดตัน |
| **Macronodular** | nodule **> 3 มม.** หลายขนาด มักมีเส้นเลือดและท่อน้ำดีอยู่ภายใน | **ไวรัสตับอักเสบ** · autoimmune hepatitis |

### สาเหตุ (สไลด์)
| กลุ่ม | ตัวอย่างในสไลด์ |
|---|---|
| **สุรา** | alcohol |
| **ติดเชื้อ** | **ไวรัสตับอักเสบ B, C** · congenital syphilis · toxoplasmosis · schistosomiasis |
| **ภูมิต้านตนเอง** | autoimmune hepatitis · autoimmune cholangitis · **PBC · PSC** |
| **ยา** | **methotrexate · PTU · methyldopa · INH · nitrofurantoin** |
| **สารเคมี** | arsenic · phosphorus · copper |
| **ท่อน้ำดีอุดตันเรื้อรัง (cholestatic)** | biliary atresia · Caroli · obstructive jaundice · choledochal cyst |
| **เลือดคั่ง (venous congestion)** | **Budd–Chiari** · **constrictive pericarditis · RHF** (cardiac cirrhosis) · veno-occlusive disease |
| **เมแทบอลิก** | α1-antitrypsin deficiency · AIP · glycogen storage · **NASH (MASH)** · **Wilson** · **hemochromatosis** · **thalassemia** (เหล็กเกิน) · intestinal bypass |
| **ไม่ทราบสาเหตุ** | cryptogenic |

### ในไทย (สไลด์ — ศิริราช 2544–47)
**สุรา 38.5% · HBV 19.6% · HCV 17%** เป็นสามอันดับแรก ที่เหลือคือไวรัสร่วมกับสุรา ไวรัสสองชนิดร่วมกัน และ **cryptogenic ~6%**

> สหรัฐฯ: ตับแข็งเป็น **สาเหตุตายอันดับที่ 10** อย่างน้อย 25,000 รายต่อปี ชายมากกว่าหญิง (สไลด์)
""",
    ["Cirrhosis = fibrosis + architecture distortion + regenerative nodules",
     "ระยะแรกย้อนกลับได้ — รักษาสาเหตุให้เร็ว",
     "Micronodular < 3 มม. = สุรา · Macronodular > 3 มม. = ไวรัส",
     "ไทย: สุรา > HBV > HCV"],
    [mcq("GI-CIR-MCQ-01",
         "Which triad of histological features defines liver cirrhosis?",
         ["Steatosis, ballooning and Mallory–Denk bodies",
          "Progressive fibrosis, distortion of hepatic architecture and regenerative nodules",
          "Portal inflammation, interface hepatitis and plasma cells",
          "Centrilobular necrosis, sinusoidal dilatation and congestion",
          "Bile duct proliferation, ductopenia and cholestasis"],
         1,
         "สไลด์นิยามตับแข็งด้วย 3 อย่าง: **พังผืดลุกลาม · โครงสร้างตับบิดเบี้ยว · regenerative nodule**\n\nตัวเลือกอื่นเป็นลักษณะของโรคที่ **อาจนำไปสู่** ตับแข็ง — steatohepatitis (ข้อ A) · autoimmune hepatitis (ข้อ C) · ตับคั่งเลือด (ข้อ D) · cholestatic disease (ข้อ E)",
         "Fibrosis + distortion + nodules = cirrhosis", "Definition"),
     mcq("GI-CIR-MCQ-02",
         "A liver explant shows uniform nodules about 2 mm in diameter that contain no portal tracts. Which aetiology is most likely?",
         ["Chronic hepatitis B", "Autoimmune hepatitis", "Alcohol-associated liver disease",
          "Chronic hepatitis C", "Wilson disease presenting in adolescence"],
         2,
         "สไลด์: **micronodular (< 3 มม.)** ขนาดสม่ำเสมอ ไม่มีเส้นเลือดหรือท่อน้ำดีในก้อน → **สุรา** ภาวะเหล็กเกิน หรือท่อน้ำดีอุดตัน\n\n**Macronodular (> 3 มม.)** หลายขนาด มี portal tract อยู่ในก้อน → **ไวรัสตับอักเสบ · autoimmune hepatitis**",
         "Micro = alcohol · Macro = virus/AIH", "Pathology"),
     mcq("GI-CIR-MCQ-03",
         "A 45-year-old man has cirrhosis with markedly raised JVP that rises on inspiration, a pericardial knock and calcified pericardium on CT. Which mechanism caused his cirrhosis?",
         ["Chronic venous congestion", "Copper accumulation", "Autoimmune destruction of bile ducts",
          "Iron overload", "Alcohol toxicity"],
         0,
         "JVP ขึ้นตอนหายใจเข้า (**Kussmaul sign**) + pericardial knock + เยื่อหุ้มหัวใจมีหินปูน = **constrictive pericarditis** → เลือดคั่งในตับเรื้อรัง → **cardiac cirrhosis**\n\nสไลด์จัดไว้ในกลุ่ม **venous congestion** ร่วมกับ Budd–Chiari, RHF และ veno-occlusive disease — **ตรวจคอ (JVP) ทุกรายที่ตับแข็งไม่ทราบสาเหตุ**",
         "ตับแข็ง + JVP สูง = นึกถึงหัวใจ", "Causes"),
     old("MOCK-148", nl=["2.3.11(4)", "B8.2.5(4)"],
         pearl="Ascites = ต้านการไหลในตับ + หลอดเลือดช่องท้องขยาย")],
    nl=["2.3.11(4)", "B8.2.5(4)", "2.3.11(2)", "B8.2.5(3)"],
    figs={"cir_roots": FIG_ROOTS})


sec("gi-cir-02", "อาการ — compensated vs decompensated และประวัติที่ต้องถาม",
    "ระยะไม่มีอาการ (เจอโดยบังเอิญ) · ระยะมีอาการ 4 อย่าง ascites บ่อยสุด · ตรวจพบตอนผ่าศพ 30–40% · ประวัติเสี่ยง 7 ข้อ",
    6, r"""
### 2 ระยะทางคลินิก (สไลด์)
| ระยะ | อาการ |
|---|---|
| **Compensated cirrhosis** (ไม่มีอาการ) | เจอ **โดยบังเอิญ** จากเลือดหรืออัลตราซาวนด์ · พบขณะผ่าตัดช่องท้อง · พบหลังเสียชีวิต · อาจมีแค่ปวดเมื่อย อ่อนเพลีย จุกแน่นชายโครงขวา นอนไม่หลับ |
| **Decompensated cirrhosis** (มีอาการ) | **น้ำในช่องท้อง (พบบ่อยที่สุด)** · **เลือดออกจาก varices** · **ตัวเหลือง** · **ซึมจากตับ (HE)** |

> สไลด์: ตับแข็ง **ตรวจพบครั้งแรกตอนผ่าศพถึง 30–40%** — เพราะระยะ compensated อาจไม่มีอาการเลยหลายปี

**เพิ่มเติม (ไม่ได้มาจากสไลด์ — Baveno VII 2022)**: นิยาม decompensation = เกิด **ascites, variceal bleeding หรือ overt HE** ครั้งแรก · ค่ามัธยฐานการรอดชีวิต **compensated > 12 ปี** · **decompensated ~2 ปี**

### อาการที่ถามได้ (สไลด์)
อ่อนเพลีย · **ช้ำง่าย** · ขาบวม · ไข้ · น้ำหนักลด · ท้องเสีย · **คัน** · **ท้องโตขึ้น** · **สับสนหรือนอนผิดเวลา** (HE ระยะแรก)

### ประวัติเสี่ยงที่ต้องถามทุกราย (สไลด์)
| ถาม | หาอะไร |
|---|---|
| เคยเป็นตับอักเสบ · ประวัติครอบครัวเป็นโรคตับ | HBV (ติดจากแม่) · Wilson · hemochromatosis |
| **ดื่มสุรา** | ปริมาณ ระยะเวลา |
| **เบาหวาน** | MASLD |
| **ยาเสพติดแบบฉีดหรือสูด** · **รับเลือด** | HBV · HCV |
| โรคภูมิต้านตนเอง — **IBD** · rheumatoid · ไทรอยด์ | AIH · **PSC (คู่กับ ulcerative colitis)** |
""",
    ["Ascites = อาการ decompensation ที่พบบ่อยที่สุด",
     "Decompensation: ascites · variceal bleed · jaundice · HE",
     "พบตอนผ่าศพ 30–40% — compensated ไม่มีอาการ",
     "IBD + cholestasis → นึกถึง PSC"],
    [mcq("GI-CIR-MCQ-04",
         "Which is the most common presenting feature of decompensated cirrhosis?",
         ["Variceal haemorrhage", "Hepatic encephalopathy", "Ascites", "Jaundice", "Hepatorenal syndrome"],
         2,
         "สไลด์: อาการของ decompensated cirrhosis 4 อย่าง — **น้ำในช่องท้องพบบ่อยที่สุด** ตามด้วยเลือดออกจาก varices ตัวเหลือง และซึมจากตับ\n\nHRS เป็นภาวะแทรกซ้อนระยะท้ายที่เกิด **หลัง** มี ascites แล้ว",
         "Decompensation ที่พบบ่อยสุด = ascites", "Clinical stage"),
     mcq("GI-CIR-MCQ-05",
         "A 38-year-old man with ulcerative colitis has pruritus, ALP 4 times the upper limit and newly diagnosed cirrhosis. Which investigation best confirms the likely cause?",
         ["Antimitochondrial antibody", "MRCP", "Serum ceruloplasmin", "Transferrin saturation", "Anti-LKM-1 antibody"],
         1,
         "**IBD (โดยเฉพาะ UC) + cholestasis** = **primary sclerosing cholangitis** · สไลด์: วินิจฉัย PSC ด้วย **ERCP หรือ MRCP** (ท่อน้ำดีตีบสลับขยายแบบลูกปัด)\n\nAMA ใช้กับ PBC (มักเป็นหญิงวัยกลางคน) · ceruloplasmin ใช้กับ Wilson · transferrin saturation ใช้กับ hemochromatosis · anti-LKM-1 ใช้กับ AIH type 2",
         "UC + ALP สูง = PSC → MRCP", "History")],
    nl=["2.3.11(4)", "2.1.12", "2.1.13"])


FIG_PE = {
 "title": "ตรวจร่างกายตับแข็ง — แยกตามกลไก",
 "cap": "สไลด์หน้า 6–12 · **Estrogen ค้าง** (ตับทำลายไม่ได้ + androstenedione จากต่อมหมวกไตถูกเปลี่ยนเป็น estrogen ที่เนื้อเยื่อรอบนอกมากขึ้น) → spider angioma, palmar erythema, gynecomastia, อัณฑะฝ่อ · **Albumin ต่ำ** → Muehrcke's, Terry's nails, บวม · **Portal hypertension** → ม้ามโต caput medusae ascites · **Toxin ค้าง** → asterixis, fetor hepaticus",
 "svg": """<svg viewBox="0 0 440 262" role="img" aria-label="อาการแสดงของตับแข็งแยกตามกลไก estrogen ค้าง albumin ต่ำ portal hypertension และสารพิษค้าง" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="205" height="118" rx="10" class="ac"/><text x="22" y="32" class="sm b tac">Estrogen ค้าง</text>
<text x="22" y="54" class="xs">• Spider angioma (ลำตัว หน้า แขน)</text><text x="22" y="72" class="xs">• Palmar erythema</text><text x="22" y="90" class="xs">• Gynecomastia</text><text x="22" y="108" class="xs">• อัณฑะฝ่อ · ขนร่วง (hypogonadism)</text>
<rect x="225" y="10" width="205" height="118" rx="10" class="ms"/><text x="237" y="32" class="sm b tms">Albumin ต่ำ</text>
<text x="237" y="54" class="xs">• Muehrcke's — แถบขาวคู่ขวาง</text><text x="237" y="72" class="xs">• Terry's — ขาว 2/3 ต้น แดงปลาย</text><text x="237" y="90" class="xs">• บวม · ascites</text><text x="237" y="108" class="xs mu">ไม่จำเพาะ (nephrotic ก็มี)</text>
<rect x="10" y="138" width="205" height="114" rx="10" class="wa"/><text x="22" y="160" class="sm b twa">Portal hypertension</text>
<text x="22" y="182" class="xs">• ม้ามโต (เลือดคั่ง red pulp)</text><text x="22" y="200" class="xs">• Caput medusae</text><text x="22" y="218" class="xs">• Cruveilhier–Baumgarten murmur</text><text x="22" y="236" class="xs">• Ascites · varices</text>
<rect x="225" y="138" width="205" height="114" rx="10" class="bad"/><text x="237" y="160" class="sm b tbad">ตับกำจัดสารไม่ได้</text>
<text x="237" y="182" class="xs">• Jaundice</text><text x="237" y="200" class="xs">• Asterixis (HE)</text><text x="237" y="218" class="xs">• Fetor hepaticus</text><text x="237" y="236" class="xs mu">(dimethyl sulphide)</text>
</svg>"""}

sec("gi-cir-03", "ตรวจร่างกาย — stigmata of chronic liver disease",
    "spider · palmar erythema · Muehrcke/Terry · clubbing/HOA · Dupuytren · gynecomastia · ม้ามโต · caput medusae · fetor · asterixis · parotid",
    10, r"""
### อาการแสดงทีละอย่าง (สไลด์)
| อาการแสดง | ลักษณะ | กลไก/ความสำคัญ |
|---|---|---|
| **Spider angioma** | arteriole ตรงกลาง มีเส้นเล็กแผ่ออก กดตรงกลางแล้วจางหาย · บน **ลำตัว หน้า แขน** (บริเวณที่ SVC ระบาย) | **ฮอร์โมนเพศไม่สมดุล (estrogen)** · **ไม่จำเพาะ** — พบในหญิงตั้งครรภ์ ขาดอาหารรุนแรง คนปกติ (มักไม่เกิน **3 จุด**) |
| **Palmar erythema** | แดงที่ **thenar และ hypothenar eminence** เว้นกลางฝ่ามือ | estrogen · ไม่จำเพาะ — ตั้งครรภ์ **RA · hyperthyroid** · มะเร็งเม็ดเลือด |
| **Muehrcke's nails** | **แถบขาวขวางคู่** คั่นด้วยสีปกติ | **albumin ต่ำ** · พบใน nephrotic ด้วย |
| **Terry's nails** | **2/3 ต้นของเล็บขาว · 1/3 ปลายแดง** | albumin ต่ำ |
| **Clubbing** | มุมระหว่างแผ่นเล็บกับ nail fold **> 180°** ปลายนิ้วเหมือนไม้ตีกลอง | พบบ่อยใน **ตับแข็งจากท่อน้ำดี (biliary)** |
| **Hypertrophic osteoarthropathy (HOA)** | เยื่อหุ้มกระดูกยาวอักเสบเรื้อรัง **ปวดมาก** | ไม่ทราบสาเหตุ |
| **Dupuytren's contracture** | palmar fascia หนาและหดสั้น | พบบ่อยใน **alcoholic cirrhosis** |
| **Gynecomastia** | เต้านมชายโต | **androstenedione** จากต่อมหมวกไตเพิ่ม → แปลงเป็น estrogen |
| **Hypogonadism** | อัณฑะฝ่อ ขนตามตัวลด ความต้องการทางเพศลด | FSH และ LH เปลี่ยน |
| **ขนาดตับ** | โต ปกติ หรือ **เล็กลง** ก็ได้ · **เนื้อแน่นและขรุขระ** | ตับแข็งระยะท้ายมักเล็ก |
| **ม้ามโต** | | เลือดคั่งใน **red pulp** → **hypersplenism** (เกล็ดเลือด เม็ดเลือดขาวต่ำ) |
| **Ascites** | | สัมพันธ์กับ portal pressure |
| **Caput medusae** | หลอดเลือดดำรอบสะดือโป่ง **แผ่ออกจากสะดือ** ไปต่อ systemic vein | **umbilical vein เปิดใหม่** → เลือดพอร์ทัลออกทางผนังหน้าท้อง |
| **Cruveilhier–Baumgarten murmur** | เสียง venous hum ที่ลิ้นปี่/รอบสะดือ | portal vein ต่อกับ umbilical vein |
| **Fetor hepaticus** | ลมหายใจกลิ่นหวานอับ | **dimethyl sulphide** |
| **Jaundice** | | bilirubin สูง |
| **Asterixis** | flapping tremor | **hepatic encephalopathy** |
| **ต่อมพาโรติดโต** | | ไขมันสะสม พังผืด และบวม (มักพบในสุรา) |
| **เบาหวาน** | | พบ **15–30%** ของผู้ป่วยตับแข็ง |
| **Esophageal varices** | | **40–50%** ตามความรุนแรงของโรค |

[[fig:cir_pe]]

### เคล็ดลับตรวจ caput medusae (เพิ่มเติม — ไม่ได้มาจากสไลด์)
ใช้นิ้วรีดเลือดดำใต้สะดือ แล้วดู **ทิศทางการไหลกลับ** — portal hypertension เลือด **ไหลออกจากสะดือ** (ใต้สะดือไหลลง) · **IVC obstruction** เลือดใต้สะดือ **ไหลขึ้น** และเส้นเลือดอยู่ด้านข้างลำตัว
""",
    ["Spider ≤ 3 จุดพบในคนปกติได้ · ยิ่งมากยิ่งชี้โรคตับ",
     "Muehrcke และ Terry = albumin ต่ำ",
     "Clubbing พบบ่อยใน biliary cirrhosis · Dupuytren ในสุรา",
     "Caput medusae = umbilical vein เปิดใหม่",
     "Fetor hepaticus = dimethyl sulphide"],
    [mcq("GI-CIR-MCQ-06",
         "Spider angiomas and palmar erythema in cirrhosis are mainly attributed to which mechanism?",
         ["Portal hypertension with collateral formation", "Hypoalbuminaemia",
          "Altered sex hormone metabolism with relative oestrogen excess",
          "Thrombocytopenia from hypersplenism", "Accumulation of bile acids in the skin"],
         2,
         "สไลด์: ทั้ง spider angioma และ palmar erythema เกิดจาก **ฮอร์โมนเพศไม่สมดุล** — ตับทำลาย estrogen ได้น้อยลง และ androstenedione ถูกแปลงเป็น estrogen ที่เนื้อเยื่อรอบนอกมากขึ้น\n\nทั้งสองอย่าง **ไม่จำเพาะ** — spider พบในหญิงตั้งครรภ์และคนปกติ (มักไม่เกิน 3 จุด) · palmar erythema พบใน RA, hyperthyroid, ตั้งครรภ์",
         "Spider + palmar erythema + gynecomastia = estrogen", "Physical signs"),
     mcq("GI-CIR-MCQ-07",
         "On examination of a cirrhotic patient, the proximal two-thirds of each nail plate is white and the distal third is red-brown. What does this finding indicate?",
         ["Hypoalbuminaemia", "Iron deficiency", "Chronic hypoxaemia", "Psoriatic nail disease", "Copper deposition"],
         0,
         "นี่คือ **Terry's nails** — สไลด์: จาก **albumin ในเลือดต่ำ** · ส่วน **Muehrcke's nails** (แถบขาวขวางคู่) ก็จาก albumin ต่ำเช่นกัน และพบใน nephrotic syndrome ได้\n\nเล็บช้อน (koilonychia) = ขาดเหล็ก · clubbing = hypoxemia เรื้อรัง/biliary cirrhosis · Kayser–Fleischer ring (ที่กระจกตา ไม่ใช่เล็บ) = ทองแดง",
         "Terry's = ขาว 2/3 ต้น · albumin ต่ำ", "Physical signs"),
     mcq("GI-CIR-MCQ-08",
         "Dilated veins radiate from the umbilicus in a patient with cirrhosis. A continuous venous hum is heard over them. Which statement is correct?",
         ["The veins fill from below upward, indicating IVC obstruction",
          "They result from recanalisation of the umbilical vein draining portal blood to abdominal wall veins",
          "They indicate superior vena cava obstruction",
          "The hum is an arterial bruit from hepatocellular carcinoma",
          "They are a sign of right heart failure"],
         1,
         "สไลด์: **caput medusae** = **umbilical vein เปิดใหม่** ให้เลือดพอร์ทัลออกไปที่หลอดเลือดดำผนังหน้าท้อง · เสียง hum ต่อเนื่อง = **Cruveilhier–Baumgarten murmur** (portal vein ต่อกับ umbilical vein)\n\nIVC obstruction เลือดใต้สะดือไหล **ขึ้น** และเส้นอยู่ด้านข้างลำตัว · bruit จาก HCC เป็นเสียงหลอดเลือดแดงเหนือก้อนตับ",
         "Caput medusae ไหลออกจากสะดือ = portal HT", "Physical signs")],
    nl=["2.3.11(4)", "B8.2.5(4)", "2.1.12"],
    figs={"cir_pe": FIG_PE},
    mnem=[{"name": "ABCDEFGHIJ", "what": "stigmata ของโรคตับเรื้อรังที่มือ ลำตัว และใบหน้า (ช่วยไล่ตรวจไม่ให้ขาด)",
           "lines": [["A", "**Asterixis** · Ascites"], ["B", "**Bruising** (ช้ำง่าย)"], ["C", "**Clubbing** · Caput medusae"],
                     ["D", "**Dupuytren's** contracture"], ["E", "**Erythema** (palmar)"], ["F", "**Fetor** hepaticus"],
                     ["G", "**Gynecomastia**"], ["H", "**Hypogonadism** (อัณฑะฝ่อ)"], ["I", "**Icterus** (jaundice)"],
                     ["J", "เล็บ Muehrcke / Terry (albumin ต่ำ)"]],
           "note": "ตรวจไล่จากมือ → แขน → หน้า → อก → ท้อง ตามลำดับเดียวกับ OSCE",
           "src": "หลักจำที่ใช้ทั่วไป (ไม่ได้มาจากสไลด์) · เนื้อหาทุกตัวอยู่ในสไลด์หน้า 6–12"}])


sec("gi-cir-04", "แล็บในตับแข็ง — AST > ALT · A/G กลับข้าง · เกล็ดเลือดต่ำ · Na ต่ำ",
    "AST/ALT สูงปานกลาง AST > ALT · ALP ไม่เกิน 2–3 เท่า · globulin สูงจาก bacterial antigen · ซีด 5 สาเหตุ · เกล็ดเลือดมักไม่ต่ำกว่า 50,000",
    8, r"""
### LFT ในตับแข็ง (สไลด์)
| ค่า | ในตับแข็ง |
|---|---|
| **AST, ALT** | สูง **ปานกลาง** · **AST มักสูงกว่า ALT** · บางรายปกติได้ |
| **ALP** | สูง **ไม่เกิน 2–3 เท่า** · สูงมากใน **PSC และ PBC** |
| **GGT** | สัมพันธ์กับ ALP |
| **Bilirubin** | ระยะแรกปกติ · **สูงขึ้นเมื่อโรคมากขึ้น** |
| **Albumin** | ลดลง · **ช่วยบอกความรุนแรง** |
| **Prothrombin time** | บอกการสร้าง clotting factor · ยาวได้จากเหตุอื่นด้วย — **ท่อน้ำดีอุดตัน ขาดวิตามิน K, DIC, warfarin** |
| **Globulin** | **สูงขึ้น** — reticuloendothelial system ถูกกระตุ้นจาก **bacterial antigen ในเลือดพอร์ทัล** ที่ตับกรองไม่ได้ (โน้ตอาจารย์: จาก plasma cell) |

> **Reverse A/G ratio** (albumin < globulin) คือภาพ LFT ที่เห็นบ่อยที่สุดในตับแข็ง — สไลด์สรุป Diagnosis ว่า **↑AST ALT LDH ALP · ↑bilirubin · coagulopathy · reverse A/G ratio**

### CBC และอื่น ๆ (สไลด์)
| ความผิดปกติ | สาเหตุ |
|---|---|
| **ซีด** | เลือดออกในทางเดินอาหาร · ขาด **เหล็ก โฟเลต** · **สุรากดไขกระดูก** · **hypersplenism** · anemia of chronic disease · hemolysis |
| **เกล็ดเลือดต่ำ** | **ม้ามโต** — แต่ **มักไม่ต่ำกว่า 50,000/µL** · ต่ำกว่านี้ให้หาเหตุอื่น เช่น **DIC** |
| **เม็ดเลือดขาวต่ำ** | ม้ามโตและทำงานมากเกิน |
| **PT ยาว** | ขาด **factor VII** (ครึ่งชีวิตสั้นสุด) · เหตุอื่น: DIC, fibrinolysis, ขาดวิตามิน K, dysfibrinogenemia, เกล็ดเลือดต่ำ |
| **Na ต่ำ** | ขับน้ำไม่ได้ เพราะ **ADH หลั่งมากเกิน** (non-osmotic จาก effective arterial volume ต่ำ) |

### ทำไม AST > ALT ในตับแข็ง (เพิ่มเติม — เชื่อมคาบ LFT)
ตับแข็งเคลียร์ AST ออกจากเลือดได้ช้าลง (sinusoid เปลี่ยนเป็น capillary) · สุรายังทำให้ขาด **pyridoxal-5'-phosphate** ซึ่ง ALT ต้องใช้มากกว่า · ดังนั้น **AST/ALT > 1 ชี้ว่ามีพังผืดมากแล้ว** และ **> 2 ชวนนึกถึงสุรา**
""",
    ["AST > ALT · ALP ≤ 2–3 เท่า (ยกเว้น PBC/PSC)",
     "Globulin สูงจาก bacterial antigen ในเลือดพอร์ทัล → A/G กลับข้าง",
     "เกล็ดเลือดจากม้ามโตมักไม่ต่ำกว่า 50,000",
     "Na ต่ำ = ADH หลั่งมาก ขับน้ำไม่ได้"],
    [mcq("GI-CIR-MCQ-09",
         "Why is serum globulin typically raised in cirrhosis?",
         ["Increased hepatic synthesis of globulin to compensate for low albumin",
          "Haemoconcentration from diuretic therapy",
          "Stimulation of the reticuloendothelial system by bacterial antigens in portal venous blood that bypass hepatic clearance",
          "Monoclonal gammopathy present in most cirrhotic patients",
          "Reduced renal excretion of immunoglobulins"],
         2,
         "สไลด์: globulin สร้างจาก **reticuloendothelial system (plasma cell)** และ **สูงขึ้นในตับแข็งจากการกระตุ้นของ bacterial antigen ในเลือดพอร์ทัล** ซึ่งปกติตับ (Kupffer cell) จะกรองออก แต่ในตับแข็งเลือดอ้อมผ่าน shunt\n\nตับ **ไม่ได้สร้าง immunoglobulin** · globulin ที่สูงในตับแข็งเป็นแบบ polyclonal",
         "Globulin ↑ = antigen จากลำไส้หลุดผ่านตับ", "Laboratory"),
     mcq("GI-CIR-MCQ-10",
         "A patient with known cirrhosis and splenomegaly has a platelet count of 22,000/µL, prolonged PT and aPTT, low fibrinogen and schistocytes on the blood smear. What is the best interpretation?",
         ["Expected hypersplenism of cirrhosis", "Vitamin K deficiency", "Another process such as DIC should be sought",
          "Isolated factor VII deficiency", "Pseudothrombocytopenia from EDTA"],
         2,
         "สไลด์: เกล็ดเลือดต่ำจาก **ม้ามโตในตับแข็งมักไม่ต่ำกว่า 50,000/µL** → 22,000 ร่วมกับ fibrinogen ต่ำและ **schistocyte** ต้องหาเหตุอื่น โดยเฉพาะ **DIC** (สไลด์ระบุ DIC เป็นสาเหตุของเกล็ดเลือดต่ำและ PT ยาวในตับแข็ง)\n\nขาดวิตามิน K ไม่ทำให้เกล็ดเลือดต่ำหรือเกิด schistocyte",
         "เกล็ดเลือด < 50,000 ในตับแข็ง → หาเหตุอื่น", "Laboratory",
         nl=["2.3.11(4)", "2.2.20", "2.3.3(1)"])],
    nl=["2.3.11(4)", "B8.3(1)", "2.3.3(1)", "B2.2.5(2)"])


sec("gi-cir-05", "ภาพถ่ายรังสี ยืนยันตับแข็ง และหาสาเหตุ",
    "US/CT/MRI แต่ละแบบเด่นอะไร · biopsy มาตรฐานแต่ sampling error · liver stiffness ไม่ต้องเจาะแต่จำกัดในคนอ้วน/ascites · ตารางตรวจหาสาเหตุ 9 โรค",
    9, r"""
### ภาพถ่ายรังสี (สไลด์)
| วิธี | ข้อดี | ข้อเสีย |
|---|---|---|
| **อัลตราซาวนด์** | ทำง่าย **ไม่มีรังสี ไม่ใช้สารทึบแสง** · ดี portal vein ม้ามโต collateral HCC (Colour Doppler ดูการไหลได้) | ความไววินิจฉัยตับแข็ง **ต่ำ** · จำกัดใน **คนอ้วน · ileus** |
| **CT** | **ดีกว่าในการหามะเร็งตับ** | ได้รังสีและสารทึบแสง · แพงกว่า |
| **MRI** | **แยกก้อนในตับว่ามะเร็งหรือเนื้องอกอื่นได้ดี** · บางการศึกษาบอกความรุนแรงตับแข็งและ **ภาวะเหล็กเกิน** ได้ | แพงและใช้เวลานาน |

ลักษณะตับแข็งบน US (เพิ่มเติม): ผิวตับขรุขระ (nodular surface) · **caudate lobe โต** เทียบ right lobe · ม้ามโต · portal vein กว้าง/ไหลย้อนทาง · ascites

### ยืนยันว่าเป็นตับแข็ง (สไลด์)
| วิธี | ข้อดี | ข้อเสีย |
|---|---|---|
| **Liver biopsy** | **ดีที่สุด** ความไว 80–100% · **หาสาเหตุได้ด้วย** — hemochromatosis · NASH · Wilson · α1-antitrypsin deficiency | **sampling error** (ตับแข็งกระจายไม่สม่ำเสมอ) · มีภาวะแทรกซ้อน (เลือดออก) |
| **Liver stiffness (elastography)** | บอกความรุนแรงพังผืดและตับแข็ง **โดยไม่ต้องเจาะชิ้นเนื้อ** | จำกัดใน **คนอ้วน · ช่องซี่โครงแคบ · มีน้ำในช่องท้อง** |

**เพิ่มเติม (Baveno VII 2022)**: liver stiffness **≥ 15 kPa** ชวนให้นึกถึง compensated advanced chronic liver disease · **< 10 kPa** แทบตัดออก · **≥ 25 kPa** = มี clinically significant portal hypertension

### ตรวจหาสาเหตุ (สไลด์)
| โรค | ประวัติ | ตรวจเพิ่ม |
|---|---|---|
| **Alcoholic liver disease** | ดื่มสุราประจำ | **AST > ALT แต่มักไม่เกิน 300 IU/L** |
| **Chronic hepatitis B** | รับเลือด · โรคตับในครอบครัว | **HBsAg · HBeAg · HBV DNA** |
| **Chronic hepatitis C** | รับเลือด · สัก | **anti-HCV · HCV RNA** |
| **NASH (MASH)** | metabolic syndrome · ตัดสุราและสาเหตุอื่นแล้ว | US ตับ · ชิ้นเนื้อตับ |
| **Autoimmune hepatitis** | มีโรคภูมิต้านตนเองอื่น | **ANA · ASMA · anti-LKM-1** |
| **PBC** | อ่อนเพลีย **คัน ผิวคล้ำ** | **ALP สูง · AMA** |
| **PSC** | คัน · steatorrhea · ขาดวิตามินละลายในไขมัน | **ERCP หรือ MRCP** |
| **Hereditary hemochromatosis** | ตับแข็งในครอบครัว **ผิวคล้ำ เบาหวาน pseudogout หัวใจโต** | **transferrin saturation > 60% (ชาย) / > 50% (หญิง)** · hepatic iron index ≥ 1.9 |
| **Wilson disease** | ตับแข็งในครอบครัว · อาการทาง **ประสาท เลือด ไต** | **ceruloplasmin ต่ำ** · ทองแดงในเนื้อตับสูง |
""",
    ["US: ทำง่าย ไม่มีรังสี แต่ไวต่ำ · CT ดีสุดหามะเร็ง · MRI แยกชนิดก้อน",
     "Biopsy = มาตรฐาน + หาสาเหตุ แต่ sampling error",
     "Elastography จำกัดใน อ้วน · ช่องซี่โครงแคบ · ascites",
     "Alcohol: AST > ALT แต่ < 300",
     "HH: transferrin sat > 60% ชาย / > 50% หญิง"],
    [mcq("GI-CIR-MCQ-11",
         "Transient elastography is planned to stage fibrosis. Which situation most limits its reliability, according to the lecture?",
         ["Chronic hepatitis B with normal ALT", "Previous cholecystectomy", "Moderate ascites",
          "Use of proton-pump inhibitors", "Age over 60 years"],
         2,
         "สไลด์: การวัดความแข็งตับมีข้อจำกัดใน **คนอ้วน · ช่องระหว่างซี่โครงแคบ · มีน้ำในช่องท้อง** (คลื่นส่งผ่านน้ำได้ไม่ดี)\n\nเพิ่มเติม: ค่าสูงเกินจริงได้เมื่อ ALT สูงมาก (ตับอักเสบ) ตับคั่งเลือด ท่อน้ำดีอุดตัน และกินอาหารก่อนตรวจ",
         "Elastography: อ้วน · ซี่โครงแคบ · ascites", "Investigation"),
     mcq("GI-CIR-MCQ-12",
         "A 52-year-old man has cirrhosis, diabetes, bronze skin, chondrocalcinosis and cardiomegaly. Which test is the best initial screen for the underlying cause?",
         ["Serum ceruloplasmin", "Antimitochondrial antibody", "Transferrin saturation",
          "Alpha-1 antitrypsin level", "Anti-smooth muscle antibody"],
         2,
         "ตับแข็ง + **เบาหวาน + ผิวคล้ำ + pseudogout (chondrocalcinosis) + หัวใจโต** = **hereditary hemochromatosis** · สไลด์: ตรวจ **transferrin saturation > 60% ในชาย / > 50% ในหญิง** และ hepatic iron index ≥ 1.9\n\nceruloplasmin = Wilson (อายุน้อย อาการทางประสาท) · AMA = PBC · ASMA = AIH",
         "Bronze diabetes + ตับแข็ง → transferrin saturation", "Etiology work-up"),
     mcq("GI-CIR-MCQ-13",
         "A 40-year-old man who drinks heavily has AST 640 U/L and ALT 520 U/L. Why does this pattern argue against alcohol as the sole cause?",
         ["Alcohol causes ALT to exceed AST", "In alcohol-related liver injury AST rarely exceeds about 300 IU/L",
          "Alcohol never raises aminotransferases", "AST:ALT ratio below 3 excludes alcohol", "GGT must be normal in alcohol injury"],
         1,
         "สไลด์ตารางหาสาเหตุ: alcoholic liver disease — **AST > ALT แต่ระดับมักไม่เกิน 300 IU/L** · ค่า AST 640 จึงต้องหาสาเหตุอื่นร่วม เช่น **ไวรัสตับอักเสบ · ยา (รวม paracetamol ที่คนดื่มสุราไวต่อพิษ) · ตับขาดเลือด**\n\nใน alcohol ปกติ AST/ALT > 2 และ GGT สูง",
         "สุรา AST > 300 → หาเหตุอื่นร่วม", "Etiology work-up",
         nl=["2.3.11(2)", "B8.3(1)"])],
    nl=["2.3.11(4)", "B8.2.5(4)", "B8.3(1)", "2.3.11(2)"])
