from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Dermato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 09-01 Leprosy
F_SPEC = fig("derm-09-01-f1", "Leprosy spectrum: TT ↔ LL ตามภูมิคุ้มกันชนิด cell-mediated", '''<svg viewBox="0 0 740 360">
 <defs><marker id="derm-09-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="20" y="20" width="700" height="34" rx="8" class="sunk"/>
 <text x="40" y="42" class="tb">TT</text>
 <text x="190" y="42" class="t2">BT</text>
 <text x="360" y="42" class="t2">BB</text>
 <text x="520" y="42" class="t2">BL</text>
 <text x="690" y="42" class="tb">LL</text>
 <path d="M90 74H650" class="lnok" marker-start="url(#derm-09-01-a)"/>
 <text x="120" y="68" class="t3">CMI ดี (Th1)</text>
 <path d="M90 94H650" class="lnbad" marker-end="url(#derm-09-01-a)"/>
 <text x="560" y="114" class="t3">เชื้อมาก · antibody สูง</text>
 <rect x="20" y="126" width="330" height="224" rx="10" class="oksoft"/>
 <text x="185" y="150" text-anchor="middle" class="tb">Tuberculoid (TT) → PB</text>
 <circle cx="70" cy="200" r="30" class="sunk"/>
 <circle cx="70" cy="200" r="30" class="lnbad"/>
 <text x="70" y="204" text-anchor="middle" class="t3">ชา</text>
 <text x="116" y="184" class="t2">1–5 รอยโรค ขอบชัด</text>
 <text x="116" y="204" class="t2">ด่างขาว ขอบนูนแดง</text>
 <text x="116" y="224" class="t2">แห้ง ขุย ขนร่วง ชา</text>
 <text x="36" y="262" class="t2">เส้นประสาทโต ไม่สมมาตร</text>
 <text x="36" y="284" class="t2">(ulnar, common peroneal)</text>
 <text x="36" y="310" class="tb">Slit-skin smear: ลบ</text>
 <text x="36" y="332" class="t3">non-caseating granuloma</text>
 <rect x="370" y="126" width="350" height="224" rx="10" class="badsoft"/>
 <text x="545" y="150" text-anchor="middle" class="tb">Lepromatous (LL) → MB</text>
 <circle cx="400" cy="190" r="8" class="bad"/><circle cx="424" cy="200" r="6" class="bad"/><circle cx="412" cy="216" r="7" class="bad"/><circle cx="436" cy="182" r="5" class="bad"/>
 <circle cx="450" cy="214" r="6" class="bad"/><circle cx="398" cy="232" r="5" class="bad"/>
 <text x="474" y="184" class="t2">มากมาย สมมาตร</text>
 <text x="474" y="204" class="t2">macule plaque nodule ขอบไม่ชัด</text>
 <text x="474" y="224" class="t2">ติ่งหู คิ้วหนา (leonine facies)</text>
 <text x="386" y="262" class="t2">neuropathy สมมาตร (glove &amp; stocking)</text>
 <text x="386" y="284" class="t2">คิ้วร่วง จมูกยุบ (เสริม)</text>
 <text x="386" y="310" class="tb">Slit-skin smear: บวก (AFB)</text>
 <text x="386" y="332" class="t3">CMI แย่ เชื้อเต็ม macrophage</text>
</svg>''', "ยิ่งภูมิคุ้มกันชนิดเซลล์ดี รอยโรคยิ่งน้อย ขอบชัด ชามาก และหาเชื้อไม่เจอ (TT) — ภูมิไม่ดีเชื้อยิ่งเต็มผิว ผื่นมากสมมาตร smear บวก (LL)")

