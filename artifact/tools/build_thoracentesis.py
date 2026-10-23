#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""คาบ chest "Thoracentesis" — Thoracentesis with interpretation (Active learning กลุ่ม 5) → data/chest.json
ต้นฉบับ: Drive 1LS_Dwx1GSl1Ikbmbon5VX8KZDQ7gAR8z "Thoracen & Pleural fluid analysis & interpretation.pdf" (25.9 MB · อ่านได้เฉพาะข้อความ)
โน้ตสไลด์: slides/thoracentesis_notes.md · ภาพประกอบ: figs_thoracentesis.py (20 ภาพ)
เนื้อหาซ้อนกับคาบ 17 (Pleural disease) → คาบนี้เน้น "หัตถการ + การเก็บสิ่งส่งตรวจ + อ่านผลทีละขั้น" และลิงก์กลับไปคาบ 17
คลัง Ward Drill: ข้อ pleural ของชุด chest ผูกกับคาบ 17 หมดแล้ว (รวม CH-MCQ-20, CH-OSCE-04) → ผูก Mock M08 ที่ยังว่าง: MOCK-137/138/142"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_mock import link_mock
import figs_thoracentesis as F

SET, LEC = "chest", "Thoracentesis"
SRC = "สไลด์ Active learning กลุ่ม 5 — Thoracentesis with interpretation"
SRC_ADD = SRC + " + BTS Clinical Statement on Pleural Procedures 2023 / BTS Guideline for Pleural Disease 2023 (ส่วนที่สไลด์ไม่มี)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl, figs=(), source=SRC_ADD):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": source,
              "nl": nl, "md": md, "pearls": pearls, "items": items, "figs": {k: getattr(F, k)() for k in figs}})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl):
    assert len(choices) == 5 and 0 <= answer <= 4 and len(set(choices)) == 5
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}
N = lambda n: "CH-THOR-MCQ-%02d" % n
R = lambda p: ["สไลด์ AL กลุ่ม 5 — " + p]
BTS = "BTS Clinical Statement on Pleural Procedures 2023"
BTSG = "BTS Guideline for Pleural Disease 2023"
PE, PFA, BF, ANAT, PLEUR = "2.3.10(7)", "B6.3(1)", "3.1.7", "B6.1.1(4)", "B6.2.2(10)"
HTX, PTX, PTX2, PEDEMA, DYSP = "B6.2.3(3)", "B6.2.3(4)", "2.3.10(6)", "B6.2.6(1)", "2.1.34"
CXR, CYTO, CULT, COAG = "3.2.1", "3.3.11", "3.3.9", "3.3.8"
TB, TBB, HF, LRTI, CA, ATL = "2.3.1(20)", "B6.2.2(8)", "2.3.9(5)", "B6.2.2(4)", "B6.2.4-3(2)", "B6.2.3(5)"
L17 = "คาบ 17 (Respiratory failure and Pleural disease)"

# ───────────────────────────── 1
sec("chest-thor-01", "Thoracentesis คืออะไร — ช่องเยื่อหุ้มปอดและชั้นที่เข็มผ่าน",
    "Pleural tap ใช้ได้ทั้งวินิจฉัยและรักษา · น้ำปกติ 10–20 mL · ชั้นที่เข็มผ่าน · อาการแสดงที่บอกว่ามีน้ำและควรเจาะ", 7,
"""### นิยาม (สไลด์)
**Thoracentesis** (thoracocentesis, pleural tap) = หัตถการเอา **น้ำหรืออากาศ** ออกจากช่องเยื่อหุ้มปอดด้วย **เข็มหรือสาย (catheter)** ใช้ได้สองจุดประสงค์ — **1. วินิจฉัย** (ส่งน้ำตรวจ) **2. รักษา** (ระบายให้หายหอบ)

### ช่องเยื่อหุ้มปอดปกติ (สไลด์)
- **Parietal pleura** บุผนังอก — มีหลอดเลือด systemic และ **ประสาท intercostal รับปวด** · **visceral pleura** หุ้มปอด — ไม่มีประสาทรับปวด
- น้ำปกติ **0.1–0.3 mL/kg (ราว 10–20 mL)** เป็นสารหล่อลื่นลดแรงเสียดทานขณะหายใจ
- **สร้าง** จาก capillary ของ parietal pleura ตามแรงดัน hydrostatic · **ดูดกลับ** ทาง lymphatic ของ parietal pleura เป็นหลัก
- น้ำคั่งเมื่อ **สร้าง > ดูดกลับ**: hydrostatic/oncotic เปลี่ยน (transudate) · permeability เพิ่ม (exudate) · lymphatic อุด (มะเร็ง พังผืด) — รายละเอียดกลไกเรียนใน """ + L17 + """ หัวข้อ Pleural effusion

[[fig:thr_layers]]

### ชั้นที่เข็มผ่าน (ภาพในสไลด์)
ผิวหนัง → superficial fascia/ไขมัน → **external → internal → innermost intercostal** → **parietal pleura** → ช่องที่มีน้ำ · ใต้ชั้นน้ำคือ visceral pleura และปอดที่ถูกกดแฟบ
→ ยาชาต้องไปถึง **parietal pleura** (ชั้นที่เจ็บที่สุด) และเมื่อดูดได้น้ำ **หยุดแทงลึกต่อ** เพราะชั้นถัดไปคือปอด

#### ทำไมถึงมีอาการนี้ — อาการแสดงที่พาไปสู่การเจาะ
| อาการ/สิ่งตรวจพบ | กลไก | ใช้ตัดสินใจอย่างไร |
|---|---|---|
| **หอบเหนื่อย** | น้ำดันกะบังลมให้แบน/กลับหัว กล้ามเนื้อหายใจเสียเปรียบ + ปอดถูกกดแฟบ (compressive atelectasis) | ระบายแล้วหายหอบทันที = ข้อบ่งชี้ therapeutic |
| **เคาะทึบ (stony dull)** | ชั้นน้ำไม่มีอากาศให้สั่นพ้อง | ทึบตรงไหน = มีน้ำตรงนั้น แต่ **ไม่ใช้เคาะเลือกจุดเจาะแทน US** |
| **Fremitus และเสียงหายใจลด** | น้ำกั้นและสะท้อนการสั่นออกก่อนถึงผนังอก | แยกจาก consolidation (fremitus เพิ่ม) |
| **Trachea เบี่ยงไปฝั่งตรงข้าม** | น้ำมากเพิ่มปริมาตรข้างนั้น ดัน mediastinum | ปอดขยายได้ → ระบายได้ผล |
| **Trachea ถูกดึงเข้าหาฝั่งที่ทึบ** | ปอดแฟบจากก้อนอุดหลอดลม ปริมาตรข้างนั้นลด | **อย่ารีบระบาย** — ปอดจะไม่ขยาย ความดันติดลบมาก → bronchoscopy/CT ก่อน |

[[fig:thr_shift]]

> สไลด์ใช้ภาพ "needle inserted through **intercostal space 9 in midaxillary line** during expiration" จาก atlas — ICS 9 ต่ำมาก ใกล้กะบังลม ตับ ม้าม · แนวปฏิบัติปัจจุบันให้ **อัลตราซาวด์เลือกจุด** (หัวข้อ 5)""",
["Thoracentesis = เอาน้ำ/อากาศออกจากช่องเยื่อหุ้มปอด ด้วยเข็มหรือสาย · ใช้วินิจฉัยหรือรักษา",
 "น้ำปกติ 0.1–0.3 mL/kg (10–20 mL) สร้างจาก capillary ของ parietal pleura ดูดกลับทาง lymphatic ของ parietal pleura",
 "Parietal pleura มีประสาทรับปวด → ยาชาต้องถึงชั้นนี้ · visceral pleura ไม่เจ็บ",
 "ฝ้าทั้งข้าง + trachea ถูกดึงเข้าหา = ปอดแฟบ ไม่ใช่น้ำล้วน → อย่ารีบระบาย"],
[mcq(N(1), "A medical student performs a diagnostic thoracentesis and infiltrates lidocaine only into the skin and subcutaneous tissue. The patient experiences sharp pain as the needle enters the pleural space. Which structure was inadequately anesthetized?",
     ["Parietal pleura, which is innervated by the intercostal nerves",
      "Visceral pleura, which is innervated by the intercostal nerves",
      "Visceral pleura, which is innervated by the phrenic nerve",
      "External intercostal muscle, which contains the main nociceptive fibres of the chest wall",
      "Periosteum of the rib above, which is always penetrated during insertion"], 0,
     "**Parietal pleura** รับความรู้สึกจากเส้นประสาท intercostal (ส่วนกะบังลมกลางรับจาก phrenic) จึงเจ็บแหลมเมื่อเข็มแทงผ่าน — สไลด์เขียนว่าให้ฉีดยาชา **ผิวหนัง ใต้ผิว และลงไปถึง parietal pleura** "
     "ดูดก่อนฉีดทุกครั้ง เมื่อดูดได้น้ำ = ถึงช่องแล้ว ถอยเล็กน้อยแล้วฉีดยาชาที่ pleura\n\n"
     "- *Visceral pleura* — ไม่มีประสาทรับปวด (มีแต่ autonomic) จึงไม่ใช่ต้นเหตุ ไม่ว่าจะอ้างเส้นประสาทใด\n"
     "- *External intercostal* — กล้ามเนื้อเจ็บได้แต่ไม่ใช่ชั้นที่ทำให้เจ็บแหลมตอนทะลุเข้าช่อง\n"
     "- *Periosteum* — แทงชิดขอบบนซี่โครงไม่จำเป็นต้องผ่านเยื่อหุ้มกระดูก (ถ้าชนซี่โครงให้เดินเข็มขึ้นเหนือขอบ)",
     "ยาชาต้องถึง parietal pleura · visceral pleura ไม่เจ็บ", "Pleural anatomy and anaesthesia", R("Thoracentesis layers · Local anesthesia"), [ANAT, PE]),
 mcq(N(2), "A 64-year-old smoker has progressive dyspnea and hemoptysis. Chest radiograph shows complete opacification of the left hemithorax with the trachea deviated to the LEFT. Which is the most appropriate next step?",
     ["Contrast CT chest followed by bronchoscopy to look for an endobronchial obstruction",
      "Therapeutic thoracentesis of 1.5 L to relieve dyspnea",
      "Insertion of a large-bore chest drain on suction",
      "Intravenous furosemide and repeat chest radiograph in 48 hours",
      "Talc pleurodesis to prevent reaccumulation"], 0,
     "ฝ้าทั้งข้างแต่ **trachea ถูกดึงเข้าหา** ฝั่งที่ทึบ = ปริมาตรข้างนั้น **ลดลง** → ปอดแฟบ (เช่นมะเร็งอุดหลอดลมใหญ่ — ไอเป็นเลือดในคนสูบบุหรี่) ไม่ใช่น้ำล้วน "
     "→ หาสาเหตุด้วย CT และ **bronchoscopy**\n\n"
     "- *Therapeutic thoracentesis / chest drain* — ปอดที่อุดอยู่จะไม่ขยาย การดูดน้ำ (ถ้ามี) ทำให้ความดันในช่องอกติดลบมาก แน่นอก เสี่ยง re-expansion edema และ pneumothorax ex vacuo\n"
     "- *Furosemide* — ไม่มีลักษณะหัวใจล้มเหลว\n- *Pleurodesis* — ปอดไม่ขยาย pleura ไม่แนบกัน ทำไม่ได้ผล และยังไม่มีการวินิจฉัย",
     "Trachea ถูกดัน = น้ำมาก ระบายได้ · ถูกดึงเข้าหา = ปอดแฟบ หาสิ่งอุดก่อน", "Mediastinal shift and whether to drain", R("Pleural space") + [BTSG], [PE, ATL, CXR])],
[PE, ANAT, PLEUR, DYSP], ["thr_layers", "thr_shift"])

# ───────────────────────────── 2
sec("chest-thor-02", "ข้อบ่งชี้ — diagnostic หรือ therapeutic และเมื่อไรไม่ต้องเจาะ",
    "น้ำใหม่ > 10 mm ใน decubitus/US · ไม่รู้สาเหตุ สงสัยติดเชื้อ มะเร็ง แยกหัวใจ · diagnostic 20–30 mL · therapeutic เป็นลิตร ต้องส่งตรวจด้วย", 6,
"""### Diagnostic thoracentesis (สไลด์)
- **น้ำที่ไม่รู้สาเหตุ (unexplained)**
- **สงสัยติดเชื้อ** (parapneumonic/empyema, TB)
- **สงสัยมะเร็ง**
- **แยกว่าเป็นจากหัวใจหรือไม่** ในน้ำที่เพิ่งพบ
- เงื่อนไขขนาด: **น้ำใหม่หนา > 10 mm ใน lateral decubitus view, CT หรือ US** — บางกว่านี้เจาะยาก ได้น้ำน้อย และเสี่ยงแทงปอด
- ดูดน้ำ **ปริมาณน้อย (สไลด์ 20–30 mL)** · ถ้าส่ง cytology ด้วยใช้ราว 25–50 mL ขึ้นไป (BTS)

### Therapeutic thoracentesis (สไลด์)
ทำเมื่อปริมาณน้ำทำให้ **มีอาการชัด โดยเฉพาะหอบเหนื่อย**
- **ลดอาการหอบ** (symptomatic relief of dyspnea)
- **เตรียมทำ pleurodesis**
- **ระบาย empyema หรือ hemothorax** (ส่วนใหญ่ต้องใส่ chest drain ต่อ)
- **ใส่สายระบาย (drain placement)**
- ระบาย **ปริมาณมาก (เป็นลิตร)** · **ถ้ายังไม่รู้สาเหตุ ต้องแบ่งน้ำส่วนหนึ่งส่งตรวจด้วยเสมอ** (สไลด์)

[[fig:thr_indic]]

### เมื่อไรยังไม่ต้องเจาะ (BTS 2023 · ทบทวนจาก """ + L17 + """)
- น้ำ **สองข้างเท่า ๆ กัน** ในผู้ป่วยหัวใจล้มเหลว ไม่มีไข้ ไม่เจ็บอกแบบ pleuritic → ให้ยาขับปัสสาวะแล้วดู · เจาะเมื่อ **ไม่เข้ารูปแบบ** (ข้างเดียว/ไม่เท่ากัน ไข้ เจ็บอก) หรือ **ไม่ลดหลังรักษา**
- น้ำบางมาก (< 10 mm) ที่เหตุชัดเจน → รักษาสาเหตุ ติดตาม

#### ทำไม "ข้างเดียว" ถึงน่าสงสัยกว่า "สองข้าง"
| รูปแบบ | กลไก | ความหมาย |
|---|---|---|
| สองข้าง เท่ากัน | แรงดันในหลอดเลือดสูงทั่วร่างกาย (หัวใจ ไต) หรือ albumin ต่ำ กระทบทั้งสองข้างเท่ากัน | transudate จากระบบ — รักษาที่ระบบ |
| ข้างเดียว | โรคอยู่ที่เยื่อหุ้มปอดหรือปอดข้างนั้น (ติดเชื้อ มะเร็ง PE) | exudate เฉพาะที่ — ต้องเจาะหาสาเหตุ |
| สองข้างไม่เท่ากัน / มีไข้ | มีโรคเฉพาะที่ซ้อนบนโรคระบบ | เจาะข้างที่มากกว่า |""",
["Diagnostic: unexplained · สงสัยติดเชื้อ · สงสัยมะเร็ง · แยกหัวใจ/ไม่ใช่ — น้ำใหม่ > 10 mm ใน decubitus/US/CT",
 "Diagnostic ดูดน้อย (20–30 mL ตามสไลด์) · therapeutic เป็นลิตรเมื่อหอบ",
 "Therapeutic ทุกครั้งที่ยังไม่รู้สาเหตุ ต้องแบ่งน้ำส่งตรวจด้วย",
 "หัวใจล้มเหลว น้ำสองข้างเท่ากัน ไม่มีไข้ → ยาขับปัสสาวะก่อน ไม่ต้องเจาะ"],
[mcq(N(3), "In which of the following patients is diagnostic thoracentesis LEAST necessary at presentation?",
     ["A 72-year-old with known HFrEF, small bilateral symmetrical effusions, afebrile, without chest pain, improving with diuretics",
      "A 45-year-old with fever, pleuritic chest pain and a new right-sided effusion 3 days after starting antibiotics for pneumonia",
      "A 68-year-old smoker with weight loss and a unilateral left-sided effusion",
      "A 70-year-old with heart failure and bilateral effusions, the left much larger than the right, with fever",
      "A 30-year-old with a new unilateral effusion and 1 month of evening fever and night sweats"], 0,
     "น้ำ **สองข้างเท่ากัน** ในหัวใจล้มเหลวที่ไม่มีไข้ ไม่เจ็บอก และ **ตอบสนองต่อยาขับปัสสาวะ** เข้ากับ transudate จากแรงดันหลอดเลือด → รักษาโรคหัวใจ ไม่ต้องเจาะ (BTS 2023)\n\n"
     "- *Parapneumonic ที่มีไข้ เจ็บอก* — ต้องเจาะดู pH/Gram เพื่อตัดสินใจใส่สาย (สไลด์: suspected infection)\n"
     "- *คนสูบบุหรี่ น้ำหนักลด น้ำข้างเดียว* — suspected malignancy\n"
     "- *HF แต่สองข้างไม่เท่ากัน + ไข้* — ไม่เข้ารูปแบบหัวใจล้มเหลว ต้องเจาะข้างที่มากกว่า\n"
     "- *ไข้ตอนเย็น เหงื่อออกกลางคืน* — สงสัย TB pleuritis ต้องเจาะ (lymphocyte, ADA)",
     "HF แบบทั่วไปไม่ต้องเจาะ · ผิดรูปแบบเมื่อไร เจาะเมื่อนั้น", "Indications for diagnostic thoracentesis", R("Indications") + [BTSG], [PE, HF, PFA]),
 mcq(N(4), "A 55-year-old man has pneumonia. A lateral decubitus radiograph shows free-flowing pleural fluid layering to a thickness of 6 mm. He is clinically improving on antibiotics. What is the most appropriate management of the effusion?",
     ["Continue antibiotics and monitor; the effusion is too small to sample safely",
      "Perform landmark-guided diagnostic thoracentesis at the 9th intercostal space",
      "Insert a small-bore chest drain",
      "Perform therapeutic thoracentesis to dryness",
      "Arrange medical thoracoscopy"], 0,
     "สไลด์ให้เจาะวินิจฉัยใน **น้ำใหม่ที่หนา > 10 mm ใน decubitus view/CT/US** · ชั้น 6 mm ในผู้ที่อาการดีขึ้น = uncomplicated parapneumonic ขนาดเล็ก ตอบสนองต่อยาปฏิชีวนะ "
     "เจาะแล้วได้น้ำน้อยและเสี่ยงแทงปอด → ติดตาม ถ้าโตขึ้นหรือมีไข้ต่อจึงเจาะใต้ US\n\n"
     "- *Landmark ICS 9* — ทั้งน้ำบางและไม่ใช้ US = เสี่ยงทั้งปอดและตับ/ม้าม\n- *Chest drain / ระบายหมด* — ไม่มีข้อบ่งชี้ (ไม่มี pH ต่ำ หนอง หรือเชื้อ)\n- *Thoracoscopy* — สำหรับน้ำ exudate ที่หาสาเหตุไม่ได้",
     "> 10 mm ใน decubitus = หนาพอเจาะ", "Minimum size to tap", R("Indications (> 10 mm in decubitus view)"), [PE, LRTI, CXR])],
[PE, PFA, BF, HF], ["thr_indic"])

