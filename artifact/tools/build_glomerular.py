#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""คาบ 14 Approach to glomerular disease — nephrotic / nephritic (พญ.ฉันทิศา อารยางกูร) → data/nephro.json
ต้นฉบับ: Drive 1R5f1MtTJIlwCUeomxvcBD10MKpDzYob4 "Lec11 Approach to glomerular disease.pdf"
โน้ตสไลด์: slides/glomerular_notes.md · ภาพประกอบ: figs_glomerular.py
ผูกข้อคลัง Ward Drill คาบ 14 ครบ 27 ข้อ + คาบ 28 ที่เป็นเรื่อง proteinuria/lipiduria/LN 8 ข้อ + Mock 6 ข้อ"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_bank import link
from link_mock import link_mock
from svg import fig
import figs_glomerular as F

SET, LEC = "nephro", "14"
SRC = "สไลด์ พญ.ฉันทิศา — Approach to glomerular disease"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl, figs=None, source=SRC):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": source,
              "nl": nl, "md": md, "pearls": pearls, "items": items, "figs": figs or {}})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}
N = lambda n: "NEPH-GN-MCQ-%02d" % n
R = lambda p: ["สไลด์ พญ.ฉันทิศา — " + p]
NS, AGN, CGN = "2.3.14(12)", "2.3.14(2)", "2.3.14-3(1)"
UA = ["3.1.6", "B9.3(2)"]

# ───────────────────────────── 1
sec("neph-gn-01", "ตะแกรงไต 3 ชั้น — glomerular filtration barrier",
    "endothelium · GBM · podocyte — แต่ละชั้นกันอะไร และพังแล้วได้อาการอะไร", 8,
"""### Glomerulus คืออะไร
**Glomerulus** คือกระจุกหลอดเลือดฝอยที่อยู่ระหว่าง **afferent** กับ **efferent arteriole** ห่อด้วย Bowman capsule ไตสองข้างกรองพลาสมาราว **180 ลิตรต่อวัน** แต่ปัสสาวะที่ออกมามีโปรตีนไม่ถึง **150 มก./วัน** (albumin < 30 มก./วัน) — เพราะผนังหลอดเลือดฝอยตรงนี้เป็น **ตะแกรง 3 ชั้น** ที่ยอมให้น้ำและสารโมเลกุลเล็กผ่าน แต่กันโปรตีนและเม็ดเลือดไว้

[[fig:barrier]]

### ตะแกรง 3 ชั้น (สไลด์)
| ชั้น | โครงสร้าง | กันอะไร |
|---|---|---|
| ① **Glomerular endothelial cell** | มีรูพรุน (fenestra) + เคลือบด้วย glycocalyx ที่เป็น **ประจุลบ** | ผลัก albumin (ประจุลบ) · กันเม็ดเลือด |
| ② **Glomerular basement membrane (GBM)** | extracellular matrix — **type IV collagen**, laminin, fibronectin | ตาข่ายกันโปรตีนขนาดใหญ่และเม็ดเลือด |
| ③ **Podocyte** (glomerular epithelial cell) | **foot process** สานกันเป็นซี่ ระหว่างซี่มี **filtration slit diaphragm** (nephrin, podocin) | ด่านสุดท้ายที่กันโปรตีน — **ชั้นที่สำคัญที่สุดของ albumin** |

ตะแกรงคัดสองอย่างพร้อมกัน — **ขนาด** (albumin 66 kDa ใหญ่พอดีขอบ) และ **ประจุ** (albumin เป็นลบ จึงถูกผนังที่เป็นลบผลัก) albumin ส่วนน้อยที่หลุดผ่านจะถูก **proximal tubule** ดูดกลับด้วยตัวรับ megalin–cubilin

### พังชั้นไหน ได้อาการอะไร — แกนของทั้งคาบ
| ชั้นที่เสีย | ผลที่เกิด | ตัวอย่างโรค |
|---|---|---|
| **Podocyte / slit diaphragm** | albumin รั่วจำนวนมาก โดย **ไม่มีการอักเสบ** → **nephrotic** | MCD · FSGS · MN |
| **GBM** ฉีกหรือบางผิดปกติ | **RBC ลอดออก** → hematuria | Alport (collagen IV ผิด) · thin basement membrane · anti-GBM |
| Endothelium / mesangium **อักเสบ** มีเซลล์อักเสบมาเกาะ | หลอดเลือดฝอยตีบ GFR ลด + GBM ฉีก → **nephritic** | PSGN · IgAN · LN class III/IV · ANCA |

> ลายมือบนสไลด์เขียนคำว่า **minimal change** ไว้ข้าง podocyte — คือโรคต้นแบบของ "podocyte พังอย่างเดียว" (เรียนต่อในหัวข้อ 9)

> **Mesangial cell** อยู่ตรงกลางกระจุกหลอดเลือด ค้ำโครงสร้างและเก็บกวาด immune complex — เมื่อ IgA หรือ immune complex ไปสะสมที่ mesangium (IgAN, LN class II) จึงเห็น **mesangial proliferation**
""",
    ["ตะแกรง 3 ชั้น: endothelium (fenestra + ประจุลบ) → GBM (collagen IV) → podocyte (foot process + slit diaphragm)",
     "ตะแกรงคัดทั้ง ขนาด และ ประจุ — albumin เป็นประจุลบจึงถูกผลัก",
     "Podocyte พัง = albumin รั่วโดยไม่อักเสบ → nephrotic · GBM ฉีก/อักเสบ = RBC ลอด → nephritic",
     "ปกติโปรตีนในปัสสาวะ < 150 มก./วัน · albumin < 30 มก./วัน"],
    [mcq(N(1), "A 7-year-old boy has generalized edema, urine protein 4+ with no red cells, serum albumin 1.6 g/dL and a normal serum creatinine. Kidney biopsy shows normal glomeruli on light microscopy and no immune deposits. Injury to which component of the glomerular filtration barrier best explains his heavy proteinuria?",
         ["Fenestrated endothelial cells", "Type IV collagen network of the glomerular basement membrane", "Podocyte foot processes and slit diaphragm", "Mesangial cells", "Proximal tubular megalin–cubilin receptors"], 2,
         "**Podocyte foot process และ slit diaphragm** คือด่านสุดท้ายที่กัน albumin — ใน minimal change disease foot process **แผ่แบน (effacement)** เห็นได้เฉพาะใน EM ส่วน LM ปกติ และไม่มีการอักเสบ จึงได้ albumin รั่วจำนวนมากโดยไม่มีเลือดในปัสสาวะ\n\n- **Endothelium** เสียมักมาพร้อมการอักเสบ (nephritic) ไม่ใช่ภาพนี้\n- **GBM collagen IV** ผิดปกติ (Alport) เด่นที่ **hematuria**\n- **Mesangial cell** เพิ่มจำนวนใน IgAN/LN ซึ่งจะเห็นใน LM\n- **Megalin–cubilin** เสียทำให้เกิด tubular proteinuria ปริมาณน้อย < 1–2 g/d",
         "albumin รั่วมาก + LM ปกติ = podocyte (foot process effacement)", "Filtration barrier", R("Glomerular structure"), ["B9.1.1(1)", NS]),
     mcq(N(2), "A 19-year-old man has persistent microscopic hematuria, mild proteinuria and progressive sensorineural hearing loss. His maternal uncle required dialysis at age 35. A defect in which structure is most likely?",
         ["Podocyte nephrin", "Glomerular basement membrane type IV collagen", "Endothelial glycocalyx", "Tamm–Horsfall protein in the thick ascending limb", "Mesangial IgA clearance"], 1,
         "ภาพนี้คือ **Alport syndrome** — ยีน **COL4A5** (X-linked จึงถ่ายทอดผ่านฝั่งแม่) ทำให้ **type IV collagen** ใน **GBM** ผิดปกติ GBM บางสลับหนาและแตก → **RBC ลอดออก** เป็น hematuria ตั้งแต่เด็ก ร่วมกับหูชั้นใน (collagen ชนิดเดียวกันอยู่ใน cochlea) และตา\n\nลายมือในสไลด์โยง asymptomatic hematuria ไปที่ **IgA · Alport · thin basement membrane**\n\n- **Nephrin** ผิดปกติให้ congenital nephrotic syndrome (โปรตีนรั่ว ไม่ใช่เลือด)\n- **Glycocalyx** เสียทำให้ albumin ผ่านง่าย ไม่ใช่ RBC\n- **Tamm–Horsfall** เป็นโปรตีนหลอดไต เป็นแม่พิมพ์ของ cast ไม่เกี่ยว\n- **IgAN** ไม่มีหูหนวกและไม่ถ่ายทอดแบบนี้",
         "hematuria + หูหนวก + ประวัติครอบครัวฝั่งแม่ = Alport (GBM collagen IV)", "Filtration barrier", R("Glomerular structure; ลายมือ asymptomatic hematuria → IgA, Alport, thin BM"), ["B9.1.1(1)", "2.1.43"])],
    ["B9.1.1(1)", "B9.1.2(2)"],
    {"barrier": fig("ตะแกรงกรอง 3 ชั้นของ glomerulus",
        "น้ำและสารโมเลกุลเล็ก **ผ่านทั้ง 3 ชั้น** ไปเป็นน้ำกรองในช่อง Bowman · **albumin** (ประจุลบ) ถูกผนังที่เป็นประจุลบผลักกลับตั้งแต่ชั้นแรก · **RBC** ใหญ่เกินกว่าจะผ่าน GBM — กล่องด้านล่างคือผลเมื่อแต่ละชั้นพัง ซึ่งเป็นแกนของการแยก nephrotic กับ nephritic ทั้งคาบ",
        F.barrier())})

