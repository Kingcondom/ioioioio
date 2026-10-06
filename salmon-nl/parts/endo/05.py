from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Endocrine"
NLCA = ["B11.2.5-3(5)", "2.3.4(2)", "B11.1.2(2)e"]

# ---------------------------------------------------------------- 05-01 Ca physiology & causes
F_LOOP = fig("endo-05-01-f1", "วงจร Ca–PTH–vitamin D", '''<svg viewBox="0 0 740 400">
 <defs><marker id="endo-05-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="280" y="10" width="180" height="48" rx="10" class="acsoft"/>
 <text x="370" y="31" text-anchor="middle" class="tb">Parathyroid</text>
 <text x="370" y="49" text-anchor="middle" class="t3">CaSR รับรู้ Ca</text>
 <path d="M370 58V96" class="lna" marker-end="url(#endo-05-01-a)"/>
 <text x="382" y="82" class="ta">PTH</text>
 <rect x="20" y="100" width="200" height="86" rx="10" class="c1soft"/>
 <text x="120" y="122" text-anchor="middle" class="tb">กระดูก</text>
 <text x="120" y="144" text-anchor="middle" class="t2">bone resorption</text>
 <text x="120" y="164" text-anchor="middle" class="t2">ปล่อย Ca + PO4</text>
 <rect x="270" y="100" width="200" height="86" rx="10" class="c2soft"/>
 <text x="370" y="122" text-anchor="middle" class="tb">ไต</text>
 <text x="370" y="142" text-anchor="middle" class="t2">ดูด Ca กลับ ↑</text>
 <text x="370" y="160" text-anchor="middle" class="t2">ขับ PO4 ทิ้ง ↑</text>
 <text x="370" y="178" text-anchor="middle" class="t3">1α-hydroxylase ↑</text>
 <rect x="520" y="100" width="200" height="86" rx="10" class="oksoft"/>
 <text x="620" y="122" text-anchor="middle" class="tb">ลำไส้</text>
 <text x="620" y="144" text-anchor="middle" class="t2">ดูดซึม Ca ↑</text>
 <text x="620" y="164" text-anchor="middle" class="t2">ดูดซึม PO4 ↑</text>
 <path d="M300 82H120V98" class="lna" marker-end="url(#endo-05-01-a)"/>
 <path d="M470 150H518" class="lnok" marker-end="url(#endo-05-01-a)"/>
 <text x="494" y="140" text-anchor="middle" class="t3">1,25-D</text>
 <rect x="20" y="214" width="340" height="62" rx="10" class="box"/>
 <text x="190" y="238" text-anchor="middle" class="tb">PTH net effect</text>
 <text x="190" y="262" text-anchor="middle" class="ta">Ca ↑ · PO4 ↓</text>
 <rect x="380" y="214" width="340" height="62" rx="10" class="box"/>
 <text x="550" y="238" text-anchor="middle" class="tb">Vitamin D net effect</text>
 <text x="550" y="262" text-anchor="middle" class="ta">Ca ↑ · PO4 ↑</text>
 <rect x="20" y="294" width="700" height="96" rx="10" class="sunk"/>
 <text x="32" y="318" class="tb">Negative feedback</text>
 <text x="32" y="340" class="t2">Ca สูงจากสาเหตุนอก parathyroid → PTH ถูกกด (PTH-independent)</text>
 <text x="32" y="362" class="t2">PTH สูง/ปกติทั้งที่ Ca สูง = PTH-dependent (1°, 3° HPT, FHH, lithium)</text>
 <text x="32" y="382" class="t3">ใช้ PO4 ช่วยแยก: PO4 ต่ำ → PTH/PTHrP · PO4 สูง → vitamin D (หรือไตวาย)</text>
</svg>''', "PTH ทำให้ Ca ขึ้นแต่ PO4 ลง ส่วน vitamin D ทำให้ขึ้นทั้งคู่ — ใช้ PO4 กับ PTH คู่กันแยกสาเหตุ hypercalcemia")

