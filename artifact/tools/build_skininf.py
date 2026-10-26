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
