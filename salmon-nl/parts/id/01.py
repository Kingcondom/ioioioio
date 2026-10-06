from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Infectious"

# ---------------------------------------------------------------- 01-01 AUF
F_AUF = fig("id-01-01-f1", "Approach to acute undifferentiated fever ในไทย", '''<svg viewBox="0 0 740 470">
 <defs><marker id="id-01-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="10" width="240" height="40" rx="10" class="acsoft"/>
 <text x="370" y="35" text-anchor="middle" class="tb">ไข้ &lt; 2 สัปดาห์</text>
 <path d="M310 50L170 82" class="ln" marker-end="url(#id-01-01-a)"/>
 <path d="M430 50L560 82" class="ln" marker-end="url(#id-01-01-a)"/>
 <rect x="30" y="84" width="280" height="54" rx="10" class="box"/>
 <text x="170" y="106" text-anchor="middle" class="tb">Acute localized infection</text>
 <text x="170" y="126" text-anchor="middle" class="t3">ไอ หอบ → pneumonia · RUQ pain → cholecystitis</text>
 <rect x="410" y="84" width="300" height="54" rx="10" class="c1soft"/>
 <text x="560" y="106" text-anchor="middle" class="tb">Acute undifferentiated fever</text>
 <text x="560" y="126" text-anchor="middle" class="t3">ไม่มี localizing sign: ปวดหัว ปวดเมื่อย อ่อนเพลีย</text>
 <path d="M560 138V160" class="ln" marker-end="url(#id-01-01-a)"/>
 <rect x="10" y="162" width="724" height="40" rx="10" class="sunk"/>
 <text x="372" y="187" text-anchor="middle" class="tb">Basic: CBC · BUN/Cr · LFT · UA → แล้วดู clue + ประวัติสัมผัส</text>
 <path d="M80 202V228" class="ln" marker-end="url(#id-01-01-a)"/>
 <path d="M226 202V228" class="ln" marker-end="url(#id-01-01-a)"/>
 <path d="M372 202V228" class="ln" marker-end="url(#id-01-01-a)"/>
 <path d="M518 202V228" class="ln" marker-end="url(#id-01-01-a)"/>
 <path d="M664 202V228" class="ln" marker-end="url(#id-01-01-a)"/>
 <rect x="10" y="230" width="140" height="34" rx="8" class="c1"/>
 <text x="80" y="252" text-anchor="middle" class="tw">Dengue</text>
 <rect x="156" y="230" width="140" height="34" rx="8" class="ac"/>
 <text x="226" y="252" text-anchor="middle" class="tw">Leptospirosis</text>
 <rect x="302" y="230" width="140" height="34" rx="8" class="ok"/>
 <text x="372" y="252" text-anchor="middle" class="tw">Scrub typhus</text>
 <rect x="448" y="230" width="140" height="34" rx="8" class="bad"/>
 <text x="518" y="252" text-anchor="middle" class="tw">Malaria</text>
 <rect x="594" y="230" width="140" height="34" rx="8" class="c2"/>
 <text x="664" y="252" text-anchor="middle" class="tw">Melioidosis</text>
 <rect x="10" y="270" width="140" height="160" rx="8" class="c1soft"/>
 <text x="20" y="292" class="t3">ยุงลาย ในเมืองได้</text>
 <text x="20" y="312" class="t3">WBC ↓ ≤ 5,000</text>
 <text x="20" y="332" class="t3">Plt ↓ · Hct ↑</text>
 <text x="20" y="352" class="t3">tourniquet +</text>
 <text x="20" y="384" class="tb">≤ 5 วัน: NS1</text>
 <text x="20" y="406" class="tb">&gt; 5 วัน: IgM/IgG</text>
 <rect x="156" y="270" width="140" height="160" rx="8" class="acsoft"/>
 <text x="166" y="292" class="t3">ลุยน้ำ/ทำนา หนู</text>
 <text x="166" y="312" class="t3">ปวดน่อง หลังล่าง</text>
 <text x="166" y="332" class="t3">ตาแดง (suffusion)</text>
 <text x="166" y="352" class="t3">WBC ↑ AKI เหลือง</text>
 <text x="166" y="384" class="tb">MAT (4-fold)</text>
 <text x="166" y="406" class="t3">PCR / culture</text>
 <rect x="302" y="270" width="140" height="160" rx="8" class="oksoft"/>
 <text x="312" y="292" class="t3">เข้าป่า น้ำตก ไร่</text>
 <text x="312" y="312" class="t3">eschar ใต้ร่มผ้า</text>
 <text x="312" y="332" class="t3">LN โต</text>
 <text x="312" y="352" class="t3">relative brady</text>
 <text x="312" y="384" class="tb">IFA (4-fold)</text>
 <text x="312" y="406" class="t3">Weil-Felix เลิกใช้</text>
 <rect x="448" y="270" width="140" height="160" rx="8" class="badsoft"/>
 <text x="458" y="292" class="t3">ชายแดน/ป่า</text>
 <text x="458" y="312" class="t3">ภายใน 2 เดือน</text>
 <text x="458" y="332" class="t3">ไข้เป็นรอบ HSM</text>
 <text x="458" y="352" class="t3">ซีด เกล็ดเลือดต่ำ</text>
 <text x="458" y="384" class="tb">Thick/thin film</text>
 <text x="458" y="406" class="t3">RDT</text>
 <rect x="594" y="270" width="140" height="160" rx="8" class="c2soft"/>
 <text x="604" y="292" class="t3">ชาวนาอีสาน</text>
 <text x="604" y="312" class="t3">DM, thalassemia</text>
 <text x="604" y="332" class="t3">pneumonia, ฝีตับ/ม้าม</text>
 <text x="604" y="352" class="t3">ปอด + bacteremia</text>
 <text x="604" y="384" class="tb">Culture</text>
 <text x="604" y="406" class="t3">(H/C, sputum, pus)</text>
 <text x="370" y="456" text-anchor="middle" class="t3">Typhoid (ดูชุด GI): hemoculture · Widal ไม่แนะนำ</text>
</svg>''', "เริ่มจากแยก localized กับ undifferentiated แล้วใช้ basic lab + ประวัติสัมผัสชี้ไปโรคหลัก แต่ละคอลัมน์มี clue และ test ยืนยันตามสไลด์")

