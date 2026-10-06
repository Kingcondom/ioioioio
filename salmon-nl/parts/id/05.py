from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Infectious"

# ---------------------------------------------------------------- 05-01 Rabies
F_PEP = fig("id-05-01-f1", "Rabies PEP: จะฉีดอะไรหลังถูกสัตว์กัด", '''<svg viewBox="0 0 740 470">
 <defs><marker id="id-05-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="230" height="74" rx="10" class="oksoft"/>
 <text x="125" y="34" text-anchor="middle" class="tb">CAT 1</text>
 <text x="125" y="54" text-anchor="middle" class="t3">เลีย/สัมผัส ผิวหนังปกติ</text>
 <text x="125" y="72" text-anchor="middle" class="tb">ไม่ต้องฉีด</text>
 <rect x="255" y="10" width="230" height="74" rx="10" class="misssoft"/>
 <text x="370" y="34" text-anchor="middle" class="tb">CAT 2</text>
 <text x="370" y="54" text-anchor="middle" class="t3">งับเป็นรอยช้ำ ถลอก ข่วน เลือดซิบ</text>
 <text x="370" y="72" text-anchor="middle" class="t3">กินเนื้อสัตว์สงสัยดิบ</text>
 <rect x="500" y="10" width="230" height="74" rx="10" class="badsoft"/>
 <text x="615" y="34" text-anchor="middle" class="tb">CAT 3</text>
 <text x="615" y="54" text-anchor="middle" class="t3">ทะลุผิว เลือดออกชัด · น้ำลายโดน</text>
 <text x="615" y="72" text-anchor="middle" class="t3">เยื่อบุ/แผลเปิด · ค้างคาว</text>
 <path d="M370 84V108" class="ln" marker-end="url(#id-05-01-a)"/>
 <path d="M615 84V96H440V108" class="ln" marker-end="url(#id-05-01-a)"/>
 <rect x="200" y="110" width="340" height="40" rx="10" class="acsoft"/>
 <text x="370" y="135" text-anchor="middle" class="tb">ล้างแผล NSS/สบู่ทันที + ประเมินสัตว์</text>
 <path d="M280 150L150 182" class="ln" marker-end="url(#id-05-01-a)"/>
 <path d="M460 150L590 182" class="ln" marker-end="url(#id-05-01-a)"/>
 <rect x="10" y="184" width="300" height="96" rx="10" class="box"/>
 <text x="160" y="206" text-anchor="middle" class="tb">สัตว์ตาย / ฆ่าได้</text>
 <text x="22" y="230" class="t2">ส่งตรวจสมองสัตว์ (เริ่ม PEP ไปก่อน)</text>
 <text x="22" y="252" class="t2">Positive → ฉีดต่อให้ครบ</text>
 <text x="22" y="272" class="t2">Negative → หยุดได้</text>
 <rect x="330" y="184" width="400" height="96" rx="10" class="box"/>
 <text x="530" y="206" text-anchor="middle" class="tb">สัตว์ยังมีชีวิต — ครบทั้ง 3 ข้อไหม?</text>
 <text x="342" y="230" class="t3">1 เลี้ยงอย่างดี กักขังบริเวณ</text>
 <text x="342" y="250" class="t3">2 ฉีดวัคซีน ≥ 2 เข็ม เข็มล่าสุด &lt; 1 ปี</text>
 <text x="342" y="270" class="t3">3 มีเหตุจูงใจ (แหย่/รังแกสัตว์)</text>
 <path d="M440 280L360 312" class="ln" marker-end="url(#id-05-01-a)"/>
 <path d="M620 280L660 312" class="ln" marker-end="url(#id-05-01-a)"/>
 <rect x="230" y="314" width="250" height="44" rx="10" class="ok"/>
 <text x="355" y="333" text-anchor="middle" class="tw">ครบ 3 ข้อ → กักดูสัตว์ 10 วัน</text>
 <text x="355" y="350" text-anchor="middle" class="tw">ปกติ → ไม่ต้องฉีด</text>
 <rect x="500" y="314" width="230" height="44" rx="10" class="bad"/>
 <text x="615" y="341" text-anchor="middle" class="tw">ไม่ครบ → ให้ PEP</text>
 <rect x="10" y="372" width="355" height="90" rx="10" class="c1soft"/>
 <text x="22" y="394" class="tb">ไม่เคยฉีดวัคซีน</text>
 <text x="22" y="416" class="t2">CAT 2: vaccine D0, 3, 7, 14, 28</text>
 <text x="22" y="438" class="t2">CAT 3: vaccine ชุดเดียวกัน + RIG</text>
 <text x="22" y="456" class="t3">(RIG แทรกรอบแผลให้มากที่สุด)</text>
 <rect x="375" y="372" width="355" height="90" rx="10" class="c2soft"/>
 <text x="387" y="394" class="tb">เคยฉีดครบมาแล้ว (CAT 2/3)</text>
 <text x="387" y="416" class="t2">เข็มสุดท้าย &lt; 6 เดือน: 1 เข็ม D0</text>
 <text x="387" y="438" class="t2">เข็มสุดท้าย &gt; 6 เดือน: 2 เข็ม D0, 3</text>
 <text x="387" y="456" class="t3">ไม่ต้องให้ RIG</text>
</svg>''', "จัด category ก่อน → ล้างแผลและประเมินสัตว์ → ถ้าต้องให้ PEP ดูว่าเคยฉีดวัคซีนหรือไม่ (ตามสไลด์หน้า 172–175)")

