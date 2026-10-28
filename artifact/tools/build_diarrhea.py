#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diarrhea — acute และ chronic (พญ.ธันยพร จันทโรจนศิริ) → data/gi.json คาบ "Diarrhea"
ต้นฉบับ: 4th_year_Gastroenteritis_and_acute_diarrhea_66.pdf (88 หน้า · ผู้ใช้แนบในแชท 28 ต.ค. 2569)
Bedside อ. 27 ต.ค. 2569 · โน้ต slides/diarrhea_notes.md
ภาพนิ่ง + ตารางกลไก: figs_gi_diarrhea.py (apply_figs.py) · ภาพเคลื่อนไหว + หลักจำ: anims_gi_diarrhea.py (ใส่ในสคริปต์นี้)
อัปเดต: ACG 2016 acute diarrheal infection · AFP 2022 · IDSA/SHEA 2021 C. difficile · WHO cholera ·
CDC Yellow Book (travelers' diarrhea) · Rome IV · Thai IBS guideline 2022"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
REPO = os.path.dirname(BUILD)
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.join(REPO, "dashboard"))
from link_mock import link_mock
from patch_learn_anim import _insert_marker
import anims_gi_diarrhea as AN

SET, LEC = "gi", "Diarrhea"
NLN = ["2.1.18"]
SRC = "สไลด์ พญ.ธันยพร — Diarrhea (ปี 2566)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None, src=SRC):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": src,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4 and len(set(choices)) == 5
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "GI-DIA-MCQ-%02d" % n
R = lambda p: ["สไลด์ พญ.ธันยพร — " + p]

# ───────────────────────────── 1
sec("gi-dia-01", "ท้องเสียจริงหรือไม่ — นิยาม และโรคที่เลียนแบบ",
    "ปกติ < 3 ครั้ง/วัน · ~200 g/วัน · Bristol 6–7 · pseudodiarrhea ถี่แต่น้ำหนักไม่เพิ่ม · overflow รอบก้อนอุจจาระ · ลำไส้อุดตันบางส่วน", 7,
"""### นิยาม
- **Diarrhea** มาจากภาษากรีก *dia* (ผ่าน) + *rheo* (ไหล) — Roux & Ryle (1924): **ขับถ่ายเร็วเกินไป และเหลวเกินไป**
- ผู้ป่วยใช้คำนี้หมายถึง **ถ่ายเหลว · ถ่ายบ่อย · หรือปวดเร่งต้องรีบเข้าห้องน้ำ (urgency)** — ต้องถามให้ชัดว่าหมายถึงอะไร
- **อุจจาระปกติ**: น้อยกว่า **3 ครั้งต่อวัน** และราว **200 กรัม/24 ชม.** — ดูทั้ง **ปริมาณ** และ **ความเหลว**
- นิยามที่ใช้ในแนวทาง (ACG 2016): **ถ่ายเหลว ≥ 3 ครั้งใน 24 ชม.** ร่วมกับอาการทางลำไส้อย่างน้อยหนึ่งอย่าง (คลื่นไส้ อาเจียน ปวดบิด ปวดเบ่ง ปวดเร่ง ลมมาก)

### Bristol Stool Form Scale
| แบบ | ลักษณะ | แปลผล |
|---|---|---|
| 1 | ก้อนกลมแข็งแยกกัน | **ท้องผูก** |
| 2 | ก้อนแข็งจับตัวกันเป็นลำ | **ท้องผูก** |
| 3 | เป็นลำ ผิวแตกร้าว | ปกติ |
| 4 | **ลำนิ่มผิวเรียบคล้ายกล้วย** | **ปกติ (ดีที่สุด)** |
| 5 | ก้อนนิ่มขอบชัด | ปกติ–ค่อนเหลว |
| 6 | เละ ขอบไม่ชัด | **ท้องเสีย** |
| 7 | เป็นน้ำ ไม่มีเนื้อ | **ท้องเสีย** |

### ไม่ใช่ท้องเสียจริง (differential diagnosis)
| ภาวะ | ลักษณะ | กุญแจ |
|---|---|---|
| **Pseudodiarrhea** | ถ่าย **บ่อยขึ้น แต่น้ำหนักอุจจาระไม่เพิ่ม** — ครั้งละน้อย | IBS, proctitis, hyperthyroidism |
| **Fecal incontinence** | กลั้นไม่อยู่ ผู้ป่วยมักเล่าว่า "ท้องเสีย" ด้วยความอาย | ต้องถามตรง ๆ · ตรวจ **sphincter tone** |
| **Overflow incontinence** | **ก้อนอุจจาระแข็งอัดแน่น (fecal impaction)** ใน rectum → น้ำอุจจาระเหลวซึมผ่านรอบก้อน | ผู้สูงอายุ ติดเตียง ยา opioid · ประวัติ **ท้องผูกสลับท้องเสีย** · PR คลำได้ก้อน |
| **ลำไส้อุดตันบางส่วน** | มะเร็งลำไส้ใหญ่ตีบ → ของเหลวผ่านจุดตีบได้ ส่วนเนื้ออุจจาระค้าง | ท้องอืด ลำไส้ส่วนต้นโป่ง (barium ในสไลด์: CA colon + cecum โป่ง) |

> **ให้ยาแก้ท้องเสียกับ overflow incontinence = ซ้ำเติมการอุดตัน** — ต้อง PR ก่อนเสมอในผู้สูงอายุติดเตียงที่ "ท้องเสีย"
""",
    ["ปกติ < 3 ครั้ง/วัน · ~200 g/วัน · Bristol 6–7 = ท้องเสีย",
     "Pseudodiarrhea: ถี่แต่น้ำหนักอุจจาระไม่เพิ่ม",
     "Overflow: ก้อนอุจจาระอัด → น้ำซึมรอบก้อน · ท้องผูกสลับเสีย · PR ก่อนให้ยา",
     "Incontinence ต้องถามตรง ๆ และตรวจ sphincter"],
    [mcq(N(1), "An 84-year-old bedridden woman on regular tramadol has had small amounts of liquid stool leaking several times a day for one week. She had not passed a formed stool for 10 days before that. The abdomen is mildly distended. What is the most appropriate next step?",
         ["Digital rectal examination to look for faecal impaction", "Start loperamide 4 mg then 2 mg after each loose stool", "Send stool for C. difficile toxin and start oral vancomycin", "Give oral rehydration solution and observe", "Arrange urgent colonoscopy"], 0,
         "ประวัติ **ไม่ได้ถ่ายเป็นก้อน 10 วัน** + ยา opioid + ติดเตียง แล้วตามด้วย **น้ำอุจจาระซึมออกครั้งละน้อย** = **overflow incontinence รอบ fecal impaction** ไม่ใช่ท้องเสียจริง\n\nขั้นแรกคือ **PR** คลำหาก้อนอุจจาระ แล้วเอาออก (disimpaction/enema)\n\n- **Loperamide** ลดการเคลื่อนไหว → อุดตันมากขึ้น อันตราย\n- C. difficile ต้องคิดในผู้ป่วยใน แต่ควรตรวจเมื่อเป็น **ถ่ายเหลว ≥ 3 ครั้ง** จริง และเรื่องนี้มีเบาะแส impaction ชัดกว่า\n- ORS ไม่แก้ต้นเหตุ · colonoscopy ไม่ใช่ขั้นแรก",
         "ท้องผูกนาน + น้ำซึมครั้งละน้อย = overflow → PR ก่อน", "Diarrhea mimic", R("Diarrhea mimick")),
     mcq(N(2), "A 30-year-old man reports going to the toilet 6–8 times a day with urgency, but each time passes only a small amount of formed or soft stool. A 72-hour collection shows stool weight of 150 g/day. Which term best describes this?",
         ["Pseudodiarrhoea", "Secretory diarrhoea", "Osmotic diarrhoea", "Steatorrhoea", "Overflow incontinence"], 0,
         "นิยามท้องเสียจริงคือ **น้ำหนักอุจจาระ > 200 g/วัน** หรือเหลวผิดปกติ\n\nผู้ป่วยถ่าย **บ่อยแต่น้ำหนักรวมไม่เพิ่ม (150 g)** และเนื้ออุจจาระยังเป็นก้อน = **pseudodiarrhea** พบใน IBS, proctitis หรือ rectum ไวเกิน\n\n- Secretory/osmotic/steatorrhea ล้วนต้องมีปริมาณอุจจาระเพิ่ม\n- Overflow ต้องมีก้อนอุจจาระอัดและประวัติท้องผูก",
         "ถี่แต่ไม่หนัก = pseudodiarrhea", "Definition", R("Differential diagnosis")),
    ], NLN + ["3.1.8"])

# ───────────────────────────── 2
sec("gi-dia-02", "น้ำ 10 ลิตรต่อวัน — ลำไส้ดูดน้ำกลับที่ไหน",
    "น้ำเข้าลำไส้ ~10 L · jejunum ดูด 6 · ileum 2.5 · เข้าลำไส้ใหญ่ 1.5 · colon ดูด 1.4 · ออก 0.1 · ท้องเสีย = motor + fluid transport", 8,
"""### บัญชีน้ำในทางเดินอาหารต่อวัน
| ที่มา/ที่ดูด | ปริมาณ | หน้าที่เด่น |
|---|---|---|
| อาหารและน้ำดื่ม | ~2 L | — |
| น้ำลาย | 0.5 L | — |
| น้ำย่อยกระเพาะ | 2 L | — |
| น้ำดี + น้ำย่อยตับอ่อน | 1.5 L | — |
| + น้ำหลั่งจากลำไส้เล็ก | ที่เหลือ | **รวมเข้าลำไส้เล็กราว 10 L** |
| **Jejunum** ดูดกลับ | **~6 L** | โปรตีน คาร์โบไฮเดรต ไขมัน วิตามินละลายน้ำ แร่ธาตุ · ผนังรั่ว (leaky) น้ำตามตัวถูกละลาย |
| **Ileum** ดูดกลับ | **~2.5 L** | **B12–intrinsic factor · กรดน้ำดี** · ควบคุมการบีบตัวของกระเพาะและลำไส้ (ileal brake) |
| ผ่าน ileocecal valve | **~1.5 L** | — |
| **Colon** ดูดกลับ | **~1.4 L** | เกลือ (Na) และ **short-chain fatty acid** · ผนังแน่น ดูดได้แม้ลำไส้มีความต่างความเข้มข้น |
| **ออกมากับอุจจาระ** | **~0.1 L** | — |

ลำไส้เล็กยาว 300–600 ซม. และ **ปรับตัว (adaptation)** ได้หลังถูกตัด

**ลำไส้ใหญ่ดูดน้ำได้สูงสุดราว 4–5 L/วัน** — ถ้าลำไส้เล็กส่งน้ำมาเกินกว่านี้ (เช่น cholera) จะถ่ายเป็นน้ำปริมาณมากแม้ลำไส้ใหญ่ปกติ
ตรงข้าม ถ้า **ลำไส้ใหญ่เสียหน้าที่** แม้ส่งมาเพียง 1.5 L ก็ท้องเสียได้

### ท้องเสียเกิดจากสองระบบที่ป้อนกลับกันเป็นเกลียว
**การเคลื่อนไหว (motor)** + **การขนส่งน้ำและเกลือแร่ (fluid & electrolyte transport)**

น้ำหลั่งมากขึ้น → ลำไส้ถูกถ่างจึง **บีบไล่แรงขึ้น (propulsion)** → อาหารผ่านเร็ว (**rapid transit**) → สัมผัสผิวดูดซึมสั้นลง → **ดูดกลับได้น้อยลง** → น้ำค้างในลำไส้มากขึ้น → บีบไล่อีก → ท้องเสีย

### ผลของการตัดลำไส้ (ข้อสอบชอบถาม)
- ตัด **ileum** → ขาด **B12** และ **กรดน้ำดีไม่ถูกดูดกลับ** → กรดน้ำดีลงลำไส้ใหญ่กระตุ้นการหลั่งน้ำ (bile acid diarrhea)
- ลำไส้เล็กสั้น + **ยังมีลำไส้ใหญ่** → ไขมันที่ไม่ถูกดูดซึมจับแคลเซียม → **oxalate อิสระถูกดูดซึมที่ลำไส้ใหญ่ → นิ่ว oxalate (enteric hyperoxaluria)**
""",
    ["เข้าลำไส้ ~10 L → jejunum 6 · ileum 2.5 · colon 1.4 · ออก 0.1 L",
     "Colon ดูดได้สูงสุด ~4–5 L/วัน — ลำไส้เล็กหลั่งเกินนี้ = ถ่ายน้ำปริมาณมาก",
     "Ileum: B12 + กรดน้ำดี · colon: Na + SCFA",
     "ท้องเสีย = motor + transport ป้อนกลับเป็นเกลียว",
     "ลำไส้เล็กสั้นที่ยังมี colon → enteric hyperoxaluria → นิ่ว oxalate"],
    [mcq(N(3), "Approximately how much fluid enters the small intestine each day in a healthy adult, and how much is normally excreted in stool?",
         ["About 10 L enters; about 0.1 L is excreted", "About 2 L enters; about 0.5 L is excreted", "About 5 L enters; about 1.5 L is excreted", "About 10 L enters; about 1.5 L is excreted", "About 20 L enters; about 0.2 L is excreted"], 0,
         "จากอาหาร/น้ำดื่ม ~2 L + น้ำลาย 0.5 + กระเพาะ 2 + น้ำดี/ตับอ่อน 1.5 + น้ำหลั่งจากลำไส้เล็ก รวม **~10 L**\n\njejunum ดูด ~6 L · ileum ~2.5 L → เหลือ **~1.5 L เข้าลำไส้ใหญ่** → colon ดูด ~1.4 L → **ออกมากับอุจจาระ ~0.1 L (≈ 100–200 g)**\n\n1.5 L คือปริมาณที่ **ผ่าน ileocecal valve** ไม่ใช่ที่ออกมากับอุจจาระ",
         "10 L เข้า → 0.1 L ออก · 1.5 L ผ่าน ileocecal valve", "Intestinal fluid balance", R("Fluid balance"), NLN + ["B8.1.2(4)"]),
     mcq(N(4), "A patient underwent resection of 150 cm of terminal ileum with an intact colon. Months later he develops a calcium oxalate kidney stone. What is the mechanism?",
         ["Unabsorbed fatty acids bind luminal calcium, leaving oxalate free to be absorbed in the colon", "Loss of intrinsic factor reduces oxalate excretion", "Bile acids directly precipitate oxalate in the renal tubule", "Rapid transit increases jejunal oxalate absorption", "Hypocalcaemia stimulates PTH, which raises urinary oxalate"], 0,
         "ตัด ileum มาก (> 100 ซม.) → **กรดน้ำดีหายจากวงจร** → ไขมันย่อยและดูดซึมไม่ได้ → **fatty acid ในโพรงลำไส้จับแคลเซียม** (saponification)\n\nแคลเซียมที่ปกติจะจับ oxalate ไว้ถูกแย่งไป → **oxalate อิสระถูกดูดซึมที่ลำไส้ใหญ่** (กรดน้ำดีที่ลงมายังเพิ่มการซึมผ่านของผนัง) → oxalate ในปัสสาวะสูง → นิ่ว\n\nจึงต้อง **มีลำไส้ใหญ่อยู่** ภาวะนี้จึงเกิด — สไลด์: colon ทำให้ **เสี่ยง enteric hyperoxaluria**",
         "ตัด ileum + มี colon → enteric hyperoxaluria", "Short bowel physiology", R("Fluid balance — colon"), ["B8.1.2(4)", "2.3.11-3(2)"]),
    ], NLN + ["B8.1.2(4)"])

