from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Dermato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 10-01 Vitiligo
F_WHITE = fig("derm-10-01-f1", "ด่างขาว 5 โรค: แยกด้วยขอบ ขุย ความรู้สึก และการตรวจข้างเตียง", '''<svg viewBox="0 0 740 330">
 <rect x="10" y="10" width="138" height="310" rx="10" class="box"/>
 <text x="79" y="34" text-anchor="middle" class="tb">Vitiligo</text>
 <path d="M44 70C60 54 104 58 112 76C122 98 104 120 80 118C54 116 32 92 44 70Z" class="sunk"/>
 <path d="M44 70C60 54 104 58 112 76C122 98 104 120 80 118C54 116 32 92 44 70Z" class="ln"/>
 <text x="79" y="150" text-anchor="middle" class="t2">ขาวจั๊วะ</text>
 <text x="79" y="170" text-anchor="middle" class="t2">ขอบชัด</text>
 <text x="79" y="190" text-anchor="middle" class="t3">ไม่มีขุย</text>
 <text x="79" y="210" text-anchor="middle" class="t3">ขนขาว</text>
 <text x="79" y="270" text-anchor="middle" class="ta">Wood lamp</text>
 <text x="79" y="290" text-anchor="middle" class="t3">ชัดขึ้น</text>
 <rect x="156" y="10" width="138" height="310" rx="10" class="box"/>
 <text x="225" y="34" text-anchor="middle" class="tb">P. alba</text>
 <ellipse cx="225" cy="90" rx="44" ry="30" class="misssoft"/>
 <text x="225" y="150" text-anchor="middle" class="t2">จาง ขอบไม่ชัด</text>
 <text x="225" y="170" text-anchor="middle" class="t2">หน้าเด็ก</text>
 <text x="225" y="190" text-anchor="middle" class="t3">ขุยละเอียด</text>
 <text x="225" y="210" text-anchor="middle" class="t3">atopy</text>
 <text x="225" y="270" text-anchor="middle" class="ta">KOH ลบ</text>
 <rect x="302" y="10" width="138" height="310" rx="10" class="box"/>
 <text x="371" y="34" text-anchor="middle" class="tb">P. versicolor</text>
 <circle cx="350" cy="80" r="12" class="misssoft"/><circle cx="378" cy="72" r="10" class="misssoft"/><circle cx="392" cy="96" r="12" class="misssoft"/><circle cx="362" cy="104" r="9" class="misssoft"/>
 <text x="371" y="150" text-anchor="middle" class="t2">หลายวงรวมกัน</text>
 <text x="371" y="170" text-anchor="middle" class="t2">หลัง อก</text>
 <text x="371" y="190" text-anchor="middle" class="t3">ขุยแป้ง</text>
 <text x="371" y="270" text-anchor="middle" class="ta">KOH</text>
 <text x="371" y="290" text-anchor="middle" class="t3">spaghetti &amp; meatballs</text>
 <rect x="448" y="10" width="138" height="310" rx="10" class="box"/>
 <text x="517" y="34" text-anchor="middle" class="tb">TT leprosy</text>
 <circle cx="517" cy="88" r="36" class="sunk"/>
 <circle cx="517" cy="88" r="36" class="lnbad"/>
 <text x="517" y="150" text-anchor="middle" class="t2">ขอบนูนแดง</text>
 <text x="517" y="170" text-anchor="middle" class="t2">แห้ง ขนร่วง</text>
 <text x="517" y="190" text-anchor="middle" class="tb">ชา</text>
 <text x="517" y="210" text-anchor="middle" class="t3">เส้นประสาทโต</text>
 <text x="517" y="270" text-anchor="middle" class="ta">pinprick ↓</text>
 <text x="517" y="290" text-anchor="middle" class="t3">slit-skin smear</text>
 <rect x="594" y="10" width="138" height="310" rx="10" class="box"/>
 <text x="663" y="34" text-anchor="middle" class="tb">Post-inflam.</text>
 <ellipse cx="663" cy="90" rx="40" ry="28" class="sunk"/>
 <text x="663" y="150" text-anchor="middle" class="t2">ตามรอยผื่นเดิม</text>
 <text x="663" y="170" text-anchor="middle" class="t2">จางลงเอง</text>
 <text x="663" y="190" text-anchor="middle" class="t3">(เสริม)</text>
 <text x="663" y="270" text-anchor="middle" class="ta">ประวัติ</text>
</svg>''', "ด่างขาวที่ขาวจั๊วะขอบชัดและเรือง Wood lamp = vitiligo · ขอบไม่ชัดที่หน้าเด็ก = pityriasis alba · ขุยแป้งที่หลัง = PV · ชา = โรคเรื้อน")

S1 = sec("derm-10-01", "Vitiligo",
    "Melanocyte ถูกทำลาย (autoimmune) · ด่างขาวจั๊วะ (depigmented) ขอบชัด + leukotrichia · Wood lamp ชัดขึ้น · W/U autoimmune (thyroid) · topical/oral steroid, phototherapy",
    minutes=5, source=f"{D} หน้า 318–320", nl=["2.3.12-3(14)"],
    md='''
### กลไก

- **ทำลาย melanocyte** — **สัมพันธ์กับโรค autoimmune** (autoimmune thyroid disease บ่อยสุด, T1DM, pernicious anemia, Addison, alopecia areata (เสริม))

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| Primary lesion | **well-demarcated, depigmented macules/patches** — **ขาวจั๊วะ (ไม่มีสีเลย)** ไม่มีขุย ผิวเรียบ |
| ตำแหน่ง | รอบรูเปิด (ตา ปาก) มือ ข้อนิ้ว เข่า ข้อศอก อวัยวะเพศ สมมาตร (เสริม) |
| ขน | **leukotrichia** (ขนในรอยโรคเป็นสีขาว) |
| อาการ | ไม่คัน ไม่เจ็บ ความรู้สึกปกติ · Koebner ได้ (เสริม) |

### Investigation

- **Wood lamp test: รอยโรคเห็นชัดขึ้น** (เรืองแสงสีขาวอมฟ้า ขอบคม (เสริม)) — ใช้ยืนยันข้างเตียง
- **W/U autoimmune ตามที่สงสัย** (เช่น TSH)

### การรักษา

- **Immunosuppressant: topical/oral steroid** (+ topical calcineurin inhibitor (เสริม))
- **Phototherapy** (narrowband UVB)
- ใช้ครีมกันแดด (เสริม)

[[fig:derm-10-01-f1]]
''',
    figs=[F_WHITE],
    pearls=[
        "Vitiligo = ด่างขาวจั๊วะขอบชัด + ขนขาว (leukotrichia) ความรู้สึกปกติ",
        "Wood lamp ทำให้รอยโรคชัดขึ้น",
        "สัมพันธ์ autoimmune (thyroid) → ตรวจตามสงสัย",
        "รักษา topical/oral steroid, phototherapy",
    ],
    items=[
        mcq("DERM-10-01-1", """An 8-year-old boy has had light spots for 4 months that are slowly expanding. They are not itchy or painful. His mother has hypothyroidism. Examination shows smooth, sharply demarcated, chalk-white patches over both knuckles, knees and inner thighs, with a tuft of white hair in one patch. Sensation is normal. What is the most appropriate bedside investigation to support the diagnosis?""",
            "Wood lamp examination", ["Serum autoantibodies", "Punch biopsy", "KOH preparation", "Tzanck smear"],
            explain="""ด่างขาวจั๊วะขอบชัด สมมาตรที่ข้อนิ้ว เข่า + **leukotrichia** + ครอบครัวเป็น autoimmune = **vitiligo** → ตรวจข้างเตียงด้วย **Wood lamp** (รอยโรคชัดขึ้น) (สไลด์หน้า 318–320)
- Serum autoantibodies ใช้คัดกรองโรคร่วม ไม่ได้ยืนยันว่าด่างนี้คือ vitiligo
- Punch biopsy ไม่จำเป็นเมื่อลักษณะชัดเจน
- KOH ใช้แยก pityriasis versicolor ซึ่งมีขุยและไม่ได้ขาวจั๊วะ
- Tzanck ใช้หา herpes""",
            pearl="ด่างขาวจั๊วะขอบชัด + leukotrichia → Wood lamp",
            topic="Vitiligo Ix", ref=[f"{D} หน้า 319–320"], nl=["2.3.12-3(14)"], kind="old", src=OLD),
        mcq("DERM-10-01-2", """A 32-year-old woman has symmetric, sharply demarcated depigmented patches around her eyes, mouth and on the backs of her hands for 1 year. She also reports fatigue, weight gain and cold intolerance. Which laboratory test is most appropriate to look for an associated condition?""",
            "Serum TSH", ["Serum ferritin", "Fasting lipid profile", "Serum uric acid", "Serum IgE"],
            explain="""Vitiligo สัมพันธ์กับ **โรค autoimmune** — บ่อยที่สุดคือ autoimmune thyroid disease ผู้ป่วยมีอาการ hypothyroid (อ่อนเพลีย น้ำหนักขึ้น ขี้หนาว) → **TSH** (สไลด์หน้า 318: W/U autoimmune ตามที่สงสัย; thyroid (เสริม))
- Ferritin ใช้ประเมินภาวะเหล็ก ไม่เกี่ยวกับ vitiligo หรืออาการนี้
- Lipid profile ใช้กับ xanthoma
- Uric acid ไม่เกี่ยวกับ vitiligo
- IgE สัมพันธ์กับ atopic dermatitis""",
            pearl="Vitiligo + อาการ thyroid → TSH",
            topic="Vitiligo W/U", ref=[f"{D} หน้า 318"], nl=["2.3.12-3(14)"]),
    ])

