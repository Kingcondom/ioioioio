from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-Cardio"

def mk(sid):
    return (f'<defs><marker id="{sid}-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            f'markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>')

# ---------- fig: murmur timing ----------
def srow(y, title, sub):
    base = y + 46
    out = (f'<rect x="8" y="{y+4}" width="176" height="58" rx="8" class="sunk"/>'
           f'<text x="18" y="{y+28}" class="tb">{title}</text>'
           f'<text x="18" y="{y+48}" class="t3">{sub}</text>'
           f'<path d="M200 {base}H712" class="lnf"/>')
    for x in (215, 445, 695):
        out += f'<path d="M{x} {base}V{base-34}" class="ln"/>'
    return out, base

r1, b1 = srow(40, "AS · PS", "ejection (เพชร)")
r2, b2 = srow(110, "MR · TR", "holosystolic (เรียบ)")
r3, b3 = srow(180, "AR · PR", "early diastolic ลดลง")
r4, b4 = srow(250, "MS · TS", "OS + diastolic rumble")
murmur_svg = ('<svg viewBox="0 0 720 352">'
    + '<text x="215" y="22" text-anchor="middle" class="tb">S1</text>'
    + '<text x="330" y="22" text-anchor="middle" class="t2">systole</text>'
    + '<text x="445" y="22" text-anchor="middle" class="tb">S2</text>'
    + '<text x="570" y="22" text-anchor="middle" class="t2">diastole</text>'
    + '<text x="695" y="22" text-anchor="middle" class="tb">S1</text>'
    + r1 + f'<path d="M232 {b1}L330 {b1-32}L428 {b1}Z" class="acsoft"/>'
    + r2 + f'<rect x="222" y="{b2-24}" width="216" height="24" class="c1soft"/>'
    + r3 + f'<path d="M452 {b3}L452 {b3-30}L640 {b3}Z" class="c2soft"/>'
    + r4 + f'<path d="M472 {b4}V{b4-38}" class="lna"/>'
    + f'<text x="472" y="{b4+18}" text-anchor="middle" class="t3">OS</text>'
    + f'<path d="M488 {b4}L488 {b4-22}L560 {b4-10}L640 {b4-10}L688 {b4-26}L688 {b4}Z" class="misssoft"/>'
    + f'<text x="664" y="{b4+18}" text-anchor="middle" class="t3">presystolic ↑</text>'
    + '<text x="712" y="344" text-anchor="end" class="t3">S1 ดัง (loud S1) ใน MS · wide split S2 ใน PS</text>'
    + '</svg>')

# ---------- fig: auscultation map ----------
S1 = "cardio-02-01"
def tag(x, y, w, cls, l1, l2):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="8" class="{cls}"/>'
            f'<text x="{x+10}" y="{y+19}" class="tb">{l1}</text>'
            f'<text x="{x+10}" y="{y+37}" class="t3">{l2}</text>')

map_svg = (f'<svg viewBox="0 0 720 360">{mk(S1)}'
    + '<rect x="335" y="40" width="50" height="250" rx="10" class="sunk"/>'
    + '<text x="360" y="306" text-anchor="middle" class="t3">sternum</text>'
    + ''.join(f'<path d="M240 {y}H330M390 {y}H560" class="lnf"/><text x="452" y="{y-5}" class="t3">{n}</text>'
              for y, n in ((80, "ICS 2"), (130, "ICS 3"), (180, "ICS 4"), (230, "ICS 5")))
    + '<circle cx="318" cy="80" r="9" class="ac"/>'
    + '<circle cx="402" cy="80" r="9" class="c1"/>'
    + '<circle cx="402" cy="130" r="9" class="c2"/>'
    + '<circle cx="402" cy="180" r="9" class="ok"/>'
    + '<circle cx="500" cy="230" r="9" class="miss"/>'
    + f'<path d="M318 70L290 20" class="lna" marker-end="url(#{S1}-a)"/>'
    + '<text x="232" y="22" class="t3">ไปคอ</text>'
    + f'<path d="M510 230H600" class="lna" marker-end="url(#{S1}-a)"/>'
    + '<text x="606" y="234" class="t3">ไป axilla</text>'
    + f'<path d="M309 80H240" class="ln"/>'
    + tag(16, 60, 222, "acsoft", "Aortic: R 2nd ICS PSB", "AS (SEM ร้าวคอ) · AR บางครั้ง")
    + f'<path d="M411 80H430L430 40H460" class="ln"/>'
    + tag(462, 8, 250, "c1soft", "Pulmonic: L 2nd ICS PSB", "PS (ร้าวหลัง, wide split S2) · PR")
    + f'<path d="M411 130H440" class="ln"/>'
    + tag(16, 120, 222, "c2soft", "Erb's: L 3rd ICS PSB", "AR diastolic blowing")
    + f'<path d="M393 130H340" class="lnf"/>'
    + f'<path d="M393 180H238" class="ln"/>'
    + tag(16, 180, 222, "oksoft", "Tricuspid: L 4th ICS PSB", "TR systolic · TS diastolic")
    + f'<path d="M500 240V262" class="ln"/>'
    + tag(388, 264, 324, "misssoft", "Mitral: apex (L 5th ICS MCL)", "MR systolic ร้าว axilla · MS rumble + OS")
    + '</svg>')
# The Erb's tag sits left of sternum: connect from left circle-free point
map_svg = map_svg.replace('<path d="M393 130H340" class="lnf"/>', '<path d="M393 130H386M334 130H238" class="lnf"/>')

# ---------- fig: syncope ----------
S5 = "cardio-02-05"
def col(x, cls, head, lines, ix_cls, ix):
    out = f'<rect x="{x}" y="110" width="226" height="150" rx="10" class="{cls}"/>'
    out += f'<text x="{x+113}" y="134" text-anchor="middle" class="tb">{head}</text>'
    yy = 158
    for t in lines:
        out += f'<text x="{x+14}" y="{yy}">{t}</text>'
        yy += 20
    out += f'<path d="M{x+113} 260V286" class="ln" marker-end="url(#{S5}-a)"/>'
    out += f'<rect x="{x}" y="290" width="226" height="82" rx="10" class="{ix_cls}"/>'
    yy = 314
    for i, t in enumerate(ix):
        out += f'<text x="{x+113}" y="{yy}" text-anchor="middle" class="{"tb" if i == 0 else "t2"}">{t}</text>'
        yy += 20
    return out

