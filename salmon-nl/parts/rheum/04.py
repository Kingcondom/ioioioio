from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Rheumato"
OLD = "ตัวอย่างข้อสอบในสไลด์"

# ---------------------------------------------------------------- 04-01 Hyperuricemia & acute gout dx
F_PROG = fig("rheum-04-01-f1", "การดำเนินโรคเกาต์: 4 ระยะ", '''<svg viewBox="0 0 740 330">
 <defs><marker id="rheum-04-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="70" y="14" width="130" height="28" rx="6" class="oksoft"/>
 <text x="135" y="33" text-anchor="middle" class="t2">Uric acid สูง</text>
 <rect x="200" y="14" width="340" height="28" rx="6" class="misssoft"/>
 <text x="370" y="33" text-anchor="middle" class="t2">Acute flares ซ้ำ ๆ + intercritical period</text>
 <rect x="540" y="14" width="180" height="28" rx="6" class="badsoft"/>
 <text x="630" y="33" text-anchor="middle" class="t2">Chronic tophaceous</text>
 <path d="M70 250V60" class="ln" marker-end="url(#rheum-04-01-a)"/>
 <path d="M70 250H725" class="ln" marker-end="url(#rheum-04-01-a)"/>
 <text x="60" y="80" text-anchor="end" class="t3">ปวด</text>
 <text x="720" y="272" text-anchor="end" class="t3">เวลา (ปี)</text>
 <rect x="212" y="226" width="14" height="24" class="miss"/>
 <rect x="300" y="200" width="18" height="50" class="miss"/>
 <rect x="376" y="168" width="22" height="82" class="miss"/>
 <rect x="446" y="136" width="26" height="114" class="miss"/>
 <path d="M548 250V110H580V170L610 150V80H640V200L670 140V250Z" class="bad"/>
 <text x="135" y="240" text-anchor="middle" class="t3">ไม่มีอาการ</text>
 <text x="219" y="218" text-anchor="middle" class="t3">ครั้งแรก</text>
 <text x="420" y="104" text-anchor="middle" class="t3">กำเริบถี่ขึ้น นานขึ้น</text>
 <text x="420" y="120" text-anchor="middle" class="t3">รุนแรงขึ้น</text>
 <text x="263" y="290" text-anchor="middle" class="t3">ช่วงสงบแรก</text>
 <text x="263" y="306" text-anchor="middle" class="t3">อาจนาน ≥ 5 ปี</text>
 <text x="410" y="290" text-anchor="middle" class="t3">intercritical period</text>
 <text x="410" y="306" text-anchor="middle" class="t3">สั้นลงเรื่อย ๆ</text>
 <text x="610" y="290" text-anchor="middle" class="t3">ปวดตลอด tophi</text>
 <text x="610" y="306" text-anchor="middle" class="t3">ข้อผิดรูป punched-out</text>
 <path d="M228 262H296" class="lnok"/>
 <path d="M322 262H372" class="lnok"/>
 <path d="M402 262H442" class="lnok"/>
 <path d="M476 262H540" class="lnok"/>
</svg>''', "แท่งเหลืองคือ acute flare ที่ถี่และรุนแรงขึ้น ช่วงสงบ (เส้นเขียว) สั้นลงเรื่อย ๆ จนเข้าสู่ chronic tophaceous gout ที่ปวดตลอด (สไลด์หน้า 70)")

F_CRY = fig("rheum-04-01-f2", "ผลึกใต้ polarized light: gout vs CPPD", '''<svg viewBox="0 0 720 300">
 <defs><marker id="rheum-04-01-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="340" height="280" rx="12" class="misssoft"/>
 <rect x="370" y="10" width="340" height="280" rx="12" class="c1soft"/>
 <text x="180" y="36" text-anchor="middle" class="tb">Gout: monosodium urate (MSU)</text>
 <text x="540" y="36" text-anchor="middle" class="tb">CPPD: calcium pyrophosphate</text>
 <path d="M40 70H160" class="lna" marker-end="url(#rheum-04-01-b)"/>
 <text x="40" y="62" class="t3">แกน compensator</text>
 <path d="M400 70H520" class="lna" marker-end="url(#rheum-04-01-b)"/>
 <text x="400" y="62" class="t3">แกน compensator</text>
 <rect x="50" y="94" width="110" height="7" rx="3" class="miss"/>
 <rect x="50" y="116" width="96" height="7" rx="3" class="miss"/>
 <rect x="226" y="80" width="7" height="100" rx="3" class="c1"/>
 <rect x="248" y="88" width="7" height="86" rx="3" class="c1"/>
 <text x="104" y="146" text-anchor="middle" class="t2">ขนาน = เหลือง</text>
 <text x="240" y="196" text-anchor="middle" class="t2">ตั้งฉาก = ฟ้า</text>
 <rect x="410" y="92" width="58" height="22" class="c1"/>
 <rect x="420" y="124" width="44" height="18" class="c1"/>
 <rect x="596" y="80" width="20" height="54" class="miss"/>
 <rect x="626" y="88" width="16" height="42" class="miss"/>
 <text x="440" y="166" text-anchor="middle" class="t2">ขนาน = ฟ้า</text>
 <text x="618" y="156" text-anchor="middle" class="t2">ตั้งฉาก = เหลือง</text>
 <text x="20" y="224" class="tb">รูปเข็ม (needle)</text>
 <text x="20" y="244" class="t2">strongly negative birefringent</text>
 <text x="20" y="264" class="t3">1st MTP, ข้อเท้า, เข่า · ชายวัยกลางคน</text>
 <text x="380" y="224" class="tb">รูปสี่เหลี่ยมขนมเปียกปูน (rhomboid)</text>
 <text x="380" y="244" class="t2">weakly positive birefringent</text>
 <text x="380" y="264" class="t3">ข้อมือ, เข่า · อายุ &gt; 60 ปี · chondrocalcinosis</text>
</svg>''', "จำแบบสลับกัน: MSU ขนานแกนเป็นสีเหลือง (negative) ส่วน CPP ขนานแกนเป็นสีฟ้า (positive) · ทั้งสองแบบน้ำไขข้อเป็นกลุ่ม inflammatory และ culture ลบ")

