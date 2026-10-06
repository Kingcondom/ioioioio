from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Rheumato"
OLD = "ตัวอย่างข้อสอบในสไลด์"


# ---------------------------------------------------------------- hand schematic helper
def _hand(ox, oy, state):
    """state: dict joint-name -> class (bad = เด่น, miss = พบได้, else box)"""
    g = lambda k: state.get(k, "box")
    out = []
    out.append(f'<rect x="{ox+45}" y="{oy+108}" width="90" height="74" rx="16" class="sunk"/>')
    out.append(f'<path d="M{ox+46} {oy+176}L{ox+60} {oy+160}L{ox+30} {oy+108}L{ox+10} {oy+116}Z" class="sunk"/>')
    out.append(f'<rect x="{ox+52}" y="{oy+184}" width="76" height="16" rx="6" class="sunk"/>')
    fingers = [(57, 30), (80, 18), (103, 26), (125, 48)]
    for i, (cx, top) in enumerate(fingers):
        x = ox + cx
        out.append(f'<rect x="{x-8}" y="{oy+top}" width="16" height="{112-top}" rx="8" class="sunk"/>')
        L = 110 - top
        for name, yy in (("MCP", 110), ("PIP", 110 - 0.48 * L), ("DIP", 110 - 0.8 * L)):
            cls = g(f"{name}{i}") if f"{name}{i}" in state else g(name)
            out.append(f'<circle cx="{x}" cy="{oy+yy:.0f}" r="6" class="{cls}"/>')
    for name, (x, y) in (("CMC1", (50, 166)), ("MCP1", (34, 140)), ("IP1", (20, 118))):
        out.append(f'<circle cx="{ox+x}" cy="{oy+y}" r="6" class="{g(name)}"/>')
    for x in (70, 90, 110):
        out.append(f'<circle cx="{ox+x}" cy="{oy+192}" r="6" class="{g("W")}"/>')
    return "\n ".join(out)


def _foot(ox, oy):
    o = []
    o.append(f'<rect x="{ox+50}" y="{oy+66}" width="80" height="120" rx="34" class="sunk"/>')
    for (x, y, r) in ((66, 46, 14), (92, 46, 8), (108, 52, 7), (121, 60, 7), (131, 72, 6)):
        o.append(f'<circle cx="{ox+x}" cy="{oy+y}" r="{r}" class="sunk"/>')
    o.append(f'<circle cx="{ox+68}" cy="{oy+80}" r="8" class="bad"/>')
    for (x, y) in ((92, 76), (108, 80), (120, 86)):
        o.append(f'<circle cx="{ox+x}" cy="{oy+y}" r="5" class="box"/>')
    o.append(f'<circle cx="{ox+90}" cy="{oy+196}" r="8" class="bad"/>')
    o.append(f'<text x="{ox+20}" y="{oy+110}" class="t3">1st MTP</text>')
    o.append(f'<text x="{ox+108}" y="{oy+200}" class="t3">ankle</text>')
    return "\n ".join(o)


RA_J = {"MCP": "bad", "PIP": "bad", "W": "bad", "MCP1": "bad", "IP1": "miss", "DIP": "box", "CMC1": "box"}
OA_J = {"DIP": "bad", "PIP": "miss", "CMC1": "bad", "IP1": "miss", "MCP": "box", "W": "box"}
PSA_J = {"DIP": "bad", "PIP0": "box", "PIP1": "bad", "PIP2": "box", "PIP3": "box", "MCP1": "box", "MCP": "box",
         "DIP0": "bad", "DIP1": "bad", "DIP2": "box", "DIP3": "bad", "MCP0": "box", "W": "box", "IP1": "bad"}

F_HAND = fig("rheum-02-01-f1", "ข้อที่เป็นบ่อย: RA · OA · PsA · Gout", f'''<svg viewBox="0 0 740 330">
 <text x="10" y="22" class="tb">วงกลม = ข้อ</text>
 <circle cx="120" cy="17" r="6" class="bad"/><text x="132" y="22" class="t3">เป็นบ่อย</text>
 <circle cx="210" cy="17" r="6" class="miss"/><text x="222" y="22" class="t3">พบได้</text>
 <circle cx="290" cy="17" r="6" class="box"/><text x="302" y="22" class="t3">มักไม่เป็น</text>
 {_hand(5, 30, RA_J)}
 {_hand(190, 30, OA_J)}
 {_hand(375, 30, PSA_J)}
 {_foot(560, 30)}
 <text x="92" y="258" text-anchor="middle" class="ta">RA</text>
 <text x="92" y="278" text-anchor="middle" class="t3">สมมาตร MCP PIP wrist</text>
 <text x="92" y="296" text-anchor="middle" class="t3">เว้น DIP และ 1st CMC</text>
 <text x="92" y="314" text-anchor="middle" class="t3">AM stiffness &gt; 30 นาที</text>
 <text x="277" y="258" text-anchor="middle" class="ta">OA</text>
 <text x="277" y="278" text-anchor="middle" class="t3">DIP (Heberden) PIP</text>
 <text x="277" y="296" text-anchor="middle" class="t3">+ 1st CMC · เว้น MCP</text>
 <text x="277" y="314" text-anchor="middle" class="t3">stiffness &lt; 30 นาที</text>
 <text x="462" y="258" text-anchor="middle" class="ta">Psoriatic arthritis</text>
 <text x="462" y="278" text-anchor="middle" class="t3">DIP + PIP อสมมาตร</text>
 <text x="462" y="296" text-anchor="middle" class="t3">ทั้งนิ้ว = dactylitis</text>
 <text x="462" y="314" text-anchor="middle" class="t3">เล็บ pitting</text>
 <text x="650" y="258" text-anchor="middle" class="ta">Gout</text>
 <text x="650" y="278" text-anchor="middle" class="t3">1st MTP (podagra)</text>
 <text x="650" y="296" text-anchor="middle" class="t3">ankle, knee · ขาเด่น</text>
 <text x="650" y="314" text-anchor="middle" class="t3">mono/oligo เฉียบพลัน</text>
</svg>''', "เทียบตำแหน่งข้อ: RA เว้น DIP แต่ OA และ PsA ชอบ DIP · OA ชอบ 1st CMC แต่ไม่เป็น MCP · gout เด่นที่ 1st MTP ของเท้า (ข้อมูล PsA และ OA ส่วนที่ไม่อยู่ในสไลด์ RA เป็นส่วนเสริม)")

