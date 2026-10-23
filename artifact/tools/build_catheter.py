#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Urethral catheterization (อ.ธนิศร หาญศิริกาญจน์ · Tanisorn Harnsirikarn, MD · nephrologist รพ.ราชวิถี) → data/nephro.json
ต้นฉบับ: Drive 1Kz2_TGtz1FmW-vOeIzCP3-97-x2p3PVz "Lec27 Urethral Catheterization for Medical Students (handout version).pdf" (25 หน้า)
โน้ตสไลด์: slides/catheter_notes.md · ภาพประกอบ: figs_catheter.py (13 ภาพ)
lec = "22/10" (ไม่มีคาบนี้ในคลัง Ward Drill) · date พฤ. 22 ต.ค. (ปฏิทิน: Lecture: Urethral catheterization 15:00)
สไลด์มี: ชนิด/ข้อบ่งชี้/ข้อห้าม (EAUN 2024) · ขนาด วัสดุ การยึด การดูแล · ใส่ไม่เข้า (Campbell) · ปวด/เลือดออกหลังใส่ · ตาราง BAUS-BAUN 2021 · 4 เคส
สไลด์ไม่มี (เติมจากแนวทาง/ตำรา และระบุในบทเรียน): กายวิภาคท่อปัสสาวะ · ขั้นตอนการใส่ทีละขั้น · urethral injury · CAUTI (CDC/HICPAC 2009, IDSA 2009) ·
post-obstructive diuresis · acute urinary retention
คลัง Ward Drill: ข้อ catheter ในคลัง (N-OLD-099..101) ผูกกับคาบ 30 แล้ว · MOCK-020 ผูกแล้ว · N-MCQ-40/N-OLD-121 เป็นของคาบ 42 AKI → ไม่ผูก"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from svg import fig
import figs_catheter as F

SET, LEC = "nephro", "22/10"
SRC = "สไลด์ อ.ธนิศร — Urethral Catheterization (handout)"
SRC_ADD = "สไลด์ อ.ธนิศร + แนวทาง/ตำรา (ส่วนใหญ่ไม่อยู่ในสไลด์)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl, figs=None, source=SRC):
    d = {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": source,
         "nl": nl, "md": md, "pearls": pearls, "items": items}
    if figs: d["figs"] = figs
    S.append(d)
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl):
    assert len(choices) == 5 and 0 <= answer <= 4 and len(set(choices)) == 5, iid
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}
N = lambda n: "NEPH-CATH-MCQ-%02d" % n
R = lambda p, *g: ["สไลด์ อ.ธนิศร — " + p] + list(g)

# รหัส นล.
RET, AUR, AUR_B = "2.1.45", "2.2.29", "B9.2.3(1)"
BPH, BPH_B, BPH_D = "2.3.14(8)", "B10.2.4(2)", "B10.4(7)"
ANAT, INNV = "B9.1.1(2)", "B9.1.1(3)"
DEVICE, HARM = "2.3.19(5)", "2.3.19(4)"
CYST, PYELO, CYST_B, PYELO_B = "2.3.14(7)", "2.3.14(14)", "B9.2.2(1)", "B9.2.2(2)"
BIOFILM, PATHO, RESIST = "B1.5.2(3)", "B1.5.2(4)", "B1.5.1(7)"
HEMAT, OLIG, POLY, OLIG_B = "2.1.43", "2.1.44", "2.1.42", "B9.2.5(1)"
LYTE, LYTE_B = "2.3.4(2)", "B9.2.5(2)"
OBST, AKI, AKI_B = "2.3.14-3(9)", "2.3.14(3)", "B9.2.7(1)"
PARA = "2.3.14-3(11)"
INCONT, SEPSIS, SHOCK, INJURY = "2.1.46", "2.2.48", "2.2.7", "2.2.47"
DELIR, CONST, FEVER = "2.1.78", "2.1.19", "2.1.1"
UA, CULT, SPEC = "3.1.6", "3.3.9", "B9.3(1)"
OAB_D = "B9.4(3)"

# ═════════════════════════════════════════════ 1
sec("nephro-cath-01", "สวนปัสสาวะมีกี่แบบ — และทำไมต้อง “หลีกเลี่ยงสายค้าง”",
    "Indwelling · intermittent · external · suprapubic — เลือกวิธีที่รุกล้ำน้อยที่สุด (EAUN 2024)", 7,
"""### โครงของคาบ (สไลด์)
อ.ธนิศร แบ่งคาบเป็น 3 ส่วน: **When & Why…** (ชนิด ข้อบ่งชี้ ข้อห้าม) → **How to do?** (เลือกขนาด วัสดุ การยึด การดูแล) → **Troubleshooting!** (ใส่ไม่เข้า ปวด เลือดออก ปัญหาอื่น) ปิดด้วย 4 เคสให้ตัดสินใจว่าควรใส่สายหรือไม่

> handout ไม่มีหน้าที่สอน **ขั้นตอนการใส่ทีละขั้น กายวิภาคท่อปัสสาวะ CAUTI และ post-obstructive diuresis** — บทเรียนนี้เติมจากแนวทาง (CDC/HICPAC 2009, IDSA 2009, EAUN 2024, EAU) และตำรา โดยบอกไว้ในแต่ละหัวข้อ

### ชนิดของการสวน (สไลด์ Definition & Terminologies)
[[fig:types]]
| ชนิด | ลักษณะ | ลายมือในสไลด์ / ใช้เมื่อ |
|---|---|---|
| **Indwelling catheter** (Foley) | ใส่ทางท่อปัสสาวะแล้ว **ค้างไว้** ยึดด้วยบอลลูน ต่อถุงระบบปิด | ✍️ "ใส่ค้างไว้" — ต้องระบายต่อเนื่องหรือวัดปัสสาวะทุกชั่วโมง |
| **Intermittent catheter** (Nelaton) | สายตรงไม่มีบอลลูน ใส่ระบายจนหมดแล้ว **ดึงออกทันที** | ✍️ "ใส่แล้วเอาออกเลย → เก็บ urine ส่งตรวจ" · ระบายเป็นรอบใน neurogenic bladder |
| **External catheter** | condom catheter (ชาย) · อุปกรณ์ดูดภายนอก (หญิง) — **ไม่มีอะไรเข้าท่อปัสสาวะ** | ✍️ ผู้ป่วยที่ **ไม่มีปัสสาวะคั่งค้าง** แต่กลั้นไม่ได้ · แบบหญิงยังหาไม่ง่ายในไทย |
| **Suprapubic catheter (SPC)** | เจาะผ่านผนังหน้าท้องเข้ากระเพาะโดยตรง | ใส่ทางท่อปัสสาวะไม่ได้ (urethral injury, stricture) หรือต้องใช้ระยะยาว |

### ทำไมสายค้างจึงเป็นตัวปัญหา
- สายที่ค้างในท่อปัสสาวะเป็น **สะพานให้เชื้อไต่ขึ้น** ทั้งผิวนอกและในท่อ และเชื้อสร้าง **biofilm** เกาะผิวสาย → bacteriuria เพิ่มวันละ 3–7% (ดูหัวข้อ 8)
- สายกดเยื่อบุท่อปัสสาวะตลอดเวลา → แผล กัดกร่อน stricture · บอลลูนระคายเคืองคอกระเพาะ → ปวดเกร็ง (หัวข้อ 10)
- external และ intermittent ไม่มีสิ่งแปลกปลอมค้าง จึงเสี่ยงน้อยกว่า

### คำแนะนำในสไลด์ (EAUN 2024)
| คำแนะนำ | LE | GR |
|---|---|---|
| ถ้าจะใส่สายค้าง ให้พิจารณาวิธีอื่นก่อน เช่น **male external catheter** หรือ **intermittent catheterization** เมื่อเหมาะสม | 1b | A |
| ในผู้ที่ **กระเพาะบีบตัวระบายไม่หมด** การสวนเป็นครั้งคราวดีกว่าสายค้างทั้งทางท่อปัสสาวะและ suprapubic ถ้าทำได้จริงในผู้ป่วยรายนั้น | 1b | B |

> **AVOID using indwelling catheter as much as you can!** — เพื่อลด catheter-associated UTI (CA-UTI) ซึ่งเป็นการติดเชื้อในโรงพยาบาลที่พบบ่อยและป้องกันได้
""",
    ["Indwelling = ค้างไว้ · Intermittent = ใส่แล้วเอาออกเลย · External = ไม่มีอะไรเข้าท่อปัสสาวะ",
     "เลือกวิธีรุกล้ำน้อยสุดก่อน: external/IC ก่อน indwelling (EAUN 1b, A)",
     "Bladder emptying dysfunction → IC ดีกว่าสายค้างทั้ง urethral และ suprapubic",
     "ความเสี่ยงติดเชื้อมาจาก “สายที่ค้าง” — ยิ่งนานยิ่งเสี่ยง"],
    [mcq(N(1), "A 74-year-old man is admitted with a minor ischaemic stroke. He is alert and cooperative but has urge incontinence. A bladder scan after voiding shows 30 mL. Nurses request an indwelling catheter to keep him dry. What is the most appropriate management?",
         ["Male external (condom) catheter with scheduled toileting", "Indwelling 16 Fr Foley catheter connected to a closed drainage bag",
          "Suprapubic catheter", "Intermittent catheterization every 6 hours", "Indwelling Foley catheter with daily prophylactic nitrofurantoin"], 0,
         "ผู้ป่วยกลั้นไม่ได้ แต่ **ไม่มีปัสสาวะคั่งค้าง** (PVR 30 mL) ปัญหาคือ \"เปียก\" ไม่ใช่ \"ระบายไม่ออก\" → อุปกรณ์ที่ไม่มีอะไรเข้าท่อปัสสาวะ (**male external catheter**) + พาเข้าห้องน้ำเป็นเวลา คือทางเลือกที่รุกล้ำน้อยสุด (EAUN 1b A · CDC/HICPAC 2009: การกลั้นไม่ได้ **ไม่ใช่** ข้อบ่งชี้ของสายค้าง)\n\n"
         "- **Foley** — ใช้แทนการพยาบาลผู้ป่วยกลั้นไม่ได้ = ข้อบ่งชี้ไม่เหมาะสม เพิ่ม CAUTI\n- **Suprapubic** — รุกล้ำกว่า ใช้เมื่อทางท่อปัสสาวะไม่ได้หรือระยะยาวที่ต้องระบาย\n"
         "- **IC** — ใช้เมื่อระบายไม่หมด ผู้ป่วยรายนี้ระบายได้หมด\n- **ยาปฏิชีวนะป้องกัน** — ไม่แนะนำ ไม่ลด CAUTI แต่เพิ่มเชื้อดื้อยา",
         "กลั้นไม่ได้แต่ไม่คั่ง → external catheter ไม่ใช่ Foley", "Choosing the least invasive drainage", R("Definition & Terminologies · Type of catheter selection", "CDC/HICPAC CAUTI 2009"), [INCONT, DEVICE]),
     mcq(N(2), "A 32-year-old man with a T10 spinal cord injury has a neurogenic bladder with post-void residuals of 400–500 mL. He has normal hand function and wants to return to work. Which long-term bladder management is preferred?",
         ["Long-term indwelling urethral catheter changed monthly", "Suprapubic catheter", "Clean intermittent self-catheterization several times a day",
          "Male external catheter alone", "Oral bethanechol and timed voiding without catheterization"], 2,
         "กระเพาะบีบตัวระบายไม่หมด (PVR 400–500 mL) ต้องระบายเป็นรอบ และผู้ป่วยใช้มือได้ดี → **clean intermittent self-catheterization** เป็นมาตรฐาน (EAUN 1b B: IC ดีกว่าสายค้างทั้ง urethral และ suprapubic) — กระเพาะได้ว่างเป็นรอบ ไม่มีสิ่งแปลกปลอมค้าง ติดเชื้อและ stricture น้อยกว่า\n\n"
         "- **สายค้างทางท่อปัสสาวะ** — ระยะยาวเสี่ยง CAUTI นิ่ว urethral erosion\n- **Suprapubic** — ใช้เมื่อทำ IC ไม่ได้ (มือไม่ดี ไม่มีผู้ช่วย)\n"
         "- **External catheter อย่างเดียว** — เก็บปัสสาวะที่ล้นออกมา แต่ไม่ได้ระบายน้ำที่คั่ง → ความดันในกระเพาะสูงทำร้ายไต\n- **Bethanechol** — ได้ผลน้อยมากใน neurogenic bladder และไม่แก้ปัญหา",
         "Neurogenic bladder + มือดี → CISC", "Intermittent vs indwelling catheterization", R("Type of catheter selection (EAUN 2024)"), [RET, DEVICE])],
    [RET, INCONT, DEVICE], {"types": F.types()})

