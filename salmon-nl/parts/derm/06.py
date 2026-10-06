from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Dermato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 06-01 depth figure (shared in sec 3)
F_DEPTH = fig("derm-06-03-f1", "ความลึกของการติดเชื้อแบคทีเรียที่ผิวหนัง", '''<svg viewBox="0 0 740 390">
 <rect x="20" y="30" width="300" height="40" class="c1soft"/>
 <text x="30" y="55" class="t3">epidermis</text>
 <rect x="20" y="70" width="300" height="50" class="misssoft"/>
 <text x="30" y="98" class="t3">superficial dermis</text>
 <rect x="20" y="120" width="300" height="70" class="sunk"/>
 <text x="30" y="160" class="t3">deep dermis</text>
 <rect x="20" y="190" width="300" height="80" class="box"/>
 <text x="30" y="232" class="t3">subcutaneous fat</text>
 <rect x="20" y="270" width="300" height="20" class="c2soft"/>
 <text x="30" y="285" class="t3">fascia</text>
 <rect x="20" y="290" width="300" height="60" class="badsoft"/>
 <text x="30" y="324" class="t3">muscle</text>
 <path d="M320 45H360" class="lnf"/>
 <path d="M320 95H360" class="lnf"/>
 <path d="M320 160H360" class="lnf"/>
 <path d="M320 230H360" class="lnf"/>
 <path d="M320 280H360" class="lnf"/>
 <rect x="360" y="28" width="360" height="34" rx="8" class="box"/>
 <text x="372" y="50" class="t2">Impetigo · folliculitis (รูขุมขนตื้น)</text>
 <rect x="360" y="78" width="360" height="34" rx="8" class="misssoft"/>
 <text x="372" y="100" class="t2">Erysipelas — ขอบชัด นูน S. pyogenes</text>
 <rect x="360" y="143" width="360" height="34" rx="8" class="box"/>
 <text x="372" y="165" class="t2">Cellulitis — ขอบไม่ชัด S. pyogenes + S. aureus</text>
 <rect x="360" y="200" width="360" height="54" rx="8" class="box"/>
 <text x="372" y="222" class="t2">Furuncle/carbuncle/abscess</text>
 <text x="372" y="242" class="t3">ก้อน fluctuant · S. aureus · I&amp;D</text>
 <rect x="360" y="264" width="360" height="54" rx="8" class="bad"/>
 <text x="372" y="286" class="tw">Necrotizing fasciitis</text>
 <text x="372" y="306" class="tw">ปวดเกินสัดส่วน · ผ่าตัดด่วน</text>
 <text x="370" y="378" text-anchor="middle" class="t3">ยิ่งลึก ขอบยิ่งไม่ชัด อาการ systemic ยิ่งมาก และยิ่งต้องผ่าตัด</text>
</svg>''', "ไล่ความลึกจากบนลงล่าง — ขอบผื่นที่ชัดบอกว่าการติดเชื้ออยู่ตื้น (erysipelas) ส่วนปวดมากเกินกว่าที่เห็นบอกว่าลงถึง fascia")

