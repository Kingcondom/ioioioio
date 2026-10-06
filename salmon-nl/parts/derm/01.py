from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Dermato"
OLD = "ตัวอย่างข้อสอบในสไลด์"


def body(cx, y, cls="box"):
    """ร่างกายแบบ schematic มองด้านหน้า สูงราว 250 (หัวที่ y)"""
    return (
        f'<circle cx="{cx}" cy="{y+20}" r="18" class="{cls}"/>'
        f'<rect x="{cx-7}" y="{y+37}" width="14" height="8" class="{cls}"/>'
        f'<rect x="{cx-30}" y="{y+44}" width="60" height="86" rx="12" class="{cls}"/>'
        f'<rect x="{cx-47}" y="{y+48}" width="15" height="100" rx="7" class="{cls}"/>'
        f'<rect x="{cx+32}" y="{y+48}" width="15" height="100" rx="7" class="{cls}"/>'
        f'<rect x="{cx-27}" y="{y+132}" width="24" height="116" rx="9" class="{cls}"/>'
        f'<rect x="{cx+3}" y="{y+132}" width="24" height="116" rx="9" class="{cls}"/>'
    )


# ---------------------------------------------------------------- 01-01 morphology
F_PRIMARY = fig("derm-01-01-f1", "Primary lesion: แบน / นูนตัน / มีน้ำ — แบ่งด้วยขนาด 1 cm", '''<svg viewBox="0 0 740 360">
 <text x="20" y="28" class="tb">ชนิด</text>
 <text x="300" y="28" text-anchor="middle" class="tb">&lt; 1 cm</text>
 <text x="560" y="28" text-anchor="middle" class="tb">≥ 1 cm</text>
 <rect x="10" y="40" width="720" height="96" rx="10" class="sunk"/>
 <text x="20" y="70" class="tb">แบนราบ</text>
 <text x="20" y="90" class="t3">เปลี่ยนแค่สี</text>
 <text x="20" y="106" class="t3">คลำไม่ได้</text>
 <path d="M190 100H410" class="ln"/>
 <rect x="280" y="96" width="40" height="5" class="ac"/>
 <text x="300" y="80" text-anchor="middle" class="ta">Macule</text>
 <path d="M450 100H690" class="ln"/>
 <rect x="500" y="96" width="120" height="5" class="ac"/>
 <text x="560" y="80" text-anchor="middle" class="ta">Patch</text>
 <rect x="10" y="144" width="720" height="104" rx="10" class="sunk"/>
 <text x="20" y="174" class="tb">นูน ตัน</text>
 <text x="20" y="194" class="t3">คลำได้</text>
 <path d="M190 214H280C284 196 316 196 320 214H410" class="ln"/>
 <text x="300" y="184" text-anchor="middle" class="ta">Papule</text>
 <path d="M440 214H470V200H540V214H560" class="ln"/>
 <text x="505" y="184" text-anchor="middle" class="ta">Plaque</text>
 <text x="505" y="236" text-anchor="middle" class="t3">กว้าง แบนบน</text>
 <path d="M580 214H600C606 180 664 180 670 214H700" class="ln"/>
 <ellipse cx="635" cy="222" rx="28" ry="10" class="lnf"/>
 <text x="635" y="174" text-anchor="middle" class="ta">Nodule</text>
 <text x="635" y="244" text-anchor="middle" class="t3">ลึกถึง dermis/SC</text>
 <rect x="10" y="256" width="720" height="96" rx="10" class="sunk"/>
 <text x="20" y="286" class="tb">มีน้ำ/หนอง</text>
 <text x="20" y="306" class="t3">ตุ่มน้ำใส</text>
 <path d="M190 322H282C284 300 316 300 318 322H410" class="ln"/>
 <path d="M284 322C286 304 314 304 316 322Z" class="c1soft"/>
 <text x="300" y="290" text-anchor="middle" class="ta">Vesicle</text>
 <path d="M450 322H515C520 286 600 286 605 322H690" class="ln"/>
 <path d="M517 322C522 290 598 290 603 322Z" class="c1soft"/>
 <text x="560" y="282" text-anchor="middle" class="ta">Bulla</text>
 <text x="560" y="344" text-anchor="middle" class="t3">Pustule = ตุ่มที่มีหนอง (ทุกขนาด)</text>
</svg>''', "ขนาดตัดที่ 1 cm (บางตำราใช้ 0.5 cm) — macule→patch, papule→plaque/nodule, vesicle→bulla · nodule ต่างจาก plaque ที่ความลึก ไม่ใช่แค่ความกว้าง")

F_STAGE = fig("derm-01-01-f2", "Eczema สามระยะ และการแบ่งกลุ่ม", '''<svg viewBox="0 0 740 330">
 <rect x="10" y="10" width="230" height="150" rx="10" class="badsoft"/>
 <text x="125" y="34" text-anchor="middle" class="tb">Acute</text>
 <path d="M30 100H220" class="ln"/>
 <path d="M60 100C62 84 78 84 80 100Z M110 100C112 86 126 86 128 100Z M160 100C162 82 180 82 182 100Z" class="c1soft"/>
 <path d="M70 104V118 M120 104V114 M171 104V120" class="lnc1"/>
 <text x="125" y="140" text-anchor="middle" class="t2">แดง บวม vesicle ซึม (oozing)</text>
 <rect x="255" y="10" width="230" height="150" rx="10" class="misssoft"/>
 <text x="370" y="34" text-anchor="middle" class="tb">Subacute</text>
 <path d="M275 100H465" class="ln"/>
 <path d="M300 100L310 92L330 94L340 100Z M380 100L392 90L414 93L420 100Z" class="miss"/>
 <text x="370" y="140" text-anchor="middle" class="t2">แดง scale crust</text>
 <rect x="500" y="10" width="230" height="150" rx="10" class="c2soft"/>
 <text x="615" y="34" text-anchor="middle" class="tb">Chronic</text>
 <path d="M520 100H540V78H690V100H710" class="ln"/>
 <path d="M548 88H682 M548 82H682 M548 94H682" class="lnc2"/>
 <text x="615" y="122" text-anchor="middle" class="t2">หนา คล้ำ</text>
 <text x="615" y="140" text-anchor="middle" class="t2">lichenification (ลายผิวชัด)</text>
 <rect x="10" y="178" width="355" height="142" rx="10" class="box"/>
 <text x="187" y="202" text-anchor="middle" class="tb">Exogenous (สาเหตุจากภายนอก)</text>
 <text x="30" y="230" class="t2">• Irritant contact dermatitis</text>
 <text x="30" y="254" class="t2">• Allergic contact dermatitis</text>
 <text x="30" y="290" class="t3">ผื่นอยู่ตรงที่สัมผัส → ถามของที่ใช้</text>
 <rect x="375" y="178" width="355" height="142" rx="10" class="box"/>
 <text x="552" y="202" text-anchor="middle" class="tb">Endogenous (จากภายใน)</text>
 <text x="395" y="228" class="t2">• Atopic • Seborrheic</text>
 <text x="395" y="250" class="t2">• Nummular • Dyshidrotic</text>
 <text x="395" y="272" class="t2">• Stasis • Asteatotic</text>
 <text x="395" y="294" class="t2">• Pityriasis alba • LSC</text>
</svg>''', "ระยะของ eczema บอกเวลา ไม่ได้บอกสาเหตุ — โรคเดียวกันเป็นได้ทุกระยะ ต้องดูตำแหน่งและประวัติเพื่อแยกชนิด")

