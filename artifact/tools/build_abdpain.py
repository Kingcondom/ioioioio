#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Approach to abdominal pain (นพ.กิตติ ชื่นยง) → data/gi.json
ต้นฉบับ: Drive 10g5J-s6Zv5JZB3RbHs6dh2QWUR5Xzr5V · บรรยาย อ. 27 ต.ค. 2569 · โน้ต slides/abdpain_notes.md
ผูกข้อ Mock หมวด GI (M09) ที่ตรงเรื่อง · อัปเดต: ACG 2024 acute pancreatitis · Tokyo Guidelines 2018 ·
ACG/CAG 2017 dyspepsia · Maastricht VI 2022 (H. pylori) · Rome IV"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_mock import link_mock

SET, LEC = "gi", "27/10"
NLN = ["2.1.11"]
SRC = "สไลด์ นพ.กิตติ — Approach to the abdominal pain"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None, src=SRC):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": src,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "GI-ABD-MCQ-%02d" % n
R = lambda p: ["สไลด์ นพ.กิตติ — " + p]

# ───────────────────────────── 1
sec("gi-abd-01", "ปวดท้องสองแบบ: visceral กับ parietal",
    "Visceral = C fiber ตื้อ บอกตำแหน่งไม่ได้ อยู่กลางตัว · Parietal = A-δ แหลม ชี้จุดได้ ขยับแล้วปวด · foregut midgut hindgut", 8,
"""### สองระบบประสาทของความปวดในท้อง
| | **Visceral pain** | **Parietal (somatic) pain** |
|---|---|---|
| เส้นประสาท | **C fiber ไม่มีปลอกไมอีลิน** | **A-δ fiber** |
| ลักษณะ | **ตื้อ บิด แสบร้อน** | **แหลม เกิดทันที** |
| ตำแหน่ง | **บอกไม่ชัด** — ปลายประสาทน้อยและมาจากหลายปล้อง · **ไม่เอียงซ้ายขวา** เพราะส่งสัญญาณขึ้นสองข้าง | **ชี้จุดได้** |
| ปัจจัย | — | **แย่ลงเมื่อขยับหรือสั่นสะเทือน** |
| เกิดจาก | ผนังอวัยวะตึง บีบตัวแรง ขาดเลือด | **เยื่อบุช่องท้องชั้นนอก (parietal peritoneum) ถูกกระตุ้น** |

### ตำแหน่งตามการเจริญของลำไส้ในตัวอ่อน
| ส่วน | อวัยวะ | ปวดที่ |
|---|---|---|
| **Foregut** | กระเพาะ ลำไส้เล็กส่วนต้น ตับอ่อน ตับ ทางเดินน้ำดี | **ใต้ลิ้นปี่ (epigastrium)** |
| **Midgut** | jejunum ileum ไส้ติ่ง ลำไส้ใหญ่ครึ่งต้น | **รอบสะดือ** |
| **Hindgut** | ลำไส้ใหญ่ครึ่งปลาย อวัยวะในอุ้งเชิงกรานและทางเดินปัสสาวะ | **ท้องน้อย (hypogastrium)** |

- **กระเพาะและลำไส้เล็กส่วนต้น** ส่งผ่าน **celiac ganglion** → **ปวดใต้ลิ้นปี่เกือบเสมอ**
- **ลำไส้ใหญ่** — ส่วนขึ้นผ่าน sympathetic T10–L2 · ส่วนลงผ่าน parasympathetic S2–S4 → **ปวดได้ทุกตำแหน่ง แม้ท้องส่วนบน** จนเลียนแบบ dyspepsia ได้

**ตัวอย่างที่เห็นทั้งสองระบบ** — **ไส้ติ่งอักเสบ** เริ่มปวดตื้อรอบสะดือ (visceral ของ midgut) แล้วย้ายมาปวดแหลมที่ท้องขวาล่าง (parietal เมื่อการอักเสบลามถึงเยื่อบุช่องท้อง)
""",
    ["Visceral: C fiber · ตื้อ · บอกตำแหน่งไม่ได้ · อยู่กลางตัว",
     "Parietal: A-δ · แหลม · ชี้จุดได้ · ขยับแล้วปวด",
     "Foregut → ใต้ลิ้นปี่ · midgut → รอบสะดือ · hindgut → ท้องน้อย",
     "ปวดจากลำไส้ใหญ่อยู่ได้ทุกตำแหน่ง",
     "ไส้ติ่ง: รอบสะดือ (visceral) → ขวาล่าง (parietal)"],
    [mcq(N(1), "Why does early appendicitis cause dull periumbilical pain before the pain localises to the right lower quadrant?",
         ["The appendix is a foregut structure", "Early pain is visceral from a midgut organ, felt in the periumbilical region; later inflammation irritates the parietal peritoneum, producing localised sharp pain",
          "The appendix is innervated by A-delta fibres only", "Periumbilical pain is referred from the diaphragm", "The caecum is supplied by S2–S4 parasympathetic fibres"], 1,
         "ไส้ติ่งเป็นอวัยวะ **midgut** — ช่วงแรกผนังตึงและอักเสบส่งสัญญาณผ่าน **C fiber (visceral)** ซึ่งบอกตำแหน่งไม่ได้และรับรู้เป็น **ปวดตื้อรอบสะดือ**\n\nเมื่อการอักเสบลามถึง **parietal peritoneum** สัญญาณผ่าน **A-δ fiber** → ปวดแหลม **ชี้จุดได้ที่ขวาล่าง** และแย่ลงเมื่อขยับ",
         "ไส้ติ่ง: visceral รอบสะดือ → parietal ขวาล่าง", "Visceral vs parietal pain", R("Visceral pain of GI tract"), NLN + ["2.3.11-3(1)"]),
    ])

# ───────────────────────────── 2
sec("gi-abd-02", "ซักประวัติและตรวจร่างกายผู้ป่วยปวดท้อง",
    "ให้ชี้ด้วยนิ้ว · เวลา ลักษณะ ปัจจัย · ปวดร้าว · ท่าทาง · guarding rebound percussion tenderness · Murphy · bruit · ก้อนเต้น", 9,
"""### สามแบบของความปวด (สไลด์)
| | **Visceral — อวัยวะกลวง** | **Visceral — อวัยวะตัน** | **Somato-parietal** |
|---|---|---|---|
| ลักษณะ | **บิดเป็นพัก (colicky)** ตื้อ | ตื้อ | **แหลม** |
| ตำแหน่ง | กลางตัว (หรือเอียงข้าง) | เอียงข้าง | แล้วแต่จุด |
| ตัวอย่าง | กระเพาะ ลำไส้ | ตับ ตับอ่อน | เยื่อบุช่องท้อง |
| สิ่งกระตุ้น | ผนังตึง บีบตัวแรง ขาดเลือด | **แคปซูลตึง** | สารเคมี การติดเชื้อ |
| **ท่าทาง** | **กระสับกระส่าย** หาท่ากดท้อง | ค่อนข้างนิ่ง | **นอนนิ่ง ไม่กล้าขยับ** |
| อาการแสดง | **เสียงลำไส้ดัง** | กดแล้วอึดอัด | **rebound tenderness · เคาะเจ็บ** |

### ข้อมูลที่ต้องได้
- **ตำแหน่ง** — **ให้ชี้ด้วยนิ้ว ไม่ใช่ทั้งฝ่ามือ** · จุดเริ่มและบริเวณที่ปวด
- **เวลา** — เริ่มอย่างไร นานเท่าไร เปลี่ยนแปลงตามเวลาอย่างไร
- **ลักษณะและความแรง** · **อะไรทำให้ดีขึ้นหรือแย่ลง**
- **ปวดร้าว** — กะบังลมถูกระคาย → **ไหล่** · ทางเดินน้ำดี → **สะบักข้างเดียวกัน**
- **ลำดับเหตุการณ์** — ไส้ติ่ง: รอบสะดือ → ขวาล่าง · **biliary colic ปวดคงที่ นานกว่า 1 ชม.** (ไม่ใช่บิดเป็นพัก) · ลำไส้เล็กอุดตัน: บิดเป็นพัก → คงที่เมื่อท้องอืด → ปวดแบบ parietal เมื่อขาดเลือดหรือทะลุ

### ตรวจร่างกาย
**ดู ฟัง เคาะ**
- ผิวหนัง: **งูสวัด** (ปวดก่อนผื่นขึ้น) · **Cullen (รอบสะดือ) และ Grey Turner (สีข้าง)** ในตับอ่อนอักเสบรุนแรง
- เสียงลำไส้ · **succussion splash** (กระเพาะอุดตัน)
- ท้องโต: **ลม vs น้ำ**
- **Bruit** — aorta, mesenteric หรือ renal artery ตีบ
- **เคาะแล้วเจ็บ = เยื่อบุช่องท้องอักเสบ** และช่วยหาจุดที่เจ็บที่สุด
**คลำ**
- **Guarding** — ตั้งใจเกร็ง (voluntary) vs **เกร็งเอง (involuntary) = peritonitis**
- ตับม้ามโต · ก้อน (คลำลึก) · **ก้อนที่เต้นตามชีพจร = abdominal aortic aneurysm**
- **Rebound tenderness** — peritonitis เฉพาะที่หรือทั่วท้อง
- ระบุอวัยวะ: ตับ ลำไส้ใหญ่ ตับอ่อน ม้าม **ถุงน้ำดี (Murphy sign)**
- ประเมิน **SIRS** และสัญญาณชีพเสมอ
""",
    ["Colicky + กระสับกระส่าย = อวัยวะกลวง · นอนนิ่ง + rebound = parietal/peritonitis",
     "ชี้ด้วยนิ้ว · ปวดร้าวไหล่ = กะบังลม · ร้าวสะบักขวา = ทางเดินน้ำดี",
     "Biliary colic ปวดคงที่ > 1 ชม. ไม่ใช่บิดเป็นพัก",
     "Involuntary guarding + เคาะเจ็บ = peritonitis",
     "ก้อนเต้นตามชีพจร = AAA · Cullen/Grey Turner = ตับอ่อนอักเสบรุนแรง"],
    [mcq(N(2), "A patient with severe abdominal pain lies completely still, and pain worsens when the bed is bumped. Percussion over the abdomen is painful. Which type of pain is this?",
         ["Visceral pain from a hollow viscus", "Somato-parietal pain from peritoneal irritation", "Visceral pain from capsular stretch of a solid organ", "Functional pain", "Referred pain from the diaphragm"], 1,
         "ตารางในสไลด์: **somato-parietal pain** — **แหลม · นอนนิ่ง · แย่ลงเมื่อขยับหรือสั่นสะเทือน · rebound และเคาะเจ็บ** = เยื่อบุช่องท้องถูกระคาย (peritonitis)\n\nตรงข้ามกับ **ปวดจากอวัยวะกลวง** ที่ผู้ป่วย **กระสับกระส่าย** หาท่ากดท้อง และฟังได้เสียงลำไส้ดัง",
         "นอนนิ่ง + ขยับแล้วปวด + เคาะเจ็บ = peritonitis", "Type of abdominal pain", R("Type of abdominal pain")),
    ])

