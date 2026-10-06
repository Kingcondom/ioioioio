from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Dermato"
OLD = "ตัวอย่างข้อสอบในสไลด์"


def body(cx, y, cls="box"):
    return (
        f'<circle cx="{cx}" cy="{y+20}" r="18" class="{cls}"/>'
        f'<rect x="{cx-7}" y="{y+37}" width="14" height="8" class="{cls}"/>'
        f'<rect x="{cx-30}" y="{y+44}" width="60" height="86" rx="12" class="{cls}"/>'
        f'<rect x="{cx-47}" y="{y+48}" width="15" height="100" rx="7" class="{cls}"/>'
        f'<rect x="{cx+32}" y="{y+48}" width="15" height="100" rx="7" class="{cls}"/>'
        f'<rect x="{cx-27}" y="{y+132}" width="24" height="116" rx="9" class="{cls}"/>'
        f'<rect x="{cx+3}" y="{y+132}" width="24" height="116" rx="9" class="{cls}"/>'
    )


# ---------------------------------------------------------------- 02-01 Psoriasis
F_DIST = fig("derm-02-01-f1", "แผนที่ผื่น: psoriasis (extensor) vs atopic (flexural) vs seborrheic (seborrheic area)", f'''<svg viewBox="0 0 740 350">
 <text x="125" y="22" text-anchor="middle" class="tb">Psoriasis</text>
 <text x="370" y="22" text-anchor="middle" class="tb">Atopic (ผู้ใหญ่)</text>
 <text x="615" y="22" text-anchor="middle" class="tb">Seborrheic</text>
 <g transform="translate(0,30)">{body(125, 6)}
  <path d="M107 12C115 0 135 0 143 12" class="lnbad"/>
  <rect x="73" y="92" width="22" height="16" rx="5" class="bad"/><rect x="155" y="92" width="22" height="16" rx="5" class="bad"/>
  <rect x="98" y="196" width="26" height="16" rx="5" class="bad"/><rect x="126" y="196" width="26" height="16" rx="5" class="bad"/>
  <rect x="112" y="122" width="26" height="12" rx="4" class="badsoft"/>
 </g>
 <g transform="translate(0,30)">{body(370, 6)}
  <rect x="355" y="40" width="30" height="10" rx="4" class="c1"/>
  <ellipse cx="331" cy="98" rx="9" ry="9" class="c1"/><ellipse cx="409" cy="98" rx="9" ry="9" class="c1"/>
  <ellipse cx="355" cy="196" rx="11" ry="9" class="c1"/><ellipse cx="385" cy="196" rx="11" ry="9" class="c1"/>
  <ellipse cx="331" cy="148" rx="9" ry="7" class="c1soft"/><ellipse cx="409" cy="148" rx="9" ry="7" class="c1soft"/>
 </g>
 <g transform="translate(0,30)">{body(615, 6)}
  <path d="M597 12C605 0 625 0 633 12" class="lnc2"/>
  <rect x="604" y="16" width="22" height="4" rx="2" class="c2"/>
  <path d="M606 30L610 38 M624 30L620 38" class="lnc2"/>
  <ellipse cx="596" cy="27" rx="3" ry="6" class="c2"/><ellipse cx="634" cy="27" rx="3" ry="6" class="c2"/>
  <rect x="603" y="60" width="24" height="18" rx="5" class="c2soft"/>
  <ellipse cx="595" cy="58" rx="7" ry="6" class="c2soft"/><ellipse cx="635" cy="58" rx="7" ry="6" class="c2soft"/>
 </g>
 <text x="125" y="300" text-anchor="middle" class="t2">scalp · ข้อศอก · เข่า · sacrum</text>
 <text x="125" y="318" text-anchor="middle" class="t3">plaque ขอบชัด ขุยเงินหนา</text>
 <text x="370" y="300" text-anchor="middle" class="t2">คอ · ข้อพับแขน · ข้อพับเข่า · มือ</text>
 <text x="370" y="318" text-anchor="middle" class="t3">ขอบไม่ชัด lichenified คันมาก</text>
 <text x="615" y="300" text-anchor="middle" class="t2">scalp · คิ้ว · ร่องจมูก · หลังหู · กลางอก</text>
 <text x="615" y="318" text-anchor="middle" class="t3">ขุยมันเหลือง คันน้อย</text>
 <text x="370" y="344" text-anchor="middle" class="t3">psoriasis = ด้านนอก (extensor) · atopic = ด้านใน (flexural) · seborrheic = ที่ที่ต่อมไขมันเยอะ</text>
</svg>''', "สามโรคที่เป็นผื่นแดงขุยเหมือนกัน แยกได้เร็วที่สุดด้วยตำแหน่ง — extensor, flexural หรือ seborrheic area")

