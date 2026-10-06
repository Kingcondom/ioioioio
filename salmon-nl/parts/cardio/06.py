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

# ---------- fig: AHF profiles ----------
S2 = "cardio-06-02"
ahf_svg = (f'<svg viewBox="0 0 720 380">{mk(S2)}'
    + f'<path d="M150 350V30" class="ln" marker-end="url(#{S2}-a)"/>'
    + f'<path d="M150 350H700" class="ln" marker-end="url(#{S2}-a)"/>'
    + '<text x="425" y="374" text-anchor="middle" class="t2">Congestion (wet): orthopnea · ↑JVP · S3 · crepitation →</text>'
    + '<text x="12" y="104" class="t2">Perfusion ดี</text><text x="12" y="122" class="t3">warm: pulse แรง</text><text x="12" y="138" class="t3">CRT &lt; 2 วินาที</text>'
    + '<text x="12" y="262" class="t2">Hypoperfusion</text><text x="12" y="280" class="t3">cold: ปลายมือเย็น</text><text x="12" y="296" class="t3">AOC, ↓BP, PP แคบ</text>'
    + box(164, 40, 252, 140, "oksoft", [("tb", "Warm &amp; dry"), ("", "ปรับยากินเดิม"), ("t3", "(compensated)")])
    + box(430, 40, 260, 140, "misssoft", [("tb", "Warm &amp; wet (พบบ่อยสุด)"), ("", "IV furosemide"), ("", "+ vasodilator"), ("t3", "IV NTG / nitroprusside เมื่อ BP สูง")])
    + box(164, 196, 252, 140, "c1soft", [("tb", "Cold &amp; dry"), ("", "fluid challenge"), ("", "± norepinephrine")])
    + box(430, 196, 260, 140, "badsoft", [("tb", "Cold &amp; wet"), ("", "inotrope"), ("", "dobutamine, dopamine"), ("t3", "SBP < 90 หรือ hypoperfusion = unstable"), ("t3", "ห้าม beta-blocker ช่วง acute")])
    + '</svg>')
ahf_svg = ahf_svg.replace("SBP < 90", "SBP &lt; 90")

# ---------- fig: HFrEF pillars ----------
S3 = "cardio-06-03"
def pillar(x, cls, name, drug, mech):
    out = f'<rect x="{x}" y="96" width="150" height="190" rx="10" class="{cls}"/>'
    out += f'<text x="{x+75}" y="122" text-anchor="middle" class="tb">{name}</text>'
    yy = 146
    for t in drug:
        out += f'<text x="{x+75}" y="{yy}" text-anchor="middle">{t}</text>'
        yy += 19
    yy = 230
    for t in mech:
        out += f'<text x="{x+75}" y="{yy}" text-anchor="middle" class="t3">{t}</text>'
        yy += 17
    return out
hf_svg = ('<svg viewBox="0 0 720 360">'
    + '<path d="M20 86L360 14L700 86Z" class="acsoft"/>'
    + '<text x="360" y="58" text-anchor="middle" class="tb">HFrEF (LVEF ≤ 40%) — ลดการตาย</text>'
    + '<text x="360" y="76" text-anchor="middle" class="t3">"4 pillars" เริ่มให้ครบโดยเร็ว</text>'
    + pillar(20, "c1soft", "RAAS inhibitor", ["ACEI: enalapril", "ARB: losartan", "ARNI: sacubitril/", "valsartan"], ["ลด afterload,", "remodeling"])
    + pillar(195, "c2soft", "Beta-blocker", ["bisoprolol", "metoprolol", "carvedilol"], ["ลด sympathetic,", "เริ่มเมื่อ stable"])
    + pillar(370, "oksoft", "MRA", ["spironolactone"], ["block aldosterone", "ระวัง hyperK"])
    + pillar(545, "misssoft", "SGLT2 inhibitor", ["dapagliflozin", "empagliflozin"], ["natriuresis,", "ใช้ได้แม้ไม่มี DM"])
    + '<rect x="20" y="296" width="675" height="56" rx="10" class="sunk"/>'
    + '<text x="34" y="320" class="tb">Diuretic (furosemide)</text>'
    + '<text x="210" y="320">ลดอาการบวม/เหนื่อย แต่ไม่ลดการตาย — ทุก EF</text>'
    + '<text x="34" y="342" class="t3">HFmrEF 41–49% และ HFpEF ≥ 50%: diuretic + SGLT2i ± ACEI/ARB/ARNI ± MRA</text>'
    + '</svg>')

# ---------- fig: IE organism map ----------
S5 = "cardio-06-05"
ie_svg = (f'<svg viewBox="0 0 720 330">{mk(S5)}'
    + '<text x="12" y="22" class="t3">ที่มา / ปัจจัยเสี่ยง</text><text x="300" y="22" class="t3">เชื้อ</text><text x="520" y="22" class="t3">Definitive ATB</text>'
    + ''.join(
        box(10, y, 250, 44, cls, [("tb", a)], center=False)
        + f'<path d="M260 {y+22}H286" class="ln" marker-end="url(#{S5}-a)"/>'
        + box(290, y, 210, 44, "box", [("", b)], center=False)
        + f'<path d="M500 {y+22}H516" class="ln" marker-end="url(#{S5}-a)"/>'
        + box(520, y, 192, 44, cls, [("ta", c)], center=False)
        for y, cls, a, b, c in (
            (32, "oksoft", "ฟันผุ / ทำฟัน", "Viridans strep, HACEK", "PGS / amox / CTX"),
            (86, "badsoft", "IVDU (ลิ้น tricuspid)", "S. aureus (MSSA)", "Cloxacillin / cefazolin"),
            (140, "badsoft", "MRSA / early PVE", "MRSA", "Vancomycin"),
            (194, "misssoft", "มะเร็งลำไส้ใหญ่", "S. bovis (gallolyticus)", "PGS / amox / CTX"),
            (248, "c1soft", "GU/GI procedure (เสริม)", "Enterococcus", "Amp + genta หรือ CTX"),
        ))
    + '<text x="12" y="320" class="t3">PGS = penicillin G sodium · CTX = ceftriaxone · S. bovis → ส่ง colonoscopy</text>'
    + '</svg>')


