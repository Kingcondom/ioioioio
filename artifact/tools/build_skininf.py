#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Skin infection (อ.วรนิษฐ์ อ่อนประเสริฐ · Woranit Onprasert) → data/derm.json คาบ 26/10
ต้นฉบับ: Drive 1PTgRH88P1bd3OYWPtBtgMtJ9KEIdXy0G "Skin infection 2025 (Hand out).pdf" · บรรยาย จ. 26 ต.ค. 2569
โน้ตสไลด์: slides/skin_infection_notes.md · ภาพประกอบ: figs_skininf.py
ขอบเขต: สไลด์หมวด "bacterial" และ "viral" ถอดได้ครบจาก Drive read_file_content
หมวด fungal/parasitic ของสไลด์ "อ่านไม่ได้" (API ตัดข้อความ + ไฟล์ 20.8 MB render ไม่ได้) → ไม่ทำในคาบนี้ ระบุใน nlGap
ไม่มีข้อสอบในคลัง Ward Drill สำหรับคาบนี้ — ข้อสอบเขียนใหม่ทั้งหมด"""
import json, os, sys

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(BUILD, "tools")
sys.path.insert(0, TOOLS)
import figs_skininf as F

SRC = "สไลด์ อ.วรนิษฐ์ — Skin infection 2025 (Hand out)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl, figs=None, source=SRC):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": source,
              "nl": nl, "md": md, "pearls": pearls, "items": items, "figs": figs or {}})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl):
    assert len(choices) == 5 and 0 <= answer <= 4, iid
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}
N = lambda n: "DE-SI-MCQ-%02d" % n
R = lambda p: ["สไลด์ อ.วรนิษฐ์ — " + p]
NL_SKIN = ["2.1.50", "2.3.12"]

# ───────────────────────────── 1
sec("derm-si-01", "เข้าหาคนไข้ติดเชื้อผิวหนัง — ถามสามคำถามก่อนตั้งชื่อโรค",
    "แบ่งตามเชื้อ · ตามความลึก · outside-in vs inside-out", 8,
"""สไลด์เปิดด้วยเหตุผลว่าทำไมหัวข้อนี้สำคัญ — **พบบ่อยทั้งที่ OPD, ER และผู้ป่วยใน** · **เชื้อก่อโรคหลากหลาย** ทั้งแบคทีเรีย ไวรัส เชื้อรา ปรสิต · **ถ้าช้าจะกลายเป็น cellulitis, sepsis หรือเนื้อตาย** · และ **หน้าตาเหมือนโรคผิวหนังที่ไม่ใช่การติดเชื้อ** จนวินิจฉัยผิดกันบ่อย

### สามแกนที่ใช้แบ่งโรค (classification ตามสไลด์)

| แกน | ตัวเลือก | ใช้ทำอะไร |
|---|---|---|
| **Type of organism** | **bacterial** (impetigo, cellulitis) · **viral** (herpes simplex, warts) · **fungal** (ringworm, candidiasis) · **parasitic** (scabies, lice) | เลือกกลุ่มยา |
| **Level of infection** | **superficial** — epidermis เช่น impetigo · **deep** — dermis/subcutaneous เช่น cellulitis, abscess | บอกว่าต้องกรีด ต้องผ่า หรือทายาได้ |
| **Outside in vs inside out** | **outside in** = เชื้อเข้าจากภายนอก (แผล แมลงกัด) · **inside out** = มาจากในร่างกาย (hematogenous spread) | ชี้ว่าต้องหาแหล่งติดเชื้อที่อื่นไหม |

[[fig:layers]]

#### ทำไมความลึกสำคัญกว่าชื่อโรค
ไล่เป็นห่วงโซ่เหตุ–ผล

| ความลึก | สิ่งที่เกิดขึ้นในเนื้อเยื่อ | สิ่งที่เห็น/คลำได้ |
|---|---|---|
| **Epidermis** | ไม่มีหลอดเลือดและเส้นประสาทของตัวเอง การอักเสบจำกัดอยู่ชั้นบน | สะเก็ด ตุ่มน้ำตื้น · **ไม่มีไข้** · หายแล้ว**ไม่เป็นแผลเป็น** |
| **Upper dermis + superficial lymphatics** | เชื้อเข้าท่อน้ำเหลืองซึ่งมีผนังกั้น | **ขอบคมและยกขึ้น** · ไข้หนาวสั่นมาเร็ว · ต่อมน้ำเหลืองโต |
| **Deep dermis + subcutaneous fat** | เนื้อเยื่อหลวม การอักเสบกระจายออกได้อิสระ | **ขอบเบลอ** บวม ร้อน กดเจ็บ |
| **Fascia** | เลือดไปเลี้ยงน้อย เชื้อลุกลามตามแนว fascia เร็วกว่าที่ผิวจะเปลี่ยนสี | **ปวดเกินกว่าที่ตาเห็น** · ต่อมาจึงมี crepitus และตุ่มเลือด |

> **หลักข้างเตียงที่ใช้ได้จริง** — ก่อนจะนึกชื่อโรค ให้ตอบสามข้อนี้ก่อน
> **1. ขอบรอยโรคคมหรือเบลอ** (คม = ตื้นถึง upper dermis)
> **2. คลำได้นุ่มตรงกลางไหม** (fluctuant = มีหนัง → ต้องกรีด)
> **3. ปวดมากเกินกว่าที่ตาเห็นไหม** (ใช่ = คิด necrotizing fasciitis ทันที)

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **superficial vs deep** | ตื้น (epidermis) vs ลึก (dermis/subcut) | แกนหลักของการแบ่งโรค |
| **outside in / inside out** | เชื้อเข้าจากนอก vs มาจากในกระแสเลือด | ตัดสินว่าต้องหา source ที่อื่น |
| **ill-defined / well-demarcated border** | ขอบเบลอ / ขอบชัด | แยก cellulitis จาก erysipelas |
| **fluctuant** | คลำได้นุ่มเป็นถุงน้ำ/หนองตรงกลาง | ข้อบ่งชี้ **incision and drainage** |
| **crepitus** | คลำได้กรอบแกรบจากแก๊สในเนื้อเยื่อ | สัญญาณของ necrotizing infection |
| **lymphangitic streaking** | รอยแดงเป็นเส้นลากไปต่อมน้ำเหลือง | บอกว่าเชื้อเข้าท่อน้ำเหลืองแล้ว |
| **mimics** | โรคที่หน้าตาเหมือนแต่ไม่ใช่การติดเชื้อ | เหตุผลที่ต้องมี DDx ทุกครั้ง |
""",
    ["แบ่งโรคด้วยสามแกน: ชนิดเชื้อ · ความลึก · outside-in vs inside-out",
     "ความลึกเป็นตัวกำหนดทั้งลักษณะขอบและความเร่งด่วน",
     "ขอบคม = ตื้นถึง upper dermis (erysipelas) · ขอบเบลอ = ลึก (cellulitis)",
     "fluctuant = ต้องกรีดระบาย ไม่ใช่ยาอย่างเดียว",
     "ปวดเกินกว่าที่ตาเห็น = necrotizing fasciitis จนกว่าจะพิสูจน์เป็นอื่น"],
    [mcq(N(1), "A 54-year-old man has a tender erythematous plaque on the shin. Which single bedside feature most reliably tells you the infection involves the deep dermis and subcutaneous fat rather than the upper dermis?",
         ["An ill-defined border that fades gradually into normal skin",
          "The presence of fever and chills",
          "Regional inguinal lymphadenopathy",
          "A honey-coloured crust at the centre of the plaque",
          "Pain on palpation of the plaque"],
         0,
         "**ขอบที่เบลอและค่อย ๆ จางเข้าหาผิวปกติ** บอกว่าการอักเสบอยู่ใน **deep dermis และชั้นไขมัน** ซึ่งเป็นเนื้อเยื่อหลวม ไม่มีผนังกั้นให้การอักเสบหยุดเป็นขอบ จึงเป็น **cellulitis** · ถ้าอยู่แค่ **upper dermis และ superficial lymphatics** ซึ่งมีผนังกั้น ขอบจะ**คมและยกขึ้นคลำได้** แบบ **erysipelas**\n\nทำไมข้ออื่นไม่ช่วยแยกความลึก\n- **ไข้หนาวสั่น** พบได้ทั้ง erysipelas และ cellulitis และที่จริงมักมาเร็วกว่าใน erysipelas จึงไม่ได้บอกว่าลึกกว่า\n- **ต่อมน้ำเหลืองโต** สะท้อนการระบายทางน้ำเหลือง พบได้ทั้งสองโรค\n- **honey-coloured crust** เป็นลักษณะของ **impetigo** ซึ่ง**ตื้นกว่า**ทั้งคู่ ไม่ใช่ลึกกว่า\n- **กดเจ็บ** มีในทุกการติดเชื้อที่ลงถึง dermis จึงไม่จำเพาะ",
         "คำถามแรกข้างเตียงคือ “ขอบคมหรือเบลอ” ไม่ใช่ “มีไข้หรือไม่”",
         "Skin infection — depth and border", R("Classification · Cellulitis · Erysipelas"), NL_SKIN),
     mcq(N(2), "A diabetic patient develops a skin infection on the forearm with no history of trauma, and blood cultures grow the same organism. By the lecture's classification, this is best described as which pattern?",
         ["Inside out — endogenous or haematogenous source",
          "Outside in — exogenous entry through the skin barrier",
          "Superficial infection limited to the epidermis",
          "A mimic of infection rather than a true infection",
          "Parasitic rather than bacterial infection"],
         0,
         "**ไม่มีประวัติบาดแผล + เพาะเชื้อจากเลือดขึ้นเชื้อเดียวกัน** = เชื้อมาถึงผิวหนัง**จากภายในร่างกายผ่านกระแสเลือด** ซึ่งสไลด์เรียกว่า **inside out** · ความสำคัญคือต้อง**ไปหาแหล่งติดเชื้อต้นทาง** เช่น ลิ้นหัวใจ กระดูก หรือทางเดินปัสสาวะ ไม่ใช่รักษาแค่ผิวหนัง\n\nทำไมข้ออื่นผิด\n- **outside in** ต้องมีทางเข้า เช่น แผล รอยแมลงกัด รอยถลอก ซึ่งโจทย์บอกว่าไม่มี\n- **superficial/epidermis** ขัดกับการมี bacteraemia ที่บ่งชี้การติดเชื้อลึกและเข้ากระแสเลือด\n- **mimic** หมายถึงโรคที่ไม่ใช่การติดเชื้อ แต่นี่เพาะเชื้อขึ้นแล้ว\n- **parasitic** ไม่เข้ากับภาพ bacteraemia จากการเพาะเชื้อ",
         "ติดเชื้อผิวหนังที่ไม่มีทางเข้า ให้สงสัย inside out แล้วตามหา source",
         "Skin infection — outside in vs inside out", R("Classification"), NL_SKIN)],
    NL_SKIN, {"layers": F.layers()})

# ───────────────────────────── 2
sec("derm-si-02", "Impetigo และ ecthyma — ตื้นแล้วไม่เป็นแผลเป็น ลึกแล้วเป็น",
    "non-bullous 70% · bullous 30% · ecthyma = impetigo ที่ลึกกว่า", 9,
"""### Impetigo
**การติดเชื้อแบคทีเรียที่ชั้น epidermis ติดต่อได้ง่ายมาก** เชื้อหลักคือ ***Staphylococcus aureus*** บางครั้งร่วมกับ ***Streptococcus pyogenes***

[[fig:impetigo]]

| | **Non-bullous ≈ 70%** | **Bullous ≈ 30%** |
|---|---|---|
| รอยโรคเริ่มต้น | ตุ่มแดงเล็ก ๆ รอบจมูกและปาก | **bullae** ตุ่มน้ำใหญ่ |
| กลไก | เชื้อลุกลามในชั้น epidermis โดยตรง | **staphylococcal exotoxin** ย่อยรอยต่อระหว่างเซลล์ ทำให้ชั้นผิวแยกเป็นถุงน้ำ |
| หลังแตก | ซึม แล้วตกสะเก็ด **honey-yellow crust** | เหลือ **erosion** ที่มีขอบสะเก็ดสีน้ำผึ้ง |

**อาการ** สะเก็ดสีน้ำผึ้ง มัก**ไม่เจ็บ** แต่คันได้ · ตำแหน่งที่พบคือ **ใบหน้า (รอบจมูกและปาก) แขน ขา** · **ไข้พบน้อย** · ต่อมน้ำเหลืองใกล้เคียงโตได้

**การวินิจฉัย** อาศัย**ลักษณะที่เห็น**เป็นหลัก · การ **swab เพาะเชื้อ** ทำเมื่อต้องการเลือกยาให้ตรง เช่น สงสัย **MRSA**

**การรักษา**

| ระดับ | ยา |
|---|---|
| Supportive | **wet compression** ประคบเพื่อลอกสะเก็ด |
| **เฉพาะที่ (mild)** | **mupirocin** หรือ **fusidic acid** ointment |
| **กินยา (ลุกลามหรือหลายตำแหน่ง)** | **cephalexin · dicloxacillin · erythromycin** |
| **MRSA หรือแพ้ penicillin** | **clindamycin · trimethoprim-sulfamethoxazole · vancomycin** |

**ภาวะแทรกซ้อน** ลุกลามเป็น **cellulitis** หรือลึกกว่านั้น · **พบน้อยแต่สำคัญ: post-streptococcal glomerulonephritis**

**การป้องกันและคำแนะนำ** ล้างมือ ปิดแผล ไม่ใช้ของใช้ร่วมกัน · **เด็กกลับโรงเรียนได้หลังเริ่มยา 24 ชั่วโมง เมื่อปิดรอยโรคแล้ว**

### Ecthyma และ ecthyma gangrenosum
**รูปแบบที่เป็นแผล (ulcerative form) ของ impetigo** — เชื้อเดิมคือ *S. aureus* และ *S. pyogenes* แต่**ลงลึกถึง dermis**

- **Morphology** **punched-out ulceration** ขอบเหมือนถูกเจาะ มี **สะเก็ดหนาและติดแน่น (thick adherent crust)** คลุม ล้อมรอบด้วยผื่นแดง
- **ตำแหน่ง** **ขาส่วนล่าง**
- **ผลลัพธ์** **หายแล้วเป็นแผลเป็น (scarring)** ← จุดที่แยกจาก impetigo ชัดที่สุด

#### ทำไมถึงมีอาการนี้

| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **สะเก็ดสีน้ำผึ้ง** | น้ำเหลืองจากรอยโรคตื้นแห้งรวมกับ neutrophil และเชื้อ กลายเป็น serum crust สีเหลืองทอง | เป็นลายเซ็นของ impetigo |
| **ไม่เจ็บแต่คัน** | รอยโรคอยู่เหนือชั้นที่มีปลายประสาทรับความเจ็บหนาแน่น | ต่างจาก cellulitis ที่กดเจ็บชัด |
| **ไข้พบน้อย** | การติดเชื้ออยู่ใน epidermis ซึ่งไม่มีหลอดเลือด เชื้อและ cytokine เข้ากระแสเลือดน้อย | มีไข้ชัด → คิดว่าลึกกว่า impetigo แล้ว |
| **bulla ใน bullous type** | exotoxin ย่อย desmosome ระหว่าง keratinocyte → ชั้นผิวแยกเป็นถุงน้ำ | กลไกเดียวกับที่ทำให้เกิด staphylococcal scalded skin syndrome |
| **แผลเป็นใน ecthyma** | รอยโรคทะลุ **basement membrane** ลงถึง dermis ซึ่งซ่อมด้วยพังผืด | impetigo ไม่เป็นแผลเป็น ecthyma เป็น |

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **honey-coloured crust** | สะเก็ดสีน้ำผึ้ง | ลายเซ็นของ impetigo |
| **non-bullous / bullous** | ไม่มี / มีตุ่มน้ำใหญ่ | สัดส่วน 70% / 30% |
| **exotoxin** | สารพิษที่เชื้อปล่อยออกมา | ต้นเหตุของ bulla |
| **erosion** | ผิวหลุดแค่ชั้น epidermis | หายไม่เป็นแผลเป็น |
| **ulcer** | ผิวหลุดลึกถึง dermis | หายเป็นแผลเป็น |
| **punched-out ulcer** | แผลขอบเหมือนถูกเจาะ | ลายเซ็นของ ecthyma |
| **adherent crust** | สะเก็ดติดแน่น แกะยาก | ต่างจากสะเก็ดบางของ impetigo |
| **post-streptococcal glomerulonephritis** | ไตอักเสบตามหลังติดเชื้อ strep | ภาวะแทรกซ้อนที่ต้องรู้ |
""",
    ["impetigo อยู่แค่ epidermis → non-scarring · ecthyma ลึกถึง dermis → scarring",
     "non-bullous 70% · bullous 30% จาก staphylococcal exotoxin",
     "honey-coloured crust = impetigo · punched-out ulcer + สะเก็ดหนา = ecthyma",
     "ยาทา mupirocin/fusidic acid ในรายเบา · กินยาเมื่อลุกลาม · MRSA ใช้ clindamycin หรือ TMP-SMX",
     "ภาวะแทรกซ้อนที่ต้องจำ: post-streptococcal glomerulonephritis",
     "เด็กกลับโรงเรียนได้ 24 ชม. หลังเริ่มยาและปิดแผล"],
    [mcq(N(3), "A 6-year-old has several lesions around the mouth: thin-walled blisters that ruptured leaving erosions rimmed by honey-coloured crust. Which mechanism explains the blister?",
         ["A staphylococcal exotoxin splitting desmosomal connections within the epidermis",
          "Streptococcal spread along superficial dermal lymphatics",
          "Neutrophilic infiltration of the subcutaneous fat",
          "IgG autoantibodies directed against the basement membrane",
          "Direct invasion of the fascia with secondary skin necrosis"],
         0,
         "นี่คือ **bullous impetigo** · กลไกคือ ***S. aureus* ปล่อย exotoxin ที่ย่อยรอยต่อ desmosome ระหว่าง keratinocyte** ทำให้ชั้น epidermis **แยกออกเป็นถุงน้ำ** ผนังจึงบางและแตกง่าย เหลือ erosion ขอบสะเก็ดสีน้ำผึ้ง · เป็นกลไกเดียวกับ **staphylococcal scalded skin syndrome** แต่จำกัดเฉพาะที่\n\nทำไมข้ออื่นผิด\n- **strep ตามท่อน้ำเหลืองใน upper dermis** คือกลไกของ **erysipelas** ซึ่งให้ผื่นแดงขอบคม ไม่ใช่ตุ่มน้ำ\n- **การอักเสบของชั้นไขมัน** คือ **panniculitis** ให้ก้อนลึกกดเจ็บ ไม่ใช่ตุ่มน้ำตื้น\n- **autoantibody ต่อ basement membrane** คือ **bullous pemphigoid** ซึ่งเป็นโรคภูมิต้านตนเอง ตุ่มน้ำผนังหนากว่าและไม่มีสะเก็ดน้ำผึ้ง เป็นหนึ่งใน mimic ที่สไลด์เตือน\n- **การลุกลามถึง fascia** คือ necrotizing fasciitis ซึ่งปวดรุนแรงและผิวคล้ำ",
         "bullous impetigo = exotoxin แยกชั้น epidermis · อย่าสับสนกับ pemphigoid",
         "Impetigo — bullous mechanism", R("Impetigo · Forms"), ["2.3.12(9)", "B4.2.2(4)"]),
     mcq(N(4), "Which feature best distinguishes ecthyma from ordinary impetigo?",
         ["It heals with scarring because the lesion extends below the epidermis",
          "It is caused by Pseudomonas rather than staphylococci or streptococci",
          "It is characteristically painless and non-pruritic",
          "It occurs on the face rather than on the lower legs",
          "It responds only to intravenous antibiotics"],
         0,
         "**ecthyma คือ impetigo ที่ลึกกว่า** — ทะลุ **basement membrane** ลงถึง **dermis** จึงเป็น **ulcer** (ไม่ใช่ erosion) และ **หายเป็นแผลเป็น** ซึ่งเป็นข้อแตกต่างที่ใช้ได้จริงที่สุด · ลักษณะที่เห็นคือ **punched-out ulcer + สะเก็ดหนาติดแน่น**\n\nทำไมข้ออื่นผิด\n- **เชื้อ**เหมือนกันคือ *S. aureus* และ *S. pyogenes* · ส่วน ***ecthyma gangrenosum*** ซึ่งสัมพันธ์กับ **Pseudomonas** ในผู้ป่วย neutropenia เป็น**อีกภาวะหนึ่ง** ชื่อคล้ายกันแต่ไม่ใช่ ecthyma ธรรมดา\n- **ไม่เจ็บ**เป็นลักษณะของ impetigo มากกว่า\n- **ตำแหน่ง**กลับกัน — ecthyma อยู่ที่**ขาส่วนล่าง** ส่วน impetigo อยู่ที่ใบหน้า\n- ไม่จำเป็นต้องให้ยาทางหลอดเลือดดำเสมอ ขึ้นกับความรุนแรง",
         "ecthyma = ulcer + สะเก็ดหนา + ขาส่วนล่าง + เป็นแผลเป็น",
         "Ecthyma vs impetigo", R("Ecthyma"), ["2.3.12(9)", "B4.2.2(4)"])],
    ["2.3.12(9)", "B4.2.2(4)"], {"impetigo": F.impetigo()})

# ───────────────────────────── 3
NL_CELL = ["2.3.12(4)", "B4.2.2(3)"]
sec("derm-si-03", "Erysipelas · cellulitis · lymphangitis — ตระกูลเดียวกันที่ต่างความลึก",
    "ขอบคมยกขึ้น vs ขอบเบลอ · เส้นแดงลากไปต่อมน้ำเหลือง", 11,
"""สามโรคนี้มาจากตระกูลเดียวกัน (**ส่วนใหญ่คือ *Streptococcus pyogenes***) แต่อยู่คนละชั้นและคนละทาง จึงให้ภาพต่างกันชัดเจน

