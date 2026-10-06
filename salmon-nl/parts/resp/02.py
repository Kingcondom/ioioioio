from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-Respiratory"
OLD = "ข้อสอบเก่าในสไลด์ MedSalmon"

FIG_ILD = '''<svg viewBox="0 0 720 300">
 <defs><marker id="resp-02-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="12" width="260" height="56" rx="10" class="acsoft"/>
 <text x="360" y="35" text-anchor="middle" class="tb">ILD: เหนื่อยค่อย ๆ มากขึ้น</text>
 <text x="360" y="55" text-anchor="middle" class="t3">ไอแห้ง · fine crepitation · restrictive PFT</text>
 <path d="M360 68V92" class="ln" marker-end="url(#resp-02-01-a)"/>
 <rect x="230" y="94" width="260" height="34" rx="10" class="box"/>
 <text x="360" y="116" text-anchor="middle" class="tb">หาสาเหตุ (secondary) ก่อนเสมอ</text>
 <path d="M300 128L95 170" class="ln" marker-end="url(#resp-02-01-a)"/>
 <path d="M330 128L270 170" class="ln" marker-end="url(#resp-02-01-a)"/>
 <path d="M390 128L450 170" class="ln" marker-end="url(#resp-02-01-a)"/>
 <path d="M420 128L625 170" class="ln" marker-end="url(#resp-02-01-a)"/>
 <rect x="10" y="172" width="170" height="116" rx="10" class="c1soft"/>
 <text x="95" y="194" text-anchor="middle" class="tb">CTD (พบบ่อยสุด)</text>
 <text x="22" y="218" class="t3">SSc · RA · SLE</text>
 <text x="22" y="238" class="t3">Polymyositis/DM</text>
 <text x="22" y="262" class="t3">ส่ง ANA, RF,</text>
 <text x="22" y="278" class="t3">anti-CCP</text>
 <rect x="190" y="172" width="160" height="116" rx="10" class="c2soft"/>
 <text x="270" y="194" text-anchor="middle" class="tb">Drug-induced</text>
 <text x="202" y="218" class="t3">amiodarone,</text>
 <text x="202" y="238" class="t3">MTX, bleomycin,</text>
 <text x="202" y="258" class="t3">nitrofurantoin</text>
 <text x="202" y="278" class="t3">(เสริม)</text>
 <rect x="360" y="172" width="180" height="116" rx="10" class="misssoft"/>
 <text x="450" y="194" text-anchor="middle" class="tb">Occupational</text>
 <text x="372" y="218" class="t3">silicosis · asbestosis</text>
 <text x="372" y="238" class="t3">coal worker</text>
 <text x="372" y="258" class="t3">ซักประวัติอาชีพ</text>
 <rect x="550" y="172" width="160" height="116" rx="10" class="sunk"/>
 <text x="630" y="194" text-anchor="middle" class="tb">Idiopathic /</text>
 <text x="630" y="212" text-anchor="middle" class="tb">granulomatous</text>
 <text x="562" y="238" class="t3">IIP (IPF)</text>
 <text x="562" y="258" class="t3">sarcoidosis (เสริม)</text>
</svg>'''

FIG_OCC = '''<svg viewBox="0 0 720 360">
 <text x="360" y="22" text-anchor="middle" class="tb">ตำแหน่งรอยโรคบน CXR: บน vs ล่าง</text>
 <path d="M200 60C150 70 120 140 118 230C117 290 150 320 210 322C260 322 300 300 320 270L320 70C300 58 240 52 200 60Z" class="box"/>
 <path d="M520 60C570 70 600 140 602 230C603 290 570 320 510 322C460 322 420 300 400 270L400 70C420 58 480 52 520 60Z" class="box"/>
 <path d="M360 40V330" class="lnf"/>
 <rect x="125" y="80" width="470" height="90" rx="10" class="misssoft"/>
 <text x="360" y="104" text-anchor="middle" class="tb">Upper lobe เด่น</text>
 <text x="360" y="126" text-anchor="middle" class="t2">Silicosis: nodules + eggshell calcification ของ hilar LN · ↑TB</text>
 <text x="360" y="148" text-anchor="middle" class="t2">Coal worker: fine nodules, chronic bronchitis</text>
 <rect x="125" y="210" width="470" height="96" rx="10" class="c1soft"/>
 <text x="360" y="234" text-anchor="middle" class="tb">Lower lobe เด่น</text>
 <text x="360" y="256" text-anchor="middle" class="t2">Asbestosis: reticular + pleural plaques · mesothelioma, CA lung</text>
 <text x="360" y="278" text-anchor="middle" class="t2">Byssinosis: haziness ล่าง, อาการ Monday morning</text>
 <text x="360" y="298" text-anchor="middle" class="t3">(IPF, SSc-ILD ก็เด่นฐานปอด — เสริม)</text>
 <text x="40" y="130" class="t3">บน</text>
 <text x="40" y="262" class="t3">ล่าง</text>
</svg>'''

