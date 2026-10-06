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


# ---------------------------------------------------------------- KOH figure
F_KOH = fig("derm-07-01-f1", "KOH preparation: เชื้อราผิวหนัง 3 แบบที่ต้องแยกให้ได้ (schematic)", '''<svg viewBox="0 0 740 330">
 <rect x="10" y="10" width="230" height="310" rx="10" class="box"/>
 <text x="125" y="34" text-anchor="middle" class="tb">Pityriasis versicolor</text>
 <circle cx="125" cy="130" r="80" class="sunk"/>
 <path d="M70 100Q85 92 100 104 M140 90Q156 98 168 88 M80 160Q96 150 110 164 M150 150Q162 160 178 152 M108 124Q120 116 132 128" class="lnc2"/>
 <circle cx="96" cy="128" r="7" class="c2"/><circle cx="104" cy="120" r="6" class="c2"/><circle cx="150" cy="118" r="7" class="c2"/>
 <circle cx="130" cy="170" r="7" class="c2"/><circle cx="122" cy="178" r="6" class="c2"/><circle cx="160" cy="176" r="6" class="c2"/>
 <circle cx="88" cy="186" r="6" class="c2"/>
 <text x="125" y="236" text-anchor="middle" class="t2">hyphae สั้นหัก + ยีสต์กลมผนังหนา</text>
 <text x="125" y="258" text-anchor="middle" class="ta">"spaghetti &amp; meatballs"</text>
 <text x="125" y="282" text-anchor="middle" class="t3">Malassezia furfur</text>
 <rect x="255" y="10" width="230" height="310" rx="10" class="box"/>
 <text x="370" y="34" text-anchor="middle" class="tb">Dermatophyte (tinea)</text>
 <circle cx="370" cy="130" r="80" class="sunk"/>
 <path d="M310 100H350V128H400V150H430" class="lnc1"/>
 <path d="M330 100V92 M350 116H342 M370 128V120 M390 128V136 M400 140H408 M416 150V158" class="lnc1"/>
 <rect x="408" y="146" width="10" height="8" rx="2" class="c1"/><rect x="420" y="146" width="10" height="8" rx="2" class="c1"/>
 <path d="M320 170H380V190H420" class="lnc1"/>
 <path d="M340 166V174 M360 166V174 M380 180H372 M400 186V194" class="lnc1"/>
 <text x="370" y="236" text-anchor="middle" class="t2">hyphae ยาวแตกแขนง มีผนังกั้น</text>
 <text x="370" y="258" text-anchor="middle" class="ta">septate hyphae + arthroconidia</text>
 <text x="370" y="282" text-anchor="middle" class="t3">Trichophyton · Microsporum</text>
 <text x="370" y="298" text-anchor="middle" class="t3">Epidermophyton</text>
 <rect x="500" y="10" width="230" height="310" rx="10" class="box"/>
 <text x="615" y="34" text-anchor="middle" class="tb">Candida</text>
 <circle cx="615" cy="130" r="80" class="sunk"/>
 <ellipse cx="560" cy="110" rx="9" ry="7" class="miss"/><ellipse cx="572" cy="102" rx="6" ry="5" class="miss"/>
 <ellipse cx="640" cy="90" rx="9" ry="7" class="miss"/><ellipse cx="652" cy="82" rx="6" ry="5" class="miss"/>
 <path d="M574 140C590 140 594 132 608 132C622 132 626 142 640 142C654 142 656 136 668 136" class="lnbad"/>
 <path d="M594 136V144 M622 138V146 M650 138V146" class="lnf"/>
 <ellipse cx="590" cy="180" rx="9" ry="7" class="miss"/><ellipse cx="600" cy="172" rx="6" ry="5" class="miss"/>
 <text x="615" y="236" text-anchor="middle" class="t2">ยีสต์แตกหน่อ + pseudohyphae</text>
 <text x="615" y="258" text-anchor="middle" class="ta">budding yeast + pseudohyphae</text>
 <text x="615" y="282" text-anchor="middle" class="t3">pseudohyphae คอดตรงรอยต่อ (ไส้กรอก)</text>
</svg>''', "KOH 10–20% ละลาย keratin เหลือแต่เชื้อ — สั้นหัก + ยีสต์กลม = PV · เส้นยาวมีผนังกั้น = tinea · ยีสต์แตกหน่อ + เส้นคอดเป็นข้อ = candida")