# ───────────────────────────── 3
sec("chest-thor-03", "ข้อห้าม (relative) การเตรียม และการขอความยินยอม",
    "เลือดออกง่าย · ผิวติดเชื้อ · ไอ/สะอึกคุมไม่ได้ · ใช้เครื่องช่วยหายใจ — ทุกข้อเป็น relative · consent ต้องบอกอะไร", 7,
"""### ข้อห้าม (สไลด์ — ลายมือเขียนกำกับ **Relative**)
- **เลือดออกง่าย** — coagulopathy, thrombocytopenia หรือ **ใช้ยาต้านการแข็งตัวของเลือด**
- **Cellulitis หรือผิวหนังติดเชื้อ** ตรงจุดเจาะ
- **ไอหรือสะอึกรุนแรงที่คุมไม่ได้**
- **ผู้ป่วยที่ใช้เครื่องช่วยหายใจ**

[[fig:thr_contra]]

#### ทำไมแต่ละข้อจึงอันตราย (กลไก)
| ข้อห้าม | กลไกที่ทำให้เกิดอันตราย | ทางลดความเสี่ยง |
|---|---|---|
| เลือดออกง่าย | เข็มเฉี่ยว **intercostal artery** (แรงดัน systemic) → เลือดไหลเข้าช่องที่ความดันลบ ไม่มีอะไรกดห้าม → **hemothorax** | แก้ค่าเลือดตามความเสี่ยง · ใช้ US · เข็มเล็ก · แทงชิดขอบบนซี่โครงล่าง ห่างกระดูกสันหลัง |
| ผิวติดเชื้อ | เข็มพาเชื้อจากผิวลงไปในน้ำ ซึ่งเป็นอาหารเลี้ยงเชื้อชั้นดี → **empyema** | เลือกจุดอื่นที่ผิวปกติ (US ช่วยหา) |
| ไอ/สะอึก | ปอดและกะบังลมขยับกระตุกเข้าหาปลายเข็ม → แทงปอด **pneumothorax** · แทงตับ/ม้าม | รักษาไอ/สะอึกก่อน · ใช้สายพลาสติกปลายทู่แทนเข็มค้าง |
| เครื่องช่วยหายใจ | ความดันบวกดันอากาศออกทางรูเล็กที่ปอดทุกครั้งที่หายใจ → **tension pneumothorax** เร็ว | ผู้ชำนาญ + US · เฝ้าความดันทางเดินหายใจและ BP · เตรียม needle/chest drain |

> ค่าที่ใช้บ่อยในทางปฏิบัติ: **INR ≤ 1.5 และเกล็ดเลือด ≥ 50,000/µL** — ไม่ใช่เกณฑ์ตายตัว · การศึกษาพบว่าการเจาะใต้ US เลือดออกน้อยมาก แม้ค่าเลือดผิดปกติเล็กน้อย · ยาต้านเกล็ดเลือด/ยาต้านการแข็งตัวพิจารณางดตามความเร่งด่วนและนโยบายโรงพยาบาล (BTS 2023) — *ส่วนนี้ไม่อยู่ในสไลด์*

### เตรียมผู้ป่วย + consent (สไลด์ "Prepare and consent")
1. **ยืนยันตัวผู้ป่วย** (ชื่อ-สกุล HN) และข้างที่จะเจาะ
2. **อธิบายหัตถการและขอความยินยอม**
3. **ทบทวนการแพ้ยา** (ยาชา น้ำยาฆ่าเชื้อ) และ **ความเสี่ยงเลือดออก** (ค่าเลือด ยาที่ใช้)
4. **วัดสัญญาณชีพ** (baseline สำหรับเทียบหลังทำ)

#### Consent ต้องมีอะไรบ้าง
| หัวข้อ | สิ่งที่บอกผู้ป่วย |
|---|---|
| ทำอะไร ทำไม | เอาน้ำในช่องปอดออกด้วยเข็ม/สายเล็ก เพื่อส่งตรวจหาสาเหตุ และ/หรือให้หายเหนื่อย |
| ขั้นตอน | นั่งโน้มตัว ฉีดยาชา จะรู้สึกตึง ๆ ใช้เวลาราว 15–30 นาที ห้ามไอหรือขยับตัวแรง ๆ ระหว่างทำ — ถ้าจะไอให้บอก |
| ความเสี่ยงที่พบบ่อย | ปวดตรงที่เจาะ · ไอ แน่นอกระหว่างระบาย · หน้ามืด (vasovagal) · **ลมรั่ว (pneumothorax) — ภาวะแทรกซ้อนสำคัญที่พบบ่อยที่สุด** |
| ความเสี่ยงที่พบน้อยแต่รุนแรง | เลือดออกในช่องอก · ปอดบวมน้ำหลังขยายตัว · ติดเชื้อ · แทงโดนตับ/ม้าม |
| ทางเลือก | ไม่เจาะแล้วติดตาม · ใส่สายระบาย · ส่องกล้อง (thoracoscopy) ตามสถานการณ์ |
| บอกเมื่อมีอาการ | เหนื่อยมากขึ้น เจ็บอก ไอไม่หยุด หน้ามืด แผลมีเลือดซึม |""",
["ข้อห้ามทุกข้อเป็น relative (ลายมือในสไลด์) — ชั่งประโยชน์กับความเสี่ยง",
 "เลือดออกง่าย → hemothorax · ผิวติดเชื้อ → empyema · ไอ/สะอึก → แทงปอด · เครื่องช่วยหายใจ → tension pneumothorax",
 "ผิวตรงจุดติดเชื้อ = เลือกจุดใหม่ ไม่ใช่เจาะผ่าน",
 "Consent: บอก pneumothorax เป็นภาวะแทรกซ้อนสำคัญที่พบบ่อยที่สุด · ขั้นตอนก่อนทำ: ยืนยันตัว · consent · แพ้ยา/เลือดออก · V/S"],
[mcq(N(5), "A 58-year-old with diabetes has a large left pleural effusion and fever; empyema is suspected. There is an area of cellulitis over the left posterior lower chest wall where the effusion appears largest. What is the most appropriate approach?",
     ["Use ultrasound to find an alternative puncture site over uninfected skin, such as the mid-axillary line",
      "Puncture through the cellulitis after applying chlorhexidine twice",
      "Defer any pleural sampling until the cellulitis has completely resolved in 2 weeks",
      "Treat with antibiotics alone; pleural sampling is contraindicated",
      "Proceed with landmark-guided puncture one interspace lower than the cellulitis"], 0,
     "ผิวติดเชื้อตรงจุดเจาะเป็น **relative contraindication** — กลไกคือเข็มพาเชื้อจากผิวลงไปในน้ำ · แต่ผู้ป่วยสงสัย **empyema** ต้องได้น้ำมาดู pH/Gram เพื่อตัดสินใจใส่สาย "
     "→ ใช้ **อัลตราซาวด์หาจุดอื่นที่ผิวปกติ** (เช่นแนว mid-axillary ที่สไลด์เขียนว่าแนะนำในท่านอน)\n\n"
     "- *เจาะผ่าน cellulitis* — น้ำยาฆ่าเชื้อไม่ฆ่าเชื้อในชั้นใต้ผิว\n- *รอ 2 สัปดาห์ / ยาปฏิชีวนะอย่างเดียว* — empyema ที่ไม่ระบายจะเป็นหนองข้นมีผนังกั้น รักษายากขึ้น\n"
     "- *ต่ำลงหนึ่งช่องโดยไม่ใช้ US* — ยังใกล้บริเวณติดเชื้อ และต่ำลงเรื่อย ๆ เสี่ยงกะบังลม/ม้าม",
     "Relative contraindication = หาทางเลี่ยง ไม่ใช่ห้ามทำ", "Contraindications — skin infection", R("Contraindications (Relative)") + [BTS], [PE, PLEUR, LRTI]),
 mcq(N(6), "While consenting a patient for an ultrasound-guided thoracentesis, which complication should be explained as the most common clinically important complication?",
     ["Pneumothorax", "Re-expansion pulmonary edema", "Splenic laceration", "Air embolism", "Pleural infection (empyema)"], 0,
     "ลายมือในสไลด์ After care: **\"Common = pneumothorax\"** · อุบัติการณ์รวมราว 6% (ลดลงเมื่อใช้ US) ส่วนน้อยที่ต้องใส่สาย · กลไก: เข็มแทงปอด หรืออากาศเข้าทางระบบเปิด (ลืมปิด 3-way) หรือ ex vacuo ใน trapped lung\n\n"
     "- *Re-expansion edema* — รุนแรงแต่พบน้อย (< 1%)\n- *ม้ามฉีก / air embolism* — พบน้อยมาก (ม้าม: เจาะต่ำเกินด้านซ้าย)\n- *Empyema* — พบน้อยเมื่อทำ aseptic technique",
     "Consent: pneumothorax พบบ่อยสุด · RPE เลือดออก ติดเชื้อ พบน้อยแต่ต้องบอก", "Consent — complications", R("After care (ลายมือ: Common = pneumothorax)") + [BTS], [PTX, PE])],
[PE, PTX, HTX, COAG], ["thr_contra"])