# ---------------------------------------------------------------- 10-02 Alopecia
F_HAIR = fig("derm-10-02-f1", "Approach to alopecia (nonscarring vs scarring)", '''<svg viewBox="0 0 740 380">
 <defs><marker id="derm-10-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="270" y="10" width="200" height="40" rx="10" class="acsoft"/>
 <text x="370" y="35" text-anchor="middle" class="tb">ผมร่วง</text>
 <path d="M320 50L180 78" class="ln" marker-end="url(#derm-10-02-a)"/>
 <path d="M440 50L610 78" class="ln" marker-end="url(#derm-10-02-a)"/>
 <rect x="10" y="80" width="520" height="290" rx="10" class="box"/>
 <text x="270" y="104" text-anchor="middle" class="tb">Nonscarring (ยังเห็นรูขุมขน)</text>
 <rect x="24" y="118" width="160" height="240" rx="8" class="c1soft"/>
 <text x="104" y="140" text-anchor="middle" class="tb">Diffuse</text>
 <text x="36" y="168" class="t2">Telogen effluvium</text>
 <text x="36" y="186" class="t3">2–4 เดือนหลัง trigger</text>
 <text x="36" y="214" class="t2">Anagen effluvium</text>
 <text x="36" y="232" class="t3">1–4 wk หลัง chemo</text>
 <rect x="194" y="118" width="160" height="240" rx="8" class="c2soft"/>
 <text x="274" y="140" text-anchor="middle" class="tb">Localized</text>
 <text x="206" y="168" class="t2">Alopecia areata</text>
 <text x="206" y="186" class="t3">ขอบชัด pull test +</text>
 <text x="206" y="214" class="t2">Trichotillomania</text>
 <text x="206" y="232" class="t3">ผมยาวไม่เท่ากัน</text>
 <text x="206" y="260" class="t2">Secondary syphilis</text>
 <text x="206" y="278" class="t3">moth-eaten (เสริม)</text>
 <text x="206" y="306" class="t2">Tinea capitis (เสริม)</text>
 <text x="206" y="324" class="t3">ขุย KOH +</text>
 <rect x="364" y="118" width="156" height="240" rx="8" class="misssoft"/>
 <text x="442" y="140" text-anchor="middle" class="tb">Pattern</text>
 <text x="376" y="168" class="t2">Androgenetic</text>
 <text x="376" y="186" class="t3">ชาย: ขมับ + กลางกระหม่อม</text>
 <text x="376" y="204" class="t3">หญิง: กลางศีรษะ</text>
 <text x="376" y="222" class="t3">แสกกว้าง</text>
 <rect x="540" y="80" width="190" height="290" rx="10" class="badsoft"/>
 <text x="635" y="104" text-anchor="middle" class="tb">Scarring</text>
 <text x="635" y="122" text-anchor="middle" class="t3">รูขุมขนหาย ผิวมันเรียบ</text>
 <text x="556" y="160" class="t2">Discoid lupus</text>
 <text x="556" y="178" class="t3">erythematosus</text>
 <text x="556" y="210" class="t2">Lichen planopilaris</text>
 <text x="556" y="228" class="t3">(LP ที่หนังศีรษะ)</text>
 <text x="556" y="270" class="t3">ผมไม่ขึ้นใหม่</text>
 <text x="556" y="288" class="t3">→ biopsy, ส่งแพทย์ผิวหนัง</text>
</svg>''', "ขั้นแรกดูว่ายังเห็นรูขุมขนไหม (nonscarring) แล้วดูรูปแบบ: ร่วงทั้งศีรษะ เป็นหย่อม หรือเป็นแบบแผนตามฮอร์โมน")

F_CYCLE = fig("derm-10-02-f2", "วงจรเส้นผมกับ telogen vs anagen effluvium", '''<svg viewBox="0 0 740 300">
 <defs><marker id="derm-10-02-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="20" y="30" width="400" height="40" rx="6" class="ok"/>
 <text x="220" y="55" text-anchor="middle" class="tw">Anagen (งอก) 2–6 ปี · ~ 85–90%</text>
 <rect x="420" y="30" width="60" height="40" rx="6" class="miss"/>
 <text x="450" y="55" text-anchor="middle" class="tw">Cat.</text>
 <rect x="480" y="30" width="240" height="40" rx="6" class="c2"/>
 <text x="600" y="55" text-anchor="middle" class="tw">Telogen (พัก) ~3 เดือน · 10–15%</text>
 <text x="20" y="20" class="t3">ปกติร่วง 100 เส้น/วัน · วันสระผม 200–300 เส้น</text>
 <rect x="20" y="96" width="340" height="190" rx="10" class="c2soft"/>
 <text x="190" y="120" text-anchor="middle" class="tb">Telogen effluvium</text>
 <path d="M60 136H300" class="lnc2" marker-end="url(#derm-10-02-b)"/>
 <text x="180" y="152" text-anchor="middle" class="t3">trigger ดันผม anagen → telogen ก่อนเวลา</text>
 <text x="36" y="180" class="t2">ร่วงหลัง trigger 2–4 เดือน</text>
 <text x="36" y="202" class="t2">ร่วง 15–50% · pull test +</text>
 <text x="36" y="224" class="t2">โคนผมเป็นตุ้มกลม (club)</text>
 <text x="36" y="246" class="t2">trichogram telogen &gt; 25%</text>
 <text x="36" y="270" class="t3">หลังคลอด ไข้สูง ผ่าตัด เสียเลือด เครียด</text>
 <rect x="380" y="96" width="340" height="190" rx="10" class="badsoft"/>
 <text x="550" y="120" text-anchor="middle" class="tb">Anagen effluvium</text>
 <path d="M420 136H660" class="lnbad" marker-end="url(#derm-10-02-b)"/>
 <text x="540" y="152" text-anchor="middle" class="t3">พิษทำให้ผม anagen หยุดแบ่งตัวทันที</text>
 <text x="396" y="180" class="t2">ร่วงใน 1–4 สัปดาห์</text>
 <text x="396" y="202" class="t2">ร่วง 80–90% · pull test +</text>
 <text x="396" y="224" class="t2">dystrophic anagen hair</text>
 <text x="396" y="246" class="t3">(โคนเรียวแหลมเหมือนดินสอ)</text>
 <text x="396" y="270" class="t3">chemotherapy · radiation · poisoning</text>
</svg>''', "ผมส่วนใหญ่อยู่ในระยะ anagen — trigger ปานกลางเลื่อนผมไป telogen แล้วร่วงหลัง 3 เดือน (TE) ส่วนพิษรุนแรงหยุดผม anagen ทันทีจึงร่วงเกือบหมดในไม่กี่สัปดาห์ (AE)")