# ---------------------------------------------------------------- 07-01 PV
S1 = sec("derm-07-01", "Pityriasis versicolor (tinea versicolor)",
    "Malassezia furfur (flora ปกติ ไม่ติดต่อ) · ร้อนชื้น เหงื่อ · ด่างขาว/น้ำตาลขุยละเอียดที่ลำตัว อก หลัง · KOH spaghetti & meatballs · topical keto/selenium/zinc/ciclopirox · กว้าง: oral fluconazole/itraconazole",
    minutes=6, source=f"{D} หน้า 221–226", nl=["2.3.12(11)", "B4.2.2(9)", "B4.3(1)"],
    md='''
### กลไก

- **Malassezia furfur** — ยีสต์ที่เป็น **normal skin flora, ไม่ติดต่อ** · เปลี่ยนเป็นรูป hyphae เมื่อสภาพเหมาะ
- **Risk: อากาศร้อนชื้น เหงื่อออกมาก** (คนไทย วัยรุ่น นักกีฬา)
- สร้าง azelaic acid ยับยั้ง melanocyte → ด่างขาว (เสริม)

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| Primary lesion | **hypo- หรือ hyperpigmented macules with fine scale** (ขุยละเอียดคล้ายแป้ง เห็นชัดเมื่อขูด) |
| การกระจาย | **ลำตัว อก หลัง** ต้นแขน คอ |
| รูปแบบ | วงเล็ก ๆ รวมกันเป็นปื้นขอบไม่เรียบ ไม่คัน/คันเล็กน้อยเมื่อเหงื่อออก |
| Wood lamp (เสริม) | สีเหลืองทอง |

### Investigation

- **KOH: short fragmented hyphae + thick-walled yeast cells = "spaghetti & meatballs"**

[[fig:derm-07-01-f1]]

### การรักษา

- **Topical antifungals (1st line)**: **ketoconazole, selenium sulfide, zinc pyrithione, ciclopirox shampoo** (ฟอกทิ้งไว้ 5–10 นาทีก่อนล้าง (เสริม))
- **Oral antifungal กรณี severe/widespread**: **fluconazole, itraconazole** (ไม่ใช้ griseofulvin และ oral terbinafine ซึ่งไม่ได้ผลกับ Malassezia (เสริม))
- สีผิวกลับมาปกติช้าหลายเดือน แม้เชื้อหายแล้ว · เป็นซ้ำบ่อย (เสริม)

> ด่างขาวที่หลัง-อก ขุยละเอียด KOH spaghetti & meatballs = PV → **ketoconazole/selenium shampoo** (ไม่ใช่ griseofulvin, steroid)
''',
    figs=[F_KOH],
    pearls=[
        "PV = Malassezia furfur, flora ปกติ ไม่ติดต่อ, ร้อนชื้นเหงื่อออก",
        "ด่างขาว/น้ำตาลขุยละเอียดที่ลำตัว อก หลัง",
        "KOH = spaghetti & meatballs",
        "Topical keto/selenium/zinc/ciclopirox · กว้าง: oral fluconazole/itraconazole",
    ],
    items=[
        mcq("DERM-07-01-1", """A Thai man has ill-defined hypopigmented macules with fine, powdery scale on his back and anterior chest. KOH preparation from the scale shows short fragmented hyphae with clusters of round yeast cells (spaghetti-and-meatball appearance). What is the most appropriate management?""",
            "Ketoconazole shampoo applied to the affected skin", ["Oral griseofulvin", "Urea cream", "Triamcinolone cream", "Liquor carbonis detergens ointment"],
            explain="""KOH spaghetti & meatballs = **pityriasis versicolor** → 1st line **topical antifungal เช่น ketoconazole shampoo** (หรือ selenium sulfide, zinc pyrithione) (สไลด์หน้า 222–224)
- Griseofulvin ไม่ได้ผลกับ Malassezia ใช้กับ dermatophyte (tinea capitis)
- Urea cream เป็น moisturizer ไม่ฆ่าเชื้อ
- Triamcinolone เป็น steroid ทำให้เชื้อราเพิ่มขึ้น
- Liquor carbonis (coal tar) ใช้รักษา psoriasis""",
            pearl="PV → ketoconazole/selenium shampoo",
            topic="PV tx", ref=[f"{D} หน้า 223–224"], nl=["2.3.12(11)"], kind="old", src=OLD),
        mcq("DERM-07-01-2", """A 21-year-old male athlete has many small hypopigmented macules with fine scale coalescing on his upper back and shoulders. They are more noticeable after sun exposure and mildly itchy when he sweats. What is the best next step in management?""",
            "Selenium sulfide lotion or shampoo", ["No treatment is indicated", "Benzathine penicillin", "Triamcinolone cream", "Narrowband UVB phototherapy"],
            explain="""ด่างขาวขุยละเอียดที่หลังส่วนบนในคนเหงื่อออกมาก = **pityriasis versicolor** → **selenium sulfide** (topical antifungal) (สไลด์หน้า 221–222, 225–226)
- การไม่รักษาไม่เหมาะ เพราะผื่นจะลามและผู้ป่วยมีอาการ รักษาได้ง่าย
- Penicillin รักษา syphilis ซึ่งผื่นจะไม่เป็นขุยแป้งที่หลังแบบนี้
- Triamcinolone ทำให้เชื้อราลาม
- UVB ใช้รักษา vitiligo/psoriasis ไม่ใช่เชื้อรา""",
            pearl="PV → selenium sulfide / ketoconazole",
            topic="PV tx", ref=[f"{D} หน้า 225–226"], nl=["2.3.12(11)"], kind="old", src=OLD),
        mcq("DERM-07-01-3", """A 26-year-old woman asks whether her pityriasis versicolor can spread to her husband and why the white patches persist 2 months after successful treatment with a negative KOH. Which statement is correct?""",
            "Malassezia is normal skin flora, so the condition is not contagious, and pigment takes months to return after the fungus is cleared", ["It is highly contagious through skin contact, so her husband should be treated too", "Persistent white patches mean treatment failure and require oral griseofulvin", "The patches are vitiligo triggered by the fungus and need phototherapy", "The condition will not recur once treated"],
            explain="""Malassezia เป็น **normal skin flora → ไม่ติดต่อ** (สไลด์หน้า 221) · ด่างขาวคงอยู่หลังเชื้อหายเพราะ melanocyte ต้องใช้เวลาฟื้น (เสริม)
- PV ไม่ติดต่อ จึงไม่ต้องรักษาคู่สมรส
- KOH ลบแล้วแปลว่าเชื้อหาย ไม่ใช่ล้มเหลว และ griseofulvin ไม่ได้ผลกับ Malassezia
- ด่างนี้ไม่ใช่ vitiligo — vitiligo ขาวจั๊วะขอบชัด ไม่มีขุย
- PV เป็นซ้ำบ่อยในอากาศร้อนชื้น อาจต้องใช้ยาป้องกันเป็นระยะ (เสริม)""",
            pearl="PV ไม่ติดต่อ · สีกลับช้าหลายเดือน · เป็นซ้ำบ่อย",
            topic="PV counselling", ref=[f"{D} หน้า 221"], nl=["2.3.12(11)"]),
    ])

