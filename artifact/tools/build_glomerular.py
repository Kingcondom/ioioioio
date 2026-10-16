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

# ───────────────────────────── 9
sec("neph-gn-09", "Podocytopathy — minimal change disease และ FSGS",
    "MCD: บวมทันที ไม่อักเสบ ตอบ steroid · FSGS: แผลเป็นเป็นหย่อม — ปฐมภูมิ ปรับตัว ไวรัส ยา", 12,
"""[[fig:fp]]

### Minimal change disease (MCD) — สไลด์
| ประเด็น | รายละเอียด |
|---|---|
| ใครเป็น | **เด็ก > ผู้ใหญ่** (ชาย > หญิง) · **70% ของเนโฟรติกในเด็ก < 10 ปี** · **10–15% ในผู้ใหญ่** · มีสองช่วงอายุ (เด็กเล็กและผู้สูงอายุ) |
| อาการ | **เริ่มทันที (abrupt)** · โปรตีนรั่วมาก (ลายมือ: *massive*) · albumin **< 3.0 g/dL** · ไขมันสูง · **แทบไม่มีสัญญาณ GN** (ความดันสูง hematuria Cr ขึ้น) |
| พยาธิ | LM **ปกติ** · IF **ไม่ติดสี** · EM **foot process หลอมรวมทั่วทั้ง glomerulus ไม่มี deposit** |

#### ทำไม MCD ถึงเป็นแบบนี้
| ลักษณะ | กลไก |
|---|---|
| บวมเร็วภายในวัน–สัปดาห์ | podocyte เสียหน้าที่ทันทีทั้งไต (ไม่ต้องรอ deposit สะสม) → albumin รั่วมากทันที |
| ไม่มี hematuria ไม่มีความดันสูง | **ไม่มีการอักเสบ** และ GBM ไม่ฉีก — เป็นปัญหาของ podocyte ล้วน |
| LM ปกติแต่ EM ผิดปกติ | foot process แผ่แบนเล็กเกินกว่ากล้องธรรมดาจะเห็น |
| โปรตีนรั่วเป็น albumin เกือบล้วน (selective) | ตะแกรงเสียแค่ด่าน podocyte โปรตีนก้อนใหญ่ (IgG) ยังถูกกัน |
| ตอบ steroid ดีมาก | podocyte ไม่ได้ตาย กลับมาเรียงตัวได้ · งานวิจัยใหม่พบ **แอนติบอดีต่อ nephrin** (โปรตีนของ slit diaphragm) ในผู้ป่วย MCD จำนวนมาก (NEJM 2024) และสาเหตุทุติยภูมิหลายตัวเป็นโรคของระบบภูมิคุ้มกัน (Hodgkin, ภูมิแพ้) |

**สาเหตุทุติยภูมิของ MCD (สไลด์ อ้าง Brenner & Rector)** — ติดเชื้อไวรัส (ลายมือ: HBV/HCV/HIV) และปรสิต · **NSAIDs** ☆ · gold, lithium, interferon · ampicillin, rifampin · **Hodgkin** ☆, lymphoma/leukemia, มะเร็งก้อน · **ภูมิแพ้** อาหาร ฝุ่น ผึ้งต่อย เกสร poison ivy · dermatitis herpetiformis · SLE · หลังปลูกถ่ายไขกระดูก

**การรักษา MCD (สไลด์ — KDIGO 2012; KDIGO 2021 คงหลักเดิม)**
- **Prednisolone 1 mg/kg/วัน (สูงสุด 80 มก.) วันละครั้ง** หรือ **2 mg/kg วันเว้นวัน (สูงสุด 120 มก.)**
- ขนาดสูงอย่างน้อย **4 สัปดาห์** และนานสุด **16 สัปดาห์** ถ้ายังไม่ complete remission
- หลัง remission **ค่อย ๆ ลด 5–10 มก./สัปดาห์** รวมระยะเวลาถึง **6 เดือน**
- กำเริบบ่อยหรือพึ่ง steroid → calcineurin inhibitor, rituximab, cyclophosphamide หรือ MMF (KDIGO 2021)

> เด็กเนโฟรติกแบบฉบับ (อายุ 1–10 ปี ไม่มี hematuria ความดันปกติ C3 ปกติ) ให้ steroid ได้เลยโดยไม่ต้องเจาะไต เพราะเกือบทั้งหมดเป็น MCD — ผู้ใหญ่ต้องหาสาเหตุทุติยภูมิและเจาะไตก่อน

### Focal segmental glomerulosclerosis (FSGS) — สไลด์
| ประเด็น | รายละเอียด |
|---|---|
| อาการ | เริ่มทันทีหรือค่อยเป็น · โปรตีน 1–2 ถึง > 10 g/วัน · **nephrotic 60–75%** · **ความดันสูง 45–65%** · micro hematuria 30–50% · ไตเสื่อม 25–50% (ลายมือ: *Nephro–Nephri* — มาได้ทั้งสองแบบ) |
| พยาธิ | LM **segmental sclerosis** (ชนิด NOS พบบ่อยสุด) · IF ปกติ หรือ IgM, C1q, C3 เฉพาะตรงแผลเป็น · EM foot process effacement มากน้อยตามชนิด |

| ชนิด | กลไก | ตัวอย่าง (สไลด์) |
|---|---|---|
| ปฐมภูมิ | สารในเลือดที่ทำร้าย podocyte ทั่วไต → effacement ทั่ว · nephrotic เต็มรูปแบบ | — |
| **ไวรัส** | ไวรัสทำให้ podocyte แบ่งตัวผิดปกติ → **collapsing** FSGS | **HIV**, CMV, parvovirus B19 |
| **ยา** | พิษต่อ podocyte | **pamidronate**, interferon, **anabolic steroid** · เฮโรอีน |
| **ปรับตัว (adaptive)** | nephron ที่เหลือต้อง **กรองหนัก (hyperfiltration)** → glomerulus โต podocyte ถูกยืดจนคลุมไม่พอ หลุดลอก → แผลเป็น | **อ้วนมาก** · sickle cell · หัวใจพิการแต่กำเนิดชนิดเขียว · โรคปอดที่ขาดออกซิเจน · ไตข้างเดียว · oligomeganephronia · reflux nephropathy · หลัง cortical necrosis · หลังตัดไต |

[[fig:fsgs]]

#### ทำไม FSGS ถึงมีความดันสูงและ hematuria มากกว่า MCD
แผลเป็นทำให้ nephron หายไปจริง GFR จึงลดและไตเก็บโซเดียม · FSGS แบบปรับตัวมัก **โปรตีนรั่วไม่ถึงขั้นเนโฟรติกและ albumin ปกติ** เพราะ podocyte เสียเป็นหย่อม ๆ — ต่างจาก MCD ที่เสียทั่วไตพร้อมกัน · **collapsing FSGS จาก HIV** ไตจะ **ใหญ่และสว่าง** บนอัลตราซาวนด์แม้ไตวายมาก

**รักษา**: ชนิดปรับตัว → ACEi/ARB ลดแรงดันใน glomerulus + ลดน้ำหนัก **ไม่ให้ steroid** · ชนิดปฐมภูมิ → steroid ขนาดสูง ถ้าไม่ตอบใช้ CNI · ชนิดไวรัส → รักษาไวรัส (ART ใน HIV) (KDIGO 2021 — สไลด์ไม่ได้ระบุ)
""",
    ["MCD: เด็ก < 10 ปี 70% · บวมทันที · LM ปกติ IF ลบ EM foot process หลอมรวม · ไม่มี GN signs",
     "MCD secondary: NSAIDs · Hodgkin · ภูมิแพ้ · ไวรัส · lithium/gold/interferon",
     "Pred 1 mg/kg/วัน (max 80) หรือ 2 mg/kg วันเว้นวัน (max 120) · 4–16 สัปดาห์ · ลด 5–10 มก./สัปดาห์ รวม 6 เดือน",
     "FSGS: nephrotic 60–75% · HT 45–65% · secondary = HIV/CMV/parvo · pamidronate/anabolic · อ้วน/nephron น้อย",
     "FSGS ปรับตัว = hyperfiltration → ACEi/ARB + ลดน้ำหนัก ไม่ใช่ steroid · HIV collapsing ไตใหญ่สว่าง"],
    [mcq(N(16), "A 38-year-old man with BMI 46 kg/m² has urine protein 2.6 g/day, serum albumin 3.9 g/dL, no edema and creatinine 1.3 mg/dL. Biopsy shows perihilar segmental sclerosis with enlarged glomeruli and only segmental foot-process effacement. What is the best management?",
         ["High-dose prednisolone for 16 weeks", "Cyclophosphamide with steroids", "RAS blockade and weight reduction", "Plasma exchange", "Rituximab"], 2,
         "ภาพนี้คือ **FSGS แบบปรับตัว (adaptive)** จากอ้วนมาก — nephron ทำงานหนักเกิน (hyperfiltration) glomerulus โต podocyte หลุดเป็นหย่อม โปรตีนรั่วไม่ถึงขั้น nephrotic และ **albumin ปกติ** ซึ่งต่างจาก FSGS ปฐมภูมิ การรักษาคือ **ลดแรงดันใน glomerulus ด้วย ACEi/ARB และลดน้ำหนัก**\n\n- **Steroid, cyclophosphamide, rituximab** ใช้กับโรคที่มีภูมิคุ้มกันเป็นตัวขับ ไม่ช่วยและเพิ่มผลเสียในชนิดปรับตัว\n- **Plasma exchange** ใช้ใน anti-GBM หรือ FSGS ที่กลับเป็นซ้ำหลังปลูกถ่ายไต",
         "FSGS + อ้วน + albumin ปกติ + effacement เป็นหย่อม = adaptive → ACEi/ARB + ลดน้ำหนัก", "FSGS", R("FSGS secondary causes: reduced nephron numbers, morbid obesity"), [NS, "B9.2.2(4)"]),
     mcq(N(17), "A 70-kg 30-year-old man has biopsy-proven minimal change disease. According to the dosing in the lecture (KDIGO), which initial regimen is correct?",
         ["Prednisolone 35 mg daily for 2 weeks then stop", "Prednisolone 70 mg daily for at least 4 weeks (up to 16 weeks if not in complete remission), then taper", "Prednisolone 140 mg daily for 4 weeks", "Prednisolone 80 mg on alternate days for 6 months without taper", "Methylprednisolone 1 g IV daily for 3 days only"], 1,
         "สไลด์ (KDIGO): **prednisolone 1 mg/kg/วัน สูงสุด 80 มก.** → 70 กก. = **70 มก./วัน** (หรือ 2 mg/kg วันเว้นวัน สูงสุด 120 มก.) ให้ขนาดสูง **อย่างน้อย 4 สัปดาห์** ถ้ายังไม่ complete remission ให้ต่อได้ถึง **16 สัปดาห์** แล้ว **ลด 5–10 มก./สัปดาห์** รวมถึง 6 เดือนหลัง remission\n\n- 35 มก. 2 สัปดาห์ ขนาดและเวลาไม่พอ เสี่ยงกำเริบ\n- 140 มก./วัน เกินขนาดสูงสุด\n- 80 มก. วันเว้นวัน ต่ำกว่า 2 mg/kg และหยุดทันทีไม่ได้\n- pulse methylprednisolone ใช้กับ RPGN ไม่ใช่ MCD",
         "MCD: 1 mg/kg/วัน (max 80) ≥ 4 สัปดาห์ ถึง 16 สัปดาห์ → ลด 5–10 มก./สัปดาห์", "MCD treatment", R("MCD treatment — KDIGO 2012"), [NS])],
    [NS, "B9.2.2(4)"],
    {"fp": fig("Podocyte ปกติ เทียบกับ foot process effacement",
        "ปกติ foot process ของ podocyte เรียงสลับเป็นซี่ ระหว่างซี่มี **slit diaphragm** กัน albumin ไว้ · ใน **MCD และ FSGS** foot process แผ่แบนรวมเป็นแผ่นเดียว slit diaphragm หาย albumin จึงรั่วออกมาก — มองไม่เห็นใน LM ต้องใช้ **EM**",
        F.fp()),
     "fsgs": fig("FSGS แบบปรับตัว — วงจรที่เร่งตัวเอง",
        "เมื่อ nephron เหลือน้อย ที่เหลือต้องกรองหนักจน glomerulus โต podocyte ซึ่งแบ่งตัวไม่ได้ถูกยืดจนคลุมไม่พอและหลุดลอก เกิดแผลเป็นเป็นหย่อม (segmental sclerosis) nephron จึงตายเพิ่ม — **ACEi/ARB** ตัดวงจรโดยลดแรงดันใน glomerulus (กลไกเดียวกับ hyperfiltration ระยะแรกของเบาหวาน)",
        F.fsgs())})