# ═════════════════════════════════════════════ 2
sec("nephro-cath-02", "ข้อบ่งชี้ — เมื่อไรควรใส่ และเมื่อไร “ไม่ควร”",
    "ตาราง EAUN 2024 · ข้อบ่งชี้ที่เหมาะสม/ไม่เหมาะสมของ CDC/HICPAC 2009 · 4 เคสในสไลด์", 9,
"""### ข้อบ่งชี้ในสไลด์ (EAUN 2024)
| Intermittent catheterization | Indwelling catheterization |
|---|---|
| Acute or chronic urinary retention | Acute or chronic urinary retention |
| Overflow incontinence | Voiding difficulties |
| ระบายไม่หมด เช่น neurogenic/hypotonic bladder | **วัดปริมาณปัสสาวะ (urine output)** |
| Continent urinary diversion | ใส่ยาเข้ากระเพาะ (intravesical therapy) |
| ใส่ยาเข้ากระเพาะ (intravesical instillation) | การผ่าตัดบางชนิด |
| การตรวจ เช่น urodynamics | ช่วยผู้ป่วยกลั้นไม่ได้ (บางกรณี เช่น มีแผล) |
| ล้างกระเพาะ (bladder washout) | นอนนิ่งนาน (prolonged immobilization) |
| ป้องกันภาวะแทรกซ้อนขณะใส่แร่ เช่น cesium ที่ปากมดลูก | ระบายกระเพาะ (bladder decompression) |
| | **ความสุขสบายในระยะท้ายของชีวิต** |

✍️ ลายมือในสไลด์: ฝั่ง intermittent เขียน **"post-void residual volume … 50–150"** (อ่านได้ไม่ชัด — ค่าที่ใช้กันทั่วไปคือ PVR < 50 mL ปกติ · ถ้าซ้ำ ๆ เกินราว 150–200 mL ถือว่าระบายไม่หมด → พิจารณา IC) · ฝั่ง indwelling เขียน **"monitor u/o, เก็บ sample 24 hr"**

### ข้อบ่งชี้ที่เหมาะสม vs ไม่เหมาะสม (CDC/HICPAC 2009 — ไม่อยู่ในสไลด์)
| เหมาะสม ✓ | ไม่เหมาะสม ✗ |
|---|---|
| Acute urinary retention หรือ bladder outlet obstruction | **ใช้แทนการพยาบาล** ผู้ป่วยกลั้นไม่ได้ |
| วัด intake/output **ถูกต้องทุกชั่วโมงในผู้ป่วยวิกฤต** (shock, vasopressor) | **เก็บปัสสาวะส่งตรวจ** ในผู้ที่ปัสสาวะเองได้ |
| ระหว่างผ่าตัดบางชนิด: ผ่าตัดระบบปัสสาวะ ผ่าตัดนาน ให้น้ำ/ยาขับปัสสาวะมาก วัดปัสสาวะระหว่างผ่าตัด — **ถอดภายใน 24 ชม.หลังผ่าตัด** | **ค้างหลังผ่าตัดนานเกินจำเป็น** โดยไม่มีข้อบ่งชี้ |
| ช่วยแผลเปิดที่ **กระดูกก้นกบ/ฝีเย็บ (sacral/perineal wound)** หายในผู้ที่กลั้นไม่ได้ | วัดปัสสาวะใน "ผู้ป่วยทั่วไป" ที่ใช้กระบอก/ชั่งผ้าอ้อมได้ |
| นอนนิ่งนานจากกระดูกสันหลังไม่มั่นคง หรือ pelvic fracture หลายตำแหน่ง | |
| ความสุขสบายระยะท้ายของชีวิต | |

#### ทำไม "วัดปัสสาวะ" จึงเป็นข้อบ่งชี้เฉพาะผู้ป่วยวิกฤต
ปัสสาวะต่อชั่วโมงเป็นตัวสะท้อน **การไหลเวียนเลือดไปไต** แบบนาทีต่อนาที ใช้ปรับ fluid/vasopressor ใน shock → ต้องแม่นทุกชั่วโมง · ในผู้ป่วยที่ไม่วิกฤต การวัดรวม 4–8 ชม. ด้วยกระบอกหรือชั่งผ้าอ้อมก็พอ ไม่คุ้มกับความเสี่ยงติดเชื้อ

### 4 เคสในสไลด์ (Scenario) — ควรใส่สายไหม
| เคส | ข้อมูล | คำตอบที่น่าจะเป็น (ผู้เขียนบทเรียน — สไลด์ไม่มีเฉลย) |
|---|---|---|
| 1 | หญิง 50 ปี เบาหวาน **complicated UTI** BT 38.5 BP 121/80 PR 100 รู้ตัวดี ทำกิจวัตรได้ | **ไม่ต้องใส่สายค้าง** — ปัสสาวะเองได้ เก็บ **midstream clean-catch** ส่งเพาะเชื้อ · ถ้าสงสัย diabetic cystopathy ให้ bladder scan ดู PVR ก่อน ถ้าคั่งจึง IC |
| 2 | 70 ปี สมองเสื่อมมาก **pneumonia** BT 39 BP 100/60 PR 130 RR 30 | **sepsis ที่อาจต้องวัดปัสสาวะทุกชั่วโมง** → สายค้างระยะสั้นเหมาะสม และ **ถอดเมื่อพ้นภาวะวิกฤต** |
| 3 | หญิง 15 ปี **major trauma เลือดออกมาก** BP 70/55 PR 160 | **shock** ต้องวัดปัสสาวะ → ใส่ได้ แต่ **ตรวจหา urethral injury ก่อน** (pelvic fracture เลือดที่ meatus/ช่องคลอด — หัวข้อ 5) |
| 4 | ชาย 55 ปี BPH หลัง **TURP** | ผ่าตัดระบบปัสสาวะ → **3-way catheter ขนาดใหญ่ + ล้างกระเพาะต่อเนื่อง** กันลิ่มเลือดอุด (หัวข้อ 6) |
""",
    ["วัดปัสสาวะทุกชั่วโมงเป็นข้อบ่งชี้เฉพาะผู้ป่วยวิกฤต",
     "ไม่ใส่สายค้างเพื่อเก็บปัสสาวะส่งตรวจ หรือเพื่อแทนการพยาบาลผู้ป่วยกลั้นไม่ได้",
     "หลังผ่าตัด: ถอดภายใน 24 ชม. ถ้าไม่มีข้อบ่งชี้ต่อ (CDC 2009)",
     "แผลที่ sacrum/ฝีเย็บในผู้ป่วยกลั้นไม่ได้ และความสุขสบายระยะท้าย = ข้อบ่งชี้ที่ยอมรับ",
     "ทุกวัน: ถามว่า “ยังต้องมีสายนี้อยู่ไหม”"],
    [mcq(N(3), "Which of the following is an appropriate indication for placing an indwelling urethral catheter according to CDC/HICPAC 2009 guidance?",
         ["Accurate hourly urine output measurement in a patient with septic shock on norepinephrine",
          "Obtaining a urine culture from an alert woman with suspected pyelonephritis who can void",
          "Managing urinary incontinence in a nursing-home resident to reduce nursing workload",
          "Continuing drainage on day 3 after an uncomplicated laparoscopic cholecystectomy",
          "Monitoring output in a ward patient with heart failure on IV furosemide who can use a urinal"], 0,
         "ข้อบ่งชี้ที่เหมาะสมของ CDC/HICPAC 2009 ข้อหนึ่งคือ **วัด urine output อย่างแม่นยำในผู้ป่วยวิกฤต** — ใน septic shock ปัสสาวะทุกชั่วโมงสะท้อนการไหลเวียนไปไตและใช้ปรับ fluid/vasopressor\n\n"
         "- **เก็บเพาะเชื้อในผู้ที่ปัสสาวะเองได้** — ใช้ midstream clean-catch (หรือ IC ครั้งเดียวถ้าจำเป็น)\n- **แทนการพยาบาลผู้ป่วยกลั้นไม่ได้** — ไม่เหมาะสมโดยตรง\n"
         "- **หลังผ่าตัดที่ไม่ซับซ้อน** — ควรถอดภายใน 24 ชม.\n- **HF บนหอผู้ป่วยทั่วไป** — ใช้กระบอกปัสสาวะ/ชั่งน้ำหนักได้ ไม่ต้องวัดรายชั่วโมง",
         "วัดปัสสาวะรายชั่วโมง = ผู้ป่วยวิกฤตเท่านั้น", "Appropriate indications for indwelling catheter", R("Indication for catheterization", "CDC/HICPAC CAUTI 2009"), [SEPSIS, SHOCK, DEVICE]),
     mcq(N(4), "A 50-year-old woman with diabetes presents with fever 38.5 °C and flank pain (complicated UTI). She is alert, BP 121/80 mmHg, and walks to the toilet independently. How should urine for culture be obtained?",
         ["Insert an indwelling catheter to collect urine and monitor output", "Midstream clean-catch urine; no catheter unless retention is demonstrated",
          "Suprapubic aspiration", "Collect urine from a 24-hour collection bottle", "Insert a 3-way catheter for bladder washout and culture"], 1,
         "เคสที่ 1 ในสไลด์: ผู้ป่วยรู้ตัวดี ปัสสาวะเองได้ hemodynamics คงที่ → **ไม่มีข้อบ่งชี้ของสายค้าง** · เก็บ **midstream clean-catch** ส่งเพาะเชื้อ · ถ้าสงสัยปัสสาวะคั่ง (diabetic cystopathy) ให้ bladder scan ดู PVR ก่อน ถ้าคั่งจริงค่อยระบาย (IC)\n\n"
         "- **ใส่สายค้างเพื่อเก็บปัสสาวะ** — ข้อบ่งชี้ที่ไม่เหมาะสมตาม CDC\n- **Suprapubic aspiration** — รุกล้ำเกินจำเป็นในผู้ใหญ่ที่ปัสสาวะได้\n"
         "- **ปัสสาวะ 24 ชม.** — ปนเปื้อน ใช้เพาะเชื้อไม่ได้\n- **3-way** — ใช้ล้างลิ่มเลือด ไม่เกี่ยว",
         "ปัสสาวะเองได้ → clean-catch ไม่ใช่ Foley", "Avoiding unnecessary catheters", R("Scenario Case 01", "CDC/HICPAC CAUTI 2009"), [CYST, PYELO, SPEC, CULT]),
     mcq(N(5), "A 58-year-old man had an uncomplicated total hip replacement under spinal anaesthesia yesterday. A urinary catheter was placed in theatre. He is haemodynamically stable and drinking well. What is the best plan for the catheter?",
         ["Keep it until he can walk to the toilet, usually day 3–4", "Remove it now (within 24 hours of surgery) and monitor voiding/post-void residual",
          "Keep it until a urine culture is negative", "Clamp it intermittently for 24 hours before removal (bladder training)", "Replace it with a suprapubic catheter"], 1,
         "CDC/HICPAC 2009: ใส่สายระหว่างผ่าตัด **เฉพาะเมื่อจำเป็น** และ **ถอดเร็วที่สุด — ภายใน 24 ชม.หลังผ่าตัด** ถ้าไม่มีข้อบ่งชี้ต่อ · หลังถอดติดตามว่าปัสสาวะได้ภายใน ~6 ชม. และ bladder scan ถ้าสงสัยคั่ง (ถ้าคั่งใช้ IC)\n\n"
         "- **รอจนเดินได้** — \"นอนบนเตียง\" อย่างเดียวไม่ใช่ข้อบ่งชี้ (ยกเว้นต้องนอนนิ่งจากกระดูกสันหลัง/เชิงกรานไม่มั่นคง)\n- **รอผลเพาะเชื้อ** — ไม่เกี่ยวกับการถอด\n"
         "- **Clamp ก่อนถอด** — CDC: ไม่จำเป็น\n- **Suprapubic** — ไม่มีข้อบ่งชี้",
         "Peri-operative catheter → ถอดภายใน 24 ชม.", "Peri-operative catheter removal", R("Indication for catheterization", "CDC/HICPAC CAUTI 2009"), [DEVICE, RET])],
    [RET, AUR, DEVICE, SEPSIS, SHOCK, INCONT, SPEC], source=SRC + " + CDC/HICPAC 2009")

# ═════════════════════════════════════════════ 3
sec("nephro-cath-03", "Acute urinary retention — ข้อบ่งชี้ที่พบบ่อยที่สุด",
    "สาเหตุ (BPH ยา ท้องผูก หลังผ่าตัด ประสาท) · ทำไมถึงมีอาการ · ระบายแล้วทำอะไรต่อ (alpha-blocker + TWOC)", 8,
"""Acute urinary retention (AUR) = **ปัสสาวะไม่ออกทันทีทั้งที่กระเพาะเต็ม มักปวดมาก** — เป็นข้อบ่งชี้แรกของทั้ง IC และ indwelling ในตารางสไลด์ (เนื้อหาหัวข้อนี้ไม่อยู่ในสไลด์ — อิงตำราและ EAU Non-neurogenic male LUTS)

### สาเหตุ — คิดเป็น "ทางออกแคบ" + "กระเพาะบีบไม่แรง"
| กลไก | ตัวอย่าง |
|---|---|
| ทางออกถูกอุด (mechanical) | **BPH** (พบบ่อยที่สุดในชายสูงอายุ) · urethral stricture · ลิ่มเลือด (clot retention) · ก้อนในอุ้งเชิงกราน · อุจจาระอัดแน่นกดคอกระเพาะ |
| แรงต้านที่คอกระเพาะเพิ่ม (dynamic) | ยา **alpha-agonist** เช่น pseudoephedrine ในยาแก้หวัด → กล้ามเนื้อเรียบที่คอกระเพาะ/prostate หดตัว |
| กระเพาะบีบไม่แรง | ยา **anticholinergic** (chlorpheniramine, TCA, antipsychotic, oxybutynin) · **opioid** · ยาระงับความรู้สึก/หลังผ่าตัด · กระเพาะยืดเกินจากกลั้นนาน |
| ประสาท | spinal cord compression/cauda equina · diabetic cystopathy · MS · stroke |
| อื่น ๆ | prostatitis/UTI (บวม เจ็บ) · ท้องผูก · ดื่มแอลกอฮอล์มาก |

#### ทำไมถึงมีอาการนี้
[[fig:aur]]
| อาการ/อาการแสดง | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ปวดท้องน้อยมาก + ปวดปัสสาวะแต่ไม่ออก** | ผนังกระเพาะยืด → receptor การยืด → pelvic splanchnic (S2–4) | **chronic retention ไม่ปวด** เพราะกระเพาะค่อย ๆ ยืดและประสาทปรับตัว |
| **ก้อนเคาะทึบเหนือหัวหน่าว** | กระเพาะที่เต็มลอยพ้นกระดูกหัวหน่าวขึ้นมา | แยกจากก้อนอื่นด้วย bladder scan/ใส่สายแล้วยุบ |
| **ความดันสูง ชีพจรเร็ว เหงื่อออก** | ความปวดกระตุ้น sympathetic | อย่ารีบให้ยาลดความดัน — ระบายแล้วลงเอง |
| **สับสน กระสับกระส่ายในผู้สูงอายุ** | ปวดแต่สื่อสารไม่ได้ + sympathetic surge | delirium ทุกรายในผู้สูงอายุ **คลำ/สแกนกระเพาะ** ก่อนให้ยาสงบประสาท |
| **ปัสสาวะเล็ดเป็นหยด (overflow)** | ความดันในกระเพาะที่ยืดเต็มที่ > แรงต้านทางออก → ล้นออกทีละน้อย | อย่าเข้าใจผิดว่า "ยังปัสสาวะได้" — คือกระเพาะเต็มจนล้น |
| **Cr สูง hydronephrosis สองข้าง** | ความดันย้อนจากกระเพาะขึ้นท่อไต → ความดันใน Bowman's space สูง → GFR ↓ (post-renal AKI) | พบใน retention นาน/เรื้อรัง → เสี่ยง **post-obstructive diuresis** หลังระบาย (หัวข้อ 11) |

### หลังระบายแล้ว
- จดปริมาณที่ระบายได้ครั้งแรก (บอกว่าคั่งมากแค่ไหน และเสี่ยง post-obstructive diuresis หรือไม่)
- หาสาเหตุ/ปัจจัยกระตุ้น: หยุดยาแก้หวัด/anticholinergic แก้ท้องผูก รักษา UTI
- AUR จาก BPH: เริ่ม **alpha-blocker (tamsulosin/alfuzosin) อย่างน้อย 2–3 วันก่อน trial without catheter (TWOC)** — คลายกล้ามเนื้อเรียบที่คอกระเพาะและ prostate เพิ่มโอกาสปัสสาวะเองได้ (EAU) · ถ้า TWOC ไม่ผ่าน → IC หรือส่งผ่าตัด
""",
    ["AUR = ทางออกแคบ (BPH, ยา alpha-agonist) + กระเพาะบีบไม่แรง (anticholinergic, opioid)",
     "ผู้สูงอายุสับสนเฉียบพลัน → คลำ/สแกนกระเพาะก่อนให้ยาสงบประสาท",
     "Overflow dribbling = กระเพาะเต็มจนล้น ไม่ใช่ “ยังปัสสาวะได้”",
     "AUR จาก BPH: alpha-blocker 2–3 วันก่อน TWOC"],
    [mcq(N(6), "A 76-year-old man with known benign prostatic hyperplasia develops inability to void for 10 hours after taking an over-the-counter cold remedy containing pseudoephedrine and chlorpheniramine. Which mechanism best explains his retention?",
         ["α1-adrenergic stimulation increases smooth-muscle tone at the bladder neck and prostate, while antimuscarinic action weakens detrusor contraction",
          "β2-adrenergic stimulation causes detrusor spasm and bladder-neck relaxation",
          "Histamine H1 blockade directly causes prostatic enlargement",
          "Pseudoephedrine causes acute urethral stricture formation",
          "Chlorpheniramine increases urine production, overdistending the bladder"], 0,
         "AUR ในผู้ป่วย BPH มักมี **ตัวกระตุ้น** — ยาแก้หวัดมีทั้ง **pseudoephedrine (α1-agonist)** ที่ทำให้กล้ามเนื้อเรียบของคอกระเพาะ/prostate หดตัว (ทางออกแคบลง) และ **chlorpheniramine** ที่มีฤทธิ์ **anticholinergic** ลดแรงบีบของ detrusor (ซึ่งอาศัย M3) → ทางออกแคบ + แรงดันน้อย = ปัสสาวะไม่ออก\n\n"
         "- **β2 → detrusor spasm** — β3 ทำให้ detrusor คลาย ไม่ใช่บีบ\n- **H1 blockade ทำให้ prostate โต** — ไม่จริง\n- **stricture เฉียบพลันจากยา** — ไม่มี\n- **เพิ่มการสร้างปัสสาวะ** — ไม่ใช่กลไก",
         "ยาแก้หวัด = α-agonist + anticholinergic → AUR ในชาย BPH", "Drug-induced acute urinary retention", ["ตำรา urology / EAU Non-neurogenic male LUTS (ไม่อยู่ในสไลด์)"], [AUR, AUR_B, BPH, BPH_B]),
     mcq(N(7), "An 84-year-old woman with dementia in a nursing home becomes acutely agitated and is hitting staff. She is afebrile, BP 172/96 mmHg, HR 108/min. Her diaper is constantly damp with small amounts of urine. There is a tender, dull mass above the pubic symphysis. What is the most appropriate next step?",
         ["Intramuscular haloperidol", "Non-contrast CT brain", "Bladder scan and, if retention is confirmed, urinary catheterization",
          "Start empirical antibiotics for UTI", "Physical restraints and observation"], 2,
         "ภาพคือ **AUR ที่มาด้วย delirium**: ผู้ป่วยสมองเสื่อมบอกปวดไม่ได้ → ปวดจากกระเพาะยืด + sympathetic → กระสับกระส่าย ความดัน/ชีพจรสูง · ผ้าอ้อมชื้นตลอด = **overflow** · ก้อนทึบเหนือหัวหน่าว = กระเพาะเต็ม → **bladder scan แล้วระบาย** อาการจะดีขึ้นทันที\n\n"
         "- **Haloperidol / restraint** — กดอาการโดยไม่แก้สาเหตุ (และ anticholinergic บางตัวยิ่งทำให้คั่ง)\n- **CT brain** — ไม่มีอาการทางประสาทเฉพาะที่ และมีสาเหตุที่เห็นชัดอยู่แล้ว\n"
         "- **ยาปฏิชีวนะ** — ไม่มีไข้ ยังไม่มีหลักฐาน UTI และไม่ได้แก้การคั่ง",
         "Delirium ในผู้สูงอายุ → คลำ/สแกนกระเพาะเสมอ", "Atypical presentation of urinary retention", ["ตำราเวชศาสตร์ผู้สูงอายุ (ไม่อยู่ในสไลด์)"], [AUR, RET, DELIR, INCONT]),
     mcq(N(8), "A 70-year-old man had an indwelling catheter placed for acute urinary retention due to BPH (1,100 mL drained). Renal function is normal. Which strategy most increases the chance of successful voiding when the catheter is removed?",
         ["Remove the catheter immediately and restart his decongestant", "Start an α1-blocker (e.g., tamsulosin) for 2–3 days, then trial without catheter",
          "Clamp the catheter every 4 hours for 1 week before removal", "Start oxybutynin before removal", "Keep the catheter for 4 weeks to let the bladder rest"], 1,
         "หลัง AUR จาก BPH การให้ **alpha-blocker อย่างน้อย 2–3 วันก่อน TWOC** คลายกล้ามเนื้อเรียบที่คอกระเพาะและ prostate (ลดส่วน dynamic ของการอุด) → เพิ่มโอกาสปัสสาวะเองได้สำเร็จ (EAU)\n\n"
         "- **ให้ยาแก้หวัดต่อ** — คือตัวกระตุ้น\n- **Clamp สาย** — ไม่ช่วยและทำให้ปวด/ติดเชื้อ\n"
         "- **Oxybutynin** — anticholinergic ลดแรงบีบ ยิ่งคั่ง\n- **ค้างสาย 4 สัปดาห์** — เพิ่ม CAUTI โดยไม่ช่วยให้ผ่าน TWOC",
         "AUR จาก BPH: alpha-blocker ก่อน TWOC", "Trial without catheter", ["EAU Guidelines on Management of Non-neurogenic Male LUTS (ไม่อยู่ในสไลด์)"], [AUR, BPH, BPH_D])],
    [AUR, AUR_B, RET, BPH, BPH_B, BPH_D, DELIR, CONST, OBST], {"aur": F.aur()},
    source="ตำรา urology + EAU Non-neurogenic male LUTS (ไม่อยู่ในสไลด์ — สไลด์ระบุ retention เป็นข้อบ่งชี้)")

