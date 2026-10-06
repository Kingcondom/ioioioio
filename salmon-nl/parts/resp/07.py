from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Respiratory"
OLD = "ข้อสอบเก่าในสไลด์ MedSalmon"

FIG_DX = '''<svg viewBox="0 0 740 400">
 <defs><marker id="resp-07-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="240" y="10" width="260" height="44" rx="10" class="acsoft"/>
 <text x="370" y="30" text-anchor="middle" class="tb">Clinical / risk สงสัย TB</text>
 <text x="370" y="47" text-anchor="middle" class="t3">ไอ ≥ 2 สัปดาห์ ไข้ น้ำหนักลด เหงื่อออกกลางคืน</text>
 <path d="M370 54V76" class="ln" marker-end="url(#resp-07-01-a)"/>
 <rect x="300" y="78" width="140" height="34" rx="10" class="box"/>
 <text x="370" y="100" text-anchor="middle" class="tb">CXR</text>
 <path d="M300 95H170" class="ln" marker-end="url(#resp-07-01-a)"/>
 <text x="236" y="88" text-anchor="middle" class="t3">ปกติ</text>
 <rect x="20" y="76" width="148" height="38" rx="10" class="sunk"/>
 <text x="94" y="100" text-anchor="middle" class="t2">หาสาเหตุอื่น</text>
 <path d="M370 112V136" class="ln" marker-end="url(#resp-07-01-a)"/>
 <text x="380" y="128" class="t3">ผิดปกติ</text>
 <rect x="230" y="138" width="280" height="44" rx="10" class="box"/>
 <text x="370" y="158" text-anchor="middle" class="tb">Sputum AFB (อย่างน้อย 2 ครั้ง)</text>
 <text x="370" y="175" text-anchor="middle" class="t3">+ ส่ง molecular test ทั้งบวกและลบ</text>
 <path d="M300 182L180 216" class="ln" marker-end="url(#resp-07-01-a)"/>
 <path d="M440 182L560 216" class="ln" marker-end="url(#resp-07-01-a)"/>
 <text x="220" y="196" class="ta">AFB +</text>
 <text x="500" y="196" class="ta">AFB −</text>
 <rect x="40" y="218" width="280" height="56" rx="10" class="c1soft"/>
 <text x="180" y="240" text-anchor="middle" class="tb">Molecular testing</text>
 <text x="180" y="260" text-anchor="middle" class="t3">ดูการดื้อ rifampicin (Xpert)</text>
 <rect x="420" y="218" width="280" height="56" rx="10" class="c1soft"/>
 <text x="560" y="240" text-anchor="middle" class="tb">Molecular testing</text>
 <text x="560" y="260" text-anchor="middle" class="t3">LPA, RT-PCR, Xpert MTB/RIF</text>
 <path d="M180 274L300 310" class="ln" marker-end="url(#resp-07-01-a)"/>
 <path d="M520 274L400 310" class="ln" marker-end="url(#resp-07-01-a)"/>
 <path d="M640 274V310" class="ln" marker-end="url(#resp-07-01-a)"/>
 <rect x="200" y="312" width="300" height="74" rx="10" class="bad"/>
 <text x="350" y="336" text-anchor="middle" class="tw">MTB detected</text>
 <text x="350" y="358" text-anchor="middle" class="tw">Culture + DST และเริ่มรักษา</text>
 <text x="350" y="378" text-anchor="middle" class="tw">(2IRZE/4IR ถ้าไม่ดื้อ R)</text>
 <rect x="560" y="312" width="160" height="74" rx="10" class="sunk"/>
 <text x="640" y="336" text-anchor="middle" class="tb">Not detected</text>
 <text x="640" y="356" text-anchor="middle" class="t3">culture, หาสาเหตุอื่น</text>
 <text x="640" y="374" text-anchor="middle" class="t3">หรือ clinical dx</text>
</svg>'''

FIG_TX = '''<svg viewBox="0 0 740 296">
 <defs><marker id="resp-07-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <text x="370" y="22" text-anchor="middle" class="tb">2IRZE / 4IR — ไทม์ไลน์ 6 เดือน</text>
 <rect x="60" y="44" width="200" height="56" rx="8" class="ac"/>
 <text x="160" y="68" text-anchor="middle" class="tw">Intensive phase</text>
 <text x="160" y="88" text-anchor="middle" class="tw">I + R + Z + E</text>
 <rect x="260" y="44" width="420" height="56" rx="8" class="c1soft"/>
 <text x="470" y="68" text-anchor="middle" class="tb">Continuation phase</text>
 <text x="470" y="88" text-anchor="middle" class="t2">I + R</text>
 <path d="M60 130H690" class="ln" marker-end="url(#resp-07-02-a)"/>
 <path d="M60 124V136M160 124V136M260 124V136M365 124V136M470 124V136M575 124V136M680 124V136" class="ln"/>
 <text x="60" y="152" text-anchor="middle" class="t3">0</text>
 <text x="160" y="152" text-anchor="middle" class="t3">1</text>
 <text x="260" y="152" text-anchor="middle" class="t3">2</text>
 <text x="365" y="152" text-anchor="middle" class="t3">3</text>
 <text x="470" y="152" text-anchor="middle" class="t3">4</text>
 <text x="575" y="152" text-anchor="middle" class="t3">5</text>
 <text x="680" y="152" text-anchor="middle" class="t3">6 เดือน</text>
 <path d="M260 162V186M365 162V186M575 162V186M680 162V186" class="lnbad"/>
 <text x="260" y="200" text-anchor="middle" class="t3">AFB</text>
 <text x="365" y="200" text-anchor="middle" class="t3">(AFB)</text>
 <text x="575" y="200" text-anchor="middle" class="t3">AFB</text>
 <text x="680" y="200" text-anchor="middle" class="t3">AFB</text>
 <text x="370" y="226" text-anchor="middle" class="ta">F/U sputum AFB ปลายเดือน 2, (3), 5, 6</text>
 <text x="370" y="246" text-anchor="middle" class="t3">ยังบวก → เช็ค compliance ก่อน แล้ว Xpert + culture/DST หาเชื้อดื้อยา</text>
 <rect x="60" y="256" width="250" height="28" rx="6" class="badsoft"/>
 <text x="185" y="275" text-anchor="middle" class="t3">Airborne precaution ≥ 2 สัปดาห์</text>
 <rect x="430" y="256" width="250" height="28" rx="6" class="sunk"/>
 <text x="555" y="275" text-anchor="middle" class="t3">TB สมอง/กระดูก รักษานานกว่านี้</text>
</svg>'''

