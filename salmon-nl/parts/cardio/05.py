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

def arr(sid, d):
    return f'<path d="{d}" class="ln" marker-end="url(#{sid}-a)"/>'

# ---------- fig: stable angina workup ----------
S1 = "cardio-05-01"
sa_svg = (f'<svg viewBox="0 0 720 282">{mk(S1)}'
    + box(220, 8, 280, 50, "acsoft", [("tb", "Typical chest pain ตอนออกแรง"), ("t3", "หายเมื่อพัก/NTG · 12-lead EKG ก่อน")])
    + arr(S1, "M300 58L140 90") + arr(S1, "M420 58L580 90") + arr(S1, "M360 58V90")
    + box(8, 94, 230, 74, "oksoft", [("tb", "Low PTP"), ("", "ไม่แนะนำตรวจเพิ่ม"), ("t3", "± CAC score / exercise stress")])
    + box(246, 94, 228, 74, "c1soft", [("tb", "Intermediate–high PTP"), ("", "CCTA"), ("t3", "หรือ cardiac stress testing")])
    + box(482, 94, 230, 74, "badsoft", [("tb", "Abnormal non-invasive"), ("", "Invasive CAG"), ("t3", "→ PCI / CABG ถ้า high risk")])
    + box(8, 186, 704, 88, "sunk",
          [("tb", "การรักษา chronic stable angina"),
           ("", "Secondary prevention: aspirin + high-intensity statin + คุม HT, DM, DLP, เลิกบุหรี่"),
           ("", "Anti-angina: beta-blocker (1st line) → CCB, nitrate (2nd line) · sublingual NTG เมื่อเจ็บ"),
           ("", "Revascularization (PCI, CABG): high risk, severe, อาการไม่ดีขึ้นด้วยยา")], center=False)
    + '</svg>')

# ---------- fig: EKG lead territory ----------
S2 = "cardio-05-02"
def lead(x, y, name, cls):
    return (f'<rect x="{x}" y="{y}" width="120" height="42" rx="7" class="{cls}"/>'
            f'<text x="{x+60}" y="{y+27}" text-anchor="middle" class="tb">{name}</text>')
grid = ''
layout = [["I", "aVR", "V1", "V4"], ["II", "aVL", "V2", "V5"], ["III", "aVF", "V3", "V6"]]
cls_of = {"I": "misssoft", "aVL": "misssoft", "V5": "misssoft", "V6": "misssoft",
          "II": "c1soft", "III": "c1soft", "aVF": "c1soft",
          "V1": "c2soft", "V2": "c2soft", "V3": "acsoft", "V4": "acsoft", "aVR": "sunk"}
for r, rowl in enumerate(layout):
    for c, n in enumerate(rowl):
        grid += lead(10 + c * 128, 10 + r * 50, n, cls_of[n])
terr_svg = ('<svg viewBox="0 0 720 340">' + grid
    + '<text x="10" y="184" class="t3">สีเดียวกัน = มองผนังเดียวกัน (I, aVL คู่กับ V5–V6)</text>'
    + box(10, 196, 344, 136, "box", [], center=False)
    + '<rect x="22" y="208" width="14" height="14" rx="3" class="c2soft"/><text x="44" y="220">V1–V2 Septal → LAD</text>'
    + '<rect x="22" y="232" width="14" height="14" rx="3" class="acsoft"/><text x="44" y="244">V2–V4 Anterior → LAD</text>'
    + '<rect x="22" y="256" width="14" height="14" rx="3" class="misssoft"/><text x="44" y="268">I, aVL, V5–V6 Lateral → LCX (LAD)</text>'
    + '<rect x="22" y="280" width="14" height="14" rx="3" class="c1soft"/><text x="44" y="292">II, III, aVF Inferior → RCA (LCX)</text>'
    + '<text x="22" y="320" class="t3">aVR: ST ยก + ST กดหลาย lead → left main / 3VD (เสริม)</text>'
    + box(530, 10, 182, 142, "badsoft", [("tb", "Posterior wall"), ("", "ST กด V1–V4"), ("", "→ ทำ V7–V9"), ("t3", "STE ≥ 0.5 mm = posterior"), ("t3", "STEMI · RCA/LCX (เสริม)")])
    + box(366, 196, 346, 136, "c1soft",
          [("tb", "Inferior STEMI → ทำ right-sided leads"), ("", "V3R–V6R: STE ใน V4R = RV infarction (RCA)"),
           ("", "ภาวะ preload dependent: BP ต่ำ JVP สูง ปอดใส"), ("ta", "ห้าม nitrate / morphine / diuretic"), ("", "ให้ IV fluid + reperfusion")], center=False)
    + '</svg>')

# ---------- fig: ACS algorithm ----------
S3 = "cardio-05-03"
acs_svg = (f'<svg viewBox="0 0 720 440">{mk(S3)}'
    + box(220, 8, 280, 46, "acsoft", [("tb", "Chest pain สงสัย ACS"), ("t3", "12-lead EKG ภายใน 10 นาที")])
    + arr(S3, "M300 54L160 86") + arr(S3, "M420 54L560 86")
    + box(10, 90, 300, 46, "badsoft", [("tb", "STE / new LBBB"), ("t3", "= STEMI (ไม่ต้องรอ troponin)")])
    + box(410, 90, 300, 46, "box", [("tb", "ST กด / T inv / ปกติ"), ("t3", "hs-cTn 0/1 ชม. (หรือ 0/3 ชม.)")])
    + arr(S3, "M160 136V160")
    + box(10, 164, 300, 92, "badsoft",
          [("tb", "Reperfusion"), ("", "PCI ทำได้ใน ≤ 120 นาที → primary PCI"),
           ("", "> 120 นาที → fibrinolysis ภายใน 10 นาที"), ("t3", "(tenecteplase, alteplase, reteplase, SK)")])
    + arr(S3, "M500 136L470 160") + arr(S3, "M620 136L650 160")
    + box(390, 164, 150, 64, "misssoft", [("tb", "hs-cTn สูง/ขึ้น"), ("", "NSTEMI")])
    + box(560, 164, 150, 64, "oksoft", [("tb", "hs-cTn ไม่เปลี่ยน"), ("", "Unstable angina")])
    + arr(S3, "M465 228L520 252") + arr(S3, "M635 228L580 252")
    + box(390, 256, 320, 64, "box", [("tb", "Risk stratification: GRACE, TIMI"), ("t3", "ไม่มี fibrinolysis ใน NSTE-ACS")])
    + arr(S3, "M480 320V340") + arr(S3, "M620 320V340")
    + box(390, 344, 150, 52, "oksoft", [("tb", "Low risk"), ("t3", "conservative")])
    + box(560, 344, 150, 52, "badsoft", [("tb", "High risk"), ("t3", "invasive (CAG)")])
    + box(10, 274, 300, 158, "sunk",
          [("tb", "ทุกราย ACS"), ("", "Aspirin + P2Y12 inhibitor (DAPT)"), ("", "Anticoagulant: UFH / enoxaparin /"),
           ("", "fondaparinux"), ("", "O2 ถ้า SpO2 < 90% · nitrate"), ("", "high-intensity statin · BB · ACEI/ARB"),
           ("t3", "ห้าม nitrate ใน RV infarct")], center=False)
    + '<text x="550" y="420" text-anchor="middle" class="t3">Medical · PCI · CABG ตาม anatomy</text>'
    + '</svg>')
