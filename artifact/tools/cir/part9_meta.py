# -*- coding: utf-8 -*-
# ข้อมูลคาบ + MEQ + OSCE + คำอธิบายชุด GI

LEC_NAME = "Liver cirrhosis and complications (ผศ.สยาม)"

MEQ1 = {
 "id": "GI-CIR-MEQ-01", "part": "MEQ", "lec": "3/11", "lecture": LEC_NAME,
 "topic": "Decompensated alcoholic cirrhosis — fever, confusion and worsening ascites (SBP, HE, HRS)",
 "vignette": "ผู้ป่วยชายไทยอายุ 54 ปี ดื่มสุราขาววันละครึ่งขวดมา 20 ปี มาด้วยท้องโตขึ้น 1 เดือน ไข้ต่ำ ปวดท้องทั่ว ๆ 3 วัน วันนี้ญาติสังเกตว่าพูดสับสน นอนกลางวันมากผิดปกติ ถ่ายอุจจาระครั้งสุดท้าย 4 วันก่อน\nPE: BT 37.9 °C · BP 98/60 · HR 104 · RR 20 · ซึม ตอบช้า สับสนเวลา · ตาเหลือง · spider angioma ที่หน้าอก 6 จุด · palmar erythema · gynecomastia · ท้องโต shifting dullness บวก กดเจ็บทั่วท้องเล็กน้อย · ม้ามโต 3 ซม. · asterixis บวก · ขาบวมกดบุ๋ม 2+\nLab: Hb 9.8 g/dL · WBC 12,400 · plt 68,000 · albumin 2.4 g/dL · globulin 4.6 g/dL · TB 4.2 mg/dL · AST 96 · ALT 41 U/L · INR 1.9 · Na 128 · K 3.1 mmol/L · BUN 32 · Cr 1.6 mg/dL (2 เดือนก่อน 0.9)",
 "questions": [
  {"q": "1. จงบอกปัญหาของผู้ป่วยรายนี้ให้ครบ และประเมิน Child-Pugh (3 คะแนน)",
   "a": "- **Decompensated alcoholic cirrhosis** (stigmata + ม้ามโต + A/G กลับข้าง + AST/ALT > 2)\n- **Ascites** · **สงสัย SBP** (ไข้ ปวดท้อง กดเจ็บ ใน ascites) · **Hepatic encephalopathy grade 2** (สับสนเวลา asterixis)\n- **AKI** (Cr 0.9 → 1.6) สงสัย prerenal/HRS-AKI · **Hyponatremia · hypokalemia**\n- **Child-Pugh**: ascites ปานกลาง 3 · bilirubin > 3 = 3 · albumin < 2.8 = 3 · INR 1.7–2.3 = 2 · HE grade 1–2 = 2 → **13 คะแนน = Child C**"},
  {"q": "2. จงบอกการตรวจที่ต้องทำทันทีเพื่อยืนยันภาวะติดเชื้อในช่องท้อง และเกณฑ์วินิจฉัย (3 คะแนน)",
   "a": "- **Diagnostic paracentesis ทันที** (ไม่ต้องรอแก้ INR/เกล็ดเลือด): **cell count + differential · albumin (คำนวณ SAAG) · total protein · Gram stain · culture ในขวด hemoculture ข้างเตียง** ± glucose LDH\n- **SBP = PMN ≥ 250/mm³** (± culture บวกเชื้อชนิดเดียว) · PMN ≥ 250 culture ลบ = CNNA รักษาเหมือนกัน\n- นึกถึง **secondary peritonitis** ถ้า PMN > 10,000 · เชื้อหลายชนิด · 2 ใน 3 ของ glucose < 50 / protein > 1 / LDH > ค่าเลือด\n- hemoculture · urine culture · CXR"},
  {"q": "3. ผล PMN 820/mm³ จงบอกการรักษาภาวะติดเชื้อและการป้องกันไตวาย (3 คะแนน)",
   "a": "- **Cefotaxime 2 g IV q8h** (หรือ ceftriaxone) **5–7 วัน**\n- **Albumin 1.5 g/kg ภายใน 6 ชม. วันที่ 1 และ 1 g/kg วันที่ 3** → ลด HRS และอัตราตาย (ผู้ป่วยรายนี้ Cr > 1, TB > 4 เสี่ยงสูง)\n- **หยุด diuretic · NSBB (BP 98/60) · NSAIDs/ยาพิษต่อไต**\n- เจาะซ้ำที่ 48 ชม. ถ้าไม่ดีขึ้น · หลังหายให้ **secondary prophylaxis** (norfloxacin/ciprofloxacin) ตลอด"},
  {"q": "4. จงบอกการดูแลภาวะซึมของผู้ป่วย (3 คะแนน)",
   "a": "- **ตัดโรคอื่น**: เจาะ **น้ำตาลปลายนิ้ว** · CT สมองถ้าล้ม/อาการเฉพาะที่ (subdural) · ระวัง Wernicke ในคนดื่มสุรา → **thiamine ก่อน glucose**\n- **แก้ตัวเร่ง**: **SBP** (กำลังรักษา) · **ท้องผูก 4 วัน** · **K ต่ำ** แก้ K · หาเลือดออกทางเดินอาหาร (PR exam) · หยุดยานอนหลับ diuretic\n- **Lactulose 30–60 mL ทุก 1 ชม. จนถ่าย** แล้วปรับให้ **ถ่ายนิ่ม 2–4 ครั้ง/วัน** (หรือสวนด้วย lactulose ถ้ากินไม่ได้) · ป้องกันสำลัก\n- หลังดีขึ้นพิจารณา **rifaximin** ป้องกันซ้ำ · **ไม่จำกัดโปรตีน** (1.2–1.5 g/kg/วัน)"},
  {"q": "5. หลังรักษา 3 วัน ไข้ลง แต่ Cr 2.6 mg/dL ปัสสาวะ 300 mL/วัน urinalysis ปกติ US ไตปกติ จงบอกการวินิจฉัยและการรักษา (3 คะแนน)",
   "a": "- **Hepatorenal syndrome (HRS-AKI / type I)** — ไตวายเร็วในตับแข็งขั้นสูง ตัวกระตุ้นคือ **SBP** · ปัสสาวะ bland (RBC < 50, protein < 500) · ไม่มี shock/ยาพิษต่อไต/obstruction · ต้องไม่ดีขึ้นหลัง **หยุด diuretic + albumin 1 g/kg/วัน 2 วัน**\n- **Terlipressin + albumin 20–40 g/วัน** (ไม่มี → norepinephrine ใน ICU หรือ midodrine + octreotide + albumin)\n- **ส่งพิจารณาเปลี่ยนตับ** (Child C · MELD สูง · HRS) — การรักษาหายจริง · ต้องหยุดสุราได้"}
 ],
 "ref": [SRC, "AASLD Practice Guidance: ascites, SBP and HRS (2021)", "AASLD/EASL: Hepatic encephalopathy (2014) · EASL CPG HE (2022)"],
 "nl": ["2.3.11(4)", "2.3.11-3(10)", "2.3.6(6)", "2.3.11-3(7)", "B8.3(4)"],
 "years": [], "_kind": "meq", "_set": "gi"}

