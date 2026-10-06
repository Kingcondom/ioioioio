from lib import lecture, sec, mcq, fig

D = "สไลด์ Update ข้อสอบ 2025"
SRC = "NL2 2025 (update)"

def R(*p):
    return [f"{D} หน้า " + ", ".join(str(x) for x in p)]

# ---------------------------------------------------------------- 07-01 CNS infection
F_CSF = fig("exam25-07-01-f1", "อ่าน CSF ให้เร็ว: cell type × น้ำตาล", '''<svg viewBox="0 0 720 300">
 <rect x="150" y="10" width="270" height="34" rx="8" class="sunk"/>
 <text x="285" y="32" text-anchor="middle" class="tb">น้ำตาล CSF ต่ำ</text>
 <rect x="440" y="10" width="270" height="34" rx="8" class="sunk"/>
 <text x="575" y="32" text-anchor="middle" class="tb">น้ำตาล CSF ปกติ</text>
 <rect x="10" y="56" width="130" height="110" rx="8" class="c2"/>
 <text x="75" y="106" text-anchor="middle" class="tw">PMN เด่น</text>
 <text x="75" y="126" text-anchor="middle" class="tw">WBC 50–5,000</text>
 <rect x="150" y="56" width="270" height="110" rx="10" class="badsoft"/>
 <text x="285" y="84" text-anchor="middle" class="tb">Bacterial meningitis</text>
 <text x="285" y="106" text-anchor="middle" class="t2">ขุ่น · protein สูงมาก</text>
 <text x="285" y="126" text-anchor="middle" class="t2">G/S: GN diplococci = meningococcus</text>
 <text x="285" y="148" text-anchor="middle" class="ta">ceftriaxone</text>
 <rect x="440" y="56" width="270" height="110" rx="10" class="box"/>
 <text x="575" y="100" text-anchor="middle" class="t2">(ระยะแรกของ viral อาจ PMN เด่นได้)</text>
 <rect x="10" y="176" width="130" height="114" rx="8" class="c1"/>
 <text x="75" y="226" text-anchor="middle" class="tw">Mono เด่น</text>
 <text x="75" y="246" text-anchor="middle" class="tw">(lymphocyte)</text>
 <rect x="150" y="176" width="270" height="114" rx="10" class="misssoft"/>
 <text x="285" y="200" text-anchor="middle" class="tb">TB · Cryptococcus</text>
 <text x="285" y="222" text-anchor="middle" class="t2">TB: subacute, protein สูงมาก,</text>
 <text x="285" y="240" text-anchor="middle" class="t2">CSF/serum sugar &lt; 30%, ADA สูง</text>
 <text x="285" y="262" text-anchor="middle" class="t2">Crypto: HIV CD4 &lt; 100, OP สูงมาก</text>
 <text x="285" y="280" text-anchor="middle" class="t3">(Eosinophil &gt; 10% = parasite)</text>
 <rect x="440" y="176" width="270" height="114" rx="10" class="oksoft"/>
 <text x="575" y="208" text-anchor="middle" class="tb">Viral meningitis</text>
 <text x="575" y="232" text-anchor="middle" class="t2">ใส · protein สูงเล็กน้อย</text>
 <text x="575" y="254" text-anchor="middle" class="t2">WBC 5–500</text>
</svg>''', "เริ่มจากชนิดเซลล์ (แถวซ้าย) แล้วดูน้ำตาล (คอลัมน์บน) — lymphocyte เด่นที่น้ำตาลต่ำคือ TB หรือเชื้อรา ไม่ใช่ไวรัส")