F_SIGN = fig("derm-02-01-f2", "สัญญาณของ psoriasis ที่โจทย์บรรยายเป็นคำ", '''<svg viewBox="0 0 740 250">
 <rect x="10" y="10" width="230" height="230" rx="10" class="box"/>
 <text x="125" y="34" text-anchor="middle" class="tb">Auspitz sign</text>
 <path d="M30 120H70V96H180V120H220" class="ln"/>
 <path d="M76 96L90 84L120 86L150 82L174 96" class="lnf"/>
 <text x="125" y="76" text-anchor="middle" class="t3">แกะขุยเงินออก</text>
 <circle cx="96" cy="104" r="3" class="bad"/><circle cx="118" cy="106" r="3" class="bad"/><circle cx="140" cy="103" r="3" class="bad"/><circle cx="160" cy="106" r="3" class="bad"/>
 <text x="125" y="154" text-anchor="middle" class="t2">จุดเลือดออกเล็ก ๆ</text>
 <text x="125" y="174" text-anchor="middle" class="t3">(dermal papilla ที่เส้นเลือด</text>
 <text x="125" y="190" text-anchor="middle" class="t3">อยู่ใกล้ผิว)</text>
 <rect x="255" y="10" width="230" height="230" rx="10" class="box"/>
 <text x="370" y="34" text-anchor="middle" class="tb">Koebner phenomenon</text>
 <path d="M290 70L450 150" class="lnf"/>
 <text x="460" y="70" text-anchor="end" class="t3">รอยขีดข่วน</text>
 <path d="M290 80L450 160" class="lnbad"/>
 <path d="M292 84L448 164" class="lnbad"/>
 <text x="370" y="200" text-anchor="middle" class="t2">ผื่นใหม่ขึ้นเป็นเส้น</text>
 <text x="370" y="218" text-anchor="middle" class="t3">ตามแนว trauma</text>
 <rect x="500" y="10" width="230" height="230" rx="10" class="box"/>
 <text x="615" y="34" text-anchor="middle" class="tb">Nail psoriasis</text>
 <rect x="575" y="60" width="80" height="110" rx="30" class="sunk"/>
 <circle cx="598" cy="96" r="3" class="ln"/><circle cx="618" cy="88" r="3" class="ln"/><circle cx="634" cy="102" r="3" class="ln"/><circle cx="606" cy="114" r="3" class="ln"/>
 <ellipse cx="628" cy="132" rx="10" ry="7" class="misssoft"/>
 <path d="M580 70C600 64 630 64 650 70" class="lnf"/>
 <text x="615" y="192" text-anchor="middle" class="t2">pitting · oil spot</text>
 <text x="615" y="210" text-anchor="middle" class="t2">onycholysis (เล็บร่อน)</text>
</svg>''', "ขุยเงินที่แกะแล้วมีจุดเลือดออก (Auspitz), ผื่นตามรอยเกา (Koebner) และเล็บเป็นหลุม = psoriasis จนกว่าจะพิสูจน์ได้ว่าไม่ใช่")