# ---------------------------------------------------------------- 02-01 RA clinical
S1 = sec("rheum-02-01", "RA: อาการ ข้อผิดรูป และ extra-articular",
    "หญิงวัยกลางคน · symmetric polyarthritis MCP PIP wrist (เว้น DIP, 1st CMC) · AM stiffness > 30 นาที ดีขึ้นเมื่อขยับ · swan neck, boutonniere, ulnar deviation · nodule, lung fibrosis", minutes=8,
    source=f"{D} หน้า 33–34, 38–41", nl=["2.3.13-3(12)", "B5.2.2-3(4)", "2.1.27"],
    md='''
### นิยามและกลไก
- **Rheumatoid arthritis (RA)** = chronic **symmetric inflammatory polyarthritis** พบบ่อยใน **หญิงวัยกลางคน** (สไลด์หน้า 33)
- กลไก (เสริม): autoimmunity ต่อ citrullinated protein (สัมพันธ์บุหรี่, HLA-DR4) → **synovitis** → เนื้อเยื่อ synovium หนาตัวเป็น **pannus** กัดกร่อนกระดูกอ่อนและกระดูกที่ขอบข้อ (**marginal erosion**) → ข้อผิดรูปถาวร

### อาการทางข้อ (สไลด์หน้า 33)
- **Symmetrical polyarthritis**: พบบ่อยที่ **MCP, PIP, wrist, knee, MTP**
- **ไม่ค่อยเป็นที่ DIP และ 1st CMC** → ใช้แยกจาก OA และ psoriatic arthritis
- **Morning stiffness > 30 นาที** (มักเป็นชั่วโมง) **ดีขึ้นเมื่อขยับ**

[[fig:rheum-02-01-f1]]

### ข้อผิดรูป (deformities)

| Deformity | ลักษณะ |
|---|---|
| **Swan neck** | PIP เหยียดเกิน (hyperextension) + DIP งอ |
| **Boutonniere** | PIP งอ + DIP เหยียดเกิน |
| **Ulnar deviation** | นิ้วเบนไปทาง ulnar ที่ MCP |
| **Atlantoaxial subluxation** | C1–C2 เคลื่อน → เสี่ยงกดไขสันหลังเมื่อแหงนคอ เช่น ตอนใส่ท่อช่วยหายใจ (เสริม) |

### Extra-articular manifestations (สไลด์หน้า 33–34)

| ระบบ | อาการ |
|---|---|
| ผิวหนัง | **Rheumatoid nodule** (ข้อศอก ด้าน extensor), vasculitic lesion |
| ปอด | **Interstitial lung disease/lung fibrosis**, pleural disease, airway disease, ปอดอักเสบจาก DMARD |
| ตา | keratoconjunctivitis sicca (ตาแห้ง), episcleritis, scleritis, scleromalacia perforans |
| หัวใจ หลอดเลือด | pericarditis, coronary artery disease, atherosclerosis, rheumatoid vasculitis, Raynaud |
| ไต | AA amyloid, membranous GN, tubulointerstitial nephritis |
| ประสาท | entrapment neuropathy (carpal tunnel), cervical myelopathy, peripheral neuropathy, mononeuritis multiplex |
| เลือด | anemia of chronic disease, thrombocytosis, **Felty syndrome** (RA + splenomegaly + neutropenia) |
| ทางเดินอาหาร | gastritis/peptic ulcer (จาก NSAID), ตับอักเสบจาก DMARD |

> โจทย์ NL: **หญิง 30–60 ปี + ข้อเล็กมือสองข้าง (MCP/PIP/wrist) + AM stiffness ≥ 1 ชั่วโมง** = RA · ถ้ามี DIP เด่นให้คิด OA หรือ PsA แทน
''',
    figs=[F_HAND],
    pearls=[
        "RA = symmetric polyarthritis MCP, PIP, wrist · เว้น DIP และ 1st CMC",
        "AM stiffness > 30 นาที (มักเป็นชั่วโมง) ดีขึ้นเมื่อขยับ = inflammatory",
        "Swan neck = PIP เหยียด DIP งอ · boutonniere = PIP งอ DIP เหยียด",
        "Atlantoaxial subluxation ต้องระวังก่อนใส่ท่อช่วยหายใจ (เสริม)",
        "Felty = RA + splenomegaly + neutropenia · nodule ที่ข้อศอก = rheumatoid nodule",
    ],
    items=[
        mcq("RHEUM-02-01-1",
            "A 40-year-old woman has had tenderness of both ankles in the early morning for 2 months; the pain usually resolves a few hours later. Examination shows tenderness and swelling of all proximal interphalangeal joints. The distal interphalangeal joints are normal. What is the most likely diagnosis?",
            "Rheumatoid arthritis",
            ["Systemic lupus erythematosus", "Osteoarthritis", "Tuberculous arthritis", "Reactive arthritis"],
            kind="old", src=OLD,
            explain='''Polyarthritis สมมาตรของ PIP ทุกข้อ **เว้น DIP** ร่วมกับ morning stiffness นานหลายชั่วโมง = **RA** (สไลด์เฉลยเน้น "spare DIP joints")
- SLE มี arthritis ได้ แต่ต้องมีอาการระบบอื่น เช่น ผื่น cytopenia ไต ซึ่งโจทย์ไม่มี
- OA ปวดตอนใช้งาน stiffness < 30 นาที และชอบ DIP
- Tuberculous arthritis มักเป็นข้อใหญ่ข้อเดียว (เข่า สะโพก) แบบเรื้อรัง
- Reactive arthritis เป็น oligoarthritis อสมมาตรที่ขา หลังติดเชื้อทางเดินอาหาร/ปัสสาวะ''',
            pearl="PIP หลายข้อสมมาตร + เว้น DIP + AM stiffness นาน = RA", topic="RA diagnosis",
            ref=[f"{D} หน้า 38–39"], nl=["2.3.13-3(12)"]),
        mcq("RHEUM-02-01-2",
            "A 65-year-old woman has swelling and tenderness of both wrists and finger joints. She cannot fully move her joints for about an hour after waking. Examination shows mild swelling of both MCP joints and wrists. Hand radiographs show periarticular osteopenia of the MCP joints, erosion of the ulnar styloid, and pancarpal joint-space narrowing. What is the most likely diagnosis?",
            "Rheumatoid arthritis",
            ["Gout", "Pseudogout", "Osteoarthritis", "Psoriatic arthritis"],
            kind="old", src=OLD,
            explain='''MCP + wrist สองข้าง + AM stiffness 1 ชั่วโมง + X-ray **periarticular osteopenia + marginal erosion (ulnar styloid) + joint space แคบทั่วข้อมือ** = **RA**
- Gout เป็นเฉียบพลันที่ 1st MTP/ขา และ X-ray เรื้อรังเป็น punched-out ที่มีขอบยื่น
- Pseudogout (CPPD) เป็น monoarthritis ข้อมือ/เข่าเฉียบพลัน X-ray เห็น chondrocalcinosis
- OA ไม่มี osteopenia แต่มี subchondral sclerosis และ osteophyte และไม่เป็น MCP
- Psoriatic arthritis ชอบ DIP X-ray เป็น pencil-in-cup''',
            pearl="Periarticular osteopenia + marginal erosion = RA", topic="RA X-ray",
            ref=[f"{D} หน้า 35, 40–41"], nl=["2.3.13-3(12)", "3.2.5"]),
        mcq("RHEUM-02-01-3",
            "A 62-year-old woman with long-standing seropositive rheumatoid arthritis is scheduled for elective surgery under general anesthesia. She reports neck pain and occasional tingling in both hands when she flexes her neck. Which complication must be evaluated before endotracheal intubation?",
            "Atlantoaxial subluxation",
            ["Cricoarytenoid arthritis causing stridor only", "Felty syndrome", "Rheumatoid nodule of the vocal cord", "Cervical spondylotic radiculopathy from osteoarthritis"],
            explain='''RA ทำให้ **atlantoaxial (C1–C2) subluxation** ได้ (สไลด์หน้า 33) ปวดคอและชาเมื่อก้มคอ = สงสัยไขสันหลังถูกกด → ต้องทำ **flexion–extension X-ray ของ C-spine** ก่อนแหงนคอใส่ท่อ (ส่วนการประเมินก่อนผ่าตัดเป็นเสริม)
- Cricoarytenoid arthritis ทำให้เสียงแหบหรือ stridor แต่ไม่อธิบายอาการชามือเมื่อก้มคอ
- Felty syndrome คือ RA + ม้ามโต + neutropenia ไม่เกี่ยวกับคอ
- Rheumatoid nodule ที่สายเสียงพบได้น้อยมาก
- Cervical spondylosis จาก OA ไม่ได้เป็นผลจาก RA และอาการชามักเป็นตาม dermatome ข้างเดียว''',
            pearl="RA + ปวดคอ ชามือ → นึกถึง atlantoaxial subluxation ก่อน intubate", topic="RA extra-articular",
            ref=[f"{D} หน้า 33–34"], nl=["2.3.13-3(12)"]),
        mcq("RHEUM-02-01-4",
            "A 58-year-old woman with 15 years of erosive rheumatoid arthritis presents with recurrent bacterial skin infections. Examination shows ulnar deviation of both hands and a spleen palpable 4 cm below the costal margin. CBC: Hb 10.5 g/dL, WBC 2,100/mm3 with absolute neutrophil count 700/mm3, platelets 180,000/mm3. What is the most likely diagnosis?",
            "Felty syndrome",
            ["Systemic lupus erythematosus overlap", "Methotrexate-induced pancytopenia", "Chronic myeloid leukemia", "AA amyloidosis"],
            explain='''**RA นาน + splenomegaly + neutropenia (ติดเชื้อซ้ำ)** = **Felty syndrome** (อยู่ในหมวด haematological ของ extra-articular RA สไลด์หน้า 34)
- SLE ทำให้ cytopenia ได้ แต่ RA ที่มี erosion และ deformity ไม่เข้ากับ SLE และไม่ทำให้ม้ามโตมากแบบนี้
- Methotrexate ทำให้ pancytopenia ได้ แต่ผู้ป่วยไม่ได้บอกว่ากินยา และ platelet ปกติ ม้ามไม่โตจากยา
- CML ทำให้ม้ามโตแต่ WBC จะสูงมาก ไม่ใช่ต่ำ
- AA amyloidosis ใน RA มักแสดงด้วย nephrotic syndrome''',
            pearl="Felty = RA + splenomegaly + neutropenia", topic="Felty syndrome",
            ref=[f"{D} หน้า 34"], nl=["2.3.13-3(12)"]),
    ])

