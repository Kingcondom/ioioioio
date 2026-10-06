from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Infectious"

# ---------------------------------------------------------------- 06-01 Syphilis
F_SYPH = fig("id-06-01-f1", "Timeline ของ syphilis และการรักษาแต่ละระยะ", '''<svg viewBox="0 0 740 330">
 <defs><marker id="id-06-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <path d="M20 110H720" class="ln" marker-end="url(#id-06-01-a)"/>
 <text x="20" y="130" class="t3">ติดเชื้อ</text>
 <text x="300" y="130" class="t3">1 ปี</text>
 <path d="M310 96V118" class="lnf"/>
 <text x="660" y="130" class="t3">หลายปี</text>
 <rect x="20" y="20" width="120" height="70" rx="10" class="c1soft"/>
 <text x="80" y="42" text-anchor="middle" class="tb">Primary</text>
 <text x="80" y="62" text-anchor="middle" class="t3">chancre เดี่ยวไม่เจ็บ</text>
 <text x="80" y="80" text-anchor="middle" class="t3">หายเอง 3–10 wk</text>
 <rect x="146" y="20" width="150" height="70" rx="10" class="c2soft"/>
 <text x="221" y="42" text-anchor="middle" class="tb">Secondary</text>
 <text x="221" y="62" text-anchor="middle" class="t3">2–10 wk หลัง primary</text>
 <text x="221" y="80" text-anchor="middle" class="t3">ผื่นฝ่ามือฝ่าเท้า</text>
 <rect x="230" y="140" width="80" height="44" rx="8" class="sunk"/>
 <text x="270" y="160" text-anchor="middle" class="t2">Early</text>
 <text x="270" y="176" text-anchor="middle" class="t2">latent</text>
 <rect x="316" y="140" width="150" height="44" rx="8" class="sunk"/>
 <text x="391" y="167" text-anchor="middle" class="t2">Late latent (&gt; 1 ปี)</text>
 <rect x="472" y="20" width="248" height="70" rx="10" class="badsoft"/>
 <text x="596" y="42" text-anchor="middle" class="tb">Tertiary</text>
 <text x="596" y="62" text-anchor="middle" class="t3">gumma · CV syphilis (aortitis)</text>
 <text x="596" y="80" text-anchor="middle" class="t3">tabes dorsalis</text>
 <rect x="20" y="200" width="290" height="58" rx="10" class="ok"/>
 <text x="165" y="222" text-anchor="middle" class="tw">Early syphilis (&lt; 1 ปี)</text>
 <text x="165" y="244" text-anchor="middle" class="tw">Benzathine PenG 2.4 MU IM × 1</text>
 <rect x="316" y="200" width="404" height="58" rx="10" class="miss"/>
 <text x="518" y="222" text-anchor="middle" class="tw">Late syphilis (&gt; 1 ปี / ไม่ทราบ)</text>
 <text x="518" y="244" text-anchor="middle" class="tw">Benzathine PenG 2.4 MU IM weekly × 3</text>
 <rect x="20" y="268" width="700" height="50" rx="10" class="bad"/>
 <text x="370" y="290" text-anchor="middle" class="tw">Neurosyphilis เกิดได้ทุกระยะ → aqueous crystalline penicillin G IV</text>
 <text x="370" y="308" text-anchor="middle" class="tw">(18–24 MU/day 10–14 วัน (เสริม))</text>
</svg>''', "ตัดแบ่งที่ 1 ปี: ก่อนหน้า (primary, secondary, early latent) ฉีดเข็มเดียว · หลัง 1 ปีหรือไม่ทราบระยะ ฉีดสัปดาห์ละครั้ง 3 ครั้ง · neurosyphilis ต้องให้ IV")