F_ABX = fig("id-01-01-f2", "ยาที่ครอบคลุมโรคไข้เขตร้อนแต่ละโรค (ตามสไลด์)", '''<svg viewBox="0 0 740 330">
 <rect x="10" y="10" width="190" height="40" rx="6" class="sunk"/>
 <text x="105" y="35" text-anchor="middle" class="tb">ยา \\ โรค</text>
 <rect x="206" y="10" width="126" height="40" rx="6" class="acsoft"/>
 <text x="269" y="35" text-anchor="middle" class="tb">Leptospirosis</text>
 <rect x="338" y="10" width="126" height="40" rx="6" class="oksoft"/>
 <text x="401" y="35" text-anchor="middle" class="tb">Rickettsia</text>
 <rect x="470" y="10" width="126" height="40" rx="6" class="misssoft"/>
 <text x="533" y="35" text-anchor="middle" class="tb">Typhoid</text>
 <rect x="602" y="10" width="128" height="40" rx="6" class="c2soft"/>
 <text x="666" y="35" text-anchor="middle" class="tb">Melioidosis</text>
 <text x="20" y="80" class="tb">Doxycycline</text>
 <rect x="206" y="60" width="126" height="34" rx="6" class="ok"/><text x="269" y="82" text-anchor="middle" class="tw">✓ mild/IV</text>
 <rect x="338" y="60" width="126" height="34" rx="6" class="ok"/><text x="401" y="82" text-anchor="middle" class="tw">✓ 1st line</text>
 <rect x="470" y="60" width="126" height="34" rx="6" class="sunk"/><text x="533" y="82" text-anchor="middle" class="t3">—</text>
 <rect x="602" y="60" width="128" height="34" rx="6" class="sunk"/><text x="666" y="82" text-anchor="middle" class="t3">—</text>
 <text x="20" y="120" class="tb">Azithromycin</text>
 <rect x="206" y="100" width="126" height="34" rx="6" class="ok"/><text x="269" y="122" text-anchor="middle" class="tw">✓ mild</text>
 <rect x="338" y="100" width="126" height="34" rx="6" class="ok"/><text x="401" y="122" text-anchor="middle" class="tw">✓ ท้อง/เด็ก</text>
 <rect x="470" y="100" width="126" height="34" rx="6" class="ok"/><text x="533" y="122" text-anchor="middle" class="tw">✓</text>
 <rect x="602" y="100" width="128" height="34" rx="6" class="sunk"/><text x="666" y="122" text-anchor="middle" class="t3">—</text>
 <text x="20" y="160" class="tb">Ceftriaxone</text>
 <rect x="206" y="140" width="126" height="34" rx="6" class="ok"/><text x="269" y="162" text-anchor="middle" class="tw">✓ severe</text>
 <rect x="338" y="140" width="126" height="34" rx="6" class="badsoft"/><text x="401" y="162" text-anchor="middle" class="t2">✗ ไม่ครอบ</text>
 <rect x="470" y="140" width="126" height="34" rx="6" class="ok"/><text x="533" y="162" text-anchor="middle" class="tw">✓</text>
 <rect x="602" y="140" width="128" height="34" rx="6" class="badsoft"/><text x="666" y="162" text-anchor="middle" class="t2">✗ ไม่ใช้</text>
 <text x="20" y="200" class="tb">Penicillin G / Amoxicillin</text>
 <rect x="206" y="180" width="126" height="34" rx="6" class="ok"/><text x="269" y="202" text-anchor="middle" class="tw">✓</text>
 <rect x="338" y="180" width="126" height="34" rx="6" class="badsoft"/><text x="401" y="202" text-anchor="middle" class="t2">✗ ไม่ครอบ</text>
 <rect x="470" y="180" width="126" height="34" rx="6" class="sunk"/><text x="533" y="202" text-anchor="middle" class="t3">—</text>
 <rect x="602" y="180" width="128" height="34" rx="6" class="badsoft"/><text x="666" y="202" text-anchor="middle" class="t2">✗ ไม่ใช้</text>
 <text x="20" y="240" class="tb">Ceftazidime / Meropenem</text>
 <rect x="206" y="220" width="126" height="34" rx="6" class="sunk"/><text x="269" y="242" text-anchor="middle" class="t3">—</text>
 <rect x="338" y="220" width="126" height="34" rx="6" class="sunk"/><text x="401" y="242" text-anchor="middle" class="t3">—</text>
 <rect x="470" y="220" width="126" height="34" rx="6" class="sunk"/><text x="533" y="242" text-anchor="middle" class="t3">—</text>
 <rect x="602" y="220" width="128" height="34" rx="6" class="ok"/><text x="666" y="242" text-anchor="middle" class="tw">✓ 10–14 วัน</text>
 <text x="20" y="280" class="tb">Cotrimoxazole</text>
 <rect x="206" y="260" width="126" height="34" rx="6" class="sunk"/><text x="269" y="282" text-anchor="middle" class="t3">—</text>
 <rect x="338" y="260" width="126" height="34" rx="6" class="sunk"/><text x="401" y="282" text-anchor="middle" class="t3">—</text>
 <rect x="470" y="260" width="126" height="34" rx="6" class="ok"/><text x="533" y="282" text-anchor="middle" class="tw">✓ ดื้อเพิ่ม</text>
 <rect x="602" y="260" width="128" height="34" rx="6" class="ok"/><text x="666" y="282" text-anchor="middle" class="tw">✓ 3–6 เดือน</text>
 <text x="370" y="318" text-anchor="middle" class="t3">Doxycycline ครอบทั้ง lepto และ scrub typhus → ยา empirical ที่ข้อสอบชอบเมื่อแยกสองโรคนี้ไม่ได้</text>
</svg>''', "อ่านตามแถว: ช่องเขียว = ยาที่สไลด์ให้ใช้ · ช่องแดง = กับดักที่ไม่ครอบคลุม · ช่องเทา = ไม่ใช่ยาหลัก (ตารางรวมเป็นส่วนเสริม)")