S1 = sec("derm-02-01", "Psoriasis",
    "Plaque แดงขอบชัดขุยเงิน extensor + scalp · Auspitz, Koebner, nail pitting · ยากระตุ้น ACEI BB chloroquine lithium · <10% BSA topical steroid · ≥10% systemic (MTX) · ห้าม systemic steroid",
    minutes=9, source=f"{D} หน้า 48–63", nl=["2.3.12-3(11)", "B4.2.2-3(8)", "B4.4(3)"],
    md='''
### Papulosquamous disease คืออะไร

ผื่นนูน (papule/plaque) ที่มีขุย (scale) — **psoriasis, pityriasis rosea, pityriasis rubra pilaris, pityriasis lichenoides, mycosis fungoides, lichen planus** (สไลด์หน้า 48)

### กลไก (เสริม)

Immune-mediated (IL-17/IL-23, TNF) → keratinocyte แบ่งตัวเร็วมาก → ขุยหนาสีเงิน, เส้นเลือดใน dermal papilla ขยายใกล้ผิว (จึงเกิด Auspitz)

### Trigger (สไลด์หน้า 49)

- **บุหรี่ แอลกอฮอล์ skin trauma ความเครียด**
- ยา: **ACEI, beta-blockers, chloroquine (antimalarial), lithium** (+ การหยุด systemic steroid → flare)

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| Primary lesion | **well-defined erythematous plaque with silvery scale** (ขุยหนาสีเงิน) |
| ตำแหน่ง | **scalp, trunk, elbows, knees (extensor surfaces)**, sacrum, ก้น |
| การกระจาย | สองข้างค่อนข้างสมมาตร · ไม่ค่อยคัน (หรือคันเล็กน้อย) |
| Nail | **pitting, onycholysis, oil spot** |
| **Auspitz sign** | **แกะขุยออกแล้วพบจุดเลือดออก** |
| **Koebner phenomenon** | **ผื่นขึ้นตามบริเวณ trauma เช่น รอยขีดข่วน** |

[[fig:derm-02-01-f1]]

[[fig:derm-02-01-f2]]

### โรคที่สัมพันธ์

- **Psoriatic arthritis** (ข้อนิ้วปวดบวม, dactylitis, DIP)
- **HT, DM, DLP, metabolic syndrome** → ต้องคัดกรองโรคหัวใจหลอดเลือด

### ชนิด (สไลด์หน้า 52 เป็นภาพ — สรุปเสริม)

chronic plaque (vulgaris, พบบ่อยสุด) · guttate (ตุ่มหยดน้ำหลัง strep throat) · pustular · erythrodermic · inverse (ซอกพับ ไม่มีขุย)

### การรักษาตาม BSA (สไลด์หน้า 53)

| ระดับ | การรักษา |
|---|---|
| **Mild (< 10% BSA)** → topical | **topical steroid (1st line)**, **coal tar**, **calcipotriene** (vitamin D analog), topical calcineurin inhibitor, **anthralin** |
| **Moderate–severe (≥ 10% BSA)** → systemic + topical | **methotrexate, acitretin, cyclosporine, phototherapy, biologic agents** |

- **ห้ามใช้ systemic steroid** — หยุดแล้วกำเริบรุนแรง (rebound, อาจกลายเป็น pustular/erythrodermic psoriasis)
- มี **psoriatic arthritis** → เลือกยาที่คุมทั้งผิวและข้อ: **methotrexate** เป็นตัวแรก (เสริม: ไม่ตอบสนอง → biologic)
- Acitretin เป็น teratogen ห้ามตั้งครรภ์ 3 ปีหลังหยุด (เสริม)

> โจทย์ "ขุยที่ศีรษะ ข้อศอก ข้อเข่า เกาแล้วผื่นขึ้น แกะสะเก็ดเลือดออก" = Koebner + Auspitz = psoriasis
''',
    figs=[F_DIST, F_SIGN],
    pearls=[
        "Psoriasis = plaque แดงขอบชัดขุยเงิน ที่ข้อศอก เข่า scalp (extensor)",
        "Auspitz = แกะขุยมีจุดเลือด · Koebner = ผื่นตามรอย trauma · เล็บ pitting/oil spot",
        "ยากระตุ้น: ACEI, beta-blocker, chloroquine, lithium",
        "< 10% BSA topical steroid (1st) · ≥ 10% systemic เช่น MTX · ห้าม systemic steroid",
        "มี psoriatic arthritis → methotrexate",
    ],
    items=[
        mcq("DERM-02-01-1", """A 40-year-old patient has had a generalized rash for 2 years. Examination shows multiple well-demarcated, erythematous plaques covered with thick silvery-white scale on the elbows, knees, extensor forearms, lower legs, buttocks and scalp. Several fingernails show pitting. What is the most likely diagnosis?""",
            "Psoriasis vulgaris", ["Lichen planus", "Lichen simplex chronicus", "Atopic dermatitis", "Seborrheic dermatitis"],
            explain="""Plaque แดง **ขอบชัด ขุยเงินหนา** ที่ **ข้อศอก เข่า ด้าน extensor และ scalp** + เล็บเป็นหลุม = **psoriasis vulgaris** (สไลด์หน้า 49, 54–55)
- Lichen planus เป็นตุ่มแบนเหลี่ยมสีม่วงคันมาก (4P) มี Wickham striae ที่ข้อมือด้านใน ไม่ใช่ plaque ขุยเงินหนา
- Lichen simplex chronicus เป็น plaque หนาจากการเกาจุดเดียว ไม่กระจายสมมาตรทั่วตัว
- Atopic dermatitis ผู้ใหญ่ขึ้นที่ข้อพับ (flexural) คันมาก ขอบไม่ชัด
- Seborrheic dermatitis เป็นขุยมันเหลืองที่หน้า คิ้ว ร่องจมูก ไม่ใช่ข้อศอกข้อเข่า""",
            pearl="Plaque ขุยเงิน extensor + nail pitting = psoriasis",
            topic="Psoriasis dx", ref=[f"{D} หน้า 54–55"], nl=["2.3.12-3(11)"], kind="old", src=OLD),
        mcq("DERM-02-01-2", """A 44-year-old man has dry, scaly plaques on both elbows and the anterior knees. The lesions itch, and pinpoint bleeding appears when he picks off the scale. He also has pitting of the fingernails. Which of the following medications may worsen or exacerbate his condition?""",
            "Propranolol", ["Amlodipine", "Losartan", "Tramadol", "Procainamide"],
            explain="""ผู้ป่วยเป็น psoriasis (Auspitz sign + nail pitting) — ยาที่กระตุ้นตามสไลด์คือ **ACEI, beta-blockers, chloroquine, lithium** จึงตอบ **propranolol** (สไลด์หน้า 49, 58–59)
- Amlodipine (CCB) ไม่อยู่ในรายการยากระตุ้น psoriasis
- Losartan (ARB) ไม่ใช่ตัวกระตุ้นที่ยอมรับ ต่างจาก ACEI ที่อยู่ในรายการ
- Tramadol เป็นยาแก้ปวดที่ไม่ทำให้ psoriasis กำเริบ
- Procainamide ทำให้เกิด drug-induced lupus ไม่ใช่ psoriasis""",
            pearl="ยากระตุ้น psoriasis: ACEI, BB, chloroquine, lithium",
            topic="Psoriasis drug trigger", ref=[f"{D} หน้า 58–59"], nl=["2.3.12-3(11)"], kind="old", src=OLD),
        mcq("DERM-02-01-3", """A woman has scaly plaques on her scalp, knees and elbows, covering about 5% of her body surface area. New lesions appear along scratch marks, and removing the scale causes slight bleeding. She has no joint symptoms. Among the following, what is the most appropriate treatment?""",
            "Topical coal tar", ["Oral cloxacillin", "Oral prednisolone", "Topical bacitracin", "Topical ketoconazole"],
            explain="""ผื่นขุยที่ศีรษะ เข่า ศอก + Koebner (ผื่นตามรอยเกา) + Auspitz (แกะสะเก็ดเลือดออก) = psoriasis ระดับ **mild (< 10% BSA)** → ยาทา · ในตัวเลือกยาทาที่ใช้รักษา psoriasis คือ **coal tar** (สไลด์หน้า 53, 60–61) — ถ้ามี topical steroid ในตัวเลือก steroid คือ 1st line
- Oral cloxacillin ใช้กับติดเชื้อ S. aureus ไม่มีบทบาทใน psoriasis
- Oral prednisolone ห้ามใช้ใน psoriasis เพราะหยุดแล้วกำเริบรุนแรง
- Bacitracin เป็นยาฆ่าเชื้อแบคทีเรียทาเฉพาะที่ ไม่ลดการแบ่งตัวของ keratinocyte
- Ketoconazole ใช้กับ seborrheic dermatitis/เชื้อรา ไม่ใช่ plaque ขุยเงินที่ศอกเข่า""",
            pearl="Mild psoriasis = topical (steroid 1st, coal tar, calcipotriene)",
            topic="Psoriasis topical tx", ref=[f"{D} หน้า 60–61"], nl=["2.3.12-3(11)", "B4.4(3)"], kind="old", src=OLD),
        mcq("DERM-02-01-4", """A 30-year-old man who neither smokes nor drinks has had red scaly plaques on his back and scalp for 2 years. Over the last 2 months the plaques have spread to involve about 30% of his body, and he has intermittent painful swelling of several finger joints. What is the most appropriate first systemic treatment?""",
            "Methotrexate", ["Prednisolone", "Chloroquine", "Cyclophosphamide", "Biologic agent"],
            explain="""Psoriasis **≥ 10% BSA** ร่วมกับ **psoriatic arthritis** → ต้องให้ยา systemic ที่คุมทั้งผิวและข้อ ตัวแรกคือ **methotrexate** (สไลด์หน้า 53, 62–63)
- Prednisolone เป็น systemic steroid ที่ห้ามใช้ เพราะหยุดแล้วกำเริบรุนแรง อาจกลายเป็น pustular psoriasis
- Chloroquine เป็นยาที่กระตุ้นให้ psoriasis กำเริบ
- Cyclophosphamide ไม่ใช่ยารักษา psoriasis ใช้ใน vasculitis/lupus nephritis
- Biologic agent ได้ผลดีแต่ราคาสูง โดยทั่วไปใช้เมื่อไม่ตอบสนองหรือมีข้อห้ามต่อ conventional systemic อย่าง MTX ก่อน (เสริม)""",
            pearl="Psoriasis กว้าง + PsA → methotrexate",
            topic="Psoriasis systemic", ref=[f"{D} หน้า 62–63"], nl=["2.3.12-3(11)", "B4.4(3)"], kind="old", src=OLD),
        mcq("DERM-02-01-5", """A 52-year-old man with chronic plaque psoriasis on 15% of his body surface area was given oral prednisolone 40 mg/day by a clinic, and his skin cleared. One week after stopping it abruptly, he develops fever and widespread erythema studded with sheets of tiny sterile pustules. What is the most likely explanation?""",
            "Rebound flare of psoriasis into a pustular form after systemic steroid withdrawal", ["Acute generalized exanthematous pustulosis from prednisolone", "Disseminated herpes simplex infection", "Staphylococcal scalded skin syndrome", "Bacterial folliculitis caused by steroid immunosuppression"],
            explain="""สไลด์ย้ำว่า **ไม่ใช้ systemic steroid ใน psoriasis เพราะเมื่อหยุดจะกำเริบ** — การกำเริบรุนแรงหลังหยุด steroid อาจออกมาเป็น **generalized pustular psoriasis** ตุ่มหนองปลอดเชื้อทั่วตัวพร้อมไข้ (สไลด์หน้า 53; ชนิด pustular (เสริม))
- AGEP เกิด 1–4 วันหลัง **เริ่ม** ยา (เช่น antibiotic, CCB) ไม่ใช่หลังหยุด steroid
- Disseminated HSV จะเป็นตุ่มน้ำกลุ่ม/แผลกลม (punched-out) ไม่ใช่แผ่นตุ่มหนองเล็ก ๆ บนพื้นแดง
- SSSS เป็นผิวลอกจาก toxin ใน เด็ก/ไตเสื่อม ไม่มีตุ่มหนองแบบนี้
- Folliculitis เป็นตุ่มหนองที่รูขุมขนแยกกัน ไม่ได้เป็นแผ่นทั่วตัวพร้อมไข้""",
            pearl="Psoriasis + systemic steroid → หยุดแล้ว rebound (pustular/erythrodermic)",
            topic="Psoriasis steroid", ref=[f"{D} หน้า 53"], nl=["2.3.12-3(11)"]),
    ])

