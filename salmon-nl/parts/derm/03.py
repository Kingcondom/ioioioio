from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Dermato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 03-01 Urticaria
F_ANA = fig("derm-03-01-f1", "Urticaria เฉียบพลัน: คัดกรอง anaphylaxis ก่อนเสมอ", '''<svg viewBox="0 0 740 400">
 <defs><marker id="derm-03-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="10" width="280" height="46" rx="10" class="acsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">Wheal &amp; flare ± angioedema</text>
 <text x="370" y="47" text-anchor="middle" class="t3">เริ่มเป็นนาที–ชั่วโมง</text>
 <path d="M370 56V76" class="ln" marker-end="url(#derm-03-01-a)"/>
 <rect x="20" y="78" width="700" height="132" rx="10" class="badsoft"/>
 <text x="370" y="100" text-anchor="middle" class="tb">Anaphylaxis ถ้าเข้าข้อใดข้อหนึ่ง</text>
 <text x="40" y="128" class="t2">1. Acute onset + อาการผิวหนัง/mucosa + (BP ต่ำ หรือ อาการทางหายใจ)</text>
 <text x="40" y="154" class="t2">2. สัมผัสสิ่งที่น่าจะแพ้ + ≥ 2 ระบบ: ผิวหนัง · หายใจ · GI · BP ต่ำ</text>
 <text x="40" y="180" class="t2">3. สัมผัสสิ่งที่รู้ว่าแพ้ + BP ต่ำ</text>
 <text x="40" y="200" class="t3">(stridor, หอบ wheeze, ปวดท้อง อาเจียน, หน้ามืด)</text>
 <path d="M200 210V240" class="ln" marker-end="url(#derm-03-01-a)"/>
 <text x="210" y="230" class="t3">ใช่</text>
 <path d="M540 210V240" class="ln" marker-end="url(#derm-03-01-a)"/>
 <text x="550" y="230" class="t3">ไม่ใช่</text>
 <rect x="20" y="242" width="360" height="148" rx="10" class="bad"/>
 <text x="200" y="266" text-anchor="middle" class="tw">IM epinephrine 1:1,000 ที่ต้นขา</text>
 <text x="200" y="290" text-anchor="middle" class="tw">ผู้ใหญ่ 0.3–0.5 mg</text>
 <text x="200" y="312" text-anchor="middle" class="tw">เด็ก 0.01 mg/kg</text>
 <text x="200" y="338" text-anchor="middle" class="tw">+ airway + IV fluid</text>
 <text x="200" y="362" text-anchor="middle" class="tw">ซ้ำได้ทุก 5–15 นาที (เสริม)</text>
 <rect x="400" y="242" width="320" height="148" rx="10" class="oksoft"/>
 <text x="560" y="266" text-anchor="middle" class="tb">Acute urticaria ธรรมดา</text>
 <text x="560" y="292" text-anchor="middle" class="t2">2nd-gen antihistamine</text>
 <text x="560" y="312" text-anchor="middle" class="t3">cetirizine · loratadine · fexofenadine</text>
 <text x="560" y="338" text-anchor="middle" class="t2">+ prednisolone ถ้ารุนแรง</text>
 <text x="560" y="362" text-anchor="middle" class="t2">+ เลี่ยง trigger</text>
</svg>''', "ผื่นลมพิษทุกรายต้องถามเรื่องหายใจ ความดัน และท้องก่อน — ถ้าเข้าเกณฑ์ anaphylaxis ยาตัวแรกคือ IM epinephrine ไม่ใช่ antihistamine")

