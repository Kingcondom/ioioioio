from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Infectious"

# ---------------------------------------------------------------- 02-01 Dengue dx
F_PHASE = fig("id-02-01-f1", "สามระยะของ dengue กับ Hct / platelet / WBC", '''<svg viewBox="0 0 740 400">
 <defs><marker id="id-02-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="70" y="10" width="300" height="30" rx="6" class="misssoft"/>
 <text x="220" y="30" text-anchor="middle" class="tb">Febrile phase (วัน 1–4/5)</text>
 <rect x="372" y="10" width="148" height="30" rx="6" class="badsoft"/>
 <text x="446" y="30" text-anchor="middle" class="tb">Critical 24–48 ชม.</text>
 <rect x="522" y="10" width="208" height="30" rx="6" class="oksoft"/>
 <text x="626" y="30" text-anchor="middle" class="tb">Recovery</text>
 <path d="M70 330H730" class="ln"/>
 <path d="M70 330V50" class="ln"/>
 <text x="100" y="350" text-anchor="middle" class="t3">D1</text>
 <text x="175" y="350" text-anchor="middle" class="t3">D2</text>
 <text x="250" y="350" text-anchor="middle" class="t3">D3</text>
 <text x="325" y="350" text-anchor="middle" class="t3">D4</text>
 <text x="400" y="350" text-anchor="middle" class="t3">D5</text>
 <text x="475" y="350" text-anchor="middle" class="t3">D6</text>
 <text x="550" y="350" text-anchor="middle" class="t3">D7</text>
 <text x="625" y="350" text-anchor="middle" class="t3">D8</text>
 <text x="700" y="350" text-anchor="middle" class="t3">D9</text>
 <path d="M372 50V330" class="lnf"/>
 <path d="M522 50V330" class="lnf"/>
 <path d="M80 80C140 66 280 66 330 80C350 90 362 160 380 200C420 250 640 250 720 250" class="lnbad"/>
 <text x="96" y="64" class="t2">ไข้สูงลอย</text>
 <path d="M80 250C200 250 300 240 340 220C380 190 420 110 460 105C500 105 520 170 560 230C620 255 680 255 720 255" class="lnc1"/>
 <text x="430" y="96" class="ta">Hct ↑ ≥ 20% = plasma leakage</text>
 <path d="M80 150C180 160 250 200 320 250C370 290 420 305 470 305C540 300 620 220 720 170" class="lnc2"/>
 <text x="480" y="300" class="t2">Plt ต่ำสุด</text>
 <path d="M80 190C180 200 250 245 300 285C320 296 360 300 380 300" class="lnok"/>
 <text x="180" y="300" class="t3">WBC ↓ ≤ 5,000</text>
 <rect x="80" y="364" width="14" height="4" class="bad"/><text x="100" y="370" class="t3">ไข้</text>
 <rect x="150" y="364" width="14" height="4" class="c1"/><text x="170" y="370" class="t3">Hct</text>
 <rect x="220" y="364" width="14" height="4" class="c2"/><text x="240" y="370" class="t3">Platelet</text>
 <rect x="320" y="364" width="14" height="4" class="ok"/><text x="340" y="370" class="t3">WBC</text>
 <text x="410" y="370" class="t3">WBC ↓ + lymph ↑ + plt ↓ → ไข้จะลงใน 24 ชม.</text>
 <text x="70" y="392" class="t3">(กราฟแสดงแนวโน้มเชิงคุณภาพ ไม่ใช่ค่าจริง)</text>
</svg>''', "ไข้ลง = เข้าสู่ critical phase ที่ Hct พุ่งและ platelet ต่ำสุด · WBC ต่ำ + lymphocyte เพิ่ม + platelet ลด บอกว่าไข้จะลงภายใน 24 ชม.")

