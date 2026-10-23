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

# ── END SECTIONS
