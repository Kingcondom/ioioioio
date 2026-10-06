from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-Respiratory"
OLD = "ข้อสอบเก่าในสไลด์ MedSalmon"

FIG_ASP = '''<svg viewBox="0 0 740 330">
 <text x="370" y="22" text-anchor="middle" class="tb">Aspergillus: ภูมิคุ้มกันของ host กำหนดรูปแบบโรค</text>
 <path d="M30 300H710" class="ln"/>
 <text x="30" y="320" class="t3">ภูมิไวเกิน (asthma, CF)</text>
 <text x="370" y="320" text-anchor="middle" class="t3">ปอดมีโพรงเดิม (TB, COPD)</text>
 <text x="710" y="320" text-anchor="end" class="t3">ภูมิต่ำ (neutropenia)</text>
 <rect x="20" y="40" width="225" height="250" rx="10" class="c2soft"/>
 <text x="132" y="64" text-anchor="middle" class="tb">ABPA</text>
 <text x="132" y="84" text-anchor="middle" class="t3">hypersensitivity</text>
 <text x="32" y="110" class="t2">• asthma กำเริบบ่อย</text>
 <text x="32" y="132" class="t2">• brown mucus plugs</text>
 <text x="32" y="154" class="t2">• eosinophilia, IgE ↑↑</text>
 <text x="32" y="176" class="t2">• HRCT: central</text>
 <text x="44" y="196" class="t2">bronchiectasis</text>
 <rect x="32" y="232" width="201" height="44" rx="8" class="c2"/>
 <text x="132" y="250" text-anchor="middle" class="tw">Prednisone +</text>
 <text x="132" y="268" text-anchor="middle" class="tw">itraconazole/vori</text>
 <rect x="258" y="40" width="225" height="250" rx="10" class="misssoft"/>
 <text x="370" y="64" text-anchor="middle" class="tb">Chronic (CPA)</text>
 <text x="370" y="84" text-anchor="middle" class="t3">aspergilloma</text>
 <text x="270" y="110" class="t2">• ไม่มีอาการ หรือ</text>
 <text x="270" y="132" class="t2">• ไอเรื้อรัง hemoptysis</text>
 <text x="270" y="154" class="t2">• fungus ball ขยับได้</text>
 <text x="282" y="174" class="t2">ใน cavity เก่า</text>
 <text x="270" y="196" class="t2">• Aspergillus IgG</text>
 <rect x="270" y="210" width="201" height="66" rx="8" class="miss"/>
 <text x="370" y="230" text-anchor="middle" class="tw">ไม่มีอาการ → expectant</text>
 <text x="370" y="249" text-anchor="middle" class="tw">มีอาการ → itra/vori</text>
 <text x="370" y="268" text-anchor="middle" class="tw">ball → ผ่าตัด</text>
 <rect x="496" y="40" width="225" height="250" rx="10" class="badsoft"/>
 <text x="608" y="64" text-anchor="middle" class="tb">Invasive</text>
 <text x="608" y="84" text-anchor="middle" class="t3">tissue invasion</text>
 <text x="508" y="110" class="t2">• severe pneumonia</text>
 <text x="508" y="132" class="t2">• hemoptysis, pleuritic</text>
 <text x="508" y="154" class="t2">• galactomannan +</text>
 <text x="508" y="176" class="t2">• HRCT: halo sign</text>
 <text x="508" y="198" class="t2">• septate, acute-angle</text>
 <text x="520" y="218" class="t2">branching hyphae</text>
 <rect x="508" y="232" width="201" height="44" rx="8" class="bad"/>
 <text x="608" y="259" text-anchor="middle" class="tw">Voriconazole</text>
</svg>'''

