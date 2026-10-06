from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-Cardio"

def mk(sid):
    return (f'<defs><marker id="{sid}-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            f'markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>')

def box(x, y, w, h, cls, lines, center=True):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" class="{cls}"/>'
    yy = y + 21
    for c, t in lines:
        if center:
            out += f'<text x="{x + w / 2}" y="{yy}" text-anchor="middle" class="{c}">{t}</text>'
        else:
            out += f'<text x="{x + 12}" y="{yy}" class="{c}">{t}</text>'
        yy += 19
    return out

# ---------- fig: HT diagnosis & drug steps ----------
S1 = "cardio-03-01"
dx_svg = (f'<svg viewBox="0 0 720 300">{mk(S1)}'
    + box(10, 10, 200, 60, "acsoft", [("tb", "Office BP ≥ 140/90"), ("t3", "ครั้งแรก ยังไม่มี HMOD")])
    + f'<path d="M210 40H246" class="ln" marker-end="url(#{S1}-a)"/>'
    + box(250, 10, 220, 60, "box", [("tb", "ยืนยันนอกโรงพยาบาล"), ("t3", "HBPM / ABPM หรือวัดซ้ำ visit หน้า")])
    + f'<path d="M470 40H506" class="ln" marker-end="url(#{S1}-a)"/>'
    + box(510, 10, 200, 60, "oksoft", [("tb", "Lifestyle modification"), ("t3", "ทำทุกรายตั้งแต่วันแรก")])
    + '<rect x="10" y="90" width="700" height="200" rx="10" class="sunk"/>'
    + '<text x="24" y="114" class="tb">ใช้ office BP เทียบกับ out-of-office BP</text>'
    + '<text x="280" y="140" text-anchor="middle" class="t2">Out-of-office BP ปกติ</text>'
    + '<text x="560" y="140" text-anchor="middle" class="t2">Out-of-office BP สูง</text>'
    + '<text x="70" y="186" text-anchor="middle" class="t2">Office สูง</text>'
    + '<text x="70" y="256" text-anchor="middle" class="t2">Office ปกติ</text>'
    + box(150, 152, 260, 60, "misssoft", [("tb", "White-coat HT"), ("t3", "LSM + ติดตาม · ไม่ต้องให้ยาส่วนใหญ่")])
    + box(430, 152, 260, 60, "badsoft", [("tb", "Sustained HT"), ("t3", "รักษาตามระดับ BP และความเสี่ยง")])
    + box(150, 222, 260, 60, "oksoft", [("tb", "Normotension"), ("t3", "ตรวจซ้ำตามรอบ")])
    + box(430, 222, 260, 60, "misssoft", [("tb", "Masked HT"), ("t3", "LSM · ยาเมื่อ high CVD risk หรือ HMOD")])
    + '</svg>')

S2 = "cardio-03-02"
step_svg = (f'<svg viewBox="0 0 720 272">{mk(S2)}'
    + box(10, 12, 220, 96, "acsoft", [("tb", "Step 1 (ส่วนใหญ่เริ่ม 2 ตัว)"), ("", "ACEI หรือ ARB"), ("", "+ CCB หรือ thiazide(-like)"), ("t3", "ผู้สูงอายุ/BP ไม่สูงมาก เริ่ม 1 ตัวได้")])
    + f'<path d="M230 60H256" class="ln" marker-end="url(#{S2}-a)"/>'
    + box(260, 12, 210, 96, "c1soft", [("tb", "Step 2"), ("", "ACEI/ARB + CCB"), ("", "+ thiazide(-like)"), ("t3", "ปรับเป็น max tolerated dose")])
    + f'<path d="M470 60H496" class="ln" marker-end="url(#{S2}-a)"/>'
    + box(500, 12, 210, 96, "badsoft", [("tb", "Resistant HT"), ("", "3 ตัว max dose ยังไม่ถึงเป้า"), ("", "+ spironolactone (เสริม)"), ("t3", "หา secondary HT · เช็ค adherence")])
    + box(10, 128, 700, 136, "sunk",
          [("tb", "5 กลุ่มหลัก: ACEI/ARB · beta-blocker · CCB · thiazide/thiazide-like"),
           ("", "ห้ามให้ ACEI ร่วมกับ ARB · beta-blocker ห้ามคู่กับ non-DHP CCB (bradycardia/AV block)"),
           ("", "Proteinuria / UACR ≥ 30 (DM หรือ CKD) → ต้องมี ACEI/ARB เป็นแกน"),
           ("", "COPD/asthma → prefer CCB · เลี่ยง beta-blocker (bronchospasm) และ ACEI (ไอ)"),
           ("", "HFrEF → ACEI/ARB/ARNI + BB + MRA + SGLT2i · เลี่ยง non-DHP CCB"),
           ("t3", "หลังเริ่ม ACEI/ARB: เช็ค Cr ใน 4 สัปดาห์ · Cr ขึ้น ≤ 30% ให้ต่อ · > 30% หยุดยา + หาสาเหตุ (RAS)")], center=False)
    + '</svg>')

# ---------- fig: secondary HT clues ----------
S3 = "cardio-03-03"
def row(y, cls, a, b, c):
    return (f'<rect x="10" y="{y}" width="700" height="44" rx="8" class="{cls}"/>'
            f'<text x="24" y="{y+27}" class="tb">{a}</text>'
            f'<text x="196" y="{y+27}">{b}</text>'
            f'<path d="M520 {y+22}H540" class="ln" marker-end="url(#{S3}-a)"/>'
            f'<text x="548" y="{y+27}" class="ta">{c}</text>')
sec_svg = (f'<svg viewBox="0 0 720 360">{mk(S3)}'
    + '<text x="24" y="20" class="t3">โรค</text><text x="196" y="20" class="t3">เบาะแสในโจทย์</text><text x="548" y="20" class="t3">ส่งตรวจ</text>'
    + row(30, "c1soft", "Renal artery stenosis", "flash pulmonary edema · abdominal bruit · Cr ↑", "Duplex US / CTA / MRA")
    + row(80, "c2soft", "Primary aldosteronism", "resistant HT · hypoK + met. alkalosis", "PAC ↑ PRA ↓ ARR ↑")
    + row(130, "badsoft", "Pheochromocytoma", "paroxysmal headache, palpitation, sweating", "metanephrines")
    + row(180, "oksoft", "Renal parenchymal / GN", "proteinuria, hematuria, edema, Cr ↑", "UA, Cr / renal US")
    + row(230, "misssoft", "ADPKD", "FHx · hematuria · flank pain · ไตโตคลำได้", "Renal ultrasound")
    + row(280, "sunk", "Coarctation of aorta", "BP แขน &gt; ขา · femoral pulse เบา", "Echocardiography")
    + '<text x="710" y="350" text-anchor="end" class="t3">OSA: อ้วน กรน ง่วงกลางวัน → sleep study</text>'
    + '</svg>')

# ---------- fig: HT emergency BP lowering timeline ----------
S4 = "cardio-03-04"
crisis_svg = (f'<svg viewBox="0 0 720 340">{mk(S4)}'
    + '<path d="M80 30V260H700" class="ln"/>'
    + '<text x="40" y="150" text-anchor="middle" class="t3" transform="rotate(-90 40 150)">BP</text>'
    + '<text x="390" y="300" text-anchor="middle" class="t3">เวลาหลังเริ่ม IV antihypertensive</text>'
    + ''.join(f'<path d="M{x} 260V266" class="ln"/><text x="{x}" y="280" text-anchor="middle" class="t3">{t}</text>'
              for x, t in ((80, "0"), (230, "1 ชม."), (420, "2–6 ชม."), (660, "24–48 ชม.")))
    + '<path d="M80 50L230 112L420 160L660 205" class="lna"/>'
    + '<circle cx="80" cy="50" r="5" class="ac"/><circle cx="230" cy="112" r="5" class="ac"/>'
    + '<circle cx="420" cy="160" r="5" class="ac"/><circle cx="660" cy="205" r="5" class="ac"/>'
    + '<text x="92" y="44" class="t2">≥ 180/120 + end-organ damage</text>'
    + '<text x="240" y="104" class="t2">ลด MAP ไม่เกิน 25%</text>'
    + '<text x="430" y="152" class="t2">~160/100–110</text>'
    + '<text x="560" y="230" class="t2">ค่อย ๆ สู่ปกติ</text>'
    + '<path d="M80 50L230 230" class="lnbad"/>'
    + '<text x="140" y="238" class="t3">dissection: SBP 100–120 + HR ≤ 60 ใน 20 นาที–1 ชม.</text>'
    + '<rect x="440" y="36" width="270" height="62" rx="9" class="box"/>'
    + '<text x="452" y="58" class="tb">ทำไมห้ามลดเร็ว?</text>'
    + '<text x="452" y="78" class="t3">autoregulation เลื่อนขึ้น ลดเร็วเกิน →</text>'
    + '<text x="452" y="94" class="t3">สมอง/ไต/หัวใจขาดเลือด (เสริม)</text>'
    + '<rect x="80" y="320" width="14" height="4" class="ac"/><text x="100" y="326" class="t3">HT emergency ทั่วไป</text>'
    + '<path d="M260 322H276" class="lnbad"/><text x="282" y="326" class="t3">aortic dissection (ลดเร็วกว่า)</text>'
    + '</svg>')


LECTURE = lecture("03", "Hypertension",
    subtitle="Dx · drug choice · secondary HT · hypertensive crises",
    objectives=[
        "วินิจฉัย HT รวมถึง white-coat และ masked HT และรู้เกณฑ์เริ่มยาได้",
        "เลือกยาลดความดันตาม comorbidity (DM, CKD, proteinuria, COPD, HF, CAD) ได้",
        "บอกเบาะแสและการตรวจเบื้องต้นของ secondary HT แต่ละสาเหตุได้",
        "แยก HT emergency กับ urgency และเลือกยา IV และเป้าการลด BP ได้",
    ],
    sections=[
    # ------------------------------------------------------------------ Dx
    sec("cardio-03-01", "Hypertension: diagnosis, HMOD & when to treat",
        "Office ≥ 140/90 → ยืนยันด้วย HBPM/ABPM · เริ่มยาที่ ≥ 130/80 ถ้ามี CVD, DM หรือ Thai CV risk ≥ 10%", minutes=6,
        source=f"{D} หน้า 116–124, 127–128, 134, 148–150", nl=["2.3.9(4)", "B7.2.5(1)"],
        md='''
### ประเภท
- **Primary (essential) HT** — ส่วนใหญ่
- **Secondary HT** — มีสาเหตุที่แก้ได้ (หัวข้อถัดไป)

### เกณฑ์วินิจฉัย (สไลด์หน้า 117–118 เป็นตาราง — ค่าตามแนวทางสมาคมความดันโลหิตสูงแห่งประเทศไทย เสริม)
| วิธีวัด | HT เมื่อ |
|---|---|
| Office BP | ≥ 140/90 mmHg |
| Home BP (HBPM) | ≥ 135/85 mmHg |
| ABPM กลางวัน | ≥ 135/85 mmHg |
| ABPM กลางคืน | ≥ 120/70 mmHg |
| ABPM 24 ชม. | ≥ 130/80 mmHg |

- เจอ office BP สูงครั้งแรกและยังไม่มี HMOD → **ยืนยันด้วย HBPM/ABPM หรือวัด office BP ซ้ำ visit หน้า** + เริ่ม lifestyle modification ระหว่างนั้น (สไลด์หน้า 134)
- **HBPM/ABPM ยังช่วยประเมิน orthostatic hypotension** และการคุม BP ที่บ้าน (สไลด์หน้า 150)

[[fig:ht-dx]]

### White-coat vs masked HT (สไลด์หน้า 127–128)
- **White-coat HT**: office สูง แต่ out-of-office ปกติ
- **Masked HT**: office ปกติ แต่ **out-of-office สูง** → LSM · **เริ่มยาเมื่อ high CVD risk หรือมี HMOD** (สไลด์หน้า 148)

### Hypertension-mediated organ damage (HMOD)
- Vascular: atherosclerosis, aortic aneurysm
- Heart: **LVH**, CAD, heart failure
- Kidney: CKD, **albuminuria**
- Brain: stroke, TIA, vascular dementia
- Eye: hypertensive retinopathy

### เมื่อไรเริ่มยาลดความดัน (สไลด์หน้า 121)
- **Office SBP ≥ 140 และ/หรือ DBP ≥ 90 mmHg**
- **Office SBP ≥ 130 และ/หรือ DBP ≥ 80 mmHg** เมื่อมี **clinical CVD, DM หรือ Thai CV risk ≥ 10%**

### เป้าหมาย (สไลด์หน้า 122–124 เป็นตาราง — เสริม)
- Office BP ส่วนใหญ่ **< 130/80 mmHg ถ้าทนได้** (ต้องไม่ต่ำกว่า 120/70) · ผู้สูงอายุมาก/เปราะบาง เป้า SBP 130–139 ได้
- Home BP เป้า < 130/80 โดยประมาณ
- ตรวจสอบตัวเลขเป้าหมายจากตารางในสไลด์อีกครั้ง เพราะเป็นภาพที่อ่านไม่ได้
''',
        figs=[fig("ht-dx", "ยืนยัน HT และแยก white-coat / masked", dx_svg,
                  "แถวบนคือลำดับเมื่อเจอ office BP สูงครั้งแรก ตารางล่างใช้เทียบ office BP กับ BP นอกโรงพยาบาลเพื่อแยกสี่กลุ่ม")],
        pearls=[
            "Office ≥ 140/90 ครั้งแรก → ยืนยันด้วย HBPM/ABPM ก่อนติดป้าย HT",
            "HBPM ≥ 135/85 = HT (เสริม)",
            "เริ่มยาที่ ≥ 130/80 ถ้ามี CVD, DM หรือ Thai CV risk ≥ 10%",
            "Masked HT: office ปกติแต่บ้านสูง → ยาเมื่อ high CVD risk/HMOD",
        ],
        items=[
            mcq("CARDIO-03-01-1",
                "A 50-year-old man has headache and dizziness for 3 months. He has no underlying disease, does not drink or smoke, and a check-up earlier this year was normal. Weight 63 kg, height 165 cm. BP 150/95 mmHg, PR 80/min. PMI at the 5th ICS medial to the MCL, normal S1S2, no murmur, normal neurological examination. What is the most appropriate initial management?",
                "Lifestyle modification and confirm with home or ambulatory BP monitoring",
                ["Start an ACE inhibitor", "Start a calcium channel blocker", "Start a beta-blocker", "Start a thiazide diuretic"],
                explain='''Office BP ≥ 140/90 **ครั้งแรก** ในคนที่ไม่มี HMOD (PMI ปกติ ไม่มี LVH ไม่มี neuro deficit) และไม่มี DM/CVD → **ยืนยันด้วย HBPM/ABPM หรือวัดซ้ำ visit หน้า** พร้อมเริ่ม lifestyle modification (สไลด์หน้า 134)
- ACEI, CCB, beta-blocker และ thiazide เป็นยาหลักทั้งหมด แต่ยังไม่ควรเริ่มก่อนยืนยันว่าเป็น HT จริง เพราะอาจเป็น white-coat HT — และในอนาคตถ้าต้องเริ่ม มักเริ่มเป็นคู่ ACEI/ARB + CCB หรือ thiazide''',
                pearl="BP สูงครั้งแรก ไม่มี HMOD → ยืนยันนอก รพ. + LSM ก่อน",
                topic="Confirm HT", ref=[f"{D} หน้า 133–134"], nl=["2.3.9(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 133"),
            mcq("CARDIO-03-01-2",
                "A 45-year-old woman has dizziness and headache. Her home BP readings are consistently above 150/95 mmHg. At the hospital two readings are 138/88 and 135/85 mmHg. She has no diabetes, no cardiovascular disease and no evidence of organ damage. What is the most appropriate management?",
                "Lifestyle modification with close home BP follow-up",
                ["Reassure that BP is normal", "Prescribe an anxiolytic", "Start an ACE inhibitor", "Start a beta-blocker"],
                explain='''Office BP ปกติ (< 140/90) แต่ **home BP สูง** = **masked hypertension** → **LSM** และติดตาม · เริ่มยาเมื่อมี **high CVD risk หรือ HMOD** (สไลด์หน้า 148) ซึ่งผู้ป่วยรายนี้ไม่มี
- การบอกว่าปกติ พลาดเพราะ out-of-office BP คือค่าที่สัมพันธ์กับความเสี่ยงจริง
- Anxiolytic ไม่ได้รักษา HT — ภาวะนี้กลับกับ white-coat HT
- ACEI และ beta-blocker จะเหมาะเมื่อมีความเสี่ยงสูงหรือ HMOD ตามสไลด์''',
                pearl="Masked HT = office ปกติ บ้านสูง → LSM, ยาถ้า high risk/HMOD",
                topic="Masked HT", ref=[f"{D} หน้า 147–148"], nl=["2.3.9(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 147"),
            mcq("CARDIO-03-01-3",
                "A 60-year-old man on HCTZ and enalapril for HT has office BP around 140–150/90–100 mmHg. He complains of dizziness, especially on changing position. Supine BP is 150/100 mmHg and sitting BP is 140/100 mmHg. BMI 28 kg/m2. What is the most appropriate management?",
                "Recommend home BP measurement",
                ["Reassure", "Increase the dose of HCTZ", "Recommend a polysomnogram", "Add a beta-blocker"],
                explain='''ผู้ป่วยมีอาการมึนเวลาเปลี่ยนท่าซึ่งชวนสงสัย orthostatic hypotension จากยา แต่ office BP ยังดูสูง การวัด **home BP** ช่วยทั้ง **ประเมินการคุม BP จริง และจับ orthostatic hypotension** ก่อนปรับยา (สไลด์หน้า 150)
- Reassure ไม่ได้ตอบคำถามว่าคุมได้หรือยังและอาการมึนมาจากอะไร
- เพิ่ม HCTZ อาจทำให้ volume ลดและ orthostatic hypotension แย่ลง
- Polysomnogram ใช้หา OSA ซึ่งโจทย์ไม่มีกรน/ง่วงกลางวัน
- Beta-blocker ไม่ใช่ยาเสริมลำดับถัดไป (step ถัดไปคือ CCB) และอาจทำให้มึนมากขึ้น''',
                pearl="สงสัย orthostatic hypotension หรือ white-coat → HBPM/ABPM",
                topic="HBPM", ref=[f"{D} หน้า 149–150"], nl=["2.3.9(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 149"),
        ]),
    # ------------------------------------------------------------------ drug choice
    sec("cardio-03-02", "Antihypertensive drug selection by comorbidity",
        "เริ่ม ACEI/ARB + CCB หรือ thiazide · proteinuria → ACEI/ARB · COPD → CCB · CCB edema", minutes=8,
        source=f"{D} หน้า 125–126, 129–132, 136–146, 152, 163", nl=["2.3.9(4)", "B7.4(4)", "B7.2.5(1)"],
        md='''
### หลักการเลือกยา
- **5 กลุ่มหลัก เลือกตัวไหนก็ได้**: ACEI หรือ ARB · beta-blocker · CCB · thiazide/thiazide-like diuretic
- **ห้าม ACEI ร่วมกับ ARB**
- **ส่วนใหญ่เริ่ม 2 ตัว** — prefer **(ACEI/ARB) + (CCB หรือ thiazide/thiazide-like)**
- **Step 2**: ACEI/ARB + CCB + thiazide/thiazide-like
- **Resistant HT** = ได้ยา 3 ชนิดขนาด maximum tolerated แล้วยังสูง (algorithm สไลด์หน้า 132 เป็นภาพ — เสริม: ตรวจ adherence, white-coat, secondary HT แล้วเพิ่ม **spironolactone** เป็นตัวที่ 4)
- ผู้สูงอายุมาก/BP ไม่สูงมาก เริ่ม **1 ตัวได้** (สไลด์หน้า 142)

[[fig:ht-steps]]

### ตารางเลือกยาตามโรคร่วม (สไลด์หน้า 129–131)
| โรคร่วม | Preferred | Avoid |
|---|---|---|
| Stable CAD | ACEI/ARB, beta-blocker | |
| Stable CAD with angina | beta-blocker, DHP-CCB, non-DHP CCB | BB ร่วมกับ non-DHP CCB |
| HFrEF | ACEI/ARB/ARNI + BB + MRA + SGLT2i | non-DHP CCB |
| ต้องใช้ diuretic | ไม่บวมมาก: thiazide(-like) · บวมมาก: loop | |
| CKD ที่ UACR ≥ 30 mg/g | **ACEI/ARB** | |
| Stroke | ACEI/ARB + diuretic | |
| DM ที่ UACR ≥ 30 mg/g | **ACEI/ARB** (finerenone เมื่อ ACEI/ARB เต็มขนาดแล้ว) | |
| DM + ASCVD | SGLT2i, GLP1-RA | |
| DM + HF/CKD (GFR < 60) | SGLT2i, GLP1-RA | |
| Aortic stenosis | ACEI/ARB, beta-blocker | |
| Aortic regurgitation | ACEI/ARB | |
| Obesity | ACEI/ARB | |
| OSA | MRA, ACEI/ARB | |
| Atrial fibrillation | beta-blocker, ACEI/ARB | BB ร่วมกับ non-DHP CCB |
| COPD / asthma (สไลด์หน้า 144) | **CCB** | beta-blocker (bronchospasm), ACEI (ไอ) |

### ผลข้างเคียงที่ออกสอบ
- **CCB (amlodipine) → peripheral edema** (dose-dependent, ไม่ใช่ volume overload) → **หยุด/ลดขนาด amlodipine** ไม่ใช่ให้ furosemide (สไลด์หน้า 152)
- **ACEI/ARB → Cr ขึ้น**: เช็ค Cr **ภายใน 4 สัปดาห์**หลังเริ่ม · **Cr ขึ้น ≤ 30% ให้ต่อได้** · **> 30% หยุดยาและหาสาเหตุ** (เช่น bilateral renal artery stenosis) (สไลด์หน้า 163)
- ACEI → ไอแห้ง, angioedema, hyperK (เสริม)

> โจทย์ "DM/CKD + proteinuria ให้ยาอะไร" → **ACEI/ARB (enalapril)** · ถ้าได้ ACEI เต็มขนาดอยู่แล้ว → **เพิ่ม CCB หรือ thiazide** ไม่ใช่เพิ่ม ARB (ห้าม ACEI + ARB)
''',
        figs=[fig("ht-steps", "ขั้นตอนการให้ยาลดความดัน", step_svg,
                  "แถวบนคือการเพิ่มยาทีละขั้น กล่องล่างสรุปกฎที่ข้อสอบชอบถามเวลามีโรคร่วม")],
        pearls=[
            "เริ่ม ACEI/ARB + (CCB หรือ thiazide) · ห้าม ACEI + ARB",
            "DM หรือ CKD + proteinuria → ACEI/ARB เป็นแกน",
            "COPD/asthma → CCB · เลี่ยง BB และ ACEI",
            "ขาบวมจาก amlodipine → หยุด/ลด amlodipine",
            "ACEI แล้ว Cr ขึ้น > 30% → หยุดยา + หา RAS",
        ],
        items=[
            mcq("CARDIO-03-02-1",
                "A 45-year-old man with type 2 diabetes has BP 160/90 mmHg on repeated measurements. Physical examination is normal. Urinalysis shows protein 2+ and glucose 3+. Which antihypertensive drug should be included in his regimen?",
                "Enalapril",
                ["Prazosin", "Atenolol", "Amlodipine alone", "Hydrochlorothiazide alone"],
                explain='''DM + **proteinuria** → ต้องมี **ACEI/ARB** เพื่อลด intraglomerular pressure และชะลอ diabetic kidney disease → **enalapril** แล้วเพิ่ม CCB หรือ thiazide เป็นคู่ (สไลด์หน้า 130, 136)
- Prazosin (alpha-blocker) ไม่ใช่ยาหลัก 5 กลุ่ม และไม่ป้องกันไต
- Atenolol อยู่ใน 5 กลุ่มแต่ไม่ลด proteinuria และไม่ใช่ตัวเลือกแรกเมื่อไม่มี CAD/AF/HF
- Amlodipine หรือ HCTZ เดี่ยว ลด BP ได้แต่ไม่มีผลปกป้องไตเท่า ACEI/ARB — ใช้เป็นตัวคู่''',
                pearl="DM + proteinuria = ACEI/ARB",
                topic="DM proteinuria", ref=[f"{D} หน้า 135–136"], nl=["2.3.9(4)", "B7.4(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 135"),
            mcq("CARDIO-03-02-2",
                "A patient with both type 2 diabetes and COPD with frequent wheezing needs an antihypertensive drug. He has no proteinuria. Which drug is most suitable?",
                "Amlodipine",
                ["Atenolol", "Enalapril", "Propranolol", "Carvedilol"],
                explain='''ในผู้ป่วย COPD/asthma ตามสไลด์ **prefer CCB** → **amlodipine** (สไลด์หน้า 144)
- Atenolol, propranolol และ carvedilol เป็น beta-blocker ที่อาจทำให้เกิด **bronchospasm** (propranolol และ carvedilol ไม่ selective จึงเสี่ยงยิ่งกว่า)
- Enalapril ทำให้ **ไอแห้ง** ซึ่งสับสนกับอาการ COPD — สไลด์จึงให้เลี่ยง (ถ้ามี proteinuria ร่วม ACEI/ARB ยังมีที่ใช้ เช่นเปลี่ยนเป็น ARB)''',
                pearl="COPD/asthma + HT → CCB",
                topic="COPD and HT", ref=[f"{D} หน้า 143–144"], nl=["2.3.9(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 143"),
            mcq("CARDIO-03-02-3",
                "A 58-year-old woman with type 2 diabetes and HT is taking enalapril 40 mg/day. BP is 150/100 mmHg, FBS 120 mg/dL, HbA1c 6.5%. Urine dipstick shows protein 2+. EKG shows LVH. Which medication should be added?",
                "Amlodipine",
                ["Losartan", "Atenolol", "Verapamil", "Prazosin"],
                explain='''ได้ ACEI เต็มขนาดแล้วยังไม่ถึงเป้า → เพิ่ม **CCB หรือ thiazide** ตาม step → **amlodipine** (สไลด์หน้า 126, 146)
- Losartan เป็น ARB — **ห้ามใช้ ACEI ร่วมกับ ARB** (เพิ่ม hyperK และ AKI โดยไม่ลด outcome)
- Atenolol ไม่ใช่ยาคู่ที่ prefer เมื่อไม่มี CAD/AF/HF
- Verapamil (non-DHP) ลด BP ได้น้อยกว่าและมีปัญหา bradycardia/ยาตีกัน — ตัวคู่ที่แนะนำคือ DHP-CCB
- Prazosin ไม่ใช่ยาหลัก 5 กลุ่ม''',
                pearl="ACEI เต็มขนาดแล้ว → เพิ่ม CCB/thiazide ไม่ใช่เพิ่ม ARB",
                topic="Add-on therapy", ref=[f"{D} หน้า 145–146"], nl=["2.3.9(4)", "B7.4(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 145"),
            mcq("CARDIO-03-02-4",
                "A patient with HT on enalapril 20 mg/day and amlodipine 10 mg/day presents with bilateral ankle edema. BP 120/80 mmHg. Pitting edema 1+ both feet. BUN 15 mg/dL, Cr 0.8 mg/dL. Urinalysis is normal. What is the most appropriate management?",
                "Discontinue or reduce amlodipine",
                ["Add furosemide", "Send 24-hour urine protein", "Order an echocardiogram", "Order a chest X-ray"],
                explain='''ขาบวมทั้งสองข้างในคนที่ใช้ **amlodipine ขนาดสูง** โดยไต ปัสสาวะ และ BP ปกติ = **ผลข้างเคียงของ DHP-CCB** (precapillary vasodilation) → **หยุดหรือลดขนาด amlodipine** (สไลด์หน้า 152)
- Furosemide แก้บวมจาก CCB ได้น้อยเพราะไม่ใช่ volume overload และเพิ่มความเสี่ยง hypovolemia
- 24-hr urine protein ใช้เมื่อสงสัย nephrotic syndrome แต่ UA ปกติ
- Echo และ CXR ใช้เมื่อสงสัย heart failure ซึ่งไม่มี dyspnea, JVP สูง หรือ crepitation''',
                pearl="ขาบวมจาก amlodipine → ลด/หยุดยา ไม่ใช่ให้ diuretic",
                topic="CCB side effect", ref=[f"{D} หน้า 151–152"], nl=["2.3.9(4)", "B1.7.1(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 151"),
            mcq("CARDIO-03-02-5",
                "A 75-year-old woman with diabetes is started on enalapril 10 mg/day for BP 170/110 mmHg. Two weeks later her BP is 150/100 mmHg but serum creatinine has risen from 1.0 to 1.5 mg/dL. What is the most appropriate management?",
                "Discontinue enalapril and recheck creatinine in 1 week",
                ["Continue enalapril and recheck creatinine in 1 week",
                 "Continue enalapril and recheck creatinine in 1 month",
                 "Decrease enalapril to 5 mg and recheck creatinine in 1 week",
                 "Add losartan to improve BP control"],
                explain='''Cr ขึ้นจาก 1.0 เป็น 1.5 = **เพิ่ม 50%** ซึ่ง **เกิน 30%** → **หยุด ACEI และหาสาเหตุ** (เช่น bilateral renal artery stenosis) แล้วติดตาม Cr (สไลด์หน้า 163)
- การให้ยาต่อ (ไม่ว่าจะเช็คใน 1 สัปดาห์หรือ 1 เดือน) ใช้เมื่อ Cr ขึ้น **≤ 30%**
- การลดขนาดครึ่งหนึ่งไม่ได้แก้ปัญหา hemodynamic ของ RAS และเกณฑ์ในสไลด์คือหยุด
- การเพิ่ม losartan = ACEI + ARB ซึ่งห้าม และจะทำให้ไตแย่ลงอีก''',
                pearl="ACEI/ARB: Cr ขึ้น > 30% → หยุดยา + หา RAS",
                topic="ACEI creatinine rise", ref=[f"{D} หน้า 162–163"], nl=["2.3.9(4)", "2.3.14-3(13)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 162"),
        ]),
    # ------------------------------------------------------------------ secondary HT
    sec("cardio-03-03", "Secondary hypertension",
        "อายุ < 40, resistant, hypoK, TOD ไม่สมส่วน → หา RAS, Conn, pheo, renal, coarctation, OSA", minutes=8,
        source=f"{D} หน้า 153–177", nl=["2.3.9(4)", "2.3.14-3(13)", "B11.2.5-3(10)"],
        md='''
### เมื่อไรสงสัย secondary HT (สไลด์หน้า 153)
- **อายุ < 40 ปี**
- **Resistant HT**
- **Hypertensive emergency**
- **BP ที่เคยคุมได้กลับแย่ลง**
- **Target organ damage ไม่สมกับระดับ BP** (เช่น HT grade 1 แต่ CKD รุนแรง)
- **HypoK ที่ไม่มีเหตุ หรือรุนแรง**

[[fig:sec-ht]]

### Renal artery stenosis (renovascular HT)
- สาเหตุ: **atherosclerosis** (ผู้สูงอายุ มี CAD/PAD) · **fibromuscular dysplasia** (หญิงอายุน้อย — เสริม)
- เบาะแส: **recurrent flash pulmonary edema** · **abdominal bruit** · **Cr ขึ้น ≥ 50% ภายใน 1 สัปดาห์หลังเริ่ม ACEI/ARB** · hypoK · **ไตสองข้างขนาดไม่เท่ากัน**
- Ix: **duplex ultrasonography / MRA / CTA ของ renal arteries**

### Renal parenchymal disease (เสริม จากข้อสอบในสไลด์)
- Glomerulonephritis: อายุน้อย HT + **proteinuria + hematuria** (สไลด์หน้า 167)
- CKD: ซีด บวม ผิวแห้ง HT → ตรวจ **renal function test** ก่อน (สไลด์หน้า 169)
- **ADPKD**: ประวัติครอบครัว · hematuria · ปวดสีข้าง · UTI ซ้ำ · **คลำไตโตได้** · Cr ขึ้น → **renal ultrasound**

### Primary hyperaldosteronism (Conn syndrome)
- Resistant HT · adrenal incidentaloma · **hypoK + metabolic alkalosis** (อาจอ่อนแรงต้นแขนขา — สไลด์หน้า 175–177)
- Ix: **PAC ↑, PRA ↓, aldosterone-to-renin ratio (ARR) ↑**
- **ต้องแก้ hypoK ก่อนตรวจ** ไม่งั้น aldosterone อาจต่ำลวง
- ขั้นต่อไป (เสริม): confirmatory test (saline infusion) → CT adrenal → adrenal vein sampling · Rx: adrenalectomy (unilateral) หรือ spironolactone (bilateral)

### Pheochromocytoma
- Resistant HT · **paroxysmal headache, palpitation, diaphoresis** (triad) ± tremor ซีด
- Ix: **24-hr urine fractionated metanephrines** หรือ **plasma metanephrines** (urine VMA ไม่ใช้แล้ว — เสริม)
- Rx (เสริม): **alpha-blocker ก่อน (phenoxybenzamine/doxazosin) แล้วค่อย beta-blocker** → ผ่าตัด · ห้ามให้ beta-blocker ก่อน alpha (unopposed alpha → BP พุ่ง)

### อื่น ๆ
- **Coarctation of aorta**: BP แขนสูงกว่าขา (femoral pulse เบา/ช้า) → **echocardiography**
- **Obstructive sleep apnea**: อ้วน กรน ง่วงกลางวัน → **sleep study**
- Drug-induced (เสริม): OCP, NSAIDs, steroid, decongestant
''',
        figs=[fig("sec-ht", "เบาะแสของ secondary HT และการตรวจแรก", sec_svg,
                  "อ่านจากซ้ายไปขวา: ชื่อโรค เบาะแสในโจทย์ และการตรวจที่ควรส่งเป็นอย่างแรก")],
        pearls=[
            "Flash pulmonary edema + abdominal bruit = renal artery stenosis",
            "HT + hypoK + met. alkalosis → PAC/PRA (แก้ K ก่อน)",
            "Headache + palpitation + sweating เป็นพัก ๆ → metanephrines",
            "BP แขน > ขา = coarctation → echo",
            "HT อายุน้อย + proteinuria + hematuria = GN",
        ],
        items=[
            mcq("CARDIO-03-03-1",
                "A 60-year-old man with long-standing HT and coronary artery disease presents with recurrent sudden pulmonary edema. BP left arm 190/105 mmHg, right arm 185/100 mmHg. There is no murmur, an S4 gallop, crackles at both lung bases and an abdominal bruit. What is the most likely diagnosis?",
                "Renal artery stenosis",
                ["Aortic dissection", "Coronary artery dissection", "Pheochromocytoma", "Primary hyperaldosteronism"],
                explain='''**Flash pulmonary edema + abdominal bruit** ในผู้สูงอายุที่มี atherosclerosis (CAD) = **renal artery stenosis** (สไลด์หน้า 155, 161)
- Aortic dissection ต้องมีเจ็บอกฉีกร้าวไปหลังและ BP สองแขนต่างกันมาก (ที่นี่ต่างแค่ 5 mmHg ซึ่งปกติ)
- Coronary artery dissection ทำให้ ACS ไม่ได้ทำให้ abdominal bruit
- Pheochromocytoma มีอาการเป็นพัก ๆ ปวดหัว ใจสั่น เหงื่อ
- Primary hyperaldosteronism ทำให้ hypoK ไม่มี bruit ที่ท้อง''',
                pearl="Flash pulmonary edema + abdominal bruit = RAS",
                topic="Renal artery stenosis", ref=[f"{D} หน้า 160–161"], nl=["2.3.14-3(13)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 160"),
            mcq("CARDIO-03-03-2",
                "A 70-year-old man is newly found to have HT and is started on enalapril. He returns with puffy eyelids, edema and pulmonary edema. BUN 20 mg/dL, Cr 4.1 mg/dL, urine specific gravity 1.010. What is the most appropriate investigation for the diagnosis?",
                "Doppler ultrasound of the renal arteries",
                ["Urine VMA", "Serum cortisol", "CT whole abdomen", "Renal biopsy"],
                explain='''ไตวายเฉียบพลันหลังเริ่ม ACEI + pulmonary edema ในผู้สูงอายุ = **bilateral renal artery stenosis** (ไตพึ่ง angiotensin II บีบ efferent arteriole เพื่อรักษา GFR) → ตรวจ **duplex/Doppler US ของ renal arteries** (สไลด์หน้า 155, 165)
- Urine VMA ใช้หา pheochromocytoma (ปัจจุบันใช้ metanephrines) ไม่เกี่ยวกับ AKI จาก ACEI
- Serum cortisol ใช้หา Cushing ไม่มี cushingoid feature
- CT whole abdomen ไม่ได้ประเมินหลอดเลือดไตโดยเฉพาะ และ contrast อันตรายใน Cr 4.1
- Renal biopsy ใช้แยก GN ซึ่งไม่มี active sediment''',
                pearl="AKI หลังเริ่ม ACEI → Doppler US renal arteries",
                topic="RAS investigation", ref=[f"{D} หน้า 164–165"], nl=["2.3.14-3(13)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 164"),
            mcq("CARDIO-03-03-3",
                "A 25-year-old woman has intermittent headache, lightheadedness and palpitation for 1 year. Her BP is high both sitting and supine. Examination shows tremor, sweating and pallor during an episode. What is the most appropriate initial investigation?",
                "24-hour urine fractionated metanephrines",
                ["Thyroid function test", "Plasma aldosterone to renin ratio", "Renal artery duplex ultrasound", "Overnight dexamethasone suppression test"],
                explain='''HT อายุน้อย + **paroxysmal headache, palpitation, sweating** + ซีด = **pheochromocytoma** → ตรวจ **24-hr urine fractionated metanephrines หรือ plasma metanephrines** (สไลด์หน้า 158, 171)
- TFT เหมาะเมื่อสงสัย hyperthyroidism ซึ่งอาการต่อเนื่อง (น้ำหนักลด ทนร้อนไม่ได้) และไม่ทำให้หน้าซีดเป็นพัก ๆ
- ARR ใช้หา primary aldosteronism (hypoK, resistant HT) ไม่ทำให้มีอาการเป็นพัก ๆ
- Renal duplex ใช้หา RAS (flash pulmonary edema, abdominal bruit)
- Dexamethasone suppression ใช้หา Cushing''',
                pearl="Headache + palpitation + sweating เป็นพัก ๆ = pheo → metanephrines",
                topic="Pheochromocytoma", ref=[f"{D} หน้า 170–171"], nl=["2.3.9(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 170"),
            mcq("CARDIO-03-03-4",
                "A 35-year-old man has headache for 1 month and today has weakness of all four limbs while fully conscious. BP 190/100 mmHg, PR 78/min. Proximal muscle power is grade II/V in all extremities. What is the most appropriate initial investigation?",
                "Serum electrolytes",
                ["Urine VMA", "Serum creatinine", "Electromyography", "Creatine phosphokinase"],
                explain='''HT ในคนอายุน้อย + อ่อนแรงต้นแขนขาเฉียบพลัน = นึกถึง **hypokalemic paralysis จาก primary aldosteronism** → ส่ง **serum electrolytes** เป็นอันดับแรก (ตามด้วย PAC/PRA) (สไลด์หน้า 175–177)
- Urine VMA ใช้หา pheochromocytoma ซึ่งไม่อธิบายอัมพาต
- Serum Cr ดูไตแต่ไม่อธิบายอาการอ่อนแรง
- EMG ไม่ใช่การตรวจแรกในอัมพาตเฉียบพลันที่น่าจะเป็นจาก electrolyte
- CPK ใช้หา myositis/rhabdomyolysis ซึ่งไม่ใช่ประเด็นหลัก''',
                pearl="HT + อ่อนแรงต้นแขนขา → เจาะ K (Conn)",
                topic="Primary aldosteronism", ref=[f"{D} หน้า 174–177"], nl=["B11.2.5-3(10)", "2.2.15"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 174"),
            mcq("CARDIO-03-03-5",
                "A 20-year-old man has headache and vomiting for 5 days. BP 170/105 mmHg, PR 80/min. Fundoscopy shows retinal artery narrowing. Na 145, K 3.9, Cl 99, HCO3 30 mEq/L. Urinalysis shows albumin 3+ and RBC 10–20/HPF. What is the most likely cause of his hypertension?",
                "Glomerulonephritis",
                ["Essential hypertension", "Cushing syndrome", "Renal artery stenosis", "Primary hyperaldosteronism"],
                explain='''HT ในคนอายุน้อย (ต้องหา secondary) + **proteinuria 3+ และ hematuria** = **glomerulonephritis** (สไลด์หน้า 167)
- Essential HT ไม่ทำให้ hematuria และอายุ 20 ปีต้องหาสาเหตุก่อน
- Cushing ต้องมี cushingoid feature
- RAS ไม่ทำให้มี RBC ในปัสสาวะมากขนาดนี้ และมักมี bruit/flash pulmonary edema
- Primary aldosteronism ทำให้ hypoK แต่ K ผู้ป่วยปกติ และไม่มี hematuria''',
                pearl="HT อายุน้อย + proteinuria + hematuria = GN",
                topic="Renal parenchymal HT", ref=[f"{D} หน้า 166–167"], nl=["2.3.9(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 166"),
        ]),
    # ------------------------------------------------------------------ crises
    sec("cardio-03-04", "Hypertensive crises: emergency vs urgency",
        "BP ≥ 180/110 + end-organ damage = emergency → IV nicardipine/labetalol/nitroprusside · ไม่มี → oral ลดใน 24–48 ชม.", minutes=7,
        source=f"{D} หน้า 178–189", nl=["2.2.4", "2.3.9(4)", "B7.4(4)"],
        md='''
### นิยาม (สไลด์หน้า 178)
| | HT emergency | HT urgency |
|---|---|---|
| BP | **≥ 180/110 mmHg** | **≥ 180/110 mmHg** |
| End-organ damage (acute) | **มี** | **ไม่มี** (อาจปวดหัวเล็กน้อย มึน คลื่นไส้) |
| การรักษา | **admit + IV antihypertensive** | **oral antihypertensive** ค่อย ๆ ลดใน **24–48 ชม.** นัด F/U **2–4 สัปดาห์** |

### Acute end-organ damage (เสริม)
- สมอง: hypertensive encephalopathy, stroke, ICH
- หัวใจ: **acute pulmonary edema / acute HF**, ACS, **aortic dissection**
- ไต: AKI · เลือด: MAHA · ตา: **malignant HT**
- **Malignant HT** = **bilateral retinopathy (hemorrhage, cotton wool spots, papilledema)** หรือ **AKI** หรือ **MAHA** — มีอย่างใดอย่างหนึ่งก็ได้ (สไลด์หน้า 179)

> LV heave, S4 gallop, LVH บอกว่าเป็น HT มานาน (chronic HMOD) **ไม่นับเป็น acute end-organ damage** ถ้าปอดยังใส = HT urgency (สไลด์หน้า 189)

### HT emergency: ยาและเป้าหมาย
- ยา IV: **nicardipine, labetalol, nitroprusside** (สไลด์หน้า 185)
- **Nitroprusside ควรเลี่ยงใน renal/liver impairment** (cyanide/thiocyanate สะสม) → CKD ใช้ **nicardipine** หรือ labetalol (สไลด์หน้า 187)
- HT emergency + **pulmonary edema** → **vasodilator (IV NTG, nitroprusside) + furosemide** (ดูหมวด HF)
- Aortic dissection → **IV beta-blocker ก่อน** แล้ว vasodilator (หมวด 04)
- เป้า (สไลด์หน้า 180/184 เป็นตาราง — เสริม): ลด **MAP ไม่เกิน 25% ในชั่วโมงแรก** → ~160/100–110 ใน 2–6 ชม. → ปกติใน 24–48 ชม. · ข้อยกเว้นที่ลดเร็วกว่า: aortic dissection, severe preeclampsia/eclampsia, pheochromocytoma crisis

[[fig:crisis-time]]

### HT urgency
- **Oral** anti-HT (เช่น nifedipine SR, amlodipine, captopril — เสริม) แล้ว **ค่อย ๆ ลดใน 24–48 ชม.** · F/U 2–4 สัปดาห์
- **ห้าม** nifedipine ชนิดออกฤทธิ์สั้นอมใต้ลิ้น (BP ตกเร็วเกิน → stroke/MI) (เสริม)
''',
        figs=[fig("crisis-time", "เป้าการลด BP ใน HT emergency", crisis_svg,
                  "เส้นสีหลักคือการลด BP แบบค่อยเป็นค่อยไปในภาวะ emergency ทั่วไป เส้นแดงคือ aortic dissection ที่ต้องลดเร็วกว่า")],
        pearls=[
            "≥ 180/110 + acute end-organ damage = emergency · ไม่มี = urgency",
            "Malignant HT: retinopathy ทั้งสองข้าง หรือ AKI หรือ MAHA",
            "IV nicardipine / labetalol / nitroprusside · CKD เลี่ยง nitroprusside",
            "ลด MAP ไม่เกิน 25% ในชั่วโมงแรก (เสริม)",
            "LVH/S4 ปอดใส ≠ acute end-organ damage → urgency → oral",
        ],
        items=[
            mcq("CARDIO-03-04-1",
                "A 45-year-old man has severe headache for 1 day and episodic palpitation 1–2 times a day for 1–2 months. He was previously prescribed antihypertensives for BP 200/120 mmHg but took them irregularly. Now BP 210/130 mmHg, PR 120/min, RR 22/min. Fundoscopy shows flame-shaped hemorrhages and early papilledema. What is the most appropriate management?",
                "IV sodium nitroprusside",
                ["Oral enalapril", "Oral propranolol", "Oral prazosin", "Sublingual short-acting nifedipine"],
                explain='''BP ≥ 180/110 + **retinal hemorrhage และ papilledema** = **malignant HT (HT emergency)** → ต้อง admit และให้ **IV** antihypertensive เช่น nicardipine, labetalol หรือ **nitroprusside** (สไลด์หน้า 185)
- Enalapril, propranolol และ prazosin เป็นยากิน ใช้ใน HT urgency ไม่ใช่ emergency — และ propranolol เดี่ยว ๆ อันตรายถ้าเป็น pheochromocytoma (มีใจสั่นเป็นพัก ๆ) เพราะเกิด unopposed alpha
- Short-acting nifedipine อมใต้ลิ้นทำให้ BP ตกเร็วควบคุมไม่ได้ เสี่ยง stroke/MI''',
                pearl="Papilledema/retinal hemorrhage + BP สูงมาก = malignant HT → IV drug",
                topic="Malignant HT", ref=[f"{D} หน้า 183–185"], nl=["2.2.4"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 183"),
            mcq("CARDIO-03-04-2",
                "A patient with CKD stage 4 presents with BP 220/110 mmHg and no other specific symptoms. Ophthalmoscopy shows hemorrhages, cotton-wool spots and papilledema. What is the most appropriate management?",
                "Admit and give IV nicardipine",
                ["Admit and give IV nitroprusside", "Oral nitroglycerin and observe", "Slow-release oral nifedipine", "Oral captopril and follow up in 1 week"],
                explain='''Fundoscopy มี hemorrhage + cotton wool spots + papilledema = **malignant HT (HT emergency)** → admit + IV drug · ผู้ป่วยเป็น **CKD stage 4 จึงควรเลี่ยง nitroprusside** (thiocyanate สะสม) → เลือก **IV nicardipine** (สไลด์หน้า 187)
- IV nitroprusside เป็นยาของ HT emergency แต่ไม่เหมาะใน renal impairment
- Oral NTG, nifedipine SR และ captopril เป็นการรักษาแบบ urgency ซึ่งไม่พอสำหรับ emergency''',
                pearl="HT emergency + CKD → nicardipine (เลี่ยง nitroprusside)",
                topic="HT emergency in CKD", ref=[f"{D} หน้า 186–187"], nl=["2.2.4", "B7.4(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 186"),
            mcq("CARDIO-03-04-3",
                "A 50-year-old man with CKD stage IV and poorly controlled HT comes for a routine follow-up. He has no symptoms. BP 210/130 mmHg, PR 80/min, RR 18/min. He has an LV heave, S4 gallop, no murmur, clear lungs and 1+ pitting edema. Fundoscopy shows only arteriolar narrowing. What is the most appropriate initial management?",
                "Oral nifedipine SR and observe",
                ["Admit and give IV labetalol", "Admit and give IV nicardipine", "Admit and give IV nitroprusside", "Sublingual nitroglycerin and observe"],
                explain='''BP สูงมากแต่ **ไม่มี acute end-organ damage** — LV heave และ S4 เป็นแค่ LVH จาก HT เรื้อรัง ปอดใส ไม่มี pulmonary edema และไม่มี retinopathy รุนแรง = **HT urgency** → **oral anti-HT** ค่อย ๆ ลดใน 24–48 ชม. (สไลด์หน้า 189)
- IV labetalol, nicardipine และ nitroprusside เป็นยาของ emergency การลด BP เร็วด้วย IV ในคนที่ไม่มี acute damage เสี่ยง hypoperfusion ของสมองและไต (nitroprusside ยังห้ามใน CKD)
- Nitroglycerin อมใต้ลิ้นใช้กับ angina ไม่ใช่การคุม BP ระยะยาว''',
                pearl="LVH/S4 ปอดใส = chronic ไม่ใช่ acute damage → urgency → oral",
                topic="HT urgency", ref=[f"{D} หน้า 188–189"], nl=["2.3.9(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 188"),
            mcq("CARDIO-03-04-4",
                "A 58-year-old woman with HT presents with BP 230/130 mmHg, severe headache, confusion and vomiting. CT brain shows no hemorrhage or infarct. What is the appropriate goal of blood pressure reduction in the first hour?",
                "Reduce mean arterial pressure by no more than 25%",
                ["Normalize BP to below 140/90 mmHg within the first hour",
                 "Reduce SBP to 100–120 mmHg within 20 minutes",
                 "Avoid any BP reduction for the first 24 hours",
                 "Reduce DBP to below 70 mmHg as fast as possible"],
                explain='''Hypertensive encephalopathy = HT emergency (ไม่ใช่ dissection/preeclampsia/pheo) → ลด **MAP ไม่เกิน 25% ในชั่วโมงแรก** แล้วค่อยลดต่อใน 2–6 ชม. และ 24–48 ชม. เพราะ cerebral autoregulation เลื่อนขึ้น การลดเร็วทำให้สมองขาดเลือด (เสริม — ตารางสไลด์หน้า 180 เป็นภาพ)
- ลดให้ปกติในชั่วโมงแรกเร็วเกินไป เสี่ยง ischemic stroke
- SBP 100–120 ใน 20 นาทีเป็นเป้าของ **aortic dissection**
- การไม่ลดเลยใช้กับ acute ischemic stroke ที่ไม่ได้ thrombolysis และ BP < 220/120 ไม่ใช่ encephalopathy
- DBP < 70 ต่ำเกินไปและเร็วเกินไป''',
                pearl="HT emergency: MAP ลด ≤ 25% ในชั่วโมงแรก ยกเว้น dissection",
                topic="BP lowering target", ref=[f"{D} หน้า 180, 184"], nl=["2.2.4"]),
        ]),
    ])