# ───────────────────────────── 3
sec("gi-dia-03", "จำแนกท้องเสีย 4 แกน — เลือกให้ถูกก่อนสืบค้น",
    "Acute < 2–3 สัปดาห์ vs chronic > 4 สัปดาห์ · ปริมาณมาก (ลำไส้เล็ก/colon ขวา) vs น้อยถี่ (rectosigmoid) · osmotic vs secretory · watery/fatty/inflammatory", 7,
"""### สี่แกนในสไลด์
| แกน | แบ่งเป็น | ใช้ทำอะไร |
|---|---|---|
| **ระยะเวลา** | **Acute < 2–3 สัปดาห์** · persistent 14–30 วัน · **chronic > 4 สัปดาห์** | acute ส่วนใหญ่ติดเชื้อ หายเอง · chronic ส่วนใหญ่ไม่ใช่ติดเชื้อ |
| **ปริมาณ** | **Large volume vs small volume** | บอก **ตำแหน่ง** — ขึ้นกับหน้าที่ **rectosigmoid เป็นที่พักอุจจาระ (reservoir)** |
| **กลไกน้ำ** | **Osmotic vs secretory** | ตรวจ **stool electrolyte → osmotic gap** |
| **ลักษณะอุจจาระ** | **Watery · malabsorptive (fatty) · inflammatory (มูกเลือด)** | ใช้วางแผนสืบค้นใน **chronic diarrhea** |

### ลำไส้เล็ก vs ลำไส้ใหญ่ส่วนปลาย
| | **ลำไส้เล็ก/colon ขวา** | **ลำไส้ใหญ่ซ้าย/rectum** |
|---|---|---|
| ปริมาณต่อครั้ง | **มาก เป็นน้ำ** | **น้อย ถี่** |
| ปวดท้อง | รอบสะดือ บิดเป็นพัก | ท้องน้อย ซ้ายล่าง |
| ปวดเบ่ง ปวดเร่ง | ไม่เด่น | **เด่น (tenesmus, urgency)** |
| เลือด มูก | ไม่ค่อยมี | **พบบ่อย** |
| ขาดน้ำ | **เร็ว** | ช้ากว่า |
| ตัวอย่าง | cholera, ETEC, ไวรัส, Giardia | Shigella, amoebic colitis, UC |

**ทำไม** — rectosigmoid ที่อักเสบ **รับแรงยืดไม่ได้** แม้อุจจาระปริมาณน้อยก็กระตุ้นให้ต้องถ่ายทันที ขณะที่ลำไส้เล็กหลั่งน้ำจำนวนมากจนลำไส้ใหญ่ดูดกลับไม่ทัน
""",
    ["Acute < 2–3 สัปดาห์ · chronic > 4 สัปดาห์",
     "ปริมาณมากเป็นน้ำ = ลำไส้เล็ก · น้อยถี่ ปวดเบ่ง มูกเลือด = colon ซ้าย/rectum",
     "Osmotic vs secretory แยกด้วย stool osmotic gap",
     "Chronic: watery / fatty / inflammatory"],
    [mcq(N(5), "A 25-year-old man has frequent small-volume stools containing mucus and blood, with lower abdominal cramps and tenesmus for 3 days. Where is the disease most likely located?",
         ["Rectosigmoid colon", "Jejunum", "Proximal ileum", "Stomach and duodenum", "Pancreas"], 0,
         "**ปริมาณน้อย ถี่ ปวดเบ่ง (tenesmus) มีมูกเลือด** = ลักษณะของลำไส้ใหญ่ส่วนปลาย\n\nrectosigmoid ปกติเป็น **ที่พักอุจจาระ (reservoir)** เมื่ออักเสบจะรับแรงยืดไม่ได้ อุจจาระเพียงเล็กน้อยก็กระตุ้นให้ต้องถ่าย และเยื่อบุที่เป็นแผลทำให้มีเลือดและมูก\n\nโรคลำไส้เล็กจะ **ถ่ายเป็นน้ำปริมาณมาก** ปวดรอบสะดือ ไม่ค่อยมีเลือด",
         "น้อย ถี่ ปวดเบ่ง มูกเลือด = rectosigmoid", "Large vs small volume", R("Clinical classification")),
    ])

# ───────────────────────────── 4
sec("gi-dia-04", "Acute diarrhea — สาเหตุ และเบาะแสจากอาหาร สถานที่",
    "80% ติดเชื้อ · เพาะเชื้อขึ้น < 10% · ไวรัส แบคทีเรีย โปรโตซัว · เบาะแสจากอาหาร: ข้าวผัด → B. cereus · สัตว์ปีก/ไข่ → Salmonella · อาหารทะเล → Vibrio", 8,
"""### ภาพรวม
- **Acute diarrhea** = ท้องเสียไม่เกิน 2–3 สัปดาห์ (แนวทางไทย 2546 ใช้ < 14 วัน)
- **80% เกิดจากการติดเชื้อ** · ที่เหลือ: ลำไส้ขาดเลือด, IBD, เนื้องอก, **ยา**, อาหารเป็นพิษ, แพ้อาหาร หรือเป็น **อาการแรกของ chronic diarrhea**
- **เพาะเชื้อพบเชื้อน้อยกว่า 10%** · 20–40% หาสาเหตุไม่ได้เลย → ส่วนใหญ่ไม่ต้องส่งตรวจ (ดูหัวข้อ approach)

### เชื้อที่พบบ่อย
| กลุ่ม | เชื้อ |
|---|---|
| **แบคทีเรีย** | Aeromonas · **Campylobacter** · **C. difficile** · **E. coli** (ETEC, EIEC, EHEC) · Plesiomonas · **Salmonella** · **Shigella** · Vibrio |
| **ไวรัส** | **Norovirus** · Rotavirus · Adenovirus · Astrovirus |
| **โปรโตซัว** | Cryptosporidium · Cyclospora · **Entamoeba histolytica** · **Giardia** · Microsporidia |

### เบาะแสจากสิ่งที่กินและสถานที่
| แหล่ง | เชื้อคลาสสิก |
|---|---|
| น้ำ | **V. cholerae** · norovirus · Giardia · Cryptosporidium |
| สัตว์ปีก | **Salmonella · Campylobacter** · Shigella |
| **ไข่** | **Salmonella** |
| เนื้อวัว (บดไม่สุก) น้ำผลไม้ไม่พาสเจอไรซ์ ถั่วงอก ผักโขม | **EHEC (O157:H7)** |
| เนื้อหมู | พยาธิตืด · **Streptococcus suis** (หมูดิบ — ไข้ เยื่อหุ้มสมองอักเสบ หูหนวก) |
| อาหารทะเล หอย | **V. cholerae, V. parahaemolyticus, V. vulnificus** · Salmonella · ไวรัสตับอักเสบ A · Anisakis |
| ชีส นม | **Listeria** |
| มายองเนส สลัด ขนมครีม | **S. aureus** · Clostridium |
| **ข้าวผัด ข้าวที่หุงทิ้งไว้** | **Bacillus cereus** |
| เบอร์รี่สด | Cyclospora |
| อาหารกระป๋อง | Clostridium (botulinum) |
| สัตว์เลี้ยง ปศุสัตว์ | Salmonella · Campylobacter · Cryptosporidium · Giardia |
| สถานรับเลี้ยงเด็ก | Shigella · Campylobacter · Cryptosporidium · Giardia |
| **โรงพยาบาล / เพิ่งได้ยาปฏิชีวนะ** | **C. difficile** |
| สระว่ายน้ำ | Giardia · Cryptosporidium |
| เดินทาง | ETEC · Salmonella · Shigella · Campylobacter · Giardia · E. histolytica · norovirus (เรือสำราญ) |
""",
    ["Acute: 80% ติดเชื้อ · เพาะเชื้อขึ้น < 10%",
     "ข้าวผัดค้าง → B. cereus · มายองเนส/ขนมครีม → S. aureus",
     "ไข่/สัตว์ปีก → Salmonella · อาหารทะเล → Vibrio",
     "เนื้อบด ถั่วงอก → EHEC · ชีส นม → Listeria",
     "นอนโรงพยาบาล/ได้ยาปฏิชีวนะ → C. difficile"],
    [mcq(N(6), "Two hours after eating leftover fried rice from a buffet, several office workers develop profuse vomiting and abdominal cramps with little diarrhoea and no fever. What is the most likely cause?",
         ["Preformed emetic toxin of Bacillus cereus", "Shiga toxin-producing Escherichia coli", "Invasive Shigella sonnei", "Rotavirus", "Giardia lamblia"], 0,
         "**ระยะฟักตัวสั้นมาก (1–6 ชม.) + อาเจียนเด่น + ไม่มีไข้ + หลายคนป่วยพร้อมกัน** = **toxin ที่สร้างไว้ก่อนในอาหาร (preformed toxin)** ไม่ต้องรอเชื้อเพิ่มจำนวนในลำไส้\n\n**ข้าวผัด/ข้าวที่หุงทิ้งไว้** เป็นแหล่งคลาสสิกของ **B. cereus** (สปอร์ทนความร้อน แตกตัวสร้าง emetic toxin เมื่อข้าววางไว้อุณหภูมิห้อง)\n\n- EHEC และ Shigella ระยะฟักตัวหลายวัน ปวดบิด ถ่ายเป็นเลือด\n- Rotavirus และ Giardia ไม่สัมพันธ์กับข้าวผัด และระยะฟักตัวยาวกว่า",
         "อาเจียนภายในไม่กี่ชั่วโมงหลังข้าวผัด = B. cereus (preformed toxin)", "Vehicle & pathogen", R("Vehicle & pathogen"), NLN + ["2.3.1(7)"]),
     mcq(N(7), "A previously well 70-year-old woman develops watery diarrhoea 6 days after starting ceftriaxone for pneumonia. Which organism should be tested for first?",
         ["Clostridioides difficile", "Vibrio cholerae", "Entamoeba histolytica", "Norovirus", "Bacillus cereus"], 0,
         "**ท้องเสียในโรงพยาบาลหลังได้ยาปฏิชีวนะ** (โดยเฉพาะ cephalosporin, clindamycin, fluoroquinolone) = ต้องตรวจ **C. difficile** ก่อนเสมอ\n\nยาปฏิชีวนะกำจัดเชื้อประจำถิ่นในลำไส้ใหญ่ → C. difficile เติบโตและปล่อย **toxin A/B** ทำลายเซลล์เยื่อบุ → colitis จนถึง pseudomembranous colitis\n\nเชื้ออื่นในตัวเลือกไม่สัมพันธ์กับการนอนโรงพยาบาลหรือยาปฏิชีวนะ",
         "นอนโรงพยาบาล + ยาปฏิชีวนะ + ท้องเสีย = C. difficile", "Hospital-acquired diarrhea", R("Vehicle & pathogen — hospital"), NLN + ["2.3.1(7)"]),
    ], NLN + ["2.3.1(7)", "B8.2.2(4)"])

# ───────────────────────────── 5
sec("gi-dia-05", "กลไกก่อโรคของเชื้อ — ยิ่งรุกล้ำลึก ยิ่งไข้และปวดบิด",
    "Toxin producer → enteroadherent → cytotoxin → invasive → systemic · toxin: อาเจียน/น้ำมาก ไม่มีไข้ · invasive: ไข้ ปวด มูกเลือด · preformed ภายใน 4 ชม. vs enterotoxin 1–3 วัน · ไวรัส", 10,
"""### ห้าแบบ เรียงตามความลึกที่เชื้อรุกล้ำ
ลายมือในสไลด์: **ยิ่งรุกล้ำเข้าไปในเนื้อเยื่อ ⇒ ยิ่งมีไข้และปวดบิด**

| กลไก / เชื้อ | คลื่นไส้อาเจียน | ปวดท้อง | ไข้ | ท้องเสีย |
|---|---|---|---|---|
| **Toxin producer** | **2+ ถึง 4+** | 1–2+ | **0–1+** | **3–4+ เป็นน้ำ** |
| — preformed toxin: **B. cereus, S. aureus, C. perfringens** | อาการ **ภายใน ~4 ชม.** | | | |
| — enterotoxin: **V. cholerae, ETEC**, K. pneumoniae, Aeromonas | อาการ **1–3 วัน** | | | |
| **Enteroadherent**: EPEC, EAEC, **Giardia**, Cryptosporidium, พยาธิ | 0–1+ | 1–3+ | 1–2+ | 1–2+ เป็นน้ำ |
| **Cytotoxin-producing**: **C. difficile, EHEC O157:H7** | 0–1+ | **3–4+** | 1–2+ | 1–3+ เป็นน้ำ บางครั้งเป็นเลือด |
| **Invasive** | 0–3+ | 2–4+ | **3–4+** | 1–4+ น้ำหรือ **เลือด** |
| — อักเสบน้อย: rotavirus, norovirus, Cryptosporidium, Cyclospora | | | | |
| — อักเสบปานกลาง: **Salmonella, Campylobacter**, Aeromonas, V. parahaemolyticus | | | | |
| — อักเสบรุนแรง: **Shigella, EIEC, E. histolytica**, anthrax | | | | |
| **Systemic infection**: hepatitis, measles, listeriosis, legionellosis, toxic shock, SARS-CoV-2 ฯลฯ | ท้องเสียถูก **กลบด้วยอาการของโรคหลัก** | | | |

### อ่านตารางอย่างไร
- **Toxin** เกาะแค่ผิว ไม่ทำลายเซลล์ → เปลี่ยนสัญญาณในเซลล์ให้ **หลั่งน้ำ (secretory)** → ถ่ายน้ำปริมาณมาก ไม่มีเม็ดเลือดขาว ไม่มีไข้
- **Preformed toxin** กินเข้าไปพร้อมอาหาร ออกฤทธิ์ทันที → **อาเจียนเด่นภายในไม่กี่ชั่วโมง** หลายคนป่วยพร้อมกัน
- **Enterotoxin** เชื้อต้องเพิ่มจำนวนในลำไส้ก่อน → อาการ 1–3 วัน
- **Cytotoxin** ทำลายเซลล์เยื่อบุ → ปวดมาก อาจมีเลือด · **Shiga toxin ของ EHEC** เข้ากระแสเลือดทำลาย endothelium → **HUS** (ไตวาย เกล็ดเลือดต่ำ เม็ดเลือดแดงแตก)
- **Invasive** เชื้อเข้าเซลล์และใต้เยื่อบุ → อักเสบ แผล → **ไข้ ปวดบิด ปวดเบ่ง มูกเลือด เม็ดเลือดขาวในอุจจาระ** = **dysentery**

### Viral diarrhea
- **Rotavirus · calicivirus (norovirus, sapovirus) · enteric adenovirus · astrovirus**
- ติดต่อง่ายมาก: คนสู่คน อาหาร น้ำ ละอองฝอย และพื้นผิวสิ่งของ
- ระยะฟักตัว **24–60 ชม.** ป่วย 12–60 ชม. **อาเจียนบ่อย**
- **Rotavirus**: อาเจียนนำ → ถ่ายเป็นน้ำ ไข้ 1 ใน 3 นาน 5–7 วัน
- **Norovirus**: คลื่นไส้ อาเจียน ท้องเสีย **1–3 วัน** (ระบาดในเรือสำราญ หอพัก)
- **Enteric adenovirus**: ฟักตัว 8–10 วัน ป่วยได้ถึง 2 สัปดาห์
- รักษา: **ประคับประคอง** + ยาลดการหลั่ง (antisecretory)
""",
    ["Toxin: อาเจียน/น้ำมาก ไม่มีไข้ · invasive: ไข้ ปวดบิด มูกเลือด",
     "Preformed toxin (B. cereus, S. aureus) อาการภายในไม่กี่ชั่วโมง · enterotoxin (cholera, ETEC) 1–3 วัน",
     "Cytotoxin: C. difficile, EHEC — ปวดมาก · EHEC → HUS",
     "Dysentery รุนแรง: Shigella, EIEC, E. histolytica",
     "Norovirus 1–3 วัน · rotavirus 5–7 วัน อาเจียนนำ"],
    [mcq(N(8), "Which feature best distinguishes diarrhoea caused by an invasive organism such as Shigella from diarrhoea caused by an enterotoxin such as that of Vibrio cholerae?",
         ["High fever with small-volume bloody stools and faecal leukocytes", "Large-volume watery stools without fever", "Onset within 2 hours of eating", "Prominent vomiting with little abdominal pain", "Normal colonic mucosa on sigmoidoscopy"], 0,
         "เชื้อ **invasive** บุกเข้าเซลล์เยื่อบุลำไส้ใหญ่ → เซลล์ตาย แผล อักเสบ → **ไข้สูง ปวดบิด ปวดเบ่ง ถ่ายน้อยถี่มีมูกเลือด และเม็ดเลือดขาวในอุจจาระ** (ตาราง: ไข้ 3–4+)\n\n**Enterotoxin ของ cholera** เกาะผิวเซลล์ลำไส้เล็กโดยไม่ทำลายเซลล์ → เพิ่ม cAMP → หลั่ง Cl และน้ำ → **ถ่ายน้ำปริมาณมาก ไม่มีไข้** เยื่อบุปกติ\n\nอาการภายใน 2 ชม. และอาเจียนเด่น = preformed toxin",
         "Invasive = ไข้ + มูกเลือด + WBC ในอุจจาระ", "Pathophysiology", R("Pathogen, pathophysiology & presentation"), NLN + ["2.3.1(7)"]),
     mcq(N(9), "A 45-year-old woman develops bloody diarrhoea 4 days after eating an undercooked hamburger. Five days later she becomes oliguric with a platelet count of 40,000/µL and schistocytes on the blood smear. Which toxin explains these findings?",
         ["Shiga toxin acting on vascular endothelium", "Cholera toxin activating adenylate cyclase", "Heat-stable toxin activating guanylate cyclase", "Emetic toxin acting on vagal afferents", "Toxin B glucosylating Rho GTPases in colonocytes"], 0,
         "เนื้อบดไม่สุก → **EHEC O157:H7** ปล่อย **Shiga toxin** → ทำลายเยื่อบุลำไส้ (ถ่ายเป็นเลือด) แล้วเข้ากระแสเลือด จับ **endothelium ของไต** → microthrombi → **HUS** (ไตวาย + เกล็ดเลือดต่ำ + schistocyte)\n\n- Cholera toxin (cAMP) และ ST ของ ETEC (cGMP) ทำให้ถ่ายเป็นน้ำ ไม่มีเลือด\n- Emetic toxin ของ B. cereus ทำให้อาเจียน\n- Toxin B ของ C. difficile ทำลายเซลล์ลำไส้ใหญ่แต่ไม่ทำให้ HUS\n\n**ACG 2016: ห้ามให้ยาปฏิชีวนะใน STEC** เพราะเชื้อที่ตายปล่อย toxin เพิ่ม เสี่ยง HUS",
         "เนื้อบด → ถ่ายเลือด → HUS = Shiga toxin (EHEC) · ห้ามยาปฏิชีวนะ", "Cytotoxin-producing organisms", R("Pathophysiology") + ["ACG Clinical Guideline: Acute diarrheal infections in adults (2016)"], NLN + ["2.3.1(7)"]),
     mcq(N(10), "A family of four develops vomiting followed by watery diarrhoea 36 hours after a shared meal. All recover within 2 days. What is the most likely cause?",
         ["Norovirus", "Entamoeba histolytica", "Clostridioides difficile", "Shigella dysenteriae", "Giardia lamblia"], 0,
         "**ระยะฟักตัว 24–60 ชม. · อาเจียนนำ · ถ่ายเป็นน้ำ · หายใน 1–3 วัน · หลายคนในบ้านป่วย** = **norovirus** (ติดง่ายมาก ปริมาณเชื้อเพียงเล็กน้อยก็ติดได้)\n\n- E. histolytica และ Giardia ฟักตัวเป็นสัปดาห์และป่วยนาน\n- Shigella ไข้ ถ่ายเป็นมูกเลือด\n- C. difficile สัมพันธ์กับยาปฏิชีวนะ",
         "อาเจียนนำ หายใน 1–3 วัน ระบาดในกลุ่ม = norovirus", "Viral diarrhea", R("Viral diarrhea"), NLN + ["2.3.1(7)"]),
    ], NLN + ["2.3.1(7)", "B8.2.2(4)"])

