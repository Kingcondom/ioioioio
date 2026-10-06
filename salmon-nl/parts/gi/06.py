from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-GI"
OLD = "ตัวอย่างข้อสอบในสไลด์ NL2-GI"

APAP_MECH = '''<svg viewBox="0 0 720 304">
 <defs><marker id="gi-06-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="260" y="10" width="200" height="44" rx="10" class="acsoft"/>
 <text x="360" y="37" text-anchor="middle" class="tb">Paracetamol</text>
 <path d="M300 54L130 100" class="ln" marker-end="url(#gi-06-01-a)"/>
 <path d="M360 54V100" class="ln" marker-end="url(#gi-06-01-a)"/>
 <path d="M420 54L590 100" class="lnf" marker-end="url(#gi-06-01-a)"/>
 <text x="190" y="70" text-anchor="middle" class="t3">85–90%</text>
 <text x="372" y="82" class="t3">5–9% (CYP2E1)</text>
 <text x="540" y="70" text-anchor="middle" class="t3">&lt; 5%</text>
 <rect x="20" y="102" width="220" height="50" rx="9" class="oksoft"/>
 <text x="130" y="123" text-anchor="middle" class="tb">Glucuronide &amp; sulfate</text>
 <text x="130" y="141" text-anchor="middle" class="t3">ขับทางปัสสาวะ ไม่เป็นพิษ</text>
 <rect x="270" y="102" width="180" height="50" rx="9" class="bad"/>
 <text x="360" y="133" text-anchor="middle" class="tw">NAPQI (toxic)</text>
 <rect x="480" y="102" width="220" height="50" rx="9" class="box"/>
 <text x="590" y="132" text-anchor="middle">ขับออกรูปเดิมทางปัสสาวะ</text>
 <path d="M300 152L210 196" class="ln" marker-end="url(#gi-06-01-a)"/>
 <path d="M420 152L510 196" class="lnbad" marker-end="url(#gi-06-01-a)"/>
 <rect x="80" y="198" width="230" height="50" rx="9" class="oksoft"/>
 <text x="195" y="219" text-anchor="middle" class="tb">จับกับ glutathione</text>
 <text x="195" y="237" text-anchor="middle" class="t3">→ ไม่เป็นพิษ</text>
 <rect x="410" y="198" width="230" height="50" rx="9" class="badsoft"/>
 <text x="525" y="219" text-anchor="middle" class="tb">Glutathione หมด</text>
 <text x="525" y="237" text-anchor="middle" class="t3">→ hepatocyte necrosis (zone 3)</text>
 <rect x="20" y="262" width="300" height="32" rx="9" class="c1"/>
 <text x="170" y="283" text-anchor="middle" class="tw">NAC เติม glutathione</text>
 <path d="M170 262V250" class="lnc1" marker-end="url(#gi-06-01-a)"/>
 <rect x="360" y="256" width="350" height="40" rx="9" class="misssoft"/>
 <text x="535" y="272" text-anchor="middle" class="t3">alcohol · INH · phenytoin · phenobarb → ↑CYP2E1</text>
 <text x="535" y="288" text-anchor="middle" class="t3">ขาดอาหาร → glutathione ต่ำ</text>
</svg>'''

# Rumack-Matthew: x: hr 0 -> 80, 24 -> 680 (25 px/hr); y log: 1000 -> 30, 1 -> 270 (80 px per decade)
import math
def Y(c):
    return 270 - 80 * math.log10(c)
pts = " ".join(f"{80 + h * 25:.0f},{Y(150 * 2 ** (-(h - 4) / 4)):.1f}" for h in range(4, 25))
pts2 = " ".join(f"{80 + h * 25:.0f},{Y(200 * 2 ** (-(h - 4) / 4)):.1f}" for h in range(4, 25))
area = f"M180,{Y(150):.1f} " + " ".join(f"L{80 + h * 25:.0f},{Y(150 * 2 ** (-(h - 4) / 4)):.1f}" for h in range(5, 25)) + f" L680,30 L180,30 Z"
NOMO = f'''<svg viewBox="0 0 720 330">
 <path d="{area}" class="badsoft"/>
 <rect x="80" y="30" width="100" height="240" class="sunk"/>
 <text x="130" y="140" text-anchor="middle" class="t3">&lt; 4 ชม.</text>
 <text x="130" y="156" text-anchor="middle" class="t3">ใช้ไม่ได้</text>
 <polyline points="{pts}" class="lnbad"/>
 <polyline points="{pts2}" class="lnf"/>
 <path d="M80 270H690M80 270V24" class="ln"/>
 <g class="t3">
  <text x="72" y="{Y(1000)+4:.0f}" text-anchor="end">1000</text>
  <text x="72" y="{Y(100)+4:.0f}" text-anchor="end">100</text>
  <text x="72" y="{Y(10)+4:.0f}" text-anchor="end">10</text>
  <text x="72" y="{Y(1)+4:.0f}" text-anchor="end">1</text>
  <text x="80" y="288" text-anchor="middle">0</text><text x="180" y="288" text-anchor="middle">4</text>
  <text x="280" y="288" text-anchor="middle">8</text><text x="380" y="288" text-anchor="middle">12</text>
  <text x="480" y="288" text-anchor="middle">16</text><text x="580" y="288" text-anchor="middle">20</text>
  <text x="680" y="288" text-anchor="middle">24</text>
 </g>
 <path d="M80 {Y(100):.0f}H690M80 {Y(10):.0f}H690" class="lnf"/>
 <text x="385" y="312" text-anchor="middle" class="tb">ชั่วโมงหลังกินยา (single acute ingestion)</text>
 <text x="20" y="18" class="t3">ระดับยา (mg/L, log scale)</text>
 <text x="196" y="{Y(150)-8:.0f}" class="ta">150 mg/L ที่ 4 ชม.</text>
 <text x="470" y="70" text-anchor="middle" class="tb">เหนือเส้น = treatment line → ให้ NAC</text>
 <text x="300" y="240" class="t3">ใต้เส้น = likely safe · ระดับลดครึ่งทุก ~4 ชม.</text>
</svg>'''