F_APP = fig("endo-05-01-f2", "Approach to hypercalcemia", '''<svg viewBox="0 0 740 330">
 <defs><marker id="endo-05-01-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="10" width="280" height="44" rx="10" class="acsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">Ca สูง (ยืนยัน corrected/ionized Ca)</text>
 <text x="370" y="46" text-anchor="middle" class="t3">ส่ง intact PTH</text>
 <path d="M300 54L190 88" class="ln" marker-end="url(#endo-05-01-b)"/>
 <path d="M440 54L550 88" class="ln" marker-end="url(#endo-05-01-b)"/>
 <rect x="40" y="90" width="300" height="40" rx="10" class="c1"/>
 <text x="190" y="115" text-anchor="middle" class="tw">PTH ↑ หรือปกติ = PTH-dependent</text>
 <rect x="400" y="90" width="300" height="40" rx="10" class="c2"/>
 <text x="550" y="115" text-anchor="middle" class="tw">PTH ↓ = PTH-independent</text>
 <rect x="40" y="140" width="300" height="180" rx="10" class="c1soft"/>
 <text x="52" y="164" class="tb">1° hyperparathyroidism</text>
 <text x="52" y="182" class="t3">adenoma · ผู้ป่วยนอก รพ. บ่อยสุด · PO4 ต่ำ</text>
 <text x="52" y="208" class="tb">3° hyperparathyroidism</text>
 <text x="52" y="226" class="t3">CKD นาน / หลังปลูกถ่ายไต</text>
 <text x="52" y="252" class="tb">FHH</text>
 <text x="52" y="270" class="t3">CaSR ไวต่ำ · urine Ca ต่ำ (FECa &lt; 0.01)</text>
 <text x="52" y="296" class="tb">Lithium</text>
 <text x="52" y="314" class="t3">เพิ่ม set point ของ CaSR</text>
 <rect x="400" y="140" width="300" height="180" rx="10" class="c2soft"/>
 <text x="412" y="164" class="tb">Malignancy</text>
 <text x="412" y="182" class="t3">PTHrP (squamous, breast, RCC) · osteolytic</text>
 <text x="412" y="198" class="t3">mets · ผู้ป่วยใน รพ. บ่อยสุด</text>
 <text x="412" y="224" class="tb">Vitamin D-dependent</text>
 <text x="412" y="242" class="t3">vit D intoxication · granuloma (TB, sarcoid)</text>
 <text x="412" y="258" class="t3">lymphoma → PO4 สูง</text>
 <text x="412" y="284" class="tb">อื่น ๆ</text>
 <text x="412" y="302" class="t3">immobilization · thyrotoxicosis · milk-alkali</text>
 <text x="412" y="316" class="t3">thiazide · vitamin A</text>
</svg>''', "ขั้นแรกส่ง PTH: ถ้า PTH ไม่ถูกกดทั้งที่ Ca สูง แปลว่าต้นเหตุอยู่ที่ parathyroid/CaSR")

