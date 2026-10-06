from lib import lecture, sec, mcq, fig

D = "สไลด์ Update ข้อสอบ 2025"
SRC = "NL2 2025 (update)"

def R(*p):
    return [f"{D} หน้า " + ", ".join(str(x) for x in p)]

S1 = sec("exam25-10-01", "Skin lumps & pigmented lesions",
    "Wart ดื้อการรักษา → electrocautery/curettage · ก้อนมี central punctum = epidermal inclusion cyst · จุดน้ำตาลแบนบนผิวโดนแดด = solar lentigo", minutes=4,
    source=f"{D} หน้า 67–70, 73–74", nl=["2.3.12(15)", "2.3.12(6)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Cutaneous wart (HPV) — สไลด์**
- First line: **topical salicylic acid, cryotherapy**
- Refractory: **laser therapy, electrocauterization/curettage**
- โจทย์ที่ถาม "**immediate procedural intervention**" → ตอบหัตถการที่เอาออกได้ทันที = electrocauterization

**ก้อนใต้ผิวหนัง**

| ก้อน | ลักษณะ |
|---|---|
| **Epidermal inclusion cyst** | สีผิว แข็ง เคลื่อนได้ ใน dermis–subcutis · **central black punctum** · บีบแล้วมีขี้ไคลกลิ่นเหม็น |
| Lipoma | นุ่ม เคลื่อนได้ **ไม่มี punctum** |
| Dermatofibroma | แข็งเล็ก ที่ขา · **dimple sign** เมื่อบีบ |
| Neurofibroma | นุ่ม กดยุบ (buttonhole sign) ± café-au-lait |
| "Sebaceous cyst" | ชื่อเรียกเดิม มักใช้หมายถึง EIC ที่ผิด (sebaceous cyst จริงคือ steatocystoma) |

**รอยน้ำตาลบนผิวที่โดนแดด**

| รอยโรค | ลักษณะ |
|---|---|
| **Solar lentigo** | **macule แบน** ขอบชัด สีน้ำตาลสม่ำเสมอ ผู้สูงอายุ **ไม่จางในฤดูหนาว** |
| Freckle (ephelis) | จุดเล็ก เด็ก/ผิวขาว **เข้มขึ้นเมื่อโดนแดด จางในหน้าหนาว** |
| Seborrheic keratosis | **นูน** stuck-on ผิวขรุขระ |
| Actinic keratosis | ปื้นแดง **สาก** มีขุย (premalignant) |
| Melanoma | ABCDE: ไม่สมมาตร ขอบไม่เรียบ หลายสี > 6 mm เปลี่ยนแปลง |
''',
    pearls=[
        "Wart: salicylic/cryo ก่อน · ดื้อ → laser หรือ electrocautery/curettage",
        "ก้อนมี central punctum = epidermal inclusion cyst",
        "Macule น้ำตาลแบนสม่ำเสมอบนผิวโดนแดดในผู้สูงอายุ = solar lentigo",
    ],
    items=[
        mcq("EXAM25-10-01-1",
            "A 28-year-old healthy man presents with a firm, hyperkeratotic, cauliflower-like papule on the dorsum of his right thumb that has been present for 4 months. It is tender with pressure but shows no sign of infection. He works as a mechanic and has frequent minor hand trauma. What is the most appropriate immediate procedural intervention?",
            "Electrocauterization",
            ["Shave excision", "Incisional biopsy", "20% urea cream", "0.1% triamcinolone cream"],
            kind="old", src=SRC,
            explain='''ตุ่มขรุขระแบบดอกกะหล่ำ = **common wart (verruca vulgaris)** · คำถามถาม "**หัตถการทันที**" → **electrocauterization (± curettage)** ทำลายรอยโรคได้ในครั้งเดียว (สไลด์: first line = salicylic acid/cryotherapy, refractory = laser หรือ electrocautery/curettage)
- Shave excision เหลือ HPV ที่ฐาน กลับเป็นซ้ำสูง
- Incisional biopsy ไม่จำเป็นเมื่อลักษณะเป็น wart ชัด
- 20% urea cream เป็นยาทาลดขุยหนา ไม่ใช่หัตถการและไม่ฆ่า HPV
- Triamcinolone (steroid) ไม่รักษา wart''',
            pearl="Wart + ต้องการหัตถการทันที → electrocautery/curettage", topic="Cutaneous wart",
            ref=R(67, 68), nl=["2.3.12(15)"]),
        mcq("EXAM25-10-01-2",
            "A 40-year-old man has a 4-cm, firm, mobile, non-tender dermal nodule with a central punctum on the upper back, present for more than 1 month. There is no erythema or discharge. What is the most likely diagnosis?",
            "Epidermal inclusion cyst",
            ["Lipoma", "Neurofibroma", "Dermatofibroma", "Pilomatricoma"],
            kind="old", src=SRC,
            explain='''ก้อนแข็ง เคลื่อนได้ อยู่ใน dermis–subcutis + **central punctum** = **epidermal inclusion (epidermoid) cyst** (สไลด์แสดงภาพ)
- Lipoma นุ่ม เป็น lobule ไม่มี punctum
- Neurofibroma นุ่ม กดยุบ (buttonhole sign)
- Dermatofibroma เป็นตุ่มแข็งเล็ก < 1 cm มี dimple sign มักที่ขา
- Pilomatricoma แข็งเหมือนหิน (calcified) มักในเด็กที่ศีรษะ/คอ ไม่มี punctum
(สไลด์มีตัวเลือก "sebaceous cyst" ซึ่งเป็นชื่อเรียกเดิมของ epidermal cyst ในคลินิก ทำให้กำกวม จึงเปลี่ยนเป็น pilomatricoma)''',
            pearl="Central punctum = epidermal inclusion cyst", topic="Epidermal cyst",
            ref=R(69, 70), nl=["2.3.12(6)"]),
        mcq("EXAM25-10-01-3",
            "A 65-year-old woman presents with multiple flat, well-demarcated, uniformly brown macules on the dorsa of her hands and on her face. They are asymptomatic, have appeared gradually over several years and do not fade in winter. What is the most likely diagnosis?",
            "Solar lentigo",
            ["Freckles (ephelides)", "Seborrheic keratosis", "Actinic keratosis", "Melanoma"],
            kind="old", src=SRC,
            explain='''Macule **แบน** ขอบชัด สีน้ำตาลสม่ำเสมอ หลายจุดบน**ผิวที่โดนแดด** (หลังมือ ใบหน้า) ในผู้สูงอายุ ค่อย ๆ เกิดหลายปี = **solar lentigo** (melanocyte เพิ่มจาก UV)
- Freckles เกิดในเด็ก/ผิวขาว เข้มขึ้นเมื่อโดนแดด**และจางในหน้าหนาว** (เติมในโจทย์เพื่อตัด)
- Seborrheic keratosis **นูน** ผิวขรุขระเหมือนแปะไว้
- Actinic keratosis เป็นปื้นแดงสากมีขุย
- Melanoma เป็นรอยเดี่ยวที่ไม่สมมาตร หลายสี เปลี่ยนแปลง''',
            pearl="Macule น้ำตาลแบนบนผิวโดนแดดผู้สูงอายุ = solar lentigo", topic="Solar lentigo",
            ref=R(73, 74), nl=["2.1.50"]),
    ])

S2 = sec("exam25-10-02", "Bullous & nodular eruptions",
    "ผู้สูงอายุ tense bullae คัน ไม่มี mucosa = bullous pemphigoid · ตุ่มแดงกดเจ็บที่หน้าแข้งหลังเจ็บคอ = erythema nodosum", minutes=4,
    source=f"{D} หน้า 71–72, 75–77", nl=["2.3.12-3(2)", "2.3.12-3(5)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Bullous diseases**

| | **Bullous pemphigoid** | Pemphigus vulgaris |
|---|---|---|
| อายุ | **ผู้สูงอายุ (> 60–70)** | 40–60 |
| ตุ่มน้ำ | **tense** ไม่แตกง่าย บนผื่นแดง **คัน** | **flaccid** แตกง่าย เป็นแผลถลอก |
| Mucosa | **มักไม่มี** | **มีเกือบทุกราย** (เริ่มที่ปาก) |
| Nikolsky | ลบ | บวก |
| Biopsy | **subepidermal** blister + **eosinophil** | intraepidermal (acantholysis) |
| รักษา | **topical steroid** (potent) · รุนแรง → prednisolone | systemic steroid ± rituximab |

- Bullous impetigo: เด็ก ตุ่มน้ำแตกเป็นสะเก็ดสีน้ำผึ้ง · Erythema multiforme: target lesion · Dermatitis herpetiformis: ตุ่มน้ำเล็กคันมากที่ข้อศอก/เข่า + celiac

**Erythema nodosum (สไลด์)**
- **ตุ่มแดงกดเจ็บที่หน้าแข้งทั้งสองข้าง** (septal panniculitis) ไม่แตกเป็นแผล
- สาเหตุ: idiopathic (บ่อยสุด), **ติดเชื้อ (strep, TB)**, autoimmune (sarcoidosis, IBD), ยา (ยาคุม sulfa)
- ตรวจตามสาเหตุที่สงสัย: CBC, ESR/CRP, **ASO titer/throat swab**, **CXR**, biopsy ถ้าไม่แน่ใจ
- รักษาสาเหตุ + supportive (NSAID, ยกขา)
''',
    pearls=[
        "ผู้สูงอายุ + tense bullae + คัน + ไม่มี mucosa = bullous pemphigoid",
        "BP: subepidermal + eosinophil → potent topical steroid",
        "ตุ่มแดงกดเจ็บหน้าแข้ง = erythema nodosum → หาสาเหตุ (strep, TB, sarcoid)",
    ],
    items=[
        mcq("EXAM25-10-02-1",
            "An 80-year-old man presents with multiple large, tense, fluid-filled bullae on erythematous skin over his trunk and limbs. The blisters do not rupture easily and are mildly pruritic. There is no mucosal involvement. What is the most likely diagnosis?",
            "Bullous pemphigoid",
            ["Pemphigus vulgaris", "Bullous impetigo", "Erythema multiforme", "Dermatitis herpetiformis"],
            kind="old", src=SRC,
            explain='''**ผู้สูงอายุ** + ตุ่มน้ำใหญ่ **tense** ไม่แตกง่าย บนผื่นแดง **คัน** + **ไม่มี mucosa** = **bullous pemphigoid** (autoantibody ต่อ BP180/BP230 ที่ hemidesmosome → subepidermal blister) → potent topical steroid
- Pemphigus vulgaris ตุ่ม flaccid แตกง่าย มีแผลในปากเกือบทุกราย Nikolsky บวก
- Bullous impetigo พบในเด็ก ตุ่มแตกเป็นสะเก็ดสีน้ำผึ้ง
- Erythema multiforme มี target lesion ตามแขนขา มักหลัง HSV
- Dermatitis herpetiformis เป็นตุ่มน้ำเล็กคันมากที่ด้านเหยียด สัมพันธ์กับ celiac''',
            pearl="ผู้สูงอายุ + tense bullae + ไม่มี mucosa = BP", topic="Bullous pemphigoid",
            ref=R(71, 72), nl=["2.3.12-3(2)"]),
        mcq("EXAM25-10-02-2",
            "A 25-year-old woman presents with painful, red, raised nodules on the anterior surfaces of both lower legs. She had a sore throat 2 weeks ago. The nodules do not ulcerate. What is the most likely diagnosis?",
            "Erythema nodosum",
            ["Cellulitis", "Erythema multiforme", "Contact dermatitis", "Pyoderma gangrenosum"],
            kind="old", src=SRC,
            explain='''ตุ่มนูนแดง**กดเจ็บที่หน้าแข้งทั้งสองข้าง** ไม่แตกเป็นแผล หลัง **เจ็บคอ 2 สัปดาห์** (streptococcal infection) = **erythema nodosum** → ตรวจ ASO/throat swab, CXR และรักษาด้วย NSAID
- Cellulitis มักเป็นข้างเดียว แดงร้อนเป็นปื้นขอบไม่ชัด มีไข้
- Erythema multiforme เป็น target lesion ที่มือเท้า ไม่ใช่ nodule
- Contact dermatitis คัน เป็นผื่นแดงมีขุยตามบริเวณที่สัมผัส
- Pyoderma gangrenosum เป็นแผลลึกขอบม่วงไม่สม่ำเสมอ''',
            pearl="ตุ่มแดงกดเจ็บหน้าแข้งหลัง strep = erythema nodosum", topic="Erythema nodosum",
            ref=R(75, 76, 77), nl=["2.3.12-3(5)"]),
    ])

LECTURE = lecture("10", "Dermato", "wart · epidermal cyst · lentigo · bullous pemphigoid · erythema nodosum",
    objectives=[
        "เลือกการรักษา wart ตามลำดับ",
        "แยกก้อนใต้ผิวหนังและรอยน้ำตาลบนผิวที่โดนแดด",
        "แยก bullous pemphigoid จาก pemphigus และหาสาเหตุ erythema nodosum",
    ],
    sections=[S1, S2])