S1 = sec("rheum-04-01", "Hyperuricemia และ gout: กลไก อาการ การวินิจฉัย",
    "UA > 7 (ชาย) > 6 (หญิง) · ขับออกลด (ยา, CKD) หรือสร้างเพิ่ม (alcohol, purine, cell turnover) · podagra · arthrocentesis = gold standard: needle-shaped negative birefringent · X-ray chronic: punched-out overhanging edge", minutes=9,
    source=f"{D} หน้า 67–72, 82–85", nl=["2.3.13(2)", "B5.2.5(1)", "B5.3(4)"],
    md='''
### Hyperuricemia (สไลด์หน้า 67)
- นิยาม: serum uric acid **ชาย > 7 mg/dL, หญิง > 6 mg/dL**
- กลไก: uric acid เป็นผลผลิตสุดท้ายของ purine (ผ่าน xanthine oxidase) ขับทางไตเป็นหลัก → เกินจุดอิ่มตัว (~6.8 mg/dL) จะตกผลึกเป็น MSU (เสริม)

| สาเหตุ | ตัวอย่าง |
|---|---|
| **ขับออกลดลง** (พบบ่อยกว่า) | ยา: **pyrazinamide, aspirin (ขนาดต่ำ), furosemide, thiazide** · **CKD** · **วัยหมดประจำเดือน** (estrogen ช่วยขับ uric acid) |
| **สร้างเพิ่มขึ้น** | **alcohol** (โดยเฉพาะเบียร์), **อาหาร purine สูง** (เนื้อแดง seafood เครื่องใน) · **cell turnover สูง**: tumor lysis syndrome, hemolytic anemia, myeloproliferative neoplasm |

### Acute gout attack (สไลด์หน้า 68)
- ผลึก **monosodium urate (MSU)** ตกตะกอนในน้ำไขข้อและเนื้อเยื่อ → neutrophil กิน → inflammasome/IL-1 → อักเสบรุนแรงเฉียบพลัน (กลไกเสริม)
- ปัจจัยเสี่ยงหลัก: **hyperuricemia** · ตัวกระตุ้น (เสริม): ดื่มเหล้า กินเลี้ยง ขาดน้ำ ผ่าตัด เริ่มหรือปรับยา ULT/ขับปัสสาวะ
- **ไข้ต่ำ ๆ** ได้ · **acute mono/oligoarthritis** **เด่นที่ข้อขา**
- ตำแหน่ง: **1st MTP (podagra)**, **ข้อเท้า**, **เข่า** · ปวดสุดใน 24 ชั่วโมง หายเองใน 1–2 สัปดาห์ (เสริม)

### Chronic tophaceous gout (สไลด์หน้า 69–70)
- **Tophi** = ก้อนแข็ง **ไม่เจ็บ** สี **เหลือง/ขาว** หลายก้อน ± ข้อผิดรูป (นิ้ว ติ่งหู ข้อศอก Achilles)
- การดำเนินโรค: asymptomatic hyperuricemia → acute flare → intercritical period ที่ **สั้นลงเรื่อย ๆ** → advanced/tophaceous gout

[[fig:rheum-04-01-f1]]

### Investigation (สไลด์หน้า 71–72)
- ส่วนใหญ่ **วินิจฉัยทางคลินิก**
- **Arthrocentesis = gold standard** ทำเมื่อ **วินิจฉัยไม่แน่ใจ** หรือ **ต้อง R/O septic arthritis**
  - **ผลึกรูปเข็ม (needle-shaped) MSU, negatively birefringent** ใต้ polarized light: **ขนานแกน = เหลือง, ตั้งฉาก = ฟ้า**
  - WBC **> 2,000/µL (PMN > 50%)** = กลุ่ม inflammatory
  - **G/S และ C/S ลบ**
- **Serum uric acid** สูง แต่ **อาจปกติหรือต่ำลงระหว่าง attack** → ค่าปกติไม่ตัด gout
- **X-ray**:
  - acute: ปกติ หรือเห็นแค่ soft tissue swelling
  - chronic: **punched-out lytic bone lesion with overhanging edge** (ขอบกระดูกยื่นแหลม) + soft tissue เป็นก้อน (lumpy, tophi)

[[fig:rheum-04-01-f2]]

> ข้อสอบชอบ: **uric acid ปกติระหว่าง attack** ไม่ตัด gout · ข้อเดียวเฉียบพลันมีไข้ → เจาะข้อแยก septic ก่อนเสมอ
''',
    figs=[F_PROG, F_CRY],
    pearls=[
        "Hyperuricemia: ชาย > 7, หญิง > 6 mg/dL · ยา PZA, ASA, furosemide, thiazide ลดการขับ",
        "Podagra = 1st MTP · acute mono/oligoarthritis ขา ± ไข้ต่ำ",
        "MSU = needle, negative birefringent (ขนานเหลือง ตั้งฉากฟ้า)",
        "Uric acid อาจปกติ/ต่ำระหว่าง attack",
        "X-ray chronic gout: punched-out lesion with overhanging edge + tophi",
    ],
    items=[
        mcq("RHEUM-04-01-1",
            "A 45-year-old man presents with pain, swelling, and tenderness of the right ankle. The ankle shows a positive ballottement sign. CBC: WBC 18,000/mm3. Synovial fluid: WBC 20,900/mm3 (PMN 90%); microscopy shows needle-shaped, strongly negatively birefringent crystals and no organisms on Gram stain. Serum uric acid is 4.5 mg/dL. What is the most likely diagnosis?",
            "Gouty arthritis",
            ["Osteoarthritis", "Reactive arthritis", "Calcium pyrophosphate deposition disease", "Septic arthritis"],
            kind="old", src=OLD,
            explain='''**ผลึกรูปเข็ม negatively birefringent** = MSU = **gout** แม้ **uric acid 4.5** ก็ไม่ตัด เพราะระดับ uric acid **ลดลงได้ระหว่าง attack** (สไลด์หน้า 71) · WBC น้ำไขข้อ 20,900 อยู่ในกลุ่ม inflammatory
- OA น้ำไขข้อเป็น non-inflammatory (< 2,000) ไม่มีผลึก
- Reactive arthritis น้ำไขข้อ inflammatory แต่ไม่มีผลึก และต้องมีประวัติติดเชื้อนำมา
- CPPD ผลึกเป็น rhomboid และ weakly **positive** birefringent
- Septic arthritis มักมี WBC > 50,000 และ Gram stain/culture บวก — ข้อนี้ Gram stain ลบและพบผลึกชัด''',
            pearl="Needle + negative birefringent = gout แม้ uric acid ปกติ", topic="Gout diagnosis",
            ref=[f"{D} หน้า 71, 82–83"], nl=["2.3.13(2)", "B5.3(3)"]),
        mcq("RHEUM-04-01-2",
            "A 50-year-old man has had recurrent swelling and tenderness of the right knee and the base of the right first toe for several years. Arthrocentesis shows WBC 20,000/mm3 with intracellular needle-shaped crystals. What is the most likely finding on radiograph of the feet?",
            "Lumpy soft-tissue densities with punched-out erosions",
            ["Generalized osteoporosis", "Osteophytes at the first MTP joint", "Chondrocalcinosis", "Bony ankylosis"],
            kind="old", src=OLD,
            explain='''Gout ที่เป็นซ้ำหลายปี → **tophi เป็นก้อน soft tissue (lumpy soft tissue)** และ **punched-out erosion ที่มี overhanging edge** (สไลด์หน้า 72, 84–85 เฉลย lumpy soft tissue)
- Osteoporosis ทั่วไปไม่ใช่ลักษณะของ gout (gout มักไม่มี osteopenia รอบข้อแบบ RA)
- Osteophyte เป็นลักษณะของ OA
- Chondrocalcinosis เป็นลักษณะของ CPPD
- Bony ankylosis เป็นลักษณะของ AS หรือข้ออักเสบระยะท้ายที่ข้อเชื่อมติดกัน''',
            pearl="Chronic gout X-ray: tophi (lumpy soft tissue) + punched-out with overhanging edge", topic="Gout X-ray",
            ref=[f"{D} หน้า 72, 84–85"], nl=["2.3.13(2)", "3.2.5"]),
        mcq("RHEUM-04-01-3",
            "A 62-year-old man with pulmonary tuberculosis has been taking isoniazid, rifampicin, pyrazinamide, and ethambutol for 6 weeks. He develops acute pain and swelling of the left first MTP joint. Serum uric acid is 11.2 mg/dL. Which drug is most likely responsible for his hyperuricemia?",
            "Pyrazinamide",
            ["Isoniazid", "Rifampicin", "Ethambutol", "Vitamin B6"],
            explain='''**Pyrazinamide** ลดการขับ uric acid ทางไต → hyperuricemia และ gout (สไลด์หน้า 67) · ethambutol ทำได้เล็กน้อยแต่ไม่เด่นเท่า (เสริม)
- Isoniazid ทำให้ peripheral neuropathy ตับอักเสบ และ drug-induced lupus
- Rifampicin ทำให้ปัสสาวะสีส้ม ตับอักเสบ และ enzyme induction
- Ethambutol ทำให้ optic neuritis (ตาบอดสี) เป็นผลหลัก ส่วนผลต่อ uric acid น้อยกว่า pyrazinamide มาก
- Vitamin B6 ให้ป้องกัน neuropathy จาก isoniazid ไม่ทำให้ uric acid สูง''',
            pearl="ยาลดการขับ uric acid: PZA, ASA ขนาดต่ำ, furosemide, thiazide", topic="Drug-induced hyperuricemia",
            ref=[f"{D} หน้า 67"], nl=["B5.2.5(1)", "B5.3(4)"]),
        mcq("RHEUM-04-01-4",
            "A 55-year-old man presents with a hot, swollen right knee for 1 day and a temperature of 38.4°C. He has a history of gout in the first MTP joint. What is the most appropriate next step?",
            "Arthrocentesis with Gram stain, culture, and crystal analysis",
            ["Start colchicine and observe", "Measure serum uric acid", "Plain radiograph of the knee", "Start allopurinol"],
            explain='''ข้อเดียวเฉียบพลันมีไข้ แม้เคยเป็น gout ก็ต้อง **R/O septic arthritis** ด้วย **arthrocentesis** (gold standard ของ gout และจำเป็นเมื่อสงสัย septic — สไลด์หน้า 71) · gout กับ septic เกิดพร้อมกันได้
- ให้ colchicine โดยไม่เจาะข้อ เสี่ยงพลาด septic arthritis ที่ทำลายข้อในไม่กี่วัน
- Serum uric acid อาจปกติระหว่าง attack และไม่แยก septic
- X-ray ระยะแรกปกติหรือเห็นแค่ soft tissue swelling
- Allopurinol ไม่ใช่ยาช่วงเฉียบพลันและไม่ช่วยวินิจฉัย''',
            pearl="Acute monoarthritis + ไข้ → arthrocentesis เสมอ", topic="Gout vs septic",
            ref=[f"{D} หน้า 71"], nl=["B5.3(3)", "2.3.13(2)"]),
    ])