S1 = sec("endo-05-01", "Hypercalcemia: สรีรวิทยา สาเหตุ และอาการ",
    "PTH ↑Ca ↓PO4 · vit D ↑Ca ↑PO4 · mild 10.5–12 · moderate 12–14 · severe >14 · ส่ง PTH: ↑/ปกติ = 1° HPT (บ่อยสุด OPD) · ↓ = malignancy (บ่อยสุด IPD), vit D · stones bones groans moans", minutes=10,
    source=f"{D} หน้า 243–248, 252–257", nl=NLCA,
    md='''
### สรีรวิทยา (สไลด์หน้า 243)

[[fig:endo-05-01-f1]]

- **PTH net effect: ↑Ca, ↓PO4** (ดูด Ca กลับที่ไต ขับ PO4 ทิ้ง ปล่อย Ca จากกระดูก กระตุ้น 1α-hydroxylase)
- **Vitamin D net effect: ↑Ca, ↑PO4** (ดูดซึมจากลำไส้ทั้งคู่)
- Corrected Ca = measured Ca + **0.8 × (4 − albumin)** (เสริม)

### ความรุนแรง (สไลด์หน้า 244)
- **Mild 10.5–12 mg/dL** · **Moderate 12–14** · **Severe > 14**

### สาเหตุ (สไลด์หน้า 244–245)

[[fig:endo-05-01-f2]]

| PTH-dependent (PTH ↑/ปกติ) | PTH-independent (PTH ↓) |
|---|---|
| **1° hyperparathyroidism** (parathyroid adenoma 80–85%) | **Hypercalcemia of malignancy**: PTHrP (humoral — squamous cell CA, breast, renal), osteolytic mets (breast, myeloma), 1,25-D (lymphoma) |
| **3° hyperparathyroidism** (CKD นานจน parathyroid ทำงานเอง) | **Vitamin D-dependent**: **vit D intoxication**, **granulomatous disease** (TB, sarcoidosis) |
| **Familial hypocalciuric hypercalcemia (FHH)** — **↓CaSR sensitivity** (ต้องใช้ Ca สูงมากจึงกด PTH ได้) + **↓renal Ca excretion** | Other: **immobilization**, endocrine (thyrotoxicosis, adrenal insufficiency), **milk-alkali**, drug (thiazide, vitamin A) |
| **Lithium** | |

- **2° hyperparathyroidism** (CKD, vit D deficiency) → PTH สูง แต่ **Ca ต่ำ/ปกติ** (ตอบสนองต่อ Ca ต่ำ) — ไม่ใช่สาเหตุ hypercalcemia (สไลด์หน้า 247: persistent 2° → กลายเป็น 3°)
- ผู้ป่วยนอกโรงพยาบาล → **1° HPT** บ่อยที่สุด · ผู้ป่วยในโรงพยาบาล → **malignancy** บ่อยที่สุด (เสริม)

### อาการ (สไลด์หน้า 246) — "stones, bones, groans, moans"
- **Psychiatric**: วิตกกังวล ซึมเศร้า อ่อนเพลีย ("**psychiatric moans**")
- **Neuro**: สับสน ซึม stupor อ่อนแรง
- **Cardio**: **short QT**, arrhythmia
- **GI**: คลื่นไส้อาเจียน **ท้องผูก**, **pancreatitis**, PUD ("**abdominal groans**")
- **Kidney**: **นิ่ว**, **polyuria (nephrogenic DI)** → ขาดน้ำ → **prerenal AKI** ("**renal stones**")
- **Bone**: ปวดกระดูก (osteitis fibrosa cystica ใน 1° HPT) ("**painful bones**")

> ผู้สูงอายุ **PTH สูง + Ca สูง + PO4 ต่ำ** + ประวัตินิ่ว = **1° hyperparathyroidism** · **Ca สูง + PO4 สูง** + กินวิตามิน/ยากระดูกพรุน (Ca + vit D) = **vitamin D intoxication**
''',
    figs=[F_LOOP, F_APP],
    pearls=[
        "PTH: Ca ↑ PO4 ↓ · vitamin D: Ca ↑ PO4 ↑",
        "Hypercalcemia → ส่ง PTH ก่อน: ไม่ถูกกด = PTH-dependent",
        "OPD → 1° HPT · IPD/มะเร็ง → PTHrP/bone mets",
        "Ca สูง + PO4 สูง = vit D intoxication / granuloma",
        "Stones, bones, abdominal groans, psychiatric moans + short QT + polyuria",
    ],
    items=[
        mcq("ENDO-05-01-1",
            "A 70-year-old patient asks about abnormal laboratory results. PTH 126 pg/mL (high), Ca 11 mg/dL, PO4 2 mg/dL, Cr 1.1 mg/dL. He takes a daily multivitamin and passed 'sand' in his urine 10 years ago. What is the most likely diagnosis?",
            "Primary hyperparathyroidism",
            ["Humoral hypercalcemia of malignancy", "Hypercalcemia from bone metastasis", "Secondary hyperparathyroidism", "Tertiary hyperparathyroidism"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**PTH สูง + Ca สูง + PO4 ต่ำ** (net effect ของ PTH) + **ประวัตินิ่ว** + ไตปกติ = **primary hyperparathyroidism**
- Malignancy (PTHrP หรือ bone mets) ต้องมี **PTH ถูกกดต่ำ**
- 2° HPT มี PTH สูงแต่ **Ca ต่ำหรือปกติ** (ตอบสนองต่อ Ca ต่ำ เช่น CKD, vit D deficiency) และ PO4 สูงใน CKD
- 3° HPT เกิดใน **CKD นาน/หลังปลูกถ่ายไต** แต่ Cr รายนี้ปกติ
- Multivitamin ขนาดปกติไม่ทำให้ PTH สูง (vit D intoxication กด PTH)''',
            pearl="PTH ↑ Ca ↑ PO4 ↓ ไตปกติ = 1° HPT", topic="Primary HPT",
            ref=[f"{D} หน้า 243–245, 252–253"], nl=NLCA),
        mcq("ENDO-05-01-2",
            "A 50-year-old woman taking calcium and vitamin D supplements to prevent osteoporosis presents with drowsiness. Ca 14.8 mg/dL, PO4 6 mg/dL; other laboratory values are within normal limits. What is the most likely cause of hypercalcemia?",
            "Vitamin D intoxication",
            ["Primary hyperparathyroidism", "Humoral hypercalcemia of malignancy (PTHrP)", "Familial hypocalciuric hypercalcemia", "Bisphosphonate toxicity"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**Ca สูง + PO4 สูง** = net effect ของ **vitamin D** (ดูดซึมทั้ง Ca และ PO4 จากลำไส้) + ประวัติกินยาเสริมสำหรับกระดูกพรุน → **vitamin D intoxication** (ร่วมกับ Ca supplement)
- 1° HPT และ PTHrP ทำให้ **PO4 ต่ำ**
- FHH ทำให้ Ca สูงเล็กน้อย ไม่มีอาการ PO4 ปกติ
- Bisphosphonate ทำให้ Ca **ต่ำ** ไม่ใช่สูง''',
            pearl="Ca ↑ + PO4 ↑ + ยากระดูก/วิตามิน = vit D intoxication", topic="Vitamin D intoxication",
            ref=[f"{D} หน้า 243, 256–257"], nl=NLCA + ["2.3.4-3(6)"]),
        mcq("ENDO-05-01-3",
            "A 62-year-old woman with advanced breast cancer and liver metastasis has fatigue, lethargy, constipation, nocturnal polyuria and polydipsia for 1 week. BP 98/65 mmHg, HR 103/min; somnolent with dry mucosa. She has no bone pain, and a recent bone scan was negative. BUN/Cr 37/1.4 mg/dL, Ca 15.7 mg/dL, Na 151 mmol/L. What is the most likely mechanism of her hypercalcemia?",
            "Humoral hypercalcemia of malignancy mediated by PTHrP",
            ["Osteolytic bone metastasis", "Primary hyperparathyroidism", "Secondary hyperparathyroidism", "Tertiary hyperparathyroidism"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''มะเร็งระยะลุกลาม + Ca สูงมาก (15.7) **โดยไม่มีอาการปวดกระดูกหรือ osteolytic lesion** → **humoral hypercalcemia of malignancy (PTHrP)** · polyuria (nephrogenic DI) + Na 151 + prerenal AKI เป็นผลของ hypercalcemia
- Osteolytic bone metastasis จะมี bone pain/osteolytic lesion (สไลด์เฉลยเน้นข้อนี้) — มะเร็งเต้านมทำได้ทั้งสองกลไก แต่โจทย์ไม่มีหลักฐานกระดูก
- 1° HPT ทำให้ Ca สูงไม่มาก เรื้อรัง และไม่สอดคล้องกับมะเร็งลุกลาม
- 2° HPT มี Ca ต่ำ/ปกติ
- 3° HPT ต้องมี CKD นาน''',
            pearl="มะเร็ง + Ca สูงมาก ไม่มี bone lesion → PTHrP", topic="Malignancy",
            ref=[f"{D} หน้า 245, 254–255"], nl=NLCA),
        mcq("ENDO-05-01-4",
            "A 38-year-old asymptomatic man has Ca 10.9 mg/dL found incidentally; his mother had similar results. PTH is mildly elevated, PO4 normal, 24-hour urine calcium is low and the calcium/creatinine clearance ratio is 0.005. What is the most likely diagnosis?",
            "Familial hypocalciuric hypercalcemia",
            ["Primary hyperparathyroidism", "Vitamin D intoxication", "Milk-alkali syndrome", "Sarcoidosis"],
            explain='''Ca สูงเล็กน้อย ไม่มีอาการ มีประวัติครอบครัว + **urine Ca ต่ำ (Ca/Cr clearance ratio < 0.01)** + PTH ปกติ/สูงเล็กน้อย = **FHH** (inactivating CaSR mutation → ต้องใช้ Ca สูงขึ้นจึงกด PTH และไตดูด Ca กลับมาก) — ไม่ต้องผ่าตัด
- 1° HPT มี PTH สูงเหมือนกันแต่ **urine Ca ปกติ/สูง** (ratio > 0.02)
- Vitamin D intoxication และ sarcoidosis กด PTH และ PO4 มักสูง
- Milk-alkali มีประวัติกิน Ca + antacid มาก และ metabolic alkalosis, PTH ต่ำ''',
            pearl="Ca สูง + urine Ca ต่ำ + ครอบครัว = FHH ไม่ต้องผ่าตัด", topic="FHH",
            ref=[f"{D} หน้า 244"], nl=NLCA),
    ])

# ---------------------------------------------------------------- 05-02 Management
F_MX = fig("endo-05-02-f1", "Hypercalcemia management", '''<svg viewBox="0 0 740 360">
 <defs><marker id="endo-05-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="20" width="200" height="74" rx="10" class="c1"/>
 <text x="110" y="46" text-anchor="middle" class="tw">1 · IV NSS</text>
 <text x="110" y="66" text-anchor="middle" class="tw">4–6 L/วัน</text>
 <text x="110" y="84" text-anchor="middle" class="tw">± calcitonin</text>
 <path d="M210 57H248" class="ln" marker-end="url(#endo-05-02-a)"/>
 <rect x="250" y="20" width="220" height="74" rx="10" class="box"/>
 <text x="360" y="44" text-anchor="middle" class="tb">Furosemide</text>
 <text x="360" y="64" text-anchor="middle" class="t2">เฉพาะ volume overload</text>
 <text x="360" y="84" text-anchor="middle" class="t3">ห้ามถ้ายัง hypovolemia</text>
 <path d="M470 57H508" class="ln" marker-end="url(#endo-05-02-a)"/>
 <rect x="510" y="20" width="220" height="74" rx="10" class="acsoft"/>
 <text x="620" y="44" text-anchor="middle" class="tb">หาสาเหตุ</text>
 <text x="620" y="64" text-anchor="middle" class="t2">PTH, PTHrP, 25-/1,25-D</text>
 <text x="620" y="84" text-anchor="middle" class="t3">ติดตาม volume, UO, Ca</text>
 <path d="M560 94L380 140" class="ln" marker-end="url(#endo-05-02-a)"/>
 <path d="M600 94L540 140" class="ln" marker-end="url(#endo-05-02-a)"/>
 <path d="M660 94L670 140" class="ln" marker-end="url(#endo-05-02-a)"/>
 <rect x="200" y="142" width="240" height="96" rx="10" class="c2soft"/>
 <text x="320" y="164" text-anchor="middle" class="tb">Malignancy / ไม่ทราบ</text>
 <text x="320" y="186" text-anchor="middle" class="t2">Bisphosphonate IV</text>
 <text x="320" y="204" text-anchor="middle" class="t3">zoledronate 4 mg · pamidronate 60–90</text>
 <text x="320" y="226" text-anchor="middle" class="t2">GFR &lt; 30 → denosumab</text>
 <rect x="450" y="142" width="150" height="96" rx="10" class="oksoft"/>
 <text x="525" y="164" text-anchor="middle" class="tb">Vit D-dependent</text>
 <text x="525" y="190" text-anchor="middle" class="t2">Corticosteroid</text>
 <text x="525" y="210" text-anchor="middle" class="t3">granuloma, lymphoma,</text>
 <text x="525" y="226" text-anchor="middle" class="t3">vit D intox</text>
 <rect x="610" y="142" width="120" height="96" rx="10" class="c1soft"/>
 <text x="670" y="170" text-anchor="middle" class="tb">1° HPT</text>
 <text x="670" y="196" text-anchor="middle" class="t2">ผ่าตัด</text>
 <text x="670" y="218" text-anchor="middle" class="t3">± cinacalcet</text>
 <rect x="10" y="142" width="180" height="96" rx="10" class="sunk"/>
 <text x="20" y="164" class="tb">Calcitonin</text>
 <text x="20" y="186" class="t2">ออกฤทธิ์ 4–6 ชม.</text>
 <text x="20" y="206" class="t2">tachyphylaxis 48 ชม.</text>
 <text x="20" y="226" class="t3">คร่อมรอ bisphosphonate</text>
 <rect x="10" y="256" width="720" height="44" rx="10" class="badsoft"/>
 <text x="370" y="283" text-anchor="middle" class="tb">ไม่ถึงเป้า / Ca &gt; 18 + ซึม / ไตวาย / HF → Hemodialysis</text>
 <rect x="10" y="310" width="720" height="40" rx="10" class="box"/>
 <text x="370" y="335" text-anchor="middle" class="t2">Mild ไม่มีอาการ: ดื่มน้ำ หยุด thiazide/lithium/Ca/vit D แล้วรักษาสาเหตุ</text>
</svg>''', "ทุกรายเริ่มด้วยการให้น้ำเกลือ แล้วเลือกยาลด Ca ตามสาเหตุ — bisphosphonate ใช้เวลา 2–4 วันจึงได้ผล จึงต้องมี calcitonin คร่อม")

S2 = sec("endo-05-02", "Hypercalcemia: การรักษา",
    "ขั้นแรก IV NSS 4–6 L/วัน · furosemide เฉพาะ volume overload · calcitonin เร็วแต่ tachyphylaxis 48 ชม. · malignancy → IV bisphosphonate (ห้าม GFR <30) / denosumab · vit D-dependent → steroid · refractory → HD", minutes=8,
    source=f"{D} หน้า 249–251, 258–259", nl=NLCA + ["B9.4(2)"],
    md='''
### ขั้นแรก: สารน้ำ (สไลด์หน้า 249)
- **IV NSS 4–6 L/วัน** (เช่น 200–300 mL/hr เป้า UO 100–150 mL/hr — เสริม) — hypercalcemia ทำให้ **nephrogenic DI + อาเจียน → ขาดน้ำ** ซึ่งยิ่งลดการขับ Ca
- **Furosemide เฉพาะกรณี volume overload** · **ห้ามให้ถ้ายัง hypovolemia** (ทำให้ขาดน้ำมากขึ้น)
- Monitor volume status, urine output, Ca

### ยาลด Ca (สไลด์หน้า 250)

[[fig:endo-05-02-f1]]

| ยา | กลไก/เวลา | ใช้เมื่อ |
|---|---|---|
| **Calcitonin** (SC/IM 4 IU/kg q12h — เสริม) | ยับยั้ง osteoclast + ↑ขับ Ca · **ออกฤทธิ์เร็ว** แต่ **tachyphylaxis หลัง 48 ชม.** | ให้ร่วมกับ IV fluid ตั้งแต่แรกใน moderate–severe |
| **Bisphosphonate IV** — **pamidronate**, **zoledronate** | ยับยั้ง osteoclast · ได้ผลใน 2–4 วัน อยู่นาน | **Hypercalcemia of malignancy (PTHrP)** · **ห้ามใน GFR < 30** |
| **Denosumab** | RANKL antibody | malignancy · **ใช้ได้เมื่อ GFR < 30** · ระวัง hypocalcemia |
| **Corticosteroid** | ลดการสร้าง 1,25-D | **Vitamin D-dependent** (granuloma, lymphoma, vit D intoxication) |
| **Hemodialysis** | — | **Refractory**, Ca สูงมาก + ซึม, ไตวาย/HF ให้น้ำไม่ได้ |
| Cinacalcet / parathyroidectomy (เสริม) | — | 1° HPT (ผ่าตัดเมื่อมีอาการ, Ca > 1 เหนือ ULN, นิ่ว, กระดูกพรุน, อายุ < 50, eGFR < 60) |

> ข้อสอบ: Ca สูงมาก ซึม BP ยังดี → **NSS + bisphosphonate (pamidronate)** · **ไม่เลือก NSS + furosemide** เพราะผู้ป่วยขาดน้ำ · calcitonin + furosemide ขาดการให้น้ำ
''',
    figs=[F_MX],
    pearls=[
        "Hypercalcemia ทุกราย → IV NSS ก่อน (4–6 L/วัน)",
        "Furosemide เฉพาะ volume overload ห้ามใน hypovolemia",
        "Calcitonin เร็วแต่ tachyphylaxis 48 ชม. → คร่อมรอ bisphosphonate",
        "Bisphosphonate ห้าม GFR <30 → denosumab แทน",
        "Vit D-dependent → steroid · refractory → hemodialysis",
    ],
    items=[
        mcq("ENDO-05-02-1",
            "A 70-year-old woman presents with altered consciousness. BP 120/80 mmHg; she is drowsy with dry mucosa. Serum calcium is 18 mg/dL; creatinine 1.3 mg/dL. What is the next most appropriate management?",
            "0.9% NaCl plus IV pamidronate",
            ["0.9% NaCl plus furosemide", "Calcitonin plus furosemide", "Calcitonin plus pamidronate without IV fluid", "Oral prednisolone alone"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Severe hypercalcemia ที่ขาดน้ำ → **IV NSS** เป็นพื้นฐาน + **bisphosphonate IV (pamidronate)** ซึ่งออกฤทธิ์นาน (สาเหตุที่น่าจะเป็นในผู้สูงอายุ Ca 18 คือมะเร็ง)
- Furosemide ห้ามเมื่อยัง hypovolemia — สไลด์เน้นข้อนี้
- Calcitonin + furosemide ขาดการให้สารน้ำ
- ไม่ให้ IV fluid เลยผิดหลัก เพราะการขาดน้ำทำให้ไตขับ Ca ไม่ได้
- Prednisolone ใช้เฉพาะ vitamin D-dependent cause

(สไลด์ไม่ได้แสดงเฉลยเป็นข้อความ — hemodialysis เป็นทางเลือกเมื่อ Ca > 18 ร่วมกับอาการทางสมองรุนแรงหรือไตวาย/ให้น้ำไม่ได้ แต่ creatinine รายนี้ยังดี)''',
            pearl="Ca สูงมาก → NSS + bisphosphonate (ไม่ใช่ furosemide)", topic="Severe hypercalcemia",
            ref=[f"{D} หน้า 249–251, 258–259"], nl=NLCA),
        mcq("ENDO-05-02-2",
            "A 66-year-old man with squamous cell lung cancer has Ca 14.2 mg/dL, PTH suppressed. He has received 0.9% NaCl and calcitonin. His eGFR is 22 mL/min/1.73 m2. Which additional calcium-lowering agent is most appropriate?",
            "Denosumab",
            ["Zoledronic acid", "Hydrochlorothiazide", "Prednisolone", "Oral phosphate"],
            explain='''Hypercalcemia of malignancy (PTHrP จาก squamous cell CA) ต้องการยายับยั้ง osteoclast ระยะยาว · **eGFR < 30 → ห้าม bisphosphonate** → ใช้ **denosumab** (ไม่ขับทางไต)
- Zoledronic acid เป็นพิษต่อไต ห้ามเมื่อ GFR < 30
- Thiazide **เพิ่ม** การดูด Ca กลับ ทำให้ Ca สูงขึ้น
- Prednisolone ได้ผลเฉพาะ vitamin D-dependent (lymphoma, granuloma)
- Oral phosphate เสี่ยง Ca-PO4 ตกตะกอนในเนื้อเยื่อและไต''',
            pearl="Malignancy + GFR <30 → denosumab", topic="Denosumab",
            ref=[f"{D} หน้า 250"], nl=NLCA),
        mcq("ENDO-05-02-3",
            "A 45-year-old man with pulmonary sarcoidosis has Ca 13.1 mg/dL, PO4 4.8 mg/dL, suppressed PTH, low-normal 25-hydroxyvitamin D and elevated 1,25-dihydroxyvitamin D. After IV hydration, which drug best addresses the mechanism?",
            "Prednisolone",
            ["Furosemide", "Cinacalcet", "Calcium carbonate", "Hydrochlorothiazide"],
            explain='''Granuloma (sarcoidosis, TB) มี macrophage สร้าง **1α-hydroxylase** เปลี่ยน 25-D → **1,25-D** โดยไม่ถูกควบคุม → Ca และ PO4 สูง PTH ถูกกด → **corticosteroid** ยับยั้งการสร้าง 1,25-D (vitamin D-dependent → steroid ตามสไลด์)
- Furosemide ไม่ได้แก้สาเหตุและใช้เฉพาะ volume overload
- Cinacalcet ลด PTH ใช้ใน hyperparathyroidism แต่ PTH ถูกกดอยู่แล้ว
- Calcium carbonate เพิ่ม Ca
- Thiazide ลดการขับ Ca''',
            pearl="Granuloma/lymphoma (1,25-D สูง) → steroid", topic="Vitamin D-dependent",
            ref=[f"{D} หน้า 245, 250"], nl=NLCA + ["B11.4(3)"]),
        mcq("ENDO-05-02-4",
            "A 58-year-old woman with multiple myeloma has Ca 14 mg/dL. After 2 days of calcitonin and IV saline, her calcium initially fell but is now rising again despite continued calcitonin. What explains the loss of calcitonin effect?",
            "Tachyphylaxis to calcitonin after about 48 hours",
            ["Calcitonin is inactivated by normal saline", "Development of anti-calcitonin antibodies within hours", "Calcitonin only works in vitamin D intoxication", "Calcitonin requires normal renal function to act"],
            explain='''Calcitonin ลด Ca ได้เร็ว (4–6 ชม.) แต่ **receptor down-regulation ทำให้เกิด tachyphylaxis หลังประมาณ 48 ชม.** → จึงใช้เป็นตัวคร่อมระหว่างรอ **bisphosphonate** ออกฤทธิ์ (2–4 วัน)
- NSS ไม่ได้ทำลาย calcitonin
- Antibody ต่อ calcitonin (salmon) เกิดได้แต่ใช้เวลานาน ไม่ใช่สาเหตุใน 2 วัน
- Calcitonin ใช้ได้ทุกสาเหตุ ไม่จำเพาะ vitamin D
- ไม่ต้องการการทำงานของไตปกติจึงจะออกฤทธิ์''',
            pearl="Calcitonin หมดฤทธิ์หลัง 48 ชม. → ต้องมี bisphosphonate", topic="Calcitonin",
            ref=[f"{D} หน้า 250"], nl=NLCA),
    ])

LECTURE = lecture("05", "Hypercalcemia", "Ca–PTH–vitamin D · สาเหตุ · การรักษา",
    objectives=[
        "อธิบายผลของ PTH และ vitamin D ต่อ Ca และ PO4 และใช้แยกสาเหตุได้",
        "แบ่งสาเหตุ hypercalcemia เป็น PTH-dependent/independent จากค่า PTH",
        "รักษา hypercalcemia ตามลำดับ: NSS → calcitonin → bisphosphonate/denosumab/steroid → HD",
    ],
    sections=[S1, S2])
