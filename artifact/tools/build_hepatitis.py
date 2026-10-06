#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Acute and chronic hepatitis (รศ.พิเศษ นพ.เฉลิมรัฐ) → data/gi.json (ชุดใหม่ GI & Hepatology)
ต้นฉบับ: Drive 1X6QMVuq2GWT3SLbV9VactnQ11MVtml98 · บรรยาย จ. 12 ต.ค. 2569 · โน้ต slides/hepatitis_notes.md
ไม่มีในคลัง Ward Drill ระดับคาบ — ผูกข้อ Mock M09 ที่ตรงเรื่อง (MOCK-149, MOCK-153)
อัปเดต: WHO 2024 / EASL 2025 / AASLD-IDSA 2025 (HBV) · ACG 2024 (ALD) · EASL–EASD–EASO 2024 + resmetirom/semaglutide (MASLD)"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_bank import link

SET = "gi"
NLN = ["2.3.1(1)", "B8.2.2-3(5)"]
CHR = ["2.3.1-3(3)", "B8.2.2-3(5)"]
SRC = "สไลด์ อ.เฉลิมรัฐ — Acute and chronic hepatitis (2026)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None, src=SRC):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": src,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "GI-HEP-MCQ-%02d" % n
R = lambda p: ["สไลด์ อ.เฉลิมรัฐ — " + p]

# ───────────────────────────── 1
sec("gi-hep-01", "ตับอักเสบเฉียบพลัน — อ่าน ALT/AST และแยกสาเหตุ",
    "ส่วนใหญ่ ALT > AST · AST สูงกว่าหลายเท่าให้นึกถึงนอกตับหรือเหล้า · bilirubin กับ PT บอกความรุนแรง · encephalopathy = ตับวาย", 9,
"""### เอนไซม์บอกอะไร
เซลล์ตับเสียหายจาก **ไวรัส ยา สารพิษ ภูมิคุ้มกัน หรือขาดเลือด** → เอนไซม์รั่วออกมา
| เอนไซม์ | อยู่ที่ไหน | ค่าครึ่งชีวิต |
|---|---|---|
| **ALT** | cytoplasm ของเซลล์ตับเป็นหลัก — **จำเพาะต่อตับ** | **~47 ชม.** |
| **AST** | cytoplasm (~17 ชม.) + **mitochondria (~87 ชม.)** — พบใน **กล้ามเนื้อ หัวใจ เม็ดเลือดแดง** ด้วย | สั้นกว่า |

- **ตับอักเสบส่วนใหญ่ ALT > AST**
- **AST สูงกว่า ALT หลายเท่า** (โน้ตในห้อง) → คิดถึง **ต้นเหตุนอกตับ** (กล้ามเนื้อสลาย หัวใจ เม็ดเลือดแดงแตก) หรือ **เหล้า** · ช่วงแรกของ **ischemic hepatitis**
- ขาดเลือดไม่มีการอักเสบ (โน้ตในห้อง) — ค่าขึ้นสูงมากแต่ลงเร็ว

### ความรุนแรง
| ระดับ | สิ่งที่พบ |
|---|---|
| มีอาการ | คล้ายไข้หวัด ไข้ต่ำ อึดอัดชายโครงขวา คลื่นไส้อาเจียน |
| **Severe acute liver injury** | **bilirubin สูง + PT ยาว** |
| **Acute liver failure** | **มี encephalopathy** (ร่วมกับ INR ≥ 1.5 ในคนที่ไม่มีโรคตับเดิม) |
**กับดัก** (โน้ตในห้อง) — **ไข้สูงหนาวสั่น ปวดชายโครงขวามาก + เหลือง → คิด cholangitis ก่อน** ไม่ใช่ไวรัสตับอักเสบ

### สาเหตุ
| พบบ่อย | พบน้อยกว่า |
|---|---|
| **ไวรัสตับอักเสบ (hepatotropic A–E)** | **Ischemic hepatitis** |
| **ยา** (รวมสมุนไพร) | **Autoimmune hepatitis** |
| **แอลกอฮอล์** | **Wilson's disease** |
| | **ติดเชื้อทั้งระบบ** — ไข้เลือดออก ไข้รากสาดใหญ่ ไทฟอยด์ เลปโตสไปโรซิส · HSV CMV EBV · COVID-19 |
""",
    ["ALT จำเพาะต่อตับ · AST มีในกล้ามเนื้อ หัวใจ เม็ดเลือดแดงด้วย",
     "ตับอักเสบส่วนใหญ่ ALT > AST · AST >> ALT → นอกตับ เหล้า หรือขาดเลือดช่วงแรก",
     "bilirubin + PT สูง = severe · encephalopathy = acute liver failure",
     "ไข้สูงหนาวสั่น + RUQ pain มาก + เหลือง → cholangitis"],
    [mcq(N(1), "A 30-year-old man has AST 1,850 U/L and ALT 210 U/L after a prolonged generalised seizure. Bilirubin is normal. What is the most likely source of the raised AST?",
         ["Acute viral hepatitis", "Skeletal muscle injury (rhabdomyolysis)", "Autoimmune hepatitis", "Chronic hepatitis B flare", "Cholestatic drug injury"], 1,
         "**AST สูงกว่า ALT หลายเท่า** (โน้ตในห้อง) → คิดถึง **ต้นเหตุนอกตับ** · AST อยู่ในกล้ามเนื้อลายมาก ชักนานทำให้ **กล้ามเนื้อสลาย** → ตรวจ **CK** ยืนยัน\n\nไวรัสตับอักเสบและ AIH มักเป็น **ALT > AST** · AST ลงเร็วกว่า ALT เพราะค่าครึ่งชีวิตสั้นกว่า",
         "AST >> ALT + CK สูง = กล้ามเนื้อ ไม่ใช่ตับ", "AST vs ALT", R("Approach to acute hepatitis"), ["2.1.13", "B8.3(1)"]),
    ], NLN + ["2.1.13", "B8.3(1)"])

# ───────────────────────────── 2
sec("gi-hep-02", "ไวรัสตับอักเสบ A ถึง E",
    "A, E ทางปาก (เฉียบพลัน) · B, C, D ทางเลือด/เพศ (เรื้อรังได้) · D ต้องมี B · E ในไทยมาจากหมู", 8,
"""| | **A** | **B** | **C** | **D** | **E** |
|---|---|---|---|---|---|
| สารพันธุกรรม | RNA | **DNA** | RNA | RNA | RNA |
| ทางติดต่อ | **ทางปาก (fecal–oral)** | **เลือด เพศสัมพันธ์ แม่สู่ลูก** | **เลือด** (ฉีดยา รับเลือดก่อน 2535) | เลือด — **ติดได้เฉพาะคนที่มี HBsAg** | **ทางปาก** |
| ระยะฟักตัว | **2–4 สัปดาห์** | **4–24 สัปดาห์** | **2–24 สัปดาห์** | — | **2–10 สัปดาห์** |
| เรื้อรัง | ไม่ | **ได้** | **ส่วนใหญ่เรื้อรัง** | ได้ (ร่วมกับ B) | ไม่ (ยกเว้นภูมิคุ้มกันบกพร่อง) |
| ข้อสังเกต | ไปต่างประเทศ · MSM | — | — | — | **ในไทยมาจากเนื้อหมูที่ไม่สุก** (โน้ตในห้อง) · อินเดีย |

**ไวรัสที่พบบ่อยที่สุดในตับอักเสบเฉียบพลัน = HBV และ HAV** · HEV HCV HDV พบน้อยกว่าหรือในกลุ่มเสี่ยงเฉพาะ

**ทำไม B เรื้อรังได้ แต่ A กับ E ไม่** — HBV สร้าง **cccDNA** เก็บไว้ในนิวเคลียสของเซลล์ตับ ส่วน HAV/HEV ถูกกำจัดหมดด้วยภูมิคุ้มกัน
""",
    ["A, E ทางปาก · B แม่สู่ลูก เพศ เลือด · C เลือด · D ต้องมี HBsAg",
     "HBV เป็น DNA virus ตัวเดียว · ที่เหลือเป็น RNA",
     "ฟักตัว: A 2–4 · E 2–10 · B 4–24 · C 2–24 สัปดาห์",
     "HEV ในไทยมาจากหมูไม่สุก"],
    [mcq(N(2), "Hepatitis D virus can infect only which patients?",
         ["Anyone exposed to contaminated food", "Patients who are HBsAg-positive", "Patients with chronic hepatitis C", "Patients vaccinated against hepatitis B", "Pregnant women only"], 1,
         "**HDV เป็นไวรัสไม่สมบูรณ์** ต้องใช้ **HBsAg** เป็นเปลือกหุ้ม → ติดได้เฉพาะคนที่มี HBsAg (ติดพร้อมกัน co-infection หรือซ้อน superinfection)\n\nดังนั้น **วัคซีนตับอักเสบบีป้องกันตับอักเสบดีได้ด้วย**",
         "HDV ติดได้เฉพาะคนที่ HBsAg บวก", "Hepatitis D", R("Viral hepatitis A to E")),
    ])

