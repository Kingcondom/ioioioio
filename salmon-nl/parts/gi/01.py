from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-GI"
OLD = "ตัวอย่างข้อสอบในสไลด์ NL2-GI"

GERD_FIG = '''<svg viewBox="0 0 720 440">
 <defs><marker id="gi-01-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="8" width="220" height="34" rx="9" class="acsoft"/>
 <text x="360" y="30" text-anchor="middle" class="tb">อาการเข้าได้กับ GERD</text>
 <path d="M360 42V60" class="ln" marker-end="url(#gi-01-01-a)"/>
 <rect x="150" y="62" width="420" height="50" rx="9" class="misssoft"/>
 <text x="360" y="82" text-anchor="middle" class="tb">มี Alarm symptoms ไหม?</text>
 <text x="360" y="101" text-anchor="middle" class="t3">dysphagia · odynophagia · GI bleed/anemia · wt loss · vomiting</text>
 <path d="M570 87H612" class="ln" marker-end="url(#gi-01-01-a)"/>
 <text x="590" y="80" text-anchor="middle" class="t3">Yes</text>
 <rect x="614" y="68" width="96" height="38" rx="9" class="badsoft"/>
 <text x="662" y="92" text-anchor="middle" class="tb">EGD</text>
 <path d="M360 112V128M130 128H590M130 128V144M360 128V144M590 128V144" class="ln"/>
 <text x="374" y="124" class="t3">No</text>
 <rect x="20" y="146" width="220" height="34" rx="8" class="c1soft"/>
 <text x="130" y="168" text-anchor="middle" class="tb">Typical symptoms</text>
 <rect x="250" y="146" width="220" height="34" rx="8" class="c1soft"/>
 <text x="360" y="168" text-anchor="middle" class="tb">Non-cardiac chest pain</text>
 <rect x="480" y="146" width="220" height="34" rx="8" class="c1soft"/>
 <text x="590" y="168" text-anchor="middle" class="tb">Extra-esophageal</text>
 <path d="M130 180V198" class="ln" marker-end="url(#gi-01-01-a)"/><path d="M360 180V198" class="ln" marker-end="url(#gi-01-01-a)"/><path d="M590 180V198" class="ln" marker-end="url(#gi-01-01-a)"/>
 <rect x="20" y="200" width="220" height="48" rx="8" class="box"/>
 <text x="130" y="220" text-anchor="middle">LSM + standard-dose PPI</text>
 <text x="130" y="238" text-anchor="middle" class="t3">4–8 wk</text>
 <rect x="250" y="200" width="220" height="48" rx="8" class="box"/>
 <text x="360" y="220" text-anchor="middle">LSM + double-dose PPI</text>
 <text x="360" y="238" text-anchor="middle" class="t3">8 wk</text>
 <rect x="480" y="200" width="220" height="48" rx="8" class="box"/>
 <text x="590" y="220" text-anchor="middle">Exclude other conditions</text>
 <text x="590" y="238" text-anchor="middle" class="t3">ENT · ปอด · หัวใจ (เสริม)</text>
 <path d="M130 248V272" class="ln" marker-end="url(#gi-01-01-a)"/><path d="M590 248V272" class="ln" marker-end="url(#gi-01-01-a)"/>
 <text x="138" y="264" class="t3">no response</text>
 <rect x="20" y="274" width="220" height="48" rx="8" class="box"/>
 <text x="130" y="294" text-anchor="middle">double dose หรือ switch PPI</text>
 <text x="130" y="312" text-anchor="middle" class="t3">8–12 wk</text>
 <rect x="480" y="274" width="220" height="48" rx="8" class="box"/>
 <text x="590" y="294" text-anchor="middle">ถ้ามี typical ร่วมด้วย →</text>
 <text x="590" y="312" text-anchor="middle" class="t3">LSM + double-dose PPI 8–12 wk</text>
 <path d="M130 322V346M360 248V346M590 322V346M130 346H590" class="ln"/>
 <path d="M200 346V370" class="ln" marker-end="url(#gi-01-01-a)"/><path d="M520 346V370" class="ln" marker-end="url(#gi-01-01-a)"/>
 <rect x="20" y="372" width="335" height="58" rx="9" class="oksoft"/>
 <text x="187" y="394" text-anchor="middle" class="tb">ตอบสนอง → Stop / step down</text>
 <text x="187" y="414" text-anchor="middle" class="t3">อาการกลับ → on-demand หรือ continuous PPI</text>
 <rect x="365" y="372" width="335" height="58" rx="9" class="badsoft"/>
 <text x="532" y="394" text-anchor="middle" class="tb">ไม่ตอบสนอง → Refractory GERD</text>
 <text x="532" y="414" text-anchor="middle" class="t3">ทำ EGD / ส่งต่อ GI</text>
</svg>'''