S1 = sec("id-01-01", "Acute undifferentiated fever (AUF)",
    "ไข้ < 2 wk ไม่มี localizing sign · rickettsia, lepto, typhoid, dengue, chikungunya, malaria · basic CBC BUN Cr LFT UA",
    minutes=6, source=f"{D} หน้า 4–6", nl=["2.1.1", "B1.5.2(8)", "B1.5.3(6)"],
    md='''
### Acute febrile illness = ไข้ < 2 สัปดาห์

| | Acute localized infection | Acute undifferentiated fever (AUF) |
|---|---|---|
| ลักษณะ | มีอาการจำเพาะ organ ชัด | **ไม่มี localizing sign** อาการไม่จำเพาะ |
| ตัวอย่าง | ไอ หอบ → pneumonia · RUQ pain → cholecystitis | fatigue, headache, malaise, arthralgia, N/V |

### สาเหตุที่พบบ่อยของ AUF ในไทย

- **Bacteria**: rickettsiosis (murine typhus, scrub typhus) · **leptospirosis** · typhoid fever · bacteremia ที่ไม่ทราบ primary source
- **Virus**: **dengue** · zika · chikungunya
- **Parasite**: **malaria**
- Melioidosis มักมี organ ชัด (pneumonia, abscess) แต่บางรายมาเป็น bacteremia ไข้อย่างเดียว ต้องนึกถึงในผู้ป่วย DM ชาวนาอีสาน

### Investigation

- **Basic**: CBC, BUN, Cr, LFT, UA
- **Specific** ตามโรคที่สงสัย: PBS (malaria, atypical lymphocyte), hemoculture, **NS1 antigen**, **rapid diagnostic test for malaria**, serology for dengue / scrub typhus / leptospirosis

[[fig:id-01-01-f1]]

### เลือกยา empirical อย่างไร (เสริม)

- แยก lepto กับ scrub typhus ไม่ได้ในวันแรก → **doxycycline** ครอบคลุมทั้งคู่ · ถ้ารุนแรงอาจให้ ceftriaxone ร่วมกับ doxycycline/azithromycin
- Dengue ห้ามให้ NSAID/aspirin และ antibiotic ไม่ช่วย — อย่าให้ยาฆ่าเชื้อถ้า clue เข้ากับ dengue ชัด

[[fig:id-01-01-f2]]

> ข้อสอบชอบให้ **ประวัติสัมผัส** เป็น clue หลัก: ลุยน้ำท่วม → lepto · เข้าป่า/น้ำตก + eschar → scrub typhus · ไปจังหวัดชายแดน → malaria · ชาวนาเบาหวานอีสาน → melioidosis · อยู่กรุงเทพฯ ไม่ได้ไปไหน → dengue
''',
    figs=[F_AUF, F_ABX],
    pearls=[
        "AUF = ไข้ < 2 สัปดาห์ที่ไม่มี localizing sign",
        "Basic Ix ของ AUF: CBC, BUN/Cr, LFT, UA ก่อนเสมอ",
        "AUF ไทย 5 โรคหลัก: dengue, lepto, scrub typhus, malaria, typhoid (+ melioid ใน DM)",
        "Doxycycline ครอบทั้ง lepto และ scrub typhus (เสริม)",
    ],
    items=[
        mcq("ID-01-01-1",
            "A 30-year-old male laborer has had high fever for 4 days with nausea and vomiting, nasal congestion, rhinorrhea and cough, without diarrhea. Temperature is 39 °C. The pharynx is injected with enlarged tonsils, there is no jaundice, and the liver is just palpable with mild tenderness. What is the most appropriate initial investigation?",
            "Complete blood count",
            ["Hemoculture", "Liver function test", "Serology for dengue virus infection", "Serology for Rickettsia infection"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไข้สูง 4 วัน อาการไม่จำเพาะ ไม่มี clue ชี้โรคใดชัด → เป็น **acute febrile illness ที่ต้องเริ่มจาก basic investigation** และตัวที่ให้ข้อมูลมากที่สุดคือ **CBC** (WBC ต่ำ + plt ต่ำ + Hct ขึ้น ชี้ dengue · WBC สูง PMN เด่น ชี้แบคทีเรีย/lepto · atypical lymphocyte · ซีด/plt ต่ำ ชวนทำ malaria film)
- Hemoculture ทำเมื่อสงสัย bacteremia/typhoid หรือ sepsis — ไม่ใช่การตรวจแรกของรายนี้
- LFT เป็น basic test เช่นกัน แต่ตับโตเล็กน้อยไม่มีเหลือง และ LFT ไม่ช่วยแยกโรคได้เท่า CBC
- Dengue serology (IgM/IgG) ใช้หลังวันที่ 5 และควรมีผล CBC ที่เข้ากันก่อน
- Rickettsia serology ไม่มีประวัติเข้าป่าหรือ eschar ให้สงสัย''',
            pearl="AUF ที่ยังไม่มี clue → CBC ก่อนเสมอ", topic="AUF basic investigation",
            ref=[f"{D} หน้า 6, 106–107"], nl=["2.1.1"]),
        mcq("ID-01-01-2",
            "A 45-year-old rice farmer from Udon Thani presents during the rainy season with 3 days of fever, headache and myalgia. He has no cough, no urinary symptoms and no localizing signs. He walked barefoot in flooded fields last week. He did not go into the forest. Which organism is the most likely cause?",
            "Leptospira interrogans",
            ["Orientia tsutsugamushi", "Plasmodium falciparum", "Salmonella Typhi", "Dengue virus"],
            explain='''AUF + **เดินเท้าเปล่าในน้ำท่วมขัง** = สัมผัสปัสสาวะหนูผ่านแผล/เยื่อบุ → **leptospirosis**
- Scrub typhus ต้องมีประวัติเข้าป่า พุ่มไม้ น้ำตก (chigger mite) และมักเห็น eschar — โจทย์บอกชัดว่าไม่ได้เข้าป่า
- Malaria ในไทยพบตามจังหวัดชายแดนป่าเขา (ตาก กาญจนบุรี ฯลฯ) ไม่ใช่นาข้าวอุดร
- Typhoid ติดทาง fecal–oral มักไข้ค่อย ๆ ขึ้นเป็นสัปดาห์ร่วมกับอาการทางเดินอาหาร
- Dengue เป็นไปได้ในฤดูฝน แต่ประวัติลุยน้ำเป็น clue ที่ข้อสอบตั้งใจให้ชี้ lepto''',
            pearl="ลุยน้ำท่วม/ทำนา + ไข้ปวดเมื่อย = leptospirosis", topic="AUF exposure clue",
            ref=[f"{D} หน้า 5, 17"], nl=["2.1.1", "2.3.1(13)"]),
        mcq("ID-01-01-3",
            "A 35-year-old man from Chanthaburi presents with 5 days of fever, myalgia and headache. Examination shows mild conjunctival suffusion and calf tenderness, but no rash. Laboratory: WBC 12,500/mm3 (neutrophils 82%), platelets 98,000/mm3, creatinine 1.8 mg/dL. He recently cleared bushes in an orchard after heavy rain. Scrub typhus and leptospirosis cannot be distinguished clinically. Which oral antibiotic covers both diseases?",
            "Doxycycline",
            ["Amoxicillin", "Ciprofloxacin", "Cotrimoxazole", "Cefixime"],
            explain='''ประวัติทั้งพุ่มไม้ (chigger mite) และน้ำขัง (lepto) แยกกันไม่ได้ → เลือกยาที่ครอบทั้งสองโรค = **doxycycline** (สไลด์ให้เป็นยา oral สำหรับ mild leptospirosis และเป็น 1st line ของ rickettsia)
- Amoxicillin รักษา lepto ได้ แต่ไม่ครอบ rickettsia (เชื้อ intracellular ไม่มี target ของ beta-lactam ที่ได้ผล)
- Ciprofloxacin ไม่ใช่ยาในสไลด์ของทั้งสองโรค
- Cotrimoxazole ใช้ eradication ของ melioidosis และ typhoid ไม่ใช่ยาหลักของสองโรคนี้
- Cefixime เป็น beta-lactam ไม่ครอบ scrub typhus''',
            pearl="แยก lepto กับ scrub ไม่ได้ → doxycycline", topic="Empirical AUF",
            ref=[f"{D} หน้า 21, 37"], nl=["2.3.1(13)", "B1.5.2(8)"]),
    ])

# ---------------------------------------------------------------- 01-02 Melioidosis
S2 = sec("id-01-02", "Melioidosis",
    "B. pseudomallei จากดิน/น้ำ · DM ชาวนาอีสาน · pneumonia บ่อยสุด + ฝีตับม้าม · culture · ceftazidime/meropenem 10–14 วัน → TMP/SMX 3–6 เดือน",
    minutes=7, source=f"{D} หน้า 7–16", nl=["2.3.1(16)", "2.3.11(8)"],
    md='''
### เชื้อและการติดต่อ

- **Burkholderia pseudomallei** อยู่ในดินและน้ำ
- ติดจากการ **สัมผัสดิน/น้ำปนเปื้อน** ผ่านแผล หรือ **สูดดม/กิน** ฝุ่นหรือน้ำที่ปนเปื้อน
- Risk: **DM** (สำคัญที่สุด), **thalassemia**, alcoholism, โรคตับ/ไต, ได้ immunosuppressant
- พบบ่อยสุด **ภาคอีสาน** โดยเฉพาะ **ชาวนา** ฤดูฝน

### อาการ — หลากหลายตาม organ

- Asymptomatic, acute หรือ chronic · localized หรือ disseminated
- **Pneumonia** (most common) · **bacteremia/septic shock**
- **Abscess**: ตับ ม้าม ต่อมน้ำเหลือง ผิวหนัง · pyelonephritis
- **Parotitis** (ในเด็ก) · osteomyelitis, septic arthritis
- เรื้อรังแบบไข้ ไอเป็นเดือนคล้าย TB ได้

> **Splenic abscess ต้อง ddx melioidosis ไว้เสมอ** · ฝีในตับ/ม้ามแบบหลายช่อง U/S เป็น **Swiss cheese / cartwheel (honeycomb) appearance**

### Investigation

- **Culture = gold standard** — ส่งตาม organ: sputum, hemoculture, pus จาก abscess, urine
- Gram stain: **Gram-negative bacilli, bipolar staining (safety pin appearance)**
- Serology (IHA) **specificity ต่ำ** ในไทยเพราะคนในพื้นที่มีภูมิอยู่แล้ว
- ไม่ขึ้นเชื้อแต่ยังสงสัย → **culture ซ้ำ**

### Management

| ระยะ | ยา | ระยะเวลา |
|---|---|---|
| Source control | Abscess drainage ตามข้อบ่งชี้ | — |
| **Initial intensive** | **IV ceftazidime** หรือ **IV meropenem** (shock/ICU) | **10–14 วัน** (นานกว่านี้ถ้ามี deep abscess) |
| **Eradication** ป้องกันเป็นซ้ำ | **Oral TMP/SMX (cotrimoxazole)** | **3–6 เดือน** |

- ฝีตับ/ม้ามจาก melioid ที่เป็นหลายช่องเล็ก ๆ มักรักษาด้วย **ATB อย่างเดียว** (ceftazidime/meropenem) ได้
- Ceftriaxone, amoxicillin, gentamicin **ไม่ใช้** (เชื้อดื้อ aminoglycoside โดยธรรมชาติ) (เสริม)
- Prevention: เลี่ยงทำงานสัมผัสดิน/น้ำด้วยมือเปล่าหรือเท้าเปล่า ใส่รองเท้าบูท ถุงมือ

> ไม่ได้ eradication phase → relapse ได้บ่อย นี่คือเหตุผลที่ต้องกิน TMP/SMX ต่ออีกหลายเดือน
''',
    pearls=[
        "Melioid = B. pseudomallei · DM + ชาวนาอีสาน + ฤดูฝน",
        "Pneumonia พบบ่อยสุด · splenic abscess ต้องนึกถึง melioid เสมอ",
        "Gram-negative bipolar (safety pin) · culture gold standard · serology spec ต่ำ",
        "IV ceftazidime/meropenem 10–14 วัน → oral TMP/SMX 3–6 เดือน",
    ],
    items=[
        mcq("ID-01-02-1",
            "A 60-year-old woman from Kalasin has had fever and chronic cough for 1 month and dyspnea for 2 weeks. Temperature 39 °C, RR 28/min, BP 140/80 mmHg. She has pale conjunctivae, no jaundice, a just-palpable liver and positive splenic dullness. Glucose 260 mg/dL, BUN 50 mg/dL, creatinine 4 mg/dL. Chest radiograph shows patchy infiltrates in both lower lungs. Abdominal ultrasound shows splenomegaly with multiple hypoechoic lesions. What is the most likely diagnosis?",
            "Melioidosis",
            ["Leptospirosis", "Salmonellosis", "Disseminated tuberculosis", "Amoebic liver abscess"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ผู้หญิงอีสาน + **DM (glucose 260)** + pneumonia ทั้งสองข้าง + **ฝีหลายก้อนในม้าม** = melioidosis (disseminated: ปอด + ม้าม)
- Leptospirosis เป็นไข้เฉียบพลันไม่ถึงเดือน ไม่ทำให้เกิดฝีในม้าม
- Salmonellosis ทำให้ splenic abscess ได้บ้าง แต่ไม่เข้ากับ pneumonia เรื้อรังในผู้ป่วยเบาหวานอีสาน
- Disseminated TB ไอเรื้อรังได้ แต่ภาพ U/S ม้ามหลายก้อน + เบาหวานอีสาน ข้อสอบตั้งใจให้ตอบ melioid ("splenic abscess ต้อง ddx melioid เสมอ")
- Amoebic liver abscess เป็นฝีเดี่ยวในตับ ไม่มีรอยโรคที่ม้ามหรือปอด''',
            pearl="DM + pneumonia + splenic abscess = melioidosis", topic="Melioidosis diagnosis",
            ref=[f"{D} หน้า 11–12"], nl=["2.3.1(16)"]),
        mcq("ID-01-02-2",
            "A 52-year-old diabetic farmer has fever and septic shock. Blood culture Gram stain shows Gram-negative bacilli with bipolar staining resembling safety pins. Which organism is most likely?",
            "Burkholderia pseudomallei",
            ["Klebsiella pneumoniae", "Pseudomonas aeruginosa", "Yersinia pestis", "Acinetobacter baumannii"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**Gram-negative bacilli + bipolar staining (safety pin)** ในชาวนาเบาหวาน = **B. pseudomallei**
- Klebsiella เป็น GNB ที่ทำให้ฝีตับใน DM ได้ แต่ไม่ติดสีแบบ bipolar และมี capsule หนา
- Pseudomonas เป็น GNB ปกติ ไม่มี bipolar staining เด่น และมักเป็นเชื้อในโรงพยาบาล
- Yersinia pestis ก็มี bipolar (safety pin) ได้ แต่เป็นกาฬโรคที่ไม่มีในไทยปัจจุบันและไม่มีบริบทหนู/หมัด
- Acinetobacter เป็น Gram-negative coccobacilli เชื้อดื้อยาใน ICU''',
            pearl="GNB bipolar safety pin + DM ชาวนา = B. pseudomallei", topic="Melioid Gram stain",
            ref=[f"{D} หน้า 9, 13–14"], nl=["2.3.1(16)"]),
        mcq("ID-01-02-3",
            "A 48-year-old man with poorly controlled diabetes presents with 2 weeks of fever and left upper quadrant pain. Ultrasound of the abdomen shows multiple liver and splenic lesions with a honeycomb (cartwheel) appearance. What is the most likely causative agent?",
            "Burkholderia pseudomallei",
            ["Staphylococcus aureus", "Acinetobacter baumannii", "Pseudomonas aeruginosa", "Entamoeba histolytica"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ฝีหลายก้อนทั้ง **ตับและม้าม** แบบ **cartwheel/Swiss cheese** ในผู้ป่วยเบาหวาน = **melioidosis** (ฝีม้ามต้องนึกถึงเสมอ)
- S. aureus ทำให้ฝีจาก bacteremia/IE ได้ แต่ไม่ใช่ภาพ honeycomb และไม่ใช่คำตอบคลาสสิกในบริบทเบาหวานไทย
- Acinetobacter เป็นเชื้อดื้อยาในโรงพยาบาล ไม่ใช่สาเหตุฝีตับม้ามในชุมชน
- Pseudomonas ไม่ใช่สาเหตุฝีตับม้ามที่พบบ่อยในชุมชน
- E. histolytica ให้ฝีตับเดี่ยว ไม่เกิดฝีม้าม''',
            pearl="ฝีตับ + ม้าม แบบ honeycomb ใน DM = melioid → ATB อย่างเดียวได้", topic="Melioid abscess",
            ref=[f"{D} หน้า 15–16"], nl=["2.3.1(16)", "2.3.11(8)"]),
        mcq("ID-01-02-4",
            "A 55-year-old diabetic man with culture-proven melioidosis pneumonia and bacteremia has completed 14 days of intravenous ceftazidime and is now afebrile. What is the most appropriate next step to prevent relapse?",
            "Oral trimethoprim-sulfamethoxazole for 3 to 6 months",
            ["Stop antibiotics and follow up clinically", "Oral amoxicillin-clavulanate for 7 days", "Oral ciprofloxacin for 2 weeks", "Intramuscular ceftriaxone once weekly for 3 months"],
            explain='''Melioidosis รักษาเป็นสองระยะ: **initial intensive (IV ceftazidime/meropenem 10–14 วัน)** แล้วต่อด้วย **eradication phase = oral TMP/SMX 3–6 เดือน** เพื่อป้องกัน relapse
- หยุดยาเลยเสี่ยง relapse สูง ซึ่งเป็นปัญหาหลักของโรคนี้
- Amoxicillin-clavulanate เป็นทางเลือกสำรองของ eradication ได้ (เสริม) แต่ 7 วันสั้นเกินไปมาก
- Ciprofloxacin มีอัตรา relapse สูง ไม่ใช้
- Ceftriaxone ไม่ได้ผลกับ B. pseudomallei และไม่มีรูปแบบนี้''',
            pearl="Melioid: IV 10–14 วัน → TMP/SMX 3–6 เดือน", topic="Melioid eradication",
            ref=[f"{D} หน้า 10"], nl=["2.3.1(16)"]),
    ])

# ---------------------------------------------------------------- 01-03 Leptospirosis
S3 = sec("id-01-03", "Leptospirosis",
    "ฉี่หนูผ่านแผล · ปวดน่อง + conjunctival suffusion · Weil: jaundice + AKI + pulmonary hemorrhage · MAT gold standard · mild doxy/amox/azithro · severe PGS/ceftriaxone",
    minutes=8, source=f"{D} หน้า 17–31", nl=["2.3.1(13)", "2.1.13"],
    md='''
### เชื้อและการติดต่อ

- **Leptospira interrogans** (spirochete)
- สัมผัส **ปัสสาวะของสัตว์ที่ติดเชื้อ (หนู)** ผ่าน **ผิวหนังที่มีแผล หรือเยื่อบุ** — ลุยน้ำท่วม ทำนา จับปลา
- Spectrum: asymptomatic → **mild (anicteric)** → **severe (icteric, Weil's disease)**

### Anicteric leptospirosis (mild)

- Fever, headache
- **Myalgia เด่นที่น่องและหลังส่วนล่าง** (calves & lower back)
- **Conjunctival suffusion** = ตาแดงแบบไม่มีขี้ตา (injection without exudate)
- Mild jaundice, aseptic meningitis, lymphadenopathy, hepatosplenomegaly, rash

### Icteric leptospirosis (Weil's disease)

- **Multiple organ failure**: liver failure (jaundice เด่น bilirubin สูงมากแต่ AST/ALT ขึ้นไม่มาก) + **AKI** (AIN/ATN, มักเป็น **non-oliguric + hypokalemia** (เสริม))
- **Pulmonary hemorrhage** (สาเหตุตายสำคัญ) · purpura, ↓platelet · hypotension
- Myocarditis, pericarditis, arrhythmia

### Investigation

- CBC: **↑WBC (PMN เด่น)**, ↓platelet · Cr ↑, AST/ALT ↑, TB ↑ · UA มี WBC/RBC/protein ได้
- Direct detection จาก blood, urine, CSF: dark-field microscopy, **PCR**, culture
- **Serology = gold standard: Microscopic agglutination test (MAT)** → **4-fold rising** (เช่น titer 80 → 320)
- ตัวอย่าง: **blood/CSF ใน 10 วันแรก** หลังจากนั้นตรวจ **urine** (เชื้อออกทางปัสสาวะ)

### Management

| ความรุนแรง | ยา |
|---|---|
| Mild | **Oral doxycycline** (100 mg bid 7 วัน (เสริม)) · oral amoxicillin · oral azithromycin |
| Severe | **IV penicillin G** · **IV ceftriaxone** · IV doxycycline |

- Supportive: ดูแล AKI (อาจต้อง dialysis), เลือดออก, ระบบหายใจ (เสริม)
- Prevention: เลี่ยงแอ่งน้ำขัง สวมรองเท้าบูท กำจัดหนูและขยะที่เป็นอาหารหนู · doxycycline 200 mg/wk เป็น prophylaxis ในผู้ที่ต้องลุยน้ำ (เสริม)

> Lepto vs dengue: lepto **WBC สูง PMN เด่น** + ปวดน่อง + conjunctival suffusion + AKI/jaundice · dengue **WBC ต่ำ** Hct ขึ้น
> Widal (typhoid) และ Weil-Felix (rickettsia) **ไม่แนะนำแล้ว** — ถ้าสงสัย lepto ให้ส่ง **leptospira titer/MAT**
''',
    pearls=[
        "Lepto: ปวดน่อง + conjunctival suffusion + ประวัติลุยน้ำ",
        "Weil's disease = jaundice + AKI + bleeding/pulmonary hemorrhage",
        "MAT = gold standard ต้อง 4-fold rising · blood/CSF 10 วันแรก หลังจากนั้น urine",
        "Mild: doxy/amox/azithro oral · Severe: IV penicillin G / ceftriaxone",
        "Lepto WBC สูง PMN เด่น ต่างจาก dengue ที่ WBC ต่ำ",
    ],
    items=[
        mcq("ID-01-03-1",
            "A 40-year-old Thai man has had fever and generalized myalgia for 3 days. His neighborhood has been flooded and he has to wade through water every day. Temperature 39 °C, BP 120/80 mmHg, PR 110 bpm, RR 24/min. He has mild jaundice, clear lungs and a liver palpable 2 cm below the right costal margin. What is the most likely diagnosis?",
            "Leptospirosis",
            ["Enteric fever", "Dengue fever", "Scrub typhus", "Murine typhus"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ลุยน้ำท่วมทุกวัน + ไข้ปวดเมื่อย + เหลืองเล็กน้อย ตับโต = **leptospirosis** (anicteric–icteric)
- Enteric fever ติดทางอาหาร/น้ำดื่ม ไข้ค่อย ๆ ขึ้น ไม่ได้สัมพันธ์กับการลุยน้ำ
- Dengue ไม่ค่อยเหลือง และไม่มี clue ประวัติสัมผัสแบบนี้
- Scrub typhus ต้องเข้าป่า/พุ่มไม้ และหา eschar
- Murine typhus จากหมัดหนูในเมือง อาการไม่เด่นเรื่องเหลือง และไม่ผูกกับการลุยน้ำ''',
            pearl="น้ำท่วม + ไข้ + เหลือง = lepto", topic="Lepto diagnosis",
            ref=[f"{D} หน้า 22–23"], nl=["2.3.1(13)"]),
        mcq("ID-01-03-2",
            "A 35-year-old woman has had fever and headache for 10 days. Temperature 38 °C, PR 100 bpm, BP 100/60 mmHg. There is conjunctival injection, the liver is just palpable, the spleen is not palpable, and there is a generalized maculopapular rash on the trunk and extremities. Hct 42%, WBC 7,000/mm3 (PMN 60%, L 40%), platelets 80,000/mm3, total bilirubin 15 mg/dL. What is the most likely diagnosis?",
            "Leptospirosis",
            ["Dengue fever", "Scrub typhus", "Typhoid fever", "Viral hepatitis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (เฉลยเป็นภาพ — ตอบตามหลักฐานในสไลด์ส่วน leptospirosis)",
            explain='''ไข้ + **conjunctival injection** + ผื่น + เกล็ดเลือดต่ำ + **bilirubin สูงถึง 15** = **icteric leptospirosis** (ตับวาย + เกล็ดเลือดต่ำ) — ข้อนี้อยู่ในชุดข้อสอบ lepto ของสไลด์
- Dengue ไข้ 10 วันเกิน critical phase แล้ว และไม่ทำให้ bilirubin สูงขนาดนี้
- Scrub typhus ทำให้เหลืองได้บ้าง แต่ต้องมีประวัติเข้าป่า/eschar ซึ่งโจทย์ไม่ให้
- Typhoid ไม่ทำให้ตาแดงและ bilirubin 15
- Viral hepatitis มักไข้ลงเมื่อเริ่มเหลือง ไม่มีเกล็ดเลือดต่ำ ตาแดงและผื่นแบบนี้''',
            pearl="ตาแดง + bilirubin สูงมาก + plt ต่ำ = Weil's disease", topic="Icteric leptospirosis",
            ref=[f"{D} หน้า 19, 24–25"], nl=["2.3.1(13)", "2.1.13"]),
        mcq("ID-01-03-3",
            "A 30-year-old farmer has had high-grade fever and headache for 5 days with calf myalgia, bilateral conjunctival suffusion and jaundice. WBC 15,000/mm3 (neutrophils 80%). Urinalysis shows white blood cells. What is the most appropriate investigation to confirm the diagnosis?",
            "Leptospira microscopic agglutination test",
            ["Serum NS1 antigen", "Widal test", "Indirect immunofluorescence assay for Rickettsia", "Weil-Felix test"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ชาวนา + **ปวดน่อง + conjunctival suffusion + เหลือง + AKI/UA ผิดปกติ** + WBC สูง PMN เด่น = **severe leptospirosis** → ยืนยันด้วย **MAT** (gold standard, 4-fold rising)
- NS1 ใช้วินิจฉัย dengue ซึ่ง WBC จะต่ำ ไม่ใช่ 15,000
- Widal เป็น serology ของ typhoid ที่ไม่แนะนำแล้ว
- IFA for Rickettsia ใช้กับ scrub/murine typhus — ไม่มีประวัติเข้าป่าหรือ eschar
- Weil-Felix เป็น test เก่าของ rickettsia ที่เลิกใช้แล้ว (ชื่อคล้าย Weil's disease เป็นกับดัก)''',
            pearl="สงสัย lepto → MAT (4-fold rising)", topic="Lepto investigation",
            ref=[f"{D} หน้า 20, 26–27"], nl=["2.3.1(13)"]),
        mcq("ID-01-03-4",
            "A 40-year-old man went fishing with 4 friends. All of them developed fever, and he now has jaundice and hepatomegaly. None of them has been into the forest. What is the most appropriate investigation?",
            "Leptospira antibody titer",
            ["Widal test", "Hemoculture", "Weil-Felix titer", "Melioidosis titer"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''หลายคนสัมผัส **น้ำปนเปื้อนแหล่งเดียวกัน** (จับปลา) แล้วไข้ + เหลือง = cluster ของ **leptospirosis** → ส่ง **leptospira titer (MAT)**
- Widal ใช้ใน typhoid แต่ปัจจุบันไม่แนะนำ (สไลด์เฉลยไว้)
- Hemoculture ช่วยหา bacteremia ทั่วไป/typhoid แต่ไม่ใช่การตรวจที่ตรงประเด็น และ leptospira ต้องใช้อาหารเลี้ยงเชื้อพิเศษ
- Weil-Felix ใช้ใน rickettsia แต่ไม่แนะนำแล้ว และไม่มีประวัติเข้าป่า
- Melioidosis titer specificity ต่ำ และ melioid ไม่ระบาดเป็นกลุ่มหลังจับปลาแบบนี้''',
            pearl="ไข้ + เหลืองเป็นกลุ่มหลังสัมผัสน้ำ = lepto", topic="Lepto exposure",
            ref=[f"{D} หน้า 28–29"], nl=["2.3.1(13)"]),
        mcq("ID-01-03-5",
            "A 38-year-old man with leptospirosis has jaundice (total bilirubin 12 mg/dL), creatinine 3.4 mg/dL, platelets 40,000/mm3 and hemoptysis. He is admitted to the intensive care unit. Which antibiotic is most appropriate?",
            "Intravenous penicillin G",
            ["Oral doxycycline", "Oral amoxicillin", "Intravenous ceftazidime", "Intravenous vancomycin"],
            explain='''นี่คือ **severe leptospirosis (Weil's disease)**: jaundice + AKI + เลือดออก/pulmonary hemorrhage → ต้องให้ยา **IV**: **penicillin G** หรือ ceftriaxone หรือ IV doxycycline
- Oral doxycycline และ oral amoxicillin ใช้กับ mild leptospirosis เท่านั้น
- Ceftazidime เป็นยาของ melioidosis/Pseudomonas ไม่ใช่ยาในสไลด์ของ lepto
- Vancomycin ครอบเฉพาะ Gram-positive ไม่ครอบ spirochete''',
            pearl="Severe lepto → IV penicillin G หรือ ceftriaxone", topic="Lepto treatment",
            ref=[f"{D} หน้า 19, 21"], nl=["2.3.1(13)"]),
    ])

# ---------------------------------------------------------------- 01-04 Rickettsial
S4 = sec("id-01-04", "Rickettsial diseases: scrub typhus, murine typhus, spotted fever",
    "Scrub = O. tsutsugamushi ไร chigger มี eschar · murine = R. typhi หมัดหนูในเมือง ไม่มี eschar · IFA gold standard · doxycycline 1st line · azithro ในท้อง/เด็ก",
    minutes=9, source=f"{D} หน้า 32–53", nl=["B1.5.2(8)", "2.1.1", "2.1.50"],
    md='''
### 3 กลุ่ม

| กลุ่ม | เชื้อ | พาหะ | แหล่ง | Eschar |
|---|---|---|---|---|
| **Scrub typhus** | **Orientia tsutsugamushi** | **Chigger mite (ตัวอ่อนไร)** | ป่าเขา น้ำตก พุ่มไม้ ไร่สวน | **มี** |
| **Murine (endemic) typhus** | **Rickettsia typhi** | **Rat flea (หมัดหนู)** | หนูในเมือง | **ไม่มี** |
| Epidemic typhus | R. prowazekii | Louse (เหา) | — | ไม่มี |
| Spotted fever group | R. helvetica, R. japonica, R. conorii, R. rickettsii (RMSF, อเมริกา) | **Tick (เห็บ)** | — | มี ยกเว้น RMSF |

### อาการ

- Fever, **severe headache**, malaise · maculopapular rash
- **Relative bradycardia** (ชีพจรไม่เร็วตามไข้)
- **Lymphadenopathy** (scrub typhus)
- **Eschar** (scrub typhus/SFG): แผลดำเล็กไม่เจ็บ มักอยู่ **ใต้ร่มผ้า — รักแร้ ขาหนีบ ใต้ราวนม** → ต้องตรวจหาให้ทั่ว
- Severe: multiorgan failure (pneumonitis/ARDS, AKI, hepatitis, meningoencephalitis)

| | Scrub typhus eschar | Cutaneous anthrax |
|---|---|---|
| ขนาด | **เล็ก** | **ใหญ่** มี **บวมรอบ ๆ** มาก |
| ตำแหน่ง | รักแร้ ขาหนีบ ใต้ราวนม | มือ แขน หน้า (ส่วนที่สัมผัสสัตว์) |
| ประวัติ | เข้าป่า/พุ่มไม้ | สัมผัสสัตว์ ขนสัตว์ เนื้อ |

### Investigation

- CBC: WBC ต่ำหรือสูงได้, ↓platelet · ↑Cr, ↑AST/ALT, ↑TB
- **Serology: Indirect immunofluorescence assay (IFA) = gold standard** (4-fold rising) · ELISA/rapid test ใช้ได้ในทางปฏิบัติ
- **Weil-Felix test เลิกใช้แล้ว** (sensitivity/specificity ต่ำ)

### Management

| ความรุนแรง | ยา |
|---|---|
| Mild | **Oral doxycycline (1st line)** (100 mg bid 7 วัน (เสริม)) · **oral azithromycin ในหญิงตั้งครรภ์และเด็ก < 8 ปี** |
| Severe (organ failure) | IV doxycycline · IV azithromycin · IV chloramphenicol |

- ได้ยา **2–3 วัน** อาการมักดีขึ้นชัด (ไข้ลงเร็ว) — ถ้าไม่ดีขึ้นให้คิดถึงโรคอื่น (เสริม)
- Doxycycline มีผลต่อการพัฒนากระดูกและฟัน (ฟันเปลี่ยนสี) → เลี่ยงในเด็กเล็ก/ตั้งครรภ์
- Prevention: ใส่เสื้อผ้าปกปิดมิดชิด ใช้ยากันแมลง

> ไม่ดีขึ้นด้วย amoxicillin/ceftriaxone + มี eschar → เป็น **intracellular organism** ต้องใช้ doxycycline หรือ azithromycin
> Beta-lactam (penicillin, ceftriaxone, ceftazidime) **ไม่ได้ผล** กับ rickettsia
''',
    pearls=[
        "Scrub typhus = O. tsutsugamushi + chigger mite + eschar ใต้ร่มผ้า + LN โต",
        "Murine typhus = R. typhi + หมัดหนูในเมือง + ไม่มี eschar",
        "IFA = gold standard · Weil-Felix เลิกใช้",
        "Doxycycline 1st line · azithromycin ในท้องหรือเด็ก < 8 ปี",
        "Eschar เล็กใต้ร่มผ้า = scrub · eschar ใหญ่บวมที่มือ = anthrax",
    ],
    items=[
        mcq("ID-01-04-1",
            "A man develops fever after a trip to a waterfall. Examination shows a painless black eschar in the groin and tender regional lymph nodes. Which vector most likely transmitted his infection?",
            "Chigger mite",
            ["Louse", "Aedes aegypti", "Tick", "Flea"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไปน้ำตก/ป่า + **eschar** + LN โต = **scrub typhus** ซึ่งเกิดจาก O. tsutsugamushi ที่มี **chigger mite (ตัวอ่อนไร)** เป็นพาหะ
- Louse (เหา) เป็นพาหะของ epidemic typhus ซึ่งไม่มี eschar และไม่พบในไทย
- Aedes aegypti เป็นพาหะของ dengue/chikungunya ไม่มี eschar
- Tick (เห็บ) เป็นพาหะของ spotted fever group ซึ่งมี eschar ได้ แต่ในบริบทป่าน้ำตกไทยคำตอบหลักคือ scrub typhus
- Flea (หมัดหนู) เป็นพาหะของ murine typhus ในเมือง ไม่มี eschar''',
            pearl="ป่า/น้ำตก + eschar = scrub typhus = chigger mite", topic="Rickettsia vector",
            ref=[f"{D} หน้า 33–34, 40–41"], nl=["B1.5.2(8)", "B1.5.1(5)"]),
        mcq("ID-01-04-2",
            "A woman has had fever for 10 days without dyspnea or cough. Examination shows hepatomegaly, clear breath sounds and a black eschar in the axilla. What is the most appropriate investigation?",
            "Indirect immunofluorescence assay for scrub typhus",
            ["NS1 antigen", "IFA for leptospirosis", "Chikungunya IgM", "Weil-Felix test"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**Eschar ที่รักแร้** (ใต้ร่มผ้า) + ไข้ 10 วัน + ตับโต = **scrub typhus** → ส่ง **IFA (gold standard)**
- NS1 ใช้ใน dengue ภายใน 5 วันแรก — ไข้ 10 วันแล้วและ dengue ไม่มี eschar
- Leptospirosis ไม่มี eschar และ gold standard คือ MAT
- Chikungunya เด่นเรื่องปวดข้อ ไม่มี eschar
- Weil-Felix เลิกใช้แล้วเพราะ sensitivity/specificity ต่ำ''',
            pearl="Eschar ใต้ร่มผ้า → IFA for scrub typhus", topic="Scrub typhus investigation",
            ref=[f"{D} หน้า 36, 42–47"], nl=["B1.5.2(8)"]),
        mcq("ID-01-04-3",
            "A 13-year-old boy has fever for 1 week with cervical lymphadenopathy, hepatosplenomegaly and a round, painless, black necrotic ulcer on his back. What is the most appropriate treatment?",
            "Doxycycline",
            ["Clindamycin", "Ceftriaxone", "Cotrimoxazole", "Cefotaxime"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (รวมสองข้อในสไลด์หน้า 44–49)",
            explain='''แผลดำไม่เจ็บ (**eschar**) + LN + HSM = **scrub typhus** → ยา 1st line คือ **doxycycline** (เด็กอายุ 13 ปีให้ได้ ส่วนเด็ก < 8 ปีหรือหญิงตั้งครรภ์ใช้ azithromycin)
- Clindamycin ไม่ครอบเชื้อ intracellular กลุ่ม rickettsia
- Ceftriaxone และ cefotaxime เป็น beta-lactam ไม่ได้ผลกับ O. tsutsugamushi
- Cotrimoxazole ไม่ใช่ยาของ rickettsia''',
            pearl="Eschar → doxycycline (เด็ก < 8 ปี/ท้อง → azithromycin)", topic="Scrub typhus treatment",
            ref=[f"{D} หน้า 37, 44–49"], nl=["B1.5.2(8)"]),
        mcq("ID-01-04-4",
            "A patient has subacute fever, headache, myalgia, hepatosplenomegaly, lymphadenopathy, conjunctival suffusion and an eschar. Renal function is abnormal and urinalysis shows protein 2+. What is the drug of choice?",
            "Doxycycline",
            ["Ceftriaxone", "Ceftazidime", "Penicillin G", "Gentamicin"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''มีทั้ง **eschar + LN** (scrub typhus) และ **conjunctival suffusion + ไตผิดปกติ** (lepto) → เลือกยาที่ครอบทั้งสองโรค = **doxycycline**
- Ceftriaxone และ penicillin G รักษา lepto ได้ แต่ไม่ครอบ scrub typhus ซึ่งมี eschar ชัด
- Ceftazidime เป็นยาของ melioidosis
- Gentamicin ไม่ใช่ยาของทั้งสองโรค และเป็นพิษต่อไตที่ผิดปกติอยู่แล้ว''',
            pearl="Eschar + clue ของ lepto → doxycycline ครอบทั้งคู่", topic="Scrub vs lepto",
            ref=[f"{D} หน้า 50–51"], nl=["B1.5.2(8)", "2.3.1(13)"]),
        mcq("ID-01-04-5",
            "A 38-year-old man has fever, myalgia and headache that did not improve after 3 days of amoxicillin-clavulanate. Temperature is 38 °C. He has a pale maculopapular rash and a lesion with central black necrosis. Doxycycline is not available. What is the most appropriate treatment?",
            "Azithromycin",
            ["Ciprofloxacin", "Meropenem", "Ceftriaxone", "Amoxicillin-clavulanate at a higher dose"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไม่ตอบสนองต่อ beta-lactam + ผื่น + **แผลตรงกลางดำ (eschar)** = scrub typhus ซึ่งเป็น intracellular → เมื่อไม่มี doxycycline ใช้ **azithromycin**
- Ciprofloxacin ไม่ได้อยู่ในยาที่แนะนำของ rickettsia และมีรายงานล้มเหลว
- Meropenem และ ceftriaxone เป็น beta-lactam ไม่ได้ผลกับ rickettsia
- เพิ่มขนาด amoxicillin-clavulanate ไม่ช่วย เพราะเชื้อไม่ไวต่อ beta-lactam''',
            pearl="Beta-lactam ไม่ได้ผล + eschar → azithro/doxy", topic="Rickettsia treatment",
            ref=[f"{D} หน้า 37, 52–53"], nl=["B1.5.2(8)"]),
    ])

LECTURE = lecture("01", "Acute febrile illness: bacterial zoonoses",
    "AUF · melioidosis · leptospirosis · scrub & murine typhus",
    objectives=[
        "แยก acute localized infection กับ AUF และเลือก basic/specific investigation ได้",
        "ใช้ประวัติสัมผัส (น้ำท่วม ป่า ดิน) แยก lepto, scrub typhus, melioid ได้",
        "เลือก test ยืนยัน (MAT, IFA, culture) และเลี่ยง test ที่เลิกใช้ (Widal, Weil-Felix)",
        "สั่งยาตามความรุนแรงและสองระยะของ melioidosis ได้",
    ],
    sections=[S1, S2, S3, S4])