# ───────────────────────────── 3
sec("gi-hep-03", "ตับอักเสบจากไวรัสเฉียบพลัน — อาการ และการอ่านผลเลือด HBV",
    "อาการนำก่อนเหลือง · ไข้หายเมื่อเหลือง · ALT พุ่ง 1,000–4,000 · สงสัย acute HBV เจาะ HBsAg + anti-HBc IgM", 11,
"""### ภาพทางคลินิก
- **อาการนำ (prodrome)** คล้ายไข้หวัด อ่อนเพลีย คลื่นไส้อาเจียน **ก่อนตัวเหลือง**
- **ไข้หายเมื่อเริ่มเหลือง** — ถ้าเหลืองแล้วยังไข้สูงให้คิดถึงโรคอื่น
- **ALT > AST** มักไม่เกิน 2,000–3,000 · ยอดสูงสุดราว **1,000–4,000 U/L**
- **ระดับ ALT ไม่สัมพันธ์กับความรุนแรง** · หลังยอดลดลง **50–70% ต่อสัปดาห์**
- **Bilirubin** ขึ้นสูงสุด **หลัง ALT** (ไม่ค่อยเกิน 20 มก./ดล.) ลด **~50% ต่อสัปดาห์**
- **Delta-bilirubin** — bilirubin ที่จับกับ albumin (ค่าครึ่งชีวิต ~21 วัน ขับทางไตไม่ได้) → **ตัวเหลืองหายช้ากว่าเอนไซม์**

### การตรวจที่ส่ง
| สงสัย | ส่ง |
|---|---|
| HAV | **anti-HAV IgM** |
| **HBV เฉียบพลัน** | **HBsAg + anti-HBc IgM** (โน้ตในห้อง: สงสัย acute เจาะสองตัวนี้พอ) |
| HEV / HCV (บางราย) | anti-HEV IgM · HCV RNA |
**กับดัก** — **HBsAg อาจเป็นลบ 10–20% ตอนมาโรงพยาบาล** (ร่างกายกำจัด HBsAg เร็ว) → **anti-HBc IgM** จึงจำเป็น

### ความหมายของผลเลือด HBV
| ผล | ความหมาย |
|---|---|
| **HBsAg** | **มีเชื้ออยู่** — เฉียบพลันหรือเรื้อรัง (เรื้อรังถ้าบวก > 6 เดือน) |
| **anti-HBc IgM** | **ติดเชื้อเฉียบพลัน/ใหม่ภายใน 6 เดือน** · แต่ **บวกได้ถึง 50% ใน HBV เรื้อรังที่กำเริบ (flare)** |
| **anti-HBc IgG** | **เคยติดเชื้อ** |
| **HBeAg** | ไวรัสแบ่งตัวมาก **ติดต่อง่าย** |
| **anti-HBe** | แบ่งตัวน้อย (ยกเว้น **precore mutant** ที่พบมากในอายุ > 45 ปี) |
| **anti-HBs ≥ 10 IU/L** | **มีภูมิคุ้มกัน** |

### รูปแบบที่ต้องอ่านให้ได้
| HBsAg | anti-HBc | anti-HBs | แปลผล |
|---|---|---|---|
| − | − | − | ไม่เคยติด ไม่มีภูมิ → **ฉีดวัคซีน** |
| − | − | **+** | **ภูมิจากวัคซีน** |
| − | **+ (IgG)** | **+** | **เคยติดและหายแล้ว** |
| **+** | **+ (IgM)** | − | **ติดเชื้อเฉียบพลัน** |
| **+** | **+ (IgG)** | − | **ติดเชื้อเรื้อรัง** |
| − | **+** | − | **isolated anti-HBc** — หายแล้วแต่ anti-HBs ลด · window period · หรือ occult HBV → ส่ง HBV DNA ถ้ามีเหตุ |
""",
    ["Prodrome → เหลือง · ไข้หายเมื่อเหลือง",
     "ALT ยอด 1,000–4,000 ไม่สัมพันธ์ความรุนแรง · bilirubin ยอดทีหลัง",
     "สงสัย acute HBV: HBsAg + anti-HBc IgM (HBsAg ลบได้ 10–20%)",
     "anti-HBc IgM บวกได้ใน chronic HBV flare",
     "anti-HBs ≥ 10 = มีภูมิ · anti-HBc IgG + anti-HBs = หายแล้ว"],
    [mcq(N(3), "A 26-year-old man has jaundice, ALT 2,400 U/L and suspected acute hepatitis B. HBsAg is negative. Which test is most important to send next?",
         ["Anti-HBs", "HBeAg", "Anti-HBc IgM", "Anti-HBc IgG", "HBV genotype"], 2,
         "สไลด์: **HBsAg อาจเป็นลบ 10–20% ของ acute hepatitis B ตอนมาโรงพยาบาล** เพราะร่างกายกำจัด HBsAg ได้เร็ว (window) → **anti-HBc IgM** เป็นตัวยืนยันการติดเชื้อเฉียบพลัน\n\nโน้ตในห้อง: **สงสัย acute เจาะแค่ HBsAg + anti-HBc IgM** · anti-HBs บอกภูมิคุ้มกัน · HBeAg บอกการแบ่งตัว · anti-HBc IgG บอกเคยติด",
         "HBsAg ลบไม่ตัด acute HBV → anti-HBc IgM", "Acute HBV serology", R("Serological markers for HBV"), NLN + ["B8.3(2)"]),
     mcq(N(4), "A health-care worker's results: HBsAg negative, anti-HBc negative, anti-HBs 150 IU/L. What is the interpretation?",
         ["Acute HBV infection", "Chronic HBV infection", "Immunity from vaccination", "Resolved past infection", "Occult HBV infection"], 2,
         "**anti-HBs บวกเดี่ยว ๆ (anti-HBc ลบ) = ภูมิคุ้มกันจากวัคซีน** · วัคซีนมีแต่ HBsAg จึงกระตุ้นได้เฉพาะ anti-HBs ไม่เคยเห็นแกนไวรัส (core) จึงไม่มี anti-HBc\n\nถ้า **anti-HBc บวกด้วย** = เคยติดเชื้อและหายแล้ว · anti-HBs ≥ 10 IU/L ถือว่ามีภูมิ",
         "anti-HBs + และ anti-HBc − = ภูมิจากวัคซีน", "HBV serology patterns", R("Serological markers for HBV"), NLN + ["B8.3(2)"]),
    ], NLN + ["2.1.13", "B8.3(2)"])

# ───────────────────────────── 4
sec("gi-hep-04", "พยากรณ์โรคและการดูแล acute viral hepatitis",
    "ผู้ใหญ่ติด HBV หายเอง > 95% · รักษาประคับประคอง · ให้ยาต้านไวรัสใน acute HBV รุนแรง · รู้จัก acute liver failure", 8,
"""### พยากรณ์โรค (สไลด์)
| | |
|---|---|
| **Hepatitis A** | ตายรวม **0.3%** · ตับวายและชนิด cholestatic พบมากใน **ผู้สูงอายุ** และ **ผู้มีโรคตับเดิม** (โดยเฉพาะ HBV, HCV) |
| **Hepatitis B เฉียบพลัน** | ตายรวม **1%** · ถ้าเป็นตับวายรอดเพียง **~20%** · **ผู้ใหญ่หายเอง > 95%** — อาการดีขึ้นใน 2–3 เดือน HBsAg หายใน 3–6 เดือน |

### การดูแล (สไลด์)
**ประคับประคอง**
- **ทำกิจวัตรได้ตามที่ไหว** ไม่ต้องนอนพักตลอด
- **ดื่มน้ำมาก ๆ**
- **งดเหล้า ยาที่เป็นพิษต่อตับ ยานอนหลับ และยากลุ่ม narcotic** (ตับขับยาไม่ได้ และบดบังอาการ encephalopathy)

**ยาต้านไวรัส**
- **HAV — ไม่มีบทบาท**
- **Acute HBV ที่รุนแรง** — **ควรพิจารณา** (เช่น **INR > 1.5, bilirubin > 3–10 มก./ดล.**) · ใช้ nucleos(t)ide analogue (เช่น tenofovir หรือ entecavir)

### Acute liver failure — ต้องจับให้ได้
**INR ≥ 1.5 + hepatic encephalopathy** ภายใน 26 สัปดาห์ ในคนที่ไม่มีโรคตับเดิม (โน้ตในห้อง: ดู encephalopathy)
→ **ส่งต่อศูนย์ปลูกถ่ายตับทันที** · หาสาเหตุที่มียาแก้ (**paracetamol → N-acetylcysteine** · HBV → ยาต้านไวรัส · AIH → steroid · Wilson → พิจารณาปลูกถ่าย)
""",
    ["Acute HBV ในผู้ใหญ่หายเอง > 95% · HAV ตาย 0.3% (ผู้สูงอายุ/มีโรคตับเดิมเสี่ยง)",
     "ดูแล: ทำกิจวัตรตามไหว ดื่มน้ำ งดเหล้า ยาพิษตับ ยานอนหลับ",
     "ยาต้านไวรัสใน acute HBV รุนแรง (INR > 1.5, bilirubin > 3–10)",
     "Acute liver failure = INR ≥ 1.5 + encephalopathy → ส่งศูนย์ปลูกถ่าย"],
    [mcq(N(5), "A previously healthy 34-year-old woman with acute hepatitis B has bilirubin 14 mg/dL and INR 1.9 but is fully alert. What is the most appropriate management?",
         ["Supportive care only; antivirals have no role in acute HBV", "Start a nucleos(t)ide analogue such as tenofovir and monitor closely for liver failure",
          "Start prednisolone", "Start interferon", "Discharge with follow-up in 6 months"], 1,
         "สไลด์: **ยาต้านไวรัสควรพิจารณาใน acute severe hepatitis B (เช่น INR > 1.5, bilirubin > 3–10 มก./ดล.)** → ใช้ **nucleos(t)ide analogue** เช่น tenofovir\n\nเฝ้าระวัง **encephalopathy** อย่างใกล้ชิด — ถ้าเกิดขึ้นคือ **acute liver failure** ต้องส่งศูนย์ปลูกถ่ายตับ · **interferon ห้ามใช้** ในตับอักเสบรุนแรง · steroid ไม่มีบทบาท",
         "Acute HBV รุนแรง (INR > 1.5) → ยาต้านไวรัส", "Antiviral in severe acute HBV", R("Management of acute viral hepatitis"), NLN + ["2.3.11-3(7)"]),
    ], NLN + ["2.3.11-3(7)", "B8.2.5-3(1)"])