# ───────────────────────────── 4
sec("chest-thor-04", "อุปกรณ์และท่าผู้ป่วย — นั่งโน้มตัว ทำไมน้ำไปรวมด้านหลัง",
    "อุปกรณ์ตามสไลด์ · ท่านั่งโน้มตัวไปข้างหน้า (แนว posterior/mid-scapular) · ท่านอน (mid-axillary) · ระดับที่เจาะ · ทำไมต้องมี 3-way stopcock", 6,
"""### อุปกรณ์ (สไลด์)
| อุปกรณ์ | ใช้ทำอะไร |
|---|---|
| **Thoracentesis catheter** (เข็มมีสายพลาสติกหุ้ม) | แทงด้วยเข็ม แล้วดันสายพลาสติกเข้าช่อง ถอยเข็มออก → ปลายทู่ ไม่บาดปอดเมื่อปอดขยายกลับ |
| **Syringe + needle** | ฉีดยาชา · ดูดน้ำส่งตรวจ (syringe ใหม่สำหรับ pH) |
| **Three-way stopcock + drainage tube** | สลับทางดูด/ระบาย **โดยไม่เปิดช่องอกสู่อากาศ** |
| **Evacuated container** (ขวดสุญญากาศ) | รองรับน้ำปริมาณมาก |
| **Specimen tube** | ส่งตรวจ (หัวข้อ 9) |
| **Sterile gloves · sterile cloth (ผ้าเจาะกลาง) · gauze · adhesive tape** | ปลอดเชื้อ + ปิดแผล |
| **Local anaesthesia** (1–2% lidocaine) | ชาผิวถึง parietal pleura |
| (เพิ่ม) อัลตราซาวด์ · น้ำยาฆ่าเชื้อ (chlorhexidine) · ขวด hemoculture | หาจุด · ฆ่าเชื้อ · เพาะเชื้อ |

#### ทำไมต้องมี 3-way stopcock
ความดันในช่องเยื่อหุ้มปอด **ต่ำกว่าบรรยากาศ** (ยิ่งตอนหายใจเข้า และยิ่งระบายไปมาก) → ถ้าเปิดสายทิ้งไว้ตอนเปลี่ยนกระบอก **อากาศจะถูกดูดเข้าช่องอก** = pneumothorax จากหัตถการ → ปิดทางเข้าผู้ป่วยทุกครั้งก่อนถอด syringe

### ท่าผู้ป่วย (สไลด์)
- **นั่งตัวตรง โน้มไปข้างหน้าเล็กน้อย** (แขนวางบนโต๊ะคร่อมเตียง) → เจาะแนว **posterior / mid-scapular**
- **นอนหงาย** (ลุกนั่งไม่ได้ ใน ICU) → เจาะแนว **mid-axillary line** (ลายมือ: *Recommend*) ยกแขนข้างนั้นเหนือศีรษะ

[[fig:thr_position]]

#### ทำไมต้องนั่งโน้มตัว
| ผลของท่า | กลไก | ประโยชน์ |
|---|---|---|
| น้ำไปรวมด้านหลังส่วนล่าง | น้ำอิสระไหลตามแรงโน้มถ่วงลงสู่ **posterior costophrenic recess** ซึ่งเป็นจุดต่ำสุดของช่องอกในท่านั่ง | ได้แอ่งน้ำลึกที่สุด ห่างปอด |
| ช่องซี่โครงด้านหลังกว้างขึ้น | การโค้งตัวไปข้างหน้าทำให้ซี่โครงด้านหลังถ่างออก scapula เลื่อนไปด้านข้าง | แทงผ่านช่องง่าย ไม่ชนกระดูก |
| ผู้ป่วยนิ่ง หายใจสบาย | แขนวางพักบนโต๊ะ กล้ามเนื้อไหล่ผ่อนคลาย | ลดการขยับขณะเข็มอยู่ในช่อง |

**ระดับที่เจาะ** — ต่ำกว่าขอบบนของน้ำ (ระดับที่เคาะทึบ/US) **1–2 ช่องซี่โครง** แต่ **ไม่ต่ำกว่า ICS 8–9 ด้านหลัง** เพราะกะบังลมขึ้นมาถึงตอนหายใจออก ด้านล่างคือตับ (ขวา) และม้าม (ซ้าย)""",
["อุปกรณ์หลัก: catheter-over-needle · syringe · 3-way stopcock + สาย · ขวดสุญญากาศ · หลอดส่งตรวจ · ถุงมือ/ผ้าปลอดเชื้อ · ยาชา",
 "3-way stopcock กันอากาศถูกดูดเข้าช่องอกที่ความดันลบ ตอนเปลี่ยน syringe",
 "ท่านั่งโน้มตัว → แนว posterior/mid-scapular · ท่านอน → mid-axillary (ลายมือ: Recommend)",
 "ต่ำกว่าขอบน้ำ 1–2 ช่อง แต่ไม่ต่ำกว่า ICS 8–9 ด้านหลัง (กะบังลม ตับ ม้าม)"],
[mcq(N(7), "Why is the patient positioned sitting upright and leaning slightly forward for a posterior thoracentesis?",
     ["Free fluid gravitates to the posterior costophrenic recess and the posterior intercostal spaces widen",
      "The neurovascular bundle moves to the upper border of the rib in this position",
      "It raises pleural pressure above atmospheric so air cannot enter the pleural space",
      "It allows safe blind insertion at the 10th intercostal space without imaging",
      "It prevents re-expansion pulmonary edema regardless of the volume removed"], 0,
     "ท่านั่งโน้มตัว: น้ำอิสระไหลลงไปรวม **ด้านหลังส่วนล่าง** (จุดต่ำสุด) ได้แอ่งลึก · การโค้งตัวทำให้ **ช่องซี่โครงด้านหลังกว้าง** scapula เลื่อนออก · ผู้ป่วยวางแขนพักได้นิ่ง\n\n"
     "- *NVB ย้ายตำแหน่ง* — มัดเส้นเลือดประสาทอยู่ใน costal groove ใต้ขอบล่างซี่โครงเสมอ ไม่ขึ้นกับท่า\n"
     "- *ความดันบวก* — ความดันในช่องเยื่อหุ้มปอดยังลบ จึงต้องใช้ 3-way stopcock\n- *ICS 10 แบบไม่ใช้ภาพ* — ต่ำเกิน เสี่ยงตับ/ม้าม\n- *กัน RPE* — ขึ้นกับปริมาณ/ความเร็ว/อาการ ไม่ใช่ท่า",
     "นั่งโน้มตัว = น้ำลงหลัง + ช่องซี่โครงกว้าง", "Positioning", R("Positioning · Identify location"), [ANAT, PE]),
 mcq(N(8), "During a therapeutic thoracentesis, a student disconnects the 50-mL syringe from the catheter to empty it without turning the three-way stopcock. The patient suddenly coughs and becomes breathless, and breath sounds diminish. What is the mechanism of this complication?",
     ["Subatmospheric pleural pressure draws ambient air into the pleural space through the open catheter",
      "The catheter tip lacerates the visceral pleura as the lung re-expands",
      "Positive pleural pressure forces fluid back into the alveoli",
      "Vagal stimulation from the stopcock causes bronchospasm",
      "Lidocaine diffuses into the pleural space and paralyses the diaphragm"], 0,
     "ความดันในช่องเยื่อหุ้มปอด **ติดลบเทียบบรรยากาศ** (ยิ่งตอนหายใจเข้าและหลังระบายน้ำไปแล้ว) · สายที่เปิดทิ้งไว้เป็นทางเชื่อมกับอากาศ → อากาศถูก **ดูดเข้า** = iatrogenic pneumothorax "
     "→ จึงต้อง **ปิด 3-way ก่อนถอด syringe ทุกครั้ง** (สไลด์: connect the catheter to a three-way stopcock and a drainage tube)\n\n"
     "- *สายบาดปอด* — เกิดได้ แต่โจทย์ชี้ไปที่จังหวะเปิดระบบ\n- *ความดันบวก* — ผิดทิศ\n- *Bronchospasm / ยาชาทำกะบังลมอัมพาต* — ไม่มีกลไกเช่นนั้น",
     "ความดันในช่องอกลบ → ระบบเปิด = ดูดลมเข้า", "Three-way stopcock", R("Equipment · Procedure (three-way stopcock)"), [PTX, ANAT])],
[ANAT, PE], ["thr_position"])

# ───────────────────────────── 5
sec("chest-thor-05", "อัลตราซาวด์เลือกจุดเจาะ — ดูอะไร และทำไมต้องเจาะทันที",
    "US หรือภาพถ่ายรังสียืนยันน้ำ (สไลด์) · BTS แนะนำ US ทุกครั้ง · หาแอ่ง ≥ 1 cm · ดูกะบังลมตลอดการหายใจ · มาร์กแล้วเจาะในท่าเดิม", 6,
"""### Identify location (สไลด์)
**ใช้อัลตราซาวด์หรือภาพถ่ายรังสี (X-ray) ยืนยันตำแหน่งน้ำ** ก่อนเจาะเสมอ · BTS 2023 แนะนำ **อัลตราซาวด์ทุกครั้ง** — ลดอัตรา pneumothorax การแทงโดนอวัยวะ และ dry tap

[[fig:thr_us]]

### ดูอะไรในอัลตราซาวด์
| สิ่งที่เห็น | ลักษณะ | ความหมาย |
|---|---|---|
| **น้ำ** | ช่องสีดำ (anechoic) ระหว่างผนังอกกับปอด/กะบังลม | จุดที่เจาะได้ · มี septation/เศษลอย = exudate/loculated |
| **ปอด** | เนื้อลอยไหวในน้ำ ("jellyfish") หรือเส้น pleura ที่ขยับ (lung sliding) | ต้องห่างจากแนวเข็ม |
| **กะบังลม + ตับ/ม้าม** | เส้นโค้งสว่าง ขยับขึ้นลงตามการหายใจ อวัยวะเนื้อแน่นใต้ลงไป | ดูตลอด **ทั้งหายใจเข้าและออก** — จุดที่กะบังลมขึ้นมาถึงตอนหายใจออกห้ามเจาะ |
| **เงาซี่โครง** | แถบมืดใต้ซี่โครง (acoustic shadow) | เลือกช่องระหว่างเงา |
| **ความลึก** | วัดจากผิวถึงน้ำ และความหนาของชั้นน้ำ | ชั้นน้ำ **≥ 1 cm** ตลอดการหายใจ · รู้ความลึกที่ต้องแทง |

#### ทำไมต้องเจาะในท่าเดิม ทันทีหลังมาร์ก
น้ำอิสระ ปอด และกะบังลม **เลื่อนตามท่าและการหายใจ** — ถ้ามาร์กตอนนั่งแล้วผู้ป่วยนอนลงหรือย้ายเตียง แอ่งน้ำจะไหลไปที่อื่น ปอด/ตับอาจขึ้นมาอยู่ใต้จุดที่มาร์ก → dry tap หรือแทงอวัยวะ · ดีที่สุดคือ **real-time** (ดูขณะแทง) หรือมาร์กแล้วเจาะทันทีโดยไม่ขยับตัว

> สไลด์มีลายมือ "*... = Mid-axillary (Recommend)*" ข้างตำแหน่งเจาะ — ตีความได้ว่าเน้นแนว mid-axillary สำหรับท่านอน (อ่านไม่ชัดทั้งประโยค)""",
["ยืนยันน้ำด้วย US หรือภาพถ่ายรังสีก่อนเจาะทุกครั้ง (สไลด์) · BTS แนะนำ US",
 "หาแอ่งน้ำ ≥ 1 cm ตลอดการหายใจ ไม่มีปอด/กะบังลมขึ้นมาแตะ",
 "ดูกะบังลมตอนหายใจออก — ขึ้นมาสูงสุดตอนนั้น",
 "มาร์กแล้วเจาะในท่าเดิมทันที ขยับตัว = มาร์กใหม่"],
[mcq(N(9), "Compared with a landmark (percussion-guided) approach, what is the main benefit of ultrasound guidance for thoracentesis?",
     ["Lower rates of pneumothorax and organ puncture, with fewer dry taps",
      "It eliminates the need to send fluid for analysis",
      "It allows safe removal of 3 litres at a single sitting",
      "It removes the need for informed consent",
      "It makes routine post-procedure chest radiographs mandatory"], 0,
     "อัลตราซาวด์เห็น **ความลึกของน้ำ ปอด กะบังลม และอวัยวะใต้กะบังลม** จริง ไม่ต้องเดาจากการเคาะ → ลด **pneumothorax** แทงตับ/ม้าม และ **dry tap** (BTS 2023 แนะนำใช้ทุกครั้ง · สไลด์: use ultrasound or imaging to identify fluid)\n\n"
     "- *ไม่ต้องส่งตรวจ* — US บอกลักษณะได้บ้าง (septation) แต่ไม่แทนผลแล็บ\n- *ระบาย 3 L* — ปริมาณจำกัดด้วยอาการ/ความดันในช่องอก ไม่ใช่วิธีหาจุด\n"
     "- *ไม่ต้อง consent* — ไม่เกี่ยว\n- *CXR บังคับ* — ตรงข้าม: เมื่อใช้ US ไม่มีอาการไม่ต้องถ่ายฟิล์มทุกราย",
     "US = ลด PTX + ลดแทงอวัยวะ + ลด dry tap", "Ultrasound guidance", R("Identify location") + [BTS], [PE, PTX]),
 mcq(N(10), "A pleural effusion is marked with ultrasound while the patient sits on the edge of the bed. The patient is then transferred supine to a procedure room 2 hours later and the needle is inserted at the marked spot, yielding blood-stained aspirate and right upper quadrant pain. Which principle was violated?",
     ["The puncture should be performed in the same position immediately after (or during) ultrasound marking",
      "The needle should always be inserted at the 9th intercostal space in the mid-axillary line",
      "The skin mark should be made with sterile ink only",
      "Ultrasound should be used only for loculated effusions",
      "Thoracentesis should always be done supine to avoid vasovagal reactions"], 0,
     "น้ำอิสระ ปอด และกะบังลม **เลื่อนตามท่าและเวลา** — เมื่อเปลี่ยนจากนั่งเป็นนอน น้ำไหลไปด้านหลัง กะบังลม/ตับขึ้นมาอยู่ใต้รอยมาร์ก → แทงโดน **ตับ** (ปวดชายโครงขวา น้ำเลือด) · "
     "ต้อง **มาร์กแล้วเจาะทันทีในท่าเดิม** หรือแทงภายใต้ภาพ real-time\n\n"
     "- *ICS 9 MAL เสมอ* — ภาพในสไลด์เป็น atlas ไม่ใช่กฎ · ICS 9 ต่ำ ใกล้ตับ\n- *หมึกปลอดเชื้อ* — ไม่ใช่ต้นเหตุ\n- *US เฉพาะ loculated* — ใช้ทุกราย\n- *นอนเสมอ* — ท่ามาตรฐานคือนั่งโน้มตัว",
     "มาร์กท่าไหน เจาะท่านั้น ทันที", "Ultrasound marking", R("Identify location") + [BTS], [PE, ANAT])],
[PE, ANAT, CXR], ["thr_us"])

