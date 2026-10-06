from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-GI"
OLD = "ตัวอย่างข้อสอบในสไลด์ NL2-GI"

# AST/ALT range bars (สไลด์หน้า 124) x: 0 U/L -> 170, 1000 -> 690 (0.52 px/U)
def bar(y, label, x0, x1, cls, arrow=False, note=""):
    X0 = 170 + x0 * 0.52
    X1 = 170 + x1 * 0.52
    s = f'<text x="160" y="{y+13}" text-anchor="end">{label}</text><rect x="{X0:.0f}" y="{y}" width="{X1-X0:.0f}" height="18" rx="4" class="{cls}"/>'
    if arrow:
        s += f'<path d="M{X1:.0f} {y-3}L{X1+14:.0f} {y+9}L{X1:.0f} {y+21}z" class="{cls.replace("soft","")}"/>'
    if note:
        s += f'<text x="{X1+8:.0f}" y="{y+13}" class="t3">{note}</text>'
    return s

ROWS = [("ปกติ", 0, 40, "oksoft", False, "&lt; 30–40"),
        ("Chronic viral hepatitis", 10, 280, "c1soft", False, ""),
        ("Steatohepatitis (MASH)", 10, 280, "c1soft", False, ""),
        ("Alcoholic hepatitis", 20, 600, "misssoft", False, "AST มัก &lt; 300–500"),
        ("Drug toxicity", 20, 1000, "c2soft", True, ""),
        ("Acute viral hepatitis", 140, 1000, "badsoft", True, ""),
        ("Ischemic hepatitis", 220, 1000, "badsoft", True, ""),
        ("Paracetamol overdose", 260, 1000, "badsoft", True, "")]
LFT = '<svg viewBox="0 0 740 330">' + "".join(bar(20 + i * 32, *r) for i, r in enumerate(ROWS)) + \
    '<path d="M170 282H700" class="ln"/>' + \
    "".join(f'<path d="M{170+v*0.52:.0f} 282V288" class="ln"/><text x="{170+v*0.52:.0f}" y="302" text-anchor="middle" class="t3">{v}</text>' for v in range(0, 1001, 200)) + \
    '<path d="M430 14V276" class="lnf"/><text x="436" y="12" class="t3">500</text>' + \
    '<text x="435" y="322" text-anchor="middle" class="tb">ช่วง AST/ALT ที่พบบ่อย (U/L)</text></svg>'

# HBV acute resolved serology. x: week 0 -> 80, week 48 -> 700 (12.92 px/wk); y: 250 baseline
HBV = '''<svg viewBox="0 0 740 380">
 <defs><marker id="gi-05-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="390" y="30" width="78" height="220" class="sunk"/>
 <text x="429" y="48" text-anchor="middle" class="t3">window</text>
 <text x="429" y="62" text-anchor="middle" class="t3">period</text>
 <rect x="170" y="30" width="155" height="16" rx="4" class="misssoft"/>
 <text x="247" y="42" text-anchor="middle" class="t3">อาการ + ALT สูง</text>
 <path d="M70 250H712" class="ln" marker-end="url(#gi-05-03-a)"/>
 <path d="M70 250V24" class="ln" marker-end="url(#gi-05-03-a)"/>
 <text x="60" y="30" text-anchor="end" class="t3">ระดับ</text>
 <g class="t3">
  <text x="80" y="268" text-anchor="middle">0</text><text x="183" y="268" text-anchor="middle">8</text>
  <text x="286" y="268" text-anchor="middle">16</text><text x="390" y="268" text-anchor="middle">24</text>
  <text x="493" y="268" text-anchor="middle">32</text><text x="596" y="268" text-anchor="middle">40</text>
  <text x="700" y="268" text-anchor="middle">48</text>
 </g>
 <text x="390" y="290" text-anchor="middle" class="tb">สัปดาห์หลังติดเชื้อ</text>
 <path d="M110 250C150 248 165 90 215 90C265 90 300 220 390 248" class="lnbad"/>
 <path d="M150 250C175 248 200 70 245 70C300 70 360 210 493 246" class="lnc2"/>
 <path d="M150 250C175 248 200 70 245 70C300 70 340 110 420 104C520 98 620 104 700 104" class="lnf"/>
 <path d="M440 250C470 248 500 130 560 128C620 126 660 126 700 126" class="lnok"/>
 <rect x="490" y="306" width="230" height="66" rx="8" class="box"/>
 <path d="M502 320H530" class="lnbad"/><text x="538" y="324" class="t3">HBsAg</text>
 <path d="M610 320H638" class="lnc2"/><text x="646" y="324" class="t3">anti-HBc IgM</text>
 <path d="M502 344H530" class="lnf"/><text x="538" y="348" class="t3">anti-HBc total (IgG)</text>
 <path d="M502 364H530" class="lnok"/><text x="538" y="368" class="t3">anti-HBs</text>
 <text x="200" y="84" class="t3">HBsAg</text>
 <text x="252" y="64" class="t3">anti-HBc IgM</text>
 <text x="512" y="92" class="t3">anti-HBc IgG ค้างตลอดชีวิต</text>
 <text x="600" y="148" class="t3">anti-HBs = immune</text>
 <text x="80" y="306" class="t3">Window: HBsAg หายแล้ว anti-HBs ยังไม่ขึ้น</text>
 <text x="80" y="324" class="t3">→ anti-HBc IgM เป็นตัวเดียวที่บอก acute HBV</text>
</svg>'''

