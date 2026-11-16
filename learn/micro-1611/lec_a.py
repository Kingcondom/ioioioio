# -*- coding: utf-8 -*-
# เนื้อหาคาบ 16/11 — ส่วนที่ 1 (แบคทีเรีย)
SRC = "ทบทวน Microorganism (จ. 16 พ.ย. 2569) — สไลด์ Microorganism 2026 + บันทึกเสียงบรรยาย"
IMG = "ภาพจากสไลด์ Microorganism 2026 (เอกสารประกอบการบรรยาย)"

def im(key, title, alt, q, quiz):
    return key, {"src": f"img/id/{key}.jpg", "title": title, "alt": alt, "credit": IMG, "q": q, "quiz": quiz}

def imc(key, title, alt, cap):
    return key, {"src": f"img/id/{key}.jpg", "title": title, "alt": alt, "credit": IMG, "cap": cap}

S = []

# ---------------------------------------------------------------- 1
S.append(dict(
 id="id-mic-01", title="ตอบโจทย์ \"จงบรรยาย วินิจฉัย และรักษา\" + จัดกลุ่มเชื้อจาก Gram stain",
 summary="ตอบให้ครบ 3 ท่อน: สิ่งที่เห็น → ชื่อโรคและเชื้อพร้อมเหตุผล → ยา · Gram + รูปร่าง + การเรียงตัว + แคปซูล + ใน/นอกเซลล์ · เขียนชื่อวิทยาศาสตร์ให้ถูก",
 minutes=8, nl=["3.1.9", "B1.5.2(5)", "B1.5.1(1)"],
 md="""### โครงคำตอบที่อาจารย์ต้องการ
ทุก quiz ในสไลด์ถามแบบเดียวกัน: **"จงบรรยาย วินิจฉัย และรักษา"** — ตอบเป็น 3 ท่อนเสมอ
1. **บรรยายสิ่งที่เห็น** — ติดสี Gram อะไร · รูปร่าง (cocci, bacilli, coccobacilli, โค้ง, แตกแขนง) · การเรียงตัว (คู่ สาย กลุ่ม) · มีแคปซูลไหม · อยู่ **ในหรือนอกเซลล์** · มี spore ไหม · มีเม็ดเลือดขาวกี่ชนิด
2. **วินิจฉัย** — **ชื่อโรค + ชื่อเชื้อ + เหตุผลจากประวัติ** (สัมผัสสัตว์ อาหาร IVDU เดินทาง ภูมิคุ้มกัน) ไม่ตอบชื่อเชื้อเปล่า ๆ
3. **รักษา** — **ชื่อยาที่สะกดถูก** สำคัญกว่าขนาดยา (แต่ถ้าจำขนาดได้ให้ใส่)

> **ข้อสอบอัตนัย** — แม้ไม่แน่ใจชื่อเชื้อ ให้บรรยายลักษณะให้ครบ (เช่น "Gram-negative diplococci ภายในเซลล์ PMN") ยังเก็บคะแนนได้ · เตรียม **differential อีกราว 2 ตัว** ไว้เสมอ

### จัดกลุ่มแบคทีเรียจากสไลด์
| กลุ่ม | รูปร่าง / การเรียงตัว | เชื้อสำคัญ |
|---|---|---|
| **GPC กลุ่ม (cluster)** | กลมเป็นพวงองุ่น | *Staphylococcus* |
| **GPC สาย (chain) / คู่** | รีเรียงเป็นสาย หรือคู่ทรงหอก | *Streptococcus*, *Enterococcus* |
| **GPR เล็ก** | แท่งเล็ก club-shaped / palisade | *Listeria*, *Corynebacterium*, *Erysipelothrix* |
| **GPR ใหญ่** | แท่งใหญ่ปลายตัด มี spore | *Bacillus*, *Clostridium* |
| **GP แตกแขนง** | เส้นใยแตกแขนง | *Nocardia* (partially acid-fast), *Actinomyces* |
| **GNC (diplococci)** | คู่รูปเมล็ดถั่ว | *Neisseria* (ในเซลล์), *Moraxella* |
| **GN coccobacilli** | กึ่งกลมกึ่งแท่ง เล็กมาก | *Haemophilus* (pleomorphic), *Acinetobacter* (อ้วนสั้น เป็นคู่), *Brucella* |
| **GNB ตรง** | แท่งมาตรฐาน | Enterobacterales (*E. coli*, *Klebsiella* มีแคปซูล), *Pseudomonas* |
| **GNB ติดสองขั้ว** | **safety-pin** | ***Burkholderia pseudomallei*** |
| **GNB โค้ง** | comma / seagull-wing | *Vibrio*, *Campylobacter*, *Aeromonas* |
| **GNB ปลายแหลม** | fusiform | *Fusobacterium*, *Capnocytophaga* |

### เขียนชื่อวิทยาศาสตร์
- **Genus ขึ้นต้นตัวใหญ่ · species ตัวเล็ก · เอียงทั้งคู่** (เขียนมือ = **ขีดเส้นใต้**) เช่น *Streptococcus pneumoniae*
- ย่อ genus ได้หลังเขียนเต็มครั้งแรก: *S. pneumoniae*
- **serotype ตัวตรง ขึ้นต้นตัวใหญ่** เช่น *Salmonella* Typhi (= *Salmonella enterica* subsp. *enterica* ser. Typhi)
- เขียนกลุ่มแบบไม่เป็นทางการ (viridans streptococci, coagulase-negative staphylococci, salmonellae) **ตัวตรง ตัวเล็ก**
- **สะกดผิดจนอ่านไม่ออก = เสียคะแนน**""",
 pearls=["ตอบ 3 ท่อน: บรรยาย → วินิจฉัย (โรค+เชื้อ+เหตุผล) → ยา", "สะกดชื่อเชื้อและชื่อยาให้ถูก สำคัญกว่าขนาดยา", "Genus Species เอียง/ขีดเส้นใต้ · serotype ตัวตรง: Salmonella Typhi", "Safety-pin = B. pseudomallei · comma = Vibrio/Campylobacter"],
 imgs={}, items=[
  dict(id="ID-MIC-MCQ-01", topic="Writing scientific names",
   stem="Which of the following is the correctly written name of the organism that causes typhoid fever?",
   choices=["*Salmonella* Typhi", "*Salmonella typhi*", "*salmonella* Typhi", "*Salmonella* *Typhi* (all italic)", "Salmonella Typhi (no italics anywhere)"],
   explain="ชื่อเต็มคือ *Salmonella enterica* subsp. *enterica* serovar Typhi → ย่อเป็น ***Salmonella* Typhi** — genus เอียง ขึ้นต้นตัวใหญ่ · **serotype ตัวตรงขึ้นต้นตัวใหญ่** (สไลด์ \"ตัวอย่างการเขียนชื่อวิทยาศาสตร์\")\n\n- *Salmonella typhi* เป็นแบบเก่าที่เขียน Typhi เหมือน species\n- genus ต้องขึ้นต้นตัวใหญ่เสมอ\n- serotype ไม่เอียง\n- เขียนมือให้ **ขีดเส้นใต้แทนตัวเอียง**",
   pearl="Genus species เอียง · Serotype ตัวตรง", ref=["สไลด์ Microorganism 2026 — ตัวอย่างการเขียนชื่อวิทยาศาสตร์", "บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — สะกดชื่อเชื้อให้ถูก"], nl=["B1.5.1(1)"]),
  dict(id="ID-MIC-MCQ-02", topic="Gram-negative bacillus with bipolar staining",
   stem="A Gram stain of pus from a multiloculated splenic abscess in a diabetic rice farmer shows small Gram-negative bacilli that stain more intensely at both ends ('safety-pin'). Which organism is most likely?",
   choices=["*Burkholderia pseudomallei*", "*Klebsiella pneumoniae*", "*Haemophilus influenzae*", "*Vibrio vulnificus*", "*Fusobacterium nucleatum*"],
   explain="**Bipolar staining (safety-pin)** + เบาหวาน + ทำนา + ฝีหลายห้องในม้าม/ตับ = **melioidosis** (*B. pseudomallei*)\n\n- *Klebsiella* เป็นแท่งมาตรฐาน มีแคปซูล (เห็นช่องใสรอบตัว)\n- *H. influenzae* เป็น coccobacilli เล็ก pleomorphic\n- *Vibrio* เป็นแท่งโค้ง\n- *Fusobacterium* ปลายเรียวแหลม (fusiform)",
   pearl="Safety-pin GNB + DM = melioidosis", ref=["สไลด์ Microorganism 2026 — ตารางจำแนก GNB จากสัณฐาน"], nl=["2.3.1(16)", "3.1.9"]),
 ]))

