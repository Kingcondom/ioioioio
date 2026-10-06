from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Nephro"

# ---------------------------------------------------------------- 06-01 Hyperkalemia
F_HK = fig("nephro-06-01-f1", "Hyperkalemia emergency: 3 ขั้นตอน", '''<svg viewBox="0 0 740 330">
 <defs><marker id="nephro-06-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="220" y="10" width="300" height="44" rx="10" class="badsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">K &gt; 5 + อ่อนแรง หรือ ECG เปลี่ยน</text>
 <text x="370" y="47" text-anchor="middle" class="t3">peaked T · wide QRS · P หาย · sine wave</text>
 <path d="M300 54L130 86" class="ln" marker-end="url(#nephro-06-01-a)"/>
 <path d="M370 54V86" class="ln" marker-end="url(#nephro-06-01-a)"/>
 <path d="M440 54L610 86" class="ln" marker-end="url(#nephro-06-01-a)"/>
 <rect x="10" y="88" width="230" height="46" rx="10" class="bad"/>
 <text x="125" y="108" text-anchor="middle" class="tw">STEP 1 · Stabilize</text>
 <text x="125" y="125" text-anchor="middle" class="tw">กันหัวใจหยุดเต้น</text>
 <rect x="255" y="88" width="230" height="46" rx="10" class="miss"/>
 <text x="370" y="108" text-anchor="middle" class="tw">STEP 2 · Shift</text>
 <text x="370" y="125" text-anchor="middle" class="tw">ดัน K เข้าเซลล์</text>
 <rect x="500" y="88" width="230" height="46" rx="10" class="c1"/>
 <text x="615" y="108" text-anchor="middle" class="tw">STEP 3 · Remove</text>
 <text x="615" y="125" text-anchor="middle" class="tw">เอา K ออกจากร่างกาย</text>
 <rect x="10" y="144" width="230" height="140" rx="10" class="badsoft"/>
 <text x="22" y="168" class="tb">10% Ca gluconate IV</text>
 <text x="22" y="190" class="t2">ออกฤทธิ์ใน 1–3 นาที</text>
 <text x="22" y="210" class="t2">ไม่ได้ลด K</text>
 <text x="22" y="230" class="t3">ซ้ำได้ถ้า ECG ยังผิดปกติ (เสริม)</text>
 <rect x="255" y="144" width="230" height="140" rx="10" class="misssoft"/>
 <text x="267" y="168" class="tb">50% glucose 50 ml</text>
 <text x="267" y="186" class="tb">+ RI 10 U IV</text>
 <text x="267" y="210" class="t2">NaHCO3 ถ้า acidosis</text>
 <text x="267" y="230" class="t2">β2-agonist NB</text>
 <text x="267" y="254" class="t3">ออกฤทธิ์ 15–30 นาที (เสริม)</text>
 <rect x="500" y="144" width="230" height="140" rx="10" class="c1soft"/>
 <text x="512" y="168" class="tb">Kalimate/Kayexalate</text>
 <text x="512" y="190" class="t2">Furosemide</text>
 <text x="512" y="210" class="t2">Hemodialysis</text>
 <text x="512" y="232" class="t3">ESRD/anuria → HD</text>
 <rect x="10" y="294" width="720" height="30" rx="8" class="sunk"/>
 <text x="370" y="314" text-anchor="middle" class="t2">ไม่ใช่ emergency (ไม่มีอาการ ECG ปกติ) → ทำแค่ STEP 3 ก็พอ</text>
</svg>''', "ทำจากซ้ายไปขวาตามลำดับ: Ca ป้องกันหัวใจก่อน แล้ว insulin + glucose ดัน K เข้าเซลล์ สุดท้ายเอา K ออกจริง")