ALD = '''<svg viewBox="0 0 720 230">
 <defs><marker id="gi-06-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="210" height="160" rx="10" class="oksoft"/>
 <text x="115" y="34" text-anchor="middle" class="tb">Alcoholic steatosis</text>
 <text x="115" y="58" text-anchor="middle" class="t3">ไขมันสะสม ไม่มีอักเสบ</text>
 <text x="115" y="80" text-anchor="middle">ไม่มีอาการ ± ตับโต</text>
 <text x="115" y="146" text-anchor="middle" class="ta">หยุดเหล้า → กลับคืนได้</text>
 <rect x="255" y="10" width="210" height="160" rx="10" class="misssoft"/>
 <text x="360" y="34" text-anchor="middle" class="tb">Alcoholic steatohepatitis</text>
 <text x="360" y="58" text-anchor="middle" class="t3">อักเสบ + fibrosis</text>
 <text x="360" y="80" text-anchor="middle">ตัวเหลือง ไข้ ตับโตกดเจ็บ</text>
 <text x="360" y="100" text-anchor="middle">AST:ALT &gt; 2 · AST &lt; 300</text>
 <text x="360" y="120" text-anchor="middle">↑GGT</text>
 <text x="360" y="146" text-anchor="middle" class="ta">หยุดเหล้า → กลับคืนได้</text>
 <rect x="500" y="10" width="210" height="160" rx="10" class="badsoft"/>
 <text x="605" y="34" text-anchor="middle" class="tb">Alcohol-associated cirrhosis</text>
 <text x="605" y="58" text-anchor="middle" class="t3">fibrosis มาก</text>
 <text x="605" y="80" text-anchor="middle">ระยะแรกไม่มีอาการ</text>
 <text x="605" y="100" text-anchor="middle">ระยะหลัง decompensate</text>
 <text x="605" y="146" text-anchor="middle" class="ta">กลับคืนไม่ได้ → transplant</text>
 <path d="M220 90H253" class="ln" marker-end="url(#gi-06-03-a)"/>
 <path d="M465 90H498" class="ln" marker-end="url(#gi-06-03-a)"/>
 <rect x="10" y="184" width="700" height="38" rx="9" class="sunk"/>
 <text x="360" y="208" text-anchor="middle">ทุกระยะ: หยุดเหล้า + nutritional therapy · steroid ถ้า severe alcoholic hepatitis</text>
</svg>'''

WILSON = '''<svg viewBox="0 0 720 260">
 <rect x="250" y="90" width="220" height="70" rx="12" class="acsoft"/>
 <text x="360" y="118" text-anchor="middle" class="tb">Wilson disease</text>
 <text x="360" y="138" text-anchor="middle" class="t3">AR · ATP7B · ทองแดงสะสม</text>
 <path d="M250 110L190 70M470 110L530 70M250 140L190 180M470 140L530 180" class="ln"/>
 <rect x="10" y="20" width="230" height="74" rx="9" class="c1soft"/>
 <text x="125" y="42" text-anchor="middle" class="tb">ตับ</text>
 <text x="125" y="62" text-anchor="middle" class="t3">HSM · ตัวเหลือง · cirrhosis</text>
 <text x="125" y="80" text-anchor="middle" class="t3">AST &gt; ALT · ↑TB</text>
 <rect x="480" y="20" width="230" height="74" rx="9" class="c2soft"/>
 <text x="595" y="42" text-anchor="middle" class="tb">สมอง</text>
 <text x="595" y="62" text-anchor="middle" class="t3">dysarthria · gait · parkinsonism</text>
 <text x="595" y="80" text-anchor="middle" class="t3">tremor · dementia · hallucination</text>
 <rect x="10" y="160" width="230" height="74" rx="9" class="misssoft"/>
 <text x="125" y="182" text-anchor="middle" class="tb">ตา</text>
 <text x="125" y="202" text-anchor="middle" class="t3">Kayser-Fleischer ring</text>
 <text x="125" y="220" text-anchor="middle" class="t3">(ทองแดงที่ขอบ cornea)</text>
 <rect x="480" y="160" width="230" height="90" rx="9" class="box"/>
 <text x="595" y="180" text-anchor="middle" class="tb">Lab</text>
 <text x="595" y="198" text-anchor="middle" class="t3">↓ceruloplasmin (&lt; 20 mg/dL)</text>
 <text x="595" y="214" text-anchor="middle" class="t3">↓total Cu · ↑free Cu</text>
 <text x="595" y="230" text-anchor="middle" class="t3">↑24-hr urine Cu (&gt; 100 mcg)</text>
</svg>'''

