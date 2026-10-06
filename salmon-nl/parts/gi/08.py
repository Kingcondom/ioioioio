from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-GI"
OLD = "ตัวอย่างข้อสอบในสไลด์ NL2-GI"

EV = '''<svg viewBox="0 0 720 270">
 <defs><marker id="gi-08-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="330" height="56" rx="10" class="sunk"/>
 <text x="175" y="32" text-anchor="middle" class="tb">Cirrhosis ทุกราย → surveillance</text>
 <text x="175" y="52" text-anchor="middle" class="t3">TE &lt; 20 kPa + Plt &gt; 150,000 → งด EGD ได้</text>
 <rect x="380" y="10" width="330" height="56" rx="10" class="sunk"/>
 <text x="545" y="32" text-anchor="middle" class="tb">HCC: U/S liver ± AFP</text>
 <text x="545" y="52" text-anchor="middle" class="t3">ทุก 6 เดือน</text>
 <rect x="285" y="86" width="150" height="40" rx="10" class="ac"/>
 <text x="360" y="111" text-anchor="middle" class="tw">EGD</text>
 <path d="M360 126V146M120 146H600M120 146V166M360 146V166M600 146V166" class="ln"/>
 <path d="M120 160V168" class="ln" marker-end="url(#gi-08-01-a)"/>
 <path d="M360 160V168" class="ln" marker-end="url(#gi-08-01-a)"/>
 <path d="M600 160V168" class="ln" marker-end="url(#gi-08-01-a)"/>
 <rect x="20" y="170" width="200" height="40" rx="9" class="oksoft"/>
 <text x="120" y="195" text-anchor="middle" class="tb">No varix</text>
 <rect x="260" y="170" width="200" height="40" rx="9" class="misssoft"/>
 <text x="360" y="195" text-anchor="middle" class="tb">Small varix</text>
 <rect x="480" y="170" width="230" height="40" rx="9" class="badsoft"/>
 <text x="595" y="188" text-anchor="middle" class="tb">Large &gt; 5 mm หรือ high risk</text>
 <text x="595" y="204" text-anchor="middle" class="t3">(red wale mark)</text>
 <path d="M120 210V228" class="ln" marker-end="url(#gi-08-01-a)"/>
 <path d="M360 210V228" class="ln" marker-end="url(#gi-08-01-a)"/>
 <path d="M595 210V228" class="ln" marker-end="url(#gi-08-01-a)"/>
 <rect x="20" y="230" width="200" height="34" rx="9" class="box"/>
 <text x="120" y="252" text-anchor="middle">EGD ซ้ำทุก 2–3 ปี</text>
 <rect x="260" y="230" width="200" height="34" rx="9" class="box"/>
 <text x="360" y="252" text-anchor="middle">EGD ซ้ำทุก 1–2 ปี</text>
 <rect x="480" y="230" width="230" height="34" rx="9" class="bad"/>
 <text x="595" y="252" text-anchor="middle" class="tw">Propranolol (primary prophylaxis)</text>
</svg>'''

SAAG = '''<svg viewBox="0 0 740 330">
 <defs><marker id="gi-08-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="8" width="280" height="44" rx="10" class="ac"/>
 <text x="370" y="27" text-anchor="middle" class="tw">SAAG</text>
 <text x="370" y="44" text-anchor="middle" class="tw">= serum albumin − ascitic albumin</text>
 <path d="M300 52V70H185V86" class="ln" marker-end="url(#gi-08-02-a)"/>
 <path d="M440 52V70H555V86" class="ln" marker-end="url(#gi-08-02-a)"/>
 <rect x="40" y="88" width="290" height="50" rx="9" class="c1soft"/>
 <text x="185" y="109" text-anchor="middle" class="tb">High SAAG ≥ 1.1 g/dL</text>
 <text x="185" y="128" text-anchor="middle" class="t3">Portal hypertension</text>
 <rect x="410" y="88" width="290" height="50" rx="9" class="badsoft"/>
 <text x="555" y="109" text-anchor="middle" class="tb">Low SAAG &lt; 1.1 g/dL</text>
 <text x="555" y="128" text-anchor="middle" class="t3">Non-portal HT</text>
 <path d="M130 138V160H95V176" class="ln" marker-end="url(#gi-08-02-a)"/>
 <path d="M240 138V160H275V176" class="ln" marker-end="url(#gi-08-02-a)"/>
 <path d="M500 138V160H465V176" class="ln" marker-end="url(#gi-08-02-a)"/>
 <path d="M610 138V160H645V176" class="ln" marker-end="url(#gi-08-02-a)"/>
 <rect x="10" y="178" width="170" height="40" rx="8" class="box"/>
 <text x="95" y="196" text-anchor="middle" class="tb">Protein &lt; 2.5</text>
 <text x="95" y="212" text-anchor="middle" class="t3">g/dL</text>
 <rect x="190" y="178" width="170" height="40" rx="8" class="box"/>
 <text x="275" y="196" text-anchor="middle" class="tb">Protein ≥ 2.5</text>
 <text x="275" y="212" text-anchor="middle" class="t3">g/dL</text>
 <rect x="380" y="178" width="170" height="40" rx="8" class="box"/>
 <text x="465" y="196" text-anchor="middle" class="tb">Protein &lt; 2.5</text>
 <text x="465" y="212" text-anchor="middle" class="t3">g/dL</text>
 <rect x="560" y="178" width="170" height="40" rx="8" class="box"/>
 <text x="645" y="196" text-anchor="middle" class="tb">Protein ≥ 2.5</text>
 <text x="645" y="212" text-anchor="middle" class="t3">g/dL</text>
 <path d="M95 218V236" class="ln" marker-end="url(#gi-08-02-a)"/>
 <path d="M275 218V236" class="ln" marker-end="url(#gi-08-02-a)"/>
 <path d="M465 218V236" class="ln" marker-end="url(#gi-08-02-a)"/>
 <path d="M645 218V236" class="ln" marker-end="url(#gi-08-02-a)"/>
 <rect x="10" y="238" width="170" height="84" rx="8" class="misssoft"/>
 <text x="95" y="262" text-anchor="middle" class="tb">Cirrhosis</text>
 <text x="95" y="282" text-anchor="middle" class="t3">Budd-Chiari (late)</text>
 <text x="95" y="306" text-anchor="middle" class="t3">ตับสร้าง protein น้อย</text>
 <rect x="190" y="238" width="170" height="84" rx="8" class="c1soft"/>
 <text x="275" y="262" text-anchor="middle" class="tb">Right heart failure</text>
 <text x="275" y="282" text-anchor="middle" class="t3">Budd-Chiari (early)</text>
 <text x="275" y="302" text-anchor="middle" class="t3">Constrictive pericarditis</text>
 <rect x="380" y="238" width="170" height="84" rx="8" class="c2soft"/>
 <text x="465" y="262" text-anchor="middle" class="tb">Nephrotic syndrome</text>
 <text x="465" y="282" text-anchor="middle" class="t3">(hypoalbuminemia)</text>
 <rect x="560" y="238" width="170" height="84" rx="8" class="badsoft"/>
 <text x="645" y="262" text-anchor="middle" class="tb">Peritoneal disease</text>
 <text x="645" y="282" text-anchor="middle" class="t3">TB · carcinomatosis</text>
 <text x="645" y="302" text-anchor="middle" class="t3">Pancreatitis</text>
</svg>'''