S1 = sec("resp-06-01", "Pneumocystis jirovecii pneumonia (PCP)",
    "HIV CD4 < 200 · ไข้ต่ำ ไอแห้ง เหนื่อย SpO2 ต่ำ · CXR bilateral ground glass · high-dose TMP/SMX + pred ถ้า PaO2 < 70",
    minutes=6, source=f"{D} หน้า 247–257", nl=["2.3.1(18)", "2.3.1(9)"],
    md='''
### ใครเป็น
- เชื้อ **Pneumocystis jirovecii** (เชื้อรา) ติดต่อทางอากาศ
- **HIV ที่ CD4 < 200 cells/mm³**, ผู้ป่วยภูมิคุ้มกันต่ำอื่น ๆ (ได้ steroid ระยะยาว เช่น SLE — เสริม)

### อาการ
- อาจไม่มีอาการ หรือเป็น **ค่อยเป็นค่อยไป (หลายวันถึงหลายสัปดาห์)**
- **ไข้ต่ำ**, อ่อนเพลีย, **เหนื่อย, ไอแห้ง**, น้ำหนักลด
- Bilateral crepitation และ rhonchi (มักฟังได้น้อย — เสริม)
- **SpO2 < 90%** — โดยเฉพาะ **desaturation ตอนออกแรง** (เสริม)
- เบาะแสของ HIV: **oral thrush**, ต่อมน้ำเหลืองโต, papular eruption, น้ำหนักลด

### Investigation
- **CXR**: **ground glass appearance** (diffuse interstitial infiltrate สมมาตรทั้งสองข้าง)
- CT chest: ground glass, **pneumatocele** (แตกเป็น pneumothorax ได้)
- **Induced sputum / BAL** → **methenamine silver stain** เห็น cyst รูปจาน (disc-shaped)
- LDH สูง, β-D-glucan (เสริม)

### การรักษา
- **High-dose TMP/SMX (co-trimoxazole)** 21 วัน (TMP 15–20 mg/kg/วัน — เสริม)
- **+ Prednisolone** เมื่อ
  - **PaO2 < 70 mmHg** หรือ **SpO2 < 92% (room air)**
  - **A–a gradient > 35 mmHg**
- **Primary prophylaxis** เมื่อ **CD4 < 200** → **low-dose TMP/SMX**

### คำนวณ A–a gradient (เสริม)
PAO2 = FiO2 × (760 − 47) − PaCO2/0.8 → ที่ room air ≈ 150 − PaCO2/0.8
ตัวอย่าง: PaCO2 32, PaO2 60 → PAO2 = 150 − 40 = 110 → A–a = 50 (> 35 → ให้ steroid)

> ข้อสอบเก่ามี ABG "PaCO2 60, PaO2 30" ในผู้ป่วย SLE ที่สงสัย PCP — ตัวเลขนี้ไม่เข้ากับ PCP (ปกติ PaCO2 ต่ำจากหายใจเร็ว) ถ้าเจอให้ยึดภาพรวมทางคลินิก: SLE + steroid + ไข้ต่ำ ไอแห้ง + bilateral → **co-trimoxazole**
''',
    pearls=["PCP: HIV CD4 < 200 · ไข้ต่ำ ไอแห้ง เหนื่อย SpO2 ต่ำ · bilateral ground glass",
            "Dx: induced sputum/BAL methenamine silver (disc-shaped cyst)",
            "Tx: high-dose TMP/SMX + prednisolone ถ้า PaO2 < 70 หรือ SpO2 < 92% หรือ A–a > 35",
            "Prophylaxis เมื่อ CD4 < 200 → low-dose TMP/SMX",
            "Oral thrush + bilateral interstitial infiltrate → คิด HIV + PCP"],
    items=[
        mcq("RESP-06-01-1", """A 28-year-old man has fever, dry cough, exertional dyspnea, poor appetite and weight loss for 10 days. BT 38°C, HR 100/min, RR 30/min, SpO2 85%. Examination: oral thrush, pale conjunctivae, generalized papular eruption and multiple cervical lymphadenopathy. CXR: bilateral diffuse interstitial infiltration. What is the most appropriate management?""",
            "Co-trimoxazole (high-dose TMP/SMX) with prednisolone",
            ["IRZE regimen", "Ceftriaxone", "Azithromycin", "Amphotericin B"],
            explain="""Oral thrush ร่วมกับ papular eruption และต่อมน้ำเหลืองโตหลายตำแหน่ง ชี้ไปที่ HIV ระยะลุกลาม เมื่อมีไข้ต่ำ ไอแห้ง เหนื่อย และ bilateral interstitial infiltrate จึงเข้ากับ PCP เนื่องจาก SpO2 85% (< 92%) ต้องให้ high-dose TMP/SMX ร่วมกับ prednisolone
- IRZE ใช้รักษา TB ซึ่งมักเห็น upper lobe หรือ cavity และเป็นแบบเรื้อรังกว่า
- Ceftriaxone และ azithromycin ใช้กับ CAP แบบ typical และ atypical
- Amphotericin B ใช้กับ cryptococcosis หรือ talaromycosis ซึ่งรอยโรคที่ผิวหนังเป็นแบบ umbilicated papule และมักเห็น nodules มากกว่า ground glass""",
            pearl="HIV + bilateral interstitial + hypoxemia → TMP/SMX (+ steroid)",
            topic="PCP treatment", ref=[f"{D} หน้า 247–249, 252–253"], nl=["2.3.1(18)"], kind="old", src=OLD),
        mcq("RESP-06-01-2", """A 45-year-old man recently diagnosed with HIV has had low-grade fever, dry cough and exertional dyspnea for 1 week. BT 38°C, RR 28/min, HR 100/min, SpO2 92% on room air. Lungs are clear. CXR: bilateral interstitial infiltration. What is the most appropriate treatment?""",
            "Co-trimoxazole",
            ["Imipenem", "Piperacillin/tazobactam", "Ceftriaxone plus azithromycin", "Anti-TB drugs"],
            explain="""HIV ร่วมกับอาการแบบ subacute (ไข้ต่ำ ไอแห้ง เหนื่อยเวลาออกแรง) SpO2 ต่ำ ฟังปอดได้ clear แต่ CXR เป็น bilateral interstitial เป็นภาพคลาสสิกของ PCP รักษาด้วย co-trimoxazole
- Imipenem และ pip/tazo เป็นยาของ HAP
- Ceftriaxone + azithromycin ใช้กับ CAP ซึ่งมักมีเสมหะ ไข้สูง และ consolidation
- Anti-TB ใช้เมื่อพบ AFB หรือภาพ CXR ที่เข้ากับ TB""",
            pearl="PCP: ปอดฟัง clear แต่ CXR bilateral และ SpO2 ต่ำ",
            topic="PCP", ref=[f"{D} หน้า 247–249, 254–255"], nl=["2.3.1(18)"], kind="old", src=OLD),
        mcq("RESP-06-01-3", """A 34-year-old man with HIV (CD4 60 cells/mm³) is diagnosed with PCP. Room-air ABG: pH 7.48, PaCO2 32 mmHg, PaO2 60 mmHg. In addition to high-dose TMP/SMX, which treatment is indicated?""",
            "Prednisolone, because PaO2 is below 70 mmHg and the A–a gradient is about 50 mmHg",
            ["No additional therapy; steroids are contraindicated in HIV",
             "Prednisolone only if PaO2 falls below 50 mmHg",
             "Add IV pentamidine as a second agent",
             "Add fluconazole because CD4 is below 100"],
            explain="""เกณฑ์ให้ steroid ใน PCP คือ PaO2 < 70 หรือ SpO2 < 92% หรือ A–a gradient > 35 ผู้ป่วยมี PaO2 60 และ A–a = (150 − 32/0.8) − 60 = 110 − 60 = 50 จึงเข้าเกณฑ์ steroid ช่วยลดการอักเสบที่เกิดขึ้นเมื่อเชื้อตาย และลดอัตราตาย ABG เป็น respiratory alkalosis ที่สอดคล้องกับการหายใจเร็ว
- Steroid ไม่ได้เป็นข้อห้ามใน HIV แต่ให้เพื่อลดอัตราตายในเคสที่ hypoxemia
- เกณฑ์คือ < 70 ไม่ใช่ < 50
- Pentamidine เป็นยาทางเลือกเมื่อใช้ TMP/SMX ไม่ได้ ไม่ได้ให้ร่วมกัน
- Fluconazole ไม่ใช่ primary prophylaxis ที่แนะนำทั่วไป และไม่ได้รักษา PCP""",
            pearl="PCP + PaO2 < 70 หรือ A–a > 35 → เติม prednisolone",
            topic="PCP steroid", ref=[f"{D} หน้า 249"], nl=["2.3.1(18)", "3.3.17"]),
        mcq("RESP-06-01-4", """A 30-year-old woman newly diagnosed with HIV has CD4 140 cells/mm³ and no respiratory symptoms. CXR is normal. Which medication should be started to prevent opportunistic pneumonia?""",
            "Low-dose TMP/SMX (co-trimoxazole) prophylaxis",
            ["Isoniazid for 9 months regardless of TB testing", "Azithromycin weekly",
             "Fluconazole daily", "No prophylaxis until CD4 falls below 50"],
            explain="""CD4 < 200 เป็นข้อบ่งชี้ primary prophylaxis ของ PCP ด้วย low-dose TMP/SMX ตามสไลด์
- Isoniazid ให้เมื่อมี latent TB ไม่ได้ให้ทุกคนโดยไม่ตรวจ
- Azithromycin เป็น prophylaxis ของ MAC เมื่อ CD4 < 50 (ปัจจุบันไม่จำเป็นถ้าเริ่ม ART — เสริม)
- Fluconazole ไม่ใช่ PCP prophylaxis
- การรอจน CD4 < 50 ทำให้เสี่ยงต่อ PCP""",
            pearl="CD4 < 200 → TMP/SMX prophylaxis",
            topic="PCP prophylaxis", ref=[f"{D} หน้า 249"], nl=["2.3.1(18)", "2.3.1(9)"]),
        mcq("RESP-06-01-5", """A patient has had low-grade fever and dry cough for 10 days and dyspnea for 2 days. CXR shows diffuse bilateral ground-glass opacities. Rapid HIV test is positive. Which investigation best confirms the suspected organism?""",
            "Induced sputum or bronchoalveolar lavage with methenamine silver stain",
            ["Serology for TB", "Sputum Gram stain and culture", "Blood culture for fungi", "Tuberculin skin test"],
            explain="""Ground glass ทั้งสองข้างในผู้ป่วย HIV นึกถึง PCP การยืนยันคือเก็บ induced sputum หรือ BAL แล้วย้อม methenamine silver เพื่อหา cyst รูปจาน (P. jirovecii เพาะเชื้อไม่ได้)
- Serology for TB ไม่มีที่ใช้ในการวินิจฉัย active TB
- Gram stain และ culture หาแบคทีเรีย ไม่เห็น Pneumocystis
- Blood culture for fungi ไม่ขึ้น Pneumocystis
- TST บอกการติดเชื้อ TB ไม่ใช่ PCP
(ข้อสอบเก่าต้นฉบับมีตัวเลือก serology for PCP กับ serology for TB ซึ่งในทางปฏิบัติไม่มี serology สำหรับ PCP จึงเรียบเรียงใหม่เป็นวิธีที่ใช้ยืนยันจริง)""",
            pearl="PCP confirm: induced sputum/BAL + silver stain",
            topic="PCP diagnosis", ref=[f"{D} หน้า 248, 250–251"], nl=["2.3.1(18)"], kind="old", src=OLD),
    ])

