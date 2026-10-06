#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liver function tests (นพ.กิตติ ชื่นยง) → data/gi.json
ต้นฉบับ: Drive 1HWt4TMmRmpgSw8lT_NIjt74YQ5LC-zJ3 · บรรยาย พฤ. 29 ต.ค. 2569 · โน้ต slides/lft_notes.md
ผูก MOCK-150 · อัปเดต: ACG 2017 abnormal liver chemistries · EASL 2024 cholestatic liver diseases/PBC ·
AASLD 2022 Wilson · EASL 2025 AIH · acetaminophen (Rumack–Matthew, NAC)"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_mock import link_mock

SET, LEC = "gi", "29/10"
NLN = ["B8.3(1)", "2.1.13"]
SRC = "สไลด์ นพ.กิตติ — Liver function tests"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None, src=SRC):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": src,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "GI-LFT-MCQ-%02d" % n
R = lambda p: ["สไลด์ นพ.กิตติ — " + p]

# ───────────────────────────── 1
sec("gi-lft-01", "LFT มีอะไรบ้าง และ 5 รูปแบบความผิดปกติ",
    "Bilirubin · AST ALT · ALP GGT 5'-NT · albumin globulin · PT · hepatocellular cholestasis isolated ALP mixed jaundice · R ratio", 8,
"""### ส่วนประกอบของ LFT (สไลด์)
| กลุ่ม | ตัวตรวจ | บอกอะไร |
|---|---|---|
| **การบาดเจ็บของเซลล์ตับ** | **AST, ALT** | เซลล์ตับตาย/อักเสบ |
| **ท่อน้ำดี (cholestasis)** | **ALP, GGT, 5'-nucleotidase** | น้ำดีไหลไม่สะดวก |
| **การขับ** | **Bilirubin** — total = direct + indirect | การจับคู่และขับ bilirubin |
| **การสร้าง (synthetic function)** | **Albumin · PT/INR** | ตับทำงานได้จริงแค่ไหน |
คำว่า "LFT" จึงไม่ตรงนัก — AST ALT ALP เป็น **liver biochemistry** ที่บอกการบาดเจ็บ มีเพียง **albumin และ PT** ที่บอก **การทำงาน**

### 5 รูปแบบ (สไลด์)
1. **Hepatocellular (hepatitis)** — AST/ALT เด่น
2. **Cholestasis** — **direct bilirubin สูง + ALP > 3 เท่า**
3. **Isolated ALP สูง**
4. **Mixed** — **transaminase > 2 เท่า + ALP > 3 เท่า**
5. **Jaundice** — bilirubin เด่น (แยก direct/indirect)

### R ratio (ACG 2017)
**R = (ALT ผู้ป่วย / ULN ของ ALT) ÷ (ALP ผู้ป่วย / ULN ของ ALP)**
| R | รูปแบบ |
|---|---|
| **> 5** | **Hepatocellular** |
| **2–5** | **Mixed** |
| **< 2** | **Cholestatic** |
ใช้มากในการแยกชนิดของ **ตับอักเสบจากยา (DILI)**
""",
    ["ALT/AST = บาดเจ็บ · ALP/GGT = ท่อน้ำดี · albumin/PT = การทำงานจริง",
     "Cholestasis = DB สูง + ALP > 3 เท่า · mixed = transaminase > 2 + ALP > 3 เท่า",
     "R ratio > 5 hepatocellular · 2–5 mixed · < 2 cholestatic"],
    [mcq(N(1), "A patient on a new antibiotic has ALT 150 U/L (ULN 40) and ALP 600 U/L (ULN 120). What is the R ratio and pattern of liver injury?",
         ["R = 3.75, hepatocellular", "R = 0.75, cholestatic", "R = 3.75, mixed", "R = 7.5, hepatocellular", "R = 1.25, mixed"], 1,
         "**R = (ALT/ULN) ÷ (ALP/ULN) = (150/40) ÷ (600/120) = 3.75 ÷ 5 = 0.75**\n\n**R < 2 = cholestatic** · 2–5 = mixed · > 5 = hepatocellular\n\nยาปฏิชีวนะที่ทำให้ตับอักเสบแบบ cholestatic บ่อย เช่น **amoxicillin–clavulanate**",
         "R < 2 cholestatic · 2–5 mixed · > 5 hepatocellular", "R ratio", R("The R ratio") + ["ACG Clinical Guideline: Evaluation of abnormal liver chemistries (2017)"]),
    ])

# ───────────────────────────── 2
sec("gi-lft-02", "Aminotransferase — ระดับและอัตราส่วน AST/ALT",
    "สูง 2–5 เท่า ไม่จำเพาะ · 5–40 ไวรัส AIH ยา Wilson · 40–100 ขาดเลือดหรือ paracetamol · AST/ALT > 2 เหล้า · AST สูงกว่ามาก = นอกตับ", 8,
"""### ระดับ ALT/AST บอกกลุ่มสาเหตุ (สไลด์)
| ระดับ | สาเหตุที่พบ |
|---|---|
| **Mild 2–5 เท่า** | ไม่จำเพาะ · พบบ่อยสุด: **เหล้า · ไขมันพอกตับ (MASLD/NASH) · โรคแทรกซึม** · HBV/HCV เรื้อรัง ยา |
| **Moderate 5–40 เท่า** | **ไวรัสตับอักเสบเฉียบพลัน · AIH · ยา · Wilson · hemochromatosis** |
| **Marked 40–100 เท่า (> 1,000–หลายพัน)** | **ตับขาดเลือด (ischemic hepatitis) · paracetamol** · ไวรัสบางราย |

### อัตราส่วน AST/ALT (สไลด์)
| AST/ALT | นึกถึง |
|---|---|
| **> 2** | **ตับจากเหล้า** — ขาด pyridoxal-5-phosphate ทำให้สร้าง ALT น้อย · AST มีใน mitochondria ที่เหล้าทำลาย |
| **< 1** | **ไวรัสตับอักเสบ · ไขมันพอกตับ** (ยกเว้นเมื่อเป็นตับแข็งแล้ว อัตราส่วนกลับ > 1) |
| 1–2 | ไม่จำเพาะ |
| **AST สูงกว่า ALT มาก** | **สาเหตุนอกตับ** — กล้ามเนื้อ (rhabdomyolysis, ออกกำลังกายหนัก) **ดู CK** · เม็ดเลือดแดงแตก · หัวใจ |

### ตับอักเสบจากเหล้า (เพิ่มเติม)
AST/ALT > 2 และ **AST แทบไม่เกิน 300–400** · GGT สูง · MCV โต — ถ้า AST > 500 ให้หาสาเหตุอื่นร่วม
""",
    ["2–5 เท่า: เหล้า MASLD · 5–40: ไวรัส AIH ยา Wilson · 40–100: ขาดเลือด paracetamol",
     "AST/ALT > 2 = เหล้า · < 1 = ไวรัส MASLD",
     "Alcoholic hepatitis: AST มักไม่เกิน 300–400",
     "AST >>> ALT → ดู CK (กล้ามเนื้อ)"],
    [mcq(N(2), "A 52-year-old man has AST 210 U/L, ALT 85 U/L, GGT 420 U/L and MCV 104 fL. Which is the most likely cause?",
         ["Acute hepatitis A", "Alcohol-associated liver disease", "Acetaminophen toxicity", "Ischaemic hepatitis", "Acute hepatitis B"], 1,
         "**AST/ALT ≈ 2.5 (> 2)** + **AST ไม่สูงมาก (< 300–400)** + **GGT สูง** + **MCV โต** = รูปแบบของ **ตับจากเหล้า**\n\nไวรัสตับอักเสบเฉียบพลันมี ALT > AST และสูงเป็นพัน · paracetamol และตับขาดเลือดสูง 40–100 เท่า",
         "AST/ALT > 2 + GGT สูง + MCV โต = เหล้า", "AST/ALT ratio", R("AST/ALT"), NLN + ["2.3.11(2)", "B8.2.5(3)"]),
     mcq(N(3), "After a marathon, a 25-year-old man has AST 480 U/L and ALT 95 U/L with normal bilirubin and ALP. What is the most useful next test?",
         ["Hepatitis B serology", "Creatine kinase", "Liver biopsy", "Ceruloplasmin", "Anti-smooth muscle antibody"], 1,
         "สไลด์: **AST สูงกว่า ALT มาก = สาเหตุนอกตับ** — AST มีมากในกล้ามเนื้อลาย กล้ามเนื้อหัวใจ และเม็ดเลือดแดง ส่วน ALT จำเพาะต่อตับกว่า\n\nหลังออกกำลังกายหนัก → ตรวจ **CK** หา **rhabdomyolysis** ก่อนสืบค้นโรคตับ",
         "AST >>> ALT → CK ก่อน", "Extrahepatic AST", R("AST/ALT")),
    ])