S1 = sec("derm-03-01", "Urticaria (ลมพิษ) และ anaphylaxis",
    "Type I · wheal & flare หายใน < 24 ชม. ไม่ทิ้งรอย · acute ≤ 6 wk / chronic > 6 wk · R/O anaphylaxis → IM epinephrine · 2nd-gen antihistamine (ปรับได้ 4 เท่า) → omalizumab → cyclosporine",
    minutes=9, source=f"{D} หน้า 81–91", nl=["2.3.12(14)", "B4.2.2(12)", "2.2.7"],
    md='''
### กลไก

- **Type I hypersensitivity** → **mast cell หลั่ง histamine และสาร vasoactive** → หลอดเลือดขยาย รั่ว → บวมใน dermis (wheal) · ถ้าบวมใน dermis ลึก/subcutis = **angioedema**
- สาเหตุ acute: **อาหาร ยา การติดเชื้อ แมลงกัดต่อย** · chronic: หลากหลาย (autoimmune, idiopathic, physical (เสริม))

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| Primary lesion | **wheal & flare** — ผื่นนูนบวมแดง ขอบชัด ตรงกลางซีด อาจเป็นวง (annular) |
| อาการ | **คันมาก**, **กดแล้วจาง (blanchable)** |
| เวลา | **แต่ละวงหายเองใน < 24 ชม.** แล้วย้ายไปขึ้นที่อื่น |
| หลังหาย | **ไม่ทิ้งรอยดำ (no residual hyperpigmentation)** — ถ้าผื่นอยู่ > 24 ชม. ทิ้งรอยช้ำ ให้นึก urticarial vasculitis (เสริม) |
| Angioedema | หน้า เปลือกตา ริมฝีปากบวม |
| อันตราย | **inspiratory stridor** = airway edema |
| Dermographism | ขีดผิวแล้วขึ้นเป็นรอยนูนตามเส้น (symptomatic dermographism) |

### Acute vs chronic

- **Acute ≤ 6 สัปดาห์** — มัก self-limited **อาจไม่ต้องหาสาเหตุ**
- **Chronic > 6 สัปดาห์** (ขึ้น **≥ 2 ครั้ง/สัปดาห์**) — **ต้องหาสาเหตุ** (เช่น autoimmune: SLE, thyroid (เสริม))

### Acute urticaria management

[[fig:derm-03-01-f1]]

- **R/O anaphylaxis!** → airway, IV fluid, **IM epinephrine (1:1,000) ผู้ใหญ่ 0.3–0.5 mg · เด็ก 0.01 mg/kg**
- **2nd-generation antihistamine** (cetirizine, loratadine, fexofenadine)
- **เพิ่ม prednisolone ใน severe urticaria** · เลี่ยง trigger

### Chronic urticaria management (สไลด์หน้า 85)

1. รักษาสาเหตุ/เลี่ยง trigger
2. **Step 1: 2nd-gen antihistamine** — **ปรับเพิ่มได้ถึง 4 เท่า** ของขนาดปกติ
3. **Step 2: + omalizumab** (anti-IgE)
4. **Step 3: + cyclosporine**
- **Prednisolone ระยะสั้น** เฉพาะ severe exacerbation

> Hydroxyzine/chlorpheniramine เป็น 1st-gen (ง่วง) ใช้ได้แต่ไม่ใช่ตัวแรก (เสริม) — ถ้าตัวเลือกมีแค่ epinephrine / hydroxyzine / steroid ในลมพิษธรรมดาที่ไม่มี anaphylaxis ให้เลือก **antihistamine**
''',
    figs=[F_ANA],
    pearls=[
        "Wheal & flare คัน กดจาง หายใน < 24 ชม. ไม่ทิ้งรอย = urticaria",
        "Acute ≤ 6 wk ไม่ต้องหาสาเหตุ · chronic > 6 wk ต้องหาสาเหตุ",
        "Anaphylaxis → IM epinephrine 1:1,000 ผู้ใหญ่ 0.3–0.5 mg, เด็ก 0.01 mg/kg",
        "Chronic: 2nd-gen AH (ขึ้นได้ 4 เท่า) → + omalizumab → + cyclosporine",
    ],
    items=[
        mcq("DERM-03-01-1", """A 4-year-old boy ate seafood 4 hours ago and then developed itchy raised lesions all over his body. Examination shows multiple erythematous edematous plaques and papules with pale centers that blanch on pressure. Individual lesions disappear within hours and reappear elsewhere. Vital signs are normal and the lungs are clear. What is the most likely diagnosis?""",
            "Acute urticaria", ["Atopic dermatitis", "Allergic contact dermatitis", "Erythema multiforme", "Fixed drug eruption"],
            explain="""ผื่นนูนบวมแดงคัน กดจาง **แต่ละวงหายในไม่กี่ชั่วโมงแล้วย้ายที่** หลังกินอาหารทะเล = **acute urticaria** (สไลด์หน้า 81, 86–87)
- Atopic dermatitis เป็นผื่น eczema เรื้อรังที่ข้อพับ/แก้ม ไม่ขึ้นแล้วหายเป็นชั่วโมง
- ACD ต้องมีการสัมผัสทางผิว และผื่นเป็น eczema อยู่หลายวัน
- Erythema multiforme เป็น target lesion ที่อยู่คงที่หลายวัน ตรงกลางคล้ำ ไม่หายในชั่วโมง
- Fixed drug eruption ต้องมีประวัติยาและผื่นกลมสีม่วงอยู่ที่เดิม""",
            pearl="Wheal ย้ายที่ หายใน < 24 ชม. = urticaria",
            topic="Acute urticaria", ref=[f"{D} หน้า 86–87"], nl=["2.3.12(14)"], kind="old", src=OLD),
        mcq("DERM-03-01-2", """A 28-year-old woman has itchy wheals that keep migrating; currently they are on her trunk. They started yesterday after a viral illness. She has no lip or tongue swelling, no dyspnea, no abdominal pain, and her blood pressure is 118/72 mmHg. What is the most appropriate management?""",
            "Oral cetirizine", ["Intramuscular epinephrine", "Intravenous hydrocortisone", "Oral montelukast", "Skin biopsy before treatment"],
            explain="""ลมพิษเฉียบพลันที่ **ไม่มีลักษณะ anaphylaxis** (หายใจปกติ BP ปกติ ไม่มีอาการ GI) → **2nd-gen antihistamine** เช่น cetirizine (สไลด์หน้า 84, 88–89) · ในสไลด์ตัวเลือกคือ epinephrine/hydroxyzine/steroid ซึ่งคำตอบคือ antihistamine เช่นกัน
- IM epinephrine สงวนไว้สำหรับ anaphylaxis ซึ่งรายนี้ไม่เข้าเกณฑ์
- IV hydrocortisone เกินจำเป็น prednisolone จะเพิ่มเฉพาะลมพิษรุนแรง
- Montelukast ไม่ใช่ยาหลักของ acute urticaria
- ลมพิษวินิจฉัยทางคลินิก ไม่ต้อง biopsy""",
            pearl="Urticaria ไม่มี anaphylaxis → 2nd-gen antihistamine",
            topic="Acute urticaria tx", ref=[f"{D} หน้า 84, 88–89"], nl=["2.3.12(14)"], kind="old", src=OLD),
        mcq("DERM-03-01-3", """A 25-year-old man develops generalized wheals, lip swelling and hoarseness 10 minutes after a wasp sting. He has inspiratory stridor and wheezing. BP is 84/50 mmHg, pulse 128/min. Weight 70 kg. What is the most appropriate first drug?""",
            "Epinephrine 1:1,000 0.5 mg intramuscularly into the anterolateral thigh", ["Chlorpheniramine 10 mg intravenously", "Hydrocortisone 200 mg intravenously", "Epinephrine 1:1,000 0.5 mg subcutaneously into the deltoid", "Nebulized salbutamol"],
            explain="""ผื่นลมพิษ + stridor/wheeze + BP ต่ำ หลังแมลงต่อย = **anaphylaxis** → ยาตัวแรกคือ **IM epinephrine 1:1,000 ขนาด 0.3–0.5 mg ในผู้ใหญ่** ฉีดที่ต้นขาด้านนอก (สไลด์หน้า 84; ตำแหน่งฉีด (เสริม))
- Chlorpheniramine ลดคันแต่ไม่แก้ airway edema และ shock — เป็นยาเสริมหลัง epinephrine
- Hydrocortisone ออกฤทธิ์ช้าเป็นชั่วโมง ไม่ใช่ยากู้ชีพ
- Epinephrine ทาง subcutaneous ดูดซึมช้าและไม่แน่นอนเมื่อเทียบกับ IM
- Salbutamol ช่วยหลอดลมหดเกร็งได้บางส่วน แต่ไม่แก้ shock และกล่องเสียงบวม""",
            pearl="Anaphylaxis → IM epinephrine 0.3–0.5 mg (เด็ก 0.01 mg/kg) ที่ต้นขา",
            topic="Anaphylaxis", ref=[f"{D} หน้า 84"], nl=["2.2.7", "B1.4.11(1)"]),
        mcq("DERM-03-01-4", """A 45-year-old woman with SLE has had itchy rashes on and off for about 6 months, occurring several times per week. Examination shows raised red wheals, some annular, on her back. They blanch, are intensely pruritic and resolve spontaneously within hours without leaving marks. What is the most likely diagnosis?""",
            "Chronic urticaria", ["Acute urticaria", "Urticarial vasculitis", "Subacute cutaneous lupus erythematosus", "Erythema multiforme"],
            explain="""Wheal ที่หายเองไม่ทิ้งรอย เป็นมา **> 6 สัปดาห์ (6 เดือน) ≥ 2 ครั้ง/สัปดาห์** = **chronic urticaria** ซึ่งสัมพันธ์กับโรค autoimmune เช่น SLE (สไลด์หน้า 81, 90–91)
- Acute urticaria คือเป็นไม่เกิน 6 สัปดาห์
- Urticarial vasculitis ผื่นอยู่ > 24 ชม. แสบ/เจ็บมากกว่าคัน และหายแล้วทิ้งรอยช้ำ (เสริม)
- SCLE เป็นผื่นวงแดงขุยบริเวณที่โดนแดด อยู่หลายสัปดาห์ ไม่หายในชั่วโมง
- Erythema multiforme เป็น target lesion อยู่หลายวัน ตรงกลางคล้ำ""",
            pearl="Wheal > 6 wk (≥ 2 ครั้ง/wk) = chronic urticaria → หาสาเหตุ",
            topic="Chronic urticaria", ref=[f"{D} หน้า 90–91"], nl=["2.3.12(14)"], kind="old", src=OLD),
        mcq("DERM-03-01-5", """A 38-year-old man has had chronic spontaneous urticaria for 8 months. Despite taking cetirizine at four times the standard dose daily for 6 weeks, he still has daily wheals that disturb his sleep. Work-up for an underlying cause is unrevealing. What is the most appropriate next step?""",
            "Add omalizumab", ["Long-term daily oral prednisolone", "Switch to a first-generation antihistamine at standard dose", "Add cyclosporine before trying any other agent", "Stop all treatment and reassure"],
            explain="""ลำดับขั้นของ chronic urticaria: **step 1 2nd-gen AH (ปรับได้ถึง 4 เท่า) → step 2 เพิ่ม omalizumab → step 3 เพิ่ม cyclosporine** · รายนี้ล้มเหลวที่ step 1 แล้ว จึงเพิ่ม **omalizumab** (สไลด์หน้า 85)
- Prednisolone ใช้ได้เฉพาะระยะสั้นช่วงกำเริบรุนแรง ใช้ยาวไม่ได้เพราะผลข้างเคียง
- การเปลี่ยนเป็น 1st-gen AH ขนาดปกติอ่อนกว่า 2nd-gen 4 เท่าที่ใช้อยู่ และง่วงมาก
- Cyclosporine เป็น step 3 ใช้เมื่อ omalizumab ไม่ได้ผล
- ผู้ป่วยยังมีอาการทุกวัน การหยุดยาไม่เหมาะ""",
            pearl="Chronic urticaria: 2nd-gen AH ×4 → omalizumab → cyclosporine",
            topic="Chronic urticaria tx", ref=[f"{D} หน้า 85"], nl=["2.3.12(14)"]),
    ])