S1 = sec("derm-01-01", "Eczema: primary lesion, ระยะ และการแบ่งกลุ่ม",
    "ภาษาผื่นพื้นฐาน (macule/patch, papule/plaque, vesicle/bulla) · acute = vesicle oozing · subacute = scale crust · chronic = lichenification",
    minutes=6, source=f"{D} หน้า 7–10", nl=["2.3.12(7)", "2.1.50", "B4.2.2(11)"],
    md='''
### ทำไมต้องอ่านผื่นเป็นคำ

ข้อสอบ NL มักไม่มีรูป จะบรรยายผื่นด้วยคำศัพท์ — ต้องแปลคำเหล่านี้เป็นภาพในหัวให้ได้ก่อน (เสริม)

[[fig:derm-01-01-f1]]

| คำ | ความหมาย | ตัวอย่างโรค |
|---|---|---|
| Macule / Patch | แบน เปลี่ยนสี < 1 / ≥ 1 cm | vitiligo, PV, FDE ระยะแรก |
| Papule / Plaque | นูน ตัน < 1 / ≥ 1 cm (plaque แบนบนกว้าง) | psoriasis, lichen planus |
| Nodule | นูน ลึกถึง dermis/subcutis | erythema nodosum, acne nodule |
| Vesicle / Bulla | ตุ่มน้ำใส < 1 / ≥ 1 cm | HSV (vesicle), pemphigoid (bulla) |
| Pustule | ตุ่มหนอง | folliculitis, AGEP |
| Wheal | นูนบวมแดง หายใน < 24 ชม. | urticaria |
| Scale / Crust | ขุย (keratin) / สะเก็ดจากน้ำเหลือง-เลือดแห้ง | psoriasis / impetigo (honey-colored crust) |
| Lichenification | ผิวหนา ลายผิวชัด จากการเกาเรื้อรัง | chronic eczema, LSC |

(ตารางนี้เป็นศัพท์มาตรฐาน (เสริม))

### Eczema (dermatitis) — สามระยะ

[[fig:derm-01-01-f2]]

| ระยะ | สิ่งที่เห็น |
|---|---|
| **Acute** | **erythema, edema, vesicle, oozing** |
| **Subacute** | **erythema, scale, crust** |
| **Chronic** | ผิว **หนาและคล้ำ (thickened pigmented skin), lichenification** |

- โรค eczema ทุกชนิดเป็นได้ทั้งสามระยะ — ระยะบอกว่าเป็นมานานแค่ไหน/เกามากแค่ไหน
- หลักการรักษาตามระยะ (เสริม): acute ซึมมาก → **wet dressing** (NSS/น้ำเกลือประคบ) ให้แห้ง · chronic หนา → topical steroid แรงขึ้นใน ointment + moisturizer

### การแบ่งกลุ่ม

- **Exogenous**: irritant contact dermatitis (ICD), allergic contact dermatitis (ACD)
- **Endogenous**: atopic, seborrheic, nummular, dyshidrotic, stasis (+ asteatotic, pityriasis alba, lichen simplex chronicus)

> โจทย์บรรยาย "erythematous papulovesicles with oozing" = acute eczema · "lichenified hyperpigmented plaque" = chronic eczema — แล้วค่อยใช้ **ตำแหน่ง + อายุ + ประวัติสัมผัส** บอกชนิด
''',
    figs=[F_PRIMARY, F_STAGE],
    pearls=[
        "Acute eczema = erythema edema vesicle oozing · subacute = scale crust · chronic = lichenification",
        "Macule/patch แบน · papule/plaque นูนตัน · vesicle/bulla มีน้ำ — ตัดที่ 1 cm",
        "Plaque = แผ่นนูนกว้างแบนบน · nodule = ก้อนลึก",
        "Exogenous eczema = ICD/ACD · ที่เหลือเป็น endogenous",
    ],
    items=[
        mcq("DERM-01-01-1", """A 35-year-old woman has had an itchy rash on both forearms for 3 days after gardening. Examination shows erythematous, edematous plaques studded with tiny clear vesicles and serous oozing. Which stage of eczema best describes these lesions?""",
            "Acute eczema", ["Subacute eczema", "Chronic eczema", "Lichen simplex chronicus", "Post-inflammatory hyperpigmentation"],
            explain="""ผื่นแดงบวม มีตุ่มน้ำเล็ก และน้ำเหลืองซึม = ลักษณะของ **acute eczema** (สไลด์หน้า 7) ซึ่งเกิดในไม่กี่วันหลังสัมผัส
- Subacute eczema จะเห็นขุยและสะเก็ด (scale, crust) แทน vesicle ที่ซึม
- Chronic eczema คือผิวหนา คล้ำ ลายผิวชัด (lichenification) ต้องเป็นเรื้อรังหลายสัปดาห์
- Lichen simplex chronicus เป็น plaque หนาจากการเกาซ้ำที่จุดเดิม ไม่มีตุ่มน้ำซึม
- Post-inflammatory hyperpigmentation เป็นรอยดำแบนหลังผื่นหาย ไม่มีบวมหรือตุ่มน้ำ""",
            pearl="Vesicle + oozing = acute; scale + crust = subacute; lichenification = chronic",
            topic="ระยะของ eczema", ref=[f"{D} หน้า 7–10"], nl=["2.3.12(7)"]),
        mcq("DERM-01-01-2", """A 60-year-old man has had intensely itchy skin on the back of his neck for 2 years. He scratches it every night. The lesion is a single well-defined, thickened, hyperpigmented plaque with exaggerated skin markings and a few excoriations; no vesicles are seen. Which term best describes the key morphologic change?""",
            "Lichenification", ["Vesiculation", "Desquamation with collarette scale", "Atrophy with telangiectasia", "Honey-colored crusting"],
            explain="""ผิวหนาขึ้นจนลายผิวเด่นชัดจากการเกาซ้ำนาน ๆ คือ **lichenification** ซึ่งเป็นลักษณะของ chronic eczema และ lichen simplex chronicus (สไลด์หน้า 9, 47)
- Vesiculation (ตุ่มน้ำ) พบใน acute eczema ไม่ใช่ผื่นที่เป็นมา 2 ปีแล้วหนา
- Collarette scale คือขุยเป็นวงชายผ้าที่ขอบผื่น เป็นลักษณะของ pityriasis rosea
- Atrophy กับ telangiectasia เป็นผลข้างเคียงของการทา steroid นาน ๆ ผิวจะบางลง ตรงข้ามกับผิวหนา
- Honey-colored crust เป็นสะเก็ดของ impetigo จากเชื้อแบคทีเรีย""",
            pearl="เกาเรื้อรัง → ผิวหนา ลายผิวชัด = lichenification",
            topic="Lichenification", ref=[f"{D} หน้า 9, 47"], nl=["2.3.12(7)"]),
        mcq("DERM-01-01-3", """A 72-year-old man presents with several tense, clear fluid-filled lesions on his thighs. The largest measures 2.5 cm in diameter and the smallest 1.2 cm. Which term most accurately describes these primary lesions?""",
            "Bullae", ["Vesicles", "Pustules", "Wheals", "Nodules"],
            explain="""ตุ่มน้ำใสที่ขนาด **≥ 1 cm เรียกว่า bulla** (พหูพจน์ bullae) — ตุ่มที่เล็กที่สุดในโจทย์ก็ยัง 1.2 cm (ศัพท์มาตรฐาน (เสริม))
- Vesicle คือตุ่มน้ำใสขนาดน้อยกว่า 1 cm
- Pustule คือตุ่มที่มีหนองข้างใน สีขาวเหลือง ไม่ใช่น้ำใส
- Wheal คือผื่นนูนบวมแดงไม่มีน้ำข้างใน และหายไปในไม่ถึง 24 ชั่วโมง
- Nodule คือก้อนนูนตันที่อยู่ลึก ไม่มีของเหลว""",
            pearl="Vesicle < 1 cm · bulla ≥ 1 cm",
            topic="Primary lesion", ref=[f"{D} หน้า 7"], nl=["2.1.50"]),
    ])