# ───────────────────────────── 6
sec("chest-thor-06", "ขั้นตอนเจาะ — ยาชา แทงเหนือขอบบนซี่โครง และเหตุผลของ neurovascular bundle",
    "ปลอดเชื้อ · ฉีดยาชาทีละชั้นถึง parietal pleura ดูดก่อนฉีด · แทง 90° ชิดขอบบนซี่โครงล่าง · ดูดขณะแทง · เห็นน้ำแล้วดันสาย · ห่างกระดูกสันหลัง", 9,
"""### ขั้นตอน (สไลด์)
[[fig:thr_steps]]

**Antiseptic** — ล้างมือ ใส่ถุงมือปลอดเชื้อ · ทาน้ำยาฆ่าเชื้อวนจากจุดเจาะออกด้านนอก · ปูผ้าปลอดเชื้อ · ต่อ catheter กับ **three-way stopcock และสายระบาย** ไว้ก่อน

**Local anaesthesia** — ฉีดยาชาเข้า **ผิวหนัง ใต้ผิว และลึกลงไปถึง parietal pleura** · แทงเข็ม **90°** ผ่านช่องซี่โครง · **ดูดก่อนฉีดทุกครั้ง** (สไลด์: should aspirate before injection)
- ดูดได้เลือด → ปลายเข็มอยู่ในหลอดเลือด ห้ามฉีด (lidocaine เข้าหลอดเลือด → ชัก/หัวใจเต้นผิดจังหวะ) ขยับเข็ม
- ดูดได้ **น้ำเหลือง** → ถึงช่องแล้ว — **จำความลึกนี้** ถอยเล็กน้อยแล้วฉีดยาชาที่ pleura

**Catheter insertion** — แทง needle-catheter ตามแนวที่ฉีดยาชา **ขณะดูด syringe เบา ๆ** → **เห็นน้ำ** แล้วดันสายพลาสติกเข้าช่อง ถอยเข็มออก ปิด 3-way

**Drainage → catheter removal + dressing** — ดูดเก็บตัวอย่าง ระบายตามต้องการ (หัวข้อ 7) → ถอดสาย (ให้ผู้ป่วยหายใจออกหรือกลั้นหายใจตอนถอด) → ปิดแผลปลอดเชื้อ

### ทำไมต้องแทงชิด "ขอบบน" ของซี่โครงล่าง
[[fig:thr_nvb]]

#### ทำไมถึงเกิดเลือดออกและปวด — กายวิภาคของ neurovascular bundle
| ข้อเท็จจริงทางกายวิภาค | ผลต่อการเจาะ |
|---|---|
| Intercostal **vein–artery–nerve (VAN)** วิ่งใน **costal groove ใต้ขอบล่างของซี่โครงบน** ระหว่าง internal กับ innermost intercostal | แทงใต้ซี่โครง = เฉี่ยวมัดหลัก → **hemothorax** (แรงดัน systemic) + ปวดจากประสาท |
| ขอบบนของซี่โครงล่างมีเพียง **collateral branch** เล็ก ๆ | แทง **ชิดเหนือขอบบนซี่โครงล่าง** ปลอดภัยที่สุด |
| ใกล้กระดูกสันหลัง (ราว 6–10 cm จากแนวกลาง) หลอดเลือดยัง **ไม่เข้าร่อง** วิ่งคดเคี้ยวกลางช่อง และ **ผู้สูงอายุคดมากขึ้น** | **อย่าเจาะชิดกระดูกสันหลัง** — ใช้แนว mid-scapular ถึง posterior axillary |
| แทงเฉียงลงหรือขึ้น | ระยะผ่านผนังอกยาวขึ้น และเข็มอาจเลี้ยวไปใต้ซี่โครงบน — สไลด์ให้แทง **90°** กับผิว |

> ถ้าเข็มชนซี่โครง ให้ "เดิน" ปลายเข็มขึ้นตามผิวกระดูกจนพ้นขอบบน แล้วจึงแทงต่อ""",
["Antiseptic → ยาชาผิว ใต้ผิว ถึง parietal pleura → ดูดก่อนฉีดทุกครั้ง",
 "ดูดได้น้ำ = ถึงช่อง — จำความลึกไว้ ไม่แทงลึกกว่า",
 "แทง 90° ชิดขอบบนของซี่โครงล่าง เพราะ VAN อยู่ใต้ขอบล่างของซี่โครงบน",
 "ห้ามเจาะใกล้กระดูกสันหลัง — intercostal artery คดเคี้ยวกลางช่อง โดยเฉพาะผู้สูงอายุ",
 "เห็นน้ำแล้วดันสายพลาสติกเข้า ถอยเข็ม ปิด 3-way"],
[mcq(N(11), "Why should the thoracentesis needle be inserted just above the superior border of the rib below the chosen intercostal space?",
     ["The intercostal vein, artery and nerve run in the costal groove along the inferior border of the rib above",
      "The parietal pleura is thinnest at the upper border of each rib",
      "The diaphragm is attached to the inferior border of each rib",
      "The intercostal muscles are absent just above each rib",
      "Pleural lymphatic stomata are concentrated at the inferior border of each rib"], 0,
     "มัด **VAN** (vein–artery–nerve เรียงจากบนลงล่าง) วิ่งใน **costal groove ใต้ขอบล่างของซี่โครงบน** · ขอบบนของซี่โครงล่างมีเพียง collateral branch เล็ก ๆ → แทงชิดขอบบนซี่โครงล่าง = ไกลมัดหลัก ลด hemothorax และปวด\n\n"
     "- *Pleura บางกว่า* — ความหนา pleura ไม่ต่างตามแนวซี่โครง\n- *กะบังลมเกาะ* — กะบังลมเกาะซี่โครงล่าง ๆ และ xiphoid ไม่ใช่ขอบล่างทุกซี่\n"
     "- *ไม่มีกล้ามเนื้อ* — intercostal ทั้งสามชั้นคลุมทั้งช่อง\n- *Lymphatic stomata* — อยู่บน parietal pleura ส่วนล่าง/กะบังลม ไม่เกี่ยวกับการเลือกขอบซี่โครง",
     "VAN ใต้ขอบล่างซี่โครง → แทงเหนือขอบบนซี่โครงล่าง", "Neurovascular bundle", R("Thoracentesis layers") + [BTS], [ANAT, HTX]),
 mcq(N(12), "An 82-year-old undergoes thoracentesis with the needle inserted 3 cm lateral to the spinous processes, just above a rib. One hour later he is hypotensive and the effusion appears larger on ultrasound. Which anatomical fact best explains this complication?",
     ["Near the spine the intercostal artery is tortuous and lies unprotected within the intercostal space, especially in the elderly",
      "The intercostal nerve is absent near the spine, so bleeding is painless",
      "The azygos vein crosses every posterior intercostal space within 3 cm of the midline",
      "The thoracic duct runs in the costal groove posteriorly",
      "The pleural space is not present medial to the angle of the rib"], 0,
     "ใกล้กระดูกสันหลัง (ราว 6–10 cm จากแนวกลาง ก่อนถึง angle of rib) **intercostal artery ยังไม่เข้า costal groove** วิ่งคดเคี้ยวอยู่กลางช่อง และ **คดมากขึ้นตามอายุ** — แม้แทงเหนือซี่โครงก็ยังโดนได้ "
     "→ เลือดออกเข้าช่อง (hemothorax): BP ตก น้ำเพิ่ม · จึงเจาะที่แนว mid-scapular ถึง posterior axillary\n\n"
     "- *ไม่มีประสาท* — ผิด และไม่อธิบายเลือดออก\n- *Azygos* — อยู่ใน mediastinum ไม่ได้ทอดทุกช่อง\n- *Thoracic duct* — อยู่ใน posterior mediastinum ไม่อยู่ใน costal groove (ถ้าฉีกเป็น chylothorax ไม่ใช่ช็อก)\n"
     "- *ไม่มีช่อง pleura* — มีถึง paravertebral",
     "ใกล้กระดูกสันหลัง หลอดเลือดคดและไม่อยู่ในร่อง → ห้ามเจาะ", "Medial approach and bleeding", [BTS] + R("Complications (bleeding/haemothorax)"), [HTX, ANAT])],
[ANAT, PE, HTX], ["thr_steps", "thr_nvb"])

# ───────────────────────────── 7
sec("chest-thor-07", "ระบายได้เท่าไร — ขีด 1–1.5 L และกลไก re-expansion pulmonary oedema",
    "ความดันในช่องอกตกขณะระบาย · trapped lung · หยุดเมื่อแน่นอก/ไอ · ไม่เกิน ~1–1.5 L ต่อครั้ง · RPE: Starling forces เปลี่ยนสองทาง", 8,
"""### ระบายเท่าไรดี
- สไลด์: therapeutic thoracentesis ระบาย **ปริมาณมาก (เป็นลิตร)** — ไม่ได้ระบุตัวเลขสูงสุด
- แนวปฏิบัติ (BTS): ระบาย **ไม่เกินราว 1–1.5 L ต่อครั้ง** ถ้าไม่ได้วัดความดันในช่องเยื่อหุ้มปอด และ **หยุดทันทีเมื่อแน่นอก ไอไม่หยุด หรือหน้ามืด** — อาการของผู้ป่วยสำคัญกว่าตัวเลข
- ระบายด้วยแรงโน้มถ่วงหรือ syringe ช้า ๆ — **ไม่ต่อ wall suction แรง ๆ**

[[fig:thr_pressure]]

#### ทำไมผู้ป่วยแน่นอก/ไอ แล้วต้องหยุด
| อาการระหว่างระบาย | กลไก | ทำอย่างไร |
|---|---|---|
| **แน่น/ตึงหน้าอก** | ความดันในช่องเยื่อหุ้มปอดติดลบมาก ดึง pleura สองชั้นและผนังอก — มักเป็นเพราะ **ปอดขยายไม่ทัน/ขยายไม่ได้ (trapped lung)** | **หยุดระบาย** |
| **ไอ** | ปอดที่แฟบกำลังพองกลับ หลอดลมเล็กที่ปิดอยู่เปิดออก กระตุ้น cough receptor — พบบ่อยและบอกว่าปอดกำลังขยาย ถ้า **ไอไม่หยุด** = ความดันติดลบมากเกิน | หยุด หรือพักแล้วค่อยต่อช้า ๆ |
| **SpO₂ ตก หลังระบายเยอะ** | สัญญาณแรกของ re-expansion edema | หยุด ให้ O₂ ประเมิน |

### Re-expansion pulmonary oedema (RPE)
[[fig:thr_rpe]]

#### ทำไมถึงมีอาการนี้ — RPE
| อาการ | กลไก |
|---|---|
| ไอ แน่นอก หอบ ภายในไม่กี่ชั่วโมง (ส่วนใหญ่ใน 1–2 ชม. ถึง 24 ชม.) | ปอดที่แฟบนานพองกลับเร็ว → **(1) ความดันรอบ capillary ติดลบมาก** (แรงดูดจากช่องอก) เพิ่ม hydrostatic gradient **(2) reperfusion** ของปอดที่ขาดเลือด สร้างอนุมูลอิสระ/สารอักเสบ + การยืดเร็ว → **ผนัง capillary รั่ว** **(3) surfactant ต่ำ** จากการแฟบนาน |
| เสมหะเป็นฟองสีชมพู crackles | น้ำโปรตีนสูงและเม็ดเลือดแดงล้นเข้าถุงลม ผสมอากาศเป็นฟอง |
| SpO₂ ตก | ถุงลมที่ท่วมน้ำยังได้เลือด แต่ไม่ได้อากาศ = shunt |
| ฝ้าใหม่ **ข้างที่เจาะ** | กลไกเกิดเฉพาะปอดที่พองกลับ (มีรายงานสองข้างได้แต่น้อยมาก — ลายมือในสไลด์มีคำว่า *Bilateral* อ่านไม่ชัด) |

- **ปัจจัยเสี่ยง** — ปอดแฟบนาน **> 3 วัน** · ระบายมาก/เร็ว · ใช้แรงดูดสูง · อายุน้อย · pneumothorax ขนาดใหญ่ที่ระบายเร็ว
- **พบน้อย (< 1%) แต่ตายได้** · รักษาประคับประคอง: O₂ ± NIV/PEEP · ส่วนใหญ่ดีขึ้นใน 24–72 ชม. (ยาขับปัสสาวะไม่ใช่การรักษาหลักเพราะไม่ใช่น้ำเกิน)""",
["ระบาย ≤ 1–1.5 L ต่อครั้ง (BTS) — หยุดทันทีเมื่อแน่นอก ไอไม่หยุด หน้ามืด",
 "แน่นอกขณะระบาย = ความดันในช่องอกติดลบมาก มักเป็น trapped lung",
 "RPE = แรงดูดติดลบ (hydrostatic ↑) + reperfusion (permeability ↑) + surfactant ↓",
 "RPE: ไอ เสมหะฟองชมพู crackles ฝ้าใหม่ข้างที่เจาะ ภายใน 1–24 ชม.",
 "เสี่ยง: ปอดแฟบ > 3 วัน · ระบายเร็ว/มาก · แรงดูดสูง · อายุน้อย"],
[mcq(N(13), "During therapeutic thoracentesis for a malignant effusion, 900 mL has been removed when the patient develops chest tightness and a persistent cough. Vital signs are stable. What is the most appropriate action?",
     ["Stop the drainage", "Continue until 1.5 L has been removed because the safe limit has not been reached",
      "Connect the catheter to wall suction to complete drainage quickly", "Give oral codeine and continue draining",
      "Reposition the patient supine and continue draining"], 0,
     "แน่นอก + ไอไม่หยุดระหว่างระบาย = **ความดันในช่องเยื่อหุ้มปอดติดลบมาก** ปอดขยายตามไม่ทัน (พบบ่อยใน malignant effusion ที่ปอดถูกเนื้องอกรัด — trapped lung) → เสี่ยง re-expansion edema และ pneumothorax ex vacuo → **หยุด**\n\n"
     "- *ไปให้ถึง 1.5 L* — ตัวเลขเป็นขีดบนเมื่อไม่มีอาการ ไม่ใช่เป้าหมาย\n- *Wall suction* — ทำให้ความดันติดลบเร็วขึ้นอีก อันตรายที่สุด\n"
     "- *Codeine แล้วต่อ* — กดอาการเตือนแต่ไม่แก้กลไก\n- *เปลี่ยนท่าแล้วต่อ* — ไม่แก้ความดันลบ และเสี่ยงแทงปอดเมื่อน้ำย้ายที่",
     "อาการ > ตัวเลข: แน่นอก/ไอ = หยุด", "Volume limit", [BTS] + R("Therapeutic thoracentesis"), [PE, PEDEMA]),
 mcq(N(14), "A 35-year-old has had a large pleural effusion for 2 weeks. Two hours after 2.5 L is drained rapidly, he develops dyspnea, pink frothy sputum and crackles over the drained hemithorax. Which mechanism best explains this?",
     ["Increased capillary permeability from reperfusion injury of the re-expanded lung combined with a markedly negative pleural pressure",
      "Left ventricular failure caused by the sudden increase in venous return",
      "Aspiration of gastric contents during the procedure",
      "Anaphylactic reaction to lidocaine",
      "Bacterial pneumonia introduced by the catheter"], 0,
     "**Re-expansion pulmonary oedema** — ปอดที่แฟบนาน (> 3 วัน) ขาดเลือด/O₂ และ surfactant ลด · พองกลับเร็วจาก **ระบายมากและเร็ว** → **reperfusion** สร้างอนุมูลอิสระ/สารอักเสบ ผนัง capillary รั่ว (น้ำโปรตีนสูง) "
     "+ **ความดันรอบ capillary ติดลบมาก** เพิ่มแรงดันขับน้ำออก → เกิดเฉพาะ **ข้างที่ระบาย** · อายุน้อยเสี่ยงกว่า\n\n"
     "- *LV failure* — จะเป็นสองข้างและไม่มีเหตุให้หัวใจล้มเหลวฉับพลัน\n- *Aspiration* — ผู้ป่วยนั่งรู้สึกตัว ไม่มีอาเจียน\n- *Anaphylaxis* — ต้องมีผื่น หลอดลมตีบ ความดันตก ไม่ใช่ฝ้าข้างเดียว\n- *Pneumonia* — ไม่เกิดใน 2 ชั่วโมง",
     "RPE = ข้างที่ระบาย + permeability ↑ + ความดันติดลบ", "Re-expansion pulmonary oedema", [BTS] + R("Complications (Re-expansion pulmonary edema)"), [PEDEMA, PE])],
[PE, PEDEMA, DYSP], ["thr_pressure", "thr_rpe"])