S2 = sec("derm-10-02", "Alopecia: androgenetic, alopecia areata, trichotillomania, telogen & anagen effluvium",
    "AGA = แบบแผน ขมับ/กลางกระหม่อม → minoxidil, finasteride (ชาย) · AA = หย่อมขอบชัด exclamation mark pull test + → intralesional steroid · trichotillomania = รูปแปลก ผมยาวไม่เท่ากัน pull test − → CBT/SSRI · TE = 2–4 เดือนหลัง trigger telogen > 25% · AE = chemo 1–4 wk 80–90%",
    minutes=11, source=f"{D} หน้า 321–342", nl=["2.1.52", "2.3.12-3(1)", "B4.2.2-3(10)"],
    md='''
### พื้นฐาน

- ปกติผมร่วง **100 เส้น/วัน** · **วันสระผม 200–300 เส้น/วัน**
- Hair pull test (เสริม): จับผม ~ 50–60 เส้นดึงเบา ๆ หลุด > 6 เส้น (> 10%) = บวก (active shedding)

[[fig:derm-10-02-f1]]

### Androgenetic alopecia (AGA)

- **Progressive, diffuse, nonscarring** · **↑ ความไวของรูขุมขนต่อ androgen (DHT) → ระยะ anagen สั้นลง** → เส้นผมเล็กลงเรื่อย ๆ (miniaturization (เสริม))
- **Pattern**: **ชาย = bitemporal (ขมับถอย) ± vertex (กลางกระหม่อม)** · **หญิง = vertex และ frontal (แสกกว้าง แนวหน้าผมยังอยู่)**
- **Tx: topical minoxidil** · **finasteride (เฉพาะผู้ชาย)** (ห้ามหญิงตั้งครรภ์ — เพศชายในครรภ์ผิดปกติ (เสริม))

### Alopecia areata (AA)

- **Nonscarring circumscribed** · **immune-mediated** · **สัมพันธ์โรค autoimmune** (vitiligo, thyroid)
- **เริ่มเฉียบพลัน (ภายในสัปดาห์)**

| สิ่งที่เห็น | รายละเอียด |
|---|---|
| ผื่น | **หย่อมผมร่วงกลม ขอบชัด ผิวเรียบปกติ ไม่มีแผลเป็น ไม่มีขุย ไม่แดง** |
| เล็บ | **pitting nail** |
| Pull test | **บวก** ที่ขอบหย่อม |
| Dermoscopy | **exclamation mark hair (!)** — ผมหักโคนเรียว · **black dot, yellow dot** |
| รุนแรง | **alopecia totalis (ทั้งศีรษะ)** · **universalis (ทั้งร่างกาย)** |

- **Tx: topical/intralesional steroid**, **topical immunotherapy**, **± minoxidil**

### Trichotillomania

- **ดึงผมตัวเองแบบ compulsive** — **กลุ่ม OCD spectrum**
- **หย่อมผมร่วงขอบไม่ชัด รูปร่างแปลก (bizarre)** ที่ **หนังศีรษะ คิ้ว ขนตา** (มักข้างถนัด (เสริม))
- **ผมยาวไม่เท่ากัน (different lengths)** · **รอยถลอก (excoriation)** ที่หนังศีรษะ
- **Hair pull test: ลบ** (ผมที่เหลือยึดแน่นปกติ)
- **Dermoscopy: chaotic arrangement of multiple broken hair shafts**
- **Mx: cognitive behavioral therapy, SSRI**

### Telogen effluvium (TE)

- **Trigger: เสียเลือดเฉียบพลัน ยา หลังคลอด ติดเชื้อรุนแรง/ไข้สูง โรคเรื้อรัง หลังผ่าตัด ต่อมไร้ท่อ (thyroid) ขาดสารอาหาร ความเครียด**
- กลไก: **trigger กระตุ้นให้ผม anagen เข้าสู่ telogen เร็วขึ้น → หลังจากนั้น 12–14 สัปดาห์ร่วง** (ร่วง **15–50%**)
- **Diffuse, nonscarring** · **pull test บวก** · โคนผมเป็นตุ้ม (**club-shaped telogen root**)
- **Trichogram: telogen hair > 25%** (ปกติ 10–15%)
- **Mx: avoid trigger, reassure — ผมขึ้นใหม่เป็นปกติ**

### Anagen effluvium (AE)

- **Trigger: chemotherapy, poisoning (thallium, arsenic (เสริม)), radiation**
- **ผมระยะ anagen หยุดงอกและร่วง (80–90%)** ภายใน **วันถึงสัปดาห์ (1–4 สัปดาห์)**
- **Pull test บวก** · **trichogram: dystrophic anagen hair** (เรียวเล็กที่โคน)
- **Mx: avoid trigger — ผมขึ้นใหม่เอง**

[[fig:derm-10-02-f2]]

| | Telogen effluvium | Anagen effluvium |
|---|---|---|
| Onset หลัง trigger | **2–4 เดือน** | **1–4 สัปดาห์** |
| ร่วง | **15–50%** | **80–90%** |
| ลักษณะเส้นผม | **normal telogen hair > 25%** (club) | **dystrophic anagen hair** |
''',
    figs=[F_HAIR, F_CYCLE],
    pearls=[
        "AA: หย่อมกลมขอบชัด ผิวปกติ exclamation mark hair pull test + nail pitting → intralesional steroid",
        "Trichotillomania: รูปแปลก ผมยาวไม่เท่ากัน pull test ลบ → CBT, SSRI",
        "TE: 2–4 เดือนหลัง trigger (หลังคลอด ไข้) ร่วง 15–50% club hair telogen > 25% → reassure",
        "AE: chemo 1–4 wk ร่วง 80–90% dystrophic anagen hair",
        "AGA: ชายขมับ ± กลางกระหม่อม · หญิงกลางศีรษะ → minoxidil ± finasteride (ชาย)",
    ],
    items=[
        mcq("DERM-10-02-1", """A 23-year-old man with vitiligo has multiple round, painless bald patches on his scalp and eyebrows that appeared over a few weeks. He denies pulling his hair. The patches show smooth skin without scarring, scale, erythema or inflammation. Several short broken hairs that taper toward the scalp are seen at the margins, the pull test is positive at the edge, and he has nail pitting. What is the most likely diagnosis?""",
            "Alopecia areata", ["Trichotillomania", "Tinea capitis", "Androgenetic alopecia", "Discoid lupus erythematosus"],
            explain="""หย่อมกลม ขอบชัด ผิวเรียบไม่มีแผลเป็น เกิดเร็ว + **exclamation mark hair** + pull test บวก + **nail pitting** + มีโรค autoimmune (vitiligo) = **alopecia areata** (สไลด์หน้า 326–327, 335–336)
- Trichotillomania เป็นหย่อมรูปแปลกขอบไม่ชัด ผมยาวไม่เท่ากัน pull test ลบ
- Tinea capitis มีขุย ผมหัก ตุ่มหนอง และ KOH บวก
- AGA เป็นแบบแผนที่ขมับและกลางกระหม่อม ค่อย ๆ บางลง ไม่ใช่หย่อมกลมที่คิ้ว
- DLE เป็น scarring alopecia มีผื่นแดงขุย รูขุมขนหาย""",
            pearl="หย่อมกลมขอบชัด + exclamation mark + nail pitting = AA",
            topic="AA dx", ref=[f"{D} หน้า 335–336"], nl=["2.3.12-3(1)"], kind="old", src=OLD),
        mcq("DERM-10-02-2", """A 14-year-old boy has had hair loss for 3 months with no other symptoms. Examination shows non-scarring, bizarre-shaped patches of hair loss in both parieto-occipital areas containing hairs broken at different lengths. The hair pull test is negative. What is the most likely diagnosis?""",
            "Trichotillomania", ["Alopecia areata", "Androgenetic alopecia", "Syphilitic alopecia", "Discoid lupus erythematosus"],
            explain="""หย่อมผมร่วง **รูปร่างแปลก** ผม **ยาวไม่เท่ากัน** และ **pull test ลบ** = **trichotillomania** (สไลด์หน้า 328–329, 337–338)
- Alopecia areata เป็นหย่อมกลมขอบชัด pull test บวกที่ขอบ มี exclamation mark hair
- AGA ในวัยรุ่นชายเป็นแบบแผนที่ขมับ ไม่ใช่หย่อมรูปแปลกที่ท้ายทอยด้านข้าง
- Syphilitic alopecia เป็นหย่อมเล็กกระจายแบบ "มอดกิน" ร่วมกับผื่นอื่นของ secondary syphilis
- DLE เป็นแผลเป็นมีผื่นแดงขุย""",
            pearl="รูปแปลก ผมยาวไม่เท่ากัน pull test ลบ = trichotillomania",
            topic="Trichotillomania", ref=[f"{D} หน้า 337–338"], nl=["2.1.52"], kind="old", src=OLD),
        mcq("DERM-10-02-3", """A 17-year-old girl with obsessive-compulsive disorder has several large, irregular patches of hair loss on the crown with hairs of different lengths and a few excoriations. The hair pull test is negative. Dermoscopy shows a chaotic pattern of broken hair shafts at varying lengths. What is the most appropriate management?""",
            "Cognitive behavioral therapy, with an SSRI if needed", ["Intralesional triamcinolone", "Oral terbinafine", "Topical minoxidil", "Oral finasteride"],
            explain="""Trichotillomania (OCD spectrum) → **cognitive behavioral therapy (habit reversal) ± SSRI** (สไลด์หน้า 328, 339–340)
- Intralesional steroid รักษา alopecia areata ซึ่ง pull test บวก หย่อมขอบชัด
- Terbinafine รักษา tinea capitis ซึ่งจะมีขุยและ KOH บวก
- Minoxidil ใช้ใน AGA และเสริมใน AA ไม่แก้พฤติกรรมดึงผม
- Finasteride ใช้ใน AGA ผู้ชาย""",
            pearl="Trichotillomania → CBT ± SSRI",
            topic="Trichotillomania tx", ref=[f"{D} หน้า 339–340"], nl=["2.1.52"], kind="old", src=OLD),
        mcq("DERM-10-02-4", """A 30-year-old woman has diffuse non-scarring hair loss. She delivered a baby 3 months ago. The hair pull test is positive, and the pulled hairs have small white club-shaped bulbs at their proximal ends. There are no bald patches. What is the most likely diagnosis?""",
            "Telogen effluvium", ["Alopecia areata", "Androgenetic alopecia", "Tinea capitis", "Trichotillomania"],
            explain="""ผมร่วงทั่วศีรษะ **3 เดือนหลังคลอด** + pull test บวก + **club-shaped (telogen) roots** = **telogen effluvium** (สไลด์หน้า 330–331, 341–342)
- Alopecia areata เป็นหย่อมกลมขอบชัด ไม่ใช่ร่วงทั่วศีรษะ
- AGA ค่อย ๆ บางลงตามแบบแผนเป็นปี ไม่เกิดหลังคลอด 3 เดือนแบบนี้
- Tinea capitis มีหย่อม ขุย ผมหัก
- Trichotillomania pull test ลบ และเป็นหย่อมรูปแปลก""",
            pearl="ร่วงทั่ว 2–4 เดือนหลังคลอด/ไข้ + club hair = telogen effluvium",
            topic="TE", ref=[f"{D} หน้า 341–342"], nl=["2.1.52"], kind="old", src=OLD),
        mcq("DERM-10-02-5", """A 45-year-old woman receiving doxorubicin and cyclophosphamide for breast cancer notices massive diffuse hair loss starting 2 weeks after the first cycle; about 85% of her scalp hair has fallen out. Which finding is expected on examination of the shed hairs?""",
            "Dystrophic anagen hairs with tapered, narrowed proximal ends", ["Club-shaped telogen hairs comprising more than 25%", "Exclamation mark hairs at the margin of round patches", "Hairs broken at different lengths with negative pull test", "Septate hyphae inside the hair shafts"],
            explain="""ผมร่วงมาก **80–90%** ภายใน **1–4 สัปดาห์หลังเคมีบำบัด** = **anagen effluvium** → เส้นผมที่หลุดเป็น **dystrophic anagen hair** (โคนเรียวเล็ก) (สไลด์หน้า 332–334)
- Club-shaped telogen > 25% เป็นของ telogen effluvium ที่เกิด 2–4 เดือนหลัง trigger และร่วง 15–50%
- Exclamation mark hair เป็นของ alopecia areata
- ผมหักยาวไม่เท่ากัน pull test ลบ เป็นของ trichotillomania
- Hyphae ในเส้นผมเป็นของ tinea capitis""",
            pearl="Chemo → anagen effluvium 1–4 wk 80–90% dystrophic anagen hair",
            topic="AE", ref=[f"{D} หน้า 332–334"], nl=["2.1.52"]),
        mcq("DERM-10-02-6", """A 28-year-old man has gradual thinning of hair over both temples and the crown over 5 years. His father has similar baldness. The scalp is normal without scale, scarring or patches, and the pull test is negative. He wants medical treatment. Which option is most appropriate?""",
            "Topical minoxidil, with oral finasteride as an option", ["Intralesional triamcinolone", "Oral griseofulvin", "Oral spironolactone", "Reassure that the hair will regrow spontaneously"],
            explain="""ผมบางค่อยเป็นค่อยไปที่ **ขมับสองข้าง (bitemporal) และกลางกระหม่อม (vertex)** ในผู้ชายที่มีประวัติครอบครัว = **androgenetic alopecia** → **topical minoxidil, finasteride (เฉพาะผู้ชาย)** (สไลด์หน้า 324–325)
- Intralesional steroid ใช้ใน alopecia areata
- Griseofulvin ใช้กับ tinea capitis
- Spironolactone เป็นยาต้าน androgen ที่ใช้ในผู้หญิงบางราย ทำให้ผู้ชายเต้านมโตและไม่ใช่ยาที่สไลด์ให้ (เสริม)
- AGA ค่อย ๆ แย่ลง ไม่หายเอง ต่างจาก telogen effluvium""",
            pearl="AGA → minoxidil ± finasteride (ชาย)",
            topic="AGA", ref=[f"{D} หน้า 324–325"], nl=["2.1.52", "B4.1.3(2)"]),
    ])