[[fig:border]]

### Erysipelas
- **นิยามตามสไลด์** **superficial form of cellulitis** ที่กิน **upper dermis ร่วมกับ superficial dermal lymphatics**
- **เชื้อ** ***Streptococcus pyogenes***
- **ลายเซ็น** **ขอบชัดเจน ยกขึ้น คลำได้ (sharply defined, raised border)**
- **อาการ** ผื่นแดงสด บวม กดเจ็บ **ขอบคม** · มี**ไข้ หนาวสั่น ต่อมน้ำเหลืองโต**ร่วมได้
- **ตำแหน่งที่พบบ่อย** **ใบหน้า และ ขา**
- **การวินิจฉัย** อาศัยลักษณะทางคลินิกเป็นหลัก
- **การรักษา** **penicillin กิน** หรือ **first-generation cephalosporin** · **อย่างน้อย 5 วัน** ปรับตามความรุนแรงและการเป็นซ้ำ

### Cellulitis
- **นิยาม** การติดเชื้อ **deep dermis ถึง subcutaneous tissue**
- **ลักษณะ** ผื่นแดง บวม **อุ่น** เป็น **plaque ขอบไม่ชัด (ill-defined)** มัก**ข้างเดียว** และ **เจ็บ**
- **อาการทั่วกาย** **ไข้ หนาวสั่น พบบ่อย**
- **เชื้อ** พบบ่อยคือ **gram-positive cocci** — *S. pyogenes*, *S. aureus* · ที่พบน้อยคือ **gram-negative bacilli**
- **ปัจจัยเสี่ยง** **ผิวหนังเสียความต่อเนื่อง (skin barrier disruption) · ขาบวม · venous insufficiency**
- **การวินิจฉัย** clinical · **เพาะเชื้อเมื่อมี abscess**

### Lymphangitis
- **นิยาม** การอักเสบของ **ท่อน้ำเหลือง** ตามหลังการติดเชื้อที่ผิวหนัง
- **เชื้อ** **_Streptococcus pyogenes_ เป็นส่วนใหญ่**
- **ลายเซ็น** **เส้นแดงกดเจ็บลากจากแผลไปทางต่อมน้ำเหลือง (lymphangitic streaking)** · มีไข้ หนาวสั่น อ่อนเพลีย
- **การวินิจฉัย** ตรวจร่างกาย · เพาะเชื้อจากแผลหรือเลือดถ้ามีอาการทั่วกาย
- **การรักษา** ยาฆ่าเชื้อกินหรือทางหลอดเลือดดำ (**penicillin, cephalexin**) **และรักษาแผลต้นทางด้วย**
- **ภาวะแทรกซ้อน** ลุกลามเป็น **bacteraemia และ sepsis**

#### ทำไมถึงมีอาการนี้

| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ขอบคมยกขึ้นใน erysipelas** | เชื้อแพร่ไปตาม **superficial lymphatics** ซึ่งมีผนังและทิศทางชัดเจน การอักเสบจึงหยุดเป็นขอบและบวมยกขึ้น | ขอบคม = erysipelas แทบทุกครั้ง |
| **ขอบเบลอใน cellulitis** | อยู่ใน **deep dermis และไขมัน** ที่เนื้อเยื่อหลวม ไม่มีผนังกั้น การอักเสบจึงค่อย ๆ จาง | ขอบเบลอ = ลึกกว่า |
| **ไข้หนาวสั่นมาเร็วใน erysipelas** | ท่อน้ำเหลืองต่อตรงเข้าสู่กระแสเลือด เชื้อและ cytokine จึงเข้าระบบเร็ว | อาการทั่วกายเด่นแต่รอยโรคตื้น = erysipelas |
| **เส้นแดงเป็นทางใน lymphangitis** | เชื้อเดินอยู่**ในลำท่อน้ำเหลือง** การอักเสบจึงเป็นเส้นตามแนวท่อ ไม่ใช่แผ่กว้าง | เห็นเส้น = เชื้อเข้าท่อน้ำเหลืองแล้ว ต้องให้ยาเร็ว |
| **บวมข้างเดียว** | การอุดกั้นและอักเสบของท่อน้ำเหลืองข้างนั้น | cellulitis สองข้างพร้อมกันพบน้อย ให้คิด mimic เช่น stasis dermatitis |

> **mimic ที่ต้องนึกถึงเสมอ** — **stasis dermatitis** และ **lipodermatosclerosis** ของคนขาบวมเรื้อรัง มักเป็น **สองข้าง** **ไม่มีไข้** และ **ไม่ลุกลามเป็นชั่วโมง** ขณะที่ cellulitis มัก**ข้างเดียว มีไข้ และแย่ลงเร็ว**

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **sharply defined, raised border** | ขอบชัดและยกขึ้น | ลายเซ็นของ erysipelas |
| **ill-defined border** | ขอบไม่ชัด | ลายเซ็นของ cellulitis |
| **superficial dermal lymphatics** | ท่อน้ำเหลืองตื้นใน dermis | เหตุผลที่ erysipelas ขอบคม |
| **lymphangitic streaking** | เส้นแดงลากไปต่อมน้ำเหลือง | lymphangitis |
| **skin barrier disruption** | ผิวหนังเสียความต่อเนื่อง | ปัจจัยเสี่ยงหลักของ cellulitis |
| **venous insufficiency** | หลอดเลือดดำทำงานบกพร่อง | ปัจจัยเสี่ยงและ mimic |
| **unilateral** | ข้างเดียว | cellulitis มักข้างเดียว |
| **stasis dermatitis** | ผื่นจากเลือดดำคั่ง | mimic ที่พบบ่อยที่สุด |
""",
    ["erysipelas = upper dermis + lymphatics → ขอบคมยกขึ้น · ไข้มาเร็ว · หน้าและขา",
     "cellulitis = deep dermis ถึง subcut → ขอบเบลอ · ข้างเดียว · อุ่นและเจ็บ",
     "erysipelas รักษาด้วย penicillin หรือ first-gen cephalosporin อย่างน้อย 5 วัน",
     "lymphangitis = เส้นแดงลากไปต่อมน้ำเหลือง จาก S. pyogenes ต้องรักษาแผลต้นทางด้วย",
     "ปัจจัยเสี่ยง cellulitis: ผิวแตก ขาบวม venous insufficiency",
     "สองข้าง ไม่มีไข้ ไม่ลุกลามเร็ว → คิด stasis dermatitis ไม่ใช่ cellulitis"],
    [mcq(N(5), "A 62-year-old woman has a bright red, tender, swollen plaque on the cheek with a sharply demarcated, palpably raised edge, plus fever and chills that began within hours. Which is the most likely diagnosis and its usual organism?",
         ["Erysipelas caused by Streptococcus pyogenes",
          "Cellulitis caused by Staphylococcus aureus",
          "Necrotizing fasciitis caused by polymicrobial flora",
          "Infective panniculitis caused by atypical mycobacteria",
          "Contact dermatitis from a topical product"],
         0,
         "**ขอบชัดและยกขึ้นคลำได้ + ใบหน้า + ไข้หนาวสั่นมาเร็ว** = **erysipelas** จาก ***S. pyogenes*** · เหตุผลเชิงกลไกคือรอยโรคอยู่ใน **upper dermis และ superficial lymphatics** ซึ่งมีผนังกั้นทำให้ขอบคม และต่อตรงเข้ากระแสเลือดทำให้มีอาการทั่วกายเร็ว\n\nทำไมข้ออื่นผิด\n- **cellulitis** ขอบ**ไม่ชัด** เพราะอยู่ลึกใน deep dermis และไขมัน จึงไม่เข้ากับขอบที่คลำได้\n- **necrotizing fasciitis** จะ**ปวดรุนแรงเกินกว่าที่ตาเห็น** มีผิวคล้ำ ตุ่มเลือด หรือ crepitus และอาการทรุดเร็วกว่านี้มาก\n- **infective panniculitis** ให้**ก้อนลึกกดเจ็บ** ไม่ใช่ผื่นแดงขอบคม และดำเนินโรคช้ากว่า\n- **contact dermatitis** คัน ไม่ใช่เจ็บ ไม่มีไข้ และมักมีขอบตรงตามบริเวณที่สัมผัส",
         "ขอบคม + ยกขึ้น + ใบหน้า + ไข้เร็ว = erysipelas → penicillin",
         "Erysipelas", R("Erysipelas"), NL_CELL),
     mcq(N(6), "A patient with a small infected wound on the dorsum of the hand now has tender red streaks running up the forearm toward the axilla, with fever. What does this finding indicate and what must be included in management?",
         ["Lymphangitis — antibiotics plus treatment of the original wound",
          "Necrotizing fasciitis — immediate surgical debridement",
          "Deep vein thrombosis — therapeutic anticoagulation",
          "Allergic contact dermatitis — topical corticosteroid",
          "Erysipelas — no antibiotic needed as it is self-limiting"],
         0,
         "**เส้นแดงกดเจ็บลากจากแผลไปทางต่อมน้ำเหลือง (lymphangitic streaking)** = **lymphangitis** ซึ่งแปลว่า**เชื้อเข้าไปอยู่ในลำท่อน้ำเหลืองแล้ว** และเสี่ยงต่อ **bacteraemia/sepsis** · การรักษาต้องให้ยาฆ่าเชื้อ **และจัดการแผลต้นทาง** เพราะถ้าไม่แก้ที่มา เชื้อจะป้อนเข้าท่อน้ำเหลืองต่อเนื่อง\n\nทำไมข้ออื่นผิด\n- **necrotizing fasciitis** ต้องมีปวดเกินกว่าที่ตาเห็น ผิวคล้ำ ตุ่มเลือด หรือ crepitus — เส้นแดงตามท่อน้ำเหลืองเพียงอย่างเดียวไม่ใช่ข้อบ่งชี้ผ่าตัด\n- **DVT** บวมทั้งแขน ไม่ให้เส้นแดงตามแนวท่อน้ำเหลืองจากแผล และมักไม่มีไข้จากแผล\n- **contact dermatitis** คัน ไม่เจ็บ ไม่มีไข้ และไม่เป็นเส้นลากไปต่อมน้ำเหลือง\n- **erysipelas** ต้องให้ยาฆ่าเชื้อ ไม่ใช่โรคที่หายเองได้ — ส่วนที่ว่า “ไม่ต้องให้ยา” ผิดอย่างชัดเจน",
         "เห็นเส้นแดงลากไปต่อมน้ำเหลือง = รักษาทั้งยาและแผลต้นทาง",
         "Lymphangitis", R("Lymphangitis"), NL_CELL),
     mcq(N(7), "Which combination is the classic risk-factor triad for bacterial cellulitis given in the lecture?",
         ["Skin barrier disruption, oedema, and venous insufficiency",
          "Aquatic exposure, trauma, and cosmetic procedures",
          "Prior tuberculosis, endemic exposure, and immunosuppression",
          "Diabetes, environmental fungal exposure, and neutropenia",
          "Recent travel, insect bite, and antibiotic use"],
         0,
         "สไลด์ระบุปัจจัยเสี่ยงของ **bacterial cellulitis** ไว้สามข้อ — **skin barrier disruption · oedema · venous insufficiency** · ทั้งสามข้อเชื่อมกันเชิงกลไก: ผิวที่แตกเปิดทางให้เชื้อเข้า ขาที่บวมทำให้น้ำเหลืองระบายช้าและภูมิคุ้มกันเข้าถึงได้น้อย และหลอดเลือดดำที่บกพร่องทำให้ทั้งสองอย่างนั้นเรื้อรัง\n\nทำไมข้ออื่นผิด — แต่ละข้อคือปัจจัยเสี่ยงของ cellulitis **ชนิดอื่น** ในตารางเดียวกันของสไลด์\n- **aquatic exposure, trauma, cosmetic procedure** = **NTM cellulitis** (*M. marinum* ฯลฯ)\n- **prior TB, endemic exposure, immunosuppression** = **tuberculous cellulitis**\n- **immunosuppression, DM, environmental exposure** = **fungal cellulitis**\n- ข้อสุดท้ายไม่ใช่ชุดปัจจัยเสี่ยงที่สไลด์ระบุ",
         "ผิวแตก + ขาบวม + venous insufficiency = ชุดเสี่ยงของ cellulitis แบคทีเรีย",
         "Cellulitis — risk factors", R("Cellulitis table"), NL_CELL)],
    NL_CELL, {"border": F.border()})

# ───────────────────────────── 4
sec("derm-si-04", "Cellulitis ที่ไม่ใช่แบคทีเรียธรรมดา — fungal · TB · NTM",
    "ตารางสี่ช่องของสไลด์ · เบาะแสคือความเร็วและบริบท", 10,
"""สไลด์มีตารางเทียบ cellulitis สี่แบบ ซึ่งเป็นหัวใจของคาบนี้ **เพราะคนไข้ที่ “cellulitis ไม่ดีขึ้นด้วยยาปฏิชีวนะ” มักอยู่ในสามคอลัมน์ขวา**

| | **Bacterial** | **Fungal** | **Tuberculous** | **NTM** |
|---|---|---|---|---|
| **Etiology** | **GPC** — *S. pyogenes*, *S. aureus* · (uncommon GNB) | *Candida* spp. · **Mucorales** · dimorphic fungi · ***Sporothrix schenckii*** | ***Mycobacterium tuberculosis*** | ***M. marinum*** · *M. fortuitum* · *M. abscessus* · *M. ulcerans* |
| **Onset** | **เฉียบพลัน — ชั่วโมงถึงวัน** | **subacute ถึง chronic — วันถึงสัปดาห์** | **chronic — สัปดาห์ถึงเดือน** | **subacute — 1–4 สัปดาห์** |
| **Morphology** | แดง อุ่น บวม กดเจ็บ **ขอบไม่ชัด** | **violaceous** หรือแดง **indurated plaque** · เป็นแผลได้ | **violaceous nodule/plaque** · เป็นแผลหรือเกิด **sinus tract** | **nodule สีแดงคล้ำ** plaque แผล หรือ abscess |
| **Symptoms** | **ไข้ หนาวสั่น ปวด** · **lymphangitic streaking** | อาการทั่วกาย**น้อย** · ปวดเฉพาะที่หรือมีเนื้อตาย | **มัก ไม่มีไข้** · ต่อมน้ำเหลืองในบริเวณโตได้ | ปวดเฉพาะที่ · อาการทั่วกาย**พบน้อย** |
| **Common sites** | บริเวณที่มีบาดแผล — ขาส่วนล่าง ใบหน้า | ตามเชื้อ — ซอกพับ ใบหน้า แขนขา | **คอ แขนขา** (แพร่ตามน้ำเหลืองหรือทางเลือด) | **มือ แขน** แผลผ่าตัดหรือจุดฉีดยา |
| **Risk factors** | **ผิวแตก ขาบวม venous insufficiency** | **ภาวะกดภูมิ เบาหวาน การสัมผัสสิ่งแวดล้อม** | **เคยเป็น TB · พื้นที่ระบาด · ภาวะกดภูมิ** | **สัมผัสน้ำ** บาดแผล หัตถการเสริมความงาม/ผ่าตัด |
| **Diagnosis** | clinical · เพาะเชื้อถ้ามี abscess | **biopsy + fungal stain (PAS, GMS)** · fungal culture | **biopsy · AFB stain · PCR · culture** | biopsy · AFB · culture |
| **Treatment** | ยาฆ่าเชื้อกินหรือ IV | **ยาต้านเชื้อราทั้งระบบ** (itraconazole, amphotericin B) | **RIPE** — rifampin, isoniazid, pyrazinamide, ethambutol | **ยาหลายตัวร่วมกัน** (clarithromycin, rifampin ฯลฯ) |
| **Prognosis** | ดีถ้ารักษาเร็ว · **เป็นซ้ำได้** | ขึ้นกับภูมิคุ้มกันและชนิดเชื้อ | ดี แต่**ต้องรักษานาน** | มัก**ต้องรักษานาน** · อาจต้อง **surgical debridement** |

#### ทำไมความเร็วของโรคบอกชนิดเชื้อได้
ไล่เป็นเหตุ–ผล

- **แบคทีเรียธรรมดาแบ่งตัวทุก 20–30 นาที** และกระตุ้น neutrophil ทันที → **บวมแดงร้อนภายในชั่วโมง** และมีไข้
- **เชื้อราและ mycobacteria แบ่งตัวช้ากว่าหลายสิบเท่า** และกระตุ้นการอักเสบแบบ **granuloma** ที่ใช้เวลาสร้าง → รอยโรค**ค่อย ๆ แข็งเป็น indurated plaque** สีคล้ำม่วง และ**มักไม่มีไข้**
- **granuloma ที่สลายตัว** จึงกลายเป็น **แผลเรื้อรังและ sinus tract** ซึ่งเป็นภาพของ TB และ NTM ไม่ใช่ของแบคทีเรียเฉียบพลัน

> **กฎการใช้งานจริง** — **cellulitis ที่ให้ยาปฏิชีวนะครบแล้วยังไม่ดีขึ้น หรือดำเนินโรคเป็นสัปดาห์ขึ้นไป ต้อง biopsy** และส่ง **ย้อมเชื้อรา (PAS, GMS) · AFB · PCR · เพาะเชื้อ** พร้อมกัน เพราะการวินิจฉัยสามคอลัมน์ขวา**ทำด้วยตาเปล่าไม่ได้**

