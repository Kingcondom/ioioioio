from lib import lecture, sec, mcq, fig

D = "สไลด์ Update ข้อสอบ 2025"
SRC = "NL2 2025 (update)"

def R(*p):
    return [f"{D} หน้า " + ", ".join(str(x) for x in p)]

# ---------------------------------------------------------------- 04-01 Potassium
S1 = sec("exam25-04-01", "Potassium disorders & RTA",
    "HyperK + ECG เปลี่ยน → calcium gluconate ก่อน · อัมพาตเป็นพัก + thyrotoxic sign = TPP · K ต่ำ + NAGMA + urine pH > 5.5 = distal RTA", minutes=6,
    source=f"{D} หน้า 30–31, 53–55, 63–66", nl=["2.2.15", "2.3.6(7)", "2.3.14-3(12)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Hyperkalemia — 3 ขั้นตอน (สไลด์)**

| ขั้น | ทำอะไร | ยา |
|---|---|---|
| 1. Stabilize หัวใจ (มี weakness หรือ **ECG เปลี่ยน**) | กัน arrhythmia **ไม่ได้ลด K** | **10% calcium gluconate IV** |
| 2. Shift K เข้าเซลล์ | ออกฤทธิ์ใน 15–30 นาที | **50% glucose 50 mL + RI 10 U IV** · NaHCO3 (ถ้า acidosis) · β2-agonist NB |
| 3. เอา K ออก | | Kalimate/Kayexalate · furosemide · **hemodialysis** |

- ถ้าไม่ emergency (ไม่มี ECG change/อาการ) ทำแค่ขั้นที่ 3 ก็พอ

**Hypokalemic periodic paralysis**
- อ่อนแรง proximal เป็นพัก ๆ (มักกลางคืน/หลังกินแป้งหรือออกกำลัง) + K ต่ำขณะเป็น
- **Thyrotoxic PP**: ชายเอเชีย + **tremor, tachycardia, เหงื่อออก, hyperreflexia** → TSH ต่ำ FT4 สูง → รักษา hyperthyroid (MMI) + propranolol (เสริม)

**Renal tubular acidosis (ตารางสไลด์)** — ทุกชนิดเป็น **normal AG (hyperchloremic) metabolic acidosis**

| | Type 1 (distal) | Type 2 (proximal) | Type 4 |
|---|---|---|---|
| ความผิดปกติ | **หลั่ง H+ ที่ distal ไม่ได้** | ดูด HCO3 กลับที่ proximal ไม่ได้ | aldosterone ต่ำ/ดื้อ |
| Urine pH | **≥ 5.5** | < 5.5 (เมื่อ HCO3 ต่ำแล้ว) | < 5.5 |
| Serum K | ต่ำ–ปกติ | ต่ำ–ปกติ | **สูง** |
| สาเหตุ | Sjögren, RA, ยา, กรรมพันธุ์ · นิ่วไต | Fanconi (glucosuria, phosphaturia, aminoaciduria) | DM, obstructive uropathy, CAH |
''',
    pearls=[
        "HyperK + ECG เปลี่ยน → calcium gluconate IV ก่อนเสมอ",
        "Calcium gluconate ไม่ลด K · insulin+glucose ย้าย K · dialysis เอา K ออก",
        "อ่อนแรงเป็นพัก + tremor/tachycardia = thyrotoxic periodic paralysis (K ต่ำ)",
        "K ต่ำ + NAGMA + urine pH > 5.5 = distal RTA (H+ secretion บกพร่อง)",
    ],
    items=[
        mcq("EXAM25-04-01-1",
            "A 55-year-old man with chronic kidney disease presents with muscle weakness. ECG shows tall peaked T waves and widened QRS complexes. Serum potassium is 7.2 mmol/L. What is the most appropriate immediate management?",
            "Intravenous calcium gluconate",
            ["Intravenous insulin with glucose", "Intravenous sodium bicarbonate", "Hemodialysis", "Sodium polystyrene sulfonate"],
            kind="old", src=SRC,
            explain='''Hyperkalemia ที่มี **ECG เปลี่ยน (peaked T, QRS กว้าง)** และอ่อนแรง → ขั้นแรกคือ **stabilize cardiac membrane ด้วย 10% calcium gluconate IV** (ออกฤทธิ์ในไม่กี่นาที แม้ไม่ลด K)
- Insulin + glucose ย้าย K เข้าเซลล์ เป็นขั้นที่ 2 หลังให้ calcium
- NaHCO3 ใช้ช่วยย้าย K เมื่อมี metabolic acidosis และได้ผลน้อย
- Hemodialysis เอา K ออกได้ดีที่สุด แต่ต้องใช้เวลาเตรียม ไม่ใช่สิ่งแรก
- Sodium polystyrene sulfonate ออกฤทธิ์ช้าหลายชั่วโมง''',
            pearl="HyperK + ECG change → IV calcium gluconate ก่อน", topic="Hyperkalemia",
            ref=R(53, 54, 55), nl=["2.2.15"]),
        mcq("EXAM25-04-01-2",
            "A 25-year-old man has recurrent episodes of proximal muscle weakness (power grade II) that prevent him from getting out of bed. BP 150/90 mmHg, pulse 100/min. He has a fine hand tremor and hyperreflexia. Which electrolyte abnormality is most likely?",
            "Hypokalemia",
            ["Hypocalcemia", "Hypercalcemia", "Hypernatremia", "Hyperphosphatemia"],
            kind="old", src=SRC,
            explain='''อ่อนแรง proximal **เป็นพัก ๆ** ในชายอายุน้อย + อาการ thyrotoxicosis (**tremor, tachycardia, BP สูง, hyperreflexia**) = **thyrotoxic periodic paralysis** → K ต่ำจาก K ถูกดึงเข้าเซลล์ (Na-K-ATPase ทำงานมากขึ้น) · ตรวจ TSH ต่ำ FT3/FT4 สูง และรักษา hyperthyroid (MMI)
- Hypocalcemia ทำให้ tetany ชา Chvostek/Trousseau ไม่ใช่อัมพาตอ่อนปวกเปียก
- Hypercalcemia ทำให้อ่อนเพลีย สับสน ท้องผูก reflex ลดลง
- Hypernatremia ทำให้สับสนซึม ไม่ใช่อัมพาตเป็นพัก
- Hyperphosphatemia ทำให้ hypocalcemia ตามมา''',
            pearl="อัมพาตเป็นพัก + thyrotoxic sign = TPP (K ต่ำ)", topic="Thyrotoxic periodic paralysis",
            ref=R(30, 31), nl=["2.3.6(7)", "2.3.4(9)"]),
        mcq("EXAM25-04-01-3",
            "A 44-year-old man has recurrent nocturnal flaccid paralysis affecting all limbs (4 episodes in 2 years). During an attack: serum K 2.0 mmol/L, HCO₃ 15 mmol/L, normal anion gap, urine pH 6.1. What is the underlying pathogenesis of the hypokalemia?",
            "Defective H⁺ secretion in the distal tubule",
            ["Defective bicarbonate reabsorption in the proximal tubule", "Decreased aldosterone secretion", "Increased renal potassium reabsorption", "Defective Na⁺-K⁺ ATPase function"],
            kind="old", src=SRC,
            explain='''K ต่ำ + **normal AG metabolic acidosis** (HCO3 15) + **urine pH 6.1 (> 5.5) ทั้งที่เลือดเป็นกรด** = ไตขับกรดไม่ได้ = **distal (type 1) RTA** จาก **α-intercalated cell หลั่ง H+ ไม่ได้** → K ถูกขับแทน จึงเกิด hypokalemic paralysis
- Proximal RTA (ดูด HCO3 กลับไม่ได้) จะปรับ urine pH ให้ < 5.5 ได้เมื่อ HCO3 ในเลือดต่ำแล้ว (ตัวเลือกนี้เพิ่มแทน "defective K reabsorption at the proximal tubule" ในสไลด์ เพื่อให้แยก type 1 กับ type 2)
- Aldosterone ต่ำ (type 4 RTA) ทำให้ **K สูง** ไม่ใช่ต่ำ
- เพิ่มการดูด K กลับจะทำให้ K สูง
- Na-K-ATPase บกพร่อง ไม่ได้อธิบาย acidosis และ urine pH สูง''',
            pearl="K ต่ำ + NAGMA + urine pH > 5.5 = distal RTA", topic="Distal RTA",
            ref=R(63, 64, 65, 66), nl=["2.3.14-3(12)", "2.3.6(7)"]),
    ])

# ---------------------------------------------------------------- 04-02 SIADH
F_NA = fig("exam25-04-02-f1", "Approach to hyponatremia (ตามสไลด์)", '''<svg viewBox="0 0 720 340">
 <defs><marker id="exam25-04-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="220" height="38" rx="10" class="acsoft"/>
 <text x="360" y="34" text-anchor="middle" class="tb">Na &lt; 135 → Serum Osm</text>
 <path d="M310 48L170 76" class="ln" marker-end="url(#exam25-04-02-a)"/>
 <path d="M410 48L540 76" class="ln" marker-end="url(#exam25-04-02-a)"/>
 <rect x="30" y="78" width="270" height="44" rx="10" class="sunk"/>
 <text x="165" y="98" text-anchor="middle" class="tb">Sosm &gt; 280</text>
 <text x="165" y="115" text-anchor="middle" class="t3">pseudo-hypoNa (sugar, protein, lipid)</text>
 <rect x="420" y="78" width="250" height="44" rx="10" class="c1"/>
 <text x="545" y="105" text-anchor="middle" class="tw">Sosm &lt; 280 → Urine Osm</text>
 <path d="M480 122L330 150" class="ln" marker-end="url(#exam25-04-02-a)"/>
 <path d="M590 122L600 150" class="ln" marker-end="url(#exam25-04-02-a)"/>
 <rect x="170" y="152" width="250" height="44" rx="10" class="oksoft"/>
 <text x="295" y="172" text-anchor="middle" class="tb">Uosm &lt; 100</text>
 <text x="295" y="189" text-anchor="middle" class="t3">polydipsia, low solute intake</text>
 <rect x="480" y="152" width="230" height="44" rx="10" class="c1soft"/>
 <text x="595" y="172" text-anchor="middle" class="tb">Uosm &gt; 100 (ADH)</text>
 <text x="595" y="189" text-anchor="middle" class="t3">→ volume status</text>
 <path d="M520 196L130 226" class="ln" marker-end="url(#exam25-04-02-a)"/>
 <path d="M580 196L370 226" class="ln" marker-end="url(#exam25-04-02-a)"/>
 <path d="M640 196L610 226" class="ln" marker-end="url(#exam25-04-02-a)"/>
 <rect x="10" y="228" width="230" height="102" rx="10" class="c2soft"/>
 <text x="125" y="250" text-anchor="middle" class="tb">Hypervolemic</text>
 <text x="125" y="272" text-anchor="middle" class="t2">HF, cirrhosis</text>
 <text x="125" y="292" text-anchor="middle" class="t2">nephrotic, renal failure</text>
 <rect x="255" y="228" width="230" height="102" rx="10" class="badsoft"/>
 <text x="370" y="250" text-anchor="middle" class="tb">Euvolemic</text>
 <text x="370" y="272" text-anchor="middle" class="ta">SIADH</text>
 <text x="370" y="292" text-anchor="middle" class="t2">adrenal insufficiency</text>
 <text x="370" y="312" text-anchor="middle" class="t2">hypothyroid</text>
 <rect x="500" y="228" width="210" height="102" rx="10" class="misssoft"/>
 <text x="605" y="250" text-anchor="middle" class="tb">Hypovolemic</text>
 <text x="605" y="272" text-anchor="middle" class="t2">extrarenal: UNa &lt; 30</text>
 <text x="605" y="292" text-anchor="middle" class="t2">renal loss: UNa &gt; 30</text>
 <text x="605" y="312" text-anchor="middle" class="t3">(diuretic, salt wasting)</text>
</svg>''', "ตัด pseudohyponatremia ด้วย Sosm ดู Uosm ว่ามี ADH ทำงานหรือไม่ แล้วแยกด้วย volume status — SIADH อยู่ในกลุ่ม euvolemic")

S2 = sec("exam25-04-02", "Hyponatremia & SIADH",
    "SCLC + Na ต่ำ + euvolemic + Sosm ต่ำ + Uosm > 100 + UNa > 30 = SIADH (ตัด adrenal/thyroid ก่อน)", minutes=4,
    source=f"{D} หน้า 56–62", nl=["2.3.4-3(5)", "2.3.4(2)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

[[fig:exam25-04-02-f1]]

**เกณฑ์ SIADH (สไลด์)** — diagnosis of exclusion
- Serum Na < 135 · **Serum Osm < 275–280** · **Urine Osm > 100** (ปัสสาวะเข้มข้นเกินสมควร)
- **Euvolemic** (BP ปกติ JVP ปกติ ไม่บวม) · **Urine Na > 20–30**
- **ตัด adrenal insufficiency และ hypothyroidism** และไม่ได้ใช้ diuretic

**สาเหตุที่ออกบ่อย (ตารางสไลด์)**: **small cell lung cancer** (ectopic ADH) · pneumonia/TB · CNS (stroke, เลือดออก, ติดเชื้อ, trauma) · ยา (**carbamazepine**, SSRI, cyclophosphamide, opiates, MDMA) · หลังผ่าตัด ปวด คลื่นไส้

| แยกจาก | จุดต่าง |
|---|---|
| Primary polydipsia | **Uosm < 100** |
| Cerebral salt wasting | **hypovolemic** หลังโรคสมอง |
| Diuretic (thiazide) | ประวัติยา, มัก hypovolemic |
| Addison | BP ต่ำ, K สูง, hyperpigmentation |

> HypoNa ที่มี seizure/coma (severe symptoms) → **3% NaCl** · แก้ไม่เกิน 8–10 mEq/L ใน 24 ชม. กัน osmotic demyelination (เสริม)
''',
    figs=[F_NA],
    pearls=[
        "SCLC + hypoNa euvolemic = SIADH",
        "SIADH: Sosm < 275, Uosm > 100, UNa > 30, euvolemic, ตัด adrenal/thyroid",
        "Uosm < 100 = polydipsia ไม่ใช่ SIADH",
        "Severe symptom (ชัก) → 3% NaCl แต่แก้ไม่เกิน 8–10 ใน 24 ชม.",
    ],
    items=[
        mcq("EXAM25-04-02-1",
            "A 68-year-old man with small-cell lung cancer presents after a generalized tonic-clonic seizure. BP 125/80 mmHg, normal JVP, no edema. Na 112 mEq/L, serum osmolality 240 mOsm/kg, urine osmolality 520 mOsm/kg, urine specific gravity 1.028. Thyroid, adrenal and renal function are normal. He denies diuretic use or excessive fluid intake. What is the most likely diagnosis?",
            "Syndrome of inappropriate ADH secretion",
            ["Cerebral salt wasting", "Psychogenic polydipsia", "Diuretic-induced hyponatremia", "Addisonian crisis"],
            kind="old", src=SRC,
            explain='''ครบเกณฑ์ **SIADH**: Na ต่ำ + **Sosm ต่ำ (240)** + **Uosm สูง (520)** + **euvolemic** (BP/JVP ปกติ ไม่บวม) + thyroid/adrenal/renal ปกติ ไม่ใช้ diuretic · สาเหตุ = **ectopic ADH จาก SCLC** · ชักจาก Na 112 → ต้องให้ 3% NaCl
- Cerebral salt wasting เกิดหลังโรคสมอง และผู้ป่วยจะ **hypovolemic**
- Psychogenic polydipsia ทำให้ **Uosm < 100** (ปัสสาวะเจือจาง)
- Diuretic ถูกตัดออกแล้วจากประวัติ
- Addisonian crisis ให้ BP ต่ำ K สูง และโจทย์บอก adrenal ปกติ''',
            pearl="SCLC + Na ต่ำ euvolemic + Uosm สูง = SIADH", topic="SIADH",
            ref=R(56, 57, 58, 59, 60), nl=["2.3.4-3(5)"]),
        mcq("EXAM25-04-02-2",
            "A 65-year-old man with small-cell lung carcinoma presents with confusion. He is clinically euvolemic. Serum sodium is 118 mmol/L. Which mechanism is most likely responsible for his hyponatremia?",
            "Syndrome of inappropriate ADH secretion",
            ["Primary polydipsia", "Adrenal insufficiency", "Renal tubular acidosis", "Congestive heart failure"],
            kind="old", src=SRC,
            explain='''Small cell lung cancer หลั่ง ADH เอง (ectopic) → ไตดูดน้ำกลับมากเกิน → **SIADH** เป็นสาเหตุ hyponatremia ที่พบบ่อยที่สุดในมะเร็งชนิดนี้
- Primary polydipsia เป็นโรคจิตเวช/ดื่มน้ำมาก ไม่เกี่ยวกับ SCLC
- Adrenal insufficiency เกิดได้จาก metastasis ไปต่อมหมวกไต แต่พบน้อยกว่ามากและมัก BP ต่ำ K สูง
- RTA ทำให้ acidosis และ K ผิดปกติ ไม่ใช่ Na ต่ำ
- CHF ให้ hypervolemic hyponatremia ซึ่งรายนี้ euvolemic (โจทย์เดิมไม่ได้ให้ volume status — เพิ่ม "euvolemic" เพื่อให้ตัดได้)''',
            pearl="SCLC → ectopic ADH → SIADH", topic="SIADH",
            ref=R(61, 62), nl=["2.3.4-3(5)"]),
    ])

LECTURE = lecture("04", "Nephro & electrolytes", "hyperK · periodic paralysis · RTA · SIADH",
    objectives=[
        "จัดลำดับการรักษา hyperkalemia ตาม 3 ขั้น",
        "จับ thyrotoxic periodic paralysis และ distal RTA จาก lab",
        "วินิจฉัย SIADH ด้วย Sosm, Uosm, volume และ UNa",
    ],
    sections=[S1, S2])