# ---------------------------------------------------------------- 06-01 Impetigo
S1 = sec("derm-06-01", "Impetigo",
    "S. aureus, S. pyogenes · non-bullous = honey-colored crust รอบจมูกปาก · bullous = ตุ่มน้ำใหญ่ flaccid ที่ลำตัว · mild: mupirocin/fusidic · กว้าง: oral dicloxacillin/cephalexin · APSGN",
    minutes=7, source=f"{D} หน้า 182–188", nl=["2.3.12(9)", "B4.2.2(4)"],
    md='''
### เชื้อและการติดต่อ

- **S. aureus, S. pyogenes** · **สัมผัสโดยตรง ติดง่ายมาก** (เด็กเล็ก โรงเรียน)
- มักเกิดบนผิวที่มีรอยแผล/eczema/แมลงกัด (เสริม)

### สิ่งที่เห็น

| ชนิด | ลักษณะ | ตำแหน่ง |
|---|---|---|
| **Non-bullous** (พบบ่อย) | **erythematous papule/plaque → แผลถลอกซึม → honey-colored crust** (สะเก็ดสีน้ำผึ้ง) | **หน้า รอบจมูกและปาก**, แขนขา |
| **Bullous** (S. aureus exfoliative toxin เฉพาะที่ (เสริม)) | **ตุ่มน้ำใหญ่ flaccid** แตกง่าย เหลือขอบเป็นวง (collarette) | **ลำตัว แขน** บริเวณผ้าอ้อม |

### ภาวะแทรกซ้อน

- **APSGN** (จาก S. pyogenes nephritogenic strain — **ATB ไม่ป้องกัน APSGN** (เสริม))
- **SSSS** · **toxic shock syndrome**

### การรักษา (สไลด์หน้า 184)

| ระดับ | การรักษา |
|---|---|
| **Mild (เฉพาะที่)** | **topical ATB (mupirocin, fusidic acid) + wet dressing** (ชะล้างสะเก็ด) |
| **Severe/widespread** | **oral ATB: dicloxacillin, cephalexin, erythromycin, amoxicillin/clavulanate, clindamycin** |

- **Prevention: ล้างมือ ตัดเล็บ**
- **เป็นซ้ำบ่อย → ทา mupirocin ในโพรงจมูก** ลด S. aureus colonization

> Atopic dermatitis ที่มีสะเก็ดสีน้ำผึ้ง = impetiginized eczema → ทา mupirocin ร่วมกับรักษา eczema
''',
    pearls=[
        "Honey-colored crust รอบจมูกปาก = non-bullous impetigo",
        "Bullous impetigo = ตุ่มน้ำใหญ่ flaccid ที่ลำตัว (S. aureus)",
        "Mild → topical mupirocin/fusidic + wet dressing · กว้าง → oral dicloxacillin/cephalexin",
        "เป็นซ้ำ → mupirocin ในโพรงจมูก · ภาวะแทรกซ้อน APSGN, SSSS, TSS",
    ],
    items=[
        mcq("DERM-06-01-1", """A 3-year-old girl has had an itchy rash on her face for 1 day. Examination shows a few vesicles and pustules covered with honey-colored crusts on the chin and around the nostrils. She is afebrile and otherwise well. What is the most likely diagnosis?""",
            "Non-bullous impetigo", ["Herpes simplex infection", "Atopic dermatitis", "Contact dermatitis", "Perioral dermatitis"],
            explain="""ตุ่มน้ำ-ตุ่มหนองที่มี **สะเก็ดสีน้ำผึ้ง (honey-colored crust)** รอบจมูกและคางในเด็กเล็ก = **non-bullous impetigo** (สไลด์หน้า 182, 185–186)
- HSV เป็นกลุ่มตุ่มน้ำใสบนพื้นแดงที่ขอบริมฝีปาก สะเก็ดไม่ได้เป็นสีน้ำผึ้งชัดแบบนี้
- Atopic dermatitis เป็นผื่นเรื้อรังคันที่แก้ม/ข้อพับ ไม่ได้ขึ้นภายใน 1 วันพร้อมสะเก็ดเหลือง
- Contact dermatitis เป็นผื่น eczema ตามรูปของที่สัมผัส
- Perioral dermatitis เป็นตุ่มแดงเล็กรอบปากที่เว้นขอบริมฝีปาก มักสัมพันธ์กับการทา steroid (เสริม)""",
            pearl="Honey-colored crust = impetigo",
            topic="Impetigo dx", ref=[f"{D} หน้า 185–186"], nl=["2.3.12(9)"], kind="old", src=OLD),
        mcq("DERM-06-01-2", """A 5-year-old boy with atopic dermatitis has a facial rash. Examination shows a few erythematous erosions on his cheeks and around the nares, some covered with honey-colored crusts. The lesions cover a small area and he is afebrile. What is the first-line treatment?""",
            "Topical mupirocin", ["Topical hydrocortisone 1%", "Oral trimethoprim-sulfamethoxazole", "Oral penicillin V", "Oral dicloxacillin"],
            explain="""Impetigo **เฉพาะที่ ไม่กว้าง** → **topical ATB (mupirocin หรือ fusidic acid)** เป็น first line (สไลด์หน้า 184, 187–188)
- Hydrocortisone รักษา eczema แต่ไม่ฆ่าเชื้อ ใช้เดี่ยว ๆ แล้ว impetigo จะลาม
- TMP-SMX ไม่ครอบคลุม S. pyogenes ได้ดี และเป็นยาระบบที่ไม่จำเป็น
- Penicillin V ไม่ครอบคลุม S. aureus ที่สร้าง penicillinase
- Dicloxacillin เป็น oral ATB สำหรับ impetigo ที่กว้าง/รุนแรง""",
            pearl="Impetigo เฉพาะที่ → topical mupirocin",
            topic="Impetigo tx", ref=[f"{D} หน้า 187–188"], nl=["2.3.12(9)"], kind="old", src=OLD),
        mcq("DERM-06-01-3", """A 6-year-old boy has widespread honey-crusted erosions on his face, both arms and legs, with several new lesions appearing daily despite 5 days of topical fusidic acid. He has mild fever. What is the most appropriate treatment?""",
            "Oral cephalexin", ["Continue topical fusidic acid for another week", "Topical mometasone", "Oral metronidazole", "Oral acyclovir"],
            explain="""Impetigo ที่ **กว้าง หลายตำแหน่ง** และไม่ตอบสนองต่อยาทา → **oral ATB** ที่ครอบคลุม S. aureus และ S. pyogenes เช่น **cephalexin** หรือ dicloxacillin (สไลด์หน้า 184)
- การใช้ fusidic acid ต่ออย่างเดียวไม่พอเมื่อโรคกว้างและลุกลาม
- Mometasone เป็น steroid ทำให้การติดเชื้อแย่ลง
- Metronidazole ไม่ครอบคลุม staphylococci/streptococci
- Acyclovir ใช้กับไวรัส herpes""",
            pearl="Impetigo กว้าง/ไม่ตอบสนอง → oral dicloxacillin/cephalexin",
            topic="Impetigo severe", ref=[f"{D} หน้า 184"], nl=["2.3.12(9)"]),
        mcq("DERM-06-01-4", """Three weeks after a skin infection with honey-colored crusts on his legs, a 7-year-old boy develops periorbital edema, cola-colored urine and hypertension. Which complication has occurred?""",
            "Acute post-streptococcal glomerulonephritis", ["Acute rheumatic fever", "Staphylococcal scalded skin syndrome", "IgA nephropathy", "Minimal change disease"],
            explain="""Impetigo จาก S. pyogenes ทำให้เกิด **APSGN** (บวมรอบตา ปัสสาวะสีโคล่า ความดันสูง หลังติดเชื้อที่ผิว 3–6 สัปดาห์) (สไลด์หน้า 182)
- Rheumatic fever ตามหลัง streptococcal pharyngitis ไม่ใช่การติดเชื้อที่ผิว (เสริม)
- SSSS เป็นผิวแดงลอกในเด็กจาก toxin ของ S. aureus ไม่ทำให้ไตอักเสบ
- IgA nephropathy มีปัสสาวะเป็นเลือดภายใน 1–2 วันหลังติดเชื้อทางเดินหายใจ ไม่ใช่ 3 สัปดาห์หลัง impetigo
- Minimal change disease เป็น nephrotic syndrome ไม่มีปัสสาวะสีโคล่าและความดันสูง""",
            pearl="Impetigo (strep) → APSGN ได้ แต่ ATB ไม่ป้องกัน",
            topic="Impetigo complication", ref=[f"{D} หน้า 182"], nl=["2.3.12(9)", "B9.2.2(3)"]),
    ])