F_DX = fig("derm-09-01-f2", "วินิจฉัยและเลือกสูตรยาโรคเรื้อน (WHO)", '''<svg viewBox="0 0 740 300">
 <defs><marker id="derm-09-01-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="720" height="104" rx="10" class="acsoft"/>
 <text x="370" y="32" text-anchor="middle" class="tb">Cardinal signs — มี ≥ 1 ข้อ = leprosy</text>
 <text x="30" y="58" class="t2">1. ปื้นด่างขาว/แดงที่ชา (loss of sensation)</text>
 <text x="30" y="80" class="t2">2. เส้นประสาทส่วนปลายโต + มีอาการ neuropathy</text>
 <text x="30" y="102" class="t2">3. Slit-skin smear พบ AFB</text>
 <path d="M250 114L160 146" class="ln" marker-end="url(#derm-09-01-b)"/>
 <path d="M490 114L580 146" class="ln" marker-end="url(#derm-09-01-b)"/>
 <rect x="10" y="148" width="350" height="142" rx="10" class="oksoft"/>
 <text x="185" y="172" text-anchor="middle" class="tb">Paucibacillary (PB)</text>
 <text x="185" y="194" text-anchor="middle" class="t2">1–5 รอยโรค และ smear ลบ</text>
 <text x="185" y="226" text-anchor="middle" class="t2">Dapsone + Rifampicin + Clofazimine</text>
 <text x="185" y="254" text-anchor="middle" class="tb">6 เดือน</text>
 <rect x="380" y="148" width="350" height="142" rx="10" class="badsoft"/>
 <text x="555" y="172" text-anchor="middle" class="tb">Multibacillary (MB)</text>
 <text x="555" y="194" text-anchor="middle" class="t2">&gt; 5 รอยโรค หรือ smear บวก</text>
 <text x="555" y="226" text-anchor="middle" class="t2">Dapsone + Rifampicin + Clofazimine</text>
 <text x="555" y="254" text-anchor="middle" class="tb">12 เดือน</text>
</svg>''', "ยาสามตัวเหมือนกันทั้งสองกลุ่ม (WHO 2018) ต่างกันแค่ระยะเวลา — smear บวกเพียงอย่างเดียวก็จัดเป็น MB")