# ───────────────────────────── 2
sec("neph-gn-02", "อาการทั้งหมดมาจาก 2 กลไก — ตะแกรงรั่ว กับ GFR ลด",
    "ทำไมปัสสาวะเป็นฟอง ทำไมบวมรอบตาตอนเช้า ทำไมความดันขึ้น ทำไมปัสสาวะน้อย", 9,
"""### กลไกใหญ่ 2 ทาง (สไลด์)
สไลด์แบ่งอาการของโรค glomerulus ออกเป็นสองกลไก — **loss of barrier** (ตะแกรงรั่ว) กับ **decreased eGFR** (กรองได้น้อยลง) แทบทุกอาการที่จะเจอในคาบนี้ตกอยู่ในสองกิ่งนี้

[[fig:twomech]]

| กลไก | สิ่งที่ตรวจพบ |
|---|---|
| **Loss of barrier** | **Proteinuria** — foamy urine · **Hematuria** — microscopic หรือ macroscopic |
| **Decreased eGFR** | **Azotemia** · **Oliguria** · **Salt/water retention** → edema (generalized) และ hypertension |

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ปัสสาวะเป็นฟอง** (foamy urine) | โปรตีนเป็นสารที่มีทั้งส่วนชอบน้ำและไม่ชอบน้ำ จึงทำตัวเหมือน **สารลดแรงตึงผิว** ไปเคลือบผิวฟองอากาศ ฟองจึงอยู่นานหลายนาที ต่างจากฟองจากการปัสสาวะแรงที่แตกหายเร็ว | เด่นมากใน **nephrotic** (++++) น้อยกว่าใน nephritic (++) |
| **บวมรอบตาตอนตื่นนอน → ขาบวมตอนบ่าย** | ผิวหนังรอบตาเป็น **เนื้อเยื่อหลวม** แรงดันในเนื้อเยื่อต่ำ น้ำจึงซึมเข้าไปสะสมได้ง่าย · นอนราบทั้งคืนน้ำกระจายมาที่หน้า · ลุกเดินทั้งวันแรงโน้มถ่วงดึงน้ำลงขา | เป็นลักษณะของบวมจาก **ไต** — บวมจากหัวใจมักเริ่มที่ขาและหอบเวลานอนราบ |
| **บวมทั้งตัว (anasarca)** ใน nephrotic | albumin ต่ำ → แรงดึงน้ำ (oncotic pressure) ในหลอดเลือดลด + ไตเก็บโซเดียมเอง (รายละเอียดหัวข้อ 7) | albumin มักต่ำมาก < 2–2.5 g/dL |
| **บวม + ความดันสูง + หอบ** ใน nephritic | GFR ลด แต่ท่อไตยังดูดโซเดียมกลับเต็มที่ → โซเดียมและน้ำ **คั่งในหลอดเลือด** (overfill) → ความดันขึ้น ปอดคั่งน้ำได้ · renin ถูกกด | albumin **ปกติหรือต่ำเล็กน้อย** · มี hematuria |
| **ปัสสาวะน้อย + BUN/Cr ขึ้น** | เซลล์อักเสบและเซลล์ที่แบ่งตัว **อุดช่องหลอดเลือดฝอย** พื้นที่กรองลด → GFR ลด (ลายมือ: *BUN rising*) | เด่นใน nephritic และ RPGN — nephrotic แท้ ๆ มักไม่มี |
| **ปัสสาวะสีโค้ก / น้ำล้างเนื้อ** | RBC ลอดผ่าน GBM ที่ฉีก แล้ว hemoglobin ถูกกรดในปัสสาวะเปลี่ยนเป็นสีน้ำตาลระหว่างทางที่ยาวผ่านท่อไต (หัวข้อ 5) | ชี้ว่าเลือดมาจาก **glomerulus** |

> เกณฑ์ปัสสาวะน้อย: **oliguria < 400 มล./วัน** · **anuria < 100 มล./วัน** (เกณฑ์มาตรฐาน — ลายมือบนสไลด์เขียนคำว่า anuria ไว้ตรงนี้)
""",
    ["อาการทั้งหมดมาจาก 2 กลไก: ตะแกรงรั่ว (proteinuria, hematuria) และ GFR ลด (azotemia, oliguria, เกลือน้ำคั่ง → บวม + HT)",
     "ปัสสาวะเป็นฟองเพราะโปรตีนทำตัวเป็นสารลดแรงตึงผิว — ฟองอยู่นาน",
     "บวมรอบตาตอนเช้าเพราะเนื้อเยื่อหลวม + นอนราบ · บ่ายย้ายไปขาตามแรงโน้มถ่วง",
     "Nephritic: GFR ลดแต่ท่อไตยังดูดโซเดียม → overfill → HT + บวม + ปอดคั่ง (renin ต่ำ)"],
    [mcq(N(3), "A 9-year-old girl develops facial puffiness, cola-colored urine and blood pressure 150/95 mmHg two weeks after a sore throat. Serum albumin is 3.8 g/dL. Which mechanism best explains her hypertension and edema?",
         ["Low plasma oncotic pressure from urinary albumin loss", "Renin release from renal hypoperfusion with high plasma renin activity", "Primary renal sodium retention with expanded plasma volume and suppressed renin", "Increased capillary permeability from systemic vasculitis", "Excess antidiuretic hormone causing pure water retention"], 2,
         "ใน **nephritic syndrome** GFR ลดลงจากการอักเสบในกระจุกหลอดเลือด แต่ท่อไตยังทำงานดี จึงดูดโซเดียมกลับเกือบหมด → โซเดียมและน้ำ **คั่งในหลอดเลือด** (overfill) → ความดันสูง บวม ปอดคั่งน้ำ ระบบ renin จึงถูก **กด** ไม่ได้ถูกกระตุ้น\n\n- **Oncotic pressure ต่ำ** ต้องมี albumin ต่ำมาก แต่รายนี้ albumin 3.8 ปกติ\n- **Renin สูง** เป็นกลไกของ renal artery stenosis ไม่ใช่ GN\n- **Vasculitis ทั่วร่างกาย** ไม่เข้ากับภาพหลัง strep\n- **ADH** ทำให้คั่งน้ำเปล่าและโซเดียมต่ำ ไม่ใช่ความดันสูง",
         "nephritic บวม + HT = โซเดียมคั่ง (overfill) renin ต่ำ · albumin ปกติ", "Clinical manifestation", R("Clinical manifestation: decreased eGFR → salt/water retention"), [AGN, "2.1.39"]),
     mcq(N(4), "A 35-year-old woman says that for 3 weeks her eyelids are swollen on waking and the swelling 'moves' to her ankles by late afternoon; her urine has persistent froth. Which statement best explains this pattern?",
         ["Periorbital tissue is loose with low tissue pressure, and fluid redistributes with posture through the day", "Thyroid hormone deficiency deposits glycosaminoglycans in the eyelids", "Right heart failure raises jugular venous pressure only when supine", "Allergic histamine release peaks in the early morning", "Lymphatic obstruction in the head and neck worsens at night"], 0,
         "บวมจากไต (โดยเฉพาะ nephrotic) เห็นที่ **รอบตาตอนเช้า** เพราะเนื้อเยื่อรอบตาหลวม แรงดันในเนื้อเยื่อต่ำ น้ำจึงสะสมง่าย บวกกับ **นอนราบทั้งคืน** · พอลุกเดินทั้งวัน **แรงโน้มถ่วง** ดึงน้ำลงขา ร่วมกับ **ฟองในปัสสาวะ** (โปรตีนเป็นสารลดแรงตึงผิว) ทำให้นึกถึงโปรตีนรั่ว\n\n- **Myxedema** บวมแบบกดไม่บุ๋มและไม่ย้ายตามท่า\n- **หัวใจห้องขวาล้มเหลว** บวมเริ่มที่ขา มี JVP สูง\n- **ภูมิแพ้** มักคันและเป็นเฉียบพลัน\n- **ท่อน้ำเหลืองอุดตัน** บวมเฉพาะที่ ไม่สัมพันธ์กับฟองในปัสสาวะ",
         "บวมรอบตาตอนเช้า → ขาตอนบ่าย + ปัสสาวะเป็นฟอง = บวมจากไต (โปรตีนรั่ว)", "Clinical manifestation", R("Clinical manifestation: foamy urine, generalized edema"), [NS, "2.1.39"])],
    ["2.1.39", "2.1.43", "2.1.44", "B9.2.5(1)", NS, AGN],
    {"twomech": fig("อาการของโรค glomerulus มาจากสองกิ่ง",
        "กิ่งซ้าย **ตะแกรงรั่ว** ให้ proteinuria (ปัสสาวะเป็นฟอง) และ hematuria · กิ่งขวา **GFR ลด** ให้ BUN/Cr ขึ้น ปัสสาวะน้อย และเกลือน้ำคั่งจนบวมและความดันขึ้น — โรคที่กิ่งซ้ายเด่นคือ **nephrotic** โรคที่กิ่งขวาเด่นร่วมกับ hematuria คือ **nephritic**",
        F.twomech())})