syncope_svg = (f'<svg viewBox="0 0 720 384">{mk(S5)}'
    + '<rect x="200" y="8" width="320" height="58" rx="10" class="acsoft"/>'
    + '<text x="360" y="32" text-anchor="middle" class="tb">Syncope: หมดสติเร็ว สั้น (< 1 นาที)</text>'
    + '<text x="360" y="52" text-anchor="middle" class="t3">ฟื้นเองสมบูรณ์ · ± myoclonic jerk สั้น ๆ</text>'
    + f'<path d="M280 66L125 106" class="ln" marker-end="url(#{S5}-a)"/>'
    + f'<path d="M360 66V106" class="ln" marker-end="url(#{S5}-a)"/>'
    + f'<path d="M440 66L595 106" class="ln" marker-end="url(#{S5}-a)"/>'
    + col(8, "oksoft", "Reflex (neurally mediated)",
          ["Vasovagal: อารมณ์ ปวด กลัว", "Situational: ไอ กลืน ปัสสาวะ", "Carotid sinus: โกนหนวด", "อายุน้อย trigger ชัด"],
          "box", ["Clinical diagnosis", "Tilt table test", "(เมื่อ dx ไม่ชัด)"])
    + col(247, "misssoft", "Orthostatic",
          ["Hypovolemia: ขาดน้ำ เสียเลือด", "Drugs: vasodilator, diuretic", "Autonomic: PD, DM", "เป็นตอนลุกยืน/เปลี่ยนท่า"],
          "box", ["Orthostatic BP", "SBP ลด ≥ 20 หรือ", "DBP ลด ≥ 10 mmHg"])
    + col(486, "badsoft", "Cardiac (อันตราย)",
          ["Arrhythmia: tachy / brady", "Structural: severe AS, HOCM", "tamponade, MI, PE, dissection", "เป็นตอนนอน/ออกแรง, FHx SCD"],
          "box", ["Arrhythmia → Holter", "Structural → Echo", "+ 12-lead EKG ทุกราย"])
    + '</svg>')
syncope_svg = syncope_svg.replace("(< 1 นาที)", "(&lt; 1 นาที)")