MEQ2 = {
 "id": "GI-CIR-MEQ-02", "part": "MEQ", "lec": "3/11", "lecture": LEC_NAME,
 "topic": "Acute variceal haemorrhage in HBV cirrhosis — resuscitation, endoscopy and secondary prophylaxis",
 "vignette": "ผู้ป่วยหญิงไทยอายุ 48 ปี ทราบว่าเป็นพาหะไวรัสตับอักเสบบีมานาน ไม่เคยรักษา มาห้องฉุกเฉินด้วยอาเจียนเป็นเลือดสด 2 ครั้ง ประมาณ 1 ชาม และถ่ายดำ 1 ครั้ง\nPE: BP 86/50 · HR 124 · ซีด ตาเหลืองเล็กน้อย · spider angioma · ม้ามโต · ascites เล็กน้อย · รู้สึกตัวดี\nLab: Hb 6.8 g/dL · plt 72,000 · INR 1.6 · albumin 3.0 · TB 2.2 mg/dL · Cr 1.0",
 "questions": [
  {"q": "1. จงบอกการวินิจฉัยที่น่าจะเป็นที่สุด และการดูแลเบื้องต้นที่ห้องฉุกเฉิน (4 คะแนน)",
   "a": "- **Acute variceal hemorrhage** จาก **portal hypertension ในตับแข็งจาก HBV** (Child B: ascites น้อย 2 + bilirubin 2–3 = 2 + albumin 2.8–3.5 = 2 + INR < 1.7 = 1 + HE ไม่มี 1 = **8**)\n- **ABC**: เปิด IV เส้นใหญ่ 2 เส้น · ป้องกันสำลัก (intubate ถ้าซึม/อาเจียนมาก) · ให้สารน้ำพอให้ BP ขึ้น\n- **ให้เลือดเป้า Hb ~8 g/dL** (ไม่เกิน — เพิ่ม portal pressure) · **ไม่ให้ FFP แก้ INR**\n- **Vasoactive ทันที**: terlipressin หรือ octreotide/somatostatin · **ยาปฏิชีวนะป้องกัน: ceftriaxone 1 g/วัน** (ลดการติดเชื้อ เลือดออกซ้ำ และอัตราตาย) · PPI ได้จนกว่าจะส่องกล้อง"},
  {"q": "2. จงบอกการส่องกล้องที่ควรทำและเวลาที่เหมาะสม (2 คะแนน)",
   "a": "- **Upper endoscopy ภายใน 12 ชม.** หลัง resuscitate · **esophageal varices → EVL (band ligation)** · **gastric varices → cyanoacrylate**\n- ควบคุมไม่ได้หรือออกซ้ำเร็ว → **balloon tamponade เป็นสะพาน → rescue TIPS** · เสี่ยงสูง (Child C 10–13 / B > 7 ที่ยังออกขณะส่อง) → **pre-emptive TIPS ภายใน 72 ชม.**"},
  {"q": "3. หลังเลือดหยุด จงบอกการป้องกันเลือดออกซ้ำ และการดูแลระยะยาวของตับแข็ง (4 คะแนน)",
   "a": "- **NSBB (propranolol/nadolol หรือ carvedilol) + EVL ซ้ำทุก 2–4 สัปดาห์จน varices หมด** · ล้มเหลว → TIPS\n- **รักษาสาเหตุ: ยาต้าน HBV (tenofovir หรือ entecavir) ตลอด** — ชะลอและอาจทำให้ตับดีขึ้น\n- **คัดกรอง HCC: US ± AFP ทุก 6 เดือน**\n- **วัคซีน HAV · ไข้หวัดใหญ่ · pneumococcus** · หลีกเลี่ยงสุรา สมุนไพร NSAIDs · paracetamol ≤ 2 g/วัน\n- ascites: จำกัดเกลือ ± spironolactone/furosemide · **ประเมินส่งเปลี่ยนตับ** (decompensated, Child B)"}
 ],
 "ref": [SRC, "Baveno VII consensus (2022)", "AASLD Guidance: varices and variceal hemorrhage (2024)"],
 "nl": ["2.3.11(4)", "B8.2.2-3(7)", "B8.4(2)", "2.1.16", "2.2.44"],
 "years": [], "_kind": "meq", "_set": "gi"}