F_SERO = fig("id-06-01-f2", "แปลผล serology ของ syphilis", '''<svg viewBox="0 0 740 260">
 <rect x="10" y="10" width="220" height="40" rx="8" class="sunk"/>
 <text x="120" y="35" text-anchor="middle" class="tb">ผล</text>
 <rect x="236" y="10" width="240" height="40" rx="8" class="c1soft"/>
 <text x="356" y="35" text-anchor="middle" class="tb">Treponemal + (TPHA, FTA)</text>
 <rect x="482" y="10" width="248" height="40" rx="8" class="sunk"/>
 <text x="606" y="35" text-anchor="middle" class="tb">Treponemal −</text>
 <rect x="10" y="58" width="220" height="90" rx="8" class="c2soft"/>
 <text x="120" y="96" text-anchor="middle" class="tb">Non-treponemal +</text>
 <text x="120" y="118" text-anchor="middle" class="t3">(VDRL, RPR)</text>
 <rect x="236" y="58" width="240" height="90" rx="8" class="bad"/>
 <text x="356" y="90" text-anchor="middle" class="tw">Active syphilis</text>
 <text x="356" y="112" text-anchor="middle" class="tw">→ รักษา + ติดตาม titer</text>
 <text x="356" y="132" text-anchor="middle" class="tw">ของ VDRL/RPR</text>
 <rect x="482" y="58" width="248" height="90" rx="8" class="misssoft"/>
 <text x="606" y="90" text-anchor="middle" class="tb">Biological false positive</text>
 <text x="606" y="112" text-anchor="middle" class="t3">SLE, APS, ตั้งครรภ์, HIV,</text>
 <text x="606" y="130" text-anchor="middle" class="t3">TB, malaria, IVDU</text>
 <rect x="10" y="156" width="220" height="90" rx="8" class="sunk"/>
 <text x="120" y="206" text-anchor="middle" class="tb">Non-treponemal −</text>
 <rect x="236" y="156" width="240" height="90" rx="8" class="c1soft"/>
 <text x="356" y="186" text-anchor="middle" class="tb">เคยเป็นและรักษาแล้ว</text>
 <text x="356" y="208" text-anchor="middle" class="t3">หรือ primary ระยะแรกมาก</text>
 <text x="356" y="228" text-anchor="middle" class="t3">หรือ late latent</text>
 <rect x="482" y="156" width="248" height="90" rx="8" class="oksoft"/>
 <text x="606" y="206" text-anchor="middle" class="tb">ไม่ติดเชื้อ</text>
</svg>''', "ต้องใช้ทั้งสองชนิด: treponemal ยืนยันว่าเคยติดเชื้อ (บวกตลอดชีวิต) · non-treponemal บอกว่ายัง active และใช้ติดตามการรักษา (สไลด์หน้า 200–204 เป็นภาพ สรุปเสริม)")

