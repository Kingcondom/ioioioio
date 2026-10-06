from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Nephro"

# ---------------------------------------------------------------- 07-01 ABG basics
S1 = sec("nephro-07-01", "ABG: ABG หรือ VBG · oxygenation · ventilation",
    "ค่าปกติ · SpO2 95/90/88 ≈ PaO2 80/60/55 · hypoxemia mild/mod/severe · A-a gradient = 2.5 + age/4 · PaCO2 บอก ventilation", minutes=6,
    source=f"{D} หน้า 208–211", nl=["3.3.17", "B6.3(2)", "2.3.4(2)"],
    md='''
### อ่าน ABG 4 ขั้น (สไลด์)

1. ABG หรือ VBG
2. Oxygenation
3. Ventilation
4. Acid–base

| ค่าปกติ | |
|---|---|
| pH | 7.4 (7.35–7.45) |
| PaO2 | 80–100 mmHg |
| PaCO2 | 40 (35–45) mmHg |
| HCO3 | 24 (22–26) mmol/L — ควรดูจากผลเลือด (serum total CO2) |

### STEP 1: ABG หรือ VBG

ถ้า **calculated SaO2 ในผล ABG ใกล้เคียงกับ SpO2** จาก pulse oximeter → เป็นเลือดแดงจริง

| SpO2 | ≈ PaO2 |
|---|---|
| 95% | 80 mmHg |
| 90% | 60 mmHg |
| 88% | 55 mmHg |

> SpO2 98% แต่ "ABG" ได้ PO2 35 sat 65% → เลือดดำ (VBG) ต้องเจาะซ้ำ — แต่ VBG ยังใช้ดู pH และ HCO3 ได้ใกล้เคียง (เสริม)

### STEP 2: Oxygenation

**Room air** (ดู PaO2 และ A-a gradient)
- Normal: PaO2 80–100
- **Mild hypoxemia: 60–80**
- **Moderate: 40–60**
- **Severe: < 40**

**A-a gradient** = PAO2 − PaO2 (เสริม: PAO2 ที่ room air ระดับน้ำทะเล ≈ 150 − PaCO2/0.8)
- ปกติ = **2.5 + (อายุ/4)**
- A-a ปกติ + hypoxemia = **hypoventilation** (ยากดการหายใจ, neuromuscular) หรือ low FiO2 (ที่สูง)
- A-a กว้าง = V/Q mismatch, shunt, diffusion defect (pneumonia, PE, ARDS) (เสริม)

**ได้ O2 อยู่** → ใช้ **P/F ratio (PaO2/FiO2)** · ปกติ ~500 (100/0.21)

### STEP 3: Ventilation

- Normal PaCO2 40 (35–45)
- **Hyperventilation: PaCO2 < 35**
- **Hypoventilation: PaCO2 > 45**
''',
    pearls=[
        "SpO2 95 ≈ PaO2 80 · SpO2 90 ≈ PaO2 60 · SpO2 88 ≈ PaO2 55",
        "Hypoxemia: mild 60–80 · moderate 40–60 · severe <40",
        "A-a gradient ปกติ = 2.5 + อายุ/4 · ปกติ + hypoxemia = hypoventilation",
        "ได้ O2 → ใช้ P/F ratio (ปกติ ~500)",
    ],
    items=[
        mcq("NEPHRO-07-01-1",
            "A 25-year-old woman is found drowsy after ingesting a large amount of a benzodiazepine. RR 6/min. ABG on room air at sea level: pH 7.21, PaCO2 70 mmHg, PaO2 62 mmHg, HCO3 27 mEq/L. What is the main mechanism of her hypoxemia?",
            "Alveolar hypoventilation",
            ["Ventilation–perfusion mismatch", "Right-to-left shunt", "Diffusion impairment", "Low inspired oxygen fraction"],
            explain='''คำนวณ A-a gradient: PAO2 ≈ 150 − (70 ÷ 0.8) = 150 − 87.5 = 62.5 → A-a = 62.5 − 62 ≈ 0.5 mmHg (ปกติสำหรับอายุ 25 คือ ≤ 2.5 + 25/4 ≈ 8.8) → A-a **ปกติ** แปลว่าปอดแลกเปลี่ยนก๊าซได้ดี hypoxemia เกิดจาก **hypoventilation** (ยากดการหายใจ)
- V/Q mismatch, shunt และ diffusion impairment ล้วนทำให้ A-a gradient **กว้าง**
- Low FiO2 เกิดที่ที่สูง แต่ผู้ป่วยอยู่ระดับน้ำทะเล room air
(ตรวจสอบ: pH ตาม Henderson–Hasselbalch = 6.1 + log(27 ÷ 2.1) ≈ 7.21)''',
            pearl="Hypoxemia + A-a ปกติ = hypoventilation", topic="A-a gradient",
            ref=[f"{D} หน้า 210–211"], nl=["3.3.17", "B6.3(2)"]),
        mcq("NEPHRO-07-01-2",
            "A 50-year-old man in the ward is comfortable with RR 16/min and SpO2 97% on room air. A blood gas labeled as arterial shows pH 7.36, PO2 36 mmHg, PCO2 47 mmHg, HCO3 26 mEq/L, calculated O2 saturation 68%. What is the most appropriate interpretation?",
            "The sample is most likely venous; repeat an arterial sample if oxygenation must be assessed",
            ["He has severe hypoxemia and needs intubation", "He has carbon monoxide poisoning", "He has acute respiratory acidosis requiring BiPAP", "The pulse oximeter is falsely high because of anemia"],
            explain='''สไลด์: ถ้า **calculated SaO2 ในผลใกล้กับ SpO2** จึงเป็น ABG — รายนี้ SaO2 ในผล 68% แต่ SpO2 97% และผู้ป่วยสบายดี → ตัวอย่างน่าจะเป็น **เลือดดำ (VBG)** pH/PCO2/HCO3 ก็เข้ากับเลือดดำปกติ
- Severe hypoxemia จริงจะเห็นผู้ป่วยหอบและ SpO2 ต่ำ
- CO poisoning ทำให้ SpO2 สูงลวงแต่ **PaO2 ปกติ** ไม่ใช่ PO2 36
- PCO2 47 และ pH 7.36 เป็นค่าปกติของเลือดดำ ไม่ใช่ acute respiratory acidosis
- Anemia ไม่ทำให้ SpO2 สูงลวง''',
            pearl="SaO2 ในผล ≠ SpO2 → น่าจะเป็น VBG", topic="ABG vs VBG",
            ref=[f"{D} หน้า 209"], nl=["3.3.17"]),
        mcq_ordered("NEPHRO-07-01-3",
            "A 60-year-old man with pneumonia is receiving oxygen via a Venturi mask at FiO2 0.4. His PaO2 is 120 mmHg. What is his PaO2/FiO2 (P/F) ratio?",
            ["120", "200", "300", "400", "480"], 2,
            explain='''P/F ratio = PaO2 ÷ FiO2 = 120 ÷ 0.4 = **300** (ปกติ ~500 = 100 ÷ 0.21)
- 120 คือ PaO2 ที่ยังไม่ได้หารด้วย FiO2
- 200, 400 และ 480 เกิดจากหารผิด (เช่นใช้ FiO2 0.6, 0.3 หรือ 0.25)
P/F ใช้แทน PaO2 ตรง ๆ เมื่อผู้ป่วยได้ออกซิเจน เพราะ PaO2 ขึ้นกับ FiO2 ที่ได้รับ''',
            pearl="ได้ O2 → ใช้ P/F ratio = PaO2 ÷ FiO2", topic="P/F ratio",
            ref=[f"{D} หน้า 210"], nl=["3.3.17"]),
    ])