# ---------------------------------------------------------------- 07-02 Tinea
S2 = sec("derm-07-02", "Dermatophyte infection (tinea)",
    "Trichophyton, Microsporum, Epidermophyton · วงขอบนูนแดงมีขุย ตรงกลางจาง ลามออก · KOH septate hyphae + arthroconidia · capitis/unguium ต้อง oral (+ topical) · ที่อื่น topical clotrimazole/ketoconazole",
    minutes=8, source=f"{D} หน้า 227–236", nl=["2.3.12(11)", "B4.2.2(9)", "B4.3(1)"],
    md='''
### เชื้อและการติดต่อ

- **Dermatophytes: Trichophyton, Microsporum, Epidermophyton** — กิน keratin (ผิว ผม เล็บ)
- ติดต่อทาง **สัมผัสคนหรือสัตว์ที่ติดเชื้อ** (ลูกหมา ลูกแมว → Microsporum canis (เสริม))

### สิ่งที่เห็น

- **Annular lesion with active border** — **ขอบชัด นูน แดง มีขุย** ตรงกลางจางลง (**central clearing**) ลามออกไปเรื่อย ๆ
- แต่ละตำแหน่งลักษณะต่างกัน (สไลด์หน้า 228)

| ชื่อ | ตำแหน่ง | ลักษณะเพิ่ม (เสริม) |
|---|---|---|
| **Tinea capitis** | หนังศีรษะ | ผมร่วงเป็นหย่อมขุย ผมหัก (black dot) · kerion = ก้อนบวมเป็นหนอง |
| **Tinea barbae** | เครา | ตุ่มหนองที่รูขุมขน |
| **Tinea corporis** | ลำตัว แขนขา | วงขอบนูน (ringworm) |
| **Tinea manuum** | มือ (มักข้างเดียว) | ฝ่ามือหนาขุยแห้ง |
| **Tinea unguium** (onychomycosis) | เล็บ | เล็บหนา ขุ่นเหลือง ยุ่ย |
| **Tinea cruris** | ขาหนีบ | วงขอบนูนลามไปต้นขา **ไม่ลงถุงอัณฑะ** |
| **Tinea pedis** | เท้า | ง่ามนิ้วเท้าเปื่อยลอก (interdigital) |

### Investigation

- **KOH: hyaline septate hyphae with arthroconidia** (ดูภาพใน PV)

### การรักษา (สไลด์หน้า 230)

| ตำแหน่ง | การรักษา |
|---|---|
| **Tinea capitis** | **oral antifungal: griseofulvin, terbinafine, itraconazole, fluconazole** **+ ketoconazole/selenium sulfide shampoo** |
| **Tinea unguium** | **oral terbinafine, itraconazole, fluconazole** **+ topical efinaconazole, ciclopirox nail lacquer** |
| **Tinea ที่อื่น** | **topical antifungal: clotrimazole, ketoconazole cream** (ทาเลยขอบผื่น 2 cm นาน 2–4 สัปดาห์ (เสริม)) |

- **Tinea capitis/unguium: ยาทาอย่างเดียวไม่พอ** (ยาไม่ซึมถึงรากผมและแผ่นเล็บ)
- **ห้ามใช้ topical steroid** — ทำให้ผื่นลามและเปลี่ยนหน้าตา (tinea incognito) (เสริม)
- Oral ketoconazole ไม่ใช้แล้วเพราะพิษต่อตับ (เสริม)

> Tinea (ขอบนูน กลางจาง KOH septate hyphae) vs candida (แดงสด ไม่มี central clearing มี satellite papule KOH budding yeast) vs nummular eczema (วงเหรียญ KOH ลบ) vs TT leprosy (วงชา)
''',
    pearls=[
        "Tinea = วงขอบนูนแดงขุย ตรงกลางจาง ลามออก",
        "KOH = septate hyphae + arthroconidia",
        "Capitis/unguium ต้อง oral (terbinafine, itraconazole, griseofulvin สำหรับ capitis)",
        "Tinea ผิวหนังทั่วไป → topical clotrimazole/ketoconazole · ห้าม steroid",
    ],
    items=[
        mcq("DERM-07-02-1", """A man has a slowly enlarging rash in the groin extending to the inner thighs, sparing the scrotum. Examination shows a well-defined, scaly, annular to arciform erythematous patch with a raised active border and central clearing. What would a KOH preparation of the scale most likely show?""",
            "Septate hyphae with arthrospores (arthroconidia)", ["Short hyphae with thick-walled oval yeasts", "Pseudohyphae with budding yeast", "Branching hyphae with sporangia", "Multinucleated giant cells"],
            explain="""วงขอบนูนแดงขุย ตรงกลางจาง ที่ขาหนีบ (ไม่ลงถุงอัณฑะ) = **tinea cruris** → KOH เห็น **septate hyphae + arthroconidia** (สไลด์หน้า 229, 231–232)
- Hyphae สั้น + ยีสต์กลมผนังหนา (spaghetti & meatballs) เป็นของ pityriasis versicolor
- Pseudohyphae + budding yeast เป็นของ candida ซึ่งมักลงถุงอัณฑะและมี satellite papule
- Branching hyphae with sporangia เป็นลักษณะของ zygomycetes ไม่ได้เป็นเชื้อผิวตื้น
- Multinucleated giant cell เป็นผล Tzanck ของ herpes ไม่ใช่ KOH""",
            pearl="Tinea KOH = septate hyphae + arthroconidia",
            topic="Tinea KOH", ref=[f"{D} หน้า 229, 231–232"], nl=["2.3.12(11)", "B4.3(1)"], kind="old", src=OLD),
        mcq("DERM-07-02-2", """A 10-year-old boy has a rash on his forearms and flank. Red circular areas have grown larger and become ring-shaped. He recently got a new puppy that sleeps in his bed. Examination shows three scaly, sharply marginated annular plaques with central clearing, each less than 4 cm. What is the most appropriate management?""",
            "Topical clotrimazole", ["Topical triamcinolone", "Oral prednisolone", "Oral griseofulvin", "Topical mupirocin"],
            explain="""วงขอบนูนขุยตรงกลางจาง ติดจากลูกหมา = **tinea corporis** ที่จำนวนน้อย พื้นที่เล็ก → **topical antifungal เช่น clotrimazole** (สไลด์หน้า 230, 233–234)
- Triamcinolone (steroid) ทำให้เชื้อราลามและหน้าตาผื่นเปลี่ยน (tinea incognito)
- Prednisolone ยิ่งกดภูมิและไม่มีข้อบ่งชี้
- Oral griseofulvin ใช้กับ tinea capitis หรือ tinea corporis ที่กว้างมาก ไม่ใช่ไม่กี่วง
- Mupirocin เป็นยาฆ่าเชื้อแบคทีเรีย ไม่ออกฤทธิ์ต่อเชื้อรา""",
            pearl="Tinea corporis เฉพาะที่ → topical clotrimazole",
            topic="Tinea corporis tx", ref=[f"{D} หน้า 233–234"], nl=["2.3.12(11)"], kind="old", src=OLD),
        mcq("DERM-07-02-3", """A 55-year-old man has thickened, yellowish, crumbly toenails on four toes with subungual debris for 2 years. KOH from the nail debris shows septate hyphae. Liver function tests are normal. What is the most appropriate treatment?""",
            "Oral itraconazole (or terbinafine)", ["Topical ketoconazole cream alone", "Oral ketoconazole", "Topical itraconazole cream alone", "Oral griseofulvin for 2 weeks"],
            explain="""**Tinea unguium** หลายเล็บ → ยาทาอย่างเดียวไม่พอ ต้องใช้ **oral terbinafine, itraconazole หรือ fluconazole** (+ nail lacquer) (สไลด์หน้า 230, 235–236)
- Ketoconazole cream ไม่ซึมผ่านแผ่นเล็บ
- Oral ketoconazole เป็นพิษต่อตับ ไม่ใช้รักษาเชื้อราผิวหนังแล้ว (เสริม)
- Itraconazole cream ไม่ใช่รูปแบบยาที่ใช้รักษาเล็บ และยาทาอย่างเดียวไม่พอ
- Griseofulvin ได้ผลต่ำกับเล็บ และต้องใช้หลายเดือน ไม่ใช่ 2 สัปดาห์""",
            pearl="Tinea unguium → oral terbinafine/itraconazole",
            topic="Onychomycosis", ref=[f"{D} หน้า 235–236"], nl=["2.3.12(11)"], kind="old", src=OLD),
        mcq("DERM-07-02-4", """A 7-year-old boy has a 4-cm round patch of hair loss on the scalp with gray scaling and broken hairs. His kitten has patchy fur loss. KOH of plucked hairs shows fungal elements. What is the most appropriate treatment?""",
            "Oral griseofulvin (or terbinafine) plus ketoconazole shampoo", ["Topical clotrimazole cream alone", "Intralesional triamcinolone", "Topical minoxidil", "Ketoconazole shampoo alone"],
            explain="""ผมร่วงเป็นหย่อมมีขุยและผมหัก KOH บวก ติดจากแมว = **tinea capitis** → ต้องให้ **oral antifungal (griseofulvin, terbinafine, itraconazole, fluconazole) + ketoconazole/selenium shampoo** (สไลด์หน้า 230)
- ยาทาอย่างเดียวไม่ซึมถึงรากผม
- Intralesional steroid ใช้ใน alopecia areata ซึ่งไม่มีขุยและ KOH ลบ
- Minoxidil ใช้ใน androgenetic alopecia
- แชมพูอย่างเดียวช่วยลดการแพร่เชื้อ แต่ไม่รักษาเชื้อในรากผม""",
            pearl="Tinea capitis → oral antifungal + shampoo",
            topic="Tinea capitis", ref=[f"{D} หน้า 230"], nl=["2.3.12(11)"]),
    ])