# ───────────────────────────── 3
sec("gi-lft-03", "Transaminase สูงมาก: ตับอักเสบเฉียบพลัน ตับขาดเลือด และ paracetamol",
    "เคสหอยดิบ → HAV · ขั้นตอนตรวจไวรัส · ALT/LDH < 1.5 = ขาดเลือด · กินยาแก้ปวดกำมือ → paracetamol · NAC", 11,
"""### เคสในสไลด์ — ชาย 29 ปี
ไม่สบาย เบื่ออาหารหลายวันก่อนเหลือง · อึดอัดชายโครงขวา · ไม่มีโรคตับเดิม ไม่มีปัจจัยเสี่ยงไวรัส · **กินหอยเมื่อหลายสัปดาห์ก่อน** · ตับโตกดเจ็บ คลำม้ามได้ · **TB 15 · AST 1,350 · ALT 1,525 · PT 14 วินาที**
→ **Acute hepatitis (ALT > AST เป็นพัน)** — สงสัย **ไวรัสตับอักเสบเอ** จากอาหารทะเล

### ขั้นตอนหาสาเหตุ acute hepatitis (สไลด์)
1. ประวัติและตรวจร่างกาย — **เหล้า ยา/สมุนไพร ความเสี่ยงไวรัส**
2. **IgM anti-HAV** · **HBsAg + IgM anti-HBc** · **anti-HCV** (± HCV RNA) · anti-HDV ถ้าเป็น HBV · (anti-HEV IgM)
3. ลบหมด → **Wilson · EBV · CMV · AIH · หัวใจล้มเหลว** → **เจาะชิ้นเนื้อตับ**
> รายละเอียดผลเลือดไวรัสและตาราง HBV อยู่ในคาบ **Acute and chronic hepatitis (12 ต.ค.)**

### Ischemic hepatitis (shock liver)
- ภาวะความดันต่ำ/หัวใจล้มเหลว → AST/ALT **ขึ้นเป็นพันเร็วมากใน 1–3 วัน และลงเร็ว**
- **LDH สูงมาก** — **ALT/LDH < 1.5 เป็นลักษณะของตับขาดเลือด** (ไวรัสมักมากกว่า 1.5)
- Bilirubin ขึ้นช้า ๆ ภายหลัง

### Paracetamol (acetaminophen) — เคสในสไลด์
**หญิง 23 ปี กินยาแก้ปวด "1 กำมือ" 1 สัปดาห์ก่อน** · เหลือง อ่อนเพลีย ไข้ต่ำ ตับโต 3 ซม. · **AST 3,580 > ALT 2,500** · TB 8 · ALP 230
→ **ตับอักเสบจาก paracetamol** (transaminase สูงหลายพัน · AST อาจ > ALT ในช่วงแรก)

**กลไกและการรักษา (ไม่ได้มาจากสไลด์)**
- ขนาดปกติเปลี่ยนเป็นสารไม่พิษ · ขนาดสูง → **CYP2E1 สร้าง NAPQI** มากจน **glutathione หมด** → เซลล์ตับตาย (zone 3)
- เสี่ยงขึ้นใน **ดื่มเหล้าเรื้อรัง ขาดอาหาร ยากระตุ้นเอนไซม์**
- **N-acetylcysteine (NAC)** เติม glutathione — **ให้เร็วที่สุด ได้ผลดีที่สุดภายใน 8 ชม.** แต่ **ยังให้ประโยชน์แม้มาช้า** หรือมีตับวายแล้ว
- กินครั้งเดียวรู้เวลา → ใช้ **Rumack–Matthew nomogram** (ระดับยาตั้งแต่ 4 ชม.) · กินหลายครั้ง/ไม่รู้เวลา หรือ AST สูงแล้ว → ให้ NAC เลย
- ประเมิน **King's College criteria** (pH < 7.3 หรือ INR > 6.5 + Cr > 3.4 + encephalopathy ระดับ 3–4) → ส่งปลูกถ่ายตับ
""",
    ["ALT > AST เป็นพัน + อาหารทะเล → IgM anti-HAV",
     "ไวรัสลบ → Wilson EBV CMV AIH หัวใจล้มเหลว → biopsy",
     "Ischemic hepatitis: ขึ้นลงเร็ว · ALT/LDH < 1.5",
     "Paracetamol: NAPQI → glutathione หมด · NAC ให้ได้แม้มาช้า"],
    [mcq(N(4), "A 68-year-old man had cardiogenic shock 2 days ago, now resolved. AST is 4,200 U/L, ALT 2,900 U/L and LDH 3,800 U/L, with bilirubin 1.6 mg/dL. What is the most likely diagnosis?",
         ["Acute hepatitis A", "Ischaemic hepatitis", "Acute hepatitis B", "Autoimmune hepatitis", "Alcoholic hepatitis"], 1,
         "หลัง **ช็อก** · transaminase **พุ่งเป็นพันใน 1–3 วัน** · **LDH สูงมาก — ALT/LDH = 2,900/3,800 ≈ 0.76 (< 1.5)** = ลักษณะของ **ischemic hepatitis**\n\nไวรัสตับอักเสบมักมี ALT/LDH > 1.5 และ bilirubin สูงกว่านี้มาก · ตับขาดเลือดจะลดลงเร็วเมื่อแก้การไหลเวียน",
         "หลังช็อก + LDH สูงมาก (ALT/LDH < 1.5) = ischemic hepatitis", "Ischaemic hepatitis", R("ALT/LDH < 1.5 is typical for ischemic hepatitis")),
     mcq(N(5), "A 23-year-old woman took a handful of paracetamol tablets about 24 hours ago (exact time unknown). AST is 1,800 U/L. What is the most appropriate immediate treatment?",
         ["Wait for the 4-hour paracetamol level before deciding", "Start IV N-acetylcysteine now", "Activated charcoal only", "Oral vitamin K", "Corticosteroids"], 1,
         "กินขนาดสูงและ **ไม่รู้เวลาแน่ชัด/เกินเวลาที่ใช้ nomogram ได้ และตับอักเสบแล้ว** → **ให้ NAC ทางหลอดเลือดทันที** ไม่ต้องรอระดับยา\n\nNAC เติม glutathione จับ NAPQI · ได้ผลดีที่สุดภายใน 8 ชม. **แต่ยังลดอัตราตายแม้มาช้าหรือมีตับวาย** · ผงถ่านใช้เมื่อมาภายใน 1–2 ชม.\n\n*(การรักษาไม่ได้มาจากสไลด์)*",
         "Paracetamol ไม่รู้เวลา หรือ AST สูงแล้ว → NAC ทันที", "Paracetamol toxicity", ["Acetaminophen toxicity — standard toxicology practice (Rumack–Matthew, NAC)"], NLN + ["2.3.11-3(7)"]),
    ], NLN + ["2.3.1(1)", "2.3.11-3(7)"])