# ───────────────────────────── 3
sec("gi-abd-03", "ปวดตามอวัยวะ — กลางตัวหรือเอียงข้าง",
    "อวัยวะกลวงปวดกลางตัว (ยกเว้นลำไส้ใหญ่) · อวัยวะตันปวดเอียงข้าง · ตำแหน่งอย่างเดียวไม่พอ ต้องดูอาการร่วม", 7,
"""### ปวดตามอวัยวะ (สไลด์)
| อวัยวะ | ปวดอย่างไร |
|---|---|
| **กระเพาะ–ลำไส้เล็กส่วนต้น** | **dyspepsia** ใต้ลิ้นปี่ |
| **ทางเดินน้ำดี** | ใต้ลิ้นปี่หรือชายโครงขวา |
| **ตับอ่อน** | **ปวดลึกกลางท้องส่วนบน ร้าวไปหลัง** |
| **ตับ** | ชายโครงขวาถึงใต้ลิ้นปี่ อึดอัดคงที่ (แคปซูล Glisson ตึง) |
| **ม้าม** | ชายโครงซ้าย |
| **ลำไส้เล็ก** | **รอบสะดือ บิดเป็นพัก** |
| **ลำไส้ใหญ่** | **ได้ทุกตำแหน่ง** |
| อวัยวะในอุ้งเชิงกราน | ท้องน้อย |

### กลางตัว vs เอียงข้าง
| **กลางตัว** | | **เอียงข้าง** | |
|---|---|---|---|
| ใต้ลิ้นปี่ | dyspepsia · biliary colic · visceral pain ของตับอ่อน ตับ ทางเดินน้ำดี ม้าม | ท้องส่วนบน | ตับ ตับอ่อน ถุงน้ำดีอักเสบ · อวัยวะโต/ก้อน · ลำไส้ใหญ่ |
| รอบสะดือ | **ลำไส้เล็ก** — อุดตัน อักเสบ IBS | สีข้าง | ลำไส้ใหญ่ · เยื่อบุช่องท้อง · **ไตและท่อไต** (กรวยไตอักเสบ มะเร็ง นิ่ว) |
| ท้องน้อย | ลำไส้ใหญ่ (อักเสบ vs IBS) · **อวัยวะสืบพันธุ์สตรี** · กระเพาะปัสสาวะ | ท้องล่างข้างใดข้างหนึ่ง | **ไส้ติ่ง** · ลำไส้ใหญ่ · IBS · **รังไข่** |

**Take home ของอาจารย์**
- **ปวดจากอวัยวะกลวงอยู่กลางตัว ยกเว้นลำไส้ใหญ่** · **อวัยวะตันส่วนใหญ่ปวดเอียงข้าง**
- **ตำแหน่งอย่างเดียวไม่พอให้วินิจฉัย ต้องดูอาการร่วมด้วยเสมอ**
""",
    ["ตับอ่อน: ปวดลึกกลางท้องบนร้าวไปหลัง",
     "ลำไส้เล็ก: รอบสะดือ บิดเป็นพัก · ลำไส้ใหญ่: ได้ทุกที่",
     "อวัยวะกลวงปวดกลางตัว (ยกเว้น colon) · อวัยวะตันเอียงข้าง",
     "ตำแหน่งไม่พอ ต้องดูอาการร่วม"],
    [mcq(N(3), "A 35-year-old woman has recurrent upper and left-sided abdominal pain for months, unrelated to meals, with alternating constipation and diarrhoea and relief after defecation. Which organ is the most likely source?",
         ["Stomach", "Pancreas", "Colon", "Gallbladder", "Spleen"], 2,
         "เคสเปิดของอาจารย์: **ปวดเป็น ๆ หาย ๆ ไม่สัมพันธ์กับอาหาร ท้องผูกสลับท้องเสีย ดีขึ้นหลังถ่าย** = **colonic pain** — แม้ปวดที่ท้องส่วนบนก็ตาม เพราะ **ปวดจากลำไส้ใหญ่อยู่ได้ทุกตำแหน่ง**\n\ndyspepsia (กระเพาะ) สัมพันธ์กับอาหาร อยู่กลางใต้ลิ้นปี่ และมีอิ่มเร็ว แน่นหลังอาหาร",
         "ปวดสัมพันธ์การถ่าย + เปลี่ยนนิสัยการถ่าย = ลำไส้ใหญ่ แม้ปวดท้องบน", "Colonic pain location", R("What is your diagnosis?")),
    ])

# ───────────────────────────── 4
sec("gi-abd-04", "ปวดจากลำไส้ใหญ่ และ IBS (Rome IV)",
    "ปวดสัมพันธ์การถ่าย · เปลี่ยนความถี่/ลักษณะอุจจาระ · Rome IV ≥ 1 วัน/สัปดาห์ 3 เดือน · alarm features ต้องส่องกล้อง", 9,
"""### ลักษณะปวดจากลำไส้ใหญ่ (สไลด์)
- **บิดเป็นพัก อยู่ได้หลายตำแหน่ง**
- **ความถี่และลักษณะอุจจาระเปลี่ยน**
- **ดีขึ้นหลังถ่าย**
- ปวดเบ่ง (tenesmus) · ถ่ายไม่สุด · ท้องอืดทั่วท้อง

**สาเหตุทางกาย (organic)** — ลำไส้อักเสบจากการติดเชื้อ · **มะเร็งลำไส้ใหญ่** · **ulcerative colitis** · **วัณโรคลำไส้** · พยาธิ · **ischemic colitis**
| | Ulcerative colitis | Crohn's disease |
|---|---|---|
| รอยโรค | **ต่อเนื่องจากทวารหนักขึ้นไป** เฉพาะเยื่อบุ | **เป็นหย่อม (skip) ทะลุทุกชั้น** · terminal ileum บ่อย |
| อาการเด่น | **ถ่ายเป็นเลือด** | ปวดท้องขวาล่าง ท้องเสียไม่เป็นเลือด น้ำหนักลด fistula |

### เกณฑ์ IBS — Rome IV
**ปวดท้องซ้ำ ๆ อย่างน้อย 1 วัน/สัปดาห์ ในช่วง 3 เดือน** ร่วมกับ **≥ 2 ข้อ**
1. **สัมพันธ์กับการถ่าย**
2. **ความถี่ของการถ่ายเปลี่ยน**
3. **ลักษณะอุจจาระเปลี่ยน**
อาการเริ่ม **≥ 6 เดือน** ก่อนวินิจฉัย
| ชนิด | ลักษณะอุจจาระ |
|---|---|
| **IBS-C** | แข็ง/เป็นก้อน > 25% · เหลว < 25% |
| **IBS-D** | เหลว > 25% · แข็ง < 25% |
| **IBS-M** | ทั้งแข็งและเหลว > 25% |
| IBS-U | ไม่เข้าชนิดใด |

### Alarm features — ต้องหาโรคทางกาย
- **อาการตอนกลางคืน** (ตื่นเพราะปวดหรือต้องถ่าย)
- **ถ่ายเป็นเลือด** (แยกจากริดสีดวง) หรือเลือดแฝง
- **เริ่มเป็นหลังอายุ 50 ปี**
- **น้ำหนักลด** · **ประวัติครอบครัวมะเร็งลำไส้ใหญ่** · **ไข้** · **ซีด**

### ในเวชปฏิบัติ (สไลด์)
วินิจฉัย IBS = **เข้าเกณฑ์ Rome + ตัดโรคทางกาย** — **ส่องกล้องลำไส้ใหญ่** · คนอายุน้อยไม่มี alarm อาจใช้ **ตรวจเลือดแฝงในอุจจาระ × 3** · ไม่มีกล้อง → CT/barium enema
""",
    ["Colonic pain: ดีขึ้นหลังถ่าย · ความถี่/ลักษณะอุจจาระเปลี่ยน · tenesmus",
     "Rome IV IBS: ปวด ≥ 1 วัน/สัปดาห์ 3 เดือน + ≥ 2 (การถ่าย ความถี่ ลักษณะ) · เริ่ม ≥ 6 เดือน",
     "IBS alarm: กลางคืน · เลือดออก · > 50 ปี · น้ำหนักลด · FHx CRC · ไข้ · ซีด",
     "UC ต่อเนื่องจากทวาร ถ่ายเป็นเลือด · Crohn skip transmural terminal ileum"],
    [mcq(N(4), "A 56-year-old man has 4 months of lower abdominal cramping relieved by defecation and a change to looser stools. He has lost 5 kg and Hb is 10.2 g/dL. What is the next step?",
         ["Diagnose IBS-D and start loperamide", "Colonoscopy", "Reassurance and a high-fibre diet", "Trial of antispasmodics for 3 months", "Stool culture only"], 1,
         "แม้อาการเข้ากับ IBS แต่มี **alarm features หลายข้อ — เริ่มหลังอายุ 50 · น้ำหนักลด · ซีด** → ต้อง **ส่องกล้องลำไส้ใหญ่** หา **มะเร็งลำไส้ใหญ่** และโรคทางกายอื่นก่อน\n\nRome IV ยังต้องมีอาการ **เริ่ม ≥ 6 เดือน** ก่อนวินิจฉัย (รายนี้เพียง 4 เดือน) · IBS เป็นการวินิจฉัยหลังตัดโรคทางกายแล้วเสมอ",
         "IBS-like + alarm (> 50, น้ำหนักลด, ซีด) → colonoscopy", "IBS alarm features", R("Alarm symptoms of IBS"), NLN + ["2.3.11(6)", "B8.2.5(2)"]),
    ], NLN + ["2.3.11(6)", "B8.2.5(2)"])

