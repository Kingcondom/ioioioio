from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Endocrine"
NLL = ["2.3.9(3)", "B7.4(8)"]

# ---------------------------------------------------------------- 07-01 FH, risk & lifestyle
S1 = sec("endo-07-01", "Familial hypercholesterolemia, Thai CV risk และ lifestyle modification",
    "FH: ผู้ใหญ่ TC ≥290 หรือ LDL ≥190 + ญาติสายตรงเป็น CVD ก่อนวัย (ชาย <55 หญิง <65) ± xanthoma · LDL = TC − HDL − TG/5 · eruptive xanthoma → lipid profile (TG สูงมาก) · อาหาร fiber สูง ลด saturated fat", minutes=8,
    source=f"{D} หน้า 296–301, 314–317", nl=NLL + ["B7.3(1)"],
    md='''
### Familial hypercholesterolemia (FH) (สไลด์หน้า 296)
- กลไก: mutation ของ **LDL receptor** (บ่อยสุด), ApoB หรือ PCSK9 → กำจัด LDL ไม่ได้ (autosomal dominant) (เสริม)
- เกณฑ์ (แบบ Simon Broome):
  - **Cholesterol สูง**: **ผู้ใหญ่ TC ≥ 290 หรือ LDL ≥ 190 mg/dL** · **เด็ก < 16 ปี TC ≥ 260 หรือ LDL ≥ 155**
  - **ประวัติครอบครัว premature CVD**: ญาติสายตรง **ชาย < 55 ปี** · **หญิง < 65 ปี**
  - **Xanthoma** (tendon xanthoma ที่ Achilles/หลังมือ), corneal arcus อายุน้อย (เสริม)
- รักษา: **high-intensity statin** (± ezetimibe, PCSK9 inhibitor) · **คัดกรองญาติ (cascade screening)** (เสริม)

### การประเมินความเสี่ยง (สไลด์หน้า 297 เป็นภาพ) (เสริม)
- **Thai CV risk score** (กรมการแพทย์/รามาธิบดี): ใช้ **อายุ เพศ สูบบุหรี่ DM SBP** และ **TC** (หรือรอบเอว/ส่วนสูงเมื่อไม่มีผลเลือด) → ความเสี่ยงเกิด CVD ใน 10 ปี · **≥ 10% = เสี่ยงสูง** ควรได้ statin
- **Risk enhancer** ที่ทำให้ควรให้ statin แม้ score < 10% (สไลด์หน้า 303): **ประวัติครอบครัว premature CVD**, **psoriasis, RA, HIV** (chronic inflammatory disease)
- กลุ่มที่ **ไม่ต้องคำนวณ score** (ให้ยาตามเกณฑ์เลย): **clinical ASCVD**, **LDL ≥ 190**, **DM**, **CKD**

### การคำนวณ LDL (Friedewald) (สไลด์หน้า 317)
- **LDL = TC − HDL − (TG/5)** · ใช้ไม่ได้เมื่อ **TG > 400** (ให้วัด direct LDL) (เสริม)

### Lifestyle modification (สไลด์หน้า 298–301 เป็นภาพ) (เสริม)
- อาหาร: **ลด saturated fat (< 7% ของพลังงาน)**, เลี่ยง trans fat · **เพิ่ม fiber (soluble fiber 10–25 g/วัน)**, ผัก ผลไม้ ธัญพืชไม่ขัดสี · **ลดเกลือ** (ถ้ามี HT) · ลดน้ำตาล/คาร์โบไฮเดรตขัดสีและแอลกอฮอล์เมื่อ TG สูง
- **ออกกำลังกายแบบแอโรบิก ≥ 150 นาที/สัปดาห์** · **ลดน้ำหนัก** 5–10% · **เลิกบุหรี่**

### Hypertriglyceridemia
- **Eruptive xanthoma** (ตุ่มเหลืองแดงที่ก้น/ข้อศอก) = **TG สูงมาก (มัก> 1,000)** → ส่ง **lipid profile** และหาสาเหตุทุติยภูมิ (DM คุมไม่ได้, แอลกอฮอล์, hypothyroid, ยา)
- **TG > 500 → fibrate** เพื่อ **ป้องกัน acute pancreatitis** (สไลด์หน้า 313)
''',
    pearls=[
        "FH: LDL ≥190 (เด็ก ≥155) + ญาติ CVD ก่อนวัย (ชาย <55 หญิง <65) ± tendon xanthoma",
        "LDL = TC − HDL − TG/5 (ใช้ไม่ได้ถ้า TG >400)",
        "Thai CV risk ≥10% → statin · risk enhancer: FHx premature CVD, psoriasis, RA, HIV",
        "Eruptive xanthoma = TG สูงมาก → lipid profile · TG >500 → fibrate",
        "อาหาร: fiber สูง ลด saturated fat",
    ],
    items=[
        mcq("ENDO-07-01-1",
            "A patient presents with multiple crops of small yellow-red papules on the buttocks and extensor surfaces of the elbows, consistent with eruptive xanthomas. Which investigation should be sent?",
            "Lipid profile",
            ["Complete blood count", "HbA1c only", "Serum electrolytes", "Skin biopsy for fungal culture"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ข้อสอบเป็นภาพ)",
            explain='''**Eruptive xanthoma** เกิดจาก **triglyceride สูงมาก** (chylomicron) → ส่ง **lipid profile** เป็นอันดับแรก แล้วหาสาเหตุทุติยภูมิ (เช่น DM ที่คุมไม่ได้ ซึ่งอาจตรวจ HbA1c ตามมา)
- CBC และ electrolytes ไม่ได้ช่วยวินิจฉัย
- HbA1c อย่างเดียวไม่ได้ยืนยันภาวะไขมันสูงซึ่งเป็นตัวการโดยตรง
- Skin biopsy ไม่จำเป็นเมื่อลักษณะทางคลินิกชัด''',
            pearl="Eruptive xanthoma → TG สูงมาก → lipid profile", topic="Eruptive xanthoma",
            ref=[f"{D} หน้า 314–315"], nl=["B7.3(1)", "2.3.9(3)"]),
        mcq("ENDO-07-01-2",
            "A 40-year-old woman comes for a health check-up. FPG 116 mg/dL, HbA1c 6.0%, triglyceride 250, total cholesterol 250, HDL 50 mg/dL. BP 140/90 mmHg, height 160 cm, weight 80 kg, waist 94 cm. Apart from exercise advice, what is the most appropriate dietary recommendation?",
            "High-fiber diet",
            ["High-protein diet", "High-carbohydrate diet", "Normal sodium intake", "Normal saturated fat intake"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ผู้ป่วยมี **metabolic syndrome** (รอบเอวเกิน, BP สูง, TG สูง, FPG 100–125 = prediabetes) · LDL = 250 − 50 − 250/5 = **150 mg/dL** · อาหาร **fiber สูง** ช่วยลด LDL น้ำตาลและน้ำหนัก
- High-protein diet ไม่ใช่คำแนะนำมาตรฐาน
- High-carbohydrate (โดยเฉพาะขัดสี) เพิ่ม TG และน้ำตาล
- BP 140/90 ควร **ลด** sodium ไม่ใช่กินปกติ
- LDL 150 ควร **ลด** saturated fat''',
            pearl="Metabolic syndrome: fiber สูง ลดเกลือ ลด saturated fat", topic="Diet",
            ref=[f"{D} หน้า 298–301, 316–317"], nl=["2.3.4(6)", "2.3.9(3)"]),
        mcq("ENDO-07-01-3",
            "A 35-year-old man's father and brother both had myocardial infarction before age 50. He has thickened Achilles tendons. Total cholesterol 370, TG 250, HDL 70, LDL 250 mg/dL. What is the most appropriate management?",
            "Lifestyle modification plus high-intensity statin",
            ["Lifestyle modification and follow-up in 6 months", "Lifestyle modification plus fibrate", "Lifestyle modification plus statin plus fibrate", "Lifestyle modification plus omega-3 fatty acids"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**LDL ≥ 190 + ญาติสายตรงเป็น CVD ก่อนวัย + tendon xanthoma** = **possible/probable FH** → **lifestyle + high-intensity statin** เป้า **LDL < 70 และลด ≥ 50%** (ตามสไลด์)
- Lifestyle อย่างเดียวไม่พอสำหรับ LDL 250 ที่เกิดจาก genetic
- Fibrate ใช้เมื่อ TG > 500 — TG 250 ไม่ใช่ปัญหาหลัก
- Statin + fibrate เพิ่มความเสี่ยง myopathy โดยไม่มีข้อบ่งชี้
- Omega-3 ไม่ได้ลด LDL''',
            pearl="FH → high-intensity statin, LDL <70 & ↓≥50%", topic="FH",
            ref=[f"{D} หน้า 296, 326–328"], nl=NLL),
        mcq_ordered("ENDO-07-01-4",
            "A 45-year-old man has total cholesterol 230, HDL 40 and triglyceride 150 mg/dL (fasting). What is his calculated LDL cholesterol?",
            ["40 mg/dL", "130 mg/dL", "160 mg/dL", "190 mg/dL", "200 mg/dL"], 2,
            explain='''Friedewald: **LDL = TC − HDL − TG/5** = 230 − 40 − 150/5 = 230 − 40 − 30 = **160 mg/dL**
- 40 mg/dL เกิดจากหัก TG ทั้งค่าโดยไม่หาร 5
- 130 mg/dL เกิดจากหัก TG/5 ซ้ำสองครั้ง
- 190 mg/dL เกิดจากลืมหัก TG/5
- 200 mg/dL เกิดจากลืมหัก HDL

(สูตรนี้ใช้ไม่ได้ถ้า TG > 400 mg/dL)''',
            pearl="LDL = TC − HDL − TG/5", topic="Friedewald",
            ref=[f"{D} หน้า 317"], nl=["B7.3(1)"]),
    ])

# ---------------------------------------------------------------- 07-02 Statin indications & goals
F_GOAL = fig("endo-07-02-f1", "ใครควรได้ statin และเป้า LDL (ตามสไลด์)", '''<svg viewBox="0 0 750 470">
 <rect x="10" y="10" width="730" height="34" rx="8" class="sunk"/>
 <text x="22" y="32" class="tb">กลุ่ม</text>
 <text x="352" y="32" class="tb">Statin</text>
 <text x="560" y="32" class="tb">เป้า LDL (mg/dL)</text>
 <rect x="10" y="52" width="730" height="74" rx="8" class="badsoft"/>
 <text x="22" y="74" class="tb">Secondary · ACS / CAD</text>
 <text x="22" y="94" class="t3">เคย MI, NSTEMI, revascularization</text>
 <text x="352" y="84" class="t2">High intensity</text>
 <text x="560" y="78" class="ta">&lt; 55 และ ↓ ≥ 50%</text>
 <text x="560" y="98" class="t3">เอาค่าที่ต่ำกว่า</text>
 <rect x="10" y="134" width="730" height="74" rx="8" class="badsoft"/>
 <text x="22" y="156" class="tb">Secondary · Ischemic stroke / TIA</text>
 <text x="22" y="176" class="t3">LDL ≥ 100 · ถ้ามี atherosclerosis / stenosis &gt; 50% เข้มขึ้น</text>
 <text x="352" y="166" class="t2">High intensity</text>
 <text x="560" y="160" class="ta">&lt; 100</text>
 <text x="560" y="180" class="t3">atherosclerotic: &lt; 70 (เสริม)</text>
 <rect x="10" y="216" width="730" height="74" rx="8" class="misssoft"/>
 <text x="22" y="238" class="tb">LDL ≥ 190 (อายุ ≥ 21)</text>
 <text x="22" y="258" class="t3">+ FHx premature CVD = possible FH</text>
 <text x="352" y="238" class="t2">Moderate (–high)</text>
 <text x="352" y="258" class="t2">possible FH → High</text>
 <text x="560" y="238" class="ta">&lt; 100 และ ↓ ≥ 50%</text>
 <text x="560" y="258" class="ta">FH: &lt; 70 และ ↓ ≥ 50%</text>
 <rect x="10" y="298" width="730" height="74" rx="8" class="c1soft"/>
 <text x="22" y="320" class="tb">DM อายุ ≥ 40, LDL &lt; 190</text>
 <text x="22" y="340" class="t3">0–1 risk · DM &gt; 10 ปี / risk หลายข้อ เข้มขึ้น</text>
 <text x="352" y="330" class="t2">Moderate</text>
 <text x="560" y="324" class="ta">&lt; 100 และ ↓ ≥ 30%</text>
 <text x="560" y="344" class="t3">high risk: &lt; 70 (เสริม)</text>
 <rect x="10" y="380" width="730" height="80" rx="8" class="oksoft"/>
 <text x="22" y="402" class="tb">ไม่มี DM/CKD · อายุ ≥ 35, LDL &lt; 190</text>
 <text x="22" y="422" class="t3">Thai CV risk ≥ 10% หรือ &lt; 10% + risk enhancer</text>
 <text x="22" y="440" class="t3">(FHx premature CVD, psoriasis, RA, HIV)</text>
 <text x="352" y="416" class="t2">Low–moderate</text>
 <text x="560" y="410" class="ta">&lt; 100 และ ↓ ≥ 30%</text>
 <text x="560" y="430" class="t3">ไม่มี risk → lifestyle</text>
</svg>''', "แถวบนสุดเสี่ยงสูงสุด — ยิ่งเสี่ยงยิ่งใช้ statin แรงขึ้นและเป้า LDL ต่ำลง · ตัวเลขตามเฉลยในสไลด์ (แนวทาง RCPT/ESC)")

S2 = sec("endo-07-02", "Dyslipidemia: ใครควรได้ statin และเป้า LDL",
    "ACS → high-intensity, LDL <55 & ↓≥50% · stroke/TIA LDL ≥100 → high-intensity, <100 · LDL ≥190 → statin · possible FH → <70 · DM ≥40 → statin <100 · อายุ ≥35 + Thai CV risk ≥10% หรือมี risk enhancer → statin", minutes=10,
    source=f"{D} หน้า 302–307, 318–341", nl=NLL + ["2.3.4(1)"],
    md='''
### หลักใหญ่ (สไลด์หน้า 302–307)
- ประเมินเป็นกลุ่ม: **secondary prevention** (มี ASCVD แล้ว) → **LDL ≥ 190** → **DM** → **CKD** → คนทั่วไปใช้ **Thai CV risk score**
- **"Goal LDL อะไรน้อยกว่าเอาเลขนั้น"** — เช่น ACS ต้องได้ทั้ง < 55 **และ** ลด ≥ 50% เลือกค่าที่ต่ำกว่า

[[fig:endo-07-02-f1]]

### รายละเอียดแต่ละกลุ่ม

| กลุ่ม (สไลด์) | การรักษา | เป้า LDL |
|---|---|---|
| **ACS / CAD** (หน้า 306, 325) | **High-intensity statin** | **< 55 mg/dL และลด ≥ 50%** |
| **Ischemic stroke/TIA** ที่ **LDL ≥ 100** (หน้า 307, 320) | **High-intensity statin** | **< 100** · มี atherosclerotic disease หรือ carotid/intracranial stenosis > 50% → เข้มขึ้น (< 70 — เสริม) |
| **Possible FH** (LDL ≥ 190 + FHx premature CVD) (หน้า 328) | **High-intensity statin** | **< 70 และลด ≥ 50%** |
| **อายุ ≥ 21, LDL ≥ 190** (หน้า 333) | **Moderate**-intensity statin (ขึ้นไป) | **< 100 และลด ≥ 50%** |
| **DM อายุ ≥ 40, LDL < 190, risk 0–1** (หน้า 48, 304) | Statin (moderate) | **< 100 และลด ≥ 30%** · **DM > 10 ปี**/risk หลายข้อ = เสี่ยงสูงขึ้น |
| **CKD** (หน้า 305 เป็นภาพ) | Statin ± ezetimibe ใน CKD ที่ยังไม่ dialysis อายุ ≥ 50 (เสริม) | < 100 (เสริม) |
| **อายุ ≥ 35, LDL < 190, Thai CV risk < 10% + risk enhancer** (หน้า 303, 336) | **Low–moderate**-intensity statin | **< 100 และลด ≥ 30%** |

- แนวทางเบาหวานปัจจุบัน **ไม่ได้ตั้งเป้า TC, HDL, TG ชัดเจน — เน้น LDL** (สไลด์หน้า 341)
- ก่อนเริ่มยาในคนที่ไม่มีอาการ: BP ครั้งเดียวสูง → ยืนยันด้วย HBPM/ABPM · FBS ครั้งเดียวสูง ไม่มีอาการ → ตรวจซ้ำก่อนวินิจฉัย DM (สไลด์หน้า 330)

> หลายข้อสอบให้ตัวเลือก **simvastatin vs atorvastatin**: secondary prevention (MI, stroke) → **atorvastatin 40–80 / rosuvastatin 20–40 (high-intensity)** · primary prevention ทั่วไป → simvastatin 20–40 (moderate) ก็ได้
''',
    figs=[F_GOAL],
    pearls=[
        "ACS/CAD → high-intensity statin, LDL <55 และ ↓≥50%",
        "Stroke/TIA LDL ≥100 → high-intensity, LDL <100",
        "LDL ≥190 → statin เลย (ไม่ต้องคำนวณ risk) · + FHx premature CVD → high-intensity <70",
        "DM ≥40 ปี → statin เป้า <100 ↓≥30%",
        "เป้า LDL: เลือกค่าที่ต่ำกว่าระหว่างตัวเลขกับ % ที่ลด",
    ],
    items=[
        mcq("ENDO-07-02-1",
            "A 65-year-old man with a previous cerebral infarction has total cholesterol 220, TG 200, HDL 50, LDL 130 mg/dL. What is the most appropriate management?",
            "Atorvastatin (high-intensity)",
            ["Simvastatin 10 mg", "Lifestyle modification alone", "Niacin", "Fibrate"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Secondary prevention หลัง **ischemic stroke** ที่ **LDL ≥ 100** → **high-intensity statin** (atorvastatin 40–80 mg) เป้า LDL < 100 (หรือ < 70 ถ้ามี atherosclerotic disease)
- Simvastatin 10 mg เป็น low-intensity ไม่พอสำหรับ secondary prevention
- Lifestyle อย่างเดียวไม่พอ
- Niacin และ fibrate ไม่ได้ลด CV event เมื่อเพิ่มเข้ามา และไม่ใช่ยาแรกในการลด LDL''',
            pearl="Ischemic stroke + LDL ≥100 → atorvastatin high-intensity", topic="Stroke secondary prevention",
            ref=[f"{D} หน้า 307, 318–320"], nl=NLL + ["2.2.39"]),
        mcq("ENDO-07-02-2",
            "A 60-year-old woman with well-controlled diabetes had an episode of arm and leg weakness from an ischemic stroke. Total cholesterol 220, TG 200, HDL 55, LDL 150 mg/dL. What is the most appropriate management?",
            "Atorvastatin 40–80 mg/day",
            ["Lifestyle modification alone", "Simvastatin 10 mg/day", "Gemfibrozil", "Ezetimibe alone"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''DM + **ischemic stroke** = secondary prevention, LDL 150 ≥ 100 → **high-intensity statin (atorvastatin 40–80)**
- Lifestyle อย่างเดียวไม่พอ
- Simvastatin ขนาดต่ำเป็น low-intensity (simvastatin สูงสุดที่แนะนำ 40 mg ยังเป็นแค่ moderate)
- Gemfibrozil ลด TG ไม่ใช่ยาหลัก และเสี่ยง myopathy เมื่อใช้ร่วม statin
- Ezetimibe ใช้เสริมเมื่อ statin เต็มที่แล้วยังไม่ถึงเป้า''',
            pearl="DM + stroke → high-intensity statin", topic="High-intensity statin",
            ref=[f"{D} หน้า 321–322"], nl=NLL),
        mcq("ENDO-07-02-3",
            "A patient with a previous NSTEMI is followed in the outpatient clinic. LDL is 150 mg/dL. Which medication is most appropriate?",
            "Atorvastatin 40 mg/day",
            ["Simvastatin 20 mg/day", "Ezetimibe 10 mg/day", "Metformin 1,000 mg/day", "Propranolol 120 mg/day"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''หลัง **ACS** → **high-intensity statin** เป้า **LDL < 55 และลด ≥ 50%** · atorvastatin 40 mg เป็น high-intensity (40–80 mg)
- Simvastatin 20 mg เป็น moderate-intensity
- Ezetimibe เดี่ยวลด LDL ได้เพียง ~20% ใช้เสริม statin
- Metformin ไม่เกี่ยวกับ LDL
- Propranolol เป็นยาหลัง MI แต่ไม่ได้รักษา LDL ที่โจทย์ถาม''',
            pearl="หลัง ACS → atorvastatin 40–80 (เป้า LDL <55)", topic="ACS",
            ref=[f"{D} หน้า 306, 323–325"], nl=NLL),
        mcq("ENDO-07-02-4",
            "A healthy 45-year-old Thai man at an annual check-up has TG 210, LDL 200, HDL 30 mg/dL. He has no diabetes, CKD or vascular disease, and no family history of premature cardiovascular disease. What is the most appropriate drug?",
            "Simvastatin",
            ["Gemfibrozil", "Fenofibrate", "Niacin", "Cholestyramine"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**อายุ ≥ 21 + LDL ≥ 190** → ให้ statin เลยโดยไม่ต้องคำนวณ risk (สไลด์: moderate-intensity statin เป้า LDL < 100 และลด ≥ 50%) · ในตัวเลือก statin มีตัวเดียวคือ **simvastatin**
- Gemfibrozil/fenofibrate ใช้ลด TG (TG > 500) ไม่ใช่ปัญหาหลัก
- Niacin ไม่ลด event และมีผลข้างเคียงมาก
- Cholestyramine ลด LDL ได้น้อยกว่า statin และทำ TG สูงขึ้น''',
            pearl="LDL ≥190 → statin ทันที", topic="LDL ≥190",
            ref=[f"{D} หน้า 331–333"], nl=NLL),
        mcq("ENDO-07-02-5",
            "A previously healthy 40-year-old woman comes for an annual check-up. Her father had a myocardial infarction at age 50. Examination is normal. FBS 110 mg/dL, TG 400, HDL 40, LDL 130 mg/dL. Her Thai CV risk score is 4%. Besides lifestyle modification, what is the most appropriate management?",
            "Low- to moderate-intensity statin such as simvastatin",
            ["Diet control alone", "Exercise alone", "Diet control and exercise only, recheck in 1 year", "Glipizide"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ปรับอายุบิดาเป็น 50 ปีให้ตรงเกณฑ์ premature)",
            explain='''อายุ ≥ 35, LDL < 190, Thai CV risk < 10% **แต่มี risk enhancer = บิดาเป็น MI ก่อนอายุ 55** → **low–moderate-intensity statin** เป้า **LDL < 100 และลด ≥ 30%** (ตามสไลด์)
- Diet หรือ exercise อย่างเดียว หรือทั้งสองโดยไม่ให้ยา เหมาะกับคนที่ไม่มี risk enhancer
- Glipizide ไม่มีที่ใช้ — FBS 110 เป็นแค่ IFG

(โจทย์เดิมในสไลด์ระบุบิดาเสียชีวิตอายุ 55 ซึ่งพอดีขอบเกณฑ์ "ชาย < 55" จึงปรับเป็น 50 ให้ตอบได้ชัด)''',
            pearl="Risk < 10% + FHx premature CVD → statin", topic="Risk enhancer",
            ref=[f"{D} หน้า 303, 334–336"], nl=NLL),
        mcq("ENDO-07-02-6",
            "A 35-year-old man's father has type 2 diabetes and had ischemic heart disease at 45 years. BP 140/90 mmHg (single office reading), weight 90 kg, height 175 cm, acanthosis nigricans. FBS 140 mg/dL (single test, asymptomatic), total cholesterol 300, LDL 190, HDL 30 mg/dL, AST 80, ALT 75 U/L. What is the most appropriate management now?",
            "Simvastatin plus lifestyle modification",
            ["Enalapril", "Metformin", "Fenofibrate", "Lifestyle modification alone"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**LDL ≥ 190 + บิดาเป็น IHD ก่อน 55 ปี** = possible FH → **statin** (ควรเป็น high-intensity ตามสไลด์; ตัวเลือกที่เป็น statin มีตัวเดียว) · AST/ALT สูงไม่ถึง 3 เท่า (น่าจะ NAFLD) ไม่ใช่ข้อห้าม
- Enalapril: BP 140/90 ครั้งเดียว ต้องยืนยันด้วย HBPM/ABPM ก่อนวินิจฉัย HT
- Metformin: FBS 140 ครั้งเดียวไม่มีอาการ ต้องตรวจซ้ำก่อนวินิจฉัย DM
- Fenofibrate ไม่ใช่ยาหลักเมื่อปัญหาคือ LDL
- Lifestyle อย่างเดียวไม่พอสำหรับ possible FH''',
            pearl="ข้อมูลเดียวที่ยืนยันแล้วคือ LDL ≥190 + FHx → statin", topic="Possible FH",
            ref=[f"{D} หน้า 329–330"], nl=NLL),
        mcq("ENDO-07-02-7",
            "A 47-year-old man is found to have blood sugar 250 mg/dL (diabetes confirmed). Total cholesterol 193, TG 180, HDL 30, LDL 130 mg/dL. He has no known vascular disease. Which statement best describes his atherosclerotic risk category and treatment goal?",
            "High risk; LDL <100 mg/dL",
            ["Very high risk; LDL <70 mg/dL", "Very high risk; LDL <70 and HDL >40 mg/dL", "Very high risk; LDL <70, HDL >40 and TG <150 mg/dL", "High risk; LDL <100, HDL >40 and TG <150 mg/dL"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''DM อายุ ≥ 40 ไม่มี ASCVD ไม่มี target organ damage = **high risk** → statin เป้า **LDL < 100** (และลด ≥ 30%) · แนวทางปัจจุบัน **เน้น LDL ไม่ได้ตั้งเป้า HDL หรือ TG** (สไลด์หน้า 341)
- Very high risk ใช้กับผู้ที่มี ASCVD แล้ว หรือ DM ร่วมกับ target organ damage/ปัจจัยเสี่ยงหลายข้อ
- ตัวเลือกที่ใส่เป้า HDL/TG ไม่ตรงกับแนวทางปัจจุบัน''',
            pearl="DM ไม่มี ASCVD = high risk, LDL <100 · ไม่มีเป้า HDL/TG", topic="DM risk category",
            ref=[f"{D} หน้า 337–341"], nl=NLL + ["2.3.4(1)"]),
    ])

# ---------------------------------------------------------------- 07-03 Drugs & statin adverse effects
F_MYO = fig("endo-07-03-f1", "ปวดกล้ามเนื้อขณะกิน statin", '''<svg viewBox="0 0 740 330">
 <defs><marker id="endo-07-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="240" y="10" width="260" height="44" rx="10" class="acsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">Statin + ปวด/อ่อนแรงกล้ามเนื้อ</text>
 <text x="370" y="46" text-anchor="middle" class="t3">ส่ง CK · TSH · Cr · ทบทวนยาที่ใช้ร่วม</text>
 <path d="M290 54L120 90" class="ln" marker-end="url(#endo-07-03-a)"/>
 <path d="M370 54V90" class="ln" marker-end="url(#endo-07-03-a)"/>
 <path d="M450 54L620 90" class="ln" marker-end="url(#endo-07-03-a)"/>
 <rect x="10" y="92" width="230" height="110" rx="10" class="oksoft"/>
 <text x="125" y="114" text-anchor="middle" class="tb">Myalgia</text>
 <text x="125" y="134" text-anchor="middle" class="t2">CK ปกติ</text>
 <text x="22" y="160" class="t3">ทนได้ → ให้ต่อ/ลดขนาด</text>
 <text x="22" y="178" class="t3">ทนไม่ได้ → หยุดจนหาย</text>
 <text x="22" y="196" class="t3">แล้วเปลี่ยน statin ตัวอื่น</text>
 <rect x="255" y="92" width="230" height="110" rx="10" class="misssoft"/>
 <text x="370" y="114" text-anchor="middle" class="tb">Myositis / myopathy</text>
 <text x="370" y="134" text-anchor="middle" class="t2">CK สูง &lt; 10 × ULN</text>
 <text x="267" y="160" class="t3">หยุด/ลดขนาด หา interaction</text>
 <text x="267" y="178" class="t3">ติดตาม CK และอาการ</text>
 <rect x="500" y="92" width="230" height="110" rx="10" class="badsoft"/>
 <text x="615" y="114" text-anchor="middle" class="tb">Rhabdomyolysis</text>
 <text x="615" y="134" text-anchor="middle" class="t2">CK &gt; 10 × ULN ± AKI</text>
 <text x="512" y="160" class="t3">หยุด statin ทันที</text>
 <text x="512" y="178" class="t3">IV fluid · ตรวจ Cr, K</text>
 <rect x="10" y="218" width="720" height="104" rx="10" class="sunk"/>
 <text x="22" y="242" class="tb">ปัจจัยเสี่ยง</text>
 <text x="22" y="264" class="t2">Gemfibrozil (ห้ามคู่ statin — ใช้ fenofibrate) · CYP3A4 inhibitor: macrolide, azole, protease inhibitor</text>
 <text x="22" y="286" class="t2">Simvastatin + amlodipine/diltiazem/verapamil (จำกัด simva ≤ 20 mg กับ amlodipine) · grapefruit</text>
 <text x="22" y="308" class="t3">Hypothyroidism · CKD · สูงอายุ ผอม · ขนาดยาสูง</text>
</svg>''', "แบ่งตามระดับ CK — myalgia CK ปกติยังใช้ statin ต่อได้ แต่ CK > 10 เท่าต้องหยุดทันที และทุกรายให้ทบทวนยาที่ใช้ร่วม")

S3 = sec("endo-07-03", "ยาลดไขมันและผลข้างเคียงของ statin",
    "High-intensity: atorva 40–80, rosuva 20–40 · moderate: simva 20–40, atorva 10–20 · เสริม ezetimibe, PCSK9i · TG >500 → fibrate · statin myopathy: simva + amlodipine/gemfibrozil/CYP3A4 → ส่ง CK", minutes=8,
    source=f"{D} หน้า 308–313, 342–347", nl=NLL,
    md='''
### ยาลด LDL (สไลด์หน้า 308–310 เป็นภาพ) (เสริม)

| ยา | ลด LDL | หมายเหตุ |
|---|---|---|
| **Statin** (HMG-CoA reductase inhibitor) | 30–> 50% | ยาหลัก ลด CV event |
| **Ezetimibe** | ~20–25% | ยับยั้งการดูดซึม cholesterol ที่ลำไส้ (NPC1L1) · เสริม statin |
| **PCSK9 inhibitor** (evolocumab, alirocumab — ฉีด) | ~60% | FH/very high risk ที่ไม่ถึงเป้า |
| Bile acid sequestrant (cholestyramine) | 15–25% | **TG สูงขึ้น**, ท้องผูก, รบกวนการดูดซึมยาอื่น |
| Niacin | 15–20% | หน้าแดง, gout, hyperglycemia — ไม่ลด event |

### Statin intensity (สไลด์หน้า 311–312 เป็นภาพ — ตาม ACC/AHA) (เสริม)

| High (ลด ≥ 50%) | Moderate (30–49%) | Low (< 30%) |
|---|---|---|
| **Atorvastatin 40–80** | **Atorvastatin 10–20** | **Simvastatin 10** |
| **Rosuvastatin 20–40** | Rosuvastatin 5–10 | Pravastatin 10–20 |
| | **Simvastatin 20–40** | Fluvastatin 20–40 |
| | Pravastatin 40–80, pitavastatin 1–4 | |

### ยาลด TG (สไลด์หน้า 313)
- **Fibrate แนะนำเมื่อ TG > 500 mg/dL** เพื่อ **ป้องกัน pancreatitis** · ร่วมกับ statin ให้ใช้ **fenofibrate** (ไม่ใช้ **gemfibrozil** — ยับยั้ง glucuronidation ของ statin → myopathy) (เสริม)
- Omega-3 (icosapent ethyl) ในผู้เสี่ยงสูงที่ TG สูงค้าง (เสริม) · แก้สาเหตุทุติยภูมิ: คุมน้ำตาล งดสุรา

### ผลข้างเคียงของ statin (สไลด์หน้า 343, 346 เป็นภาพ)

[[fig:endo-07-03-f1]]

- **Statin-associated muscle symptoms**: myalgia (CK ปกติ) → myositis (CK สูง) → **rhabdomyolysis** (CK > 10 × ULN, myoglobinuria, AKI)
- **Hepatotoxicity**: transaminase สูง — หยุดเมื่อ **ALT > 3 × ULN** (ไม่ต้องตรวจ LFT routine ทุกครั้ง) · fatty liver ไม่ใช่ข้อห้าม (เสริม)
- **New-onset DM** เล็กน้อย (ประโยชน์มากกว่า) (เสริม)
- **Drug interactions ที่ออกสอบ**: **simvastatin + amlodipine** (simva ≤ 20 mg — และ amlodipine ขนาดสูงสุดเพียง 10 mg/วัน) · **statin + gemfibrozil** · simva/atorva + **macrolide (clarithromycin), azole, HIV protease inhibitor**, diltiazem/verapamil, grapefruit
- เมื่อมีอาการกล้ามเนื้อ → **ส่ง CK** (และ TSH — hypothyroid เพิ่มความเสี่ยง)
''',
    figs=[F_MYO],
    pearls=[
        "High-intensity = atorvastatin 40–80, rosuvastatin 20–40",
        "Simvastatin 20–40 = moderate · 10 = low",
        "TG >500 → fibrate (กัน pancreatitis) · คู่ statin ใช้ fenofibrate ไม่ใช่ gemfibrozil",
        "Statin + ปวดกล้ามเนื้อ → CK · >10 × ULN หยุดทันที",
        "Simvastatin + amlodipine/diltiazem/macrolide/gemfibrozil → myopathy",
    ],
    items=[
        mcq("ENDO-07-03-1",
            "A 50-year-old man with diabetes, hypertension and dyslipidemia takes amlodipine 20 mg/day, simvastatin 40 mg/day and metformin 500 mg/day. He complains of muscle pain. BP 140/70 mmHg. Motor power grade IV in all limbs, intact sensation, DTR 2+, plantar flexor. AST 20, ALT 32 U/L, CK 300 U/L. What is the most likely diagnosis?",
            "Drug-induced (statin) myopathy",
            ["Pyomyositis", "Fibromyalgia", "Diabetic peripheral neuropathy", "Hypothyroid myopathy"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ปวดและอ่อนแรงกล้ามเนื้อทั่วตัว + CK สูง ในผู้ที่ได้ **simvastatin 40 mg ร่วมกับ amlodipine** (amlodipine ยับยั้ง CYP3A4 เพิ่มระดับ simvastatin — ควรจำกัด simva ≤ 20 mg และ amlodipine เกินขนาดสูงสุด 10 mg) → **statin-induced myopathy**
- Pyomyositis มีไข้ กล้ามเนื้อบวมแดงเฉพาะที่
- Fibromyalgia มี tender points ไม่มีอ่อนแรงและ CK ปกติ
- Peripheral neuropathy มีชา sensory ผิดปกติ reflex ลด แต่รายนี้ sensory ปกติ DTR 2+
- Hypothyroid myopathy เป็นได้ (CK สูง) แต่ไม่มีอาการอื่นของ hypothyroid และมี interaction ของยาชัดเจน''',
            pearl="Simvastatin + amlodipine + ปวดกล้ามเนื้อ CK สูง = statin myopathy", topic="Statin myopathy",
            ref=[f"{D} หน้า 342–344"], nl=NLL),
        mcq("ENDO-07-03-2",
            "An elderly man has had pain and weakness of the extremities with difficulty getting up from the floor for 3 weeks. Over the last 3 months he started simvastatin, gemfibrozil and amlodipine. PR 80/min, BP 150/100 mmHg. No facial palsy; proximal weakness grade IV/V, DTR 1+, plantar flexor. What is the most appropriate investigation?",
            "Serum creatine kinase",
            ["Serum potassium", "Edrophonium (Tensilon) test", "CT brain", "Lumbar puncture"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**Simvastatin + gemfibrozil** (gemfibrozil ยับยั้ง glucuronidation ของ statin) ± amlodipine → เสี่ยง **statin myopathy/rhabdomyolysis** → อ่อนแรง proximal + ปวดกล้ามเนื้อ → ส่ง **CK**
- Serum K ใช้หา periodic paralysis (เฉียบพลัน ไม่ปวด) แต่ประวัติยาชี้ไป statin
- Tensilon test ใช้ใน myasthenia gravis (fatigable, ptosis, diplopia) ไม่มีปวด
- CT brain ไม่เหมาะกับอ่อนแรงแบบ proximal ทั้งสี่ระยางค์
- LP ใช้ใน GBS (ascending, areflexia) — รายนี้ reflex ยังมี''',
            pearl="Statin + gemfibrozil + ปวดอ่อนแรง → CK", topic="Statin–fibrate interaction",
            ref=[f"{D} หน้า 345–347"], nl=NLL),
        mcq("ENDO-07-03-3",
            "A 52-year-old man with type 2 diabetes has fasting TG 1,150 mg/dL, LDL 90 mg/dL and recurrent epigastric pain. Besides glycemic control and alcohol abstinence, which drug is most appropriate to prevent pancreatitis?",
            "Fenofibrate",
            ["Ezetimibe", "Cholestyramine", "Rosuvastatin as sole therapy", "PCSK9 inhibitor"],
            explain='''**TG > 500 (โดยเฉพาะ > 1,000)** เสี่ยง **acute pancreatitis** → **fibrate** ลด TG ได้มากที่สุด (fenofibrate ปลอดภัยกว่า gemfibrozil เมื่อต้องใช้ร่วม statin)
- Ezetimibe และ PCSK9 inhibitor ลด LDL ไม่ได้ลด TG มาก
- Cholestyramine **เพิ่ม** TG — ห้ามใน TG สูง
- Statin ลด TG ได้บ้าง (10–30%) ไม่พอเมื่อ TG > 1,000''',
            pearl="TG >500 → fibrate กัน pancreatitis", topic="Hypertriglyceridemia",
            ref=[f"{D} หน้า 313"], nl=NLL),
        mcq("ENDO-07-03-4",
            "A 68-year-old man on atorvastatin 40 mg after myocardial infarction has LDL 95 mg/dL after 3 months of good adherence; he tolerates the drug well. His goal is LDL <55 mg/dL. What is the most appropriate next step?",
            "Increase atorvastatin to 80 mg (or add ezetimibe)",
            ["Switch to simvastatin 40 mg", "Add gemfibrozil", "Add niacin", "Stop the statin and start cholestyramine"],
            explain='''Secondary prevention ที่ยังไม่ถึงเป้า → **เพิ่ม statin เป็นขนาดสูงสุดที่ทนได้** (atorvastatin 80) และ/หรือ **เพิ่ม ezetimibe** · ไม่ถึงเป้าอีก → PCSK9 inhibitor (เสริม)
- Simvastatin 40 เป็น moderate-intensity → ลดความแรงลง
- Gemfibrozil ไม่ลด LDL มากและเสี่ยง myopathy
- Niacin ไม่ลด event และมีผลข้างเคียงมาก
- Cholestyramine ลด LDL ได้น้อยกว่า statin มาก''',
            pearl="ไม่ถึงเป้า LDL → max statin → + ezetimibe → PCSK9i", topic="Intensifying therapy",
            ref=[f"{D} หน้า 308–312"], nl=NLL),
    ])

LECTURE = lecture("07", "Familial hypercholesterolemia & dyslipidemia", "FH · Thai CV risk · statin indication & goal · lipid drugs",
    objectives=[
        "วินิจฉัย possible FH และคำนวณ LDL ด้วยสูตร Friedewald",
        "จัดกลุ่มความเสี่ยงและเลือก statin intensity พร้อมเป้า LDL ตามสไลด์ได้",
        "เลือกยาลด TG และรู้ว่าเมื่อไรต้องใช้ fibrate",
        "วินิจฉัยและจัดการ statin myopathy และ drug interaction ที่ออกสอบ",
    ],
    sections=[S1, S2, S3])