# ---------------------------------------------------------------- 07-02 Acid-base steps & compensation
F_STEPS = fig("nephro-07-02-f1", "Acid–base 5 ขั้น (ตามสไลด์)", '''<svg viewBox="0 0 740 400">
 <defs><marker id="nephro-07-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="160" height="56" rx="10" class="ac"/>
 <text x="90" y="34" text-anchor="middle" class="tw">STEP 1 · pH</text>
 <text x="90" y="54" text-anchor="middle" class="tw">&lt; 7.35 / &gt; 7.45</text>
 <path d="M170 38H198" class="ln" marker-end="url(#nephro-07-02-a)"/>
 <rect x="200" y="10" width="250" height="56" rx="10" class="ac"/>
 <text x="325" y="34" text-anchor="middle" class="tw">STEP 2 · PaCO2 เทียบ pH</text>
 <text x="325" y="54" text-anchor="middle" class="tw">ทางเดียวกัน = metabolic</text>
 <path d="M450 38H478" class="ln" marker-end="url(#nephro-07-02-a)"/>
 <rect x="480" y="10" width="250" height="56" rx="10" class="ac"/>
 <text x="605" y="34" text-anchor="middle" class="tw">STEP 3 · Compensation</text>
 <text x="605" y="54" text-anchor="middle" class="tw">คาดว่าเท่าไร vs จริง</text>
 <rect x="10" y="80" width="355" height="150" rx="10" class="c1soft"/>
 <text x="22" y="104" class="tb">Metabolic primary → predicted PaCO2</text>
 <text x="22" y="130" class="t2">Acidosis: 1.5 × HCO3 + 8 ± 2 (Winter)</text>
 <text x="22" y="154" class="t2">Alkalosis: ΔCO2 = 0.7 × ΔHCO3 ± 2</text>
 <text x="22" y="182" class="t3">Trick: เลขหลังจุดของ pH ≈ PaCO2</text>
 <text x="22" y="200" class="t3">→ น่าจะ compensate (ใช้ได้เฉพาะ metabolic)</text>
 <rect x="375" y="80" width="355" height="150" rx="10" class="c2soft"/>
 <text x="387" y="104" class="tb">Respiratory primary → predicted HCO3</text>
 <text x="387" y="128" class="t2">ทุก PaCO2 เปลี่ยน 10 mmHg HCO3 เปลี่ยน</text>
 <text x="387" y="152" class="t2">Acute acidosis 1 · Acute alkalosis 2</text>
 <text x="387" y="176" class="t2">Chronic acidosis 4 · Chronic alkalosis 5</text>
 <text x="387" y="204" class="t3">จำ "กรด 1–4 · เบส 2–5"</text>
 <rect x="10" y="240" width="720" height="70" rx="10" class="misssoft"/>
 <text x="370" y="261" text-anchor="middle" class="tb">ค่าจริงไม่ตรงที่คาด = มีความผิดปกติที่สองซ้อน</text>
 <text x="370" y="281" text-anchor="middle" class="t2">PaCO2 สูงกว่าคาด = + resp acidosis · ต่ำกว่าคาด = + resp alkalosis</text>
 <text x="370" y="300" text-anchor="middle" class="t2">HCO3 สูงกว่าคาด = + met alkalosis · ต่ำกว่าคาด = + met acidosis</text>
 <path d="M370 310V322" class="ln" marker-end="url(#nephro-07-02-a)"/>
 <rect x="10" y="324" width="355" height="66" rx="10" class="ac"/>
 <text x="187" y="350" text-anchor="middle" class="tw">STEP 4 · ถ้า met acidosis → AG</text>
 <text x="187" y="372" text-anchor="middle" class="tw">ปกติ → ดู albumin (STEP 4.5)</text>
 <rect x="375" y="324" width="355" height="66" rx="10" class="ac"/>
 <text x="552" y="350" text-anchor="middle" class="tw">STEP 5 · ถ้า AG กว้าง</text>
 <text x="552" y="372" text-anchor="middle" class="tw">→ delta ratio</text>
</svg>''', "ทำตามลำดับซ้ายไปขวาและบนลงล่าง ขั้นที่ 3 คือหัวใจ: คำนวณค่าที่คาดไว้แล้วเทียบกับค่าจริงเพื่อหาความผิดปกติซ้อน")

