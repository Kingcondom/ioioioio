from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Neuro"

# ---------------------------------------------------------------- 04-01 Bacterial meningitis
F_LP = fig("neuro-04-01-f1", "Suspected bacterial meningitis: ต้อง CT ก่อน LP ไหม", '''<svg viewBox="0 0 740 330">
 <defs><marker id="neuro-04-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="220" y="10" width="300" height="46" rx="10" class="acsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">ไข้ + ปวดหัว + คอแข็ง</text>
 <text x="370" y="48" text-anchor="middle" class="t3">H/C 2 ขวด + blood glucose ทันที</text>
 <path d="M370 56V76" class="ln" marker-end="url(#neuro-04-01-a)"/>
 <rect x="150" y="78" width="440" height="102" rx="10" class="misssoft"/>
 <text x="370" y="100" text-anchor="middle" class="tb">มีข้อใดข้อหนึ่ง?</text>
 <text x="166" y="124" class="t2">• Focal neurodeficit</text>
 <text x="166" y="146" class="t2">• AOC (ซึม/สับสน)</text>
 <text x="166" y="168" class="t2">• Immunocompromised</text>
 <text x="380" y="124" class="t2">• Papilledema</text>
 <text x="380" y="146" class="t2">• เคยมีโรค CNS (mass)</text>
 <text x="380" y="168" class="t2">• ชักครั้งใหม่</text>
 <path d="M250 180L150 214" class="ln" marker-end="url(#neuro-04-01-a)"/>
 <path d="M490 180L590 214" class="ln" marker-end="url(#neuro-04-01-a)"/>
 <text x="228" y="206" text-anchor="middle" class="tb">มี</text>
 <text x="510" y="206" text-anchor="middle" class="tb">ไม่มี</text>
 <rect x="20" y="216" width="300" height="102" rx="10" class="badsoft"/>
 <text x="170" y="240" text-anchor="middle" class="tb">ให้ dexamethasone + ATB ทันที</text>
 <text x="170" y="264" text-anchor="middle" class="t2">→ CT brain</text>
 <text x="170" y="288" text-anchor="middle" class="t2">→ LP ถ้าไม่มี mass effect</text>
 <text x="170" y="308" text-anchor="middle" class="t3">ป้องกัน brain herniation</text>
 <rect x="420" y="216" width="300" height="102" rx="10" class="oksoft"/>
 <text x="570" y="240" text-anchor="middle" class="tb">LP ทันที</text>
 <text x="570" y="264" text-anchor="middle" class="t2">cell count + diff, glucose, protein</text>
 <text x="570" y="286" text-anchor="middle" class="t2">Gram stain, culture</text>
 <text x="570" y="308" text-anchor="middle" class="t3">แล้ว dexa + ATB ทันที</text>
</svg>''', "ข้อบ่งชี้ CT ก่อน LP ในกล่องเหลืองตามสไลด์ — ถ้าต้อง CT ห้ามรอผล CT แล้วค่อยให้ยา (ลำดับยาก่อน CT เป็นส่วนเสริม)")