# ───────────────────────────── 6
sec("gi-dia-06", "Approach to acute diarrhea — ใครต้องส่งตรวจ ใครต้องได้ยา",
    "ทุกรายแก้ขาดน้ำก่อน (ORS) · red flags: ไข้ ≥ 38.3 °C > 72 ชม. · มูกเลือด · เดินทาง · ปวดรุนแรง · sepsis · ภูมิต่ำ · เพิ่งนอนรพ./ได้ยาปฏิชีวนะ · ระบาด · ไม่มี + < 7 วัน → ORS ± loperamide", 10,
"""### ขั้นตอน (Meisenheimer, Am Fam Physician 2022)
1. **ถ่ายเหลวหรือเป็นน้ำ ≥ 3 ครั้ง/วัน**
2. **ประเมินและแก้ภาวะขาดน้ำก่อนเสมอ — ให้ทางปากเป็นหลัก**
3. ถามหา **สัญญาณอันตราย (red flags)** ข้อใดข้อหนึ่ง
   - **ไข้ ≥ 38.3 °C นาน ≥ 72 ชม.**
   - **ถ่ายเป็นเลือดหรือมูก**
   - **เพิ่งเดินทาง**
   - **ปวดท้องรุนแรง**
   - **อาการของ sepsis**
   - **ภูมิคุ้มกันบกพร่อง**
   - **เพิ่งนอนโรงพยาบาลหรือได้ยาปฏิชีวนะ**
   - **เสี่ยงต่อการระบาด** (ผู้สัมผัสอาหาร บุคลากรการแพทย์ ศูนย์เด็กเล็ก)
4. **ไม่มี red flag**
   - อาการ **< 7 วัน** → **ORS + loperamide หรือ bismuth subsalicylate** · ไม่ดีขึ้น → เพาะเชื้ออุจจาระ
   - อาการ **≥ 7 วัน** → **เพาะเชื้ออุจจาระ** → ยาปฏิชีวนะตามผล
5. **มี red flag**
   - **เพิ่งเดินทาง**: อาการน้อย → ORS/loperamide · ปานกลาง–รุนแรงไม่มีเลือด → **ยาปฏิชีวนะได้เลย** · มีเลือด → เพาะเชื้อแล้วให้ยา
   - **ไม่ได้เดินทาง**: ไข้ ± มูกเลือด, หรือมีเลือดไม่มีไข้, ภูมิต่ำ, เสี่ยงระบาด → **เพาะเชื้ออุจจาระ** แล้วให้ยาตามเชื้อ

### ACG 2016 — ความรุนแรงวัดจากผลกระทบต่อชีวิตประจำวัน
| ระดับ | นิยาม |
|---|---|
| **Mild** | ทำกิจวัตรได้ตามปกติ |
| **Moderate** | ทำได้ แต่ต้องปรับเปลี่ยนกิจกรรมเพราะอาการ |
| **Severe** | **ทำอะไรไม่ได้เลย** เพราะท้องเสีย |

| ลักษณะ | แนวทาง ACG 2016 |
|---|---|
| ทุกราย | **สารน้ำและเกลือทางปาก** · อาหาร: ซุป น้ำแกงใส แครกเกอร์ อาหารต้ม/อบ |
| Watery · mild | สารน้ำอย่างเดียว · อาจให้ **loperamide 4 มก.** ครั้งแรกเพื่อคุมการถ่าย |
| Watery · mod–severe · เดินทาง | **ยาปฏิชีวนะ** |
| Watery · mod–severe · ไม่ได้เดินทาง · ไข้ ≤ 100 °F (37.8 °C) หรือไข้ ≥ 101 °F < 72 ชม. | **loperamide ไม่เกิน 48 ชม.** |
| Watery · ไข้ ≥ 101 °F (38.3 °C) **≥ 72 ชม.** | **ตรวจหาเชื้อ** |
| **Dysentery** · ไม่มีไข้หรือไข้ต่ำ | **ตรวจหาเชื้อก่อน แล้วให้ยาตามเชื้อ ยกเว้น STEC** |
| **Dysentery** · รุนแรง + ไข้ ≥ 101 °F · เดินทาง | **Azithromycin 1 g ครั้งเดียว** หรือ **500 มก. วันละครั้ง 3 วัน** |
| **ท้องเสียเกิน 14–30 วัน (persistent)** | เพาะเชื้อ หรือตรวจ multiplex PCR → ให้ยาตามเชื้อ |

### Loperamide — ใช้ได้ แต่มีเงื่อนไข
- ออกฤทธิ์ที่ **μ-opioid receptor ในลำไส้** (ไม่ผ่าน blood–brain barrier ในขนาดปกติ) → ลดการบีบไล่ เพิ่มเวลาดูดกลับ
- ขนาด: **4 มก. ครั้งแรก แล้ว 2 มก. หลังถ่ายเหลวแต่ละครั้ง ไม่เกิน 16 มก./วัน**
- **ห้ามใช้เดี่ยว ๆ เมื่อถ่ายเป็นเลือดหรือมีไข้สูง** — กักเชื้อ invasive และ toxin ไว้ในลำไส้ (เสี่ยง toxic megacolon และ HUS)
- **ห้ามในสงสัย C. difficile** และในเด็กเล็ก

### ตรวจอุจจาระเมื่อไร
- **ไม่ต้องส่งในรายส่วนใหญ่** — หายเองและเพาะเชื้อขึ้นน้อยกว่า 10%
- **ส่ง** เมื่อมี red flag, **มูกเลือด**, อาการ ≥ 7 วัน, สงสัยระบาด, หรือผู้ป่วยในหลังนอนโรงพยาบาล ≥ 3 วัน (ตรวจ C. difficile แทนการเพาะเชื้อทั่วไป)
""",
    ["แก้ขาดน้ำก่อนเสมอ ทางปากเป็นหลัก",
     "Red flags: ไข้ ≥ 38.3 °C ≥ 72 ชม. · มูกเลือด · เดินทาง · ปวดรุนแรง · sepsis · ภูมิต่ำ · นอนรพ./ยาปฏิชีวนะ · ระบาด",
     "ไม่มี red flag + < 7 วัน → ORS ± loperamide · ไม่ต้องส่งตรวจ",
     "Loperamide 4 มก. แล้ว 2 มก./ครั้ง สูงสุด 16 มก. · ห้ามใช้เดี่ยวเมื่อมีเลือด/ไข้สูง",
     "Dysentery: ตรวจหาเชื้อก่อน ให้ยาตามเชื้อ ยกเว้น STEC"],
    [mcq(N(11), "A healthy 28-year-old office worker has had 5 watery stools a day for 2 days without blood or fever. She has not travelled and has taken no antibiotics. She is drinking well and her vital signs are normal. What is the most appropriate management?",
         ["Oral rehydration and loperamide as needed, without stool testing", "Stool culture and empirical ciprofloxacin", "Stool ova and parasite examination before any treatment", "Intravenous normal saline and admission", "Empirical metronidazole for 7 days"], 0,
         "ไม่มี red flag ใดเลย (ไม่มีไข้ ไม่มีเลือด ไม่ได้เดินทาง ไม่ได้ยาปฏิชีวนะ ภูมิปกติ) และป่วย **< 7 วัน** → ตาม AFP 2022/ACG 2016 **ให้สารน้ำทางปาก ± loperamide** โดย **ไม่ต้องส่งตรวจอุจจาระ** เพราะส่วนใหญ่หายเองและเพาะเชื้อขึ้นน้อย\n\n- ยาปฏิชีวนะเชิงประจักษ์ในท้องเสียทั่วไปที่ไม่ได้เดินทางไม่เกิดประโยชน์ และเพิ่มเชื้อดื้อยา/C. difficile\n- ยังดื่มได้ สัญญาณชีพปกติ → ไม่ต้องให้ IV",
         "ไม่มี red flag + < 7 วัน → ORS ± loperamide ไม่ต้องตรวจ", "Approach to acute diarrhea", R("Approach to diarrhea (AFP 2022)") + ["Meisenheimer ES et al. Am Fam Physician 2022;106:72–80"], NLN + ["B8.4(4)"]),
     mcq(N(12), "A 35-year-old man has fever of 39 °C, abdominal cramps and frequent small stools with visible blood for 2 days. Which drug should be avoided as monotherapy?",
         ["Loperamide", "Oral rehydration solution", "Paracetamol", "Azithromycin", "Zinc supplement"], 0,
         "ถ่ายเป็นเลือด + ไข้สูง = **dysentery จากเชื้อ invasive** (Shigella, Campylobacter, EIEC, EHEC)\n\n**Loperamide ลดการบีบไล่ → กักเชื้อและ toxin ไว้ในลำไส้นานขึ้น** → อาจทำให้โรครุนแรงขึ้น เกิด toxic megacolon และเพิ่มความเสี่ยง HUS ใน EHEC → แนวทาง CDC/ACG: **ไม่ใช้ยาหยุดการเคลื่อนไหวเพียงอย่างเดียวในผู้ป่วยที่ถ่ายเป็นเลือดหรือมีไข้**\n\nORS ให้ทุกราย · azithromycin เป็นยาที่เลือกในหลายกรณีของ dysentery (หลังส่งเพาะเชื้อ)",
         "เลือด + ไข้ → ห้าม loperamide เดี่ยว", "Antimotility agents", R("Traveller's diarrhea — treatment") + ["CDC Yellow Book — Travelers' diarrhea"], NLN + ["B8.4(4)"]),
    ], NLN + ["3.1.8", "B8.4(4)", "2.3.1(7)"])

# ───────────────────────────── 7
sec("gi-dia-07", "ORS และการแก้ภาวะขาดน้ำ — ทำไมต้องใส่น้ำตาล",
    "SGLT1 ดูด Na + glucose คู่กันและยังทำงานแม้ใน cholera · น้ำตามไป · ORS ทำเอง: เกลือ 1 ช้อนชา + น้ำตาล 8 ช้อนชา + น้ำ 1 ลิตร · reduced osmolarity 245 mOsm/L · ช็อก → IV ก่อน", 9,
"""### กลไกที่ทำให้ ORS ได้ผล
- เยื่อบุลำไส้เล็กมีตัวพา **SGLT1** ที่ขน **glucose 1 โมเลกุลคู่กับ Na⁺ 2 ตัว** เข้าเซลล์
- glucose ออกทาง **GLUT2** ด้านหลอดเลือด · Na⁺ ถูกปั๊มออกโดย **Na⁺/K⁺-ATPase** · **Cl⁻ และน้ำตามไป** เพราะแรงดันออสโมติก
- **จุดสำคัญ** — toxin ของ cholera และ ETEC เปิดช่อง Cl⁻ (CFTR) ให้หลั่งน้ำ แต่ **ไม่ได้ทำลาย SGLT1** → ให้น้ำตาลคู่กับเกลือ ลำไส้จึง **ยังดูดน้ำกลับได้มากกว่าที่หลั่ง**
- ดื่มน้ำเปล่าหรือเกลืออย่างเดียวไม่ได้ผลเท่า · **น้ำอัดลมและเครื่องดื่มเกลือแร่สำหรับนักกีฬา** มีน้ำตาลสูง Na ต่ำ → osmolarity สูงดึงน้ำเข้าโพรงลำไส้ ท้องเสียมากขึ้น

### สูตร ORS
| ส่วนประกอบ (mmol/L) | เกณฑ์ WHO | สูตรมาตรฐานเดิม | **สูตรลดออสโมลาริตี (ปัจจุบัน)** |
|---|---|---|---|
| Glucose | ≤ 111 | 111 | **75** |
| Sodium | 60–90 | 90 | **75** |
| Chloride | 50–80 | 80 | **65** |
| Potassium | 15–25 | 20 | **20** |
| Citrate | 8–12 | 10 | **10** |
| **Total osmolarity (mOsm/L)** | 200–310 | 311 | **245** |

**สูตรลดออสโมลาริตี** (WHO 2002) ลดปริมาณอุจจาระ อาเจียน และความจำเป็นต้องให้ IV เมื่อเทียบกับสูตรเดิม เพราะ **ไม่ดึงน้ำเข้าโพรงลำไส้** · citrate (หรือ bicarbonate) ช่วยแก้ภาวะเลือดเป็นกรด · K แก้ K ที่เสียไปกับอุจจาระ

### ORS ทำเองที่บ้าน (สไลด์)
**เกลือ 1 ช้อนชาปาด + น้ำตาลทราย 8 ช้อนชาปาด + น้ำต้มสุกที่ทิ้งให้เย็น 1 ลิตร (5 ถ้วย ถ้วยละ 200 มล.)**
(สูตร WHO ในภาพ: น้ำตาล 6 ช้อนชา + เกลือครึ่งช้อนชา ต่อน้ำ 1 ลิตร)

### ประเมินและแก้ภาวะขาดน้ำ
| ระดับ | สิ่งตรวจพบ | ให้อะไร |
|---|---|---|
| ไม่มี/น้อย | กระหายน้ำเล็กน้อย สัญญาณชีพปกติ | ORS ดื่มทดแทนทุกครั้งที่ถ่าย |
| ปานกลาง | ปากแห้ง ตาลึก ปัสสาวะน้อย **ชีพจรเร็ว ความดันลดเมื่อลุกนั่ง** | **ORS อย่างรวดเร็ว** ถ้าดื่มได้ |
| **รุนแรง** | **ช็อก ซึม ปัสสาวะไม่ออก** อาเจียนจนดื่มไม่ได้ | **IV isotonic crystalloid (Ringer's lactate/NSS) ทันที** แล้วเปลี่ยนเป็น ORS เมื่อดีขึ้น |

ผลทางแล็บที่พบได้: **hypokalemia** · **metabolic acidosis แบบ normal anion gap** (เสีย HCO₃⁻ ทางอุจจาระ) · prerenal AKI (BUN:Cr > 20)
""",
    ["SGLT1: glucose + 2 Na เข้าเซลล์ น้ำตามไป — ยังทำงานใน cholera",
     "ORS ทำเอง: เกลือ 1 ช้อนชา + น้ำตาล 8 ช้อนชา + น้ำ 1 ลิตร",
     "Reduced osmolarity ORS 245 mOsm/L: Na 75 glucose 75",
     "ช็อก/ดื่มไม่ได้ → IV isotonic ก่อน แล้วต่อ ORS",
     "ท้องเสียมาก → K ต่ำ + normal AG metabolic acidosis"],
    [mcq(N(13), "Why does oral rehydration solution remain effective in cholera even though the cholera toxin causes massive intestinal secretion?",
         ["Sodium-glucose cotransport through SGLT1 is not affected by the toxin, so coupled Na and glucose absorption pulls water back", "Glucose blocks the binding of cholera toxin to GM1 ganglioside", "The potassium in ORS closes the CFTR chloride channel", "Citrate in ORS inactivates adenylate cyclase", "ORS is hypertonic and draws water from the lumen by osmosis"], 0,
         "Cholera toxin → Gsα ทำงานตลอด → **cAMP สูง → CFTR เปิด หลั่ง Cl⁻ และน้ำ** แต่ **ตัวพา SGLT1 ยังปกติ**\n\nเมื่อให้ glucose คู่กับ Na⁺ → SGLT1 ขน **Na⁺ + glucose เข้าเซลล์** → Na⁺ ถูกปั๊มออกด้านหลอดเลือด glucose ออกทาง GLUT2 → **น้ำตามไปตามแรงดันออสโมติก** → ดูดกลับได้มากกว่าที่หลั่ง\n\n- glucose ไม่ได้ขัดการจับของ toxin · K และ citrate แก้การเสียเกลือแร่และภาวะกรด ไม่ได้ปิด CFTR\n- ORS ปัจจุบันเป็น **hypotonic เล็กน้อย (245 mOsm/L)** ไม่ใช่ hypertonic",
         "ORS ได้ผลเพราะ SGLT1 ยังทำงาน", "ORS physiology", R("Scientific basis for ORS"), NLN + ["B8.4(4)", "B8.1.2(4)"]),
     mcq(N(14), "Compared with the original WHO ORS (311 mOsm/L), what is the main advantage of the reduced-osmolarity ORS (245 mOsm/L)?",
         ["Less stool output and vomiting and fewer unscheduled intravenous infusions", "Higher sodium content that corrects hyponatraemia faster", "It contains no glucose, so it is safe in diabetes", "It contains bicarbonate instead of potassium", "It acts as an antisecretory agent"], 0,
         "สูตรใหม่ลด **glucose และ Na ลงเหลือ 75 mmol/L** → osmolarity 245 → **ไม่ดึงน้ำเข้าโพรงลำไส้** และยังคงอัตราส่วน Na:glucose ที่ SGLT1 ใช้ได้ดี\n\nผล: **ถ่ายน้อยลง อาเจียนน้อยลง และต้องให้ IV น้อยลง** — WHO แนะนำตั้งแต่ปี 2002\n\nNa ในสูตรใหม่ **ต่ำกว่า** สูตรเดิม · ยังมี glucose และ K · citrate ใช้แทน bicarbonate · ORS ไม่ได้ออกฤทธิ์ลดการหลั่ง",
         "ORS 245: ถ่ายน้อยลง อาเจียนน้อยลง IV น้อยลง", "ORS composition", R("ORS ทำเอง"), NLN + ["B8.4(4)"]),
    ], NLN + ["2.3.4(2)", "2.2.7", "B8.4(4)"])