# ───────────────────────────── 5
sec("gi-hep-05", "ตับอักเสบจากแอลกอฮอล์",
    "ดื่มหนักต่อเนื่อง · AST/ALT > 2 แต่ AST ไม่เกิน 400 · GGT MCV สูง · ครึ่งหนึ่งมีตับแข็งแล้ว", 9,
"""### ภาพทางคลินิก (สไลด์)
- **ดื่มหนักและยังดื่มอยู่** (> 30 ก./วัน)
- **ไข้ ตัวเหลือง เบื่ออาหาร ปวดชายโครงขวา** · ตับโตกดเจ็บ · ท้องมาน (~30%) · สับสน
- **ราวครึ่งหนึ่งมีตับแข็งแล้ว** · อาจเห็น **spider naevi, palmar erythema** (โน้ตในห้อง)

### เบาะแสจากผลเลือด
| เบาะแส | กลไก |
|---|---|
| **AST/ALT > 2** | แอลกอฮอล์ทำให้ **mitochondrial AST** รั่วออกมา + **ขาด pyridoxine (B6)** ซึ่งต้องใช้ในการทำงานของ ALT → ALT ต่ำกว่าที่ควร |
| **AST ไม่เกิน ~400 U/L** | **ถ้าเกิน 400 ให้หาสาเหตุอื่นร่วม** (โน้ตในห้อง) — ไวรัส ยา paracetamol ขาดเลือด |
| **GGT สูง · MCV สูง** | เหนี่ยวนำเอนไซม์ · พิษต่อไขกระดูกและขาด folate |

### ดื่มเท่าไรจึงเรียกว่ามาก (สไลด์)
**1 standard drink ≈ 14 ก. แอลกอฮอล์** = เบียร์ 360 มล. (4–6%) · ไวน์ 150 มล. (10–15%) · เหล้า/เหล้าขาว 45 มล. (36–40%)
| | |
|---|---|
| **ดื่มประจำมากเกิน** | **> 20 ก./วัน ในหญิง · > 30 ก./วัน ในชาย** (> 14 / > 21 drinks ต่อสัปดาห์) |
| **ดื่มหนักครั้งเดียว (binge)** | **≥ 5 drinks (ชาย) · ≥ 4 drinks (หญิง) ต่อครั้ง** |
ต้อง **ซักให้ละเอียด** ว่าดื่มอะไร ปริมาณเท่าไร บ่อยแค่ไหน (โน้ตในห้อง)

### ธรรมชาติของโรค (ACG 2024)
ดื่มหนัก → **ไขมันพอกตับ 90–95%** → **ตับอักเสบจากแอลกอฮอล์ 20–35%** · **พังผืด 20–40%** → **ตับแข็ง 8–20%** → **มะเร็งตับ 3–10%**
ปัจจัยเสี่ยง: **หญิง · ปริมาณ · อ้วน · ยีน PNPLA3 · สูบบุหรี่ · ไวรัสตับอักเสบร่วม** (กาแฟเป็นปัจจัยป้องกัน)

### การรักษา (ACG 2024 — ไม่อยู่ในสไลด์)
- **หยุดดื่ม** สำคัญที่สุด · โภชนาการ · ป้องกัน alcohol withdrawal
- **รุนแรง** (Maddrey discriminant function ≥ 32 หรือ MELD > 20) ไม่มีข้อห้าม → **prednisolone 40 มก./วัน 28 วัน** · ประเมิน **Lille score วันที่ 7** ถ้าไม่ตอบสนอง (> 0.45) หยุดยา
""",
    ["Alcoholic hepatitis: AST/ALT > 2 · AST ไม่เกิน 400 · GGT, MCV สูง",
     "AST > 400 ในคนดื่ม → หาสาเหตุอื่นร่วม",
     "1 standard drink ≈ 14 ก. · มากเกิน > 20 ก./วัน หญิง > 30 ก./วัน ชาย",
     "Binge ≥ 5 ชาย / ≥ 4 หญิง ต่อครั้ง",
     "รุนแรง (MDF ≥ 32): prednisolone 40 มก. 28 วัน + หยุดดื่ม"],
    [mcq(N(6), "A 48-year-old man who drinks a bottle of spirits daily has jaundice, fever and tender hepatomegaly. AST 1,250 U/L and ALT 980 U/L. What should you conclude?",
         ["Typical alcoholic hepatitis", "Look for an additional cause such as viral hepatitis, paracetamol toxicity or ischaemia, because AST rarely exceeds about 400 U/L in alcoholic hepatitis",
          "Wilson's disease is excluded", "Start prednisolone immediately without further tests", "This pattern proves chronic hepatitis C"], 1,
         "สไลด์: alcoholic hepatitis มี **AST/ALT > 2 และ AST สูงสุดมักไม่เกิน 400 U/L** · โน้ตในห้อง: **ถ้ามากกว่า 400 น่าจะมีสาเหตุอื่นร่วม**\n\nผู้ป่วยรายนี้ AST เป็นพันและ ALT สูงใกล้กัน → ต้องหา **ไวรัสตับอักเสบ · พิษ paracetamol (คนดื่มเหล้าเสี่ยงพิษ paracetamol แม้ขนาดปกติ) · ขาดเลือด** ก่อนสรุปว่าเป็นจากเหล้าอย่างเดียว",
         "AST > 400 ในคนดื่มเหล้า → มีสาเหตุอื่นร่วม", "Alcoholic hepatitis pattern", R("Alcoholic hepatitis"), ["2.3.11(2)", "B8.2.5(3)"]),
    ], ["2.3.11(2)", "B8.2.5(3)", "2.3.19(6)"], SRC + " · ACG 2024")

# ───────────────────────────── 6
sec("gi-hep-06", "ตับอักเสบจากยาและสมุนไพร (DILI)",
    "ยาแผนปัจจุบันและสมุนไพร · ชนิด direct, idiosyncratic, immunoallergic · ระยะแฝง 4 วันถึง 8 สัปดาห์ · วินิจฉัยโดยแยกโรคอื่น", 7,
"""### กลไกสามแบบ (สไลด์)
| แบบ | ลักษณะ | ตัวอย่าง |
|---|---|---|
| **Direct toxic** | ขึ้นกับขนาดยา คาดเดาได้ | **paracetamol** |
| **Idiosyncratic** | ไม่ขึ้นกับขนาด คาดเดาไม่ได้ | **sulfa · phenytoin · carbamazepine · PTU · ยาวัณโรค** |
| **Immunoallergic** | มี **ผื่น eosinophil สูง** ไข้ | **phenytoin · allopurinol · nevirapine** |

- **รวมทั้งยาแผนปัจจุบันและสมุนไพร** — ต้องถามเสมอ
- **ระยะแฝงมัก 4 วันถึง 8 สัปดาห์** หลังเริ่มยา
- รูปแบบผลตับ **หลากหลาย** — hepatocellular · cholestatic · mixed (ดูวิธีคำนวณ R ratio ในคาบ Liver function tests)
- **วินิจฉัยด้วยประวัติละเอียด แยกสาเหตุอื่น และดีขึ้นหลังหยุดยา**
- ข้อมูลล่าสุดของยาแต่ละตัว: **LiverTox (livertox.nih.gov)**

**ป้องกันได้บางตัว** (โน้ตในห้อง) — **allopurinol ตรวจ HLA-B5801 ก่อนให้** (ป้องกัน SJS/TEN และ DRESS ที่มีตับอักเสบ)
""",
    ["DILI: direct (paracetamol) · idiosyncratic (anti-TB, phenytoin, CBZ, PTU, sulfa) · immunoallergic (allopurinol, nevirapine)",
     "ระยะแฝง 4 วัน–8 สัปดาห์ · ถามสมุนไพรเสมอ",
     "วินิจฉัย: ประวัติ + แยกโรคอื่น + ดีขึ้นหลังหยุดยา · LiverTox",
     "Allopurinol → ตรวจ HLA-B5801 ก่อน"],
    [mcq(N(7), "Three weeks after starting allopurinol, a man develops fever, rash, eosinophilia and ALT 640 U/L. Which mechanism of drug-induced liver injury is most likely?",
         ["Direct dose-dependent toxicity", "Immunoallergic hypersensitivity", "Ischaemic hepatitis", "Steatosis from mitochondrial toxicity", "Cholestasis from bile salt export pump inhibition"], 1,
         "สไลด์: **immunoallergic DILI มีผื่นและ eosinophil สูง** — ตัวอย่างคือ **phenytoin, allopurinol, nevirapine** · ระยะแฝงเข้ากัน (4 วัน–8 สัปดาห์)\n\nต้อง **หยุดยาทันที** และระวัง DRESS · ป้องกันได้ด้วยการ **ตรวจ HLA-B5801 ก่อนให้ allopurinol** (โน้ตในห้อง) · direct toxic แบบขึ้นกับขนาดคือ paracetamol",
         "DILI + ผื่น + eosinophil = immunoallergic", "DILI mechanisms", R("Drug-induced liver injury")),
    ])

