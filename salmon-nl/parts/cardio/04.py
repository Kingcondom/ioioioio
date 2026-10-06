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

# ---------- fig: pericarditis EKG vs STEMI ----------
def beat(x0, base, st, pr_dep=False, tinv=False, conv=False):
    # P wave, PR segment, QRS, ST, T
    pr = base + (5 if pr_dep else 0)
    out = f'<path d="M{x0} {base}q9 -12 18 0L{x0+30} {pr}L{x0+34} {pr+5}L{x0+40} {base-48}L{x0+46} {base+10}'
    stb = base - st
    if conv:
        out += f'L{x0+50} {stb}Q{x0+66} {stb-6} {x0+80} {stb-14}Q{x0+92} {stb-22} {x0+104} {base}'
    else:
        out += f'L{x0+50} {stb}Q{x0+70} {stb-8} {x0+82} {stb-18 if not tinv else stb+14}Q{x0+92} {stb-24 if not tinv else stb+20} {x0+104} {base}'
    out += f'L{x0+130} {base}" class="lna"/>'
    return out

S1 = "cardio-04-01"
peri_svg = ('<svg viewBox="0 0 720 290">'
    + '<rect x="8" y="8" width="346" height="274" rx="10" class="oksoft"/>'
    + '<text x="181" y="32" text-anchor="middle" class="tb">Acute pericarditis</text>'
    + '<path d="M30 110H330" class="lnf"/>'
    + beat(40, 110, 10, pr_dep=True, conv=True) + beat(180, 110, 10, pr_dep=True, conv=True)
    + '<text x="24" y="160" class="">• ST ยก <tspan class="tb">ทุก lead</tspan> (diffuse)</text>'
    + '<text x="24" y="182" class="">• ST รูป concave (หน้าอยู่ด้านบน)</text>'
    + '<text x="24" y="204" class="">• <tspan class="tb">PR depression</tspan></text>'
    + '<text x="24" y="226" class="">• ไม่มี reciprocal ST depression</text>'
    + '<text x="24" y="248" class="">• ระยะหลัง: T wave inversion</text>'
    + '<text x="24" y="270" class="t3">aVR อาจ ST กด + PR ยก (เสริม)</text>'
    + '<rect x="366" y="8" width="346" height="274" rx="10" class="badsoft"/>'
    + '<text x="539" y="32" text-anchor="middle" class="tb">STEMI</text>'
    + '<path d="M388 110H688" class="lnf"/>'
    + beat(398, 110, 22) + beat(538, 110, 22)
    + '<text x="382" y="160" class="">• ST ยกเฉพาะ <tspan class="tb">territory</tspan> ของหลอดเลือด</text>'
    + '<text x="382" y="182" class="">• ST รูป convex (tombstone)</text>'
    + '<text x="382" y="204" class="">• มี <tspan class="tb">reciprocal ST depression</tspan></text>'
    + '<text x="382" y="226" class="">• Q wave เกิดตามมา</text>'
    + '<text x="382" y="248" class="">• PR segment ปกติ</text>'
    + '<text x="382" y="270" class="t3">เจ็บแน่น ไม่ดีขึ้นเมื่อโน้มตัว</text>'
    + '</svg>')

# ---------- fig: tamponade physiology ----------
S3 = "cardio-04-03"
tamp_svg = (f'<svg viewBox="0 0 720 330">{mk(S3)}'
    + '<ellipse cx="170" cy="160" rx="150" ry="130" class="misssoft"/>'
    + '<text x="170" y="48" text-anchor="middle" class="tb">น้ำในเยื่อหุ้มหัวใจ</text>'
    + '<ellipse cx="125" cy="170" rx="55" ry="80" class="c1soft"/>'
    + '<text x="125" y="165" text-anchor="middle" class="tb">RV</text>'
    + '<text x="125" y="185" text-anchor="middle" class="t3">หายใจเข้า</text>'
    + '<text x="125" y="201" text-anchor="middle" class="t3">เลือดเข้ามากขึ้น</text>'
    + '<ellipse cx="225" cy="170" rx="50" ry="78" class="badsoft"/>'
    + '<text x="225" y="170" text-anchor="middle" class="tb">LV</text>'
    + '<text x="225" y="190" text-anchor="middle" class="t3">ถูกเบียด</text>'
    + f'<path d="M158 250L170 230" class="ln"/>'
    + '<text x="150" y="266" text-anchor="middle" class="t3">septum ถูกดันไปทาง LV →</text>'
    + box(350, 14, 362, 74, "box", [("tb", "Inspiration → venous return ฝั่งขวา ↑"), ("", "RV ขยายออกนอกไม่ได้ (pericardium ตึง)"), ("", "→ septum ดันเข้า LV")], center=False)
    + f'<path d="M530 88V104" class="ln" marker-end="url(#{S3}-a)"/>'
    + box(350, 106, 362, 54, "box", [("tb", "LV filling ↓ → stroke volume ↓"), ("", "→ SBP ลด > 10 mmHg ตอนหายใจเข้า")], center=False)
    + f'<path d="M530 160V176" class="ln" marker-end="url(#{S3}-a)"/>'
    + box(350, 178, 362, 40, "acsoft", [("ta", "= Pulsus paradoxus")], center=True)
    + box(350, 232, 362, 90, "sunk", [("tb", "Beck's triad"), ("", "↓ BP · muffled heart sounds · ↑ JVP"), ("", "+ tachycardia, ปอดใส, EKG low voltage /"), ("", "electrical alternans")], center=False)
    + '</svg>')