# ───────────────────────────── 4
AI = NLN + ["2.3.1-3(3)"]
sec("gi-lft-04", "Transaminase สูงเล็กน้อยเรื้อรัง: ไล่หาสาเหตุ · AIH · Wilson",
    "เหล้า ยา ไวรัส B C MASLD · AIH หญิงสาว ANA ASMA anti-LKM score ≥ 6/7 · Wilson AST/ALT > 2.2 + ALP/TB < 4 · ceruloplasmin < 200 mg/L", 10,
"""### ขั้นตอนเมื่อ LFT สูงเล็กน้อยแบบกระจาย (สไลด์)
| ขั้น | หาอะไร |
|---|---|
| ประวัติ ตรวจร่างกาย | **เหล้า · ยา/สมุนไพร** |
| ปัจจัยเสี่ยงไวรัส | **HBsAg · anti-HCV** |
| กลุ่มอาการเมตาบอลิก (อ้วน เบาหวาน ความดัน ไขมัน) | **ไขมันพอกตับ (MASLD)** |
| ลักษณะภูมิต้านตนเอง | **globulin · ANA · anti-smooth muscle (ASMA)** |
| อื่น ๆ | **hemochromatosis (ferritin, transferrin saturation) · Wilson (ceruloplasmin)** |
| ยังไม่ทราบ | **เจาะชิ้นเนื้อตับ** |

### Autoimmune hepatitis (สไลด์)
- **หญิงสาวเด่น** (แต่พบได้ทุกวัย) · ไม่มีอาการ อ่อนเพลีย เหลือง คัน ปวดข้อ · **ตับวายเฉียบพลัน 2–5%**
- โรคภูมิต้านตนเองร่วม: **ไทรอยด์อักเสบ 10–23%** · UC · celiac · T1DM · RA 2–5% · SLE 1–2%
| ชนิด | แอนติบอดี |
|---|---|
| **Type 1** (พบบ่อย ผู้ใหญ่) | **ANA · ASMA** |
| **Type 2** (เด็ก) | **anti-LKM1 · anti-LC1** |
- พยาธิ: **interface hepatitis · lymphoplasmacytic infiltration รอบ portal**
- **Simplified criteria (IAIHG 2008)**: autoantibody · **IgG สูง** · ชิ้นเนื้อเข้ากัน · ไม่มีไวรัส → **≥ 6 = probable · ≥ 7 = definite**
- รักษา **prednisolone ± azathioprine** (budesonide ในรายไม่มีตับแข็ง) — *(การรักษาไม่ได้มาจากสไลด์ · EASL 2025)*

### Wilson disease (สไลด์)
- โรคพันธุกรรม (ATP7B ถ่ายทอดแบบยีนด้อย) ทองแดงสะสม — **ตับ และ/หรือ ระบบประสาท** · อายุน้อย (มักก่อน 40)
- ตับ: เรื้อรังหรือ **ตับวายเฉียบพลัน (fulminant)**
- **LFT ช่วยบอก: AST/ALT > 2.2 และ ALP/TB < 4** ในตับวายจาก Wilson (ALP ต่ำผิดคาด · bilirubin สูงมากจาก **เม็ดเลือดแดงแตก Coombs ลบ**)
- ประสาท: **extrapyramidal** (สั่น dystonia พูดไม่ชัด) จิตเวช
- ตา: **Kayser–Fleischer ring · sunflower cataract**
- วินิจฉัย: **ceruloplasmin < 200 mg/L (< 20 mg/dL)** · ทองแดงในปัสสาวะ 24 ชม. > 100 µg · ทองแดงในตับ
- รักษา: **D-penicillamine หรือ trientine** · zinc (ระยะคงที่) · ตับวาย → ปลูกถ่ายตับ — *(ไม่ได้มาจากสไลด์ · AASLD 2022)*
""",
    ["LFT สูงเล็กน้อย: เหล้า ยา HBV HCV MASLD → AIH hemochromatosis Wilson → biopsy",
     "AIH type 1: ANA ASMA · type 2: anti-LKM1 · IgG สูง · score ≥ 6 probable ≥ 7 definite",
     "Wilson ตับวาย: AST/ALT > 2.2 + ALP/TB < 4 + hemolysis",
     "Wilson: ceruloplasmin < 200 mg/L · KF ring"],
    [mcq(N(6), "A 17-year-old girl presents with acute liver failure. Bilirubin 22 mg/dL, ALP 40 U/L, AST 280 U/L, ALT 95 U/L, Hb 8.5 g/dL with a negative Coombs test. Which diagnosis must be considered first?",
         ["Acute hepatitis A", "Wilson disease", "Paracetamol overdose", "Primary biliary cholangitis", "Gilbert syndrome"], 1,
         "สไลด์: Wilson ช่วยบอกด้วย **AST/ALT > 2.2 (280/95 ≈ 2.9) และ ALP/TB < 4 (40/22 ≈ 1.8)** · ร่วมกับ **เม็ดเลือดแดงแตก Coombs ลบ** (ทองแดงอิสระทำลายเม็ดเลือด) ในวัยรุ่นที่ตับวาย\n\nยืนยันด้วย **ceruloplasmin ต่ำ · ทองแดงในปัสสาวะ · KF ring** · Wilson ที่มาด้วยตับวายเฉียบพลันมักต้อง **ปลูกถ่ายตับ**",
         "ตับวายวัยรุ่น + ALP ต่ำ + hemolysis Coombs ลบ = Wilson", "Wilson disease", R("Wilson disease"), NLN + ["2.3.11-3(7)"]),
     mcq(N(7), "A 34-year-old woman with Hashimoto thyroiditis has ALT 320 U/L, raised IgG and positive ANA and anti-smooth muscle antibody. Viral markers are negative. What is the most likely diagnosis?",
         ["Primary biliary cholangitis", "Type 1 autoimmune hepatitis", "Type 2 autoimmune hepatitis", "Wilson disease", "Hemochromatosis"], 1,
         "**หญิงอายุน้อย + โรคภูมิต้านตนเองร่วม (ไทรอยด์อักเสบพบ 10–23%) + transaminase สูง + IgG สูง + ANA และ ASMA** = **AIH type 1**\n\n**Type 2** มี **anti-LKM1/anti-LC1** และพบในเด็ก · **PBC** ใช้ AMA และเป็นแบบ cholestatic (ALP สูง transaminase ปกติ)",
         "ANA + ASMA + IgG สูง = AIH type 1 · anti-LKM = type 2", "Autoimmune hepatitis", R("Autoimmune hepatitis"), AI),
    ], AI, SRC + " · AASLD 2022 Wilson · EASL 2025 AIH")

