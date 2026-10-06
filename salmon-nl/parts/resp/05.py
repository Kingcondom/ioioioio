from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-Respiratory"
OLD = "ข้อสอบเก่าในสไลด์ MedSalmon"

FIG_CAP = '''<svg viewBox="0 0 740 420">
 <defs><marker id="resp-05-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="200" y="8" width="340" height="68" rx="10" class="acsoft"/>
 <text x="370" y="28" text-anchor="middle" class="tb">CAP → ประเมิน CURB-65</text>
 <text x="370" y="48" text-anchor="middle" class="t3">Confusion · BUN &gt; 20 · RR ≥ 30 · SBP ≤ 90/DBP ≤ 60</text>
 <text x="370" y="66" text-anchor="middle" class="t3">Age ≥ 65 (ข้อละ 1)</text>
 <path d="M260 76L130 106" class="ln" marker-end="url(#resp-05-03-a)"/>
 <path d="M370 76V106" class="ln" marker-end="url(#resp-05-03-a)"/>
 <path d="M480 76L610 106" class="ln" marker-end="url(#resp-05-03-a)"/>
 <rect x="10" y="108" width="240" height="34" rx="8" class="ok"/>
 <text x="130" y="130" text-anchor="middle" class="tw">0–1 → OPD</text>
 <rect x="260" y="108" width="220" height="34" rx="8" class="miss"/>
 <text x="370" y="130" text-anchor="middle" class="tw">≥ 2 → Admit IPD</text>
 <rect x="490" y="108" width="240" height="34" rx="8" class="bad"/>
 <text x="610" y="130" text-anchor="middle" class="tw">≥ 3 → ICU</text>
 <rect x="10" y="154" width="240" height="256" rx="10" class="oksoft"/>
 <text x="130" y="176" text-anchor="middle" class="tb">OPD ไม่มีโรคร่วม</text>
 <text x="22" y="200" class="t2">• Amoxicillin 1 g PO tid</text>
 <text x="22" y="222" class="t2">• Doxycycline 100 mg bid</text>
 <text x="22" y="244" class="t2">• Azithro 500 → 250 mg/d</text>
 <text x="22" y="266" class="t2">• Clarithro 500 mg bid</text>
 <text x="130" y="296" text-anchor="middle" class="tb">OPD มีโรคร่วม</text>
 <text x="22" y="320" class="t2">• Amox/clav, cefuroxime,</text>
 <text x="34" y="340" class="t2">cefpodoxime + macrolide</text>
 <text x="34" y="360" class="t2">หรือ doxycycline</text>
 <text x="22" y="384" class="t2">• หรือ Respiratory FQ</text>
 <rect x="260" y="154" width="220" height="256" rx="10" class="misssoft"/>
 <text x="370" y="176" text-anchor="middle" class="tb">IPD non-ICU</text>
 <text x="272" y="200" class="t2">IV β-lactam:</text>
 <text x="272" y="222" class="t2">• Ceftriaxone 1–2 g OD</text>
 <text x="272" y="244" class="t2">• Cefotaxime 1–2 g q8h</text>
 <text x="272" y="266" class="t2">• Amp-sulbactam</text>
 <text x="272" y="288" class="t2">• Ceftaroline</text>
 <text x="272" y="316" class="ta">+ Macrolide</text>
 <text x="272" y="340" class="t2">หรือ Respiratory FQ</text>
 <text x="272" y="364" class="t3">เดี่ยว (levo, moxi)</text>
 <rect x="490" y="154" width="240" height="256" rx="10" class="badsoft"/>
 <text x="610" y="176" text-anchor="middle" class="tb">ICU</text>
 <text x="502" y="200" class="t2">IV β-lactam</text>
 <text x="502" y="222" class="t3">(ceftriaxone, cefotaxime,</text>
 <text x="502" y="240" class="t3">amp-sulbactam, ceftaroline)</text>
 <text x="502" y="268" class="ta">+ Macrolide</text>
 <text x="502" y="292" class="t2">หรือ</text>
 <text x="502" y="316" class="ta">+ Respiratory FQ</text>
 <text x="502" y="348" class="t3">ต้องเป็นยาคู่เสมอ</text>
 <text x="502" y="388" class="t3">ระยะเวลา ATB 5–7 วัน</text>
</svg>'''

