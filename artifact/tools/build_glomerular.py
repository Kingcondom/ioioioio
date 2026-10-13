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

# ═══════════════════════════ END SECTIONS