NH = '''<svg viewBox="0 0 720 300">
 <defs><marker id="gi-05-04-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <text x="120" y="20" text-anchor="middle" class="ta">HAV / HEV</text>
 <text x="360" y="20" text-anchor="middle" class="ta">HBV (ผู้ใหญ่)</text>
 <text x="600" y="20" text-anchor="middle" class="ta">HCV</text>
 <rect x="30" y="32" width="180" height="40" rx="8" class="misssoft"/>
 <text x="120" y="57" text-anchor="middle" class="tb">Acute (มีอาการ)</text>
 <path d="M120 72V96" class="ln" marker-end="url(#gi-05-04-a)"/>
 <rect x="30" y="98" width="180" height="48" rx="8" class="oksoft"/>
 <text x="120" y="118" text-anchor="middle" class="tb">หายเอง</text>
 <text x="120" y="136" text-anchor="middle" class="t3">anti-HAV IgG = immune</text>
 <text x="120" y="172" text-anchor="middle" class="t3">ไม่เป็น chronic</text>
 <text x="120" y="190" text-anchor="middle" class="t3">ส่วนน้อย fulminant → death</text>
 <text x="120" y="208" text-anchor="middle" class="t3">HEV รุนแรงในหญิงตั้งครรภ์</text>
 <rect x="270" y="32" width="180" height="48" rx="8" class="misssoft"/>
 <text x="360" y="52" text-anchor="middle" class="tb">Acute HBV</text>
 <text x="360" y="70" text-anchor="middle" class="t3">ส่วนใหญ่หาย → anti-HBs</text>
 <path d="M360 80V96" class="ln" marker-end="url(#gi-05-04-a)"/>
 <rect x="270" y="98" width="180" height="40" rx="8" class="c1soft"/>
 <text x="360" y="123" text-anchor="middle" class="tb">Chronic HBV (ส่วนน้อย)</text>
 <path d="M360 138V162" class="ln" marker-end="url(#gi-05-04-a)"/>
 <rect x="270" y="164" width="180" height="36" rx="8" class="badsoft"/>
 <text x="360" y="187" text-anchor="middle" class="tb">Cirrhosis</text>
 <path d="M360 200V224" class="ln" marker-end="url(#gi-05-04-a)"/>
 <rect x="270" y="226" width="180" height="36" rx="8" class="bad"/>
 <text x="360" y="249" text-anchor="middle" class="tw">HCC</text>
 <path d="M270 118H248V244H268" class="lnbad" marker-end="url(#gi-05-04-a)"/>
 <text x="244" y="282" text-anchor="middle" class="t3">HBV → HCC ได้โดยไม่ผ่าน cirrhosis</text>
 <rect x="510" y="32" width="180" height="48" rx="8" class="sunk"/>
 <text x="600" y="52" text-anchor="middle" class="tb">Acute HCV</text>
 <text x="600" y="70" text-anchor="middle" class="t3">90% ไม่มีอาการ</text>
 <path d="M600 80V96" class="ln" marker-end="url(#gi-05-04-a)"/>
 <rect x="510" y="98" width="180" height="40" rx="8" class="c2soft"/>
 <text x="600" y="123" text-anchor="middle" class="tb">Chronic HCV (ส่วนใหญ่)</text>
 <path d="M600 138V162" class="ln" marker-end="url(#gi-05-04-a)"/>
 <rect x="510" y="164" width="180" height="36" rx="8" class="badsoft"/>
 <text x="600" y="187" text-anchor="middle" class="tb">Cirrhosis</text>
 <path d="M600 200V224" class="ln" marker-end="url(#gi-05-04-a)"/>
 <rect x="510" y="226" width="180" height="36" rx="8" class="bad"/>
 <text x="600" y="249" text-anchor="middle" class="tw">HCC</text>
 <text x="600" y="282" text-anchor="middle" class="t3">DAA รักษาหายขาด แต่ไม่มีภูมิ</text>
</svg>'''