# ───────────────────────────── 8
sec("gi-dia-08", "ยาปฏิชีวนะเมื่อไร — แนวทางไทย 2546 เทียบปัจจุบัน และ traveler's diarrhea",
    "ข้อบ่งชี้: shigellosis · cholera · traveler's · C. difficile · ปรสิต · STD · ไทยปัจจุบันเชื้อดื้อ quinolone → azithromycin · amoeba: metronidazole แล้วต่อยาฆ่าซีสต์ · C. diff: vancomycin/fidaxomicin กิน", 10,
"""### แนวทางไทย พ.ศ. 2546 — อุจจาระร่วงเฉียบพลัน (< 14 วัน)
1. **ซักประวัติ ตรวจร่างกาย** — แยก **โรคที่เลียนแบบ** (ไส้ติ่งอักเสบ ปีกมดลูกอักเสบ diverticulitis peritonitis IBD ลำไส้ขาดเลือด mesenteric artery occlusion) และ **กลุ่มที่ต้องดูแลพิเศษ** (อายุ > 65 ปี, traveler's, antibiotic-associated, EHEC, ระบาด, HIV, ภูมิต่ำ, ในสถาบัน, ติดเชื้อในโรงพยาบาล, เสี่ยงติดเชื้อในกระแสเลือด)
2. **อาเจียนเด่น** → **อาหารเป็นพิษจาก toxin หรือไวรัส** → รักษาตามอาการ + ป้องกัน/แก้ขาดน้ำด้วย ORT/ORS/IVF
3. **ถ่ายเป็นน้ำ**
   - ขาดน้ำปานกลาง–รุนแรง → **ORS/IVF อย่างรวดเร็ว** + ตรวจและเพาะเชื้ออุจจาระ → **cholera: tetracycline 2 g/วัน นาน 3 วัน** · เชื้ออื่นให้ยาตามสาเหตุ
   - ไม่มี/น้อย → ORT · ไม่ดีขึ้นจึงตรวจอุจจาระ
4. **ถ่ายเป็นมูกเลือด** → **ตรวจอุจจาระด้วยกล้องจุลทรรศน์และเพาะเชื้อ**
   - ทั่วไป → **norfloxacin 400 มก. วันละ 2 ครั้ง 3 วัน**
   - **พบ trophozoite ของ E. histolytica** → **metronidazole 500 มก. วันละ 3 ครั้ง 7 วัน**
   - ไม่ดีขึ้น → ตามผลเพาะเชื้อ → **sigmoidoscopy/colonoscopy + biopsy**

### ⚠️ สิ่งที่เปลี่ยนไปจากแนวทาง 2546
| แนวทางเดิม | ปัจจุบัน | เหตุผล |
|---|---|---|
| Norfloxacin สำหรับมูกเลือด | **Azithromycin** (500 มก. วันละครั้ง 3 วัน หรือ 1 g ครั้งเดียว) · ceftriaxone ถ้ารุนแรง | **Campylobacter และ Shigella ในไทย/เอเชียดื้อ fluoroquinolone สูง** |
| Tetracycline 2 g/วัน 3 วัน สำหรับ cholera | **Doxycycline 300 มก. ครั้งเดียว** (WHO) · azithromycin 1 g ครั้งเดียว ในหญิงตั้งครรภ์/เด็ก · tetracycline 3 วันยังใช้ได้ | ยาครั้งเดียวสะดวก ลดระยะถ่ายและการแพร่เชื้อ — **สารน้ำยังเป็นหัวใจหลัก** |
| Metronidazole 7 วันสำหรับ amoebic colitis | metronidazole 7–10 วัน **แล้วต่อยาฆ่าซีสต์ในโพรงลำไส้ (paromomycin)** | metronidazole ฆ่าซีสต์ในโพรงลำไส้ได้ไม่ดี → กลับเป็นซ้ำ/ฝีตับ |

### ข้อบ่งชี้ให้ยาปฏิชีวนะ (สไลด์)
**Shigellosis · cholera · traveler's diarrhea · C. difficile colitis · ปรสิต · โรคติดต่อทางเพศสัมพันธ์** (proctitis จาก gonorrhea, chlamydia)
**ห้ามให้ใน STEC/EHEC** และไม่จำเป็นใน **Salmonella ที่ไม่รุนแรงในคนภูมิปกติ** (ยืดระยะเวลาปล่อยเชื้อ) — ให้เมื่ออายุมาก ภูมิต่ำ ลิ้นหัวใจเทียม หลอดเลือดเทียม หรือมีเชื้อในกระแสเลือด

### C. difficile (IDSA/SHEA 2021 · ACG 2021)
- ตรวจเมื่อ **ถ่ายเหลวใหม่ ≥ 3 ครั้ง/24 ชม.** ในผู้ที่ไม่มีเหตุอื่น (ไม่ได้กินยาระบาย)
- รักษาครั้งแรก: **fidaxomicin 200 มก. วันละ 2 ครั้ง 10 วัน** (แนะนำกว่า) หรือ **vancomycin กิน 125 มก. วันละ 4 ครั้ง 10 วัน**
- **Metronidazole** ใช้เฉพาะไม่รุนแรงและไม่มียาสองตัวแรก · **vancomycin ฉีดเข้าหลอดเลือดไม่ได้ผล** (ไม่ออกมาในโพรงลำไส้)
- **หยุดยาปฏิชีวนะตัวต้นเหตุ** ถ้าทำได้

### Traveler's diarrhea (CDC)
- แบคทีเรีย 80–90% (**ETEC** มากที่สุด, Campylobacter, Shigella, Salmonella, EAEC) · ไวรัส 5–15% · Giardia
- **ป้องกัน**: bismuth subsalicylate
| ระดับ | การรักษา |
|---|---|
| **Mild** | **ไม่ให้ยาปฏิชีวนะ** · loperamide หรือ bismuth subsalicylate |
| **Moderate** | ยาปฏิชีวนะได้ (FQ, **azithromycin**, rifaximin สำหรับชนิดไม่ invasive) · loperamide เสริมหรือใช้เดี่ยวได้ |
| **Severe** | **ให้ยาปฏิชีวนะ — azithromycin ดีที่สุด** · FQ/rifaximin เฉพาะที่ไม่ใช่ dysentery · ให้ครั้งเดียวได้ |

| ยา | ขนาด | ระยะเวลา |
|---|---|---|
| **Azithromycin** | **1,000 มก.** | **ครั้งเดียว** (หรือแบ่งให้) |
| Azithromycin | 500 มก. วันละครั้ง | 3 วัน |
| Levofloxacin | 500 มก. วันละครั้ง | 1–3 วัน |
| Ciprofloxacin | 750 มก. ครั้งเดียว · หรือ 500 มก. วันละ 2 ครั้ง | 1 · 3 วัน |
| Ofloxacin | 400 มก. วันละ 2 ครั้ง | 1–3 วัน |
| Rifamycin SV | 388 มก. วันละ 2 ครั้ง | 3 วัน |
| Rifaximin | 200 มก. วันละ 3 ครั้ง | 3 วัน |
""",
    ["ให้ยา: shigellosis · cholera · traveler's · C. diff · ปรสิต · STD · ห้ามใน EHEC",
     "ไทยปัจจุบัน Campylobacter/Shigella ดื้อ quinolone → azithromycin",
     "Cholera: สารน้ำคือหัวใจ + doxycycline 300 มก. ครั้งเดียว (หรือ tetracycline 3 วัน)",
     "Amoebic colitis: metronidazole แล้วต่อ paromomycin",
     "C. diff: fidaxomicin หรือ oral vancomycin 10 วัน · IV vancomycin ไม่ได้ผล",
     "Traveler's severe → azithromycin 1 g ครั้งเดียว"],
    [mcq(N(15), "A 30-year-old Thai man has fever, abdominal cramps and bloody mucoid stools for 2 days. Stool microscopy shows many leukocytes and no trophozoites. Stool culture has been sent. Which empirical antibiotic is most appropriate in Thailand today?",
         ["Azithromycin", "Norfloxacin", "Ampicillin", "Trimethoprim-sulfamethoxazole", "Oral vancomycin"], 0,
         "Dysentery (ไข้ มูกเลือด เม็ดเลือดขาวในอุจจาระ) ไม่พบ amoeba → คิดถึง **Shigella หรือ Campylobacter**\n\nแนวทางไทย 2546 ใช้ **norfloxacin** แต่ปัจจุบัน **Campylobacter ในไทยดื้อ fluoroquinolone มากกว่า 80%** และ Shigella ดื้อเพิ่มขึ้น → ยาที่เลือกคือ **azithromycin**\n\n- Ampicillin และ TMP-SMX ดื้อแพร่หลายมานาน\n- Oral vancomycin ใช้กับ C. difficile",
         "Dysentery ในไทยตอนนี้ → azithromycin (quinolone ดื้อ)", "Antibiotic choice", R("Thai guideline 2546") + ["ACG Clinical Guideline: Acute diarrheal infections in adults (2016)"], NLN + ["2.3.1(7)", "B1.7.2"]),
     mcq(N(16), "Stool microscopy of a man with 5 days of bloody diarrhoea shows motile trophozoites containing ingested red blood cells. After a course of metronidazole, what additional treatment is recommended?",
         ["A luminal amoebicide such as paromomycin", "A second course of metronidazole for 21 days", "Oral vancomycin", "Albendazole single dose", "No further treatment is needed"], 0,
         "**Trophozoite ที่กินเม็ดเลือดแดง (erythrophagocytosis)** = **E. histolytica** (แยกจาก E. dispar ที่ไม่ก่อโรค)\n\n**Metronidazole** ฆ่าตัวที่บุกเข้าเนื้อเยื่อได้ดี แต่ **ฆ่าซีสต์ในโพรงลำไส้ได้ไม่ดี** → ต้องต่อด้วย **ยาออกฤทธิ์ในโพรงลำไส้ (paromomycin, diloxanide)** เพื่อกันการกลับเป็นซ้ำและการแพร่เชื้อ\n\nแนวทางไทย 2546 เขียนเพียง metronidazole 500 มก. วันละ 3 ครั้ง 7 วัน — ปัจจุบันเพิ่มยาตัวที่สองนี้\n\nAlbendazole ใช้กับพยาธิ ไม่ใช่โปรโตซัว",
         "Amoeba: metronidazole + luminal agent", "Amoebic colitis", R("Thai guideline 2546 — E. histolytica"), NLN + ["2.3.1(7)", "B8.2.2(5)"]),
     mcq(N(17), "A traveller develops 6 watery stools a day with fever of 38.8 °C and is unable to work. There is no blood in the stool. According to CDC guidance, what is the preferred treatment?",
         ["Azithromycin, which may be given as a single 1-g dose", "Loperamide alone", "Rifaximin for 7 days", "Bismuth subsalicylate alone", "Metronidazole for 7 days"], 0,
         "ทำอะไรไม่ได้เลย = **severe traveler's diarrhea** และมี **ไข้** → **ต้องให้ยาปฏิชีวนะ** โดย **azithromycin เป็นยาที่แนะนำ** (ใช้ได้ทั้งชนิดมีและไม่มีเลือด และเชื้อในเอเชียดื้อ FQ) ให้ **1 g ครั้งเดียว** ได้\n\n- Loperamide หรือ bismuth เดี่ยว ๆ สำหรับ mild\n- Rifaximin ใช้เฉพาะชนิดไม่ invasive ไม่มีไข้ ขนาด 200 มก. วันละ 3 ครั้ง 3 วัน\n- Metronidazole สำหรับ Giardia/amoeba",
         "Traveler's severe/มีไข้ → azithromycin", "Traveler's diarrhea", R("Recommended treatment (CDC)") + ["CDC Yellow Book — Travelers' diarrhea"], NLN + ["2.3.1(7)", "B1.7.2"]),
    ], NLN + ["2.3.1(7)", "B1.7.2", "B8.4(4)"])

# ───────────────────────────── 9
sec("gi-dia-09", "Chronic diarrhea — ซักประวัติ ตรวจร่างกาย และแล็บ",
    "> 4 สัปดาห์ · ส่วนใหญ่ไม่ใช่ติดเชื้อ · ถามลักษณะอุจจาระ น้ำหนักลด ยา อาหาร ถ่ายกลางคืน · flushing + wheeze + murmur = carcinoid · แยก fatty / watery / bloody", 9,
"""### นิยามและภาพรวม
- **Chronic diarrhea = > 4 สัปดาห์** (บางตำรา 6–8 สัปดาห์)
- **ติดเชื้อเป็นสาเหตุน้อยกว่า acute** — ยกเว้น Aeromonas, Yersinia, ปรสิตและโปรโตซัว, วัณโรคลำไส้
- คำถามแรก: **ท้องเสียจริงหรือไม่** (~200 g/วัน) → **organic หรือ functional** → **ลักษณะอุจจาระ**

### ประวัติ
| ถาม | บอกอะไร |
|---|---|
| **เริ่มเมื่อไร อย่างไร** — ทันทีหรือค่อยเป็น | ทันที → ติดเชื้อ ยา · ค่อยเป็น → เรื้อรัง |
| **รูปแบบ** — เป็นต่อเนื่องหรือเป็น ๆ หาย ๆ, ระยะเวลา | เป็น ๆ หาย ๆ ตามความเครียด → IBS |
| **เดินทาง** | ปรสิต tropical sprue |
| **ปวดท้อง** | IBD, IBS, ลำไส้ขาดเลือด |
| **ลักษณะอุจจาระ** — **เลือด / น้ำ / มัน** | inflammatory / watery / fatty |
| **น้ำหนักลด** | **malabsorption หรือเนื้องอก** |
| สิ่งที่ทำให้แย่ลง — **อาหาร** (นม แป้ง หวานเทียม) | lactose, FODMAP, celiac |
| สิ่งที่ทำให้ดีขึ้น — **งดอาหารแล้วหยุดถ่ายหรือไม่** | หยุด = osmotic · ไม่หยุด = secretory |
| **ถ่ายกลางคืน / ตื่นมาถ่าย** | **organic** (ไม่ใช่ IBS) |
| ผลตรวจที่เคยทำ | — |
| **ยา** (รวมยาระบาย สมุนไพร) | **iatrogenic หรือแอบกินยาระบาย (factitious)** |
| **โรคประจำตัว** — เบาหวาน ไทรอยด์ HIV ผ่าตัด ฉายรังสี | ดูหัวข้อกลุ่มพิเศษ |

### ตรวจร่างกาย
| ระบบ | หาอะไร | คิดถึง |
|---|---|---|
| **ทั่วไป** | **ภาวะน้ำ ไข้ ภาวะโภชนาการ** | ความรุนแรง malabsorption |
| ผิวหนัง | ผื่น **หน้าแดงวูบวาบ (flushing)** · dermatitis herpetiformis · erythema nodosum | **carcinoid** · celiac · IBD |
| ไทรอยด์ | **ก้อน** | hyperthyroid · **medullary thyroid CA (calcitonin)** |
| ทรวงอก | **wheeze** | **carcinoid** |
| หัวใจ | **murmur** (ลิ้นหัวใจขวา) | **carcinoid heart disease** |
| ท้อง | ก้อน ตับโต กดเจ็บ ท้องมาน | มะเร็ง IBD (ก้อนขวาล่าง) ตับมีมะเร็งกระจาย |
| **ทวารหนัก** | **sphincter tone · FOBT · fissure · fistula** | incontinence · มะเร็ง · **Crohn (fistula)** |
| ขา | **บวมกดบุ๋ม** | **albumin ต่ำ** — malabsorption, protein-losing enteropathy |

### แล็บ
| เลือด | อุจจาระ |
|---|---|
| **CBC** — ซีด (เหล็ก B12 โฟเลต) · เม็ดเลือดขาวสูง | **น้ำหนักอุจจาระ** |
| **ESR** | **electrolyte (Na K) → osmotic gap** |
| electrolyte · **LFT (โดยเฉพาะ ALP)** · albumin/globulin | **pH** |
| **Ca · P** | **WBC/RBC · FOBT** |
| **PT** (ขาดวิตามิน K) | **ไขมัน** — Sudan stain, เชิงปริมาณ |
| TSH · serology celiac ตามข้อบ่งชี้ | **ตรวจหายาระบาย (laxative screen)** |

### ทางแยกหลัก
| ลักษณะ | กลไกย่อย |
|---|---|
| **Fatty (ถ่ายเป็นมัน)** | โรคตับอ่อน · ขาดน้ำดี · ทางเดินน้ำเหลืองอุดตัน · เยื่อบุลำไส้เล็ก |
| **Watery (ถ่ายเป็นน้ำ)** | **osmotic** · **secretory** |
| **Bloody (มูกเลือด)** | เยื่อบุ: **ติดเชื้อ** หรือ **อักเสบ** |
""",
    ["Chronic > 4 สัปดาห์ · ติดเชื้อน้อยกว่า acute",
     "ถ่ายกลางคืน น้ำหนักลด = organic",
     "งดอาหารแล้วหยุด = osmotic · ไม่หยุด = secretory",
     "Flushing + wheeze + murmur หัวใจขวา = carcinoid",
     "แยกก่อน: fatty / watery / bloody"],
    [mcq(N(18), "A 60-year-old man has 3 months of watery diarrhoea, episodes of facial flushing and wheeze. A systolic murmur is heard at the left lower sternal border, and the liver is enlarged and nodular. Which test is most appropriate next?",
         ["24-hour urinary 5-hydroxyindoleacetic acid", "Serum gastrin", "Hydrogen breath test with lactose", "Stool elastase", "Anti-tissue transglutaminase IgA"], 0,
         "**ท้องเสียเป็นน้ำ + flushing + wheeze + murmur ลิ้น tricuspid (ขอบล่างซ้ายของ sternum) + ตับโตเป็นก้อน** = **carcinoid syndrome** จาก neuroendocrine tumor ที่กระจายไปตับ\n\nserotonin จากก้อนในตับเข้ากระแสเลือดโดยตรง ไม่ถูกตับทำลาย → ตรวจ **5-HIAA ในปัสสาวะ** (สลายมาจาก serotonin)\n\n- Gastrin: Zollinger–Ellison (แผลหลายที่ + ท้องเสีย)\n- Lactose breath test: osmotic diarrhea\n- Stool elastase: ตับอ่อนบกพร่อง · anti-tTG: celiac",
         "Flushing + wheeze + murmur หัวใจขวา + ท้องเสีย → urine 5-HIAA", "Physical exam in chronic diarrhea", R("Physical examination / secretory diarrhea"), ["2.3.11-3(2)", "B8.2.2-3(1)"]),
     mcq(N(19), "Which feature in a patient with chronic diarrhoea most strongly suggests an organic rather than a functional cause?",
         ["Waking from sleep to defecate", "Abdominal pain relieved by defecation", "Alternating constipation and diarrhoea", "Symptoms worse during periods of stress", "Bloating after meals"], 0,
         "**ถ่ายตอนกลางคืนจนต้องตื่น (nocturnal diarrhea)** บ่งว่ามีโรคจริง เช่น secretory diarrhea, IBD, diabetic autonomic neuropathy — เพราะ **การหลั่งเกิดต่อเนื่องไม่ขึ้นกับอาหารหรืออารมณ์**\n\nอีกสี่ข้อเป็นลักษณะของ **IBS (functional)**: ปวดดีขึ้นหลังถ่าย ท้องผูกสลับเสีย แย่ลงตามความเครียด ท้องอืด\n\nแนวทาง IBS ไทย 2022 นับ **อาการรบกวนการนอน** เป็น alarm feature",
         "ตื่นมาถ่ายกลางคืน = organic", "Organic vs functional", R("History"), ["2.3.11-3(2)", "2.3.11(6)"]),
    ], ["2.3.11-3(2)", "B8.2.2-3(1)", "3.1.8"])