# ───────────────────────────── 10
sec("neph-gn-10", "Membranous nephropathy — nephrotic ของผู้ใหญ่ ที่ต้องคิดถึงมะเร็งและลิ่มเลือด",
    "anti-PLA2R · subepithelial deposit · spike · rule of thirds · RVT · หาสาเหตุทุติยภูมิ · รักษาตามความเสี่ยง", 11,
"""### ลักษณะทางคลินิก (สไลด์)
| ประเด็น | รายละเอียด |
|---|---|
| ใครเป็น | ผู้ใหญ่ **> 40 ปี** (30–50) · **ชาย : หญิง = 2–3 : 1** |
| อาการ | **> 80% โปรตีน > 3 g/วัน** · **ค่อยเป็นค่อยไปเกือบทุกราย** · **ตะกอนใส** · micro hematuria 30–40% · ความดันสูง 15–55% · ไตปกติหรือลดเล็กน้อย · albumin ต่ำ LDL/VLDL สูง |
| ภาวะแทรกซ้อน | **thromboembolism — RVT, PE, DVT** · **ความเสี่ยงมะเร็งเพิ่มตามอายุ** |
| การดำเนินโรค | **หายเอง 30% · คงที่ 30% · แย่ลง 30%** (rule of thirds) |
| พยาธิ | LM **GBM หนาทั่ว** + **spike** · IF **granular IgG + C3 ตามผนังหลอดเลือด** · EM **subepithelial electron-dense deposit** |

### กลไก — ทำไม MN ถึงรั่วมากแต่ตะกอนใส
[[fig:mnspike]]

ใน MN ปฐมภูมิ แอนติบอดี (ส่วนใหญ่ **anti-PLA2R** ราว 70–80% · ส่วนน้อย THSD7A) จับกับแอนติเจนที่อยู่บนผิว **podocyte** โดยตรง immune complex จึง **ก่อตัวตรงนั้น (in situ)** ใต้ podocyte → complement ถูกกระตุ้นจนเกิด **membrane attack complex (C5b-9)** เจาะ podocyte → โปรตีนรั่ว — แต่ทุกอย่างอยู่ **นอก GBM ด้านปัสสาวะ** neutrophil ในเลือดเข้าไม่ถึง จึง **ไม่มีการอักเสบ ตะกอนใส** และ GBM ตอบสนองโดยงอกแทรกระหว่างก้อน (spike) จนคลุมหนาทั้งแผ่น

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก |
|---|---|
| **ค่อยเป็นค่อยไป** (ต่างจาก MCD) | deposit ต้องสะสมใต้ podocyte ทีละน้อยก่อนความเสียหายจะมากพอ |
| **ลิ่มเลือดบ่อยที่สุดในบรรดา nephrotic** — RVT | โปรตีนรั่วมากและนาน + antithrombin III รั่ว + fibrinogen สูง · albumin < 2.5 g/dL เสี่ยงสูงขึ้นชัด · **RVT**: ปวดสีข้างเฉียบพลัน hematuria โปรตีนเพิ่ม Cr ขึ้น varicocele ซ้าย · หลุดไปปอดเป็น PE |
| **สัมพันธ์กับมะเร็ง** | แอนติเจนจากก้อนมะเร็งกลายเป็นเป้าของ immune complex (ทุติยภูมิ) — anti-PLA2R มักลบ |

### MN ทุติยภูมิ — ต้องหาเสมอ (สไลด์)
| กลุ่ม | ตัวอย่าง |
|---|---|
| ติดเชื้อ | **HBV**, HCV, HIV, ปรสิต (filariasis, schistosomiasis, malaria), เรื้อน, **ซิฟิลิส** |
| มะเร็ง | ก้อน — **ปอด 26%** · ต่อมลูกหมาก 15% · โลหิตวิทยา 14% · **ลำไส้ใหญ่ 11%** · melanoma ฯลฯ |
| ภูมิต้านตนเอง | **SLE (class V)** · thyroiditis · RA · Sjögren · IgG4 disease |
| ยา/สารพิษ | **NSAIDs/COX-2** · gold · penicillamine · **captopril** · anti-TNF · ปรอท · lithium · มลพิษอากาศ |

**ชุดตรวจหาสาเหตุ (ตาราง KDIGO 2021 ในสไลด์เป็นภาพ — สรุปจากแนวทาง)**: **anti-PLA2R** · HBsAg, anti-HCV, anti-HIV, VDRL · ANA, anti-dsDNA, C3/C4 · ประวัติยา · คัดกรองมะเร็งตามอายุและเพศ (CXR หรือ CT ทรวงอก · ส่องกล้องลำไส้ · แมมโมแกรม · PSA) — ถ้า **anti-PLA2R บวก** และภาพเข้ากับ MN ปฐมภูมิ KDIGO 2021 ระบุว่าวินิจฉัยได้โดย **ไม่ต้องเจาะไต**

### การรักษา (อัลกอริทึมในสไลด์เป็นภาพ — สรุปจาก KDIGO 2021)
| ความเสี่ยงที่ไตจะเสื่อม | ลักษณะ (ย่อ) | การรักษา |
|---|---|---|
| ต่ำ | eGFR ปกติ · โปรตีน < 3.5 g/วัน · albumin > 3 g/dL | **supportive** — ACEi/ARB คุมความดัน รอ remission เอง |
| ปานกลาง | eGFR ปกติ · โปรตีน > 4 g/วัน และไม่ลดลง > 50% หลัง supportive 6 เดือน | **rituximab** หรือ calcineurin inhibitor |
| สูง | eGFR < 60 และ/หรือ โปรตีน > 8 g/วัน นานกว่า 6 เดือน · หรือ anti-PLA2R สูงมาก albumin ต่ำมาก | **rituximab** หรือ **cyclophosphamide + steroid** |
| สูงมาก | nephrotic รุนแรงคุกคามชีวิต · ไตเสื่อมเร็วโดยไม่มีสาเหตุอื่น | **cyclophosphamide + steroid** |
**Anticoagulant ป้องกัน**: เมื่อ albumin ต่ำมาก (< 2–2.5 g/dL) ร่วมกับปัจจัยเสี่ยงอื่น และเลือดออกง่ายต่ำ
""",
    ["MN: ผู้ใหญ่ > 40 ปี ชาย 2–3 : 1 · > 80% โปรตีน > 3 g · ค่อยเป็น · ตะกอนใส",
     "Anti-PLA2R ~70–80% ของ MN ปฐมภูมิ — complex ก่อตัวใต้ podocyte → C5b-9 → รั่วแต่ไม่อักเสบ",
     "LM GBM หนา + spike · IF granular IgG/C3 · EM subepithelial deposit",
     "Rule of thirds: หายเอง 30% · คงที่ 30% · แย่ลง 30% · เสี่ยง RVT สูงสุด",
     "หาสาเหตุทุติยภูมิ: HBV · มะเร็ง (ปอด ลำไส้) · SLE class V · NSAIDs/captopril"],
    [mcq(N(18), "A 56-year-old man with membranous nephropathy (albumin 1.7 g/dL, urine protein 11 g/day) suddenly develops left flank pain, gross hematuria and a new left-sided varicocele; creatinine rises from 1.0 to 1.7 mg/dL. Which complication is most likely?",
         ["Nephrolithiasis with obstruction", "Renal vein thrombosis", "Acute pyelonephritis", "Transformation to crescentic glomerulonephritis", "Testicular torsion"], 1,
         "**Renal vein thrombosis** — MN เป็น nephrotic ที่เสี่ยงลิ่มเลือดสูงสุด (albumin < 2 g/dL เสี่ยงยิ่งขึ้น) RVT ข้างซ้ายทำให้ **varicocele ซ้าย** เพราะหลอดเลือดดำอัณฑะซ้ายเทเข้า renal vein ซ้าย ร่วมกับปวดสีข้าง hematuria และไตแย่ลง → ยืนยันด้วย Doppler US หรือ CT venography แล้วให้ anticoagulant\n\n- นิ่วไม่อธิบาย varicocele\n- pyelonephritis ต้องมีไข้ ปัสสาวะแสบขัด\n- crescentic GN ไม่ทำให้ปวดสีข้างเฉียบพลันและ varicocele\n- testicular torsion ปวดอัณฑะเฉียบพลัน ไม่ใช่ varicocele + hematuria",
         "MN + ปวดสีข้าง + hematuria + varicocele ซ้าย = RVT", "MN complications", R("MN: thromboembolic manifestation (RVT, PE, DVT)"), [NS, "2.3.9(2)"]),
     mcq(N(19), "A 47-year-old woman has nephrotic syndrome with normal eGFR, bland sediment and a strongly positive serum anti-PLA2R antibody. HBV, HCV, HIV, ANA and age-appropriate cancer screening are negative. According to KDIGO 2021, what is the status of kidney biopsy?",
         ["Biopsy is mandatory before any treatment", "Biopsy is not required to diagnose primary membranous nephropathy in this setting", "Biopsy is contraindicated in all nephrotic patients", "Biopsy should be replaced by anti-GBM testing", "Biopsy is required only if C3 is low"], 1,
         "KDIGO 2021: ผู้ป่วยเนโฟรติกที่ **anti-PLA2R บวก** และภาพทางคลินิกเข้ากับ MN ปฐมภูมิ (ตรวจหาสาเหตุทุติยภูมิแล้วไม่พบ) **วินิจฉัย MN ได้โดยไม่ต้องเจาะไต** — แต่ถ้า eGFR ลดหรือภาพไม่ตรงยังควรเจาะเพื่อหาโรคร่วม\n\n- ไม่ได้ห้ามเจาะไตในเนโฟรติกทุกราย\n- anti-GBM ไม่เกี่ยวกับ MN\n- C3 ต่ำชี้ไปทาง LN/MPGN ไม่ใช่เงื่อนไขของ MN",
         "anti-PLA2R บวก + ภาพเข้ากับ MN ปฐมภูมิ → วินิจฉัยได้โดยไม่ต้องเจาะไต (KDIGO 2021)", "MN diagnosis", ["KDIGO 2021 Glomerular Diseases — ตาราง/อัลกอริทึม MN ในสไลด์เป็นภาพ"], [NS, "B1.6.1(1)"])],
    [NS, "B9.2.2(4)", "2.3.9(2)"],
    {"mnspike": fig("Membranous nephropathy — จาก immune complex ใต้ podocyte ถึง GBM หนา",
        "① แอนติบอดี (anti-PLA2R) จับแอนติเจนบน podocyte → immune complex ก่อตัวใต้ podocyte · ② GBM งอกแทรกระหว่างก้อน เห็นเป็น **spike** ใน silver stain · ③ GBM คลุมก้อนจนหนาทั้งแผ่น — ทุกอย่างอยู่ **นอก GBM ด้านปัสสาวะ** จึงรั่วมากแต่ไม่อักเสบ",
        F.mnspike())})