S2 = sec("nephro-07-02", "Acid–base STEP 1–3: primary disorder & compensation",
    "pH → ทิศ PaCO2 → Winter's (1.5×HCO3+8±2) / ΔCO2 = 0.7ΔHCO3 / resp 1-2-4-5 ต่อ CO2 10 mmHg", minutes=10,
    source=f"{D} หน้า 212–220, 227–242", nl=["2.3.4(2)", "B9.2.5(2)", "3.3.17"],
    md='''
[[fig:nephro-07-02-f1]]

### STEP 1: pH

- pH < 7.35 → **acidemia** · pH > 7.45 → **alkalemia**

### STEP 2: PaCO2 เทียบกับ pH

- เปลี่ยน **ทิศทางเดียวกัน → metabolic** (pH ↓ PaCO2 ↓ = met acidosis · pH ↑ PaCO2 ↑ = met alkalosis)
- เปลี่ยน **คนละทิศ → respiratory** (pH ↓ PaCO2 ↑ = resp acidosis · pH ↑ PaCO2 ↓ = resp alkalosis)

### STEP 3: Compensation

**Metabolic primary** (HCO3 เปลี่ยนก่อน → ปอดชดเชย)
- Metabolic acidosis: **Predicted PaCO2 = 1.5 × HCO3 + 8 ± 2** (Winter's formula)
- Metabolic alkalosis: **ΔPaCO2 = 0.7 × ΔHCO3 ± 2** (predicted PaCO2 = 40 + 0.7 × ΔHCO3)
- **Trick (เฉพาะ metabolic)**: ตัวเลขหลังจุดทศนิยมของ pH ≈ PaCO2 → น่าจะ compensate พอดี (เช่น pH 7.27 PaCO2 25 · pH 7.50 PaCO2 48)

**Respiratory primary** (CO2 เปลี่ยนก่อน → ไตชดเชย) — ทุก PaCO2 เปลี่ยน 10 mmHg HCO3 เปลี่ยน

| | Acute | Chronic |
|---|---|---|
| Respiratory **acidosis** (กรด) | **1** | **4** |
| Respiratory **alkalosis** (เบส) | **2** | **5** |

### ตัวอย่างจากสไลด์ (ทำตามขั้น)

| ABG (pH / PaCO2 / HCO3) | Primary | ค่าที่คาด | สรุป |
|---|---|---|---|
| 7.25 / 60 / 26 | Resp acidosis | HCO3 = 24 + 2 = 26 | Acute resp acidosis, compensated |
| 7.50 / 45 / 34 | Met alkalosis | ΔCO2 = 0.7 × 10 = 7 → 47 ± 2 | Met alkalosis, compensated |
| 7.16 / 35 / 12 | Met acidosis | 1.5 × 12 + 8 = 26 ± 2 | PaCO2 สูงกว่าคาด → **+ resp acidosis** |
| 7.04 / 85 / 22 | Resp acidosis | HCO3 = 24 + 4.5 ≈ 28 | HCO3 ต่ำกว่าคาด → **+ met acidosis** |
| 7.27 / 25 / 11 | Met acidosis | 1.5 × 11 + 8 = 24.5 ± 2 | Compensated |
| 7.12 / 32 / 10 | Met acidosis | 1.5 × 10 + 8 = 23 ± 2 | **+ resp acidosis** |
| 7.34 / 65 / 34 | Resp acidosis (acute, หมดสติ 4 ชม.) | HCO3 = 24 + 2.5 ≈ 26.5 | HCO3 สูงกว่าคาด → **+ met alkalosis** (อาเจียน) |

> ทำไมต้องรู้ว่า acute/chronic: ข้อ 7.34/65/34 ถ้าเป็น COPD เรื้อรัง (คาด HCO3 = 24 + 4 × 2.5 = 34) จะเป็นแค่ chronic resp acidosis compensated — โจทย์จึงต้องบอกบริบท (หมดสติ 4 ชั่วโมง = acute)

> ตรวจความถูกต้องของ ABG ได้ด้วย Henderson–Hasselbalch: pH = 6.1 + log(HCO3 ÷ (0.03 × PaCO2)) (เสริม)
''',
    figs=[F_STEPS],
    pearls=[
        "PaCO2 กับ pH ทิศเดียวกัน = metabolic · คนละทิศ = respiratory",
        "Met acidosis: PaCO2 = 1.5 × HCO3 + 8 ± 2 · Met alkalosis: ΔCO2 = 0.7 × ΔHCO3",
        "Resp: ต่อ CO2 10 mmHg → HCO3 acute กรด 1 / เบส 2 · chronic กรด 4 / เบส 5",
        "ค่าจริงไม่ตรงที่คาด = มี disorder ที่สอง",
        "Trick: หลังจุดของ pH ≈ PaCO2 = compensated (metabolic เท่านั้น)",
    ],
    items=[
        mcq("NEPHRO-07-02-1",
            "An ABG shows pH 7.16, PaCO2 35 mmHg, HCO3 12 mEq/L. Which acid–base disorder is present?",
            "Metabolic acidosis with respiratory acidosis",
            ["Metabolic acidosis with appropriate respiratory compensation", "Metabolic acidosis with respiratory alkalosis", "Acute respiratory acidosis", "Chronic respiratory acidosis with metabolic alkalosis"],
            kind="old", src="ตัวอย่างในสไลด์",
            explain='''pH ↓ และ PaCO2 ↓ (ทิศเดียวกัน) → **primary metabolic acidosis** · Winter's: 1.5 × 12 + 8 = 26 ± 2 (24–28) แต่ PaCO2 จริง 35 **สูงกว่าที่คาด** → ปอดชดเชยไม่พอ = มี **respiratory acidosis ซ้อน**
- ถ้า compensate พอดี PaCO2 ต้องอยู่ราว 24–28
- Respiratory alkalosis ซ้อนจะทำให้ PaCO2 ต่ำกว่า 24
- Primary respiratory acidosis ต้องมี PaCO2 > 45
- HCO3 ต่ำ ไม่ใช่ metabolic alkalosis
(ตรวจ: 6.1 + log(12 ÷ 1.05) ≈ 7.16)''',
            pearl="Met acidosis + PaCO2 สูงกว่า Winter's = + resp acidosis", topic="Winter's formula",
            ref=[f"{D} หน้า 231–232"], nl=["2.3.4(2)"]),
        mcq("NEPHRO-07-02-2",
            "A patient is brought in after a cardiac arrest with return of spontaneous circulation. ABG: pH 7.04, PaCO2 85 mmHg, HCO3 22 mEq/L. Which acid–base disorder is present?",
            "Acute respiratory acidosis with metabolic acidosis",
            ["Acute respiratory acidosis with appropriate compensation", "Chronic respiratory acidosis with appropriate compensation", "Acute respiratory acidosis with metabolic alkalosis", "Metabolic acidosis with respiratory compensation"],
            kind="old", src="ตัวอย่างในสไลด์",
            explain='''pH ↓ PaCO2 ↑ (คนละทิศ) → **primary respiratory acidosis** (acute) · คาด HCO3 = 24 + 1 × (85 − 40)/10 ≈ 28.5 แต่จริง 22 **ต่ำกว่าคาด** → มี **metabolic acidosis ซ้อน** (lactic acidosis หลัง arrest)
- Compensated acute จะมี HCO3 ราว 28–29
- Chronic จะคาด HCO3 ราว 42 (24 + 4 × 4.5)
- Metabolic alkalosis ซ้อนจะทำให้ HCO3 สูงกว่า 28.5
- Primary metabolic acidosis ต้องมี PaCO2 ต่ำ ไม่ใช่ 85''',
            pearl="Resp acidosis + HCO3 ต่ำกว่าคาด = + met acidosis", topic="Mixed disorder",
            ref=[f"{D} หน้า 233–234"], nl=["2.3.4(2)"]),
        mcq("NEPHRO-07-02-3",
            "A 24-year-old man is found unresponsive on the floor, soiled with vomit; he was last seen well 4 hours ago. ABG: pH 7.34, PaCO2 65 mmHg, HCO3 34 mEq/L. Which acid–base disorder is present?",
            "Acute respiratory acidosis with metabolic alkalosis",
            ["Acute respiratory acidosis with appropriate compensation", "Metabolic alkalosis with appropriate compensation", "Acute respiratory acidosis with metabolic acidosis", "Respiratory alkalosis with metabolic acidosis"],
            kind="old", src="ตัวอย่างในสไลด์",
            explain='''pH ↓ PaCO2 ↑ → **primary respiratory acidosis** และเป็น **acute** (หมดสติ 4 ชั่วโมง) · คาด HCO3 = 24 + 2.5 ≈ 26.5 แต่จริง 34 **สูงกว่าคาด** → มี **metabolic alkalosis** ซ้อน (จากอาเจียน)
- Compensated acute จะมี HCO3 ราว 26–27
- Primary metabolic alkalosis จะมี pH > 7.45 แต่รายนี้ acidemia
- Metabolic acidosis ซ้อนจะทำให้ HCO3 ต่ำกว่า 26
- PaCO2 สูง ไม่ใช่ respiratory alkalosis
(ตรวจ: 6.1 + log(34 ÷ 1.95) ≈ 7.34)''',
            pearl="Acute resp acidosis + HCO3 สูงกว่าคาด + อาเจียน = + met alkalosis", topic="Acute vs chronic",
            ref=[f"{D} หน้า 241–242"], nl=["2.3.4(2)"]),
        mcq("NEPHRO-07-02-4",
            "A 68-year-old man with severe COPD is seen in clinic at his baseline. ABG on room air: pH 7.36, PaCO2 60 mmHg, HCO3 33 mEq/L. Which acid–base disorder is present?",
            "Chronic respiratory acidosis with appropriate compensation",
            ["Acute respiratory acidosis with metabolic alkalosis", "Primary metabolic alkalosis", "Acute respiratory acidosis with appropriate compensation", "Chronic respiratory acidosis with metabolic acidosis"],
            explain='''pH ↓ (ค่อนต่ำ) PaCO2 ↑ → respiratory acidosis ใน COPD ที่ stable = **chronic** · คาด HCO3 = 24 + 4 × 2 = **32** → จริง 33 ตรงกับที่คาด → **compensated chronic respiratory acidosis**
- ถ้าเป็น acute คาด HCO3 = 26 ค่าจริง 33 จะดูเหมือนมี met alkalosis ซ้อน — แต่บริบทคือเรื้อรัง
- Primary metabolic alkalosis ต้องมี pH > 7.45
- Metabolic acidosis ซ้อนจะทำให้ HCO3 ต่ำกว่า 32
(ตรวจ: 6.1 + log(33 ÷ 1.8) ≈ 7.36)''',
            pearl="Chronic resp acidosis: HCO3 ↑ 4 ต่อ CO2 10", topic="Chronic compensation",
            ref=[f"{D} หน้า 219–220"], nl=["2.3.4(2)"]),
        mcq_ordered("NEPHRO-07-02-5",
            "A 40-year-old man with gastric outlet obstruction has persistent vomiting. Serum HCO3 is 40 mEq/L and pH is 7.52. If respiratory compensation is appropriate, approximately what PaCO2 (mmHg) is expected?",
            ["40", "45", "51", "58", "65"], 2,
            explain='''Primary **metabolic alkalosis**: ΔHCO3 = 40 − 24 = 16 → ΔPaCO2 = 0.7 × 16 ≈ 11 → PaCO2 ที่คาด ≈ 40 + 11 = **51 ± 2**
- 40 คือไม่มีการชดเชยเลย
- 45 ชดเชยน้อยเกิน (ถ้าเจอจริงแปลว่ามี resp alkalosis ซ้อน)
- 58 และ 65 สูงเกินที่คาด (ถ้าเจอแปลว่ามี resp acidosis ซ้อน)
(ตรวจ: 6.1 + log(40 ÷ (0.03 × 51)) ≈ 7.52)''',
            pearl="Met alkalosis: PaCO2 ที่คาด = 40 + 0.7 × ΔHCO3", topic="Metabolic alkalosis compensation",
            ref=[f"{D} หน้า 216"], nl=["2.3.4(2)"]),
    ])