OSCE1 = {
 "id": "GI-CIR-OSCE-01", "part": "OSCE/SAQ", "lec": "3/11", "lecture": LEC_NAME,
 "topic": "OSCE – Physical examination for stigmata of chronic liver disease and ascites",
 "station": "OSCE (ตรวจร่างกาย + รายงานผล) 6 นาที · ผู้ป่วยจำลองหรือหุ่น",
 "instruction": "ผู้ป่วยชายอายุ 55 ปี ดื่มสุรามานาน มาด้วยท้องโตขึ้น 2 เดือน\n\n**จงทำสิ่งต่อไปนี้**\n1. ตรวจร่างกายเพื่อหาอาการแสดงของโรคตับเรื้อรังและ portal hypertension อย่างเป็นระบบ\n2. ตรวจหาน้ำในช่องท้องและม้ามโต\n3. รายงานผลตรวจแยกตามกลไก (portal hypertension กับ liver insufficiency) ภายใน 1 นาที",
 "answer": "| หัวข้อ | สิ่งที่ต้องทำ/พูด | คะแนน |\n|---|---|---|\n| **แนะนำตัว ขออนุญาต ล้างมือ จัดท่า** | นอนหงายราบ เปิดหน้าท้องตั้งแต่ใต้ราวนมถึงขาหนีบ (คลุมส่วนอื่น) · ยืนขวาผู้ป่วย | 1 |\n| **มือ** | **palmar erythema** (thenar/hypothenar) · **Muehrcke's/Terry's nails** · **clubbing** · **Dupuytren's** · **asterixis** (เหยียดแขน กระดกข้อมือ 30 วินาที) | 2 |\n| **แขน หน้า ตา** | **spider angioma** (กดตรงกลางแล้วจาง · นับจำนวน) · รอยช้ำ · **icterus** · parotid โต · **fetor hepaticus** | 1 |\n| **อก** | **gynecomastia** · ขนรักแร้/หน้าอกลด · spider บริเวณที่ SVC ระบาย | 1 |\n| **ท้อง — ดู/ฟัง** | ท้องโต สะดือจุ่น · **caput medusae** + ตรวจทิศเลือด (ไหลออกจากสะดือ) · ฟัง **venous hum (Cruveilhier–Baumgarten)** | 1 |\n| **คลำตับ ม้าม** | คลำจากหน้าท้องขวาล่างขึ้นตามจังหวะหายใจ · **ตับแข็ง ขรุขระ อาจเล็กหรือโต** · **ม้ามโต** (คลำจากขวาล่างไปซ้ายบน · ถ้ามี ascites ใช้ dipping) | 2 |\n| **ตรวจน้ำในช่องท้อง** | **เคาะ flank dullness** → **shifting dullness** (ตะแคงรอ 30 วินาที เคาะซ้ำ) · ascites มาก → **fluid thrill** (ให้ผู้ช่วยวางสันมือกลางท้อง) | 2 |\n| **อื่น ๆ** | **ขาบวมกดบุ๋ม** · อัณฑะฝ่อ (ขออนุญาต/ระบุว่าจะตรวจ) · **บอกว่าจะ PR** ดูถ่ายดำ | 1 |\n| **รายงาน 1 นาที** | “มี **stigmata of chronic liver disease** ได้แก่ … · **portal hypertension**: ม้ามโต caput medusae **ascites (shifting dullness บวก)** · **liver insufficiency**: jaundice spider palmar erythema gynecomastia · **ไม่มี/มี asterixis** → เข้าได้กับ **decompensated cirrhosis** แนะนำ diagnostic paracentesis” | 2 |\n| **ขอบคุณ คลุมผ้า** | | 1 |\n\n**รวม 14 คะแนน** · จุดที่ทำให้ตก: ไม่ตรวจ asterixis · ตรวจ shifting dullness ไม่รอให้น้ำไหล · คลำม้ามจากซ้ายบนลงมา (พลาดม้ามโตมาก)",
 "ref": [SRC + " หน้า 6–12", "Macleod's Clinical Examination — abdominal examination"],
 "nl": ["2.3.11(4)", "2.1.12", "2.1.13"],
 "years": [], "_kind": "meq", "_set": "gi"}