# ---------------------------------------------------------------- 06-02 Folliculitis, furuncle
S2 = sec("derm-06-02", "Folliculitis, furuncle, carbuncle และ skin abscess",
    "Folliculitis = ตุ่มหนองที่รูขุมขน (S. aureus · hot tub = P. aeruginosa) → topical mupirocin · furuncle = folliculitis ลึก, carbuncle = หลาย furuncle รวมกัน → I&D + oral dicloxacillin (แพ้ penicillin: clindamycin)",
    minutes=6, source=f"{D} หน้า 189–196", nl=["2.3.12(2)", "B4.2.2(2)"],
    md='''
### Folliculitis

- **การอักเสบของรูขุมขน**
- เชื้อ: **S. aureus** (บ่อยสุด) · **P. aeruginosa** เมื่อแช่ **hot tub/น้ำปนเปื้อน** ("hot tub folliculitis")

| สิ่งที่เห็น | รายละเอียด |
|---|---|
| Primary lesion | **papule/pustule เล็กที่มีขนตรงกลาง** (follicular) เจ็บ |
| ตำแหน่ง | ที่มีขน: รักแร้ ขา ก้น เครา |
| อาการ | **คันได้** เจ็บเล็กน้อย |

- **Tx: topical ATB (เช่น mupirocin)**

### Furuncle, carbuncle, skin abscess

- **Furuncle = deep folliculitis** (ฝีที่รูขุมขน)
- **Carbuncle = furuncle หลายอันรวมกัน** (หลายหัว มักที่ต้นคอ หลัง)
- Skin abscess = โพรงหนองใน dermis/subcutis
- เชื้อ: **S. aureus**

| สิ่งที่เห็น | รายละเอียด |
|---|---|
| Primary lesion | **fluctuant red nodule** กดเจ็บ (นุ่ม-หยุ่นเพราะมีหนอง) |
| อาการ | ปวดตุบ ๆ ± ไข้ |

- **Tx: incision & drainage (I&D) + oral ATB**
  - **dicloxacillin**
  - **clindamycin (กรณีแพ้ penicillin)**
  - **amoxicillin/clavulanate**
- เสริม: สงสัย MRSA (community, เป็นซ้ำ) → TMP-SMX, doxycycline, clindamycin

> โจทย์ "เจาะได้หนอง" → **S. aureus** · ผ่าระบายหนองแล้วให้ยา → **dicloxacillin** (ไม่ใช่ penicillin G ซึ่ง S. aureus ดื้อ)
''',
    pearls=[
        "Folliculitis = ตุ่มหนองที่รูขุมขน → topical mupirocin",
        "Hot tub folliculitis = P. aeruginosa",
        "Furuncle/carbuncle/abscess = S. aureus → I&D + oral dicloxacillin",
        "แพ้ penicillin → clindamycin",
    ],
    items=[
        mcq("DERM-06-02-1", """A 35-year-old woman has had itchy, mildly painful pustules in her right axilla for 5 days after shaving. Examination shows multiple small erythematous papules and pustules, each centered on a hair follicle. There is no surrounding cellulitis, abscess or fever. What is the most appropriate treatment?""",
            "Topical mupirocin", ["Oral cephalexin", "Oral ciprofloxacin", "Oral clindamycin", "Topical retinoid"],
            explain="""ตุ่มหนองเล็กที่ **มีรูขุมขนตรงกลาง** หลังโกนขน ไม่มี cellulitis = **superficial folliculitis** → **topical ATB เช่น mupirocin** (สไลด์หน้า 189–191)
- Cephalexin เป็นยาระบบ ใช้เมื่อเป็นกว้าง มี cellulitis หรือฝี
- Ciprofloxacin ใช้เมื่อสงสัย Pseudomonas (hot tub) และไม่ครอบคลุม S. aureus ดีพอ
- Oral clindamycin ใช้ในฝีที่แพ้ penicillin ไม่จำเป็นในโรคตื้นเฉพาะที่
- Topical retinoid ใช้รักษาสิว ไม่ฆ่าเชื้อ""",
            pearl="Folliculitis เฉพาะที่ → topical mupirocin",
            topic="Folliculitis tx", ref=[f"{D} หน้า 189–191"], nl=["2.3.12(2)"], kind="old", src=OLD),
        mcq("DERM-06-02-2", """A 40-year-old Thai woman has pain and swelling of her left upper thigh with fever of 39°C. Examination shows a tender, erythematous, fluctuant nodule. Needle aspiration yields thick pus. What is the most likely causative organism?""",
            "Staphylococcus aureus", ["Streptococcus pyogenes", "Haemophilus influenzae", "Pseudomonas aeruginosa", "Clostridium perfringens"],
            explain="""ก้อนแดงเจ็บ **fluctuant เจาะได้หนอง** = **skin abscess/furuncle** ซึ่งเชื้อหลักคือ **S. aureus** (สไลด์หน้า 192–194)
- S. pyogenes ทำให้เกิด erysipelas/cellulitis ที่ลามแผ่กว้าง ไม่ค่อยเกิดโพรงหนอง
- H. influenzae ไม่ใช่สาเหตุของฝีที่ผิวหนังในผู้ใหญ่
- P. aeruginosa ทำให้เกิด hot tub folliculitis หรือ ecthyma gangrenosum ในผู้ป่วยภูมิต่ำ
- C. perfringens ทำให้เกิด gas gangrene มี crepitus เนื้อตาย ไม่ใช่ฝีหนองข้น""",
            pearl="ฝี เจาะได้หนอง = S. aureus",
            topic="Abscess organism", ref=[f"{D} หน้า 193–194"], nl=["2.3.12(2)"], kind="old", src=OLD),
        mcq("DERM-06-02-3", """A 20-year-old man with ordinary acne has a lesion on his cheek that has not resolved and is more painful than his usual pimples: a 2.5-cm tender, fluctuant, red nodule with a central pustule and surrounding erythema. Incision and drainage is performed. He has no drug allergy. Which antibiotic is most appropriate?""",
            "Oral dicloxacillin", ["Packing the wound only, without antibiotics", "Topical mupirocin", "Intravenous vancomycin", "Penicillin G"],
            explain="""Furuncle/abscess ขนาดใหญ่มี cellulitis รอบ ๆ → **I&D + oral ATB** โดยยาที่สไลด์ให้คือ **dicloxacillin** (แพ้ penicillin ใช้ clindamycin) (สไลด์หน้า 192, 195–196)
- การ packing ไม่ใช่ยาปฏิชีวนะ และฝีที่มีผิวแดงรอบควรให้ยาร่วม
- Mupirocin ทาไม่ถึงชั้นลึกของฝี
- Vancomycin IV สำหรับ MRSA หรือผู้ป่วยรุนแรงใน รพ. ไม่จำเป็นในผู้ป่วยนอก
- Penicillin G ไม่ครอบคลุม S. aureus ส่วนใหญ่ที่สร้าง penicillinase""",
            pearl="Furuncle หลัง I&D → oral dicloxacillin",
            topic="Furuncle tx", ref=[f"{D} หน้า 195–196"], nl=["2.3.12(2)"], kind="old", src=OLD),
    ])

