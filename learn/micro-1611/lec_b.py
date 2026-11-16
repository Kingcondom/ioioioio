# -*- coding: utf-8 -*-
# เนื้อหาคาบ 16/11 — ส่วนที่ 2 (รา ผื่น mycobacteria ปรสิต มาลาเรีย)
from lec_a import im, imc, S

# ---------------------------------------------------------------- 8
S.append(dict(
 id="id-mic-08", title="เชื้อรา: Cryptococcus, Candida, Mucor, Aspergillus, Histoplasma กับ Talaromyces",
 summary="ยีสต์มีแคปซูล = Cryptococcus → AmB + flucytosine แล้ว fluconazole · สายไม่มีผนังกั้น มุมกว้าง = Mucor (DKA) · มีผนังกั้น 45° = Aspergillus (neutropenia) · ยีสต์ใน macrophage: budding = Histo · septum ตรงกลาง = Talaromyces → AmB แล้ว itraconazole",
 minutes=11, nl=["2.3.1-3(7)", "B1.5.4(1)", "B1.5.4(2)", "B3.3(2)", "2.3.1(9)"],
 md="""### จัดกลุ่มเชื้อราจากสไลด์
| กลุ่ม | ลักษณะ | เชื้อ |
|---|---|---|
| **Yeast** | เซลล์กลมแตกหน่อ | *Candida* (มี **pseudohyphae**) · ***Cryptococcus neoformans*** (มี **แคปซูล**) · *Trichosporon* |
| **Aseptate hyphae** | สายใหญ่ **ไม่มีผนังกั้น** | **Mucorales**: *Rhizopus*, *Mucor*, *Rhizomucor* |
| **Septate hyaline** | สายใส **มีผนังกั้น** | ***Aspergillus***, *Fusarium* · dermatophytes |
| **Dematiaceous** | สายมีสีคล้ำ | *Bipolaris*, *Alternaria*, *Exophiala* |
| **Dimorphic** | ราในธรรมชาติ ยีสต์ในร่างกาย | ***Histoplasma***, ***Talaromyces marneffei***, *Coccidioides*, *Blastomyces* |

### *Cryptococcus neoformans*
[[img:mic-crypto-yeast]]
- **round budding yeast with capsule** — ช่องใสรอบตัว · **India ink** · **CrAg** ในเลือด/CSF
- HIV **CD4 < 100** → **meningitis** (ICP สูงมาก) · ผิวหนังเป็น **ตุ่มบุ๋มคล้าย molluscum**
- **ยา (induction → consolidation → maintenance)**
  1. **amphotericin B IV + flucytosine กิน 2 สัปดาห์**
  2. **fluconazole 800 mg/วัน 8 สัปดาห์**
  3. fluconazole 200 mg/วัน จน CD4 > 100 นานพอ
- **WHO 2022**: liposomal AmB **10 mg/kg ครั้งเดียว** + flucytosine + fluconazole 14 วัน (ใช้เมื่อมียา)
- **เจาะ LP ระบายความดัน** ซ้ำถ้า opening pressure > 25 · **เลื่อนเริ่ม ART 4–6 สัปดาห์** (กัน IRIS)

> **ผู้สอน:** จำขนาดไม่ได้ให้เขียน **ชื่อยาให้ถูกก่อน** — ยาคู่กับ amphotericin คือ **flucytosine ไม่ใช่ fluconazole**

[[img:mic-candida]]

### Mucormycosis (*Rhizopus/Mucor*)
[[img:mic-mucor-face]]
[[img:mic-mucor-hyphae]]
- **broad, ribbon-like hyphae** · **แตกแขนงมุมกว้าง (~90°)** · **ผนังกั้นน้อยหรือไม่มี**
- **เบาหวานที่มี DKA** · ได้ deferoxamine · ปลูกถ่ายอวัยวะ · มะเร็งเม็ดเลือด · neutropenia · steroid
- **rhinocerebral** (พบบ่อยสุด): เข้าหลอดเลือด → thrombosis → **เนื้อตายดำที่เพดานปาก โพรงจมูก ใบหน้า**
- ยา: **liposomal amphotericin B + ผ่าตัดเนื้อตายออก + แก้ DKA** (ผู้สอน: ง่าย ไม่ค่อยถาม)

### Aspergillosis
[[img:mic-asperg]]
- **septate hyphae** · **แตกแขนงสองแฉกมุมแหลม ~45° (dichotomous)**
- **invasive aspergillosis** ใน **febrile neutropenia / leukemia** (halo sign ใน CT) · aspergilloma ในโพรงเก่า · ABPA ในหืด
- ยา invasive: **voriconazole**

### ยีสต์ใน macrophage — Histoplasma หรือ Talaromyces
[[img:mic-dimorph-a]]
[[img:mic-dimorph-b]]

| | ***Histoplasma capsulatum*** | ***Talaromyces marneffei*** |
|---|---|---|
| รูป | **ยีสต์เล็กแตกหน่อ (budding)** | ยีสต์รี/ยาว มี **ผนังกั้นกลางเซลล์ (transverse septum)** แบ่งตัวแบบ **binary fission** |
| คลินิก | HIV CD4 < 150 · ไข้ ตับม้ามโต **pancytopenia** · ผื่นตุ่มบุ๋ม | HIV CD4 < 100 · ไข้ ซีด **ตุ่มบุ๋มตรงกลาง (umbilicated)** ที่หน้า · ภาคเหนือ |
| ยา | **amphotericin B ~2 สัปดาห์ → itraconazole** (รวม ~10–12 สัปดาห์ แล้ว 200 mg/วันป้องกันซ้ำ) | เช่นเดียวกัน |

> **ไม่ใช้ fluconazole** กับ histo/talaro — ฤทธิ์ต่ำ (ผู้สอน: ช่วงหลังออกน้อยลงแต่ต้องตอบได้)""",
 pearls=["Crypto: capsule · India ink/CrAg · AmB + flucytosine 2 wk → fluconazole 8 wk · LP ลดความดัน", "Flucytosine ≠ fluconazole", "Mucor: สายกว้างไม่มีผนังกั้น 90° · DKA · เนื้อตายดำ → L-AmB + ผ่าตัด", "Aspergillus: มีผนังกั้น 45° · neutropenia → voriconazole", "Histo budding · Talaro septum → AmB → itraconazole (ไม่ใช่ fluconazole)"],
 imgs=dict([
  im("mic-crypto-yeast", "Cryptococcus ในสไลด์", "เซลล์ยีสต์กลมหลายตัวมีวงใสล้อมรอบ ปนเม็ดเลือดขาว",
     "ยีสต์กลมมีวงใสล้อมรอบ ในผู้ป่วย HIV ปวดศีรษะ 3 สัปดาห์ — คือเชื้ออะไร ย้อมอะไรยืนยัน",
     "***Cryptococcus neoformans*** — **round budding yeast with capsule** · ยืนยันด้วย **India ink** (แคปซูลใสบนพื้นดำ) หรือ **CrAg** · รักษา **amphotericin B + flucytosine → fluconazole**"),
  imc("mic-candida", "Candida — budding yeast with pseudohyphae", "เซลล์ยีสต์รีเกาะตามเส้นสายแตกกิ่งสีม่วงบนเซลล์เยื่อบุ",
      "**ยีสต์แตกหน่อ + pseudohyphae** = *Candida* — oral thrush, esophagitis (HIV), candidemia จากสายสวน"),
  imc("mic-mucor-face", "Rhinocerebral mucormycosis", "ใบหน้าผู้ป่วยมีเนื้อตายสีดำรอบตาและจมูกด้านหนึ่ง",
      "**เนื้อตายดำที่ใบหน้า จมูก รอบตา** ในผู้ป่วยเบาหวาน DKA = rhinocerebral mucormycosis → ผ่าตัดเนื้อตาย + liposomal AmB"),
  im("mic-mucor-hyphae", "Mucor — ชิ้นเนื้อ", "เส้นสายราขนาดใหญ่ แบน ไม่มีผนังกั้น แตกแขนงมุมกว้าง บนพื้นชมพู",
     "ชิ้นเนื้อจากเพดานปากผู้ป่วย DKA — บรรยายลักษณะเชื้อ",
     "**broad, ribbon-like, aseptate (pauciseptate) hyphae** แตกแขนง **มุมกว้าง ~90°** = **Mucorales** (*Rhizopus/Mucor*)"),
  im("mic-asperg", "Aspergillus — ชิ้นเนื้อ", "เส้นสายราบางขนาดเท่ากัน มีผนังกั้น แตกแขนงเป็นมุมแหลม",
     "ผู้ป่วย AML ไข้ไม่ลงระหว่าง neutropenia — บรรยายลักษณะเชื้อ วินิจฉัย และรักษา",
     "**septate hyphae** ขนาดสม่ำเสมอ แตกแขนง **สองแฉกมุมแหลม ~45°** = **invasive aspergillosis** (*Aspergillus*) → **voriconazole**"),
  im("mic-dimorph-a", "ยีสต์ใน macrophage (1)", "macrophage สองเซลล์มียีสต์เล็กกลมจำนวนมากอยู่ภายใน มีวงใสรอบแต่ละตัว",
     "ผู้ป่วย HIV ไข้ pancytopenia — ยีสต์เล็กใน macrophage ภาพนี้คือเชื้อใด",
     "**small budding yeasts within macrophages** = ***Histoplasma capsulatum*** · รักษา **amphotericin B แล้วต่อ itraconazole**"),
  im("mic-dimorph-b", "ยีสต์ใน macrophage (2)", "macrophage มียีสต์รูปรีจำนวนมาก บางตัวมีเส้นกั้นกลางเซลล์",
     "ผู้ป่วย HIV ตุ่มบุ๋มที่หน้า ไข้ ซีด — ยีสต์ในภาพนี้ต่างจากภาพก่อนอย่างไร",
     "**oval/elongated yeast-like cells with a central (transverse) septum** แบ่งตัวแบบ binary fission = ***Talaromyces marneffei*** · รักษา **amphotericin B ~2 สัปดาห์ → itraconazole** (ไม่ใช้ fluconazole)"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-16", topic="Induction therapy for cryptococcal meningitis",
   stem="A 29-year-old man with newly diagnosed HIV (CD4 40 cells/µL) has cryptococcal meningitis with an opening pressure of 34 cmH2O. Which induction regimen is preferred, and when should antiretroviral therapy start?",
   choices=["Amphotericin B plus flucytosine; start ART 4–6 weeks after antifungal therapy", "Amphotericin B plus fluconazole 200 mg; start ART immediately", "Fluconazole 200 mg alone; start ART after 6 months", "Flucytosine alone; start ART in 2 weeks", "Itraconazole; start ART immediately"],
   explain="Induction = **amphotericin B + flucytosine (2 สัปดาห์)** → fluconazole 800 mg 8 สัปดาห์ → 200 mg maintenance · **เลื่อน ART 4–6 สัปดาห์** เพราะเริ่มเร็วเพิ่มอัตราตายจาก IRIS · และต้อง **LP ซ้ำลดความดัน**\n\n- fluconazole 200 mg เป็นขนาด maintenance\n- flucytosine เดี่ยวดื้อยาเร็ว\n- itraconazole ใช้กับ histo/talaro",
   pearl="Crypto: AmB + 5-FC · ART หลัง 4–6 สัปดาห์", ref=["สไลด์ Microorganism 2026 — Cryptococcosis", "WHO. Guidelines for diagnosing, preventing and managing cryptococcal disease (2022)"], nl=["2.3.1-3(7)", "2.3.1(9)"]),
  dict(id="ID-MIC-MCQ-17", topic="Talaromyces vs Histoplasma",
   stem="A bone-marrow smear from an HIV-infected patient with fever and umbilicated facial papules shows oval yeast-like cells within macrophages, many with a transverse central septum. Which statement is correct?",
   choices=["The organism is *Talaromyces marneffei*; treat with amphotericin B followed by itraconazole", "The organism is *Histoplasma capsulatum*; treat with fluconazole", "The organism is *Cryptococcus*; treat with flucytosine alone", "The organism is *Candida*; treat with nystatin", "The organism is *Pneumocystis*; treat with co-trimoxazole"],
   explain="ยีสต์ใน macrophage ที่มี **ผนังกั้นกลาง (binary fission)** = ***Talaromyces marneffei*** → **amphotericin B ~2 สัปดาห์ แล้ว itraconazole**\n\n- *Histoplasma* เป็นยีสต์เล็ก **แตกหน่อ** ไม่มี septum และไม่ใช้ fluconazole\n- *Cryptococcus* มีแคปซูลใหญ่ ไม่อยู่ใน macrophage แบบนี้\n- *Pneumocystis* เห็นเป็น cyst สีดำใน silver stain",
   pearl="Septum = Talaromyces · budding = Histoplasma", ref=["สไลด์ Microorganism 2026 — Dimorphic fungi", "บรรยาย 16 พ.ย. 2569 (บันทึกเสียง)"], nl=["2.3.1-3(7)", "B1.5.4(2)"]),
  dict(id="ID-MIC-MCQ-18", topic="Mucor vs Aspergillus morphology",
   stem="A man with diabetic ketoacidosis has a black necrotic lesion on the hard palate. Biopsy is most likely to show which fungal morphology?",
   choices=["Broad, ribbon-like hyphae with few septa and wide-angle branching", "Narrow septate hyphae with acute-angle (45°) dichotomous branching", "Budding yeast with pseudohyphae", "Encapsulated round budding yeast", "Small intracellular yeasts with a central septum"],
   explain="DKA + เนื้อตายดำที่เพดาน = **rhinocerebral mucormycosis** → **สายกว้าง แบน ผนังกั้นน้อย แตกแขนงมุมกว้าง**\n\n- septate 45° = *Aspergillus* (neutropenia)\n- pseudohyphae = *Candida*\n- encapsulated yeast = *Cryptococcus*\n- septum กลางเซลล์ = *Talaromyces*",
   pearl="DKA + palate necrosis = Mucor (aseptate, 90°)", ref=["สไลด์ Microorganism 2026 — Rhinocerebral mucormycosis, Aspergillosis"], nl=["2.3.1-3(7)", "B1.5.4(2)"]),
 ]))

# ---------------------------------------------------------------- 9
S.append(dict(
 id="id-mic-09", title="Quiz 11 · ตุ่มบุ๋มตรงกลางและผื่นทั่วตัว: Mpox, ราฉวยโอกาส, อีสุกอีใส, syphilis ระยะ 2",
 summary="MSM ผื่นคล้าย molluscum = Mpox (ระยะเดียวกันทั้งตัว) → tecovirimat ในรายรุนแรง · ตุ่มบุ๋มใน HIV: crypto · talaro · histo · อีสุกอีใสหลายระยะพร้อมกัน → acyclovir · syphilis ระยะ 2 ผื่นฝ่ามือฝ่าเท้าไม่บุ๋ม → RPR",
 minutes=8, nl=["2.3.1(22)", "B4.2.2(6)", "2.3.1(19)", "2.3.1(9)", "2.3.1-3(7)"],
 md="""### Quiz 11 — ผู้ป่วยชาย MSM ผื่นตามตัวและก้น 2 วัน
[[img:mic-q11-skin]]

### Umbilicated skin lesion — differential
1. **Mpox** — กลุ่ม **MSM** · ตุ่มน้ำ/ตุ่มหนองบุ๋มกลาง เริ่มที่ **อวัยวะเพศ ก้น รอบทวาร** · ต่อมน้ำเหลืองโต · **รอยโรคระยะเดียวกัน**
2. **Cryptococcosis** — HIV CD4 < 100
3. **Talaromycosis** — HIV · ใบหน้า · ภาคเหนือ
4. **Histoplasmosis** — HIV
5. **Molluscum contagiosum** — ตุ่มนูนเรียบบุ๋มกลาง ไม่มีไข้ (กระจายมากใน HIV)

### ผื่นทั่วตัว — แยกอย่างไร
| | ผู้ป่วย | ลักษณะผื่น | สิ่งที่ต้องตอบ |
|---|---|---|---|
| **อีสุกอีใส (chickenpox)** | คนปกติ | **หลายระยะพร้อมกัน (pleomorphic)**: ตุ่มแดง ตุ่มน้ำ ตุ่มหนอง สะเก็ด · เริ่มที่ลำตัว | **acyclovir** |
| **Mpox** | MSM / HIV | **ระยะเดียวกันทั้งตัว** · บุ๋มกลาง · เจ็บ | PCR จากตุ่ม · ประคับประคอง · **tecovirimat (TPOXX) ในรายรุนแรง/ภูมิต่ำ** |
| **Syphilis ระยะ 2** | กลุ่มเสี่ยงทางเพศ | maculopapular **ฝ่ามือฝ่าเท้า** · ขุยน้อย · **ไม่บุ๋ม** | **ส่ง RPR (คัดกรอง)** + treponemal test → benzathine penicillin G |

> **ผู้สอน:** ยาของ Mpox **มักไม่ค่อยมีคะแนน** แต่อาจให้ตอบ **differential อีก 2 โรค** · **syphilis ระยะ 2 ช่วงหลังออกเยอะ** ให้ตอบว่าส่ง **RPR** · มือเท้าปากในผู้ใหญ่ไม่ค่อยถาม""",
 pearls=["MSM + ตุ่มบุ๋มที่อวัยวะเพศ/ก้น = Mpox · ผื่นระยะเดียวกัน", "อีสุกอีใส = หลายระยะพร้อมกัน → acyclovir", "Umbilicated ใน HIV: crypto · talaro · histo", "Syphilis ระยะ 2: ฝ่ามือฝ่าเท้า ไม่บุ๋ม → RPR"],
 imgs=dict([
  im("mic-q11-skin", "Quiz 11 — ผื่นที่ก้น", "ผิวหนังบริเวณก้นมีตุ่มนูนสีชมพูหลายตุ่มขนาดใกล้กัน บางตุ่มบุ๋มตรงกลาง",
     "ผู้ป่วยชาย MSM ผื่นตามตัวและก้น 2 วัน — บรรยาย วินิจฉัย differential 2 ข้อ และรักษา",
     "**บรรยาย:** papule/pustule หลายตุ่ม **ขนาดและระยะเดียวกัน** บางตุ่ม **บุ๋มตรงกลาง (umbilicated)** · **วินิจฉัย:** **Mpox** (MSM, รอยโรคบริเวณก้น/อวัยวะเพศ) — ยืนยันด้วย **PCR จากตุ่ม** · **differential:** cryptococcosis, talaromycosis (ถ้า HIV), molluscum, อีสุกอีใส (หลายระยะ), syphilis ระยะ 2 · **รักษา:** ประคับประคอง แยกผู้ป่วย · **tecovirimat** ในรายรุนแรง/ภูมิต่ำ · ตรวจ HIV และ STI อื่น"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-19", topic="Mpox vs chickenpox",
   stem="Which feature best distinguishes chickenpox from mpox in an adult with a generalized vesiculopustular rash?",
   choices=["Lesions at different stages (papules, vesicles, pustules, crusts) at the same time", "Umbilicated lesions concentrated in the anogenital area", "Prominent lymphadenopathy", "Lesions all at the same stage of evolution", "History of sex between men"],
   explain="**อีสุกอีใส = รอยโรคหลายระยะพร้อมกัน (pleomorphic)** · Mpox = รอยโรคระยะเดียวกัน บุ๋มกลาง ต่อมน้ำเหลืองโต มักเริ่มที่อวัยวะเพศ/ก้นในกลุ่ม MSM\n\nตัวเลือกที่เหลือเป็นลักษณะของ **Mpox**",
   pearl="หลายระยะ = chickenpox · ระยะเดียว = Mpox", ref=["สไลด์ Microorganism 2026 — Generalised rash", "บรรยาย 16 พ.ย. 2569 (บันทึกเสียง)"], nl=["2.3.1(22)", "B4.2.2(6)"]),
  dict(id="ID-MIC-MCQ-20", topic="Secondary syphilis rash",
   stem="A 24-year-old man has a non-pruritic maculopapular rash involving the palms and soles, without umbilication or vesicles. What is the most appropriate initial laboratory test?",
   choices=["RPR (rapid plasma reagin)", "Tzanck smear", "Mpox PCR", "KOH preparation", "Serum cryptococcal antigen"],
   explain="ผื่น maculopapular **ฝ่ามือฝ่าเท้า** ไม่คัน ไม่บุ๋ม = **syphilis ระยะ 2** → **RPR** (non-treponemal คัดกรอง) แล้วยืนยันด้วย treponemal test\n\n- Tzanck ใช้กับตุ่มน้ำ herpes/VZV\n- Mpox PCR ใช้กับตุ่มบุ๋ม\n- KOH ใช้กับเชื้อราผิวหนัง\n- CrAg ใช้กับตุ่มบุ๋มใน HIV",
   pearl="ผื่นฝ่ามือฝ่าเท้า → RPR", ref=["บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — secondary syphilis ออกบ่อยช่วงหลัง"], nl=["2.3.1(19)", "B10.2.2(1)"]),
 ]))

# ---------------------------------------------------------------- 10
S.append(dict(
 id="id-mic-10", title="Mycobacteria: NTM และ leprosy",
 summary="NTM: slow grower = MAC · rapid grower = M. fortuitum/chelonae/abscessus · ปลา = M. marinum · HIV CD4 < 50 = disseminated MAC · leprosy: TT (Th1 เชื้อน้อย) ↔ LL (Th2 เชื้อมาก) · ENL",
 minutes=7, nl=["2.3.1(20)", "2.3.12-3(9)", "B4.2.2-3(1)", "3.1.9", "2.3.1(9)"],
 md="""### กลุ่ม *Mycobacterium*
- ***M. tuberculosis***
- **Nontuberculous mycobacteria (NTM)** — **slow grower: MAC** (*M. avium complex*), *M. kansasii* · **rapid grower (RGM): *M. fortuitum*, *M. chelonae*, *M. abscessus***
- ***M. leprae***

### NTM ตามกลุ่มอาการ (สไลด์)
| อาการ | ผู้ป่วย / ประวัติ | เชื้อ |
|---|---|---|
| ปอด — **โพรงกลีบบน** | ชายสูบบุหรี่ | MAC, *M. kansasii* |
| ปอด — **bronchiectasis** | หญิงไม่สูบบุหรี่ | MAC, *M. abscessus* |
| hypersensitivity pneumonitis | **hot tub**, ช่างโลหะ | *M. avium* |
| **ต่อมน้ำเหลืองที่คอ** | เด็ก | MAC, *M. scrofulaceum* |
| **fish tank granuloma** — ตุ่มม่วงคล้ำ/แผลตกสะเก็ดที่หลังมือ เรียงตามท่อน้ำเหลือง | เลี้ยงปลา **ตกปลา** สัมผัสน้ำ | ***M. marinum*** |
| แผลเนื้อตาย (Buruli ulcer) | | *M. ulcerans* |
| แผลติดเชื้อหลังผ่าตัด/ฉีดยา/สายสวน | health-care associated | **RGM** |
| **disseminated** | **HIV CD4 < 50** | **MAC**, *M. kansasii* |
| disseminated + Sweet's syndrome | **anti-IFN-γ autoantibody** (พบในคนไทย) | RGM |

### Leprosy — สเปกตรัมภูมิคุ้มกัน
| | **Tuberculoid (TT)** | **Lepromatous (LL)** |
|---|---|---|
| ภูมิคุ้มกัน | **Th1** cell-mediated · granuloma | **Th2** humoral · foamy macrophage |
| เชื้อในรอยโรค | **น้อย** (paucibacillary) | **มากมาย** (multibacillary) |
| ผื่น | **ปื้นเดียว** ขอบชัดนูนแดง หรือวงด่างขาว **แห้ง ขนร่วง ชาชัด** | **หลายรอยสมมาตร** ตุ่ม ปื้น ก้อน · **หน้าสิงโต (leonine facies)** · ชาน้อยกว่า |
| เส้นประสาท | **โต กดเจ็บ** ทำงานเสีย | เสียช้า ไม่รู้ตัว |
| อื่น ๆ | lepromin test บวก · หายเองได้ | **คัดจมูก เลือดกำเดา** ลูกอัณฑะ ตา · lepromin ลบ |

- **Reversal reaction (type 1)** — Th1 เพิ่มขึ้น รอยโรคเดิมอักเสบ เส้นประสาทเจ็บ (borderline)
- **ENL (type 2)** — immune complex ใน BL/LL · ตุ่มแดงกดเจ็บ ไข้

> ผู้สอนกล่าวถึง **MAC ใน HIV ที่ CD4 ต่ำ** ว่าเป็นหัวข้อในเกณฑ์ นล. — ส่วนอื่นของ mycobacteria ไม่ได้ลงรายละเอียดในคาบ""",
 pearls=["MAC = slow grower · CD4 < 50 disseminated", "RGM: fortuitum, chelonae, abscessus — แผลหลังหัตถการ", "เลี้ยงปลา = M. marinum", "TT: Th1 เชื้อน้อย ปื้นเดียวชาชัด · LL: Th2 เชื้อมาก หน้าสิงโต"],
 imgs={},
 items=[
  dict(id="ID-MIC-MCQ-21", topic="Leprosy spectrum",
   stem="A patient has a single, well-demarcated, dry, hairless hypopigmented plaque with marked loss of sensation and a thickened, tender ulnar nerve. Slit-skin smear shows very few acid-fast bacilli. Which statement about this form is correct?",
   choices=["It reflects a strong Th1 cell-mediated response with granulomas", "It is associated with leonine facies and nasal stuffiness", "The lepromin skin test is negative", "Foamy macrophages full of bacilli are characteristic", "It is the form most associated with erythema nodosum leprosum"],
   explain="ปื้นเดียว ชาชัด เส้นประสาทโต เชื้อน้อย = **tuberculoid leprosy** → **Th1 แข็งแรง granuloma** lepromin บวก\n\nตัวเลือกที่เหลือเป็นลักษณะของ **lepromatous leprosy** (Th2, foamy macrophage เชื้อมาก, หน้าสิงโต, คัดจมูก, ENL)",
   pearl="TT = Th1 เชื้อน้อย · LL = Th2 เชื้อมาก", ref=["สไลด์ Microorganism 2026 — Leprosy spectrum"], nl=["2.3.12-3(9)", "B4.2.2-3(1)"]),
  dict(id="ID-MIC-MCQ-22", topic="NTM syndromes",
   stem="An aquarium keeper develops nodules ascending along the lymphatics of his forearm after a minor cut while cleaning the fish tank. Which organism is most likely?",
   choices=["*Mycobacterium marinum*", "*Mycobacterium avium* complex", "*Mycobacterium ulcerans*", "*Mycobacterium kansasii*", "*Mycobacterium leprae*"],
   explain="แผลจากตู้ปลา + ตุ่มเรียงตามท่อน้ำเหลือง (sporotrichoid) = **fish tank granuloma** จาก ***M. marinum***\n\n- MAC: ปอด, ต่อมน้ำเหลืองเด็ก, disseminated ใน HIV\n- *M. ulcerans*: Buruli ulcer\n- *M. kansasii*: ปอดโพรงคล้ายวัณโรค",
   pearl="ตู้ปลา = M. marinum", ref=["สไลด์ Microorganism 2026 — NTM infection"], nl=["B6.2.2(8)"]),
 ]))

# ---------------------------------------------------------------- 11
S.append(dict(
 id="id-mic-11", title="Quiz 15–16 · HIV: PCP, toxoplasma, ท้องเสียเรื้อรังจาก coccidia และโปรโตซัวอื่น",
 summary="Silver stain cyst ดำพื้นเขียว = PCP → co-trimoxazole TMP 15 mg/kg/วัน · hemiparesis ค่อยเป็น + ring-enhancing = toxo → pyrimethamine + sulfadiazine + leucovorin หรือ Bactrim · mAFB ในอุจจาระ: crypto 5 · cyclo 8 · cystoisospora 25 µm",
 minutes=11, nl=["2.3.1(18)", "2.3.1-3(6)", "2.3.1(9)", "3.1.9", "B8.3(6)"],
 md="""### Quiz 15 — HIV ยังไม่ได้ยาต้าน ไข้ ไอ เหนื่อยมากขึ้น 2 วัน
[[img:mic-q15-pcp]]

### *Pneumocystis jirovecii* pneumonia (PCP)
- HIV **CD4 < 200** · ไข้ **ไอแห้ง เหนื่อยมากขึ้นเรื่อย ๆ** · SpO₂ ลดตอนออกแรง · CXR ฝ้าทั้งสองข้าง
- **bronchial washing / induced sputum ย้อม silver (GMS)** → **cyst สีดำบนพื้นเขียว** ขนาด ~5 µm บางอันเป็นรูป "เป้า" · จัดเป็น **เชื้อรา**
- **co-trimoxazole: TMP 15 (–20) mg/kg/วัน** แบ่งให้ 3–4 ครั้ง **21 วัน** · **PaO₂ < 70 mmHg** (หรือ A–a gradient ≥ 35) → **prednisolone** ภายใน 72 ชม.

> **คำนวณให้เป็น** (ผู้สอนให้ตัวอย่าง): Bactrim 1 เม็ดธรรมดา = **TMP 80 mg** · หนัก 50 kg → TMP 750 mg/วัน ≈ **3 เม็ด วันละ 3 ครั้ง** · หนักกว่านี้ ≈ 4 เม็ด วันละ 3 ครั้ง — **เป็นขนาดยาเดียวที่ผู้สอนพูดชัดทั้งคาบ**

### Quiz 16 — HIV ยังไม่ได้ยาต้าน ไข้ต่ำ ๆ แขนขาซ้ายอ่อนแรง สับสน 1 วัน
[[img:mic-q16-toxo]]

### Toxoplasma encephalitis
- HIV **CD4 < 100** · **อาการทางระบบประสาทค่อยเป็นค่อยไปเป็นวัน (subacute)** ต่างจาก stroke ที่ฉับพลัน · ชัก สับสน ไข้
- CT/MRI: **ring-enhancing lesions หลายก้อน** ที่ basal ganglia / รอยต่อ gray–white · toxo IgG บวก
- ภาพ: **tachyzoite รูปจันทร์เสี้ยว**
- ยา **6 สัปดาห์**: **pyrimethamine + sulfadiazine + leucovorin (folinic acid)** · ทางเลือก **co-trimoxazole** (ผู้สอน: ถ้าในตัวเลือกไม่มี Bactrim ให้ตอบสูตรสามตัวนี้) · ไม่ดีขึ้นใน 2 สัปดาห์ → คิดถึง **CNS lymphoma**

### ท้องเสียเรื้อรังใน HIV — ย้อม **modified AFB** ในอุจจาระ
[[img:mic-crypto]]
[[img:mic-cyclo]]
[[img:mic-isospora]]

| เชื้อ | ขนาด oocyst | ยา |
|---|---|---|
| ***Cryptosporidium*** | **เล็กสุด ~4–6 µm** กลม | **เริ่ม ART ฟื้นภูมิ** เป็นหลัก · nitazoxanide/paromomycin ช่วยได้น้อย |
| ***Cyclospora cayetanensis*** | **~8–10 µm** ติดสีไม่สม่ำเสมอ | **co-trimoxazole 160/800 mg bid 7–10 วัน** |
| ***Cystoisospora belli*** (เดิม *Isospora*) | **ใหญ่สุด ~20–30 µm รูปรี** | **co-trimoxazole 160/800 mg qid 10 วัน → bid 3 สัปดาห์** |
| Microsporidia | เล็กมาก ต้องย้อมพิเศษ | albendazole (บางชนิด) |

> **ผู้สอน:** หัวข้อ HIV diarrhea **ชอบถาม** · ***Cryptosporidium* ≠ *Cryptococcus*** (ปรสิตลำไส้ vs รา) · microsporidia ไม่ออก

### โปรโตซัวอื่นในสไลด์
| เชื้อ | ภาพ | ยา |
|---|---|---|
| ***Entamoeba histolytica*** | cyst 4 นิวเคลียส · trophozoite กิน RBC | ไม่มีอาการ: **paromomycin** · ลำไส้/ฝีตับ: **metronidazole 750 mg tid 5–10 วัน** แล้วตาม paromomycin |
| ***Giardia lamblia*** | trophozoite รูปลูกแพร์ 2 นิวเคลียส (หน้าลิง) | **metronidazole 250 mg tid 5 วัน** |
| ***Trichomonas vaginalis*** | trophozoite มีแส้ เคลื่อนไหว (wet prep) | **metronidazole 2 g ครั้งเดียว** หรือ 500 mg bid 7 วัน · รักษาคู่นอน |""",
 pearls=["PCP: silver stain cyst ดำพื้นเขียว → TMP 15 mg/kg/วัน 21 วัน (+ steroid ถ้า PaO₂ < 70)", "Bactrim SS = TMP 80 mg · 50 kg ≈ 3 เม็ด tid", "Toxo: hemiparesis ค่อยเป็น + ring-enhancing → pyrimethamine + sulfadiazine + leucovorin", "mAFB อุจจาระ: crypto 5 · cyclo 8 · cystoisospora 25 µm", "Crypto(sporidium) → ART · cyclo/cystoiso → Bactrim"],
 imgs=dict([
  im("mic-q15-pcp", "Quiz 15 — Bronchial washing, silver stain", "กลุ่มก้อนสีดำของ cyst กลมเล็กจำนวนมากบนพื้นสีเขียวอ่อน",
     "ผู้ป่วย HIV ยังไม่ได้ยาต้าน ไข้ ไอ เหนื่อยมากขึ้น 2 วัน — บรรยาย วินิจฉัย และรักษา (คำนวณขนาดยาสำหรับน้ำหนัก 50 kg)",
     "**บรรยาย:** silver stain เห็น **cyst สีดำ ขนาด ~5 µm บนพื้นเขียว** บางอันรูปเป้า · **วินิจฉัย:** ***Pneumocystis jirovecii* pneumonia (PCP)** ในผู้ป่วย HIV (CD4 น่าจะ < 200) · **รักษา:** **co-trimoxazole TMP 15 mg/kg/วัน** แบ่ง 3 ครั้ง × 21 วัน → 50 kg = TMP 750 mg/วัน ≈ **Bactrim SS (80/400) 3 เม็ด tid** · PaO₂ < 70 → **prednisolone** · แล้วให้ secondary prophylaxis และเริ่ม ART ภายใน 2 สัปดาห์"),
  im("mic-q16-toxo", "Quiz 16 — Toxoplasma", "เชื้อเซลล์เดียวรูปจันทร์เสี้ยวติดสีม่วงจำนวนมากกระจายบนพื้นชมพู",
     "ผู้ป่วย HIV ยังไม่ได้ยาต้าน ไข้ต่ำ ๆ แขนขาซ้ายอ่อนแรง สับสน 1 วัน — บรรยาย วินิจฉัย และรักษา",
     "**บรรยาย:** **crescent-shaped tachyzoites** · **วินิจฉัย:** **Toxoplasma encephalitis** (*Toxoplasma gondii*) — focal deficit แบบ subacute ใน HIV, CT/MRI จะเห็น **ring-enhancing lesions** · **รักษา:** **pyrimethamine + sulfadiazine + leucovorin 6 สัปดาห์** หรือ **co-trimoxazole** · ไม่ดีขึ้นใน 2 สัปดาห์ให้คิด CNS lymphoma"),
  imc("mic-crypto", "Cryptosporidium — modified AFB", "oocyst กลมเล็กติดสีแดงชมพูหลายตัวบนพื้นฟ้า มีแถบมาตราส่วน 10 ไมครอน",
      "oocyst **กลมเล็กที่สุด ~5 µm** ติดสี modified AFB = ***Cryptosporidium*** → **เริ่ม ART** เป็นหลัก"),
  imc("mic-cyclo", "Cyclospora — modified AFB", "oocyst กลมติดสีแดงหนึ่งตัวข้างแถบมาตราส่วน 10 ไมครอน",
      "oocyst กลม **~8–10 µm** ติดสีไม่สม่ำเสมอ = ***Cyclospora*** → **co-trimoxazole**"),
  imc("mic-isospora", "Cystoisospora — modified AFB", "oocyst รูปรีขนาดใหญ่ติดสีแดงสองตัวบนพื้นฟ้า",
      "oocyst **รีใหญ่ที่สุด ~25 µm** = ***Cystoisospora belli*** → **co-trimoxazole qid 10 วัน แล้ว bid 3 สัปดาห์**"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-23", topic="PCP dose calculation",
   stem="A 60-kg man with HIV has PCP with PaO2 62 mmHg on room air. Using co-trimoxazole at trimethoprim 15 mg/kg/day, which daily trimethoprim dose and adjunct are correct?",
   choices=["Trimethoprim 900 mg/day plus prednisolone", "Trimethoprim 900 mg/day without corticosteroids", "Trimethoprim 160 mg/day plus prednisolone", "Trimethoprim 320 mg/day plus prednisolone", "Trimethoprim 1,800 mg/day without corticosteroids"],
   explain="TMP 15 mg/kg/วัน × 60 kg = **900 mg/วัน** (≈ Bactrim SS 80 mg 4 เม็ด tid ใกล้เคียง) · **PaO₂ < 70 → เติม prednisolone** (40 mg bid 5 วัน แล้วลดขนาด)\n\n- 160–320 mg/วัน เป็นขนาด **ป้องกัน**\n- 1,800 mg/วัน = 30 mg/kg สูงเกิน",
   pearl="PCP: TMP 15 mg/kg/วัน · PaO₂ < 70 → steroid", ref=["บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — ตัวอย่างคำนวณ Bactrim", "สไลด์ Microorganism 2026 — Quiz 15"], nl=["2.3.1(18)", "B1.7.2"]),
  dict(id="ID-MIC-MCQ-24", topic="Coccidian parasites in HIV diarrhea",
   stem="A man with untreated HIV has 2 months of watery diarrhea. Modified acid-fast stain of stool shows large oval oocysts about 25 µm long. What is the treatment?",
   choices=["Co-trimoxazole", "Albendazole", "Start ART only; no specific drug is effective", "Metronidazole", "Praziquantel"],
   explain="oocyst ติด mAFB **รีใหญ่ ~25 µm** = ***Cystoisospora belli*** → **co-trimoxazole 160/800 mg qid 10 วัน แล้ว bid 3 สัปดาห์**\n\n- \"เริ่ม ART อย่างเดียว\" เป็นคำตอบของ ***Cryptosporidium*** (oocyst เล็ก ~5 µm)\n- albendazole ใช้กับ microsporidia บางชนิดและพยาธิ\n- metronidazole ใช้กับ *Giardia*, amoeba",
   pearl="25 µm = Cystoisospora → Bactrim · 5 µm = Cryptosporidium → ART", ref=["สไลด์ Microorganism 2026 — Isospora belli oocyst", "บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — HIV diarrhea ชอบถาม"], nl=["2.3.1-3(6)", "B8.3(6)"]),
  dict(id="ID-MIC-MCQ-25", topic="Toxoplasma encephalitis",
   stem="A woman with HIV (CD4 45 cells/µL) develops right hemiparesis over 3 days with low-grade fever. MRI shows multiple ring-enhancing lesions in the basal ganglia; Toxoplasma IgG is positive. What is the most appropriate management?",
   choices=["Pyrimethamine, sulfadiazine and leucovorin, then reassess imaging in 2 weeks", "Immediate stereotactic brain biopsy before any treatment", "Intravenous alteplase", "Amphotericin B plus flucytosine", "Albendazole plus dexamethasone"],
   explain="HIV CD4 < 100 + **focal deficit แบบ subacute** + ring-enhancing หลายก้อน + IgG บวก = **toxoplasma encephalitis** → **empirical pyrimethamine + sulfadiazine + leucovorin** (หรือ co-trimoxazole) แล้วดู MRI ใน 2 สัปดาห์ · ไม่ดีขึ้นจึง biopsy (CNS lymphoma)\n\n- alteplase ใช้กับ stroke ฉับพลัน\n- AmB + 5-FC ใช้กับ cryptococcal meningitis\n- albendazole + dexamethasone ใช้กับ neurocysticercosis",
   pearl="Ring-enhancing ใน HIV → รักษา toxo ก่อน 2 สัปดาห์", ref=["สไลด์ Microorganism 2026 — Quiz 16"], nl=["2.3.1(9)", "2.3.1-3(6)"]),
 ]))

# ---------------------------------------------------------------- 12
S.append(dict(
 id="id-mic-12", title="Quiz 13 · ไข่พยาธิในอุจจาระ: plug, operculum และยาที่ต้องตอบ",
 summary="ไข่มี plug สองข้าง = Trichuris (ถังเบียร์) · Capillaria (ท้องเสียเรื้อรังโปรตีนรั่ว) · plug ข้างเดียว = Gnathostoma · มี operculum = พยาธิใบไม้ → praziquantel · ไข่ Taenia แยกชนิดไม่ได้ · คะแนนอยู่ที่ชื่อยา",
 minutes=10, nl=["2.3.1(12)", "B8.2.2(5)", "B8.3(6)", "B1.5.5(2)", "B1.7.2"],
 md="""### Quiz 13 — ตรวจอุจจาระพบไข่พยาธิ
[[img:mic-q13-egg]]

### แยกไข่พยาธิด้วยปลายไข่ (ผู้สอน)
| ลักษณะไข่ | พยาธิ | จุดเด่น |
|---|---|---|
| **plug สองข้าง (bipolar plugs)** | ***Trichuris trichiura*** | **รูปถังเบียร์/ลูกรักบี้** สีน้ำตาลเหลือง 50–55 µm |
| plug สองข้าง แบนกว่า | ***Capillaria philippinensis*** | **ท้องเสียเรื้อรังเป็นเดือน โปรตีนรั่ว บวม** · กินปลาน้ำจืดดิบ |
| **plug ข้างเดียว** | ***Gnathostoma spinigerum*** (พยาธิตัวจี๊ด) | **ก้อนบวมคันย้ายที่ใต้ผิวหนัง** ไม่มีผื่น |
| **มีฝาปิด (operculum)** | **พยาธิใบไม้ (trematodes)**: ใบไม้ตับ *Opisthorchis/Clonorchis* · ใบไม้ปอด *Paragonimus* · ใบไม้ลำไส้ · *Diphyllobothrium* | → **praziquantel** |
| ไม่มี plug เปลือกบาง | **hookworm** (4–8 cell) · ***Enterobius*** (แบนด้านหนึ่ง เก็บด้วย scotch tape) | |
| ไม่มี plug เปลือกหนา | ***Ascaris*** (เปลือกขรุขระ mammillated) · ***Taenia*** (มีขอเกี่ยว 6 อัน radial striation) | ไข่ *T. solium* กับ *T. saginata* **แยกกันไม่ได้** |

[[img:mic-capillaria]]

### ยาที่ต้องตอบ (สไลด์)
| พยาธิ | ยา |
|---|---|
| ***Ascaris*, hookworm, *Enterobius*** | **albendazole 400 mg ครั้งเดียว** หรือ mebendazole 100 mg bid 3 วัน / 500 mg ครั้งเดียว · *Enterobius* ซ้ำใน 2 สัปดาห์ รักษาทั้งบ้าน |
| ***Trichuris*** | **albendazole 400 mg** (ให้ 3 วันได้ผลดีกว่า) หรือ mebendazole 100 mg bid 3 วัน |
| ***Capillaria*** | **albendazole 400 mg/วัน 10 วัน** (ต้องให้นาน) |
| พยาธิใบไม้ตับ | **praziquantel 25 mg/kg tid 1 วัน** |
| *Paragonimus* (ปูน้ำตก ไอเป็นเลือด) | praziquantel 25 mg/kg tid 2 วัน |
| ***Taenia* ในลำไส้** | **praziquantel 5–10 mg/kg ครั้งเดียว** |
| *Diphyllobothrium latum* (ปลา) | praziquantel 5–10 mg/kg ครั้งเดียว · ทำให้ **ขาด B12 → megaloblastic anemia** |
| *Schistosoma* (ไข่มีหนาม) | praziquantel — ผู้สอน: ไม่ค่อยถาม |

> **ผู้สอน:** หน้า Ascaris, Enterobius, hookworm **คะแนนส่วนใหญ่อยู่ที่ชื่อยา** · **สะกดผิดหักคะแนน อ่านไม่ออกไม่ได้คะแนน**""",
 pearls=["Plug 2 ข้าง: Trichuris (ถังเบียร์) · Capillaria (ท้องเสียเรื้อรังโปรตีนรั่ว)", "Plug ข้างเดียว: Gnathostoma", "Operculum = พยาธิใบไม้ → praziquantel", "Capillaria: albendazole 10 วัน", "ไข่ Taenia 2 ชนิดแยกไม่ได้ · D. latum → B12"],
 imgs=dict([
  im("mic-q13-egg", "Quiz 13 — Stool exam", "ไข่พยาธิรูปรีสีน้ำตาลเหลือง เปลือกหนา ปลายทั้งสองข้างมีจุกใส",
     "ตรวจอุจจาระพบไข่นี้ — บรรยายสิ่งที่พบ และให้การรักษา",
     "**บรรยาย:** ไข่รูป **ถังเบียร์/ลูกรักบี้** สีน้ำตาลเหลือง เปลือกหนา มี **bipolar plugs** ขนาด ~50 µm · **วินิจฉัย:** ***Trichuris trichiura*** (whipworm) — ติดเชื้อมากทำให้ถ่ายเป็นมูกเลือด ทวารหนักยื่น · **รักษา:** **albendazole 400 mg** (3 วันได้ผลดีกว่า) หรือ **mebendazole 100 mg bid 3 วัน**"),
  im("mic-capillaria", "Capillaria philippinensis egg", "ไข่รูปรียาวมีจุกแบนที่ปลายทั้งสองข้าง ภายในเป็นเม็ดละเอียด",
     "ชายกินปลาน้ำจืดดิบ ท้องเสียเรื้อรัง 2 เดือน บวมทั้งตัว albumin ต่ำ — ไข่ในอุจจาระคือ",
     "***Capillaria philippinensis*** — ไข่คล้าย *Trichuris* แต่ **ปลายจุกแบนกว่า ผนังมีลาย** · ทำให้ **protein-losing enteropathy** · รักษา **albendazole 400 mg/วัน × 10 วัน**"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-26", topic="Capillaria philippinensis",
   stem="A 45-year-old man who often eats raw freshwater fish has had watery diarrhea for 3 months with weight loss, edema and serum albumin 1.8 g/dL. Stool shows peanut-shaped eggs with flattened bipolar plugs. What is the treatment?",
   choices=["Albendazole 400 mg daily for 10 days", "Albendazole 400 mg as a single dose", "Praziquantel 25 mg/kg three times in one day", "Metronidazole 250 mg three times daily for 5 days", "Ivermectin 200 µg/kg single dose"],
   explain="ท้องเสียเรื้อรัง + **โปรตีนรั่ว** + ปลาน้ำจืดดิบ + ไข่ plug สองข้างแบน = ***Capillaria philippinensis*** → **albendazole 400 mg/วัน 10 วัน** (ต้องให้นาน — พยาธิ autoinfection)\n\n- ครั้งเดียวไม่พอสำหรับ Capillaria\n- praziquantel ใช้กับไข่มี operculum\n- metronidazole ใช้กับ Giardia",
   pearl="Capillaria = albendazole 10 วัน", ref=["สไลด์ Microorganism 2026 — Capillaria philippinensis egg"], nl=["2.3.1(12)", "B8.2.2(5)"]),
  dict(id="ID-MIC-MCQ-27", topic="Operculated eggs",
   stem="A stool examination from a man in northeastern Thailand who eats raw fermented fish (koi pla) shows small operculated eggs with a shoulder at the operculum. Which drug should be prescribed?",
   choices=["Praziquantel", "Albendazole", "Ivermectin", "Diethylcarbamazine", "Mebendazole"],
   explain="ไข่ **มีฝาปิด (operculum)** + กินปลาดิบ ภาคอีสาน = **พยาธิใบไม้ตับ *Opisthorchis viverrini*** → **praziquantel 25 mg/kg tid 1 วัน** (ระยะยาวเสี่ยง cholangiocarcinoma)\n\n- albendazole/mebendazole ใช้กับพยาธิตัวกลม\n- ivermectin ใช้กับ Strongyloides\n- DEC ใช้กับ filaria",
   pearl="Operculum → praziquantel", ref=["บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — ไข่มี operculum", "สไลด์ Microorganism 2026 — Liver flukes"], nl=["2.3.1(12)", "B1.7.2"]),
 ]))

# ---------------------------------------------------------------- 13
S.append(dict(
 id="id-mic-13", title="Quiz 14 · Strongyloides hyperinfection, larva migrans, filaria และ cysticercosis",
 summary="ภูมิต่ำ + ไข้ ไอ หอบ + ตัวอ่อนในเสมหะ = Strongyloides hyperinfection → ivermectin · Löffler: Ascaris, hookworm, Strongyloides · CLM จากปากขอหมาแมว · eosinophilic meningitis = Angiostrongylus (หอย) · filaria → DEC · neurocysticercosis หินปูน = ไม่ต้องฆ่าพยาธิ",
 minutes=11, nl=["2.3.1(12)", "2.3.1-3(8)", "B2.2.2-3(3)", "B3.2.2(1)", "B6.2.2-3(1)"],
 md="""### Quiz 14 — SLE ได้ prednisolone 20 mg/วัน ไข้ ไอ เหนื่อย 2 วัน
[[img:mic-q14-sputum]]

### *Strongyloides stercoralis* hyperinfection
- **autoinfection** ทำให้อยู่ในตัวได้หลายสิบปี → ได้ **steroid / ยากดภูมิ / HTLV-1** → ตัวอ่อนเพิ่มจำนวนมหาศาล
- **ไข้ ไอ หอบ** ปอดอักเสบ · **พบตัวอ่อน (rhabditiform / filariform) ในเสมหะหรืออุจจาระ** · **GN bacteremia / meningitis** (เชื้อลำไส้ติดตัวอ่อนมา) · eosinophil อาจไม่สูง (steroid กด)
- ยา: **ivermectin 200 µg/kg/วัน** — hyperinfection ให้ **ต่อเนื่องจนตรวจไม่พบตัวอ่อน** (อย่างน้อย 2 สัปดาห์) · ลด steroid · ยาปฏิชีวนะคลุม GN · ทางเลือก albendazole 400 mg bid (ช้ากว่า)
- **ป้องกัน**: คนจากพื้นที่ระบาดก่อนให้ steroid ขนาดสูง → ตรวจหรือให้ ivermectin

> **ผู้สอน:** ในกลุ่ม larva migration **ที่นิยมถามมากที่สุดคือ Strongyloides hyperinfection** · ยาที่ต้องตอบคือ **ivermectin** (ขนาดไม่เน้น)

### ตัวอ่อนไชผ่านปอด — **Löffler syndrome**
***Ascaris lumbricoides*** · **hookworm** · ***Strongyloides*** → ไอ หอบ ฝ้าในปอดย้ายที่ eosinophil สูง · ใบไม้ปอด *Paragonimus* (ปูน้ำตก) → ไอเป็นเลือด

### พยาธิในเนื้อเยื่อ
| พยาธิ | ติดจาก | อาการ | ยา |
|---|---|---|---|
| ***Gnathostoma spinigerum*** (ตัวจี๊ด) | ปลาไหล ปลาช่อน กบ ไก่ ดิบ | **ก้อนบวมคันย้ายที่** · ไขสันหลัง/สมองเลือดออก | **albendazole 400 mg bid 21 วัน** หรือ ivermectin |
| **Cutaneous larva migrans** — *Ancylostoma braziliense/caninum* (ปากขอหมาแมว) | เดินเท้าเปล่าบนทราย/ดิน | **รอยนูนคดเคี้ยวคันมาก (creeping eruption)** ที่เท้า | albendazole 400 mg 3 วัน หรือ ivermectin ครั้งเดียว |
| ***Angiostrongylus cantonensis*** (พยาธิหอยโข่ง) | **หอยโข่ง หอยเชอรี่ดิบ** | **eosinophilic meningitis** ปวดศีรษะมาก CSF eosinophil > 10% | **ประคับประคอง: เจาะหลังลดความดัน + prednisolone** · **เลี่ยงยาฆ่าพยาธิ** |

[[img:mic-angio]]

### Lymphatic filariasis
- **ยุง** เป็นพาหะ (*Mansonia* สำหรับ *B. malayi* ภาคใต้ · *Culex/Aedes* สำหรับ *W. bancrofti*) · เจาะเลือด **ตอนกลางคืน** หา microfilaria
- รักษา **DEC (diethylcarbamazine)** · ผู้สอน: ไม่ค่อยชอบถาม

| | ***Wuchereria bancrofti*** | ***Brugia malayi*** |
|---|---|---|
| รูปร่าง | **ยาวโค้งสวย (graceful)** | **หงิกงอ (kinky)** |
| sheath ใน Giemsa | ใสจาง | **ชมพู** |
| นิวเคลียส | เรียงห่าง | ซ้อนกัน |
| cephalic space | สั้น (1:1) | ยาว (2:1) |
| ปลายหาง | **ไม่มีนิวเคลียสถึงปลาย** | **มี 2 นิวเคลียสที่ปลายหาง** |

### *Taenia solium* — สองทางติด สองโรค
- **กินหมูดิบที่มีเม็ดสาคู (cysticercus)** → **ตัวแก่ในลำไส้ (taeniasis)** → praziquantel 5–10 mg/kg ครั้งเดียว
- **กินไข่** (ผักปนเปื้อน มือ) → **ตัวอ่อนฝังในเนื้อเยื่อ = cysticercosis / neurocysticercosis** → ชัก
- **Neurocysticercosis**
  1. **ถุงยังมีชีวิต (เห็น scolex)** → **albendazole 15 mg/kg/วัน (7.5 mg/kg bid) ~8–14 วัน** ± praziquantel **+ dexamethasone** (กันสมองบวมเมื่อพยาธิตาย) + ยากันชัก
  2. **กลายเป็นหินปูน (calcified)** = พยาธิตายแล้ว → **ไม่ต้องให้ยาฆ่าพยาธิ** ให้แค่ยากันชัก
- **เห็นเม็ดหินปูนในกล้ามเนื้อจากฟิล์มโดยบังเอิญ** → **ไม่ต้องทำอะไร** (ผู้สอน: **ชอบถาม**)""",
 pearls=["Steroid + ไข้ ไอ หอบ + ตัวอ่อนในเสมหะ = Strongyloides hyperinfection → ivermectin จนเชื้อหมด", "Löffler: Ascaris · hookworm · Strongyloides", "หอยดิบ + eosinophilic meningitis = Angiostrongylus → ประคับประคอง + steroid", "W. bancrofti หางไม่มีนิวเคลียส · B. malayi 2 นิวเคลียสที่หาง → DEC", "NCC หินปูน = ไม่ต้องฆ่าพยาธิ · มีชีวิต = albendazole + dexamethasone"],
 imgs=dict([
  im("mic-q14-sputum", "Quiz 14 — Sputum direct smear", "ตัวอ่อนพยาธิรูปเส้นโค้งหลายตัวบนพื้นสีเทา",
     "ผู้ป่วย SLE ได้ prednisolone 20 mg/วัน ไข้ ไอ เหนื่อย 2 วัน — บรรยายสิ่งที่พบ และให้การรักษา",
     "**บรรยาย:** พบ **ตัวอ่อนพยาธิ (rhabditiform/filariform larvae)** จำนวนมากในเสมหะ · **วินิจฉัย:** ***Strongyloides stercoralis* hyperinfection syndrome** จาก steroid · **รักษา:** **ivermectin 200 µg/kg/วัน** ต่อเนื่องจนตรวจไม่พบตัวอ่อน · ลดยากดภูมิ · เพาะเชื้อเลือดและให้ยาคลุม **gram-negative bacteremia**"),
  imc("mic-angio", "Angiostrongylus cantonensis larvae", "ตัวอ่อนพยาธิขดเป็นวงสีส้มทองหลายตัวบนพื้นดำ",
      "ตัวอ่อน *Angiostrongylus cantonensis* — พยาธิปอดหนู ติดคนจาก **หอยโข่ง/หอยเชอรี่ดิบ** → **eosinophilic meningitis** · รักษาประคับประคอง เจาะหลังลดความดัน และ prednisolone"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-28", topic="Strongyloides hyperinfection",
   stem="A 50-year-old woman from northeastern Thailand receiving high-dose prednisolone for SLE develops fever, cough, dyspnea and *Escherichia coli* bacteremia. Sputum direct smear shows numerous nematode larvae. What is the drug of choice for the parasite?",
   choices=["Ivermectin daily until larvae are cleared", "Albendazole 400 mg as a single dose", "Praziquantel 25 mg/kg three times daily", "Diethylcarbamazine", "Mebendazole 100 mg twice daily for 3 days"],
   explain="Steroid + ไข้ ไอ หอบ + **ตัวอ่อนในเสมหะ** + **GN bacteremia** = ***Strongyloides* hyperinfection** → **ivermectin 200 µg/kg/วัน ต่อเนื่องจนตรวจไม่พบตัวอ่อน** + ลด steroid + ยาปฏิชีวนะคลุม GN\n\n- albendazole ได้ผลช้ากว่า และครั้งเดียวไม่พอ\n- praziquantel ใช้กับพยาธิใบไม้/ตืด\n- DEC ใช้กับ filaria",
   pearl="Hyperinfection = ivermectin จนตัวอ่อนหมด", ref=["สไลด์ Microorganism 2026 — Quiz 14, Nematodes treatment", "บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — นิยมถามมากที่สุด"], nl=["2.3.1(12)", "B1.7.2"]),
  dict(id="ID-MIC-MCQ-29", topic="Neurocysticercosis with calcified lesions",
   stem="A 30-year-old man has had one generalized seizure. CT shows two small calcified lesions in the brain parenchyma without edema or enhancement. What is the most appropriate management?",
   choices=["Antiseizure medication only; no anthelmintic therapy", "Albendazole plus dexamethasone for 14 days", "Praziquantel 5–10 mg/kg single dose", "Surgical excision of the lesions", "Ivermectin 200 µg/kg single dose"],
   explain="**Calcified neurocysticercosis = พยาธิตายแล้ว** → **ไม่ต้องให้ยาฆ่าพยาธิ** ให้เพียงยากันชัก\n\n- albendazole + dexamethasone ใช้เมื่อ **ถุงยังมีชีวิต** (cystic, เห็น scolex)\n- praziquantel ครั้งเดียวเป็นขนาดของ *Taenia* ในลำไส้\n- ผ่าตัดใช้กับถุงในโพรงสมองที่อุดตัน",
   pearl="NCC หินปูน = ไม่ให้ยาฆ่าพยาธิ", ref=["บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — calcified ไม่ต้องให้ยา", "สไลด์ Microorganism 2026 — Neurocysticercosis"], nl=["2.3.1-3(8)"]),
  dict(id="ID-MIC-MCQ-30", topic="Eosinophilic meningitis",
   stem="Two days after eating raw golden apple snails, a man develops severe headache and neck stiffness. CSF shows WBC 600/µL with 40% eosinophils and normal glucose. Which organism is most likely and what is the main treatment?",
   choices=["*Angiostrongylus cantonensis*; supportive care with therapeutic lumbar puncture and corticosteroids", "*Gnathostoma spinigerum*; albendazole for 21 days", "*Taenia solium*; praziquantel", "*Cryptococcus neoformans*; amphotericin B", "*Toxocara canis*; diethylcarbamazine"],
   explain="หอยดิบ + **eosinophilic meningitis** ปวดศีรษะมาก ไม่มีอาการเฉพาะที่ = ***Angiostrongylus cantonensis*** → **ประคับประคอง เจาะหลังลดความดัน + prednisolone** · เลี่ยงยาฆ่าพยาธิ (พยาธิตายแล้วอักเสบมากขึ้น)\n\n- *Gnathostoma* ก็ทำ eosinophilic meningitis ได้ แต่มักมี **เลือดออก/ไขสันหลังอักเสบ อ่อนแรงเฉพาะที่** และติดจากปลา/กบ ไม่ใช่หอย\n- *Cryptococcus* CSF เป็น lymphocyte ไม่ใช่ eosinophil",
   pearl="หอยดิบ + CSF eosinophil = Angiostrongylus", ref=["สไลด์ Microorganism 2026 — Eosinophilic meningitis"], nl=["B3.2.2(1)", "2.3.1-3(8)"]),
 ]))

# ---------------------------------------------------------------- 14
S.append(dict(
 id="id-mic-14", title="Quiz 12 · Malaria: อ่าน blood smear และยาตามแนวทางไทย",
 summary="RBC ขนาดปกติ ring เล็กหลายวง double chromatin appliqué gametocyte รูปกล้วย = PF → DHA-piperaquine + primaquine ครั้งเดียว · RBC โต Schüffner's dots = PV/PO → chloroquine + primaquine 14 วัน · PM band form → chloroquine",
 minutes=10, nl=["2.3.1(14)", "B2.2.2(5)", "3.1.3", "B2.3(9)", "B1.7.2"],
 md="""### Quiz 12 — Peripheral blood smear
[[img:mic-q12-pbs]]

> **ผู้สอน:** บางทีโจทย์ **ไม่มีประวัติเลย ให้ดู smear อย่างเดียว** — **บรรยายสิ่งที่เห็นให้ครบ** (marginal form, double chromatin, หลาย ring ใน RBC เดียว) **มีในรูปก็ได้คะแนน** · ข้อสอบมักเป็น **PF หรือ PV** · PO/PM โอกาสน้อย

### แยกชนิดจาก thin film
| | ***P. falciparum*** | ***P. vivax*** | ***P. ovale*** | ***P. malariae*** |
|---|---|---|---|---|
| ขนาด RBC | **ปกติ** | **โตขึ้น** กลม | **โต รูปรี** ขอบหยัก/ปลายแหลม (fimbriated) | **ปกติหรือเล็ก** |
| จุดใน RBC | Maurer's clefts | **Schüffner's dots** | **Schüffner's dots** | ไม่มี |
| ระยะที่เห็น | **ring เล็กจำนวนมาก หลาย ring ใน RBC เดียว** · **double chromatin** · **appliqué (marginal) form** | ring ปนระยะโต amoeboid trophozoite | | **band form** · rosette schizont |
| gametocyte | **รูปกล้วย/จันทร์เสี้ยว** | กลม | กลม | กลม |
| hypnozoite ในตับ | ไม่มี | **มี → relapse** | **มี** | ไม่มี |

[[img:mic-plasmo-vf]]
[[img:mic-plasmo-o]]
[[img:mic-plasmo-m]]

### ยารักษา (แนวทางกองโรคติดต่อนำโดยแมลง — ผู้สอนอ้างฉบับ 2562 และฉบับล่าสุด 2568 ที่ไม่เปลี่ยน)
| ชนิด | ยา | เหตุผล |
|---|---|---|
| ***P. falciparum*** ไม่รุนแรง | **dihydroartemisinin–piperaquine 3 วัน** (แทน artesunate + mefloquine เดิมเพราะ PF ดื้อยาที่ชายแดน) **+ primaquine ครั้งเดียว (single low dose)** | primaquine ฆ่า **gametocyte** ตัดการแพร่เชื้อสู่ยุง |
| ***P. vivax / P. ovale*** | **chloroquine 3 วัน + primaquine 14 วัน** | chloroquine ฆ่าระยะในเลือด · primaquine ฆ่า **hypnozoite** ในตับ **กันกลับเป็นซ้ำ** |
| ***P. malariae*** | **chloroquine อย่างเดียว** | ไม่มี hypnozoite |
| **severe malaria** (ซึม ชัก ไตวาย parasitemia สูง ฯลฯ) | **artesunate IV** แล้วต่อด้วยยากินครบสูตร | |

- **ตรวจ G6PD ก่อนให้ primaquine 14 วัน** (เม็ดเลือดแดงแตก) · ห้ามในหญิงตั้งครรภ์
- **ตรวจแรกเมื่อสงสัย** (ไข้หนาวสั่นหลังเข้าป่า/ชายแดน): **thick และ thin blood film** (หรือ rapid test)
- **หญิงตั้งครรภ์ไตรมาสแรก PF**: **quinine + clindamycin 7 วัน** (แนวทางเดิมและคำตอบในโพย) · WHO 2022 ให้ **artemether–lumefantrine** ได้แล้ว · **ห้าม primaquine และ doxycycline**
- **ยาป้องกันก่อนเข้าป่า** (PF ดื้อยาหลายขนาน ชายแดน): **doxycycline 100 mg วันละครั้ง** เริ่ม 1–2 วันก่อนเข้า กินทุกวัน และต่อ **4 สัปดาห์หลังออก** + ป้องกันยุงกัด
- ผู้สอน: **เปลี่ยนแค่สูตร PF** สายพันธุ์อื่นยังเหมือนเดิม""",
 pearls=["ป้องกันก่อนเข้าป่า: doxycycline 100 mg/วัน 1–2 วันก่อน → 4 สัปดาห์หลังออก", "PF: RBC ปกติ · ring หลายวง · double chromatin · appliqué · gametocyte กล้วย", "PV/PO: RBC โต + Schüffner's dots · PO รูปรีขอบหยัก · PM: band form ไม่มีจุด", "PF → DHA-piperaquine + primaquine ครั้งเดียว (ฆ่า gametocyte)", "PV/PO → chloroquine + primaquine 14 วัน (ฆ่า hypnozoite) · ตรวจ G6PD"],
 imgs=dict([
  im("mic-q12-pbs", "Quiz 12 — Thin blood smear", "เม็ดเลือดแดงขนาดปกติหลายเซลล์ บางเซลล์มี ring เล็กอยู่ชิดขอบเซลล์และมีจุดโครมาตินสองจุด",
     "Peripheral blood smear — บรรยายสิ่งที่พบ วินิจฉัย และให้การรักษา",
     "**บรรยาย:** RBC **ขนาดปกติ** · พบ **ring form เล็ก** บางอัน **ชิดขอบเซลล์ (appliqué/marginal form)** · **double chromatin dots** · ไม่มี Schüffner's dots · **วินิจฉัย:** ***Plasmodium falciparum* malaria** · **รักษา:** **dihydroartemisinin–piperaquine 3 วัน + primaquine single low dose** (ฆ่า gametocyte) · ประเมินภาวะ severe malaria — ถ้ามีให้ **artesunate IV**"),
  imc("mic-plasmo-vf", "P. vivax เทียบ P. falciparum", "แผ่นภาพวาดระยะต่าง ๆ ของเชื้อ P. vivax และ P. falciparum ในเม็ดเลือดแดง",
      "ซ้าย ***P. vivax***: RBC **โตขึ้น มีจุด Schüffner** trophozoite รูปร่างไม่แน่นอน · ขวา ***P. falciparum***: RBC ขนาดปกติ ring เล็กหลายวง และ **gametocyte รูปกล้วย**"),
  imc("mic-plasmo-o", "P. ovale", "แผ่นภาพวาดระยะต่าง ๆ ของ P. ovale ในเม็ดเลือดแดงรูปรี",
      "***P. ovale*** — RBC **โต รูปรี ขอบหยัก (fimbriated)** มี Schüffner's dots · มี hypnozoite เหมือน PV → chloroquine + primaquine 14 วัน"),
  imc("mic-plasmo-m", "P. malariae", "แผ่นภาพวาดระยะต่าง ๆ ของ P. malariae รวมถึงระยะรูปแถบพาดเซลล์",
      "***P. malariae*** — RBC **ขนาดปกติ ไม่มีจุด** · **band form** พาดกลางเซลล์ · ไม่มี hypnozoite → chloroquine อย่างเดียว"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-31", topic="Role of primaquine in P. vivax",
   stem="A soldier returning from the Thai–Myanmar border has *Plasmodium vivax* malaria. G6PD activity is normal. Why is a 14-day course of primaquine added to chloroquine?",
   choices=["To eradicate liver hypnozoites and prevent relapse", "To kill gametocytes and block transmission only", "To treat chloroquine-resistant blood-stage parasites", "To prevent cerebral malaria", "To treat concurrent bacterial infection"],
   explain="*P. vivax/ovale* มี **hypnozoite ในตับ** → **primaquine 14 วัน** เพื่อ **radical cure กัน relapse** · chloroquine ฆ่าระยะในเลือด\n\n- primaquine **ครั้งเดียว** ใช้ใน **PF** เพื่อฆ่า gametocyte\n- PV ไม่ทำ cerebral malaria เป็นลักษณะเด่น",
   pearl="PV/PO: primaquine 14 วัน = ฆ่า hypnozoite", ref=["บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — PV/PO chloroquine + primaquine 14 วัน", "แนวทางการรักษาโรคมาลาเรียในประเทศไทย (กองโรคติดต่อนำโดยแมลง)"], nl=["2.3.1(14)", "B1.7.2"]),
  dict(id="ID-MIC-MCQ-32", topic="Smear features of P. falciparum",
   stem="A thin blood film shows normal-sized red cells containing multiple small rings, some with double chromatin dots and some lying at the cell margin, plus a crescent-shaped gametocyte. Which regimen is recommended for uncomplicated disease in Thailand?",
   choices=["Dihydroartemisinin–piperaquine for 3 days plus single low-dose primaquine", "Chloroquine for 3 days plus primaquine for 14 days", "Chloroquine alone", "Quinine alone for 3 days", "Primaquine alone for 14 days"],
   explain="RBC ปกติ + ring หลายวง + **double chromatin** + **appliqué** + **gametocyte รูปจันทร์เสี้ยว** = ***P. falciparum*** → **DHA–piperaquine 3 วัน + primaquine ครั้งเดียว**\n\n- chloroquine + primaquine 14 วัน เป็นสูตร PV/PO\n- chloroquine เดี่ยวเป็นสูตร PM (PF ดื้อ chloroquine)\n- quinine 3 วันไม่ครบ และไม่ใช่สูตรหลัก",
   pearl="PF: DHA-PPQ + primaquine ครั้งเดียว", ref=["สไลด์ Microorganism 2026 — Quiz 12, Plasmodium morphology", "บรรยาย 16 พ.ย. 2569 (บันทึกเสียง)"], nl=["2.3.1(14)", "3.1.3"]),
 ]))