# ───────────────────────────── 11
sec("neph-gn-11", "IgA nephropathy — เลือดออกตามหลังเจ็บคอใน 1–2 วัน",
    "Gd-IgA1 4 ขั้น · synpharyngitic hematuria · C3 ปกติ · mesangial IgA · รักษาด้วย ACEi/ARB", 10,
"""### ลักษณะทางคลินิก (สไลด์)
| แบบที่มา | สัดส่วน |
|---|---|
| **ปัสสาวะเป็นเลือดเห็นด้วยตาเป็นพัก ๆ หลังติดเชื้อเยื่อบุ** (synpharyngitic) | **40–50%** |
| micro hematuria ± proteinuria (เจอจากตรวจสุขภาพ) | 30–40% |
| Nephrotic syndrome | 5% |
| RPGN | < 10% |

**โรคที่พบร่วม (สไลด์)**: ankylosing spondylitis · RA · Reiter · uveitis · **celiac** · **โรคตับจากแอลกอฮอล์/ตับแข็ง** · schistosomiasis ตับ · sarcoid · dermatitis herpetiformis · **HIV, HBV** (ถิ่นระบาด)
**พยาธิ**: LM **mesangial expansion และ hypercellularity** · IF **mesangial IgA** · EM **mesangial deposit**

### กลไก 4 ขั้น — ทำไมเลือดออกเร็วหลังเจ็บคอ
[[fig:igan]]

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก |
|---|---|
| **เลือดออกภายใน 1–2 วัน หลังเจ็บคอ/ท้องเสีย** | เยื่อบุที่ติดเชื้อสร้าง **IgA1 ชนิดขาด galactose** เพิ่มขึ้น **ทันที** → immune complex ที่มีอยู่แล้วเพิ่มและไปติด mesangium — ไม่ต้องรอสร้างแอนติบอดีใหม่ |
| **Hematuria เด่น โปรตีนไม่มาก** | deposit อยู่ที่ **mesangium** → mesangial cell แบ่งตัว ทำให้ผนังหลอดเลือดฝอยรอบ ๆ เปราะและฉีกเป็นจุด ๆ ส่วน podocyte ยังดี |
| **C3 ในเลือดปกติ** | complement ถูกกระตุ้นเฉพาะที่ใน glomerulus (alternative/lectin pathway) ไม่ได้ถูกใช้หมดทั้งร่างกาย — ใช้แยกจาก PSGN และ LN |
| สัมพันธ์กับโรคตับ ลำไส้ | ตับเป็นที่กำจัด IgA complex (ตับแข็งกำจัดไม่ได้) · โรคลำไส้กระตุ้นการสร้าง IgA ที่เยื่อบุ |

### การรักษา
**สไลด์ (KDIGO 2012)**
- **ACEi หรือ ARB ระยะยาว** เมื่อโปรตีน **> 1 g/วัน** ปรับขนาดขึ้นตามความดัน (1B) — ไต่ขนาดให้โปรตีน **< 1 g/วัน** (2C)
- **Fish oil** เมื่อโปรตีนยัง > 1 g/วัน หลัง supportive ดีที่สุด 3–6 เดือน (2D)
- **Corticosteroid 6 เดือน** เมื่อโปรตีนยัง > 1 g/วัน หลัง supportive 3–6 เดือน **และ GFR > 50** (2C)

**แนวทางปัจจุบัน — KDIGO 2025 (ไม่ได้อยู่ในสไลด์)**: เป้าหมายโปรตีน **< 0.5 g/วัน (ดีที่สุด < 0.3)** · supportive: RAS blockade ขนาดสูงสุดที่ทนได้ หรือ **sparsentan** + **SGLT2 inhibitor** + คุมความดัน · ยาลดการสร้าง Gd-IgA1: **budesonide ชนิดออกฤทธิ์ที่ลำไส้ (targeted-release)** หรือ steroid ระบบในผู้ที่เสี่ยงสูง
""",
    ["IgAN: macroscopic hematuria หลังติดเชื้อเยื่อบุ 40–50% · micro ± protein 30–40% · nephrotic 5% · RPGN < 10%",
     "Synpharyngitic = เลือดออก 1–2 วันหลังเจ็บคอ (PSGN ต้องรอ 2–4 สัปดาห์)",
     "Gd-IgA1 → anti-glycan IgG → immune complex → mesangium · C3 ปกติ",
     "พยาธิ: mesangial hypercellularity + mesangial IgA",
     "KDIGO 2012 (สไลด์): ACEi/ARB ถ้า > 1 g ให้ < 1 g · steroid 6 เดือนถ้ายัง > 1 g และ GFR > 50 · KDIGO 2025 เป้า < 0.5 g"],
    [mcq(N(20), "Which sequence best describes the pathogenesis of IgA nephropathy?",
         ["Anti-PLA2R antibodies bind podocytes and form subepithelial immune complexes", "Galactose-deficient IgA1 is recognized by IgG autoantibodies, forming immune complexes that deposit in the mesangium", "Streptococcal antigens planted in the glomerulus bind antibody 2–4 weeks after infection", "Autoantibodies against type IV collagen bind the GBM in a linear pattern", "ANCA-activated neutrophils cause pauci-immune necrotizing lesions"], 1,
         "IgAN เกิดจาก 4 ขั้น: ① **IgA1 ขาด galactose (Gd-IgA1)** จากเยื่อบุ ② ร่างกายสร้าง **IgG ต่อต้าน Gd-IgA1** ③ รวมเป็น **immune complex** ในเลือด ④ ไปติดที่ **mesangium** → mesangial cell แบ่งตัวและ complement ถูกกระตุ้นเฉพาะที่\n\n- **anti-PLA2R** = membranous nephropathy\n- **แอนติเจน strep** = PSGN\n- **anti-type IV collagen** = anti-GBM\n- **ANCA** = pauci-immune vasculitis",
         "IgAN = Gd-IgA1 + anti-glycan IgG → mesangial deposit", "IgAN", ["หลักพยาธิกำเนิด (KDIGO 2025) — สไลด์แสดง LM/IF/EM"], [AGN])],
    [AGN, "2.1.43"],
    {"igan": fig("IgA nephropathy เกิดเป็น 4 ขั้น",
        "เยื่อบุสร้าง **IgA1 ที่ขาด galactose** → ร่างกายมองเป็นสิ่งแปลกปลอมและสร้าง **IgG** มาจับ → เป็น **immune complex** → ไปติดที่ **mesangium** เมื่อติดเชื้อทางเดินหายใจ เยื่อบุสร้าง IgA1 เพิ่มทันที เลือดในปัสสาวะจึงตามมาใน 1–2 วัน",
        F.igan())})