DYS_FIG = '''<svg viewBox="0 0 720 380">
 <defs><marker id="gi-01-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="8" width="220" height="34" rx="9" class="acsoft"/>
 <text x="360" y="30" text-anchor="middle" class="tb">Uninvestigated dyspepsia</text>
 <path d="M360 42V60" class="ln" marker-end="url(#gi-01-02-a)"/>
 <rect x="210" y="62" width="300" height="50" rx="9" class="badsoft"/>
 <text x="360" y="83" text-anchor="middle" class="tb">Age of onset ≥ 50 ปี</text>
 <text x="360" y="102" text-anchor="middle" class="tb">หรือ มี Alarm features?</text>
 <path d="M210 87H130V140" class="ln" marker-end="url(#gi-01-02-a)"/>
 <text x="170" y="80" text-anchor="middle" class="t3">Yes</text>
 <path d="M510 87H590V140" class="ln" marker-end="url(#gi-01-02-a)"/>
 <text x="550" y="80" text-anchor="middle" class="t3">No</text>
 <rect x="30" y="142" width="200" height="50" rx="9" class="c1soft"/>
 <text x="130" y="163" text-anchor="middle" class="tb">EGD</text>
 <text x="130" y="182" text-anchor="middle">+ H. pylori testing</text>
 <rect x="490" y="142" width="200" height="50" rx="9" class="oksoft"/>
 <text x="590" y="163" text-anchor="middle" class="tb">PPI ± prokinetic</text>
 <text x="590" y="182" text-anchor="middle">4–8 wk</text>
 <path d="M590 192V230" class="ln" marker-end="url(#gi-01-02-a)"/>
 <rect x="490" y="232" width="200" height="50" rx="9" class="box"/>
 <text x="590" y="253" text-anchor="middle" class="tb">H. pylori test</text>
 <text x="590" y="272" text-anchor="middle">ถ้าบวก → eradicate</text>
 <path d="M490 167H232" class="lnbad" marker-end="url(#gi-01-02-a)"/>
 <rect x="300" y="150" width="120" height="22" rx="6" class="box"/>
 <text x="360" y="166" text-anchor="middle" class="t3">ไม่ตอบสนอง</text>
 <path d="M130 192V214M70 214H190M70 214V240M190 214V240" class="ln"/>
 <path d="M70 230V242" class="ln" marker-end="url(#gi-01-02-a)"/><path d="M190 230V242" class="ln" marker-end="url(#gi-01-02-a)"/>
 <text x="62" y="232" text-anchor="end" class="t3">ผิดปกติ</text>
 <text x="198" y="232" class="t3">ปกติ</text>
 <rect x="10" y="244" width="120" height="40" rx="8" class="box"/>
 <text x="70" y="269" text-anchor="middle" class="tb">รักษาตามสาเหตุ</text>
 <rect x="140" y="244" width="290" height="110" rx="9" class="misssoft"/>
 <text x="285" y="268" text-anchor="middle" class="tb">Functional dyspepsia</text>
 <text x="285" y="290" text-anchor="middle">PPI · prokinetic</text>
 <text x="285" y="310" text-anchor="middle">TCA · cytoprotective</text>
 <text x="285" y="336" text-anchor="middle" class="t3">(Rome IV: postprandial distress / epigastric pain)</text>
</svg>'''

HP_FIG = '''<svg viewBox="0 0 720 330">
 <text x="20" y="22" class="tb">วัน</text>
 <g class="t3">
 <text x="250" y="22" text-anchor="middle">0</text><text x="355" y="22" text-anchor="middle">5</text>
 <text x="460" y="22" text-anchor="middle">10</text><text x="670" y="22" text-anchor="middle">14</text>
 </g>
 <path d="M250 30V300M355 30V300M460 30V300M670 30V300" class="lnf"/>
 <text x="20" y="54" class="ta">1st line</text>
 <text x="20" y="80" class="tb">Triple</text>
 <text x="20" y="96" class="t3">ดื้อยามากขึ้น</text>
 <rect x="250" y="66" width="420" height="30" rx="6" class="c1soft"/>
 <text x="460" y="86" text-anchor="middle">Amox 1 g + Clarith 500 + PPI · bid × 14 วัน</text>
 <text x="20" y="128" class="tb">Sequential</text>
 <rect x="250" y="112" width="105" height="30" rx="6" class="c2soft"/>
 <text x="302" y="132" text-anchor="middle">Amox 1 g bid</text>
 <rect x="355" y="112" width="105" height="30" rx="6" class="misssoft"/>
 <text x="407" y="126" text-anchor="middle" class="t3">Metro 500 +</text>
 <text x="407" y="139" text-anchor="middle" class="t3">Clarith 500 bid</text>
 <rect x="250" y="146" width="210" height="14" rx="4" class="sunk"/>
 <text x="355" y="157" text-anchor="middle" class="t3">PPI bid × 10 วัน</text>
 <text x="20" y="190" class="tb">Concomitant</text>
 <rect x="250" y="174" width="210" height="30" rx="6" class="c1soft"/>
 <text x="355" y="187" text-anchor="middle" class="t3">Amox 1 g bid + Metro 400 tid</text>
 <text x="355" y="200" text-anchor="middle" class="t3">+ Clarith 500 bid + PPI bid</text>
 <text x="472" y="194" class="t3">10 วัน (4 ตัวพร้อมกัน)</text>
 <path d="M20 218H700" class="lnf"/>
 <text x="20" y="240" class="ta">2nd line</text>
 <text x="20" y="266" class="tb">Levo-amox triple</text>
 <rect x="250" y="250" width="210" height="30" rx="6" class="c2soft"/>
 <text x="355" y="263" text-anchor="middle" class="t3">Levo 500 OD + Amox 1 g bid</text>
 <text x="355" y="276" text-anchor="middle" class="t3">+ PPI bid × 10 วัน</text>
 <text x="20" y="306" class="tb">Bismuth quadruple</text>
 <rect x="250" y="290" width="420" height="30" rx="6" class="acsoft"/>
 <text x="460" y="303" text-anchor="middle" class="t3">Bismuth 524 qid + Metro 250 qid + Tetracycline 500 qid</text>
 <text x="460" y="316" text-anchor="middle" class="t3">+ PPI bid × 14 วัน</text>
</svg>'''