# ───────────────────────────── 5
CHO = NLN + ["B8.2.2-3(6)", "2.3.11-3(3)"]
sec("gi-lft-05", "Cholestasis: อุดตันทางกล vs ทางยา (medical) · PBC · sepsis",
    "DB สูง + ALP > 3 เท่า · อุดตัน: นิ่ว มะเร็งรอบ ampulla ถุงน้ำท่อน้ำดี ท่อตีบ · medical: ยา sepsis PBC PSC · Courvoisier · AMA", 11,
"""### นิยาม (สไลด์)
**Cholestasis = direct hyperbilirubinemia + ALP สูงกว่า 3 เท่า**
- **โรคท่อน้ำดีเล็ก (small duct) อาจมี bilirubin ปกติ** — ต้องแยกจาก isolated ALP สูง

| **อุดตันทางกล (obstructive)** | **Medical (intrahepatic) cholestasis** |
|---|---|
| **นิ่วในท่อน้ำดี** | **ยา** (amoxicillin–clavulanate, anabolic steroid, chlorpromazine) |
| **มะเร็งรอบ ampulla** (หัวตับอ่อน ท่อน้ำดีปลาย ampulla duodenum) | **ติดเชื้อในกระแสเลือด (sepsis)** |
| ถุงน้ำท่อน้ำดี (choledochal cyst) | **PBC · PSC** |
| ท่อน้ำดีตีบชนิดไม่ร้าย | AIDS cholangiopathy · โรคแทรกซึม |

### เบาะแสว่าเป็นการอุดตัน (สไลด์)
- **ปวดชายโครงขวา + ไข้** (cholangitis)
- **อุจจาระสีซีด (acholic stool)**
- **คลำถุงน้ำดีได้แต่ไม่เจ็บ (Courvoisier sign)** → มะเร็งรอบ ampulla มากกว่านิ่ว
- **คันตามตัว**
→ **อัลตราซาวนด์ดูท่อน้ำดีขยาย** เป็นการตรวจแรก

### เคสในสไลด์
**ชาย 57 ปี ไข้ เหลือง ปวดท้อง 2 วัน · T 39 °C · Murphy ลบ · อุจจาระสีปกติ · TB/DB 5/3 · AST/ALT 55/60 · ALP 380**
→ แปล: **cholestatic pattern** (DB เด่น ALP > 3 เท่า transaminase ใกล้ปกติ) + ไข้สูง → **ท่อน้ำดีอักเสบ (ascending cholangitis)** หรือฝีในตับ/sepsis → **US** ดูท่อน้ำดีและฝี · hemoculture · ยาปฏิชีวนะ · ERCP ถ้าท่อขยาย

**หญิง 74 ปี ปอดอักเสบ นอนโรงพยาบาลได้ยาปฏิชีวนะ แล้วเหลือง · TB/DB 5/3 · AST ALT ปกติ · ALP 540 · US ปกติ**
→ **cholestasis ที่ท่อไม่ขยาย = medical cholestasis** → **sepsis-induced cholestasis** (cytokine ยับยั้งตัวขนส่งน้ำดี) หรือ **ตับอักเสบจากยาปฏิชีวนะ** · รักษาการติดเชื้อ ทบทวนยา

### Primary biliary cholangitis (สไลด์)
- **หญิงวัยกลางคน** · **คัน** เหลือง อ่อนเพลีย
- **ALP และ GGT สูง · transaminase ปกติ** · bilirubin แล้วแต่ระยะ
- **Antimitochondrial antibody (AMA)** — ตัวหลัก (> 90%) · ASMA ถึง 67% · ANA ถึง 50%
- **รักษา (ไม่ได้มาจากสไลด์ · EASL 2024/AASLD)**: **ursodeoxycholic acid 13–15 มก./กก./วัน ตลอดชีวิต** · ตอบสนองไม่พอ → **PPAR agonist (elafibranor, seladelpar — FDA 2024)** หรือ fenofibrate/bezafibrate · obeticholic acid ถูกถอนข้อบ่งใช้ในสหรัฐฯ ปี 2025
""",
    ["Cholestasis = DB สูง + ALP > 3 เท่า · small duct อาจ bilirubin ปกติ",
     "อุดตัน: ปวด+ไข้ · อุจจาระซีด · Courvoisier · คัน → US",
     "เหลืองใน sepsis ท่อไม่ขยาย = sepsis-induced cholestasis",
     "PBC: หญิงวัยกลางคน คัน ALP สูง AMA บวก → UDCA"],
    [mcq(N(8), "A 52-year-old woman has 1 year of pruritus and fatigue. ALP 420 U/L, GGT 380 U/L, AST/ALT normal, bilirubin 1.0 mg/dL. Ultrasound shows a normal biliary tree. Which test is most useful for diagnosis?",
         ["Anti-smooth muscle antibody", "Antimitochondrial antibody", "Anti-LKM1", "Ceruloplasmin", "HBsAg"], 1,
         "หญิงวัยกลางคน + **คัน อ่อนเพลีย** + **ALP/GGT สูง transaminase ปกติ** + **ท่อน้ำดีไม่ขยาย** = small duct cholestasis → **PBC**\n\nตรวจ **AMA** (บวก > 90%) · ASMA และ ANA อาจบวกได้แต่ไม่จำเพาะ · รักษาด้วย **ursodeoxycholic acid**",
         "หญิง คัน ALP สูง ท่อไม่ขยาย → AMA → PBC", "Primary biliary cholangitis", R("Primary biliary cholangitis"), NLN),
     mcq(N(9), "A 66-year-old man has progressive painless jaundice, pale stools, pruritus and weight loss. A non-tender gallbladder is palpable. What is the most likely cause?",
         ["Choledocholithiasis", "Carcinoma of the pancreatic head (periampullary cancer)", "Primary biliary cholangitis", "Acute cholecystitis", "Gilbert syndrome"], 1,
         "**Courvoisier sign** — ถุงน้ำดีโตคลำได้ไม่เจ็บในคนเหลือง → การอุดตันค่อยเป็นค่อยไป **มักเป็นมะเร็งรอบ ampulla (หัวตับอ่อน)** มากกว่านิ่ว (นิ่วทำให้ถุงน้ำดีอักเสบเรื้อรังจนพังผืด ขยายไม่ได้)\n\nเหลืองไม่ปวด + อุจจาระซีด + คัน + น้ำหนักลด = **obstructive jaundice** → US แล้ว **CT ตับอ่อน**",
         "เหลือง ไม่ปวด + Courvoisier = มะเร็งรอบ ampulla", "Obstructive jaundice", R("Clinical clues of obstructive jaundice"), NLN + ["B8.2.4-3(2)"]),
    ], CHO, SRC + " · EASL 2024 cholestatic liver disease")