> **เบาะแสจากประวัติที่ชี้ตรง** — **สัมผัสน้ำ ตู้ปลา ทำเล็บ หรือหัตถการเสริมความงาม → NTM** · **คอโตเรื้อรังไม่มีไข้ → TB** · **กดภูมิหรือเบาหวานคุมไม่ได้ + รอยโรคมีเนื้อตาย → เชื้อรากลุ่ม Mucorales**

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **indurated plaque** | ปื้นแข็งคลำได้เป็นแผ่น | ภาพของเชื้อราและ mycobacteria |
| **violaceous** | สีม่วงคล้ำ | สีของรอยโรคเรื้อรัง |
| **sinus tract** | ทางเชื่อมเป็นรูระบายจากรอยโรคออกผิว | TB และ NTM |
| **AFB stain** | ย้อมหาเชื้อที่ทนกรด | ตรวจหา mycobacteria |
| **PAS / GMS** | ย้อมจำเพาะสำหรับเชื้อรา | ตรวจชิ้นเนื้อหาเชื้อรา |
| **RIPE** | rifampin · isoniazid · pyrazinamide · ethambutol | สูตรยา TB |
| **NTM** | non-tuberculous mycobacteria | กลุ่ม M. marinum, fortuitum, abscessus, ulcerans |
| **dimorphic fungi** | เชื้อราที่มีสองรูปแบบตามอุณหภูมิ | กลุ่มที่ก่อ cellulitis เรื้อรัง |
| **Sporothrix schenckii** | เชื้อราจากดิน หนามตำ | sporotrichosis |
""",
    ["cellulitis ที่ดื้อยาหรือเป็นสัปดาห์ = ต้อง biopsy ส่ง fungal stain + AFB + PCR + culture",
     "เฉียบพลันชั่วโมง = แบคทีเรีย · วันถึงสัปดาห์ = เชื้อรา · สัปดาห์ถึงเดือน = TB · 1–4 สัปดาห์ = NTM",
     "indurated violaceous plaque + ไม่มีไข้ = คิดเชื้อราหรือ mycobacteria",
     "สัมผัสน้ำหรือหัตถการเสริมความงาม = NTM (M. marinum)",
     "TB cellulitis รักษาด้วย RIPE · NTM ใช้ยาหลายตัวและอาจต้อง debridement"],
    [mcq(N(8), "A 45-year-old aquarium hobbyist has a 3-week history of painful red-brown nodules on the dorsum of the right hand that have not responded to two courses of oral cephalexin. Which investigation is most likely to establish the diagnosis?",
         ["Skin biopsy for acid-fast staining and mycobacterial culture",
          "Blood cultures drawn during a fever spike",
          "Wound swab for routine aerobic bacterial culture",
          "Serum beta-D-glucan and galactomannan",
          "Doppler ultrasound of the hand and forearm"],
         0,
         "**สัมผัสน้ำ/ตู้ปลา + รอยโรคที่มือ + ดำเนินโรค 1–4 สัปดาห์ + ไม่ตอบสนองยาแบคทีเรียทั่วไป** = ภาพของ **NTM cellulitis** โดยเฉพาะ ***Mycobacterium marinum*** · ตารางของสไลด์ระบุการวินิจฉัยไว้ชัดว่าใช้ **biopsy ร่วมกับ AFB stain และ culture**\n\nทำไมข้ออื่นผิด\n- **เพาะเชื้อจากเลือด** ให้ผลลบเพราะ NTM ที่ผิวหนังมัก**ไม่มีอาการทั่วกาย**และไม่เข้ากระแสเลือด\n- **swab เพาะเชื้อธรรมดา** ขึ้นเฉพาะแบคทีเรียทั่วไป **ไม่ขึ้น mycobacteria** ที่ต้องใช้อาหารเลี้ยงและเวลาจำเพาะ จึงอธิบายไม่ได้ว่าทำไมยาไม่ได้ผล\n- **beta-D-glucan และ galactomannan** ใช้คัดกรอง**เชื้อราในระบบ** ไม่ใช่ NTM และไม่เหมาะกับรอยโรคเฉพาะที่\n- **Doppler** ตรวจหลอดเลือด ไม่ตอบคำถามเรื่องเชื้อ",
         "ตู้ปลา + มือ + ดื้อยา = M. marinum → biopsy + AFB + culture",
         "NTM cellulitis", R("Cellulitis table — NTM"), ["2.3.12(4)", "2.3.12(11)"]),
     mcq(N(9), "Compared with bacterial cellulitis, which set of features best characterises tuberculous cellulitis in the lecture's table?",
         ["Chronic course over weeks to months, usually afebrile, violaceous plaques that may form sinus tracts",
          "Acute onset over hours, high fever, and lymphangitic streaking",
          "Subacute onset after aquatic exposure with nodules on the hands",
          "Rapidly spreading necrosis with crepitus and hemorrhagic bullae",
          "Pruritic bilateral plaques on the shins without systemic symptoms"],
         0,
         "ตารางสไลด์ระบุ **tuberculous cellulitis** ว่า **chronic เป็นสัปดาห์ถึงเดือน · มักไม่มีไข้ · violaceous nodule/plaque ที่เป็นแผลหรือเกิด sinus tract ได้** · กลไกคือ granulomatous inflammation ที่ก่อตัวช้าแล้วสลายเป็นทางระบาย\n\nทำไมข้ออื่นผิด\n- **เฉียบพลัน ไข้สูง lymphangitic streaking** = **bacterial** cellulitis\n- **subacute หลังสัมผัสน้ำ รอยโรคที่มือ** = **NTM**\n- **เนื้อตายลุกลามเร็ว crepitus ตุ่มเลือด** = **necrotizing fasciitis** ไม่ใช่ cellulitis จาก TB\n- **ผื่นคันสองข้างที่หน้าแข้งไม่มีอาการทั่วกาย** = **stasis dermatitis** ซึ่งเป็น mimic ที่ไม่ใช่การติดเชื้อ",
         "TB cellulitis: เรื้อรัง ไม่มีไข้ ม่วงคล้ำ และมี sinus tract",
         "Tuberculous cellulitis", R("Cellulitis table — TB"), ["2.3.12(4)", "2.3.12(11)"])],
    ["2.3.12(4)", "2.3.12(11)"])

# ───────────────────────────── 5
NL_ABS = ["2.3.12(2)", "B4.2.2(2)", "2.1.54"]
sec("derm-si-05", "Abscess และ infective panniculitis — คลำได้นุ่มคือเส้นแบ่งการรักษา",
    "fluctuance → I&D · ก้อนลึกไม่ fluctuant → biopsy", 9,
"""### Abscess
- **นิยาม** การสะสมของ **หนอง (pus)** เป็นโพรงเฉพาะที่ในเนื้อเยื่อ เกิดจาก **แบคทีเรีย เชื้อรา หรือ mycobacteria**
- **เชื้อที่พบบ่อยที่สุด** ***Staphylococcus aureus***
- **อาการ** ก้อนแดง บวม เจ็บ · **คลำได้นุ่มตรงกลาง (fluctuant center)** · หนองแตกออกเองได้
- **การวินิจฉัย** **เพาะเชื้อจากหนองที่ระบายออกมา** ช่วยเลือกยา
- **การรักษา** **หลักคือ incision and drainage (I&D)** · ยาฆ่าเชื้อให้ตามเชื้อที่พบ
- **ภาวะแทรกซ้อน** ลุกลามเข้ากระแสเลือดหรือเนื้อเยื่อลึก

> **เหตุผลที่ยาอย่างเดียวไม่พอ** — ในโพรงหนองมี **pH ต่ำ ออกซิเจนน้อย และมีเอนไซม์จากเม็ดเลือดขาวจำนวนมาก** ซึ่ง**ลดฤทธิ์ยาปฏิชีวนะ** และยาก็ซึมเข้าโพรงที่ไม่มีหลอดเลือดได้น้อย จึงต้อง**ระบายหนองออกก่อน**

### Infective panniculitis
- **นิยาม** การติดเชื้อของ **ชั้นไขมันใต้ผิวหนัง (subcutaneous fat)**
- **เชื้อ** *Staphylococcus* · *Streptococcus* · **atypical mycobacteria** · เชื้อรา เช่น ***Histoplasma***
- **อาการ** **ก้อนลึกที่เจ็บ แต่ ไม่ fluctuant** · พบที่ **ขาและก้น** · เป็นแผลหรือมีน้ำเหลืองไหลได้
- **การวินิจฉัย** **biopsy** ร่วมกับการย้อมและเพาะเชื้อจำเพาะ
- **การรักษา** ตามสาเหตุ — **ยาปฏิชีวนะ ยาต้านเชื้อรา หรือยาต้าน mycobacteria**

#### ทำไมถึงมีอาการนี้

| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **fluctuance ใน abscess** | หนองเป็นของเหลวอยู่ในโพรงที่มีผนัง จึงกดแล้วยวบและเด้งกลับ | **มี fluctuance → กรีดระบาย** |
| **ก้อนลึกแข็งไม่ยวบใน panniculitis** | การอักเสบกระจายอยู่ใน **กลีบไขมัน** ยังไม่รวมเป็นโพรงหนอง | **ไม่ fluctuant → กรีดไม่ได้ประโยชน์ ต้อง biopsy** |
| **ตำแหน่งที่ขาและก้น** | เป็นบริเวณที่ชั้นไขมันหนาที่สุด | ช่วยยืนยันว่าเป็นโรคของชั้นไขมัน |
| **หนองแตกออกเอง** | ความดันในโพรงสูงขึ้นจนทะลุผิวที่บางที่สุด | เป็นการระบายตามธรรมชาติ แต่ยังควรระบายให้หมด |

> **DDx ที่ต้องแยกจาก infective panniculitis** — **erythema nodosum** ซึ่งเป็น panniculitis ที่**ไม่ใช่การติดเชื้อ** มักขึ้น**สองข้างที่หน้าแข้ง** **ไม่เป็นแผล** และ**ไม่มีหนอง** (รายละเอียดอยู่ในคาบ Derm1)

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **abscess** | โพรงหนองเฉพาะที่ | เชื้อหลัก S. aureus |
| **fluctuant** | กดแล้วยวบเพราะมีของเหลวในโพรง | เส้นแบ่งว่าต้องกรีดหรือไม่ |
| **incision and drainage (I&D)** | กรีดและระบายหนอง | การรักษาหลักของ abscess |
| **panniculitis** | การอักเสบของชั้นไขมันใต้ผิวหนัง | ก้อนลึกกดเจ็บ |
| **subcutaneous nodule** | ก้อนใต้ผิวหนัง | คำบรรยายรอยโรคของ panniculitis |
| **atypical mycobacteria** | mycobacteria ที่ไม่ใช่ TB | สาเหตุหนึ่งของ panniculitis |
| **erythema nodosum** | panniculitis ที่ไม่ติดเชื้อ | DDx หลัก |
""",
    ["abscess เชื้อหลักคือ S. aureus · การรักษาหลักคือ I&D ไม่ใช่ยาอย่างเดียว",
     "fluctuance คือเส้นแบ่ง — มี = กรีด · ไม่มี = หาทางอื่น",
     "ยาซึมเข้าโพรงหนองได้น้อยและถูกลดฤทธิ์ด้วย pH ต่ำกับออกซิเจนน้อย",
     "infective panniculitis = ก้อนลึกเจ็บแต่ไม่ fluctuant ที่ขาและก้น → biopsy",
     "panniculitis เชื้อได้ทั้งแบคทีเรีย atypical mycobacteria และ Histoplasma",
     "DDx ของก้อนที่หน้าแข้งสองข้างไม่เป็นแผล = erythema nodosum"],
    [mcq(N(10), "A 29-year-old man has a 4 cm tender erythematous lump on the buttock with a soft, fluctuant centre. What is the single most important step in management?",
         ["Incision and drainage",
          "Oral dicloxacillin alone for 7 days",
          "Topical mupirocin three times daily",
          "Punch biopsy for fungal and mycobacterial stains",
          "Compression dressing and observation for 48 hours"],
         0,
         "**fluctuant = มีหนองเป็นโพรง** ซึ่งคือ **abscess** · การรักษาหลักตามสไลด์คือ **incision and drainage** · เหตุผลเชิงกลไกคือภายในโพรงมี **pH ต่ำ ออกซิเจนน้อย และเอนไซม์จากเม็ดเลือดขาว** ที่ลดฤทธิ์ยา และยาซึมเข้าโพรงที่ไม่มีหลอดเลือดได้น้อย **ยาอย่างเดียวจึงไม่หาย**\n\nทำไมข้ออื่นผิด\n- **ยากินอย่างเดียว** ไม่สามารถกำจัดหนองในโพรงได้ · ยาเป็นส่วนเสริมหลังระบาย ไม่ใช่แทนการระบาย\n- **ยาทา** ซึมไม่ถึงชั้นที่มีโพรงหนอง ใช้ได้กับรอยโรคตื้นระดับ impetigo\n- **biopsy หาเชื้อราและ mycobacteria** เหมาะกับก้อนลึก**ที่ไม่ fluctuant** และดำเนินโรคเรื้อรัง ไม่ใช่ abscess เฉียบพลันที่คลำได้หนอง\n- **ประคบและสังเกตอาการ** ทำให้ช้าและเสี่ยงลุกลามเข้ากระแสเลือด",
         "คลำได้นุ่มตรงกลาง = กรีดระบาย ยาเป็นของเสริม",
         "Abscess — management", R("Abscess"), NL_ABS),
     mcq(N(11), "A 51-year-old woman with poorly controlled diabetes has three painful deep nodules on the shin over six weeks. They are firm, not fluctuant, and one has begun to drain serous fluid. Which next step fits the lecture's approach?",
         ["Skin biopsy with culture and special stains for fungi and mycobacteria",
          "Incision and drainage of each nodule",
          "Empirical oral cephalexin and review in one week",
          "Topical corticosteroid for suspected erythema nodosum",
          "Duplex ultrasound to exclude superficial thrombophlebitis"],
         0,
         "**ก้อนลึกเจ็บ ไม่ fluctuant ดำเนินโรคหลายสัปดาห์ในผู้ป่วยเบาหวาน** = ภาพของ **infective panniculitis** ซึ่งสไลด์ระบุการวินิจฉัยไว้ว่า **biopsy ร่วมกับการเพาะเชื้อและย้อมจำเพาะ** เพราะเชื้อที่เป็นไปได้รวม **atypical mycobacteria และเชื้อรา** ที่ตรวจด้วยวิธีปกติไม่พบ\n\nทำไมข้ออื่นผิด\n- **กรีดระบาย** ไม่ได้ประโยชน์เมื่อ**ยังไม่มีโพรงหนอง** (ไม่ fluctuant) และทำให้เกิดแผลเปิดเพิ่ม\n- **ยากินตามประสบการณ์** เสี่ยงพลาด เพราะถ้าเป็น mycobacteria หรือเชื้อราจะไม่ตอบสนอง และเสียเวลาอีกหนึ่งสัปดาห์\n- **ยาทาสเตียรอยด์** จะกดภูมิเฉพาะที่และทำให้การติดเชื้อแย่ลง · และ erythema nodosum มัก**สองข้างและไม่เป็นแผล**\n- **duplex** ตรวจหลอดเลือด ไม่ตอบคำถามเรื่องเชื้อในชั้นไขมัน",
         "ก้อนลึกไม่ fluctuant + เรื้อรัง = biopsy อย่ากรีดและอย่าให้สเตียรอยด์",
         "Infective panniculitis", R("Infective panniculitis"), NL_ABS)],
    NL_ABS)

# ───────────────────────────── 6
sec("derm-si-06", "Folliculitis → furuncle → carbuncle — เรื่องเดียวกันที่ลึกขึ้น",
    "ลึกขึ้นและรวมหลายรูขุมขน = ชื่อเปลี่ยน การรักษาเปลี่ยน", 8,
"""### Folliculitis
- **นิยาม** การติดเชื้อ**ตื้น**ของ **รูขุมขน (hair follicle)**
- **เชื้อ** ***Staphylococcus aureus*** เป็นหลัก · ที่พบไม่บ่อยคือ ***Pseudomonas* spp. — “hot tub folliculitis”** · เชื้อรา · เริม
- **เกิดที่ไหนก็ได้ที่มีขน**
- **อาการ** ตุ่มแดงหรือตุ่มหัวขาวเล็ก ๆ **อยู่กลางรูขุมขน** · คัน กดเจ็บ หรือปวดเล็กน้อย
- **การวินิจฉัย** clinical
- **การรักษา** สบู่หรือน้ำยาฆ่าเชื้อ · ยาทา **mupirocin** หรือ **clindamycin** · ถ้ารุนแรงหรือเป็นซ้ำจึงให้**ยากิน**
- **การป้องกัน** โกนให้ถูกวิธี เลี่ยงเสื้อผ้ารัด รักษาสุขอนามัย
- **ภาวะแทรกซ้อน** ลุกลามเป็น **furuncle** หรือ **carbuncle**

[[fig:follicle]]

### ลำดับที่ต้องจำให้ขึ้นใจ

| ชื่อ | ขอบเขต | สิ่งที่คลำได้ | การรักษาหลัก |
|---|---|---|---|
| **Folliculitis** | ปากรูขุมขน **หนึ่ง**รู ตื้น | ตุ่มเล็ก ไม่มีโพรงหนอง | **ยาทา** |
| **Furuncle (boil)** | รูขุมขนหนึ่งรู **ลงลึกถึงฐาน** เกิดโพรงหนอง | **fluctuant** | **กรีดระบาย** ± ยากิน |
| **Carbuncle** | **หลายรูขุมขนติดกันเป็นกลุ่ม** หลายโพรง | ก้อนใหญ่ หลายหัว มีหนอง | **กรีดระบาย + ยากิน** |

#### ทำไมถึงมีอาการนี้

| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ตุ่มอยู่กลางรูขุมขน** | เชื้อลงไปตามท่อของรูขุมขน การอักเสบจึงวางตัวรอบท่อนั้น | **ตุ่มเรียงตามรูขน = folliculitis** ไม่ใช่ผื่นกระจายทั่ว |
| **หัวขาวตรงยอด** | neutrophil รวมกันเป็นหนองใต้ชั้นผิวบาง ๆ | เป็น pustule ไม่ใช่ vesicle (ซึ่งเป็นน้ำใสของไวรัส) |
| **fluctuance ใน furuncle** | การอักเสบลงถึงฐานรูขุมขนและทำลายเนื้อเยื่อรอบ ๆ จนเกิดโพรงหนอง | **เริ่มคลำได้นุ่ม = ต้องกรีด** |
| **หลายหัวใน carbuncle** | รูขุมขนที่อยู่ติดกันเชื่อมโพรงหนองถึงกันใต้ผิว | จึงกรีดจุดเดียวไม่พอ ต้องเปิดให้ระบายทุกช่อง |
| **hot tub folliculitis** | *Pseudomonas* เจริญได้ในน้ำอุ่นที่คลอรีนต่ำ แล้วเข้าทางรูขุมขนที่เปิดจากความร้อน | **ประวัติแช่น้ำอุ่น/อ่างน้ำวน → คิด Pseudomonas** ไม่ใช่ S. aureus |

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **follicular papule / pustule** | ตุ่มหรือตุ่มหนองที่อยู่ตรงรูขุมขน | ลายเซ็นของ folliculitis |
| **furuncle / boil** | ฝีที่รูขุมขนเดียว | เริ่มมี fluctuance |
| **carbuncle** | กลุ่มฝีที่เชื่อมกันหลายรูขุมขน | ต้องระบายหลายช่อง |
| **hot tub folliculitis** | folliculitis จาก Pseudomonas หลังแช่น้ำอุ่น | เบาะแสจากประวัติ |
| **pustule vs vesicle** | ตุ่มหนอง vs ตุ่มน้ำใส | หนอง = แบคทีเรีย · น้ำใส = ไวรัส |
""",
    ["folliculitis → furuncle → carbuncle คือเรื่องเดียวกันที่ลึกและกว้างขึ้น",
     "เชื้อหลัก S. aureus · ประวัติแช่น้ำอุ่น = Pseudomonas (hot tub folliculitis)",
     "ตุ่มอยู่ตรงรูขุมขนคือสิ่งที่แยกจากผื่นอื่น",
     "มี fluctuance = เปลี่ยนจากยาทาเป็นกรีดระบาย",
     "carbuncle เชื่อมหลายโพรงใต้ผิว กรีดจุดเดียวไม่พอ",
     "pustule = แบคทีเรีย · vesicle น้ำใส = ไวรัส"],
    [mcq(N(12), "Three days after using a poorly chlorinated hot tub, a woman develops itchy follicular pustules on the trunk and thighs, sparing areas covered tightly by her swimsuit edges. Which organism is most likely?",
         ["Pseudomonas aeruginosa",
          "Staphylococcus aureus",
          "Streptococcus pyogenes",
          "Candida albicans",
          "Malassezia furfur"],
         0,
         "**ประวัติแช่อ่างน้ำอุ่นที่คลอรีนต่ำ + ตุ่มหนองตามรูขุมขน** = **hot tub folliculitis** จาก ***Pseudomonas aeruginosa*** ซึ่งสไลด์ระบุไว้เป็น uncommon organism ของ folliculitis · เชื้อนี้เจริญได้ดีในน้ำอุ่นที่ฆ่าเชื้อไม่พอ และความร้อนทำให้รูขุมขนเปิด เชื้อจึงเข้าได้ง่าย\n\nทำไมข้ออื่นผิด\n- ***S. aureus*** เป็นเชื้อที่พบบ่อยที่สุดของ folliculitis **โดยทั่วไป** แต่ไม่อธิบายความสัมพันธ์กับอ่างน้ำอุ่นและการกระจายตามบริเวณที่แช่น้ำ\n- ***S. pyogenes*** ก่อ erysipelas และ lymphangitis มากกว่า ไม่ใช่ folliculitis จากน้ำ\n- ***Candida*** ก่อผื่นในซอกพับที่อับชื้น ไม่ใช่รูปแบบหลังแช่น้ำอุ่น\n- ***Malassezia*** ก่อ **Malassezia folliculitis** ได้จริง แต่สัมพันธ์กับความมันและความอับของลำตัวในที่ร้อนชื้น ไม่ใช่เบาะแสอ่างน้ำวน",
         "แช่อ่างน้ำอุ่น + ตุ่มหนองตามรูขุมขน = Pseudomonas",
         "Folliculitis — hot tub", R("Folliculitis"), ["2.3.12", "2.1.50"]),
     mcq(N(13), "A furuncle on the thigh has become a 5 cm mass with several draining points. Which term and which management apply?",
         ["Carbuncle — drainage of all loculations plus oral antibiotics",
          "Carbuncle — topical mupirocin alone is sufficient",
          "Folliculitis — antibacterial wash and improved shaving technique",
          "Infective panniculitis — biopsy with special stains before any treatment",
          "Necrotizing fasciitis — immediate theatre for debridement"],
         0,
         "**หลายรูขุมขนเชื่อมกันเป็นก้อนใหญ่และมีหลายช่องระบาย** = **carbuncle** · เพราะหนองอยู่ใน**หลายโพรงที่เชื่อมกันใต้ผิว** การกรีดจุดเดียวจึงไม่พอ ต้อง**เปิดระบายให้ครบทุกช่อง** และเนื่องจากกว้างและมีอาการทั่วกายได้ จึง**ให้ยากินร่วม**\n\nทำไมข้ออื่นผิด\n- **ยาทาอย่างเดียว** ซึมไม่ถึงโพรงหนองหลายช่อง\n- **folliculitis** คือระยะตื้นที่ยังไม่มีโพรงหนอง ไม่ใช่ก้อน 5 ซม. ที่มีทางระบาย\n- **infective panniculitis** เป็นก้อนลึกที่ **ไม่ fluctuant** และดำเนินโรคเป็นสัปดาห์ ไม่ใช่ฝีที่ระบายหนองอยู่\n- **necrotizing fasciitis** ต้องมีปวดเกินกว่าที่ตาเห็น ผิวคล้ำ crepitus หรืออาการทรุด — การมีหลายหัวระบายหนองไม่ใช่ข้อบ่งชี้",
         "หลายหัว = carbuncle = ระบายทุกช่อง + ยากิน",
         "Carbuncle", R("Folliculitis — complications"), ["2.3.12", "2.3.12(2)"])],
    ["2.3.12", "2.1.50"], {"follicle": F.follicle()})

# ───────────────────────────── 7
NL_NF = ["2.2.50", "B5.2.2(1)"]
sec("derm-si-07", "Necrotizing fasciitis — โรคที่แพ้ที่เวลา ไม่ใช่ที่ยา",
    "ปวดเกินกว่าที่ตาเห็น · Type I vs II · ผ่าตัดคือการวินิจฉัย", 11,
"""- **นิยาม** การติดเชื้อของ **fascia และชั้นใต้ผิวหนัง** ที่**ลุกลามเร็วและคุกคามชีวิต** · **ต้องผ่าตัดด่วน**
- ✍️ อาจารย์เน้นกลุ่มเสี่ยง **เบาหวานและภาวะกดภูมิ**

### สาเหตุแบ่งสองแบบ

| | **Type I** | **Type II** |
|---|---|---|
| เชื้อ | **polymicrobial** — แบคทีเรียหลายชนิดร่วมกัน (รวม anaerobe) | ***Streptococcus pyogenes*** · **MRSA** |
| บริบทที่พบ | ผู้สูงอายุ เบาหวาน โรคเรื้อรัง หลังผ่าตัดช่องท้องหรือบริเวณก้นและอวัยวะเพศ | คนแข็งแรงก็เป็นได้ หลังบาดแผลเล็กน้อย |
| เบาะแส | มี **แก๊ส** ในเนื้อเยื่อได้มากกว่า (anaerobe) | ลุกลามเร็วมาก อาจมี **toxic shock** ร่วม |

[[fig:nf]]

### อาการ — เรียงตามลำดับที่มันปรากฏ
1. **ปวดรุนแรงเกินกว่าที่ตรวจพบ (severe pain out of proportion to physical signs)** ← **สัญญาณที่มาก่อนและสำคัญที่สุด**
2. **บวม แดง ผิวเปลี่ยนสี ลุกลามเร็ว**
3. **crepitus · ตุ่มน้ำและตุ่มเลือด (bullae) · เนื้อตาย**
4. **อาการทั่วกาย — ไข้ ความดันต่ำ สับสน**

### การวินิจฉัย
- **ความสงสัยทางคลินิกสำคัญที่สุด (clinical suspicion is critical)**
- **CT หรือ MRI** เห็นการอักเสบที่ชั้น fascia
- **การผ่าตัดสำรวจ (surgical exploration) คือสิ่งที่ยืนยันการวินิจฉัย**

### การรักษา
- **ผ่าตัดตัดเนื้อตายทันที (immediate surgical debridement)**
- **ยาฆ่าเชื้อกว้างทางหลอดเลือดดำ** เช่น **vancomycin + piperacillin-tazobactam**
- **ดูแลในหอผู้ป่วยวิกฤต**

### ภาวะแทรกซ้อนและการป้องกัน
- **septic shock · multi-organ failure · อัตราตายสูงถ้าไม่รักษา**
- ป้องกันด้วยการ**ดูแลแผลตั้งแต่ต้น คุมเบาหวาน และจัดการภาวะกดภูมิ**

#### ทำไมถึงมีอาการนี้

| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ปวดมากแต่ผิวยังดูไม่แย่** | เชื้อลุกลามไปตาม **fascia** ซึ่งอยู่ใต้ชั้นไขมันและมีเลือดไปเลี้ยงน้อย · เส้นประสาทถูกทำลายก่อนที่ผิวด้านบนจะเปลี่ยนแปลง | **ช่องว่างระหว่าง “ปวดมาก” กับ “ผิวดูเกือบปกติ” คือหน้าต่างทองที่ต้องจับให้ได้** |
| **ผิวคล้ำและตุ่มเลือด** | หลอดเลือดที่ทะลุจาก fascia ขึ้นมาเลี้ยงผิวถูกอุดตัน (thrombosis) ผิวจึงขาดเลือดตาย | เป็นสัญญาณ**ระยะหลัง** ถ้ารอให้เห็นจะสายแล้ว |
| **crepitus** | anaerobe สร้างแก๊สในเนื้อเยื่อ | พบใน **Type I** มากกว่า |
| **ชาบริเวณรอยโรค** | เส้นประสาทผิวหนังถูกทำลาย | ปวดมากแล้วกลับชา = แย่ลง ไม่ใช่ดีขึ้น |
| **ความดันต่ำและสับสนเร็ว** | exotoxin ของ *S. pyogenes* เป็น superantigen กระตุ้น cytokine มหาศาล | ภาพของ **Type II** ที่มี toxic shock |

> **กับดักที่ทำให้วินิจฉัยช้า** — รอผล CT ก่อนปรึกษาศัลยกรรม · เชื่อว่าผิวที่ยังดูดีแปลว่าไม่รุนแรง · ให้ยาแก้ปวดแล้วนัดดูอาการ · **ทั้งสามข้อทำให้เสียเวลาที่เป็นตัวตัดสินชีวิต**

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **pain out of proportion** | ปวดเกินกว่าสิ่งที่ตรวจพบ | สัญญาณไวที่สุด |
| **crepitus** | เสียงกรอบแกรบจากแก๊สใต้ผิว | Type I |
| **hemorrhagic bullae** | ตุ่มน้ำที่มีเลือด | สัญญาณระยะหลัง |
| **surgical exploration** | การผ่าตัดสำรวจ | เป็นการวินิจฉัยที่ยืนยัน |
| **debridement** | การตัดเนื้อตายออก | การรักษาหลัก ทำซ้ำได้ |
| **polymicrobial (Type I)** | หลายเชื้อร่วมกัน | กลุ่มเบาหวาน ผู้สูงอายุ |
| **monomicrobial (Type II)** | เชื้อเดียว — S. pyogenes หรือ MRSA | คนแข็งแรงก็เป็นได้ |
| **superantigen** | สารพิษกระตุ้นภูมิคุ้มกันรุนแรง | กลไกของ toxic shock |
""",
    ["ปวดเกินกว่าที่ตาเห็น = สัญญาณแรกและไวที่สุดของ necrotizing fasciitis",
     "Type I = polymicrobial (เบาหวาน ผู้สูงอายุ) · Type II = S. pyogenes หรือ MRSA",
     "crepitus และตุ่มเลือดเป็นสัญญาณระยะหลัง ถ้ารอให้ครบจะสาย",
     "การผ่าตัดสำรวจคือการวินิจฉัย ไม่ใช่ CT/MRI",
     "รักษา: debridement ทันที + vancomycin ร่วมกับ piperacillin-tazobactam + ICU",
     "ปวดมากแล้วกลับชา = เส้นประสาทถูกทำลาย แปลว่าแย่ลง"],
    [mcq(N(14), "A 58-year-old man with diabetes has 12 hours of rapidly worsening leg pain. He rates the pain 10/10, yet the overlying skin shows only mild erythema and slight swelling. He is febrile with a blood pressure of 92/54 mmHg. What is the most appropriate immediate action?",
         ["Urgent surgical consultation for operative exploration",
          "Contrast-enhanced CT of the leg before any referral",
          "Admit for intravenous cefazolin and reassess in the morning",
          "Mark the erythema margin and observe for six hours",
          "Doppler ultrasound to exclude deep vein thrombosis first"],
         0,
         "**ปวด 10/10 ที่ไม่สมดุลกับผิวที่ยังดูเกือบปกติ + ลุกลามเป็นชั่วโมง + ไข้และความดันต่ำ + เบาหวาน** = **necrotizing fasciitis** จนกว่าจะพิสูจน์เป็นอื่น · สไลด์ระบุว่า **clinical suspicion สำคัญที่สุด** และ **surgical exploration เป็นสิ่งที่ยืนยันการวินิจฉัย** จึงต้อง**ปรึกษาศัลยกรรมทันที** พร้อมให้ยา IV กว้างและกู้ชีพไปด้วย\n\nทำไมข้ออื่นผิดและอันตราย\n- **ส่ง CT ก่อนปรึกษา** ทำให้เสียเวลาในโรคที่วัดผลลัพธ์กันเป็นชั่วโมง · CT ช่วยยืนยันได้แต่**ห้ามให้การรอผลทำให้การผ่าตัดช้า**\n- **cefazolin แล้วรอเช้า** คลุมเชื้อไม่ครบ (ไม่คลุม MRSA และ anaerobe) และยาไม่สามารถแทนการตัดเนื้อตายได้\n- **ขีดขอบแล้วสังเกต 6 ชั่วโมง** เป็นวิธีของ cellulitis ที่คนไข้คงที่ ไม่ใช่ของคนที่ความดันตกและปวดผิดปกติ\n- **Doppler ก่อน** ทำให้ช้า และ DVT ไม่อธิบายไข้กับความดันต่ำ",
         "ปวดไม่สมดุลกับผิว + สัญญาณชีพแย่ = โทรหาศัลยกรรม อย่าโทรหาห้องเอกซเรย์",
         "Necrotizing fasciitis — immediate action", R("Necrotizing fasciitis"), NL_NF),
     mcq(N(15), "Which statement about the two types of necrotizing fasciitis is correct?",
         ["Type I is polymicrobial, whereas Type II is due to Streptococcus pyogenes or MRSA",
          "Type I is caused by Streptococcus pyogenes alone and Type II by anaerobes",
          "Type II occurs only in patients with diabetes or immunosuppression",
          "Type I is managed medically and Type II surgically",
          "Both types are confirmed by blood culture before surgery"],
         0,
         "สไลด์แบ่งไว้ตรงไปตรงมา — **Type I = polymicrobial** และ **Type II = *S. pyogenes* หรือ MRSA**\n\nทำไมข้ออื่นผิด\n- ข้อสองสลับกัน — *S. pyogenes* คือ **Type II** ไม่ใช่ Type I\n- **Type II เกิดในคนแข็งแรงได้** หลังบาดแผลเล็กน้อย จึงไม่จำกัดเฉพาะเบาหวานหรือกดภูมิ (กลุ่มนั้นเด่นใน Type I)\n- **ทั้งสองแบบต้องผ่าตัด** ไม่มีแบบที่รักษาด้วยยาเพียงอย่างเดียว\n- **ไม่รอผลเพาะเชื้อจากเลือดก่อนผ่าตัด** เพราะจะเสียเวลา · การวินิจฉัยยืนยันด้วย **surgical exploration**",
         "Type I polymicrobial · Type II strep หรือ MRSA · ทั้งคู่ต้องเข้าห้องผ่าตัด",
         "Necrotizing fasciitis — types", R("Necrotizing fasciitis — causes"), NL_NF)],
    NL_NF, {"nf": F.nf()})

# ───────────────────────────── 8
sec("derm-si-08", "Cutaneous anthrax — แผลดำที่ไม่เจ็บ",
    "painless papule → vesicle → black eschar + บวมมาก", 7,
"""- **เชื้อ** ***Bacillus anthracis*** — พบในผู้ที่**สัมผัสผลิตภัณฑ์จากสัตว์** (หนัง ขนสัตว์ เนื้อ) · **cutaneous เป็นรูปแบบที่พบบ่อยที่สุด**ของ anthrax
- **ลำดับของรอยโรค** **ตุ่มเล็กที่ไม่เจ็บ (painless papule)** → **vesicle** → **แผลเนื้อตายที่มีสะเก็ดดำ (necrotic ulcer with black eschar)**
- **ลักษณะร่วมที่เป็นลายเซ็น** **บวมรอบรอยโรคมากผิดส่วน (significant surrounding edema)** · มีไข้และอ่อนเพลียได้
- **การวินิจฉัย** ลักษณะทางคลินิก · **Gram stain และเพาะเชื้อจากรอยโรค** · **PCR และ immunohistochemistry** ในห้องปฏิบัติการอ้างอิง
- **การรักษา** **penicillin G** หรือ **fluoroquinolone ร่วมกับ rifampicin** · ให้ทางหลอดเลือดดำถ้ามีการลุกลามทั่วกาย
- **ภาวะแทรกซ้อน** **septicaemia และ meningitis**
- **การป้องกัน** เลี่ยงผลิตภัณฑ์สัตว์ที่ปนเปื้อน · **วัคซีน anthrax** ในกลุ่มเสี่ยงสูง

#### ทำไมถึงมีอาการนี้

| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ไม่เจ็บ** | **lethal toxin และ edema toxin** ของเชื้อกดการทำงานของเซลล์ภูมิคุ้มกันและรบกวนสัญญาณความเจ็บเฉพาะที่ | **แผลเนื้อตายที่ “ไม่เจ็บ” เป็นสิ่งที่ผิดปกติมาก** — ของแบคทีเรียทั่วไปจะเจ็บ |
| **สะเก็ดดำตรงกลาง** | toxin ทำให้หลอดเลือดเล็กตายและเลือดไม่ไปเลี้ยง เนื้อตรงกลางจึงตายเป็น eschar | ลายเซ็นที่ทำให้นึกถึง anthrax |
| **บวมมากผิดส่วน** | **edema toxin** กระตุ้น adenylate cyclase ทำให้น้ำรั่วออกนอกหลอดเลือดมาก | บวมเกินกว่าขนาดแผล = เบาะแสสำคัญ |
| **ลุกลามเป็น septicaemia** | เชื้อมี capsule ต้าน phagocytosis จึงเข้ากระแสเลือดได้ | เหตุผลที่ต้องให้ยาทางหลอดเลือดดำเมื่อมีอาการทั่วกาย |

> **DDx ของแผลที่มีสะเก็ดดำ** — **ecthyma gangrenosum** (*Pseudomonas* ในผู้ป่วย neutropenia) · **แผลกัดของแมงมุมบางชนิด** · **mucormycosis** ในผู้ป่วยเบาหวานคุมไม่ได้ · **แผลเนื้อตายจากหลอดเลือดอุดตัน** · ตัวช่วยแยกคือ **ประวัติสัมผัสสัตว์ + ไม่เจ็บ + บวมมาก**

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **eschar** | สะเก็ดแผลเนื้อตายสีดำ | ลายเซ็นของ cutaneous anthrax |
| **painless ulcer** | แผลที่ไม่เจ็บ | ผิดปกติสำหรับแบคทีเรียทั่วไป |
| **edema toxin / lethal toxin** | สารพิษสองตัวของ B. anthracis | อธิบายทั้งอาการบวมและไม่เจ็บ |
| **zoonosis** | โรคติดต่อจากสัตว์สู่คน | หมวดของ anthrax (นล. กลุ่ม 3) |
| **immunohistochemistry** | การย้อมด้วยแอนติบอดีจำเพาะ | การตรวจยืนยันใน reference lab |
""",
    ["cutaneous anthrax: ตุ่มไม่เจ็บ → vesicle → แผลสะเก็ดดำ + บวมมากผิดส่วน",
     "เบาะแสคือประวัติสัมผัสผลิตภัณฑ์จากสัตว์",
     "แผลเนื้อตายที่ไม่เจ็บเป็นสิ่งผิดปกติ ต้องนึกถึง anthrax",
     "edema toxin อธิบายอาการบวม · lethal toxin อธิบายการไม่เจ็บและเนื้อตาย",
     "รักษาด้วย penicillin G หรือ fluoroquinolone + rifampicin",
     "ภาวะแทรกซ้อน: septicaemia และ meningitis"],
    [mcq(N(16), "A man who works in a tannery has a 1 cm ulcer with a black central eschar on the forearm, surrounded by marked oedema. Strikingly, the lesion is not painful. Which organism is most likely?",
         ["Bacillus anthracis",
          "Staphylococcus aureus",
          "Pseudomonas aeruginosa",
          "Streptococcus pyogenes",
          "Mycobacterium marinum"],
         0,
         "**อาชีพสัมผัสหนังสัตว์ + แผลสะเก็ดดำ + บวมมากผิดส่วน + ไม่เจ็บ** = **cutaneous anthrax** จาก ***Bacillus anthracis*** · จุดที่ชี้ชัดที่สุดคือ **ไม่เจ็บ** ซึ่งอธิบายด้วย **lethal toxin** ที่กดการทำงานของเซลล์ภูมิคุ้มกันในบริเวณนั้น และ **บวมมาก** จาก **edema toxin**\n\nทำไมข้ออื่นผิด\n- ***S. aureus*** ก่อฝีและ furuncle ที่ **เจ็บมาก** และไม่ให้ eschar ดำพร้อมบวมผิดส่วน\n- ***Pseudomonas*** ก่อ **ecthyma gangrenosum** ที่มีสะเก็ดดำได้จริง แต่เกิดใน **ผู้ป่วย neutropenia** ไม่ใช่คนทำงานโรงหนังที่สุขภาพดี และมักเจ็บ\n- ***S. pyogenes*** ก่อ erysipelas และ necrotizing fasciitis ซึ่ง**เจ็บเด่น**\n- ***M. marinum*** สัมพันธ์กับ**การสัมผัสน้ำ** ให้ nodule เรื้อรังที่มือ ไม่ใช่ eschar ดำที่บวมมาก",
         "แผลสะเก็ดดำที่ไม่เจ็บ + บวมมาก + สัมผัสสัตว์ = anthrax",
         "Cutaneous anthrax", R("Cutaneous anthrax"), ["2.3.1-3(9)"])],
    ["2.3.1-3(9)"])

# ───────────────────────────── 9
sec("derm-si-09", "Pitted keratolysis และ Corynebacterium — เท้าเหม็น ซอกพับ และ Wood lamp",
    "หลุมที่ฝ่าเท้า · erythrasma coral-red · trichomycosis ที่เส้นขน", 9,
"""### Pitted keratolysis
- **ชื่ออื่น** keratoma plantare sulcatum
- **เชื้อ** ***Micrococcus sedentarius*** — **gram-positive**
- **กลุ่มที่พบ** **ผู้ชายวัยผู้ใหญ่ที่เท้าเหงื่อออกมาก**
- **อาการ** **เท้ามีกลิ่นเหม็น** · **หลุมเล็ก ๆ คล้ายปากแอ่ง (crater-like depressions) ในชั้น stratum corneum** บริเวณ**ฝ่าเท้าส่วนที่รับน้ำหนัก** · **ไม่มีผื่นแดงหรือการอักเสบ**
- **การรักษา** **ทำให้เท้าแห้ง** · รักษาเหงื่อออกมากด้วย **aluminium chloride 20% solution** · **benzoyl peroxide (wash หรือ 5% gel)** · **clindamycin solution** · **erythromycin solution**