# ───────────────────────────── 7
sec("gi-hep-07", "สาเหตุที่พบน้อยแต่ห้ามพลาด: ischemic hepatitis, AIH, Wilson",
    "ขาดเลือด: ALT เป็นหมื่นแล้วลงใน 72 ชม. · AIH: หญิง globulin สูง ANA ASMA · Wilson: hemolysis ALP ต่ำ ALP/TB < 2", 10,
"""### Ischemic hepatitis (สไลด์)
- ประวัติ **ช็อก เลือดออกมาก ความดันต่ำ** (30–50%) · **ผู้สูงอายุ โรคหัวใจ ICU**
- **ALT/AST สูงมาก (> 10,000)** · **AST > ALT ช่วงแรก**
- **bilirubin ปกติหรือสูงเล็กน้อย** · PT ยาวชั่วคราว
- **ALT ลดลงเร็วภายใน 72 ชม.** — เพราะไม่มีการอักเสบต่อเนื่อง (โน้ตในห้อง: ไม่ค่อยเหลือง ลงเร็ว)

### Autoimmune hepatitis (AIH)
- **หญิงวัยกลางคนหรือวัยรุ่น** · เป็นได้ทั้งเฉียบพลัน เรื้อรัง หรือตับแข็ง · อ่อนเพลีย ปวดข้อ ปวดกล้าม เหลือง
- เบาะแส: **โรคภูมิคุ้มกันอื่นร่วม (ถึง 40%)** เช่น thyroiditis, RA · **ตับอักเสบเฉียบพลันแต่มีอาการแสดงของโรคตับเรื้อรัง** · **globulin สูง (> 1.5 × ULN)**
- แอนติบอดี: **ANA · ASMA (anti-smooth muscle)** · seronegative < 10% (แต่สูงถึง 30–40% ใน AIH เฉียบพลัน/fulminant)
- รักษา: **prednisolone ± azathioprine** (ตามแนวทาง)

### Wilson's disease
- **อายุ 20–40 ปี** · ตับอักเสบเฉียบพลัน เรื้อรัง หรือตับแข็ง
- **KF ring (~50%)** · อาการทางสมอง: **extrapyramidal** หรือ **จิตเวช**
- **ตับอักเสบรุนแรงเฉียบพลันร่วมกับเม็ดเลือดแดงแตกในหลอดเลือด** — ทองแดงที่ปล่อยออกมาจากเซลล์ตับที่ตายทำลายเม็ดเลือดแดง
- **AST > ALT (มัก < 1,000) · ALP ต่ำ · ALP/total bilirubin < 2**
- Lab: **ceruloplasmin < 20 มก./ดล. · ทองแดงในปัสสาวะ 24 ชม. > 40 µg** · ในตับวายเฉียบพลัน ceruloplasmin/ทองแดงในเลือดอาจหลอกได้
- Wilson เฉียบพลันรุนแรงมักต้อง **ปลูกถ่ายตับ**
""",
    ["Ischemic: ALT > 10,000 · bilirubin ไม่ค่อยสูง · ลดเร็วใน 72 ชม.",
     "AIH: หญิง · autoimmune ร่วม · globulin > 1.5×ULN · ANA, ASMA",
     "Wilson: 20–40 ปี · KF ring · hemolysis · ALP ต่ำ · ALP/TB < 2",
     "Wilson: ceruloplasmin < 20 · urine Cu > 40 µg/24 ชม."],
    [mcq(N(8), "A 72-year-old man in the ICU after cardiac arrest has ALT 8,900 U/L and AST 11,200 U/L on day 2 with bilirubin 1.6 mg/dL. Two days later ALT is 2,100 U/L. What is the diagnosis?",
         ["Acute hepatitis B", "Ischaemic hepatitis", "Autoimmune hepatitis", "Wilson's disease", "Alcoholic hepatitis"], 1,
         "ครบลักษณะของ **ischemic hepatitis** ในสไลด์ — **ภาวะช็อก/หัวใจหยุดเต้น · ALT/AST สูงเป็นหมื่น · AST > ALT ช่วงแรก · bilirubin ปกติหรือสูงเล็กน้อย · ลดลงเร็วมากภายใน 72 ชม.**\n\nไวรัสตับอักเสบลดลงช้ากว่านี้มาก (50–70% ต่อสัปดาห์) และ bilirubin สูงตามมา · รักษาที่ต้นเหตุคือ **การไหลเวียนเลือด**",
         "ALT เป็นหมื่น + ลดเร็วใน 72 ชม. + ไม่ค่อยเหลือง = ischemic", "Ischaemic hepatitis", R("Ischemic hepatitis")),
     mcq(N(9), "A 24-year-old woman has acute severe hepatitis with Coombs-negative haemolytic anaemia, a tremor and an alkaline phosphatase of 25 U/L. Total bilirubin is 18 mg/dL. Which diagnosis must be considered?",
         ["Hepatitis A", "Wilson's disease", "Gilbert syndrome", "Primary biliary cholangitis", "Alcoholic hepatitis"], 1,
         "สไลด์ Wilson: **อายุน้อย · ตับอักเสบรุนแรงเฉียบพลัน + เม็ดเลือดแดงแตกในหลอดเลือด · อาการทางสมอง (extrapyramidal) · ALP ต่ำ · ALP/total bilirubin < 2** (25/18 ≈ 1.4)\n\nส่ง **ceruloplasmin, ทองแดงในปัสสาวะ 24 ชม., ตรวจ KF ring** · Wilson ที่เป็นตับวายเฉียบพลันมักต้อง **ปลูกถ่ายตับ** → ส่งต่อด่วน",
         "ตับอักเสบรุนแรง + hemolysis + ALP ต่ำ = Wilson", "Wilson's disease", R("Wilson's disease")),
    ], NLN + ["B8.3(1)"])

