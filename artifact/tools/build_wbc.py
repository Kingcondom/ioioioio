#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Approach to WBC disorder and lymphadenopathy (อ.เบญจมาภรณ์ เมฆรักษ์เสรี · active learning) → data/hemonc.json
ต้นฉบับ: Drive 1VtpxDAfvwYkpJPIrqs19s7JoLJU-hA6V "Lec22Approach to WBC disorder and lymphadenopathy.pdf" (66 หน้า)
บรรยาย จ. 12 ต.ค. 2569 · โน้ต slides/wbc_notes.md (มีลายมือผู้ใช้ ✍️)
เน้นตามคำขอผู้ใช้: กลไกของอาการเด่นแต่ละโรค (#### ทำไมถึงมีอาการนี้) + ภาพ SVG กลไก (svg.py)
ไม่มีคลัง Ward Drill ของคาบนี้ → ผูกข้อ Mock หมวด M03 Hematology ที่ตรงเรื่อง (CML, aplastic anaemia)
เนื้อหาที่ไม่ได้มาจากสไลด์ระบุไว้ในบทเรียน: acute leukemia/APL, CML treatment (ELN 2020), iwCLL 2018,
Lugano 2014, เกณฑ์ biopsy ต่อมน้ำเหลือง, กลไก B symptoms และอาการเฉพาะของ Hodgkin"""
import json, math, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_mock import link_mock
from svg import *

SET, LEC = "hemonc", "12/10"
NLN = ["B2.1.2(3)"]
SRC = "สไลด์ อ.เบญจมาภรณ์ — Approach to WBC disorder and lymphadenopathy"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None, src=SRC, figs=None):
    d = {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": src,
         "nl": nl or NLN, "md": md, "pearls": pearls, "items": items}
    if figs: d["figs"] = figs
    S.append(d)
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "HON-WBC-MCQ-%02d" % n
R = lambda p: ["สไลด์ อ.เบญจมาภรณ์ — " + p]
NOTSLIDE = "*(ไม่ได้มาจากสไลด์ — เติมจากตำรา/แนวทาง)*"

# ───────────────────────────── ตัวช่วยวาดเฉพาะคาบนี้
def badge(x, y, n, c="acf"):
    """วงกลมตัวเลขอ้างอิงในภาพ"""
    return circ(x, y, 9, c) + t(x, y + 4, str(n), "xs b mid tpa")
def tbar(x1, y1, x2, y2, c="lok w2"):
    """เส้นยับยั้ง (ปลายเป็นขีดตั้งฉาก ⊣)"""
    dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy); px, py = -dy / L * 8, dx / L * 8
    return line(x1, y1, x2, y2, c) + line(x2 - px, y2 - py, x2 + px, y2 + py, c)
def cell(x, y, r, nr, c1="wa", c2="waf", dx=0):
    return circ(x, y, r, c1) + circ(x + dx, y, nr, c2)
def fan(x0, y0, xs, y1, y2, c="ln", m="ah"):
    """เส้นแยกจากจุดเดียวลงหลายกล่อง: (x0,y0) → แนวนอนที่ y1 → ลงถึง y2 ที่แต่ละ x"""
    out = line(x0, y0, x0, y1, c) + line(min(xs + [x0]), y1, max(xs + [x0]), y1, c)
    return out + "".join(line(x, y1, x, y2, c, m) for x in xs)

# ───────────────────────────── 1
F1 = {"hemtree": fig("เม็ดเลือดขาวแต่ละชนิดมาจากไหน — และมะเร็งเกิดที่ระดับใด",
 "Stem cell แตกเป็น **สาย myeloid** (neutrophil monocyte eosinophil basophil — สายเดียวกับเม็ดเลือดแดงและเกล็ดเลือด) และ **สาย lymphoid** (B T NK) · "
 "ถ้าเซลล์มะเร็ง **ค้างอยู่ที่ระยะ blast** ไม่เจริญต่อ = **acute leukemia** (AML/ALL) ไขกระดูกถูกยึดจนสร้างเซลล์ปกติไม่ได้ อาการจึงมาเร็ว · "
 "ถ้า **เจริญได้ครบแต่สร้างมากเกิน** = **chronic leukemia** (CML/CLL) เลือดเต็มไปด้วยเซลล์ตัวแก่ อาการค่อยเป็นค่อยไป · "
 "มะเร็งของ lymphocyte ที่ก่อก้อนในต่อมหรือม้าม = **lymphoma** · **MDS** เป็นโรคของระดับ progenitor ที่สร้างเซลล์ผิดรูปและกลายเป็น AML ได้ (✍️ ในสไลด์ MDS) "
 "*(แผนภาพสรุปแนวคิด ไม่ได้อยู่ในสไลด์)*",
 svg(420, 384, "แผนภาพการสร้างเม็ดเลือดขาวสาย myeloid และ lymphoid กับระดับที่เกิด AML ALL CML CLL MDS และ lymphoma",
     box(150, 10, 120, 40, "ac", "Stem cell (HSC)", fs=12.5),
     ar(186, 50, 104, 78), ar(234, 50, 316, 78),
     box(16, 80, 140, 34, "bx", "Myeloid progenitor", fs=12), box(264, 80, 140, 34, "bx", "Lymphoid progenitor", fs=12),
     t(162, 102, "MDS", "sm b tms"),
     ar(86, 114, 86, 138), ar(334, 114, 334, 138),
     box(16, 140, 140, 34, "bad", "Myeloblast"), box(264, 140, 140, 34, "bad", "Lymphoblast"),
     t(162, 162, "AML", "b tbad"), t(258, 162, "ALL", "b tbad end"),
     ar(86, 174, 86, 224, "lok", "ah-ok"), ar(334, 174, 334, 224, "lok", "ah-ok"),
     t(94, 203, "เจริญเต็มที่", "xs mu"), t(326, 203, "เจริญเต็มที่", "xs mu end"),
     box(16, 226, 140, 44, "ok", "Neutrophil · Mono\nEos · Baso", fs=12), box(264, 226, 140, 44, "ok", "B · T · NK cell", fs=12),
     t(162, 252, "CML", "b tms"), t(258, 252, "CLL", "b tms end"),
     t(86, 288, "สายเดียวกับ RBC · เกล็ดเลือด", "xs mu mid"),
     ar(334, 270, 334, 292, "lac", "ah-ac"), box(264, 294, 140, 30, "ac", "Lymphoma (ในต่อม)", fs=12),
     box(16, 338, 190, 40, "bad", "Acute: ค้างที่ blast\n→ ไขกระดูกล้ม · มาเร็ว", fs=11.5),
     box(214, 338, 190, 40, "ms", "Chronic: เจริญได้แต่มากเกิน\n→ ค่อยเป็นค่อยไป", fs=11.5)))}

CBC = ["3.3.1", "3.1.2", "B2.3(2)"]
sec("hon-wbc-01", "อ่าน CBC ให้เป็น — absolute count และแผนที่ของเม็ดเลือดขาว",
    "WBC 4,000–11,000 · absolute = % × WBC · เกณฑ์ neutrophilia lymphocytosis monocytosis eosinophilia basophilia · relative vs absolute · myeloid/lymphoid × acute/chronic", 8,
"""### ค่าปกติและเกณฑ์ (สไลด์)
| เซลล์ | % ใน differential | สูงเมื่อ (absolute) | ต่ำเมื่อ (absolute) |
|---|---|---|---|
| **WBC รวม** | 4,000–11,000 /µL | **> 11,000 = leukocytosis** · **> 50,000 = leukemoid reaction** | **< 4,000 = leukopenia** |
| Neutrophil | 40–60% | **> 7,700** | **< 1,500** |
| Lymphocyte | 20–40% | **> 3,500** | **< 1,000** |
| Monocyte | 2–8% | **> 1,000** | ไม่มีความสำคัญทางคลินิก |
| Eosinophil | 1–4% | **> 500** (hypereosinophilia **> 1,500**) | ไม่มีความสำคัญทางคลินิก |
| Basophil | 0.5–1% | **> 300** | ไม่มีความสำคัญทางคลินิก |

### หลักที่สำคัญที่สุด — ตัดสินด้วย absolute count เสมอ
**Absolute count = % differential × WBC รวม** (สไลด์) · สำหรับ neutrophil ให้รวม band ด้วย: **ANC = WBC × (% segmented + % band)**
- ตัวอย่าง: WBC 3,000 · neutrophil 35% · lymphocyte 60%
  - ANC = 3,000 × 0.35 = **1,050 → neutropenia จริง**
  - lymphocyte = 3,000 × 0.60 = **1,800 → ปกติ** — เปอร์เซ็นต์สูงเพราะ neutrophil หายไป = **relative lymphocytosis** ไม่ใช่โรคของ lymphocyte
- กลับกัน: WBC 20,000 · lymphocyte 20% = **4,000 → absolute lymphocytosis** แม้ % จะดูปกติ

### แผนที่ของเม็ดเลือดขาว — คิดเป็นสองแกน
[[fig:hemtree]]
| | **สาย myeloid** | **สาย lymphoid** |
|---|---|---|
| **Acute** — ค้างที่ blast | **AML** | **ALL** |
| **Chronic** — เจริญได้ แต่มากเกิน | **CML** (และ MPN อื่น) | **CLL** |
| ก่อก้อนในต่อม/ม้าม | — | **Lymphoma** (Hodgkin, NHL) |
| โรคของ progenitor | **MDS** → AML ได้ | — |

### ถามสามคำถามทุกครั้งที่ WBC ผิดปกติ
1. **เซลล์ชนิดไหน** ผิดปกติ — ดู absolute count ทีละชนิด ไม่ใช่ดูแค่ WBC รวม
2. **Reactive หรือ clonal** — มีสาเหตุชัด (ติดเชื้อ ยา stress) และหายเมื่อสาเหตุหาย = reactive · หาสาเหตุไม่ได้ เรื้อรัง ม้ามโต = นึกถึง clonal
3. **ตัวแก่หรือตัวอ่อน** — เห็น **blast** ในเลือด = ภาวะเร่งด่วน ต้องคิดถึง acute leukemia จนกว่าจะพิสูจน์ได้ว่าไม่ใช่
""",
    ["Absolute count = % × WBC — ตัดสินทุกอย่างด้วย absolute",
     "ANC รวม band ด้วย · ANC < 1,500 = neutropenia",
     "Leukocytosis > 11,000 · leukemoid > 50,000",
     "Acute = ค้างที่ blast · chronic = เจริญได้แต่มากเกิน",
     "เห็น blast ในเลือด = คิดถึง acute leukemia จนกว่าจะพิสูจน์ว่าไม่ใช่"],
    [mcq(N(1), "A 34-year-old woman has a CBC: WBC 2,800/µL with 30% segmented neutrophils, 5% bands, 58% lymphocytes, 6% monocytes and 1% eosinophils. Which interpretation is correct?",
         ["Normal ANC with absolute lymphocytosis", "Mild neutropenia (ANC about 1,400/µL)", "Moderate neutropenia (ANC about 980/µL) with a normal absolute lymphocyte count",
          "Severe neutropenia (ANC about 280/µL)", "Agranulocytosis with lymphocytosis"], 2,
         "**ANC = WBC × (% segmented + % band)** = 2,800 × 0.35 = **980/µL** → อยู่ในช่วง **500–1,000 = moderate neutropenia** (สไลด์)\n\n"
         "Lymphocyte = 2,800 × 0.58 = **1,624/µL** → **ปกติ** (lymphocytosis ต้อง > 3,500) — เปอร์เซ็นต์ที่สูงเป็นแค่ **relative lymphocytosis** จาก neutrophil ที่ลดลง\n\n"
         "- 1,400 และ 280 มาจากการคูณผิด (ต้องใช้ % segmented + band = 35%) · agranulocytosis = ANC < 500 · lymphocyte ไม่ถึง 3,500 จึงไม่ใช่ lymphocytosis",
         "ตัดสินด้วย absolute count — % ที่สูงอาจเป็นแค่เงาของอีกเซลล์ที่ลดลง", "Absolute cell count", R("Leukocytosis; Neutropenia"), CBC + ["2.3.3(2)"]),
     mcq(N(2), "In a CBC report, which statement about absolute counts is correct?",
         ["A lymphocyte percentage of 55% always indicates a lymphoproliferative disorder",
          "Leukocytosis is defined by the slides as a WBC above 11,000/µL, and a leukemoid reaction as above 50,000/µL",
          "Eosinophilia is defined as an eosinophil percentage above 4% regardless of the total WBC",
          "Monocytopenia below 200/µL is a clinically important cause of infection",
          "Absolute neutrophil count excludes band forms"], 1,
         "สไลด์ให้เกณฑ์ **leukocytosis > 11,000/µL** และ **leukemoid reaction > 50,000/µL** (George TI, ASH 2012)\n\n"
         "- % lymphocyte สูงอาจเป็น **relative** ต้องคูณ WBC ก่อน\n- eosinophilia ใช้ **absolute > 500/µL** ไม่ใช่ %\n"
         "- สไลด์ระบุว่า monocytopenia eosinopenia basopenia **ไม่มีความสำคัญทางคลินิก**\n- ANC **รวม band**",
         "ทุกเกณฑ์ในสไลด์เป็น absolute /µL", "Leukocytosis definitions", R("Leukocytosis; Leukopenia"), CBC),
    ], CBC + ["B2.1.2(3)"], SRC + " · Berliner (Cecil 24th) · George TI (ASH 2012)", F1)

# ───────────────────────────── 2
POOLROWS = [(1, "Demargination — ภายในไม่กี่นาที", "adrenaline · ออกกำลังกาย · stress เฉียบพลัน → ไม่มี left shift"),
            (2, "ดึงจาก storage pool — ภายในชั่วโมง", "endotoxin · corticosteroid · ติดเชื้อ → เริ่มเห็น band"),
            (3, "ออกสู่เนื้อเยื่อน้อยลง", "corticosteroid ลด adhesion molecule → ค้างอยู่ในเลือด"),
            (4, "สร้างเพิ่ม — ใช้เวลาหลายวัน", "G-CSF จากการติดเชื้อ/อักเสบ · มะเร็ง · CML (อยู่นานขึ้นด้วย)")]
F2 = {"pools": fig("Neutrophil อยู่ 5 คลัง — CBC นับได้แค่คลังเดียว",
 "Neutrophil ส่วนใหญ่ของร่างกาย **อยู่ในไขกระดูก** (mitotic → maturation → storage pool) และในเลือดเองก็ **เกาะผนังหลอดเลือดอยู่ราวครึ่งหนึ่ง (marginal pool)** — "
 "CBC นับได้เฉพาะ **circulating pool** ดังนั้น WBC ขึ้นได้โดย **ไม่ต้องสร้างเซลล์ใหม่เลย** แค่ย้ายเซลล์จากคลังหนึ่งไปอีกคลัง · "
 "ความเร็วบอกกลไก: ขึ้นภายใน **นาที** = หลุดจากผนัง (1) · ภายใน **ชั่วโมง** = ดึงจากคลังในไขกระดูก (2) หรือออกสู่เนื้อเยื่อน้อยลง (3) · ใช้เวลา **หลายวัน** = สร้างเพิ่ม (4) "
 "(ดัดแปลงจากสไลด์ Mechanism of neutrophilia — Williams Hematology 8th)",
 svg(420, 392, "แผนภาพคลังของ neutrophil ในไขกระดูก ในเลือด และในเนื้อเยื่อ พร้อมกลไกทำให้ neutrophil สูงสี่แบบ",
     t(69, 24, "ไขกระดูก", "sm b mid tac"), t(230, 24, "ในเลือด", "sm b mid twa"), t(371, 24, "เนื้อเยื่อ", "sm b mid i2"),
     box(14, 34, 110, 36, "ac", "Mitotic pool", fs=12), ar(69, 70, 69, 84, "lac", "ah-ac"),
     box(14, 84, 110, 36, "ac", "Maturation", fs=12), ar(69, 120, 69, 134, "lac", "ah-ac"),
     box(14, 134, 110, 62, "ac", "Storage pool\n(band · seg)", fs=12),
     t(69, 212, "อยู่ในไขกระดูกหลายวัน", "xs mid mu"),
     box(170, 56, 120, 44, "sk", "Marginal pool\nเกาะผนังหลอดเลือด", fs=11.5),
     path("M230 104 L230 126", "ln", "ah", "ah"),
     box(170, 130, 120, 44, "wa", "Circulating pool\nส่วนที่ CBC นับได้", fs=11.5),
     ar(124, 168, 168, 158), ar(290, 152, 334, 152),
     box(336, 126, 70, 52, "bx", "เนื้อเยื่อ", fs=12),
     badge(250, 115, 1), badge(140, 150, 2), badge(312, 138, 3), badge(140, 52, 4),
     *[badge(24, 236 + i * 40, n) + t(40, 240 + i * 40, a, "sm b") + t(40, 256 + i * 40, b, "xs i2")
       for i, (n, a, b) in enumerate(POOLROWS)]))}

NEU = ["B2.1.2(3)", "3.3.1", "3.1.2"]
sec("hon-wbc-02", "กลไกของ neutrophilia — neutrophil 5 คลัง",
    "Mitotic maturation storage marginal circulating · demargination (นาที) storage release (ชั่วโมง) egress ลดลง proliferation (วัน) · steroid · left shift toxic granulation · สาเหตุ 5 กลุ่ม", 9,
"""### ทำไม WBC ขึ้นได้ภายในไม่กี่นาที (สไลด์)
CBC ไม่ได้วัดจำนวน neutrophil ทั้งร่างกาย — วัดได้แค่ส่วนที่ **ลอยอยู่ในกระแสเลือด** ณ เวลาที่เจาะ
[[fig:pools]]
| กลไก (สไลด์) | ตัวกระตุ้น | เร็วแค่ไหน | ใน smear |
|---|---|---|---|
| **Marginal → circulating pool** (demargination) | **Exercise · adrenaline** · stress เฉียบพลัน ชัก | นาที | เซลล์ตัวแก่ ไม่มี left shift |
| **Storage pool → เลือด** | **Endotoxin · corticosteroids** · ติดเชื้อ hypoxia intoxication | ชั่วโมง | เริ่มมี band |
| **ออกสู่เนื้อเยื่อน้อยลง (egress ↓)** | **Corticosteroids** | ชั่วโมง | ตัวแก่ |
| **สร้างเพิ่ม (proliferation)** | **Infection · inflammation · malignancy · endocrinopathy · post-neutropenia** | หลายวัน | left shift + toxic granulation |
| **อยู่ในเลือดนานขึ้น** + สร้างเพิ่มแบบ clone | **CML** | สัปดาห์–เดือน | ตัวอ่อนครบทุกระยะ |

#### ทำไมถึงมีอาการนี้ — ลักษณะใน smear บอกกลไก
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Left shift** (band metamyelocyte myelocyte) | ความต้องการสูงจน storage pool หมด ไขกระดูกต้อง **ปล่อยตัวอ่อนออกมาก่อนกำหนด** (✍️ "เจอตัวอ่อน") | ติดเชื้อแบคทีเรีย อักเสบรุนแรง |
| **Toxic granulation** | G-CSF เร่งการเจริญจนเม็ด primary (azurophilic) **ยังติดสีเข้มอยู่** ตอนเซลล์ออกสู่เลือด | ✍️ บ่งชี้การติดเชื้อ |
| **Cytoplasmic vacuolization** | ช่องว่างจาก **การกินเชื้อและย่อยภายในเซลล์** | sepsis/bacteremia |
| WBC ขึ้นหลังให้ steroid แต่ **ไม่มี left shift ไม่มี toxic granule** และ **eosinophil หายไป** | demargination + ดึงจากคลัง + ออกสู่เนื้อเยื่อน้อยลง · steroid ทำให้ eosinophil และ lymphocyte ไปอยู่ในเนื้อเยื่อและตาย | ✍️ "ใช้ steroid" — อย่าแปลว่าติดเชื้อจาก WBC อย่างเดียว |
| WBC ขึ้นหลังออกกำลัง ชัก หรือตื่นเต้น แล้วลงเองในไม่กี่ชั่วโมง | adrenaline ปลด neutrophil ที่เกาะผนังออกมา | ไม่ต้องสืบค้นต่อ |

### สาเหตุของ neutrophilia (สไลด์)
| กลุ่ม | ตัวอย่าง |
|---|---|
| **Infection & inflammation** | ติดเชื้อแบคทีเรีย การอักเสบเรื้อรัง |
| **Stress** | exercise, convulsions, pain, labor, anesthesia, surgery, cold, heat, burns, electric shock, trauma, infarction, emotional stress |
| **Drug** | **G-CSF, epinephrine, glucocorticoids** (✍️ วงไว้), androgen, lithium, vaccines |
| **Malignancy** | solid cancer โดยเฉพาะระยะลุกลาม (เนื้องอกสร้าง G-CSF ได้) · lymphoma, MM · **CML** |
| **Miscellaneous** | pregnancy, preeclampsia, thyroid storm, ACTH เกิน, **smoking**, venoms, ethylene glycol, หลังภาวะ neutropenia, hemolysis หรือ hemorrhage, **หลังตัดม้าม**, Down syndrome, congenital neutrophilia |
- **หลังตัดม้าม** — ม้ามเป็นที่กักและทำลายเซลล์เม็ดเลือด เมื่อไม่มีม้าม neutrophil และเกล็ดเลือดอยู่ในเลือดนานขึ้น
- **สูบบุหรี่** — การอักเสบเรื้อรังของทางเดินหายใจ WBC สูงเล็กน้อยได้ตลอด
""",
    ["CBC นับได้แค่ circulating pool",
     "นาที = demargination · ชั่วโมง = storage release · วัน = สร้างเพิ่ม",
     "Steroid: WBC ขึ้น ไม่มี left shift eosinophil หาย",
     "Left shift + toxic granulation + vacuole = นึกถึงติดเชื้อแบคทีเรีย",
     "หลังตัดม้าม neutrophil และเกล็ดเลือดสูงได้ถาวร"],
    [mcq(N(3), "A 60-year-old man with COPD exacerbation receives IV methylprednisolone. Six hours later his WBC has risen from 8,000 to 16,500/µL with 88% mature segmented neutrophils, no bands, no toxic granulation and eosinophils 0%. He is afebrile. What is the best explanation?",
         ["New bacterial pneumonia with marrow proliferation", "Release from the marrow storage pool, demargination and reduced egress into tissues",
          "Leukemoid reaction requiring BCR-ABL1 testing", "Increased proliferation of the mitotic pool", "Early chronic myeloid leukemia"], 1,
         "Corticosteroid ทำให้ neutrophil สูงได้ **ภายในชั่วโมง** โดย **ไม่ต้องสร้างใหม่** (สไลด์ Mechanism of neutrophilia):\n"
         "- ดึงจาก **marrow storage pool** · ลด adhesion → **demargination** · และ **ลดการออกสู่เนื้อเยื่อ (egress)**\n"
         "- จึงเป็นเซลล์ **ตัวแก่ ไม่มี band ไม่มี toxic granule** และ steroid ทำให้ **eosinophil ลดจนเป็นศูนย์**\n\n"
         "การสร้างเพิ่มใน mitotic pool ใช้เวลา **หลายวัน** · ติดเชื้อมักมี left shift/toxic granulation · leukemoid ต้อง > 50,000",
         "Steroid → WBC ขึ้นเร็ว ไม่มี left shift eosinophil หาย", "Mechanism of neutrophilia", R("Mechanism of neutrophilia"), NEU + ["B11.4(3)"]),
     mcq(N(4), "A healthy 22-year-old has blood drawn immediately after a 10-km race; WBC is 15,000/µL with mature neutrophils. A repeat count 3 hours later is 7,200/µL. Which mechanism explains the first result?",
         ["Increased granulopoiesis driven by G-CSF", "Shift of neutrophils from the marginal pool to the circulating pool",
          "Decreased neutrophil apoptosis in tissues", "Release of myelocytes from the maturation pool", "Splenic sequestration"], 1,
         "การออกกำลังกายหลั่ง **adrenaline** → neutrophil ที่ **เกาะผนังหลอดเลือด (marginal pool)** หลุดเข้ากระแสเลือด → WBC ขึ้นภายใน **นาที** และกลับเป็นปกติในไม่กี่ชั่วโมง (สไลด์: exercise, adrenaline = marginal storage pool shift)\n\n"
         "- G-CSF/proliferation ใช้เวลาหลายวัน\n- myelocyte ออกมาในเลือด = left shift ไม่ใช่กรณีนี้\n- splenic sequestration ทำให้ **ลดลง** ไม่ใช่เพิ่ม",
         "WBC ขึ้นในไม่กี่นาทีแล้วลงเอง = demargination", "Mechanism of neutrophilia", R("Mechanism of neutrophilia"), NEU),
    ], NEU, SRC + " · Williams Hematology 8th", F2)

# ───────────────────────────── 3
def XL(v):
    return 40 + (math.log10(v) - 3) * 126.67
AXROWS = [("Reactive neutrophilia", "ติดเชื้อ · stress · steroid", 11000, 30000, "ms"),
          ("Leukemoid reaction", "> 50,000 · LAP สูง · มีสาเหตุ", 50000, 100000, "ms"),
          ("CML", "ตัวอ่อนครบทุกระยะ · baso ↑", 30000, 500000, "ac"),
          ("Acute leukemia", "ต่ำ ปกติ หรือสูงก็ได้ — ดู blast", 1000, 400000, "bad da"),
          ("CLL", "lymphocyte เล็ก · smudge cell", 5000, 300000, "wa")]
F3 = {"wbcaxis": fig("WBC เท่าไรบอกอะไรได้บ้าง — และบอกอะไรไม่ได้",
 "แกนนอนเป็น **สเกล log** (1k = 1,000/µL) · แถบเขียว = ค่าปกติ 4,000–11,000 · แถบแดง = **hyperleukocytosis > 100,000** · "
 "ตัวเลข WBC อย่างเดียวแยกโรคไม่ได้ เพราะช่วงซ้อนกันมาก — **leukemoid reaction กับ CML ซ้อนกันที่ 50,000–100,000** ต้องดู smear (basophil, ตัวอ่อนครบทุกระยะ) LAP และ BCR::ABL1 · "
 "**Acute leukemia มี WBC ได้ตั้งแต่ต่ำมากจนสูงมาก** (เส้นประ) ตัวชี้คือ **blast** ไม่ใช่จำนวน · CLL สูงถึงหลายแสนได้แต่ไม่ค่อยเกิด leukostasis (หัวข้อ 8) "
 "*(ช่วงตัวเลขของแต่ละโรคเป็นค่าโดยประมาณจากตำรา ไม่ได้อยู่ในสไลด์)*",
 svg(440, 302, "แกน WBC สเกล log เทียบช่วงของ reactive neutrophilia leukemoid reaction CML acute leukemia และ CLL",
     rect(XL(4000), 24, XL(11000) - XL(4000), 232, "ok ns", 0), rect(XL(100000), 24, 420 - XL(100000), 232, "bad ns", 0),
     t((XL(4000) + XL(11000)) / 2, 18, "ปกติ", "xs b mid tok"), t(XL(100000) + 4, 18, "hyperleukocytosis", "xs b tbad"),
     *[line(XL(v), 24, XL(v), 256, "lru da") for v in (4000, 11000, 50000, 100000)],
     *[t(40, 46 + i * 42, n, "sm b") + t(432, 46 + i * 42, d, "xs i2 end") + rect(XL(a), 53 + i * 42, XL(b) - XL(a), 12, c, 6)
       for i, (n, d, a, b, c) in enumerate(AXROWS)],
     line(40, 256, 420, 256, "ln"),
     *[line(XL(v), 256, XL(v), 262, "ln") + t(XL(v), 276, lab, "xs mid")
       for v, lab in ((1000, "1k"), (4000, "4k"), (11000, "11k"), (50000, "50k"), (100000, "100k"), (1000000, "1M"))],
     t(230, 294, "WBC (/µL) — สเกล log", "xs mid mu")))}
F3["bcrabl"] = fig("CML — ยีนเดียวอธิบายอาการได้ทั้งหมด",
 "**t(9;22)** ย้าย **ABL1** จากโครโมโซม 9 ไปต่อกับ **BCR** บนโครโมโซม 22 → โครโมโซม 22 ที่สั้นลง = **Philadelphia chromosome** · "
 "โปรตีน **BCR::ABL1 เป็น tyrosine kinase ที่เปิดค้างตลอด** สั่งให้เซลล์ myeloid แบ่งตัวและไม่ตาย แต่ **ยังเจริญเป็นตัวแก่ได้** → เลือดเต็มไปด้วย granulocyte ทุกระยะ basophil eosinophil และเกล็ดเลือด · "
 "ไขกระดูกล้นจน **ม้ามกลายเป็นที่สร้างเม็ดเลือด** → ม้ามโตมาก · **ยา TKI (imatinib) เข้าไปอุดช่องจับ ATP ของ kinase** จึงหยุดต้นเหตุได้ตรงจุด "
 "*(กลไกระดับโมเลกุลและยา ไม่ได้อยู่ในสไลด์)*",
 svg(420, 372, "กลไก t(9;22) สร้าง BCR::ABL1 kinase ทำให้เกิดลักษณะของ CML และจุดที่ยา imatinib ยับยั้ง",
     rect(40, 24, 22, 104, "bx", 10), rect(40, 98, 22, 16, "acf", 0), t(36, 110, "ABL1", "xs b tac end"), t(51, 146, "chr 9", "xs mid b"),
     rect(100, 44, 22, 64, "bx", 10), rect(100, 70, 22, 12, "waf", 0), t(126, 80, "BCR", "xs b twa"), t(111, 146, "chr 22", "xs mid b"),
     ar(132, 104, 188, 104, "ln", "ah", "t(9;22)", "xs i2 mid"),
     rect(196, 44, 22, 58, "bx", 10), rect(196, 72, 22, 10, "waf", 0), rect(196, 82, 22, 18, "acf", 0),
     t(207, 118, "Ph", "sm b mid"), t(207, 132, "der(22)", "xs mid mu"),
     t(226, 92, "BCR::ABL1", "sm b tac"),
     box(300, 22, 106, 54, "ok", "TKI (imatinib)\nอุดช่องจับ ATP", fs=11.5),
     ar(254, 100, 254, 150, "lac", "ah-ac"), tbar(353, 78, 353, 148),
     box(40, 152, 340, 38, "bad", "BCR::ABL1 tyrosine kinase ทำงานตลอดเวลา", fs=12.5),
     fan(210, 190, [77, 210, 343], 202, 213),
     box(14, 214, 126, 40, "ac", "สร้าง granulocyte\nทุกระยะเพิ่ม", fs=11.5),
     box(147, 214, 126, 40, "ac", "ไขกระดูกล้น\nสร้างนอกไขกระดูก", fs=11.5),
     box(280, 214, 126, 40, "ac", "เซลล์เกิด-ตาย\nเร็วมาก", fs=11.5),
     ar(77, 254, 77, 269), ar(210, 254, 210, 269), ar(343, 254, 343, 269),
     box(14, 270, 126, 42, "ms", "WBC สูง ตัวอ่อนครบ\nbaso · eos · plt ↑", fs=11.5),
     box(147, 270, 126, 42, "ms", "ม้ามโตมาก\nอิ่มเร็ว จุกท้องซ้าย", fs=11.5),
     box(280, 270, 126, 42, "ms", "uric acid ↑ (gout)\nเหงื่อออก ผอมลง", fs=11.5),
     ar(77, 312, 77, 329),
     box(14, 330, 392, 32, "bx", "Basophil ↑ → หลั่ง histamine → คันทั้งตัว · แผลในกระเพาะ", fs=12)))

CML = ["B2.2.4-3(1)", "B2.2.4-3(2)", "3.1.2"]
sec("hon-wbc-03", "Left shift, leukemoid reaction และ CML",
    "Toxic granulation vacuolization · leukemoid > 50,000 LAP สูง มีสาเหตุ · CML: ม้ามโตไม่ทราบสาเหตุ myelocyte basophil eosinophil LAP ต่ำ Ph+ · ทำไมม้ามโต อิ่มเร็ว คัน", 11,
"""### Leukemoid reaction (สไลด์)
**WBC > 50,000/µL จากสาเหตุ reactive** — ไขกระดูกปกติที่ถูกกระตุ้นอย่างหนัก (ติดเชื้อรุนแรง เช่น C. difficile วัณโรค · เลือดออก/hemolysis รุนแรง · มะเร็งที่สร้าง G-CSF) ไม่ใช่มะเร็งของเม็ดเลือด
[[fig:wbcaxis]]
### Leukemoid VS Leukemia (CML) — ตารางในสไลด์
| | **Reactive neutrophilia / Leukemoid reaction** | **CML** |
|---|---|---|
| ไข้ ม้ามโต | **ขึ้นกับสาเหตุ reactive** | **ม้ามโตโดยหาสาเหตุไม่ได้** (✍️ ขีดเส้นใต้) · ไข้เฉพาะ **ระยะลุกลาม** |
| Smear | myelocyte metamyelocyte **band เพิ่ม** · **toxic granule** (✍️ infection) · vacuolization | **myelocyte** promyelocyte blast · **basophil และ eosinophil เพิ่ม** (✍️ ไฮไลต์) |
| **LAP score** | **สูง** | **ต่ำ** |
| ยืนยัน | **มีสาเหตุ reactive** · DDx chronic neutrophilic leukemia (พบน้อย) | **Philadelphia chromosome t(9;22) หรือ BCR-ABL1 บวก** |

**ทำไม LAP ต่างกัน** — leukocyte alkaline phosphatase เป็นเอนไซม์ใน granule ของ neutrophil ตัวแก่ที่ **ถูกกระตุ้นด้วย G-CSF และการอักเสบ** → leukemoid สูง · neutrophil ของ CML มาจาก clone ผิดปกติที่ **สร้างเอนไซม์นี้น้อย** → ต่ำ *(ปัจจุบันใช้ BCR::ABL1 แทน LAP เป็นหลัก)*

### CML — smear ในสไลด์
**RBC normochromic normocytic · leukocytosis ที่มี myeloid ทุกระยะ (multistage) · eosinophil และ basophil เพิ่ม · เกล็ดเลือดเพิ่ม** — ตัวอ่อนในเลือดมีครบทุกขั้นตั้งแต่ blast ถึงตัวแก่ โดยมี myelocyte กับ segmented มากที่สุด (ต่างจาก acute leukemia ที่มี blast มากแต่ตัวกลาง ๆ หายไป)
[[fig:bcrabl]]
#### ทำไมถึงมีอาการนี้ — CML
| อาการ/อาการแสดง | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ม้ามโตมาก** (คลำได้ถึงสะดือหรืออุ้งเชิงกราน) | ไขกระดูกล้น → **สร้างเม็ดเลือดนอกไขกระดูก** ที่ม้าม + เซลล์ myeloid จำนวนมากไปสะสม | leukemoid ม้ามไม่โตจากตัวมันเอง |
| **อิ่มเร็ว จุกแน่นท้องซ้าย** | ม้ามที่ใหญ่ **ดันกระเพาะอาหาร** | ถามทุกรายที่ WBC สูงเรื้อรัง |
| **ปวดชายโครงซ้ายร้าวไหล่ซ้ายเฉียบพลัน** | ม้ามโตเร็วเกินเลือดเลี้ยง → **splenic infarction** ระคายกะบังลม (เส้นประสาท phrenic C3–5) | infarct ม้าม |
| **คันทั้งตัว ร้อนวูบวาบ แผลในกระเพาะ** | **basophil หลั่ง histamine** | basophilia เป็นเบาะแสของ CML ที่ leukemoid ไม่มี |
| **เกาต์ นิ่วกรดยูริก** | เซลล์เกิดและตายเร็ว → purine → **uric acid สูง** | |
| เหงื่อออก น้ำหนักลด อ่อนเพลีย | hypermetabolism + cytokine + ซีด | |
| เกล็ดเลือดสูง | BCR::ABL1 กระตุ้นทุกสาย myeloid รวม megakaryocyte | |
| **ไข้ ปวดกระดูก ซีดและเลือดออกมากขึ้น** | ระยะลุกลาม — **blast เพิ่มขึ้นจนกลายเป็น acute leukemia (blast phase)** | สไลด์: fever in advanced phase |

### ระยะของโรคและการรักษา *(ไม่ได้มาจากสไลด์)*
- ส่วนใหญ่พบใน **chronic phase** (อาการน้อย มักเจอจาก CBC) → ถ้าไม่รักษาจะเข้าสู่ **blast phase (blast ≥ 20%)** ซึ่งเป็น acute leukemia ที่รักษายาก · **WHO 5th edition (2022)** ตัด accelerated phase ออกเหลือ chronic กับ blast phase ส่วน **ICC 2022** ยังคง accelerated phase ไว้
- **ยามุ่งเป้า TKI** — imatinib หรือรุ่นที่สอง (dasatinib nilotinib bosutinib) กินต่อเนื่อง · ก่อนผลยืนยันอาจให้ **hydroxyurea** ลดจำนวนเซลล์
- ติดตามด้วย **BCR::ABL1 RQ-PCR (international scale)** — เป้าหมายตาม **ELN 2020**: **≤ 10% ที่ 3 เดือน · ≤ 1% ที่ 6 เดือน · ≤ 0.1% (MMR) ที่ 12 เดือน**
- ผู้ป่วยที่ตอบสนองดีมีอายุใกล้เคียงคนทั่วไป บางรายหยุดยาได้ภายใต้การติดตามใกล้ชิด
""",
    ["Leukemoid = > 50,000 + สาเหตุ reactive + toxic granule + LAP สูง",
     "CML = ม้ามโตไม่ทราบสาเหตุ + myelocyte + basophil/eosinophil + LAP ต่ำ + Ph+",
     "Basophilia เป็นเบาะแสสำคัญที่ leukemoid ไม่มี",
     "ม้ามโตใน CML = สร้างเม็ดเลือดนอกไขกระดูก → อิ่มเร็ว",
     "รักษาด้วย TKI ติดตาม BCR::ABL1 ตาม ELN 2020"],
    [mcq(N(5), "A 50-year-old man with severe Clostridioides difficile colitis has WBC 64,000/µL with many bands, metamyelocytes, toxic granulation and cytoplasmic vacuoles. Basophils are not increased and the spleen is not palpable. Which additional finding would best support the most likely diagnosis?",
         ["Low leukocyte alkaline phosphatase (LAP) score", "Philadelphia chromosome on karyotype", "High leukocyte alkaline phosphatase (LAP) score",
          "Absolute basophilia", "Myeloblasts 25% in peripheral blood"], 2,
         "ภาพนี้คือ **leukemoid reaction** — WBC > 50,000 จาก **สาเหตุ reactive ชัดเจน** (C. difficile) มี **toxic granulation และ vacuolization** ม้ามไม่โต basophil ไม่เพิ่ม\n\n"
         "สไลด์: leukemoid reaction มี **LAP score สูง** เพราะ neutrophil ตัวแก่ถูกกระตุ้นด้วย G-CSF\n\n"
         "- LAP ต่ำ · Ph chromosome · basophilia = ลักษณะของ **CML**\n- blast 25% = **acute leukemia**",
         "Leukemoid: มีสาเหตุ + toxic granule + LAP สูง", "Leukemoid vs CML", R("Leukemoid VS Leukemia"), CML + ["2.2.48"]),
     mcq(N(6), "A 47-year-old woman with CML (WBC 210,000/µL, spleen palpable 14 cm below the left costal margin) reports that she feels full after a few spoonfuls of rice, and since this morning has sharp left upper quadrant pain radiating to the left shoulder tip. Which mechanism best explains both complaints?",
         ["Basophil histamine release causing gastric hypersecretion", "Leukostasis in mesenteric vessels",
          "Massive splenomegaly from extramedullary haematopoiesis compressing the stomach, with splenic infarction irritating the diaphragm",
          "Hyperuricaemia causing renal colic", "Portal vein thrombosis from thrombocytosis"], 2,
         "ใน CML ไขกระดูกล้นจน **ม้ามกลายเป็นที่สร้างเม็ดเลือด (extramedullary haematopoiesis)** และมีเซลล์ myeloid สะสม → **ม้ามโตมาก**\n"
         "- ม้ามดันกระเพาะ → **อิ่มเร็ว (early satiety)**\n- ม้ามโตเกินเลือดเลี้ยง → **splenic infarction** → ระคายกะบังลม → **ปวดร้าวไหล่ซ้าย** (เส้นประสาท phrenic C3–5)\n\n"
         "Histamine จาก basophil ทำให้คันและแผลในกระเพาะ แต่ไม่ทำให้ปวดร้าวไหล่ · leukostasis มักเกิดที่ปอดและสมอง",
         "CML: ม้ามโต → อิ่มเร็ว · ปวดไหล่ซ้าย = ม้ามขาดเลือด", "CML clinical features", R("Leukemoid VS Leukemia; CML"), CML),
     mcq(N(7), "Which feature most reliably distinguishes chronic myeloid leukemia from a leukemoid reaction at the bedside before cytogenetics is available?",
         ["WBC above 50,000/µL", "Presence of myelocytes in the peripheral smear", "Absolute basophilia with eosinophilia and unexplained splenomegaly",
          "Presence of band forms", "Normocytic anaemia"], 2,
         "สไลด์ Leukemoid VS Leukemia: **CML = unexplained splenomegaly + myelocyte promyelocyte blast + increased basophils, eosinophils** (✍️ ไฮไลต์)\n\n"
         "- WBC > 50,000 พบได้ทั้งคู่\n- **myelocyte และ band** พบใน leukemoid ได้เช่นกัน (left shift)\n- ซีดพบได้ทั้งสองภาวะ\n\n"
         "basophil เพิ่มเพราะ BCR::ABL1 กระตุ้นทุกสาย myeloid — การติดเชื้อไม่ทำให้ basophil สูง",
         "Basophilia + ม้ามโตไม่ทราบสาเหตุ = นึกถึง CML", "Leukemoid vs CML", R("Leukemoid VS Leukemia"), CML),
    ], CML, SRC + " · Williams Hematology 8th · ELN 2020 · WHO 5th 2022/ICC 2022", F3)

# ───────────────────────────── 4
F4 = {"lymphflow": fig("Lymphocytosis — reactive หรือ clone? สามขั้นในสไลด์",
 "ขั้นที่ 1 หา **สาเหตุ reactive** (ติดเชื้อ ยา) · ขั้นที่ 2 **ดู smear**: reactive lymphocyte **หลายขนาดหลายหน้าตา (pleomorphic)** เพราะเป็นเซลล์ปกติหลายตัวที่ถูกกระตุ้นต่างระยะกัน ส่วน clone มะเร็ง **หน้าตาเหมือนกันหมด (monomorphic)** (✍️ \"หน้าเหมือนกันหมด\") และใน CLL มี **smudge cell** · "
 "ขั้นที่ 3 **flow cytometry** ดู light chain บนผิว B cell: B cell ปกติใช้ทั้ง κ และ λ (ราว 2:1) · ถ้า **ใช้ light chain ชนิดเดียว = มาจากเซลล์ต้นกำเนิดเดียว (monoclonal)** "
 "(ภาพเซลล์และ κ/λ วาดเพื่ออธิบาย ไม่ได้อยู่ในสไลด์)",
 svg(420, 356, "ขั้นตอนประเมิน lymphocytosis หาสาเหตุ reactive ดู smear pleomorphic หรือ monomorphic และ flow cytometry ดู kappa lambda",
     box(60, 10, 300, 32, "ac", "Absolute lymphocyte > 3,500/µL", fs=12.5),
     ar(132, 42, 132, 57),
     rect(14, 58, 236, 38, "bx"), badge(30, 77, 1), t(46, 81, "มีสาเหตุชัด? ไข้ ไวรัส ไอกรน ยา", "sm"),
     ar(250, 77, 273, 77, "lok", "ah-ok"),
     box(274, 58, 132, 38, "ok", "ใช่ → reactive\nติดตามจนหาย", fs=11.5),
     ar(132, 96, 132, 111), t(140, 107, "ไม่ชัด / ไม่หาย", "xs mu"),
     rect(14, 112, 392, 26, "bx"), badge(30, 125, 2), t(46, 129, "Blood smear — ดูหน้าตาของเซลล์", "sm b"),
     rect(14, 146, 192, 88, "ok"), rect(214, 146, 192, 88, "ms"),
     t(24, 163, "Pleomorphic", "sm b tok"), t(224, 163, "Monomorphic", "sm b tms"),
     ell(50, 194, 19, 14, "wa"), ell(46, 194, 9, 8, "waf"),
     cell(92, 190, 11, 7), cell(124, 199, 7, 5.5), ell(162, 192, 13, 10, "wa"), circ(168, 192, 6, "waf"),
     t(110, 226, "หลายขนาด หลายหน้าตา → reactive", "xs mid i2"),
     *[cell(236 + k * 23, 192, 8, 6.5) for k in range(4)],
     path("M330 186 q9 -9 19 -2 q10 6 4 15 q-7 9 -18 5 q-11 -6 -5 -18z", "waf"), t(384, 197, "smudge", "xs mid i2"),
     t(310, 226, "เหมือนกันหมด → สงสัย clone", "xs mid i2"),
     ar(310, 234, 310, 249),
     rect(14, 250, 392, 26, "bx"), badge(30, 263, 3), t(46, 267, "Flow cytometry — light chain κ : λ", "sm b"),
     t(24, 300, "Polyclonal", "sm b tok"),
     t(36, 322, "κ", "xs b end"), rect(42, 312, 80, 12, "okf", 3), t(36, 340, "λ", "xs b end"), rect(42, 330, 40, 12, "okf", 3),
     t(132, 322, "κ : λ ≈ 2 : 1", "xs i2"), t(132, 340, "= reactive", "xs i2"),
     t(224, 300, "Monoclonal", "sm b tbad"),
     t(236, 322, "κ", "xs b end"), rect(242, 312, 120, 12, "badf", 3), t(236, 340, "λ", "xs b end"), rect(242, 330, 3, 12, "badf", 1),
     t(252, 340, "λ ≈ 0 → clone เช่น CLL", "xs i2")))}

LYM = ["3.1.2", "B2.2.2(6)", "B2.2.4-3(1)", "B2.2.4-3(3)"]
sec("hon-wbc-04", "Monocytosis และ lymphocytosis — reactive หรือ clone",
    "Monocytosis > 1,000: TB SBE CMV dengue malaria vs CMML AML M4/5 · lymphocytosis > 3,500: mononucleosis syndrome vs lymphoid neoplasm · สามขั้น smear pleomorphic/monomorphic flow cytometry · หน้าตาเซลล์ใน smear", 11,
"""### Monocytosis > 1,000/µL (สไลด์)
| | สาเหตุ |
|---|---|
| **Reactive — infection** | **Tuberculosis, syphilis, subacute bacterial endocarditis**, CMV, VZV, dengue, malaria |
| Reactive — inflammation / stress | การอักเสบเรื้อรัง · surgery, trauma, pregnancy, labor, MI |
| Reactive — miscellaneous | หลังตัดม้าม · **หลังยาเคมี (post CMT) และหลังปลูกถ่ายไขกระดูก** · corticosteroids · solid cancer, MM, lymphoma |
| **Myeloid neoplasms** (✍️ "BM abnormal") | **CMML**, CML, atypical CML, JMML, **AML M4/M5** (myelomonocytic/monocytic) |
- **ทำไมโรคติดเชื้อเรื้อรังทำให้ monocyte สูง** — เชื้อที่อยู่ในเซลล์และก่อ granuloma (TB syphilis) หรือติดเชื้อนาน (SBE) ต้องใช้ **macrophage** จำนวนมาก ร่างกายจึงสร้าง monocyte ซึ่งเป็นตัวตั้งต้นของ macrophage เพิ่ม
- **Monocyte ขึ้นหลังยาเคมี** — เป็นเซลล์กลุ่มแรกที่กลับมาเมื่อไขกระดูกฟื้น จึงเป็น **สัญญาณดีว่า neutrophil กำลังจะตามมา**

### Lymphocytosis > 3,500/µL (สไลด์)
| | สาเหตุ |
|---|---|
| **Infection** | **Mononucleosis syndrome** (EBV, CMV, VZV, HSV type 2 6 8, **HIV**, rubella, adenovirus, hepatitis virus, **dengue**, toxoplasmosis) · **pertussis**, brucellosis, cat-scratch disease, TB, leprosy, syphilis, rickettsiosis, malaria, leishmaniasis, babesiosis |
| **Drug reaction** | เช่น DRESS |
| **Miscellaneous** | หลังตัดม้าม · post CMT/BMT · malignancy · **thymoma** |
| **Lymphoid neoplasms** | CLL, ALL, PLL, lymphoma ที่ออกมาในเลือด, hairy cell leukemia |

### สามขั้นในสไลด์ — Approach to lymphocytosis
[[fig:lymphflow]]
1. **หาสาเหตุ reactive** — ติดเชื้อ ยา
2. **Morphology (blood smear)** — **pleomorphic vs monomorphic**
3. **Immunophenotype (flow cytometry)** ✍️ ✓ — ยืนยัน clone และบอกชนิด · ✍️ **"CLL > 5000"** = เกณฑ์ **iwCLL 2018: monoclonal B lymphocyte ≥ 5,000/µL นานอย่างน้อย 3 เดือน** · CD5+ CD19+ CD23+ · ถ้าน้อยกว่านี้และไม่มีต่อมโต = monoclonal B-cell lymphocytosis (MBL) *(รายละเอียด iwCLL ไม่ได้อยู่ในสไลด์)*

### หน้าตาเซลล์ใน smear (สไลด์ — ภาพ)
| โรค | ลักษณะเซลล์ | ทำไมหน้าตาเป็นแบบนั้น |
|---|---|---|
| **Infectious mononucleosis** ✓ | atypical lymphocyte **ตัวใหญ่ ไซโตพลาสซึมกว้างสีฟ้า ขอบโอบรอบเม็ดเลือดแดง** | ส่วนใหญ่คือ **CD8 T cell ที่ถูกกระตุ้น** มาจัดการ B cell ที่ติด EBV — เซลล์ที่กำลังทำงานจึงใหญ่และหลากหลาย |
| Pertussis | lymphocyte **เล็ก** นิวเคลียสหยัก | **pertussis toxin กันไม่ให้ lymphocyte ออกจากเลือดเข้าต่อม** → ค้างในเลือด (ไม่ได้สร้างเพิ่ม) |
| Dengue | ✍️ **plasmacytoid lymphocyte** | B cell เร่งเปลี่ยนเป็นเซลล์สร้าง antibody |
| **CLL** | lymphocyte **ตัวเล็ก โตเต็มที่ เหมือนกันหมด** (✍️) + **smudge cell** | เซลล์ CLL **เปราะ** (โครงสร้าง cytoskeleton น้อย) แตกตอนป้ายสไลด์ |
| **ALL** ✓ | **lymphoblast** โครมาตินละเอียด มี nucleolus | blast — ไม่เจริญต่อ |
| PLL ✓ | **prolymphocyte** nucleolus เด่นชัด | |
| Mantle cell · follicular · marginal zone | lymphocyte เล็ก **นิวเคลียสหยัก (cleaved)** | lymphoma ที่ออกมาในเลือด |
| **Burkitt** ✓ | เซลล์ขนาดกลาง **ไซโตพลาสซึมมีช่องว่าง (vacuole)** | หยดไขมันในเซลล์ที่แบ่งตัวเร็วมาก |
| Hairy cell leukemia | ขอบเซลล์เป็น **ขนฝอยรอบตัว** (✍️ "ไข่ดาว" — fried-egg ในชิ้นเนื้อไขกระดูก) | |
| Splenic lymphoma with villous lymphocytes | ขนสั้น **ที่ขั้วเดียว** | |

#### ทำไมถึงมีอาการนี้ — infectious mononucleosis
| อาการ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ต่อมน้ำเหลืองคอด้านหลังโต ม้ามโต** | T cell แบ่งตัวจำนวนมากใน **ต่อมและม้าม** เพื่อกำจัด B cell ที่ติด EBV | ม้ามโตแบบนี้ **แตกง่าย** → งดกีฬาปะทะหลายสัปดาห์ |
| **เจ็บคอ ทอนซิลบวมมีฝ้า** | EBV ติดเยื่อบุและ B cell ใน **Waldeyer's ring** | คล้าย strep throat แต่มี atypical lymphocyte |
| **ผื่นหลังได้ amoxicillin/ampicillin** | ปฏิกิริยาภูมิคุ้มกันต่อยาในช่วงที่ภูมิถูกกระตุ้นอย่างมาก | ไม่ได้แปลว่าแพ้ยาถาวร |
| ตับอักเสบเล็กน้อย | lymphocyte ไปแทรกในตับ | |
""",
    ["Monocytosis เรื้อรัง: TB syphilis SBE · หรือ CMML/AML M4–5",
     "Monocyte ขึ้นหลังยาเคมี = ไขกระดูกกำลังฟื้น",
     "สามขั้น: reactive cause → smear pleomorphic/monomorphic → flow cytometry",
     "CLL: ≥ 5,000 monoclonal B cell · smudge cell · หน้าเหมือนกันหมด",
     "Atypical lymphocyte ใน IM = CD8 T cell ที่ถูกกระตุ้น"],
    [mcq(N(8), "A 72-year-old asymptomatic man has WBC 24,000/µL with 82% lymphocytes. The smear shows uniform small mature lymphocytes and numerous smudge cells. There is no lymphadenopathy or splenomegaly and the haemoglobin and platelet count are normal. What is the most appropriate next investigation?",
         ["Bone marrow aspiration and biopsy", "Excisional lymph node biopsy", "Peripheral blood flow cytometry", "EBV serology and monospot test", "CT scan of chest, abdomen and pelvis"], 2,
         "Absolute lymphocyte = 24,000 × 0.82 ≈ **19,700/µL** · smear **monomorphic + smudge cell** → สงสัย **CLL**\n\n"
         "ขั้นต่อไปตามสไลด์คือ **immunophenotype ด้วย flow cytometry จากเลือด** — ยืนยัน clone (light chain ชนิดเดียว) และ CD5+ CD19+ CD23+ (iwCLL 2018)\n\n"
         "- เจาะไขกระดูกและ CT **ไม่จำเป็นในการวินิจฉัย** CLL ระยะต้น\n- ไม่มีต่อมโต จึงไม่ต้องตัดต่อม\n- EBV ทำให้ lymphocyte หลากหลาย (pleomorphic) ไม่ใช่ smudge cell",
         "สงสัย CLL → flow cytometry จากเลือดก่อน", "Approach to lymphocytosis", R("Approach to lymphocytosis; Lymphoid neoplasms"), LYM),
     mcq(N(9), "A 19-year-old student has fever, exudative pharyngitis, tender posterior cervical lymphadenopathy and splenomegaly. Her smear shows many large lymphocytes with abundant blue cytoplasm that indents around adjacent red cells, varying in size and shape. What are these cells mainly?",
         ["Malignant monoclonal B cells", "EBV-infected B cells", "Reactive cytotoxic CD8+ T cells", "Circulating plasma cells", "Lymphoblasts"], 2,
         "นี่คือ **infectious mononucleosis** — atypical (reactive) lymphocyte ส่วนใหญ่คือ **CD8+ T cell ที่ถูกกระตุ้น** มาจัดการกับ B cell ที่ติด EBV · เป็นเซลล์ปกติหลายตัวที่ถูกกระตุ้นต่างระยะ จึง **หลากหลาย (pleomorphic)**\n\n"
         "- B cell ที่ติด EBV มีจำนวนน้อยในเลือด\n- clone มะเร็งจะ **เหมือนกันหมด (monomorphic)**\n- lymphoblast มีโครมาตินละเอียดและ nucleolus · ไม่มีไซโตพลาสซึมกว้าง",
         "Pleomorphic = reactive · IM atypical lymphocyte = CD8 T cell", "Infectious mononucleosis", R("Infectious mononucleosis"), LYM + ["2.1.57"]),
    ], LYM, SRC + " · Williams Hematology 8th · iwCLL 2018", F4)

# ───────────────────────────── 5
EGR = [(196, 108), (207, 104), (219, 106), (229, 113), (233, 125), (229, 136), (216, 143), (203, 143), (191, 136), (187, 122), (210, 116), (210, 133)]
F5 = {"eos": fig("Eosinophil มาจากสองทาง — แล้วทำลายอวัยวะได้อย่างไร",
 "**Reactive** (พบบ่อย): พยาธิ ภูมิแพ้ ยา กระตุ้น **Th2 cell ให้หลั่ง IL-5** ซึ่งเป็นปัจจัยหลักที่สั่งไขกระดูกสร้าง eosinophil · **Clonal**: ยีนผิดปกติในเซลล์ต้นกำเนิด (เช่น FIP1L1::PDGFRA) ทำให้สร้างเองโดยไม่ต้องรอ IL-5 (✍️ \"BM\") · "
 "eosinophil เข้าเนื้อเยื่อแล้ว **ปล่อยโปรตีนใน granule (MBP, ECP)** ที่ออกแบบมาเจาะผิวพยาธิ แต่ถ้ามีมากและนานจะทำลายอวัยวะตัวเอง — **หัวใจ** (endocardium อักเสบ ลิ่มเลือด พังผืด) ปอด ผิวหนัง เส้นประสาท · "
 "**cortisol กด eosinophil** จึงลดลงเกือบหมดเวลาเครียด/ได้ steroid · แถบล่างคือระดับความรุนแรงตามสไลด์",
 svg(420, 322, "กลไก eosinophilia แบบ reactive ผ่าน IL-5 และแบบ clonal การทำลายอวัยวะ และระดับ absolute eosinophil count",
     box(14, 12, 186, 64, "ms", "Reactive\nTh2 cell สร้าง IL-5\nพยาธิ · ภูมิแพ้ · ยา", fs=12),
     box(220, 12, 186, 64, "bad", "Clonal\nยีนผิดปกติในไขกระดูก\n(เช่น PDGFRA)", fs=12),
     ar(107, 76, 185, 108), ar(313, 76, 236, 107),
     circ(210, 124, 25, "ms"), ell(200, 124, 8, 10, "waf"), ell(221, 124, 8, 10, "waf"),
     *[circ(x, y, 1.9, "msf") for x, y in EGR],
     t(242, 122, "Eosinophil", "sm b"), t(242, 138, "> 500/µL", "xs i2"),
     box(14, 104, 140, 40, "ok", "Cortisol / steroid\nกด eosinophil", fs=11.5), tbar(154, 124, 181, 124),
     fan(210, 149, [61, 159, 257, 355], 176, 185),
     t(218, 166, "เข้าเนื้อเยื่อ ปล่อย MBP · ECP", "xs i2"),
     box(14, 186, 94, 42, "bad", "หัวใจ\nพังผืด ลิ่มเลือด", fs=11), box(112, 186, 94, 42, "bad", "ปอด\nหอบ ฝ้าในปอด", fs=11),
     box(210, 186, 94, 42, "bad", "ผิวหนัง\nคัน ผื่น", fs=11), box(308, 186, 94, 42, "bad", "เส้นประสาท\nชา อ่อนแรง", fs=11),
     t(14, 252, "Absolute eosinophil count (/µL) — สไลด์", "xs b i2"),
     rect(40, 260, 120, 16, "ok", 0), rect(160, 260, 130, 16, "ms", 0), rect(290, 260, 116, 16, "bad", 0),
     t(100, 272, "mild", "xs mid"), t(225, 272, "moderate", "xs mid"), t(348, 272, "severe", "xs mid"),
     t(40, 290, "500", "xs mid"), t(160, 290, "1,500", "xs mid"), t(290, 290, "5,000", "xs mid"),
     t(14, 312, "Hypereosinophilia > 1,500 · HES = > 1,500 + อวัยวะเสียหายจาก eosinophil", "xs b")))}

EOS = ["3.1.2", "B1.4.11", "2.3.1(12)", "B1.5.5(1)"]
sec("hon-wbc-05", "Eosinophilia — พยาธิ ภูมิแพ้ ยา หรือ clone",
    "AEC mild 500–1,500 moderate 1,500–5,000 severe > 5,000 · hypereosinophilia > 1,500 · HES = มีอวัยวะเสียหาย · reactive (infection drug allergy hypoadrenalism) vs clonal · strongyloides ก่อนให้ steroid", 9,
"""### นิยาม (สไลด์ — Gotlib 2011, Klion 2015)
| ระดับ | Absolute eosinophil count (AEC) |
|---|---|
| **Mild** | **500–1,500 /µL** (✍️ "เจอบ่อย") |
| **Moderate** | **1,500–5,000 /µL** |
| **Severe** | **> 5,000 /µL** |
- **Hypereosinophilia** = AEC **> 1,500 /µL** (✍️ "EOD")
- **Hypereosinophilic syndrome (HES)** = hypereosinophilia **+ หลักฐานว่าอวัยวะเสียหายจาก eosinophil** · เกณฑ์ปัจจุบันต้องพบ > 1,500 **สองครั้งห่างกันอย่างน้อย 1 เดือน** *(ไม่ได้มาจากสไลด์)*
[[fig:eos]]
### สาเหตุ (สไลด์)
| | สาเหตุ |
|---|---|
| **Reactive — infection** | **พยาธิที่ไชผ่านเนื้อเยื่อ** เป็นหลัก — ในไทยที่สำคัญ: **Strongyloides**, hookworm, **Gnathostoma** (ก้อนบวมย้ายที่), **Angiostrongylus** (eosinophilic meningitis), พยาธิใบไม้ *(ตัวอย่างพยาธิไม่ได้อยู่ในสไลด์)* |
| **Reactive — drug** (✍️ วงไว้) | ยาเกือบทุกกลุ่ม — DRESS เป็นรูปแบบรุนแรง (ไข้ ผื่น ตับอักเสบ eosinophil สูง) |
| **Allergic disease** (mild) | ✍️ **asthma** · allergic rhinitis · atopic dermatitis |
| **Miscellaneous** | connective tissue disease · **vasculitis** (EGPA) · sarcoidosis · cancer (เช่น Hodgkin) · **ABPA** · eosinophilic pneumonia · eosinophilic gastroenteritis · **hypoadrenalism** |
| **Clonal** (✍️ "BM →") | **clonal eosinophilia** (myeloid/lymphoid neoplasm with eosinophilia เช่น PDGFRA PDGFRB FGFR1) · **hypereosinophilic syndrome** |

#### ทำไมถึงมีอาการนี้ — eosinophil
| อาการ/ลักษณะ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| พยาธิที่ไชผ่านเนื้อเยื่อทำให้ eos **สูงมาก** แต่พยาธิที่อยู่แค่ในโพรงลำไส้ **ไม่ค่อยสูง** | eosinophil ถูกเรียกเมื่อพยาธิ **สัมผัสเนื้อเยื่อ** (Th2 → IL-5) · พยาธิใหญ่เกินกว่าจะกลืนกิน eosinophil จึง **ปล่อย granule ทำลายผิวพยาธิ** แทน | eos สูง + ถ่ายเหลว/ผื่นคันที่ย้ายที่ = นึกถึง strongyloides |
| ภูมิแพ้ หอบหืด → eos **สูงเล็กน้อย** | Th2 → IL-5 แบบเบา ๆ | **ถ้า > 1,500 อย่าโทษภูมิแพ้** — หา ABPA EGPA พยาธิ ยา |
| **ป่วยหนักหรือช็อก แต่ eos ไม่ต่ำ** | ปกติ **cortisol จากความเครียดกด eosinophil จนเกือบเป็นศูนย์** — ถ้าไม่ลดแปลว่า cortisol ไม่พอ | นึกถึง **adrenal insufficiency** (สไลด์: hypoadrenalism) |
| HES: **หัวใจล้มเหลว ลิ่มเลือดในหัวใจ** | MBP ECP ทำลาย endocardium → ลิ่มเลือดเกาะ → พังผืด (endomyocardial fibrosis) | ตรวจ troponin และ echocardiogram ทุกรายที่ > 1,500 |
| HES: หอบ ไอ · ผื่น คัน · ชา | granule proteins + ลิ่มเลือดในหลอดเลือดเล็กของปอด ผิว เส้นประสาท | อวัยวะเสียหาย = ต้องรักษาแม้ยังหาสาเหตุไม่ได้ |
| หลังได้ steroid eos หายเกือบหมดในไม่กี่ชั่วโมง | cortisol ทำให้ eosinophil ไปอยู่ในเนื้อเยื่อและตาย | eos ที่ต่ำหลังให้ steroid ไม่ได้แปลว่าโรคหาย |

### ก่อนให้ steroid ในคนไทยที่ eos สูง *(ไม่ได้มาจากสไลด์)*
- **คัดกรองหรือให้ยา ivermectin ครอบคลุม Strongyloides ก่อน** — steroid กดภูมิทำให้ตัวอ่อนเพิ่มจำนวนในร่างกายเองและไชทะลุผนังลำไส้ทั่วตัว (**hyperinfection syndrome**) พาแบคทีเรียลำไส้ไปด้วย → gram-negative sepsis เยื่อหุ้มสมองอักเสบ ตายสูง
- ประเมินอวัยวะ: CBC smear · troponin · echocardiogram · CXR · LFT · UA · stool exam หลายครั้ง และ serology พยาธิ
- หาสาเหตุไม่ได้และ > 1,500 นาน → **เจาะไขกระดูก + ตรวจยีน (PDGFRA/PDGFRB/FGFR1, JAK2) + flow cytometry หา T-cell clone** · กลุ่ม **PDGFRA ตอบสนองดีมากต่อ imatinib**
""",
    ["Mild 500–1,500 · moderate 1,500–5,000 · severe > 5,000",
     "Hypereosinophilia > 1,500 · HES = + อวัยวะเสียหาย",
     "ป่วยหนักแต่ eos ไม่ต่ำ = นึกถึง adrenal insufficiency",
     "ก่อนให้ steroid คนไทยที่ eos สูง — คิดถึง Strongyloides",
     "HES ทำลายหัวใจ — ตรวจ troponin และ echo"],
    [mcq(N(10), "A 58-year-old rice farmer from north-eastern Thailand has eosinophils 2,100/µL, intermittent diarrhoea and a migrating serpiginous itchy rash on the buttocks. He is about to start high-dose prednisolone for newly diagnosed immune thrombocytopenia. What should be done first?",
         ["Start prednisolone immediately and recheck eosinophils in 1 month", "Give ivermectin (or test for Strongyloides) before starting prednisolone",
          "Perform bone marrow examination for PDGFRA rearrangement", "Start imatinib", "Give antihistamines only"], 1,
         "ผื่นคันที่ย้ายตำแหน่งรอบก้น (larva currens) + ถ่ายเหลว + eosinophil สูง ในชาวนาไทย = **Strongyloides stercoralis**\n\n"
         "ถ้าให้ steroid ก่อน ตัวอ่อนจะเพิ่มจำนวนในร่างกายเองและไชทะลุลำไส้ทั่วตัว (**hyperinfection/disseminated strongyloidiasis**) พาแบคทีเรียลำไส้ไปด้วย → sepsis เยื่อหุ้มสมองอักเสบ ตายสูง → **ให้ ivermectin ก่อน** (หรือตรวจ serology/stool ก่อน)\n\n"
         "- เจาะไขกระดูกหา clone ทำเมื่อหาสาเหตุ reactive ไม่ได้\n- imatinib สำหรับ PDGFRA-positive clonal eosinophilia เท่านั้น\n\n*(ตัวอย่างพยาธิในไทยไม่ได้อยู่ในสไลด์)*",
         "Eos สูงในคนไทยก่อนให้ steroid = นึกถึง Strongyloides", "Eosinophilia — infection", R("Cause of eosinophilia"), EOS + ["B8.2.2(5)"]),
     mcq(N(11), "A 45-year-old woman in the ICU has septic shock that responds poorly to fluids and norepinephrine. Labs: Na 128, K 5.6 mmol/L, glucose 62 mg/dL, WBC 14,000/µL with eosinophils 9% (1,260/µL). Which explanation for the eosinophil count is most useful?",
         ["Eosinophilia is expected in bacterial sepsis", "It suggests a drug reaction to the antibiotics as the cause of shock",
          "Cortisol normally suppresses eosinophils during severe stress; their persistence suggests adrenal insufficiency", "It indicates a parasitic co-infection only", "It indicates clonal eosinophilia"], 2,
         "ในภาวะเครียดรุนแรง **cortisol สูงจะกด eosinophil จนเกือบเป็นศูนย์** — ผู้ป่วยช็อกที่ยังมี eosinophil > 500 ร่วมกับ **Na ต่ำ K สูง น้ำตาลต่ำ ช็อกไม่ตอบสนองต่อยา** ชี้ไปที่ **adrenal insufficiency** (สไลด์: hypoadrenalism เป็นสาเหตุของ eosinophilia) → ตรวจ cortisol และให้ hydrocortisone\n\n"
         "- การติดเชื้อแบคทีเรียมักทำให้ eosinophil **ต่ำ**\n- drug reaction และพยาธิเป็นไปได้แต่ไม่อธิบายเกลือแร่และช็อก",
         "ช็อก + eos ไม่ต่ำ + Na ต่ำ K สูง = adrenal insufficiency", "Eosinophilia — hypoadrenalism", R("Cause of eosinophilia"), EOS[:2] + ["2.3.4-3(4)", "2.2.48"]),
    ], EOS, SRC + " · Gotlib 2011 · Klion AD (Blood 2015)", F5)

# ───────────────────────────── 6
NPROWS = [(1, "สร้างลดลง (production ↓)", "ไขกระดูกล้ม · ยาเคมี · ขาด B12/folate/ทองแดง · MDS · ไวรัส"),
          (2, "ถูกทำลายหรือใช้หมด (destruction ↑)", "ภูมิต้านตนเอง SLE Felty LGL · ยาบางชนิด · sepsis"),
          (3, "ไปกองอยู่ที่อื่น (margination/sequestration)", "ม้ามโต (hypersplenism) — ร่างกายมีพอ แต่ CBC ต่ำ")]
F6 = {"neutropenia": fig("Neutropenia สามกลไก — วางบนแผนภาพคลังเดียวกัน",
 "ใช้แผนภาพคลังเดียวกับหัวข้อ 2 แต่กลับทิศ: **(1) สร้างลดลง** — คลังในไขกระดูกว่าง (เส้นประ) เช่น ไขกระดูกล้ม ยาเคมี ขาดสารอาหาร MDS · "
 "**(2) ถูกทำลายหรือใช้หมด** — antibody ต่อ neutrophil (SLE Felty LGL ยา) หรือถูกดึงไปใช้ในเนื้อเยื่อเร็วกว่าที่สร้างทัน (sepsis ไข้เลือดออก) · "
 "**(3) ไปกองอยู่ที่อื่น** — ม้ามโตกักเซลล์ไว้ (hypersplenism) หรือเกาะผนังหลอดเลือดมากขึ้น · "
 "สองกลไกหลังไขกระดูกยังปกติหรือสร้างมากขึ้น จึงมักไม่ติดเชื้อรุนแรงเท่ากลไกแรก (ดัดแปลงจากสไลด์ Classification of neutropenia — Boxer, ASH 2012)",
 svg(420, 372, "แผนภาพคลัง neutrophil แสดงกลไก neutropenia สามแบบ สร้างลดลง ถูกทำลาย และถูกกักในม้าม",
     t(69, 24, "ไขกระดูก", "sm b mid tac"), t(230, 24, "ในเลือด", "sm b mid twa"), t(371, 24, "เนื้อเยื่อ", "sm b mid i2"),
     box(14, 34, 110, 36, "sk da", "Mitotic pool", fs=12), ar(69, 70, 69, 84, "lmu", "ah-mu"),
     box(14, 84, 110, 36, "sk da", "Maturation", fs=12), ar(69, 120, 69, 134, "lmu", "ah-mu"),
     box(14, 134, 110, 62, "sk da", "Storage pool\n(ว่าง)", fs=12),
     box(170, 56, 120, 44, "sk", "Marginal pool\nเกาะผนังหลอดเลือด", fs=11.5),
     path("M230 104 L230 126", "ln", "ah", "ah"),
     box(170, 130, 120, 44, "wa", "Circulating pool\nCBC ต่ำ", fs=11.5),
     ar(124, 168, 168, 158, "lmu", "ah-mu"),
     ar(290, 150, 334, 150, "lbad w2", "ah-bad"), box(336, 124, 70, 52, "bx", "เนื้อเยื่อ", fs=12),
     path("M190 194 L190 183 M190 183 L184 176 M190 183 L196 176", "lbad w2"),
     path("M214 194 L214 183 M214 183 L208 176 M214 183 L220 176", "lbad w2"),
     t(226, 192, "antibody", "xs tbad"),
     ar(280, 174, 320, 214, "lbad w2", "ah-bad"),
     ell(360, 228, 44, 22, "bad"), t(360, 232, "ม้ามโต", "sm b mid tbad"),
     badge(140, 52, 1), badge(312, 136, 2), badge(170, 196, 2), badge(290, 210, 3),
     *[badge(24, 268 + i * 36, n) + t(40, 272 + i * 36, a, "sm b") + t(40, 287 + i * 36, b, "xs i2")
       for i, (n, a, b) in enumerate(NPROWS)]))}

NP = ["2.3.3(2)", "B2.2.2(7)", "2.3.3-3(5)"]
sec("hon-wbc-06", "Leukopenia และ neutropenia — กลไก สาเหตุ และ approach",
    "Neutropenia < 1,500 · mild moderate severe (< 500 agranulocytosis) · ยืนยัน ≥ 3 ครั้ง · acute vs chronic 3 เดือน · production ↓ destruction ↑ sequestration · ยาที่ทำให้ agranulocytosis · BM aplasia vs maturation arrest · MDS", 13,
"""### นิยาม (สไลด์)
- **Leukopenia < 4,000/µL** · **Neutropenia < 1,500** · **Lymphopenia < 1,000** · monocytopenia eosinopenia basopenia **ไม่มีความสำคัญทางคลินิก**
- **ยืนยันอย่างน้อย 3 ครั้งในหลายสัปดาห์** — ค่าแกว่งตามธรรมชาติ (physiological variation) · บางเชื้อชาติมี ANC ต่ำกว่าเกณฑ์โดยไม่ติดเชื้อง่าย (Duffy-null associated neutrophil count) *(ไม่ได้มาจากสไลด์)*

| ความรุนแรง (สไลด์) | ANC (/µL) | ความเสี่ยง |
|---|---|---|
| Mild | 1,000–1,500 | ต่ำ |
| Moderate | 500–1,000 | ปานกลาง |
| **Severe = agranulocytosis** | **< 500** | **ติดเชื้อหนองรุนแรงและเสี่ยงชีวิต** |
- **Acute neutropenia**: ไม่กี่วัน – **3 เดือน** · **Chronic**: **> 3 เดือน**

### สามกลไก (สไลด์)
[[fig:neutropenia]]
**Impaired production · Increased destruction · Margination and sequestration**

### สาเหตุ (สไลด์)
| กลุ่ม | ตัวอย่าง |
|---|---|
| **Infection** | ดูตารางถัดไป |
| **Drug** | ดูตารางยา |
| **Immune** | **SLE, RA, Sjögren, Felty syndrome, LGL leukemia** |
| **Bone marrow failure** | aplastic anemia · MDS · มะเร็งแทรกไขกระดูก · ยาเคมี/รังสี |
| **Nutritional deficiency** | **B12 · folate · ทองแดง** (สไลด์ให้ตรวจ copper ceruloplasmin B12 folate) |
| **Miscellaneous** | congenital neutropenia · margination · **hypersplenism** · idiopathic |

| Infection-induced (สไลด์) | เชื้อ | กลไก |
|---|---|---|
| **ติดเซลล์สร้าง granulocyte** | EBV, CMV, **HIV**, hepatitis virus, rubella, influenza | สร้างลดลง |
| **เกาะ endothelium หรือถูกใช้มาก** | babesiosis, rickettsiosis, **dengue**, measles, **septicemia** | ใช้หมด/ไปกองที่ผนัง |
| **ม้ามโต** | brucellosis, salmonellosis, **tuberculosis, malaria**, kala-azar | ถูกกักในม้าม |

| ยาที่ทำให้ neutropenia — definite causality (สไลด์ · Andersohn 2007) | ตัวอย่าง |
|---|---|
| Analgesics & NSAIDs | aminopyrine, diclofenac, diflunisal, **dipyrone (metamizole)**, ibuprofen |
| Antiarrhythmics | disopyramide, **procainamide**, quinidine |
| Anti-infectives | ampicillin, carbenicillin, cefotaxime, cefuroxime, flucytosine, fusidic acid, imipenem, nafcillin, oxacillin, penicillin G, quinine, ticarcillin |
| Anticonvulsants · antineoplastic · antirheumatics | phenytoin · amygdalin · infliximab, levamisole |
| **Antithyroid** | **propylthiouracil** |
| CVS · GI | clopidogrel, methyldopa, ramipril, spironolactone · cimetidine, metoclopramide |
| **Psychotropic** | chlorpromazine, **clozapine**, fluoxetine |
| Others | calcium dobesilate, mebhydrolin |
- กลไกของยา: **ภูมิคุ้มกันทำลาย** (ยาจับผิว neutrophil แล้วเกิด antibody — เกิดเร็ว ไม่ขึ้นกับขนาดยา เช่น ยาต้านไทรอยด์) หรือ **พิษตรงต่อเซลล์ตั้งต้น** (ขึ้นกับขนาดยาและระยะเวลา เช่น clozapine chlorpromazine) *(ไม่ได้มาจากสไลด์)*
- **ยาต้านไทรอยด์ (PTU และ methimazole)** — agranulocytosis มักเกิดใน 3 เดือนแรก · สอนผู้ป่วย **ไข้ เจ็บคอ แผลในปาก = หยุดยาและมาตรวจ CBC ทันที** · ห้ามเปลี่ยนไปใช้ยาต้านไทรอยด์อีกตัว (ข้ามกันได้)

### Approach to neutropenia (สไลด์)
| ประวัติ | ตรวจร่างกาย | ส่งตรวจ |
|---|---|---|
| onset · การติดเชื้อ · **ยา** · โรคภูมิต้านตนเอง · ภาวะขาดสารอาหาร · ประวัติครอบครัว | **ต่อมน้ำเหลือง** · **ตับและม้าม** · ผิวหนัง ช่องปาก ผม เล็บ กระดูก | **CBC + blood smear** · anti-HIV serology culture · ANA RF antineutrophil Ab · copper ceruloplasmin B12 folate · **bone marrow study** |

### ไขกระดูกบอกกลไก (สไลด์ — ภาพ)
- **Granulocytic aplasia/hypoplasia** — ไม่มีเซลล์ตั้งต้นสาย granulocyte = **สร้างไม่ได้** (พิษจากยาโดยตรง)
- **Maturation arrest** — มีตัวอ่อน (promyelocyte/myelocyte) แต่ **ไม่มีตัวแก่** = ถูกทำลายที่ระยะหลัง (ภูมิคุ้มกัน) หรือกำลังฟื้นตัว
- **Myelodysplastic syndrome** — dysplasia ทั้งสามสาย: pseudo-Pelger, granule น้อย, ring sideroblast, micromegakaryocyte · พบในผู้สูงอายุ มักมี MCV สูงและ cytopenia หลายสาย · ✍️ **กลายเป็น AML ได้**

#### ทำไมถึงมีอาการนี้ — neutropenia
| อาการ | กลไก | ใช้อย่างไร |
|---|---|---|
| **ไข้อาจเป็นอาการเดียว** — ไม่มีหนอง ฝ้าในปอดน้อย ปัสสาวะไม่มี WBC | หนองและ infiltrate **สร้างจาก neutrophil** — ไม่มี neutrophil จึงไม่มีสัญญาณการอักเสบ แต่ macrophage ยังหลั่ง cytokine ทำให้ไข้ได้ | ไข้ + ANC < 500 = **febrile neutropenia** → ยาต้านเชื้อครอบคลุม Pseudomonas ภายใน 1 ชั่วโมง (ดูคาบ General oncology) |
| **แผลในปาก เจ็บคอ เหงือกอักเสบ ฝีรอบทวาร** | ปาก คอ และทวารหนักมีเชื้อประจำถิ่นมาก — neutrophil เป็นด่านแรกที่คุมเชื้อเหล่านี้ | ผู้ที่กินยาต้านไทรอยด์ + เจ็บคอ ไข้ → CBC ทันที |
| ติดเชื้อราเมื่อ neutropenia นานเกิน 1 สัปดาห์ | neutrophil เป็นตัวหลักที่กำจัด Candida และ Aspergillus | ไข้ไม่ลงหลังยาต้านแบคทีเรีย → คิดถึงเชื้อรา |
| ม้ามโต + ต่ำหลายสาย แต่ไขกระดูกปกติ | **ม้ามกักเซลล์ (hypersplenism)** — ร่างกายสร้างพอ | ติดเชื้อไม่รุนแรงเท่าไขกระดูกล้ม |
| **Felty syndrome**: RA + ม้ามโต + neutropenia | antibody + การกักในม้าม | ตรวจ RF/anti-CCP |
""",
    ["Neutropenia < 1,500 · agranulocytosis < 500 = เสี่ยงติดเชื้อรุนแรง",
     "ยืนยัน ≥ 3 ครั้ง · acute < 3 เดือน chronic > 3 เดือน",
     "สามกลไก: สร้างลด · ทำลายเพิ่ม · ไปกองที่ผนัง/ม้าม",
     "ยาต้านไทรอยด์ + ไข้ เจ็บคอ = หยุดยา ตรวจ CBC ทันที",
     "ไม่มี neutrophil = ไม่มีหนอง — ไข้อาจเป็นอาการเดียว"],
    [mcq(N(12), "A 28-year-old woman with Graves' disease started propylthiouracil 6 weeks ago. She presents with fever 39.2 °C and a painful sore throat. CBC: WBC 1,100/µL, ANC 150/µL, haemoglobin and platelets normal. What is the most appropriate management?",
         ["Continue propylthiouracil and give oral amoxicillin", "Switch to methimazole and recheck CBC in 1 week",
          "Stop propylthiouracil permanently, take cultures and start empirical broad-spectrum IV antibiotics", "Start prednisolone for immune neutropenia", "Observe as this is physiological variation"], 2,
         "นี่คือ **drug-induced agranulocytosis** (ANC < 500) จาก **propylthiouracil** (สไลด์: antithyroid drugs — definite causality) ร่วมกับไข้ = **febrile neutropenia**\n\n"
         "- **หยุดยาถาวร** · เพาะเชื้อ · **ยาต้านเชื้อทางหลอดเลือดครอบคลุม Pseudomonas ทันที**\n"
         "- **ห้ามเปลี่ยนเป็น methimazole** — เกิดปฏิกิริยาข้ามกันได้ · ควบคุมไทรอยด์ด้วยวิธีอื่น (เช่น ไอโอดีนรังสีหรือผ่าตัดเมื่อพร้อม)\n"
         "- ยากินเฉย ๆ ไม่พอใน ANC 150 ที่มีไข้สูง · ไม่ใช่ physiological variation",
         "ยาต้านไทรอยด์ + ไข้ เจ็บคอ + ANC < 500 = หยุดยา + ยาต้านเชื้อ IV", "Drug-induced neutropenia", R("Drug-induced neutropenia"), NP + ["2.3.19(2)"]),
     mcq(N(13), "A 55-year-old man with alcoholic cirrhosis has a spleen palpable 8 cm below the costal margin. WBC 2,600/µL (ANC 1,300/µL), platelets 58,000/µL, haemoglobin 11 g/dL. Bone marrow is normocellular with normal maturation. Which mechanism best explains the neutropenia?",
         ["Impaired production from marrow failure", "Sequestration of neutrophils in an enlarged spleen", "Antineutrophil antibodies", "Copper deficiency", "Maturation arrest"], 1,
         "ไขกระดูก **ปกติและเจริญครบ** แต่ม้ามโตจาก portal hypertension → **hypersplenism**: ม้ามกักเม็ดเลือดขาวและเกล็ดเลือดไว้ (สไลด์: **margination and sequestration** · Misc: hypersplenism)\n\n"
         "- marrow failure และขาดทองแดงจะเห็นไขกระดูก hypocellular หรือ dysplasia\n- maturation arrest จะไม่มีตัวแก่ในไขกระดูก\n- antibody มักไม่ทำให้เกล็ดเลือดต่ำพร้อมกันแบบนี้ร่วมกับม้ามโต",
         "ม้ามโต + ต่ำหลายสาย + ไขกระดูกปกติ = sequestration", "Mechanism of neutropenia", R("Classification of neutropenia; Cause of neutropenia"), NP),
     mcq(N(14), "A patient receiving chemotherapy has ANC 80/µL and fever 38.6 °C. Chest examination is normal, chest radiograph shows only a subtle opacity, and urinalysis shows no pyuria despite a urine culture later growing E. coli. Why are localising signs so scant?",
         ["The fever is drug-related rather than infectious", "Neutrophils are required to form pus and inflammatory infiltrates, so classic signs are blunted",
          "Gram-negative bacteria do not cause inflammation", "Chemotherapy blocks the hypothalamic response to cytokines", "Lymphocytes replace neutrophils at infected sites"], 1,
         "หนอง ฝ้าในปอด และ WBC ในปัสสาวะ **ล้วนเกิดจาก neutrophil ที่ไปรวมตัวในจุดติดเชื้อ** — เมื่อ ANC < 500 สัญญาณเหล่านี้จึงหายไป แม้ติดเชื้อรุนแรง\n\n"
         "ไข้ยังเกิดได้เพราะ macrophage และเซลล์อื่นยังหลั่ง IL-1 IL-6 TNF ไปตั้ง set point ที่ hypothalamus → **ไข้อาจเป็นอาการเดียวของ febrile neutropenia** ต้องให้ยาต้านเชื้อทันทีไม่ต้องรอหาตำแหน่ง\n\n"
         "- เชื้อแกรมลบก่อการอักเสบได้ปกติ · lymphocyte ไม่ได้มาแทนที่เพื่อสร้างหนอง",
         "ไม่มี neutrophil = ไม่มีหนอง — อย่ารอหาตำแหน่งติดเชื้อ", "Neutropenia — clinical", R("Neutropenia"), NP + ["2.1.1"]),
    ], NP + ["2.3.3-3(1)"], SRC + " · Boxer (ASH 2012) · Dale 2003 · Andersohn (Ann Intern Med 2007)", F6)

# ───────────────────────────── 7
NMC = [(40, 50, 12), (152, 100, 13), (112, 52, 10), (180, 60, 9)]           # fat cells
ERY = [(96, 84), (105, 92), (98, 100), (132, 72), (140, 80), (118, 112), (170, 88), (178, 112), (60, 60)]
GRN = [(48, 82), (62, 110), (130, 100), (160, 44), (88, 40), (186, 92), (34, 108)]
BL = [(232 + c * 18, 40 + r * 18) for r in range(5) for c in range(10)]
F7 = {"marrowfail": fig("Acute leukemia — blast ยึดไขกระดูก แล้วเกิดอะไรตามมา",
 "ซ้าย: ไขกระดูกปกติมีหลายสาย (จุดแดงเล็ก = เซลล์ตั้งต้นเม็ดเลือดแดง · ชมพู = granulocyte · เหลืองใหญ่ = megakaryocyte · วงกลมว่าง = ไขมัน) · "
 "ขวา: **blast ชนิดเดียวแบ่งตัวเต็มโพรงไขกระดูก (≥ 20%)** — เซลล์ตั้งต้นปกติถูกเบียดและถูกกดการทำงาน จึง **ต่ำพร้อมกันสามสาย** และอาการสามกลุ่มสะท้อนอายุของเซลล์: "
 "**เกล็ดเลือดอยู่ได้ 7–10 วัน** จึงเลือดออกเร็ว · **neutrophil อยู่ในเลือดไม่กี่ชั่วโมง** จึงติดเชื้อเร็ว · **เม็ดเลือดแดงอยู่ 120 วัน** จึงซีดค่อยเป็นค่อยไป · "
 "blast ที่ล้นยังดันโพรงกระดูกและไปฝังตามอวัยวะ *(อาการทางคลินิกของ acute leukemia ไม่ได้อยู่ในสไลด์ — เติมจากตำรา)*",
 svg(420, 294, "ไขกระดูกปกติเทียบกับ acute leukemia ที่ blast ยึดเต็ม ทำให้เม็ดเลือดแดง neutrophil เกล็ดเลือดต่ำ ปวดกระดูก และการแทรกอวัยวะ",
     t(107, 18, "ไขกระดูกปกติ", "sm b mid tok"), rect(14, 26, 186, 100, "sk", 10),
     *[circ(x, y, r, "paf") + circ(x, y, r, "lru") for x, y, r in NMC],
     circ(72, 92, 13, "ms"), ell(67, 89, 5, 4, "msf"), ell(76, 93, 5, 4, "msf"), ell(69, 98, 4, 3, "msf"),
     *[circ(x, y, 4.5, "badf") for x, y in ERY],
     *[circ(x, y, 6.5, "ac") + circ(x, y, 2.6, "acf") for x, y in GRN],
     t(313, 18, "Acute leukemia — blast ≥ 20%", "sm b mid tbad"), rect(220, 26, 186, 100, "sk", 10),
     *[(circ(x, y, 4.5, "badf") if (x, y) == BL[13] else circ(x, y, 6.5, "ac") + circ(x, y, 2.6, "acf") if (x, y) == BL[37]
        else circ(x, y, 8.2, "bad") + circ(x, y, 6.2, "badf")) for x, y in BL],
     fan(313, 127, [77, 210, 343], 140, 149),
     box(14, 150, 126, 46, "ms", "RBC ↓\nซีด เหนื่อย ใจสั่น", fs=11.5),
     box(147, 150, 126, 46, "ms", "Neutrophil ↓\nไข้ ติดเชื้อ แผลในปาก", fs=11.5),
     box(280, 150, 126, 46, "ms", "Platelet ↓\nจุดเลือด เลือดกำเดา", fs=11.5),
     t(14, 222, "blast ที่ล้นยังทำให้เกิด", "sm b"),
     box(14, 230, 192, 56, "bad", "ล้นโพรงไขกระดูก\n→ แรงดันสูง ยืดเยื่อหุ้มกระดูก\n→ ปวดกระดูก sternum กดเจ็บ", fs=11),
     box(214, 230, 192, 56, "bad", "ออกไปฝังในอวัยวะ\n→ ตับม้ามโต ต่อมโต (ALL)\n→ เหงือกบวม ผิวหนัง (AML M4/5)", fs=11)))}

AL = ["B2.2.4-3(1)", "2.1.56", "2.1.58", "2.1.1"]
SRC7 = SRC + " (AML/ALL ในหัวข้อ hyperleukocytosis, TLS, smear) · อาการทางคลินิกเติมจาก Williams Hematology · WHO 5th 2022 · ELN 2022 — ไม่ได้มาจากสไลด์"
sec("hon-wbc-07", "Acute leukemia — ทำไมมาด้วยซีด ไข้ เลือดออก",
    "Blast ≥ 20% · marrow failure triad ตามอายุเซลล์ · ปวดกระดูก sternal tenderness · เหงือกบวม AML M4/5 · ต่อมโตและก้อนในช่องอกใน ALL/T-ALL · APL กับ DIC และ ATRA (เติมจากตำรา)", 11,
"""### ทำไมมีหัวข้อนี้
สไลด์พูดถึง AML และ ALL ในหลายจุด — **lymphoblast ใน smear**, **AML M4/M5 ในสาเหตุ monocytosis**, **MDS กลายเป็น AML** (✍️), **T-ALL ที่มาด้วยก้อนในช่องอกและ BM failure**, **hyperleukocytosis** และ **TLS** — แต่ไม่มีสไลด์ที่อธิบายอาการโดยตรง หัวข้อนี้จึงเติมกลไกของอาการ {ns}

### นิยามและภาพรวม
- **Acute leukemia** = blast **≥ 20%** ในไขกระดูกหรือเลือด (WHO 5th 2022) · บาง genetic abnormality วินิจฉัย AML ได้แม้ blast น้อยกว่านี้ เช่น **PML::RARA ของ APL**
- **AML** พบมากในผู้ใหญ่และผู้สูงอายุ (MDS ก่อนหน้า หลังยาเคมี/รังสี) · **ALL** พบมากในเด็ก และในผู้ใหญ่พบได้ทุกวัย
- WBC เป็นได้ทั้ง **ต่ำ ปกติ หรือสูงมาก** (ภาพ 1 หัวข้อ 3) — ตัวชี้คือ **blast** และ **cytopenia สายอื่น**
[[fig:marrowfail]]
#### ทำไมถึงมีอาการนี้ — acute leukemia
| อาการ/อาการแสดง | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ซีด เหนื่อย ใจสั่น** | blast เบียดสาย erythroid (มาจาก progenitor เดียวกับ myeloid) → reticulocyte ต่ำ · RBC อยู่ 120 วัน ซีดจึง **ค่อย ๆ มากขึ้น** | normocytic normochromic · retic ต่ำ |
| **ไข้ ติดเชื้อรุนแรง แผลในปาก** | neutrophil ปกติไม่ถูกสร้าง · **blast ไม่ทำหน้าที่แบบ neutrophil** ถึง WBC จะสูงมาก | "WBC 80,000 แต่ติดเชื้อง่าย" = ส่วนใหญ่เป็น blast |
| **จุดเลือด จ้ำเลือด เลือดกำเดา เลือดออกเหงือก** | เกล็ดเลือดต่ำ → เลือดออกแบบ **ผิวหนังและเยื่อบุ** (primary hemostasis) · เกล็ดเลือดอายุสั้น จึงลดเร็ว | จุดเลือดที่ขา ในปาก |
| **ปวดกระดูก กดเจ็บที่ sternum** | blast แบ่งตัวในโพรงไขกระดูกที่ขยายไม่ได้ → **แรงดันในโพรงสูง** และ **ยืดเยื่อหุ้มกระดูก (periosteum)** ที่มีปลายประสาท | เด็ก ALL มาด้วยปวดขา เดินกะเผลก |
| **เหงือกบวมหนา ผื่น/ตุ่มที่ผิวหนัง** (leukemia cutis) | **AML M4/M5 (monocytic)** — blast สาย monocyte ยังมีคุณสมบัติของ monocyte ที่ **ออกจากหลอดเลือดไปฝังในเนื้อเยื่อ** | สไลด์: AML M4/5 เป็นสาเหตุ monocytosis |
| **ต่อมโต ตับม้ามโต** | ALL — lymphoblast กลับไปอยู่ในเนื้อเยื่อ lymphoid | ALL > AML |
| **ก้อนในช่องอก** หอบ หน้าบวม | **T-ALL เกิดจาก T cell ตั้งต้นที่เจริญใน thymus** → ก้อนที่ anterior mediastinum (SVC syndrome) | สไลด์: T-ALL ชาย AYA + BM failure |
| ปวดศีรษะ เส้นประสาทสมองอ่อนแรง | blast เข้าน้ำไขสันหลัง (พบใน ALL) | ต้องเจาะหลังและให้ยาเข้าน้ำไขสันหลัง |
| **เลือดออกรุนแรงตั้งแต่แรก** fibrinogen ต่ำมาก | **APL**: granule ของ promyelocyte มี **tissue factor** (กระตุ้นการแข็งตัว → DIC) และผิวเซลล์มี **annexin II** เพิ่มการสร้าง plasmin (**hyperfibrinolysis**) → เลือดออกในสมองได้ | **ให้ ATRA ทันทีที่สงสัย** ไม่ต้องรอผลยีน · สไลด์: ห้าม leukapheresis ใน APL |
| หอบ สับสน stroke | leukostasis เมื่อ WBC สูงมาก (หัวข้อ 8) | |

### ตรวจเบื้องต้น {ns}
- CBC smear (blast · **Auer rod** = myeloid · **faggot cell** = APL) · PT aPTT **fibrinogen** D-dimer · K PO4 uric acid Ca Cr LDH (TLS)
- ไขกระดูก: morphology · **flow cytometry** (myeloid vs B vs T) · cytogenetics และ molecular (ELN 2022 แบ่งความเสี่ยง เช่น t(8;21), inv(16), NPM1 = ดี · TP53, complex karyotype = แย่)
- ภาวะเร่งด่วนพร้อมกัน: **febrile neutropenia · DIC/APL · leukostasis · TLS**
""".format(ns=NOTSLIDE),
    ["Acute leukemia = blast ≥ 20% · WBC ต่ำ ปกติ หรือสูงก็ได้",
     "ซีด ไข้ เลือดออก = ไขกระดูกถูกยึดทั้งสามสาย",
     "ปวดกระดูก sternum กดเจ็บ = โพรงไขกระดูกแรงดันสูงยืดเยื่อหุ้มกระดูก",
     "เหงือกบวม ผิวหนัง = AML monocytic (M4/M5)",
     "สงสัย APL (เลือดออก fibrinogen ต่ำ) → ATRA ทันที ห้าม leukapheresis"],
    [mcq(N(15), "A 42-year-old man has 3 weeks of fatigue and swollen, spongy gums that bleed easily. WBC 68,000/µL with 70% large blasts with folded nuclei that are strongly non-specific esterase positive; haemoglobin 7.8 g/dL, platelets 31,000/µL. Why are the gums swollen?",
         ["Vitamin C deficiency from poor intake", "Gingival infiltration by leukemic cells with monocytic differentiation", "Drug-induced gingival hyperplasia",
          "Thrombocytopenic bleeding into the gingiva only", "Periodontitis from neutropenia"], 1,
         "Blast ที่ **non-specific esterase บวก** = สาย monocyte → **AML with monocytic differentiation (FAB M4/M5)** (สไลด์: AML M4/5 อยู่ในสาเหตุ monocytosis)\n\n"
         "blast สาย monocyte ยังมีคุณสมบัติของ monocyte ที่ **ออกจากหลอดเลือดไปฝังในเนื้อเยื่อ** → **เหงือกบวมหนา** leukemia cutis และ CNS\n\n"
         "- เกล็ดเลือดต่ำทำให้เลือดออก แต่ไม่ทำให้เหงือก **หนาขึ้น**\n- ไม่มีประวัติยา (phenytoin, cyclosporine, nifedipine)\n- ขาดวิตามินซีไม่อธิบาย blast",
         "เหงือกบวม + blast = AML monocytic (M4/M5)", "Acute myeloid leukemia", ["Williams Hematology — AML (ไม่ได้มาจากสไลด์)"], AL),
     mcq(N(16), "A 31-year-old woman presents with gum bleeding, widespread ecchymoses and heavy menstrual bleeding. Platelets 18,000/µL, PT prolonged, fibrinogen 72 mg/dL, D-dimer markedly raised. The smear shows abnormal promyelocytes with heavy granules and bundles of Auer rods. What is the most important immediate step?",
         ["Await PML::RARA confirmation before any specific treatment", "Start all-trans retinoic acid (ATRA) immediately while supporting with platelets and cryoprecipitate",
          "Perform urgent leukapheresis", "Give heparin infusion", "Give tranexamic acid alone and observe"], 1,
         "นี่คือ **acute promyelocytic leukemia (APL)** — granule ของ promyelocyte มี **tissue factor** กระตุ้น DIC และผิวเซลล์มี **annexin II** เพิ่ม plasmin → **hyperfibrinolysis** fibrinogen ต่ำมาก เสี่ยงเลือดออกในสมองตั้งแต่วันแรก\n\n"
         "**ให้ ATRA ทันทีที่สงสัยจาก smear** (ทำให้ promyelocyte เจริญต่อ หยุดปล่อยสารก่อ DIC) ไม่ต้องรอผลยีน · ให้เกล็ดเลือดและ cryoprecipitate/fibrinogen ทดแทน\n\n"
         "- **สไลด์: leukapheresis ห้ามใน APL** — ทำให้ DIC แย่ลง\n- heparin และ tranexamic acid ไม่ใช่การรักษาหลัก\n\n*(รายละเอียด APL ไม่ได้มาจากสไลด์)*",
         "สงสัย APL → ATRA ทันที · ห้าม leukapheresis", "Acute promyelocytic leukemia", ["สไลด์ อ.เบญจมาภรณ์ — Hyperleukocytosis (leukapheresis contraindicated in APL)", "ELN APL recommendations"], AL + ["B2.2.2(8)"]),
     mcq(N(17), "A 6-year-old boy has 2 weeks of leg pain that wakes him at night, limping, pallor and petechiae. There is tenderness over the sternum and tibiae. What mechanism best explains the bone pain?",
         ["Osteomyelitis from neutropenia", "Expansion of the marrow cavity by proliferating blasts, raising intramedullary pressure and stretching the periosteum",
          "Hypercalcaemia from PTHrP", "Avascular necrosis from steroids", "Growth pains unrelated to the cytopenias"], 1,
         "ใน acute leukemia (ที่พบบ่อยในเด็กคือ ALL) blast แบ่งตัวเต็มโพรงไขกระดูกซึ่ง **ขยายไม่ได้** → **แรงดันในโพรงสูง** และ **ดันยืดเยื่อหุ้มกระดูก (periosteum)** ที่มีปลายประสาทรับความเจ็บ → ปวดกระดูก ปวดกลางคืน **sternum กดเจ็บ**\n\n"
         "ร่วมกับซีดและจุดเลือด (ไขกระดูกถูกยึด) ภาพนี้ต้องตรวจ CBC smear ทันที — อย่าวินิจฉัยว่าเป็น growing pain\n\n*(ไม่ได้มาจากสไลด์)*",
         "ปวดกระดูก + ซีด + จุดเลือดในเด็ก = คิดถึง ALL", "Acute leukemia — bone pain", ["Williams Hematology — ALL (ไม่ได้มาจากสไลด์)"], AL),
    ], AL, SRC7, F7)

# ───────────────────────────── 8
RBCQ = [(40, 135), (40, 148), (62, 135), (62, 148), (84, 135), (84, 148), (106, 141)]
F8 = {"leukostasis": fig("Leukostasis — ทำไม blast อุดหลอดเลือดฝอย",
 "บน: หลอดเลือดฝอยกว้างพอ ๆ กับเม็ดเลือดแดง เซลล์ปกติ **เล็กและยืดหยุ่น** จึงเบียดผ่านได้ · "
 "ล่าง: **myeloblast ใหญ่ แข็ง เปลี่ยนรูปไม่ได้** และหลั่ง cytokine ทำให้ผนังหลอดเลือดเหนียว blast จึง **เกาะผนังและอุดตัน** เม็ดเลือดแดงค้างอยู่ด้านหลัง เนื้อเยื่อปลายทางขาด O2 · "
 "blast ยังใช้ O2 เองสูง และทำลายผนังหลอดเลือดจนเลือดออก (ถุงลม สมอง จอตา) · "
 "**การให้ PRC เพิ่มปริมาตรเซลล์ในเลือด → ความหนืดสูงขึ้นอีก** (✍️ \"ยิ่งข้นนะ!\") · lymphocyte ของ CLL เล็กและยืดหยุ่น จึงอุดตันยากแม้ WBC หลายแสน "
 "(อาการจากสไลด์ · ภาพกลไกวาดเพื่ออธิบาย)",
 svg(420, 322, "หลอดเลือดฝอยปกติที่เซลล์ไหลผ่านได้ เทียบกับ hyperleukocytosis ที่ blast ใหญ่อุดตัน และอาการที่ปอด สมอง ตา",
     t(14, 18, "หลอดเลือดฝอยปกติ", "sm b tok"),
     line(14, 30, 406, 30, "ln w2"), line(14, 64, 406, 64, "ln w2"),
     *[ell(x, 47, 9, 5, "badf") for x in (40, 72, 104, 136, 168, 268, 300, 332)],
     ell(214, 47, 15, 8, "ac"), ell(207, 47, 3.5, 3.5, "acf"), ell(215, 46, 3.5, 3.5, "acf"), ell(222, 48, 3.5, 3.5, "acf"),
     ar(352, 47, 398, 47, "lok w2", "ah-ok"),
     t(14, 84, "เซลล์เล็กและยืดหยุ่น เบียดผ่านได้", "xs i2"),
     t(14, 112, "Hyperleukocytosis — blast ใหญ่ แข็ง เกาะผนัง", "sm b tbad"),
     line(14, 124, 406, 124, "ln w2"), line(14, 158, 406, 158, "ln w2"),
     *[ell(x, y, 9, 5, "badf") for x, y in RBCQ],
     *[circ(x, 141, 15, "bad") + circ(x, 141, 11, "badf") for x in (140, 172, 204, 236)],
     line(156, 124, 156, 127, "lbad w2"), line(220, 158, 220, 155, "lbad w2"),
     t(330, 146, "เลือดไม่ถึง → ขาด O2", "xs b tbad mid"),
     fan(210, 160, [77, 210, 343], 172, 185),
     box(14, 186, 126, 56, "bad", "ปอด\nหอบ O2 ต่ำ\nเลือดออกในถุงลม", fs=11.5),
     box(147, 186, 126, 56, "bad", "สมอง\nปวดหัว สับสน\nstroke · เลือดออก", fs=11.5),
     box(280, 186, 126, 56, "bad", "ตา\nจอตาเลือดออก\nเส้นเลือดดำโป่ง", fs=11.5),
     box(14, 258, 392, 30, "ms", "ให้เม็ดเลือดแดง (PRC) → เลือดข้นขึ้นอีก — เลี่ยงจนกว่า WBC จะลด", fs=11.5),
     t(210, 310, "AML อุดตันได้ที่ WBC ต่ำกว่า ALL และ CLL มาก", "xs mid i2")))}

HL = ["B2.2.4-3(1)", "2.1.34", "2.2.39"]
sec("hon-wbc-08", "Hyperleukocytosis และ leukostasis",
    "พบบ่อย AML > ALL >>> CML CLL · AML > 50,000–100,000 · ALL > 100,000–400,000 · CML ระยะลุกลาม > 300,000 · CLL > 500,000 · ปอด สมอง ตา · ห้ามให้ PRC · hydroxyurea dexamethasone leukapheresis (ห้ามใน APL)", 10,
"""### ภาพรวม (สไลด์)
✍️ **"อาการ: stroke / confusion"** — leukostasis คือ WBC สูงมากจนเลือดไหลผ่านหลอดเลือดฝอยไม่ได้ เกิดอาการที่ **ปอดและสมอง** เป็นหลัก · **Laboratory analysis is usually diagnostic**
| โรค | WBC ที่มักทำให้เกิด (สไลด์) |
|---|---|
| **ความถี่: AML > ALL >>> CML, CLL** | |
| **AML** | **> 100,000** (สไลด์ระบุ acute myeloblastic leukemia ที่ **> 50,000–100,000** ด้วย) |
| **ALL** | **> 100,000–400,000** |
| **CML** | มักอยู่ใน **accelerated/blast phase** · **> 300,000** |
| **CLL** | พบน้อยมาก · **> 500,000–1,000,000** |
- สไลด์ยังยกข้อความเรื่อง hyperviscosity ทั่วไป: Hct สูงและ rouleaux · ห้องแล็บรายงานว่า **เลือดข้นเกินกว่าจะตรวจได้** · ตรวจระบบประสาทอาจพบ focal deficit
[[fig:leukostasis]]
#### ทำไมถึงมีอาการนี้ — ทำไม AML อุดตันได้ที่ WBC ต่ำกว่า CLL หลายเท่า
| ปัจจัย | AML blast | ลิมโฟไซต์ของ CLL |
|---|---|---|
| ขนาด | **ใหญ่** กว่าหลอดเลือดฝอย | **เล็ก** ใกล้เม็ดเลือดแดง |
| ความยืดหยุ่น | **แข็ง** เปลี่ยนรูปไม่ได้ | ยืดหยุ่น เบียดผ่านได้ |
| การเกาะผนัง | หลั่ง cytokine → ผนังหลอดเลือดแสดง adhesion molecule → **เกาะ** | น้อย |
| การใช้ O2 | blast แบ่งตัวเร็ว **ใช้ O2 สูง** → ขาด O2 เฉพาะที่ | ต่ำ |
| ผล | อุดตันได้ตั้งแต่ **50,000–100,000** | แทบไม่อุดตันแม้ **> 500,000** |
*(เหตุผลเชิงกลไกเติมจากตำรา — ตัวเลขเป็นของสไลด์)*

### อาการ (สไลด์) และกลไก
| ระบบ | อาการ (สไลด์) | กลไก |
|---|---|---|
| **ปอด/หัวใจ** | หอบ หายใจเร็ว **hypoxemia** · **DAH (diffuse alveolar hemorrhage)** · CXR interstitial หรือ alveolar infiltration | blast อุดหลอดเลือดฝอยปอด → V/Q mismatch · ทำลายผนังจนเลือดออกในถุงลม |
| **สมอง** | ปวดศีรษะ ตามัว **หูอื้อ** focal neurological deficit **เลือดออกในสมอง (ICH)** ระดับความรู้สึกตัวลดลง | อุดตันหลอดเลือดเล็ก + ผนังเปราะ + เกล็ดเลือดต่ำ |
| **ตา** | **จอตาเลือดออก papilledema exudates เส้นเลือดดำโป่งเป็นปล้อง (sausage-like)** | หลอดเลือดดำที่จอตาอุดตันและคั่ง |

### กับดักของผลแล็บเมื่อ WBC สูงมาก {ns}
- **Pseudohypoxemia** — WBC จำนวนมากในหลอดเก็บ ABG **ใช้ O2 ต่อ** ระหว่างรอส่ง → PaO2 ต่ำเท็จ · เชื่อ SpO2 มากกว่า ส่งตรวจทันทีบนน้ำแข็ง
- **Pseudohyperkalemia** — WBC แตกในหลอดเลือดที่แข็งตัว ปล่อย K ออกมา → ตรวจ K จาก plasma (heparin) หรือ blood gas ก่อนตัดสินใจรักษา

### การรักษา (สไลด์)
| ส่วน | สิ่งที่ทำ | เหตุผล |
|---|---|---|
| **Supportive** | **IV hydration · O2** · **เฝ้าระวัง TLS** | เซลล์ตายเร็วเมื่อเริ่มยา |
| | **หลีกเลี่ยง PRC** (✍️ "ยิ่งข้นนะ!") | ความหนืดขึ้นกับปริมาตรเซลล์รวม — เพิ่ม RBC = เพิ่มความหนืด · ให้เกล็ดเลือดได้ (ปริมาตรเซลล์น้อย) |
| **Specific** | **ยาเคมีเฉพาะโรค** | กำจัดต้นเหตุ |
| | **Hydroxyurea 50–100 mg/kg/day ใน AML** | ยับยั้ง ribonucleotide reductase → ลด WBC ภายในไม่กี่วัน |
| | **Dexamethasone IV ใน ALL** (✍️ "สลาย lymphocyte") | steroid ทำให้ lymphoblast ตาย |
| | **Leukapheresis** (✍️ "เอา WBC ออก") — ได้ผล **ชั่วคราว** | ไขกระดูกยังสร้าง blast ต่อ · **ห้ามใน APL — DIC แย่ลง** |
""".format(ns=NOTSLIDE),
    ["Leukostasis: AML > ALL >>> CML CLL",
     "AML > 50,000–100,000 · ALL > 100,000–400,000 · CML > 300,000 · CLL > 500,000",
     "อาการหลัก: ปอด (hypoxemia DAH) และสมอง (stroke สับสน ICH) + จอตา",
     "ห้ามให้ PRC — เลือดข้นขึ้นอีก",
     "Hydroxyurea ใน AML · dexamethasone ใน ALL · leukapheresis ห้ามใน APL"],
    [mcq(N(18), "A 64-year-old man with newly diagnosed AML has WBC 186,000/µL (90% blasts), haemoglobin 6.9 g/dL, platelets 22,000/µL, SpO2 89% on room air, headache and confusion. Which action should be avoided at this point?",
         ["Oxygen therapy", "IV hydration and monitoring for tumour lysis", "Hydroxyurea for rapid cytoreduction",
          "Transfusing packed red cells to raise haemoglobin to 10 g/dL", "Urgent haematology consultation for induction chemotherapy"], 3,
         "ผู้ป่วยมี **leukostasis** (หอบ O2 ต่ำ สับสน) จาก hyperleukocytosis\n\n"
         "สไลด์: **Avoid PRC transfusion — it will worsen leukocytosis** (✍️ \"ยิ่งข้นนะ!\") — ความหนืดของเลือดขึ้นกับปริมาตรเซลล์รวม การเพิ่มเม็ดเลือดแดงทำให้ข้นและอุดตันมากขึ้น ให้เลือดเมื่อ WBC ลดลงแล้วหรือเมื่อจำเป็นจริงในปริมาณน้อย\n\n"
         "ข้ออื่นเป็นการรักษาตามสไลด์: **IV hydration, O2, observe TLS, hydroxyurea 50–100 mg/kg/day ใน AML, ยาเคมีเฉพาะโรค**",
         "Leukostasis: ห้ามให้ PRC จนกว่า WBC จะลด", "Hyperleukocytosis treatment", R("Hyperleukocytosis"), HL),
     mcq(N(19), "Leukostasis develops in AML at WBC counts of 50,000–100,000/µL but is rarely seen in CLL even above 500,000/µL. What best explains this difference?",
         ["CLL cells are destroyed in the spleen before they can obstruct vessels", "Myeloblasts are large, rigid and adhesive to endothelium, whereas CLL lymphocytes are small and deformable",
          "CLL patients are always anticoagulated", "AML causes hyperviscosity through paraprotein production", "Lymphocytes cannot enter capillaries"], 1,
         "ความหนืดและการอุดตันขึ้นกับ **ขนาด ความแข็ง และการเกาะผนัง** ของเซลล์ ไม่ใช่จำนวนอย่างเดียว\n"
         "- **myeloblast ใหญ่ แข็ง** และหลั่ง cytokine ทำให้ผนังหลอดเลือดแสดง adhesion molecule → เกาะและอุดตัน · ใช้ O2 สูง\n"
         "- **lymphocyte ของ CLL เล็กและยืดหยุ่น** เบียดผ่านหลอดเลือดฝอยได้\n\n"
         "สไลด์จึงให้เกณฑ์ **AML > 50,000–100,000** แต่ **CLL > 500,000–1,000,000** และ \"rarely seen\" · paraprotein เป็นกลไกของ myeloma/Waldenström",
         "Leukostasis ขึ้นกับขนาดและความแข็งของเซลล์ ไม่ใช่จำนวนอย่างเดียว", "Hyperleukocytosis pathophysiology", R("Hyperleukocytosis"), HL),
    ], HL, SRC, F8)

# ───────────────────────────── 9
FOL = [(120, 90, 13), (168, 74, 12), (228, 72, 12), (102, 140, 12), (150, 164, 11)]
def mini(x, y, title, tc, drawing, lines):
    return (rect(x, y, 194, 100, "bx") + t(x + 8, y + 18, title, "sm b " + tc) + drawing
            + "".join(t(x + 88, y + 40 + i * 15, s_, "xs i2") for i, s_ in enumerate(lines)))
def dots(cx, cy, r, c):
    return "".join(circ(cx + dx, cy + dy, 1.6, c) for dx in range(-18, 19, 6) for dy in range(-18, 19, 6) if dx * dx + dy * dy <= (r - 4) ** 2)
F9 = {"node": fig("ต่อมน้ำเหลือง — โครงสร้างและเหตุที่คลำได้ต่างกัน",
 "น้ำเหลืองจากบริเวณที่ต่อมรับผิดชอบไหล **เข้าทาง afferent** ผ่าน subcapsular sinus (เส้นประ) → cortex (follicle ของ B cell) → paracortex (T cell) → medulla → **ออกทาง efferent ที่ hilum** · "
 "ต่อมจึงโตตามสิ่งที่ไหลเข้ามา (เชื้อ เซลล์มะเร็ง) หรือจากเซลล์ในต่อมเองแบ่งตัว (lymphoma) · **ความเจ็บมาจากแคปซูลที่มีปลายประสาท**: "
 "**ติดเชื้อเฉียบพลัน** บวมเร็วจนแคปซูลยืดไม่ทันจึงเจ็บ แดง ร้อน · **lymphoma** โตช้าและเต็มไปด้วยเซลล์สม่ำเสมอ จึงหยุ่นแบบยางลบและไม่เจ็บ · "
 "**มะเร็งแพร่กระจาย** สร้างพังผืดและลามทะลุแคปซูล จึงแข็งและติดแน่น · **วัณโรค** มีเนื้อตาย caseous ที่เหลวกลายเป็นหนองเย็น ต่อมหลายต่อมอักเสบติดกันเป็นพวง และแตกเป็นรูเรื้อรัง "
 "(ลักษณะต่อมจากสไลด์ · กลไกเติมจากตำรา)",
 svg(420, 444, "โครงสร้างต่อมน้ำเหลืองและภาพเปรียบเทียบต่อมจากการติดเชื้อเฉียบพลัน lymphoma มะเร็งแพร่กระจาย และวัณโรค",
     t(14, 16, "น้ำเหลืองเข้า (afferent)", "xs b twa"),
     ar(84, 22, 98, 60, "lwa", "ah-wa"), ar(156, 22, 162, 52, "lwa", "ah-wa"), ar(240, 22, 236, 52, "lwa", "ah-wa"),
     ell(200, 120, 150, 70, "bx w2"), ell(200, 120, 141, 61, "lwa da"),
     ell(188, 124, 92, 40, "wa ns"),
     *[circ(x, y, r, "ac") for x, y, r in FOL],
     ell(296, 120, 32, 30, "sk"), t(296, 124, "Medulla", "xs mid i2"),
     t(190, 128, "Paracortex (T)", "xs b mid twa"),
     t(14, 70, "Follicle", "xs b tac"), t(14, 86, "(B cell)", "xs tac"), line(56, 80, 106, 88, "lmu"),
     ar(350, 120, 404, 120, "lwa w2", "ah-wa"), t(378, 110, "efferent", "xs b twa mid"),
     line(200, 190, 200, 200, "lmu"), t(200, 212, "Capsule — มีปลายประสาทรับความเจ็บ", "xs mid i2"),
     mini(14, 226, "ติดเชื้อเฉียบพลัน", "tbad",
          circ(56, 286, 30, "lbad da") + circ(56, 286, 21, "bad")
          + ar(56, 265, 56, 252, "lbad", "ah-bad") + ar(77, 286, 90, 286, "lbad", "ah-bad") + ar(35, 286, 22, 286, "lbad", "ah-bad") + ar(56, 307, 56, 320, "lbad", "ah-bad"),
          ["บวมเร็ว", "แคปซูลยืดเร็ว", "→ กดเจ็บ แดง ร้อน"]),
     mini(212, 226, "Lymphoma", "tac", circ(256, 286, 26, "ac") + dots(256, 286, 26, "acf"),
          ["โตช้า เซลล์แน่น", "สม่ำเสมอ", "→ หยุ่นแบบยางลบ", "ไม่เจ็บ"]),
     mini(14, 334, "มะเร็งแพร่กระจาย", "tms",
          poly([(56, 362), (66, 376), (84, 372), (78, 390), (90, 402), (72, 406), (66, 422), (54, 408), (36, 414), (40, 396), (26, 386), (44, 378), (42, 364)], "ms", True)
          + path("M44 384 L68 400 M50 400 L72 382 M58 372 L60 410", "lms"),
          ["มะเร็งสร้างพังผืด", "ลามทะลุแคปซูล", "→ แข็ง ติดแน่น", "ไม่เจ็บ"]),
     mini(212, 334, "วัณโรค", "i2",
          circ(242, 396, 15, "sk") + circ(266, 390, 16, "sk") + circ(256, 410, 13, "sk")
          + ell(254, 398, 12, 8, "paf") + ell(254, 398, 12, 8, "lms da") + path("M266 376 Q272 362 276 348", "lms w2"),
          ["เนื้อตาย caseous", "ลามติดกันเป็นพวง", "→ นิ่ม fluctuant", "แตกเป็นรูเรื้อรัง"])))}
F9["ladflow"] = fig("Approach to lymphadenopathy — เมื่อไรเฝ้าดู เมื่อไรตัดต่อม",
 "เริ่มจากแยก **เฉพาะที่ vs ทั่วตัว** (สไลด์) แล้วหา **red flag** · ไม่มี red flag และดูเป็นการติดเชื้อ → รักษาหรือเฝ้าดูราว 2–4 สัปดาห์ (✍️ \"Augmentin\" ข้างต่อมโตเฉียบพลัน 1–2 สัปดาห์) · "
 "**มี red flag หรือไม่ยุบ → ตัดต่อมทั้งต่อม (excisional biopsy)** เพราะการวินิจฉัยและแบ่งชนิด lymphoma ต้องเห็น **โครงสร้างของต่อม** และต้องใช้ชิ้นเนื้อมากพอสำหรับ immunohistochemistry flow cytometry และยีน · "
 "FNA พอสำหรับมะเร็งแพร่กระจายหรือวัณโรค · **ห้ามให้ steroid ก่อนได้ชิ้นเนื้อ** — lymphoma ยุบจนวินิจฉัยไม่ได้ (✍️ \"ต้องทำหลัง get tissue!\") "
 "*(เกณฑ์ red flag และระยะเวลาเฝ้าดูไม่ได้อยู่ในสไลด์ — เติมจากแนวทางทั่วไป)*",
 svg(420, 418, "แผนภูมิการตัดสินใจเมื่อพบต่อมน้ำเหลืองโต แยกเฉพาะที่หรือทั่วตัว ดู red flag เฝ้าดูหรือตัดชิ้นเนื้อ",
     box(110, 8, 200, 30, "ac", "ต่อมน้ำเหลืองโต"),
     ar(210, 38, 210, 51),
     box(40, 52, 340, 34, "ms", "เฉพาะที่ หรือ ทั่วตัว (≥ 2 กลุ่มที่ไม่ติดกัน)?", fs=12),
     ar(120, 86, 107, 107), ar(300, 86, 313, 107),
     box(14, 108, 186, 58, "bx", "เฉพาะที่ (localized)\nตรวจบริเวณที่ระบายน้ำเหลือง\nหาแผล ฟันผุ การติดเชื้อ", fs=11),
     box(220, 108, 186, 58, "bx", "ทั่วตัว (generalized)\nCBC smear · anti-HIV · EBV\nANA · TB · ทบทวนยา", fs=11),
     ar(107, 166, 150, 189), ar(313, 166, 270, 189),
     box(14, 190, 392, 52, "bad", "Red flag: อายุ > 40 · > 2 ซม. · แข็ง ติดแน่น เป็นพวง\nsupraclavicular · B symptoms · ม้ามโต · โตต่อเนื่อง", fs=11.5),
     ar(107, 242, 107, 265), t(115, 258, "ไม่มี", "xs b tok"), ar(313, 242, 313, 265), t(321, 258, "มี", "xs b tbad"),
     box(14, 266, 186, 62, "ok", "รักษา/เฝ้าดู 2–4 สัปดาห์\nสงสัยแบคทีเรีย → ยาปฏิชีวนะ\nแล้วนัดคลำซ้ำ", fs=11),
     box(220, 266, 186, 62, "bad", "ส่งตรวจชิ้นเนื้อ\nเลือกต่อมที่ผิดปกติที่สุด\nเลี่ยงขาหนีบถ้าเลือกได้", fs=11),
     ar(107, 328, 150, 351), t(70, 346, "ไม่ยุบ", "xs b tms"), ar(313, 328, 270, 351),
     box(14, 352, 392, 58, "ac", "Excisional biopsy ทั้งต่อม — lymphoma ต้องดูโครงสร้างต่อม\nFNA พอแค่มะเร็งแพร่กระจาย/TB · ห้าม steroid ก่อนได้ชิ้นเนื้อ", fs=11.5)))

LAD = ["2.1.57", "2.3.3(6)", "B2.2.2(9)", "B2.1.1(4)"]
sec("hon-wbc-09", "Approach to lymphadenopathy — ประวัติ ลักษณะต่อม และเมื่อไรต้อง biopsy",
    "Primary/secondary lymphoid tissue · localized vs generalized · EBV TB NTM เชื้อรา SLE RA Sjögren lymphoma · acute 1–2 สัปดาห์ vs chronic · lymphoma ยางลบ เป็นพวง ไม่เจ็บ · metastasis แข็ง ติดแน่น · infection เจ็บ แดง มีรู · excisional biopsy", 12,
"""### ระบบน้ำเหลือง (สไลด์)
| | อวัยวะ | หน้าที่ |
|---|---|---|
| **Primary lymphoid tissue** | **ไขกระดูก · thymus** | ที่เกิดและคัดเลือก lymphocyte (B ในไขกระดูก T ใน thymus) |
| **Secondary lymphoid tissue** | **ต่อมน้ำเหลือง · ม้าม · Waldeyer's ring · lymphoid aggregates ในทางเดินหายใจและลำไส้ (Peyer's patches)** | ที่ lymphocyte พบ antigen และตอบสนอง — **ที่เกิดต่อมโตและ lymphoma** |