# ---------------------------------------------------------------- 03-02 ADR overview + MPE + FDE
F_TIME = fig("derm-03-02-f1", "Latency: ผื่นแพ้ยาแต่ละชนิดขึ้นหลังเริ่มยากี่วัน", '''<svg viewBox="0 0 740 330">
 <path d="M140 280H720" class="ln"/>
 <path d="M140 280V30" class="ln"/>
 <text x="140" y="300" text-anchor="middle" class="t3">0</text>
 <text x="263" y="300" text-anchor="middle" class="t3">1 wk</text>
 <text x="387" y="300" text-anchor="middle" class="t3">2 wk</text>
 <text x="510" y="300" text-anchor="middle" class="t3">3 wk</text>
 <text x="633" y="300" text-anchor="middle" class="t3">4 wk</text>
 <text x="430" y="322" text-anchor="middle" class="t2">เวลาหลังเริ่มยาครั้งแรก</text>
 <path d="M263 280V36 M387 280V36 M510 280V36 M633 280V36" class="lnf"/>
 <text x="130" y="56" text-anchor="end" class="tb">Urticaria</text>
 <rect x="140" y="44" width="8" height="18" rx="3" class="c1"/>
 <text x="156" y="58" class="t3">นาที–ชั่วโมง</text>
 <text x="130" y="96" text-anchor="end" class="tb">AGEP</text>
 <rect x="158" y="84" width="53" height="18" rx="4" class="miss"/>
 <text x="220" y="98" class="t3">1–4 วัน</text>
 <text x="130" y="136" text-anchor="end" class="tb">FDE</text>
 <rect x="263" y="124" width="124" height="18" rx="4" class="c2"/>
 <text x="396" y="138" class="t3">1–2 wk</text>
 <text x="130" y="176" text-anchor="end" class="tb">MPE</text>
 <rect x="263" y="164" width="124" height="18" rx="4" class="ac"/>
 <text x="396" y="178" class="t3">7–14 วัน</text>
 <text x="130" y="216" text-anchor="end" class="tb">SJS/TEN</text>
 <rect x="211" y="204" width="422" height="18" rx="4" class="bad"/>
 <text x="422" y="218" text-anchor="middle" class="tw">4–28 วัน</text>
 <text x="130" y="256" text-anchor="end" class="tb">DRESS</text>
 <rect x="387" y="244" width="333" height="18" rx="4" class="badsoft"/>
 <text x="553" y="258" text-anchor="middle" class="t2">2–6 wk (ยาวเลยขอบภาพ)</text>
 <rect x="440" y="40" width="280" height="64" rx="8" class="sunk"/>
 <text x="452" y="62" class="tb">เคยได้ยามาก่อน (re-exposure)</text>
 <text x="452" y="82" class="t3">FDE, SJS/TEN: &lt; 48 ชม. · MPE: 2–5 วัน</text>
 <text x="452" y="98" class="t3">DRESS: เร็วขึ้นได้</text>
</svg>''', "เวลานับจากเริ่มยาตัวใหม่ช่วยชี้ทั้งชนิดของผื่นและยาที่เป็นผู้ร้าย — ยาที่เพิ่งเริ่มเมื่อวานมักไม่ใช่สาเหตุของ DRESS แต่อาจเป็น AGEP")

F_SPEC = fig("derm-03-02-f2", "แยก simple กับ severe cutaneous adverse reaction (SCAR)", '''<svg viewBox="0 0 740 300">
 <rect x="10" y="10" width="300" height="280" rx="10" class="oksoft"/>
 <text x="160" y="36" text-anchor="middle" class="tb">Simple</text>
 <text x="160" y="56" text-anchor="middle" class="t3">มีแค่ผื่น ไม่มีอวัยวะอื่น</text>
 <text x="30" y="96" class="t2">• Maculopapular drug eruption</text>
 <text x="44" y="116" class="t3">คัน ผื่นแดง macule-papule ทั่วตัว</text>
 <text x="30" y="150" class="t2">• Urticaria</text>
 <text x="44" y="170" class="t3">wheal &amp; flare</text>
 <text x="30" y="204" class="t2">• Fixed drug eruption</text>
 <text x="44" y="224" class="t3">วงม่วงคล้ำที่เดิม (เสริม: จัดเป็น simple)</text>
 <rect x="330" y="10" width="400" height="280" rx="10" class="badsoft"/>
 <text x="530" y="36" text-anchor="middle" class="tb">Severe (SCAR) — red flags</text>
 <text x="350" y="66" class="t2">ไข้ · ปวดหัว อ่อนเพลีย ปวดข้อ</text>
 <text x="350" y="90" class="t2">หน้าบวม · ต่อมน้ำเหลืองโต</text>
 <text x="350" y="114" class="t2">ตุ่มน้ำ ผิวหลุดลอก Nikolsky + · ตุ่มหนอง</text>
 <text x="350" y="138" class="t2">mucosa: ปาก ตา อวัยวะเพศ</text>
 <text x="350" y="162" class="t2">Lab: eosinophil/atypical lymph ↑</text>
 <text x="350" y="182" class="t2">AST/ALT/ALP/bilirubin ↑ · Cr ↑</text>
 <rect x="350" y="200" width="170" height="36" rx="8" class="bad"/>
 <text x="435" y="223" text-anchor="middle" class="tw">SJS/TEN</text>
 <rect x="530" y="200" width="90" height="36" rx="8" class="bad"/>
 <text x="575" y="223" text-anchor="middle" class="tw">DRESS</text>
 <rect x="630" y="200" width="90" height="36" rx="8" class="bad"/>
 <text x="675" y="223" text-anchor="middle" class="tw">AGEP</text>
 <rect x="350" y="244" width="370" height="36" rx="8" class="bad"/>
 <text x="535" y="267" text-anchor="middle" class="tw">Exfoliative dermatitis (erythroderma)</text>
</svg>''', "เจอผื่นแพ้ยาให้ไล่ red flag ทางขวา — มีข้อใดข้อหนึ่งคือ SCAR ต้องหยุดยาทันทีและส่งตรวจ lab")