# ---------------------------------------------------------------- 06-03 Erysipelas / cellulitis
S3 = sec("derm-06-03", "Erysipelas และ cellulitis",
    "Erysipelas = superficial dermis, S. pyogenes, ขอบชัดนูน · cellulitis = deep dermis, S. pyogenes + S. aureus, ขอบไม่ชัด · mild: oral dicloxacillin/cephalexin · severe: IV cloxacillin/cefazolin · แผลกดทับ/สัตว์กัด: amox-clav",
    minutes=7, source=f"{D} หน้า 197–202", nl=["2.3.12(4)", "B4.2.2(3)"],
    md='''
### เปรียบเทียบ (สไลด์หน้า 197)

| | **Erysipelas** | **Cellulitis** |
|---|---|---|
| ความลึก | **superficial dermis** + lymphatics (เสริม) | **deep dermis** + subcutaneous fat |
| เชื้อ | **S. pyogenes** | **S. pyogenes, S. aureus** |
| ขอบ | **well-demarcated** ขอบนูนชัด (คลำขอบได้) | **ill-defined** ขอบค่อย ๆ จาง |
| สี | แดงสด มันวาว (เสริม) | แดงชมพู |
| ตำแหน่งที่พบบ่อย (เสริม) | หน้า (แก้ม) ขา | ขา |

[[fig:derm-06-03-f1]]

### สิ่งที่เห็นร่วมกัน

- แดง ร้อน บวม เจ็บ (4 สัญญาณอักเสบ) ข้างเดียว · ± ไข้ · ต่อมน้ำเหลืองอักเสบ
- ประตูเข้า: แผล tinea pedis ระหว่างนิ้วเท้า แมลงกัด (เสริม)
- ต้องแยก **DVT** (compression ultrasound) โดยเฉพาะขาบวมข้างเดียว (เสริม)

### การรักษา (สไลด์หน้า 198)

| ระดับ | ยา |
|---|---|
| **Mild → oral** | **dicloxacillin, cephalexin** · **clindamycin (แพ้ penicillin)** |
| **Severe → IV** | **cloxacillin, cefazolin** · **clindamycin (แพ้ penicillin)** |
| **สงสัย polymicrobial** (แผลกดทับ สัตว์กัด) | **amoxicillin/clavulanate, ampicillin/sulbactam** |

- เสริม: ยกขาสูง วาดขอบผื่นเพื่อติดตาม · รักษา tinea pedis ป้องกันการเป็นซ้ำ

> Red flag ว่าไม่ใช่ cellulitis ธรรมดา: **ปวดเกินสัดส่วน, ลามเร็วเป็นชั่วโมง, ตุ่มน้ำเลือด, ผิวม่วงคล้ำ, crepitus, ชา, shock** → necrotizing fasciitis
''',
    figs=[F_DEPTH],
    pearls=[
        "Erysipelas ขอบชัด ตื้น S. pyogenes · cellulitis ขอบไม่ชัด ลึก strep + staph",
        "Mild: oral dicloxacillin/cephalexin · severe: IV cloxacillin/cefazolin · แพ้ PCN: clindamycin",
        "แผลกดทับ/สัตว์กัด (polymicrobial) → amox-clav หรือ amp-sulbactam",
        "ปวดเกินสัดส่วน ลามเร็ว ตุ่มน้ำเลือด crepitus = นึกถึง NF",
    ],
    items=[
        mcq("DERM-06-03-1", """A 25-year-old man has a swollen, red right calf. Examination shows a poorly demarcated, 10-cm, warm, tender erythematous plaque on the calf without fluctuance. Temperature is 37.9°C; he is otherwise well. Compression ultrasound shows no DVT. What is the most appropriate management?""",
            "Oral cephalexin", ["Heparin", "Incision and drainage", "Intravenous piperacillin-tazobactam", "Intravenous vancomycin"],
            explain="""ผื่นแดงร้อนเจ็บ **ขอบไม่ชัด** ไม่มีหนอง และ US ไม่พบ DVT = **cellulitis ระดับ mild** → **oral dicloxacillin หรือ cephalexin** (สไลด์หน้า 198, 201–202)
- Heparin ใช้รักษา DVT ซึ่ง ultrasound ตัดออกแล้ว
- I&D ใช้เมื่อมีฝี (fluctuant) ซึ่งตรวจไม่พบ
- Piperacillin-tazobactam เป็นยา broad-spectrum สำหรับ NF หรือ polymicrobial รุนแรง เกินจำเป็น
- Vancomycin สำหรับ MRSA หรือผู้ป่วยรุนแรง ไม่ใช่ cellulitis เบาในผู้ป่วยนอก""",
            pearl="Cellulitis mild → oral cephalexin/dicloxacillin",
            topic="Cellulitis tx", ref=[f"{D} หน้า 201–202"], nl=["2.3.12(4)"], kind="old", src=OLD),
        mcq("DERM-06-03-2", """A 62-year-old woman has sudden fever and a bright red, shiny, raised plaque on her left cheek with a sharply demarcated, palpable advancing edge. Which organism is most likely responsible?""",
            "Streptococcus pyogenes", ["Staphylococcus aureus", "Pseudomonas aeruginosa", "Pasteurella multocida", "Vibrio vulnificus"],
            explain="""ผื่นแดงมันนูน **ขอบชัดคลำได้** ที่หน้าพร้อมไข้เฉียบพลัน = **erysipelas** ซึ่งอยู่ใน superficial dermis และเชื้อหลักคือ **S. pyogenes** (สไลด์หน้า 197)
- S. aureus เป็นเชื้อร่วมของ cellulitis (ขอบไม่ชัด) และฝี
- P. aeruginosa ทำให้เกิด ecthyma gangrenosum ในผู้ป่วยภูมิต่ำ หรือ hot tub folliculitis
- Pasteurella ทำให้เกิด cellulitis หลังสุนัขหรือแมวกัด
- Vibrio vulnificus ทำให้เกิด NF/bullae หลังสัมผัสน้ำทะเลหรือกินอาหารทะเล""",
            pearl="ขอบชัดนูน = erysipelas = S. pyogenes",
            topic="Erysipelas", ref=[f"{D} หน้า 197"], nl=["2.3.12(4)"]),
        mcq("DERM-06-03-3", """A 30-year-old man was bitten on the hand by his cat 18 hours ago. The hand is now red, warm, swollen and tender around the puncture wounds, without crepitus or fluctuance. He is afebrile. Which oral antibiotic is most appropriate?""",
            "Amoxicillin-clavulanate", ["Dicloxacillin", "Cephalexin", "Clindamycin alone", "Metronidazole alone"],
            explain="""Cellulitis หลัง **สัตว์กัด** เป็นการติดเชื้อ **polymicrobial** (Pasteurella, anaerobes, staph, strep) → **amoxicillin/clavulanate** (หรือ ampicillin/sulbactam ทาง IV) (สไลด์หน้า 198)
- Dicloxacillin ไม่ครอบคลุม Pasteurella multocida
- Cephalexin ครอบคลุม Pasteurella ได้ไม่ดี
- Clindamycin เดี่ยว ๆ ไม่ครอบคลุม Pasteurella
- Metronidazole ครอบคลุมเฉพาะ anaerobe""",
            pearl="สัตว์กัด/แผลกดทับ → amox-clav",
            topic="Bite cellulitis", ref=[f"{D} หน้า 198"], nl=["2.3.12(4)"]),
    ])