### Erythrasma
- **เชื้อ** ***Corynebacterium minutissimum*** — short gram-positive rod ที่มี **subterminal granules**
- **ตำแหน่ง**
  - **ซอกนิ้วเท้า (พบบ่อยที่สุด โดยเฉพาะนิ้วที่ 4–5)** — ปื้นขาวเปียกยุ่ยหนา (hyperkeratotic white macerated plaque)
  - **บริเวณซอกพับ (intertriginous area)** — **ปื้นสีน้ำตาลแดงขอบชัดมีสะเก็ดละเอียด**
- **Wood lamp** — **เรืองแสงสีแดงปนส้ม (coral-red fluorescence)** จาก **coproporphyrin III** ← **จุดที่ออกสอบ**
- **การรักษา** เฉพาะที่: **BP wash 5% gel · clindamycin solution 2% · azole cream** · กระจายกว้าง: **erythromycin กิน 1 กรัม** หรือ **clarithromycin ครั้งเดียว** · ป้องกันการเป็นซ้ำด้วย **BP bar**

[[fig:wood]]

### Trichomycosis axillaris และ pubis
- **เชื้อ** ***Corynebacterium*** — ติดเชื้อที่ **เส้นขน (hair shaft)** ไม่ใช่ที่ผิวหนัง
- **อาการ** **ปุ่มหนาเกาะบนเส้นขน** ที่**รักแร้และหัวหน่าว** · เชื้อสร้างเม็ดสีได้หลายสี **น้ำตาลอ่อน แดง เหลือง ดำ** · **ไม่มีอาการแต่มีกลิ่น**
- **DDx** **pediculosis (เหา) · white piedra · black piedra**
- **การตรวจ** **Gram stain ของปุ่มที่ขูดออกมา** → เห็น **coryneform morphology**
- **การรักษา** **โกนขน** · **BP wash หรือ gel**

#### ทำไมถึงมีอาการนี้

| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **หลุมที่ฝ่าเท้าโดยไม่อักเสบ** | เชื้อสร้าง **protease** ย่อย keratin ของ stratum corneum เฉพาะจุด โดยไม่ลงลึกถึงชั้นที่มีหลอดเลือด | **ไม่แดง ไม่เจ็บ แต่เป็นหลุม** = pitted keratolysis ไม่ใช่เชื้อราหรือหูด |
| **เท้าเหม็น** | แบคทีเรียย่อย keratin แล้วปล่อย **sulphur compound** | กลิ่นเป็นอาการนำที่คนไข้มาหาหมอ |
| **coral-red ใต้ Wood lamp** | **coproporphyrin III** ที่เชื้อสร้างเป็น fluorophore เปล่งแสงเมื่อรับ UV ~365 nm | **แยก erythrasma จากเชื้อราในซอกพับ** ซึ่งหน้าตาเหมือนกันมาก |
| **ปุ่มบนเส้นขนไม่ใช่ที่ผิว** | เชื้อเกาะและสร้าง matrix หุ้มรอบ hair shaft | ถ้ารอยโรคอยู่**บนเส้นขน** ไม่ใช่ที่รูขุมขน → ไม่ใช่ folliculitis |
| **หลายสีของปุ่ม** | เชื้อแต่ละสายพันธุ์สร้างเม็ดสีต่างกัน | ช่วยแยกจาก white/black piedra ที่เป็นเชื้อรา |

> **ความสำคัญเชิงการรักษา** — ทั้งสามโรคนี้เป็น **แบคทีเรีย** ที่หน้าตาเหมือนเชื้อรา ถ้าวินิจฉัยผิดแล้วให้**ยาฆ่าเชื้อรา จะไม่หาย** · **Wood lamp และ Gram stain จึงเปลี่ยนการรักษาได้จริง**

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **stratum corneum** | ชั้นขี้ไคลนอกสุด | ชั้นที่ถูกย่อยเป็นหลุม |
| **crater-like depression / pit** | หลุมเล็กคล้ายปากแอ่ง | ลายเซ็นของ pitted keratolysis |
| **hyperhidrosis** | ภาวะเหงื่อออกมาก | ปัจจัยที่ต้องรักษาร่วม |
| **intertriginous area** | บริเวณซอกพับ | ตำแหน่งของ erythrasma |
| **coral-red fluorescence** | เรืองแสงสีแดงปนส้ม | Wood lamp ของ erythrasma |
| **coproporphyrin III** | สารเรืองแสงที่เชื้อสร้าง | กลไกของ coral-red |
| **Wood lamp** | ไฟ UV ~365 nm สำหรับส่องผิวหนัง | เครื่องมือข้างเตียง |
| **hair shaft** | ก้านเส้นขน | ตำแหน่งของ trichomycosis |
| **coryneform** | รูปร่างแบบ Corynebacterium | ผล Gram stain |
| **piedra** | โรคเชื้อราที่เกาะเส้นขน | DDx ของ trichomycosis |
""",
    ["pitted keratolysis: Micrococcus sedentarius · เท้าเหงื่อมาก · หลุมที่ฝ่าเท้าโดยไม่อักเสบ",
     "erythrasma: Corynebacterium minutissimum · ซอกนิ้วเท้า 4–5 และซอกพับ",
     "Wood lamp coral-red = coproporphyrin III = erythrasma (ไม่ใช่เชื้อรา)",
     "erythrasma กระจายกว้าง: erythromycin 1 กรัม หรือ clarithromycin ครั้งเดียว",
     "trichomycosis เกาะที่เส้นขน ไม่ใช่รูขุมขน → DDx เหา white/black piedra",
     "สามโรคนี้เป็นแบคทีเรีย ให้ยาฆ่าเชื้อราจะไม่หาย"],
    [mcq(N(17), "A 34-year-old man has well-defined reddish-brown patches with fine scale in both groins. Under a Wood lamp the patches fluoresce coral-red. Which treatment is appropriate?",
         ["Topical clindamycin solution or oral erythromycin if widespread",
          "Topical terbinafine cream twice daily for four weeks",
          "Oral griseofulvin for six weeks",
          "Topical high-potency corticosteroid",
          "Oral acyclovir for seven days"],
         0,
         "**coral-red fluorescence** ใต้ Wood lamp = **erythrasma** จาก ***Corynebacterium minutissimum*** ซึ่งเป็น **แบคทีเรีย** · การรักษาตามสไลด์คือ **clindamycin solution 2%, benzoyl peroxide, azole cream** เฉพาะที่ หรือ **erythromycin กิน 1 กรัม / clarithromycin ครั้งเดียว** เมื่อกระจายกว้าง · การเรืองแสงเกิดจาก **coproporphyrin III** ที่เชื้อสร้าง\n\nทำไมข้ออื่นผิด\n- **terbinafine** และ **griseofulvin** เป็น**ยาฆ่าเชื้อรา** ซึ่งไม่ออกฤทธิ์กับ Corynebacterium · นี่คือกับดักหลักของโจทย์ เพราะผื่นในซอกพับหน้าตาเหมือน tinea cruris มาก และ **Wood lamp คือสิ่งที่แยกออก**\n- **สเตียรอยด์แรงสูง** กดภูมิเฉพาะที่และทำให้การติดเชื้อแย่ลง\n- **acyclovir** ใช้กับไวรัสเริม ไม่เกี่ยวกับรอยโรคนี้",
         "ซอกพับ + coral-red = แบคทีเรีย ให้ยาต้านแบคทีเรีย อย่าให้ยาฆ่าเชื้อรา",
         "Erythrasma — Wood lamp", R("Erythrasma"), ["2.3.12", "2.1.50"]),
     mcq(N(18), "A man complains of malodorous feet. On the weight-bearing areas of both soles there are multiple small crater-like depressions in the stratum corneum, with no erythema or scaling between the toes. Which organism and which first measure?",
         ["Micrococcus sedentarius — keep the feet dry and treat hyperhidrosis",
          "Trichophyton rubrum — topical terbinafine",
          "Candida albicans — topical nystatin",
          "Corynebacterium minutissimum — oral erythromycin",
          "Staphylococcus aureus — oral dicloxacillin"],
         0,
         "**เท้าเหม็น + หลุมเล็กในชั้น stratum corneum บริเวณรับน้ำหนัก + ไม่มีการอักเสบ** = **pitted keratolysis** จาก ***Micrococcus sedentarius*** · มาตรการแรกตามสไลด์คือ **ทำให้เท้าแห้งและรักษาเหงื่อออกมาก** ด้วย **aluminium chloride 20%** ร่วมกับ benzoyl peroxide หรือ clindamycin/erythromycin solution เพราะความชื้นคือเงื่อนไขที่ทำให้เชื้อย่อย keratin ได้\n\nทำไมข้ออื่นผิด\n- ***Trichophyton rubrum*** ก่อ **tinea pedis** ซึ่งมี**สะเก็ดและผื่นแดง โดยเฉพาะซอกนิ้ว** — โจทย์บอกชัดว่าไม่มี\n- ***Candida*** ก่อผื่นแดงเปียกในซอกพับ ไม่ใช่หลุมบนฝ่าเท้าที่ไม่อักเสบ\n- ***C. minutissimum*** ก่อ **erythrasma** ซึ่งให้**ปื้นน้ำตาลแดงและ coral-red ใต้ Wood lamp** ไม่ใช่หลุม\n- ***S. aureus*** ก่อ folliculitis และฝีที่เจ็บ ไม่ใช่รอยโรคไม่อักเสบแบบนี้",
         "หลุมที่ฝ่าเท้า + เหม็น + ไม่อักเสบ = pitted keratolysis → ทำให้แห้งก่อน",
         "Pitted keratolysis", R("Pitted keratolysis"), ["2.3.12", "2.1.50"])],
    ["2.3.12", "2.1.50"], {"wood": F.wood()})

# ───────────────────────────── 10
sec("derm-si-10", "แปลคำบรรยายรอยโรคให้เป็นชื่อโรค",
    "ตารางสรุปของสไลด์ · ฝึกอ่านโจทย์ที่ให้มาเป็นคำศัพท์", 8,
"""สไลด์ปิดหมวดแบคทีเรียด้วยตารางนี้ ซึ่งเป็น**เครื่องมือทำข้อสอบโดยตรง** เพราะโจทย์มักให้มาเป็น**คำบรรยายรอยโรค** แล้วให้เลือกชื่อโรค

| Condition | Morphology (skin lesion terms) | Key features |
|---|---|---|
| **Impetigo** | **erosions · crusts · bullae** | **superficial · non-scarring** |
| **Ecthyma** | **ulcer with thick crust** | impetigo ที่ลึกกว่า · **อาจเป็นแผลเป็น** |
| **Folliculitis** | **follicular papules and pustules** | **อยู่กลางรูขุมขน** |
| **Erysipelas** | **raised, well-demarcated erythematous plaques** | กินท่อน้ำเหลือง · มีอาการทั่วกาย |
| **Cellulitis** | **diffuse, erythematous, edematous plaques** | **ขอบไม่ชัด** · ลงถึง deep dermis |
| **Necrotizing fasciitis** | **hemorrhagic bullae · necrosis · crepitus** | **ภาวะฉุกเฉินทางศัลยกรรม** · ลุกลามเร็ว |

### คำศัพท์บรรยายรอยโรคที่ต้องแปลให้ออก
เป็นภาษาที่ใช้ทั้งในข้อสอบและใบ consult

| คำ | ความหมาย | ความลึกที่สื่อ |
|---|---|---|
| **Macule** | จุดสีที่**ไม่นูน** ขนาดเล็ก | อยู่ในชั้นผิว ไม่มีการบวม |
| **Patch** | เหมือน macule แต่**ใหญ่กว่า** | เช่น erythrasma |
| **Papule** | ตุ่มนูนเล็ก (< 1 ซม.) | ผิวหรือ dermis ตื้น |
| **Plaque** | **ปื้นนูนแบนกว้าง** | dermis — เช่น erysipelas, cellulitis |
| **Nodule** | **ก้อนลึก** คลำได้ในเนื้อ | dermis ลึกหรือชั้นไขมัน — เช่น panniculitis |
| **Vesicle** | ตุ่ม**น้ำใส** < 0.5 ซม. | แยกชั้นใน epidermis — ไวรัส |
| **Bulla** | ตุ่มน้ำ**ใหญ่** > 0.5 ซม. | bullous impetigo, NF ระยะหลัง |
| **Pustule** | ตุ่มที่มี**หนอง** | แบคทีเรีย |
| **Erosion** | ผิวหลุด**แค่ epidermis** | **ไม่เป็นแผลเป็น** |
| **Ulcer** | ผิวหลุด**ถึง dermis หรือลึกกว่า** | **เป็นแผลเป็น** |
| **Crust** | สะเก็ดจากน้ำเหลือง เลือด หรือหนองที่แห้ง | honey-coloured = impetigo |
| **Eschar** | สะเก็ด**เนื้อตายสีดำ** | anthrax, เนื้อตายจากขาดเลือด |
| **Induration** | เนื้อ**แข็ง**ขึ้นเมื่อคลำ | เรื้อรัง — เชื้อรา, mycobacteria |
| **Fluctuance** | กด**ยวบ**เพราะมีของเหลวในโพรง | abscess → กรีด |
| **Crepitus** | กรอบแกรบจาก**แก๊ส** | necrotizing infection |

#### วิธีใช้ตารางนี้ทำข้อสอบ
ไล่สามขั้นเสมอ

1. **คำบรรยายบอกความลึกอะไร** — erosion = ตื้น · ulcer = ลึก · nodule = ชั้นไขมัน
2. **ขอบเป็นอย่างไร** — well-demarcated/raised = erysipelas · diffuse/ill-defined = cellulitis
3. **มีคำที่เป็นสัญญาณฉุกเฉินไหม** — **hemorrhagic bullae · necrosis · crepitus · pain out of proportion** → ตอบ **necrotizing fasciitis** และตอบว่าต้องผ่าตัด

> **กับดักที่พบบ่อยในข้อสอบ** — คำว่า **“bullae”** ปรากฏทั้งใน **bullous impetigo** (ตุ่มน้ำใส ไม่เจ็บ เด็ก ตื้น) และใน **necrotizing fasciitis** (**ตุ่มมีเลือด** ปวดรุนแรง ผิวคล้ำ) · **คำเดียวกันแต่บริบทต่างกันสุดขั้ว** ให้อ่านคำขยายข้างหน้าเสมอ
""",
    ["โจทย์ให้คำบรรยายรอยโรค → แปลเป็นความลึก → แปลเป็นชื่อโรค",
     "erosion = ตื้น ไม่เป็นแผลเป็น · ulcer = ลึก เป็นแผลเป็น",
     "well-demarcated raised plaque = erysipelas · diffuse ill-defined = cellulitis",
     "hemorrhagic bullae + necrosis + crepitus = necrotizing fasciitis",
     "คำว่า bullae อยู่ได้ทั้งใน bullous impetigo และ NF — ดูคำขยายและบริบท"],
    [mcq(N(19), "An examination question describes: “diffuse erythematous oedematous plaques with ill-defined borders on the left shin, warm and tender, with fever.” Which diagnosis do these morphology terms point to?",
         ["Cellulitis",
          "Erysipelas",
          "Impetigo",
          "Ecthyma",
          "Folliculitis"],
         0,
         "คำสำคัญคือ **diffuse · oedematous plaques · ill-defined borders** ซึ่งตารางของสไลด์จับคู่กับ **cellulitis** โดยตรง เพราะรอยโรคอยู่ใน **deep dermis ถึงชั้นไขมัน** ที่ไม่มีผนังกั้น ขอบจึงเบลอ\n\nทำไมข้ออื่นผิด — แต่ละข้อมีคำบรรยายของตัวเองในตารางเดียวกัน\n- **erysipelas** = **raised, well-demarcated** plaques ซึ่งตรงข้ามกับ ill-defined\n- **impetigo** = **erosions, crusts, bullae** ตื้น ๆ ไม่ใช่ plaque บวมทั้งแผ่น\n- **ecthyma** = **ulcer with thick crust**\n- **folliculitis** = **follicular papules and pustules** ที่อยู่ตรงรูขุมขน",
         "ill-defined + oedematous plaque = cellulitis แทบทุกครั้ง",
         "Morphology → diagnosis", R("Summary table"), NL_SKIN),
     mcq(N(20), "Which description should make you think of a surgical emergency rather than a simple skin infection?",
         ["Hemorrhagic bullae with skin necrosis and crepitus",
          "Honey-coloured crusts around the nose and mouth",
          "Follicular pustules on the thighs after shaving",
          "A well-demarcated raised erythematous plaque on the cheek",
          "Reddish-brown patches with fine scale in the groin"],
         0,
         "**hemorrhagic bullae + necrosis + crepitus** เป็นชุดคำที่ตารางสไลด์จับคู่กับ **necrotizing fasciitis** และกำกับว่าเป็น **surgical emergency** · กลไกคือหลอดเลือดที่เลี้ยงผิวถูกอุดตันทำให้ผิวตาย และ anaerobe สร้างแก๊สในเนื้อเยื่อ\n\nทำไมข้ออื่นไม่ใช่ภาวะฉุกเฉินทางศัลยกรรม\n- **honey-coloured crust** = impetigo ตื้น ๆ รักษาด้วยยาทา\n- **follicular pustules หลังโกนขน** = folliculitis\n- **well-demarcated raised plaque ที่แก้ม** = erysipelas ให้ penicillin\n- **ปื้นน้ำตาลแดงมีสะเก็ดละเอียดที่ขาหนีบ** = erythrasma ให้ยาต้านแบคทีเรียเฉพาะที่",
         "เห็นคำว่า necrosis หรือ crepitus = หยุดคิดเรื่องยาแล้วโทรหาศัลยกรรม",
         "Red-flag morphology", R("Summary table"), NL_NF)],
    NL_SKIN)

# ───────────────────────────── 11
NL_WART = ["2.3.12(15)", "B4.2.2(8)"]
sec("derm-si-11", "HPV และหูด — จำเลข type คู่กับตำแหน่ง",
    "ชนิดของหูด · koilocytosis · บันไดการรักษา", 11,
"""- **ไวรัส** **HPV** เป็น **double-stranded DNA virus** วงศ์ **Papillomaviridae** · มีมากกว่า **200 types**
  - **cutaneous types** (HPV 1, 2, 3, 4, 10) → หูดที่ผิวหนัง
  - **mucosal types** (HPV 6, 11, 16, 18) → หูดอวัยวะเพศและมะเร็ง
- **การติดต่อ** สัมผัสผิวโดยตรง · **autoinoculation (แพร่จากที่หนึ่งไปอีกที่ในตัวเอง)** · fomites
- **พยาธิกำเนิด** เป้าหมายคือ **basal keratinocyte** ผ่านรอยถลอกเล็ก ๆ → ไวรัสกระตุ้น **การแบ่งตัวของเซลล์และชะลอ apoptosis** → เกิดหูด · **แฝงตัวได้เป็นเดือนถึงปี**