S1 = sec("derm-09-01", "Leprosy (Hansen disease) และ leprosy reaction",
    "M. leprae · TT = รอยโรคน้อย ขอบชัด ด่างขาวชา เส้นประสาทโตไม่สมมาตร smear ลบ · LL = รอยโรคมากสมมาตร leonine facies smear บวก · ≥ 1 cardinal sign · PB 6 เดือน, MB 12 เดือน (dapsone + rifampicin + clofazimine) · reaction type 1 vs 2 (ENL)",
    minutes=11, source=f"{D} หน้า 293–314", nl=["2.3.12-3(9)", "B4.2.2-3(1)"],
    md='''
### เชื้อและการติดต่อ

- **Mycobacterium leprae** (acid-fast bacilli) — ชอบที่เย็น: ผิว เส้นประสาทส่วนปลาย จมูก ติ่งหู
- ติดต่อ: **respiratory droplet**, **ดินปนเปื้อน**, **สัมผัสใกล้ชิดผู้ป่วย**, **armadillo**

### Spectrum (สไลด์หน้า 294–296)

[[fig:derm-09-01-f1]]

| | **Lepromatous (LL)** | **Tuberculoid (TT)** |
|---|---|---|
| ภูมิ | **CMI แย่** | CMI ดี |
| ผิวหนัง | **macules/plaques/nodules จำนวนมาก สมมาตร** ขอบไม่ชัด · **leonine facies** (ติ่งหู แก้ม คิ้วหนา) | **รอยโรคน้อย ขอบชัด ด่างขาว (hypopigmented) ขอบนูนแดง** · **แห้ง ขุย ขนร่วง** · **ชา** |
| เส้นประสาท | **neuropathy + เส้นประสาทโต สมมาตร** (glove & stocking) | **neuropathy + เส้นประสาทโต ไม่สมมาตร** (เช่น ulnar → กล้ามเนื้อมือลีบ) |
| Slit-skin smear | **บวก** | **ลบ** |

### การวินิจฉัย (≥ 1 ข้อ) และการจำแนกเพื่อรักษา

[[fig:derm-09-01-f2]]

- **Slit-skin smear** (ขูดติ่งหู ข้อศอก รอยโรค ย้อม AFB): PB ลบ, MB บวก
- **Skin biopsy**: TT = non-caseating granuloma รอบเส้นประสาท · LL = foamy macrophage เต็มเชื้อ (เสริม)

### การรักษา (สไลด์หน้า 300 — WHO 2018)

| กลุ่ม | นิยาม | ยา | ระยะเวลา |
|---|---|---|---|
| **Paucibacillary (PB)** | **1–5 รอยโรค** (smear ลบ) | **dapsone + rifampicin + clofazimine** | **6 เดือน** |
| **Multibacillary (MB)** | **> 5 รอยโรค หรือ smear บวก** | **dapsone + rifampicin + clofazimine** | **12 เดือน** |

- เสริม: ตรวจ G6PD ก่อน dapsone · clofazimine ทำให้ผิวคล้ำแดง · rifampicin ทำให้ปัสสาวะสีส้ม

### Leprosy reactions (สไลด์หน้า 301–302)

| | **Type 1 (reversal reaction)** | **Type 2 (erythema nodosum leprosum, ENL)** | **Lucio phenomenon** |
|---|---|---|---|
| กลไก (เสริม) | CMI กลับมาแรง (type IV) — BT/BB/BL | immune complex (type III) — BL/LL | vasculitis ใน diffuse LL |
| ผิว | **รอยโรคเดิมแดง ร้อน บวม เจ็บ** | **ตุ่ม/ก้อนใต้ผิว แดง เจ็บ กระจายทั่วตัว** | **ผื่นจ้ำเลือดและแผลทั่วตัว** |
| Systemic | ไม่ค่อยมี (แต่ **neuritis เฉียบพลัน** อันตราย (เสริม)) | **ไข้ ปวดข้อ ต่อมน้ำเหลืองโตเจ็บ uveitis orchitis glomerulonephritis** | ไม่ค่อยมี |
| รักษา (เสริม) | prednisolone | prednisolone, thalidomide | — |

- **ไม่หยุด MDT ระหว่างเกิด reaction** (เสริม)
''',
    figs=[F_SPEC, F_DX],
    pearls=[
        "ด่างขาว/แดงที่ชา หรือเส้นประสาทโต + neuropathy หรือ smear บวก (≥ 1 ข้อ) = leprosy",
        "TT: รอยโรคน้อย ขอบชัด ชา ขนร่วง เส้นประสาทโตไม่สมมาตร smear ลบ",
        "LL: รอยโรคมากสมมาตร leonine facies neuropathy สมมาตร smear บวก",
        "PB (1–5 รอยโรค smear ลบ) 6 เดือน · MB (> 5 หรือ smear บวก) 12 เดือน — dapsone + rifampicin + clofazimine",
        "Type 1 = รอยโรคเดิมอักเสบ · type 2 (ENL) = ตุ่มใต้ผิวเจ็บทั่วตัว + ไข้ ปวดข้อ uveitis orchitis",
    ],
    items=[
        mcq("DERM-09-01-1", """A 23-year-old woman has a single annular erythematous plaque with central clearing on her thigh. The lesion is dry and hairless, and pinprick sensation within it is decreased. KOH preparation is negative. What is the most likely diagnosis?""",
            "Leprosy", ["Tinea corporis", "Granuloma annulare", "Nummular eczema", "Erythema migrans"],
            explain="""ผื่นวงที่ **ชา (decreased pinprick)** แห้งไม่มีขน = cardinal sign ของ **leprosy** (tuberculoid) — **การชาในรอยโรคคือจุดตัดสิน** (สไลด์หน้า 298, 303–304)
- Tinea corporis เป็นวงขอบนูนขุยแต่ความรู้สึกปกติ และ KOH บวก
- Granuloma annulare เป็นวงตุ่มนูนเรียบไม่มีขุย ความรู้สึกปกติ (เสริม)
- Nummular eczema เป็นวงเหรียญที่คัน ไม่ชา
- Erythema migrans (Lyme) เป็นวงแดงขยายหลังเห็บกัด ไม่ชาและไม่พบในไทย""",
            pearl="ผื่นวง/ด่างขาวที่ชา = leprosy จนกว่าจะพิสูจน์ว่าไม่ใช่",
            topic="Leprosy dx", ref=[f"{D} หน้า 303–304"], nl=["2.3.12-3(9)"], kind="old", src=OLD),
        mcq("DERM-09-01-2", """A 50-year-old woman says her face feels thicker than normal and she has developed a rash all over her body. Examination shows leonine facies with thickened earlobes, cheeks and eyebrows, and diffuse, symmetric nodules and plaques with ill-defined borders. Sensation in a glove-and-stocking distribution is reduced. Which result is expected on slit-skin smear and what is the classification?""",
            "Acid-fast bacilli present; multibacillary (lepromatous) leprosy", ["No acid-fast bacilli; paucibacillary (tuberculoid) leprosy", "No acid-fast bacilli; multibacillary leprosy", "Acid-fast bacilli present; paucibacillary leprosy", "Septate hyphae; deep fungal infection"],
            explain="""**Leonine facies + ผื่นก้อนมากสมมาตรขอบไม่ชัด + neuropathy แบบ glove & stocking** = **lepromatous leprosy** — CMI แย่ เชื้อมาก → **smear บวก (AFB)** และจัดเป็น **multibacillary** (สไลด์หน้า 294–295, 299–300, 305–306)
- Smear ลบเป็นของ TT/PB ซึ่งมีรอยโรคน้อยขอบชัด
- Smear ลบ + MB เป็นไปได้เมื่อรอยโรค > 5 แต่ LL แบบนี้ smear บวกเสมอ
- ผล smear บวกจัดเป็น MB อัตโนมัติ จะเป็น PB ไม่ได้
- Septate hyphae เป็นเชื้อราซึ่งไม่ทำให้เกิด leonine facies และชา""",
            pearl="LL = leonine facies + smear บวก = MB",
            topic="LL", ref=[f"{D} หน้า 305–306"], nl=["2.3.12-3(9)"], kind="old", src=OLD),
        mcq("DERM-09-01-3", """A 55-year-old man has a slowly enlarging white patch on his right forearm. It is not itchy but feels numb. Examination shows a hypopigmented macule with a raised erythematous border, dry hairless surface, decreased pinprick sensation, a thickened palpable right ulnar nerve and wasting of the right hypothenar and interosseous muscles. What is the most likely diagnosis?""",
            "Tuberculoid leprosy", ["Vitiligo", "Secondary syphilis", "Tinea corporis", "Pityriasis versicolor"],
            explain="""ด่างขาวขอบนูน **ชา** ขนร่วง + **ulnar nerve โต + กล้ามเนื้อมือลีบ** ข้างเดียว = **tuberculoid leprosy** (สไลด์หน้า 294, 307–308)
- Vitiligo เป็นด่างขาวจั๊วะขอบชัด ความรู้สึกปกติ ไม่มีเส้นประสาทโต
- Secondary syphilis เป็นผื่นทั่วตัวรวมฝ่ามือฝ่าเท้า ไม่ชา
- Tinea corporis เป็นวงขอบนูนขุย คัน ความรู้สึกปกติ
- Pityriasis versicolor เป็นด่างขาวขุยละเอียดที่ลำตัว ไม่ชา""",
            pearl="ด่างขาวชา + เส้นประสาทโตข้างเดียว = TT leprosy",
            topic="TT", ref=[f"{D} หน้า 307–308"], nl=["2.3.12-3(9)"], kind="old", src=OLD),
        mcq("DERM-09-01-4", """A patient has many erythematous bumps and anesthetic patches (more than 10 lesions), nasal mucosal involvement with crusting, thickened peripheral nerves and glove-and-stocking sensory loss. What is the most appropriate management?""",
            "Dapsone, rifampicin and clofazimine for 12 months", ["Dapsone and rifampicin for 6 months", "Dapsone, rifampicin and clofazimine for 6 months", "Reassure without treatment", "Rifampicin, isoniazid, pyrazinamide and ethambutol for 6 months"],
            explain="""รอยโรค **> 5** + นิวโรพาทีสมมาตร + จมูก = **multibacillary leprosy** → **dapsone + rifampicin + clofazimine 12 เดือน** (WHO 2018) (สไลด์หน้า 300, 311–312) · ตัวเลือกในสไลด์คือ slit skin smear / 1 year medical course / reassure / full course — คำตอบคือรักษา 1 ปี
- ยา 2 ตัว 6 เดือนเป็นสูตร PB แบบเก่า (ก่อน 2018) และสั้นไปสำหรับ MB
- ยา 3 ตัว 6 เดือนเป็นสูตร PB
- การไม่รักษาทำให้พิการและแพร่เชื้อ
- สูตร RIPE เป็นการรักษาวัณโรค ไม่ใช่โรคเรื้อน""",
            pearl="MB → 3 ยา 12 เดือน · PB → 3 ยา 6 เดือน",
            topic="Leprosy tx", ref=[f"{D} หน้า 300, 311–312"], nl=["2.3.12-3(9)"], kind="old", src=OLD),
        mcq("DERM-09-01-5", """A 60-year-old man has had painful red nodules for 1 month with fever and joint pain. Examination shows multiple tender erythematous nodules on the trunk, arms and legs, and infiltrated plaques with ill-defined borders on both earlobes and the back. Slit-skin smears from the earlobe and nasal mucosa show acid-fast bacilli. What is the most likely diagnosis?""",
            "Lepromatous leprosy with type 2 reaction (erythema nodosum leprosum)", ["Tuberculoid leprosy", "Lepromatous leprosy with type 1 (reversal) reaction", "Cutaneous vasculitis", "Cutaneous tuberculosis"],
            explain="""LL (ติ่งหูหนา smear บวก) + **ก้อนใต้ผิวแดงเจ็บกระจายทั่วตัว + ไข้ ปวดข้อ** = **type 2 reaction (ENL)** (สไลด์หน้า 302, 313–314) — สไลด์ใส่ "non-caseating granuloma" ในโจทย์ แต่ histology ของ ENL เด่นที่ neutrophil/vasculitis บน foamy macrophage (เสริม)
- Tuberculoid leprosy มีรอยโรคน้อยและ smear ลบ
- Type 1 reaction คือรอยโรคเดิมบวมแดงเจ็บ ไม่ใช่ก้อนใหม่ทั่วตัวพร้อมอาการ systemic
- Vasculitis ไม่อธิบาย AFB ใน smear
- Cutaneous TB ไม่ทำให้ติ่งหูหนาและเชื้อ AFB เต็มผิวแบบนี้""",
            pearl="LL + ก้อนแดงเจ็บทั่วตัว + ไข้ ปวดข้อ = ENL (type 2)",
            topic="Leprosy reaction", ref=[f"{D} หน้า 313–314"], nl=["2.3.12-3(9)"], kind="old", src=OLD),
    ])