# ───────────────────────────── 12
sec("neph-gn-12", "Post-streptococcal GN — nephritic ต้นแบบ",
    "latency 2–4 / 4–6 สัปดาห์ · C3 ต่ำ C4 ปกติ กลับใน 8–10 สัปดาห์ · hump · รักษาประคับประคอง", 11,
"""### ลักษณะทางคลินิก (สไลด์)
| ประเด็น | รายละเอียด |
|---|---|
| การเริ่ม | acute nephritic มัก **< 2 สัปดาห์** · **4–6 สัปดาห์หลังติดเชื้อผิวหนัง** · **2–4 สัปดาห์หลังคออักเสบ** |
| อาการ | **gross hematuria** (microscopic 100%) · **ความดันสูง 60–80%** · **บวม/volume เกิน (หัวใจล้มเหลว) 80–90%** · oliguria 10–58% · nephrotic range ได้ราว 20% |
| Complement | **ต่ำ 90%** · **C3 และ CH50 ลดลงภายใน 2 สัปดาห์** · **C4 มักปกติ** · **กลับปกติใน 8–10 สัปดาห์** |
| แอนติบอดี | **ASO 30%** · **anti-DNase B 70%** |
| พยาธิ | LM **exudative / endocapillary proliferative GN มี neutrophil** · IF **coarse granular IgG + C3** · EM **subepithelial hump** |

[[fig:psgn]]

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก |
|---|---|
| **อาการไตตามหลังติดเชื้อหลายสัปดาห์** (latency) | ต้องรอให้ร่างกาย **สร้างแอนติบอดี** ต่อแอนติเจนของ strep ที่ไปฝังใน glomerulus ก่อน — ต่างจาก IgAN ที่เลือดออกใน 1–2 วัน |
| **C3 ต่ำ C4 ปกติ** | complement ถูกกระตุ้นทาง **alternative pathway** (ไม่ผ่าน C4) และถูกใช้มากจนระดับในเลือดลด |
| **ปัสสาวะสีโค้ก + RBC cast** | neutrophil และการแบ่งตัวของเซลล์ทำให้ GBM ฉีก |
| **ความดันสูง ปวดศีรษะ บวมหน้า หอบ** | GFR ลดจากหลอดเลือดฝอยถูกอุด แต่ท่อไตยังดูดโซเดียม → **volume เกิน (overfill)** renin ต่ำ — ความดันอาจสูงจน **hypertensive encephalopathy** |
| **ASO บวกน้อยหลังติดเชื้อผิวหนัง** | streptolysin O ถูกไขมันในผิวหนังจับไว้ภูมิจึงไม่ค่อยขึ้น → ใช้ **anti-DNase B** ซึ่งไวกว่า |

[[fig:timeline]]

### การรักษา (สไลด์ — KDIGO 2012)
- **Antibiotic** (penicillin หรือ erythromycin) — **กำจัด strep และกันการแพร่** ไปยังคนใกล้ชิด แต่ **ช่วยย้อน GN ได้น้อย** เพราะ immune complex ฝังในไตแล้ว
- **Pulse IV methylprednisolone** เฉพาะรายที่เป็น RPGN (อนุมานจาก crescentic GN อื่น — **ไม่มี RCT**)
- ส่วนหลักคือ **ประคับประคอง** (แนวทางทั่วไป): **จำกัดเกลือและน้ำ** · **loop diuretic** · ยาลดความดัน · ฟอกไตถ้าน้ำเกิน/K สูง/ยูรีเมียรุนแรง

### เมื่อไรต้องสงสัยว่าไม่ใช่ PSGN — ควรเจาะไต
**C3 ยังต่ำเกิน 8–10 สัปดาห์** (นึกถึง C3 glomerulopathy, MPGN, LN) · ไตเสื่อมเร็วแบบ RPGN · โปรตีนรั่วระดับ nephrotic นาน · ไม่มีหลักฐานติดเชื้อ strep · ผู้ใหญ่ที่มีโรคร่วม — ผู้ใหญ่พยากรณ์โรคแย่กว่าเด็ก
""",
    ["PSGN: 2–4 สัปดาห์หลังคอ · 4–6 สัปดาห์หลังผิวหนัง · gross hematuria · HT 60–80% · บวม 80–90%",
     "C3 + CH50 ต่ำใน 2 สัปดาห์ (90%) · C4 ปกติ · กลับปกติใน 8–10 สัปดาห์ — ถ้ายังต่ำ ต้องเจาะไต",
     "ASO 30% · anti-DNase B 70% (ไวกว่าหลังติดเชื้อผิวหนัง)",
     "พยาธิ: exudative GN มี neutrophil · IF coarse granular IgG/C3 · EM subepithelial hump",
     "รักษา: ประคับประคอง (เกลือ/น้ำ, loop, ลดความดัน) · ATB กำจัดเชื้อแต่ไม่ย้อน GN"],
    [mcq(N(21), "A 12-year-old boy with post-impetigo acute nephritic syndrome had low C3 at presentation. At 12 weeks, his blood pressure has normalized but C3 remains low and microscopic hematuria persists. What is the most appropriate next step?",
         ["Reassure; low C3 can persist for 1 year in PSGN", "Repeat ASO titer and treat with penicillin again", "Kidney biopsy to look for C3 glomerulopathy, MPGN or lupus nephritis", "Start high-dose prednisolone empirically", "Tonsillectomy"], 2,
         "สไลด์: C3 ใน PSGN **กลับปกติภายใน 8–10 สัปดาห์** — **ยังต่ำที่ 12 สัปดาห์** ทำให้ต้องสงสัยโรคที่ complement ถูกกระตุ้นต่อเนื่อง เช่น **C3 glomerulopathy, MPGN หรือ LN** จึงควร **เจาะไต**\n\n- การรอถึง 1 ปีไม่ถูกต้องตามธรรมชาติของ PSGN\n- ATB ซ้ำไม่แก้ C3 ต่ำ\n- ให้ steroid โดยไม่มีพยาธิวินิจฉัยไม่เหมาะ\n- ตัดต่อมทอนซิลไม่ใช่การรักษา PSGN",
         "C3 ต่ำเกิน 8–10 สัปดาห์ = ไม่ใช่ PSGN ธรรมดา → เจาะไต", "PSGN", R("PSGN: complement level usually normal within 8–10 weeks"), [AGN, "B9.2.2(3)"]),
     mcq(N(22), "A 7-year-old girl develops cola-colored urine and hypertension 5 weeks after impetigo. Which serologic test is most likely to document the preceding streptococcal infection?",
         ["Antistreptolysin O (ASO)", "Anti-DNase B", "Anti-dsDNA", "Anti-PLA2R", "Rheumatoid factor"], 1,
         "สไลด์: **ASO บวกเพียง 30%** แต่ **anti-DNase B บวก 70%** — หลัง **ติดเชื้อผิวหนัง** ASO ขึ้นน้อยเป็นพิเศษ (streptolysin O ถูกไขมันในผิวหนังจับไว้) anti-DNase B จึงเป็นตัวที่ดีกว่า\n\n- anti-dsDNA ใช้กับ SLE\n- anti-PLA2R ใช้กับ MN\n- RF ไม่จำเพาะ",
         "หลัง impetigo ใช้ anti-DNase B (70%) ดีกว่า ASO (30%)", "PSGN", R("PSGN: ASO 30%, anti-DNase B 70%"), [AGN, "B9.2.2(3)"])],
    [AGN, "B9.2.2(3)", "2.1.43"],
    {"psgn": fig("PSGN — จาก strep ถึงอาการสามกลุ่ม",
        "แอนติเจนของ strep ไปฝังใน glomerulus แล้วจับกับแอนติบอดีเป็น immune complex (**hump**) → complement ทาง alternative ถูกใช้ (**C3 ต่ำ C4 ปกติ**) → neutrophil เข้ามาและเซลล์แบ่งตัว (**exudative GN**) → แตกเป็นสามกลุ่มอาการ: GFR ลด · โซเดียมคั่ง · GBM ฉีก",
        F.psgn()),
     "timeline": fig("เวลาเป็นตัวแยก IgAN จาก PSGN",
        "บน: **IgAN** เลือดออก 1–2 วันหลังเจ็บคอ · **PSGN** ต้องรอ 2–4 สัปดาห์หลังคออักเสบ หรือ 4–6 สัปดาห์หลังติดเชื้อผิวหนัง · ล่าง: **C3 ใน PSGN** ต่ำตั้งแต่ 2 สัปดาห์แรกแล้วกลับปกติใน 8–10 สัปดาห์ (IgAN C3 ปกติตลอด)",
        F.timeline())})