S1 = sec("exam25-07-01", "CNS infections",
    "Meningococcus → ceftriaxone · subacute + ADA สูง = TBM · HIV CD4 < 100 + ICP สูง = crypto · calcified cysts = T. solium · CD4 < 50 + retinitis = CMV", minutes=7,
    source=f"{D} หน้า 5–13, 20–21", nl=["2.3.6(5)", "2.3.6(1)", "2.3.1-3(8)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

[[fig:exam25-07-01-f1]]

**CSF (ตารางสไลด์)**

| | Bacteria | Virus | TB | Fungus | Parasite |
|---|---|---|---|---|---|
| OP | ↑↑ | ↔/↑ | ↑↑ | **↑↑↑** | ↑↑ |
| สี | ขุ่น | ใส | เหลือง/ขุ่น | ใส/ขุ่น | ขุ่น, xanthochromia |
| WBC | 50–5,000 | 5–500 | 25–500 | 5–100 | > 5 |
| เซลล์เด่น | **PMN** | Mono | Mono | Mono | **Eosinophil > 10%** |
| Protein | > 100–1,000 | 50–100 | **100–5,000** | 20–500 | > 60 |
| CSF/serum sugar | ↓ | ↔ | **< 30%** | ↔/↓ | ↔/↓ |

**จุดจำของแต่ละโจทย์ (สไลด์)**
- **N. meningitidis**: G/S **gram-negative diplococci** · Tx **ceftriaxone/cefotaxime**
- **TB meningitis**: subacute, protein สูง น้ำตาลต่ำ **ADA สูง** culture ลบ
- **Cryptococcal meningitis**: HIV **CD4 < 100** · ปวดหัว ตามัว **papilledema** (OP สูงมาก) CT ไม่มีก้อน
- **CMV encephalitis**: **CD4 < 50** · ชัก ซึม CN palsy · **CMV retinitis** · MRI **periventricular** · Tx **ganciclovir + foscarnet**
- **Neurocysticercosis (T. solium)** ระยะ **calcified**: Tx **steroid (ถ้า ICP สูง) + antiepileptic ไม่ต้องให้ยาฆ่าพยาธิ**
''',
    figs=[F_CSF],
    pearls=[
        "Meningococcal meningitis → ceftriaxone/cefotaxime",
        "Lymphocyte + น้ำตาลต่ำมาก + protein สูง + ADA สูง = TBM",
        "HIV CD4 < 100 + papilledema + CT ปกติ = cryptococcal meningitis",
        "CMV: CD4 < 50, retinitis, periventricular → ganciclovir + foscarnet",
        "Calcified NCC → AED ± steroid ไม่ต้อง albendazole",
    ],
    items=[
        mcq("EXAM25-07-01-1",
            "A 22-year-old college student presents with fever, neck stiffness and altered mental status. CSF analysis confirms Neisseria meningitidis meningitis. What is the antibiotic of choice?",
            "Ceftriaxone",
            ["Penicillin G", "Vancomycin", "Ampicillin", "Meropenem"],
            kind="old", src=SRC,
            explain='''Meningococcal meningitis (CSF: PMN เด่น protein สูง น้ำตาลต่ำ G/S gram-negative diplococci) → **ceftriaxone (หรือ cefotaxime)** ตามสไลด์ ผ่าน BBB ได้ดีและครอบคลุมสายพันธุ์ที่ดื้อ penicillin บางส่วน
- Penicillin G ใช้ได้เมื่อทราบผลความไวแล้ว แต่ไม่ใช่ยาที่ข้อสอบเลือก
- Vancomycin เพิ่มเพื่อครอบคลุม pneumococcus ที่ดื้อยา ไม่จำเป็นเมื่อรู้ว่าเป็น meningococcus
- Ampicillin เพิ่มเพื่อครอบคลุม Listeria ในผู้สูงอายุ > 50 ปี/ภูมิคุ้มกันต่ำ
- Meropenem ใช้ใน nosocomial/เชื้อดื้อยา กว้างเกินจำเป็น''',
            pearl="Meningococcal meningitis → ceftriaxone", topic="Bacterial meningitis",
            ref=R(5, 6), nl=["2.3.6(5)"]),
        mcq("EXAM25-07-01-2",
            "A 40-year-old man presents with 3 weeks of fever and headache. CSF shows a lymphocytic pleocytosis, low glucose, high protein and elevated adenosine deaminase (ADA). Bacterial culture is negative. What is the most likely diagnosis?",
            "Tuberculous meningitis",
            ["Bacterial meningitis", "Viral meningitis", "Cryptococcal meningitis", "Carcinomatous meningitis"],
            kind="old", src=SRC,
            explain='''อาการ **subacute** + CSF **น้ำตาลต่ำ protein สูง** + **ADA สูง** + bacterial culture ลบ = **tuberculous meningitis** (สไลด์ไม่ได้ระบุชนิดเซลล์และระยะเวลา จึงเติม "3 weeks" และ "lymphocytic" ตามความหมายของ subacute เพื่อให้ตัวเลือกแยกได้)
- Bacterial meningitis เป็นเฉียบพลัน PMN เด่น และ culture มักขึ้น
- Viral meningitis น้ำตาลปกติ protein สูงเล็กน้อย
- Cryptococcal meningitis ก็น้ำตาลต่ำได้ แต่มักเป็นใน HIV และ ADA ไม่สูง ยืนยันด้วย India ink/CrAg
- Carcinomatous meningitis มีประวัติมะเร็ง ยืนยันด้วย CSF cytology''',
            pearl="Subacute + น้ำตาลต่ำ + ADA สูง = TBM", topic="TB meningitis",
            ref=R(7, 8, 9), nl=["2.3.6(5)", "B3.2.2(1)"]),
        mcq("EXAM25-07-01-3",
            "A 26-year-old HIV-positive man presents with headache, nausea, blurred vision and neck stiffness. CD4 count is 80 cells/mm³. CT brain shows no mass lesion. Fundoscopy reveals papilledema. What is the most likely diagnosis?",
            "Cryptococcal meningitis",
            ["Cerebral toxoplasmosis", "Bacterial meningitis", "HSV encephalitis", "CMV encephalitis"],
            kind="old", src=SRC,
            explain='''HIV **CD4 < 100** + ปวดหัว คอแข็ง ตามัว + **papilledema** (opening pressure สูงมาก) + **CT ไม่มีก้อน** = **cryptococcal meningitis** → LP วัด OP, CrAg/India ink
- Toxoplasmosis ทำให้ **ring-enhancing lesions** หลายก้อนใน CT
- Bacterial meningitis เป็นเฉียบพลัน ไข้สูง ไม่ใช่ลักษณะเด่นของ HIV CD4 ต่ำ
- HSV encephalitis มี AOC ชัก พฤติกรรมเปลี่ยน temporal lobe lesion
- CMV encephalitis เกิดที่ CD4 < 50 มี periventricular change และ retinitis''',
            pearl="HIV CD4 < 100 + ICP สูง + CT ปกติ = crypto meningitis", topic="Cryptococcal meningitis",
            ref=R(10, 11), nl=["2.3.1-3(7)", "2.3.1(9)"]),
        mcq("EXAM25-07-01-4",
            "A 30-year-old man presents with headache and convulsions. Temperature 36.8 °C, pulse 86/min, BP 110/70 mmHg. Neurological examination reveals no motor or sensory deficit. CT brain shows multiple calcified cystic lesions. What is the most likely causative pathogen?",
            "Taenia solium",
            ["Toxoplasma gondii", "Gnathostoma spinigerum", "Angiostrongylus cantonensis", "Mycobacterium tuberculosis"],
            kind="old", src=SRC,
            explain='''ชัก + ไม่มีไข้ + **multiple calcified cystic lesions** = **neurocysticercosis ระยะ calcified** จาก **Taenia solium** (กินไข่พยาธิตืดหมู) → AED ± steroid ไม่ต้องให้ยาฆ่าพยาธิในระยะนี้
- Toxoplasma ทำให้ ring-enhancing lesions ในคนภูมิคุ้มกันต่ำ (calcification พบใน congenital)
- Gnathostoma ทำให้ eosinophilic myeloencephalitis มีเลือดออกในสมอง ปวดร้าวตามเส้นประสาท
- Angiostrongylus ทำให้ eosinophilic meningitis (CSF eosinophil > 10%) ไม่มี cyst
- TB ทำให้ tuberculoma (ring-enhancing) และ basal meningitis''',
            pearl="Calcified cysts หลายอันในสมอง + ชัก = T. solium", topic="Neurocysticercosis",
            ref=R(12, 13), nl=["2.3.1-3(8)", "2.3.6(9)"]),
        mcq("EXAM25-07-01-5",
            "A 45-year-old immunocompromised patient (HIV, CD4 30 cells/mm³) presents with confusion, nystagmus and diplopia. MRI shows periventricular white matter lesions. CSF PCR is positive for a neurotropic virus that also causes necrotizing retinitis in this population. What is the most likely diagnosis?",
            "CMV encephalitis",
            ["Progressive multifocal leukoencephalopathy", "Herpes simplex meningitis", "West Nile virus encephalitis", "Varicella-zoster vasculopathy"],
            kind="old", src=SRC,
            explain='''ภูมิคุ้มกันต่ำมาก (**CD4 < 50**) + AOC + CN palsy (nystagmus, diplopia) + **MRI periventricular** + ไวรัสที่ทำให้ **retinitis** = **CMV ventriculoencephalitis** → ganciclovir + foscarnet (สไลด์เขียน "immunocompromised" — เติม CD4 30 ให้ตรงกับ risk ที่สไลด์สรุป)
- PML (JC virus) ทำให้ white matter lesion ไม่ enhance ไม่มีไข้ และไม่ทำให้ retinitis
- HSV ทำให้ temporal lobe encephalitis ไม่ใช่ periventricular
- West Nile ไม่พบในไทย ทำให้ flaccid paralysis
- VZV vasculopathy ทำให้ stroke จาก vasculitis และ acute retinal necrosis ได้ แต่ภาพ MRI เป็น infarct ไม่ใช่ periventricular''',
            pearl="CD4 < 50 + periventricular + retinitis = CMV encephalitis", topic="CMV encephalitis",
            ref=R(20, 21), nl=["2.3.1-3(4)", "2.3.6(1)"]),
    ])

# ---------------------------------------------------------------- 07-02 Fever syndromes & parasites
S2 = sec("exam25-07-02", "Tropical fevers, EBV & Strongyloides",
    "ไข้ + conjunctival suffusion + น่อง + ดีซ่าน = leptospirosis · เจ็บคอ + LN + atypical lymph = EBV · steroid + larva currens = Strongyloides", minutes=5,
    source=f"{D} หน้า 40–45", nl=["2.3.1(13)", "2.3.1(10)", "2.3.1(12)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

| โรค | จุดจำ (สไลด์) | ตรวจ | รักษา |
|---|---|---|---|
| **Leptospirosis** | เกษตรกร ย่ำน้ำ · **conjunctival suffusion** · ปวดกล้ามเนื้อเด่นที่ **น่องและหลังล่าง** · ดีซ่าน AKI · WBC สูง PMN Plt ต่ำ | **MAT** | Mild: **doxycycline** · Severe: **IV PGS / ceftriaxone** |
| Scrub typhus (เทียบ) | **eschar**, ต่อมน้ำเหลืองโต | | doxycycline |
| **Infectious mononucleosis** | ไข้ **pharyngitis** ต่อมน้ำเหลืองคอโต (หลายตำแหน่งได้) · **atypical lymphocytes (Downey cells)** | heterophile Ab (เสริม) | **supportive** · ห้าม ampicillin (ผื่น) |
| **Strongyloides hyperinfection** | **immunocompromised (steroid ขนาดสูง)** · GI: ปวดท้อง ท้องเสีย · lung: pneumonitis · skin: **larva currens** | stool เห็น rhabditiform larva | **Ivermectin** |

> ก่อนเริ่ม steroid ขนาดสูงในคนจากพื้นที่ระบาด ควรตรวจ/ให้ ivermectin ป้องกัน Strongyloides (เสริม)
''',
    pearls=[
        "Conjunctival suffusion + ปวดน่อง + ดีซ่าน = leptospirosis",
        "Leptospirosis รุนแรง → PGS หรือ ceftriaxone · ไม่รุนแรง → doxycycline",
        "Downey cells + pharyngitis + LN = EBV → supportive",
        "Steroid + ท้องเสีย + ไอ + larva currens = Strongyloides → ivermectin",
    ],
    items=[
        mcq("EXAM25-07-02-1",
            "A 35-year-old woman with systemic lupus erythematosus treated with high-dose prednisone (1 mg/kg/day) presents with 2 weeks of watery diarrhea, epigastric pain and cough. She has serpiginous urticarial rashes over the buttocks and thighs. A stool sample shows rhabditiform larvae. Which parasite is most likely responsible?",
            "Strongyloides stercoralis",
            ["Ascaris lumbricoides", "Giardia lamblia", "Hookworm (Ancylostoma duodenale)", "Toxoplasma gondii"],
            kind="old", src=SRC,
            explain='''ได้ **steroid ขนาดสูง** + อาการ GI (ท้องเสีย ปวดลิ้นปี่) + ปอด (ไอ) + **ผื่นลมพิษคดเคี้ยวที่ก้นและต้นขา (larva currens)** + พบ **ตัวอ่อน (larva) ในอุจจาระ** = **Strongyloides hyperinfection** (autoinfection ทำให้พยาธิเพิ่มจำนวน) → **ivermectin** (สไลด์แสดงภาพ larva ในอุจจาระ)
- Ascaris พบ **ไข่** ในอุจจาระ ไม่ใช่ตัวอ่อน และไม่ทำ larva currens
- Giardia ทำให้ท้องเสียเป็นมัน แต่ไม่มีอาการปอดหรือผิวหนัง
- Hookworm พบไข่ในอุจจาระ ทำให้ IDA และ ground itch ที่เท้า
- Toxoplasma ไม่ทำให้ท้องเสียหรือ larva currens''',
            pearl="Steroid + larva ในอุจจาระ + larva currens = Strongyloides", topic="Strongyloidiasis",
            ref=R(40, 41), nl=["2.3.1(12)"]),
        mcq("EXAM25-07-02-2",
            "A 17-year-old boy presents with fever, sore throat and generalized lymphadenopathy for 10 days. There are enlarged cervical, axillary and inguinal lymph nodes; the spleen is not palpable. The peripheral blood smear shows atypical lymphocytes (Downey cells). What is the most likely cause?",
            "Epstein-Barr virus",
            ["Cytomegalovirus", "Acute HIV infection", "Toxoplasmosis", "Hodgkin lymphoma"],
            kind="old", src=SRC,
            explain='''วัยรุ่น + ไข้ + **pharyngitis** + ต่อมน้ำเหลืองโต + **atypical lymphocytes (Downey cells)** = **infectious mononucleosis จาก EBV** (สาเหตุที่พบบ่อยที่สุด) → supportive
- CMV ทำ mononucleosis-like ได้ แต่มักไม่มี pharyngitis และต่อมน้ำเหลืองโตน้อย
- Acute HIV ให้ไข้ เจ็บคอ ต่อมน้ำเหลืองโตได้ แต่มักมีผื่นและแผลในปาก และไม่ใช่ข้อที่เป็นไปได้มากที่สุดเมื่อไม่มีประวัติเสี่ยง
- Toxoplasmosis ทำต่อมน้ำเหลืองคอโตแต่ไม่ค่อยมี pharyngitis
- Hodgkin lymphoma ไม่ทำให้ Downey cells และไม่ใช่อาการเฉียบพลัน 10 วัน''',
            pearl="ไข้ + เจ็บคอ + LN + Downey cells = EBV", topic="Infectious mononucleosis",
            ref=R(42, 43), nl=["2.3.1(10)"]),
        mcq("EXAM25-07-02-3",
            "A rice farmer presents with 5 days of fever, headache, bilateral conjunctival suffusion, jaundice and severe calf myalgia. There is no rash or eschar. Hct 24%, WBC 15,000/mm³ (neutrophil predominance), platelets 100,000/μL. What is the most likely diagnosis?",
            "Leptospirosis",
            ["Scrub typhus", "Murine typhus", "Melioidosis", "Acute viral hepatitis"],
            kind="old", src=SRC,
            explain='''เกษตรกร (สัมผัสน้ำ/ปัสสาวะหนู) + ไข้ + **conjunctival suffusion** + **ปวดกล้ามเนื้อน่องรุนแรง** + **ดีซ่าน** + WBC สูง PMN เด่น เกล็ดเลือดต่ำ = **leptospirosis** (Weil disease) → ยืนยันด้วย MAT · รายรุนแรงให้ IV PGS/ceftriaxone
- Scrub typhus มี **eschar** และต่อมน้ำเหลืองโต (โจทย์บอกไม่มี eschar)
- Murine typhus อาการน้อยกว่า มีผื่น ไม่มีดีซ่าน/ปวดน่องเด่น
- Melioidosis มาด้วย pneumonia, abscess หลายที่ ในคนเป็นเบาหวาน
- Viral hepatitis ไม่ทำให้ conjunctival suffusion ปวดน่อง และ WBC สูง''',
            pearl="Conjunctival suffusion + ปวดน่อง + ดีซ่าน = leptospirosis", topic="Leptospirosis",
            ref=R(44, 45), nl=["2.3.1(13)"]),
    ])

# ---------------------------------------------------------------- 07-03 Candida & syphilis
S3 = sec("exam25-07-03", "Oral candidiasis & syphilis",
    "ICS ไม่บ้วนปาก → oral thrush · first-line = clotrimazole troche · secondary syphilis → VDRL/RPR, Tx benzathine PGS 2.4 MU", minutes=5,
    source=f"{D} หน้า 46–52", nl=["2.3.12(11)", "2.3.1(19)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Oral candidiasis vs OHL (สไลด์)**

| | Oral candidiasis | Oral hairy leukoplakia |
|---|---|---|
| เชื้อ | Candida albicans | EBV |
| ขูดออก | **ได้** (เห็นพื้นแดงข้างใต้) | ไม่ได้ (ขอบลิ้นด้านข้าง) |
| รักษา | **Topical antifungal: clotrimazole troche, nystatin** | ไม่ต้องรักษา |

- ปัจจัยเสี่ยง: **inhaled corticosteroid (ไม่บ้วนปาก)**, DM คุมไม่ได้, ฟันปลอม, ยาปฏิชีวนะ, HIV, steroid ระบบ
- รุนแรง/ลงหลอดอาหาร/ภูมิคุ้มกันต่ำมาก → **fluconazole** (เสริม)

**Syphilis**
- **Secondary**: ผื่น MP ทั่วตัว **รวมฝ่ามือฝ่าเท้า**, **condylomata lata**, ผมร่วงหย่อม (2–10 สัปดาห์หลัง chancre)
- ตรวจ: **Non-treponemal (RPR, VDRL)** ใช้คัดกรองและติดตามการรักษา · **Treponemal (TPHA, TPPA, FTA-ABS, EIA/CIA)** ใช้ยืนยัน
- รักษา (primary/secondary/early latent): **Benzathine penicillin G 2.4 MU IM ครั้งเดียว**
- Dark-field ใช้กับ **chancre** (primary) ไม่ใช่ผื่น
''',
    pearls=[
        "ICS + oral thrush → บ้วนปากหลังพ่นยา",
        "Oral thrush ไม่รุนแรง → clotrimazole troche (nystatin เป็นทางเลือก)",
        "ผื่นฝ่ามือฝ่าเท้า + เพศสัมพันธ์ไม่ป้องกัน = secondary syphilis → VDRL/RPR",
        "Early syphilis → benzathine PGS 2.4 MU IM ครั้งเดียว",
    ],
    items=[
        mcq("EXAM25-07-03-1",
            "A 60-year-old man with type 2 diabetes, autoimmune hepatitis (on prednisolone 5 mg/day and azathioprine) and COPD (on theophylline and a budesonide/formoterol inhaler) presents with creamy white oral patches that can be scraped off. Which medication is most likely the causative agent?",
            "Budesonide/formoterol inhaler",
            ["Prednisolone", "Azathioprine", "Metformin", "Theophylline"],
            kind="old", src=SRC,
            explain='''Oral candidiasis (คราบขาวขูดออกได้ — สไลด์แสดงภาพลิ้น) ที่สัมพันธ์กับยาโดยตรงมากที่สุดคือ **inhaled corticosteroid (budesonide)** ที่ตกค้างในช่องปากโดยไม่บ้วนปาก → แนะนำบ้วนปาก/ใช้ spacer
- Prednisolone (steroid ระบบ) เพิ่มความเสี่ยงได้ แต่ ICS สัมผัสเยื่อบุปากโดยตรงและเป็นคำตอบของข้อสอบ (โจทย์ใส่ขนาด prednisolone ต่ำเพิ่มเพื่อให้ตัดสินได้)
- Azathioprine กดไขกระดูก แต่ไม่ใช่สาเหตุหลักของ thrush
- Metformin ไม่ทำให้ candidiasis (DM คุมไม่ได้ต่างหากที่เสี่ยง)
- Theophylline ไม่เกี่ยวข้อง''',
            pearl="ICS ไม่บ้วนปาก → oral thrush", topic="Oral candidiasis",
            ref=R(46, 47), nl=["2.3.12(11)"]),
        mcq("EXAM25-07-03-2",
            "A 45-year-old woman with poorly controlled diabetes presents with painful white plaques on her tongue and buccal mucosa that can be scraped off, leaving an erythematous base. She is diagnosed with oral candidiasis. There is no odynophagia. What is the most appropriate first-line treatment?",
            "Clotrimazole troche",
            ["Fluconazole oral tablet", "Intravenous amphotericin B", "Chlorhexidine mouthwash", "Gentian violet paint"],
            kind="old", src=SRC,
            explain='''Oral candidiasis ไม่รุนแรง ไม่ลงหลอดอาหาร → **topical antifungal** โดยสไลด์เลือก **clotrimazole troche** (อมละลาย 5 ครั้ง/วัน 7–14 วัน)
- Fluconazole ใช้ในรายปานกลาง–รุนแรง กลืนเจ็บ (esophageal) หรือภูมิคุ้มกันต่ำมาก
- Amphotericin B IV ใช้ใน invasive/systemic candidiasis
- Chlorhexidine ใช้ทำความสะอาดช่องปาก ไม่ใช่ยาฆ่าเชื้อราหลัก
- Gentian violet เป็นยาทาเก่า ใช้น้อยแล้ว
(ตัวเลือก nystatin suspension ในสไลด์ถูกเอาออกและแทนด้วย gentian violet เพราะ nystatin ก็เป็น topical first-line ทำให้มีคำตอบถูกสองข้อ)''',
            pearl="Oral thrush ไม่รุนแรง → clotrimazole troche", topic="Oral candidiasis",
            ref=R(48, 49, 50), nl=["2.3.12(11)"]),
        mcq("EXAM25-07-03-3",
            "A 28-year-old man presents with a generalized maculopapular rash involving the trunk, palms and soles. He reports unprotected sexual intercourse 2 months ago. Which is the most appropriate diagnostic test at this stage?",
            "VDRL",
            ["Dark-field microscopy", "HIV ELISA", "Gram stain", "Antinuclear antibody"],
            kind="old", src=SRC,
            explain='''ผื่น MP ทั่วตัว **รวมฝ่ามือฝ่าเท้า** 2 เดือนหลังเพศสัมพันธ์ไม่ป้องกัน = **secondary syphilis** → ตรวจ **non-treponemal test (VDRL/RPR)** ซึ่งระยะนี้ titer สูงเกือบ 100% แล้วยืนยันด้วย treponemal test · รักษา benzathine PGS 2.4 MU IM ครั้งเดียว
- Dark-field microscopy ใช้ตรวจ chancre ระยะ primary ซึ่งมีเชื้อจำนวนมาก
- HIV ELISA ควรตรวจคู่กันทุกราย แต่ไม่ได้วินิจฉัยผื่นนี้
- Gram stain ไม่เห็น Treponema
- ANA ใช้กับ SLE''',
            pearl="ผื่นฝ่ามือฝ่าเท้า + เสี่ยงทางเพศ → VDRL/RPR", topic="Secondary syphilis",
            ref=R(51, 52), nl=["2.3.1(19)"]),
    ])

LECTURE = lecture("07", "Infectious", "CNS infection · leptospirosis · EBV · Strongyloides · thrush · syphilis",
    objectives=[
        "อ่าน CSF แยก bacterial, TB, fungal, viral และ parasite",
        "จับ pattern CNS infection ใน HIV ตามระดับ CD4",
        "แยก leptospirosis จาก rickettsia และจำการรักษา",
        "รักษา oral candidiasis และเลือกการตรวจ syphilis ตามระยะ",
    ],
    sections=[S1, S2, S3])
