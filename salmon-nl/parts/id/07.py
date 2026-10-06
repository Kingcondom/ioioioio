from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Infectious"

# ---------------------------------------------------------------- 07-01 HIV natural history & diagnosis
F_HIVT = fig("id-07-01-f1", "Natural history ของ HIV: viral load, CD4 และ marker ที่ตรวจได้", '''<svg viewBox="0 0 740 380">
 <defs><marker id="id-07-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="70" y="10" width="150" height="28" rx="6" class="badsoft"/>
 <text x="145" y="29" text-anchor="middle" class="tb">Acute (2–8 wk)</text>
 <rect x="224" y="10" width="330" height="28" rx="6" class="sunk"/>
 <text x="389" y="29" text-anchor="middle" class="tb">Chronic asymptomatic 7–10 ปี</text>
 <rect x="558" y="10" width="172" height="28" rx="6" class="c2soft"/>
 <text x="644" y="29" text-anchor="middle" class="tb">AIDS (CD4 &lt; 200)</text>
 <path d="M70 290H730" class="ln"/>
 <path d="M70 290V50" class="ln"/>
 <path d="M220 50V290" class="lnf"/>
 <path d="M556 50V290" class="lnf"/>
 <path d="M75 280C95 260 110 70 135 70C160 70 180 190 230 200C350 205 450 190 556 150C620 120 680 80 725 66" class="lnbad"/>
 <text x="142" y="64" class="t2">Viral load สูงสุด (ARS)</text>
 <text x="600" y="98" class="t3">VL ↑</text>
 <path d="M75 80C110 82 120 170 140 170C170 168 200 110 230 112C350 130 450 180 556 230C620 255 680 270 725 276" class="lnc1"/>
 <text x="240" y="106" class="ta">CD4</text>
 <text x="600" y="250" class="t3">CD4 &lt; 200</text>
 <path d="M150 262C180 200 200 150 225 140C350 135 600 135 725 135" class="lnok"/>
 <text x="320" y="128" class="t3">Anti-HIV antibody (บวกตลอด)</text>
 <text x="70" y="310" class="t3">สัมผัสเชื้อ</text>
 <text x="380" y="310" text-anchor="middle" class="t3">เวลา</text>
 <rect x="70" y="322" width="660" height="50" rx="8" class="c1soft"/>
 <text x="82" y="342" class="tb">ตรวจพบได้เร็วสุดหลังสัมผัส:</text>
 <text x="82" y="362" class="t2">HIV RNA/DNA PCR 10–12 วัน → p24 Ag 14–16 วัน → 4th gen (Ag/Ab) 15–18 วัน → 3rd gen (Ab) 22–24 วัน</text>
</svg>''', "ระยะ acute viral load พุ่งและ CD4 ตกชั่วคราว (อาการ ARS) ก่อน antibody ขึ้น · จากนั้น CD4 ค่อย ๆ ลดเป็นปีจนต่ำกว่า 200 = AIDS (กราฟเชิงคุณภาพ)")