S1 = sec("id-05-01", "Rabies & animal bite wound",
    "Hydrophobia + hypersalivation + agitation = rabies ตายเกือบ 100% · CAT 1/2/3 · ล้างแผล ไม่เย็บทันที · amoxicillin prophylaxis · PEP D0 3 7 14 28 + RIG ใน CAT 3",
    minutes=9, source=f"{D} หน้า 171–179", nl=["2.3.1-3(1)", "2.3.18(1)", "2.2.45"],
    md='''
### เชื้อและอาการ

- **Rabies virus** (lyssavirus) · ติดจาก **การกัด/ข่วน/น้ำลายของสัตว์เลี้ยงลูกด้วยนม** — **สุนัขพบบ่อยที่สุด** (แมว ค้างคาว)
- Prodrome: **flu-like**, **ปวด/ชา (paresthesia) ที่ตำแหน่งแผล**
- Furious (encephalitic): **hydrophobia** (pharyngeal muscle spasm เจ็บเวลากลืน → กลัวน้ำ) · aerophobia · **hypersalivation** (น้ำลายไหล) · agitation, confusion, **อาการเป็นพัก ๆ (fluctuating)**, seizure · hypertonia, hyperreflexia
- Paralytic (dumb) rabies: อ่อนแรงแบบ ascending คล้าย GBS (เสริม)
- **เกือบทั้งหมดเสียชีวิต** เมื่อมีอาการแล้ว

### Investigation

- Direct fluorescent antibody (DFA), **PCR** จาก serum, **saliva, CSF, hair follicles (nuchal skin biopsy)**

### Management

- เมื่อมีอาการแล้ว: **palliative care** (ห้องแยก ยากล่อมประสาท)
- **Prevention** สำคัญที่สุด: pre-exposure prophylaxis (PrEP) ในกลุ่มเสี่ยง · **post-exposure prophylaxis (PEP)** · วัคซีนในสัตว์

### Animal bite: แบ่ง category

| Category | ลักษณะ |
|---|---|
| **CAT 1** | **ถูกเลียผิวหนังปกติ** ไม่มีแผล/รอยข่วน |
| **CAT 2** | **งับเป็นรอยช้ำ แผลถลอก รอยข่วน ไม่มีเลือดออกหรือเลือดซิบ ๆ** · **กินเนื้อสัตว์ที่สงสัยเป็นโรคที่ปรุงไม่สุก** |
| **CAT 3** | **กัด/ข่วนทะลุผิวหนัง มีเลือดออกชัด** · **น้ำลายสัตว์ถูกเยื่อบุ** (ตา จมูก ปาก ทวาร อวัยวะเพศ) หรือแผลเปิด · **ค้างคาวกัด/ข่วน** |

### Wound care

- **ล้างด้วยน้ำสบู่/NSS ทันที (irrigation)** + wound dressing + antiseptic (povidone-iodine)
- **ไม่เย็บแผลทันที → delayed primary suture (3–7 วัน)** (ยกเว้นแผลที่หน้าหรือเลือดออกมาก เย็บหลวม ๆ หลังให้ RIG (เสริม))
- **ATB prophylaxis**: **amoxicillin 500 mg 1×3 po pc 3–5 วัน**
- **ATB for treatment** (มาช้าแล้วมี signs of infection): **amoxicillin/clavulanate (500/125) 1×3 po pc** (ครอบ Pasteurella, anaerobe, S. aureus)
- อย่าลืม **tetanus prophylaxis** (ดูหัวข้อ tetanus)

[[fig:id-05-01-f1]]

### PEP (ตามสไลด์)

**สัตว์**: สัตว์ตาย → ตรวจสมองสัตว์ (positive → PEP, negative → no tx) · สัตว์ไม่ตายและ **ครบ 3 ข้อ** (เลี้ยงอย่างดีกักขังบริเวณ + ฉีดวัคซีน ≥ 2 เข็ม เข็มล่าสุด < 1 ปี + มีเหตุจูงใจ) → **กักดู 10 วัน** ปกติไม่ต้องรักษา · **ไม่ครบ 3 ข้อ → PEP**

| | CAT 1 | CAT 2 | CAT 3 |
|---|---|---|---|
| **ไม่เคยฉีด** | No tx | **Rabies vaccine 1 course (D0, 3, 7, 14, 28)** | **Vaccine 1 course + RIG** |
| **เคยฉีดแล้ว** | No tx | เข็มสุดท้าย **< 6 เดือน: 1 dose D0** · **> 6 เดือน: 2 doses D0, 3** | เหมือน CAT 2 (**ไม่ต้อง RIG**) |

- สูตร D0, 3, 7, 14, 28 = Essen IM · ไทยใช้ intradermal 2 จุด D0, 3, 7, 28 ได้ (เสริม)
- RIG (ERIG 40 IU/kg หรือ HRIG 20 IU/kg) แทรกรอบแผลให้มากที่สุด ให้ภายใน 7 วันหลังเข็มแรก (เสริม)

> ในทางปฏิบัติไทย ถ้าต้องกักดูสัตว์ 10 วัน มักเริ่มวัคซีนไปก่อนแล้วหยุดเมื่อสัตว์ปกติครบ 10 วัน (เสริม) — แต่ข้อสอบยึดสไลด์: ครบ 3 ข้อ = กักดูอย่างเดียว
''',
    figs=[F_PEP],
    pearls=[
        "Rabies: hydrophobia + hypersalivation + agitation เป็นพัก ๆ → palliative (ตายเกือบ 100%)",
        "CAT 2 = ถลอก/ข่วน เลือดซิบ · CAT 3 = เลือดออกชัด, เยื่อบุ, ค้างคาว",
        "ไม่เคยฉีด: CAT 2 vaccine D0 3 7 14 28 · CAT 3 + RIG",
        "เคยฉีด: < 6 เดือน 1 เข็ม · > 6 เดือน 2 เข็ม D0, 3 · ไม่ต้อง RIG",
        "แผลสัตว์กัด: ล้าง ไม่เย็บทันที (delayed 3–7 วัน) + amoxicillin 3–5 วัน",
    ],
    items=[
        mcq("ID-05-01-1",
            "A 40-year-old man has had low-grade fever and malaise for 7 days. Over the past 4 days he developed behavioral changes with fluctuating, increasingly severe hyperactive episodes. He has throat discomfort when drinking and is spitting out saliva. He is agitated, pupils are 4 mm and reactive, there is no neck stiffness and no visible wound. What is the most likely diagnosis?",
            "Rabies",
            ["Neurosyphilis", "Herpes simplex encephalitis", "Japanese encephalitis", "Enterovirus encephalitis"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''**กลืนน้ำแล้วเจ็บ (hydrophobia) + น้ำลายมาก + agitation เป็นพัก ๆ** = **rabies** (แผลอาจหายไปแล้วหรือจำไม่ได้) → palliative care
- Neurosyphilis เป็นเรื้อรัง ไม่มี hydrophobia
- HSV encephalitis มีไข้ สับสน ชัก พฤติกรรมเปลี่ยน temporal lobe แต่ไม่มี pharyngeal spasm/hypersalivation
- Japanese encephalitis มักมี parkinsonism, ซึม, movement disorder ไม่ใช่ hydrophobia
- Enterovirus ทำให้ aseptic meningitis/brainstem encephalitis ในเด็ก ไม่ใช่ภาพนี้''',
            pearl="กลัวน้ำ + น้ำลายไหล + agitation fluctuating = rabies", topic="Rabies diagnosis",
            ref=[f"{D} หน้า 171, 176–177"], nl=["2.3.1-3(1)"]),
        mcq("ID-05-01-2",
            "A 30-year-old man is bitten on the forearm by a stray dog, producing puncture wounds with obvious bleeding. He has never received rabies vaccine. The dog ran away. Besides wound care, what is the most appropriate post-exposure prophylaxis?",
            "Rabies vaccine on days 0, 3, 7, 14 and 28 plus rabies immunoglobulin",
            ["Rabies vaccine on days 0, 3, 7, 14 and 28 only", "Rabies vaccine on days 0 and 3 only", "Rabies immunoglobulin only", "Observe for 10 days and vaccinate only if symptoms develop"],
            explain='''แผลทะลุผิวหนัง **เลือดออกชัด = CAT 3** + **ไม่เคยฉีดวัคซีน** + สัตว์จรจัดหนีไป (ประเมินไม่ได้) → **vaccine 1 course (D0, 3, 7, 14, 28) + RIG**
- Vaccine อย่างเดียวใช้กับ CAT 2 ในคนไม่เคยฉีด
- 2 เข็ม D0, 3 ใช้กับคนที่เคยฉีดครบแล้วและเข็มสุดท้าย > 6 เดือน
- RIG อย่างเดียวไม่สร้างภูมิระยะยาว
- การรอดูอาการผู้ป่วยไม่ได้ เพราะเมื่อมีอาการแล้วตายเกือบทั้งหมด และสัตว์ก็กักดูไม่ได้''',
            pearl="CAT 3 + ไม่เคยฉีด = vaccine ครบชุด + RIG", topic="Rabies PEP",
            ref=[f"{D} หน้า 172, 175"], nl=["2.3.1-3(1)", "2.3.18(1)"]),
        mcq("ID-05-01-3",
            "A 25-year-old veterinary student who completed rabies pre-exposure vaccination 2 years ago is scratched by a stray cat, causing a bleeding scratch on her hand. What is the most appropriate post-exposure prophylaxis?",
            "Rabies vaccine 2 doses on days 0 and 3",
            ["Rabies vaccine 1 dose on day 0", "Rabies vaccine on days 0, 3, 7, 14 and 28 plus rabies immunoglobulin", "Rabies immunoglobulin plus 2 doses of vaccine", "No prophylaxis because she is already immune"],
            explain='''เคยฉีดวัคซีนมาแล้ว + **เข็มสุดท้าย > 6 เดือน** + CAT 3 → **vaccine 2 doses D0, 3** · **ไม่ต้องให้ RIG** ในคนที่เคยฉีดครบ
- 1 dose D0 ใช้เมื่อเข็มสุดท้าย < 6 เดือน
- ชุดเต็ม + RIG ใช้กับคนที่ไม่เคยฉีด
- RIG จะไปรบกวนการตอบสนองแบบ booster จึงไม่ให้ในคนเคยฉีด
- ไม่ฉีดเลยไม่ได้ ต้องกระตุ้นทุกครั้งที่สัมผัส CAT 2/3''',
            pearl="เคยฉีดแล้ว > 6 เดือน → 2 เข็ม D0, 3 ไม่ต้อง RIG", topic="Rabies booster",
            ref=[f"{D} หน้า 175"], nl=["2.3.1-3(1)"]),
        mcq("ID-05-01-4",
            "A 12-year-old boy is bitten on the leg after pulling the tail of his neighbor's dog, producing a small bleeding wound. The dog is kept indoors, has received 3 doses of rabies vaccine, the latest 4 months ago, and is healthy. According to the Thai guideline in the slides, what is the most appropriate management of rabies risk?",
            "Observe the dog for 10 days; no vaccine is needed if it remains healthy",
            ["Start rabies vaccine with rabies immunoglobulin immediately", "Kill the dog and send its brain for testing", "Give rabies vaccine on days 0 and 3", "Give rabies immunoglobulin only"],
            explain='''สัตว์ยังมีชีวิตและ **ครบ 3 ข้อ**: เลี้ยงอย่างดีกักขังบริเวณ · ฉีดวัคซีน ≥ 2 เข็มเข็มล่าสุด < 1 ปี · **มีเหตุจูงใจ (ดึงหางสุนัข)** → **กักดูอาการสัตว์ 10 วัน** ถ้าปกติไม่ต้องรักษา (ยังต้องล้างแผล ATB และ tetanus)
- เริ่ม vaccine + RIG ใช้เมื่อไม่ครบ 3 ข้อ หรือสัตว์มีอาการ
- ฆ่าสัตว์ส่งตรวจสมองไม่จำเป็นเมื่อสัตว์สุขภาพดีและสังเกตได้
- 2 เข็ม D0, 3 เป็นสูตรของคนที่เคยฉีดวัคซีนแล้ว
- RIG อย่างเดียวไม่ใช่ทางเลือก''',
            pearl="สัตว์ครบ 3 ข้อ (เลี้ยงดี วัคซีน มีเหตุจูงใจ) → กักดู 10 วัน", topic="Rabies animal assessment",
            ref=[f"{D} หน้า 174"], nl=["2.3.1-3(1)", "2.3.18(1)"]),
        mcq("ID-05-01-5",
            "A 45-year-old woman is bitten on the calf by a dog 30 minutes ago. The wound is a 2-cm laceration with bleeding. She has no penicillin allergy. Besides rabies and tetanus prophylaxis, what is the most appropriate wound management?",
            "Irrigate with saline and leave open for delayed primary closure, with oral amoxicillin for 3–5 days",
            ["Primary suture immediately and no antibiotic", "Primary suture immediately with oral amoxicillin-clavulanate for 14 days", "Irrigate and apply occlusive dressing with topical mupirocin only", "Irrigate and give intravenous ceftriaxone for 7 days"],
            explain='''แผลสัตว์กัดตามสไลด์: **NSS irrigation + dressing** → **delayed primary suture 3–7 วัน** และให้ **ATB prophylaxis = amoxicillin 500 mg tid pc 3–5 วัน** (amox/clav ใช้เมื่อมีการติดเชื้อแล้ว)
- เย็บปิดทันทีเพิ่มความเสี่ยงติดเชื้อ (ยกเว้นแผลที่หน้า)
- Amox/clav 14 วันนานเกินไปและใช้สำหรับแผลติดเชื้อแล้ว
- Mupirocin ทาไม่พอสำหรับแผลกัดลึก
- IV ceftriaxone ไม่จำเป็นสำหรับแผลไม่ติดเชื้อ และไม่ครอบ anaerobe''',
            pearl="แผลสัตว์กัด: ล้าง + delayed suture + amoxicillin 3–5 วัน", topic="Bite wound care",
            ref=[f"{D} หน้า 173"], nl=["2.3.18(1)", "2.2.45"]),
    ])

# ---------------------------------------------------------------- 05-02 Tetanus
F_TET = fig("id-05-02-f1", "Tetanus PEP (ตามสไลด์)", '''<svg viewBox="0 0 740 280">
 <rect x="10" y="10" width="200" height="40" rx="8" class="sunk"/>
 <text x="110" y="35" text-anchor="middle" class="tb">ประวัติวัคซีน</text>
 <rect x="216" y="10" width="252" height="40" rx="8" class="oksoft"/>
 <text x="342" y="35" text-anchor="middle" class="tb">แผลสะอาด (non-prone)</text>
 <rect x="474" y="10" width="256" height="40" rx="8" class="badsoft"/>
 <text x="602" y="35" text-anchor="middle" class="tb">Tetanus-prone wound</text>
 <rect x="10" y="58" width="200" height="60" rx="8" class="box"/>
 <text x="110" y="84" text-anchor="middle" class="tb">ไม่เคยฉีด / ไม่ครบ 3 เข็ม</text>
 <text x="110" y="104" text-anchor="middle" class="t3">หรือไม่ทราบ</text>
 <rect x="216" y="58" width="252" height="60" rx="8" class="miss"/>
 <text x="342" y="84" text-anchor="middle" class="tw">Td/TT 1 course</text>
 <text x="342" y="104" text-anchor="middle" class="tw">0, 1, 6 เดือน</text>
 <rect x="474" y="58" width="256" height="60" rx="8" class="bad"/>
 <text x="602" y="84" text-anchor="middle" class="tw">Td/TT 1 course</text>
 <text x="602" y="104" text-anchor="middle" class="tw">+ TIG</text>
 <rect x="10" y="126" width="200" height="56" rx="8" class="box"/>
 <text x="110" y="150" text-anchor="middle" class="tb">ครบ 3 เข็มแล้ว</text>
 <text x="110" y="170" text-anchor="middle" class="t3">เข็มสุดท้ายนานเกินเกณฑ์</text>
 <rect x="216" y="126" width="252" height="56" rx="8" class="misssoft"/>
 <text x="342" y="150" text-anchor="middle" class="tb">&gt; 10 ปี → Td 1 dose</text>
 <rect x="474" y="126" width="256" height="56" rx="8" class="misssoft"/>
 <text x="602" y="150" text-anchor="middle" class="tb">&gt; 5 ปี → Td 1 dose</text>
 <rect x="10" y="190" width="200" height="56" rx="8" class="box"/>
 <text x="110" y="214" text-anchor="middle" class="tb">ครบ 3 เข็มแล้ว</text>
 <text x="110" y="234" text-anchor="middle" class="t3">เข็มสุดท้ายยังไม่ถึงเกณฑ์</text>
 <rect x="216" y="190" width="252" height="56" rx="8" class="oksoft"/>
 <text x="342" y="214" text-anchor="middle" class="tb">&lt; 10 ปี → ไม่ต้องให้</text>
 <rect x="474" y="190" width="256" height="56" rx="8" class="oksoft"/>
 <text x="602" y="214" text-anchor="middle" class="tb">&lt; 5 ปี → ไม่ต้องให้</text>
 <text x="370" y="270" text-anchor="middle" class="t3">Prone wound = แผลลึก สกปรก ปนดิน/มูลสัตว์ ถูกตำ เนื้อตายมาก ไฟไหม้</text>
</svg>''', "ดูสองอย่าง: เคยฉีดครบ 3 เข็มหรือไม่ และแผลสกปรกหรือไม่ · TIG ให้เฉพาะแผลเสี่ยงในคนที่ไม่เคยฉีดครบ · แผลเสี่ยงใช้เกณฑ์ 5 ปี แผลสะอาดใช้ 10 ปี")

S2 = sec("id-05-02", "Tetanus",
    "C. tetani toxin · trismus, risus sardonicus, opisthotonus, spasm เมื่อถูกกระตุ้น · airway + diazepam + TIG + debridement + metronidazole · หายแล้วไม่มีภูมิ → ฉีดวัคซีน",
    minutes=6, source=f"{D} หน้า 180–186", nl=["2.3.1(5)", "B3.2.2(4)"],
    md='''
### เชื้อและกลไก

- **Clostridium tetani** (spore อยู่ในดิน) สร้าง **tetanospasmin** → ยับยั้งการหลั่ง GABA/glycine จาก inhibitory interneuron (เสริม) → **muscular rigidity & spasm**
- ติดจาก **แผลปนเปื้อน**: แผลลึก ถูกตะปูตำ (penetrating), ไฟไหม้, **สายสะดือ** (neonatal tetanus)

### อาการ

- **Trismus (lockjaw)** มักเป็นอาการแรก
- **Risus sardonicus** (facial muscle spasm ยิ้มแสยะ)
- **Opisthotonus** (หลังแอ่นโค้ง)
- **Spasm เมื่อถูกกระตุ้น** (เสียง แสง สัมผัส) · ผู้ป่วย **รู้สึกตัวดี**
- **Laryngospasm**, respiratory muscle spasm → หายใจล้มเหลว
- **Autonomic dysfunction**: ชีพจร/ความดันขึ้นลงแกว่ง ไข้ เหงื่อออก

### Management

1. **Airway management** (intubation/tracheostomy) · ห้องเงียบ มืด
2. **IV diazepam** (benzodiazepine) ลด muscle spasm · magnesium สำหรับ autonomic instability (เสริม)
3. **Passive immunization: tetanus immunoglobulin (TIG)** จับ toxin ที่ยังไม่เข้า neuron (HTIG 500 IU IM (เสริม))
4. **Wound debridement**
5. **ATB: metronidazole** (preferred) หรือ penicillin G
6. **Active immunization (Td/TT) หลังหาย** — **เป็นแล้วก็ไม่มีภูมิ** เพราะ toxin ปริมาณน้อยไม่กระตุ้นภูมิ

### Tetanus post-exposure prophylaxis (สไลด์หน้า 183–184)

[[fig:id-05-02-f1]]

| ประวัติวัคซีน | Non-prone (แผลสะอาด) | Prone wound (แผลเสี่ยง) |
|---|---|---|
| **ไม่เคยฉีด** | **Tetanus vaccine 1 course (0, 1, 6 เดือน)** | **Vaccine 1 course + TIG** |
| เคยฉีดแล้ว | เข็มสุดท้าย **> 10 ปี → Td/TT 1 dose** · < 10 ปี → no tx | เข็มสุดท้าย **> 5 ปี → Td/TT 1 dose** · < 5 ปี → no tx |

- Prone wound: แผลลึก สกปรก ปนดิน/มูลสัตว์ ถูกตำ เนื้อตายมาก ไฟไหม้ แผลถูกสัตว์กัด มาช้า > 6 ชม. (เสริม)

> Tetanus vs botulism: tetanus = **เกร็ง spasm** · botulism = **อ่อนแรงแบบ descending** ม่านตาขยาย (กินหน่อไม้ปี๊บ)
''',
    figs=[F_TET],
    pearls=[
        "Tetanus: trismus + risus sardonicus + opisthotonus + spasm เมื่อถูกกระตุ้น รู้สึกตัวดี",
        "รักษา: airway + IV diazepam + TIG + debridement + metronidazole",
        "หายจาก tetanus แล้วไม่มีภูมิ → ต้องฉีดวัคซีนต่อ",
        "PEP: ไม่เคยฉีด + แผลเสี่ยง = vaccine 0/1/6 + TIG",
        "เคยฉีด: แผลสะอาด booster ถ้า > 10 ปี · แผลเสี่ยง booster ถ้า > 5 ปี",
    ],
    items=[
        mcq("ID-05-02-1",
            "A 40-year-old construction worker has fever and muscle spasms whenever he is stimulated. Temperature 39 °C, RR 28/min, PR 100/min. He has jaw locking, back arching and a healed punctate wound on the right sole. He is fully conscious. What is the diagnosis?",
            "Tetanus",
            ["Botulism", "Parkinson disease", "Necrotizing fasciitis", "Strychnine poisoning"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''แผลถูกตำที่ฝ่าเท้า + **trismus (jaw lock) + opisthotonus (back arching) + spasm เมื่อถูกกระตุ้น** รู้สึกตัวดี = **tetanus**
- Botulism ทำให้ **อ่อนแรงแบบ flaccid descending** ไม่ใช่เกร็ง
- Parkinson เป็น rigidity เรื้อรัง ไม่มีไข้และ spasm เฉียบพลัน
- Necrotizing fasciitis มีผิวหนังบวมแดงเจ็บรุนแรง ไม่ใช่ trismus
- Strychnine poisoning ทำให้ spasm คล้ายกันได้ แต่ไม่มีแผลและไข้ และไม่มี trismus เด่นตั้งแต่ต้น''',
            pearl="แผลตำ + trismus + opisthotonus = tetanus", topic="Tetanus diagnosis",
            ref=[f"{D} หน้า 180–181, 185–186"], nl=["2.3.1(5)"]),
        mcq("ID-05-02-2",
            "A 55-year-old man is admitted with generalized tetanus 10 days after a deep puncture wound from a rusty nail. He is intubated and sedated with intravenous diazepam. Which combination should be given next?",
            "Human tetanus immunoglobulin, wound debridement and metronidazole",
            ["Tetanus toxoid only", "Intravenous penicillin G only", "Pyridostigmine and botulinum antitoxin", "High-dose dexamethasone and vancomycin"],
            explain='''การรักษา tetanus ตามสไลด์: airway + diazepam + **TIG (passive immunization)** + **wound debridement** + **ATB (metronidazole หรือ penicillin G)** และให้ active immunization เมื่อหาย
- Toxoid อย่างเดียวไม่จับ toxin ที่มีอยู่ (ต้องให้ TIG) — ให้ toxoid เพิ่มได้แต่ไม่พอ
- Penicillin G อย่างเดียวไม่จัดการ toxin และแผล
- Pyridostigmine และ botulinum antitoxin เป็นการรักษาของ myasthenia/botulism
- Dexamethasone และ vancomycin ไม่ใช่การรักษา tetanus''',
            pearl="Tetanus = TIG + debridement + metronidazole + diazepam + airway", topic="Tetanus treatment",
            ref=[f"{D} หน้า 182"], nl=["2.3.1(5)"]),
        mcq("ID-05-02-3",
            "A 30-year-old farmer steps on a nail in a cattle shed, producing a deep dirty puncture wound. He received 3 doses of tetanus vaccine as a child and his last Td booster was 7 years ago. What tetanus prophylaxis is most appropriate?",
            "Td 1 dose",
            ["No tetanus prophylaxis", "Td 1 dose plus tetanus immunoglobulin", "Td 3 doses at 0, 1 and 6 months", "Tetanus immunoglobulin only"],
            explain='''**Tetanus-prone wound** (ลึก สกปรก มูลสัตว์) ในคนที่ **ฉีดครบแล้ว** และ **เข็มสุดท้าย > 5 ปี** (7 ปี) → **Td/TT 1 dose** · ไม่ต้อง TIG
- ไม่ให้เลยใช้ได้เมื่อแผลสะอาดและเข็มสุดท้าย < 10 ปี — แต่แผลนี้เป็นแผลเสี่ยง ใช้เกณฑ์ 5 ปี
- TIG ให้เฉพาะคนไม่เคยฉีด/ฉีดไม่ครบ + แผลเสี่ยง
- 3 เข็ม 0/1/6 เดือนใช้กับคนที่ไม่เคยฉีด
- TIG อย่างเดียวไม่สร้างภูมิระยะยาว''',
            pearl="ฉีดครบแล้ว + แผลเสี่ยง + > 5 ปี → Td 1 เข็ม", topic="Tetanus PEP",
            ref=[f"{D} หน้า 184"], nl=["2.3.1(5)", "B1.4.8"]),
        mcq("ID-05-02-4",
            "A 68-year-old woman who has never received tetanus vaccine sustains a deep laceration contaminated with soil while gardening. What is the most appropriate tetanus prophylaxis?",
            "Tetanus vaccine series (0, 1, 6 months) plus tetanus immunoglobulin",
            ["Tetanus vaccine series only", "Td 1 dose only", "Tetanus immunoglobulin only", "Oral metronidazole for 7 days only"],
            explain='''**ไม่เคยฉีดวัคซีน + prone wound** → **vaccine 1 course (0, 1, 6 เดือน) + TIG**
- Vaccine series อย่างเดียวใช้กับแผลสะอาดในคนไม่เคยฉีด
- Td 1 dose ใช้เป็น booster ในคนที่ฉีดครบแล้ว
- TIG อย่างเดียวป้องกันได้ชั่วคราว ต้องให้วัคซีนร่วมด้วย
- Metronidazole ไม่ใช่การป้องกัน tetanus หลังแผล''',
            pearl="ไม่เคยฉีด + แผลเสี่ยง = vaccine 0/1/6 + TIG", topic="Tetanus PEP unvaccinated",
            ref=[f"{D} หน้า 184"], nl=["2.3.1(5)"]),
    ])

# ---------------------------------------------------------------- 05-03 CDI
F_CDI = fig("id-05-03-f1", "Multistep strategy วินิจฉัย C. difficile", '''<svg viewBox="0 0 740 280">
 <defs><marker id="id-05-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="20" width="200" height="60" rx="10" class="acsoft"/>
 <text x="110" y="44" text-anchor="middle" class="tb">ท้องเสีย ≥ 3 ครั้ง/วัน</text>
 <text x="110" y="64" text-anchor="middle" class="t3">หลังได้ ATB / อยู่ รพ.</text>
 <path d="M210 50H246" class="ln" marker-end="url(#id-05-03-a)"/>
 <rect x="248" y="20" width="220" height="60" rx="10" class="c1soft"/>
 <text x="358" y="44" text-anchor="middle" class="tb">High sensitivity</text>
 <text x="358" y="64" text-anchor="middle" class="t2">NAAT (PCR) หรือ GDH EIA</text>
 <path d="M358 80V120" class="ln" marker-end="url(#id-05-03-a)"/>
 <text x="366" y="104" class="t3">Positive</text>
 <path d="M468 50H538" class="ln" marker-end="url(#id-05-03-a)"/>
 <text x="474" y="42" class="t3">Negative</text>
 <rect x="540" y="30" width="190" height="40" rx="10" class="ok"/>
 <text x="635" y="55" text-anchor="middle" class="tw">CDI unlikely</text>
 <rect x="248" y="122" width="220" height="60" rx="10" class="c2soft"/>
 <text x="358" y="146" text-anchor="middle" class="tb">High specificity</text>
 <text x="358" y="166" text-anchor="middle" class="t2">Toxin A/B EIA</text>
 <path d="M468 152H538" class="ln" marker-end="url(#id-05-03-a)"/>
 <text x="474" y="144" class="t3">Negative</text>
 <rect x="540" y="122" width="190" height="60" rx="10" class="misssoft"/>
 <text x="635" y="146" text-anchor="middle" class="tb">CDI unlikely</text>
 <text x="635" y="166" text-anchor="middle" class="t3">(อาจเป็น colonization)</text>
 <path d="M358 182V222" class="ln" marker-end="url(#id-05-03-a)"/>
 <text x="366" y="206" class="t3">Positive</text>
 <rect x="248" y="224" width="220" height="44" rx="10" class="bad"/>
 <text x="358" y="251" text-anchor="middle" class="tw">Diagnose CDI</text>
 <text x="20" y="230" class="t3">Endoscopy: pseudomembrane</text>
 <text x="20" y="248" class="t3">(yellow-white plaques)</text>
</svg>''', "ตรวจไวก่อน (NAAT/GDH) ถ้าลบตัดทิ้ง ถ้าบวกยืนยันด้วย toxin EIA ที่จำเพาะ (ตามสไลด์หน้า 189)")

S3 = sec("id-05-03", "Clostridioides difficile infection (CDI)",
    "หลังได้ ATB (clinda, amox, ceph, FQ) + PPI + อยู่ รพ. · NAAT/GDH → toxin EIA · mild oral vanco/fidaxomicin · severe WBC ≥ 15,000/Cr > 1.5 · ล้างมือด้วยสบู่",
    minutes=7, source=f"{D} หน้า 187–192", nl=["2.3.1(7)", "2.1.18"],
    md='''
### เชื้อและ risk

- **Clostridioides (Clostridium) difficile** — Gram-positive anaerobe สร้าง spore · สร้าง **toxin A, B** → colitis
- **Fecal–oral** (spore อยู่บนพื้นผิวในโรงพยาบาล)
- Risk: **recent antibiotic** ทำลาย gut microbiota — **clindamycin, amoxicillin/ampicillin, cephalosporins, fluoroquinolones** · **PPI** · NG tube · **recent hospitalization** · อายุมาก

### อาการ

- **Watery diarrhea** (บางครั้งมีเลือด) · fever, N/V, abdominal pain · WBC สูง (leukemoid ได้)
- **Severe CDI: pseudomembranous colitis** — ไข้สูง ปวดท้องมาก ความดันต่ำ · fulminant: ileus, **toxic megacolon**, perforation (เสริม)

### Investigation

- **High sensitivity**: **NAAT (PCR for C. difficile toxin genes)** (นิยม) · **EIA for GDH**
- **High specificity**: **EIA for toxin A/B** · toxigenic culture & cell cytotoxicity (ยุ่งยาก ไม่นิยม)
- **Endoscopy**: pseudomembranous colitis (**yellow-white plaques**)
- ตรวจเฉพาะอุจจาระเหลว (ไม่ตรวจ test of cure) (เสริม)

[[fig:id-05-03-f1]]

### Management

- **หยุด ATB ที่เป็นสาเหตุถ้าทำได้** · หลีกเลี่ยงยาหยุดถ่าย (เสริม)

| ระดับ | เกณฑ์ (ตามสไลด์) | ยา |
|---|---|---|
| **Mild/non-severe** | **WBC < 15,000 และ Cr < 1.5** | **Oral vancomycin** (125 mg qid 10 วัน (เสริม)) หรือ **fidaxomicin** · **oral metronidazole** (ทางเลือกถ้าไม่มี) |
| **Severe** | **WBC ≥ 15,000 หรือ Cr > 1.5** | **Oral vancomycin** (± IV metronidazole) |
| Fulminant | **↓BP**/shock, ileus, megacolon | **Oral vancomycin 500 mg qid + IV metronidazole** (± rectal vancomycin ถ้า ileus) · ปรึกษาศัลย์ (เสริม) |
| Refractory/recurrent บ่อย | | **Fecal microbiota transplantation (FMT)** |

- **IV vancomycin ไม่ได้ผล** เพราะไม่ถูกขับเข้าลำไส้ · **IV metronidazole ได้ผล** เพราะขับออกทางน้ำดี/ผนังลำไส้
- สไลด์จัด "↓BP" อยู่ในกลุ่ม severe และให้ oral vanco + IV metro — ตามแนวทาง IDSA 2017/2021 สูตรนี้สำหรับ **fulminant** ส่วน severe ให้ oral vancomycin หรือ fidaxomicin เดี่ยว ๆ ได้

### Prevention

- **ใช้ ATB อย่างเหมาะสม** (antimicrobial stewardship)
- **Contact precaution**: ถุงมือ เสื้อกาวน์ ห้องแยก
- **ล้างมือด้วยสบู่และน้ำ** — **alcohol hand rub ฆ่า spore ไม่ได้** · ทำความสะอาดพื้นผิวด้วย chlorine (เสริม)
''',
    figs=[F_CDI],
    pearls=[
        "CDI: ท้องเสียหลังได้ ATB/อยู่ รพ. · clinda, amox, ceph, FQ + PPI",
        "NAAT/GDH (ไว) → toxin A/B EIA (จำเพาะ)",
        "Severe = WBC ≥ 15,000 หรือ Cr > 1.5 · ↓BP = fulminant",
        "Oral vancomycin/fidaxomicin · IV vancomycin ไม่ได้ผล · IV metronidazole ใช้เสริมในรายรุนแรง",
        "Spore ทน alcohol → ล้างมือด้วยสบู่และน้ำ",
    ],
    items=[
        mcq("ID-05-03-1",
            "A 70-year-old woman was admitted for pneumonia 4 weeks ago and treated with ceftriaxone. She is readmitted with diarrhea. Temperature 39 °C, tenderness in the left abdomen. WBC 15,000/mm3 with neutrophil predominance. Stool shows numerous WBC. Creatinine is 1.0 mg/dL and BP is normal. Among the following, what is the most appropriate treatment?",
            "Oral metronidazole",
            ["Intravenous ceftriaxone", "Oral doxycycline", "Intravenous vancomycin", "Oral cotrimoxazole"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ตัวเลือกไม่มี oral vancomycin)",
            explain='''ท้องเสียหลังได้ ATB และอยู่ รพ. + ไข้ + WBC 15,000 = **C. difficile infection** · ยาที่ดีที่สุดคือ **oral vancomycin หรือ fidaxomicin** แต่ไม่มีในตัวเลือก → ตัวที่ได้ผลคือ **oral metronidazole** (สไลด์จัด WBC ≥ 15,000 เป็น severe ซึ่งควรใช้ oral vancomycin — ถ้าเจอตัวเลือกนั้นในข้อสอบให้เลือก oral vancomycin)
- Ceftriaxone เป็นตัวทำให้เกิด CDI ยิ่งทำให้แย่ลง
- Doxycycline และ cotrimoxazole ไม่ใช่ยารักษา CDI
- **IV vancomycin ไม่ได้ผล** เพราะไม่ไปถึงลำไส้ — ต้องเป็น oral vancomycin เท่านั้น''',
            pearl="CDI: oral vancomycin (ไม่ใช่ IV) · ไม่มีให้เลือก → oral metronidazole", topic="CDI treatment",
            ref=[f"{D} หน้า 190–192"], nl=["2.3.1(7)"]),
        mcq("ID-05-03-2",
            "A 62-year-old man develops 6 watery stools per day on day 5 of clindamycin for cellulitis. Stool NAAT for C. difficile toxin gene is positive and toxin A/B EIA is positive. Temperature 37.8 °C, WBC 9,800/mm3, creatinine 0.9 mg/dL. Clindamycin is stopped. What is the most appropriate treatment?",
            "Oral vancomycin for 10 days",
            ["Intravenous vancomycin for 10 days", "Loperamide alone", "Fecal microbiota transplantation", "Oral vancomycin plus intravenous metronidazole"],
            explain='''CDI ยืนยันแล้ว (NAAT + toxin) · **non-severe** (WBC < 15,000, Cr < 1.5) → **oral vancomycin** (หรือ fidaxomicin) 10 วัน
- IV vancomycin ไม่ถูกขับเข้าลำไส้ ไม่ได้ผลกับ CDI
- Loperamide อย่างเดียวไม่รักษาเชื้อ และเสี่ยง toxic megacolon
- FMT ใช้เมื่อ refractory หรือ recurrent บ่อย
- Oral vancomycin + IV metronidazole สำหรับรายรุนแรงมาก/fulminant (ความดันต่ำ ileus)''',
            pearl="Non-severe CDI → oral vancomycin หรือ fidaxomicin", topic="Mild CDI",
            ref=[f"{D} หน้า 188–190"], nl=["2.3.1(7)", "2.1.18"]),
        mcq("ID-05-03-3",
            "A 75-year-old patient with suspected C. difficile infection has a positive stool GDH enzyme immunoassay. What is the most appropriate next step in the two-step diagnostic strategy?",
            "Toxin A/B enzyme immunoassay",
            ["Diagnose CDI and treat without further testing", "Repeat GDH assay in 48 hours", "Stool culture for Salmonella and Shigella", "Colonoscopy for all patients"],
            explain='''GDH และ NAAT **ไวสูงแต่ไม่จำเพาะ** (แยก colonization ไม่ได้) → บวกแล้วต้องยืนยันด้วย **toxin A/B EIA** ที่จำเพาะ · ถ้า toxin บวก = CDI
- วินิจฉัยเลยจาก GDH อย่างเดียวจะ overdiagnose ผู้ที่เป็นแค่ carrier
- ตรวจ GDH ซ้ำไม่เพิ่มข้อมูล
- Stool culture แบคทีเรียอื่นไม่ใช่ขั้นตอนต่อของ CDI algorithm
- Colonoscopy ใช้เฉพาะบางราย (เห็น pseudomembrane) ไม่ใช่ทุกราย''',
            pearl="GDH/NAAT บวก → ยืนยันด้วย toxin A/B EIA", topic="CDI diagnosis",
            ref=[f"{D} หน้า 188–189"], nl=["2.3.1(7)"]),
        mcq("ID-05-03-4",
            "A nurse is caring for a patient with confirmed C. difficile infection. Which infection-control measure is most important after patient contact?",
            "Hand washing with soap and water",
            ["Alcohol-based hand rub", "Surgical mask only", "Prophylactic oral metronidazole for staff", "Airborne isolation with an N95 respirator"],
            explain='''C. difficile สร้าง **spore ที่ alcohol ฆ่าไม่ได้** → ต้อง **ล้างมือด้วยสบู่และน้ำ** (ชะล้าง spore ออก) ร่วมกับ contact precaution (ถุงมือ เสื้อกาวน์)
- Alcohol hand rub ใช้ได้ดีกับเชื้อส่วนใหญ่ แต่ไม่ได้ผลกับ spore
- หน้ากากอนามัยไม่เกี่ยว เพราะติดทาง fecal–oral/contact
- ไม่ให้ยาป้องกันแก่บุคลากร
- Airborne precaution ไม่จำเป็น''',
            pearl="CDI: contact precaution + ล้างมือด้วยสบู่ (alcohol ไม่ฆ่า spore)", topic="CDI prevention",
            ref=[f"{D} หน้า 190"], nl=["2.3.1(7)"]),
    ])

LECTURE = lecture("05", "Rabies, tetanus & C. difficile",
    "Animal bite & rabies PEP · tetanus & PEP · CDI",
    objectives=[
        "จัด category แผลสัตว์กัด ประเมินสัตว์ และให้ rabies PEP ตามประวัติวัคซีนได้",
        "ดูแลแผลสัตว์กัดและให้ ATB prophylaxis ได้",
        "วินิจฉัยและรักษา tetanus และให้ tetanus PEP ตามชนิดแผลได้",
        "วินิจฉัย CDI ด้วย multistep strategy และเลือกยาตามความรุนแรงได้",
    ],
    sections=[S1, S2, S3])