acs_svg = acs_svg.replace("SpO2 < 90%", "SpO2 &lt; 90%")

# ---------- fig: MI complications timeline ----------
S5 = "cardio-05-05"
comp_svg = (f'<svg viewBox="0 0 720 280">{mk(S5)}'
    + f'<path d="M30 60H700" class="ln" marker-end="url(#{S5}-a)"/>'
    + ''.join(f'<path d="M{x} 54V66" class="ln"/><text x="{x}" y="44" text-anchor="middle" class="tb">{t}</text>'
              for x, t in ((60, "0–24 ชม."), (230, "1–3 วัน"), (420, "3–14 วัน"), (620, "สัปดาห์–เดือน")))
    + box(10, 80, 150, 130, "badsoft", [("tb", "Arrhythmia"), ("", "VF/VT (ตายเร็ว)"), ("", "AV block"), ("t3", "inferior MI → brady"), ("", "Cardiogenic shock")])
    + box(170, 80, 130, 130, "misssoft", [("tb", "Early"), ("", "pericarditis"), ("t3", "(postinfarction)"), ("", "acute HF")])
    + box(310, 80, 220, 130, "badsoft", [("tb", "Mechanical (3–5 วัน)"), ("", "LV free wall rupture"), ("t3", "→ tamponade, PEA, ตายเฉียบพลัน"), ("", "Papillary muscle rupture"), ("t3", "→ acute MR + pulmonary edema"), ("", "Ventricular septal rupture")])
    + box(540, 80, 172, 130, "c2soft", [("tb", "Late"), ("", "LV aneurysm"), ("t3", "ST ยกค้าง, thrombus"), ("", "Dressler syndrome"), ("t3", "autoimmune pericarditis")])
    + '<text x="360" y="240" text-anchor="middle" class="t3">สไลด์หน้า 258 เป็นภาพ — กรอบเวลาเรียบเรียงตามตำรามาตรฐาน (เสริม)</text>'
    + '<text x="360" y="266" text-anchor="middle">MI ใหญ่ 3–7 วันแล้ว tamponade + เสียชีวิต = LV free wall rupture</text>'
    + '</svg>')