# ---------------------------------------------------------------- 10-03 HTS & keloid
F_SCAR = fig("derm-10-03-f1", "Hypertrophic scar vs keloid", '''<svg viewBox="0 0 740 260">
 <path d="M20 160H340" class="ln"/>
 <path d="M110 160H250" class="lnf"/>
 <text x="180" y="178" text-anchor="middle" class="t3">ขอบแผลเดิม</text>
 <path d="M110 160C120 110 240 110 250 160Z" class="misssoft"/>
 <path d="M110 160V100 M250 160V100" class="lnf"/>
 <text x="180" y="30" text-anchor="middle" class="tb">Hypertrophic scar</text>
 <text x="180" y="54" text-anchor="middle" class="t2">อยู่ในขอบเขตแผลเดิม</text>
 <text x="180" y="206" text-anchor="middle" class="t2">ขึ้น &lt; 1 เดือนหลังแผล</text>
 <text x="180" y="226" text-anchor="middle" class="t2">ยุบลงเองได้ · ตัดแล้วเป็นซ้ำน้อย</text>
 <path d="M400 160H720" class="ln"/>
 <path d="M490 160H630" class="lnf"/>
 <text x="560" y="178" text-anchor="middle" class="t3">ขอบแผลเดิม</text>
 <path d="M430 160C420 120 440 96 470 104C500 80 560 84 600 100C640 90 690 120 690 160Z" class="badsoft"/>
 <path d="M490 160V90 M630 160V90" class="lnf"/>
 <path d="M690 150C704 146 708 136 700 128" class="lnbad"/>
 <text x="560" y="30" text-anchor="middle" class="tb">Keloid</text>
 <text x="560" y="54" text-anchor="middle" class="t2">ลามเกินขอบแผล มีขาแฉก (claw)</text>
 <text x="560" y="206" text-anchor="middle" class="t2">ขึ้นหลายเดือน–ปีหลังแผล</text>
 <text x="560" y="226" text-anchor="middle" class="t2">ไม่ยุบ · ตัดแล้วเป็นซ้ำบ่อย</text>
 <text x="370" y="252" text-anchor="middle" class="t3">ทั้งคู่เป็นก้อนนูนแข็งยืดหยุ่น หลายสี · first line ของทั้งคู่ = intralesional steroid</text>
</svg>''', "ดูว่าก้อนอยู่ในเส้นขอบแผลเดิมหรือลามออกไป — ลามเกินคือ keloid ซึ่งไม่ยุบเองและตัดแล้วกลับมาบ่อย")