# ═════════════════════════════════════════════ 4
sec("nephro-cath-04", "กายวิภาค — ทำไมผู้ชายกับผู้หญิงใส่ต่างกัน",
    "ท่อปัสสาวะชาย ~20 ซม. 2 โค้ง 2 หูรูด prostate · หญิง 3–4 ซม. ตรง แต่หารูยาก", 8,
"""(เนื้อหากายวิภาคไม่อยู่ในสไลด์ — สไลด์มีภาพ BPH/stricture และหญิงอ้วนในหน้า "Difficult to insert" ซึ่งอธิบายด้วยกายวิภาคนี้)

### ท่อปัสสาวะชาย
[[fig:male_urethra]]
| ส่วน | ความยาวโดยประมาณ | สิ่งที่ต้องรู้ตอนใส่สาย |
|---|---|---|
| **Prostatic** | 3–4 ซม. (ยาวขึ้นมากใน BPH) | **internal sphincter** ที่คอกระเพาะ · ติ่ง prostate/median lobe ยกคอกระเพาะสูง → ปลายสายชน |
| **Membranous** | 1–2 ซม. | ผ่าน pelvic floor = **external sphincter** (กล้ามเนื้อลาย ควบคุมได้) — เกร็งเมื่อเจ็บ/กลัว |
| **Bulbar** | ~4 ซม. | กว้างและพื้นหย่อน — ปลายสายที่ถูกดันแรงจิ้มลงพื้นจน **false passage** · เป็นจุดที่ **ฉีกจาก pelvic fracture** (รอยต่อ bulbomembranous) |
| **Penile (pendulous)** | ~15 ซม. รวม glans | **fossa navicularis/meatus แคบที่สุด** |

#### สองโค้ง — ทำไมต้องจับองคชาตตั้ง 90°
- **Prepubic curve** (ที่มุม penoscrotal) — **ขยับได้** · จับองคชาตตั้งฉากกับลำตัวแล้วดึงขึ้นเบา ๆ โค้งนี้จะหายไป เหลือทางตรงยาว
- **Subpubic curve** (ใต้กระดูกหัวหน่าว) — **ตายตัว** · สายต้องเลี้ยวขึ้นเอง → สายที่นิ่มเกินหรือเล็กเกินมักขดตรงนี้ · ปลาย **coudé/Tiemann** ที่งอขึ้นช่วยเลี้ยว
- สไลด์: **"Change angle of penis into 90°, ask patient to strain"** — การเบ่งเหมือนจะปัสสาวะทำให้ external sphincter คลาย

### ท่อปัสสาวะหญิง
[[fig:female]]
- ยาว **3–4 ซม.** ตรง ไม่มี prostate · ความยากอยู่ที่ **มองหารูเปิด** ไม่ใช่ดันสายผ่าน
- รูเปิดอยู่ระหว่าง clitoris กับช่องคลอด · ในผู้สูงอายุ (เนื้อเยื่อฝ่อจากขาด estrogen) หรือคนอ้วน รูมักหลบเข้าไปที่ **ผนังด้านบนของช่องคลอด**
- สไลด์ (Difficult to insert — หญิง): **(1) สอดนิ้วเข้าช่องคลอด (2) ใส่สายใหม่เหนือนิ้ว**
- ท่อสั้นและใกล้ทวารหนัก → เชื้อจากฝีเย็บไต่ขึ้นตามผิวนอกของสายได้ง่าย = เหตุที่ผู้หญิงเกิด CAUTI ทางผิวนอก (extraluminal) บ่อย

| | ชาย | หญิง |
|---|---|---|
| ความยาว | ~18–20 ซม. | 3–4 ซม. |
| ใส่ลึกแค่ไหนก่อนเติมบอลลูน | **จนถึง bifurcation (สุดสาย)** | ถึงปัสสาวะไหล แล้วดันต่ออีก 2–3 ซม. |
| จุดยาก | sphincter · bulbar · prostate | หารูเปิด |
| ยึดสาย | หน้าท้อง | ต้นขาด้านใน |
""",
    ["ท่อปัสสาวะชาย: prostatic → membranous (external sphincter) → bulbar → penile",
     "จับองคชาตตั้ง 90° = ลบโค้ง prepubic เหลือโค้ง subpubic ที่ตายตัว",
     "ติดที่ sphincter → ให้หายใจลึก/เบ่งเหมือนปัสสาวะ อย่าดันแรง",
     "หญิง: ท่อสั้นตรง ความยากคือหารู — ผู้สูงอายุรูหลบที่ผนังบนช่องคลอด"],
    [mcq(N(9), "During urethral catheterization of an anxious 28-year-old man after appendicectomy, the catheter advances smoothly to about 16 cm and then meets firm resistance. He is tense and grimacing. What is the most likely cause and the best response?",
         ["Contraction of the external urethral sphincter; pause, ask him to breathe slowly and strain gently as if voiding while maintaining gentle steady pressure",
          "Benign prostatic hyperplasia; change to a 22 Fr coudé catheter immediately",
          "Meatal stenosis; dilate the meatus with forceps",
          "The catheter has entered the bladder; inflate the balloon now",
          "Urethral stricture; push firmly through the resistance"], 0,
         "ผู้ชายอายุน้อย สายผ่านไปได้ราว 15–17 ซม. แล้วติด = ระดับ **membranous urethra** ซึ่งมี **external sphincter (กล้ามเนื้อลาย)** ที่เกร็งเมื่อเจ็บหรือกลัว · แก้ด้วย lidocaine gel ให้พอ หยุดรอ ให้หายใจช้า ๆ และ **เบ่งเหมือนจะปัสสาวะ** (สไลด์: ask patient to strain) ซึ่งทำให้หูรูดคลาย แล้วดันต่อด้วยแรงคงที่เบา ๆ\n\n"
         "- **BPH** — อายุ 28 ไม่น่าใช่ และไม่ควรกระโดดไปใช้สายใหญ่\n- **Meatal stenosis** — จะติดตั้งแต่ปลายท่อ ไม่ใช่ 16 ซม.\n"
         "- **เติมบอลลูน** — ยังไม่มีปัสสาวะไหลและยังไม่ถึง bifurcation → บอลลูนจะพองในท่อ\n- **ดันแรงผ่าน** — สาเหตุหลักของ false passage",
         "ติดที่ sphincter → ผ่อนคลาย/เบ่งเหมือนปัสสาวะ ไม่ใช่ดัน", "External sphincter resistance", R("Difficult to insert (2)"), [ANAT, INNV, HARM]),
     mcq(N(10), "Why is the penis held perpendicular to the body with gentle upward traction during male urethral catheterization?",
         ["It straightens the mobile prepubic (penoscrotal) curve so that only the fixed subpubic curve remains",
          "It relaxes the internal urethral sphincter at the bladder neck",
          "It compresses the prostate and widens the prostatic urethra",
          "It prevents paraphimosis by keeping the foreskin retracted",
          "It closes the meatus so that the lidocaine gel does not leak out"], 0,
         "ท่อปัสสาวะชายมี 2 โค้ง: **prepubic** ที่มุม penoscrotal ซึ่ง **ขยับได้** และ **subpubic** ใต้หัวหน่าวซึ่ง **ตายตัว** · การจับองคชาตตั้งฉากแล้วดึงขึ้นเบา ๆ ทำให้โค้งแรกหายไป ท่อเป็นทางตรงยาว สายเลื่อนผ่านง่ายขึ้นและเหลือแค่โค้งเดียวที่สายต้องเลี้ยว\n\n"
         "- **internal sphincter** — เป็นกล้ามเนื้อเรียบ ควบคุมด้วย autonomic การจัดท่าไม่ทำให้คลาย\n- **กด prostate** — ไม่ได้ทำ\n"
         "- **paraphimosis** — ป้องกันด้วยการรูดหนังหุ้มกลับหลังใส่ ไม่เกี่ยวกับมุม\n- **กันเจลรั่ว** — ทำโดยบีบปลายองคชาตหลังฉีดเจล",
         "90° = ลบโค้ง prepubic", "Male urethral curves", R("Difficult to insert (2)"), [ANAT])],
    [ANAT, INNV, BPH], {"male_urethra": F.male_urethra(), "female": F.female()},
    source="ตำรากายวิภาค/urology (ไม่อยู่ในสไลด์) + สไลด์ Difficult to insert")

# ═════════════════════════════════════════════ 5
sec("nephro-cath-05", "ข้อห้าม — โดยเฉพาะ “สงสัยท่อปัสสาวะฉีกขาด”",
    "ไม่มีข้อห้ามสัมบูรณ์ · urethral trauma · urethritis/prostatitis · gross hematuria · traumatic hypospadias", 8,
"""### ข้อห้ามในสไลด์ (EAUN 2024)
> In general, **no "ABSOLUTE" contraindication** for these procedures ✓✓ — ทุกข้อด้านล่างเป็นข้อห้ามสัมพัทธ์ ต้องชั่งกับความจำเป็นในการระบาย และมักแก้ด้วย **เปลี่ยนวิธี** (เช่น suprapubic)

| Intermittent catheterization | Indwelling catheterization |
|---|---|
| มือไม่คล่อง (ถ้าจะให้ทำเองซ้ำ ๆ) | **Acute หรือ symptomatic chronic prostatitis** |
| **Urethral trauma** | **สงสัย urethral trauma** |
| Urethritis | **Traumatic hypospadias** จากสายค้างนาน (✍️ "รูออกผิดรู") |
| Prostatitis/UTI | |
| Gross hematuria ชัดเจน | |

#### ทำไมแต่ละข้อจึงเป็นข้อห้าม
| ภาวะ | ใส่สายแล้วเกิดอะไร | ทางเลือก |
|---|---|---|
| **Urethral injury** | ปลายสายออกนอกท่อเข้าก้อนเลือด → ฉีกบางส่วนกลายเป็นขาดทั้งหมด + นำเชื้อเข้าก้อนเลือด → stricture รุนแรงภายหลัง | retrograde urethrogram · **suprapubic catheter** |
| **Acute prostatitis** | ต่อมบวมเจ็บมาก การดันสายผ่านทำให้ปวดและอาจดันเชื้อเข้ากระแสเลือด | ระบายตามความเห็น urology (IC ครั้งเดียว/สายเล็ก หรือ suprapubic) |
| **Urethritis** | เยื่อบุอักเสบ เปราะ → บาดเจ็บง่าย และดันเชื้อขึ้นกระเพาะ | รักษาการอักเสบก่อนถ้ารอได้ |
| **Gross hematuria (สำหรับ IC)** | สายตรงขนาดเล็กอุดด้วยลิ่มเลือด ระบายไม่ได้ | 3-way catheter ขนาดใหญ่ + ล้างกระเพาะ |
| **Traumatic hypospadias** | รูเปิดถูกกัดผ่าลงจากสายที่กดนาน — ใส่ต่อยิ่งผ่ายาว | **suprapubic catheter** |

### สงสัย urethral injury — ตรวจก่อนใส่ทุกครั้งในผู้ป่วยอุบัติเหตุ
[[fig:injury]]
| สิ่งที่ตรวจพบ | กลไก |
|---|---|
| **เลือดที่ปลายท่อปัสสาวะ (blood at meatus)** | เลือดจากรอยฉีกไหลออกทางท่อ — สัญญาณสำคัญที่สุด |
| **prostate ยกสูง/คลำไม่ได้ (high-riding)** จาก DRE | prostate ยึดกับกระดูกหัวหน่าวด้วย puboprostatic ligament → เมื่อท่อขาดที่ bulbomembranous ก้อนเลือดดัน prostate ขึ้น |
| **ช้ำรูปผีเสื้อที่ฝีเย็บ/ถุงอัณฑะ** | เลือดจาก bulbar urethra ถูกกักโดย Colles' fascia |
| **ปัสสาวะไม่ออกทั้งที่กระเพาะเต็ม** | ท่อขาดต่อเนื่องไม่ได้ |
| **Pelvic fracture** (โดยเฉพาะ pubic rami/symphysis แยก) | แรงเฉือนที่ pelvic floor |
| หญิง: เลือดออกทางช่องคลอด/รอยฉีกช่องคลอดร่วมกับ pelvic fracture | พบน้อย แต่ต้องคิดถึง |

> แนวทาง (ATLS · EAU Urological Trauma — ไม่อยู่ในสไลด์): มีเลือดที่ meatus ในผู้ป่วยอุบัติเหตุ → **retrograde urethrogram ก่อน** · EAU อนุโลมให้ **ผู้มีประสบการณ์** ลองใส่อย่างนุ่มนวลได้หนึ่งครั้ง — นักศึกษา/แพทย์ทั่วไป **ไม่ควรลองเอง** ถ้าต้องวัดปัสสาวะใน shock ให้ปรึกษา urology เพื่อใส่ **suprapubic catheter**
""",
    ["ไม่มีข้อห้ามสัมบูรณ์ — แต่มีข้อห้ามที่ทำให้ “เปลี่ยนวิธี”",
     "Blood at meatus · high-riding prostate · perineal butterfly hematoma · pelvic fracture → ห้ามดันสาย ทำ RUG",
     "Urethral injury ที่ต้องระบาย → suprapubic catheter",
     "Traumatic hypospadias จากสายค้าง → เปลี่ยนเป็น suprapubic",
     "Acute prostatitis = ข้อห้ามของสายค้างทางท่อปัสสาวะ (EAUN)"],
    [mcq(N(11), "A 30-year-old man is brought in after a motorcycle crash. BP 86/50 mmHg, HR 128/min. Pelvic X-ray shows wide pubic symphysis diastasis. There is blood at the urethral meatus and a scrotal haematoma; the prostate cannot be palpated on rectal examination. Hourly urine output monitoring is needed. What is the most appropriate approach?",
         ["Insert a 14 Fr Foley catheter gently with extra lidocaine gel", "Insert an 18 Fr coudé catheter", "Retrograde urethrogram and urological drainage by suprapubic catheter if urethral injury is confirmed",
          "Insert a 3-way catheter and irrigate to clear blood", "Avoid any bladder drainage until the patient is haemodynamically stable"], 2,
         "เลือดที่ meatus + prostate คลำไม่ได้ (ยกสูง) + ช้ำที่ถุงอัณฑะ + pelvic fracture = **posterior urethral injury** จนกว่าจะพิสูจน์ได้ว่าไม่ใช่ · การดันสายสวนอาจทำให้ฉีกบางส่วนกลายเป็นขาดทั้งหมด หรือปลายสายเข้าไปในก้อนเลือด → ต้อง **retrograde urethrogram** และระบายด้วย **suprapubic catheter** (สไลด์: suspicion of urethral trauma = ข้อห้ามของสายค้าง)\n\n"
         "- **Foley/coudé** — ดันสายผ่านท่อที่อาจขาด (สายใหญ่หรือ coudé ไม่ได้ทำให้ปลอดภัยขึ้น)\n- **3-way irrigation** — สำหรับเลือดในกระเพาะ ไม่ใช่ท่อขาด\n"
         "- **ไม่ระบายเลย** — ผู้ป่วย shock ต้องวัดปัสสาวะ และกระเพาะที่เต็มจะรั่ว — ระบายได้ แต่ต้องผ่านทาง suprapubic",
         "Blood at meatus + high-riding prostate → RUG/suprapubic", "Suspected urethral injury", R("Contraindication for catheterization", "ATLS 10th ed · EAU Urological Trauma (ไม่อยู่ในสไลด์)"), [INJURY, SHOCK, ANAT]),
     mcq(N(12), "An 82-year-old bedbound man has had an indwelling urethral catheter for 2 years because of a hypocontractile bladder. The ventral meatus has eroded, splitting the glans down to the coronal sulcus. He still needs continuous drainage and cannot perform intermittent catheterization. What is the best option?",
         ["Replace with a larger 22 Fr urethral catheter to stop leakage", "Convert to a suprapubic catheter", "Use a latex catheter instead of silicone",
          "Tape the catheter more tightly to the thigh", "Change the urethral catheter weekly"], 1,
         "นี่คือ **traumatic (catheter-induced) hypospadias** — สายที่กดเยื่อบุด้านล่างของท่อปัสสาวะนาน ๆ (โดยเฉพาะเมื่อยึดลงต้นขา) ทำให้ขาดเลือดและกัดกร่อนจนรูเปิดผ่าลง · สไลด์ระบุเป็น **ข้อห้ามของสายค้างทางท่อปัสสาวะ** (BAUS-BAUN: urethral erosion → consider SPC) → เปลี่ยนเป็น **suprapubic catheter**\n\n"
         "- **สายใหญ่ขึ้น** — กดมากขึ้น ยิ่งกัดกร่อน และไม่ลดการรั่ว\n- **Latex** — ระคายเคืองมากกว่า ใช้ระยะสั้น\n"
         "- **ยึดที่ต้นขาให้แน่นขึ้น** — คือกลไกที่ทำให้เกิดแผล (ผู้ชายควรยึดที่หน้าท้อง)\n- **เปลี่ยนทุกสัปดาห์** — ไม่แก้แรงกด และเพิ่มการบาดเจ็บ",
         "Catheter hypospadias → SPC", "Urethral erosion from long-term catheter", R("Contraindication · Miscellaneous problems (1)", "BAUS-BAUN 2021"), [HARM, DEVICE, ANAT])],
    [INJURY, SHOCK, ANAT, HARM, CYST], {"injury": F.injury()},
    source=SRC + " + ATLS/EAU Urological Trauma (ส่วน urethral injury ไม่อยู่ในสไลด์)")