# ───────────────────────────── 10
sec("gi-dia-10", "ถ่ายเป็นน้ำเรื้อรัง — osmotic vs secretory และ stool osmotic gap",
    "Gap = 290 − 2(Na+K) · < 50 = secretory · > 100 = osmotic · ติดลบ = กิน phosphate/sulfate · stool pH < 6 = คาร์โบไฮเดรตดูดซึมไม่ได้ · งดอาหารแล้วหาย = osmotic", 10,
"""### สองกลไกของถ่ายเป็นน้ำ
| | **Osmotic** | **Secretory** |
|---|---|---|
| กลไก | **สารที่ดูดซึมไม่ได้ค้างในโพรงลำไส้ ดึงน้ำไว้** | **เยื่อบุหลั่ง Cl⁻/HCO₃⁻ และน้ำออกมา** หรือดูดกลับไม่ได้ |
| ตัวอย่างในสไลด์ | **lactose intolerance** | **neuroendocrine tumor** · ติดเชื้อ |
| **งดอาหาร** | **หยุดถ่าย** | **ยังถ่ายต่อ** |
| ถ่ายกลางคืน | ไม่ค่อย | **มี** |
| ปริมาณ | มักไม่เกิน 1 L/วัน | **มาก ได้หลายลิตร** |
| **Stool osmotic gap** | **> 100 mOsm/kg** | **< 50 mOsm/kg** |

### คำนวณ stool osmotic gap
**Gap = 290 − 2 × (Na⁺ + K⁺ ในอุจจาระ)**
- ใช้ **290** แทนค่า osmolality ที่วัดได้ เพราะอุจจาระในลำไส้มี osmolality เท่ากับพลาสมา (ค่าที่วัดจริงสูงขึ้นหลังเก็บเพราะแบคทีเรียหมักต่อ)
- คูณ 2 เพื่อรวม anion ที่จับคู่กับ Na และ K
- **< 50** → osmolality เกือบทั้งหมดมาจากเกลือ = **secretory**
- **> 100** → มีสารอื่นที่ไม่ใช่เกลือมาดึงน้ำ = **osmotic**
- **ค่าติดลบ** → กิน **anion หลายประจุที่ดูดซึมได้น้อย** เช่น **phosphate หรือ sulfate** (ยาระบาย)

### Osmotic diarrhea
- **กินสารที่ดูดซึมไม่ได้** — ยาระบาย Mg, PEG, sorbitol/xylitol/mannitol (หมากฝรั่งไม่มีน้ำตาล), lactulose
- **คาร์โบไฮเดรตดูดซึมไม่ได้** — **lactase deficiency**, fructose
- หลังผ่าตัด
- **Stool pH < 6** → คาร์โบไฮเดรตถูกแบคทีเรียในลำไส้ใหญ่หมักเป็น **กรดไขมันสายสั้น + CO₂ + H₂** → ท้องอืด ลมมาก
- สืบค้น: **laxative screen** (Mg, phosphate, sulfate, PEG ในอุจจาระ) · **pH** · ทบทวนอาหาร · **hydrogen breath test** ด้วย lactose · lactase ในชิ้นเนื้อเยื่อบุ · reducing substances

### Secretory diarrhea
- **เนื้องอกต่อมไร้ท่อ** — **VIPoma** · **carcinoid** (serotonin) · **gastrinoma** · **medullary thyroid CA** (calcitonin) · mastocytosis (histamine) · pheochromocytoma
- มะเร็งที่ไม่ใช่ต่อมไร้ท่อ (villous adenoma ใน rectum)
- **Chronic idiopathic secretory diarrhea · diabetic diarrhea · alcoholic diarrhea**
- **ติดเชื้อ** (Cryptosporidium, Giardia, ฯลฯ) · bile acid diarrhea · microscopic colitis · ยา
- สืบค้น
  1. **ตัดการติดเชื้อ** — เพาะเชื้อ (รวม Aeromonas, Plesiomonas) · ไข่พยาธิ · Giardia/Cryptosporidium antigen · ย้อมพิเศษหา Cyclospora, coccidia, microsporidia
  2. **ตัดโรคโครงสร้าง** — CT/MRI · **sigmoidoscopy/colonoscopy + biopsy** (microscopic colitis ต้องตัดชิ้นเนื้อ แม้ตาเปล่าปกติ) · biopsy + ดูดน้ำในลำไส้เล็กเพาะเชื้อ (SIBO) · capsule endoscopy
  3. **ตรวจเฉพาะ** — plasma **gastrin, calcitonin, VIP, somatostatin, chromogranin A** · ปัสสาวะ **5-HIAA, metanephrine, histamine** · TSH · ACTH stimulation · SPEP, immunoglobulin
  4. **ลองรักษา** — **ยาจับกรดน้ำดี** (cholestyramine) ถ้าสงสัย bile acid diarrhea
""",
    ["Gap = 290 − 2(Na+K) · < 50 secretory · > 100 osmotic · ติดลบ = phosphate/sulfate",
     "Osmotic: งดอาหารแล้วหาย · secretory: ไม่หาย ถ่ายกลางคืน ปริมาณมาก",
     "Stool pH < 6 = คาร์โบไฮเดรตดูดซึมไม่ได้ (lactose)",
     "Secretory: ตัดติดเชื้อ → โครงสร้าง (colonoscopy + biopsy) → hormone",
     "Microscopic colitis: colonoscopy ปกติ ต้อง biopsy"],
    [mcq(N(20), "A 40-year-old woman with chronic watery diarrhoea has stool Na 30 mmol/L and K 25 mmol/L. Her diarrhoea stops during a 48-hour fast. Stool pH is 5.4. What is the most likely diagnosis?",
         ["Lactose (carbohydrate) malabsorption", "VIPoma", "Microscopic colitis", "Carcinoid syndrome", "Bile acid diarrhoea"], 0,
         "**Gap = 290 − 2(30 + 25) = 290 − 110 = 180 mOsm/kg → > 100 = osmotic**\n\nข้อมูลสนับสนุนอีกสองอย่าง: **หยุดถ่ายเมื่องดอาหาร** (ไม่มีสารดึงน้ำเข้ามา) และ **pH < 6** (แบคทีเรียหมักคาร์โบไฮเดรตเป็นกรด) → **คาร์โบไฮเดรตดูดซึมไม่ได้ เช่น lactose**\n\nVIPoma, carcinoid, microscopic colitis และ bile acid diarrhea เป็น **secretory** → gap < 50 และยังถ่ายแม้งดอาหาร",
         "Gap > 100 + งดอาหารหาย + pH < 6 = carbohydrate malabsorption", "Stool osmotic gap", R("Watery diarrhea / osmotic diarrhea"), ["2.3.11-3(2)", "3.1.8"]),
     mcq(N(21), "A 50-year-old man has profuse watery diarrhoea of about 4 L/day that continues during fasting. Laboratory tests show K 2.6 mmol/L, low gastric acid output and a stool osmotic gap of 20 mOsm/kg. Which hormone is most likely elevated?",
         ["Vasoactive intestinal peptide", "Gastrin", "Calcitonin", "Somatostatin", "Cholecystokinin"], 0,
         "**Gap 20 (< 50) + ถ่ายต่อแม้งดอาหาร + ปริมาณมาก** = **secretory diarrhea**\n\nร่วมกับ **K ต่ำ และกรดในกระเพาะต่ำ** = **WDHA (Watery Diarrhea, Hypokalemia, Achlorhydria)** = **VIPoma** — VIP กระตุ้น cAMP ในเยื่อบุลำไส้ (คล้าย cholera toxin) และยับยั้งการหลั่งกรด\n\n- **Gastrin** สูง (gastrinoma) → **กรดมาก** แผลหลายที่ ไม่ใช่ achlorhydria\n- Calcitonin: medullary thyroid CA · somatostatinoma: นิ่ว steatorrhea เบาหวาน",
         "WDHA = VIPoma", "Secretory diarrhea", R("Secretory diarrhea"), ["2.3.11-3(2)", "B8.2.2-3(1)"]),
     mcq(N(22), "A young woman with recurrent watery diarrhoea has stool Na 120 mmol/L and K 40 mmol/L, giving a markedly negative osmotic gap. What is the most likely explanation?",
         ["Ingestion of a sodium phosphate or sulfate laxative", "VIPoma", "Lactulose ingestion", "Lactase deficiency", "Diabetic autonomic neuropathy"], 0,
         "Gap = 290 − 2(120 + 40) = 290 − 320 = **−30 (ติดลบ)**\n\nค่าติดลบเกิดเมื่อ Na และ K จับคู่กับ **anion หลายประจุที่ดูดซึมได้น้อย** (เช่น **phosphate, sulfate**) แทน Cl⁻ หนึ่งประจุ ทำให้สูตรประเมิน osmolality จากเกลือสูงเกินจริง → นึกถึง **แอบกินยาระบาย (surreptitious laxative)** → ตรวจ laxative screen\n\nLactulose และ lactase deficiency ให้ gap **สูง** (osmotic) · VIPoma และ diabetic diarrhea ให้ gap ต่ำแต่ไม่ติดลบ",
         "Gap ติดลบ = phosphate/sulfate laxative", "Negative osmotic gap", R("Watery diarrhea"), ["2.3.11-3(2)", "B8.4(5)"]),
    ], ["2.3.11-3(2)", "B8.2.2-3(1)", "3.1.8"])

# ───────────────────────────── 11
sec("gi-dia-11", "ถ่ายเป็นมัน — steatorrhea และ malabsorption",
    "ต้องเสียหน้าที่ตับอ่อน ≥ 90% · fat > 7 g/วัน (> 14 g แน่นอน) · Sudan stain · luminal (ตับอ่อน น้ำดี SIBO) · mucosal (celiac Whipple) · lymphatic · ตรวจ elastase ลองให้เอนไซม์", 10,
"""### ลักษณะ
- **อุจจาระมัน ลอยน้ำ กลิ่นเหม็นมาก ล้างชักโครกไม่ลง** มีหยดน้ำมันลอย
- ไขมันดูดซึมผิดปกติ **เด่นกว่าสารอาหารอื่น** · ตับอ่อนต้อง **เสียหน้าที่ส่วน exocrine ไปอย่างน้อย 90%** จึงถ่ายเป็นมัน
- อาการขาด **วิตามินที่ละลายในไขมัน (A D E K)** — ตาบอดกลางคืน กระดูกบาง เลือดออกง่าย (PT ยาว) · น้ำหนักลด

### วัดไขมันในอุจจาระ
| วิธี | เกณฑ์ |
|---|---|
| **เชิงปริมาณ 72 ชม.** (กินไขมัน ~100 g/วัน) | **> 7 g/วัน หรือ > 9% ของที่กิน = ผิดปกติ** · **> 14 g/วัน = fat malabsorption/maldigestion ชัด** (7–14 g ความจำเพาะต่ำ เพราะท้องเสียเองก็ทำให้ไขมันออกมามากขึ้นได้) |
| **Sudan stain** (อุจจาระครั้งเดียว) | เชิงคุณภาพ |
| กึ่งปริมาณ | นับ **จำนวนและขนาดหยดไขมัน** |

### สามขั้นของการดูดซึมไขมัน — เสียขั้นไหนก็ถ่ายเป็นมัน
| ขั้น | สิ่งที่ต้องมี | โรค |
|---|---|---|
| **1. ย่อยในโพรงลำไส้ (luminal)** | **lipase ตับอ่อน** + **กรดน้ำดี** ทำ micelle | **ตับอ่อนอักเสบเรื้อรัง** มะเร็งตับอ่อน cystic fibrosis · **ทางเดินน้ำดีอุดตัน ตับแข็ง** · **ตัด ileum > 100 ซม.** · **SIBO** (แบคทีเรียแยกกรดน้ำดี) · gastrinoma (กรดทำลาย lipase) |
| **2. ดูดเข้าเยื่อบุ (mucosal)** | ผิว villi ปกติ | **celiac disease** · tropical sprue · **Whipple** · Crohn ลำไส้เล็ก · ลำไส้เล็กสั้น · Giardia |
| **3. ส่งออกทางน้ำเหลือง (lymphatic)** | lacteal → ท่อน้ำเหลือง | **intestinal lymphangiectasia** · **lymphoma** · Whipple · หัวใจล้มเหลวด้านขวา/เยื่อหุ้มหัวใจรัด |
| ผสม | — | ผ่าตัดกระเพาะ เบาหวาน AIDS |

### สืบค้นถ่ายเป็นมันเรื้อรัง (สไลด์)
1. **ตัดโรคโครงสร้าง** — **CT หรือ MRI ช่องท้อง** (ตับอ่อนมีหินปูน ก้อน) · **biopsy ลำไส้เล็ก + ดูดน้ำเพาะเชื้อเชิงปริมาณ** (SIBO)
2. **ตัดตับอ่อนบกพร่อง (pancreatic exocrine insufficiency)** — **ลองให้เอนไซม์ตับอ่อน** · **stool elastase** (< 200 μg/g ผิดปกติ) หรือ chymotrypsin · secretin test
3. **ตัดการขาดกรดน้ำดีในลำไส้เล็ก** — **ลองให้กรดน้ำดีเสริม** · วัดกรดน้ำดีในน้ำจาก duodenum หลังอาหาร

**D-xylose test** (แบบคลาสสิก) — xylose ดูดซึมได้โดยไม่ต้องใช้เอนไซม์ตับอ่อน → **ผิดปกติในโรคเยื่อบุ** ปกติในโรคตับอ่อน

### กับดักเรื่อง ileum
| ตัด terminal ileum | กลไก | รักษา |
|---|---|---|
| **< 100 ซม.** | กรดน้ำดีลงลำไส้ใหญ่ → **กระตุ้นการหลั่งน้ำ** (bile acid diarrhea = secretory) | **cholestyramine** |
| **> 100 ซม.** | ตับสร้างทดแทนไม่ทัน → **กรดน้ำดีพร่อง** → ไขมันย่อยไม่ได้ → **steatorrhea** | อาหารไขมันต่ำ MCT · **cholestyramine ทำให้แย่ลง** |
""",
    ["ถ่ายเป็นมันเมื่อเสียหน้าที่ตับอ่อน ≥ 90%",
     "Fecal fat > 7 g/วัน ผิดปกติ · > 14 g ชัดเจน",
     "Luminal (ตับอ่อน น้ำดี SIBO) · mucosal (celiac Whipple) · lymphatic (lymphangiectasia lymphoma)",
     "Stool elastase + ลองให้เอนไซม์ = ตัดตับอ่อน",
     "D-xylose ผิดปกติ = เยื่อบุ · ปกติ = ตับอ่อน",
     "ตัด ileum < 100 ซม. → cholestyramine · > 100 ซม. → steatorrhea ห้าม cholestyramine"],
    [mcq(N(23), "A 52-year-old man with long-standing heavy alcohol use has bulky, greasy, foul-smelling stools and weight loss. CT shows pancreatic calcifications. Approximately what proportion of exocrine pancreatic function must be lost before steatorrhoea appears?",
         ["About 90%", "About 10%", "About 25%", "About 50%", "About 70%"], 0,
         "ตับอ่อนมีเอนไซม์ **สำรองมาก** — lipase ต้องลดลงเหลือน้อยกว่าประมาณ **10% (เสียไป ≥ 90%)** จึงย่อยไขมันไม่พอจนถ่ายเป็นมัน (สไลด์: at least 90% of pancreatic exocrine lost)\n\nผู้ป่วยรายนี้เป็น **ตับอ่อนอักเสบเรื้อรังจากเหล้า** (หินปูนในตับอ่อน) → ตรวจ **stool elastase** และให้ **pancreatic enzyme replacement**\n\nแปลว่าตับอ่อนอักเสบเรื้อรังระยะต้นอาจยังไม่ถ่ายเป็นมันแม้เนื้อตับอ่อนเสียไปมาก",
         "Steatorrhea เมื่อเสียตับอ่อน ≥ 90%", "Steatorrhea", R("Malabsorption: steatorrhea"), ["2.3.11-3(2)", "B8.1.2(4)"]),
     mcq(N(24), "A patient with steatorrhoea has an abnormal D-xylose absorption test. Which disorder is most likely?",
         ["Celiac disease", "Chronic pancreatitis", "Obstructive jaundice", "Cystic fibrosis", "Zollinger–Ellison syndrome"], 0,
         "**D-xylose เป็นน้ำตาลที่ดูดซึมได้เองผ่านเยื่อบุลำไส้เล็กโดยไม่ต้องใช้เอนไซม์ตับอ่อนหรือน้ำดี** → ถ้าดูดซึมได้น้อย = **เยื่อบุเสีย (mucosal)** เช่น **celiac disease** (villous atrophy), tropical sprue, Whipple\n\nโรคในโพรงลำไส้ — **ตับอ่อนอักเสบเรื้อรัง, cystic fibrosis** (ขาด lipase), **ทางเดินน้ำดีอุดตัน** (ขาดกรดน้ำดี), **Zollinger–Ellison** (กรดทำลาย lipase) — D-xylose ปกติ\n\n(ภาวะ SIBO ทำให้ผิดปกติได้ เพราะแบคทีเรียกิน xylose)",
         "D-xylose ผิดปกติ = เยื่อบุลำไส้เล็ก", "Malabsorption workup", R("Malabsorptive diarrhea"), ["2.3.11-3(2)", "B8.1.2(4)"]),
    ], ["2.3.11-3(2)", "B8.1.2(4)", "B8.2.2-3(1)"])