# ───────────────────────────── 8
sec("gi-hep-08", "ตับอักเสบเรื้อรัง — ไล่หาสาเหตุ และวัดพังผืด",
    "ALT สูง ≥ 3–6 เดือน · HBsAg anti-HCV US ANA ASMA ceruloplasmin iron · Fibroscan < 8 ตัด advanced fibrosis · FIB-4", 10,
"""### สาเหตุ
| พบบ่อย | พบน้อย |
|---|---|
| **Hepatitis B · Hepatitis C · แอลกอฮอล์ · MASLD/MASH** | **AIH · Wilson · hemochromatosis · ยา** |

### ขั้นตอน (สไลด์)
**ALT สูง ≥ 3–6 เดือน** หรือมีหลักฐานโรคเรื้อรังจากการตรวจร่างกาย lab ภาพ หรือชิ้นเนื้อ
1. **ประวัติ** ยา สมุนไพร เหล้า ประวัติครอบครัว โรคร่วม + ตรวจร่างกาย
2. ตรวจชุดแรก
| ตรวจ | ตัดโรคได้เมื่อ |
|---|---|
| **HBsAg, anti-HCV** | — |
| **อัลตราซาวนด์ + BMI รอบเอว FBS ไขมัน** | หา MASLD |
| **ANA, ASMA** | **ลบทั้งคู่ → ตัด AIH ได้ ~90%** |
| **Ceruloplasmin, ทองแดงในปัสสาวะ, KF ring** | **ceruloplasmin ≥ 20 + urine Cu ≤ 40 µg + ไม่มี KF → ตัด Wilson** |
| **Iron study** (บางราย) | **TSAT < 45% + ferritin ปกติ → ตัด hemochromatosis** |
3. ยังไม่พบสาเหตุ → โรคหายาก · CT/MRI-MRCP · **ตัดชิ้นเนื้อตับ**

### ระยะพังผืด
**F0–F4** · **significant fibrosis (F2–F4)** → เสี่ยงโรคดำเนินต่อ · **advanced (≥ F3)** → เสี่ยง **ตับแข็งเสื่อม (decompensation) และมะเร็งตับ**

### วัดโดยไม่เจาะตับ (สไลด์)
**Transient elastography (Fibroscan)**
| ค่า | ความหมาย |
|---|---|
| **CAP ≥ 250–288 dB/m** | ไขมันพอกตับ · **≥ 340 = รุนแรง (S3)** |
| **Liver stiffness < 8 kPa** | **ตัด advanced fibrosis** |
| **≥ 8 kPa** | น่าจะ ≥ F2 |
| **≥ 12 kPa** | น่าจะ ≥ F3 |
ความแม่นต่ำเมื่อ IQR/median > 30% (stiffness) หรือ IQR > 40 dB/m (CAP)

| | ≥ F2 | ตับแข็ง (F4) |
|---|---|---|
| Fibroscan | 7–8 kPa | 12–15 kPa |
| **APRI** | 0.5–0.7 | 1.5–2.0 |
| **FIB-4** (อายุ, AST, ALT, เกล็ดเลือด) | 1.3–1.45 | 2.67–3.25 |
**FIB-4 แม่นน้อยลงเมื่ออายุ < 35 หรือ > 65 ปี** · คำนวณได้ที่ MDCalc
""",
    ["Chronic hepatitis: ALT สูง ≥ 3–6 เดือน",
     "ชุดแรก: HBsAg anti-HCV · US · ANA ASMA · ceruloplasmin urine Cu · iron",
     "ANA/ASMA ลบ ตัด AIH 90% · TSAT < 45 + ferritin ปกติ ตัด hemochromatosis",
     "Fibroscan < 8 ตัด advanced · ≥ 12 น่าจะ F3 · CAP ≥ 250–288 = fatty",
     "FIB-4 < 1.3 ตัด F2 · > 2.67–3.25 ตับแข็ง · แม่นน้อยในอายุ < 35, > 65"],
    [mcq(N(10), "A 52-year-old man with type 2 diabetes has ALT persistently 70 U/L. Fibroscan shows CAP 310 dB/m and liver stiffness 6.1 kPa (valid measurement). What is the best interpretation?",
         ["Normal liver", "Steatosis present; advanced fibrosis is unlikely", "Cirrhosis", "Severe fibrosis requiring biopsy", "The test is invalid"], 1,
         "**CAP ≥ 250–288 dB/m = มีไขมันพอกตับ** (310) · **liver stiffness < 8 kPa = ตัด advanced fibrosis ได้** (6.1)\n\nขั้นต่อไป: แก้ปัจจัยเมตาบอลิก ลดน้ำหนัก ติดตาม · ยังต้องคัด HBsAg/anti-HCV และซักประวัติเหล้า",
         "CAP ≥ 250–288 = fatty · stiffness < 8 = ไม่มี advanced fibrosis", "Fibroscan interpretation", R("Transient elastography: interpretation"), CHR),
    ], CHR)

# ───────────────────────────── 9
sec("gi-hep-09", "ตับอักเสบบีเรื้อรัง — เมื่อไรให้ยา (อัปเดต WHO 2024 / EASL 2025)",
    "คนไทย HBsAg+ 2–3 ล้าน · ติดตอนเด็กเรื้อรัง > 90% · HBV DNA > 2,000 + ตับอักเสบ/พังผืด → TAF · เฝ้าระวังมะเร็งตับ", 11,
"""### ระบาดวิทยาไทย (สไลด์)
- ผู้ติดเชื้อเรื้อรัง (HBsAg+) **ราว 2–3 ล้านคน** ส่วนใหญ่ **อายุ > 40 ปี**
- **ฉีดวัคซีนเด็กแรกเกิดทุกรายตั้งแต่ พ.ศ. 2535** · คนอายุ 40–50 ปี **30–40% เคยติด (anti-HBc+)**

### การติดต่อและการดำเนินโรค
- ไวรัสมาก: **เลือด น้ำเหลือง แผล** · ปานกลาง: **น้ำอสุจิ น้ำในช่องคลอด น้ำลาย** · **อยู่นอกร่างกายได้ 5–7 วัน**
- **โอกาสเป็นเรื้อรังขึ้นกับอายุที่ติด** — **แรกคลอด/เด็กเล็ก > 90%** · **ผู้ใหญ่ < 5% (หายเอง > 90%)**
- เรื้อรัง → **ตับแข็ง** · **มะเร็งตับเกิดได้แม้ไม่มีตับแข็ง** (HBV DNA แทรกใน genome)

### เมื่อไรให้ยา
| สไลด์ | **WHO 2024 · EASL 2025 · AASLD/IDSA 2025** |
|---|---|
| **HBV DNA > 2,000 IU/mL** ร่วมกับ **ALT > 1.5 × ULN ≥ 3 เดือน** หรือ **biopsy ≥ F2 / HAI ≥ 4** หรือ **Fibroscan > 7.0 kPa** | **HBV DNA ≥ 2,000 IU/mL + ALT > ULN** (WHO ลดจากเดิม 20,000) |
| ULN ของ ALT ใหม่ **35 (ชาย) · 25 (หญิง)** | ใช้เกณฑ์เดียวกัน |
| — | **พังผืด ≥ F2 → ให้ยาโดยไม่ดู HBV DNA หรือ ALT** (WHO) |
| — | **ตับแข็ง + HBV DNA ตรวจพบ → ให้ยาทุกราย** ไม่ดู ALT |
| — | **WHO 2024 เพิ่ม**: ติดเชื้อร่วม (HIV, HDV, HCV) · ประวัติครอบครัวมะเร็งตับหรือตับแข็ง · ภูมิคุ้มกันต่ำ · อาการนอกตับ → ให้ยาได้ |
อายุ > 35 ปี เสี่ยงตับเสียมากขึ้น · ไม่เข้าเกณฑ์ → **ติดตามต่อ**

### ยาและคำแนะนำ (สไลด์)
- **Tenofovir alafenamide (TAF) 1 เม็ดหลังอาหารวันละครั้ง** — ยาแรกในบัญชียาหลักแห่งชาติ · ผลข้างเคียงน้อย ติดตามไตและมวลกระดูกในกลุ่มเสี่ยง
- **คุมได้ทุกราย แต่หายขาดเพียง 1–3%** (cccDNA ยังอยู่)
- **ต้องกินยานาน** — HBeAg ลบมักตลอดชีวิต · HBeAg บวกหลายปี
- **ลดความเสี่ยงมะเร็งตับ แต่ไม่ได้ป้องกันทั้งหมด** · เน้นกินยาสม่ำเสมอและมาตามนัด · **ห้ามหยุดยาเอง** (ตับอักเสบกำเริบรุนแรงได้)

### เฝ้าระวังมะเร็งตับ
**อัลตราซาวนด์ + AFP ทุก 6–12 เดือน** ใน **ชาย > 40 ปี · หญิง > 50 ปี · ประวัติครอบครัวมะเร็งตับ · พังผืดมาก/ตับแข็ง**
""",
    ["ติด HBV ตอนแรกคลอด เรื้อรัง > 90% · ผู้ใหญ่ < 5%",
     "ให้ยา: HBV DNA ≥ 2,000 + ALT > ULN (35 ชาย/25 หญิง) หรือพังผืด ≥ F2",
     "ตับแข็ง + HBV DNA ตรวจพบ → ให้ยาทุกราย",
     "TAF วันละครั้ง · หายขาดเพียง 1–3% · ห้ามหยุดเอง",
     "เฝ้าระวัง HCC: US + AFP ทุก 6–12 เดือน (ชาย > 40 หญิง > 50 FHx ตับแข็ง)"],
    [mcq(N(11), "A 45-year-old man is HBsAg-positive, HBeAg-negative, HBV DNA 18,000 IU/mL and ALT 52 U/L on repeated testing over 6 months. Fibroscan is 6.5 kPa. According to current (WHO 2024, EASL/AASLD 2025) criteria, what is appropriate?",
         ["No treatment because ALT is below 2 × ULN", "Start tenofovir (e.g., TAF) because HBV DNA ≥ 2,000 IU/mL with ALT above the ULN of 35 U/L",
          "Start interferon for 48 weeks only if HBeAg positive", "Repeat tests in 5 years", "Liver transplantation"], 1,
         "เกณฑ์ปัจจุบัน: **HBV DNA ≥ 2,000 IU/mL ร่วมกับ ALT > ULN** โดยใช้ **ULN ใหม่ 35 U/L ในชาย** (25 ในหญิง) → ALT 52 สูงกว่า ULN → **ให้ยา** (WHO 2024 ลดเกณฑ์ HBV DNA จาก 20,000 เหลือ 2,000)\n\nสไลด์ของอาจารย์ใช้ ALT > 1.5 × ULN (52 ≥ 1.5 × 35 = 52.5 พอดีเกือบถึง) — แนวทางใหม่ให้ยาง่ายขึ้นเพื่อลดมะเร็งตับ · ยาแรกในไทยคือ **TAF**",
         "HBV DNA ≥ 2,000 + ALT > ULN (35/25) → ให้ยา", "HBV treatment indication", R("Chronic hepatitis B: treatment indications") + ["WHO 2024 HBV guidelines", "EASL 2025 HBV CPG"], CHR + ["B8.3(2)"]),
    ], CHR + ["B8.3(2)"], SRC + " · อัปเดต WHO 2024 / EASL 2025 / AASLD–IDSA 2025")