# ═════════════════════════════════════════════ 6
sec("nephro-cath-06", "เลือกสาย — ขนาด วัสดุ จำนวนทาง และปลายสาย",
    "French size ตามลักษณะปัสสาวะ (EAUN) · PVC/latex/silicone · 2-way vs 3-way · coudé/Tiemann", 8,
"""### ขนาด (French, Fr)
**Fr = เส้นรอบวงเป็นมิลลิเมตร ≈ 3 × เส้นผ่านศูนย์กลาง** (14 Fr ≈ 4.7 มม.) · ข้อต่อปลายสายมีรหัสสีตามขนาด (สไลด์มีแผ่นรหัสสี 6–24 Fr)

| ผู้ป่วย | ลักษณะปัสสาวะ | ขนาด (สไลด์ EAUN 2024) |
|---|---|---|
| เด็ก | – | 6–10 |
| ผู้ใหญ่ตัวเล็กมาก | ใส ไม่มีตะกอน | 10 |
| ผู้ใหญ่ | **ใส ไม่มีตะกอน/เลือด/กรวด** | **12–14** |
| ผู้ใหญ่ | ขุ่นเล็กน้อย เลือดเล็กน้อย ± ลิ่มเล็ก ตะกอน/กรวดน้อย | 16 |
| ผู้ใหญ่ | กรวด/ตะกอนปานกลาง–มาก | 18 |
| ผู้ใหญ่ | เลือดมีลิ่มปานกลาง | 18 |
| ผู้ใหญ่ | **เลือดออกมาก ต้องล้าง** | **20–24** (3-way) |

#### ทำไมไม่เลือกสายใหญ่ไว้ก่อน
สายใหญ่กดเยื่อบุท่อปัสสาวะมากขึ้นและปิดทางระบายของต่อม paraurethral → ขาดเลือด อักเสบ เป็น **stricture** และเพิ่มการระคายคอกระเพาะ (ปวดเกร็ง) · CDC: ใช้ **ขนาดเล็กที่สุดที่ระบายได้ดี**

✍️ ลายมือในสไลด์: **"สงสัย stricture → size เล็ก ๆ ✓"** · **"urine ข้น ๆ เหนียว ๆ + BPH → อาจลองเลย bigger size"** — สายใหญ่ **แข็งกว่า** จึงดันผ่าน prostate ที่โตได้โดยไม่ขด และรูใหญ่ไม่อุดด้วยตะกอน

### วัสดุ (สไลด์)
| วัสดุ | ข้อดี | ข้อจำกัด | ระยะเวลา |
|---|---|---|---|
| **PVC** (สาย intermittent) | ถูก ทน ยืดหยุ่น | ใช้ครั้งเดียว · อาจแพ้ | ใส่แล้วเอาออก |
| **Latex** | ถูก ยืดหยุ่น | ระคายเคือง/แพ้ latex ได้ · ? UTI มากกว่า · ไม่สบายกว่า | **ระยะสั้น < 14 วัน** (✍️ 2 weeks) |
| **Silicone** | ทน hypoallergenic เข้ากับร่างกาย · ผนังบาง รูในกว้างกว่าที่ Fr เดียวกัน | ราคาสูง | **4–12 สัปดาห์** (✍️ 3 months) |
แพ้ latex (เช่น spina bifida, บุคลากรการแพทย์) → silicone เสมอ · สายเคลือบยาฆ่าเชื้อ/silver **ไม่แนะนำใช้ประจำ** (CDC 2009)

### จำนวนทางและปลายสาย
[[fig:foley]]
- **2-way** = ทางปัสสาวะ + ทางเติมบอลลูน — สายค้างทั่วไป
- **3-way** = เพิ่มทางล้าง → **continuous bladder irrigation** หลัง TURP หรือเลือดออกมาก (เคสที่ 4 ในสไลด์) — น้ำล้างไหลเข้าไม่ให้เลือดจับเป็นลิ่มอุดสาย
- **Coudé / Tiemann** (สไลด์ Tiemann/Coudé Catheter!) = ปลายงอขึ้น 30–45° · ใช้ใน **BPH** ที่ prostate ยกคอกระเพาะสูง — ปลายชี้ **12 นาฬิกา** เลี้ยวข้ามติ่งได้ · ห้ามหมุนปลายลง
- **Council-tip** = ปลายมีรู ใส่ตาม guidewire (งานของ urologist — อยู่ใน flowchart ของ Campbell)
- **Suprapubic catheter** = ใช้สาย Foley/silicone ใส่ผ่านผนังหน้าท้อง
""",
    ["Fr = เส้นรอบวง (มม.) ≈ 3 × เส้นผ่านศูนย์กลาง",
     "ปัสสาวะใสในผู้ใหญ่ 12–14 Fr · เลือดมาก ต้องล้าง 20–24 Fr 3-way",
     "Stricture → สายเล็ก · BPH → สายใหญ่ขึ้น/coudé",
     "Latex < 14 วัน · Silicone 4–12 สัปดาห์ · แพ้ latex → silicone",
     "Coudé: ปลายชี้ 12 นาฬิกาตลอด"],
    [mcq(N(13), "A 68-year-old man returns from transurethral resection of the prostate (TURP). His urine is heavily blood-stained with clots. Which catheter is most appropriate?",
         ["12 Fr 2-way latex Foley", "16 Fr 2-way silicone Foley", "14 Fr coudé intermittent catheter", "20–24 Fr 3-way catheter with continuous bladder irrigation", "Male external catheter"], 3,
         "เลือดออกมากและมีลิ่ม (หลัง TURP — เคสที่ 4 ในสไลด์) → ตารางขนาดของ EAUN: **heavy hematuria, need for flushing = 20–24 Fr** และต้องเป็น **3-way** เพื่อล้างกระเพาะต่อเนื่อง — น้ำไหลเข้าทางที่สามและออกทางระบายตลอด ทำให้เลือดเจือจางไม่จับเป็นลิ่มที่อุดสาย (clot retention)\n\n"
         "- **12/16 Fr 2-way** — รูเล็กเกิน ลิ่มเลือดอุด และล้างต่อเนื่องไม่ได้\n- **Coudé intermittent** — ใช้ผ่าน prostate ที่โต ไม่ใช่ระบายเลือด\n- **External** — ไม่ได้ระบายกระเพาะ",
         "เลือดมาก ต้องล้าง → 20–24 Fr 3-way", "Catheter size selection", R("Size of catheter selection · Scenario Case 04"), [HEMAT, BPH, DEVICE]),
     mcq(N(14), "A 45-year-old woman with spina bifida needs an indwelling catheter for about 8 weeks while awaiting reconstructive surgery. She reports lip swelling after dental procedures with rubber dams. Which catheter material is most appropriate?",
         ["Latex Foley, changed every 2 weeks", "Silicone Foley", "PVC (Nelaton) catheter left indwelling", "Silver-alloy-coated latex Foley", "Hydrogel-coated latex Foley"], 1,
         "ผู้ป่วย spina bifida มีความเสี่ยง **แพ้ latex** สูงมาก (ประวัติปากบวมจาก rubber dam) และต้องค้างสาย **8 สัปดาห์** → **silicone** ซึ่ง hypoallergenic ทนทาน และใช้ได้ **4–12 สัปดาห์** ตามสไลด์\n\n"
         "- **Latex ทุกแบบ (เคลือบ silver/hydrogel ก็ยังมี latex)** — แพ้ได้ถึง anaphylaxis และ latex เหมาะกับระยะสั้น < 14 วัน\n"
         "- **PVC Nelaton** — สายตรงสำหรับ IC ใช้ครั้งเดียว ไม่มีบอลลูน ค้างไม่ได้",
         "แพ้ latex/ใช้นาน → silicone", "Catheter material", R("Material of catheter selection"), [DEVICE, HARM])],
    [DEVICE, HEMAT, BPH, HARM], {"foley": F.foley()}, source=SRC + " + CDC/HICPAC 2009")

# ═════════════════════════════════════════════ 7
sec("nephro-cath-07", "ขั้นตอนการใส่สายค้าง — ทุกขั้นมีเหตุผล",
    "ยินยอม → aseptic → lidocaine gel รอ 3–5 นาที → ดันถึง bifurcation → เห็นปัสสาวะ → sterile water → รูดหนังหุ้มกลับ → ยึดสาย → ถุงต่ำ", 10,
"""(handout ส่วน "How to do?" มีเฉพาะการเลือกขนาด/วัสดุ/การยึด/การดูแล — ขั้นตอนทีละขั้นด้านล่างอิง CDC/HICPAC 2009, EAUN 2024 และแนวปฏิบัติมาตรฐาน)

### ก่อนเริ่ม
| ขั้น | ทำอะไร | ทำไม |
|---|---|---|
| 1 | ทบทวน **ข้อบ่งชี้** และ **ข้อห้าม** (blood at meatus? pelvic fracture? เคยผ่าตัด prostate/stricture?) · ถ้าสงสัยคั่ง → **bladder scan ก่อน** | ไม่ใส่สายที่ไม่จำเป็น และไม่ดันสายในท่อที่ฉีก |
| 2 | แนะนำตัว อธิบาย ขอ **ความยินยอม** · ถามประวัติ **แพ้ latex/lidocaine/น้ำยา** · ความเป็นส่วนตัว + ผู้ช่วย/chaperone | ผู้ป่วยร่วมมือ = หูรูดคลาย |
| 3 | เตรียมของ: ชุดสวนปลอดเชื้อ สาย (ผู้ใหญ่ 12–14 Fr) **ต่อกับถุงระบบปิดไว้ก่อน** · ถุงมือปลอดเชื้อ · 2% lidocaine gel แบบใช้ครั้งเดียว · syringe + **sterile water** · อุปกรณ์ยึดสาย | ต่อถุงก่อนไม่ต้องเปิดระบบภายหลัง |
| 4 | **ล้างมือ** · ท่านอนหงาย (หญิง: frog-leg) | CDC 1b |

### ผู้ชาย
| ขั้น | ทำอะไร | ทำไม |
|---|---|---|
| 5 | ใส่ถุงมือปลอดเชื้อ ปูผ้า · มือที่ไม่ถนัดจับองคชาต (มือนี้ "ไม่ปลอดเชื้อ" แล้ว) | แยกมือสะอาด/มือปลอดเชื้อ |
| 6 | **รูดหนังหุ้มลง** ทำความสะอาด meatus วนจากรูออกด้านนอก | ไม่ลากเชื้อเข้าหารู |
| 7 | ฉีด **lidocaine gel ~10 mL เข้าท่อช้า ๆ** บีบปลายไว้ **รอ 3–5 นาที** | ต้องใช้เวลาให้ยาชาออกฤทธิ์ · gel หล่อลื่นและขยายท่อทั้งความยาว → เจ็บน้อย หูรูดไม่เกร็ง เยื่อบุไม่ถลอก |
| 8 | จับองคชาต **ตั้งฉาก 90°** ดึงขึ้นเบา ๆ ดันสายด้วยแรงสม่ำเสมอ ผ่านจุดต้านให้หายใจลึก/เบ่งเหมือนปัสสาวะ | ลบโค้ง prepubic · หูรูดนอกคลาย |
| 9 | ดัน **จนสุดถึง bifurcation** → รอเห็นปัสสาวะไหล | บอลลูนต้องพ้น prostatic urethra (ดูภาพด้านล่าง) |
| 10 | เติม **sterile water ตามปริมาตรที่ระบุบนสาย (มักเป็น 10 mL)** ช้า ๆ — ถ้าผู้ป่วยปวดมาก **หยุด ดูดออก** ดันเข้าอีก | ปวดตอนเติม = บอลลูนอยู่ในท่อ |
| 11 | ดึงกลับเบา ๆ จนรู้สึกติด | บอลลูนพักที่คอกระเพาะ ระบายได้หมด |
| 12 | **รูดหนังหุ้มกลับคลุม glans** | ป้องกัน **paraphimosis** (หัวข้อ 10) |
| 13 | ยึดสายที่ **หน้าท้อง** · ถุง **ต่ำกว่ากระเพาะ ไม่แตะพื้น** · ล้างมือ | ป้องกันแรงดึง/แผล และปัสสาวะไหลย้อน |
| 14 | บันทึก: วันเวลา ข้อบ่งชี้ ขนาด/ชนิดสาย ปริมาตรน้ำในบอลลูน **ปริมาณปัสสาวะที่ระบายครั้งแรก** ลักษณะปัสสาวะ ปัญหา และ **วันที่วางแผนถอด** | ใช้ประเมิน post-obstructive diuresis และเตือนให้ถอดเร็ว |

[[fig:balloon]]

### ผู้หญิง — ที่ต่างจากผู้ชาย
- แยก labia ด้วยมือที่ไม่ถนัดค้างไว้ตลอดจนสายเข้า · ทำความสะอาด **จากหน้าไปหลัง** (จากรูเปิดไปทางทวารหนัก) — ไม่ลากเชื้อลำไส้มาที่รู
- ท่อสั้น: ใส่จนปัสสาวะไหล แล้ว **ดันต่ออีกราว 2–3 ซม.** ก่อนเติมบอลลูน
- **สายเข้าช่องคลอด** → ทิ้งไว้เป็นจุดสังเกต ใช้สายปลอดเชื้อเส้นใหม่ใส่ด้านบน (หัวข้อ 9)
- ยึดสายที่ **ต้นขาด้านใน**

### ทำไมใช้ sterile water ไม่ใช่ NSS เติมบอลลูน
NaCl ตกผลึกในทางเติมบอลลูนเล็ก ๆ ได้เมื่อค้างนาน → **อุดทาง → ดูดน้ำออกไม่ได้ = บอลลูนแฟบไม่ลง** (หัวข้อ 10) · ใช้ปริมาตร **ตามที่ผู้ผลิตกำหนด** (BAUS-BAUN: no more, no less) — น้อยไปบอลลูนเบี้ยว ปลายสายเอียงชนผนัง / มากไประคายคอกระเพาะ ปวดเกร็ง

### การยึดสาย (สไลด์ Fixation of Catheter)
[[fig:fixation]]
""",
    ["Lidocaine gel ต้องรอ 3–5 นาที — ทั้งชาและหล่อลื่น",
     "ผู้ชาย: ดันถึง bifurcation ก่อนเติมบอลลูน · ปัสสาวะไหลอย่างเดียวไม่พอ",
     "ปวดตอนเติมบอลลูน → หยุด ดูดออก ดันลึกขึ้น",
     "Sterile water ตามปริมาตรบนสาย (มัก 10 mL) — NSS ตกผลึกจนบอลลูนแฟบไม่ลง",
     "จบทุกครั้ง: รูดหนังหุ้มกลับ · ยึดสายที่หน้าท้อง (ชาย)/ต้นขา (หญิง) · ถุงต่ำกว่ากระเพาะ"],
    [mcq(N(15), "An intern inserts a 16 Fr Foley catheter in a 74-year-old man with a large prostate. After about 14 cm, urine appears in the tubing, so he inflates the balloon with 10 mL. The patient cries out in severe pain and blood appears at the meatus. What is the most likely explanation?",
         ["The balloon was inflated in the prostatic urethra because the catheter had not been advanced to the bifurcation",
          "Sterile water instead of saline caused osmotic rupture of the balloon", "The catheter entered a urethral diverticulum in the penile urethra",
          "Lidocaine gel caused a chemical urethritis", "The balloon was overfilled; 10 mL exceeds the recommended volume"], 0,
         "รูรับปัสสาวะอยู่ปลายสุด ห่างจากบอลลูนไม่กี่เซนติเมตร และ prostatic urethra ใน BPH ยาวมาก → **ปัสสาวะไหลได้ตั้งแต่ปลายสายพ้น bladder neck ทั้งที่บอลลูนยังอยู่ในท่อ** · การเติมน้ำตอนนั้นทำให้บอลลูนพองในท่อที่แคบ → ปวดรุนแรง ท่อฉีก เลือดออก และเป็น stricture ภายหลัง · ป้องกันโดย **ดันสายจนสุดถึง bifurcation ก่อนเติมเสมอ** (ผู้ชาย)\n\n"
         "- **Sterile water** — คือของที่ถูกต้อง ไม่ทำให้บอลลูนแตก\n- **Diverticulum** — พบน้อย และจะไม่มีปัสสาวะไหล\n"
         "- **Lidocaine gel** — ไม่ทำให้ปวดเฉียบพลันขณะเติมบอลลูน\n- **10 mL** — เป็นปริมาตรมาตรฐานของบอลลูนทั่วไป",
         "ผู้ชาย: เห็นปัสสาวะยังไม่พอ ต้องดันถึง bifurcation", "Balloon inflation in the urethra", ["หลักปฏิบัติมาตรฐาน / EAUN 2024 (ไม่อยู่ในสไลด์)"], [HARM, DEVICE, ANAT, BPH]),
     mcq(N(16), "Why is sterile water, rather than 0.9% saline, recommended for inflating the balloon of a standard Foley catheter?",
         ["Saline can crystallise in the narrow inflation channel, so the balloon may fail to deflate",
          "Saline is hypotonic and leaks out of the balloon",
          "Water is radiolucent whereas saline is radio-opaque",
          "Saline irritates the trigone if the balloon leaks and causes bladder spasm",
          "Water is cheaper; there is no clinical difference"], 0,
         "ทางเติมบอลลูนเป็นช่องเล็กมาก · NaCl ที่ค้างนาน **ตกผลึกอุดช่อง** → ดูดน้ำออกไม่ได้ = **balloon ไม่แฟบ** ถอดสายไม่ได้ (ปัญหาในตาราง BAUS-BAUN ของสไลด์) · จึงใช้ **sterile water** (หรือสายที่บรรจุน้ำมาแล้ว) ในปริมาตรที่ผู้ผลิตกำหนด\n\n"
         "- **Saline hypotonic** — ผิด NSS เป็น isotonic\n- **ความทึบรังสี** — ทั้งสองโปร่งรังสีเท่ากัน\n"
         "- **ระคาย trigone** — ไม่ใช่เหตุผลหลัก\n- **ไม่มีความต่าง** — มีความต่างทางคลินิก",
         "Sterile water เติมบอลลูน — NSS ตกผลึกจนแฟบไม่ลง", "Balloon inflation fluid", ["EAUN 2024 · หลักปฏิบัติมาตรฐาน (ไม่อยู่ในสไลด์)"], [DEVICE, HARM])],
    [DEVICE, HARM, ANAT, PARA], {"balloon": F.balloon(), "fixation": F.fixation()},
    source="CDC/HICPAC 2009 · EAUN 2024 · หลักปฏิบัติมาตรฐาน (ขั้นตอนทีละขั้นไม่อยู่ในสไลด์) + สไลด์ Fixation of catheter")