# ---------------------------------------------------------------- 04-02 Acute gout treatment
S2 = sec("rheum-04-02", "Acute gout attack: การรักษาและการเลือกยาตามโรคร่วม",
    "Colchicine (ปรับตาม CrCl ห้ามใน dialysis) · NSAID (ระวัง CKD, PU, HF) · steroid PO/IA (ระวัง infection, DM) · พักข้อ ประคบเย็น · ห้ามเริ่ม/หยุด ULT ระหว่าง attack", minutes=8,
    source=f"{D} หน้า 73–74, 94–99", nl=["2.3.13(2)", "B5.4(4)", "B5.4(1)"],
    md='''
### ยาระงับการอักเสบ (สไลด์หน้า 73–74)

| ยา | ขนาด (สไลด์) | ข้อห้าม/ระวัง | Drug interaction |
|---|---|---|---|
| **NSAID** | indomethacin 50 mg tid · naproxen 500 mg bid | **severe HF, peptic ulcer, GI bleed, NSAID/aspirin-induced asthma, renal impairment** | warfarin |
| **Colchicine** | 0.6 mg tid (**ปรับตาม CrCl**) | **ห้ามในผู้ป่วยฟอกไต (dialysis)** · ระวังไต/ตับ-ทางเดินน้ำดีบกพร่อง · SE: **คลื่นไส้ อาเจียน ท้องเสีย** | **cyclosporine, statin, macrolide** (ยับยั้ง CYP3A4/P-gp → พิษ colchicine) |
| **Corticosteroid** | prednisone 20–40 mg/d · **intra-articular methylprednisolone 20–40 mg** (1–2 ข้อ) | **ติดเชื้อ**, **เบาหวานคุมไม่ได้** | — |

- ร่วมกับ: **พักข้อ ประคบเย็น (ice pack)**
- **ULT** เริ่มเมื่อมี indication (หมวดถัดไป)
- ขนาด colchicine แบบ low-dose ที่ใช้ปัจจุบัน (เสริม): 1.2 mg ทันที แล้ว 0.6 mg อีก 1 ชั่วโมง (รวม 1.8 mg) ภายใน 12–36 ชั่วโมงแรก ได้ผลเท่าขนาดสูงแต่ท้องเสียน้อยกว่า

### หลักเลือกยาตามโรคร่วม

| ผู้ป่วย | ยาที่เหมาะ | หลีกเลี่ยง |
|---|---|---|
| ไตปกติ ไม่มีโรคร่วม | colchicine, NSAID หรือ steroid ได้ทั้งหมด | — |
| **CKD รุนแรง / ESRD / dialysis** | **prednisolone** (หรือ IA steroid) | colchicine, NSAID |
| Peptic ulcer, HF, ใช้ warfarin | colchicine หรือ steroid | NSAID |
| เบาหวานคุมไม่ได้, สงสัยติดเชื้อ | colchicine หรือ NSAID | steroid |
| เป็น 1–2 ข้อ | **IA steroid** (หลัง R/O septic) | — |

> **ห้ามเริ่ม ULT ใหม่เพื่อรักษา attack** (ไม่ลดปวด) · ถ้ากิน allopurinol อยู่แล้ว **ให้กินต่อ ห้ามหยุด** ระหว่าง attack (เสริม)
> AKI ระหว่างรักษา gout: หยุด NSAID (diclofenac), ACEI (K สูง), thiazide (Na ต่ำ + uric acid สูง), metformin (เสี่ยง lactic acidosis) — ยาที่ไม่ต้องหยุดคือ antibiotic ที่ไม่พิษต่อไต เช่น ceftriaxone (สไลด์หน้า 98–99)
''',
    pearls=[
        "Acute gout: colchicine, NSAID, steroid — เลือกตามโรคร่วม",
        "ESRD/dialysis → prednisolone (colchicine ห้ามใน dialysis, NSAID ห้ามในไตวาย)",
        "Colchicine SE: ท้องเสีย · interaction: cyclosporine, statin, macrolide",
        "IA steroid เมื่อเป็น 1–2 ข้อ · steroid ระวัง infection และ DM คุมไม่ได้",
        "อย่าเริ่ม ULT เพื่อลดปวด · ถ้ากินอยู่แล้วให้กินต่อ",
    ],
    items=[
        mcq("RHEUM-04-02-1",
            "A 40-year-old man presents with redness, swelling, and tenderness at the base of the left first toe for 2 days. Arthrocentesis was attempted but failed. Serum uric acid is 6 mg/dL. He has normal renal function and no other medical illness. What is the most appropriate initial management?",
            "Colchicine",
            ["Tramadol", "Antibiotics", "Allopurinol", "Topical NSAIDs"],
            kind="old", src=OLD,
            explain='''**Podagra** ในชายวัยกลางคน (ไม่มีไข้) = acute gout ทางคลินิก แม้เจาะข้อไม่ได้และ uric acid 6 (ลดได้ระหว่าง attack) → รักษาด้วย **colchicine** (สไลด์เฉลย colchicine) · prednisolone หรือ NSAID ชนิดกินก็ใช้ได้เท่ากันในคนไตปกติ
- Tramadol เป็นยาแก้ปวดที่ไม่ลดการอักเสบ
- Antibiotics ไม่จำเป็นถ้าภาพไม่เข้ากับ septic (ไม่มีไข้ ตำแหน่ง 1st MTP คลาสสิก)
- Allopurinol เป็น ULT ไม่ใช้รักษา attack และอาจทำให้กำเริบมากขึ้นถ้าเริ่มโดยไม่มียาคุมการอักเสบ
- Topical NSAID ไม่มีฤทธิ์พอสำหรับ acute gout''',
            pearl="Podagra ไตปกติ → colchicine/NSAID/steroid ชนิดกิน", topic="Acute gout Tx",
            ref=[f"{D} หน้า 73, 94–95"], nl=["2.3.13(2)", "B5.4(4)"]),
        mcq("RHEUM-04-02-2",
            "An elderly man with end-stage renal disease on maintenance hemodialysis is diagnosed with an acute gout attack of the right knee. Septic arthritis has been excluded. What is the most appropriate drug?",
            "Prednisolone",
            ["Colchicine", "Allopurinol", "Probenecid", "Naproxen"],
            kind="old", src=OLD,
            explain='''**ESRD/dialysis** → ยาที่ปลอดภัยคือ **corticosteroid (prednisolone หรือ IA steroid)** (สไลด์เฉลย prednisolone)
- Colchicine **ห้ามในผู้ป่วยฟอกไต** (ขับออกไม่ได้และถูกฟอกออกไม่ได้ → พิษต่อกล้ามเนื้อ ประสาท ไขกระดูก)
- Allopurinol เป็น ULT ไม่รักษา attack
- Probenecid ไม่ได้ผลเมื่อไตเสื่อมรุนแรงและไม่รักษา attack
- NSAID (naproxen) ห้ามในไตวาย และทำลายไตที่เหลือ''',
            pearl="Gout + ESRD/dialysis → prednisolone", topic="Acute gout CKD",
            ref=[f"{D} หน้า 73–74, 96–97"], nl=["B5.4(4)", "B11.4(3)"]),
        mcq("RHEUM-04-02-3",
            "A 60-year-old man with diabetes and hypertension is treated for infectious diarrhea with ceftriaxone. His other medications are enalapril, hydrochlorothiazide, and metformin. He then develops an acute gout attack and receives diclofenac. Three days later: creatinine 3.5 mg/dL, Na 132 mmol/L, K 5.8 mmol/L, HCO3 15 mmol/L. Which drug can be continued?",
            "Ceftriaxone",
            ["Enalapril", "Hydrochlorothiazide", "Metformin", "Diclofenac"],
            kind="old", src=OLD,
            explain='''ผู้ป่วยมี **AKI + K สูง + Na ต่ำ + metabolic acidosis** → ต้องหยุดยาที่ซ้ำเติม เหลือ **ceftriaxone** ซึ่งรักษาการติดเชื้อที่เป็นอยู่ ไม่พิษต่อไต และขับทางน้ำดีได้ (ไม่ต้องปรับขนาดตามไต — เสริม)
- Enalapril (ACEI) ลด GFR ในภาวะขาดน้ำ และทำให้ **K สูง**
- Hydrochlorothiazide ทำให้ **Na ต่ำ** และ **uric acid สูง กระตุ้น gout**
- Metformin เมื่อเกิด **AKI** เสี่ยง **metformin-associated lactic acidosis** (HCO3 15)
- Diclofenac (NSAID) ทำให้ **AKI** โดยเฉพาะร่วมกับ ACEI + diuretic (triple whammy — เสริม)''',
            pearl="AKI ในผู้ป่วย gout: หยุด NSAID, ACEI, thiazide, metformin", topic="Drug safety in gout",
            ref=[f"{D} หน้า 98–99"], nl=["B5.4(1)", "B5.4(4)"]),
        mcq("RHEUM-04-02-4",
            "A 58-year-old man with acute gout of the left ankle is started on colchicine. He also takes simvastatin and was recently prescribed clarithromycin for pneumonia. Three days later he has severe diarrhea, muscle weakness, and CK of 4,800 U/L. What is the most likely explanation?",
            "Colchicine toxicity due to drug interaction with clarithromycin",
            ["Gout flare involving the proximal muscles", "Clostridioides difficile colitis alone", "Polymyositis triggered by infection", "Hypokalemic periodic paralysis"],
            explain='''Colchicine มี **drug interaction กับ macrolide, statin, cyclosporine** (สไลด์หน้า 74) — clarithromycin ยับยั้ง CYP3A4/P-gp → ระดับ colchicine สูง → **ท้องเสียรุนแรง + myopathy/rhabdomyolysis** (ซ้ำเติมด้วย statin)
- Gout ไม่ทำให้กล้ามเนื้ออ่อนแรงและ CK สูง
- C. difficile colitis อธิบายท้องเสียได้ แต่ไม่อธิบาย CK สูงและกล้ามเนื้ออ่อนแรง
- Polymyositis เป็นช้า ๆ หลายสัปดาห์ ไม่ใช่ใน 3 วันหลังเริ่มยา
- Hypokalemic periodic paralysis ทำให้อ่อนแรง แต่ CK ไม่สูงมากและไม่มีท้องเสียรุนแรงแบบนี้''',
            pearl="Colchicine + macrolide/statin/cyclosporine → พิษ (ท้องเสีย myopathy)", topic="Colchicine interaction",
            ref=[f"{D} หน้า 74"], nl=["B5.4(4)"]),
    ])