# ───────────────────────────── 5
DYS = NLN + ["2.3.11(10)", "2.3.11(6)"]
sec("gi-abd-05", "Dyspepsia — ปวดจากกระเพาะและลำไส้เล็กส่วนต้น",
    "ปวดใต้ลิ้นปี่ + อิ่มเร็ว แน่นหลังอาหาร คลื่นไส้ เรอ · organic vs functional (Rome IV) · alarm 4 ข้อ · โรคที่เลียนแบบ", 9,
"""### นิยาม (สไลด์)
**Dyspepsia = อาการจากรอยโรคของกระเพาะและลำไส้เล็กส่วนต้น** — **ปวดหรือแสบใต้ลิ้นปี่** ร่วมกับ
- **อิ่มเร็ว (early satiation)** · **แน่นหลังอาหาร (postprandial fullness)**
- คลื่นไส้ อาเจียน · ท้องอืดส่วนบน · เรอ
**ปวดอยู่กลางตัว ไม่ออกนอกแนวกลาง** — ถ้าอาการร่วมไม่ชัดหรือปวดเอียงข้าง ให้นึกถึงโรคที่เลียนแบบ

### Uninvestigated dyspepsia — ยังไม่ได้ส่องกล้อง
| **Organic** | **Functional dyspepsia** |
|---|---|
| **แผลลำไส้เล็กส่วนต้น (DU)** · **แผลกระเพาะ (GU)** · กระเพาะอักเสบ · **มะเร็งกระเพาะ** · lymphoma | ส่องกล้องแล้ว **ไม่พบรอยโรคทางโครงสร้าง** — พบบ่อยที่สุด |

### Rome IV — Functional dyspepsia
**≥ 1 อาการที่รบกวน**: แน่นหลังอาหาร · อิ่มเร็ว · ปวดใต้ลิ้นปี่ · แสบใต้ลิ้นปี่
**และ** ไม่พบโรคทางโครงสร้าง (**รวมการส่องกล้องกระเพาะ**) · อาการ 3 เดือนล่าสุด เริ่ม ≥ 6 เดือน
- **Postprandial distress syndrome** — แน่นหลังอาหาร อิ่มเร็ว
- **Epigastric pain syndrome** — ปวด/แสบใต้ลิ้นปี่

### Alarm features (สมาคมแพทย์ระบบทางเดินอาหารแห่งประเทศไทย)
1. **กลืนลำบาก**
2. **เลือดออกทางเดินอาหาร หรือ ซีดจากขาดธาตุเหล็ก**
3. **น้ำหนักลดโดยไม่ทราบสาเหตุ**
4. **อาเจียนต่อเนื่อง**

### โรคที่เลียนแบบ dyspepsia
| โรค | จุดแยก |
|---|---|
| **Gastroparesis** | อิ่มเร็ว อาเจียนอาหารที่กินไปนาน · เบาหวาน |
| **IBS / ปวดจากลำไส้ใหญ่** | สัมพันธ์การถ่าย ไม่สัมพันธ์มื้ออาหาร |
| **Biliary colic** | **หลังอาหาร ไม่เคยปวดก่อนอาหาร** · ปวดคงที่ > 1 ชม. · เป็นครั้งคราว |
| **Sphincter of Oddi dysfunction** | ชายโครงขวา/ใต้ลิ้นปี่ **ไม่มีไข้ ไม่เหลือง** · AST ALT amylase สูงช่วงปวด |
| **ตับอ่อนอักเสบเรื้อรัง** | ปวดขึ้นลง **ถ่ายเป็นไขมัน เบาหวาน** |
| **มะเร็งอวัยวะตัน** | ตับกลีบซ้าย ตับอ่อน |
""",
    ["Dyspepsia = กระเพาะ–ลำไส้เล็กส่วนต้น · ปวดกลางใต้ลิ้นปี่ + อิ่มเร็ว แน่นหลังอาหาร",
     "Rome IV FD ต้องส่องกล้องแล้วปกติ · 3 เดือน เริ่ม ≥ 6 เดือน",
     "Alarm ไทย: กลืนลำบาก · เลือดออก/IDA · น้ำหนักลด · อาเจียนต่อเนื่อง",
     "Biliary colic ปวดหลังอาหาร ไม่ปวดก่อนอาหาร"],
    [mcq(N(5), "A 55-year-old woman has 3 days of epigastric pain with fullness, nausea after meals, belching and poor intake. Which feature, if present, is an alarm feature requiring prompt endoscopy according to the Thai GI society?",
         ["Belching", "Postprandial fullness", "Iron-deficiency anaemia", "Early satiation", "Epigastric burning"], 2,
         "Alarm features ของ dyspepsia (สมาคมแพทย์ระบบทางเดินอาหารไทย ในสไลด์) มี 4 ข้อ: **กลืนลำบาก · เลือดออกทางเดินอาหารหรือซีดจากขาดเหล็ก · น้ำหนักลดโดยไม่ทราบสาเหตุ · อาเจียนต่อเนื่อง**\n\nตัวเลือกอื่นเป็น **อาการหลักของ dyspepsia เอง** ไม่ใช่ alarm",
         "Alarm: dysphagia · bleed/IDA · weight loss · persistent vomiting", "Dyspepsia alarm features", R("Alarm features"), DYS),
     mcq(N(6), "Which feature best distinguishes biliary colic from dyspepsia in a patient with epigastric pain?",
         ["Pain located in the epigastrium", "Pain occurs after meals, never before meals, is steady and lasts more than an hour, and occurs episodically", "Pain associated with belching",
          "Pain relieved by defecation", "Pain associated with early satiation"], 1,
         "สไลด์ DDx of dyspepsia: **biliary colic ปวดหลังอาหาร (ไม่ปวดก่อนอาหาร)** ปวด **คงที่นานกว่า 1 ชม.** และเป็นครั้งคราวห่างกันเป็นสัปดาห์หรือเดือน\n\nทั้งสองโรคปวดใต้ลิ้นปี่ได้ (ทางเดินน้ำดีเป็น foregut) ตำแหน่งจึงแยกไม่ได้ · ดีขึ้นหลังถ่าย = colonic pain",
         "Biliary colic: หลังอาหาร คงที่ > 1 ชม. เป็นครั้งคราว", "Dyspepsia mimics", R("Differential diagnosis of dyspepsia"), DYS + ["2.3.11-3(3)"]),
    ], DYS)