# ---------------------------------------------------------------- 01-02 ICD
S2 = sec("derm-01-02", "Irritant contact dermatitis (ICD)",
    "สารระคายทำลายผิวตรง ๆ ไม่ผ่านภูมิ · ใครโดนก็เป็น · ผื่นอยู่เฉพาะจุดสัมผัส · Paederus kissing lesion · แมงกะพรุนล้างด้วยน้ำส้มสายชู/น้ำทะเล ห้ามน้ำจืด",
    minutes=6, source=f"{D} หน้า 11–13", nl=["2.3.12(7)", "B4.2.2(11)", "2.3.18(8)"],
    md='''
### กลไก

สารระคายเคืองทำลาย skin barrier และเซลล์ผิวโดยตรง — **ไม่ต้องผ่านระบบภูมิคุ้มกัน ไม่ต้องเคยสัมผัสมาก่อน** (เสริม)
- **Acute ICD**: สัมผัสสารระคายเคืองแรง **ครั้งเดียว/ช่วงสั้น** → เป็นใน **วินาทีถึงชั่วโมง** · **ทุกคนที่สัมผัสเป็นหมด**
  - กรด/ด่างแก่ (strong acids/alkalis)
  - **Paederus dermatitis** (ด้วงก้นกระดก)
  - **Jellyfish dermatitis** (แมงกะพรุน)
- **Chronic (cumulative) ICD**: สัมผัสสารระคายอ่อน **ซ้ำ ๆ** → ค่อย ๆ เป็น (gradual onset)
  - **น้ำ สบู่ ผงซักฟอก** กรด/ด่างอ่อน → เช่น มือแม่บ้าน พยาบาล คนล้างจาน

### สิ่งที่เห็น

| ชนิด | ลักษณะผื่น |
|---|---|
| Acute ICD | แดง แสบร้อนมากกว่าคัน ตุ่มน้ำ/แผลไหม้ **ขอบเขตเท่าบริเวณที่สัมผัสพอดี** (lesion limited to exposure area) |
| Paederus | ผื่นแดงเป็นเส้น/ปื้น มี vesicle-pustule ตรงกลาง แสบร้อน · ผื่นสองข้างของข้อพับที่ประกบกัน = **"kissing lesion"** (ตื่นมาเจอ เพราะตบแมลงบนผิว) |
| Jellyfish | ผื่นแดงเป็นเส้นตามรอยหนวดพาดผ่านผิว ปวดแสบทันที |
| Chronic ICD | ผิวแห้ง แตก ขุย หนา ที่หลังมือ/ง่ามนิ้ว ไม่มีขอบชัด |

### การดูแล

- **Avoid causative irritant** + **ใส่ PPE** (ถุงมือ face shield)
- **Acute ICD**: **irrigate with water** (ล้างสารเคมีด้วยน้ำปริมาณมาก) + **wet dressing**
- **Chronic ICD**: **moisturizer + topical steroid**
- **Jellyfish**: ราด/แช่ด้วย **acetic acid (น้ำส้มสายชู) หรือน้ำทะเล** — **ห้ามใช้น้ำจืดหรือ alcohol** (ทำให้ nematocyst ที่เหลือแตกปล่อยพิษเพิ่ม (เสริม)) · เอาหนวดออกด้วย **ถุงมือหนา / แหนบคีบ / บัตรขูด**

> ICD vs ACD: ICD **เกิดกับทุกคน, เร็ว, จำกัดที่จุดสัมผัส, แสบมากกว่าคัน** · ACD **เฉพาะคนที่แพ้, 12–48 ชม., ลามเกินจุดสัมผัส, คันเด่น**
''',
    pearls=[
        "Acute ICD: ทุกคนที่สัมผัสเป็น ผื่นจำกัดที่จุดสัมผัส เกิดในวินาที–ชั่วโมง",
        "Chronic ICD: น้ำ สบู่ ผงซักฟอกซ้ำ ๆ → มือแห้งแตก → moisturizer + topical steroid + ถุงมือ",
        "Paederus = kissing lesion ตรงข้อพับ",
        "แมงกะพรุน: น้ำส้มสายชู/น้ำทะเล ห้ามน้ำจืด ห้าม alcohol",
    ],
    items=[
        mcq("DERM-01-02-1", """A 22-year-old man wakes up with a burning, linear erythematous plaque with small vesicles and pustules on the right antecubital fossa. A mirror-image lesion is present on the opposing skin of the forearm and arm where the elbow folds. He remembers slapping an insect on his arm the night before. What is the most likely diagnosis?""",
            "Paederus dermatitis", ["Herpes zoster", "Allergic contact dermatitis to nickel", "Bullous impetigo", "Fixed drug eruption"],
            explain="""ผื่นแสบร้อนเป็นเส้น มีตุ่มน้ำ-ตุ่มหนอง หลังตบแมลง และมีผื่นคู่สะท้อนบนผิวที่ประกบกันตรงข้อพับ (**kissing lesion**) = **Paederus dermatitis** ซึ่งเป็น acute ICD จากสาร pederin ของด้วงก้นกระดก (สไลด์หน้า 11–12)
- Herpes zoster เป็นกลุ่มตุ่มน้ำตาม dermatome ข้างเดียว มี prodrome ปวดแสบนำ ไม่เกิดเป็นคู่ประกบตรงข้อพับ
- ACD ต่อ nickel ต้องมีประวัติสัมผัสโลหะ ผื่นคันและขึ้นหลัง 12–48 ชม. ตรงที่ใส่เครื่องประดับ
- Bullous impetigo เป็นตุ่มน้ำใหญ่ flaccid จาก S. aureus ไม่ได้เป็นเส้นแสบร้อนหลังตบแมลง
- Fixed drug eruption ต้องมีประวัติกินยา ผื่นกลมสีม่วงคล้ำที่เดิมซ้ำ ๆ""",
            pearl="Paederus = ผื่นแสบเป็นเส้น + kissing lesion",
            topic="Paederus dermatitis", ref=[f"{D} หน้า 11–12"], nl=["2.3.12(7)"]),
        mcq("DERM-01-02-2", """A 28-year-old woman is stung by a box jellyfish while swimming. Several tentacle fragments still adhere to her leg, which shows painful linear erythematous streaks. What is the most appropriate immediate local management?""",
            "Rinse the area with vinegar (acetic acid) and remove tentacles with forceps or a card", ["Rinse the area with fresh tap water", "Wipe the area with 70% alcohol", "Rub the tentacles off with a towel and bare hands", "Apply a pressure immobilization bandage and observe without rinsing"],
            explain="""การดูแลแมงกะพรุนตามสไลด์คือ **ล้าง/แช่ด้วย acetic acid (น้ำส้มสายชู) หรือน้ำทะเล** แล้วเอาหนวดออกด้วยถุงมือหนา แหนบ หรือบัตรขูด (สไลด์หน้า 12)
- น้ำจืดเปลี่ยนแรงดันออสโมติกทำให้ nematocyst ที่ยังไม่แตกปล่อยพิษเพิ่ม สไลด์ห้ามไว้ชัดเจน
- Alcohol ก็กระตุ้นให้ nematocyst ยิงพิษเช่นกัน สไลด์ห้ามใช้
- การถูด้วยผ้าหรือมือเปล่ากดให้ nematocyst แตกเพิ่ม และผู้ช่วยก็จะโดนพิษด้วย
- Pressure immobilization ใช้กับงูพิษต่อระบบประสาท ไม่ได้ทำให้พิษแมงกะพรุนที่ผิวหยุด และไม่ได้เอาหนวดออก""",
            pearl="แมงกะพรุน = น้ำส้มสายชู/น้ำทะเล ห้ามน้ำจืด ห้าม alcohol",
            topic="Jellyfish dermatitis", ref=[f"{D} หน้า 12"], nl=["2.3.18(8)"]),
        mcq("DERM-01-02-3", """A 45-year-old housewife who washes dishes by hand many times a day has had dry, cracked, scaly skin on the backs of both hands and finger webs for 6 months. There are no vesicles and the rash does not extend to the forearms. Patch testing is negative. Besides wearing protective gloves, what is the most appropriate treatment?""",
            "Regular moisturizer plus a topical corticosteroid", ["Oral prednisolone for 4 weeks", "Topical ketoconazole cream", "Oral cephalexin", "Wet dressing alone with normal saline"],
            explain="""มือแห้งแตกเป็นขุยจากน้ำและน้ำยาล้างจานซ้ำ ๆ patch test ลบ = **chronic (cumulative) ICD** · การรักษาตามสไลด์คือเลี่ยงสารระคาย ใส่ PPE แล้วใช้ **moisturizer + topical steroid** (สไลด์หน้า 11, 13)
- Oral prednisolone เป็นยาระบบที่ไม่จำเป็นสำหรับผื่นเฉพาะที่ไม่รุนแรง และผื่นจะกลับเมื่อหยุดยา
- Ketoconazole cream ใช้รักษาเชื้อรา/seborrheic dermatitis แต่ผื่นนี้ไม่มีลักษณะของการติดเชื้อรา
- Cephalexin ใช้เมื่อมีติดเชื้อแบคทีเรียแทรก ไม่มี crust หนองในโจทย์
- Wet dressing ใช้กับ acute ICD ที่ซึม ผื่นเรื้อรังที่แห้งแตกต้องการความชุ่มชื้นและ steroid""",
            pearl="Chronic ICD = moisturizer + topical steroid + ถุงมือ",
            topic="Chronic ICD", ref=[f"{D} หน้า 13"], nl=["2.3.12(7)", "B4.4(1)"]),
    ])