### สาเหตุ (สไลด์)
- แบ่ง **localized** vs **generalized** (ทั่วตัว = โตตั้งแต่ 2 กลุ่มที่ไม่ติดกันขึ้นไป *(นิยามไม่ได้อยู่ในสไลด์)*)
| กลุ่ม | ตัวอย่าง (สไลด์) |
|---|---|
| **Infection** | **EBV · TB · NTM · fungus** (และ HIV ซิฟิลิส แมวข่วน ฯลฯ ในหัวข้อถัดไป) |
| **Autoimmune** | **SLE · rheumatoid arthritis · Sjögren's syndrome** |
| **Malignancy** | **lymphoma** (และมะเร็งแพร่กระจาย) |
| **Rare** | sarcoidosis · **Castleman's disease** · **Kikuchi's disease** · Rosai-Dorfman disease |

### ประวัติ — onset (สไลด์)
- **Acute ภายใน 1–2 สัปดาห์ → viral infection** (✍️ ลูกศรไป "Augmentin" — ต่อมโตเฉียบพลันที่สงสัยแบคทีเรียรักษาด้วยยาปฏิชีวนะแล้วนัดดู)
- **Chronic → chronic infection (TB) หรือ malignancy**
- ถามเพิ่ม: ไข้ เหงื่อออกกลางคืน น้ำหนักลด (B symptoms) · คัน · ปวดต่อมหลังดื่มเหล้า · สัตว์เลี้ยง (แมว) · เพศสัมพันธ์ · ยา (phenytoin) · ผู้สัมผัสวัณโรค