# ═════════════════════════════════════════════ 8
sec("nephro-cath-08", "ดูแลสายและ CAUTI — biofilm กับ “ถอดให้เร็วที่สุด”",
    "เส้นทางเชื้อ 2 ทาง · biofilm · นิยาม CAUTI (IDSA 2009) · รักษา · bundle ป้องกัน (CDC 2009, EAUN 2024)", 10,
"""### การดูแลสายในสไลด์ (EAUN 2024)
| คำแนะนำ | LE | GR |
|---|---|---|
| **ล้างมือทันทีก่อนและหลัง** จับสายหรือระบบทุกครั้ง · ใส่ถุงมือใช้แล้วทิ้งเมื่อจับระบบ | 1b | B |
| ให้ปัสสาวะไหลสะดวก ไม่ให้สายและท่อพับ | 1b | B |
| **ถุงต่ำกว่าระดับกระเพาะตลอดเวลา ไม่วางบนพื้น** | 1b | B |

[[fig:bag]]

### เชื้อเข้าทางไหน — และทำไมรักษาด้วยยาอย่างเดียวไม่พอ
[[fig:cauti]]
- **Extraluminal (ผิวนอก)** ~2 ใน 3 — เชื้อจากฝีเย็บ/ลำไส้ไต่ขึ้นในชั้นเมือกระหว่างสายกับเยื่อบุ · เกิดตั้งแต่ตอนใส่ (เทคนิคไม่ปลอดเชื้อ) หรือช่วงแรก · พบมากในผู้หญิง
- **Intraluminal (ในท่อ)** — ระบบปิดถูกเปิด/ถอดข้อต่อ · ก๊อกถุงปนเปื้อน · **ถุงถูกยกสูงจนปัสสาวะไหลย้อน**
- **Biofilm**: เชื้อเกาะผิวสาย สร้างเมือก polysaccharide · ยาและเม็ดเลือดขาวเข้าไม่ถึง เชื้อในนั้นโตช้าจึงดื้อยา → bacteriuria เพิ่ม **3–7% ต่อวัน** · BAUS-BAUN (สไลด์): **ค้างเกิน 4 สัปดาห์ แทบทุกรายมีเชื้อ** · Proteus/Providencia สร้าง urease → ปัสสาวะด่าง → struvite เกาะ (encrustation) → **สายอุด**

### CAUTI — นิยาม (IDSA 2009 — ไม่อยู่ในสไลด์)
อาการ/อาการแสดงที่เข้าได้กับ UTI **โดยไม่มีแหล่งติดเชื้ออื่น** + เพาะเชื้อ **≥ 10³ CFU/mL** จากปัสสาวะในสาย (หรือ midstream ภายใน 48 ชม.หลังถอดสาย)
#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | หมายเหตุ |
|---|---|---|
| **ไข้ หนาวสั่น** | เชื้อจาก biofilm ขึ้นไปไต/prostate หรือเข้ากระแสเลือด → cytokine | อาการที่พบบ่อยที่สุด — มักไม่มีอาการเฉพาะที่ |
| **ไม่มีแสบขัด/ปัสสาวะบ่อย** | สายระบายตลอด กระเพาะไม่เคยเต็ม และไม่มีปัสสาวะผ่านท่อ | ทำให้วินิจฉัยยาก ต้องตัดแหล่งอื่นก่อน |
| **ปวดสีข้าง/เคาะเจ็บ CVA** | pyelonephritis — เชื้อขึ้นตามท่อไต | complicated UTI |
| **สับสน ซึม** ในผู้สูงอายุ | ตอบสนองต่อการติดเชื้อทั้งระบบ | ต้องไม่มีสาเหตุอื่น |
| **ปวดท้องน้อย/ปวดเกร็ง ปัสสาวะรั่วรอบสาย** | กระเพาะอักเสบ → detrusor บีบ | แยกจาก CRBD/สายอุด |
| ปัสสาวะขุ่น มีกลิ่น | ตะกอน/เมือก/เชื้อ | **อย่างเดียวไม่ใช่ข้อบ่งชี้ส่งเพาะเชื้อหรือให้ยา** · pyuria ก็ใช้วินิจฉัยไม่ได้ |

### รักษา CAUTI (IDSA 2009)
1. เก็บปัสสาวะเพาะเชื้อ **ก่อน** ให้ยา — จาก **sampling port** ด้วยเทคนิคปลอดเชื้อ **ไม่ใช่จากถุง**
2. สายค้าง **> 2 สัปดาห์** และยังจำเป็น → **เปลี่ยนสายใหม่ และเก็บเพาะเชื้อจากสายใหม่** (สายเก่ามี biofilm — ผลเพาะเชื้อปนเชื้อที่เกาะสาย และยาเข้าไม่ถึง) · ไม่จำเป็นแล้ว → ถอด
3. ระยะเวลา: **7 วัน** ถ้าตอบสนองเร็ว · **10–14 วัน** ถ้าตอบสนองช้า
4. **Bacteriuria ที่ไม่มีอาการ (CA-ASB)** — **ไม่ตรวจคัดกรองและไม่รักษา** (ยกเว้นหญิงตั้งครรภ์ และก่อนหัตถการทางเดินปัสสาวะที่มีเลือดออก) — เชื้อกลับมาเสมอตราบที่สายยังอยู่ ให้ยาก็ได้แต่เชื้อดื้อยา

### Bundle ป้องกัน CAUTI (CDC/HICPAC 2009 + EAUN 2024)
| ป้องกันอะไร | ทำ | ไม่ทำ |
|---|---|---|
| ไม่ใส่โดยไม่จำเป็น | ใส่เฉพาะข้อบ่งชี้ · ใช้ external/IC/bladder scan แทน | ใส่เพื่อความสะดวก |
| ใส่อย่างปลอดเชื้อ | ล้างมือ ถุงมือ/ผ้าปลอดเชื้อ gel ใช้ครั้งเดียว สายเล็กที่สุดที่ระบายได้ | – |
| รักษาระบบปิด | ไม่ถอดข้อต่อ · ถ้าระบบเปิด/รั่ว → **เปลี่ยนทั้งสายและถุง** | ล้างกระเพาะ (irrigation) เป็นประจำ |
| ระบายทางเดียว | ถุงต่ำกว่ากระเพาะ ไม่แตะพื้น ไม่พับ · เทถุงด้วยภาชนะแยกรายคน | ยกถุงขึ้นตอนย้ายเตียงโดยไม่หนีบสาย |
| ทำความสะอาด | ทำความสะอาด meatus ตามปกติตอนอาบน้ำ | ทา antiseptic รอบ meatus ทุกวัน |
| **ถอดเร็ว** | **ทบทวนทุกวัน** · nurse-driven removal protocol · ระบบเตือน · หลังผ่าตัดถอดใน 24 ชม. | เปลี่ยนสาย/ถุงตามรอบเวลาที่กำหนดตายตัว · ยาปฏิชีวนะป้องกัน · clamp ก่อนถอด |

> การป้องกันที่ได้ผลที่สุดคือ **ไม่ใส่** และ **ถอดเร็ว** — ทุกวันที่สายอยู่เพิ่มความเสี่ยง
""",
    ["Extraluminal (ผิวนอก) ~2/3 · intraluminal เมื่อระบบเปิด/ถุงไหลย้อน",
     "Biofilm → ยาเข้าไม่ถึง → สายค้าง > 2 สัปดาห์ที่เป็น CAUTI ให้เปลี่ยนสายและเพาะเชื้อจากสายใหม่",
     "CAUTI: อาการ + ≥ 10³ CFU/mL · ปัสสาวะขุ่น/มีกลิ่น หรือ pyuria อย่างเดียวไม่พอ",
     "รักษา 7 วัน (ตอบสนองเร็ว) · 10–14 วัน (ตอบสนองช้า)",
     "ไม่คัดกรอง/ไม่รักษา CA-ASB · ไม่ให้ยาป้องกัน · ไม่เปลี่ยนสายตามรอบ"],
    [mcq(N(17), "In women with a short-term indwelling urethral catheter, by which route do most bacteria that cause catheter-associated bacteriuria reach the bladder?",
         ["Extraluminally, ascending from the perineum along the outside of the catheter in the mucous film between catheter and urethra",
          "Intraluminally, by reflux from the drainage bag", "Haematogenous seeding of the bladder wall", "Lymphatic spread from the rectum", "Descending infection from the kidney"], 0,
         "เชื้อส่วนใหญ่ (~2 ใน 3) ขึ้น **ทางผิวนอกของสาย (extraluminal)** — เชื้อจากลำไส้ที่อยู่บริเวณฝีเย็บ/รูเปิด ไต่ขึ้นในชั้นเมือกระหว่างสายกับเยื่อบุ ซึ่งผู้หญิงท่อสั้นและใกล้ทวารหนักจึงเกิดง่าย · ป้องกันด้วยเทคนิคปลอดเชื้อตอนใส่ ยึดสายไม่ให้ขยับเข้า–ออก และถอดเร็ว\n\n"
         "- **Intraluminal** — เกิดได้ (ระบบเปิด ถุงไหลย้อน) แต่เป็นส่วนน้อย\n- **Haematogenous / lymphatic / descending** — ไม่ใช่กลไกหลักของ CAUTI",
         "CAUTI ส่วนใหญ่มาทางผิวนอกสาย", "Pathogenesis of CAUTI", ["CDC/HICPAC CAUTI 2009 · IDSA 2009 (ไม่อยู่ในสไลด์)", "สไลด์ อ.ธนิศร — Miscellaneous problems (1)"], [CYST, BIOFILM, PATHO]),
     mcq(N(18), "An 81-year-old man with BPH has had an indwelling urethral catheter for 3 weeks. He develops fever 38.8 °C, rigors and right costovertebral-angle tenderness. Chest X-ray and other examination show no alternative source. The catheter is still needed. What is the best management?",
         ["Send urine from the drainage bag for culture and start antibiotics through the existing catheter",
          "Replace the catheter, send urine for culture from the newly placed catheter, then start empirical antibiotics",
          "Start antibiotics without culture and continue for 21 days", "Perform antibiotic bladder irrigation through the existing catheter",
          "Observe; fever with a catheter is usually colonisation"], 1,
         "นี่คือ **CAUTI (น่าจะ pyelonephritis)** — ไข้ หนาวสั่น CVA tenderness ไม่มีแหล่งอื่น · IDSA 2009: สายค้าง **> 2 สัปดาห์** และยังจำเป็น → **เปลี่ยนสายใหม่ แล้วเก็บเพาะเชื้อจากสายใหม่** ก่อนให้ยา — สายเก่ามี **biofilm** ซึ่งทำให้ผลเพาะเชื้อปนเชื้อที่เกาะสาย และยาเข้าไม่ถึงเชื้อในเมือก · ให้ยา **7 วัน** ถ้าตอบสนองเร็ว (10–14 วันถ้าช้า)\n\n"
         "- **เพาะเชื้อจากถุง** — เชื้อในถุงโตเพิ่มและปนเปื้อน ไม่สะท้อนเชื้อในกระเพาะ\n- **ไม่เพาะเชื้อ + 21 วัน** — ต้องมีผลเพาะเชื้อเพื่อปรับยา และนานเกิน\n"
         "- **Antibiotic irrigation** — ไม่แนะนำ ไม่ได้ผลและเปิดระบบปิด\n- **สังเกตอาการ** — มีอาการทั้งระบบ = ต้องรักษา (ต่างจาก ASB)",
         "CAUTI + สาย > 2 สัปดาห์ → เปลี่ยนสาย เพาะเชื้อจากสายใหม่", "Management of CAUTI", ["IDSA CA-UTI Guideline 2009 (ไม่อยู่ในสไลด์)", "สไลด์ อ.ธนิศร — Miscellaneous problems (1)"], [PYELO, PYELO_B, FEVER, CULT, BIOFILM]),
     mcq(N(19), "A hospital infection-control team wants to reduce catheter-associated UTI on its medical wards. Which intervention is supported by CDC/HICPAC 2009 guidance?",
         ["Routine catheter and bag changes every 2 weeks", "Daily cleaning of the meatus with povidone-iodine",
          "Weekly screening urine cultures with treatment of bacteriuria", "A daily review of catheter necessity with a nurse-driven removal protocol",
          "Prophylactic oral antibiotics while the catheter is in place"], 3,
         "หัวใจของ bundle ป้องกัน CAUTI คือ **ลดจำนวนวันที่มีสาย** — ทบทวนทุกวันว่ายังจำเป็นไหม และให้พยาบาลถอดได้ตามเกณฑ์ (**nurse-driven removal protocol**/ระบบเตือน) · CDC/HICPAC 2009 แนะนำ\n\n"
         "- **เปลี่ยนสาย/ถุงตามรอบ** — CDC ไม่แนะนำ (เปลี่ยนตามข้อบ่งชี้ เช่น อุดตัน ติดเชื้อ ระบบรั่ว)\n- **ทา antiseptic รอบ meatus ทุกวัน** — ไม่ลด CAUTI ทำความสะอาดตามปกติพอ\n"
         "- **คัดกรอง + รักษา bacteriuria** — ไม่ลดการติดเชื้อที่มีอาการ แต่เพิ่มเชื้อดื้อยา\n- **ยาปฏิชีวนะป้องกัน** — ไม่แนะนำด้วยเหตุผลเดียวกัน (BAUS-BAUN ในสไลด์: usually ineffective)",
         "ป้องกัน CAUTI = ไม่ใส่ + ถอดเร็ว", "CAUTI prevention bundle", ["CDC/HICPAC CAUTI 2009 (ไม่อยู่ในสไลด์)", "สไลด์ อ.ธนิศร — Catheter care · Miscellaneous problems (1)"], [CYST, DEVICE, RESIST])],
    [CYST, CYST_B, PYELO, PYELO_B, FEVER, BIOFILM, PATHO, RESIST, UA, CULT, SPEC, DEVICE, HARM], {"cauti": F.cauti(), "bag": F.bag()},
    source=SRC + " (Catheter care · BAUS-BAUN) + CDC/HICPAC 2009 + IDSA 2009")