# ---------------------------------------------------------------- 01-03 ACD
S3 = sec("derm-01-03", "Allergic contact dermatitis (ACD)",
    "Type IV hypersensitivity · ต้องเคย sensitize · เฉพาะคนแพ้ · ผื่นขึ้น 12–48 ชม. ลามเกินจุดสัมผัส · nickel, น้ำหอม, เครื่องสำอาง, ถุงมือ · patch test",
    minutes=6, source=f"{D} หน้า 14–19", nl=["2.3.12(7)", "B4.2.2(11)", "B1.4.11(1)"],
    md='''
### กลไก

- **Type IV (delayed-type) hypersensitivity** — ต้องเคยสัมผัส allergen ซ้ำ (sensitization) ก่อน ครั้งต่อมาจึงเกิดผื่น
- เกิด **เฉพาะบางคน** ที่แพ้ ไม่ใช่ทุกคนที่สัมผัส
- ผื่นขึ้น **12–48 ชั่วโมง** หลังสัมผัส · ผื่น **ลามเกินขอบเขตที่สัมผัส (extend beyond area)** ได้

### สารก่อแพ้ที่พบบ่อย (สไลด์หน้า 14)

| สาร | ตำแหน่งผื่นที่ชวนนึกถึง |
|---|---|
| **Nickel** | ติ่งหู (ต่างหู) ข้อมือ (นาฬิกา) **ใต้สะดือ (หัวเข็มขัด กระดุมกางเกง)** ข้างจมูก-หลังหู (แว่นตา) |
| Personal care products: น้ำหอม สบู่ เครื่องสำอาง | หน้า เปลือกตา (eye shadow) คอ |
| ถุงมือ (gloves) | มือ ข้อมือ |
| รองเท้า (เสริม) | หลังเท้า สองข้างสมมาตร |

### สิ่งที่เห็น

- Eczema ระยะใดก็ได้: acute = แดง บวม vesicle ซึม · chronic = หนา คล้ำ
- **คันเด่น** · ผื่นมีรูปร่างตามของที่สัมผัส (เช่น วงกลมใต้สะดือ ใต้สายนาฬิกา) แต่ขอบลามออกได้
- เปลือกตาบวมแดงสองข้าง + vesicle หลังเปลี่ยน eye shadow = ACD ต่อเครื่องสำอาง

### การวินิจฉัย

- **Skin patch test** — ใช้เมื่อไม่แน่ใจ หรือไม่รู้สาเหตุ และ **ช่วยแยก ACD จาก ICD** (ACD ให้ผลบวก) (สไลด์หน้า 16–17)
- Patch test = ทดสอบ type IV (ติดสารบนหลัง 48 ชม. อ่านที่ 48 และ 72–96 ชม. (เสริม)) — ต่างจาก **skin prick test ที่ทดสอบ type I (IgE)**

### การรักษา

- **Avoid allergen** (สำคัญที่สุด)
- **Moisturizer, wet dressing** (ผื่นซึม), **topical steroid**
- **Prednisone** เมื่อผื่นกว้างหรือรุนแรง

| | ICD | ACD |
|---|---|---|
| กลไก | ทำลายผิวตรง ๆ | Type IV hypersensitivity |
| ใครเป็น | ทุกคน (acute) | เฉพาะคนที่แพ้ |
| เวลาเริ่ม | วินาที–ชั่วโมง | **12–48 ชม.** |
| ขอบเขต | **จำกัดที่จุดสัมผัส** | **ลามเกินจุดสัมผัส** |
| อาการเด่น | แสบ เจ็บ | คัน |
| Patch test | ลบ | **บวก** |
''',
    pearls=[
        "ACD = type IV · 12–48 ชม. · ลามเกินจุดสัมผัส · เฉพาะคนแพ้",
        "Nickel: ต่างหู นาฬิกา หัวเข็มขัด กระดุม แว่นตา",
        "Patch test = type IV (ACD) · skin prick test = type I (IgE)",
        "รักษา: เลี่ยง allergen + topical steroid ± prednisone ถ้ากว้าง",
    ],
    items=[
        mcq("DERM-01-03-1", """A 20-year-old woman presents with symmetric swelling of both eyes. She recently changed her brand of eye shadow. Examination shows erythematous upper eyelids with small vesicles. What is the most likely diagnosis?""",
            "Allergic contact dermatitis", ["Angioedema", "Periorbital cellulitis", "Atopic dermatitis", "Seborrheic dermatitis"],
            explain="""เปลือกตาบวมแดงมีตุ่มน้ำ **สองข้างสมมาตร** หลังเปลี่ยนเครื่องสำอาง = **allergic contact dermatitis** ต่อส่วนผสมใน eye shadow (สไลด์หน้า 18–19)
- Angioedema บวมนุ่มที่ชั้นลึก ไม่มี vesicle หรือผื่นแดงแบบ eczema และมักหายใน 1–3 วัน
- Periorbital cellulitis มักเป็นข้างเดียว เจ็บ ร้อน มีไข้ ไม่มี vesicle และไม่สัมพันธ์กับเครื่องสำอาง
- Atopic dermatitis เป็นผื่นเรื้อรังตามข้อพับในผู้ใหญ่ ร่วมกับประวัติ atopy ไม่ได้เริ่มเฉียบพลันหลังสัมผัสของใหม่
- Seborrheic dermatitis เป็นผื่นแดงขุยมันที่คิ้ว ร่องจมูก หนังศีรษะ ไม่มีตุ่มน้ำ""",
            pearl="เปลี่ยนเครื่องสำอาง → เปลือกตาแดงบวม vesicle สองข้าง = ACD",
            topic="ACD", ref=[f"{D} หน้า 18–19"], nl=["2.3.12(7)"], kind="old", src=OLD),
        mcq("DERM-01-03-2", """A 30-year-old man has a recurrent itchy eczematous plaque just below the umbilicus that appears 1–2 days after he wears a particular pair of jeans. The rash spreads slightly beyond the area touched by the metal button. He has no history of atopy. Which test is most useful to confirm the cause?""",
            "Skin patch test", ["Skin prick test", "Serum total IgE", "KOH preparation", "Tzanck smear"],
            explain="""ผื่น eczema ใต้สะดือตรงกระดุมโลหะ ขึ้นหลังใส่ 1–2 วัน ลามเกินจุดสัมผัส = **ACD ต่อ nickel** · ยืนยันสาเหตุด้วย **skin patch test** ซึ่งทดสอบ type IV hypersensitivity (สไลด์หน้า 14–17)
- Skin prick test ตรวจ type I (IgE) ใช้หา trigger ใน atopic dermatitis/urticaria ไม่ใช่ปฏิกิริยา delayed type IV
- Serum total IgE บอกความรุนแรงของ atopic dermatitis ไม่ได้บอกว่าแพ้สารสัมผัสตัวใด
- KOH ใช้หาเชื้อรา (tinea) ซึ่งจะเป็นผื่นวงขอบนูนขุย ไม่สัมพันธ์กับการใส่กางเกงตัวเดิม
- Tzanck smear หา multinucleated giant cell ของ herpes ไม่เกี่ยวกับผื่นแพ้สัมผัส""",
            pearl="สงสัย ACD ไม่รู้สาร → patch test",
            topic="Patch test", ref=[f"{D} หน้า 14–17"], nl=["2.3.12(7)"]),
        mcq("DERM-01-03-3", """A 26-year-old nurse develops itchy erythematous papulovesicles on both hands and wrists 24 hours after starting to use a new brand of rubber gloves. Her colleagues using the same gloves have no rash. Which feature most strongly favors allergic over irritant contact dermatitis?""",
            "Only she is affected and the rash extends beyond the area covered by the gloves after a 24-hour delay", ["The rash appeared on the hands", "The rash itches", "The lesions contain vesicles", "The rash improved after topical corticosteroid"],
            explain="""ลักษณะที่แยก ACD จาก ICD คือ **เกิดเฉพาะคนที่แพ้ (คนอื่นใช้แล้วไม่เป็น), ผื่นขึ้นช้า 12–48 ชม., ลามเกินจุดสัมผัส** — สะท้อน type IV hypersensitivity (สไลด์หน้า 11, 14–15)
- ผื่นที่มือเกิดได้ทั้ง ICD และ ACD เพราะมือสัมผัสสารบ่อยที่สุด
- อาการคันพบได้ทั้งสองแบบ แม้ ACD จะคันเด่นกว่า แต่ไม่ใช่ตัวแยกที่ชัดที่สุด
- Vesicle เป็นลักษณะของ acute eczema ทุกชนิด ไม่ได้จำเพาะกับ ACD
- การตอบสนองต่อ topical steroid เกิดได้กับ eczema ทุกชนิด ไม่ได้บอกกลไก""",
            pearl="เฉพาะคนแพ้ + ช้า 12–48 ชม. + ลามเกินจุดสัมผัส = ACD",
            topic="ACD vs ICD", ref=[f"{D} หน้า 11, 14–17"], nl=["2.3.12(7)", "B1.4.11(1)"]),
    ])

# ---------------------------------------------------------------- 01-04 AD
F_AD = fig("derm-01-04-f1", "Atopic dermatitis: ตำแหน่งผื่นเปลี่ยนตามอายุ", f'''<svg viewBox="0 0 740 330">
 <text x="185" y="22" text-anchor="middle" class="tb">ทารก (infant)</text>
 <text x="555" y="22" text-anchor="middle" class="tb">เด็กโต / ผู้ใหญ่</text>
 <g transform="translate(0,34)">{body(185, 10)}
  <ellipse cx="174" cy="34" rx="7" ry="6" class="bad"/><ellipse cx="196" cy="34" rx="7" ry="6" class="bad"/>
  <path d="M168 14C176 4 194 4 202 14" class="lnbad"/>
  <ellipse cx="146" cy="128" rx="9" ry="22" class="badsoft"/><ellipse cx="224" cy="128" rx="9" ry="22" class="badsoft"/>
  <ellipse cx="170" cy="210" rx="11" ry="20" class="badsoft"/><ellipse cx="200" cy="210" rx="11" ry="20" class="badsoft"/>
  <rect x="160" y="128" width="50" height="22" rx="6" class="oksoft"/>
 </g>
 <text x="20" y="64" class="t2">แก้มสองข้าง</text>
 <text x="20" y="82" class="t2">หนังศีรษะ</text>
 <text x="20" y="160" class="t2">ด้านนอกแขน</text>
 <text x="20" y="178" class="t2">(extensor)</text>
 <text x="20" y="246" class="t2">ด้านหน้าขา/เข่า</text>
 <text x="250" y="178" class="t3">ผ้าอ้อมมักไม่เป็น</text>
 <g transform="translate(0,34)">{body(555, 10)}
  <rect x="540" y="44" width="30" height="10" rx="4" class="bad"/>
  <ellipse cx="516" cy="102" rx="9" ry="9" class="bad"/><ellipse cx="594" cy="102" rx="9" ry="9" class="bad"/>
  <ellipse cx="516" cy="150" rx="9" ry="7" class="badsoft"/><ellipse cx="594" cy="150" rx="9" ry="7" class="badsoft"/>
  <ellipse cx="540" cy="200" rx="11" ry="9" class="bad"/><ellipse cx="570" cy="200" rx="11" ry="9" class="bad"/>
  <ellipse cx="540" cy="250" rx="11" ry="7" class="badsoft"/><ellipse cx="570" cy="250" rx="11" ry="7" class="badsoft"/>
 </g>
 <text x="640" y="84" class="t2">คอ</text>
 <text x="640" y="140" class="t2">ข้อพับแขน</text>
 <text x="640" y="188" class="t2">ข้อมือ มือ</text>
 <text x="640" y="238" class="t2">ข้อพับเข่า</text>
 <text x="640" y="256" class="t3">(ด้านหลัง)</text>
 <text x="640" y="290" class="t2">ข้อเท้า</text>
 <text x="370" y="322" text-anchor="middle" class="t3">สีแดงเข้ม = ตำแหน่งหลัก · สีอ่อน = พบได้ · กรอบเขียว = มักไม่เป็น</text>
</svg>''', "ทารกเป็นที่แก้ม หนังศีรษะ และด้าน extensor · พอโตย้ายไปข้อพับ (flexural) คอ ข้อมือ — ตำแหน่งตามอายุคือกุญแจของโจทย์ AD")

