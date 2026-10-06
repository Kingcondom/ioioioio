from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Dermato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 04-01 Blister approach + EM
F_APPROACH = fig("derm-04-01-f1", "Approach to blistering dermatosis", '''<svg viewBox="0 0 740 330">
 <defs><marker id="derm-04-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="270" y="10" width="200" height="40" rx="10" class="acsoft"/>
 <text x="370" y="35" text-anchor="middle" class="tb">ตุ่มน้ำ (blister)</text>
 <path d="M320 50L180 82" class="ln" marker-end="url(#derm-04-01-a)"/>
 <path d="M420 50L560 82" class="ln" marker-end="url(#derm-04-01-a)"/>
 <rect x="10" y="84" width="330" height="236" rx="10" class="box"/>
 <text x="175" y="108" text-anchor="middle" class="tb">Localized</text>
 <text x="30" y="138" class="t2">• Eczema (acute, dyshidrotic)</text>
 <text x="30" y="162" class="t2">• Herpes simplex · herpes zoster</text>
 <text x="30" y="186" class="t2">• HFMD</text>
 <text x="30" y="210" class="t2">• Bullous impetigo</text>
 <text x="30" y="234" class="t2">• Necrotizing fasciitis (hemorrhagic bullae)</text>
 <text x="30" y="258" class="t2">• Fixed drug eruption</text>
 <text x="30" y="282" class="t2">• Trauma (friction, burn)</text>
 <rect x="360" y="84" width="370" height="236" rx="10" class="badsoft"/>
 <text x="545" y="108" text-anchor="middle" class="tb">Generalized</text>
 <text x="380" y="138" class="t2">• Severe eczema</text>
 <text x="380" y="164" class="tb">• Skin necrosis</text>
 <text x="396" y="184" class="t2">EM · SJS/TEN</text>
 <text x="380" y="210" class="tb">• Autoimmune bullous disease</text>
 <text x="396" y="230" class="t2">flaccid → pemphigus · tense → pemphigoid</text>
 <text x="380" y="256" class="tb">• Infection</text>
 <text x="396" y="276" class="t2">disseminated HSV/HZ · chickenpox</text>
 <text x="396" y="296" class="t2">SSSS</text>
</svg>''', "ตุ่มน้ำเฉพาะที่มักเป็นโรคติดเชื้อหรือ eczema · ตุ่มน้ำทั่วตัวให้คิดสามกลุ่ม: ผิวตาย (EM, SJS/TEN), autoimmune และติดเชื้อ")

F_TARGET = fig("derm-04-01-f2", "Typical target (EM) vs atypical target (SJS/TEN)", '''<svg viewBox="0 0 740 260">
 <circle cx="140" cy="110" r="70" class="badsoft"/>
 <circle cx="140" cy="110" r="46" class="sunk"/>
 <circle cx="140" cy="110" r="24" class="c2"/>
 <circle cx="140" cy="110" r="10" class="c2soft"/>
 <text x="140" y="206" text-anchor="middle" class="tb">Typical target (EM)</text>
 <text x="140" y="226" text-anchor="middle" class="t3">3 วงชัด: กลางคล้ำ/ตุ่มน้ำ · วงซีดบวม · ขอบแดง</text>
 <text x="140" y="244" text-anchor="middle" class="t3">กลม ขอบชัด ที่มือ เท้า (acral)</text>
 <path d="M500 60C560 40 620 70 610 120C600 170 540 170 500 160C450 150 440 80 500 60Z" class="badsoft"/>
 <path d="M510 90C540 80 570 100 560 120C550 140 520 140 510 130C495 120 495 95 510 90Z" class="c2"/>
 <text x="530" y="206" text-anchor="middle" class="tb">Atypical (dusky) target (SJS/TEN)</text>
 <text x="530" y="226" text-anchor="middle" class="t3">2 วง ขอบไม่ชัด รูปร่างไม่กลม กลางม่วงคล้ำ</text>
 <text x="530" y="244" text-anchor="middle" class="t3">เริ่มที่ลำตัว รวมกันเป็นปื้น เจ็บ</text>
 <text x="660" y="70" class="t3">ผิวหลุดได้</text>
 <text x="660" y="88" class="t3">(Nikolsky +)</text>
</svg>''', "EM เป็นวงกลมสามชั้นชัดที่มือเท้า · SJS เป็นปื้นคล้ำรูปร่างไม่แน่นอนบนลำตัวที่ถูแล้วผิวหลุด")