S1 = sec("resp-07-01", "Pulmonary TB: อาการและการวินิจฉัย",
    "ไอ ≥ 2 สัปดาห์ + constitutional · CXR upper lobe/cavity · sputum AFB ≥ 2 ครั้ง + molecular (Xpert MTB/RIF) ทั้ง AFB บวกและลบ",
    minutes=6, source=f"{D} หน้า 271–274, 285–287", nl=["2.3.1(20)", "B6.2.2(8)", "3.1.9"],
    md='''
### เชื้อและการติดต่อ
- **Mycobacterium tuberculosis** ติดต่อทาง **airborne** (droplet nuclei)
- กลุ่มเสี่ยง (สไลด์ 272 เป็นภาพ — เสริม): HIV, DM, ผู้สัมผัสร่วมบ้าน, ผู้ต้องขัง, ผู้สูงอายุ, ผู้ได้ยากดภูมิ, silicosis, บุคลากรทางการแพทย์

### อาการ
- **ไอเรื้อรัง ≥ 2 สัปดาห์**
- น้ำหนักลด เบื่ออาหาร อ่อนเพลีย **ไข้ (ต่ำ ๆ ตอนบ่าย/เย็น)**
- ไอมีเลือดปน, เจ็บหน้าอก, หายใจขัด, **เหงื่อออกกลางคืน**

### CXR ใน TB
- **Cavity**
- Consolidation / reticulonodular ใน **upper lung**
- Hilar lymphadenopathy
- Pleural effusion

[[fig:resp-07-01-dx]]

### แนวทางวินิจฉัย (ตามสไลด์ 274)
1. Clinical / risk → **CXR**
2. CXR ผิดปกติ → **sputum AFB อย่างน้อย 2 ครั้ง**
3. ไม่ว่า AFB บวกหรือลบ → **molecular testing** (LPA, RT-PCR, **Xpert MTB/RIF**) — บอกทั้งเชื้อ TB และการดื้อ rifampicin
4. MTB detected → **culture + DST** และเริ่มรักษา

> ข้อสอบเก่า: ไอ ไอเป็นเลือด น้ำหนักลด CXR มี reticulonodular + cavity ผนังหนา แต่ **sputum AFB ลบ 3 ครั้ง** → ขั้นต่อไป **PCR for TB (molecular testing)** — ไม่ต้องรอ culture 6–8 สัปดาห์ และยังไม่ต้องทำ bronchoscopy

> AFB smear ต้องมีเชื้อ ~5,000–10,000 ตัว/mL จึงเห็น → smear ลบไม่ได้ตัด TB (เสริม)
''',
    figs=[fig("resp-07-01-dx", "แนวทางวินิจฉัย pulmonary TB", FIG_DX,
              "CXR ผิดปกติแล้วส่ง AFB อย่างน้อย 2 ครั้ง และส่ง molecular test ทุกราย เพราะ AFB ลบก็ยังเป็น TB ได้ และต้องรู้ว่าดื้อ rifampicin หรือไม่")],
    pearls=["TB: ไอ ≥ 2 สัปดาห์ + ไข้ต่ำ น้ำหนักลด เหงื่อออกกลางคืน",
            "CXR: upper lobe infiltrate/cavity, hilar LN, effusion",
            "Sputum AFB ≥ 2 ครั้ง + molecular test (Xpert MTB/RIF) ทั้ง AFB บวกและลบ",
            "AFB ลบแต่ภาพเข้า TB → PCR/Xpert ไม่ต้องรอ culture"],
    items=[
        mcq("RESP-07-01-1", """A 55-year-old man has dry cough with occasional blood-streaked sputum and has lost 4 kg in 1 month. CXR shows reticulonodular infiltration with a thick-walled cavity in the right upper lobe. Sputum AFB smears are negative 3 times consecutively. What is the most appropriate next step?""",
            "Send sputum for molecular testing (PCR, e.g., Xpert MTB/RIF)",
            ["Wait for TB culture results before deciding", "Start anti-TB drugs empirically without further testing",
             "Bronchoscopy as the next step", "Percutaneous aspiration of the cavity"],
            explain="""ภาพทางคลินิกและ CXR เข้ากับ TB มาก แม้ AFB smear จะลบ ตามแนวทางในสไลด์ให้ส่ง molecular test ซึ่งไวกว่า smear ได้ผลในวันเดียว และบอกการดื้อ rifampicin ด้วย
- Culture ใช้เวลา 6–8 สัปดาห์ การรอทำให้แพร่เชื้อและอาการแย่ลง
- การเริ่มยาโดยไม่ตรวจเพิ่มทำให้ไม่รู้ว่าเชื้อดื้อยาหรือไม่ (ทำได้ถ้าตรวจเพิ่มไม่ได้และอาการรุนแรง)
- Bronchoscopy เป็นหัตถการรุกล้ำ เก็บไว้เมื่อ molecular test ลบ หรือเก็บเสมหะไม่ได้
- การเจาะดูดโพรงทางผิวหนังไม่ใช่วิธีวินิจฉัย TB""",
            pearl="AFB ลบแต่สงสัย TB → molecular test",
            topic="Smear-negative TB", ref=[f"{D} หน้า 274, 285–287"], nl=["2.3.1(20)"], kind="old", src=OLD),
        mcq("RESP-07-01-2", """A 48-year-old man with diabetes has had productive cough for 4 weeks, evening fever, night sweats and weight loss. CXR shows patchy consolidation with a cavity in the left upper lobe. What is the most appropriate initial investigation?""",
            "Sputum AFB smear at least 2 specimens plus molecular testing",
            ["Tuberculin skin test", "Interferon-gamma release assay", "Serum TB antibody", "CT chest before any sputum test"],
            explain="""อาการและ CXR เข้ากับ active pulmonary TB การตรวจขั้นแรกคือเก็บเสมหะส่ง AFB อย่างน้อย 2 ครั้งร่วมกับ molecular test (Xpert MTB/RIF)
- TST และ IGRA ใช้วินิจฉัย latent TB แยก active disease ไม่ได้
- Serum TB antibody ไม่แนะนำ เพราะความแม่นยำต่ำ
- CT chest ไม่จำเป็นต้องทำก่อน เพราะ CXR บอกได้ชัดแล้ว""",
            pearl="Active TB: เสมหะ AFB + molecular · ไม่ใช่ TST/IGRA",
            topic="TB investigation", ref=[f"{D} หน้า 271–274"], nl=["2.3.1(20)", "3.1.9"]),
        mcq("RESP-07-01-3", """A 35-year-old woman has cough for 3 weeks. Sputum AFB is positive 2+. Xpert MTB/RIF shows MTB detected, rifampicin resistance detected. What is the most appropriate next step?""",
            "Send culture and drug susceptibility testing and manage as rifampicin-resistant TB",
            ["Start standard 2IRZE/4IR", "Repeat AFB smear in 2 months", "Treat with isoniazid alone",
             "Start a fluoroquinolone alone for 2 weeks"],
            explain="""Xpert ที่พบว่าดื้อ rifampicin แสดงว่าเป็น RR/MDR-TB ต้องส่ง culture และ DST และรักษาด้วยสูตรยาสำหรับเชื้อดื้อยา (ส่งต่อผู้เชี่ยวชาญ — เสริม)
- สูตรมาตรฐาน IRZE ใช้ไม่ได้ เพราะ rifampicin เป็นยาหลักและเชื้อดื้อแล้ว ถ้าใช้จะเกิดการดื้อยาเพิ่ม
- การรอตรวจ AFB ซ้ำทำให้แพร่เชื้อต่อ
- การให้ยาตัวเดียวทำให้เกิดการดื้อยาเพิ่ม""",
            pearl="Xpert RIF resistance → culture/DST + สูตรเชื้อดื้อยา",
            topic="RR-TB", ref=[f"{D} หน้า 274, 292"], nl=["2.3.1(20)"]),
    ])