S2 = sec("derm-03-02", "Adverse drug reaction: ภาพรวม, maculopapular eruption, fixed drug eruption",
    "Type A dose-related / type B hypersensitivity · simple vs severe (red flags) · MPE 7–14 วัน (2–5 วันถ้าเคยได้) · FDE วงม่วงคล้ำที่เดิมซ้ำ (< 48 ชม. ถ้าเคยได้) ทิ้งรอยดำ",
    minutes=8, source=f"{D} หน้า 92–102", nl=["B1.7.1(4)", "2.1.50"],
    md='''
### ประเภทของ ADR (สไลด์หน้า 92)

| Type | ลักษณะ | ตัวอย่าง |
|---|---|---|
| **A** | **dose-related, predictable** (ฤทธิ์ยาเกิน) | **เลือดออกจาก warfarin, กดการหายใจจาก opioid** |
| **B** | **not dose-related, unpredictable** | **drug hypersensitivity type I–IV** (ผื่นแพ้ยาส่วนใหญ่) |

- Hypersensitivity (สไลด์หน้า 93 เป็นภาพ — สรุปเสริม): I = IgE (urticaria, anaphylaxis) · II = antibody ต่อเซลล์ (hemolytic anemia) · III = immune complex (serum sickness, vasculitis) · IV = T cell (MPE, FDE, SJS/TEN, DRESS, AGEP)

### Simple vs severe

[[fig:derm-03-02-f2]]

### Latency ของผื่นแพ้ยาแต่ละชนิด

[[fig:derm-03-02-f1]]

### Maculopapular drug eruption (MPE, exanthematous) — พบบ่อยที่สุด

- ยาที่พบบ่อย: **antibiotics, NSAIDs, allopurinol, antiepileptics, anti-TB drugs, antiretrovirals**
- **Onset 7–14 วันหลังเริ่มยา** · **2–5 วันถ้าเคยได้รับยามาก่อน**

| สิ่งที่เห็น | รายละเอียด |
|---|---|
| Primary lesion | **erythematous macules & papules** รวมกันเป็นปื้น (morbilliform) |
| การกระจาย | **generalized** เริ่มลำตัวแล้วลามแขนขา สมมาตร (เสริม) |
| อาการ | **คัน** · ไม่มีไข้สูง ไม่มี mucosa ไม่มีตุ่มน้ำ |

- **Mx: หยุดยา (discontinue culprit drug) + topical steroid** · **oral/IV steroid ถ้าผื่นกว้าง**

### Fixed drug eruption (FDE)

- ยา: **sulfonamide, NSAIDs, antihistamine, pseudoephedrine, antiepileptics** (+ tetracycline (เสริม))
- **Onset 1–2 สัปดาห์** · **< 48 ชม. ถ้าเคยได้รับยามาก่อน** (ในทางปฏิบัติมักขึ้นใน 30 นาที–8 ชม. (เสริม))

| สิ่งที่เห็น | รายละเอียด |
|---|---|
| Primary lesion | **well-defined round/oval red–violaceous (ม่วงคล้ำ) patch/plaque** |
| ตรงกลาง | **± central blister หรือ necrosis** |
| ตำแหน่ง | ริมฝีปาก อวัยวะเพศ มือ เท้า (เสริม) · จำนวน 1 ถึงไม่กี่วง |
| จุดเด่น | **เป็นซ้ำที่ตำแหน่งเดิมเมื่อได้ยาอีก** (+ อาจเพิ่มวงใหม่) |
| หลังหาย | **post-inflammatory hyperpigmentation** — รอยดำเทาคงอยู่นาน |

- **Mx: หยุดยา + topical steroid**

> "ซื้อยาฆ่าเชื้อ/ยาแก้ปวดกินเอง → ผื่นวงแดงคล้ำตรงกลางมี necrosis ที่เดิม" = FDE (ไม่ใช่ EM ซึ่งเป็นหลายวง ที่มือเท้า สัมพันธ์ HSV)
''',
    figs=[F_SPEC, F_TIME],
    pearls=[
        "Type A = dose-related predictable (warfarin bleed) · type B = hypersensitivity",
        "SCAR red flags: ไข้ หน้าบวม LN ตุ่มน้ำ Nikolsky + mucosa eos LFT Cr",
        "MPE 7–14 วัน (2–5 วันถ้าเคยได้) → หยุดยา + topical steroid",
        "FDE: วงม่วงคล้ำ ± blister กลาง ซ้ำที่เดิม ทิ้งรอยดำ · < 48 ชม. ถ้าเคยได้",
    ],
    items=[
        mcq("DERM-03-02-1", """A 25-year-old man bought an antibiotic over the counter for a sore throat. Several days later, he developed a single well-defined, round, dusky violaceous plaque with a central blister and necrosis on his upper lip. He recalls a similar lesion at exactly the same site after a previous course of the same drug, which left a gray-brown mark. What is the most likely diagnosis?""",
            "Fixed drug eruption", ["Erythema multiforme", "Erythema nodosum", "Herpes labialis", "Bullous impetigo"],
            explain="""วงกลมม่วงคล้ำขอบชัด ตรงกลางมีตุ่มน้ำ/necrosis **เป็นซ้ำที่ตำแหน่งเดิมเมื่อได้ยาเดิม** และทิ้งรอยดำ = **fixed drug eruption** (สไลด์หน้า 100–102)
- Erythema multiforme เป็น target lesion หลายวงที่มือเท้าแล้วลามเข้าลำตัว ส่วนใหญ่สัมพันธ์กับ HSV ไม่ได้ขึ้นวงเดียวที่เดิมหลังกินยา
- Erythema nodosum เป็นก้อนแดงเจ็บใต้ผิวที่หน้าแข้งสองข้าง ไม่ใช่ plaque มี necrosis ที่ปาก
- Herpes labialis เป็นกลุ่มตุ่มน้ำเล็กบนพื้นแดง ไม่ใช่วงม่วงคล้ำขอบชัด
- Bullous impetigo เป็นตุ่มน้ำใหญ่ flaccid จากแบคทีเรีย ไม่ซ้ำที่เดิมตามการกินยา""",
            pearl="วงม่วงคล้ำ ± blister กลาง ซ้ำที่เดิมหลังกินยา = FDE",
            topic="FDE", ref=[f"{D} หน้า 100–102"], nl=["B1.7.1(4)"], kind="old", src=OLD),
        mcq("DERM-03-02-2", """A 50-year-old man started allopurinol 10 days ago. He now has an itchy, symmetric, generalized eruption of erythematous macules and papules on the trunk and limbs. He is afebrile, has no facial swelling, lymphadenopathy, mucosal lesions or blisters. CBC, liver and renal function are normal. What is the most appropriate management?""",
            "Stop allopurinol and apply a topical corticosteroid", ["Continue allopurinol and add an oral antihistamine", "Admit to a burn unit for wound care", "Start oral prednisolone 1 mg/kg for 3–6 months", "Switch to febuxostat while continuing allopurinol at a lower dose"],
            explain="""ผื่น macule-papule คันทั่วตัวหลังยา 10 วัน **ไม่มี red flag** (ไข้ หน้าบวม LN mucosa ตุ่มน้ำ lab ผิดปกติ) = **maculopapular drug eruption** → **หยุดยาที่สงสัย + topical steroid** (สไลด์หน้า 99)
- การให้ยาต่อเสี่ยงลุกลามเป็น SCAR โดยเฉพาะ allopurinol ที่เป็นสาเหตุสำคัญของ SJS/TEN และ DRESS
- Burn unit ใช้กับ SJS/TEN ที่ผิวหลุดลอก ซึ่งรายนี้ไม่มี
- Prednisolone 3–6 เดือนเป็นการรักษา DRESS ซึ่งต้องมีไข้ หน้าบวม และอวัยวะภายในผิดปกติ
- การลดขนาด allopurinol ไม่ช่วยเพราะเป็น type B ไม่ขึ้นกับขนาดยา""",
            pearl="MPE ไม่มี red flag → หยุดยา + topical steroid",
            topic="MPE", ref=[f"{D} หน้า 99"], nl=["B1.7.1(4)"]),
        mcq("DERM-03-02-3", """A 68-year-old man taking warfarin for atrial fibrillation starts a course of oral metronidazole and develops gum bleeding and an INR of 7.5. How is this adverse drug reaction best classified?""",
            "Type A reaction: dose-related and predictable", ["Type B reaction: type I hypersensitivity", "Type B reaction: type IV hypersensitivity", "Idiosyncratic reaction unrelated to drug concentration", "Severe cutaneous adverse reaction"],
            explain="""เลือดออกจาก warfarin เป็นผลจาก **ฤทธิ์ยาที่เกิน** (metronidazole ยับยั้งการกำจัด warfarin ทำให้ระดับยาสูงขึ้น (เสริม)) — ตรงกับ **type A: dose-related, predictable** ตัวอย่างในสไลด์ (สไลด์หน้า 92)
- Type I hypersensitivity เป็นปฏิกิริยา IgE เช่น urticaria/anaphylaxis ไม่ใช่เลือดออก
- Type IV hypersensitivity คือผื่นแพ้ยาจาก T cell เช่น MPE, SJS
- Idiosyncratic reaction (type B) ไม่ขึ้นกับขนาดยา แต่เลือดออกนี้ขึ้นกับระดับ warfarin โดยตรง
- SCAR เป็นปฏิกิริยาทางผิวหนังที่รุนแรง ไม่ใช่ภาวะเลือดออก""",
            pearl="ฤทธิ์ยาเกินขนาด (warfarin bleed, opioid resp. depression) = type A",
            topic="ADR type", ref=[f"{D} หน้า 92"], nl=["B1.7.1(4)"]),
    ])