S3 = sec("derm-10-03", "Hypertrophic scar และ keloid",
    "ทั้งคู่ = ก้อนนูนแข็งยืดหยุ่น · HTS อยู่ในขอบแผล ขึ้น < 1 เดือน ยุบเอง · keloid ลามเกินขอบ ขึ้นเป็นเดือน–ปี ไม่ยุบ เป็นซ้ำบ่อย · first line = intralesional steroid",
    minutes=5, source=f"{D} หน้า 343–347", nl=["2.3.12-3(8)", "B4.2.3-3(1)", "2.3.12(12)"],
    md='''
### สิ่งที่เห็น

- ทั้งคู่: **rubbery to firm plaque/nodule** · สีได้หลายแบบ (แดง ชมพู น้ำตาล) · คัน/เจ็บได้

[[fig:derm-10-03-f1]]

| | **Hypertrophic scar** | **Keloid** |
|---|---|---|
| ขอบเขต | **confined to borders** (อยู่ในขอบแผลเดิม) | **extend beyond borders** |
| เริ่ม | **< 1 เดือน** หลังแผล | **เดือน–ปี** |
| พยากรณ์ | **ยุบลงเองตามเวลา** | **ไม่ยุบ** |
| เป็นซ้ำหลังตัด | **น้อย** | **บ่อย** |
| ตำแหน่ง (เสริม) | ข้อต่อที่ตึง แผลไหม้ | ติ่งหู อก ไหล่ หลังบน · คนผิวเข้ม |

### การรักษา (สไลด์หน้า 345)

- **1st line: intralesional steroid injection** (triamcinolone)
- **Physical**: **cryotherapy, laser, radiation, compression therapy**
- **Surgical** — keloid ห้ามตัดอย่างเดียว เพราะเป็นซ้ำและใหญ่กว่าเดิม ต้องร่วมกับ intralesional steroid/radiation หลังผ่าตัด (เสริม)
- **Topical: silicone gel/sheet, vitamin E**
''',
    figs=[F_SCAR],
    pearls=[
        "HTS อยู่ในขอบแผล ขึ้นเร็ว ยุบเอง · keloid ลามเกินขอบ ขึ้นช้า ไม่ยุบ เป็นซ้ำบ่อย",
        "First line ทั้งคู่ = intralesional steroid",
        "Keloid ห้ามตัดอย่างเดียว (เป็นซ้ำ)",
    ],
    items=[
        mcq("DERM-10-03-1", """A 25-year-old woman has a firm, rubbery, itchy nodule on her earlobe that appeared 6 months after ear piercing and has grown well beyond the original piercing site. What is the most appropriate first-line management?""",
            "Intralesional corticosteroid injection", ["Topical corticosteroid", "Simple excision alone", "Silicone gel alone", "Excision followed only by topical corticosteroid"],
            explain="""ก้อนแข็งที่ติ่งหู ขึ้นหลังเจาะหลายเดือนและ **ลามเกินขอบแผลเดิม** = **keloid** → **first line: intralesional steroid injection** (สไลด์หน้า 344–347)
- Topical steroid ซึมไม่ถึงชั้น dermis ที่หนาของ keloid
- การตัดอย่างเดียวทำให้เป็นซ้ำบ่อยและมักใหญ่กว่าเดิม
- Silicone gel ใช้เสริม/ป้องกัน แต่ไม่ใช่ first line สำหรับ keloid ที่โตแล้ว
- ตัดแล้วทา steroid ไม่ป้องกันการเป็นซ้ำได้พอ ต้องฉีด steroid เข้ารอยโรค""",
            pearl="Keloid → intralesional steroid เป็น first line",
            topic="Keloid tx", ref=[f"{D} หน้า 345–347"], nl=["2.3.12-3(8)"], kind="old", src=OLD),
        mcq("DERM-10-03-2", """A 30-year-old man had a laceration on his forearm repaired 3 weeks ago. The scar is now raised, red and firm but remains exactly within the boundaries of the original wound. Which feature best predicts its course compared with a keloid?""",
            "It tends to regress over time and rarely recurs after excision", ["It will continue to grow beyond the wound margins for years", "It recurs frequently after excision", "It typically appears months to years after injury", "It should be excised immediately to prevent malignant change"],
            explain="""แผลนูนแดงขึ้น **< 1 เดือน** และ **อยู่ในขอบแผลเดิม** = **hypertrophic scar** ซึ่ง **ยุบลงเองตามเวลาและเป็นซ้ำน้อย** (สไลด์หน้า 344)
- การลามเกินขอบแผลเป็นปีเป็นลักษณะของ keloid
- การเป็นซ้ำบ่อยหลังตัดเป็นของ keloid
- การขึ้นหลังแผลหลายเดือนถึงปีเป็นของ keloid
- Hypertrophic scar ไม่ใช่รอยโรคก่อนมะเร็ง ไม่ต้องตัดด่วน""",
            pearl="HTS: ใน < 1 เดือน อยู่ในขอบแผล ยุบเอง",
            topic="HTS vs keloid", ref=[f"{D} หน้า 344"], nl=["2.3.12-3(8)"]),
    ])