S1 = sec("id-06-01", "Syphilis",
    "T. pallidum · chancre เดี่ยวไม่เจ็บ → ผื่นฝ่ามือฝ่าเท้า condyloma lata → latent → tertiary · VDRL/RPR + TPHA · BPG 2.4 MU × 1 (early) หรือ weekly × 3 (late) · neuro IV PGS",
    minutes=10, source=f"{D} หน้า 193–214", nl=["2.3.1(19)", "B10.2.2(1)", "2.1.48"],
    md='''
### เชื้อและการแบ่งระยะ

- **Treponema pallidum** (spirochete) · ติดทาง **เพศสัมพันธ์** และ **แม่สู่ลูก**

| กลุ่ม | ระยะ |
|---|---|
| **Early syphilis** | Primary · Secondary · **Early latent (< 1 ปี)** |
| **Late syphilis** | **Late latent (> 1 ปี)** · Latent ไม่ทราบระยะเวลา · Tertiary |
| **Neurosyphilis** | **เกิดได้ทุกระยะ** |

[[fig:id-06-01-f1]]

### Primary syphilis

- **Single painless chancre** · **clean base, indurated border**
- **Painless inguinal lymphadenopathy**
- **หายได้เอง 3–10 สัปดาห์** (ไม่ได้แปลว่าหายจากโรค)

### Secondary syphilis (2–10 สัปดาห์หลัง primary)

- **Disseminated disease**: fever, malaise, **generalized lymphadenopathy**
- **Generalized MP rash** ทั้ง trunk, extremities และ **palms & soles** (ไม่คัน)
- **Condylomata lata**: painless, ผื่นนูนขาวชื้นที่อวัยวะเพศ ผิวมัน (glazed top)
- **Moth-eaten alopecia** · mucous patch, hepatitis, nephritis (เสริม)

### Latent syphilis

- **Asymptomatic** (ยังไม่หาย แค่ไม่มีอาการ) — early latent < 1 ปี · late latent > 1 ปี · ไม่ทราบระยะ → รักษาแบบ late

### Tertiary syphilis (หลายปีหลัง secondary)

- **Gumma**: chronic granuloma มีเนื้อตายตรงกลาง ที่ผิวหนัง อวัยวะภายใน กระดูก CNS
- **Cardiovascular syphilis**: aortitis → aortic aneurysm/AR (เสริม)
- **Neurosyphilis** (ทุกระยะ): meningitis, stroke, uveitis, SNHL · **tabes dorsalis** (เสีย proprioception, Romberg +) · general paresis · Argyll Robertson pupil (เสริม)

### Investigation

- **Direct detection**: dark-field microscopy (จากแผล chancre/condyloma) · DFA, NAAT
- **Serology — ต้องใช้ทั้งสองชนิด**

| ชนิด | ตัวอย่าง | ใช้ทำอะไร |
|---|---|---|
| **Treponemal test (TT)** | FTA-ABS, TPPA, **TPHA**, immunoassay (ELISA, EIA, CIA, CMIA) | **Confirm diagnosis** · **บวกตลอดไป** ใช้ติดตามการรักษาไม่ได้ |
| **Non-treponemal test (NTT)** | **RPR, VDRL** | Screening + **ติดตามการรักษา** (titer ลด ≥ 4 เท่า = ตอบสนอง) |

[[fig:id-06-01-f2]]

### Management

| ระยะ | ยาหลัก | แพ้ penicillin |
|---|---|---|
| **Early (< 1 ปี)** | **Benzathine penicillin G 2.4 MU IM single dose** | Doxycycline, tetracycline, azithromycin, ceftriaxone, erythromycin |
| **Late (> 1 ปี)/ไม่ทราบ** | **Benzathine penicillin G 2.4 MU IM weekly × 3** | Doxycycline, tetracycline |
| **Neurosyphilis** | **Aqueous crystalline penicillin G IV** | (desensitization) |

- **Partner**: early — รักษาคู่นอนในช่วง **90 วัน** ก่อนผู้ป่วยมีอาการ (แม้ไม่มีอาการ) · late — รักษาคู่นอนเมื่อผลเลือดผิดปกติ
- **ตั้งครรภ์ + แพ้ penicillin → penicillin desensitization** แล้วรักษาด้วย penicillin G (ยาอื่นไม่ป้องกัน congenital syphilis)
- **F/U NTT (VDRL/RPR)** ดูการตอบสนอง · แนะนำ **คัดกรอง HIV, hepatitis B, C**
- Jarisch-Herxheimer reaction: ไข้ หนาวสั่น ปวดเมื่อยภายใน 24 ชม.หลังฉีด (เสริม)

> ผื่นที่ **ฝ่ามือฝ่าเท้า** + LN ทั่วตัว ในคนอายุน้อย → **VDRL/RPR** เสมอ (แม้ไม่มีแผลที่อวัยวะเพศหรือไม่ยอมรับประวัติเสี่ยง)
''',
    figs=[F_SYPH, F_SERO],
    pearls=[
        "Primary: chancre เดี่ยว ไม่เจ็บ ขอบแข็ง พื้นสะอาด + LN ไม่เจ็บ",
        "Secondary: ผื่นฝ่ามือฝ่าเท้า + condyloma lata + moth-eaten alopecia",
        "Treponemal บวกตลอดชีวิต · VDRL/RPR ใช้ติดตามการรักษา",
        "Early: BPG 2.4 MU IM × 1 · late: weekly × 3 · neuro: IV aqueous PenG",
        "ตั้งครรภ์แพ้ penicillin → desensitize แล้วให้ penicillin",
    ],
    items=[
        mcq("ID-06-01-1",
            "A 20-year-old man has fever, rash and myalgia for 1 week. Temperature 37.8 °C, PR 98 bpm, BP 100/70 mmHg. There is a maculopapular rash on the trunk, both hands and the soles, with generalized lymphadenopathy, no hepatomegaly and no genital ulcer. What is the most appropriate investigation?",
            "VDRL",
            ["Rubella titer", "Chikungunya titer", "IFA for scrub typhus", "EBV antibody"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ผื่น **MP ที่ฝ่ามือฝ่าเท้า** + LN ทั่วตัว + ไข้ต่ำ = **secondary syphilis** → ตรวจ **VDRL/RPR** (แล้วยืนยันด้วย treponemal test) — ไม่จำเป็นต้องเห็น chancre เพราะหายเองไปแล้ว
- Rubella มีผื่นเริ่มที่หน้า postauricular LN ไม่เด่นฝ่ามือฝ่าเท้า
- Chikungunya เด่นเรื่องปวดข้อและไข้สูง
- Scrub typhus ต้องมีประวัติเข้าป่าและ eschar
- EBV มักมี pharyngitis และ HSM''',
            pearl="ผื่นฝ่ามือฝ่าเท้า + LN ทั่วตัว → VDRL", topic="Secondary syphilis investigation",
            ref=[f"{D} หน้า 195, 207–208"], nl=["2.3.1(19)", "2.1.50"]),
        mcq("ID-06-01-2",
            "A 30-year-old man has an erythematous rash on the palms and soles and patchy hair loss. VDRL is reactive at 1:32 and TPHA is positive. Anti-HIV is non-reactive. He has no drug allergy. What is the first-line management?",
            "Benzathine penicillin G 2.4 million units intramuscularly, single dose",
            ["Benzathine penicillin G 2.4 million units intramuscularly weekly for 3 weeks", "Oral doxycycline for 14 days", "Oral azithromycin single dose", "Aqueous crystalline penicillin G intravenously for 14 days"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (รวมสไลด์หน้า 209–214)",
            explain='''ผื่นฝ่ามือฝ่าเท้า + moth-eaten alopecia + VDRL/TPHA บวก = **secondary syphilis = early syphilis** → **benzathine penicillin G 2.4 MU IM single dose**
- Weekly × 3 ใช้กับ late latent/ไม่ทราบระยะ
- Doxycycline และ azithromycin เป็นทางเลือกเมื่อแพ้ penicillin (azithromycin มีปัญหาดื้อยา)
- IV aqueous penicillin G ใช้กับ neurosyphilis ซึ่งรายนี้ไม่มีอาการทางระบบประสาท''',
            pearl="Secondary syphilis = early → BPG 2.4 MU IM เข็มเดียว", topic="Early syphilis treatment",
            ref=[f"{D} หน้า 205, 209–214"], nl=["2.3.1(19)"]),
        mcq("ID-06-01-3",
            "A 35-year-old woman is found to have reactive RPR (1:8) and positive TPPA on routine pre-employment screening. She has no symptoms or signs, had a negative test 4 years ago, and cannot recall any lesion. CSF examination is not indicated. What is the most appropriate treatment?",
            "Benzathine penicillin G 2.4 million units intramuscularly weekly for 3 weeks",
            ["Benzathine penicillin G 2.4 million units intramuscularly, single dose", "Aqueous crystalline penicillin G intravenously", "No treatment because she is asymptomatic", "Repeat RPR in 6 months before deciding"],
            explain='''ไม่มีอาการ + serology บวกทั้งสองชนิด = **latent syphilis** · ไม่รู้ว่าติดเมื่อไร (ผลลบครั้งสุดท้าย 4 ปีก่อน) → **latent of unknown duration = รักษาแบบ late** → **BPG 2.4 MU IM weekly × 3**
- Single dose ใช้เฉพาะ early (< 1 ปี) ที่มีหลักฐานว่าติดภายใน 1 ปี
- IV aqueous penicillin ใช้กับ neurosyphilis
- Latent ยังไม่หาย แค่ไม่มีอาการ ต้องรักษาเพื่อกัน tertiary
- การรอผลซ้ำทำให้เสียโอกาสรักษา''',
            pearl="Latent ไม่ทราบระยะ = รักษาแบบ late (weekly × 3)", topic="Latent syphilis",
            ref=[f"{D} หน้า 197, 205"], nl=["2.3.1(19)"]),
        mcq("ID-06-01-4",
            "A 26-year-old woman at 14 weeks' gestation has a positive RPR (1:16) and TPHA. She has a documented history of urticaria and wheezing after penicillin. What is the most appropriate management?",
            "Penicillin desensitization followed by benzathine penicillin G",
            ["Oral doxycycline for 14 days", "Oral azithromycin 2 g single dose", "Intramuscular ceftriaxone for 10 days", "Delay treatment until after delivery"],
            explain='''Syphilis ในหญิงตั้งครรภ์ที่แพ้ penicillin → **penicillin desensitization แล้วรักษาด้วย penicillin G** — penicillin เป็นยาเดียวที่ป้องกัน congenital syphilis ได้แน่นอน
- Doxycycline ห้ามในหญิงตั้งครรภ์
- Azithromycin ไม่ผ่านรกได้ดีพอและเชื้อดื้อ
- Ceftriaxone ข้อมูลในการป้องกัน congenital syphilis ไม่พอ
- การรอหลังคลอดเสี่ยง congenital syphilis และทารกตายในครรภ์''',
            pearl="ตั้งครรภ์ + แพ้ penicillin = desensitize", topic="Syphilis in pregnancy",
            ref=[f"{D} หน้า 206"], nl=["2.3.1(19)", "2.3.16-3(1)"]),
        mcq("ID-06-01-5",
            "A 45-year-old man treated for secondary syphilis returns for follow-up. Which test should be used to monitor his response to therapy?",
            "Quantitative RPR titer",
            ["TPHA", "FTA-ABS", "Treponemal enzyme immunoassay", "Dark-field microscopy of a skin scraping"],
            explain='''ใช้ **non-treponemal test (RPR/VDRL) แบบ titer** ติดตามการรักษา — titer ลดลง ≥ 4 เท่า (2 dilution) ภายใน 6–12 เดือน = ตอบสนองดี (เสริม)
- TPHA, FTA-ABS และ treponemal EIA **บวกตลอดไป** จึงใช้ติดตามไม่ได้
- Dark-field ใช้เมื่อมีแผล/condyloma ไม่ใช้ติดตามผล''',
            pearl="ติดตามการรักษา syphilis = RPR/VDRL titer", topic="Syphilis follow-up",
            ref=[f"{D} หน้า 199, 206"], nl=["2.3.1(19)"]),
    ])

# ---------------------------------------------------------------- 06-02 Genital ulcers: chancroid, LGV
F_GUD = fig("id-06-02-f1", "แยก genital ulcer สามโรคแบคทีเรีย", '''<svg viewBox="0 0 740 300">
 <rect x="10" y="10" width="160" height="36" rx="8" class="sunk"/>
 <text x="90" y="33" text-anchor="middle" class="tb">ลักษณะ</text>
 <rect x="176" y="10" width="180" height="36" rx="8" class="c1soft"/>
 <text x="266" y="33" text-anchor="middle" class="tb">Syphilis (chancre)</text>
 <rect x="362" y="10" width="180" height="36" rx="8" class="badsoft"/>
 <text x="452" y="33" text-anchor="middle" class="tb">Chancroid</text>
 <rect x="548" y="10" width="182" height="36" rx="8" class="c2soft"/>
 <text x="639" y="33" text-anchor="middle" class="tb">LGV</text>
 <text x="20" y="74" class="tb">เชื้อ</text>
 <text x="186" y="74" class="t2">T. pallidum</text>
 <text x="372" y="74" class="t2">H. ducreyi</text>
 <text x="558" y="74" class="t2">C. trachomatis L1–L3</text>
 <text x="20" y="108" class="tb">เจ็บแผล</text>
 <text x="186" y="108" class="t2">ไม่เจ็บ</text>
 <text x="372" y="108" class="ta">เจ็บมาก</text>
 <text x="558" y="108" class="t2">ไม่เจ็บ (หายเร็ว)</text>
 <text x="20" y="142" class="tb">จำนวน/พื้นแผล</text>
 <text x="186" y="142" class="t2">เดี่ยว พื้นสะอาด ขอบแข็ง</text>
 <text x="372" y="142" class="t2">หลายแผล พื้นสกปรก เทา</text>
 <text x="558" y="142" class="t2">แผลเล็ก มักไม่ทันเห็น</text>
 <text x="20" y="176" class="tb">ต่อมน้ำเหลือง</text>
 <text x="186" y="176" class="t2">โต ไม่เจ็บ</text>
 <text x="372" y="176" class="ta">เจ็บ (bubo แตกได้)</text>
 <text x="558" y="176" class="ta">เจ็บมาก + groove sign</text>
 <text x="20" y="210" class="tb">Lab</text>
 <text x="186" y="210" class="t2">Dark-field, VDRL+TPHA</text>
 <text x="372" y="210" class="t2">GNCB school of fish</text>
 <text x="558" y="210" class="t2">NAAT C. trachomatis</text>
 <text x="20" y="244" class="tb">ยา</text>
 <text x="186" y="244" class="t2">BPG 2.4 MU IM</text>
 <text x="372" y="244" class="t2">Ceftriaxone / azithro</text>
 <text x="558" y="244" class="t2">Doxycycline 21 วัน</text>
 <text x="20" y="278" class="tb">รักษาคู่นอน</text>
 <text x="186" y="278" class="t2">90 วัน</text>
 <text x="372" y="278" class="t2">10 วัน</text>
 <text x="558" y="278" class="t2">90 วัน (ตามสไลด์)</text>
 <path d="M10 92H730M10 126H730M10 160H730M10 194H730M10 228H730M10 262H730" class="lnf"/>
</svg>''', "แผลเจ็บ + ต่อมเจ็บ = chancroid · แผลไม่เจ็บ + ต่อมไม่เจ็บ = syphilis · แผลหายไปแล้วเหลือต่อมเจ็บข้ามขาหนีบ = LGV · HSV (เสริม) = กลุ่มตุ่มน้ำแผลตื้นเจ็บ")

S2 = sec("id-06-02", "Chancroid & lymphogranuloma venereum",
    "Chancroid: H. ducreyi แผลเจ็บหลายแผล พื้นสกปรก LN เจ็บ school of fish · ceftriaxone/azithro · LGV: C. trachomatis L1–3 แผลไม่เจ็บ bubo เจ็บ groove sign · doxycycline",
    minutes=6, source=f"{D} หน้า 215–221", nl=["2.3.1(19)", "2.1.48"],
    md='''
### Chancroid

- **Haemophilus ducreyi** · sexual transmission
- **Multiple painful genital ulcers** · **grayish necrotic (dirty) base, irregular/ragged border** (ขอบนิ่ม)
- **Painful inguinal lymphadenopathy** (bubo แตกเป็นหนองได้)
- Swab lesion → Gram stain, culture: **Gram-negative coccobacilli/short rod** เรียง **parallel chain (school of fish)**
- **Tx: ceftriaxone, azithromycin** · ciprofloxacin, erythromycin (ceftriaxone 250 mg IM × 1 หรือ azithromycin 1 g PO × 1 (เสริม))
- รักษาคู่นอนในช่วง **10 วัน** ก่อนผู้ป่วยมีอาการ (แม้ไม่มีอาการ)
- แนะนำ **คัดกรอง HIV, syphilis, hepatitis B, C**

### Chancroid vs chancre (syphilis)

| | Chancroid | Chancre |
|---|---|---|
| Pathogen | H. ducreyi | T. pallidum |
| Pain | **Painful** | **Painless** |
| Number | **Multiple** | **Single** |
| Wound base | **Dirty** | **Clean** |
| Lymph node | **Tender** | **Not tender** |

### Lymphogranuloma venereum (LGV)

- **Chlamydia trachomatis serovar L1–L3** · sexual transmission
- **Painless genital ulcer** (เล็ก หายเร็ว มักไม่ทันสังเกต) → **painful swollen inguinal lymphadenopathy** (bubo)
- **Groove sign**: lymph node โต **ทั้งเหนือและใต้ inguinal ligament** เกิดร่องตรง ligament
- Proctocolitis ในชายมีเพศสัมพันธ์กับชาย (เสริม)
- **Ix: NAAT for C. trachomatis**
- **Tx: doxycycline** (100 mg bid **21 วัน** (เสริม)), azithromycin, erythromycin
- รักษาคู่นอนในช่วง **90 วัน** ก่อนมีอาการ (ตามสไลด์; CDC ใช้ 60 วัน) · คัดกรอง HIV, syphilis, HBV, HCV

[[fig:id-06-02-f1]]

> Genital herpes (HSV) — **กลุ่มตุ่มน้ำแตกเป็นแผลตื้นเจ็บ** Tzanck/PCR → acyclovir (เสริม) เป็น DDx สำคัญของ painful genital ulcer
''',
    figs=[F_GUD],
    pearls=[
        "Chancroid: แผลเจ็บหลายแผล พื้นสกปรก + LN เจ็บ · GN coccobacilli school of fish",
        "Chancroid → ceftriaxone หรือ azithromycin · คู่นอน 10 วัน",
        "LGV: แผลไม่เจ็บ + bubo เจ็บ + groove sign · C. trachomatis L1–L3",
        "LGV → doxycycline (21 วัน) · NAAT",
        "Syphilis chancre: เดี่ยว ไม่เจ็บ พื้นสะอาด LN ไม่เจ็บ",
    ],
    items=[
        mcq("ID-06-02-1",
            "A man with recent unsafe sex presents with tender genital ulcers on the penis. Gram stain of an ulcer swab shows Gram-negative coccobacilli arranged in parallel chains. What is the most likely diagnosis?",
            "Chancroid",
            ["Syphilis", "Gonorrhea", "Genital herpes", "Lymphogranuloma venereum"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''แผลเจ็บ + **Gram-negative coccobacilli เรียงขนานกันแบบ school of fish** = **chancroid (H. ducreyi)**
- Syphilis แผลไม่เจ็บ และ T. pallidum ย้อม Gram ไม่ติด (ต้อง dark-field)
- Gonorrhea ทำให้ urethritis มีหนอง ไม่ใช่แผล และเชื้อเป็น Gram-negative intracellular diplococci
- Genital herpes เป็นกลุ่มตุ่มน้ำ แผลตื้น และเป็นไวรัส ย้อม Gram ไม่เห็นเชื้อ
- LGV แผลไม่เจ็บ ไม่เห็นเชื้อจาก Gram stain (intracellular)''',
            pearl="Painful ulcer + school of fish = chancroid", topic="Chancroid diagnosis",
            ref=[f"{D} หน้า 215–216, 218–219"], nl=["2.3.1(19)", "2.1.48"]),
        mcq("ID-06-02-2",
            "A 35-year-old man with multiple sex partners has a painful 3-cm penile ulcer with a grey-whitish necrotic base and tender bilateral inguinal lymphadenopathy. He reports anaphylaxis to penicillin. What is the most appropriate antibiotic?",
            "Azithromycin",
            ["Benzathine penicillin G", "Clindamycin", "Doxycycline for 21 days", "Metronidazole"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''แผลเจ็บ พื้นสกปรกสีเทา + LN เจ็บ = **chancroid** → **azithromycin** (หรือ ceftriaxone — แต่แพ้ penicillin แบบ anaphylaxis จึงเลี่ยง cephalosporin และ azithromycin เป็นตัวเลือกที่ปลอดภัย)
- Benzathine penicillin G ใช้กับ syphilis และผู้ป่วยแพ้ penicillin
- Clindamycin ไม่ใช่ยาของ H. ducreyi
- Doxycycline 21 วัน เป็นการรักษา LGV ซึ่งแผลไม่เจ็บ
- Metronidazole ใช้กับ Trichomonas/anaerobe''',
            pearl="Chancroid → azithromycin หรือ ceftriaxone", topic="Chancroid treatment",
            ref=[f"{D} หน้า 215, 220–221"], nl=["2.3.1(19)"]),
        mcq("ID-06-02-3",
            "A 28-year-old man had a small painless penile papule that healed spontaneously 2 weeks ago. He now has fever and markedly tender, fluctuant inguinal lymph nodes both above and below the inguinal ligament, creating a groove. What is the most appropriate treatment?",
            "Doxycycline",
            ["Benzathine penicillin G", "Ceftriaxone single dose", "Acyclovir", "Incision and drainage alone"],
            explain='''แผลเล็กไม่เจ็บหายเอง → ตามด้วย **bubo เจ็บ + groove sign** = **LGV (C. trachomatis L1–L3)** → **doxycycline** (21 วัน (เสริม)) · bubo ที่ fluctuant ให้ needle aspiration ร่วมได้
- Benzathine penicillin G รักษา syphilis ซึ่ง LN ไม่เจ็บ
- Ceftriaxone single dose เป็นยาของ chancroid/gonorrhea ไม่ครอบ Chlamydia
- Acyclovir ใช้กับ HSV ซึ่งเป็นตุ่มน้ำเจ็บ
- I&D อย่างเดียวไม่รักษาเชื้อ และเสี่ยงเกิด fistula''',
            pearl="Groove sign = LGV → doxycycline", topic="LGV",
            ref=[f"{D} หน้า 217"], nl=["2.3.1(19)"]),
    ])

# ---------------------------------------------------------------- 06-03 Urethritis: GC & NGU
S3 = sec("id-06-03", "Gonorrhea & non-gonococcal urethritis",
    "GC: หนองเหลือง GN intracellular diplococci → ceftriaxone + azithro/doxy · NGU: C. trachomatis, M. genitalium, Ureaplasma, Trichomonas มูกใส → doxycycline/azithromycin",
    minutes=7, source=f"{D} หน้า 222–230", nl=["2.3.1(19)", "B10.2.2(4)", "2.1.47"],
    md='''
### Gonorrhea

- **Neisseria gonorrhoeae** · sexual transmission · ระยะฟักตัวสั้น 2–7 วัน (เสริม)
- **ชาย**: dysuria + **purulent (หนองข้นเหลือง) urethral discharge**
- **หญิง**: มักไม่มีอาการ · ตกขาว · cervicitis, cervical discharge
- **Extragenital**: conjunctivitis, pharyngitis, proctitis
- **Gram stain: Gram-negative intracellular diplococci** (ใน PMN) · culture, NAAT
- **Complication**: PID, epididymitis, orchitis, **disseminated gonococcal infection (DGI)** (tenosynovitis + pustular skin lesion + migratory arthritis (เสริม))

### Gonorrhea management (ตามสไลด์)

| สูตร | ยา |
|---|---|
| **หลัก** | **IM ceftriaxone 1 g + oral azithromycin/doxycycline** |
| ทางเลือก | Oral cefixime 800 mg + oral azithromycin 2 g |
| ทางเลือก (แพ้ cephalosporin) | IM/IV gentamicin 160–240 mg + oral azithromycin 2 g |

- **ร่วมรักษา non-GC urethritis ด้วยเสมอ** ถ้าตรวจ Chlamydia ไม่ได้ (ติดร่วมบ่อย) → นี่คือเหตุผลที่ให้ azithromycin/doxycycline คู่
- รักษาคู่นอนในช่วง **60 วัน** ก่อนผู้ป่วยมีอาการ · คัดกรอง **HIV, syphilis, HBV, HCV**
- **ไม่ใช้ ciprofloxacin/penicillin** เพราะเชื้อดื้อสูง · ไม่ต้องรอผล culture เมื่อ Gram stain ชัด

### Non-gonococcal urethritis (NGU)

- **Chlamydia trachomatis** (พบบ่อยสุด) · Ureaplasma urealyticum, **Mycoplasma genitalium** · **Trichomonas vaginalis** (protozoa)
- **ชาย**: dysuria + **cloudy/clear mucous (มูกใส) discharge** · **หญิง**: dysuria, leukorrhea, cervicitis
- Complication: PID, epididymitis · reactive arthritis (เสริม)
- Ix: Gram stain (PMN แต่ **ไม่พบ diplococci**) · **NAAT for Chlamydia, Mycoplasma, Trichomonas**
- **Tx: oral doxycycline** (100 mg bid 7 วัน (เสริม)) **หรือ azithromycin** (1 g × 1 (เสริม)) · Trichomonas → metronidazole (เสริม)
- รักษาคู่นอนในช่วง **60 วัน** · คัดกรอง HIV, syphilis, HBV, HCV

| | Gonococcal | Non-gonococcal |
|---|---|---|
| Discharge | **หนองข้น เหลือง มาก** | **มูกใส/ขุ่น น้อย** |
| ระยะฟักตัว | สั้น 2–7 วัน | นานกว่า 1–3 สัปดาห์ |
| Gram stain | **GN intracellular diplococci** | PMN ไม่มี diplococci |
| ยา | Ceftriaxone + azithro/doxy | Doxycycline หรือ azithromycin |
''',
    pearls=[
        "GC: หนองเหลืองข้น + GN intracellular diplococci",
        "GC → IM ceftriaxone 1 g + azithromycin/doxycycline (คลุม Chlamydia ร่วม)",
        "NGU: มูกใส · C. trachomatis บ่อยสุด → doxycycline หรือ azithromycin",
        "รักษาคู่นอน 60 วัน (GC, NGU) · คัดกรอง HIV, syphilis, HBV, HCV ทุกราย",
    ],
    items=[
        mcq("ID-06-03-1",
            "A 16-year-old boy has yellow urethral discharge 2 weeks after unprotected sex. Gram stain of the discharge shows numerous PMNs with intracellular Gram-negative diplococci. What is the most appropriate management?",
            "Intramuscular ceftriaxone plus oral doxycycline",
            ["Urethral swab culture and wait for the result", "Intramuscular benzathine penicillin G", "Oral metronidazole plus azithromycin", "Oral ciprofloxacin"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''หนองเหลือง + **GN intracellular diplococci** = **gonococcal urethritis** → **ceftriaxone IM + doxycycline/azithromycin** (คลุม Chlamydia ที่ติดร่วมบ่อย)
- รอผล culture ไม่จำเป็นเมื่อ Gram stain วินิจฉัยได้ชัด ควรรักษาทันทีเพื่อลดการแพร่เชื้อ
- Benzathine penicillin G รักษา syphilis — gonococcus ดื้อ penicillin
- Metronidazole ใช้กับ Trichomonas ไม่ครอบ gonococcus
- Ciprofloxacin ไม่แนะนำเพราะเชื้อดื้อ quinolone สูง''',
            pearl="GN intracellular diplococci → ceftriaxone + doxy/azithro", topic="Gonorrhea treatment",
            ref=[f"{D} หน้า 222–225"], nl=["2.3.1(19)", "B10.2.2(4)"]),
        mcq("ID-06-03-2",
            "A 26-year-old man has penile discharge and dysuria that started 3 days ago, after unprotected intercourse with a new female partner last weekend. Examination shows scant mucoid discharge at the urethral meatus. Gram stain shows PMNs without intracellular diplococci. What is the most likely diagnosis?",
            "Chlamydial urethritis",
            ["Gonococcal urethritis", "Trichomoniasis", "Bacterial cystitis", "Reactive arthritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Discharge **มูกใส (mucoid) ปริมาณน้อย** + Gram stain ไม่พบ diplococci = **non-gonococcal urethritis** ซึ่งสาเหตุที่พบบ่อยสุดคือ **C. trachomatis** (สไลด์เฉลยเป็น NGU)
- Gonococcal urethritis หนองข้นเหลืองมาก พบ GN intracellular diplococci
- Trichomoniasis เป็นสาเหตุ NGU ได้ แต่พบน้อยกว่า Chlamydia ในผู้ชาย
- Bacterial cystitis ในชายหนุ่มพบน้อย และไม่มี urethral discharge
- Reactive arthritis เป็นภาวะแทรกซ้อนภายหลัง ต้องมีข้ออักเสบ''',
            pearl="Urethritis มูกใส ไม่มี diplococci = NGU (Chlamydia)", topic="NGU diagnosis",
            ref=[f"{D} หน้า 226–230"], nl=["2.3.1(19)", "2.1.47"]),
        mcq("ID-06-03-3",
            "A 24-year-old woman is diagnosed with uncomplicated cervical chlamydial infection by NAAT. She is not pregnant and has no allergies. What is the most appropriate treatment?",
            "Oral doxycycline for 7 days",
            ["Intramuscular ceftriaxone single dose", "Oral metronidazole for 7 days", "Oral fluconazole single dose", "Benzathine penicillin G single dose"],
            explain='''Chlamydia → **doxycycline** (หรือ azithromycin) ตามสไลด์ · ปัจจุบันแนะนำ doxycycline 100 mg bid 7 วันเป็นหลัก (เสริม) และรักษาคู่นอนในช่วง 60 วัน
- Ceftriaxone รักษา gonorrhea ไม่ครอบ Chlamydia (intracellular ไม่มี cell wall แบบ peptidoglycan ที่ beta-lactam ทำงานได้ดี)
- Metronidazole รักษา Trichomonas/BV
- Fluconazole รักษา candida vaginitis
- Benzathine penicillin G รักษา syphilis''',
            pearl="Chlamydia → doxycycline หรือ azithromycin", topic="Chlamydia treatment",
            ref=[f"{D} หน้า 228"], nl=["2.3.1(19)"]),
        mcq("ID-06-03-4",
            "A 22-year-old woman has fever, migratory polyarthralgia, tenosynovitis of the right wrist and a few pustular skin lesions on the hands. She has a new sexual partner. Which complication of which organism is most likely?",
            "Disseminated gonococcal infection",
            ["Reactive arthritis from Chlamydia", "Secondary syphilis", "Acute rheumatic fever", "Chikungunya arthritis"],
            explain='''Triad **tenosynovitis + pustular skin lesion + migratory polyarthralgia** ในหญิงอายุน้อยที่มีคู่นอนใหม่ = **disseminated gonococcal infection (DGI)** (complication ของ gonorrhea ตามสไลด์) → ceftriaxone 1 g IV (เสริม)
- Reactive arthritis เป็น oligoarthritis ข้อใหญ่ขา + urethritis + conjunctivitis ไม่มี pustule
- Secondary syphilis มีผื่น MP ฝ่ามือฝ่าเท้า ไม่ใช่ pustule + tenosynovitis
- Rheumatic fever ต้องมีประวัติ strep และเกณฑ์ Jones
- Chikungunya มีไข้สูงและผื่น MP แต่ไม่มี pustule''',
            pearl="Tenosynovitis + pustule + arthralgia = DGI", topic="Gonorrhea complication",
            ref=[f"{D} หน้า 222"], nl=["2.3.1(19)"]),
    ])

LECTURE = lecture("06", "Sexually transmitted infections",
    "Syphilis · chancroid · LGV · gonorrhea · non-gonococcal urethritis",
    objectives=[
        "จำแนกระยะ syphilis และเลือกขนาด/จำนวนครั้ง benzathine penicillin ได้",
        "แปลผล treponemal กับ non-treponemal test และใช้ติดตามการรักษาได้",
        "แยก genital ulcer (syphilis, chancroid, LGV) และให้ยาที่ถูกต้องได้",
        "รักษา GC/NGU รวมถึงคู่นอนและการคัดกรอง STI อื่น",
    ],
    sections=[S1, S2, S3])