F_HKC = fig("nephro-06-01-f2", "หาสาเหตุ hyperkalemia", '''<svg viewBox="0 0 740 280">
 <defs><marker id="nephro-06-01-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="170" height="40" rx="10" class="badsoft"/>
 <text x="95" y="35" text-anchor="middle" class="tb">Hyperkalemia</text>
 <path d="M180 30H218" class="ln" marker-end="url(#nephro-06-01-b)"/>
 <rect x="220" y="10" width="140" height="40" rx="10" class="box"/>
 <text x="290" y="35" text-anchor="middle" class="tb">K load?</text>
 <path d="M290 50V74" class="ln" marker-end="url(#nephro-06-01-b)"/>
 <text x="300" y="66" class="t3">ใช่</text>
 <rect x="220" y="76" width="140" height="56" rx="10" class="sunk"/>
 <text x="232" y="98" class="t2">Acute: IV, intake</text>
 <text x="232" y="120" class="t2">Lysis/shift</text>
 <path d="M360 30H398" class="ln" marker-end="url(#nephro-06-01-b)"/>
 <text x="366" y="22" class="t3">ไม่</text>
 <rect x="400" y="10" width="140" height="40" rx="10" class="box"/>
 <text x="470" y="35" text-anchor="middle" class="tb">Renal failure?</text>
 <path d="M470 50V74" class="ln" marker-end="url(#nephro-06-01-b)"/>
 <rect x="400" y="76" width="140" height="56" rx="10" class="sunk"/>
 <text x="412" y="98" class="t2">AKI</text>
 <text x="412" y="120" class="t2">CKD (GFR &lt; 20)</text>
 <path d="M540 30H578" class="ln" marker-end="url(#nephro-06-01-b)"/>
 <rect x="580" y="10" width="150" height="40" rx="10" class="box"/>
 <text x="655" y="35" text-anchor="middle" class="tb">Drug / hypoaldo</text>
 <path d="M655 50V74" class="ln" marker-end="url(#nephro-06-01-b)"/>
 <rect x="580" y="76" width="150" height="104" rx="10" class="sunk"/>
 <text x="592" y="98" class="t2">ACEI, ARB</text>
 <text x="592" y="118" class="t2">Spironolactone</text>
 <text x="592" y="138" class="t2">Amiloride, TMP/SMX</text>
 <text x="592" y="160" class="t2">Adrenal insuff.</text>
 <rect x="10" y="150" width="350" height="120" rx="10" class="misssoft"/>
 <text x="22" y="174" class="tb">Lysis / shift ออกนอกเซลล์</text>
 <text x="22" y="198" class="t2">Rhabdomyolysis · Tumor lysis</text>
 <text x="22" y="218" class="t2">Hemolysis (เลือดผิดหมู่)</text>
 <text x="22" y="238" class="t2">Digitalis intoxication · Periodic paralysis</text>
 <text x="22" y="258" class="t3">Metabolic acidosis, insulin ต่ำ (เสริม)</text>
 <rect x="400" y="200" width="330" height="70" rx="10" class="box"/>
 <text x="412" y="224" class="tb">อย่าลืม pseudohyperkalemia (เสริม)</text>
 <text x="412" y="246" class="t3">เลือด hemolyzed, รัดแขนนาน, WBC/plt สูงมาก</text>
 <text x="412" y="262" class="t3">→ เจาะซ้ำก่อนถ้า ECG ปกติ</text>
</svg>''', "ถามสามคำถามตามลำดับในสไลด์: มี K เข้ามาหรือออกจากเซลล์มากไหม ไตวายไหม แล้วจึงดูยาและ aldosterone")