# ───────────────────────────── 12
sec("gi-dia-12", "ถ่ายมูกเลือดเรื้อรัง การติดเชื้อเรื้อรัง และกลุ่มผู้ป่วยพิเศษ",
    "Inflammatory: IBD, microscopic colitis, eosinophilic, รังสี · ส่องกล้อง + biopsy · ตัด TB ปรสิต CMV ตามภูมิ · เบาหวาน: ยา SIBO celiac · AIDS: crypto CMV MAC · ในโรงพยาบาล: C. diff ยา overflow", 9,
"""### Inflammatory diarrhea
- **มีเม็ดเลือดขาวหรือเลือดในอุจจาระ** · เยื่อบุอักเสบและฉีกขาด
- สาเหตุ: **IBD (UC, Crohn)** · eosinophilic gastroenteritis · แพ้อาหาร · **microscopic colitis** · protein-losing enteropathy · **ลำไส้อักเสบจากรังสี** · ลำไส้ขาดเลือด · มะเร็ง
- **สืบค้น**: CT/MRI · **sigmoidoscopy หรือ colonoscopy + ตัดชิ้นเนื้อ** · enteroscopy · **ตัดวัณโรค ปรสิต และไวรัสก่อนเสมอ** — ดูภูมิคุ้มกันของผู้ป่วย
  - **ห้ามให้ steroid รักษา "IBD" ก่อนตัดวัณโรคลำไส้และ amoeba** ในประเทศไทย

### ภาพจากกล้องในสไลด์
| ภาพ | ลักษณะเด่น |
|---|---|
| ปกติ | เยื่อบุเรียบ เห็นหลอดเลือด |
| **Ulcerative colitis** | อักเสบ **ต่อเนื่องจาก rectum** แดง เปราะ เลือดซึม ไม่เห็นหลอดเลือด |
| **Crohn disease** | **แผลเป็นช่วง (skip)** แผลยาว เยื่อบุนูนเป็น cobblestone |
| **Pseudomembranous colitis** | **แผ่นเหลืองนูนกระจาย** = C. difficile |
| **Ischemic colitis** | บวมแดงเป็นปล้อง มักที่ splenic flexure |
| **วัณโรค** | **ileocecal valve ผิดรูป อ้ากว้าง** แผลขวางรอบลำไส้ — ลายมือ: valve "dysfunction ไปแล้ว" · หายเมื่อรักษา |
| **NSAID colitis** | แผลตื้นเฉพาะที่ |
| **CMV** | แผลในผู้ป่วยภูมิต่ำ · ชิ้นเนื้อพบ **inclusion body ในเซลล์** |

### เชื้อที่ทำให้ท้องเสียเรื้อรัง (secretory และ inflammatory)
| กลุ่ม | เชื้อ |
|---|---|
| **โปรโตซัว** | **E. histolytica** · Dientamoeba · **Giardia** · Cyclospora · **Cryptosporidium** · **Cystoisospora** · Microsporidia · Blastocystis |
| แบคทีเรียพิเศษ | **Tropheryma whipplei** · Yersinia · Aeromonas · Plesiomonas · **C. difficile ที่กลับเป็นซ้ำ** · **Mycobacterium** |
| **พยาธิ** | **Strongyloides** · ไส้เดือน · พยาธิปากขอ · พยาธิแส้ม้า · พยาธิตืด · **Capillaria philippinensis** (กินปลาน้ำจืดดิบ — ท้องเสียเรื้อรัง โปรตีนรั่ว) |

### กลุ่มผู้ป่วยพิเศษ
| กลุ่ม | คิดถึง |
|---|---|
| **นักเดินทาง** | แบคทีเรีย (ส่วนใหญ่ acute) · **amoeba, Giardia** · tropical sprue |
| **ระบาด** | แบคทีเรีย · Brainerd diarrhea · Cryptosporidium · rotavirus |
| **เบาหวาน** | **การเคลื่อนไหวผิดปกติ (autonomic neuropathy)** · **celiac** · ตับอ่อนบกพร่อง · **SIBO** · **ยา (metformin, acarbose)** |
| **AIDS** | ยา (ARV) · **lymphoma** · **ติดเชื้อฉวยโอกาส: Cryptosporidium, CMV, HSV, Mycobacterium avium complex**, Cystoisospora, microsporidia |
| **ในสถานพยาบาล/นอนโรงพยาบาล** | **C. difficile** · **ยา** · **fecal impaction + overflow** · **ลำไส้ขาดเลือด** · **อาหารทางสายยาง** |
""",
    ["Inflammatory: colonoscopy + biopsy · ตัด TB และ amoeba ก่อนให้ steroid",
     "Pseudomembrane = C. diff · ileocecal valve ผิดรูป = TB · inclusion body = CMV",
     "AIDS: Cryptosporidium, CMV, MAC, Cystoisospora",
     "เบาหวาน: neuropathy, SIBO, celiac, metformin",
     "ในโรงพยาบาล: C. diff · ยา · overflow · ischemia · tube feeding"],
    [mcq(N(25), "A 32-year-old man with HIV infection and a CD4 count of 40 cells/µL has 2 months of profuse watery diarrhoea and weight loss. Modified acid-fast staining of the stool shows small round oocysts of 4–6 µm. What is the most likely organism?",
         ["Cryptosporidium", "Entamoeba histolytica", "Giardia lamblia", "Clostridioides difficile", "Strongyloides stercoralis"], 0,
         "**HIV CD4 ต่ำมาก + ท้องเสียเป็นน้ำเรื้อรังปริมาณมาก + oocyst กลมเล็ก 4–6 μm ติดสี modified acid-fast** = **Cryptosporidium** (ติดเชื้อฉวยโอกาสในเกณฑ์ นล.)\n\nกลไก: เกาะผิวเยื่อบุลำไส้เล็ก (enteroadherent) ทำให้ villi ฝ่อ และหลั่งน้ำ · รักษาหลักคือ **ฟื้นภูมิด้วย ART** (nitazoxanide ช่วยได้บ้าง)\n\n- Cyclospora ใหญ่กว่า (8–10 μm) · Cystoisospora เป็นรูปไข่ยาว\n- E. histolytica และ Giardia ตรวจด้วยการส่องหา trophozoite/cyst ไม่ใช่ acid-fast",
         "AIDS + ท้องเสียน้ำ + oocyst acid-fast 4–6 μm = Cryptosporidium", "Opportunistic infection", R("Infectious cause of chronic diarrhea / patients with AIDS"), ["2.3.11-3(2)", "2.3.1-3(6)"]),
     mcq(N(26), "A 38-year-old Thai woman has 4 months of intermittent diarrhoea, right lower quadrant pain, low-grade fever and weight loss. Colonoscopy shows a deformed, gaping ileocaecal valve with transverse ulcers. Before starting corticosteroids for presumed Crohn disease, which diagnosis must be excluded?",
         ["Intestinal tuberculosis", "Irritable bowel syndrome", "Lactose intolerance", "Microscopic colitis", "Carcinoid syndrome"], 0,
         "**ileocecal valve ผิดรูป อ้ากว้าง + แผลวางตัวขวางรอบลำไส้ + ไข้ น้ำหนักลด** = ลักษณะของ **วัณโรคลำไส้** ซึ่งเลียนแบบ Crohn ได้มาก (ภาพในสไลด์: TB ที่ ileocecal valve ก่อน/หลังรักษา)\n\nในไทยต้อง **ตัดวัณโรคก่อนเสมอ** (ชิ้นเนื้อ: caseating granuloma, AFB, PCR/culture · CXR) เพราะ **steroid หรือยากดภูมิทำให้วัณโรคลุกลาม**\n\nIBS, lactose intolerance, microscopic colitis และ carcinoid ไม่ทำให้เกิดแผลลักษณะนี้",
         "ileocecal valve ผิดรูป = นึกถึง TB · ตัดก่อนให้ steroid", "Inflammatory chronic diarrhea", R("Tuberculosis involve ileocecal valve"), ["2.3.11-3(2)", "2.3.1(20)"]),
    ], ["2.3.11-3(2)", "B8.2.2-3(1)", "2.3.1(12)", "2.3.1-3(6)"])

# ───────────────────────────── 13
sec("gi-dia-13", "IBS — functional diarrhea, Rome IV และแนวทางไทย 2022",
    "Rome IV: ปวดท้อง ≥ 1 วัน/สัปดาห์ใน 3 เดือน + 2 ใน 3 (สัมพันธ์การถ่าย ความถี่ ลักษณะ) · เริ่ม ≥ 6 เดือน · subtype ตาม Bristol 25% · ไม่มี alarm วินิจฉัยได้เลย · low FODMAP · ยาตามอาการเด่น", 11,
"""### IBS คืออะไร
- **ปวดท้องเป็นซ้ำ + การขับถ่ายผิดปกติ** · ปวด ท้องอืด อึดอัด ที่ **ดีขึ้นหรือแย่ลงเมื่อถ่ายหรือผายลม**
- อาจมีความถี่/ลักษณะอุจจาระเปลี่ยน ปวดเร่ง เบ่ง รู้สึกถ่ายไม่สุด
- กลไก: **แกนสมอง–ลำไส้ (gut–brain axis)** — ลำไส้ไวต่อความรู้สึก (visceral hypersensitivity) การเคลื่อนไหวผิดปกติ ความเครียดและ HPA axis แบคทีเรียในลำไส้

### เกณฑ์ Rome IV
**ปวดท้องเป็นซ้ำ เฉลี่ยอย่างน้อย 1 วันต่อสัปดาห์ ใน 3 เดือนที่ผ่านมา** ร่วมกับ **≥ 2 ข้อ**
1. **สัมพันธ์กับการถ่าย**
2. **ความถี่ของการถ่ายเปลี่ยน**
3. **ลักษณะ (รูปร่าง) อุจจาระเปลี่ยน**

**มีอาการครบเกณฑ์ใน 3 เดือนล่าสุด และเริ่มมีอาการอย่างน้อย 6 เดือนก่อนวินิจฉัย**

### Subtype — นับเฉพาะวันที่ถ่ายผิดปกติ (Bristol)
| Subtype | Bristol 1–2 (แข็ง) | Bristol 6–7 (เหลว) |
|---|---|---|
| **IBS-C** | **> 25%** | < 25% |
| **IBS-D** | < 25% | **> 25%** |
| **IBS-M** | **> 25%** | **> 25%** |
| **IBS-U** | < 25% | < 25% |
ลายมือในสไลด์: **subtype เปลี่ยนไปมาได้ตามเวลา**

### แนวทางไทย 2022 — วินิจฉัย
- **ไม่มีสัญญาณเตือน + เข้าเกณฑ์ Rome → วินิจฉัย IBS ได้เลยโดยไม่ต้องสืบค้นเพิ่ม**
- **มีสัญญาณเตือน → ส่องกล้องลำไส้ใหญ่** หรือสืบค้นเพิ่ม

**สัญญาณเตือน (alarm features) ไทย 2022**
1. เริ่มมีอาการเมื่อ **อายุ > 50 ปี**
2. **โลหิตจางจากการขาดธาตุเหล็ก**
3. **ถ่ายเป็นเลือด** ที่ไม่ได้มาจากริดสีดวงทวารหรือแผลปริขอบทวาร
4. **น้ำหนักลด > 10% ใน 3 เดือน**
5. ปวดท้องหรือถ่ายเหลว **รบกวนการนอนหลับ**
6. **ไข้**
7. ญาติสายตรงเป็น **มะเร็งลำไส้ใหญ่**
8. ญาติสายตรงเป็น **ลำไส้อักเสบเรื้อรัง (IBD)**
9. **ตรวจร่างกายผิดปกติ** — ก้อนในท้อง ก้อนในทวารหนัก ท้องมาน ต่อมน้ำเหลืองโต

### การรักษา
**ไม่ใช้ยา**
- อธิบายโรค ปัจจัยกระตุ้น และแผนการรักษา · ใยอาหาร (psyllium) · ออกกำลังกาย
- **อาหาร low FODMAP** (Fermentable Oligo-, Di-, Mono-saccharides And Polyols) — คาร์โบไฮเดรตสายสั้นที่ดูดซึมไม่ดี ถูกหมักเกิดแก๊สและดึงน้ำ
  - งดช่วงสั้น → **ไม่ดีขึ้นให้หยุด** · **ดีขึ้นให้ค่อย ๆ กลับมากินทีละรายการ** · ระวัง **ทุพโภชนาการและ eating disorder**
- อาการรุนแรงหรือไม่ตอบสนอง → **ประเมินทางจิตวิทยา**: **CBT · gut-directed hypnotherapy · psychotherapy** · mindfulness · relaxation

**ยา — เลือกตามอาการเด่น**
| | **ปวดท้อง** | **ท้องผูก** | **ท้องเสีย** |
|---|---|---|---|
| **First line** | **antispasmodic · peppermint oil** | **fiber · laxative (PEG)** | **loperamide · ondansetron** |
| **Second line** | **TCA** | secretagogue (linaclotide, lubiprostone) · 5-HT4 agonist (prucalopride) · IBAT inhibitor (elobixibat) | 5-HT3 antagonist (alosetron, ramosetron) · **rifaximin** · **bile acid sequestrant** · eluxadoline → TCA |
| ไม่ดีขึ้น | | | **ปรึกษาแพทย์ทางเดินอาหาร** |
- **TCA** ลดอาการโดยรวมและปวด · **SSRI** ลดอาการโดยรวมแต่ไม่ลดปวด
- loperamide ลดการถ่ายแต่ **ไม่ลดปวด**
""",
    ["Rome IV: ปวด ≥ 1 วัน/สัปดาห์ 3 เดือน + ≥ 2 ใน 3 (การถ่าย ความถี่ ลักษณะ) · เริ่ม ≥ 6 เดือน",
     "Subtype ตาม Bristol ที่ 25% · เปลี่ยนไปมาได้",
     "ไม่มี alarm → วินิจฉัยได้เลย · มี alarm → colonoscopy",
     "Alarm: > 50 ปี · IDA · ถ่ายเลือด · น้ำหนักลด > 10% · ตื่นกลางคืน · ไข้ · ญาติมะเร็ง/IBD · ตรวจพบผิดปกติ",
     "Low FODMAP: ไม่ดีขึ้นหยุด ดีขึ้นค่อย reintroduce",
     "IBS-D: loperamide/ondansetron → rifaximin, 5-HT3, bile acid sequestrant"],
    [mcq(N(27), "A 26-year-old woman has had abdominal pain about 2 days a week for 8 months, relieved by defecation, with loose stools on most days of abnormal bowel movements and occasional hard stools (<25%). She has no alarm features, and examination and CBC are normal. According to the Thai IBS guideline 2022, what is the next step?",
         ["Make a positive diagnosis of IBS-D and start treatment without further investigation", "Colonoscopy with random biopsies", "CT abdomen", "Stool culture and ova and parasites on three occasions", "Hydrogen breath test before any diagnosis"], 0,
         "เข้าเกณฑ์ **Rome IV**: ปวด ≥ 1 วัน/สัปดาห์ (2 วัน) นาน > 6 เดือน + สัมพันธ์กับการถ่าย + ลักษณะอุจจาระเปลี่ยน · อุจจาระเหลว > 25% และแข็ง < 25% = **IBS-D**\n\nแนวทางไทย 2022: **ไม่มีสัญญาณเตือนและเข้าเกณฑ์ Rome → วินิจฉัยได้เลย ไม่ต้องสืบค้นเพิ่ม** (อายุน้อย CBC ปกติ)\n\nการส่องกล้องหรือ CT ใช้เมื่อ **มี alarm features** — การตรวจโดยไม่มีข้อบ่งชี้เพิ่มความกังวลและค่าใช้จ่ายโดยไม่เปลี่ยนการรักษา",
         "Rome IV + ไม่มี alarm = วินิจฉัย IBS ได้เลย", "IBS diagnosis", R("Thai IBS guideline 2022: diagnosis"), ["2.3.11(6)", "B8.2.5(2)"]),
     mcq(N(28), "A 55-year-old man presents with 4 months of intermittent abdominal pain and loose stools relieved by defecation. Which finding makes colonoscopy necessary before diagnosing IBS?",
         ["Onset of symptoms after age 50", "Bloating after meals", "Symptoms worse with stress", "Relief of pain after passing flatus", "Mucus in the stool"], 0,
         "แนวทางไทย 2022: **เริ่มมีอาการเมื่ออายุ > 50 ปี** เป็น **alarm feature** → ต้อง **ส่องกล้องลำไส้ใหญ่** เพื่อตัดมะเร็งลำไส้ใหญ่ก่อนวินิจฉัย IBS\n\nนอกจากนี้อาการ **4 เดือน** ยังไม่ครบเกณฑ์ Rome IV ที่ต้องเริ่ม ≥ 6 เดือน\n\nท้องอืดหลังอาหาร แย่ลงตามความเครียด ดีขึ้นเมื่อผายลม และมีมูกในอุจจาระ พบได้ใน IBS และไม่ใช่สัญญาณเตือน",
         "อาการเริ่มหลังอายุ 50 = alarm → colonoscopy", "IBS alarm features", R("Alarm feature: Thai guideline 2022"), ["2.3.11(6)", "B8.2.5(2)"]),
     mcq(N(29), "A woman with IBS-D has pain and loose stools despite loperamide. Which agent is a recommended second-line option for her diarrhoea according to the Thai guideline?",
         ["Rifaximin", "Linaclotide", "Prucalopride", "Polyethylene glycol", "Lubiprostone"], 0,
         "ยาทางเลือกที่สองสำหรับ **IBS อาการเด่นท้องเสีย**: **5-HT3 antagonist (alosetron, ramosetron) · rifaximin · bile acid sequestrant · eluxadoline** → แล้วจึง TCA\n\n**Rifaximin** เป็นยาปฏิชีวนะที่ดูดซึมน้อย ปรับแบคทีเรียในลำไส้ ลดท้องอืดและถ่ายเหลว\n\n**Linaclotide, lubiprostone (secretagogue), prucalopride (5-HT4 agonist), PEG** ล้วนเพิ่มน้ำหรือการเคลื่อนไหว → ใช้กับ **IBS-C** จะทำให้ท้องเสียแย่ลง",
         "IBS-D second line: rifaximin, 5-HT3 antagonist, bile acid sequestrant, eluxadoline", "IBS pharmacotherapy", R("Thai IBS guideline 2022: medication"), ["2.3.11(6)", "B8.2.5(2)", "B8.4(4)"]),
    ], ["2.3.11(6)", "B8.2.5(2)"])