# ---------------------------------------------------------------- 07-03 Candida
S3 = sec("derm-07-03", "Candidiasis",
    "C. albicans · ภูมิต่ำ (HIV, DM, neutropenia, ICU), ATB/steroid, อับชื้น · intertrigo = ปื้นแดงสดเปื่อยตามซอก + satellite papule/pustule · thrush = คราบขาวขูดออกได้ · KOH budding yeast + pseudohyphae · topical clotrimazole/miconazole/keto/nystatin",
    minutes=6, source=f"{D} หน้า 237–243", nl=["2.3.12(11)", "B4.2.2(9)", "B4.3(1)"],
    md='''
### ปัจจัยเสี่ยง

- **Candida albicans**
- **Immunosuppression: HIV, DM, neutropenia, ผู้ป่วย ICU**
- **ใช้ antibiotic / steroid เมื่อเร็ว ๆ นี้**, **ความชื้นสะสม** (อ้วน ซอกพับ ผ้าอ้อม)

### Mucosal infections

| ชนิด | สิ่งที่เห็น |
|---|---|
| **Oral thrush** | **คราบขาว (white plaque) ขูดออกได้** เหลือพื้นแดง (**underlying erythema**) |
| **Esophageal candidiasis** | กลืนเจ็บ — นึก HIV (เสริม) |
| **Vulvovaginitis** | ตกขาวเป็นก้อนแป้ง คันมาก (เสริม) |
| **Balanitis** | ผื่นแดงตุ่มเล็กที่หัวองคชาต (เสริม) |

### Cutaneous infections

| ชนิด | สิ่งที่เห็น |
|---|---|
| **Candidal intertrigo** | **erythematous patch แดงสด เปื่อยชื้น (macerated) ใน intertriginous area** (รักแร้ ใต้ราวนม ขาหนีบ) + **satellite papules/pustules** รอบนอก · ไม่มี central clearing |
| **Diaper dermatitis** (candida) | แดงสดในซอกขาหนีบที่ผ้าอ้อมปิด + satellite · ต่างจาก irritant diaper dermatitis ที่ **เว้นซอกพับ** (เสริม) |

### Investigation

- **KOH: budding yeast cells with pseudohyphae** (ดูภาพใน pityriasis versicolor)

### การรักษา (สไลด์หน้า 239)

- **Candida intertrigo: topical antifungal (1st line) — clotrimazole, miconazole, ketoconazole, nystatin** + ทำให้แห้ง
- **Oral candidiasis: clotrimazole oral troche, nystatin oral suspension**
- เสริม: esophageal/systemic → oral fluconazole

> ผื่นแดงที่ขาหนีบ "ทายา (steroid) แล้วไม่ดีขึ้น" + satellite papule = candida → **ketoconazole** (azole) ไม่ใช่ steroid
''',
    pearls=[
        "Candidal intertrigo = แดงสดเปื่อยตามซอก + satellite papule/pustule",
        "Oral thrush = คราบขาวขูดออกได้ พื้นแดง",
        "KOH = budding yeast + pseudohyphae",
        "Intertrigo → topical clotrimazole/miconazole/ketoconazole/nystatin · thrush → clotrimazole troche/nystatin suspension",
    ],
    items=[
        mcq("DERM-07-03-1", """A 50-year-old woman weighing 80 kg has an itchy rash in both axillae and under the breasts. Examination shows multiple erythematous, macerated and eroded patches with satellite vesicles and pustules. What is the most appropriate investigation?""",
            "10% KOH preparation", ["Tzanck smear", "Gram stain and culture", "Wood lamp examination", "Skin biopsy for direct immunofluorescence"],
            explain="""ปื้นแดงเปื่อยตามซอกพับในคนอ้วน + **satellite vesicles/pustules** = **candidal intertrigo** → ยืนยันด้วย **KOH** หา budding yeast + pseudohyphae (สไลด์หน้า 238, 240–241)
- Tzanck ใช้หา herpes ซึ่งเป็นกลุ่มตุ่มน้ำบนพื้นแดง ไม่ใช่ปื้นแดงตามซอก
- Gram stain/culture ใช้หาแบคทีเรีย ตุ่มหนองรอบ ๆ ของ candida ไม่ได้เกิดจากแบคทีเรีย
- Wood lamp ใช้ใน vitiligo/erythrasma (เรืองแสงแดงปะการัง) ไม่ใช่การตรวจหลักของ candida
- DIF ใช้วินิจฉัยโรคตุ่มน้ำ autoimmune""",
            pearl="ผื่นซอกพับ + satellite → KOH หา candida",
            topic="Candida Ix", ref=[f"{D} หน้า 240–241"], nl=["2.3.12(11)", "B4.3(1)"], kind="old", src=OLD),
        mcq("DERM-07-03-2", """A 60-year-old woman has an itchy rash in both groins that has not improved with a cream from the pharmacy. Examination shows bilateral, well-defined, bright erythematous macerated patches extending into the skin folds, surrounded by scattered erythematous satellite papules. What is the most appropriate management?""",
            "Topical ketoconazole", ["Mid-potency topical steroid", "Povidone-iodine", "Topical calcineurin inhibitor", "Oral cephalexin"],
            explain="""ปื้นแดงสดในซอกขาหนีบ + **satellite papules** = **candidal intertrigo** → **topical azole เช่น ketoconazole** (หรือ clotrimazole, miconazole, nystatin) (สไลด์หน้า 239, 242–243) · ยาที่ซื้อทาแล้วไม่ดีขึ้นมักเป็น steroid
- Topical steroid ทำให้เชื้อราลามมากขึ้น
- Povidone-iodine ระคายผิวในซอกพับ และไม่ใช่ยารักษาเชื้อราผิวหนัง
- TCI ใช้กับ eczema ไม่ฆ่าเชื้อ
- Cephalexin รักษาแบคทีเรีย ไม่ได้ผลกับ candida""",
            pearl="Candidal intertrigo → topical azole",
            topic="Candida tx", ref=[f"{D} หน้า 242–243"], nl=["2.3.12(11)"], kind="old", src=OLD),
        mcq("DERM-07-03-3", """A 34-year-old man recently completed a course of antibiotics. He has painless white plaques on the tongue and buccal mucosa that can be wiped off with a tongue depressor, leaving an erythematous base. He has no dysphagia. HIV test is pending. What is the most appropriate initial treatment?""",
            "Nystatin oral suspension (or clotrimazole troche)", ["Oral acyclovir", "Topical triamcinolone in orabase", "Oral amoxicillin", "Biopsy before treatment"],
            explain="""คราบขาวที่ **ขูดออกได้** เหลือพื้นแดง หลังได้ antibiotic = **oral thrush** → **nystatin oral suspension หรือ clotrimazole troche** (สไลด์หน้า 237, 239)
- Acyclovir รักษา herpes ซึ่งเป็นตุ่มน้ำ/แผลเจ็บ ไม่ใช่คราบขาว
- Triamcinolone (steroid) ทำให้เชื้อราเพิ่ม
- Amoxicillin เป็นยาฆ่าแบคทีเรีย ยิ่งส่งเสริม candida
- คราบขาวขูดออกได้วินิจฉัยทางคลินิกได้ — คราบขาวที่ขูดไม่ออกจึงต้องคิดถึง leukoplakia/hairy leukoplakia (เสริม)""",
            pearl="Thrush = คราบขาวขูดออกได้ → nystatin suspension/clotrimazole troche",
            topic="Oral thrush", ref=[f"{D} หน้า 237, 239"], nl=["2.3.12(11)"]),
    ])