# ---------------------------------------------------------------- 02-02 RA diagnosis
S2 = sec("rheum-02-02", "RA: การวินิจฉัย — 2010 ACR/EULAR, RF/anti-CCP และ X-ray",
    "≥ 6/10 คะแนน (joints 0–5 · serology 0–3 · APR 0–1 · duration ≥ 6 wk 1) · RF ไวไม่จำเพาะ · anti-CCP จำเพาะ · X-ray marginal erosion + periarticular osteopenia", minutes=8,
    source=f"{D} หน้า 35–36, 42–45", nl=["2.3.13-3(12)", "B5.3(5)", "3.2.5"],
    md='''
### Classification criteria 2010 ACR/EULAR (สไลด์หน้า 36)
- ใช้กับผู้ป่วยที่มี **definite clinical synovitis อย่างน้อย 1 ข้อ** ที่โรคอื่นอธิบายไม่ได้ดีกว่า
- ต้องแยกโรคที่คล้ายกันก่อน: **psoriatic arthritis, viral polyarthritis, gout, CPPD, SLE**
- **≥ 6/10 คะแนน = definite RA**
- สไลด์เขียนหัวว่า "2020 ACR-EULAR" แต่เกณฑ์ชุดนี้คือ **2010** (ยังเป็นชุดปัจจุบัน)

| Domain | เกณฑ์ | คะแนน |
|---|---|---|
| **Joint involvement** | 1 large joint | 0 |
| | 2–10 large joints | 1 |
| | 1–3 small joints (± large) | 2 |
| | 4–10 small joints (± large) | 3 |
| | > 10 joints (อย่างน้อย 1 small joint) | 5 |
| **Serology** | RF และ anti-CCP ลบทั้งคู่ | 0 |
| | RF หรือ anti-CCP บวกต่ำ | 2 |
| | RF หรือ anti-CCP บวกสูง (> 3 เท่าของค่าปกติ) | 3 |
| **Acute phase reactant** | CRP และ ESR ปกติ | 0 |
| | CRP หรือ ESR ผิดปกติ | 1 |
| **Duration** | < 6 สัปดาห์ | 0 |
| | **≥ 6 สัปดาห์** | 1 |

> ตารางในสไลด์ให้ "1–3 small joints = 3" แต่เกณฑ์ต้นฉบับคือ **1–3 small = 2, 4–10 small = 3** — ตารางนี้ใช้ค่าต้นฉบับ (ข้อสอบน่าจะยึดต้นฉบับ)
> Small joints = MCP, PIP, 2nd–5th MTP, thumb IP, wrist · large = shoulder, elbow, hip, knee, ankle (เสริม)

### Investigation (สไลด์หน้า 35)

| การตรวจ | ความหมาย |
|---|---|
| **ESR, CRP สูง** | acute phase reactant ใช้ดู activity |
| **Rheumatoid factor (RF)** | ไว (~70–80%) แต่ **ไม่จำเพาะ** — บวกได้ใน Sjögren, HCV, endocarditis, ผู้สูงอายุ (เสริม) |
| **Anti-CCP** | **จำเพาะสูง (> 95%)** บวกได้ก่อนมีอาการ ทำนาย erosive disease (เสริม) |
| **X-ray มือ/เท้า** | **marginal erosion**, **diffuse (periarticular/juxta-articular) osteopenia**, **joint space narrowing แบบสม่ำเสมอ**, **subchondral bone cyst** |

### X-ray: RA เทียบ OA (เสริม — ใช้แยกบ่อย)

| | RA | OA |
|---|---|---|
| Joint space | แคบ **ทั่วข้อ (uniform)** | แคบ **ไม่สม่ำเสมอ** (เฉพาะส่วนรับน้ำหนัก) |
| กระดูกรอบข้อ | **osteopenia** | **subchondral sclerosis** |
| ขอบข้อ | **marginal erosion** | **osteophyte** |
| ตำแหน่ง | MCP, PIP, wrist (ulnar styloid) | DIP, PIP, 1st CMC, เข่า |

> โจทย์ "ยืนยัน RA" ในสไลด์ (หน้า 44–45) เฉลย **rheumatoid factor** — ในทางปฏิบัติส่ง **RF + anti-CCP** คู่กัน และ anti-CCP จำเพาะกว่า
''',
    pearls=[
        "2010 ACR/EULAR ≥ 6/10: joints 0–5 · serology 0–3 · ESR/CRP 0–1 · ≥ 6 wk 1",
        "RF ไวแต่ไม่จำเพาะ · anti-CCP จำเพาะสูง ทำนาย erosion",
        "X-ray RA: marginal erosion + periarticular osteopenia + uniform JSN",
        "X-ray OA: osteophyte + subchondral sclerosis + JSN ไม่สม่ำเสมอ",
        "ก่อนให้คะแนนต้องแยก PsA, viral arthritis, gout, CPPD, SLE",
    ],
    items=[
        mcq("RHEUM-02-02-1",
            "A 50-year-old man has had pain in multiple joints including the hands, wrists, elbows, knees, PIP and MCP joints. Some joints are swollen and morning stiffness lasts a few hours. Examination shows a 1-cm firm nodule over the right olecranon and a positive ballottement test of the knee. What is the most appropriate investigation to support the diagnosis?",
            "Rheumatoid factor",
            ["Arthrocentesis", "Synovial biopsy", "Antinuclear antibody", "Nodule biopsy"],
            kind="old", src=OLD,
            explain='''Symmetric polyarthritis ของข้อเล็กและใหญ่ + AM stiffness หลายชั่วโมง + **rheumatoid nodule ที่ข้อศอก** = สงสัย **RA** → ส่ง **serology (RF; ปัจจุบันส่งคู่กับ anti-CCP)** ซึ่งเป็นส่วนหนึ่งของ 2010 criteria (สไลด์เฉลย RF)
- Arthrocentesis ช่วยบอกว่าน้ำไขข้อเป็นกลุ่ม inflammatory แต่ไม่จำเพาะกับ RA — ใช้เมื่อเป็นข้อเดียวหรือสงสัย septic/crystal
- Synovial biopsy เป็นหัตถการรุกล้ำ ใช้เมื่อสงสัย TB หรือโรคที่หาสาเหตุไม่ได้
- ANA ใช้คัดกรอง SLE/CTD ไม่ใช่ RA
- ตัด nodule ไปตรวจไม่จำเป็น เพราะภาพทางคลินิกชัดอยู่แล้ว''',
            pearl="Polyarthritis + rheumatoid nodule → ส่ง RF/anti-CCP", topic="RA serology",
            ref=[f"{D} หน้า 35, 44–45"], nl=["B5.3(5)", "2.3.13-3(12)"]),
        mcq("RHEUM-02-02-2",
            "A 60-year-old woman has had morning stiffness for 1 hour for several months. Examination shows mild swelling of the MCP joints and wrists. Hand radiographs show periarticular osteopenia, joint-space narrowing, and erosion at the ulnar styloid. What is the most likely diagnosis?",
            "Rheumatoid arthritis",
            ["Septic arthritis", "Osteoarthritis", "Psoriatic arthritis", "Chronic tophaceous gout"],
            kind="old", src=OLD,
            explain='''MCP + wrist + AM stiffness 1 ชั่วโมง + **periarticular osteopenia และ erosion ที่ ulnar styloid** = ภาพรังสีคลาสสิกของ **RA**
- Septic arthritis เป็นข้อเดียวเฉียบพลันมีไข้ ไม่ใช่หลายข้อเรื้อรัง
- OA X-ray มี osteophyte และ subchondral sclerosis ไม่มี osteopenia และไม่เป็น MCP/wrist เป็นหลัก
- Psoriatic arthritis ชอบ DIP และมี pencil-in-cup
- Chronic tophaceous gout X-ray เป็น punched-out ที่ขอบยื่น (overhanging edge) และมี tophi''',
            pearl="Ulnar styloid erosion + periarticular osteopenia = RA", topic="RA X-ray",
            ref=[f"{D} หน้า 35, 42–43"], nl=["2.3.13-3(12)", "3.2.5"]),
        mcq_ordered("RHEUM-02-02-3",
            "A 45-year-old woman has had swelling of 6 MCP and PIP joints of both hands and both wrists for 8 weeks. Rheumatoid factor is negative and anti-CCP is positive at 5 times the upper limit of normal. ESR is 48 mm/h. Using the 2010 ACR/EULAR classification criteria, what is her total score?",
            ["4", "6", "8", "9", "10"], 4,
            explain='''คิดทีละ domain:
- Joints: small joint 8 ข้อ (MCP/PIP 6 + wrist 2) อยู่ในช่วง 4–10 small joints = **3** (ถ้านับเกิน 10 ข้อจะได้ 5)
- Serology: anti-CCP **บวกสูง** (> 3 เท่า) = **3**
- ESR สูง = **1**
- Duration ≥ 6 สัปดาห์ = **1**
- รวม **8** → ≥ 6 = definite RA

ตัวเลือกอื่นเกิดจากนับพลาด: 4 และ 6 มักเกิดจากลืม serology หรือให้ serology บวกต่ำ (2) · 9 และ 10 เกิดจากนับข้อเป็นกลุ่ม > 10 joints (5)''',
            pearl="2010 RA criteria ≥ 6: 4–10 small = 3, > 10 = 5, high-positive serology = 3", topic="2010 ACR/EULAR",
            ref=[f"{D} หน้า 36"], nl=["2.3.13-3(12)"]),
        mcq("RHEUM-02-02-4",
            "A 48-year-old woman has symmetric polyarthritis of the hands. Rheumatoid factor is weakly positive. Which additional antibody is most specific for rheumatoid arthritis and predicts erosive disease?",
            "Anti-cyclic citrullinated peptide antibody",
            ["Antinuclear antibody", "Anti-double-stranded DNA antibody", "Antihistone antibody", "HLA-B27"],
            explain='''**Anti-CCP** จำเพาะต่อ RA สูง (> 95%) และบวกสูงสัมพันธ์กับ erosive disease ส่วน RF ไวแต่ไม่จำเพาะ (ส่วนตัวเลขเป็นเสริม)
- ANA ไวสำหรับ SLE แต่ไม่จำเพาะ และบวกใน RA ได้บ้าง
- Anti-dsDNA จำเพาะกับ SLE
- Antihistone ใช้กับ drug-induced lupus
- HLA-B27 สัมพันธ์กับ seronegative spondyloarthropathy ไม่ใช่ RA''',
            pearl="Anti-CCP = จำเพาะ RA + ทำนาย erosion", topic="Anti-CCP",
            ref=[f"{D} หน้า 35"], nl=["B5.3(5)"]),
    ])