LECTURE = lecture("02", "Valvular heart disease & syncope",
    subtitle="AS · AR · MS · MR · right-sided valves · syncope",
    objectives=[
        "บอกตำแหน่ง timing และการร้าวของ murmur แต่ละลิ้นได้",
        "ระบุสาเหตุที่พบบ่อยของโรคลิ้นหัวใจแต่ละชนิดและอาการของ severe AS ได้",
        "แยก reflex, orthostatic และ cardiac syncope และเลือก investigation ที่เหมาะได้",
        "แยก syncope ออกจาก seizure, TIA, subclavian steal และ hypoglycemia ได้",
    ],
    sections=[
    # ------------------------------------------------------------------ approach murmurs
    sec("cardio-02-01", "Approach to heart murmurs",
        "ฟังตำแหน่ง → timing (systolic/diastolic) → รูปร่าง → การร้าว แล้วเดาลิ้นได้", minutes=5,
        source=f"{D} หน้า 73–78", nl=["2.3.9-3(8)", "B7.2.3-3(1)", "B7.1.1(1)"],
        md='''
### สรุปโรคลิ้นหัวใจทั้ง 8 ตามสไลด์
| ลิ้น | สาเหตุ (ตามสไลด์) | Murmur | ตำแหน่ง / ร้าว |
|---|---|---|---|
| **AS** | degenerative calcification (พบบ่อยสุด) · bicuspid · rheumatic | crescendo-decrescendo **systolic ejection** | R 2nd ICS PSB → **คอ/carotid** |
| **AR** | acute: IE, aortic dissection, trauma · chronic: bicuspid, RF, CTD (Marfan) | **diastolic blowing** | L 3rd ICS PSB (**Erb's point**) |
| **MS** | **rheumatic fever** | **diastolic rumbling** + **opening snap** | apex |
| **MR** | degenerative, DCM, CTD, MI, RF, IE | **systolic** (pansystolic) | apex → **axilla** |
| **PS** | congenital | crescendo-decrescendo SEM + **wide split S2** | L 2nd ICS PSB → **หลัง** |
| **PR** | pulmonary HT, DCM | diastolic | L 2nd ICS PSB |
| **TS** | RF, IE | diastolic | L 4th ICS PSB |
| **TR** | RV dilation (right HF), IE, RF, CTD | systolic | L 4th ICS PSB |

[[fig:murmur-map]]

[[fig:murmur-timing]]

### เคล็ดลับแยก (เสริม)
- **Systolic** = AS, PS, MR, TR (+ VSD, HOCM) · **Diastolic** = AR, PR, MS, TS
- Right-sided murmur **ดังขึ้นตอนหายใจเข้า** (Carvallo sign ใน TR) · left-sided ดังขึ้นตอนหายใจออก
- **HOCM** ก็เป็น SEM ได้ แต่ **ดังขึ้นเมื่อ Valsalva/ยืน** (preload ลด) และไม่ร้าวคอ ส่วน AS เบาลงเมื่อ Valsalva
- **Loud S1** + diastolic rumble ที่ apex + AF = นึกถึง MS ก่อนเสมอ
''',
        figs=[fig("murmur-map", "ตำแหน่งฟังเสียงและการร้าวของ murmur", map_svg,
                  "จุดสีบนหน้าอกคือตำแหน่งฟัง ลูกศรคือทิศการร้าวที่ใช้แยกโรค: AS ร้าวขึ้นคอ MR ร้าวไป axilla"),
              fig("murmur-timing", "Timing ของ murmur ในรอบการเต้นหัวใจ", murmur_svg,
                  "เส้นตั้งคือ S1 และ S2 รูปร่างระหว่างเส้นบอกจังหวะและความดังของ murmur แต่ละกลุ่ม")],
        pearls=[
            "SEM R 2nd ICS ร้าวคอ = AS · pansystolic apex ร้าว axilla = MR",
            "Diastolic rumble ที่ apex + opening snap + loud S1 = MS (rheumatic)",
            "Diastolic blowing ที่ Erb's point (L 3rd ICS) = AR",
            "PS: L 2nd ICS + wide split S2 + ร้าวหลัง",
            "Murmur ข้างขวาดังขึ้นตอนหายใจเข้า (เสริม)",
        ],
        items=[
            mcq("CARDIO-02-01-1",
                "A 45-year-old man has an early diastolic, high-pitched blowing murmur heard best at the left third intercostal space near the sternal border, with a wide pulse pressure. Which valvular lesion is most likely?",
                "Aortic regurgitation",
                ["Mitral stenosis", "Aortic stenosis", "Pulmonic stenosis", "Tricuspid regurgitation"],
                explain='''Diastolic blowing murmur ที่ **Erb's point (L 3rd ICS PSB)** + pulse pressure กว้าง = **aortic regurgitation** (สไลด์หน้า 75)
- MS เป็น diastolic **rumbling** ที่ **apex** มี opening snap ไม่ใช่ blowing ที่ข้างกระดูกอก และไม่ทำให้ pulse pressure กว้าง
- AS เป็น **systolic** ejection murmur ที่ R 2nd ICS และ pulse pressure แคบ
- PS เป็น systolic ejection murmur ที่ L 2nd ICS
- TR เป็น **systolic** murmur ที่ L 4th ICS''',
                pearl="Diastolic blowing ที่ Erb's point = AR",
                topic="Murmur localisation", ref=[f"{D} หน้า 75"], nl=["2.3.9-3(8)"]),
            mcq("CARDIO-02-01-2",
                "A 22-year-old woman has a systolic ejection murmur at the left second intercostal space that radiates to the back, with a widely split second heart sound. What is the most likely diagnosis?",
                "Pulmonic stenosis",
                ["Aortic stenosis", "Mitral regurgitation", "Pulmonic regurgitation", "Tricuspid stenosis"],
                explain='''SEM ที่ **L 2nd ICS PSB ร้าวไปหลัง** + **wide split S2** (RV ejection นานขึ้น P2 มาช้า) = **pulmonic stenosis** สาเหตุส่วนใหญ่เป็น congenital (สไลด์หน้า 77)
- AS เป็น SEM ที่ **R** 2nd ICS ร้าวไปคอ
- MR เป็น pansystolic ที่ apex ร้าวไป axilla
- PR เป็น **diastolic** murmur ที่ L 2nd ICS
- TS เป็น diastolic murmur ที่ L 4th ICS''',
                pearl="PS = L 2nd ICS + wide split S2 + ร้าวหลัง",
                topic="Pulmonic stenosis", ref=[f"{D} หน้า 77"], nl=["2.3.9-3(8)"]),
            mcq("CARDIO-02-01-3",
                "A 35-year-old man with a history of injection drug use has a holosystolic murmur at the left lower sternal border that becomes louder during inspiration, with prominent v waves in the jugular venous pulse. Which lesion is most likely?",
                "Tricuspid regurgitation",
                ["Mitral regurgitation", "Aortic stenosis", "Ventricular septal defect from birth", "Mitral stenosis"],
                explain='''Systolic murmur ที่ **L 4th ICS (lower sternal border)** ดังขึ้นตอนหายใจเข้า (venous return ฝั่งขวาเพิ่ม — Carvallo sign, เสริม) และ JVP มี large v wave = **TR** ใน IVDU มักเกิดจาก IE ที่ลิ้น tricuspid (สไลด์หน้า 78, 324)
- MR ฟังชัดที่ apex ร้าวไป axilla และไม่ดังขึ้นตอนหายใจเข้า
- AS เป็น SEM ที่ R 2nd ICS
- VSD เป็น holosystolic ที่ LLSB ได้ แต่ไม่ดังขึ้นตอนหายใจเข้าและไม่มี v wave ใน JVP และโจทย์ชี้ไปที่ IVDU
- MS เป็น diastolic rumble ที่ apex''',
                pearl="Right-sided murmur ดังขึ้นตอนหายใจเข้า — TR ใน IVDU",
                topic="Tricuspid regurgitation", ref=[f"{D} หน้า 78"], nl=["2.3.9-3(8)"]),
        ]),
    # ------------------------------------------------------------------ AS & AR
    sec("cardio-02-02", "Aortic stenosis & aortic regurgitation",
        "AS: SEM ร้าวคอ + pulsus parvus et tardus · มีอาการ (angina, syncope, HF) → AVR", minutes=6,
        source=f"{D} หน้า 74–75, 88–94", nl=["2.3.9-3(8)", "B7.2.3-3(1)"],
        md='''
### Aortic stenosis (AS)
- สาเหตุ: **degenerative calcification (พบบ่อยที่สุด, ผู้สูงอายุ)** · bicuspid aortic valve (อายุน้อยกว่า) · rheumatic fever
- Murmur: **crescendo-decrescendo systolic ejection murmur ที่ R 2nd ICS PSB ร้าวไปคอ/carotid**
- Carotid pulse: **delayed peak, decreased amplitude, gradual decline** (pulsus parvus et tardus) · sustained apical heave (LVH) · pulse pressure แคบ — ตามข้อสอบในสไลด์หน้า 92
- **อาการสามอย่างของ severe AS: angina · syncope (โดยเฉพาะตอนออกแรง) · heart failure** (dyspnea, orthopnea, PND) (เสริม: เมื่อมีอาการแล้วอัตราตายสูงมากถ้าไม่ผ่าตัด)
- Ix: **echocardiography** (severe AS เสริม: AVA < 1.0 cm2, mean gradient ≥ 40 mmHg, peak velocity ≥ 4 m/s)
- Rx: **symptomatic severe AS → aortic valve replacement** (surgical AVR หรือ TAVI) — ไม่มียาที่ชะลอโรคได้ (เสริม)
- ข้อควรระวัง: เลี่ยง vasodilator/nitrate ขนาดสูงใน severe AS เพราะ preload-dependent → BP ตก (เสริม)

### Aortic regurgitation (AR)
- **Acute**: infective endocarditis, **aortic dissection**, trauma → pulmonary edema/shock ทันที ต้องผ่าตัดด่วน
- **Chronic**: bicuspid, rheumatic, connective tissue disease (Marfan)
- Murmur: **diastolic blowing murmur ที่ L 3rd ICS PSB (Erb's point)** · pulse pressure กว้าง, water-hammer pulse (เสริม)
- Rx (เสริม): symptomatic severe AR หรือ LV dysfunction/dilatation → AVR · BP ใช้ ACEI/ARB (ตามตาราง HT ในสไลด์หน้า 131)

| | AS | AR |
|---|---|---|
| Timing | systolic ejection | early diastolic |
| ตำแหน่ง | R 2nd ICS → คอ | L 3rd ICS (Erb) |
| Pulse | parvus et tardus, PP แคบ | bounding, PP กว้าง (เสริม) |
| ยาลด BP ที่ชอบ (สไลด์หน้า 131) | ACEI/ARB, beta-blocker | ACEI/ARB |

> ข้อสอบในสไลด์หลายข้อบอกว่า murmur อยู่ "left upper parasternal" หรือ "right & left upper parasternal" แต่ **SEM ร้าวไปคอในผู้สูงอายุ = AS** — อย่าหลงไปตอบ carotid stenosis (bruit ไม่ใช่ murmur ที่หน้าอก) หรือ MR (ร้าวไป axilla)
''',
        pearls=[
            "AS ผู้สูงอายุ = degenerative calcification · อายุน้อย = bicuspid",
            "Severe AS: angina, syncope, HF → valve replacement",
            "Carotid pulse ขึ้นช้า แรงน้อย = pulsus parvus et tardus = AS",
            "Acute AR: IE, aortic dissection, trauma",
        ],
        items=[
            mcq("CARDIO-02-02-1",
                "A 75-year-old woman has dyspnea on exertion for 1 year with a history of syncope, orthopnea and PND. BP 150/80 mmHg, PR 72/min, alert, no neck vein engorgement. The carotid pulse has a delayed peak, decreased amplitude and gradual decline. There is a systolic ejection murmur at the right upper parasternal border radiating to the neck with a sustained apical heave. What is the most likely diagnosis?",
                "Aortic stenosis",
                ["Aortic regurgitation", "Carotid stenosis", "Coarctation of aorta", "Hypertrophic obstructive cardiomyopathy"],
                explain='''SEM ที่ RUPSB ร้าวคอ + carotid pulse ขึ้นช้าแรงน้อย (**pulsus parvus et tardus**) + sustained heave + อาการ syncope และ HF = **severe aortic stenosis** (สไลด์หน้า 74, 92)
- AR เป็น diastolic blowing murmur และ pulse เป็น bounding (pulse pressure กว้าง) ตรงข้ามกับรายนี้
- Carotid stenosis ให้ bruit ที่คอ ไม่ทำให้เกิด SEM ที่หน้าอก heave หรืออาการ HF
- Coarctation ทำให้ BP แขนสูงกว่าขา และ pulse ที่ขาเบา/ช้า (radio-femoral delay) ไม่ใช่ carotid pulse ช้า
- HOCM เป็น SEM ที่ LLSB/apex ไม่ร้าวคอ และ carotid pulse ขึ้นเร็วแบบ bisferiens''',
                pearl="SEM ร้าวคอ + pulsus parvus et tardus = AS",
                topic="AS diagnosis", ref=[f"{D} หน้า 91–92"], nl=["2.3.9-3(8)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 91"),
            mcq("CARDIO-02-02-2",
                "A 77-year-old man with HT, DLP and DM presents with syncope. Lungs are clear and there is a grade III systolic ejection murmur at the left upper parasternal border radiating to the neck. Otherwise the examination is normal. What is the most likely diagnosis?",
                "Aortic stenosis",
                ["Acute embolic stroke", "Vasovagal syncope", "Mitral regurgitation", "Orthostatic hypotension"],
                explain='''ผู้สูงอายุ + **syncope** + SEM ร้าวไปคอ = **AS** (structural cardiac syncope) สาเหตุพบบ่อยในวัยนี้คือ degenerative calcification (สไลด์หน้า 88)
- Embolic stroke ทำให้มี neurological deficit ค้าง ไม่ใช่หมดสติแล้วฟื้นเต็มที่ และไม่อธิบาย murmur
- Vasovagal เป็นในคนอายุน้อยที่มี trigger ชัดเจน ไม่ใช่ผู้สูงอายุที่มี murmur
- MR เป็น pansystolic ที่ apex ร้าวไป axilla
- Orthostatic hypotension ต้องมีประวัติเป็นลมตอนลุกยืนและ BP ลดเมื่อเปลี่ยนท่า''',
                pearl="ผู้สูงอายุเป็นลม + SEM ร้าวคอ = AS (cardiac syncope)",
                topic="AS syncope", ref=[f"{D} หน้า 87–88"], nl=["2.3.9-3(8)", "2.2.40"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 87"),
            mcq("CARDIO-02-02-3",
                "A 60-year-old man has central chest pain and dizziness for 1 month, worse when climbing stairs and relieved by rest. BP 100/80 mmHg, PR 88/min, low-volume pulse, grade III/VI systolic ejection murmur at the 2nd right intercostal space radiating to the carotid artery, clear lungs. Echocardiogram confirms severe calcific aortic stenosis. What is the most appropriate management?",
                "Aortic valve replacement",
                ["Thrombolytic agent", "Percutaneous coronary intervention", "Vasodilator therapy", "Percutaneous mitral valvuloplasty"],
                explain='''**Symptomatic severe AS** (exertional angina, presyncope) → การรักษาเดียวที่เปลี่ยน outcome คือ **aortic valve replacement** (surgical AVR หรือ TAVI) (สไลด์หน้า 94)
- Thrombolytic ใช้ใน STEMI ผู้ป่วยไม่มี ST elevation และเจ็บอกจาก AS
- PCI แก้ coronary stenosis แต่ angina ของผู้ป่วยมาจาก LV ที่หนาและ O2 demand สูงจาก AS
- Vasodilator ทำให้ BP ตกอันตรายใน severe AS ที่ preload-dependent และ pulse pressure แคบอยู่แล้ว
- Mitral valvuloplasty ใช้กับ mitral stenosis ไม่ใช่ลิ้น aortic''',
                pearl="Severe AS มีอาการ = เปลี่ยนลิ้น",
                topic="AS treatment", ref=[f"{D} หน้า 93–94"], nl=["2.3.9-3(8)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 93"),
            mcq("CARDIO-02-02-4",
                "A 58-year-old man with well-controlled HT and DLP complains of dyspnea. He has a carotid bruit and a grade III systolic ejection murmur at the right and left upper parasternal borders. Neurological examination is normal and the rest of the examination is unremarkable. What is the most likely diagnosis?",
                "Aortic stenosis",
                ["Carotid artery stenosis", "Mitral regurgitation", "Vasovagal attack", "Pulmonic regurgitation"],
                explain='''SEM ที่ upper parasternal border + เสียงที่ได้ยินบริเวณคอ (murmur ของ AS ร้าวมาที่ carotid ได้ยินคล้าย bruit) + เหนื่อย = **AS** (สไลด์หน้า 90)
- Carotid artery stenosis ทำให้ได้ยิน bruit ที่คอ แต่ไม่ทำให้เกิด SEM ที่หน้าอกและไม่ทำให้เหนื่อย — และ neuro exam ปกติ
- MR ฟังชัดที่ apex ร้าวไป axilla
- Vasovagal attack เป็นอาการหมดสติชั่วคราวที่มี trigger ไม่ใช่เหนื่อยเรื้อรังกับ murmur
- PR เป็น diastolic murmur''',
                pearl="Bruit ที่คอ + SEM ที่ base ของหัวใจ = นึกถึง AS ที่ร้าวขึ้นคอก่อน",
                topic="AS vs carotid bruit", ref=[f"{D} หน้า 89–90"], nl=["2.3.9-3(8)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 89"),
        ]),
    # ------------------------------------------------------------------ MS & MR
    sec("cardio-02-03", "Mitral stenosis & mitral regurgitation",
        "MS = rheumatic, rumble + OS + loud S1 + AF · MR = pansystolic apex ร้าว axilla", minutes=6,
        source=f"{D} หน้า 76, 79–86", nl=["2.3.9-3(8)", "B7.2.3-3(1)", "2.3.9-3(1)"],
        md='''
### Mitral stenosis (MS)
- สาเหตุ: **rheumatic fever (เกือบทั้งหมด)** — ในไทยยังพบบ่อยในหญิงวัยเจริญพันธุ์
- Murmur: **diastolic rumbling murmur ที่ apex + opening snap** · **loud S1**
- กลไก (เสริม): ลิ้นแคบ → LA pressure สูง → **LA โต → AF** และ pulmonary venous HT → pulmonary HT → **loud P2, RV heave**, right HF (hepatomegaly, edema)
- อาการ: dyspnea on exertion, AF (irregular pulse), hemoptysis, embolic stroke (เสริม)
- Ix: **echocardiography**
- Rx (เสริม): AF + MS ปานกลาง–รุนแรง → **warfarin** (สไลด์หน้า 29) · rate control · diuretic · symptomatic severe MS → **percutaneous balloon mitral valvotomy (PBMV)** ถ้าลิ้นเหมาะ ไม่งั้นผ่าตัด · secondary prophylaxis rheumatic fever ด้วย benzathine penicillin

### Mitral regurgitation (MR)
- สาเหตุ: degenerative (MVP), dilated cardiomyopathy, CTD (Marfan), **MI (papillary muscle rupture)**, rheumatic fever, **infective endocarditis**
- Murmur: **systolic (pansystolic) murmur ที่ apex ร้าวไป axilla**
- PE (จากข้อสอบสไลด์หน้า 82): PMI เลื่อนลงซ้าย (LV โต volume overload) · EKG LA enlargement, LVH
- Rx (เสริม): severe symptomatic หรือ LV dysfunction → mitral repair/replacement · acute MR จาก MI/chordae rupture → ผ่าตัดด่วน

> สไลด์ข้อ IE (หน้า 349): pansystolic + diastolic murmur ที่ apex ในคนสงสัย IE = **MR with relative MS** (เลือดไหลผ่านลิ้นมากในช่วง diastole ทำให้เกิด flow rumble) ไม่จำเป็นต้องมี MS จริง
''',
        pearls=[
            "MS = rheumatic · loud S1 + opening snap + diastolic rumble ที่ apex",
            "MS → LA โต → AF → stroke · ให้ warfarin",
            "MS นาน → pulmonary HT → loud P2, RV heave, hepatomegaly",
            "MR = pansystolic ที่ apex ร้าว axilla + PMI เลื่อนลงซ้าย",
            "Acute MR หลัง MI = papillary muscle rupture (เสริม)",
        ],
        items=[
            mcq("CARDIO-02-03-1",
                "A 30-year-old woman has gradual-onset dyspnea on exertion for 1 month without chest pain, cough or fever. BT 37.2°C, BP 120/80 mmHg, PR 80/min totally irregular, RR 20/min. Lungs are clear. There is RV heave 1+, no LV heave, loud S1, normal S2 and a grade III/VI diastolic rumbling murmur. What is the most likely diagnosis?",
                "Mitral stenosis",
                ["Atrial septal defect", "Aortic regurgitation", "Ruptured chordae tendineae", "Hypertrophic cardiomyopathy"],
                explain='''หญิงอายุน้อย + AF (irregular) + **loud S1 + diastolic rumbling murmur** + RV heave (pulmonary HT) โดยไม่มี LV heave = **mitral stenosis** (สไลด์หน้า 80) ส่ง echo ยืนยัน
- ASD ให้ systolic flow murmur ที่ L 2nd ICS และ **fixed split S2** ไม่ใช่ diastolic rumble กับ loud S1
- AR เป็น diastolic **blowing** ที่ Erb's point และทำให้ LV โต (มี LV heave)
- Ruptured chordae ทำให้เกิด **acute MR** = systolic murmur และ pulmonary edema เฉียบพลัน
- HCM เป็น systolic murmur ที่ดังขึ้นเมื่อ Valsalva''',
                pearl="Loud S1 + diastolic rumble + AF ในหญิงอายุน้อย = rheumatic MS",
                topic="MS diagnosis", ref=[f"{D} หน้า 79–80"], nl=["2.3.9-3(8)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 79"),
            mcq("CARDIO-02-03-2",
                "A 40-year-old woman has dyspnea on exertion for 6 months. BT 37.4°C, BP 120/80 mmHg, RR 14/min, HR 76/min. The PMI is at the 6th intercostal space, midclavicular line, with a left parasternal heave and a grade III pansystolic murmur at the apex radiating to the axilla. The jugular veins are flat. EKG shows sinus rhythm, LA enlargement and LVH. What is the most likely diagnosis?",
                "Mitral regurgitation",
                ["Pulmonary stenosis", "Aortic stenosis", "Ventricular septal defect", "Hypertrophic cardiomyopathy"],
                explain='''**Pansystolic murmur ที่ apex ร้าวไป axilla** + PMI เลื่อนลง (LV dilate จาก volume overload) + LAE และ LVH บน EKG = **mitral regurgitation** (สไลด์หน้า 76, 82)
- PS เป็น SEM ที่ L 2nd ICS ร้าวไปหลัง
- AS เป็น SEM ที่ R 2nd ICS ร้าวไปคอ
- VSD เป็น pansystolic ที่ **LLSB** ไม่ร้าวไป axilla
- HCM เป็น SEM ที่ LLSB/apex ดังขึ้นเมื่อ Valsalva ไม่ร้าว axilla''',
                pearl="Pansystolic apex → axilla = MR",
                topic="MR diagnosis", ref=[f"{D} หน้า 81–82"], nl=["2.3.9-3(8)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 81"),
            mcq("CARDIO-02-03-3",
                "A 50-year-old woman has progressive dyspnea on exertion. SpO2 96%. Examination shows an irregular pulse, loud P2, a grade III diastolic rumbling murmur at the apex, crepitation in both lungs and hepatomegaly. What is the most likely underlying cause?",
                "Rheumatic heart disease",
                ["Degenerative valve disease", "Dilated cardiomyopathy", "Cardiac beriberi", "Infective endocarditis"],
                explain='''Diastolic rumble ที่ apex + AF + loud P2 (pulmonary HT) + right HF (hepatomegaly) = **MS** ซึ่งสาเหตุเกือบทั้งหมดคือ **rheumatic heart disease** (สไลด์หน้า 76, 86)
- Degenerative เป็นสาเหตุหลักของ AS และ MR ในผู้สูงอายุ ไม่ใช่ MS
- Dilated cardiomyopathy ทำให้เกิด functional MR (systolic murmur) ไม่ใช่ diastolic rumble
- Cardiac beriberi เป็น high-output HF ในคนดื่มสุรา ไม่ทำให้เกิด diastolic rumble กับ loud P2
- IE ทำให้ลิ้นรั่ว (regurgitation) มากกว่าตีบ และต้องมีไข้''',
                pearl="MS ในผู้ใหญ่ไทย = rheumatic จนกว่าจะพิสูจน์ได้ว่าไม่ใช่",
                topic="MS cause", ref=[f"{D} หน้า 85–86"], nl=["2.3.9-3(8)", "2.3.9-3(1)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 85"),
            mcq("CARDIO-02-03-4",
                "A 57-year-old woman has progressive dyspnea for 6 months. RR 27/min. Examination shows engorged jugular veins, a grade 2/6 pansystolic murmur radiating to the axilla, crackles at both lung bases and pitting edema of both legs. What is the most likely valvular diagnosis?",
                "Mitral regurgitation",
                ["Aortic stenosis", "Aortic regurgitation", "Mitral stenosis", "Tricuspid regurgitation"],
                explain='''Murmur **pansystolic ร้าวไป axilla** = MR · JVP สูง ขาบวม และ crackles เป็นผลของ HF จาก MR นาน (left HF → pulmonary HT → right HF) (สไลด์หน้า 84)
- AS เป็น SEM ร้าวคอ
- AR เป็น diastolic blowing murmur
- MS เป็น diastolic rumble ที่ apex
- TR เป็น systolic ได้และทำให้ JVP สูงกับขาบวม แต่ฟังชัดที่ LLSB และ **ไม่ร้าวไป axilla** — การร้าวไป axilla ชี้ไปที่ลิ้น mitral''',
                pearl="ร้าวไป axilla = ลิ้น mitral แม้จะมี right HF ร่วม",
                topic="MR vs TR", ref=[f"{D} หน้า 83–84"], nl=["2.3.9-3(8)"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 83"),
        ]),
    # ------------------------------------------------------------------ right-sided
    sec("cardio-02-04", "Right-sided valve lesions (PS · PR · TS · TR)",
        "PS congenital · PR จาก pulmonary HT · TS rheumatic/IE · TR จาก RV dilation และ IE ใน IVDU", minutes=3,
        source=f"{D} หน้า 77–78", nl=["2.3.9-3(8)"],
        md='''
| ลิ้น | สาเหตุ | Murmur | ตำแหน่ง |
|---|---|---|---|
| Pulmonic stenosis | **congenital** | crescendo-decrescendo SEM · **wide split S2** · ร้าวไปหลัง | L 2nd ICS PSB |
| Pulmonic regurgitation | **pulmonary hypertension**, DCM | diastolic (Graham Steell เมื่อเกิดจาก pulm HT — เสริม) | L 2nd ICS PSB |
| Tricuspid stenosis | rheumatic fever, IE | diastolic | L 4th ICS PSB |
| Tricuspid regurgitation | **RV dilation (right HF)**, IE, RF, CTD | systolic | L 4th ICS PSB |

### จุดที่ออกสอบ
- **TR ใน IVDU = IE ของลิ้น tricuspid จาก S. aureus** → septic pulmonary emboli (nodular/patchy infiltrates ทั้งสองปอด) (ดูหมวด IE)
- TR ทำให้เกิด **right HF**: JVP สูง large v wave, hepatomegaly (อาจคลำ pulsatile liver), ขาบวม (เสริม)
- PS ที่รุนแรงทำให้ RV heave และ wide split S2 เพราะ RV ejection นานขึ้น (เสริม)
- Right-sided murmur ดังขึ้นตอนหายใจเข้า (เสริม)
''',
        pearls=[
            "PS = congenital + wide split S2",
            "PR มักตามหลัง pulmonary hypertension",
            "TR พบบ่อยจาก RV dilation และ IE ใน IVDU",
            "TS/TR ฟังที่ L 4th ICS PSB",
        ],
        items=[
            mcq("CARDIO-02-04-1",
                "A 62-year-old man with long-standing COPD and pulmonary hypertension develops a new high-pitched early diastolic decrescendo murmur at the left second intercostal space. Which valvular lesion is most likely?",
                "Pulmonic regurgitation",
                ["Aortic stenosis", "Pulmonic stenosis", "Tricuspid stenosis", "Mitral stenosis"],
                explain='''Diastolic murmur ที่ **L 2nd ICS** ในผู้ป่วยที่มี **pulmonary hypertension** = **pulmonic regurgitation** (สไลด์หน้า 77) วงแหวนลิ้น pulmonic ขยายจากความดันสูง
- AS เป็น systolic murmur ที่ R 2nd ICS
- PS เป็น systolic murmur และสาเหตุส่วนใหญ่เป็น congenital
- TS เป็น diastolic แต่ฟังที่ L 4th ICS และเกิดจาก rheumatic/IE
- MS เป็น diastolic rumble ที่ apex''',
                pearl="Pulmonary HT → PR (diastolic ที่ L 2nd ICS)",
                topic="Pulmonic regurgitation", ref=[f"{D} หน้า 77"], nl=["2.3.9-3(8)"]),
            mcq("CARDIO-02-04-2",
                "A 50-year-old woman with long-standing left-sided heart failure now has a holosystolic murmur at the left fourth intercostal space, elevated JVP with prominent v waves and a pulsatile liver. What is the most likely mechanism of the new murmur?",
                "Functional tricuspid regurgitation from right ventricular dilation",
                ["Rheumatic tricuspid stenosis",
                 "Congenital pulmonic stenosis",
                 "Aortic valve calcification",
                 "Papillary muscle rupture of the mitral valve"],
                explain='''Systolic murmur ที่ **L 4th ICS PSB** + JVP มี large v wave + ตับเต้นตามชีพจร = **TR** และในคนที่มี left HF นาน สาเหตุคือ **RV dilation → วงแหวน tricuspid ขยาย (functional TR)** ตามสไลด์หน้า 78
- Tricuspid stenosis เป็น **diastolic** murmur
- Pulmonic stenosis เป็น SEM ที่ L 2nd ICS และเป็น congenital
- Aortic calcification ทำให้เกิด AS ที่ R 2nd ICS
- Papillary muscle rupture ทำให้ acute MR ฟังที่ apex ร้าว axilla พร้อม pulmonary edema เฉียบพลัน''',
                pearl="TR ส่วนใหญ่เป็น functional จาก RV dilation",
                topic="Tricuspid regurgitation", ref=[f"{D} หน้า 78"], nl=["2.3.9-3(8)"]),
        ]),
    # ------------------------------------------------------------------ syncope
    sec("cardio-02-05", "Syncope",
        "Reflex · orthostatic · cardiac · mimic — แยกด้วย prodrome ท่าทาง trigger แล้วเลือก tilt/Holter/echo", minutes=7,
        source=f"{D} หน้า 95–115", nl=["2.2.40", "2.1.5"],
        md='''
### นิยาม
Syncope = หมดสติ **เร็ว ระยะสั้น (มักไม่เกิน 1 นาที)** แล้ว **ฟื้นเองอย่างสมบูรณ์** · อาจมี **brief myoclonic jerk** ได้ (ไม่ได้แปลว่าชัก)
- Prodrome ช่วยบอกกลุ่ม: **vasovagal** = คลื่นไส้ เหงื่อออก ซีด · **orthostatic** = คลื่นไส้ มึนงง · **cardiac** = ใจสั่น (หรือไม่มี prodrome เลย)

[[fig:syncope-tree]]

### 1. Reflex (neurally mediated) syncope
- **Vasovagal**: emotional — กลัว ปวด เห็นเลือด (และยืนนาน ที่ร้อนแออัด — เสริม)
- **Situational**: ไอ กลืน จาม **ปัสสาวะ** ถ่ายอุจจาระ
- **Carotid sinus**: กระตุ้น carotid sinus เล็กน้อย (โกนหนวด ผูกเนกไท)
- อายุไม่มาก · **trigger ชัด** · Dx ทางคลินิก · **tilt table test เมื่อ dx ไม่ชัด**

### 2. Orthostatic syncope
- Hypovolemia (ขาดน้ำ เสียเลือด diuretics) · drug-induced (vasodilators, diuretics, antidepressant) · autonomic failure (**Parkinson's disease, DM**)
- ประวัติเป็นลมตอนยืน/เปลี่ยนท่า · **orthostatic hypotension = SBP ลด ≥ 20 mmHg หรือ DBP ลด ≥ 10 mmHg** (ภายใน 3 นาทีหลังยืน — เสริม)

### 3. Cardiac syncope (อันตราย ต้องหาให้เจอ)
- **Arrhythmia**: tachy (VT, SVT) / brady (sick sinus, AV block)
- **Structural**: severe AS, HOCM, massive MI, cardiac mass, pericardial disease/tamponade
- Cardiopulmonary & great vessel: acute aortic dissection, PE, pulmonary HT
- **Red flags**: เจ็บอก เหนื่อย ใจสั่น murmur · **เป็นลมขณะนอนราบหรือขณะออกแรง** · มีโรคหัวใจ · **ประวัติครอบครัว sudden cardiac death** · EKG ผิดปกติ

### Syncope mimics
| ภาวะ | จุดแยก |
|---|---|
| Seizure | ประวัติ epilepsy · tonic-clonic · **กัดลิ้นด้านข้าง** · ปัสสาวะ/อุจจาระราด · หมดสตินาน · **postictal confusion** |
| Brainstem TIA | มี neurological deficit (CN palsy) · นาน |
| Subclavian steal | เป็นเมื่อใช้แขนข้างนั้น · pulse เบา **BP แขนข้างนั้นต่ำกว่า** |
| Hypoglycemia | DM ที่ใช้ยา · เหงื่อออก มือสั่น · น้ำตาลต่ำ · ดีขึ้นเมื่อให้น้ำตาล |

### Investigation
- **ทุกราย**: ประวัติ ตรวจร่างกาย orthostatic BP และ **12-lead EKG** (เสริม)
- Reflex / orthostatic → **clinical diagnosis** · **tilt table test** ถ้า dx ไม่ชัด
- สงสัย arrhythmia → **Holter** (หรือ event/loop recorder ถ้าเป็นนาน ๆ ครั้ง — เสริม)
- สงสัย structural → **echocardiography**
- EEG / CT brain **ไม่ใช่** การตรวจแรกของ syncope ที่ไม่มีอาการทางระบบประสาท

> เป็นลม **ตอนนอนอยู่บนเตียง** = ไม่เข้ากับ reflex/orthostatic → คิดถึง **arrhythmia → Holter monitoring**
''',
        figs=[fig("syncope-tree", "แยกชนิด syncope และการตรวจ", syncope_svg,
                  "แบ่งเป็นสามกลุ่มจากประวัติ แล้วแต่ละกลุ่มมีการตรวจที่ใช้ยืนยันต่างกัน (กล่องล่าง) กลุ่ม cardiac ต้องรีบหาเพราะเสี่ยงเสียชีวิต")],
        pearls=[
            "Orthostatic hypotension: SBP ลด ≥ 20 หรือ DBP ลด ≥ 10 mmHg",
            "Vasovagal: trigger ชัด + prodrome คลื่นไส้ เหงื่อ ซีด → clinical dx, tilt table ถ้าไม่ชัด",
            "เป็นลมตอนนอนราบ/ออกแรง หรือ FHx SCD = cardiac syncope",
            "Arrhythmia → Holter · structural → echo",
            "Myoclonic jerk สั้น ๆ เกิดใน syncope ได้ — ไม่ใช่ seizure ถ้าไม่มี postictal",
        ],
        items=[
            mcq("CARDIO-02-05-1",
                "A 20-year-old woman had a transient loss of consciousness. Beforehand she felt lightheaded, nauseated and had blurred vision. She had a few myoclonic jerks and fully recovered within 30 seconds. There is no orthostatic hypotension, PR 80/min, RR 16/min and no neurological deficit. What is the most useful investigation?",
                "Tilt table test",
                ["Plasma glucose", "EEG", "Echocardiography", "CT brain"],
                explain='''Prodrome คลื่นไส้ มึน ตาพร่า แล้วหมดสติสั้นฟื้นเร็ว ในหญิงอายุน้อย = **vasovagal syncope** · myoclonic jerk สั้น ๆ พบได้ใน syncope · ถ้าต้องการยืนยันใช้ **tilt table test** (สไลด์หน้า 101, 107)
- Plasma glucose ใช้เมื่อมีประวัติ DM/ใช้ยาลดน้ำตาล และอาการเหงื่อ มือสั่น ที่ดีขึ้นเมื่อได้น้ำตาล ไม่ใช่ฟื้นเองใน 30 วินาที
- EEG ใช้เมื่อสงสัย seizure (tonic-clonic นาน กัดลิ้นด้านข้าง postictal) ซึ่งไม่มี
- Echocardiography ใช้เมื่อสงสัย structural heart disease (murmur, เป็นลมตอนออกแรง)
- CT brain ใช้เมื่อมี neurological deficit หรือ head injury''',
                pearl="Myoclonic jerk สั้น ๆ + ฟื้นเร็ว + prodrome vagal = vasovagal ไม่ใช่ seizure",
                topic="Vasovagal syncope", ref=[f"{D} หน้า 106–107"], nl=["2.2.40"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 106"),
            mcq("CARDIO-02-05-2",
                "An 82-year-old woman feels dizzy and briefly loses consciousness when she gets up at night to urinate. She has had poor oral intake for several days. Examination confirms orthostatic hypotension. What is the most likely cause?",
                "Hypovolemia",
                ["Aortic stenosis", "Coronary artery disease", "Complete heart block", "Vasovagal reflex from fear"],
                explain='''เป็นลมตอนลุกยืน + ตรวจพบ **orthostatic hypotension** + กินได้น้อย = **orthostatic syncope จาก hypovolemia** (สไลด์หน้า 99, 109)
- AS ทำให้เป็นลมขณะออกแรงและต้องมี SEM ร้าวคอ
- CAD ทำให้เจ็บอก ไม่ได้ทำให้ BP ลดตามท่า
- Complete heart block เป็นลมได้ทุกท่า ไม่เกี่ยวกับการลุกยืน และจะพบ HR ช้ามาก
- Vasovagal ต้องมี trigger ทางอารมณ์/ความเจ็บปวด ไม่ใช่ BP ลดตามท่า (micturition syncope เป็น situational แต่โจทย์ตรวจพบ orthostatic hypotension ชัดเจน)''',
                pearl="ลุกยืนแล้ววูบ + orthostatic hypotension → หาสาเหตุ hypovolemia/ยา/autonomic",
                topic="Orthostatic syncope", ref=[f"{D} หน้า 108–109"], nl=["2.2.40"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 108"),
            mcq("CARDIO-02-05-3",
                "A 70-year-old woman has had recurrent syncope over 2 months, typically while lying in bed. Physical examination is unremarkable and the 12-lead EKG is normal. What is the most appropriate investigation?",
                "Holter monitoring",
                ["Tilt table test", "Measurement of orthostatic blood pressure only", "EEG", "Carotid ultrasound"],
                explain='''เป็นลม **ขณะนอนราบ** ไม่เข้ากับ reflex หรือ orthostatic syncope (ซึ่งเป็นตอนยืน) → ต้องคิดถึง **cardiac syncope จาก arrhythmia** แม้ EKG ขณะตรวจปกติ → **Holter monitoring** (สไลด์หน้า 100–101, 113)
- Tilt table test ใช้ยืนยัน reflex syncope ที่ประวัติไม่ชัด ไม่ใช่กรณีที่เป็นตอนนอน
- Orthostatic BP ใช้สำหรับคนที่เป็นตอนเปลี่ยนท่า ไม่ช่วยหา arrhythmia
- EEG ใช้เมื่อสงสัย seizure
- Carotid ultrasound ไม่ได้ช่วยหาสาเหตุ syncope (carotid stenosis ไม่ทำให้หมดสติทั้งตัว)''',
                pearl="Syncope ตอนนอน = arrhythmia จนกว่าจะพิสูจน์ได้ว่าไม่ใช่ → Holter",
                topic="Cardiac syncope", ref=[f"{D} หน้า 112–115"], nl=["2.2.40"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 112"),
            mcq("CARDIO-02-05-4",
                "A 16-year-old student is brought by her mother because she faints repeatedly while standing in the morning school assembly, especially on hot days. Each episode is preceded by nausea, sweating and pallor, and she recovers fully within a minute. What is the most likely cause?",
                "Vasovagal syncope",
                ["Orthostatic hypotension from autonomic failure", "Cardiogenic syncope", "Generalized tonic-clonic seizure", "Hypoglycemia"],
                explain='''การยืนนานในที่ร้อนเป็น trigger คลาสสิกของ **vasovagal (reflex) syncope** ในคนอายุน้อย ร่วมกับ prodrome คลื่นไส้ เหงื่อ ซีด และฟื้นเร็ว (สไลด์หน้า 95, 98, 103)
- Orthostatic hypotension จาก autonomic failure พบในผู้สูงอายุ/PD/DM และเกิดทันทีหลังลุกยืน ไม่ใช่หลังยืนนาน
- Cardiogenic syncope มักไม่มี prodrome, เป็นตอนออกแรงหรือนอน, มี murmur หรือประวัติครอบครัว
- Seizure ทำให้หมดสตินานกว่า มีอาการชักเกร็งกระตุก และ postictal confusion
- Hypoglycemia ต้องมีปัจจัยเสี่ยง (DM ที่ใช้ยา) และไม่ฟื้นเองจนกว่าจะได้น้ำตาล''',
                pearl="ยืนนาน ที่ร้อน + prodrome = vasovagal",
                topic="Vasovagal trigger", ref=[f"{D} หน้า 102–103"], nl=["2.2.40", "2.1.5"],
                kind="old", src="ข้อสอบเก่าในสไลด์ NL2-Cardio หน้า 102"),
            mcq("CARDIO-02-05-5",
                "A 55-year-old man has lightheadedness and near-syncope whenever he uses his left arm to paint a ceiling. Left radial pulse is weaker than the right, and BP is 150/90 mmHg in the right arm and 115/70 mmHg in the left arm. What is the most likely diagnosis?",
                "Subclavian steal syndrome",
                ["Vasovagal syncope", "Carotid sinus hypersensitivity", "Brainstem TIA", "Aortic stenosis"],
                explain='''อาการเกิด **เมื่อใช้แขนข้างนั้น** + pulse ข้างนั้นเบา + **BP แขนซ้ายต่ำกว่าขวามาก** = **subclavian steal syndrome** (left subclavian ตีบก่อนแยก vertebral → ขณะใช้แขน เลือดไหลย้อนจาก vertebral ไปเลี้ยงแขน) (สไลด์หน้า 96)
- Vasovagal ต้องมี trigger ทางอารมณ์/ยืนนาน และ BP สองแขนเท่ากัน
- Carotid sinus hypersensitivity เกิดเมื่อกดบริเวณคอ เช่นโกนหนวด ผูกเนกไท
- Brainstem TIA มี neurological deficit เช่น CN palsy และไม่สัมพันธ์กับการใช้แขน
- AS ให้ SEM ร้าวคอและเป็นลมตอนออกแรงทั่วไป ไม่ทำให้ BP สองแขนต่างกัน''',
                pearl="วูบตอนใช้แขน + BP แขนข้างนั้นต่ำ = subclavian steal",
                topic="Syncope mimics", ref=[f"{D} หน้า 96"], nl=["2.2.40"]),
        ]),
    ])