# ───────────────────────────── 6
sec("gi-abd-06", "ขั้นตอนดูแล uninvestigated dyspepsia และ H. pylori",
    "อายุมากหรือมี alarm → ส่องกล้อง · ไม่มี → test-and-treat H. pylori หรือ PPI ตามความชุก · bismuth quadruple 14 วัน", 9,
"""### Algorithm ในสไลด์ (AJG 2005)
| กลุ่ม | ทำอะไร |
|---|---|
| **อายุ > 55 ปี หรือมี alarm features** | **ส่องกล้องกระเพาะ (EGD)** |
| อายุ ≤ 55 ไม่มี alarm · **ความชุก H. pylori < 10%** | **ลอง PPI 4–8 สัปดาห์** → ไม่ดีขึ้น → test-and-treat → ยังไม่ดี → EGD |
| อายุ ≤ 55 ไม่มี alarm · **ความชุก H. pylori > 10%** | **Test-and-treat H. pylori** → ไม่ดีขึ้น → PPI → ยังไม่ดี → EGD |
ประเทศไทยความชุก H. pylori สูง → **test-and-treat** เป็นทางเลือกแรกในคนอายุน้อยไม่มี alarm

> **อัปเดต (ไม่ได้มาจากสไลด์)** — **ACG/CAG 2017** ปรับเกณฑ์อายุเป็น **≥ 60 ปี → EGD** · ต่ำกว่านั้นไม่ส่องกล้องเพียงเพราะ alarm features แต่ดูเป็นรายไป · test-and-treat H. pylori → ไม่ดีขึ้นจึงให้ PPI → TCA/prokinetic · แนวทางเอเชียหลายฉบับยังใช้เกณฑ์อายุต่ำกว่า (เช่น 40–45 ปี) เพราะมะเร็งกระเพาะพบบ่อยกว่า

### ตรวจ H. pylori
- **Urea breath test** หรือ **stool antigen** — ไม่ต้องส่องกล้อง
- ส่องกล้อง → **rapid urease test (CLO)** · ชิ้นเนื้อ
- **หยุด PPI 2 สัปดาห์ และยาปฏิชีวนะ/บิสมัท 4 สัปดาห์** ก่อนตรวจ มิฉะนั้นผลลบลวง
- **Serology บอกไม่ได้ว่ายังติดเชื้ออยู่** — ไม่ใช้ตรวจยืนยันการกำจัด

### การรักษา (Maastricht VI/Florence 2022 · แนวทางไทย — ไม่ได้มาจากสไลด์)
- **Bismuth quadruple 14 วัน** — **PPI + bismuth + metronidazole + tetracycline** เป็นทางเลือกแรกในพื้นที่ที่ดื้อ clarithromycin สูง (> 15%) รวมถึงไทย
- Triple therapy ที่มี clarithromycin ใช้เมื่อรู้ว่าเชื้อไวต่อยาเท่านั้น
- **ตรวจยืนยันการกำจัดเชื้อ (UBT/stool Ag) ≥ 4 สัปดาห์หลังจบยา** ทุกราย

### GERD (เกี่ยวข้อง)
แสบร้อนกลางอก เปรี้ยวย้อน ไม่มี alarm → **ปรับพฤติกรรม + PPI 8 สัปดาห์** ก่อน ไม่ต้องส่องกล้องทุกราย
""",
    ["อายุ > 55 (สไลด์) / ≥ 60 (ACG 2017) หรือ alarm → EGD",
     "ความชุก H. pylori สูงอย่างไทย → test-and-treat ก่อน",
     "หยุด PPI 2 สัปดาห์ก่อน UBT · serology ไม่ใช้ยืนยันการกำจัด",
     "Bismuth quadruple 14 วัน · ยืนยันการกำจัด ≥ 4 สัปดาห์หลังจบยา"],
    [mcq(N(7), "A 32-year-old Thai man has 2 months of epigastric pain and postprandial fullness. He has no alarm features. According to the algorithm in the lecture, what is the most appropriate initial approach?",
         ["Immediate EGD", "Test for H. pylori and treat if positive", "CT abdomen", "Empirical antibiotics without testing", "Reassurance only, no investigation"], 1,
         "ผู้ป่วย **อายุ ≤ 55 ไม่มี alarm features** อยู่ในพื้นที่ที่ **ความชุก H. pylori > 10%** (ไทย) → **test-and-treat** (UBT หรือ stool antigen แล้วรักษาถ้าบวก)\n\nถ้าไม่ดีขึ้นจึงให้ PPI และถ้ายังไม่ดีขึ้นจึงส่องกล้อง · EGD ทันทีสงวนไว้สำหรับอายุมากหรือมี alarm",
         "อายุน้อย ไม่มี alarm ในพื้นที่ H. pylori ชุก → test-and-treat", "Uninvestigated dyspepsia", R("Uninvestigated dyspepsia (AJG 2005)"), DYS),
     mcq(N(8), "A patient with dyspepsia has been taking omeprazole daily for 6 weeks. A urea breath test is planned. What is the correct preparation?",
         ["No preparation needed", "Stop the PPI for at least 2 weeks before the test", "Stop the PPI 24 hours before the test", "Add bismuth before the test", "Use H. pylori serology instead to confirm current infection"], 1,
         "PPI กดเชื้อ (ลดเอนไซม์ urease) → **UBT และ stool antigen ผลลบลวง** จึงต้อง **หยุด PPI ≥ 2 สัปดาห์** (ยาปฏิชีวนะและบิสมัท ≥ 4 สัปดาห์)\n\n**Serology บอกเพียงว่าเคยติดเชื้อ** แอนติบอดีอยู่ได้นานหลังกำจัดเชื้อแล้ว จึงไม่ใช้วินิจฉัยการติดเชื้อปัจจุบันหรือยืนยันการกำจัด\n\n*(ไม่ได้มาจากสไลด์ — Maastricht VI 2022)*",
         "หยุด PPI 2 สัปดาห์ก่อน UBT/stool Ag", "H. pylori testing", ["Maastricht VI/Florence consensus 2022"], DYS),
    ], DYS, SRC + " · ACG/CAG 2017 · Maastricht VI 2022")

# ───────────────────────────── 7
GS = NLN + ["2.3.11-3(3)"]
sec("gi-abd-07", "นิ่วในถุงน้ำดีและภาวะแทรกซ้อน",
    "Biliary colic · ถุงน้ำดีอักเสบ (Tokyo 2018) · นิ่วในท่อน้ำดีร่วม · ท่อน้ำดีอักเสบ (Charcot/Reynolds) · ตับอ่อนอักเสบจากนิ่ว", 10,
"""### สเปกตรัมของนิ่วในถุงน้ำดี (ตารางในสไลด์)
| ภาวะ | อาการ | ไข้ | เหลือง | WBC | LFT | Amylase | ภาพถ่าย |
|---|---|---|---|---|---|---|---|
| **Biliary colic** | ปวดใต้ลิ้นปี่/ชายโครงขวาหลังอาหาร เป็นซ้ำ | — | — | ปกติ | ปกติ | ปกติ | US: นิ่ว |
| **ถุงน้ำดีอักเสบเฉียบพลัน** | ปวดชายโครงขวานาน > 6 ชม. **Murphy sign** | **+** | ± เล็กน้อย | **สูง** | ปกติหรือสูงเล็กน้อย | ปกติ | **US: ผนังหนา น้ำรอบถุงน้ำดี sonographic Murphy** |
| **นิ่วในท่อน้ำดีร่วม (CBD stone)** | ปวด + **เหลือง** | — | **+** | ปกติ | **ALP bilirubin สูง** · AST/ALT สูงชั่วคราวช่วงแรก | ปกติ | **ท่อน้ำดีขยาย** |
| **ท่อน้ำดีอักเสบ (cholangitis)** | **ไข้ + เหลือง + ปวดชายโครงขวา** | **+** | **+** | **สูง** | cholestatic | ปกติ | ท่อขยาย |
| **ตับอ่อนอักเสบจากนิ่ว** | ปวดร้าวไปหลัง | ± | ± | สูง | **ALT สูง** | **> 3 เท่า** | นิ่ว ± ท่อขยาย |

### เกณฑ์และการรักษา (Tokyo Guidelines 2018 — ไม่ได้มาจากสไลด์)
**ถุงน้ำดีอักเสบ** = (A) อาการเฉพาะที่ (Murphy, ปวด/กดเจ็บชายโครงขวา) + (B) อักเสบทั่วร่างกาย (ไข้ CRP WBC) + (C) ภาพถ่ายเข้ากัน
- **รักษา: NPO สารน้ำ ยาปฏิชีวนะ** · **ผ่าตัดถุงน้ำดีผ่านกล้องภายใน 72 ชม.** (early) ถ้าผู้ป่วยทนผ่าตัดได้ · เสี่ยงสูง → เจาะระบายถุงน้ำดีผ่านผิวหนัง

**ท่อน้ำดีอักเสบ** — **Charcot triad** (ไข้ เหลือง ปวดชายโครงขวา) · **Reynolds pentad** (+ ความดันต่ำ + ซึมสับสน = รุนแรง)
- **ยาปฏิชีวนะ + สารน้ำ** แล้ว **ระบายท่อน้ำดีด้วย ERCP** — **ด่วน (ภายใน 24 ชม.) ถ้ารุนแรง** หรือไม่ตอบสนองต่อการรักษาเบื้องต้น

**Biliary colic ที่มีอาการ** → ผ่าตัดถุงน้ำดีแบบนัด · **นิ่วไม่มีอาการ** → ส่วนใหญ่ไม่ต้องผ่าตัด
""",
    ["Colic ไม่มีไข้ LFT ปกติ · cholecystitis ไข้ + Murphy + WBC สูง",
     "CBD stone: เหลือง ไม่มีไข้ ALP bilirubin สูง ท่อขยาย",
     "Cholangitis: Charcot (ไข้ เหลือง ปวด) · Reynolds + ช็อก + ซึม → ERCP ด่วน",
     "Cholecystitis → ผ่าตัดผ่านกล้องภายใน 72 ชม. ถ้าทนได้ (Tokyo 2018)"],
    [mcq(N(9), "A 62-year-old woman has fever 39 °C, jaundice and RUQ pain. BP 84/50 mmHg and she is confused. US shows a dilated common bile duct. After fluids and IV antibiotics, what is the key definitive step?",
         ["Elective cholecystectomy in 6 weeks", "Urgent biliary drainage by ERCP", "HIDA scan", "Oral ursodeoxycholic acid", "Observation with antibiotics alone for 2 weeks"], 1,
         "ไข้ + เหลือง + ปวดชายโครงขวา = **Charcot triad** · มี **ความดันต่ำและซึมสับสน = Reynolds pentad** → **ท่อน้ำดีอักเสบรุนแรง**\n\nการรักษาหลักคือ **ระบายท่อน้ำดีอย่างด่วน (ERCP)** ร่วมกับยาปฏิชีวนะและสารน้ำ · ยาปฏิชีวนะอย่างเดียวไม่พอเพราะท่อยังอุดตัน\n\n*(เกณฑ์ความรุนแรงและเวลา — Tokyo Guidelines 2018 ไม่ได้มาจากสไลด์)*",
         "Reynolds pentad → ERCP ด่วน", "Acute cholangitis", R("Gallstone diseases") + ["Tokyo Guidelines 2018"], GS),
     mcq(N(10), "A 45-year-old man has painless jaundice for 1 week with dark urine. No fever. ALP 480 U/L, total bilirubin 6.5 mg/dL, AST/ALT mildly raised, amylase normal, WBC normal. US shows gallstones and a dilated CBD. What is the most likely diagnosis?",
         ["Acute cholecystitis", "Biliary colic", "Choledocholithiasis (CBD stone)", "Acute cholangitis", "Gallstone pancreatitis"], 2,
         "ตารางในสไลด์: **CBD stone — เหลือง ไม่มีไข้ WBC ปกติ · ALP และ bilirubin สูง · amylase ปกติ · ท่อน้ำดีขยาย**\n\nถ้ามีไข้และ WBC สูงด้วย = cholangitis · amylase/lipase > 3 เท่า = gallstone pancreatitis · cholecystitis ไม่ค่อยเหลืองชัดและมี Murphy sign\n\nแม้ไม่ปวดก็ต้องนึกถึง **มะเร็งหัวตับอ่อน/ท่อน้ำดี** ไว้ด้วย",
         "เหลือง ไม่มีไข้ ALP สูง ท่อขยาย = CBD stone", "Gallstone spectrum", R("Gallstone diseases"), GS),
    ], GS, SRC + " · Tokyo Guidelines 2018")