# ───────────────────────────── 13
sec("neph-gn-13", "Lupus nephritis — class บอกตำแหน่ง deposit และการรักษา",
    "อาการ 3 ระบบ · ACR 2012 · ข้อบ่งชี้เจาะไต · full house · class I–VI · รักษาตาม class", 12,
"""### อาการของ LN (สไลด์)
| กลุ่ม | สัดส่วน |
|---|---|
| **Glomerular** | proteinuria **100%** · nephrotic 45–65% · micro hematuria **80%** · macro 1–2% · ไตเสื่อม 40–80% · **RPGN 30%** · ความดันสูง 15–50% |
| **Vascular** | renal vein หรือ artery thrombosis (มัก antiphospholipid) |
| **Tubular** | renal tubular acidosis · **K สูง 15%** |

### กลไก (แผนภาพในสไลด์)
[[fig:sle]]

### เกณฑ์ LN ของ ACR 2012 (สไลด์)
- **Spot UPCR > 0.5**
- **Active urinary sediment**: > 5 RBC/HPF · > 5 WBC/HPF (ไม่มีติดเชื้อ) · หรือ cellular cast (RBC หรือ WBC cast)

### ข้อบ่งชี้เจาะไตใน SLE (สไลด์)
- **creatinine สูงขึ้น** โดยไม่มีสาเหตุอื่นที่ชัดเจน
- **proteinuria ยืนยัน > 1.0 g/24 ชม.**
- จากการตรวจอย่างน้อย 2 ครั้งในเวลาใกล้กัน: **proteinuria ≥ 0.5 g/24 ชม. + hematuria ≥ 5 RBC/HPF** หรือ **proteinuria ≥ 0.5 g/24 ชม. + cellular cast**

**พยาธิ**: IF **"full house"** — IgG, IgA, IgM, C1q, C3 (ติดทั้ง glomerulus TBM และหลอดเลือด) · EM deposit **subendothelial** หรือ **mesangial** เด่น

### Class (ISN/RPS) — deposit อยู่ตรงไหน → ได้กลุ่มอาการอะไร → รักษาอย่างไร
| Class | พยาธิ | deposit | ภาพทางคลินิก | การรักษา (สไลด์) |
|---|---|---|---|---|
| **I** | minimal mesangial | mesangium น้อย | ปัสสาวะแทบปกติ | **ไม่ต้องรักษาที่ไต** |
| **II** | mesangial proliferative | mesangium | hematuria/โปรตีนเล็กน้อย | รักษาอาการนอกไต · โปรตีน > 1–2 g/วัน: pred สั้น 6–8 สัปดาห์ (หลักฐานน้อย) |
| **III / IV** | **proliferative** — focal (< 50% glomeruli) / diffuse (≥ 50%) | **subendothelial** ติดเลือด | **nephritic** · RPGN · Cr ขึ้น | **pred 0.5–1 mg/kg/วัน + ยากดภูมิอื่น** |
| **V** | **membranous** | **subepithelial** | **nephrotic** ตะกอนใส | pred 0.5–1 mg/kg/วัน + ยากดภูมิอื่น (กลุ่มพิเศษ) |
| **VI** | advanced sclerosing (≥ 90% แผลเป็น) | — | ไตวายเรื้อรัง | **supportive** (เตรียมบำบัดทดแทนไต) |

> ทบทวนภาพ "ตำแหน่ง deposit" ในหัวข้อ 6 — **class IV คือ subendothelial = ติดเลือด = อักเสบ** · **class V คือ subepithelial = รั่ว ไม่อักเสบ** · ผู้ป่วยหนึ่งคนอาจเป็น **III/IV + V** ร่วมกัน จึงเห็น oval fat body ร่วมกับ dysmorphic RBC

**แนวทางปัจจุบัน — KDIGO 2024 LN (ไม่ได้อยู่ในสไลด์)**: **hydroxychloroquine ทุกราย** · class III/IV: glucocorticoid ร่วมกับ **mycophenolate** หรือ **cyclophosphamide ขนาดต่ำ (Euro-Lupus)** หรือแบบสามยา (เพิ่ม **belimumab** หรือ calcineurin inhibitor เช่น voclosporin) · ลด steroid ให้เร็ว · ACEi/ARB ลดโปรตีน · ระวังลิ่มเลือดถ้ามี antiphospholipid
""",
    ["LN: proteinuria 100% · micro hematuria 80% · nephrotic 45–65% · RPGN 30% · K สูง 15%",
     "ACR 2012: UPCR > 0.5 หรือ active sediment (> 5 RBC, > 5 WBC/HPF ไม่ติดเชื้อ, cellular cast)",
     "เจาะไต: Cr ขึ้น · protein > 1 g/24 ชม. · protein ≥ 0.5 g + hematuria ≥ 5 RBC หรือ + cellular cast",
     "IF full house (IgG IgA IgM C1q C3) · EM subendothelial/mesangial",
     "Class III/IV = subendothelial = nephritic → pred + ยากดภูมิ · V = subepithelial = nephrotic · VI = supportive"],
    [mcq(N(23), "A 29-year-old woman with SLE has edema, urine protein 6 g/day, bland sediment, normal creatinine and low-normal C3. Biopsy shows diffuse GBM thickening with subepithelial deposits and no endocapillary proliferation. Which ISN/RPS class is this?",
         ["Class II", "Class III", "Class IV", "Class V", "Class VI"], 3,
         "**Class V (membranous lupus nephritis)** — deposit อยู่ **subepithelial** เหมือน MN จึงเป็น **nephrotic ตะกอนใส** และไม่มี proliferative lesion\n\n- **Class II** deposit ที่ mesangium อาการน้อย\n- **Class III/IV** มี subendothelial deposit + endocapillary proliferation → nephritic\n- **Class VI** แผลเป็น ≥ 90% ไตวายเรื้อรัง",
         "LN nephrotic ตะกอนใส + subepithelial = class V", "Lupus nephritis", R("Lupus nephritis classes; Class V: membranous nephropathy"), [NS, "B5.2.2-3(5)"]),
     mcq(N(24), "A 24-year-old woman with SLE has two urine tests a week apart showing protein 0.7 g/24 h and 10 RBC/HPF without infection; creatinine is normal. According to the lecture's criteria, what is the most appropriate next step?",
         ["Observe and repeat in 6 months", "Kidney biopsy", "Start cyclophosphamide without biopsy", "Treat as a urinary tract infection", "Restrict protein intake only"], 1,
         "สไลด์ระบุข้อบ่งชี้เจาะไต: **proteinuria ≥ 0.5 g/24 ชม. ร่วมกับ hematuria ≥ 5 RBC/HPF** จากการตรวจอย่างน้อย 2 ครั้ง — รายนี้เข้าเกณฑ์ (0.7 g + 10 RBC) จึงควร **เจาะไต** เพื่อกำหนด class และการรักษา แม้ creatinine ยังปกติ\n\n- การรอ 6 เดือนเสี่ยงพลาด proliferative LN\n- ให้ cyclophosphamide โดยไม่รู้ class ไม่เหมาะ\n- ไม่มีหลักฐานติดเชื้อ\n- จำกัดโปรตีนไม่ใช่การรักษาหลัก",
         "SLE + protein ≥ 0.5 g + RBC ≥ 5/HPF (หรือ cellular cast) → เจาะไต", "Lupus nephritis", R("Indication for kidney biopsy in SLE"), [AGN, "B5.2.2-3(5)", "B1.6.1(1)"])],
    [AGN, NS, "B5.2.2-3(5)", "2.3.13-3(15)", "B1.6.1(1)"],
    {"sle": fig("Lupus nephritis — จากซากเซลล์ถึงแผลเป็น",
        "ซากเซลล์ตายที่เก็บกวาดไม่หมดเผยแอนติเจนในนิวเคลียส → กระตุ้น TLR7/9 และ interferon → B cell สร้าง **anti-dsDNA** → immune complex ไปติดที่ไต → **complement ถูกใช้ (C3, C4 ต่ำ)** และเซลล์อักเสบทำลาย → ถ้าไม่หยุดจะกลายเป็นพังผืด (class VI) — ตำแหน่งที่ complex ไปติดกำหนด class",
        F.sle())})