# ---------- fig: aortic dissection ----------
S4 = "cardio-04-04"
def aorta(cx, tear_cls_asc, tear_cls_desc, label, sub):
    out = (f'<path d="M{cx-40} 230V120Q{cx-40} 60 {cx+10} 60Q{cx+60} 60 {cx+60} 120V250" class="ln"/>'
           f'<path d="M{cx-20} 230V122Q{cx-20} 80 {cx+10} 80Q{cx+40} 80 {cx+40} 122V250" class="ln"/>')
    if tear_cls_asc:
        out += f'<path d="M{cx-34} 210V125Q{cx-34} 68 {cx+10} 68Q{cx+52} 68 {cx+52} 122V240" class="{tear_cls_asc}"/>'
    if tear_cls_desc:
        out += f'<path d="M{cx+52} 128V240" class="{tear_cls_desc}"/>'
    out += (f'<text x="{cx+10}" y="292" text-anchor="middle" class="tb">{label}</text>'
            f'<text x="{cx+10}" y="311" text-anchor="middle" class="t3">{sub}</text>'
            f'<text x="{cx-30}" y="250" text-anchor="middle" class="t3">ascending</text>'
            f'<text x="{cx+50}" y="268" text-anchor="middle" class="t3">descending</text>')
    return out

dis_svg = (f'<svg viewBox="0 0 720 322">{mk(S4)}'
    + aorta(110, "lnbad", None, "Stanford A", "มี ascending → ผ่าตัด")
    + aorta(310, None, "lnbad", "Stanford B", "descending อย่างเดียว")
    + box(450, 10, 262, 300, "sunk",
          [("tb", "การรักษา"),
           ("", "BP สูง: เป้า SBP 100–120, HR ≤ 60"),
           ("ta", "1) IV beta-blocker ก่อน"),
           ("t3", "    labetalol, esmolol"),
           ("ta", "2) แล้วค่อย IV vasodilator"),
           ("t3", "    nicardipine, NTG"),
           ("t3", "    (กัน reflex tachycardia)"),
           ("", "+ morphine ระงับปวด"),
           ("", "BP ต่ำ: IV fluid, vasopressor"),
           ("tb", "ผ่าตัด"),
           ("", "Stanford A ทุกราย"),
           ("", "Stanford B ที่มี complication"),
           ("t3", "ห้าม thrombolytic / antiplatelet")], center=False)
    + '<text x="225" y="22" text-anchor="middle" class="t3">เส้นแดง = false lumen</text>'
    + '</svg>')