# ---------------------------------------------------------------- 07-03 AG & delta ratio
F_DELTA = fig("nephro-07-03-f1", "Anion gap & delta ratio", '''<svg viewBox="0 0 740 300">
 <defs><marker id="nephro-07-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="340" height="110" rx="10" class="acsoft"/>
 <text x="22" y="34" class="tb">STEP 4 · AG = Na − Cl − HCO3</text>
 <text x="22" y="56" class="t2">ปกติ 10 ± 2</text>
 <text x="22" y="80" class="tb">STEP 4.5 · ถ้า AG ปกติ ดู albumin</text>
 <text x="22" y="102" class="t2">Corrected AG = AG + 2.5 × (4 − Alb)</text>
 <rect x="370" y="10" width="360" height="110" rx="10" class="acsoft"/>
 <text x="382" y="34" class="tb">STEP 5 · ถ้า AG กว้าง</text>
 <text x="382" y="60" class="t2">Delta ratio = ΔAG ÷ ΔHCO3</text>
 <text x="382" y="84" class="t2">= (AG − 10) ÷ (24 − HCO3)</text>
 <text x="382" y="106" class="t3">(ใช้ AG ปกติ 10 ตามสไลด์)</text>
 <path d="M60 190H700" class="ln" marker-end="url(#nephro-07-03-a)"/>
 <path d="M260 180V200" class="ln"/>
 <path d="M460 180V200" class="ln"/>
 <text x="260" y="218" text-anchor="middle" class="tb">1</text>
 <text x="460" y="218" text-anchor="middle" class="tb">2</text>
 <rect x="60" y="140" width="196" height="36" rx="8" class="c1"/>
 <text x="158" y="163" text-anchor="middle" class="tw">&lt; 1</text>
 <rect x="264" y="140" width="192" height="36" rx="8" class="ok"/>
 <text x="360" y="163" text-anchor="middle" class="tw">1–2</text>
 <rect x="464" y="140" width="226" height="36" rx="8" class="c2"/>
 <text x="577" y="163" text-anchor="middle" class="tw">&gt; 2</text>
 <rect x="60" y="230" width="196" height="62" rx="8" class="c1soft"/>
 <text x="158" y="254" text-anchor="middle" class="tb">Wide AG + Normal AG</text>
 <text x="158" y="274" text-anchor="middle" class="t3">HCO3 ลดมากกว่า AG ที่เพิ่ม</text>
 <rect x="264" y="230" width="192" height="62" rx="8" class="oksoft"/>
 <text x="360" y="254" text-anchor="middle" class="tb">Pure wide AG MA</text>
 <text x="360" y="274" text-anchor="middle" class="t3">เพิ่ม/ลดพอ ๆ กัน</text>
 <rect x="464" y="230" width="226" height="62" rx="8" class="c2soft"/>
 <text x="577" y="254" text-anchor="middle" class="tb">Wide AG + Met alkalosis</text>
 <text x="577" y="274" text-anchor="middle" class="t3">HCO3 ลดน้อยกว่าที่ AG เพิ่ม</text>
</svg>''', "ด้านบนคือสูตรสามตัว ด้านล่างคือการแปลผล delta ratio เป็นสามช่วงตามสไลด์")

