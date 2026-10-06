from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-GI"
OLD = "ตัวอย่างข้อสอบในสไลด์ NL2-GI"

CMP = '''<svg viewBox="0 0 740 360">
 <rect x="10" y="10" width="140" height="40" rx="8" class="sunk"/>
 <text x="80" y="35" text-anchor="middle" class="tb">ลักษณะ</text>
 <rect x="160" y="10" width="186" height="40" rx="8" class="c1"/>
 <text x="253" y="35" text-anchor="middle" class="tw">Pyogenic (PLA)</text>
 <rect x="356" y="10" width="186" height="40" rx="8" class="c2"/>
 <text x="449" y="35" text-anchor="middle" class="tw">Amebic (ALA)</text>
 <rect x="552" y="10" width="178" height="40" rx="8" class="bad"/>
 <text x="641" y="35" text-anchor="middle" class="tw">Melioidosis</text>
 <g>
 <text x="20" y="80" class="tb">ใคร</text>
 <text x="253" y="74" text-anchor="middle">50–70 ปี · DM</text><text x="253" y="92" text-anchor="middle" class="t3">cirrhosis · CA</text>
 <text x="449" y="74" text-anchor="middle">ผู้ใหญ่ชาย</text><text x="449" y="92" text-anchor="middle" class="t3">ท้องเสีย/มูกเลือดนำ</text>
 <text x="641" y="74" text-anchor="middle">อีสาน · DM</text><text x="641" y="92" text-anchor="middle" class="t3">CKD · thalassemia</text>
 <path d="M10 104H730" class="lnf"/>
 <text x="20" y="128" class="tb">เชื้อ/ที่มา</text>
 <text x="253" y="122" text-anchor="middle">K. pneumoniae, E. coli</text><text x="253" y="140" text-anchor="middle" class="t3">จาก biliary tract บ่อยสุด</text>
 <text x="449" y="122" text-anchor="middle">E. histolytica</text><text x="449" y="140" text-anchor="middle" class="t3">fecal-oral</text>
 <text x="641" y="122" text-anchor="middle">B. pseudomallei</text><text x="641" y="140" text-anchor="middle" class="t3">bipolar GNB</text>
 <path d="M10 152H730" class="lnf"/>
 <text x="20" y="176" class="tb">ภาพ U/S/CT</text>
 <text x="253" y="170" text-anchor="middle">rim enhancement</text><text x="253" y="188" text-anchor="middle" class="t3">หนึ่งหรือหลายก้อน</text>
 <text x="449" y="170" text-anchor="middle">ก้อนเดียว กลม ขอบชัด</text><text x="449" y="188" text-anchor="middle" class="t3">hypoechoic · ม้ามปกติ</text>
 <text x="641" y="170" text-anchor="middle">Swiss cheese</text><text x="641" y="188" text-anchor="middle" class="t3">ตับ + ม้าม (splenic abscess)</text>
 <path d="M10 200H730" class="lnf"/>
 <text x="20" y="224" class="tb">วินิจฉัย</text>
 <text x="253" y="224" text-anchor="middle">Aspirate G/S, C/S</text>
 <text x="449" y="218" text-anchor="middle">Serology (แยกอดีตไม่ได้)</text><text x="449" y="236" text-anchor="middle" class="t3">aspirate เพื่อ R/O PLA</text>
 <text x="641" y="218" text-anchor="middle">Melioid titer</text><text x="641" y="236" text-anchor="middle" class="t3">aspirate/hemoculture</text>
 <path d="M10 248H730" class="lnf"/>
 <text x="20" y="276" class="tb">รักษา</text>
 <rect x="160" y="258" width="186" height="92" rx="8" class="c1soft"/>
 <text x="253" y="280" text-anchor="middle" class="tb">Drainage + IV ATB</text>
 <text x="253" y="300" text-anchor="middle">4–6 สัปดาห์</text>
 <text x="253" y="320" text-anchor="middle" class="t3">ceftriaxone + metronidazole</text>
 <text x="253" y="338" text-anchor="middle" class="t3">amp/sulbactam · pip/tazo</text>
 <rect x="356" y="258" width="186" height="92" rx="8" class="c2soft"/>
 <text x="449" y="280" text-anchor="middle" class="tb">ATB อย่างเดียว</text>
 <text x="449" y="300" text-anchor="middle">PO metronidazole 7–10 วัน</text>
 <text x="449" y="320" text-anchor="middle" class="t3">→ paromomycin</text>
 <text x="449" y="338" text-anchor="middle" class="t3">drain ถ้า &gt; 5 cm / left lobe</text>
 <rect x="552" y="258" width="178" height="92" rx="8" class="badsoft"/>
 <text x="641" y="280" text-anchor="middle" class="tb">ATB อย่างเดียว</text>
 <text x="641" y="300" text-anchor="middle">Ceftazidime</text>
 <text x="641" y="320" text-anchor="middle">หรือ Meropenem</text>
 <text x="641" y="338" text-anchor="middle" class="t3">ceftriaxone ไม่ครอบคลุม</text>
 </g>
</svg>'''