LECTURE = {
 "lec": "3/11",
 "date": "อ. 3 พ.ย.",
 "title": "Liver cirrhosis and complications",
 "subtitle": "นิยามและสาเหตุ · stigmata · แล็บ ภาพถ่าย และยืนยันพังผืด · Child-Pugh MELD พยากรณ์ · portal hypertension · hepatic encephalopathy · varices และเลือดออกเฉียบพลัน · ascites SAAG และ LVP + albumin · SBP · hepatorenal syndrome · HCC HPS และข้อบ่งชี้เปลี่ยนตับ",
 "objectives": [
  "อธิบายนิยาม พยาธิกำเนิด และสาเหตุของตับแข็ง รวมทั้งแยก micronodular กับ macronodular",
  "แยก compensated กับ decompensated cirrhosis และตรวจร่างกายหา stigmata of chronic liver disease พร้อมอธิบายกลไก",
  "แปลผลแล็บ ภาพถ่ายรังสี และเลือกการตรวจหาสาเหตุของตับแข็ง",
  "คำนวณ Child-Pugh บอกพยากรณ์โรค และรู้จัก MELD",
  "อธิบายกลไก portal hypertension และกฎของ Laplace กับการแตกของ varices",
  "วินิจฉัยและรักษา hepatic encephalopathy โดยหาตัวเร่งและใช้ lactulose อย่างถูกต้อง",
  "วางแผนป้องกันเลือดออกจาก varices ครั้งแรก รักษาเลือดออกเฉียบพลัน และป้องกันซ้ำ",
  "เจาะตรวจน้ำในช่องท้อง แปลผล SAAG และรักษา ascites รวมถึงการให้ albumin หลัง LVP",
  "วินิจฉัยและรักษา SBP แยก secondary peritonitis และป้องกัน",
  "วินิจฉัยและรักษา hepatorenal syndrome",
  "บอกการดูแลทั่วไป คัดกรอง HCC รู้จัก hepatopulmonary syndrome และข้อบ่งชี้ผ่าตัดเปลี่ยนตับ"
 ],
 "nlGap": "เกณฑ์ฯ มีรหัส `นล. 2.3.11(4)` Cirrhosis (กลุ่ม 2) · `2.3.11(2)` Alcoholic liver disease · `2.3.11-3(7)` Hepatic failure · `2.3.11-3(10)` Peritonitis · `2.3.6(6)` hepatic encephalopathy · `B8.2.2-3(7)` Esophageal varices · `B8.4(2)` Drugs used in variceal bleeding · `B8.3(4)` Ascitic fluid analysis แต่ **ไม่มีรหัสเฉพาะของ hepatorenal syndrome, hepatopulmonary syndrome หรือ MELD** และสไลด์ (เนื้อหาส่วนใหญ่อ้างงานวิจัยปี 1988–2003) **ไม่ได้ระบุขนาดยา vasoactive, ยาปฏิชีวนะใน SBP, ขนาด diuretic, rifaximin หรือนิยาม HRS-AKI ฉบับใหม่** จึงเสริมจากแนวทางด้านล่าง โดยระบุ “เพิ่มเติม — ไม่ได้มาจากสไลด์” ทุกจุด",
 "guidelines": [
  "**สไลด์ ผศ.สยาม ศิรินธรปัญญา (Lec Cirrhosis and complication Rx.pdf · 51 หน้า · GI unit รพ.ราชวิถี)** — ต้นฉบับหลักของคาบ",
  "**Baveno VII — Renewing consensus in portal hypertension (J Hepatol 2022)** — cACLD, liver stiffness, CSPH, carvedilol, pre-emptive TIPS",
  "**AASLD Practice Guidance: Risk stratification and management of portal hypertension and varices (2024)**",
  "**AASLD Practice Guidance: Diagnosis, evaluation and management of ascites, SBP and hepatorenal syndrome (2021)** — ขนาด diuretic, albumin, cefotaxime",
  "**EASL Clinical Practice Guidelines for decompensated cirrhosis (2018)**",
  "**AASLD/EASL Practice Guideline: Hepatic encephalopathy (2014)** และ **EASL CPG on HE (2022)** — West Haven, rifaximin, โปรตีน 1.2–1.5 g/kg",
  "**International Club of Ascites — HRS-AKI criteria (2015, ปรับปรุง 2024)**"
 ],
 "meq": [MEQ1, MEQ2],
 "osce": [OSCE1]
}