# ---------------------------------------------------------------- 06-04 NF
S4 = sec("derm-06-04", "Necrotizing fasciitis (NF)",
    "Type I polymicrobial (DM, IVDU, alcohol) · II S. pyogenes · III Vibrio · IV fungal · ปวดเกินสัดส่วน → ม่วงคล้ำ bullae crepitus ชา shock · ผ่าตัด explore + debride ด่วน + empirical ATB (vanco + pip/tazo) · strep/C. perfringens → PGS + clindamycin",
    minutes=10, source=f"{D} หน้า 199–200, 203–217", nl=["2.2.50", "B5.2.2(1)", "2.3.12-3(6)"],
    md='''
### นิยาม

ภาวะ **คุกคามชีวิต**: ติดเชื้อลามตามชั้น **fascia** ทำให้เนื้อเยื่อตายกว้าง

### ชนิดตามเชื้อ (สไลด์หน้า 203)

| Type | เชื้อ | กลุ่มเสี่ยง/ประวัติ |
|---|---|---|
| **I (บ่อยสุด)** | **polymicrobial** (aerobe + anaerobe) | **DM, ภูมิต่ำ, alcohol, IVDU**, แผลผ่าตัด perineum (Fournier) (เสริม) |
| **II** | **monomicrobial S. pyogenes** (± S. aureus) | คนแข็งแรง แผลเล็ก ๆ |
| **III** | **Vibrio spp.** | **สัมผัสน้ำทะเล**/อาหารทะเล ตับแข็ง (เสริม) |
| **IV** | **fungal (Candida, Zygomycetes)** | ภูมิต่ำ |
| (gas gangrene) | **Clostridium perfringens** — Gram-positive bacilli | แผลลึกปนดิน ไม้ตำ (เสริม) |

### สิ่งที่เห็น (สไลด์หน้า 205)

| ระยะ | อาการ |
|---|---|
| **Early** | **ไข้, ผื่นแดงกระจาย, ปวดมากเกินสัดส่วน (pain out of proportion)** — ผิวดูไม่แย่เท่าที่ปวด |
| **Later** | **ผิวสีม่วงคล้ำ (purple/dusky), ตุ่มน้ำ (hemorrhagic bullae), crepitus, gangrene/necrosis** |
| | **ชา** (เส้นประสาทถูกทำลาย) |
| Systemic | **sepsis, septic shock**, tachycardia |

### การรักษา (สไลด์หน้า 206–207)

1. **Surgical exploration เพื่อยืนยันและ debridement ทันที** (ห้ามรอผล culture/imaging) — เห็น "dishwater" pus, fascia ซีด ใช้นิ้วแยกได้ง่าย (finger test) (เสริม)
2. ส่ง **G/S, C/S จาก necrotic tissue** + **hemoculture**
3. **Empirical IV ATB** = **คลุม MRSA (vancomycin/linezolid/daptomycin)** **+** หนึ่งใน:
   - **piperacillin/tazobactam**
   - หรือ **carbapenem**
   - หรือ **ceftriaxone + metronidazole**
   - หรือ **fluoroquinolone + metronidazole**
4. **Pathogen-specific**:

| เชื้อ | ยา |
|---|---|
| **S. pyogenes / C. perfringens** | **IV penicillin G + IV clindamycin** (clindamycin ยับยั้งการสร้าง toxin) |
| **MSSA** | **IV cloxacillin / cefazolin** |
| **MRSA** | **IV vancomycin** |

> ไข้สูง + ขาบวมปวดมาก + ผิวม่วงคล้ำ + crepitus หลังแผลเล็ก = NF → **empirical ATB + debridement** ทันที · Gram stain จากตุ่มน้ำเห็น **Gram-positive bacilli (boxcar)** = **C. perfringens** → **PGS + clindamycin**
''',
    pearls=[
        "NF: ปวดเกินสัดส่วน → ม่วงคล้ำ ตุ่มน้ำเลือด crepitus ชา shock",
        "Type I polymicrobial (DM, IVDU, alcohol) · II S. pyogenes · III Vibrio (น้ำทะเล) · IV fungal",
        "รักษา = surgical debridement ด่วน + empirical vanco + pip/tazo (หรือ carbapenem)",
        "S. pyogenes / C. perfringens → penicillin G + clindamycin",
        "Gram-positive bacilli จากตุ่มน้ำ + crepitus = C. perfringens",
    ],
    items=[
        mcq("DERM-06-04-1", """A 32-year-old man was bitten by a spider on his left calf 3 days ago. Yesterday the calf became swollen, red and extremely painful. Temperature is 39.3°C, HR 112/min, BP 134/76 mmHg. The distal left leg is swollen and exquisitely tender, the skin is purple and dusky, and crepitus is palpable. What is the most likely diagnosis?""",
            "Necrotizing fasciitis", ["Deep venous thrombosis", "Superficial thrombophlebitis", "Chronic venous insufficiency", "Osteomyelitis"],
            explain="""ไข้สูง ปวดมาก **ผิวม่วงคล้ำ + crepitus** ลามเร็วหลังแผลเล็ก = **necrotizing fasciitis** (สไลด์หน้า 205, 208–209)
- DVT ทำให้ขาบวม เจ็บ แต่ไม่มี crepitus ผิวม่วงคล้ำแบบเนื้อตาย และไข้สูงแบบ sepsis
- Thrombophlebitis เป็นเส้นแข็งแดงตามหลอดเลือดดำผิว ไม่ลามทั้งขา
- Venous insufficiency เป็นโรคเรื้อรัง ไม่เกิดใน 1 วันพร้อมไข้
- Osteomyelitis ปวดลึกที่กระดูก ไม่มี crepitus ใต้ผิวและผิวม่วงคล้ำแบบนี้""",
            pearl="ปวดมาก + ผิวม่วงคล้ำ + crepitus + ไข้ = NF",
            topic="NF dx", ref=[f"{D} หน้า 208–209"], nl=["2.2.50"], kind="old", src=OLD),
        mcq("DERM-06-04-2", """A 40-year-old man with alcoholism has extreme pain in his left thigh 4 days after falling while drunk. Temperature is 39.5°C, HR 115/min, BP 108/74 mmHg. The thigh is swollen with dusky skin, severe tenderness and crepitus. After intravenous fluids, what is the next step in management?""",
            "Empirical broad-spectrum IV antibiotics and urgent surgical debridement", ["Culture the wound and await results before starting antibiotics", "Aggressive fluid resuscitation and serial BUN/creatinine only", "Systemic prednisolone", "Empirical IV antibiotics alone and reassess in 48 hours"],
            explain="""NF ต้องได้ **ทั้ง empirical IV ATB และ surgical debridement ทันที** — การผ่าตัดเอาเนื้อตายออกคือหัวใจของการรักษา ยาอย่างเดียวเข้าไม่ถึงเนื้อตายที่ไม่มีเลือดไปเลี้ยง (สไลด์หน้า 206, 210–211)
- การรอผล culture ก่อนให้ยาทำให้ล่าช้าจนเสียชีวิต — ให้เก็บ culture แล้วเริ่มยาทันที
- การให้น้ำเกลือและติดตามไตเป็นแค่ supportive ไม่ได้รักษาต้นเหตุ
- Prednisolone ไม่มีบทบาทและกดภูมิ
- ยาอย่างเดียวแล้วรอ 48 ชม. ทำให้เนื้อตายลาม อัตราตายเพิ่มตามความล่าช้าของการผ่าตัด""",
            pearl="NF → empirical ATB + debridement ด่วน (ห้ามรอ)",
            topic="NF mx", ref=[f"{D} หน้า 210–211"], nl=["2.2.50"], kind="old", src=OLD),
        mcq("DERM-06-04-3", """A 60-year-old man was stabbed by brushwood while gardening yesterday. Today he has fever 40°C, BP 80/40 mmHg, HR 120/min. His left thigh shows erythematous and purplish-black blebs with crepitation and extreme tenderness. Gram stain of bleb fluid shows large, boxcar-shaped Gram-positive bacilli with few neutrophils. What is the causative pathogen?""",
            "Clostridium perfringens", ["Bacillus anthracis", "Clostridium tetani", "Corynebacterium striatum", "Erysipelothrix rhusiopathiae"],
            explain="""แผลลึกปนดิน + ลามเร็วใน 1 วัน + **crepitus** + ตุ่มน้ำม่วงดำ + shock + **Gram-positive bacilli รูปกล่อง** = **C. perfringens** (gas gangrene/clostridial myonecrosis) (สไลด์หน้า 212–213)
- B. anthracis ทำให้เกิด cutaneous anthrax เป็นแผล eschar ดำ ไม่เจ็บ บวมรอบ ๆ ไม่มี crepitus
- C. tetani ทำให้เกิดบาดทะยัก (กล้ามเนื้อเกร็ง) ไม่ใช่เนื้อตายมีแก๊ส
- Corynebacterium striatum เป็นเชื้อฉวยโอกาสในโรงพยาบาล ไม่ทำให้เกิดภาพนี้
- Erysipelothrix ทำให้เกิด erysipeloid ผื่นม่วงแดงที่นิ้วของคนจับปลา/เนื้อสัตว์ ไม่รุนแรง""",
            pearl="Crepitus + GPB boxcar จากตุ่มน้ำ = C. perfringens",
            topic="C. perfringens", ref=[f"{D} หน้า 212–213"], nl=["2.2.50", "2.3.12-3(6)"], kind="old", src=OLD),
        mcq("DERM-06-04-4", """A 30-year-old man injured his right leg while gardening. He now has fever, hemorrhagic bullae and a warm, swollen, erythematous right leg. Gram stain of bleb fluid shows Gram-positive bacilli. Surgical debridement has been arranged. Which antibiotic regimen is most appropriate?""",
            "Penicillin G plus clindamycin", ["Vancomycin plus clindamycin", "Piperacillin-tazobactam alone", "Ceftriaxone plus clindamycin", "Cloxacillin plus clindamycin"],
            explain="""Gram-positive bacilli จากตุ่มน้ำเลือดหลังแผลปนดิน = **C. perfringens** → **IV penicillin G + IV clindamycin** (clindamycin ยับยั้งการสร้าง toxin) ร่วมกับ debridement (สไลด์หน้า 207, 214–217)
- Vancomycin + clindamycin ใช้กับ MRSA/TSS ที่ไม่ทราบเชื้อ ไม่ใช่ยาจำเพาะของ clostridia
- Piperacillin-tazobactam เดี่ยว ๆ เป็นส่วนหนึ่งของ empirical regimen แต่ไม่มี clindamycin กด toxin
- Ceftriaxone ไม่ใช่ยาหลักต่อ clostridia
- Cloxacillin + clindamycin เป็นสูตรของ MSSA (เช่น SSSS/TSS) ไม่ครอบคลุม clostridia ดีเท่า penicillin G""",
            pearl="C. perfringens / S. pyogenes NF → PGS + clindamycin",
            topic="NF specific ATB", ref=[f"{D} หน้า 214–217"], nl=["2.2.50", "2.3.12-3(6)"], kind="old", src=OLD),
        mcq("DERM-06-04-5", """A 58-year-old man with alcoholic cirrhosis cut his leg on rocks while wading in seawater 24 hours ago. He now has hemorrhagic bullae spreading rapidly on the leg, severe pain and hypotension. Which organism should be specifically suspected?""",
            "Vibrio species", ["Streptococcus pyogenes alone", "Candida species", "Pseudomonas aeruginosa", "Mycobacterium marinum"],
            explain="""แผลสัมผัส **น้ำทะเล** + ตับแข็ง + ตุ่มน้ำเลือดลามเร็ว + shock = **NF type III จาก Vibrio spp.** (สไลด์หน้า 203) · โรคตับเป็นปัจจัยเสี่ยงสำคัญ (เสริม)
- S. pyogenes (type II) ไม่สัมพันธ์จำเพาะกับน้ำทะเลและตับแข็ง
- Candida (type IV) พบในผู้ป่วยภูมิต่ำรุนแรง ไม่เกิดหลังแผลน้ำทะเลภายในวันเดียว
- P. aeruginosa ทำให้เกิด ecthyma gangrenosum ใน neutropenia
- M. marinum ทำให้เกิดตุ่ม granuloma เรื้อรังเป็นสัปดาห์หลังสัมผัสตู้ปลา ไม่ใช่ NF เฉียบพลัน (เสริม)""",
            pearl="NF หลังน้ำทะเล + ตับแข็ง = Vibrio (type III)",
            topic="NF type III", ref=[f"{D} หน้า 203"], nl=["2.2.50"]),
    ])