# ---------------------------------------------------------------- 07-04 CLM
S4 = sec("derm-07-04", "Cutaneous larva migrans (creeping eruption)",
    "Hookworm ของสุนัข/แมว (A. braziliense, A. caninum) จากดิน/ทราย · ผื่นแดงเป็นเส้นคดเคี้ยว คันมาก เคลื่อน 1–2 cm/วัน · albendazole, ivermectin · larva currens (Strongyloides) 5–10 cm/ชม.",
    minutes=4, source=f"{D} หน้า 244–248", nl=["2.3.12-3(3)", "B4.2.2-3(4)"],
    md='''
### เชื้อและการติดต่อ

- ตัวอ่อน **hookworm ของสุนัขและแมว**: **Ancylostoma braziliense, A. caninum**
- **สัมผัสดิน/ทรายที่ปนเปื้อนอุจจาระสัตว์** (เดินเท้าเปล่าชายหาด ชาวสวน นั่งบนทราย)
- คนเป็น dead-end host ตัวอ่อนไชได้แค่ใน epidermis (เสริม)

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| Primary lesion | **serpiginous (คดเคี้ยวเป็นงู)** เส้นนูนแดงกว้าง 2–3 mm (เสริม) อาจมีตุ่มน้ำ |
| อาการ | **คันมาก (severe pruritus)** แดง |
| การเคลื่อน | **ช้า 1–2 cm/วัน** |
| ตำแหน่ง | เท้า ก้น มือ (ที่สัมผัสดิน) |

### การรักษา

- **Albendazole, ivermectin**
- **หายเองได้ใน 5–6 สัปดาห์** แต่ยาทำให้หายเร็วขึ้น

### แยกจาก larva currens

| | CLM | **Larva currens** (racing larva) |
|---|---|---|
| เชื้อ | hookworm สัตว์ | **Strongyloides stercoralis** |
| ความเร็ว | **1–2 cm/วัน** | **5–10 cm/ชั่วโมง** |
| ตำแหน่ง (เสริม) | เท้า | รอบก้น ต้นขา ลำตัว (autoinfection) |
''',
    pearls=[
        "CLM = เส้นคดเคี้ยวคันมาก ช้า 1–2 cm/วัน หลังเดินเท้าเปล่าบนทราย/ดิน",
        "เชื้อ A. braziliense, A. caninum (hookworm สุนัข แมว)",
        "รักษา albendazole หรือ ivermectin (หายเองใน 5–6 wk)",
        "Larva currens (Strongyloides) เร็ว 5–10 cm/ชม.",
    ],
    items=[
        mcq("DERM-07-04-1", """A 40-year-old man has an intensely itchy, raised, red, snake-like track on the sole of his foot. The track advances about 2 cm each day. Three weeks ago, he returned from a beach vacation where he walked barefoot in the sand. What is the most likely diagnosis?""",
            "Cutaneous larva migrans", ["Larva currens", "Tinea pedis", "Jellyfish dermatitis", "Scabies"],
            explain="""เส้นคดเคี้ยวคันมาก **เคลื่อน ~ 2 cm/วัน** หลังเดินเท้าเปล่าบนทราย = **cutaneous larva migrans** (สไลด์หน้า 244–246)
- Larva currens (Strongyloides) เคลื่อนเร็ว 5–10 cm/ชั่วโมง มักอยู่รอบก้นและลำตัว
- Tinea pedis เป็นขุยลอกที่ง่ามนิ้วเท้า ไม่เป็นเส้นเคลื่อนที่
- Jellyfish dermatitis เป็นเส้นแดงจากหนวดตั้งแต่ตอนสัมผัส ปวดแสบทันที ไม่เคลื่อนที่ทุกวัน
- Scabies เป็นตุ่มและ burrow สั้น ๆ ที่ง่ามนิ้วมือ ข้อมือ ซอกพับ""",
            pearl="เส้นคดเคี้ยวคัน ช้า 1–2 cm/วัน หลังเดินทราย = CLM",
            topic="CLM dx", ref=[f"{D} หน้า 245–246"], nl=["2.3.12-3(3)"], kind="old", src=OLD),
        mcq("DERM-07-04-2", """A farmer who works barefoot in soil contaminated with dog feces has an intensely itchy, serpiginous, erythematous track on his foot that has moved slowly over 10 days. What is the most appropriate management?""",
            "Albendazole", ["Acyclovir", "Dicloxacillin", "Surgical excision of the track", "Skin graft"],
            explain="""เส้นคดเคี้ยวคันเคลื่อนช้าหลังสัมผัสดินปนอุจจาระสุนัข = **CLM** → **albendazole** (หรือ ivermectin) (สไลด์หน้า 244, 247–248)
- Acyclovir รักษา herpes ไม่ออกฤทธิ์ต่อพยาธิ
- Dicloxacillin รักษาแบคทีเรีย
- การตัดเส้นทางออกไม่ได้ผล เพราะตัวอ่อนมักอยู่เลยปลายเส้นที่เห็นไปแล้ว (เสริม)
- Skin graft ไม่มีข้อบ่งชี้สำหรับโรคเฉพาะที่ที่หายได้ด้วยยา""",
            pearl="CLM → albendazole/ivermectin",
            topic="CLM tx", ref=[f"{D} หน้า 247–248"], nl=["2.3.12-3(3)"], kind="old", src=OLD),
    ])