# ───────────────────────────── 8
sec("chest-thor-08", "ภาวะแทรกซ้อนและ after care — แยก pneumothorax · vasovagal · hemothorax · RPE",
    "ลายมือ: Common = pneumothorax · vasovagal (bradycardia) · bleeding (tachycardia + vasoconstriction) · เฝ้า V/S SpO₂ เสียงปอด แผล · CXR เมื่อมีอาการ ไม่ต้องถ่ายทุกราย", 8,
"""### After care (สไลด์)
- **Monitor** — วัด BP ชีพจร RR SpO₂ ซ้ำ · ประเมินการหายใจ อาการเจ็บอก **เสียงหายใจ** · ดูแผลว่ามีเลือดหรือน้ำซึม
- **Chest X-ray** — **ถ่ายเมื่อสงสัยภาวะแทรกซ้อน** · **ไม่ต้องถ่ายทุกรายถ้าไม่มีอาการ** (สไลด์)
- **Wound care** — ผ้าปิดแผลสะอาดแห้ง · ปวดให้ paracetamol · ก่อนกลับบ้านยืนยันว่าหายใจสบายและสัญญาณชีพคงที่

**ควรถ่าย CXR เมื่อ** — หอบ/เจ็บอก/SpO₂ ตก · ดูดได้อากาศระหว่างทำ · แทงหลายครั้ง · ผู้ป่วยใช้เครื่องช่วยหายใจ · ต้องการดูปอดหลังระบาย (หาก้อนที่ถูกน้ำบัง) *(เกณฑ์ตาม BTS/ACCP — ไม่อยู่ในสไลด์)*

### ภาวะแทรกซ้อน (สไลด์ + ลายมือ)
- **Pneumothorax** — ลายมือ "**Common**" · ตรวจพบ **hyperresonance** เสียงหายใจลด
- **Vasovagal reaction** — ลายมือ "**Bradycardia**" BP drop
- **Bleeding / haemothorax** — ลายมือ "pulse ↑ **tachycardia** · (vaso)**constrict**"
- **Re-expansion pulmonary oedema** (หัวข้อ 7)
- อื่น ๆ: ปวด/pleuritic chest pain + ไอ (ลายมือ) · ติดเชื้อ · แทงตับ/ม้าม · ยาชาเป็นพิษ

[[fig:thr_comp]]

#### ทำไมถึงมีอาการนี้ — แยกภาวะแทรกซ้อนจากกลไก
| ภาวะ | กลไก | สิ่งที่ตรวจพบ (ใช้แยก) | จัดการ |
|---|---|---|---|
| **Vasovagal** | ความกลัว/ปวด/เข็มกระตุ้น pleura → **vagal (parasympathetic) ทำงานเด่น** → หัวใจเต้นช้า + หลอดเลือดขยาย | **HR ช้า** BP ตก ซีด เหงื่อ หน้ามืด · **ปอดฟังเหมือนเดิม** | หยุดชั่วคราว นอนราบยกขา · atropine 0.5–1 mg IV ถ้าไม่ดีขึ้น |
| **Pneumothorax** | เข็มแทงปอด / อากาศเข้าทางระบบเปิด / ex vacuo ใน trapped lung | หอบ **HR เร็ว** SpO₂ ตก · **เคาะโปร่ง (hyperresonance)** เสียงหายใจหาย | CXR/US · เล็กไม่มีอาการ → สังเกต · ใหญ่/มีอาการ → ระบาย · **ex vacuo ไม่ต้องใส่สาย** (ไม่มีรูรั่ว) |
| **Hemothorax** | แทงโดน intercostal artery → เสียเลือด → baroreceptor กระตุ้น sympathetic | **HR เร็ว** หลอดเลือดหด มือเย็น BP ตกตามมา · **ทึบเพิ่ม** น้ำที่ดูดกลายเป็นเลือด Hb ตก | Hct น้ำ · chest drain ขนาดใหญ่ · แก้ค่าเลือด · ปรึกษาศัลยแพทย์/embolization |
| **RPE** | หัวข้อ 7 | ไอ เสมหะฟองชมพู **crackles ข้างที่เจาะ** SpO₂ ตก | O₂ ± NIV |
| **Tension pneumothorax** (ใช้เครื่องช่วยหายใจ) | ความดันบวกดันอากาศเข้าช่องทุกครั้งที่หายใจ ทางออกไม่มี | peak pressure สูง BP ตก trachea เบี่ยงออก | **needle/finger decompression ทันที ห้ามรอฟิล์ม** |""",
["Pneumothorax = ภาวะแทรกซ้อนที่พบบ่อยที่สุด (ลายมือ: Common) — เคาะโปร่ง เสียงหายใจหาย",
 "Vasovagal: HR ช้า + BP ตก + ปอดปกติ → นอนยกขา ± atropine",
 "Hemothorax: HR เร็ว + หลอดเลือดหด + ทึบเพิ่ม/น้ำเป็นเลือด → Hct น้ำ + chest drain",
 "CXR หลังเจาะเฉพาะเมื่อมีอาการ/ดูดได้ลม/แทงหลายครั้ง/ใส่เครื่องช่วยหายใจ — ไม่ต้องทุกราย (สไลด์)",
 "Pneumothorax ex vacuo จาก trapped lung ไม่มีรูรั่ว ไม่ต้องใส่สาย"],
[mcq(N(15), "Thirty minutes after a diagnostic thoracentesis performed 4 cm from the spine, a 76-year-old has heart rate 118/min, blood pressure 92/60 mmHg and cool peripheries. Dullness has extended higher on the tapped side, and a repeat aspirate is frankly bloody. Breath sounds are reduced but the percussion note is not hyperresonant. What is the most likely diagnosis?",
     ["Hemothorax from intercostal artery injury", "Vasovagal reaction", "Iatrogenic pneumothorax",
      "Re-expansion pulmonary oedema", "Local anaesthetic systemic toxicity"], 0,
     "**ชีพจรเร็ว + มือเย็น (sympathetic ตอบสนองต่อการเสียเลือด) + ทึบสูงขึ้น + น้ำกลายเป็นเลือด** หลังเจาะใกล้กระดูกสันหลังในผู้สูงอายุ (intercostal artery คดเคี้ยว) = **hemothorax** → วัด Hct น้ำ ใส่ chest drain ขนาดใหญ่ แก้ไขการเสียเลือด\n\n"
     "- *Vasovagal* — ชีพจร **ช้า** ไม่ใช่เร็ว และน้ำไม่เพิ่ม (ลายมือในสไลด์: vasovagal = bradycardia)\n- *Pneumothorax* — เคาะ **โปร่ง** ไม่ใช่ทึบเพิ่ม\n"
     "- *RPE* — ไอ เสมหะฟองชมพู crackles หลังระบายเยอะ ไม่ใช่หลังเจาะวินิจฉัย\n- *ยาชาเป็นพิษ* — ชารอบปาก ชัก หัวใจเต้นผิดจังหวะ ไม่ทำให้ทึบเพิ่ม",
     "ชีพจรเร็ว + ทึบเพิ่ม = เลือด · ชีพจรช้า = vagal · โปร่ง = ลม", "Complications — hemothorax", R("After care (ลายมือ: tachycardia, vasoconstrict) · Complications"), [HTX, PE]),
 mcq(N(16), "In which situation is a chest radiograph after thoracentesis MOST clearly indicated?",
     ["Air was aspirated during the procedure and the patient now has new dyspnea",
      "An asymptomatic patient after a single-pass, ultrasound-guided diagnostic tap",
      "To document the volume of fluid removed for the medical record",
      "Routinely before discharge in every patient regardless of symptoms",
      "To check whether the dressing is correctly applied"], 0,
     "สไลด์: **ถ่าย X-ray เมื่อสงสัยภาวะแทรกซ้อน** · **ไม่ต้องถ่ายประจำถ้าไม่มีอาการ** · ดูดได้อากาศ + หอบใหม่ = สงสัย pneumothorax ชัดเจน\n\n"
     "- *ไม่มีอาการ แทงครั้งเดียวใต้ US* — ไม่ต้องถ่าย (โอกาสพบ pneumothorax ที่ต้องรักษาต่ำมาก)\n- *บันทึกปริมาณ / ถ่ายทุกราย / ดูผ้าปิดแผล* — ไม่ใช่ข้อบ่งชี้",
     "CXR เมื่อมีอาการหรือมีเหตุสงสัย ไม่ใช่ทุกราย", "Post-procedure CXR", R("After care (Chest X-ray)"), [CXR, PTX])],
[PE, PTX, PTX2, HTX, CXR], ["thr_comp"])

# ───────────────────────────── 9
sec("chest-thor-09", "เก็บสิ่งส่งตรวจ — หลอดไหนตรวจอะไร และทำไม pH ต้องใช้ syringe blood gas",
    "แบ่งน้ำห้าทาง · ส่งเลือดคู่ · pH: syringe heparin ไล่ลม ส่งทันที · ฟองอากาศ pH สูงปลอม · lidocaine/heparin เกิน pH ต่ำปลอม · หนองชัดไม่ต้องวัด pH", 7,
"""### หลอดส่งตรวจ (ชนิดหลอดเป็นแนวปฏิบัติทั่วไป — สไลด์ระบุเพียง specimen tube)
[[fig:thr_tubes]]

| ส่งตรวจ | ภาชนะ | หมายเหตุ/เหตุผล |
|---|---|---|
| **pH** | **syringe heparin แบบ blood gas** | ไล่ลมหมด ปิดจุก ส่งเครื่อง blood gas ทันที (ถ้าช้าใส่น้ำแข็ง) |
| **Cell count + differential** | **EDTA (จุกม่วง)** | EDTA จับแคลเซียม กันน้ำที่มี fibrinogen แข็งตัวจนนับเซลล์ไม่ได้ |
| **Protein · LDH · glucose · albumin** (+ amylase, TG/cholesterol, ADA ตามข้อสงสัย) | ขวด/หลอดปลอดเชื้อ (glucose อาจใช้หลอด fluoride) | **ส่ง serum protein, LDH, glucose, albumin พร้อมกัน** เพื่อคำนวณอัตราส่วน |
| **Gram stain + culture** | ขวดปลอดเชื้อ **+ ขวด hemoculture (aerobic/anaerobic)** | ใส่ขวด hemoculture ข้างเตียงเพิ่มโอกาสพบเชื้อ |
| **AFB, TB culture, Xpert** | ขวดปลอดเชื้อ | เชื้อ TB ในน้ำมีน้อย → ADA ช่วยมากกว่า |
| **Cytology** | ภาชนะใหญ่ | **≥ 25–50 mL** — ส่งมากกว่านี้เพิ่มผลไม่มาก · ครั้งที่สองเพิ่มโอกาสพบ |

### pH — ทำไมต้องเก็บแบบ blood gas
น้ำในช่องเยื่อหุ้มปอดปกติเป็นด่าง (**pH ~7.6**) · ใน parapneumonic effusion **pH < 7.2 = ต้องใส่สายระบาย** — ค่าห่างกันไม่กี่ทศนิยมเปลี่ยนการรักษา จึงต้องวัดด้วยเครื่อง blood gas (ไม่ใช้กระดาษ litmus หรือ pH meter ของห้องแล็บทั่วไป)

[[fig:thr_ph]]

#### ทำไมค่า pH ถึงเพี้ยน
| สาเหตุ | กลไก | ผลต่อการตัดสินใจ |
|---|---|---|
| **ฟองอากาศในกระบอก** | pCO₂ ในอากาศ ≈ 0 → CO₂ จากน้ำแพร่ออก (CO₂ + H₂O ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻ เลื่อนไปทางซ้าย) → H⁺ ลด | **pH สูงปลอม** → พลาด complicated parapneumonic/empyema |
| **Lidocaine ปน** (ใช้ syringe เดียวกับยาชา) | สารละลาย lidocaine เป็นกรด | **pH ต่ำปลอม** → ใส่สายโดยไม่จำเป็น |
| **Heparin มากเกิน** | heparin เป็นกรด + เจือจาง | pH ต่ำปลอม |
| **ทิ้งไว้นานที่อุณหภูมิห้อง** | เซลล์/แบคทีเรียในหลอดยังเผาผลาญ glucose → สร้างกรด | pH ต่ำ + glucose ต่ำปลอม |

> **หนองชัด → ไม่ต้องวัด pH** (มีข้อบ่งชี้ใส่สายอยู่แล้ว และหนองทำเครื่อง blood gas เสีย) · ถ้าวัด pH ไม่ได้ ใช้ **glucose < 72 mg/dL (4 mmol/L)** แทนในบริบท parapneumonic (BTS 2023)""",
["pH ใส่ syringe heparin แบบ blood gas ไล่ลมหมด ส่งทันที — ไม่ใช้ syringe ที่ฉีดยาชา",
 "ฟองอากาศ → CO₂ หนี → pH สูงปลอม (พลาด empyema) · lidocaine/heparin เกิน → pH ต่ำปลอม",
 "Cell count ใส่ EDTA · ชีวเคมี + เจาะเลือดคู่ (protein, LDH, glucose, albumin)",
 "Culture: ใส่ขวด hemoculture ข้างเตียงด้วย · cytology ≥ 25–50 mL",
 "หนองชัดไม่ต้องวัด pH · ไม่มีเครื่องใช้ glucose < 72 mg/dL"],
[mcq(N(17), "Which is the correct way to collect and analyse pleural fluid for pH?",
     ["Draw fluid anaerobically into a heparinised blood gas syringe, expel air, cap it and analyse promptly in a blood gas analyser",
      "Send fluid in a plain tube with the biochemistry samples for measurement with a laboratory pH meter",
      "Use the syringe that contained lidocaine to avoid an additional puncture",
      "Collect in an EDTA tube to prevent clotting and measure with litmus paper",
      "Leave the sample at room temperature until all other tests are completed"], 0,
     "pH ของน้ำต้องวัด **แบบ blood gas**: syringe heparin ไม่มีอากาศ ปิดจุก ส่งทันที (ช้าให้แช่น้ำแข็ง) — ค่าจุดตัด 7.2 ต้องการความแม่นระดับทศนิยม\n\n"
     "- *หลอดเปล่า/pH meter* — สัมผัสอากาศ CO₂ หนี pH สูงปลอม\n- *Syringe ที่มี lidocaine* — lidocaine เป็นกรด pH ต่ำปลอม\n"
     "- *EDTA + litmus* — EDTA เปลี่ยนค่า และกระดาษ litmus หยาบเกินไป\n- *ทิ้งไว้* — เซลล์ยังสร้างกรด pH ต่ำปลอม",
     "pH = blood gas syringe · ไม่มีลม · ส่งทันที", "pH sampling", [BTSG], [PFA, BF]),
 mcq(N(18), "A pleural fluid sample from a patient with pneumonia was sent for pH with a large air bubble left in the syringe. The reported pH is 7.34. What is the main concern with this result?",
     ["Loss of CO2 into the air bubble may have falsely raised the pH, so a complicated parapneumonic effusion could be missed",
      "Air contamination always falsely lowers pH, so the true pH is higher",
      "The result is reliable because pH is unaffected by air exposure",
      "The pH is falsely high because heparin is alkaline",
      "Air exposure raises pleural glucose, making the fluid look less infected"], 0,
     "ฟองอากาศมี pCO₂ เกือบศูนย์ → CO₂ แพร่ออกจากน้ำ สมการ CO₂ + H₂O ⇌ H⁺ + HCO₃⁻ เลื่อนไปทางซ้าย H⁺ ลด → **pH สูงปลอม** · ค่า 7.34 จึงอาจปิดบัง pH จริง < 7.2 ที่ต้องใส่สาย → เก็บใหม่ให้ถูกวิธี\n\n"
     "- *อากาศทำให้ pH ต่ำ* — ผิดทิศ\n- *ไม่มีผล* — ผิด\n- *Heparin เป็นด่าง* — heparin เป็นกรด ทำให้ pH ต่ำปลอมเมื่อมากเกิน\n- *Glucose เพิ่ม* — อากาศไม่เพิ่ม glucose",
     "ฟองอากาศ = pH สูงปลอม = พลาด empyema", "pH artefacts — air", [BTSG], [PFA, LRTI]),
 mcq(N(19), "A patient with a resolving pneumonia has clear, straw-coloured pleural fluid: glucose 98 mg/dL, LDH 160 U/L, Gram stain negative, but pH 7.12. On review, the pH sample was drawn into the same syringe used to infiltrate lidocaine. What is the best next step?",
     ["Repeat the pH measurement on a properly collected sample before deciding on chest drainage",
      "Insert a chest drain immediately because pH is below 7.2",
      "Start intrapleural tPA and DNase",
      "Refer for video-assisted thoracoscopic decortication",
      "Diagnose rheumatoid pleuritis because pH is low with normal glucose"], 0,
     "ผลอื่นทั้งหมดบอก **uncomplicated** (ใส glucose ปกติ LDH ต่ำ Gram ลบ) ขัดกับ pH 7.12 · **lidocaine เป็นกรด** ทำให้ pH ต่ำปลอม → เก็บใหม่ด้วย syringe heparin ใหม่ก่อนตัดสินใจ\n\n"
     "- *ใส่สายทันที* — ตัดสินจากค่าปลอม ผู้ป่วยได้หัตถการไม่จำเป็น\n- *tPA/DNase, VATS* — สำหรับ empyema ที่ระบายไม่ออก\n- *Rheumatoid* — glucose ต้องต่ำมาก (< 30) ไม่ใช่ปกติ",
     "ผลขัดกัน → สงสัย preanalytic error ก่อน", "pH artefacts — lidocaine", [BTSG], [PFA, LRTI])],
[PFA, BF, CULT, CYTO], ["thr_tubes", "thr_ph"])