# ---------------------------------------------------------------- 06-05 Ecthyma gangrenosum
S5 = sec("derm-06-05", "Ecthyma gangrenosum",
    "P. aeruginosa bacteremia ในผู้ป่วยภูมิต่ำ (neutropenia) → แผลเนื้อตายกลางดำ · IV anti-pseudomonal: cefepime, pip/tazo, imipenem",
    minutes=4, source=f"{D} หน้า 218–220", nl=["2.3.3(2)", "2.3.12(13)"],
    md='''
### กลไก

- **P. aeruginosa bacteremia → กระจายมาที่ผิวหนัง** (บุกผนังหลอดเลือด → หลอดเลือดอุดตัน → เนื้อตาย (เสริม))
- **Risk: immunocompromised** โดยเฉพาะ **neutropenia หลังเคมีบำบัด**

### สิ่งที่เห็น

| ระยะ | ลักษณะ |
|---|---|
| เริ่ม (เสริม) | ปื้นแดง/ตุ่มน้ำเลือดไม่เจ็บมาก |
| ต่อมา | **gangrenous ulcer with necrotic black center** (eschar ดำ) ล้อมด้วยขอบแดง |
| ตำแหน่ง (เสริม) | ก้น ฝีเย็บ รักแร้ แขนขา |
| อาการร่วม | ไข้ (febrile neutropenia) ความดันต่ำ |

### การรักษา

- **IV ATB ที่คลุม P. aeruginosa**: **cefepime, piperacillin/tazobactam, imipenem** (หรือ meropenem)
- เป็น febrile neutropenia → เริ่มยาทันทีหลังเจาะ hemoculture (เสริม)

> Neutropenia + ไข้ + แผลดำตรงกลาง = **P. aeruginosa** (ไม่ใช่ S. aureus/strep) · แผล eschar ดำ ไม่เจ็บ บวมมากในคนเลี้ยงสัตว์ = anthrax (เสริม)
''',
    pearls=[
        "Ecthyma gangrenosum = P. aeruginosa bacteremia ในผู้ป่วย neutropenia",
        "แผลเนื้อตายกลางดำ ขอบแดง",
        "รักษา IV cefepime / pip-tazo / carbapenem",
    ],
    items=[
        mcq("DERM-06-05-1", """A patient with acute lymphoblastic leukemia received chemotherapy 1 week ago. He has had high fever for 2 days. Temperature 39°C, BP 90/70 mmHg. There is a painless, eschar-like ulcer with a black necrotic center and red rim in the antecubital fossa. CBC: WBC 1,000/mm3 (neutrophils 10%, lymphocytes 90%), Hct 25%, platelets 50,000/mm3. What is the most likely causative pathogen?""",
            "Pseudomonas aeruginosa", ["Staphylococcus aureus", "Streptococcus pyogenes", "Escherichia coli", "Vibrio vulnificus"],
            explain="""**Neutropenia หลังเคมีบำบัด** + ไข้ + **แผลเนื้อตายกลางดำ** = **ecthyma gangrenosum** จาก **P. aeruginosa** bacteremia (สไลด์หน้า 218–220)
- S. aureus ทำให้เกิดฝี/cellulitis ที่มีหนอง ไม่ใช่ eschar ดำจากหลอดเลือดอุดตันแบบนี้
- S. pyogenes ทำให้เกิด erysipelas/cellulitis/NF ซึ่งแดงลามมากกว่าเป็นจุดเนื้อตาย
- E. coli เป็นสาเหตุ bacteremia ใน neutropenia ได้ แต่ไม่ใช่เชื้อหลักของรอยโรคนี้
- Vibrio ต้องมีประวัติน้ำทะเล และเป็นตุ่มน้ำเลือดลามเร็ว""",
            pearl="Neutropenia + แผลกลางดำ = P. aeruginosa",
            topic="Ecthyma gangrenosum", ref=[f"{D} หน้า 219–220"], nl=["2.3.3(2)"], kind="old", src=OLD),
        mcq("DERM-06-05-2", """A 50-year-old woman with febrile neutropenia after chemotherapy for AML develops several painless, round, necrotic ulcers with black centers and erythematous halos on the buttocks. Blood cultures have been drawn. Which empirical antibiotic is most appropriate?""",
            "Intravenous cefepime", ["Oral dicloxacillin", "Intravenous cefazolin", "Oral amoxicillin-clavulanate", "Intravenous penicillin G plus clindamycin"],
            explain="""Ecthyma gangrenosum ใน febrile neutropenia → **IV ATB ที่คลุม P. aeruginosa** เช่น **cefepime**, piperacillin/tazobactam, imipenem (สไลด์หน้า 218)
- Dicloxacillin เป็นยากิน คลุมแค่ S. aureus และไม่พอสำหรับ febrile neutropenia
- Cefazolin เป็น first-generation cephalosporin ไม่ครอบคลุม Pseudomonas
- Amox-clav ไม่ครอบคลุม Pseudomonas และเป็นยากิน
- Penicillin G + clindamycin ใช้กับ strep/clostridial NF ไม่ครอบคลุม Pseudomonas""",
            pearl="Ecthyma gangrenosum → IV anti-pseudomonal (cefepime, pip/tazo, carbapenem)",
            topic="EG tx", ref=[f"{D} หน้า 218"], nl=["2.3.3(2)"]),
    ])

LECTURE = lecture("06", "Bacterial skin infections", subtitle="impetigo · folliculitis/furuncle · erysipelas & cellulitis · necrotizing fasciitis · ecthyma gangrenosum",
    objectives=[
        "จำผื่นของ impetigo, folliculitis, furuncle/carbuncle จากคำบรรยายและเชื้อที่เป็นสาเหตุ",
        "แยก erysipelas กับ cellulitis และเลือก oral/IV ATB ตามความรุนแรงและประวัติแผล",
        "จับ red flag ของ necrotizing fasciitis และสั่ง debridement + empirical ATB ทันที",
        "เลือกยาจำเพาะเชื้อ (PGS + clindamycin, cloxacillin, vancomycin, anti-pseudomonal)",
    ],
    sections=[S1, S2, S3, S4, S5])