GI_INTRO = ("ชุดระบบทางเดินอาหาร ตับ และทางเดินน้ำดี มี 5 คาบ — **Acute and chronic hepatitis (อ.เฉลิมรัฐ 12 ต.ค.)** ไวรัสตับอักเสบ ผลเลือด HBV การรักษา HBV HCV MASLD · "
            "**Approach to abdominal pain (นพ.กิตติ 27 ต.ค.)** visceral/parietal pain, IBS, dyspepsia, นิ่วถุงน้ำดี ตับอ่อนอักเสบ ลำไส้อุดตันและขาดเลือด · "
            "**Liver function tests (นพ.กิตติ 29 ต.ค.)** รูปแบบ LFT, R ratio, cholestasis, ALP/GGT และขั้นตอนดูแลผู้ป่วยเหลือง · "
            "**Diarrhea — acute และ chronic (พญ.ธันยพร · Bedside 27 ต.ค.)** นิยามและโรคเลียนแบบ กลไกของเชื้อ approach ท้องเสียเฉียบพลัน ORS ยาปฏิชีวนะ ท้องเสียเรื้อรังแบบ fatty/watery/bloody stool osmotic gap และ IBS · "
            "**Liver cirrhosis and complications (ผศ.สยาม 3 พ.ย.)** stigmata Child-Pugh portal hypertension HE varices ascites SAAG SBP HRS และเปลี่ยนตับ "
            "จบแต่ละหัวข้อมีข้อสอบเช็คความเข้าใจทันที")