# ───────────────────────────── 10
sec("chest-thor-10", "อ่านผลขั้น 1–3 — ดูด้วยตา · Light's criteria · cell count",
    "Step 1 รูปลักษณ์ · Step 2 Light's (ทบทวนเร็ว + false exudate albumin gradient > 1.2) · Step 3 neutrophil/lymphocyte/eosinophil บอกกลไก", 9,
"""### โครงอ่านผลห้าขั้น (สไลด์)
[[fig:thr_stepwise]]

### Step 1 — Gross appearance
[[fig:thr_appear]]
- สไลด์แสดงภาพ **turbid** และ **high lipid-rich effusion** (ลายมือ: **milky white**)
- ขุ่นจาก **เซลล์** (หนอง) หรือ **ไขมัน** (chyle) → **ปั่น**: ส่วนบนใสขึ้น = เซลล์ · ยังขุ่น = ไขมัน (หัวข้อ 11)
- **หนองชัดหรือเหม็น** = empyema ใส่สายได้เลย ไม่ต้องรอผล
- **แดง** — RBC เพียง 5,000–10,000/µL ก็ดูแดงแล้ว → ตัดสินด้วย **Hct** ไม่ใช่ตา

### Step 2 — Light's criteria (ทบทวนเร็ว · รายละเอียดใน """ + L17 + """)
[[fig:thr_light]]

**Exudate ถ้าเข้า ≥ 1 ข้อ · transudate ถ้าไม่เข้าเลย** (สไลด์)
1. Pleural protein / serum protein **> 0.5**
2. Pleural LDH / serum LDH **> 0.6**
3. Pleural LDH **> 2/3 ของค่าสูงสุดปกติ (ULN) ของ serum LDH**

**Suspected false exudate** (สไลด์) — ผู้ป่วยหัวใจล้มเหลวที่ได้ยาขับปัสสาวะ ค่าเกินเกณฑ์เล็กน้อย → **serum albumin − pleural albumin > 1.2 g/dL ยืนยัน transudate**

#### ทำไม Light's ถึงแยกได้ และทำไมมี false exudate
| ข้อเท็จจริง | กลไก |
|---|---|
| Transudate โปรตีน/LDH ต่ำ | ผนัง capillary ปกติ กรองแต่น้ำและโมเลกุลเล็กออกมาตามแรง Starling |
| Exudate โปรตีน/LDH สูง | ผนังอักเสบรั่ว โปรตีนหลุดตามมา + เซลล์อักเสบ/มะเร็งตายปล่อย LDH + lymphatic อุดจนโปรตีนค้าง |
| False exudate ในผู้ได้ยาขับปัสสาวะ | ยาขับดูดน้ำกลับเร็วกว่าโปรตีนและ LDH → น้ำที่เหลือ **เข้มข้นขึ้น** จนเกินเกณฑ์ ทั้งที่กลไกยังเป็น Starling |
| Albumin gradient ใช้แก้ได้ | วัด "ส่วนต่าง" ไม่ใช่ "อัตราส่วน" — ความเข้มข้นที่เพิ่มขึ้นทำให้ส่วนต่างลดไม่มาก ยังกว้าง > 1.2 ใน transudate |

### Step 3 — Cell count และ differential
[[fig:thr_cell]]
*(ตาราง Step 3 ในสไลด์เป็นภาพ อ่านไม่ได้ — สรุปจากตำรา/BTS 2023)*

| ผล | กลไก | นึกถึง |
|---|---|---|
| WBC < 1,000/µL | ไม่มีการอักเสบ | transudate |
| WBC > 10,000/µL, **neutrophil** เด่น | การอักเสบเฉียบพลันดึง neutrophil | **parapneumonic/empyema**, pancreatitis, PE, TB ระยะแรก |
| **Lymphocyte > 50%** | การอักเสบเรื้อรัง/cell-mediated immunity | **TB**, มะเร็ง, lymphoma, chylothorax, หลัง CABG |
| Lymphocyte + **mesothelial < 5%** | fibrin คลุมผิว pleura ในวัณโรค mesothelial หลุดลงน้ำน้อย | สนับสนุน TB |
| **Eosinophil > 10%** | อากาศหรือเลือดในช่องกระตุ้น eosinophil | **หลังเจาะซ้ำ/pneumothorax**, hemothorax, ยา, พยาธิ, EGPA, asbestos |""",
["ห้าขั้น: ตา → Light's → cell → pH/glucose/LDH → ตรวจพิเศษ",
 "Light's: protein ratio > 0.5 · LDH ratio > 0.6 · LDH > 2/3 ULN — เข้าข้อเดียวก็ exudate",
 "False exudate (HF + ยาขับปัสสาวะ) → albumin เลือด − น้ำ > 1.2 g/dL = transudate",
 "Neutrophil = เฉียบพลัน (parapneumonic) · lymphocyte = เรื้อรัง (TB มะเร็ง) · eosinophil = มีลม/เลือดในช่อง",
 "น้ำแดงตัดสินด้วย Hct ไม่ใช่ตา"],
[mcq(N(20), "A 78-year-old with chronic heart failure on furosemide 80 mg/day has a right pleural effusion. Pleural protein 3.6 g/dL (serum 6.4), pleural LDH 120 U/L (serum 260; upper limit of normal 250). Serum albumin 3.4 g/dL, pleural albumin 1.9 g/dL. How should this effusion be classified?",
     ["Transudate from heart failure; Light's criteria are falsely positive because of diuresis",
      "Exudate; malignancy must be excluded with cytology and CT",
      "Exudate due to tuberculous pleuritis",
      "Transudate due to hypoalbuminaemia",
      "Chylothorax"], 0,
     "Light's: protein 3.6/6.4 = **0.56 (> 0.5 เข้าเกณฑ์)** · LDH 120/260 = 0.46 · 120 < 2/3 × 250 (167) → เข้า **ข้อเดียวแบบก้ำกึ่ง** ในผู้ได้ยาขับปัสสาวะ = สงสัย **false exudate** "
     "→ albumin gradient 3.4 − 1.9 = **1.5 g/dL (> 1.2)** = transudate จริงจากหัวใจล้มเหลว (สไลด์ Step 2)\n\n"
     "- *Exudate → cytology/CT* — ไม่จำเป็นเมื่อ gradient ยืนยัน transudate\n- *TB* — ไม่มีข้อมูล lymphocyte/ADA และกลไกไม่ใช่\n"
     "- *Hypoalbuminaemia* — albumin 3.4 ไม่ต่ำพอที่จะทำให้น้ำคั่ง\n- *Chylothorax* — ต้องขาวขุ่น TG > 110",
     "ก้ำกึ่ง + ยาขับปัสสาวะ → albumin gradient > 1.2 = transudate", "False exudate", R("Step two: Light's criteria (suspected false exudate)"), [PFA, HF, PE]),
 mcq(N(21), "A patient with a malignant effusion has had two therapeutic thoracenteses in the past 3 weeks; a small pneumothorax occurred after the second. Fluid from a third tap shows 18% eosinophils. What is the most likely explanation for the eosinophilia?",
     ["Air and blood introduced into the pleural space by the previous procedures",
      "Strongyloides hyperinfection",
      "Eosinophilic granulomatosis with polyangiitis",
      "Drug reaction to lidocaine",
      "Tuberculous pleuritis"], 0,
     "**Eosinophil > 10%** ในน้ำ สาเหตุที่พบบ่อยที่สุดคือ **มีอากาศหรือเลือดในช่องเยื่อหุ้มปอด** — หลังเจาะซ้ำ pneumothorax หรือ hemothorax ซึ่งกระตุ้นการหลั่ง IL-5 ดึง eosinophil มา · ไม่ได้แปลว่ามีโรคใหม่\n\n"
     "- *พยาธิ / EGPA / ยา* — เป็นสาเหตุได้แต่พบน้อย ต้องมีหลักฐานอื่น (eosinophil ในเลือดสูง หอบหืด หลอดเลือดอักเสบ ยาใหม่)\n- *Lidocaine* — ไม่ใช่สาเหตุที่รู้จัก\n- *TB* — lymphocyte เด่น eosinophil น้อยมาก",
     "Eosinophilic effusion: ถามก่อนว่าเคยเจาะ/มีลม/มีเลือดไหม", "Cell differential — eosinophils", R("Step three: cell count & differential") + [BTSG], [PFA, PTX])],
[PFA, BF, PE, HF], ["thr_stepwise", "thr_appear", "thr_light", "thr_cell"])

# ───────────────────────────── 11
sec("chest-thor-11", "อ่านผลขั้น 4–5 — pH glucose LDH และการตรวจพิเศษ (ADA · cytology · TG · Hct · amylase · culture)",
    "pH < 7.2 / glucose < 60 / LDH > 1,000 · ADA > 40 ใน lymphocytic = TB · TG > 110 chylothorax · cholesterol > 200 pseudochylothorax · Hct ≥ 50% hemothorax · amylase · cytology ~60%", 10,
"""### Step 4 — pH · glucose · LDH
[[fig:thr_lowglu]]

| ค่า | จุดตัด | ความหมาย |
|---|---|---|
| **pH** | **< 7.2** | ใน parapneumonic = complicated → **ใส่สายระบาย** · อื่น ๆ: RA, TB, มะเร็ง (พยากรณ์แย่ pleurodesis ไม่ติด), หลอดอาหารแตก (~6) |
| **Glucose** | **< 60 mg/dL (3.3 mmol/L)** หรือน้ำ/เลือด < 0.5 | empyema · **rheumatoid (< 30)** · TB · มะเร็ง · Boerhaave · lupus |
| **LDH** | **> 1,000 U/L** | อักเสบรุนแรง เซลล์ตายมาก — empyema, RA |

ลายมือใน Step 4: *rheumatoid · complicated parapneumonic effusion · Boerhaave syndrome · pH ↓ parapneumonic* — ตรงกับรายการข้างบน (ตารางในสไลด์เป็นภาพ — จุดตัดอิง BTS 2023/ตำรา)

### Step 5 — Special tests
| การตรวจ | ผล | นึกถึง + กลไก |
|---|---|---|
| **ADA** | **> 40 U/L** ใน lymphocytic exudate | **TB pleuritis** — T cell ที่ถูกกระตุ้นจากปฏิกิริยา delayed hypersensitivity สร้าง ADA · ในไทยที่ TB ชุก เริ่มยาได้เลย (ดูคาบ EPTB) · ADA สูงปลอม: empyema (neutrophil), lymphoma, RA · **ADA ต่ำ (Case 1: 2.5) ช่วยตัด TB** |
| **Cytology** | พบเซลล์มะเร็ง | **malignant effusion** (ลายมือ: *→ Malignancy*) · ไวราว 60% ครั้งแรก ส่งครั้งที่สองเพิ่มขึ้น · ลบไม่ตัดมะเร็ง → biopsy/thoracoscopy |
| **Triglyceride** | **> 110 mg/dL** | **chylothorax** — chylomicron จาก thoracic duct ที่ฉีก · < 50 แทบตัดออก · 50–110 ส่ง lipoprotein electrophoresis |
| **Cholesterol** | **> 200 mg/dL**/ผลึก cholesterol + TG ต่ำ | **pseudochylothorax** — น้ำค้างนานในเยื่อหุ้มหนา (TB เก่า RA) |
| **Hematocrit** | **น้ำ/เลือด ≥ 0.5** | **hemothorax** → chest drain ขนาดใหญ่ |
| **Amylase** | สูงกว่า ULN ในเลือด / น้ำ/เลือด > 1 | **pancreatitis/pseudocyst** (ลายมือ: *Pancreas*) · **หลอดอาหารแตก** (salivary amylase + pH ต่ำมาก) · มะเร็งบางชนิด |
| **Gram stain / culture** | บวก | complicated parapneumonic/empyema → ใส่สาย · Case 1: ไม่พบเชื้อ culture ไม่ขึ้น 3 วัน |
| (เพิ่ม) NT-proBNP ในเลือด | สูงมาก | สนับสนุนหัวใจล้มเหลว (false exudate) |
| (เพิ่ม) Creatinine น้ำ/เลือด > 1 | | urinothorax (transudate ที่ pH ต่ำ) |

[[fig:thr_chylo]]

[[fig:thr_hct]]

#### ทำไมถึงมีอาการนี้ — ลักษณะเฉพาะของน้ำแต่ละชนิด
- **Chylothorax ขาวเหมือนนม** — chyle จากลำไส้มีไขมันในรูป chylomicron (TG สูง) ไหลผ่าน thoracic duct ซึ่งทอดผ่าน posterior mediastinum → ฉีกจากมะเร็ง/lymphoma ผ่าตัด บาดเจ็บ → chyle เข้าช่องอก · ไขมันไม่ตกตะกอนเมื่อปั่น · ไม่ระคายเคืองจึงมักไม่มีไข้
- **Pseudochylothorax** — น้ำที่ค้างหลายปีในช่องที่เยื่อหุ้มหนาจนระบายไม่ได้ เซลล์สลายปล่อย cholesterol สะสมเป็นผลึก (TB เก่า RA)
- **Hemothorax** — เลือดในช่องอกถูกการเคลื่อนไหวของปอดและหัวใจกวนจน defibrinate ไม่ค่อยแข็งตัว จึงดูดออกได้ แต่ถ้าออกมากจะเป็นก้อน (clotted hemothorax) ต้องผ่าตัด
- **Glucose ต่ำมากใน RA** — เยื่อหุ้มปอดอักเสบหนาขัดการขนส่ง glucose จากเลือดเข้าช่อง ร่วมกับเซลล์อักเสบใช้ glucose""",
["pH < 7.2 · glucose < 60 mg/dL · LDH > 1,000 = อักเสบรุนแรง (empyema RA TB มะเร็ง Boerhaave)",
 "ADA > 40 U/L ใน lymphocytic exudate = TB pleuritis · ADA ต่ำช่วยตัด TB",
 "TG > 110 = chylothorax · cholesterol > 200 + TG ต่ำ = pseudochylothorax · ปั่นแล้วใส = หนอง",
 "Hct น้ำ/เลือด ≥ 0.5 = hemothorax → chest drain ขนาดใหญ่",
 "Amylase สูง = ตับอ่อน หรือหลอดอาหารแตก (pH ~6) · cytology ไวราว 60%"],
[mcq(N(22), "A 50-year-old treated for pulmonary tuberculosis 15 years ago has a chronic left pleural effusion with a thickened pleura. The fluid is milky. Triglyceride 42 mg/dL, cholesterol 320 mg/dL, and cholesterol crystals are seen. What is the diagnosis?",
     ["Pseudochylothorax", "Chylothorax from thoracic duct injury", "Empyema", "Hemothorax", "Malignant effusion from lymphoma"], 0,
     "ขาวขุ่น + **cholesterol > 200 + ผลึก cholesterol + TG < 50** ในน้ำเรื้อรังหลายปีที่เยื่อหุ้มหนา (TB เก่า) = **pseudochylothorax** — เซลล์สลายสะสม cholesterol เพราะระบายไม่ได้\n\n"
     "- *Chylothorax* — TG > 110 (มี chylomicron) cholesterol มักต่ำ เกิดเร็วหลังท่อฉีก\n- *Empyema* — ขุ่นจากเซลล์ ปั่นแล้วใส pH/glucose ต่ำ\n"
     "- *Hemothorax* — แดง Hct สูง\n- *Lymphoma* — ทำให้เกิด chylothorax จริง (TG สูง) ไม่ใช่ cholesterol effusion",
     "ขาวขุ่น: TG > 110 = chylo · cholesterol > 200 + TG ต่ำ = pseudo", "Pseudochylothorax", R("Step five: special pleural fluid tests") + [BTSG], [PFA, TB, PE]),
 mcq(N(23), "After blunt chest trauma, a patient has a right effusion. Aspirated fluid is dark red. Pleural fluid haematocrit is 22% and blood haematocrit is 38%. What is the most appropriate interpretation and management?",
     ["Hemothorax (ratio about 0.58); insert a large-bore chest drain and assess ongoing bleeding",
      "Blood-stained effusion (ratio below 0.5); observe",
      "Traumatic chylothorax; start a low-fat diet",
      "Hemothorax; perform repeated therapeutic thoracentesis daily",
      "Ratio is uninterpretable because haematocrit cannot be measured in pleural fluid"], 0,
     "Hct น้ำ/เลือด = 22/38 = **0.58 (≥ 0.5)** = **hemothorax** → **chest drain ขนาดใหญ่** ระบายให้หมด (กันก้อนเลือดและพังผืด) และวัดปริมาณที่ออกต่อเนื่องเพื่อดูว่าต้องผ่าตัดไหม (สไลด์: drainage of hemothorax เป็นข้อบ่งชี้ therapeutic)\n\n"
     "- *Blood-stained* — คำนวณผิด · น้ำที่ดูแดงแต่ Hct < 1% เท่านั้นที่ถือว่าแค่เลือดปน\n- *Chylothorax* — ขาวขุ่น TG สูง\n"
     "- *เจาะซ้ำทุกวัน* — ระบายไม่หมด เลือดแข็งเป็นก้อน เสี่ยง fibrothorax/ติดเชื้อ\n- *วัดไม่ได้* — วัดได้ตามปกติ",
     "Hct น้ำ ≥ ครึ่งหนึ่งของเลือด = hemothorax → สายใหญ่", "Hemothorax — haematocrit rule", R("Therapeutic indications (hemothorax)") + [BTSG], [HTX, PFA]),
 mcq(N(24), "A 60-year-old woman with long-standing seropositive rheumatoid arthritis and subcutaneous nodules has a small unilateral exudative effusion. She is afebrile. Pleural glucose is 18 mg/dL (serum 110), pH 7.05, LDH 1,450 U/L, Gram stain and culture negative. What is the most likely cause?",
     ["Rheumatoid pleuritis", "Tuberculous pleuritis", "Malignant mesothelioma", "Pulmonary embolism", "Hepatic hydrothorax"], 0,
     "**Glucose ต่ำมาก (< 30)** + pH ต่ำ + LDH สูงมาก ในผู้ป่วย RA ที่มี nodule ไม่มีไข้ เชื้อลบ = **rheumatoid pleuritis** (ลายมือ Step 4: *Rheumatoid*) — เยื่อหุ้มอักเสบหนาขัดการขนส่ง glucose เข้าช่อง + เซลล์อักเสบใช้ glucose\n\n"
     "- *TB* — glucose ต่ำได้แต่ไม่ต่ำขนาดนี้ lymphocyte เด่น ADA สูง\n- *Mesothelioma* — glucose ต่ำได้เมื่อก้อนใหญ่ แต่ไม่ใช่ภาพนี้\n"
     "- *PE* — exudate เลือดปน glucose ปกติ\n- *Hepatic hydrothorax* — transudate",
     "Glucose < 30 + RA = rheumatoid pleuritis", "Low glucose effusion", R("Step 4: pH, glucose and LDH (ลายมือ: Rheumatoid)"), [PFA, PLEUR])],
[PFA, BF, CYTO, CULT, HTX, TB, CA], ["thr_lowglu", "thr_chylo", "thr_hct"])