# ───────────────────────────── 3
sec("neph-gn-03", "วัดโปรตีนในปัสสาวะ — dipstick · SSA · 24 ชั่วโมง · UPCR",
    "dipstick เห็นแค่ albumin · SSA เห็นทุกโปรตีน · เก็บ 24 ชม. ต้องเช็คความครบด้วย creatinine", 9,
"""### วิธีกึ่งปริมาณ (semi-quantitative) — สไลด์
| Urine dipstick | protein (mg/dL) | | SSA turbidity | protein (mg/dL) |
|---|---|---|---|---|
| Negative | 0 | | 0 | 0 |
| Trace | 15–30 | | Trace | 1–10 |
| 1+ | 30–100 | | 1+ | 15–30 |
| 2+ | 100–300 | | 2+ | 40–100 |
| 3+ | 300–1,000 | | 3+ | 150–350 |
| 4+ | > 1,000 | | 4+ | > 500 |

**Turbidometric test** ใช้ปัสสาวะผสม **sulfosalicylic acid (SSA) อัตรา 1 : 3** แล้วดูความขุ่น

[[fig:dipstick]]

#### ทำไม dipstick ถึงพลาด light chain
แผ่น dipstick ใช้สี **tetrabromophenol blue** ที่ pH ต่ำ สีจะเปลี่ยนเมื่อมีโปรตีนมาจับ (protein error of indicator) และจับกับ **หมู่ amino ของ albumin** ได้ดีที่สุด — **light chain และ globulin แทบไม่ทำให้สีเปลี่ยน** สไลด์ (และลายมือ) จึงเน้นว่า **dipstick ตรวจได้เฉพาะ albumin** ส่วน SSA เป็นกรดที่ทำให้โปรตีน **ทุกชนิด** ตกตะกอนจนขุ่น

| ผลไม่ตรงกัน | ความหมาย |
|---|---|
| Dipstick ลบ/น้อย แต่ **SSA หรือ 24-h protein สูง** | มีโปรตีนที่ไม่ใช่ albumin → **light chain (multiple myeloma)** · tubular proteinuria |
| Dipstick บวกปลอม | ปัสสาวะด่างมาก (pH > 8 เช่น ติดเชื้อ Proteus) · ปนน้ำยาฆ่าเชื้อ chlorhexidine · จุ่มนานเกิน |
| Dipstick ลบปลอม | ปัสสาวะเจือจางมาก · โปรตีนไม่ใช่ albumin |

ตัวเลข dipstick เป็น **ความเข้มข้น (mg/dL)** ไม่ใช่ปริมาณต่อวัน — 1+ ในปัสสาวะเจือจางอาจหมายถึงโปรตีนมากกว่า 1+ ในปัสสาวะเข้มข้น นี่คือเหตุผลที่ต้องวัดเชิงปริมาณ

### วิธีเชิงปริมาณ (quantitative)
**1) 24-hour urine protein** — มาตรฐานอ้างอิง แต่ผู้ป่วยมักเก็บไม่ครบ ต้องเช็คด้วย **urine creatinine ใน 24 ชม.** (สไลด์)
| เพศ | creatinine ที่ควรออกใน 24 ชม. |
|---|---|
| หญิง | **15–20 mg/kg/วัน** |
| ชาย | **20–25 mg/kg/วัน** |
ตัวอย่าง: ชาย 60 กก. ควรออก 1,200–1,500 มก./วัน ถ้าวัดได้ 700 มก. แปลว่า **เก็บไม่ครบ** โปรตีนที่วัดได้จึงต่ำกว่าความจริง

**2) Urine protein–creatinine ratio (UPCR)** — ตรวจปัสสาวะครั้งเดียว หารโปรตีนด้วย creatinine ในหน่วยเดียวกัน (mg/dL ÷ mg/dL) ความเข้มข้นของปัสสาวะถูก **หักล้างกัน** เพราะทั้งสองตัวถูกเจือจางเท่ากัน ค่าที่ได้ (g/g) **ประมาณเท่ากับกรัมต่อวัน** เพราะคนทั่วไปขับ creatinine ราววันละ 1 กรัม — นิยมใช้ **ปัสสาวะครั้งแรกตอนเช้า** เพื่อตัดผลของการยืนเดินและออกกำลัง
| UPCR (g/g) | ความหมาย (แนวทางทั่วไป — ไม่ได้อยู่ในสไลด์) |
|---|---|
| < 0.15–0.2 | ปกติ |
| 0.5–3 | โปรตีนรั่วระดับกลาง (subnephrotic) |
| > 3–3.5 | **nephrotic range** |

> ในผู้ป่วยเบาหวานใช้ **urine albumin–creatinine ratio (UACR)** คัดกรองระยะแรก เพราะไวกว่า
""",
    ["Dipstick จับเฉพาะ albumin — myeloma (light chain) อาจได้ dipstick ลบแต่ SSA/24-h protein สูง",
     "SSA ปัสสาวะ : SSA = 1 : 3 ตกตะกอนโปรตีนทุกชนิด",
     "เช็คการเก็บ 24 ชม. ด้วย creatinine: หญิง 15–20 · ชาย 20–25 mg/kg/วัน",
     "UPCR (g/g) ≈ กรัมต่อวัน · ใช้ปัสสาวะเช้า · > 3–3.5 = nephrotic range"],
    [mcq(N(5), "A 60-kg man collects a 24-hour urine sample for protein, which returns 1.1 g/day. The total urine creatinine in the same collection is 650 mg. What is the best interpretation?",
         ["The collection is complete and the proteinuria is subnephrotic", "The collection is incomplete, so the true protein excretion is likely higher", "The low creatinine indicates severe acute kidney injury", "Creatinine excretion is irrelevant to the interpretation of urine protein", "The collection is over-complete, so the true proteinuria is lower"], 1,
         "ชาย 60 กก. ควรขับ creatinine **20–25 mg/kg/วัน = 1,200–1,500 มก.** ได้แค่ 650 มก. คือ **เก็บไม่ครบราวครึ่งเดียว** โปรตีนจริงจึงน่าจะสูงกว่า 1.1 g (อาจถึงราว 2 g)\n\n- เก็บครบต้องได้ creatinine อยู่ในช่วงข้างต้น\n- AKI ไม่ทำให้ creatinine ในปัสสาวะ 24 ชม. ลดได้ฉับพลันขนาดนี้ในภาวะคงที่ — ค่าที่ต่ำมากชี้ไปที่การเก็บมากกว่า\n- creatinine ใช้ **เช็คความครบ** จึงจำเป็นเสมอ\n- เก็บเกินจะได้ creatinine สูงเกินช่วง ไม่ใช่ต่ำ",
         "24-h urine: creatinine ชาย 20–25 · หญิง 15–20 mg/kg/วัน — ต่ำกว่านี้ = เก็บไม่ครบ", "Proteinuria measurement", R("24 hr collection of urine protein — urine creatinine"), UA),
     mcq(N(6), "A first-morning spot urine sample shows protein 360 mg/dL and creatinine 90 mg/dL. Which estimate of daily protein excretion is most appropriate?",
         ["About 0.4 g/day", "About 1 g/day", "About 4 g/day", "About 9 g/day", "It cannot be estimated without a 24-hour collection"], 2,
         "**UPCR = 360 ÷ 90 = 4 g/g ≈ 4 กรัมต่อวัน** (เพราะคนทั่วไปขับ creatinine ราววันละ 1 กรัม) → อยู่ใน **nephrotic range**\n\n- 0.4 คือหารผิดหลัก\n- UPCR ใช้แทน 24-h ได้ดีในทางคลินิก ไม่จำเป็นต้องรอเก็บ 24 ชม. เสมอ",
         "UPCR (mg/dL ÷ mg/dL) ≈ กรัมต่อวัน", "Proteinuria measurement", R("Urine protein creatinine ratio (UPCR)"), UA + [NS])],
    UA + ["B9.3(1)"],
    {"dipstick": fig("Dipstick เทียบกับ SSA",
        "ผู้ป่วยที่มีแต่ **light chain** ในปัสสาวะ dipstick จะอ่านได้ลบหรือแค่ trace เพราะแผ่นสีจับเฉพาะ albumin แต่ **SSA ขุ่น** และ 24-h protein สูง — ความไม่ตรงกันนี้คือเบาะแสของ **multiple myeloma** (ลายมือบนสไลด์)",
        F.dipstick())})