# ---------------------------------------------------------------- 03-03 SJS/TEN
F_BSA = fig("derm-03-03-f1", "SJS–TEN spectrum ตาม % BSA ที่ผิวหลุด", '''<svg viewBox="0 0 740 260">
 <rect x="40" y="60" width="66" height="50" class="misssoft"/>
 <rect x="106" y="60" width="132" height="50" class="miss"/>
 <rect x="238" y="60" width="462" height="50" class="bad"/>
 <path d="M40 60V130 M106 60V130 M238 60V130 M700 60V130" class="ln"/>
 <text x="40" y="146" text-anchor="middle" class="t3">0%</text>
 <text x="106" y="146" text-anchor="middle" class="t2">10%</text>
 <text x="238" y="146" text-anchor="middle" class="t2">30%</text>
 <text x="700" y="146" text-anchor="middle" class="t3">100%</text>
 <text x="73" y="44" text-anchor="middle" class="tb">SJS</text>
 <text x="73" y="90" text-anchor="middle" class="t2">&lt; 10</text>
 <text x="172" y="44" text-anchor="middle" class="tb">Overlap</text>
 <text x="172" y="90" text-anchor="middle" class="tw">10–30</text>
 <text x="469" y="44" text-anchor="middle" class="tb">TEN</text>
 <text x="469" y="90" text-anchor="middle" class="tw">&gt; 30% BSA ผิวหลุดลอก</text>
 <rect x="40" y="170" width="660" height="80" rx="10" class="sunk"/>
 <text x="56" y="194" class="tb">ทุกระดับมีเหมือนกัน:</text>
 <text x="56" y="216" class="t2">mucosa ≥ 2 ตำแหน่ง (ปาก ตา อวัยวะเพศ) · dusky/atypical target · Nikolsky +</text>
 <text x="56" y="238" class="t3">นับเฉพาะพื้นที่ที่ผิว detach/detachable ไม่นับผื่นแดงเฉย ๆ (เสริม)</text>
</svg>''', "โรคเดียวกันต่างกันแค่พื้นที่ผิวที่หลุด — ใช้ฝ่ามือผู้ป่วย ≈ 1% BSA ประเมินคร่าว ๆ")

F_SCORTEN = fig("derm-03-03-f2", "SCORTEN: 7 ข้อ วันแรกที่รับไว้ (เสริม)", '''<svg viewBox="0 0 740 280">
 <rect x="10" y="10" width="380" height="260" rx="10" class="box"/>
 <text x="200" y="34" text-anchor="middle" class="tb">ข้อละ 1 คะแนน</text>
 <text x="30" y="64" class="t2">1. อายุ ≥ 40 ปี</text>
 <text x="30" y="92" class="t2">2. มี malignancy</text>
 <text x="30" y="120" class="t2">3. HR ≥ 120/min</text>
 <text x="30" y="148" class="t2">4. ผิวหลุด &gt; 10% BSA วันแรก</text>
 <text x="30" y="176" class="t2">5. BUN &gt; 28 mg/dL</text>
 <text x="30" y="204" class="t2">6. Glucose &gt; 252 mg/dL</text>
 <text x="30" y="232" class="t2">7. HCO3 &lt; 20 mmol/L</text>
 <path d="M440 240H720" class="ln"/>
 <path d="M440 240V30" class="ln"/>
 <text x="430" y="244" text-anchor="end" class="t3">0</text>
 <text x="430" y="139" text-anchor="end" class="t3">50</text>
 <text x="430" y="44" text-anchor="end" class="t3">100%</text>
 <rect x="455" y="234" width="36" height="6" class="ok"/>
 <rect x="505" y="215" width="36" height="25" class="ok"/>
 <rect x="555" y="166" width="36" height="74" class="miss"/>
 <rect x="605" y="118" width="36" height="122" class="bad"/>
 <rect x="655" y="51" width="36" height="189" class="bad"/>
 <text x="473" y="258" text-anchor="middle" class="t3">0–1</text>
 <text x="523" y="258" text-anchor="middle" class="t3">2</text>
 <text x="573" y="258" text-anchor="middle" class="t3">3</text>
 <text x="623" y="258" text-anchor="middle" class="t3">4</text>
 <text x="673" y="258" text-anchor="middle" class="t3">≥ 5</text>
 <text x="473" y="226" text-anchor="middle" class="t3">3%</text>
 <text x="523" y="208" text-anchor="middle" class="t3">12%</text>
 <text x="573" y="159" text-anchor="middle" class="t3">35%</text>
 <text x="623" y="111" text-anchor="middle" class="t3">58%</text>
 <text x="673" y="44" text-anchor="middle" class="t3">&gt; 90%</text>
 <text x="580" y="276" text-anchor="middle" class="t3">คะแนน SCORTEN → อัตราตาย</text>
</svg>''', "คะแนนยิ่งสูงยิ่งตายมาก — ≥ 3 ควรอยู่ ICU/burn unit (เกณฑ์มาตรฐาน ไม่อยู่ในสไลด์)")