# ---------------------------------------------------------------- 02-03 RA management
F_TL = fig("rheum-02-03-f1", "RA: DMARD ใช้เวลา ~3 เดือนกว่าจะออกฤทธิ์ → ต้องมียา bridge", '''<svg viewBox="0 0 720 300">
 <defs><marker id="rheum-02-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <path d="M80 230H690" class="ln" marker-end="url(#rheum-02-03-a)"/>
 <path d="M80 230V30" class="ln" marker-end="url(#rheum-02-03-a)"/>
 <text x="70" y="40" text-anchor="end" class="t3">ฤทธิ์</text>
 <text x="70" y="56" text-anchor="end" class="t3">คุมโรค</text>
 <text x="80" y="250" text-anchor="middle" class="t3">0</text>
 <text x="180" y="250" text-anchor="middle" class="t3">1</text>
 <text x="280" y="250" text-anchor="middle" class="t3">2</text>
 <text x="380" y="250" text-anchor="middle" class="t3">3</text>
 <text x="480" y="250" text-anchor="middle" class="t3">4</text>
 <text x="580" y="250" text-anchor="middle" class="t3">5</text>
 <text x="680" y="250" text-anchor="middle" class="t3">6</text>
 <text x="385" y="276" text-anchor="middle" class="t2">เดือนหลังเริ่ม methotrexate</text>
 <path d="M380 230V40" class="lnf"/>
 <path d="M80 70C140 70 260 80 320 150S380 215 420 222L690 222" class="lnbad"/>
 <path d="M80 224C180 222 260 190 330 110S420 72 690 70" class="lnok"/>
 <rect x="450" y="80" width="230" height="44" rx="8" class="oksoft"/>
 <text x="462" y="98" class="tb">DMARD (MTX 1st line)</text>
 <text x="462" y="116" class="t3">คุมโรคระยะยาว หยุด erosion</text>
 <rect x="450" y="140" width="230" height="62" rx="8" class="badsoft"/>
 <text x="462" y="160" class="tb">Bridge: NSAID / steroid</text>
 <text x="462" y="178" class="t3">ออกฤทธิ์ทันที ลดปวด-บวม</text>
 <text x="462" y="194" class="t3">แล้วค่อย ๆ ลดขนาดจนหยุด</text>
 <text x="386" y="34" class="t3">≈ 3 เดือน DMARD เริ่มได้ผล</text>
</svg>''', "เส้นเขียวคือ DMARD ที่ค่อย ๆ ออกฤทธิ์ภายในราว 3 เดือน · เส้นแดงคือ NSAID/steroid ที่ให้ช่วงแรกเพื่อคุมอาการแล้วลดลง")