S2 = sec("resp-07-02", "Pulmonary TB: การรักษาและการป้องกันการแพร่เชื้อ",
    "2IRZE/4IR · ตั้งครรภ์ใช้ first-line + B6 · airborne precaution ≥ 2 สัปดาห์ · F/U AFB ปลายเดือน 2, (3), 5, 6",
    minutes=7, source=f"{D} หน้า 275, 288–292, 301–304", nl=["2.3.1(20)", "B6.2.2(8)"],
    md='''
### สูตรยามาตรฐาน: **2IRZE / 4IR**
- **Intensive phase 2 เดือน**: Isoniazid + Rifampicin + Pyrazinamide + Ethambutol
- **Continuation phase 4 เดือน**: Isoniazid + Rifampicin

[[fig:resp-07-02-tx]]

### การป้องกันการแพร่เชื้อ
- **Airborne precautions**: ผู้ป่วยใส่ **surgical mask**, บุคลากรใส่ **N95**
- นาน **≥ 2 สัปดาห์** หรือจนกว่า sputum AFB จะลบ
- หยุดงาน/หยุดเรียน **ประมาณ 2 สัปดาห์** หลังเริ่มยา (ตามหลักเดียวกัน) — ไม่ต้องหยุดนานเป็นเดือนหรือเป็นเทอม

### กลุ่มพิเศษ
- **ตั้งครรภ์ / หลังคลอด**: ใช้ **first-line (IRZE) ได้ + vitamin B6 (pyridoxine)**
  - **หลีกเลี่ยง aminoglycosides (streptomycin → หูหนวกในทารก) และ fluoroquinolones**
  - ให้นมได้ ถ้ายังไอมากหรือ AFB ยังบวก → แม่ใส่ surgical mask หรือบีบนมใส่ขวดให้คนอื่นป้อน
- **HIV**: เริ่ม ART ภายใน 2–8 สัปดาห์หลังเริ่มยา TB (เสริม) · ระวัง IRIS

### การติดตามผล (สไลด์ 291 + 292)
- Sputum AFB **ปลายเดือนที่ 2, (3), 5, 6**
- ถ้า AFB ยังบวก → **Xpert MTB/RIF + culture/DST**
- รักษาแล้วไม่ดีขึ้น / AFB กลับบวกมากขึ้น: **1) เช็ค compliance ก่อน → 2) เช็คเชื้อดื้อยา**

> ข้อสอบเก่า: ผู้ป่วย HIV ได้ IRZE 2 เดือน + IR 2 เดือน แล้วอาการไม่ดีขึ้น AFB จาก 1+ เป็น 3+ → สาเหตุที่ต้องคิดอันดับแรกคือ **ไม่กินยาสม่ำเสมอ (non-compliance)** รองลงมาคือ **เชื้อดื้อยา**
''',
    figs=[fig("resp-07-02-tx", "สูตร 2IRZE/4IR และจุดติดตาม", FIG_TX,
              "สองเดือนแรกให้ยาสี่ตัว อีกสี่เดือนให้ I+R และตรวจ AFB ซ้ำที่ปลายเดือน 2, 5, 6 (และเดือน 3 ถ้าเดือน 2 ยังบวก)")],
    pearls=["2IRZE/4IR = 6 เดือน",
            "ตั้งครรภ์: IRZE + B6 ได้ · เลี่ยง streptomycin และ FQ",
            "Surgical mask ผู้ป่วย · N95 บุคลากร · ≥ 2 สัปดาห์หรือจน AFB ลบ",
            "F/U AFB ปลายเดือน 2, (3), 5, 6",
            "รักษาไม่ดีขึ้น → compliance ก่อน แล้วค่อย drug resistance"],
    items=[
        mcq("RESP-07-02-1", """A 26-year-old woman at 16 weeks of gestation is diagnosed with smear-positive pulmonary TB, rifampicin-susceptible. Which regimen is most appropriate for the intensive phase?""",
            "Isoniazid + rifampicin + pyrazinamide + ethambutol (with pyridoxine)",
            ["Isoniazid + rifampicin + ethambutol + streptomycin", "Isoniazid + rifampicin + ethambutol + ofloxacin",
             "Isoniazid + streptomycin + ethambutol + ofloxacin", "Isoniazid + pyrazinamide + ethambutol + ofloxacin"],
            explain="""ตามสไลด์ หญิงตั้งครรภ์ใช้ยา first-line ได้ทั้งหมด (IRZE) ร่วมกับ vitamin B6 เพื่อป้องกัน neuropathy จาก isoniazid
- Streptomycin เป็น aminoglycoside ทำให้ทารกหูหนวก จึงต้องหลีกเลี่ยง
- Ofloxacin และ fluoroquinolone อื่น สไลด์ให้หลีกเลี่ยงในหญิงตั้งครรภ์
- สูตรที่ไม่มี rifampicin ทำให้ประสิทธิภาพลดลงมากโดยไม่จำเป็น""",
            pearl="TB ตั้งครรภ์ = IRZE + B6 · ไม่ใช้ streptomycin/FQ",
            topic="TB in pregnancy", ref=[f"{D} หน้า 275, 288–289"], nl=["2.3.1(20)"], kind="old", src=OLD),
        mcq("RESP-07-02-2", """A 20-year-old university student has smear-positive pulmonary TB and has just started anti-TB treatment. What is the most appropriate advice to prevent transmission?""",
            "Wear a surgical mask for about 2 weeks (until sputum becomes negative)",
            ["Sleep in an air-conditioned room", "Take a leave of absence for one semester",
             "Wear an N95 respirator for 6 months", "No precautions are needed once drugs are started"],
            explain="""หลังเริ่มยาที่เหมาะสม การแพร่เชื้อลดลงเร็วมาก สไลด์ให้ airborne precaution อย่างน้อย 2 สัปดาห์หรือจน AFB ลบ โดยผู้ป่วยใส่ surgical mask
- ห้องแอร์เป็นห้องปิด อากาศหมุนเวียนน้อย เพิ่มการแพร่เชื้อ ควรอยู่ในห้องที่ระบายอากาศดี
- การหยุดเรียนหนึ่งเทอมนานเกินความจำเป็น
- N95 ใช้กับบุคลากรทางการแพทย์ ไม่ใช่ผู้ป่วย และไม่ต้องใส่นาน 6 เดือน
- การไม่ป้องกันเลยหลังเริ่มยาไม่ถูกต้อง เพราะช่วงแรกยังแพร่เชื้อได้""",
            pearl="ผู้ป่วย TB ใส่ surgical mask ~2 สัปดาห์",
            topic="Infection control", ref=[f"{D} หน้า 275, 301–302"], nl=["2.3.1(20)"], kind="old", src=OLD),
        mcq_ordered("RESP-07-02-3", """A 30-year-old bus driver has smear-positive (3+) pulmonary TB and is started on anti-TB drugs. How long should the medical certificate for sick leave be?""",
            ["No leave is necessary", "2 weeks", "1 month", "2 months", "6 months"], 1,
            explain="""การแพร่เชื้อลดลงมากหลังได้ยาที่เหมาะสมประมาณ 2 สัปดาห์ ตามหลัก airborne precaution ≥ 2 สัปดาห์ในสไลด์ คนขับรถโดยสารสัมผัสคนจำนวนมากในที่ปิด จึงควรหยุดงานประมาณ 2 สัปดาห์
- การไม่หยุดงานเลยเสี่ยงต่อการแพร่เชื้อให้ผู้โดยสาร
- 1 เดือน 2 เดือน และ 6 เดือน นานเกินความจำเป็น (6 เดือนคือระยะเวลาของการรักษาทั้งหมด)
(ข้อสอบเก่ามีตัวเลือกให้ลาครั้งละ 1 สัปดาห์จนกว่า AFB จะลบ ซึ่งเป็นแนวคิดที่ยอมรับได้เหมือนกัน)""",
            pearl="TB เริ่มยาแล้ว ~2 สัปดาห์จึงแพร่เชื้อน้อยลงมาก",
            topic="Sick leave", ref=[f"{D} หน้า 275, 303–304"], nl=["2.3.1(20)"], kind="old", src=OLD),
        mcq("RESP-07-02-4", """A patient with HIV and pulmonary TB (initial sputum AFB 1+) received 2 months of IRZE and 2 months of IR. He is clinically worse; CXR shows a new opacity and sputum AFB is now 3+. What should be checked first?""",
            "Adherence (compliance) to anti-TB drugs",
            ["Immediate switch to a second-line regimen without testing", "Add streptomycin to the current regimen",
             "Stop all drugs and observe", "Start high-dose corticosteroids"],
            explain="""ตามสไลด์ เมื่อรักษาแล้วไม่ดีขึ้น สิ่งแรกที่ต้องตรวจคือผู้ป่วยกินยาสม่ำเสมอหรือไม่ แล้วจึงหาเชื้อดื้อยาด้วย Xpert MTB/RIF และ culture/DST
- การเปลี่ยนเป็นยา second-line ทันทีโดยไม่ตรวจ อาจไม่จำเป็นหรือเลือกยาผิด
- การเติมยาเพียงตัวเดียวเข้าไปในสูตรที่ล้มเหลว ทำให้เกิดการดื้อยาเพิ่ม (ห้ามทำ)
- การหยุดยาทั้งหมดทำให้โรคลุกลาม
- Steroid ไม่ได้แก้ปัญหาการรักษาล้มเหลว (ใช้เฉพาะ IRIS หรือ TB บางตำแหน่ง)""",
            pearl="Treatment failure → compliance ก่อน แล้ว drug resistance",
            topic="Treatment failure", ref=[f"{D} หน้า 290–292"], nl=["2.3.1(20)"], kind="old", src=OLD),
    ])