S1 = sec("derm-04-01", "Approach to blisters และ erythema multiforme (EM)",
    "Blister localized vs generalized · EM: HSV (บ่อยสุด), mycoplasma, ยา · typical target ที่มือเท้า → ลำตัว · mucosa 1 ที่ · Nikolsky ลบ · recurrent HSV-EM → acyclovir/valacyclovir 6 เดือน",
    minutes=8, source=f"{D} หน้า 118–127", nl=["2.3.12-3(5)", "B4.2.2-3(7)", "2.1.50"],
    md='''
### Approach to blistering dermatosis (สไลด์หน้า 118–119)

[[fig:derm-04-01-f1]]

- **ตุ่มน้ำ flaccid (เหี่ยว แตกง่าย)** = รอยแยกอยู่ **ใน epidermis** (pemphigus, bullous impetigo, SSSS)
- **ตุ่มน้ำ tense (ตึง แตกยาก)** = รอยแยกอยู่ **ใต้ epidermis** (pemphigoid)

### Erythema multiforme (EM)

**สาเหตุ** (สไลด์หน้า 120)
- **HSV (พบบ่อยสุด)** — มักขึ้น 1–3 สัปดาห์หลังเริมที่ริมฝีปาก (เสริม)
- **Mycoplasma pneumoniae**
- **ยา (NSAIDs, sulfonamides, antiepileptics)**
- Autoimmune (เช่น SLE) · idiopathic

**สิ่งที่เห็น**

| หัวข้อ | รายละเอียด |
|---|---|
| Primary lesion | **target lesion (dusky center)** — วงกลมสามชั้น |
| การกระจาย | **เริ่มที่มือเท้า (ฝ่ามือ หลังมือ) → ลามเข้าลำตัว** · สองข้างสมมาตร |
| Mucosa | **1 ตำแหน่ง** (มักเป็นปาก — แผลถลอกที่ริมฝีปาก) |
| **Nikolsky** | **ลบ** |
| EM major | **extensive target + blister** + mucosa (ยังไม่มีผิวหลุดเป็นแผ่นแบบ SJS) |
| EM minor | target ที่ผิว ไม่มี/มี mucosa เล็กน้อย |

[[fig:derm-04-01-f2]]

**การรักษา** (สไลด์หน้า 121)
- **รักษาสาเหตุ**: HSV → **acyclovir** · ยา → **หยุดยา**
- **EM minor**: มัก **หายเอง** → supportive (**topical steroid, antihistamine**)
- **EM major**: **systemic steroid**
- **Recurrent EM (HSV-associated)** → **acyclovir/valacyclovir prophylaxis 6 เดือน**

| | EM | SJS |
|---|---|---|
| สาเหตุหลัก | **HSV** | **ยา** |
| Target | typical 3 ชั้น นูน | atypical/dusky แบน |
| ตำแหน่งเริ่ม | **มือ เท้า (acral)** | **ลำตัว หน้า** |
| Mucosa | 1 ที่ | **≥ 2 ที่** |
| Nikolsky | **ลบ** | **บวก** |
| ผิวหลุด | ไม่มี (< 10% ของตุ่มน้ำ) | มี |
''',
    figs=[F_APPROACH, F_TARGET],
    pearls=[
        "EM สาเหตุบ่อยสุด = HSV · รองลงมา mycoplasma และยา",
        "Typical target ที่มือเท้า + mucosa 1 ที่ + Nikolsky ลบ = EM",
        "Recurrent HSV-EM → acyclovir/valacyclovir prophylaxis 6 เดือน",
        "Flaccid = แยกใน epidermis · tense = แยกใต้ epidermis",
    ],
    items=[
        mcq("DERM-04-01-1", """A 17-year-old boy has had erosions on his lips and a rash on his trunk and palms for 1 week. He has had similar episodes repeatedly in the past, each preceded by a cold sore. Examination shows multiple erosions on the lips and round target lesions with three concentric zones on the palms and trunk. The Nikolsky sign is negative and the eyes and genitalia are normal. What is the most likely diagnosis?""",
            "Erythema multiforme", ["Stevens-Johnson syndrome", "Herpes simplex virus infection", "Urticarial vasculitis", "Fixed drug eruption"],
            explain="""Typical target ที่ **ฝ่ามือ** และลำตัว + แผลที่ริมฝีปาก (mucosa **1 ที่**) + Nikolsky ลบ + เป็นซ้ำหลังเริม = **erythema multiforme (HSV-associated)** (สไลด์หน้า 120, 124–125)
- SJS ต้องมี atypical/dusky target, Nikolsky บวก และ mucosa ≥ 2 ตำแหน่ง
- HSV infection เองเป็นกลุ่มตุ่มน้ำที่ริมฝีปาก แต่ไม่อธิบาย target lesion ที่ฝ่ามือ ซึ่งเป็นปฏิกิริยาภูมิต่อ HSV
- Urticarial vasculitis เป็นผื่นนูนแบบลมพิษที่อยู่ > 24 ชม. ทิ้งรอยช้ำ ไม่ใช่ target lesion
- Fixed drug eruption เป็นวงม่วงคล้ำไม่กี่วงที่เดิมหลังกินยา ไม่ใช่ target หลายวงตามมือ""",
            pearl="Target ที่มือ + แผลปาก + เป็นซ้ำหลังเริม = HSV-associated EM",
            topic="EM dx", ref=[f"{D} หน้า 124–125"], nl=["2.3.12-3(5)"], kind="old", src=OLD),
        mcq("DERM-04-01-2", """A 22-year-old woman developed target-shaped lesions on her palms and soles. She has taken an over-the-counter NSAID for dysmenorrhea for the past week. She has no fever, mucosal lesions or genital ulcers. Which diagnosis best explains her rash?""",
            "Erythema multiforme triggered by a drug", ["Acute HIV infection", "Secondary syphilis", "Rocky Mountain spotted fever", "Hand, foot and mouth disease"],
            explain="""ผื่น **target lesion** ที่ฝ่ามือฝ่าเท้าหลังกินยา NSAID = **erythema multiforme** ที่มียาเป็นสาเหตุ (NSAID, sulfonamide, antiepileptic) (สไลด์หน้า 120, 126–127) · ตัวเลือกในสไลด์คือ acute HIV, secondary syphilis, drug eruption — คำตอบคือผื่นจากยาแบบ EM
- Acute HIV ทำให้เกิดผื่น MP ร่วมกับไข้ เจ็บคอ ต่อมน้ำเหลืองโต ไม่ใช่ target
- Secondary syphilis มีผื่นที่ฝ่ามือฝ่าเท้าจริง แต่เป็น macule สีน้ำตาลแดงขุย ไม่ใช่ target สามชั้น
- Rocky Mountain spotted fever เป็น petechiae เริ่มที่ข้อมือข้อเท้าพร้อมไข้สูง
- HFMD เป็น vesicle รูปรีที่ฝ่ามือฝ่าเท้าในเด็กเล็กพร้อมแผลในปาก""",
            pearl="Target ที่ฝ่ามือฝ่าเท้าหลังกินยา → EM จากยา",
            topic="EM cause", ref=[f"{D} หน้า 126–127"], nl=["2.3.12-3(5)"], kind="old", src=OLD),
        mcq("DERM-04-01-3", """A 28-year-old man has had five episodes of erythema multiforme in the past year, each occurring about 10 days after an outbreak of herpes labialis. He is currently lesion-free. What is the most appropriate management to prevent further episodes?""",
            "Continuous oral valacyclovir (or acyclovir) prophylaxis for 6 months", ["Long-term oral prednisolone", "Topical acyclovir cream at the start of each cold sore", "Oral antihistamine daily", "Avoid all NSAIDs"],
            explain="""**Recurrent EM ที่สัมพันธ์กับ HSV** → **acyclovir/valacyclovir prophylaxis 6 เดือน** เพื่อกด HSV reactivation ซึ่งเป็นตัวกระตุ้น (สไลด์หน้า 121)
- Prednisolone ระยะยาวมีผลข้างเคียงมาก และไม่ป้องกัน HSV (อาจทำให้เริมกำเริบบ่อยขึ้น)
- Acyclovir cream ไม่แนะนำ และไม่ป้องกัน EM ได้
- Antihistamine ลดคันในช่วงเป็นผื่น แต่ไม่ป้องกันการเกิดซ้ำ
- สาเหตุของรายนี้คือ HSV ไม่ใช่ NSAID การเลี่ยง NSAID จึงไม่ตรงเหตุ""",
            pearl="Recurrent HSV-EM → oral antiviral prophylaxis 6 เดือน",
            topic="EM prophylaxis", ref=[f"{D} หน้า 121"], nl=["2.3.12-3(5)", "2.3.1(8)"]),
        mcq("DERM-04-01-4", """A 9-year-old boy has had cough and low-grade fever for 10 days. Chest X-ray shows patchy bilateral infiltrates and cold agglutinins are positive. He now has target lesions on his hands and feet and erosions on the lips only; the Nikolsky sign is negative. Which organism is the most likely trigger?""",
            "Mycoplasma pneumoniae", ["Streptococcus pyogenes", "Staphylococcus aureus", "Parvovirus B19", "Coxsackievirus A16"],
            explain="""Atypical pneumonia ในเด็ก + cold agglutinin บวก + target lesion ที่มือเท้า = EM ที่มี **Mycoplasma pneumoniae** เป็นตัวกระตุ้น (สาเหตุอันดับสองรองจาก HSV) (สไลด์หน้า 120)
- S. pyogenes ทำให้เกิด scarlet fever (ผื่นกระดาษทราย) ไม่ใช่ target lesion
- S. aureus ทำให้เกิด impetigo/SSSS ไม่ใช่ EM หลังปอดอักเสบ
- Parvovirus B19 ทำให้เกิด slapped cheek และผื่นลายลูกไม้
- Coxsackie A16 ทำให้เกิด HFMD ซึ่งเป็น vesicle ที่ฝ่ามือฝ่าเท้าและในปาก ไม่ใช่ target สามชั้น""",
            pearl="Atypical pneumonia + target lesion = Mycoplasma-associated EM",
            topic="EM cause", ref=[f"{D} หน้า 120"], nl=["2.3.12-3(5)"]),
    ])