LECTURE = lecture("04", "Pericardial disease & aortic dissection",
    subtitle="pericarditis · effusion · tamponade · aortic dissection",
    objectives=[
        "วินิจฉัย acute pericarditis จากอาการและ EKG และสั่งยาได้ถูก รวมถึง TB pericarditis",
        "แยก constrictive pericarditis, pericardial effusion และ cardiac tamponade ได้",
        "รู้ข้อบ่งชี้ pericardiocentesis",
        "วินิจฉัย aortic dissection และเลือกยาคุม BP ตามลำดับได้",
    ],
    sections=[
    # ------------------------------------------------------------------ pericarditis
    sec("cardio-04-01", "Acute & constrictive pericarditis",
        "เจ็บอก pleuritic ดีขึ้นเมื่อโน้มตัว + rub + diffuse STE/PR depression → NSAID/ASA + colchicine", minutes=7,
        source=f"{D} หน้า 190–194, 201–209", nl=["2.3.9-3(6)", "B7.2.2-3(3)"],
        md='''
### สาเหตุ
- **Infection: virus (พบบ่อยที่สุด)**, bacteria (และ TB — พบบ่อยในไทย)
- Myocardial infarction (early, Dressler — เสริม), postoperative
- **Uremia**, radiation, malignancy, trauma
- Idiopathic

### Acute pericarditis
- **Pleuritic chest pain ที่ดีขึ้นเมื่อโน้มตัวไปข้างหน้า**
- **Pericardial friction rub**
- ไข้ต่ำ เหนื่อย ไอแห้ง · viral pericarditis มักมี **flu-like symptoms** นำมา
- **EKG: diffuse ST elevation + PR segment depression** → ระยะหลัง T wave inversion
- **Echo: ± pericardial effusion**

[[fig:peri-ekg]]

### Chronic: constrictive pericarditis
เยื่อหุ้มหนาแข็ง → หัวใจคลายตัวรับเลือดไม่ได้
- **Fluid overload / right-sided**: ↑JVP, **Kussmaul sign** (JVP ขึ้นตอนหายใจเข้า — ปกติต้องลดลง), hepatomegaly, hepatojugular reflux, edema
- **Low cardiac output**: dyspnea
- **Pericardial knock** (ventricle ขยายไม่เต็มที่ เลือดไหลเข้ากระแทกจนเกิดเสียง)
- Pulsus paradoxus (SBP ลด > 10 mmHg ตอนหายใจเข้า) — สไลด์ใส่ไว้ แต่พบเด่นใน tamponade มากกว่า (เสริม)
- **Echo: pericardial thickness ↑** · EKG low voltage, diffuse ST-T change (จากข้อสอบสไลด์หน้า 209)
- ปอดมักใส (เป็นปัญหาฝั่งขวาเด่น)

### การรักษา
- Acute pericarditis มักหายเอง (self-limited) · รักษาสาเหตุ (เช่น TB pericarditis)
- **Pain control + ป้องกันการเป็นซ้ำ: NSAID หรือ ASA + colchicine**
  - ขนาดยา (เสริม): aspirin 750–1,000 mg ทุก 8 ชม. หรือ ibuprofen 600 mg ทุก 8 ชม. 1–2 สัปดาห์ แล้วค่อยลด · colchicine 0.5 mg วันละ 1–2 ครั้ง 3 เดือน
  - pericarditis หลัง MI ใช้ **aspirin** (NSAID อื่นรบกวนการหายของแผลกล้ามเนื้อ — เสริม)
- **Prednisolone** เฉพาะรายรุนแรง/ดื้อยา (ไม่ใช่ first line เพราะเพิ่มการกลับเป็นซ้ำ — เสริม)
- **Pericardiocentesis**: cardiac tamponade, large effusion
- **Pericardiectomy**: constrictive pericarditis ที่อาการคงอยู่
- **TB pericarditis**: ยา anti-TB + **prednisolone เพื่อป้องกัน constrictive pericarditis** (ตามสไลด์)

> TB pericarditis ในข้อสอบ: ไข้ ไอเรื้อรัง pericardial fluid **lymphocyte เด่น + ADA สูง (> 40 U/L)** · แนวทาง ESC ล่าสุดให้ steroid เป็นทางเลือก (ลด constriction แต่ไม่ลดการตาย — เสริม) ข้อสอบตามสไลด์ตอบ prednisolone
''',
        figs=[fig("peri-ekg", "EKG ของ acute pericarditis เทียบกับ STEMI", peri_svg,
                  "ซ้ายคือ pericarditis (ST ยกทุก lead รูปเว้า และ PR segment กดลง) ขวาคือ STEMI (ST ยกเฉพาะ territory รูปนูน และมี reciprocal change)")],
        pearls=[
            "Pleuritic chest pain ดีขึ้นเมื่อโน้มตัว + rub = pericarditis",
            "EKG: diffuse STE + PR depression",
            "Rx: NSAID/ASA + colchicine · prednisolone เฉพาะรายรุนแรง",
            "TB pericarditis (lymphocyte, ADA สูง): + prednisolone กัน constriction",
            "Constrictive: Kussmaul sign + pericardial knock + เยื่อหุ้มหนา",
        ],
        items=[
            mcq("CARDIO-04-01-1",
                "A 20-year-old man has low-grade fever, myalgia and chest pain for 1 day. The chest pain improves when he leans forward. Examination shows normal S1S2, no murmur, no cardiomegaly and a friction rub at the apex. What is the most appropriate management?",
                "NSAID",
                ["Acyclovir", "Prednisolone", "Ceftriaxone", "Heparin"],
                explain='''ไข้ต่ำ ปวดเมื่อย (flu-like) + เจ็บอกดีขึ้นเมื่อโน้มตัว + friction rub = **acute (viral) pericarditis** → **NSAID** (ร่วมกับ colchicine) (สไลด์หน้า 194, 205)
- Acyclovir ไม่มีบทบาทใน viral pericarditis ทั่วไป
- Prednisolone ใช้เฉพาะรายรุนแรง/ดื้อต่อ NSAID หรือมีข้อห้าม และเพิ่มการกลับเป็นซ้ำ
- Ceftriaxone ใช้ใน purulent bacterial pericarditis ซึ่งผู้ป่วยจะไข้สูงและป่วยหนัก
- Heparin เพิ่มความเสี่ยง hemopericardium ใน pericarditis''',
                pearl="Viral pericarditis → NSAID (+ colchicine)",
                topic="Acute pericarditis", ref=[f"{D} หน้า 204–205"], nl=["2.3.9-3(6)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 204"),
            mcq("CARDIO-04-01-2",
                "An 18-year-old woman has chest pain that improves when she leans forward. Lungs are clear and a friction rub is present. EKG shows ST elevation in all chest leads with PR segment depression. What is the most appropriate management?",
                "Aspirin",
                ["IVIG", "Streptokinase", "Prednisolone", "Primary PCI"],
                explain='''อาการและ rub เข้าได้กับ **acute pericarditis** และ EKG เป็น **diffuse ST elevation** (ไม่ใช่ territory เดียว) → **aspirin/NSAID** (สไลด์หน้า 203)
- IVIG ใช้ใน Kawasaki หรือ myocarditis บางชนิด ไม่ใช่ pericarditis ทั่วไป
- Streptokinase และ primary PCI เป็นการรักษา STEMI — การให้ fibrinolytic ใน pericarditis เสี่ยง hemopericardium/tamponade
- Prednisolone ไม่ใช่ first line''',
                pearl="Diffuse STE + rub ในคนอายุน้อย = pericarditis ห้าม thrombolysis",
                topic="Pericarditis vs STEMI", ref=[f"{D} หน้า 202–203"], nl=["2.3.9-3(6)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 202"),
            mcq("CARDIO-04-01-3",
                "A 50-year-old man has chronic cough and dyspnea for 1 month. BT 38.5°C, BP 100/60 mmHg, PR 80/min, RR 18/min. There is a pericardial friction rub and soft S1. Pericardial fluid is straw-coloured with WBC 2,000 cells/mm3 (N 30%, L 70%), ADA 100 U/L and no organisms on Gram stain. Besides specific treatment, which drug can prevent long-term complications?",
                "Prednisolone",
                ["Aspirin", "Celecoxib", "Colchicine", "Indomethacin"],
                explain='''Lymphocyte เด่น + **ADA สูงมาก** + ไอเรื้อรัง ไข้ = **TB pericarditis** · นอกจาก anti-TB แล้ว สไลด์ให้ **prednisolone เพื่อป้องกัน constrictive pericarditis** (สไลด์หน้า 194, 201)
- Aspirin, celecoxib และ indomethacin บรรเทาปวดได้แต่ไม่ลดการเกิด constriction จากการอักเสบแบบ granulomatous
- Colchicine ป้องกันการกลับเป็นซ้ำของ viral/idiopathic pericarditis แต่ไม่ใช่ยาที่แนะนำให้กัน constriction ใน TB
- หมายเหตุ: ESC 2025 ยังถือ steroid เป็นทางเลือก (ลด constriction แต่ไม่ลดการตาย) — ข้อสอบตอบ prednisolone (เสริม)''',
                pearl="TB pericarditis + steroid → กัน constrictive pericarditis",
                topic="TB pericarditis", ref=[f"{D} หน้า 200–201"], nl=["2.3.9-3(6)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 200"),
            mcq("CARDIO-04-01-4",
                "A 30-year-old man has dyspnea for 1 month. He has a past history of pulmonary tuberculosis. Examination shows neck vein engorgement that rises further on inspiration, clear and equal breath sounds, hepatomegaly and an early diastolic extra sound. EKG shows diffuse ST-T changes and low voltage. Echocardiogram shows a thickened pericardium without significant effusion. What is the most likely diagnosis?",
                "Constrictive pericarditis",
                ["Cardiac tamponade", "Cardiac beriberi", "Dilated cardiomyopathy", "Right ventricular infarction"],
                explain='''JVP สูง + **Kussmaul sign** (JVP ขึ้นตอนหายใจเข้า) + hepatomegaly + ปอดใส + **pericardial knock** + low voltage + **เยื่อหุ้มหนาโดยไม่มีน้ำ** = **constrictive pericarditis** (สไลด์หน้า 192, 209)
- Cardiac tamponade ต้องมี effusion บน echo และ BP ต่ำ/pulsus paradoxus เด่น
- Cardiac beriberi เป็น high-output HF ในคนดื่มสุรา มี pulmonary congestion และ S3 ไม่มีเยื่อหุ้มหนา
- DCM ทำให้หัวใจโต ปอดมี congestion และ EF ต่ำ
- RV infarction เกิดเฉียบพลันพร้อม inferior STEMI และเจ็บอก''',
                pearl="Kussmaul + pericardial knock + เยื่อหุ้มหนา = constrictive",
                topic="Constrictive pericarditis", ref=[f"{D} หน้า 192, 208–209"], nl=["2.3.9-3(6)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 208 (ปรับโจทย์)"),
        ]),
    # ------------------------------------------------------------------ effusion
    sec("cardio-04-02", "Pericardial effusion",
        "Echo เป็น gold standard · EKG low voltage + electrical alternans · CXR flask-shaped ปอดใส", minutes=4,
        source=f"{D} หน้า 195–198", nl=["2.3.9-3(6)", "3.3.23"],
        md='''
### สาเหตุ
| ชนิด | สาเหตุ |
|---|---|
| **Hemopericardium** | cardiac wall rupture (หลัง MI), chest trauma, **aortic dissection**, cardiac surgery |
| Serous / serosanguinous | idiopathic, acute pericarditis, **malignancy**, postpericardiotomy syndrome, **uremia**, autoimmune |

### อาการ
- ไม่มีอาการ (น้ำสะสมช้า เยื่อหุ้มยืดทัน) · หรือ dyspnea, orthopnea, chest pain
- ถ้าสะสมเร็ว น้ำน้อยก็เกิด tamponade ได้ (เสริม)

### การตรวจ
- **Echocardiography = gold standard**
- **EKG (large effusion)**
  - **Low voltage — "ซ้าย 5 ขวา 10"**: QRS < 5 mm ใน limb leads · < 10 mm ใน precordial leads
  - **Electrical alternans**: QRS สูงสลับต่ำ (หัวใจแกว่งในถุงน้ำ)
- **CXR: flask-shaped heart (water-bottle) และไม่มี pulmonary edema** (ต่างจาก HF ที่หัวใจโต + ปอดมีน้ำ)

### การรักษา
- รักษาสาเหตุ
- **Pericardiocentesis** กรณี **large effusion** (หรือ tamponade, หรือต้องการส่งน้ำตรวจหาสาเหตุ — เสริม)
''',
        pearls=[
            "Low voltage: limb < 5 mm, precordial < 10 mm (ซ้าย 5 ขวา 10)",
            "Electrical alternans = large effusion",
            "Flask-shaped heart + ปอดใส = effusion ไม่ใช่ HF",
            "Echo = gold standard",
        ],
        items=[
            mcq("CARDIO-04-02-1",
                "A 62-year-old woman with lung cancer has progressive dyspnea. BP 118/72 mmHg, no pulsus paradoxus. Chest X-ray shows an enlarged, globular heart with clear lung fields. EKG shows QRS amplitude of 4 mm in the limb leads and 8 mm in the precordial leads with alternating QRS heights. What is the most appropriate investigation to confirm the diagnosis?",
                "Echocardiography",
                ["CT pulmonary angiography", "Cardiac MRI", "Serum BNP", "Coronary angiography"],
                explain='''Flask-shaped heart + ปอดใส + **low voltage (ซ้าย < 5, ขวา < 10)** + **electrical alternans** = **large pericardial effusion** (ในผู้ป่วยมะเร็ง) → ยืนยันด้วย **echocardiography (gold standard)** (สไลด์หน้า 196–198)
- CTPA ใช้หา pulmonary embolism ไม่ใช่ effusion
- Cardiac MRI เห็น effusion ได้แต่ไม่ใช่การตรวจแรก ใช้เวลานาน และไม่เหมาะกับคนเหนื่อย
- BNP ช่วยเรื่อง HF แต่ CXR ไม่มี pulmonary congestion
- Coronary angiography ใช้ใน ACS''',
                pearl="สงสัย pericardial effusion → echo",
                topic="Effusion investigation", ref=[f"{D} หน้า 196–198"], nl=["3.3.23"]),
            mcq("CARDIO-04-02-2",
                "A 45-year-old man on maintenance hemodialysis has a chest X-ray showing a markedly enlarged cardiac silhouette. Which combination of EKG findings best supports a large pericardial effusion?",
                "Low QRS voltage with electrical alternans",
                ["Diffuse ST elevation with PR depression only",
                 "Left ventricular hypertrophy with strain pattern",
                 "Peaked T waves with wide QRS",
                 "Right bundle branch block with S1Q3T3"],
                explain='''Large effusion ทำให้ **QRS เตี้ย (low voltage: limb < 5 mm, precordial < 10 mm)** และหัวใจแกว่งไปมาในถุงน้ำจนเกิด **electrical alternans** (สไลด์หน้า 196–197) · uremia เป็นสาเหตุหนึ่งของ effusion
- Diffuse STE + PR depression เป็น EKG ของ acute pericarditis ไม่ได้บอกขนาดน้ำ
- LVH with strain ทำให้ QRS **สูง** ตรงข้ามกับ effusion
- Peaked T กับ wide QRS เป็นลักษณะ hyperkalemia (พบในผู้ป่วยไตได้แต่ไม่ใช่ effusion)
- RBBB + S1Q3T3 ชวนนึกถึง PE''',
                pearl="Low voltage + electrical alternans = large effusion",
                topic="Effusion EKG", ref=[f"{D} หน้า 196–197"], nl=["3.1.12", "2.3.9-3(6)"]),
        ]),
    # ------------------------------------------------------------------ tamponade
    sec("cardio-04-03", "Cardiac tamponade",
        "Beck's triad (↓BP, muffled HS, ↑JVP) + pulsus paradoxus + ปอดใส → pericardiocentesis", minutes=6,
        source=f"{D} หน้า 193, 199, 210–217", nl=["2.2.2", "B7.2.3(1)"],
        md='''
### กลไก
น้ำ/เลือดในเยื่อหุ้มหัวใจกดห้องหัวใจ → ventricle รับเลือดไม่ได้ → stroke volume ตก → obstructive shock

### อาการและอาการแสดง
- **Beck's triad: ↓BP · distant/muffled heart sounds · ↑JVP**
- เหนื่อย, ชีพจรเร็ว
- **Pulsus paradoxus**: SBP ลด > 10 mmHg ตอนหายใจเข้า
- อาการ right HF (JVP สูง ตับโต) แต่ **ปอดใส** (lung clear)
- EKG: low voltage, electrical alternans

[[fig:tamp-phys]]

### Pulsus paradoxus วัดอย่างไร (เสริม จากข้อสอบสไลด์หน้า 211)
ค่อย ๆ ปล่อย cuff: ได้ยิน Korotkoff sound **เป็นช่วง ๆ (เฉพาะตอนหายใจออก)** ที่ 100 mmHg และได้ยิน **ทุกจังหวะ** ที่ 80 mmHg → ต่างกัน 20 mmHg > 10 = pulsus paradoxus

### การรักษา
- **Pericardiocentesis** (definitive)
- **IV fluid ให้ด้วยความระวัง** เพื่อพยุง preload ระหว่างรอ
- เลี่ยง positive pressure ventilation และยาขับปัสสาวะ/vasodilator (ลด preload) (เสริม)
- Inotrope/vasopressor ไม่แก้ปัญหาการกดทับ

| | Tamponade | Constrictive | Acute HF (LV) |
|---|---|---|---|
| BP | ต่ำ | มักปกติ | ปกติ/สูง/ต่ำ |
| JVP | สูง | สูง + Kussmaul | สูง |
| ปอด | **ใส** | ใส | **crepitation** |
| Heart sound | muffled | pericardial knock | S3 gallop |
| Pulsus paradoxus | **เด่น** | บางครั้ง | ไม่มี |
| Echo | effusion + RA/RV collapse (เสริม) | เยื่อหุ้มหนา | EF ต่ำ |

> คีย์เวิร์ดข้อสอบ: **ผู้ป่วยมะเร็ง (CA breast, CA lung) + BP ต่ำ + JVP สูง + เสียงหัวใจเบา + ปอดใส** = **malignant pericardial effusion with tamponade** → pericardiocentesis
''',
        figs=[fig("tamp-phys", "กลไก pulsus paradoxus ใน cardiac tamponade", tamp_svg,
                  "ตอนหายใจเข้า RV ได้เลือดมากขึ้นแต่ขยายออกด้านนอกไม่ได้ จึงดัน septum ไปเบียด LV ทำให้ stroke volume และ SBP ลดลงเกิน 10 mmHg")],
        pearls=[
            "Beck's triad: hypotension + muffled HS + ↑JVP",
            "Pulsus paradoxus: SBP ลด > 10 mmHg ตอนหายใจเข้า",
            "JVP สูง + ปอดใส + BP ต่ำ = tamponade (ไม่ใช่ LV failure)",
            "มะเร็ง + Beck's triad → pericardiocentesis",
            "IV fluid ระหว่างรอ แต่ห้าม diuretic",
        ],
        items=[
            mcq("CARDIO-04-03-1",
                "A woman with breast cancer, post modified radical mastectomy and chemotherapy, has progressive dyspnea for 2 weeks. JVP is raised up to the angle of the mandible. While deflating the BP cuff, Korotkoff sounds are heard intermittently at 100 mmHg and clearly with every beat at 80 mmHg. What is the most likely diagnosis?",
                "Cardiac tamponade",
                ["Congestive heart failure", "Constrictive pericarditis", "Superior vena cava syndrome", "Pulmonary embolism"],
                explain='''Korotkoff ได้ยินเป็นช่วงที่ 100 แต่ได้ยินทุกจังหวะที่ 80 = SBP ต่างกันตามการหายใจ 20 mmHg = **pulsus paradoxus** + JVP สูงมาก + มะเร็งเต้านม = **malignant pericardial effusion with cardiac tamponade** (สไลด์หน้า 193, 211)
- CHF มี pulmonary congestion, S3 และไม่มี pulsus paradoxus เด่น
- Constrictive pericarditis เป็นเรื้อรัง เด่น Kussmaul sign และ pericardial knock (มักหลัง radiation/TB นานเป็นปี)
- SVC syndrome ทำให้หน้า คอ แขนบวม เส้นเลือดดำโป่ง แต่ไม่มี pulsus paradoxus
- PE ทำให้เหนื่อยเฉียบพลัน hypoxemia และ pulsus paradoxus ไม่ใช่ลักษณะเด่น''',
                pearl="Korotkoff เป็นช่วงแล้วต่อเนื่องห่างกัน > 10 mmHg = pulsus paradoxus",
                topic="Pulsus paradoxus", ref=[f"{D} หน้า 210–211"], nl=["2.2.2"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 210"),
            mcq("CARDIO-04-03-2",
                "A 40-year-old woman has dyspnea on exertion. BP 90/60 mmHg, PR 110/min, RR 24/min, JVP 20 cmH2O. Lungs are clear with equal breath sounds and no adventitious sounds. Heart sounds are of low intensity and there is 1+ pitting edema. What is the most likely diagnosis?",
                "Cardiac tamponade",
                ["Pulmonary embolism", "Nephrotic syndrome", "Chronic kidney disease", "Left ventricular failure"],
                explain='''**BP ต่ำ + JVP สูง + เสียงหัวใจเบา** (Beck's triad) + tachycardia + **ปอดใส** = **cardiac tamponade** (สไลด์หน้า 199, 213)
- PE ทำให้ BP ต่ำและ JVP สูงได้ แต่เสียงหัวใจไม่เบา มักมี hypoxemia และ loud P2
- Nephrotic syndrome บวมทั่วตัวแต่ JVP ไม่สูงและไม่มี hypotension จากการกดทับหัวใจ
- CKD มี volume overload แต่ปอดมักมี congestion และไม่มีเสียงหัวใจเบา
- LV failure ต้องมี crepitation/pulmonary edema''',
                pearl="JVP สูง + ปอดใส + BP ต่ำ + เสียงหัวใจเบา = tamponade",
                topic="Beck's triad", ref=[f"{D} หน้า 212–213"], nl=["2.2.2"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 212"),
            mcq("CARDIO-04-03-3",
                "A patient with stage IIIA breast cancer presents with dyspnea. BP 70/40 mmHg. Examination shows neck vein engorgement, equal breath sounds in both lungs, decreased S1S2 and no murmur. After initial resuscitation, what is the most appropriate management?",
                "Pericardiocentesis",
                ["Dobutamine infusion", "Dopamine infusion", "Furosemide IV", "Large-volume NSS as definitive therapy"],
                explain='''มะเร็ง + Beck's triad (BP 70/40, คอโป่ง, เสียงหัวใจเบา) + ปอดปกติ = **cardiac tamponade** → การรักษาที่แก้ต้นเหตุคือ **pericardiocentesis** (สไลด์หน้า 199, 217)
- Dobutamine และ dopamine เพิ่มการบีบตัว แต่ปัญหาคือ **หัวใจรับเลือดไม่ได้** เพราะถูกกด ยาจึงไม่ช่วยและอาจทำให้แย่ลงจาก tachycardia
- Furosemide ลด preload ทำให้ BP ตกหนักขึ้น
- NSS ช่วยพยุงชั่วคราวได้ (ให้ด้วยความระวัง) แต่ไม่ใช่ definitive treatment''',
                pearl="Tamponade: pericardiocentesis คือการรักษา ยาเป็นแค่สะพาน",
                topic="Tamponade treatment", ref=[f"{D} หน้า 216–217"], nl=["2.2.2"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 216"),
            mcq("CARDIO-04-03-4",
                "A 45-year-old man with lung cancer on chemotherapy has dizziness for 1 week. BT 36.5°C, BP 80/50 mmHg, RR 12/min. JVP is raised to the mid-cervical level, heart sounds are decreased and the lungs are clear. EKG shows generalized low voltage. What is the most likely diagnosis?",
                "Cardiac tamponade",
                ["Pulmonary embolism", "Acute pericarditis", "Congestive heart failure", "Septic shock"],
                explain='''มะเร็งปอด + hypotension + JVP สูง + เสียงหัวใจเบา + ปอดใส + **low voltage** = **cardiac tamponade** จาก malignant effusion (สไลด์หน้า 215)
- PE ทำให้ RR เร็ว hypoxemia และไม่ทำให้เสียงหัวใจเบาหรือ low voltage (RR ผู้ป่วย 12)
- Acute pericarditis มีเจ็บอก pleuritic, rub และ diffuse STE ไม่ได้มี shock
- CHF มี crepitation และ S3
- Septic shock มีไข้หรืออุณหภูมิผิดปกติ และ JVP ต่ำ (distributive)''',
                pearl="Low voltage + JVP สูง + hypotension ในคนมะเร็ง = tamponade",
                topic="Malignant tamponade", ref=[f"{D} หน้า 214–215"], nl=["2.2.2"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 214"),
        ]),
    # ------------------------------------------------------------------ dissection
    sec("cardio-04-04", "Aortic dissection",
        "เจ็บฉีกร้าวไปหลัง + BP/pulse สองแขนไม่เท่ากัน → CTA · IV beta-blocker ก่อน vasodilator · type A ผ่าตัด", minutes=7,
        source=f"{D} หน้า 218–230", nl=["2.3.9-3(2)", "2.2.6", "B7.2.6-3(1)"],
        md='''
### กลไกและปัจจัยเสี่ยง
- **Intima ฉีกขาด → เลือดเซาะเข้าชั้น intima–media** เกิด false lumen
- Risk: **HT (พบบ่อยที่สุด)**, trauma, connective tissue disease (Marfan, Ehlers-Danlos), bicuspid AV, cocaine (เสริม)

### อาการ
- **เจ็บเฉียบพลัน รุนแรง แบบฉีก/ร้าว (tearing/ripping) ร้าวไปหลัง**
- BP มักสูง · **BP ต่ำ** เมื่อเสียเลือดมากหรือเกิด **cardiac tamponade**
- **BP และ pulse สองข้างไม่เท่ากัน** (ปกติ BP สองแขนต่างกัน **< 10 mmHg**) · pulse ขาเบากว่าแขน

### ภาวะแทรกซ้อน (ตามแขนงที่ถูกเซาะ)
- **AR** (เซาะถึง aortic root) · **MI** (มักเป็น RCA → inferior STEMI) · **cardiac tamponade**
- **Stroke** (carotid) · **AKI** (renal artery) · **paraplegia** (spinal artery) · mesenteric/limb ischemia (เสริม)

### Investigation
- **EKG: R/O STEMI** (และระวัง — dissection ที่เซาะ RCA ทำให้ STE ได้)
- **CXR: widened mediastinum**
- **CTA chest, abdomen and pelvis = gold standard**
- **Echocardiography (TEE)** เมื่อ **unstable** หรือ **renal failure** (เลี่ยง contrast)

[[fig:dissection]]

### การรักษา
- **BP ต่ำ**: IV fluid, vasopressor (หา tamponade/rupture)
- **BP สูง**: คุม BP เพื่อไม่ให้ dissection ลาม — **เป้า SBP 100–120 mmHg และ HR ≤ 60 bpm**
  1. **IV beta-blocker ก่อน (labetalol, esmolol)** — ลด dP/dt และ HR
  2. **แล้วค่อย IV vasodilator (nicardipine, NTG)** ถ้า BP ยังสูง — ต้องตามหลัง BB เพื่อ **ป้องกัน reflex tachycardia**
- **Pain control** เช่น morphine
- **Vascular surgery**: **Stanford A** (มี ascending aorta) ทุกราย · **Stanford B ที่มี complication** (malperfusion, rupture, ปวดไม่หาย)
- **ห้าม thrombolytic, anticoagulant, antiplatelet** แม้มี STE หรือ stroke (เสริม)

> โจทย์ "เจ็บอกร้าวไปหลัง + อ่อนแรงครึ่งซีก + BP สองแขนต่างกันมาก" = **aortic dissection with stroke** → **IV labetalol** ไม่ใช่ rt-PA
''',
        figs=[fig("dissection", "Stanford classification และลำดับยา", dis_svg,
                  "ซ้ายแสดงตำแหน่งที่ฉีก (เส้นแดง): Stanford A มี ascending aorta ต้องผ่าตัด, Stanford B อยู่ descending อย่างเดียว ขวาคือลำดับการคุม BP")],
        pearls=[
            "เจ็บฉีกร้าวไปหลัง + BP สองแขนต่าง ≥ 10 mmHg = aortic dissection",
            "CTA chest-abdomen-pelvis = gold standard · TEE ถ้า unstable/ไตวาย",
            "IV beta-blocker ก่อน แล้วค่อย vasodilator · เป้า SBP 100–120, HR ≤ 60",
            "Stanford A = ผ่าตัด · B = ยา (ผ่าตัดถ้ามี complication)",
            "Dissection + stroke/STE → ห้าม thrombolytic",
        ],
        items=[
            mcq("CARDIO-04-04-1",
                "A 60-year-old man develops severe chest pain radiating to the back while driving. He has HT and smokes, with GERD and COPD. BP 190/100 mmHg, PR 110/min, SpO2 98%. He is distressed; the left radial pulse is weaker than the right, JVP is flat, S1S2 normal, no murmur, breath sounds normal. What is the most likely diagnosis?",
                "Acute aortic dissection",
                ["Ruptured esophagus", "Acute pulmonary embolism", "Acute myocardial infarction", "Spontaneous pneumothorax"],
                explain='''HT + เจ็บอกรุนแรง **ร้าวไปหลัง** + **pulse สองแขนไม่เท่ากัน** = **acute aortic dissection** (สไลด์หน้า 218, 222)
- Esophageal rupture มักตามหลังอาเจียนรุนแรง มี subcutaneous emphysema/pneumomediastinum ไม่ทำให้ pulse ไม่เท่ากัน
- PE ทำให้เหนื่อย hypoxemia (SpO2 ผู้ป่วย 98%) และ JVP สูง
- Acute MI เจ็บแน่นร้าวแขน/กราม pulse สองแขนเท่ากัน
- Pneumothorax ทำให้เสียงหายใจลดข้างหนึ่ง แต่ผู้ป่วยเสียงปกติ''',
                pearl="Pulse/BP สองแขนต่างกัน = dissection จนกว่าพิสูจน์ได้ว่าไม่ใช่",
                topic="Dissection diagnosis", ref=[f"{D} หน้า 221–222"], nl=["2.3.9-3(2)", "2.1.35"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 221"),
            mcq("CARDIO-04-04-2",
                "A 70-year-old man has sudden chest pain radiating to the back. BP 170/100 mmHg. The pulse in the left arm and both legs is weak or absent. What is the most appropriate initial medication?",
                "IV beta-blocker",
                ["Oral enalapril", "IV hydralazine", "Oral amlodipine", "IV alteplase"],
                explain='''Aortic dissection ที่ BP สูง → ลด shear stress ด้วย **IV beta-blocker เป็นอันดับแรก** (labetalol, esmolol) เป้า SBP 100–120 และ HR ≤ 60 (สไลด์หน้า 220, 226)
- Enalapril และ amlodipine ชนิดกินออกฤทธิ์ช้าไป ไม่ได้ลด HR
- Hydralazine เป็น vasodilator ที่ทำให้ **reflex tachycardia** เพิ่ม dP/dt ทำให้ dissection ลามถ้าให้ก่อน BB
- Alteplase เป็น thrombolytic **ห้ามเด็ดขาด** ใน dissection''',
                pearl="Dissection: BB ก่อนเสมอ",
                topic="Dissection BP control", ref=[f"{D} หน้า 225–226"], nl=["2.3.9-3(2)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 225"),
            mcq("CARDIO-04-04-3",
                "A 70-year-old man with DM and HT has chest pain radiating to the back 30 minutes before arrival. While waiting he develops right-sided weakness. BP right arm 130/60 mmHg, left arm 200/100 mmHg, HR 86/min. He has dysarthria, left facial palsy, right hemiplegia and a right Babinski sign. EKG shows sinus rhythm with LVH. What is the most appropriate management?",
                "IV labetalol",
                ["IV rt-PA", "Oral amlodipine", "IV sodium nitroprusside alone", "Aspirin plus clopidogrel"],
                explain='''เจ็บอกร้าวไปหลัง + **BP สองแขนต่างกัน 70 mmHg** + stroke = **aortic dissection ที่เซาะ carotid** → ยาเริ่มต้นคือ **IV beta-blocker (labetalol)** และเตรียมผ่าตัด (สไลด์หน้า 230)
- rt-PA ใน stroke จาก dissection ทำให้เลือดออกในผนังหลอดเลือดลุกลาม/ rupture — ห้าม
- Amlodipine กินออกฤทธิ์ช้า ไม่ลด HR
- Nitroprusside เดี่ยว ๆ ทำให้ reflex tachycardia — ใช้ได้เฉพาะหลังให้ BB แล้ว
- Aspirin + clopidogrel เพิ่มเลือดออก ห้ามใน dissection''',
                pearl="Stroke + เจ็บอกร้าวหลัง + BP สองแขนต่าง → คิด dissection ห้าม rt-PA",
                topic="Dissection with stroke", ref=[f"{D} หน้า 229–230"], nl=["2.3.9-3(2)", "2.2.6"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 229"),
            mcq("CARDIO-04-04-4",
                "A 50-year-old man with poorly controlled HT has severe progressive chest pain radiating to the back for 1 hour. BP 100/80 mmHg. Pulses are regular, 2+ in the upper limbs and 1+ in the lower limbs. Creatinine is 2.8 mg/dL and he is hemodynamically unstable. Which imaging is most appropriate to confirm the diagnosis?",
                "Bedside transesophageal echocardiography",
                ["CT angiography of chest, abdomen and pelvis", "Coronary angiography", "Ventilation-perfusion scan", "Plain chest X-ray only"],
                explain='''อาการเข้าได้กับ **aortic dissection** (เจ็บร้าวหลัง pulse ขาเบากว่าแขน) · ปกติ gold standard คือ CTA แต่ผู้ป่วย **unstable และมี renal failure** → ใช้ **echocardiography (TEE) ข้างเตียง** ตามสไลด์หน้า 219
- CTA C/A/P เป็น gold standard ในคนที่ stable แต่ต้องย้ายไปห้อง CT และใช้ contrast ในคน Cr สูง
- Coronary angiography ใช้ใน ACS และอาจทำให้ dissection แย่ลง
- V/Q scan ใช้หา PE
- CXR เห็น widened mediastinum ได้แต่ไม่พอวินิจฉัย''',
                pearl="Dissection + unstable หรือไตวาย → TEE",
                topic="Dissection imaging", ref=[f"{D} หน้า 219, 223–224"], nl=["2.3.9-3(2)", "3.3.23"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 223 (ปรับโจทย์)"),
            mcq("CARDIO-04-04-5",
                "A middle-aged man has sudden chest pain. BP is 173/110 mmHg in the right arm and 153/100 mmHg in the left arm. CTA confirms aortic dissection. What is the most appropriate management?",
                "IV esmolol",
                ["IV rt-PA", "Warfarin", "Aspirin", "IV nicardipine as the first agent"],
                explain='''Aortic dissection ที่ BP สูง → **IV beta-blocker ก่อน (esmolol)** แล้วค่อยเพิ่ม vasodilator (สไลด์หน้า 228) · BP สองแขนต่างกัน 20 mmHg (ปกติ < 10)
- rt-PA, warfarin และ aspirin เพิ่มเลือดออกในผนังหลอดเลือด ห้ามใช้
- Nicardipine ใช้ได้เป็นตัวที่สอง ถ้าให้ก่อน BB จะเกิด reflex tachycardia''',
                pearl="Esmolol/labetalol ก่อน nicardipine/NTG",
                topic="Dissection drug order", ref=[f"{D} หน้า 227–228"], nl=["2.3.9-3(2)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 227"),
        ]),
    ])