# ═════════════════════════════════════════════ 9
sec("nephro-cath-09", "Troubleshooting 1 — ใส่ไม่เข้า และใส่แล้วไม่มีปัสสาวะ",
    "4 ขั้นในสไลด์ (gel · 90° + เบ่ง · เปลี่ยนขนาด · Tiemann) · flowchart Campbell · หญิง: นิ้วนำ · ไม่มีปัสสาวะออก", 9,
"""### ใส่ไม่เข้า — ผู้ชาย (สไลด์ Difficult to Insert!!)
1. **ฉีด sterile lubricant (lidocaine gel) เข้าท่อปัสสาวะโดยตรง** — ไม่ใช่แค่ทาที่สาย
2. **จับองคชาตตั้ง 90° และให้ผู้ป่วยเบ่ง** (เหมือนจะปัสสาวะ) — ลบโค้ง prepubic และให้ external sphincter คลาย
3. **เปลี่ยนขนาด — เล็กลงถ้าเป็น stricture · ใหญ่ขึ้นถ้าเป็น BPH**
4. **ใช้ปลาย Tiemann (coudé)** — ปลายงอชี้ 12 นาฬิกาเลี้ยวข้าม prostate/bladder neck ที่ยกสูง

#### ทำไม BPH ต้อง "ใหญ่ขึ้น" แต่ stricture ต้อง "เล็กลง"
| ปัญหา | สิ่งที่ขวาง | สายแบบไหนผ่าน |
|---|---|---|
| **BPH** | ท่อไม่ได้แคบเป็นวง แต่ **ยาวและคดเคี้ยว** prostate สองข้างเบียดและคอกระเพาะยกสูง | สาย **ใหญ่/แข็ง** ไม่งอขดในท่อ · ปลาย **coudé** เลี้ยวขึ้นข้ามติ่ง |
| **Stricture** | **วงแผลเป็นที่แคบ** (มักที่ bulbar — เคย UTI/STI ใส่สาย/ส่องกล้อง/อุบัติเหตุ) | สาย **เล็ก** ลอดผ่านช่องแคบ · ติดตั้งแต่ส่วนต้น (penile/bulbar) |

[[fig:trouble]]

**ห้ามดันแรง** — แรงที่ใช้ต้องเท่ากับที่ใช้ตอนผ่านปกติ · สัญญาณว่าเข้าผิดทาง: เลือดออกจาก meatus · ผู้ป่วยปวดมาก · สายเข้าไปลึกแต่ไม่มีปัสสาวะ → หยุด **ห้ามเติมบอลลูน** ปรึกษา urology · ถ้ากระเพาะโป่งและระบายด่วน = **suprapubic catheter**

### ใส่ไม่เข้า — ผู้หญิง
หารูไม่เจอในผู้สูงอายุ/อ้วน (สไลด์มีภาพหญิงอ้วนมาก): **สอดนิ้วเข้าช่องคลอด แล้วใส่สายเหนือนิ้ว** · จัดท่า/ให้ผู้ช่วยแยกขา ใช้ไฟส่องให้ดี

### ใส่แล้ว "ไม่มีปัสสาวะ"
| สาเหตุ | ตรวจ/แก้ |
|---|---|
| **หญิง: สายเข้าช่องคลอด** | ทิ้งสายไว้เป็นจุดสังเกต ใช้สายปลอดเชื้อเส้นใหม่ใส่ด้านบน (สายเดิมปนเปื้อน ห้ามดึงมาใส่ท่อปัสสาวะ) |
| **ชาย: ยังไม่ถึงกระเพาะ** — สายขดใน bulbar/ติด prostate | ดันต่อจนถึง bifurcation · ถ้าดันไม่ได้ ห้ามเติมบอลลูน |
| **gel อุดรูรับปัสสาวะ** | กดท้องน้อยเบา ๆ · ฉีด sterile saline 20–30 mL ผ่านสายแล้วดูว่าไหลกลับ |
| **กระเพาะว่างจริง** (เพิ่งปัสสาวะ หรือไตไม่สร้างปัสสาวะ) | **bladder scan ก่อนใส่** ช่วยตัดได้ · ถ้า oliguria → คิดถึง pre-renal/AKI ไม่ใช่ปัญหาสาย |
| **สาย/ท่อพับ** | ตรวจตลอดแนวจนถึงถุง |
""",
    ["ใส่ไม่เข้า: gel เข้าท่อ → 90° + เบ่ง → เปลี่ยนขนาด → Tiemann",
     "Stricture → สายเล็ก · BPH → สายใหญ่/coudé (สายนิ่มเล็กจะขด)",
     "เลือดออก ปวดมาก ไม่มีปัสสาวะ = เข้าผิดทาง → หยุด ห้ามเติมบอลลูน",
     "หญิงหารูไม่เจอ → นิ้วในช่องคลอด สายเหนือนิ้ว · สายเข้าช่องคลอด → ทิ้งไว้ ใช้สายใหม่",
     "ไม่มีปัสสาวะ: ตำแหน่งสาย · gel อุด · กระเพาะว่าง · สายพับ"],
    [mcq(N(20), "A 79-year-old man with BPH (prostate ~80 mL) is in acute urinary retention. A 14 Fr straight Foley catheter passes 16 cm and then stops; a second attempt with more lidocaine gel and the penis held at 90° also fails. There is no blood at the meatus. What is the most appropriate next step?",
         ["Try a 10 Fr straight catheter because it is easier to pass", "Push more firmly with the 14 Fr catheter while rotating it",
          "Use a 16–18 Fr coudé (Tiemann) catheter with the tip pointing at 12 o'clock", "Inflate the balloon where it stops to anchor it and drain",
          "Make repeated attempts with the same catheter until it passes"], 2,
         "ติดที่ระดับ prostate ใน BPH → สไลด์: **ใช้สายใหญ่ขึ้นใน BPH** และ **ปลาย Tiemann** · Campbell: สงสัย prostate อุด → **18 Fr coudé** — สายใหญ่แข็งไม่ขด ปลายงอ **ชี้ 12 นาฬิกา** เลี้ยวขึ้นข้ามติ่ง prostate/คอกระเพาะที่ยกสูง\n\n"
         "- **สาย 10 Fr** — นิ่มกว่า ยิ่งขดในท่อที่คด (สายเล็กใช้กับ stricture)\n- **ดันแรง/หมุน** — สาเหตุของ false passage\n"
         "- **เติมบอลลูนตรงที่ติด** — บอลลูนพองใน prostatic urethra → ฉีก เลือดออก\n- **ลองซ้ำ ๆ แบบเดิม** — เพิ่มการบาดเจ็บ ถ้าไม่สำเร็จต้องปรึกษา urology",
         "BPH ใส่ไม่เข้า → 16–18 Fr coudé ชี้ 12 นาฬิกา", "Difficult catheterization in BPH", R("Difficult to insert · Tiemann/Coudé catheter", "Campbell-Walsh-Wein Urology 12th ed"), [BPH, AUR, DEVICE]),
     mcq(N(21), "While catheterizing an obese 72-year-old woman, you cannot see the urethral meatus clearly. The catheter enters the vagina and no urine drains. What should you do?",
         ["Withdraw the catheter, wipe it with antiseptic and reinsert it higher", "Inflate the balloon in the vagina to keep the catheter in place as a drain",
          "Leave the catheter in the vagina as a landmark and insert a new sterile catheter just above it, using a finger in the vagina to guide if needed",
          "Abandon the procedure and insert a suprapubic catheter immediately", "Insert the same catheter into the anus to check the anatomy"], 2,
         "สายที่เข้าช่องคลอด **ปนเปื้อนแล้ว** ใช้ต่อไม่ได้ · ทิ้งไว้เป็น **จุดสังเกต** (ปิดช่องคลอดไว้ด้วย) แล้วใส่ **สายปลอดเชื้อเส้นใหม่ด้านบน** · สไลด์: ผู้หญิงหารูไม่เจอ → **สอดนิ้วเข้าช่องคลอด แล้วใส่สายเหนือนิ้ว** — รูเปิดในผู้สูงอายุ/อ้วนมักหลบที่ผนังบนของช่องคลอด\n\n"
         "- **เช็ดแล้วใส่ใหม่** — นำเชื้อช่องคลอดเข้ากระเพาะ\n- **เติมบอลลูนในช่องคลอด** — ไม่ได้ระบายกระเพาะ\n"
         "- **Suprapubic ทันที** — รุกล้ำเกินจำเป็น ยังมีเทคนิคให้ลอง\n- **ใส่ทวารหนัก** — ไม่มีเหตุผล",
         "สายเข้าช่องคลอด → ทิ้งไว้เป็นจุดสังเกต ใช้สายใหม่ใส่ด้านบน", "Difficult female catheterization", R("Difficult to insert (female)"), [ANAT, DEVICE])],
    [BPH, AUR, ANAT, DEVICE, HARM, OLIG], {"trouble": F.trouble()},
    source=SRC + " (Difficult to insert · Campbell-Walsh-Wein flowchart)")

# ═════════════════════════════════════════════ 10
sec("nephro-cath-10", "Troubleshooting 2 — ปัญหาหลังใส่สาย",
    "CRBD 25% · hematuria (ห้าม antifibrinolytic) · รั่วรอบสาย · บอลลูนไม่แฟบ · สายหลุด · paraphimosis · urethral trauma/stricture (BAUS-BAUN 2021)", 10,
"""### ปวดหลังใส่สาย — Catheter-related bladder discomfort (CRBD) (สไลด์: ~25%)
**กลไก**: ปลายสายและบอลลูนระคาย **trigone/คอกระเพาะ** → กระตุ้น muscarinic receptor → detrusor บีบตัวเองเป็นพัก ๆ → ปวดแสบท้องน้อย ปวดอยากปัสสาวะทั้งที่มีสาย ปัสสาวะรั่วรอบสาย · เสี่ยงมากขึ้นเมื่อ **สายใหญ่ บอลลูนเติมเกิน** และผู้ชาย
| ขั้นตอนในสไลด์ | เหตุผล |
|---|---|
| **ตัดสาเหตุร้ายแรงก่อน** — CA-UTI, บาดเจ็บ, นิ่ว, ตะกอน | อาการเดียวกันแต่รักษาต่างกัน |
| **แก้ท้องผูก** | อุจจาระอัดกดกระเพาะ/สาย → spasm และระบายไม่ดี |
| **ถอดสายถ้าไม่จำเป็น** | สาเหตุคือสาย — ถอดแล้วหาย |
| ยา **anticholinergic** (oxybutynin, tolterodine) · **intravesical botulinum toxin** | ยับยั้ง muscarinic/การหลั่ง acetylcholine → detrusor ไม่บีบ |

### เลือดออกหลังใส่สาย (สไลด์ Hematuria after Catheterization!!)
- **ส่วนใหญ่หายเอง** (เยื่อบุถลอก หรือ decompression hematuria — หัวข้อ 11)
- เริ่มด้วย **ล้างกระเพาะผ่าน 3-way catheter** · ถ้าไม่หยุดหรือรุนแรง → **ปรึกษา urology**
- ❗ **ห้ามใช้ยา antifibrinolytic** (เช่น tranexamic acid) — ✍️ "เกิด clot ก้อนใหญ่ → อุดตัน!!" ปกติปัสสาวะมี urokinase ที่ละลายลิ่มเลือด · ยาต้านการละลายลิ่มทำให้ลิ่มแข็งเป็นก้อนใหญ่ → **clot retention** อุดสาย/คอกระเพาะ (และอุดท่อไตได้ถ้าเลือดมาจากไต)

### ปัญหาอื่น (สไลด์ Miscellaneous Problems — BAUS-BAUN 2021)
| ปัญหา | สาเหตุ (กลไก) | ทำอย่างไร |
|---|---|---|
| **ปัสสาวะรั่วรอบสาย (bypassing)** ✍️ วงไว้ | ทางระบายอุด (ตะกอน encrustation รูรับปัสสาวะถูกเยื่อบุดูดปิด) · เยื่อบุบวม · **bladder spasm/detrusor overactivity** | ตรวจสายพับ/อุด · ถุงต่ำกว่ากระเพาะ · anticholinergic/mirabegron/botox · **บอลลูนเติมตามที่กำหนด (no more, no less)** — **อย่าเปลี่ยนเป็นสายหรือบอลลูนที่ใหญ่ขึ้น** (ยิ่งระคาย ยิ่งบีบ ยิ่งรั่ว) |
| **ระบายไม่ดี** | ท่อพับ · ลิ่มเลือด/ตะกอนอุด · สายผิดตำแหน่ง · เยื่อบุถูกดูดปิดรู | ให้ไหลสะดวก · ล้าง · **ยกถุงสูงกว่ากระเพาะชั่วครู่ (หนีบสายก่อน) ช่วยปลดแรงดูด** · ดื่มน้ำ แก้ท้องผูก |
| **สายหลุด (expulsion)** | เติมบอลลูนไม่ถูก · บอลลูนแฟบ · คอกระเพาะหลวม (หญิง/โรคประสาท) | ตรวจปริมาตรน้ำในบอลลูน · **สายหรือบอลลูนใหญ่ขึ้นไม่แนะนำ** · หลุดบ่อย → พิจารณา SPC |
| **บอลลูนไม่แฟบ** | วาล์วเสีย · ทางเติมอุด (เช่น ผลึกจาก NSS) | ต่อ syringe แล้ว **รอให้ไหลออกเอง** (ไม่ดูดแรง — ทางเติมแฟบปิด) · ลองฉีด sterile water/อากาศ **2 mL** เข้าไปดันสิ่งอุด · ใช้เข็มดูดจากแขนเติมบอลลูน · ให้ผู้ป่วยเดิน · สุดท้าย urology เจาะบอลลูนนำด้วย ultrasound |
| **UTI ระหว่างใส่ / ผ่านระบบระบาย** | เทคนิคไม่ปลอดเชื้อ · ถอดข้อต่อ · ล้างมือไม่พอ | เทคนิค/ถุง/ล้างมือ (หัวข้อ 8) |
| **CAUTI ซ้ำ** | เชื้อเกาะสายหลัง 4 สัปดาห์แทบทุกราย · นิ่ว/ตะกอน | **ไม่ dipstick ปัสสาวะจากสาย** · ยาป้องกันมักไม่ได้ผล · US/cystoscopy หานิ่ว ล้างตะกอน |
| **Urethral mucosa trauma / false passage** | ขนาดหรือตำแหน่งผิด เทคนิคไม่ดี | ใส่ใหม่ด้วยขนาดที่ถูก · ไม่ระบาย → ถอดสาย อาจต้อง cystoscopy · ระยะยาว → **stricture** |
| **Urethral erosion (catheter hypospadias)** | แรงกดเรื้อรัง | ยึดสายถูกทิศ ดูแลความสะอาด · พิจารณา **SPC** |
| **Paraphimosis** | **ไม่รูดหนังหุ้มกลับ** | รูดหนังหุ้มกลับทุกครั้ง + ทำความสะอาดประจำวัน |
| เปลี่ยนสายยาก | ปวด encrustation stricture false passage | SPC · Tiemann สำหรับ prostate โต · เปลี่ยนผ่าน guidewire |

### Paraphimosis — ทำไมถึงเป็นภาวะฉุกเฉิน
[[fig:paraphimosis]]
""",
    ["CRBD (~25%): ตัดสาเหตุร้าย → แก้ท้องผูก → ถอดสาย → anticholinergic/botox",
     "Hematuria หลังใส่: ส่วนใหญ่หายเอง · ล้างผ่าน 3-way · ห้าม tranexamic acid (clot retention)",
     "รั่วรอบสาย/สายหลุด: อย่าเปลี่ยนเป็นสายหรือบอลลูนที่ใหญ่ขึ้น",
     "บอลลูนไม่แฟบ: ต่อ syringe รอให้ไหลออกเอง → เติม 2 mL ดันสิ่งอุด → เข็มดูดจากแขน → urology",
     "Paraphimosis = ลืมรูดหนังหุ้มกลับ → วงรัด → บวม → ขาดเลือด"],
    [mcq(N(22), "A 66-year-old man has persistent blood-stained urine with small clots 6 hours after a traumatic catheterization. He is haemodynamically stable and the catheter is draining. Which management should be avoided?",
         ["Exchange to a 3-way catheter and start bladder irrigation", "Ensure free drainage and encourage oral fluids",
          "Give systemic tranexamic acid to stop the bleeding", "Monitor haemoglobin and clot passage", "Consult urology if bleeding persists or is severe"], 2,
         "สไลด์: hematuria หลังใส่สายมักหายเอง → ล้างกระเพาะผ่าน **3-way** · ปรึกษา urology ถ้าไม่หยุด · ❗ **NOT USE ANTIFIBRINOLYTIC THERAPY** — ✍️ \"เกิด clot ก้อนใหญ่ → อุดตัน!!\" ปัสสาวะปกติมี urokinase ละลายลิ่มเลือดอยู่ · tranexamic acid ยับยั้งการละลาย → ลิ่มเลือดแข็งเป็นก้อนใหญ่ในกระเพาะ → **clot retention** อุดสายและคอกระเพาะ\n\n"
         "- **3-way irrigation · ระบายสะดวก/ดื่มน้ำ · ติดตาม Hb · ปรึกษาเมื่อไม่หยุด** — ทั้งหมดเป็นการดูแลที่ถูกต้อง",
         "เลือดออกจากทางเดินปัสสาวะล่าง: ห้าม antifibrinolytic", "Haematuria after catheterization", R("Hematuria after catheterization"), [HEMAT, HARM]),
     mcq(N(23), "An 80-year-old uncircumcised man with delirium had a urinary catheter inserted in the emergency department. The next morning the glans is swollen, purple and tender, with a tight band of oedematous foreskin proximal to it. What caused this and what is the immediate management?",
         ["Latex allergy; remove the catheter and give antihistamines",
          "Retracted foreskin left behind the glans formed a constricting ring that obstructed venous and lymphatic return; reduce it manually after analgesia and compression, with urology help if this fails",
          "Fournier's gangrene; start broad-spectrum antibiotics and plan surgical debridement",
          "Balloon inflated in the penile urethra; deflate the balloon",
          "Contact dermatitis from povidone-iodine; apply topical steroid"], 1,
         "ภาพคือ **paraphimosis** — ผู้ใส่ลืม **รูดหนังหุ้มกลับ** หลังใส่สาย หนังหุ้มที่ร่นค้างเป็น **วงรัดหลัง glans** → เลือดดำและน้ำเหลืองไหลกลับไม่ได้ → glans บวม → วงยิ่งรัด → สุดท้ายเลือดแดงเข้าไม่ได้ → **เนื้อตาย** (BAUS-BAUN ในสไลด์: failure to replace foreskin) · รักษาทันที: ยาชา/บีบไล่บวม (ประคบเย็น พันบีบ) แล้วดันกลับ · ไม่สำเร็จ → urology (dorsal slit) · ป้องกัน: รูดกลับทุกครั้ง\n\n"
         "- **แพ้ latex / ผื่นจาก povidone-iodine** — ไม่ทำให้เกิดวงรัดที่ชัดเจนแบบนี้\n- **Fournier's gangrene** — เนื้อตายเน่าที่ฝีเย็บ/ถุงอัณฑะ ไข้ ผิวดำ crepitus\n"
         "- **บอลลูนพองใน penile urethra** — จะปวดตอนเติมทันที ไม่ใช่วงรัดที่หนังหุ้ม",
         "ใส่สายในชายไม่ขลิบ → รูดหนังหุ้มกลับเสมอ", "Paraphimosis after catheterization", R("Miscellaneous problems (1)", "BAUS-BAUN 2021"), [PARA, HARM])],
    [HEMAT, HARM, PARA, OAB_D, CONST, DEVICE, BIOFILM], {"paraphimosis": F.paraphimosis()},
    source=SRC + " (Painful · Hematuria · Miscellaneous problems — BAUS-BAUN 2021)")