# ───────────────────────────── 10
sec("gi-hep-10", "ตับอักเสบซีเรื้อรัง — รักษาหายขาดได้",
    "anti-HCV บวกต้องตรวจ HCV RNA · เรื้อรัง ~80% · SOF/VEL 12 สัปดาห์ หาย > 95% · ไม่เหมือน HBV และ HIV", 9,
"""### ติดต่อทางไหน (สไลด์)
- **เลือด** — **รับเลือดหรือปลูกถ่ายอวัยวะก่อน พ.ศ. 2535** · **ใช้ยาฉีด/สูดทางจมูก** · สัก เจาะ ฝังเข็ม ใช้ของมีคมร่วม · ในโรงพยาบาล (ฟอกไต) และบุคลากรถูกเข็มตำ
- **เพศสัมพันธ์** — **ชายรักชาย** · กิจกรรมเสี่ยงสูง
- **แม่สู่ลูก** — พบน้อย · **30% ไม่ทราบทาง**

### ไทย
ผู้ติดเชื้อ **300,000–400,000 คน** · คนเกิดก่อน 2535 ~1% · กลุ่มเสี่ยงพิเศษ: **ผู้ใช้ยาฉีด 36–80%** · ผู้ติด HIV 3–8% · MSM 5–7% · ผู้ต้องขัง 6% · บุคลากรการแพทย์

### ธรรมชาติของโรค
**หายเองได้ < 20% · เรื้อรัง ~80%** → ตับแข็ง 20–50% ใน 20–40 ปี → มะเร็งตับ 1–4% ต่อปี
**อาการนอกตับ** — คุณภาพชีวิตลด ซึมเศร้า **ดื้ออินซูลิน/เบาหวาน** โปรตีนรั่ว CKD **lymphoma** โรคภูมิคุ้มกัน (**cryoglobulinemia, MPGN**, PCT, ITP)

### ตรวจอย่างไร
**anti-HCV บวก → ต้องตรวจ HCV RNA (หรือ HCV antigen)** เพราะ anti-HCV บอกเพียงว่า **เคยติด**
- RNA บวก → ติดเชื้ออยู่: วัดปริมาณ genotype ประเมินพังผืด โรคร่วม
- RNA ลบ → หายเองแล้วหรือผลบวกลวง (ตรวจ RNA ซ้ำใน 3–6 เดือน)

### ทำไม HCV รักษาหายขาดได้
| ไวรัส | สารพันธุกรรมในเซลล์ | หายขาด |
|---|---|---|
| **HBV** | **cccDNA** ในนิวเคลียส | ยาก (1–3%) |
| **HIV** | **proviral DNA แทรกใน genome** | ไม่ได้ |
| **HCV** | RNA แบ่งตัวใน cytoplasm **ไม่มีแหล่งซ่อน** | **ได้ > 95%** |

### ยา DAA (สไลด์)
- **Sofosbuvir + velpatasvir (400/100 มก.) วันละเม็ด 12 สัปดาห์** — ในบัญชียาหลักแห่งชาติ ใช้ได้ทุก genotype
- **หาย > 95%** · **SVR = ตรวจไม่พบ HCV RNA 12 สัปดาห์หลังหยุดยา** = หายขาด → ป้องกันหรือย้อนโรค ลดมะเร็งตับ อยู่รอดนานขึ้น
- ผลข้างเคียงน้อย · เน้นกินยาสม่ำเสมอ · **ตรวจยาตีกัน เลี่ยง PPI ถ้าทำได้** (กรดน้อยทำให้ velpatasvir ดูดซึมลด)
- **มีพังผืดมากก่อนรักษา → เฝ้าระวังมะเร็งตับตลอดชีวิตแม้หายแล้ว**
""",
    ["anti-HCV บวก = เคยติด → ต้องตรวจ HCV RNA",
     "HCV เรื้อรัง ~80% · อาการนอกตับ: DM, cryoglobulinemia, MPGN, lymphoma",
     "SOF/VEL 12 สัปดาห์ หาย > 95% · SVR12 = หายขาด",
     "เลี่ยง PPI ระหว่างใช้ SOF/VEL",
     "พังผืดมากก่อนรักษา → เฝ้าระวัง HCC ตลอดชีวิต"],
    [mcq(N(12), "A 50-year-old man who received a blood transfusion in 1988 is anti-HCV positive. What is the next step?",
         ["Start sofosbuvir/velpatasvir immediately", "Measure HCV RNA to confirm current infection", "Reassure: a positive antibody means immunity",
          "Repeat anti-HCV in 5 years", "Perform liver biopsy before any other test"], 1,
         "**anti-HCV บอกเพียงว่าเคยติดเชื้อ** — ราว 20% หายเองแล้วแต่ยังมีแอนติบอดี และอาจเป็นผลบวกลวง → ต้องตรวจ **HCV RNA (หรือ HCV antigen)** ยืนยันว่ายังติดเชื้ออยู่ก่อนให้ยา\n\nanti-HCV **ไม่ได้แปลว่ามีภูมิคุ้มกัน** (ติดซ้ำได้)",
         "anti-HCV + → HCV RNA ก่อนรักษา", "HCV testing", R("HCV: initial evaluation"), CHR),
     mcq(N(13), "Why can hepatitis C be cured with direct-acting antivirals, whereas hepatitis B usually cannot?",
         ["HCV is a DNA virus", "HCV has no nuclear reservoir such as cccDNA; HBV persists as cccDNA in hepatocyte nuclei",
          "HCV integrates into host DNA", "HBV has no effective drugs", "HCV infection is always acute"], 1,
         "สไลด์: **HCV เป็น RNA virus ที่แบ่งตัวใน cytoplasm และไม่มีแหล่งซ่อน** เมื่อยาหยุดการแบ่งตัวจนหมด ไวรัสก็หายไปจริง → **SVR = หายขาด**\n\n**HBV เก็บ cccDNA ในนิวเคลียส** (และบางส่วนแทรกใน genome) ยาจึงกดได้แต่กำจัดไม่หมด · **HIV แทรก proviral DNA ใน genome** จึงไม่หายขาด",
         "HCV ไม่มี reservoir → หายขาด · HBV มี cccDNA", "HCV cure", R("HCV is curable")),
    ], CHR, SRC + " · AASLD–IDSA HCV guidance")

# ───────────────────────────── 11
sec("gi-hep-11", "MASLD — ไขมันพอกตับที่สัมพันธ์กับเมตาบอลิก",
    "ชื่อใหม่ 2023 · ไขมันพอกตับ + ปัจจัยเมตาบอลิก ≥ 1 ข้อ · ลดน้ำหนัก 5/7/10% · semaglutide, pioglitazone, vitamin E, resmetirom", 10,
"""### ชื่อใหม่ (multi-society Delphi 2023)
NAFLD → **MASLD (metabolic dysfunction-associated steatotic liver disease)** · NASH → **MASH**
**MASLD = ไขมันพอกตับ + ปัจจัยเมตาบอลิกอย่างน้อย 1 ข้อ** (ไม่มีสาเหตุอื่น)
| ปัจจัย (เกณฑ์เอเชีย) | |
|---|---|
| **BMI ≥ 23** หรือ **รอบเอว > 90 ซม. (ชาย) / > 80 ซม. (หญิง)** | |
| **FBS ≥ 100** หรือ **HbA1c ≥ 5.7%** หรือเบาหวาน | |
| **BP ≥ 130/85** หรือได้ยาลดความดัน | |
| **TG ≥ 150** หรือได้ยาลดไขมัน | |
| **HDL ≤ 40 (ชาย) / ≤ 50 (หญิง)** หรือได้ยา | |
ถ้าดื่มเหล้า **≥ 210 / 140 ก./สัปดาห์ (ชาย/หญิง)** ด้วย → MetALD หรือ ALD

### ตรวจหาไขมันในตับ
**อัลตราซาวนด์** (ไวและจำเพาะต่ำ) · **CAP > 250–288 dB/m** · CT ใกล้เคียง US · **MRI-PDFF แม่นที่สุด**

### ความสำคัญ
- ทั่วโลก **25%** · **ไทย ~21%** · MASH 1.5–6%
- **ตายเพิ่มทั้งจากหัวใจและหลอดเลือด (สาเหตุตายอันดับหนึ่ง) และมะเร็ง**
- พังผืดเพิ่ม **~1 ระยะทุก 7 ปี** · **~10% ดำเนินเร็ว** เป็นตับแข็งใน 10 ปี

### ลดน้ำหนักเท่าไรได้อะไร (สไลด์)
| ลดน้ำหนัก | ผล |
|---|---|
| **≥ 3%** | ไขมันในตับลด |
| **≥ 5%** | การอักเสบลด |
| **≥ 7%** | **MASH หาย** 64–90% |
| **≥ 10%** | **พังผืดถอยกลับ** 45% |

### การรักษา (EASL–EASD–EASO 2024 + อัปเดตยา)
- **ปรับวิถีชีวิตทุกราย** — อาหาร (Mediterranean) ออกกำลังกาย ลด/งดเหล้า
- ยาที่สไลด์กล่าวถึง: **semaglutide** (ลดน้ำหนัก ช่วยทั้งตับและหัวใจ) · **pioglitazone** · **vitamin E (natural) 400–800 IU/วัน** (คนที่ไม่เป็นเบาหวาน)
- **ยาที่ได้รับอนุมัติเฉพาะ MASH พังผืด F2–F3 (ไม่มีตับแข็ง)**: **resmetirom** (FDA มี.ค. 2024 — กระตุ้น thyroid hormone receptor-β ในตับ) และ **semaglutide** (FDA ส.ค. 2025)
- **ตับแข็ง → เฝ้าระวังมะเร็งตับด้วย US + AFP ทุก 6 เดือน**
""",
    ["MASLD = ไขมันพอกตับ + ปัจจัยเมตาบอลิก ≥ 1 ข้อ (BMI ≥ 23 ในเอเชีย)",
     "สาเหตุตายอันดับหนึ่งของ MASLD คือโรคหัวใจและหลอดเลือด",
     "ลดน้ำหนัก ≥ 7% MASH หาย · ≥ 10% พังผืดถอย",
     "ยา: semaglutide · pioglitazone · vitamin E · resmetirom (MASH F2–F3)",
     "ตับแข็ง → US + AFP ทุก 6 เดือน"],
    [mcq(N(14), "A 46-year-old woman with MASH (biopsy F2) and BMI 31 asks how much weight she needs to lose to reduce liver fibrosis. What is the best answer?",
         ["Any weight loss reverses fibrosis", "About 3%", "About 5%", "At least 7%, which resolves MASH, but ≥ 10% is associated with fibrosis regression", "Weight loss has no effect on fibrosis"], 3,
         "สไลด์ weight loss targets: **≥ 3% ไขมันลด · ≥ 5% การอักเสบลด · ≥ 7% MASH หาย (64–90%) · ≥ 10% พังผืดถอยกลับ (45%)**\n\nผู้ป่วยรายนี้มีพังผืด F2 → เป้าคือ **≥ 10%** · ถ้าลดเองไม่ได้ พิจารณา **semaglutide** หรือ **resmetirom** ซึ่งได้รับอนุมัติสำหรับ MASH F2–F3",
         "พังผืดถอยต้องลดน้ำหนัก ≥ 10%", "MASLD weight-loss targets", R("Weight loss targets and improvement of MASLD"), CHR + ["2.3.11(4)"]),
    ], ["B8.2.5(4)", "2.3.11(4)"], SRC + " · EASL–EASD–EASO 2024 · FDA 2024–2025")