S1 = sec("resp-02-01", "Interstitial lung disease (ILD)",
    "Progressive dyspnea + dry cough + fine crepitation · HRCT honeycomb/GGO · PFT restrictive · หาสาเหตุ CTD ก่อน",
    minutes=5, source=f"{D} หน้า 205–208", nl=["2.3.10-3(4)", "3.3.18"],
    md='''
### นิยาม
ILD คือกลุ่มโรคที่มีการอักเสบและเกิดพังผืดในเนื้อปอด (interstitium) → ปอดแข็ง ขยายตัวได้น้อย → **restrictive** + gas exchange แย่ (DLCO ↓ — เสริม)

### สาเหตุ
- **Secondary**
  - **Connective tissue diseases (พบบ่อยที่สุด)**: systemic sclerosis, polymyositis, dermatomyositis, RA, SLE
  - Drug-induced ILD
  - Occupational lung disease
- **Idiopathic interstitial pneumonia** (เช่น IPF — เสริม)
- **Granulomatous ILD** (เช่น sarcoidosis — เสริม)
- อื่น ๆ

[[fig:resp-02-01-ild]]

### อาการ
- **เหนื่อยค่อย ๆ มากขึ้น (progressive dyspnea)**, ไอแห้ง
- **Fine crepitation** (velcro crackles ที่ฐานปอด — เสริม), clubbing (เสริม)
- อาการของ CTD ถ้าเป็นสาเหตุ (Raynaud, ผื่น, ข้ออักเสบ)

### Investigation
| การตรวจ | สิ่งที่พบ |
|---|---|
| CXR | reticular/nodular opacities ↑ |
| **HRCT** | honeycombing, reticular pattern, ground-glass opacity, traction bronchiectasis |
| PFT | **restrictive pattern** |
| Autoantibodies | ANA, rheumatoid factor, anti-CCP — เพื่อ screen CTD |

### การรักษา
- **Supportive**: เลิกบุหรี่, วัคซีน influenza/pneumococcal, pulmonary rehabilitation, oxygen therapy
- **รักษาสาเหตุ**: หยุดยาที่เป็นสาเหตุ, หลีกเลี่ยงการสัมผัส, รักษา CTD (immunosuppressant)
- (IPF: antifibrotic เช่น nintedanib, pirfenidone — เสริม)

### ภาวะแทรกซ้อน
- **Pulmonary hypertension** → **cor pulmonale** (right heart failure: JVP สูง ขาบวม loud P2)
''',
    figs=[fig("resp-02-01-ild", "ILD: แหล่งสาเหตุที่ต้องไล่", FIG_ILD,
              "เมื่อเจอ ILD ให้ไล่หาสาเหตุ secondary ก่อน โดยเฉพาะ CTD ที่พบบ่อยที่สุด แล้วจึงสรุปว่าเป็น idiopathic")],
    pearls=["ILD = progressive dyspnea + dry cough + fine crepitation + restrictive PFT",
            "สาเหตุที่พบบ่อยที่สุดคือ CTD (SSc, RA, SLE, PM/DM) → ส่ง ANA, RF, anti-CCP",
            "HRCT: honeycombing, reticular, GGO, traction bronchiectasis",
            "ภาวะแทรกซ้อน: pulmonary HT → cor pulmonale"],
    items=[
        mcq("RESP-02-01-1", """A 55-year-old woman has 1 year of progressive exertional dyspnea and dry cough. Examination: bibasilar fine end-inspiratory crackles and clubbing. Spirometry: FEV1/FVC 0.86, FVC 58% predicted. HRCT shows peripheral reticulation with honeycombing. Which test should be sent next to look for the most common secondary cause?""",
            "ANA, rheumatoid factor and anti-CCP antibodies",
            ["Sputum AFB × 3", "Serum ACE level only", "Sweat chloride test", "Alpha-1 antitrypsin level"],
            explain="""ภาพทางคลินิก PFT และ HRCT เข้ากับ ILD สาเหตุ secondary ที่พบบ่อยที่สุดคือ connective tissue disease สไลด์จึงให้ส่ง autoantibodies (ANA, RF, anti-CCP) เพื่อ screen
- Sputum AFB ใช้เมื่อสงสัย TB ซึ่งมักมีไข้ น้ำหนักลด และ upper lobe cavity
- Serum ACE ช่วยได้น้อยในการวินิจฉัย sarcoidosis และไม่ใช่สาเหตุที่พบบ่อยที่สุด
- Sweat chloride ใช้วินิจฉัย cystic fibrosis ซึ่งทำให้เกิด bronchiectasis ในคนอายุน้อย
- Alpha-1 antitrypsin เกี่ยวกับ emphysema (obstructive) ไม่ใช่ ILD""",
            pearl="ILD → screen CTD ด้วย ANA, RF, anti-CCP",
            topic="ILD workup", ref=[f"{D} หน้า 205–206"], nl=["2.3.10-3(4)"]),
        mcq("RESP-02-01-2", """A 62-year-old man with long-standing ILD develops worsening dyspnea, raised JVP, a loud P2, hepatomegaly and bilateral leg edema. Echocardiography shows a dilated right ventricle with normal LV function. What is the most likely complication?""",
            "Pulmonary hypertension with cor pulmonale",
            ["Left ventricular systolic heart failure", "Constrictive pericarditis",
             "Acute pulmonary embolism with RV infarction", "Nephrotic syndrome"],
            explain="""ภาวะ hypoxemia เรื้อรังและพังผืดใน ILD ทำให้เกิด pulmonary hypertension จน RV ทำงานล้มเหลว (cor pulmonale) จึงพบ loud P2, JVP สูง ตับโต ขาบวม และ RV โต โดย LV ปกติ
- LV systolic failure ผิด เพราะ echo พบ LV function ปกติ
- Constrictive pericarditis ไม่ทำให้ RV โตหรือ loud P2 และมักมี pericardial knock
- Acute PE เกิดฉับพลัน แต่รายนี้เป็นแบบค่อย ๆ แย่ลงในโรคเรื้อรัง
- Nephrotic syndrome ทำให้บวมได้ แต่ไม่ทำให้ JVP สูงหรือ RV โต""",
            pearl="ILD/COPD เรื้อรัง + RV failure = cor pulmonale",
            topic="ILD complication", ref=[f"{D} หน้า 208"], nl=["2.3.10-3(4)"]),
        mcq("RESP-02-01-3", """A 60-year-old man with ILD due to a connective tissue disease asks what supportive measures are recommended. Which is NOT part of the supportive management listed in the lecture?""",
            "Long-term high-dose inhaled corticosteroid and LABA",
            ["Smoking cessation", "Influenza and pneumococcal vaccination",
             "Pulmonary rehabilitation", "Oxygen therapy when hypoxemic"],
            explain="""การรักษาแบบ supportive ของ ILD ตามสไลด์ประกอบด้วย การเลิกบุหรี่ วัคซีน pulmonary rehab และ O2 แล้วจึงรักษาสาเหตุ ส่วน ICS/LABA เป็นยาของโรค obstructive (asthma, COPD) ไม่ช่วยพังผืดในเนื้อปอด
- การเลิกบุหรี่ช่วยลดการทำลายปอดเพิ่ม
- วัคซีนลดการติดเชื้อซึ่งทำให้ ILD กำเริบ
- Pulmonary rehab เพิ่มความทนทานในการออกกำลังกาย
- O2 ใช้เมื่อมี hypoxemia เพื่อลดภาระหัวใจห้องขวา""",
            pearl="ILD supportive = เลิกบุหรี่ วัคซีน rehab O2 + รักษาสาเหตุ",
            topic="ILD management", ref=[f"{D} หน้า 207"], nl=["2.3.10-3(4)"]),
    ])