S4 = sec("derm-01-04", "Atopic dermatitis (AD)",
    "เริ่มวัยเด็ก · ประวัติ atopy · คัน + ผิวแห้ง · ทารก = หน้า/extensor · เด็กโต-ผู้ใหญ่ = flexural · mild: moisturizer + topical steroid · mod–severe: TCI, phototherapy, immunosuppressant",
    minutes=8, source=f"{D} หน้า 21–29", nl=["2.3.12(7)", "B4.2.2(11)", "B4.4(7)"],
    md='''
### กลไกและใครเป็น

- สไลด์จัดเป็น **type I hypersensitivity** (IgE) — จริง ๆ เป็นโรค **ผิวกั้นบกพร่อง (barrier defect เช่น filaggrin) + Th2 inflammation** ร่วมกัน (เสริม)
- **Onset: early childhood** · มีประวัติ **atopy ของตัวเอง/ครอบครัว**: **allergic rhinitis, asthma, allergic conjunctivitis**
- อาการมัก **ดีขึ้นเมื่อโตเป็นผู้ใหญ่**

### Triggers (สไลด์หน้า 21)

- อากาศแห้งมาก/ชื้นมาก, ความร้อน
- การระคายผิว: **เสื้อผ้าขนสัตว์ (wool), ผงซักฟอก**
- **ไรฝุ่น, เกสร, ขนสัตว์**
- ความเครียด · อาหาร: **ไข่ นม ถั่วลิสง แป้งสาลี** (ในเด็กเล็ก)

### สิ่งที่เห็น

| อายุ | ตำแหน่ง | ลักษณะ |
|---|---|---|
| **Infant** | **หน้า (แก้ม) หนังศีรษะ ด้าน extensor** ของแขนขา | acute: แดง papulovesicle **ซึม** มีรอยเกา |
| **Children & adult** | **ข้อพับ (flexor)**: ข้อพับแขน ข้อพับเข่า คอ ข้อมือ ข้อเท้า มือ | subacute–chronic: ขุย หนา **lichenification** |

- **Pruritus (คันมาก โดยเฉพาะกลางคืน) + dry skin** เป็นแกนของโรค — "itch that rashes"

[[fig:derm-01-04-f1]]

### การรักษา

- **Avoid trigger** ทุกระดับ
- **Mild**: **moisturizer, urea cream, topical steroid**
- **Moderate to severe**: **topical calcineurin inhibitors (TCI** เช่น tacrolimus, pimecrolimus**)**, **phototherapy**, **immunosuppressant** (เช่น cyclosporine, MTX (เสริม))
- ถ้ามีหนองหรือ honey-colored crust = ติดเชื้อ S. aureus แทรก → เพิ่ม antibiotic (เสริม)

### Investigation — ทำเมื่ออาการไม่ดีขึ้น

| Test | ใช้ทำอะไร |
|---|---|
| **Serum IgE** | บอก **ความรุนแรง** |
| **Skin prick test** | หา **trigger** (type I allergen) |
| **Skin patch test** | **R/O contact dermatitis** |

> ทารก 4–5 เดือน แก้มแดงซึม + ครอบครัว asthma/eczema = AD · ผู้ใหญ่ผื่นคันข้อพับแขน ข้อพับเข่า คอ คันจนนอนไม่หลับ = AD
''',
    figs=[F_AD],
    pearls=[
        "AD = คัน + ผิวแห้ง + ประวัติ atopy (AR, asthma, conjunctivitis)",
        "ทารก: แก้ม หนังศีรษะ extensor · เด็กโต/ผู้ใหญ่: ข้อพับ",
        "Mild: moisturizer + topical steroid · mod–severe: TCI, phototherapy, immunosuppressant",
        "IgE = ความรุนแรง · prick test = หา trigger · patch test = R/O contact dermatitis",
    ],
    items=[
        mcq("DERM-01-04-1", """A 5-month-old boy has had a rash on his cheeks for the past few weeks. His family history includes asthma and eczema. Examination shows bilateral erythematous cheeks with oozing papulovesicles and excoriations; the diaper area is spared. What is the most likely diagnosis?""",
            "Atopic dermatitis", ["Infantile seborrheic dermatitis", "Impetigo", "Irritant diaper dermatitis", "Scabies"],
            explain="""ทารกที่มี **ผื่นแดงซึม papulovesicle ที่แก้มสองข้าง** รอยเกา (คัน) และครอบครัวเป็น atopy = **atopic dermatitis** ระยะ infant (สไลด์หน้า 22, 24–25)
- Infantile seborrheic dermatitis เป็นขุยมันเหลืองที่หนังศีรษะ (cradle cap) คิ้ว ซอกพับ ไม่ค่อยคัน และไม่สัมพันธ์กับ atopy
- Impetigo เป็นสะเก็ดสีน้ำผึ้งรอบจมูกปาก ไม่ได้เป็นผื่นสองข้างเรื้อรังหลายสัปดาห์
- Irritant diaper dermatitis เกิดที่บริเวณผ้าอ้อม ซึ่งโจทย์บอกว่าไม่เป็น
- Scabies ในทารกมักเห็นตุ่มที่ฝ่ามือฝ่าเท้า ซอกพับ และคนในบ้านคันด้วย""",
            pearl="ทารก แก้มแดงซึม + family atopy = AD",
            topic="AD infant", ref=[f"{D} หน้า 24–25"], nl=["2.3.12(7)"], kind="old", src=OLD),
        mcq("DERM-01-04-2", """A 25-year-old woman has an itchy rash on both hands that oozes and stings. She is so itchy at night that she cannot sleep. She has had allergic rhinitis since childhood. Examination shows large erythematous plaques with excoriations on her hands, neck, antecubital fossae and popliteal fossae. What is the most likely diagnosis?""",
            "Atopic dermatitis", ["Pityriasis alba", "Psoriasis vulgaris", "Scabies", "Seborrheic dermatitis"],
            explain="""ผู้ใหญ่ที่มีผื่นคันมากกลางคืนที่ **ข้อพับ (flexural): คอ ข้อพับแขน ข้อพับเข่า** ร่วมกับมือ และมีประวัติ atopy = **atopic dermatitis** (สไลด์หน้า 22, 28–29)
- Pityriasis alba เป็นวงด่างขาวขอบไม่ชัดที่หน้าเด็ก ไม่คันมาก และไม่มีผื่นซึม
- Psoriasis vulgaris เป็น plaque ขุยเงินที่ด้าน extensor (ข้อศอก เข่า) ไม่ใช่ข้อพับ และไม่ซึม
- Scabies คันกลางคืนจริง แต่ผื่นเป็นตุ่มเล็กและ burrow ที่ง่ามนิ้ว ข้อมือ รักแร้ ขาหนีบ และคนใกล้ชิดคันด้วย
- Seborrheic dermatitis ขึ้นที่หนังศีรษะ หน้า ร่องจมูก หลังหู เป็นขุยมันไม่ซึม""",
            pearl="ผู้ใหญ่ผื่นคันข้อพับ + atopy = AD",
            topic="AD adult", ref=[f"{D} หน้า 28–29"], nl=["2.3.12(7)"], kind="old", src=OLD),
        mcq("DERM-01-04-3", """A 9-year-old girl with long-standing atopic dermatitis has persistent lichenified flexural plaques and facial eczema despite regular emollients and mid-potency topical corticosteroids on the body. Her mother is worried about skin atrophy on the face. Which topical agent is the most appropriate next step for the facial lesions?""",
            "Topical tacrolimus (calcineurin inhibitor)", ["Clobetasol propionate 0.05% ointment", "Topical mupirocin", "Topical ketoconazole", "Topical calcipotriol"],
            explain="""AD ระดับ moderate–severe ที่ไม่ดีขึ้น สไลด์ให้ใช้ **topical calcineurin inhibitor (TCI)** — tacrolimus/pimecrolimus ไม่ทำให้ผิวบาง จึงเหมาะกับหน้าและเปลือกตา (สไลด์หน้า 23)
- Clobetasol เป็น super-potent steroid ห้ามใช้บนหน้าเพราะทำให้ผิวฝ่อ เส้นเลือดฝอยขยาย ซึ่งเป็นสิ่งที่แม่กังวลอยู่
- Mupirocin ใช้เมื่อมีติดเชื้อ S. aureus (impetiginized) ซึ่งโจทย์ไม่มีหนองหรือสะเก็ด
- Ketoconazole ใช้รักษา seborrheic dermatitis/เชื้อรา ไม่ใช่การรักษา AD
- Calcipotriol (vitamin D analog) ใช้ใน psoriasis และระคายผิว AD""",
            pearl="AD หน้า/เปลือกตา ที่ต้องรักษานาน → TCI แทน steroid แรง",
            topic="AD treatment", ref=[f"{D} หน้า 23"], nl=["2.3.12(7)", "B4.4(7)"]),
        mcq("DERM-01-04-4", """A 6-year-old boy with moderate atopic dermatitis continues to flare despite good skin care. His parents want to know which environmental allergen (house dust mite, cat dander or pollen) is triggering his disease. Which investigation is most appropriate?""",
            "Skin prick test", ["Skin patch test", "Serum total IgE level", "Skin biopsy", "KOH preparation"],
            explain="""การหา **trigger** ของ AD ที่เป็น aeroallergen (ไรฝุ่น ขนสัตว์ เกสร) ซึ่งเป็น IgE-mediated ใช้ **skin prick test** (สไลด์หน้า 23)
- Patch test ใช้ R/O contact dermatitis (type IV) ไม่ใช่หา aeroallergen แบบ IgE
- Serum total IgE บอกความรุนแรงของโรคโดยรวม ไม่บอกว่าแพ้สารตัวไหน
- Skin biopsy ของ AD ได้ spongiotic dermatitis แบบไม่จำเพาะ ไม่ช่วยหา trigger
- KOH ใช้หาเชื้อรา ไม่เกี่ยวกับการหาสารกระตุ้นภูมิแพ้""",
            pearl="AD: prick = trigger · IgE = severity · patch = R/O contact",
            topic="AD investigation", ref=[f"{D} หน้า 23"], nl=["2.3.12(7)"]),
    ])