# ---------------------------------------------------------------- 04-02 AIBD
F_LAYER = fig("derm-04-02-f1", "ระดับรอยแยกในผิวหนัง: pemphigus vs pemphigoid (และโรคอื่นที่ต้องรู้)", '''<svg viewBox="0 0 740 400">
 <rect x="20" y="40" width="330" height="22" class="misssoft"/>
 <text x="26" y="34" class="t3">stratum corneum</text>
 <rect x="20" y="62" width="330" height="100" class="c1soft"/>
 <text x="26" y="80" class="t3">epidermis (keratinocyte ยึดกันด้วย desmosome)</text>
 <path d="M20 162H350" class="lnc2"/>
 <text x="26" y="178" class="t3">basement membrane (hemidesmosome)</text>
 <rect x="20" y="186" width="330" height="110" class="sunk"/>
 <text x="26" y="210" class="t3">dermis</text>
 <text x="185" y="22" text-anchor="middle" class="tb">Pemphigus vulgaris</text>
 <path d="M90 140C100 100 270 100 280 140Z" class="c1"/>
 <path d="M90 140H280" class="ln"/>
 <text x="185" y="132" text-anchor="middle" class="tw">ตุ่มน้ำ</text>
 <rect x="90" y="140" width="190" height="22" class="c1soft"/>
 <text x="185" y="156" text-anchor="middle" class="t3">basal cell ค้างที่พื้น (tombstone)</text>
 <text x="40" y="320" class="tb">Intraepidermal (suprabasal)</text>
 <text x="40" y="340" class="t2">anti-desmoglein 3 (± 1) → acantholysis</text>
 <text x="40" y="360" class="t2">หลังคาบาง → flaccid แตกง่าย Nikolsky +</text>
 <text x="40" y="380" class="t3">DIF: IgG รอบเซลล์ (fishnet / reticular)</text>
 <rect x="390" y="40" width="330" height="22" class="misssoft"/>
 <rect x="390" y="62" width="330" height="100" class="c1soft"/>
 <path d="M390 162H720" class="lnc2"/>
 <rect x="390" y="186" width="330" height="110" class="sunk"/>
 <text x="555" y="22" text-anchor="middle" class="tb">Bullous pemphigoid</text>
 <path d="M460 162C470 206 640 206 650 162Z" class="c2"/>
 <text x="555" y="184" text-anchor="middle" class="tw">ตุ่มน้ำ + eosinophil</text>
 <text x="555" y="110" text-anchor="middle" class="t3">epidermis ทั้งชั้น (รวม basal) = หลังคา</text>
 <path d="M555 116V156" class="lnf"/>
 <text x="410" y="320" class="tb">Subepidermal</text>
 <text x="410" y="340" class="t2">anti-hemidesmosome (BP180, BP230)</text>
 <text x="410" y="360" class="t2">หลังคาหนา → tense แตกยาก Nikolsky ลบ</text>
 <text x="410" y="380" class="t3">DIF: linear IgG + C3 ตาม DEJ</text>
</svg>''', "ตุ่มน้ำยิ่งแยกตื้น หลังคายิ่งบางและแตกง่าย — pemphigus แยกใน epidermis (flaccid) ส่วน pemphigoid แยกใต้ epidermis (tense)")