S1 = sec("resp-05-01", "Influenza",
    "ไข้สูงเฉียบพลัน ปวดเมื่อยมาก · กลุ่มเสี่ยง (BMI > 30, ตั้งครรภ์, อายุ < 2/> 60, โรคเรื้อรัง) → oseltamivir 5 วัน",
    minutes=6, source=f"{D} หน้า 258–270", nl=["2.3.1(11)", "B6.2.2(9)"],
    md='''
### เชื้อและการระบาด
- Influenza A, B · ติดต่อทาง **respiratory droplets**
- **Antigenic drift** (point mutation) → **epidemic** (ระบาดตามฤดูกาล) · **Antigenic shift** (reassortment ของ gene segment ระหว่างสายพันธุ์) → **pandemic** — จึงมีสายพันธุ์ใหม่ตลอด ต้องฉีดวัคซีนทุกปี

### อาการ
- **ไข้สูงเฉียบพลัน**, ปวดศีรษะ, **ปวดเมื่อยกล้ามเนื้อมาก (myalgia)**, อ่อนเพลีย
- คลื่นไส้อาเจียน, ไอ, เจ็บคอ
- แยกกับ **common cold**: หวัดเด่นที่น้ำมูก จาม คัดจมูก ไม่ค่อยมีไข้สูงหรือปวดกล้ามเนื้อ

### ภาวะแทรกซ้อน
- **Pneumonia** จาก influenza เอง หรือ secondary bacterial: **S. pneumoniae, S. aureus, H. influenzae**

### การวินิจฉัย
- **Clinical diagnosis** เป็นหลัก · nasopharyngeal swab (rapid test/PCR) เมื่ออาการรุนแรง

### กลุ่มเสี่ยงสูง (high risk)
| กลุ่ม |
|---|
| **อ้วน BMI > 30** |
| **ตั้งครรภ์ / หลังคลอด ≤ 14 วัน** |
| อายุ < 2 ปี หรือ > 60 ปี (สไลด์ใช้ > 60; CDC ใช้ ≥ 65) |
| โรคเรื้อรัง: asthma, COPD, หัวใจ, ตับ, ไต, **DM**, มะเร็ง |
| ภูมิคุ้มกันต่ำ / ได้ยากดภูมิ |
| อายุ < 18 ปี + ได้ aspirin (เสี่ยง **Reye syndrome**) |
| โรคพันธุกรรม, เด็กที่มีความบกพร่องทางระบบประสาทรุนแรง พัฒนาการช้า ลมชัก |

### การรักษา
| กลุ่ม | การรักษา |
|---|---|
| อาการน้อย + ไม่มีความเสี่ยง | supportive (ORS, paracetamol, ยาแก้ไอ) **± oseltamivir 5 วัน** (หายเร็วขึ้น) |
| **อาการรุนแรง หรือ กลุ่มเสี่ยง** | **oseltamivir PO 5 วัน** (ให้ได้แม้เกิน 48 ชม. — เสริม) |
| ป้องกัน | **วัคซีนไข้หวัดใหญ่ทุกปี** |

> โจทย์ชอบให้ "น้ำหนัก 100 kg" หรือบอกว่าตั้งครรภ์มาเป็นใบ้ → กลุ่มเสี่ยง → **oseltamivir**

> **ไม่ใช่** กลุ่มเสี่ยงของตัวผู้ป่วยเอง: แค่ "อยู่บ้านเดียวกับพ่อที่สูงอายุและเป็น COPD" (นั่นคือข้อบ่งชี้ chemoprophylaxis ของพ่อ ไม่ใช่การรักษาผู้ป่วย — ข้อสอบเก่า)
''',
    pearls=["Drift → epidemic · shift → pandemic",
            "Flu: ไข้สูงเฉียบพลัน + ปวดเมื่อยกล้ามเนื้อมาก · หวัดธรรมดา: น้ำมูกเด่น ไข้ต่ำ",
            "High risk: BMI > 30, ตั้งครรภ์/หลังคลอด ≤ 14 วัน, < 2 ปี/> 60 ปี, โรคเรื้อรัง, ภูมิคุ้มกันต่ำ, เด็ก + aspirin",
            "Severe หรือ high risk → oseltamivir 5 วัน",
            "Secondary bacterial pneumonia หลัง flu: S. pneumoniae, S. aureus"],
    items=[
        mcq("RESP-05-01-1", """A 40-year-old Thai woman weighing 100 kg (BMI 38) has fever, cough and severe myalgia. Her daughter had the same symptoms last week. BT 39°C, BP 100/70 mmHg, RR 28/min. What is the most appropriate management?""",
            "Oseltamivir for 5 days",
            ["Ibuprofen and supportive care only", "Amoxicillin", "Roxithromycin", "Orphenadrine–paracetamol"],
            explain="""อาการเข้ากับ influenza (ไข้สูง ปวดเมื่อยมาก มีคนในบ้านป่วย) และผู้ป่วยอ้วนมาก (BMI > 30) จึงเป็นกลุ่มเสี่ยง ต้องได้ oseltamivir 5 วัน
- Supportive care อย่างเดียวพอเฉพาะคนที่อาการน้อยและไม่มีความเสี่ยง
- Amoxicillin และ roxithromycin เป็นยาฆ่าเชื้อแบคทีเรีย ไม่มีผลต่อ influenza
- Orphenadrine–paracetamol บรรเทาอาการปวด แต่ไม่ได้รักษาเชื้อในผู้ป่วยกลุ่มเสี่ยง""",
            pearl="Flu + อ้วน (BMI > 30) → oseltamivir",
            topic="Influenza high risk", ref=[f"{D} หน้า 260, 262, 265–268"], nl=["2.3.1(11)"], kind="old", src=OLD),
        mcq("RESP-05-01-2", """A 32-year-old woman has had low-grade fever, sore throat, mild cough, rhinorrhea and mild myalgia for 3 days. She has no dyspnea and stable vital signs. She is worried about pandemic influenza. In which of the following situations would oseltamivir NOT be indicated for her own treatment?""",
            "She is otherwise healthy but lives with her elderly father who has COPD",
            ["She has obesity with BMI 34", "She has type 2 diabetes mellitus",
             "She is 20 weeks pregnant", "She is taking immunosuppressive drugs"],
            explain="""การอยู่บ้านเดียวกับผู้สูงอายุที่เป็น COPD ไม่ได้ทำให้ตัวผู้ป่วยเป็นกลุ่มเสี่ยง ผู้ป่วยอาการน้อยและไม่มีความเสี่ยงเอง จึงรักษาแบบ supportive ได้ (คนที่ควรพิจารณาให้ยาป้องกันคือพ่อ)
- อ้วน BMI > 30 เป็นกลุ่มเสี่ยงตามสไลด์
- DM เป็นโรคเรื้อรังที่อยู่ในกลุ่มเสี่ยง
- การตั้งครรภ์เป็นกลุ่มเสี่ยงสูง
- การได้ยากดภูมิคุ้มกันเป็นกลุ่มเสี่ยง""",
            pearl="Oseltamivir ให้ตามความเสี่ยงของตัวผู้ป่วยเอง",
            topic="Oseltamivir indication", ref=[f"{D} หน้า 260, 269–270"], nl=["2.3.1(11)"], kind="old", src=OLD),
        mcq("RESP-05-01-3", """A 30-year-old healthy woman has high-grade fever for 5 days with cough, sneezing, rhinorrhea and severe malaise. Pharynx is injected and lungs are clear. CBC: WBC 9,000 (N70, L30), platelets 200,000. CXR is normal. What is the most appropriate management?""",
            "Paracetamol and supportive care",
            ["Ceftriaxone", "Doxycycline", "Azithromycin", "Oseltamivir plus azithromycin"],
            explain="""ผู้ป่วยแข็งแรงดีและไม่มีปัจจัยเสี่ยง ปอด clear CXR ปกติ ไม่มีภาวะแทรกซ้อน รักษาแบบประคับประคองด้วย paracetamol พักผ่อน และดื่มน้ำ ตามเฉลยข้อสอบเก่าในสไลด์ (oseltamivir เป็นทางเลือกได้ในคนที่ไม่เสี่ยง แต่ให้หลังมีอาการมา 5 วันแล้วได้ประโยชน์น้อย)
- Ceftriaxone, doxycycline และ azithromycin ไม่ได้รักษาโรคจากไวรัส และไม่มีหลักฐานของแบคทีเรีย
- Oseltamivir ร่วมกับ azithromycin เป็นการให้ ATB โดยไม่จำเป็น""",
            pearl="Flu ไม่มีความเสี่ยง ไม่มีแทรกซ้อน → supportive (± oseltamivir)",
            topic="Influenza low risk", ref=[f"{D} หน้า 262–264"], nl=["2.3.1(11)"], kind="old", src=OLD),
        mcq("RESP-05-01-4", """A new influenza A strain emerges through reassortment of gene segments between avian and human viruses, causing a worldwide outbreak. Which mechanism best explains this pandemic?""",
            "Antigenic shift",
            ["Antigenic drift", "Phase variation", "Transformation", "Latency and reactivation"],
            explain="""Antigenic shift คือการสลับชิ้นส่วนยีน (reassortment) ระหว่างเชื้อต่างสายพันธุ์ ทำให้เกิด HA หรือ NA ชนิดใหม่ที่ประชากรไม่มีภูมิคุ้มกัน จึงระบาดใหญ่ทั่วโลก (pandemic)
- Antigenic drift เป็น point mutation ทีละน้อย ทำให้ระบาดตามฤดูกาล (epidemic)
- Phase variation เป็นกลไกของแบคทีเรีย
- Transformation คือการรับ DNA เข้าเซลล์แบคทีเรีย
- Latency/reactivation เป็นลักษณะของ herpesvirus""",
            pearl="Shift = reassortment = pandemic",
            topic="Antigenic shift", ref=[f"{D} หน้า 258"], nl=["B6.2.2(9)"]),
    ])