[[fig:warts]]

### การวินิจฉัย
- **clinical** จากรูปร่างและตำแหน่ง
- **dermatoscopy** — **“red dots”** และ **“mosaic pattern”** ใน plantar wart
- **biopsy** เมื่อรูปร่างผิดแผก ดื้อการรักษา หรือต้องตัดมะเร็งออกไป
- **Histopathology** — **koilocytosis เป็น hallmark** · **hypergranulosis** · **papillomatosis**
- **PCR / DNA hybridization** ระบุ type (ใช้ในงานวิจัยและงานมะเร็งเป็นหลัก)

### การรักษา

| Category | Methods | Notes |
|---|---|---|
| **Physical destruction** | **cryotherapy · electrosurgery · curettage** | **ใช้บ่อยที่สุด ประสิทธิภาพสูง** |
| **Chemical agents** | **salicylic acid · trichloroacetic acid · podophyllin** | **first-line ของ common และ plantar wart** |
| **Immunotherapy** | **imiquimod · Candida antigen · MMR · PPD · intralesional interferon** | สำหรับรายดื้อหรือหลายตำแหน่ง |
| **Laser** | **CO₂ · pulsed dye laser** | หูดที่ดื้อ |
| **Systemic (ใช้น้อย)** | cimetidine · zinc · retinoids | ผลไม่แน่นอน |

### ข้อพิจารณาพิเศษ
- **เด็ก** หูดมัก**หายเองได้** → **สังเกตอาการได้ถ้าไม่มีอาการรบกวน**
- **ผู้ป่วยกดภูมิ** ดื้อการรักษาและเป็นซ้ำสูง
- **ผู้ป่วย epidermodysplasia verruciformis** ต้อง**กันแดดและคัดกรองมะเร็งเป็นประจำ**
- **สอนผู้ป่วย** อย่าแกะ (ป้องกัน autoinoculation) · ใส่รองเท้าในพื้นที่ส่วนรวม

#### ทำไมถึงมีอาการนี้

| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **จุดดำเล็ก ๆ ในหูด (black puncta)** | **หลอดเลือดฝอยที่ขึ้นมาเลี้ยงหูดเกิดลิ่มเลือดอุดตัน** จึงเห็นเป็นจุดดำ | **เป็นตัวแยกหูดจากตาปลา (callus)** ซึ่งไม่มีจุดดำ |
| **plantar wart เจ็บเวลาเดิน** | หูดถูกแรงกดจากน้ำหนักตัวดันลงไปกดปลายประสาทใน dermis | ตาปลาเจ็บเมื่อกดตรง ๆ แต่หูดเจ็บเมื่อ**บีบด้านข้าง** |
| **mosaic pattern** | หูดหลายอันโตมาเชื่อมกันเป็นแผ่น | ลายเซ็นของ plantar wart |
| **koilocyte** | ไวรัสทำให้เกิด **perinuclear halo** รอบนิวเคลียสของ keratinocyte | **hallmark ทางพยาธิของ HPV ทุกชนิด** |
| **EV เสี่ยงมะเร็ง** | HPV 5 และ 8 ใน EV รวมกับ **แสง UV** ก่อการกลายพันธุ์สะสม | จึงต้องกันแดดและคัดกรอง **SCC** |

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **verruca vulgaris / plana / plantaris** | หูดธรรมดา / แบน / ฝ่าเท้า | HPV 2,4 / 3,10 / 1 |
| **filiform wart** | หูดเป็นติ่งยื่น | ใบหน้า คอ เปลือกตา |
| **butcher's wart** | หูดจากอาชีพสัมผัสเนื้อสัตว์ | HPV 7 |
| **epidermodysplasia verruciformis** | โรคพันธุกรรมที่ไวต่อ HPV 5, 8 | เสี่ยง SCC |
| **autoinoculation** | แพร่เชื้อไปตำแหน่งอื่นในตัวเอง | เหตุผลที่ห้ามแกะ |
| **koilocytosis** | เซลล์มีวงใสรอบนิวเคลียส | hallmark ทางพยาธิ |
| **hypergranulosis** | ชั้น granular หนาขึ้น | พบร่วมใน histology |
| **papillomatosis** | ผิวยื่นเป็นตุ่มหนามคล้ายนิ้วมือ | พบร่วมใน histology |
| **black puncta** | จุดดำจากหลอดเลือดอุดตัน | แยกหูดจากตาปลา |
| **mosaic pattern** | ลายโมเสกจากหูดเชื่อมกัน | plantar wart |
| **cryotherapy** | จี้ด้วยความเย็น | physical destruction |
""",
    ["cutaneous HPV 1,2,3,4,10 · mucosal HPV 6,11,16,18",
     "plantar = HPV 1 · common = HPV 2,4 · flat = HPV 3,10 · butcher's = HPV 7 · EV = HPV 5,8",
     "koilocytosis คือ hallmark ทางพยาธิ (+ hypergranulosis, papillomatosis)",
     "black puncta = หลอดเลือดอุดตัน ใช้แยกหูดจากตาปลา",
     "first-line ของ common/plantar wart คือ salicylic acid · ที่ใช้บ่อยสุดคือ cryotherapy",
     "เด็กหายเองได้ · EV ต้องกันแดดและคัดกรอง SCC"],
    [mcq(N(21), "A 10-year-old has a painful keratotic lesion on the sole that hurts more when squeezed from the sides than when pressed directly, and shows tiny black dots on paring. Which HPV type is most characteristic, and what do the black dots represent?",
         ["HPV 1 — thrombosed capillaries",
          "HPV 3 — melanin deposition",
          "HPV 7 — inflammatory infiltrate",
          "HPV 16 — koilocytes seen macroscopically",
          "HPV 11 — foreign-body granuloma"],
         0,
         "**หูดที่ฝ่าเท้า (verruca plantaris) สัมพันธ์กับ HPV 1** ตามสไลด์ · **จุดดำเล็ก ๆ คือ thrombosed capillaries** — หลอดเลือดฝอยที่ขึ้นมาเลี้ยงหูดเกิดลิ่มเลือดอุดตัน · และ**การเจ็บเมื่อบีบด้านข้างมากกว่ากดตรง ๆ** ช่วยแยกหูดจาก **callus (ตาปลา)** ซึ่งไม่มีจุดดำและเจ็บเมื่อกดตรง\n\nทำไมข้ออื่นผิด\n- **HPV 3** คือ **flat wart** ที่ใบหน้าและหลังมือ · จุดดำไม่ใช่เมลานิน\n- **HPV 7** คือ **butcher's wart** จากอาชีพสัมผัสเนื้อสัตว์\n- **HPV 16** เป็น mucosal type ที่สัมพันธ์กับมะเร็ง · **koilocyte มองด้วยตาเปล่าไม่ได้** ต้องดูด้วยกล้องจุลทรรศน์\n- **HPV 11** เป็น mucosal type ของหูดอวัยวะเพศ และจุดดำไม่ใช่ granuloma",
         "ฝ่าเท้า = HPV 1 · จุดดำ = หลอดเลือดอุดตัน ไม่ใช่เมลานิน",
         "Plantar wart — HPV type", R("Human papilloma virus"), NL_WART),
     mcq(N(22), "Which histopathological finding is the hallmark of HPV infection?",
         ["Koilocytosis", "Multinucleated giant cells", "Acantholysis with tombstoning",
          "Caseating granulomas", "Subepidermal blister with eosinophils"],
         0,
         "**koilocytosis** — keratinocyte ที่มี **วงใสรอบนิวเคลียส (perinuclear halo)** เป็น **hallmark ของ HPV** · มักพบร่วมกับ **hypergranulosis** และ **papillomatosis**\n\nทำไมข้ออื่นผิด — แต่ละข้อเป็น hallmark ของโรคอื่นที่ควรแยกให้ออก\n- **multinucleated giant cells** คือสิ่งที่เห็นใน **Tzanck smear ของ HSV และ VZV**\n- **acantholysis with tombstoning** คือภาพของ **pemphigus vulgaris**\n- **caseating granuloma** คือภาพของ **วัณโรค**\n- **subepidermal blister with eosinophils** คือภาพของ **bullous pemphigoid**",
         "koilocyte = HPV · multinucleated giant cell = herpes · อย่าสลับกัน",
         "HPV — histopathology", R("Human papilloma virus — histopathology"), NL_WART),
     mcq(N(23), "A healthy 9-year-old has two small common warts on a finger that do not bother him. His mother asks whether treatment is necessary. What does the lecture support?",
         ["Observation is reasonable because warts in children are often self-limiting",
          "Immediate cryotherapy to prevent malignant transformation",
          "Oral retinoids to shorten the course",
          "Screening for immunodeficiency before any treatment",
          "Topical high-potency corticosteroid to reduce inflammation"],
         0,
         "สไลด์ระบุไว้ตรง ๆ ว่าใน **เด็ก หูดมักหายเองได้ (self-limiting) จึงสังเกตอาการได้ถ้าไม่มีอาการรบกวน** · เหตุผลคือภูมิคุ้มกันระดับเซลล์กำจัดไวรัสได้เองเมื่อเวลาผ่านไป\n\nทำไมข้ออื่นผิด\n- **การกลายเป็นมะเร็ง** ไม่ใช่ความเสี่ยงของ common wart ในเด็กปกติ · ความเสี่ยง SCC สงวนไว้สำหรับ **epidermodysplasia verruciformis (HPV 5, 8)**\n- **retinoids กิน** สไลด์จัดอยู่ในกลุ่ม systemic ที่ **ใช้น้อยและผลไม่แน่นอน** ไม่ใช่ทางเลือกแรกในเด็กที่ไม่มีอาการ\n- **คัดกรองภูมิคุ้มกันบกพร่อง** ทำเมื่อหูด**มากผิดปกติ ดื้อ หรือเป็นซ้ำรุนแรง** ไม่ใช่สองตุ่มในเด็กแข็งแรง\n- **สเตียรอยด์แรงสูง** ไม่ใช่การรักษาหูด และกดภูมิเฉพาะที่จะยิ่งแย่",
         "เด็ก หูดไม่กวน = สังเกตอาการได้ ไม่ต้องรีบจี้",
         "Warts — treatment considerations", R("Human papilloma virus — treatment considerations"), NL_WART)],
    NL_WART, {"warts": F.warts()})

# ───────────────────────────── 12
NL_HSV = ["2.3.1(8)", "B4.2.2(5)"]
sec("derm-si-12", "HHV ทั้งแปดชนิด และ HSV-1/HSV-2",
    "variant ที่ต้องจำ · ขนาดยา · พิษของ acyclovir", 12,
"""### Human herpesviruses — ต้องจำให้ได้ทั้งแปด

| | ไวรัส | สิ่งที่ก่อ |
|---|---|---|
| **HHV-1** | **HSV-1** | herpes labialis · whitlow · gladiatorum · eczema herpeticum |
| **HHV-2** | **HSV-2** | genital herpes |
| **HHV-3** | **VZV** | varicella · herpes zoster |
| **HHV-4** | **EBV** | infectious mononucleosis · oral hairy leukoplakia |
| **HHV-5** | **CMV** | retinitis · colitis ในผู้ป่วยกดภูมิ |
| **HHV-6** | **Roseolovirus A/B** | roseola infantum |
| **HHV-7** | **Roseolovirus** | roseola |
| **HHV-8** | **KSHV** | **Kaposi sarcoma** |

> **ลักษณะร่วมของทั้งวงศ์** — **แฝงตัว (latency) แล้วกลับมาเป็นซ้ำ (reactivation)** · นี่คือเหตุผลที่โรคกลุ่มนี้ “หายแล้วกลับมาที่เดิม” ไม่ใช่ “ติดใหม่ทุกครั้ง”

[[fig:hsvvzv]]

### HSV-1 และ HSV-2
- **ตำแหน่งคลาสสิก** **herpes labialis (HSV-1)** · **genital herpes (HSV-2)**
- **Primary infection** **กลุ่มตุ่มน้ำที่เจ็บมากบนพื้นแดง** หรือ **erosion/ulcer ที่รอยต่อผิวหนังกับเยื่อบุ (mucocutaneous junction)**
- **Recurrent infection** **รุนแรงน้อยกว่า** และมักกลับมา**ที่ตำแหน่งเดิม**

### Variant ที่ต้องจำ

| ชื่อ | ภาพ | ไวรัส |
|---|---|---|
| **Herpetic whitlow** | ตุ่มน้ำเจ็บที่**นิ้วมือ** | HSV-1 หรือ HSV-2 |
| **Herpetic folliculitis** | ตุ่มน้ำตามรูขุมขน | มัก HSV-1 |
| **Herpes gladiatorum** | ตุ่มน้ำในนักกีฬาปะทะ (มวยปล้ำ) | มัก HSV-1 |
| **Eczema herpeticum** | **แพร่กระจายทั่วตัวในผู้ป่วย atopic dermatitis** | HSV |
| **Chronic herpes infection** | แผลเรื้อรังไม่หายในผู้ป่วยกดภูมิ | HSV |

### การวินิจฉัย
**Tzanck smear · PCR · viral culture · serology**

### การรักษา — ขนาดยาตามสไลด์

| ยา | Initial outbreak | Recurrent | Suppressive |
|---|---|---|---|
| **Acyclovir กิน** | **400 mg TID** หรือ **200 mg วันละ 5 ครั้ง × 7–10 วัน** | **400 mg TID × 5–7 วัน** | **400 mg BID** |
| **Acyclovir IV** | **5–10 mg/kg ทุก 8 ชม.** สำหรับรายรุนแรงหรือ encephalitis | — | — |
| **Valacyclovir** | **1 g BID × 7–10 วัน** | **500 mg BID × 3 วัน** หรือ 1 g OD × 5–7 วัน | **500 mg–1 g OD** |
| **Famciclovir** | **250 mg TID × 7–10 วัน** | **125 mg BID × 5 วัน** | **250 mg BID** |

### ภาวะแทรกซ้อน
- **ของตัวโรค** การติดเชื้อแบคทีเรียซ้อน · **herpes encephalitis**
- ✍️ **ของยา — อาจารย์เน้น**
  - **พิษต่อไต (nephrotoxicity)** โดยเฉพาะ **acyclovir ทางหลอดเลือดดำ** → **ให้สารน้ำให้พอ และหยดช้ากว่า 1 ชั่วโมง**
  - **พิษต่อระบบประสาท (CNS toxicity)** — **มือสั่น ประสาทหลอน** มักในผู้สูงอายุหรือไตเสื่อม
  - **GI upset** คลื่นไส้ ท้องเสีย
  - **การดื้อยา** ในผู้ป่วยกดภูมิ

#### ทำไมถึงมีอาการนี้

| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ตุ่มน้ำเป็นกลุ่มบนพื้นแดง** | ไวรัสทำลาย keratinocyte ที่อยู่ติดกันเป็นหย่อม เกิดการแยกชั้นเป็นถุงน้ำหลายใบในพื้นที่เดียว | **“กลุ่ม” คือลายเซ็นของ herpes** ไม่ใช่ตุ่มเดี่ยวกระจาย |
| **กลับมาที่ตำแหน่งเดิมทุกครั้ง** | ไวรัสหลับใน **ganglion** ที่เลี้ยงผิวบริเวณนั้น พอกลับมาจึงออกที่ผิวแปลงเดิม | ต่างจากการติดเชื้อใหม่ที่ตำแหน่งจะสุ่ม |
| **เจ็บมากกว่าที่ขนาดรอยโรคบอก** | ไวรัสอยู่ในเส้นประสาทรับความรู้สึกโดยตรง | ช่วยแยกจาก impetigo ที่มักไม่เจ็บ |
| **ผลึกยาในไตจาก acyclovir IV** | acyclovir **ละลายน้ำได้น้อย** เมื่อเข้มข้นในท่อไตจึงตกผลึกและอุดท่อไต | เหตุผลที่ต้อง**ให้น้ำและหยดช้า** ไม่ใช่ลดขนาดยาอย่างเดียว |
| **มือสั่นและประสาทหลอนในผู้สูงอายุ** | ยาและ metabolite คั่งเมื่อการทำงานของไตลดลง แล้วผ่านเข้าระบบประสาท | ต้อง**ปรับขนาดยาตามการทำงานของไต** |

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **latency / reactivation** | แฝงตัว / กลับมาเป็นซ้ำ | ลักษณะร่วมของ herpesvirus |
| **mucocutaneous junction** | รอยต่อผิวหนังกับเยื่อบุ | ตำแหน่งของ HSV |
| **grouped vesicles on an erythematous base** | กลุ่มตุ่มน้ำบนพื้นแดง | ลายเซ็นของ herpes |
| **herpetic whitlow** | เริมที่นิ้วมือ | ระวังติดจากการตรวจคนไข้ |
| **herpes gladiatorum** | เริมในนักกีฬาปะทะ | ติดจากการสัมผัสผิว |
| **eczema herpeticum** | เริมแพร่กระจายใน atopic dermatitis | ภาวะที่ต้องรักษาเร็ว |
| **Tzanck smear** | ขูดฐานรอยโรคย้อมดูเซลล์ | เห็น multinucleated giant cells |
| **suppressive therapy** | กินยาต่อเนื่องเพื่อกันเป็นซ้ำ | acyclovir 400 mg BID |
| **nephrotoxicity** | พิษต่อไต | acyclovir IV ต้องให้น้ำและหยดช้า |
""",
    ["HHV-1 HSV1 · 2 HSV2 · 3 VZV · 4 EBV · 5 CMV · 6/7 roseolovirus · 8 KSHV (Kaposi)",
     "กลุ่มตุ่มน้ำบนพื้นแดงที่กลับมาที่เดิม = HSV",
     "variant ที่ต้องจำ: whitlow · folliculitis · gladiatorum · eczema herpeticum · chronic",
     "acyclovir กิน initial 400 mg TID 7–10 วัน · recurrent 400 mg TID 5–7 วัน · suppressive 400 mg BID",
     "acyclovir IV 5–10 mg/kg ทุก 8 ชม. ต้องให้สารน้ำพอและหยดช้ากว่า 1 ชั่วโมง",
     "พิษของยา: ไต · ระบบประสาท (สั่น ประสาทหลอน) ในผู้สูงอายุหรือไตเสื่อม"],
    [mcq(N(24), "A 70-year-old man with chronic kidney disease receives intravenous acyclovir for severe herpes infection. Two days later he develops tremor and visual hallucinations, and his creatinine has risen. Which two measures directly address the mechanisms involved?",
         ["Adequate hydration with infusion over more than one hour, and dose adjustment for renal function",
          "Switching to oral famciclovir at the same total daily dose",
          "Adding a loop diuretic to increase urine output",
          "Giving an antipsychotic and continuing the same acyclovir dose",
          "Changing to topical acyclovir until the creatinine normalises"],
         0,
         "สองปัญหานี้มาจากกลไกต่างกันแต่แก้ด้วยหลักเดียวกัน · **พิษต่อไต** เกิดเพราะ **acyclovir ละลายน้ำได้น้อย จึงตกผลึกในท่อไต** → แก้ด้วย **ให้สารน้ำให้พอและหยดยาช้ากว่า 1 ชั่วโมง** ตามที่สไลด์เน้น · **พิษต่อระบบประสาท** (สั่น ประสาทหลอน) เกิดจาก**ยาคั่งเมื่อไตทำงานลดลง** → แก้ด้วย **ปรับขนาดยาตามการทำงานของไต**\n\nทำไมข้ออื่นผิด\n- **เปลี่ยนเป็น famciclovir ขนาดเดิม** ไม่แก้ปัญหา เพราะยากลุ่มนี้ขับทางไตเช่นกันและยังต้องปรับขนาดตามไต\n- **เพิ่มยาขับปัสสาวะ** ทำให้ขาดน้ำมากขึ้น ซึ่ง**เพิ่ม**การตกผลึกในท่อไต ไม่ใช่ลด\n- **ให้ยาต้านโรคจิตแล้วให้ยาเดิมต่อ** รักษาอาการแต่ปล่อยสาเหตุ และยาจะยังคั่งต่อไป\n- **ยาทา** ไม่มีที่ใช้ในการติดเชื้อรุนแรงที่ต้องให้ยาทั้งระบบ",
         "acyclovir IV: ให้น้ำพอ หยดช้ากว่า 1 ชม. และปรับขนาดตามไต",
         "Acyclovir toxicity", R("HSV — treatment complications ✍️"), NL_HSV),
     mcq(N(25), "A 25-year-old nurse develops painful grouped vesicles on the pulp of her index finger about a week after caring for a patient with oral ulcers. What is the diagnosis?",
         ["Herpetic whitlow", "Bacterial paronychia", "Bullous impetigo",
          "Contact dermatitis from glove latex", "Pyogenic granuloma"],
         0,
         "**กลุ่มตุ่มน้ำที่เจ็บบริเวณปลายนิ้ว** หลังสัมผัสผู้ป่วยที่มีแผลในปาก = **herpetic whitlow** ซึ่งสไลด์ระบุเป็น variant ของ HSV (ได้ทั้ง HSV-1 และ HSV-2) · สำคัญสำหรับบุคลากรทางการแพทย์เพราะ**ติดจากการตรวจคนไข้โดยไม่ใส่ถุงมือ**\n\nทำไมข้ออื่นผิด\n- **bacterial paronychia** บวมแดงรอบเล็บและมี**หนอง** ไม่ใช่กลุ่มตุ่มน้ำใส และมักไม่มีประวัติสัมผัสแผลในปาก\n- **bullous impetigo** พบในเด็กที่ใบหน้าหรือลำตัว ตุ่มน้ำ**ไม่เจ็บ** และมีสะเก็ดสีน้ำผึ้ง\n- **contact dermatitis จากถุงมือ** **คัน** ไม่เจ็บ และกระจายตามบริเวณที่สัมผัสทั้งมือ ไม่ใช่เป็นกลุ่มที่ปลายนิ้วเดียว\n- **pyogenic granuloma** เป็นก้อนเนื้อแดงเลือดออกง่าย ไม่ใช่ตุ่มน้ำเป็นกลุ่ม",
         "ตุ่มน้ำเป็นกลุ่มที่ปลายนิ้วในบุคลากรการแพทย์ = herpetic whitlow",
         "Herpetic whitlow", R("HSV — variant cutaneous manifestation"), NL_HSV)],
    NL_HSV, {"hsvvzv": F.hsvvzv()})

# ───────────────────────────── 13
NL_VZV = ["2.3.1(22)", "B4.2.2(6)"]
sec("derm-si-13", "VZV — สุกใส งูสวัด และสามภาวะที่ห้ามพลาด",
    "varicella · zoster · HZO (Hutchinson) · Ramsay Hunt · disseminated", 14,
"""**HHV-3 (VZV)** ให้สองโรคจากไวรัสตัวเดียว — **ติดครั้งแรกเป็น varicella (สุกใส)** และ **กลับมาเป็น herpes zoster (งูสวัด)**