S3 = sec("derm-03-03", "Stevens-Johnson syndrome / toxic epidermal necrolysis (SJS/TEN)",
    "< 10% SJS · 10–30% overlap · > 30% TEN · ยา 4–28 วัน · HLA-B1502 (carbamazepine), B5801 (allopurinol), B5701 (abacavir) · dusky atypical target + Nikolsky + mucosa ≥ 2 · หยุดยา ICU/burn unit",
    minutes=10, source=f"{D} หน้า 103–115", nl=["2.2.49", "B4.2.2(13)", "B1.7.1(4)"],
    md='''
### นิยามตาม % BSA ที่ผิวหลุด

[[fig:derm-03-03-f1]]

### สาเหตุ

- **ยา (พบบ่อยสุด)**, การติดเชื้อ (เช่น Mycoplasma ในเด็ก (เสริม))
- ยาที่พบบ่อย: **allopurinol, NSAIDs, antibiotics (เช่น sulfonamide/cotrimoxazole), nevirapine, antiepileptics**
- **Genetic risk (HLA)**

| HLA | ยา |
|---|---|
| **HLA-B1502** | **carbamazepine, lamotrigine, phenytoin** (ตรวจก่อนให้ carbamazepine ในคนเอเชีย (เสริม)) |
| **HLA-B5801** | **allopurinol** |
| **HLA-B5701** | **abacavir** (hypersensitivity syndrome (เสริม)) |

### Time course

- **Onset 4–28 วัน** หลังเริ่มยา · **< 48 ชม. ถ้าเคยได้รับยามาก่อน**
- **Prodrome 1–3 วัน**: ไข้ อ่อนเพลีย ปวดหัว **ระคายตา เจ็บคอ** (มักถูกคิดว่าเป็นหวัดแล้วได้ยาเพิ่ม)

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| ผื่นแรก | **painful dusky red/purpuric macules, atypical target-like** (วงไม่ครบ 3 ชั้น ตรงกลางคล้ำ) เริ่มที่หน้า-ลำตัว (เสริม) |
| อาการ | **เจ็บ/แสบ** มากกว่าคัน |
| ตุ่มน้ำ | **bullae & sloughing** — ผิวหลุดเป็นแผ่นเหมือนกระดาษเปียก |
| **Nikolsky sign +** | **ใช้มือถูผื่นแล้ว epidermis หลุดลอก** |
| **Mucosa ≥ 2** | **ปาก (hemorrhagic crust ที่ริมฝีปาก), ตา (conjunctivitis), อวัยวะเพศ** |
| Pathology (เสริม) | full-thickness epidermal necrosis — แยกที่ dermo-epidermal junction |

### การรักษา (สไลด์หน้า 107)

1. **หยุดยาที่สงสัยทันที (discontinue culprit drug)** — ปัจจัยสำคัญที่สุดต่อการรอด
2. **Admit ICU / burn unit**
3. **Supportive: IV fluid, pain control, wound care**
4. **Consult ตา (eye), สูตินรีเวช (gyne), urology** — ป้องกันพังผืด ตาบอด ช่องคลอดตีบ
5. **Monitor infection/septic shock และ hypovolemic shock** (เสียน้ำทางผิวเหมือนแผลไหม้)
- ยาที่ใช้ในบางศูนย์ (เสริม): cyclosporine, IVIG · ไม่ให้ antibiotic ป้องกันโดยไม่มีหลักฐานติดเชื้อ

### SCORTEN (เสริม)

[[fig:derm-03-03-f2]]

> SJS vs EM: **EM** = typical target (3 ชั้น) ที่มือเท้า mucosa **1 ที่** Nikolsky **ลบ** สาเหตุหลัก HSV · **SJS** = atypical/dusky target เริ่มที่ลำตัว mucosa **≥ 2** Nikolsky **บวก** สาเหตุหลักยา
''',
    figs=[F_BSA, F_SCORTEN],
    pearls=[
        "SJS < 10% · overlap 10–30% · TEN > 30% BSA",
        "HLA-B1502 carbamazepine/lamotrigine/phenytoin · B5801 allopurinol · B5701 abacavir",
        "Onset 4–28 วัน (< 48 ชม. ถ้าเคยได้) · prodrome ไข้ เจ็บคอ ระคายตา",
        "Dusky atypical target + Nikolsky + + mucosa ≥ 2",
        "หยุดยาทันที → ICU/burn unit → fluid, wound care, consult ตา/gyne/uro",
    ],
    items=[
        mcq("DERM-03-03-1", """A patient has atypical, dusky target-like lesions on the trunk with a positive Nikolsky sign. There are erosions on the oral mucosa, genital mucosa and conjunctivae. Detached skin involves about 6% of body surface area. What is the most likely diagnosis?""",
            "Stevens-Johnson syndrome", ["Erythema multiforme major", "Staphylococcal scalded skin syndrome", "Toxic epidermal necrolysis", "Pemphigus vulgaris"],
            explain="""Atypical target + **Nikolsky +** + **mucosa ≥ 2 ตำแหน่ง** (ปาก อวัยวะเพศ ตา) และผิวหลุด **< 10% BSA** = **Stevens-Johnson syndrome** (สไลด์หน้า 103–104, 108–109)
- EM major มี typical target ที่มือเท้า mucosa มักตำแหน่งเดียว และ Nikolsky ลบ
- SSSS ไม่มี mucosal involvement และไม่มี target lesion
- TEN ต้องมีผิวหลุด > 30% BSA
- Pemphigus vulgaris เป็นโรคเรื้อรังในวัย 50–60 ปี เริ่มจากแผลในปากเรื้อรัง ไม่มี target lesion""",
            pearl="Atypical target + Nikolsky + + mucosa ≥ 2 + < 10% = SJS",
            topic="SJS dx", ref=[f"{D} หน้า 108–109"], nl=["2.2.49"], kind="old", src=OLD),
        mcq("DERM-03-03-2", """A 20-year-old man with epilepsy was recently started on lamotrigine. Three weeks later he has fever and a painful rash all over his body with oral erosions. Examination shows multiple flaccid bullae and sheets of epidermis that slough off easily, involving more than 30% of his body surface area. What is the most likely diagnosis?""",
            "Toxic epidermal necrolysis", ["Stevens-Johnson syndrome", "Erythema multiforme", "Rocky Mountain spotted fever", "Pemphigus vulgaris"],
            explain="""ผิวหลุดลอก **> 30% BSA** + mucosa หลัง lamotrigine (ยากลุ่ม antiepileptic ที่สัมพันธ์กับ HLA-B1502) ใน 3 สัปดาห์ = **toxic epidermal necrolysis** (สไลด์หน้า 103, 112–113)
- SJS ผิวหลุดน้อยกว่า 10%
- EM ไม่มีผิวหลุดเป็นแผ่นกว้าง Nikolsky ลบ และสัมพันธ์ HSV
- Rocky Mountain spotted fever เป็น petechial rash จาก rickettsia เริ่มที่ข้อมือข้อเท้า ไม่มีผิวหลุดลอก
- Pemphigus vulgaris ไม่สัมพันธ์กับยาที่เพิ่งเริ่ม และดำเนินโรคเรื้อรัง""",
            pearl="ผิวหลุด > 30% BSA หลังยา = TEN",
            topic="TEN dx", ref=[f"{D} หน้า 112–113"], nl=["2.2.49"], kind="old", src=OLD),
        mcq("DERM-03-03-3", """A 32-year-old man with AIDS has been taking cotrimoxazole prophylaxis, 2 tablets daily, for 4 weeks in preparation for antiretroviral therapy. Over the past 3 days he has developed erythematous papules with dusky red centers, some with fibrinous tops, and bilateral conjunctivitis. What is the most appropriate management?""",
            "Prompt withdrawal of cotrimoxazole", ["Prompt systemic antibiotics", "Gentle daily dressing of the denuded areas while continuing the drug", "Debridement of the necrotic centers", "Replace cotrimoxazole with dapsone immediately"],
            explain="""ผื่น dusky center + ตาอักเสบสองข้าง หลัง sulfonamide 4 สัปดาห์ = SJS ระยะแรก — การรักษาที่สำคัญที่สุดคือ **หยุดยาที่สงสัยทันที** (สไลด์หน้า 107, 114–115)
- Systemic antibiotic ไม่มีบทบาทถ้ายังไม่มีหลักฐานการติดเชื้อ และอาจเพิ่มยาที่แพ้
- การทำแผลเป็นส่วนของ supportive care แต่ถ้ายังให้ยาต่อ โรคจะลุกลาม
- การ debride กลางผื่นทำให้แผลกว้างขึ้นและติดเชื้อ ไม่ใช่การรักษา SJS
- Dapsone เป็น sulfone ที่อาจแพ้ข้ามกับ sulfonamide และไม่ควรให้ยาใหม่ทันทีระหว่างที่ผื่นกำลังลุกลาม""",
            pearl="SJS/TEN: สิ่งแรก = หยุดยาที่สงสัยทันที",
            topic="SJS mx", ref=[f"{D} หน้า 114–115"], nl=["2.2.49"], kind="old", src=OLD),
        mcq("DERM-03-03-4", """A 35-year-old Thai woman with newly diagnosed trigeminal neuralgia is about to start carbamazepine. Which test should be done before the first dose to reduce the risk of Stevens-Johnson syndrome?""",
            "HLA-B1502 genotyping", ["HLA-B5801 genotyping", "HLA-B5701 genotyping", "HLA-B27 genotyping", "Serum IgE level"],
            explain="""**HLA-B1502** สัมพันธ์กับ SJS/TEN จาก **carbamazepine** (รวมทั้ง lamotrigine, phenytoin) และพบบ่อยในคนเอเชียรวมทั้งคนไทย จึงตรวจก่อนเริ่มยา (สไลด์หน้า 103)
- HLA-B5801 สัมพันธ์กับ allopurinol
- HLA-B5701 สัมพันธ์กับ abacavir hypersensitivity
- HLA-B27 สัมพันธ์กับ spondyloarthritis ไม่ใช่การแพ้ยา
- Serum IgE ไม่ทำนาย type IV hypersensitivity อย่าง SJS""",
            pearl="Carbamazepine → HLA-B1502 · allopurinol → B5801 · abacavir → B5701",
            topic="HLA screening", ref=[f"{D} หน้า 103"], nl=["2.2.49", "B1.7.1(4)"]),
        mcq("DERM-03-03-5", """A 10-year-old boy was given penicillin for a sore throat. He then developed fever and a rash. Now his skin is sloughing off over more than 30% of his body, with oral mucosal and corneal involvement, and the Nikolsky sign is positive. The culprit drug has been stopped. Which complication is the most common cause of death that must be monitored for?""",
            "Sepsis from skin barrier loss", ["Acute myocardial infarction", "Ischemic stroke", "Acute pancreatitis", "Diabetic ketoacidosis"],
            explain="""TEN (> 30% BSA) สูญเสียผิวกั้นเหมือนแผลไหม้ — สไลด์ให้ **monitor infection/septic shock และ hypovolemic shock** · sepsis เป็นสาเหตุตายที่พบบ่อยที่สุด (สไลด์หน้า 107, 110–111; สาเหตุตายอันดับหนึ่ง (เสริม))
- Myocardial infarction ไม่ใช่ภาวะแทรกซ้อนหลักของ TEN ในเด็ก
- Ischemic stroke ไม่เกี่ยวข้องกับกลไกผิวหลุด
- Pancreatitis ไม่ใช่ภาวะแทรกซ้อนที่ต้องเฝ้าระวังหลัก
- DKA ไม่เกี่ยว — ภาวะ hyperglycemia ใน TEN เป็นแค่ตัวชี้ความรุนแรงใน SCORTEN""",
            pearl="TEN: เฝ้าระวัง sepsis และ hypovolemic shock",
            topic="TEN complication", ref=[f"{D} หน้า 107, 110–111"], nl=["2.2.49", "2.2.48"], kind="old", src=OLD),
    ])