F_LEVELS = fig("derm-04-02-f2", "โรคตุ่มน้ำเรียงตามความลึกของรอยแยก (เสริม)", '''<svg viewBox="0 0 740 270">
 <rect x="20" y="20" width="200" height="26" class="misssoft"/>
 <text x="120" y="38" text-anchor="middle" class="t3">granular / subcorneal</text>
 <rect x="20" y="46" width="200" height="110" class="c1soft"/>
 <text x="120" y="104" text-anchor="middle" class="t3">spinous / suprabasal</text>
 <path d="M20 156H220" class="lnc2"/>
 <rect x="20" y="160" width="200" height="90" class="sunk"/>
 <text x="120" y="210" text-anchor="middle" class="t3">dermis</text>
 <path d="M220 33H300" class="lnf"/>
 <path d="M220 140H300" class="lnf"/>
 <path d="M220 158H300" class="lnf"/>
 <rect x="300" y="14" width="420" height="40" rx="8" class="misssoft"/>
 <text x="312" y="38" class="t2">SSSS · bullous impetigo · pemphigus foliaceus</text>
 <text x="708" y="38" text-anchor="end" class="t3">ตื้นสุด ผิวลอกบาง</text>
 <rect x="300" y="118" width="420" height="34" rx="8" class="c1soft"/>
 <text x="312" y="140" class="t2">Pemphigus vulgaris (suprabasal)</text>
 <text x="708" y="140" text-anchor="end" class="t3">flaccid</text>
 <rect x="300" y="162" width="420" height="34" rx="8" class="c2soft"/>
 <text x="312" y="184" class="t2">Bullous pemphigoid (subepidermal)</text>
 <text x="708" y="184" text-anchor="end" class="t3">tense</text>
 <rect x="300" y="204" width="420" height="50" rx="8" class="badsoft"/>
 <text x="312" y="224" class="t2">SJS/TEN: epidermis ตายทั้งชั้น หลุดที่ DEJ</text>
 <text x="312" y="244" class="t3">ต่างจาก SSSS ที่ลอกแค่ชั้นบน — biopsy แยกได้</text>
 <path d="M300 229H260V158" class="lnf"/>
</svg>''', "SSSS กับ TEN ดูคล้ายกันแต่ระดับรอยแยกต่าง — SSSS ลอกบางที่ชั้น granular ส่วน TEN epidermis ตายทั้งชั้น")