# ───────────────────────────── 4
sec("neph-gn-04", "Proteinuria 5 ชนิด — โปรตีนรั่วมาจากไหน",
    "functional · orthostatic · overflow · tubular · glomerular — แยกด้วยปริมาณ ชนิดโปรตีน และตะกอน", 9,
"""### แบ่งตามระยะเวลาและกลไก (สไลด์)
| กลุ่ม | ชนิด | ลักษณะ |
|---|---|---|
| **Transient** | **Functional** | < 1–2 g/d · ตะกอนปกติ (bland) · ความเครียด ออกกำลังหนัก ไข้ UTI หัวใจล้มเหลว |
| | **Orthostatic** | < 1 g/d · **บวกเมื่อยืน ลบเมื่อนอน** |
| **Persistent** | **Overflow** | light chain (MM) · lysozyme (AML) · myoglobin (rhabdomyolysis) · hemoglobin (hemolysis) |
| | **Tubular** | < 1–2 g/d · ATN, AIN, chronic tubulointerstitial nephritis, hypertensive nephrosclerosis |
| | **Glomerular** | subnephrotic ถึง **nephrotic > 3.5 g/d** |

[[fig:protsrc]]

#### ทำไมแต่ละชนิดถึงเกิด
| ชนิด | กลไก | เบาะแสแยก |
|---|---|---|
| **Functional** | ออกกำลัง ไข้ หัวใจล้มเหลว → catecholamine และ angiotensin II เพิ่ม → แรงดันและสัดส่วนการกรองใน glomerulus เปลี่ยน **ชั่วคราว** | หายเองเมื่อสาเหตุหาย · ตรวจซ้ำตอนพักเป็นลบ |
| **Orthostatic** | ท่ายืนทำให้การไหลเวียนในไตเปลี่ยน (บางรายมีหลอดเลือดดำไตซ้ายถูกกด) → โปรตีนรั่วเฉพาะตอนยืน | วัยรุ่น/คนหนุ่มสาว · **ปัสสาวะเช้าหลังตื่น (นอนทั้งคืน) ปกติ** แต่ตอนบ่ายบวก |
| **Overflow** | ในเลือดมีโปรตีนโมเลกุลเล็กมากผิดปกติ ถูกกรองออกมามากเกินกว่า proximal tubule จะดูดกลับทัน | ตัว glomerulus ปกติ · dipstick อาจลบ (light chain) แต่ SSA บวก · myoglobin/Hb ให้ dipstick heme บวกแต่ไม่มี RBC |
| **Tubular** | glomerulus กรองโปรตีนเล็ก (β2-microglobulin, α1-microglobulin) ออกมาตามปกติ แต่ **proximal tubule เสีย** ดูดกลับไม่ได้ | ปริมาณน้อย < 1–2 g/d · เป็นโปรตีนเล็กไม่ใช่ albumin · อาจมี glycosuria, phosphaturia ร่วม |
| **Glomerular** | ตะแกรงพัง → albumin รั่ว | ปริมาณมากได้ · albumin เด่น · มี hematuria/cast หรือ lipiduria ตามโรค |

### เมื่อเจอ dipstick บวกในคนสุขภาพดี — เดินทีละขั้น (แนวทางทั่วไป)
1. **ตรวจซ้ำ** ตอนพัก ไม่มีไข้ ไม่ได้ออกกำลัง — ลบ = **functional** จบ
2. ยังบวก → **split collection** ปัสสาวะเช้าแรก (นอน) เทียบกับตอนกลางวัน — เช้าลบ บ่ายบวก = **orthostatic** ไม่ต้องรักษา ติดตาม
3. บวกทั้งสองช่วง (**persistent**) → วัดปริมาณ (UPCR) · ดูตะกอน · creatinine/eGFR · อัลตราซาวนด์ไต → คิดถึง glomerular disease (เข้าคำถามข้อ 1 ของหัวข้อ 6)
""",
    ["Transient = functional (หายเมื่อสาเหตุหาย) + orthostatic (ยืนบวก นอนลบ) · ทั้งคู่ < 1–2 g/d ตะกอนปกติ",
     "Overflow: light chain–MM · lysozyme–AML · myoglobin–rhabdo · Hb–hemolysis — glomerulus ปกติ",
     "Tubular: β2-microglobulin < 1–2 g/d จาก ATN/AIN/CTIN/HT",
     "Glomerular: albumin เด่น ได้ถึง > 3.5 g/d",
     "ปัสสาวะเช้าแรกปกติแต่ตอนบ่ายบวก = orthostatic"],
    [mcq(N(7), "A 58-year-old man with acute monocytic leukemia has urine protein of 2.4 g/day; serum albumin and creatinine are normal and the urine sediment is bland. Most of the urinary protein is lysozyme. What is the mechanism of his proteinuria?",
         ["Loss of podocyte foot processes", "Filtered load of a small protein exceeding proximal tubular reabsorption", "Immune-complex deposition in the mesangium", "Hemodynamic changes induced by upright posture", "Leukemic infiltration of the glomerular basement membrane"], 1,
         "**Overflow proteinuria** — leukemia ชนิด monocytic สร้าง **lysozyme** (โปรตีนโมเลกุลเล็ก) ออกมาในเลือดมาก glomerulus ที่ปกติกรองผ่านได้ง่าย จนปริมาณที่ถูกกรอง **เกินความสามารถของ proximal tubule** ที่จะดูดกลับ สไลด์จัด lysozyme–AML ไว้ในกลุ่มนี้ร่วมกับ light chain–MM\n\n- **Podocyte** เสียจะได้ albumin เด่นและ albumin ในเลือดต่ำ\n- **Immune complex** ให้ hematuria/cast\n- **Orthostatic** ปริมาณ < 1 g/d และหายเมื่อนอน\n- การแทรกซึมของเซลล์มะเร็งที่ GBM ไม่ใช่กลไกของโปรตีนชนิดนี้",
         "โปรตีนเล็กในเลือดล้น (light chain, lysozyme, myoglobin, Hb) = overflow", "Types of proteinuria", R("Overflow proteinuria"), UA)],
    UA,
    {"protsrc": fig("โปรตีนในปัสสาวะมาจาก 4 จุด",
        "① **Glomerular** — ตะแกรงรั่ว ได้ albumin มากที่สุด · ② **Tubular** — glomerulus ปกติ แต่ proximal tubule ดูดโปรตีนเล็กกลับไม่ได้ · ③ **Overflow** — โปรตีนเล็กในเลือดมากจนกรองออกมาเกินที่ท่อไตจะดูดกลับ · ④ **Functional / orthostatic** — แรงดันใน glomerulus เปลี่ยนชั่วคราว ปริมาณน้อยและตะกอนปกติ",
        F.protsrc())})