# ───────────────────────────── 12
sec("chest-thor-12", "Case example — ชาย 59 ปี น้ำสองข้างจากหัวใจล้มเหลว (ไล่อ่านทีละขั้น)",
    "Case 1 ในสไลด์: HF + CKD V น้ำสองข้าง · protein 1.7/6.9 · LDH 83/308 · WBC 133 · ADA 2.5 → transudate · ฝึกอ่านเพิ่ม 4 ราย", 8,
"""### Case 1 (สไลด์) — Bilateral pleural effusion in decompensated heart failure
**ชายไทย 59 ปี** เหนื่อยมากขึ้นเรื่อย ๆ **orthopnea ปัสสาวะออกน้อย บวมทั้งตัว** (ขาสองข้าง ถุงอัณฑะบวม)
- **U/D**: DM with proliferative diabetic retinopathy · HT · DLP · **CKD stage V**
- **PE**: **S3 gallop** · crepitation ปอดสองข้าง · ตับโต · ascites เล็กน้อย · pitting edema ขาสองข้าง 3+
- **CXR**: **cardiomegaly + pleural effusion สองข้าง**

| ผลตรวจน้ำ | ค่า |
|---|---|
| ลักษณะ | **เหลือง (yellow)** |
| RBC / WBC | **200 / 133 /µL** · macrophage |
| Protein น้ำ / เลือด | **1.7 / 6.9 g/dL** |
| LDH น้ำ / เลือด | **83 / 308 U/L** |
| ADA | **2.5 U/L** |
| Gram stain | few leukocyte · ไม่พบเชื้อ |
| Culture | ไม่ขึ้นหลัง 3 วัน |

[[fig:thr_case1]]

### ไล่ห้าขั้น
1. **ตา** — เหลืองใส → เข้ากับ transudate
2. **Light's** — protein 1.7/6.9 = **0.25** (< 0.5) · LDH 83/308 = **0.27** (< 0.6) · 2/3 × 308 = **205** → 83 ต่ำกว่า → **ไม่เข้าเลย = transudate** (หมายเหตุ: สไลด์คูณ 2/3 กับ LDH ในเลือดของผู้ป่วย — เกณฑ์จริงใช้ **ULN ของห้องแล็บ** เช่น ULN 250 → 167 ผลสรุปเหมือนกัน)
3. **Cell** — WBC 133 (< 1,000) macrophage เด่น → ไม่อักเสบ
4. **pH/glucose/LDH** — LDH ต่ำ (สไลด์ไม่ได้แสดง pH/glucose)
5. **พิเศษ** — ADA 2.5 · Gram/culture ลบ → สไลด์สรุป: **WBC และ LDH ต่ำ ไม่บ่งการอักเสบมาก TB pleuritis ไม่น่าเป็น**

**สรุป (สไลด์)** — **transudative effusion เข้ากับ cardiac pleural effusion จาก decompensated heart failure**

#### ทำไมถึงมีอาการนี้ — Case 1
| อาการ/สิ่งตรวจพบ | กลไก |
|---|---|
| Orthopnea | นอนราบ เลือดจากขาไหลกลับหัวใจมากขึ้น หัวใจที่ล้มเหลวรับไม่ไหว → แรงดันในหลอดเลือดปอดสูง ปอดแข็ง หายใจลำบาก |
| S3 gallop | เลือดไหลเข้า ventricle ที่ขยายและแรงดันสูงอย่างรวดเร็วช่วงต้น diastole แล้วหยุดกะทันหัน ผนังสั่น |
| น้ำในช่องเยื่อหุ้มปอดสองข้าง | แรงดันใน **pulmonary/systemic vein สูง** → น้ำซึมออกจาก capillary ของปอดและ parietal pleura มากกว่าที่ lymphatic ระบายได้ (lymphatic ระบายลง systemic vein ที่แรงดันสูงด้วย) |
| ปัสสาวะน้อย บวมทั้งตัว | CKD V ขับน้ำ/เกลือไม่ได้ + cardiac output ต่ำ → น้ำเกินทั้งร่างกาย |

> **ประเด็นคิดต่อ** (ไม่อยู่ในสไลด์) — น้ำสองข้างแบบหัวใจล้มเหลวทั่วไปตาม BTS ไม่จำเป็นต้องเจาะตั้งแต่แรก · ใน **CKD V** ต้องนึกถึง **uremic pleuritis** (exudate มักมีเลือดปน) ด้วย — ผล transudate ในรายนี้ช่วยตัดออก · รักษา: **ลดน้ำด้วยยาขับปัสสาวะหรือ dialysis/ultrafiltration** ไม่ต้องใส่สายหรือเจาะซ้ำถ้าอาการดีขึ้น

### ฝึกอ่านเพิ่ม (ตัวอย่างประกอบ — ไม่ได้มาจากสไลด์)
| ราย | ผลน้ำ | อ่านว่า | ทำอะไรต่อ |
|---|---|---|---|
| A ชาย 28 ปี ไข้ต่ำ ๆ 1 เดือน | protein 5.4/7.2 · LDH 410 · lymphocyte 85% · **ADA 86** | exudate lymphocytic ADA สูง = **TB pleuritis** | เริ่มยาวัณโรค (ดูคาบ EPTB) |
| B หญิง 60 ปี pneumonia ไข้ไม่ลง | ขุ่น · **pH 7.02 · glucose 30** · neutrophil 90% · Gram บวก | **complicated parapneumonic/empyema** | ใส่ chest drain + ยาปฏิชีวนะ (คาบ 17) |
| C ชาย 55 ปี lymphoma | ขาวขุ่น · **TG 260 mg/dL** · lymphocyte เด่น | **chylothorax** | รักษา lymphoma · ลดไขมัน/MCT · ระบายตามอาการ |
| D หญิง 70 ปี น้ำหนักลด น้ำซ้ำเร็ว | เลือดปน · exudate · **cytology: adenocarcinoma** | **malignant effusion** | CT staging · IPC หรือ talc pleurodesis (คาบ 17) |""",
["Case 1: protein 0.25 · LDH 0.27 · LDH 83 < 2/3 → transudate = HF",
 "ADA 2.5 + WBC/LDH ต่ำ → ไม่คิดถึง TB",
 "เกณฑ์ข้อ 3 ใช้ ULN ของห้องแล็บ (สไลด์ใช้ LDH ผู้ป่วย — ผลสรุปไม่ต่าง)",
 "CKD V + น้ำ → นึกถึง uremic pleuritis ด้วย · transudate ช่วยตัดออก",
 "รักษาที่สาเหตุ: ยาขับ/dialysis ไม่ใช่เจาะซ้ำ"],
[mcq(N(25), "A patient's pleural LDH is 83 U/L and serum LDH is 308 U/L. The laboratory's upper limit of normal for serum LDH is 250 U/L. Which statement correctly applies the third Light criterion?",
     ["Compare pleural LDH with two-thirds of the laboratory upper limit of normal (about 167 U/L): 83 is below this, so the criterion is not met",
      "Compare pleural LDH with two-thirds of the patient's serum LDH (205 U/L); this is the only valid method",
      "Compare pleural LDH with the full upper limit of normal (250 U/L)",
      "The third criterion is met because serum LDH exceeds the upper limit of normal",
      "The third criterion cannot be used when serum LDH is elevated"], 0,
     "ข้อ 3 ของ Light's คือ **pleural LDH > 2/3 ของ upper limit of normal ของ serum LDH** ของห้องแล็บ → 2/3 × 250 ≈ **167** · 83 < 167 = ไม่เข้า · "
     "สไลด์ Case 1 คำนวณจาก LDH ของผู้ป่วย (2/3 × 308 = 205) ได้ข้อสรุปเดียวกัน แต่ถ้าค่า LDH น้ำอยู่ระหว่าง 167–205 วิธีของสไลด์จะเรียก exudate เป็น transudate ได้\n\n"
     "- *ใช้ ULN เต็ม* — ผิดสัดส่วน\n- *serum LDH สูงจึงเข้าเกณฑ์* — เกณฑ์ดูที่ค่าในน้ำ ไม่ใช่ในเลือด\n- *ใช้ไม่ได้เมื่อ serum สูง* — ใช้ได้ (และข้อ 2 ยังใช้อัตราส่วน)",
     "2/3 ของ ULN ห้องแล็บ ไม่ใช่ของ LDH ผู้ป่วย", "Light's criterion 3", R("Case 1 (Light's criteria)"), [PFA, PE]),
 mcq(N(26), "A 59-year-old with CKD stage 5, S3 gallop, generalized edema and bilateral pleural effusions has pleural fluid: yellow, WBC 133/µL, protein 1.7 g/dL (serum 6.9), LDH 83 U/L (serum 308), ADA 2.5 U/L, Gram stain and culture negative. What is the most appropriate management of the effusions?",
     ["Optimise fluid removal with diuretics and/or dialysis ultrafiltration and treat the heart failure",
      "Start a four-drug anti-tuberculosis regimen",
      "Insert bilateral chest drains",
      "Arrange talc pleurodesis",
      "Proceed to medical thoracoscopy with pleural biopsy"], 0,
     "ผล **transudate** (protein 0.25, LDH 0.27) WBC ต่ำ ADA ต่ำ เชื้อลบ = **cardiac effusion จาก decompensated HF** ร่วมกับน้ำเกินจาก CKD V (สไลด์ Case 1) → รักษาที่ **ภาวะน้ำเกิน/หัวใจ**: ยาขับปัสสาวะ หรือ dialysis/ultrafiltration\n\n"
     "- *ยาวัณโรค* — ADA 2.5 และ WBC ต่ำ TB ไม่น่าเป็น (สไลด์)\n- *Chest drain / pleurodesis* — transudate ที่รักษาสาเหตุได้ ไม่ต้องระบายถาวร\n- *Thoracoscopy* — สำหรับ exudate ที่หาสาเหตุไม่ได้",
     "Transudate → รักษาสาเหตุ ไม่ใช่รักษาน้ำ", "Case 1 — management", R("Case 1"), [PE, HF, PFA])],
[PE, PFA, BF, HF], ["thr_case1"])