# ---------------------------------------------------------------- 07-05 Scabies & lice
F_SCAB = fig("derm-07-05-f1", "Scabies: ตำแหน่งที่ต้องมองหา burrow และตุ่ม", f'''<svg viewBox="0 0 740 330">
 <g transform="translate(0,20)">{body(200, 10)}
  <circle cx="153" cy="84" r="6" class="bad"/><circle cx="247" cy="84" r="6" class="bad"/>
  <circle cx="176" cy="130" r="5" class="bad"/><circle cx="224" cy="130" r="5" class="bad"/>
  <circle cx="200" cy="140" r="5" class="bad"/>
  <circle cx="190" cy="152" r="5" class="bad"/><circle cx="210" cy="152" r="5" class="bad"/>
  <circle cx="160" cy="152" r="6" class="bad"/><circle cx="240" cy="152" r="6" class="bad"/>
  <circle cx="186" cy="248" r="5" class="badsoft"/><circle cx="214" cy="248" r="5" class="badsoft"/>
 </g>
 <text x="200" y="20" text-anchor="middle" class="t3">หน้า-ศีรษะ: ผู้ใหญ่มักไม่เป็น</text>
 <text x="20" y="104" class="t2">รักแร้</text>
 <text x="20" y="150" class="t2">รอบสะดือ เอว</text>
 <text x="20" y="176" class="t2">ข้อมือ ง่ามนิ้วมือ</text>
 <text x="20" y="196" class="t3">(burrow เห็นชัดสุด)</text>
 <text x="20" y="276" class="t2">ข้อเท้า หลังเท้า</text>
 <text x="270" y="166" class="t2">ขาหนีบ ก้น อวัยวะเพศ</text>
 <text x="270" y="186" class="t3">ตุ่ม nodule ที่องคชาต = จำเพาะ</text>
 <rect x="440" y="20" width="290" height="140" rx="10" class="box"/>
 <text x="585" y="44" text-anchor="middle" class="tb">Burrow (รูขุดของตัวหิด)</text>
 <path d="M470 110C500 90 530 120 560 100C590 80 620 110 650 96" class="lnbad"/>
 <circle cx="660" cy="92" r="6" class="bad"/>
 <text x="660" y="76" text-anchor="middle" class="t3">ตัวเมีย</text>
 <circle cx="520" cy="104" r="2.5" class="ln"/><circle cx="560" cy="100" r="2.5" class="ln"/><circle cx="600" cy="94" r="2.5" class="ln"/>
 <text x="585" y="136" text-anchor="middle" class="t3">เส้นสีน้ำตาลเทาบาง ๆ ยาว 2–10 mm · มีไข่และมูล</text>
 <rect x="440" y="176" width="290" height="140" rx="10" class="misssoft"/>
 <text x="585" y="200" text-anchor="middle" class="tb">ทารก &lt; 2 ปี / ผู้สูงอายุ (เสริม)</text>
 <text x="456" y="226" class="t2">ทารก: ฝ่ามือ ฝ่าเท้า หนังศีรษะ หน้า</text>
 <text x="456" y="250" class="t2">ตุ่มน้ำ ตุ่มหนองได้</text>
 <text x="456" y="280" class="t2">Crusted scabies: สะเก็ดหนา</text>
 <text x="456" y="300" class="t3">ภูมิต่ำ ไม่ค่อยคัน ติดต่อสูงมาก</text>
</svg>''', "ตุ่มคันกลางคืนที่ง่ามนิ้ว ข้อมือ รักแร้ สะดือ และขาหนีบ พร้อมคนในบ้านคันด้วย = scabies · ผู้ใหญ่ไม่เป็นที่หน้า แต่ทารกเป็นได้")