# ───────────────────────────── 8
AP = NLN + ["2.3.11(1)"]
sec("gi-abd-08", "ตับอ่อนอักเสบเฉียบพลันและเรื้อรัง",
    "AP 2 ใน 3 · amylase ขึ้น 6 ชม. lipase อยู่นานกว่า · ประเมินความรุนแรง · ACG 2024: LR พอประมาณ กินเร็ว ไม่ให้ยาฆ่าเชื้อป้องกัน · CP: DM type 3c ถ่ายเป็นไขมัน", 11,
"""### ตับอ่อนอักเสบเฉียบพลัน — วินิจฉัย 2 ใน 3 (Revised Atlanta)
1. **ปวดท้องเข้ากัน** — ปวดคงที่ท้องส่วนบน **ร้าวไปหลัง ~50%** คลื่นไส้อาเจียน
2. **Amylase หรือ lipase > 3 เท่าของค่าปกติ**
3. **ภาพ CT/MRI/US เข้ากัน**
**สาเหตุ** — **เหล้า · นิ่ว** (สองอันดับแรก) · เมตาบอลิก (**TG > 1,000**, แคลเซียมสูง) · บาดเจ็บ/หลัง ERCP · ยา · กรรมพันธุ์ · ไม่ทราบสาเหตุ

### ผลเลือดและอาการแสดง (สไลด์)
- **Amylase ขึ้นภายใน 6 ชม. อยู่ 3–5 วัน** · **lipase อยู่นานกว่า** และจำเพาะกว่า — ระดับไม่บอกความรุนแรง
- **Cullen (รอบสะดือ) / Grey Turner (สีข้าง)** — พบ **1–3%** · ขึ้นหลัง **~48 ชม.** · **อัตราตาย ~37%** (เลือดออกหลังเยื่อบุช่องท้อง)
- ประเมินความรุนแรง: **Ranson · APACHE-II · BISAP · SIRS/อวัยวะล้มเหลว** · Revised Atlanta: mild (ไม่มีอวัยวะล้มเหลว) · moderately severe (ล้มเหลว < 48 ชม. หรือภาวะแทรกซ้อนเฉพาะที่) · **severe (อวัยวะล้มเหลว > 48 ชม.)**

### การรักษา — ACG Guideline 2024 (ไม่ได้มาจากสไลด์)
- **สารน้ำแบบมีเป้าหมาย ปริมาณพอประมาณ** — **Lactated Ringer's** (WATERFALL trial: ให้แบบ aggressive เพิ่ม fluid overload โดยไม่ช่วยผลลัพธ์)
- **ให้กินทางปากเร็ว (ภายใน 24–48 ชม.) ถ้าทนได้** · ถ้ากินไม่ได้ให้ทางสายให้อาหาร ดีกว่าทางหลอดเลือด
- **ไม่ให้ยาปฏิชีวนะป้องกัน** แม้ severe หรือมีเนื้อตาย · ให้เมื่อมีหลักฐานติดเชื้อ
- **ERCP ภายใน 24 ชม. เฉพาะเมื่อมี cholangitis ร่วม** · ไม่ทำในทุกรายของ gallstone pancreatitis
- **Gallstone pancreatitis ชนิด mild → ผ่าตัดถุงน้ำดีในการนอนโรงพยาบาลครั้งเดียวกัน** ป้องกันการกลับเป็นซ้ำ
- ระงับปวดเต็มที่ (รวม opioid)

### ตับอ่อนอักเสบเรื้อรัง (สไลด์)
- พังผืดถาวร · **ปวดร้าวไปหลัง แย่ลงหลังอาหาร** · **เบาหวานชนิด 3c (pancreatogenic)** · **ถ่ายเป็นไขมัน**
- ภาพถ่าย: หินปูนในตับอ่อน ท่อตับอ่อนขยาย · **ภาพปกติไม่ตัดโรค**
- **เอนไซม์ตับอ่อน (PERT) ไม่ช่วยลดปวด** — ใช้แก้ถ่ายเป็นไขมัน
- ปวด: NSAIDs · opioid · TCA · ERCP ระบายท่อตับอ่อน · **EUS celiac plexus neurolysis** · ผ่าตัด
""",
    ["AP = 2 ใน 3: ปวด · enzyme > 3 เท่า · ภาพถ่าย",
     "Lipase อยู่นานกว่า amylase · ระดับไม่บอกความรุนแรง",
     "Cullen/Grey Turner 1–3% หลัง ~48 ชม. ตาย ~37%",
     "ACG 2024: LR พอประมาณ · กินเร็ว · ไม่ให้ antibiotic ป้องกัน · ERCP เฉพาะ cholangitis",
     "CP: DM 3c · steatorrhea · PERT ไม่ลดปวด"],
    [mcq(N(11), "A 38-year-old man with heavy alcohol use has epigastric pain radiating to the back for 4 days. Serum amylase is 1.5 times the upper limit of normal. Which test is most useful to confirm acute pancreatitis now?",
         ["Repeat amylase", "Serum lipase", "Plain abdominal X-ray", "Serum calcium", "Upper endoscopy"], 1,
         "สไลด์: **amylase ขึ้นใน 6 ชม. และกลับปกติใน 3–5 วัน** — มาวันที่ 4 จึงอาจลงแล้ว · **lipase อยู่นานกว่าและจำเพาะต่อตับอ่อนกว่า** จึงช่วยยืนยันในผู้ที่มาช้า\n\nถ้า enzyme ยังไม่เข้าเกณฑ์ ใช้ **CT ที่เข้ากัน** เป็นเกณฑ์ข้อที่สาม (2 ใน 3)",
         "มาช้า → lipase ดีกว่า amylase", "Pancreatic enzymes", R("Acute pancreatitis"), AP),
     mcq(N(12), "A 50-year-old woman has mild gallstone pancreatitis without cholangitis. Which management is recommended by current guidelines?",
         ["Prophylactic imipenem", "Urgent ERCP within 24 hours", "Moderate goal-directed lactated Ringer's, early oral feeding, and cholecystectomy during the same admission",
          "Nil by mouth for 7 days with TPN", "Aggressive fluids of 20 mL/kg/h for 48 hours"], 2,
         "**ACG 2024** (ไม่ได้มาจากสไลด์): สารน้ำ **Lactated Ringer's แบบพอประมาณ** · **ให้กินเร็ว** · **ไม่ให้ยาปฏิชีวนะป้องกัน** · **ERCP เฉพาะเมื่อมี cholangitis** · **ผ่าตัดถุงน้ำดีในการนอนครั้งเดียวกัน** สำหรับรายที่ไม่รุนแรง\n\nสารน้ำแบบ aggressive (WATERFALL trial 2022) เพิ่ม fluid overload โดยไม่ช่วยลดความรุนแรง",
         "Mild gallstone AP → ผ่าตัดถุงน้ำดีก่อนกลับบ้าน", "AP management", ["ACG Guideline: Management of acute pancreatitis (2024)"], AP + ["2.3.11-3(3)"]),
    ], AP + ["2.3.11-3(3)"], SRC + " · ACG 2024 · Revised Atlanta 2012")