HE = '''<svg viewBox="0 0 740 300">
 <defs><marker id="gi-08-04-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="190" height="56" rx="10" class="box"/>
 <text x="105" y="33" text-anchor="middle" class="tb">ลำไส้: แบคทีเรีย</text>
 <text x="105" y="52" text-anchor="middle" class="t3">ย่อยโปรตีน/เลือด → NH3</text>
 <path d="M200 38H268" class="ln" marker-end="url(#gi-08-04-a)"/>
 <rect x="270" y="10" width="190" height="56" rx="10" class="badsoft"/>
 <text x="365" y="33" text-anchor="middle" class="tb">ตับเสีย + shunt</text>
 <text x="365" y="52" text-anchor="middle" class="t3">กำจัด NH3 ไม่ได้/เลี่ยงตับ</text>
 <path d="M460 38H528" class="ln" marker-end="url(#gi-08-04-a)"/>
 <rect x="530" y="10" width="200" height="56" rx="10" class="bad"/>
 <text x="630" y="33" text-anchor="middle" class="tw">NH3 ถึงสมอง</text>
 <text x="630" y="52" text-anchor="middle" class="tw">→ encephalopathy</text>
 <rect x="10" y="84" width="190" height="62" rx="9" class="c1soft"/>
 <text x="105" y="106" text-anchor="middle" class="tb">Lactulose</text>
 <text x="105" y="124" text-anchor="middle" class="t3">acidify → NH4⁺ ขับทางอุจจาระ</text>
 <text x="105" y="140" text-anchor="middle" class="t3">ถ่าย 2–3 ครั้ง/วัน</text>
 <rect x="10" y="154" width="190" height="44" rx="9" class="c2soft"/>
 <text x="105" y="174" text-anchor="middle" class="tb">Rifaximin</text>
 <text x="105" y="190" text-anchor="middle" class="t3">ฆ่าแบคทีเรียสร้าง NH3</text>
 <path d="M105 84V68" class="lnc1" marker-end="url(#gi-08-04-a)"/>
 <text x="240" y="106" class="ta">Precipitating causes: BIG SCALP</text>
 <g>
 <rect x="240" y="118" width="120" height="34" rx="8" class="misssoft"/><text x="300" y="140" text-anchor="middle"><tspan class="tb">B</tspan>lood transfusion</text>
 <rect x="370" y="118" width="110" height="34" rx="8" class="misssoft"/><text x="425" y="140" text-anchor="middle"><tspan class="tb">I</tspan>nfection (SBP)</text>
 <rect x="490" y="118" width="110" height="34" rx="8" class="misssoft"/><text x="545" y="140" text-anchor="middle"><tspan class="tb">G</tspan>I bleed</text>
 <rect x="610" y="118" width="120" height="34" rx="8" class="misssoft"/><text x="670" y="140" text-anchor="middle"><tspan class="tb">S</tspan>edative</text>
 <rect x="240" y="160" width="120" height="34" rx="8" class="misssoft"/><text x="300" y="182" text-anchor="middle"><tspan class="tb">C</tspan>onstipation</text>
 <rect x="370" y="160" width="110" height="34" rx="8" class="misssoft"/><text x="425" y="182" text-anchor="middle"><tspan class="tb">A</tspan>KI</text>
 <rect x="490" y="160" width="110" height="34" rx="8" class="misssoft"/><text x="545" y="182" text-anchor="middle"><tspan class="tb">L</tspan>ow K</text>
 <rect x="610" y="160" width="120" height="34" rx="8" class="misssoft"/><text x="670" y="182" text-anchor="middle"><tspan class="tb">P</tspan>rotein diet</text>
 </g>
 <rect x="10" y="214" width="720" height="78" rx="9" class="sunk"/>
 <text x="24" y="236" class="tb">West Haven grade</text>
 <text x="24" y="258">MHE/I (covert): ปกติ หรือขาดสมาธิ นอนผิดปกติ คำนวณผิด · II: สับสนเวลา พฤติกรรมเปลี่ยน</text>
 <text x="24" y="278">flapping tremor · III: ง่วงซึม สับสนสถานที่ · IV: coma (overt = II–IV)</text>
</svg>'''

SBP = '''<svg viewBox="0 0 740 300">
 <defs><marker id="gi-08-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="250" y="8" width="240" height="40" rx="10" class="acsoft"/>
 <text x="370" y="33" text-anchor="middle" class="tb">Ascitic fluid: PMN + C/S</text>
 <path d="M310 48V62H285V76" class="ln" marker-end="url(#gi-08-03-a)"/>
 <path d="M430 48V62H630V76" class="ln" marker-end="url(#gi-08-03-a)"/>
 <rect x="10" y="78" width="550" height="34" rx="9" class="bad"/>
 <text x="285" y="100" text-anchor="middle" class="tw">PMN ≥ 250 cells/mm³</text>
 <rect x="570" y="78" width="160" height="34" rx="9" class="box"/>
 <text x="650" y="100" text-anchor="middle" class="tb">PMN &lt; 250</text>
 <path d="M95 112V128" class="ln" marker-end="url(#gi-08-03-a)"/>
 <path d="M285 112V128" class="ln" marker-end="url(#gi-08-03-a)"/>
 <path d="M475 112V128" class="ln" marker-end="url(#gi-08-03-a)"/>
 <path d="M650 112V128" class="ln" marker-end="url(#gi-08-03-a)"/>
 <rect x="10" y="130" width="170" height="36" rx="8" class="box"/>
 <text x="95" y="153" text-anchor="middle">C/S ≥ 2 เชื้อ</text>
 <rect x="200" y="130" width="170" height="36" rx="8" class="box"/>
 <text x="285" y="153" text-anchor="middle">C/S 1 เชื้อ</text>
 <rect x="390" y="130" width="170" height="36" rx="8" class="box"/>
 <text x="475" y="153" text-anchor="middle">C/S negative</text>
 <rect x="570" y="130" width="160" height="36" rx="8" class="box"/>
 <text x="650" y="153" text-anchor="middle">C/S positive</text>
 <path d="M95 166V182" class="ln" marker-end="url(#gi-08-03-a)"/>
 <path d="M285 166V182" class="ln" marker-end="url(#gi-08-03-a)"/>
 <path d="M475 166V182" class="ln" marker-end="url(#gi-08-03-a)"/>
 <path d="M650 166V182" class="ln" marker-end="url(#gi-08-03-a)"/>
 <rect x="10" y="184" width="170" height="106" rx="9" class="badsoft"/>
 <text x="95" y="206" text-anchor="middle" class="tb">Secondary</text>
 <text x="95" y="224" text-anchor="middle" class="tb">peritonitis</text>
 <text x="95" y="250" text-anchor="middle" class="t3">CT abdomen</text>
 <text x="95" y="268" text-anchor="middle" class="t3">+ surgery</text>
 <rect x="200" y="184" width="170" height="106" rx="9" class="c1soft"/>
 <text x="285" y="206" text-anchor="middle" class="tb">SBP</text>
 <text x="285" y="228" text-anchor="middle" class="t3">monomicrobial</text>
 <text x="285" y="250" text-anchor="middle" class="t3">ceftriaxone/cefotaxime</text>
 <text x="285" y="268" text-anchor="middle" class="t3">≥ 5–7 วัน ± albumin</text>
 <rect x="390" y="184" width="170" height="106" rx="9" class="c2soft"/>
 <text x="475" y="206" text-anchor="middle" class="tb">CNNA</text>
 <text x="475" y="226" text-anchor="middle" class="t3">culture-negative</text>
 <text x="475" y="242" text-anchor="middle" class="t3">neutrocytic ascites</text>
 <text x="475" y="268" text-anchor="middle" class="tb">รักษาแบบ SBP</text>
 <rect x="570" y="184" width="160" height="106" rx="9" class="misssoft"/>
 <text x="650" y="206" text-anchor="middle" class="tb">Bacterascites</text>
 <text x="650" y="232" text-anchor="middle" class="t3">มีอาการ → รักษาแบบ SBP</text>
 <text x="650" y="256" text-anchor="middle" class="t3">ไม่มีอาการ → observe</text>
 <text x="650" y="274" text-anchor="middle" class="t3">(เจาะซ้ำ)</text>
</svg>'''