# ---------------------------------------------------------------- 04-03 ULT
F_ULT = fig("rheum-04-03-f1", "เมื่อไหร่ควรเริ่ม ULT และเริ่มอย่างไร", '''<svg viewBox="0 0 740 400">
 <defs><marker id="rheum-04-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="230" height="120" rx="10" class="badsoft"/>
 <text x="22" y="32" class="tb">Absolute indication</text>
 <text x="22" y="56" class="t2">• มี tophi</text>
 <text x="22" y="78" class="t2">• X-ray เห็นข้อถูกทำลาย</text>
 <text x="22" y="100" class="t2">• attack ≥ 2 ครั้ง/ปี</text>
 <rect x="255" y="10" width="230" height="120" rx="10" class="misssoft"/>
 <text x="267" y="32" class="tb">Relative indication</text>
 <text x="267" y="56" class="t2">• attack ≥ 1 แต่ &lt; 2 ครั้ง/ปี</text>
 <text x="267" y="78" class="t2">• attack ครั้งแรก + นิ่วไต</text>
 <text x="267" y="100" class="t2">  หรือ CKD ≥ 3 หรือ UA &gt; 9</text>
 <rect x="500" y="10" width="230" height="120" rx="10" class="oksoft"/>
 <text x="512" y="32" class="tb">ไม่ให้ ULT</text>
 <text x="512" y="56" class="t2">Asymptomatic hyperuricemia</text>
 <text x="512" y="80" class="t3">→ LSM: ลดเหล้า purine fructose</text>
 <text x="512" y="98" class="t3">ลดน้ำหนัก · เปลี่ยน thiazide/</text>
 <text x="512" y="116" class="t3">furosemide → losartan/amlodipine</text>
 <path d="M125 130V160L300 172" class="ln" marker-end="url(#rheum-04-03-a)"/>
 <path d="M370 130V170" class="ln" marker-end="url(#rheum-04-03-a)"/>
 <rect x="150" y="174" width="440" height="40" rx="10" class="ac"/>
 <text x="370" y="199" text-anchor="middle" class="tw">เริ่ม ULT แบบ start low, go slow · เป้าหมาย UA &lt; 6 mg/dL</text>
 <path d="M80 300H720" class="ln" marker-end="url(#rheum-04-03-a)"/>
 <text x="80" y="320" text-anchor="middle" class="t3">เริ่ม</text>
 <text x="280" y="320" text-anchor="middle" class="t3">3 เดือน</text>
 <text x="480" y="320" text-anchor="middle" class="t3">6 เดือน</text>
 <text x="700" y="320" text-anchor="end" class="t3">ต่อเนื่องตลอดชีวิต</text>
 <rect x="80" y="232" width="400" height="26" rx="6" class="miss"/>
 <text x="280" y="250" text-anchor="middle" class="tw">Prophylaxis: low-dose colchicine / NSAID / pred 3–6 เดือน</text>
 <rect x="80" y="266" width="620" height="26" rx="6" class="ok"/>
 <text x="390" y="284" text-anchor="middle" class="tw">XOI 1st line: allopurinol (ตรวจ HLA-B5801) หรือ febuxostat · 2nd: probenecid</text>
 <rect x="10" y="340" width="720" height="50" rx="10" class="sunk"/>
 <text x="370" y="360" text-anchor="middle" class="t2">ทำไมต้อง prophylaxis: ช่วงแรก uric acid ลดลงเร็ว ผลึกเดิมละลายหลุดออก → กระตุ้น attack ได้</text>
 <text x="370" y="380" text-anchor="middle" class="t2">ถ้าเกิด attack ระหว่าง ULT → รักษา attack และกิน ULT ต่อ ไม่หยุด</text>
</svg>''', "แถวบนคือการตัดสินใจเริ่ม ULT · แถบเวลาด้านล่างแสดงว่าต้องให้ยากันกำเริบคู่กับ ULT ช่วง 3–6 เดือนแรก ส่วน ULT ให้ต่อเนื่อง")