LECTURE = lecture("06", "Heart failure, digoxin toxicity & infective endocarditis",
    subtitle="AHF profiles · HFrEF drugs · digoxin toxicity · IE diagnosis & antibiotics",
    objectives=[
        "จัดผู้ป่วย acute HF เป็น warm/cold–wet/dry และเลือกการรักษาได้ รวมถึง HT emergency with pulmonary edema",
        "สั่งยา chronic HFrEF ครบ 4 กลุ่มและรู้ว่ายาใดห้ามในช่วง acute",
        "บอกปัจจัยกระตุ้นและการรักษา digoxin toxicity ได้",
        "วินิจฉัย IE จากอาการ เชื่อมปัจจัยเสี่ยงกับเชื้อ และเลือก antibiotic/prophylaxis ได้",
    ],
    sections=[
    # ------------------------------------------------------------------ HF basics
    sec("cardio-06-01", "Heart failure: causes & clinical features",
        "Left HF = pulmonary congestion · right HF = fluid overload · S3, pulsus alternans · NYHA class", minutes=5,
        source=f"{D} หน้า 277–279, 318", nl=["2.3.9(5)", "B7.2.5(2)"],
        md='''
### สาเหตุ
- **Coronary artery disease** · **HT, DM** · valvular heart disease · arrhythmia · cardiomyopathies · constrictive pericarditis · COPD, smoking
- **Cardiac beriberi** (high-output HF จาก thiamine deficiency ในคนดื่มสุราเรื้อรัง) → **IV thiamine** (สไลด์หน้า 318)

### อาการและอาการแสดง
- ทั่วไป: **S3/S4 gallop**, **pulsus alternans** (pulse แรงสลับเบา)
- **Left-sided HF (pulmonary congestion)**: dyspnea, **orthopnea, PND**, cardiac asthma (wheeze), **crepitation ที่ฐานปอดทั้งสองข้าง**, cardiomegaly (PMI เลื่อนลงซ้าย)
- **Right-sided HF (fluid overload)**: **pitting edema**, **↑JVP** (> 3 cm เหนือ sternal angle หรือ > 8 cmH2O), Kussmaul sign, hepatic congestion, **hepatojugular reflux**

### NYHA functional class (สไลด์หน้า 279 เป็นตาราง — เสริม)
| Class | อาการ |
|---|---|
| I | ไม่มีอาการเมื่อทำกิจกรรมปกติ |
| II | เหนื่อยเมื่อทำกิจกรรมปกติ (เล็กน้อย) |
| III | เหนื่อยเมื่อทำกิจกรรมน้อยกว่าปกติ สบายเฉพาะตอนพัก |
| IV | มีอาการแม้ขณะพัก |

### แบ่งตาม LVEF (สไลด์หน้า 291, 294)
- **HFrEF: LVEF ≤ 40%** · **HFmrEF: 41–49%** · **HFpEF: ≥ 50%**
''',
        pearls=[
            "Orthopnea, PND, crepitation = left HF · JVP สูง edema HJR = right HF",
            "JVP สูง = > 3 cm เหนือ sternal angle (> 8 cmH2O)",
            "Pulsus alternans = LV systolic dysfunction รุนแรง",
            "ดื่มสุราเรื้อรัง + HF + S3 → นึกถึง cardiac beriberi → thiamine",
        ],
        items=[
            mcq("CARDIO-06-01-1",
                "A 50-year-old man has dyspnea on exertion and edema for 1 week. He has drunk beer every day for 25 years. BP 120/70 mmHg. There are fine crepitations at both lung bases, the PMI is at the 6th ICS 1 cm lateral to the MCL and an S3 gallop is present. In addition to an IV diuretic, what is the next management?",
                "IV thiamine",
                ["IV dobutamine", "IV nitroprusside", "IV digoxin", "IV atropine"],
                explain='''Chronic alcoholism → **thiamine deficiency → cardiac (wet) beriberi** ซึ่งเป็น high-output HF ที่รักษาได้ด้วย **IV thiamine** (สไลด์หน้า 318)
- Dobutamine ใช้เมื่อ cold & wet (hypoperfusion) ผู้ป่วย BP ปกติ
- Nitroprusside ใช้เมื่อ BP สูง (HT emergency with pulmonary edema)
- Digoxin ใช้ใน HF ที่มี AF หรือ HFrEF ที่ยังมีอาการ ไม่ได้แก้สาเหตุ
- Atropine ใช้ใน symptomatic bradycardia''',
                pearl="HF ในคนดื่มสุรา → ให้ thiamine",
                topic="Cardiac beriberi", ref=[f"{D} หน้า 317–318"], nl=["2.3.9(5)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 317"),
            mcq("CARDIO-06-01-2",
                "A 68-year-old woman with ischemic cardiomyopathy is comfortable at rest but becomes breathless walking across a room or dressing, which is less than ordinary activity. What is her NYHA functional class?",
                "Class III",
                ["Class I", "Class II", "Class IV", "Stage C only, NYHA class cannot be assigned"],
                explain='''สบายตอนพัก แต่เหนื่อยเมื่อทำกิจกรรม **น้อยกว่าปกติ** (เดินในห้อง แต่งตัว) = **NYHA class III** (เสริม — ตารางสไลด์หน้า 279 เป็นภาพ)
- Class I ไม่มีอาการเลย
- Class II เหนื่อยเมื่อทำกิจกรรมปกติ เช่นขึ้นบันได 2 ชั้น เดินเร็ว
- Class IV มีอาการแม้ขณะพัก
- ACC/AHA stage เป็นอีกระบบหนึ่ง (A–D) ใช้ร่วมกับ NYHA ได้ ไม่ได้แทนกัน''',
                pearl="NYHA III = เหนื่อยเมื่อทำน้อยกว่าปกติ สบายตอนพัก",
                topic="NYHA class", ref=[f"{D} หน้า 279"], nl=["2.3.9(5)"]),
            mcq("CARDIO-06-01-3",
                "A 72-year-old man has progressive dyspnea. Which finding most specifically indicates elevated right-sided filling pressure?",
                "JVP 5 cm above the sternal angle with a positive hepatojugular reflux",
                ["Bilateral basal crepitation", "Paroxysmal nocturnal dyspnea", "Wheezing at night (cardiac asthma)", "Cardiomegaly on chest X-ray"],
                explain='''**JVP > 3 cm เหนือ sternal angle** และ **hepatojugular reflux** สะท้อนความดันฝั่งขวา (right-sided HF/fluid overload) โดยตรง (สไลด์หน้า 278)
- Crepitation, PND และ cardiac asthma เป็นลักษณะของ **left-sided HF** (pulmonary congestion)
- Cardiomegaly บอกว่าหัวใจโต แต่ไม่ได้บอกความดันฝั่งขวา''',
                pearl="JVP + HJR = right side · crepitation/PND/orthopnea = left side",
                topic="Left vs right HF", ref=[f"{D} หน้า 278"], nl=["2.3.9(5)"]),
        ]),
    # ------------------------------------------------------------------ AHF
    sec("cardio-06-02", "Acute heart failure",
        "ABC + หา CHAMP → warm-wet: IV furosemide (+ vasodilator) · cold-wet: inotrope · HT + pulmonary edema: vasodilator + furosemide", minutes=9,
        source=f"{D} หน้า 280–288, 295–316", nl=["2.2.5", "2.3.9(5)", "B6.2.6(1)"],
        md='''
### นิยามและการประเมิน
Acute HF = อาการ HF เกิดใหม่หรือแย่ลงอย่างรวดเร็ว
- **Adequate perfusion (warm)**: pulse แรง ผิวอุ่น capillary refill < 2 วินาที
- **Hypoperfusion (cold)**: pulse pressure แคบ ปลายมือเท้าเย็น cyanosis skin mottling **AOC ↓BP**
- **Congestion (wet)**: orthopnea, ↑JVP, S3 gallop, crepitation

[[fig:ahf-profile]]

### Investigation
- **CXR**: perihilar alveolar infiltration (**bat wing**), **Kerley B lines**, cardiomegaly, cephalization, basal interstitial infiltration, pleural effusion
- **Echo**: LV systolic/diastolic dysfunction · ประเมิน EF
- **↑BNP**
- **EKG** และ **troponin**: R/O ACS, arrhythmia

### การรักษา
1. **ABC** · **O2 ถ้า SpO2 < 90%** · **NIPPV** ถ้า respiratory distress · **ETT** ถ้า NIPPV ไม่ดีขึ้น
2. **หาและรักษาสาเหตุเฉียบพลัน "CHAMP"**: **C**oronary syndrome · **H**ypertensive emergency · **A**rrhythmia · acute **M**echanical cause · **P**ulmonary embolism
3. รักษาตาม profile:

| สถานะ | Profile | การรักษา |
|---|---|---|
| Stable (SBP > 90, ไม่มี hypoperfusion) | Warm & dry | ปรับยากิน |
| | **Warm & wet** | **IV furosemide** ± vasodilator (IV NTG, nitroprusside) |
| Unstable (SBP < 90 หรือ hypoperfusion) | **Cold & wet** | **Inotrope (dobutamine, dopamine)** |
| | Cold & dry | **Fluid challenge**, vasopressor (norepinephrine) |
| **HT emergency + pulmonary edema** | | **Vasodilator (IV NTG, nitroprusside) + furosemide** |

4. **Supportive**: จำกัดน้ำและเกลือ · รักษา precipitating cause · ติดตามอาการ CXR urine output

> **ห้าม beta-blocker ใน acute HF** (ใช้ใน chronic HF) — สไลด์หน้า 316 · AF + acute HF ที่ไม่รุนแรงพอจะ cardioversion → rate control ด้วย **digoxin หรือ amiodarone** (ไม่ใช่ diltiazem/verapamil/esmolol) — สไลด์หน้า 298

### เลือก vasodilator ตัวไหน (เสริม)
- **IV NTG** ใช้บ่อยสุด โดยเฉพาะมี ischemia ร่วม · ขนาด 10–20 mcg/min ปรับขึ้น
- **Nitroprusside** แรงกว่า ใช้เมื่อ BP สูงมาก · เลี่ยงใน renal/liver impairment
- Furosemide IV: เดิมไม่เคยได้ 20–40 mg · เคยได้ยากินให้ IV ≥ ขนาดที่กินต่อวัน
''',
        figs=[fig("ahf-profile", "Acute HF profile (warm/cold × wet/dry)", ahf_svg,
                  "แกนนอนคือ congestion แกนตั้งคือ perfusion — ผู้ป่วยส่วนใหญ่อยู่ช่องขวาบน (warm & wet) และรักษาด้วย IV furosemide")],
        pearls=[
            "Warm & wet → IV furosemide (+ vasodilator ถ้า BP สูง)",
            "Cold & wet → inotrope (dobutamine) · cold & dry → fluid ± norepinephrine",
            "HT emergency + pulmonary edema → IV NTG/nitroprusside + furosemide",
            "ห้าม beta-blocker ใน acute HF",
            "AF + acute HF → digoxin/amiodarone ไม่ใช่ non-DHP CCB",
        ],
        items=[
            mcq("CARDIO-06-02-1",
                "A 50-year-old man has shortness of breath, chest tightness and cough with frothy sputum for 1 day. BP 160/100 mmHg, PR 120/min. He has mild cyanosis, an S3 gallop and fine crepitations in both lungs. What is the most appropriate first step in management?",
                "IV furosemide",
                ["Digoxin", "Propranolol", "Oral nicardipine", "Nitroprusside without a diuretic"],
                explain='''Acute HF แบบ **warm & wet** (BP ดี มี congestion) ที่ BP < 180 → ขั้นแรกคือ **IV furosemide** ลด congestion (สไลด์หน้า 286, 300)
- Digoxin ไม่ใช่ยาแรกของ acute pulmonary edema ที่ไม่มี AF
- Propranolol (beta-blocker) **ห้ามใน acute HF** ทำให้การบีบตัวลดลง
- Nicardipine เป็น vasodilator สำหรับ HT emergency ที่ไม่ใช่ pulmonary edema เป็นหลัก
- Nitroprusside ใช้ใน HT emergency with pulmonary edema (BP สูงมาก ≥ 180/110) และต้องให้ร่วมกับ furosemide''',
                pearl="Acute pulmonary edema BP ไม่สูงมาก → IV furosemide ก่อน",
                topic="Warm and wet", ref=[f"{D} หน้า 299–300"], nl=["2.2.5"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 299"),
            mcq("CARDIO-06-02-2",
                "A 55-year-old man has chest pain and shortness of breath for 30 minutes. BP 80/40 mmHg, PR 90/min, SpO2 89%. He has crepitation in both lungs and capillary refill > 4 seconds. What is the most appropriate initial management?",
                "Inotropic drug",
                ["IV fluid loading", "Diuretics", "Opioid", "Beta-blocker"],
                explain='''Hypotension + capillary refill ช้า (hypoperfusion = **cold**) + crepitation (**wet**) = **cold & wet (cardiogenic shock)** → **inotrope (dobutamine, dopamine)** (สไลด์หน้า 287, 306)
- IV fluid loading ทำให้ pulmonary edema แย่ลง (ใช้ใน cold & dry)
- Diuretics ใน BP 80/40 ทำให้ BP ตกลงอีก ต้องพยุง perfusion ก่อน
- Opioid กดการหายใจและลด BP
- Beta-blocker ห้ามใน acute HF/shock''',
                pearl="Cold & wet = cardiogenic shock → inotrope",
                topic="Cold and wet", ref=[f"{D} หน้า 305–306"], nl=["2.2.7", "2.2.5"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 305"),
            mcq("CARDIO-06-02-3",
                "A 70-year-old woman with poorly controlled HT has dyspnea for 1 day. BP 220/110 mmHg, PR 110/min, RR 24/min. The PMI is at the 6th ICS with a gallop, crepitation in both lungs and leg edema. Which antihypertensive drug is most appropriate?",
                "IV nitroprusside",
                ["HCTZ", "IV labetalol", "Oral captopril", "Oral amlodipine"],
                explain='''BP ≥ 180/110 + **acute pulmonary edema** = **HT emergency with pulmonary edema** → **vasodilator (IV NTG หรือ nitroprusside) + furosemide** (สไลด์หน้า 287, 310)
- HCTZ เป็น diuretic อ่อน ทางปาก ไม่เหมาะกับภาวะฉุกเฉิน
- Labetalol มีฤทธิ์ beta-blocker ทำให้การบีบตัวลดลงใน acute HF — ไม่ใช่ตัวเลือกในภาวะนี้
- Captopril และ amlodipine เป็นยากินสำหรับ HT urgency''',
                pearl="HT emergency + pulmonary edema → IV NTG/nitroprusside + furosemide",
                topic="HT emergency with pulmonary edema", ref=[f"{D} หน้า 309–310"], nl=["2.2.5", "2.2.4"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 309"),
            mcq("CARDIO-06-02-4",
                "A 68-year-old man with poorly controlled HT has progressive dyspnea on exertion and palpitation for 2 weeks. BP 160/95 mmHg, irregular pulse 140/min, RR 24/min. Neck veins are engorged and there are fine crepitations in both lungs. EKG shows atrial fibrillation. In addition to IV furosemide, which drug should be given?",
                "IV digoxin",
                ["IV esmolol", "IV verapamil", "IV diltiazem", "IV nitroprusside"],
                explain='''**AF with RVR ที่ทำให้เกิด acute HF** แต่ยัง stable → rate control ด้วยยาที่ไม่กดการบีบตัว คือ **digoxin** (หรือ amiodarone) (สไลด์หน้า 298)
- Esmolol (beta-blocker) และ verapamil/diltiazem (non-DHP CCB) มีฤทธิ์ negative inotrope ทำให้ HF แย่ลงในช่วง acute decompensation
- Nitroprusside ใช้เมื่อเป็น HT emergency (≥ 180/110) — BP 160/95 ยังไม่ใช่ และไม่ได้คุม rate''',
                pearl="AF + acute HF → digoxin/amiodarone",
                topic="AF with acute HF", ref=[f"{D} หน้า 297–298"], nl=["2.3.9(1)", "2.3.9(5)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 297"),
            mcq("CARDIO-06-02-5",
                "A 66-year-old man presents with dyspnea, chest pain and inability to lie flat. JVP is raised and there are crepitations in both lungs. BP 150/90 mmHg. Which drug is contraindicated at this time?",
                "Beta-blocker",
                ["Aspirin", "Clopidogrel", "Nitroglycerin", "IV furosemide"],
                explain='''ผู้ป่วยเป็น **acute HF** (orthopnea, JVP สูง, crepitation) · **beta-blocker ใช้ใน chronic HF แต่ห้ามเริ่มในช่วง acute HF** เพราะกดการบีบตัวของหัวใจ (สไลด์หน้า 316)
- Aspirin และ clopidogrel ใช้ได้ถ้ามี ACS เป็นสาเหตุ
- Nitroglycerin เป็น vasodilator ที่ใช้รักษา congestion และ ischemia ได้ (BP 150/90)
- Furosemide เป็นยาหลักของ congestion''',
                pearl="Acute HF: ห้ามเริ่ม beta-blocker",
                topic="BB in acute HF", ref=[f"{D} หน้า 315–316"], nl=["2.3.9(5)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 315"),
        ]),
    # ------------------------------------------------------------------ chronic HF
    sec("cardio-06-03", "Chronic heart failure management",
        "HFrEF ≤ 40%: ACEI/ARB/ARNI + BB + MRA + SGLT2i (+ diuretic) · HFmrEF/HFpEF: diuretic + SGLT2i", minutes=6,
        source=f"{D} หน้า 289–294", nl=["2.3.9(5)", "B7.2.5(2)", "B9.4(1)"],
        md='''
### HFrEF (LVEF ≤ 40%) — ตามสไลด์หน้า 291
- **Diuretics: furosemide** (บรรเทาอาการ)
- **RAAS inhibitors**: ACEI (enalapril) · ARB (losartan) · **ARNI (sacubitril/valsartan)**
- **Beta-blockers: bisoprolol, metoprolol (succinate), carvedilol**
- **SGLT2 inhibitors: dapagliflozin, empagliflozin**
- **MRA: spironolactone**

[[fig:hfref-pillars]]

### HFmrEF (41–49%) และ HFpEF (≥ 50%) — สไลด์หน้า 294
- **Diuretic (furosemide)**
- **SGLT2 inhibitor**
- **± ACEI/ARB/ARNI, ± MRA**

### ข้อควรรู้ (เสริม)
- 4 กลุ่มหลัก (ACEI/ARB/ARNI, BB, MRA, SGLT2i) **ลดการตาย** — diuretic ลดแค่อาการ
- ห้ามใช้ ACEI ร่วมกับ ARNI (เว้น 36 ชม. — angioedema) · ห้าม ACEI + ARB + MRA พร้อมกัน (hyperK)
- MRA: ระวัง K > 5.0 และ eGFR < 30
- Beta-blocker เริ่มขนาดต่ำเมื่อ euvolemic/stable ค่อย ๆ เพิ่ม — **ไม่เริ่มขณะ acute decompensation**
- **ห้าม non-DHP CCB (verapamil, diltiazem) ใน HFrEF** (ตาราง HT สไลด์หน้า 129) · เลี่ยง NSAIDs, TZD
- Digoxin: ลดการ admit แต่ไม่ลดการตาย ใช้เมื่อยังมีอาการหรือมี AF
- Hydralazine + isosorbide dinitrate: ทางเลือกเมื่อใช้ ACEI/ARB/ARNI ไม่ได้
''',
        figs=[fig("hfref-pillars", "ยาหลัก 4 กลุ่มของ HFrEF", hf_svg,
                  "เสาทั้งสี่คือยาที่ลดการตายใน HFrEF ต้องให้ครบ ส่วน diuretic ที่ฐานใช้ลดอาการบวมในทุกระดับ EF")],
        pearls=[
            "HFrEF = ACEI/ARB/ARNI + BB + MRA + SGLT2i",
            "HFpEF/HFmrEF = diuretic + SGLT2i ± RAASi ± MRA",
            "BB ใน HF: bisoprolol, metoprolol, carvedilol เท่านั้น",
            "ห้าม verapamil/diltiazem ใน HFrEF",
            "Diuretic ลดอาการ ไม่ลดการตาย (เสริม)",
        ],
        items=[
            mcq("CARDIO-06-03-1",
                "A 62-year-old man with ischemic cardiomyopathy and LVEF 30% is now euvolemic on furosemide, enalapril and spironolactone. BP 118/72 mmHg, HR 92/min in sinus rhythm, K 4.4 mEq/L, eGFR 65 mL/min/1.73m2. Which medication should be added to reduce mortality?",
                "Bisoprolol",
                ["Verapamil", "Atenolol", "Amlodipine", "Digoxin"],
                explain='''HFrEF ที่ยังขาด **beta-blocker** ซึ่งเป็นหนึ่งใน 4 กลุ่มที่ลดการตาย → เพิ่ม **bisoprolol** (หรือ metoprolol succinate/carvedilol) เมื่อ euvolemic และ HR ยังเร็ว (สไลด์หน้า 291) — และควรเพิ่ม SGLT2i ด้วย
- Verapamil เป็น non-DHP CCB กดการบีบตัว **ห้ามใน HFrEF**
- Atenolol ไม่มีข้อมูลลดการตายใน HF ไม่ได้อยู่ในรายชื่อ BB ของ HF
- Amlodipine ปลอดภัยใน HF แต่ไม่ลดการตาย
- Digoxin ลดการนอน รพ. ไม่ลดการตาย''',
                pearl="BB ที่ใช้ใน HF: bisoprolol, metoprolol succinate, carvedilol",
                topic="HFrEF beta-blocker", ref=[f"{D} หน้า 291"], nl=["2.3.9(5)"]),
            mcq("CARDIO-06-03-2",
                "A 78-year-old woman has dyspnea on exertion and ankle edema. Echocardiogram shows LVEF 58% with diastolic dysfunction and LVH. NT-proBNP is elevated. She has no diabetes. After a loop diuretic, which drug has the strongest evidence to reduce HF hospitalization?",
                "Empagliflozin",
                ["Bisoprolol", "Digoxin", "Ivabradine", "Verapamil"],
                explain='''**HFpEF (LVEF ≥ 50%)** → นอกจาก diuretic แล้ว ยาที่มีหลักฐานลดการนอน รพ. คือ **SGLT2 inhibitor (empagliflozin, dapagliflozin)** ใช้ได้แม้ไม่มี DM (สไลด์หน้า 294)
- Bisoprolol ไม่มีหลักฐานใน HFpEF เว้นมีข้อบ่งชี้อื่น
- Digoxin ไม่ได้ช่วยใน HFpEF ที่ sinus rhythm
- Ivabradine ใช้ใน HFrEF ที่ HR สูงใน sinus rhythm (เสริม)
- Verapamil ไม่ลด HF hospitalization''',
                pearl="HFpEF: diuretic + SGLT2i",
                topic="HFpEF treatment", ref=[f"{D} หน้า 294"], nl=["2.3.9(5)"]),
            mcq("CARDIO-06-03-3",
                "A 60-year-old man with HFrEF (LVEF 30%) has been stable on lisinopril. His cardiologist wants to switch him to sacubitril/valsartan. What is the most important precaution when switching?",
                "Stop the ACE inhibitor at least 36 hours before starting sacubitril/valsartan",
                ["Give both drugs together for 1 week to avoid rebound",
                 "Stop spironolactone permanently before starting",
                 "Check serum digoxin level before switching",
                 "Start at the maximum dose to achieve benefit quickly"],
                explain='''ACEI + neprilysin inhibitor (sacubitril) ทำให้ bradykinin สะสม → **angioedema** จึงต้อง **หยุด ACEI อย่างน้อย 36 ชม.** ก่อนเริ่ม ARNI (เสริม · ARNI อยู่ในรายการยาของ HFrEF สไลด์หน้า 291)
- การให้ ACEI ร่วมกับ ARNI ห้ามเด็ดขาด
- Spironolactone (MRA) ให้ต่อได้ เป็นหนึ่งใน 4 pillars (ติดตาม K)
- ระดับ digoxin ไม่เกี่ยวกับการเปลี่ยนยานี้
- ARNI เริ่มขนาดต่ำแล้วค่อยเพิ่ม เพื่อป้องกัน hypotension''',
                pearl="ACEI → ARNI: เว้น 36 ชม. (angioedema)",
                topic="ARNI switch", ref=[f"{D} หน้า 291"], nl=["2.3.9(5)", "B1.7.1(4)"]),
        ]),
    # ------------------------------------------------------------------ digoxin
    sec("cardio-06-04", "Digoxin toxicity",
        "HypoK (จาก furosemide), ไตเสื่อม, ยา verapamil/amiodarone → N/V, ตามัว เห็นสีเพี้ยน, arrhythmia → หยุดยา แก้ K, DigiFab", minutes=5,
        source=f"{D} หน้า 319–322", nl=["B1.7.1(4)", "2.2.46", "2.3.9(1)"],
        md='''
### ปัจจัยเสี่ยง
- **Electrolyte imbalance**: **hypoK** (พบบ่อยสุด — มักจาก **furosemide/thiazide**), hyperK, hypoMg, **hyperCa** (และ ↑Na ตามสไลด์)
- **Renal failure** (digoxin ขับทางไต), **volume depletion**, ผู้สูงอายุ
- **Drug interaction: verapamil, diltiazem, amiodarone** (เพิ่มระดับ digoxin) (และ macrolide — เสริม)

### อาการ
- GI: **คลื่นไส้ อาเจียน เบื่ออาหาร** ท้องเสีย ปวดท้อง
- **Arrhythmia**
- Neuro: สับสน อ่อนแรง disorientation
- **Visual disturbance**: ตามัว เห็นสีเหลือง-เขียว (xanthopsia) หรือรัศมีรอบแสง (เสริม)

### Investigation
- **EKG**: bradyarrhythmia (AV block, sinus brady) หรือ tachyarrhythmia — ตัวที่ชวนคิดมากคือ **PAT with block, bidirectional VT, frequent PVC/bigeminy** (เสริม) · "scooped ST" (reverse tick) เป็นผลของยา ไม่ได้แปลว่า toxic
- **LAB: ↑serum digoxin, ↑K** (acute toxicity → hyperK บ่งพยากรณ์ไม่ดี เพราะ Na/K-ATPase ถูกยับยั้ง)

### การรักษา
- **หยุด digoxin และแก้ precipitating cause**
- **แก้ electrolyte** (K, Mg) — ระวังอย่าให้ Ca IV ในภาวะ hyperK จาก digoxin (เสริม: เดิมเชื่อเรื่อง "stone heart")
- **Digoxin immune Fab (DigiFab)** เมื่อ life-threatening (arrhythmia อันตราย, K > 5–6 ใน acute, end-organ dysfunction — เสริม)
- Monitor EKG
  - **Bradyarrhythmia / AV block: atropine**
  - **Ventricular arrhythmia: phenytoin / lidocaine**
''',
        pearls=[
            "Furosemide → hypoK → digoxin toxicity",
            "Verapamil, diltiazem, amiodarone เพิ่มระดับ digoxin",
            "คลื่นไส้ + เห็นสีผิดปกติ + bradycardia ในคนกิน digoxin = toxicity",
            "Life-threatening → DigiFab · brady → atropine · VT → lidocaine/phenytoin",
        ],
        items=[
            mcq("CARDIO-06-04-1",
                "A 32-year-old woman with rheumatic mitral stenosis takes digoxin 0.25 mg once daily and furosemide 40 mg once daily. For 3 days she has worsening dyspnea, nausea, vomiting, anorexia and abnormal colour vision. BP 100/70 mmHg, PR 50/min. She has fine crepitation in both lungs, loud S1 and a diastolic murmur at the apex. What is the most likely precipitating cause of her symptoms?",
                "Hypokalemia",
                ["Hyponatremia", "Drug interaction", "Volume depletion", "Metabolic alkalosis"],
                explain='''อาการ GI + การมองเห็นสีผิดปกติ + bradycardia ในคนกิน digoxin = **digoxin toxicity** · ปัจจัยกระตุ้นที่ชัดที่สุดคือ **furosemide → hypokalemia** (K ต่ำทำให้ digoxin จับ Na/K-ATPase ได้มากขึ้น) (สไลด์หน้า 322)
- Hyponatremia ไม่ได้เพิ่มความเป็นพิษของ digoxin โดยตรง
- Drug interaction ต้องมียาอย่าง verapamil/amiodarone ซึ่งผู้ป่วยไม่ได้ใช้
- Volume depletion เป็นปัจจัยได้ แต่ผู้ป่วยมี crepitation (ยังมี congestion) จึงไม่น่าใช่
- Metabolic alkalosis เกิดร่วมกับ diuretic ได้ แต่ตัวที่ทำให้ digoxin toxic คือ hypoK''',
                pearl="Digoxin + furosemide → hypoK → toxicity",
                topic="Digoxin toxicity precipitant", ref=[f"{D} หน้า 321–322"], nl=["B1.7.1(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 321"),
            mcq("CARDIO-06-04-2",
                "A 76-year-old woman with AF on digoxin is admitted with vomiting and confusion. HR 38/min with complete heart block; BP 82/50 mmHg. Serum digoxin is markedly elevated and K is 6.4 mEq/L. Atropine has been given without improvement. What is the most appropriate specific treatment?",
                "Digoxin immune Fab",
                ["IV calcium gluconate", "IV amiodarone", "Hemodialysis to remove digoxin", "IV verapamil"],
                explain='''Digoxin toxicity ที่ **life-threatening** (CHB + hypotension + hyperK) → **digoxin immune Fab (DigiFab)** ตามสไลด์หน้า 320 ซึ่งจะแก้ทั้ง arrhythmia และ hyperK
- IV calcium ใน hyperK จาก digoxin เคยถือว่าห้าม (stone heart) และไม่แก้ต้นเหตุ — ปัจจุบันไม่เป็นอันตรายชัดเจนแต่ไม่ใช่การรักษาหลัก (เสริม)
- Amiodarone และ verapamil เพิ่มระดับ digoxin และกด AV node ให้แย่ลง
- Hemodialysis เอา digoxin ออกไม่ได้เพราะ volume of distribution สูงมาก (เสริม)''',
                pearl="Digoxin toxicity ที่อันตราย = DigiFab",
                topic="Digoxin toxicity treatment", ref=[f"{D} หน้า 319–320"], nl=["B1.7.1(4)", "2.2.46"]),
            mcq("CARDIO-06-04-3",
                "A 70-year-old man on long-term digoxin for heart failure is started on a new drug for AF rhythm control. Two weeks later he develops nausea and xanthopsia with a serum digoxin level twice the previous value. Which newly added drug most likely caused this?",
                "Amiodarone",
                ["Bisoprolol", "Apixaban", "Atorvastatin", "Furosemide 20 mg in the morning"],
                explain='''**Amiodarone** (รวมถึง verapamil, diltiazem) ลดการขับ digoxin ทำให้ระดับยาเพิ่มเกือบเท่าตัว → ต้องลดขนาด digoxin ครึ่งหนึ่งเมื่อเริ่ม amiodarone (สไลด์หน้า 319 + เสริม)
- Bisoprolol เสริมฤทธิ์ bradycardia ได้แต่ไม่เพิ่มระดับ digoxin
- Apixaban และ atorvastatin ไม่มีผลต่อระดับ digoxin อย่างมีนัยสำคัญ
- Furosemide ทำให้ hypoK (เพิ่มความเป็นพิษ) แต่ไม่ได้ทำให้ระดับ digoxin สูงเป็นสองเท่า และไม่ใช่ยา rhythm control''',
                pearl="Amiodarone/verapamil/diltiazem → digoxin สูงขึ้น",
                topic="Digoxin interaction", ref=[f"{D} หน้า 319"], nl=["B1.7.1(4)"]),
        ]),
    # ------------------------------------------------------------------ IE
    sec("cardio-06-05", "Infective endocarditis (IE)",
        "ไข้ + murmur ใหม่ + embolic sign → blood culture × 3 + echo (Duke) · IVDU = S. aureus ที่ TV → cloxacillin", minutes=9,
        source=f"{D} หน้า 323–353", nl=["2.3.9-3(5)", "B7.2.2-3(2)"],
        md='''
### นิยามและปัจจัยเสี่ยง
IE = การติดเชื้อของ endocardium (ส่วนใหญ่ที่ลิ้นหัวใจ)
- **Acquired valvular disease** (rheumatic) · congenital heart disease · **prosthetic heart valve** · CIED · **IVDU** · hemodialysis · **poor dental status / dental procedures**

### เชื้อตามปัจจัยเสี่ยง
| ปัจจัย | เชื้อ |
|---|---|
| ฟันผุ / ทำฟัน | **Viridans streptococci**, HACEK |
| **IVDU** (มักลิ้น **tricuspid** → TR) | **S. aureus** |
| สัมพันธ์กับ **มะเร็งลำไส้ใหญ่** | **S. bovis (S. gallolyticus)** → ส่ง colonoscopy |
| Early PVE (< 1 ปีหลังผ่าตัด) | MRSA, enterococci, gram-negative |

[[fig:ie-bugs]]

### อาการ
- **Constitutional**: ไข้ อ่อนเพลีย น้ำหนักลด
- **Murmur ใหม่ หรือเปลี่ยนไป** · **heart failure** (ลิ้นรั่วเฉียบพลัน)
- **Extracardiac**
  - **Petechiae** (conjunctiva, เพดานปาก), **splinter hemorrhage** (ใต้เล็บ)
  - **Janeway lesions**: ผื่นแดง **ไม่เจ็บ** ที่ฝ่ามือฝ่าเท้า (septic emboli)
  - **Osler nodes**: ตุ่ม **เจ็บ** ที่ปลายนิ้วมือนิ้วเท้า (immune complex)
  - **Roth spots**: จุดเลือดออกที่จอตา ตรงกลางซีด
  - **Septic embolic stroke** · glomerulonephritis · arthritis
- Right-sided IE (IVDU): ไข้ ไอ ไอเป็นเลือด เหนื่อย + CXR **multiple nodular/patchy infiltrates** (septic pulmonary emboli) + murmur TR ที่ LLSB

### การวินิจฉัย — Modified Duke criteria (สไลด์หน้า 331 เป็นภาพ — เสริม)
- **Major**: (1) **blood culture บวก** เชื้อ typical จาก 2 ชุดแยกกัน (หรือ persistent bacteremia) (2) **echo พบ vegetation/abscess** หรือ new valvular regurgitation
- **Minor**: predisposition (โรคหัวใจ/IVDU) · ไข้ ≥ 38°C · vascular phenomena (emboli, Janeway, ICH, conjunctival hemorrhage) · immunologic (Osler, Roth, GN, RF บวก) · culture บวกที่ไม่เข้า major
- **Definite IE = 2 major หรือ 1 major + 3 minor หรือ 5 minor**
- ปฏิบัติ: **hemoculture อย่างน้อย 3 ชุด ก่อนให้ ATB** + **echo (TTE → TEE)**

### Empirical ATB (ก่อนรู้เชื้อ) — สไลด์หน้า 332
| ชนิด | เชื้อที่ต้องครอบคลุม | Regimen |
|---|---|---|
| **NVE / late PVE (> 1 ปี)** | Streptococci, staphylococci, enterococci | **ampicillin + cloxacillin + gentamicin** หรือ **ampicillin + ceftriaxone + gentamicin** |
| **Early PVE (< 1 ปี)** | MRSA, enterococci, gram-negative | **vancomycin + gentamicin + rifampicin** |

### Definitive ATB (ตามผล culture) — สไลด์หน้า 333
- **MSSA: cloxacillin หรือ cefazolin** · **MRSA: vancomycin**
- **Oral streptococci และ S. gallolyticus: penicillin G หรือ amoxicillin หรือ ceftriaxone**
- **Enterococci: (ampicillin หรือ amoxicillin) + gentamicin** หรือ **+ ceftriaxone**
- **HACEK: ceftriaxone**
- ระยะเวลา (เสริม): NVE 4–6 สัปดาห์ · PVE ≥ 6 สัปดาห์ · right-sided MSSA ไม่ซับซ้อน 2 สัปดาห์

> ข้อสอบเก่าในสไลด์ใช้ "cloxacillin + gentamicin" สำหรับ S. aureus IE ใน IVDU · แนวทางปัจจุบัน (ESC 2023) **ไม่แนะนำ gentamicin ใน native valve S. aureus แล้ว** (ไตวายโดยไม่เพิ่มการรอด) — ถ้ามีตัวเลือก cloxacillin เดี่ยวให้เลือกตัวนั้น

### IE prophylaxis ก่อนทำฟัน (สไลด์หน้า 335 เป็นตาราง — เสริม)
- **ใครต้องได้**: **เคยเป็น IE**, prosthetic valve/วัสดุซ่อมลิ้น, cyanotic CHD ที่ยังไม่ซ่อม/ซ่อมใน 6 เดือน (และ VAD, TAVI — ESC 2023)
- **หัตถการ**: ที่ต้องจัดการเหงือก/บริเวณ periapical หรือทะลุ mucosa
- **ยา** 30–60 นาทีก่อน: **amoxicillin 2 g PO** (เด็ก 50 mg/kg)
- **แพ้ penicillin**: **azithromycin หรือ clarithromycin 500 mg**, หรือ **doxycycline 100 mg** · cephalexin 2 g ได้ **ถ้าไม่ได้แพ้แบบ anaphylaxis, angioedema, urticaria** · **clindamycin ไม่แนะนำแล้ว** (C. difficile)
''',
        figs=[fig("ie-bugs", "IE: ปัจจัยเสี่ยง → เชื้อ → antibiotic", ie_svg,
                  "อ่านแต่ละแถวจากซ้ายไปขวา: ที่มาของเชื้อในโจทย์ชี้เชื้อ และเชื้อชี้ยารักษาที่จำเพาะ")],
        pearls=[
            "IVDU + vegetation ที่ tricuspid = S. aureus → cloxacillin",
            "ฟันผุ/ทำฟัน = viridans strep → PGS/amoxicillin/ceftriaxone",
            "S. bovis bacteremia → colonoscopy หามะเร็งลำไส้",
            "Janeway ไม่เจ็บ (ฝ่ามือ/เท้า) · Osler เจ็บ (ปลายนิ้ว)",
            "Prophylaxis: amoxicillin 2 g · แพ้แบบ anaphylaxis → azithromycin (ไม่ใช่ cephalosporin, ไม่ใช่ clindamycin)",
        ],
        items=[
            mcq("CARDIO-06-05-1",
                "A 20-year-old man with rheumatic mitral stenosis since childhood presents with fever. BT 38°C, PR 100/min, BP 110/80 mmHg. He has petechiae on the conjunctiva and fingertips, and a diastolic rumbling murmur with a new pansystolic murmur at the apex. What is the most likely diagnosis?",
                "Infective endocarditis",
                ["Acute rheumatic fever", "Pericarditis", "Acute heart failure", "Aortic dissection"],
                explain='''โรคลิ้นเดิม (rheumatic MS = predisposition) + ไข้ + **petechiae** + **murmur ใหม่ (MR)** = **infective endocarditis** (สไลด์หน้า 326, 337) · ต้องส่ง hemoculture ≥ 3 ชุดและ echo
- Acute rheumatic fever ทำให้ carditis ได้ แต่ต้องมีหลักฐาน GAS ร่วมกับ arthritis, chorea, erythema marginatum ไม่ใช่ petechiae
- Pericarditis มีเจ็บอก pleuritic + rub
- Acute HF ไม่อธิบายไข้และ petechiae
- Aortic dissection เจ็บอกฉีกร้าวหลัง''',
                pearl="โรคลิ้นเดิม + ไข้ + murmur ใหม่ + petechiae = IE",
                topic="IE diagnosis", ref=[f"{D} หน้า 336–337"], nl=["2.3.9-3(5)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 336"),
            mcq("CARDIO-06-05-2",
                "A 25-year-old man with a history of injection drug use has fever and fatigue for 2 days that worsened rapidly over 24 hours. There is a systolic murmur at the left parasternal border. Echocardiogram shows a vegetation on the tricuspid valve leaflet. What is the most likely causative organism?",
                "Staphylococcus aureus",
                ["Candida albicans", "Haemophilus influenzae", "Streptococcus viridans", "Streptococcus pyogenes"],
                explain='''IVDU + vegetation ที่ **tricuspid valve** + ดำเนินโรคเร็ว (acute IE) = **S. aureus** (สไลด์หน้า 324, 339)
- Candida ทำให้ IE ใน IVDU ได้แต่พบน้อยกว่ามาก และมักเป็น subacute vegetation ใหญ่
- H. influenzae เป็นหนึ่งใน HACEK สัมพันธ์กับช่องปาก ดำเนินโรคช้า
- Streptococcus viridans สัมพันธ์กับฟันผุ/ทำฟัน ทำให้ subacute IE ที่ลิ้นซ้าย
- S. pyogenes ไม่ใช่เชื้อที่พบบ่อยของ IE''',
                pearl="IVDU + tricuspid vegetation = S. aureus",
                topic="IE organism IVDU", ref=[f"{D} หน้า 338–339"], nl=["2.3.9-3(5)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 338"),
            mcq("CARDIO-06-05-3",
                "A 35-year-old man with years of injection drug use has fever for 2 weeks. BT 39.3°C, PR 110/min, RR 20/min, BP 70/50 mmHg. There is a systolic murmur at the left lower sternal border and splinter hemorrhages under the fingernails. Blood cultures have been drawn. What is the most appropriate antibiotic regimen?",
                "Cloxacillin plus gentamicin",
                ["Penicillin G plus gentamicin", "Ampicillin plus gentamicin", "Amoxicillin plus gentamicin", "Ceftriaxone plus gentamicin"],
                explain='''IVDU + TR murmur + splinter hemorrhage = **right-sided IE จาก S. aureus** → ยาต้องครอบคลุม MSSA คือ **cloxacillin** (ข้อสอบเก่าในสไลด์หน้า 347 ใช้ cloxacillin + gentamicin) และเพราะ shock ต้องประเมิน MRSA เพิ่ม vancomycin ตามบริบท (เสริม)
- Penicillin G, ampicillin และ amoxicillin ถูกทำลายโดย beta-lactamase ของ S. aureus ส่วนใหญ่
- Ceftriaxone ครอบคลุม MSSA ได้ไม่ดีเท่า anti-staphylococcal penicillin เหมาะกับ viridans strep/HACEK
- หมายเหตุ: ESC 2023 ไม่แนะนำเพิ่ม gentamicin ใน native valve S. aureus แล้ว — ตัวที่สำคัญในคำตอบคือ cloxacillin''',
                pearl="S. aureus IE (MSSA) → cloxacillin",
                topic="IE antibiotic IVDU", ref=[f"{D} หน้า 346–347"], nl=["2.3.9-3(5)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 346"),
            mcq("CARDIO-06-05-4",
                "A 40-year-old man with multiple dental caries has prolonged low-grade fever and a new mitral regurgitation murmur. Infective endocarditis is suspected and three sets of blood cultures have been drawn. Which empirical antibiotic regimen is most appropriate?",
                "Ceftriaxone plus gentamicin",
                ["Cloxacillin alone", "Azithromycin", "Meropenem", "Vancomycin plus rifampicin"],
                explain='''ฟันผุ → เชื้อที่คิดถึงคือ **viridans streptococci** (และ HACEK) → **ceftriaxone** ครอบคลุมทั้งสอง (ข้อสอบเก่าสไลด์หน้า 351 ตอบ ceftriaxone + gentamicin; empirical NVE ตามสไลด์คือ ampicillin + ceftriaxone + gentamicin)
- Cloxacillin เดี่ยวครอบคลุม S. aureus แต่ไม่ครอบคลุม HACEK และ enterococci
- Azithromycin เป็นยา prophylaxis ในคนแพ้ penicillin ไม่ใช่ยารักษา IE
- Meropenem กว้างเกินจำเป็นและไม่ใช่ยาที่แนะนำ
- Vancomycin + rifampicin ใช้ใน early PVE/MRSA''',
                pearl="IE จากฟัน = viridans/HACEK → ceftriaxone",
                topic="IE dental origin", ref=[f"{D} หน้า 350–351"], nl=["2.3.9-3(5)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 350"),
            mcq("CARDIO-06-05-5",
                "A patient with a previous episode of infective endocarditis is scheduled for a tooth extraction. He had anaphylactic shock after taking penicillin in the past. What is the most appropriate prophylactic antibiotic?",
                "Azithromycin 500 mg orally 30–60 minutes before the procedure",
                ["Amoxicillin 2 g orally", "Cephalexin 2 g orally", "Clindamycin 600 mg orally", "Ceftriaxone 1 g IV"],
                explain='''เคยเป็น IE = high risk ต้องได้ prophylaxis ก่อนถอนฟัน · **แพ้ penicillin แบบ anaphylaxis** → ใช้ **azithromycin/clarithromycin หรือ doxycycline** (สไลด์หน้า 335, 353)
- Amoxicillin เป็นยามาตรฐานแต่ผู้ป่วยแพ้ penicillin รุนแรง
- Cephalexin และ ceftriaxone เป็น cephalosporin — **ห้ามในผู้ที่แพ้ penicillin แบบ anaphylaxis, angioedema, urticaria**
- Clindamycin **ไม่แนะนำแล้ว** (เสี่ยง C. difficile) ตามสไลด์
- หมายเหตุ: ตัวเลือกในข้อสอบเก่าหน้า 353 ไม่มี azithromycin — ข้อนี้เรียบเรียงใหม่ให้มีคำตอบตามสไลด์''',
                pearl="Prophylaxis แพ้ penicillin รุนแรง → azithromycin/clarithromycin/doxycycline",
                topic="IE prophylaxis", ref=[f"{D} หน้า 352–353"], nl=["2.3.9-3(5)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 352 (ปรับตัวเลือก)"),
            mcq("CARDIO-06-05-6",
                "In a patient with suspected infective endocarditis, examination reveals a grade 3/6 pansystolic murmur at the apex and a grade 2/6 mid-diastolic murmur at the apex. Echocardiography shows a perforated anterior mitral leaflet with severe regurgitation and a normal mitral valve area. Which lesion best explains both murmurs?",
                "Mitral regurgitation with a relative (flow) mitral stenosis murmur",
                ["Aortic stenosis", "Combined true rheumatic mitral stenosis and regurgitation", "Tricuspid regurgitation", "Aortic regurgitation with an Austin Flint murmur"],
                explain='''Severe MR ทำให้ช่วง diastole มีเลือดไหลผ่านลิ้น mitral ปริมาณมาก → เกิด **flow (relative) MS murmur** ทั้งที่พื้นที่ลิ้นปกติ จึงได้ยินทั้ง pansystolic และ diastolic ที่ apex (สไลด์หน้า 349)
- AS เป็น SEM ที่ R 2nd ICS
- True MS ต้องมีพื้นที่ลิ้นแคบบน echo ซึ่งผู้ป่วยปกติ
- TR ฟังที่ LLSB และไม่มี diastolic murmur ที่ apex
- Austin Flint เป็น diastolic rumble ที่ apex จาก AR ต้องมี diastolic blowing ที่ Erb's point ร่วม''',
                pearl="Severe MR → diastolic flow rumble (relative MS)",
                topic="IE murmur", ref=[f"{D} หน้า 348–349"], nl=["2.3.9-3(5)", "2.3.9-3(8)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 348 (ปรับโจทย์)"),
        ]),
    ])