S1 = sec("id-07-01", "HIV: natural history, acute retroviral syndrome & diagnosis",
    "Acute 2–8 wk (ARS mono-like) → chronic 7–10 ปี → AIDS (CD4 < 200 หรือ AIDS-defining) · window: PCR 10–12 d, p24 14–16, 4th gen 15–18, 3rd gen 22–24",
    minutes=8, source=f"{D} หน้า 231–242", nl=["2.3.1(9)", "3.3.15", "2.1.57"],
    md='''
### การติดต่อและระยะของโรค

- **Human immunodeficiency virus** · ติดทาง **sexual, parenteral (เข็ม/เลือด), vertical (แม่สู่ลูก)**

| ระยะ | ลักษณะ |
|---|---|
| **Acute HIV infection** | Incubation **2–8 สัปดาห์** · asymptomatic หรือ **acute retroviral syndrome (ARS) 2–4 สัปดาห์** |
| **Chronic HIV infection** | Asymptomatic **7–10 ปี** · CD4 ค่อย ๆ ลด |
| **AIDS** | **AIDS-defining conditions** หรือ **CD4 < 200 cells/mm3** |

[[fig:id-07-01-f1]]

### Acute retroviral syndrome

- **Mononucleosis-like / flu-like** · **MP rash** · **generalized nontender lymphadenopathy**
- Sore throat, **oral ulcer**, diarrhea · aseptic meningitis (เสริม)
- **Ix: HIV RNA, p24 antigen** — anti-HIV (antibody อย่างเดียว) อาจยังไม่ขึ้น แต่ปัจจุบัน **4th generation (HIV antigen/antibody combination assay)** ตรวจได้ทั้ง antigen และ antibody

### Investigation: window period (สไลด์หน้า 236)

| Test | ตรวจพบได้หลังสัมผัสเชื้อ |
|---|---|
| **HIV RNA/DNA (PCR)** | **10–12 วัน** (เร็วสุด) |
| p24 antigen | 14–16 วัน |
| **4th generation ELISA (IgM/IgG + p24 Ag)** | **15–18 วัน** |
| 3rd generation ELISA (IgM/IgG antibody) | 22–24 วัน |

- การวินิจฉัยในไทย: anti-HIV บวกจาก **3 วิธีที่หลักการต่างกัน** (เสริม) · ทารกใช้ PCR (เสริม)
- หลังวินิจฉัย: CD4, viral load (baseline), CBC, Cr, LFT, HBsAg, anti-HCV, VDRL, CXR, lipid/FBS (เสริม)

### AIDS-defining conditions (สไลด์หน้า 233–234 เป็นภาพ — สรุปเสริม)

- **Infection**: PCP · esophageal candidiasis · extrapulmonary cryptococcosis · **TB** (ปอด/นอกปอด) · **talaromycosis (penicilliosis)** · disseminated histoplasmosis · toxoplasmosis สมอง · CMV retinitis/disease · disseminated MAC · chronic cryptosporidiosis/cystoisosporiasis > 1 เดือน · chronic HSV ulcer > 1 เดือน · recurrent bacterial pneumonia · recurrent Salmonella septicemia · PML
- **Cancer**: Kaposi sarcoma · **non-Hodgkin lymphoma/primary CNS lymphoma** · invasive cervical cancer
- อื่น ๆ: HIV wasting syndrome · HIV encephalopathy

> สงสัย acute HIV หลังสัมผัสไม่กี่วัน–สัปดาห์ → ตรวจ **HIV RNA (PCR)** หรือ **4th gen Ag/Ab** · antibody (3rd gen) อย่างเดียวอาจลบปลอม
''',
    figs=[F_HIVT],
    pearls=[
        "ARS = mono-like + ผื่น + LN ทั่วตัวไม่เจ็บ + oral ulcer 2–4 สัปดาห์หลังสัมผัส",
        "Window: PCR 10–12 วัน < p24 14–16 < 4th gen 15–18 < 3rd gen 22–24",
        "AIDS = CD4 < 200 หรือมี AIDS-defining condition",
        "4th gen (Ag + Ab) เป็น test มาตรฐานปัจจุบัน จับได้ตั้งแต่ระยะ acute",
    ],
    items=[
        mcq("ID-07-01-1",
            "A 20-year-old man had sex with his boyfriend about 1 week ago and has just learned that his partner has AIDS. He wants to know whether he acquired HIV from this exposure. Which investigation detects infection earliest?",
            "HIV RNA PCR",
            ["Third-generation HIV antibody ELISA", "p24 antigen", "CD4 count", "Absolute lymphocyte count"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**HIV RNA/DNA PCR ตรวจพบได้เร็วที่สุด (10–12 วัน)** หลังสัมผัส (สไลด์เฉลย) — ในทางปฏิบัติถ้าสัมผัสภายใน 72 ชม.ต้องเริ่ม PEP ด้วย และตรวจซ้ำตาม window period (เสริม)
- Antibody ELISA (3rd gen) ขึ้นช้าที่สุด 22–24 วัน
- p24 antigen ขึ้นหลัง PCR (14–16 วัน)
- CD4 count และ absolute lymphocyte count ไม่ใช่ test วินิจฉัย HIV''',
            pearl="ต้องการรู้เร็วที่สุด = HIV PCR (10–12 วัน)", topic="HIV window period",
            ref=[f"{D} หน้า 236–238"], nl=["2.3.1(9)", "3.3.15"]),
        mcq("ID-07-01-2",
            "A woman has had a rash and lymphadenopathy for 2 weeks. Her husband was recently diagnosed with acute retroviral syndrome. What is the most appropriate screening investigation?",
            "Fourth-generation HIV ELISA (antibody plus p24 antigen)",
            ["HIV p24 antigen alone", "Qualitative HIV PCR", "HIV viral load", "CD4 count"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''สงสัย acute HIV หลังอาการ 2 สัปดาห์ → **4th generation ELISA** ตรวจได้ทั้ง **antibody (IgM/IgG) และ p24 antigen** จับได้ตั้งแต่ราววันที่ 15–18 จึงเป็น test มาตรฐานที่เหมาะสม (สไลด์เฉลย)
- p24 antigen อย่างเดียวขึ้นช่วงสั้น ๆ แล้วลดลง ลบปลอมได้
- Qualitative PCR ใช้ในทารกหรือกรณีพิเศษ ไม่ใช่ screening มาตรฐาน
- Viral load ใช้ติดตามการรักษา ค่าต่ำอาจเป็นผลบวกปลอม
- CD4 ไม่ใช่ test วินิจฉัย''',
            pearl="Acute HIV สงสัย → 4th gen Ag/Ab", topic="Acute HIV test",
            ref=[f"{D} หน้า 232, 239–240"], nl=["2.3.1(9)", "3.3.15"]),
        mcq("ID-07-01-3",
            "A 25-year-old man has malaise and low-grade fever for 10 days. He had unprotected sex 2 months ago. Temperature 38 °C, BP 100/60 mmHg. There is an erythematous macular rash on the trunk and generalized non-tender lymphadenopathy 1 cm in diameter. What is the most appropriate investigation?",
            "Combined HIV antigen and antibody test",
            ["HIV viral load", "HIV antibody test alone", "Qualitative HIV PCR", "HIV p24 antigen test alone"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไข้ ผื่น LN ทั่วตัวไม่เจ็บ หลังเพศสัมพันธ์เสี่ยง = **acute retroviral syndrome** → ตรวจ **combined HIV Ag/Ab (4th gen)** ซึ่งเป็น test มาตรฐานที่ไวทั้งระยะ acute และ chronic
- Viral load ไม่ใช่ test วินิจฉัยมาตรฐาน (ใช้ติดตาม)
- Antibody test อย่างเดียวอาจยังไม่ขึ้นในระยะ acute
- Qualitative PCR ใช้ในทารกหรือยืนยันในบางกรณี
- p24 antigen อย่างเดียวมีช่วงที่ตรวจได้สั้น''',
            pearl="ARS → combined Ag/Ab test", topic="ARS investigation",
            ref=[f"{D} หน้า 232, 241–242"], nl=["2.3.1(9)", "3.3.15"]),
        mcq_ordered("ID-07-01-4",
            "Which HIV test becomes positive latest after exposure?",
            ["HIV RNA PCR", "p24 antigen", "Fourth-generation antigen/antibody ELISA", "Third-generation antibody ELISA", "CD4 count below 200"], 3,
            explain='''ตามสไลด์: PCR **10–12 วัน** → p24 **14–16 วัน** → 4th gen **15–18 วัน** → **3rd gen antibody 22–24 วัน** (ช้าสุดในบรรดา test วินิจฉัย)
- CD4 < 200 ไม่ใช่ test วินิจฉัย HIV และมักเกิดหลังติดเชื้อหลายปี (ใช้บอก AIDS)''',
            pearl="Antibody อย่างเดียว (3rd gen) ขึ้นช้าสุด 22–24 วัน", topic="Window period order",
            ref=[f"{D} หน้า 236"], nl=["3.3.15"]),
    ])

# ---------------------------------------------------------------- 07-02 OI by CD4, screening, prophylaxis, ART timing
F_CD4 = fig("id-07-02-f1", "OI ตามระดับ CD4 และการป้องกัน", '''<svg viewBox="0 0 740 420">
 <rect x="10" y="10" width="110" height="400" rx="10" class="sunk"/>
 <text x="65" y="34" text-anchor="middle" class="tb">CD4</text>
 <rect x="20" y="46" width="90" height="76" rx="8" class="oksoft"/>
 <text x="65" y="90" text-anchor="middle" class="tb">&lt; 500</text>
 <rect x="20" y="130" width="90" height="86" rx="8" class="misssoft"/>
 <text x="65" y="178" text-anchor="middle" class="tb">&lt; 200</text>
 <rect x="20" y="224" width="90" height="96" rx="8" class="badsoft"/>
 <text x="65" y="276" text-anchor="middle" class="tb">&lt; 100</text>
 <rect x="20" y="328" width="90" height="74" rx="8" class="bad"/>
 <text x="65" y="370" text-anchor="middle" class="tw">&lt; 50</text>
 <rect x="130" y="46" width="300" height="76" rx="8" class="box"/>
 <text x="142" y="70" class="tb">โรคที่พบ</text>
 <text x="142" y="92" class="t2">Pneumococcal pneumonia</text>
 <text x="142" y="112" class="t2">Pulmonary TB</text>
 <rect x="130" y="130" width="300" height="86" rx="8" class="box"/>
 <text x="142" y="154" class="t2">Oropharyngeal/esophageal candida</text>
 <text x="142" y="176" class="t2">PCP</text>
 <text x="142" y="198" class="t2">Miliary / extrapulmonary TB</text>
 <rect x="130" y="224" width="300" height="96" rx="8" class="box"/>
 <text x="142" y="246" class="t2">Cryptococcosis · Talaromycosis</text>
 <text x="142" y="268" class="t2">Histoplasmosis</text>
 <text x="142" y="290" class="t2">Toxoplasmosis (สมอง)</text>
 <text x="142" y="312" class="t2">Cryptosporidiosis</text>
 <rect x="130" y="328" width="300" height="74" rx="8" class="box"/>
 <text x="142" y="356" class="t2">Disseminated CMV (retinitis)</text>
 <text x="142" y="380" class="t2">Disseminated MAC</text>
 <rect x="440" y="46" width="290" height="76" rx="8" class="oksoft"/>
 <text x="452" y="70" class="tb">คัดกรองทุกราย</text>
 <text x="452" y="92" class="t2">CXR / อาการ TB</text>
 <text x="452" y="112" class="t3">ไม่มี active TB → TPT (INH) (เสริม)</text>
 <rect x="440" y="130" width="290" height="86" rx="8" class="misssoft"/>
 <text x="452" y="154" class="tb">TMP/SMX 1 DS วันละครั้ง</text>
 <text x="452" y="176" class="t3">CD4 &lt; 200 หรือ thrush</text>
 <text x="452" y="196" class="t3">หรือ AIDS-defining illness</text>
 <rect x="440" y="224" width="290" height="96" rx="8" class="badsoft"/>
 <text x="452" y="246" class="tb">Serum cryptococcal Ag</text>
 <text x="452" y="266" class="tb">ตรวจตา (indirect ophthalmoscope)</text>
 <text x="452" y="288" class="t3">CrAg + → LP · ไม่มี meningitis →</text>
 <text x="452" y="308" class="t3">fluconazole pre-emptive (เสริม)</text>
 <rect x="440" y="328" width="290" height="74" rx="8" class="c2soft"/>
 <text x="452" y="352" class="t2">ตรวจตาหา CMV retinitis</text>
 <text x="452" y="374" class="t3">MAC: azithromycin 1,200 mg/wk</text>
 <text x="452" y="392" class="t3">ถ้ายังเริ่ม ART ไม่ได้ (เสริม)</text>
</svg>''', "ไล่ลงตาม CD4: ยิ่งต่ำยิ่งเจอเชื้อฉวยโอกาสชนิดรุนแรง · คอลัมน์ขวาคือสิ่งที่ต้องคัดกรอง/ป้องกันที่ระดับนั้น (ตารางป้องกันในสไลด์หน้า 247–252 เป็นภาพ สรุปตามแนวทางไทย)")

S2 = sec("id-07-02", "HIV: opportunistic infections by CD4, screening, prophylaxis & ART timing",
    "<500 pneumococcus/PTB · <200 candida, PCP, EPTB · <100 crypto, talaromyces, histo, toxo · <50 CMV, MAC · TMP/SMX เมื่อ CD4 < 200 · no OI → same-day ART · OI → รักษา OI ก่อน (IRIS)",
    minutes=10, source=f"{D} หน้า 243–252, 258–259", nl=["2.3.1(9)", "2.3.1(18)", "2.3.1-3(6)"],
    md='''
### Opportunistic infection ตาม CD4 (สไลด์หน้า 243)

| CD4 (cells/mm3) | Common OI |
|---|---|
| **< 500** | Pneumococcal pneumonia · pulmonary TB |
| **< 200** | Oropharyngeal candidiasis/esophagitis · **PCP** · miliary TB/extrapulmonary TB |
| **< 100** | **Cryptococcosis** · **talaromycosis** · histoplasmosis · **toxoplasmosis** · cryptosporidiosis |
| **< 50** | **Disseminated CMV** · **disseminated MAC** |

[[fig:id-07-02-f1]]

### OI screening (สไลด์หน้า 244)

- **Pulmonary TB ทุกราย** → CXR (+ ซักอาการ)
- **Cryptococcosis** กรณี **CD4 < 100** → **serum cryptococcal antigen (CrAg)**
- **CMV retinitis** กรณี **CD4 < 100** → **indirect ophthalmoscope**

### เริ่ม ART เมื่อไร

- **ไม่มี OI → same-day ART** (เริ่มเร็วที่สุด ไม่ว่า CD4 เท่าไร)
- **มี OI → รักษา OI ก่อน แล้วค่อยเริ่ม ART (delayed ART)** เพื่อลด **IRIS**
  - ส่วนใหญ่เริ่ม ART ภายใน **2 สัปดาห์** หลังรักษา OI (PCP, talaromycosis, toxoplasmosis) (เสริม)
  - TB: เริ่ม ART ภายใน 2 สัปดาห์ (โดยเฉพาะ CD4 < 50) · **TB meningitis และ cryptococcal meningitis รอ 4–6 สัปดาห์** (เสริม)

### IRIS (immune reconstitution inflammatory syndrome)

- หลังเริ่ม ART ภูมิคุ้มกันฟื้นตัว ตอบสนองต่อเชื้อ OI ที่มีอยู่ → **อาการของ OI แย่ลง (paradoxical) หรือ OI ที่ซ่อนอยู่แสดงออกมาใหม่ (unmasking)**
- มักเกิดใน 2–12 สัปดาห์แรก CD4 เพิ่ม VL ลด · ส่วนใหญ่ **ไม่หยุด ART** ให้ NSAID/steroid ตามความรุนแรง (เสริม)

### Prophylaxis for OI (สไลด์หน้า 247: เริ่มเมื่อ CD4 < 200 หรือ oropharyngeal candidiasis หรือ AIDS-defining illness — ตารางหน้า 248–252 เป็นภาพ สรุปตามแนวทางไทย (เสริม))

| OI | เริ่มเมื่อ | ยา | หยุดเมื่อ |
|---|---|---|---|
| **PCP** | **CD4 < 200** หรือ < 14% หรือ **thrush** หรือ AIDS-defining | **TMP/SMX 1 DS (800/160) วันละครั้ง** (แพ้ → dapsone) | CD4 > 200 นาน ≥ 3–6 เดือนหลัง ART |
| Toxoplasmosis | CD4 < 100 + toxo IgG + | TMP/SMX 1 DS วันละครั้ง (ตัวเดียวกับ PCP) | CD4 > 200 ≥ 3 เดือน |
| Cryptococcosis | CD4 < 100 | ตรวจ **serum CrAg** → บวก: LP · ไม่มี meningitis → **fluconazole pre-emptive** | ตามแนวทาง |
| Talaromycosis | CD4 < 100 (ภาคเหนือ) | Itraconazole 200 mg/d | CD4 > 100 ≥ 6 เดือน |
| MAC | CD4 < 50 และยังเริ่ม ART ไม่ได้ | Azithromycin 1,200 mg/wk | เริ่ม ART แล้ว |
| TB (latent) | ทุกรายที่ไม่มี active TB | INH 9 เดือน หรือ 3HP | — |

> กับดัก: CD4 250 ไม่มี OI → **ไม่ต้องให้ TMP/SMX** แต่ต้องเริ่ม ART · **มี thrush แม้ CD4 > 200 ก็ให้ TMP/SMX**
''',
    figs=[F_CD4],
    pearls=[
        "CD4 < 200: PCP, candida, EPTB · < 100: crypto, talaromyces, toxo · < 50: CMV, MAC",
        "คัดกรอง TB ทุกราย · CD4 < 100 → serum CrAg + ตรวจตา",
        "ไม่มี OI → same-day ART · มี OI → รักษา OI ก่อน (crypto/TB meningitis รอ 4–6 สัปดาห์)",
        "TMP/SMX prophylaxis: CD4 < 200 หรือ thrush หรือ AIDS-defining",
        "IRIS = อาการ OI แย่ลง/โผล่ใหม่หลังเริ่ม ART — ไม่หยุด ART",
    ],
    items=[
        mcq("ID-07-02-1",
            "A 30-year-old man is newly diagnosed with HIV. He is asymptomatic, with small rubbery mobile lymph nodes in the neck and axillae, no fever or weight loss, normal chest radiograph and CD4 count 250 cells/mm3. What is the most appropriate management?",
            "Tenofovir / lamivudine / dolutegravir",
            ["Reassurance and repeat CD4 in 6 months", "Isoniazid preventive therapy alone", "Isoniazid / rifampicin / ethambutol / pyrazinamide", "Trimethoprim-sulfamethoxazole prophylaxis alone"],
            kind="old", src="ดัดแปลงจากตัวอย่างข้อสอบในสไลด์หน้า 258–259 (โจทย์เดิมมีไข้และน้ำหนักลด ทำให้ต้องคิดถึง TB/lymphoma ก่อน จึงปรับเป็นผู้ป่วยไม่มี OI)",
            explain='''HIV รายใหม่ **ไม่มี OI** (ไม่มีไข้/น้ำหนักลด CXR ปกติ LN เล็กนุ่มแบบ persistent generalized lymphadenopathy) → **same-day ART: TDF/3TC/DTG** ไม่ขึ้นกับ CD4
- Reassurance แล้วรอ ไม่ถูก — ทุกรายต้องเริ่ม ART
- INH preventive therapy ให้ได้หลังตัด active TB (เสริม) แต่ไม่ใช่การรักษาหลักแทน ART
- ยารักษา TB 4 ตัวใช้เมื่อพบ active TB ซึ่งรายนี้ไม่มีหลักฐาน (ในโจทย์เดิมของสไลด์ที่มีไข้น้ำหนักลด ต้องหา TB/lymphoma ก่อน)
- TMP/SMX prophylaxis ให้เมื่อ CD4 < 200 หรือมี thrush/AIDS-defining — CD4 250 ไม่ต้องให้''',
            pearl="HIV ไม่มี OI → same-day ART (TDF/3TC/DTG)", topic="When to start ART",
            ref=[f"{D} หน้า 245–247, 258–259"], nl=["2.3.1(9)"]),
        mcq("ID-07-02-2",
            "A 32-year-old woman with newly diagnosed HIV has a CD4 count of 60 cells/mm3. She has no fever, headache or visual symptoms. Chest radiograph is normal. Which screening test is most important before starting antiretroviral therapy?",
            "Serum cryptococcal antigen",
            ["Serum galactomannan", "Toxoplasma IgM", "Stool modified acid-fast stain", "Brain MRI"],
            explain='''CD4 **< 100** → ตามสไลด์ต้องคัดกรอง **cryptococcosis ด้วย serum cryptococcal antigen** (และตรวจตาหา CMV retinitis) ก่อนเริ่ม ART เพื่อลด IRIS/cryptococcal meningitis
- Galactomannan ใช้กับ aspergillosis ในผู้ป่วย neutropenia ไม่ใช่การคัดกรองใน HIV
- Toxoplasma ใช้ IgG (ไม่ใช่ IgM) เพื่อพิจารณา prophylaxis
- Stool modified AFB ทำเมื่อมีท้องเสียเรื้อรัง
- MRI สมองไม่ใช่ screening ในผู้ไม่มีอาการ''',
            pearl="CD4 < 100 → serum CrAg + ตรวจตา", topic="OI screening",
            ref=[f"{D} หน้า 244"], nl=["2.3.1(9)", "2.3.1-3(7)"]),
        mcq("ID-07-02-3",
            "A 35-year-old man with HIV has oral thrush. His CD4 count is 240 cells/mm3 and he has just started antiretroviral therapy. Which additional medication is indicated?",
            "Trimethoprim-sulfamethoxazole one double-strength tablet daily",
            ["Azithromycin 1,200 mg weekly", "Isoniazid for 9 months without TB screening", "Valganciclovir daily", "No prophylaxis because CD4 is above 200"],
            explain='''ข้อบ่งชี้ PCP prophylaxis คือ **CD4 < 200 หรือ oropharyngeal candidiasis หรือ AIDS-defining illness** → มี thrush จึงต้องให้ **TMP/SMX 1 DS วันละครั้ง** แม้ CD4 > 200
- Azithromycin ป้องกัน MAC เมื่อ CD4 < 50
- INH ต้องตัด active TB ก่อนเสมอ
- Valganciclovir ไม่ใช้เป็น primary prophylaxis ของ CMV
- การยึด CD4 อย่างเดียวพลาดข้อบ่งชี้เรื่อง thrush''',
            pearl="Thrush = ข้อบ่งชี้ TMP/SMX prophylaxis แม้ CD4 > 200", topic="PCP prophylaxis",
            ref=[f"{D} หน้า 247"], nl=["2.3.1(9)", "2.3.1(18)"]),
        mcq("ID-07-02-4",
            "A 28-year-old man with HIV (CD4 45 cells/mm3) is being treated for cryptococcal meningitis with amphotericin B and flucytosine. When should antiretroviral therapy be started?",
            "After 4–6 weeks of antifungal therapy",
            ["On the same day as the diagnosis", "Within 48 hours of starting antifungal therapy", "Only after CSF culture becomes sterile for 1 year", "Never, until CD4 rises above 200 spontaneously"],
            explain='''มี OI → **รักษา OI ก่อนแล้วค่อยเริ่ม ART** เพื่อลด IRIS (ตามสไลด์) · cryptococcal meningitis เป็นข้อยกเว้นที่ต้องรอนานกว่า OI อื่น คือ **4–6 สัปดาห์** เพราะ IRIS ในสมองอันตรายถึงชีวิต (เสริม)
- Same-day ART ใช้เมื่อไม่มี OI
- เริ่มภายใน 48 ชม. เพิ่มการตายจาก IRIS ใน cryptococcal meningitis
- รอ 1 ปีนานเกินไป เสี่ยง OI อื่น
- CD4 จะไม่ขึ้นเองถ้าไม่ได้ ART''',
            pearl="Crypto/TB meningitis → รอ ART 4–6 สัปดาห์ · OI อื่นส่วนใหญ่ ≤ 2 สัปดาห์", topic="ART timing & IRIS",
            ref=[f"{D} หน้า 244–245"], nl=["2.3.1(9)", "2.3.1-3(7)"]),
        mcq("ID-07-02-5",
            "A 34-year-old woman with HIV and pulmonary TB started antituberculous therapy 4 weeks ago and ART 2 weeks ago. She had improved, but now has new fever and enlarging cervical lymph nodes. Her CD4 has risen from 40 to 160 cells/mm3 and viral load has fallen markedly. Sputum smear is now negative. What is the most likely diagnosis?",
            "Immune reconstitution inflammatory syndrome",
            ["Multidrug-resistant TB", "Antiretroviral treatment failure", "Drug fever from rifampicin", "New Talaromyces infection"],
            explain='''อาการดีขึ้นแล้วแย่ลงใหม่ **หลังเริ่ม ART** + **CD4 เพิ่ม VL ลด** = **IRIS (paradoxical TB-IRIS)** — ภูมิคุ้มกันที่ฟื้นตัวตอบสนองต่อเชื้อเดิม · ไม่หยุด ART/ยา TB, ให้ NSAID หรือ prednisolone ตามความรุนแรง (เสริม)
- MDR-TB มักไม่ดีขึ้นเลยตั้งแต่ต้นและ sputum ยังบวก
- ART failure จะมี VL สูง CD4 ไม่เพิ่ม
- Drug fever ไม่ทำให้ LN โตขึ้น
- Talaromycosis มักมีผื่น papule ตรงกลางบุ๋ม/เนื้อตาย และไม่ได้อธิบายช่วงเวลาที่สัมพันธ์กับ ART''',
            pearl="หลังเริ่ม ART อาการ OI แย่ลง + CD4 ↑ VL ↓ = IRIS", topic="IRIS",
            ref=[f"{D} หน้า 244"], nl=["2.3.1(9)"]),
    ])

# ---------------------------------------------------------------- 07-03 ART & side effects
F_ART = fig("id-07-03-f1", "ผลข้างเคียงของยาต้านไวรัสที่ออกสอบ", '''<svg viewBox="0 0 740 360">
 <rect x="10" y="10" width="230" height="104" rx="10" class="c1soft"/>
 <text x="22" y="34" class="tb">Tenofovir (TDF)</text>
 <text x="22" y="56" class="t2">ไตเสื่อม proteinuria</text>
 <text x="22" y="76" class="t2">Fanconi (glucosuria</text>
 <text x="22" y="96" class="t2">phosphaturia) · osteoporosis</text>
 <rect x="255" y="10" width="230" height="104" rx="10" class="badsoft"/>
 <text x="267" y="34" class="tb">Zidovudine (AZT)</text>
 <text x="267" y="56" class="t2">BM suppression</text>
 <text x="267" y="76" class="t2">macrocytic anemia</text>
 <text x="267" y="96" class="t2">GI · insulin resistance · lipoatrophy</text>
 <rect x="500" y="10" width="230" height="104" rx="10" class="misssoft"/>
 <text x="512" y="34" class="tb">Nevirapine (NVP)</text>
 <text x="512" y="56" class="t2">Hypersensitivity: ผื่น</text>
 <text x="512" y="76" class="t2">(SJS) + hepatitis</text>
 <text x="512" y="96" class="t3">หญิง CD4 &gt; 250 เสี่ยงตับ (เสริม)</text>
 <rect x="10" y="124" width="230" height="104" rx="10" class="c2soft"/>
 <text x="22" y="148" class="tb">Efavirenz (EFV)</text>
 <text x="22" y="170" class="t2">CNS: ฝันร้าย มึน นอนไม่หลับ</text>
 <text x="22" y="190" class="t2">DLP · lipohypertrophy</text>
 <text x="22" y="210" class="t3">gynecomastia (เสริม)</text>
 <rect x="255" y="124" width="230" height="104" rx="10" class="box"/>
 <text x="267" y="148" class="tb">Abacavir (ABC)</text>
 <text x="267" y="170" class="t2">Hypersensitivity</text>
 <text x="267" y="190" class="t2">ตรวจ HLA-B5701 ก่อนให้</text>
 <rect x="500" y="124" width="230" height="104" rx="10" class="box"/>
 <text x="512" y="148" class="tb">Protease inhibitors (LPV/r)</text>
 <text x="512" y="170" class="t2">GI · insulin resistance</text>
 <text x="512" y="190" class="t2">DLP · lipohypertrophy</text>
 <text x="512" y="210" class="t3">drug interaction (ritonavir)</text>
 <rect x="10" y="238" width="475" height="110" rx="10" class="sunk"/>
 <text x="22" y="262" class="tb">Stavudine (d4T) / didanosine (ddI) — ยาเก่า เลิกใช้</text>
 <text x="22" y="284" class="t2">Insulin resistance · DLP (d4T) · lipoatrophy (d4T)</text>
 <text x="22" y="306" class="t2">Peripheral neuropathy · pancreatitis · lactic acidosis (เสริม)</text>
 <rect x="500" y="238" width="230" height="110" rx="10" class="oksoft"/>
 <text x="512" y="262" class="tb">Dolutegravir (DTG)</text>
 <text x="512" y="284" class="t2">ทนได้ดี · น้ำหนักเพิ่ม</text>
 <text x="512" y="304" class="t2">นอนไม่หลับ · Cr ขึ้นเล็กน้อย</text>
 <text x="512" y="324" class="t3">(ยับยั้ง OCT2 ไม่ใช่ไตเสื่อม) (เสริม)</text>
</svg>''', "จับคู่ยากับผลข้างเคียงเด่น: TDF ไต/กระดูก · AZT ไขกระดูก · NVP ตับ+ผื่น · EFV สมอง+ไขมัน · ABC แพ้ (HLA-B5701) · PIs เมตาบอลิก")

S3 = sec("id-07-03", "Antiretroviral therapy & adverse effects",
    "First line TDF + 3TC (หรือ FTC) + DTG · TDF ไต/Fanconi/กระดูก · AZT ซีด macrocytic · NVP ผื่น+ตับ · EFV CNS · ABC HLA-B5701 · PIs/d4T metabolic",
    minutes=8, source=f"{D} หน้า 246, 256–257, 260–267", nl=["2.3.1(9)", "B1.7.2"],
    md='''
### First-line ART (ตามสไลด์)

- **Tenofovir (TDF) + lamivudine (3TC) + dolutegravir (DTG)** (TLD)
- หรือ **tenofovir + emtricitabine (FTC) + dolutegravir**
- โครงสร้าง: **2 NRTIs (backbone) + 1 INSTI** · สูตรเก่าใช้ NNRTI (EFV/NVP) หรือ PI/r เป็นตัวที่สาม (เสริม)
- ไตเสื่อม (CrCl < 50) → เปลี่ยน TDF เป็น AZT หรือ ABC หรือใช้ TAF (เสริม)

### Common ART side effects (สไลด์หน้า 256–257)

| ผลข้างเคียง | ยา |
|---|---|
| **Nephrotoxicity** (proteinuria, **Fanconi syndrome**: glucosuria ทั้งที่น้ำตาลปกติ, phosphaturia) | **Tenofovir (TDF)** |
| **Osteoporosis** | Tenofovir |
| **BM suppression** (macrocytic anemia, neutropenia) | **Zidovudine (AZT)** |
| **Hypersensitivity reaction** | **Abacavir (HLA-B5701)** · **nevirapine** |
| **Hepatitis** | **NNRTI (nevirapine)** |
| GI symptom | AZT, PIs |
| **CNS** (ฝันร้าย มึนงง ซึมเศร้า) | **Efavirenz** |
| Insulin resistance | Stavudine (d4T), didanosine (ddI), AZT, PIs (lopinavir/ritonavir) |
| Dyslipidemia | d4T, EFV (และ PIs (เสริม)) |
| **Lipoatrophy** (ไขมันใต้ผิวหน้า/แขนขาลีบ) | d4T, AZT |
| **Lipohypertrophy** (ไขมันพุง/หลังคอ) | EFV, PIs |

[[fig:id-07-03-f1]]

### เลือกสูตรในผู้ป่วยมีโรคร่วม (ข้อสอบชอบถาม)

- **DM, HT, DLP** → เลี่ยง AZT, d4T, PIs (insulin resistance/DLP) → ในตัวเลือกเก่าเลือก **TDF + 3TC + EFV** · ปัจจุบันเลือก **TDF + 3TC + DTG**
- **ซีด** → เลี่ยง AZT · **ไตเสื่อม** → เลี่ยง TDF · **โรคตับ/HBV co-infection** → ต้องมี TDF (+3TC/FTC) เพราะรักษา HBV ด้วย (เสริม) และเลี่ยง NVP
- **โรคจิต/ซึมเศร้า** → เลี่ยง EFV
- **Ritonavir ไม่ใช้เป็นตัวที่สามเดี่ยว ๆ** ใช้เป็น booster ของ PI
''',
    figs=[F_ART],
    pearls=[
        "First line: TDF + 3TC/FTC + DTG",
        "TDF → Cr ขึ้น proteinuria glucosuria (Fanconi) + กระดูกพรุน",
        "AZT → ซีด macrocytic (BM suppression) หลังเริ่มยาไม่กี่เดือน",
        "NVP → ผื่นคัน + ตับอักเสบ · ABC → HLA-B5701 hypersensitivity · EFV → CNS",
        "DM/DLP → เลี่ยง AZT, d4T, PIs",
    ],
    items=[
        mcq("ID-07-03-1",
            "A 30-year-old woman with HIV has been on antiretroviral therapy for 1 year. She has no comorbidities or other medications and a normal examination. FBS 88 mg/dL, creatinine 2.1 mg/dL (0.8 mg/dL last year). Urinalysis shows protein 2+ and glucose 3+. Which antiretroviral drug most likely caused these findings?",
            "Tenofovir",
            ["Zidovudine", "Efavirenz", "Lamivudine", "Nevirapine"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Cr เพิ่ม + proteinuria + **glucosuria ทั้งที่ FBS ปกติ** = **proximal tubulopathy (Fanconi syndrome)** จาก **tenofovir (TDF)**
- Zidovudine ทำให้ BM suppression/ซีด ไม่ทำให้ไตเสื่อม
- Efavirenz ทำให้อาการ CNS และ DLP
- Lamivudine ปลอดภัยมาก (ปรับขนาดตามไต แต่ไม่ทำให้ไตเสื่อม)
- Nevirapine ทำให้ผื่นแพ้และตับอักเสบ''',
            pearl="Glucosuria + FBS ปกติ + Cr ขึ้นใน HIV = TDF Fanconi", topic="TDF nephrotoxicity",
            ref=[f"{D} หน้า 256, 262–263"], nl=["2.3.1(9)", "B1.7.2"]),
        mcq("ID-07-03-2",
            "A 30-year-old woman with HIV has been on ART for 6 months and has had fatigue and dyspnea on exertion for 2 months. Examination is normal. CD4 has risen from 45 to 203 cells/mm3. Hct 26%, MCV 112 fL, WBC 4,000/mm3, platelets 200,000/mm3. What is the most likely cause?",
            "Antiretroviral therapy (zidovudine)",
            ["HIV infection itself", "Immune reconstitution inflammatory syndrome", "Opportunistic infection", "Nutritional deficiency"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ซีด **macrocytic (MCV 112)** หลังเริ่ม ART ไม่กี่เดือน + CD4 ดีขึ้น = **zidovudine (AZT) BM suppression** (สไลด์เฉลย = ART)
- HIV เองทำให้ซีดได้แต่มักเป็น normocytic และควรดีขึ้นเมื่อคุมไวรัสได้
- IRIS เป็นการอักเสบของ OI ไม่ได้ทำให้ซีด macrocytic เด่น
- OI (เช่น MAC, parvovirus) ทำให้ซีดได้ แต่รายนี้ไม่มีอาการอื่นและ CD4 สูงขึ้น
- ขาด B12/folate ทำให้ macrocytic ได้ แต่ไม่มีประวัติชี้นำ และ AZT เป็นคำตอบคลาสสิก''',
            pearl="ซีด macrocytic หลังเริ่ม ART = AZT", topic="AZT toxicity",
            ref=[f"{D} หน้า 256, 264–265"], nl=["2.3.1(9)", "B1.7.2"]),
        mcq("ID-07-03-3",
            "A patient with HIV recently started antiretroviral therapy and develops a pruritic maculopapular rash with elevated liver enzymes. Which drug is the most likely cause?",
            "Nevirapine",
            ["Efavirenz", "Abacavir", "Tenofovir", "Lamivudine"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**ผื่น + ตับอักเสบ** ช่วงแรกหลังเริ่มยา = **nevirapine** hypersensitivity/hepatitis (NNRTI)
- Efavirenz มีผื่นได้แต่เด่นที่อาการ CNS
- Abacavir hypersensitivity มีไข้ ผื่น GI อาการหายใจ (สัมพันธ์ HLA-B5701) ไม่เด่นตับ
- Tenofovir เป็นพิษต่อไตและกระดูก
- Lamivudine แทบไม่มีผลข้างเคียง''',
            pearl="ผื่น + ตับอักเสบหลังเริ่ม ART = nevirapine", topic="NVP toxicity",
            ref=[f"{D} หน้า 256, 266–267"], nl=["2.3.1(9)", "B1.7.2"]),
        mcq("ID-07-03-4",
            "A 60-year-old man with diabetes, hypertension and dyslipidemia is newly diagnosed with HIV. Among the following regimens, which is the most appropriate?",
            "Lamivudine / tenofovir / efavirenz",
            ["Lamivudine / zidovudine / nevirapine", "Lamivudine / stavudine / efavirenz", "Lamivudine / tenofovir / ritonavir", "Lamivudine / zidovudine / ritonavir"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''มี DM/DLP → เลี่ยงยาที่ทำให้ insulin resistance/DLP (**AZT, d4T, PIs**) → ในตัวเลือกนี้เหมาะสุดคือ **3TC/TDF/EFV** (ปัจจุบันแนวทางไทยใช้ TDF/3TC/DTG)
- AZT/NVP: AZT ทำ insulin resistance และ NVP เสี่ยงตับ
- d4T เป็นยาเก่าที่เลิกใช้ ทำทั้ง insulin resistance, DLP, lipoatrophy
- Ritonavir ไม่ใช้เป็นตัวที่สามเดี่ยว ๆ (ใช้เป็น booster) และทำ metabolic ผิดปกติ
- AZT/ritonavir ไม่เหมาะทั้งสองตัว''',
            pearl="HIV + DM/DLP → เลี่ยง AZT, d4T, PIs", topic="ART selection",
            ref=[f"{D} หน้า 256–257, 260–261"], nl=["2.3.1(9)"]),
        mcq("ID-07-03-5",
            "A 27-year-old man with HIV is to start abacavir because of chronic kidney disease. Which test should be done before starting this drug?",
            "HLA-B5701",
            ["HLA-B1502", "HLA-B5801", "G6PD level", "Serum lipase"],
            explain='''**Abacavir hypersensitivity** สัมพันธ์กับ **HLA-B5701** → ต้องตรวจก่อนให้ (บวกห้ามใช้)
- HLA-B1502 สัมพันธ์กับ SJS/TEN จาก carbamazepine
- HLA-B5801 สัมพันธ์กับ SCAR จาก allopurinol
- G6PD ตรวจก่อนยา oxidant เช่น primaquine, dapsone
- Lipase ไม่เกี่ยวกับ abacavir (ddI/d4T ทำ pancreatitis)''',
            pearl="Abacavir → ตรวจ HLA-B5701 ก่อน", topic="Abacavir HLA",
            ref=[f"{D} หน้า 256"], nl=["2.3.1(9)", "B1.7.2"]),
    ])

# ---------------------------------------------------------------- 07-04 HIV prevention
S4 = sec("id-07-04", "HIV prevention: PrEP & PEP",
    "Condom + ไม่ใช้เข็มร่วม · PrEP = TDF/FTC · PEP = TDF/FTC (หรือ 3TC) + DTG ภายใน 72 ชม. นาน 28 วัน",
    minutes=4, source=f"{D} หน้า 253–255", nl=["2.3.1(9)"],
    md='''
### การป้องกัน

- **Condom** · **ไม่ใช้เข็มฉีดยาร่วมกับผู้อื่น**
- **PrEP (pre-exposure prophylaxis)** ในคนเสี่ยงสูง
- **PEP (post-exposure prophylaxis)** หลังสัมผัส
- U = U: ผู้ติดเชื้อที่กินยาจน viral load undetectable ไม่แพร่เชื้อทางเพศสัมพันธ์ (เสริม) · PMTCT ในหญิงตั้งครรภ์ (เสริม)

### PrEP

- **Tenofovir (TDF) + emtricitabine (FTC)** กินทุกวัน
- กลุ่มเป้าหมาย: คู่ผลเลือดต่าง (คู่ที่ยังไม่ได้ ART/VL ยังไม่กดลง), MSM, sex worker, ใช้สารเสพติดชนิดฉีด (เสริม)
- ก่อนเริ่ม: ตรวจ anti-HIV ลบ, Cr, HBsAg · ติดตาม anti-HIV ทุก 3 เดือน (เสริม)
- MSM ใช้แบบ event-driven 2-1-1 ได้ (เสริม)

### PEP

- **TDF + FTC + DTG** หรือ **TDF + 3TC + DTG**
- เริ่ม **เร็วที่สุด ภายใน 72 ชั่วโมง** หลังสัมผัส กิน **28 วัน** (เสริม)
- ใช้ทั้ง occupational (เข็มตำ) และ non-occupational (เพศสัมพันธ์ ถูกข่มขืน) (เสริม)
- ตรวจ anti-HIV baseline และติดตามที่ 1 และ 3 เดือน · ตรวจ HBV/HCV/syphilis ร่วม (เสริม)

| | PrEP | PEP |
|---|---|---|
| เมื่อไร | ก่อนเสี่ยง ต่อเนื่อง | หลังสัมผัส ≤ 72 ชม. |
| ยา | **TDF/FTC (2 ตัว)** | **TDF/FTC (หรือ 3TC) + DTG (3 ตัว)** |
| ระยะเวลา | ตลอดช่วงที่ยังเสี่ยง | 28 วัน |
''',
    pearls=[
        "PrEP = TDF/FTC สองตัว กินทุกวัน",
        "PEP = TDF/FTC (หรือ 3TC) + DTG สามตัว",
        "PEP เริ่มภายใน 72 ชม. กิน 28 วัน (เสริม)",
        "ก่อน PrEP ต้องแน่ใจว่า anti-HIV ลบ (กันการใช้ 2 ตัวรักษา HIV ที่ติดแล้ว)",
    ],
    items=[
        mcq("ID-07-04-1",
            "A 24-year-old nurse sustains a deep needlestick injury from a patient with HIV whose viral load is unknown. The injury occurred 2 hours ago. Her baseline anti-HIV is negative. What is the most appropriate prophylaxis?",
            "Tenofovir/emtricitabine plus dolutegravir for 28 days",
            ["Tenofovir/emtricitabine for 28 days", "Zidovudine alone for 28 days", "Wait for the source patient's viral load before deciding", "No prophylaxis; repeat anti-HIV in 3 months"],
            explain='''สัมผัสเลือดผู้ติดเชื้อ HIV ภายใน 72 ชม. → **PEP 3 ตัว: TDF/FTC (หรือ 3TC) + DTG** นาน 28 วัน (ระยะเวลาเสริม) เริ่มให้เร็วที่สุด
- TDF/FTC 2 ตัวเป็นสูตร **PrEP** ไม่พอสำหรับ PEP
- AZT เดี่ยวเป็นสูตรเก่ามาก ไม่แนะนำแล้ว
- การรอผล VL ของ source ทำให้เริ่มช้า — เริ่มก่อนแล้วปรับภายหลังได้
- ไม่ให้ยาเลยเสียโอกาสป้องกัน''',
            pearl="PEP = 3 ตัว (TDF/FTC + DTG) ภายใน 72 ชม.", topic="HIV PEP",
            ref=[f"{D} หน้า 255"], nl=["2.3.1(9)"]),
        mcq("ID-07-04-2",
            "A 29-year-old HIV-negative man has an HIV-positive partner who has just started ART and is not yet virally suppressed. He wants ongoing protection. His creatinine and HBsAg are normal. What is the most appropriate regimen?",
            "Daily tenofovir disoproxil fumarate/emtricitabine",
            ["Daily tenofovir/lamivudine/dolutegravir", "Daily dolutegravir alone", "Zidovudine/lamivudine after each exposure", "Monthly benzathine penicillin"],
            explain='''ป้องกันก่อนสัมผัสต่อเนื่อง = **PrEP: TDF + FTC** (ตามสไลด์) ร่วมกับ condom
- TDF/3TC/DTG เป็นสูตร PEP/การรักษา ไม่ใช่ PrEP ระยะยาว
- DTG เดี่ยวไม่ใช่ PrEP และเสี่ยงดื้อยา
- AZT/3TC หลังสัมผัสไม่ใช่สูตรมาตรฐาน
- Penicillin ไม่เกี่ยวกับ HIV''',
            pearl="PrEP = TDF/FTC", topic="HIV PrEP",
            ref=[f"{D} หน้า 253–254"], nl=["2.3.1(9)"]),
    ])

LECTURE = lecture("07", "HIV/AIDS",
    "Natural history · diagnosis · OI by CD4 · prophylaxis · ART & side effects · PrEP/PEP",
    objectives=[
        "เลือก test วินิจฉัย HIV ตาม window period และระยะ acute",
        "บอก OI ตามระดับ CD4 คัดกรองและให้ prophylaxis ได้",
        "กำหนดเวลาเริ่ม ART และรู้จัก IRIS",
        "เลือกสูตร ART และจับคู่ยากับผลข้างเคียงได้ · สั่ง PrEP/PEP ได้",
    ],
    sections=[S1, S2, S3, S4])