LECTURE = lecture("05", "Coronary artery disease & ACS",
    subtitle="stable angina · ACS diagnosis · STEMI · NSTE-ACS · complications",
    objectives=[
        "เลือก investigation ของ chronic stable angina ตาม pretest probability และให้ยาที่เหมาะได้",
        "อ่าน EKG STEMI ตามเกณฑ์ ระบุ territory และหลอดเลือดได้ และใช้ hs-cTn 0/1 ชม. แยก NSTEMI กับ UA ได้",
        "ตัดสินใจ primary PCI หรือ fibrinolysis ตามเวลา และสั่ง DAPT + anticoagulant ได้",
        "บอกภาวะแทรกซ้อนของ MI ตามเวลาได้",
    ],
    sections=[
    # ------------------------------------------------------------------ CAD & stable angina
    sec("cardio-05-01", "CAD & chronic stable angina",
        "Typical angina ตอนออกแรง → PTP ปานกลาง–สูงทำ CCTA/stress test · ยา BB 1st line + ASA + high-intensity statin", minutes=6,
        source=f"{D} หน้า 231–239", nl=["2.3.9(6)", "B7.2.6(2)"],
        md='''
### กลไก
**Atherosclerosis**: stable plaque → หลอดเลือดตีบ → เลือดไปเลี้ยงกล้ามเนื้อหัวใจไม่พอเมื่อ demand สูง → myocardial ischemia

### Chronic stable angina — ลักษณะ
- **เจ็บ/แน่นหลังกระดูกอก** ร้าวไปแขนซ้าย คอ กราม
- **Trigger: ออกแรง ความเครียด**
- **Reproducible/predictable** — ความรุนแรงและความถี่ไม่เปลี่ยน
- **หายเมื่อพักหรือได้ nitroglycerin**

| | Stable angina | ACS |
|---|---|---|
| Trigger | ออกแรง | ขณะพัก / ออกแรงเล็กน้อย |
| รูปแบบ | คาดเดาได้ เหมือนเดิม | ใหม่ รุนแรงขึ้น ถี่ขึ้น นานขึ้น |
| หาย | พัก/NTG | มักไม่หายด้วยพัก/NTG |
| อาการร่วม | – | เหงื่อ ใจสั่น คลื่นไส้ เป็นลม |

### Investigation
- **EKG (initial)** — ส่วนใหญ่ปกติขณะไม่เจ็บ
- ตาราง pretest probability (PTP) ในสไลด์หน้า 233 เป็นภาพ — PTP ขึ้นกับ อายุ เพศ ลักษณะอาการ (typical > atypical) (เสริม)
- **Low PTP**: ไม่แนะนำให้ตรวจเพิ่ม ± CAC scoring / exercise stress test
- **Intermediate–high PTP**: **coronary CT angiography (CCTA)** หรือ **cardiac stress testing**
- **Abnormal non-invasive test → coronary angiography (CAG)**

[[fig:sa-work]]

### การรักษา
- **Secondary prevention**: **aspirin, high-intensity statin** (atorvastatin 40–80, rosuvastatin 20–40 mg — เสริม) · รักษา HT, DM, DLP · เลิกบุหรี่ · ออกกำลังกาย
- **Anti-angina**: **beta-blocker (1st line)** · **CCB, nitrate (2nd line)**
- **Revascularization** (PCI, CABG) เมื่อ high risk, severe
- ระวัง: BB ร่วมกับ non-DHP CCB (bradycardia) · nitrate ห้ามร่วมกับ PDE5 inhibitor (sildenafil) (เสริม)

### ออกกำลังกายเพื่อป้องกัน CVD (จากข้อสอบสไลด์หน้า 276 — เสริม)
- aerobic ระดับปานกลาง **≥ 150 นาที/สัปดาห์** เช่น **เดินเร็ว 30 นาที 5 วัน/สัปดาห์** หรือหนัก 75 นาที/สัปดาห์ + เวทเทรนนิ่ง ≥ 2 วัน/สัปดาห์
''',
        figs=[fig("sa-work", "Workup และการรักษา chronic stable angina", sa_svg,
                  "แถวบนเลือกการตรวจตาม pretest probability กล่องล่างคือการรักษาที่ต้องให้ทุกราย")],
        pearls=[
            "Stable angina: ออกแรงแล้วเจ็บ พักหาย รูปแบบเดิม",
            "PTP ปานกลาง–สูง → CCTA หรือ stress test · ผิดปกติ → CAG",
            "Anti-angina: BB 1st line · CCB/nitrate 2nd line",
            "ทุกรายได้ aspirin + high-intensity statin",
            "ออกกำลังกาย ≥ 150 นาที/สัปดาห์ เช่น เดินเร็ว 30 นาที × 5 วัน (เสริม)",
        ],
        items=[
            mcq("CARDIO-05-01-1",
                "A 55-year-old man has a 3-month history of intermittent pressure-like chest tightness that occurs with exertion and is relieved by rest. He has HT and DLP but no previous cardiac events. Examination is unremarkable and the resting EKG is normal. What is the most appropriate investigation to confirm the diagnosis?",
                "Coronary CT angiography",
                ["Invasive coronary angiography", "Cardiac MRI", "Resting echocardiogram", "Serial troponin"],
                explain='''Typical angina ในชายวัยกลางคนที่มีปัจจัยเสี่ยง = **intermediate–high PTP** → ตรวจ non-invasive ด้วย **CCTA** (หรือ cardiac stress testing) (สไลด์หน้า 234, 237)
- Invasive CAG ทำเมื่อ non-invasive test ผิดปกติ หรือ high risk — ไม่ใช่การตรวจแรกใน stable angina
- Cardiac MRI ไม่ใช่การตรวจแรก
- Resting echo ดู LV function และลิ้นได้ แต่ไม่วินิจฉัย CAD เมื่อไม่มี wall motion ผิดปกติขณะพัก
- Serial troponin ใช้ใน ACS ผู้ป่วยรายนี้อาการคงที่ 3 เดือน''',
                pearl="Stable angina PTP ปานกลาง–สูง → CCTA/stress test ก่อน CAG",
                topic="Stable angina workup", ref=[f"{D} หน้า 236–237"], nl=["2.3.9(6)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 236"),
            mcq("CARDIO-05-01-2",
                "A 50-year-old man has chest tightness radiating to both sides of the mandible when climbing stairs, relieved by 10 minutes of rest. He has HT with poor adherence and smokes 3–4 cigarettes a day for 10 years. BP 160/90 mmHg, HR 80/min, RR 18/min. Besides aspirin and a statin, which antihypertensive drug is most appropriate?",
                "Atenolol",
                ["Enalapril", "Amlodipine", "Hydralazine", "HCTZ"],
                explain='''Chronic stable angina + HT → ยาที่ลดทั้ง BP และ angina คือ **beta-blocker (1st line anti-angina)** → **atenolol** (สไลด์หน้า 235, 239)
- Enalapril ลด BP และ CV event ได้ แต่ไม่ลดอาการ angina
- Amlodipine เป็น 2nd line anti-angina (ใช้เมื่อ BB มีข้อห้ามหรือคุมไม่พอ)
- Hydralazine ทำให้ reflex tachycardia ทำให้ angina แย่ลง
- HCTZ ลด BP แต่ไม่ช่วย angina''',
                pearl="Angina + HT → beta-blocker",
                topic="Stable angina drug", ref=[f"{D} หน้า 238–239"], nl=["2.3.9(6)", "2.3.9(4)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 238"),
            mcq("CARDIO-05-01-3",
                "A 50-year-old man has no history of heart disease, no symptoms and does not exercise. He asks which physical activity would best help prevent cardiovascular disease. What should you recommend?",
                "Brisk walking 30 minutes, 5 days per week",
                ["Jogging 15 minutes, 3 days per week", "Walking 2,000 steps per day", "Two sets of 10 squats per day", "One hour of gentle stretching once a week"],
                explain='''แนวทางป้องกัน CVD แนะนำ aerobic ระดับปานกลาง **≥ 150 นาที/สัปดาห์** → **เดินเร็ว 30 นาที 5 วัน/สัปดาห์** = 150 นาทีพอดี (สไลด์หน้า 276 — เฉลยเป็นภาพ อธิบายตามแนวทางมาตรฐาน เสริม)
- Jogging 15 นาที 3 วัน = 45 นาที/สัปดาห์ ต่ำกว่าเป้าแม้เป็นระดับหนัก (เป้า vigorous 75 นาที)
- 2,000 ก้าว/วัน น้อยมาก (กิจวัตรทั่วไปก็เกินแล้ว)
- Squat 2 ชุด/วัน เป็น resistance exercise เสริมได้ แต่ไม่แทน aerobic
- Stretching สัปดาห์ละครั้งไม่ใช่ aerobic ที่ลด CV risk''',
                pearl="≥ 150 นาที/สัปดาห์ moderate aerobic",
                topic="CV prevention exercise", ref=[f"{D} หน้า 275–276"], nl=["2.3.9(6)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 275"),
        ]),
    # ------------------------------------------------------------------ ACS diagnosis
    sec("cardio-05-02", "ACS: classification, EKG & troponin",
        "EKG ใน 10 นาที · STE ≥ 1 mm 2 lead ติดกัน (V2–V3 ≥ 2/1.5 mm) · hs-cTn 0/1 ชม. แยก NSTEMI กับ UA", minutes=8,
        source=f"{D} หน้า 240–249", nl=["2.2.1", "B7.3(3)c", "3.3.13"],
        md='''
### กลไกและการแบ่งกลุ่ม
**Atherosclerotic plaque disruption** → thrombus → เลือดไปเลี้ยงลดลงเฉียบพลัน

| ชนิด | หลอดเลือด | Biomarker | กล้ามเนื้อ |
|---|---|---|---|
| **STEMI** | **complete occlusion** | สูง | **transmural** infarction |
| **NSTEMI** | partial occlusion | **สูง** (myocardial injury) | **subendocardial** infarction |
| **Unstable angina** | partial occlusion | **ไม่สูง** | ischemia ไม่มี infarction |

### อาการ ACS
- Angina **คาดเดาไม่ได้** · เกิด **ขณะพัก/ออกแรงเล็กน้อย** · มักไม่หายด้วยพัก/NTG
- **New-onset** หรือ **รุนแรง/นาน/ถี่ขึ้น**
- Autonomic: **เหงื่อแตก เป็นลม ใจสั่น คลื่นไส้อาเจียน**

### EKG (ทำภายใน 10 นาที)
- **STEMI**: **ST elevation ≥ 1 mm ใน 2 contiguous leads** ยกเว้น **V2–V3: ≥ 2 mm ในชาย, ≥ 1.5 mm ในหญิง** · หรือ **new LBBB**
- **NSTEMI/UA**: ปกติ, ST depression, T-wave inversion
- **ST depression V1–V4 → ทำ V7–V9** หา posterior wall STEMI
- **Inferior STEMI (II, III, aVF) → ทำ V3R–V6R** หา RV infarction

| ST elevation | ผนัง | หลอดเลือด |
|---|---|---|
| V1, V2 | Septal | LAD |
| V2, V3, V4 | Anterior | LAD |
| V5, V6, I, aVL | Lateral | LCX, LAD |
| II, III, aVF | Inferior | RCA (LCX) |
| V7, V8, V9 | Posterior | RCA, LCX |
| V3R, V4R | Right ventricle | RCA |

[[fig:ekg-territory]]

### High-sensitivity troponin (hs-cTn)
- **0/1-hr algorithm** (ตัวเลขในตารางสไลด์หน้า 248 เป็นภาพ — เสริม: rule-out เมื่อค่า 0 ชม. ต่ำมากและเจ็บอก > 3 ชม. หรือค่าต่ำและเปลี่ยนน้อยใน 1 ชม.)
  - **Very low (เจ็บอก > 3 ชม.) หรือ low และไม่มี significant change** → UA หรือภาวะอื่น
  - **High หรือ significant change** → **NSTEMI**
- **0/3-hr algorithm (ทางเลือก)**: ULN = **99th percentile**
  - 0 ชม. **> ULN** → 3 ชม. เปลี่ยน **> 20%** = MI
  - 0 ชม. **< ULN** → 3 ชม. เปลี่ยน **> 50%** = MI

> ระวังหน่วย: troponin-T **0.12 ng/mL = 120 ng/L** (ULN 14 ng/L) → สูงเกือบ 10 เท่า = NSTEMI (สไลด์หน้า 260)
''',
        figs=[fig("ekg-territory", "EKG lead → ผนังหัวใจ → หลอดเลือด", terr_svg,
                  "สีของแต่ละ lead ใน 12-lead layout บอกผนังที่ lead นั้นมอง จับคู่กับคำอธิบายด้านล่างซ้าย กล่องขวาคือ lead เพิ่มเติมที่ต้องทำ")],
        pearls=[
            "STEMI: STE ≥ 1 mm ใน 2 lead ติดกัน · V2–V3 ≥ 2 mm ชาย/≥ 1.5 mm หญิง · หรือ new LBBB",
            "II, III, aVF = inferior = RCA → ทำ V3R–V6R",
            "ST กด V1–V4 → ทำ V7–V9 หา posterior STEMI",
            "NSTEMI = troponin สูง · UA = troponin ไม่สูง",
            "0/3 ชม.: เกิน ULN ต้องเปลี่ยน > 20% · ไม่เกิน ULN ต้องเปลี่ยน > 50%",
        ],
        items=[
            mcq("CARDIO-05-02-1",
                "A 40-year-old man with high ASCVD risk has intermittent chest tightness and shortness of breath for 2 weeks. EKG shows ST depression in leads II, III and aVF. Troponin-T is 0.12 ng/mL (normal < 14 ng/L). What is the most likely diagnosis?",
                "Acute NSTEMI",
                ["High-risk unstable angina", "Acute aortic dissection", "Acute STEMI", "Acute pericarditis"],
                explain='''ST depression (ไม่มี ST elevation) + **troponin-T 0.12 ng/mL = 120 ng/L ซึ่งสูงกว่า 14 ng/L** = มี myocardial injury = **NSTEMI** (สไลด์หน้า 242, 260)
- Unstable angina ต้องมี troponin **ไม่สูง** — ตัวลวงนี้ดักคนที่ไม่แปลงหน่วย ng/mL เป็น ng/L
- Aortic dissection เจ็บฉีกร้าวไปหลัง BP สองแขนไม่เท่ากัน
- STEMI ต้องมี ST **elevation**
- Pericarditis มี diffuse **ST elevation** + PR depression และเจ็บแบบ pleuritic''',
                pearl="แปลงหน่วย troponin ก่อนเทียบ: 0.12 ng/mL = 120 ng/L",
                topic="NSTEMI vs UA", ref=[f"{D} หน้า 259–260"], nl=["2.2.1", "3.3.13"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 259"),
            mcq("CARDIO-05-02-2",
                "A 62-year-old man has 1 hour of crushing chest pain. EKG shows 3 mm ST elevation in leads II, III and aVF with ST depression in I and aVL. BP is 82/50 mmHg, JVP is elevated and the lungs are clear. Which additional investigation should be done immediately?",
                "Right-sided chest leads (V3R–V6R)",
                ["Posterior leads (V7–V9)", "Chest X-ray before any treatment", "CT pulmonary angiography", "Repeat troponin at 3 hours before deciding"],
                explain='''**Inferior STEMI** + hypotension + JVP สูง + ปอดใส = สงสัย **RV infarction (RCA proximal)** → ทำ **V3R–V6R** (STE ใน V4R ยืนยัน) ตามสไลด์หน้า 245 เพื่อหลีกเลี่ยง nitrate และให้ IV fluid
- V7–V9 ใช้เมื่อเห็น **ST depression V1–V4** เพื่อหา posterior STEMI
- CXR ไม่ควรทำให้ reperfusion ช้า
- CTPA ใช้หา PE ซึ่งไม่ทำให้ STE ใน inferior leads แบบนี้
- STEMI วินิจฉัยจาก EKG ไม่ต้องรอ troponin''',
                pearl="Inferior STEMI + hypotension + ปอดใส → V4R หา RV infarct",
                topic="RV infarction", ref=[f"{D} หน้า 245–246"], nl=["B7.3(3)c", "2.2.1"]),
            mcq("CARDIO-05-02-3",
                "A 58-year-old woman has 40 minutes of chest pressure. EKG shows ST elevation of 3 mm in leads V2–V4 with ST depression in II, III and aVF. Which coronary artery is most likely occluded?",
                "Left anterior descending artery",
                ["Right coronary artery", "Left circumflex artery", "Left main coronary artery only", "Posterior descending artery"],
                explain='''ST elevation ใน **V2–V4 = anterior wall → LAD** (สไลด์หน้า 246) · ST depression ใน inferior leads เป็น reciprocal change
- RCA ให้ STE ใน II, III, aVF (inferior) และ RV leads
- LCX ให้ STE ใน I, aVL, V5–V6 (lateral) หรือ posterior
- Left main มักให้ ST depression หลาย lead + STE ใน aVR (เสริม) ไม่ใช่ STE เฉพาะ V2–V4
- PDA เลี้ยง inferior wall''',
                pearl="V1–V4 = LAD · II, III, aVF = RCA · I, aVL, V5–6 = LCX",
                topic="EKG territory", ref=[f"{D} หน้า 246"], nl=["B7.3(3)c"]),
            mcq("CARDIO-05-02-4",
                "A 66-year-old man has had chest discomfort for 5 hours. EKG shows no ST elevation. High-sensitivity troponin T at 0 hours is above the 99th percentile URL. Using the 0/3-hour algorithm, which change at 3 hours confirms NSTEMI?",
                "A change of more than 20% from the 0-hour value",
                ["Any detectable change", "A change of more than 5%", "A change of more than 50% is required", "No repeat is needed because one value above the URL is diagnostic"],
                explain='''0/3-hr algorithm ตามสไลด์หน้า 249: เมื่อค่า **0 ชม. > ULN (99th percentile)** ต้องมี **การเปลี่ยน > 20%** ที่ 3 ชม. จึงบอกว่าเป็น acute MI
- การเปลี่ยนเพียงเล็กน้อย (detectable หรือ 5%) อยู่ในช่วง analytical variation และพบใน chronic troponin elevation เช่น CKD
- > 50% เป็นเกณฑ์เมื่อค่า **0 ชม. < ULN**
- ค่าเดียวที่เกิน ULN ไม่พอ ต้องมี rise/fall เพื่อแยก acute กับ chronic myocardial injury''',
                pearl="0/3 ชม.: เกิน ULN → > 20% · ต่ำกว่า ULN → > 50%",
                topic="hs-troponin algorithm", ref=[f"{D} หน้า 249"], nl=["3.3.13", "2.2.1"]),
        ]),
    # ------------------------------------------------------------------ STEMI
    sec("cardio-05-03", "STEMI management",
        "PCI ≤ 120 นาที → primary PCI · > 120 นาที → fibrinolysis · DAPT + heparin", minutes=7,
        source=f"{D} หน้า 250–252, 256–257, 265–268", nl=["2.2.1", "B7.2.6(1)", "B2.4(3)"],
        md='''
### Reperfusion
- **ถ้าส่งต่อไปทำ PCI ได้ภายใน ≤ 120 นาที → primary PCI**
- **ถ้า PCI ใช้เวลา > 120 นาที → fibrinolysis** (เป้า door-to-needle ≤ 10–30 นาที, ภายใน 12 ชม. จากเริ่มเจ็บ — เสริม) แล้วส่งต่อไป PCI center ภายหลัง (pharmaco-invasive)
- Flowchart ในสไลด์หน้า 250 เป็นภาพ — หลักข้างต้นมาจากข้อความในหน้าเดียวกัน

[[fig:acs-algo]]

### ยาตามวิธี reperfusion
| | Primary PCI | Fibrinolysis |
|---|---|---|
| Fibrinolytic | – | **tenecteplase, alteplase, reteplase** (streptokinase ในไทย — เสริม) |
| Aspirin | ✓ | ✓ |
| P2Y12 inhibitor | **clopidogrel, prasugrel, ticagrelor** | **clopidogrel** เท่านั้น |
| Anticoagulant | **heparin** | **heparin, enoxaparin, fondaparinux** |

ขนาดยา (เสริม): aspirin 162–325 mg เคี้ยว แล้ว 81 mg/วัน · clopidogrel loading 300–600 mg (fibrinolysis: 300 mg, อายุ > 75 ปี 75 mg) · ticagrelor 180 mg · streptokinase 1.5 ล้านยูนิต IV ใน 30–60 นาที

### ข้อห้าม fibrinolysis (เสริม)
- เคยมี ICH · ischemic stroke ใน 3 เดือน · มะเร็ง/AVM ในสมอง · **สงสัย aortic dissection** · active bleeding · head trauma รุนแรงใน 3 เดือน
- Relative: BP > 180/110 ที่คุมไม่ได้ · CPR นาน · ตั้งครรภ์ · ได้ anticoagulant

### Adjunctive (ใช้ทั้ง STEMI และ NSTE-ACS — สไลด์หน้า 256)
- **O2 เมื่อ SpO2 < 90%** เท่านั้น
- **Nitrate** (SL / IV NTG) — **ห้ามใน RV infarct** (และ SBP < 90, ใช้ PDE5i — เสริม)
- **High-intensity statin** · **beta-blocker** (เลี่ยงใน acute HF/shock — เสริม) · **ACEI/ARB**
- ผู้ป่วย bleeding risk สูง → **ลดระยะเวลา DAPT** (ปกติ 12 เดือน — เสริม)

> "Most appropriate **initial** management" ของ STEMI ในตัวเลือกที่ไม่มี PCI/fibrinolysis = **aspirin** · O2 ให้เมื่อ SpO2 < 90% เท่านั้น
''',
        figs=[fig("acs-algo", "Approach to suspected ACS", acs_svg,
                  "เริ่มที่ EKG ภายใน 10 นาที ซ้ายคือ STEMI ที่ต้อง reperfusion ตามเวลา ขวาคือ NSTE-ACS ที่ใช้ troponin และ risk score ตัดสิน กล่องเทาคือยาที่ทุกรายได้")],
        pearls=[
            "PCI ≤ 120 นาที → primary PCI · > 120 นาที → fibrinolysis",
            "Fibrinolysis คู่กับ clopidogrel (ไม่ใช่ ticagrelor/prasugrel)",
            "O2 เฉพาะ SpO2 < 90%",
            "ห้าม nitrate ใน RV infarction",
            "ห้าม fibrinolysis ถ้าสงสัย aortic dissection (เสริม)",
        ],
        items=[
            mcq("CARDIO-05-03-1",
                "A 45-year-old Thai man develops chest tightness while watching TV. He is a heavy smoker with DM and DLP. BP 140/70 mmHg, HR 100/min, SpO2 98% on room air. EKG shows ST elevation in V1–V3. Among the following, what is the most appropriate initial management?",
                "Aspirin",
                ["Oxygen", "NSAID", "Dopamine", "Morphine as the first drug"],
                explain='''**Anteroseptal STEMI** (STE V1–V3) → ยาตัวแรกที่ต้องให้ทันทีคือ **aspirin** (เคี้ยว) ร่วมกับเตรียม reperfusion (สไลด์หน้า 251, 266)
- Oxygen ให้เมื่อ **SpO2 < 90%** — ผู้ป่วย SpO2 98% การให้ O2 ไม่ช่วยและอาจเพิ่ม infarct size
- NSAID (ที่ไม่ใช่ aspirin) เพิ่ม CV event และ myocardial rupture
- Dopamine ใช้ใน cardiogenic shock ผู้ป่วย BP ปกติ
- Morphine ใช้บรรเทาปวดที่ไม่ตอบสนอง nitrate เท่านั้นและชะลอการดูดซึม P2Y12 inhibitor (เสริม)''',
                pearl="STEMI SpO2 ปกติ → aspirin ไม่ใช่ O2",
                topic="STEMI initial", ref=[f"{D} หน้า 265–266"], nl=["2.2.1"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 265"),
            mcq("CARDIO-05-03-2",
                "A 45-year-old man with DM and heavy smoking has severe chest pain for 1 hour. BP 100/70 mmHg, PR 110/min. EKG shows ST elevation in V1–V4 with ST depression in II, III and aVF. The nearest PCI centre is 150 minutes away. After aspirin and clopidogrel, what is the most appropriate management?",
                "Streptokinase",
                ["Refer to the PCI centre for primary PCI", "Enoxaparin alone", "Dobutamine", "Furosemide"],
                explain='''**Anterior STEMI** เจ็บ 1 ชม. แต่ **PCI ใช้เวลา 150 นาที (> 120)** → ให้ **fibrinolysis** ทันที (ในไทยมัก streptokinase) แล้วค่อยส่งต่อ (สไลด์หน้า 250, 268)
- ส่งต่อทำ primary PCI จะเกินเวลาเป้าหมาย 120 นาที กล้ามเนื้อหัวใจตายมากขึ้น
- Enoxaparin เป็น anticoagulant ร่วม แต่ไม่ใช่ reperfusion
- Dobutamine ใช้ใน cardiogenic shock (BP 100/70 ยังไม่ shock)
- Furosemide ใช้เมื่อมี pulmonary congestion ซึ่งไม่มี''',
                pearl="STEMI + PCI > 120 นาที = fibrinolysis",
                topic="Reperfusion timing", ref=[f"{D} หน้า 267–268"], nl=["2.2.1", "B2.4(3)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 267"),
            mcq("CARDIO-05-03-3",
                "A 60-year-old man with inferior STEMI is in a hospital where primary PCI is available within 60 minutes. He has received aspirin. Which antithrombotic combination is most appropriate before PCI?",
                "Ticagrelor plus unfractionated heparin",
                ["Clopidogrel plus streptokinase", "Fondaparinux alone", "Warfarin plus aspirin", "Tenecteplase plus enoxaparin"],
                explain='''Primary PCI → **DAPT (aspirin + P2Y12 inhibitor: clopidogrel, prasugrel หรือ ticagrelor) + heparin** (สไลด์หน้า 251) → ticagrelor + UFH
- Clopidogrel + streptokinase และ tenecteplase + enoxaparin เป็น regimen ของ **fibrinolysis** ซึ่งไม่ต้องใช้เมื่อทำ PCI ได้ทันเวลา
- Fondaparinux ไม่ใช้เดี่ยว ๆ ใน primary PCI (เสี่ยง catheter thrombosis — เสริม)
- Warfarin ไม่ใช่ยาใน acute STEMI''',
                pearl="Primary PCI: ASA + P2Y12 (ตัวไหนก็ได้) + heparin",
                topic="STEMI antithrombotic", ref=[f"{D} หน้า 251–252"], nl=["2.2.1", "B2.4(3)"]),
            mcq("CARDIO-05-03-4",
                "A 64-year-old man with inferior STEMI has BP 86/54 mmHg, JVP 12 cm, clear lungs and ST elevation in V4R. He is awaiting primary PCI. Which drug should be avoided?",
                "Sublingual nitroglycerin",
                ["Aspirin", "Ticagrelor", "Unfractionated heparin", "Normal saline bolus"],
                explain='''**RV infarction** (inferior STEMI + STE V4R + hypotension + JVP สูง + ปอดใส) เป็นภาวะ **preload-dependent** → **ห้าม nitrate** (ทำให้ preload ลด BP ตกรุนแรง) ตามสไลด์หน้า 256
- Aspirin, ticagrelor และ heparin เป็นยามาตรฐานก่อน PCI
- NSS bolus เป็นการรักษาที่ถูกต้องเพื่อเพิ่ม RV preload''',
                pearl="RV infarct: ห้าม nitrate · ให้ IV fluid",
                topic="RV infarct nitrate", ref=[f"{D} หน้า 245, 256"], nl=["2.2.1"]),
        ]),
    # ------------------------------------------------------------------ NSTE-ACS
    sec("cardio-05-04", "NSTE-ACS (NSTEMI & unstable angina)",
        "Risk stratify ด้วย GRACE/TIMI → high risk ทำ invasive · DAPT + anticoagulant · ไม่มี fibrinolysis", minutes=6,
        source=f"{D} หน้า 253–255, 259–264, 269–272", nl=["2.2.1", "B7.2.6(1)", "B2.4(3)"],
        md='''
### หลักการ
- **Risk stratification** เพื่อกำหนด **timing ของ revascularization**: **GRACE score**, **TIMI score**
- **ไม่มีการใช้ fibrinolytics ใน NSTE-ACS** (ไม่มี complete occlusion จึงไม่ได้ประโยชน์และเพิ่มเลือดออก)

### Timing ของ invasive strategy (สไลด์หน้า 254 เป็นภาพ — เสริม ตาม ESC)
| ระดับ | เกณฑ์ตัวอย่าง | Timing |
|---|---|---|
| Very high risk | hemodynamic unstable/cardiogenic shock, เจ็บไม่หายด้วยยา, life-threatening arrhythmia, mechanical complication, acute HF, ST depression > 1 mm ≥ 6 lead + STE aVR | **immediate < 2 ชม.** |
| High risk | NSTEMI ยืนยันด้วย troponin, dynamic ST-T change, GRACE > 140 | **early < 24 ชม.** |
| Low risk | ไม่มีข้างบน | selective invasive / non-invasive test ก่อน |

### ยา
- **Dual antiplatelet**: aspirin + P2Y12 inhibitor (**clopidogrel, prasugrel, ticagrelor**)
- **Anticoagulant**: **heparin, enoxaparin, fondaparinux** (enoxaparin 1 mg/kg SC q 12 h — เสริม)
- Adjunctive เหมือน STEMI: O2 ถ้า SpO2 < 90%, nitrate, high-intensity statin, BB, ACEI/ARB

> โจทย์ "ได้ aspirin + clopidogrel แล้ว next step?" ใน NSTE-ACS → **anticoagulant (enoxaparin)** ไม่ใช่ alteplase · ถ้าโจทย์บอกว่า **high risk** → **coronary angiogram (invasive strategy)**
''',
        pearls=[
            "ไม่มี fibrinolysis ใน NSTE-ACS",
            "DAPT + anticoagulant (heparin/enoxaparin/fondaparinux)",
            "Risk stratify ด้วย GRACE/TIMI → high risk ทำ CAG ใน 24 ชม.",
            "Very high risk (shock, refractory pain, arrhythmia) → CAG ภายใน 2 ชม. (เสริม)",
        ],
        items=[
            mcq("CARDIO-05-04-1",
                "A patient with chest pain is diagnosed with NSTEMI. He is clinically high risk with dynamic ST-T changes and a GRACE score of 160. He is hemodynamically stable and has received aspirin, ticagrelor and enoxaparin. What is the most appropriate management?",
                "Coronary angiography within 24 hours",
                ["Observe and discharge if pain resolves", "rt-PA", "Streptokinase", "Exercise stress test before discharge"],
                explain='''NSTEMI ที่ **high risk** (troponin บวก, dynamic ST-T change, GRACE > 140) → **invasive strategy: coronary angiography ภายใน 24 ชม.** (สไลด์หน้า 253–254, 264)
- Observe/discharge ไม่เหมาะกับ high risk
- rt-PA และ streptokinase เป็น fibrinolytic — **ไม่ใช้ใน NSTE-ACS**
- Exercise stress test ใช้ในกลุ่ม low risk เท่านั้น และห้ามทำในช่วง acute high risk''',
                pearl="NSTEMI high risk → CAG เร็ว ไม่ใช่ fibrinolysis",
                topic="NSTE-ACS invasive", ref=[f"{D} หน้า 263–264"], nl=["2.2.1"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 263 (ปรับโจทย์)"),
            mcq("CARDIO-05-04-2",
                "A 65-year-old woman with DM and DLP has palpitation, sweating and left-sided chest tightness for 3 hours. PR 100/min, BP 110/70 mmHg. EKG shows 1.5 mm horizontal ST depression in V4–V6 without ST elevation, and hs-troponin is elevated. She has been given aspirin and clopidogrel. What is the most appropriate next step in treatment?",
                "Enoxaparin",
                ["Alteplase", "Metoprolol IV in high dose", "Isosorbide dinitrate as the next essential drug", "Warfarin"],
                explain='''NSTEMI (ST depression + troponin สูง) ได้ DAPT แล้ว → ต้องเพิ่ม **anticoagulant** (heparin/**enoxaparin**/fondaparinux) ตามสไลด์หน้า 255 แล้ว risk stratify เพื่อวาง timing ของ CAG
- Alteplase เป็น fibrinolytic ห้ามใช้ใน NSTE-ACS
- Metoprolol ให้ได้ใน ACS (ทางปากเมื่อไม่มี HF/shock) แต่ไม่ใช่ขั้นจำเป็นถัดไป และ IV ขนาดสูงเสี่ยง cardiogenic shock
- Nitrate ช่วยอาการเจ็บ แต่ไม่ลดการตาย
- Warfarin ไม่ใช่ anticoagulant ใน acute ACS''',
                pearl="NSTE-ACS: DAPT + anticoagulant",
                topic="NSTE-ACS anticoagulant", ref=[f"{D} หน้า 255, 271–272"], nl=["2.2.1", "B2.4(3)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 271 (EKG เป็นภาพ — ปรับโจทย์)"),
            mcq("CARDIO-05-04-3",
                "A 70-year-old man has 30 minutes of chest pain at rest that is now relieved. EKG shows T-wave inversion in V2–V4. hs-cTnT at 0 and 1 hour are both below the 99th percentile with no significant change. What is the most likely diagnosis?",
                "Unstable angina",
                ["NSTEMI", "STEMI", "Chronic stable angina", "Acute pericarditis"],
                explain='''เจ็บอกขณะพัก (ACS) + T inversion + **troponin ไม่สูงและไม่เปลี่ยน** = **unstable angina** (ischemia ไม่มี infarction) (สไลด์หน้า 242, 247)
- NSTEMI ต้องมี troponin สูงหรือเปลี่ยนอย่างมีนัยสำคัญ
- STEMI ต้องมี ST elevation
- Stable angina เกิดตอนออกแรงตามรูปแบบเดิม ไม่ใช่เจ็บขณะพัก
- Pericarditis ให้ diffuse STE + PR depression และเจ็บแบบ pleuritic''',
                pearl="ACS + troponin ปกติ = UA",
                topic="Unstable angina", ref=[f"{D} หน้า 242, 247"], nl=["2.2.1", "3.3.13"]),
        ]),
    # ------------------------------------------------------------------ complications
    sec("cardio-05-05", "Complications of MI",
        "arrhythmia ช่วงแรก · mechanical complication 3–5 วัน (free wall, papillary muscle, VSR) · LV aneurysm/Dressler ภายหลัง", minutes=4,
        source=f"{D} หน้า 258, 273–274", nl=["2.2.1", "2.3.9(6)", "2.2.2"],
        md='''
> สไลด์หน้า 258 (ACS complication) เป็นภาพ — เนื้อหาด้านล่างเรียบเรียงจากตำรามาตรฐาน (เสริม) โดยยึดข้อสอบในสไลด์หน้า 274

[[fig:mi-comp]]

| ภาวะแทรกซ้อน | เวลา | เบาะแส |
|---|---|---|
| VF/VT | ชั่วโมงแรก ๆ | สาเหตุตายก่อนถึง รพ. |
| Bradycardia / AV block | วันแรก ๆ | inferior MI (RCA เลี้ยง AV node) |
| Cardiogenic shock | วันแรก ๆ | MI ใหญ่ (มักเป็น anterior) |
| Early pericarditis | 1–3 วัน | เจ็บ pleuritic + rub |
| **LV free wall rupture** | **3–5 (ถึง 14) วัน** | **tamponade → PEA → ตายเฉียบพลัน** |
| Papillary muscle rupture | 3–5 วัน | **acute MR** + pulmonary edema (มักเป็น inferior MI) |
| Ventricular septal rupture | 3–5 วัน | holosystolic murmur ใหม่ที่ LLSB + shock · O2 step-up ใน RV |
| LV aneurysm | สัปดาห์–เดือน | ST ยกค้าง · HF · LV thrombus → embolism |
| Dressler syndrome | 2–10 สัปดาห์ | autoimmune pericarditis ไข้ · รักษา aspirin |

> ข้อสอบในสไลด์: MI ใหญ่ที่ LV นอน รพ. 6 วันแล้วเกิด **cardiac tamponade** เสียชีวิต = **rupture of LV free wall**
''',
        figs=[fig("mi-comp", "ภาวะแทรกซ้อนของ MI ตามเวลา", comp_svg,
                  "แกนนอนคือเวลาหลัง MI กล่องแดงคือกลุ่มที่ทำให้เสียชีวิตเร็ว — arrhythmia ช่วงแรก และ mechanical rupture ช่วง 3–5 วัน")],
        pearls=[
            "3–5 วันหลัง MI + tamponade/PEA = LV free wall rupture",
            "Acute MR + pulmonary edema หลัง inferior MI = papillary muscle rupture",
            "Murmur ใหม่ที่ LLSB + shock หลัง MI = VSR (เสริม)",
            "ST ยกค้างหลายสัปดาห์ = LV aneurysm",
        ],
        items=[
            mcq("CARDIO-05-05-1",
                "A 65-year-old man is admitted to the CCU with a massive left ventricular myocardial infarction. On day 6 of admission he suddenly develops cardiac tamponade and dies. What is the most likely cause?",
                "Rupture of the left ventricular free wall",
                ["Fatal ventricular arrhythmia", "Extension of the previous infarction", "Rupture of the papillary muscle", "Ventricular septal rupture"],
                explain='''ช่วง **3–14 วัน** หลัง MI ใหญ่ กล้ามเนื้อที่ตายอ่อนตัวที่สุด · **free wall rupture** ทำให้เลือดเข้าช่องเยื่อหุ้มหัวใจ → **cardiac tamponade** → ตายเฉียบพลัน (สไลด์หน้า 274)
- Fatal arrhythmia ทำให้ตายเฉียบพลันได้แต่พบมากในชั่วโมงแรก ๆ และไม่ทำให้ tamponade
- Infarct extension ทำให้เจ็บอกซ้ำและ HF ไม่ใช่ tamponade
- Papillary muscle rupture ทำให้ acute MR + pulmonary edema
- VSR ทำให้ murmur ใหม่ที่ LLSB + shock ไม่ใช่ tamponade (เลือดไหลระหว่าง ventricle ไม่ใช่เข้า pericardium)''',
                pearl="Tamponade หลัง MI ใหญ่ ~1 สัปดาห์ = free wall rupture",
                topic="Free wall rupture", ref=[f"{D} หน้า 273–274"], nl=["2.2.1", "2.2.2"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 273"),
            mcq("CARDIO-05-05-2",
                "A 68-year-old woman is on day 4 after an inferior STEMI treated with fibrinolysis. She suddenly develops severe dyspnea and hypotension. There are bilateral crackles and a new soft holosystolic murmur at the apex radiating to the axilla. What is the most likely complication?",
                "Papillary muscle rupture",
                ["Left ventricular free wall rupture", "Dressler syndrome", "Left ventricular aneurysm", "Reinfarction of the anterior wall"],
                explain='''วันที่ 3–5 หลัง **inferior MI** + **pulmonary edema เฉียบพลัน** + murmur ใหม่ที่ apex ร้าว axilla = **acute MR จาก papillary muscle rupture** (posteromedial papillary muscle มีเลือดเลี้ยงจาก PDA เส้นเดียว) (เสริม)
- Free wall rupture ทำให้ tamponade (JVP สูง เสียงหัวใจเบา ปอดใส) ไม่ใช่ murmur MR
- Dressler เกิดหลายสัปดาห์ เป็น pericarditis มีไข้
- LV aneurysm เกิดช้าเป็นสัปดาห์–เดือน
- Reinfarction ไม่อธิบาย murmur ใหม่ที่ apex''',
                pearl="Acute MR + pulmonary edema หลัง inferior MI = papillary muscle rupture",
                topic="Papillary muscle rupture", ref=[f"{D} หน้า 258"], nl=["2.2.1", "2.2.5"]),
        ]),
    ])
