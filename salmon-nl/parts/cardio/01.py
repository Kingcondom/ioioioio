from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Cardio"

def mk(sid):
    return (f'<defs><marker id="{sid}-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            f'markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>')

# ---------- fig: ACLS cardiac arrest ----------
def step(x, y, w, cls, l1, l2=None):
    cx = x + w / 2
    if l2:
        return (f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="9" class="{cls}"/>'
                f'<text x="{cx}" y="{y+19}" text-anchor="middle" class="tb">{l1}</text>'
                f'<text x="{cx}" y="{y+37}" text-anchor="middle" class="t3">{l2}</text>')
    return (f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="9" class="{cls}"/>'
            f'<text x="{cx}" y="{y+28}" text-anchor="middle" class="tb">{l1}</text>')

def arrow(sid, x, y1, y2):
    return f'<path d="M{x} {y1}V{y2}" class="ln" marker-end="url(#{sid}-a)"/>'

S2 = "cardio-01-02"
acls_svg = (f'<svg viewBox="0 0 720 450">{mk(S2)}'
    + step(190, 8, 340, "acsoft", "Cardiac arrest: CPR 30:2 + O2", "ติด monitor/defibrillator ให้เร็วที่สุด")
    + arrow(S2, 360, 54, 76)
    + step(250, 78, 220, "box", "Shockable rhythm?")
    + f'<path d="M290 124L190 154" class="ln" marker-end="url(#{S2}-a)"/>'
    + f'<path d="M430 124L530 154" class="ln" marker-end="url(#{S2}-a)"/>'
    + '<text x="215" y="132" class="t3">ใช่</text><text x="490" y="132" class="t3">ไม่ใช่</text>'
    + step(30, 156, 310, "badsoft", "VF / pulseless VT", "shockable")
    + step(380, 156, 310, "c1soft", "Asystole / PEA", "non-shockable")
    + arrow(S2, 185, 202, 216)
    + step(30, 218, 310, "box", "Shock 1 → CPR 2 นาที", "biphasic 120–200 J (เสริม)")
    + arrow(S2, 185, 264, 278)
    + step(30, 280, 310, "box", "Shock 2 → CPR + Epinephrine 1 mg", "ซ้ำทุก 3–5 นาที")
    + arrow(S2, 185, 326, 340)
    + step(30, 342, 310, "box", "Shock 3 → CPR + Amiodarone 300 mg", "หรือ lidocaine · dose 1 หลัง shock ครั้งที่ 3")
    + arrow(S2, 185, 388, 400)
    + step(30, 402, 310, "box", "Shock 5 → Amiodarone 150 mg", "dose 2 (3–5 นาทีหลัง dose 1)")
    + arrow(S2, 535, 202, 216)
    + step(380, 218, 310, "box", "Epinephrine 1 mg IV ASAP", "พร้อม CPR ต่อเนื่อง")
    + arrow(S2, 535, 264, 278)
    + step(380, 280, 310, "box", "CPR 2 นาที + epi ทุก 3–5 นาที", "ไม่ shock · ไม่ให้ atropine")
    + arrow(S2, 535, 326, 340)
    + step(380, 342, 310, "box", "ค้นหาและแก้ Hs &amp; Ts", "hypoxia · hypovolemia · K · tamponade ฯลฯ")
    + arrow(S2, 535, 388, 400)
    + step(380, 402, 310, "misssoft", "ตรวจ rhythm ทุก 2 นาที", "กลายเป็น VF/VT → ไปฝั่ง shock")
    + '</svg>')

# ---------- fig: tachycardia grid ----------
S3 = "cardio-01-03"
def cell(x, y, w, h, cls, lines):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" class="{cls}"/>'
    yy = y + 22
    for i, (c, t) in enumerate(lines):
        out += f'<text x="{x+12}" y="{yy}" class="{c}">{t}</text>'
        yy += 19
    return out

tachy_svg = (f'<svg viewBox="0 0 740 450">{mk(S3)}'
    + '<rect x="170" y="8" width="400" height="40" rx="9" class="acsoft"/>'
    + '<text x="370" y="33" text-anchor="middle" class="tb">Tachycardia ที่ยังคลำ pulse ได้</text>'
    + arrow(S3, 370, 48, 66)
    + '<rect x="170" y="68" width="400" height="56" rx="9" class="box"/>'
    + '<text x="370" y="90" text-anchor="middle" class="tb">Unstable? hypotension · AOC · shock</text>'
    + '<text x="370" y="110" text-anchor="middle" class="t2">chest discomfort · acute heart failure</text>'
    + f'<path d="M570 96H596" class="ln" marker-end="url(#{S3}-a)"/>'
    + '<text x="574" y="88" class="t3">ใช่</text>'
    + '<rect x="600" y="68" width="132" height="56" rx="9" class="bad"/>'
    + '<text x="666" y="91" text-anchor="middle" class="tw">Synchronized</text>'
    + '<text x="666" y="110" text-anchor="middle" class="tw">cardioversion</text>'
    + arrow(S3, 370, 124, 150)
    + '<text x="380" y="142" class="t3">ไม่ใช่ (stable) → ดู QRS กับ rhythm</text>'
    + '<rect x="140" y="154" width="292" height="30" rx="7" class="sunk"/>'
    + '<text x="286" y="174" text-anchor="middle" class="tb">Narrow QRS (&lt; 0.12 s)</text>'
    + '<rect x="442" y="154" width="290" height="30" rx="7" class="sunk"/>'
    + '<text x="587" y="174" text-anchor="middle" class="tb">Wide QRS (≥ 0.12 s)</text>'
    + '<rect x="8" y="192" width="124" height="118" rx="9" class="sunk"/>'
    + '<text x="70" y="256" text-anchor="middle" class="tb">Regular</text>'
    + '<rect x="8" y="318" width="124" height="124" rx="9" class="sunk"/>'
    + '<text x="70" y="385" text-anchor="middle" class="tb">Irregular</text>'
    + cell(140, 192, 292, 118, "oksoft", [("tb", "SVT · atrial flutter"), ("", "1. Vagal maneuver"),
                                           ("", "2. Adenosine IV push"), ("", "3. Beta-blocker / non-DHP CCB"),
                                           ("t3", "flutter = sawtooth P wave")])
    + cell(442, 192, 290, 118, "misssoft", [("tb", "Monomorphic VT"), ("", "QRS รูปเดียวกันทุกตัว"),
                                             ("", "Amiodarone IV (เสริม)"), ("", "ไม่ดีขึ้น → sync cardioversion"),
                                             ("t3", "unstable → cardioversion ทันที")])
    + cell(140, 318, 292, 124, "oksoft", [("tb", "AF · flutter · MAT"), ("", "Rate control: BB / non-DHP CCB"),
                                           ("", "+ ประเมิน anticoagulant"), ("t3", "MAT = P wave ≥ 3 รูปแบบ"),
                                           ("t3", "MAT: รักษาโรคปอดที่เป็นเหตุ (เสริม)")])
    + cell(442, 318, 290, 124, "badsoft", [("tb", "Polymorphic VT"), ("", "pulseless/unstable → defibrillation"),
                                            ("tb", "AF + WPW (delta wave)"), ("", "ห้าม adenosine/BB/CCB/digoxin"),
                                            ("t3", "→ cardioversion / procainamide (เสริม)")])
    + '</svg>')

# ---------- fig: AF management ----------
S4 = "cardio-01-04"
af_svg = (f'<svg viewBox="0 0 730 430">{mk(S4)}'
    + '<rect x="215" y="8" width="300" height="40" rx="9" class="acsoft"/>'
    + '<text x="365" y="33" text-anchor="middle" class="tb">AF (irregularly irregular, no P)</text>'
    + arrow(S4, 365, 48, 66)
    + '<rect x="215" y="68" width="300" height="40" rx="9" class="box"/>'
    + '<text x="365" y="93" text-anchor="middle" class="tb">Hemodynamically unstable?</text>'
    + f'<path d="M515 88H556" class="ln" marker-end="url(#{S4}-a)"/>'
    + '<text x="522" y="80" class="t3">ใช่</text>'
    + '<rect x="560" y="62" width="162" height="52" rx="9" class="bad"/>'
    + '<text x="641" y="84" text-anchor="middle" class="tw">Sync cardioversion</text>'
    + '<text x="641" y="103" text-anchor="middle" class="tw">+ anticoagulant</text>'
    + f'<path d="M300 108L190 140" class="ln" marker-end="url(#{S4}-a)"/>'
    + f'<path d="M430 108L540 140" class="ln" marker-end="url(#{S4}-a)"/>'
    + '<text x="365" y="134" text-anchor="middle" class="t3">stable: ทำทั้งสองอย่าง</text>'
    + cell(10, 142, 350, 148, "oksoft", [("tb", "1) Rate control — goal HR &lt; 110"),
                                         ("", "1st: BB (esmolol, metoprolol, atenolol,"),
                                         ("", "      propranolol) / diltiazem, verapamil"),
                                         ("", "2nd: digoxin, amiodarone"),
                                         ("t3", "ยังมีอาการ → goal &lt; 80 หรือ rhythm control"),
                                         ("t3", "rhythm: flecainide, propafenone, amiodarone")])
    + cell(370, 142, 352, 148, "c1soft", [("tb", "2) Anticoagulant — ดูใคร?"),
                                          ("", "Mod–severe MS · mechanical valve · HCM"),
                                          ("ta", "→ Warfarin (ห้าม DOAC ใน MS/valve)"),
                                          ("", "อื่น ๆ ใช้ CHA2DS2-VASc"),
                                          ("ta", "≥ 1 ชาย / ≥ 2 หญิง → DOAC หรือ warfarin"),
                                          ("t3", "0 ชาย / 1 หญิง → ไม่ต้อง (เสริม)")])
    + '<rect x="10" y="304" width="712" height="118" rx="9" class="sunk"/>'
    + '<text x="24" y="328" class="tb">CHA2DS2-VASc (เสริม — สไลด์หน้า 30 เป็นภาพ)</text>'
    + '<text x="24" y="354">C · CHF = 1</text><text x="200" y="354">H · HT = 1</text><text x="360" y="354">A2 · อายุ ≥ 75 = 2</text><text x="560" y="354">D · DM = 1</text>'
    + '<text x="24" y="378">S2 · stroke/TIA/thromboembolism = 2</text><text x="360" y="378">V · vascular disease (MI, PAD) = 1</text>'
    + '<text x="24" y="402">A · อายุ 65–74 = 1</text><text x="200" y="402">Sc · เพศหญิง = 1</text><text x="360" y="402" class="t3">คะแนนเต็ม 9</text>'
    + '</svg>')

# ---------- fig: AV block ECG schematic ----------
S5 = "cardio-01-05"
def ecg_row(y, ps, qrs, wide=False, drops=()):
    base = y + 40
    out = f'<path d="M180 {base}H712" class="lnf"/>'
    for p in ps:
        out += f'<path d="M{p} {base}q7 -14 14 0" class="lnc1"/>'
    for q in qrs:
        if wide:
            out += f'<path d="M{q} {base}l6 6l8 -34l10 40l6 -12" class="lna"/>'
        else:
            out += f'<path d="M{q} {base}l3 4l5 -32l5 36l3 -8" class="lna"/>'
    for d in drops:
        out += f'<text x="{d+7}" y="{base+22}" text-anchor="middle" class="t3">drop</text>'
    return out

def lab(y, a, b):
    return (f'<text x="12" y="{y+30}" class="tb">{a}</text>'
            f'<text x="12" y="{y+50}" class="t3">{b}</text>')

p1 = [190 + 85 * i for i in range(7)]
row1 = ecg_row(10, p1, [p + 52 for p in p1])
p2 = [190 + 76 * i for i in range(7)]
pr2 = [26, 40, 54, None, 26, 40, 54]
row2 = ecg_row(95, p2, [p + d for p, d in zip(p2, pr2) if d], drops=[p2[3]])
pr3 = [28, 28, None, 28, 28, None, 28]
row3 = ecg_row(180, p2, [p + d for p, d in zip(p2, pr3) if d], drops=[p2[2], p2[5]])
p4 = [190 + 62 * i for i in range(9)]
row4 = ecg_row(265, p4, [212, 332, 455, 578], wide=True)
avb_svg = ('<svg viewBox="0 0 720 360">'
    + '<rect x="6" y="6" width="166" height="348" rx="9" class="sunk"/>'
    + lab(10, "1st degree", "PR > 0.20 s คงที่ทุกตัว")
    + lab(95, "Mobitz I", "PR ยาวขึ้นจน drop")
    + lab(180, "Mobitz II", "PR คงที่ แล้ว drop ทันที")
    + lab(265, "3rd degree", "P กับ QRS ไม่สัมพันธ์")
    + row1 + row2 + row3 + row4
    + '<text x="712" y="352" text-anchor="end" class="t3">เส้นฟ้า = P wave · เส้นสีหลัก = QRS</text>'
    + '</svg>')


LECTURE = lecture("01", "Resuscitation & arrhythmias",
    subtitle="BLS · ACLS · tachycardia · AF · bradycardia",
    objectives=[
        "แยก shockable กับ non-shockable rhythm และสั่งยา ACLS ตามลำดับได้",
        "อ่าน tachycardia จาก QRS กว้าง/แคบ และ regular/irregular แล้วเลือกการรักษาได้",
        "ตัดสินใจ rate control และ anticoagulant ใน AF ด้วย CHA2DS2-VASc ได้",
        "แยก sinus node dysfunction กับ AV block แต่ละชนิดจาก EKG และรู้ว่าเมื่อไรต้อง pacing",
    ],
    sections=[
    # ------------------------------------------------------------------ BLS
    sec("cardio-01-01", "Adult Basic Life Support (BLS)",
        "ลำดับการช่วยชีวิตพื้นฐาน: ปลุก-เรียก-คลำ pulse-กดอก-AED", minutes=4,
        source=f"{D} หน้า 5", nl=["2.2.3", "B7.2.5(3)"],
        md='''
> สไลด์หน้า 5 เป็นภาพ algorithm ทั้งหน้า (อ่านเป็นข้อความไม่ได้) — เนื้อหาด้านล่างเรียบเรียงตาม AHA Adult BLS มาตรฐาน (เสริม)

### ลำดับ Adult BLS (เสริม)
1. **ดูความปลอดภัยของที่เกิดเหตุ** แล้วปลุกเรียกผู้ป่วย (ตบไหล่ เรียกเสียงดัง)
2. ไม่ตอบสนอง → **ตะโกนขอความช่วยเหลือ เรียก 1669 / code blue และให้คนไปเอา AED**
3. **ดูการหายใจและคลำ carotid pulse พร้อมกัน ไม่เกิน 10 วินาที**
4. ไม่หายใจหรือหายใจเฮือก (gasping) + ไม่มี pulse → **เริ่ม CPR ทันที โดยเริ่มที่การกดหน้าอก (C-A-B)**
5. AED มาถึง → ติดแผ่นแล้ววิเคราะห์ rhythm ทันที · shockable → shock 1 ครั้ง แล้ว **กด CPR ต่อทันที 2 นาที** ค่อยตรวจ rhythm ใหม่
6. มีหายใจแต่ไม่มี pulse ไม่ได้ · มี pulse แต่ไม่หายใจ → rescue breathing 1 ครั้งทุก 6 วินาที (10 ครั้ง/นาที) และเช็ค pulse ทุก 2 นาที

### คุณภาพ CPR (high-quality CPR) (เสริม)
| หัวข้อ | ค่า |
|---|---|
| อัตรากด | 100–120 ครั้ง/นาที |
| ความลึก | 5–6 cm (อย่างน้อย 2 นิ้ว) |
| การคืนตัว | ปล่อยให้หน้าอกคืนตัวเต็มที่ ไม่พิงอก |
| อัตราส่วน (ยังไม่มี advanced airway) | กด 30 : เป่า 2 |
| มี advanced airway แล้ว | กดต่อเนื่อง + ช่วยหายใจ 1 ครั้งทุก 6 วินาที |
| หยุดกด | ให้น้อยที่สุด (< 10 วินาที) · สลับคนกดทุก 2 นาที |

> กับดักข้อสอบ: **ห้ามรอ AED หรือรอวัด BP ก่อนเริ่มกดหน้าอก** และหลัง shock **ไม่ต้องคลำ pulse ทันที** ให้กด CPR ต่อ 2 นาทีก่อน
''',
        pearls=[
            "ไม่ตอบสนอง + ไม่หายใจปกติ + ไม่มี pulse ใน 10 วินาที = เริ่มกดหน้าอกทันที",
            "กด 100–120 ครั้ง/นาที ลึก 5–6 cm อัตรา 30:2 (เสริม)",
            "Shock แล้วกด CPR ต่อทันที 2 นาที ค่อยดู rhythm",
            "มี advanced airway แล้ว: กดต่อเนื่อง ช่วยหายใจทุก 6 วินาที",
        ],
        items=[
            mcq("CARDIO-01-01-1",
                "A 55-year-old man collapses in a shopping mall. He does not respond to shouting or tapping, has only occasional gasping breaths, and no carotid pulse is felt within 10 seconds. Help has been called and someone has gone to get an AED. What is the most appropriate next step?",
                "Start chest compressions immediately",
                ["Give 2 rescue breaths and recheck the pulse",
                 "Wait for the AED before starting CPR",
                 "Measure blood pressure and capillary glucose",
                 "Place him in the recovery position"],
                explain='''ผู้ป่วยไม่ตอบสนอง หายใจเฮือก (gasping ไม่นับว่าหายใจปกติ) และคลำ pulse ไม่ได้ใน 10 วินาที = cardiac arrest ต้อง **เริ่มกดหน้าอกทันที** ตามลำดับ C-A-B
- การเป่าปาก 2 ครั้งก่อนแล้วคลำ pulse ซ้ำ เป็นลำดับ A-B-C แบบเก่า ทำให้เสียเวลากดอก
- การรอ AED ก่อนเริ่ม CPR ทำให้สมองขาดเลือดระหว่างรอ — กดไปก่อนแล้วติด AED ทันทีที่มาถึง
- การวัด BP/น้ำตาล ไม่ใช่สิ่งที่ทำในคนที่ไม่มี pulse
- ท่า recovery position ใช้ในคนที่หมดสติแต่ **หายใจได้และมี pulse** เท่านั้น''',
                pearl="Gasping ไม่ใช่การหายใจ — ไม่มี pulse ให้กดอกทันที",
                topic="BLS sequence", ref=[f"{D} หน้า 5"], nl=["2.2.3"]),
            mcq("CARDIO-01-01-2",
                "During adult CPR without an advanced airway, which combination best describes high-quality chest compressions?",
                "Rate 100–120/min, depth 5–6 cm, compression-to-ventilation ratio 30:2",
                ["Rate 60–80/min, depth 3–4 cm, ratio 15:2",
                 "Rate 80–100/min, depth 4 cm, ratio 30:2",
                 "Rate 120–150/min, depth 6–7 cm, ratio 15:1",
                 "Rate 100–120/min, depth 2–3 cm, continuous compressions without breaths"],
                explain='''high-quality CPR ในผู้ใหญ่ = **กด 100–120 ครั้ง/นาที ลึก 5–6 cm ปล่อยให้อกคืนตัวเต็มที่ และ 30:2 เมื่อยังไม่มี advanced airway** (เสริม — สไลด์หน้า 5 เป็นภาพ)
- อัตรา 60–80 ลึก 3–4 cm ช้าและตื้นเกินไป เลือดไปสมองไม่พอ · 15:2 เป็นสัดส่วนของเด็กเมื่อมีผู้ช่วย 2 คน
- อัตรา 80–100 ช้ากว่าเกณฑ์ และลึก 4 cm ตื้นไป
- อัตราเกิน 120 และลึกเกิน 6 cm ทำให้หัวใจเติมเลือดไม่ทันและเสี่ยงซี่โครงหัก
- ความลึก 2–3 cm ตื้นเกินไป และการกดต่อเนื่องไม่เป่าใช้เมื่อมี advanced airway หรือ hands-only CPR ของคนทั่วไป''',
                pearl="100–120 ครั้ง/นาที · ลึก 5–6 cm · 30:2",
                topic="High-quality CPR", ref=[f"{D} หน้า 5"], nl=["2.2.3"]),
            mcq("CARDIO-01-01-3",
                "A 60-year-old woman in cardiac arrest is receiving bystander CPR. An AED is attached and advises a shock. A shock is delivered. What should be done immediately afterwards?",
                "Resume chest compressions for 2 minutes before reanalysing the rhythm",
                ["Check the carotid pulse for 10 seconds",
                 "Deliver a second shock right away",
                 "Give 2 rescue breaths and then check breathing",
                 "Stop CPR and wait for the paramedic team"],
                explain='''หลัง shock หัวใจแม้กลับมาเต้นก็มักบีบไม่แรงพอในช่วงแรก จึงต้อง **กด CPR ต่อทันที 2 นาที** แล้วให้ AED วิเคราะห์ใหม่ (เสริม)
- การคลำ pulse ทันทีหลัง shock ทำให้หยุดกดนานโดยไม่จำเป็น
- การ shock ซ้ำทันที (stacked shock) ไม่แนะนำแล้ว — ต้องมี CPR 2 นาทีคั่น
- การเป่า 2 ครั้งแล้วดูการหายใจ เป็นการหยุดกดอกที่ไม่จำเป็น
- การหยุด CPR รอทีมทำให้ไม่มีเลือดไปเลี้ยงสมอง''',
                pearl="Shock → กดต่อทันที 2 นาที → ค่อยดู rhythm",
                topic="AED use", ref=[f"{D} หน้า 5"], nl=["2.2.3"]),
        ]),
    # ------------------------------------------------------------------ ACLS
    sec("cardio-01-02", "Adult Cardiac Arrest (ACLS)",
        "VF/pVT → shock · asystole/PEA → epinephrine ASAP · amiodarone หลัง shock ครั้งที่ 3", minutes=7,
        source=f"{D} หน้า 6–19", nl=["2.2.3", "B7.2.5(3)", "B7.4(7)"],
        md='''
### 4 rhythm ของ cardiac arrest
| Rhythm | ลักษณะ EKG | กลุ่ม |
|---|---|---|
| Ventricular fibrillation (VF) | คลื่นยุ่งเหยิง ไม่มี QRS ชัด | **shockable** |
| Pulseless VT | wide QRS regular แต่คลำ pulse ไม่ได้ | **shockable** |
| Asystole | เส้นตรง (ยืนยันด้วยดูหลาย lead/เพิ่ม gain) | non-shockable |
| Pulseless electrical activity (PEA) | **EKG อะไรก็ได้ที่ไม่มี pulse** ที่ไม่ใช่ VF, VT, asystole | non-shockable |

> ข้อสอบชอบให้ EKG "ดูเหมือนปกติ" แต่โจทย์บอกว่า **คลำ pulse ไม่ได้** = PEA → **Epinephrine ASAP + CPR** ไม่ใช่ atropine ไม่ใช่ shock

[[fig:acls-algo]]

### Shockable: VF / pulseless VT
- CPR + **defibrillation (unsynchronized)** ให้เร็วที่สุด — shock สำคัญที่สุด ยาเป็นแค่ส่วนเสริม
- Epinephrine 1 mg IV/IO ทุก 3–5 นาที (เริ่มหลัง shock ครั้งที่ 2 ตาม AHA) (เสริม)
- **Amiodarone หรือ lidocaine**: dose แรก **ให้หลัง shock ครั้งที่ 3** · dose ที่ 2 **ให้หลัง shock ครั้งที่ 5** (ห่างจาก dose แรก 3–5 นาที)
- ขนาดยา (เสริม): amiodarone 300 mg IV bolus → 150 mg · lidocaine 1–1.5 mg/kg → 0.5–0.75 mg/kg
- ถ้าโจทย์บอกว่าให้ adrenaline ไปแล้วหลาย dose แต่ยังเป็น pulseless VT → คำตอบคือ **defibrillation** (shock ต้องมาก่อนยาเสมอ)

### Non-shockable: asystole / PEA
- **Epinephrine 1 mg IV ASAP** + CPR ต่อเนื่อง ซ้ำทุก 3–5 นาที
- ห้าม shock · atropine ไม่ใช้แล้วใน arrest (เสริม)
- หาสาเหตุที่แก้ได้ **Hs & Ts** (เสริม): Hypovolemia, Hypoxia, H+ (acidosis), Hypo/Hyperkalemia, Hypothermia · Tension pneumothorax, Tamponade, Toxins, Thrombosis (pulmonary, coronary)
- ตัวอย่างในสไลด์: ถูกฟ้าผ่าแล้ว EKG เป็น asystole → epinephrine ASAP + CPR

### Post-cardiac arrest care (สไลด์หน้า 11 เป็นภาพ — เสริม)
- ROSC แล้ว: จัด airway · SpO2 92–98% · หลีกเลี่ยง hypotension (SBP ≥ 90, MAP ≥ 65)
- ทำ 12-lead EKG → STEMI หรือสงสัย cardiac cause → emergency coronary angiography
- ไม่ทำตามสั่ง → targeted temperature management · ตรวจหาสาเหตุ arrest
''',
        figs=[fig("acls-algo", "Adult cardiac arrest algorithm",
                  acls_svg.replace("cardio-01-02-a", "cardio-01-02-a"),
                  "อ่านจากบนลงล่าง: ซ้ายคือ shockable (shock ก่อนยา) ขวาคือ non-shockable (epinephrine ทันที) ทั้งสองฝั่งตรวจ rhythm ซ้ำทุก 2 นาที")],
        pearls=[
            "PEA = EKG อะไรก็ได้ที่คลำ pulse ไม่ได้ (ยกเว้น VF/VT/asystole) → epinephrine ASAP",
            "VF/pVT: shock มาก่อนยาเสมอ ต่อให้ให้ adrenaline ไปแล้วกี่ dose",
            "Amiodarone/lidocaine dose 1 หลัง shock ครั้งที่ 3 · dose 2 หลัง shock ครั้งที่ 5",
            "Epinephrine 1 mg IV ทุก 3–5 นาที ทั้งสองฝั่ง",
            "ถูกฟ้าผ่า + asystole = non-shockable → epinephrine + CPR",
        ],
        items=[
            mcq("CARDIO-01-02-1",
                "A man with uncontrolled hypertension presents in cardiac arrest. CPR is in progress and he has already received three doses of adrenaline 1 mg IV. The monitor still shows pulseless ventricular tachycardia. What is the most appropriate management?",
                "Defibrillation",
                ["Amiodarone 300 mg IV", "Synchronized cardioversion", "Another dose of adrenaline 1 mg IV", "Atropine 1 mg IV"],
                explain='''Pulseless VT เป็น **shockable rhythm** การรักษาที่ช่วยรอดชีวิตจริงคือ **defibrillation (unsynchronized shock)** ต้องทำทุกครั้งที่ตรวจพบ rhythm นี้ ยาเป็นเพียงส่วนเสริม
- Amiodarone 300 mg ให้ได้ใน shockable rhythm แต่ตามสไลด์ให้ **หลัง shock ครั้งที่ 3** และไม่ได้แทน shock — ถ้ายังเห็น pVT ต้อง shock ก่อน
- Synchronized cardioversion ใช้กับ tachycardia ที่ **ยังมี pulse** · ใน pulseless VT เครื่องอาจ sync กับ QRS ไม่ได้ ทำให้ shock ช้า
- Adrenaline อีก dose ให้ได้ตามรอบ 3–5 นาที แต่ไม่ใช่สิ่งที่สำคัญที่สุดตอนนี้
- Atropine ไม่มีบทบาทใน cardiac arrest''',
                pearl="เห็น VF/pVT เมื่อไร ต้อง shock ก่อนยาเสมอ",
                topic="Pulseless VT", ref=[f"{D} หน้า 12–13"], nl=["2.2.3"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 12"),
            mcq("CARDIO-01-02-2",
                "A 30-year-old farmer is struck by lightning. He is unresponsive and pulseless. CPR is started and the monitor shows asystole confirmed in two leads. What is the most appropriate management?",
                "Epinephrine 1 mg IV as soon as possible with continued CPR",
                ["Immediate defibrillation", "Atropine 1 mg IV", "Synchronized cardioversion", "Transcutaneous pacing"],
                explain='''Asystole เป็น **non-shockable rhythm** การรักษาคือ **CPR คุณภาพสูง + epinephrine 1 mg IV ให้เร็วที่สุด** แล้วซ้ำทุก 3–5 นาที (สไลด์หน้า 15)
- Defibrillation ไม่มีประโยชน์ใน asystole เพราะไม่มีกิจกรรมไฟฟ้าให้ reset
- Atropine ถูกตัดออกจาก cardiac arrest algorithm แล้ว เพราะไม่ช่วยให้รอดชีวิต (เสริม)
- Synchronized cardioversion ต้องมี QRS ให้ sync ด้วยและใช้กับคนที่มี pulse
- Transcutaneous pacing ไม่ช่วยใน asystole ระหว่าง arrest (เสริม)''',
                pearl="Asystole/PEA → epinephrine ASAP + CPR ไม่ shock",
                topic="Asystole", ref=[f"{D} หน้า 14–15"], nl=["2.2.3"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 14"),
            mcq("CARDIO-01-02-3",
                "A 58-year-old man has a cardiac arrest from acute myocardial infarction. During chest compressions the monitor shows an organised narrow-complex rhythm at 70/min, but no pulse can be palpated. What is the most appropriate management?",
                "Epinephrine 1 mg IV",
                ["NSS IV bolus", "Atropine 0.5 mg IV", "Dopamine infusion", "Advanced airway insertion before any drug"],
                explain='''มี electrical activity ที่เป็นระเบียบ แต่คลำ pulse ไม่ได้ = **PEA** (non-shockable) → **CPR + epinephrine 1 mg IV ให้เร็วที่สุด** ตามสไลด์หน้า 17–19
- NSS bolus เหมาะเมื่อสงสัย hypovolemia เป็นสาเหตุ (Hs) แต่ไม่ใช่ยาหลักของ PEA และโจทย์ไม่มีประวัติเสียเลือด/ขาดน้ำ
- Atropine 0.5 mg เป็นยาของ symptomatic bradycardia ที่ **มี pulse** ไม่ใช้ใน arrest
- Dopamine infusion ใช้ใน bradycardia/shock ที่มี pulse ไม่ใช่ใน arrest
- Advanced airway ทำได้ แต่ไม่ต้องรอใส่ก่อนให้ epinephrine และไม่ใช่สิ่งที่เปลี่ยน outcome มากที่สุด''',
                pearl="EKG ดูดีแต่ไม่มี pulse = PEA → epinephrine",
                topic="PEA", ref=[f"{D} หน้า 18–19"], nl=["2.2.3"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 18"),
            mcq("CARDIO-01-02-4",
                "A 64-year-old woman in VF arrest has received three shocks with CPR, and one dose of epinephrine 1 mg IV. The rhythm remains VF after the third shock. Which antiarrhythmic regimen is most appropriate now?",
                "Amiodarone 300 mg IV bolus",
                ["Amiodarone 150 mg IV infused over 10 minutes",
                 "Adenosine 6 mg rapid IV push",
                 "Magnesium sulfate 2 g IV",
                 "Verapamil 5 mg IV"],
                explain='''VF ที่ยังไม่หายหลัง shock ครั้งที่ 3 (refractory VF) → ให้ antiarrhythmic dose แรก คือ **amiodarone 300 mg IV bolus** (หรือ lidocaine) แล้ว dose ที่สอง 150 mg หลัง shock ครั้งที่ 5
- Amiodarone 150 mg ใน 10 นาที เป็นขนาดสำหรับ **stable VT ที่มี pulse** หรือ dose ที่สองใน arrest ไม่ใช่ dose แรก (เสริม)
- Adenosine ใช้กับ regular narrow-complex SVT ที่มี pulse ไม่มีที่ใช้ใน VF
- Magnesium ใช้เฉพาะ torsades de pointes/hypomagnesemia (เสริม) โจทย์ไม่มีข้อมูลนั้น
- Verapamil เป็น non-DHP CCB สำหรับ rate control ใน SVT/AF ใน VF อาจทำให้แย่ลง''',
                pearl="Refractory VF: amiodarone 300 mg → 150 mg",
                topic="Refractory VF", ref=[f"{D} หน้า 13"], nl=["2.2.3", "B7.4(7)"]),
        ]),
    # ------------------------------------------------------------------ Tachycardia
    sec("cardio-01-03", "Tachycardia: approach & common tachyarrhythmias",
        "unstable → synchronized cardioversion · stable → แยกด้วย QRS กว้าง/แคบ และ regular/irregular", minutes=8,
        source=f"{D} หน้า 20–24, 31–34, 39–48", nl=["2.3.9(1)", "B7.2.5(5)", "B7.3(3)b"],
        md='''
### ขั้นที่ 1: Stable หรือ unstable?
สไลด์หน้า 20–21 เป็นภาพ tachycardia algorithm — สรุปจากคำตอบข้อสอบในสไลด์ (หน้า 44–48) ว่า **unstable** คือมีอย่างน้อยหนึ่งข้อ:
- **Hypotension**
- **Alteration of consciousness (AOC)**
- **Signs of shock**
- **Chest discomfort** (ischemic)
- **Acute heart failure** (pulmonary edema, crepitation, SpO2 ต่ำ)

Unstable → **synchronized cardioversion** ทันที (ไม่ใช่ defibrillation ไม่ใช่ CPR เพราะยังมี pulse) · พลังงาน (เสริม): narrow regular 50–100 J · narrow irregular (AF) 120–200 J · wide regular 100 J · polymorphic VT ใช้ defibrillation dose

### ขั้นที่ 2: Stable → ดู QRS และ rhythm
| | Narrow QRS | Wide QRS |
|---|---|---|
| **Regular** | SVT · atrial flutter | Monomorphic VT |
| **Irregular** | AF · atrial flutter (variable block) · MAT | Polymorphic VT · AF with WPW |

[[fig:tachy-grid]]

### EKG ที่ต้องจำ
- **SVT**: regular narrow QRS เร็ว **มองไม่เห็น P wave**
- **Atrial flutter**: P wave แบบ **sawtooth** (เห็นชัดใน II, III, aVF) · regular หรือ irregular ก็ได้ตาม block
- **AF**: irregularly irregular · fibrillary P / ไม่เห็น P (ดูหัวข้อถัดไป)
- **MAT**: irregularly irregular narrow QRS · **P wave ≥ 3 รูปแบบ** (มักเจอใน COPD เสริม)
- **Monomorphic VT**: regular wide QRS **รูปเดียวกันทุกตัว**
- **Polymorphic VT**: irregular wide QRS **หลายรูปแบบ**
- **AF with WPW**: irregularly irregular wide QRS หลายรูปแบบ ไม่เห็น P · มี **delta wave** (slurred upstroke ต้น QRS)

### Stable SVT (regular narrow) — ตามสไลด์
1. **Vagal maneuver** (modified Valsalva, carotid sinus massage — ฟังว่าไม่มี carotid bruit ก่อน เสริม)
2. **Adenosine** IV rapid push (6 mg → 12 mg flush ตามด้วย NSS เสริม)
3. **Beta-blocker / non-DHP CCB** (verapamil, diltiazem)

> คำถาม "first line **medication**" ของ SVT = **adenosine** · คำถาม "most appropriate **management**" ใน stable SVT = **vagal maneuver ก่อน**

### Wide QRS (เสริม)
- Stable monomorphic VT → amiodarone 150 mg IV ใน 10 นาที (หรือ procainamide) · ไม่ดีขึ้น → synchronized cardioversion
- Polymorphic VT ที่ unstable/ไม่มี pulse → **defibrillation** · torsades de pointes → magnesium sulfate
- **AF + WPW: ห้ามยา AV nodal blocker** (adenosine, beta-blocker, CCB, digoxin) เพราะจะดันกระแสลง accessory pathway → VF · ใช้ cardioversion หรือ procainamide
''',
        figs=[fig("tachy-grid", "Approach to tachycardia with a pulse", tachy_svg,
                  "เริ่มจากถามว่า unstable หรือไม่ ถ้า stable ให้ดูความกว้าง QRS (คอลัมน์) กับความสม่ำเสมอ (แถว) แล้วอ่านการรักษาในช่องนั้น")],
        pearls=[
            "Tachycardia + hypotension/AOC/shock/chest pain/AHF = unstable → synchronized cardioversion",
            "Stable SVT: vagal → adenosine → BB/non-DHP CCB",
            "Flutter = sawtooth · MAT = P ≥ 3 รูปแบบ · WPW = delta wave",
            "AF + WPW ห้าม adenosine, BB, CCB, digoxin (เสริม)",
        ],
        items=[
            mcq("CARDIO-01-03-1",
                "A patient presents with palpitation without syncope, chest pain or dyspnea. BP 100/80 mmHg, pulse 160/min. EKG shows a regular narrow-QRS tachycardia with no visible P waves. What is the most appropriate management?",
                "Carotid sinus massage",
                ["Amiodarone IV", "Synchronized cardioversion", "Defibrillation", "IV verapamil"],
                explain='''Regular narrow QRS ไม่เห็น P = **SVT** และผู้ป่วย **stable** (ไม่มี hypotension, AOC, shock, chest pain, AHF) → ขั้นแรกคือ **vagal maneuver** เช่น carotid sinus massage ตามสไลด์หน้า 40
- Amiodarone ไม่ใช่ยาแรกของ SVT ใช้กับ VT หรือ AF บางกรณี
- Synchronized cardioversion ใช้เมื่อ **unstable** ผู้ป่วยรายนี้ BP ยังดีและไม่มีอาการเตือน
- Defibrillation ใช้กับ VF/pulseless VT ใน cardiac arrest เท่านั้น
- Verapamil (non-DHP CCB) เป็นขั้นที่ 3 หลัง vagal และ adenosine ไม่ใช่สิ่งแรก''',
                pearl="Stable SVT เริ่มที่ vagal maneuver เสมอ",
                topic="Stable SVT", ref=[f"{D} หน้า 39–40"], nl=["2.3.9(1)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 39"),
            mcq("CARDIO-01-03-2",
                "A man presents with palpitation and no chest pain. BT 37°C, BP 130/80 mmHg, pulse 150/min, RR 20/min. Physical examination is normal. EKG shows a regular narrow-complex tachycardia without visible P waves. Vagal maneuvers have failed. What is the first-line medication?",
                "Adenosine",
                ["Procainamide", "Amiodarone", "Calcium channel blocker", "Beta-blocker"],
                explain='''Stable SVT ที่ vagal ไม่ได้ผล → ยาตัวแรกคือ **adenosine** IV rapid push (block AV node ชั่วคราว ตัดวงจร reentry ที่ผ่าน AV node) ตามสไลด์หน้า 42
- Procainamide เป็นยาสำหรับ stable wide-complex tachycardia หรือ AF + WPW (เสริม) ไม่ใช่ SVT ทั่วไป
- Amiodarone ไม่ใช่ยาแรกของ SVT
- Calcium channel blocker (non-DHP) และ beta-blocker เป็นขั้นที่ 3 หลัง adenosine — ใช้ได้แต่ไม่ใช่ first line''',
                pearl="SVT first-line drug = adenosine",
                topic="SVT drug", ref=[f"{D} หน้า 41–42"], nl=["2.3.9(1)", "B7.4(7)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 41"),
            mcq("CARDIO-01-03-3",
                "A 25-year-old woman has palpitation and near-syncope. BP 80/50 mmHg, HR 180/min. EKG shows a regular narrow-complex tachycardia. What is the most appropriate management?",
                "Synchronized cardioversion",
                ["Adenosine", "Metoprolol", "Amiodarone", "Defibrillation"],
                explain='''Tachycardia ที่มี **hypotension และเกือบหมดสติ** = **unstable** → **synchronized cardioversion** ทันที (สไลด์หน้า 44)
- Adenosine อาจลองได้ระหว่างเตรียมเครื่องในบางแนวทาง แต่ในผู้ป่วยที่ BP 80/50 คำตอบหลักคือไฟฟ้า
- Metoprolol ลด BP ลงอีก อันตรายใน hypotension
- Amiodarone ใช้เวลาออกฤทธิ์และลด BP ได้ ไม่ใช่การรักษาของ unstable SVT
- Defibrillation (ไม่ sync) ใช้กับ VF/pulseless VT ถ้าใช้กับ rhythm ที่มี QRS อาจ shock ตรง T wave แล้วเกิด VF''',
                pearl="Unstable + มี pulse = synchronized cardioversion · ไม่มี pulse = defibrillation",
                topic="Unstable tachycardia", ref=[f"{D} หน้า 43–44"], nl=["2.3.9(1)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 43"),
            mcq("CARDIO-01-03-4",
                "A 60-year-old woman with DM, HT and dyslipidemia has chest tightness this morning. BT 37°C, BP 70/40 mmHg, PR 150/min, RR 28/min. She is drowsy with crepitation in both lungs and SpO2 88%. EKG shows a tachyarrhythmia with a pulse. After oxygen by mask with bag at 10 L/min, what is the most appropriate next step?",
                "Synchronized cardioversion",
                ["Adenosine", "Dopamine infusion", "NSS loading", "Cardiopulmonary resuscitation"],
                explain='''มีครบทุกข้อของ **unstable tachycardia**: hypotension, AOC (drowsy), chest discomfort และ acute heart failure (crepitation, SpO2 88%) → **synchronized cardioversion** (สไลด์หน้า 48)
- Adenosine ไม่เหมาะกับคนที่ unstable และหัวใจเต้นเร็วเป็นตัวก่อ shock
- Dopamine เพิ่ม HR และ myocardial O2 demand ไม่แก้ต้นเหตุคือ arrhythmia
- NSS loading จะทำให้ pulmonary edema แย่ลง
- CPR ใช้เมื่อไม่มี pulse ผู้ป่วยรายนี้ยังมี pulse 150''',
                pearl="Tachy + shock + pulmonary edema → ไฟฟ้า ไม่ใช่ยา",
                topic="Unstable tachycardia", ref=[f"{D} หน้า 47–48"], nl=["2.3.9(1)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 47"),
            mcq("CARDIO-01-03-5",
                "A 28-year-old man has palpitation for 1 hour. BP 124/78 mmHg and he is alert. EKG shows an irregularly irregular wide-complex tachycardia at 210/min with varying QRS morphology and slurred upstrokes at the start of the QRS complexes. Which drug is most appropriate?",
                "IV procainamide",
                ["IV adenosine", "IV verapamil", "IV digoxin", "IV metoprolol"],
                explain='''Irregularly irregular + wide QRS หลายรูปแบบ + **delta wave** = **AF with WPW** (สไลด์หน้า 34) ผู้ป่วย stable → ใช้ยาที่ชะลอการนำผ่าน accessory pathway เช่น **procainamide** (หรือ ibutilide) ถ้า unstable ใช้ cardioversion (เสริม)
- Adenosine, verapamil, digoxin และ metoprolol ล้วนเป็น **AV nodal blocker** เมื่อ block AV node กระแสจาก AF จะวิ่งลง accessory pathway มากขึ้น ventricular rate เร็วขึ้นจนกลายเป็น VF ได้ — ห้ามใช้ทั้งหมด''',
                pearl="AF + WPW: ห้าม ABCD (adenosine, BB, CCB, digoxin)",
                topic="AF with WPW", ref=[f"{D} หน้า 34"], nl=["2.3.9(1)", "B7.4(7)"]),
        ]),
    # ------------------------------------------------------------------ AF
    sec("cardio-01-04", "Atrial fibrillation (AF)",
        "unstable → cardioversion · stable → rate control (BB/non-DHP) + ประเมิน anticoagulant ด้วย CHA2DS2-VASc", minutes=7,
        source=f"{D} หน้า 25–30, 35–38", nl=["2.3.9(1)", "B7.2.5(5)", "B2.4(3)"],
        md='''
### อาการและ EKG
- ใจสั่น เหนื่อย มึนงง เป็นลม · **pulse irregularly irregular** (S1 ดังไม่เท่ากัน, pulse deficit)
- EKG: **irregularly irregular RR interval** · narrow QRS · **fibrillary P waves / หา P ไม่เจอ**
- **AF with RVR** = HR > 100 · AF without RVR = HR < 100
- ภาวะแทรกซ้อน: **acute heart failure** และ **thromboembolism** — stroke/TIA, renal/splenic infarct, intestinal ischemia, acute limb ischemia

[[fig:af-mx]]

### Unstable AF
- ABC → **synchronized cardioversion**
- ควรให้ **anticoagulant ก่อน cardioversion** (ถ้าสถานการณ์อนุญาต)

### Stable AF: rate control
| ลำดับ | ยา |
|---|---|
| 1st line | **Beta-blocker** (esmolol, metoprolol, propranolol, atenolol) · **non-DHP CCB** (diltiazem, verapamil) |
| 2nd line | **Digoxin, amiodarone** |
| เป้าหมาย | **HR < 110 bpm** (< 80 bpm ถ้ายังมีอาการ) |

> ในผู้ป่วย AF ที่มี **acute heart failure / LVEF ต่ำ** เลี่ยง non-DHP CCB และ beta-blocker ขนาดสูงช่วงเฉียบพลัน — ใช้ **digoxin หรือ amiodarone** (ดูข้อสอบในหมวด heart failure สไลด์หน้า 298)

### Rhythm control
- Electrical หรือ pharmacological cardioversion (flecainide, propafenone, amiodarone) + **pericardioversion anticoagulation**
- พิจารณาเมื่อ rate control แล้วอาการยังเยอะ

### Anticoagulant
- **Moderate–severe mitral stenosis, mechanical heart valve, HCM → warfarin** (DOAC ห้ามใช้ใน MS และ mechanical valve — เสริม) · target INR 2–3 (mechanical mitral 2.5–3.5) (เสริม)
- กรณีอื่นใช้ **CHA2DS2-VASc**: **≥ 1 ในชาย หรือ ≥ 2 ในหญิง → DOAC หรือ warfarin**

| ตัวอักษร | ปัจจัย | คะแนน |
|---|---|---|
| C | Congestive heart failure | 1 |
| H | Hypertension | 1 |
| A2 | Age ≥ 75 | 2 |
| D | Diabetes | 1 |
| S2 | Stroke / TIA / thromboembolism | 2 |
| V | Vascular disease (prior MI, PAD, aortic plaque) | 1 |
| A | Age 65–74 | 1 |
| Sc | Sex category: female | 1 |

ตารางคะแนนในสไลด์หน้า 30 เป็นภาพ — ตารางนี้เรียบเรียงตามมาตรฐาน (เสริม) · ESC 2024 เปลี่ยนเป็น **CHA2DS2-VA** (ตัดเพศหญิงออก ใช้เกณฑ์ ≥ 1 เท่ากันทุกเพศ) แต่ข้อสอบ NL ตามสไลด์ยังใช้ CHA2DS2-VASc (เสริม)
''',
        figs=[fig("af-mx", "การจัดการ AF", af_svg,
                  "AF ที่ stable ต้องทำสองเรื่องคู่กันเสมอ: คุมอัตรา (กล่องเขียว) และตัดสินใจเรื่อง anticoagulant (กล่องฟ้า) ส่วนล่างคือวิธีนับคะแนน CHA2DS2-VASc")],
        pearls=[
            "Stable AF RVR → rate control ด้วย BB หรือ diltiazem/verapamil ไม่ใช่ amlodipine",
            "Rate goal < 110 bpm (< 80 ถ้ายังมีอาการ)",
            "AF + MS ปานกลาง–รุนแรง/mechanical valve/HCM → warfarin เสมอ ไม่ต้องคิดคะแนน",
            "CHA2DS2-VASc ≥ 1 ชาย ≥ 2 หญิง → anticoagulant",
            "AF + hypotension/chest pain/AHF → synchronized cardioversion",
        ],
        items=[
            mcq("CARDIO-01-04-1",
                "A woman presents with intermittent palpitation. She is alert with normal blood pressure. Pulse 122/min, irregular. EKG confirms atrial fibrillation with a narrow QRS. What is the most appropriate management?",
                "Atenolol",
                ["Digoxin", "Amlodipine", "Amiodarone", "Synchronized cardioversion"],
                explain='''Stable AF with RVR (HR 122) → **rate control ด้วย beta-blocker หรือ non-DHP CCB เป็น first line** จึงเลือก **atenolol** แล้วค่อยประเมินข้อบ่งชี้ anticoagulant (สไลด์หน้า 36)
- Digoxin เป็น 2nd line (ออกฤทธิ์ช้า คุม HR ขณะออกแรงไม่ดี) เหมาะในคนที่มี HF/hypotension
- Amlodipine เป็น **DHP-CCB** ไม่มีผลต่อ AV node จึงคุม rate ไม่ได้
- Amiodarone เป็น 2nd line สำหรับ rate control หรือใช้ทำ rhythm control
- Synchronized cardioversion ใช้เมื่อ **unstable** ผู้ป่วยรายนี้ stable''',
                pearl="Rate control AF: BB/non-DHP CCB (amlodipine ใช้ไม่ได้)",
                topic="AF rate control", ref=[f"{D} หน้า 35–36"], nl=["2.3.9(1)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 35"),
            mcq("CARDIO-01-04-2",
                "An adult comes for an annual check-up and has no chest pain or palpitation. Examination shows a totally irregular rhythm with a diastolic murmur at the apex. EKG shows fibrillatory waves with no P waves; heart rate is 84/min. Echocardiogram shows moderate mitral stenosis. What is the most appropriate management?",
                "Oral anticoagulant (warfarin)",
                ["Beta-blocker", "Balloon mitral valvotomy", "Surgical valve replacement", "Follow-up echocardiogram in 3 months"],
                explain='''AF + **mitral stenosis** = ความเสี่ยง thromboembolism สูงมาก ให้ **oral anticoagulant (warfarin)** โดยไม่ต้องคิด CHA2DS2-VASc (สไลด์หน้า 29, 38) HR 84 อยู่ในเป้าหมาย < 110 อยู่แล้ว
- Beta-blocker ใช้คุม rate แต่ HR ผู้ป่วยอยู่ในเป้าหมายแล้ว และไม่ป้องกัน stroke ซึ่งเป็นอันตรายหลัก
- Balloon valvotomy ใช้ใน symptomatic severe MS ผู้ป่วยไม่มีอาการ
- Surgical valve replacement ก็สำหรับ severe symptomatic ที่ไม่เหมาะกับ balloon
- การนัดติดตามเฉย ๆ ปล่อยให้เสี่ยง stroke''',
                pearl="AF + MS → warfarin เสมอ (ห้าม DOAC)",
                topic="AF with MS", ref=[f"{D} หน้า 37–38"], nl=["2.3.9(1)", "B2.4(3)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 37"),
            mcq("CARDIO-01-04-3",
                "A 58-year-old woman with DM and HT presents with palpitation and acute chest pain. BP 90/60 mmHg, pulse totally irregular at 180/min, varying intensity of S1, and a grade 3/6 pansystolic murmur at the apex. What is the most appropriate management?",
                "Synchronized cardioversion",
                ["IV adrenaline", "IV antibiotic", "IV dexamethasone", "IV diltiazem"],
                explain='''Irregular 180/min + S1 ดังไม่เท่ากัน = **AF with RVR** ที่มี **chest pain และ BP ต่ำ** = **unstable** → **synchronized cardioversion** (สไลด์หน้า 46)
- IV adrenaline ใช้ใน arrest หรือ anaphylaxis จะเพิ่ม HR และ ischemia
- IV antibiotic ใช้เมื่อสงสัย IE ซึ่งโจทย์ไม่มีไข้หรือ embolic sign — murmur MR อธิบายได้จากโรคลิ้นเดิม
- IV dexamethasone ไม่มีบทบาท
- IV diltiazem ใช้ rate control ใน **stable** AF แต่จะทำให้ BP ที่ต่ำอยู่แล้วต่ำลงอีก''',
                pearl="AF + hypotension/chest pain = cardioversion ไม่ใช่ rate control",
                topic="Unstable AF", ref=[f"{D} หน้า 45–46"], nl=["2.3.9(1)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 45"),
            mcq("CARDIO-01-04-4",
                "A 70-year-old woman with hypertension and type 2 diabetes is found to have persistent non-valvular atrial fibrillation. Heart rate is controlled with bisoprolol. She has no history of stroke, heart failure or vascular disease, and her creatinine clearance is 70 mL/min. What is the most appropriate antithrombotic therapy?",
                "Apixaban",
                ["No antithrombotic therapy", "Aspirin alone", "Aspirin plus clopidogrel", "Long-term subcutaneous enoxaparin"],
                explain='''CHA2DS2-VASc = HT 1 + DM 1 + อายุ 65–74 1 + เพศหญิง 1 = **4** (เกณฑ์ในหญิงคือ ≥ 2) และไม่มี MS/mechanical valve → **DOAC เช่น apixaban** (หรือ warfarin) (สไลด์หน้า 29)
- ไม่ให้ยาเลย ผิด เพราะคะแนนเกินเกณฑ์ชัดเจน
- Aspirin เดี่ยว ป้องกัน stroke ใน AF ได้น้อยแต่มีเลือดออกใกล้เคียงกัน ไม่แนะนำแล้ว
- Aspirin + clopidogrel ด้อยกว่า anticoagulant และเลือดออกมากขึ้น
- Enoxaparin ใช้ชั่วคราวช่วง bridging ไม่ใช่ยาระยะยาว''',
                pearl="นับ CHA2DS2-VASc แล้ว ≥ 2 ในหญิง → DOAC/warfarin ไม่ใช่ aspirin",
                topic="CHA2DS2-VASc", ref=[f"{D} หน้า 29–30"], nl=["2.3.9(1)", "B2.4(3)"]),
            mcq("CARDIO-01-04-5",
                "A 45-year-old woman with rheumatic heart disease has atrial fibrillation. Echocardiogram shows severe mitral stenosis with a mitral valve area of 0.9 cm2. Which anticoagulant is most appropriate?",
                "Warfarin with target INR 2–3",
                ["Rivaroxaban", "Apixaban", "Dabigatran", "Aspirin"],
                explain='''AF + **moderate–severe MS** → **warfarin** ตามสไลด์หน้า 29 · target INR 2–3 (เสริม)
- Rivaroxaban, apixaban และ dabigatran เป็น DOAC ที่ **ไม่มีข้อมูล/ไม่แนะนำ** ใน moderate–severe MS (การศึกษา INVICTUS พบว่า rivaroxaban ด้อยกว่า warfarin ใน rheumatic AF — เสริม)
- Aspirin ไม่พอสำหรับป้องกัน stroke ในกลุ่มเสี่ยงสูงนี้''',
                pearl="Rheumatic MS + AF = warfarin",
                topic="AF anticoagulant choice", ref=[f"{D} หน้า 29"], nl=["2.3.9(1)", "B2.4(3)"]),
        ]),
    # ------------------------------------------------------------------ Bradycardia
    sec("cardio-01-05", "Bradycardia: sinus node dysfunction & AV block",
        "SND vs AV block · Mobitz II/CHB ต้อง pacing · unstable → atropine แล้ว pacing", minutes=7,
        source=f"{D} หน้า 49–71", nl=["2.3.9(1)", "B7.3(3)b"],
        md='''
### ชนิดของ bradyarrhythmia ที่ต้องรู้
#### Sinus node dysfunction (sick sinus syndrome)
| ชนิด | กลไก / EKG |
|---|---|
| Sinus bradycardia | P และ QRS ปกติ rate < 60 bpm |
| Sinus pause / sinus arrest | SA node ไม่ปล่อยกระแส · P หายเป็นช่วง ๆ · **P-P ช่วงยาวไม่เป็นจำนวนเท่า** ของ P-P ปกติ · sinus arrest = pause > 3 วินาที · อาจมี escape rhythm |
| Sinoatrial (SA) block | กระแสออกจาก SA node แต่ถูกกั้น · คล้าย pause แต่ **P-P ช่วงยาวเป็นจำนวนเท่า** ของ P-P ปกติ |
| Tachycardia–bradycardia syndrome | AF/flutter/SVT สลับกับ sinus arrest หรือ bradycardia |

#### AV block
| ชนิด | EKG |
|---|---|
| 1st degree | **PR ยาว** (> 0.20 s) ทุกตัวเท่ากัน ไม่มี drop |
| 2nd degree Mobitz I (Wenckebach) | **PR ยาวขึ้นเรื่อย ๆ จน drop** |
| 2nd degree Mobitz II | PR คงที่ แล้ว **drop โดยไม่มีสัญญาณเตือน** |
| 3rd degree (complete) | **AV dissociation** — P กับ QRS ไม่สัมพันธ์กัน · QRS มักกว้าง (ventricular escape) |

[[fig:avb-ecg]]

### การรักษา
- Bradycardia algorithm ในสไลด์หน้า 49–50 เป็นภาพ — หลักจากคำตอบในสไลด์:
- **Mobitz II และ complete heart block**: unstable → **atropine แล้ว pacing** · stable → **pacing** (permanent pacemaker)
- Symptomatic bradycardia ที่ unstable (hypotension, AOC, shock, chest pain, AHF) → **atropine** เป็นยาแรก
- ขนาดยา (เสริม, AHA 2020): atropine **1 mg IV ทุก 3–5 นาที รวมไม่เกิน 3 mg** (ตำราเก่าใช้ 0.5 mg) · atropine ไม่ได้ผล → **transcutaneous pacing** หรือ dopamine 5–20 mcg/kg/min หรือ epinephrine 2–10 mcg/min
- Atropine มักไม่ได้ผลใน Mobitz II/CHB ที่ block ต่ำกว่า AV node และในหัวใจที่ปลูกถ่าย — อย่ารอนาน ให้ pacing (เสริม)
- 1st degree และ Mobitz I ที่ไม่มีอาการ → สังเกตอาการ หาสาเหตุ (ยา BB/CCB/digoxin, inferior MI, hyperK) (เสริม)

> ข้อสอบในสไลด์: ผู้สูงอายุเป็นลมวูบซ้ำ ๆ HR ปกติแต่มี dropped beat และ EKG เป็น **sinus pause** → dx **sick sinus syndrome** ไม่ใช่ AV block
''',
        figs=[fig("avb-ecg", "EKG schematic ของ AV block", avb_svg,
                  "ดูระยะจาก P (สีฟ้า) ไปถึง QRS ในแต่ละแถว: ยาวคงที่ = 1st degree, ยาวขึ้นจนหาย = Mobitz I, คงที่แล้วหาย = Mobitz II, ไม่สัมพันธ์กันเลย = complete block")],
        pearls=[
            "Sinus pause: P-P ยาวไม่เป็นจำนวนเท่า · SA block: เป็นจำนวนเท่า",
            "Mobitz I = PR ยาวขึ้นจน drop · Mobitz II = PR คงที่แล้ว drop",
            "Mobitz II/CHB: stable → pacing · unstable → atropine + pacing",
            "Atropine 1 mg ทุก 3–5 นาที max 3 mg ไม่ได้ผล → transcutaneous pacing (เสริม)",
            "เป็นลมซ้ำ + sinus pause = sick sinus syndrome",
        ],
        items=[
            mcq("CARDIO-01-05-1",
                "A 70-year-old man has had dizziness and episodes of syncope on and off for 3 months. BP 130/70 mmHg, HR 70/min with dropped beats, RR 18/min. EKG shows sinus rhythm with intermittent absence of P waves; the long P-P intervals are not multiples of the basic P-P interval. What is the diagnosis?",
                "Sick sinus syndrome",
                ["AV block", "Supraventricular tachycardia", "Pericarditis", "Myocardial infarction"],
                explain='''P wave หายเป็นช่วง ๆ และ P-P ที่ยาวไม่เป็นจำนวนเท่าของปกติ = **sinus pause/arrest** ซึ่งเป็นส่วนหนึ่งของ **sick sinus syndrome (sinus node dysfunction)** ทำให้เป็นลมซ้ำ (สไลด์หน้า 53, 63)
- AV block: P wave ยังมาตามจังหวะ แต่ QRS หายไป (P ที่ไม่ตามด้วย QRS) — ต่างจากรายนี้ที่ P หายไปเอง
- SVT เป็น tachycardia ไม่ใช่ HR 70 ที่มี pause
- Pericarditis ให้ diffuse ST elevation + PR depression ไม่ทำให้ P หาย
- MI ดูจาก ST-T change ไม่ได้ทำให้เกิด pause แบบนี้โดยตรง''',
                pearl="P หาย = ปัญหาที่ SA node · P อยู่แต่ QRS หาย = AV block",
                topic="Sinus pause", ref=[f"{D} หน้า 62–63"], nl=["2.3.9(1)", "B7.3(3)b"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 62"),
            mcq("CARDIO-01-05-2",
                "A 50-year-old man presents with dyspnea on exertion and fatigue. BT 37°C, BP 90/60 mmHg, PR 30/min, RR 16/min. He looks fatigued. EKG shows a bradyarrhythmia. What is the most appropriate initial management?",
                "Atropine",
                ["Adenosine", "Amiodarone", "Dobutamine", "Norepinephrine"],
                explain='''Bradycardia HR 30 ที่มีอาการ (เหนื่อย อ่อนเพลีย BP ค่อนต่ำ) → ยาแรกคือ **atropine** IV (1 mg ทุก 3–5 นาที max 3 mg ตาม AHA 2020 — เสริม) ถ้าไม่ได้ผลจึงไป pacing หรือ dopamine/epinephrine infusion (สไลด์หน้า 66–71)
- Adenosine ใช้หยุด SVT จะทำให้ bradycardia แย่ลงหรือ asystole
- Amiodarone เป็น antiarrhythmic สำหรับ tachyarrhythmia กด SA/AV node ทำให้ช้าลงอีก
- Dobutamine เป็น inotrope สำหรับ cardiogenic shock ไม่ใช่ยาลำดับแรกของ bradycardia
- Norepinephrine เป็น vasopressor ไม่ได้แก้ HR ต่ำซึ่งเป็นต้นเหตุ''',
                pearl="Symptomatic bradycardia: atropine ก่อน แล้วค่อย pacing/infusion",
                topic="Symptomatic bradycardia", ref=[f"{D} หน้า 66–67"], nl=["2.3.9(1)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 66"),
            mcq("CARDIO-01-05-3",
                "A 75-year-old woman reports intermittent lightheadedness. BP 128/74 mmHg, alert, no chest pain. EKG shows a constant PR interval of 0.18 s with occasional non-conducted P waves that occur without preceding PR prolongation. What is the most appropriate management?",
                "Permanent pacemaker implantation",
                ["Observation and reassurance", "Oral metoprolol", "IV adenosine", "Oral digoxin"],
                explain='''PR คงที่แล้วมี P ที่ไม่ตามด้วย QRS โดยไม่มี PR ยาวขึ้นก่อน = **2nd degree AV block Mobitz II** ซึ่งมีโอกาสลุกลามเป็น complete heart block → แม้ stable ก็ต้อง **pacing (permanent pacemaker)** ตามสไลด์หน้า 69
- การสังเกตอาการเฉย ๆ ใช้กับ 1st degree หรือ Mobitz I ที่ไม่มีอาการ ไม่ใช่ Mobitz II ที่มีอาการ
- Metoprolol และ digoxin กด AV node ทำให้ block แย่ลง
- Adenosine block AV node ชั่วคราว ใช้ใน SVT อันตรายใน AV block''',
                pearl="Mobitz II แม้ stable ก็ต้อง pacing",
                topic="Mobitz II", ref=[f"{D} หน้า 60, 68–69"], nl=["2.3.9(1)"]),
            mcq("CARDIO-01-05-4",
                "A 68-year-old man on no medications has a rhythm strip showing progressive lengthening of the PR interval over three beats, followed by a P wave that is not conducted, after which the cycle repeats. What is the diagnosis?",
                "Second-degree AV block, Mobitz type I (Wenckebach)",
                ["Second-degree AV block, Mobitz type II",
                 "First-degree AV block",
                 "Third-degree AV block",
                 "Sinoatrial exit block"],
                explain='''**PR ยาวขึ้นเรื่อย ๆ จน drop แล้ววนซ้ำ** = **Mobitz I (Wenckebach)** (สไลด์หน้า 59) block มักอยู่ที่ AV node พยากรณ์ดี
- Mobitz II: PR **คงที่** แล้ว drop ทันที
- 1st degree: PR ยาวคงที่ **ไม่มี** P ที่ไม่ถูกนำ
- 3rd degree: P กับ QRS ไม่สัมพันธ์กันเลย (AV dissociation) ไม่มีรูปแบบ PR ที่ค่อย ๆ ยาว
- SA exit block: **P wave หายไปเอง** ไม่ใช่ P ที่มาแล้วไม่มี QRS''',
                pearl="Wenckebach = PR ยาวขึ้นจนหลุด",
                topic="Mobitz I", ref=[f"{D} หน้า 59"], nl=["B7.3(3)b"]),
            mcq("CARDIO-01-05-5",
                "A 72-year-old man presents with confusion. BP 70/40 mmHg, HR 32/min. EKG shows complete AV dissociation with wide QRS escape complexes. He has received atropine 1 mg IV three times without response. What is the most appropriate next step?",
                "Transcutaneous pacing",
                ["IV adenosine", "IV amiodarone", "Unsynchronized defibrillation", "Repeat atropine 1 mg IV"],
                explain='''**Complete heart block ที่ unstable** (BP 70/40, สับสน) และ atropine ครบ 3 mg ไม่ได้ผล → **transcutaneous pacing** (หรือ dopamine/epinephrine infusion) ระหว่างรอ transvenous/permanent pacing (สไลด์หน้า 71 + เสริม)
- Adenosine ทำให้ AV block แย่ลง
- Amiodarone กดระบบนำไฟฟ้า ทำให้ช้าลงอีก
- Defibrillation ใช้ใน VF/pulseless VT ผู้ป่วยมี pulse
- Atropine ให้ครบ maximum 3 mg แล้ว และมักไม่ได้ผลใน infranodal block (wide QRS escape)''',
                pearl="CHB unstable: atropine ไม่ได้ผล → pacing ทันที",
                topic="Complete heart block", ref=[f"{D} หน้า 61, 70–71"], nl=["2.3.9(1)"]),
        ]),
    ])