# ───────────────────────────── MEQ / OSCE
LECNAME = "Approach to glomerular disease (พญ.ฉันทิศา)"
MEQ = [{"id": "NEPH-GN-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Adult nephrotic syndrome — membranous nephropathy complicated by renal vein thrombosis",
 "vignette": """ผู้ป่วยชายไทยอายุ 58 ปี อาชีพขับรถรับจ้าง มาด้วยขาบวมสองข้าง 6 สัปดาห์
PI: 6 สัปดาห์ก่อน สังเกตว่าปัสสาวะเป็นฟองมาก กดชักโครกแล้วฟองยังไม่หาย ต่อมาตื่นนอนหนังตาบวม ตอนบ่ายขาบวม น้ำหนักเพิ่ม 7 กก. นอนราบได้ ไม่หอบ ปัสสาวะไม่เป็นสีโค้ก
PH: ปวดเข่า ซื้อยาแก้ปวดกินเกือบทุกวันมา 1 ปี · สูบบุหรี่ 30 pack-year
PE: BP 132/84 mmHg, PR 80/min · ไม่ซีด ไม่เหลือง JVP ไม่สูง · pitting edema 3+ ถึงต้นขา · มีน้ำในช่องท้องเล็กน้อย · ปอดใส
Lab: UA: SG 1.020, protein 4+, blood 1+, RBC 3–5/HPF รูปร่างปกติ, WBC 0–2/HPF, พบ oval fat bodies และ fatty casts
UPCR 9.2 g/g · albumin 1.9 g/dL · cholesterol 386 mg/dL · creatinine 1.0 mg/dL · C3, C4 ปกติ
HBsAg ลบ · anti-HCV ลบ · anti-HIV ลบ · ANA ลบ""",
 "questions": [
  {"q": "1. ผู้ป่วยมีกลุ่มอาการทาง glomerulus แบบใด จงบอกเกณฑ์ที่ใช้ให้ครบ (3 คะแนน)",
   "a": """**Nephrotic syndrome** — ครบเกณฑ์ (สไลด์)
- **Proteinuria > 3.5 g/วัน** — UPCR 9.2 g/g ≈ 9 g/วัน
- **Edema** — pitting edema ถึงต้นขา + ascites
- **Hypoalbuminemia** — 1.9 g/dL
- **Hypercholesterolemia > 200** — 386 mg/dL
- **Lipiduria** — oval fat bodies, fatty casts
ไม่มี glomerular hematuria (RBC น้อย รูปร่างปกติ) ความดันไม่สูง ไตปกติ → ไม่ใช่ nephritic"""},
  {"q": "2. จงอธิบายกลไกที่ทำให้ผู้ป่วยบวมและไขมันในเลือดสูง (3 คะแนน)",
   "a": """**บวม** — สองกลไกร่วมกัน
- **Underfill**: albumin ต่ำ → oncotic pressure ในหลอดเลือดลด → น้ำซึมออกนอกหลอดเลือด → volume ลด → RAAS/ADH → ไตเก็บน้ำเกลือ
- **Overfill**: plasminogen ที่รั่วมาในน้ำกรองถูกเปลี่ยนเป็น plasmin → ตัดและเปิด **ENaC** ที่ collecting duct → ไตเก็บโซเดียมเองโดยตรง
**ไขมันสูง** — albumin ต่ำกระตุ้นตับให้ **สร้าง lipoprotein (apoB) เพิ่ม** + PCSK9 เพิ่ม LDL receptor ลด + **lipoprotein lipase ทำงานลด** จึงกำจัด VLDL ช้า (ไม่ได้เกิดจากอาหาร)"""},
  {"q": "3. โรคทาง glomerulus ที่น่าจะเป็นมากที่สุดคืออะไร เพราะเหตุใด และจะหาสาเหตุทุติยภูมิอะไรเพิ่มในผู้ป่วยรายนี้ (4 คะแนน)",
   "a": """**Membranous nephropathy (MN)** — ผู้ใหญ่ > 40 ปี เพศชาย nephrotic ค่อยเป็นค่อยไป **ตะกอนใส** ไตปกติ (ลักษณะตามสไลด์)
ต้องหาสาเหตุทุติยภูมิ (ผู้ป่วยรายนี้มีสองประเด็นเด่น)
- **ยา NSAIDs** ที่ซื้อกินประจำ — หยุดยา
- **มะเร็ง** — อายุ 58 สูบบุหรี่มาก → **CT ทรวงอก (มะเร็งปอดพบบ่อยสุด 26%)** · ส่องกล้องลำไส้ใหญ่ · PSA
- ตรวจแล้ว: HBV, HCV, HIV, ANA ลบ — ส่ง **VDRL** เพิ่ม
- **Anti-PLA2R** — ถ้าบวกสนับสนุน MN ปฐมภูมิ"""},
  {"q": "4. ผลชิ้นเนื้อไต: LM พบ GBM หนาทั่วและมี spike ใน silver stain · IF พบ granular IgG และ C3 ตามผนังหลอดเลือดฝอย — จะพบอะไรใน EM และอธิบายว่าทำไมผู้ป่วยรายนี้ไม่มี hematuria หรือการอักเสบ (3 คะแนน)",
   "a": """**EM: subepithelial electron-dense deposits** (ระหว่าง GBM กับ podocyte)
แอนติบอดี (anti-PLA2R) จับแอนติเจนบน **podocyte** → immune complex ก่อตัว **ใต้ podocyte** → complement (C5b-9) เจาะ podocyte → โปรตีนรั่วมาก แต่ deposit อยู่ **นอก GBM ฝั่งปัสสาวะ** เซลล์อักเสบในเลือดเข้าไม่ถึง → ไม่มี proliferation ไม่มี RBC cast ตะกอนใส · GBM งอกแทรกระหว่างก้อนเห็นเป็น spike"""},
  {"q": "5. 10 วันต่อมา ผู้ป่วยปวดสีข้างซ้ายเฉียบพลัน ปัสสาวะเป็นเลือดเห็นด้วยตา คลำได้เส้นเลือดขอดที่ถุงอัณฑะซ้าย creatinine 1.0 → 1.6 mg/dL — จงให้การวินิจฉัย การตรวจยืนยัน และการรักษา (4 คะแนน)",
   "a": """**Left renal vein thrombosis (RVT)** — ภาวะแทรกซ้อนที่พบบ่อยที่สุดใน MN (albumin < 2 g/dL)
- กลไก: antithrombin III รั่ว · fibrinogen, factor V/VIII สูง · เกล็ดเลือดจับกลุ่ม · เลือดข้นจากยาขับปัสสาวะ
- **varicocele ซ้าย** เพราะ left gonadal vein เทเข้า left renal vein
- ยืนยัน: **Doppler ultrasound ของ renal vein** หรือ **CT venography / MR venography**
- รักษา: **anticoagulation** (heparin → warfarin หรือยาตามแนวทาง) ตลอดช่วงที่ยังเนโฟรติก · เฝ้าระวัง **PE**"""},
  {"q": "6. จงเขียนการรักษาทั่วไปของ nephrotic syndrome ในผู้ป่วยรายนี้ (3 คะแนน)",
   "a": """- **จำกัดเกลือ** (Na < 2 g/วัน) + **loop diuretic** ขนาดสูงพอ (albumin ต่ำ furosemide ถึงท่อน้อย) ± thiazide/amiloride
- **ACEi หรือ ARB** ลดโปรตีนรั่ว (ลดแรงดันใน glomerulus) — ติดตาม Cr, K
- **Statin**
- **Anticoagulant** (มี RVT แล้ว — ให้รักษา)
- **วัคซีน** pneumococcus, influenza · หลีกเลี่ยง **NSAIDs**
- ประเมินความเสี่ยงตาม KDIGO 2021 เพื่อพิจารณา **rituximab** หรือ cyclophosphamide + steroid (โปรตีน > 8 g/วัน = ความเสี่ยงสูงถ้าไม่ลดลง)"""}],
 "ref": ["สไลด์ พญ.ฉันทิศา — Nephrotic syndrome, MN", "KDIGO 2021 Glomerular Diseases"],
 "nl": [NS, "B9.2.2(4)", "2.1.39", "2.3.9(2)"], "years": [], "_kind": "meq", "_set": SET}]