# ---------------------------------------------------------------- 02-02 PR, PRP, LP
F_PR = fig("derm-02-02-f1", "Pityriasis rosea: herald patch แล้วตามด้วยผื่นแนว Christmas tree", '''<svg viewBox="0 0 740 330">
 <rect x="230" y="20" width="200" height="290" rx="40" class="box"/>
 <path d="M330 30V300" class="lnf"/>
 <text x="330" y="16" text-anchor="middle" class="t3">แนวกระดูกสันหลัง</text>
 <ellipse cx="290" cy="110" rx="26" ry="16" class="bad" transform="rotate(-20 290 110)"/>
 <g class="badsoft">
  <ellipse cx="368" cy="80" rx="12" ry="6" transform="rotate(25 368 80)" class="badsoft"/>
  <ellipse cx="392" cy="100" rx="12" ry="6" transform="rotate(25 392 100)" class="badsoft"/>
  <ellipse cx="364" cy="130" rx="12" ry="6" transform="rotate(25 364 130)" class="badsoft"/>
  <ellipse cx="398" cy="150" rx="12" ry="6" transform="rotate(25 398 150)" class="badsoft"/>
  <ellipse cx="366" cy="180" rx="12" ry="6" transform="rotate(25 366 180)" class="badsoft"/>
  <ellipse cx="396" cy="205" rx="12" ry="6" transform="rotate(25 396 205)" class="badsoft"/>
  <ellipse cx="368" cy="235" rx="12" ry="6" transform="rotate(25 368 235)" class="badsoft"/>
  <ellipse cx="300" cy="160" rx="12" ry="6" transform="rotate(-25 300 160)" class="badsoft"/>
  <ellipse cx="268" cy="185" rx="12" ry="6" transform="rotate(-25 268 185)" class="badsoft"/>
  <ellipse cx="296" cy="210" rx="12" ry="6" transform="rotate(-25 296 210)" class="badsoft"/>
  <ellipse cx="264" cy="235" rx="12" ry="6" transform="rotate(-25 264 235)" class="badsoft"/>
  <ellipse cx="296" cy="260" rx="12" ry="6" transform="rotate(-25 296 260)" class="badsoft"/>
 </g>
 <path d="M340 70L420 130 M340 120L420 180 M340 170L420 230 M320 150L240 210 M320 200L240 260" class="lnf"/>
 <path d="M200 110H262" class="ln"/>
 <text x="20" y="104" class="tb">Herald patch</text>
 <text x="20" y="122" class="t3">วงรีใหญ่ 2–5 cm อันแรก</text>
 <text x="20" y="138" class="t3">collarette scale ขอบใน</text>
 <text x="450" y="70" class="tb">1–2 สัปดาห์ต่อมา</text>
 <text x="450" y="92" class="t2">ผื่นวงรีเล็กจำนวนมาก</text>
 <text x="450" y="112" class="t2">แกนยาวขนานแนวซี่โครง</text>
 <text x="450" y="132" class="t2">→ รูปต้นคริสต์มาส</text>
 <text x="450" y="170" class="tb">Collarette scale</text>
 <ellipse cx="500" cy="200" rx="40" ry="18" class="badsoft"/>
 <path d="M468 196C480 190 520 190 532 196" class="ln"/>
 <text x="450" y="240" class="t3">ขุยเป็นวงคล้ายปกเสื้อ</text>
 <text x="450" y="256" class="t3">ติดอยู่ด้านในของขอบผื่น</text>
 <text x="450" y="290" class="t2">หายเองใน 6–12 สัปดาห์</text>
</svg>''', "ผื่นแรกใหญ่ (herald) ตามด้วยผื่นวงรีเล็กที่แกนยาววางตามแนวซี่โครงทั้งสองข้างของหลัง — ภาพต้นคริสต์มาสกลับหัว")

