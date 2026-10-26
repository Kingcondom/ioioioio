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