OSCE = [{"id": "NEPH-GN-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "SAQ – Interpreting urinalysis and sediment in five patients",
 "station": "SAQ 10 นาที",
 "instruction": """จงแปลผลปัสสาวะต่อไปนี้ บอกว่าเข้าได้กับภาวะใด และกลไกที่ทำให้ได้ผลเช่นนั้น (รายละ 2 คะแนน)

| ราย | ผลตรวจ |
|---|---|
| A | หญิง 25 ปี บวมทั้งตัว · protein 4+ · RBC 0–2/HPF · **oval fat bodies** (Maltese cross ใต้แสงโพลาไรซ์) |
| B | ชาย 30 ปี ความดัน 170/100 ปัสสาวะสีโค้ก · protein 1+ · RBC 50–100/HPF **dysmorphic 70%** · **RBC cast** |
| C | ชาย 22 ปี หลังวิ่งมาราธอน ปัสสาวะสีน้ำตาลแดง · **dipstick blood 3+** · RBC 0–2/HPF · น้ำส่วนบนหลังปั่นยังแดง |
| D | หญิง 68 ปี ซีด ปวดหลัง Ca 11.8 mg/dL · **dipstick protein trace** · **SSA 3+** · 24-h protein 3.2 g |
| E | ชาย 66 ปี สูบบุหรี่ ปัสสาวะแดงสดมี **ลิ่มเลือด** · protein trace · RBC เต็ม HPF **รูปร่างปกติ** ไม่มี cast |""",
 "answer": """**เกณฑ์ให้คะแนน (10 คะแนน)**

| ราย | การแปลผล | กลไก | คะแนน |
|---|---|---|---|
| A | **Nephrotic syndrome** (lipiduria) | lipoprotein รั่วผ่านตะแกรง เซลล์ท่อไตกลืนไขมันเป็น oval fat body · cholesterol ester เห็นเป็น Maltese cross | 2 |
| B | **Nephritic syndrome / glomerular hematuria** | RBC เบียดผ่าน GBM ที่ฉีกและผ่านท่อไตที่ความเข้มข้นเปลี่ยน → dysmorphic · Tamm–Horsfall หุ้มเป็น RBC cast · GFR ลด + Na คั่ง → HT | 2 |
| C | **Myoglobinuria (rhabdomyolysis)** | heme ของ myoglobin ทำปฏิกิริยา peroxidase กับแผ่น blood ทั้งที่ไม่มี RBC · สีอยู่ในน้ำส่วนบน → ส่ง CK | 2 |
| D | **Overflow proteinuria — light chain (multiple myeloma)** | dipstick จับเฉพาะ albumin · SSA ตกตะกอนโปรตีนทุกชนิด → ส่ง SPEP/UPEP, serum free light chain | 2 |
| E | **Non-glomerular hematuria** — สงสัยมะเร็งทางเดินปัสสาวะ | เลือดออกใกล้ทางออก RBC ไม่ผ่านท่อไตจึงรูปร่างปกติ · ไม่มี urokinase ปริมาณมากจึงจับเป็นลิ่ม → CT urography + cystoscopy | 2 |

**ข้อที่ทำให้เสียคะแนน**: แปลราย C ว่าเป็น hematuria · แปลราย D ว่าโปรตีนน้อยตาม dipstick · ไม่บอกกลไก""",
 "ref": ["สไลด์ พญ.ฉันทิศา — Proteinuria, hematuria"], "nl": UA + ["2.1.43", NS, AGN],
 "years": [], "_kind": "meq", "_set": SET}]