LECTURE = lecture("08", "Cirrhosis & complications",
    subtitle="Cirrhosis · ascites (SAAG) · SBP · hepatic encephalopathy",
    objectives=[
        "วินิจฉัย cirrhosis จาก signs of CLD/portal HT, LFT และ U/S และ work up สาเหตุได้",
        "วางแผน surveillance ของ varices (EGD/propranolol) และ HCC (U/S ± AFP ทุก 6 เดือน)",
        "บอกข้อบ่งชี้เจาะท้อง แปลผล SAAG/protein และรักษา ascites ตามความรุนแรง",
        "แปลผล ascitic PMN/culture แยก SBP, CNNA, bacterascites, secondary peritonitis และให้ยา/albumin/prophylaxis ถูก",
        "หา precipitating cause ของ hepatic encephalopathy (BIG SCALP) และรักษาด้วย lactulose ± rifaximin",
    ],
    sections=[
    sec("gi-08-01", "Cirrhosis: diagnosis, work-up & surveillance",
        "Signs of CLD + portal HT · AST > ALT ↓albumin ↑INR ↓plt · work up HBV/HCV/อื่น ๆ · EGD + HCC surveillance", minutes=8,
        source=f"{D} หน้า 224–245", nl=["2.3.11(4)", "B8.2.5(4)"],
        md='''
### นิยามและกลไก
**Irreversible diffuse fibrosis ของตับ** (+ regenerative nodules) — **hepatic stellate cell (Ito cell)** ถูกกระตุ้นเปลี่ยนเป็น myofibroblast → สร้าง collagen → ↑↑fibrosis

### สาเหตุ
Alcoholic liver disease · **chronic HBV, HCV** · fatty liver (MASLD) · autoimmune hepatitis · Wilson disease · hemochromatosis — **chronic liver disease ทุกสาเหตุนำไปสู่ cirrhosis ได้** (ยกเว้น HAV/HEV ที่ไม่เรื้อรัง)

### อาการ
- อ่อนเพลีย น้ำหนักลด เบื่ออาหาร คัน
- **Signs of portal HT**: ascites, splenomegaly, caput medusae
- **Signs of chronic liver disease** (คำช่วยจำจากสไลด์)

| คำช่วยจำ | Sign |
|---|---|
| ต่อมใหญ่ | Parotid gland enlargement |
| ไข่ฝ่อ | Testicular atrophy |
| พ่อมีเต้า | Gynecomastia |
| เจ้าแมงมุม | Spider nevi |
| ปุ้มนิ้วออก | Clubbing of fingers |
| หมอกลงเล็บ | Terry's nail |
| เจ็บมือแดง | Palmar erythema |

### การตรวจ
- **LFT**: AST/ALT ปกติหรือสูง (**ส่วนใหญ่ AST > ALT**), ALP ปกติ/สูง, ↑TB, **↓albumin, ↑globulin**
- **Coagulogram**: ↑PT, ↑INR (PTT ปกติหรือสูง)
- **CBC**: ↓Hb, **↓platelet** (hypersplenism)
- **U/S**: ผิวตับขรุขระเป็นปุ่ม (nodular), ตับเล็ก, hypoechoic nodules, **left lobe hypertrophy**, ↑echogenicity, ภาวะแทรกซ้อนจาก portal HT (ascites, splenomegaly)
- Liver biopsy = gold standard แต่มักไม่จำเป็น
- **วินิจฉัยจาก**: ประวัติ CLD/ความเสี่ยง + signs of CLD + lab + U/S
- Non-invasive fibrosis: **FIB-4** (อายุ AST ALT platelet), **APRI** (AST platelet), Fibrotest, **liver elastography**

### Work up สาเหตุ
| สาเหตุ | ส่งตรวจ |
|---|---|
| HBV | **HBsAg** |
| HCV | **Anti-HCV** |
| Fatty liver | Lipid profile, HbA1c |
| Alcohol | ประวัติ, AST/ALT > 2 (มัก < 500), GGT |
| Hemochromatosis | Serum iron, ferritin (> 200 หญิง/> 300 ชาย), transferrin saturation > 45% |
| Wilson | Ceruloplasmin, serum total/free copper, urine copper |
| Autoimmune hepatitis | IgG, ANA, anti-smooth muscle, anti-LKM1 |
| PBC / PSC | AMA / MRCP (beaded bile duct) |

### ภาวะแทรกซ้อน
Ascites · esophageal varices · SBP · hepatic encephalopathy · hepatorenal syndrome · HCC
- **Compensated** cirrhosis: ไม่มีอาการ
- **Decompensated**: ascites, variceal hemorrhage, hepatic encephalopathy, jaundice

### การดูแล
- รักษาสาเหตุ · **หลีกเลี่ยง hepatotoxin** (alcohol, NSAIDs) · nutrition
- **Vaccine**: HAV, HBV, influenza, pneumococcal
- **Surveillance**
  - **Esophageal varices: EGD**
  - **HCC: liver U/S ± AFP ทุก 6 เดือน**
- **Liver transplant**: refractory ascites, hepatic encephalopathy, variceal hemorrhage, **MELD ≥ 15**

[[fig:gi-08-01-ev]]

> ตามสไลด์: ถ้า transient elastography < 20 kPa และ platelet > 150,000 **งด EGD ได้** (Baveno criteria)
''',
        figs=[fig("gi-08-01-ev", "Surveillance ใน cirrhosis และ primary prophylaxis ของ varices", EV,
                  "ส่อง EGD ทุกรายที่ไม่เข้าเกณฑ์ยกเว้น แล้วนัดซ้ำตามขนาด varix; varix ใหญ่หรือมี red wale ให้ propranolol ก่อนเลือดออก")],
        pearls=[
            "Fibrosis ใน cirrhosis มาจาก hepatic stellate (Ito) cell",
            "Cirrhosis lab: AST > ALT, ↓albumin, ↑globulin, ↑INR, ↓platelet",
            "Work up สาเหตุ: HBsAg + anti-HCV เป็นอย่างแรก",
            "HCC surveillance: U/S ± AFP ทุก 6 เดือน; EGD: no varix q 2–3 ปี, small q 1–2 ปี, large → propranolol",
            "Decompensated = ascites, variceal bleed, HE, jaundice",
        ],
        items=[
            mcq("GI-08-01-1", "A microscopic section of a cirrhotic liver shows abundant fibrosis of the hepatic parenchyma. Which liver cell is primarily responsible for this collagen deposition?",
                "Hepatic stellate cell", ["Kupffer cell", "Hepatocyte", "Sinusoidal endothelial cell", "Hepatic lymphocyte"],
                explain='''**Hepatic stellate cell (Ito cell)** ใน space of Disse ปกติเก็บ vitamin A เมื่อถูกกระตุ้นจากการอักเสบเรื้อรังจะเปลี่ยนเป็น myofibroblast และสร้าง collagen → fibrosis/cirrhosis
- Kupffer cell เป็น macrophage ปล่อย cytokine กระตุ้น stellate cell แต่ไม่ได้สร้าง collagen เอง
- Hepatocyte เป็นเซลล์ทำงานหลักที่ถูกทำลาย
- Sinusoidal endothelial cell เสีย fenestration (capillarization) แต่ไม่ใช่แหล่ง collagen หลัก
- Lymphocyte เกี่ยวกับการอักเสบ ไม่สร้าง collagen''',
                pearl="Cirrhosis fibrosis = hepatic stellate (Ito) cell", topic="Cirrhosis pathogenesis",
                ref=[f"{D} หน้า 224, 238–239"], nl=["B8.2.5(4)"], kind="old", src=OLD),
            mcq("GI-08-01-2", "A 50-year-old man has features of cirrhosis: jaundice, spider nevi and 2+ pitting edema. He has never been evaluated for the cause. Which set of investigations is most appropriate first to identify the cause?",
                "HBsAg and anti-HCV", ["Anti-HAV IgG and anti-HEV IgM", "HBsAg, HCV antigen and anti-HAV", "Liver biopsy", "Serum alpha-fetoprotein"],
                explain='''สาเหตุที่พบบ่อยและรักษาได้ของ cirrhosis ในไทยคือ chronic HBV และ HCV → ส่ง **HBsAg และ anti-HCV** เป็นอย่างแรก (ร่วมกับประวัติ alcohol และ metabolic risk)
- HAV/HEV ไม่ทำให้ cirrhosis จึงไม่ต้องส่ง
- Anti-HAV ไม่เกี่ยวข้อง และ HCV antigen ไม่ใช่การคัดกรองเริ่มต้น (ใช้ anti-HCV)
- Liver biopsy ไม่จำเป็นในการหาสาเหตุเป็นขั้นแรก
- AFP ใช้คัดกรอง HCC ไม่ได้บอกสาเหตุ''',
                pearl="Cirrhosis หาสาเหตุ → HBsAg + anti-HCV ก่อน", topic="Cirrhosis work-up",
                ref=[f"{D} หน้า 234, 242–243"], nl=["2.3.11(4)", "B8.3(2)"], kind="old", src=OLD),
            mcq("GI-08-01-3", "A woman with cryptogenic cirrhosis returns after 4 months lost to follow-up. Her last ultrasound, CBC, BUN, creatinine and LFT were unremarkable. Her last EGD, 4 years ago, showed no esophageal varices. She has spider nevi and palmar erythema. Platelets 110,000/mm³. Which is the most appropriate management now?",
                "Esophagogastroduodenoscopy", ["Triple-phase CT of the liver", "HBsAg and anti-HCV", "Serum AFP only", "Repeat ultrasound in 2 years"],
                explain='''Cirrhosis ที่ EGD ครั้งก่อนไม่มี varix → ต้องส่องซ้ำ **ทุก 2–3 ปี** ตอนนี้ผ่านมา 4 ปีแล้ว (และ platelet < 150,000 ไม่เข้าเกณฑ์งด EGD) จึงควรทำ **EGD** (เฉลยในสไลด์: EGD)
- Triple-phase CT ใช้เมื่อ U/S เจอก้อนสงสัย HCC
- HBsAg/anti-HCV เป็นการหาสาเหตุ ซึ่งผู้ป่วย cryptogenic น่าจะตรวจไปแล้ว
- AFP อย่างเดียวไม่พอสำหรับ HCC surveillance และ U/S ยังอยู่ในรอบ 6 เดือนเท่านั้น
- U/S ต้องทำทุก 6 เดือน ไม่ใช่ 2 ปี
> หมายเหตุ: U/S ครั้งล่าสุด "4 เดือนก่อน" — ถ้าไม่ได้ทำมาเกิน 6 เดือน U/S ก็เป็นคำตอบที่ถูกได้; โจทย์นี้ต้องการให้เห็นว่า EGD เลยรอบแล้ว''',
                pearl="Cirrhosis no varix → EGD ทุก 2–3 ปี; HCC → U/S ± AFP ทุก 6 เดือน", topic="Cirrhosis surveillance",
                ref=[f"{D} หน้า 236–237, 244–245"], nl=["2.3.11(4)"], kind="old", src=OLD),
            mcq("GI-08-01-4", "A 52-year-old man with compensated HCV cirrhosis undergoes screening EGD, which shows two large esophageal varices (7 mm) with red wale marks. He has never bled. Heart rate 84/min, BP 128/78 mmHg, no asthma. What is the most appropriate management?",
                "Start propranolol", ["Repeat EGD in 1–2 years without treatment", "Transjugular intrahepatic portosystemic shunt", "Long-term proton pump inhibitor", "Sclerotherapy every 3 months"],
                explain='''**Large varices > 5 mm และ high-risk (red wale mark)** ที่ยังไม่เคยเลือดออก → **primary prophylaxis ด้วย non-selective beta-blocker (propranolol)** ตามสไลด์ (EVL เป็นทางเลือกเมื่อใช้ beta-blocker ไม่ได้ — เสริม)
- Repeat EGD 1–2 ปีโดยไม่รักษาใช้กับ small varix
- TIPS ใช้ใน refractory bleeding/ascites ไม่ใช่ prophylaxis
- PPI ไม่ลด portal pressure
- Sclerotherapy ไม่ใช้เป็น primary prophylaxis เพราะภาวะแทรกซ้อนสูง''',
                pearl="Large varix > 5 mm/red wale ยังไม่ bleed → propranolol", topic="Primary prophylaxis",
                ref=[f"{D} หน้า 237"], nl=["B8.2.2-3(7)", "B8.4(2)"]),
            mcq("GI-08-01-5", "A man presents with jaundice and shifting dullness. Albumin 2 g/dL, globulin 4 g/dL, AST 50, ALT 121, ALP 120 U/L, TB 4 mg/dL, DB 3 mg/dL. Ultrasound shows coarse echogenicity with multiple nodules and marked ascites. What is the cause of his jaundice?",
                "Decompensated cirrhosis", ["Hemolysis", "Budd-Chiari syndrome", "Obstructive jaundice from choledocholithiasis", "Gilbert syndrome"],
                explain='''Albumin ต่ำ globulin สูง (reversed A/G ratio) + ตับหยาบเป็นปุ่มใน U/S + ascites + ตัวเหลือง (direct bilirubin เด่น) = **decompensated cirrhosis**
- Hemolysis ทำให้ indirect bilirubin สูงเด่น ไม่ทำให้ albumin ต่ำหรือตับเป็นปุ่ม
- Budd-Chiari มี ascites + ตับโต ปวดท้อง แต่ U/S จะเห็น hepatic vein อุดตัน
- Choledocholithiasis ทำให้ ALP/GGT สูงเด่นและ CBD ขยาย
- Gilbert เป็น indirect hyperbilirubinemia ที่ไม่มีโรคตับ''',
                pearl="Reversed A/G + nodular liver + ascites + jaundice = decompensated cirrhosis", topic="Decompensated cirrhosis",
                ref=[f"{D} หน้า 226, 240–241"], nl=["2.3.11(4)", "2.1.13"], kind="old", src=OLD),
        ]),

    sec("gi-08-02", "Ascites: SAAG & management",
        "SAAG ≥ 1.1 = portal HT · protein แยกต่อ · Na restriction + spironolactone ± furosemide · paracentesis > 5 L ให้ albumin 6–8 g/L", minutes=8,
        source=f"{D} หน้า 246–254, 260–267", nl=["2.1.12", "3.1.7", "2.3.11(4)"],
        md='''
### สาเหตุ
**Cirrhosis ~81–84%** ที่เหลือ: mixed, malignancy, CHF, TB peritonitis, fulminant hepatic failure, constrictive pericarditis, nephrotic, pancreatic, dialysis ascites

### กลไก
**Portal HT (high SAAG)**
- ↑portal venous pressure → น้ำซึมเข้าช่องท้อง
- Splanchnic vasodilation + blood pooling → ↓effective circulating volume → ↓renal blood flow → **RAAS activation** → เก็บ Na และน้ำ

**Non-portal HT (low SAAG)**
- Hypoalbuminemia: ↓oncotic pressure
- Malignancy: lymphatic obstruction, ↑vascular permeability
- Infection: ↑vascular permeability

### อาการ
ท้องโต อิ่มเร็ว น้ำหนักเพิ่ม เหนื่อย — ตรวจ **shifting dullness, fluid thrill**

### การตรวจ
- **Abdominal U/S**: เห็น ascites เล็กน้อยได้ + หาสาเหตุ (cirrhosis, CA)
- **Abdominal paracentesis**
  - Basic: **cell count with differential, albumin, protein**, sugar, LDH, G/S, C/S
  - เพิ่มตามสงสัย: malignancy → cytology; TB → ADA, C/S for TB
- CT abdomen เพื่อหาสาเหตุ

**ข้อบ่งชี้เจาะท้อง (diagnostic paracentesis)**
1. Ascites ครั้งแรก
2. ผู้ป่วยตับแข็งที่มี ascites และ **admit ด้วยสาเหตุใดก็ตาม**
3. Ascites ร่วมกับอาการใหม่: **ไข้**, **ปวดท้อง/กดเจ็บ**, ascites มากขึ้นทั้งที่คุมด้วยยาได้, LFT แย่ลง, AKI, **hepatic encephalopathy**, **leukocytosis**

### SAAG
**SAAG = serum albumin − ascitic albumin** (เจาะวันเดียวกัน)

[[fig:gi-08-02-saag]]

| ตัวอย่างจากสไลด์ | SAAG | Protein | คำตอบ |
|---|---|---|---|
| Serum alb 4, ascitic alb 4.8, protein สูง | 4 − 4.8 = −0.8 (low) | สูง | **Pancreatitis** (peritoneal disease) |
| Serum alb 2.5, ascitic alb 1.1 | 1.4 (high) | — | **Cirrhosis** |
| Serum 3.2, ascitic 1.9, protein 2.1 | 1.3 (high) | ต่ำ | Cirrhosis → precipitant: **high salt intake** |

### การรักษา (หลักการสำหรับ cirrhotic ascites)
- รักษาสาเหตุ
- **Mild** (เห็นแค่ใน U/S): ไม่ต้องรักษา
- **Moderate** (shifting dullness, fluid thrill): **Na restriction** + diuretics: **spironolactone (ตัวแรก)** ± furosemide (อัตราส่วน 100:40 — เสริม)
- **Severe** (ท้องตึงมาก): เพิ่ม **therapeutic paracentesis** — ถ้าเจาะ **> 5 L ให้ albumin 6–8 g ต่อทุก 1 L ที่เจาะ** (ป้องกัน post-paracentesis circulatory dysfunction)
- **Refractory**: **TIPS**, liver transplant

> TIPS = ต่อ shunt จาก portal vein เข้า hepatic vein ผ่านตับ ลด portal pressure (ใช้ทั้ง refractory ascites และ variceal bleeding ที่ EGD ล้มเหลว) แต่เพิ่ม hepatic encephalopathy (เสริม)
''',
        figs=[fig("gi-08-02-saag", "แปลผล SAAG ร่วมกับ ascitic protein", SAAG,
                  "SAAG แยก portal HT กับ non-portal HT ก่อน แล้ว protein แยกต่อ — cirrhosis protein ต่ำ, หัวใจ protein สูง, TB/CA/pancreatitis เป็น low SAAG high protein")],
        pearls=[
            "SAAG = serum albumin − ascitic albumin; ≥ 1.1 = portal HT",
            "High SAAG + protein < 2.5 = cirrhosis; high SAAG + protein ≥ 2.5 = heart failure/early Budd-Chiari",
            "Low SAAG + protein ≥ 2.5 = TB, carcinomatosis, pancreatitis; low protein = nephrotic",
            "Cirrhotic ascites: Na restriction + spironolactone ± furosemide",
            "Paracentesis > 5 L → albumin 6–8 g/L ที่เจาะ; refractory → TIPS/transplant",
        ],
        items=[
            mcq("GI-08-02-1", "A 56-year-old woman has had abdominal swelling for several months. Vital signs are normal. Ultrasound shows free intraperitoneal fluid. Ascitic fluid: WBC < 50/mm³, albumin 4.8 g/dL, total protein 5.8 g/dL; Gram stain and culture pending. Serum albumin 4 g/dL. What is the most likely cause of this ascites?",
                "Pancreatitis", ["Alcoholic cirrhosis", "Cryptogenic cirrhosis", "Heart failure", "Hepatic vein occlusion"],
                explain='''SAAG = 4 − 4.8 = **−0.8 (low SAAG < 1.1)** + **protein สูง** → non-portal HT จาก peritoneal disease (TB, carcinomatosis) หรือ **pancreatitis** ซึ่งเป็นตัวเลือกเดียวในกลุ่มนี้ (เฉลยในสไลด์)
- Alcoholic/cryptogenic cirrhosis เป็น high SAAG low protein
- Heart failure เป็น high SAAG high protein
- Hepatic vein occlusion (Budd-Chiari) เป็น high SAAG
> สไลด์เขียน total protein 18 g/dL ซึ่งเป็นไปไม่ได้ทางสรีรวิทยา (น่าจะพิมพ์ผิด) ข้อนี้ปรับเป็น 5.8 g/dL โดยคงความหมาย "high protein"''',
                pearl="Low SAAG + high protein = peritoneal TB/CA หรือ pancreatitis", topic="SAAG low",
                ref=[f"{D} หน้า 252, 260–261"], nl=["2.1.12", "3.1.7"], kind="old", src=OLD),
            mcq("GI-08-02-2", "An elderly patient has progressive abdominal distension. Shifting dullness and fluid thrill are positive. Ascitic fluid: albumin 1.1 g/dL, WBC 200/mm³ (lymphocytes 60%). Serum albumin 2.5 g/dL. What is the most likely diagnosis?",
                "Cirrhosis", ["Constrictive pericarditis", "Peritoneal carcinomatosis", "Spontaneous bacterial peritonitis", "Nephrotic syndrome"],
                explain='''SAAG = 2.5 − 1.1 = **1.4 g/dL (high SAAG)** → portal hypertension สาเหตุที่พบบ่อยที่สุดคือ **cirrhosis**; WBC 200 lymphocyte เด่น (PMN ~80) ไม่ถึงเกณฑ์ SBP
- Constrictive pericarditis ก็เป็น high SAAG แต่ protein สูงและพบน้อยกว่ามาก ไม่มี clue ทางหัวใจ
- Carcinomatosis เป็น low SAAG
- SBP ต้องมี PMN ≥ 250
- Nephrotic syndrome เป็น low SAAG low protein''',
                pearl="SAAG ≥ 1.1 → portal HT → cirrhosis บ่อยสุด", topic="SAAG high",
                ref=[f"{D} หน้า 252, 262–263"], nl=["2.1.12", "2.3.11(4)"], kind="old", src=OLD),
            mcq("GI-08-02-3", "A 50-year-old man with alcoholic cirrhosis has had increasing abdominal distension for 1 month. Vital signs are stable; there is tense ascites. Ascitic fluid: clear, RBC 15/mm³, WBC 200/mm³ (PMN 40%, L 60%), albumin 1.9 g/dL (serum 3.2 g/dL), protein 2.1 g/dL. What is the most likely precipitating cause of his worsening ascites?",
                "High salt intake", ["Hemoperitoneum", "Tuberculous peritonitis", "Peritoneal carcinomatosis", "Spontaneous bacterial peritonitis"],
                explain='''SAAG 3.2 − 1.9 = 1.3 (high) + protein ต่ำ = ascites จาก cirrhosis เอง ไม่มีหลักฐานของสาเหตุอื่น: PMN = 80 (< 250 ไม่ใช่ SBP), RBC น้อย (ไม่ใช่ hemoperitoneum) → ปัจจัยกระตุ้นที่เหลือคือ **กินเค็ม (high salt intake)** / ไม่ร่วมมือรักษา
- Hemoperitoneum จะมีน้ำสีเลือด RBC จำนวนมาก
- TB peritonitis และ carcinomatosis เป็น low SAAG high protein
- SBP ต้อง PMN ≥ 250''',
                pearl="Cirrhotic ascites แย่ลงโดยน้ำปกติ (PMN < 250) → คิดถึงกินเค็ม/ไม่กินยา", topic="Ascites precipitant",
                ref=[f"{D} หน้า 253, 264–265"], nl=["2.3.11(4)"], kind="old", src=OLD),
            mcq("GI-08-02-4", "A 50-year-old man with cirrhosis for 2 years is admitted with temperature 37.8 °C, moderate jaundice, moderate ascites, spider nevi and other signs of chronic liver disease. Which investigation is most important now?",
                "Diagnostic abdominal paracentesis", ["Liver function test", "Coagulogram", "Complete blood count", "CT of the abdomen"],
                explain='''ผู้ป่วยตับแข็งที่มี ascites และ **admit ด้วยสาเหตุใดก็ตาม** หรือ **มีไข้** เป็นข้อบ่งชี้ **diagnostic paracentesis** เพื่อหา SBP ซึ่งมักไม่มีอาการชัดและมี mortality สูง
- LFT, coagulogram และ CBC มีประโยชน์ แต่ไม่วินิจฉัย SBP
- CT ไม่จำเป็นเป็นขั้นแรกและไม่บอก PMN ในน้ำ
> Coagulopathy ไม่ใช่ข้อห้ามเจาะท้อง (เสริม)''',
                pearl="Cirrhosis + ascites + admit/ไข้ → เจาะท้องทุกราย", topic="Paracentesis indication",
                ref=[f"{D} หน้า 251, 266–267"], nl=["3.1.7", "2.3.11-3(10)"], kind="old", src=OLD),
            mcq("GI-08-02-5", "A 58-year-old man with alcoholic cirrhosis has moderate ascites with shifting dullness. He has stopped drinking, renal function and potassium are normal, and diagnostic paracentesis excludes infection. Which diuretic should be started first along with dietary sodium restriction?",
                "Spironolactone", ["Furosemide alone", "Hydrochlorothiazide", "Acetazolamide", "Mannitol"],
                explain='''Cirrhotic ascites เกิดจาก **secondary hyperaldosteronism** (RAAS activation) → diuretic ตัวแรกคือ **spironolactone** (aldosterone antagonist) ± furosemide ตามสไลด์
- Furosemide อย่างเดียวได้ผลน้อยกว่าและเสี่ยง hypokalemia ซึ่งกระตุ้น HE
- Hydrochlorothiazide ไม่ใช้ใน cirrhotic ascites และทำให้ Na ต่ำ
- Acetazolamide และ mannitol ไม่มีบทบาท''',
                pearl="Cirrhotic ascites: Na restriction + spironolactone (ตัวแรก) ± furosemide", topic="Ascites treatment",
                ref=[f"{D} หน้า 247, 253"], nl=["2.3.11(4)"]),
        ]),

    sec("gi-08-03", "Spontaneous bacterial peritonitis (SBP)",
        "PMN ≥ 250 + เชื้อเดียว · ceftriaxone/cefotaxime ≥ 5–7 วัน · albumin ถ้า TB > 4 หรือ Cr > 1 · prophylaxis ตามข้อบ่งชี้", minutes=7,
        source=f"{D} หน้า 255–259, 268–273", nl=["2.3.11-3(10)", "2.3.11(4)", "3.1.7"],
        md='''
### กลไกและเชื้อ
- **Bacterial translocation** จากลำไส้ (ไม่มีรูทะลุ)
- เชื้อ: **E. coli, K. pneumoniae, Streptococcus spp.** — เป็น **monomicrobial infection**
- Risk: **UGIB, prior SBP, ascitic protein ต่ำ (< 1.5 g/dL)**

### อาการ
ไข้ · ปวด/กดเจ็บทั่วท้อง · ascites มากขึ้น · **hepatic encephalopathy** — หลายรายอาการน้อย จึงต้องเจาะท้องง่าย ๆ

### แปลผล ascitic fluid
[[fig:gi-08-03-sbp]]

| PMN | C/S | วินิจฉัย | การดูแล |
|---|---|---|---|
| ≥ 250 | บวก **≥ 2 เชื้อ** | **Secondary peritonitis** | CT abdomen + surgery |
| ≥ 250 | บวก **1 เชื้อ** | **SBP** | รักษาแบบ SBP |
| ≥ 250 | ลบ | **CNNA** (culture-negative neutrocytic ascites) | รักษาแบบ SBP |
| < 250 | บวก | **Bacterascites** | มีอาการ → รักษาแบบ SBP; ไม่มีอาการ → observe |

> ไม่ต้องรอผล culture — **PMN ≥ 250 ให้ ATB ทันที**

### การรักษา SBP
- **ATB ≥ 5–7 วัน**: IV **ceftriaxone, cefotaxime**, หรือ IV ciprofloxacin
- **Albumin** เมื่อเสี่ยง hepatorenal syndrome: **TB > 4 mg/dL** หรือ **Cr > 1 mg/dL หรือ BUN > 30 mg/dL** (albumin 1.5 g/kg วันแรก และ 1 g/kg วันที่ 3 — เสริม)

### SBP prophylaxis
**ข้อบ่งชี้**
- Cirrhosis + **UGIB** (ceftriaxone 7 วัน)
- Cirrhosis + **ascitic protein < 1.5 g/dL** + renal impairment/liver failure
- **เคยเป็น SBP** (secondary prophylaxis ระยะยาว)

**ยา**: IV ceftriaxone, PO norfloxacin, PO TMP/SMX

> ข้อสอบชอบสลับยา: **ceftriaxone + somatostatin/terlipressin** คือสูตร variceal bleeding ไม่ใช่ SBP; SBP ให้ ATB **5–7 วัน** ไม่ใช่ 15 หรือ 29 วัน
''',
        figs=[fig("gi-08-03-sbp", "แปลผล PMN และ culture ของน้ำในช่องท้อง", SBP,
                  "แยกด้วย PMN 250 ก่อน แล้วดูจำนวนเชื้อ: หลายเชื้อ = มีรูทะลุ (secondary), เชื้อเดียวหรือ culture ลบ = SBP/CNNA รักษาเหมือนกัน")],
        pearls=[
            "SBP = PMN ≥ 250 + culture เชื้อเดียว (E. coli, Klebsiella, strep)",
            "PMN ≥ 250 culture ลบ = CNNA → รักษาแบบ SBP",
            "≥ 2 เชื้อ = secondary peritonitis → CT + surgery",
            "Tx: ceftriaxone/cefotaxime ≥ 5–7 วัน + albumin ถ้า TB > 4 หรือ Cr > 1/BUN > 30",
            "Prophylaxis: cirrhosis + UGIB, protein < 1.5 + ไต/ตับเสีย, prior SBP",
        ],
        items=[
            mcq("GI-08-03-1", "A 56-year-old man with cirrhosis presents with confusion, abdominal pain and fever. Shifting dullness is positive. Paracentesis: SAAG 1.3 g/dL, ascitic PMN 280 cells/mm³. Which is the best treatment while awaiting ascitic fluid culture?",
                "IV cefotaxime", ["Nadolol", "Penicillin G", "Gentamicin", "Oral metronidazole"],
                explain='''Cirrhosis + ไข้ ปวดท้อง สับสน + **ascitic PMN ≥ 250** = SBP → ให้ **third-generation cephalosporin (cefotaxime/ceftriaxone)** ทันทีไม่ต้องรอ culture
- Nadolol เป็น beta-blocker สำหรับ variceal prophylaxis
- Penicillin G ไม่ครอบคลุม gram-negative enteric
- Gentamicin (aminoglycoside) **ห้ามใน cirrhosis** เสี่ยง nephrotoxicity/HRS
- Metronidazole ไม่ครอบคลุม E. coli/Klebsiella
> สไลด์มี levofloxacin เป็นตัวเลือกด้วย ซึ่ง quinolone (ciprofloxacin) ก็อยู่ในรายการยารักษา SBP ของสไลด์ แต่คำตอบที่ดีที่สุดคือ cefotaxime''',
                pearl="SBP → cefotaxime/ceftriaxone ทันที; ห้าม aminoglycoside", topic="SBP treatment",
                ref=[f"{D} หน้า 258, 270–271"], nl=["2.3.11-3(10)"], kind="old", src=OLD),
            mcq("GI-08-03-2", "A man who drinks heavily presents with abdominal pain and distension. Shifting dullness and fluid thrill are positive. Ascitic fluid WBC is 1,500 cells/mm³ (PMN 75%). Gram stain shows no organisms and culture is negative at 48 hours. What is the most likely diagnosis?",
                "Culture-negative neutrocytic ascites", ["Secondary peritonitis", "Spontaneous bacterial peritonitis", "Bacterascites", "Tuberculous peritonitis"],
                explain='''PMN = 1,500 × 0.75 = **1,125 (≥ 250)** แต่ **culture ลบ** = **CNNA** ซึ่งรักษาเหมือน SBP
- Secondary peritonitis ต้องมี culture หลายเชื้อ
- SBP ต้อง culture บวกเชื้อเดียว
- Bacterascites คือ culture บวกแต่ PMN < 250
- TB peritonitis มี lymphocyte เด่นและ low SAAG high protein''',
                pearl="PMN ≥ 250 + culture ลบ = CNNA → tx as SBP", topic="CNNA",
                ref=[f"{D} หน้า 257, 268–269"], nl=["2.3.11-3(10)", "3.1.7"], kind="old", src=OLD),
            mcq("GI-08-03-3", "A 60-year-old woman with HCV cirrhosis has fever, ascites and leg edema. SAAG is 1.5 g/dL and ascitic PMN is 600 cells/mm³ with E. coli on culture. Total bilirubin 4.8 mg/dL, creatinine 1.4 mg/dL. Besides IV ceftriaxone, which additional treatment reduces her risk of hepatorenal syndrome and death?",
                "IV albumin", ["IV somatostatin", "Terlipressin", "Oral ciprofloxacin for 15 days", "Large-volume paracentesis of 8 L"],
                explain='''SBP ที่มี **TB > 4 mg/dL และ Cr > 1 mg/dL** → เสี่ยง hepatorenal syndrome สูง ต้องให้ **IV albumin** ร่วมกับ ATB (ลด HRS และ mortality)
- Somatostatin และ terlipressin เป็นยาของ variceal bleeding (terlipressin ใช้รักษา HRS ที่เกิดแล้ว ไม่ใช่ป้องกัน)
- Ciprofloxacin 15 วันยาวเกินจำเป็น (SBP ≥ 5–7 วัน) และเปลี่ยนจาก IV ไปเป็น PO ในผู้ป่วยหนักไม่เหมาะ
- เจาะท้องปริมาณมากระหว่าง SBP + ไตเริ่มเสียจะทำให้ HRS แย่ลง''',
                pearl="SBP + TB > 4 หรือ Cr > 1/BUN > 30 → เพิ่ม albumin", topic="Albumin in SBP",
                ref=[f"{D} หน้า 258, 272–273"], nl=["2.3.11-3(10)"]),
            mcq("GI-08-03-4", "A 54-year-old man with cirrhosis was treated for culture-proven SBP 1 month ago and has now recovered. Which is the most appropriate long-term management to prevent recurrence?",
                "Daily oral norfloxacin (or TMP/SMX) indefinitely", ["No prophylaxis unless ascitic protein is below 1.5 g/dL", "Monthly IV ceftriaxone", "Oral rifaximin only during admissions", "Pneumococcal vaccine alone"],
                explain='''**เคยเป็น SBP** เป็นข้อบ่งชี้ secondary prophylaxis ระยะยาว ด้วย **PO norfloxacin หรือ TMP/SMX** (ตามสไลด์) เพราะกลับเป็นซ้ำสูงมาก
- Protein < 1.5 เป็นเกณฑ์ของ primary prophylaxis ส่วน prior SBP ให้ได้เลยโดยไม่ต้องดู protein
- Ceftriaxone รายเดือนไม่ใช่ regimen ที่ถูกต้อง (IV ceftriaxone ใช้ระยะสั้นใน UGIB)
- Rifaximin ใช้ป้องกัน HE
- วัคซีน pneumococcal ควรให้แต่ไม่ป้องกัน SBP จาก gram-negative''',
                pearl="Prior SBP → norfloxacin/TMP-SMX ระยะยาว", topic="SBP prophylaxis",
                ref=[f"{D} หน้า 259"], nl=["2.3.11-3(10)"]),
        ]),

    sec("gi-08-04", "Hepatic encephalopathy",
        "NH3 จากลำไส้ + ตับกำจัดไม่ได้ · หา BIG SCALP (เจาะท้องถ้ามี ascites) · lactulose 2–3 ครั้ง/วัน ± rifaximin", minutes=7,
        source=f"{D} หน้า 274–285", nl=["2.3.6(6)", "2.3.11-3(7)"],
        md='''
### กลไก
- **Liver dysfunction** → กำจัด NH3 ได้น้อยลง
- **Portosystemic shunts** → NH3 เลี่ยงตับไปถึงสมองโดยตรง → neurological deterioration

### Precipitating causes — "BIG SCALP"
| ตัวอักษร | สาเหตุ |
|---|---|
| **B** | Blood transfusion |
| **I** | Infection (โดยเฉพาะ **SBP**) |
| **G** | GI bleed |
| **S** | Sedative |
| **C** | Constipation |
| **A** | AKI (และ diuretic เกิน — เสริม) |
| **L** | Low K (hypokalemia → ↑ammoniagenesis ที่ไต) |
| **P** | Protein diet |

[[fig:gi-08-04-he]]

### อาการ
- **Cognitive** (สมาธิ การคำนวณ) · **consciousness** (สับสน ง่วง ซึม) · **motor: asterixis (flapping tremor)**
- นอนผิดปกติ (กลางวันง่วงกลางคืนตื่น), พฤติกรรมเปลี่ยน

| West Haven | ลักษณะ |
|---|---|
| MHE (covert) | ปกติ แต่ผิดปกติใน psychometric test |
| I (covert) | ความรู้สึกตัวเปลี่ยนเล็กน้อย วิตกกังวล/เคลิ้มสุข ขาดสมาธิ คำนวณผิด นอนผิดปกติ |
| II (overt) | สับสนวันเวลา บุคลิกเปลี่ยน เฉื่อยชา พฤติกรรมไม่เหมาะสม **flapping tremor** |
| III | ง่วงซึม สับสนสถานที่ มึนงง clonus hyperreflexia rigidity |
| IV | Coma ไม่ตอบสนองต่อความเจ็บปวด |

### การวินิจฉัย — **diagnosis by exclusion**
ต้องแยกสาเหตุซึมอื่นในผู้ป่วยตับแข็ง: alcohol (intoxication/withdrawal), **Wernicke**, electrolyte (Na, Ca), **hypoglycemia**, ยา (benzodiazepine, opioid), **sepsis/CNS infection**, subdural hematoma/stroke, non-convulsive seizure
- ระดับ NH3 ไม่จำเป็นต่อการวินิจฉัย (เสริม)

### การรักษา
- **รักษา precipitating cause** — ถ้ามี ascites ปานกลางขึ้นไปและไม่รู้สาเหตุ → **เจาะท้องหา SBP**
- **1st line: lactulose** — ขับ NH3 ทางอุจจาระ (ปรับให้ **ถ่าย 2–3 ครั้ง/วัน**)
- **Rifaximin** — ฆ่าแบคทีเรียในลำไส้ที่สร้าง NH3
- **Prevention**: lactulose ± rifaximin
- หลีกเลี่ยง sedative; ไม่ต้องงดโปรตีนระยะยาว (เสริม)

> ข้อสอบ: ผู้ป่วยตับแข็งซึม + ascites + ไข้ (หรือท้องเสียแล้วซึม) → next investigation = **abdominal paracentesis** (หา SBP) · ถ้าไม่มี clue ติดเชื้อ/เลือดออก → initial management = **lactulose**
''',
        figs=[fig("gi-08-04-he", "กลไก hepatic encephalopathy, ตัวกระตุ้น BIG SCALP และจุดออกฤทธิ์ของยา", HE,
                  "NH3 จากลำไส้ไปถึงสมองเมื่อตับกำจัดไม่ได้ — lactulose และ rifaximin ลด NH3 ต้นทาง ส่วนกล่องเหลืองคือตัวกระตุ้นที่ต้องหาทุกครั้ง")],
        pearls=[
            "HE = diagnosis by exclusion — ต้อง R/O hypoglycemia, sepsis, ยา, intracranial",
            "Precipitant: BIG SCALP — หา SBP ด้วยการเจาะท้องถ้ามี ascites",
            "Lactulose 1st line ปรับให้ถ่าย 2–3 ครั้ง/วัน; เพิ่ม rifaximin",
            "Asterixis (flapping tremor) = West Haven grade II",
            "ห้ามให้ benzodiazepine ใน HE",
        ],
        items=[
            mcq("GI-08-04-1", "A 60-year-old man with HBV cirrhosis presents with altered consciousness for 2 hours. He has no fever, abdominal pain or hematemesis. He is drowsy and disoriented to time, place and person, with asterixis. Which is the most appropriate initial management?",
                "Lactulose", ["NG lavage", "Tramadol", "IV ceftriaxone", "Benzodiazepines"],
                explain='''Cirrhosis + ซึม สับสน + **asterixis** = hepatic encephalopathy และไม่มี clue ของ GI bleed หรือการติดเชื้อ → initial management คือ **lactulose** (ร่วมกับหาสาเหตุกระตุ้น)
- NG lavage ใช้เมื่อสงสัยเลือดออกในทางเดินอาหาร ซึ่งผู้ป่วยปฏิเสธ hematemesis
- Tramadol เป็น opioid ทำให้ HE แย่ลง
- Ceftriaxone ใช้เมื่อสงสัยติดเชื้อ/SBP หรือมี UGIB
- Benzodiazepine เป็น sedative ทำให้ HE แย่ลง (S ใน BIG SCALP)''',
                pearl="HE ไม่มี clue ติดเชื้อ/เลือดออก → lactulose", topic="HE initial management",
                ref=[f"{D} หน้า 277, 284–285"], nl=["2.3.6(6)"], kind="old", src=OLD),
            mcq("GI-08-04-2", "A 45-year-old woman with spider nevi presents with altered consciousness. Temperature 39 °C, RR 18/min, pulse 80/min. Shifting dullness and flapping tremor are positive. Which investigation should be done next to find the cause?",
                "Abdominal paracentesis", ["Ultrasound of the abdomen", "Plain film of the abdomen", "CT of the brain", "Lumbar puncture"],
                explain='''Hepatic encephalopathy (flapping tremor) ที่มี **ไข้ + ascites** → precipitating cause ที่ต้องคิดถึงอันดับแรกคือ **SBP** ต้องทำ **abdominal paracentesis** ส่ง cell count/culture
- U/S abdomen ยืนยันว่ามี ascites แต่ไม่บอกการติดเชื้อ
- Plain film abdomen ไม่ช่วย
- CT brain ทำเมื่อมี focal deficit หรือสงสัย intracranial bleed
- Lumbar puncture ทำเมื่อสงสัย meningitis (คอแข็ง) และเสี่ยงในผู้ป่วย coagulopathy''',
                pearl="HE + ไข้ + ascites → เจาะท้องหา SBP", topic="HE precipitant",
                ref=[f"{D} หน้า 274, 282–283"], nl=["2.3.6(6)", "2.3.11-3(10)"], kind="old", src=OLD),
            mcq("GI-08-04-3", "A 56-year-old man with cirrhosis for 2 years has had loose stools 3–4 times/day for 3 days and today became stuporous. Temperature 37.3 °C, pulse 98/min, BP 104/80 mmHg. He has mild jaundice, moderate ascites, spider nevi and palmar erythema. Which investigation is most appropriate?",
                "Abdominal paracentesis", ["Complete blood count", "Stool examination", "Coagulogram", "Liver function test"],
                explain='''ผู้ป่วยตับแข็งซึมลง (HE) ต้องหา precipitating cause "BIG SCALP" และเมื่อมี **ascites ปานกลางขึ้นไป ควรเจาะท้องเสมอ** เพราะ SBP อาจไม่มีไข้หรือปวดท้องชัด (เฉลยในสไลด์: abdominal paracentesis)
- CBC, coagulogram และ LFT ช่วยประเมินภาพรวมแต่ไม่วินิจฉัย SBP
- Stool exam ดูสาเหตุท้องเสีย แต่ท้องเสียอาจเป็นผลของ SBP/ยา lactulose และไม่เปลี่ยนการรักษาเร่งด่วน''',
                pearl="HE + ascites ปานกลางขึ้นไป → เจาะท้อง", topic="HE workup",
                ref=[f"{D} หน้า 280–281"], nl=["2.3.6(6)", "3.1.7"], kind="old", src=OLD),
            mcq("GI-08-04-4", "A 46-year-old man with advanced cirrhosis has worsening abdominal pain and confusion. Temperature 38.6 °C, pulse 106/min, RR 22/min. The abdomen is distended with shifting dullness and diffuse tenderness with rebound. Ascitic PMN is 900 cells/mm³. Which management is most appropriate?",
                "Lactulose plus IV third-generation cephalosporin", ["Lactulose alone", "Emergency laparotomy", "Oral rifaximin alone", "Haloperidol for agitation"],
                explain='''HE ที่มี **SBP เป็น precipitating cause** (ไข้ ปวดกดเจ็บทั่วท้อง PMN ≥ 250) → ต้องรักษาทั้งสองอย่าง: **lactulose + IV cefotaxime/ceftriaxone** (± albumin)
- Lactulose อย่างเดียวไม่ได้รักษาการติดเชื้อที่เป็นต้นเหตุ
- Laparotomy ใช้ใน secondary peritonitis (หลายเชื้อ/free air) ไม่ใช่ SBP
- Rifaximin อย่างเดียวไม่รักษา SBP
- Haloperidol/sedative ทำให้ประเมินระดับความรู้สึกตัวยากและอาจแย่ลง''',
                pearl="HE + SBP → lactulose + ceftriaxone/cefotaxime", topic="HE with SBP",
                ref=[f"{D} หน้า 278–279"], nl=["2.3.6(6)", "2.3.11-3(10)"], kind="old", src=OLD),
        ]),
    ])