# ───────────────────────────── 6
sec("gi-lft-06", "ALP · GGT · 5'-nucleotidase — ALP สูงอย่างเดียว",
    "ALP มาจากกระดูก รก ลำไส้ · ปกติสูงในวัยรุ่น ตั้งครรภ์ หลังอาหาร · ยืนยันแหล่งตับด้วย GGT/5'-NT · GGT ไม่มีในกระดูก · GGT สูงอย่างเดียว = เหล้า ยา", 9,
"""### Alkaline phosphatase (สไลด์)
- แหล่งนอกตับ: **กระดูก · รก · ลำไส้** · เม็ดเลือดขาว · ไต
- **สูงตามสรีรวิทยา: วัยรุ่น (กระดูกโต) · ตั้งครรภ์ (รก ไตรมาสสาม) · หลังอาหาร** (เลือดกลุ่ม O/B)
- **ยืนยันว่ามาจากตับ**: **1) GGT · 2) 5'-nucleotidase · 3) ALP isoenzyme**

### ALP สูงอย่างเดียว (isolated) จากตับ — คิดถึง (สไลด์)
- **ท่อน้ำดีหลักอุดตันข้างเดียว** (ท่ออีกข้างยังระบายได้ bilirubin จึงปกติ)
- **โรคแทรกซึม** — วัณโรค lymphoma amyloid sarcoid
- **ก้อนในตับ** — มะเร็งแพร่กระจาย ฝี
- **cholestasis ท่อเล็กระยะแรก** — **PBC · ยา**
นอกตับ: **โรคกระดูก** — Paget · มะเร็งแพร่กระจายไปกระดูก · กระดูกหักกำลังติด · osteomalacia/vitamin D ต่ำ · hyperparathyroidism

### GGT (สไลด์)
- อยู่ในเซลล์ตับและเยื่อบุท่อน้ำดี + ไต ม้าม ตับอ่อน หัวใจ ปอด สมอง ลำไส้ ต่อมลูกหมาก
- **ไวต่อโรคตับและทางเดินน้ำดี แต่ไม่จำเพาะ** — สูงได้ใน เบาหวาน โรคไต MI รูมาติก ตับอ่อนอักเสบ
- **เหล้าและยากระตุ้นการสร้าง**
- **ไม่พบในกระดูก** → ALP สูง + GGT ปกติ = มาจากกระดูก
**GGT สูงอย่างเดียว**: **เหล้า · ยา — กันชัก (phenytoin, carbamazepine) · warfarin**

### Delta bilirubin (สไลด์)
ในท่อน้ำดีอุดตันนาน **bilirubin จับ albumin แบบโควาเลนต์** → **ครึ่งชีวิตเท่า albumin (~20 วัน)** — **อธิบายว่าทำไมเหลืองยังค้างนานหลังแก้การอุดตันแล้ว**

### เคสในสไลด์ — หญิง 30 ปี ตรวจสุขภาพ ALP 580 อย่างเดียว
แปล: isolated ALP สูง → สาเหตุ: **ตั้งครรภ์ · โรคกระดูก · PBC ระยะแรก · โรคแทรกซึม/ก้อนในตับ** → **ตรวจ GGT (หรือ 5'-NT)** ยืนยันว่ามาจากตับ แล้ว US และ AMA
""",
    ["ALP สูงตามธรรมชาติ: วัยรุ่น ตั้งครรภ์ หลังอาหาร",
     "ALP สูง + GGT ปกติ = กระดูก · GGT ไม่มีในกระดูก",
     "Isolated ALP จากตับ: ท่อตันข้างเดียว แทรกซึม ก้อน PBC ระยะแรก",
     "GGT สูงอย่างเดียว: เหล้า กันชัก warfarin",
     "Delta bilirubin ครึ่งชีวิต ~20 วัน → เหลืองค้างหลังแก้อุดตัน"],
    [mcq(N(10), "A 70-year-old man has bone pain and ALP 650 U/L. GGT, AST, ALT and bilirubin are normal. Which is the most likely source of the ALP?",
         ["Liver infiltration", "Bone", "Early PBC", "Biliary obstruction", "Drug-induced cholestasis"], 1,
         "**ALP สูง + GGT ปกติ** → ALP **ไม่ได้มาจากตับ** เพราะ **GGT ไม่มีในกระดูก** ถ้า ALP มาจากตับ GGT จะสูงตาม\n\nชายสูงอายุปวดกระดูก ALP สูง → **Paget disease** หรือ **มะเร็งแพร่กระจายไปกระดูก (ต่อมลูกหมาก)**",
         "ALP สูง GGT ปกติ = กระดูก", "Isolated ALP", R("Gamma glutamyl transpeptidase")),
     mcq(N(11), "A 40-year-old man taking phenytoin for epilepsy has GGT 210 U/L with normal ALP, AST, ALT and bilirubin. He drinks rarely. What is the most likely explanation?",
         ["Biliary obstruction", "Enzyme induction by phenytoin", "Acute hepatitis", "Primary sclerosing cholangitis", "Bone disease"], 1,
         "สไลด์ **isolated GGT สูง**: **เหล้า · ยา — กันชัก · warfarin** — ยาเหล่านี้ **กระตุ้นการสร้าง GGT** ใน microsome โดยไม่มีโรคตับ\n\nถ้า ALP transaminase และ bilirubin ปกติ ไม่ต้องสืบค้นเพิ่มมาก · ท่อน้ำดีอุดตันจะมี ALP สูงด้วย",
         "GGT สูงอย่างเดียว = เหล้า/ยากระตุ้นเอนไซม์", "Isolated GGT", R("Isolated elevation of GGT")),
    ])