S3 = sec("rheum-04-03", "Urate-lowering therapy (ULT) และ chronic gout",
    "Absolute: tophi, X-ray damage, ≥ 2 attacks/ปี · relative: 1st attack + นิ่ว/CKD ≥ 3/UA > 9 · ไม่ให้ใน asymptomatic hyperuricemia · XOI 1st (allopurinol C/I HLA-B5801, febuxostat C/I CVD) · probenecid 2nd · prophylaxis 3–6 เดือน · goal < 6 · LSM + losartan/amlodipine", minutes=10,
    source=f"{D} หน้า 75–77, 86–93", nl=["B5.4(4)", "2.3.13(2)", "B5.3(4)"],
    md='''
### ข้อบ่งชี้ของ ULT (สไลด์หน้า 75)

| ระดับ | เกณฑ์ |
|---|---|
| **Absolute** | **tophi** · **radiographic joint damage** · **attack ≥ 2 ครั้ง/ปี** |
| **Relative** | attack ≥ 1 แต่ < 2 ครั้ง/ปี · **attack ครั้งแรก + (นิ่วไต หรือ CKD stage ≥ 3 หรือ uric acid > 9 mg/dL)** |
| **ไม่แนะนำ** | **asymptomatic hyperuricemia** → แก้ปัจจัยเสี่ยง/LSM แทน |

### ยา ULT (สไลด์หน้า 76)

| กลุ่ม | ยา | กลไก | ข้อห้าม/ระวัง |
|---|---|---|---|
| **Xanthine oxidase inhibitor (1st line)** | **Allopurinol** | ลดการสร้าง uric acid | **HLA-B5801 บวก** (เสี่ยง SJS/TEN/DRESS — คนไทยพบบ่อย ควรตรวจก่อนเริ่ม) |
| | **Febuxostat** | ลดการสร้าง | **โรคหัวใจและหลอดเลือด (CVD)** |
| **Uricosuric (2nd line)** | **Probenecid** (benzbromarone — เสริม) | เพิ่มการขับทางไต | **CKD รุนแรง, นิ่วไต** |

- **Anti-inflammatory prophylaxis ก่อน/พร้อมเริ่ม ULT**: **low-dose colchicine, NSAID หรือ prednisolone** นาน **3–6 เดือน** หรือจนถึงเป้าหมาย uric acid
- **Goal uric acid < 6 mg/dL** (มี tophi ให้ < 5 — เสริม)
- **ULT ช่วงแรก trigger acute gout attack ได้** (ผลึกละลายหลุด)
- วิธีให้ allopurinol (เสริม): เริ่ม **100 mg/วัน** (CKD stage 4 ขึ้นไปเริ่ม ≤ 50 mg/วัน) แล้วเพิ่มทีละ 100 mg ทุก 2–4 สัปดาห์จนถึงเป้า

[[fig:rheum-04-03-f1]]

### Lifestyle modification (สไลด์หน้า 77)
- **ลด alcohol** (โดยเฉพาะเบียร์ สุรา)
- **ลด purine**: **เครื่องใน เนื้อแดง seafood**
- **ลด high-fructose syrup** (ขนมหวาน น้ำผลไม้ น้ำอัดลม)
- **ลดน้ำหนัก** · รักษาโรคร่วม (HT, DM)
- **ยาลดความดัน: หลีกเลี่ยง HCTZ, furosemide** → **ใช้ losartan** (ขับ uric acid เพิ่มเล็กน้อย) **หรือ amlodipine** แทน

> โจทย์ hyperuricemia ไม่มีอาการ: คำตอบคือ **แก้สาเหตุ** — เลิกเหล้า · เปลี่ยน thiazide เป็น losartan · หยุด furosemide ที่ไม่จำเป็น — **ไม่ใช่ allopurinol** (ยกเว้นมีนิ่ว/UA สูงมาก ตามเฉลยสไลด์ข้อ UA 11 + นิ่ว)
''',
    figs=[F_ULT],
    pearls=[
        "ULT absolute: tophi, X-ray damage, attack ≥ 2/ปี",
        "Asymptomatic hyperuricemia → ไม่ให้ ULT · แก้เหล้า ยา อาหาร",
        "Allopurinol 1st line — ตรวจ HLA-B5801 ก่อน · febuxostat ห้ามใน CVD · probenecid ห้ามใน CKD/นิ่ว",
        "เริ่ม ULT ต้องให้ low-dose colchicine/NSAID/pred 3–6 เดือน · goal UA < 6",
        "HT + gout: เลี่ยง HCTZ/furosemide ใช้ losartan หรือ amlodipine",
    ],
    items=[
        mcq("RHEUM-04-03-1",
            "A 55-year-old man is found to have a serum uric acid of 10 mg/dL. He has no history of joint pain or flank pain. He has hypertension treated with amlodipine and is a heavy alcohol drinker. Examination shows no arthritis or tophi. Creatinine is 0.8 mg/dL. What is the most appropriate management?",
            "Advise alcohol cessation",
            ["Add colchicine", "Add allopurinol", "Advise a high-carbohydrate diet", "Switch amlodipine to hydrochlorothiazide"],
            kind="old", src=OLD,
            explain='''**Asymptomatic hyperuricemia** → **ไม่ให้ ULT** แต่แก้สาเหตุที่แก้ได้ คือ **alcohol** ซึ่งเพิ่มการสร้างและลดการขับ uric acid (สไลด์หน้า 75, 77)
- Colchicine ใช้รักษาหรือป้องกัน attack ผู้ป่วยไม่เคยมี attack
- Allopurinol ไม่แนะนำใน asymptomatic hyperuricemia
- อาหารคาร์โบไฮเดรตสูง (โดยเฉพาะ fructose) ทำให้ uric acid สูงขึ้น
- HCTZ เพิ่ม uric acid — amlodipine ดีอยู่แล้ว''',
            pearl="Asymptomatic hyperuricemia + เหล้า → เลิกเหล้า ไม่ให้ allopurinol", topic="Asymptomatic hyperuricemia",
            ref=[f"{D} หน้า 75, 77, 86–87"], nl=["B5.3(4)", "2.3.13(2)"]),
        mcq("RHEUM-04-03-2",
            "A 60-year-old man comes for follow-up of hypertension, well controlled on hydrochlorothiazide. He is a low-risk alcohol drinker and has no history of joint pain or urinary stones. BMI is 24 kg/m2 and BP is 130/75 mmHg. There is no arthritis or tophi. Creatinine is 0.8 mg/dL and uric acid is 10 mg/dL. What is the most appropriate management?",
            "Switch hydrochlorothiazide to losartan",
            ["Start allopurinol", "Start colchicine", "Continue current medication and monitor", "Advise weight reduction"],
            kind="old", src=OLD,
            explain='''สาเหตุที่แก้ได้ของ hyperuricemia ในคนนี้คือ **thiazide** (ลดการขับ uric acid) → เปลี่ยนเป็น **losartan** ซึ่งคุมความดันได้และช่วยขับ uric acid (สไลด์หน้า 77, 88–89)
- Allopurinol ไม่แนะนำใน asymptomatic hyperuricemia
- Colchicine ไม่มีบทบาทเมื่อไม่มี attack
- ใช้ยาเดิมต่อไปทั้งที่มีสาเหตุที่แก้ได้ไม่ใช่คำตอบที่ดีที่สุด
- BMI 24 ปกติ ไม่ต้องลดน้ำหนัก''',
            pearl="Hyperuricemia จาก thiazide → เปลี่ยนเป็น losartan", topic="Antihypertensive in gout",
            ref=[f"{D} หน้า 77, 88–89"], nl=["B5.3(4)"]),
        mcq("RHEUM-04-03-3",
            "A 70-year-old man with well-controlled hypertension takes amlodipine and furosemide. He has no edema or heart failure. At his annual checkup, uric acid is 11 mg/dL. He has no symptoms of arthritis. What is the most appropriate management?",
            "Discontinue furosemide",
            ["Add losartan", "Discontinue amlodipine", "Change amlodipine to losartan", "Start allopurinol"],
            kind="old", src=OLD,
            explain='''**Furosemide** เป็นยาที่ลดการขับ uric acid และไม่มีข้อบ่งชี้ (ไม่มี HF หรือบวม) → **หยุด furosemide** (สไลด์: avoid HCTZ, furosemide)
- เพิ่ม losartan ไม่ได้แก้ต้นเหตุ ยังคง furosemide อยู่
- Amlodipine เป็นยาที่สไลด์แนะนำให้ใช้ได้ ไม่ต้องหยุด
- เปลี่ยน amlodipine เป็น losartan ไม่จำเป็น เพราะตัวปัญหาคือ furosemide
- Allopurinol ไม่แนะนำใน asymptomatic hyperuricemia''',
            pearl="Hyperuricemia + furosemide ที่ไม่จำเป็น → หยุด furosemide", topic="Drug-induced hyperuricemia",
            ref=[f"{D} หน้า 77, 90–91"], nl=["B5.3(4)"]),
        mcq("RHEUM-04-03-4",
            "A 50-year-old man with hypertension on amlodipine has a serum uric acid of 11 mg/dL. He has a history of passing urinary stones and is a heavy alcohol drinker. There is no arthritis or tophi. Creatinine is 0.8 mg/dL. What is the most appropriate management?",
            "Allopurinol",
            ["Change amlodipine to enalapril", "Low-carbohydrate diet", "Colchicine", "Benzbromarone"],
            kind="old", src=OLD,
            explain='''Hyperuricemia สูงมาก (11) **ร่วมกับประวัตินิ่วไต** → สไลด์เฉลย **allopurinol** (ลดการสร้าง uric acid และลดนิ่ว uric acid) พร้อมแนะนำเลิกเหล้า
- Enalapril ไม่ได้ช่วยลด uric acid และ amlodipine เหมาะอยู่แล้ว
- อาหาร low-carb ไม่ใช่การรักษาหลัก (ที่ควรลดคือ purine, alcohol, fructose)
- Colchicine ไม่ลด uric acid
- **Benzbromarone เป็น uricosuric ห้ามในผู้ที่มีนิ่วไต** เพราะเพิ่ม uric acid ในปัสสาวะ

หมายเหตุ: แนวทาง ACR 2020 ไม่แนะนำ ULT ใน asymptomatic hyperuricemia แม้มีนิ่ว ส่วนเกณฑ์ relative indication ในสไลด์ใช้ "attack ครั้งแรก + นิ่วไต" — ข้อนี้ให้ยึดเฉลยสไลด์ (allopurinol) เพราะมีนิ่วและ UA สูงมาก''',
            pearl="นิ่วไต → เลี่ยง uricosuric ใช้ XOI (allopurinol)", topic="ULT choice",
            ref=[f"{D} หน้า 75–76, 92–93"], nl=["B5.4(4)", "2.3.14-3(15)"]),
        mcq("RHEUM-04-03-5",
            "A 52-year-old Thai man has tophaceous gout with 4 attacks in the past year. Creatinine is 1.0 mg/dL. Allopurinol is planned. Which test should be done before starting allopurinol to reduce the risk of a severe adverse drug reaction?",
            "HLA-B5801 genotyping",
            ["HLA-B27 typing", "Glucose-6-phosphate dehydrogenase level", "Thiopurine methyltransferase activity", "24-hour urine uric acid"],
            explain='''**HLA-B5801** สัมพันธ์กับ **SJS/TEN/DRESS จาก allopurinol** พบบ่อยในคนไทยและเอเชีย — สไลด์ระบุเป็นข้อห้ามของ allopurinol (หน้า 76) ถ้าบวก ใช้ febuxostat (ถ้าไม่มี CVD) หรือ probenecid แทน
- HLA-B27 เกี่ยวกับ spondyloarthropathy
- G6PD ตรวจก่อนให้ยาที่ทำให้ hemolysis เช่น primaquine, dapsone, rasburicase
- TPMT ตรวจก่อนให้ azathioprine/6-MP — ส่วน allopurinol มี interaction กับ azathioprine (เสริม)
- Urine uric acid 24 ชั่วโมงใช้ประเมินก่อนให้ uricosuric ไม่ใช่ป้องกันแพ้ยา''',
            pearl="ก่อน allopurinol → HLA-B5801 (คนไทยเสี่ยง SJS/TEN)", topic="Allopurinol safety",
            ref=[f"{D} หน้า 76"], nl=["B5.4(4)"]),
    ])