LECTURE = lecture("07", "Liver abscess & amebiasis",
    subtitle="Pyogenic · amebic · melioidosis liver abscess · intestinal amebiasis",
    objectives=[
        "แยก pyogenic, amebic และ melioidosis liver abscess จากประวัติ ภาพ และ lab ได้",
        "เลือกการรักษา PLA: drainage + ceftriaxone/metronidazole 4–6 สัปดาห์",
        "รักษา amebic liver abscess ด้วย metronidazole แล้วตามด้วย paromomycin และรู้ข้อบ่งชี้ drainage",
        "นึกถึง melioidosis เมื่อมี splenic abscess/Swiss cheese ในผู้ป่วยอีสาน DM และให้ ceftazidime/meropenem",
    ],
    sections=[
    sec("gi-07-01", "Pyogenic liver abscess (PLA)",
        "DM/biliary disease · K. pneumoniae/E. coli · rim enhancement · drainage + ceftriaxone + metronidazole 4–6 wk", minutes=5,
        source=f"{D} หน้า 207–210, 216–217", nl=["2.3.11(8)", "B8.2.2(6)"],
        md='''
### ฝีในตับมี 3 ชนิดที่ต้องรู้
Pyogenic liver abscess (PLA) · Amebic liver abscess (ALA) · Melioidosis liver abscess

[[fig:gi-07-01-cmp]]

### ใครเป็น
- Peak age **50–70 ปี**
- Risk: **DM**, cirrhosis, cancer, immunocompromised

### เชื้อและที่มา
- **Gram-negative (K. pneumoniae, E. coli)**, gram-positive cocci, anaerobes
- ที่มา: **biliary tract infection (พบบ่อยสุด)**, bacteremia, intra-abdominal infection (appendicitis, diverticulitis — portal vein)

> *K. pneumoniae* hypervirulent strain ในผู้ป่วย DM ชาวเอเชีย อาจแพร่ไปตา (endophthalmitis) และสมอง (เสริม)

### อาการ
- ปวด RUQ, tender hepatomegaly, ตัวเหลือง
- ไข้ อ่อนเพลีย เบื่ออาหาร คลื่นไส้อาเจียน น้ำหนักลด
- **ปวดไหล่ขวา** (ถ้าฝีอยู่ชิดกระบังลม — referred pain)

### การตรวจ
- Lab: ↑WBC, AST/ALT/ALP/TB ปกติหรือสูง (ALP สูงเด่น — เสริม)
- U/S: hyper/hypoechoic lesion
- CT: **hypodense lesion with peripheral rim enhancement**
- **Aspiration ส่ง G/S, C/S** — imaging แยก ALA ได้ยาก จึงต้องใช้ aspiration ช่วยวินิจฉัย; hemoculture ด้วย (เสริม)

### การรักษา
**Drainage + IV ATB 4–6 สัปดาห์**
- **Ceftriaxone + metronidazole** (สูตรหลัก)
- Ampicillin/sulbactam
- Piperacillin/tazobactam

**Surgery** เมื่อ large abscess, ruptured abscess, peritonitis หรือต้องรักษาสาเหตุ (cholecystitis, appendicitis)
''',
        figs=[fig("gi-07-01-cmp", "เปรียบเทียบฝีในตับ 3 ชนิด", CMP,
                  "อ่านเป็นแถว: ใครเป็น เชื้อ ภาพ การวินิจฉัย และการรักษา — PLA ต้อง drain ส่วน ALA และ melioidosis ใช้ยาฆ่าเชื้ออย่างเดียวเป็นหลัก")],
        pearls=[
            "PLA: DM ผู้สูงอายุ, มาจาก biliary tract บ่อยสุด, K. pneumoniae/E. coli",
            "CT: hypodense lesion + peripheral rim enhancement",
            "Tx: drainage + ceftriaxone + metronidazole 4–6 สัปดาห์",
            "Aspiration ช่วยแยก PLA กับ ALA",
        ],
        items=[
            mcq("GI-07-01-1", "A 64-year-old man with poorly controlled type 2 diabetes and hypertension presents with fever and right upper quadrant pain for 5 days. Ultrasound shows a single 6-cm hypoechoic lesion in the right lobe of the liver. Amebic serology is negative. Which is the most appropriate treatment?",
                "Percutaneous drainage plus IV ceftriaxone and metronidazole", ["Oral metronidazole alone", "IV ceftazidime alone", "Oral praziquantel", "IV vancomycin alone"],
                explain='''ผู้สูงอายุ DM ควบคุมไม่ดี + ไข้ ปวด RUQ + ก้อนเดียวในตับ (amebic serology ลบ) = **pyogenic liver abscess** ต้อง **drainage + IV ceftriaxone + metronidazole** (ครอบคลุม gram-negative และ anaerobes) 4–6 สัปดาห์
- Metronidazole อย่างเดียวเป็นการรักษา amebic abscess ไม่ครอบคลุม Klebsiella
- Ceftazidime อย่างเดียวใช้ใน melioidosis (Swiss cheese ตับ+ม้าม)
- Praziquantel ใช้กับพยาธิใบไม้ตับ
- Vancomycin ไม่ครอบคลุม gram-negative ซึ่งเป็นเชื้อหลัก''',
                pearl="DM + ก้อนเดียวในตับ + ไข้ = PLA → drain + ceftriaxone/metronidazole", topic="PLA treatment",
                ref=[f"{D} หน้า 210, 216–217"], nl=["2.3.11(8)"], kind="old", src=OLD),
            mcq("GI-07-01-2", "A 68-year-old woman with gallstones has fever, jaundice and right upper quadrant pain. CT shows a 5-cm hypodense hepatic lesion with peripheral rim enhancement and a dilated common bile duct. What is the most common route by which this lesion develops?",
                "Ascending biliary tract infection", ["Hematogenous spread via the hepatic artery from endocarditis", "Portal venous spread from appendicitis", "Direct extension from a perforated duodenal ulcer", "Trophozoite invasion from the colon"],
                explain='''ฝีในตับที่มี rim enhancement ร่วมกับนิ่ว/ท่อน้ำดีขยาย = PLA และ **biliary tract infection เป็นที่มาที่พบบ่อยที่สุด** ตามสไลด์
- Hematogenous (bacteremia) และ portal (appendicitis/diverticulitis) เป็นที่มาที่รองลงมา
- Direct extension จาก perforated ulcer พบน้อย
- Trophozoite invasion จากลำไส้ใหญ่เป็นกลไกของ amebic liver abscess''',
                pearl="PLA มาจาก biliary tract บ่อยสุด", topic="PLA pathogenesis",
                ref=[f"{D} หน้า 208"], nl=["2.3.11(8)", "B8.2.2(6)"]),
            mcq("GI-07-01-3", "A 58-year-old man with diabetes has fever and right upper quadrant pain radiating to the right shoulder. CT shows a 7-cm rim-enhancing hepatic lesion. Imaging cannot reliably distinguish pyogenic from amebic abscess. Which investigation is most useful for definitive diagnosis and guiding antibiotic therapy?",
                "Aspiration of the abscess for Gram stain and culture", ["Stool examination for cysts", "Serum alpha-fetoprotein", "Triple-phase CT", "Repeat ultrasound in 1 week"],
                explain='''ตามสไลด์ imaging แยก PLA กับ ALA ยาก ต้องใช้ **aspiration ส่ง G/S, C/S** ซึ่งยังเป็นการรักษา (drainage) และนำทางการเลือกยาด้วย
- Stool exam หา cyst มี sensitivity ต่ำใน amebic liver abscess
- AFP ใช้กับ HCC ไม่ใช่ฝี
- Triple-phase CT ใช้แยก HCC และไม่บอกเชื้อ
- รอ 1 สัปดาห์ทำให้เสียเวลารักษาฝีที่กำลังโต''',
                pearl="แยก PLA กับ ALA → aspiration G/S, C/S", topic="Liver abscess aspiration",
                ref=[f"{D} หน้า 209"], nl=["2.3.11(8)"]),
        ]),

    sec("gi-07-02", "Amebiasis & amebic liver abscess (ALA)",
        "E. histolytica: dysentery → ALA ก้อนเดียวกลม · metronidazole แล้ว paromomycin · drain ถ้า > 5 cm/left lobe/ไม่ดีขึ้น 5–7 วัน", minutes=6,
        source=f"{D} หน้า 211–214, 218–221", nl=["2.3.11(8)", "2.3.1(12)"],
        md='''
### Intestinal amebiasis
- เชื้อ ***Entamoeba histolytica*** ติดต่อ **fecal-oral** (น้ำ/อาหารปนเปื้อน); risk: immunocompromised
- อาการ: ถ่ายเหลวหรือ **ถ่ายมูกเลือด**, ปวดท้อง, **tenesmus**
- Stool exam: **cyst และ trophozoite (ที่กิน RBC เข้าไป)**; stool PCR, antigen
- **Tx: metronidazole ตามด้วย paromomycin** (luminal agent กำจัด cyst ในลำไส้ ป้องกันกลับเป็นซ้ำ/แพร่เชื้อ)

### Extraintestinal amebiasis
- **Amebic liver abscess (พบบ่อยที่สุด)** — เชื้อเข้าทาง portal vein
- อื่น ๆ: สมอง ปอด ไต

### Amebic liver abscess (ALA)
- อาการคล้าย PLA (ไข้ ปวด RUQ ตับโตกดเจ็บ) แต่มี **ประวัติถ่ายเหลว/มูกเลือดนำมาก่อน**
- **U/S/CT: solitary lesion, round, well-defined, hypoechoic mass, ไม่มี splenic abscess** (มักอยู่ right lobe — เสริม)
- Aspiration เพื่อ R/O PLA (หนองสี "anchovy paste" — เสริม)
- Stool exam: cyst/trophozoite (**sensitivity ต่ำ**)
- **Serology** (แยก past infection ไม่ได้ — ในพื้นที่ระบาดบวกค้าง)

### การรักษา ALA
- **ATB อย่างเดียว: PO metronidazole 7–10 วัน** ตามด้วย **paromomycin**
- **Drainage** เมื่อ:
  - **ฝีใหญ่ > 5 cm** (เสี่ยงแตก)
  - **อยู่ left lobe** (เสี่ยงแตกเข้าเยื่อหุ้มหัวใจ)
  - **อาการไม่ดีขึ้นหลังให้ยา 5–7 วัน**

> ข้อสอบ: ALA 3 cm + titer บวก → **oral metronidazole**; ALA 8 cm → **percutaneous drainage** (ร่วมกับ metronidazole)
''',
        pearls=[
            "Amebiasis: dysentery + tenesmus + trophozoite กิน RBC",
            "ALA = extraintestinal amebiasis ที่พบบ่อยที่สุด; ก้อนเดียวกลมขอบชัด ไม่มี splenic abscess",
            "Tx: metronidazole แล้วตามด้วย paromomycin (กำจัด cyst)",
            "Drain ALA เมื่อ > 5 cm, left lobe หรือไม่ดีขึ้น 5–7 วัน",
            "Amebic serology แยก past infection ไม่ได้",
        ],
        items=[
            mcq("GI-07-02-1", "A 50-year-old woman had watery stools for 7 days and now has right upper quadrant pain. Ultrasound shows a 3-cm liver abscess in the right lobe. E. histolytica serology is positive. What is the most appropriate management?",
                "Oral metronidazole", ["IV ceftriaxone", "Percutaneous needle aspiration", "Percutaneous catheter drainage", "Open surgical drainage"],
                explain='''ประวัติถ่ายเหลวนำ + ฝีในตับ + **amebic titer บวก** = amebic liver abscess ขนาด **3 cm (< 5 cm)** อยู่ right lobe → **ATB อย่างเดียว: PO metronidazole** 7–10 วัน แล้วตามด้วย paromomycin
- Ceftriaxone ไม่ฆ่า *E. histolytica*
- Needle aspiration, catheter drainage และ open drainage สงวนไว้เมื่อฝี > 5 cm, left lobe หรือไม่ตอบสนองต่อยา 5–7 วัน''',
                pearl="ALA เล็ก (< 5 cm) → metronidazole อย่างเดียว", topic="ALA treatment",
                ref=[f"{D} หน้า 214, 220–221"], nl=["2.3.11(8)"], kind="old", src=OLD),
            mcq("GI-07-02-2", "A 25-year-old man has fever and right-sided abdominal pain for 2 weeks. Temperature 38 °C. There is RUQ tenderness and the liver is palpable 5 fingerbreadths below the costal margin. TB 0.9 mg/dL, AST 123, ALT 98, ALP 389 U/L. Ultrasound shows an 8-cm round homogeneous hypoechoic lesion in the upper right lobe. Amebic serology is positive. Besides metronidazole, what is the most appropriate management?",
                "Percutaneous drainage", ["Surgical resection", "Oral praziquantel", "IV ceftriaxone alone", "Observation with repeat ultrasound in 4 weeks"],
                explain='''ชายหนุ่ม ก้อนเดียวกลมขอบชัด hypoechoic ในตับ + serology บวก = amebic liver abscess ที่ **ใหญ่ 8 cm (> 5 cm)** เสี่ยงแตก → **percutaneous drainage** ร่วมกับ metronidazole (เฉลยในสไลด์: percutaneous drainage)
- Surgical resection ไม่จำเป็นสำหรับฝี
- Praziquantel ใช้กับ liver fluke/schistosomiasis
- Ceftriaxone ไม่ฆ่าอะมีบา
- การเฝ้าดูฝีขนาดใหญ่เสี่ยงแตกเข้าช่องท้อง/ช่องอก''',
                pearl="ALA > 5 cm → drainage + metronidazole", topic="ALA drainage indication",
                ref=[f"{D} หน้า 214, 218–219"], nl=["2.3.11(8)"], kind="old", src=OLD),
            mcq("GI-07-02-3", "A 30-year-old man has 3 weeks of bloody mucoid diarrhea with tenesmus. Stool microscopy shows motile trophozoites containing ingested red blood cells. After a course of metronidazole his symptoms resolve. Which additional drug should be given?",
                "Paromomycin", ["Albendazole", "Vancomycin", "Ciprofloxacin", "Loperamide"],
                explain='''Trophozoite ที่กิน RBC = *E. histolytica* (intestinal amebiasis) หลังให้ metronidazole (tissue amebicide) ต้องตามด้วย **paromomycin (luminal agent)** เพื่อกำจัด **cyst** ในลำไส้ ป้องกันกลับเป็นซ้ำและการแพร่เชื้อ
- Albendazole ใช้กับพยาธิตัวกลม
- Vancomycin ใช้กับ C. difficile
- Ciprofloxacin ใช้กับ bacterial dysentery ไม่ฆ่าอะมีบา
- Loperamide ห้ามใน dysentery''',
                pearl="Amebiasis: metronidazole → paromomycin (ฆ่า cyst)", topic="Intestinal amebiasis",
                ref=[f"{D} หน้า 211"], nl=["2.3.1(12)", "2.3.1(7)"]),
        ]),

    sec("gi-07-03", "Melioidosis liver abscess",
        "B. pseudomallei · อีสาน DM CKD thalassemia · Swiss cheese ตับ + splenic abscess · ceftazidime/meropenem", minutes=4,
        source=f"{D} หน้า 215, 222–223", nl=["2.3.1(16)", "2.3.11(8)"],
        md='''
### เชื้อและใครเป็น
- ***Burkholderia pseudomallei*** — อยู่ในดินและน้ำ (นาข้าว)
- Risk: **ภาคอีสาน, DM, CKD, thalassemia** (ชาวนา ดื่มเหล้า — เสริม)

### อาการ
- คล้าย PLA (ไข้ ปวด RUQ)
- **ปวด LUQ** ถ้ามี **splenic abscess**
- อาจมีปอดอักเสบ/ฝีหลายอวัยวะร่วม (เสริม)

### การตรวจ
- Serology: **↑melioid titer**
- Aspiration หนองส่ง G/S, C/S: **bipolar gram-negative bacilli** (safety pin)
- **U/S/CT: "Swiss cheese" ในตับและม้าม** = โพรงหนองเล็ก ๆ หลายโพรงรวมกลุ่ม

> **ถ้ามี splenic abscess ให้ ddx *B. pseudomallei* ไว้เสมอ**

### การรักษา
**ATB อย่างเดียว** (ไม่ต้อง drain ฝีเล็ก ๆ หลายโพรง)
- **Ceftazidime** หรือ **Meropenem** (intensive phase ≥ 10–14 วัน แล้วตามด้วย eradication phase ด้วย TMP/SMX 3–6 เดือน — เสริม)

> **Ceftriaxone ไม่ได้ผลกับ melioidosis** — ตัวลวงที่ข้อสอบชอบใช้
''',
        pearls=[
            "Multiple tiny abscess ตับ + ม้าม (Swiss cheese) ในคนอีสาน DM/CKD = melioidosis",
            "Splenic abscess → ddx B. pseudomallei เสมอ",
            "Gram stain: bipolar gram-negative bacilli",
            "Tx: ceftazidime หรือ meropenem (ไม่ใช่ ceftriaxone)",
        ],
        items=[
            mcq("GI-07-03-1", "A 60-year-old rice farmer from northeastern Thailand with poorly controlled diabetes and CKD presents with fever and abdominal pain. Temperature 39 °C, pulse 110/min. Ultrasound shows multiple tiny hypoechoic lesions in the liver and spleen. Which antibiotic is most appropriate?",
                "Ceftazidime", ["Ceftriaxone", "Tigecycline", "Amoxicillin-clavulanic acid", "Metronidazole"],
                explain='''คนอีสาน DM + CKD + **ฝีเล็กหลายโพรงทั้งตับและม้าม (Swiss cheese)** = melioidosis → **ceftazidime** (หรือ meropenem) ให้ยาอย่างเดียวโดยไม่ต้อง drain
- **Ceftriaxone ไม่ได้ผล** กับ *B. pseudomallei* แม้ครอบคลุม PLA
- Tigecycline ไม่ใช่ยาสำหรับ melioidosis
- Amoxicillin-clavulanate เป็นทางเลือกระยะ eradication ไม่ใช่ intensive phase ในผู้ป่วยรุนแรง
- Metronidazole ใช้กับ amebic abscess/anaerobe''',
                pearl="Swiss cheese ตับ+ม้าม = melioidosis → ceftazidime/meropenem", topic="Melioidosis treatment",
                ref=[f"{D} หน้า 215, 222–223"], nl=["2.3.1(16)", "2.3.11(8)"], kind="old", src=OLD),
            mcq("GI-07-03-2", "A 52-year-old man with thalassemia from Khon Kaen has fever and left upper quadrant pain for 10 days. CT shows multiple small abscesses in the spleen and liver. Aspirated pus shows gram-negative bacilli with bipolar staining. What is the most likely organism?",
                "Burkholderia pseudomallei", ["Klebsiella pneumoniae", "Entamoeba histolytica", "Salmonella Typhi", "Mycobacterium tuberculosis"],
                explain='''Risk factor (thalassemia, ภาคอีสาน) + **splenic abscess** (ปวด LUQ) + ฝีหลายโพรงในตับ + **bipolar gram-negative bacilli** (safety-pin) = *B. pseudomallei* (melioidosis)
- *K. pneumoniae* เป็นเชื้อหลักของ PLA แต่ไม่มี bipolar staining และมักไม่ทำ splenic abscess หลายก้อนแบบนี้
- *E. histolytica* เป็นโปรโตซัว ไม่ใช่ gram-negative bacilli และไม่ทำ splenic abscess
- *S.* Typhi ไม่ค่อยทำฝีในตับและม้าม
- TB ย้อมติด acid-fast ไม่ใช่ gram-negative''',
                pearl="Bipolar GNB + splenic abscess = B. pseudomallei", topic="Melioidosis diagnosis",
                ref=[f"{D} หน้า 215"], nl=["2.3.1(16)"]),
        ]),
    ])