# ───────────────────────────── 5
sec("neph-gn-05", "Hematuria — เลือดมาจาก glomerulus หรือไม่",
    "ปั่นก่อน · dysmorphic RBC · RBC cast · สีโค้ก · ไม่มีลิ่มเลือด — ทำไมแต่ละอย่างชี้ไปที่ glomerulus", 10,
"""### ขั้นแรก: สีแดงนั้นเป็นเลือดจริงไหม (สไลด์)
[[fig:redurine]]

ปัสสาวะสีแดงต้อง **ปั่นก่อน** — ถ้าสีแดงตกเป็นตะกอน (มี Hct) คือ **hematuria** · ถ้าตะกอนใสแต่น้ำส่วนบนยังแดง ให้จุ่ม dipstick
- **Dipstick heme บวก แต่ไม่มี RBC** → **myoglobinuria** (rhabdomyolysis) หรือ **hemoglobinuria** (hemolysis) — แผ่น dipstick ตรวจกิจกรรม peroxidase ของ heme จึงไม่แยกว่า heme อยู่ใน RBC หรือละลายอยู่
- **Dipstick ลบ** → สีจากยาหรืออาหาร: **rifampin · porphyrin · beet root · สีผสมอาหาร**

### Glomerular หรือ non-glomerular (สไลด์ อ้าง Brenner & Rector)
| | **Glomerular hematuria** | **Non-glomerular hematuria** |
|---|---|---|
| สี | แดงขุ่น **smoky** สีน้ำตาล หรือ **coca-cola** | แดงสด หรือชมพู |
| ลิ่มเลือด | **ไม่มี** | **อาจมี** |
| Proteinuria | **> 500 มก./วัน** | < 500 มก./วัน |
| ตะกอน | **Dysmorphic RBC / RBC cast** | RBC รูปร่างปกติ ไม่มี cast |

**เกณฑ์ glomerular RBC** (RBC ≥ 3/HPF ร่วมกับข้อใดข้อหนึ่ง): ① **RBC cast** ② **dysmorphic RBC** — **distorted microcytic RBC > 50%** หรือ **acanthocyte > 5%**

[[fig:rbcjourney]]

#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก | ความหมาย |
|---|---|---|
| **Dysmorphic RBC** | RBC ต้อง **เบียดผ่านรอยฉีกเล็ก ๆ ของ GBM** แล้วไหลผ่านท่อไตที่ความเข้มข้น **เปลี่ยนสลับเจือจาง–เข้มข้น** (loop of Henle) เยื่อหุ้มเซลล์บวม-หดซ้ำจนเสียรูป | ชี้ว่าเลือดผ่าน nephron มาตั้งแต่ glomerulus |
| **Acanthocyte** (วงแหวนมีตุ่มยื่น) | รูปที่จำเพาะที่สุดของความเสียหายแบบข้างต้น — แทบไม่เกิดจากเลือดที่ออกในกระเพาะปัสสาวะ | > 5% ก็พอจะบอกว่าเป็น glomerular |
| **RBC cast** | **Tamm–Horsfall protein (uromodulin)** ที่หลั่งจาก thick ascending limb เป็นเจลในท่อไตส่วนปลาย RBC ที่หลุดมาจาก glomerulus ถูกหุ้มไว้ตามรูปท่อ จึงออกมาเป็นแท่ง | **บอกตำแหน่งได้แน่นอนที่สุด** — ต้องเกิดในท่อไต ไม่มีทางเกิดใต้ต่อไต |
| **สีโค้ก / ชา / smoky** | hemoglobin อยู่ในปัสสาวะที่เป็นกรดนานตลอดทางยาวของท่อไต จึงถูกออกซิไดซ์เป็นสารสีน้ำตาล (acid hematin, methemoglobin) | เลือดที่ออกใกล้ทางออก (กระเพาะปัสสาวะ) ยังแดงสด |
| **ไม่มีลิ่มเลือด** | RBC ปนอยู่ในน้ำกรองปริมาณมาก ความเข้มข้นต่ำ และท่อไตสร้าง **urokinase** ที่สลายไฟบริน | ลิ่มเลือดชี้ไปที่ทางเดินปัสสาวะส่วนล่าง (นิ่ว เนื้องอก) |
| **Proteinuria > 500 มก./วัน** | GBM ที่ฉีกให้ RBC ลอดได้ ย่อมให้ albumin รั่วด้วย | hematuria ร่วมกับโปรตีนมาก = โรคเนื้อไต |

### Non-glomerular — คิดอะไร
นิ่ว · ติดเชื้อ · **มะเร็งทางเดินปัสสาวะ** (โดยเฉพาะผู้สูงอายุ สูบบุหรี่ เลือดออกไม่เจ็บ) · ต่อมลูกหมากโต · บาดเจ็บ · ยาต้านการแข็งตัวของเลือด (ยามักแค่เผยรอยโรคที่มีอยู่ ต้องหาสาเหตุต่อ) — การส่องกล้องและ CT urography เรียนในคาบ Renal imaging
""",
    ["ปัสสาวะแดง → ปั่นก่อน: ตะกอนแดง = hematuria · น้ำส่วนบนแดง + heme บวก = myoglobin/Hb · heme ลบ = ยา/อาหาร",
     "Glomerular: สีโค้ก smoky · ไม่มี clot · protein > 500 มก./วัน · dysmorphic RBC / RBC cast",
     "Dysmorphic: distorted microcytic RBC > 50% หรือ acanthocyte > 5%",
     "RBC cast = Tamm–Horsfall หุ้ม RBC ในท่อไต → บอกว่ามาจาก nephron แน่นอน",
     "ลิ่มเลือดในปัสสาวะ = เลือดออกจากทางเดินปัสสาวะส่วนล่าง"],
    [mcq(N(8), "A 24-year-old man develops dark red urine 2 days after an extreme cross-fit session. The urine dipstick is 3+ for blood, but microscopy shows 0–2 RBC/HPF; the urine supernatant remains red after centrifugation. Serum creatine kinase is 48,000 U/L. What explains the dipstick result?",
         ["Glomerular hematuria with lysed dysmorphic red cells", "Myoglobin reacting with the heme peroxidase pad", "Food dye producing a false-positive dipstick", "Rifampicin discoloration of the urine", "Bilirubin crossreacting with the blood pad"], 1,
         "แผ่น blood ของ dipstick ตรวจ **กิจกรรม peroxidase ของ heme** — **myoglobin** จากกล้ามเนื้อสลายก็มี heme จึงให้ผลบวกแรงทั้งที่ **แทบไม่มี RBC** และสีแดงค้างอยู่ใน **น้ำส่วนบน** หลังปั่น (สไลด์: dipstick +ve → myoglobinuria / hemoglobinuria)\n\n- Glomerular hematuria จะเห็น RBC ในตะกอนจำนวนมาก\n- **สีผสมอาหารและ rifampin** ให้ปัสสาวะแดงแต่ **dipstick ลบ**\n- Bilirubin มีแผ่นตรวจของตัวเอง ไม่ทำให้แผ่น blood บวก",
         "heme บวก + ไม่มี RBC + น้ำส่วนบนแดง = myoglobin หรือ hemoglobin", "Hematuria", R("Red urine algorithm"), ["2.1.43"] + UA),
     mcq(N(9), "Urine microscopy from a 30-year-old woman shows 25 RBC/HPF. Which finding most strongly localizes the bleeding to the glomerulus?",
         ["Bright red urine with small clots", "Acanthocytes making up 8% of the red cells", "Isomorphic red cells with a few white cells", "Hyaline casts", "Positive leukocyte esterase"], 1,
         "สไลด์กำหนด dysmorphic RBC ว่า **distorted microcytic RBC > 50% หรือ acanthocyte > 5%** — acanthocyte 8% จึงเข้าเกณฑ์ glomerular hematuria เพราะ RBC ต้องเบียดผ่าน GBM และผ่านท่อไตที่ความเข้มข้นเปลี่ยนจึงจะได้รูปแบบนี้\n\n- **ลิ่มเลือดและสีแดงสด** ชี้ไปที่ทางเดินปัสสาวะส่วนล่าง\n- **RBC รูปร่างปกติ** = non-glomerular\n- **Hyaline cast** พบได้ในคนปกติ (ขาดน้ำ ออกกำลัง) ไม่บอกโรค glomerulus\n- **Leukocyte esterase** บอกว่ามีเม็ดเลือดขาว (ติดเชื้อ/อักเสบ)",
         "acanthocyte > 5% หรือ dysmorphic > 50% หรือ RBC cast = glomerular", "Hematuria", R("Glomerular RBC criteria"), ["2.1.43"] + UA)],
    ["2.1.43"] + UA,
    {"redurine": fig("ปัสสาวะสีแดง — ปั่นก่อน แล้วดูว่าสีอยู่ตรงไหน",
        "ขั้นตอนตามสไลด์: ตะกอนแดง = **hematuria** ไปส่องตะกอนต่อ · น้ำส่วนบนแดงให้ดู **dipstick heme** — บวกแต่ไม่มี RBC คือ myoglobin หรือ hemoglobin · ลบคือสีจากยา อาหาร หรือ porphyrin",
        F.redurine()),
     "rbcjourney": fig("ทำไม RBC จาก glomerulus ถึงผิดรูปและกลายเป็น cast",
        "RBC ที่หลุดจาก glomerulus ต้อง ① **เบียดผ่าน GBM** ② ผ่านท่อไตที่ **ความเข้มข้นเปลี่ยนสลับ** จนเสียรูปเป็น **acanthocyte** และ ③ ถูก **Tamm–Horsfall** หุ้มเป็น **RBC cast** ระหว่างทาง hemoglobin ถูกกรดเปลี่ยนเป็นสีน้ำตาล — ส่วนเลือดจากกระเพาะปัสสาวะ RBC ยังกลม สีแดงสด และอาจจับเป็นลิ่ม",
        F.rbcjourney())})