# ───────────────────────────── 9
sec("gi-abd-09", "อาการคลาสสิกและปวดท้องรุนแรง",
    "ไส้ติ่ง · ถุงน้ำดี · diverticulitis · ท้องนอกมดลูก · mesenteric ischemia · ลำไส้อุดตัน · ตับอ่อน · ทะลุ · รังไข่บิด · AAA แตก · นิ่วท่อไต", 7,
"""### อาการคลาสสิก (สไลด์)
| โรค | ลักษณะเด่น |
|---|---|
| **ไส้ติ่งอักเสบ** | **รอบสะดือ → ขวาล่าง** ไข้ คลื่นไส้อาเจียน เบื่ออาหาร |
| **ถุงน้ำดีอักเสบ** | ชายโครงขวา ร้าวสะบักขวา Murphy ไข้ |
| **Diverticulitis** | **ท้องซ้ายล่าง ผู้สูงอายุ** ไข้ |
| **ท้องนอกมดลูกแตก** | ผู้หญิงวัยเจริญพันธุ์ ขาดประจำเดือน ปวดท้องน้อยข้างเดียว ช็อก |
| **Mesenteric ischemia** | **ปวดมากเกินกว่าที่ตรวจพบ (pain out of proportion)** · AF |
| **ลำไส้อุดตัน** | ปวดบิด อาเจียน ท้องอืด ไม่ผายลม |
| **ตับอ่อนอักเสบ** | ใต้ลิ้นปี่ **ร้าวไปหลัง** |
| **กระเพาะ/ลำไส้ทะลุ** | **ปวดทันทีทั่วท้อง** ท้องแข็ง ลมใต้กะบังลม |
| **รังไข่บิด** | ปวดท้องน้อยข้างเดียวทันที อาเจียน |
| **AAA แตก** | **ปวดท้อง + หลัง + ก้อนเต้นตามชีพจร** ช็อก |
| **นิ่วท่อไต** | **สีข้าง → ขาหนีบ** กระสับกระส่าย ปัสสาวะเป็นเลือด |

### ปวดท้องรุนแรง — ห้ามพลาด (สไลด์)
**Peritonitis · มะเร็ง · mesenteric ischemia · ตับอ่อนอักเสบ · aortic dissection · อวัยวะกลวงขนาดเล็กอุดตัน (ท่อน้ำดี ท่อไต)**
> **อย่าลืมนอกช่องท้อง (ไม่ได้มาจากสไลด์)** — **MI ผนังด้านล่าง** ปวดใต้ลิ้นปี่ได้ · ปอดอักเสบกลีบล่าง · DKA · ตั้งครรภ์ (ตรวจ urine hCG ในหญิงวัยเจริญพันธุ์ทุกราย) · งูสวัด · porphyria
""",
    ["ไส้ติ่ง รอบสะดือ → ขวาล่าง · diverticulitis ซ้ายล่างผู้สูงอายุ",
     "Pain out of proportion = mesenteric ischemia",
     "ปวด + หลัง + ก้อนเต้น + ช็อก = AAA แตก",
     "หญิงวัยเจริญพันธุ์ปวดท้อง → urine hCG เสมอ · ปวดใต้ลิ้นปี่ → EKG"],
    [mcq(N(13), "A 72-year-old hypertensive smoker presents with sudden severe abdominal and back pain, BP 80/50 mmHg and a pulsatile periumbilical mass. What is the most likely diagnosis?",
         ["Acute pancreatitis", "Ruptured abdominal aortic aneurysm", "Ureteric colic", "Perforated peptic ulcer", "Sigmoid volvulus"], 1,
         "สไลด์ classic presentation: **AAA แตก = ปวดท้องและหลังทันที + ก้อนเต้นตามชีพจร + ช็อก** ในผู้สูงอายุที่มีปัจจัยเสี่ยงหลอดเลือด (สูบบุหรี่ ความดันสูง ชาย)\n\nต้องให้เลือดแบบ permissive hypotension และส่งผ่าตัด/ใส่ stent graft ด่วน · ตับอ่อนอักเสบปวดร้าวหลังได้แต่ไม่มีก้อนเต้น",
         "ปวดท้อง + หลัง + pulsatile mass + ช็อก = ruptured AAA", "Classic presentations", R("Classic presentation of abdominal pain")),
    ])

# ───────────────────────────── 10
OBS = NLN + ["2.3.11-3(5)"]
sec("gi-abd-10", "ท้องอืดจากลม: ลำไส้อุดตันและ toxic megacolon",
    "SBO: อาเจียน เสียงลำไส้ดัง air-fluid level · ผังผืดพบบ่อยสุด · LBO: มะเร็ง volvulus · NPO NG · megacolon 12/8/6/6.5 ซม.", 8,
"""### Gaseous abdomen — DDx (สไลด์)
**ลำไส้เล็กอุดตัน · ลำไส้ใหญ่อุดตัน · mesenteric ischemia · toxic megacolon · ทะลุ (ลมอิสระ)**

| | **ลำไส้เล็กอุดตัน (SBO)** | **ลำไส้ใหญ่อุดตัน (LBO)** |
|---|---|---|
| อาการ | **คลื่นไส้อาเจียนเด่น** ปวดบิดรอบสะดือ | **ท้องอืดมาก** ไม่ถ่าย ไม่ผายลม อาเจียนทีหลัง |
| เสียงลำไส้ | **ดังถี่ (hyperactive)** — ยกเว้นเมื่อขาดเลือด | |
| ภาพรังสี | ลำไส้เล็กโป่ง **air-fluid level หลายระดับ** (step ladder) | ลำไส้ใหญ่โป่ง **ไม่มีลมส่วนปลาย** · coffee bean (sigmoid volvulus) |
| สาเหตุ | **พังผืดจากการผ่าตัด (พบบ่อยสุด)** · ไส้เลื่อน · ลำไส้กลืนกัน · volvulus · internal hernia | **มะเร็งลำไส้ใหญ่** · **sigmoid volvulus** · อุจจาระอัดแน่น · ลำไส้กลืนกัน |
| ตรวจ | **CT** บอกจุดอุดตันและการขาดเลือด | **CT** |
| รักษา | **NPO · ใส่ NG ดูด · สารน้ำ** แก้เกลือแร่ · ผ่าตัดถ้าขาดเลือดหรือไม่ดีขึ้น | **rectal tube / ส่องกล้องคลาย volvulus** · ผ่าตัด/ใส่ stent ในมะเร็ง |

**สัญญาณลำไส้ขาดเลือด (strangulation)** — ปวดเปลี่ยนจากบิดเป็นคงที่ ไข้ ชีพจรเร็ว WBC สูง lactate สูง กดเจ็บเฉพาะที่ → **ผ่าตัดด่วน**

### Megacolon และ toxic megacolon (สไลด์)
| ส่วนของลำไส้ใหญ่ | ขยาย > |
|---|---|
| **Caecum** | **12 ซม.** |
| Ascending | 8 ซม. |
| **Transverse** | **6 ซม.** |
| Rectosigmoid | 6.5 ซม. |
**Toxic megacolon = megacolon + SIRS** — พบใน **UC รุนแรง** และ **C. difficile colitis** · เสี่ยงทะลุ → หยุดยาแก้ท้องเสีย/opioid/anticholinergic · steroid IV (UC) · ปรึกษาศัลยแพทย์
""",
    ["SBO: อาเจียนเด่น เสียงลำไส้ดัง air-fluid level · พังผืดพบบ่อยสุด",
     "LBO: ไม่มีลมส่วนปลาย · มะเร็งลำไส้ใหญ่ · sigmoid volvulus",
     "SBO: NPO + NG + สารน้ำ · strangulation → ผ่าตัด",
     "Megacolon: caecum > 12 · transverse > 6 ซม. · + SIRS = toxic"],
    [mcq(N(14), "A 58-year-old man with previous appendicectomy has colicky periumbilical pain, repeated vomiting and no flatus for 1 day. Bowel sounds are high-pitched. X-ray shows dilated small-bowel loops with multiple air-fluid levels. No fever, no peritonism, lactate normal. What is the initial management?",
         ["Immediate laparotomy", "Nil by mouth, nasogastric decompression and IV fluids with electrolyte correction", "Oral laxatives", "Colonoscopic decompression", "Rectal tube"], 1,
         "**ลำไส้เล็กอุดตันจากพังผืด** (เคยผ่าตัด) **ไม่มีสัญญาณขาดเลือด** → รักษาประคับประคองก่อน: **NPO · ใส่ NG ดูดลม · สารน้ำและเกลือแร่** · CT ดูจุดอุดตัน\n\nผ่าตัดเมื่อมีสัญญาณ strangulation (ปวดคงที่ ไข้ WBC/lactate สูง peritonitis) หรือไม่ดีขึ้น · rectal tube และส่องกล้องใช้กับ sigmoid volvulus (LBO) · ห้ามยาระบาย",
         "SBO ไม่มี strangulation → NPO + NG + IV fluid", "Small bowel obstruction", R("Small bowel obstruction"), OBS),
    ], OBS)