### ตรวจร่างกาย — ขนาดและลักษณะ (สไลด์)
| | **Lymphoma** | **Metastatic cancer** | **Infection** |
|---|---|---|---|
| ขนาด | หลากหลาย | หลากหลาย | |
| เนื้อ | **rubbery firm** (✍️ วง) | **hard** (✍️ วง) | นิ่ม |
| การยึด | **matted** (✍️ วง) | **fixed with surrounding tissue** (✍️ วง) | |
| ความเจ็บ | **nontender** (✍️ วง) | ไม่เจ็บ | **tender · ผิวแดง · มี sinus tract** |
[[fig:node]]
#### ทำไมถึงมีอาการนี้ — ต่อมแต่ละแบบ
| ลักษณะ | กลไก | นึกถึง |
|---|---|---|
| **กดเจ็บ แดง ร้อน** | การอักเสบเฉียบพลัน → เลือดคั่ง บวมน้ำ เซลล์อักเสบ → ต่อม **โตเร็วจนแคปซูลที่มีปลายประสาทยืดไม่ทัน** · การอักเสบลามรอบต่อม | ติดเชื้อแบคทีเรีย ไวรัส · Kikuchi ก็เจ็บได้ |
| **ไม่เจ็บ** | **โตช้า** แคปซูลค่อย ๆ ขยายตาม · ไม่มีการอักเสบเฉียบพลัน | lymphoma มะเร็ง TB เรื้อรัง — ต่อมที่ไม่เจ็บน่ากังวลกว่า |
| **หยุ่นแบบยางลบ (rubbery)** | ต่อมเต็มไปด้วย lymphocyte มะเร็ง **ชนิดเดียวเรียงแน่นสม่ำเสมอ** ไม่ค่อยมีพังผืด | lymphoma |
| **แข็งเหมือนหิน ติดแน่น** | carcinoma กระตุ้น **desmoplasia (พังผืด)** และ **ลามทะลุแคปซูล** ยึดติดโครงสร้างรอบข้าง | มะเร็งแพร่กระจาย |
| **เป็นพวงติดกัน (matted)** | การอักเสบหรือมะเร็ง **ลามข้ามแคปซูล (periadenitis)** เชื่อมต่อมข้างเคียงเข้าด้วยกัน | TB · lymphoma (Hodgkin) · มะเร็งแพร่กระจาย |
| **นิ่ม fluctuant ไม่ค่อยร้อน มีรูหนองเรื้อรัง** | **caseous necrosis** เหลวกลายเป็น **หนองเย็น (cold abscess)** → ทะลุผิวหนังเป็น sinus tract (scrofuloderma) | **TB** (สไลด์: cervical suppurative = tuberculosis) |
| **ปวดต่อมหลังดื่มเหล้า** | พบน้อยแต่ค่อนข้างจำเพาะต่อ **Hodgkin lymphoma** — กลไกยังไม่ชัด (เชื่อว่าเกี่ยวกับหลอดเลือดในต่อมขยายตัว) | หัวข้อ 12 |