# ---------------------------------------------------------------- 01-05 SD
S5 = sec("derm-01-05", "Seborrheic dermatitis (SD)",
    "Malassezia + ต่อมไขมันทำงาน · Parkinson, HIV · ผื่นแดงขุยมันที่ scalp คิ้ว ร่องจมูก หลังหู ซอกพับ · ทารก = cradle cap · topical ketoconazole + topical steroid",
    minutes=6, source=f"{D} หน้า 30–35", nl=["2.3.12(7)", "B4.2.2(11)"],
    md='''
### กลไกและปัจจัยเสี่ยง

- สัมพันธ์กับเชื้อยีสต์ **Malassezia spp.** บนผิว + **ต่อมไขมันทำงานมาก (active sebaceous glands)**
- พบมากขึ้นใน **Parkinson disease** และ **HIV** (ผื่นกว้าง รุนแรง ดื้อยา → ควรนึกถึง HIV (เสริม))
- Trigger: **ความเครียด อดนอน อากาศ trauma**

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| Primary lesion | **erythematous patch/plaque with greasy (yellowish) scale** ขุยมันสีเหลือง |
| ตำแหน่ง (seborrheic area) | **scalp, หน้า, คิ้ว, glabella, nasolabial fold, หลังหู (retroauricular), ช่องหู, intertriginous area**, กลางอก (เสริม) |
| อาการ | คันเล็กน้อย เป็น ๆ หาย ๆ เรื้อรัง |
| Infantile SD | **scalp = cradle cap** (ขุยเหลืองมันหนาบนหนังศีรษะ), หน้า, ซอกพับ · ทารกไม่ค่อยคัน (เสริม) |
| Dandruff (รังแค) | รอยโรคที่ **ไม่ค่อยอักเสบบน scalp** = SD ชนิดอ่อน |

### การรักษา

- **Topical antifungals**: **ketoconazole, ciclopirox**
- **Topical steroid** (ฤทธิ์อ่อน ระยะสั้น)
- **Scalp**: แชมพู **ketoconazole, selenium sulfide, zinc pyrithione, tar**
- **Infantile SD**: **baby shampoo / baby oil** ชโลมแล้ว **แปรงขุยออกเบา ๆ** · **หายเองได้เมื่ออายุราว 1 ขวบ**

> SD vs AD ในทารก: SD = ขุยเหลืองมันที่หนังศีรษะ/ซอก **ไม่คัน** · AD = แก้มแดงซึม **คันมาก** มี family atopy
''',
    pearls=[
        "SD = Malassezia + ต่อมไขมัน · ผื่นแดงขุยมันที่ scalp คิ้ว ร่องจมูก หลังหู",
        "Parkinson และ HIV เสี่ยง SD — SD รุนแรงผิดปกติให้นึกถึง HIV",
        "ยาหลัก: topical ketoconazole ± topical steroid · scalp ใช้แชมพู keto/selenium/zinc/tar",
        "Cradle cap: baby oil + แปรงเบา ๆ หายเองราว 1 ขวบ",
    ],
    items=[
        mcq("DERM-01-05-1", """A 50-year-old man has chronic, intermittent, well-defined erythematous plaques with greasy yellowish scale on the external ear canals, eyebrows, glabella and nasolabial folds. The lesions are mildly itchy. What is the most likely diagnosis?""",
            "Seborrheic dermatitis", ["Pityriasis rosea", "Atopic dermatitis", "Acne vulgaris", "Verruca vulgaris"],
            explain="""ผื่นแดงขุยมันเหลืองที่ **ช่องหู คิ้ว glabella ร่องจมูก** (seborrheic area) เป็น ๆ หาย ๆ = **seborrheic dermatitis** (สไลด์หน้า 30, 32–33)
- Pityriasis rosea เป็นผื่นวงรีขุยแบบ collarette เรียงตามแนว Christmas tree บนลำตัว และหายเองใน 6–12 สัปดาห์
- Atopic dermatitis ในผู้ใหญ่ขึ้นที่ข้อพับ คันมาก ไม่มีขุยมันเหลือง
- Acne vulgaris เป็น comedone papule pustule ไม่ใช่ plaque ขุยมัน
- Verruca vulgaris เป็นตุ่มผิวขรุขระสีเนื้อ ไม่ใช่ผื่นแดงขุย""",
            pearl="ผื่นแดงขุยมัน คิ้ว ร่องจมูก หลังหู = SD",
            topic="SD diagnosis", ref=[f"{D} หน้า 32–33"], nl=["2.3.12(7)"], kind="old", src=OLD),
        mcq("DERM-01-05-2", """A 40-year-old man presents with an itchy rash on his scalp. Examination shows greasy scale on an erythematous base scattered across the scalp. There is no hair loss. What is the most appropriate management?""",
            "Topical ketoconazole (shampoo)", ["Oral diphenhydramine", "Reassurance only", "Oral prednisone plus oral ketoconazole", "Sun protection"],
            explain="""ขุยมันบนพื้นแดงที่หนังศีรษะ = **seborrheic dermatitis ของ scalp** → การรักษาคือ **topical antifungal เช่น ketoconazole shampoo** (สไลด์หน้า 31, 34–35)
- Diphenhydramine เป็น antihistamine ลดคันได้บ้างแต่ไม่ลดเชื้อ Malassezia และการอักเสบ
- การ reassure อย่างเดียวไม่เหมาะเพราะผู้ป่วยมีอาการและมียาที่ได้ผลดี
- Oral prednisone + oral ketoconazole เกินจำเป็น ยาระบบมีผลข้างเคียง (oral ketoconazole เป็นพิษต่อตับ) สำหรับโรคเฉพาะที่
- Sun protection ไม่ใช่การรักษา SD""",
            pearl="SD ที่ scalp → ketoconazole/selenium/zinc pyrithione shampoo",
            topic="SD treatment", ref=[f"{D} หน้า 31, 34–35"], nl=["2.3.12(7)"], kind="old", src=OLD),
        mcq("DERM-01-05-3", """A 2-month-old girl has thick, yellowish, greasy scales adherent to her scalp. She feeds well and does not seem itchy. There are a few similar mildly erythematous patches behind the ears. What is the most appropriate management?""",
            "Soften the scales with baby oil, wash with baby shampoo and gently brush them off", ["Oral fluconazole for 2 weeks", "Potent topical corticosteroid twice daily for 4 weeks", "Topical mupirocin three times daily", "Skin prick test for food allergens"],
            explain="""ทารกที่มีขุยเหลืองมันหนาบนหนังศีรษะ (**cradle cap**) และหลังหู ไม่คัน = **infantile seborrheic dermatitis** · สไลด์ให้ใช้ **baby oil/baby shampoo แล้วแปรงออกเบา ๆ** โรคหายเองได้เมื่ออายุราว 1 ขวบ (สไลด์หน้า 30–31)
- Oral fluconazole เป็นยาระบบที่ไม่จำเป็นสำหรับโรคที่หายเองและไม่รุนแรงในทารก
- Potent steroid นาน 4 สัปดาห์ในทารกเสี่ยงผิวบางและดูดซึมเข้าร่างกาย
- Mupirocin ใช้กับ impetigo ซึ่งจะเป็นสะเก็ดสีน้ำผึ้ง ไม่ใช่ขุยมัน
- Skin prick test ใช้หา trigger ของ AD ซึ่งทารกรายนี้ไม่คันและไม่มีลักษณะ AD""",
            pearl="Cradle cap = baby oil + แปรงเบา ๆ หายเองราว 1 ขวบ",
            topic="Infantile SD", ref=[f"{D} หน้า 30–31"], nl=["2.3.12(7)"]),
    ])