S5 = sec("derm-07-05", "Scabies และ pediculosis (เหา โลน)",
    "Sarcoptes scabiei · คันมากกลางคืน · papule vesicle burrow ที่ง่ามนิ้ว ข้อมือ ซอกพับ · 5% permethrin D1, D7 (1st line) · < 2 ปี/ตั้งครรภ์ใช้ sulfur · รักษาทั้งบ้าน · crusted → ivermectin · เหา: 1% permethrin 10 นาที ซ้ำ 7–10 วัน",
    minutes=9, source=f"{D} หน้า 249–261", nl=["2.3.12(10)", "2.1.51"],
    md='''
### Scabies (หิด)

- **Sarcoptes scabiei** · ติดต่อทาง **สัมผัสผิวโดยตรง (ติดง่ายมาก)** — คนในบ้าน หอพัก บ้านพักคนชรา
- อาการเกิด 3–6 สัปดาห์หลังติดครั้งแรก (type IV ต่อตัวหิด ไข่ มูล) (เสริม)

| หัวข้อ | สิ่งที่เห็น |
|---|---|
| อาการ | **คันมาก โดยเฉพาะกลางคืน** · คนในบ้านคันด้วย |
| Primary lesion | **erythematous papules, vesicles, burrows** (เส้นสีน้ำตาลแดงบาง ๆ) + รอยเกา |
| ตำแหน่ง | **intertriginous areas, ข้อมือ, ง่ามนิ้ว (interdigital folds)**, รักแร้ สะดือ ขาหนีบ ก้น อวัยวะเพศ — ผู้ใหญ่ **เว้นหน้า** |

[[fig:derm-07-05-f1]]

**Investigation**: **skin scraping (ใส่ mineral oil) → ตัวหิด ไข่ มูล**

**การรักษา** (สไลด์หน้า 251–252)

| ยา | วิธีใช้ | หมายเหตุ |
|---|---|---|
| **5% permethrin cream (1st line)** | **ทา D1, D7** | ทารก > 2 เดือนใช้ได้ (เสริม) |
| **10–25% benzyl benzoate** | **ทา D1, 2, 3 และ D8, 9, 10** | ระคายผิว |
| **1% lindane** | **ทา D1, D7** | **ห้ามในเด็ก < 2 ปี, ตั้งครรภ์, ให้นมบุตร** (neurotoxic) |
| **5–10% sulfur ointment** | **ทา D1–7** | **ใช้ในเด็ก < 2 ปี, ตั้งครรภ์, ให้นมบุตร** |

- **ทาทั้งตัวตั้งแต่คอถึงปลายนิ้วเท้า เน้นซอกต่าง ๆ รวมทั้งซอกเล็บ ยกเว้นหน้า ทิ้งไว้ 1 คืน ล้างตอนเช้า**
- **ทาซ้ำหลัง 1 สัปดาห์** — ยาฆ่าแค่ตัวหิด ไม่ฆ่าไข่
- **รักษาคนในบ้านพร้อมกัน แม้ไม่มีอาการ**
- **เสื้อผ้า ผ้าปู ผ้าเช็ดตัว ซักน้ำ > 60°C** · ของที่ซักไม่ได้ **ใส่ถุงพลาสติกปิดมิด 48–72 ชม.**
- อาการคันอาจคงอยู่ 2–4 สัปดาห์หลังรักษาหาย (post-scabetic itch) (เสริม)

**Crusted (Norwegian) scabies**: ใน **immunocompromised** · **สะเก็ดหนา (thick crusts)** ตัวหิดนับล้าน ติดต่อสูงมาก · **Tx: ivermectin** (oral) ร่วมกับยาทา (เสริม)

### Lice (pediculosis)

| ชนิด | เชื้อ |
|---|---|
| เหา (head louse) | **Pediculus humanus capitis** |
| เหาตัว (body louse) | **Pediculus humanus corporis** (อยู่ในตะเข็บเสื้อผ้า) |
| โลน (pubic/crab louse) | **Phthirus pubis** |

- ติดต่อ: **สัมผัสโดยตรง ใช้หวี/หมวก/ที่นอน/เสื้อผ้าร่วมกัน, เพศสัมพันธ์**
- สิ่งที่เห็น: **คัน** + **เห็นตัวเหาหรือไข่ (nit)** — ไข่สีขาวเทาเกาะแน่นติดเส้นผม ปัดไม่ออก (ต่างจากรังแค) · nit ที่อยู่ **< 1 cm จากหนังศีรษะ** = ยังมีชีวิต/ติดเชื้ออยู่ (เสริม)

**การรักษา** (สไลด์หน้า 259)
- **Head lice: 1% permethrin — ชโลมศีรษะที่แห้ง 10 นาทีแล้วล้างออก, ทำซ้ำที่ 7–10 วัน** + **หวีเสนียด (fine-tooth comb)**
- **Body lice: รักษาความสะอาดร่างกายและเสื้อผ้า**
- **Pubic lice: 1% permethrin + รักษาคู่นอน + ตรวจคัดกรอง STD**
- รักษาคนในบ้านพร้อมกัน · ทำความสะอาดของใช้ · หมวก เสื้อผ้า ที่นอน **ซักแล้วแช่น้ำร้อน** · ที่ซักไม่ได้ **ซักแห้งหรือใส่ถุงปิด 2 สัปดาห์**
''',
    figs=[F_SCAB],
    pearls=[
        "Scabies = คันกลางคืน + ตุ่ม/burrow ที่ง่ามนิ้ว ข้อมือ ซอกพับ + คนในบ้านคัน",
        "5% permethrin D1, D7 คอถึงปลายเท้า ทิ้งค้างคืน · ซ้ำ 1 wk · รักษาทั้งบ้าน",
        "Lindane ห้าม < 2 ปี/ตั้งครรภ์/ให้นม → ใช้ sulfur 5–10% D1–7",
        "Crusted scabies (ภูมิต่ำ สะเก็ดหนา) → ivermectin",
        "เหา: 1% permethrin 10 นาที ซ้ำ 7–10 วัน + หวีเสนียด · โลน: รักษาคู่นอน + คัดกรอง STD",
    ],
    items=[
        mcq("DERM-07-05-1", """A 20-year-old man has generalized itching that is much worse at night. His roommate has similar symptoms. Examination shows erythematous papules and excoriations in the finger webs, flexor wrists, axillae and inguinal area, with a few short, thin, wavy gray-brown lines on the wrists. The face is spared. What is the most likely diagnosis?""",
            "Scabies", ["Atopic dermatitis", "Papular urticaria from insect bites", "Dermatitis herpetiformis", "Pediculosis corporis"],
            explain="""คันมากกลางคืน + ตุ่มที่ **ง่ามนิ้ว ข้อมือ รักแร้ ขาหนีบ** + **burrow** + คนใกล้ชิดคัน = **scabies** (สไลด์หน้า 249, 253–254)
- Atopic dermatitis เป็นผื่น eczema ที่ข้อพับ เรื้อรัง และคนใกล้ชิดไม่ได้คันไปด้วย
- Papular urticaria จากแมลงกัดเป็นตุ่มที่ผิวที่เปิดโล่ง (แขนขา) ไม่มี burrow
- Dermatitis herpetiformis เป็นตุ่มน้ำเล็กสมมาตรที่ข้อศอก เข่า ก้น ไม่ติดต่อ
- Pediculosis corporis เห็นตัวเหาและไข่ในตะเข็บเสื้อผ้า ผื่นที่ลำตัวในคนสุขอนามัยไม่ดี ไม่มี burrow ที่ง่ามนิ้ว""",
            pearl="คันกลางคืน + ง่ามนิ้ว ข้อมือ ซอกพับ + burrow = scabies",
            topic="Scabies dx", ref=[f"{D} หน้า 253–254"], nl=["2.3.12(10)"], kind="old", src=OLD),
        mcq("DERM-07-05-2", """A 30-year-old woman has had a diffuse itchy rash for 3 weeks. Examination shows small red papules in both axillae and groin and thin reddish-brown lines in her finger webs. What is the most appropriate treatment?""",
            "Permethrin 5% cream", ["Hydrocortisone cream", "Nystatin cream", "Ketoconazole cream", "Capsaicin cream"],
            explain="""ตุ่มแดงที่รักแร้ ขาหนีบ + **เส้นสีน้ำตาลแดงที่ง่ามนิ้ว (burrow)** = **scabies** → **5% permethrin cream** (first line) ทา D1, D7 (สไลด์หน้า 251, 255–256)
- Hydrocortisone ลดคันได้แต่ไม่ฆ่าตัวหิด โรคจะลาม
- Nystatin รักษา candida ซึ่งเป็นปื้นแดงตามซอก ไม่มี burrow
- Ketoconazole รักษาเชื้อรา
- Capsaicin ใช้กับอาการปวดจากเส้นประสาท ไม่ใช่ปรสิต""",
            pearl="Scabies → 5% permethrin (D1, D7)",
            topic="Scabies tx", ref=[f"{D} หน้า 255–256"], nl=["2.3.12(10)"], kind="old", src=OLD),
        mcq("DERM-07-05-3", """A 25-year-old woman who is 20 weeks pregnant and her 14-month-old son both have scabies. A pharmacy offered 1% lindane lotion. Which treatment plan from the slide options is safest for both mother and child?""",
            "5–10% sulfur ointment daily on days 1–7 for both", ["1% lindane on days 1 and 7 for both", "1% lindane for the mother and sulfur for the child", "Oral ivermectin for both", "No treatment until after delivery"],
            explain="""สไลด์ระบุ **lindane ห้ามในเด็ก < 2 ปี, ตั้งครรภ์, ให้นมบุตร** และให้ใช้ **5–10% sulfur ointment D1–7** ในกลุ่มนี้ (สไลด์หน้า 251) · ในทางปฏิบัติ permethrin 5% ก็ถือว่าปลอดภัยในตั้งครรภ์และเด็กอายุ > 2 เดือน (เสริม)
- Lindane เป็นพิษต่อระบบประสาท (ชัก) ห้ามทั้งสองคน
- แม่ตั้งครรภ์ห้ามใช้ lindane เช่นกัน
- Ivermectin ไม่แนะนำในหญิงตั้งครรภ์และเด็กน้ำหนัก < 15 kg (เสริม)
- การไม่รักษาทำให้คันทรมาน ติดต่อคนในบ้าน และติดเชื้อแทรกซ้อน""",
            pearl="Scabies < 2 ปี/ตั้งครรภ์/ให้นม: ห้าม lindane → sulfur (หรือ permethrin)",
            topic="Scabies special groups", ref=[f"{D} หน้า 251"], nl=["2.3.12(10)"]),
        mcq("DERM-07-05-4", """An 8-year-old boy has had severe scalp itching for 3 days. Several classmates had the same problem a week ago. Examination shows several oval, gray-white specks firmly attached to hair shafts less than 1 cm from the scalp, especially behind the ears and at the nape; they cannot be brushed off. What is the most likely diagnosis?""",
            "Pediculosis capitis", ["Seborrheic dermatitis (dandruff)", "Tinea capitis", "Scabies", "Hair casts"],
            explain="""คันศีรษะ + เพื่อนในห้องเป็น + **ไข่เหา (nits) เกาะแน่นติดเส้นผม < 1 cm จากหนังศีรษะ** หลังหูและท้ายทอย = **pediculosis capitis** (สไลด์หน้า 258, 260–261)
- รังแคหลุดง่ายเมื่อปัด ไม่เกาะติดเส้นผม
- Tinea capitis ทำให้ผมร่วงเป็นหย่อม มีขุย ผมหัก
- Scabies ในผู้ใหญ่/เด็กโตไม่เป็นที่หนังศีรษะ
- Hair casts เป็นปลอกรอบเส้นผมที่เลื่อนไปตามเส้นได้ ไม่คันและไม่ระบาดในห้องเรียน (เสริม)""",
            pearl="Nit เกาะแน่นติดเส้นผม + ระบาดในห้องเรียน = เหา",
            topic="Head lice", ref=[f"{D} หน้า 260–261"], nl=["2.3.12(10)"], kind="old", src=OLD),
        mcq("DERM-07-05-5", """A 62-year-old man with HIV (CD4 40 cells/µL) has thick, gray, crusted, scaly plaques on his hands, elbows and buttocks with minimal itching. Several nurses on the ward have developed itchy papules. Skin scraping shows numerous mites. What is the most appropriate treatment?""",
            "Oral ivermectin combined with topical permethrin", ["Topical permethrin once only", "Topical corticosteroid", "Oral terbinafine", "Topical sulfur alone for 3 days"],
            explain="""ผู้ป่วยภูมิต่ำมาก + **สะเก็ดหนา** + ตัวหิดจำนวนมาก + ติดต่อเจ้าหน้าที่ = **crusted (Norwegian) scabies** → **ivermectin** (สไลด์หน้า 257) ร่วมกับยาทา (เสริม)
- Permethrin ครั้งเดียวไม่พอสำหรับสะเก็ดหนาที่ยาซึมไม่ถึง
- Topical steroid ทำให้ตัวหิดเพิ่มและโรคลาม
- Terbinafine เป็นยาต้านเชื้อรา สะเก็ดหนานี้ไม่ใช่เชื้อรา
- Sulfur 3 วันไม่พอสำหรับ crusted scabies (สไลด์ให้ทา 7 วันแม้ในหิดธรรมดา)""",
            pearl="Crusted scabies (ภูมิต่ำ สะเก็ดหนา) → ivermectin",
            topic="Crusted scabies", ref=[f"{D} หน้า 257"], nl=["2.3.12(10)"]),
    ])

LECTURE = lecture("07", "Fungal & parasitic skin infections", subtitle="pityriasis versicolor · tinea · candidiasis · cutaneous larva migrans · scabies · lice",
    objectives=[
        "อ่านผล KOH ได้: spaghetti & meatballs, septate hyphae + arthroconidia, budding yeast + pseudohyphae",
        "เลือก topical vs oral antifungal ตามตำแหน่ง (capitis/unguium ต้อง oral)",
        "วินิจฉัย CLM จากความเร็วการเคลื่อนและแยก larva currens",
        "รักษา scabies ถูกวิธี (ยา วิธีทา คนในบ้าน กลุ่มห้าม lindane) และเหา/โลน",
    ],
    sections=[S1, S2, S3, S4, S5])