# ───────────────────────────── MEQ / OSCE
LECNAME = "Thoracentesis with interpretation (AL กลุ่ม 5)"
MEQ = [{"id": "CH-THOR-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
        "topic": "Large right pleural effusion — thoracentesis, specimen handling and interpretation (TB pleuritis) with re-expansion symptoms",
        "nl": [PE, PFA, BF, TB, PEDEMA, ANAT], "ref": R("Indications · Procedure · Analysis and interpretation") + [BTS, BTSG],
        "vignette": "ชายไทยอายุ 34 ปี อาชีพพนักงานโรงงาน มาด้วยไข้ต่ำ ๆ ตอนเย็น ไอแห้ง และเหนื่อยมากขึ้นเรื่อย ๆ 3 สัปดาห์ น้ำหนักลด 4 กก. ไม่มีโรคประจำตัว ไม่สูบบุหรี่\n"
                    "V/S: BT 37.9 °C · BP 124/78 mmHg · PR 104/min · RR 26/min · SpO2 93% room air\n"
                    "PE: trachea เบี่ยงไปทางซ้าย · ทรวงอกขวาเคาะทึบตั้งแต่ระดับ ICS 4 ลงไป · tactile fremitus และเสียงหายใจลดลงที่ปอดขวาส่วนล่าง\n"
                    "CXR: ฝ้าทึบปอดขวา 2 ใน 3 ส่วน มี meniscus sign · mediastinum ถูกดันไปทางซ้าย\n"
                    "Lab: CBC ปกติ · platelet 260,000/µL · INR 1.0 · Anti-HIV negative",
        "questions": [
            {"q": "1. อธิบายกลไกของสิ่งตรวจพบ เคาะทึบ, fremitus ลดลง และ trachea เบี่ยงไปทางซ้าย (3 คะแนน)",
             "a": "- **เคาะทึบ** — ชั้นน้ำไม่มีอากาศให้สั่นพ้อง\n- **Fremitus/เสียงหายใจลด** — น้ำกั้นและสะท้อนแรงสั่นออกก่อนถึงผนังอก\n"
                  "- **Trachea เบี่ยงไปฝั่งตรงข้าม** — น้ำปริมาณมากเพิ่มปริมาตรข้างขวา ดัน mediastinum ไปซ้าย → บอกว่าเป็นน้ำ (ไม่ใช่ปอดแฟบ) และปอดน่าจะขยายได้เมื่อระบาย"},
            {"q": "2. ผู้ป่วยรายนี้มีข้อบ่งชี้ thoracentesis แบบใด และต้องเตรียม/ตรวจอะไรก่อนลงมือ (3 คะแนน)",
             "a": "- **ทั้ง diagnostic** (น้ำข้างเดียวไม่รู้สาเหตุ สงสัยติดเชื้อ/TB/มะเร็ง) **และ therapeutic** (หอบ RR 26 SpO2 93%) — ระบายแล้วต้องแบ่งส่งตรวจ\n"
                  "- เตรียม: ยืนยันตัว · อธิบายและขอ consent (บอก pneumothorax, เลือดออก, RPE, vasovagal) · ถามแพ้ยาชา/น้ำยา · ค่าเลือด (INR 1.0, plt ปกติ = ทำได้) · V/S baseline\n"
                  "- **อัลตราซาวด์** หาแอ่งน้ำ ≥ 1 cm ดูกะบังลมตลอดการหายใจ มาร์กแล้วเจาะในท่าเดิม"},
            {"q": "3. อธิบายท่าผู้ป่วย ตำแหน่ง และเทคนิคการแทงเข็ม พร้อมเหตุผลทางกายวิภาค (3 คะแนน)",
             "a": "- **นั่งโน้มตัวไปข้างหน้า** แขนวางบนโต๊ะ → น้ำลงไปรวมด้านหลังส่วนล่าง ช่องซี่โครงด้านหลังกว้าง\n"
                  "- แนว **mid-scapular ถึง posterior axillary** ต่ำกว่าขอบน้ำ 1–2 ช่อง ไม่ต่ำกว่า ICS 8–9 · **ไม่ชิดกระดูกสันหลัง** (intercostal artery คดเคี้ยวกลางช่อง)\n"
                  "- ยาชาทีละชั้นถึง **parietal pleura** ดูดก่อนฉีด · แทง 90° **ชิดขอบบนของซี่โครงล่าง** เพราะ **VAN อยู่ใน costal groove ใต้ขอบล่างซี่โครงบน** · ดูดขณะแทง เห็นน้ำแล้วดันสาย ถอยเข็ม ปิด 3-way"},
            {"q": "4. จงบอกการส่งตรวจน้ำ (ชนิดภาชนะ) และสิ่งที่ต้องระวังในการส่ง pH (3 คะแนน)",
             "a": "- **pH**: syringe heparin แบบ blood gas ไล่ลม ปิดจุก ส่งทันที — **ฟองอากาศ → pH สูงปลอม · lidocaine/heparin เกิน → pH ต่ำปลอม**\n"
                  "- **EDTA**: cell count + differential\n- **ขวดปลอดเชื้อ**: protein, LDH, glucose, albumin, **ADA** + เจาะเลือด protein/LDH/glucose/albumin คู่กัน\n"
                  "- **Gram/culture** + ขวด hemoculture · **AFB/TB culture/Xpert**\n- **Cytology** ≥ 25–50 mL"},
            {"q": "5. ผลตรวจน้ำ: สีเหลืองใส · protein 5.2 g/dL (serum 7.0) · LDH 420 U/L (serum 230; ULN 250) · WBC 2,800/µL lymphocyte 88% mesothelial 2% · glucose 70 mg/dL (serum 102) · pH 7.32 · ADA 82 U/L · Gram/AFB ไม่พบเชื้อ · cytology ไม่พบเซลล์มะเร็ง — จงแปลผลทีละขั้นและให้การวินิจฉัย (4 คะแนน)",
             "a": "1. **ตา**: ใสเหลือง\n2. **Light's**: protein 5.2/7.0 = **0.74 (> 0.5)** · LDH 420/230 = **1.83 (> 0.6)** · 420 > 2/3 × 250 (**167**) → **exudate**\n"
                  "3. **Cell**: lymphocyte 88% + mesothelial < 5% → lymphocytic exudate เข้ากับ TB\n4. **pH/glucose**: pH 7.32 glucose 70 — ต่ำเล็กน้อย ไม่ใช่ empyema\n"
                  "5. **ADA 82 (> 40)** + AFB ลบ (เชื้อในน้ำน้อย) + cytology ลบ\n\n→ **Tuberculous pleuritis**"},
            {"q": "6. ระหว่างระบายน้ำได้ 1,200 mL ผู้ป่วยไอไม่หยุดและแน่นหน้าอก จะทำอย่างไร ภาวะแทรกซ้อนใดที่กังวล และอธิบายกลไก (3 คะแนน)",
             "a": "- **หยุดระบายทันที** · ประเมิน V/S SpO2 ฟังปอด · ให้ O2 · CXR ถ้ามีอาการต่อ\n"
                  "- กังวล **re-expansion pulmonary oedema** (และ pneumothorax)\n"
                  "- กลไก: ปอดที่แฟบหลายสัปดาห์ขาดเลือดและ surfactant ลด → พองกลับเร็ว **ความดันในช่องอกติดลบมาก** เพิ่ม hydrostatic gradient + **reperfusion** ทำให้ capillary รั่ว → น้ำโปรตีนสูงท่วมถุงลม **ข้างที่เจาะ** · ป้องกันด้วยการหยุดเมื่อมีอาการ ไม่เกิน ~1–1.5 L ต่อครั้ง"},
            {"q": "7. วางแผนการรักษาต่อ (2 คะแนน)",
             "a": "- **ยาวัณโรค 2HRZE/4HR** (ตามแนวทางแห่งชาติ) · ส่ง sputum/induced sputum หา TB ปอดร่วม · คัดกรองผู้สัมผัส\n"
                  "- ระบายเพิ่มเฉพาะเมื่อหอบ (therapeutic) — **ไม่ต้องใส่ chest drain** ถ้าไม่ใช่ empyema · steroid ไม่แนะนำเป็นประจำ\n"
                  "- ติดตาม CXR · น้ำมักหายใน 6–12 สัปดาห์ อาจเหลือ pleural thickening"}]}]

OSCE = [{"id": "CH-THOR-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
         "topic": "OSCE – Consent and ultrasound-guided diagnostic thoracentesis (manikin)",
         "station": "OSCE (หัตถการ) 10 นาที",
         "nl": [PE, PFA, BF, ANAT, PTX], "ref": R("Procedure · After care") + [BTS],
         "instruction": "หญิงไทยอายุ 62 ปี มีน้ำในช่องเยื่อหุ้มปอดข้างซ้ายปริมาณปานกลาง ไม่ทราบสาเหตุ อาการคงที่ ผลเลือด: platelet 210,000/µL · INR 1.1 · ไม่ได้ใช้ยาต้านเกล็ดเลือด/ยาต้านการแข็งตัวของเลือด\n\n"
                        "**จงอธิบายและขอความยินยอมจากผู้ป่วย (ผู้ป่วยมาตรฐาน) แล้วทำ diagnostic thoracentesis บนหุ่น พร้อมเก็บสิ่งส่งตรวจให้ถูกต้อง ภายใน 10 นาที** · "
                        "มีเครื่องอัลตราซาวด์ ชุดเจาะปลอดเชื้อ thoracentesis catheter, 3-way stopcock, syringe, 1% lidocaine, chlorhexidine, หลอดส่งตรวจครบ วางไว้ให้",
         "answer": "**เกณฑ์ให้คะแนน (20 คะแนน)**\n\n| ข้อ | สิ่งที่ต้องทำ | คะแนน |\n|---|---|---|\n"
                   "| 1 | แนะนำตัว **ยืนยันตัวผู้ป่วย** (ชื่อ-สกุล + HN) และข้างที่จะเจาะ · ล้างมือ | 1 |\n"
                   "| 2 | **อธิบายเหตุผล** (หาสาเหตุของน้ำ) และขั้นตอนเป็นภาษาที่เข้าใจง่าย · บอกว่าจะรู้สึกอะไร ห้ามไอ/ขยับแรง ถ้าจะไอให้บอก | 2 |\n"
                   "| 3 | **บอกความเสี่ยง**: pneumothorax (พบบ่อยที่สุด) · เลือดออก · หน้ามืด · ไอ/แน่นอก · ติดเชื้อ (พบน้อย) · ทางเลือกอื่น · เปิดโอกาสให้ถาม · **ลงนามยินยอม** | 2 |\n"
                   "| 4 | ทบทวน **แพ้ยา** (lidocaine, chlorhexidine) · **ค่าเลือด/ยาต้านเลือด** · วัด **V/S + SpO2** ก่อนทำ | 2 |\n"
                   "| 5 | จัดท่า **นั่งโน้มตัวไปข้างหน้า** แขนวางบนโต๊ะ · **อัลตราซาวด์** หาแอ่งน้ำลึก ≥ 1 cm ดูกะบังลมตลอดการหายใจ · มาร์กจุดแนว mid-scapular–posterior axillary ไม่ชิดกระดูกสันหลัง | 3 |\n"
                   "| 6 | **ปลอดเชื้อ**: ล้างมือ ถุงมือ ทา chlorhexidine วนออก ปูผ้า · ต่อ catheter กับ **3-way stopcock** และสาย | 2 |\n"
                   "| 7 | **ยาชา** ผิว → ใต้ผิว → **parietal pleura** · **ดูดก่อนฉีดทุกครั้ง** · บอกได้ว่าดูดได้น้ำ = ถึงช่อง | 2 |\n"
                   "| 8 | แทง **90° ชิดขอบบนของซี่โครงล่าง** ขณะดูดเบา ๆ · เห็นน้ำ → ดันสาย ถอยเข็ม · **ปิด 3-way ทุกครั้งก่อนถอด syringe** | 2 |\n"
                   "| 9 | **เก็บสิ่งส่งตรวจถูกภาชนะ**: pH ใน syringe heparin ไล่ลม · EDTA (cell) · ขวดปลอดเชื้อ (protein LDH glucose albumin ± ADA) · Gram/culture + ขวด H/C · cytology · **เจาะเลือดคู่** | 2 |\n"
                   "| 10 | ถอดสาย ปิดแผลปลอดเชื้อ · ประเมิน V/S SpO2 เสียงหายใจ แผล · บอกว่าจะถ่าย CXR เมื่อมีอาการ (ไม่ต้องทุกราย) · บอกอาการที่ต้องแจ้งทันที | 2 |\n\n"
                   "**จุดตาย**: ไม่ขอ consent · ไม่ใช้อัลตราซาวด์/เจาะต่ำกว่า ICS 9 · แทงใต้ขอบล่างของซี่โครง · เปิดสายสู่อากาศ (ไม่ปิด 3-way) · ใช้ syringe ที่มีลิโดเคนส่ง pH"}]

LECTURE = {
 "lec": LEC, "date": "", "title": "Thoracentesis และการแปลผลน้ำในช่องเยื่อหุ้มปอด",
 "subtitle": "Active learning กลุ่ม 5 — ข้อบ่งชี้ diagnostic/therapeutic · ข้อห้าม · consent · อุปกรณ์ ท่า อัลตราซาวด์ · แทงเหนือขอบบนซี่โครง · ขีดระบาย 1–1.5 L · RPE · ภาวะแทรกซ้อน · การส่งตรวจและ pH · อ่านผลห้าขั้น · Case HF",
 "objectives": [
   "บอกข้อบ่งชี้ของ thoracentesis เพื่อวินิจฉัยและเพื่อรักษา และรู้ว่าเมื่อใดไม่จำเป็นต้องเจาะ",
   "อธิบาย relative contraindication แต่ละข้อด้วยกลไกของอันตราย และขอ informed consent ได้ครบ",
   "จัดท่า ใช้อัลตราซาวด์เลือกจุด และอธิบายว่าทำไมต้องแทงชิดขอบบนของซี่โครงล่างและห่างกระดูกสันหลัง",
   "อธิบายเหตุผลของขีดระบาย ~1–1.5 L และกลไก re-expansion pulmonary oedema",
   "แยก pneumothorax, vasovagal, hemothorax และ RPE จากสัญญาณชีพและการตรวจร่างกาย พร้อมการดูแลหลังทำ",
   "เก็บสิ่งส่งตรวจให้ถูกภาชนะ โดยเฉพาะ pH ในหลอด blood gas และอธิบายสิ่งที่ทำให้ pH เพี้ยน",
   "อ่านผลน้ำห้าขั้น: รูปลักษณ์ · Light's criteria (+ false exudate) · cell · pH/glucose/LDH · ตรวจพิเศษ (ADA, cytology, TG, Hct, amylase, culture)",
   "แปลผล Case ในสไลด์ได้ด้วยตัวเลข และวางแผนการรักษาตามสาเหตุ"],
 "nlGap": "เกณฑ์ฯ มีรหัสโรคและการตรวจครบ — pleural effusion (`นล. 2.3.10(7)`), pleural fluid analysis (`B6.3(1)`), body fluid analysis (`3.1.7`), กายวิภาค pleura (`B6.1.1(4)`), hemothorax/pneumothorax (`B6.2.3(3)/(4)`) · "
          "แต่ **พจนานุกรม นล. ในเว็บไม่มีรหัสหัตถการ thoracentesis** (หมวดหัตถการไม่ได้แกะไว้) จึงใช้รหัสโรค/การตรวจแทน · "
          "**สไลด์เป็นงานนำเสนอของนักศึกษา ตารางในขั้นแปลผลเป็นภาพ (อ่านไม่ได้) และไม่มีตัวเลขขีดระบาย ชนิดหลอดส่งตรวจ จุดตัด pH/glucose/ADA/TG/Hct** — ส่วนเหล่านี้อิงแนวทางด้านล่าง และระบุในบทเรียนว่าไม่ได้มาจากสไลด์",
 "guidelines": [
   "**BTS Clinical Statement on Pleural Procedures (Thorax 2023)** — อัลตราซาวด์ทุกครั้ง · ค่าเลือดและยาต้านเลือด · ขีดระบาย · CXR หลังทำ",
   "**BTS Guideline for Pleural Disease (Thorax 2023)** — ลำดับการตรวจน้ำ · Light's criteria · pH/glucose ใน parapneumonic · ปริมาณ cytology",
   "**Light RW. Pleural Diseases / Light's criteria (1972)** — เกณฑ์ exudate และ albumin gradient",
   "**ACCP consensus 2000: Medical and surgical treatment of parapneumonic effusions** — pH < 7.2 / glucose < 60 / LDH > 1,000",
   "**แนวทางการควบคุมวัณโรคประเทศไทย 2564** — ADA และการรักษา TB pleuritis (ดูคาบ EPTB)"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ───────────────────────────── กระจายตำแหน่งคำตอบ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น)
_slot = 0
for s_ in S:
    for it in s_["items"]:
        tgt = [2, 4, 1, 3, 0][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

# ───────────────────────────── เขียนลงไฟล์ (ต่อท้ายคาบ 17) แล้วผูกข้อ Mock M08
path = os.path.join(BUILD, "data", SET + ".json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LEC]
pos = next((i + 1 for i, l in enumerate(data) if l["lec"] == "17"), len(data))
data.insert(pos, LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
added = link_mock(SET, LEC, {"chest-thor-07": ["MOCK-142"], "chest-thor-10": ["MOCK-138"], "chest-thor-11": ["MOCK-137"]})

data = json.load(open(path, encoding="utf-8"))
L = [l for l in data if l["lec"] == LEC][0]
seen = set()
for f in os.listdir(os.path.join(BUILD, "data")):
    if f.endswith(".json") and f not in ("nl.json", "index.json"):
        for l in json.load(open(os.path.join(BUILD, "data", f), encoding="utf-8")):
            for x in [i for s_ in l["sections"] for i in s_["items"]] + l["meq"] + l["osce"] + [{"id": s_["id"]} for s_ in l["sections"]]:
                assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
                seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = ({c for s_ in L["sections"] for c in s_["nl"]} | {c for s_ in L["sections"] for i in s_["items"] for c in i.get("nl", [])}
         | {c for m in L["meq"] + L["osce"] for c in m.get("nl", [])})
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
for s_ in L["sections"]:
    assert "```" not in s_["md"], s_["id"]
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == SET: m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print("sections %d | ข้อใหม่ %d + mock %d = %d | meq %d | osce %d | ภาพ %d | nl %d" % (
    len(S), sum(1 for s_ in S for i in s_["items"] if i["id"].startswith("CH-THOR")), added,
    sum(len(s_["items"]) for s_ in L["sections"]), len(L["meq"]), len(L["osce"]), sum(len(s_["figs"]) for s_ in S), len(codes)))
print("ตำแหน่งคำตอบข้อใหม่:", dict(sorted(Counter(i["answer"] for s_ in S for i in s_["items"] if i["id"].startswith("CH-THOR")).items())))
print("%s.json มี %d คาบ: %s" % (SET, len(data), [l["lec"] for l in data]))