# ───────────────────────────── 11
sec("gi-abd-11", "ลำไส้ขาดเลือดเฉียบพลันและเยื่อบุช่องท้องอักเสบ",
    "Pain out of proportion · AMAE จาก AF · MAT กลัวกิน · MVT ภาวะเลือดแข็งตัวง่าย · NOMI ช็อก · peritonitis ปฐมภูมิ vs ทุติยภูมิ · ลมใต้กะบังลม", 9,
"""### Acute mesenteric ischemia (สไลด์)
**ปวดรุนแรงเกินกว่าที่ตรวจพบ (pain out of proportion to physical findings)** — ท้องยังนุ่มในช่วงแรก
| ชนิด | ปัจจัยเสี่ยง | ลักษณะ | ตรวจ |
|---|---|---|---|
| **Arterial embolism (AMAE)** — พบบ่อยสุด | **AF · ลิ้นหัวใจรูมาติก · CAD** | **ทันที** ปวดมาก ถ่ายเหลว อาเจียน | **CT angiography** / angiography |
| **Arterial thrombosis (MAT)** | หลอดเลือดแดงแข็ง | เคยมี **ปวดหลังอาหาร กลัวกิน (sitophobia) น้ำหนักลด** มาก่อน | CTA |
| **Venous thrombosis (MVT)** | **ภาวะเลือดแข็งตัวง่าย · หัวใจซีกขวาล้มเหลว · มะเร็ง · ตับแข็ง** | **ค่อยเป็นค่อยไป** | **CT/MR venography** |
| **Non-occlusive (NOMI)** | **ช็อก · digitalis · ยาขับปัสสาวะ · beta-blocker** · vasopressor | ผู้ป่วยหนัก | angiography |
**Lactate สูง** และกรดเกินช่วงท้าย (ปกติไม่ตัดโรค) · รักษา: สารน้ำ **heparin** ยาปฏิชีวนะ · **ผ่าตัดหรือเปิดหลอดเลือด (embolectomy/endovascular)** · ตัดลำไส้ที่ตาย

### Peritonitis (สไลด์)
- ปวด **คงที่ รุนแรง แย่ลงเมื่อกดหรือขยับ** · **rebound tenderness** · guarding แบบเกร็งเอง
- **Peritonitis** (การอักเสบจริง) vs **peritonism** (อาการแสดงคล้ายแต่ไม่มีการอักเสบของเยื่อบุ)
| | **ปฐมภูมิ (SBP)** | **ทุติยภูมิ** |
|---|---|---|
| ที่มา | เชื้อจากลำไส้ข้ามผนังเข้าน้ำในท้อง **ในตับแข็งที่มีท้องมาน** | **อวัยวะทะลุหรืออักเสบ** — แผลกระเพาะทะลุ น้ำดี ไส้ติ่งแตก |
| วินิจฉัย | **PMN ในน้ำท้อง ≥ 250/mm³** · เชื้อเดียว | เชื้อหลายชนิด · **ลมอิสระใต้กะบังลม** |
| รักษา | ยาปฏิชีวนะ (cefotaxime) + albumin | **ผ่าตัดแก้ต้นเหตุ** + ยาปฏิชีวนะ |
- **เฉพาะที่**: ไส้ติ่ง ถุงน้ำดี ฝี diverticulitis · **ทั่วท้อง**: SBP แผลทะลุ น้ำดีรั่ว
- **ลมอิสระ (free air)** — **CXR ท่ายืน** เห็นลมใต้กะบังลม → ทะลุ ต้องผ่าตัด
""",
    ["AMI: pain out of proportion · AMAE จาก AF ทันที · MAT กลัวกิน · MVT ค่อยเป็น · NOMI ช็อก",
     "Lactate ปกติไม่ตัด AMI · CTA",
     "SBP: PMN ≥ 250 · secondary: หลายเชื้อ + free air → ผ่าตัด",
     "CXR ท่ายืน หาลมใต้กะบังลม"],
    [mcq(N(15), "A 74-year-old woman with atrial fibrillation not on anticoagulation develops sudden severe periumbilical pain and diarrhoea. She is writhing in pain, but the abdomen is soft with only mild tenderness. Lactate is 4.2 mmol/L. What is the most likely diagnosis and next investigation?",
         ["Acute pancreatitis — serum lipase", "Acute mesenteric arterial embolism — CT angiography", "Gastroenteritis — stool culture", "Biliary colic — ultrasound", "IBS — reassurance"], 1,
         "**ปวดรุนแรงเกินกว่าที่ตรวจพบ + AF ไม่ได้ยาต้านการแข็งตัว + ทันที + ถ่ายเหลว** = **acute mesenteric arterial embolism (AMAE)** — ชนิดที่พบบ่อยที่สุด\n\nตรวจ **CT angiography** ทันที · ให้ heparin สารน้ำ และส่งเปิดหลอดเลือดหรือผ่าตัด · lactate สูงสนับสนุนแต่ถ้าปกติก็ไม่ตัดโรค",
         "AF + pain out of proportion = AMAE → CTA", "Acute mesenteric ischemia", R("Acute mesenteric ischemia"), NLN + ["2.1.12"]),
     mcq(N(16), "A patient with sudden generalised abdominal pain and board-like rigidity has free air under the diaphragm on an erect chest X-ray. Which statement is correct?",
         ["This is primary (spontaneous) bacterial peritonitis", "This is secondary peritonitis from a perforated viscus and needs surgical source control",
          "Ascitic PMN ≥ 250/mm³ is required for diagnosis", "Antibiotics alone are sufficient", "Peritonism rules out peritonitis"], 1,
         "**ลมอิสระใต้กะบังลม = อวัยวะกลวงทะลุ** (บ่อยสุดคือแผลกระเพาะ/ลำไส้เล็กส่วนต้นทะลุ) → **secondary peritonitis** ทั่วท้อง ต้อง **ผ่าตัดแก้ต้นเหตุ** ร่วมกับยาปฏิชีวนะ\n\n**SBP** เกิดในตับแข็งที่มีท้องมาน ไม่มีลมอิสระ วินิจฉัยด้วย PMN ในน้ำท้อง ≥ 250 และรักษาด้วยยา",
         "Free air = secondary peritonitis → ผ่าตัด", "Peritonitis", R("Peritonitis")),
    ], NLN + ["2.1.12", "2.1.18"])