S3 = sec("rheum-02-03", "RA: การรักษา — NSAID/steroid bridge และ DMARD",
    "Flare: steroid, NSAID · ระยะยาว DMARD: MTX 1st line, SSZ, HCQ/CQ · biologic anti-TNF · MTX/SSZ + folic acid · antimalarial ตรวจตา · DMARD ใช้เวลา 3 เดือน", minutes=8,
    source=f"{D} หน้า 37, 46–51", nl=["2.3.13-3(12)", "B5.4(3)", "B5.4(1)"],
    md='''
### หลักการ (สไลด์หน้า 37)
- **Acute exacerbation (flare): steroid, NSAID** — คุมอาการเร็ว
- **Long-term: DMARD** — เริ่มเร็วที่สุดเมื่อวินิจฉัย เพื่อป้องกัน erosion ถาวร
- **DMARD ใช้เวลาประมาณ 3 เดือนกว่าจะออกฤทธิ์** → ช่วงแรกต้องใช้ **NSAID/steroid ร่วม** (bridging)
- **Physical therapy** ร่วมด้วยเสมอ

[[fig:rheum-02-03-f1]]

### DMARD

| กลุ่ม | ยา | สิ่งที่ต้องรู้ |
|---|---|---|
| Conventional (non-biologic) | **Methotrexate (1st line)** | ให้ **folic acid ร่วม** · ติดตาม CBC, LFT, Cr · ห้ามในครรภ์ · พิษ: ตับ กดไขกระดูก pneumonitis (เสริม) |
| | **Sulfasalazine** | ให้ **folic acid ร่วม** · ใช้ได้ในครรภ์ (เสริม) |
| | **Hydroxychloroquine/Chloroquine** | ต้อง **screening maculopathy** (ตรวจตา) |
| Biologic | **TNF-α inhibitor** (etanercept, adalimumab) | ใช้เมื่อ conventional DMARD ไม่พอ · **ตรวจคัดกรอง TB แฝง และ HBV ก่อนเริ่ม** (เสริม) |

> ขนาด MTX ที่ใช้บ่อย (เสริม): เริ่ม 7.5–15 mg **สัปดาห์ละครั้ง** ปรับถึง 20–25 mg/สัปดาห์ + folic acid 5 mg/สัปดาห์ (หรือ 1 mg/วัน) — การกิน MTX ทุกวันโดยผิดพลาดเป็นสาเหตุพิษรุนแรง

### เลือกยาตามโจทย์
- "**ยาที่บรรเทาปวดเร็วที่สุด**" → **NSAID** (เช่น ibuprofen) — DMARD ช้า paracetamol ไม่ลดการอักเสบ
- "**RA active มี erosion ควรให้อะไร**" ในสไลด์เฉลย **prednisolone** (คุม flare ได้แรงกว่า NSAID)
- "**นอกจาก NSAID ควรให้อะไร**" → **methotrexate** (DMARD 1st line)
''',
    figs=[F_TL],
    pearls=[
        "RA flare: steroid หรือ NSAID · ระยะยาว: DMARD เริ่มทันทีที่วินิจฉัย",
        "Methotrexate = DMARD 1st line · MTX และ SSZ ต้องให้ folic acid",
        "HCQ/CQ ต้องตรวจตาหา maculopathy",
        "DMARD ออกฤทธิ์ ~3 เดือน → bridge ด้วย NSAID/steroid",
        "ก่อนเริ่ม anti-TNF ต้องคัดกรอง TB แฝง (เสริม)",
    ],
    items=[
        mcq("RHEUM-02-03-1",
            "A 50-year-old woman has had pain and swelling of both wrists, MCP, PIP joints, and knees for 6 weeks with morning stiffness lasting 1 hour. She cannot walk because of knee tenderness. Which medication has the fastest onset of pain relief for this patient?",
            "Ibuprofen",
            ["Paracetamol", "Methotrexate", "Sulfasalazine", "Chloroquine"],
            kind="old", src=OLD,
            explain='''ถามยาที่ **บรรเทาปวดเร็วที่สุด** ใน inflammatory arthritis → **NSAID (ibuprofen)** ออกฤทธิ์ภายในชั่วโมงและลดการอักเสบด้วย
- Paracetamol ออกฤทธิ์เร็วแต่ไม่มีฤทธิ์ต้านการอักเสบ จึงช่วยข้ออักเสบได้น้อย
- Methotrexate, sulfasalazine, chloroquine เป็น DMARD ต้องใช้เวลาประมาณ 3 เดือนกว่าจะออกฤทธิ์ (สไลด์หน้า 37) แม้จำเป็นต้องเริ่ม แต่ไม่ใช่คำตอบของคำถามเรื่องความเร็ว''',
            pearl="ยาลดปวดเร็วใน inflammatory arthritis = NSAID", topic="RA symptomatic",
            ref=[f"{D} หน้า 37, 46–47"], nl=["B5.4(1)", "2.3.13-3(12)"]),
        mcq("RHEUM-02-03-2",
            "A 30-year-old woman has had several swollen, painful joints for 2 months with morning stiffness lasting 2 hours. There is no skin rash. Examination shows swelling and tenderness of the PIP, MCP joints, and wrists. Hand radiographs show juxta-articular osteopenia and marginal erosions. Which is the most appropriate management?",
            "Prednisolone",
            ["NSAIDs", "Colchicine", "Tramadol", "Acetaminophen"],
            kind="old", src=OLD,
            explain='''RA ที่ active มากและ **มี erosion แล้ว** → คุม flare ด้วย **steroid (prednisolone) ขนาดต่ำ** เป็น bridge พร้อมเริ่ม MTX — สไลด์เฉลย **prednisolone** (สรุปในสไลด์: flare ใช้ steroid หรือ NSAID ระยะยาวใช้ DMARD)
- NSAIDs ก็ใช้คุม flare ได้และเป็นตัวที่ใกล้เคียงที่สุด แต่ลดเฉพาะอาการ ไม่กด synovitis ได้แรงเท่า steroid ในโรคที่มี erosion แล้ว — ข้อนี้ถ้าเจอในข้อสอบให้ยึดเฉลยสไลด์
- Colchicine ใช้กับ crystal arthritis (gout, CPPD)
- Tramadol และ acetaminophen เป็นยาแก้ปวดที่ไม่ลดการอักเสบ''',
            pearl="RA active มี erosion → prednisolone bridge + เริ่ม MTX", topic="RA flare",
            ref=[f"{D} หน้า 48–49"], nl=["2.3.13-3(12)", "B11.4(3)"]),
        mcq("RHEUM-02-03-3",
            "A 30-year-old woman has had morning joint stiffness for 2 hours. Examination shows swelling and tenderness of multiple PIP and MCP joints. Rheumatoid factor is negative and anti-CCP is positive. Apart from NSAIDs, which drug should be given?",
            "Methotrexate",
            ["Prednisolone", "Paracetamol", "Gabapentin", "Diazepam"],
            kind="old", src=OLD,
            explain='''RA (anti-CCP บวก RF ลบก็ได้) → ต้องเริ่ม **DMARD** ทันที โดย **methotrexate เป็น 1st line** เพื่อป้องกันข้อถูกทำลาย
- Prednisolone ใช้เป็น bridge ระยะสั้นได้ แต่ไม่ใช่ยาหลักระยะยาว — คำถาม "นอกจาก NSAID" ต้องการยาควบคุมโรค
- Paracetamol เป็นยาแก้ปวด ไม่เปลี่ยนการดำเนินโรค
- Gabapentin ใช้กับ neuropathic pain
- Diazepam ไม่มีบทบาทใน RA''',
            pearl="RA ทุกราย → เริ่ม MTX (1st line DMARD)", topic="RA DMARD",
            ref=[f"{D} หน้า 37, 50–51"], nl=["B5.4(3)", "2.3.13-3(12)"]),
        mcq("RHEUM-02-03-4",
            "A 42-year-old woman with rheumatoid arthritis is started on methotrexate 15 mg once weekly. Which supplement should be prescribed with it to reduce adverse effects?",
            "Folic acid",
            ["Vitamin B12", "Vitamin D", "Pyridoxine", "Ferrous sulfate"],
            explain='''MTX เป็น **folate antagonist** → ให้ **folic acid ร่วม** ลดแผลในปาก คลื่นไส้ ตับอักเสบ และการกดไขกระดูก (สไลด์: MTX, SSZ ต้องให้ folic acid ร่วม)
- Vitamin B12 ไม่ได้แก้ผลของการยับยั้ง dihydrofolate reductase
- Vitamin D ให้เมื่อใช้ steroid ระยะยาวเพื่อป้องกันกระดูกพรุน ไม่เกี่ยวกับ MTX
- Pyridoxine ให้คู่กับ isoniazid ป้องกัน neuropathy
- Ferrous sulfate ใช้รักษาภาวะขาดธาตุเหล็ก''',
            pearl="MTX/SSZ + folic acid", topic="MTX",
            ref=[f"{D} หน้า 37"], nl=["B5.4(3)"]),
        mcq("RHEUM-02-03-5",
            "A 39-year-old man with rheumatoid arthritis has persistent active synovitis despite 6 months of methotrexate at maximal dose plus sulfasalazine and hydroxychloroquine. Adalimumab is planned. Which test is most important before starting this drug?",
            "Screening for latent tuberculosis with chest radiograph and tuberculin skin test or IGRA",
            ["Serum uric acid", "HLA-B27 typing", "Anti-dsDNA antibody", "Nerve conduction study"],
            explain='''Adalimumab/etanercept เป็น **TNF-α inhibitor** (สไลด์หน้า 37) TNF สำคัญต่อการคุม granuloma → เสี่ยง **TB แฝงกำเริบ** จึงต้องคัดกรอง TB (และ HBV) ก่อนเริ่มทุกราย (การคัดกรองเป็นเสริม — สำคัญมากในไทย)
- Uric acid เกี่ยวกับ gout
- HLA-B27 ใช้ช่วยวินิจฉัย spondyloarthropathy ไม่ใช่ก่อนให้ biologic
- Anti-dsDNA ใช้กับ SLE
- Nerve conduction study ไม่จำเป็นก่อนให้ยา''',
            pearl="ก่อน anti-TNF → คัดกรอง TB แฝง + HBV", topic="Biologic DMARD",
            ref=[f"{D} หน้า 37"], nl=["B5.4(3)", "2.3.13-3(12)"]),
    ])

LECTURE = lecture("02", "Rheumatoid arthritis", "symmetric polyarthritis · extra-articular · 2010 criteria · RF/anti-CCP · X-ray · DMARD",
    objectives=[
        "วินิจฉัย RA จากรูปแบบข้อ (สมมาตร MCP PIP wrist เว้น DIP) และ morning stiffness",
        "คิดคะแนน 2010 ACR/EULAR และเลือก RF/anti-CCP ได้ถูกบริบท",
        "แยก X-ray ของ RA จาก OA, gout, PsA",
        "เลือกยา flare (NSAID/steroid) กับยาระยะยาว (MTX 1st line) และติดตามผลข้างเคียงของ DMARD",
    ],
    sections=[S1, S2, S3])
