from lib import lecture, sec, mcq, fig

D = "สไลด์ Update ข้อสอบ 2025"
SRC = "NL2 2025 (update)"

def R(*p):
    return [f"{D} หน้า " + ", ".join(str(x) for x in p)]

# ---------------------------------------------------------------- 01-01 Valve & IE
S1 = sec("exam25-01-01", "Valvular heart disease & infective endocarditis",
    "ไข้เรื้อรัง + ลิ้นหัวใจผิดปกติ + embolic/immunologic sign = IE · PSM ที่ apex ร้าวไป axilla = MR", minutes=5,
    source=f"{D} หน้า 116–122, 137–138", nl=["2.3.9-3(5)", "2.3.9-3(8)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

- โจทย์ IE ปี 2025 ออก **2 ข้อ** ใช้ pattern เดียวกัน: **มีลิ้นหัวใจผิดปกติ** (RHD, MVP) + **ไข้** + **splinter hemorrhage / conjunctival petechiae / murmur ใหม่** (± ฟันผุ = แหล่ง viridans strep)
- Murmur: ให้ระบุตำแหน่ง + ระยะ + ทิศทางการร้าว

| ลักษณะ murmur | โรค |
|---|---|
| Pansystolic ที่ apex ร้าวไป **left axilla** | **MR** |
| Mid-diastolic rumble ที่ apex (± opening snap) | MS (RHD) |
| Ejection systolic ที่ RUSB ร้าวไป carotid | AS |
| Pansystolic ที่ LLSB ดังขึ้นตอนหายใจเข้า | TR |
| Harsh PSM ที่ LLSB + thrill | VSD |
| Systolic ที่ LLSB ดังขึ้นเมื่อ Valsalva/ยืน | HCM |

### Duke criteria (ฉบับ 2023 ตามสไลด์)

- **Major**: blood culture บวก (เชื้อที่ทำให้เกิด IE บ่อย จาก 2 ขวด หรือบวกต่อเนื่อง) · **imaging บวก** (echo/CT/PET เห็น vegetation, abscess, ลิ้นรั่วใหม่)
- **Minor**: predisposing condition · ไข้ > 38 °C · **vascular** (emboli, mycotic aneurysm, ICH, **conjunctival hemorrhage, Janeway lesion**) · **immunologic** (GN, **Osler node, Roth spot**, RF) · microbiologic ที่ไม่ถึง major
- **Definite** = 2 major หรือ 1 major + ≥ 3 minor หรือ 5 minor · **Possible** = 1 major + 1–2 minor หรือ 3–4 minor

> สงสัย IE → **hemoculture อย่างน้อย 3 ขวด ก่อนให้ยาปฏิชีวนะ** แล้วตามด้วย echo (เสริม)
''',
    pearls=[
        "RHD/MVP + ไข้ + splinter hemorrhage = IE จนกว่าจะพิสูจน์ได้ว่าไม่ใช่",
        "ฟันผุ + ลิ้นหัวใจผิดปกติ → viridans streptococci",
        "Duke definite: 2 major / 1 major + 3 minor / 5 minor",
        "PSM ที่ apex ร้าวไป axilla = MR",
    ],
    items=[
        mcq("EXAM25-01-01-1",
            "A 20-year-old woman with known rheumatic mitral valve disease presents with low-grade fever for 1 month. Vital signs are otherwise normal. Examination shows conjunctival petechiae, splinter hemorrhages of the fingernails, and a pansystolic murmur together with a diastolic rumble at the apex. What is the most likely diagnosis?",
            "Infective endocarditis",
            ["Rheumatic carditis", "Tuberculous pericarditis", "Meningococcemia", "Systemic lupus erythematosus"],
            kind="old", src=SRC,
            explain='''ลิ้นหัวใจผิดปกติเดิม (rheumatic MS/MR) + **ไข้นาน 1 เดือน** + **conjunctival petechiae และ splinter hemorrhage** (vascular phenomena ใน Duke minor) = **infective endocarditis** (subacute)
- Rheumatic carditis เป็นการอักเสบหลังติดเชื้อ strep ครั้งแรก/ซ้ำ มักมี migratory polyarthritis ไม่ทำให้ splinter hemorrhage
- TB pericarditis ให้ pericardial rub, effusion, JVP สูง ไม่มี embolic sign
- Meningococcemia เป็นแบบเฉียบพลัน ไข้สูง ผื่น purpura กระจาย ป่วยหนักใน 1–2 วัน ไม่ใช่ไข้ต่ำ 1 เดือน
- SLE อาจมี Libman–Sacks endocarditis ได้ แต่โจทย์ไม่มีผื่น ข้อ หรือไต และมี RHD ซึ่งเป็น predisposing condition ชัดเจน''',
            pearl="ลิ้นผิดปกติ + ไข้เรื้อรัง + splinter/petechiae = IE", topic="Infective endocarditis",
            ref=R(116, 117, 120), nl=["2.3.9-3(5)"]),
        mcq("EXAM25-01-01-2",
            "A 50-year-old woman with mitral valve prolapse presents with fever, a new murmur, and splinter hemorrhages. Dental examination reveals multiple untreated caries. What is the most likely diagnosis?",
            "Infective endocarditis",
            ["Sepsis from a dental source", "Periodontal abscess", "Acute rheumatic fever", "Acute pericarditis"],
            kind="old", src=SRC,
            explain='''MVP (โดยเฉพาะมี MR) เป็น predisposing condition · **ฟันผุ** = แหล่งของ viridans streptococci เข้ากระแสเลือด · **ไข้ + murmur ใหม่ + splinter hemorrhage** = **infective endocarditis**
- Sepsis จากฟันไม่ได้อธิบาย murmur ใหม่และ embolic sign ได้ (ต้นเหตุจริงคือเชื้อไปเกาะลิ้นหัวใจ)
- Periodontal abscess เป็นแหล่งเชื้อเฉพาะที่ ไม่ทำให้เกิด murmur
- Rheumatic fever พบในเด็ก/วัยรุ่นหลัง strep pharyngitis ใช้ Jones criteria ไม่ใช่หญิงอายุ 50 ที่มีฟันผุ
- Acute pericarditis ให้เจ็บหน้าอกตามท่า + friction rub ไม่ใช่ murmur''',
            pearl="ฟันผุ + MVP + ไข้ + murmur ใหม่ = IE (viridans strep)", topic="Infective endocarditis",
            ref=R(121, 122), nl=["2.3.9-3(5)"]),
        mcq("EXAM25-01-01-3",
            "A 50-year-old patient has a 6-month history of exertional dyspnea and palpitations. Vital signs are normal. Examination reveals a grade 3/6 pansystolic murmur loudest at the apex and radiating to the left axilla. What is the most likely cause?",
            "Mitral regurgitation",
            ["Aortic stenosis", "Tricuspid regurgitation", "Ventricular septal defect", "Hypertrophic cardiomyopathy"],
            kind="old", src=SRC,
            explain='''**Pansystolic ที่ apex ร้าวไป left axilla** = **mitral regurgitation** (เลือดย้อนจาก LV ไป LA ตลอด systole)
- AS เป็น ejection systolic (crescendo–decrescendo) ที่ right upper sternal border ร้าวไป carotid
- TR เป็น pansystolic ที่ left lower sternal border ดังขึ้นเมื่อหายใจเข้า (Carvallo sign)
- VSD เป็น harsh pansystolic ที่ left lower sternal border มักคลำ thrill ได้ ไม่ร้าวไป axilla
- HCM เป็น systolic ที่ LLSB ดังขึ้นเมื่อ Valsalva/ยืน (preload ลด)''',
            pearl="Apex + PSM + ร้าวไป axilla = MR", topic="Murmur",
            ref=R(137, 138), nl=["2.3.9-3(8)"]),
    ])

# ---------------------------------------------------------------- 01-02 Chest pain
S2 = sec("exam25-01-02", "Acute chest pain & myocardial injury",
    "Troponin สูง ไม่มี STE = NSTEMI · ปวดฉีกร้าวไปหลัง + BP สูง = dissection (IV BB ก่อน) · หลัง URI + shock + troponin = myocarditis", minutes=5,
    source=f"{D} หน้า 123–126, 131–132", nl=["2.2.1", "2.3.9-3(2)", "2.3.9-3(6)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

| โจทย์ให้ | คิดถึง | จุดที่ใช้แยก |
|---|---|---|
| Risk factor + เจ็บอก + **troponin สูง** + ECG **ไม่มี ST elevation** | **NSTEMI** | STEMI ต้องมี STE ≥ 2 lead ติดกัน |
| เจ็บอกทันที **ฉีกร้าวไปหลัง** + BP สูงมาก/BP แขนสองข้างต่างกัน | **Aortic dissection** | ECG มักไม่มี ST change |
| **ไข้หวัดนำ 1 สัปดาห์** → HF/cardiogenic shock + troponin สูง ในคนอายุน้อย | **Acute myocarditis** | ไม่มี risk factor ของ CAD · ECG sinus tachycardia |
| เจ็บอกตามท่า ดีขึ้นเมื่อนั่งโน้มตัวไปข้างหน้า + diffuse STE + PR depression | Acute pericarditis | troponin มักปกติหรือสูงเล็กน้อย |

### Aortic dissection: ลำดับการรักษา (สไลด์)

1. **IV beta-blocker ก่อน** (esmolol, labetalol) ลด HR < 60 และลด dP/dt
2. แล้วค่อยให้ **IV vasodilator** (nicardipine, nitroprusside) ถ้า SBP ยังสูง (เป้า SBP 100–120 (เสริม))
3. Type A (ascending) → ผ่าตัดด่วน · Type B → ส่วนใหญ่ให้ยา (เสริม)

> ห้ามให้ vasodilator ก่อน beta-blocker เพราะจะเกิด reflex tachycardia ทำให้ dissection ลุกลาม (เสริม)
''',
    pearls=[
        "Troponin สูง + ไม่มี STE = NSTEMI",
        "Dissection: IV beta-blocker ก่อน แล้วจึงให้ vasodilator",
        "URI นำ → cardiogenic shock + troponin สูงในคนอายุน้อย = myocarditis",
        "BP แขนสองข้างต่างกัน + ปวดร้าวไปหลัง = dissection",
    ],
    items=[
        mcq("EXAM25-01-02-1",
            "A 50-year-old man with hyperlipidemia presents with 3 days of dyspnea and intermittent chest discomfort. BP 120/70 mmHg, pulse 150/min. There are bilateral lung crepitations and an S3 gallop. Troponin T is 200 ng/L. The ECG shows a regular narrow-complex tachycardia at about 150/min without ST-segment elevation. What is the most likely diagnosis?",
            "Acute NSTEMI",
            ["Acute STEMI", "Acute myocarditis", "Acute pericarditis", "Pulmonary embolism"],
            kind="old", src=SRC,
            explain='''มี risk factor (hyperlipidemia, ชายอายุ 50) + เจ็บแน่นอกเป็นพัก ๆ + **troponin สูง** + HF (crepitation, S3) และ **ECG ไม่มี ST elevation** = **NSTEMI** (ECG ในสไลด์เป็นภาพ narrow-complex tachycardia ไม่มี STE)
- STEMI ต้องมี ST elevation ใน lead ที่ติดกัน ซึ่งโจทย์ไม่มี
- Myocarditis มักเกิดในคนอายุน้อย มีไข้หวัดนำ ไม่มี risk factor ของ CAD
- Pericarditis ให้ diffuse STE + PR depression และเจ็บตามท่า
- PE ให้หอบ hypoxemia ปอดใส ไม่มี S3 และ crepitation ทั้งสองข้าง''',
            pearl="Troponin สูง + ไม่มี STE = NSTEMI", topic="NSTEMI",
            ref=R(123, 124), nl=["2.2.1"]),
        mcq("EXAM25-01-02-2",
            "A 50-year-old man with poorly controlled hypertension presents with sudden, severe tearing chest pain radiating to his back. BP 200/130 mmHg, pulse 120/min. ECG shows no ST changes. What is the most likely diagnosis?",
            "Acute aortic dissection",
            ["Acute myocardial infarction", "Pulmonary embolism", "Pneumothorax", "Acute pancreatitis"],
            kind="old", src=SRC,
            explain='''HT คุมไม่ได้ + **ปวดเฉียบพลันแบบฉีกร้าวทะลุหลัง** + BP สูงมาก + ECG ปกติ = **acute aortic dissection** · รักษา: **IV beta-blocker ก่อน** แล้วจึงให้ IV vasodilator
- AMI ปวดแน่นกดทับ ไม่ใช่ฉีกร้าวทันทีที่สุด และมักมี ECG เปลี่ยน
- PE ปวดแบบ pleuritic + หอบ + hypoxemia ไม่ใช่ BP สูงมาก
- Pneumothorax ปวดแหลมด้านเดียว หายใจเสียงเบา ไม่ร้าวไปหลัง
- Pancreatitis ปวดลิ้นปี่ทะลุหลังได้ แต่ค่อยเป็นค่อยไป มีคลื่นไส้อาเจียน ไม่ใช่เจ็บอก''',
            pearl="ปวดฉีกทะลุหลัง + HT = dissection → IV BB ก่อน vasodilator", topic="Aortic dissection",
            ref=R(125, 126), nl=["2.3.9-3(2)", "2.2.6"]),
        mcq("EXAM25-01-02-3",
            "A 30-year-old previously healthy woman presents with 3 days of progressive dyspnea, preceded by 7 days of fever, rhinorrhea and non-productive cough. BP 80/50 mmHg, pulse 130/min, RR 32/min, SpO2 80%. She has cold extremities, raised JVP, a displaced apex beat (6th ICS, 3 cm lateral to the midclavicular line), an S3 gallop and bilateral crepitations. Troponin T 440 ng/L. ECG: sinus tachycardia. What is the most likely diagnosis?",
            "Acute myocarditis",
            ["Acute myocardial infarction", "Pneumonia with septic shock", "Acute massive pulmonary embolism", "Hypovolemic shock"],
            kind="old", src=SRC,
            explain='''หญิงอายุน้อยไม่มีโรคเดิม + **ไข้หวัดนำ 1 สัปดาห์** → HF เฉียบพลันจนเกิด **cardiogenic shock** (ปลายมือเย็น JVP สูง S3 crepitation หัวใจโต) + **troponin สูง** + ECG ไม่มี STE = **acute (viral) myocarditis**
- AMI ไม่เข้ากับอายุ 30 ไม่มี risk factor และ ECG ไม่มี ST change
- Septic shock มักเป็น warm shock และ JVP ไม่สูง หัวใจไม่โต
- Massive PE ทำให้ JVP สูงได้ แต่ไม่ทำให้ LV failure (crepitation ทั้งสองข้าง, S3, apex เลื่อน)
- Hypovolemic shock จะมี JVP ต่ำ ปอดใส''',
            pearl="URI นำ + cardiogenic shock + troponin ในคนอายุน้อย = myocarditis", topic="Myocarditis",
            ref=R(131, 132), nl=["2.3.9-3(6)", "2.2.7"]),
    ])

# ---------------------------------------------------------------- 01-03 Syncope & tachy
S3 = sec("exam25-01-03", "Syncope & unstable tachycardia",
    "Vasovagal = clinical dx (tilt table เมื่อไม่ชัด) · tachycardia + unstable sign = synchronized cardioversion", minutes=4,
    source=f"{D} หน้า 127–130", nl=["2.2.40", "2.3.9(1)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Vasovagal (reflex) syncope**
- Trigger: **ความเครียด/อารมณ์** ยืนนาน เจ็บปวด เห็นเลือด · มีอาการเตือน (หน้ามืด เหงื่อออก) · ฟื้นเร็วเมื่อนอนราบ
- วินิจฉัยจาก **ประวัติ (clinical diagnosis)** · **Tilt table test** ใช้เมื่อการวินิจฉัยไม่ชัด/เป็นซ้ำ
- ทุกรายควรมี 12-lead ECG ตั้งแต่แรก (เสริม) · Holter/echo เมื่อสงสัยสาเหตุจากหัวใจ (หมดสติขณะออกแรง, นอนอยู่, มีโรคหัวใจ)

**Tachycardia ที่ unstable** = มีอย่างใดอย่างหนึ่ง: **hypotension, AOC, sign of shock, ischemic chest discomfort, acute heart failure**

| Rhythm | Unstable | Stable (เสริม) |
|---|---|---|
| AF/SVT/VT ที่มีชีพจร | **Synchronized cardioversion** | Rate control / adenosine (SVT) / amiodarone (VT) |
| VF / pulseless VT | **Defibrillation** (unsynchronized) | — |

> AF ที่ unstable → synchronized cardioversion ทันที (ไม่ต้องรอ anticoagulant) · defibrillation ใช้กับ VF/pulseless VT เท่านั้น
''',
    pearls=[
        "หมดสติตอนทะเลาะ ฟื้นเองเมื่อพัก = vasovagal → tilt table ถ้าไม่ชัด",
        "Unstable = hypotension, AOC, shock, chest pain, AHF",
        "Tachycardia ที่มีชีพจร + unstable → synchronized cardioversion",
        "Defibrillation (ไม่ sync) ใช้กับ VF/pulseless VT",
    ],
    items=[
        mcq("EXAM25-01-03-1",
            "A 32-year-old woman collapses with loss of consciousness during an argument and regains consciousness after resting. She reports similar previous episodes. Vital signs and cardiac auscultation are normal. What is the most appropriate initial investigation?",
            "Tilt table test",
            ["Holter monitor", "Echocardiogram", "EEG", "Serum electrolytes"],
            kind="old", src=SRC,
            explain='''หมดสติขณะมีอารมณ์รุนแรง ฟื้นเองเร็วเมื่อพัก เป็นซ้ำ ตรวจหัวใจปกติ = **vasovagal syncope** ซึ่งเป็น clinical diagnosis และใช้ **tilt table test** เมื่ออาการเป็นซ้ำ/วินิจฉัยไม่ชัด (เฉลยของสไลด์) — ในเวชปฏิบัติจริงทุกรายควรทำ 12-lead ECG ก่อน แต่ไม่มีในตัวเลือก
- Holter ใช้เมื่อสงสัย arrhythmia (หมดสติขณะออกแรง ใจสั่นนำ มีโรคหัวใจ)
- Echo ใช้เมื่อได้ยิน murmur หรือสงสัย structural heart disease ซึ่งรายนี้ฟังปกติ
- EEG ใช้เมื่อสงสัยชัก (มีชักเกร็ง กัดลิ้น สับสนนานหลังฟื้น)
- Electrolyte ไม่ช่วยอธิบายหมดสติที่มี trigger ทางอารมณ์ชัด''',
            pearl="Emotional trigger + ฟื้นเร็ว + หัวใจปกติ = vasovagal → tilt table", topic="Vasovagal syncope",
            ref=R(127, 128), nl=["2.2.40", "2.1.5"]),
        mcq("EXAM25-01-03-2",
            "A 60-year-old man is found unconscious. BP 90/50 mmHg, pulse 130–150/min and irregular. ECG shows atrial fibrillation with rapid ventricular response. He has no prior cardiac history. What is the most appropriate management?",
            "Synchronized cardioversion",
            ["Defibrillation", "Intravenous amiodarone", "Intravenous digoxin", "Intravenous adenosine"],
            kind="old", src=SRC,
            explain='''AF with RVR + **unstable sign** (hypotension, หมดสติ) → **synchronized electrical cardioversion** ทันที
- Defibrillation (ไม่ sync) ใช้กับ VF/pulseless VT ถ้าใช้กับ AF อาจช็อตตรง T wave แล้วกลายเป็น VF
- Amiodarone และ digoxin เป็นยาสำหรับ AF ที่ stable ออกฤทธิ์ช้า และ amiodarone ทำให้ BP ลดลงอีก
- Adenosine ใช้กับ regular narrow-complex SVT ไม่ได้ช่วยหยุด AF''',
            pearl="Tachycardia + unstable → synchronized cardioversion", topic="Unstable tachycardia",
            ref=R(129, 130), nl=["2.3.9(1)"]),
    ])

# ---------------------------------------------------------------- 01-04 HT
S4 = sec("exam25-01-04", "Hypertension",
    "BP office ≥140/90 ครั้งแรก → ยืนยัน HBPM/ABPM + lifestyle · DM + proteinuria → ACEI/ARB", minutes=4,
    source=f"{D} หน้า 133–136", nl=["2.3.9(4)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

- **วัดที่ office ได้ ≥ 140/90 ครั้งแรก** ไม่มีโรคร่วม/target organ damage → **ยืนยันด้วย HBPM/ABPM หรือวัดซ้ำครั้งหน้า** และเริ่ม **lifestyle modification** ยังไม่ต้องเริ่มยา
- **วินิจฉัย HT แล้ว** → เริ่มยาได้ · แนวทางใหม่แนะนำเริ่ม **2 ตัว** (low-dose combination)
- เลือกยาตัวแรกตามโรคร่วม:

| โรคร่วม | ยาที่ควรมี |
|---|---|
| **DM + proteinuria / CKD with albuminuria** | **ACEI หรือ ARB** (+ CCB หรือ thiazide) |
| HFrEF, post-MI | ACEI/ARB/ARNI + beta-blocker |
| ไม่มีโรคร่วม | ACEI/ARB, CCB, thiazide (ตัวใดก็ได้) |

- Beta-blocker และ alpha-blocker (doxazosin) **ไม่ใช่ first-line** ถ้าไม่มีข้อบ่งชี้เฉพาะ (เสริม)
- Lifestyle: ลดเกลือ < 2 g Na/วัน, DASH, ออกกำลังกาย, ลดน้ำหนัก, ลดแอลกอฮอล์ (เสริม)
''',
    pearls=[
        "BP office สูงครั้งแรก ไม่มี TOD → ยืนยันด้วย HBPM/ABPM + lifestyle",
        "DM + proteinuria → ACEI/ARB",
        "แนวทางใหม่เริ่ม 2 ยา: ACEI/ARB + CCB หรือ thiazide",
    ],
    items=[
        mcq("EXAM25-01-04-1",
            "A 50-year-old man presents with 3 months of headaches and dizziness. His office BP is 150/95 mmHg. He has no prior hypertension, diabetes or smoking history. BMI is 23 kg/m². Physical examination is unremarkable. What is the initial management?",
            "Lifestyle modification",
            ["ACE inhibitor", "Calcium channel blocker", "Beta-blocker", "Thiazide diuretic"],
            kind="old", src=SRC,
            explain='''BP สูงที่ office **ครั้งแรก** ระดับ 150/95 ไม่มีโรคร่วม ไม่มี target organ damage → ยังวินิจฉัย HT ไม่ได้ ต้อง **ยืนยันด้วย HBPM/ABPM หรือวัดซ้ำครั้งหน้า** ระหว่างนี้เริ่ม **lifestyle modification**
- ACEI, CCB และ thiazide เป็น first-line เมื่อวินิจฉัย HT แล้ว ยังไม่ควรเริ่มจากการวัดครั้งเดียว
- Beta-blocker ไม่ใช่ first-line ถ้าไม่มีข้อบ่งชี้เฉพาะ (HF, post-MI, rate control)''',
            pearl="BP สูงครั้งแรกที่ office → ยืนยัน + lifestyle ก่อนเริ่มยา", topic="Hypertension diagnosis",
            ref=R(133, 134), nl=["2.3.9(4)"]),
        mcq("EXAM25-01-04-2",
            "A 55-year-old man with type 2 diabetes has been taking metformin and glipizide for 5 years. BP is 150/90 mmHg on repeated measurements. HbA1c 7%. Urinalysis: protein 1+, no glycosuria. He has no chest pain or edema and renal function is normal. Which medication should be added?",
            "Enalapril",
            ["Amlodipine", "Hydrochlorothiazide", "Atenolol", "Doxazosin"],
            kind="old", src=SRC,
            explain='''HT (≥ 140/90) ใน **DM ที่มี proteinuria** → ยาที่ต้องมีคือ **ACEI/ARB (enalapril)** เพราะลด intraglomerular pressure ลด proteinuria และชะลอ diabetic kidney disease (สไลด์: ควรใช้ 2 ยา โดยมี ACEI/ARB + CCB หรือ thiazide)
- Amlodipine และ HCTZ ใช้เป็นยาตัวที่สองร่วมกับ ACEI/ARB ได้ แต่ไม่ลด proteinuria
- Atenolol ไม่ใช่ first-line และอาจบดบังอาการ hypoglycemia จาก glipizide
- Doxazosin ไม่ใช่ first-line (ALLHAT พบ HF มากขึ้น)''',
            pearl="DM + proteinuria + HT → ACEI/ARB", topic="HT in DM",
            ref=R(135, 136), nl=["2.3.9(4)"]),
    ])

# ---------------------------------------------------------------- 01-05 HF
S5 = sec("exam25-01-05", "Heart failure",
    "Wet–warm + BP ไม่ต่ำ → IV furosemide · HFrEF ลดตาย = ACEI/ARNI + BB + MRA + SGLT2i", minutes=4,
    source=f"{D} หน้า 139–143", nl=["2.3.9(5)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Acute HF — แบ่งตาม congestion (wet/dry) × perfusion (warm/cold)**

| Profile | ลักษณะ | รักษา |
|---|---|---|
| **Wet & warm** (พบบ่อยสุด) | crepitation, edema, JVP สูง แต่ปลายมืออุ่น | **IV furosemide** ± vasodilator ถ้า BP สูง |
| Wet & cold | congestion + hypoperfusion | inotrope/vasopressor + diuretic เมื่อ BP ขึ้น (เสริม) |
| Dry & warm | ปกติ | ปรับยา oral |
| Dry & cold | hypovolemic/low output | ให้สารน้ำอย่างระวัง (เสริม) |

- Nitrate (SL/IV) ใช้ใน **hypertensive AHF** (SBP สูง) — ข้อนี้ BP 130/80 จึงเลือก diuretic

**Chronic HFrEF — ยาที่ลดการตาย (4 pillars ตามสไลด์)**
- **ACEI / ARB / ARNI** · **Beta-blocker** (bisoprolol, carvedilol, metoprolol succinate) · **MRA** (spironolactone) · **SGLT2 inhibitor**
- Loop diuretic, digoxin = ลดอาการ/ลดการนอนโรงพยาบาล **ไม่ลดการตาย**
- Non-DHP CCB (verapamil, diltiazem) **ห้ามใช้** ใน HFrEF (เสริม)
''',
    pearls=[
        "Wet & warm + BP ปกติ → IV furosemide",
        "HFrEF ลดตาย: ACEI/ARNI + BB + MRA + SGLT2i",
        "Diuretic และ digoxin ลดอาการ ไม่ลดตาย",
    ],
    items=[
        mcq("EXAM25-01-05-1",
            "A 65-year-old woman with hypertension, taking amlodipine and enalapril, presents with chest discomfort and dyspnea. BP 130/80 mmHg. Examination shows fine crepitations in both lungs and 2+ bilateral pitting edema. Her extremities are warm. What is the initial management?",
            "Intravenous furosemide",
            ["Sublingual nitroglycerin", "Intravenous calcium gluconate", "Intravenous normal saline 500 mL", "Increase the enalapril dose"],
            kind="old", src=SRC,
            explain='''Crepitation ทั้งสองข้าง + edema = **congestion (wet)** · ปลายอุ่น BP ปกติ = **warm** → acute HF แบบ **wet & warm** → รักษาด้วย **IV loop diuretic (furosemide)**
- SL nitroglycerin เหมาะกับ hypertensive AHF ที่ SBP สูง ซึ่งรายนี้ BP 130/80
- IV calcium gluconate ใช้ใน hyperkalemia/hypocalcemia ไม่เกี่ยว
- NSS ทำให้ congestion แย่ลง
- เพิ่ม enalapril เป็นการปรับยาระยะยาว ไม่แก้น้ำเกินเฉียบพลัน''',
            pearl="Wet & warm AHF → IV furosemide", topic="Acute heart failure",
            ref=R(139, 140), nl=["2.3.9(5)"]),
        mcq("EXAM25-01-05-2",
            "A 65-year-old man with chronic heart failure with reduced ejection fraction presents with exertional dyspnea. He is taking a loop diuretic with partial symptom relief. Which additional drug class should be started to improve survival?",
            "ACE inhibitor",
            ["Digoxin", "Calcium channel blocker", "Nitrate", "Statin"],
            kind="old", src=SRC,
            explain='''ยาที่ **ลดการตาย** ใน HFrEF คือ **ACEI/ARB/ARNI**, beta-blocker, MRA และ SGLT2i → ในตัวเลือกมีเพียง **ACE inhibitor**
- Digoxin ลดการนอนโรงพยาบาลและลดอาการ แต่ไม่ลดการตาย
- CCB ไม่ลดตาย และ non-DHP CCB ทำให้ HFrEF แย่ลง
- Nitrate เดี่ยว ๆ ไม่ลดตาย (hydralazine + nitrate ลดตายเฉพาะกลุ่มที่ใช้ ACEI/ARB ไม่ได้)
- Statin ใช้ตามข้อบ่งชี้ของ ASCVD ไม่ได้ลดการตายจาก HF''',
            pearl="HFrEF ลดตาย = ACEI/ARNI, BB, MRA, SGLT2i", topic="Chronic HFrEF",
            ref=R(141, 142, 143), nl=["2.3.9(5)"]),
    ])

LECTURE = lecture("01", "Cardio", "IE · NSTEMI · dissection · myocarditis · syncope · HT · HF",
    objectives=[
        "จับ pattern IE จากลิ้นหัวใจผิดปกติ + ไข้ + embolic sign",
        "แยก NSTEMI, dissection และ myocarditis จากโจทย์เจ็บอกได้",
        "เลือก synchronized cardioversion เมื่อ tachycardia unstable",
        "เลือกยา HT ตามโรคร่วม และยาลดการตายใน HFrEF",
    ],
    sections=[S1, S2, S3, S4, S5])