S2 = sec("resp-05-02", "CAP: typical vs atypical และเชื้อตามความเสี่ยง",
    "Typical (S. pneumo, H. flu, M. cat) vs atypical (Mycoplasma, Chlamydia, Legionella) · เชื้อตามบริบท: IVDU→S. aureus, aspiration→anaerobe",
    minutes=7, source=f"{D} หน้า 116–123, 131–140", nl=["2.3.10(5)", "B6.2.2(4)"],
    md='''
### Typical vs Atypical pneumonia
| | Typical | Atypical |
|---|---|---|
| เชื้อ | **S. pneumoniae, H. influenzae, M. catarrhalis** | **Mycoplasma pneumoniae, Chlamydia pneumoniae, Legionella**, virus |
| Onset | เฉียบพลัน | ค่อยเป็นค่อยไป ("walking pneumonia") |
| ไข้ | สูง | ต่ำ |
| ไอ | มีเสมหะ | ไอแห้ง / เสมหะน้อย |
| ตรวจปอด | crepitation, bronchial breath sound, tactile fremitus ↑, egophony | มักพบน้อยกว่าที่ CXR เห็น (เสริม) |
| นอกปอด | — | อ่อนเพลีย ปวดศีรษะ เจ็บคอ ปวดกล้ามเนื้อ |
| CXR | **alveolar infiltrate/consolidation** (lobar, bronchopneumonia) | **perihilar interstitial** (reticular/reticulonodular) |

- Typical: sputum G/S, culture · hemoculture เมื่อรุนแรง
- **Mycoplasma** มีอาการนอกปอดได้: ผื่น, erythema multiforme, **hemolytic anemia, cold agglutinin titer ↑**, **bullous myringitis** (หูอักเสบตุ่มน้ำ)

### เชื้อตามปัจจัยเสี่ยง/อาการจำเพาะ
| บริบท | เชื้อ |
|---|---|
| ติดสุรา | S. pneumoniae, H. influenzae (Klebsiella — เสริม) |
| **COPD / สูบบุหรี่จัด** | S. pneumoniae, **H. influenzae**, M. catarrhalis |
| Aspiration / ฟันผุ | **anaerobes** |
| **IVDU / skin infection** | **S. aureus** (hematogenous → multiple patchy infiltrates) |
| หลัง influenza | S. pneumoniae, **S. aureus** |
| **Bullous myringitis** | **Mycoplasma** |
| **Relative bradycardia** (+ ท้องเสีย, Na ต่ำ — เสริม) | **Legionella** |

#### Gram stain ที่ข้อสอบชอบ
- Gram-positive diplococci (lancet-shaped) → S. pneumoniae
- **Gram-negative pleomorphic coccobacilli** → **H. influenzae** (ผู้สูบบุหรี่/COPD)
- **Gram-negative rod with capsule** → **Klebsiella pneumoniae** (ติดสุรา, DM, เสมหะ currant-jelly — เสริม)
- Gram-positive cocci in clusters → S. aureus

> ข้อสอบเก่า: ไข้ ไอแห้ง เหนื่อย **ปวดหู (tympanic membrane บวมแดง)** และท้องเสีย → **Mycoplasma** (bullous myringitis) — ถึงจะมีท้องเสียซึ่งชวนให้นึกถึง Legionella แต่ PR 80 ขณะมีไข้ ไม่ได้บอก relative bradycardia ชัด สไลด์เฉลย Mycoplasma
''',
    pearls=["Typical: ไข้สูง เสมหะ consolidation · atypical: ไข้ต่ำ ไอแห้ง interstitial infiltrate",
            "Bullous myringitis / cold agglutinin / hemolysis → Mycoplasma",
            "Relative bradycardia → Legionella",
            "IVDU / skin infection / post-flu → S. aureus",
            "COPD/smoker + GN coccobacilli → H. influenzae"],
    items=[
        mcq("RESP-05-02-1", """A 30-year-old man has had fever for 4 days and dry cough, dyspnea, ear pain and diarrhea for 2 days. BT 38°C, HR 80/min. Examination: mildly injected pharynx, erythematous bulging right tympanic membrane with vesicles, fine crackles at the right lower lung. WBC 15,000. CXR: patchy infiltration of the RLL. What is the most likely diagnosis?""",
            "Mycoplasma pneumoniae pneumonia",
            ["Legionella pneumophila pneumonia", "Chlamydophila pneumoniae pneumonia",
             "Klebsiella pneumoniae pneumonia", "Streptococcus pneumoniae pneumonia"],
            explain="""Atypical pneumonia ร่วมกับ bullous myringitis (แก้วหูบวมแดงมีตุ่มน้ำ ปวดหู) เป็นลักษณะจำเพาะของ Mycoplasma ตามสไลด์
- Legionella มีท้องเสียได้ แต่ลักษณะเด่นคือ relative bradycardia, Na ต่ำ และอาการรุนแรง ไม่ใช่ bullous myringitis
- Chlamydophila มักมีเสียงแหบหรือ laryngitis
- Klebsiella เป็น lobar pneumonia เสมหะ currant-jelly ในคนติดสุรา
- S. pneumoniae ให้ภาพ typical (ไข้สูงเฉียบพลัน เสมหะสนิม lobar consolidation)""",
            pearl="Bullous myringitis → Mycoplasma",
            topic="Mycoplasma", ref=[f"{D} หน้า 117–118, 133–134"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-05-02-2", """A 28-year-old man has had fever, cough and dyspnea with orthopnea for 5 days. BT 39°C, HR 100/min, RR 24/min. There are multiple infection scars on the extremities. CXR: multiple patchy infiltrates in both lungs. What is the most likely organism?""",
            "Staphylococcus aureus",
            ["Streptococcus pyogenes", "Haemophilus influenzae", "Streptococcus viridans", "Mycoplasma pneumoniae"],
            explain="""แผลติดเชื้อหลายแห่งตามแขนขา (นึกถึง IVDU หรือ skin infection) ร่วมกับ infiltrate หลายจุดทั้งสองปอด เข้ากับ hematogenous spread ของ S. aureus (septic emboli) ตามสไลด์
- S. pyogenes ทำให้เกิด pneumonia ได้น้อย และไม่ใช่สาเหตุของ septic emboli ในคนฉีดยา
- H. influenzae พบในผู้สูบบุหรี่หรือ COPD
- Strep viridans ทำให้เกิด subacute endocarditis ที่ลิ้นฝั่งซ้าย ไม่ค่อยมี septic emboli ไปปอด
- Mycoplasma เป็น atypical pneumonia ไม่สัมพันธ์กับแผลที่ผิวหนัง""",
            pearl="IVDU/skin infection + multiple patchy infiltrates → S. aureus",
            topic="S. aureus pneumonia", ref=[f"{D} หน้า 118, 135–138"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-05-02-3", """A 65-year-old man who smokes 20 pack-years has fever and green sputum for 3 days. Sputum Gram stain shows gram-negative pleomorphic coccobacilli. What is the most appropriate oral antibiotic?""",
            "Cefuroxime",
            ["Oseltamivir", "Clindamycin", "Doxycycline", "Cloxacillin"],
            explain="""ผู้สูบบุหรี่จัดและ Gram stain เป็น gram-negative pleomorphic coccobacilli นึกถึง H. influenzae ซึ่งมักสร้าง β-lactamase ยาที่ครอบคลุมคือ cephalosporin รุ่น 2–3 เช่น PO cefuroxime หรือ cefpodoxime (IV ceftriaxone หรือ cefotaxime) ตามเฉลยในสไลด์
- Oseltamivir เป็นยาต้านไวรัส
- Clindamycin ไม่ครอบคลุม gram-negative
- Doxycycline ครอบคลุมได้บ้าง แต่ไม่ใช่คำตอบในสไลด์
- Cloxacillin ครอบคลุมเฉพาะ staphylococcus""",
            pearl="GN pleomorphic coccobacilli = H. influenzae → 2nd/3rd gen cephalosporin",
            topic="H. influenzae", ref=[f"{D} หน้า 153–154"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-05-02-4", """A 60-year-old man who smoked heavily until 2–3 years ago has fever, dyspnea, yellow-green sputum and right-sided chest pain. Breath sounds are decreased over the RUL area, and CXR shows RUL infiltration. Spirometry last year showed COPD. Which group of organisms is most likely?""",
            "S. pneumoniae, H. influenzae and Moraxella catarrhalis",
            ["Pseudomonas aeruginosa and Acinetobacter baumannii", "Anaerobes and Streptococcus milleri",
             "Mycoplasma and Chlamydophila only", "Pneumocystis jirovecii"],
            explain="""Pneumonia ในผู้ป่วย COPD เชื้อที่พบบ่อยตามสไลด์คือ S. pneumoniae, H. influenzae และ M. catarrhalis
- Pseudomonas และ Acinetobacter เป็นเชื้อของ HAP/VAP
- Anaerobes สัมพันธ์กับ aspiration และ lung abscess
- Atypical pathogens พบได้ แต่ไม่ใช่กลุ่มหลักใน COPD ที่มีเสมหะเป็นหนอง
- PCP พบในผู้ที่ภูมิคุ้มกันต่ำ""",
            pearl="COPD pneumonia: S. pneumo, H. flu, M. cat",
            topic="COPD pneumonia", ref=[f"{D} หน้า 118, 131–132"], nl=["2.3.10(5)"], kind="old", src=OLD),
    ])

S3 = sec("resp-05-03", "CAP: CURB-65 และการเลือกยาปฏิชีวนะ",
    "CURB-65 0–1 OPD, ≥ 2 admit, ≥ 3 ICU · OPD: amox/doxy/macrolide · IPD: β-lactam + macrolide หรือ resp FQ · 5–7 วัน",
    minutes=8, source=f"{D} หน้า 124–130, 141–152", nl=["2.3.10(5)", "2.2.7", "2.2.48"],
    md='''
### CURB-65 (ข้อละ 1 คะแนน)
- **C**onfusion
- **U**rea: BUN > 20 mg/dL
- **R**R ≥ 30/min
- **B**P: SBP ≤ 90 หรือ DBP ≤ 60 mmHg
- อายุ ≥ **65** ปี

| คะแนน | ที่รักษา |
|---|---|
| 0–1 | OPD |
| ≥ 2 | admit IPD |
| ≥ 3 | admit ICU |

> นอกจากคะแนน ให้ดูความรุนแรงทางคลินิกด้วย: **ใช้ accessory muscles, paradoxical breathing, ต้องใช้ O2 mask with bag** = severe → รักษาแบบ IPD/ICU

### การรักษาเบื้องต้น
- ABC, O2, ETT เมื่อ respiratory failure, **IV fluid resuscitation**
- ATB **5–7 วัน**
- Septic shock: **fluid resuscitation ก่อน** (crystalloid เช่น NSS 30 mL/kg — เสริม) แล้วจึง NE ถ้า MAP ยังต่ำ

[[fig:resp-05-03-cap]]

### ขนาดยาตามสไลด์
| กลุ่ม | ยา |
|---|---|
| OPD ไม่มีโรคร่วม | **Amoxicillin 1 g PO tid** · **Doxycycline 100 mg PO bid** · **Azithromycin 500 mg วันแรก แล้ว 250 mg/วัน** · **Clarithromycin 500 mg PO bid** |
| OPD มีโรคร่วม (DM, ปอด, หัวใจ, ไต, ตับ) | **Amox/clav 875/125 mg PO bid**, cefuroxime, cefpodoxime **+ macrolide หรือ doxycycline** · หรือ respiratory FQ PO (gemifloxacin, moxifloxacin, levofloxacin) |
| IPD non-ICU | IV β-lactam: **amp-sulbactam 1.5–3 g IV q6h**, ceftaroline, **ceftriaxone 1–2 g IV OD**, **cefotaxime 1–2 g IV q8h** **+ macrolide** (azithro 500 mg IV 2 วัน แล้ว 500 mg PO/วัน หรือ clarithro 500 mg bid) · หรือ respiratory FQ |
| ICU | IV β-lactam **+ macrolide** หรือ IV β-lactam **+ respiratory FQ** |

> **Atypical (interstitial infiltrate) ในคนอายุน้อยที่แข็งแรง** → **oral macrolide** (azithromycin, clarithromycin, roxithromycin)

> คำตอบ "Ceftriaxone + clarithromycin/azithromycin" เป็นคำตอบมาตรฐานของ CAP ที่ต้อง admit — ไม่ใช่ pip/tazo, ceftazidime, imipenem (เก็บไว้ HAP/Pseudomonas)

> ข้อสอบเก่า: อายุ 65 ปี BUN 8 sputum เป็น **GN rod with capsule (Klebsiella)** → ตอบ **ceftriaxone + azithromycin** (ยังเป็น CAP เชื้อ Klebsiella ไวต่อ 3rd-gen cephalosporin)
''',
    figs=[fig("resp-05-03-cap", "CURB-65 → สถานที่รักษา → ยา", FIG_CAP,
              "คะแนน CURB-65 บอกว่าควรรักษาที่ไหน แต่ละที่มี regimen ของตัวเอง; ผู้ป่วยใน ICU ต้องได้ยาคู่เสมอ")],
    pearls=["CURB-65: confusion, BUN > 20, RR ≥ 30, SBP ≤ 90/DBP ≤ 60, อายุ ≥ 65",
            "0–1 OPD · ≥ 2 admit · ≥ 3 ICU",
            "IPD: ceftriaxone 1–2 g OD + macrolide (หรือ respiratory FQ เดี่ยว)",
            "ICU: β-lactam + macrolide หรือ β-lactam + resp FQ",
            "Atypical ในคนหนุ่มสาว OPD → oral macrolide"],
    items=[
        mcq("RESP-05-03-1", """A 70-year-old man has had fever and tachypnea for 3 days. BT 38°C, HR 120/min, BP 140/90 mmHg, RR 30/min. He uses accessory muscles with paradoxical breathing, and fine crackles are heard at the RLL. SpO2 95% on an O2 mask with bag at 10 L/min. He has no recent hospitalization. What is the most appropriate antibiotic regimen?""",
            "IV ceftriaxone plus clarithromycin",
            ["Cefazolin", "Ciprofloxacin", "Piperacillin/tazobactam", "Oral amoxicillin"],
            explain="""Severe CAP (RR 30 อายุ ≥ 65 ใช้ accessory muscles ต้องใช้ O2 mask with bag) ต้อง admit และให้ IV β-lactam ร่วมกับ macrolide เช่น ceftriaxone + clarithromycin หรือ azithromycin
- Cefazolin (รุ่นที่ 1) ครอบคลุม S. pneumoniae และ H. influenzae ได้ไม่ดี และไม่ครอบคลุม atypical
- Ciprofloxacin ไม่ใช่ respiratory FQ เพราะครอบคลุม pneumococcus ได้ไม่ดี
- Pip/tazo เป็นยาสำหรับ HAP หรือ Pseudomonas ซึ่งผู้ป่วยไม่มีปัจจัยเสี่ยง
- Amoxicillin PO เป็นยาของ OPD""",
            pearl="Severe CAP → ceftriaxone + macrolide",
            topic="CAP IPD", ref=[f"{D} หน้า 126, 129–130, 145–146"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-05-03-2", """An 18-year-old previously healthy man has fever, cough and mild dyspnea. He is alert, RR 20/min, BP 118/72 mmHg. CXR shows bilateral interstitial infiltration. What is the most appropriate antibiotic?""",
            "Roxithromycin (oral macrolide)",
            ["Ampicillin", "Ciprofloxacin", "Gentamicin", "Amoxicillin/clavulanate"],
            explain="""ผู้ป่วยอายุน้อย แข็งแรงดี CURB-65 = 0 และ CXR เป็น interstitial infiltrate นึกถึง atypical pneumonia (Mycoplasma) ยาที่ครอบคลุมคือ macrolide ชนิดรับประทาน
- Ampicillin และ amox/clav เป็น β-lactam ซึ่ง Mycoplasma ไม่มี cell wall จึงไม่ได้ผล
- Ciprofloxacin ไม่ใช่ทางเลือกของ CAP ทั่วไป
- Gentamicin ไม่ครอบคลุม atypical และมีพิษต่อไต""",
            pearl="Atypical pneumonia OPD → macrolide (ไม่ใช่ β-lactam)",
            topic="Atypical CAP", ref=[f"{D} หน้า 127, 143–144"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-05-03-3", """A 65-year-old man with severe pneumonia has been intubated and given IV antibiotics. BT 39°C, BP 80/50 mmHg, HR 124/min. He has received no fluid yet. Lungs have bilateral crackles but there is no history of heart failure. What is the most appropriate next step?""",
            "IV normal saline bolus",
            ["Gelatin solution", "Norepinephrine without fluid", "Dopamine", "Dobutamine"],
            explain="""Septic shock จาก pneumonia ต้องเริ่มด้วย crystalloid resuscitation ก่อน (NSS หรือ balanced solution 30 mL/kg — เสริม) ถ้า MAP ยัง < 65 จึงให้ norepinephrine ตามเฉลยข้อสอบเก่าในสไลด์
- Gelatin (colloid สังเคราะห์) ไม่แนะนำ เพราะเพิ่มความเสี่ยงต่อไต
- NE ใช้เมื่อให้สารน้ำแล้วยังความดันต่ำ หรือให้ควบคู่กันถ้าความดันต่ำมาก แต่ไม่ใช่แทนการให้สารน้ำ
- Dopamine ทำให้เกิด arrhythmia มากกว่า NE
- Dobutamine เป็น inotrope ใช้ใน cardiogenic shock และอาจทำให้ความดันต่ำลงอีก""",
            pearl="Septic shock → crystalloid ก่อน แล้ว NE",
            topic="Septic shock", ref=[f"{D} หน้า 125, 141–142"], nl=["2.2.7", "2.2.48"], kind="old", src=OLD),
        mcq("RESP-05-03-4", """A 72-year-old woman with pneumonia is confused. BUN 28 mg/dL, RR 32/min, BP 100/58 mmHg. What is her CURB-65 score and the appropriate site of care?""",
            "5 — admit to ICU",
            ["3 — outpatient treatment", "4 — general ward", "2 — outpatient treatment", "1 — outpatient treatment"],
            explain="""นับทีละข้อ: confusion (1), BUN 28 > 20 (1), RR 32 ≥ 30 (1), DBP 58 ≤ 60 (1) และอายุ 72 ≥ 65 (1) รวมเป็น 5 คะแนน ซึ่ง ≥ 3 → ICU
- 3 คะแนนเกิดจากลืมนับ DBP หรืออายุ และถึงได้ 3 ก็ต้องเข้า ICU ไม่ใช่รักษาแบบ OPD
- 4 คะแนนพลาดไปหนึ่งข้อ และการรับไว้ใน ward ทั่วไปไม่พอ
- 2 และ 1 คะแนนนับขาดไปหลายข้อ""",
            pearl="CURB-65 ≥ 3 → ICU",
            topic="CURB-65", ref=[f"{D} หน้า 124"], nl=["2.3.10(5)"]),
        mcq("RESP-05-03-5", """A 70-year-old woman with no underlying disease has had fever, dyspnea and productive cough for 3 days. She is alert, RR 24/min, BP 128/76 mmHg, BUN 24 mg/dL. CXR shows lobar consolidation. She is admitted to the general ward. What is the most appropriate antibiotic treatment?""",
            "Ceftriaxone plus clarithromycin",
            ["Ceftazidime", "Piperacillin/tazobactam", "Imipenem", "Cefotaxime alone"],
            explain="""CURB-65 = 2 (อายุ ≥ 65 และ BUN > 20) จึง admit แบบ non-ICU และให้ IV β-lactam ร่วมกับ macrolide เช่น ceftriaxone + clarithromycin
- Ceftazidime ครอบคลุม Pseudomonas แต่ครอบคลุม S. pneumoniae ได้ไม่ดี จึงไม่ใช่ยาของ CAP
- Pip/tazo และ imipenem เป็นยา broad-spectrum สำหรับ HAP หรือ Pseudomonas
- Cefotaxime เดี่ยวไม่ครอบคลุม atypical ต้องให้คู่กับ macrolide""",
            pearl="CAP ward: 3rd-gen ceph + macrolide",
            topic="CAP ward", ref=[f"{D} หน้า 129, 149–150"], nl=["2.3.10(5)"], kind="old", src=OLD),
    ])

S4 = sec("resp-05-04", "Hospital-acquired pneumonia (HAP)",
    "Pneumonia หลัง admit > 48 ชม. หรือ D/C < 3 เดือน · เชื้อ GNB ดื้อยา (Pseudomonas, Acinetobacter) · ให้ยาครอบคลุม Pseudomonas",
    minutes=4, source=f"{D} หน้า 155–159", nl=["2.3.10(5)"],
    md='''
### นิยาม
- Pneumonia ที่เกิด **หลัง admit > 48 ชม.** หรือ **หลัง D/C < 3 เดือน** (ตามสไลด์)
- VAP (ventilator-associated pneumonia) คือ pneumonia ที่เกิดหลังใส่ท่อช่วยหายใจ > 48 ชม. (เสริม)

### เชื้อ
- **P. aeruginosa, A. baumannii**, E. coli, K. pneumoniae, Enterobacter spp., S. aureus

### การรักษา — IV ATB ที่ครอบคลุม P. aeruginosa
| กลุ่มยา | ตัวอย่าง |
|---|---|
| Carbapenem | **imipenem, meropenem** (ไม่ใช่ ertapenem — เสริม) |
| Anti-pseudomonal cephalosporin | **ceftazidime**, cefoperazone, **cefepime** |
| Anti-pseudomonal penicillin | **piperacillin/tazobactam** |

- เติม **vancomycin** เมื่อเสี่ยง MRSA (เห็น GPC in clusters, เคยมี MRSA — เสริม)
- เลือกยาตาม local antibiogram และอาการ (shock/VAP → เลือกยาที่ครอบคลุมกว้าง เช่น carbapenem — เสริม)

> **Ceftriaxone, ampicillin/sulbactam, levofloxacin เดี่ยว** ไม่ครอบคลุม Pseudomonas ดีพอ → ไม่ใช่คำตอบของ HAP

> Amikacin เดี่ยวไม่ใช้ใน pneumonia (ซึมเข้าเนื้อปอดได้ไม่ดี — เสริม)
''',
    pearls=["HAP = > 48 ชม. หลัง admit หรือ < 3 เดือนหลัง D/C",
            "เชื้อ: Pseudomonas, Acinetobacter, Enterobacterales, S. aureus",
            "ยา: carbapenem (imipenem/meropenem), ceftazidime/cefepime, pip/tazo",
            "สงสัย MRSA → เติม vancomycin"],
    items=[
        mcq("RESP-05-04-1", """A 68-year-old man admitted for STEMI develops fever, productive cough and dyspnea on hospital day 7. Sputum Gram stain shows numerous gram-negative bacilli. What is the most appropriate empirical antibiotic?""",
            "Ceftazidime",
            ["Ampicillin/sulbactam", "Ceftriaxone", "Levofloxacin", "Amikacin"],
            explain="""Pneumonia ที่เกิดหลัง admit นานกว่า 48 ชม. คือ HAP และ GNB ต้องครอบคลุม P. aeruginosa ในตัวเลือก มีเพียง ceftazidime ที่เป็น anti-pseudomonal β-lactam
- Ampicillin/sulbactam ไม่ครอบคลุม Pseudomonas
- Ceftriaxone เป็นยาของ CAP ไม่ครอบคลุม Pseudomonas
- Levofloxacin มีฤทธิ์ต่อ Pseudomonas บ้าง แต่ไม่แนะนำให้ใช้เดี่ยวเป็น empirical และไม่ใช่เฉลยในสไลด์
- Amikacin เดี่ยวเข้าเนื้อปอดได้ไม่ดี จึงไม่ใช้เป็นยาเดี่ยว""",
            pearl="HAP + GNB → anti-pseudomonal β-lactam",
            topic="HAP", ref=[f"{D} หน้า 155–157"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-05-04-2", """A 70-year-old man with hemorrhagic stroke has been intubated in the ICU for 5 days and now has fever. BT 39°C, HR 100/min, BP 90/70 mmHg. Crackles at the RLL. Sputum Gram stain: numerous PMNs and gram-negative bacilli. What is the most appropriate empirical antibiotic?""",
            "Imipenem",
            ["Amikacin", "Ceftriaxone", "Levofloxacin", "Vancomycin"],
            explain="""ใส่ท่อช่วยหายใจ 5 วันแล้วเกิด pneumonia คือ VAP ที่มีความดันค่อนข้างต่ำ Gram stain เป็น GNB จึงต้องให้ยาครอบคลุม Pseudomonas และเชื้อดื้อยาได้กว้าง เช่น imipenem
- Amikacin เดี่ยวเข้าปอดได้ไม่ดี
- Ceftriaxone ไม่ครอบคลุม Pseudomonas
- Levofloxacin เดี่ยวไม่พอสำหรับ VAP ที่รุนแรง
- Vancomycin ครอบคลุมเฉพาะ gram-positive (MRSA) ไม่ครอบคลุม GNB ที่เห็นใน Gram stain""",
            pearl="VAP + GNB + hemodynamic ไม่ดี → carbapenem",
            topic="VAP", ref=[f"{D} หน้า 155, 158–159"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-05-04-3", """A 74-year-old woman was discharged 6 weeks ago after a 10-day admission for urosepsis. She now presents with fever, purulent sputum and new RLL consolidation. How should this pneumonia be classified for empirical therapy per the lecture?""",
            "Hospital-acquired pneumonia, requiring antipseudomonal coverage",
            ["Typical community-acquired pneumonia treated with amoxicillin",
             "Atypical pneumonia treated with a macrolide alone",
             "Aspiration pneumonia treated with metronidazole alone",
             "Viral pneumonia requiring oseltamivir only"],
            explain="""ตามสไลด์ pneumonia ที่เกิดภายใน 3 เดือนหลังจำหน่ายจากโรงพยาบาลจัดเป็น HAP เพราะมีโอกาสติดเชื้อดื้อยาจากโรงพยาบาล จึงต้องให้ยาที่ครอบคลุม Pseudomonas
- Amoxicillin เป็นยาของ CAP แบบ OPD ไม่ครอบคลุม GNB ที่ดื้อยา
- Macrolide เดี่ยวใช้กับ atypical pneumonia ในคนอายุน้อย
- Metronidazole เดี่ยวครอบคลุมแค่ anaerobes
- Oseltamivir ไม่ครอบคลุมแบคทีเรีย""",
            pearl="D/C < 3 เดือน = HAP (ตามสไลด์)",
            topic="HAP definition", ref=[f"{D} หน้า 155"], nl=["2.3.10(5)"]),
    ])

LECTURE = lecture("05", "Influenza & Pneumonia",
    subtitle="influenza · CAP typical/atypical · CURB-65 · HAP",
    objectives=["แยก influenza จากหวัดธรรมดา และระบุกลุ่มเสี่ยงที่ต้องได้ oseltamivir ได้",
                "แยก typical กับ atypical pneumonia และบอกเชื้อตามบริบทหรือ Gram stain ได้",
                "ใช้ CURB-65 ตัดสินใจสถานที่รักษาและเลือก ATB พร้อมขนาดยาได้",
                "รักษา HAP/VAP ด้วยยาที่ครอบคลุม Pseudomonas ได้"],
    sections=[S1, S2, S3, S4])