# ═════════════════════════════════════════════ 11
sec("nephro-cath-11", "หลังระบายกระเพาะที่คั่งมาก — post-obstructive diuresis และเลือดออก",
    "นิยาม · กลไก physiologic vs pathologic · ใครเสี่ยง · การดูแลน้ำและเกลือแร่ · decompression hematuria · ไม่ต้อง clamp", 8,
"""(หัวข้อนี้ไม่อยู่ในสไลด์ — สไลด์ระบุ "bladder decompression" เป็นข้อบ่งชี้ และ hematuria หลังใส่สาย · กลไกและการดูแลอิงตำรา urology/nephrology)

### Post-obstructive diuresis (POD)
**นิยามที่ใช้บ่อย**: ปัสสาวะ **> 200 mL/ชม. ติดต่อกัน 2 ชม.** หรือ **> 3 L ใน 24 ชม.** หลังปลดการอุดกั้น
[[fig:pod]]
#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก | ความหมาย |
|---|---|---|
| **ปัสสาวะมากหลังใส่สาย** (ช่วงแรก) | ขับ urea เกลือ และน้ำที่คั่งระหว่างอุด → **osmotic/solute diuresis** | **physiologic** — เหมาะสม หยุดเองเมื่อของที่คั่งหมด (มัก 24–48 ชม.) |
| **ปัสสาวะยังมากแม้ร่างกายเริ่มขาดน้ำ** | ท่อไตเสียจากแรงดัน: medulla ถูกชะล้าง · **aquaporin-2 ↓** (ไตตอบ ADH ไม่ได้ = nephrogenic DI ชั่วคราว) · ตัวขนส่ง Na ↓ | **pathologic** — อันตราย |
| **ความดันต่ำ ชีพจรเร็ว** | เสียน้ำเกินที่รับเข้า | hypovolemia |
| **Na ต่ำหรือสูง · K ต่ำ · Mg ต่ำ** | เสีย Na และ K ในปัสสาวะ · ถ้าชดเชยด้วยน้ำเปล่า/สารน้ำผิดชนิด → Na เพี้ยน | ตรวจ electrolytes บ่อย |

**ใครเสี่ยง**: chronic retention (คั่งนาน ปริมาณมาก) · **Cr สูง/AKI** · บวมหรือน้ำเกิน หัวใจวาย · สับสน (ดื่มน้ำเองไม่ได้) · bicarbonate สูง/ BUN สูง

### การดูแล
| ทำ | เหตุผล |
|---|---|
| วัดปัสสาวะ **ทุกชั่วโมง** · สัญญาณชีพ · น้ำหนัก | จับ pathologic POD ได้เร็ว |
| electrolytes (Na K Mg) และ Cr **ทุก 6–12 ชม.** ในรายเสี่ยง | เกลือแร่เปลี่ยนเร็ว |
| ผู้ป่วยรู้ตัวดี สัญญาณชีพคงที่ → **ให้ดื่มตามกระหาย** | ร่างกายควบคุมเองได้ |
| มีอาการขาดน้ำ → IV ทดแทน **บางส่วน (~½–¾ ของปัสสาวะชั่วโมงก่อน)** มักใช้ 0.45% NaCl ปรับตาม Na | ทดแทน **มิลลิลิตรต่อมิลลิลิตร** จะไล่ตามจน physiologic diuresis ไม่หยุด |

### เลือดออกและความดันต่ำหลังระบาย — ต้อง clamp ไหม
- **Decompression hematuria**: กระเพาะที่ยืดมาก หลอดเลือดในผนังถูกยืดและกด → เมื่อแฟบลงทันที ความดันรอบหลอดเลือดลด หลอดเลือดเปราะแตก → ปัสสาวะมีเลือด — **พบบ่อยแต่ส่วนใหญ่น้อยและหายเอง**
- **ความดันต่ำชั่วคราว**: vasovagal + การกดหลอดเลือดดำในเชิงกรานหายไป
- ความเชื่อเดิมให้ **ระบายทีละ 500 mL แล้ว clamp** — การทบทวนวรรณกรรม (Nyman et al., Mayo Clin Proc 2010) **ไม่พบว่าการระบายช้า ๆ ลดภาวะแทรกซ้อน** → ระบายให้หมดได้ แล้วเฝ้าระวัง (CDC 2009 ก็ระบุว่าไม่ต้อง clamp ก่อนถอด)
""",
    ["POD: > 200 mL/ชม. 2 ชม.ติด หรือ > 3 L/24 ชม.",
     "Physiologic (ขับของที่คั่ง หยุดเอง) vs pathologic (AQP2 ↓ medulla ถูกชะล้าง ท่อไตเก็บ Na ไม่ได้)",
     "เสี่ยง: chronic retention + Cr สูง + น้ำเกิน/สับสน",
     "ทดแทน ~½–¾ ของปัสสาวะเมื่อขาดน้ำ — ไม่ใช่มิลลิลิตรต่อมิลลิลิตร",
     "ระบายหมดได้ ไม่ต้อง clamp · decompression hematuria มักหายเอง"],
    [mcq(N(24), "A 72-year-old man with chronic urinary retention from BPH has 2.4 L drained after catheterization. Creatinine is 3.4 mg/dL (baseline 1.1). Over the next 4 hours his urine output is 450–500 mL/h; BP falls from 150/90 to 104/62 mmHg and serum sodium rises from 138 to 147 mmol/L. Which statement best explains and manages this?",
         ["Physiologic diuresis only; restrict fluids because the kidneys are excreting excess volume",
          "Pathologic post-obstructive diuresis from impaired tubular concentrating ability (reduced aquaporin-2, medullary washout); replace part of the hourly output (about one-half to three-quarters) with hypotonic saline and monitor electrolytes closely",
          "Central diabetes insipidus; give desmopressin",
          "Bladder rupture; obtain a cystogram",
          "Diuresis caused by the lidocaine gel; observe only"], 1,
         "หลังปลดการอุดเรื้อรัง (Cr สูง) ปัสสาวะ 450–500 mL/ชม. = **post-obstructive diuresis** · ความดันลดและ Na สูงขึ้น = เสียน้ำมากกว่าเกลือ ร่างกายเริ่มขาดน้ำแต่ยังปัสสาวะต่อ → **pathologic** จากท่อไตเสีย: medulla ถูกชะล้าง **aquaporin-2 ลดลง** (ตอบ ADH ไม่ได้ ~ nephrogenic DI) และเก็บ Na ไม่ได้ · ดูแล: ทดแทนด้วยสารน้ำ hypotonic (เช่น 0.45% NaCl) **บางส่วน ~½–¾ ของปัสสาวะ** วัดทุกชั่วโมง ตรวจ Na K Mg บ่อย\n\n"
         "- **จำกัดน้ำ** — ผู้ป่วยกำลังขาดน้ำ (BP ↓ Na ↑) จะยิ่ง shock\n- **Central DI / desmopressin** — ปัญหาอยู่ที่ไตตอบ ADH ไม่ได้ desmopressin ไม่ช่วย\n"
         "- **กระเพาะแตก** — จะไม่มีปัสสาวะออกมาก\n- **lidocaine gel** — ไม่ทำให้ปัสสาวะมาก",
         "POD pathologic: ทดแทนบางส่วน + เฝ้า electrolytes", "Post-obstructive diuresis", ["ตำรา urology/nephrology (ไม่อยู่ในสไลด์)"], [POLY, LYTE, LYTE_B, OBST, AKI, OLIG_B])],
    [POLY, LYTE, LYTE_B, OBST, AKI, AKI_B, OLIG_B, HEMAT, RET], {"pod": F.pod()},
    source="ตำรา urology/nephrology · Nyman et al. Mayo Clin Proc 2010 (ไม่อยู่ในสไลด์)")

# ── END SECTIONS