S2 = sec("derm-02-02", "Pityriasis rosea และ papulosquamous อื่น (PRP, lichen planus)",
    "Prodrome คล้ายหวัด → herald patch → ผื่นวงรีขุย collarette แนว Christmas tree บนลำตัว · หายเอง 6–12 wk · LP = 4P + Wickham striae · PRP = islands of sparing",
    minutes=6, source=f"{D} หน้า 64–69", nl=["2.3.12-3(11)", "B4.2.2-3(8)"],
    md='''
### Pityriasis rosea (PR)

- พบในวัยรุ่น-ผู้ใหญ่ตอนต้น สัมพันธ์กับ HHV-6/7 reactivation (เสริม)
- **Prodrome: flu-like symptoms**
- **Initial: single ovoid macule/patch = herald patch** (ผื่นแรก ใหญ่สุด)
- ตามด้วย **multiple scaly ovoid papules/plaques แนว Christmas tree pattern บนลำตัว**

| หัวข้อ | สิ่งที่เห็น |
|---|---|
| Herald patch | วงรีสีชมพู-แดง 2–5 cm (เสริม) มี **collarette scale** |
| Secondary eruption | ผื่นวงรีเล็กจำนวนมาก **แกนยาวขนานแนวซี่โครง** บนหลัง-อก-ท้อง → **Christmas tree** |
| Scale | **collarette** — ขุยเป็นวงที่ขอบด้านใน |
| อาการ | คันได้บ้าง |

[[fig:derm-02-02-f1]]

- **Tx: หายเองใน 6–12 สัปดาห์** → **reassure** · คันให้ **moisturizer, topical steroid, antihistamine**
- Differential สำคัญ (เสริม): **secondary syphilis** (ผื่นที่ฝ่ามือฝ่าเท้า, ไม่มี herald patch, เสี่ยงทางเพศ → ตรวจ VDRL/RPR) · tinea corporis (ขอบนูน KOH +)

### Pityriasis rubra pilaris (PRP)

- ผื่นแดงส้มลามกว้างจนเกือบทั้งตัว แต่มีบริเวณผิวปกติเป็นเกาะ = **islands of sparing** + ตุ่มที่รูขุมขน, ฝ่ามือเท้าหนาสีส้ม (เสริม)

### Lichen planus (LP)

- **4P: Purple, Polygonal, Pruritic, Papule** (+ planar = ยอดแบน (เสริม))
- **Wickham striae** — ลายร่างแหสีขาวบนตุ่ม และในกระพุ้งแก้ม (เสริม)
- ตำแหน่งที่พบบ่อย: ข้อมือด้านใน หน้าแข้ง (เสริม) · มี Koebner ได้ · สัมพันธ์ HCV (เสริม)
''',
    figs=[F_PR],
    pearls=[
        "PR: prodrome → herald patch → ผื่นวงรี collarette scale แนว Christmas tree",
        "PR หายเองใน 6–12 สัปดาห์ → reassure ± ยาลดคัน",
        "ผื่นคล้าย PR แต่มีที่ฝ่ามือฝ่าเท้า ไม่มี herald patch → ตรวจ syphilis (เสริม)",
        "Lichen planus = 4P + Wickham striae · PRP = islands of sparing",
    ],
    items=[
        mcq("DERM-02-02-1", """A 30-year-old woman had a single oval pink patch with fine peripheral scale on her chest. One week later, many smaller oval, mildly itchy patches with collarette scale appeared on her chest, abdomen and back, with their long axes along the skin cleavage lines in a Christmas-tree pattern. Her palms and soles are spared. What is the most appropriate management?""",
            "Reassurance", ["Mupirocin ointment", "20% urea cream", "Clotrimazole cream", "Oral itraconazole"],
            explain="""Herald patch ตามด้วยผื่นวงรีขุย collarette แนว Christmas tree = **pityriasis rosea** ซึ่ง **หายเองใน 6–12 สัปดาห์** → **reassure** (ใช้ยาลดคันได้ถ้าคัน) (สไลด์หน้า 64, 66–67)
- Mupirocin ใช้กับ impetigo/folliculitis จากแบคทีเรีย ไม่เกี่ยวกับ PR
- Urea cream ใช้เพิ่มความชุ่มชื้นในผิวแห้ง/หนา ไม่ได้เปลี่ยนการดำเนินโรค
- Clotrimazole ใช้กับ tinea ซึ่งเป็นวงขอบนูนตรงกลางจาง ไม่ได้กระจายแนวซี่โครง
- Oral itraconazole ใช้กับเชื้อราระดับรุนแรง ไม่มีข้อบ่งชี้ใน PR""",
            pearl="PR → reassure (หายเอง 6–12 wk)",
            topic="PR treatment", ref=[f"{D} หน้า 66–67"], nl=["2.3.12-3(11)"], kind="old", src=OLD),
        mcq("DERM-02-02-2", """A 19-year-old man had sore throat and malaise one week before a 3-cm salmon-colored oval patch appeared on his flank. Ten days later, numerous smaller oval scaly patches erupted on his trunk. What is the name of the first lesion?""",
            "Herald patch", ["Koplik spot", "Satellite lesion", "Christmas tree lesion", "Target lesion"],
            explain="""ผื่นวงรีอันแรกที่ใหญ่ที่สุดของ pityriasis rosea เรียกว่า **herald patch** (สไลด์หน้า 64–65)
- Koplik spot เป็นจุดขาวเล็กบนกระพุ้งแก้มในหัด (measles)
- Satellite lesion คือตุ่มแดงเล็กที่อยู่รอบผื่นหลักของ candidiasis
- Christmas tree เป็นชื่อรูปแบบการเรียงตัวของผื่นชุดที่สอง ไม่ใช่ชื่อผื่นแรก
- Target lesion คือผื่นวงซ้อนกลางคล้ำของ erythema multiforme""",
            pearl="ผื่นแรกของ PR = herald patch",
            topic="Herald patch", ref=[f"{D} หน้า 64–65"], nl=["2.3.12-3(11)"]),
        mcq("DERM-02-02-3", """A 24-year-old man has a 2-week eruption of oval, scaly, pinkish papules on his trunk, which resembles pityriasis rosea. However, there was no initial larger patch, and there are also copper-colored scaly macules on both palms and soles. He had unprotected sex 2 months ago. What is the most appropriate next investigation?""",
            "Serum VDRL or RPR with treponemal confirmation", ["KOH preparation", "Skin prick test", "Tzanck smear", "No investigation; reassure as pityriasis rosea"],
            explain="""ผื่นคล้าย PR แต่ **ไม่มี herald patch และมีที่ฝ่ามือฝ่าเท้า** ร่วมกับมีเพศสัมพันธ์ไม่ป้องกัน ต้องนึกถึง **secondary syphilis** → ตรวจ **VDRL/RPR แล้วยืนยันด้วย treponemal test** (differential ของ PR (เสริม))
- KOH ใช้หาเชื้อรา (tinea) ซึ่งไม่อธิบายผื่นที่ฝ่ามือฝ่าเท้าร่วมกับความเสี่ยงทางเพศ
- Skin prick test ใช้หา IgE allergen ไม่ช่วยวินิจฉัยการติดเชื้อ
- Tzanck smear หา herpes ซึ่งจะเป็นตุ่มน้ำกลุ่ม
- การ reassure ว่าเป็น PR จะพลาดโรคที่รักษาได้และติดต่อได้""",
            pearl="คล้าย PR + ฝ่ามือฝ่าเท้า + เสี่ยงทางเพศ → VDRL/RPR",
            topic="PR mimic", ref=[f"{D} หน้า 64"], nl=["2.3.12-3(11)", "2.3.1(19)"]),
        mcq("DERM-02-02-4", """A 45-year-old woman with chronic hepatitis C has intensely itchy, flat-topped, polygonal, violaceous papules on the flexor wrists and shins. A fine lacy white network is seen on the surface of the papules and on the buccal mucosa. What is the most likely diagnosis?""",
            "Lichen planus", ["Psoriasis", "Pityriasis rosea", "Pityriasis rubra pilaris", "Lichen simplex chronicus"],
            explain="""ตุ่มแบน เหลี่ยม สีม่วง คันมาก (**4P: purple, polygonal, pruritic, papule**) และลายร่างแหขาว (**Wickham striae**) บนตุ่มและในปาก = **lichen planus** (สไลด์หน้า 69) · HCV สัมพันธ์กับ LP (เสริม)
- Psoriasis เป็น plaque แดงขุยเงินหนาที่ extensor ไม่ใช่ตุ่มม่วงเหลี่ยม
- Pityriasis rosea เป็นผื่นวงรีขุย collarette บนลำตัว ไม่มีรอยโรคในปาก
- PRP เป็นผื่นแดงส้มกว้างที่มี islands of sparing
- LSC เป็น plaque หนาจากการเกาจุดเดียว ไม่มี Wickham striae""",
            pearl="4P + Wickham striae = lichen planus",
            topic="Lichen planus", ref=[f"{D} หน้า 69"], nl=["2.3.12-3(11)"]),
    ])