S2 = sec("resp-06-02", "Lung abscess",
    "Aspiration → anaerobes · เสมหะเหม็น + cavity with air-fluid level · ATB 4–6 สัปดาห์ (amp-sulbactam, clindamycin, ceftriaxone + metronidazole)",
    minutes=5, source=f"{D} หน้า 197–204", nl=["2.3.10(5)", "B6.2.2(4)"],
    md='''
### สาเหตุและกลไก
- **Aspiration (พบบ่อยที่สุด)** — สำลักเนื้อหาจากปากและคอ → pneumonitis → เนื้อปอดตายเป็นโพรงหนองใน 1–2 สัปดาห์
- รองลงมา: หลอดลมอุดตัน (มะเร็ง สิ่งแปลกปลอม), hematogenous spread (septic emboli)
- เชื้อ: **anaerobes (พบบ่อยที่สุด)**

### ปัจจัยเสี่ยง
- **ระดับความรู้สึกตัวลดลง** (ติดสุรา ชัก ยาเกินขนาด)
- กลืนลำบาก
- **ฟันผุ** / เหงือกอักเสบ
- ภูมิคุ้มกันต่ำ
- Pneumonia / bronchiectasis

### อาการ
- ไข้ ไอ น้ำหนักลด (มักเป็นแบบ subacute 1–2 สัปดาห์)
- **เสมหะเป็นหนองกลิ่นเหม็น (foul-smelling purulent sputum)** / ลมหายใจเหม็น

### Investigation
- **CXR: cavity ที่มี air-fluid level** (ตำแหน่ง aspiration: posterior segment RUL, superior segment RLL — เสริม)
- Sputum G/S, culture

### การรักษา — ATB 4–6 สัปดาห์
| ยา |
|---|
| **Ampicillin/sulbactam** (หรือ amoxicillin/clavulanate PO) |
| **Clindamycin** |
| **Ceftriaxone + metronidazole** |

> Ceftriaxone เดี่ยวครอบคลุม anaerobes ได้ไม่ดี — ข้อสอบเก่าบางข้อให้ ceftriaxone เป็นคำตอบเพราะตัวเลือกอื่นแย่กว่า (ceftazidime, cipro, roxithromycin, azithromycin) แต่ถ้ามี amox/clav หรือ clindamycin ให้เลือกตัวนั้น

> ไม่ต้องเจาะระบายส่วนใหญ่ — ระบายตามธรรมชาติผ่านหลอดลม (postural drainage) (เสริม)
''',
    pearls=["Lung abscess: aspiration + anaerobes · ติดสุรา/ชัก/ฟันผุ",
            "เสมหะเหม็น + cavity with air-fluid level",
            "ATB 4–6 สัปดาห์: amp-sulbactam/amox-clav, clindamycin, ceftriaxone + metronidazole",
            "ไม่ต้องให้ IRZE ถ้าภาพคลาสสิกของ abscess (เสมหะเหม็น ระดับน้ำในโพรง)"],
    items=[
        mcq("RESP-06-02-1", """A middle-aged man has fever, cough, dyspnea and foul-smelling breath for 2 weeks. CXR shows a cavitary lesion with an air-fluid level. What is the most likely diagnosis?""",
            "Lung abscess",
            ["Pulmonary tuberculosis", "Aspergilloma", "Squamous cell carcinoma with cavitation", "Bullous emphysema"],
            explain="""ไข้ ไอ ลมหายใจและเสมหะเหม็น (anaerobes) ร่วมกับโพรงที่มี air-fluid level เป็นภาพคลาสสิกของ lung abscess
- TB cavity มักผนังบาง อยู่ที่ upper lobe ไม่ค่อยมี air-fluid level และไม่มีกลิ่นเหม็น
- Aspergilloma เห็นเป็นก้อน fungus ball ขยับได้ใน cavity และมี air crescent
- มะเร็งที่เป็นโพรงจะมีผนังหนา ขอบไม่เรียบ และไม่มีไข้หรือกลิ่นเหม็นแบบนี้
- Bulla เป็นโพรงอากาศผนังบาง ไม่มีน้ำ และไม่มีไข้""",
            pearl="เสมหะเหม็น + air-fluid level = lung abscess",
            topic="Lung abscess dx", ref=[f"{D} หน้า 198–200"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-06-02-2", """A man who drinks alcohol heavily has had fever and foul-smelling sputum for 2 weeks. Crackles are heard over the right upper lung. CXR shows a thick-walled cavity with an air-fluid level in the posterior segment of the right upper lobe. What is the most appropriate antibiotic treatment?""",
            "Amoxicillin–clavulanate",
            ["Azithromycin", "Co-trimoxazole", "IRZE", "Ciprofloxacin"],
            explain="""ผู้ติดสุราเสี่ยงต่อ aspiration เกิด lung abscess จาก anaerobes ยาที่ครอบคลุมคือ β-lactam/β-lactamase inhibitor (amox/clav PO หรือ amp-sulbactam IV) ให้นาน 4–6 สัปดาห์
- Azithromycin ไม่ครอบคลุม anaerobes
- Co-trimoxazole ใช้กับ PCP หรือ Nocardia
- IRZE ใช้เมื่อพิสูจน์ได้ว่าเป็น TB ซึ่งภาพนี้ไม่เข้า (เสมหะเหม็น มี air-fluid level)
- Ciprofloxacin ครอบคลุม anaerobes ได้ไม่ดี""",
            pearl="Lung abscess → amox/clav หรือ amp-sulbactam",
            topic="Lung abscess tx", ref=[f"{D} หน้า 198, 201–202"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-06-02-3", """A 52-year-old homeless man with alcohol-use disorder has cough, foul-smelling sputum and fever (BT 39°C). CXR shows a thick-walled cavitary lesion. Among the following, which is the most appropriate antibiotic?""",
            "Ceftriaxone",
            ["Ceftazidime", "Ciprofloxacin", "Roxithromycin", "Azithromycin"],
            explain="""Lung abscess จาก aspiration ในคนติดสุรา ยามาตรฐานคือ ceftriaxone + metronidazole, clindamycin หรือ amp-sulbactam ในตัวเลือกนี้ ceftriaxone ดีที่สุด เพราะครอบคลุม streptococci ในช่องปาก และ Klebsiella ในคนติดสุรา และควรให้ร่วมกับ metronidazole ตามสไลด์
- Ceftazidime ครอบคลุม gram-positive และ anaerobes ได้ไม่ดี
- Ciprofloxacin ครอบคลุม anaerobes และ streptococci ได้ไม่ดี
- Roxithromycin และ azithromycin ครอบคลุม anaerobes ได้ไม่พอ
(ข้อสอบเก่า — ถ้ามี clindamycin หรือ amp-sulbactam ให้เลือกตัวนั้น)""",
            pearl="Abscess: ceftriaxone ต้องคู่ metronidazole",
            topic="Lung abscess regimen", ref=[f"{D} หน้า 198, 203–204"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-06-02-4", """A 45-year-old man is diagnosed with a lung abscess after an episode of alcohol intoxication with vomiting. He improves on IV ampicillin–sulbactam. What is the expected total duration of antibiotic therapy?""",
            "4–6 weeks",
            ["5–7 days", "10–14 days", "6 months", "Until the cavity completely disappears on CXR regardless of symptoms, for at least 1 year"],
            explain="""Lung abscess ต้องให้ ATB นาน 4–6 สัปดาห์ตามสไลด์ (เริ่ม IV แล้วเปลี่ยนเป็น PO เมื่อดีขึ้น) เพราะยาซึมเข้าโพรงหนองได้ช้า
- 5–7 วันเป็นระยะเวลาของ CAP
- 10–14 วันสั้นเกินไปสำหรับ abscess
- 6 เดือนเป็นระยะเวลาของการรักษา TB
- ไม่จำเป็นต้องรอจนโพรงหายหมด ซึ่งอาจใช้เวลานานกว่าที่อาการทางคลินิกจะดีขึ้นมาก""",
            pearl="Lung abscess ATB 4–6 สัปดาห์",
            topic="Abscess duration", ref=[f"{D} หน้า 198"], nl=["2.3.10(5)"]),
    ])

S3 = sec("resp-06-03", "Aspergillosis",
    "ABPA (asthma, IgE ↑) → pred + itraconazole · CPA/aspergilloma ใน cavity เก่า · invasive (neutropenia, halo sign) → voriconazole",
    minutes=6, source=f"{D} หน้า 241–246", nl=["2.3.1-3(7)"],
    md='''
### เชื้อ
- **Aspergillus fumigatus** (พบบ่อยที่สุด) — เชื้อราสาย ติดต่อทางอากาศ
- รูปแบบโรคขึ้นกับภูมิคุ้มกันของผู้ป่วย

[[fig:resp-06-03-asp]]

### 1. Allergic bronchopulmonary aspergillosis (ABPA)
- ปฏิกิริยา **ภูมิไวเกิน** ต่อ Aspergillus ในทางเดินหายใจ
- Risk: **asthma, cystic fibrosis**
- asthma กำเริบบ่อย (wheeze), ไอมี **brown mucus plugs**
- Lab: **eosinophilia, total IgE สูง**
- HRCT: **bronchiectasis** (central)
- Tx: **prednisone + antifungal (itraconazole, voriconazole)**

### 2. Chronic pulmonary aspergillosis (CPA)
- ติดเชื้อเรื้อรัง ใน **ปอดที่มีโรคเดิม (TB, COPD)** — มักอยู่ใน **cavity เก่าของ TB**
- ไม่มีอาการ หรือไอเรื้อรัง **hemoptysis**, ไข้ อ่อนเพลีย น้ำหนักลด
- **Aspergillus IgG serology**
- CXR/CT: **aspergilloma = fungus ball ที่ขยับได้** (air crescent sign — เสริม)
- Tx: ไม่มีอาการ → **expectant** · มีอาการ → **itraconazole, voriconazole** · aspergilloma (ไอเป็นเลือดมาก) → **surgical resection**

### 3. Invasive aspergillosis
- ติดเชื้อรุนแรง **ลุกลามเข้าเนื้อปอด** ใน **ภูมิคุ้มกันต่ำ โดยเฉพาะ neutropenia** (หลังเคมีบำบัด, BMT, steroid ขนาดสูง)
- **Severe pneumonia**: ไข้ ไอ เหนื่อย **hemoptysis**, เจ็บหน้าอกแบบ pleuritic (ลุกลามเข้าหลอดเลือด → infarct) · อวัยวะอื่น (สมอง ไซนัส)
- Lab: **galactomannan**
- HRCT: **nodules หลายจุด + halo sign** (ground glass รอบ nodule = เลือดออก)
- BAL: **septate hyphae แตกแขนงเป็นมุมแหลม (acute angle, dichotomous branching)**
- Tx: **voriconazole**

| | Aspergillus | Mucor (เสริม) |
|---|---|---|
| Hyphae | septate | non-septate (ไม่มีผนังกั้น) กว้าง |
| แขนง | มุมแหลม 45° | มุมฉาก 90° |
| ยา | voriconazole | amphotericin B + ผ่าตัด |
''',
    figs=[fig("resp-06-03-asp", "สามรูปแบบของ aspergillosis", FIG_ASP,
              "ซ้ายไปขวาเรียงจากภาวะภูมิไวเกิน (ABPA) ไปจนถึงภูมิต่ำ (invasive) โดยมี aspergilloma ในโพรงเดิมอยู่ตรงกลาง")],
    pearls=["ABPA: asthma/CF + eos + IgE ↑ + central bronchiectasis → pred + itraconazole",
            "Aspergilloma: fungus ball ขยับได้ใน cavity TB เก่า + hemoptysis",
            "Invasive: neutropenia + halo sign + galactomannan → voriconazole",
            "Aspergillus: septate hyphae แตกแขนงมุมแหลม"],
    items=[
        mcq("RESP-06-03-1", """A 25-year-old woman with SLE on low-dose prednisolone has had fever and hemoptysis for 3 weeks without improvement after 5 days of roxithromycin. CBC is normal. CXR shows a rounded intracavitary mass with a crescent of air around it in an old upper-lobe cavity. What is the most likely diagnosis?""",
            "Aspergillosis (aspergilloma)",
            ["Lupus pneumonitis", "Pulmonary tuberculosis", "Cryptococcosis", "Lung abscess"],
            explain="""ผู้ป่วยภูมิคุ้มกันต่ำจาก steroid มีไอเป็นเลือดเรื้อรัง และเห็นก้อนใน cavity ที่มี air crescent เข้ากับ aspergilloma ซึ่งเป็นรูปแบบหนึ่งของ aspergillosis
- Lupus pneumonitis เป็นแบบเฉียบพลัน มี infiltrate ทั้งสองข้าง ไม่ใช่ก้อนในโพรง
- TB cavity ไม่มีก้อนกลมในโพรง (แต่ cavity เก่าของ TB เป็นที่อยู่ของ aspergilloma)
- Cryptococcosis มักเห็นเป็น nodule และมีอาการทางสมอง
- Lung abscess มี air-fluid level และเสมหะเหม็น ไม่ใช่ก้อนที่มีอากาศล้อมรอบ""",
            pearl="Ball in cavity + air crescent + hemoptysis = aspergilloma",
            topic="Aspergilloma", ref=[f"{D} หน้า 243, 245–246"], nl=["2.3.1-3(7)"], kind="old", src=OLD),
        mcq("RESP-06-03-2", """A 52-year-old man with acute myeloid leukemia has been neutropenic for 14 days after chemotherapy. Despite broad-spectrum antibiotics, he has persistent fever, pleuritic chest pain and hemoptysis. CT chest shows multiple nodules surrounded by ground-glass halos. Serum galactomannan is positive. What is the treatment of choice?""",
            "Voriconazole",
            ["Fluconazole", "Itraconazole plus prednisone", "Co-trimoxazole", "Surgical resection alone"],
            explain="""Neutropenia นาน ไข้ไม่ลงแม้ได้ ATB ร่วมกับ nodules ที่มี halo sign และ galactomannan บวก คือ invasive aspergillosis ยาหลักคือ voriconazole
- Fluconazole ไม่มีฤทธิ์ต่อ Aspergillus
- Itraconazole ร่วมกับ prednisone เป็นการรักษา ABPA และ steroid จะทำให้ invasive disease แย่ลง
- Co-trimoxazole ใช้กับ PCP
- การผ่าตัดใช้กับ aspergilloma ไม่ใช่การรักษาหลักของ invasive disease""",
            pearl="Neutropenia + halo sign → invasive aspergillosis → voriconazole",
            topic="Invasive aspergillosis", ref=[f"{D} หน้า 244"], nl=["2.3.1-3(7)"]),
        mcq("RESP-06-03-3", """A 30-year-old woman with long-standing asthma has had frequent exacerbations and expectorates brown mucus plugs. Eosinophils are 1,200/µL and total IgE is markedly elevated. HRCT shows central bronchiectasis. What is the most appropriate treatment?""",
            "Oral prednisone plus itraconazole",
            ["Voriconazole alone for invasive disease", "Surgical resection",
             "Long-term azithromycin only", "Increase SABA use only"],
            explain="""Asthma ร่วมกับ brown mucus plugs, eosinophilia, IgE สูง และ central bronchiectasis คือ ABPA รักษาด้วย steroid เพื่อลดปฏิกิริยาภูมิไวเกิน ร่วมกับ antifungal (itraconazole) เพื่อลดปริมาณเชื้อ
- Voriconazole เดี่ยวเป็นการรักษา invasive aspergillosis ซึ่งไม่ใช่รูปแบบนี้
- การผ่าตัดใช้กับ aspergilloma
- Azithromycin ระยะยาวใช้ใน bronchiectasis ทั่วไป ไม่ได้รักษาปฏิกิริยาต่อ Aspergillus
- SABA ไม่ได้รักษาการอักเสบ""",
            pearl="ABPA → prednisone + itraconazole",
            topic="ABPA", ref=[f"{D} หน้า 242"], nl=["2.3.1-3(7)"]),
        mcq("RESP-06-03-4", """A 60-year-old man treated for pulmonary TB 10 years ago has an asymptomatic mobile fungus ball in an old right upper lobe cavity, found incidentally. Aspergillus IgG is positive. He has never had hemoptysis. What is the most appropriate management per the lecture?""",
            "Expectant management with follow-up",
            ["Immediate lobectomy", "IV amphotericin B", "Restart anti-TB treatment", "Oral prednisone"],
            explain="""CPA หรือ aspergilloma ที่ไม่มีอาการ ตามสไลด์ให้ expectant หรือเฝ้าติดตาม ถ้ามีอาการให้ itraconazole หรือ voriconazole ถ้าไอเป็นเลือดมากพิจารณาผ่าตัด
- Lobectomy มีความเสี่ยง ใช้เมื่อไอเป็นเลือดมากหรือเป็นซ้ำ
- Amphotericin B ใช้กับ invasive fungal infection รุนแรง
- Anti-TB ไม่จำเป็น เพราะไม่มีหลักฐานว่า TB กลับเป็นซ้ำ
- Steroid ทำให้เชื้อราลุกลาม""",
            pearl="Aspergilloma ไม่มีอาการ → expectant",
            topic="CPA management", ref=[f"{D} หน้า 243"], nl=["2.3.1-3(7)"]),
    ])

LECTURE = lecture("06", "Opportunistic & suppurative lung infection",
    subtitle="PCP · lung abscess · aspergillosis",
    objectives=["วินิจฉัยและรักษา PCP พร้อมเกณฑ์ให้ steroid และ prophylaxis ได้",
                "วินิจฉัย lung abscess และเลือกยาครอบคลุม anaerobes นาน 4–6 สัปดาห์ได้",
                "แยก ABPA, aspergilloma และ invasive aspergillosis และเลือกการรักษาได้"],
    sections=[S1, S2, S3])