# ───────────────────────────── 7
sec("gi-lft-07", "การสร้างของตับ (PT, albumin) และ bilirubin เด่น",
    "ปัจจัยแข็งตัวสร้างจากตับยกเว้น VIII · factor V/วิตามินเค แยกตับเสียจากขาดวิตามินเค · albumin ครึ่งชีวิต 20 วัน · IB/TB > 0.8 · DB/TB > 0.5", 9,
"""### Prothrombin time (สไลด์)
- **ปัจจัยการแข็งตัวทุกตัวสร้างที่ตับ ยกเว้น factor VIII** (สร้างที่ endothelium) → **ตับวาย factor VIII ปกติหรือสูง** แต่ **DIC ต่ำ**
- **PT ยาวจากตับเสีย vs ขาดวิตามินเค**:
  - **ให้วิตามินเคใต้ผิวหนัง/ทางหลอดเลือด** → PT ดีขึ้นใน 24–48 ชม. = **ขาดวิตามินเค** (ท่อน้ำดีอุดตัน ดูดซึมไขมันไม่ได้ ยาปฏิชีวนะ ขาดอาหาร)
  - **Factor V ไม่ขึ้นกับวิตามินเค** → factor V ต่ำ = **ตับสร้างไม่ได้**
- PT สะท้อนความรุนแรงเร็ว (factor VII ครึ่งชีวิต ~6 ชม.)

### Albumin (สไลด์)
- **ครึ่งชีวิต ~20 วัน** → **ไม่ลดในตับอักเสบเฉียบพลัน** ลดในโรคตับ **กึ่งเฉียบพลันและเรื้อรัง**
- ตับแข็ง: **albumin ลด globulin เพิ่ม** (A/G กลับข้าง) — แต่ไม่จำเพาะ ต้องแยกจากโรคที่ globulin สูงอื่น (เช่น myeloma) · ไตรั่ว ขาดอาหาร ก็ทำให้ albumin ต่ำ

### Bilirubin เด่น (สไลด์)
| อัตราส่วน | ความหมาย |
|---|---|
| **Indirect/total > 0.8** | **unconjugated เด่น** — เม็ดเลือดแดงแตก · **Gilbert** · Crigler–Najjar · ineffective erythropoiesis · resorption ของก้อนเลือด |
| **Direct/total > 0.5** | **โรคตับหรือทางเดินน้ำดี** · (Dubin–Johnson, Rotor ถ้า LFT อื่นปกติ) |

**Gilbert syndrome (เพิ่มเติม — ไม่ได้มาจากสไลด์)**: UGT1A1 ลดลง · indirect bilirubin สูงเล็กน้อย (มักไม่เกิน 4) **เวลาอดอาหาร ป่วย เครียด** · LFT อื่นและ CBC/reticulocyte ปกติ · **ไม่ต้องรักษา**
""",
    ["ปัจจัยแข็งตัวสร้างที่ตับทั้งหมดยกเว้น VIII",
     "PT ดีขึ้นหลังวิตามินเค = ขาดวิตามินเค (อุดตัน) · ไม่ดีขึ้น = ตับสร้างไม่ได้",
     "Albumin ครึ่งชีวิต 20 วัน → ไม่ลดในโรคเฉียบพลัน",
     "IB/TB > 0.8 hemolysis/Gilbert · DB/TB > 0.5 โรคตับ"],
    [mcq(N(12), "A patient with obstructive jaundice from a CBD stone has INR 2.1. After 10 mg IV vitamin K, INR falls to 1.2 within 24 hours. What does this indicate?",
         ["Severe hepatocellular failure", "Vitamin K deficiency from impaired fat absorption, with preserved hepatic synthetic function", "DIC", "Factor VIII deficiency", "Haemophilia"], 1,
         "สไลด์: PT ยาว **ตอบสนองต่อวิตามินเค = ขาดวิตามินเค** — ท่อน้ำดีอุดตัน → ไม่มีน้ำดีไปช่วยดูดซึมวิตามินที่ละลายในไขมัน · **ตับยังสร้างได้**\n\nตับวายรุนแรง PT ยาวและ **ไม่ตอบสนอง** ต่อวิตามินเค · ตรวจ **factor V** (ไม่ขึ้นกับวิตามินเค) ช่วยยืนยันการสร้างของตับ",
         "PT แก้ได้ด้วยวิตามินเค = ขาดวิตามินเค ตับยังดี", "Synthetic function", R("Liver synthetic function")),
     mcq(N(13), "A 22-year-old man notices yellow eyes during a fasting period. Total bilirubin 3.2 mg/dL, direct 0.3 mg/dL. AST, ALT, ALP, CBC and reticulocyte count are normal. What is the most likely diagnosis?",
         ["Haemolytic anaemia", "Gilbert syndrome", "Dubin–Johnson syndrome", "Acute hepatitis A", "Primary biliary cholangitis"], 1,
         "**Indirect/total = 2.9/3.2 ≈ 0.9 (> 0.8)** = unconjugated hyperbilirubinemia · **ไม่มีเม็ดเลือดแดงแตก** (CBC reticulocyte ปกติ) · LFT อื่นปกติ · **เหลืองเวลาอดอาหาร** = **Gilbert syndrome** — ไม่ต้องรักษา\n\nDubin–Johnson เป็น **direct** bilirubin สูง",
         "Indirect เด่น + อดอาหาร + CBC ปกติ = Gilbert", "Unconjugated hyperbilirubinaemia", R("Predominant bilirubin elevations")),
    ])

# ───────────────────────────── 8
sec("gi-lft-08", "รวมรูปแบบ LFT · ไข้กับตัวเหลือง · ขั้นตอนดูแลผู้ป่วยเหลือง",
    "ตารางรูปแบบตามโรค · ไข้ + เหลือง ในไทย: leptospirosis typhoid มาลาเรีย melioidosis cholangitis ฝีตับ · US: ท่อขยาย → ERCP/MRCP · ไม่ขยาย → serology biopsy", 10,
"""### รูปแบบ LFT ตามชนิดโรค (ตารางในสไลด์)
| | **พิษ/ขาดเลือด** | **ไวรัส** | **เหล้า** | **อุดตันสมบูรณ์** | **อุดตันบางส่วน** | **แทรกซึม** |
|---|---|---|---|---|---|---|
| ตัวอย่าง | paracetamol · ischemic | HAV HBV | alcoholic hepatitis | มะเร็งตับอ่อน | hilar CA | วัณโรค มะเร็ง |
| AST/ALT | **50–100×** | **5–50×** | **2–5×** | 1–5× | 1–5× | 1–3× |
| ALP | 1–3× | 1–3× | 1–10× | **2–20×** | 2–10× | **1–20×** |
| Bilirubin | 1–5× | 1–30× | 1–30× | **1–30×** | 1–5× | **มักปกติ** |
| PT | **ยาว ไม่ตอบสนองวิตามินเค** (รุนแรง) | | | **ยาว ตอบสนองวิตามินเค** | | ปกติ |
| Albumin | ลดในโรคกึ่งเฉียบพลัน/เรื้อรัง | | | ปกติ (ลดในตับแข็ง) | | |

### Mixed pattern (สไลด์)
**Transaminase > 2× + ALP > 3×** → **นิ่วกำลังเคลื่อนผ่าน** · **ตับอักเสบจากยา** · overlap syndrome · โรคแทรกซึม · **ตับคั่งเลือด** · SIRS

### ไข้ร่วมกับตัวเหลือง (สไลด์)
| **ลักษณะ hepatitis** | **ลักษณะ cholestasis** |
|---|---|
| AIH · ยา · fulminant hepatitis · ตับอักเสบจากเหล้า | **ท่อน้ำดีอักเสบ (ascending cholangitis)** · **ฝีในตับ** |
| **Typhoidal hepatitis** · **leptospirosis ชนิดเหลือง (Weil)** | **Melioidosis** · วัณโรค · โรคแทรกซึม |
| **มาลาเรีย** · ติดเชื้อที่มีเม็ดเลือดแดงแตก | **Sepsis-induced cholestasis** · ยา · PBC/PSC · AIDS cholangiopathy |
> **Leptospirosis (เพิ่มเติม)** — ลุยน้ำ/ทำนา · ไข้สูง **ปวดน่องมาก ตาแดง (conjunctival suffusion)** · **bilirubin สูงมากแต่ transaminase สูงเพียงเล็กน้อย** · ไตวาย เลือดออกในปอด · รักษา penicillin G/ceftriaxone หรือ doxycycline

### ขั้นตอนดูแลผู้ป่วยเหลือง (สไลด์)
1. **ประวัติ ตรวจร่างกาย LFT** → แยก **hepatitis · mixed (ยา overlap) · cholestasis**
2. Cholestasis → **อัลตราซาวนด์**
   - **ท่อน้ำดีขยาย = obstructive jaundice** → มี **cholangitis → ERCP** · ไม่มี → **CT/MRCP** หาตำแหน่งและสาเหตุ → ERCP/EUS
   - **ท่อไม่ขยาย = medical cholestasis** → serum markers (AMA ฯลฯ) ทบทวนยา sepsis → **เจาะชิ้นเนื้อตับ**
3. Hepatitis → serology ไวรัส ประวัติยาเหล้า (หัวข้อ 3–4)
""",
    ["พิษ/ขาดเลือด 50–100× · ไวรัส 5–50× · เหล้า 2–5×",
     "อุดตัน: ALP และ bilirubin เด่น PT ตอบสนองวิตามินเค · แทรกซึม: ALP สูง bilirubin ปกติ",
     "ไข้ + เหลืองในไทย: leptospirosis typhoid มาลาเรีย melioidosis cholangitis ฝีตับ",
     "เหลืองแบบ cholestatic → US: ขยาย → ERCP/MRCP · ไม่ขยาย → markers/biopsy"],
    [mcq(N(14), "A 35-year-old rice farmer has 5 days of high fever, severe calf pain and conjunctival suffusion. Total bilirubin 14 mg/dL, AST 110 U/L, ALT 85 U/L, creatinine 3.1 mg/dL. Which is the most likely diagnosis?",
         ["Acute hepatitis A", "Leptospirosis (Weil disease)", "Paracetamol toxicity", "Gilbert syndrome", "Primary biliary cholangitis"], 1,
         "สไลด์ fever with jaundice มี **icteric leptospirosis** · เบาะแส: **ชาวนา ไข้สูง ปวดน่องมาก ตาแดง** + **bilirubin สูงมากแต่ transaminase สูงเล็กน้อย** (ไม่สมสัดส่วน) + **ไตวาย** = **Weil disease**\n\nไวรัสตับอักเสบจะมี ALT เป็นพัน · รักษาด้วย **penicillin G หรือ ceftriaxone** (รายไม่รุนแรง doxycycline)\n\n*(ลักษณะทางคลินิกและการรักษาไม่ได้มาจากสไลด์)*",
         "ไข้ ปวดน่อง ตาแดง + bilirubin สูง ALT ต่ำ + AKI = leptospirosis", "Fever with jaundice", R("Fever with jaundice"), NLN + ["2.1.1"]),
     mcq(N(15), "A 60-year-old woman has painless cholestatic jaundice. Ultrasound shows dilated intrahepatic ducts and CBD without a visible stone. She has no fever. What is the most appropriate next step?",
         ["Liver biopsy", "CT abdomen (pancreatic protocol) or MRCP to define the level and cause", "Antimitochondrial antibody only", "Repeat LFT in 6 months", "Start ursodeoxycholic acid"], 1,
         "Algorithm ในสไลด์: **cholestasis → US → ท่อน้ำดีขยาย = obstructive jaundice** · ไม่มี cholangitis → **CT/MRCP** หาระดับและสาเหตุ (นิ่ว มะเร็งรอบ ampulla) แล้วจึง ERCP/EUS เพื่อระบายหรือตัดชิ้นเนื้อ\n\nเจาะชิ้นเนื้อตับและ AMA ใช้เมื่อ **ท่อไม่ขยาย** (medical cholestasis)",
         "ท่อขยาย ไม่มี cholangitis → CT/MRCP", "Jaundice algorithm", R("Jaundice algorithm"), NLN + ["B8.2.4-3(2)"]),
    ], NLN + ["2.1.1"])