GI_HOWTO = ("**วิธีใช้** — อ่านเนื้อหาให้จบแล้วตอบข้อสอบท้ายหัวข้อ ระบบเฉลยพร้อมคำอธิบายกลไกทันทีที่ตอบ · ข้อที่ตอบผิดรวมอยู่ในแท็บ **ทบทวนข้อที่ผิด** · จบคาบแล้วฝึก **MEQ** และ **OSCE/SAQ** ต่อ\n\n"
            "**ลำดับที่แนะนำ** — เรียน **LFT ก่อน** (ภาษากลางของโรคตับ) แล้วต่อ **Hepatitis** (หัวข้อ 3 ตารางผลเลือด HBV ออกสอบบ่อยที่สุด) → **Cirrhosis** (ปลายทางของโรคตับเรื้อรังทุกสาเหตุ · ภาวะแทรกซ้อน SBP HE HRS และ varices ออกสอบ MEQ บ่อย) และ **Abdominal pain** (สเปกตรัมนิ่วถุงน้ำดีและตับอ่อนอักเสบ) · **Diarrhea** ต่อจาก Abdominal pain (IBS ซ้ำกันสองคาบ — คาบนี้เน้นเกณฑ์และการรักษาตามแนวทางไทย 2022)\n\n"
            "**หมายเหตุ** — ชุด GI ยังไม่มีคลังข้อสอบเก่ารายคาบใน Ward Drill จึงผูกข้อจาก Mock exam หมวด GI ที่ตรงเรื่องแทน · ข้อความที่ไม่ได้มาจากสไลด์มีระบุไว้ทุกจุด")