S2 = sec("resp-02-02", "Systemic sclerosis (Scleroderma)",
    "Limited (CREST) vs diffuse (renal crisis, ILD) · Raynaud→CCB · renal crisis→ACEI · ILD→MMF/CYC",
    minutes=6, source=f"{D} หน้า 209–215, 225–226", nl=["2.3.12-3(13)", "2.3.10-3(4)"],
    md='''
### นิยามและการแบ่งชนิด
Systemic sclerosis (SSc) = autoimmune ที่ทำให้เกิด **พังผืด (fibrosis)** ในผิวหนังและอวัยวะภายใน ร่วมกับ **vasculopathy**
| | Limited cutaneous SSc | Diffuse SSc |
|---|---|---|
| ผิวหนัง | ปลายมือ ปลายเท้า ใบหน้า (เสริม) | ลามถึงต้นแขน ลำตัว (เสริม) |
| อวัยวะภายใน | น้อย | มาก: **scleroderma renal crisis**, cardiac, **ILD** |
| ลักษณะเด่น | **CREST** (ก็พบใน diffuse ได้) | ไตและปอด |
| Antibody (เสริม) | anti-centromere | anti-Scl-70 (topoisomerase I) |

### CREST syndrome
- **C**alcinosis cutis
- **R**aynaud phenomenon
- **E**sophageal dysmotility
- **S**clerodactyly
- **T**elangiectasia

### อาการตามระบบ
- **ผิวหนัง**: ผิวหนาแข็ง, sclerodactyly + ขยับนิ้วได้น้อย, Raynaud (ปวดนิ้วเวลาอากาศเย็น), **salt & pepper appearance** (สีผิวด่างสลับ)
- **ไต**: **scleroderma renal crisis** = AKI + ความดันสูงเฉียบพลัน + MAHA
- **หัวใจ**: myocarditis, pericarditis
- **ปอด**: **ILD**, pulmonary hypertension (สาเหตุตายสำคัญ — เสริม)
- **GI**: esophageal dysmotility → กลืนลำบากและ reflux

### Investigation
- วินิจฉัยทางคลินิก + **ANA positive**, SSc-specific autoantibodies
- ตรวจอวัยวะ: ไต (BUN, Cr, electrolytes, urine protein), หัวใจ (ECG, echo), ปอด (PFT: restrictive, HRCT: reticular, GGO, fibrosis, honeycombing, bronchiolectasis)

### การรักษาตามอวัยวะ
| ปัญหา | ยา |
|---|---|
| Raynaud phenomenon | **CCB** (nifedipine) |
| Scleroderma renal crisis | **ACEI** (captopril) — แม้ Cr สูงก็ให้ |
| ILD | immunosuppressant: **mycophenolate / cyclophosphamide** |
| GERD | **PPI** |

> ข้อสอบเก่า: ตรวจได้ chest expansion ลดลง ผิว salt & pepper ปวดนิ้วเวลาอากาศเย็น และ CXR เป็น honeycomb → **systemic sclerosis**

> กับดัก: steroid ขนาดสูง (เช่น prednisolone > 15 mg/วัน) กระตุ้น renal crisis ได้ (เสริม)
''',
    pearls=["CREST = calcinosis, Raynaud, esophageal dysmotility, sclerodactyly, telangiectasia",
            "Diffuse SSc: renal crisis + ILD · limited: CREST",
            "Scleroderma renal crisis (AKI + HT + MAHA) → ACEI",
            "Raynaud → CCB · ILD → MMF/cyclophosphamide · GERD → PPI",
            "Salt & pepper skin + Raynaud + honeycomb CXR = SSc"],
    items=[
        mcq("RESP-02-02-1", """A 45-year-old woman has decreased chest expansion, salt-and-pepper skin pigmentation and painful fingers that turn white in cold weather. CXR shows a honeycomb appearance at both bases. What is the most likely diagnosis?""",
            "Systemic sclerosis with interstitial lung disease",
            ["Cystic fibrosis", "Pulmonary tuberculosis", "Idiopathic pulmonary fibrosis",
             "Rheumatoid arthritis with rheumatoid nodules"],
            explain="""ผิวหนังเป็น salt & pepper ร่วมกับ Raynaud phenomenon และ ILD (honeycomb ที่ฐานปอด) เป็นภาพคลาสสิกของ systemic sclerosis
- Cystic fibrosis เป็นตั้งแต่เด็ก ทำให้เกิด bronchiectasis ที่ upper lobe และไม่มีอาการทางผิวหนังแบบนี้
- TB มักเป็นที่ upper lobe เป็น cavity และมีอาการ constitutional
- IPF ไม่มี Raynaud หรือการเปลี่ยนแปลงของผิวหนัง
- RA เด่นที่ข้อเล็กอักเสบแบบสมมาตร ไม่ใช่ผิวหนังแข็งหรือ salt & pepper""",
            pearl="Salt & pepper + Raynaud + ILD = systemic sclerosis",
            topic="SSc diagnosis", ref=[f"{D} หน้า 225–226"], nl=["2.3.12-3(13)"], kind="old", src=OLD),
        mcq("RESP-02-02-2", """A 48-year-old woman with diffuse cutaneous systemic sclerosis presents with headache and blurred vision. BP 210/120 mmHg. Cr 2.8 mg/dL (baseline 0.8). Hb 8.5 g/dL with schistocytes on smear, platelets 85,000/µL. What is the drug of choice?""",
            "Captopril (ACE inhibitor)",
            ["IV methylprednisolone pulse", "Nifedipine as monotherapy",
             "Plasma exchange as first-line", "Hold all antihypertensives until dialysis"],
            explain="""Diffuse SSc ที่มี AKI ความดันสูงเฉียบพลัน และ MAHA (schistocytes, เกล็ดเลือดต่ำ) คือ scleroderma renal crisis ซึ่งยาหลักคือ ACEI ให้ต่อแม้ Cr จะสูง เพราะช่วยให้ไตฟื้นตัวและเพิ่มอัตรารอด
- Steroid ขนาดสูงเป็นปัจจัยกระตุ้นให้เกิด renal crisis จึงห้ามใช้
- CCB ช่วยลดความดันได้บ้างแต่ไม่แทน ACEI
- Plasma exchange ใช้ใน TTP ซึ่งไม่ใช่กลไกหลักของภาวะนี้
- การหยุดยาลดความดันทำให้ไตเสียหายมากขึ้น""",
            pearl="Scleroderma renal crisis → ACEI แม้ Cr สูง",
            topic="Renal crisis", ref=[f"{D} หน้า 211, 215"], nl=["2.3.12-3(13)"]),
        mcq("RESP-02-02-3", """A 40-year-old woman with limited cutaneous systemic sclerosis has painful color changes of her fingers on cold exposure, with no digital ulcers. Which medication is first-line for this symptom?""",
            "Nifedipine (dihydropyridine calcium channel blocker)",
            ["Propranolol", "Captopril", "Mycophenolate mofetil", "Omeprazole"],
            explain="""Raynaud phenomenon ใน SSc รักษาด้วย CCB (nifedipine) เพื่อขยายหลอดเลือดส่วนปลาย ร่วมกับการรักษาความอบอุ่น
- Propranolol (β-blocker) ทำให้หลอดเลือดส่วนปลายหดตัว อาการแย่ลง
- Captopril เป็นยาของ renal crisis
- Mycophenolate ใช้กับ ILD
- Omeprazole ใช้กับ GERD จาก esophageal dysmotility""",
            pearl="Raynaud → CCB · เลี่ยง β-blocker",
            topic="Raynaud", ref=[f"{D} หน้า 215"], nl=["2.3.12-3(13)"]),
        mcq("RESP-02-02-4", """A 50-year-old woman with diffuse systemic sclerosis has progressive dyspnea. PFT shows FVC 62% predicted with reduced DLCO; HRCT shows ground-glass opacities and reticulation at both bases. Which treatment is most appropriate for this organ involvement?""",
            "Mycophenolate mofetil",
            ["High-dose prednisolone alone", "Inhaled salbutamol", "Captopril", "Nifedipine"],
            explain="""SSc-ILD ที่กำลังลุกลาม (FVC ลด, GGO) รักษาด้วย immunosuppressant ตามสไลด์คือ mycophenolate หรือ cyclophosphamide
- Steroid ขนาดสูงอย่างเดียวได้ผลไม่ดี และเสี่ยงต่อ renal crisis
- Salbutamol ใช้กับ bronchospasm ไม่ใช่พังผืด
- Captopril ใช้กับ renal crisis
- Nifedipine ใช้กับ Raynaud""",
            pearl="SSc-ILD → mycophenolate หรือ cyclophosphamide",
            topic="SSc-ILD", ref=[f"{D} หน้า 214–215"], nl=["2.3.10-3(4)"]),
    ])