# ───────────────────────────── 14
sec("gi-dia-14", "ยาที่ทำให้ท้องเสีย สาเหตุที่หาไม่เจอ และยารักษาตามอาการ",
    "ยาแบ่งตามกลไก: osmotic (Mg, sorbitol, acarbose) · secretory (metformin, colchicine, misoprostol) · inflammatory (NSAID, PPI, olmesartan, ipilimumab) · steatorrhea (orlistat) · รักษาตามสาเหตุ + empirical: loperamide, cholestyramine, octreotide", 9,
"""### สาเหตุที่มักถูกมองข้าม (diarrhea of obscure origin)
**Bile acid malabsorption** · คาร์โบไฮเดรตดูดซึมไม่ได้ · chronic idiopathic secretory diarrhea · **fecal incontinence** · functional diarrhea · **iatrogenic (ยา ผ่าตัด รังสี)** · **IBS** · **microscopic colitis** · autonomic neuropathy · **ตับอ่อนบกพร่อง** · เนื้องอกหลั่ง peptide · **SIBO** · **แอบกินยาระบาย**

### ยาที่ทำให้ท้องเสีย แบ่งตามกลไก
| กลไก | ยาที่ควรจำ |
|---|---|
| **Osmotic** | **ยาระบาย Mg, antacid ที่มี Mg** · phosphate · PEG · **น้ำตาลแอลกอฮอล์ (sorbitol, xylitol, mannitol)** · **alpha-glucosidase inhibitor (acarbose, miglitol)** · fructose · อาหารทางสายยาง · prebiotic · ampicillin, clindamycin |
| **Secretory** | **metformin** · **colchicine** · **misoprostol** · digoxin, quinidine · **NSAID** · theophylline · caffeine · ยาเคมีบำบัด · olsalazine · ticlopidine · cholinesterase inhibitor · calcitonin · ยาระบาย (stimulant) |
| **Inflammatory (colitis)** | **ยาปฏิชีวนะ** (C. difficile) · **NSAID** · **PPI · SSRI · ticlopidine** (microscopic colitis) · **olmesartan** (sprue-like enteropathy) · **ipilimumab และ immune checkpoint inhibitor** · ยาเคมีบำบัด (5-FU, irinotecan, MTX) · mycophenolate · TKI · isotretinoin · ยาเม็ดคุมกำเนิด |
| **Steatorrhea** | **orlistat** (ยับยั้ง lipase) · **cholestyramine** · neomycin, polymyxin · colchicine · **octreotide** · ARV · biguanide · L-thyroxine |
(J Clin Gastroenterol 2017;51:111–117)

### การรักษา chronic diarrhea
- **รักษาตามสาเหตุ** เป็นหลัก
- **ให้ยาเชิงประจักษ์ (empirical)** เมื่อ 1) รอผลวินิจฉัย 2) สืบค้นแล้วหาสาเหตุไม่พบ 3) วินิจฉัยได้แต่ไม่มีการรักษาจำเพาะ
  - quinolone หรือ metronidazole ในบางราย (สงสัยติดเชื้อ/SIBO)
  - **เอนไซม์ตับอ่อน, กรดน้ำดีเสริม** ในถ่ายเป็นมัน
- **ประคับประคอง** — สารน้ำ เกลือแร่ โภชนาการ

### ยารักษาตามอาการ (สไลด์)
| กลุ่ม | ยา | ขนาด |
|---|---|---|
| **Opiate (μ receptor)** | **Loperamide** | **2–4 มก. วันละ 4 ครั้ง** |
| | Diphenoxylate | 2.5–5 มก. วันละ 4 ครั้ง |
| | Codeine | 15–60 มก. วันละ 4 ครั้ง |
| | Morphine | 2–20 มก. วันละ 4 ครั้ง |
| | Tincture of opium | 2–20 หยด วันละ 4 ครั้ง |
| **Enkephalinase inhibitor** | **Racecadotril** | 1.5 มก./กก. วันละ 3 ครั้ง |
| **α2-adrenergic agonist** | **Clonidine** (diabetic diarrhea) | 0.1–0.3 มก. วันละ 3 ครั้ง |
| **Somatostatin analog** | **Octreotide** (VIPoma, carcinoid, dumping) | 50–250 มคก. ฉีดใต้ผิวหนัง วันละ 3 ครั้ง |
| **Bile acid-binding resin** | **Cholestyramine** | 4 g วันละ 1–4 ครั้ง |
| | Colesevelam | 3 เม็ด วันละ 2 ครั้ง |
| | Colestipol | 4 g วันละ 1–4 ครั้ง |
| **Fiber** | Calcium polycarbophil | 5–10 g/วัน |
| | **Psyllium** | 10–20 g/วัน |

**Racecadotril** ยับยั้ง enkephalinase → enkephalin ในลำไส้อยู่นานขึ้น → **ลดการหลั่ง (antisecretory) โดยไม่ชะลอการเคลื่อนไหว** — ต่างจาก loperamide
""",
    ["Metformin, colchicine, misoprostol → secretory",
     "Mg, sorbitol, acarbose → osmotic",
     "PPI, SSRI, NSAID → microscopic colitis · olmesartan → sprue-like",
     "Orlistat → steatorrhea",
     "Racecadotril = antisecretory ไม่ชะลอการเคลื่อนไหว",
     "Octreotide: VIPoma/carcinoid · clonidine: diabetic diarrhea · cholestyramine: bile acid"],
    [mcq(N(30), "A 68-year-old woman has 3 months of watery, non-bloody diarrhoea, including at night. She takes omeprazole, sertraline and naproxen. Colonoscopy appears normal. What should be done during the colonoscopy?",
         ["Take random biopsies from the colon to look for microscopic colitis", "No biopsy is needed because the mucosa is normal", "Biopsy only the terminal ileum for Crohn disease", "Aspirate colonic fluid for bacterial culture", "Take biopsies only if polyps are seen"], 0,
         "หญิงสูงอายุ ท้องเสียเป็นน้ำเรื้อรัง ถ่ายกลางคืน และกิน **PPI + SSRI + NSAID** (ยาที่สัมพันธ์กับ microscopic colitis ในตารางยา) → คิดถึง **microscopic colitis** (collagenous/lymphocytic)\n\nโรคนี้ **เยื่อบุดูปกติด้วยตาเปล่า** วินิจฉัยได้จาก **ชิ้นเนื้อเท่านั้น** (collagen band หนาใต้เยื่อบุ หรือ lymphocyte แทรกในเยื่อบุ) → ต้อง **ตัดชิ้นเนื้อหลายตำแหน่งทั่วลำไส้ใหญ่** แม้กล้องปกติ\n\nรักษา: หยุดยาที่เป็นต้นเหตุ + budesonide",
         "ท้องเสียน้ำ + PPI/SSRI/NSAID + กล้องปกติ → random biopsy (microscopic colitis)", "Drug-induced inflammatory diarrhea", R("Drug induce inflammatory diarrhea") + ["J Clin Gastroenterol 2017;51:111–117"], ["2.3.19(2)", "2.3.11-3(2)"]),
     mcq(N(31), "How does racecadotril differ from loperamide in treating diarrhoea?",
         ["Racecadotril reduces intestinal secretion by inhibiting enkephalinase without slowing transit", "Racecadotril is a μ-opioid agonist that slows colonic transit", "Racecadotril binds bile acids in the colon", "Racecadotril is a somatostatin analogue given subcutaneously", "Racecadotril acts centrally and causes dependence"], 0,
         "**Racecadotril** ยับยั้ง **enkephalinase** → enkephalin ในลำไส้ไม่ถูกทำลาย → กระตุ้น **δ-opioid receptor** ที่เยื่อบุ → ลด cAMP → **ลดการหลั่งน้ำและเกลือแร่ (antisecretory)** โดย **ไม่ชะลอการเคลื่อนไหว** จึงไม่ค่อยทำให้ท้องผูกตามมา\n\n**Loperamide** เป็น **μ-opioid agonist** → ลดการบีบไล่ เพิ่มเวลาดูดกลับ\n\nจับกรดน้ำดี = cholestyramine · somatostatin analog = octreotide",
         "Racecadotril: antisecretory (δ) · loperamide: antimotility (μ)", "Antidiarrheal drugs", R("Treatment of chronic diarrhea"), ["B8.4(4)"]),
    ], ["2.3.11-3(2)", "2.3.19(2)", "B8.4(4)", "B8.4(5)"])