S3 = sec("nephro-07-03", "Acid–base STEP 4–5: anion gap, albumin & delta ratio",
    "AG = Na − Cl − HCO3 (10 ± 2) · corrected AG = AG + 2.5(4 − alb) · delta ratio <1 + NAGMA / 1–2 pure / >2 + met alk", minutes=10,
    source=f"{D} หน้า 221–226, 243–259", nl=["2.3.4(2)", "B9.2.5(2)", "B9.3(5)"],
    md='''
### STEP 4: Anion gap (เมื่อเป็น metabolic acidosis)

**AG = Na − Cl − HCO3** · ปกติ **10 ± 2**

- Normal AG (hyperchloremic) MA: เสีย HCO3 แล้ว **Cl เพิ่มขึ้นชดเชย** (diarrhea, RTA)
- Wide AG MA: มีกรดที่ไม่ใช่ Cl เพิ่มขึ้น (lactate, ketone, toxin, uremic acid)

### STEP 4.5: ถ้า AG ปกติ → ดู albumin

- Albumin เป็น anion ที่ไม่ได้วัด albumin ต่ำ → AG ต่ำลงหลอก
- **Corrected AG = AG + 2.5 × (4 − albumin)**
- ถ้า AG กว้างอยู่แล้ว การแก้ด้วย albumin มีแต่ทำให้กว้างขึ้น จึงดู albumin เมื่อ AG ปกติก็พอ (ตามสไลด์)

### STEP 5: ถ้า AG กว้าง → delta ratio

**Delta ratio = ΔAG ÷ ΔHCO3 = (AG − 10) ÷ (24 − HCO3)**

[[fig:nephro-07-03-f1]]

- **< 1** → wide AG MA **+ normal AG MA** (HCO3 ลดมากกว่าที่กรดเพิ่มอธิบายได้)
- **1–2** → **pure wide AG MA**
- **> 2** → wide AG MA **+ metabolic alkalosis** (HCO3 เดิมสูงอยู่ เช่น อาเจียน)

### ตัวอย่างจากสไลด์

| เคส | Lab | AG | Delta | สรุป |
|---|---|---|---|---|
| — | Na 140 Cl 116 HCO3 14 · pH 7.32 PaCO2 28 | 10 | — | Normal AG MA, compensated (Winter 29 ± 2) |
| — | Na 128 Cl 94 HCO3 12 · pH 7.28 PaCO2 24 | 22 | 12/12 = 1 | Pure wide AG MA, compensated |
| DM CKD หอบเฉียบพลัน 2 ชม. | Na 135 Cl 114 HCO3 14 · pH 7.47 PaCO2 20 | 7 | — | **Resp alkalosis** (คาด HCO3 = 24 − 4 = 20 แต่จริง 14) **+ normal AG MA** |
| ไม่รู้สึกตัวข้างขวดยา | Na 135 Cl 112 HCO3 12 Alb 2 · pH 7.09 PaCO2 34 | 11 → corrected 16 | 6/12 = 0.5 | Wide AG MA + normal AG MA + **resp acidosis** (Winter 26 ± 2) |
| หญิง 75 ปี ไข้ ท้องเสียมาก ช็อก | Na 125 Cl 94 HCO3 14 · pH 7.29 PaCO2 30 | 17 | 7/10 = 0.7 | Wide AG MA (lactic) + normal AG MA (diarrhea), compensated |
| T1DM ไข้ อาเจียน ปวดท้อง | Na 140 Cl 90 HCO3 12 · pH 7.27 PaCO2 27 | 38 | 28/12 ≈ 2.3 | Wide AG MA (DKA) + **met alkalosis** (อาเจียน), compensated |

> หมายเหตุตัวเลขในสไลด์: เคส "ขวดยา" สไลด์ใช้ HCO3 13 ตอนคำนวณ (AG 10, corrected 15) แต่ผลสรุปเหมือนกัน และค่า pH 7.09 ต่ำกว่าที่ Henderson–Hasselbalch ให้ (~7.17) · เคสรายที่ 2 pH ตามสูตรควร ~7.32 — ใช้ขั้นตอนเป็นหลัก
''',
    figs=[F_DELTA],
    pearls=[
        "AG = Na − Cl − HCO3 ปกติ 10 ± 2",
        "AG ปกติแต่ albumin ต่ำ → corrected AG = AG + 2.5 × (4 − alb)",
        "Delta ratio = (AG − 10)/(24 − HCO3): <1 + NAGMA · 1–2 pure · >2 + met alkalosis",
        "DKA + อาเจียน → delta ratio > 2 · lactic + diarrhea → delta < 1",
    ],
    items=[
        mcq("NEPHRO-07-03-1",
            "A 75-year-old woman presents with fever and profuse diarrhea. BT 38.5 °C, BP 78/30 mmHg, HR 130/min. Na 125, Cl 94, HCO3 14 mEq/L. ABG: pH 7.29, PaCO2 30 mmHg. Which acid–base disorder is present?",
            "High anion gap metabolic acidosis with normal anion gap metabolic acidosis, with appropriate respiratory compensation",
            ["Pure high anion gap metabolic acidosis with appropriate respiratory compensation",
             "High anion gap metabolic acidosis with metabolic alkalosis",
             "Normal anion gap metabolic acidosis with respiratory acidosis",
             "High anion gap metabolic acidosis with respiratory alkalosis"],
            kind="old", src="ตัวอย่างในสไลด์",
            explain='''Metabolic acidosis (pH ↓ PaCO2 ↓) · Winter's 1.5 × 14 + 8 = 29 ± 2 → PaCO2 30 compensated · AG = 125 − 94 − 14 = **17** (กว้าง — lactic acidosis จากช็อก) · delta ratio = (17 − 10) ÷ (24 − 14) = **0.7 (< 1)** → มี **normal AG MA ซ้อน** (เสีย HCO3 ทางท้องเสีย)
- Pure wide AG ต้องมี delta 1–2
- Met alkalosis ซ้อนต้องมี delta > 2
- PaCO2 ตรงกับที่คาด จึงไม่มี respiratory disorder ซ้อน''',
            pearl="ช็อก + ท้องเสีย → wide AG + normal AG MA (delta <1)", topic="Delta ratio <1",
            ref=[f"{D} หน้า 254–256"], nl=["2.3.4(2)"]),
        mcq("NEPHRO-07-03-2",
            "A 34-year-old man with type 1 diabetes presents with fever, nausea, repeated vomiting, and abdominal pain. Na 140, Cl 90, HCO3 12 mEq/L. ABG: pH 7.27, PaCO2 27 mmHg. Which acid–base disorder is present?",
            "High anion gap metabolic acidosis with metabolic alkalosis, with appropriate respiratory compensation",
            ["Pure high anion gap metabolic acidosis", "High anion gap with normal anion gap metabolic acidosis", "Normal anion gap metabolic acidosis with respiratory alkalosis", "High anion gap metabolic acidosis with respiratory acidosis"],
            kind="old", src="ตัวอย่างในสไลด์",
            explain='''Winter's 1.5 × 12 + 8 = 26 ± 2 → PaCO2 27 compensated · AG = 140 − 90 − 12 = **38** (DKA) · delta ratio = (38 − 10) ÷ (24 − 12) = 28 ÷ 12 ≈ **2.3 (> 2)** → HCO3 ลดน้อยกว่าที่กรดเพิ่ม แปลว่ามี **metabolic alkalosis** ซ้อน (จากอาเจียน)
- Pure wide AG ต้อง delta 1–2
- Normal AG MA ซ้อนต้อง delta < 1
- PaCO2 ตรงกับที่คาด ไม่มี respiratory disorder ซ้อน
(ตรวจ: 6.1 + log(12 ÷ 0.81) ≈ 7.27)''',
            pearl="DKA + อาเจียน → delta >2 = + met alkalosis", topic="Delta ratio >2",
            ref=[f"{D} หน้า 257–259"], nl=["2.3.4(2)"]),
        mcq("NEPHRO-07-03-3",
            "A 58-year-old man with diabetes and CKD presents with abrupt dyspnea for 2 hours. Na 135, K 5.6, Cl 114, HCO3 14 mEq/L, albumin 4.0 g/dL. ABG: pH 7.47, PaCO2 20 mmHg. Which acid–base disorder is present?",
            "Acute respiratory alkalosis with normal anion gap metabolic acidosis",
            ["Normal anion gap metabolic acidosis with appropriate compensation", "Acute respiratory alkalosis with appropriate compensation", "Chronic respiratory alkalosis with appropriate compensation", "High anion gap metabolic acidosis with respiratory alkalosis"],
            kind="old", src="ตัวอย่างในสไลด์",
            explain='''pH ↑ PaCO2 ↓ (คนละทิศ) → **primary respiratory alkalosis** (acute — หอบ 2 ชั่วโมง) · คาด HCO3 = 24 − 2 × 2 = 20 แต่จริง 14 **ต่ำกว่าคาด** → มี metabolic acidosis ซ้อน · AG = 135 − 114 − 14 = **7** (albumin ปกติ) → **normal AG MA** (จาก CKD ระยะต้น/RTA type 4 — สอดคล้องกับ K สูง)
- Normal AG MA เป็น primary ไม่ได้เพราะ pH > 7.45
- ถ้า compensated acute HCO3 ต้องราว 20
- Chronic resp alkalosis คาด HCO3 = 24 − 10 = 14 ซึ่งตรงพอดี — แต่อาการเพิ่งเกิด 2 ชั่วโมง จึงเป็น acute
- AG ไม่กว้าง
(ตรวจ: 6.1 + log(14 ÷ 0.6) ≈ 7.47)''',
            pearl="หอบเฉียบพลัน + HCO3 ต่ำกว่าคาด = resp alk + met acidosis", topic="Respiratory alkalosis mixed",
            ref=[f"{D} หน้า 248–249"], nl=["2.3.4(2)"]),
        mcq_ordered("NEPHRO-07-03-4",
            "A 56-year-old man with decompensated cirrhosis has Na 136, Cl 108, HCO3 18 mEq/L, and serum albumin 1.5 g/dL. What is his albumin-corrected anion gap?",
            ["10", "13", "16", "19", "22"], 2,
            explain='''AG = 136 − 108 − 18 = 10 (ดูปกติ) · albumin ต่ำมากทำให้ AG ต่ำหลอก → corrected AG = 10 + 2.5 × (4 − 1.5) = 10 + 6.25 ≈ **16** → จริง ๆ เป็น **wide AG** (ในผู้ป่วยตับแข็งคิดถึง lactic acidosis)
- 10 คือ AG ที่ยังไม่ได้แก้
- 13 แก้ไม่ครบ (คูณ 2.5 กับ 1.2 หรือคิด albumin ปกติเป็น 2.7)
- 19 และ 22 แก้เกิน (เช่นคูณ 4 หรือ 5 แทน 2.5)''',
            pearl="Albumin ต่ำ → AG ต่ำหลอก ต้อง correct", topic="Corrected anion gap",
            ref=[f"{D} หน้า 222, 252"], nl=["2.3.4(2)", "B9.3(5)"]),
    ])

LECTURE = lecture("07", "ABG interpretation", "Oxygenation · ventilation · compensation · anion gap · delta ratio",
    objectives=[
        "ตรวจว่าเป็น ABG จริง ประเมิน hypoxemia, A-a gradient, P/F ratio ได้",
        "หา primary disorder และคำนวณ compensation (Winter's, 0.7ΔHCO3, 1-2-4-5) เพื่อหา disorder ซ้อนได้",
        "คำนวณ anion gap, corrected AG และ delta ratio แล้วแปลผลได้",
    ],
    sections=[S1, S2, S3])
