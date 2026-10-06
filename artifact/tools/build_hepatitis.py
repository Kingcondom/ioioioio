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

# ═══ ต่อส่วนที่ 2 ด้านล่าง ═══