# ───────────────────────────── MEQ / OSCE
LECNAME = "Acute and chronic hepatitis (อ.เฉลิมรัฐ)"
MEQ = [{"id": "GI-HEP-MEQ-01", "part": "MEQ", "lec": "12/10", "lecture": LECNAME,
 "topic": "Acute jaundice — acute hepatitis B, severity assessment and household contacts",
 "vignette": """ผู้ป่วยชายไทยอายุ 29 ปี พนักงานขาย มาด้วยตาเหลือง 5 วัน
PI: 10 วันก่อน ไข้ต่ำ อ่อนเพลีย เบื่ออาหาร คลื่นไส้ ปวดตื้อชายโครงขวา 5 วันก่อนตาเหลือง ปัสสาวะสีชาเข้ม ไข้หายไปเมื่อเริ่มเหลือง
ประวัติ: มีเพศสัมพันธ์กับคู่นอนหลายคนโดยไม่ใช้ถุงยางเมื่อ 3 เดือนก่อน · ไม่ดื่มเหล้า · ไม่ได้กินยาหรือสมุนไพร · ไม่เคยได้วัคซีนตับอักเสบบี
PE: BT 37.2 C · รู้สึกตัวดี ไม่มี asterixis · ตาเหลือง · ตับโต 2 ซม. กดเจ็บเล็กน้อย · ไม่มีท้องมาน ไม่มี spider naevi
Lab: AST 1,640 U/L · ALT 2,380 U/L · ALP 160 · TB 9.8 mg/dL · DB 7.2 · albumin 3.8 · INR 1.3
HBsAg positive · anti-HBc IgM positive · anti-HAV IgM negative · anti-HCV negative · anti-HIV negative""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัย พร้อมเหตุผลจากอาการและผลเลือด (3 คะแนน)",
   "a": """**Acute hepatitis B**
- อาการนำคล้ายไข้หวัด → ตาเหลือง และ **ไข้หายเมื่อเริ่มเหลือง** · ระยะฟักตัว 4–24 สัปดาห์ เข้ากับการสัมผัสเสี่ยง 3 เดือนก่อน
- **ALT > AST** อยู่ในช่วง 1,000–4,000 แบบ acute viral hepatitis
- **HBsAg + anti-HBc IgM บวก** = ติดเชื้อเฉียบพลัน · anti-HAV IgM ลบ · ไม่มีประวัติยา/เหล้า"""},
  {"q": "2. ผู้ป่วยรายนี้รุนแรงหรือไม่ จะเฝ้าระวังอะไร และต้องให้ยาต้านไวรัสหรือไม่ (4 คะแนน)",
   "a": """- **ยังไม่รุนแรง** — **INR 1.3 (< 1.5)** ไม่มี encephalopathy
- เฝ้าระวัง **INR, bilirubin, ระดับความรู้สึกตัว (encephalopathy/asterixis)** · ถ้า INR ≥ 1.5 + encephalopathy = acute liver failure → ส่งศูนย์ปลูกถ่ายตับ
- **ยังไม่ต้องให้ยาต้านไวรัส** — ผู้ใหญ่หายเอง > 95% · พิจารณาให้ (เช่น tenofovir) เมื่อ **รุนแรง: INR > 1.5 หรือ bilirubin สูงมากต่อเนื่อง**
- ประคับประคอง: ทำกิจวัตรตามไหว **ดื่มน้ำมาก งดเหล้า ยาพิษตับ ยานอนหลับ**"""},
  {"q": "3. จะติดตามผลอย่างไรเพื่อดูว่าหายหรือเป็นเรื้อรัง (3 คะแนน)",
   "a": """- อาการดีขึ้นใน 2–3 เดือน · **HBsAg ควรหายใน 3–6 เดือน และเกิด anti-HBs**
- ตรวจ **HBsAg ซ้ำที่ 6 เดือน** — **ยังบวกเกิน 6 เดือน = chronic HBV** → ประเมิน HBV DNA, ALT, พังผืด ตามเกณฑ์การรักษา
- ALT ควรลด 50–70% ต่อสัปดาห์หลังยอด · bilirubin ลดช้ากว่าเพราะ delta-bilirubin"""},
  {"q": "4. จะให้คำแนะนำการป้องกันแก่คู่นอนและคนในบ้านอย่างไร (3 คะแนน)",
   "a": """- **ตรวจ HBsAg, anti-HBs (± anti-HBc) ในคู่นอนและคนในบ้าน** · ไม่มีภูมิ → **ฉีดวัคซีนตับอักเสบบี**
- **คู่นอนที่สัมผัสภายใน 14 วัน** และไม่มีภูมิ → **HBIG + วัคซีน**
- **ใช้ถุงยาง** จนกว่าคู่นอนมีภูมิ · ไม่ใช้มีดโกน แปรงสีฟันร่วมกัน (ไวรัสอยู่นอกร่างกายได้ 5–7 วัน)
- ตรวจคัดกรอง STI อื่นและ HIV ซ้ำ (window period)"""}],
 "ref": ["สไลด์ อ.เฉลิมรัฐ — acute viral hepatitis, HBV serology, management"],
 "nl": ["2.3.1(1)", "2.1.13", "B8.3(2)"], "years": [], "_kind": "meq", "_set": SET}]

OSCE = [{"id": "GI-HEP-OSCE-01", "part": "OSCE/SAQ", "lec": "12/10", "lecture": LECNAME,
 "topic": "SAQ – Interpreting hepatitis B serology",
 "station": "SAQ (เขียนตอบ) 5 นาที",
 "instruction": """จงแปลผลการตรวจไวรัสตับอักเสบบีของบุคคล 5 รายต่อไปนี้ และบอกสิ่งที่ควรทำต่อ

| ราย | HBsAg | anti-HBc (total) | anti-HBc IgM | anti-HBs | HBeAg |
|---|---|---|---|---|---|
| A | − | − | − | − | − |
| B | − | − | − | + (120) | − |
| C | − | + | − | + | − |
| D | + | + | + | − | + |
| E | + | + | − | − | − (HBV DNA 25,000 IU/mL, ALT 60 U/L ชาย) |""",
 "answer": """| ราย | แปลผล | ทำต่อ | คะแนน |
|---|---|---|---|
| **A** | **ไม่เคยติดเชื้อ ไม่มีภูมิ** | **ฉีดวัคซีนตับอักเสบบี** | 2 |
| **B** | **ภูมิคุ้มกันจากวัคซีน** (anti-HBs ≥ 10 · ไม่มี anti-HBc) | ไม่ต้องทำอะไร | 2 |
| **C** | **เคยติดเชื้อและหายแล้ว** มีภูมิ | ระวัง HBV กำเริบถ้าจะได้ยากดภูมิแรง (เช่น rituximab, เคมีบำบัด) | 2 |
| **D** | **ติดเชื้อเฉียบพลัน** ไวรัสแบ่งตัวมาก ติดต่อง่าย | ประเมินความรุนแรง (INR encephalopathy) · ตรวจ HBsAg ซ้ำที่ 6 เดือน · ป้องกันคู่นอน/คนในบ้าน | 2 |
| **E** | **ติดเชื้อเรื้อรัง HBeAg ลบ** · **HBV DNA ≥ 2,000 + ALT > ULN (35 ในชาย)** | **เข้าเกณฑ์ให้ยา → TAF วันละครั้ง** · ประเมินพังผืด · เฝ้าระวัง HCC (US + AFP) | 2 |

**หลักการที่ต้องเขียนให้เห็น**: anti-HBs = มีภูมิ · anti-HBc = เคยเห็นแกนไวรัส (ติดจริง ไม่ใช่วัคซีน) · IgM = ใหม่ · HBsAg > 6 เดือน = เรื้อรัง""",
 "ref": ["สไลด์ อ.เฉลิมรัฐ — serological markers for HBV, CHB treatment indications"],
 "nl": ["B8.3(2)", "2.3.1(1)", "2.3.1-3(3)"], "years": [], "_kind": "meq", "_set": SET}]

LECTURE = {
 "lec": "12/10", "date": "จ. 12 ต.ค.",
 "title": "Acute and chronic hepatitis",
 "subtitle": "อ่าน ALT/AST · ไวรัส A–E และผลเลือด HBV · ดูแล acute hepatitis และตับวาย · เหล้า ยา ขาดเลือด AIH Wilson · ไล่หาสาเหตุตับอักเสบเรื้อรังและวัดพังผืด · HBV HCV MASLD ตามแนวทางล่าสุด",
 "objectives": [
   "แปลผล ALT/AST และแยกตับอักเสบเฉียบพลันจากสาเหตุนอกตับ",
   "เปรียบเทียบไวรัสตับอักเสบ A–E ทางติดต่อ ระยะฟักตัว และการเป็นเรื้อรัง",
   "แปลผลการตรวจ HBV และเลือกการตรวจที่เหมาะกับการสงสัยตับอักเสบเฉียบพลัน",
   "ประเมินความรุนแรงของตับอักเสบเฉียบพลัน และรู้จัก acute liver failure",
   "จดจำลักษณะของตับอักเสบจากเหล้า ยา ขาดเลือด AIH และ Wilson",
   "วางขั้นตอนหาสาเหตุตับอักเสบเรื้อรังและแปลผล Fibroscan, APRI, FIB-4",
   "บอกเกณฑ์ให้ยาใน HBV เรื้อรังตามแนวทางปัจจุบัน และการเฝ้าระวังมะเร็งตับ",
   "ตรวจวินิจฉัยและรักษา HCV ให้หายขาด และวินิจฉัยและดูแล MASLD"],
 "nlGap": "เกณฑ์ฯ มีรหัส `นล. 2.3.1(1)` Acute viral hepatitis (กลุ่ม 2) · `2.3.1-3(3)` Chronic viral hepatitis (กลุ่ม 3) · `2.3.11(2)` Alcoholic liver disease · `B8.3(2)` Viral hepatitis serologies แต่ **ไม่มีรหัสของ MASLD, DILI, AIH หรือ Wilson โดยเฉพาะ** และเกณฑ์การรักษา HBV เปลี่ยนในปี 2024–2025 จึงอ้างอิงแนวทางด้านล่าง",
 "guidelines": [
   "**WHO Guidelines for the prevention, diagnosis, care and treatment of people with chronic hepatitis B (2024)** — HBV DNA > 2,000 + ALT > ULN · ≥ F2 ให้ยาทุกราย",
   "**EASL Clinical Practice Guidelines on the management of HBV infection (2025)** และ **AASLD/IDSA HBV guideline (2025)** — ULN ALT 35/25",
   "**AASLD–IDSA HCV Guidance** — pangenotypic DAA (SOF/VEL 12 สัปดาห์)",
   "**ACG Clinical Guideline: Alcohol-associated liver disease (2024)** (อาจารย์อ้างในสไลด์)",
   "**EASL–EASD–EASO Clinical Practice Guidelines on MASLD (2024)** และ **multi-society Delphi nomenclature (Hepatology 2023)** · FDA: resmetirom 2024, semaglutide 2025 สำหรับ MASH F2–F3",
   "**แนวทางเวชปฏิบัติโรคไวรัสตับอักเสบของประเทศไทย** — TAF และ SOF/VEL ในบัญชียาหลักแห่งชาติ (ตามสไลด์)"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

GI_META = {"set": "gi", "title": "GI · ระบบทางเดินอาหารและตับ",
 "intro": "ชุดใหม่ของระบบทางเดินอาหาร ตับ และทางเดินน้ำดี เริ่มจากคาบ **Acute and chronic hepatitis ของ อ.เฉลิมรัฐ (12 ต.ค.)** — ตั้งแต่การอ่าน ALT/AST ไวรัสตับอักเสบ A–E ผลเลือด HBV ตับอักเสบจากเหล้า ยา ขาดเลือด AIH และ Wilson ไปจนถึงการรักษา HBV HCV และ MASLD ตามแนวทางล่าสุด จบแต่ละหัวข้อมีข้อสอบเช็คความเข้าใจทันที",
 "howto": "**วิธีใช้** — อ่านเนื้อหาให้จบแล้วตอบข้อสอบท้ายหัวข้อ ระบบเฉลยพร้อมคำอธิบายกลไกทันทีที่ตอบ · ข้อที่ตอบผิดรวมอยู่ในแท็บ **ทบทวนข้อที่ผิด** · จบคาบแล้วฝึก **MEQ** และ **OSCE/SAQ** ต่อ\n\n**ลำดับที่แนะนำ** — หัวข้อ 3 (ตารางผลเลือด HBV) คือส่วนที่ออกสอบบ่อยที่สุด ฝึกจนวาดตารางได้เอง แล้วไปทำ SAQ แปลผล HBV 5 ราย\n\n**หมายเหตุ** — ชุด GI ยังไม่มีคลังข้อสอบเก่ารายคาบใน Ward Drill จึงผูกข้อจาก Mock exam หมวด GI ที่ตรงเรื่องแทน",
 "label": "GI", "thai": "ระบบทางเดินอาหารและตับ",
 "accent": {"light": "#4d6b1f", "soft": "#eaf0df", "ink": "#3b5317", "dark": "#b5d97a", "darkSoft": "#182010", "darkInk": "#cfe8a3"},
 "file": "data/gi.json", "lectureCount": 1}

# กระจายตำแหน่งคำตอบของข้อใหม่ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น)
_slot = 0
for s_ in S:
    for it in s_["items"]:
        if it["id"] in {N(14)}:
            continue
        tgt = [0, 2, 4, 1, 3][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", SET + ".json")
data = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
data = [l for l in data if l.get("lec") != LECTURE["lec"]] + [LECTURE]
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
if not any(m["set"] == SET for m in idx):
    idx.append(GI_META)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ผูกข้อ Mock หมวด GI ที่ตรงเรื่อง (ผ่าน link_bank ซึ่งตรวจว่าไม่ซ้ำกับคาบอื่นในชุดนี้)
import link_bank
_orig = link_bank.link
def link_mock(setkey, lec, sections):
    """ข้อ mock อยู่ในคลังชุด 'mock' แต่ลงในไฟล์ชุด gi"""
    idxm = link_bank.bank_index("mock")
    d = json.load(open(path, encoding="utf-8"))
    L = [l for l in d if l["lec"] == lec][0]
    have = {i["id"] for s_ in L["sections"] for i in s_["items"]}
    used = set()
    for f in os.listdir(os.path.join(BUILD, "data")):
        if f.endswith(".json") and f not in ("nl.json", "index.json"):
            for l in json.load(open(os.path.join(BUILD, "data", f), encoding="utf-8")):
                if f == SET + ".json" and l["lec"] == lec:
                    continue
                used |= {i["id"] for s_ in l["sections"] for i in s_["items"]}
    n = 0
    secs = {s_["id"]: s_ for s_ in L["sections"]}
    for sid, ids in sections.items():
        for i in ids:
            assert i in idxm and i not in used, i
            if i not in have:
                it = dict(idxm[i]); it["kind"] = "old"
                it["topic"] = (it.get("topic") or "").split("·", 1)[-1].strip()
                it["ref"] = ["Mock exam MED421 — " + i] + list(it.get("ref", []))
                secs[sid]["items"].append(it); n += 1
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    return n
added = link_mock(SET, "12/10", {"gi-hep-03": ["MOCK-149"], "gi-hep-05": ["MOCK-153"]})

d = json.load(open(path, encoding="utf-8"))
L = [l for l in d if l["lec"] == "12/10"][0]
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = {c for s_ in L["sections"] for c in s_["nl"]} | {c for s_ in L["sections"] for i in s_["items"] for c in i.get("nl", [])} | {c for m in L["meq"] + L["osce"] for c in m["nl"]}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == SET: m["lectureCount"] = len(d)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | ข้อใหม่ %d + mock %d | meq %d | osce %d | nl %d" % (len(S), sum(len(s_["items"]) for s_ in S), added, len(MEQ), len(OSCE), len(codes)))