S1 = sec("neuro-04-01", "Bacterial meningitis",
    "เชื้อตามอายุ · S. pneumoniae พบบ่อยสุด · หมู → S. suis (SNHL) · CT ก่อน LP เมื่อ AOC/focal/papilledema/immunocomp/ชัก · ceftriaxone ± vanco (+ampicillin >50 ปี) + dexa", minutes=10,
    source=f"{D} หน้า 132–135, 139, 143, 145–158", nl=["B3.2.2(1)", "2.3.6(5)", "B3.3(2)"],
    md='''
### นิยาม

- **Meningitis** = เยื่อหุ้มสมองอักเสบ (virus, bacteria, TB, fungus, parasite)
- **Encephalitis** = เนื้อสมองอักเสบ (virus พบบ่อยสุด) → ชัก focal deficit พฤติกรรมเปลี่ยน
- **Meningoencephalitis** = ทั้งสองอย่าง

### เชื้อตามอายุ/กลุ่มเสี่ยง (สไลด์)

| กลุ่ม | เชื้อ |
|---|---|
| < 1 เดือน | GBS, gram-negative bacilli, **L. monocytogenes** |
| 1 เดือน – 2 ปี | S. pneumoniae, N. meningitidis, GBS, H. influenzae |
| 2 – 50 ปี | **S. pneumoniae, N. meningitidis** |
| > 50 ปี | S. pneumoniae, GNB, N. meningitidis, H. influenzae, **L. monocytogenes** |
| Immunocompromised | **L. monocytogenes**, GNB |
| **สัมผัสหมู (คนชำแหละ เลี้ยงหมู) / กินหมูดิบ** | **Streptococcus suis** |

- Gram stain: **S. pneumoniae = gram-positive diplococci (lancet)** · **S. suis = gram-positive cocci in pairs/short chains** · N. meningitidis = gram-negative diplococci · Listeria = gram-positive bacilli/coccobacilli · Staphylococcus = cocci in clusters

### อาการ

- ไข้ ปวดหัว **meningeal sign** (stiff neck, Kernig, Brudzinski) photophobia N/V AOC papilledema
- **Petechiae/purpura → N. meningitidis**
- Encephalitis: ชัก focal deficit พฤติกรรมเปลี่ยน
- **Complication: SNHL (พบบ่อยสุด)**, focal deficit, ชัก, hydrocephalus, brain abscess — **SNHL เด่นมากใน S. suis** (เสริม)

### Investigation

[[fig:neuro-04-01-f1]]

- **CT ก่อน LP** เมื่อมี: **focal neurodeficit, AOC, immunocompromised, papilledema, เคยมีโรค CNS (mass), ชักครั้งใหม่** — เพื่อป้องกัน brain herniation
- **LP**: cell count + differential, glucose, protein, Gram stain, culture · **blood glucose** พร้อมกัน · **hemoculture**

### การรักษา (สไลด์)

**IV antibiotic + IV dexamethasone**

| กลุ่ม | Empirical ATB |
|---|---|
| < 1 เดือน | Ampicillin + gentamicin + cefotaxime |
| 1 เดือน – 50 ปี | **Ceftriaxone/cefotaxime ± vancomycin** |
| > 50 ปี / immunocompromised | Ceftriaxone/cefotaxime ± vancomycin **+ ampicillin** (คลุม Listeria) |
| S. suis | **Penicillin G + ceftriaxone** |
| N. meningitidis | Cefotaxime/ceftriaxone |

- **Dexamethasone** (0.15 mg/kg IV q6h × 4 วัน เริ่มก่อน/พร้อม ATB dose แรก — เสริม) **มีประโยชน์เฉพาะ S. pneumoniae, H. influenzae** → ลด hearing loss/neurologic sequelae
- ขนาดยา (เสริม): ceftriaxone **2 g IV q12h** (ขนาด meningitis) · ระยะเวลา: pneumococcus 10–14 วัน, meningococcus 7 วัน, Listeria ≥ 21 วัน
- Culture ไม่ขึ้น (partially treated/ได้ ATB ก่อน) แต่ CSF เป็น bacterial pattern และอาการดีขึ้น → **ให้ ceftriaxone ต่อจนครบ** ไม่ต้องเปลี่ยนเป็นยากิน
''',
    figs=[F_LP],
    pearls=[
        "Bacterial meningitis ผู้ใหญ่ที่พบบ่อยสุด = S. pneumoniae",
        "สัมผัสหมู/กินหมูดิบ + meningitis + หูดับ = S. suis → PGS + ceftriaxone",
        "CT ก่อน LP: AOC, focal deficit, papilledema, immunocomp, CNS disease, new seizure",
        "> 50 ปี/ภูมิต่ำ เพิ่ม ampicillin คลุม Listeria",
        "Dexamethasone ได้ประโยชน์ใน S. pneumoniae และ H. influenzae",
    ],
    items=[
        mcq("NEURO-04-01-1",
            "A 50-year-old man has fever and severe headache for 2 days. BT 40°C, PR 100/min, RR 24/min, BP 130/85 mmHg. He is alert with a left sensorineural hearing loss. LP: opening pressure 24 cmH2O, cloudy CSF, WBC 1,500/mm3 (PMN 90%), protein 500 mg/dL, glucose 10 mg/dL (serum 90 mg/dL). He has no contact with pigs and has not eaten raw pork. What is the most likely causative organism?",
            "Streptococcus pneumoniae",
            ["Naegleria fowleri", "Streptococcus suis", "Neisseria meningitidis", "Listeria monocytogenes"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 145–146)",
            explain='''CSF แบบ **bacterial** (PMN เด่น protein สูง glucose ต่ำมาก) ในผู้ใหญ่ → เชื้อที่ **พบบ่อยที่สุดคือ S. pneumoniae** (สไลด์เฉลย: most common S. pneumoniae · ถ้าจะตอบ S. suis โจทย์ควรให้ประวัติสัมผัสหมู/กินหมูดิบ — จึงเติมประโยคปฏิเสธไว้ในโจทย์)
- Naegleria (primary amebic meningoencephalitis) ต้องมีประวัติว่ายน้ำในน้ำจืด อาการรุนแรงเร็ว
- S. suis ทำให้ SNHL เด่นจริง แต่ต้องมีประวัติหมู
- N. meningitidis มักมี petechiae/purpura ในคนอายุน้อย
- Listeria พบในทารก > 50 ปี และภูมิคุ้มกันต่ำ — อายุ 50 พอดีแต่เป็นเชื้อที่พบน้อยกว่า pneumococcus''',
            pearl="Bacterial meningitis ไม่มีประวัติพิเศษ → S. pneumoniae", topic="Pathogen",
            ref=[f"{D} หน้า 133, 145–146"], nl=["B3.2.2(1)"]),
        mcq("NEURO-04-01-2",
            "A butcher presents with headache and fever. He has neck stiffness. CSF Gram stain shows gram-positive cocci in pairs and short chains. What is the most likely causative agent?",
            "Streptococcus suis",
            ["Streptococcus pneumoniae", "Haemophilus influenzae", "Staphylococcus aureus", "Neisseria meningitidis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 147–148)",
            explain='''**คนชำแหละหมู (butcher)** + meningitis + gram-positive cocci = **S. suis** (สไลด์: ประวัติ pig contact — butcher, กินหมูดิบ)
- S. pneumoniae เป็น gram-positive แต่ไม่ได้เชื่อมกับอาชีพสัมผัสหมู
- H. influenzae และ N. meningitidis เป็น **gram-negative**
- S. aureus เป็น gram-positive cocci **in clusters** และมักเกิดหลังผ่าตัด/บาดเจ็บศีรษะ''',
            pearl="Butcher/เลี้ยงหมู/ลาบหมูดิบ + meningitis = S. suis", topic="S. suis",
            ref=[f"{D} หน้า 133, 147–148"], nl=["B3.2.2(1)"]),
        mcq("NEURO-04-01-3",
            "A 20-year-old man presents with fever and alteration of consciousness. He ate raw pork salad (larb) 3 days ago. BT 39°C, petechial rash on the legs, positive stiff neck. CSF Gram stain shows gram-positive coccobacilli, some in pairs and short chains. What is the most likely organism?",
            "Streptococcus suis",
            ["Listeria monocytogenes", "Staphylococcus aureus", "Streptococcus pyogenes", "Streptococcus pneumoniae"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 149–150)",
            explain='''Gram-positive รูปร่างกลม-รี (coccobacillary) **เรียงเป็นคู่/สายสั้น** + petechial rash ได้ + ประวัติกินหมูดิบ = **S. suis** (โจทย์ในสไลด์มีเครื่องหมาย "??" ที่ rash และ coccobacilli แสดงว่าโจทย์กำกวม — จึงเติมประวัติลาบหมูดิบเพื่อให้มีคำตอบเดียว)
- Listeria เป็น gram-positive **bacilli** สั้น พบในทารก สูงอายุ ภูมิคุ้มกันต่ำ ไม่ใช่ชายอายุ 20 แข็งแรง
- Staphylococcus เรียงเป็น **กลุ่มพวง (cluster)**
- S. pyogenes ทำให้ meningitis ได้น้อยมาก
- S. pneumoniae เป็น diplococci รูป lancet แต่ไม่เชื่อมกับการกินหมูดิบ''',
            pearl="Strep = cocci in chain · Staph = cluster · Listeria = bacilli", topic="Gram stain",
            ref=[f"{D} หน้า 149–150"], nl=["B3.2.2(1)", "B3.3(2)"]),
        mcq("NEURO-04-01-4",
            "A 40-year-old man presents with fever and alteration of consciousness. Examination shows neck stiffness but no focal deficit. Blood cultures have been drawn. What is the most appropriate investigation before lumbar puncture?",
            "CT brain",
            ["Lumbar puncture without imaging", "EEG", "MRI spine", "Chest radiograph"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 153–154)",
            explain='''**AOC** เป็นหนึ่งในข้อบ่งชี้ทำ **CT ก่อน LP** (ร่วมกับ focal deficit, immunocompromised, papilledema, CNS disease, new-onset seizure) เพื่อป้องกัน herniation — และควรให้ dexamethasone + ATB ไปก่อนโดยไม่รอผล CT (เสริม)
- LP ทันทีไม่ปลอดภัยในคนซึม
- EEG ไม่ช่วยตัดสินความปลอดภัยของ LP
- MRI spine ไม่เกี่ยว
- CXR อาจหาแหล่งติดเชื้อแต่ไม่ใช่สิ่งที่ต้องทำก่อน LP (ตัวเลือกในสไลด์คือ CT/LP/hemoculture)''',
            pearl="Meningitis + AOC → CT ก่อน LP (ATB ไม่ต้องรอ)", topic="CT before LP",
            ref=[f"{D} หน้า 139, 153–154"], nl=["B3.3(2)", "B3.2.2(1)"]),
        mcq("NEURO-04-01-5",
            "A 50-year-old woman who works on a pig farm has fever with chills for 5 days and drowsiness for 3 days. BT 39.5°C, nuchal rigidity, no focal deficit. CSF: WBC 1,000/mm3 (PMN 90%), protein 200 mg/dL, glucose 30 mg/dL. CSF Gram stain: gram-positive diplococci. What is the most appropriate antibiotic?",
            "Ceftriaxone",
            ["Vancomycin alone", "Ceftazidime plus amikacin", "Piperacillin–tazobactam", "Meropenem"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 155–156)",
            explain='''ทำงานฟาร์มหมู + bacterial meningitis + gram-positive diplococci = **S. suis** → สไลด์ให้ **penicillin G + ceftriaxone** · ตัวเลือกที่ตรงคือ **ceftriaxone** (ร่วมกับ dexamethasone ตามแนวทางเดิม)
- Vancomycin เดี่ยวไม่ใช่ยาหลัก ใช้เสริมเมื่อสงสัย pneumococcus ดื้อยา
- Ceftazidime + amikacin เน้น Pseudomonas/gram-negative ผ่าน BBB ได้ไม่ดีพอสำหรับ strep
- Piperacillin–tazobactam ผ่านเข้า CSF ได้ไม่ดี
- Meropenem กว้างเกินจำเป็น''',
            pearl="S. suis → ceftriaxone (± penicillin G)", topic="Empirical ATB",
            ref=[f"{D} หน้า 143, 155–156"], nl=["B3.2.2(1)"]),
    ])

# ---------------------------------------------------------------- 04-02 CSF interpretation
F_CSF = fig("neuro-04-02-f1", "CSF pattern ตามเชื้อ (ตามตารางสไลด์)", '''<svg viewBox="0 0 740 360">
 <rect x="10" y="10" width="120" height="40" rx="6" class="sunk"/>
 <rect x="134" y="10" width="96" height="40" rx="6" class="oksoft"/>
 <text x="182" y="35" text-anchor="middle" class="tb">Normal</text>
 <rect x="234" y="10" width="96" height="40" rx="6" class="badsoft"/>
 <text x="282" y="35" text-anchor="middle" class="tb">Bacteria</text>
 <rect x="334" y="10" width="96" height="40" rx="6" class="c1soft"/>
 <text x="382" y="35" text-anchor="middle" class="tb">Virus</text>
 <rect x="434" y="10" width="96" height="40" rx="6" class="misssoft"/>
 <text x="482" y="35" text-anchor="middle" class="tb">TB</text>
 <rect x="534" y="10" width="96" height="40" rx="6" class="c2soft"/>
 <text x="582" y="35" text-anchor="middle" class="tb">Fungus</text>
 <rect x="634" y="10" width="96" height="40" rx="6" class="acsoft"/>
 <text x="682" y="35" text-anchor="middle" class="tb">Parasite</text>
 <text x="20" y="80" class="tb">OP</text>
 <text x="20" y="96" class="t3">cmH2O</text>
 <text x="182" y="86" text-anchor="middle" class="t2">10–20</text>
 <text x="282" y="86" text-anchor="middle" class="t2">↑↑</text>
 <text x="382" y="86" text-anchor="middle" class="t2">↔/↑</text>
 <text x="482" y="86" text-anchor="middle" class="t2">↑↑</text>
 <text x="582" y="86" text-anchor="middle" class="tb">↑↑↑</text>
 <text x="682" y="86" text-anchor="middle" class="t2">↑↑</text>
 <path d="M10 106H730" class="lnf"/>
 <text x="20" y="130" class="tb">ลักษณะ</text>
 <text x="182" y="130" text-anchor="middle" class="t2">ใส</text>
 <text x="282" y="130" text-anchor="middle" class="t2">ขุ่น</text>
 <text x="382" y="130" text-anchor="middle" class="t2">ใส</text>
 <text x="482" y="130" text-anchor="middle" class="t2">เหลือง/ขุ่น</text>
 <text x="582" y="130" text-anchor="middle" class="t2">ใส/ขุ่น</text>
 <text x="682" y="130" text-anchor="middle" class="t2">ขุ่น</text>
 <path d="M10 146H730" class="lnf"/>
 <text x="20" y="170" class="tb">WBC</text>
 <text x="182" y="170" text-anchor="middle" class="t2">&lt; 5</text>
 <text x="282" y="170" text-anchor="middle" class="t2">50–5,000</text>
 <text x="382" y="170" text-anchor="middle" class="t2">5–500</text>
 <text x="482" y="170" text-anchor="middle" class="t2">25–500</text>
 <text x="582" y="170" text-anchor="middle" class="t2">5–100</text>
 <text x="682" y="170" text-anchor="middle" class="t2">&gt; 5</text>
 <path d="M10 186H730" class="lnf"/>
 <text x="20" y="210" class="tb">เซลล์เด่น</text>
 <text x="182" y="210" text-anchor="middle" class="t2">Lymph</text>
 <text x="282" y="210" text-anchor="middle" class="tb">PMN</text>
 <text x="382" y="210" text-anchor="middle" class="t2">Mono</text>
 <text x="482" y="210" text-anchor="middle" class="t2">Mono</text>
 <text x="582" y="210" text-anchor="middle" class="t2">Mono</text>
 <text x="682" y="210" text-anchor="middle" class="tb">Eo &gt; 10%</text>
 <path d="M10 226H730" class="lnf"/>
 <text x="20" y="250" class="tb">Protein</text>
 <text x="20" y="266" class="t3">mg/dL</text>
 <text x="182" y="256" text-anchor="middle" class="t2">&lt; 45</text>
 <text x="282" y="256" text-anchor="middle" class="t2">100–1,000</text>
 <text x="382" y="256" text-anchor="middle" class="t2">50–100</text>
 <text x="482" y="256" text-anchor="middle" class="tb">100–5,000</text>
 <text x="582" y="256" text-anchor="middle" class="t2">20–500</text>
 <text x="682" y="256" text-anchor="middle" class="t2">&gt; 60</text>
 <path d="M10 278H730" class="lnf"/>
 <text x="20" y="302" class="tb">CSF/serum</text>
 <text x="20" y="318" class="tb">glucose</text>
 <text x="182" y="308" text-anchor="middle" class="t2">~60%</text>
 <text x="282" y="308" text-anchor="middle" class="tb">↓</text>
 <text x="382" y="308" text-anchor="middle" class="t2">↔</text>
 <text x="482" y="308" text-anchor="middle" class="tb">&lt; 30%</text>
 <text x="582" y="308" text-anchor="middle" class="t2">↔/↓</text>
 <text x="682" y="308" text-anchor="middle" class="t2">↔/↓</text>
 <rect x="234" y="330" width="96" height="24" rx="6" class="sunk"/>
 <text x="282" y="347" text-anchor="middle" class="t3">Gram stain</text>
 <rect x="334" y="330" width="96" height="24" rx="6" class="sunk"/>
 <text x="382" y="347" text-anchor="middle" class="t3">PCR (HSV)</text>
 <rect x="434" y="330" width="96" height="24" rx="6" class="sunk"/>
 <text x="482" y="347" text-anchor="middle" class="t3">AFB, ↑ADA</text>
 <rect x="534" y="330" width="96" height="24" rx="6" class="sunk"/>
 <text x="582" y="347" text-anchor="middle" class="t3">India ink, CrAg</text>
 <rect x="634" y="330" width="96" height="24" rx="6" class="sunk"/>
 <text x="682" y="347" text-anchor="middle" class="t3">Eo count</text>
</svg>''', "อ่านทีละแถว: PMN + glucose ต่ำ = bacteria · lymph + glucose ปกติ = virus · lymph + protein สูงมาก + glucose < 30% = TB · OP สูงมาก = fungus · eosinophil > 10% = parasite · แถวล่างคือการตรวจเพิ่มที่ยืนยัน")

S2 = sec("neuro-04-02", "CSF interpretation",
    "ปกติ OP 10–20 cmH2O WBC <5 protein <45 CSF/serum glucose 60% · bacteria PMN+glucose ต่ำ · virus lymph+glucose ปกติ · TB lymph protein สูงมาก glucose <30% · fungus OP สูงมาก · parasite Eo >10%", minutes=6,
    source=f"{D} หน้า 140–142, 157–158", nl=["B3.3(2)", "B3.2.2(1)"],
    md='''
### ค่าปกติ (สไลด์)

- **Opening pressure 10–20 cmH2O** (8–15 mmHg) · ใส · **WBC < 5** (lymphocyte) · **protein < 45 mg/dL** · **CSF/serum glucose ≈ 60%**

### Pattern ตามเชื้อ

[[fig:neuro-04-02-f1]]

| | Bacteria | Virus | TB | Fungus | Parasite |
|---|---|---|---|---|---|
| OP | ↑↑ | ↔/↑ | ↑↑ | **↑↑↑** | ↑↑ |
| ลักษณะ | Turbid | Clear | Yellow/cloudy | Clear/cloudy | Cloudy, xanthochromia |
| WBC | 50–5,000 | 5–500 | 25–500 | 5–100 | > 5 |
| Diff | **PMN** | Mono | Mono | Mono | **Eosinophil > 10%** |
| Protein | 100–1,000 | 50–100 | **100–5,000** | 20–500 | > 60 |
| CSF/serum glucose | **↓** | ↔ | **< 30%** | ↔/↓ | ↔/↓ |

- การตรวจเพิ่ม: **TB** → AFB, **↑ADA**, CT (hydrocephalus, basilar meningeal enhancement) · **Cryptococcus** → **India ink, cryptococcal antigen** (HIV, CD4 < 100)

> กับดัก: **TB meningitis ระยะแรกอาจเป็น PMN เด่นได้** คล้าย bacterial — ดูที่ประวัติ subacute (> 1–2 สัปดาห์), protein สูงมาก, hydrocephalus, basal enhancement · **Partially treated bacterial meningitis** CSF ยังเป็น PMN/glucose ต่ำแต่ culture ไม่ขึ้น
''',
    figs=[F_CSF],
    pearls=[
        "CSF ปกติ: OP 10–20, WBC < 5, protein < 45, glucose ratio ~60%",
        "PMN + glucose ต่ำ = bacterial",
        "Lymph + protein สูงมาก + glucose < 30% + hydrocephalus = TB",
        "OP สูงมากใน HIV = cryptococcus → CrAg/India ink",
        "Eosinophil > 10% = eosinophilic meningitis",
    ],
    items=[
        mcq("NEURO-04-02-1",
            "A 40-year-old woman has had headache and fever for 1 day. BT 40°C, stiff neck. CT brain is normal. CSF: opening pressure 30 cmH2O, WBC 1,000/mm3 (PMN 95%), protein 100 mg/dL, glucose 10 mg/dL; Gram stain shows no organisms. She is afebrile and much better after 2 days of ceftriaxone. CSF and blood cultures show no growth. What is the most appropriate management?",
            "Continue IV ceftriaxone to complete the course",
            ["Switch to oral cefdinir", "Switch to IV acyclovir", "Add dexamethasone now", "Repeat lumbar puncture"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 157–158)",
            explain='''CSF เป็น **bacterial pattern ชัด** (PMN 95%, glucose 10) แม้ Gram stain/culture ลบ (เช่นได้ยามาก่อน) และ **ตอบสนองดีต่อ ceftriaxone** → **ให้ ceftriaxone ต่อจนครบ** (มัก 10–14 วัน — เสริม)
- Cefdinir ทางปากผ่านเข้า CSF ได้ไม่พอ
- Acyclovir ใช้กับ HSV encephalitis ซึ่ง CSF เป็น lymphocyte
- Dexamethasone ต้องเริ่มก่อน/พร้อม ATB dose แรก เริ่มหลัง 2 วันไม่มีประโยชน์
- Repeat LP ไม่จำเป็นเมื่ออาการดีขึ้นชัด''',
            pearl="Culture ลบแต่ CSF แบบ bacteria + ดีขึ้น → ATB เดิมจนครบ", topic="Culture-negative meningitis",
            ref=[f"{D} หน้า 142–143, 157–158"], nl=["B3.2.2(1)", "B3.3(2)"]),
        mcq("NEURO-04-02-2",
            "A 22-year-old woman has 3 days of fever, headache and photophobia after a week of sore throat and diarrhea. She is alert without focal deficits. CSF: opening pressure 18 cmH2O, clear, WBC 120/mm3 (lymphocytes 90%), protein 70 mg/dL, glucose 60 mg/dL (serum 95 mg/dL). Gram stain is negative. What is the most likely cause?",
            "Enterovirus",
            ["Streptococcus pneumoniae", "Mycobacterium tuberculosis", "Cryptococcus neoformans", "Angiostrongylus cantonensis"],
            explain='''CSF **ใส lymphocyte เด่น protein สูงเล็กน้อย glucose ปกติ (ratio 63%)** + prodrome ไข้หวัด/ท้องเสีย รู้สึกตัวดี = **viral meningitis** ซึ่งเชื้อพบบ่อยที่สุดคือ **enterovirus** → supportive
- S. pneumoniae ให้ PMN เด่น glucose ต่ำ
- TB ให้ protein สูงมากและ glucose < 30% มักเป็นหลายสัปดาห์
- Cryptococcus พบในภูมิคุ้มกันต่ำ OP สูงมาก
- Angiostrongylus ให้ eosinophil > 10%''',
            pearl="Lymph + glucose ปกติ + รู้สึกตัวดี = viral (enterovirus)", topic="CSF pattern",
            ref=[f"{D} หน้า 137, 141–142"], nl=["B3.3(2)", "B3.2.2(1)"]),
        mcq("NEURO-04-02-3",
            "A 45-year-old man has had 3 weeks of fever, headache and progressive drowsiness. CT brain shows communicating hydrocephalus with basal meningeal enhancement. CSF: WBC 250/mm3 (lymphocytes 80%), protein 450 mg/dL, glucose 25 mg/dL (serum 110 mg/dL). Which additional CSF test most supports the likely diagnosis?",
            "Adenosine deaminase (ADA)",
            ["India ink preparation", "HSV PCR", "Eosinophil count", "VDRL"],
            explain='''Subacute 3 สัปดาห์ + **hydrocephalus + basal meningeal enhancement** + lymphocyte + **protein สูงมาก + glucose ratio 23% (< 30%)** = **TB meningitis** → สไลด์ให้ตรวจ **AFB และ ↑ADA**
- India ink ใช้กับ cryptococcus (HIV, OP สูงมาก, protein ไม่สูงขนาดนี้)
- HSV PCR ใช้กับ encephalitis เฉียบพลัน glucose ปกติ
- Eosinophil count ใช้เมื่อสงสัย parasite
- VDRL ใช้กับ neurosyphilis''',
            pearl="Hydrocephalus + basal enhancement + glucose < 30% → TB (ADA)", topic="TB CSF",
            ref=[f"{D} หน้า 140, 142"], nl=["B3.3(2)"]),
    ])

# ---------------------------------------------------------------- 04-03 Meningococcemia
S3 = sec("neuro-04-03", "Meningococcemia & chemoprophylaxis",
    "N. meningitidis: petechiae/purpura, Waterhouse-Friderichsen (DIC + adrenal hemorrhage) · Tx ceftriaxone/cefotaxime · close contact prophylaxis: rifampin, ceftriaxone (ตั้งครรภ์), ciprofloxacin", minutes=5,
    source=f"{D} หน้า 136, 151–152, 163–166", nl=["B3.2.2(1)", "2.3.6(5)"],
    md='''
### Meningococcemia

- เชื้อ **Neisseria meningitidis** (gram-negative diplococci) — พบในวัยรุ่น/ผู้ใหญ่ตอนต้น ที่อยู่รวมกัน (ค่ายทหาร หอพัก — เสริม)
- **Petechiae, purpura** (มักที่ขา) ± meningitis
- **Waterhouse-Friderichsen syndrome** = septic shock + **DIC** + **adrenal gland hemorrhage** → adrenal insufficiency
- **Tx: cefotaxime/ceftriaxone** (+ supportive, หากช็อกดื้อ — พิจารณา hydrocortisone — เสริม)

### Chemoprophylaxis สำหรับ close contact

| ยา | หมายเหตุ |
|---|---|
| **Rifampin** | 600 mg PO q12h × 2 วัน (เสริม) · ห้ามในตั้งครรภ์ |
| **Ceftriaxone** | 250 mg IM ครั้งเดียว (เสริม) · **ตัวเลือกแรกในหญิงตั้งครรภ์** |
| **Ciprofloxacin** | 500 mg PO ครั้งเดียว (เสริม) |

- Close contact (เสริม): คนในบ้าน, คนที่นอน/ทำงานใกล้ชิด, สัมผัสน้ำลายโดยตรง, บุคลากรที่ทำหัตถการทางเดินหายใจโดยไม่ป้องกัน — ให้เร็วที่สุด (ภายใน 24 ชม.)
- ไม่ต้อง throat/nasopharyngeal swab ก่อนให้ยา
''',
    pearls=[
        "ไข้ + petechiae/purpura + คอแข็ง = N. meningitidis",
        "Waterhouse-Friderichsen = DIC + adrenal hemorrhage",
        "Prophylaxis: rifampin / ceftriaxone / ciprofloxacin",
        "ตั้งครรภ์ → ceftriaxone IM",
    ],
    items=[
        mcq("NEURO-04-03-1",
            "A young adult presents with BT 39°C, subconjunctival hemorrhage, positive neck stiffness, and petechiae and purpura on both legs. What is the most likely organism?",
            "Neisseria meningitidis",
            ["Haemophilus influenzae", "Streptococcus pneumoniae", "Staphylococcus aureus", "Mycoplasma pneumoniae"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 151–152)",
            explain='''Meningitis + **petechiae/purpura** = **N. meningitidis** (meningococcemia) ตามสไลด์
- H. influenzae และ S. pneumoniae ทำให้ meningitis ได้ แต่ผื่น petechiae/purpura ไม่ใช่ลักษณะเด่น (ยกเว้นเกิด DIC รุนแรง)
- S. aureus ทำให้ septic emboli/endocarditis มากกว่า meningitis primary
- Mycoplasma ทำให้ atypical pneumonia ไม่ทำ meningitis เด่น''',
            pearl="Meningitis + petechiae/purpura = meningococcus", topic="Meningococcemia",
            ref=[f"{D} หน้า 134, 136, 151–152"], nl=["B3.2.2(1)"]),
        mcq("NEURO-04-03-2",
            "A 28-year-old woman is hospitalized with meningococcemia (fever, headache and petechial rash) and is receiving appropriate antibiotics. Her family members live in the same house; none is pregnant. What is the recommended prophylactic measure for them?",
            "Rifampicin",
            ["Throat swab culture", "Nasopharyngeal swab culture", "Azithromycin", "Ofloxacin"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 163–164)",
            explain='''Close contact ของ meningococcal disease → **chemoprophylaxis ทันที** ด้วย **rifampin**, ceftriaxone หรือ ciprofloxacin (สไลด์)
- Throat/nasopharyngeal swab ไม่ช่วยตัดสินใจ และทำให้ prophylaxis ล่าช้า
- Azithromycin ไม่ใช่ยามาตรฐานในแนวทางนี้
- Ofloxacin ไม่ใช่ตัวเลือกในสไลด์ (fluoroquinolone ที่ใช้คือ ciprofloxacin)''',
            pearl="Meningococcal contact → rifampin/ceftriaxone/cipro", topic="Chemoprophylaxis",
            ref=[f"{D} หน้า 136, 163–164"], nl=["B3.2.2(1)"]),
        mcq("NEURO-04-03-3",
            "A 30-year-old construction worker is brought to the ER unconscious with a purplish maculopapular rash on both thighs and is diagnosed with meningococcemia. Which agent should be used as chemoprophylaxis for his co-worker who shares his sleeping quarters?",
            "Ciprofloxacin",
            ["Amoxicillin–clavulanate", "Doxycycline", "Cephalexin", "Metronidazole"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 165–166)",
            explain='''Close contact (นอนที่เดียวกัน) → prophylaxis ด้วย **ciprofloxacin** 500 mg ครั้งเดียว (หรือ rifampin/ceftriaxone) — ในตัวเลือกมีเพียง ciprofloxacin ที่อยู่ในแนวทาง
- Amoxicillin–clavulanate และ cephalexin ไม่กำจัดเชื้อในโพรงจมูก (nasopharyngeal carriage)
- Doxycycline ไม่ใช่ยาที่แนะนำ
- Metronidazole ใช้กับ anaerobe/protozoa''',
            pearl="Single-dose ciprofloxacin สำหรับ meningococcal contact", topic="Chemoprophylaxis",
            ref=[f"{D} หน้า 136, 165–166"], nl=["B3.2.2(1)"]),
    ])

# ---------------------------------------------------------------- 04-04 Viral & HSV encephalitis
S4 = sec("neuro-04-04", "Viral meningitis & HSV encephalitis",
    "Enterovirus พบบ่อยสุด → supportive · HSV encephalitis: ไข้ ชัก พฤติกรรมเปลี่ยน CSF lymph + RBC · temporal lobe lesion · PCR · IV acyclovir ทันที", minutes=6,
    source=f"{D} หน้า 137, 144, 159–162", nl=["B3.2.2(2)", "2.3.6(1)", "B3.2.2(1)"],
    md='''
### Viral meningitis

- เชื้อ: **enterovirus (พบบ่อยสุด)**, HSV
- Prodrome แบบไข้หวัด → ไข้ ปวดหัว คอแข็ง รู้สึกตัวดี
- Encephalitis ร่วมได้บ่อย: ชัก focal deficit พฤติกรรมเปลี่ยน
- **Tx: supportive**

### HSV encephalitis

- อาการ: ไข้ + **ชัก, focal deficit, พฤติกรรม/บุคลิกเปลี่ยน, สับสน** (temporal lobe — aphasia, olfactory hallucination — เสริม)
- **CSF: lymphocyte เด่น + มี RBC**, protein ↔/↑, glucose ปกติ
- **CSF PCR for HSV** (ยืนยัน)
- **Imaging: temporal lobe lesion** (MRI ดีกว่า CT — อาจเป็นสองข้าง frontotemporal)
- **Tx: IV acyclovir** (10 mg/kg q8h × 14–21 วัน — เสริม) **เริ่มทันทีที่สงสัย** ไม่ต้องรอ PCR

> ไข้ + ชักแบบ focal/พฤติกรรมเปลี่ยน + CSF lymph + RBC + glucose ปกติ → **acyclovir** (ไม่ใช่ anti-TB หรือ ceftriaxone)
''',
    pearls=[
        "Viral meningitis ส่วนใหญ่ = enterovirus → supportive",
        "HSV encephalitis: ไข้ + ชัก/พฤติกรรมเปลี่ยน + temporal lesion",
        "CSF HSV: lymph + RBC + glucose ปกติ → PCR",
        "สงสัย HSV → IV acyclovir ทันที",
    ],
    items=[
        mcq("NEURO-04-04-1",
            "A 28-year-old man had fever and severe headache for 3 days, and today had a focal seizure of the left face and arm. BT 40.9°C. LP: opening pressure 30 cmH2O, RBC 100/mm3, WBC 150/mm3 (lymphocytes 95%), glucose 90 mg/dL (blood 100 mg/dL), protein 50 mg/dL. Gram stain and India ink are negative. What is the most appropriate management?",
            "IV acyclovir",
            ["Anti-tuberculous drugs", "IV ceftriaxone alone", "IV dexamethasone alone", "Amphotericin B"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 159–160)",
            explain='''ไข้ + **focal seizure** + CSF **lymphocyte เด่น + มี RBC + glucose ปกติ** = **HSV encephalitis** → **IV acyclovir** (สไลด์เฉลย Herpes encephalitis, Tx acyclovir IV) — โจทย์เดิมถามว่า "investigation" แต่ตัวเลือกเป็นการรักษา จึงปรับคำถาม และปรับ protein จาก 20 เป็น 50 mg/dL ให้เข้ากับภาวะอักเสบ
- Anti-TB ใช้เมื่อ protein สูงมากและ glucose < 30% แบบ subacute
- Ceftriaxone เหมาะกับ bacterial (PMN, glucose ต่ำ)
- Dexamethasone เดี่ยว ๆ ไม่รักษา HSV
- Amphotericin B สำหรับ cryptococcus ซึ่ง India ink ลบและไม่มีภูมิคุ้มกันต่ำ''',
            pearl="ไข้ + focal seizure + CSF lymph + RBC = HSV → acyclovir", topic="HSV encephalitis",
            ref=[f"{D} หน้า 137, 159–160"], nl=["B3.2.2(2)"]),
        mcq("NEURO-04-04-2",
            "A 65-year-old Thai man has had fever, alteration of consciousness and behavioral change for 6 days. He is drowsy and does not follow commands. CT brain: low-density lesions in both frontotemporal regions. CSF: opening pressure 18 cmH2O, WBC 10/mm3 (mononuclear 100%), RBC 50/mm3, protein 45 mg/dL, glucose 65 mg/dL (blood 100 mg/dL). What is the most appropriate treatment?",
            "IV acyclovir",
            ["IV ceftriaxone", "Prednisolone", "Amoxicillin–clavulanate", "Oral fluconazole"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 161–162)",
            explain='''ไข้ + ซึม + **พฤติกรรมเปลี่ยน** + **frontotemporal lesion** + CSF mononuclear + RBC + glucose ปกติ = **HSV encephalitis** → **IV acyclovir**
- Ceftriaxone ไม่ครอบคลุม HSV และ CSF ไม่ใช่ bacterial pattern
- Prednisolone ไม่ใช่การรักษาหลัก
- Amoxicillin–clavulanate ไม่ผ่าน CSF ในขนาดรักษาและไม่ครอบคลุมไวรัส
- Fluconazole สำหรับ fungal infection''',
            pearl="Temporal/frontotemporal lesion + ไข้ + พฤติกรรมเปลี่ยน = HSV", topic="HSV encephalitis",
            ref=[f"{D} หน้า 137, 161–162"], nl=["B3.2.2(2)", "2.3.6(1)"]),
        mcq("NEURO-04-04-3",
            "A 19-year-old university student has fever, headache and neck stiffness for 2 days following a flu-like illness. He is alert and oriented with no focal deficit. CSF: clear, WBC 80/mm3 (lymphocytes 85%), protein 60 mg/dL, glucose 62 mg/dL (serum 100 mg/dL), Gram stain negative. What is the most appropriate management?",
            "Supportive care with analgesics and hydration",
            ["IV ceftriaxone for 14 days", "Four-drug anti-tuberculous therapy", "Amphotericin B plus flucytosine", "Prednisolone and albendazole"],
            explain='''อาการไม่รุนแรง รู้สึกตัวดี ไม่มีอาการ encephalitis + CSF แบบ **viral (lymph, glucose ปกติ)** = **viral meningitis (enterovirus)** → **supportive** (สไลด์)
- Ceftriaxone 14 วันใช้กับ bacterial meningitis (PMN, glucose ต่ำ)
- Anti-TB ใช้กับ subacute protein สูงมาก glucose < 30%
- Amphotericin + flucytosine สำหรับ cryptococcus ในภูมิคุ้มกันต่ำ
- Prednisolone/albendazole สำหรับ eosinophilic meningitis''',
            pearl="Viral meningitis ไม่มี encephalitis → supportive", topic="Viral meningitis",
            ref=[f"{D} หน้า 137, 144"], nl=["B3.2.2(1)"]),
    ])

# ---------------------------------------------------------------- 04-05 TB & cryptococcal meningitis
S5 = sec("neuro-04-05", "TB meningitis & cryptococcal meningitis",
    "TB: subacute, hydrocephalus, basal enhancement, glucose <30% → 2IRZE/10IR + dexa · Crypto: HIV CD4 <100, OP สูงมาก → CrAg/India ink → ampho B + flucytosine → fluconazole", minutes=8,
    source=f"{D} หน้า 140, 144, 167–176", nl=["B3.2.2(1)", "2.3.1(20)", "2.3.1-3(7)"],
    md='''
### TB meningitis

- Subacute (> 1–2 สัปดาห์) ไข้ ปวดหัว ซึม CN palsy (เสริม)
- **CSF**: lymphocyte เด่น (**ระยะแรกอาจ PMN เด่นได้** — profile เหมือน bacterial), **protein สูงมาก (100–5,000)**, **glucose < 30%**, OP สูง, สีเหลือง
- Ix: **AFB, ↑ADA**, (GeneXpert — เสริม) · **CT: hydrocephalus, basilar meningeal enhancement**
- **Tx: 2IRZE + 10IR** (รวม 12 เดือน) **+ IV dexamethasone**

### Cryptococcal meningitis

- ผู้ป่วย **HIV, CD4 < 100**
- ปวดหัวแบบค่อยเป็นค่อยไป ไข้ต่ำ ๆ — อาการ meningeal sign อาจน้อย
- **OP สูงมาก (↑↑↑)**, WBC น้อย (5–100), protein ไม่สูงมาก, glucose ↔/↓
- Ix: **India ink** (encapsulated budding yeast), **cryptococcal antigen (CrAg)** ใน CSF/serum
- **Tx: amphotericin B + flucytosine (induction) → fluconazole** (consolidation/maintenance)
- (เสริม) OP ≥ 25 cmH2O + อาการ → **therapeutic LP ซ้ำ** ระบาย CSF · เริ่ม ARV หลังเริ่มยาเชื้อราราว 4–6 สัปดาห์ (ป้องกัน IRIS) · ห้ามให้ steroid

| | TB meningitis | Cryptococcal meningitis |
|---|---|---|
| ผู้ป่วย | ใครก็ได้ รวม HIV | HIV CD4 < 100 |
| OP | ↑↑ | **↑↑↑** |
| Protein | **สูงมาก** | ปานกลาง |
| Glucose | **< 30%** | ↔/↓ |
| Imaging | Hydrocephalus, basal enhancement | มักปกติ |
| ยืนยัน | AFB, ADA | India ink, CrAg |
| รักษา | 2IRZE/10IR + dexa | Ampho B + 5-FC → fluconazole |
''',
    pearls=[
        "TB meningitis: protein สูงมาก + glucose < 30% + hydrocephalus/basal enhancement",
        "TBM รักษา 2IRZE + 10IR + dexamethasone",
        "HIV CD4 < 100 + ปวดหัว + OP สูงมาก → CSF CrAg/India ink",
        "Crypto: ampho B + flucytosine → fluconazole",
        "TBM ระยะแรกอาจ PMN เด่นได้",
    ],
    items=[
        mcq("NEURO-04-05-1",
            "An HIV-positive patient has had low-grade fever for 5 days with progressive headache. There is no focal deficit; stiff neck is positive. CSF: protein 600 mg/dL, glucose 20 mg/dL (serum 110 mg/dL), WBC 300/mm3 (lymphocytes 60%). India ink is negative. What is the most likely diagnosis?",
            "Tuberculous meningitis",
            ["Cryptococcal meningitis", "Toxoplasma meningitis", "Viral meningitis", "Bacterial meningitis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 167–168)",
            explain='''Lymphocyte เด่น + **protein สูงมาก (600)** + **glucose ratio 18% (< 30%)** = **TB meningitis** แม้เป็น HIV (เติมผล India ink ลบและ serum glucose ในโจทย์ให้ชัดขึ้น)
- Cryptococcus พบใน HIV เช่นกัน แต่ WBC มักต่ำกว่า protein ไม่สูงขนาดนี้ และ OP สูงมาก
- Toxoplasma ทำให้ brain abscess แบบ ring-enhancing ไม่ใช่ meningitis
- Viral: glucose ปกติ protein สูงเล็กน้อย
- Bacterial: PMN เด่น อาการเฉียบพลัน''',
            pearl="Lymph + protein สูงมาก + glucose < 30% = TB", topic="TB meningitis",
            ref=[f"{D} หน้า 142, 167–168"], nl=["B3.2.2(1)", "2.3.1(20)"]),
        mcq("NEURO-04-05-2",
            "A 40-year-old man has had headache for 2 weeks. BT 39°C. CT brain: mild hydrocephalus and enhancement of the basal cisterns. CSF: opening pressure 21 cmH2O, WBC 1,500/mm3 (PMN 95%, eosinophils 5%), glucose 20 mg/dL, protein 160 mg/dL. What is the diagnosis?",
            "Tuberculous meningitis",
            ["Eosinophilic meningitis", "Cryptococcal meningitis", "Acute bacterial meningitis", "Viral meningitis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 169–170)",
            explain='''แม้ CSF จะ **PMN เด่น** แต่ประวัติ **2 สัปดาห์** + **hydrocephalus + basal cistern enhancement** = **TB meningitis** (สไลด์: ระยะแรก CSF profile เหมือน bacterial ได้ · CT hydrocephalus, basilar meningeal enhancement) — โจทย์เดิมเขียน WBC 15,000 ซึ่งน่าจะพิมพ์ผิด จึงปรับเป็น 1,500
- Eosinophilic meningitis ต้อง eosinophil > 10% (ที่นี่ 5%)
- Cryptococcal พบใน HIV และไม่ทำ basal enhancement เด่น
- Acute bacterial meningitis มักเป็นเฉียบพลันไม่กี่วัน และไม่ทำ basal enhancement ตั้งแต่ 2 สัปดาห์แรก
- Viral: lymph และ glucose ปกติ''',
            pearl="PMN เด่นได้ใน TBM ระยะแรก — ดู hydrocephalus + basal enhancement", topic="TB meningitis",
            ref=[f"{D} หน้า 140, 169–170"], nl=["B3.2.2(1)"]),
        mcq("NEURO-04-05-3",
            "A 40-year-old man has had fever for 3 weeks and headache unresponsive to analgesics, and has been drowsy then unresponsive for 2 days. BT 38.5°C, PR 100/min, BP 110/70 mmHg. Stiff neck is positive. LP: opening pressure 40 cmH2O. CSF: WBC 450/mm3 (N 15%, L 85%), protein 400 mg/dL, glucose 25 mg/dL (blood 120 mg/dL). He is HIV-negative. What is the most appropriate management?",
            "Anti-tuberculous drugs plus dexamethasone",
            ["Acyclovir", "Amphotericin B", "Ceftriaxone alone", "Co-trimoxazole"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 171–172)",
            explain='''Subacute (สัปดาห์) + lymphocyte เด่น + **protein 400 + glucose ratio 21%** = **TB meningitis** → **2IRZE + 10IR + dexamethasone** (สไลด์ตัวเลือกคือ anti-TB drugs; โจทย์เดิมระบุ OP เป็น mmHg จึงปรับเป็น cmH2O และเติม HIV ลบ)
- Acyclovir สำหรับ HSV (glucose ปกติ)
- Amphotericin B สำหรับ cryptococcus ในผู้ป่วยภูมิคุ้มกันต่ำ
- Ceftriaxone เดี่ยว ๆ สำหรับ bacterial meningitis เฉียบพลัน
- Co-trimoxazole ใช้ toxoplasmosis/PCP''',
            pearl="TBM → IRZE + dexamethasone", topic="TB meningitis treatment",
            ref=[f"{D} หน้า 144, 171–172"], nl=["B3.2.2(1)", "2.3.1(20)"]),
        mcq("NEURO-04-05-4",
            "A 30-year-old woman with HIV infection and CKD stage 4 has had headache for 3 days. CSF India ink preparation shows round budding yeasts surrounded by a clear thick capsule. What is the diagnosis?",
            "Cryptococcosis",
            ["Aspergillosis", "Mucormycosis", "Candidiasis", "Toxoplasmosis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 173–174)",
            explain='''**India ink** เห็น **budding yeast ที่มี capsule หนาใส** = **Cryptococcus neoformans** (โจทย์ในสไลด์เป็นภาพ CSF stain จึงบรรยายภาพเป็นข้อความ)
- Aspergillus เป็น septate hyphae แตกกิ่งมุมแหลม
- Mucor เป็น broad non-septate hyphae มุมฉาก (rhino-orbital ใน DKA)
- Candida เป็น pseudohyphae + budding yeast ไม่มี capsule
- Toxoplasma เป็น protozoa ไม่เห็นใน India ink''',
            pearl="India ink + capsule = cryptococcus", topic="Cryptococcal meningitis",
            ref=[f"{D} หน้า 140, 173–174"], nl=["2.3.1-3(7)", "B3.3(2)"]),
        mcq("NEURO-04-05-5",
            "A young man with HIV (CD4 100 cells/mm3) has had headache for 2 weeks. Vital signs are normal; stiff neck is positive. CSF: WBC 100/mm3 (N 10%, M 90%), opening pressure 40 cmH2O, glucose 30 mg/dL (serum 90 mg/dL), protein 150 mg/dL. What is the most appropriate investigation?",
            "CSF cryptococcal antigen",
            ["CSF AFB stain", "CSF PCR for herpes simplex virus", "CSF VDRL", "Serum Toxoplasma IgG"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 175–176)",
            explain='''HIV **CD4 ≤ 100** + ปวดหัวเรื้อรัง + **OP สูงมาก (40)** + WBC ไม่มาก = **cryptococcal meningitis** → **CSF cryptococcal antigen** (หรือ India ink) — สไลด์เฉลยด้วยหลัก immunocompromised, HIV CD4 < 100
- AFB stain ใช้เมื่อสงสัย TB (protein มักสูงกว่านี้มาก)
- HSV PCR ใช้เมื่อเป็น encephalitis เฉียบพลัน
- CSF VDRL สำหรับ neurosyphilis
- Toxoplasma IgG ใช้ร่วมเมื่อเห็น ring-enhancing lesion''',
            pearl="HIV CD4 < 100 + OP สูงมาก → CrAg", topic="Cryptococcal antigen",
            ref=[f"{D} หน้า 140, 175–176"], nl=["2.3.1-3(7)", "2.3.1(9)"]),
    ])

# ---------------------------------------------------------------- 04-06 Eosinophilic meningitis
S6 = sec("neuro-04-06", "Eosinophilic meningitis",
    "CSF eosinophil >10% · Angiostrongylus (หอยโข่ง/ทากดิบ) · Gnathostoma · Tx prednisolone ± analgesic · ยาฆ่าพยาธิอาจทำให้อักเสบมากขึ้น", minutes=5,
    source=f"{D} หน้า 138, 177–180", nl=["B3.2.2(1)", "2.3.1-3(8)"],
    md='''
### นิยามและเชื้อ

- **Eosinophil ใน CSF > 10%**
- **Angiostrongylus cantonensis** (พยาธิปอดหนู) — กิน **หอยโข่ง/หอยเชอรี่ดิบ**, ทาก, ผักที่ปนเปื้อน (เสริม) → ปวดหัวรุนแรง คอแข็ง ชาผิวหนัง (paresthesia) มักไม่ค่อยมีไข้สูง ไม่มี focal deficit
- **Gnathostoma spinigerum** (พยาธิตัวจี๊ด) — กิน **ปลาน้ำจืด/กบ/ไก่ดิบ** (เสริม) → ปวดร้าวตามเส้นประสาท/ไขสันหลัง (radiculomyelitis), **ICH/SAH**, migratory swelling (เสริม)

### การรักษา (สไลด์)

- **Prednisolone** (ลดการอักเสบ) — เช่น 60 mg/day × 2 สัปดาห์ (เสริม) + ยาแก้ปวด, LP ระบายเมื่อ ICP สูง (เสริม)
- **Anti-parasite ให้บางกรณี** เพราะเมื่อพยาธิตาย → inflammatory response มากขึ้น → อาการแย่ลง (Angiostrongylus มักไม่ให้; Gnathostoma ให้ albendazole — เสริม)

> CSF eosinophil 10% ขึ้นไป ไม่ว่าจะมี neutrophil ปนมากเท่าไร → คิด eosinophilic meningitis
''',
    pearls=[
        "CSF eosinophil > 10% = eosinophilic meningitis",
        "หอยดิบ → Angiostrongylus · ปลาดิบ/กบ → Gnathostoma",
        "Tx หลัก = prednisolone",
        "ยาฆ่าพยาธิอาจทำให้แย่ลงจากการอักเสบ",
    ],
    items=[
        mcq("NEURO-04-06-1",
            "A 30-year-old female farmer has had headache for 2 weeks. BT 37.8°C, BP 120/80 mmHg, PR 100/min. She is alert with a stiff neck. CT brain is normal. LP: opening pressure 30 cmH2O, cloudy CSF, WBC 100/mm3 (neutrophils 60%, eosinophils 40%), protein 200 mg/dL, glucose 50 mg/dL. She often eats raw snails. What is the causative organism?",
            "Angiostrongylus cantonensis",
            ["Taenia solium", "Trichuris trichiura", "Strongyloides stercoralis", "Toxocara canis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 177–178)",
            explain='''**CSF eosinophil 40% (> 10%)** = **eosinophilic meningitis** — เชื้อที่พบบ่อยในไทยคือ **Angiostrongylus cantonensis** (จากการกินหอยดิบ — ประวัติกินหอยเติมในโจทย์ให้ชัด)
- Taenia solium ทำให้ neurocysticercosis (cyst ในสมอง ชัก) ไม่ใช่ eosinophilic meningitis เด่น
- Trichuris อยู่ในลำไส้ใหญ่ ไม่ไปสมอง
- Strongyloides ทำให้ hyperinfection + gram-negative meningitis ในคนภูมิต่ำ ไม่ใช่ eosinophilic
- Toxocara ทำให้ visceral/ocular larva migrans พบ meningitis ได้น้อย''',
            pearl="CSF Eo > 10% + กินหอยดิบ = Angiostrongylus", topic="Eosinophilic meningitis",
            ref=[f"{D} หน้า 138, 177–178"], nl=["2.3.1-3(8)", "B3.2.2(1)"]),
        mcq("NEURO-04-06-2",
            "A 35-year-old patient has had headache and fever for 10 days. BT 37.8°C. Neurological examination is normal except for a stiff neck. CSF: opening pressure 20 cmH2O, WBC 400/mm3 (N 60%, L 30%, eosinophils 10%), protein 60 mg/dL, glucose 50 mg/dL (serum 90 mg/dL). What is the appropriate management?",
            "Prednisone",
            ["Acyclovir", "Mebendazole", "Ceftriaxone", "Isoniazid, rifampicin, pyrazinamide and ethambutol"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 179–180)",
            explain='''Eosinophil 10% + glucose ratio 56% (ไม่ต่ำ) = **eosinophilic meningitis** → **prednisolone/prednisone** (สไลด์)
- Acyclovir สำหรับ HSV encephalitis
- Mebendazole (anti-parasite) ไม่ใช่การรักษาหลัก และอาจทำให้อักเสบมากขึ้น
- Ceftriaxone สำหรับ bacterial (glucose จะต่ำ)
- IRZE สำหรับ TB (glucose < 30%, protein สูงมาก)''',
            pearl="Eosinophilic meningitis → prednisolone", topic="Treatment",
            ref=[f"{D} หน้า 138, 179–180"], nl=["B3.2.2(1)"]),
        mcq("NEURO-04-06-3",
            "A 38-year-old man from northeastern Thailand develops severe radicular pain in both legs followed by leg weakness and urinary retention, then a sudden severe headache. He regularly eats raw freshwater fish (koi pla). CT brain shows a small intracerebral hemorrhage; CSF is xanthochromic with 25% eosinophils. Which parasite is most likely responsible?",
            "Gnathostoma spinigerum",
            ["Angiostrongylus cantonensis", "Taenia solium", "Toxoplasma gondii", "Schistosoma mansoni"],
            explain='''Eosinophilic meningitis + **ปวดร้าวตามเส้นประสาท/myelitis** + **intracerebral hemorrhage/CSF xanthochromia** + กินปลาน้ำจืดดิบ = **Gnathostoma** (พยาธิตัวจี๊ดไชเนื้อเยื่อทำให้เลือดออก) — ทั้งหมดเป็นส่วนเสริมจากสไลด์ที่ระบุชื่อเชื้อเท่านั้น
- Angiostrongylus (กินหอย) มักไม่ทำ myelitis รุนแรงหรือเลือดออก
- Taenia solium ทำให้ cyst/calcification ชัก
- Toxoplasma ใน HIV ทำ ring-enhancing lesions ไม่มี eosinophil
- Schistosoma mansoni ไม่พบในไทย''',
            pearl="Eosinophilic meningitis + radiculomyelitis/เลือดออก + ปลาดิบ = Gnathostoma", topic="Gnathostomiasis",
            ref=[f"{D} หน้า 138"], nl=["2.3.1-3(8)"]),
    ])

# ---------------------------------------------------------------- 04-07 Neurocysticercosis & brain abscess
F_NCC = fig("neuro-04-07-f1", "Neurocysticercosis 4 ระยะ กับการรักษา", '''<svg viewBox="0 0 740 280">
 <defs><marker id="neuro-04-07-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="356" height="30" rx="8" class="ok"/>
 <text x="188" y="30" text-anchor="middle" class="tw">พยาธิยังมีชีวิต (viable)</text>
 <rect x="374" y="10" width="356" height="30" rx="8" class="sunk"/>
 <text x="552" y="30" text-anchor="middle" class="tb">พยาธิตายแล้ว</text>
 <rect x="10" y="50" width="170" height="130" rx="10" class="box"/>
 <circle cx="95" cy="98" r="28" class="sunk"/>
 <circle cx="104" cy="92" r="5" class="c2"/>
 <text x="95" y="146" text-anchor="middle" class="tb">1. Vesicular</text>
 <text x="95" y="166" text-anchor="middle" class="t3">cyst + scolex (dot)</text>
 <rect x="196" y="50" width="170" height="130" rx="10" class="box"/>
 <circle cx="281" cy="98" r="34" class="misssoft"/>
 <circle cx="281" cy="98" r="24" class="c1soft"/>
 <text x="281" y="146" text-anchor="middle" class="tb">2. Colloidal</text>
 <text x="281" y="166" text-anchor="middle" class="t3">ring enhance + edema</text>
 <rect x="374" y="50" width="170" height="130" rx="10" class="box"/>
 <circle cx="459" cy="98" r="18" class="c1soft"/>
 <text x="459" y="146" text-anchor="middle" class="tb">3. Granular</text>
 <text x="459" y="166" text-anchor="middle" class="t3">nodule หดเล็กลง</text>
 <rect x="560" y="50" width="170" height="130" rx="10" class="box"/>
 <circle cx="645" cy="98" r="9" class="ac"/>
 <text x="645" y="146" text-anchor="middle" class="tb">4. Calcified</text>
 <text x="645" y="166" text-anchor="middle" class="t3">จุดหินปูน</text>
 <path d="M180 115H195" class="ln" marker-end="url(#neuro-04-07-a)"/>
 <path d="M366 115H373" class="ln" marker-end="url(#neuro-04-07-a)"/>
 <path d="M544 115H559" class="ln" marker-end="url(#neuro-04-07-a)"/>
 <rect x="10" y="192" width="356" height="78" rx="10" class="oksoft"/>
 <text x="22" y="214" class="tb">Albendazole (viable cyst)</text>
 <text x="22" y="236" class="t2">+ steroid (โดยเฉพาะมี edema/ให้ albendazole)</text>
 <text x="22" y="258" class="t2">+ AED ถ้าชัก</text>
 <rect x="374" y="192" width="356" height="78" rx="10" class="misssoft"/>
 <text x="386" y="214" class="tb">ไม่ต้องให้ยาฆ่าพยาธิ</text>
 <text x="386" y="236" class="t2">AED ถ้าชัก</text>
 <text x="386" y="258" class="t2">steroid ถ้ามี ↑ICP/edema</text>
</svg>''', "สองระยะแรกพยาธิยังมีชีวิตจึงได้ประโยชน์จาก albendazole ส่วนสองระยะหลังพยาธิตายแล้ว รักษาเพียงอาการชักและการอักเสบ")

S7 = sec("neuro-04-07", "Neurocysticercosis & brain abscess",
    "Taenia solium · cyst ที่ grey-white junction · viable (scolex, ring enhance) → albendazole + steroid · calcified → AED เท่านั้น · HIV + หูน้ำหนวก + focal deficit → bacterial brain abscess", minutes=7,
    source=f"{D} หน้า 181–189", nl=["2.3.1-3(8)", "B3.2.2-3(1)", "2.3.6-3(6)"],
    md='''
### Neurocysticercosis (NCC)

- เชื้อ **Taenia solium** (พยาธิตืดหมู) — กิน **ไข่** ที่ปนเปื้อนจากคนที่มีพยาธิตัวแก่ (fecal–oral) ไม่ใช่จากกินเนื้อหมูดิบโดยตรง (เสริม)
- อาการ: **ชัก** (สาเหตุ symptomatic epilepsy ที่พบบ่อย), ปวดหัว, focal deficit, ↑ICP (hydrocephalus)
- CT brain: ตำแหน่งที่พบบ่อย **grey-white junction**

[[fig:neuro-04-07-f1]]

| ระยะ | ภาพ | สถานะพยาธิ |
|---|---|---|
| Vesicular | Cyst + **scolex** (จุดใน cyst) | Viable |
| Colloidal | **Ring-enhancing + perilesional edema** | Viable (กำลังตาย) |
| Granular nodular | Nodule หดเล็ก | ตาย |
| **Calcified** | **จุดหินปูน** | ตาย |

### การรักษา (สไลด์)

- **Albendazole** เมื่อเป็น **viable cyst** (scolex, ring enhancement)
- **Steroid** เมื่อมี brain edema — โดยเฉพาะขณะให้ albendazole (พยาธิตาย → inflammatory response มาก)
- **Antiepileptics** เมื่อมีชัก
- **Calcified stage**: **ไม่ต้องให้ยาฆ่าพยาธิ** → AED (± steroid ถ้า ↑ICP)

### Brain abscess (เสริมจากข้อสอบในสไลด์)

- แหล่ง: ลามจาก **หูชั้นกลาง/mastoid** (temporal lobe, cerebellum), sinus (frontal), ฟัน, หรือกระจายทางเลือด (endocarditis)
- อาการ: ปวดหัว ไข้ (มีไม่ถึงครึ่ง) **focal deficit ค่อยเป็นมากขึ้น** ชัก
- CT/MRI: ring-enhancing lesion · Tx: drainage + ATB (ceftriaxone + metronidazole)
- ใน HIV ให้นึกถึง toxoplasmosis (multiple ring-enhancing, basal ganglia) แต่ถ้ามี **หูน้ำหนวก/แก้วหูทะลุ** ข้างเดียวกับรอยโรค → **bacterial brain abscess**
''',
    figs=[F_NCC],
    pearls=[
        "NCC = Taenia solium · ชัก + cyst/calcification ที่ grey-white junction",
        "Scolex/ring enhancement (viable) → albendazole + steroid",
        "Calcified NCC → AED อย่างเดียว ไม่ให้ยาฆ่าพยาธิ",
        "Focal deficit + หูน้ำหนวก → bacterial brain abscess (temporal lobe)",
    ],
    items=[
        mcq("NEURO-04-07-1",
            "A 35-year-old man has his first generalized tonic-clonic seizure. He denies trauma, drug use and fever. Examination is normal except for papilledema. CT brain shows multiple calcified cystic lesions. What is the most likely etiology?",
            "Taenia solium",
            ["Taenia saginata", "Toxocara canis", "Toxoplasma gondii", "Angiostrongylus cantonensis"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 184–185)",
            explain='''ชัก + **multiple calcified cysts** = **neurocysticercosis (Taenia solium)** ระยะ calcified (สไลด์เฉลย: calcified stage, Tx steroid ถ้ามี ICP, AED, ไม่ต้องให้ยาฆ่าพยาธิ)
- Taenia saginata (ตืดวัว) ไม่ทำให้ cysticercosis ในคน
- Toxocara ทำให้ larva migrans ที่ตา/อวัยวะภายใน
- Toxoplasma ในคนภูมิปกติไม่ทำ calcified cysts หลายจุดแบบนี้ (congenital toxo ทำ calcification ในทารก)
- Angiostrongylus ทำ eosinophilic meningitis ไม่ทำ cyst''',
            pearl="ชัก + calcified cysts หลายจุด = neurocysticercosis", topic="Neurocysticercosis",
            ref=[f"{D} หน้า 181–182, 184–185"], nl=["2.3.1-3(8)"]),
        mcq("NEURO-04-07-2",
            "A 30-year-old woman had a generalized tonic-clonic seizure 30 minutes ago; she has never had a seizure before. She completed treatment for neurocysticercosis 6 months ago. Neurological examination and metabolic tests are normal. CT brain shows three small calcified cysts without edema. What is the most appropriate management?",
            "Antiepileptic drug",
            ["Dexamethasone", "Albendazole", "MRI brain", "Surgical excision"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 186–187)",
            explain='''NCC **ระยะ calcified** (พยาธิตายแล้ว) ที่ทำให้ชัก → **antiepileptics** อย่างเดียว ไม่ต้องให้ยาฆ่าพยาธิ (สไลด์เฉลย: Tx antiepileptics, no antiparasite need)
- Dexamethasone ใช้เมื่อมี edema/↑ICP — CT ไม่มี edema
- Albendazole ใช้เฉพาะ viable cyst
- MRI ไม่เปลี่ยนการรักษาเมื่อ CT ชัดว่าเป็น calcified
- ผ่าตัดเฉพาะ intraventricular cyst/hydrocephalus''',
            pearl="Calcified NCC + ชัก → AED", topic="Calcified NCC",
            ref=[f"{D} หน้า 183, 186–187"], nl=["2.3.1-3(8)", "B3.4(3)"]),
        mcq("NEURO-04-07-3",
            "A 24-year-old man from a pig-farming village has a focal seizure. MRI brain shows two cystic lesions at the grey-white junction, each containing an eccentric dot (scolex), with mild surrounding edema. Neurological examination is otherwise normal. In addition to an antiepileptic drug, what is the most appropriate treatment?",
            "Albendazole with corticosteroid",
            ["Corticosteroid alone", "Praziquantel alone without corticosteroid", "Surgical excision of both cysts", "Observation only"],
            explain='''Cyst ที่เห็น **scolex** = **viable cyst** → **albendazole** + **steroid** (มี edema และป้องกันการอักเสบเมื่อพยาธิตาย) + AED (สไลด์)
- Steroid อย่างเดียวไม่กำจัดพยาธิที่ยังมีชีวิต
- Praziquantel ใช้ได้แต่ต้องให้ร่วมกับ steroid — ให้เดี่ยวเสี่ยงสมองบวม
- ผ่าตัดใช้กับ intraventricular cyst/hydrocephalus
- เฝ้าดูอย่างเดียวไม่เหมาะเมื่อเป็น viable cyst ที่มีอาการ''',
            pearl="Viable NCC (scolex) → albendazole + steroid + AED", topic="Viable NCC",
            ref=[f"{D} หน้า 182–183"], nl=["2.3.1-3(8)"]),
        mcq("NEURO-04-07-4",
            "A 20-year-old man with HIV infection has progressive right hemiparesis (grade 2/5) and a right UMN-type facial palsy over 2 weeks. He has purulent discharge from the left ear with tympanic membrane perforation. What is the most likely diagnosis?",
            "Bacterial brain abscess",
            ["Neurocysticercosis", "Cryptococcosis", "Toxoplasmosis", "Primary CNS lymphoma"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (หน้า 188–189)",
            explain='''Focal deficit ซีกขวา (สมองซีกซ้าย) ที่ค่อย ๆ เป็นมากขึ้น + **หูน้ำหนวกซ้าย แก้วหูทะลุ** = เชื้อลามจากหูชั้นกลางเข้า temporal lobe ซ้าย → **bacterial brain abscess** แม้เป็น HIV (เฉลยในสไลด์เป็นภาพ — ตอบตามหลักแหล่งติดเชื้อที่ติดกัน)
- NCC มักมาด้วยชักและ cyst/calcification ไม่สัมพันธ์กับหูน้ำหนวก
- Cryptococcus ทำ meningitis (ปวดหัว OP สูง) มากกว่า focal deficit
- Toxoplasmosis เป็นตัวลวงที่สำคัญใน HIV (multiple ring-enhancing lesions) แต่ไม่อธิบายหูน้ำหนวกข้างเดียวกัน
- Primary CNS lymphoma ไม่เกี่ยวกับการติดเชื้อที่หู''',
            pearl="Focal deficit + otitis media ข้างเดียวกัน = brain abscess", topic="Brain abscess",
            ref=[f"{D} หน้า 188–189"], nl=["2.3.6-3(6)", "B3.2.2-3(1)"]),
    ])

LECTURE = lecture("04", "CNS infection", "Bacterial · CSF · meningococcus · HSV · TB/crypto · eosinophilic · NCC",
    objectives=[
        "บอกเชื้อก่อโรค meningitis ตามอายุและประวัติ (หมู HIV หอย) ได้",
        "รู้ข้อบ่งชี้ CT ก่อน LP และให้ empirical ATB + dexamethasone ได้ถูกต้อง",
        "แปลผล CSF แยก bacteria, virus, TB, fungus, parasite ได้",
        "รักษา HSV encephalitis, TB/crypto meningitis, eosinophilic meningitis และ NCC ตามระยะได้",
        "ให้ chemoprophylaxis แก่ผู้สัมผัส meningococcus ได้",
    ],
    sections=[S1, S2, S3, S4, S5, S6, S7])