LECTURE = {
 "lec": LEC, "date": "พฤ. 1 ต.ค.",
 "title": "Approach to glomerular disease — nephrotic · nephritic",
 "subtitle": "ตะแกรง 3 ชั้น · อาการมาจาก 2 กลไก · วัดโปรตีน · proteinuria 5 ชนิด · hematuria · 6 คำถาม 5 กลุ่มอาการ · nephrotic · nephritic/RPGN · MCD · FSGS · MN · IgAN · PSGN · lupus nephritis",
 "objectives": [
   "อธิบายโครงสร้างตะแกรงกรอง 3 ชั้นของ glomerulus และบอกว่าความเสียหายของแต่ละชั้นทำให้เกิดอาการอะไร",
   "อธิบายกลไกของอาการเด่น — ปัสสาวะเป็นฟอง บวมรอบตา บวมทั้งตัว ความดันสูง ปัสสาวะสีโค้ก ปัสสาวะน้อย",
   "เลือกและแปลผลการตรวจโปรตีนในปัสสาวะ (dipstick, SSA, 24 ชม., UPCR) และแยก proteinuria 5 ชนิด",
   "แยก glomerular จาก non-glomerular hematuria และอธิบายที่มาของ dysmorphic RBC และ RBC cast",
   "จัดผู้ป่วยเข้า 5 กลุ่มอาการ และอธิบายว่าตำแหน่ง deposit กำหนด nephrotic หรือ nephritic อย่างไร",
   "อธิบายกลไกภาวะแทรกซ้อนของ nephrotic (ไขมันสูง ลิ่มเลือด ติดเชื้อ) และให้การรักษาทั่วไป",
   "วินิจฉัยและรักษา MCD, FSGS, MN, IgAN, PSGN และ lupus nephritis ตามสไลด์และแนวทาง KDIGO"],
 "nlGap": "เกณฑ์ฯ มีรหัส nephrotic syndrome (`นล. 2.3.14(12)`, `B9.2.2(4)`) acute GN (`2.3.14(2)`) APSGN (`B9.2.2(3)`) chronic GN (`2.3.14-3(1)`) urinalysis (`3.1.6`, `B9.3(2)`) และ SLE (`B5.2.2-3(5)`) แต่ **ไม่มีรหัสเฉพาะของ MCD, FSGS, membranous nephropathy, IgA nephropathy, RPGN หรือ class ของ lupus nephritis** — และสไลด์ส่วนภาพ (พยาธิ LM/IF/EM, ตารางและอัลกอริทึม KDIGO 2021 ของ MN, ภาพ LN class) อ่านไม่ได้ เนื้อหาส่วนนั้นจึงอิงแนวทางด้านล่างและระบุไว้ในแต่ละหัวข้อ",
 "guidelines": [
   "**KDIGO 2012 Clinical Practice Guideline for Glomerulonephritis** — การรักษา MCD, IgAN, PSGN ในสไลด์ (อาจารย์อ้าง)",
   "**KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases** — การรักษาทั่วไปของ nephrotic, การหาสาเหตุและการรักษา MN ตามความเสี่ยง (อาจารย์อ้าง)",
   "**KDIGO 2025 Clinical Practice Guideline for the Management of IgA Nephropathy and IgA Vasculitis** — เป้าหมายโปรตีน < 0.5 g/วัน",
   "**KDIGO 2024 Clinical Practice Guideline for the Management of Lupus Nephritis** และ **ACR 2012 Lupus Nephritis guideline** (อาจารย์อ้างเกณฑ์ LN และข้อบ่งชี้เจาะไต)",
   "**KDIGO 2024 Clinical Practice Guideline for the Management of ANCA-Associated Vasculitis** — RPGN",
   "**Brenner & Rector's The Kidney** — glomerular vs non-glomerular hematuria, สาเหตุทุติยภูมิ (อาจารย์อ้าง)"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ───────────────────────────── กระจายตำแหน่งคำตอบ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น) · ตัวเลือกเรียงตามธรรมชาติไม่สลับ
ORDERED = {N(6), N(23)}
_slot = 0
for s_ in S:
    for it in s_["items"]:
        if it["id"] in ORDERED:
            continue
        tgt = [3, 0, 4, 2, 1][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

# ───────────────────────────── เขียนลงไฟล์ แล้วผูกข้อคลัง
path = os.path.join(BUILD, "data", SET + ".json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LEC]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

BANK_MAP = {
    "neph-gn-02": ["N-OLD-032"],
    "neph-gn-03": ["N-MCQ-08", "N-OLD-018", "N-OLD-025"],
    "neph-gn-04": ["N-MCQ-29", "N-OLD-078", "N-OLD-079", "N-OLD-028"],
    "neph-gn-05": ["N-MCQ-11", "N-OLD-026", "N-OLD-027", "N-OLD-030"],
    "neph-gn-06": ["N-MCQ-07", "N-OLD-016"],
    "neph-gn-07": ["N-OLD-017", "N-OLD-075", "N-MCQ-12", "N-OLD-019"],
    "neph-gn-09": ["N-OLD-021", "N-OLD-022", "N-MCQ-09", "N-OLD-023", "N-OLD-024"],
    "neph-gn-10": ["N-OLD-020"],
    "neph-gn-11": ["N-OLD-033"],
    "neph-gn-12": ["N-MCQ-10", "N-OLD-029"],
    "neph-gn-13": ["N-OLD-031", "N-OLD-076", "N-OLD-085", "N-OLD-086"],
}
added = link(SET, LEC, BANK_MAP, meq=["N-MEQ-01", "N-MEQ-03"], osce=["N-OSCE-02", "N-OSCE-01"])
added_m = link_mock(SET, LEC, {"neph-gn-06": ["MOCK-166"], "neph-gn-08": ["MOCK-177"],
                               "neph-gn-09": ["MOCK-168", "MOCK-167"], "neph-gn-11": ["MOCK-176"], "neph-gn-12": ["MOCK-172"]})

data = json.load(open(path, encoding="utf-8"))
L = [l for l in data if l["lec"] == LEC][0]
seen = set()
for l in data:
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
data.sort(key=lambda l: (0, int(l["lec"])) if l["lec"].isdigit() else (1, l["lec"]))
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == SET: m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print("sections %d | ข้อใหม่ %d + คลัง %d + mock %d = %d | meq %d | osce %d | ภาพ %d | nl %d" % (
    len(S), sum(1 for s_ in S for i in s_["items"] if i["id"].startswith("NEPH-GN")), added - 4, added_m,
    sum(len(s_["items"]) for s_ in L["sections"]), len(L["meq"]), len(L["osce"]),
    sum(len(s_["figs"]) for s_ in S), len(codes)))
print("ตำแหน่งคำตอบข้อใหม่:", dict(sorted(Counter(i["answer"] for s_ in S for i in s_["items"] if i["kind"] == "mcq" and i["id"].startswith("NEPH-GN")).items())))
print("%s.json มี %d คาบ: %s" % (SET, len(data), [l["lec"] for l in data]))