S1 = sec("id-02-01", "Dengue: classification, phases & diagnosis",
    "DEN-1–4 ยุงลาย · DF/DHF I–IV/EDS · WBC ≤ 5,000, plt ≤ 100,000, Hct ↑ ≥ 20% · NS1 ≤ 5 วัน, IgM/IgG > 5 วัน",
    minutes=9, source=f"{D} หน้า 54–65, 73–80", nl=["2.3.1(2)", "B1.5.3(6)"],
    md='''
### เชื้อและการติดต่อ

- **Dengue virus 4 serotype (DEN-1, 2, 3, 4)** · ยุงลาย **Aedes spp.**
- ติดเชื้อครั้งที่สอง **ต่าง serotype** จากครั้งแรก → อาการอาจรุนแรงกว่า (antibody-dependent enhancement (เสริม))

### Classification (WHO 1997/2011 ที่ไทยใช้ — สไลด์หน้า 55–59 เป็นภาพ สรุปเสริม)

| กลุ่ม | ลักษณะ |
|---|---|
| Dengue fever (DF) | ไข้สูง + ≥ 2 อาการ: ปวดหัว ปวดกระบอกตา ปวดเมื่อย ปวดข้อ ผื่น เลือดออก (tourniquet +) leukopenia (เสริม) |
| **DHF grade I** | **Tourniquet test positive** เป็นอาการเลือดออกอย่างเดียว |
| **DHF grade II** | **Spontaneous bleeding** (จุดเลือด เลือดกำเดา อาเจียนเป็นเลือด) |
| **DSS = DHF grade III** | ช็อก **วัด BP, PR ได้** (pulse pressure แคบ ≤ 20 mmHg หรือ BP ต่ำ) |
| **DSS = DHF grade IV** | **วัด BP, PR ไม่ได้** (profound shock) |
| Expanded dengue syndrome (EDS) | organ involvement ผิดปกติ เช่น encephalopathy, hepatitis/liver failure, myocarditis, AKI (เสริม) |

**เกณฑ์ DHF** (สไลด์หน้า 74): ไข้สูง + อาการเลือดออก (petechiae/tourniquet +) + ตับโต + **platelet ≤ 100,000** + **หลักฐาน plasma leakage (Hct ↑ ≥ 20%)**

### สามระยะ (ไม่จำเป็นต้องครบทุกระยะ — บางคนเป็นแค่ febrile phase แล้วหาย)

[[fig:id-02-01-f1]]

| ระยะ | ช่วง | สิ่งที่ต้องดู |
|---|---|---|
| Febrile | วัน 1–4/5 | ไข้สูงลอย หน้าแดง ปวดเมื่อย tourniquet + · **WBC เริ่มลด ↑lymphocyte ↓platelet → ไข้จะลงใน 24 ชม.** |
| **Critical** | **24–48 ชม.รอบไข้ลง** | plasma leakage → Hct ↑, pleural effusion (ฟังได้ crepitation/rhonchi ด้านขวา), ascites → shock |
| Recovery | หลังจากนั้น | ของเหลวกลับเข้าหลอดเลือด · **convalescent rash "white islands in a sea of red"** · หัวใจช้า · **ระวัง volume overload** |

### Investigation

- **CBC**: **WBC ≤ 5,000** with **atypical lymphocyte** · Hct ↑ 5–10% · **platelet ≤ 150,000** (DHF ≤ 100,000)
- **Evidence of plasma leakage**: **Hct ↑ ≥ 20%** จาก baseline · CXR **pleural effusion** · U/S **ascites, gallbladder wall thickening** · **albumin ≤ 3.5 g/dL** (≤ 4 ในคนอ้วน)
- **Confirmatory test**: **≤ 5 วัน → NS1 antigen** · **> 5 วัน → dengue IgM & IgG**
- Tourniquet test: วัด BP กลาง inflate ค้าง 5 นาที → petechiae ≥ 10 จุด/ตร.นิ้ว = positive (เสริม)

### Warning signs (สไลด์หน้า 64 เป็นภาพ — สรุปตามแนวทาง WHO/กรมการแพทย์ (เสริม))

- ไข้ลงแต่อาการแย่ลง · อาเจียนมาก กินไม่ได้ · **ปวดท้องมาก/กดเจ็บตับ**
- ซึม กระสับกระส่าย พฤติกรรมเปลี่ยน · **เลือดออก** (อาเจียน/ถ่ายดำ ประจำเดือนมาก)
- ตัวเย็นชื้น ตัวลาย · **ปัสสาวะน้อย/ไม่ออก 4–6 ชม.** · Hct เพิ่มร่วมกับ platelet ลดเร็ว

### Admission criteria (สไลด์หน้า 65 เป็นภาพ — (เสริม))

- มี warning sign หรือ shock · เลือดออกผิดปกติ · Hct ↑ ≥ 10–20% ร่วมกับ platelet ≤ 100,000
- กลุ่มเสี่ยง: หญิงตั้งครรภ์ ผู้สูงอายุ อ้วน โรคประจำตัว (DM, HT, หัวใจ ไต ตับ, thalassemia) · อยู่คนเดียว/บ้านไกล

> Dengue → **WBC ต่ำ + plt ต่ำ + Hct สูง** · Lepto → WBC สูง PMN เด่น · Scrub → eschar · คนไข้อยู่กรุงเทพฯ ไม่ได้เดินทาง ไข้ 7 วัน → ส่ง **dengue IgM/IgG** (ไม่ใช่ NS1)
''',
    figs=[F_PHASE],
    pearls=[
        "DHF I tourniquet + · II spontaneous bleed · III (DSS) วัด BP ได้ · IV วัดไม่ได้",
        "Plasma leakage = Hct ↑ ≥ 20%, effusion/ascites/GB wall thick, albumin ≤ 3.5",
        "NS1 ≤ 5 วัน · IgM/IgG > 5 วัน",
        "WBC ↓ + lymph ↑ + plt ↓ → ไข้จะลงใน 24 ชม. = เข้า critical phase",
        "Recovery: white islands in a sea of red + ระวัง fluid overload",
    ],
    items=[
        mcq("ID-02-01-1",
            "A 20-year-old man has had high fever for 5 days with headache and nausea. Temperature 39.5 °C, PR 90 bpm, BP 120/90 mmHg. He has mild conjunctival injection, no jaundice, a liver palpable 1 fingerbreadth below the costal margin and petechiae on the extremities. Hct 45%, WBC 4,300/mm3 (N 50%, L 40%, M 3%, atypical lymphocytes 7%), platelets 60,000/mm3. What is the most likely diagnosis?",
            "Dengue infection",
            ["Leptospirosis", "Scrub typhus", "Malaria", "Enteric fever"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไข้สูง + **petechiae** + **ตับโต** + **WBC ต่ำ มี atypical lymphocyte** + **platelet ≤ 100,000** = **dengue infection** (เข้าเกณฑ์ DHF ถ้ามี Hct ↑ ≥ 20%)
- Leptospirosis มัก WBC สูง PMN เด่น ร่วมกับปวดน่องและ AKI/เหลือง
- Scrub typhus ต้องมีประวัติเข้าป่าและ eschar
- Malaria ต้องมีประวัติเดินทางพื้นที่ระบาด และตรวจ blood film
- Enteric fever ไม่ทำให้ petechiae และเกล็ดเลือดต่ำขนาดนี้''',
            pearl="ไข้ + petechiae + WBC ต่ำ + plt ≤ 100k = dengue", topic="Dengue diagnosis",
            ref=[f"{D} หน้า 73–74"], nl=["2.3.1(2)"]),
        mcq("ID-02-01-2",
            "A 35-year-old woman living in Bangkok has had fever and malaise for 7 days without specific organ symptoms or travel outside the city. Hb 12.5 g/dL, WBC 8,800/mm3 (N 70%, L 18%). Total bilirubin 3 mg/dL, direct bilirubin 1.2 mg/dL, AST 77 U/L, ALP 111 U/L. Which investigation is most appropriate?",
            "Dengue IgM and IgG",
            ["Anti-HBc", "IFA for leptospira", "IFA for scrub typhus", "Dengue NS1 antigen"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''อยู่กรุงเทพฯ ไม่ได้เดินทาง (ไม่มี exposure ของ lepto/scrub) ไข้ **7 วัน (> 5 วัน)** → ตรวจ **dengue IgM & IgG**
- NS1 antigen ใช้ช่วง **≤ 5 วัน** ของไข้ หลังจากนั้นผลลบปลอมได้
- Anti-HBc ใช้หา hepatitis B ซึ่งไม่ทำให้ไข้แบบนี้และ AST ขึ้นแค่ 77
- IFA for leptospira และ IFA for scrub typhus ไม่มีประวัติสัมผัสน้ำท่วมหรือเข้าป่า''',
            pearl="ไข้ > 5 วัน → dengue IgM/IgG แทน NS1", topic="Dengue serology timing",
            ref=[f"{D} หน้า 60, 77–78"], nl=["2.3.1(2)"]),
        mcq("ID-02-01-3",
            "A middle-aged patient has had fever and generalized malaise for 3 days. Temperature 39 °C, BP 120/70 mmHg, PR 100 bpm. The liver is palpable 1–2 cm below the costal margin and the spleen is not palpable. Hb 13 g/dL, Hct 40%, WBC 4,100/mm3 (PMN 45%, lymphocytes 40%, monocytes 10%), platelets 80,000/mm3. The peripheral smear shows atypical lymphocytes. What is the most appropriate investigation?",
            "Dengue NS1 antigen",
            ["Leptospirosis serology", "Nasopharyngeal swab for influenza", "EBV serology", "Blood cultures"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ตัวเลือกเดิมเป็น dengue serology)",
            explain='''ไข้ 3 วัน + WBC ต่ำ + platelet ต่ำ + atypical lymphocyte + ตับโต = dengue · ไข้ **≤ 5 วัน** → **NS1 antigen** (ในสไลด์เฉลยว่า dengue serology และระบุว่า ≤ 5 วันใช้ NS1)
- Leptospirosis serology ไม่มีประวัติสัมผัสน้ำ และ lepto WBC มักสูง
- Influenza มีอาการทางเดินหายใจเด่น ไม่ทำให้เกล็ดเลือดต่ำมาก
- EBV ทำให้ atypical lymphocyte ได้ แต่ต้องมี pharyngitis LN โต และ lymphocytosis
- Blood culture ใช้เมื่อสงสัย bacteremia''',
            pearl="ไข้ ≤ 5 วัน สงสัย dengue → NS1", topic="Dengue NS1",
            ref=[f"{D} หน้า 60, 79–80"], nl=["2.3.1(2)"]),
        mcq_ordered("ID-02-01-4",
            "A 25-year-old man with dengue is on day 5 of illness. His fever has just subsided. BP 100/86 mmHg, PR 118 bpm, capillary refill 3 seconds. He is alert. According to the WHO dengue classification used in Thailand, what is his grade?",
            ["DHF grade I", "DHF grade II", "DHF grade III", "DHF grade IV", "Expanded dengue syndrome"], 2,
            explain='''ไข้เพิ่งลง + **pulse pressure แคบ (14 mmHg)** + ชีพจรเร็ว CRT ช้า แต่ **ยังวัด BP และ PR ได้** = **DSS = DHF grade III**
- Grade I มีแค่ tourniquet test positive ไม่มีช็อก
- Grade II มี spontaneous bleeding แต่ไม่มีช็อก
- Grade IV ต้องวัด BP/PR ไม่ได้ (profound shock)
- Expanded dengue syndrome หมายถึงมีอวัยวะผิดปกติแบบไม่ปกติของโรค เช่น encephalopathy ตับวาย ซึ่งรายนี้ไม่มี''',
            pearl="DSS วัด BP ได้ = grade III · วัดไม่ได้ = grade IV", topic="DHF grading",
            ref=[f"{D} หน้า 57–58"], nl=["2.3.1(2)", "2.2.7"]),
    ])

# ---------------------------------------------------------------- 02-02 Dengue management
F_FLUID = fig("id-02-02-f1", "Dengue management ตามระยะ", '''<svg viewBox="0 0 740 330">
 <defs><marker id="id-02-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="230" height="300" rx="10" class="misssoft"/>
 <text x="125" y="36" text-anchor="middle" class="tb">Febrile phase (OPD)</text>
 <text x="22" y="66" class="t2">• Paracetamol</text>
 <text x="22" y="88" class="t2">• ห้าม NSAID / aspirin</text>
 <text x="22" y="110" class="t2">• ดื่มน้ำ เกลือแร่</text>
 <text x="22" y="132" class="t2">• งดอาหารสีแดง/ดำ</text>
 <text x="22" y="154" class="t2">• สอน warning sign</text>
 <text x="22" y="176" class="t2">• CBC ทุกวันตั้งแต่</text>
 <text x="34" y="196" class="t2">วันที่ 3 จนไข้ลง</text>
 <text x="22" y="236" class="t3">ไม่ต้องให้ antibiotic</text>
 <text x="22" y="256" class="t3">ไม่ต้องให้ steroid</text>
 <text x="22" y="276" class="t3">ไม่ให้ platelet ป้องกัน</text>
 <path d="M240 160H262" class="ln" marker-end="url(#id-02-02-a)"/>
 <rect x="264" y="10" width="230" height="300" rx="10" class="badsoft"/>
 <text x="379" y="36" text-anchor="middle" class="tb">Critical phase (admit)</text>
 <text x="276" y="66" class="t2">• IV isotonic (NSS/5%D/NSS)</text>
 <text x="276" y="88" class="t2">• Monitor V/S, Hct, UO</text>
 <text x="276" y="110" class="t2">• ปรับตาม Hct + V/S</text>
 <text x="276" y="140" class="tb">DSS (grade III–IV)</text>
 <text x="276" y="162" class="t2">5%D/NSS 500 mL</text>
 <text x="276" y="182" class="t2">ใน 1–2 ชม. (ผู้ใหญ่)</text>
 <text x="276" y="204" class="t3">ไม่ดีขึ้น → colloid (dextran)</text>
 <text x="276" y="226" class="t3">Hct ลงแต่ยังช็อก → เลือดออกใน</text>
 <text x="276" y="246" class="t3">→ ให้เลือด (เสริม)</text>
 <text x="276" y="276" class="t3">ให้น้ำ 24–48 ชม. แล้วหยุด</text>
 <path d="M494 160H516" class="ln" marker-end="url(#id-02-02-a)"/>
 <rect x="518" y="10" width="212" height="300" rx="10" class="oksoft"/>
 <text x="624" y="36" text-anchor="middle" class="tb">Recovery phase</text>
 <text x="530" y="66" class="t2">• หยุด/ลด IV fluid</text>
 <text x="530" y="88" class="t2">• ระวัง volume overload</text>
 <text x="542" y="108" class="t3">(effusion, หอบ, ความดันสูง)</text>
 <text x="530" y="130" class="t2">• Convalescent rash</text>
 <text x="542" y="150" class="t3">white islands in red sea</text>
 <text x="530" y="172" class="t2">• Bradycardia ได้</text>
 <text x="530" y="194" class="t2">• Hct ลดลงเอง</text>
 <text x="530" y="226" class="t3">overload → furosemide (เสริม)</text>
</svg>''', "ซ้ายไปขวาตามเวลา: OPD ดูแลตามอาการ → critical phase ให้ IV fluid แบบมีเป้า → recovery หยุดน้ำและเฝ้าระวังน้ำเกิน")

S2 = sec("id-02-02", "Dengue: management & prevention",
    "Febrile: PCM ห้าม NSAID CBC ทุกวันจาก D3 · critical: admit IV fluid monitor · DSS 5%D/NSS 500 mL ใน 1–2 ชม. · recovery: ระวัง overload",
    minutes=7, source=f"{D} หน้า 66–72, 81–86", nl=["2.3.1(2)", "2.2.7"],
    md='''
### Febrile phase — ดูแลแบบ OPD

- **Paracetamol** · **avoid NSAID/aspirin** (เลือดออก, Reye) · เช็ดตัว
- ดื่มน้ำ เกลือแร่ · **งดอาหารสีแดง/ดำ** (สับสนกับเลือดออก)
- **สอน warning sign** ให้กลับมาทันที
- ตั้งแต่ **AFI day 3 → CBC ทุกวันจนไข้ลง** (ดู WBC, platelet, Hct)

### Critical phase — admit

- **Admit + IV fluid** (isotonic: NSS, 5%D/NSS, LRS) · **monitor V/S, Hct, urine output** ถี่
- ปริมาณ (สไลด์หน้า 68 เป็นภาพ — (เสริม)): ประมาณ maintenance + 5% deficit ใน 24–48 ชม. ปรับตาม Hct, V/S, UO (ผู้ใหญ่เริ่ม 1.5–3 mL/kg/hr แล้วไต่ระดับ)
- **DSS (DHF grade III)**: **5%D/NSS 500 mL IV ใน 1–2 ชม.** (ตามสไลด์) แล้วลดลงเมื่อ V/S ดีขึ้น · grade IV ให้ bolus เร็วกว่านี้ (free flow) (เสริม)
- ไม่ดีขึ้นหลัง crystalloid → colloid (dextran-40) · **Hct ลดแต่ยังช็อก → นึกถึงเลือดออกภายใน → ให้เลือด** (เสริม)
- Rhonchi/crepitation ในผู้ป่วย dengue ช่วง critical = **pleural effusion จาก plasma leakage** (ไม่ใช่ปอดอักเสบ)

### Recovery phase

- ลด/หยุด IV fluid · **ระวัง volume overload!** (ของเหลวกลับเข้าหลอดเลือด)
- Convalescent rash: **white islands in a sea of red** · คันฝ่ามือฝ่าเท้า · ชีพจรช้า

### สิ่งที่ไม่ต้องทำ (กับดักข้อสอบ)

- **Antibiotic** (ceftriaxone, doxycycline) ไม่ช่วย ถ้าเป็น dengue ชัด
- **Steroid** ไม่มีประโยชน์
- **Prophylactic platelet transfusion** ไม่ทำ แม้ platelet ต่ำ ถ้าไม่มีเลือดออกรุนแรง (เสริม)
- **Dopamine** ไม่ใช่การรักษาแรกของ DSS เพราะช็อกเป็นแบบ hypovolemic → ให้น้ำก่อน

### Prevention

- ป้องกันยุงลายกัด **ทำลายแหล่งน้ำขัง** (ลดแหล่งเพาะพันธุ์) ทายากันยุง ติดมุ้งลวด
- **Dengue vaccine** (เช่น TAK-003/Qdenga 2 เข็มห่าง 3 เดือน · CYD-TDV เฉพาะคนที่เคยติดเชื้อแล้ว (เสริม))

[[fig:id-02-02-f1]]
''',
    figs=[F_FLUID],
    pearls=[
        "Dengue febrile: paracetamol ห้าม NSAID · CBC ทุกวันตั้งแต่วันที่ 3",
        "DSS = hypovolemic → 5%D/NSS 500 mL ใน 1–2 ชม. ไม่ใช่ dopamine",
        "Antibiotic/steroid/prophylactic platelet ไม่ช่วยใน dengue",
        "Rhonchi ในผู้ป่วย dengue = pleural effusion จาก plasma leakage",
        "Recovery phase ต้องลดน้ำ ระวัง volume overload",
    ],
    items=[
        mcq("ID-02-02-1",
            "An 18-year-old man has had fever, myalgia, nausea and vomiting for 4 days. Today he is drowsy. Temperature 36.5 °C, BP 80/50 mmHg, PR 120 bpm. Hct 58%, WBC 2,500/mm3 (N 12%, L 80%, M 6%, E 2%), platelets 35,000/mm3. What is the most appropriate management?",
            "Rapid intravenous isotonic crystalloid (5% D/NSS) infusion",
            ["Dopamine infusion", "Intravenous ceftriaxone", "Intravenous dexamethasone", "Platelet concentrate transfusion"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไข้เพิ่งลง + ช็อก (วัด BP ได้) + **Hct 58% (hemoconcentration)** + WBC และ platelet ต่ำ = **dengue shock syndrome (DHF grade III)** จาก plasma leakage → ให้ **5%D/NSS 500 mL IV ใน 1–2 ชม.** (NSS loading)
- Dopamine ไม่ใช่การรักษาแรกเพราะเป็น hypovolemic shock ต้องเติมน้ำก่อน
- Ceftriaxone ไม่มีบทบาท dengue เป็นไวรัส
- Dexamethasone ไม่มีประโยชน์ใน dengue shock
- Platelet concentrate ไม่แก้ช็อก และไม่ให้แบบป้องกันเมื่อไม่มีเลือดออกรุนแรง''',
            pearl="DSS → crystalloid bolus ก่อนเสมอ", topic="Dengue shock",
            ref=[f"{D} หน้า 83–84"], nl=["2.3.1(2)", "2.2.7"]),
        mcq("ID-02-02-2",
            "An 18-year-old woman has low-grade fever and generalized abdominal pain. She has a maculopapular rash and the liver is palpable 3 cm below the right costal margin. Hct 42%, WBC 2,700/mm3 with 10% atypical lymphocytes, platelets 90,000/mm3. Vital signs are stable. What is the most appropriate management?",
            "Fluid replacement therapy",
            ["Prednisolone", "Doxycycline", "Ceftriaxone", "Ciprofloxacin"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไข้ต่ำ ๆ (ใกล้ไข้ลง) + ปวดท้อง + ตับโต + WBC ต่ำมี atypical lymphocyte + platelet ต่ำ = **dengue** ที่ปวดท้อง (warning sign) → การรักษาหลักคือ **fluid replacement** และ monitor
- Prednisolone ไม่มีประโยชน์ใน dengue
- Doxycycline ใช้กับ lepto/rickettsia ซึ่ง WBC จะไม่ต่ำแบบนี้และไม่มี atypical lymphocyte เด่น
- Ceftriaxone และ ciprofloxacin ใช้กับแบคทีเรีย (typhoid/lepto) ไม่ช่วยในไวรัส dengue''',
            pearl="Dengue รักษาด้วยน้ำ ไม่ใช่ยาฆ่าเชื้อหรือ steroid", topic="Dengue fluid",
            ref=[f"{D} หน้า 67, 85–86"], nl=["2.3.1(2)"]),
        mcq("ID-02-02-3",
            "A 22-year-old woman admitted with dengue on day 6 of illness, one day after defervescence, develops mild tachypnea. Examination reveals decreased breath sounds and crepitations at the right lung base. Hct has risen from 38% to 47%. What is the most likely cause of the lung findings?",
            "Plasma leakage causing pleural effusion",
            ["Hypovolemic shock causing pulmonary edema", "Secondary bacterial pneumonia", "Pulmonary hemorrhage from thrombocytopenia", "Acute pulmonary embolism"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ขยายจากโจทย์สั้นในสไลด์)",
            explain='''ช่วง critical phase หลังไข้ลง + **Hct เพิ่ม ≥ 20%** + เสียงปอดลดที่ฐานขวา = **plasma leakage → pleural effusion** (หลักฐานของ leakage อย่างหนึ่ง)
- Hypovolemic shock เป็นผลของ leakage ไม่ได้ทำให้เกิดน้ำในปอด และรายนี้ยังไม่มีช็อก
- Secondary pneumonia ไม่เข้ากับช่วงเวลาและ Hct ที่สูงขึ้น
- Pulmonary hemorrhage พบใน lepto มากกว่า และจะมีไอเป็นเลือด Hct ลด
- Pulmonary embolism ไม่มีเหตุและไม่ทำให้ Hct สูง''',
            pearl="Dengue + เสียงปอดผิดปกติช่วง critical = effusion จาก leakage", topic="Plasma leakage",
            ref=[f"{D} หน้า 60, 81–82"], nl=["2.3.1(2)"]),
        mcq("ID-02-02-4",
            "A 28-year-old man with dengue was resuscitated for shock 2 days ago and has been on IV fluid since. His temperature is normal, he has a pruritic confluent erythematous rash with small islands of normal skin on the legs, and he now complains of dyspnea. BP 150/90 mmHg, PR 58 bpm, and there are bilateral crepitations. Hct is 36%. What is the most appropriate next step?",
            "Stop intravenous fluid and give a diuretic",
            ["Give a crystalloid bolus", "Transfuse packed red cells", "Start ceftriaxone for pneumonia", "Give platelet concentrate"],
            explain='''ผื่น **white islands in a sea of red** + bradycardia + Hct ลดลงเอง = **recovery phase** ที่ของเหลวกลับเข้าหลอดเลือด แต่ยังได้น้ำอยู่ → **volume overload** (หอบ ความดันสูง crepitation) → **หยุดน้ำ ± furosemide** (เสริม)
- Crystalloid bolus จะทำให้ปอดบวมน้ำหนักขึ้น
- PRC ใช้เมื่อ Hct ลดแต่ยังช็อก (เลือดออกภายใน) ซึ่งรายนี้ความดันสูง
- Ceftriaxone ไม่ช่วย ภาพเป็นน้ำเกินไม่ใช่ปอดอักเสบ
- Platelet ไม่เกี่ยวกับปัญหานี้''',
            pearl="Recovery phase + หอบ ความดันสูง = fluid overload → หยุดน้ำ", topic="Recovery phase",
            ref=[f"{D} หน้า 69"], nl=["2.3.1(2)"]),
    ])

# ---------------------------------------------------------------- 02-03 Chikungunya
S3 = sec("id-02-03", "Chikungunya",
    "ยุงลาย ภาคใต้ฤดูฝน · ไข้สูง + ปวดข้อเล็กสมมาตรแบบย้ายที่ + ผื่น · lymphopenia · RT-PCR < 6 วัน, IgM ≥ 6 วัน · paracetamol, เลี่ยง NSAID ช่วงไข้",
    minutes=5, source=f"{D} หน้า 87–93", nl=["2.3.1(2)", "B1.5.3(6)"],
    md='''
### เชื้อและการติดต่อ

- **Chikungunya virus** (alphavirus) · ยุงลาย **Aedes spp.** (เหมือน dengue)
- **พบบ่อยสุดภาคใต้ ฤดูฝน** · มักเป็นหลายคนในละแวกเดียวกัน

### อาการ

| ระยะ | อาการ |
|---|---|
| **Acute (1–2 wk)** | ไข้สูง ปวดหัว อ่อนเพลีย · **symmetrical, migratory polyarthralgia/arthritis** ข้อเล็ก (**นิ้ว ข้อมือ ข้อเท้า**) · **MP rash** · conjunctivitis, pharyngitis · encephalitis (ทารก/ผู้สูงอายุ) |
| **Chronic** | **ปวดข้อต่อเนื่องเป็นเดือน/ปี** |

### Investigation

- CBC: ↓WBC, **lymphopenia < 1,000/mm3**, ± atypical lymphocyte, ↓platelet (มักไม่ต่ำเท่า dengue (เสริม))
- **< 6 วัน: RT-PCR** for chikungunya RNA · **≥ 6 วัน: chikungunya IgM & IgG**

### Management

- **Supportive: paracetamol**, พัก, ประคบเย็น
- **Avoid NSAID ช่วงมีไข้** เพราะอาจแยกจาก dengue ไม่ได้ หรือติด dengue ร่วม
- Chronic arthralgia: NSAID หลังพ้นระยะไข้ · **HCQ / methotrexate** ในรายเรื้อรัง
- Prevention: ทำลายแหล่งน้ำขัง ทายากันยุง มุ้งลวด

| | Dengue | Chikungunya |
|---|---|---|
| เด่น | Plasma leakage, เลือดออก ช็อก | **ปวดข้อมาก บวม** |
| Platelet | ต่ำมาก | ต่ำเล็กน้อย |
| เรื้อรัง | ไม่มี | ปวดข้อเป็นเดือน–ปี |

> ไข้ + ผื่น + **ปวดข้อหลายข้อสมมาตร** + เพื่อนบ้านเป็นเหมือนกัน (ภาคใต้) = chikungunya
''',
    pearls=[
        "Chik: ไข้สูง + polyarthralgia สมมาตรข้อเล็กแบบย้ายที่ + ผื่น",
        "ภาคใต้ ฤดูฝน ยุงลาย · มักเป็นหลายคนในหมู่บ้าน",
        "RT-PCR < 6 วัน · IgM/IgG ≥ 6 วัน",
        "Paracetamol · เลี่ยง NSAID ช่วงไข้ (อาจเป็น dengue) · เรื้อรัง HCQ/MTX",
    ],
    items=[
        mcq("ID-02-03-1",
            "A 40-year-old man from Narathiwat had fever for 4 days followed by a rash. Two days later he developed pain in both knees, and today pain in both ankles and elbows. Temperature 40 °C, BP 100/80 mmHg. There is a maculopapular rash on the trunk and extremities, and both knees, ankles and elbows are swollen, warm and tender with limited motion. Hct 40%, WBC 3,500/mm3 (N 45%, L 50%, atypical lymphocytes 5%), platelets 45,000/mm3. What is the most likely diagnosis?",
            "Chikungunya infection",
            ["Rickettsial infection", "Acute gouty arthritis", "Acute rheumatoid arthritis", "Disseminated gonococcal arthritis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ภาคใต้ (นราธิวาส) + ไข้สูง + ผื่น + **polyarthritis สมมาตรแบบย้ายที่** + WBC ต่ำ = **chikungunya**
- Rickettsial infection ไม่มีข้ออักเสบเด่น และต้องมีประวัติเข้าป่า/eschar
- Gout มักข้อเดียว ไม่มีผื่น WBC ไม่ต่ำ
- RA เป็นเรื้อรังหลายสัปดาห์ ไม่ใช่ไข้ 40 °C ร่วมผื่นเฉียบพลัน
- DGI มี tenosynovitis + pustular skin lesion ในคนที่มีเพศสัมพันธ์เสี่ยง และ WBC ไม่ต่ำ''',
            pearl="ไข้ + ผื่น + ปวดข้อสมมาตรหลายข้อ ภาคใต้ = chikungunya", topic="Chikungunya diagnosis",
            ref=[f"{D} หน้า 87, 90–91"], nl=["2.3.1(2)"]),
        mcq("ID-02-03-2",
            "A patient presents with fever for 3 days, multiple joint pain and rash. His neighbor had the same illness last week. What is the most likely diagnosis?",
            "Chikungunya",
            ["Rubella", "Scrub typhus", "Reactive arthritis", "Leptospirosis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ไข้ + ผื่น + **ปวดหลายข้อ** + **เพื่อนบ้านเป็นเหมือนกัน** (ยุงลายในชุมชน) = **chikungunya** — รักษาแบบ supportive
- Rubella ทำให้ไข้ผื่นและปวดข้อได้ แต่มักมี postauricular LN และปวดข้อไม่เด่นเท่า ในข้อสอบ NL ภาพนี้ตั้งใจให้ตอบ chik
- Scrub typhus ไม่มี polyarthritis และต้องเข้าป่า
- Reactive arthritis เกิดหลังติดเชื้อทางเดินอาหาร/ปัสสาวะ 1–4 สัปดาห์ ไม่ใช่ไข้ผื่นพร้อมกันในชุมชน
- Leptospirosis เด่นที่ปวดน่องไม่ใช่ข้อ''',
            pearl="ไข้ ผื่น ปวดข้อ + คนรอบข้างเป็น = chikungunya", topic="Chikungunya cluster",
            ref=[f"{D} หน้า 92–93"], nl=["2.3.1(2)"]),
        mcq("ID-02-03-3",
            "A 34-year-old woman from Songkhla has had fever for 2 days with severe pain in her fingers and wrists bilaterally and a faint rash. Platelets are 120,000/mm3 and lymphocytes 800/mm3. Dengue cannot yet be excluded. Which is the most appropriate analgesic?",
            "Paracetamol",
            ["Ibuprofen", "Aspirin", "Prednisolone", "Hydroxychloroquine"],
            explain='''สงสัย chikungunya ระยะไข้ แต่ **ยังแยก dengue ไม่ได้** → ใช้ **paracetamol** · **เลี่ยง NSAID** ช่วงมีไข้
- Ibuprofen และ aspirin เป็น NSAID/antiplatelet เพิ่มเลือดออกถ้าเป็น dengue
- Prednisolone ไม่ใช้ในระยะ acute
- Hydroxychloroquine ใช้ใน chronic chikungunya arthralgia ไม่ใช่ระยะไข้ 2 วัน''',
            pearl="Chik ระยะไข้ → paracetamol ห้าม NSAID จนกว่าจะแยก dengue", topic="Chikungunya treatment",
            ref=[f"{D} หน้า 88–89"], nl=["2.3.1(2)"]),
    ])

# ---------------------------------------------------------------- 02-04 IM
S4 = sec("id-02-04", "Infectious mononucleosis (EBV)",
    "EBV/CMV ผ่านน้ำลาย · ไข้ + pharyngitis + LN คอหน้า/หลัง + HSM · atypical lymphocyte · VCA IgM / Monospot · ผื่นหลัง amoxicillin · งดกระแทก 3 สัปดาห์",
    minutes=7, source=f"{D} หน้า 94–107", nl=["2.3.1(10)", "2.1.57"],
    md='''
### เชื้อและการติดต่อ

- **Epstein-Barr virus (EBV)** (ส่วนน้อย CMV)
- ผ่านสารคัดหลั่ง โดยเฉพาะ **น้ำลาย** (kissing disease) · วัยรุ่น–ผู้ใหญ่ตอนต้น

### อาการ (classic triad: ไข้ + pharyngitis + LN)

- Fever · **pharyngitis/tonsillitis** (มี exudate ได้)
- **Cervical lymphadenopathy ทั้ง anterior และ posterior** (posterior เป็น clue)
- Fatigue, headache, malaise · **palatal petechiae** · periorbital edema
- **Hepatosplenomegaly**
- **MP rash มักเกิดหลังกิน amoxicillin/ampicillin** — มักเข้าใจผิดว่าแพ้ยา

### Investigation

- PBS: **lymphocytosis, atypical lymphocytes**
- **EBV serology (gold standard)**: **anti-VCA IgM** (acute) & IgG · **anti-EBNA IgG ขึ้นช้า 6–12 wk** จึงบอก acute infection ไม่ได้ (ถ้า EBNA + แปลว่าติดมานานแล้ว)
- **Heterophile antibody (Monospot test)** — ตรวจง่าย เร็ว · **false negative บ่อยในเด็ก < 5 ปี** และสัปดาห์แรก
- LFT: transaminase ขึ้นเล็กน้อย (เสริม)

### Complications

- **Splenic rupture** · **upper airway obstruction** (ต่อมทอนซิลโตมาก)
- AIHA (cold agglutinin), thrombocytopenia
- Oral hairy leukoplakia (ใน immunocompromised)
- Associated cancer: **lymphoma (Burkitt, Hodgkin), nasopharyngeal carcinoma**

### Management

- **Supportive**: hydration, **paracetamol**
- **Avoid trauma/contact sport ≥ 3 สัปดาห์** ป้องกัน splenic rupture
- **Steroid เฉพาะมี complication**: upper airway obstruction, AIHA, severe thrombocytopenia, marked splenomegaly
- **Antibiotic ไม่ช่วย** (amoxicillin ทำให้ผื่น) · acyclovir ไม่แนะนำ (เสริม)
- Prevention: เลี่ยงสารคัดหลั่ง/น้ำลายของผู้ป่วย ไม่จูบ ไม่ใช้แก้วน้ำ/แปรงสีฟันร่วม

### Differential diagnosis ของเจ็บคอ + ไข้

| | IM | Diphtheria | Strep group A tonsillitis |
|---|---|---|---|
| คอ | Exudate ขาว ลอกออกได้ | **Grayish-white pseudomembrane เลยออกนอก tonsil** ขูดแล้วเลือดออก | Exudate, palatal petechiae (doughnut lesion) |
| LN | **Anterior + posterior** | Bull neck | **Anterior เท่านั้น** |
| HSM | **มี** | ไม่มี | **ไม่มี** |
| อื่น ๆ | Atypical lymph, ผื่นหลัง amoxicillin | ไม่ได้รับวัคซีน, myocarditis | ไข้สูง ไม่ไอ |

> Acute retroviral syndrome (HIV) เป็น mono-like ได้ แต่เด่น oral ulcer, ผื่น, LN ทั่วตัว และมีประวัติเสี่ยง
''',
    pearls=[
        "IM: ไข้ + pharyngitis + LN คอหน้าและหลัง + HSM + atypical lymphocyte",
        "ผื่นหลัง amoxicillin ใน IM ไม่ใช่การแพ้ยาจริง",
        "Monospot (heterophile) เร็ว แต่ลบปลอมในเด็ก < 5 ปี · anti-VCA IgM = acute",
        "งดกีฬาปะทะ ≥ 3 สัปดาห์ (splenic rupture) · steroid เฉพาะ airway obstruction/AIHA/ITP",
        "Strep: LN คอหน้าอย่างเดียว ไม่มี HSM",
    ],
    items=[
        mcq("ID-02-04-1",
            "A young woman has low-grade fever and sore throat. Temperature 38 °C. She has an injected pharynx with enlarged exudative tonsils, cervical lymphadenopathy, and a tender enlarged liver and spleen. What is the most likely diagnosis?",
            "Infectious mononucleosis",
            ["Diphtheria", "Acute HIV infection", "Rubella", "Scarlet fever"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''เจ็บคอ + tonsil exudate + LN คอ + **ตับม้ามโต** = **infectious mononucleosis**
- Diphtheria มี grayish pseudomembrane ขูดแล้วเลือดออก และไม่มี HSM
- Acute HIV ทำ mono-like ได้ แต่ไม่มีประวัติเสี่ยงและมักมีผื่น oral ulcer
- Rubella มีผื่นเด่น postauricular LN ไม่ใช่ tonsil exudate กับ HSM
- Scarlet fever มีผื่น sandpaper และ strawberry tongue ไม่มี HSM''',
            pearl="Pharyngitis + HSM = IM", topic="IM diagnosis",
            ref=[f"{D} หน้า 95, 100–101"], nl=["2.3.1(10)"]),
        mcq("ID-02-04-2",
            "A 25-year-old man has had fever and sore throat for 5 days. Temperature 38.3 °C. There are grey exudative tonsillar patches, hepatosplenomegaly, a discrete maculopapular rash all over the body and generalized lymphadenopathy. Hb 13 g/dL, WBC 4,700/mm3 (N 22%, L 58%, M 20%), platelets 200,000/mm3. What is the most likely diagnosis?",
            "Infectious mononucleosis",
            ["Diphtheria", "Scarlet fever", "Scrub typhus", "Acute retroviral syndrome"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (เฉลยในสไลด์ = IM)",
            explain='''ไข้ + tonsillitis มี exudate + **HSM** + LN + **lymphocytosis (L 58%, M 20%)** = **infectious mononucleosis** (สไลด์เฉลยไว้) — ผื่นอาจเป็นผื่นของโรคเองหรือหลังได้ amoxicillin
- Diphtheria pseudomembrane ขูดแล้วเลือดออก ไม่มี HSM และ lymphocytosis
- Scarlet fever มี neutrophilia ไม่มี HSM
- Scrub typhus ต้องมี eschar ประวัติเข้าป่า และไม่มี tonsillitis
- Acute retroviral syndrome เป็น mono-like ที่ต้องคิดถึงเสมอในคนมีความเสี่ยง (ควรตรวจ anti-HIV ร่วมด้วยในชีวิตจริง) แต่ HSM + tonsil exudate + lymphocytosis เป็น classic IM''',
            pearl="IM: lymphocytosis + tonsil exudate + HSM", topic="IM vs mimics",
            ref=[f"{D} หน้า 102–103"], nl=["2.3.1(10)"]),
        mcq("ID-02-04-3",
            "A 19-year-old student has fever, exudative pharyngitis, posterior cervical lymphadenopathy and splenomegaly. Peripheral smear shows atypical lymphocytes. Which test is the most appropriate rapid confirmatory test?",
            "Heterophile antibody (Monospot) test",
            ["Cold agglutinin titer", "EBV early antigen antibody", "Anti-EBNA IgG", "Throat culture for diphtheria"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ภาพ IM ชัดในวัยรุ่น → ตรวจยืนยันเร็วด้วย **heterophile antibody (Monospot)** (หรือ anti-VCA IgM ถ้าทำได้)
- Cold agglutinin ใช้กับ Mycoplasma pneumoniae (และเป็น complication AIHA ของ IM) ไม่ใช่ test วินิจฉัย
- EBV early antigen ไม่ใช่ test มาตรฐานในการวินิจฉัย acute IM
- Anti-EBNA ขึ้นช้า 6–12 สัปดาห์ จึงบอก acute infection ไม่ได้
- Throat culture for diphtheria ไม่เข้ากับ HSM และ atypical lymphocyte''',
            pearl="IM → Monospot หรือ anti-VCA IgM · EBNA ขึ้นช้า", topic="IM serology",
            ref=[f"{D} หน้า 96, 104–105"], nl=["2.3.1(10)"]),
        mcq("ID-02-04-4",
            "A 20-year-old college rugby player is diagnosed with infectious mononucleosis. He has mild tonsillar enlargement without stridor, and the spleen is palpable 2 cm below the costal margin. He asks about returning to play. What is the most appropriate advice?",
            "Avoid contact sports for at least 3 weeks",
            ["Start amoxicillin and return when afebrile", "Start prednisolone to shorten the illness", "Return to play immediately as the spleen is only mildly enlarged", "Start oral acyclovir and return after 5 days"],
            explain='''IM มีความเสี่ยง **splenic rupture** → **งดกีฬาปะทะ/การกระแทกอย่างน้อย 3 สัปดาห์** (หลายแนวทางให้ 3–4 สัปดาห์หรือจนม้ามยุบ (เสริม)) + supportive
- Amoxicillin ไม่ได้ผลกับไวรัสและมักทำให้เกิดผื่น
- Prednisolone ใช้เฉพาะเมื่อมี complication (airway obstruction, AIHA, thrombocytopenia รุนแรง) ซึ่งรายนี้ไม่มี
- ม้ามโตเล็กน้อยก็แตกได้ จึงไม่ควรกลับไปเล่นทันที
- Acyclovir ไม่แนะนำใน IM และไม่ลดความเสี่ยงม้ามแตก''',
            pearl="IM → งดกีฬาปะทะ ≥ 3 สัปดาห์", topic="IM management",
            ref=[f"{D} หน้า 97–98"], nl=["2.3.1(10)"]),
    ])

LECTURE = lecture("02", "Arboviral fever & mononucleosis",
    "Dengue · chikungunya · infectious mononucleosis",
    objectives=[
        "จัด grade DF/DHF/DSS และระบุระยะของ dengue จาก V/S + CBC ได้",
        "เลือก NS1 หรือ IgM/IgG ตามวันไข้ และรู้ warning sign/admission criteria",
        "ให้สารน้ำใน DSS และระวัง fluid overload ใน recovery phase ได้",
        "แยก chikungunya และ IM จาก dengue/โรคเจ็บคออื่น และให้คำแนะนำที่ถูกต้อง",
    ],
    sections=[S1, S2, S3, S4])