LECTURE = lecture("01", "GERD · Dyspepsia · H. pylori",
    subtitle="อาการแสบร้อนกลางอก ปวดจุกลิ้นปี่ และการกำจัด H. pylori",
    objectives=[
        "บอก typical/extra-esophageal symptoms ของ GERD และข้อบ่งชี้ส่อง EGD ได้",
        "สั่ง PPI ขนาดและระยะเวลาที่ถูกต้องใน GERD ได้",
        "ใช้ algorithm uninvestigated dyspepsia (อายุ ≥ 50 ปี / alarm features) ตัดสินใจ EGD หรือ empirical PPI ได้",
        "เลือกสูตร H. pylori eradication ทั้ง 1st/2nd line และตรวจยืนยันการกำจัดเชื้อได้ถูกเวลา",
    ],
    sections=[
    sec("gi-01-01", "Gastroesophageal reflux disease (GERD)",
        "แสบร้อนกลางอก + เรอเปรี้ยว → PPI 4–8 wk + LSM; มี alarm → EGD", minutes=6,
        source=f"{D} หน้า 5–8", nl=["2.3.11(5)", "B8.4(1)"],
        md='''
### นิยามและกลไก
GERD คือภาวะที่กรด/น้ำย่อยจากกระเพาะไหลย้อนขึ้นหลอดอาหารจนเกิดอาการหรือ mucosal injury เกิดจาก lower esophageal sphincter (LES) คลายตัวชั่วคราวบ่อยหรือความดันต่ำ ร่วมกับ hiatal hernia, gastric emptying ช้า (เสริม)

### อาการ
- **Typical**: chest pain/burning sensation (**heartburn**), **regurgitation**
- dysphagia, odynophagia (ถ้ามี = alarm)
- **Trigger**: นอนราบหลังอาหาร, อาหารมัน, caffeine, alcohol, น้ำอัดลม
- **Extra-esophageal**: chronic dry cough / ไอตอนกลางคืน, hoarseness, dental erosion

### เมื่อไรต้องส่อง EGD
ส่อง EGD เมื่อมี **alarm symptoms** หรือ **failed medication**
- Dysphagia, odynophagia
- GI bleeding, anemia
- Unintentional weight loss
- Recurrent vomiting > 10 ครั้ง/วัน

> GERD ทั่วไปที่ไม่มี alarm **ไม่ต้องส่องก่อน** — ให้ PPI therapeutic trial ได้เลย การตอบสนองต่อ PPI ช่วยยืนยันการวินิจฉัย

[[fig:gi-01-01-algo]]

### การรักษา
**PPI 4–8 สัปดาห์** (standard dose วันละครั้งก่อนอาหารเช้า)

| ยา | ขนาด |
|---|---|
| Omeprazole | 20–40 mg PO OD |
| Esomeprazole | 20–40 mg PO OD |
| Pantoprazole | 40 mg PO OD |

**Lifestyle modification (LSM)**
- งดมื้อดึก งดอาหารกระตุ้น (chocolate, อาหารเผ็ด, อาหารเปรี้ยว, อาหารมัน)
- ลดน้ำหนัก, **ยกหัวเตียงสูง**
- งดบุหรี่ alcohol caffeine

### ไม่ตอบสนองต่อยา
- Typical symptoms: standard PPI 4–8 wk → ไม่ดีขึ้น → **double dose หรือเปลี่ยน PPI** 8–12 wk → ยังไม่ดี = refractory GERD
- Non-cardiac chest pain (NCCP): LSM + double-dose PPI 8 wk (ต้อง R/O หัวใจก่อนเสมอ)
- Extra-esophageal: exclude สาเหตุอื่นก่อน ถ้ามี typical ร่วม → double-dose PPI 8–12 wk
- ตอบสนองแล้ว → stop/step down → ถ้ากลับเป็นซ้ำ → on-demand หรือ continuous PPI

### ภาวะแทรกซ้อน (เสริม)
Erosive esophagitis, peptic stricture (dysphagia ต่อของแข็งค่อย ๆ เป็นมากขึ้น), **Barrett esophagus** → esophageal adenocarcinoma
''',
        figs=[fig("gi-01-01-algo", "แนวทางรักษา GERD ตามกลุ่มอาการ", GERD_FIG,
                  "เริ่มจากถาม alarm ก่อนเสมอ ถ้าไม่มีให้แยกตามชนิดอาการ แล้วปรับขนาด PPI ตามการตอบสนอง")],
        pearls=[
            "GERD ไม่มี alarm → PPI 4–8 wk + LSM ไม่ต้องส่องก่อน",
            "Alarm ของ GERD: dysphagia, odynophagia, GI bleed/anemia, wt loss, vomiting > 10 ครั้ง/วัน",
            "ไม่ตอบสนอง standard dose → double dose หรือ switch PPI 8–12 wk",
            "Extra-esophageal GERD: chronic night cough, hoarseness, dental erosion",
            "ยกหัวเตียง + งดมื้อดึก คือ LSM ที่ข้อสอบชอบถาม",
        ],
        items=[
            mcq("GI-01-01-1", "A 35-year-old man has had burning retrosternal discomfort after large meals and when lying down for 2 months, with occasional sour regurgitation. He has no dysphagia, weight loss, vomiting or melena. Physical examination is normal. Which is the most appropriate management?",
                "Omeprazole 20 mg once daily for 4–8 weeks with lifestyle modification",
                ["Esophagogastroduodenoscopy before starting any treatment", "24-hour esophageal pH monitoring", "Barium swallow", "Laparoscopic Nissen fundoplication"],
                explain='''อาการ heartburn + regurgitation ที่สัมพันธ์กับมื้ออาหารและท่านอน เป็น typical GERD และ **ไม่มี alarm symptoms** จึงรักษาด้วย PPI standard dose 4–8 สัปดาห์ร่วมกับ lifestyle modification ได้ทันที (empirical PPI trial)
- การส่อง EGD ก่อนรักษาสงวนไว้เมื่อมี alarm symptoms หรือรักษาแล้วไม่ดีขึ้น
- 24-hour pH monitoring ใช้ในรายที่วินิจฉัยไม่ชัด/refractory หรือก่อนผ่าตัด ไม่ใช่ first step
- Barium swallow ไม่ไวต่อ reflux และใช้ดู anatomy เช่น stricture เป็นหลัก
- Fundoplication เป็นทางเลือกในรายดื้อยาหรือไม่ต้องการกินยาระยะยาว ไม่ใช่การรักษาเริ่มต้น''',
                pearl="Typical GERD ไม่มี alarm → empirical PPI 4–8 wk + LSM",
                topic="GERD initial management", ref=[f"{D} หน้า 8"], nl=["2.3.11(5)"]),
            mcq("GI-01-01-2", "A 58-year-old woman with long-standing heartburn now reports progressive difficulty swallowing solid food for 6 weeks and a 4-kg weight loss. Which is the most appropriate next step?",
                "Esophagogastroduodenoscopy",
                ["Double-dose proton pump inhibitor for 8 weeks", "Add a prokinetic agent", "H. pylori urea breath test", "Reassurance and lifestyle modification"],
                explain='''ผู้ป่วยมี **alarm symptoms** คือ dysphagia และน้ำหนักลด ต้องส่อง EGD เพื่อหา stricture, Barrett esophagus หรือมะเร็งหลอดอาหาร
- การเพิ่ม PPI เป็น double dose ใช้ใน typical GERD ที่ไม่ตอบสนอง standard dose แต่ไม่มี alarm
- Prokinetic ไม่ได้ตอบปัญหาการกลืนลำบากที่อาจเป็นมะเร็ง
- Urea breath test ใช้กับ dyspepsia ที่ไม่มี alarm ไม่ใช่ dysphagia ที่ต้องดูพยาธิสภาพ
- การให้คำแนะนำอย่างเดียวจะทำให้วินิจฉัยมะเร็งล่าช้า''',
                pearl="GERD + dysphagia/wt loss = alarm → EGD ก่อนเสมอ",
                topic="GERD alarm symptoms", ref=[f"{D} หน้า 6"], nl=["2.3.11(5)", "2.1.17"]),
            mcq("GI-01-01-3", "A 42-year-old man with typical heartburn has taken omeprazole 20 mg once daily for 8 weeks with only partial improvement. He has no alarm features. Which is the most appropriate next step?",
                "Increase to double-dose PPI (or switch to another PPI) for 8–12 weeks",
                ["Stop PPI and start an H2-receptor antagonist", "Refer for fundoplication", "Add sucralfate and continue the same dose indefinitely", "Start empirical H. pylori eradication therapy"],
                explain='''ตาม algorithm GERD: typical symptoms ที่ไม่ตอบสนอง standard-dose PPI 4–8 wk ให้ **เพิ่มเป็น double dose หรือ switch PPI** อีก 8–12 สัปดาห์ ถ้ายังไม่ตอบสนองจึงเรียก refractory GERD และส่องต่อ
- H2RA กดกรดได้น้อยกว่า PPI การเปลี่ยนลงไปจึงไม่เหมาะ
- การผ่าตัดยังเร็วเกินไปเพราะยังไม่ได้ปรับยาให้เต็มที่
- Sucralfate เป็น cytoprotective ไม่ได้แก้ปัญหากรดไหลย้อนหลัก
- H. pylori eradication ไม่ใช่การรักษา GERD''',
                pearl="Standard PPI ไม่พอ → double dose/switch PPI 8–12 wk → ยังไม่ดี = refractory GERD",
                topic="Refractory GERD", ref=[f"{D} หน้า 7"], nl=["2.3.11(5)", "B8.4(1)"]),
        ]),

    sec("gi-01-02", "Dyspepsia: approach & EGD indication",
        "ปวด/ไม่สบายลิ้นปี่ — อายุ ≥ 50 หรือ alarm → EGD; ไม่ใช่ → PPI ± prokinetic แล้ว test & treat", minutes=6,
        source=f"{D} หน้า 9–11, 15–22", nl=["2.3.11(6)", "2.1.11", "2.3.11(10)"],
        md='''
### นิยาม
**Dyspepsia** = ปวดหรือไม่สบายบริเวณ **epigastrium** (เช่น จุกแน่น อิ่มเร็ว แน่นหลังอาหาร) สาเหตุมี peptic ulcer, GERD, มะเร็งกระเพาะ, ยา (NSAIDs) และที่พบบ่อยสุดคือ **functional dyspepsia** (เสริม)

### ข้อบ่งชี้ส่อง EGD
- **Age of onset ≥ 50 ปี** (อาการเริ่มครั้งแรกตอนอายุ ≥ 50)
- Failed medication
- **Alarm features**
  - GI bleeding
  - Odynophagia / dysphagia
  - อาเจียน > 10 ครั้ง/วัน หรือหลังอาการ
  - น้ำหนักลด
  - ประวัติครอบครัว (1st-degree) เป็นมะเร็งกระเพาะ/หลอดอาหาร
  - คลำได้ก้อนที่ epigastrium
  - Iron deficiency anemia (IDA)

[[fig:gi-01-02-algo]]

### Approach (uninvestigated dyspepsia)
1. อายุเริ่มเป็น ≥ 50 ปี หรือมี alarm → **EGD + H. pylori testing**
   - ผิดปกติ → รักษาตามสาเหตุ
   - ปกติ → **functional dyspepsia** → PPI, prokinetic, TCA, cytoprotective
2. อายุ < 50 และไม่มี alarm → **PPI ± prokinetics 4–8 wk** แล้วตรวจ **H. pylori และรักษาถ้าบวก**
3. ไม่ตอบสนอง → EGD

> ข้อสอบชอบให้ "อายุ 56/70 ปี อาการเพิ่งเริ่ม" แม้ไม่มี alarm ก็ตอบ **EGD/gastroscopy** ส่วนคนอายุน้อยไม่มี alarm ตอบ **PPI**

| สถานการณ์ในโจทย์ | คำตอบ |
|---|---|
| 56 ปี new onset postprandial discomfort ไม่มี alarm | Gastroscopy |
| 70 ปี new onset epigastric pain 4 เดือน | EGD |
| 55 ปี น้ำหนักลด 7 kg ใน 1 เดือน | Gastroscopy |
| 20 ปี ปวดลิ้นปี่ 4 เดือน ไม่มี alarm | PPI |

### Functional dyspepsia (เสริม)
ตาม Rome IV: postprandial fullness, early satiety, epigastric pain/burning ≥ 1 อย่าง นาน ≥ 6 เดือน (active 3 เดือนล่าสุด) และ EGD ปกติ แบ่ง postprandial distress syndrome กับ epigastric pain syndrome — ต่างจาก IBS ตรงที่อาการ **ไม่สัมพันธ์กับการถ่ายอุจจาระ**
''',
        figs=[fig("gi-01-02-algo", "Approach to uninvestigated dyspepsia", DYS_FIG,
                  "จุดตัดสินใจเดียวคืออายุเริ่มเป็น ≥ 50 ปีหรือ alarm features — ถ้าใช่ไป EGD ถ้าไม่ใช่ลองยาแล้ว test & treat H. pylori")],
        pearls=[
            "Dyspepsia อายุเริ่มเป็น ≥ 50 ปี หรือ alarm → EGD + H. pylori testing",
            "อายุน้อยไม่มี alarm → PPI ± prokinetic 4–8 wk แล้ว H. pylori test & treat",
            "EGD ปกติ = functional dyspepsia → PPI, prokinetic, TCA",
            "Alarm ที่มักลืม: IDA, FHx มะเร็งกระเพาะ/หลอดอาหารใน 1st-degree, ก้อนที่ epigastrium",
        ],
        items=[
            mcq("GI-01-02-1", "A 56-year-old man presents with new-onset postprandial abdominal discomfort and bloating. He has not lost weight. Examination shows mild epigastric discomfort without organomegaly or mass. Which is the most appropriate next step?",
                "Gastroscopy", ["Ultrasound of the upper abdomen", "Urea breath test for H. pylori", "Plain film of the abdomen", "Empirical treatment with a PPI"],
                explain='''Dyspepsia ที่ **เริ่มเป็นครั้งแรกเมื่ออายุ ≥ 50 ปี** เป็นข้อบ่งชี้ส่อง EGD (gastroscopy) แม้ไม่มี alarm features เพราะต้อง R/O มะเร็งกระเพาะ และระหว่างส่องตรวจ H. pylori ได้ด้วย
- Ultrasound upper abdomen ดูตับ/ถุงน้ำดี ไม่เห็น mucosa กระเพาะ
- Urea breath test (test & treat) ใช้ในคนอายุน้อยไม่มี alarm
- Plain film abdomen ไม่ช่วยใน dyspepsia
- Empirical PPI เหมาะกับอายุ < 50 ปีไม่มี alarm''',
                pearl="Dyspepsia new onset ≥ 50 ปี → EGD", topic="Dyspepsia EGD indication",
                ref=[f"{D} หน้า 15–16"], nl=["2.3.11(6)", "2.1.11"], kind="old", src=OLD),
            mcq("GI-01-02-2", "A 70-year-old woman has had new-onset epigastric pain and postprandial fullness for 4 months. She has no weight loss or other alarm features. Which is the most appropriate management?",
                "Esophagogastroduodenoscopy (EGD)", ["Prokinetic agent", "CT of the abdomen", "Lifestyle modification only", "Proton pump inhibitor trial"],
                explain='''หญิงอายุ 70 ปีที่เพิ่งเริ่มมีอาการ dyspepsia → อายุเริ่มเป็น ≥ 50 ปี จึงต้องส่อง **EGD** เป็นอันดับแรก
- Prokinetic และ PPI trial เป็นทางเลือกในคนอายุน้อยที่ไม่มี alarm
- CT abdomen ไม่ใช่การตรวจหลักของ dyspepsia และไม่เห็นรอยโรคที่ mucosa
- Lifestyle modification อย่างเดียวเสี่ยงพลาดมะเร็งกระเพาะในผู้สูงอายุ''',
                pearl="ผู้สูงอายุ dyspepsia เพิ่งเริ่ม → EGD แม้ไม่มี alarm", topic="Dyspepsia in elderly",
                ref=[f"{D} หน้า 17–18"], nl=["2.3.11(6)"], kind="old", src=OLD),
            mcq("GI-01-02-3", "A 55-year-old man has had epigastric fullness, mostly after meals, for 1 month. His weight has fallen from 67 to 60 kg during this time. Stools are normal yellow. Which is the most appropriate management?",
                "Gastroscopy", ["H2-receptor antagonist", "Proton pump inhibitor", "PPI + amoxicillin + metronidazole", "Double-contrast upper GI study"],
                explain='''มีทั้งอายุ ≥ 50 ปีและ **alarm feature คือน้ำหนักลด 7 kg ใน 1 เดือน** ต้องส่อง gastroscopy เพื่อหามะเร็งกระเพาะ และได้ชิ้นเนื้อด้วย
- H2RA และ PPI เป็นการรักษาตามอาการ อาจบังอาการมะเร็ง
- การให้ยาฆ่าเชื้อ H. pylori โดยไม่ได้ตรวจยืนยันและไม่ได้ส่องไม่เหมาะเมื่อมี alarm
- Double-contrast upper GI study ด้อยกว่า endoscopy และตัดชิ้นเนื้อไม่ได้''',
                pearl="Dyspepsia + น้ำหนักลด = alarm → gastroscopy", topic="Dyspepsia alarm features",
                ref=[f"{D} หน้า 19–20"], nl=["2.3.11(6)", "2.1.11"], kind="old", src=OLD),
            mcq("GI-01-02-4", "A 20-year-old man has had epigastric pain for 4 months. Each episode lasts about 30 minutes and resolves spontaneously. The pain is not relieved by defecation. He has no diarrhea, constipation, weight loss or nocturnal pain. Which is the most appropriate treatment?",
                "Proton pump inhibitor", ["Psychotherapy", "Lactose restriction", "Smooth muscle relaxant", "Triple-drug regimen for H. pylori"],
                explain='''Dyspepsia ในคนอายุ < 50 ปีที่ **ไม่มี alarm feature** → เริ่ม **PPI** (± prokinetic) 4–8 สัปดาห์ อาการไม่สัมพันธ์กับการถ่ายจึงไม่ใช่ IBS
- Psychotherapy ไม่ใช่การรักษาเริ่มต้นของ dyspepsia
- Lactose restriction ใช้เมื่อสงสัย lactose intolerance ซึ่งจะมีท้องเสีย/ท้องอืดหลังดื่มนม
- Smooth muscle relaxant (antispasmodic) ใช้ใน IBS ที่ปวดสัมพันธ์กับการถ่าย
- Triple therapy ต้องตรวจพบ H. pylori ก่อน ไม่ให้แบบ empirical''',
                pearl="Dyspepsia อายุน้อย ไม่มี alarm → PPI", topic="Dyspepsia young no alarm",
                ref=[f"{D} หน้า 21–22"], nl=["2.3.11(6)", "B8.4(1)"], kind="old", src=OLD),
        ]),

    sec("gi-01-03", "H. pylori eradication therapy",
        "Triple/sequential/concomitant (1st line) · levofloxacin/bismuth quadruple (2nd line) · ตรวจยืนยันหลังจบยา ≥ 4 wk", minutes=5,
        source=f"{D} หน้า 12–14, 23–24", nl=["2.3.11(10)", "B8.4(1)"],
        md='''
### ทำไมต้องกำจัด H. pylori
H. pylori ทำให้เกิด chronic gastritis, peptic ulcer, gastric MALT lymphoma และ gastric adenocarcinoma (เสริม) — **ผลบวกต้องรักษาทุกราย** และในผู้ป่วย peptic ulcer/ulcer bleeding ต้องตรวจหาเชื้อเสมอ

### สูตรยา (ตามสไลด์)
[[fig:gi-01-03-reg]]

| แนว | สูตร | ยา | ระยะเวลา |
|---|---|---|---|
| 1st line | **Triple therapy** | Amoxicillin 1 g bid + Clarithromycin 500 mg bid + PPI bid | **14 วัน** |
| 1st line | **Sequential** | Amoxicillin 1 g bid 5 วัน → Metronidazole 500 mg + Clarithromycin 500 mg bid 5 วัน; PPI bid ตลอด | 10 วัน |
| 1st line | **Concomitant** | Amoxicillin 1 g bid + Metronidazole 400 mg tid + Clarithromycin 500 mg bid + PPI bid | 10 วัน |
| 2nd line | **Levofloxacin-amoxicillin triple** | Levofloxacin 500 mg OD + Amoxicillin 1 g bid + PPI bid | 10 วัน |
| 2nd line | **Bismuth quadruple** | Bismuth subsalicylate 524 mg qid + Metronidazole 250 mg qid + Tetracycline 500 mg qid + PPI bid | **14 วัน** |

> Triple therapy ยังอยู่ใน 1st line แต่ **พบการดื้อ clarithromycin มากขึ้นเรื่อย ๆ** ในพื้นที่ดื้อสูง แนวทางปัจจุบันนิยม bismuth quadruple เป็น 1st line (เสริม)

### การตรวจยืนยันว่ากำจัดเชื้อหมด
- ทำหลังรักษาครบ **อย่างน้อย 4 สัปดาห์** ด้วย **urea breath test** หรือ **stool antigen**
- หยุด PPI ≥ 2 สัปดาห์ก่อนตรวจ เพราะ PPI ทำให้ผลลบลวง (เสริม)
- Serology (anti-H. pylori IgG) **ใช้ยืนยันการกำจัดเชื้อไม่ได้** เพราะบวกค้างนาน (เสริม)
''',
        figs=[fig("gi-01-03-reg", "สูตรกำจัด H. pylori เทียบระยะเวลา", HP_FIG,
                  "แต่ละแถบคือช่วงวันที่ให้ยา — sequential เปลี่ยนยาที่วันที่ 5 ส่วน triple และ bismuth quadruple ยาว 14 วัน")],
        pearls=[
            "Triple therapy = amoxicillin + clarithromycin + PPI bid 14 วัน",
            "Bismuth quadruple = bismuth + metronidazole + tetracycline + PPI 14 วัน (2nd line ตามสไลด์)",
            "ยืนยันการกำจัดเชื้อด้วย UBT หรือ stool Ag หลังจบยา ≥ 4 สัปดาห์",
            "Serology ใช้ยืนยันการกำจัดเชื้อไม่ได้",
        ],
        items=[
            mcq("GI-01-03-1", "A 36-year-old man was diagnosed with H. pylori gastritis and completed omeprazole, amoxicillin and metronidazole for 10 days. At follow-up he has no further symptoms and the abdomen is soft and non-tender. Which is the most appropriate advice?",
                "Urea breath test at least 4 weeks after completing therapy", ["No further investigation is needed", "Long-term omeprazole", "Annual barium upper GI study", "Repeat EGD in 4 weeks"],
                explain='''หลังรักษา H. pylori ต้อง **ตรวจยืนยันว่ากำจัดเชื้อหมด (test of cure)** เพราะอาการหายไม่ได้แปลว่าเชื้อหมด ทำด้วย urea breath test หรือ stool antigen หลังจบยาอย่างน้อย 4 สัปดาห์
- การไม่ตรวจต่อเสี่ยงให้เชื้อค้าง → ulcer กลับเป็นซ้ำ
- Omeprazole ระยะยาวไม่จำเป็นเมื่อไม่มีอาการ และทำให้ผลตรวจเชื้อลบลวง
- Barium study ไม่บอกเรื่องเชื้อ
- Repeat EGD invasive เกินจำเป็นใน gastritis ที่ไม่มีแผล (ส่องซ้ำใช้ใน gastric ulcer)''',
                pearl="H. pylori test of cure: UBT/stool Ag ≥ 4 wk หลังจบยา", topic="H. pylori test of cure",
                ref=[f"{D} หน้า 23–24"], nl=["2.3.11(10)"], kind="old", src=OLD),
            mcq("GI-01-03-2", "A 45-year-old woman with a duodenal ulcer has a positive rapid urease test. She has no drug allergy. According to the regimen listed as standard triple therapy, which combination and duration is correct?",
                "Amoxicillin 1 g bid + clarithromycin 500 mg bid + PPI bid for 14 days",
                ["Amoxicillin 1 g bid + PPI bid for 5 days", "Metronidazole 500 mg bid + PPI bid for 7 days", "Levofloxacin 500 mg OD + amoxicillin 1 g bid + PPI bid for 10 days", "Clarithromycin 500 mg bid + PPI bid for 7 days"],
                explain='''Standard triple therapy ตามสไลด์คือ **amoxicillin 1 g bid + clarithromycin 500 mg bid + PPI bid นาน 14 วัน**
- Amoxicillin + PPI 5 วันเป็นเพียงครึ่งแรกของ sequential therapy ไม่ใช่สูตรครบ
- Metronidazole + PPI สองตัว หรือ clarithromycin + PPI สองตัว (dual therapy) อัตรากำจัดเชื้อต่ำและเพิ่มการดื้อยา
- Levofloxacin-amoxicillin triple เป็น 2nd line สำหรับคนที่ล้มเหลวจากสูตรแรก''',
                pearl="Triple therapy 14 วัน: amox + clarith + PPI", topic="H. pylori triple therapy",
                ref=[f"{D} หน้า 12"], nl=["2.3.11(10)", "B8.4(1)"]),
            mcq("GI-01-03-3", "A 50-year-old man completed 14 days of amoxicillin, clarithromycin and a PPI for H. pylori-positive gastric ulcer. A urea breath test 6 weeks later is still positive. Which is the most appropriate next regimen?",
                "Bismuth subsalicylate + metronidazole + tetracycline + PPI for 14 days",
                ["Repeat the same clarithromycin-based triple therapy", "Amoxicillin + PPI for 14 days", "Metronidazole monotherapy for 7 days", "Continue PPI alone and repeat breath test in 3 months"],
                explain='''ล้มเหลวจาก clarithromycin-based triple → ใช้ **2nd line** ได้แก่ bismuth-containing quadruple therapy (bismuth subsalicylate 524 mg qid + metronidazole 250 mg qid + tetracycline 500 mg qid + PPI bid 14 วัน) หรือ levofloxacin-amoxicillin triple
- ให้สูตรเดิมซ้ำมักล้มเหลวเพราะเชื้อน่าจะดื้อ clarithromycin แล้ว
- Amoxicillin + PPI สองตัวไม่พอ
- Metronidazole ตัวเดียวทำให้ดื้อยา
- PPI อย่างเดียวไม่ฆ่าเชื้อ แค่กดอาการ''',
                pearl="Triple therapy ล้มเหลว → bismuth quadruple หรือ levofloxacin triple", topic="H. pylori 2nd line",
                ref=[f"{D} หน้า 14"], nl=["2.3.11(10)", "B8.4(1)"]),
        ]),
    ])