S2 = sec("derm-04-02", "Autoimmune bullous disease: pemphigus vulgaris vs bullous pemphigoid",
    "PV: anti-desmoglein · intraepidermal · flaccid · Nikolsky + · แผลปากนำ · 50–60 ปี · DIF reticular IgG → prednisolone, rituximab · BP: anti-hemidesmosome · subepidermal · tense คัน · > 60 ปี · DIF linear IgG/C3 → topical steroid",
    minutes=10, source=f"{D} หน้า 128–137", nl=["2.3.12-3(2)", "B4.2.2-3(5)", "B4.1.1(2)"],
    md='''
### กลไกและระดับรอยแยก (สไลด์หน้า 128)

- **Pemphigus vulgaris**: autoantibody ต่อ **desmoglein** (โปรตีนใน desmosome ที่ยึด keratinocyte) → **intraepidermal blister** → **flaccid blister**
- **Bullous pemphigoid**: autoantibody ต่อ **hemidesmosome** (ยึด basal cell กับ basement membrane) → **subepidermal blister** → **tense blister**

[[fig:derm-04-02-f1]]

### เปรียบเทียบ (สไลด์หน้า 130–131)

| | **Pemphigus vulgaris (PV)** | **Bullous pemphigoid (BP)** |
|---|---|---|
| อายุ | **50–60 ปี** | **> 60 ปี** |
| อาการนำ | **แผลในปากเรื้อรังนำมาก่อน** | **คันมาก** ± ผื่นลมพิษนำ (urticarial phase) |
| ตุ่มน้ำ | **flaccid** แตกง่าย → **erosion** กว้าง เจ็บ | **tense bullae** บนผิวปกติหรือพื้นแดง แตกยาก |
| Mucosa | **เกือบทุกราย** | **10–30%** |
| **Nikolsky** | **บวก** | **ลบ** |
| Tzanck smear | **acantholytic cells** | ไม่มี acantholytic cell · เห็น **eosinophil** |
| Biopsy | **intraepidermal blister, acantholysis** | **subepidermal blister, eosinophil** |
| **DIF** | **IgG รอบเซลล์ epidermis (reticular/fishnet)** | **linear IgG & C3 ตาม dermo-epidermal junction** |
| รักษา | **prednisolone, rituximab, wound care** | **topical steroid** (potent) · **prednisolone กรณีรุนแรง** · wound care |

### การตรวจยืนยัน

- **Skin biopsy for histopathology + direct immunofluorescence (DIF)** — เป็นการตรวจมาตรฐานสำหรับ AIBD ทุกชนิด
- Biopsy ตุ่มน้ำใหม่ไปดู histopath · biopsy **ผิวปกติข้างตุ่มน้ำ (perilesional)** ไปทำ DIF (เสริม)
- Tzanck smear ช่วยคัดกรองได้ (acantholysis ใน PV) แต่ไม่ใช่การวินิจฉัยยืนยัน

[[fig:derm-04-02-f2]]

> ผู้สูงอายุ คันมาก ตุ่มน้ำตึงที่ท้องน้อย ต้นขาด้านใน ไม่มีแผลในปาก = BP · วัยกลางคน แผลในปากเรื้อรัง แล้วตามด้วยตุ่มน้ำเหี่ยวแตกง่าย Nikolsky + = PV
''',
    figs=[F_LAYER, F_LEVELS],
    pearls=[
        "PV = anti-desmoglein, intraepidermal, flaccid, Nikolsky +, แผลปากนำ",
        "BP = anti-hemidesmosome, subepidermal, tense คัน, Nikolsky ลบ, > 60 ปี",
        "DIF: PV reticular (fishnet) IgG · BP linear IgG + C3 ที่ DEJ",
        "ยืนยัน AIBD = skin biopsy histopath + DIF",
        "PV → prednisolone ± rituximab · BP → potent topical steroid (pred ถ้ารุนแรง)",
    ],
    items=[
        mcq("DERM-04-02-1", """A 44-year-old woman has had recurrent painful oral erosions for 3 months, followed by multiple flaccid bullae and large erosions on the trunk. The Nikolsky sign is positive. A Tzanck smear from a fresh blister shows acantholytic cells without multinucleated giant cells. What is the most likely diagnosis?""",
            "Pemphigus vulgaris", ["Bullous pemphigoid", "Stevens-Johnson syndrome", "Herpes simplex infection", "Bullous impetigo"],
            explain="""แผลในปากเรื้อรังนำ → **flaccid bullae** + **Nikolsky +** + **acantholytic cells** = **pemphigus vulgaris** (สไลด์หน้า 130, 132–133)
- Bullous pemphigoid เป็นตุ่มน้ำตึง Nikolsky ลบ พบในผู้สูงอายุ และแผลในปากพบน้อย
- SJS เกิดเฉียบพลันหลังยาภายในวันถึงสัปดาห์ มี dusky target ไม่ใช่แผลปากเรื้อรัง 3 เดือน
- HSV infection ใน Tzanck จะเห็น multinucleated giant cell และเป็นกลุ่มตุ่มน้ำเล็ก ไม่ใช่ bulla กว้างทั่วลำตัว
- Bullous impetigo ไม่มีแผลในปากเรื้อรัง และ Gram stain เห็น cocci""",
            pearl="แผลปากเรื้อรัง → flaccid bullae + Nikolsky + + acantholysis = PV",
            topic="PV dx", ref=[f"{D} หน้า 132–133"], nl=["2.3.12-3(2)"], kind="old", src=OLD),
        mcq("DERM-04-02-2", """A 72-year-old man has multiple non-tender, tense, fluid-filled bullae on the lower abdomen and inner thighs, preceded by weeks of intense itching. There are no oral lesions and the Nikolsky sign is negative. A Tzanck smear shows no multinucleated giant cells and no acantholytic cells, but eosinophils are seen. What is the most likely diagnosis?""",
            "Bullous pemphigoid", ["Pemphigus vulgaris", "Toxic epidermal necrolysis", "Pemphigus foliaceus", "Friction blisters"],
            explain="""ผู้สูงอายุ **คันนำ ตุ่มน้ำตึง** ที่ท้องน้อยและต้นขาด้านใน ไม่มีแผลปาก Nikolsky ลบ และเห็น **eosinophil** แต่ไม่มี acantholysis = **bullous pemphigoid** (สไลด์หน้า 131, 134–135)
- Pemphigus vulgaris มี acantholytic cells, Nikolsky บวก และตุ่มเหี่ยวพร้อมแผลในปาก
- TEN เกิดเฉียบพลันหลังยา เจ็บมาก ผิวหลุดเป็นแผ่น Nikolsky บวก
- Pemphigus foliaceus แยกตื้นใต้ stratum corneum ไม่เห็นตุ่มน้ำตึง เห็นแต่สะเก็ดขุยบนหน้าอก หลัง (เสริม)
- Friction blister เกิดตรงจุดที่เสียดสีเช่นเท้า ไม่ได้คันนำเป็นสัปดาห์ และไม่มี eosinophil""",
            pearl="ผู้สูงอายุ คันนำ ตุ่มน้ำตึง Nikolsky ลบ eosinophil = BP",
            topic="BP dx", ref=[f"{D} หน้า 134–135"], nl=["2.3.12-3(2)"], kind="old", src=OLD),
        mcq("DERM-04-02-3", """A 70-year-old woman has tense bullae and vesicles on her trunk without mucosal involvement. What is the most appropriate investigation to confirm the diagnosis?""",
            "Skin biopsy for histopathology and direct immunofluorescence", ["Tzanck smear", "Gram stain of blister fluid", "KOH preparation", "Acid-fast stain"],
            explain="""ตุ่มน้ำตึงในผู้สูงอายุ สงสัย bullous pemphigoid — การ **ยืนยัน autoimmune bullous disease ต้องทำ skin biopsy ดู histopath + direct immunofluorescence** (linear IgG/C3 ตาม DEJ) (สไลด์หน้า 131, 136–137) · ตัวเลือกในสไลด์ไม่มี biopsy และสไลด์เฉลยว่า biopsy for DIF & histopath — ข้อนี้จึงใส่ตัวเลือกนั้นเข้ามาแทน India ink
- Tzanck smear ใช้คัดกรองแค่ acantholysis/giant cell ยืนยัน AIBD ไม่ได้
- Gram stain ใช้เมื่อสงสัย bullous impetigo ในเด็ก ไม่ใช่ตุ่มน้ำตึงในผู้สูงอายุ
- KOH ใช้หาเชื้อรา
- AFB ใช้หาเชื้อ mycobacteria เช่น leprosy ไม่เกี่ยวกับตุ่มน้ำ""",
            pearl="ยืนยัน AIBD = biopsy (histopath + DIF)",
            topic="AIBD investigation", ref=[f"{D} หน้า 136–137"], nl=["2.3.12-3(2)"], kind="old", src=OLD),
        mcq("DERM-04-02-4", """A 55-year-old man has painful oral erosions and flaccid bullae on the scalp and trunk. Skin biopsy shows a suprabasal intraepidermal split with acantholysis. Which direct immunofluorescence pattern is expected?""",
            "Intercellular IgG deposition around keratinocytes in a fishnet (reticular) pattern", ["Linear IgG and C3 along the dermo-epidermal junction", "Granular IgA in the dermal papillae", "Granular IgG and C3 at the dermo-epidermal junction (lupus band)", "Negative immunofluorescence"],
            explain="""Pemphigus vulgaris → antibody ต่อ desmoglein บนผิวเซลล์ keratinocyte จึงเห็น **IgG รอบเซลล์เป็นตาข่าย (reticular/fishnet)** (สไลด์หน้า 130)
- Linear IgG + C3 ตาม DEJ เป็นของ bullous pemphigoid
- Granular IgA ที่ dermal papillae เป็นของ dermatitis herpetiformis (เสริม)
- Lupus band (granular IgG/C3 ที่ DEJ) เป็นของ cutaneous lupus
- DIF ลบไม่เข้ากับ autoimmune bullous disease ที่มี acantholysis ชัดเจน""",
            pearl="DIF: PV = fishnet IgG · BP = linear IgG/C3 ที่ DEJ",
            topic="DIF pattern", ref=[f"{D} หน้า 130–131"], nl=["2.3.12-3(2)", "B4.1.1(2)"]),
        mcq("DERM-04-02-5", """An 80-year-old woman with dementia has biopsy-confirmed bullous pemphigoid limited to the lower legs and lower abdomen (about 8% of body surface area). She has diabetes and osteoporosis. What is the most appropriate first-line treatment?""",
            "Potent topical corticosteroid with wound care", ["High-dose oral prednisolone 1 mg/kg/day", "Intravenous rituximab", "Oral acyclovir", "Oral cloxacillin"],
            explain="""Bullous pemphigoid ระดับเฉพาะที่ → **topical steroid** (potent) + wound care · ให้ prednisolone เฉพาะกรณีรุนแรง (สไลด์หน้า 131) · ผู้สูงอายุที่มีเบาหวาน กระดูกพรุน ยิ่งควรเลี่ยง systemic steroid (เสริม)
- Prednisolone ขนาดสูงในผู้สูงอายุเสี่ยงติดเชื้อ น้ำตาลสูง กระดูกหัก และไม่จำเป็นในโรคเฉพาะที่
- Rituximab เป็นยาที่สไลด์ใช้ใน pemphigus vulgaris ไม่ใช่ first-line ของ BP
- Acyclovir ใช้กับ herpes ไม่เกี่ยวกับโรค autoimmune
- Cloxacillin ใช้รักษาการติดเชื้อ S. aureus ไม่ใช่การรักษา BP""",
            pearl="BP เฉพาะที่ → potent topical steroid · รุนแรง → prednisolone",
            topic="BP tx", ref=[f"{D} หน้า 131"], nl=["2.3.12-3(2)", "B4.4(7)"]),
    ])

LECTURE = lecture("04", "Blistering diseases", subtitle="approach to blister · erythema multiforme · pemphigus vulgaris · bullous pemphigoid",
    objectives=[
        "แยกตุ่มน้ำเฉพาะที่กับทั่วตัว และ flaccid กับ tense ตามระดับรอยแยก",
        "แยก EM กับ SJS ด้วย target, ตำแหน่ง, mucosa และ Nikolsky",
        "แยก PV กับ BP ด้วยอายุ อาการนำ Nikolsky Tzanck biopsy และ DIF",
        "เลือกการรักษา EM (รวม prophylaxis), PV และ BP ตามสไลด์",
    ],
    sections=[S1, S2])