# ---------------------------------------------------------------- 09-02 EN
S2 = sec("derm-09-02", "Erythema nodosum (EN)",
    "Panniculitis · idiopathic บ่อยสุด, ติดเชื้อ (strep, TB), autoimmune (sarcoid, IBD), ยา (OCP) · ก้อนแดงเจ็บที่หน้าแข้งสองข้าง ไม่แตก ไม่เป็นแผล · CBC ESR CRP ASO throat swab CXR · รักษาสาเหตุ + NSAID",
    minutes=5, source=f"{D} หน้า 315–317", nl=["2.3.12-3(5)", "B4.2.2-3(7)"],
    md='''
### กลไก

- **Septal panniculitis** — ปฏิกิริยาภูมิไวเกิน (delayed hypersensitivity) ต่อสิ่งกระตุ้น (เสริม)

### สาเหตุ (สไลด์หน้า 315)

- **Idiopathic (พบบ่อยสุด)**
- **ติดเชื้อ**: streptococcal pharyngitis (บ่อยสุดในเด็ก), TB, leprosy (ENL), ไวรัส, เชื้อรา (เสริม)
- **Autoimmune**: sarcoidosis (Löfgren syndrome), IBD, Behçet (เสริม)
- **ยา**: OCP, sulfonamides (เสริม) · ตั้งครรภ์

### สิ่งที่เห็น

| หัวข้อ | รายละเอียด |
|---|---|
| Primary lesion | **erythematous, tender nodules** ขนาด 1–5 cm (เสริม) ใต้ผิว คลำได้มากกว่ามองเห็น |
| ตำแหน่ง | **หน้าแข้งสองข้าง (both shins)** สมมาตร |
| วิวัฒนาการ | สีเปลี่ยนเหมือนรอยช้ำ (แดง → ม่วง → เหลืองเขียว) **ไม่แตก ไม่เป็นแผล ไม่มีแผลเป็น** (เสริม) |
| อาการร่วม | ไข้ต่ำ ปวดข้อ (เสริม) |

### Investigation (ตามสาเหตุที่สงสัย)

- **CBC, ESR, CRP**
- **ASO titer / throat swab culture**
- **CXR** (hilar adenopathy → sarcoidosis, TB)
- **Skin biopsy เมื่อวินิจฉัยไม่แน่ใจ** (ต้องเป็น deep incisional ให้ถึงไขมัน (เสริม))

### การรักษา

- **รักษาสาเหตุ + supportive (NSAID)**, พัก ยกขา (เสริม) · หายเองใน 3–6 สัปดาห์ (เสริม)

> ก้อนแดงเจ็บหน้าแข้งสองข้างในหญิงสาว ไม่มีโรคประจำตัว ไม่กินยา = EN (idiopathic) · ถ้าเป็นข้างเดียว ร้อน ลาม = cellulitis
''',
    pearls=[
        "EN = ก้อนแดงเจ็บใต้ผิวที่หน้าแข้งสองข้าง ไม่แตก ไม่เป็นแผล",
        "สาเหตุบ่อยสุด idiopathic · อื่น ๆ strep, TB, sarcoid, IBD, OCP",
        "ตรวจ CBC ESR CRP, ASO/throat swab, CXR · biopsy เมื่อไม่แน่ใจ",
        "รักษาสาเหตุ + NSAID",
    ],
    items=[
        mcq("DERM-09-02-1", """A 30-year-old woman has painful, warm, erythematous, 2–4 cm subcutaneous nodules on the anterior and lateral aspects of both lower legs for 1 week. They are not ulcerated or fluctuant. She has no underlying disease and takes no medications. What is the most likely diagnosis?""",
            "Erythema nodosum", ["Cellulitis", "Abscess", "Erysipelas", "Gnathostomiasis"],
            explain="""ก้อนแดงเจ็บ **ใต้ผิว** ที่หน้าแข้ง **สองข้าง** ไม่มีหนอง ไม่เป็นแผล = **erythema nodosum** (สาเหตุบ่อยสุด idiopathic) (สไลด์หน้า 315–317)
- Cellulitis มักเป็นข้างเดียว เป็นปื้นแดงลามขอบไม่ชัด ไม่ใช่ก้อนหลายก้อนสองข้าง
- Abscess เป็นก้อน fluctuant มีหนอง
- Erysipelas เป็นปื้นแดงขอบนูนชัด ข้างเดียว พร้อมไข้
- Gnathostomiasis ทำให้บวมเคลื่อนที่ (migratory swelling) หลังกินปลาดิบ/อาหารสุก ๆ ดิบ ๆ ไม่ใช่ก้อนเจ็บคงที่สองข้าง""",
            pearl="ก้อนแดงเจ็บหน้าแข้งสองข้าง = EN",
            topic="EN dx", ref=[f"{D} หน้า 316–317"], nl=["2.3.12-3(5)"], kind="old", src=OLD),
        mcq("DERM-09-02-2", """A 28-year-old woman has tender red nodules on both shins, fever, bilateral ankle arthritis and a dry cough for 2 weeks. CBC is normal except for an elevated ESR. Which initial investigation is most likely to reveal the underlying cause?""",
            "Chest X-ray", ["Skin prick test", "KOH preparation", "Tzanck smear", "Patch test"],
            explain="""EN + ปวดข้อเท้าสองข้าง + ไอ ชวนนึก **sarcoidosis (Löfgren syndrome)** หรือ TB → สไลด์ให้ตรวจ **CXR** หา bilateral hilar lymphadenopathy (สไลด์หน้า 315; Löfgren (เสริม))
- Skin prick test ใช้หา IgE allergen ไม่เกี่ยวกับ EN
- KOH ใช้หาเชื้อราผิวตื้น
- Tzanck ใช้หา herpes
- Patch test ใช้หา allergen ของ contact dermatitis""",
            pearl="EN → CXR (sarcoid/TB) + ASO/throat swab + ESR",
            topic="EN Ix", ref=[f"{D} หน้า 315"], nl=["2.3.12-3(5)"]),
        mcq("DERM-09-02-3", """A 9-year-old girl developed tender erythematous nodules on both shins 2 weeks after an episode of exudative tonsillitis. ASO titer is markedly raised. She has no cardiac murmur and urinalysis is normal. Besides NSAIDs for pain, what is the most appropriate management?""",
            "Treat the streptococcal infection with penicillin", ["Systemic corticosteroid as first-line", "Excise the largest nodule", "Start dapsone, rifampicin and clofazimine", "Stop the oral contraceptive pill"],
            explain="""EN ตามหลัง **streptococcal pharyngitis** (ASO สูง) → **รักษาสาเหตุ** (penicillin) + NSAID (สไลด์หน้า 315)
- Systemic steroid ไม่ใช่ first line และต้อง R/O การติดเชื้อก่อน
- การตัดก้อนไม่ใช่การรักษา (biopsy ทำเมื่อวินิจฉัยไม่แน่ใจเท่านั้น)
- MDT ใช้รักษาโรคเรื้อน ซึ่งเด็กรายนี้ไม่มีด่างชาหรือเส้นประสาทโต
- เด็กอายุ 9 ปีไม่ได้กิน OCP""",
            pearl="EN → รักษาสาเหตุ + NSAID",
            topic="EN tx", ref=[f"{D} หน้า 315"], nl=["2.3.12-3(5)"]),
    ])

LECTURE = lecture("09", "Leprosy & erythema nodosum", subtitle="leprosy spectrum · การวินิจฉัย · MDT · leprosy reactions · erythema nodosum",
    objectives=[
        "จำ cardinal signs ของ leprosy และแยก TT กับ LL",
        "จัด PB/MB และให้ MDT 6 หรือ 12 เดือน",
        "แยก type 1 reaction, type 2 reaction (ENL) และ Lucio phenomenon",
        "วินิจฉัย erythema nodosum สืบค้นสาเหตุ และรักษา",
    ],
    sections=[S1, S2])