# ---------------------------------------------------------------- 04-04 CPPD
S4 = sec("rheum-04-04", "CPPD disease (pseudogout)",
    "CPP ใน articular cartilage · อายุ > 60 · idiopathic หรือ trauma, ↑PTH, hemochromatosis, ↓Mg, ↓PO4 · ข้อมือ เข่า · rhomboid weakly positive · chondrocalcinosis · colchicine NSAID steroid", minutes=6,
    source=f"{D} หน้า 78–81, 100–103", nl=["2.3.13(2)", "B5.2.5(1)", "B5.3(3)"],
    md='''
### นิยามและสาเหตุ (สไลด์หน้า 78)
- ผลึก **calcium pyrophosphate (CPP)** สะสมใน **articular cartilage** · อายุเริ่ม **> 60 ปี**
- สาเหตุ: **idiopathic (พบบ่อยสุด)** · secondary: **trauma, hyperparathyroidism (↑PTH), hemochromatosis, hypomagnesemia (↓Mg), hypophosphatemia (↓PO4)**
- ผู้ป่วยอายุน้อย (< 60) ที่เป็น CPPD → ต้องหาโรค metabolic เหล่านี้ (เสริม)

### รูปแบบทางคลินิก (สไลด์หน้า 78)

| รูปแบบ | ลักษณะ |
|---|---|
| **Asymptomatic** | เห็น chondrocalcinosis บน X-ray โดยบังเอิญ |
| **Acute CPP crystal arthritis (pseudogout)** | **acute monoarthritis** คล้าย gout · พบบ่อยที่ **ข้อมือ (wrist), เข่า** · ตัวกระตุ้น: ป่วยหนัก ผ่าตัด นอนโรงพยาบาล (เสริม) |
| **Chronic CPP crystal arthritis** | คล้าย **osteoarthritis** แต่เป็นข้อที่ OA ไม่ค่อยเป็น เช่น ข้อมือ MCP ไหล่ (เสริม) |

### Investigation (สไลด์หน้า 79)
- **Arthrocentesis: weakly positively birefringent rhomboid-shaped crystals** (**ขนานแกน = ฟ้า, ตั้งฉาก = เหลือง**) — ตรงข้ามกับ gout
- WBC **> 2,000/µL (PMN > 50%)** · **G/S และ C/S ลบ**
- **X-ray: chondrocalcinosis** (เส้นแคลเซียมในกระดูกอ่อน เช่น meniscus ของเข่า, triangular fibrocartilage ของข้อมือ)

| | Gout | CPPD |
|---|---|---|
| ผลึก | MSU รูป **เข็ม** | CPP รูป **rhomboid** |
| Birefringence | **strongly negative** | **weakly positive** |
| ขนานแกน | **เหลือง** | **ฟ้า** |
| ข้อที่ชอบ | 1st MTP, ข้อเท้า, เข่า | **ข้อมือ, เข่า** |
| อายุ | ชายวัยกลางคน | **> 60 ปี** |
| X-ray | punched-out, overhanging edge | **chondrocalcinosis** |

### การรักษา (สไลด์หน้า 81)
- **รักษาสาเหตุ** (เช่น แก้ Mg, PTH)
- Acute: **colchicine, NSAID, steroid** (ระบายน้ำไขข้อ + IA steroid ได้ผลดี — เสริม)
- **Prophylaxis: low-dose colchicine** ถ้าเป็นซ้ำบ่อย
- **ไม่มียาลดผลึก CPP** แบบ ULT ของ gout (เสริม)
''',
    pearls=[
        "CPPD = อายุ > 60 · ข้อมือ/เข่า · rhomboid weakly positive (ขนานฟ้า)",
        "X-ray chondrocalcinosis",
        "สาเหตุ secondary: trauma, ↑PTH, hemochromatosis, ↓Mg, ↓PO4",
        "รักษา: colchicine, NSAID, steroid · ป้องกันด้วย low-dose colchicine",
    ],
    items=[
        mcq("RHEUM-04-04-1",
            "An 80-year-old woman presents with tenderness and swelling of the left wrist for 2 days. Examination shows swelling and tenderness along the joint line. Synovial fluid analysis: WBC 5,000/mm3 (PMN 95%) with rhomboid-shaped crystals. What is the most likely finding on radiograph?",
            "Chondrocalcinosis",
            ["Acro-osteolysis", "Punched-out erosions", "Calcinosis cutis", "Marginal erosions"],
            kind="old", src=OLD,
            explain='''ผู้สูงอายุ + **ข้อมือ** อักเสบเฉียบพลัน + **ผลึก rhomboid** = **CPPD (pseudogout)** → X-ray เห็น **chondrocalcinosis** (สไลด์หน้า 79)
- Acro-osteolysis (ปลายกระดูกนิ้วสลาย) พบใน systemic sclerosis, psoriatic arthritis, hyperparathyroidism
- Punched-out erosion เป็นของ chronic gout
- Calcinosis cutis (แคลเซียมใต้ผิวหนัง) พบใน limited systemic sclerosis (CREST), dermatomyositis
- Marginal erosion เป็นของ RA''',
            pearl="Rhomboid crystal → X-ray chondrocalcinosis", topic="CPPD",
            ref=[f"{D} หน้า 79, 100–101"], nl=["2.3.13(2)", "3.2.5"]),
        mcq("RHEUM-04-04-2",
            "A 70-year-old woman has been admitted for congestive heart failure for 3 days. She develops tenderness and swelling of the left knee. Synovial fluid analysis shows rhomboid-shaped crystals and a negative Gram stain. What is the most appropriate management for her pain?",
            "Colchicine",
            ["Cold pack alone", "Tramadol", "Paracetamol", "COX-2 inhibitor"],
            kind="old", src=OLD,
            explain='''Acute CPP crystal arthritis (pseudogout) ซึ่งมักกระตุ้นจากการนอนโรงพยาบาลป่วยหนัก → ยาต้านการอักเสบ คือ colchicine, NSAID, steroid · ผู้ป่วยมี **heart failure** จึง **เลี่ยง NSAID/COX-2 inhibitor** (บวมน้ำ HF แย่ลง) → **colchicine** (สไลด์เฉลย)
- Cold pack ช่วยเสริมได้ แต่ใช้เดี่ยว ๆ ไม่พอ
- Tramadol และ paracetamol เป็นยาแก้ปวดที่ไม่ลดการอักเสบของผลึก
- COX-2 inhibitor ยังทำให้คั่งเกลือและน้ำ ห้ามใน HF ที่กำลังกำเริบ''',
            pearl="Pseudogout + HF → colchicine (เลี่ยง NSAID)", topic="CPPD treatment",
            ref=[f"{D} หน้า 81, 102–103"], nl=["2.3.13(2)", "B5.4(4)"]),
        mcq("RHEUM-04-04-3",
            "A 45-year-old man presents with recurrent acute arthritis of the knees. Synovial fluid shows weakly positively birefringent rhomboid crystals. He also has diabetes, skin hyperpigmentation, hepatomegaly, and arthropathy of the 2nd and 3rd MCP joints. Ferritin is 2,400 ng/mL and transferrin saturation is 78%. Which underlying disorder should be treated?",
            "Hereditary hemochromatosis",
            ["Primary hypoparathyroidism", "Hypermagnesemia", "Wilson disease", "Hyperphosphatemia"],
            explain='''CPPD ใน **คนอายุน้อย (< 60)** ต้องหาสาเหตุ secondary · **เบาหวาน + ผิวคล้ำ + ตับโต + MCP 2–3 + ferritin และ transferrin saturation สูง** = **hemochromatosis** (สไลด์ระบุเป็นสาเหตุ CPPD) → รักษาด้วย phlebotomy (เสริม)
- สาเหตุของ CPPD คือ **hyper**parathyroidism ไม่ใช่ hypoparathyroidism
- สาเหตุคือ **hypo**magnesemia ไม่ใช่ hypermagnesemia
- Wilson disease สะสมทองแดง ไม่ใช่เหล็ก (ferritin ไม่สูงแบบนี้)
- สาเหตุคือ **hypo**phosphatemia ไม่ใช่ hyperphosphatemia''',
            pearl="CPPD อายุน้อย → หา hemochromatosis, ↑PTH, ↓Mg, ↓PO4", topic="Secondary CPPD",
            ref=[f"{D} หน้า 78"], nl=["B5.2.5(1)"]),
    ])

LECTURE = lecture("04", "Crystal-induced arthritis", "hyperuricemia · acute gout · urate-lowering therapy · CPPD",
    objectives=[
        "บอกสาเหตุของ hyperuricemia และวินิจฉัย acute/chronic gout จากอาการ ผลึก และ X-ray",
        "เลือกยา acute gout ให้เหมาะกับโรคร่วม (CKD, PU, HF, DM) และรู้ interaction ของ colchicine",
        "ตัดสินใจเริ่ม ULT ตาม indication รู้ข้อห้ามของ allopurinol, febuxostat, probenecid และเป้าหมาย UA < 6",
        "จัดการ asymptomatic hyperuricemia ด้วย LSM และการเปลี่ยนยาลดความดัน",
        "แยก CPPD จาก gout ด้วยผลึกและ X-ray และรักษาได้",
    ],
    sections=[S1, S2, S3, S4])