S3 = sec("resp-07-03", "Anti-TB drugs: ผลข้างเคียง",
    "Rash ทุกตัว · hepatitis I R Z · neuropathy I · arthralgia/gout Z · optic neuritis E · red urine + ลด OCP R · oto/nephro S",
    minutes=5, source=f"{D} หน้า 276–278, 295–300", nl=["2.3.1(20)"],
    md='''
### ตารางผลข้างเคียง (สไลด์ 278)
| ผลข้างเคียง | ยา |
|---|---|
| Rash | ทุกตัว |
| **Hepatitis / jaundice** | **I, R, Z** (Z ตับอักเสบรุนแรงที่สุด — เสริม) |
| **Peripheral neuropathy** | **I** (ขาด B6 → ให้ pyridoxine ป้องกัน) |
| **Arthralgia** | **Z**, E |
| **Hyperuricemia** (gout) | **Z** |
| Ototoxic / nephrotoxic | **S** (streptomycin) |
| **Optic nerve** (ตามัว ตาบอดสีแดง–เขียว) | **E**, I |
| **Red/orange urine**, **ลดระดับ OCP** (enzyme inducer) | **R** |

### จำง่าย (เสริม)
- **I**soniazid: **I**nduce neuropathy (B6), hepatitis, drug-induced lupus
- **R**ifampicin: **R**ed-orange body fluids, CYP450 inducer → ลดฤทธิ์ OCP, warfarin, ART บางตัว
- **Z** (pyrazinamide): urate ↑ → **gout** ที่นิ้วโป้งเท้า หรือข้ออื่น, ตับอักเสบ
- **E**thambutol: **E**yes — optic neuritis (ลดขนาดในไตเสื่อม)
- **S**treptomycin: **S**ound (หู) + ไต

### Drug-induced hepatitis (เสริม — สไลด์ 276–277 เป็นภาพ)
- หยุดยาที่ตับเป็นพิษ (I, R, Z) เมื่อ AST/ALT > 3 เท่าของค่าปกติ **และมีอาการ** หรือ > 5 เท่า **โดยไม่มีอาการ** หรือมีดีซ่าน
- ระหว่างหยุด ถ้า TB รุนแรงให้ยาที่ไม่เป็นพิษต่อตับแทน (E + FQ + aminoglycoside)
- ค่าตับกลับมาแล้ว **reintroduce ทีละตัว** (R → I → พิจารณา Z)

> ผู้หญิงที่กินยาคุมกำเนิดและได้ rifampicin → แนะนำวิธีคุมกำเนิดอื่น (ยาฉีด DMPA, IUD, ถุงยาง — เสริม)
''',
    pearls=["Hepatitis: I, R, Z · neuropathy: I (ให้ B6)",
            "Pyrazinamide → hyperuricemia → gout/arthralgia",
            "Ethambutol → optic neuritis",
            "Rifampicin → ปัสสาวะสีส้มแดง + ลดฤทธิ์ OCP",
            "Streptomycin → หูและไต"],
    items=[
        mcq("RESP-07-03-1", """A man with tuberculosis on a 5-drug regimen develops acute pain and swelling of his right big toe. Which drug is the most likely cause?""",
            "Pyrazinamide",
            ["Isoniazid", "Rifampicin", "Ethambutol", "Streptomycin"],
            explain="""Pyrazinamide ลดการขับ uric acid ทางไต ทำให้ hyperuricemia และเกิด gout ที่นิ้วหัวแม่เท้า (podagra)
- Isoniazid ทำให้เกิด neuropathy และตับอักเสบ
- Rifampicin ทำให้ปัสสาวะสีส้มแดง และเป็น enzyme inducer
- Ethambutol ทำให้เกิด optic neuritis (และ arthralgia ได้เล็กน้อย) แต่สาเหตุหลักของ gout คือ Z
- Streptomycin มีพิษต่อหูและไต""",
            pearl="TB + gout = pyrazinamide",
            topic="PZA gout", ref=[f"{D} หน้า 278, 297–298"], nl=["2.3.1(20)"], kind="old", src=OLD),
        mcq("RESP-07-03-2", """A woman with pulmonary TB on IRZE and pyridoxine becomes pregnant despite taking combined oral contraceptive pills correctly. Which drug is responsible?""",
            "Rifampicin",
            ["Isoniazid", "Pyrazinamide", "Ethambutol", "Pyridoxine"],
            explain="""Rifampicin เป็น CYP450 inducer ที่แรง ทำให้ estrogen และ progestin ในยาคุมถูกเผาผลาญเร็วขึ้น ยาคุมจึงล้มเหลว
- Isoniazid เป็น enzyme inhibitor ไม่ได้ลดระดับยาคุม
- Pyrazinamide และ ethambutol ไม่มีปฏิกิริยากับยาคุม
- Pyridoxine เป็นวิตามิน ไม่มีผลต่อยาคุม""",
            pearl="Rifampicin ลดฤทธิ์ OCP",
            topic="Rifampicin interaction", ref=[f"{D} หน้า 278, 299–300"], nl=["2.3.1(20)"], kind="old", src=OLD),
        mcq("RESP-07-03-3", """A patient with TB has been on IRZE for 4 weeks and now has a red, swollen, painful medial malleolus. Serum uric acid is 11 mg/dL. What is the most likely cause?""",
            "Pyrazinamide-induced arthritis (hyperuricemia)",
            ["Pseudogout", "Rifampicin-induced arthritis", "Tuberculous arthritis", "Isoniazid-induced lupus"],
            explain="""ข้ออักเสบเฉียบพลันบวมแดงร่วมกับ uric acid สูงหลังเริ่มยาไม่กี่สัปดาห์ เข้ากับ hyperuricemia จาก pyrazinamide ตามเฉลยในสไลด์
- Pseudogout เกิดจาก CPPD พบบ่อยที่เข่าในผู้สูงอายุ ไม่สัมพันธ์กับยา TB
- Rifampicin ไม่ได้ทำให้เกิด arthritis เป็นผลข้างเคียงหลัก
- TB arthritis มักเป็นแบบเรื้อรังที่ข้อใหญ่ ไม่ได้เกิดเฉียบพลันหลังเริ่มยา
- Isoniazid ทำให้เกิด drug-induced lupus ได้ แต่จะเป็นข้ออักเสบหลายข้อ และ uric acid ไม่สูง""",
            pearl="ข้ออักเสบเฉียบพลันระหว่างกินยา TB → นึกถึง Z",
            topic="PZA arthritis", ref=[f"{D} หน้า 295–296"], nl=["2.3.1(20)"], kind="old", src=OLD),
        mcq("RESP-07-03-4", """A 50-year-old man on IRZE for 6 weeks complains of blurred vision and difficulty distinguishing red from green. Which drug is the most likely cause?""",
            "Ethambutol",
            ["Rifampicin", "Pyrazinamide", "Streptomycin", "Pyridoxine"],
            explain="""Ethambutol ทำให้เกิด optic neuritis ทำให้การมองเห็นลดลงและตาบอดสีแดงเขียว ต้องหยุดยาทันทีและส่งตรวจตา
- Rifampicin ทำให้สารคัดหลั่งเป็นสีส้ม (รวมถึงคราบบน contact lens) แต่ไม่ทำให้ตาบอดสี
- Pyrazinamide ทำให้ตับอักเสบและ gout
- Streptomycin มีพิษต่อหูและไต
- Pyridoxine ใช้ป้องกัน neuropathy""",
            pearl="Ethambutol → optic neuritis (red-green)",
            topic="Ethambutol", ref=[f"{D} หน้า 278"], nl=["2.3.1(20)"]),
        mcq("RESP-07-03-5", """A 60-year-old woman on IRZE for 3 weeks develops numbness and burning of both feet. She has diabetes and drinks alcohol. Which supplement should have been given to prevent this?""",
            "Pyridoxine (vitamin B6)",
            ["Thiamine (vitamin B1)", "Folic acid", "Vitamin B12 injections", "Vitamin D"],
            explain="""Isoniazid รบกวนการทำงานของ pyridoxine ทำให้เกิด peripheral neuropathy โดยเฉพาะในผู้ที่มีความเสี่ยง (DM, ติดสุรา, HIV, ตั้งครรภ์, ขาดอาหาร) การป้องกันคือให้ vitamin B6
- Thiamine ใช้ป้องกัน Wernicke ในคนติดสุรา ไม่ได้ป้องกัน neuropathy จาก INH
- Folic acid และ B12 แก้ภาวะขาดวิตามินเหล่านั้น ไม่ได้แก้กลไกของ INH
- Vitamin D ไม่เกี่ยวข้อง""",
            pearl="INH neuropathy → ป้องกันด้วย B6",
            topic="INH neuropathy", ref=[f"{D} หน้า 275, 278"], nl=["2.3.1(20)"]),
    ])