# ───────────────────────────── MEQ / OSCE
LECNAME = "Diarrhea — acute และ chronic (พญ.ธันยพร)"
MEQ = [{"id": "GI-DIA-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Acute watery diarrhoea with hypovolaemic shock — cholera: resuscitation, laboratory interpretation and antibiotics",
 "vignette": """ผู้ป่วยชายไทยอายุ 42 ปี อาชีพประมง มาด้วยถ่ายเป็นน้ำ 12 ชั่วโมง
PI: ถ่ายเป็นน้ำสีขาวขุ่นคล้ายน้ำซาวข้าว มากกว่า 15 ครั้ง ไม่ปวดท้อง ไม่มีไข้ ไม่มีมูกเลือด อาเจียน 3 ครั้ง ตะคริวที่น่อง 1 วันก่อนกินหอยแครงลวกที่ตลาด เพื่อนบ้าน 2 คนมีอาการคล้ายกัน
PE: BT 36.8 C · BP 78/50 mmHg · HR 128/min · RR 26/min · ซึม ตาลึก ปากแห้ง ผิวหนังเหี่ยว capillary refill 4 วินาที · ท้องนุ่ม ไม่กดเจ็บ เสียงลำไส้ดัง
Lab: Na 136 · K 2.9 · Cl 112 · HCO3 13 mmol/L · BUN 42 · Cr 2.1 mg/dL · Hct 54% · stool: ไม่พบเม็ดเลือดขาวและเม็ดเลือดแดง · dark-field: เชื้อเคลื่อนที่เร็ว (darting motility)""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัยที่น่าจะเป็นที่สุด และบอกกลไกที่ทำให้ถ่ายเป็นน้ำปริมาณมาก (3 คะแนน)",
   "a": """**Cholera (Vibrio cholerae)** ร่วมกับ **hypovolemic shock**
- เบาะแส: **ถ่ายน้ำซาวข้าวปริมาณมาก ไม่ปวด ไม่มีไข้** · กินอาหารทะเล · ป่วยหลายคน · อุจจาระไม่มีเม็ดเลือด · darting motility
- กลไก: **cholera toxin** จับ GM1 ที่เยื่อบุลำไส้เล็ก → ADP-ribosylate **Gsα** → adenylate cyclase ทำงานตลอด → **cAMP สูง** → เปิด **CFTR หลั่ง Cl⁻** และยับยั้งการดูด NaCl → น้ำตามออกมา (**secretory diarrhea**)
- ลำไส้เล็กหลั่งน้ำ **เกินความสามารถดูดกลับของลำไส้ใหญ่ (~4–5 L/วัน)** → ถ่ายน้ำปริมาณมาก · **เซลล์ไม่ถูกทำลาย** จึงไม่มีไข้หรือเม็ดเลือดขาว"""},
  {"q": "2. จงแปลผลแล็บ (Na K Cl HCO3 BUN Cr Hct) (3 คะแนน)",
   "a": """- **Anion gap = 136 − (112 + 13) = 11 → normal anion gap (hyperchloremic) metabolic acidosis** จากการเสีย **HCO₃⁻ ไปกับอุจจาระ** (อุจจาระใน cholera มี HCO₃⁻ สูง) — ถ้าช็อกนานจะมี lactic acidosis ซ้อน AG สูงขึ้น
- **Hypokalemia** — เสีย K ทางอุจจาระ (และ aldosterone สูงจากปริมาตรเลือดลด) · ระวัง K ต่ำลงอีกเมื่อแก้ภาวะกรด
- **BUN:Cr = 20 + Cr สูง → prerenal AKI** จากปริมาตรเลือดลด
- **Hct 54%** — เลือดข้นจากการเสียน้ำ (hemoconcentration)"""},
  {"q": "3. จงบอกการรักษาในชั่วโมงแรก และเกณฑ์ที่จะเปลี่ยนเป็น ORS (4 คะแนน)",
   "a": """- **ภาวะขาดน้ำรุนแรง + ช็อก → IV isotonic crystalloid ทันที** — WHO แนะนำ **Ringer's lactate 100 มล./กก.** ใน 3 ชั่วโมงสำหรับผู้ใหญ่ (**30 มล./กก. ใน 30 นาทีแรก** แล้ว 70 มล./กก. ใน 2.5 ชั่วโมง) · ใช้ IV line ใหญ่ 2 เส้น
- ประเมินซ้ำบ่อย: ชีพจร ความดัน ความรู้สึกตัว ปัสสาวะ · **ทดแทนน้ำที่ยังเสียต่อ** (ชั่งหรือตวงอุจจาระ)
- **เริ่ม ORS ทันทีที่ดื่มได้** (มี glucose ช่วยดูด Na ผ่าน SGLT1 ที่ยังทำงาน) · เมื่อชีพจรแรง ความดันปกติ รู้สึกตัวดี ปัสสาวะออก → เปลี่ยนเป็น ORS ทดแทนทุกครั้งที่ถ่าย
- **ให้ K ทดแทน** เมื่อปัสสาวะออก · **ห้ามให้ loperamide** · กินอาหารได้เร็ว"""},
  {"q": "4. ต้องให้ยาปฏิชีวนะหรือไม่ ถ้าให้เลือกอะไร และต้องทำอะไรด้านสาธารณสุข (2 คะแนน)",
   "a": """- **ให้** — ลดปริมาณอุจจาระ ระยะเวลาป่วย และการแพร่เชื้อ (แต่สารน้ำยังเป็นหัวใจหลัก)
- **Doxycycline 300 มก. กินครั้งเดียว** (WHO) · ทางเลือก **azithromycin 1 g ครั้งเดียว** (หญิงตั้งครรภ์/เด็ก) · tetracycline 500 มก. วันละ 4 ครั้ง 3 วัน (2 g/วัน ตามแนวทางไทย 2546) — ให้หลังผู้ป่วยหยุดอาเจียน
- **อหิวาตกโรคเป็นโรคติดต่อที่ต้องแจ้งความ** → รายงานงานระบาดวิทยา/สสจ. · สอบสวนแหล่งอาหาร (หอยแครง) · ค้นหาผู้ป่วยรายอื่น · สุขอนามัยในบ้าน"""}],
 "ref": ["สไลด์ พญ.ธันยพร — Thai guideline 2546, ORS, pathophysiology", "WHO — Cholera fact sheet / GTFCC treatment guidance", "ACG Clinical Guideline: Acute diarrheal infections in adults (2016)"],
 "nl": ["2.3.1(7)", "2.2.7", "2.3.4(2)", "2.1.18"], "years": [], "_kind": "meq", "_set": SET},
 {"id": "GI-DIA-MEQ-02", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Chronic diarrhoea — systematic approach using stool characteristics and osmotic gap",
 "vignette": """ผู้ป่วยหญิงไทยอายุ 46 ปี มาด้วยถ่ายเหลวมา 3 เดือน
PI: ถ่ายเป็นน้ำ 6–8 ครั้ง/วัน รวมกลางคืนต้องตื่นมาถ่าย 2 ครั้ง ไม่มีมูกเลือด ไม่มันลอยน้ำ ปวดท้องเล็กน้อย น้ำหนักลด 5 กก. ใน 3 เดือน ลองงดอาหาร 1 วันยังถ่ายเป็นน้ำ
ประวัติ: ไม่ได้เดินทาง ไม่ได้รับยาปฏิชีวนะ ยาประจำ: ไม่มี
PE: BW 52 kg · BP 104/68 · HR 96 · ไม่ซีด ไม่เหลือง ไม่มีผื่น ไทรอยด์ไม่โต ปอดและหัวใจปกติ ท้องนุ่ม ตับม้ามไม่โต PR: ไม่มีก้อน
Lab: CBC ปกติ · K 2.8 mmol/L · HCO3 18 · stool: ไม่พบ WBC/RBC · occult blood negative · stool Na 95, K 45 mmol/L · stool pH 7.0 · Sudan stain negative · stool weight 1,500 g/วัน""",
 "questions": [
  {"q": "1. ผู้ป่วยรายนี้ท้องเสียชนิดใด จงแสดงการคำนวณและเหตุผลประกอบ (3 คะแนน)",
   "a": """**Chronic watery diarrhea ชนิด secretory**
- Chronic: > 4 สัปดาห์ · watery: ไม่มีเลือด ไม่มีไขมัน (Sudan negative) ไม่มี WBC
- **Gap = 290 − 2(95 + 45) = 290 − 280 = 10 mOsm/kg (< 50) → secretory**
- สนับสนุน: **ยังถ่ายแม้งดอาหาร · ถ่ายกลางคืน · ปริมาณ 1.5 L/วัน · pH ไม่เป็นกรด** (ไม่ใช่คาร์โบไฮเดรต) · น้ำหนักลด = organic"""},
  {"q": "2. จงบอกแผนการสืบค้นตามลำดับ (4 คะแนน)",
   "a": """ตามแนวทางในสไลด์
1. **ตัดการติดเชื้อ** — เพาะเชื้อ (รวม Aeromonas Plesiomonas) · ไข่พยาธิ/O&P · Giardia/Cryptosporidium antigen · ย้อมหา Cyclospora microsporidia · (anti-HIV)
2. **ตัดโรคโครงสร้าง** — **colonoscopy + biopsy หลายตำแหน่งแม้เยื่อบุปกติ** (microscopic colitis) · CT/MRI ช่องท้อง (ก้อนตับอ่อน ตับ) · biopsy ลำไส้เล็กถ้าจำเป็น
3. **ตรวจเฉพาะ** — **VIP · gastrin · calcitonin · chromogranin A · somatostatin** · urine **5-HIAA** · metanephrine · **TSH**
4. **Laxative screen** แม้ gap ไม่ติดลบ (ยาระบายกระตุ้นบางชนิดเป็น secretory)
5. ถ้ายังไม่พบ → **ลองยาจับกรดน้ำดี**"""},
  {"q": "3. ผล CT พบก้อนที่หางตับอ่อน 3 ซม. และ VIP สูง จงอธิบายความสัมพันธ์กับผลแล็บ และการรักษาเบื้องต้น (3 คะแนน)",
   "a": """**VIPoma (Verner–Morrison / WDHA syndrome)**
- VIP กระตุ้น **cAMP** ในเยื่อบุลำไส้ (เหมือน cholera toxin) → หลั่งน้ำ Cl⁻ K⁺ HCO₃⁻ → **Watery Diarrhea · Hypokalemia · metabolic acidosis (normal AG)** · และยับยั้งการหลั่งกรด → **Achlorhydria**
- รักษา: **สารน้ำและ K ทดแทน** · **octreotide** (somatostatin analog) ลดการหลั่ง VIP และคุมอาการ · **ผ่าตัดเอาก้อนออก** ถ้าไม่กระจาย"""}],
 "ref": ["สไลด์ พญ.ธันยพร — chronic diarrhea, watery diarrhea, diagnostic approach to chronic secretory diarrhea, treatment of chronic diarrhea"],
 "nl": ["2.3.11-3(2)", "B8.2.2-3(1)", "3.1.8"], "years": [], "_kind": "meq", "_set": SET}]

OSCE = [{"id": "GI-DIA-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "OSCE – Counselling on oral rehydration and warning signs in acute watery diarrhoea",
 "station": "OSCE (ซักประวัติ + ให้คำแนะนำ) 6 นาที · ผู้ป่วยจำลอง",
 "instruction": """ผู้ป่วยหญิงอายุ 30 ปี ถ่ายเป็นน้ำ 5 ครั้งตั้งแต่เมื่อคืน หลังกินยำทะเลจากร้านข้างทาง ไม่มีไข้ ไม่มีมูกเลือด ยังดื่มน้ำได้ สัญญาณชีพปกติ ไม่มีโรคประจำตัว

**จงทำสิ่งต่อไปนี้**
1. ซักประวัติเพิ่มเติมเพื่อประเมินภาวะขาดน้ำและสัญญาณอันตราย
2. อธิบายวิธีเตรียมและดื่มสารละลายเกลือแร่ (ORS)
3. แนะนำเรื่องอาหาร ยา และอาการที่ต้องกลับมาพบแพทย์""",
 "answer": """| หัวข้อ | สิ่งที่ต้องทำ/พูด | คะแนน |
|---|---|---|
| **แนะนำตัว ยืนยันตัวผู้ป่วย** | บอกชื่อ บทบาท ขออนุญาต | 1 |
| **ประเมินภาวะขาดน้ำ** | ปริมาณและความถี่การถ่าย อาเจียนจนดื่มไม่ได้หรือไม่ **ปัสสาวะออกน้อยลง** หน้ามืดเวลาลุก | 2 |
| **ถาม red flags** | **ไข้ · มูกเลือด · ปวดท้องรุนแรง** · เพิ่งได้ยาปฏิชีวนะ/นอนรพ. · โรคภูมิคุ้มกันต่ำ ตั้งครรภ์ · คนกินด้วยกันป่วยหรือไม่ · อาชีพเกี่ยวกับอาหาร | 2 |
| **ORS — เตรียม** | ผงเกลือแร่ 1 ซองละลาย **น้ำต้มสุกที่เย็นแล้วตามปริมาตรบนซอง** ห้ามผสมเข้มหรือจางกว่า · ถ้าไม่มีซอง: **เกลือ 1 ช้อนชาปาด + น้ำตาล 8 ช้อนชาปาด + น้ำ 1 ลิตร** · เตรียมแล้วใช้ภายใน 24 ชม. | 2 |
| **ORS — ดื่ม** | **จิบบ่อย ๆ** ทีละน้อย · ดื่มเพิ่มทุกครั้งที่ถ่าย (ราว 1–2 แก้ว) · อาเจียน → พัก 10 นาทีแล้วจิบช้าลง · **ไม่ใช้น้ำอัดลม/เครื่องดื่มเกลือแร่สำหรับนักกีฬาแทน** (น้ำตาลสูง ทำให้ถ่ายมากขึ้น) | 2 |
| **อาหาร** | กินได้ตามปกติ อาหารอ่อน ต้ม ซุป ข้าวต้ม · เลี่ยงของมัน เผ็ด นม แอลกอฮอล์ ชั่วคราว | 1 |
| **ยา** | **ไม่จำเป็นต้องใช้ยาปฏิชีวนะ** · loperamide ใช้ได้เมื่อไม่มีไข้ไม่มีเลือด (4 มก. แล้ว 2 มก. หลังถ่ายแต่ละครั้ง ไม่เกิน 16 มก./วัน) | 1 |
| **อาการที่ต้องกลับมาทันที** | **ถ่ายเป็นเลือด · ไข้สูง · ปวดท้องมาก · อาเจียนจนดื่มไม่ได้ · ปัสสาวะออกน้อย หน้ามืด ซึม · ไม่ดีขึ้นใน 2–3 วัน** | 2 |
| **ป้องกันการแพร่** | ล้างมือด้วยสบู่หลังเข้าห้องน้ำและก่อนเตรียมอาหาร · ไม่ทำอาหารให้ผู้อื่นจนหาย | 1 |
| **ทวนความเข้าใจ** | ให้ผู้ป่วยทวนวิธีผสม ORS และอาการที่ต้องกลับมา | 1 |

**รวม 15 คะแนน** · **ข้อผิดพลาดร้ายแรง**: แนะนำให้ซื้อยาปฏิชีวนะกินเอง · ไม่บอกอาการที่ต้องกลับมาพบแพทย์""",
 "ref": ["สไลด์ พญ.ธันยพร — ORS ทำเอง, approach to diarrhea", "WHO — Oral rehydration salts (reduced osmolarity)", "ACG Clinical Guideline: Acute diarrheal infections in adults (2016)"],
 "nl": ["2.1.18", "2.3.1(7)", "B8.4(4)"], "years": [], "_kind": "meq", "_set": SET}]

LECTURE = {
 "lec": LEC, "date": "อ. 27 ต.ค. · Bedside อ.ธันยพร",
 "title": "Diarrhea — acute และ chronic",
 "subtitle": "นิยามและโรคเลียนแบบ · น้ำ 10 ลิตรในลำไส้ · กลไกของเชื้อตามความลึกที่รุกล้ำ · approach acute (AFP 2022 · ACG 2016) · ORS · ยาปฏิชีวนะ · chronic: fatty / watery (osmotic gap) / bloody · IBS Rome IV · ยาที่ทำให้ท้องเสีย",
 "objectives": [
   "นิยามท้องเสียและแยกจาก pseudodiarrhea, incontinence และ overflow รอบ fecal impaction",
   "อธิบายสมดุลน้ำในทางเดินอาหาร และใช้ปริมาณ/ลักษณะอุจจาระบอกตำแหน่งโรค",
   "อธิบายกลไกก่อโรคของเชื้อตั้งแต่ toxin จนถึง invasive และใช้ทำนายอาการ ไข้ และมูกเลือด",
   "ประเมินและดูแลผู้ป่วยท้องเสียเฉียบพลัน: แก้ขาดน้ำ ใช้ red flags เลือกผู้ที่ต้องส่งตรวจ และใช้ loperamide อย่างปลอดภัย",
   "อธิบายกลไก ORS ผ่าน SGLT1 และส่วนประกอบของสูตรลดออสโมลาริตี",
   "เลือกยาปฏิชีวนะให้เหมาะกับ cholera, dysentery, amoebiasis, C. difficile และ traveler's diarrhea ตามแนวทางปัจจุบัน",
   "สืบค้นท้องเสียเรื้อรังตามลักษณะอุจจาระ แปลผล stool osmotic gap, pH และไขมันในอุจจาระ",
   "วินิจฉัย IBS ตาม Rome IV แยกสัญญาณเตือน และเลือกการรักษาตามอาการเด่น",
   "จดจำยาที่ทำให้ท้องเสียตามกลไก และยารักษาตามอาการของท้องเสียเรื้อรัง"],
 "nlGap": "เกณฑ์ฯ มีรหัส `นล. 2.1.18` อุจจาระร่วง · `2.3.1(7)` GI infection and food-borne intoxication · `2.3.11-3(2)` Chronic diarrhea · `2.3.11(6)` IBS · `B8.4(4)` Drugs used in acute diarrhea แต่สไลด์ใช้ **แนวทางไทย พ.ศ. 2546** ซึ่ง **ยาปฏิชีวนะเปลี่ยนไปแล้ว** (norfloxacin → azithromycin เพราะเชื้อดื้อ quinolone · cholera ใช้ doxycycline ครั้งเดียว · amoeba ต้องต่อยาฆ่าซีสต์) และไม่มีการรักษา C. difficile จึงอ้างอิงแนวทางด้านล่าง",
 "guidelines": [
   "**ACG Clinical Guideline: Diagnosis, treatment, and prevention of acute diarrheal infections in adults (2016)** — นิยาม ความรุนแรง loperamide azithromycin ไม่ให้ยาใน STEC",
   "**Meisenheimer ES et al. Am Fam Physician 2022;106:72–80** — algorithm red flags",
   "**IDSA/SHEA 2021 focused update: C. difficile infection** — fidaxomicin หรือ oral vancomycin",
   "**WHO / GTFCC — Cholera** — สารน้ำ + doxycycline 300 มก. ครั้งเดียว",
   "**CDC Yellow Book — Travelers' diarrhea** — mild/moderate/severe และขนาดยา",
   "**WHO reduced-osmolarity ORS (2002)** — 245 mOsm/L",
   "**Rome IV (2016)** และ **แนวทางเวชปฏิบัติโรคลำไส้แปรปรวนไทย 2022**"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ภาพเคลื่อนไหว + หลักจำ (anims_gi_diarrhea.py) — ใส่ marker ท้ายหัวข้อที่ระบุ
secs = {s_["id"]: s_ for s_ in S}
for it in AN.ITEMS:
    s_ = secs[it["sec"]]
    a = it["anim"]
    s_.setdefault("anims", {})[a["key"]] = {k: a[k] for k in ("title", "svg", "steps")}
    s_["md"], ok = _insert_marker(s_["md"], it.get("after", ""), "[[anim:%s]]" % a["key"])
    assert ok, ("ไม่พบหัวข้อ", it["sec"], it.get("after"))
for m in AN.MNEM:
    secs[m["sec"]].setdefault("mnem", []).append({x: m[x] for x in ("name", "what", "lines", "note", "src") if m.get(x)})

# กระจายตำแหน่งคำตอบ (เขียนคำตอบถูกไว้ที่ choices[0] ทุกข้อ)
_slot = 0
for s_ in S:
    for it in s_["items"]:
        assert it["answer"] == 0
        tgt = [2, 0, 3, 1, 4][_slot % 5]; _slot += 1
        ch = it["choices"]; ch[0], ch[tgt] = ch[tgt], ch[0]; it["answer"] = tgt

path = os.path.join(BUILD, "data", SET + ".json")
data = json.load(open(path, encoding="utf-8"))
old = [l for l in data if l.get("lec") == LEC]
if old:  # คงภาพนิ่งที่ apply_figs ใส่ไว้แล้วไม่ต้องทำใหม่ — apply_figs รันซ้ำได้อยู่แล้ว
    pass
data = [l for l in data if l.get("lec") != LEC]
# วางต่อจากคาบ 27/10 Approach to abdominal pain
pos = next((i + 1 for i, l in enumerate(data) if l.get("lec") == "27/10"), len(data))
data.insert(pos, LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

added = link_mock(SET, LEC, {"gi-dia-08": ["MOCK-010", "MOCK-159"], "gi-dia-11": ["MOCK-163"]})

d = json.load(open(path, encoding="utf-8"))
L = [l for l in d if l["lec"] == LEC][0]
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = {c for s_ in L["sections"] for c in s_["nl"]} | {c for s_ in L["sections"] for i in s_["items"] for c in i.get("nl", [])} | {c for m in L["meq"] + L["osce"] for c in m["nl"]}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
ids = [i["id"] for l in d for s_ in l["sections"] for i in s_["items"]]
dup = {x for x in ids if ids.count(x) > 1}
assert not dup, dup
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
INTRO_ADD = (" · **Diarrhea — acute และ chronic (พญ.ธันยพร · Bedside 27 ต.ค.)** นิยามและโรคเลียนแบบ กลไกของเชื้อ "
             "approach ท้องเสียเฉียบพลัน ORS ยาปฏิชีวนะ ท้องเสียเรื้อรังแบบ fatty/watery/bloody stool osmotic gap และ IBS")
for m in idx:
    if m["set"] == SET:
        m["lectureCount"] = len(d)
        if "Diarrhea — acute" not in m["intro"]:
            m["intro"] = (m["intro"].replace("มี 3 คาบ", "มี 4 คาบ")
                          .replace(" จบแต่ละหัวข้อมีข้อสอบ", INTRO_ADD + " จบแต่ละหัวข้อมีข้อสอบ", 1))
        if "**Diarrhea**" not in m["howto"]:
            m["howto"] = m["howto"].replace("(สเปกตรัมนิ่วถุงน้ำดีและตับอ่อนอักเสบ)",
                "(สเปกตรัมนิ่วถุงน้ำดีและตับอ่อนอักเสบ) · **Diarrhea** ต่อจาก Abdominal pain (IBS ซ้ำกันสองคาบ — คาบนี้เน้นเกณฑ์และการรักษาตามแนวทางไทย 2022)", 1)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | ข้อใหม่ %d + mock %d | meq %d | osce %d | anims %d | mnem %d | nl %d" % (
    len(S), sum(len(s_["items"]) for s_ in S), added, len(MEQ), len(OSCE), len(AN.ITEMS), len(AN.MNEM), len(codes)))