# ───────────────────────────── 6
sec("neph-gn-06", "6 คำถาม และ 5 กลุ่มอาการ — เดินจากปัสสาวะไปหาชื่อโรค",
    "Clinical clues ของสไลด์ · asymptomatic · nephrotic · nephritic · RPGN · CGN · ทำไมตำแหน่ง deposit กำหนดกลุ่มอาการ", 11,
"""### Clinical clues — ถาม 6 ข้อตามลำดับ (สไลด์)
| | คำถาม | ใช้อะไรตอบ |
|---|---|---|
| 1 | **Is this glomerular disease?** | มี **glomerular hematuria** และ/หรือ **glomerular proteinuria** (หัวข้อ 4–5) |
| 2 | **What's the glomerular syndrome?** | จัดเข้า 1 ใน 5 กลุ่มอาการ (ตารางถัดไป) |
| 3 | **What's the morphological diagnosis?** | ชิ้นเนื้อไต — LM · IF · EM |
| 4 | **Is this primary or secondary?** | primary = **จำกัดที่ไต** · secondary = **โรคทั้งระบบ** |
| 5 | **Proper investigations?** | เลือกตามกลุ่มอาการและโรคที่สงสัย |
| 6 | **Proper treatments?** | ทั่วไป + เฉพาะโรค |

### 5 กลุ่มอาการ (สไลด์)
| กลุ่มอาการ | เกณฑ์ |
|---|---|
| **Asymptomatic** (เจอจากการตรวจสุขภาพ) | isolated proteinuria **130 มก.–3 g/วัน** · hematuria **> 2 dysmorphic RBC/HPF** ในปัสสาวะปั่น หรือ **> 1 RBC cast** — ลายมือ: นึกถึง **IgAN · Alport · thin basement membrane** |
| **Nephrotic syndrome** | proteinuria **> 3.5 g/วัน** · edema · albumin ต่ำ (**< 3–3.5 g/dL**) · cholesterol **> 200 mg/dL** · **lipiduria** (oval fat body, fatty cast) |
| **Nephritic syndrome** | **glomerular hematuria** · proteinuria **< 3 g/วัน** · azotemia · edema · oliguria · ความดันสูงหรือ AKI ที่เพิ่งเกิด |
| **RPGN** | acute GN ร่วมกับ **crescent จำนวนมาก (มัก > 30–50%)** · GFR ลด **50% ภายใน 3 เดือน** |
| **Chronic GN (CGN)** | ไตเสื่อมช้า **> 3 เดือน** · proteinuria > 3 g/วัน และ/หรือ glomerular hematuria · HT · **ไตเล็ก** หรือ glomerulosclerosis รุนแรง |

### Nephrotic เทียบ nephritic (สไลด์)
| ลักษณะ | Nephrotic | Nephritic |
|---|---|---|
| Edema | ++++ | ++ |
| ความดันสูง | ไม่มี | **มี** |
| ปอดคั่งน้ำ | มักไม่มี | อาจมี |
| ปัสสาวะเป็นฟอง/proteinuria | ++++ | ++ |
| Albumin | **ต่ำ** | ปกติหรือต่ำเล็กน้อย |
| Glomerular hematuria | ไม่มี | **มี** |
| Oliguria / AKI | มักไม่มี | **มี** |

### โรคแต่ละโรคอยู่ตรงไหนของสเปกตรัม
[[fig:spectrum]]

#### ทำไมบางโรค nephrotic บางโรค nephritic — ดูที่ตำแหน่งของ deposit
[[fig:deposits]]

| ตำแหน่ง | อยู่ติดกับอะไร | ผล | โรค |
|---|---|---|---|
| **Podocyte เอง** (ไม่มี deposit) | — | foot process แผ่แบน → รั่วล้วน ไม่อักเสบ | MCD · FSGS |
| **Subepithelial** (นอก GBM ด้านปัสสาวะ) | podocyte · **ห่างจากกระแสเลือด** | complement เจาะ podocyte → รั่วมาก แต่เซลล์อักเสบในเลือดเข้าไม่ถึง → **ตะกอนใส** | **MN** (เล็กสม่ำเสมอ) · PSGN (hump ใหญ่ — แต่มีอักเสบใน capillary ร่วมด้วยจึงเป็น nephritic) |
| **Subendothelial** (ใต้ endothelium ด้านเลือด) | **กระแสเลือดโดยตรง** | ดึง neutrophil/monocyte + complement → อักเสบ หลอดเลือดอุด GBM ฉีก → **nephritic** | **LN class III/IV** · MPGN |
| **Mesangial** | แกนกลางกระจุกหลอดเลือด | mesangial cell แบ่งตัว → hematuria เด่น โปรตีนปานกลาง | **IgAN** · LN class II |

### Morphological diagnosis (แผนภาพในสไลด์)
podocytopathy (**MCD, FSGS**) · **MN** · deposition disease · **ANCA**-associated · **anti-GBM** (Goodpasture) — แต่ละกลุ่มอยู่ในหัวข้อ 8–13

### Proper investigations — ชุดแรก (แนวทางทั่วไป อิง KDIGO 2021 — สไลด์ไม่ได้ลงรายละเอียด)
| กลุ่ม | ส่งตรวจ |
|---|---|
| ทุกราย | UA + ตะกอน · UPCR · BUN/Cr/eGFR · albumin · lipid profile · CBC · อัลตราซาวนด์ไต (ขนาด ความหนาของเนื้อไต) |
| หาสาเหตุทุติยภูมิ | **C3, C4** · ANA, anti-dsDNA · HBsAg, anti-HCV, anti-HIV · FBS/HbA1c |
| ตามภาพ | nephritic หลังติดเชื้อ: **ASO, anti-DNase B** · RPGN: **ANCA (MPO/PR3), anti-GBM** · nephrotic ผู้ใหญ่: **anti-PLA2R** · อายุมาก: **SPEP/UPEP, serum free light chain** · คัดกรองมะเร็งตามอายุ (MN) |
| ชิ้นเนื้อไต | ผู้ใหญ่ส่วนใหญ่ — ยกเว้นเด็กเนโฟรติกแบบฉบับ (ให้ steroid ก่อน) · **ไตเล็กแล้ว (CGN) ไม่เจาะ** เพราะได้แต่แผลเป็นและเสี่ยงเลือดออก |
""",
    ["6 คำถาม: ใช่โรค glomerulus ไหม → กลุ่มอาการอะไร → พยาธิอะไร → ปฐมภูมิหรือทุติยภูมิ → ส่งตรวจ → รักษา",
     "Nephrotic: > 3.5 g/วัน + บวม + albumin ต่ำ + cholesterol > 200 + lipiduria",
     "Nephritic: glomerular hematuria + protein < 3 g + azotemia + บวม + oliguria + HT ใหม่",
     "RPGN: crescent > 30–50% + GFR ลด 50% ใน 3 เดือน · CGN: > 3 เดือน + ไตเล็ก",
     "Deposit ติดด้านเลือด (subendothelial) = อักเสบ = nephritic · ด้านปัสสาวะ (subepithelial) = รั่ว = nephrotic"],
    [mcq(N(10), "A 52-year-old woman has creatinine that rose from 0.9 to 2.4 mg/dL over 5 weeks, with dysmorphic red cells, red cell casts and urine protein 1.5 g/day. Which glomerular syndrome is this?",
         ["Asymptomatic urinary abnormality", "Nephrotic syndrome", "Rapidly progressive glomerulonephritis", "Chronic glomerulonephritis", "Isolated tubular proteinuria"], 2,
         "**RPGN** = acute GN ที่ไตเสื่อมเร็ว — เกณฑ์ในสไลด์คือ **GFR ลดลง 50% ภายใน 3 เดือน** (creatinine เพิ่มขึ้นเกินเท่าตัวใน 5 สัปดาห์) ร่วมกับตะกอนแบบ glomerular และพยาธิจะมี **crescent > 30–50%**\n\n- **Asymptomatic** ไตต้องปกติ\n- **Nephrotic** ต้องโปรตีน > 3.5 g และไม่มี active sediment เด่น\n- **CGN** ต้องดำเนินโรค > 3 เดือนและมักไตเล็ก\n- **Tubular proteinuria** ไม่มี RBC cast",
         "creatinine เพิ่มเกินเท่าตัวในไม่กี่สัปดาห์ + RBC cast = RPGN → หา anti-GBM/ANCA/C3 และเจาะไตด่วน", "Glomerular syndromes", R("Rapidly progressive glomerulonephritis"), [AGN, "B9.2.7(1)"]),
     mcq(N(11), "In which location do immune deposits typically produce heavy proteinuria with a bland urine sediment, because circulating inflammatory cells cannot reach them?",
         ["Subendothelial space", "Mesangium", "Subepithelial space on the outer side of the GBM", "Within the tubular basement membrane", "Within the lumen of glomerular capillaries"], 2,
         "deposit ที่อยู่ **ด้าน subepithelial** (นอก GBM ฝั่งปัสสาวะ ติด podocyte) อย่างใน **membranous nephropathy** อยู่ **หลังกำแพง GBM** ห่างจากกระแสเลือด complement ที่ถูกกระตุ้นเจาะ podocyte ให้โปรตีนรั่วมาก แต่ neutrophil และ monocyte ในเลือดเข้าไม่ถึง จึงไม่มีการอักเสบ ตะกอนใส\n\n- **Subendothelial** ติดกระแสเลือด → อักเสบ → nephritic (LN III/IV)\n- **Mesangium** → mesangial proliferation hematuria เด่น (IgAN)\n- TBM และในช่องหลอดเลือดไม่ใช่ตำแหน่งที่ให้ภาพนี้",
         "subepithelial (MN) = รั่วไม่อักเสบ · subendothelial (LN IV) = อักเสบ", "Glomerular syndromes", ["หลักพยาธิสรีรวิทยา (Brenner & Rector) — ไม่ได้อยู่ในสไลด์ตรง ๆ"], [NS, AGN])],
    [NS, AGN, CGN, "B9.2.2(4)", "B1.6.1(1)"],
    {"spectrum": fig("สเปกตรัมจาก nephrotic ถึง nephritic (ตารางในสไลด์)",
        "ความยาวแท่งตามจำนวน + ที่อาจารย์ให้ไว้ — **MCD** อยู่ปลาย nephrotic ล้วน **crescentic GN** อยู่ปลาย nephritic ล้วน โรคที่อยู่กลาง ๆ อย่าง **FSGS** (ลายมือ: *Nephro–Nephri*) หรือ **IgAN/LN** มาได้ทั้งสองแบบ ขึ้นกับความรุนแรง",
        F.spectrum()),
     "deposits": fig("ตำแหน่งของ immune deposit บอกกลุ่มอาการ",
        "deposit ที่ **ติดด้านเลือด** (subendothelial) เรียกเซลล์อักเสบได้ทันที → **nephritic** · deposit **นอก GBM ด้านปัสสาวะ** (subepithelial) ทำร้าย podocyte แต่เซลล์อักเสบเข้าไม่ถึง → **nephrotic ตะกอนใส** · **hump** ของ PSGN อยู่ด้านเดียวกันแต่มาพร้อมการอักเสบใน capillary จึงเป็น nephritic · **mesangial** deposit ให้ hematuria เด่น",
        F.deposits())})