### เมื่อไรต้องตัดต่อม และตัดอย่างไร {ns}
[[fig:ladflow]]
- ต่อมผิดปกติโดยทั่วไปเมื่อ **> 1 ซม.** (epitrochlear > 0.5 ซม. · ขาหนีบ > 1.5 ซม.) · **supraclavicular คลำได้ถือว่าผิดปกติเสมอ**
- **Excisional biopsy ทั้งต่อม** เป็นมาตรฐานเมื่อสงสัย lymphoma (Lugano 2014) — FNA ได้แค่เซลล์กระจาย ไม่เห็นว่าเซลล์เรียงตัวแบบ follicle หรือทำลายโครงสร้างต่อม · core needle biopsy ใช้เมื่อตัดทั้งต่อมไม่ได้
- **FNA เพียงพอ** สำหรับมะเร็งแพร่กระจาย (carcinoma) และวัณโรค (AFB, PCR)
- เลือก **ต่อมที่ใหญ่และผิดปกติที่สุด** · เลี่ยงขาหนีบถ้ามีที่อื่น (มักเป็น reactive)
- **ห้ามให้ steroid ก่อนได้ชิ้นเนื้อ** — lymphoma ยุบชั่วคราวจนผลชิ้นเนื้อไม่ชัด (✍️ สไลด์ SVC: \"ยุบแน่นอน → ต้องทำหลัง get tissue!\")
""".format(ns=NOTSLIDE),
    ["Acute 1–2 สัปดาห์ = viral · chronic = TB/มะเร็ง",
     "Lymphoma: ยางลบ เป็นพวง ไม่เจ็บ · metastasis: แข็ง ติดแน่น · infection: เจ็บ แดง มีรู",
     "เจ็บ = แคปซูลยืดเร็วจากการอักเสบ · ไม่เจ็บ = โตช้า",
     "สงสัย lymphoma → excisional biopsy ไม่ใช่ FNA",
     "ห้าม steroid ก่อนได้ชิ้นเนื้อ"],
    [mcq(N(20), "A 26-year-old man has a 3.5-cm rubbery, non-tender, matted right cervical lymph node mass for 2 months, with night sweats and 8 kg weight loss. What is the best next diagnostic step?",
         ["Fine-needle aspiration cytology of the largest node", "A 2-week trial of oral prednisolone", "Excisional biopsy of an entire abnormal lymph node",
          "Observation for another 4 weeks", "Empirical anti-tuberculous therapy"], 2,
         "ต่อม **ยางลบ เป็นพวง ไม่เจ็บ** (สไลด์: ลักษณะของ lymphoma) + **B symptoms** + เรื้อรัง = สงสัย **lymphoma** (เช่น Hodgkin ในคนหนุ่ม)\n\n"
         "การวินิจฉัยและแบ่งชนิด lymphoma ต้องเห็น **โครงสร้างของต่อม** และใช้ชิ้นเนื้อพอสำหรับ IHC/flow/ยีน → **excisional biopsy ทั้งต่อม**\n\n"
         "- FNA ไม่เห็นโครงสร้าง มักสรุปไม่ได้\n- **steroid ทำให้ lymphoma ยุบจนวินิจฉัยไม่ได้**\n- มี red flag แล้ว ไม่ควรเฝ้าดูหรือให้ยา TB โดยไม่มีหลักฐาน",
         "สงสัย lymphoma → excisional biopsy · ห้าม steroid ก่อน", "Approach to lymphadenopathy", R("Approach") + ["Lugano classification 2014"], LAD + ["B1.6.1(1)"]),
     mcq(N(21), "A 21-year-old woman has a 2-cm exquisitely tender, warm submandibular lymph node that appeared 3 days after a dental abscess. What best explains why this node is painful while lymphomatous nodes are typically painless?",
         ["Desmoplastic fibrosis compressing nerves", "Rapid inflammatory enlargement stretching the innervated nodal capsule", "Caseous necrosis within the node",
          "Tumour invasion of adjacent sensory nerves", "Obstruction of efferent lymphatics only"], 1,
         "ความเจ็บของต่อมมาจาก **แคปซูลที่มีปลายประสาท** — การอักเสบเฉียบพลันทำให้เลือดคั่ง บวมน้ำ และเซลล์อักเสบเข้ามา **ต่อมโตเร็วจนแคปซูลถูกยืดเร็ว** จึงเจ็บ แดง ร้อน (สไลด์: infection = tender with erythematous skin)\n\n"
         "lymphoma และมะเร็ง **โตช้า** แคปซูลค่อย ๆ ขยายตาม จึงไม่เจ็บ · desmoplasia ทำให้ **แข็ง** (มะเร็งแพร่กระจาย) · caseous necrosis ทำให้ **นิ่ม เป็นหนองเย็น** (TB)",
         "เจ็บ = โตเร็วจากการอักเสบ · ไม่เจ็บ = โตช้า", "Lymph node characteristics", R("Approach"), LAD),
     mcq(N(22), "A 30-year-old man has several matted, firm-to-fluctuant posterior cervical nodes for 6 weeks, mild evening fever, and a chronic draining sinus over one node. Which pathological process best explains these features?",
         ["Reactive follicular hyperplasia", "Caseous necrosis with periadenitis", "Desmoplastic metastatic carcinoma", "Diffuse large B-cell lymphoma", "Kikuchi histiocytic necrotising lymphadenitis"], 1,
         "ต่อมคอ **เป็นพวง (matted) นิ่มเป็นหนอง และมีรูหนองเรื้อรัง** = **tuberculous lymphadenitis (scrofula)** — สไลด์: cervical (suppurative) = tuberculosis และ infection มี **sinus tract formation**\n\n"
         "- **caseous necrosis** เหลวเป็นหนองเย็น → นิ่ม และทะลุผิวหนังเป็นรู\n- การอักเสบลามรอบต่อม (**periadenitis**) ทำให้ต่อมติดกันเป็นพวง\n\n"
         "มะเร็งแพร่กระจายแข็ง ติดแน่น ไม่เป็นหนอง · lymphoma ไม่ค่อยเป็นหนองหรือมีรู · Kikuchi พบในหญิงสาว ต่อมเจ็บ ไม่เป็นรู",
         "ต่อมคอเป็นพวง นิ่ม มีรูหนอง = TB", "Tuberculous lymphadenitis", R("Approach; Sites of enlarged lymph nodes"), LAD + ["2.3.1(20)"]),
    ], LAD, SRC + " · Lugano 2014", F9)

# ───────────────────────────── 10
def mirror(pts):
    return [(420 - x, y) for x, y in pts]
ARM = [(150, 102), (140, 106), (124, 182), (118, 248), (128, 250), (134, 186), (152, 126)]
LEG = [(162, 246), (206, 252), (200, 382), (178, 382)]
NODES_L = [(190, 64), (200, 90), (176, 102), (152, 130), (136, 184), (178, 262)]
NODES_R = [(234, 50), (220, 90), (268, 130), (242, 262)]
LBL_L = [(40, "หลังหู/ท้ายทอย", "หนังศีรษะ หัดเยอรมัน", (190, 64)),
         (92, "Cervical", "ช่องปาก คอหอย · TB", (200, 90)),
         (142, "R supraclavicular", "ปอด mediastinum หลอดอาหาร", (176, 102)),
         (196, "Axillary", "แขน เต้านม", (152, 130)),
         (248, "Epitrochlear", "มือ แขนท่อนล่าง", (136, 184)),
         (302, "Inguinal", "ขา ฝีเย็บ อวัยวะเพศภายนอก", (178, 262))]
LBL_R = [(40, "หน้าหู", "ตา เยื่อบุตา", (234, 50)),
         (96, "L supraclavicular", "= Virchow node", (244, 102)),
         (150, "Thoracic duct", "น้ำเหลืองจากช่องท้อง", (218, 168)),
         (206, "Hilar / mediastinal", "ปอด TB lymphoma", (216, 138)),
         (262, "Para-aortic", "อัณฑะ (ไม่ใช่ขาหนีบ)", (228, 222))]
F10 = {"drainage": fig("ต่อมแต่ละกลุ่มรับน้ำเหลืองจากที่ไหน",
 "ภาพมองจากด้านหน้า — **ซ้ายของภาพคือข้างขวาของผู้ป่วย** · ต่อมโตเฉพาะที่ให้มองหาโรคใน **บริเวณที่ต่อมนั้นรับน้ำเหลือง** · "
 "**Thoracic duct** (เส้นประสีฟ้า) รับน้ำเหลืองจากช่องท้อง อุ้งเชิงกราน ขา และอกซีกซ้าย ขึ้นไปเทเข้ามุมหลอดเลือดดำ **ซ้าย** → เซลล์มะเร็งจากช่องท้อง (เช่น กระเพาะอาหาร) ไปค้างที่ต่อม **supraclavicular ซ้าย = Virchow node** (จุดสีแดง) · "
 "supraclavicular ขวารับจากปอดและ mediastinum · **อัณฑะเกิดในช่องท้องแล้วเลื่อนลงมาพร้อมท่อน้ำเหลืองของตัวเอง** จึงไปต่อม para-aortic ไม่ใช่ขาหนีบ (ขาหนีบรับจากผิวหนังถุงอัณฑะ) "
 "(โรคตามตำแหน่งจากตารางในสไลด์ · ทางเดินน้ำเหลืองเติมจากตำรา)",
 svg(420, 404, "แผนภาพร่างกายด้านหน้าแสดงต่อมน้ำเหลืองแต่ละกลุ่ม บริเวณที่รับน้ำเหลือง thoracic duct และ Virchow node",
     circ(210, 50, 26, "sk"), rect(198, 74, 24, 24, "sk", 4),
     path("M150 100 Q210 90 270 100 L262 248 Q210 260 158 248 Z", "sk"),
     poly(ARM, "sk", True), poly(mirror(ARM), "sk", True), poly(LEG, "sk", True), poly(mirror(LEG), "sk", True),
     path("M214 236 C216 204 211 176 215 146 C219 120 230 108 242 103", "lwa w2 da", "ah-wa"),
     circ(214, 238, 5, "wa"),
     *[line(104, y + 4, nx - 4, ny, "lmu") for y, a, b, (nx, ny) in LBL_L],
     *[line(302, y + 4, nx + 4, ny, "lmu") for y, a, b, (nx, ny) in LBL_R],
     *[circ(x, y, 5, "acf") for x, y in NODES_L + NODES_R],
     circ(204, 138, 4.5, "acf"), circ(216, 138, 4.5, "acf"), circ(200, 222, 4.5, "acf"), circ(228, 222, 4.5, "acf"),
     circ(244, 102, 6, "badf"),
     *[t(8, y, a, "xs b") + t(8, y + 15, b, "xs i2") for y, a, b, n in LBL_L],
     *[t(412, y, a, "xs b end" + (" tbad" if "Virchow" in b else "")) + t(412, y + 15, b, "xs i2 end") for y, a, b, n in LBL_R],
     t(210, 398, "ซ้าย–ขวาของภาพ = ขวา–ซ้ายของผู้ป่วย", "xs mid mu")))}

SITE = ["2.1.57", "2.1.53", "B2.1.1(4)"]
sec("hon-wbc-10", "ตำแหน่งของต่อมบอกต้นเหตุ — แผนที่การระบายน้ำเหลือง",
    "Occipital auricular cervical supraclavicular axillary epitrochlear inguinal hilar mediastinal · Virchow node ทาง thoracic duct · supraclavicular แข็งติดแน่น = มะเร็ง · อัณฑะไป para-aortic · generalized: IM HIV SLE lymphoma syphilis", 9,
"""### ตารางในสไลด์ — Sites of enlarged lymph nodes
| ตำแหน่ง | โรคที่นึกถึง |
|---|---|
| Occipital | scalp infection, insect bites, ringworm · lymphoma หรือมะเร็งแพร่กระจาย (พบน้อย) · cat-scratch disease |
| Posterior auricular | **rubella**, oculoglandular syndromes |
| Anterior auricular | การติดเชื้อที่เปลือกตาและเยื่อบุตา · epidemic keratoconjunctivitis |
| Posterior and anterior cervical | toxoplasmosis · adenovirus · การติดเชื้อในช่องปากและคอหอย |
| Posterior cervical and submental | scalp infection · การติดเชื้อที่ฟัน · tuberculosis |
| **Cervical (suppurative)** | **tuberculosis** |
| **Supraclavicular (hard and fixed)** | **มะเร็งแพร่กระจายจากช่องอกหรือช่องท้อง · Hodgkin's disease** |
| Axillary | การติดเชื้อที่แขน · cat-scratch disease · brucellosis · sporotrichosis · NHL |
| Epitrochlear ข้างเดียว | การติดเชื้อที่มือ · Hodgkin's lymphoma |
| Epitrochlear สองข้าง | viral disease ในเด็ก · sarcoidosis · tularemia |
| Inguinal ข้างเดียว | **LGV, syphilis, chancroid**, gonococcal, herpes · mycoplasma · urethritis · tularemia plague loiasis onchocerciasis · lymphoma · มะเร็งอุ้งเชิงกราน มะเร็งนรีเวช |
| Inguinal สองข้าง | lymphoma |
| Hilar ข้างเดียว | **metastatic lung carcinoma** |
| Hilar สองข้าง | **sarcoidosis**, tuberculosis, histoplasmosis, coccidioidomycosis |
| Mediastinal สมมาตร | **lymphoma** |
| ในช่องท้องและ retroperitoneum | lymphoma · มะเร็งแพร่กระจาย · TB ของต่อม mesentery |
| ร่วมกับการติดเชื้อทั้งระบบ | **infectious mononucleosis**, viral hepatitis, CMV, rubella, influenza, leprosy, toxoplasmosis, **AIDS** |
| **Generalized lymphadenopathy** | sarcoidosis · **hyperthyroidism** · **SLE** · **lymphoma** · **syphilis** |
[[fig:drainage]]
#### ทำไมถึงมีอาการนี้ — ตำแหน่งที่มีความหมายพิเศษ
| ตำแหน่ง | กลไก (ทางเดินน้ำเหลือง) | ความหมาย |
|---|---|---|
| **Supraclavicular ซ้าย (Virchow node)** | **thoracic duct** รับน้ำเหลืองจากช่องท้อง อุ้งเชิงกราน ขา และอกซีกซ้าย แล้วเทเข้ามุมระหว่าง **internal jugular กับ subclavian vein ซ้าย** — เซลล์มะเร็งที่ลอยมาตามท่อค้างที่ต่อมข้างทางเข้า | มะเร็ง **กระเพาะอาหาร** ตับอ่อน ลำไส้ รังไข่ อัณฑะ (Troisier sign) |
| **Supraclavicular ขวา** | รับจาก mediastinum ปอด หลอดอาหาร | มะเร็งปอด หลอดอาหาร lymphoma ในช่องอก |
| Supraclavicular ทั้งสองข้าง | อยู่ปลายทางของน้ำเหลืองจากช่องอกและช่องท้อง | **คลำได้ = ผิดปกติเสมอ** · สไลด์: **แข็งและติดแน่น = มะเร็งแพร่กระจายหรือ Hodgkin** |
| Posterior cervical | รับจากหนังศีรษะ และเป็นที่ชอบของ EBV และ TB | IM · TB · หนังศีรษะอักเสบ |
| Epitrochlear | รับจากมือและแขนด้านใน | ไม่มีแผลที่มือ → นึกถึง lymphoma (สไลด์: Hodgkin) |
| Inguinal | รับจากขา ฝีเย็บ อวัยวะเพศภายนอก และทวารหนักส่วนล่าง | คนเดินเท้าเปล่าโตเล็กน้อยได้ · ข้างเดียว + แผลที่อวัยวะเพศ = STI |
| **อัณฑะ → para-aortic** | อัณฑะเกิดใกล้ไตแล้วเลื่อนลงถุงอัณฑะพร้อมหลอดเลือดและน้ำเหลืองของตัวเอง | มะเร็งอัณฑะไปต่อม **retroperitoneum** ก่อน · ห้ามผ่าตัดผ่านถุงอัณฑะ (ทำให้ไปขาหนีบได้) |
| **Generalized + hyperthyroidism** | ฮอร์โมนไทรอยด์กระตุ้นเนื้อเยื่อ lymphoid ให้โต (thymus ต่อม ม้าม) | ต่อมทั่วตัวที่ไม่ต้องกลัว ถ้าไทรอยด์เป็นพิษชัด |
*(กลไกทางเดินน้ำเหลือง ไม่ได้อยู่ในสไลด์)*
""",
    ["ต่อมโตเฉพาะที่ = ดูบริเวณที่ต่อมรับน้ำเหลือง",
     "Supraclavicular คลำได้ = ผิดปกติเสมอ · แข็งติดแน่น = มะเร็ง/Hodgkin",
     "Virchow node (ซ้าย) = thoracic duct จากช่องท้อง · มะเร็งกระเพาะ",
     "Cervical suppurative = TB · hilar สองข้างสมมาตร = sarcoidosis/TB",
     "อัณฑะ → para-aortic ไม่ใช่ขาหนีบ"],
    [mcq(N(23), "A 64-year-old man has early satiety, epigastric discomfort and 9 kg weight loss. A hard, fixed 2-cm node is palpable just above the medial end of the left clavicle. Which anatomical fact best explains the location of this node?",
         ["The left supraclavicular node drains the left breast only", "The thoracic duct carries lymph from the abdomen and empties into the left venous angle near this node",
          "The right lymphatic duct drains the stomach", "Gastric lymph drains directly to the axilla", "Supraclavicular nodes drain only the scalp"], 1,
         "**Virchow node** — **thoracic duct** รับน้ำเหลืองจากช่องท้อง อุ้งเชิงกราน ขา และอกซีกซ้าย แล้วเทเข้า **มุมหลอดเลือดดำซ้าย** (internal jugular + subclavian) เซลล์มะเร็งกระเพาะที่ลอยตามท่อจึงไปค้างที่ต่อม **supraclavicular ซ้าย**\n\n"
         "สไลด์: supraclavicular **hard and fixed** = metastases จาก intrathoracic หรือ intraabdominal carcinoma · ต่อม **แข็งติดแน่น** เกิดจาก desmoplasia และการลามทะลุแคปซูล\n\n"
         "- right lymphatic duct รับจากแขนขวา หัวและอกซีกขวา\n- เต้านมไปต่อมรักแร้เป็นหลัก",
         "Supraclavicular ซ้ายแข็ง + อาการทางเดินอาหาร = Virchow node", "Sites of lymphadenopathy", R("Sites of enlarged lymph nodes"), SITE + ["B8.2.4-3(1)", "2.3.2-3(1)"]),
     mcq(N(24), "A 29-year-old man has a painless, hard right testicular mass. Which lymph node group is the expected first site of lymphatic spread?",
         ["Right superficial inguinal nodes", "Right external iliac nodes only", "Para-aortic (retroperitoneal) nodes at the level of the renal hilum",
          "Right axillary nodes", "Right supraclavicular nodes"], 2,
         "อัณฑะเกิดใน **ช่องท้องด้านหลังใกล้ไต** แล้วเลื่อนลงถุงอัณฑะ **พร้อมหลอดเลือดและท่อน้ำเหลืองของตัวเอง** (ตามหลอดเลือด gonadal) → น้ำเหลืองจึงไปต่อม **para-aortic/retroperitoneal ระดับไต** ก่อน\n\n"
         "ต่อม **ขาหนีบรับจากผิวหนังถุงอัณฑะ** ไม่ใช่ตัวอัณฑะ — การผ่าตัดผ่านถุงอัณฑะ (trans-scrotal) จึงเสี่ยงให้มะเร็งไปขาหนีบ ต้องทำ radical inguinal orchiectomy\n\n*(ไม่ได้มาจากสไลด์)*",
         "อัณฑะ → para-aortic · ถุงอัณฑะ → ขาหนีบ", "Lymphatic drainage", ["กายวิภาคทางเดินน้ำเหลือง (ไม่ได้มาจากสไลด์)"], SITE),
    ], SITE, SRC + " · กายวิภาคทางเดินน้ำเหลือง (ตำรา)", F10)

# ───────────────────────────── 11
BROWS = [("Precursor B\n(ไขกระดูก)", [("B-ALL / LBL", "bad")], 32, 44),
         ("Naive B\n(mantle zone)", [("Mantle cell", "ms")], 88, 44),
         ("Germinal center\ncentroblast ↔ centrocyte", [("Follicular", "ok"), ("DLBCL", "ms"), ("Burkitt", "bad"), ("Hodgkin", "ac")], 144, 56),
         ("Memory B\nmarginal zone", [("Marginal zone", "ok"), ("CLL/SLL", "ok")], 212, 44),
         ("Plasma cell", [("Myeloma · WM", "ok")], 268, 38),
         ("Precursor T\n(thymus)", [("T-ALL / LBL", "bad")], 344, 44),
         ("Peripheral T / NK", [("PTCL", "ms"), ("ALCL", "ms"), ("NK/T nasal", "ms"), ("Mycosis fungoides", "ok")], 400, 56)]
def pw(s_):
    return max(36, 7.2 * len(s_) + 18)
def pills_row(y, h, items):
    lines_, cur, x = [[]], 0, 210
    for s_, c in items:
        w = pw(s_)
        if x + w > 406:
            lines_.append([]); x = 210
        lines_[-1].append((x, s_, c)); x += w + 6
    ys = [y + h / 2 - 11] if len(lines_) == 1 else [y + h / 2 - 24, y + h / 2 + 2]
    return "".join(pill(x_, ys[i], s_, c, "sm b mid t" + c) for i, ln in enumerate(lines_) for x_, s_, c in ln)
LEG11 = [[("Indolent — โตเป็นปี", "ok"), ("Aggressive — สัปดาห์–เดือน", "ms")], [("Highly aggressive — วัน", "bad"), ("Hodgkin", "ac")]]
def legend11():
    out = ""
    for r, row in enumerate(LEG11):
        x = 14
        for s_, c in row:
            out += pill(x, 476 + r * 28, s_, c, "sm b mid t" + c); x += pw(s_) + 8
    return out
F11 = {"bcell": fig("Lymphoma เกิดจาก lymphocyte ระยะไหน — และโตเร็วแค่ไหน",
 "ดัดแปลงจากแผนภาพ B-cell และ T-cell development ในสไลด์ — lymphoma แต่ละชนิด **หยุดอยู่ที่ระยะการเจริญหนึ่ง** และยังมีหน้าตา/โปรตีนผิวของระยะนั้น · "
 "**Germinal center** เป็นที่ B cell จงใจตัดต่อและกลายพันธุ์ยีน antibody (somatic hypermutation · class switch) DNA จึงขาดบ่อย → เกิด translocation เช่น **t(14;18) BCL2 ใน follicular** และ **t(8;14) MYC ใน Burkitt** — lymphoma ส่วนใหญ่จึงมาจากระยะนี้ · "
 "T cell ตั้งต้นเจริญใน **thymus** (สไลด์: ผ่านการคัดเลือกเพียง ~2%) → **T-ALL/LBL มาด้วยก้อนในช่องอก** · สีบอกความเร็ว (สไลด์ Classification of lymphoma)",
 svg(420, 536, "แผนภาพระยะการเจริญของ B cell และ T cell กับชนิดของ lymphoma ที่เกิดในแต่ละระยะ แยกสีตามความเร็ว",
     t(14, 22, "B cell — ระยะการเจริญ", "sm b tac"), t(210, 22, "→ lymphoma ที่เกิด", "sm b i2"),
     *[box(14, y, 176, h, "bx", s_, fs=11.5) + ar(190, y + h / 2, 206, y + h / 2) + pills_row(y, h, it)
       for s_, it, y, h in BROWS],
     *[ar(102, BROWS[i][2] + BROWS[i][3], 102, BROWS[i + 1][2]) for i in (0, 1, 2, 3, 5)],
     line(14, 322, 406, 322, "lru da"), t(14, 338, "T / NK cell", "sm b tac"),
     legend11()))}

LYMPH = ["B2.2.4-3(3)", "B1.4.4", "B1.4.3"]
sec("hon-wbc-11", "Lymphoma — เกิดจากระยะไหน และแบ่งกลุ่มตามความเร็ว",
    "Lymphoma = มะเร็งของ lymphocyte ระยะต่าง ๆ · B-cell development germinal center · Hodgkin vs NHL · indolent aggressive highly aggressive · Burkitt · ทำไมโตช้ากลับรักษาไม่หายขาด", 10,
"""### Lymphoma คืออะไร (สไลด์)
- เนื้องอกของ **lymphocyte หรือเซลล์ตั้งต้นของ lymphocyte**
- เกิดจาก lymphoid cell **ที่ระยะการเจริญต่าง ๆ กัน**
- แสดงตัวเป็น **ก้อนของต่อมน้ำเหลือง** หรืออวัยวะที่เกี่ยวข้อง — ม้าม ตับ และเนื้อเยื่ออื่น
- ต่างจาก leukemia ที่เริ่มในไขกระดูกและเลือด — แต่บางชนิดเป็นได้ทั้งสองแบบ (CLL/SLL, lymphoblastic leukemia/lymphoma, Burkitt leukemia/lymphoma)
[[fig:bcell]]
### การแบ่งกลุ่ม (สไลด์ — WHO)
| | B cell | T/NK cell |
|---|---|---|
| **Hodgkin lymphoma** | **Classical HL** (nodular sclerosis, mixed cellularity, lymphocyte-rich, lymphocyte-depleted) · **NLPHL** | — |
| **Indolent NHL** | **follicular** · **SLL/CLL** · **marginal zone** · lymphoplasmacytic (Waldenström) | mycosis fungoides · Sézary syndrome · primary cutaneous ALCL |
| **Aggressive NHL** | **DLBCL** · follicular grade 3 และ transformed FL · **mantle cell** · primary effusion | ALCL · angioimmunoblastic · subcutaneous panniculitis-like · blastic NK · **extranodal NK/T nasal** · enteropathy-type · hepatosplenic · PTCL NOS |
| **Highly aggressive NHL** | **precursor B lymphoblastic · Burkitt** | **precursor T lymphoblastic** |

#### ทำไมถึงมีอาการนี้ — ความเร็วของการแบ่งตัวกำหนดอาการ
| | **Indolent** | **Aggressive** | **Highly aggressive** |
|---|---|---|---|
| อาการเด่น (สไลด์) | ✍️ **"ค่อยๆ โต"** ต่อมโตทั่วตัวเป็นปี · immune cytopenia · lymphocytosis · hyperviscosity | ก้อนโตในสัปดาห์–เดือน · **นอกต่อม**: ผิวหนัง เบ้าตา จมูก (ภาพในสไลด์) · ขาบวมจากหลอดเลือดดำอุดตัน | ก้อนโตเป็นวัน · **กดไขสันหลัง กดทางเดินหายใจ** · **TLS เกิดเองได้ก่อนให้ยา** |
| กลไก | เซลล์ **แบ่งตัวช้าแต่ไม่ยอมตาย** (เช่น BCL2 ใน follicular) → สะสมทีละน้อย | แบ่งตัวเร็ว | **Burkitt: MYC เปิดค้าง** → เกือบทุกเซลล์กำลังแบ่งตัว (Ki-67 เกือบ 100%) · "starry sky" = macrophage ที่กินเซลล์ที่ตาย |
| ยาเคมี | **ไม่หายขาดด้วยยาเคมีมาตรฐาน** แต่มีชีวิตได้นาน | **หายขาดได้** (เช่น R-CHOP ใน DLBCL) | หายขาดได้ถ้ารักษาเร็วด้วยยาเข้มข้น · ต้องป้องกัน TLS |
- **ทำไมโตช้ากลับรักษาไม่หาย** — ยาเคมีส่วนใหญ่ฆ่า **เซลล์ที่กำลังแบ่งตัว** · lymphoma ชนิด indolent มีเซลล์ที่แบ่งตัวอยู่น้อย จึงเหลือเซลล์ที่ "หลับ" อยู่เสมอ ส่วนชนิดที่โตเร็วเซลล์ส่วนใหญ่แบ่งตัวและไวต่อยา
- **ขาบวมใน aggressive NHL (ภาพ DVT ในสไลด์)** — ก้อนในอุ้งเชิงกรานหรือ retroperitoneum **กดหลอดเลือดดำ iliac** + มะเร็งทำให้เลือดแข็งตัวง่าย → DVT
- **Endemic (African) Burkitt** (ภาพในสไลด์) — สัมพันธ์กับ **EBV + มาลาเรีย** ก้อนที่ **ขากรรไกร** · ชนิด sporadic มักเป็นก้อนในช่องท้อง (ileocecal) · ชนิดที่สัมพันธ์กับภูมิคุ้มกันบกพร่องพบใน HIV
*(กลไกระดับยีนและเหตุผลเรื่องยาเคมี ไม่ได้อยู่ในสไลด์)*
""",
    ["Lymphoma = มะเร็งของ lymphocyte ที่หยุดอยู่ระยะหนึ่ง",
     "Germinal center = แหล่งกำเนิดของ FL Burkitt DLBCL Hodgkin",
     "Indolent ค่อย ๆ โต แต่ไม่หายขาดด้วยยาเคมี · aggressive หายขาดได้",
     "Burkitt: MYC t(8;14) แบ่งตัวเร็วที่สุด → TLS เอง",
     "T-ALL/LBL มาจาก thymus → ก้อนในช่องอก"],
    [mcq(N(25), "A 58-year-old woman has slowly enlarging, painless generalised lymphadenopathy for 3 years; biopsy shows grade 1–2 follicular lymphoma with t(14;18). Her 60-year-old neighbour has a 6-week history of a rapidly growing neck mass diagnosed as DLBCL. Why is the neighbour's lymphoma more likely to be cured with chemotherapy?",
         ["DLBCL cells lack BCL2 protein entirely", "A higher proportion of DLBCL cells are actively dividing and therefore sensitive to cytotoxic drugs",
          "Follicular lymphoma is always confined to one node", "DLBCL never involves the bone marrow", "Follicular lymphoma cells are resistant to rituximab"], 1,
         "ยาเคมีส่วนใหญ่ฆ่า **เซลล์ที่กำลังแบ่งตัว** · **DLBCL (aggressive)** มีเซลล์แบ่งตัวสูง จึง **หายขาดได้ด้วย R-CHOP** · **follicular lymphoma (indolent)** — t(14;18) ทำให้ BCL2 สูง เซลล์ **ไม่ยอมตายแต่แบ่งตัวช้า** (✍️ \"ค่อยๆโต\") จึงเหลือเซลล์ที่ไม่แบ่งตัวรอดยาเสมอ โรคจึงกลับมาแม้อยู่ได้นาน\n\n"
         "- DLBCL หลายรายมี BCL2 สูงได้\n- FL มักเป็นทั่วตัวและเข้าไขกระดูกบ่อย\n- FL ตอบสนองต่อ rituximab ดี",
         "Indolent ไม่หายขาด เพราะเซลล์ส่วนใหญ่ไม่แบ่งตัว", "Indolent vs aggressive NHL", R("Classification of lymphoma; Indolent NHL"), LYMPH),
     mcq(N(26), "A 14-year-old boy has a right lower quadrant abdominal mass that has doubled in size over 10 days. Before any treatment: K 6.1 mmol/L, phosphate 7.8 mg/dL, uric acid 14 mg/dL, creatinine rising. Biopsy shows sheets of medium-sized cells with vacuolated cytoplasm and a 'starry sky' pattern. Which genetic event drives this tumour?",
         ["t(14;18) involving BCL2", "t(11;14) involving cyclin D1", "t(8;14) involving MYC", "t(9;22) BCR::ABL1", "t(15;17) PML::RARA"], 2,
         "**Burkitt lymphoma** (very aggressive NHL ในสไลด์) — เซลล์ขนาดกลางมี vacuole · **starry sky** (macrophage กินเซลล์ที่ตายจำนวนมาก) · ก้อนแถว ileocecal ในเด็ก (sporadic)\n\n"
         "**t(8;14) ทำให้ MYC เปิดค้าง** → เกือบทุกเซลล์แบ่งตัว (Ki-67 เกือบ 100%) เซลล์เกิดและตายเร็วมากจนเกิด **tumour lysis syndrome เองก่อนให้ยา** (สไลด์: TLS occurs spontaneously or after CMT)\n\n"
         "- t(14;18) = follicular · t(11;14) = mantle cell · t(9;22) = CML · t(15;17) = APL",
         "Burkitt = MYC t(8;14) · starry sky · TLS เอง", "Burkitt lymphoma", R("Very aggressive NHL; Tumor lysis syndrome"), LYMPH + ["2.2.15"]),
    ], LYMPH, SRC + " · WHO classification", F11)

# ───────────────────────────── 12
F12 = {"bsym": fig("B symptoms — cytokine ปรับ set point ของสมอง",
 "เซลล์ Hodgkin (HRS) และเซลล์อักเสบรอบข้างหลั่ง **IL-1 IL-6 TNF-α** → เซลล์บุผนังหลอดเลือดในสมองส่วน hypothalamus สร้าง **PGE2** → **ตั้ง set point สูงขึ้น** (เส้นประ) · "
 "ช่วงที่ร่างกายยังเย็นกว่าเป้า → **หดหลอดเลือด หนาวสั่น** เพื่อสร้างความร้อน = ไข้ · เมื่อระดับ cytokine ลดลง (มักกลางดึก) set point ตกกลับ ร่างกายกลายเป็น **ร้อนเกินเป้า** → **หลอดเลือดขยาย เหงื่อท่วม** = night sweats · "
 "TNF-α และ IL-6 ยังเพิ่มการสลายกล้ามเนื้อและไขมันและทำให้เบื่ออาหาร → **น้ำหนักลด** · สามอาการนี้จึงมักมาด้วยกัน *(กลไกไม่ได้อยู่ในสไลด์)*",
 svg(420, 352, "กลไก B symptoms cytokine ทำให้ set point สูงขึ้นแล้วตกลง กราฟอุณหภูมิกับ set point ตอนหนาวสั่นและเหงื่อออก",
     box(14, 12, 186, 46, "ac", "Lymphoma\n(HRS + เซลล์รอบข้าง)", fs=12),
     ar(200, 35, 228, 35),
     box(230, 12, 176, 46, "ms", "IL-1 · IL-6 · TNF-α", fs=12.5),
     ar(330, 58, 330, 81),
     box(214, 82, 192, 46, "bad", "Hypothalamus\nPGE2 ↑ → set point ↑", fs=12),
     ar(262, 58, 140, 81),
     box(14, 82, 186, 46, "bx", "สลายกล้ามเนื้อ ไขมัน\nเบื่ออาหาร → ผอมลง", fs=11.5),
     t(14, 152, "อุณหภูมิ", "xs b i2"),
     line(50, 160, 50, 300, "ln"), line(50, 300, 404, 300, "ln"),
     t(44, 194, "39 °C", "xs end"), t(44, 294, "37 °C", "xs end"),
     path("M50 290 L120 290 L120 190 L250 190 L250 290 L404 290", "lac w2 da"),
     path("M50 293 L120 293 C150 293 155 193 186 193 L250 193 C280 193 285 293 320 293 L404 293", "lbad w3"),
     t(122, 180, "หนาวสั่น หลอดเลือดหด", "xs b tbad"),
     t(292, 226, "เหงื่อท่วม", "xs b twa"), t(292, 240, "หลอดเลือดขยาย", "xs twa"),
     t(120, 316, "หัวค่ำ", "xs mid"), t(250, 316, "กลางดึก", "xs mid"), t(370, 316, "เช้า", "xs mid"),
     line(56, 338, 82, 338, "lac w2 da"), t(88, 342, "set point ที่สมองตั้ง", "xs"),
     line(236, 338, 262, 338, "lbad w3"), t(268, 342, "อุณหภูมิร่างกาย", "xs")))}
F12["cll"] = fig("CLL/indolent B-cell lymphoma — clone เดียว ทำให้ภูมิพังสองทาง",
 "Clone ของ B cell ตัวเล็กที่ไม่ยอมตายสะสมใน **ไขกระดูก เลือด ต่อม และม้าม** · ผลที่ตามมามีสองด้านที่ดูขัดกัน: "
 "**ภูมิต่ำ** — เบียด B cell ปกติ ทำให้ **IgG ต่ำ** ติดเชื้อที่ต้องอาศัย antibody (เชื้อมีแคปซูล เช่น pneumococcus) ซ้ำ ๆ · "
 "**ภูมิทำร้ายตัวเอง** — การควบคุม T cell ผิดปกติ ทำให้ B cell ปกติที่เหลือสร้าง **autoantibody ต่อเม็ดเลือดแดงและเกล็ดเลือด** (AIHA · ITP — สไลด์ immune cytopenia) · "
 "**ซีดจากไขกระดูกถูกแทนที่ (retic ต่ำ) ต่างจากซีดจาก AIHA (retic สูง DAT บวก)** และรักษาต่างกัน *(กลไกไม่ได้อยู่ในสไลด์)*",
 svg(420, 322, "CLL clone ทำให้ไขกระดูกถูกแทนที่ IgG ต่ำ autoantibody และต่อมม้ามโต",
     box(130, 128, 160, 50, "ac", "CLL clone\nB cell เล็ก CD5+ CD23+", fs=12),
     box(14, 12, 184, 66, "ms", "ไขกระดูกถูกแทนที่\n→ ซีด เกล็ดเลือดต่ำ\n(สร้างน้อย · retic ต่ำ)", fs=11.5),
     box(222, 12, 184, 66, "wa", "เบียด B cell ปกติ\n→ IgG ต่ำ → ติดเชื้อซ้ำ\n(เชื้อมีแคปซูล)", fs=11.5),
     box(14, 226, 184, 66, "bad", "T cell คุมภูมิผิดปกติ\n→ autoantibody → AIHA · ITP\n(ถูกทำลาย · retic สูง)", fs=11.5),
     box(222, 226, 184, 66, "ac", "สะสมในต่อมและม้าม\n→ ต่อมโตทั่วตัว\nม้ามโต ไม่เจ็บ", fs=11.5),
     ar(160, 128, 122, 80), ar(260, 128, 298, 80), ar(160, 178, 122, 224), ar(260, 178, 298, 224),
     t(210, 312, "ในเลือด: monoclonal B ≥ 5,000/µL · smudge cell", "xs mid i2")))

HD = ["B2.2.4-3(3)", "2.1.1", "2.1.9", "2.1.51"]
sec("hon-wbc-12", "Hodgkin, indolent NHL และ B symptoms — อาการเฉพาะและ staging",
    "Hodgkin: ต่อมคอ คนหนุ่มสาว Reed–Sternberg B symptoms 1/3 venous/airway obstruction · ทำไมคัน ปวดต่อมหลังดื่มเหล้า · indolent NHL: ต่อมทั่วตัว immune cytopenia lymphocytosis hyperviscosity · Ann Arbor และ Lugano", 12,
"""### Hodgkin lymphoma (สไลด์)
- มักเกิดใน **ต่อมน้ำเหลือง โดยเฉพาะที่คอ** · ส่วนใหญ่ในวัย **หนุ่มสาว**
- ก้อนมี **เซลล์มะเร็งตัวใหญ่ นิวเคลียสเดียวหรือหลายนิวเคลียสกระจายอยู่จำนวนน้อย** (Hodgkin/Reed–Sternberg cell) ที่เหลือเป็นเซลล์อักเสบ
- **B symptoms ราว 1 ใน 3**
- **ภาวะฉุกเฉิน: หลอดเลือดดำอุดตัน (SVC) · ทางเดินหายใจอุดกั้น** (ก้อนในช่องอก — มักเป็น nodular sclerosis)

#### ทำไมถึงมีอาการนี้ — Hodgkin lymphoma
| อาการ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| ก้อนส่วนใหญ่เป็นเซลล์อักเสบ ไม่ใช่มะเร็ง | HRS cell (มาจาก B cell ใน germinal center) **หลั่ง cytokine/chemokine ดึง lymphocyte eosinophil plasma cell macrophage** มาล้อมตัวเอง | อธิบายอาการทั้งระบบที่เกินขนาดก้อน |
| **ไข้ เหงื่อออกกลางคืน น้ำหนักลด** | cytokine (IL-1 IL-6 TNF-α) ปรับ set point — ภาพด้านล่าง | ไข้เป็นรอบ ๆ ทุก 1–2 สัปดาห์ (Pel-Ebstein) เป็นภาพคลาสสิก |
| **คันทั้งตัว** (ไม่นับเป็น B symptom) | cytokine และสารจาก eosinophil/mast cell ที่ถูกดึงมา | คันเรื้อรังไม่มีผื่น + ต่อมโตในคนหนุ่มสาว = นึกถึง HL |
| **ปวดต่อมหลังดื่มแอลกอฮอล์** | พบน้อยแต่ค่อนข้างจำเพาะต่อ HL · **กลไกยังไม่ทราบแน่ชัด** (เชื่อว่าเกี่ยวกับหลอดเลือดในต่อมขยายตัว) | ถามทุกรายที่ต่อมโตไม่เจ็บ |
| eosinophil สูง | HRS cell สร้าง IL-5 | สไลด์: cancer เป็นสาเหตุ eosinophilia |
| หน้าบวม เส้นเลือดคอโป่ง · หายใจลำบาก ไอ | ก้อน **anterior mediastinum กด SVC และหลอดลม** | หัวข้อ 13 |
| ลามจากต่อมไปต่อมข้างเคียงทีละกลุ่ม | HL ลามตามทางเดินน้ำเหลืองต่อเนื่อง (contiguous) | staging จึงพยากรณ์ได้ดี |
*(กลไกในตารางนี้ไม่ได้อยู่ในสไลด์)*

### Indolent NHL (สไลด์) — ✍️ "ค่อยๆ โต"
**Follicular · marginal zone · CLL/SLL** — อาการที่พบบ่อย: **ต่อมโต/กดเบียด (มักทั่วตัว)** · **immune cytopenia** (AIHA · ITP — ภาพจุดเลือดและเลือดออกที่เหงือกในสไลด์) · **absolute lymphocytosis** · **hyperviscosity syndrome**
[[fig:cll]]
#### ทำไมถึงมีอาการนี้ — CLL และ indolent NHL
| อาการ | กลไก | ใช้อย่างไร |
|---|---|---|
| ต่อมโตทั่วตัว ม้ามโต ไม่เจ็บ | เซลล์อายุยืนสะสมช้า ๆ ในเนื้อเยื่อ lymphoid | ✍️ "ค่อยๆ โต" |
| **ซีดเร็ว ตาเหลือง ปัสสาวะสีเข้ม** | **AIHA** — autoantibody ต่อเม็ดเลือดแดง ถูกทำลายในม้าม | **retic สูง · DAT บวก** → steroid |
| ซีดค่อยเป็นค่อยไป เกล็ดเลือดต่ำ | ไขกระดูกถูกแทนที่ | **retic ต่ำ** → ต้องรักษาตัวโรค |
| **จุดเลือด เลือดออกที่เหงือก** | **ITP** — autoantibody ต่อเกล็ดเลือด | เกล็ดเลือดต่ำเดี่ยว ไขกระดูกมี megakaryocyte |
| **ปอดอักเสบซ้ำ ไซนัสอักเสบ** | **IgG ต่ำ** — clone เบียด B cell ปกติ | IgG ต่ำ + ติดเชื้อรุนแรงซ้ำ → IVIG |
| **ปวดหัว ตามัว เลือดกำเดา** (hyperviscosity) | **IgM** ของ lymphoplasmacytic lymphoma (Waldenström) เป็น **pentamer ขนาดใหญ่** เพิ่มความหนืดของเลือด | จอตาเส้นเลือดดำโป่ง · รักษาด้วย plasmapheresis |

### B symptoms และ Ann Arbor staging (สไลด์)
[[fig:bsym]]
**B symptoms** (หมายเหตุในตาราง Ann Arbor ของสไลด์) — มีข้อใดข้อหนึ่งให้ต่อท้ายระยะด้วย **B** ถ้าไม่มี = **A**
- **น้ำหนักลดโดยไม่ทราบสาเหตุ > 10% ใน 6 เดือน**
- **ไข้ > 38 °C**
- **เหงื่อออกกลางคืน** (drenching night sweats)
- *คันและปวดต่อมหลังดื่มเหล้า ไม่นับเป็น B symptoms*

| ระยะ (Ann Arbor — สไลด์) | นิยาม |
|---|---|
| **I** | ต่อมน้ำเหลือง **1 กลุ่ม** หรืออวัยวะนอกระบบน้ำเหลือง 1 ตำแหน่ง (IE) |
| **II** | ต่อม **≥ 2 กลุ่มด้านเดียวกันของกะบังลม** (อาจมีการลามเฉพาะที่นอกระบบน้ำเหลือง IIE) |
| **III** | ต่อม **ทั้งสองด้านของกะบังลม** (อาจมีม้าม IIIS หรือการลามเฉพาะที่ IIIE) |
| **IV** | **ลามกระจายนอกระบบน้ำเหลือง** (✍️ วงไว้) — ตับ ไขกระดูก ปอด ผิวหนัง |
- **Lugano 2014** *(ไม่ได้มาจากสไลด์)*: ใช้ PET-CT จัดระยะใน lymphoma ที่จับ FDG · ใช้ A/B เฉพาะ Hodgkin · ระบุ **bulky disease** · Hodgkin และ DLBCL ที่ทำ PET-CT แล้วไม่ต้องเจาะไขกระดูกทุกราย · ระยะ I–II = limited, III–IV = advanced
""",
    ["Hodgkin: ต่อมคอในคนหนุ่มสาว · HRS cell น้อย เซลล์อักเสบมาก",
     "B symptoms = ไข้ > 38 · เหงื่อกลางคืน · น้ำหนักลด > 10% ใน 6 เดือน",
     "คันและปวดต่อมหลังดื่มเหล้า ไม่ใช่ B symptoms แต่ชี้ไปที่ Hodgkin",
     "CLL: ซีด retic ต่ำ = ไขกระดูกถูกแทนที่ · retic สูง DAT บวก = AIHA",
     "Ann Arbor: I หนึ่งกลุ่ม · II ด้านเดียวของกะบังลม · III สองด้าน · IV นอกระบบน้ำเหลืองกระจาย"],
    [mcq(N(27), "A 23-year-old woman with biopsy-proven classical Hodgkin lymphoma reports several symptoms. Which one, by itself, qualifies her disease for the 'B' designation?",
         ["Generalised pruritus for 4 months", "Pain in the neck nodes after drinking beer", "Unexplained loss of 12% of body weight over the past 5 months",
          "Fatigue limiting her studies", "Weight loss of 6% over 6 months"], 2,
         "**B symptoms** (หมายเหตุใน Ann Arbor ของสไลด์): **น้ำหนักลดโดยไม่ทราบสาเหตุ > 10% ใน 6 เดือน** · **ไข้ > 38 °C** · **เหงื่อออกกลางคืน** — 12% ใน 5 เดือนเข้าเกณฑ์\n\n"
         "- **คัน** และ **ปวดต่อมหลังดื่มแอลกอฮอล์** พบใน Hodgkin แต่ **ไม่นับเป็น B symptoms**\n- อ่อนเพลียไม่อยู่ในเกณฑ์\n- น้ำหนักลด 6% ยังไม่ถึง 10%\n\n"
         "กลไก: IL-1 IL-6 TNF-α จาก HRS และเซลล์รอบข้าง ปรับ set point และเร่งการสลายกล้ามเนื้อ/ไขมัน",
         "B = ไข้ > 38 · เหงื่อกลางคืน · น้ำหนักลด > 10%/6 เดือน", "B symptoms", R("Ann Arbor staging; Hodgkin lymphoma"), HD),
     mcq(N(28), "A 30-year-old man with Hodgkin lymphoma has involved cervical and mediastinal lymph nodes and an involved spleen. There is no liver, lung or bone marrow involvement. What is his Ann Arbor stage?",
         ["Stage I", "Stage II", "Stage IIE", "Stage III", "Stage IV"], 3,
         "ต่อมที่คอและ mediastinum อยู่ **เหนือกะบังลม** ส่วน **ม้ามอยู่ใต้กะบังลม** และนับเป็นอวัยวะในระบบน้ำเหลือง → **ทั้งสองด้านของกะบังลม = stage III** (มีม้าม = IIIS)\n\n"
         "- stage II = ≥ 2 กลุ่ม **ด้านเดียวกัน** ของกะบังลม\n- IIE = ลามเฉพาะที่นอกระบบน้ำเหลืองด้านเดียวกัน\n- **stage IV = ลามกระจายนอกระบบน้ำเหลือง** (ตับ ไขกระดูก ปอด) ซึ่งรายนี้ไม่มี",
         "ม้ามนับเป็นระบบน้ำเหลือง · สองด้านของกะบังลม = III", "Ann Arbor staging", R("Ann Arbor staging of lymphoma"), ["B2.2.4-3(3)"]),
     mcq(N(29), "A 68-year-old man with known CLL (lymphocytes 48,000/µL) has haemoglobin that fell from 12.5 to 7.9 g/dL over 2 weeks, with jaundice and dark urine. Reticulocytes 9%, indirect bilirubin and LDH raised, haptoglobin undetectable, direct antiglobulin test positive for IgG. What is the mechanism of his anaemia?",
         ["Bone marrow replacement by CLL cells", "Autoimmune haemolysis from dysregulated immunity producing antibodies against red cells",
          "Hypersplenism alone", "Iron deficiency from occult bleeding", "Pure red cell aplasia"], 1,
         "**retic สูง + bilirubin indirect สูง + LDH สูง + haptoglobin ต่ำ + DAT บวก IgG** = **warm autoimmune haemolytic anaemia** — สไลด์: indolent NHL มี **immune cytopenia (AIHA, ITP)**\n\n"
         "กลไก: CLL ทำให้การควบคุม T cell ผิดปกติ B cell ปกติที่เหลือจึงสร้าง **autoantibody ต่อเม็ดเลือดแดง** → ถูกจับทำลายในม้าม\n\n"
         "- ไขกระดูกถูกแทนที่และ pure red cell aplasia จะมี **retic ต่ำ**\n- hypersplenism ไม่ทำให้ DAT บวก\n- ขาดเหล็กไม่ทำให้ haptoglobin หายและ DAT บวก",
         "CLL + ซีดเร็ว + retic สูง + DAT+ = AIHA (ทำลาย ไม่ใช่สร้างน้อย)", "Immune cytopenia in CLL", R("Indolent NHL; Immune cytopenia"), ["B2.2.4-3(3)", "2.3.3(4)", "B2.2.2(1)"]),
    ], HD + ["2.3.3(4)", "2.3.3(5)"], SRC + " · Lugano 2014", F12)

# ───────────────────────────── 13
def arcp(cx, cy, r, a1, a2):
    p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
    p2 = (cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2)))
    return "M%.1f %.1f A%s %s 0 0 1 %.1f %.1f" % (p1[0], p1[1], r, r, p2[0], p2[1])
SPILL = [(170, 40, "badf"), (162, 60, "msf"), (252, 36, "waf"), (258, 58, "badf"), (238, 86, "msf"), (182, 84, "waf")]
F13 = {"tls": fig("Tumour lysis syndrome — เซลล์แตกแล้วปล่อยอะไรออกมา",
 "เซลล์มะเร็งที่แบ่งตัวเร็ว (Burkitt ALL AML ที่ WBC สูง lymphoma ก้อนใหญ่) แตกพร้อมกันจำนวนมาก **เองหรือหลังยาเคมี** (สไลด์) แล้วปล่อยของในเซลล์ออกมาเกินกว่าที่ไตขับทัน: "
 "**K** (ไอออนหลักในเซลล์) → หัวใจเต้นผิดจังหวะ · **phosphate** (lymphoblast มีมากกว่าเซลล์ปกติหลายเท่า) → **จับ Ca ตกผลึกในไต** และทำให้ Ca ต่ำ · "
 "**DNA/RNA** → purine → hypoxanthine → xanthine → **uric acid** (เอนไซม์ xanthine oxidase) → **ตกผลึกในท่อไตที่เป็นกรด** · ไตวายทำให้ทุกตัวยิ่งค้าง (วงจรร้าย — เส้นประ) · "
 "✍️ จำ **\"PKCU\"** = Phosphate K Calcium Uric acid · **allopurinol ยับยั้ง xanthine oxidase** (กันกรดยูริกใหม่ ไม่ลดของเดิม) · **rasburicase** เปลี่ยน uric acid เป็น allantoin ที่ละลายน้ำ แต่ **ห้ามใน G6PD deficiency** (เกิด H2O2 → เม็ดเลือดแดงแตก) *(G6PD ไม่ได้อยู่ในสไลด์)*",
 svg(420, 438, "กลไก tumour lysis syndrome การปล่อย potassium phosphate และกรดนิวคลีอิก ไปสู่หัวใจเต้นผิดจังหวะ แคลเซียมต่ำ และไตวาย พร้อมจุดออกฤทธิ์ของ allopurinol และ rasburicase",
     circ(210, 58, 28, "bad ns"),
     path(arcp(210, 58, 30, 200, 290), "lbad w2"), path(arcp(210, 58, 30, 315, 30), "lbad w2"), path(arcp(210, 58, 30, 60, 170), "lbad w2"),
     *[circ(x, y, 3.2, c) for x, y, c in SPILL],
     t(272, 50, "เซลล์มะเร็งแตก", "sm b tbad"), t(272, 66, "เอง หรือหลังยาเคมี", "xs i2"),
     ar(186, 82, 90, 103), ar(210, 90, 210, 103), ar(234, 82, 330, 103),
     box(14, 104, 122, 30, "bad", "K สูง", fs=12.5), box(149, 104, 122, 30, "ms", "Phosphate สูง", fs=12.5),
     box(284, 104, 122, 30, "wa", "DNA/RNA → purine", fs=12),
     ar(75, 134, 75, 155), box(14, 156, 122, 56, "bad", "หัวใจเต้น\nผิดจังหวะ\nตายกะทันหัน", fs=11.5),
     ar(210, 134, 210, 155), box(149, 156, 122, 44, "ms", "จับ Ca → Ca ต่ำ\nชัก เกร็ง QT ยาว", fs=11.5),
     ar(210, 200, 210, 217), box(149, 218, 122, 44, "ms", "ผลึก Ca-phosphate\nในไตและเนื้อเยื่อ", fs=11),
     ar(345, 134, 345, 151), box(284, 152, 122, 40, "bx", "hypoxanthine\n→ xanthine", fs=11.5),
     ar(345, 192, 345, 221), t(338, 211, "allopurinol ⊣", "xs b tok end"),
     box(284, 222, 122, 30, "wa", "Uric acid สูง", fs=12.5),
     ar(345, 252, 345, 269), box(284, 270, 122, 44, "wa", "ผลึกในท่อไต\n(ปัสสาวะเป็นกรด)", fs=11),
     ar(210, 262, 210, 323), ar(330, 314, 300, 323),
     box(100, 324, 220, 42, "bad", "ไตวายเฉียบพลัน\n→ K PO4 uric ยิ่งค้าง", fs=11.5),
     path("M100 345 Q62 345 62 214", "lbad da", "ah-bad"),
     box(14, 382, 192, 46, "ok", "Allopurinol: กันกรดยูริกใหม่\nไม่ลดของที่มีอยู่", fs=11),
     box(214, 382, 192, 46, "ok", "Rasburicase: uric → allantoin\nห้ามใน G6PD deficiency", fs=11)))}
F13["svc"] = fig("SVC syndrome — เลือดดำจากหัวและแขนกลับหัวใจไม่ได้",
 "ก้อนใน **anterior mediastinum** (lymphoma มะเร็งปอด) กด **superior vena cava** → ความดันในหลอดเลือดดำ **ต้นทาง (หัว คอ แขน)** สูงขึ้น: "
 "น้ำซึมออกนอกหลอดเลือดฝอย → **หน้า คอ แขนบวม** · เลือดดำคั่ง → **หน้าแดงคล้ำ (plethora)** · เลือดหาทางอ้อม (**collateral** ผ่าน azygos และหลอดเลือดดำผนังอก — เส้นประ) ลงสู่ IVC → **เส้นเลือดดำคอและผนังอกโป่ง** (สไลด์) · "
 "อาการแย่ลงเมื่อก้มหรือนอนราบ (เลือดคั่งที่หัวมากขึ้น) · **กล่องเสียงบวม → เสียงแหบ stridor** และ **สมองบวม → ปวดหัว สับสน** เป็นสัญญาณอันตราย (สไลด์ให้ furosemide ลดความดันในกะโหลก) "
 "(อาการจากสไลด์ · ภาพกลไกวาดเพื่ออธิบาย)",
 svg(420, 372, "หลอดเลือดดำใหญ่ส่วนบน ก้อนใน mediastinum กด SVC เลือดอ้อมผ่าน collateral และอาการจากความดันหลอดเลือดดำต้นทางสูง",
     t(14, 16, "จากหัว คอ แขน", "xs b twa"),
     line(150, 24, 150, 100, "lwa w5"), line(40, 102, 150, 102, "lwa w5"), line(290, 24, 290, 100, "lwa w5"), line(400, 102, 290, 102, "lwa w5"),
     line(150, 102, 192, 132, "lwa w5"), line(290, 102, 194, 130, "lwa w5"),
     line(192, 132, 192, 158, "lwa w5"), line(194, 158, 194, 204, "lwa w2"), line(192, 204, 192, 236, "lwa w5"),
     ar(150, 34, 150, 64, "lwa", "ah-wa"), ar(290, 34, 290, 64, "lwa", "ah-wa"),
     ar(162, 64, 162, 34, "lbad w2", "ah-bad"), ar(278, 64, 278, 34, "lbad w2", "ah-bad"), t(220, 52, "ความดันย้อน ↑", "xs b mid tbad"),
     t(150, 118, "R brachiocephalic", "xs i2 end"), t(300, 118, "L brachiocephalic", "xs i2"),
     ell(242, 182, 46, 40, "ac"), t(242, 178, "ก้อนใน", "xs b mid tac"), t(242, 192, "mediastinum", "xs b mid tac"),
     t(184, 184, "SVC", "xs b end twa"),
     box(160, 236, 64, 32, "wa", "RA", fs=12.5),
     line(192, 304, 192, 270, "lwa w5"), ar(206, 300, 206, 276, "lwa", "ah-wa"), t(212, 300, "IVC", "xs b twa"),
     path("M146 108 C96 150 92 262 150 296 L186 300", "lwa w2 da", "ah-wa"),
     t(74, 210, "collateral", "xs b twa mid"), t(74, 224, "azygos ผนังอก", "xs twa mid"),
     t(14, 318, "ผลจากความดันหลอดเลือดดำต้นทางสูง", "sm b tbad"),
     box(14, 326, 94, 40, "bad", "หน้า คอ แขนบวม\nแดงคล้ำ", fs=10.5), box(113, 326, 94, 40, "bad", "เส้นเลือดดำ\nคอ อก โป่ง", fs=10.5),
     box(212, 326, 94, 40, "bad", "กล่องเสียงบวม\nเสียงแหบ stridor", fs=10.5), box(311, 326, 95, 40, "bad", "สมองบวม\nปวดหัว สับสน", fs=10.5)))

EMG = ["2.2.13", "2.2.15", "2.3.4(2)", "B7.2.3(2)"]
sec("hon-wbc-13", "ภาวะฉุกเฉินของ lymphoma — TLS และ SVC syndrome",
    "Compressive symptoms · TLS: AML WBC > 50,000 ALL > 100,000 aggressive lymphoma bulky > 10 ซม. LDH > 2 เท่า · Cairo–Bishop · allopurinol NSS rasburicase dialysis · SVC syndrome · DDx mediastinal lymphoma · steroid หลังได้ชิ้นเนื้อ", 13,
"""### ภาวะแทรกซ้อนของ very aggressive NHL (สไลด์)
- **อาการจากการกด**: **ไขสันหลังถูกกด · ทางเดินหายใจอุดกั้น**
- **Tumour lysis syndrome**: K สูง · phosphate สูง · uric acid สูง · lactic acidosis · creatinine สูงขึ้น · Ca ต่ำ

### Tumour lysis syndrome (สไลด์)
**เกิดเองหรือหลังให้ยาเคมี** · ปัจจัยเสี่ยงของโรค:
| ปัจจัยเสี่ยง (สไลด์) | |
|---|---|
| ชนิดของมะเร็ง | **AML (WBC > 50,000)** · **ALL (WBC > 100,000)** · **aggressive lymphoma** |
| ขนาด | **Bulky disease > 10 ซม.** |
| LDH | **> 2 เท่าของค่าปกติสูงสุด** |

**Cairo–Bishop** (สไลด์ — Cairo & Bishop 2004 · Coiffier 2008 · Howard 2011) ✍️ **"PKCU"**
| **Laboratory TLS** — ≥ 2 ข้อ ภายใน 3 วันก่อนถึง 7 วันหลังเริ่มรักษา | เกณฑ์ |
|---|---|
| Hyperkalemia | **K ≥ 6.0 mEq/L** หรือเพิ่ม 25% จาก baseline |
| Hyperuricemia | **uric acid ≥ 8.0 mg/dL** หรือเพิ่ม 25% |
| Hyperphosphatemia | **phosphate ≥ 4.5 mg/dL** หรือเพิ่ม 25% |
| Hypocalcemia | **Ca ≤ 7.0 mg/dL** หรือลด 25% |
- **Clinical TLS** = laboratory TLS **ร่วมกับ** อย่างน้อย 1 ข้อ: **ไตวายเฉียบพลัน** (Cr เพิ่ม 0.3 mg/dL จาก baseline · ปัสสาวะ < 0.5 mL/kg/h นาน 6 ชม. · หรือ Cr ≥ 1.5 เท่าของค่าปกติสูงสุด) · **ชัก กล้ามเนื้อกระตุก** · **หัวใจเต้นผิดจังหวะหรือเสียชีวิตกะทันหัน** — กล่องในสไลด์: \"CTLS ≥ 1 ข้อ + LTLS ≥ 2 ข้อ\"
- ผลแล็บอื่น (สไลด์): Cr สูง Ca ต่ำ P สูง **acidosis และ coagulopathy**
[[fig:tls]]
#### ทำไมถึงมีอาการนี้ — TLS
| ความผิดปกติ | กลไก | อาการ/ผลที่ตามมา |
|---|---|---|
| **K สูง** | K ส่วนใหญ่ของร่างกายอยู่ในเซลล์ — เซลล์แตกพร้อมกันปล่อยออกมาเกินที่ไตขับทัน | หัวใจเต้นผิดจังหวะ ตายกะทันหัน อ่อนแรง |
| **Phosphate สูง** | lymphoblast มี phosphate มากกว่า lymphocyte ปกติหลายเท่า | **จับ Ca ตกผลึก** ในท่อไตและเนื้อเยื่อ → ไตวาย |
| **Ca ต่ำ** | Ca ถูก phosphate จับไป | ชา เกร็ง ชัก QT ยาว · **ไม่ให้ Ca ถ้าไม่มีอาการ** — เพิ่มผลึก Ca-phosphate |
| **Uric acid สูง** | DNA/RNA → purine → hypoxanthine → xanthine → **uric acid** (xanthine oxidase) | ตกผลึกในท่อไตส่วนปลายที่เป็นกรด → ไตวายอุดตัน |
| **ไตวาย** | ผลึก + ขาดน้ำ | ทุกค่าที่ไตต้องขับยิ่งสูง (วงจรร้าย) |

### การรักษา TLS (สไลด์) และเหตุผล
| การรักษา (สไลด์) | เหตุผล |
|---|---|
| **Allopurinol 300 mg วันละ 2 ครั้ง 3 วัน → วันละครั้ง** | ยับยั้ง xanthine oxidase — **กันกรดยูริกใหม่** แต่ไม่ลดของที่มีอยู่ · เริ่มก่อนให้ยาเคมี |
| **Hydration NSS 2,000 mL/วัน** | เพิ่มปัสสาวะ ชะผลึกออก · *แนวทางปัจจุบันมักให้มากกว่านี้ (2–3 L/m²/วัน ให้ปัสสาวะออกดี) — ไม่ได้มาจากสไลด์* |
| **Rasburicase 0.15 mg/kg IV วันละครั้ง ได้ถึง 5 วัน** เมื่อมี TLS แล้ว Cr สูงขึ้น หรือ uric acid สูง | เปลี่ยน uric acid เป็น **allantoin ที่ละลายน้ำได้** → ลดลงภายในชั่วโมง · **ตรวจ G6PD ก่อน** — คนไทยพร่อง G6PD บ่อย *(ไม่ได้มาจากสไลด์)* |
| **ฟอกเลือด** เมื่อดื้อการรักษา K สูง หรือน้ำเกินในผู้ที่ปัสสาวะออกน้อย | ขับ K phosphate uric acid แทนไต |
| **Uric acid → ตัวทำนายการฟื้นจาก TLS ที่ดีที่สุด** (สไลด์) | |
- **ไม่แนะนำทำปัสสาวะเป็นด่าง** แล้ว — ช่วยละลายกรดยูริกแต่ทำให้ Ca-phosphate และ xanthine ตกผลึกมากขึ้น *(ไม่ได้มาจากสไลด์)*

### SVC syndrome (สไลด์)
- **อาการระยะแรก: หลอดเลือดดำที่คอและอกส่วนบนโป่ง · หน้าแดงคล้ำและ telangiectasia · หน้าและแขนบวมเล็กน้อย**
- **อาจคลำก้อนที่ supraclavicular ได้**
- **CXR มักเห็นความผิดปกติใน mediastinum หรือปอด** (ภาพ: mediastinum กว้าง)
[[fig:svc]]
#### ทำไมถึงมีอาการนี้ — SVC syndrome
| อาการ | กลไก |
|---|---|
| **หน้า คอ แขนบวม** | ความดันหลอดเลือดดำต้นทางสูง → ความดันในหลอดเลือดฝอยสูง น้ำซึมออก |
| **หน้าแดงคล้ำ (plethora) เขียว** | เลือดดำคั่งในผิวหนังของหัวและคอ |
| **เส้นเลือดดำคอและผนังอกโป่ง** | เลือดหาทางอ้อม (azygos internal mammary หลอดเลือดดำผนังอก) ไปลง IVC |
| แย่ลงเมื่อก้มหรือนอนราบ · ยกแขนสองข้างแล้วหน้าแดงขึ้น (Pemberton sign) | แรงโน้มถ่วงทำให้เลือดคั่งที่หัวมากขึ้น · ยกแขนยิ่งเบียดทางออกช่องอก |
| **เสียงแหบ หายใจเสียงดัง (stridor)** | กล่องเสียงและคอหอยบวม — **ทางเดินหายใจฉุกเฉิน** |
| **ปวดหัว สับสน** | สมองบวมจากเลือดดำคั่ง (สไลด์จึงให้ furosemide ลดความดันในกะโหลก) |

### DDx ของ lymphoma ใน mediastinum (สไลด์)
| Lymphoma | เพศ | อายุ | ลักษณะ |
|---|---|---|---|
| **Classical HL** | ชาย = หญิง | หนุ่มสาว | มักเป็น **nodular sclerosis** |
| **T-ALL** | **ชาย** | วัยรุ่นและผู้ใหญ่ตอนต้น (AYA) | **ไขกระดูกล้มเหลว** (ซีด ไข้ เลือดออก) |
| **DLBCL** | ชาย = หญิง | **ผู้สูงอายุ** | มักมีต่อมอื่นหรืออวัยวะนอกต่อมร่วมด้วย |
| **PMBCL** | **หญิง** | AYA | โรค **จำกัดอยู่ใน mediastinum** |

### การรักษา SVC syndrome (สไลด์)
- **Corticosteroid IV** (เช่น **dexamethasone 5 mg IV ทุก 6 ชม.**) ในรายที่สงสัย lymphoma — ✍️ **"ยุบแน่นอน" → "ต้องทำหลัง get tissue!"** — steroid ทำให้ lymphoma ยุบจนวินิจฉัยไม่ได้ จึงต้อง **ได้ชิ้นเนื้อก่อน** ยกเว้นทางเดินหายใจหรือสมองบวมคุกคามชีวิต
- **Furosemide และลดความดันในกะโหลก** · ยกหัวสูง ให้ O2
- **ปรึกษารังสีรักษา — ฉายแสงที่ mediastinum**
- *ปัจจุบัน (ไม่ได้มาจากสไลด์)*: อาการรุนแรงพิจารณา **ใส่ stent หลอดเลือดดำ** ซึ่งได้ผลเร็วและไม่รบกวนการวินิจฉัย · มะเร็งที่ไวต่อยา (lymphoma, small cell lung cancer, germ cell tumour) ให้ยาเคมีเป็นหลัก
""",
    ["TLS เสี่ยง: AML > 50,000 · ALL > 100,000 · aggressive lymphoma · bulky > 10 ซม. · LDH > 2 เท่า",
     "Cairo–Bishop: LTLS ≥ 2 ใน PKCU + CTLS (AKI ชัก arrhythmia)",
     "Allopurinol กันใหม่ · rasburicase ลดของเดิม (ตรวจ G6PD)",
     "SVC: หน้าแขนบวม แดงคล้ำ เส้นเลือดดำโป่ง · stridor/สับสน = อันตราย",
     "Steroid หลังได้ชิ้นเนื้อ — ยกเว้นคุกคามชีวิต"],
    [mcq(N(30), "A 19-year-old man with Burkitt lymphoma starts chemotherapy. On day 2: K 6.4 mmol/L, phosphate 6.8 mg/dL, Ca 6.9 mg/dL, uric acid 12.6 mg/dL, creatinine 2.1 mg/dL (baseline 0.8), urine output 0.3 mL/kg/h for 8 hours. He is already on allopurinol. Which additional drug most rapidly lowers his existing uric acid, and what must be checked?",
         ["Febuxostat; liver enzymes", "Rasburicase 0.15 mg/kg IV; G6PD status", "Sodium bicarbonate infusion; urine pH",
          "Calcium gluconate infusion; ionised calcium", "Higher-dose allopurinol; HLA-B5801"], 1,
         "รายนี้เข้า **clinical TLS** ตาม Cairo–Bishop (lab ≥ 2 ข้อ: K ≥ 6.0 · uric ≥ 8 · PO4 ≥ 4.5 · Ca ≤ 7 + **AKI**: Cr เพิ่ม > 0.3 และปัสสาวะ < 0.5 mL/kg/h นาน 6 ชม.)\n\n"
         "สไลด์: **rasburicase 0.15 mg/kg IV วันละครั้ง ได้ถึง 5 วัน** เมื่อมี TLS หรือ Cr สูงขึ้น — เปลี่ยน uric acid เป็น allantoin ที่ละลายน้ำ **ลดของที่มีอยู่ได้ในไม่กี่ชั่วโมง** · ต้อง **ตรวจ G6PD ก่อน** เพราะเกิด H2O2 ทำให้เม็ดเลือดแดงแตก/methaemoglobinaemia\n\n"
         "- febuxostat และ allopurinol **กันการสร้างใหม่** ไม่ลดของเดิม\n- ทำปัสสาวะเป็นด่างไม่แนะนำแล้ว (Ca-phosphate ตกผลึก)\n- **ไม่ให้ Ca ถ้า Ca ต่ำไม่มีอาการ** · ถ้า K สูงมี EKG เปลี่ยนจึงให้ calcium gluconate เพื่อปกป้องหัวใจ\n- K 6.4 + oliguria → เตรียมฟอกเลือด",
         "TLS ที่เป็นแล้ว → rasburicase (ตรวจ G6PD) · allopurinol แค่กันใหม่", "Tumour lysis syndrome", R("Tumor lysis syndrome"), EMG[1:] + ["B2.2.4-3(3)", "2.3.3(3)"]),
     mcq(N(31), "A 22-year-old woman has 3 weeks of facial swelling worse on bending, distended neck veins and dilated veins over the upper chest. She has no stridor, is alert, and SpO2 is 97%. CT shows a 9-cm anterior mediastinal mass and an enlarged left supraclavicular node. What is the most appropriate next step?",
         ["Start dexamethasone immediately before any tissue diagnosis", "Obtain tissue first (biopsy of the supraclavicular node), with supportive care, before giving corticosteroids",
          "Emergency mediastinal radiotherapy before biopsy", "Start empirical anti-tuberculous therapy", "Thrombolysis for presumed SVC thrombosis"], 1,
         "SVC syndrome ที่ **ไม่มีอาการคุกคามชีวิต** (ไม่มี stridor ไม่สับสน O2 ปกติ) → **ได้ชิ้นเนื้อก่อน** — ต่อม supraclavicular เข้าถึงง่าย\n\n"
         "สไลด์ให้ steroid เมื่อสงสัย lymphoma แต่ ✍️ **\"ยุบแน่นอน → ต้องทำหลัง get tissue!\"** — steroid และการฉายแสงทำให้ lymphoma ยุบและเซลล์ตายจนผลชิ้นเนื้อไม่ชัด\n\n"
         "- ให้ steroid/ฉายแสงก่อนได้ชิ้นเนื้อเฉพาะเมื่อทางเดินหายใจหรือสมองบวมคุกคามชีวิต\n- ไม่มีหลักฐานของ TB หรือลิ่มเลือดที่ต้องสลาย",
         "SVC ไม่คุกคามชีวิต → ชิ้นเนื้อก่อน steroid", "SVC syndrome", R("Superior vena cava syndrome"), ["2.2.13", "B7.2.3(2)", "B2.2.4-3(3)"]),
     mcq(N(32), "A 17-year-old boy has a large anterior mediastinal mass with SVC obstruction, together with pallor, fever and petechiae. CBC: haemoglobin 7.2 g/dL, WBC 92,000/µL with many blasts, platelets 19,000/µL. Which diagnosis best fits?",
         ["Classical Hodgkin lymphoma, nodular sclerosis", "Primary mediastinal large B-cell lymphoma", "T-cell acute lymphoblastic leukaemia/lymphoma",
          "Diffuse large B-cell lymphoma in an older adult", "Thymoma"], 2,
         "สไลด์ DDx of mediastinal lymphoma: **T-ALL — ชาย วัยรุ่น/ผู้ใหญ่ตอนต้น (AYA) — BM failure**\n\n"
         "T cell ตั้งต้นเจริญใน **thymus** จึงเป็นก้อนที่ anterior mediastinum และ blast เต็มไขกระดูกทำให้ **ซีด ไข้ เลือดออก** + blast ในเลือด\n\n"
         "- **PMBCL** = **หญิง** AYA โรคจำกัดใน mediastinum\n- **cHL** มักเป็น nodular sclerosis ไม่มี blast ในเลือด\n- **DLBCL** ในผู้สูงอายุ มีต่อม/อวัยวะอื่นร่วม\n- thymoma ไม่ทำให้มี blast",
         "ก้อน mediastinum + BM failure + blast ในชายวัยรุ่น = T-ALL", "Mediastinal lymphoma DDx", R("Differential diagnosis of mediastinal lymphoma"), ["B2.2.4-3(1)", "B2.2.4-3(3)", "2.2.13"]),
    ], EMG + ["B2.2.4-3(3)"], SRC + " · Cairo–Bishop 2004", F13)

MOCK_MAP = {"hon-wbc-03": ["MOCK-044"], "hon-wbc-06": ["MOCK-056"]}

# ───────────────────────────── MEQ / OSCE
LECNAME = "Approach to WBC disorder and lymphadenopathy (อ.เบญจมาภรณ์)"
MEQ = [{"id": "HON-WBC-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Painless cervical lymphadenopathy with B symptoms and SVC obstruction",
 "vignette": """ผู้ป่วยหญิงไทยอายุ 24 ปี นักศึกษา
CC: ก้อนที่คอซ้าย 2 เดือน และหน้าบวมตอนเช้า 2 สัปดาห์
PI: ก้อนค่อย ๆ โตขึ้น ไม่เจ็บ คันทั้งตัวโดยไม่มีผื่น 3 เดือน เหงื่อออกกลางคืนจนต้องเปลี่ยนเสื้อ มีไข้ต่ำ ๆ ตอนเย็น น้ำหนักลดจาก 52 เป็น 46 กก. ใน 3 เดือน · 2 สัปดาห์นี้ตื่นมาหน้าบวม ก้มแล้วหน้าแดงคล้ำ ไอแห้ง · ดื่มเบียร์แล้วปวดที่ก้อน
PE: BT 38.3 °C · BP 118/76 · RR 18 · SpO2 97% · ไม่มีเสียง stridor · รู้สึกตัวดี
ต่อมน้ำเหลืองคอซ้ายและเหนือไหปลาร้าซ้ายหลายต่อม ขนาด 2–4 ซม. **หยุ่นแบบยางลบ ติดกันเป็นพวง ไม่เจ็บ** · หน้าและคอบวมเล็กน้อย หลอดเลือดดำที่คอโป่ง มีหลอดเลือดดำโป่งที่ผนังอกด้านบน · ตับม้ามไม่โต
Lab: Hb 10.8 g/dL · WBC 12,400/µL (N 76% · L 10% · Eo 9% · M 5%) · Plt 420,000/µL · ESR 85 mm/h · LDH 380 U/L (ULN 250)
CXR: mediastinum กว้าง เข้าได้กับก้อนที่ anterior mediastinum""",
 "questions": [
  {"q": "1. จงบรรยายลักษณะต่อมน้ำเหลืองที่ตรวจพบ บอกว่าบ่งชี้อะไร และให้การวินิจฉัยแยกโรค 3 โรค (3 คะแนน)",
   "a": """- ต่อม **ยางลบ เป็นพวง ไม่เจ็บ** โตเรื้อรัง 2 เดือน + supraclavicular (สไลด์: ลักษณะของ **lymphoma**; supraclavicular คลำได้ = ผิดปกติเสมอ)
- DDx: **classical Hodgkin lymphoma (nodular sclerosis)** — หญิงหนุ่มสาว ต่อมคอ ก้อน mediastinum คัน eosinophil สูง ปวดต่อมหลังดื่มแอลกอฮอล์ · **primary mediastinal large B-cell lymphoma** — หญิง AYA · **tuberculous lymphadenitis** — ต่อมเป็นพวง ไข้ น้ำหนักลด (แต่มักนิ่ม/มีรู) · T-ALL ไม่เข้า (ไม่มี BM failure/blast)"""},
  {"q": "2. อาการใดของผู้ป่วยเป็น B symptoms จงอธิบายกลไกของไข้และเหงื่อออกกลางคืน (3 คะแนน)",
   "a": """- **B symptoms**: ไข้ > 38 °C · **เหงื่อออกกลางคืน** · **น้ำหนักลด 6/52 = 11.5% ใน 3 เดือน** (> 10% ใน 6 เดือน)
- **คันและปวดต่อมหลังดื่มเบียร์ไม่ใช่ B symptoms** แต่ชี้ไปที่ Hodgkin
- กลไก: HRS cell และเซลล์รอบข้างหลั่ง **IL-1 IL-6 TNF-α** → hypothalamus สร้าง **PGE2** → set point สูงขึ้น → หนาวสั่น ไข้ · เมื่อ cytokine ลด set point ตกกลับ ร่างกายร้อนเกินเป้า → **หลอดเลือดขยาย เหงื่อท่วม** · TNF/IL-6 สลายกล้ามเนื้อไขมันและเบื่ออาหาร → ผอม"""},
  {"q": "3. ภาวะเร่งด่วนของผู้ป่วยรายนี้คืออะไร ควรให้ dexamethasone ทันทีหรือไม่ และจะทำอะไรก่อน (4 คะแนน)",
   "a": """- **SVC syndrome** จากก้อน anterior mediastinum — หน้าคอบวม เส้นเลือดดำคอและผนังอกโป่ง แย่ลงเมื่อก้ม (สไลด์)
- **ยังไม่คุกคามชีวิต** (ไม่มี stridor ไม่สับสน O2 ปกติ) → **ได้ชิ้นเนื้อก่อน: excisional biopsy ต่อม supraclavicular/คอ** (ไม่ใช่ FNA) · ยกหัวสูง ให้ O2 เมื่อจำเป็น
- **ยังไม่ให้ steroid** — ✍️ "ยุบแน่นอน → ต้องทำหลัง get tissue!" lymphoma ยุบจนวินิจฉัยไม่ได้
- ถ้ามี **stridor สมองบวม (ปวดหัว สับสน)** → dexamethasone 5 mg IV ทุก 6 ชม. ± furosemide · ปรึกษารังสีรักษา/ใส่ stent ได้ทันที"""},
  {"q": "4. ผลชิ้นเนื้อเป็น classical Hodgkin lymphoma ชนิด nodular sclerosis · PET-CT พบรอยโรคที่ต่อมคอ supraclavicular และ mediastinum เท่านั้น ไม่พบใต้กะบังลม จงบอกระยะโรค (2 คะแนน)",
   "a": """- ต่อม **≥ 2 กลุ่มด้านเดียวกัน (เหนือ) ของกะบังลม** = **stage II** + B symptoms = **IIB** · ก้อน mediastinum ใหญ่ = **bulky** (Lugano 2014)
- *ไม่ได้มาจากสไลด์*: รักษาด้วยยาเคมี (เช่น ABVD หรือสูตรตามแนวทางปัจจุบัน) ± ฉายแสง มีโอกาสหายขาดสูง"""}],
 "ref": ["สไลด์ อ.เบญจมาภรณ์ — Approach (lymphadenopathy), Hodgkin lymphoma, SVC syndrome, Ann Arbor staging", "Lugano classification 2014"],
 "nl": ["2.1.57", "B2.2.4-3(3)", "2.2.13", "2.1.9"], "years": [], "_kind": "meq", "_set": SET}]

OSCE = [{"id": "HON-WBC-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "SAQ – Interpret the CBC: absolute counts, diagnosis and next step",
 "station": "SAQ (เขียนตอบ) 8 นาที",
 "instruction": """สำหรับผู้ป่วย 5 รายต่อไปนี้ จง **คำนวณ absolute count ของเซลล์ที่ผิดปกติ** · **ให้การวินิจฉัย/กลไกที่เป็นไปได้มากที่สุด** และ **บอกขั้นตอนถัดไป 1 อย่าง**

| ราย | ข้อมูล |
|---|---|
| A | ชาย 35 ปี หอบหืดกำเริบ ได้ dexamethasone IV 8 ชม.ก่อน · ไม่มีไข้ · WBC 15,800 · N 90% (ไม่มี band) · L 8% · Eo 0% |
| B | ชาย 55 ปี จุกแน่นท้องซ้าย ม้ามคลำได้ 12 ซม. · WBC 168,000 · มี myeloid ทุกระยะ · basophil 6% · Plt 620,000 |
| C | หญิง 70 ปี ไม่มีอาการ · WBC 32,000 · lymphocyte 85% ตัวเล็กหน้าตาเหมือนกันหมด · smudge cell มาก |
| D | ชาย 40 ปี ชาวนาอีสาน ผื่นคันย้ายที่ ถ่ายเหลวเป็นพัก ๆ · WBC 11,000 · eosinophil 22% · กำลังจะได้ prednisolone รักษา nephrotic syndrome |
| E | หญิง 30 ปี Graves กิน methimazole 5 สัปดาห์ · ไข้ 39 °C เจ็บคอ · WBC 1,500 · N 10% |""",
 "answer": """| ราย | Absolute count | วินิจฉัย/กลไก | ขั้นตอนถัดไป | คะแนน |
|---|---|---|---|---|
| **A** | ANC = 15,800 × 0.90 = **14,220** (> 7,700) | **Neutrophilia จาก steroid** — demargination + ดึงจาก storage pool + ออกสู่เนื้อเยื่อลดลง · ไม่มี left shift · eos หาย | **ไม่ต้องสืบค้นการติดเชื้อจาก WBC อย่างเดียว** · ตรวจซ้ำเมื่อหยุดยา | 2 |
| **B** | basophil = 168,000 × 0.06 = **10,080** (> 300) | **CML** — ม้ามโตไม่ทราบสาเหตุ ตัวอ่อนครบ basophilia เกล็ดเลือดสูง | **BCR::ABL1 (RT-PCR/FISH) หรือ Ph chromosome** → TKI · ให้น้ำ + allopurinol | 2 |
| **C** | lymphocyte = 32,000 × 0.85 = **27,200** (> 3,500) | **สงสัย CLL** — monomorphic + smudge cell | **Flow cytometry จากเลือด** (CD5 CD19 CD23 · κ หรือ λ อย่างเดียว · ≥ 5,000 monoclonal B ตาม iwCLL 2018) | 2 |
| **D** | AEC = 11,000 × 0.22 = **2,420** (moderate · hypereosinophilia > 1,500) | **Strongyloidiasis** (larva currens) | **ivermectin ก่อน steroid** (หรือ stool exam + serology) · ประเมินอวัยวะ (troponin echo) | 2 |
| **E** | ANC = 1,500 × 0.10 = **150** (< 500 = agranulocytosis) | **Drug-induced agranulocytosis** จากยาต้านไทรอยด์ + **febrile neutropenia** | **หยุดยาถาวร** เพาะเชื้อ **ยาต้านเชื้อ IV ครอบคลุม Pseudomonas ภายใน 1 ชม.** · ห้ามเปลี่ยนเป็น PTU | 2 |

**ข้อที่ทำให้เสียคะแนน**: ใช้ % แทน absolute count · ส่ง bone marrow ก่อน flow cytometry ในราย C · ให้ steroid ก่อนจัดการพยาธิในราย D · เปลี่ยนยาต้านไทรอยด์อีกตัวในราย E""",
 "ref": ["สไลด์ อ.เบญจมาภรณ์ — Leukocytosis, Mechanism of neutrophilia, Leukemoid VS Leukemia, Approach to lymphocytosis, Eosinophilia, Neutropenia, Drug-induced neutropenia", "iwCLL 2018"],
 "nl": ["3.3.1", "3.1.2", "2.3.3(2)", "B2.2.4-3(1)"], "years": [], "_kind": "meq", "_set": SET}]

LECTURE = {
 "lec": LEC, "date": "จ. 12 ต.ค.",
 "title": "Approach to WBC disorder and lymphadenopathy",
 "subtitle": "absolute count · neutrophil 5 คลัง · leukemoid vs CML · monocytosis lymphocytosis และ smear · eosinophilia · neutropenia · acute leukemia และ hyperleukocytosis · approach to lymphadenopathy · lymphoma · TLS และ SVC syndrome — พร้อมกลไกของอาการและภาพ",
 "objectives": [
   "คำนวณ absolute count และใช้เกณฑ์ leukocytosis/leukopenia ของเม็ดเลือดขาวแต่ละชนิด",
   "อธิบายกลไก neutrophilia ด้วยแผนภาพ 5 คลัง และแยกสาเหตุจากความเร็วและลักษณะใน smear",
   "แยก leukemoid reaction กับ CML และอธิบายอาการของ CML จาก BCR::ABL1",
   "ประเมิน monocytosis และ lymphocytosis ตามสามขั้น: สาเหตุ reactive → smear → flow cytometry",
   "หาสาเหตุของ eosinophilia รู้จัก HES และระวัง Strongyloides ก่อนให้ steroid",
   "จำแนก neutropenia ตามความรุนแรงและกลไก และจัดการ drug-induced agranulocytosis",
   "อธิบายอาการของ acute leukemia จาก marrow failure และการแทรกอวัยวะ รวมถึง APL",
   "วินิจฉัยและจัดการ hyperleukocytosis/leukostasis",
   "ซักประวัติ ตรวจ และตัดสินใจ biopsy ในผู้ป่วยต่อมน้ำเหลืองโต โดยใช้ลักษณะและตำแหน่งของต่อม",
   "จำแนก lymphoma ตามระยะการเจริญและความเร็ว อธิบาย B symptoms และจัดระยะ Ann Arbor",
   "วินิจฉัยและจัดการ tumour lysis syndrome และ SVC syndrome"],
 "nlGap": "เกณฑ์ฯ มีรหัส CBC/blood smear (`นล. 3.3.1` `3.1.2` `B2.3(2)`) · การสร้างเม็ดเลือดขาว (`B2.1.2(3)`) · agranulocytosis/febrile neutropenia (`2.3.3(2)`) · leukemias MPN lymphomas (`B2.2.4-3(1)–(3)`) · ต่อมน้ำเหลืองโต (`2.1.57`) · lymphadenitis (`2.3.3(6)`) · SVC obstruction (`2.2.13`) แต่ **ไม่มีรหัสของ leukemoid reaction, eosinophilia/HES, hyperleukocytosis/leukostasis, tumour lysis syndrome (มีแค่รหัสเกลือแร่) และ staging ของ lymphoma** จึงอ้างแนวทางด้านล่าง · สไลด์ไม่มีอาการทางคลินิกของ acute leukemia/APL การรักษา CML เกณฑ์ iwCLL และเกณฑ์ตัดต่อมน้ำเหลือง — **หัวข้อ 7 เติมเกือบทั้งหมด** ส่วนที่เติมในหัวข้ออื่นระบุไว้ทุกจุด · ตาราง \"ทำไมถึงมีอาการนี้\" และภาพประกอบทั้ง 17 ภาพเขียนเพิ่มตามที่ผู้ใช้ขอ (กลไกส่วนใหญ่มาจากตำรา)",
 "guidelines": [
   "**WHO Classification of Haematolymphoid Tumours, 5th edition (WHO-HAEM5, 2022)** และ **International Consensus Classification (ICC 2022)** — นิยาม acute leukemia, ระยะของ CML, การแบ่งชนิด lymphoma",
   "**ELN 2022 recommendations for AML** (Döhner, Blood 2022) — การแบ่งความเสี่ยงทางพันธุกรรม",
   "**ELN 2020 recommendations for CML** (Hochhaus, Leukemia 2020) — TKI และเป้าหมาย BCR::ABL1 ที่ 3, 6, 12 เดือน",
   "**iwCLL 2018 guidelines** (Hallek, Blood 2018) — monoclonal B lymphocyte ≥ 5,000/µL",
   "**Lugano classification 2014** (Cheson, J Clin Oncol 2014) — PET-CT staging และ excisional biopsy",
   "**Cairo–Bishop definition of TLS (2004)** (อยู่ในสไลด์) และ **BCSH/BSH guideline on tumour lysis syndrome (2015)**",
   "**Klion AD. How I treat hypereosinophilia (Blood 2015)** (อยู่ในสไลด์) และ **ICOG-EO consensus criteria (Valent, J Allergy Clin Immunol 2012)**",
   "**IDSA febrile neutropenia guideline (Freifeld 2010)** และ **ASCO/IDSA outpatient fever and neutropenia (2018)**",
   "**Gaddey HL, Riegel AM. Unexplained lymphadenopathy: evaluation and differential diagnosis (Am Fam Physician 2016)**",
   "**Williams Hematology 8th ed.** · **Andersohn F. Ann Intern Med 2007** · **Boxer LA, ASH 2012** (อ้างในสไลด์)"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# กระจายตำแหน่งคำตอบของข้อใหม่ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น) · ข้อที่ตัวเลือกเรียงตามธรรมชาติไม่สลับ
ORDERED = {N(28)}  # ระยะ I–IV เรียงตามธรรมชาติ
_slot = 0
for s_ in S:
    for it in s_["items"]:
        if it["id"] in ORDERED:
            continue
        tgt = [1, 4, 0, 3, 2][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

for s_ in S:
    assert "```" not in s_["md"], s_["id"]
path = os.path.join(BUILD, "data", SET + ".json")
data = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
data = [l for l in data if l.get("lec") != LEC] + [LECTURE]
data.sort(key=lambda l: tuple(int(x) for x in l["lec"].split("/")[::-1]))  # เรียงตามวันที่ d/m
seen = set()
for l in data:
    for x in [i for s_ in l["sections"] for i in s_["items"]] + l["meq"] + l["osce"] + [{"id": s_["id"]} for s_ in l["sections"]]:
        assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
        seen.add(x["id"])
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

added = link_mock(SET, LEC, MOCK_MAP)

d = json.load(open(path, encoding="utf-8"))
L = [l for l in d if l["lec"] == LEC][0]
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = ({c for s_ in L["sections"] for c in s_["nl"]} | {c for s_ in L["sections"] for i in s_["items"] for c in i.get("nl", [])}
         | {c for m in L["meq"] + L["osce"] for c in m["nl"]})
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == SET: m["lectureCount"] = len(d)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print("sections %d | ข้อใหม่ %d + mock %d | meq %d | osce %d | figs %d | nl %d" % (
    len(S), sum(1 for s_ in S for i in s_["items"] if i["kind"] == "mcq"), added, len(MEQ), len(OSCE),
    sum(len(s_.get("figs") or {}) for s_ in S), len(codes)))
print("answer positions:", dict(sorted(Counter(i["answer"] for s_ in S for i in s_["items"] if i["kind"] == "mcq").items())))
print("%s.json มี %d คาบ: %s" % (SET, len(d), [l["lec"] for l in d]))