# ---------------------------------------------------------------- 02-03 Acne
F_ACNE = fig("derm-02-03-f1", "บันไดการรักษาสิวตามสไลด์", '''<svg viewBox="0 0 740 300">
 <defs><marker id="derm-02-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="190" width="230" height="100" rx="10" class="oksoft"/>
 <text x="125" y="212" text-anchor="middle" class="tb">Mild</text>
 <text x="125" y="230" text-anchor="middle" class="t3">comedone เด่น (ไม่อักเสบ)</text>
 <text x="125" y="252" text-anchor="middle" class="t2">Topical retinoid</text>
 <text x="125" y="270" text-anchor="middle" class="t3">± topical ATB · azelaic · salicylic</text>
 <rect x="255" y="110" width="230" height="180" rx="10" class="misssoft"/>
 <text x="370" y="132" text-anchor="middle" class="tb">Moderate</text>
 <text x="370" y="150" text-anchor="middle" class="t3">papule/pustule เด่น nodule ไม่มาก</text>
 <text x="370" y="176" text-anchor="middle" class="t2">Topical retinoid</text>
 <text x="370" y="196" text-anchor="middle" class="t2">+ Oral ATB</text>
 <text x="370" y="216" text-anchor="middle" class="t3">doxycycline / macrolide</text>
 <rect x="500" y="30" width="230" height="260" rx="10" class="badsoft"/>
 <text x="615" y="52" text-anchor="middle" class="tb">Severe</text>
 <text x="615" y="70" text-anchor="middle" class="t3">nodule · cyst · scar</text>
 <text x="615" y="96" text-anchor="middle" class="t2">Oral isotretinoin</text>
 <text x="615" y="116" text-anchor="middle" class="t3">pregnancy category X</text>
 <text x="615" y="134" text-anchor="middle" class="t3">คุมกำเนิด + ตรวจครรภ์ (เสริม)</text>
 <path d="M130 180L250 120" class="lna" marker-end="url(#derm-02-03-a)"/>
 <path d="M380 100L495 50" class="lna" marker-end="url(#derm-02-03-a)"/>
 <text x="20" y="30" class="tb">Topical retinoid = แกนของทุกระดับ</text>
 <text x="20" y="50" class="t3">ห้ามใช้ antibiotic เดี่ยว ๆ (ดื้อยา) (เสริม)</text>
 <text x="20" y="68" class="t3">oral ATB ใช้ 3 เดือนแล้วประเมิน (เสริม)</text>
</svg>''', "ดูชนิดผื่นที่เด่นแล้วไต่บันได: comedone → retinoid ทา · papule/pustule → retinoid + oral ATB · nodule/cyst/scar → isotretinoin")