# ---------------------------------------------------------------- 10-04 Xanthoma
S4 = sec("derm-10-04", "Xanthoma (xanthomatosis)",
    "สัมพันธ์ dyslipidemia · xanthelasma = ปื้นเหลืองที่เปลือกตาบน (cholesterol สูง, cholestasis) · eruptive xanthoma = ตุ่มเล็กแดงเหลืองที่ก้น ไหล่ แขนขา (TG สูงมาก) → lipid profile",
    minutes=4, source=f"{D} หน้า 348–352", nl=["2.1.50", "2.3.2(1)"],
    md='''
### ภาพรวม

- **Xanthoma = macrophage กลืนไขมันสะสมในผิว** · **สัมพันธ์กับ dyslipidemia** (primary หรือ secondary: DM, hypothyroid, nephrotic, cholestasis (เสริม))

| ชนิด | สิ่งที่เห็น | ไขมันที่สัมพันธ์ |
|---|---|---|
| **Xanthelasma** | **ปื้น/แผ่นเหลืองนุ่มที่เปลือกตาบน** (มุมตาด้านใน) สองข้าง | cholesterol สูง (แต่ครึ่งหนึ่ง lipid ปกติ (เสริม)) · **cholestasis (PBC)** |
| **Eruptive xanthoma** | **ตุ่มเล็ก 1–4 mm สีแดงเหลือง** ขึ้นพร้อมกันเป็นกลุ่ม ที่ **ก้น ไหล่ ด้าน extensor ของแขนขา** อาจคัน | **TG สูงมาก** (> 1,000 mg/dL (เสริม)) → เสี่ยง **pancreatitis** |
| Tendinous (เสริม) | ก้อนแข็งที่เอ็นร้อยหวาย หลังมือ | familial hypercholesterolemia (LDL สูง) |
| Tuberous (เสริม) | ก้อนเหลืองที่ข้อศอก เข่า | dysbetalipoproteinemia |

### การตรวจและรักษา

- **Lipid profile** (+ FBS, TSH, LFT หา secondary cause (เสริม))
- รักษา dyslipidemia (eruptive ยุบหลังลด TG) · xanthelasma อาจผ่าตัด/laser (เสริม)
''',
    pearls=[
        "Xanthelasma = ปื้นเหลืองเปลือกตาบน · สัมพันธ์ cholesterol สูง/cholestasis",
        "Eruptive xanthoma = ตุ่มเล็กแดงเหลืองที่ก้น ไหล่ แขนขา = TG สูงมาก (เสี่ยง pancreatitis)",
        "Xanthoma → ตรวจ lipid profile",
    ],
    items=[
        mcq("DERM-10-04-1", """A 36-year-old woman has crops of small (2–3 mm) yellow-red papules with erythematous halos that appeared suddenly on her buttocks, shoulders and the extensor surfaces of her arms and legs. She has poorly controlled type 2 diabetes. What is the most appropriate investigation?""",
            "Lipid profile", ["Serum uric acid", "Blood culture for fungus", "Skin biopsy", "Serum calcium"],
            explain="""ตุ่มเล็กแดงเหลืองขึ้นพร้อมกันที่ก้น ไหล่ แขนขา = **eruptive xanthoma** จาก **triglyceride สูงมาก** (เบาหวานคุมไม่ดีเป็นสาเหตุ secondary) → **lipid profile** (สไลด์หน้า 348–350)
- Uric acid ใช้กับ gouty tophi ซึ่งเป็นก้อนขาวแข็งที่ข้อและใบหู
- Blood culture for fungus ใช้เมื่อสงสัย disseminated fungal infection ในผู้ป่วยภูมิต่ำมีไข้ (เช่น ตุ่มสะดือบุ๋มของ talaromycosis)
- Skin biopsy ไม่จำเป็นเมื่อภาพชัดเจนและ lipid ยืนยันได้
- Calcium ไม่เกี่ยวกับ xanthoma""",
            pearl="ตุ่มเล็กแดงเหลืองที่ก้น/extensor = eruptive xanthoma → lipid profile (TG)",
            topic="Eruptive xanthoma", ref=[f"{D} หน้า 349–350"], nl=["2.1.50"], kind="old", src=OLD),
        mcq("DERM-10-04-2", """A 50-year-old woman has had jaundice and pruritus for several weeks. Laboratory tests show cholesterol 350 mg/dL and triglyceride 250 mg/dL, with markedly elevated ALP. Which skin finding is most likely to be found?""",
            "Xanthelasma", ["Eczema", "Lipoma", "Seborrheic dermatitis", "Acanthosis nigricans"],
            explain="""Cholestasis (ตัวเหลือง คัน ALP สูง) ทำให้ **cholesterol สูง** → **xanthelasma** (ปื้นเหลืองที่เปลือกตาบน) (สไลด์หน้า 348, 351–352) · ตัวอย่างคลาสสิกคือ primary biliary cholangitis (เสริม)
- Eczema ไม่สัมพันธ์จำเพาะกับไขมันสูง (แม้คันจากน้ำดีจะทำให้มีรอยเกา)
- Lipoma เป็นก้อนไขมันนุ่มใต้ผิว ไม่สัมพันธ์กับระดับ cholesterol
- Seborrheic dermatitis สัมพันธ์กับ Malassezia ไม่ใช่ไขมันในเลือด
- Acanthosis nigricans สัมพันธ์กับ insulin resistance ไม่ใช่ cholestasis""",
            pearl="Cholestasis + cholesterol สูง → xanthelasma",
            topic="Xanthelasma", ref=[f"{D} หน้า 351–352"], nl=["2.1.50"], kind="old", src=OLD),
    ])