LECTURE = lecture("05", "LFT & viral hepatitis",
    subtitle="อ่าน LFT · acute vs chronic hepatitis · HAV · HBV · HCV",
    objectives=[
        "แยก pattern LFT เป็น hepatocellular, cholestatic, isolated hyperbilirubinemia และ cirrhosis ได้",
        "ใช้ระดับ AST/ALT และสัดส่วน AST:ALT เดาสาเหตุ (viral, alcohol, ischemic, drug) ได้",
        "สั่งและแปลผล serology ของ HAV, HBV, HCV ได้ถูกต้อง",
        "บอกข้อบ่งชี้ antiviral ใน chronic HBV และการติดตาม/HCC surveillance ได้",
        "บอกการรักษา chronic HCV ด้วย sofosbuvir/velpatasvir และความต่างของ natural history HAV/HBV/HCV",
    ],
    sections=[
    sec("gi-05-01", "LFT interpretation & approach to hepatitis",
        "Hepatocellular vs cholestatic · AST:ALT > 2 = alcohol · > 1000 = viral/drug/ischemic · ALT > AST ใน viral", minutes=6,
        source=f"{D} หน้า 122–128", nl=["2.1.13", "B8.1.2(3)"],
        md='''
### 4 pattern ของ LFT
| Pattern | AST, ALT | ALP, GGT | Bilirubin | Albumin | INR |
|---|---|---|---|---|---|
| Hepatocellular | ↑ ถึง ↑↑↑ | ปกติ ถึง ↑↑ | ปกติ ถึง ↑↑ | ปกติ ถึง ↓↓ | ปกติ ถึง ↑↑ |
| Cholestatic | ปกติ ถึง ↑↑ | **↑ ถึง ↑↑↑** | ↑ ถึง ↑↑↑ | ปกติ | ปกติ |
| Isolated hyperbilirubinemia | ปกติ | ปกติ | ↑ ถึง ↑↑↑ | ปกติ | ปกติ |
| Cirrhosis | ปกติ ถึง ↑ | ปกติ | ↑ ถึง ↑↑↑ | **↓ ถึง ↓↓↓** | **↑ ถึง ↑↑↑** |

### เดาสาเหตุจาก pattern
- **Hepatocellular**
  - **AST:ALT > 2** → alcoholic liver disease
  - **AST, ALT > 1,000** → viral hepatitis, drug (paracetamol), ischemic
- **Cholestatic**
  - ↑ALP + ↑GGT → biliary tract obstruction
  - ↑ALP แต่ **GGT ปกติ** → bone disease (ALP มาจากกระดูก)
- **Isolated hyperbilirubinemia** (unconjugated ↑) → hemolysis, Gilbert, Crigler-Najjar
- **Cirrhosis** → ปลายทางของ hepatocellular/cholestatic disease (albumin ต่ำ INR สูง = synthetic function เสีย)

[[fig:gi-05-01-lft]]

### Acute vs chronic hepatitis — สาเหตุ
| Acute hepatitis | Chronic hepatitis |
|---|---|
| Viral hepatitis A, B, C, D, E; CMV, EBV | Viral hepatitis B, C |
| Alcohol | Fatty liver disease (MASLD, MASH) |
| Drug/toxin-induced | Alcohol-related liver disease |
| Ischemic hepatitis | Autoimmune hepatitis |
| Autoimmune hepatitis | Drug-induced |
| Genetics: Wilson disease | Wilson disease, hemochromatosis |

### Acute hepatitis — อาการ
- นำด้วย **flu-like symptoms**: ไข้ อ่อนเพลีย คลื่นไส้อาเจียน เบื่ออาหาร ปวดหัว
- ตามด้วย **ตัวเหลือง ปวด RUQ (1–2 สัปดาห์หลัง)**
- Tender hepatomegaly

### Acute hepatitis — การตรวจ
- LFT: **ALT มักสูงกว่า AST** (ถ้า AST:ALT > 2 คิดถึง alcoholic hepatitis)
- **Viral hepatitis profile**
  - Acute HAV: **anti-HAV IgM**
  - Acute HBV: **HBsAg, anti-HBc IgM**
  - Acute HCV: anti-HCV + **HCV RNA**
  - Acute HEV: anti-HEV IgM
- Ultrasound (R/O obstruction)
- ซักประวัติ **ยา และการดื่มสุรา** ทุกราย
''',
        figs=[fig("gi-05-01-lft", "ช่วง AST/ALT ตามสาเหตุ", LFT,
                  "แถบสั้นอยู่ซ้ายคือโรคเรื้อรัง (มักไม่เกิน 300) ส่วนแถบที่ยาวทะลุ 1,000 พร้อมลูกศรคือ acute viral, ischemic และ paracetamol (ดัดแปลงจากสไลด์หน้า 124)")],
        pearls=[
            "AST:ALT > 2 = alcohol; AST/ALT > 1,000 = viral, drug (paracetamol), ischemic",
            "ALP สูง + GGT สูง = biliary; ALP สูง + GGT ปกติ = bone",
            "Albumin ต่ำ + INR สูง = synthetic function เสีย (cirrhosis)",
            "Acute viral hepatitis: ALT > AST, flu-like นำแล้วตัวเหลือง",
        ],
        items=[
            mcq("GI-05-01-1", "A 62-year-old woman has bone pain. Laboratory tests show ALP 480 U/L, GGT 30 U/L (normal < 50), AST 22 U/L, ALT 18 U/L and total bilirubin 0.6 mg/dL. Which is the most likely source of the elevated ALP?",
                "Bone", ["Intrahepatic cholestasis", "Extrahepatic biliary obstruction", "Hepatocellular injury", "Hemolysis"],
                explain='''ALP สูงแต่ **GGT ปกติ** → ALP ไม่ได้มาจากตับ/ท่อน้ำดี แต่มาจาก **กระดูก** (เช่น Paget disease, bone metastasis, osteomalacia)
- Intrahepatic cholestasis และ extrahepatic obstruction ต้องมี GGT สูงร่วมด้วย
- Hepatocellular injury จะมี AST/ALT สูงเด่น
- Hemolysis ทำให้ unconjugated bilirubin สูง ไม่ใช่ ALP''',
                pearl="ALP สูง GGT ปกติ = bone", topic="LFT pattern",
                ref=[f"{D} หน้า 123"], nl=["B8.1.2(3)"]),
            mcq("GI-05-01-2", "A 22-year-old man has mild intermittent jaundice during fasting and after febrile illnesses. Total bilirubin 2.8 mg/dL, direct bilirubin 0.3 mg/dL. AST, ALT, ALP, albumin and CBC with reticulocyte count are normal. What is the most likely diagnosis?",
                "Gilbert syndrome", ["Dubin-Johnson syndrome", "Acute viral hepatitis", "Choledocholithiasis", "Autoimmune hemolytic anemia"],
                explain='''**Isolated unconjugated hyperbilirubinemia** ที่เป็น ๆ หาย ๆ เมื่ออดอาหาร/ไม่สบาย โดยไม่มี hemolysis (CBC, retic ปกติ) และ LFT อื่นปกติ = Gilbert syndrome (UGT1A1 ลดลงเล็กน้อย — ไม่ต้องรักษา)
- Dubin-Johnson เป็น **conjugated** hyperbilirubinemia
- Acute viral hepatitis มี AST/ALT สูงมาก
- Choledocholithiasis ทำให้ ALP/GGT และ direct bilirubin สูง
- AIHA ต้องมี anemia และ reticulocyte สูง''',
                pearl="Isolated indirect bilirubin สูง + CBC ปกติ + อดอาหารกำเริบ = Gilbert", topic="Isolated hyperbilirubinemia",
                ref=[f"{D} หน้า 123"], nl=["2.1.13"]),
            mcq("GI-05-01-3", "A 20-year-old woman has jaundice and malaise preceded by 1 week of flu-like symptoms. She denies drugs and alcohol. Temperature 37.2 °C. The liver is palpable and mildly tender. Total bilirubin 4 mg/dL, direct 3.1 mg/dL, albumin 3 g/dL, AST 1,580 U/L, ALT 1,700 U/L, ALP 256 U/L. Which investigation is most appropriate first?",
                "Anti-HAV IgM", ["Total anti-HBc", "Anti-HCV", "Antinuclear antibody", "Ultrasound of the upper abdomen"],
                explain='''Acute hepatitis (AST/ALT > 1,000, ALT > AST) หลัง prodrome แบบ flu-like ในคนอายุน้อยที่ไม่ใช้ยา/ดื่มเหล้า → สาเหตุที่พบบ่อยที่สุดคือ **acute hepatitis A** ส่ง **anti-HAV IgM** (และ HBsAg + anti-HBc IgM สำหรับ acute HBV)
- Total anti-HBc (ไม่ได้ระบุ IgM = IgG) บอกได้แค่เคยติดเชื้อ ไม่บอก acute
- Anti-HCV มักยังลบในระยะ acute และ HCV ไม่ค่อยมีอาการเฉียบพลัน
- ANA ใช้เมื่อสงสัย autoimmune hepatitis หลัง viral profile ลบ
- U/S ช่วย R/O obstruction แต่ pattern เป็น hepatocellular ไม่ใช่ cholestatic''',
                pearl="Acute hepatitis คนอายุน้อย → anti-HAV IgM ± HBsAg/anti-HBc IgM", topic="Acute hepatitis workup",
                ref=[f"{D} หน้า 148–149"], nl=["2.3.1(1)", "B8.3(2)"], kind="old", src=OLD),
        ]),

    sec("gi-05-02", "Viral hepatitis overview & hepatitis A",
        "HAV/HEV fecal-oral ไม่เป็น chronic · anti-HAV IgM = acute · IgG = immune · supportive ไม่ต้อง F/U", minutes=5,
        source=f"{D} หน้า 129–133, 143–153", nl=["2.3.1(1)", "B8.3(2)"],
        md='''
### เปรียบเทียบไวรัสตับอักเสบ
| | HAV | HBV | HCV | HEV |
|---|---|---|---|---|
| การติดต่อ | **Fecal-oral** | Perinatal, blood, sexual | Blood, sexual, perinatal | **Fecal-oral** |
| เป็นเรื้อรัง | **ไม่** | **ได้** | **ได้ (ส่วนใหญ่)** | ไม่ |
| ความรุนแรง | mild | mild | มักไม่มีอาการ | **รุนแรงในหญิงตั้งครรภ์** |
| Acute infection | Anti-HAV IgM | HBsAg, anti-HBc IgM | Anti-HCV + HCV RNA | Anti-HEV IgM |
| ภูมิคุ้มกัน | Anti-HAV IgG | **Anti-HBs** | ไม่มี | — |

> **ข้อควรรู้**: ถ้าโจทย์ **ไม่ระบุว่า IgM** ให้ตีความเป็น **IgG หรือ total** — "anti-HAV positive" = anti-HAV IgG (เคยติดเชื้อ/ได้วัคซีน), "anti-HBc positive" = anti-HBc IgG; anti-HCV ไม่แยก IgM/IgG

[[fig:gi-05-02-nh]]

### Acute hepatitis A
- ติดต่อ fecal-oral (น้ำ/อาหารปนเปื้อน) — ระบาดเป็นกลุ่ม, เดินทางไปประเทศที่สุขาภิบาลไม่ดี
- **Prodrome 1–2 สัปดาห์**: ไข้ อ่อนเพลีย เบื่ออาหาร คลื่นไส้อาเจียน (อาจท้องเสีย)
- ปวด RUQ, tender hepatomegaly แล้วตามด้วย **ตัวเหลือง ปัสสาวะสีเข้ม**
- Lab: ↑AST, **↑↑ALT**, ↑TB; **anti-HAV IgM positive** = active infection
- **Tx: supportive, ไม่ต้อง F/U ระยะยาว**
- หายแล้ว → natural immunity (anti-HAV IgG positive) · **ไม่เป็น chronic** · ส่วนน้อยมากเป็น fulminant hepatitis → death

| Anti-HAV IgM | Anti-HAV IgG | แปลผล |
|---|---|---|
| Positive | Negative | Acute hepatitis A |
| Negative | Positive | Natural immune / vaccinated |

### การป้องกัน
- HAV: hepatitis A vaccine · HBV: hepatitis B vaccine · **HCV: ยังไม่มี vaccine**

> **HAV ไม่ทำให้เกิด cirrhosis** — ข้อสอบถาม "สาเหตุใดไม่ทำให้ตับแข็ง" ตอบ hepatitis A
''',
        figs=[fig("gi-05-02-nh", "Natural history ของ HAV/HEV, HBV และ HCV", NH,
                  "HAV/HEV หายเองไม่เรื้อรัง; HBV ผู้ใหญ่ส่วนใหญ่หายแต่บางรายเรื้อรังและเป็น HCC ได้โดยไม่ผ่าน cirrhosis; HCV ส่วนใหญ่เรื้อรังแต่รักษาหายขาดได้")],
        pearls=[
            "HAV/HEV = fecal-oral ไม่เป็น chronic; HBV/HCV = เลือด/เพศสัมพันธ์/แม่สู่ลูก เป็น chronic ได้",
            "Anti-HAV IgM = acute; ไม่ระบุ IgM = IgG = เคยติด/วัคซีน",
            "Hepatitis A: supportive ไม่ต้อง F/U ระยะยาว",
            "HEV รุนแรงในหญิงตั้งครรภ์",
            "HAV ไม่ทำให้ cirrhosis",
        ],
        items=[
            mcq("GI-05-02-1", "A 16-year-old boy has fever, fatigue and anorexia for 1 week, diarrhea on the first day and jaundice for 3 days. He takes no medications. Icteric sclerae. AST 1,210 U/L, ALT 1,435 U/L, ALP 95 U/L, albumin 3.5 g/dL, total bilirubin 13.5 mg/dL, direct 10 mg/dL. Anti-HAV IgM positive; HBsAg and anti-HBc IgM negative. What is the most appropriate management?",
                "Supportive care without long-term follow-up", ["Oral tenofovir", "Prednisolone", "Liver biopsy", "Follow HBsAg and anti-HBs in 6 months"],
                explain='''**Anti-HAV IgM บวก** = acute hepatitis A ซึ่งหายเองและ **ไม่เป็น chronic** → รักษาแบบประคับประคอง (พัก สารน้ำ หลีกเลี่ยงยาตับ) ไม่ต้องติดตามระยะยาว
- Tenofovir เป็นยาต้าน HBV ไม่มีบทบาทใน HAV
- Prednisolone ใช้ใน autoimmune/severe alcoholic hepatitis
- Liver biopsy ไม่จำเป็นเมื่อวินิจฉัยได้จาก serology
- การตรวจ HBsAg/anti-HBs ที่ 6 เดือนเป็นการติดตาม acute HBV ไม่ใช่ HAV''',
                pearl="Acute HAV: supportive, ไม่ต้อง F/U", topic="Hepatitis A management",
                ref=[f"{D} หน้า 131, 152–153"], nl=["2.3.1(1)"], kind="old", src=OLD),
            mcq("GI-05-02-2", "Which of the following is NOT a cause of liver cirrhosis?",
                "Hepatitis A virus", ["Hepatitis B virus", "Hepatitis C virus", "Non-alcoholic fatty liver disease", "Wilson disease"],
                explain='''**HAV ไม่เป็น chronic infection** จึงไม่ทำให้ตับแข็ง (อาจทำให้ fulminant hepatitis แต่ถ้ารอดก็หายสนิท)
- HBV และ HCV เป็น chronic viral hepatitis → cirrhosis → HCC
- NAFLD/MASH เป็นสาเหตุ cirrhosis ที่เพิ่มขึ้นเรื่อย ๆ
- Wilson disease สะสมทองแดงในตับ → cirrhosis''',
                pearl="HAV/HEV ไม่ทำให้ตับแข็ง", topic="Causes of cirrhosis",
                ref=[f"{D} หน้า 146–147"], nl=["2.3.1(1)", "2.3.11(4)"], kind="old", src=OLD),
            mcq("GI-05-02-3", "A 24-year-old man develops fever, tender hepatomegaly and jaundice. He always uses condoms with his single partner, has no underlying disease and takes no medications. Two weeks before symptoms he ate raw shellfish at a street-food stall. Hb 14 g/dL. What is the most likely diagnosis?",
                "Acute hepatitis A infection", ["Acute hepatitis B infection", "G6PD deficiency with acute hemolysis", "Drug-induced hepatitis", "Chronic hepatitis C"],
                explain='''ไข้ ตับโตกดเจ็บ ตัวเหลือง หลังกินอาหารเสี่ยง (fecal-oral) โดยไม่มีความเสี่ยงทางเลือด/เพศสัมพันธ์ → **acute hepatitis A**
- Acute HBV ติดทางเลือด/เพศสัมพันธ์ ซึ่งผู้ป่วยป้องกันแล้ว
- G6PD hemolysis ทำให้ซีด ตัวเหลือง แต่ไม่มีไข้ ตับโตกดเจ็บ และ Hb ปกติ
- Drug-induced hepatitis ผู้ป่วยปฏิเสธยา
- HCV มักไม่มีอาการเฉียบพลันและไม่มาด้วยไข้ตับโต''',
                pearl="ไข้ ตับโต ตัวเหลือง + ไม่มีความเสี่ยงเลือด/เพศ = HAV", topic="Hepatitis A clinical",
                ref=[f"{D} หน้า 144–145"], nl=["2.3.1(1)"]),
        ]),

    sec("gi-05-03", "Hepatitis B: serology, acute & chronic HBV",
        "HBsAg + anti-HBc IgM = acute · HBsAg > 6 เดือน = chronic · antiviral ตามเกณฑ์ DNA ≥ 2,000 + ALT/fibrosis/อายุ · HCC surveillance", minutes=9,
        source=f"{D} หน้า 134–138, 154–167", nl=["2.3.1-3(3)", "2.3.1(1)", "B8.3(2)"],
        md='''
### Acute hepatitis B
- ติดต่อทาง **เพศสัมพันธ์, parenteral (เลือด/เข็ม), vertical (แม่สู่ลูก)**
- อาการคล้าย hepatitis A
- Lab: ↑AST, ↑↑ALT, ↑TB; **HBsAg positive + anti-HBc IgM positive** = acute infection
- **Tx: supportive**
- **F/U AST, ALT, HBsAg, anti-HBs (± anti-HBc) ที่ 3–6 เดือน** — ดูว่าหายหรือเป็นเรื้อรัง
- หาย → natural immunity (**anti-HBs positive**); มีโอกาสเป็น chronic (ผู้ใหญ่ < 5%, ทารกที่ติดจากแม่ ~90% — เสริม)

[[fig:gi-05-03-sero]]

### แปลผล HBV serology
| HBsAg | Anti-HBc IgM | Anti-HBc IgG | Anti-HBs | แปลผล |
|---|---|---|---|---|
| + | + | − | − | **Acute hepatitis B** |
| + | − | + | − | **Chronic hepatitis B** |
| − | − | + | + | **Natural immune** (เคยติดแล้วหาย) |
| − | − | − | + | **Vaccinated** |
| − | + | ± | − | Window period (เสริม) |

> Anti-HBc เกิดจากการติดเชื้อจริงเท่านั้น — วัคซีนให้แค่ anti-HBs

### Chronic hepatitis B
- มักไม่มีอาการ — เจอจากบริจาคเลือด/ตรวจสุขภาพ
- นิยาม: **HBsAg positive > 6 เดือน**
- **ข้อบ่งชี้ antiviral (ตามสไลด์)**
  1. **Decompensated cirrhosis** (TB > 2 mg/dL, ascites หรือ hepatic encephalopathy) — ให้เลยไม่ว่า viral load เท่าไร
  2. **Compensated cirrhosis + HBV DNA detectable**
  3. **HBV DNA ≥ 2,000 IU/mL ร่วมกับ ≥ 1 ข้อ**: ALT > 1.5 เท่าของค่าปกติ · APRI > 0.5 หรือ FIB-4 > 1.45 · อายุ > 35 ปี
- ยา: **Tenofovir alafenamide (TAF), tenofovir disoproxil fumarate (TDF), entecavir (ETV)**

### ถ้ายังไม่ต้องให้ antiviral
- F/U AST, ALT, platelet ทุก 6–12 เดือน
- ALT > 1.5 เท่า → ตรวจ HBV viral load → ≥ 2,000 IU/mL → antiviral
- ตรวจ co-infection: HIV, HCV
- **HCC surveillance: U/S + AFP ทุก 6–12 เดือน** ถ้า cirrhosis, **ชาย > 40 ปี หรือหญิง > 50 ปี**, หรือ FHx HCC

> HBV เป็น HCC ได้ **โดยไม่ต้องผ่าน cirrhosis** (DNA virus integrate เข้า genome)

### โจทย์ในสไลด์ (สรุปแนวคิด)
| โจทย์ | คำตอบ |
|---|---|
| HBsAg +, anti-HBc IgM +, anti-HAV (IgG) +, anti-HAV IgM − | Acute HBV (anti-HAV IgG = เคยเป็น A) |
| Acute HBV แล้วถามการรักษา | Supportive + F/U 3–6 เดือน |
| "เคยเป็น HBV เมื่อ 6 เดือนก่อน กลัวมะเร็ง" | ตรวจ HBsAg, anti-HBs (± anti-HBc) ว่าหายหรือ chronic ก่อน |
| HBsAg + จากบริจาคเลือด AST/ALT ปกติ แม่และพี่น้องเป็น | Chronic HBV (vertical) → F/U LFT q 6–12 เดือน + ตรวจ HIV/HCV + HCC surveillance |
| AST/ALT สูง 3 เท่าหลายปี HBsAg + HBeAg + | Chronic HBV → ส่ง **HBV DNA** เพื่อดูข้อบ่งชี้ antiviral |
| HBV + ascites (decompensated) | **Antiviral** |
''',
        figs=[fig("gi-05-03-sero", "Serology ของ acute hepatitis B ที่หายเอง", HBV,
                  "HBsAg ขึ้นก่อนแล้วหายภายใน ~6 เดือน ตามด้วย anti-HBs; ช่วง window ที่ทั้งสองตัวลบ anti-HBc IgM เป็นตัวเดียวที่บอก acute infection")],
        pearls=[
            "HBsAg + anti-HBc IgM = acute HBV; HBsAg + anti-HBc IgG = chronic HBV",
            "Anti-HBs + anti-HBc IgG = หายแล้ว; anti-HBs อย่างเดียว = วัคซีน",
            "Chronic HBV = HBsAg > 6 เดือน",
            "Antiviral: decompensated cirrhosis ให้เลย; DNA ≥ 2,000 + (ALT > 1.5×, APRI > 0.5/FIB-4 > 1.45, อายุ > 35)",
            "HCC surveillance U/S + AFP q 6–12 เดือน: cirrhosis, ชาย > 40, หญิง > 50, FHx HCC",
        ],
        items=[
            mcq("GI-05-03-1", "A 22-year-old man has had fever, fatigue and anorexia for 5 days and jaundice for 3 days. He takes no medications. AST 1,110 U/L, ALT 1,435 U/L, ALP 95 U/L, total bilirubin 13.5 mg/dL, direct 10 mg/dL. HBsAg positive, anti-HBc IgM positive, anti-HAV positive, anti-HAV IgM negative. What is the most likely diagnosis?",
                "Acute hepatitis B", ["Acute hepatitis A", "Chronic hepatitis B with acute flare", "Hepatocellular carcinoma", "Choledocholithiasis"],
                explain='''**HBsAg + anti-HBc IgM บวก** = acute hepatitis B ส่วน "anti-HAV positive" ที่ไม่ระบุ IgM หมายถึง **IgG** = เคยติด HAV/ได้วัคซีน และ anti-HAV IgM ลบ จึงไม่ใช่ acute HAV
- Acute hepatitis A ต้องมี anti-HAV IgM บวก
- Chronic HBV flare อาจมี anti-HBc IgM ต่ำ ๆ ได้ แต่ผู้ป่วยไม่มีประวัติ HBV และอาการเข้าได้กับ acute ครั้งแรก
- HCC ไม่ทำให้ AST/ALT > 1,000 แบบนี้ในคนหนุ่มที่เพิ่งป่วย
- Choledocholithiasis เป็น cholestatic pattern (ALP สูง)''',
                pearl="Anti-HAV ไม่ระบุ IgM = IgG = immune; HBsAg + anti-HBc IgM = acute HBV", topic="HBV serology",
                ref=[f"{D} หน้า 154–155"], nl=["2.3.1(1)", "B8.3(2)"], kind="old", src=OLD),
            mcq("GI-05-03-2", "A 24-year-old man is found to be HBsAg positive after blood donation. He feels well and has never been jaundiced. His mother and all his siblings have hepatitis B. Examination is normal. AST 11 U/L, ALT 13 U/L, albumin 4 g/dL, total bilirubin 0.5 mg/dL. Which is the most appropriate management?",
                "Monitor ALT and platelets every 6–12 months and screen for HIV and HCV",
                ["Start tenofovir immediately", "Repeat HBsAg in 4 weeks and discharge if negative", "Liver biopsy", "Give hepatitis B vaccine"],
                explain='''ติดจากแม่ตั้งแต่เกิด (vertical) และ HBsAg บวกโดยไม่มีอาการ = **chronic HBV** ALT ปกติ อายุ < 35 ปี → ยังไม่เข้าเกณฑ์ antiviral ให้ **ติดตาม AST, ALT, platelet ทุก 6–12 เดือน** ตรวจ co-infection HIV/HCV และพิจารณา HCC surveillance ตามความเสี่ยง (FHx HCC)
- Tenofovir ยังไม่จำเป็นเมื่อ ALT ปกติและไม่มี cirrhosis (ต้องดู HBV DNA และเกณฑ์อื่นก่อน)
- การตรวจซ้ำแค่ 4 สัปดาห์ไม่เหมาะ การติดเชื้อตั้งแต่เกิดแทบไม่หายเอง
- Liver biopsy ไม่จำเป็นเป็นขั้นแรก ใช้ non-invasive fibrosis assessment ได้
- วัคซีนไม่มีประโยชน์ในคนที่ติดเชื้ออยู่แล้ว''',
                pearl="Chronic HBV ALT ปกติ → F/U q 6–12 เดือน + ตรวจ HIV/HCV", topic="Chronic HBV monitoring",
                ref=[f"{D} หน้า 136, 160–161"], nl=["2.3.1-3(3)"], kind="old", src=OLD),
            mcq("GI-05-03-3", "A 30-year-old man has had AST and ALT about 3 times the upper limit for several years. He is asymptomatic and denies alcohol, herbs, IV drug use and multiple partners. Examination is normal. AST 110 U/L, ALT 135 U/L, ALP 95 U/L, albumin 4 g/dL, bilirubin 0.5 mg/dL. HBsAg positive, HBeAg positive, anti-HCV negative. What is the most appropriate next investigation?",
                "HBV DNA viral load", ["Anti-HBc IgM", "Alpha-fetoprotein alone", "Liver biopsy", "Ceruloplasmin"],
                explain='''HBsAg บวกและ ALT สูงเรื้อรังหลายปี = **chronic hepatitis B** ขั้นต่อไปคือ **HBV DNA** เพื่อดูว่าเข้าเกณฑ์ antiviral (DNA ≥ 2,000 IU/mL + ALT > 1.5 เท่า) หรือไม่
- Anti-HBc IgM ใช้แยก acute ไม่จำเป็นเพราะเป็นเรื้อรังหลายปีแล้ว
- AFP อย่างเดียวไม่ใช่การประเมินเพื่อการรักษา (และ surveillance ต้องใช้คู่กับ U/S)
- Liver biopsy ไม่จำเป็นก่อนทราบ viral load
- Ceruloplasmin ใช้หา Wilson disease ซึ่งไม่เข้ากับ HBsAg บวก''',
                pearl="Chronic HBV + ALT สูง → HBV DNA เพื่อดูข้อบ่งชี้ antiviral", topic="Chronic HBV workup",
                ref=[f"{D} หน้า 162–165"], nl=["2.3.1-3(3)", "B8.3(2)"], kind="old", src=OLD),
            mcq("GI-05-03-4", "A 55-year-old man with chronic hepatitis B presents with abdominal distension. Shifting dullness is positive (grade 2 ascites), total bilirubin 2.6 mg/dL, HBV DNA 200,000 IU/mL. Besides sodium restriction and diuretics, which treatment is most important for his liver disease?",
                "Start entecavir or tenofovir", ["Peginterferon alfa", "Observe and repeat HBV DNA in 6 months", "Lamivudine-adefovir combination", "Hepatitis B immunoglobulin"],
                explain='''Chronic HBV ที่มี **decompensated cirrhosis** (ascites, TB > 2) → **ให้ antiviral ทันที** ด้วย nucleos(t)ide analogue ที่ barrier สูง (entecavir, TDF, TAF) ไม่ว่าระดับ DNA เท่าไร
- Peginterferon **ห้ามใช้ใน decompensated cirrhosis** อาจทำให้ตับวายแย่ลง
- การรอ 6 เดือนเสี่ยงตับวาย
- Lamivudine/adefovir เป็นยารุ่นเก่า ดื้อยาง่าย ไม่ใช่ first line
- HBIG ใช้ป้องกันหลังสัมผัสหรือในทารก/หลังปลูกถ่ายตับ''',
                pearl="HBV + decompensated cirrhosis → antiviral (ETV/TDF/TAF) ทันที", topic="HBV antiviral indication",
                ref=[f"{D} หน้า 135, 166–167"], nl=["2.3.1-3(3)", "2.3.11(4)"], kind="old", src=OLD),
            mcq("GI-05-03-5", "A man had acute hepatitis B 6 months ago and now asks about his risk of liver cancer. He is asymptomatic. Which investigation is most appropriate first?",
                "HBsAg and anti-HBs", ["HBsAg and HBV viral load", "Ultrasound of the liver", "AST, ALT and albumin", "Alpha-fetoprotein"],
                explain='''ต้องตอบก่อนว่า **หายแล้วหรือกลายเป็น chronic** — ตรวจ **HBsAg และ anti-HBs** (± anti-HBc) ที่ 6 เดือน: HBsAg หาย + anti-HBs ขึ้น = หาย, HBsAg ยังบวก = chronic HBV แล้วจึงวางแผน HCC surveillance
- HBV viral load มีประโยชน์หลังยืนยันว่าเป็น chronic แล้ว
- U/S และ AFP คือ HCC surveillance ซึ่งทำเมื่อเป็น chronic HBV ที่เข้าเกณฑ์
- AST/ALT/albumin ไม่บอกสถานะการติดเชื้อ''',
                pearl="6 เดือนหลัง acute HBV → HBsAg + anti-HBs ดูว่าหายหรือ chronic", topic="HBV follow-up",
                ref=[f"{D} หน้า 158–159"], nl=["2.3.1-3(3)", "B8.3(2)"], kind="old", src=OLD),
        ]),

    sec("gi-05-04", "Hepatitis C",
        "Acute ส่วนใหญ่ไม่มีอาการ → chronic · anti-HCV + → HCV RNA · sofosbuvir/velpatasvir (± ribavirin ถ้า cirrhosis)", minutes=5,
        source=f"{D} หน้า 139–143", nl=["2.3.1-3(3)", "B8.3(2)"],
        md='''
### Acute hepatitis C
- ติดต่อ **parenteral** (เข็ม, เลือด — ก่อนปี 2535 ยังไม่ได้ตรวจคัดเลือด), vertical, sexual
- **ไม่มีอาการ ~90%**; มีอาการ < 10% (อ่อนเพลีย ตัวเหลือง)
- Lab: ↑AST, ↑↑ALT, ↑TB; **anti-HCV negative แต่ HCV RNA positive** (antibody ยังไม่ขึ้น)
- Tx: supportive; F/U AST, ALT, anti-HCV, HCV RNA
- **มักกลายเป็น chronic** — ส่วนใหญ่จึงพบตอนเป็น chronic แล้ว
- หายเอง → **ไม่มีภูมิคุ้มกัน** (anti-HCV ยังบวกได้ แต่ป้องกันติดซ้ำไม่ได้)

### Chronic hepatitis C
- ไม่มีอาการ
- Ix: **anti-HCV positive → ยืนยันด้วย HCV RNA positive** (หรือ HCV core antigen)
- **Tx: antiviral therapy (DAA) — รักษาหายขาดได้**

| สภาวะ | สูตร (ตามสไลด์) |
|---|---|
| ไม่มี cirrhosis | **Sofosbuvir/Velpatasvir** (12 สัปดาห์ — เสริม) |
| Cirrhosis | Sofosbuvir/Velpatasvir **+ Ribavirin** |

- ตรวจ co-infection: HIV, HBV (DAA อาจทำให้ HBV reactivate — เสริม)
- **HCC surveillance: U/S + AFP ทุก 6–12 เดือน** ถ้ามี cirrhosis หรือ advanced fibrosis (แม้รักษาหายแล้ว)

### แปลผล HCV
| HCV RNA | Anti-HCV | แปลผล |
|---|---|---|
| + | − | **Acute hepatitis C** |
| + | + | **Chronic hepatitis C** |
| − | + | **Resolved (non-immune)** หรือรักษาหายแล้ว |

> ไม่มีวัคซีน HCV · anti-HCV ไม่มีการแยก IgM/IgG
''',
        pearls=[
            "Acute HCV 90% ไม่มีอาการ ส่วนใหญ่เป็น chronic",
            "Anti-HCV + → ยืนยันด้วย HCV RNA",
            "Anti-HCV + แต่ RNA − = หายแล้ว ไม่มีภูมิ",
            "Chronic HCV: sofosbuvir/velpatasvir; cirrhosis เพิ่ม ribavirin",
            "HCV ไม่มีวัคซีน",
        ],
        items=[
            mcq("GI-05-04-1", "A 40-year-old man who received multiple blood transfusions in 1988 is found to be anti-HCV positive on a health check. He is asymptomatic and ALT is 68 U/L. What is the most appropriate next investigation?",
                "HCV RNA", ["Anti-HCV IgM", "Liver biopsy", "Repeat anti-HCV in 6 months", "HCV genotype before any confirmation"],
                explain='''Anti-HCV บวกบอกแค่ว่า **เคยสัมผัสเชื้อ** ต้องยืนยันว่ายังมี viremia ด้วย **HCV RNA** (หรือ HCV core antigen) — ถ้าบวก = chronic HCV ถ้าลบ = หายแล้ว
- Anti-HCV ไม่มีการแยก IgM ในการตรวจทั่วไป
- Liver biopsy ไม่จำเป็น ใช้ elastography/FIB-4 ประเมิน fibrosis
- ตรวจ anti-HCV ซ้ำจะบวกเหมือนเดิม ไม่ได้ข้อมูลเพิ่ม
- Genotype ไม่จำเป็นเมื่อใช้ pangenotypic DAA และต้องยืนยัน viremia ก่อน''',
                pearl="Anti-HCV + → HCV RNA ยืนยัน", topic="HCV diagnosis",
                ref=[f"{D} หน้า 140–141"], nl=["2.3.1-3(3)", "B8.3(2)"]),
            mcq("GI-05-04-2", "A 45-year-old woman has chronic hepatitis C (anti-HCV positive, HCV RNA 1.2 × 10⁶ IU/mL). Transient elastography and imaging show compensated cirrhosis. HBsAg and anti-HIV are negative. Which regimen is most appropriate according to the slides?",
                "Sofosbuvir/velpatasvir plus ribavirin", ["Sofosbuvir/velpatasvir alone for 4 weeks", "Peginterferon plus ribavirin for 48 weeks", "Entecavir", "Observation until decompensation"],
                explain='''Chronic HCV ที่มี **cirrhosis** → ตามสไลด์ใช้ **sofosbuvir/velpatasvir ร่วมกับ ribavirin** (ไม่มี cirrhosis ใช้ SOF/VEL อย่างเดียว)
- SOF/VEL 4 สัปดาห์สั้นเกินไป (มาตรฐาน 12 สัปดาห์)
- Peginterferon + ribavirin เป็นสูตรเก่า ผลข้างเคียงมาก หายน้อยกว่า
- Entecavir เป็นยาต้าน HBV
- การรอจน decompensate ทำให้เสียโอกาสรักษาหายขาด''',
                pearl="HCV + cirrhosis → SOF/VEL + ribavirin", topic="HCV treatment",
                ref=[f"{D} หน้า 140"], nl=["2.3.1-3(3)"]),
            mcq("GI-05-04-3", "A 32-year-old nurse had a needlestick injury from a patient with chronic hepatitis C. Eight weeks later her ALT is 420 U/L. Anti-HCV is negative but HCV RNA is positive. What is the correct interpretation?",
                "Acute hepatitis C", ["Chronic hepatitis C", "Resolved HCV infection with immunity", "False-positive HCV RNA; no infection", "Past HCV infection, non-immune"],
                explain='''**HCV RNA บวกแต่ anti-HCV ยังลบ** = ติดเชื้อเฉียบพลันก่อนที่ antibody จะขึ้น (seroconversion ใช้ ~8–12 สัปดาห์) = acute hepatitis C
- Chronic HCV จะมีทั้ง anti-HCV และ HCV RNA บวก
- HCV ไม่มีภาวะ "หายแล้วมีภูมิ" — คนหายแล้วไม่มีภูมิคุ้มกัน
- RNA บวกพร้อม ALT สูงหลังสัมผัสชัดเจน ไม่ใช่ผลบวกลวง
- Past infection จะเป็น anti-HCV บวกและ RNA ลบ''',
                pearl="HCV RNA + / anti-HCV − = acute HCV", topic="HCV serology",
                ref=[f"{D} หน้า 139, 141"], nl=["2.3.1(1)", "B8.3(2)"]),
        ]),
    ])