S4 = sec("resp-07-04", "Extrapulmonary TB และ latent TB infection",
    "TB สมอง/กระดูกรักษานานกว่า · paradoxical reaction · TST conversion + ไม่มีอาการ + CXR ปกติ → treat LTBI (INH)",
    minutes=6, source=f"{D} หน้า 281–284, 293–294, 305–307", nl=["2.3.1(20)", "3.1.11"],
    md='''
### Extrapulmonary TB (สไลด์ 281)
- ช่วงแรกที่เชื้อตาย อาจเกิด **reaction (paradoxical worsening)** เช่น ต่อมน้ำเหลืองโตขึ้นชั่วคราว (เสริม: ไม่ได้แปลว่ายาล้มเหลว)
- **สมองและกระดูก**: ยาเข้าได้ยาก จึงต้อง **รักษานานขึ้น** (TB meningitis และ TB กระดูก ~ 9–12 เดือน + steroid ใน TB meningitis/pericarditis — เสริม)

#### TB lymphadenitis ที่ไม่ตอบสนองต่อยา
- ถ้าให้ยาครบ 2 เดือน ต่อมน้ำเหลืองไม่ยุบ และ FNA ยังพบ AFB เท่าเดิม → นึกถึง **NTM** หรือ **M. bovis** (ดื้อ pyrazinamide โดยธรรมชาติ; สัมผัสวัว นมดิบ — เสริม) หรือเชื้อดื้อยา → **culture for mycobacterial species + DST**

### Latent TB infection (LTBI) (สไลด์ 282–284, 306 เป็นภาพ — สรุปจากแนวทางไทย, เสริม)
นิยาม: ติดเชื้อ TB แต่ **ไม่มีอาการ, CXR ปกติ, ไม่แพร่เชื้อ** — มีโอกาสกลายเป็น active TB

#### ใครควรตรวจ/รักษา
- ผู้สัมผัสร่วมบ้านกับผู้ป่วย TB ปอด (โดยเฉพาะเด็ก < 5 ปี)
- HIV, ผู้จะได้ยากดภูมิ (anti-TNF, steroid ขนาดสูง, ก่อนปลูกถ่ายอวัยวะ), ล้างไต, silicosis
- บุคลากรทางการแพทย์ที่มี **TST conversion** (จากลบเป็นบวกในช่วงไม่นาน = เพิ่งติดเชื้อ)

#### การตรวจ
- **Tuberculin skin test (TST/PPD)**: บวกเมื่อ ≥ 10 mm (≥ 5 mm ใน HIV, ภูมิต่ำ, ผู้สัมผัสใกล้ชิด) · **IGRA** เป็นทางเลือก (ไม่ถูกรบกวนจาก BCG)
- **ต้องตัด active TB ก่อนเสมอ** — ซักอาการ + **CXR**

#### สูตรรักษา LTBI
| สูตร | ระยะเวลา |
|---|---|
| **Isoniazid (INH) รายวัน** | 6–9 เดือน |
| Rifampicin รายวัน (4R) | 4 เดือน |
| Isoniazid + rifapentine รายสัปดาห์ (3HP) | 3 เดือน |

> ข้อสอบเก่า: นักศึกษาแพทย์ปี 4 PPD ปีที่แล้ว 0 mm ปีนี้ 16 mm ไม่มีอาการ CXR ปกติ → **TST conversion = recent infection** → ขั้นต่อไป **INH (รักษา LTBI)** — ไม่ใช่ IRZE (ไม่ใช่ active TB), ไม่ต้องตรวจ IGRA ซ้ำ, ไม่ต้องเก็บเสมหะเมื่อไม่มีอาการและ CXR ปกติ
''',
    pearls=["TB สมองและกระดูก ยาเข้ายาก รักษานานกว่า 6 เดือน",
            "Paradoxical reaction ช่วงแรกไม่ได้แปลว่ายาล้มเหลว",
            "LTBI = TST/IGRA บวก + ไม่มีอาการ + CXR ปกติ",
            "TST conversion ในบุคลากร → ตัด active TB แล้วรักษา LTBI (INH)",
            "ไม่ดีขึ้นหลังรักษา TB lymphadenitis → culture หา NTM/M. bovis + DST"],
    items=[
        mcq("RESP-07-04-1", """A fourth-year medical student undergoes routine PPD screening before entering clinical years. This year the induration is 16 mm; last year it was 0 mm. She is asymptomatic and the CXR is normal. What is the most appropriate next management?""",
            "Isoniazid preventive therapy for latent TB infection",
            ["Close observation without treatment", "Sputum AFB staining", "Interferon-gamma release assay to confirm",
             "IRZE regimen"],
            explain="""PPD เปลี่ยนจาก 0 เป็น 16 mm ภายในหนึ่งปี คือ TST conversion ซึ่งแสดงว่าเพิ่งติดเชื้อและมีความเสี่ยงสูงที่จะเป็น active TB ผู้ป่วยไม่มีอาการและ CXR ปกติ จึงตัด active TB ได้แล้ว ขั้นต่อไปคือรักษา LTBI ด้วย isoniazid (หรือ 3HP/4R)
- การเฝ้าดูโดยไม่รักษา ปล่อยให้คนที่เพิ่งติดเชื้อเสี่ยงเป็นโรค
- Sputum AFB ไม่จำเป็นเมื่อไม่มีอาการและ CXR ปกติ
- IGRA ไม่จำเป็นต้องทำซ้ำ เพราะ conversion ชัดเจนแล้ว
- IRZE เป็นการรักษา active TB""",
            pearl="TST conversion + ไม่มีอาการ + CXR ปกติ → INH",
            topic="LTBI", ref=[f"{D} หน้า 305–307"], nl=["3.1.11", "2.3.1(20)"], kind="old", src=OLD),
        mcq("RESP-07-04-2", """A woman who raises cattle has low-grade fever for 3–4 weeks and bilateral matted cervical lymph nodes (1–1.5 cm). CXR is clear. FNA shows AFB 3+, and anti-TB drugs are started. After 2 months, the nodes have not regressed and repeat FNA still shows AFB 3+. What is the most appropriate management?""",
            "Culture of the aspirate for mycobacterial species with drug susceptibility testing",
            ["Culture for Brucella", "Intravenous immunoglobulin", "CT chest", "Stop anti-TB drugs and observe"],
            explain="""AFB ยังพบเท่าเดิมหลังรักษา 2 เดือน แสดงว่าเชื้อไม่ตอบสนองต่อยา อาจเป็น NTM, M. bovis (ซึ่งดื้อ pyrazinamide โดยธรรมชาติ และพบในคนเลี้ยงวัว) หรือ MDR-TB จึงต้อง culture เพื่อระบุชนิดของ mycobacteria และทำ DST
- Brucella ไม่ติดสี AFB จึงไม่อธิบาย AFB 3+
- Immunoglobulin ไม่มีบทบาท
- CT chest ไม่ได้ช่วยระบุเชื้อ (CXR ปกติอยู่แล้ว)
- การหยุดยาทั้งที่ยังพบเชื้ออยู่ เป็นอันตราย""",
            pearl="AFB ยังบวกหลังรักษา → culture แยกชนิด mycobacteria + DST",
            topic="Non-responding lymphadenitis", ref=[f"{D} หน้า 281, 293–294"], nl=["2.3.1(20)"], kind="old", src=OLD),
        mcq("RESP-07-04-3", """A 25-year-old man with TB meningitis asks how long his treatment will be compared with his brother who had pulmonary TB treated for 6 months. What is the best answer?""",
            "Longer (about 9–12 months), because drugs penetrate the CNS poorly",
            ["The same 6 months", "Shorter, 4 months", "Lifelong", "Only 2 months of intensive phase"],
            explain="""ตามสไลด์ TB ที่สมองและกระดูกรักษานานกว่าเพราะยาเข้าได้ยาก TB meningitis มักรักษา 9–12 เดือน และให้ steroid ช่วงแรกด้วย (เสริม)
- 6 เดือนเป็นระยะเวลาของ pulmonary TB
- 4 เดือนสั้นเกินไป
- ไม่ต้องรักษาตลอดชีวิต
- Intensive phase 2 เดือนอย่างเดียวไม่พอ""",
            pearl="TB สมอง/กระดูก → รักษานาน 9–12 เดือน",
            topic="Extrapulmonary TB", ref=[f"{D} หน้า 281"], nl=["2.3.1(20)"]),
        mcq("RESP-07-04-4", """A 32-year-old woman with cervical TB lymphadenitis started IRZE 3 weeks ago. Her fever has subsided, but one lymph node has enlarged and become fluctuant. She is adherent and the organism is drug-susceptible. What is the most likely explanation?""",
            "Paradoxical reaction during treatment",
            ["Treatment failure from multidrug-resistant TB", "Lymphoma transformation",
             "Rifampicin hypersensitivity", "Non-adherence"],
            explain="""ในช่วงแรกของการรักษา TB นอกปอด อาจเกิด paradoxical reaction (ต่อมน้ำเหลืองโตขึ้นหรือเป็นหนองชั่วคราว) จากปฏิกิริยาภูมิคุ้มกันต่อเชื้อที่ตาย ตามที่สไลด์ระบุว่าช่วงแรกที่เชื้อตายจะเกิด reaction ไข้ลงและเชื้อไวต่อยา จึงไม่ใช่การรักษาล้มเหลว
- MDR-TB ตัดได้เพราะผลทดสอบพบว่าไวต่อยา และอาการโดยรวมดีขึ้น
- Lymphoma ไม่ทำให้เกิดหนองแบบนี้หลังเริ่มยาไม่กี่สัปดาห์
- Rifampicin hypersensitivity ทำให้เกิดผื่นหรืออาการคล้ายไข้หวัด ไม่ใช่ต่อมโตเฉพาะที่
- ผู้ป่วยกินยาสม่ำเสมอ""",
            pearl="ต่อมโตขึ้นช่วงแรกของการรักษา = paradoxical reaction",
            topic="Paradoxical reaction", ref=[f"{D} หน้า 281"], nl=["2.3.1(20)"]),
    ])

LECTURE = lecture("07", "Tuberculosis",
    subtitle="diagnosis · 2IRZE/4IR · side effects · extrapulmonary · latent TB",
    objectives=["ใช้ CXR, sputum AFB และ molecular test วินิจฉัย pulmonary TB ได้",
                "สั่งสูตร 2IRZE/4IR และจัดการกลุ่มพิเศษ (ตั้งครรภ์) การป้องกันการแพร่เชื้อ และการติดตามได้",
                "จับคู่ผลข้างเคียงกับยา TB แต่ละตัวได้",
                "จัดการ extrapulmonary TB, paradoxical reaction และ latent TB (TST conversion) ได้"],
    sections=[S1, S2, S3, S4])