S3 = sec("derm-02-03", "Acne vulgaris",
    "Comedone (white/black) → papule/pustule → nodule/cyst · mild: topical retinoid ± topical ATB · moderate: retinoid + oral doxycycline/macrolide · severe: oral isotretinoin (cat X) · R/O PCOS",
    minutes=8, source=f"{D} หน้า 70–80", nl=["2.3.12(1)", "B4.2.2(1)", "B4.4(5)"],
    md='''
### กลไก (เสริม)

4 ขั้น: ต่อมไขมันผลิต sebum มาก (androgen) → keratin อุดรูขุมขน (comedone) → **Cutibacterium (Propionibacterium) acnes** เจริญ → การอักเสบ

### ใครเป็น / ปัจจัยเสี่ยง (สไลด์หน้า 70)

- **วัยรุ่นและผู้ใหญ่ตอนต้น**
- Risk: **ฮอร์โมน อดนอน เครียด อาหาร high glycemic index ยา และสุขอนามัย**
- **R/O PCOS** เมื่อมี สิว + ผิวมัน + ขนดก + ประจำเดือนไม่สม่ำเสมอ

### สิ่งที่เห็น

| ชนิด | ลักษณะ |
|---|---|
| **Closed comedone (whitehead)** | ตุ่มเล็กสีเนื้อ-ขาว รูปิด |
| **Open comedone (blackhead)** | รูเปิดมีจุดดำตรงกลาง (oxidized keratin) |
| **Inflammatory: papule / pustule** | ตุ่มแดง / ตุ่มหนอง |
| **Nodule / cyst** | ก้อนลึกเจ็บ ≥ 5 mm (เสริม) / ถุงมีหนองลึก |
| แผลเป็น | **hypertrophic/atrophic scar**, **hyperpigmentation** |

- **Multistage lesion** — เห็นหลายระยะพร้อมกัน · ตำแหน่ง **หน้า ไหล่ อกส่วนบน หลัง**
- **Drug-induced acne** (steroid, isoniazid, lithium, phenytoin (เสริม)) → **monomorphic lesion** (ตุ่มหน้าตาเหมือนกันหมด ไม่มี comedone)

### การรักษา (สไลด์หน้า 72)

[[fig:derm-02-03-f1]]

| ระดับ | ลักษณะเด่น | ยา |
|---|---|---|
| **Mild** | **non-inflammatory acne (comedone)** เด่น | **topical retinoid (adapalene, tretinoin)** ± topical ATB (clindamycin, erythromycin) · azelaic acid, salicylic acid |
| **Moderate** | **inflammatory acne เด่น** nodule ไม่มาก | **topical retinoid + oral ATB (doxycycline, macrolide)** |
| **Severe** | **inflammatory + nodules + cysts** (scar) | **oral isotretinoin** (**pregnancy category X**) |

- เสริม: ใช้ benzoyl peroxide ร่วมกับ antibiotic ทุกครั้งเพื่อลดดื้อยา · isotretinoin ต้องคุมกำเนิด ตรวจ pregnancy test, lipid, LFT · ห้ามใช้ร่วมกับ tetracycline (pseudotumor cerebri)
''',
    figs=[F_ACNE],
    pearls=[
        "Comedone = mild → topical retinoid (adapalene, tretinoin)",
        "Papule/pustule เด่น = moderate → topical retinoid + oral doxycycline/macrolide",
        "Nodule/cyst/scar = severe → oral isotretinoin (category X)",
        "สิว + ขนดก + ประจำเดือนไม่สม่ำเสมอ → R/O PCOS",
        "Drug-induced acne = monomorphic ไม่มี comedone",
    ],
    items=[
        mcq("DERM-02-03-1", """An 18-year-old woman has had recurrent non-itchy bumps on her face for 1 year. Examination shows multiple open and closed comedones on the forehead and cheeks, with no inflammatory papules or pustules. What is the most appropriate management?""",
            "Topical tretinoin", ["1% clindamycin solution alone", "4% erythromycin gel alone", "Oral isotretinoin", "Oral doxycycline"],
            explain="""Comedone ล้วน = **mild (non-inflammatory) acne** → 1st line คือ **topical retinoid** เช่น tretinoin หรือ adapalene ซึ่งแก้การอุดตันของรูขุมขน (สไลด์หน้า 72–74) · ในสไลด์ตัวเลือกเขียน "0.25% tretinoic acid" ความเข้มข้นที่ใช้จริงคือ 0.025–0.05% (เสริม)
- Clindamycin ทาเดี่ยว ๆ ไม่แก้ comedone และเสี่ยงดื้อยา เป็นได้แค่ส่วนเสริม (±) ของ retinoid
- Erythromycin gel เดี่ยว ๆ ก็มีปัญหาเดียวกัน — antibiotic ไม่ใช่แกนของสิวอุดตัน
- Oral isotretinoin สำรองไว้สำหรับสิว nodule/cyst รุนแรง
- Oral doxycycline ใช้ในสิวอักเสบระดับ moderate ไม่ใช่ comedone ล้วน""",
            pearl="Comedone → topical retinoid",
            topic="Mild acne", ref=[f"{D} หน้า 73–74"], nl=["2.3.12(1)", "B4.4(5)"], kind="old", src=OLD),
        mcq("DERM-02-03-2", """A 16-year-old boy has a facial rash. Examination shows multiple blackheads and whiteheads with a moderate number of erythematous papules and pustules on the forehead and both cheeks. There are no nodules or cysts. What is the most appropriate management?""",
            "Topical adapalene plus oral doxycycline", ["Oral cetirizine", "Oral doxycycline alone", "Topical mupirocin", "Topical triamcinolone"],
            explain="""มี comedone ร่วมกับ **papule/pustule อักเสบเด่น** = **moderate acne** → **topical retinoid + oral ATB (doxycycline, macrolide)** (สไลด์หน้า 72, 75–76)
- Cetirizine เป็น antihistamine ไม่มีบทบาทในสิว
- Doxycycline เดี่ยว ๆ ไม่แก้ comedone และเสี่ยงดื้อยา ต้องคู่กับ topical retinoid
- Mupirocin ใช้กับ impetigo/folliculitis จาก S. aureus ไม่ใช่ C. acnes
- Triamcinolone ทาหน้าทำให้เกิด steroid acne และผิวบาง""",
            pearl="Moderate acne → topical retinoid + oral doxycycline",
            topic="Moderate acne", ref=[f"{D} หน้า 75–76"], nl=["2.3.12(1)", "B4.4(5)"], kind="old", src=OLD),
        mcq("DERM-02-03-3", """A 20-year-old woman presents with small papules, a few pustules and one small nodule on her face, along with scattered closed comedones. Which of the following agents should form the backbone of her treatment regimen?""",
            "Topical tretinoin", ["Topical mupirocin", "Topical corticosteroid", "Topical clindamycin alone", "Oral clindamycin"],
            explain="""สิวอักเสบระดับ moderate (papule/pustule เด่น nodule ไม่มาก) — สไลด์ให้ **topical retinoid + oral ATB (doxycycline, macrolide)** · ในตัวเลือกไม่มีชุดผสม จึงเลือก **topical retinoid (tretinoin)** ซึ่งเป็นแกนของการรักษาสิวทุกระดับ แล้วเพิ่ม doxycycline (สไลด์หน้า 72, 77–78) · เฉลยในสไลด์เป็นภาพ อ่านไม่ได้ — ตอบตามหลักฐานปัจจุบัน
- Mupirocin ไม่ครอบคลุม C. acnes และไม่ใช่ยาสิว
- Topical steroid ทำให้สิวแย่ลง (steroid acne)
- Clindamycin ทาเดี่ยว ๆ ทำให้ดื้อยาและไม่แก้ comedone
- Oral clindamycin ไม่ใช่ oral ATB มาตรฐานของสิว (ใช้ doxycycline/macrolide) และเสี่ยง C. difficile colitis""",
            pearl="Topical retinoid = backbone ของการรักษาสิวทุกระดับ",
            topic="Moderate acne", ref=[f"{D} หน้า 77–78"], nl=["2.3.12(1)", "B4.4(5)"], kind="old", src=OLD),
        mcq("DERM-02-03-4", """A 17-year-old boy has multiple erythematous papules, pustules, painful cysts and nodules on his face and back, with atrophic scars on the lateral forehead. Twelve weeks of topical adapalene plus oral doxycycline has failed. What is the most appropriate treatment?""",
            "Oral isotretinoin", ["Increase doxycycline dose and continue for 6 more months", "Oral prednisolone", "Topical clindamycin added to the current regimen", "Intralesional steroid injection of every lesion as monotherapy"],
            explain="""สิว **nodule/cyst + แผลเป็น** = **severe acne** → **oral isotretinoin** (สไลด์หน้า 72, 79–80) โดยเฉพาะเมื่อยา oral ATB ไม่ได้ผล · ต้องระวัง teratogen (category X) (ผู้ชายไม่ต้องคุมกำเนิดแต่ต้องเฝ้าระวัง lipid, LFT, อารมณ์ (เสริม))
- การเพิ่มขนาด doxycycline และใช้นานขึ้นเพิ่มการดื้อยา และไม่ได้ผลกับ nodulocystic acne
- Prednisolone ไม่ใช่การรักษาสิว (ใช้ระยะสั้นเฉพาะ acne fulminans (เสริม))
- Topical clindamycin ไม่เพิ่มประสิทธิภาพพอสำหรับ cyst ลึก
- Intralesional steroid ช่วยลดก้อนที่ใหญ่บางก้อน แต่ไม่ใช่การรักษาหลักของสิวทั้งหน้าและหลัง""",
            pearl="Nodule/cyst/scar → oral isotretinoin",
            topic="Severe acne", ref=[f"{D} หน้า 79–80"], nl=["2.3.12(1)", "B4.4(5)"], kind="old", src=OLD),
        mcq("DERM-02-03-5", """A 24-year-old woman has persistent inflammatory acne on her lower face and jawline, oily skin, coarse hair on her upper lip and chin, and menstrual cycles every 45–90 days. BMI is 29 kg/m2. Before choosing further acne treatment, which condition should be evaluated?""",
            "Polycystic ovary syndrome", ["Cushing syndrome caused by topical steroid", "Hypothyroidism", "Drug-induced acne from oral contraceptives", "Rosacea"],
            explain="""สไลด์ระบุให้ **R/O PCOS** เมื่อมี **สิว + ผิวมัน + ขนดก + ประจำเดือนไม่สม่ำเสมอ** — ภาวะ hyperandrogenism ทำให้สิวไม่ตอบสนอง และอาจต้องใช้ฮอร์โมนรักษา (สไลด์หน้า 70)
- Cushing จากยาทาไม่สอดคล้อง เพราะไม่มีประวัติใช้ steroid และไม่มีลักษณะ Cushingoid
- Hypothyroidism ทำให้ประจำเดือนผิดปกติได้ แต่ไม่ทำให้ขนดกและสิวแบบ androgen
- Drug-induced acne เป็น monomorphic และโจทย์ไม่ได้บอกว่าใช้ยาคุม (ยาคุมส่วนใหญ่กลับช่วยสิว)
- Rosacea เป็นหน้าแดง เส้นเลือดฝอย papule/pustule กลางหน้า ไม่มี comedone และไม่สัมพันธ์กับ androgen""",
            pearl="สิว + ขนดก + ประจำเดือนไม่สม่ำเสมอ → R/O PCOS",
            topic="Acne & PCOS", ref=[f"{D} หน้า 70"], nl=["2.3.12(1)"]),
    ])

LECTURE = lecture("02", "Papulosquamous & acne", subtitle="psoriasis · pityriasis rosea · lichen planus/PRP · acne vulgaris",
    objectives=[
        "จำผื่น psoriasis และ sign ที่โจทย์บรรยาย (Auspitz, Koebner, nail pitting) และยาที่กระตุ้น",
        "เลือกการรักษา psoriasis ตาม BSA และรู้ว่าห้าม systemic steroid",
        "วินิจฉัย pityriasis rosea จาก herald patch + Christmas tree และรู้ว่า reassure",
        "จัดระดับสิว (comedone / inflammatory / nodulocystic) แล้วเลือกยาตามบันได",
    ],
    sections=[S1, S2, S3])