# ───────────────────────────── 7
sec("neph-gn-07", "Nephrotic syndrome — ทำไมแต่ละอาการถึงเกิด",
    "บวม (underfill + overfill) · ไขมันสูง · lipiduria · ลิ่มเลือด · ติดเชื้อ · Ca/T4 ต่ำ · การรักษาทั่วไป", 12,
"""### ต้นไม้ของ nephrotic
[[fig:nstree]]

ทุกอาการเริ่มจากจุดเดียว — **podocyte พัง → albumin และโปรตีนอื่นรั่วมาก** แล้วแตกเป็นกิ่ง

#### ทำไมถึงมีอาการนี้
| อาการ / สิ่งตรวจพบ | กลไก | เบาะแสทางคลินิก |
|---|---|---|
| **บวมกดบุ๋ม ทั้งตัว** | สองกลไกร่วมกัน (ภาพถัดไป): **underfill** — albumin ต่ำ แรงดึงน้ำในหลอดเลือดลด น้ำซึมออก · **overfill** — plasminogen ที่รั่วมาถูกเปลี่ยนเป็น plasmin แล้วไป **เปิด ENaC** ที่ collecting duct ไตจึงเก็บโซเดียมเอง | บวมรอบตาตอนเช้า ขาตอนบ่าย · น้ำในช่องท้อง/เยื่อหุ้มปอด |
| **ไม่ค่อยมีปอดคั่งน้ำ** | ความดันในหลอดเลือดไม่ได้สูงแบบ nephritic และ oncotic pressure ในเนื้อเยื่อปอดลดตามไปด้วย น้ำเหลืองระบายได้มากขึ้น | ต่างจาก nephritic ที่ volume ล้นในหลอดเลือด |
| **Cholesterol สูง** | albumin ต่ำกระตุ้นให้ **ตับสร้าง lipoprotein (apoB) เพิ่ม** · PCSK9 เพิ่ม ทำให้ LDL receptor ลด · การทำงานของ **lipoprotein lipase ลด** จึงกำจัด VLDL/triglyceride ช้า — **ไม่ได้มาจากการกินหรือไตขับไม่ออก** | LDL และ TG สูง เสี่ยงหลอดเลือดแข็งระยะยาว |
| **Lipiduria** — oval fat body, fatty cast | lipoprotein รั่วผ่านตะแกรง เซลล์ท่อไตกลืนไขมันไว้แล้วหลุดออกมา (**oval fat body**) หรือติดอยู่ใน cast · ใต้แสงโพลาไรซ์ cholesterol ester เห็นเป็น **Maltese cross** | ใช้ยืนยันว่าโปรตีนรั่วจาก glomerulus |
| **ลิ่มเลือด** — RVT, PE, DVT | **antithrombin III** (ขนาดใกล้ albumin) รั่วออก · ตับสร้าง **fibrinogen, factor V, VIII** เพิ่ม · เกล็ดเลือดจับกลุ่มง่าย · เลือดข้นจากยาขับปัสสาวะ | **RVT**: ปวดสีข้างเฉียบพลัน hematuria โปรตีนรั่วมากขึ้น ไตวาย และในชาย **varicocele ข้างซ้าย** (หลอดเลือดดำอัณฑะซ้ายเทเข้า renal vein ซ้าย) · เสี่ยงสูงสุดใน **MN** |
| **ติดเชื้อง่าย** | สูญเสีย **IgG** และ **complement factor B** ซึ่งจำเป็นต่อการเคลือบเชื้อมีแคปซูล + บวมน้ำเป็นแหล่งเพาะเชื้อ + ยากดภูมิ | เด็ก MCD ไข้ ปวดท้อง → **SBP จาก pneumococcus** · cellulitis |
| **Muehrcke's lines** (เล็บมีแถบขาวคู่) | albumin ต่ำทำให้ฐานเล็บบวม | หายเมื่อ albumin กลับมา |
| **Ca รวมต่ำ** | albumin ที่จับ Ca ลด + **vitamin D binding protein** รั่ว | ดู ionized Ca หรือแก้ด้วย albumin |
| **T4 รวมต่ำ แต่ free T4/TSH ปกติ** | **thyroxine-binding globulin** รั่ว | ไม่ต้องให้ thyroxine |
| **ซีด** | **transferrin** และ erythropoietin รั่ว | — |
| **AKI** | volume ในหลอดเลือดต่ำเกิน (ขับน้ำมากไป) · เนื้อไตบวม · RVT · ยา (NSAIDs, AIN) | creatinine ขึ้นระหว่างรักษา |

### ทำไมบวม — underfill หรือ overfill
[[fig:fill]]

### ทำไม furosemide ต้องใช้ขนาดสูง
furosemide ต้อง **จับกับ albumin** เพื่อถูกส่งไปยัง proximal tubule แล้วหลั่งเข้าท่อ — albumin ในเลือดต่ำ ยาถึงท่อน้อย · และ albumin ที่รั่วอยู่ในน้ำกรอง **จับยาไว้ในท่อ** ไม่ให้ออกฤทธิ์ที่ loop of Henle → ต้องเพิ่มขนาด ให้วันละ 2 ครั้ง หรือร่วมกับ thiazide/amiloride (ยับยั้ง ENaC)

### การรักษาทั่วไปของ nephrotic syndrome (อิง KDIGO 2021 — สไลด์เน้นการรักษาเฉพาะโรค)
| เป้าหมาย | การรักษา | เหตุผลเชิงกลไก |
|---|---|---|
| บวม | **จำกัดเกลือ** (Na < 2 g/วัน) + **loop diuretic** ± thiazide | ลด Na คั่ง |
| ลดโปรตีนรั่ว | **ACEi / ARB** (± SGLT2i ในผู้ใหญ่) | ขยาย efferent arteriole ลดแรงดันใน glomerulus — ระวัง Cr ขึ้นและ K สูง ไม่เริ่มขณะ volume ต่ำหรือ AKI |
| ไขมัน | **statin** ถ้าโปรตีนรั่วต่อเนื่อง | ลดความเสี่ยงหลอดเลือด |
| ลิ่มเลือด | **anticoagulant ป้องกัน** ใน MN ที่ albumin ต่ำมาก (< 2–2.5 g/dL) และเลือดออกง่ายต่ำ | MN เสี่ยงสูงสุด |
| ติดเชื้อ | วัคซีน pneumococcus, influenza · ระวัง SBP | IgG/factor B รั่ว |
""",
    ["Nephrotic ทุกอาการเริ่มจาก podocyte พัง → โปรตีนรั่ว → albumin ต่ำ + โปรตีนอื่นรั่ว",
     "บวม = underfill (albumin ต่ำ) + overfill (plasmin เปิด ENaC)",
     "Cholesterol สูงเพราะตับสร้าง lipoprotein เพิ่ม + LPL ลด · lipiduria = oval fat body, Maltese cross",
     "ลิ่มเลือด: AT-III รั่ว + fibrinogen/V/VIII เพิ่ม → RVT (ปวดสีข้าง hematuria varicocele ซ้าย) — MN เสี่ยงสุด",
     "ติดเชื้อ: IgG/factor B รั่ว → เด็ก MCD เป็น pneumococcal SBP"],
    [mcq(N(12), "A 40-year-old man with nephrotic syndrome (albumin 2.0 g/dL, urine protein 8 g/day) has low total T4 but normal free T4 and TSH. He has no thyroid symptoms. What is the best interpretation?",
         ["Primary hypothyroidism requiring levothyroxine", "Central hypothyroidism from pituitary infarction", "Urinary loss of thyroxine-binding globulin with normal thyroid function", "Sick euthyroid syndrome requiring T3 replacement", "Iodine deficiency from proteinuria"], 2,
         "**Thyroxine-binding globulin** เป็นโปรตีนขนาดเล็กพอจะรั่วออกทางตะแกรงที่พัง T4 ที่จับกับโปรตีนจึงลด → **T4 รวมต่ำ** แต่ส่วนที่ออกฤทธิ์ (**free T4**) และ **TSH ปกติ** = ต่อมไทรอยด์ทำงานปกติ ไม่ต้องให้ยา (หลักเดียวกับ Ca รวมต่ำจาก albumin ต่ำ)\n\n- **Primary hypothyroid** ต้องมี TSH สูง\n- **Central** ต้องมี free T4 ต่ำ\n- **Sick euthyroid** ไม่รักษาด้วย T3\n- โปรตีนรั่วไม่ทำให้ขาดไอโอดีน",
         "nephrotic: T4 รวมต่ำ / Ca รวมต่ำ จากโปรตีนจับรั่ว — ดู free T4, ionized Ca", "Nephrotic complications", ["หลักพยาธิสรีรวิทยา — ไม่ได้อยู่ในสไลด์"], [NS]),
     mcq(N(13), "A patient with nephrotic syndrome (albumin 1.9 g/dL) remains edematous despite oral furosemide 40 mg daily. Which mechanism best explains the diuretic resistance?",
         ["Furosemide is excreted unchanged by the liver in hypoalbuminemia", "Reduced albumin-bound delivery to the proximal tubule and binding of furosemide by albumin within the tubular lumen", "Downregulation of the Na–K–2Cl cotransporter by aldosterone", "Increased renal blood flow washing out the drug", "Furosemide-induced hyperkalemia blocking its own action"], 1,
         "furosemide ต้องจับกับ **albumin** จึงถูกนำไปส่งและหลั่งที่ proximal tubule — albumin ต่ำ ยาถึงท่อน้อย และ **albumin ที่รั่วอยู่ในท่อจับยาไว้** ไม่ให้ไปออกฤทธิ์ที่ Na–K–2Cl ของ loop of Henle ร่วมกับ ENaC ที่ถูก plasmin เปิดช่วยดูดโซเดียมกลับที่ปลายท่อ → ต้องใช้ขนาดสูงขึ้น วันละ 2 ครั้ง หรือเสริม thiazide/amiloride\n\n- furosemide ขับทางไต ไม่ใช่ตับ\n- aldosterone ไม่ได้ลดจำนวน NKCC2\n- เลือดไปไตใน nephrotic ไม่ได้เพิ่ม\n- furosemide ทำให้ K ต่ำ ไม่ใช่สูง",
         "albumin ต่ำ = furosemide ส่งถึงท่อน้อย + ถูกจับในท่อ → ขนาดสูง ± thiazide/amiloride", "Nephrotic treatment", ["หลักเภสัชวิทยา + KDIGO 2021 — ไม่ได้อยู่ในสไลด์"], [NS, "B9.4(1)"])],
    [NS, "B9.2.2(4)", "2.1.39", "B9.4(1)", "2.3.9(2)"],
    {"nstree": fig("ต้นไม้ของ nephrotic syndrome",
        "กิ่งซ้าย: **albumin ต่ำ** → บวม และตับเร่งสร้างไขมัน → lipiduria · กิ่งขวา: **โปรตีนอื่นรั่วตาม** — antithrombin III (ลิ่มเลือด) · IgG/factor B (ติดเชื้อ) · โปรตีนจับฮอร์โมนและแร่ธาตุ (Ca, T4 รวมต่ำ ซีด)",
        F.nstree()),
     "fill": fig("บวมใน nephrotic — สองกลไกที่เกิดพร้อมกัน",
        "**Underfill** (ซ้าย) อธิบายบวมเมื่อ albumin ต่ำมาก โดยเฉพาะเด็ก MCD · **Overfill** (ขวา) อธิบายว่าทำไมผู้ป่วยหลายรายบวมทั้งที่ volume ในหลอดเลือดไม่ได้ต่ำ — plasminogen ที่รั่วมาเปิด **ENaC** ไตจึงเก็บโซเดียมเองโดยไม่ต้องรอ renin",
        F.fill())})