S3 = sec("resp-02-03", "Occupational lung diseases",
    "Silicosis (upper, eggshell, ↑TB) · asbestosis (lower, pleural plaques, mesothelioma) · byssinosis (Monday) · หยุดสัมผัส",
    minutes=8, source=f"{D} หน้า 216–224, 227–240", nl=["2.3.10-3(4)", "2.3.19(8)"],
    md='''
### การแบ่งกลุ่ม
- **Inorganic dust (pneumoconiosis)**: coal worker pneumoconiosis, **silicosis**, **asbestosis**
- **Organic dust**: **byssinosis** (ฝุ่นฝ้าย)

### ตารางเปรียบเทียบ
| โรค | สาเหตุ / อาชีพ | CXR / HRCT | PFT | ภาวะแทรกซ้อน |
|---|---|---|---|---|
| Coal worker's lung | ฝุ่นถ่านหิน / คนงานเหมืองถ่านหิน | fine nodules ที่ **upper lungs** | — | chronic bronchitis |
| **Silicosis** | crystalline silica (ฝุ่นหิน ฝุ่นทราย): พ่นทราย โรงงานแก้ว เซรามิก เหมือง โม่หิน แกะสลักหิน ครก อิฐ | **eggshell calcification** ของ hilar LN, nodules เล็กหลายจุดเด่น **upper lobe**, GGO | mixed restrictive + obstructive | **↑ TB risk** |
| **Asbestosis** | asbestos fiber: หลังคา ผ้าเบรก ฉนวนกันความร้อน ต่อเรือ | reticular เด่น **lower lobes**, **pleural plaques** / pleural thickening | restrictive | **bronchogenic CA, mesothelioma** |
| **Byssinosis** | ฝุ่นฝ้ายดิบ / โรงงานทอผ้า | diffuse haziness ล่าง (ไม่มีลักษณะจำเพาะ) | reversible → irreversible obstruction | — |

[[fig:resp-02-03-occ]]

### Byssinosis — "Monday morning sickness"
- เหนื่อย แน่นหน้าอก ไอ wheeze **วันแรกที่กลับมาทำงาน** หลังวันหยุด ดีขึ้นเมื่อหยุดสัมผัส และแย่ลงเมื่อกลับไปสัมผัส
- ระยะแรก airway obstruction **กลับคืนได้** → นานไปเป็น **irreversible**

### ชื่อโรคที่ใช้เป็นตัวลวง
- **Bagassosis** = ชานอ้อย (โรงงานน้ำตาล, เยื่อกระดาษ) — hypersensitivity pneumonitis
- **Berylliosis** = โลหะ beryllium (alloy, high-tech) — granuloma คล้าย sarcoidosis

### Investigation
- เริ่มต้น: **CXR, PFT** · ดีที่สุด: **HRCT**
- ซักประวัติอาชีพละเอียดเสมอ (ชนิดงาน ระยะเวลา อุปกรณ์ป้องกัน)

### การรักษา — ไม่มีการรักษาให้หายขาด
- **หยุดการสัมผัส (cessation of exposure)** — สำคัญที่สุด: ย้ายงาน/เปลี่ยนตำแหน่ง/หยุดงาน
- เลิกบุหรี่ (asbestos + บุหรี่ เพิ่มความเสี่ยงมะเร็งปอดแบบทวีคูณ — เสริม)
- Vaccine influenza, pneumococcal
- Oxygen therapy
- Silicosis: screen TB / latent TB (เสริม)

> ข้อสอบเก่า: เมื่อวินิจฉัยโรคปอดจากอาชีพแล้ว คำแนะนำที่ถูกคือ **ย้ายงานหรือเปลี่ยนตำแหน่ง/หยุดงาน** ไม่ใช่ใส่ mask อย่างเดียว เปลี่ยนน้ำยา หรือติดพัดลม (เป็นมาตรการป้องกันระดับโรงงาน ไม่ช่วยคนที่ป่วยแล้ว)

> ข้อสอบเก่า: ช่างแกะสลักหินหอบเหนื่อย ถามว่า investigation ใดช่วยวินิจฉัยได้ดีที่สุดจากตัวเลือก (CXR, PFT, sputum silicon crystal, bronchoscopy, cytology) → **CXR** (ถ้ามี HRCT ในตัวเลือก HRCT ดีที่สุด)
''',
    figs=[fig("resp-02-03-occ", "ตำแหน่งรอยโรคบน CXR ของ pneumoconiosis", FIG_OCC,
              "Silicosis และ coal worker เด่นที่ปอดบน · asbestosis และ byssinosis เด่นที่ปอดล่าง")],
    pearls=["Silicosis: upper lobe nodules + eggshell calcification + ↑TB",
            "Asbestosis: lower lobe reticular + pleural plaques → mesothelioma, CA lung",
            "Byssinosis (ฝุ่นฝ้าย): Monday morning sickness, reversible → irreversible",
            "รักษาหลัก = หยุดสัมผัส (ย้ายงาน) · ไม่มี curative tx",
            "Initial CXR/PFT · best HRCT"],
    items=[
        mcq("RESP-02-03-1", """A 20-year-old woman working in a textile (cotton) factory has dyspnea, chest tightness and wheeze, worst on the first working day of the week and absent on Sundays and holidays. CXR shows no infiltration; spirometry shows reversible airway obstruction. What is the most likely diagnosis?""",
            "Byssinosis",
            ["Pneumoconiosis", "Hypersensitivity pneumonitis", "Acute bronchiolitis", "Silicosis"],
            explain="""คนงานโรงงานฝ้ายที่มีอาการช่วงต้นสัปดาห์ (Monday morning sickness) หายในวันหยุด และในระยะแรก obstruction ยังกลับคืนได้ เข้ากับ byssinosis ตามเฉลยในสไลด์
- Pneumoconiosis เกิดจากฝุ่นอนินทรีย์ ทำให้เกิดพังผืดถาวร และ CXR ผิดปกติ
- Hypersensitivity pneumonitis มีไข้ crepitation และ infiltrate ไม่ใช่ wheeze อย่างเดียว
- Acute bronchiolitis เป็นโรคติดเชื้อในเด็กเล็ก
- Silicosis เกิดจากฝุ่นหินและทราย และเห็น nodules ที่ปอดบน
หมายเหตุ: ข้อสอบเก่ามี occupational asthma ในตัวเลือกด้วย ซึ่งก็ทำให้อาการดีขึ้นในวันหยุดได้ แต่สไลด์เฉลย byssinosis เพราะระบุว่าเป็นโรงงานฝ้าย""",
            pearl="ฝุ่นฝ้าย + Monday morning sickness = byssinosis",
            topic="Byssinosis", ref=[f"{D} หน้า 222, 227–228"], nl=["2.3.10-3(4)"], kind="old", src=OLD),
        mcq("RESP-02-03-2", """A 55-year-old non-smoking man has worked in an insulation factory for 25 years. He has 1 year of exertional dyspnea. Examination: clubbing and bibasilar crackles. CXR: reticular infiltration in both lower lungs with calcified pleural plaques. What is the diagnosis?""",
            "Asbestosis",
            ["Silicosis", "Malignant mesothelioma", "Hypersensitivity pneumonitis", "Coal worker's pneumoconiosis"],
            explain="""ประวัติทำงานโรงงานฉนวน ร่วมกับรอยโรค reticular ที่ปอดล่างทั้งสองข้าง และ pleural plaques ที่มีหินปูน เข้ากับ asbestosis
- Silicosis เด่นที่ปอดบน และเห็น eggshell calcification ของต่อมน้ำเหลือง ไม่ใช่ pleural plaque
- Mesothelioma เป็นก้อนหรือเยื่อหุ้มปอดหนาเป็นปุ่มข้างเดียว มักมี effusion และเจ็บหน้าอก
- Hypersensitivity pneumonitis เกิดจากฝุ่นอินทรีย์ อาการสัมพันธ์กับการสัมผัส
- Coal worker เด่นที่ปอดบน""",
            pearl="Insulation/brake/roofing + lower reticular + pleural plaques = asbestosis",
            topic="Asbestosis", ref=[f"{D} หน้า 220–221, 229–230"], nl=["2.3.10-3(4)"], kind="old", src=OLD),
        mcq("RESP-02-03-3", """A 68-year-old man who has worked in the ceramic industry for 30 years presents with cough and dyspnea for 1 month. Crackles are heard over both upper lungs. CXR shows multiple small nodules in the upper zones and eggshell calcification of hilar lymph nodes. What is the most likely diagnosis?""",
            "Silicosis",
            ["Bagassosis", "Asbestosis", "Berylliosis", "Byssinosis"],
            explain="""อุตสาหกรรมเซรามิกทำให้สัมผัส crystalline silica รอยโรคเด่นที่ปอดบนร่วมกับ eggshell calcification ของต่อมน้ำเหลืองที่ขั้วปอด เข้ากับ silicosis
- Bagassosis เกิดจากชานอ้อย (โรงงานน้ำตาล เยื่อกระดาษ)
- Asbestosis เด่นที่ปอดล่างและมี pleural plaques
- Berylliosis เกิดจากโลหะ beryllium ในงาน alloy หรือ high-tech
- Byssinosis เกิดจากฝุ่นฝ้าย และไม่มีลักษณะจำเพาะบน CXR""",
            pearl="Ceramic/glass/sandblasting/stone + eggshell calcification = silicosis",
            topic="Silicosis", ref=[f"{D} หน้า 218–219, 231–232"], nl=["2.3.10-3(4)"], kind="old", src=OLD),
        mcq("RESP-02-03-4", """A 60-year-old man has worked in a stone-crushing mill for 30 years. He has had a dry cough for 2 years and weight loss without fever. He does not smoke. PFT shows a restrictive defect. Repeated sputum AFB is negative, and 3 months of bronchodilator gave no benefit. CXR shows upper-zone nodular opacities. What is the most appropriate management?""",
            "Stop the exposure by leaving this work",
            ["Empirical anti-TB drugs for 6 months", "Nebulized bronchodilator four times daily",
             "Inhaled corticosteroid", "Codeine for cough suppression"],
            explain="""ประวัติทำงานโรงโม่หินนาน 30 ปี PFT เป็น restrictive และเห็น nodules ที่ปอดบน คือ silicosis ซึ่งไม่มีการรักษาให้หายขาด สิ่งสำคัญที่สุดคือหยุดการสัมผัส
- Anti-TB 6 เดือนโดยไม่มีหลักฐาน TB (AFB ลบ ไม่มีไข้) ไม่เหมาะ แต่ควรเฝ้าระวัง TB เพราะความเสี่ยงสูงขึ้น
- Bronchodilator ลองให้มา 3 เดือนแล้วไม่ได้ผล
- ICS ไม่ช่วยพังผืดจาก silica
- Codeine บรรเทาอาการไอ แต่ไม่ช่วยให้โรคหยุดลุกลาม""",
            pearl="Occupational lung disease → หยุด/ย้ายงาน เป็นการรักษาหลัก",
            topic="Occupational mx", ref=[f"{D} หน้า 223, 239–240"], nl=["2.3.19(8)"], kind="old", src=OLD),
        mcq("RESP-02-03-5", """A 20-year-old man has worked in a car-spray-painting factory for 2 years and now has progressive dyspnea. Lung function shows a restrictive defect attributed to occupational exposure. What is the most appropriate advice for this patient?""",
            "Change job or move to a position without exposure",
            ["Wear personal protective equipment while spraying and continue the same job",
             "Ask the factory to switch to a different spray solvent",
             "Install ventilation fans in the factory",
             "Use an inhaled bronchodilator before each shift"],
            explain="""ผู้ป่วยมีโรคปอดจากอาชีพแล้ว การรักษาที่ได้ผลคือหยุดการสัมผัสโดยย้ายงานหรือเปลี่ยนตำแหน่ง
- PPE ช่วยป้องกันคนที่ยังไม่ป่วย แต่ไม่พอสำหรับคนที่มีโรคแล้วและยังทำงานเดิม
- การเปลี่ยนน้ำยาพ่นสีไม่แน่ว่าจะปลอดภัย และไม่ได้อยู่ในการควบคุมของแพทย์
- พัดลมระบายอากาศเป็นมาตรการระดับโรงงาน ลดการสัมผัสได้ไม่หมด
- Bronchodilator ไม่ช่วย restrictive disease""",
            pearl="ป่วยจากงานแล้ว → ย้ายงาน/เปลี่ยนตำแหน่ง",
            topic="Occupational advice", ref=[f"{D} หน้า 237–238"], nl=["2.3.19(8)"], kind="old", src=OLD),
    ])

LECTURE = lecture("02", "Restrictive lung diseases",
    subtitle="ILD · systemic sclerosis · occupational lung disease",
    objectives=["บอกสาเหตุ อาการ และการตรวจของ ILD และภาวะแทรกซ้อน cor pulmonale ได้",
                "แยก limited กับ diffuse SSc และเลือกยาตามอวัยวะ (CCB, ACEI, MMF, PPI) ได้",
                "จับคู่อาชีพกับ pneumoconiosis และลักษณะ CXR (บน vs ล่าง) ได้",
                "ให้คำแนะนำหลักคือหยุดสัมผัสในโรคปอดจากอาชีพได้"],
    sections=[S1, S2, S3])