# ───────────────────────────── MEQ / OSCE
LECNAME = "Liver function tests (นพ.กิตติ)"
MEQ = [{"id": "GI-LFT-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Jaundice after analgesic overdose — LFT interpretation, paracetamol hepatotoxicity and acute liver failure",
 "vignette": """ผู้ป่วยหญิงไทยอายุ 23 ปี นักศึกษา มาด้วยตาเหลือง อ่อนเพลีย ไข้ต่ำ 3 วัน
PI: 1 สัปดาห์ก่อนทะเลาะกับแฟน กินยาแก้ปวดที่บ้าน "ประมาณ 1 กำมือ" ไม่ทราบชื่อยาแน่ชัด หลังกินคลื่นไส้อาเจียน 1 วันแล้วดีขึ้น 3 วันก่อนเริ่มเหลือง
PE: BT 37.6 C · BP 112/70 · HR 96 · ตาเหลือง ไม่ซีด · ตับโต 3 ซม. ใต้ชายโครงขวา กดเจ็บ · ม้ามโตเล็กน้อย · ไม่มี asterixis
Lab: albumin/globulin 3.4/3.5 g/dL · TB/DB 8/5 mg/dL · AST 3,580 U/L · ALT 2,500 U/L · ALP 230 U/L · INR 1.8 · Cr 0.8 · glucose 82""",
 "questions": [
  {"q": "1. จงแปลผล LFT ของผู้ป่วยรายนี้ (3 คะแนน)",
   "a": """- **Hepatocellular pattern รุนแรง** — AST/ALT สูง **> 40–100 เท่า (marked)** · R ratio สูงมาก (> 5)
- **Bilirubin สูง direct เด่น** (DB/TB > 0.5 = โรคตับ) · ALP สูงเล็กน้อย (< 3 เท่า)
- **การสร้างของตับลดลง: INR 1.8** · albumin ยังปกติเพราะครึ่งชีวิตยาว (โรคเฉียบพลัน)"""},
  {"q": "2. จงให้การวินิจฉัยแยกโรคที่สำคัญ 3 ข้อ และการวินิจฉัยที่น่าจะเป็นที่สุด (3 คะแนน)",
   "a": """- ระดับ **40–100 เท่า** นึกถึง: **ตับอักเสบจาก paracetamol** · **ตับขาดเลือด** (ไม่มีประวัติช็อก) · **ไวรัสตับอักเสบเฉียบพลันรุนแรง** (HAV, HBV, HEV) · อื่น: Wilson (หญิงอายุน้อย), AIH, สมุนไพร
- **น่าจะเป็นที่สุด: ตับอักเสบจาก paracetamol ขนาดสูง** — ประวัติกินยาแก้ปวดจำนวนมาก (ยาสามัญที่หาได้ในบ้าน) · อาการระยะแรกคลื่นไส้ แล้วดีขึ้น ก่อนตับอักเสบวันที่ 2–4 · AST > ALT ในช่วงแรก
- ต้องตรวจ **IgM anti-HAV, HBsAg/IgM anti-HBc, anti-HCV** และ **ระดับ paracetamol** (บอกว่าเคยได้รับ แม้มาช้า) · ceruloplasmin ถ้ายังไม่ชัด"""},
  {"q": "3. จงบอกการรักษาและการเฝ้าระวัง (4 คะแนน)",
   "a": """- **ให้ N-acetylcysteine ทางหลอดเลือดทันที** แม้มาช้ากว่า 24 ชม. และไม่รู้เวลากินแน่ — ยังลดอัตราตายในตับวาย · **ไม่ใช้ Rumack–Matthew nomogram** เพราะไม่รู้เวลาและเกิน 24 ชม.
- เฝ้าระวัง **INR, glucose (น้ำตาลต่ำ), ระดับความรู้สึกตัว (encephalopathy), Cr, pH/lactate, phosphate** ทุก 6–12 ชม.
- หลีกเลี่ยงยากล่อมประสาท · ให้ dextrose ป้องกันน้ำตาลต่ำ
- **ประเมินจิตเวช/ความเสี่ยงฆ่าตัวตาย** เพราะเป็นการกินยาเกินขนาดโดยตั้งใจ"""},
  {"q": "4. เมื่อใดต้องส่งต่อศูนย์ปลูกถ่ายตับ (2 คะแนน)",
   "a": """- **Acute liver failure** = INR ≥ 1.5 + **encephalopathy** ในผู้ที่ไม่มีโรคตับเดิม → ปรึกษาศูนย์ปลูกถ่ายตับตั้งแต่เนิ่น
- **King's College criteria (paracetamol)**: **arterial pH < 7.30** หลังให้สารน้ำ **หรือ** ครบทั้ง 3 ข้อ — **INR > 6.5 · Cr > 3.4 mg/dL · encephalopathy ระดับ 3–4** (lactate สูงช่วยเพิ่มความไว)"""}],
 "ref": ["สไลด์ นพ.กิตติ — LFT case หญิง 23 ปี กินยาแก้ปวด 1 กำมือ", "King's College criteria · acetaminophen toxicity management"],
 "nl": ["B8.3(1)", "2.1.13", "2.3.11-3(7)"], "years": [], "_kind": "meq", "_set": SET}]