LECTURE = lecture("06", "Toxic, ischemic, alcoholic, fatty & metabolic liver disease",
    subtitle="Paracetamol overdose · ischemic hepatitis · alcohol-related liver disease · MASLD · Wilson disease",
    objectives=[
        "อธิบายกลไก NAPQI และตัดสินใจให้ NAC จาก Rumack-Matthew nomogram/ขนาดที่กิน",
        "วินิจฉัย ischemic hepatitis จาก AST/ALT พุ่งหลังภาวะช็อก",
        "แยก alcoholic hepatitis (AST:ALT > 2, AST < 300, GGT สูง) จาก fatty liver (ALT > AST)",
        "วินิจฉัย Wilson disease จากอาการตับ + ระบบประสาท + KF ring และ lab ทองแดง",
    ],
    sections=[
    sec("gi-06-01", "Paracetamol (acetaminophen) overdose",
        "> 7–10 g ครั้งเดียว หรือ 10–20 g ใน 3 วันในคนเสี่ยง · NAPQI · charcoal < 4 ชม. · NAC ตาม nomogram/> 150 mg/kg", minutes=7,
        source=f"{D} หน้า 168–177", nl=["2.3.18(7)", "2.2.46", "B1.7.6"],
        md='''
### ขนาดที่เป็นพิษ
- Therapeutic dose **≤ 4 g/วัน**
- **ตั้งใจกินเกินขนาด (single dose) > 7–10 g**
- **ไม่ตั้งใจ (therapeutic misadventure) 10–20 g ใน 3 วัน** ในผู้ป่วยที่มีความเสี่ยง
  - Alcohol (เรื้อรัง)
  - Malnutrition (glutathione ต่ำ)
  - ยาที่กระตุ้น CYP2E1: phenobarbital, phenytoin, isoniazid, zidovudine

### กลไก
[[fig:gi-06-01-mech]]

### ระยะทางคลินิก
| ระยะ | เวลา | อาการ |
|---|---|---|
| I | 0.5–24 ชม. | เบื่ออาหาร คลื่นไส้อาเจียน อ่อนเพลีย — ดูปกติ |
| II | 24–48 ชม. | อาการลดลง แต่ **liver enzyme และ bilirubin เริ่มสูง**, ไตเริ่มเสีย |
| III | 72–96 ชม. | **Hepatic necrosis**: coagulopathy, ตัวเหลือง, ไตวาย, คลื่นไส้กลับมา, เสียชีวิตจากตับวาย |
| IV | 4–14 วัน | ถ้ารอดระยะ III ตับและไตกลับปกติ |

> ระยะแรกอาการน้อย — **อย่าวางใจว่าไม่เป็นไร** ต้องเจาะระดับยาเสมอ AST/ALT ใน paracetamol overdose สูงได้ถึงหลายพัน (สูงสุดในบรรดาสาเหตุ)

### การรักษา
**GI decontamination** (ลดการดูดซึม)
- Gastric lavage (< 1 ชม.)
- **Activated charcoal ภายใน 4 ชม.**

**Antidote: N-acetylcysteine (NAC)** PO/IV — เติม glutathione
- **ควรเริ่มภายใน 8 ชม.** หรือเร็วที่สุด (ได้ผลแม้มาช้า — เสริม)
- **ข้อบ่งชี้ NAC**
  - ระดับยา **เหนือ treatment line** (Rumack-Matthew nomogram)
  - สงสัยกินครั้งเดียว **> 150 mg/kg หรือ 7.5 g** (กรณีเจาะระดับยาไม่ได้)

| มาเมื่อ | ทำอะไร |
|---|---|
| < 4 ชม. | Gastric lavage (< 1 ชม.) / activated charcoal → **เจาะระดับยาที่ 4 ชม.** |
| > 4 ชม. | เจาะระดับยาทันที |
| ระดับเหนือเส้น หรือกิน > 150 mg/kg / 7.5 g | **NAC** + monitor liver injury |

### Rumack-Matthew nomogram
[[fig:gi-06-01-nomo]]
- ใช้ได้กับ **acute single ingestion** เท่านั้น ไม่ใช้กับ chronic ingestion
- **ใช้ไม่ได้ก่อน 4 ชม.** หลังกิน (ยังดูดซึมไม่หมด)
- Treatment line เริ่มที่ **150 mg/L (≈ 1,000 µmol/L) ที่ 4 ชม.** (ระวังหน่วย)
''',
        figs=[fig("gi-06-01-mech", "การเปลี่ยนแปลง paracetamol ในตับและจุดออกฤทธิ์ของ NAC", APAP_MECH,
                  "ปกติ NAPQI ถูก glutathione กำจัด เมื่อกินมากหรือ CYP2E1 ถูกกระตุ้น glutathione หมด → ตับตาย; NAC ช่วยเติม glutathione"),
              fig("gi-06-01-nomo", "Rumack-Matthew nomogram (แบบย่อ)", NOMO,
                  "แกนตั้งเป็น log scale ระดับยาที่เจาะหลัง 4 ชม. ถ้าอยู่ในโซนแดงเหนือเส้นทึบให้ NAC; เส้นประคือเส้นเดิม 200 mg/L")],
        pearls=[
            "Paracetamol toxic: single > 7–10 g หรือ 150 mg/kg; misadventure 10–20 g ใน 3 วัน + risk",
            "Alcohol, INH, phenytoin, phenobarbital ↑CYP2E1 → NAPQI มากขึ้น",
            "Activated charcoal < 4 ชม.; เจาะระดับยาที่ ≥ 4 ชม.",
            "NAC เติม glutathione เริ่มภายใน 8 ชม.; ข้อบ่งชี้: เหนือ treatment line หรือ > 150 mg/kg",
            "Nomogram ใช้กับ acute single ingestion เท่านั้น",
        ],
        items=[
            mcq("GI-06-01-1", "A 30-year-old man has nausea and vomiting. He has drunk 1–2 bottles of whiskey daily for 10 years. One week ago he took paracetamol 2 tablets (500 mg) 4 times a day for headache. Temperature 37 °C. He has mild pallor, jaundice, spider angiomas, palmar erythema, tender hepatomegaly and no ascites. Which is the most likely diagnosis according to the slide answer?",
                "Acetaminophen toxicity", ["Acute pancreatitis", "Acute viral hepatitis", "Ascending cholangitis", "Alcoholic intoxication"],
                explain='''เฉลยในสไลด์คือ **paracetamol toxicity** แบบ therapeutic misadventure: ผู้ป่วยมี **ความเสี่ยงคือ alcohol เรื้อรัง** (CYP2E1 ถูกกระตุ้นและ glutathione ต่ำ) ทำให้แม้ขนาดที่กิน (~4 g/วัน) ก็เกิดพิษต่อตับได้ มาด้วยคลื่นไส้ อาเจียน ตัวเหลือง ตับโตกดเจ็บ
- Acute pancreatitis ปวดลิ้นปี่ร้าวหลัง ไม่ได้มาด้วยตัวเหลืองตับโต
- Acute viral hepatitis ไม่มีประวัติเสี่ยงและมี prodrome ไข้
- Ascending cholangitis ต้องมีไข้ RUQ pain ตัวเหลือง (Charcot triad) ร่วมกับ biliary obstruction
- Alcoholic intoxication ไม่อธิบายตัวเหลืองและตับกดเจ็บ
> หมายเหตุ: ตัวเลขในโจทย์ (2 เม็ด × 4 ครั้ง = 4 g/วัน) อยู่ในขนาด therapeutic ตามตำรา และอาการคนนี้อาจเข้าได้กับ alcoholic hepatitis ด้วย — ข้อสอบตามสไลด์ต้องการให้นึกถึงความเสี่ยงของคนดื่มเหล้าที่กิน paracetamol''',
                pearl="คนดื่มเหล้าเรื้อรัง + paracetamol ขนาดปกติ → เสี่ยงพิษต่อตับ", topic="Therapeutic misadventure",
                ref=[f"{D} หน้า 174–175"], nl=["2.3.18(7)"], kind="old", src=OLD),
            mcq("GI-06-01-2", "A 19-year-old woman (weight 50 kg) ingested 30 tablets of paracetamol 500 mg (15 g) 2 hours ago after an argument. She is alert with mild nausea. Vital signs are normal. Which is the most appropriate management now?",
                "Give activated charcoal and check a serum paracetamol level at 4 hours after ingestion", ["Discharge because she is asymptomatic", "Check a paracetamol level immediately and plot it on the nomogram", "Start hemodialysis", "Give IV vitamin K"],
                explain='''มาภายใน 4 ชม. หลังกิน → ให้ **activated charcoal** ลดการดูดซึม แล้ว **เจาะระดับยาที่ 4 ชม.** เพื่อ plot บน Rumack-Matthew nomogram (ขนาดที่กิน 300 mg/kg > 150 mg/kg จึงควรเริ่ม NAC ด้วยถ้าผลระดับยาจะช้า)
- ไม่มีอาการไม่ได้แปลว่าปลอดภัย ระยะ I อาการน้อยเสมอ
- ระดับยาที่เจาะ < 4 ชม. plot บน nomogram ไม่ได้เพราะยังดูดซึมไม่หมด
- Hemodialysis ใช้ในรายที่ระดับยาสูงมากร่วมกับ AOC/metabolic acidosis เท่านั้น
- Vitamin K ไม่ใช่ antidote''',
                pearl="Paracetamol < 4 ชม. → charcoal + เจาะระดับที่ 4 ชม.", topic="Paracetamol decontamination",
                ref=[f"{D} หน้า 171–173"], nl=["2.2.46", "B1.7.6"]),
            mcq("GI-06-01-3", "A 25-year-old man took an unknown number of paracetamol tablets 6 hours ago. The serum paracetamol level at 6 hours is 160 mg/L. What is the mechanism of action of the most appropriate antidote?",
                "Replenishes hepatic glutathione to detoxify NAPQI", ["Inhibits CYP2E1 to block NAPQI formation", "Binds paracetamol in the gut lumen", "Enhances renal excretion of paracetamol", "Competitively blocks paracetamol receptors on hepatocytes"],
                explain='''ระดับยา 160 mg/L ที่ 6 ชม. อยู่ **เหนือ treatment line** (เส้นที่ 6 ชม. ≈ 106 mg/L) → ให้ **N-acetylcysteine** ซึ่ง **เติม glutathione** ไว้จับ NAPQI
- การยับยั้ง CYP2E1 เป็นกลไกของ fomepizole ซึ่งไม่ใช่ antidote มาตรฐาน
- การจับยาในลำไส้คือ activated charcoal (decontamination ไม่ใช่ antidote)
- NAC ไม่ได้เพิ่มการขับทางไต
- Paracetamol ไม่ได้ออกฤทธิ์ผ่าน receptor บนเซลล์ตับ''',
                pearl="NAC = glutathione precursor จับ NAPQI", topic="NAC mechanism",
                ref=[f"{D} หน้า 169, 171"], nl=["B1.7.6", "2.3.18(7)"]),
            mcq("GI-06-01-4", "A 25-year-old man has dark urine and malaise for 2 days. Two weeks ago he travelled to India, drank tap water and 4 bottles of beer. Five days ago he had fever and myalgia, treated with paracetamol 4 g/day. After the fever subsided he developed dark urine. He is afebrile with icteric sclerae and a smooth, mildly tender liver 2 cm below the costal margin. Albumin 3.4, TB 12, DB 10, AST 6,500, ALT 9,900, ALP 180. According to the slide answer, what is the most likely cause?",
                "Acetaminophen", ["Hepatitis A virus", "Salmonella Typhi", "Entamoeba histolytica", "Alcohol"],
                explain='''เฉลยในสไลด์คือ **acetaminophen** — AST/ALT สูง **หลายพัน** (> 5,000) เข้าได้กับ paracetamol hepatotoxicity มากที่สุด ร่วมกับมีปัจจัยเสี่ยงคือดื่มแอลกอฮอล์และกินยา 4 g/วันขณะเจ็บป่วย/เบื่ออาหาร (glutathione ต่ำ)
- Hepatitis A เป็นคู่แข่งสำคัญ (ไปอินเดีย ดื่มน้ำประปา ระยะฟักตัวเข้าได้ ไข้นำแล้วตัวเหลือง) — ควรส่ง anti-HAV IgM ด้วยในชีวิตจริง
- *S.* Typhi ไม่ทำให้ transaminase สูงหลายพัน
- *E. histolytica* ทำให้ liver abscess ไม่ใช่ diffuse hepatitis
- Alcohol: AST:ALT > 2 และ AST มักไม่เกิน 300
> ข้อนี้กำกวม: แนวทางทั่วไปถือว่า 4 g/วันเป็นขนาด therapeutic และภาพทางคลินิกเข้ากับ acute HAV ได้ดี — ถ้าเจอข้อนี้ในสอบ ให้ดูว่าโจทย์เน้นระดับ transaminase (> 5,000 → APAP) หรือ prodrome/ประวัติเดินทาง''',
                pearl="AST/ALT หลายพัน (> 3,000–5,000) → นึกถึง paracetamol, ischemic ก่อน viral", topic="Acetaminophen vs HAV",
                ref=[f"{D} หน้า 176–177"], nl=["2.3.18(7)", "2.3.1(1)"], kind="old", src=OLD),
        ]),

    sec("gi-06-02", "Ischemic hepatitis",
        "หลังช็อก/HF/hypoxemia → AST/ALT > 1,000 พุ่งเร็วลงเร็ว + ไตเสียร่วม · รักษา hemodynamic", minutes=4,
        source=f"{D} หน้า 178–182", nl=["2.2.7", "2.3.11-3(7)"],
        md='''
### นิยามและกลไก
**Hypoperfusion → acute hepatic injury** ("shock liver") — zone 3 (centrilobular) ขาดเลือดง่ายที่สุด (เสริม)

### สาเหตุ
- Heart failure, shock → hypoperfusion
- Respiratory failure → hypoxemia

### อาการ
- อ่อนเพลีย ซึม (AOC) จากโรคพื้นฐาน
- **↓BP, ↑PR**
- มี end-organ hypoperfusion อื่นร่วม (ไต, สมอง)

### Lab
- **↑AST, ↑↑ALT > 1,000** (มักขึ้นเร็วภายใน 1–3 วันหลังช็อก และลดลงเร็วเมื่อ hemodynamic ดีขึ้น — เสริม), ↑TB
- **↑BUN, ↑Cr** (AKI ร่วม)
- LDH สูงมาก (ALT/LDH < 1.5 — เสริม)

### การรักษา
**Hemodynamic support และรักษาสาเหตุ** — ไม่มียาเฉพาะ

> โจทย์: ผู้ป่วย ICU septic shock/HF/AF ที่ BP ต่ำ แล้ว transaminase พุ่งหลักพัน → **ischemic hepatitis** ไม่ใช่ drug-induced (แม้ได้ยาหลายตัว)
''',
        pearls=[
            "Shock/HF/hypoxemia + AST/ALT > 1,000 = ischemic hepatitis",
            "ขึ้นเร็ว ลงเร็ว มักมี AKI ร่วม",
            "Tx: แก้ hemodynamic และสาเหตุ",
        ],
        items=[
            mcq("GI-06-02-1", "A 73-year-old man with COPD, CAD and hypertension is admitted to the ICU with septic shock from pneumonia and treated with fluids, vasopressors and IV antibiotics. On day 2: ALT 2,000 U/L, AST 1,500 U/L, ALP 120 U/L, TB 3.9 mg/dL, DB 2.2 mg/dL. What is the most likely diagnosis?",
                "Ischemic hepatitis", ["Hepatitis A", "Drug-induced hepatitis", "Autoimmune hepatitis", "Alcoholic hepatitis"],
                explain='''Transaminase พุ่งหลักพันทันทีหลัง **septic shock** ที่ต้องใช้ vasopressor = **ischemic hepatitis** (hypoperfusion)
- Hepatitis A ไม่มีปัจจัยเสี่ยงและไม่สัมพันธ์กับเวลาช็อก
- Drug-induced hepatitis จาก ATB มักใช้เวลาหลายวัน–สัปดาห์ และระดับไม่พุ่งเร็วแบบนี้
- Autoimmune hepatitis เป็นภาวะเรื้อรังในหญิง มี IgG สูง
- Alcoholic hepatitis มี AST:ALT > 2 และ AST < 300''',
                pearl="ICU shock + transaminase หลักพัน = ischemic hepatitis", topic="Ischemic hepatitis",
                ref=[f"{D} หน้า 179–180"], nl=["2.2.7", "2.3.11-3(7)"], kind="old", src=OLD),
            mcq("GI-06-02-2", "A 55-year-old woman with SLE, dyslipidemia and chronic atrial fibrillation (on hydroxychloroquine, simvastatin and warfarin) presents with severe watery diarrhea. Pulse 115/min, BP 90/60 mmHg. Mild icteric sclerae. AST 3,000 U/L, ALT 3,000 U/L, TB 6 mg/dL, DB 3 mg/dL. What is the most likely cause of the transaminitis?",
                "Acute ischemic hepatitis", ["Acute viral hepatitis", "Autoimmune hepatitis", "Drug-induced transaminitis from simvastatin", "Hydroxychloroquine toxicity"],
                explain='''ท้องเสียรุนแรง → **hypovolemia (BP 90/60, HR 115)** ร่วมกับโรคหัวใจ (AF) → ตับขาดเลือด → AST/ALT พุ่งถึง 3,000 = **ischemic hepatitis**
- Acute viral hepatitis ไม่มีประวัติเสี่ยงและไม่อธิบายช็อก
- Autoimmune hepatitis สัมพันธ์กับโรคภูมิคุ้มกันได้ แต่มักไม่ทำให้ transaminase พุ่งเฉียบพลันพร้อมช็อก
- Simvastatin ทำให้ transaminase สูงเล็กน้อยได้ แต่ไม่ถึงหลักพัน และใช้มานานแล้ว
- Hydroxychloroquine แทบไม่ทำให้ตับอักเสบ''',
                pearl="ช็อกจากสาเหตุใดก็ได้ (รวม hypovolemia จากท้องเสีย) → ischemic hepatitis", topic="Ischemic hepatitis clinical",
                ref=[f"{D} หน้า 181–182"], nl=["2.2.7"], kind="old", src=OLD),
        ]),

    sec("gi-06-03", "Alcohol-related liver disease",
        "Steatosis → steatohepatitis (AST:ALT > 2, AST < 300, GGT สูง) → cirrhosis · หยุดเหล้า · steroid ถ้า severe", minutes=6,
        source=f"{D} หน้า 183–197", nl=["2.3.11(2)", "B8.2.5(3)"],
        md='''
### สามระยะของโรค
[[fig:gi-06-03-ald]]

**1. Alcoholic steatosis**
- Fatty liver ไม่มีการอักเสบ
- ไม่มีอาการ ± ตับโต
- **หยุดเหล้า → กลับคืนได้**

**2. Alcoholic steatohepatitis (alcoholic hepatitis)**
- Fatty liver + inflammation + fibrosis
- **ตัวเหลืองเฉียบพลัน ไข้** อ่อนเพลีย คลื่นไส้ เบื่ออาหาร
- **Tender hepatomegaly**
- Lab: **↑↑AST / ↑ALT > 2** (**AST มักไม่เกิน 300**), **↑GGT**
- U/S: steatosis, hepatomegaly
- Mx: **หยุดเหล้า** (กลับคืนได้), **nutritional therapy**, **steroid ถ้า severe** (เช่น Maddrey DF ≥ 32 — เสริม)

**3. Alcohol-associated cirrhosis**
- Fibrosis มาก
- ระยะแรกไม่มีอาการ ระยะหลังมี signs of CLD, decompensated cirrhosis (variceal bleeding, ascites, encephalopathy, jaundice)
- Mx: หยุดเหล้า (**กลับคืนไม่ได้**), nutrition, steroid ถ้า severe AH ซ้อน; **definitive tx: liver transplant**

### ทำไม AST > ALT ใน alcohol
- Alcohol ทำให้ขาด **pyridoxal 5'-phosphate (vit B6)** ซึ่ง ALT ต้องใช้มากกว่า AST + mitochondrial injury ปล่อย AST (เสริม)

### GGT — marker ว่ายังดื่มอยู่
- GGT ถูก induce โดยแอลกอฮอล์ ถ้าหยุดดื่มจริง **GGT จะลดลง** → ใช้ติดตามว่าผู้ป่วยยังดื่มอยู่หรือไม่

### โจทย์ในสไลด์
| ข้อมูล | คำตอบ |
|---|---|
| ดื่มหนัก parotid โต ตับแข็ง AST 110 ALT 45 HBsAg/anti-HCV ลบ | ALD → R/O สาเหตุอื่น, หยุดเหล้า, nutrition |
| Alcohol use disorder + RUQ pain + ตับโต AST 315 ALT 152 | Alcoholic hepatitis |
| วิสกี้วันละขวด ไข้ RUQ pain ตัวเหลือง AST 800 ALT 400 | Alcoholic hepatitis |
| ไข้ 2 สัปดาห์ ตัวเหลือง AST 300 ALT 150 GGT 200 | Alcoholic hepatitis |
| ตรวจสุขภาพ AST 270 ALT 137 | Alcoholic hepatitis (AST:ALT ~2:1) |
| Lab บอกว่ายังดื่มอยู่ | **GGT** |

> เกณฑ์ "AST < 300" เป็น clue คลาสสิก แต่โจทย์ในสไลด์บางข้อ AST 800 ก็ยังเฉลย alcoholic hepatitis เพราะสัดส่วน 2:1 และประวัติชัด
''',
        figs=[fig("gi-06-03-ald", "สเปกตรัม alcohol-related liver disease", ALD,
                  "สองระยะแรกกลับคืนได้เมื่อหยุดดื่ม ส่วน cirrhosis กลับคืนไม่ได้และต้องพิจารณาปลูกถ่ายตับ")],
        pearls=[
            "Alcoholic hepatitis: AST:ALT > 2, AST มัก < 300, GGT สูง",
            "Steatosis และ steatohepatitis กลับคืนได้เมื่อหยุดเหล้า; cirrhosis ไม่กลับคืน",
            "GGT ลดลงเมื่อหยุดดื่ม → ใช้ติดตาม",
            "Severe alcoholic hepatitis → steroid; definitive tx ของ cirrhosis = transplant",
        ],
        items=[
            mcq("GI-06-03-1", "A 45-year-old man has drunk a bottle of whiskey daily for 15 years. He presents with fever and right upper quadrant pain. He has moderate jaundice and mild tender hepatomegaly. AST 280 U/L, ALT 110 U/L, GGT 420 U/L. What is the most likely diagnosis?",
                "Alcoholic hepatitis", ["Acute pancreatitis", "Acute viral hepatitis", "Acute cholecystitis", "Pyogenic liver abscess"],
                explain='''ดื่มหนักเรื้อรัง + ไข้ ตัวเหลือง ตับโตกดเจ็บ + **AST:ALT > 2, AST < 300, GGT สูงมาก** = alcoholic hepatitis
- Acute pancreatitis ปวดลิ้นปี่ร้าวหลัง ไม่ได้ตัวเหลืองตับโตแบบนี้
- Acute viral hepatitis มี ALT > AST และมักหลักพัน
- Acute cholecystitis มี Murphy sign ไม่ได้ทำให้ transaminase แบบ AST เด่น
- Pyogenic liver abscess จะเห็นก้อนใน U/S และมี ALP สูงเด่น''',
                pearl="AST:ALT > 2 + AST < 300 + GGT สูง + ดื่มหนัก = alcoholic hepatitis", topic="Alcoholic hepatitis",
                ref=[f"{D} หน้า 184, 190–191"], nl=["2.3.11(2)"]),
            mcq("GI-06-03-2", "A 44-year-old man with alcohol use disorder and previous admissions for acute pancreatitis has abdominal pain that has worsened over a few days. He has right upper quadrant tenderness and hepatomegaly. AST 315 U/L, ALT 152 U/L. Lipase is normal. What is the most likely diagnosis?",
                "Alcoholic hepatitis", ["Acute pancreatitis", "Cholecystitis", "Viral hepatitis", "Non-alcoholic fatty liver disease"],
                explain='''Alcohol use disorder + ปวด RUQ ตับโต + **AST:ALT ≈ 2:1** ที่ระดับไม่กี่ร้อย = alcoholic hepatitis
- Acute pancreatitis เป็นตัวลวงจากประวัติเดิม แต่ lipase ปกติและปวดที่ RUQ กับตับโต
- Cholecystitis มีไข้ Murphy sign และ U/S เห็นถุงน้ำดีอักเสบ
- Viral hepatitis มี ALT > AST
- NAFLD ต้อง exclude alcohol และมักมี ALT > AST ไม่มีอาการ''',
                pearl="AST/ALT ~2:1 ในคนติดเหล้า = alcoholic hepatitis", topic="Alcoholic hepatitis vs pancreatitis",
                ref=[f"{D} หน้า 188–189"], nl=["2.3.11(2)"], kind="old", src=OLD),
            mcq("GI-06-03-3", "A 45-year-old man with alcoholic liver disease was advised to stop drinking. At follow-up he claims abstinence. Which laboratory test best indicates that he is still drinking?",
                "GGT", ["Albumin", "ALP", "ALT", "AST"],
                explain='''**GGT** ถูก induce โดยแอลกอฮอล์และลดลงเมื่อหยุดดื่มจริง จึงใช้ติดตาม abstinence ได้ดีที่สุดในตัวเลือก
- Albumin สะท้อน synthetic function ใช้เวลานานและได้รับผลจากภาวะโภชนาการ
- ALP สะท้อน cholestasis/กระดูก
- ALT และ AST สะท้อน hepatocyte injury ซึ่งอาจปกติได้แม้ยังดื่ม และไม่จำเพาะกับแอลกอฮอล์''',
                pearl="ติดตามว่ายังดื่มอยู่ → GGT", topic="GGT in ALD",
                ref=[f"{D} หน้า 184, 196–197"], nl=["2.3.11(2)", "B8.2.5(3)"], kind="old", src=OLD),
            mcq("GI-06-03-4", "A previously healthy 55-year-old man attends a health check-up. He admits to drinking daily. The liver is palpable with a span of 11 cm. Albumin 3.5 g/dL, total bilirubin 0.8 mg/dL, AST 270 U/L, ALT 137 U/L. HBsAg and anti-HCV are negative. Which is the most important treatment?",
                "Cessation of alcohol", ["Prednisolone 40 mg/day", "Ursodeoxycholic acid", "Tenofovir", "Liver transplantation"],
                explain='''AST:ALT ≈ 2:1 AST < 300 ในคนดื่มประจำ ไม่มีตัวเหลือง bilirubin ปกติ = alcoholic liver disease ระยะที่ยังกลับคืนได้ → การรักษาที่สำคัญที่สุดคือ **หยุดเหล้า** ร่วมกับ nutritional therapy
- Prednisolone ใช้เฉพาะ severe alcoholic hepatitis (ตัวเหลือง coagulopathy)
- Ursodeoxycholic acid ใช้ใน PBC/cholestasis
- Tenofovir เป็นยาต้าน HBV ซึ่งผลลบ
- Liver transplant สำหรับ decompensated cirrhosis ที่หยุดดื่มแล้ว''',
                pearl="ALD ทุกระยะ: หยุดเหล้าสำคัญที่สุด", topic="ALD management",
                ref=[f"{D} หน้า 183–187, 194–195"], nl=["2.3.11(2)"], kind="old", src=OLD),
        ]),

    sec("gi-06-04", "Fatty liver disease (MASLD/MASH)",
        "Fatty liver + metabolic risk, exclude alcohol · ALT > AST · U/S echogenicity สูง · ลดน้ำหนัก + คุม DM/DLP", minutes=5,
        source=f"{D} หน้า 198–203", nl=["2.3.4(6)", "2.3.4(7)"],
        md='''
### ชื่อใหม่
| ชื่อใหม่ | ชื่อเดิม | ความหมาย |
|---|---|---|
| **MASLD** — metabolic dysfunction-associated steatotic liver disease | NAFLD | ไขมันพอกตับในคนที่มี metabolic syndrome/risk (exclude สาเหตุอื่นเช่น alcohol) |
| **MASH** — metabolic dysfunction-associated steatohepatitis | NASH | **subset** ของ MASLD ที่มี hepatocellular inflammation และ damage เรื้อรัง |

### ใครเสี่ยง
**Obesity, DM, dyslipidemia, hypertriglyceridemia** (metabolic syndrome — waist circumference, BP, FBS, TG, HDL)

### การวินิจฉัย
- Lab: **↑AST, ↑↑ALT** (ALT > AST — กลับกับ alcohol)
- **U/S: ↑echogenicity** (bright liver เทียบกับ cortex ไต)
- **ต้อง R/O สาเหตุอื่น**: viral (HBsAg, anti-HCV), alcohol, ยา
- ประเมิน fibrosis: FIB-4, transient elastography (CAP วัดไขมัน) (เสริมจากสไลด์ตาราง cirrhosis)

### การรักษา
- **Low-fat diet, weight loss** (ลด 7–10% ทำให้ MASH ดีขึ้น — เสริม)
- **คุม DM, DLP**

| ลักษณะ | MASLD/MASH | Alcoholic hepatitis |
|---|---|---|
| AST:ALT | < 1 (ALT เด่น) | > 2 |
| ประวัติ | อ้วน DM DLP | ดื่มหนัก |
| GGT | สูงได้เล็กน้อย | สูงมาก |

> โจทย์: AST/ALT สูง 2–3 เท่าหลายปี ไม่มีอาการ BMI สูง TG สูง FBS/HbA1c สูง HBsAg/anti-HCV ลบ ปฏิเสธเหล้า → **fatty liver (MASLD/MASH)**; ถ้า transaminase สูงต่อเนื่องตอบ **steatohepatitis (MASH)** มากกว่า simple steatosis
''',
        pearls=[
            "MASLD = NAFLD เดิม; MASH = NASH เดิม (มีอักเสบ)",
            "Fatty liver: ALT > AST, U/S bright liver, metabolic risk, exclude alcohol/viral/drug",
            "Tx: ลดน้ำหนัก low-fat diet คุม DM/DLP",
            "ALT สูงต่อเนื่อง + metabolic syndrome = MASH (ไม่ใช่ simple steatosis)",
        ],
        items=[
            mcq("GI-06-04-1", "A 46-year-old woman is asymptomatic. She drinks alcohol occasionally (about once a month). BMI 26 kg/m², waist circumference 92 cm, BP 125/85 mmHg. Examination is normal. FBS 120 mg/dL, AST 105 U/L, ALT 200 U/L. HBsAg and anti-HCV are negative. What is the most likely cause of her elevated liver enzymes?",
                "Non-alcoholic steatohepatitis", ["Chronic viral hepatitis", "Alcoholic fatty liver disease", "Autoimmune hepatitis", "Simple non-alcoholic steatosis"],
                explain='''มี metabolic syndrome (waist 92 cm, FBS 120, BP 125/85) ดื่มเหล้าเพียงครั้งคราว และ **ALT > AST สูงหลายเท่า** → ไขมันพอกตับที่ **มีการอักเสบ** = NASH (MASH)
- Chronic viral hepatitis ผลตรวจ HBsAg/anti-HCV ลบ
- Alcoholic fatty liver ต้องดื่มหนักและ AST > ALT
- Autoimmune hepatitis ต้องมี IgG สูง ANA/SMA บวก
- Simple steatosis มักมี enzyme ปกติหรือสูงเล็กน้อย — ALT 200 บ่งชี้การอักเสบ''',
                pearl="Metabolic syndrome + ALT > AST สูง = MASH", topic="MASH",
                ref=[f"{D} หน้า 202–203"], nl=["2.3.4(6)"], kind="old", src=OLD),
            mcq("GI-06-04-2", "A 48-year-old man has had AST and ALT about 3 times normal for several years. He is asymptomatic and denies alcohol, medicines and herbs. BMI 31 kg/m². AST 110 U/L, ALT 135 U/L, albumin 4 g/dL. HBsAg and anti-HCV negative. TG 405 mg/dL, FBS 168 mg/dL, HbA1c 7%. Ultrasound shows increased hepatic echogenicity. Which is the most appropriate management?",
                "Weight loss with a low-fat diet and control of diabetes and dyslipidemia", ["Prednisolone", "Penicillamine", "Ursodeoxycholic acid as the main therapy", "Liver biopsy before any lifestyle advice"],
                explain='''Fatty liver disease (MASLD/MASH) ในคนอ้วน DM TG สูง หลังตัดสาเหตุ viral/alcohol/drug ออกแล้ว → การรักษาหลักคือ **ลดน้ำหนัก low-fat diet และคุม DM, DLP**
- Prednisolone ใช้ใน autoimmune/severe alcoholic hepatitis
- Penicillamine เป็น chelator ของ Wilson disease
- Ursodeoxycholic acid ไม่ได้ผลชัดเจนใน MASLD
- Liver biopsy ไม่จำเป็นก่อนเริ่มปรับพฤติกรรม ใช้ non-invasive fibrosis test ก่อน''',
                pearl="MASLD tx = ลดน้ำหนัก + คุม metabolic risk", topic="MASLD management",
                ref=[f"{D} หน้า 199–201"], nl=["2.3.4(6)", "2.3.4(7)"], kind="old", src=OLD),
            mcq("GI-06-04-3", "A 35-year-old man who drinks heavily is found to have intermittently elevated liver enzymes on check-ups. He is asymptomatic. Parotid glands are enlarged and the liver is firm with a 13-cm span. AST 110 U/L, ALT 45 U/L, ALP 95 U/L. HBsAg and anti-HCV negative. TG 505 mg/dL, FBS 98 mg/dL, HbA1c 5.5%. What is the most likely diagnosis?",
                "Alcoholic liver disease", ["Non-alcoholic fatty liver disease", "Chronic hepatitis C", "Wilson disease", "Hemochromatosis"],
                explain='''ดื่มหนัก + parotid gland enlargement + **AST:ALT > 2** (110:45) → alcoholic liver disease (TG สูงก็เกิดจากแอลกอฮอล์ได้) น้ำตาลปกติ
- NAFLD ต้อง exclude alcohol และมี ALT เด่น
- Chronic HCV ผล anti-HCV ลบ
- Wilson disease พบในคนอายุน้อยกว่าร่วมกับอาการทางระบบประสาท/KF ring
- Hemochromatosis มี ferritin/transferrin saturation สูง ผิวคล้ำ DM''',
                pearl="ดื่มหนัก + AST:ALT > 2 → ALD แม้ TG สูง", topic="ALD vs NAFLD",
                ref=[f"{D} หน้า 186–187"], nl=["2.3.11(2)"], kind="old", src=OLD),
        ]),

    sec("gi-06-05", "Wilson disease",
        "AR ทองแดงสะสม: ตับ + สมอง (parkinsonism/tremor) + KF ring · ↓ceruloplasmin ↑urine Cu · chelator, zinc", minutes=4,
        source=f"{D} หน้า 204–206, 230", nl=["2.1.24", "2.3.6-3(8)", "2.3.11-3(7)"],
        md='''
### นิยาม
**Autosomal recessive** (ATP7B gene) → ทองแดงขับออกทางน้ำดีไม่ได้ → **สะสม** ในตับ สมอง ตา

[[fig:gi-06-05-wil]]

### อาการ
- **ตับ**: hepatosplenomegaly, ตัวเหลือง, cirrhosis (หรือ acute liver failure + hemolysis — เสริม)
- **สมอง**: dysarthria, abnormal gait, **parkinsonism, tremor**, dementia, hallucination (psychiatric)
- **ตา**: **Kayser-Fleischer ring** = ทองแดงสะสมที่ขอบ cornea (สีน้ำตาลเหลือง/เขียวที่ limbus) ตรวจด้วย slit lamp

> คิดถึง Wilson ใน **คนอายุน้อย** ที่มีโรคตับร่วมกับอาการทางระบบประสาท/จิตเวช หรือประวัติครอบครัวเป็นโรคตับตั้งแต่อายุน้อย

### Lab
- ↑↑AST > ↑ALT, ↑TB
- **↓Serum ceruloplasmin** (< 20 mg/dL)
- ↓Total serum copper, **↑free serum copper**
- **↑24-hr urine copper** (> 100 mcg/24 ชม.)
- ยืนยัน: ATP7B genetic test, hepatic copper content > 250 mcg/g dry weight

### การรักษา
- จำกัดอาหารที่มีทองแดงสูง (ตับสัตว์ หอย ถั่ว ช็อกโกแลต — เสริม)
- **Chelating agent** (D-penicillamine, trientine)
- **Zinc salts** (ลดการดูดซึมทองแดงในลำไส้)
- Liver transplant ใน fulminant (เสริม)

| ภาวะ | ตัวเหลืองแบบ | ลักษณะ |
|---|---|---|
| Wilson | hepatocellular ร่วมอาการทางระบบประสาท | KF ring, ceruloplasmin ต่ำ |
| Gilbert | unconjugated เป็น ๆ หาย ๆ | ไม่มีอาการอื่น |
| Crigler-Najjar | unconjugated รุนแรงตั้งแต่ทารก | kernicterus |
| Dubin-Johnson | conjugated | ตับสีดำ ไม่มีอาการ |
''',
        figs=[fig("gi-06-05-wil", "Wilson disease: อวัยวะที่ทองแดงสะสมและ lab", WILSON,
                  "ทองแดงสะสมสามที่หลัก — ตับ สมอง ตา — ยืนยันด้วย ceruloplasmin ต่ำและ urine copper สูง")],
        pearls=[
            "Wilson = AR ทองแดงสะสม: ตับ + parkinsonism/tremor/psychiatric + KF ring",
            "↓ceruloplasmin (< 20), ↑free Cu, ↑24-hr urine Cu (> 100 mcg)",
            "Tx: copper restriction + chelator (penicillamine/trientine) + zinc",
            "คนอายุน้อย โรคตับ + อาการทางระบบประสาท → นึกถึง Wilson",
        ],
        items=[
            mcq("GI-06-05-1", "A 20-year-old man has progressive jaundice, pruritus and tremor of both hands for 3 months. Examination shows a brownish-yellow ring at the corneal limbus and rigidity on flexion and extension of the limbs. What is the most likely diagnosis?",
                "Wilson disease", ["Crigler-Najjar syndrome", "Gilbert syndrome", "Dubin-Johnson syndrome", "Cholangiocarcinoma"],
                explain='''คนอายุน้อย + โรคตับ (ตัวเหลือง) + **อาการทางระบบประสาท (tremor, rigidity)** + **Kayser-Fleischer ring** = Wilson disease
- Crigler-Najjar เป็น unconjugated hyperbilirubinemia รุนแรงตั้งแต่ทารก
- Gilbert syndrome ไม่มีอาการอื่นนอกจากตัวเหลืองเล็กน้อยเป็นครั้งคราว
- Dubin-Johnson เป็น conjugated hyperbilirubinemia ไม่มีอาการทางระบบประสาท
- Cholangiocarcinoma ทำให้ obstructive jaundice ในผู้สูงอายุ ไม่มี KF ring''',
                pearl="ตับ + tremor/rigidity + KF ring = Wilson", topic="Wilson diagnosis",
                ref=[f"{D} หน้า 204–206"], nl=["2.1.24", "2.3.6-3(8)"], kind="old", src=OLD),
            mcq("GI-06-05-2", "A 17-year-old girl has new behavioral changes, slurred speech and mild hepatomegaly. AST 140 U/L, ALT 90 U/L. Hepatitis serologies are negative. Which test is the most appropriate initial screening test for the suspected diagnosis?",
                "Serum ceruloplasmin", ["Serum ferritin and transferrin saturation", "Alpha-1 antitrypsin level", "Antimitochondrial antibody", "Serum ammonia"],
                explain='''วัยรุ่นที่มีอาการทางจิตเวช/ระบบประสาท (พฤติกรรมเปลี่ยน พูดไม่ชัด) ร่วมกับโรคตับ → สงสัย Wilson disease ส่ง **serum ceruloplasmin** (ต่ำ < 20 mg/dL) ร่วมกับ 24-hr urine copper และ slit lamp หา KF ring
- Ferritin/transferrin saturation ใช้คัดกรอง hemochromatosis (ผู้ใหญ่ ผิวคล้ำ DM)
- Alpha-1 antitrypsin ใช้เมื่อมีโรคตับร่วมกับ emphysema อายุน้อย
- AMA ใช้วินิจฉัย PBC (หญิงวัยกลางคน คันตัว cholestasis)
- Serum ammonia ใช้สนับสนุน hepatic encephalopathy แต่ไม่บอกสาเหตุ''',
                pearl="สงสัย Wilson → ceruloplasmin + 24-hr urine Cu + slit lamp", topic="Wilson workup",
                ref=[f"{D} หน้า 204, 230"], nl=["2.3.6-3(8)", "2.3.11-3(7)"]),
        ]),
    ])