# ---------------------------------------------------------------- 01-06 Dyshidrotic
S6 = sec("derm-01-06", "Dyshidrotic eczema (Pompholyx)",
    "ตุ่มน้ำลึก (deep-seated vesicle) คันมาก สองข้าง ที่ฝ่ามือ ฝ่าเท้า ข้างนิ้ว · เป็นซ้ำ · topical steroid (แรง) ± oral steroid ถ้ารุนแรง",
    minutes=4, source=f"{D} หน้า 36–40", nl=["2.3.12(8)", "2.3.12(7)"],
    md='''
### ลักษณะ

- **Acute, recurrent** — เป็น ๆ หาย ๆ
- **Bilateral deep-seated vesicles/bullae** — ตุ่มน้ำใสเล็กฝังลึกใต้ผิวหนา ดูเหมือน "เม็ดสาคู" (tapioca-like (เสริม))
- ตำแหน่ง: **ฝ่ามือ ฝ่าเท้า ด้านข้างของนิ้วมือ-นิ้วเท้า**
- **Pruritus** คันมาก
- Trigger (เสริม): เหงื่อออกมาก ความเครียด อากาศร้อน สัมผัส nickel, ผื่นแพ้จากเชื้อราที่เท้า (id reaction)

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| Primary lesion | vesicle เล็ก 1–2 mm (เสริม) ฝังลึก ไม่แตกง่าย บางครั้งรวมเป็น bulla |
| การกระจาย | สองข้าง ด้านข้างนิ้วกลาง-นิ้วชี้ ฝ่ามือ ฝ่าเท้า |
| หลังตุ่มแห้ง | ลอกเป็นขุยวงเล็ก (เสริม) |

### การวินิจฉัยแยก

- **Scabies** (ตุ่มที่ง่ามนิ้ว + burrow, คนในบ้านคัน) → skin scraping
- **Herpetic whitlow** (ตุ่มน้ำกลุ่มเดียว ปวด ที่ปลายนิ้วข้างเดียว) → Tzanck
- **Tinea manuum/pedis** (ขอบนูนขุย) → KOH
- ถ้า scabies และ Tzanck ลบ → dyshidrotic eczema

### การรักษา

- **Topical steroid** (ฝ่ามือผิวหนาต้องใช้ระดับ potent เช่น triamcinolone 0.1% ขึ้นไป (เสริม))
- **Oral steroid** กรณี severe
- เลี่ยง trigger ใช้ moisturizer (เสริม)
''',
    pearls=[
        "Deep-seated vesicle คันมาก สองข้าง ข้างนิ้ว ฝ่ามือฝ่าเท้า เป็นซ้ำ = dyshidrotic eczema",
        "รักษา topical steroid · severe ให้ oral steroid",
        "ต้องแยก scabies (scraping), herpetic whitlow (Tzanck), tinea (KOH)",
    ],
    items=[
        mcq("DERM-01-06-1", """A 40-year-old man presents with itchy vesicles on his hands. He has had the same problem many times. Examination shows deep-seated, tapioca-like papulovesicles along the lateral sides of the middle and index fingers of both hands. There are no burrows. What is the most likely diagnosis?""",
            "Dyshidrotic eczema", ["Atopic dermatitis", "Lichen simplex chronicus", "Herpetic whitlow", "Prurigo nodularis"],
            explain="""ตุ่มน้ำ **ฝังลึก คันมาก สองข้าง ที่ด้านข้างนิ้ว เป็นซ้ำหลายครั้ง** = **dyshidrotic eczema (pompholyx)** (สไลด์หน้า 36–38)
- Atopic dermatitis ในผู้ใหญ่เป็นผื่นที่ข้อพับ คอ ร่วมกับ atopy ไม่ใช่ตุ่มน้ำลึกเฉพาะข้างนิ้ว
- Lichen simplex chronicus เป็น plaque หนาจากการเกาซ้ำจุดเดียว ไม่มีตุ่มน้ำ
- Herpetic whitlow เป็นกลุ่มตุ่มน้ำที่ปวดมาก ที่ปลายนิ้วนิ้วเดียว ไม่ใช่สองข้างสมมาตร
- Prurigo nodularis เป็นตุ่มนูนแข็งจากการเกา (nodule) กระจายที่แขนขา ไม่ใช่ vesicle""",
            pearl="Deep-seated vesicle ข้างนิ้วสองข้าง เป็นซ้ำ = pompholyx",
            topic="Dyshidrotic dx", ref=[f"{D} หน้า 37–38"], nl=["2.3.12(8)"], kind="old", src=OLD),
        mcq("DERM-01-06-2", """A 17-year-old woman has recurrent itchy vesicles on her hands. Examination shows deep-seated papulovesicles at the lateral aspects of the middle and index fingers of both hands. Skin scraping for scabies and a Tzanck smear are negative. What is the most appropriate management?""",
            "Topical triamcinolone", ["Topical mupirocin", "Topical salicylic acid", "Topical acyclovir", "Topical ketoconazole"],
            explain="""เมื่อ scraping หา scabies และ Tzanck ลบแล้ว ผื่นนี้คือ **dyshidrotic eczema** — การรักษาหลักคือ **topical steroid** เช่น triamcinolone (สไลด์หน้า 36, 39–40)
- Mupirocin เป็นยาฆ่าเชื้อแบคทีเรีย ใช้กับ impetigo/folliculitis ไม่ได้ลดการอักเสบของ eczema
- Salicylic acid เป็น keratolytic ใช้กับหูด/ผิวหนา ระคายผิวที่อักเสบ
- Acyclovir ใช้กับ herpes ซึ่ง Tzanck ลบแล้ว และ acyclovir cream ก็ไม่แนะนำแม้ใน HSV
- Ketoconazole ใช้กับเชื้อรา ซึ่งผื่นนี้ไม่มีขอบนูนขุยแบบ tinea""",
            pearl="Pompholyx → topical steroid (triamcinolone)",
            topic="Dyshidrotic tx", ref=[f"{D} หน้า 39–40"], nl=["2.3.12(8)", "B4.4(7)"], kind="old", src=OLD),
        mcq("DERM-01-06-3", """A 33-year-old man has had several episodes of intensely itchy deep vesicles on both palms and soles, often worse in hot weather. During the current flare there are numerous coalescing vesicles and bullae on both palms and soles, making it hard to walk and work despite potent topical corticosteroid for 2 weeks. What is the most appropriate next step?""",
            "Add a short course of oral prednisolone", ["Start oral acyclovir", "Start oral terbinafine without testing", "Incise and drain each bulla", "Switch to a mild hydrocortisone 1% cream"],
            explain="""Dyshidrotic eczema ที่ **รุนแรง** (ตุ่มน้ำรวมเป็น bulla ทั้งฝ่ามือฝ่าเท้า ทำงานไม่ได้) และไม่ตอบสนองต่อ topical steroid → สไลด์ให้ **oral steroid กรณี severe** (สไลด์หน้า 36)
- Acyclovir ใช้กับ herpes ซึ่งจะเป็นกลุ่มตุ่มน้ำที่ปวด ไม่ใช่ตุ่มลึกคันสองข้างเป็นซ้ำ
- การให้ terbinafine โดยไม่ตรวจ KOH ไม่เหมาะ และตุ่มน้ำลึกสองข้างไม่ใช่ลักษณะของ tinea
- การเจาะทุกตุ่มเพิ่มโอกาสติดเชื้อ และไม่ได้รักษาการอักเสบ
- Hydrocortisone 1% อ่อนเกินไปสำหรับฝ่ามือที่หนา โดยเฉพาะเมื่อ potent steroid ยังไม่พอ""",
            pearl="Pompholyx รุนแรง/ดื้อ topical → oral steroid ระยะสั้น",
            topic="Dyshidrotic severe", ref=[f"{D} หน้า 36"], nl=["2.3.12(8)"]),
    ])

