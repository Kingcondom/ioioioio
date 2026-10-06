from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Nephro"

# ---------------------------------------------------------------- 09-01 UTI dx
S1 = sec("nephro-09-01", "UTI: เชื้อ อาการ และการส่งตรวจ",
    "E. coli อันดับ 1 · upper (ไข้ ปวดเอว CVA) vs lower (ไม่มีไข้) · pyuria + LE/nitrite · C/S และ imaging เมื่อไร", minutes=7,
    source=f"{D} หน้า 277–279, 283–286, 295–296", nl=["2.3.14(7)", "2.3.14(14)", "B9.2.2(2)"],
    md='''
### เชื้อก่อโรค

- ***E. coli*** (อันดับ 1), ***S. saprophyticus*** (หญิงวัยเจริญพันธุ์ เพศสัมพันธ์), ***K. pneumoniae***, ***Proteus mirabilis***
- Proteus สร้าง **urease** → แยก urea เป็น NH3 → **ปัสสาวะเป็นด่าง (pH > 7)** + นิ่ว struvite (staghorn) (เสริม)

### อาการ

| Upper UTI (pyelonephritis) | Lower UTI (cystitis, prostatitis, urethritis) |
|---|---|
| **Fever**, N/V | Urgency, frequency |
| **Flank pain, CVA tenderness** | Dysuria, suprapubic pain |
| ± อาการ lower UTI | **มักไม่มี fever** |

> Prostatitis ในผู้ชายมีไข้ได้ ต่อมลูกหมากกดเจ็บ (เสริม)

### Investigation

**UA**
- **WBC > 5 cells/HPF**, WBC cast (WBC cast = การอักเสบในไต → pyelonephritis)
- RBC, bacteria, **leukocyte esterase +**
- **Nitrite +** (เฉพาะเชื้อ Enterobacteriaceae ที่เปลี่ยน nitrate → nitrite; Enterococcus/S. saprophyticus ให้ผลลบ (เสริม))

**Urine G/S, C/S** กรณี
- Pyelonephritis/complicated UTI
- อาการนาน **> 7 วัน**
- Treatment failure
- Recurrent UTI (**2 ครั้งใน 6 เดือน หรือ 3 ครั้งใน 1 ปี**)
- **Pregnancy**

**Imaging** กรณี
- **Pyelonephritis ที่ไม่ดีขึ้นใน 72 ชั่วโมง**
- Recurrent UTI
- Immunocompromised
- **Male**

| Imaging | ใช้หา |
|---|---|
| Plain KUB | นิ่ว (radio-opaque) |
| **U/S KUB** | **Renal abscess, hydronephrosis** (ตรวจแรกที่ปลอดภัย) |
| CT KUB | ละเอียดที่สุด (emphysematous pyelonephritis, abscess, นิ่ว) |
''',
    pearls=[
        "UTI: E. coli อันดับ 1 · ปัสสาวะด่าง (pH ≥7.5) → Proteus",
        "Upper UTI = ไข้ + ปวดเอว/CVA · lower UTI มักไม่มีไข้",
        "UA: WBC >5/HPF + LE + nitrite (Enterobacteriaceae) · WBC cast = pyelonephritis",
        "C/S: pyelo/complicated, >7 วัน, failure, recurrent, pregnancy",
        "Imaging: pyelo ไม่ดีขึ้น 72 ชม., recurrent, immunocompromised, ผู้ชาย → U/S KUB",
    ],
    items=[
        mcq("NEPHRO-09-01-1",
            "A 50-year-old woman presents with acute fever, urinary frequency, and suprapubic and back pain. Urinalysis: pH 7.5, sp.gr. 1.015, WBC > 50/HPF, RBC 0–1/HPF, numerous bacteria. What is the most likely pathogen?",
            "Proteus mirabilis",
            ["Escherichia coli", "Enterococcus faecium", "Chlamydia trachomatis", "Pseudomonas aeruginosa"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (เฉลยแก้ไขโดยพี่ซี)",
            explain='''จุดสำคัญคือ **urine pH 7.5 (alkaline)** → เชื้อที่สร้าง **urease** แยก urea เป็น ammonia ทำให้ปัสสาวะเป็นด่าง = ***Proteus mirabilis*** (พี่ซีแก้เฉลยในสไลด์: ถ้ามี alkaline urine ควรตอบ Proteus มากกว่า)
- *E. coli* เป็นเชื้อที่พบบ่อยที่สุดโดยรวม และเป็นคำตอบถ้าไม่มีเบาะแสพิเศษ แต่ไม่ทำให้ปัสสาวะเป็นด่าง
- *Enterococcus* พบใน UTI หลังใส่สายสวน/ผู้สูงอายุ ไม่สร้าง urease
- *Chlamydia* ทำ urethritis (sterile pyuria) ไม่เห็นแบคทีเรียมาก
- *Pseudomonas* พบใน complicated/hospital-acquired UTI''',
            pearl="UTI + urine pH ด่าง → Proteus", topic="UTI pathogen",
            ref=[f"{D} หน้า 277, 283–284"], nl=["2.3.14(14)", "2.3.14(7)"]),
        mcq("NEPHRO-09-01-2",
            "A 6-year-old girl has fever for 2 days and daily urinary incontinence. BT 39 °C. She has flank tenderness and a palpable urinary bladder. Urine dipstick: nitrite, leukocyte esterase, and blood all positive. What is the most likely diagnosis?",
            "Acute pyelonephritis",
            ["Acute cystitis", "Acute glomerulonephritis", "Acute interstitial nephritis", "IgA nephropathy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**ไขสูง 39 °C + flank tenderness** + dipstick nitrite/LE บวก = **upper UTI (acute pyelonephritis)** (กระเพาะปัสสาวะโป่งและกลั้นไม่ได้ชวนคิด voiding dysfunction/VUR เป็นปัจจัยเสี่ยง)
- Acute cystitis มักไม่มีไข้และไม่มี flank tenderness
- AGN มี hematuria + RBC cast + ความดันสูง บวม ไม่มี nitrite/LE
- AIN มีประวัติยา ผื่น eosinophilia nitrite ลบ
- IgAN มี hematuria หลัง URI ไม่มี pyuria/nitrite''',
            pearl="UTI + ไข้ + ปวดเอว = pyelonephritis", topic="Upper vs lower UTI",
            ref=[f"{D} หน้า 277, 285–286"], nl=["2.3.14(14)", "B9.2.2(2)"]),
        mcq("NEPHRO-09-01-3",
            "A 60-year-old man presents with left flank pain, fever with chills, and dark urine. Left CVA tenderness. CBC: leukocytosis (PMN 80%). Urinalysis: WBC 50–100/HPF, RBC 5–10/HPF. What is the most appropriate next investigation?",
            "Ultrasound of the kidneys, ureters, and bladder",
            ["Intravenous pyelography", "Retrograde urethrography", "Voiding cystourethrography", "Renal biopsy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Pyelonephritis ใน **ผู้ชาย** เป็นข้อบ่งชี้ imaging (สไลด์: male) เพื่อหาการอุดตัน/นิ่ว/ฝี → **U/S KUB** ปลอดภัย ไม่มี contrast หา hydronephrosis และ renal abscess ได้
- IVP ใช้ contrast ในขณะติดเชื้อ/อาจมีไตเสื่อม และถูกแทนด้วย CT แล้ว
- Retrograde urethrography ดู urethral stricture ไม่เกี่ยวกับปวดเอว
- VCUG ใช้หา vesicoureteral reflux ในเด็ก
- Renal biopsy ไม่มีบทบาทใน pyelonephritis''',
            pearl="Pyelonephritis ในผู้ชาย → U/S KUB", topic="UTI imaging",
            ref=[f"{D} หน้า 279, 295–296"], nl=["2.3.14(14)"]),
    ])

# ---------------------------------------------------------------- 09-02 UTI management
F_UTI = fig("nephro-09-02-f1", "เลือกยารักษา UTI (ตามสไลด์)", '''<svg viewBox="0 0 740 380">
 <rect x="10" y="10" width="355" height="40" rx="10" class="c1"/>
 <text x="187" y="35" text-anchor="middle" class="tw">Cystitis (lower UTI)</text>
 <rect x="375" y="10" width="355" height="40" rx="10" class="bad"/>
 <text x="552" y="35" text-anchor="middle" class="tw">Pyelonephritis (upper UTI)</text>
 <rect x="10" y="60" width="355" height="150" rx="10" class="c1soft"/>
 <text x="22" y="82" class="tb">Uncomplicated</text>
 <text x="22" y="100" class="t3">หญิง ไม่ตั้งครรภ์ host ปกติ ทางเดินปัสสาวะปกติ</text>
 <text x="22" y="126" class="t2">1st: Fosfomycin 1 วัน (single dose)</text>
 <text x="54" y="146" class="t2">Nitrofurantoin 5 วัน</text>
 <text x="54" y="166" class="t2">Cephalexin 7 วัน</text>
 <text x="22" y="190" class="t2">2nd: Ciprofloxacin 3 วัน</text>
 <rect x="375" y="60" width="355" height="150" rx="10" class="badsoft"/>
 <text x="387" y="82" class="tb">Uncomplicated</text>
 <text x="387" y="108" class="t2">OPD: Ciprofloxacin 7 วัน</text>
 <text x="425" y="128" class="t2">Levofloxacin 5 วัน</text>
 <text x="387" y="154" class="t2">IPD (severe เช่น ไข้สูง):</text>
 <text x="387" y="174" class="t2">IV ceftriaxone, cefotaxime,</text>
 <text x="387" y="194" class="t2">ciprofloxacin, gentamicin</text>
 <rect x="10" y="220" width="355" height="96" rx="10" class="misssoft"/>
 <text x="22" y="242" class="tb">Complicated</text>
 <text x="22" y="262" class="t3">immunocompromised, pregnancy, male,</text>
 <text x="22" y="280" class="t3">stone/stent/catheter, ADPKD</text>
 <text x="22" y="304" class="t2">ยาเดิม แต่ให้นาน 1–2 สัปดาห์</text>
 <rect x="375" y="220" width="355" height="96" rx="10" class="misssoft"/>
 <text x="387" y="242" class="tb">Complicated (เช่น ตั้งครรภ์)</text>
 <text x="387" y="268" class="t2">IPD: IV ceftriaxone, cefotaxime</text>
 <text x="387" y="292" class="t3">ตั้งครรภ์ห้าม quinolone (เสริม)</text>
 <rect x="10" y="324" width="720" height="50" rx="10" class="oksoft"/>
 <text x="22" y="346" class="tb">Asymptomatic bacteriuria: ไม่ต้องให้ยา</text>
 <text x="22" y="364" class="t2">ยกเว้น pregnancy, ก่อน urologic procedure → amoxicillin, ampicillin, nitrofurantoin 3–7 วัน</text>
</svg>''', "เลือกคอลัมน์ตามตำแหน่ง (cystitis/pyelonephritis) แล้วเลือกแถวตามว่า complicated หรือไม่ แถบล่างคือ asymptomatic bacteriuria")

S2 = sec("nephro-09-02", "UTI management: ASB · cystitis · pyelonephritis",
    "ASB ไม่ต้องรักษา ยกเว้นตั้งครรภ์/ก่อนหัตถการ · cystitis: fosfomycin/nitrofurantoin/cephalexin · pyelo OPD cipro/levo · ตั้งครรภ์ IV ceftriaxone", minutes=8,
    source=f"{D} หน้า 280–282, 287–294", nl=["2.3.14(7)", "2.3.14(14)", "B9.2.2(1)"],
    md='''
[[fig:nephro-09-02-f1]]

### Asymptomatic bacteriuria (ASB)

- พบแบคทีเรีย (± WBC) **โดยไม่มีอาการ**
- **ไม่ต้องให้ ATB** (รวมถึงผู้สูงอายุ เบาหวาน ใส่สายสวน ESRD นิ่ว)
- **ยกเว้น: pregnancy, ก่อน urologic procedure** (ที่ทำให้เลือดออกในเยื่อบุ เช่น TURP)
- ยาใน pregnancy: **amoxicillin, ampicillin, nitrofurantoin 3–7 วัน**
- ASB ในหญิงตั้งครรภ์ที่ไม่รักษา → pyelonephritis, คลอดก่อนกำหนด, ทารกน้ำหนักน้อย (เสริม)

### Cystitis

**Uncomplicated cystitis** (host ปกติ, ไม่ตั้งครรภ์, หญิง, ไม่มีความผิดปกติทางเดินปัสสาวะ)
- **1st line: fosfomycin 1 วัน (single dose), nitrofurantoin 5 วัน, cephalexin 7 วัน**
- **2nd line: ciprofloxacin 3 วัน** (เก็บ quinolone ไว้ใช้กับโรครุนแรงกว่า และมีผลข้างเคียง — tendinopathy, QT ยาว (เสริม))
- ไม่จำเป็นต้องส่ง culture ในรายแรก (เสริม)

**Complicated cystitis** (immunocompromised, pregnancy, male, urologic abnormality เช่น stone, stent, catheter, ADPKD)
- **ยาเดิม แต่นาน 1–2 สัปดาห์**

### Pyelonephritis

**Uncomplicated**
- **OPD: ciprofloxacin 7 วัน, levofloxacin 5 วัน**
- **IPD** (severe เช่น ไข้สูง อาเจียนกินไม่ได้ sepsis): **IV ceftriaxone, cefotaxime, ciprofloxacin, gentamicin**

**Complicated** (เช่น ตั้งครรภ์, ผู้ชาย, มีนิ่วอุดตัน)
- **IPD: IV ceftriaxone, cefotaxime**
- **ตั้งครรภ์: admit + IV ceftriaxone** (หลีกเลี่ยง quinolone, tetracycline, TMP/SMX ช่วงไตรมาส 1 และใกล้คลอด (เสริม))
- ไม่ดีขึ้นใน 72 ชม. → imaging หา abscess/obstruction
''',
    figs=[F_UTI],
    pearls=[
        "ASB ไม่ต้องรักษา ยกเว้นตั้งครรภ์ และก่อน urologic procedure",
        "Uncomplicated cystitis: fosfomycin single dose / nitrofurantoin 5 วัน / cephalexin 7 วัน · cipro 3 วันเป็น 2nd line",
        "Complicated cystitis: ยาเดิม 1–2 สัปดาห์",
        "Pyelo OPD: cipro 7 วัน หรือ levo 5 วัน · severe/complicated: IV ceftriaxone",
        "Pyelonephritis ในหญิงตั้งครรภ์ → admit + IV ceftriaxone",
    ],
    items=[
        mcq("NEPHRO-09-02-1",
            "In which of the following patients should asymptomatic bacteriuria be treated with antibiotics?",
            "A 26-year-old woman at 14 weeks of pregnancy",
            ["A 70-year-old man with ESRD on hemodialysis", "A 55-year-old woman with a non-obstructing renal stone", "An 80-year-old nursing-home resident with a long-term urinary catheter", "A 60-year-old woman with well-controlled type 2 diabetes"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''สไลด์: ASB **ไม่ต้องให้ ATB ยกเว้น pregnancy และ urologic procedure** — ในหญิงตั้งครรภ์ ASB เพิ่มความเสี่ยง pyelonephritis และคลอดก่อนกำหนด
- ESRD, นิ่วที่ไม่อุดตัน, สายสวนถาวร และเบาหวานที่คุมได้ ล้วนเป็นกลุ่มที่การรักษา ASB ไม่ได้ลดภาวะแทรกซ้อน แต่เพิ่มเชื้อดื้อยาและผลข้างเคียง''',
            pearl="ASB รักษาเฉพาะตั้งครรภ์ และก่อน urologic procedure", topic="Asymptomatic bacteriuria",
            ref=[f"{D} หน้า 280, 287–288"], nl=["2.3.14(7)"]),
        mcq("NEPHRO-09-02-2",
            "A 20-year-old woman presents with frequency, urgency, and dysuria. BT 37 °C, BP 100/70 mmHg. Mild suprapubic tenderness. Urinalysis: albumin trace, sugar negative, WBC 50–100/HPF, RBC 5–10/HPF, moderate bacteria. She is not pregnant. What is the most appropriate management?",
            "Fosfomycin single dose",
            ["Co-trimoxazole for 7 days", "Amoxicillin/clavulanic acid for 5 days", "Ciprofloxacin single dose", "Doxycycline for 7 days"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''หญิงสาว ไม่มีไข้ ไม่ตั้งครรภ์ อาการ lower UTI = **uncomplicated cystitis** → 1st line ตามสไลด์: **fosfomycin 1 วัน (single dose)**, nitrofurantoin 5 วัน, cephalexin 7 วัน
- Co-trimoxazole ใช้ได้ในบางแนวทางแต่ 3 วันพอ และเชื้อในไทยดื้อสูง 7 วันนานเกิน
- Amoxicillin/clavulanate เป็นตัวเลือกรอง ประสิทธิภาพต่ำกว่า
- Ciprofloxacin เป็น 2nd line และต้องให้ 3 วัน ไม่ใช่ single dose
- Doxycycline ใช้กับ chlamydia urethritis ไม่ใช่ cystitis จาก E. coli''',
            pearl="Uncomplicated cystitis → fosfomycin single dose (หรือ nitrofurantoin 5 วัน)", topic="Uncomplicated cystitis",
            ref=[f"{D} หน้า 281, 289–290"], nl=["2.3.14(7)", "B9.2.2(1)"]),
        mcq("NEPHRO-09-02-3",
            "A 28-year-old non-pregnant woman has back pain, fever 38.3 °C, and chills for 1 day. She can take oral fluids, BP 118/72 mmHg, and has right CVA tenderness. Urinalysis: WBC 50–100/HPF, bacteria positive. She has no urologic abnormality. What is the most appropriate management?",
            "Oral ciprofloxacin for 7 days as an outpatient",
            ["Admit for intravenous ceftriaxone", "Fosfomycin single dose", "Nitrofurantoin for 5 days", "No antibiotics; repeat urinalysis in 1 week"],
            kind="old", src="ดัดแปลงจากตัวอย่างข้อสอบในสไลด์",
            explain='''ไข้ + ปวดเอว + CVA tenderness = **pyelonephritis** ที่ **uncomplicated** และอาการไม่รุนแรง (กินได้ ความดันปกติ) → **OPD: ciprofloxacin 7 วัน** (หรือ levofloxacin 5 วัน)
- IV ceftriaxone ในโรงพยาบาลใช้เมื่อรุนแรง (ไข้สูงมาก อาเจียน sepsis) หรือ complicated
- Fosfomycin และ nitrofurantoin มีระดับยาในเนื้อไตต่ำ ใช้ได้เฉพาะ cystitis
- ไม่ให้ยาเลยใน pyelonephritis เสี่ยง sepsis/renal abscess''',
            pearl="Uncomplicated pyelo OPD → cipro 7 วัน / levo 5 วัน", topic="Uncomplicated pyelonephritis",
            ref=[f"{D} หน้า 282, 291–292"], nl=["2.3.14(14)", "B9.2.2(2)"]),
        mcq("NEPHRO-09-02-4",
            "A 35-year-old primigravida presents with right flank pain, fever, and dysuria. Right CVA tenderness. Urinalysis: WBC 10–20/HPF, RBC 0–1/HPF. What is the most appropriate management?",
            "Admit and give intravenous ceftriaxone",
            ["Oral doxycycline", "Oral levofloxacin", "Oral co-trimoxazole", "Oral amoxicillin/clavulanic acid as an outpatient"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Pyelonephritis ใน **หญิงตั้งครรภ์ = complicated** → สไลด์: **IPD + IV ceftriaxone** (หรือ cefotaxime) เพราะเสี่ยง sepsis และคลอดก่อนกำหนด
- Doxycycline (tetracycline) ห้ามในครรภ์ — กระทบฟันและกระดูกทารก
- Levofloxacin (quinolone) หลีกเลี่ยงในครรภ์
- Co-trimoxazole หลีกเลี่ยงไตรมาสแรก (antifolate) และใกล้คลอด (kernicterus)
- Amoxicillin/clavulanate แบบ OPD ไม่เพียงพอสำหรับ pyelonephritis ในครรภ์''',
            pearl="Pyelo ในครรภ์ → admit + IV ceftriaxone", topic="Pyelonephritis in pregnancy",
            ref=[f"{D} หน้า 282, 293–294"], nl=["2.3.14(14)"]),
        mcq("NEPHRO-09-02-5",
            "A 58-year-old man with diabetes is admitted with pyelonephritis and treated with IV ceftriaxone based on a susceptible E. coli culture. After 72 hours he still has fever 39 °C and flank pain. What is the most appropriate next step?",
            "Imaging of the kidneys to look for abscess or obstruction",
            ["Switch to oral nitrofurantoin", "Continue the same antibiotic without further investigation", "Add oral fluconazole empirically", "Stop antibiotics and repeat culture in 1 week"],
            explain='''สไลด์: imaging เมื่อ **pyelonephritis ไม่ดีขึ้นใน 72 ชั่วโมง** (และผู้ป่วยเป็นชาย เบาหวาน) → หา **renal/perinephric abscess, การอุดตัน, emphysematous pyelonephritis** ด้วย U/S หรือ CT ซึ่งอาจต้องเจาะระบาย
- Nitrofurantoin ไม่มีระดับยาในเนื้อไต
- ให้ยาเดิมต่อโดยไม่หาสาเหตุ พลาดภาวะที่ต้องระบาย
- ไม่มีหลักฐานติดเชื้อรา
- หยุดยาในผู้ที่ยังไข้สูงเป็นอันตราย''',
            pearl="Pyelo ไม่ดีขึ้น 72 ชม. → imaging หา abscess/obstruction", topic="Non-resolving pyelonephritis",
            ref=[f"{D} หน้า 279"], nl=["2.3.14(14)"]),
    ])

LECTURE = lecture("09", "Urinary tract infection", "เชื้อ · UA · imaging · ASB · cystitis · pyelonephritis",
    objectives=[
        "แยก upper vs lower UTI และบอกเชื้อที่น่าจะเป็นจากเบาะแส (เช่น ปัสสาวะด่าง) ได้",
        "บอกข้อบ่งชี้ส่ง urine culture และ imaging ได้",
        "เลือกยาและระยะเวลารักษา ASB, cystitis, pyelonephritis ทั้ง uncomplicated และ complicated ได้",
    ],
    sections=[S1, S2])