# ---------------------------------------------------------------- 10-05 Malignant tumor
F_ABCDE = fig("derm-10-05-f1", "ABCDE ของ melanoma (เทียบไฝปกติ)", '''<svg viewBox="0 0 740 300">
 <text x="20" y="24" class="tb">ไฝปกติ</text>
 <circle cx="60" cy="80" r="22" class="c2soft"/>
 <circle cx="60" cy="80" r="22" class="lnc2"/>
 <text x="20" y="130" class="t3">กลม สมมาตร</text>
 <text x="20" y="146" class="t3">ขอบเรียบ สีเดียว</text>
 <text x="20" y="162" class="t3">&lt; 5–6 mm คงที่</text>
 <path d="M150 20V290" class="lnf"/>
 <text x="235" y="24" text-anchor="middle" class="ta">A</text>
 <path d="M200 60C210 50 250 52 262 68C270 80 250 100 236 104C222 108 206 96 204 88C200 78 194 68 200 60Z" class="c2"/>
 <text x="235" y="130" text-anchor="middle" class="t2">Asymmetry</text>
 <text x="235" y="148" text-anchor="middle" class="t3">สองซีกไม่เหมือนกัน</text>
 <text x="350" y="24" text-anchor="middle" class="ta">B</text>
 <path d="M320 64L332 56L340 66L352 54L364 62L376 58L374 74L384 84L370 92L372 104L356 98L346 108L338 96L322 100L326 86L314 78Z" class="c2"/>
 <text x="350" y="130" text-anchor="middle" class="t2">Border</text>
 <text x="350" y="148" text-anchor="middle" class="t3">ขอบหยักไม่ชัด</text>
 <text x="465" y="24" text-anchor="middle" class="ta">C</text>
 <circle cx="465" cy="80" r="26" class="c2"/>
 <circle cx="455" cy="74" r="10" class="bad"/>
 <circle cx="476" cy="90" r="8" class="miss"/>
 <circle cx="472" cy="68" r="6" class="sunk"/>
 <text x="465" y="130" text-anchor="middle" class="t2">Color</text>
 <text x="465" y="148" text-anchor="middle" class="t3">หลายสีในก้อนเดียว</text>
 <text x="580" y="24" text-anchor="middle" class="ta">D</text>
 <circle cx="580" cy="80" r="30" class="c2"/>
 <path d="M550 118H610" class="ln"/>
 <path d="M550 113V123 M610 113V123" class="ln"/>
 <text x="580" y="140" text-anchor="middle" class="t2">Diameter</text>
 <text x="580" y="158" text-anchor="middle" class="t3">&gt; 5 mm (สไลด์)</text>
 <text x="580" y="174" text-anchor="middle" class="t3">ตำรา &gt; 6 mm</text>
 <text x="690" y="24" text-anchor="middle" class="ta">E</text>
 <circle cx="676" cy="70" r="12" class="c2soft"/>
 <path d="M690 78L702 88" class="ln"/>
 <circle cx="706" cy="98" r="18" class="c2"/>
 <text x="690" y="140" text-anchor="middle" class="t2">Evolving</text>
 <text x="690" y="158" text-anchor="middle" class="t3">ขนาด รูป สี</text>
 <text x="690" y="174" text-anchor="middle" class="t3">เปลี่ยนไป</text>
 <rect x="170" y="200" width="560" height="90" rx="10" class="badsoft"/>
 <text x="186" y="224" class="tb">พบ ≥ 1 ข้อ → excisional biopsy (ยืนยัน) → wide excision</text>
 <text x="186" y="248" class="t2">Superficial spreading = ชนิดที่พบบ่อยสุด (โดยรวม)</text>
 <text x="186" y="270" class="t3">คนเอเชีย/ไทย: acral lentiginous ที่ฝ่าเท้า ใต้เล็บ พบมากที่สุด (เสริม)</text>
</svg>''', "ไฝที่ไม่สมมาตร ขอบหยัก หลายสี ใหญ่ หรือเปลี่ยนแปลง ต้องตัดชิ้นเนื้อ — ในคนไทยให้ดูฝ่าเท้าและใต้เล็บด้วย")