[[fig:zoster]]

## Varicella (chickenpox)
- **การติดต่อ** **airborne droplets** และการสัมผัสโดยตรง · **ระยะฟักตัว ~10–21 วัน**
- **ระยะแพร่เชื้อ** **1–2 วันก่อนผื่นขึ้น จนกว่าทุกรอยโรคจะตกสะเก็ด**
- **อาการนำ** (เด่นในผู้ใหญ่) ไข้ อ่อนเพลีย ปวดศีรษะ
- **ผื่น** คัน · **macule → papule → vesicle → pustule → crust**
  - ลักษณะ vesicle ที่สไลด์เรียกว่า **“dew drop on a rose petal”** — หยดน้ำบนกลีบกุหลาบ
  - **ขึ้นเป็นชุด (crops) และอยู่ต่างระยะกันพร้อมกัน** ← **จุดที่ใช้แยกจากโรคอื่น**
  - **centripetal** — ลำตัวมากกว่าแขนขาและใบหน้า
- **การวินิจฉัย** clinical · **Tzanck smear (ขูดจากฐานรอยโรค)** → **multinucleated giant cells** · **PCR = gold standard** · **DFA** · serology IgM และ IgG ที่สูงขึ้น
- **การรักษา**
  - **supportive** — ยาลดไข้ (**เลี่ยง aspirin**) · ยาแก้แพ้ลดคัน
  - **ยาต้านไวรัสเมื่อ** **ผู้ใหญ่ · ผู้ป่วยกดภูมิ · ทารกแรกเกิด · หญิงตั้งครรภ์**
  - **รับไว้ในโรงพยาบาล** เมื่อรุนแรงหรือมีภาวะแทรกซ้อน
- **ภาวะแทรกซ้อน** การติดเชื้อแบคทีเรียซ้อน (impetigo) · **ปอดอักเสบ (เด่นในผู้ใหญ่)** · **encephalitis และ cerebellar ataxia** · ตับอักเสบในผู้ป่วยกดภูมิ · **congenital varicella syndrome** ถ้าติดช่วงต้นครรภ์

## Herpes zoster (shingles)
- **กลไก** **reactivation ของ VZV ที่หลับอยู่ใน dorsal root ganglia**
- **ปัจจัยเสี่ยง** **อายุมากขึ้น · ภาวะกดภูมิ**
- **อาการ**
  - **อาการนำ: ปวด แสบ หรือซ่าตาม dermatome — นำมาก่อนผื่นเป็นวัน**
  - ผื่น: ปื้นแดง → ตุ่มน้ำใส → แตก → ตกสะเก็ด หายใน **2–4 สัปดาห์**
  - **ข้างเดียว ตาม dermatome เดียว ไม่ข้ามแนวกลางลำตัว**
- **Variant** **zoster sine herpete = ปวดตาม dermatome โดยไม่มีผื่น**
- **ตัวอย่างการบรรยายรอยโรคจากสไลด์** *multiple group of vesicles on erythematous and purpuric base with hemorrhagic crust along T9–T10 dermatome*
- **การวินิจฉัย** clinical · **Tzanck smear** จากฐานรอยโรค → multinucleated giant cells · **PCR ไวที่สุด** · DFA หรือ viral culture
- **การรักษา**
  - **ยาต้านไวรัสภายใน 72 ชั่วโมง** — **acyclovir · valacyclovir · famciclovir** → **ลดระยะเวลาและลดภาวะแทรกซ้อน**
  - **คุมปวด** — **gabapentin · pregabalin · opioid**
  - **สเตียรอยด์** พิจารณาในรายรุนแรง **ร่วมกับยาต้านไวรัสเสมอ**
- **ภาวะแทรกซ้อน** **postherpetic neuralgia (PHN) = ปวดนานเกิน 90 วัน** · ติดเชื้อแบคทีเรียซ้อน · **HZO** · **Ramsay Hunt** · **disseminated zoster** · encephalitis และ myelitis

## สามภาวะที่ห้ามพลาด

[[fig:hzo]]

### 1. Herpes zoster ophthalmicus (HZO)
- **reactivation ที่แขนง ophthalmic (V1) ของ trigeminal nerve**
- **ครอบคลุม** ตา เปลือกตา หน้าผาก และ **ปลายจมูก**
- **Hutchinson's sign** = **ตุ่มน้ำที่ปลายจมูก → เสี่ยงสูงมากที่ตาจะถูก involve**
- **อาการ** ปวด แสบ ซ่าใน V1 · ผื่นตุ่มน้ำข้างเดียวที่หน้าผาก เปลือกตาบน ปลายจมูก · **conjunctivitis · uveitis · keratitis** · การมองเห็นเปลี่ยน กลัวแสง
- **การตรวจ** **slit-lamp exam โดยจักษุแพทย์** · PCR หรือ DFA จากฐานตุ่มน้ำถ้าไม่แน่ใจ
- **การรักษา** ยาต้านไวรัส · คุมปวด · **ส่งจักษุแพทย์ด่วน** · สเตียรอยด์หรือยาปฏิชีวนะหยอดตาใต้การดูแลจักษุแพทย์ · **cycloplegic drops** ลดปวดจาก ciliary spasm