S1 = sec("nephro-06-01", "Hyperkalemia",
    "K >5 · ECG peaked T → wide QRS → sine wave · Ca gluconate → insulin+glucose → remove (Kayexalate, furosemide, HD)", minutes=9,
    source=f"{D} หน้า 190–200", nl=["2.2.15", "2.3.4(2)", "B9.4(2)"],
    md='''
### อาการ

- **K > 5 mEq/L**
- Cardiac arrhythmia (ตายได้), **muscle weakness, paralysis** (ascending), paresthesia, ↓DTR
- N/V, diarrhea

### ECG (เรียงตามความรุนแรง)

1. **Tall peaked T wave**
2. Widening & flattening P wave → PR ยาว (เสริม)
3. **Wide QRS complex**, **absent P wave**
4. **Sine wave pattern** → VF/asystole

> ECG ไม่สัมพันธ์กับระดับ K เป๊ะ ๆ — ถ้ามี ECG เปลี่ยนคือ emergency ไม่ว่า K เท่าไร (เสริม)

### การรักษา (สไลด์)

[[fig:nephro-06-01-f1]]

**STEP 1 Heart stabilization** (เมื่อ weakness หรือ ECG change)
- **10% calcium gluconate IV** (10 ml ใน 2–3 นาที (เสริม)) — ทำให้ membrane potential ของกล้ามเนื้อหัวใจคงที่ ไม่ได้ลด K

**STEP 2 Shift K เข้าเซลล์**
- **50% glucose 50 ml + regular insulin 10 U IV**
- **IV NaHCO3** กรณีมี acidosis
- **β2-agonist nebulization** (salbutamol)

**STEP 3 Remove K**
- **Kalimate/Kayexalate** (resin แลก K ในลำไส้)
- **Furosemide** (ถ้าไตยังมีปัสสาวะ)
- **Hemodialysis** (ESRD, anuria, refractory)

> **กรณีไม่ emergency ทำแค่ STEP 3 ก็พอ**

### สาเหตุ

[[fig:nephro-06-01-f2]]

- **Load**: intake, IV
- **Lysis/shift**: rhabdomyolysis, tumor lysis, periodic paralysis (hyperkalemic), **hemolysis** (เช่น transfusion reaction), digitalis intoxication
- **Renal failure**: AKI, CKD (GFR < 20)
- **Drugs**: ACEI, ARB, spironolactone, amiloride (ENaC blocker), TMP/SMX
- **Hypoaldosteronism**: adrenal insufficiency

> ผู้ป่วย ESRD ที่ขาดการฟอกเลือด/ฟอกไม่พอ + ใจสั่น อ่อนแรง → hyperK — ตอบ **Ca gluconate ก่อน** เสมอเมื่อ ECG เปลี่ยน แล้วจึง HD
''',
    figs=[F_HK, F_HKC],
    pearls=[
        "Hyperkalemia + ECG เปลี่ยน → 10% Ca gluconate IV ก่อนเสมอ",
        "Shift: 50% glucose 50 ml + RI 10 U · NaHCO3 ถ้า acidosis · β2-agonist NB",
        "Remove: Kayexalate · furosemide · HD (ESRD/anuria)",
        "ไม่ใช่ emergency → แค่ STEP 3",
        "ECG: peaked T → P แบน → wide QRS → sine wave",
    ],
    items=[
        mcq("NEPHRO-06-01-1",
            "A 58-year-old man with diabetes, hypertension, and dyslipidemia presents with sudden dyspnea and anuria. BP 180/100 mmHg, PR 110/min, RR 28/min, bilateral crackles. ECG shows peaked T waves and widened QRS complexes. What is the most appropriate management at this time?",
            "Intravenous calcium gluconate",
            ["Intravenous amiodarone", "Intravenous fluid loading", "Intravenous furosemide", "Synchronized cardioversion"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Anuria + **peaked T + wide QRS** = hyperkalemia ที่คุกคามชีวิต ขั้นแรกคือ **stabilize หัวใจด้วย calcium gluconate IV** (ออกฤทธิ์ในไม่กี่นาที)
- Amiodarone ไม่แก้สาเหตุ (K) และอาจทำให้ conduction แย่ลง
- IV fluid ทำให้น้ำท่วมปอดแย่ลง (มี crackles และ anuria)
- Furosemide ใช้ลด K/น้ำได้ในขั้นที่ 3 แต่ช้าและผู้ป่วย anuria อาจไม่ตอบสนอง
- Cardioversion ไม่ใช่การรักษา wide QRS จาก hyperK''',
            pearl="Wide QRS จาก hyperK → Ca gluconate ก่อน", topic="Hyperkalemia emergency",
            ref=[f"{D} หน้า 191, 193–194"], nl=["2.2.15"]),
        mcq("NEPHRO-06-01-2",
            "A 60-year-old man with ESRD on hemodialysis twice weekly presents with palpitations and puffy eyelids. BP 160/110 mmHg, PR 80/min. K 6.3 mmol/L, BUN 80 mg/dL, Cr 7 mg/dL. ECG shows tall peaked T waves. What is the most appropriate initial management?",
            "Calcium gluconate",
            ["Sodium bicarbonate", "Kayexalate", "Intravenous insulin with glucose", "Hemodialysis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Hyperkalemia ที่มี **อาการ (ใจสั่น) และ ECG เปลี่ยน** → **initial** management คือ **calcium gluconate** เพื่อป้องกันหัวใจ ก่อนทำขั้นต่อไป
- Insulin + glucose (และ NaHCO3 ถ้ามี acidosis) เป็นขั้นที่ 2 ทำตามหลัง Ca
- Kayexalate ออกฤทธิ์ช้าหลายชั่วโมง
- Hemodialysis เป็นการรักษาเด็ดขาดใน ESRD แต่ต้องใช้เวลาเตรียม จึงไม่ใช่ขั้นแรก
- NaHCO3 ได้ผลน้อยเมื่อไม่มี acidosis และไม่ใช่ขั้นแรก''',
            pearl="ESRD + K สูง + ECG เปลี่ยน → Ca gluconate ก่อน แล้วค่อย HD", topic="Hyperkalemia in ESRD",
            ref=[f"{D} หน้า 191, 195–196"], nl=["2.2.15"]),
        mcq("NEPHRO-06-01-3",
            "A 50-year-old man develops fever and dark urine shortly after a blood transfusion. BP 90/60 mmHg, SpO2 99%. ECG shows peaked T waves and a widened QRS complex. What is the most appropriate immediate management?",
            "Intravenous calcium gluconate",
            ["Normal saline loading only", "Intravenous amiodarone", "Intravenous magnesium sulfate", "Intravenous epinephrine"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Acute hemolytic transfusion reaction → เม็ดเลือดแดงแตก **ปล่อย K ออกมา** (lysis) + ปัสสาวะสีเข้ม (hemoglobinuria) ECG แบบ hyperK → ต้องให้ **calcium gluconate** ทันที (แล้วหยุดเลือด ให้สารน้ำรักษา AKI ต่อ)
- NSS จำเป็นสำหรับความดันต่ำและป้องกัน pigment nephropathy แต่ไม่ป้องกันหัวใจจาก K ทันที
- Amiodarone ไม่ใช่การรักษา hyperK
- Magnesium sulfate ใช้กับ torsades de pointes
- Epinephrine ใช้กับ anaphylaxis ซึ่งไม่ทำให้ ECG แบบ hyperK''',
            pearl="Hemolysis → K สูง → Ca gluconate", topic="Hemolysis hyperkalemia",
            ref=[f"{D} หน้า 192, 199–200"], nl=["2.2.15"]),
        mcq("NEPHRO-06-01-4",
            "A 66-year-old man with CKD stage 3 on lisinopril and spironolactone has K 6.0 mEq/L on routine testing. He has no symptoms. ECG is normal. What is the most appropriate management?",
            "Stop spironolactone and give a potassium-binding resin with a low-potassium diet",
            ["Intravenous calcium gluconate", "Insulin 10 U with 50% glucose 50 mL IV", "Urgent hemodialysis", "Intravenous sodium bicarbonate"],
            explain='''K 6.0 **ไม่มีอาการ ECG ปกติ** = ไม่ใช่ emergency → สไลด์: **ทำแค่ STEP 3 (remove)** ร่วมกับหาสาเหตุ (spironolactone + ACEI + CKD) และ low K diet
- Ca gluconate ใช้เมื่อมี ECG change/อ่อนแรง
- Insulin + glucose เป็นการ shift ชั่วคราวในภาวะฉุกเฉิน
- HD ไม่มีข้อบ่งชี้
- NaHCO3 ใช้เมื่อมี acidosis''',
            pearl="HyperK ไม่ emergency → หยุดยาที่เป็นเหตุ + remove K", topic="Non-emergency hyperkalemia",
            ref=[f"{D} หน้า 191–192"], nl=["2.3.4(2)", "B9.4(2)"]),
        mcq("NEPHRO-06-01-5",
            "A 70-year-old man with ESRD who has refused hemodialysis presents with fatigue and drowsiness. K 7.8 mEq/L. ECG shows absent P waves, a wide QRS complex, and tall peaked T waves. What is the most appropriate initial management?",
            "10% calcium gluconate IV",
            ["Regular insulin with 50% glucose IV", "7.5% sodium bicarbonate IV", "Intravenous furosemide", "Oral sodium polystyrene sulfonate"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (เพิ่มค่า K และ ECG ที่สไลด์แสดงเป็นภาพ)",
            explain='''ECG มี **P หาย QRS กว้าง** = hyperK ใกล้ sine wave/หัวใจหยุดเต้น → initial คือ **10% calcium gluconate IV** เพื่อ stabilize membrane ทันที (ตามด้วย insulin + glucose และวางแผน dialysis)
- Insulin + glucose เป็นขั้นที่ 2 (shift) ทำหลัง Ca
- NaHCO3 ได้ผลน้อยถ้าไม่มี acidosis และไม่ใช่ขั้นแรก
- Furosemide แทบไม่ได้ผลในผู้ป่วย ESRD ที่ไม่มีปัสสาวะ
- Resin ออกฤทธิ์ช้าหลายชั่วโมง''',
            pearl="QRS กว้างจาก hyperK → Ca gluconate ก่อนทุกอย่าง", topic="Hyperkalemia emergency",
            ref=[f"{D} หน้า 197–198"], nl=["2.2.15"]),
    ])

# ---------------------------------------------------------------- 06-02 Hypokalemia
F_HYPOK = fig("nephro-06-02-f1", "Approach to hypokalemia (ตามสไลด์)", '''<svg viewBox="0 0 740 420">
 <defs><marker id="nephro-06-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="160" height="40" rx="10" class="c1soft"/>
 <text x="90" y="35" text-anchor="middle" class="tb">Hypokalemia</text>
 <path d="M170 30H218" class="ln" marker-end="url(#nephro-06-02-a)"/>
 <rect x="220" y="10" width="170" height="40" rx="10" class="box"/>
 <text x="305" y="35" text-anchor="middle" class="tb">Acute loss/shift?</text>
 <path d="M305 50V72" class="ln" marker-end="url(#nephro-06-02-a)"/>
 <text x="315" y="66" class="t3">ใช่</text>
 <rect x="220" y="74" width="170" height="92" rx="10" class="sunk"/>
 <text x="232" y="94" class="t2">Loss: diarrhea, vomit,</text>
 <text x="232" y="112" class="t2">diuretics</text>
 <text x="232" y="132" class="t2">Shift: periodic paralysis,</text>
 <text x="232" y="150" class="t3">thyroid, insulin, β2, refeeding</text>
 <path d="M390 30H438" class="ln" marker-end="url(#nephro-06-02-a)"/>
 <text x="398" y="22" class="t3">ไม่</text>
 <rect x="440" y="10" width="290" height="40" rx="10" class="box"/>
 <text x="585" y="35" text-anchor="middle" class="tb">Urine K &gt; 15 (renal loss)?</text>
 <path d="M500 50V72" class="ln" marker-end="url(#nephro-06-02-a)"/>
 <text x="510" y="66" class="t3">ไม่</text>
 <rect x="420" y="74" width="190" height="56" rx="10" class="oksoft"/>
 <text x="515" y="96" text-anchor="middle" class="tb">Non-renal</text>
 <text x="515" y="116" text-anchor="middle" class="t3">low intake, diarrhea เรื้อรัง</text>
 <path d="M670 50V186" class="ln" marker-end="url(#nephro-06-02-a)"/>
 <text x="680" y="120" class="t3">ใช่</text>
 <rect x="230" y="188" width="500" height="40" rx="10" class="c1"/>
 <text x="480" y="213" text-anchor="middle" class="tw">Renal loss → ดู BP และ acid–base</text>
 <path d="M320 228L130 262" class="ln" marker-end="url(#nephro-06-02-a)"/>
 <path d="M440 228V262" class="ln" marker-end="url(#nephro-06-02-a)"/>
 <path d="M560 228L600 262" class="ln" marker-end="url(#nephro-06-02-a)"/>
 <path d="M690 228L715 262" class="ln" marker-end="url(#nephro-06-02-a)"/>
 <rect x="10" y="264" width="250" height="146" rx="10" class="badsoft"/>
 <text x="22" y="286" class="tb">Met alkalosis + HT</text>
 <text x="22" y="306" class="t3">ดู PRA / PAC</text>
 <text x="22" y="330" class="t2">↑PRA ↑PAC: RAS, renin tumor</text>
 <text x="22" y="352" class="t2">↓PRA ↑PAC: hyperaldo</text>
 <text x="22" y="374" class="t2">↓PRA ↓PAC: Cushing</text>
 <text x="22" y="394" class="t3">(และ licorice (เสริม))</text>
 <rect x="275" y="264" width="200" height="146" rx="10" class="misssoft"/>
 <text x="287" y="286" class="tb">Met alkalosis</text>
 <text x="287" y="306" class="t3">BP ปกติ</text>
 <text x="287" y="330" class="t2">Diuretics</text>
 <text x="287" y="350" class="t2">Vomiting</text>
 <text x="287" y="370" class="t2">Bartter</text>
 <text x="287" y="390" class="t2">Gitelman</text>
 <rect x="490" y="264" width="150" height="146" rx="10" class="c2soft"/>
 <text x="502" y="286" class="tb">Met acidosis</text>
 <text x="502" y="310" class="t2">RTA (1, 2)</text>
 <text x="502" y="330" class="t2">Amphotericin B</text>
 <text x="502" y="350" class="t3">DKA ระหว่างรักษา</text>
 <rect x="650" y="264" width="80" height="146" rx="10" class="sunk"/>
 <text x="690" y="300" text-anchor="middle" class="tb">↓Mg</text>
 <text x="690" y="326" text-anchor="middle" class="t3">แก้ Mg</text>
 <text x="690" y="344" text-anchor="middle" class="t3">ก่อน K</text>
 <text x="690" y="362" text-anchor="middle" class="t3">จะขึ้น</text>
</svg>''', "ตัด shift และการเสียแบบเฉียบพลันก่อน แล้วใช้ urine K แยกเสียทางไต จากนั้นใช้ความดันและ acid–base แบ่งสาเหตุทางไต")


F_NEPH = fig("nephro-06-02-f2", "ตำแหน่งตาม nephron: ยาขับปัสสาวะ · โรค · RTA", """<svg viewBox="0 0 740 330">
 <defs><marker id="nephro-06-02-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="95" y="10" width="148" height="48" rx="10" class="c1"/>
 <text x="169" y="31" text-anchor="middle" class="tw">PCT</text>
 <text x="169" y="49" text-anchor="middle" class="tw">ดูด Na ~65%, HCO3</text>
 <rect x="258" y="10" width="148" height="48" rx="10" class="ac"/>
 <text x="332" y="31" text-anchor="middle" class="tw">Thick ascending</text>
 <text x="332" y="49" text-anchor="middle" class="tw">NKCC2 · Na ~25%</text>
 <rect x="421" y="10" width="148" height="48" rx="10" class="c2"/>
 <text x="495" y="31" text-anchor="middle" class="tw">DCT</text>
 <text x="495" y="49" text-anchor="middle" class="tw">NCC · Na ~5%</text>
 <rect x="584" y="10" width="148" height="48" rx="10" class="miss"/>
 <text x="658" y="31" text-anchor="middle" class="tw">Collecting duct</text>
 <text x="658" y="49" text-anchor="middle" class="tw">ENaC · ADH</text>
 <path d="M243 34H256" class="ln" marker-end="url(#nephro-06-02-b)"/>
 <path d="M406 34H419" class="ln" marker-end="url(#nephro-06-02-b)"/>
 <path d="M569 34H582" class="ln" marker-end="url(#nephro-06-02-b)"/>
 <text x="6" y="94" class="tb">ยา</text>
 <text x="6" y="164" class="tb">ผลข้างเคียง</text>
 <text x="6" y="234" class="tb">โรคที่</text>
 <text x="6" y="250" class="tb">ตำแหน่งนี้</text>
 <text x="6" y="300" class="tb">RTA</text>
 <rect x="95" y="68" width="148" height="56" rx="8" class="c1soft"/>
 <text x="107" y="90" class="t2">Acetazolamide</text>
 <text x="107" y="110" class="t2">SGLT2i</text>
 <rect x="258" y="68" width="148" height="56" rx="8" class="acsoft"/>
 <text x="270" y="90" class="t2">Furosemide</text>
 <text x="270" y="110" class="t3">(loop diuretic)</text>
 <rect x="421" y="68" width="148" height="56" rx="8" class="c2soft"/>
 <text x="433" y="90" class="t2">HCTZ</text>
 <text x="433" y="110" class="t3">(thiazide)</text>
 <rect x="584" y="68" width="148" height="56" rx="8" class="misssoft"/>
 <text x="596" y="90" class="t2">Spironolactone</text>
 <text x="596" y="110" class="t2">Amiloride</text>
 <rect x="95" y="134" width="148" height="62" rx="8" class="sunk"/>
 <text x="107" y="156" class="t2">เสีย HCO3</text>
 <text x="107" y="176" class="t3">→ normal-AG acidosis</text>
 <rect x="258" y="134" width="148" height="62" rx="8" class="sunk"/>
 <text x="270" y="156" class="t2">↓K, met alkalosis</text>
 <text x="270" y="176" class="t3">Ca ในปัสสาวะ ↑</text>
 <rect x="421" y="134" width="148" height="62" rx="8" class="sunk"/>
 <text x="433" y="156" class="t2">↓K, ↓Na บ่อย</text>
 <text x="433" y="176" class="t3">Ca ในปัสสาวะ ↓</text>
 <rect x="584" y="134" width="148" height="62" rx="8" class="sunk"/>
 <text x="596" y="156" class="t2">↑K (K-sparing)</text>
 <text x="596" y="176" class="t3">gynecomastia (spiro)</text>
 <rect x="95" y="206" width="148" height="56" rx="8" class="box"/>
 <text x="107" y="230" class="t2">Fanconi</text>
 <rect x="258" y="206" width="148" height="56" rx="8" class="box"/>
 <text x="270" y="230" class="t2">Bartter</text>
 <text x="270" y="250" class="t3">เหมือนกิน loop</text>
 <rect x="421" y="206" width="148" height="56" rx="8" class="box"/>
 <text x="433" y="230" class="t2">Gitelman</text>
 <text x="433" y="250" class="t3">เหมือนกิน thiazide, ↓Mg</text>
 <rect x="584" y="206" width="148" height="56" rx="8" class="box"/>
 <text x="596" y="230" class="t2">Nephrogenic DI</text>
 <text x="596" y="250" class="t3">Liddle (↑ENaC)</text>
 <rect x="95" y="272" width="148" height="48" rx="8" class="c1soft"/>
 <text x="107" y="301" class="t2">Type 2 (proximal)</text>
 <rect x="258" y="272" width="311" height="48" rx="8" class="sunk"/>
 <text x="413" y="301" text-anchor="middle" class="t3">—</text>
 <rect x="584" y="272" width="148" height="48" rx="8" class="misssoft"/>
 <text x="596" y="292" class="t2">Type 1 (distal)</text>
 <text x="596" y="310" class="t2">Type 4 (↓aldo, ↑K)</text>
</svg>""", "อ่านทีละคอลัมน์ตามทางไหลของปัสสาวะ: แต่ละส่วนของ nephron มียาที่ออกฤทธิ์ ผลต่อ K/Ca โรคที่เกิดตรงส่วนนั้น (Bartter/Gitelman เหมือนกินยา) และชนิด RTA ที่เกิดตรงนั้น (เสริม)")

S2 = sec("nephro-06-02", "Hypokalemia",
    "K <3.5 · proximal weakness, U wave · emergency = KCl IV + monitor · ไม่ emergency ให้ oral KCl · หาสาเหตุด้วย UK, BP, acid–base", minutes=8,
    source=f"{D} หน้า 201–207", nl=["2.2.15", "2.3.6(7)", "2.3.4(2)"],
    md='''
### อาการ

- **K < 3.5 mEq/L**
- **Proximal muscle weakness**, rhabdomyolysis, ↓DTR, (paralysis ถ้า K < 2.5 (เสริม))
- Cardiac arrhythmia (โดยเฉพาะเมื่อได้ digoxin (เสริม))
- Constipation/ileus, fatigue
- Nephrogenic DI (polyuria) ได้ (เสริม)

### ECG

- **T wave inversion/flattening, ST depression**
- **Prominent U wave**

### การรักษา (สไลด์)

| Emergency (weakness หรือ ECG change) | Non-emergency |
|---|---|
| **KCl IV** (peripheral ≤ 10–20 mEq/hr; ทาง **central line** ถ้าต้องให้เร็ว/เข้มข้น (เสริม)) | **Oral KCl ดีกว่า IV** |
| **Admit ICU + monitor ECG** | |

- ห้ามผสม KCl ใน dextrose เพราะ insulin ที่หลั่งตามจะดัน K เข้าเซลล์ (เสริม)
- **Hypomagnesemia ต้องแก้ด้วย** ไม่เช่นนั้น K ไม่ขึ้น (Mg ต่ำทำให้ ROMK รั่ว K ออก (เสริม))

### หาสาเหตุ

[[fig:nephro-06-02-f1]]

- **Shift** (K รวมในร่างกายไม่ได้ลด): hypokalemic periodic paralysis, hyperthyroidism (thyrotoxic periodic paralysis), insulin, β2-agonist, refeeding
- **Loss เฉียบพลัน**: diarrhea, vomiting, diuretics
- **Renal loss (urine K > 15 mEq/day)** แบ่งตาม BP/acid–base
  - **Met alkalosis + HT** → ดู PRA/PAC: ↑↑ RAS (renovascular); ↓PRA ↑PAC = primary hyperaldosteronism; ↓↓ = Cushing (หรือ licorice (เสริม))
  - **Met alkalosis, BP ปกติ**: diuretics, vomiting, Bartter, Gitelman
  - **Met acidosis**: RTA, amphotericin B
  - **HypoMg**

### ตำแหน่งยาขับปัสสาวะและโรคที่เลียนแบบ (เสริม)

[[fig:nephro-06-02-f2]]

- Loop และ thiazide ส่ง Na ไปถึง collecting duct มากขึ้น + aldosterone สูงจาก volume ลด → ขับ K และ H ออก → **hypoK + met alkalosis**
- **Bartter = เหมือนกิน loop** (Ca ในปัสสาวะสูง) · **Gitelman = เหมือนกิน thiazide** (Ca ในปัสสาวะต่ำ, Mg ต่ำ) — แยกจากการแอบกินยาด้วย urine diuretic screen

> ผู้ป่วยกิน **HCTZ** ขนาดสูงนาน ๆ แล้วอ่อนแรง → hypoK · ผู้ป่วย HF ได้ **furosemide** แล้ว K ต่ำ → จาก diuretic

> ภาคอีสาน + อ่อนแรง + **hypoK + metabolic acidosis (normal AG)** + Cr ขึ้น → **distal RTA** (ดูหมวด metabolic acidosis)
''',
    figs=[F_HYPOK, F_NEPH],
    pearls=[
        "HypoK: proximal weakness + ECG ST↓ T แบน/กลับหัว + U wave",
        "Emergency → KCl IV + ICU monitor ECG · ไม่ emergency → oral KCl",
        "แก้ Mg ด้วย ไม่งั้น K ไม่ขึ้น",
        "Renal loss + HT + alkalosis → PRA/PAC · BP ปกติ + alkalosis → diuretic/vomiting/Bartter/Gitelman · acidosis → RTA",
        "Thiazide และ loop diuretic = สาเหตุ hypoK ที่พบบ่อยที่สุดในข้อสอบ",
    ],
    items=[
        mcq("NEPHRO-06-02-1",
            "A 43-year-old woman complains of easy fatigue and weakness of the arms and legs. She previously had leg edema and has been taking hydrochlorothiazide 50 mg/day for a long time. Which electrolyte abnormality most likely explains her symptoms?",
            "Hypokalemia",
            ["Hyponatremia", "Hypomagnesemia", "Hypocalcemia", "Hypercalcemia"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Thiazide เพิ่ม Na มาถึง distal nephron → แลกเปลี่ยนกับ K มากขึ้น → **hypokalemia** ซึ่งทำให้ **กล้ามเนื้อแขนขาอ่อนแรง** อ่อนเพลีย (ขนาด 50 mg/วัน ถือว่าสูง)
- Hyponatremia จาก thiazide พบได้ แต่มักทำให้ปวดหัว คลื่นไส้ สับสน มากกว่าอ่อนแรงของกล้ามเนื้อแขนขา
- Hypomagnesemia เกิดร่วมได้ แต่เด่นที่ตะคริว tetany arrhythmia
- Thiazide ลดการขับ Ca ทำให้ Ca **สูง** ไม่ใช่ต่ำ และ hypocalcemia ทำให้เกร็ง/ชาไม่ใช่อ่อนแรง
- Hypercalcemia จาก thiazide มักเล็กน้อยและไม่ใช่สาเหตุหลักของกล้ามเนื้ออ่อนแรง''',
            pearl="HCTZ ขนาดสูง + อ่อนแรง → hypoK", topic="Diuretic hypokalemia",
            ref=[f"{D} หน้า 201, 204–205"], nl=["2.3.4(2)"]),
        mcq("NEPHRO-06-02-2",
            "A patient admitted for myocardial infarction develops heart failure and is treated for 2 days. Follow-up labs: Na 140, K 3.0, HCO3 30 mmol/L. What is the most likely cause of the abnormal laboratory values?",
            "Intravenous furosemide",
            ["Aspirin", "Clopidogrel", "Enoxaparin", "Atorvastatin"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ปรับ HCO3 ให้เข้ากับ diuretic)",
            explain='''ผู้ป่วย HF ได้ **loop diuretic (furosemide)** → เสีย K ทางไต และเกิด contraction alkalosis → **hypoK + HCO3 สูง** (สไลด์เฉลย diuretics)
- Aspirin ขนาดต่ำไม่ทำ hypoK
- Clopidogrel และ atorvastatin ไม่มีผลต่อ K
- Enoxaparin/heparin ทำให้ K **สูง** (ยับยั้ง aldosterone) ไม่ใช่ต่ำ
หมายเหตุ: ในสไลด์ให้ HCO3 23 ซึ่งยังปกติ ข้อนี้ปรับเป็น 30 ให้เห็นภาพ diuretic ชัดขึ้น''',
            pearl="HF + furosemide → hypoK + met alkalosis", topic="Loop diuretic hypokalemia",
            ref=[f"{D} หน้า 203, 206–207"], nl=["2.3.4(2)"]),
        mcq("NEPHRO-06-02-3",
            "A 28-year-old man wakes up unable to move his legs after a large carbohydrate meal and alcohol the night before. He has tremor, HR 118/min, and a fine goiter. K 2.1 mEq/L, normal acid–base status. ECG shows prominent U waves. What is the most likely underlying cause?",
            "Thyrotoxic periodic paralysis",
            ["Distal renal tubular acidosis", "Gitelman syndrome", "Primary hyperaldosteronism", "Guillain–Barré syndrome"],
            explain='''อ่อนแรงทันทีหลังกินคาร์โบไฮเดรต/แอลกอฮอล์ + **hyperthyroid signs** + K ต่ำมากโดย acid–base ปกติ = **thyrotoxic periodic paralysis** — เป็น **shift** (thyroid hormone และ insulin กระตุ้น Na–K ATPase) ไม่ใช่ K รวมในร่างกายลด จึงให้ KCl ปริมาณน้อยระวัง rebound hyperK และให้ propranolol (เสริม)
- Distal RTA ทำ hypoK ร่วมกับ normal-AG metabolic acidosis
- Gitelman ทำ hypoK + met alkalosis + hypoMg เรื้อรัง
- Hyperaldosteronism มีความดันสูง + alkalosis
- GBS อ่อนแรงแบบ ascending ไม่ได้ทำ K ต่ำ''',
            pearl="Hyperthyroid + อัมพาตหลังกินแป้ง + hypoK = thyrotoxic periodic paralysis (shift)", topic="Hypokalemic periodic paralysis",
            ref=[f"{D} หน้า 203"], nl=["2.3.6(7)"]),
        mcq("NEPHRO-06-02-4",
            "A 60-year-old woman with diarrhea for 1 week has generalized weakness. K 2.3 mEq/L. ECG shows ST depression, flattened T waves, and prominent U waves with frequent PVCs. Mg 1.2 mg/dL (low). What is the most appropriate management?",
            "Intravenous KCl with ECG monitoring and magnesium replacement",
            ["Oral KCl alone as outpatient", "Spironolactone", "Intravenous KCl in 5% dextrose bolus", "Intravenous insulin with glucose"],
            explain='''HypoK **มี ECG change และอ่อนแรง = emergency** → **KCl IV + admit monitor ECG** (สไลด์) และต้อง **แก้ Mg** ด้วย ไม่เช่นนั้น K จะไม่ขึ้น
- Oral KCl เหมาะกับรายไม่ฉุกเฉิน
- Spironolactone ใช้ป้องกันการเสีย K ทางไตระยะยาว ไม่ใช่ภาวะฉุกเฉินจาก GI loss
- ผสม KCl ใน dextrose ทำให้ insulin หลั่ง ดัน K เข้าเซลล์ และห้าม bolus KCl เด็ดขาด
- Insulin + glucose ทำให้ K ต่ำลงอีก''',
            pearl="HypoK + ECG change → KCl IV + monitor + แก้ Mg", topic="Hypokalemia treatment",
            ref=[f"{D} หน้า 202–203"], nl=["2.2.15"]),
    ])

LECTURE = lecture("06", "Potassium disorders", "Hyperkalemia · hypokalemia",
    objectives=[
        "อ่าน ECG ของ hyperK/hypoK และบอกว่าเมื่อไรเป็น emergency ได้",
        "สั่งการรักษา hyperkalemia ตามลำดับ stabilize → shift → remove ได้",
        "หาสาเหตุ hyperK (load, lysis, renal, drug, hypoaldo) และ hypoK (shift, loss, renal) ได้",
        "แก้ hypokalemia อย่างปลอดภัยรวมถึงแก้ Mg ได้",
    ],
    sections=[S1, S2])