OSCE = [{"id": "GI-LFT-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "SAQ – Interpreting liver function test patterns",
 "station": "SAQ (เขียนตอบ) 6 นาที",
 "instruction": """จงบอกรูปแบบความผิดปกติของ LFT และสาเหตุที่น่าจะเป็นที่สุด พร้อมการตรวจเพิ่มเติม 1 อย่าง ของผู้ป่วย 5 รายต่อไปนี้ (ค่าปกติ: AST/ALT < 40 · ALP < 120 · TB < 1.2 U/L หรือ mg/dL)

| ราย | ข้อมูล | TB/DB | AST/ALT | ALP | อื่น ๆ |
|---|---|---|---|---|---|
| A | ชาย 29 ปี กินหอยดิบ เบื่ออาหาร แล้วเหลือง | 15/11 | 1,350/1,525 | 160 | PT 14 วินาที |
| B | ชาย 57 ปี ไข้ 39 °C เหลือง ปวดท้อง 2 วัน | 5/3 | 55/60 | 380 | — |
| C | หญิง 74 ปี ปอดอักเสบได้ยาปฏิชีวนะ แล้วเหลือง | 5/3 | ปกติ | 540 | US ปกติ |
| D | หญิง 30 ปี ตรวจสุขภาพ ไม่มีอาการ | ปกติ | ปกติ | 580 | — |
| E | ชาย 50 ปี ดื่มเหล้าทุกวัน | 2.0/1.2 | 180/70 | 140 | GGT 450 · MCV 105 |""",
 "answer": """| ราย | รูปแบบ | สาเหตุที่น่าจะเป็น | ตรวจต่อ | คะแนน |
|---|---|---|---|---|
| **A** | **Hepatocellular** ALT > AST เป็นพัน | **Acute hepatitis A** | **IgM anti-HAV** (± HBsAg, IgM anti-HBc) | 2 |
| **B** | **Cholestatic** DB เด่น ALP > 3× + ไข้ | **Ascending cholangitis** / ฝีในตับ | **US ช่องท้อง** + hemoculture | 2 |
| **C** | **Cholestatic** ท่อไม่ขยาย | **Sepsis-induced cholestasis** หรือยาปฏิชีวนะ | ทบทวนยา · ติดตาม LFT เมื่อติดเชื้อดีขึ้น | 2 |
| **D** | **Isolated ALP** | ตั้งครรภ์ · กระดูก · PBC ระยะแรก · แทรกซึม | **GGT หรือ 5'-NT** (± urine hCG) | 2 |
| **E** | **AST/ALT > 2** AST < 300 · GGT สูง | **Alcohol-associated liver disease** | US ตับ ประเมินพังผืด · AUDIT | 2 |

**หลักที่ต้องแสดง**: แยก hepatocellular vs cholestatic ก่อน · ระดับ transaminase บอกกลุ่มสาเหตุ · cholestasis → US ดูท่อ · isolated ALP → GGT""",
 "ref": ["สไลด์ นพ.กิตติ — LFT cases"],
 "nl": ["B8.3(1)", "2.1.13", "2.3.11(2)", "B8.2.2-3(6)"], "years": [], "_kind": "meq", "_set": SET}]

LECTURE = {
 "lec": LEC, "date": "พฤ. 29 ต.ค.",
 "title": "Liver function tests",
 "subtitle": "5 รูปแบบ LFT และ R ratio · ระดับ transaminase และ AST/ALT · ขาดเลือด paracetamol AIH Wilson · cholestasis PBC sepsis · ALP GGT · PT albumin bilirubin · ไข้กับเหลือง และขั้นตอนดูแลผู้ป่วยเหลือง",
 "objectives": [
   "บอกส่วนประกอบของ LFT แยก 5 รูปแบบความผิดปกติ และคำนวณ R ratio",
   "ใช้ระดับ transaminase และอัตราส่วน AST/ALT จำกัดกลุ่มสาเหตุ",
   "ไล่หาสาเหตุ acute hepatitis และจดจำตับขาดเลือด paracetamol AIH และ Wilson จาก LFT",
   "แยก obstructive จาก medical cholestasis และรู้จัก PBC",
   "แปลผล ALP, GGT, 5'-NT และหาสาเหตุของ ALP หรือ GGT สูงอย่างเดียว",
   "ประเมินการสร้างของตับด้วย PT และ albumin และแยกชนิดของ hyperbilirubinemia",
   "วางขั้นตอนดูแลผู้ป่วยเหลืองและไข้ร่วมกับตัวเหลือง"],
 "nlGap": "เกณฑ์ฯ มีรหัส `นล. B8.3(1)` Liver function test, amylase and lipase · `2.1.13` Jaundice · `B8.3(2)` Viral hepatitis serologies · `2.3.11-3(7)` Hepatic failure แต่ **ไม่มีรหัสเฉพาะของ PBC, AIH, Wilson หรือ paracetamol hepatotoxicity** และสไลด์ปี 2563 ไม่ได้กล่าวถึงการรักษา จึงอ้างอิงแนวทางด้านล่าง",
 "guidelines": [
   "**ACG Clinical Guideline: Evaluation of abnormal liver chemistries (2017)** — R ratio และขั้นตอนสืบค้น (อาจารย์อ้างในสไลด์)",
   "**EASL Clinical Practice Guidelines on cholestatic liver diseases / PBC (2024)** — UDCA · PPAR agonists elafibranor และ seladelpar (FDA 2024)",
   "**AASLD Practice Guidance: Wilson disease (2022)** — ceruloplasmin · chelation · Leipzig score",
   "**EASL Clinical Practice Guidelines on autoimmune hepatitis (2025)** และ simplified criteria IAIHG 2008",
   "**การรักษาพิษ paracetamol** — Rumack–Matthew nomogram · IV NAC · King's College criteria"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# กระจายตำแหน่งคำตอบของข้อใหม่ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น)
_slot = 0
for s_ in S:
    for it in s_["items"]:
        tgt = [3, 0, 4, 2, 1][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", SET + ".json")
data = json.load(open(path, encoding="utf-8"))
data = [l for l in data if l.get("lec") != LEC] + [LECTURE]
data.sort(key=lambda l: tuple(int(x) for x in l["lec"].split("/")[::-1]))
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

added = link_mock(SET, LEC, {"gi-lft-06": ["MOCK-150"]})

d = json.load(open(path, encoding="utf-8"))
L = [l for l in d if l["lec"] == LEC][0]
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = {c for s_ in L["sections"] for c in s_["nl"]} | {c for s_ in L["sections"] for i in s_["items"] for c in i.get("nl", [])} | {c for m in L["meq"] + L["osce"] for c in m["nl"]}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == SET: m["lectureCount"] = len(d)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | ข้อใหม่ %d + mock %d | meq %d | osce %d | nl %d" % (len(S), sum(len(s_["items"]) for s_ in S), added, len(MEQ), len(OSCE), len(codes)))