# ═════════════════════════════════════════════ ประกอบคาบ
LECNAME = "Urethral catheterization (อ.ธนิศร)"
MEQ = [{"id": "NEPH-CATH-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Acute urinary retention in BPH — catheter choice, difficult insertion, post-obstructive diuresis and CAUTI",
 "vignette": """ผู้ป่วยชายไทยอายุ 78 ปี มาห้องฉุกเฉินด้วยปัสสาวะไม่ออก 14 ชั่วโมง
PI: 3 วันก่อนเป็นหวัด ซื้อยาแก้หวัดที่มี pseudoephedrine + chlorpheniramine มากิน · 1 ปีที่ผ่านมาปัสสาวะลำบาก ต้องเบ่ง ลำปัสสาวะอ่อน ตื่นมาปัสสาวะกลางคืน 3–4 ครั้ง · วันนี้ปวดท้องน้อยมาก กระสับกระส่าย มีปัสสาวะเล็ดเป็นหยดตลอด
PH: ความดันโลหิตสูง · ไม่เคยผ่าตัดทางเดินปัสสาวะ · ไม่มีประวัติอุบัติเหตุ
PE: BT 37.2 °C, BP 178/98 mmHg, PR 112/min · ก้อนเคาะทึบเหนือหัวหน่าวถึงกึ่งกลางสะดือ กดเจ็บ · ไม่มีเลือดที่ meatus · DRE: prostate โต เรียบ ยืดหยุ่น ไม่กดเจ็บ
Lab: Cr 2.9 mg/dL (6 เดือนก่อน 1.2) · Na 137 · K 5.1 mmol/L · bladder scan > 999 mL""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัย บอกปัจจัยกระตุ้น และอธิบายกลไกของ (ก) ความดัน/ชีพจรสูงและกระสับกระส่าย (ข) ปัสสาวะเล็ดเป็นหยด (ค) Cr สูง (4 คะแนน)",
   "a": """**การวินิจฉัย**: acute (on chronic) urinary retention จาก **BPH** + **post-renal AKI** · **ตัวกระตุ้น** = ยาแก้หวัด: pseudoephedrine (**α1-agonist** → กล้ามเนื้อเรียบที่คอกระเพาะ/prostate หดตัว) + chlorpheniramine (**anticholinergic** → detrusor บีบอ่อน)
(ก) กระเพาะยืด → ปวด (S2–4) → **sympathetic** → BP/HR สูง กระสับกระส่าย — ระบายแล้วลงเอง ไม่ต้องรีบให้ยาลดความดัน
(ข) **overflow incontinence** — ความดันในกระเพาะที่ยืดเต็มที่ชนะแรงต้านทางออก ล้นออกทีละน้อย ไม่ได้แปลว่าปัสสาวะได้
(ค) ความดันย้อนขึ้นท่อไตทั้งสองข้าง → ความดันใน Bowman's space สูง → GFR ↓ = **post-renal AKI**"""},
  {"q": "2. ก่อนใส่สาย ต้องตรวจ/ถามอะไรเพื่อดูข้อห้าม และจะเลือกสายชนิด ขนาด วัสดุอะไร พร้อมเหตุผล (3 คะแนน)",
   "a": """**ข้อห้าม/ข้อควรระวัง**: เลือดที่ meatus · อุบัติเหตุ/pelvic fracture · prostate ยกสูงหรือกดเจ็บมาก (prostatitis) · ประวัติ stricture/ผ่าตัด/ส่องกล้อง · **แพ้ latex/lidocaine** — ผู้ป่วยรายนี้ไม่มีข้อห้าม
**สาย**: Foley **2-way** (ต้องค้างไว้ระบายและวัดปัสสาวะเพราะมี AKI และเสี่ยง POD) · ขนาด **14–16 Fr** (ปัสสาวะใส; สไลด์: BPH อาจใช้ใหญ่ขึ้นเพราะแข็งไม่ขด) · วัสดุ: latex ได้ถ้าใช้ < 14 วันและไม่แพ้ ถ้าคาดว่าค้างนานหรือแพ้ → **silicone**
**ระบบปิด**: ต่อถุงไว้ก่อน · lidocaine gel · sterile water สำหรับบอลลูน"""},
  {"q": "3. สาย 14 Fr ผ่านไปราว 17 ซม. แล้วติด ลองซ้ำพร้อมฉีด gel เพิ่มและจับองคชาต 90° ยังไม่ผ่าน จะทำอย่างไรต่อ และสิ่งใดที่ห้ามทำ (3 คะแนน)",
   "a": """**ทำต่อ**: ระดับ prostate ใน BPH → **16–18 Fr coudé/Tiemann ปลายชี้ 12 นาฬิกา** (Campbell: prostatic obstruction suspected → 18 Fr coudé) · ไม่สำเร็จ → **ปรึกษา urology** (cystoscopy/guidewire/Council-tip) · กระเพาะโป่งต้องระบายด่วนแต่ใส่ไม่ได้ → **suprapubic catheter**
**ห้าม**: ดันแรง (false passage) · **เติมบอลลูนตรงที่ติด** (บอลลูนพองใน prostatic urethra) · ลดเป็นสายเล็กนิ่ม (ขดใน prostate — สายเล็กใช้กับ stricture) · ลองซ้ำหลายครั้งโดยไม่เปลี่ยนวิธี"""},
  {"q": "4. ใส่ coudé 18 Fr สำเร็จ ระบายได้ 1,600 mL · 4 ชั่วโมงต่อมา ปัสสาวะ 400–450 mL/ชม. BP 108/64 mmHg ชีพจร 104/min Na 146 K 3.2 mmol/L — เกิดอะไรขึ้น อธิบายกลไกและการดูแล (4 คะแนน)",
   "a": """**Post-obstructive diuresis** (> 200 mL/ชม. 2 ชม.ติด) ชนิด **pathologic** — BP ลด ชีพจรเร็ว Na สูง K ต่ำ = เสียน้ำและ K เกิน
**กลไก**: ระหว่างอุด urea/เกลือ/น้ำคั่ง (ส่วน physiologic) + ท่อไตเสียจากแรงดัน: medulla ถูกชะล้าง **aquaporin-2 ↓** (ตอบ ADH ไม่ได้) ตัวขนส่ง Na ↓ → ปัสสาวะออกต่อแม้ร่างกายขาดน้ำ
**ดูแล**: วัดปัสสาวะทุกชั่วโมง สัญญาณชีพ · Na K Mg Cr ทุก 6–12 ชม. · ทดแทน IV **บางส่วน (~½–¾ ของปัสสาวะชั่วโมงก่อน)** ด้วยสารน้ำ hypotonic เช่น 0.45% NaCl + KCl · ให้ดื่มเองถ้ารู้ตัวดี · ไม่ทดแทนมิลลิลิตรต่อมิลลิลิตร (ไล่ตามจนไม่หยุด) · ปัสสาวะมีเลือดเล็กน้อยหลังระบาย = decompression hematuria มักหายเอง (ไม่จำเป็นต้อง clamp)"""},
  {"q": "5. วันที่ 9 ของการค้างสาย ผู้ป่วยมีไข้ 38.7 °C หนาวสั่น สับสน ปัสสาวะในถุงขุ่น ไม่พบแหล่งติดเชื้ออื่น — จงให้การวินิจฉัย บอกการเก็บสิ่งส่งตรวจ การรักษา และแผนป้องกัน/ถอดสาย (4 คะแนน)",
   "a": """**CAUTI** (IDSA 2009: อาการเข้าได้ ไม่มีแหล่งอื่น + เพาะเชื้อ ≥ 10³ CFU/mL) — ไข้/สับสนเป็นอาการเด่นเพราะสายระบายตลอดจึงไม่มีแสบขัด
**สิ่งส่งตรวจ**: urine culture จาก **sampling port** ด้วยเทคนิคปลอดเชื้อ (ไม่ใช่จากถุง) **ก่อนให้ยา** + hemoculture · สายค้างยังไม่ถึง 2 สัปดาห์ (9 วัน) — ถ้าสายอุด/มีตะกอนก็เปลี่ยนและเก็บจากสายใหม่ (สายเก่ามี **biofilm**)
**รักษา**: ยาปฏิชีวนะครอบคลุม gram-negative ตามข้อมูลเชื้อดื้อยาของโรงพยาบาล แล้วปรับตามผลเพาะเชื้อ · **7 วัน** ถ้าตอบสนองเร็ว **10–14 วัน** ถ้าช้า
**ป้องกัน/ถอด**: ทบทวนความจำเป็นทุกวัน · alpha-blocker (tamsulosin) แล้วทำ **TWOC** · ไม่ผ่าน → IC หรือส่งผ่าตัด prostate แทนการค้างสายยาว · ระบบปิด ถุงต่ำกว่ากระเพาะ ไม่แตะพื้น · ไม่เปลี่ยนสายตามรอบ ไม่ให้ยาป้องกัน ไม่คัดกรอง ASB"""}],
 "ref": ["สไลด์ อ.ธนิศร — Indication · Size · Difficult to insert · Tiemann · Campbell flowchart · Miscellaneous problems",
         "CDC/HICPAC CAUTI 2009 · IDSA CA-UTI 2009 · EAU Non-neurogenic male LUTS"],
 "nl": [AUR, AUR_B, BPH, BPH_D, AKI, POLY, LYTE, CYST, PYELO, DEVICE],
 "years": [], "_kind": "meq", "_set": "nephro"}]

OSCE = [{"id": "NEPH-CATH-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Procedure station – Male urethral catheterization on a manikin",
 "station": "หัตถการบนหุ่น 8 นาที (ผู้ป่วยสมมุติพูดแทนหุ่น)",
 "instruction": """**สถานการณ์**: ชายอายุ 70 ปี มี acute urinary retention จาก BPH (bladder scan 900 mL) ไม่มีประวัติอุบัติเหตุ ไม่มีเลือดที่ meatus แพทย์ให้ใส่สายสวนปัสสาวะค้างไว้

**งานของนักศึกษา**: (1) ขอความยินยอมจากผู้ป่วย (2) ใส่สายสวนปัสสาวะชนิดค้างไว้ในหุ่นผู้ชายด้วยเทคนิคปลอดเชื้อ (3) ยึดสายและจัดถุงให้ถูกต้อง (4) บอกผู้คุมสอบว่าจะบันทึกอะไรลงในเวชระเบียน

อุปกรณ์บนโต๊ะ: ชุดสวนปลอดเชื้อ · Foley 2-way latex และ silicone ขนาด 12 14 16 Fr · coudé 18 Fr · 2% lidocaine gel · syringe 10 mL · sterile water และ NSS · ถุงปัสสาวะระบบปิด · ถุงมือปลอดเชื้อ · พลาสเตอร์/อุปกรณ์ยึดสาย""",
 "answer": """**เกณฑ์ให้คะแนน (20 คะแนน)**

| หมวด | สิ่งที่ต้องทำ | คะแนน |
|---|---|---|
| เตรียม | ยืนยันตัวผู้ป่วย ข้อบ่งชี้ และถามข้อห้าม (อุบัติเหตุ เลือดที่ meatus ผ่าตัด/stricture) | 1 |
| เตรียม | อธิบายเหตุผล ขั้นตอน ความรู้สึกที่จะเกิด ความเสี่ยง (เจ็บ เลือดออก ติดเชื้อ) และขอความยินยอม · ถามแพ้ latex/lidocaine | 2 |
| เตรียม | ความเป็นส่วนตัว/chaperone · ล้างมือ · จัดท่านอนหงาย | 1 |
| เตรียม | เลือก **14–16 Fr 2-way** ที่ไม่แพ้ · **ต่อถุงระบบปิดไว้ก่อน** · เตรียม **sterile water** (ไม่ใช่ NSS) | 2 |
| ปลอดเชื้อ | ใส่ถุงมือปลอดเชื้อโดยไม่ปนเปื้อน · ปูผ้า · แยกมือสะอาด/มือปลอดเชื้อ | 2 |
| ปลอดเชื้อ | รูดหนังหุ้มลง ทำความสะอาด meatus จากรูออกด้านนอก | 1 |
| ใส่สาย | ฉีด lidocaine gel เข้าท่อช้า ๆ บีบปลายไว้ **รอ 3–5 นาที** (บอกเหตุผล) | 2 |
| ใส่สาย | จับองคชาต **ตั้งฉาก 90°** ดันด้วยแรงสม่ำเสมอ บอกผู้ป่วยหายใจลึก/เบ่งเมื่อผ่านหูรูด · ไม่ดันแรง | 2 |
| ใส่สาย | ดัน **ถึง bifurcation** → เห็นปัสสาวะ → เติม sterile water ตามปริมาตรบนสาย สังเกตอาการปวด → ดึงกลับเบา ๆ จนติด | 2 |
| จบ | **รูดหนังหุ้มกลับ** | 1 |
| จบ | ยึดสายที่ **หน้าท้อง** · ถุง **ต่ำกว่ากระเพาะ ไม่แตะพื้น** · สายไม่พับ | 2 |
| จบ | ทิ้งของ ล้างมือ · บอกการบันทึก: วันเวลา ข้อบ่งชี้ ขนาด/ชนิด ปริมาตรบอลลูน **ปริมาณปัสสาวะที่ระบาย** ลักษณะปัสสาวะ แผนถอดสาย/เฝ้าระวัง post-obstructive diuresis | 2 |

**Critical errors (ไม่ผ่านสถานีทันที)**: ปลอดเชื้อหลุดแล้วไม่เปลี่ยนอุปกรณ์ · **เติมบอลลูนก่อนดันถึง bifurcation/ก่อนเห็นปัสสาวะ** · ดันฝืนเมื่อมีแรงต้านมาก · **ลืมรูดหนังหุ้มกลับ** · เติมบอลลูนด้วย NSS

**คำถามต่อจากผู้คุมสอบ (ถ้ามีเวลา)**: "ถ้าใส่ 14 Fr ไม่ผ่านที่ระดับ prostate จะทำอย่างไร" → 16–18 Fr coudé ปลายชี้ 12 นาฬิกา ไม่ผ่าน → urology/suprapubic · "ถ้ามีเลือดที่ meatus" → ไม่ใส่ ทำ retrograde urethrogram""",
 "ref": ["สไลด์ อ.ธนิศร — Size · Material · Fixation · Catheter care · Difficult to insert", "CDC/HICPAC CAUTI 2009 · EAUN 2024"],
 "nl": [AUR, BPH, DEVICE, ANAT, PARA],
 "years": [], "_kind": "meq", "_set": "nephro"}]

LECTURE = {
 "lec": LEC, "date": "พฤ. 22 ต.ค.",
 "title": "Urethral catheterization",
 "subtitle": "ชนิดของการสวน · ข้อบ่งชี้/ไม่บ่งชี้ (EAUN 2024 · CDC 2009) · acute urinary retention · กายวิภาคชาย vs หญิง · ข้อห้าม (urethral injury) · ขนาด/วัสดุ/coudé · ขั้นตอนพร้อมเหตุผล · CAUTI และ bundle ป้องกัน · ใส่ไม่เข้า · CRBD hematuria paraphimosis บอลลูนไม่แฟบ · post-obstructive diuresis",
 "objectives": [
   "เลือกวิธีระบายปัสสาวะที่รุกล้ำน้อยที่สุด (external · intermittent · indwelling · suprapubic) และบอกข้อบ่งชี้ที่เหมาะสม/ไม่เหมาะสมของสายค้าง",
   "อธิบายกลไกของอาการใน acute urinary retention และสาเหตุจากยา",
   "อธิบายกายวิภาคท่อปัสสาวะชายและหญิงที่ทำให้เทคนิคการใส่ต่างกัน และจุดที่สายมักติด",
   "ตรวจหาสัญญาณของ urethral injury ก่อนใส่สาย และเลือกทางเลือก (retrograde urethrogram, suprapubic)",
   "เลือกขนาด วัสดุ และชนิดของสายตามลักษณะปัสสาวะและปัญหาของผู้ป่วย",
   "ใส่สายค้างในผู้ชายและผู้หญิงด้วยเทคนิคปลอดเชื้อ พร้อมบอกเหตุผลของทุกขั้นตอน",
   "อธิบายกลไกการเกิด CAUTI และ biofilm วินิจฉัย/รักษาตาม IDSA 2009 และใช้ bundle ป้องกันตาม CDC 2009",
   "แก้ปัญหาใส่ไม่เข้า ไม่มีปัสสาวะ ปวด เลือดออก รั่ว บอลลูนไม่แฟบ และป้องกัน paraphimosis",
   "อธิบายและดูแล post-obstructive diuresis หลังระบายกระเพาะที่คั่งมาก"],
 "nlGap": "เกณฑ์ฯ มีรหัสปัสสาวะคั่ง (`2.1.45` `2.2.29` `B9.2.3(1)`) BPH (`2.3.14(8)`) phimosis/paraphimosis (`2.3.14-3(11)`) cystitis/pyelonephritis (`2.3.14(7)` `2.3.14(14)`) biofilm (`B1.5.2(3)`) และอันตรายจากอุปกรณ์การแพทย์ (`2.3.19(5)`) แต่ **ไม่มีรหัสของหัตถการใส่สายสวนปัสสาวะ ไม่มี CAUTI และไม่มี post-obstructive diuresis โดยตรง** · handout ไม่มีหน้าขั้นตอนการใส่ทีละขั้น กายวิภาค urethral injury CAUTI และ post-obstructive diuresis — เนื้อหาส่วนนั้นอิงแนวทางด้านล่างและบอกไว้ในแต่ละหัวข้อ · สไลด์ไม่มีเฉลย 4 เคส (คำตอบในหัวข้อ 2 เป็นของผู้เขียนบทเรียน)",
 "guidelines": [
   "**2024 EAUN Guidelines for Urethral Intermittent Catheterisation in Adults** และ **2024 EAUN Guidelines for Indwelling Catheterisation in Adults** — ข้อบ่งชี้ ข้อห้าม ขนาด วัสดุ การยึด การดูแล (อาจารย์อ้างในสไลด์)",
   "**2021 BAUS-BAUN Consensus on Management of the Complications of Long-term Indwelling Catheters** — ตาราง miscellaneous problems (อาจารย์อ้างในสไลด์)",
   "**Campbell-Walsh-Wein Urology 12th ed (2021)** — flowchart ใส่สายไม่ผ่าน (อาจารย์อ้างในสไลด์)",
   "**CDC/HICPAC Guideline for Prevention of Catheter-Associated Urinary Tract Infections 2009** — ข้อบ่งชี้ที่เหมาะสม/ไม่เหมาะสม และ bundle ป้องกัน",
   "**IDSA International Clinical Practice Guidelines for Catheter-Associated UTI in Adults 2009** — นิยาม CAUTI การเก็บสิ่งส่งตรวจ การเปลี่ยนสาย ระยะเวลารักษา",
   "**EAU Guidelines on Urological Trauma** และ **ATLS 10th ed** — urethral injury",
   "**EAU Guidelines on Management of Non-neurogenic Male LUTS** — alpha-blocker ก่อน trial without catheter",
   "**Nyman MA et al. Mayo Clin Proc 2010** — การระบายเร็ว vs ช้าในภาวะปัสสาวะคั่ง"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# กระจายตำแหน่งคำตอบของข้อใหม่ (ทำก่อน publish ครั้งแรกเท่านั้น)
ORDERED = set()
_slot = 0
for s in S:
    for it in s["items"]:
        if it["id"] in ORDERED or not it["id"].startswith("NEPH-CATH-MCQ"):
            continue
        tgt = [0, 2, 4, 1, 3][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", "nephro.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LEC]
data.append(LECTURE)

seen = set()
for l in data:
    for x in [i for s in l["sections"] for i in s["items"]] + l["meq"] + l["osce"] + [{"id": s["id"]} for s in l["sections"]]:
        assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
        seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
L = LECTURE
codes = {c for s in L["sections"] for c in s["nl"]} | {c for s in L["sections"] for i in s["items"] for c in i["nl"]} | {c for m in L["meq"] + L["osce"] for c in m.get("nl", [])}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
for s in L["sections"]:
    assert "```" not in s["md"], s["id"]
    for k in (s.get("figs") or {}):
        assert "[[fig:%s]]" % k in s["md"], (s["id"], k)

data.sort(key=lambda l: (0, int(l["lec"])) if l["lec"].isdigit() else (1, l["lec"]))
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "nephro": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
newi = [i for s in L["sections"] for i in s["items"] if i["id"].startswith("NEPH-CATH")]
print("sections %d | ข้อใหม่ %d | meq %d | osce %d | figs %d | nl %d" % (
    len(S), len(newi), len(L["meq"]), len(L["osce"]), sum(len(s.get("figs") or {}) for s in S), len(codes)))
print("answer positions (ข้อใหม่):", dict(sorted(Counter(i["answer"] for i in newi).items())))
print("nephro.json มี %d คาบ: %s" % (len(data), [l["lec"] for l in data]))