# ───────────────────────────── MEQ / OSCE
LECNAME = "Approach to abdominal pain (นพ.กิตติ)"
MEQ = [{"id": "GI-ABD-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Acute epigastric pain — gallstone pancreatitis: diagnosis, severity and management",
 "vignette": """ผู้ป่วยหญิงไทยอายุ 48 ปี มาด้วยปวดท้องใต้ลิ้นปี่ 8 ชั่วโมงหลังรับประทานอาหารมัน
PI: ปวดคงที่ รุนแรง ร้าวไปหลัง คลื่นไส้อาเจียน 4 ครั้ง · 6 เดือนก่อนเคยปวดใต้ลิ้นปี่หลังอาหารเป็นครั้งคราว ครั้งละ 2–3 ชม. หายเอง
ประวัติ: ไม่ดื่มเหล้า ไม่ได้กินยาประจำ · BMI 29
PE: BT 37.8 C · BP 118/72 · HR 104 · RR 22 · SpO2 97% · ไม่เหลือง · กดเจ็บใต้ลิ้นปี่ มี guarding เล็กน้อย ไม่มี rebound · Murphy sign negative · ไม่มี Cullen/Grey Turner sign
Lab: WBC 14,200 · Hct 44% · BUN 18 · Cr 0.9 · glucose 140 · Ca 9.0 · TG 180 · AST 240 · ALT 310 · ALP 150 · TB 1.6 · lipase 2,400 U/L (ULN 60)
US: นิ่วหลายก้อนในถุงน้ำดี ผนังไม่หนา CBD 6 มม.""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัยพร้อมเกณฑ์ และสาเหตุที่น่าจะเป็น (3 คะแนน)",
   "a": """**Acute pancreatitis จากนิ่ว (gallstone pancreatitis)**
- เข้าเกณฑ์ **2 ใน 3**: ปวดใต้ลิ้นปี่ร้าวไปหลัง + **lipase 40 เท่าของค่าปกติ (> 3 เท่า)** — ไม่จำเป็นต้องทำ CT เพื่อวินิจฉัย
- สาเหตุเป็นนิ่ว: **มีนิ่วในถุงน้ำดี · ALT > 150 (สามเท่าของปกติ)** · ไม่ดื่มเหล้า · TG และแคลเซียมปกติ · เคยมี biliary colic มาก่อน"""},
  {"q": "2. จงประเมินความรุนแรง และบอกว่าจะเฝ้าระวังอะไร (3 คะแนน)",
   "a": """- ขณะนี้ **ยังไม่มีอวัยวะล้มเหลว** (ความดัน การหายใจ ไตปกติ) · มี **SIRS** (HR > 90, RR > 20, WBC > 12,000) → เสี่ยงดำเนินโรครุนแรงขึ้น
- **BISAP**: BUN > 25 (0) · ซึมสับสน (0) · **SIRS (1)** · อายุ > 60 (0) · น้ำในเยื่อหุ้มปอด (ยังไม่ทราบ) → 1 คะแนน = เสี่ยงต่ำ
- เฝ้าระวัง **สัญญาณชีพ ปัสสาวะ BUN Hct ใน 24–48 ชม.** · SIRS ที่ไม่หาย, BUN/Hct เพิ่มขึ้น = พยากรณ์ไม่ดี · อวัยวะล้มเหลว > 48 ชม. = severe
- CT เมื่อไม่ดีขึ้นหลัง 48–72 ชม. เพื่อดูเนื้อตายหรือภาวะแทรกซ้อน"""},
  {"q": "3. จงบอกแนวทางการรักษาในช่วงแรก (4 คะแนน)",
   "a": """ตาม **ACG 2024**
- **สารน้ำ Lactated Ringer's แบบมีเป้าหมาย ปริมาณพอประมาณ** — ประเมินซ้ำบ่อยจาก HR ปัสสาวะ BUN ไม่ให้มากเกินจน fluid overload
- **ระงับปวด** อย่างเพียงพอ (รวม opioid)
- **ให้กินทางปากเร็ว** เมื่อปวดและคลื่นไส้ลดลง ไม่ต้องรอ enzyme ปกติ
- **ไม่ให้ยาปฏิชีวนะป้องกัน** · **ERCP ไม่จำเป็น** เพราะไม่มี cholangitis (ไม่มีไข้สูง เหลือง) และ CBD ไม่ขยาย"""},
  {"q": "4. ก่อนกลับบ้านต้องทำอะไรเพื่อป้องกันการเป็นซ้ำ (2 คะแนน)",
   "a": """- **ผ่าตัดถุงน้ำดีผ่านกล้องในการนอนโรงพยาบาลครั้งเดียวกัน** (mild gallstone pancreatitis) — ถ้ารอผ่าตัดภายหลัง เสี่ยงกลับเป็นซ้ำสูง
- ถ้าสงสัยนิ่วในท่อน้ำดีค้าง (LFT ไม่ลง ท่อขยาย) → MRCP หรือ EUS ก่อน/ระหว่างผ่าตัด"""}],
 "ref": ["สไลด์ นพ.กิตติ — gallstone diseases, acute pancreatitis", "ACG Guideline: Management of acute pancreatitis (2024)"],
 "nl": ["2.3.11(1)", "2.3.11-3(3)", "2.1.11"], "years": [], "_kind": "meq", "_set": SET}]

OSCE = [{"id": "GI-ABD-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "SAQ – Matching abdominal pain patterns to diagnoses",
 "station": "SAQ (เขียนตอบ) 6 นาที",
 "instruction": """จงให้การวินิจฉัยที่น่าจะเป็นที่สุด และการตรวจเพิ่มเติม 1 อย่าง สำหรับผู้ป่วย 6 รายต่อไปนี้

| ราย | ลักษณะ |
|---|---|
| A | ชาย 55 ปี ปวดใต้ลิ้นปี่หลังอาหาร 2–3 ชม. คงที่ นานกว่า 1 ชม. เป็นครั้งคราว 2 เดือน ไม่มีไข้ LFT ปกติ |
| B | หญิง 35 ปี ปวดท้องเป็น ๆ หาย ๆ 1 ปี ดีขึ้นหลังถ่าย ท้องผูกสลับเสีย ไม่มี alarm feature |
| C | ชาย 68 ปี ปวดท้องซ้ายล่าง 2 วัน ไข้ 38.3 C กดเจ็บซ้ายล่าง |
| D | หญิง 26 ปี ขาดประจำเดือน 7 สัปดาห์ ปวดท้องน้อยขวาทันที หน้ามืด BP 86/50 |
| E | ชาย 45 ปี ปวดสีข้างซ้ายร้าวลงขาหนีบ บิดตัวไปมา ปัสสาวะมีเลือดเล็กน้อย |
| F | ชาย 60 ปี ปวดใต้ลิ้นปี่ 30 นาที เหงื่อแตก คลื่นไส้ เบาหวาน สูบบุหรี่ ท้องนุ่ม |""",
 "answer": """| ราย | การวินิจฉัย | ตรวจเพิ่ม | คะแนน |
|---|---|---|---|
| **A** | **Biliary colic** (หลังอาหาร คงที่ > 1 ชม. เป็นครั้งคราว) | **US ช่องท้องส่วนบน** | 2 |
| **B** | **IBS (Rome IV)** — ปวดจากลำไส้ใหญ่ | CBC · ตรวจเลือดแฝงในอุจจาระ (อายุน้อยไม่มี alarm) | 2 |
| **C** | **Diverticulitis** (ผู้สูงอายุ ซ้ายล่าง ไข้) | **CT ช่องท้อง** | 2 |
| **D** | **ท้องนอกมดลูกแตก** + ช็อก | **urine/serum hCG** + US ทางช่องคลอด/FAST → ผ่าตัดด่วน | 2 |
| **E** | **นิ่วท่อไต** | **CT KUB ไม่ฉีดสี** (UA) | 2 |
| **F** | **Acute MI ผนังด้านล่าง** (นอกช่องท้อง) | **EKG 12 lead ภายใน 10 นาที** + troponin | 2 |

**หลักที่ต้องแสดง**: ตำแหน่งอย่างเดียวไม่พอ ใช้อาการร่วม · หญิงวัยเจริญพันธุ์ต้องตรวจ hCG · ปวดใต้ลิ้นปี่ในผู้มีปัจจัยเสี่ยงต้องทำ EKG""",
 "ref": ["สไลด์ นพ.กิตติ — classic presentation of abdominal pain, what is your diagnosis?"],
 "nl": ["2.1.11", "2.3.11-3(3)", "2.3.11(6)", "2.3.11-3(9)"], "years": [], "_kind": "meq", "_set": SET}]

LECTURE = {
 "lec": LEC, "date": "อ. 27 ต.ค.",
 "title": "Approach to abdominal pain",
 "subtitle": "Visceral vs parietal · ตำแหน่งตามอวัยวะ · ปวดจากลำไส้ใหญ่และ IBS · dyspepsia และ H. pylori · นิ่วถุงน้ำดีและตับอ่อนอักเสบ · ลำไส้อุดตัน ขาดเลือด และ peritonitis",
 "objectives": [
   "อธิบายกลไก visceral และ parietal pain และใช้ตำแหน่งตาม foregut midgut hindgut",
   "ซักประวัติและตรวจร่างกายผู้ป่วยปวดท้องอย่างเป็นระบบ แยกปวดจากอวัยวะกลวง อวัยวะตัน และเยื่อบุช่องท้อง",
   "แยกปวดจากลำไส้ใหญ่และวินิจฉัย IBS ตาม Rome IV พร้อม alarm features",
   "นิยาม dyspepsia แยกโรคที่เลียนแบบ และวางขั้นตอนดูแล uninvestigated dyspepsia และ H. pylori",
   "แยกสเปกตรัมของโรคนิ่วในถุงน้ำดีจากอาการและผลเลือด",
   "วินิจฉัย ประเมินความรุนแรง และรักษาตับอ่อนอักเสบเฉียบพลันตามแนวทางปัจจุบัน และรู้จักตับอ่อนอักเสบเรื้อรัง",
   "จดจำอาการคลาสสิกและภาวะปวดท้องรุนแรงที่ห้ามพลาด รวมถึงลำไส้อุดตัน ลำไส้ขาดเลือด และ peritonitis"],
 "nlGap": "เกณฑ์ฯ มีรหัส `นล. 2.1.11` Abdominal pain · `2.3.11(1)` Acute pancreatitis · `2.3.11(6)` Functional GI disorder · `2.3.11-3(3)` Gallstone/cholecystitis/cholangitis · `2.3.11-3(5)` GI obstruction แต่สไลด์ปี 2565 อ้าง algorithm dyspepsia ปี 2005 และ **การรักษาตับอ่อนอักเสบ ถุงน้ำดีอักเสบ และ H. pylori เปลี่ยนไปแล้ว** จึงอ้างอิงแนวทางด้านล่าง",
 "guidelines": [
   "**ACG Guideline: Management of acute pancreatitis (2024)** — LR แบบพอประมาณ · กินเร็ว · ไม่ให้ยาปฏิชีวนะป้องกัน · ERCP เฉพาะ cholangitis · ผ่าตัดถุงน้ำดีในการนอนครั้งเดียวกัน",
   "**Revised Atlanta classification (2012)** — เกณฑ์ 2 ใน 3 และระดับความรุนแรง",
   "**Tokyo Guidelines 2018 (TG18)** — เกณฑ์และการรักษาถุงน้ำดีอักเสบ/ท่อน้ำดีอักเสบ",
   "**ACG/CAG Clinical Guideline: Management of dyspepsia (2017)** — EGD เมื่ออายุ ≥ 60",
   "**Maastricht VI/Florence consensus (2022)** และแนวทาง H. pylori ของไทย — bismuth quadruple 14 วัน",
   "**Rome IV (2016)** — IBS และ functional dyspepsia"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# กระจายตำแหน่งคำตอบของข้อใหม่ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น)
_slot = 0
for s_ in S:
    for it in s_["items"]:
        tgt = [0, 2, 4, 1, 3][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", SET + ".json")
data = json.load(open(path, encoding="utf-8"))
data = [l for l in data if l.get("lec") != LEC] + [LECTURE]
data.sort(key=lambda l: tuple(int(x) for x in l["lec"].split("/")[::-1]))
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

added = link_mock(SET, LEC, {"gi-abd-04": ["MOCK-154", "MOCK-155"], "gi-abd-06": ["MOCK-161", "MOCK-160"],
                             "gi-abd-07": ["MOCK-157"], "gi-abd-08": ["MOCK-156", "MOCK-152"]})

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