# ---------------------------------------------------------------- 03-04 DRESS & AGEP
S4 = sec("derm-03-04", "DRESS และ AGEP",
    "DRESS: AED, sulfa, allopurinol, nevirapine, abacavir · 2–6 wk · ไข้ หน้าบวม LN ผื่น MP + eos/atypical lymph + ตับ ไต → prednisolone 3–6 เดือน · AGEP: ATB, omeprazole, CCB · 1–4 วัน · ตุ่มหนองเล็กที่ซอกพับ → ทั่วตัว + neutrophil",
    minutes=7, source=f"{D} หน้า 116–117", nl=["B1.7.1(4)", "2.1.50"],
    md='''
### DRESS (Drug reaction with eosinophilia and systemic symptoms)

- ยา: **antiepileptics (aromatic: carbamazepine, phenytoin, phenobarbital), sulfonamides, allopurinol, nevirapine, abacavir**
- **Onset 2–6 สัปดาห์** หลังเริ่มยา (ช้าที่สุดในกลุ่ม) · เร็วขึ้นได้ถ้าเคยได้ยา

| หัวข้อ | สิ่งที่เห็น |
|---|---|
| อาการทั่วไป | **ไข้, หน้าบวม (facial swelling), ต่อมน้ำเหลืองโต** |
| ผื่น | **generalized erythematous maculopapular rash** (บางรายลามเป็น erythroderma) |
| อวัยวะ | ตับอักเสบ (บ่อยสุด) ไตอักเสบ ปอด หัวใจ (เสริม) |
| Lab | **eosinophil ↑ / atypical lymphocyte ↑**, **AST/ALT/ALP/bilirubin ↑**, **Cr ↑** |

- **Mx: หยุดยา + prednisolone 3–6 เดือน (ค่อย ๆ ลด) + topical steroid**
- ภาวะแทรกซ้อนระยะยาว: autoimmune thyroiditis, T1DM (เสริม)

### AGEP (Acute generalized exanthematous pustulosis)

- ยา: **antibiotics (β-lactam, macrolide), omeprazole, CCB (diltiazem)**
- **Onset 1–4 วัน** หลังเริ่มยา (เร็วที่สุด)

| หัวข้อ | สิ่งที่เห็น |
|---|---|
| ผื่น | **ตุ่มหนองเล็ก ๆ ผิวตื้น (non-follicular, sterile) หลายร้อยตุ่มบนพื้นแดงบวม** |
| ตำแหน่ง | **เริ่มที่ซอกพับ (intertriginous)** → ลามทั่วตัว |
| อาการ | **ไข้, ต่อมน้ำเหลืองโต** |
| Lab | **neutrophil ↑**, AST/ALT ↑, Cr ↑ |
| หลังหาย | ลอกเป็นขุยใน ~ 2 สัปดาห์ (เสริม) |

- **Mx: หยุดยา + topical/oral steroid** · หายเร็วหลังหยุดยา

| | MPE | DRESS | AGEP | SJS/TEN |
|---|---|---|---|---|
| Latency | 7–14 วัน | **2–6 wk** | **1–4 วัน** | 4–28 วัน |
| ผื่น | MP คัน | MP + **หน้าบวม** | **ตุ่มหนองเล็ก** | dusky target, ตุ่มน้ำ ผิวหลุด |
| Mucosa | ไม่มี | น้อย | น้อย | **≥ 2** |
| Lab | ปกติ | **eos ↑, LFT ↑** | **neutrophil ↑** | — |
| เด่น | — | อวัยวะภายใน | ซอกพับ | Nikolsky + |
''',
    pearls=[
        "DRESS = 2–6 wk, ไข้ หน้าบวม LN ผื่น MP, eos ↑ ตับอักเสบ → prednisolone 3–6 เดือน",
        "ยา DRESS: antiepileptic, sulfonamide, allopurinol, nevirapine, abacavir",
        "AGEP = 1–4 วัน ตุ่มหนองเล็กปลอดเชื้อเริ่มซอกพับ + neutrophilia",
        "ยา AGEP: antibiotic, omeprazole, CCB",
    ],
    items=[
        mcq("DERM-03-04-1", """A 42-year-old man started carbamazepine 4 weeks ago. He now has fever of 39°C, marked facial edema, generalized lymphadenopathy and a widespread erythematous maculopapular rash without blisters or mucosal erosions. Laboratory tests show WBC 15,000/mm3 with 18% eosinophils and atypical lymphocytes, and ALT 420 U/L. What is the most likely diagnosis?""",
            "DRESS", ["Maculopapular drug eruption", "Stevens-Johnson syndrome", "Acute generalized exanthematous pustulosis", "Infectious mononucleosis"],
            explain="""ยา antiepileptic **4 สัปดาห์** + **ไข้ หน้าบวม ต่อมน้ำเหลืองโต ผื่น MP** + **eosinophilia, atypical lymphocyte, ตับอักเสบ** = **DRESS** (สไลด์หน้า 116)
- MPE ไม่มีไข้สูง หน้าบวม หรืออวัยวะภายในผิดปกติ
- SJS ต้องมีตุ่มน้ำ ผิวหลุด และ mucosa ≥ 2 ซึ่งรายนี้ไม่มี
- AGEP เกิดใน 1–4 วัน เป็นตุ่มหนองเล็ก และมี neutrophilia ไม่ใช่ eosinophilia
- Infectious mononucleosis มี atypical lymphocyte ได้ แต่ไม่มี eosinophilia และไม่สัมพันธ์กับการเริ่มยา 4 สัปดาห์ก่อน""",
            pearl="ยา 2–6 wk + ไข้ หน้าบวม LN + eos + ตับ = DRESS",
            topic="DRESS dx", ref=[f"{D} หน้า 116"], nl=["B1.7.1(4)"]),
        mcq("DERM-03-04-2", """A 55-year-old woman develops DRESS 5 weeks after starting allopurinol, with eosinophilia, ALT 380 U/L and creatinine rising from 0.8 to 1.9 mg/dL. Allopurinol has been stopped. What is the most appropriate treatment?""",
            "Systemic prednisolone tapered over 3–6 months plus topical steroid", ["Topical steroid alone", "Rechallenge with a lower dose of allopurinol", "Oral antihistamine and observe", "Intravenous acyclovir"],
            explain="""DRESS ที่มีอวัยวะภายในผิดปกติ (ตับ ไต) → หยุดยา + **prednisolone 3–6 เดือน** (ลดช้า ๆ เพราะลดเร็วแล้วกำเริบ) + topical steroid (สไลด์หน้า 116)
- Topical steroid อย่างเดียวไม่คุมการอักเสบของตับและไต
- การให้ allopurinol ซ้ำแม้ขนาดต่ำทำให้ปฏิกิริยากลับมารุนแรงกว่าเดิม
- Antihistamine ไม่คุมการอักเสบระบบที่เกิดจาก T cell
- Acyclovir ไม่ใช่การรักษามาตรฐาน แม้จะมี HHV-6 reactivation ร่วมใน DRESS (เสริม)""",
            pearl="DRESS → หยุดยา + prednisolone 3–6 เดือน",
            topic="DRESS tx", ref=[f"{D} หน้า 116"], nl=["B1.7.1(4)"]),
        mcq("DERM-03-04-3", """A 60-year-old woman started amoxicillin for sinusitis 2 days ago. She now has fever of 38.6°C and hundreds of tiny, non-follicular, pinhead-sized pustules on an erythematous, edematous base that began in the axillae and groin and have spread to the trunk. There are no mucosal lesions. WBC is 16,000/mm3 with 85% neutrophils. Pustule Gram stain shows no organisms. What is the most likely diagnosis?""",
            "Acute generalized exanthematous pustulosis", ["Generalized pustular psoriasis", "Bacterial folliculitis", "DRESS", "Disseminated candidiasis"],
            explain="""ตุ่มหนองเล็กผิวตื้นปลอดเชื้อจำนวนมาก **เริ่มที่ซอกพับแล้วลามทั่วตัว** + ไข้ + neutrophilia **1–4 วันหลังเริ่ม antibiotic** = **AGEP** (สไลด์หน้า 117)
- Generalized pustular psoriasis หน้าตาคล้ายกัน แต่ผู้ป่วยต้องมีประวัติ psoriasis หรือหยุด steroid ไม่ใช่เริ่มหลัง amoxicillin 2 วัน
- Bacterial folliculitis เป็นตุ่มหนองตามรูขุมขน Gram stain จะพบ cocci
- DRESS เกิด 2–6 สัปดาห์ เป็นผื่น MP กับ eosinophilia ไม่ใช่ตุ่มหนอง
- Disseminated candidiasis เกิดในผู้ป่วยภูมิต่ำ/neutropenia เป็นตุ่มแดงกระจาย ไม่ใช่แผ่นตุ่มหนองที่ซอกพับหลังยา""",
            pearl="ยา 1–4 วัน + ตุ่มหนองเล็กเริ่มซอกพับ + neutrophilia = AGEP",
            topic="AGEP dx", ref=[f"{D} หน้า 117"], nl=["B1.7.1(4)"]),
        mcq("DERM-03-04-4", """Which drug–reaction pairing below best matches the typical latency between the first dose and onset of the cutaneous reaction?""",
            "DRESS appearing 3–4 weeks after starting phenytoin", ["AGEP appearing 3 weeks after starting omeprazole", "Maculopapular drug eruption appearing 6 hours after the first dose of amoxicillin in a drug-naive patient", "Stevens-Johnson syndrome appearing 3 months after starting allopurinol", "Fixed drug eruption appearing 8 weeks after first exposure to a sulfonamide"],
            explain="""**DRESS เกิด 2–6 สัปดาห์** หลังเริ่มยา ซึ่ง phenytoin (antiepileptic) เป็นสาเหตุที่พบบ่อย — 3–4 สัปดาห์จึงตรงที่สุด (สไลด์หน้า 99–104, 116–117)
- AGEP เกิดเร็วใน 1–4 วัน ไม่ใช่ 3 สัปดาห์
- MPE ในคนที่ไม่เคยได้ยาเกิด 7–14 วัน ถ้าขึ้นใน 6 ชั่วโมงให้นึกถึง urticaria มากกว่า
- SJS เกิด 4–28 วัน ถ้าผ่านไป 3 เดือนแล้วโอกาสที่ยาตัวนั้นเป็นสาเหตุต่ำมาก
- FDE ครั้งแรกเกิด 1–2 สัปดาห์ ไม่ใช่ 8 สัปดาห์""",
            pearl="AGEP 1–4 d · FDE 1–2 wk · MPE 7–14 d · SJS 4–28 d · DRESS 2–6 wk",
            topic="Drug latency", ref=[f"{D} หน้า 99–117"], nl=["B1.7.1(4)"]),
    ])

LECTURE = lecture("03", "Urticaria & drug eruptions", subtitle="urticaria · anaphylaxis · MPE · FDE · SJS/TEN · DRESS · AGEP",
    objectives=[
        "วินิจฉัย urticaria แยก acute/chronic และคัดกรอง anaphylaxis พร้อมขนาด epinephrine",
        "ใช้ latency + ลักษณะผื่น + lab แยก MPE, FDE, SJS/TEN, DRESS, AGEP",
        "จำ HLA กับยา (B1502, B5801, B5701) และยาที่เป็นสาเหตุแต่ละกลุ่ม",
        "จัดการ SJS/TEN: หยุดยา, ICU/burn unit, consult ตา/gyne/uro, เฝ้าระวัง sepsis",
    ],
    sections=[S1, S2, S3, S4])