# ---------------------------------------------------------------- 01-07 Stasis + others
S7 = sec("derm-01-07", "Stasis dermatitis และ eczema อื่น ๆ (asteatotic, nummular, pityriasis alba, LSC)",
    "Stasis = chronic venous HT ที่ขาล่าง medial malleolus + varicose · asteatotic = ผิวแห้งแตกลายตาราง · nummular = วงเหรียญ · pityriasis alba = ด่างขาวขอบไม่ชัด · LSC = plaque หนาจากการเกา",
    minutes=6, source=f"{D} หน้า 41–47", nl=["2.3.12(7)", "B4.2.2(11)"],
    md='''
### Stasis dermatitis (venous eczema)

- **Cause: chronic venous hypertension** → ของเหลวและเม็ดเลือดแดงรั่วออกนอกหลอดเลือด → hemosiderin + การอักเสบ (เสริม)
- ผื่น eczema ได้ทุกระยะ ที่ **ขาส่วนล่าง โดยเฉพาะ medial malleolus** · **คัน**
- **Signs of chronic venous insufficiency**: **ขาบวม, หลอดเลือดดำผิวหน้าขยาย, varicose veins, venous ulcer**

| สิ่งที่เห็น | รายละเอียด |
|---|---|
| ตำแหน่ง | เหนือตาตุ่มด้านใน (medial ankle) สองข้าง |
| สี | น้ำตาลคล้ำ (hemosiderin), ขอบไม่ชัด |
| ระยะ chronic | lichenified plaque, ผิวแข็งตึง (lipodermatosclerosis (เสริม)) |
| ร่วม | varicose veins, pitting edema, แผลที่ medial malleolus |

- **Tx: topical steroid, moisturizer** + **รักษา CVI: ยกขาสูง, ใส่ support stocking**
- ระวัง ACD ซ้อนจากยาทา (neomycin) และ cellulitis (เสริม)

### Eczema อื่นที่ต้องรู้จักหน้าตา

| โรค | สิ่งที่เห็น | จุดแยก |
|---|---|---|
| **Asteatotic (xerotic) eczema** | **fine scale, crack & fissure** ลายแตกเหมือนดินแห้ง/กระเบื้อง | ผู้สูงอายุ หน้าแล้ง หน้าแข้ง อาบน้ำร้อน (เสริม) → moisturizer |
| **Nummular (discoid) eczema** | **วงกลมรูปเหรียญ (discoid)** ขอบชัด มี papulovesicle ซึม | ต่างจาก tinea ที่ขอบนูน ตรงกลางจาง (KOH ลบ) |
| **Pityriasis alba** | **ill-defined hypopigmented macule/patch** ขุยละเอียด ที่หน้าเด็ก | แยก **PV ด้วย KOH** · แยก **vitiligo ที่ขอบชัด สีขาวจั๊วะ + Wood lamp** |
| **Lichen simplex chronicus (LSC)** | **plaque + lichenification** จุดเดียว | เกาซ้ำที่เดิม (ต้นคอ ข้อเท้า แขน) (เสริม) |

> ด่างขาว 3 โรคที่โจทย์ชอบให้แยก: **pityriasis alba** (ขอบไม่ชัด เด็ก หน้า) · **pityriasis versicolor** (ขุยละเอียด หลัง-อก KOH spaghetti & meatballs) · **vitiligo** (ขาวจั๊วะ ขอบชัด Wood lamp ชัดขึ้น)
''',
    pearls=[
        "Stasis dermatitis = medial malleolus + varicose + edema → topical steroid + ยกขา + stocking",
        "Asteatotic = ผิวแห้งแตกเป็นลาย crack & fissure ในผู้สูงอายุ",
        "Nummular = วงเหรียญ · LSC = plaque หนาจากการเกาจุดเดิม",
        "Pityriasis alba ขอบไม่ชัด · vitiligo ขอบชัด Wood lamp · PV ต้อง KOH",
    ],
    items=[
        mcq("DERM-01-07-1", """A 60-year-old patient has had leg pruritus for 6 months. Examination shows symmetric, ill-defined, hyperpigmented, lichenified plaques on the medial side of both ankles, with multiple varicose veins and mild pitting edema of both legs. What is the most likely diagnosis?""",
            "Stasis (venous) eczema", ["Atopic dermatitis", "Shoe allergic contact dermatitis", "Asteatotic eczema", "Nummular eczema"],
            explain="""ผื่นคล้ำหนาที่ **medial ankle สองข้าง** ร่วมกับ **varicose veins และขาบวม** = **stasis dermatitis** จาก chronic venous hypertension (สไลด์หน้า 41–43)
- Atopic dermatitis ในผู้ใหญ่เป็นที่ข้อพับ คอ และมีประวัติ atopy ไม่สัมพันธ์กับ varicose veins
- Shoe dermatitis (ACD ต่อรองเท้า) เป็นที่หลังเท้าตามรูปรองเท้า ไม่ใช่เหนือตาตุ่มด้านใน
- Asteatotic eczema เป็นผิวแห้งแตกลายตารางที่หน้าแข้ง ไม่ได้หนาคล้ำร่วมกับ varicose veins
- Nummular eczema เป็นวงกลมรูปเหรียญขอบชัด กระจายที่แขนขา""",
            pearl="Medial malleolus + varicose + edema = stasis dermatitis",
            topic="Stasis dermatitis", ref=[f"{D} หน้า 42–43"], nl=["2.3.12(7)"], kind="old", src=OLD),
        mcq("DERM-01-07-2", """A 66-year-old woman with stasis dermatitis of both lower legs asks what will help besides her topical corticosteroid. She has varicose veins and ankle edema; ankle-brachial index is 1.0. What is the most appropriate additional measure?""",
            "Leg elevation and graduated compression stockings", ["Oral furosemide long term", "Topical neomycin cream", "Oral doxycycline for 3 months", "Strict bed rest without compression"],
            explain="""นอกจาก topical steroid/moisturizer แล้ว สไลด์ให้ **รักษา chronic venous insufficiency: ยกขาสูง ใส่ support stocking** เพื่อลด venous hypertension ซึ่งเป็นต้นเหตุ (สไลด์หน้า 41) · ABI ปกติจึงใส่ compression ได้ (เสริม)
- Furosemide ไม่ได้แก้ venous hypertension ใช้นานเสี่ยง electrolyte ผิดปกติ
- Neomycin เป็นสารก่อ ACD ที่พบบ่อยในขาที่มี stasis ทำให้ผื่นแย่ลง
- Doxycycline ไม่มีข้อบ่งชี้ เพราะไม่มีติดเชื้อ
- นอนพักโดยไม่ใส่ compression ไม่ใช่การรักษาระยะยาว และเพิ่มเสี่ยง DVT""",
            pearl="Stasis dermatitis: topical steroid + ยกขา + compression",
            topic="Stasis tx", ref=[f"{D} หน้า 41"], nl=["2.3.12(7)"]),
        mcq("DERM-01-07-3", """An 8-year-old boy has several ill-defined, slightly scaly, hypopigmented patches on both cheeks. They are asymptomatic and become more obvious after sun exposure. He has a history of mild atopic dermatitis. KOH preparation from the scale is negative. What is the most likely diagnosis?""",
            "Pityriasis alba", ["Vitiligo", "Pityriasis versicolor", "Tuberculoid leprosy", "Tinea faciei"],
            explain="""ด่างขาว **ขอบไม่ชัด ขุยละเอียด ที่แก้มเด็ก** ที่มี atopy และ **KOH ลบ** = **pityriasis alba** (สไลด์หน้า 46)
- Vitiligo เป็นด่างขาวจั๊วะ (depigmented) **ขอบชัด** ไม่มีขุย และเห็นชัดขึ้นด้วย Wood lamp
- Pityriasis versicolor มักอยู่ที่หลัง อก และ KOH จะเห็น spaghetti & meatballs ซึ่งโจทย์ลบ
- Tuberculoid leprosy เป็น plaque ขอบชัดนูน **ชา** ขนร่วง ไม่ใช่ปื้นจาง ๆ ที่แก้มสองข้าง
- Tinea faciei เป็นวงขอบนูนแดงมีขุย และ KOH พบ hyphae""",
            pearl="ด่างขาวขอบไม่ชัดที่หน้าเด็ก atopy + KOH ลบ = pityriasis alba",
            topic="Pityriasis alba", ref=[f"{D} หน้า 46"], nl=["2.3.12(7)"]),
        mcq("DERM-01-07-4", """A 78-year-old man has itchy shins every winter. He takes long hot showers twice daily. Examination of both anterior shins shows dry skin with fine scale and a network of superficial cracks and fissures resembling a dried riverbed. What is the most appropriate management?""",
            "Regular emollient, shorter lukewarm showers, and a short course of mild topical steroid if inflamed", ["Oral terbinafine", "Topical permethrin", "Oral antihistamine alone while continuing hot showers", "Oral isotretinoin"],
            explain="""ผิวแห้ง ขุยละเอียด แตกเป็นลายร่องในผู้สูงอายุหน้าหนาว = **asteatotic (xerotic) eczema** (สไลด์หน้า 44) · การดูแลคือเติมความชุ่มชื้น ลดการอาบน้ำร้อน และใช้ steroid อ่อนช่วงอักเสบ (เสริม)
- Terbinafine ใช้กับเชื้อรา ผื่นนี้ไม่มีขอบนูนแบบ tinea
- Permethrin ใช้กับ scabies ซึ่งจะเป็นตุ่มและ burrow ที่ง่ามนิ้ว คันกลางคืน
- Antihistamine อย่างเดียวไม่แก้ผิวแห้ง และการอาบน้ำร้อนต่อยิ่งทำลาย barrier
- Isotretinoin ทำให้ผิวแห้งมากขึ้น ใช้กับสิวรุนแรง""",
            pearl="Asteatotic = crack & fissure ผู้สูงอายุ → moisturizer",
            topic="Asteatotic eczema", ref=[f"{D} หน้า 44"], nl=["2.3.12(7)", "B4.4(1)"]),
    ])

LECTURE = lecture("01", "Eczema", subtitle="ICD · ACD · atopic · seborrheic · dyshidrotic · stasis · eczema อื่น ๆ",
    objectives=[
        "อ่านคำบรรยายผื่น (primary lesion, ระยะ eczema) แล้วนึกภาพออก",
        "แยก ICD กับ ACD ด้วยกลไก เวลา และขอบเขตผื่น และเลือก patch test ได้ถูก",
        "ใช้อายุ + ตำแหน่งผื่นแยก atopic, seborrheic, dyshidrotic และ stasis dermatitis",
        "เลือกการรักษาแต่ละชนิดตามสไลด์ (moisturizer, steroid, TCI, ketoconazole, compression)",
    ],
    sections=[S1, S2, S3, S4, S5, S6, S7])