S5 = sec("derm-10-05", "Malignant skin tumor: melanoma, SCC, BCC",
    "Melanoma = ABCDE (D > 5 mm ในสไลด์) → biopsy → wide excision · SCC = ตุ่ม/แผ่นหนามีแผลกลางที่โดนแดด, chronic wound (Marjolin) · BCC = ตุ่มมุก (pearly) ขอบม้วน (rolled border) แผลกลาง โตช้า ไม่เจ็บ · biopsy → resection",
    minutes=8, source=f"{D} หน้า 353–363", nl=["2.3.2-3(2)", "B4.2.4-3(1)", "B4.2.4-3(2)"],
    md='''
### Malignant melanoma

- **Risk: UV exposure, ผิวขาว, dysplastic nevi, ประวัติครอบครัวเป็น melanoma**
- **ABCDE**: **A**symmetry · **B**order (ขอบหยัก ไม่ชัด) · **C**olor (หลายสี) · **D**iameter (**> 5 mm** ตามสไลด์; ตำราส่วนใหญ่ใช้ > 6 mm) · **E**volving (ขนาด รูป สีเปลี่ยน)
- **Skin biopsy (confirm diagnosis)** — excisional biopsy ขอบ 1–3 mm (เสริม)
- **Tx: wide excision**
- **Superficial spreading melanoma = ชนิดที่พบบ่อยที่สุด** (โดยรวม) · ในคนเอเชีย/ไทย **acral lentiginous** (ฝ่าเท้า ฝ่ามือ ใต้เล็บ — Hutchinson sign ที่ nail fold) พบมากที่สุด (เสริม)
- ชนิดอื่น (สไลด์หน้า 356 เป็นภาพ — เสริม): nodular (โตเร็ว ก้อนนูนดำ), lentigo maligna (หน้าผู้สูงอายุ)

[[fig:derm-10-05-f1]]

### Squamous cell carcinoma (SCC)

- **Risk: UV, ผิวขาว, immunosuppression (หลังปลูกถ่ายอวัยวะ), radiation, chronic wound** (แผลเรื้อรัง/แผลเป็นไฟไหม้ → **Marjolin ulcer** (เสริม)), สารหนู, HPV (เสริม)
- **Hyperkeratotic papule/plaque + central ulceration** บน **sun-exposed areas** (หน้า หู ริมฝีปากล่าง หลังมือ)
- รอยโรคก่อนมะเร็ง: actinic keratosis (เสริม)
- **Skin biopsy → tumor resection**

### Basal cell carcinoma (BCC) — มะเร็งผิวหนังที่พบบ่อยที่สุด (เสริม)

- **Risk: UV, ผิวขาว**
- **Painless, slow-growing pearly papule/nodule/plaque** · **rolled borders** (ขอบม้วนนูนมันวาวคล้ายมุก) · **central depression/erosion/ulceration** (rodent ulcer) · เห็นเส้นเลือดฝอย (telangiectasia) บนผิว (เสริม)
- **Sun-exposed areas** (หน้า โดยเฉพาะจมูก หน้าผาก ส่วนบนของหน้า)
- **Nodular type = ชนิดที่พบบ่อยที่สุด** · คนไทยมักเป็น **pigmented BCC** (มีสีดำน้ำตาล) (เสริม)
- แพร่กระจายน้อยมาก แต่ทำลายเนื้อเยื่อเฉพาะที่ (เสริม)
- **Skin biopsy → tumor resection** (Mohs surgery ที่หน้า (เสริม))

| | Melanoma | SCC | BCC |
|---|---|---|---|
| ลักษณะ | ไฝ ABCDE | ตุ่ม/แผ่นหนา keratin + แผลกลาง | **ตุ่มมุก ขอบม้วน + แผลกลาง** |
| โต | เปลี่ยนแปลงเร็ว | ปานกลาง | **ช้ามาก ไม่เจ็บ** |
| ปัจจัยเสี่ยงเด่น | dysplastic nevi, FHx | **ภูมิต่ำ, แผลเรื้อรัง, radiation** | UV |
| แพร่กระจาย | สูง | ปานกลาง | น้อยมาก |
| รักษา | wide excision | resection | resection |
''',
    figs=[F_ABCDE],
    pearls=[
        "Melanoma ABCDE (D > 5 mm ในสไลด์) → biopsy → wide excision · superficial spreading พบบ่อยสุด",
        "คนไทย melanoma มักเป็น acral lentiginous (ฝ่าเท้า ใต้เล็บ) (เสริม)",
        "SCC = hyperkeratotic plaque + แผลกลาง · ภูมิต่ำ แผลเรื้อรัง (Marjolin) radiation",
        "BCC = ตุ่มมุกขอบม้วน + แผลกลาง โตช้าไม่เจ็บ ที่หน้า · nodular พบบ่อยสุด",
    ],
    items=[
        mcq("DERM-10-05-1", """A 50-year-old woman has had a painless mass on her forehead for 2 years. It grows slowly and occasionally bleeds. Examination shows a 1-cm raised lesion with pearly, rolled edges, fine surface telangiectasia and a central ulcer. What is the most likely diagnosis?""",
            "Basal cell carcinoma", ["Seborrheic keratosis", "Epidermal inclusion cyst", "Squamous cell carcinoma", "Keratoacanthoma"],
            explain="""ก้อน **โตช้า ไม่เจ็บ** ที่หน้าผาก ขอบ **มุก ม้วน (pearly rolled border)** + เส้นเลือดฝอย + **แผลกลาง** = **basal cell carcinoma** (สไลด์หน้า 358, 362–363)
- Seborrheic keratosis เป็นตุ่มสีน้ำตาลผิวขรุขระ "แปะติด" (stuck-on) ไม่มีขอบมุกหรือแผล (เสริม)
- Epidermal inclusion cyst เป็นก้อนกลมใต้ผิว มีรูเปิดตรงกลาง บีบได้ไขขาว
- SCC เป็นแผ่นหนา keratin มีแผลกลาง แต่ไม่มีขอบมุกม้วน และโตเร็วกว่า
- Keratoacanthoma เป็นก้อนรูปโดมมีหลุม keratin ตรงกลาง โตเร็วในไม่กี่สัปดาห์ (เสริม)""",
            pearl="ตุ่มมุก ขอบม้วน แผลกลาง โตช้าที่หน้า = BCC",
            topic="BCC", ref=[f"{D} หน้า 362–363"], nl=["B4.2.4-3(1)", "2.3.2-3(2)"], kind="old", src=OLD),
        mcq("DERM-10-05-2", """A 58-year-old man has a pigmented lesion on his upper back that his wife says has enlarged over 6 months. It measures 9 mm, is asymmetric, has an irregular notched border and contains black, brown and reddish areas. What is the most appropriate next step?""",
            "Excisional biopsy of the lesion", ["Reassure and review in 1 year", "Cryotherapy", "Shave the raised portion for cosmetic reasons", "Topical imiquimod"],
            explain="""ไฝที่ **Asymmetry, Border ไม่เรียบ, Color หลายสี, Diameter > 5 mm, Evolving** = สงสัย **melanoma** → **skin biopsy (excisional) เพื่อยืนยัน** แล้วจึง wide excision (สไลด์หน้า 354)
- การรอ 1 ปีทำให้มะเร็งลุกลามลึกขึ้นและพยากรณ์แย่ลง
- Cryotherapy ทำลายเนื้อเยื่อโดยไม่ได้ชิ้นเนื้อมาตรวจความลึก (Breslow) ซึ่งกำหนดการรักษา
- การ shave บางส่วนตัดความลึกของก้อนไม่ครบ ทำให้ประเมินระยะไม่ได้
- Imiquimod ไม่ใช่การรักษา melanoma ที่ยังไม่ได้วินิจฉัย""",
            pearl="ไฝ ABCDE → excisional biopsy",
            topic="Melanoma", ref=[f"{D} หน้า 354"], nl=["B4.2.4-3(2)", "2.3.2-3(2)"]),
        mcq("DERM-10-05-3", """A 52-year-old man had a severe flame burn of his leg 30 years ago. For the past 4 months a chronic ulcer within the old burn scar has enlarged, with a heaped-up, indurated, hyperkeratotic edge and foul discharge. What is the most likely diagnosis?""",
            "Squamous cell carcinoma arising in a chronic wound", ["Basal cell carcinoma", "Venous ulcer", "Pyoderma gangrenosum", "Keloid"],
            explain="""**แผลเรื้อรัง/แผลเป็นไฟไหม้** เป็นปัจจัยเสี่ยงของ **SCC** (chronic wound ตามสไลด์; Marjolin ulcer (เสริม)) — แผลโตขึ้น ขอบนูนแข็ง keratin หนา (สไลด์หน้า 357)
- BCC เกิดที่ผิวโดนแดด เป็นตุ่มมุกขอบม้วน ไม่ค่อยเกิดในแผลเป็นไฟไหม้
- Venous ulcer อยู่ที่ medial malleolus ร่วมกับ varicose veins ไม่ได้มีขอบนูนแข็ง keratin
- Pyoderma gangrenosum เป็นแผลขอบม่วงเซาะใต้ขอบ สัมพันธ์ IBD
- Keloid เป็นก้อนนูนไม่เป็นแผล""",
            pearl="แผลเรื้อรัง/แผลไฟไหม้ที่เปลี่ยนไป = SCC (Marjolin) → biopsy",
            topic="SCC", ref=[f"{D} หน้า 357"], nl=["B4.2.4-3(3)", "2.3.2-3(2)"]),
        mcq("DERM-10-05-4", """A 61-year-old kidney transplant recipient on tacrolimus and mycophenolate has several rapidly enlarging, tender, scaly papules with central ulceration on the backs of his hands and ears. Which skin cancer is he at greatest increased risk of developing?""",
            "Squamous cell carcinoma", ["Basal cell carcinoma", "Malignant melanoma", "Dermatofibroma", "Seborrheic keratosis"],
            explain="""**Immunosuppression** (โดยเฉพาะหลังปลูกถ่ายอวัยวะ) เป็นปัจจัยเสี่ยงสำคัญของ **SCC** ตามสไลด์ — รอยโรคเป็นตุ่มขุยหนามีแผลกลางที่ผิวโดนแดด (สไลด์หน้า 357; ความเสี่ยงเพิ่มหลายสิบเท่า (เสริม))
- BCC ก็เพิ่มขึ้นได้แต่น้อยกว่า และลักษณะเป็นตุ่มมุกโตช้าไม่เจ็บ
- Melanoma เพิ่มขึ้นเล็กน้อยเท่านั้น และเป็นรอยโรคสีดำตาม ABCDE
- Dermatofibroma เป็นตุ่มแข็งไม่ใช่มะเร็ง บุ๋มเมื่อบีบ
- Seborrheic keratosis เป็นเนื้องอกไม่ร้าย""",
            pearl="ภูมิต่ำ (post-transplant) → SCC",
            topic="SCC risk", ref=[f"{D} หน้า 357"], nl=["B4.2.4-3(3)"]),
    ])

LECTURE = lecture("10", "Pigment, hair, scars & tumors", subtitle="vitiligo · alopecia · hypertrophic scar/keloid · xanthoma · melanoma/SCC/BCC",
    objectives=[
        "แยกด่างขาว (vitiligo, pityriasis alba, PV, leprosy) ด้วยลักษณะและการตรวจข้างเตียง",
        "ใช้ pattern, pull test, trichogram และเวลา แยก AA, trichotillomania, TE, AE และ AGA",
        "แยก hypertrophic scar กับ keloid และให้ intralesional steroid",
        "จำ xanthoma กับชนิดไขมัน และแยก melanoma/SCC/BCC จากคำบรรยาย",
    ],
    sections=[S1, S2, S3, S4, S5])