### 2. Ramsay Hunt syndrome (herpes zoster oticus)
- **reactivation ที่ geniculate ganglion ของ facial nerve (CN VII)**
- **อาการ** ตุ่มน้ำที่เจ็บใน/รอบ **ช่องหู ใบหู หรือเพดานปาก** · **อ่อนแรงใบหน้าข้างเดียวกัน (เหมือน Bell's palsy)** · **การได้ยินลดลง เวียนศีรษะ หูอื้อ** ถ้า **CN VIII** ร่วม · บางครั้งเสียการรับรส ตาและปากแห้ง
- **การรักษา** ยาต้านไวรัส · คุมปวด · ส่ง ENT หรือประสาทวิทยา · **prednisone 60 mg/วัน × 5–7 วันแล้วลดขนาด** — **ช่วยการฟื้นตัวของ facial nerve เมื่อใช้ร่วมกับยาต้านไวรัส**

### 3. Disseminated herpes zoster (DHZ)
- **นิยาม** ผื่นตุ่มน้ำ **≥ 20 รอยโรค นอก dermatome เดิมและ dermatome ข้างเคียง**
- **มักพบใน** ผู้ป่วยกดภูมิ — **มะเร็ง ปลูกถ่ายอวัยวะ HIV**

#### ทำไมถึงมีอาการนี้

| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **สุกใสอยู่ต่างระยะกันพร้อมกัน** | ไวรัสเข้ากระแสเลือดเป็น **ระลอก (crops)** ผื่นแต่ละระลอกจึงแก่ไม่เท่ากัน | **ถ้าทุกรอยโรคอยู่ระยะเดียวกันหมด ให้คิดถึงโรคอื่น** เช่น ฝีดาษลิงหรือผื่นแพ้ยา |
| **สุกใสขึ้นลำตัวมากกว่าแขนขา (centripetal)** | ไวรัสกระจายทางเลือดไปผิวที่อุณหภูมิเหมาะและเลือดไปเลี้ยงมาก | ตรงข้ามกับผื่นที่กระจายปลายมือปลายเท้า (centrifugal) |
| **งูสวัดปวดก่อนผื่นเป็นวัน** | ไวรัสแบ่งตัวและทำลาย **ganglion กับ axon** ก่อนจะถึงปลายประสาทที่ผิวหนัง | **ปวดเฉพาะที่ไม่มีสาเหตุในผู้สูงอายุ ให้นึกถึง zoster ที่ยังไม่ออกผื่น** |
| **งูสวัดไม่ข้ามแนวกลางลำตัว** | ganglion หนึ่งอันเลี้ยงผิวเพียง dermatome เดียวของข้างนั้น | **ข้ามแนวกลาง = ไม่ใช่ zoster ธรรมดา ให้คิด disseminated** |
| **PHN ปวดเกิน 90 วัน** | เส้นประสาทเสียหายถาวรจนเกิดการส่งสัญญาณปวดผิดปกติ (neuropathic pain) | ยาที่ได้ผลจึงเป็น **gabapentin/pregabalin** ไม่ใช่ NSAID |
| **Hutchinson's sign ทำนายตาอักเสบ** | แขนง **nasociliary** ของ V1 เลี้ยงทั้งปลายจมูกและ **cornea** | ตุ่มที่ปลายจมูก = แขนงที่เลี้ยงตาถูก involve แล้ว |
| **Ramsay Hunt มีอ่อนแรงใบหน้า** | **geniculate ganglion** อยู่บนทาง CN VII · การบวมอักเสบกด facial nerve ในช่องกระดูกที่แคบ | **Bell's palsy ที่มีตุ่มน้ำในหู = Ramsay Hunt ไม่ใช่ Bell's palsy** |

> **สองเลขที่ต้องจำ** — **72 ชั่วโมง** คือหน้าต่างของยาต้านไวรัสใน zoster · **90 วัน** คือเกณฑ์เวลาของ PHN
> **สองสัญญาณที่เปลี่ยนการดูแลทันที** — **Hutchinson's sign → ส่งจักษุแพทย์ด่วน** · **ตุ่มน้ำในหู + หน้าเบี้ยว → Ramsay Hunt ต้องให้ prednisone ร่วมกับยาต้านไวรัส**

#### คำศัพท์สากลที่ต้องจำ

| คำ | ความหมาย | จุดที่ใช้ |
|---|---|---|
| **dew drop on a rose petal** | หยดน้ำบนกลีบกุหลาบ | ลักษณะ vesicle ของสุกใส |
| **lesions in crops / different stages** | ขึ้นเป็นชุด อยู่ต่างระยะกัน | ลายเซ็นของสุกใส |
| **centripetal** | กระจายเข้าหาลำตัว | รูปแบบผื่นสุกใส |
| **dermatomal distribution** | กระจายตามแนว dermatome | ลายเซ็นของงูสวัด |
| **dorsal root ganglion** | ปุ่มประสาทรับความรู้สึก | ที่หลับของ VZV |
| **prodromal pain** | ปวดนำก่อนผื่น | งูสวัด |
| **zoster sine herpete** | ปวดตาม dermatome โดยไม่มีผื่น | variant ที่วินิจฉัยยาก |
| **postherpetic neuralgia (PHN)** | ปวดต่อเนื่องเกิน 90 วัน | รักษาด้วย gabapentin/pregabalin |
| **Hutchinson's sign** | ตุ่มน้ำที่ปลายจมูก | ทำนายการ involve ของตา |
| **Ramsay Hunt syndrome** | zoster ที่ geniculate ganglion | หน้าเบี้ยว + ตุ่มในหู |
| **disseminated zoster** | ≥ 20 รอยโรคนอก dermatome เดิม | ผู้ป่วยกดภูมิ |
| **congenital varicella syndrome** | ความผิดปกติของทารกจากสุกใสในครรภ์ | เหตุผลที่ต้องให้ยาในหญิงตั้งครรภ์ |
| **multinucleated giant cells** | เซลล์หลายนิวเคลียส | ผล Tzanck smear ของ HSV และ VZV |
""",
    ["สุกใส: ขึ้นเป็นชุด อยู่ต่างระยะกันพร้อมกัน และ centripetal",
     "แพร่เชื้อตั้งแต่ 1–2 วันก่อนผื่น จนทุกรอยโรคตกสะเก็ด · ฟักตัว 10–21 วัน",
     "ให้ยาต้านไวรัสในสุกใสเมื่อ: ผู้ใหญ่ กดภูมิ ทารกแรกเกิด ตั้งครรภ์ · เลี่ยง aspirin",
     "งูสวัด: ปวดนำก่อนผื่น ข้างเดียว ไม่ข้ามแนวกลาง · ให้ยาภายใน 72 ชั่วโมง",
     "PHN = ปวดเกิน 90 วัน · รักษาด้วย gabapentin หรือ pregabalin",
     "Hutchinson's sign (ตุ่มที่ปลายจมูก) = ส่งจักษุแพทย์ด่วน",
     "Bell's palsy + ตุ่มน้ำในหู = Ramsay Hunt → prednisone 60 mg 5–7 วัน + ยาต้านไวรัส",
     "disseminated zoster = ≥ 20 รอยโรคนอก dermatome เดิม มักกดภูมิ"],
    [mcq(N(26), "A 68-year-old man has a painful unilateral vesicular rash over the right forehead and upper eyelid. There are also vesicles on the tip of his nose. Besides starting an antiviral, what is the single most important next step?",
         ["Urgent ophthalmology referral",
          "Oral prednisone 60 mg daily for one week",
          "Reassurance, as nasal lesions carry no special significance",
          "Topical acyclovir cream to the eyelid",
          "CT of the orbit before any referral"],
         0,
         "**ตุ่มน้ำที่ปลายจมูก = Hutchinson's sign** · แขนง **nasociliary** ของ **V1** เลี้ยงทั้ง**ปลายจมูก**และ **cornea** ดังนั้นการมีตุ่มที่ปลายจมูกบ่งชี้ว่า**แขนงที่เลี้ยงตาถูก involve แล้ว** และทำนาย **keratitis/uveitis** ซึ่งอาจทำให้สูญเสียการมองเห็น · สไลด์ระบุการจัดการว่า **urgent ophthalmology referral**\n\nทำไมข้ออื่นผิด\n- **prednisone กิน** ไม่ใช่ขั้นตอนสำคัญที่สุดใน HZO และการใช้สเตียรอยด์ที่ตาต้องอยู่ใต้การดูแลของจักษุแพทย์ · ขนาด 60 mg เป็นของ **Ramsay Hunt**\n- **บอกว่าไม่สำคัญ** ผิดอย่างชัดเจน — นี่คือสัญญาณที่มีชื่อเรียกเฉพาะเพราะมันสำคัญ\n- **ยาทา acyclovir** ไม่เพียงพอสำหรับ zoster และไม่ป้องกันภาวะแทรกซ้อนทางตา\n- **CT orbit** ทำให้ช้าโดยไม่เปลี่ยนการรักษา · สิ่งที่ต้องทำคือ **slit-lamp exam**",
         "ตุ่มที่ปลายจมูก = Hutchinson's sign = ส่งจักษุแพทย์ด่วน",
         "Herpes zoster ophthalmicus", R("HZO — Hutchinson's sign"), NL_VZV),
     mcq(N(27), "A 59-year-old woman has right facial droop that spares no part of the face, plus ear pain, vertigo, and vesicles in the right ear canal. Which treatment combination does the lecture recommend?",
         ["Antiviral plus prednisone 60 mg daily for 5–7 days then taper",
          "Prednisone alone, as antivirals do not help facial recovery",
          "Antiviral alone, as steroids worsen viral replication",
          "Intravenous immunoglobulin plus physiotherapy",
          "Observation only, since recovery is nearly always complete"],
         0,
         "**ตุ่มน้ำในช่องหู + อ่อนแรงใบหน้าข้างเดียวกัน + เวียนศีรษะ** = **Ramsay Hunt syndrome** จาก VZV ที่ **geniculate ganglion ของ CN VII** · สไลด์ระบุการรักษาว่า **ยาต้านไวรัสร่วมกับ prednisone 60 mg/วัน × 5–7 วันแล้วลดขนาด** ซึ่ง **ช่วยการฟื้นตัวของ facial nerve เมื่อใช้ร่วมกับยาต้านไวรัส**\n\nทำไมข้ออื่นผิด\n- **สเตียรอยด์เดี่ยว** ไม่จัดการตัวไวรัส และในภาวะนี้สไลด์ระบุให้ใช้ร่วมกัน\n- **ยาต้านไวรัสเดี่ยว** พลาดประโยชน์ต่อการฟื้นตัวของเส้นประสาท · ข้ออ้างว่าสเตียรอยด์ทำให้ไวรัสแบ่งตัวมากขึ้นไม่ใช่เหตุผลที่ใช้ในภาวะนี้เมื่อให้คู่กับยาต้านไวรัส\n- **IVIG** ไม่ใช่การรักษามาตรฐานของ Ramsay Hunt\n- **สังเกตอาการเฉย ๆ** ผิด เพราะ **Ramsay Hunt ฟื้นตัวแย่กว่า Bell's palsy** และการรักษาเร็วมีผลต่อผลลัพธ์",
         "หน้าเบี้ยว + ตุ่มในหู = Ramsay Hunt → ยาต้านไวรัส + prednisone ไม่ใช่อย่างใดอย่างเดียว",
         "Ramsay Hunt syndrome", R("Ramsay Hunt syndrome"), NL_VZV),
     mcq(N(28), "Which feature of the varicella rash is most useful for distinguishing it from other vesicular eruptions?",
         ["Lesions appear in crops and are at different stages at the same time",
          "All lesions evolve synchronously through each stage",
          "The rash begins on the palms and soles and moves centrally",
          "Lesions are confined to a single dermatome",
          "Vesicles are filled with pus from the outset"],
         0,
         "สไลด์เน้นว่า **รอยโรคของสุกใสขึ้นเป็นชุด (crops) และอยู่ต่างระยะกันพร้อมกัน** — macule, papule, vesicle, pustule, crust ปรากฏในเวลาเดียวกันบนตัวคนไข้คนเดียว · กลไกคือไวรัสเข้ากระแสเลือด**เป็นระลอก** ผื่นแต่ละระลอกจึงแก่ไม่เท่ากัน\n\nทำไมข้ออื่นผิด\n- **ทุกรอยโรคไปพร้อมกันเป็นระยะเดียว** เป็นลักษณะที่**ตรงข้าม** และเป็นเบาะแสของโรคอื่น\n- **เริ่มที่ฝ่ามือฝ่าเท้าแล้วเข้าหาลำตัว** ตรงข้ามกับสุกใสที่เป็น **centripetal** (ลำตัวมากกว่าแขนขา)\n- **จำกัดใน dermatome เดียว** คือ **herpes zoster** ไม่ใช่สุกใส\n- **มีหนองตั้งแต่แรก** ไม่ใช่ลำดับของสุกใส ซึ่งเริ่มจาก macule และเป็น vesicle ใสก่อนจะเป็น pustule",
         "สุกใส = หลายระยะพร้อมกัน · งูสวัด = dermatome เดียว",
         "Varicella — rash pattern", R("Varicella — clinical manifestations"), NL_VZV)],
    NL_VZV, {"zoster": F.zoster(), "hzo": F.hzo()})

# ───────────────────────────── MEQ
MEQ = [{
 "id": "DE-SI-MEQ-01", "kind": "meq", "topic": "ชายเบาหวานขาบวมแดงและปวดมาก", "nl": NL_NF + NL_CELL,
 "vignette": """ชายไทยอายุ 58 ปี เป็น**เบาหวานชนิดที่ 2** มา 12 ปี ควบคุมไม่ดี (HbA1c 9.8%)

มาห้องฉุกเฉินด้วย **ปวดขาขวาอย่างรุนแรงมา 14 ชั่วโมง** เริ่มจากปวดบริเวณหน้าแข้งแล้วลามขึ้นน่อง
สองวันก่อนมีแผลถลอกเล็ก ๆ ที่หลังเท้าขวาจากรองเท้ากัด

**ตรวจร่างกาย** อุณหภูมิ 38.9°C · ชีพจร 118 ครั้ง/นาที · **ความดัน 94/58 มม.ปรอท** · หายใจ 24 ครั้ง/นาที
รู้สึกตัวดีแต่กระสับกระส่าย · **ขาขวาบวมทั้งขา ผิวแดงคล้ำเป็นหย่อม ขอบไม่ชัด อุ่น**
**กดเจ็บมากจนทนไม่ได้ ซึ่งดูไม่สมดุลกับลักษณะผิวที่เห็น** · คลำได้ **กรอบแกรบใต้ผิวบริเวณน่อง**
ชีพจรที่หลังเท้าคลำได้ · ความรู้สึกที่ผิวบริเวณกลางรอยโรค**ลดลง**

**ผลตรวจแรกรับ** WBC 21,400/µL (N 88%) · Cr 1.9 mg/dL · น้ำตาล 312 mg/dL · lactate 3.8 mmol/L · CRP 268 mg/L""",
 "questions": [
   {"q": "**1. จากข้อมูลนี้ ท่านคิดถึงภาวะใดมากที่สุด และมีข้อมูลใดในโจทย์ที่สนับสนุน (4 คะแนน)**",
    "a": """**ภาวะที่คิดถึง: Necrotizing fasciitis (น่าจะเป็น Type I polymicrobial เพราะเป็นเบาหวานและมี crepitus)** — 1 คะแนน

**ข้อมูลที่สนับสนุน** (ข้อละ 0.5 คะแนน เต็ม 3 คะแนน)
- **ปวดรุนแรงไม่สมดุลกับลักษณะผิวที่เห็น (pain out of proportion)** — สัญญาณที่ไวที่สุด
- **ลุกลามเร็วภายใน 14 ชั่วโมง**
- **crepitus คลำได้ใต้ผิว** — บ่งชี้แก๊สจาก anaerobe
- **ผิวแดงคล้ำเป็นหย่อม** — หลอดเลือดที่เลี้ยงผิวเริ่มอุดตัน
- **ความรู้สึกที่ผิวลดลง** — เส้นประสาทผิวหนังถูกทำลาย
- **สัญญาณชีพของ sepsis** — ไข้สูง ชีพจรเร็ว **ความดัน 94/58** lactate 3.8
- **เบาหวานคุมไม่ได้** — ปัจจัยเสี่ยงของ Type I
- **มีทางเข้าของเชื้อ** — แผลถลอกที่หลังเท้า (outside in)"""},
   {"q": "**2. ท่านจะทำอะไรใน 1 ชั่วโมงแรก เรียงลำดับความสำคัญ (5 คะแนน)**",
    "a": """เรียงตามลำดับ (ข้อละ 1 คะแนน)

1. **ปรึกษาศัลยกรรมทันทีเพื่อ surgical exploration และ debridement** — **การผ่าตัดสำรวจคือทั้งการวินิจฉัยและการรักษา** ห้ามรอผลภาพถ่าย
2. **กู้ชีพภาวะ sepsis** — เปิดเส้นใหญ่สองเส้น ให้สารน้ำ crystalloid เจาะ **เพาะเชื้อจากเลือดสองชุด** ติดตามปัสสาวะและ lactate
3. **ให้ยาฆ่าเชื้อกว้างทางหลอดเลือดดำทันทีหลังเพาะเชื้อ** — **vancomycin ร่วมกับ piperacillin-tazobactam** (คลุม MRSA แกรมลบ และ anaerobe) · พิจารณาเพิ่ม **clindamycin** เพื่อลดการสร้าง exotoxin
4. **คุมน้ำตาลและแก้ความผิดปกติทางเมตาบอลิก** — น้ำตาล 312 และ Cr 1.9 (ปรับขนาดยาตามไต)
5. **เตรียมผู้ป่วยเข้าห้องผ่าตัดและแจ้ง ICU** — งดน้ำงดอาหาร ตรวจการแข็งตัวของเลือด เซ็นยินยอม อธิบายว่าอาจต้องตัดเนื้อตายซ้ำหลายครั้ง

**หัก 2 คะแนน** ถ้าตอบว่า “ส่ง CT ก่อนแล้วจึงปรึกษาศัลยกรรม” หรือ “ให้ยาแล้วสังเกตอาการ 6 ชั่วโมง”"""},
   {"q": "**3. ถ้าผู้ป่วยรายนี้มาด้วยภาพเดียวกันแต่ ไม่มี crepitus ไม่มีความดันต่ำ และปวดพอดีกับลักษณะผิว ท่านจะคิดถึงอะไร และต่างกันตรงไหน (3 คะแนน)**",
    "a": """**คิดถึง cellulitis** (1 คะแนน)

**เหตุผลที่ต่างกัน** (2 คะแนน)
- **cellulitis** อยู่ใน **deep dermis ถึงชั้นไขมัน** ไม่ลงถึง fascia · ความเจ็บจึง**สมดุลกับสิ่งที่เห็น** · **ไม่มี crepitus** เพราะไม่มี anaerobe สร้างแก๊ส · ไม่มีเนื้อตายและผิวไม่คล้ำ
- **การรักษาต่างกันโดยสิ้นเชิง** — cellulitis ใช้**ยาฆ่าเชื้อเป็นหลัก** (คลุม streptococci และ staphylococci) ขีดขอบรอยโรคติดตามการตอบสนอง · **ไม่ต้องผ่าตัด** เว้นแต่เกิด abscess ที่คลำได้ fluctuance
- **แต่ต้องเฝ้าระวังต่อ** — ถ้าปวดมากขึ้นผิดส่วน ผิวเริ่มคล้ำ หรือสัญญาณชีพแย่ลง ต้องกลับมาคิดถึง necrotizing fasciitis ทันที เพราะสองโรคนี้อยู่บนความต่อเนื่องเดียวกัน"""},
   {"q": "**4. จงบอกการป้องกันที่ควรให้คำแนะนำผู้ป่วยรายนี้ก่อนกลับบ้าน (3 คะแนน)**",
    "a": """ข้อละ 1 คะแนน (เลือก 3 ข้อ)
- **ควบคุมระดับน้ำตาลให้ดีขึ้น** — เบาหวานที่คุมไม่ได้ทำให้ทั้งผิวหนังเสียความต่อเนื่องและภูมิคุ้มกันบกพร่อง
- **ดูแลเท้าทุกวัน** — ตรวจดูแผล ซอกนิ้ว เล็บ และผิวแตก เพราะผู้ป่วยมีความรู้สึกที่เท้าลดลง จึงเกิดแผลโดยไม่รู้ตัว
- **เลือกรองเท้าที่พอดีและไม่เดินเท้าเปล่า** — ป้องกันแผลถลอกซึ่งเป็นทางเข้าของเชื้อ
- **รักษาแผลเล็กทันทีและมาพบแพทย์เร็วเมื่อมีผื่นแดง บวม หรือปวด** — สไลด์ระบุว่า early treatment of wounds คือการป้องกันหลัก
- **รักษาเชื้อราที่ซอกนิ้วเท้าถ้ามี** — เป็นจุดที่ทำให้ผิวแตกและเป็นประตูของแบคทีเรีย"""}],
}]

# ───────────────────────────── OSCE
OSCE = [{
 "id": "DE-SI-OSCE-01", "kind": "osce", "topic": "บรรยายรอยโรคผิวหนังและให้การวินิจฉัยแยกโรค",
 "station": "สถานีเขียนตอบ · 8 นาที", "nl": NL_SKIN,
 "instruction": """**คำสั่ง** ท่านเป็นแพทย์เวรห้องฉุกเฉิน มีผู้ป่วยสี่รายมาด้วยรอยโรคที่ผิวหนัง
จงตอบคำถามทั้งสองส่วนลงในกระดาษคำตอบ ภายใน 8 นาที

**ผู้ป่วย A** หญิง 7 ขวบ มีรอยโรครอบจมูกและมุมปาก **ลักษณะเป็นผิวหลุดตื้นปิดด้วยสะเก็ดสีเหลืองทอง** ไม่เจ็บ ไม่มีไข้

**ผู้ป่วย B** หญิง 64 ปี **ปื้นแดงสดที่แก้มซ้าย ขอบชัดเจนและยกขึ้นคลำได้** มีไข้ 38.8°C หนาวสั่น เริ่มเป็นเมื่อ 8 ชั่วโมงก่อน

**ผู้ป่วย C** ชาย 45 ปี เลี้ยงปลาสวยงาม มี **ก้อนแดงคล้ำหลายก้อนที่หลังมือขวา** เป็นมา 3 สัปดาห์ ไม่มีไข้
เคยได้ **cephalexin กิน 2 คอร์สแล้วไม่ดีขึ้น**

**ผู้ป่วย D** ชาย 33 ปี **ปื้นสีน้ำตาลแดงขอบชัดมีสะเก็ดละเอียดที่ขาหนีบสองข้าง** คันเล็กน้อย เป็นมา 2 เดือน

**คำถาม**
**1. จงบรรยายรอยโรคของผู้ป่วย A และ B ด้วยศัพท์มาตรฐาน (skin lesion terms) และให้การวินิจฉัยของทั้งสี่ราย (8 คะแนน)**
**2. สำหรับผู้ป่วย C และ D จงระบุการตรวจที่จะยืนยันการวินิจฉัย และการรักษาที่เหมาะสม (7 คะแนน)**""",
 "answer": """## เกณฑ์ให้คะแนน (เต็ม 15 คะแนน)

### ส่วนที่ 1 — บรรยายรอยโรคและวินิจฉัย (8 คะแนน)

| หัวข้อ | คำตอบที่ยอมรับ | คะแนน |
|---|---|---|
| **บรรยาย A** | **erosions covered with honey-coloured crusts** บริเวณ perioral และ perinasal | 1 |
| **วินิจฉัย A** | **Impetigo (non-bullous)** | 1 |
| **บรรยาย B** | **well-demarcated, raised, erythematous plaque** ที่แก้มซ้าย | 1 |
| **วินิจฉัย B** | **Erysipelas** (เชื้อ *Streptococcus pyogenes*) | 1 |
| **วินิจฉัย C** | **NTM cellulitis / infection** — นึกถึง ***Mycobacterium marinum*** | 2 |
| **วินิจฉัย D** | **Erythrasma** (*Corynebacterium minutissimum*) | 2 |

**หมายเหตุการให้คะแนน** — ถ้าบรรยาย A ว่า “ulcer” **ไม่ได้คะแนน** เพราะ impetigo อยู่แค่ epidermis จึงเป็น **erosion** ไม่ใช่ ulcer · ถ้าบรรยาย B ว่า “ill-defined” **ไม่ได้คะแนน** เพราะขัดกับโจทย์ที่ระบุว่าขอบชัดและยกขึ้น

### ส่วนที่ 2 — การตรวจและการรักษา (7 คะแนน)

| หัวข้อ | คำตอบที่ยอมรับ | คะแนน |
|---|---|---|
| **การตรวจของ C** | **skin biopsy** ส่ง **AFB stain · mycobacterial culture** (± PCR) | 2 |
| **เหตุผลของ C** | เพาะเชื้อธรรมดาและ swab **ไม่ขึ้น mycobacteria** จึงอธิบายการดื้อยาได้ และต้องใช้อาหารเลี้ยงจำเพาะ | 1 |
| **การรักษาของ C** | **ยาหลายตัวร่วมกัน** เช่น **clarithromycin ร่วมกับ rifampin** (± ethambutol) · **ระยะยาว** · อาจต้อง **surgical debridement** | 1 |
| **การตรวจของ D** | **Wood lamp** → **coral-red fluorescence** (จาก coproporphyrin III) | 2 |
| **การรักษาของ D** | เฉพาะที่ **clindamycin solution 2% · benzoyl peroxide · azole cream** · ถ้ากระจายกว้าง **erythromycin กิน 1 กรัม** หรือ **clarithromycin ครั้งเดียว** | 1 |

### คะแนนพิเศษ (ไม่เกินคะแนนเต็ม)
- ระบุว่าผู้ป่วย D **ต้องแยกจาก tinea cruris** และถ้าให้**ยาฆ่าเชื้อราจะไม่หาย** เพราะเป็นแบคทีเรีย — **+1**
- ระบุว่าผู้ป่วย C มี**เบาะแสจากประวัติสัมผัสน้ำ/ตู้ปลา** ซึ่งเป็นปัจจัยเสี่ยงของ NTM ตามตารางของสไลด์ — **+1**

### จุดที่ผู้สอบพลาดบ่อย
- ตอบผู้ป่วย D ว่าเป็น **tinea cruris** แล้วให้ terbinafine — **เป็นกับดักหลักของสถานีนี้** · ตัวแยกคือ **Wood lamp**
- ตอบผู้ป่วย C ว่าเป็น cellulitis ธรรมดาแล้วเปลี่ยนยาปฏิชีวนะตัวใหม่ โดย**ไม่ทำ biopsy** · คาบนี้เน้นว่า **cellulitis ที่ดื้อยาหรือเป็นสัปดาห์ขึ้นไปต้อง biopsy**
- ใช้คำบรรยายรอยโรคผิดระดับความลึก (erosion ↔ ulcer) ซึ่งเป็นคำที่สื่อ**การเกิดแผลเป็น**ต่างกัน""",
}]

LECTURE = {
 "lec": "26/10", "date": "จ. 26 ต.ค.",
 "title": "Skin infection — การติดเชื้อที่ผิวหนัง",
 "subtitle": "อ.วรนิษฐ์ อ่อนประเสริฐ · หมวดแบคทีเรียและไวรัส · เน้นคำศัพท์สากลสำหรับทำข้อสอบ",
 "lecture": "Skin infection",
 "objectives": [
   "แบ่งการติดเชื้อที่ผิวหนังด้วยสามแกน — ชนิดเชื้อ ความลึก และ outside-in vs inside-out",
   "ใช้ลักษณะขอบรอยโรคและ fluctuance ตัดสินความลึกและวิธีรักษาข้างเตียง",
   "แยก impetigo ecthyma erysipelas cellulitis folliculitis furuncle และ carbuncle ออกจากกันด้วยศัพท์บรรยายรอยโรค",
   "จับสัญญาณของ necrotizing fasciitis ให้ได้ตั้งแต่ระยะที่ผิวยังดูเกือบปกติ และเรียงลำดับการรักษา",
   "รู้ว่าเมื่อไรต้อง biopsy เพราะ cellulitis อาจมาจากเชื้อรา วัณโรค หรือ NTM",
   "ใช้ Wood lamp และ Gram stain แยกโรคของ Corynebacterium จากเชื้อรา",
   "จำชนิดของหูดคู่กับ HPV type และเลือกวิธีรักษาตามกลุ่มผู้ป่วย",
   "วินิจฉัยและรักษา HSV และ VZV รวมถึง HZO Ramsay Hunt และ disseminated zoster พร้อมระวังพิษของ acyclovir"],
 "nlGap": "เกณฑ์ฯ มีรหัสของ impetigo (`นล. 2.3.12(9)`) cellulitis (`2.3.12(4)`) abscess (`2.3.12(2)`) necrotizing fasciitis (`2.2.50`) herpes simplex (`2.3.1(8)`) VZV (`2.3.1(22)`) และ wart (`2.3.12(15)`) ครบ แต่**ไม่มีรหัสเฉพาะของ erysipelas, ecthyma, lymphangitis, pitted keratolysis, erythrasma หรือ trichomycosis** หัวข้อเหล่านั้นจึงผูกไว้กับรหัสหมวดผิวหนัง (`2.3.12`) และอาการผื่นผิวหนัง (`2.1.50`) · **ขอบเขตของคาบนี้ครอบคลุมเฉพาะหมวดแบคทีเรียและไวรัสของสไลด์** เพราะหมวด **fungal และ parasitic** ของสไลด์ดึงข้อความออกมาไม่ได้ (Drive ตัดข้อความ และไฟล์ 20.8 MB ใหญ่เกินกว่าจะ render เป็นภาพได้) — หมวดเชื้อรา (`2.3.12(11)`) ยังไม่ได้ทำและต้องใช้สไลด์ส่วนที่เหลือ",
 "guidelines": [
   "**สไลด์ Skin infection 2025 (Hand out)** — อ.วรนิษฐ์ อ่อนประเสริฐ, Division of Dermatology, Department of Internal Medicine, Rajavithi Hospital (ต้นฉบับของคาบนี้)",
   "**IDSA Practice Guidelines for the Diagnosis and Management of Skin and Soft Tissue Infections** — ใช้ประกอบเรื่องขั้นตอนการรักษาและข้อบ่งชี้ของ incision and drainage",
   "**Fitzpatrick's Dermatology, 9th ed.** — ใช้ประกอบคำบรรยายรอยโรคและกลไกของอาการในหัวข้อ “ทำไมถึงมีอาการนี้”",
   "**CDC Clinical Overview of Herpes Zoster (Shingles)** — ใช้ประกอบเรื่องหน้าต่าง 72 ชั่วโมงและนิยามของ postherpetic neuralgia"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# กระจายตำแหน่งคำตอบ (ข้อที่ตัวเลือกเรียงตามธรรมชาติไม่สลับ)
ORDERED = set()
_slot = 0
for s in S:
    for it in s["items"]:
        if it["id"] in ORDERED:
            continue
        tgt = [0, 2, 4, 1, 3][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", "derm.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LECTURE["lec"]]
data.append(LECTURE)
seen = set()
for l in data:
    for x in [i for s_ in l["sections"] for i in s_["items"]] + l["meq"] + l["osce"] + [{"id": s_["id"]} for s_ in l["sections"]]:
        assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
        seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = {c for s_ in S for c in s_["nl"]} | {c for s_ in S for i in s_["items"] for c in i["nl"]} | {c for m in MEQ + OSCE for c in m["nl"]}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
for s_ in S:
    assert "```" not in s_["md"], s_["id"]
    assert s_["md"].count("**") % 2 == 0, "** ไม่ครบคู่: " + s_["id"]
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "derm": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print("sections %d | items %d | meq %d | osce %d | figs %d | nl %d"
      % (len(S), sum(len(s_["items"]) for s_ in S), len(MEQ), len(OSCE),
         sum(len(s_["figs"]) for s_ in S), len(codes)))
print("answer positions:", dict(sorted(Counter(i["answer"] for s_ in S for i in s_["items"]).items())))
print("derm.json มี %d คาบ: %s" % (len(data), [l["lec"] for l in data]))