# ---------------------------------------------------------------- 2
S.append(dict(
 id="id-mic-02", title="Quiz 1 · Meningococcus และตาราง CSF แยกเยื่อหุ้มสมองอักเสบ",
 summary="GN diplococci ใน PMN = N. meningitidis · ceftriaxone 2 g / PGS 24 MU/วัน · ป้องกันผู้สัมผัส: cipro 500 ครั้งเดียว / rifampin / ceftriaxone 250 IM (ตั้งครรภ์) · CSF: bacterial vs crypto vs HSV",
 minutes=10, nl=["2.3.1(17)", "2.3.6(5)", "B3.2.2(1)", "B3.3(2)"],
 md="""### Quiz 1 — ไข้ ปวดศีรษะ ซึมลง 2 วัน
[[img:mic-q01-csf]]

### *Neisseria meningitidis*
- **Gram-negative diplococci รูปเมล็ดถั่ว อยู่ในเซลล์ PMN** (*N. gonorrhoeae* ก็ intracellular แต่มาจากระบบสืบพันธุ์)
- สาเหตุอันดับ 2 ของ community-acquired meningitis (รองจาก pneumococcus)
- แยกจาก *H. influenzae* (GN **coccobacilli** เล็ก มักไม่อยู่ในเซลล์หนาแน่น) ด้วย **ตำแหน่งในเซลล์** — ผู้สอนย้ำว่า **โจทย์ไม่จำเป็นต้องบอกว่ามีผื่น** ให้ดูที่ intracellular
- **Meningococcemia** → **purpura fulminans** · DIC · **Waterhouse–Friderichsen syndrome** (ต่อมหมวกไตเลือดออก ช็อก)

[[img:mic-purpura]]

| | ยา |
|---|---|
| **รักษา** | **ceftriaxone 2 g IV q12h** หรือ **cefotaxime 2 g IV q4–6h** · **penicillin G sodium (PGS) 24 ล้านหน่วย/วัน** · แพ้ β-lactam → **chloramphenicol** |
| **ป้องกันผู้สัมผัสใกล้ชิด** | **ciprofloxacin 500 mg ครั้งเดียว** · หรือ **rifampin 600 mg q12h × 2 วัน** · หรือ **ceftriaxone 250 mg IM ครั้งเดียว (ใช้ในหญิงตั้งครรภ์)** |

> **ผู้สอน:** ตอบยาเบื้องต้นแบบผู้ป่วยมาจากบ้าน (**PGS หรือ ceftriaxone**) **ขนาดยาไม่ค่อยเน้น** ไม่ต้องตอบยาแอดวานซ์

### ตาราง CSF แยกโรค (จากสไลด์)
| | Bacterial meningitis | Cryptococcal meningitis | HSV encephalitis |
|---|---|---|---|
| ดำเนินโรค | เฉียบพลัน (ชั่วโมง–วัน) | ค่อยเป็นค่อยไป (สัปดาห์) | เฉียบพลัน (วัน) |
| อาการเด่น | ไข้สูง คอแข็ง ซึม | **ปวดศีรษะรุนแรง ICP สูง** | สับสน พฤติกรรมเปลี่ยน ชัก |
| WBC | **> 1,000** | 20–500 | 10–500 |
| เซลล์ | **neutrophil** | lymphocyte | lymphocyte |
| glucose | **ต่ำมาก (< 40)** | ต่ำ | ปกติ |
| protein | สูงมาก | สูง | สูงเล็กน้อย |
| opening pressure | สูง | **สูงมาก (> 25 cmH₂O)** | ปกติหรือสูงเล็กน้อย |
| lab พิเศษ | Gram stain, culture | **India ink, CrAg** | **HSV PCR** |
| MRI | meningeal enhancement | soap-bubble lesions ที่ basal ganglia | **temporal lobe** บวม/เลือดออก |
| ยา | **ceftriaxone + vancomycin** (empiric) | **amphotericin B + flucytosine** | **acyclovir IV** |""",
 pearls=["GN diplococci ใน PMN ใน CSF = meningococcus", "Purpura fulminans · Waterhouse–Friderichsen", "Prophylaxis: cipro 500 ครั้งเดียว · rifampin 600 q12h × 2 วัน · ceftriaxone 250 IM (ตั้งครรภ์)", "Crypto: opening pressure > 25 · India ink/CrAg · HSV: temporal lobe · PCR"],
 imgs=dict([
  im("mic-q01-csf", "Quiz 1 — CSF Gram stain", "สไลด์ย้อม Gram เห็นเม็ดเลือดขาวนิวเคลียสหลายพู และเชื้อสีชมพูเป็นคู่ภายในเซลล์",
     "ผู้ป่วยชาย ไข้ ปวดศีรษะ ซึมลง 2 วัน — บรรยาย วินิจฉัย และรักษา",
     "**บรรยาย:** Gram-negative diplococci (รูปเมล็ดถั่ว) อยู่ **ภายใน PMN** · **วินิจฉัย:** acute bacterial meningitis จาก ***Neisseria meningitidis*** · **รักษา:** ceftriaxone 2 g IV q12h (หรือ PGS 24 ล้านหน่วย/วัน) · ให้ยาป้องกันผู้สัมผัสใกล้ชิด (ciprofloxacin 500 mg ครั้งเดียว)"),
  imc("mic-purpura", "Purpura fulminans", "ขาทั้งสองข้างมีผื่นจ้ำเลือดสีม่วงดำกระจายทั่ว",
      "**จ้ำเลือดกระจายและเนื้อตาย (purpura fulminans)** จาก meningococcemia ร่วมกับ DIC — ช็อกเร็ว ต้องให้ยาทันทีไม่รอ LP"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-03", topic="Chemoprophylaxis for meningococcal contacts in pregnancy",
   stem="A 28-year-old woman who is 20 weeks pregnant shared a dormitory room with a student just diagnosed with meningococcal meningitis. Which prophylaxis is most appropriate for her?",
   choices=["Ceftriaxone 250 mg IM as a single dose", "Ciprofloxacin 500 mg orally as a single dose", "Rifampin 600 mg orally every 12 hours for 2 days", "No prophylaxis; observe for fever", "Meningococcal vaccine alone"],
   explain="ผู้สัมผัสใกล้ชิด (ร่วมห้องนอน) ต้องได้ **chemoprophylaxis** · **หญิงตั้งครรภ์ → ceftriaxone 250 mg IM ครั้งเดียว** (ตามสไลด์)\n\n- ciprofloxacin เลี่ยงในหญิงตั้งครรภ์\n- rifampin ใช้ได้ทั่วไปแต่ไม่แนะนำในตั้งครรภ์ และมี drug interaction\n- วัคซีนเพียงอย่างเดียวป้องกันไม่ทันในผู้สัมผัส",
   pearl="Contact ตั้งครรภ์ → ceftriaxone 250 mg IM", ref=["สไลด์ Microorganism 2026 — N. meningitidis prophylaxis"], nl=["2.3.1(17)", "B1.7.2"]),
  dict(id="ID-MIC-MCQ-04", topic="CSF pattern of cryptococcal meningitis",
   stem="A 34-year-old man with untreated HIV has had worsening headache for 3 weeks. CSF: opening pressure 38 cmH2O, WBC 40/µL (90% lymphocytes), glucose 32 mg/dL (serum 100), protein 110 mg/dL. Which test on the CSF is most likely to confirm the diagnosis rapidly?",
   choices=["Cryptococcal antigen (CrAg)", "HSV PCR", "Gram stain", "VDRL", "Adenosine deaminase"],
   explain="ปวดศีรษะเป็นสัปดาห์ · **opening pressure สูงมาก (> 25)** · lymphocyte · glucose ต่ำ ใน HIV = **cryptococcal meningitis** → **CrAg (หรือ India ink)**\n\n- HSV encephalitis: เฉียบพลัน สับสน ชัก glucose ปกติ\n- Gram stain ใช้กับ bacterial (PMN > 1,000)\n- VDRL/ADA ใช้กับ neurosyphilis/TB meningitis ซึ่งไม่เด่นเรื่อง ICP สูงมากแบบนี้",
   pearl="Crypto: ICP สูงมาก + lympho → CrAg/India ink", ref=["สไลด์ Microorganism 2026 — ตารางเปรียบเทียบการวินิจฉัยแยกโรค"], nl=["B3.3(2)", "2.3.1-3(7)"]),
 ]))

# ---------------------------------------------------------------- 3
S.append(dict(
 id="id-mic-03", title="Quiz 2–4 · Streptococcus: GAS, pneumococcus, S. suis, GBS, Enterococcus",
 summary="แยก strep ด้วย hemolysis · GAS ทอนซิลอักเสบ (ARF, AGN) · pneumococcus = GP lancet diplococci มีแคปซูล · S. suis = เนื้อหมู + หูดับ · GBS ทารก/ตั้งครรภ์/ผู้สูงอายุ · Enterococcus UTI/IE",
 minutes=10, nl=["2.3.6(5)", "B3.2.2(1)", "B9.2.2(3)", "B1.5.2(8)", "2.3.9-3(5)"],
 md="""### แยก *Streptococcus* ด้วย hemolysis บน blood agar
| hemolysis | กลุ่ม | โรคเด่น |
|---|---|---|
| **β (ใสทั้งวง)** | **Group A — *S. pyogenes*** | **pharyngitis** · ผิวหนัง (erysipelas, cellulitis, **necrotizing fasciitis**) · STSS · ตามมาด้วย **ARF, AGN** |
| β | **Group B — *S. agalactiae*** | **ทารกแรกเกิด หญิงตั้งครรภ์** · ผู้ใหญ่ที่มี DM มะเร็ง ตับเรื้อรัง อายุ > 65 → meningitis, bacteremia |
| **α (เขียว)** | ***S. pneumoniae*** | **CAP · meningitis · otitis media** |
| α | **viridans streptococci** | **IE แบบ subacute** |
| α (ในสไลด์) | ***S. suis*** | **meningitis + หูดับ (sensorineural hearing loss)** · endocarditis |
| **γ (ไม่สลาย)** | ***Enterococcus faecalis / faecium*** | **UTI · IE** |

### Quiz 2 — ไข้ เจ็บคอ 2 วัน ทอนซิลมีหนอง
[[img:mic-q02-throat]]

### Quiz 3 — ไข้ ไอ เหนื่อย 2 วัน crepitation ปอดขวาล่าง
[[img:mic-q03-sputum]]

### Quiz 4 — ไข้สูง ปวดศีรษะ หูซ้ายไม่ได้ยิน 4 วัน
[[img:mic-q04-csf]]

> **ผู้สอน:** ข้อ *S. suis* ต้องตอบ **ชื่อโรคและอาการด้วย** (เช่น *S. suis* meningitis ร่วมหูดับ) ไม่ใช่ตอบแค่ชื่อเชื้อ

> ***S. suis*** — ซักประวัติ **ชำแหละ/ขายเนื้อหมู กินหมูดิบ (ลาบ หลู้)** · มาด้วย meningitis และ **หูดับถาวร** · รักษาแบบ meningitis: **penicillin G หรือ ceftriaxone**

### ยาที่ต้องตอบ
> ผู้สอนสรุปยาที่ต้องจำ: **Strep → penicillin / cephalosporin** · **Staph → cloxacillin** · **Enterococcus → ampicillin**

- **GAS pharyngitis** → **penicillin V / amoxicillin 10 วัน** (ป้องกัน ARF)
- **Pneumococcal CAP** → amoxicillin/ceftriaxone ตามความรุนแรง — ผู้สอน: ผู้ป่วยมาจากบ้าน **ไม่ต้องตอบ piperacillin-tazobactam** · **meningitis** → ceftriaxone + vancomycin จนรู้ความไว
- **Enterococcal IE** → **ampicillin + ceftriaxone** (เลี่ยง gentamicin เพื่อรักษาไต)""",
 pearls=["β: GAS (คอ ผิว ARF AGN) · GBS (ทารก ตั้งครรภ์ ผู้สูงอายุ)", "α: pneumococcus (lancet diplococci มีแคปซูล) · viridans (IE) · S. suis (หมู + หูดับ)", "γ: Enterococcus → UTI, IE · amp + ceftriaxone"],
 imgs=dict([
  im("mic-q02-throat", "Quiz 2 — Throat swab Gram stain", "เชื้อกลมติดสีม่วงเข้มเรียงเป็นสายยาวคดเคี้ยว",
     "ผู้ป่วยชาย ไข้ เจ็บคอ 2 วัน exudative tonsillitis — บรรยาย วินิจฉัย และรักษา",
     "**บรรยาย:** Gram-positive cocci **in chains** · **วินิจฉัย:** acute exudative pharyngitis จาก **β-hemolytic streptococcus group A (*Streptococcus pyogenes*)** · **รักษา:** penicillin V หรือ amoxicillin **10 วัน** (ป้องกัน rheumatic fever) · ภาวะแทรกซ้อน: ARF, AGN, peritonsillar abscess"),
  im("mic-q03-sputum", "Quiz 3 — Sputum Gram stain", "พื้นสีชมพู มีเชื้อกลมรีติดสีม่วงอยู่เป็นคู่ ปลายแหลมคล้ายหอก",
     "ผู้ป่วยชาย ไข้ ไอ เหนื่อย 2 วัน crepitation ปอดขวาล่าง — บรรยาย วินิจฉัย และรักษา",
     "**บรรยาย:** Gram-positive **lancet-shaped diplococci** มี **แคปซูล** (ช่องใสรอบตัว) · **วินิจฉัย:** community-acquired pneumonia จาก ***Streptococcus pneumoniae*** · **รักษา:** amoxicillin (OPD) หรือ ceftriaxone ± macrolide ถ้านอนโรงพยาบาล"),
  im("mic-q04-csf", "Quiz 4 — CSF Gram stain", "เชื้อกลมติดสีม่วงอยู่เป็นคู่และเป็นสายสั้น ๆ บนพื้นสีชมพูอ่อน",
     "ผู้ป่วยไข้สูง ปวดศีรษะ หูซ้ายไม่ได้ยิน 4 วัน — บรรยาย วินิจฉัย และรักษา (ถามประวัติอะไรเพิ่ม)",
     "**บรรยาย:** Gram-positive cocci เป็น **คู่และสายสั้น** · **วินิจฉัย:** bacterial meningitis ร่วม **sensorineural hearing loss** จาก ***Streptococcus suis*** — ถามประวัติ **สัมผัสหรือกินเนื้อหมูดิบ** · **รักษา:** penicillin G หรือ ceftriaxone (ขนาด meningitis) · ภาวะหูดับมักถาวร"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-05", topic="Meningitis with hearing loss after pork exposure",
   stem="A 55-year-old pig butcher has fever, headache, neck stiffness and new left-sided deafness for 3 days. CSF Gram stain shows Gram-positive cocci in pairs and short chains. Which organism is most likely?",
   choices=["*Streptococcus suis*", "*Listeria monocytogenes*", "*Neisseria meningitidis*", "*Staphylococcus aureus*", "*Streptococcus agalactiae*"],
   explain="**ชำแหละหมู + meningitis + หูดับ (sensorineural hearing loss)** + GPC คู่/สายสั้น = ***S. suis*** → penicillin G หรือ ceftriaxone\n\n- *Listeria* เป็น GP **rod** ในผู้สูงอายุ/ภูมิต่ำ\n- meningococcus เป็น GN diplococci\n- *S. aureus* เป็น GPC กลุ่ม\n- GBS พบในทารก ตั้งครรภ์ ผู้สูงอายุที่มีโรคร่วม ไม่สัมพันธ์กับหมู",
   pearl="หมู + meningitis + หูดับ = S. suis", ref=["สไลด์ Microorganism 2026 — Quiz 4, S. suis", "บรรยาย 16 พ.ย. 2569 (บันทึกเสียง)"], nl=["B3.2.2(1)", "B1.5.2(8)"]),
  dict(id="ID-MIC-MCQ-06", topic="Group A strep sequelae",
   stem="An 18-year-old has exudative tonsillitis; a throat swab shows Gram-positive cocci in chains with beta-hemolysis on blood agar. The main reason to complete a 10-day course of penicillin is to prevent which complication?",
   choices=["Acute rheumatic fever", "Post-streptococcal glomerulonephritis", "Scarlet fever", "Streptococcal toxic shock syndrome", "Infective endocarditis"],
   explain="ให้ penicillin ครบ **10 วัน** เพื่อกำจัดเชื้อจากคอและ **ป้องกัน acute rheumatic fever**\n\n- **AGN (PSGN) ป้องกันไม่ได้ด้วยยาปฏิชีวนะ** — เป็นภาวะทางภูมิคุ้มกันที่เกิดได้แม้รักษาแล้ว\n- scarlet fever เป็นผื่นจาก toxin ระหว่างติดเชื้อ ไม่ใช่เหตุผลหลักของการให้ครบ\n- STSS และ IE ไม่ใช่ภาวะแทรกซ้อนที่การให้ครบ 10 วันมุ่งป้องกัน",
   pearl="GAS ครบ 10 วัน = กัน ARF (ไม่กัน AGN)", ref=["สไลด์ Microorganism 2026 — β-hemolytic streptococci group A"], nl=["B9.2.2(3)", "B1.7.2"]),
 ]))

# ---------------------------------------------------------------- 4
S.append(dict(
 id="id-mic-04", title="Quiz 5 · S. aureus bacteremia และการรักษา IE ตามเชื้อ",
 summary="GPC กลุ่มใน hemoculture + IVDU = S. aureus IE ลิ้น tricuspid · MSSA → cloxacillin · MRSA → vancomycin · complicated vs uncomplicated SAB · ตารางยา IE ตามเชื้อ",
 minutes=10, nl=["2.3.9-3(5)", "B7.2.2-3(2)", "3.1.9", "B1.7.2"],
 md="""### Quiz 5 — ไข้สูง เหนื่อย 2 วัน ประวัติ IVDU
[[img:mic-q05-hemo]]

### *Staphylococcus*
- **coagulase บวก** = ***S. aureus*** · **coagulase ลบ (CoNS)** = *S. epidermidis* (สายสวน อุปกรณ์), *S. saprophyticus* (UTI หญิงสาว), *S. haemolyticus*
- **IVDU** → *S. aureus* bacteremia + **IE ลิ้น tricuspid** → **septic pulmonary emboli** (ก้อนในปอดหลายก้อน มีโพรง)

### *S. aureus* bacteremia (SAB) — complicated หรือไม่
| complicated / high risk | uncomplicated / low risk |
|---|---|
| **IE** · ฝีในอวัยวะ (ปอด ไต ม้าม ตับ) · septic arthritis · discitis/osteomyelitis · embolic phenomena (สมอง ปอด ม้าม) · central line infection | peripheral line infection · SSTI ที่เอาต้นเหตุออกแล้ว |

> **ผู้สอน:** ยาชื่อ **cloxacillin** (ในไทย) — ผู้ป่วยอาจมี HIV ร่วมหรือไม่ก็ได้

> SAB **ทุกราย** ต้องหาจุดติดเชื้อ ทำ **echocardiography** และเจาะเลือดซ้ำจนเชื้อหาย

### ยารักษา IE ตามเชื้อ (สไลด์)
| เชื้อ | ลิ้นธรรมชาติ (NVE) | ลิ้นเทียม (PVE) |
|---|---|---|
| **Streptococci (viridans)** | **penicillin G หรือ ceftriaxone 4 สัปดาห์** (2 สัปดาห์ถ้าร่วม gentamicin) | + gentamicin 2 สัปดาห์แรก รวม 6 สัปดาห์ |
| **MSSA** | **nafcillin/oxacillin (ไทยใช้ cloxacillin) 4–6 สัปดาห์** · **ไม่ใช้ gentamicin** (ไตวาย) | + **rifampin + gentamicin** ≥ 6 สัปดาห์ |
| **MRSA** | **vancomycin หรือ daptomycin (10–12 mg/kg)** 4–6 สัปดาห์ | vancomycin + rifampin + gentamicin |
| **Enterococci** | **ampicillin + ceftriaxone 6 สัปดาห์** | เช่นเดียวกัน |
| **HACEK** | **ceftriaxone** 4 (NVE) / 6 (PVE) สัปดาห์ | |
| culture ลบ (NVE) | vancomycin + ceftriaxone แล้วปรับตาม serology | |

- **rifampin** เริ่มหลังให้ยาอื่น 3–5 วันเมื่อเชื้อในเลือดหมด — ใช้เพื่อ biofilm บนลิ้นเทียม""",
 pearls=["GPC กลุ่ม + IVDU = S. aureus → tricuspid IE + septic emboli ปอด", "MSSA = cloxacillin · MRSA = vancomycin/daptomycin", "Staph NVE ไม่ให้ gentamicin · rifampin เฉพาะ PVE", "Enterococcus = amp + ceftriaxone 6 สัปดาห์"],
 imgs=dict([
  im("mic-q05-hemo", "Quiz 5 — Hemoculture Gram stain", "เชื้อกลมติดสีม่วงเข้มเกาะกันเป็นกลุ่มคล้ายพวงองุ่น มีแถบมาตราส่วน 10 ไมครอน",
     "ผู้ป่วยไข้สูง เหนื่อย 2 วัน ประวัติ IVDU hemoculture ขึ้นเชื้อ — บรรยาย วินิจฉัย และรักษา",
     "**บรรยาย:** Gram-positive cocci **in clusters (grape-like)** · **วินิจฉัย:** ***Staphylococcus aureus*** bacteremia สงสัย **infective endocarditis ลิ้น tricuspid** (IVDU) ± septic pulmonary emboli · **รักษา:** MSSA → **cloxacillin IV** 4–6 สัปดาห์ · ระหว่างรอผลความไว/เสี่ยง MRSA → **vancomycin** · ทำ echocardiography"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-07", topic="Treatment of MSSA native-valve endocarditis",
   stem="A 30-year-old man who injects drugs has fever, multiple cavitating lung nodules and a tricuspid vegetation. Blood cultures grow methicillin-susceptible *Staphylococcus aureus*. Which regimen is most appropriate?",
   choices=["Cloxacillin IV for 4–6 weeks", "Cloxacillin IV plus gentamicin for 6 weeks", "Vancomycin plus rifampin plus gentamicin for 6 weeks", "Ceftriaxone IV for 2 weeks", "Oral dicloxacillin for 2 weeks"],
   explain="**MSSA native-valve IE** → **anti-staphylococcal penicillin (nafcillin/oxacillin; ในไทยใช้ cloxacillin) 4–6 สัปดาห์**\n\n- **ไม่เติม gentamicin** ใน Staph NVE — ไม่ช่วยและเพิ่มไตวาย\n- vancomycin + rifampin + gentamicin เป็นสูตร **MRSA ลิ้นเทียม**\n- ceftriaxone 2 สัปดาห์ใช้กับ viridans strep (ร่วม gentamicin)\n- ยากินไม่ใช่สูตรเริ่มต้นของ IE",
   pearl="MSSA NVE = cloxacillin 4–6 wk ไม่ต้อง genta", ref=["สไลด์ Microorganism 2026 — Clinical treatment of infective endocarditis"], nl=["2.3.9-3(5)", "B1.7.2"]),
  dict(id="ID-MIC-MCQ-08", topic="Complicated Staphylococcus aureus bacteremia",
   stem="Which finding classifies *S. aureus* bacteremia as complicated (high risk), requiring prolonged therapy?",
   choices=["Vertebral discitis on MRI", "Infection of a peripheral IV cannula that has been removed", "Fever resolving within 48 hours", "Negative repeat blood cultures at 48 hours", "Coagulase-negative staphylococci in one of two blood culture bottles"],
   explain="**Complicated SAB** = มีจุดติดเชื้อลึก: IE, ฝีในอวัยวะ, septic arthritis, **discitis/osteomyelitis**, embolic phenomena, central line\n\n- peripheral line ที่ถอดแล้ว = uncomplicated\n- ไข้ลงเร็วและเชื้อในเลือดหายใน 48 ชม. เป็นลักษณะของ low risk\n- CoNS ขวดเดียวมักเป็น contamination ไม่ใช่ SAB",
   pearl="SAB + discitis/IE/abscess = complicated", ref=["สไลด์ Microorganism 2026 — Clinical manifestations of SAB"], nl=["B7.2.2-3(2)"]),
 ]))

# ---------------------------------------------------------------- 5
S.append(dict(
 id="id-mic-05", title="Quiz 6–7 · Gram-positive rods: Listeria และ cutaneous anthrax",
 summary="GPR ใน CSF ผู้สูงอายุ/ภูมิต่ำ/ตั้งครรภ์ = Listeria → ampicillin ± gentamicin (ตั้งครรภ์ไม่ให้ genta) · แผลดำไม่เจ็บบวมรอบ + GPR ใหญ่ปลายตัดเป็นสาย = cutaneous anthrax",
 minutes=9, nl=["B3.2.2(1)", "2.3.6(5)", "2.3.1-3(9)", "B1.5.2(8)"],
 md="""### Gram-positive rods ในสไลด์
- **เล็ก**: *Listeria monocytogenes*, *Erysipelothrix rhusiopathiae* (จับปลา/เนื้อสัตว์), *Corynebacterium*
- **ใหญ่ มี spore**: *Bacillus* (anthrax), *Clostridium*

### Quiz 6 — ไข้ ปวดศีรษะ ซึม 2 วัน
[[img:mic-q06-csf]]

### *Listeria monocytogenes*
| | |
|---|---|
| ปัจจัยเสี่ยง | **อายุ ≥ 65** · **ตั้งครรภ์ (เสี่ยง 10 เท่า)** · steroid · มะเร็ง · ภูมิคุ้มกันบกพร่อง · ทารกแรกเกิด |
| อาหาร | **อาหารแช่เย็นพร้อมกิน** (cold cuts, pâté, ไส้กรอก, ชีสนมดิบ) — เติบโตได้ในตู้เย็น |
| คลินิก | gastroenteritis + ไข้ · bacteremia · **meningoencephalitis / rhombencephalitis** (ก้านสมอง) · ตั้งครรภ์ → แท้ง คลอดก่อนกำหนด ทารกติดเชื้อ |
| CSF | เซลล์ได้ทั้ง PMN และ mono · glucose ต่ำ · **Gram stain มักลบ** · culture บวก |
| ยา | **ampicillin 2 g IV q4h** (หรือ PGS 4 ล้านหน่วย q4h) **± gentamicin** · **ตั้งครรภ์: ampicillin ไม่ให้ gentamicin** · แพ้ penicillin → TMP-SMX |

> ผู้สอนบอกว่า *Listeria* **ไม่ค่อยออกสอบ** แต่ให้จำ host และยา

> **ceftriaxone ไม่ครอบคลุม *Listeria*** — empiric meningitis ในคนอายุ > 50 หรือภูมิต่ำจึงต้อง **เติม ampicillin**

### Quiz 7 — แผลที่ต้นคอ 10 วัน
[[img:mic-q07-eschar]]
[[img:mic-q07-pus]]

> **ผู้สอน:** ข้อนี้ **เคยออกสอบ (มีข่าวปีกลาย)** — เทียบกับ eschar ของ scrub typhus ซึ่ง **เล็ก อยู่ในร่มผ้า/รักแร้ รอบไม่แดง** ส่วนโจทย์นี้ **แผลใหญ่ ขอบแดงบวม ไม่เจ็บ อยู่ที่คอ (exposed area)** + large GPR in chains

### Cutaneous anthrax (*Bacillus anthracis*)
- แผล **ดำ (black eschar) ไม่เจ็บ** ล้อมด้วย **บวมน้ำมาก** (malignant edema) · ติดจากสัตว์กินหญ้า หนังสัตว์ ขนสัตว์
- **GPR ใหญ่ ปลายตัดเหลี่ยม (square-ended) เรียงเป็นสาย** (boxcar)
- ยา: **ciprofloxacin หรือ doxycycline** กิน 7–10 วัน (ได้รับจาก bioterrorism/สูดดมให้ 60 วัน) · ห้ามผ่าตัดแผล
- แยกจาก **eschar ของ scrub typhus** (เล็ก ไม่บวมรอบ อยู่ใต้ร่มผ้า) และ **mucormycosis** (เนื้อตายดำที่เพดาน/จมูกใน DKA)""",
 pearls=["Listeria: GPR + ผู้สูงอายุ/ตั้งครรภ์/steroid + อาหารแช่เย็น", "Ceftriaxone ไม่คลุม Listeria → เติม ampicillin", "ตั้งครรภ์: ampicillin ไม่ใส่ gentamicin", "Anthrax: eschar ดำไม่เจ็บ บวมมาก + boxcar GPR → cipro/doxy"],
 imgs=dict([
  im("mic-q06-csf", "Quiz 6 — CSF Gram stain", "เชื้อรูปแท่งติดสีม่วงเข้มจำนวนมาก",
     "ผู้ป่วยชาย ไข้ ปวดศีรษะ ซึมลง 2 วัน CSF เห็น Gram-positive bacilli — บรรยาย วินิจฉัย และรักษา",
     "**บรรยาย:** Gram-positive **bacilli** (แท่งสั้น ไม่มี spore) · **วินิจฉัย:** bacterial meningitis จาก ***Listeria monocytogenes*** — ถามอายุ ตั้งครรภ์ steroid มะเร็ง อาหารแช่เย็น · **รักษา:** **ampicillin 2 g IV q4h ± gentamicin** (ตั้งครรภ์ไม่ให้ gentamicin) · แพ้ penicillin → TMP-SMX"),
  im("mic-q07-eschar", "Quiz 7 — แผลที่ต้นคอ", "แผลกลมตรงกลางเป็นสะเก็ดดำ ขอบแดงบวมกว้างที่ต้นคอ",
     "ผู้ป่วยชาย แผลที่ต้นคอ 10 วัน **ไม่เจ็บ** black eschar ขอบแดงบวม — คิดถึงอะไร",
     "**Painless black eschar + บวมน้ำรอบแผลมาก** = **cutaneous anthrax** — ถามการสัมผัสสัตว์ หนัง ขนสัตว์ · ดูภาพหนองถัดไป"),
  im("mic-q07-pus", "Quiz 7 — Pus Gram stain", "เชื้อแท่งใหญ่ติดสีม่วงปลายตัดเหลี่ยมเรียงต่อกันเป็นสายยาว ปนเม็ดเลือดขาว",
     "หนองจากแผลเดียวกัน — บรรยาย วินิจฉัย และรักษา",
     "**บรรยาย:** **large, square-ended Gram-positive rods in chains** (boxcar) · **วินิจฉัย:** **cutaneous anthrax** (*Bacillus anthracis*) · **รักษา:** **ciprofloxacin หรือ doxycycline** กิน 7–10 วัน · ไม่ผ่าตัดแผล"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-09", topic="Empiric coverage for Listeria",
   stem="A 72-year-old man taking prednisolone for bullous pemphigoid presents with fever and confusion. CSF shows WBC 450/µL (60% neutrophils), low glucose and a negative Gram stain. Empiric therapy should include ceftriaxone and vancomycin plus which drug?",
   choices=["Ampicillin", "Gentamicin alone", "Metronidazole", "Acyclovir alone without antibacterials", "Clindamycin"],
   explain="อายุ > 50 + steroid → ต้องคลุม ***Listeria*** ซึ่ง **ceftriaxone ไม่ครอบคลุม** → **เติม ampicillin** · Gram stain ของ Listeria มักลบ\n\n- gentamicin ใช้ร่วมกับ ampicillin ไม่ใช้เดี่ยว\n- metronidazole/clindamycin ไม่คลุม Listeria ใน CNS\n- acyclovir อาจเติมถ้าสงสัย HSV แต่ต้องไม่ตัดยาต้านแบคทีเรีย",
   pearl="อายุ > 50 / ภูมิต่ำ / ตั้งครรภ์ → + ampicillin", ref=["สไลด์ Microorganism 2026 — Listeria monocytogenes"], nl=["B3.2.2(1)", "B1.7.2"]),
  dict(id="ID-MIC-MCQ-10", topic="Cutaneous anthrax",
   stem="A goat farmer has a painless black eschar on the neck surrounded by marked non-pitting edema. A Gram stain of the exudate shows large Gram-positive rods with square ends arranged in chains. Which is the most appropriate treatment?",
   choices=["Oral ciprofloxacin", "Surgical excision of the eschar", "Doxycycline for scrub typhus for 3 days only", "Amphotericin B", "Cloxacillin"],
   explain="แผลดำไม่เจ็บ + บวมมาก + **boxcar GPR** = **cutaneous anthrax** → **ciprofloxacin หรือ doxycycline** 7–10 วัน\n\n- **ห้ามผ่าตัด** เพราะอาจทำให้กระจาย\n- eschar ของ scrub typhus เล็ก ไม่บวมรอบ และเชื้อเห็นใน Gram stain ไม่ได้\n- amphotericin ใช้กับ mucormycosis\n- cloxacillin ไม่ใช่ยาหลักของ anthrax",
   pearl="Anthrax: cipro/doxy · ไม่ผ่าตัด", ref=["สไลด์ Microorganism 2026 — Quiz 7"], nl=["2.3.1-3(9)", "B1.5.2(8)"]),
 ]))

# ---------------------------------------------------------------- 6
S.append(dict(
 id="id-mic-06", title="Quiz 8 · Gram-negative bacilli: Vibrio, Salmonella, เชื้อจากสัตว์กัด และฝีในตับ",
 summary="ตับแข็ง + น้ำทะเล + hemorrhagic bullae + GN curved rod = V. vulnificus · Salmonella Typhi/nontyphi (gr C choleraesuis → หลอดเลือด) · หมาแมวกัด: Pasteurella, Capnocytophaga · ฝีในตับ: amoeba vs Klebsiella vs melioid",
 minutes=11, nl=["2.3.11(8)", "B8.2.2(6)", "2.3.1(21)", "2.3.1(16)", "2.2.50", "B1.5.2(8)"],
 md="""### Quiz 8 — ผู้ป่วยตับแข็ง มือบวมแดง ปวด 2 วัน
[[img:mic-q08-bullae]]
[[img:mic-q08-pus]]

### *Vibrio vulnificus*
- **GN curved rod** · อยู่ใน **น้ำทะเล น้ำกร่อย อาหารทะเลดิบ (หอยนางรม)**
- เสี่ยงสูงใน **ตับแข็ง ติดสุรา ธาลัสซีเมีย (เหล็กเกิน)** — ผู้สอนย้ำว่าโจทย์จะให้ **ดื่มสุรา/ตับแข็ง** มาเสมอ ร่วมกับ **ลุยน้ำกร่อย เที่ยวทะเล กินอาหารทะเล** (เชื้อชอบเกลือ)
- **hemorrhagic bullae สีม่วงคล้ำ** + **necrotizing fasciitis** + septic shock ภายในวัน
- ยา: **ceftazidime (หรือ ceftriaxone) + doxycycline** · **debridement เร่งด่วน**
- *Aeromonas* — น้ำจืด · ท้องเสีย · แผลติดเชื้อหลังโดนน้ำ/ปลิง

### *Salmonella*
| | Typhoid (*S.* Typhi, Paratyphi) | Nontyphoidal *Salmonella* |
|---|---|---|
| คลินิก | **ไข้นาน (FUO)** ปวดท้อง ผื่น rose spots · กลับจากอินเดีย/เนปาล | ท้องเสีย ไข้ ปวดท้อง (อาหาร ไข่ เนื้อดิบ) |
| ตรวจ | **hemoculture** · bone marrow culture ไวสุด | stool culture |
| แทรกซ้อน | **ลำไส้ทะลุ** เลือดออก ถุงน้ำดีอักเสบ encephalopathy | bacteremia · **gr C *S.* Choleraesuis → หลอดเลือดติดเชื้อ (mycotic aneurysm)** · osteomyelitis |

### สัตว์กัด — ผู้สอน: **ออกบ่อย**
- ***Pasteurella multocida*** — **แมว** (และหมา) กัด → cellulitis เร็วภายใน 24 ชม. · **amoxicillin–clavulanate** · **ดื้อ cloxacillin, cephalosporin รุ่น 1, clindamycin**
- ***Capnocytophaga canimorsus*** — **หมากัด** + **ไม่มีม้าม/ติดสุรา** → sepsis, **purpura fulminans**, DIC, meningitis · amox-clav / ceftriaxone

### ฝีในตับ — แยกด้วยภาพและปัจจัยเสี่ยง
> **ผู้สอน:** melioidosis ใช้ **ceftazidime ไม่ใช่ ceftriaxone** (เชื้อเป็นญาติ *Pseudomonas*) · amoeba ใช้ **metronidazole** · ข้อสอบอาจถามชื่อเชื้อ ชื่อยา หรือให้บรรยาย Gram stain/ลักษณะหนอง

| เชื้อ | ภาพ | ประเด็นสำคัญ | ยา |
|---|---|---|---|
| ***Entamoeba histolytica*** | **โพรงเดียวขนาดใหญ่** กลีบขวา | ไม่สัมพันธ์กับเบาหวาน · หนองสีช็อกโกแลต (anchovy paste) | **metronidazole** แล้วตาม **paromomycin** |
| ***Klebsiella pneumoniae*** | เดียวหรือหลายช่อง **รังผึ้ง / Swiss cheese** | **เบาหวาน** · hypervirulent → endophthalmitis | ceftriaxone + ระบาย |
| ***B. pseudomallei*** | **หลายห้องหลายตำแหน่ง** ตับและ **ม้าม** | **เบาหวาน** ทำนา · bipolar staining | ceftazidime/meropenem → co-trimoxazole |""",
 pearls=["ตับแข็ง + ทะเล + hemorrhagic bullae = V. vulnificus → ceftazidime + doxy + debride", "Typhoid = ไข้นาน · hemoculture/bone marrow · gr C Choleraesuis → mycotic aneurysm", "แมวกัด → Pasteurella (amox-clav) · หมากัด + ไม่มีม้าม → Capnocytophaga", "ฝีตับ: amoeba โพรงเดี่ยวไม่เกี่ยว DM · Klebsiella/melioid เกี่ยว DM · melioid มีม้าม"],
 imgs=dict([
  im("mic-q08-bullae", "Quiz 8 — มือบวมแดงมีตุ่มพองเลือด", "มือทั้งสองข้างบวม มีตุ่มพองสีม่วงคล้ำขนาดใหญ่ที่ฝ่ามือและหลังมือ",
     "ผู้ป่วยชายตับแข็ง มือบวมแดง ปวด 2 วัน — ถามประวัติอะไรเพิ่ม",
     "**Hemorrhagic bullae บนฐานแดง** ในผู้ป่วย **ตับแข็ง** → ถาม **สัมผัสน้ำทะเล/น้ำกร่อย แผลจากก้างปลา กินอาหารทะเลดิบ** · สงสัย ***Vibrio vulnificus*** necrotizing soft tissue infection"),
  im("mic-q08-pus", "Quiz 8 — Pus Gram stain", "เชื้อแท่งสั้นติดสีชมพูโค้งเล็กน้อยจำนวนมาก",
     "หนองจากตุ่มพอง — บรรยาย วินิจฉัย และรักษา",
     "**บรรยาย:** **Gram-negative curved rods** · **วินิจฉัย:** necrotizing fasciitis / septicemia จาก ***Vibrio vulnificus*** · **รักษา:** **ceftazidime (หรือ ceftriaxone) + doxycycline** ร่วมกับ **surgical debridement ด่วน** · ประคับประคองภาวะช็อก"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-11", topic="Vibrio vulnificus",
   stem="A 58-year-old man with alcoholic cirrhosis cut his hand while cleaning shellfish 1 day ago. He now has hypotension and painful violaceous hemorrhagic bullae spreading up the forearm. Which regimen is most appropriate in addition to urgent surgical debridement?",
   choices=["Ceftazidime plus doxycycline", "Cloxacillin alone", "Amoxicillin–clavulanate orally", "Metronidazole plus gentamicin", "Fluconazole"],
   explain="ตับแข็ง + อาหารทะเล + **hemorrhagic bullae** + ช็อก = ***V. vulnificus*** → **ceftazidime (3rd-gen cephalosporin) + doxycycline** + debridement\n\n- cloxacillin คลุมแค่ GP\n- ยากินไม่พอในรายช็อก\n- metronidazole + gentamicin ไม่ใช่สูตรมาตรฐานของ Vibrio\n- fluconazole เป็นยาเชื้อรา",
   pearl="Vibrio: ceftazidime + doxy + ผ่าตัด", ref=["สไลด์ Microorganism 2026 — Quiz 8"], nl=["2.2.50", "B5.2.2(1)"]),
  dict(id="ID-MIC-MCQ-12", topic="Liver abscess differential",
   stem="A 35-year-old man without diabetes has fever and right upper quadrant pain. Ultrasound shows a single large abscess in the right lobe of the liver. Aspiration yields odorless brown 'anchovy paste' material with no organisms on Gram stain. What is the treatment of choice?",
   choices=["Metronidazole followed by a luminal agent (paromomycin)", "Ceftazidime for 2 weeks then co-trimoxazole for 3 months", "Ceftriaxone plus percutaneous drainage only", "Praziquantel", "Amphotericin B"],
   explain="**โพรงเดียวใหญ่ + ไม่มีเบาหวาน + หนองสีช็อกโกแลตไม่มีกลิ่น ไม่เห็นเชื้อ** = **amoebic liver abscess** → **metronidazole 750 mg × 7–10 วัน** แล้วตามด้วย **paromomycin** กำจัด cyst ในลำไส้\n\n- ceftazidime → co-trimoxazole เป็นสูตร melioidosis (หลายห้อง เบาหวาน)\n- ceftriaxone + ระบายเหมาะกับ Klebsiella\n- praziquantel ใช้กับพยาธิใบไม้",
   pearl="Amoebic abscess: โพรงเดี่ยว ไม่เกี่ยว DM → metronidazole + paromomycin", ref=["บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — ฝีในตับ", "สไลด์ Microorganism 2026 — Entamoeba histolytica"], nl=["2.3.11(8)", "B8.2.2(6)"]),
  dict(id="ID-MIC-MCQ-13", topic="Cat bite infection",
   stem="A woman develops rapidly spreading cellulitis within 12 hours of a cat bite on her hand. Which oral antibiotic is most appropriate?",
   choices=["Amoxicillin–clavulanate", "Cephalexin", "Cloxacillin", "Clindamycin alone", "Erythromycin"],
   explain="แมวกัด + cellulitis เร็ว = ***Pasteurella multocida*** → **amoxicillin–clavulanate**\n\n- Pasteurella **ดื้อ cloxacillin, cephalosporin รุ่น 1 (cephalexin), clindamycin และ erythromycin** (ตามสไลด์)",
   pearl="หมาแมวกัด = amox-clav", ref=["สไลด์ Microorganism 2026 — Pasteurella multocida & Capnocytophaga"], nl=["2.3.12(4)", "B1.5.2(8)"]),
 ]))

# ---------------------------------------------------------------- 7
S.append(dict(
 id="id-mic-07", title="Quiz 9–10 · Nocardia กับ Actinomyces, anaerobes และ botulism",
 summary="เส้นใยแตกแขนงเป็นลูกปัด GP + modified AFB บวก + ภูมิต่ำ = Nocardia → co-trimoxazole · Actinomyces ไม่ใช้ O₂ ฝีใบหน้าลำคอ → amoxicillin · ชาเฉียบพลันหลังกินอาหารกระป๋อง + GPR มี spore = botulism → antitoxin",
 minutes=9, nl=["3.1.9", "B1.5.2(5)", "2.3.1(3)", "B3.2.2(5)", "2.3.1-3(6)"],
 md="""### Quiz 9 — หญิง 41 ปี SLE ได้ prednisolone 1 mg/kg/วัน + cyclophosphamide ไข้ ไอ เหนื่อย 2 สัปดาห์
[[img:mic-q09-gram]]
[[img:mic-q09-mafb]]

### Higher bacteria — เส้นใยแตกแขนง Gram บวก
| | ***Nocardia*** | ***Actinomyces*** |
|---|---|---|
| ออกซิเจน | **aerobe** | **anaerobe** |
| ย้อม | GP **beaded branching filaments** · **modified AFB บวก** (partially acid-fast) | GP แตกแขนง · **AFB ลบ** · **sulfur granules** |
| จำแบบผู้สอน | **ติดทั้ง Gram และ mAFB (2 ภาพ)** | **ติด Gram อย่างเดียว (1 ภาพ)** |
| ผู้ป่วย | **ภูมิต่ำ: steroid, HIV, ปลูกถ่าย** | คนปกติ ฟันผุ ใส่ IUD |
| โรค | **ฝีในปอดและสมอง** | **ฝีบริเวณใบหน้าลำคอ (lumpy jaw)** ทะลุเป็นโพรง · ช่องท้อง เชิงกราน |
| ยา | **co-trimoxazole (Bactrim)** · รายรุนแรง + imipenem/amikacin · CT สมองทุกราย | **amoxicillin / penicillin** ระยะยาว |

### เบาะแสว่าเป็น anaerobe
- Gram stain/เพาะเชื้อได้ **หลายเชื้อปนกัน**
- **มีแก๊ส** ในหนองหรือเนื้อเยื่อ
- **หนองเหม็น**
- **เนื้อตาย**
- ติดเชื้อ **ใกล้เยื่อบุ** ที่มี anaerobe ประจำถิ่น

| GN anaerobes | GP anaerobes |
|---|---|
| ***Bacteroides*** ฝีในช่องท้อง · *Fusobacterium* ฝี ปอด สมอง · *Porphyromonas* aspiration ปริทันต์ · *Prevotella* | *Actinomyces* · ***Clostridium*** · *Peptostreptococcus* · *Cutibacterium (Propionibacterium)* อุปกรณ์ในร่างกาย |

***Clostridium*** — *C. perfringens* gas gangrene และอาหารเป็นพิษ · ***C. botulinum* botulism** · *C. tetani* tetanus · *C. difficile* pseudomembranous colitis

### Quiz 10 — อ่อนแรง หายใจขัด 2 ชม. หลังกินอาหารกระป๋อง
[[img:mic-q10-hemo]]

### Botulism
- toxin ยับยั้งการหลั่ง **acetylcholine** ที่ปลายประสาท → **อ่อนแรงแบบ descending, symmetric** เริ่มที่ **ตา (หนังตาตก เห็นภาพซ้อน รูม่านตาขยาย) ปาก คอ (กลืนลำบาก พูดไม่ชัด)** → แขนขา → **หายใจล้มเหลว** · **ไม่มีไข้ รู้สึกตัวดี ชาไม่เสีย**
- แหล่ง: **หน่อไม้ปี๊บ (เคยระบาดที่น่าน) อาหารกระป๋อง/หมักดองไม่ได้มาตรฐาน** 
- รักษา: **antitoxin ให้เร็วที่สุด** · **ดูแลการหายใจ** (vital capacity, ใส่ท่อ) · foodborne **ไม่ให้ยาปฏิชีวนะ** (ยกเว้น wound botulism) · **เลี่ยง aminoglycoside**""",
 pearls=["Nocardia: aerobe · beaded branching · mAFB บวก · ภูมิต่ำ · ฝีปอด+สมอง → Bactrim", "Actinomyces: anaerobe · AFB ลบ · sulfur granules · ฝีใบหน้าลำคอ → amoxicillin", "Botulism: descending paralysis เริ่มที่ตา ไม่มีไข้ → antitoxin + ดูแลหายใจ"],
 imgs=dict([
  im("mic-q09-gram", "Quiz 9 — Sputum Gram stain", "เส้นใยบางติดสีม่วงแตกแขนงยาวคดเคี้ยวปนเม็ดเลือดขาว",
     "หญิง 41 ปี SLE ได้ steroid ขนาดสูง + cyclophosphamide ไข้ ไอ เหนื่อย 2 สัปดาห์ — บรรยายภาพนี้",
     "**Gram-positive, beaded, branching filamentous bacteria** — ย้อม modified AFB ต่อ (ภาพถัดไป)"),
  im("mic-q09-mafb", "Quiz 9 — Modified AFB stain", "เส้นใยบางสีแดงแตกแขนงบนพื้นเขียว มีลูกศรชี้",
     "เสมหะเดียวกันย้อม modified acid-fast — วินิจฉัย และรักษา",
     "**บรรยาย:** เส้นใยแตกแขนง **ติดสี modified AFB (partially acid-fast)** · **วินิจฉัย:** **pulmonary nocardiosis** (*Nocardia* spp.) ในผู้ป่วยภูมิคุ้มกันต่ำ · **รักษา:** **co-trimoxazole (TMP-SMX)** ขนาดสูง ± imipenem/amikacin ถ้ารุนแรง · **ทำ CT/MRI สมองหาฝี** · ระยะยาว ≥ 6–12 เดือน"),
  im("mic-q10-hemo", "Quiz 10 — Gram stain", "เชื้อแท่งติดสีม่วงจำนวนมาก บางตัวมีส่วนใสรูปไข่ที่ปลาย",
     "ผู้ป่วยชาย อ่อนแรง หายใจขัด 2 ชม. หลังกินอาหารกระป๋อง — บรรยาย วินิจฉัย และรักษา",
     "**บรรยาย:** Gram-positive rods **with (subterminal) spores** · **วินิจฉัย:** **foodborne botulism** (*Clostridium botulinum*) — descending flaccid paralysis หลังกินอาหารกระป๋อง · **รักษา:** **botulinum antitoxin โดยเร็ว** + ดูแลทางหายใจ/ใส่ท่อ · ไม่ให้ยาปฏิชีวนะใน foodborne · เลี่ยง aminoglycoside"),
 ]),
 items=[
  dict(id="ID-MIC-MCQ-14", topic="Nocardia vs Actinomyces",
   stem="A kidney transplant recipient has a cavitating lung lesion. Sputum shows Gram-positive beaded branching filaments that stain with the modified acid-fast method. Which is the treatment of choice, and what additional imaging is mandatory?",
   choices=["Co-trimoxazole; brain imaging", "Amoxicillin; sinus CT", "Isoniazid, rifampicin, pyrazinamide and ethambutol; chest CT only", "Amphotericin B; echocardiography", "Penicillin G; abdominal ultrasound"],
   explain="เส้นใยแตกแขนง GP + **modified AFB บวก** + ภูมิต่ำ = ***Nocardia*** → **co-trimoxazole** · Nocardia ชอบกระจายไป **สมอง** จึงต้องทำ **CT/MRI สมองทุกราย**\n\n- amoxicillin/penicillin เป็นยา *Actinomyces* (AFB ลบ anaerobe)\n- ยาวัณโรคใช้กับ *M. tuberculosis* ซึ่งเป็นแท่ง ไม่แตกแขนง\n- amphotericin เป็นยาเชื้อรา",
   pearl="Nocardia = Bactrim + ดูสมอง", ref=["สไลด์ Microorganism 2026 — Higher bacteria"], nl=["3.1.9", "2.3.1-3(6)"]),
  dict(id="ID-MIC-MCQ-15", topic="Foodborne botulism",
   stem="Six villagers develop ptosis, diplopia, dysphagia and descending weakness 18 hours after eating home-canned bamboo shoots. They are afebrile and alert with intact sensation. Besides airway support, what is the most important specific treatment?",
   choices=["Botulinum antitoxin", "Penicillin G", "Gentamicin", "Intravenous immunoglobulin", "Pyridostigmine"],
   explain="Descending symmetric paralysis เริ่มที่ตา ไม่มีไข้ หลังกิน **หน่อไม้อัดปี๊บ** = **foodborne botulism** → **antitoxin ให้เร็วที่สุด** (จับ toxin ที่ยังไม่เข้าปลายประสาท)\n\n- foodborne ไม่ต้องให้ยาปฏิชีวนะ\n- **aminoglycoside ทำให้ neuromuscular blockade แย่ลง**\n- IVIG ใช้ใน GBS (ascending)\n- pyridostigmine ใช้ใน myasthenia gravis",
   pearl="Botulism = antitoxin + ดูแลหายใจ", ref=["สไลด์ Microorganism 2026 — Quiz 10"], nl=["2.3.1(3)", "B3.2.2(5)"]),
 ]))