# ───────────────────────────── 8
sec("neph-gn-08", "Nephritic · RPGN · CGN — ทำไม GFR ลด และ crescent คืออะไร",
    "หลอดเลือดฝอยถูกเซลล์อักเสบอุด · GBM ฉีกจน fibrin รั่วเข้า Bowman space เป็น crescent · IF 3 แบบ", 10,
"""### Nephritic syndrome (สไลด์)
glomerular hematuria · proteinuria < 3 g/วัน · azotemia (ลายมือ: **BUN rising**) · edema · oliguria · ความดันสูงหรือ AKI ที่เพิ่งเกิด

[[fig:glomx]]

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก |
|---|---|
| **Oliguria, BUN/Cr ขึ้น** | immune complex หรือแอนติบอดีกระตุ้น complement → neutrophil และ monocyte มาเกาะ · endothelial และ mesangial cell แบ่งตัว (**endocapillary proliferation**) → **ช่องหลอดเลือดฝอยตีบ** พื้นที่กรองลด → GFR ลด |
| **ความดันสูง + บวม + ปอดคั่งน้ำ** | GFR ลดแต่ท่อไตยังดูดโซเดียมเต็มที่ → **โซเดียมคั่ง (overfill)** renin ถูกกด — ความดันอาจสูงจนปวดศีรษะ ชัก (hypertensive encephalopathy) |
| **Hematuria สีโค้ก + RBC cast** | การอักเสบทำให้ **GBM ฉีก** RBC ลอดออกแล้วผ่านท่อไต (หัวข้อ 5) |
| **Proteinuria ไม่มาก** | podocyte ไม่ได้เป็นเป้าหลัก และ GFR ที่ลดทำให้ปริมาณที่กรองลดด้วย |

### RPGN — crescent เกิดอย่างไร
เมื่อการอักเสบรุนแรงจน **GBM ฉีกเป็นรู** → fibrin และโปรตีนพลาสมาทะลักเข้า **Bowman space** → กระตุ้น **parietal epithelial cell** แบ่งตัวร่วมกับ macrophage เป็นชั้นรูปพระจันทร์เสี้ยว (**cellular crescent**) → **เบียดกระจุกหลอดเลือด** และปิดทางออกสู่ท่อไต → GFR ลดเร็วมาก ถ้าปล่อยไว้ crescent จะกลายเป็น **fibrocellular → fibrous** ซึ่งไม่กลับคืน — จึงต้อง **วินิจฉัยและรักษาภายในวัน–สัปดาห์**

RPGN แบ่งตาม **immunofluorescence** เป็น 3 กลไก

[[fig:ifpat]]

| แบบ | IF | ตัวอย่าง | เบาะแส |
|---|---|---|---|
| **Anti-GBM** | **linear** IgG ตาม GBM | Goodpasture | **ไอเป็นเลือด** — แอนติเจนเป้าหมาย (α3 ของ type IV collagen) มีทั้งใน GBM และ **alveolar basement membrane** · สูบบุหรี่เผยแอนติเจนในปอด |
| **Immune complex** | **granular** | PSGN · IgAN · LN · MPGN | C3 ต่ำ (PSGN, LN, MPGN) · ANA/anti-dsDNA · ASO |
| **Pauci-immune** | แทบไม่ติดสี | **ANCA** (MPO, PR3) | ไซนัส ปอด ผื่น เส้นประสาท · อายุมาก |

การรักษา (อิง KDIGO 2024 ANCA vasculitis และ KDIGO 2021 — สไลด์ระบุเพียงชื่อกลุ่ม): **methylprednisolone pulse** + **cyclophosphamide หรือ rituximab** · **plasma exchange** ใน anti-GBM · เจาะไตโดยเร็วแต่ไม่ต้องรอผลก่อนเริ่มยาถ้าภาพชัด

### Chronic GN (CGN)
ไตเสื่อมช้า > 3 เดือน · proteinuria และ/หรือ glomerular hematuria · ความดันสูง · **ไตเล็ก** หรือ glomerulosclerosis รุนแรง (สไลด์) — ถ้าอัลตราซาวนด์พบไตเล็ก เนื้อไตบาง **การเจาะไตมักไม่ช่วย** (เห็นแต่แผลเป็น) และเลือดออกง่าย การดูแลคือชะลอไตเสื่อมแบบ CKD
""",
    ["Nephritic: เซลล์อักเสบอุดช่องหลอดเลือด → GFR ลด · ท่อไตยังดูด Na → HT บวม (overfill)",
     "RPGN: GBM ฉีก → fibrin เข้า Bowman space → crescent เบียด tuft — fibrous แล้วไม่กลับ",
     "IF: linear = anti-GBM · granular = immune complex · pauci-immune = ANCA",
     "Anti-GBM ไอเป็นเลือดเพราะแอนติเจนเดียวกันอยู่ที่ alveolar BM",
     "CGN ไตเล็ก — ไม่เจาะไต"],
    [mcq(N(14), "A 68-year-old woman has chronic sinusitis, creatinine rising from 1.0 to 3.1 mg/dL over 4 weeks and red cell casts. Kidney biopsy shows crescents in 60% of glomeruli with little or no immunoglobulin or complement staining. Which test is most likely positive?",
         ["Anti-glomerular basement membrane antibody", "Antistreptolysin O titer with low C3", "Anti-phospholipase A2 receptor antibody", "Antineutrophil cytoplasmic antibody", "Serum IgA with mesangial deposits"], 3,
         "crescentic GN ที่ IF **แทบไม่ติดสี = pauci-immune** — เกือบทั้งหมดเป็น **ANCA-associated vasculitis** (MPO หรือ PR3) ภาพไซนัสเรื้อรังเข้ากับ granulomatosis with polyangiitis\n\n- **Anti-GBM** ให้ **linear IgG**\n- **PSGN** ให้ granular IgG/C3\n- **Anti-PLA2R** เป็นของ membranous nephropathy (nephrotic ไม่ใช่ crescent)\n- **IgAN** เห็น mesangial IgA ชัด ไม่ใช่ pauci-immune",
         "crescent + IF ว่าง = pauci-immune = ANCA", "RPGN", ["สไลด์ พญ.ฉันทิศา — morphological diagnosis: ANCA, anti-GBM; KDIGO 2024 AAV"], [AGN, "B5.2.2-3(6)"]),
     mcq(N(15), "A 45-year-old man has hypertension, creatinine 4.8 mg/dL that has been rising for 3 years, urine protein 2.5 g/day and dysmorphic hematuria. Ultrasound shows both kidneys measuring 8 cm with thin echogenic cortex. What is the most appropriate next step?",
         ["Urgent kidney biopsy to identify the primary glomerulonephritis", "Pulse methylprednisolone followed by cyclophosphamide", "CKD care: BP control, RAS blockade as tolerated and preparation for kidney replacement therapy, without biopsy", "Plasma exchange", "Repeat ultrasound in 1 week to see if the kidneys enlarge"], 2,
         "ภาพนี้คือ **chronic GN** — ไตเสื่อมช้า > 3 เดือน และ **ไตเล็ก เนื้อไตบางและสว่าง** (แผลเป็น) สไลด์ระบุว่า CGN มี small kidney/severe glomerulosclerosis การเจาะไตตอนนี้จะเห็นแต่แผลเป็น ไม่เปลี่ยนการรักษา และเสี่ยงเลือดออก จึงดูแลแบบ **CKD** และเตรียมบำบัดทดแทนไต\n\n- ยากดภูมิแรง ๆ และ plasma exchange ไม่ช่วยแผลเป็นที่ไม่กลับคืน\n- ไตเล็กไม่โตกลับมา",
         "ไตเล็ก + เสื่อม > 3 เดือน = CGN → ดูแลแบบ CKD ไม่เจาะไต", "CGN", R("Chronic glomerulonephritis"), [CGN, "2.3.14(3)", "B9.2.7(2)"])],
    [AGN, CGN, "B9.2.7(1)", "B5.2.2-3(6)", "2.1.44"],
    {"glomx": fig("Glomerulus ปกติ · nephritic · RPGN",
        "**ปกติ** — ช่องหลอดเลือดฝอยเปิดกว้าง · **Nephritic** — เซลล์อักเสบและเซลล์ที่แบ่งตัวอุดช่องหลอดเลือด GFR จึงลด · **RPGN** — fibrin ทะลัก GBM ที่ฉีกเข้า Bowman space จนเซลล์บุผนังแบ่งตัวเป็น **crescent** (สีเหลือง) เบียดกระจุกหลอดเลือดให้เล็กลง",
        F.glomx()),
     "ifpat": fig("Immunofluorescence 3 แบบ บอกกลไกของ RPGN",
        "**Linear** — แอนติบอดีจับ GBM เองทั้งแผ่น (anti-GBM) · **Granular** — immune complex เป็นก้อน ๆ (PSGN, IgAN, LN, MPGN) · **Pauci-immune** — แทบไม่มี immunoglobulin เพราะความเสียหายมาจาก neutrophil ที่ถูก ANCA กระตุ้น",
        F.ifpat())})

# ═══════════════════════════ END SECTIONS
