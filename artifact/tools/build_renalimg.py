#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Essential Renal Imaging (อ.ธนิศร หาญศิริกาญจน์ · Tanisorn Harnsirikarn, MD · nephrologist รพ.ราชวิถี) → data/nephro.json
ต้นฉบับ: Drive 1NHjoGyLcAer6GbmfEp9FEXBw4F_8xmAN "Lec19 Essential Renal Imaging (handout version).pdf"
โน้ตสไลด์: slides/renalimg_notes.md — ข้อความในสไลด์อ่านได้ครบ แต่ภาพรังสี/อัลตราซาวนด์/CT ทุกภาพมองไม่เห็น
และ handout ไม่มีหน้าเนื้อหาของ MRI กับ Nuclear imaging (มีแค่ใน outline) → ส่วนนั้นอิงตำรา/แนวทางและระบุไว้ในบทเรียน
lec = "Imaging" (ไม่ตรงเลขคาบในคลัง — คาบ 19 ในคลังคือ CKD) · date ว่าง
ผูกข้อคลัง: คาบ 28 (อ.ธนิศร urinalysis/abdominal pain) เฉพาะข้อภาพรังสี/นิ่ว/ปัสสาวะเป็นเลือด 8 ข้อ + Mock 4 ข้อ
ภาพประกอบ: SVG วาดเอง — ภาพที่เป็น "ฟิล์ม" (X-ray/CT/US) ใช้สีเทาคงที่ทั้งสองโหมด เพราะความทึบ = ความหมาย"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from svg import *
from svg import _n
from link_bank import link
from link_mock import link_mock

LEC = "Imaging"
NLN = ["B9.1.1(1)"]
SRC = "สไลด์ อ.ธนิศร — Essential Renal Imaging (handout)"
SRC_ADD = "สไลด์ อ.ธนิศร + ตำรา/แนวทาง (เนื้อหาส่วนใหญ่ไม่อยู่ในสไลด์)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None, figs=None, src=SRC):
    d = {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": src,
         "nl": nl or NLN, "md": md, "pearls": pearls, "items": items}
    if figs: d["figs"] = figs
    S.append(d)
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "NEPH-IMG-MCQ-%02d" % n
REF = lambda p: ["สไลด์ อ.ธนิศร — " + p]

# ── ตัวช่วยวาด "ฟิล์ม" (สีเทาคงที่ — ภาพรังสีขาว/ดำตามความทึบ ไม่สลับตามโหมด)
AIR, FAT, SOFT, BONE, METAL = "#050505", "#2f2f2f", "#6e6e6e", "#d2d2d2", "#ffffff"
FT, FT2 = "#f2f2f2", "#bdbdbd"          # ตัวอักษรบนฟิล์ม
def _st(fill=None, stroke=None, sw=None, dash=None, op=None):
    s = ["fill:%s" % (fill or "none"), "stroke:%s" % (stroke or "none")]
    if sw: s.append("stroke-width:%s" % sw)
    if dash: s.append("stroke-dasharray:%s" % dash)
    if op is not None: s.append("opacity:%s" % op)
    return ' style="%s"' % ";".join(s)
def FR(x, y, w, h, fill, r=0, stroke=None, sw=None):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s"%s/>' % (_n(x), _n(y), _n(w), _n(h), _n(r), _st(fill, stroke, sw))
def FE(cx, cy, rx, ry, fill, rot=None, stroke=None, sw=None):
    tr = (' transform="rotate(%s %s %s)"' % (_n(rot), _n(cx), _n(cy))) if rot else ""
    return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s"%s%s/>' % (_n(cx), _n(cy), _n(rx), _n(ry), tr, _st(fill, stroke, sw))
def FC(cx, cy, r, fill, stroke=None, sw=None):
    return '<circle cx="%s" cy="%s" r="%s"%s/>' % (_n(cx), _n(cy), _n(r), _st(fill, stroke, sw))
def FP(d, fill=None, stroke=None, sw=None, dash=None):
    return '<path d="%s"%s/>' % (d, _st(fill, stroke, sw, dash))
def FL(x1, y1, x2, y2, stroke, sw=1.3, dash=None):
    return '<line x1="%s" y1="%s" x2="%s" y2="%s"%s/>' % (_n(x1), _n(y1), _n(x2), _n(y2), _st(None, stroke, sw, dash))
def TF(x, y, s, c="sm", col=FT):
    return t(x, y, s, c).replace("<text ", '<text style="fill:%s" ' % col, 1)
def bean(cx, cy, rx, ry, fill, rot=0, side=1, stroke=None, sw=None, cls=None):
    """ไตรูปถั่ว — side=+1 ขั้วไต (hilum) หันไปทางขวาของภาพ · -1 หันซ้าย"""
    k = side
    v = (cx, cy - ry, cx - k * rx * 1.3, cy - ry, cx - k * rx * 1.3, cy + ry, cx, cy + ry,
         cx + k * rx * 0.9, cy + ry, cx + k * rx * 1.05, cy + ry * 0.5, cx + k * rx * 0.6, cy + ry * 0.2,
         cx + k * rx * 0.25, cy, cx + k * rx * 0.6, cy - ry * 0.2,
         cx + k * rx * 1.05, cy - ry * 0.5, cx + k * rx * 0.9, cy - ry, cx, cy - ry)
    d = "M%s %s C%s %s %s %s %s %s C%s %s %s %s %s %s Q%s %s %s %s C%s %s %s %s %s %s Z" % tuple(_n(a) for a in v)
    tr = (' transform="rotate(%s %s %s)"' % (_n(rot), _n(cx), _n(cy))) if rot else ""
    return '<path d="%s"%s%s/>' % (d, tr, (' class="%s"' % cls) if cls else _st(fill, stroke, sw))
def film(x, y, w, h, fill="#161616", r=6):
    return rect(x, y, w, h, "lru", r, ' style="fill:%s"' % fill)


# ═════════════════════════════════════════════ 1
F1 = {"modality": fig("แต่ละเครื่องมือ “มองเห็น” คุณสมบัติคนละอย่าง",
  "**X-ray/CT** วัดว่ารังสีถูก **ดูดกลืน** มากแค่ไหน (แคลเซียมและโลหะดูดกลืนมาก → ขาว) · **Ultrasound** วัด **เสียงสะท้อน** ที่รอยต่อของเนื้อเยื่อ (รอยต่อมาก → สว่าง · น้ำใสไม่มีรอยต่อ → ดำ) · **MRI** วัดสัญญาณจาก **โปรตอนของน้ำและไขมัน** (ไม่มีรังสี) · **Nuclear** วัดรังสีที่ **ยาในตัวผู้ป่วยปล่อยออกมา** หลังถูกไตกรอง หลั่ง หรือจับไว้ จึงบอก **การทำงาน** ไม่ใช่รูปร่าง — เลือกเครื่องมือให้ตรงกับคำถามที่อยากรู้",
  svg(420, 404, "เปรียบเทียบหลักการของ X-ray CT ultrasound MRI และ nuclear imaging",
    # แถว X-ray
    rect(4, 6, 412, 92, "sk", 10), t(12, 36, "X-ray · CT", "sm b"), t(12, 52, "KUB · IVP · CT", "xs mu"),
    ell(196, 52, 34, 30, "bx"), rect(104, 32, 22, 40, "ms", 4), t(115, 56, "X", "xs b mid tms"),
    line(126, 40, 248, 40, "lms", "ah-ms"), line(126, 64, 248, 64, "lms", "ah-ms"), line(126, 52, 188, 52, "lms"),
    circ(196, 52, 7, "inkf"), FR(250, 20, 10, 64, "#262626", 0, "#8a8a8a", 1), FR(250, 46, 10, 12, "#f5f5f5"),
    t(272, 28, "วัดการดูดกลืนรังสี", "sm b"), t(272, 46, "Ca/โลหะ ดูดกลืน: ขาว", "xs"),
    t(272, 62, "ลม/ไขมัน ทะลุผ่าน: ดำ", "xs"), t(272, 78, "CT = หมุนรอบตัว วัดเป็น HU", "xs mu"),
    # แถว US
    rect(4, 106, 412, 92, "sk", 10), t(12, 136, "Ultrasound", "sm b"), t(12, 152, "คลื่นเสียงสะท้อน", "xs mu"),
    ell(196, 162, 40, 28, "bx"), rect(180, 112, 32, 14, "ac", 3),
    line(190, 128, 190, 160, "lwa w2", "ah-wa"), path("M176 168 Q196 158 216 168", "ln w3"),
    line(203, 160, 203, 130, "lms w2", "ah-ms"),
    t(272, 128, "วัดเสียงสะท้อนที่รอยต่อ", "sm b"), t(272, 146, "รอยต่อสะท้อนมาก: สว่าง", "xs"),
    t(272, 162, "น้ำใส ไม่มีรอยต่อ: ดำ", "xs"), t(272, 178, "ไม่มีรังสี ไม่ต้องฉีดสี", "xs mu"),
    # แถว MRI
    rect(4, 206, 412, 92, "sk", 10), t(12, 236, "MRI", "sm b"), t(12, 252, "สนามแม่เหล็ก + RF", "xs mu"),
    rect(150, 214, 92, 9, "muf", 3), rect(150, 281, 92, 9, "muf", 3), t(246, 223, "B₀", "xs mu"),
    ell(196, 252, 40, 22, "bx"),
    line(172, 262, 172, 244, "ln", "ah"), line(184, 262, 184, 244, "ln", "ah"), line(196, 262, 196, 244, "ln", "ah"),
    line(208, 262, 208, 244, "ln", "ah"), line(220, 262, 220, 244, "ln", "ah"),
    t(272, 228, "สัญญาณจากโปรตอน (H)", "sm b"), t(272, 246, "ของน้ำและไขมัน", "xs"),
    t(272, 262, "T2: น้ำสว่าง เห็นท่อที่ขยาย", "xs"), t(272, 278, "ไม่มีรังสี · gadolinium", "xs mu"),
    # แถว Nuclear
    rect(4, 306, 412, 92, "sk", 10), t(12, 336, "Nuclear", "sm b"), t(12, 352, "DTPA · MAG3 · DMSA", "xs mu"),
    rect(158, 312, 76, 14, "bx", 3), t(196, 323, "gamma camera", "xs mid mu"),
    ell(196, 364, 40, 26, "bx"), bean(184, 366, 8, 15, None, 0, 1, cls="ac"), bean(208, 366, 8, 15, None, 0, -1, cls="ac"),
    circ(183, 362, 2, "acf"), circ(186, 371, 2, "acf"), circ(207, 360, 2, "acf"), circ(210, 370, 2, "acf"),
    line(183, 351, 179, 330, "lac", "ah-ac"), line(209, 351, 213, 330, "lac", "ah-ac"),
    t(272, 328, "วัดรังสีจากยาในตัว", "sm b"), t(272, 346, "ไตกรอง/หลั่ง/จับยาติดรังสี", "xs"),
    t(272, 362, "= การทำงาน ไม่ใช่รูปร่าง", "xs"), t(272, 378, "GFR · การระบาย · แผลเป็น", "xs mu")))}

sec("neph-img-01", "มุมมองนักไต — เครื่องมือแต่ละชนิดเห็นอะไร",
    "X-ray/IVP · ultrasound · CT/MRI · nuclear — ฟิสิกส์คนละแบบ ตอบคำถามคนละข้อ · ACR Appropriateness Criteria", 8,
"""### โครงของคาบ (สไลด์)
อ.ธนิศร สอน imaging จาก **มุมมองของนักไต (Nephrologist's Perspective)** — ไม่ได้ต้องอ่านภาพแทนรังสีแพทย์ แต่ต้อง **เลือกการตรวจให้ตรงคำถาม** และ **รู้ว่าผลแต่ละแบบหมายถึงอะไร**
1. **X-ray / IVP** · 2. **Ultrasound** · 3. **CT / MRI** · 4. **Nuclear imaging**
5. **How to C-H-O-O-S-E the test?** — สไลด์ใช้ตาราง **ACR Appropriateness Criteria** ของแต่ละเครื่องมือ
6. **Clinical S-E-L-E-C-T-E-D conditions** — 4 เคส: ปวดสีข้างเฉียบพลัน · กรวยไตอักเสบที่ไข้ไม่ลง · ไตวายที่ต้องแยก AKI กับ CKD · กล้ามเนื้ออ่อนแรงจาก K ต่ำ + nephrocalcinosis

> ไฟล์ที่ได้เป็น **handout** — ภาพรังสีในสไลด์มองไม่เห็น และ **ไม่มีหน้าเนื้อหาของ MRI กับ nuclear imaging** บทเรียนนี้จึงวาดภาพประกอบใหม่ทั้งหมด และเติมส่วนที่ขาดจากตำรา/แนวทาง (บอกไว้ในแต่ละหัวข้อ)

### หลักฟิสิกส์ที่ต้องรู้ — ภาพขาว/ดำมาจากอะไร
[[fig:modality]]
| เครื่องมือ | สัญญาณมาจาก | ขาว/สว่างเมื่อ | จุดแข็งในงานไต | ข้อจำกัด |
|---|---|---|---|---|
| **Plain KUB** | X-ray ทะลุตัว ถูกดูดกลืนตามความหนาแน่นและเลขอะตอม | ดูดกลืนมาก — Ca, โลหะ | นิ่วทึบรังสี · ก๊าซผิดที่ · เงาไต psoas | ภาพ 2 มิติซ้อนกัน · นิ่วโปร่งรังสีไม่เห็น · ไวต่อนิ่วแค่ **29%** |
| **IVP / IVU** | X-ray + iodinated contrast ที่ไตกรองแล้วขับออก | ที่ที่มี contrast | เห็นทางเดินปัสสาวะทั้งสาย · ระดับการอุดกั้น | ต้องฉีดสี · หลายฟิล์ม · ACR ไม่แนะนำแล้ว |
| **CT** | X-ray หมุนรอบตัว คำนวณ attenuation เป็น **HU** | HU สูง | นิ่ว (**97%**) · ภาวะแทรกซ้อน · ก้อน หนอง ก๊าซ | รังสีมากกว่า · ฉีดสีเสี่ยงต่อไตบางราย |
| **Ultrasound** | เสียงสะท้อนที่รอยต่อของเนื้อเยื่อ (acoustic impedance ต่างกัน) | รอยต่อมาก — ไขมันใน sinus นิ่ว พังผืด | ไม่มีรังสี ไม่ฉีดสี ทำข้างเตียง · ขนาดไต ความหนาเนื้อไต ไตบวมน้ำ | ขึ้นกับผู้ตรวจ · ท่อไตช่วงกลางมองยาก · ลมในลำไส้บัง |
| **MRI** | โปรตอนของน้ำ/ไขมันในสนามแม่เหล็ก | T2: น้ำสว่าง | ไม่มีรังสี · แยกเนื้อเยื่อดี · ตั้งครรภ์ (ไม่ฉีด gadolinium) | แพง นาน · เห็นนิ่วไม่ดี · gadolinium กับ NSF |
| **Nuclear** | รังสี gamma จากยาที่ไตกรอง/หลั่ง/จับ | ที่ที่ยาไปสะสม | **การทำงานแยกข้าง** · การระบาย (obstruction) · แผลเป็น | ภาพหยาบ ไม่เห็นกายวิภาคละเอียด |

### ACR Appropriateness Criteria — ภาษากลางของการ "เลือก"
**American College of Radiology (ACR)** ให้คะแนนการตรวจแต่ละแบบต่อสถานการณ์ทางคลินิก 1–9 แล้วจัดเป็นสามกลุ่ม
| คะแนน | ความหมาย |
|---|---|
| **7–9** | **Usually appropriate** — ควรทำ |
| **4–6** | **May be appropriate** — ทำได้ในบางสถานการณ์ / เป็นทางเลือก |
| **1–3** | **Usually not appropriate** — ไม่ควรทำ |
ทุก modality ในสไลด์จบด้วยตาราง ACR สี่สถานการณ์เดียวกัน (สงสัยนิ่ว · microscopic hematuria · AKI/CKD · acute pyelonephritis) — รวมไว้เป็นตารางเดียวในหัวข้อ **How to CHOOSE**

### ปริมาณรังสีโดยประมาณ (ไม่อยู่ในสไลด์ — EAU Urolithiasis guideline)
| การตรวจ | mSv โดยประมาณ |
|---|---|
| Plain KUB | 0.5–1 |
| IVU | 1.3–3.5 |
| Non-contrast CT ปกติ | 4.5–5 |
| **Low-dose CT** | **0.97–1.9** |
| Enhanced CT (หลายเฟส) | 25–35 |
เหตุผลที่แนวทางนิ่วแนะนำ **low-dose non-contrast CT** — ได้ความไวใกล้เคียงกันแต่รังสีใกล้ IVU
""",
    ["X-ray/CT = การดูดกลืนรังสี · US = เสียงสะท้อนที่รอยต่อ · MRI = โปรตอน · Nuclear = การทำงาน",
     "ACR: 7–9 usually appropriate · 4–6 may be · 1–3 usually not",
     "ไม่มีการตรวจไหนดีที่สุดเสมอ — เริ่มจากคำถามทางคลินิก แล้วชั่งรังสี สารทึบรังสี และการตั้งครรภ์",
     "ต้องการรู้ 'การทำงานแยกข้าง' หรือ 'อุดกั้นจริงไหม' → nuclear renogram ไม่ใช่ภาพกายวิภาค"],
    [mcq(N(1), "Which renal imaging study primarily provides functional rather than anatomical information, such as split renal function and drainage?",
         ["Plain KUB radiograph", "Grey-scale renal ultrasound", "Non-contrast CT KUB", "Tc-99m MAG3 renal scintigraphy", "Retrograde pyelography"], 3,
         "**Renal scintigraphy** (MAG3, DTPA, DMSA) วัดรังสีที่ยาในตัวผู้ป่วยปล่อยออกมาหลังถูกไต **กรอง หลั่ง หรือจับ** จึงบอก **การทำงานแยกข้าง (split function)** และ **การระบาย** ได้ — แต่ภาพหยาบ เห็นกายวิภาคไม่ละเอียด\n\n- **Plain KUB** — เห็นแค่ความทึบ (นิ่วทึบรังสี เงาไต) ไม่บอกการทำงาน\n- **Ultrasound** — ขนาด ความหนาเนื้อไต echogenicity และ hydronephrosis เป็นข้อมูลกายวิภาค\n- **Non-contrast CT** — ดีที่สุดสำหรับนิ่ว แต่ไม่วัดการทำงาน\n- **Retrograde pyelography** — ฉีดสีย้อนขึ้นทางท่อไต เห็นรูปร่างทางเดินปัสสาวะโดย **ไม่ขึ้นกับการทำงานของไต**",
         "อยากรู้การทำงานแยกข้าง → nuclear", "Imaging modality — function vs anatomy", ["ตำราเวชศาสตร์นิวเคลียร์ (outline สไลด์: Nuclear imaging)"], ["B9.1.1(1)", "B9.3(4)"]),
     mcq(N(2), "In the ACR Appropriateness Criteria, an imaging procedure rated 7–9 for a clinical scenario is classified as:",
         ["Usually not appropriate", "May be appropriate", "Usually appropriate", "Experimental", "Contraindicated"], 2,
         "ACR ให้คะแนน 1–9: **7–9 = usually appropriate** · 4–6 = may be appropriate · 1–3 = usually not appropriate\n\nไม่มีหมวด \"experimental\" หรือ \"contraindicated\" ในระบบนี้ — ข้อห้ามเฉพาะราย (เช่นแพ้สารทึบรังสี ตั้งครรภ์) ต้องพิจารณาแยก ตาราง ACR บอกเพียงความเหมาะสมโดยรวมของการตรวจต่อคำถามทางคลินิกนั้น",
         "ACR 7–9 usually · 4–6 may be · 1–3 usually not", "ACR Appropriateness Criteria", REF("ACR tables (ทุก modality)"), ["B9.1.1(1)"]),
    ], nl=["B9.1.1(1)", "3.2.3", "3.3.20", "B9.3(4)"], figs=F1, src=SRC_ADD)

# ═════════════════════════════════════════════ 2
def _density():
    out = [path("M26 28 L394 28", "lmu w2", m="ah-mu", ms="ah-mu"),
           t(20, 16, "โปร่งรังสี (radiolucent) → ดำ", "xs mu"), t(400, 16, "ทึบรังสี (radiopaque) → ขาว", "xs mu end")]
    cols = [(AIR, "Air", "ลม", "ลมในลำไส้", "ก๊าซใน EPN"), (FAT, "Fat", "ไขมัน", "ไขมันรอบไต", "ไขมันรอบ psoas"),
            (SOFT, "Soft tissue", "เนื้อเยื่อ / น้ำ", "ไต กล้ามเนื้อ", "ปัสสาวะ เลือด"),
            (BONE, "Bone / Ca", "กระดูก หินปูน", "นิ่ว Ca", "phlebolith"), (METAL, "Metal", "โลหะ", "คลิป ลวด", "สาย DJ stent")]
    for i, (c, en, th, e1, e2) in enumerate(cols):
        x = 15 + i * 80
        out += [FR(x, 38, 70, 84, c, 4, "#8a8a8a", 1), t(x + 35, 140, en, "sm b mid"), t(x + 35, 157, th, "xs mid"),
                t(x + 35, 174, e1, "xs mid mu"), t(x + 35, 191, e2, "xs mid mu")]
    out += [t(15, 222, "ขอบของอวัยวะเห็นได้เพราะ “ความต่าง” ของความทึบ", "sm b"),
            film(15, 232, 190, 80, FAT), bean(110, 272, 22, 30, SOFT, 0, 1), TF(104, 276, "ไต", "xs b mid"),
            film(215, 232, 190, 80, "#646464"), bean(310, 272, 22, 30, "#6b6b6b", 0, 1), TF(304, 276, "ไต ?", "xs b mid", "#202020"),
            t(110, 330, "ไขมันล้อมรอบ: เห็นขอบชัด", "xs mid"), t(310, 330, "เลือด/หนองแทนที่ไขมัน: ขอบหาย", "xs mid tbad")]
    return svg(420, 340, "ความทึบ 5 ระดับบนภาพรังสี และหลักการเห็นขอบอวัยวะ", *out)

def _kub():
    o = [film(8, 8, 364, 410, "#272727")]
    o.append(FE(92, 64, 80, 54, "#383838"))                       # ตับ
    for i, lab in enumerate(["T11", "T12", "L1", "L2", "L3", "L4", "L5"]):
        y = 28 + i * 38
        o.append(FR(168, y, 44, 30, BONE, 5))
        if i >= 2: o += [FR(150, y + 12, 18, 6, "#a8a8a8", 2), FR(212, y + 12, 18, 6, "#a8a8a8", 2)]
        o.append(TF(190, y + 19, lab, "xs b mid", "#202020"))
    o += [FP("M168 296 L212 296 L204 350 L176 350 Z", BONE),
          FP("M170 300 C120 270 70 272 58 302 C50 332 80 360 110 375 C125 395 160 405 186 405", None, "#c4c4c4", 4),
          FP("M210 300 C260 270 310 272 322 302 C330 332 300 360 270 375 C255 395 220 405 194 405", None, "#c4c4c4", 4),
          FL(172, 108, 128, 330, "#8f8f8f", 2), FL(208, 108, 252, 330, "#8f8f8f", 2),         # psoas
          bean(122, 160, 22, 52, SOFT, 11, 1), bean(258, 121, 22, 52, SOFT, -11, -1),                       # ไต
          FE(190, 372, 46, 26, "#5c5c5c"),
          FP("M142 170 C152 200 160 230 158 262 C156 290 156 310 160 330 C164 350 170 360 178 368", None, "#9ecbff", 1.8, "4 3"),
          FP("M238 132 C228 172 222 220 222 262 C224 290 224 310 220 330 C216 350 210 360 202 368", None, "#9ecbff", 1.8, "4 3"),
          FC(238, 352, 5.5, BONE), FC(238, 352, 2.2, "#272727"), TF(248, 356, "phlebolith", "xs", FT2)]
    for n, (x, y) in enumerate([(146, 182), (157, 300), (176, 366)], 1):
        o += [FC(x, y, 8.5, "#e8bb63", "#1b1b1b", 1.5), TF(x, y + 4, str(n), "xs b mid", "#1b1b1b")]
    o += [TF(20, 30, "R", "lg b"), TF(52, 48, "ตับ", "xs", FT2), TF(24, 150, "ไตขวา", "sm b"), TF(24, 165, "L1–L3", "xs", FT2),
          TF(296, 104, "ไตซ้าย", "sm b"), TF(296, 119, "T12–L2", "xs", FT2), TF(246, 236, "psoas", "xs", FT2),
          TF(190, 393, "กระเพาะปัสสาวะ", "xs mid")]
    o += [t(10, 438, "จุดแคบของท่อไต 3 ตำแหน่ง — นิ่วชอบติด", "sm b"),
          FC(18, 455, 7, "#e8bb63", "#1b1b1b", 1), TF(18, 459, "1", "xs b mid", "#1b1b1b"), t(30, 459, "PUJ", "xs"),
          FC(72, 455, 7, "#e8bb63", "#1b1b1b", 1), TF(72, 459, "2", "xs b mid", "#1b1b1b"), t(84, 459, "ข้าม iliac vessels (pelvic brim)", "xs"),
          FC(262, 455, 7, "#e8bb63", "#1b1b1b", 1), TF(262, 459, "3", "xs b mid", "#1b1b1b"), t(274, 459, "VUJ — แคบที่สุด", "xs"),
          t(10, 478, "เส้นประ = แนวท่อไต · ภาพมองจากด้านหน้า: ขวาของผู้ป่วยอยู่ซ้ายภาพ", "xs mu")]
    return svg(380, 486, "ภาพวาด plain KUB ปกติ ตำแหน่งไต psoas กระเพาะปัสสาวะ และจุดแคบของท่อไต", *o)

F2 = {"density": fig("ความทึบ 5 ระดับ — และทำไมเราเห็น “ขอบ” ของไต",
        "แถวบน: เรียงจาก **ลม (ดำที่สุด) → ไขมัน → เนื้อเยื่อ/น้ำ → กระดูก/หินปูน → โลหะ (ขาวที่สุด)** ตามสไลด์ · แถวล่าง: ไตเป็น soft tissue เราเห็นขอบไตได้เพราะมี **ไขมันรอบไต (perirenal fat)** ซึ่งดำกว่าล้อมอยู่ ถ้ามี **เลือด หนอง หรือน้ำ** (ความทึบเท่า soft tissue) มาแทนที่ไขมัน ขอบจะ **หายไป** — หลักเดียวกับ **loss of psoas shadow** ใน perinephric abscess หรือ retroperitoneal hematoma",
        _density()),
      "kub": fig("Plain KUB ปกติ (ภาพวาด) — ไต psoas กระเพาะปัสสาวะ และจุดแคบ 3 ตำแหน่ง",
        "ไตขวาอยู่ **L1–L3** ต่ำกว่าไตซ้าย (**T12–L2**) เพราะตับกดอยู่ด้านบน · **แนวแกนยาวของไตขนานกับขอบ psoas** (ขั้วบนเอียงเข้าหาแนวกลาง) · ท่อไตวิ่งลงตามปลาย transverse process ข้าม **iliac vessels ที่ pelvic brim** แล้วเข้ากระเพาะปัสสาวะ · นิ่วติดที่ **(1) PUJ (2) จุดข้าม iliac vessels (3) VUJ** ซึ่งแคบที่สุด · เงากลมเล็กในอุ้งเชิงกรานที่มี **จุดโปร่งตรงกลาง** และอยู่ต่ำ/ด้านข้างแนวท่อไตมักเป็น **phlebolith** (หินปูนในหลอดเลือดดำ) ไม่ใช่นิ่ว (ตำแหน่ง/ความยาวไตจากสไลด์ IVP: Krairittichai 2011)",
        _kub())}

sec("neph-img-02", "Plain KUB — ความทึบ 5 ระดับ และการอ่านเงาไต psoas นิ่ว",
    "ทำไมของแต่ละอย่างขาว/ดำไม่เท่ากัน · เห็นขอบไตได้เพราะไขมัน · อ่าน KUB เป็นระบบ · ACR", 9,
"""### ความทึบ 5 ระดับ (5 DENSITIES — สไลด์)
**Metallic → Bone/Calcification → Soft tissue → Fat → Air** เรียงจาก **radiopaque (ขาว)** ไป **radiolucent (ดำ)**
[[fig:density]]
#### ทำไมภาพถึงออกมาแบบนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **แคลเซียม โลหะ ไอโอดีน = ขาว** | การดูดกลืนรังสีแปรตาม **ความหนาแน่น** และ **เลขอะตอม (Z) ยกกำลังสาม** (photoelectric effect) — Ca (Z 20) ไอโอดีน (Z 53) โลหะ ดูดกลืนมาก รังสีไปไม่ถึงฟิล์ม → ฟิล์มไม่ถูกเปิด = ขาว | นิ่วที่มีแคลเซียมเห็นบน KUB · นิ่ว **uric acid** (มีแค่ C H N O) **ไม่เห็น** |
| **ลม = ดำ** | ลมแทบไม่มีอะไรดูดกลืนรังสี → รังสีทะลุถึงฟิล์มเต็มที่ | **ก๊าซในเนื้อไต/รอบไต** = emphysematous pyelonephritis |
| **เห็นขอบไตและ psoas** | ไต/psoas (soft tissue) ถูกล้อมด้วย **ไขมัน** ซึ่งดำกว่า ความต่างของความทึบสร้างขอบ | **ขอบไตหรือ psoas หาย** = มีของเหลว (หนอง เลือด) แทนที่ไขมันใน retroperitoneum — perinephric abscess, hematoma (คนผอมไขมันน้อยก็หายได้) |
| **อวัยวะซ้อนกัน** | ภาพ 2 มิติ ทุกอย่างในแนวรังสีซ้อนทับ | หินปูนนอกทางเดินปัสสาวะ (phlebolith, หลอดเลือด, ต่อมน้ำเหลือง, นิ่วถุงน้ำดี) ปนกับนิ่วได้ → สไลด์: **difficult to differentiate on single 2-D view** |

### อ่าน KUB อย่างเป็นระบบ
[[fig:kub]]
1. **ชนิดและคุณภาพ** — KUB ท่า supine AP ต้องคลุมตั้งแต่ **ขอบบนของไต (T11–T12) ถึง symphysis pubis**
2. **Bone** — กระดูกสันหลัง เชิงกราน ซี่โครงล่าง (lytic/sclerotic lesion)
3. **Soft tissue** — เงาไตสองข้าง (ขนาด ตำแหน่ง แนวแกน) · **psoas shadow** · ตับ ม้าม · กระเพาะปัสสาวะ
4. **Gas** — ลมในลำไส้ปกติหรือไม่ · **ก๊าซในบริเวณไต** (EPN)
5. **Calcification** — ไล่ตามแนว **ไต → ท่อไต (ปลาย transverse process → pelvic brim) → กระเพาะปัสสาวะ** โดยเน้น **จุดแคบ 3 ตำแหน่ง**

**ไตปกติบนฟิล์ม (สไลด์ IVP · Krairittichai 2011)** — ขวา **L1–L3** · ซ้าย **T12–L2** · ยาว **9.3–10.7 ซม. (คนไทย)** / 9–12 ซม. (ต่างประเทศ) · **แกนขนานกับ psoas**

**แยกนิ่วจากหินปูนอื่น** (ตำรามาตรฐาน)
| เงาทึบ | ลักษณะที่ช่วยแยก |
|---|---|
| **Phlebolith** | กลม ขอบเรียบ **ตรงกลางโปร่ง** อยู่ด้านข้างอุ้งเชิงกรานใต้แนว ischial spine — บน CT มี "comet-tail sign" |
| **นิ่วท่อไต** | อยู่ในแนวท่อไต รูปรีหรือเหลี่ยม · บน CT มี **soft tissue rim sign** (ผนังท่อไตบวมรอบนิ่ว) |
| หลอดเลือด/ต่อมน้ำเหลือง/นิ่วถุงน้ำดี | เป็นเส้นตามแนวหลอดเลือด · กลุ่มก้อนไม่เป็นระเบียบ · อยู่ใต้ตับ |

### ACR — plain radiograph (สไลด์)
| ข้อบ่งชี้ | ความเหมาะสม |
|---|---|
| สงสัยนิ่ว (ปวดสีข้าง) | **May be appropriate (CT preferred)** |
| Microscopic hematuria | Usually not appropriate |
| AKI/CKD | Usually not appropriate |
| Acute pyelonephritis | Usually not appropriate |
KUB ยังมีที่ใช้ — **ติดตามนิ่วทึบรังสีที่รู้จักแล้ว** (เช่นหลังขับนิ่ว) เพราะรังสีน้อยกว่า CT มาก
""",
    ["ความทึบ: metal > bone/Ca > soft tissue > fat > air",
     "เห็นขอบไต/psoas เพราะไขมันล้อม · ขอบหาย = หนอง/เลือดใน retroperitoneum",
     "ไตขวา L1–L3 · ไตซ้าย T12–L2 · ยาว 9.3–10.7 ซม. (ไทย) · แกนขนาน psoas",
     "จุดแคบท่อไต: PUJ · pelvic brim (iliac vessels) · VUJ (แคบสุด)",
     "Phlebolith: กลม เรียบ ตรงกลางโปร่ง อยู่ด้านข้างอุ้งเชิงกราน"],
    [mcq(N(3), "A plain abdominal radiograph of a febrile diabetic patient shows that the right psoas shadow, clearly visible on an old film, can no longer be seen. What is the best explanation?",
         ["A radiolucent uric acid stone in the right ureter", "Overlying bowel gas, which always hides the psoas", "Fluid such as pus or blood replacing retroperitoneal fat and removing the fat–muscle interface", "Normal finding because the liver lies on the right", "Excreted iodinated contrast in the right ureter"], 2,
         "ขอบ psoas เห็นได้เพราะกล้ามเนื้อ (soft tissue) ถูกล้อมด้วย **ไขมัน retroperitoneum** ซึ่งดำกว่า — ความต่างของความทึบคือสิ่งที่สร้าง \"ขอบ\" เมื่อ **หนอง เลือด หรือน้ำ** ซึ่งมีความทึบเท่า soft tissue มาแทนที่ไขมัน ขอบจึงหายไป (เช่น **perinephric abscess** ในผู้ป่วยเบาหวาน)\n\n- นิ่ว uric acid โปร่งรังสี ไม่ทำให้ขอบ psoas หาย\n- ลมในลำไส้บังได้บางส่วน แต่ไม่ใช่ \"เสมอ\" และฟิล์มเก่าเห็นชัด\n- ตับไม่ได้ทำให้ psoas ขวาหายตามปกติ\n- ไม่มีการฉีดสารทึบรังสีในโจทย์",
         "ขอบหาย = ไขมันถูกแทนที่ด้วยของเหลว", "Psoas shadow", REF("Plain radiograph — densities, psoas shadow"), ["3.2.3", "2.3.14(14)"]),
     mcq(N(4), "On a KUB radiograph, a small round calcification with a smooth margin and a radiolucent centre is seen in the lateral pelvis below the level of the ischial spines. It most likely represents:",
         ["A distal ureteric calculus", "A phlebolith", "A bladder calculus", "A staghorn calculus", "Emphysematous cystitis"], 1,
         "**Phlebolith** คือหินปูนในหลอดเลือดดำของอุ้งเชิงกราน — **กลม ขอบเรียบ ตรงกลางโปร่ง** อยู่ด้านข้างอุ้งเชิงกราน มักต่ำกว่าแนว ischial spine จึงปนกับนิ่วท่อไตส่วนปลายได้บ่อย (สไลด์: แยกยากบนภาพ 2 มิติ)\n\n- **นิ่วท่อไตส่วนปลาย** — อยู่ในแนวท่อไต รูปรี ไม่มีจุดโปร่งกลาง · CT แยกได้ด้วย soft tissue rim sign\n- **นิ่วในกระเพาะปัสสาวะ** — อยู่กลางอุ้งเชิงกราน มักใหญ่ เป็นชั้น\n- **Staghorn** — อยู่ใน renal pelvis/calyces ไม่ใช่ในอุ้งเชิงกราน\n- **Emphysematous cystitis** — เป็นเงาลม (ดำ) ที่ผนังกระเพาะปัสสาวะ ไม่ใช่หินปูน",
         "กลม เรียบ กลางโปร่ง = phlebolith", "KUB calcifications", REF("Plain radiograph of kidney stone — limitations (phleboliths)"), ["3.2.3", "2.3.14-3(15)"]),
    ], nl=["3.2.3", "3.2.2", "B9.1.1(1)", "B9.1.1(2)", "2.3.14-3(15)"], figs=F2)

# ═════════════════════════════════════════════ 3
def _ivp_panel(x, y, ph):
    o = [film(x, y, 128, 84, "#1d1d1d")]
    kid = "#e6e6e6" if ph == 1 else ("#4a4a4a" if ph >= 5 else "#8a8a8a")
    o += [FE(x + 36, y + 32, 12, 21, kid, 10), FE(x + 92, y + 28, 12, 21, kid, -10)]
    bl = {1: ("#383838", 16, 8), 2: ("#3c3c3c", 16, 8), 3: ("#3c3c3c", 16, 8), 4: ("#cfcfcf", 15, 7), 5: (METAL, 24, 12), 6: ("#e8e8e8", 8, 4)}[ph]
    o.append(FE(x + 64, y + 72, bl[1], bl[2], bl[0]))
    if ph in (2, 3, 4):
        sw = 1.4 if ph == 2 else 2.4
        for (cx, cy, s) in ((x + 36, y + 32, 1), (x + 92, y + 28, -1)):
            px, py = cx + 5 * s, cy + 4
            o += [FL(px, py, cx - 3 * s, cy - 13, METAL, sw), FL(px, py, cx - 6 * s, cy + 1, METAL, sw), FL(px, py, cx - 2 * s, cy + 14, METAL, sw)]
            if ph >= 3: o.append(FC(px, py, 3.2, METAL))
            if ph == 2: o.append(FL(px, py, px + 4 * s, py + 14, METAL, 1.2))
            if ph == 4: o.append(FP("M%s %s Q%s %s %s %s" % (_n(px), _n(py), _n(px + 8 * s), _n(py + 22), _n(x + 64 - 10 * s), _n(y + 68)), None, METAL, 1.6))
    if ph == 3: o.append(FR(x + 6, y + 56, 116, 7, "#5a5a5a", 3))
    return o

def _ivp():
    lab = [("1 นาที", "nephrographic", "เนื้อไต ขนาด ขอบ"), ("5 นาที", "early excretion", "PCS + ท่อไตส่วนบน"),
           ("10 นาที (กดท้อง)", "pyelographic", "PCS ขยายเต็มที่"), ("15 นาที (ปล่อย)", "KUB film", "ท่อไตทั้งสาย"),
           ("Full bladder", "", "รูปร่างกระเพาะปัสสาวะ"), ("Post-void", "", "ปัสสาวะค้าง (residual)")]
    o = []
    for i in range(6):
        x, y = 8 + (i % 3) * 138, 8 + (i // 3) * 140
        o += _ivp_panel(x, y, i + 1)
        a, b, c = lab[i]
        o += [t(x + 64, y + 100, a, "sm b mid"), t(x + 64, y + 114, b, "xs mid i2") if b else "", t(x + 64, y + 128, c, "xs mid mu")]
    return svg(420, 290, "ลำดับฟิล์ม IVP ตามเวลาหลังฉีดสารทึบรังสี", *o)

def _calyx():
    o = []
    for i, (name, sub) in enumerate([("ปกติ — cupped", "fornix แหลม papilla ยื่นเข้า"), ("Blunted", "fornix มน (ขยายระยะแรก)"), ("Clubbed / ballooned", "นูนออก เนื้อไตบาง")]):
        x = 8 + i * 138; cx, cy = x + 64, 62
        o.append(film(x, 8, 128, 100, "#1d1d1d"))
        if i == 0:
            o += [FR(cx - 22, 14, 44, 26, SOFT), FP("M%s %s C%s %s %s %s %s %s C%s %s %s %s %s %s L%s %s L%s %s L%s %s Z" % tuple(_n(v) for v in (
                cx - 26, cy - 22, cx - 24, cy + 4, cx - 12, cy + 16, cx, cy + 16, cx + 12, cy + 16, cx + 24, cy + 4, cx + 26, cy - 22, cx + 20, cy - 22, cx, cy + 2, cx - 20, cy - 22)), METAL),
                  FP("M%s %s L%s %s L%s %s Z" % (_n(cx - 20), _n(cy - 22), _n(cx + 20), _n(cy - 22), _n(cx), _n(cy + 2)), SOFT),
                  FR(cx - 4, cy + 14, 8, 30, METAL)]
        elif i == 1:
            o += [FR(cx - 26, 14, 52, 26, SOFT), FP("M%s %s L%s %s C%s %s %s %s %s %s C%s %s %s %s %s %s Z" % tuple(_n(v) for v in (
                cx - 27, cy - 22, cx + 27, cy - 22, cx + 27, cy + 6, cx + 14, cy + 17, cx, cy + 17, cx - 14, cy + 17, cx - 27, cy + 6, cx - 27, cy - 22)), METAL),
                  FR(cx - 5, cy + 14, 10, 30, METAL)]
        else:
            o += [FR(cx - 30, 14, 60, 18, SOFT), FC(cx, cy - 4, 30, METAL), FR(cx - 6, cy + 22, 12, 22, METAL)]
        o += [t(cx, 124, name, "sm b mid"), t(cx, 138, sub, "xs mid mu")]
    # แถวล่าง: interpapillary line
    for j, scar in enumerate((False, True)):
        x = 8 + j * 206; cx, cy = x + 99, 214
        o.append(film(x, 156, 198, 116, "#1d1d1d"))
        if not scar:
            o.append(FE(cx, cy, 82, 44, SOFT))
        else:
            o.append(FP("M%s %s C%s %s %s %s %s %s Q%s %s %s %s Q%s %s %s %s Q%s %s %s %s C%s %s %s %s %s %s C%s %s %s %s %s %s C%s %s %s %s %s %s Z" % tuple(_n(v) for v in (
                cx - 82, cy, cx - 82, cy - 30, cx - 52, cy - 44, cx - 22, cy - 44, cx - 10, cy - 44, cx - 7, cy - 30, cx, cy - 24, cx + 7, cy - 30,
                cx + 10, cy - 44, cx + 22, cy - 44, cx + 52, cy - 44, cx + 82, cy - 30, cx + 82, cy, cx + 82, cy + 30, cx + 52, cy + 44, cx, cy + 44,
                cx - 52, cy + 44, cx - 82, cy + 30, cx - 82, cy)), SOFT))
        o.append(FE(cx, cy + 6, 34, 12, METAL))
        tips = [(-58, -10), (-32, -24), (0, -28), (32, -24), (58, -10)]
        for k, (dx, dy) in enumerate(tips):
            if scar and k == 2:
                o += [FL(cx, cy + 2, cx, cy - 12, METAL, 3), FC(cx, cy - 16, 8, METAL)]
            else:
                o += [FL(cx + dx * 0.45, cy + 2 + dy * 0.2, cx + dx, cy + dy, METAL, 3),
                      FP("M%s %s Q%s %s %s %s" % (_n(cx + dx - 6), _n(cy + dy - 3), _n(cx + dx), _n(cy + dy + 6), _n(cx + dx + 6), _n(cy + dy - 3)), None, METAL, 2.4)]
        o.append(FP("M%s %s Q%s %s %s %s Q%s %s %s %s" % tuple(_n(v) for v in (cx - 62, cy - 16, cx - 34, cy - 36, cx, cy - 36, cx + 34, cy - 36, cx + 62, cy - 16)), None, "#e8bb63", 1.6, "4 3"))
        o.append(t(cx, 288, "ปกติ: เส้นประขนานขอบไต" if not scar else "แผลเป็น: ขอบไตบุ๋มเข้าหา calyx", "xs mid" + (" tbad" if scar else "")))
    o.append(t(210, 304, "เส้นประ = interpapillary line (ลากผ่านปลาย papilla)", "xs mid mu"))
    return svg(420, 312, "รูปร่าง calyx ปกติ blunted clubbed และ interpapillary line", *o)

F3 = {"ivp": fig("IVP ทีละฟิล์ม — contrast เดินทางจากเนื้อไตลงกระเพาะปัสสาวะ",
        "ฉีด iodinated contrast ทางหลอดเลือดดำ → **1 นาที** contrast อยู่ในหลอดเลือดฝอยและ tubule เนื้อไตจึงขาวทั้งก้อน (**nephrogram**) → **5 นาที** เริ่มไหลลง calyx → **10 นาที** รัดเข็มขัดกดท่อไตที่ pelvic brim ให้ contrast ค้างจน **PCS ขยายเต็มที่** → **15 นาที** ปล่อยเข็มขัดทันที contrast ไหลลง **ท่อไตทั้งสาย** → ถ่ายตอน **กระเพาะปัสสาวะเต็ม** และ **หลังปัสสาวะ** ดูปัสสาวะค้าง (เวลาตามสไลด์ อ้าง Madaan & Ghasi 2022)",
        _ivp()),
      "calyx": fig("Calyx ปกติ vs ขยาย และ interpapillary line",
        "แถวบน: calyx ปกติเป็น **ถ้วย (cupped)** เพราะ papilla ยื่นเข้ามา ขอบ **fornix แหลม** · เมื่อความดันในระบบรวบรวมปัสสาวะสูงขึ้น fornix ถูกดันจน **มน (blunted)** แล้ว papilla ถูกกดแบนจน calyx **นูนออก (clubbed/ballooned)** · แถวล่าง: เส้นที่ลากผ่านปลาย papilla (**interpapillary line**) ปกติ **ขนานกับขอบไต** (สไลด์) ถ้าขอบไตบุ๋มลงเหนือ calyx ที่ clubbed = เนื้อไตบางเฉพาะที่ = **แผลเป็น** จาก chronic pyelonephritis/reflux nephropathy · ใน hydronephrosis ทั้งไตจะบางสม่ำเสมอ",
        _calyx())}

sec("neph-img-03", "IVP/IVU และ retrograde pyelogram — ฟิล์มตามเวลา",
    "contrast ถูกกรองแล้วขับออก → เห็นเนื้อไต PCS ท่อไต กระเพาะ · ไตปกติ · calyx ขยาย · ACR ไม่ใช้เป็นประจำแล้ว", 9,
"""### หลักการ
**IVP (intravenous pyelogram) / IVU (urogram)** = ถ่าย X-ray ต่อเนื่องหลังฉีด **iodinated contrast** ทางหลอดเลือดดำ — "Enhanced visualization of KUB structure through different phases" (สไลด์ · Fried & Morgan 2019)
- contrast ถูก **กรองที่ glomerulus อย่างเดียว ไม่ถูกดูดกลับ** → ขณะท่อไตดูดน้ำกลับ contrast ถูก **ทำให้เข้มข้นขึ้น** → ขาวชัดใน calyx ท่อไต กระเพาะ
- ภาพจึงขึ้นกับ **การทำงานของไต** — ไตที่ทำงานน้อยขับ contrast ได้น้อย ภาพจาง
- **Retrograde pyelogram** = ใส่สายทางท่อไตผ่าน cystoscope แล้วฉีด contrast ย้อนขึ้น → เห็นทางเดินปัสสาวะได้ **โดยไม่ขึ้นกับการทำงานของไต** และไม่ต้องให้ contrast เข้ากระแสเลือด

### ฟิล์มแต่ละช่วงเวลา (สไลด์)
[[fig:ivp]]
| เวลาหลังฉีด | ใช้ดู |
|---|---|
| **1 นาที (nephrographic phase)** | เนื้อไต ขอบ ขนาด |
| **5 นาที (early excretion)** | pelvicalyceal system และท่อไตส่วนบน |
| **10 นาที (pyelographic phase)** | PCS ที่ขยายเต็มที่ (หลังกดท้อง 5 นาที) |
| **15 นาที (KUB radiograph)** | ขอบท่อไตและกระเพาะปัสสาวะ (ถ่ายทันทีหลังปล่อย) |
| **Full bladder** | รูปร่างและขอบกระเพาะปัสสาวะ |
| **Post-void** | ปริมาณปัสสาวะค้าง |
ท่ามาตรฐาน **supine AP** · เพิ่ม **oblique/lateral ± prone** เมื่อภาพก้ำกึ่งหรือสงสัย

### ไตปกติบน IVP (สไลด์ · Krairittichai 2011)
- ตำแหน่ง: **ขวา L1–L3 · ซ้าย T12–L2** · ความยาว **9.3–10.7 ซม. (คนไทย)** / 9–12 ซม. (ต่างประเทศ)
- ขอบเรียบ · **แกนขนานกับ psoas** · **interpapillary line ขนานกับขอบไต**
[[fig:calyx]]
#### ทำไมภาพถึงออกมาแบบนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Nephrogram ขาวทั้งไตที่ 1 นาที** | contrast อยู่ในหลอดเลือดฝอยและ tubule ของเนื้อไต | ไตเล็ก ขอบขรุขระ หรือมีก้อนดันขอบ |
| **Nephrogram ช้าและ "ขาวขึ้นเรื่อย ๆ" (obstructive nephrogram)** | ท่ออุดกั้นเฉียบพลัน → **ความดันใน tubule สูง** น้ำไหลช้า น้ำถูกดูดกลับมากขึ้น contrast ค้างและเข้มข้นในเนื้อไต แต่ไหลลง calyx ช้า | ไตข้างที่อุดกั้น **nephrogram ขาวช้าและค้าง** + **ขับ contrast ช้า** (delayed excretion) |
| **Calyx มน → นูนออก** | ความดันย้อนจากการอุดกั้น ดัน fornix และ papilla | hydronephrosis · ไล่ลงไปจะเห็น **ท่อไตขยายจนถึงจุดอุดกั้น** |
| **ขอบไตบุ๋มเหนือ calyx ที่ clubbed** | แผลเป็นทำให้เนื้อไตตรงนั้นหดบาง | chronic pyelonephritis / reflux nephropathy (ต่างจาก hydronephrosis ที่บางทั่วไต) |
| **ไตไม่ขับ contrast เลย** | ไม่มีการกรอง (ไตไม่ทำงาน อุดกั้นนาน หลอดเลือดอุด) | ต้องใช้ retrograde pyelogram หรือ nuclear scan ต่อ |

### ACR — IVP ไม่ได้อยู่ในการตรวจประจำแล้ว (สไลด์)
| ข้อบ่งชี้ | ความเหมาะสม |
|---|---|
| สงสัยนิ่ว | **Usually not appropriate!!** |
| Microscopic hematuria | Usually not appropriate |
| AKI/CKD | Usually not appropriate |
| Acute pyelonephritis | Usually not appropriate |
> "Does not form a part of the current routine urological imaging protocols. Indicated in some situations when USG, CT and MRI are either unavailable or considered inappropriate." — Madaan & Ghasi 2022

เหตุผล: CT ไม่ฉีดสีหานิ่วได้ไวกว่าและเร็วกว่า · IVP ต้องฉีด contrast (เสี่ยงต่อไตและแพ้) ใช้หลายฟิล์ม ลมในลำไส้บัง — ยังพอใช้ได้ในที่ที่ไม่มี CT
""",
    ["IVP: 1 นาที nephrogram · 5 นาที PCS · 10 นาที กดท้อง · 15 นาที ปล่อยดูท่อไต · full bladder · post-void",
     "contrast ถูกกรองไม่ถูกดูดกลับ → เข้มข้นในท่อ — ภาพขึ้นกับการทำงานของไต",
     "อุดกั้นเฉียบพลัน: nephrogram ช้าแต่ขาวขึ้นเรื่อย ๆ + ขับช้า",
     "Interpapillary line ต้องขนานขอบไต — ไม่ขนาน = แผลเป็นเฉพาะที่",
     "ACR: IVP usually not appropriate ทุกข้อบ่งชี้ ใช้เมื่อไม่มี US/CT/MRI"],
    [mcq(N(5), "During an intravenous urogram, the film taken about 1 minute after contrast injection (nephrographic phase) is mainly used to assess:",
         ["Bladder shape and outline", "The renal parenchyma, contour and size", "Post-void residual urine", "The full length of both ureters", "Vesicoureteric reflux"], 1,
         "ที่ **1 นาที** contrast ยังอยู่ในหลอดเลือดฝอยและ tubule ของเนื้อไต ไตจึงขาวทั้งก้อน (**nephrogram**) ใช้ดู **เนื้อไต ขอบ และขนาด** (สไลด์)\n\n- ท่อไตทั้งสาย → ฟิล์ม **15 นาที** หลังปล่อยเข็มขัด\n- รูปร่างกระเพาะปัสสาวะ → ฟิล์ม **full bladder**\n- ปัสสาวะค้าง → ฟิล์ม **post-void**\n- Vesicoureteric reflux ต้องใช้ **voiding cystourethrogram** (ฉีด contrast เข้ากระเพาะแล้วดูการไหลย้อน) — IVP ไม่ได้ออกแบบมาดูสิ่งนี้",
         "IVP 1 นาที = nephrogram", "IVU phases", REF("IVP — time after contrast administration"), ["3.2.3", "B9.1.1(1)"]),
     mcq(N(6), "A patient with acute left ureteric obstruction undergoes an IVU. Which appearance of the left kidney is most typical?",
         ["Absent nephrogram on all films", "Immediate dense pyelogram at 1 minute", "A delayed nephrogram that becomes increasingly dense, with delayed excretion into the collecting system", "A small kidney with a thin cortex", "Normal nephrogram and excretion"], 2,
         "การอุดกั้นเฉียบพลันทำให้ **ความดันใน tubule สูง** → ปัสสาวะไหลช้า น้ำถูกดูดกลับนานขึ้น contrast จึง **ค้างและเข้มข้นในเนื้อไต** ได้ภาพ **nephrogram ที่มาช้าแต่ขาวขึ้นเรื่อย ๆ (obstructive nephrogram)** และ contrast ลง calyx ช้า\n\n- **ไม่มี nephrogram เลย** — คิดถึงหลอดเลือดแดงไตอุด หรือไตไม่ทำงานมานาน ไม่ใช่อุดกั้นเฉียบพลันทั่วไป\n- **Pyelogram ทันทีที่ 1 นาที** — ผิดลำดับ ในไตปกติก็ยังไม่ลง calyx ที่ 1 นาที\n- **ไตเล็ก cortex บาง** — โรคไตเรื้อรัง ไม่ใช่การอุดกั้นเฉียบพลัน\n- ภาพปกติ — ไม่เข้ากับการอุดกั้น",
         "อุดกั้นเฉียบพลัน = delayed, increasingly dense nephrogram", "Obstructive nephrogram", ["ตำรารังสีมาตรฐาน (Grainger & Allison)"], ["3.2.3", "2.3.14-3(9)"]),
     mcq(N(7), "On an IVU, the interpapillary line is no longer parallel to the renal outline: the cortex is focally thinned over a clubbed upper-pole calyx while the rest of the kidney is normal. The most likely diagnosis is:",
         ["Acute ureteric obstruction", "Focal cortical scarring from chronic pyelonephritis / reflux nephropathy", "Normal variant (fetal lobulation)", "Simple renal cyst", "Medullary sponge kidney"], 1,
         "สไลด์: **interpapillary line ควรขนานกับขอบไต** — ถ้าเนื้อไตบาง **เฉพาะที่เหนือ calyx ที่ clubbed** แปลว่ามี **แผลเป็น** ดึงเนื้อไตตรงนั้นหดลง ซึ่งเป็นลักษณะของ **chronic pyelonephritis / reflux nephropathy**\n\n- **อุดกั้นเฉียบพลัน** — calyx ขยายทุกอันและเนื้อไตบางสม่ำเสมอทั้งไต ไม่ใช่เฉพาะจุด\n- **Fetal lobulation** — ขอบเป็นลอน แต่บุ๋มอยู่ **ระหว่าง** calyx และ calyx ปกติ\n- **Simple cyst** — ดัน calyx ให้โค้งหลบ ไม่ทำให้ calyx clubbed\n- **Medullary sponge kidney** — เห็น contrast เป็นเส้นริ้วใน papilla (paintbrush) ไม่ใช่แผลเป็นที่ cortex",
         "เนื้อไตบางเฉพาะที่เหนือ calyx clubbed = แผลเป็น", "Interpapillary line", REF("IVP — interpapillary line"), ["3.2.3", "2.3.14(14)"]),
    ], nl=["3.2.3", "B9.1.1(1)", "B9.1.1(2)", "2.3.14-3(9)"], figs=F3)

# ═════════════════════════════════════════════ 4
def _ctk(cx, cy, ph):
    """ภาพตัดขวางไตขวา (hilum หันไปทางขวาของภาพ = แนวกลางตัว) ในแต่ละเฟส"""
    par = {0: "#777777", 1: "#ededed", 2: "#c8c8c8", 3: "#9c9c9c"}[ph]
    o = [bean(cx, cy, 26, 30, par, 0, 1)]
    if ph == 1:      # medulla (pyramids) ยังมืด
        for (dx, dy) in ((-14, -18), (-22, -2), (-14, 15), (1, -22), (1, 21)):
            o.append(FC(cx + dx, cy + dy, 5.5, "#6c6c6c"))
    o.append(FE(cx + 14, cy, 10, 9, "#2a2a2a"))                       # renal sinus fat
    if ph == 0:
        o.append(FC(cx + 13, cy, 4.2, METAL))                         # นิ่วใน pelvis
    elif ph == 1:
        o.append(FC(cx - 13, cy - 27, 8, METAL, "#1a1a1a", 1))        # ก้อนเลือดมาก
    elif ph == 2:
        o.append(FC(cx - 12, cy + 4, 7.5, "#4c4c4c"))                 # ก้อน/หนองไม่รับสี
    else:
        o += [FL(cx + 12, cy - 3, cx - 2, cy - 15, METAL, 2.6), FL(cx + 12, cy + 3, cx - 2, cy + 15, METAL, 2.6),
              FE(cx + 15, cy, 9, 7.5, METAL), FC(cx + 16, cy, 3.4, "#5a5a5a")]
    return o

def _ctphase():
    xs = [56, 158, 260, 362]
    o = [line(20, 34, 402, 34, "lmu w2", "ah-mu")]
    tl = ["ไม่ฉีดสี", "15–45 วินาที", "80–120 วินาที", "> 3 นาที"]
    for x, s in zip(xs, tl):
        o += [circ(x, 34, 4, "acf"), t(x, 22, s, "xs b mid tac")]
    name = [("Plain", "นิ่ว · ไตบวมน้ำ", "ขนาดไต"), ("Corticomedullary", "cortex สว่างก่อน", "ก้อนเลือดมาก (RCC)"),
            ("Nephrographic", "เนื้อไตสว่างทั่ว", "ก้อน/หนองเด่นชัด"), ("Excretory", "contrast ในท่อ", "filling defect")]
    for i, x in enumerate(xs):
        o.append(film(x - 47, 48, 94, 82, "#1a1a1a"))
        o += _ctk(x - 4, 89, i)
        a, b, c = name[i]
        o += [t(x, 148, a, ("xs b mid" if i == 1 else "sm b mid")), t(x, 163, b, "xs mid"), t(x, 177, c, "xs mid mu")]
    o += [TF(xs[0] + 22, 64, "นิ่ว", "xs b"), FL(xs[0] + 25, 67, xs[0] + 13, 85, FT2, 1),
          TF(xs[1] - 44, 64, "RCC", "xs b"), FL(xs[1] - 30, 66, xs[1] - 19, 59, FT2, 1),
          TF(xs[2] - 44, 126, "ก้อน", "xs b"), FL(xs[2] - 32, 117, xs[2] - 17, 97, FT2, 1),
          TF(xs[3] + 4, 126, "defect", "xs b"), FL(xs[3] + 16, 117, xs[3] + 14, 93, FT2, 1)]
    o += [box(10, 192, 400, 48, "ms", "contrast ที่ขับออกมามีความทึบใกล้นิ่ว → นิ่วกลืนหายไปในสีขาว\nหานิ่วจึงต้องใช้ CT ไม่ฉีดสี (และทำเฟสนี้ก่อนเสมอใน CTU)", "", 8, 12)]
    return svg(420, 248, "เฟสของ CT urography และสิ่งที่แต่ละเฟสแสดง", *o)

F4 = {"ctphase": fig("CT urography 4 เฟส — contrast อยู่ที่ไหน เห็นอะไร",
        "**ก่อนฉีด**: นิ่ว (ขาวมาก) hydronephrosis ขนาดไต · **Corticomedullary (15–45 วินาที)**: contrast ถึง cortex ก่อน (cortex รับเลือดส่วนใหญ่ของไต) cortex ขาว medulla ยังมืด → **ก้อนที่เลือดมากอย่าง RCC** สว่างเด่น แต่ก้อนเล็กในเนื้อไตอาจถูกบังด้วย medulla ที่มืด · **Nephrographic (80–120 วินาที)**: contrast ถูกกรองเข้าทุก tubule เนื้อไตสว่างสม่ำเสมอ → **ก้อนหรือหนองที่ไม่รับสี** เด่นที่สุด · **Excretory (> 3 นาที)**: contrast ลงระบบรวบรวมปัสสาวะ → สิ่งที่ไม่ทึบในท่อเห็นเป็น **filling defect** (มะเร็ง urothelium ลิ่มเลือด นิ่วโปร่งรังสี) — เวลาตามสไลด์ (Grainger & Allison 2021 · Fried 2019)",
        _ctphase())}

sec("neph-img-04", "CT และ CT urography — เฟสของสารทึบรังสี (+ MRI)",
    "HU · 4 เฟสของ CTU และเหตุผลของแต่ละเฟส · ทำไมหานิ่วต้องไม่ฉีดสี · CT ในนิ่ว · MRI/MRU", 10,
"""### CT วัดค่า attenuation เป็น Hounsfield unit (HU)
CT ฉายรังสีรอบตัวแล้วคำนวณว่าแต่ละจุดดูดกลืนรังสีเท่าไร เทียบกับน้ำ (ค่าโดยประมาณจากตำรามาตรฐาน)
| เนื้อเยื่อ | HU โดยประมาณ | ความหมายในงานไต |
|---|---|---|
| ลม | −1000 | ก๊าซใน EPN · ลมรอบไต |
| ไขมัน | −100 ถึง −50 | ก้อนที่มีไขมันในไต = **angiomyolipoma** |
| น้ำ / ถุงน้ำธรรมดา | 0–20 | simple cyst ไม่รับสี (เพิ่ม < 20 HU หลังฉีด) |
| เนื้อไตไม่ฉีดสี | ~30–40 | |
| นิ่ว uric acid | ราว 200–500 | เห็นบน CT แม้ไม่เห็นบน KUB |
| นิ่วแคลเซียม | > 1000 | |

### 4 เฟสของ CT urography (สไลด์)
[[fig:ctphase]]
| เวลาหลังฉีด | เฟส | ใช้ดู |
|---|---|---|
| **ก่อนฉีด (plain, non-contrast)** | non-contrast | **นิ่ว · hydronephrosis · ขนาดไต** |
| **15–30 / 30–45 วินาที** | corticomedullary | **ก้อนที่เลือดมาก** เช่น renal cell carcinoma |
| **80–100 / 90–120 วินาที** | nephrographic | **ก้อนกินที่ (space-taking lesion)** ในไต |
| **หลัง 3 นาที** | excretory | **filling defect** ในทางเดินปัสสาวะ |
(ตัวเลขสองชุดคือโปรโตคอลสองแบบที่ตำราใช้ — Grainger & Allison 2021 · Fried & Morgan 2019)

#### ทำไมภาพถึงออกมาแบบนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Cortex สว่างก่อน medulla** | เลือดไปไตส่วนใหญ่ไปที่ cortex (glomeruli) — contrast จึงถึง cortex ก่อน แล้วจึงถูกกรองลง tubule ใน medulla | RCC ชนิด clear cell เลือดมาก สว่างจัดในเฟสนี้ · ระวัง medulla ที่ยังมืดดูเหมือนก้อน |
| **เนื้อไตสว่างสม่ำเสมอ** | contrast ถูกกรองเข้าทุก tubule ทั้ง cortex และ medulla | ก้อน หนอง แผลขาดเลือด (ไม่รับสี) ตัดกับพื้นหลังชัดที่สุด |
| **ท่อสว่างขาวจัด** | contrast ถูกขับและทำให้เข้มข้นในระบบรวบรวม | สิ่งที่ไม่ทึบในท่อ = **filling defect**: มะเร็ง urothelium · ลิ่มเลือด · นิ่วโปร่งรังสี · papilla ที่หลุด |
| **นิ่วหายไปในเฟสฉีดสี** | contrast ที่ขับออกมาขาวพอ ๆ กับนิ่ว | **หานิ่วต้องใช้ CT ไม่ฉีดสี** · ACR: CT KUB **with contrast = usually not appropriate** ในนิ่ว |

### CT กับนิ่ว (สไลด์ · ACR 2023 · Dell'Aversana 2025)
- **Sensitivity 97% · Specificity 95%** สำหรับนิ่วทุกขนาดทุกตำแหน่ง
- ข้อดี: บอก **จำนวน ขนาด ตำแหน่งที่แน่นอน** · **แยกจากหินปูนอื่น** (phlebolith) · เห็น **ภาวะแทรกซ้อน** (hydronephrosis) · **วางแผนผ่าตัด** · บอก **ชนิดนิ่ว** ด้วย **dual-energy CT (DECT)** — ใช้ X-ray สองพลังงาน แยก uric acid (ไม่มีธาตุหนัก) ออกจากนิ่วแคลเซียม
- สไลด์ CT: corticomedullary phase เห็น **moderate left hydronephrosis** · excretory phase เห็นนิ่วในท่อไตซ้ายส่วนกลางพร้อม **"soft tissue rim sign"** = ผนังท่อไตที่บวมล้อมนิ่วเป็นวง (phlebolith ไม่มี)

### MRI / MR urography (ไม่มีหน้าเนื้อหาในสไลด์ — ตำรามาตรฐาน)
- **T2-weighted**: น้ำสว่าง → **MR urography แบบไม่ฉีดสี** เห็นท่อที่ขยายได้ ใช้ใน **หญิงตั้งครรภ์** และเด็ก (ไม่มีรังสี)
- นิ่วไม่ให้สัญญาณ (signal void) → **MRI ไม่เหมาะหานิ่ว** (ACR: usually not appropriate)
- ใช้ **gadolinium** เมื่อต้องดูการรับสีของก้อน/ฝีโดยไม่ใช้รังสี — ข้อควรระวังเรื่อง NSF อยู่หัวข้อถัดไป
- ACR: complicated acute pyelonephritis — MRI **may be appropriate** (ทางเลือกเมื่อฉีด iodinated contrast ไม่ได้)

### ACR — CT urography (สไลด์)
| ข้อบ่งชี้ | ความเหมาะสม |
|---|---|
| สงสัยนิ่ว | **Usually APPROPRIATE (non-contrast)** |
| Microscopic hematuria | May be appropriate |
| AKI/CKD | May be appropriate (non-contrast) |
| Acute pyelonephritis | May be appropriate (complicated) |
""",
    ["CTU: plain → corticomedullary (15–45 s) → nephrographic (80–120 s) → excretory (> 3 นาที)",
     "CM phase: ก้อนเลือดมาก (RCC) · nephrographic: ก้อน/หนอง · excretory: filling defect",
     "หานิ่ว = CT ไม่ฉีดสี (contrast ขาวเท่านิ่ว บังนิ่ว)",
     "CT นิ่ว: sens 97% spec 95% · soft tissue rim sign · DECT บอกชนิดนิ่ว",
     "MRI: ไม่มีรังสี เหมาะตั้งครรภ์ แต่เห็นนิ่วไม่ดี"],
    [mcq(N(8), "A 68-year-old smoker with painless gross haematuria undergoes CT urography. In which phase is a small urothelial carcinoma of the renal pelvis best seen as a filling defect?",
         ["Non-contrast phase", "Corticomedullary phase", "Nephrographic phase", "Excretory phase", "Arterial angiographic phase"], 3,
         "มะเร็ง urothelium อยู่ **ในท่อ** — จะเห็นได้ชัดเมื่อท่อเต็มไปด้วย contrast สีขาว ซึ่งเกิดใน **excretory phase (หลัง 3 นาที)** ก้อนจึงเป็นรอย **filling defect** (สไลด์)\n\n- **Non-contrast** — ใช้หานิ่ว/ไตบวมน้ำ ก้อนเนื้อเยื่ออ่อนในท่อแทบไม่ต่างจากปัสสาวะ\n- **Corticomedullary** — ดีสำหรับก้อนเลือดมากในเนื้อไต (RCC)\n- **Nephrographic** — ดีสำหรับก้อนในเนื้อไต ไม่ใช่ในท่อ\n- **Arterial angiographic phase** — ดูหลอดเลือดแดง (เช่น renal artery stenosis) ไม่ใช่ท่อปัสสาวะ",
         "Filling defect = excretory phase", "CT urography phases", REF("CT urography — phases"), ["3.3.20", "B9.2.4-3(2)", "2.1.43"]),
     mcq(N(9), "Why is a non-contrast series always obtained before contrast when CT is used to look for urinary tract stones?",
         ["Contrast dissolves calcium stones", "Excreted contrast has an attenuation similar to stones and can mask them", "Stones are only visible on MRI after contrast", "Non-contrast CT has a higher radiation dose, so it is done first", "Contrast causes ureteric spasm that pushes stones into the bladder"], 1,
         "contrast ที่ถูกขับลงระบบรวบรวมปัสสาวะมีค่า HU สูงพอ ๆ กับนิ่ว — ถ้าถ่ายหลังฉีด **นิ่วจะกลืนหายไปในสีขาว** จึงต้องทำ **non-contrast** ก่อน (ACR: CT KUB **with** contrast = usually not appropriate ในสงสัยนิ่ว) และเฟสนี้ยังเป็นค่าพื้นฐานไว้วัดการรับสีของก้อน\n\n- contrast **ไม่ละลายนิ่ว**\n- MRI เห็นนิ่วไม่ดี (signal void) ไม่ว่าฉีดหรือไม่\n- CT ไม่ฉีดสีไม่ได้มีรังสีมากกว่า — ยิ่งหลายเฟสยิ่งรังสีมาก\n- contrast ไม่ทำให้ท่อไตบีบไล่นิ่ว",
         "หานิ่ว: CT ไม่ฉีดสี", "Non-contrast CT for stones", REF("CT urography — non-contrast phase; ACR flank pain"), ["3.3.20", "2.3.14-3(15)"]),
    ], nl=["3.3.20", "B9.2.3-3(1)", "B9.2.4-3(2)", "2.3.14-3(15)"], figs=F4)

# ═════════════════════════════════════════════ 5
def _cin():
    o = [box(110, 6, 200, 40, "ac", "Iodinated contrast\n(IV / intra-arterial)", "", 8, 12.5),
         ar(170, 46, 108, 66, "lmu", "ah-mu"), ar(250, 46, 312, 66, "lmu", "ah-mu"),
         box(10, 68, 195, 30, "wa", "กลไกหลอดเลือด (hemodynamic)", "b", 8, 12),
         box(215, 68, 195, 30, "bad", "พิษตรงต่อเซลล์ท่อไต", "b", 8, 12)]
    L = [("bx", "adenosine, endothelin ↑\nNO, prostaglandin ↓"), ("bx", "หลอดเลือดหดตัว + เลือดหนืด\nเลือดไป medulla ลดลง"),
         ("ms", "outer medulla ขาด O₂\n(mTAL ใช้ O₂ มาก pO₂ ต่ำอยู่แล้ว)")]
    R = [("bx", "ท่อไตดูดน้ำกลับ\ncontrast เข้มข้นใน tubule"), ("bx", "vacuolization · ROS\napoptosis ของเซลล์ท่อไต"),
         ("ms", "tubular injury\n(ยิ่งขาดน้ำ ยิ่งเข้มข้น)")]
    for i, ((c1, s1), (c2, s2)) in enumerate(zip(L, R)):
        y = 112 + i * 58
        o += [box(10, y, 195, 44, c1, s1, "", 8, 11.5), box(215, y, 195, 44, c2, s2, "", 8, 11.5)]
        o += [ar(107, y - 14, 107, y - 1, "lmu", "ah-mu"), ar(312, y - 14, 312, y - 1, "lmu", "ah-mu")]
    o += [ar(107, 274, 170, 296, "lbad", "ah-bad"), ar(312, 274, 250, 296, "lbad", "ah-bad"),
          box(70, 298, 280, 46, "bad", "CI-AKI: Cr ขึ้นใน 24–48 ชม. · สูงสุด 3–5 วัน\nส่วนใหญ่กลับสู่ค่าเดิมใน 7–10 วัน", "", 8, 11.5),
          box(10, 356, 400, 48, "ok", "ป้องกัน (eGFR < 30 หรือ AKI): IV isotonic fluid\nขยาย volume · ลดการหดของหลอดเลือด · เจือจาง contrast ในท่อ", "", 8, 11.5)]
    return svg(420, 412, "กลไกการเกิดไตบาดเจ็บเฉียบพลันจากสารทึบรังสีไอโอดีน", *o)

def _gd():
    import math
    o = [t(105, 18, "Macrocyclic", "sm b mid tok"), t(315, 18, "Linear (กลุ่ม I ทั้งหมด)", "sm b mid tbad"),
         circ(105, 80, 46, "ok"), circ(105, 80, 30, "bx")]
    for k in range(8):
        a = k * math.pi / 4
        o.append(circ(105 + 38 * math.cos(a), 80 + 38 * math.sin(a), 5, "okf"))
    o += [circ(105, 80, 13, "inkf"), t(105, 84, "Gd", "xs b mid tpa"),
          path("M250 112 C262 70 280 54 300 60 C320 66 334 92 352 72 C362 60 372 58 382 64", "lbad w3"),
          circ(250, 112, 5, "badf"), circ(275, 64, 5, "badf"), circ(330, 84, 5, "badf"), circ(382, 64, 5, "badf"),
          circ(318, 112, 13, "inkf"), t(318, 116, "Gd", "xs b mid tpa"), ar(318, 96, 318, 72, "lbad", "ah-bad"),
          t(340, 132, "Gd³⁺ หลุดออก", "xs tbad"),
          t(105, 146, "Gd ถูกล็อกในกรง → เสถียร", "xs mid"), t(315, 150, "สายเปิด → Gd หลุดง่ายเมื่อค้างนาน", "xs mid"),
          box(10, 166, 400, 54, "ms", "eGFR < 30 / ฟอกไต → ขับ Gd ช้า (ชั่วโมง → วัน) → Gd³⁺ หลุดจาก chelate\nสะสมที่ผิวหนัง ข้อ อวัยวะ → fibrocyte สร้างพังผืด = NSF (ผิวแข็งหนา ข้อยึด)", "", 8, 11.5)]
    return svg(420, 228, "chelate ของ gadolinium แบบ macrocyclic และ linear กับกลไก NSF", *o)

F5 = {"cin": fig("ทำไม iodinated contrast ทำให้ไตบาดเจ็บ — สองทางที่บรรจบกัน",
        "**ทางหลอดเลือด**: contrast กระตุ้น adenosine และ endothelin ลด NO → หลอดเลือดในไตหดตัว และ contrast ทำให้เลือดหนืดขึ้น → เลือดไป **medulla** ลด ซึ่งปกติขาด O₂ อยู่แล้ว (vasa recta แลก O₂ ลัดกันแบบ countercurrent และ **mTAL** ใช้ O₂ มากในการดูด Na) · **ทางพิษตรง**: ขณะท่อไตดูดน้ำกลับ contrast ยิ่งเข้มข้นในท่อ → เซลล์บวมเป็นถุง (vacuolization) เกิดอนุมูลอิสระ ตายแบบ apoptosis · **การขาดน้ำ** ขยายทั้งสองทาง — จึงป้องกันด้วยการให้ **สารน้ำ isotonic** (ไม่อยู่ในสไลด์ — ACR–NKF 2020 · ESUR 2018)",
        _cin()),
      "gd": fig("Gadolinium กับ NSF — ปัญหาอยู่ที่ Gd³⁺ หลุดจาก “กรง” ไม่ใช่ไตวาย",
        "Gd³⁺ อิสระเป็นพิษ จึงต้องจับไว้ในโมเลกุล **chelate** — แบบ **macrocyclic** ล้อม Gd เป็นวงปิด เสถียรมาก · แบบ **linear** เป็นสายเปิด Gd หลุดได้ง่ายกว่า (แลกที่กับ Zn Fe Ca ในร่างกาย) · ไตปกติขับ gadolinium หมดในไม่กี่ชั่วโมง แต่ใน **eGFR < 30 หรือฟอกไต** ยาค้างนานหลายวัน Gd³⁺ จึงหลุดออกมาสะสมที่ผิวหนัง ข้อ และอวัยวะ กระตุ้น fibrocyte สร้างพังผืด = **nephrogenic systemic fibrosis** · ผู้ป่วย NSF เกือบทั้งหมดได้ยา **กลุ่ม I** (linear ทั้งหมด) — ยา **กลุ่ม II** (ส่วนใหญ่เป็น macrocyclic) ความเสี่ยงต่ำมาก (ACR–NKF 2021 · ไม่อยู่ในสไลด์)",
        _gd())}

sec("neph-img-05", "สารทึบรังสีกับไต — CI-AKI และ gadolinium/NSF",
    "ทำไม contrast ทำร้ายไต · eGFR เท่าไรต้องป้องกัน (ACR–NKF 2020 · ESUR 2018) · metformin · gadolinium กลุ่ม I/II", 9,
"""> หัวข้อนี้ **ไม่อยู่ในสไลด์** แต่เป็นคำถามที่นักไตถูกปรึกษาบ่อยที่สุดก่อนส่ง CT/MRI และมีในข้อสอบ (Mock) — เรียบเรียงจาก **ACR–NKF consensus 2020 (iodinated) · ACR–NKF 2021 (gadolinium) · ACR Manual on Contrast Media · ESUR 2018**

### CA-AKI กับ CI-AKI — ไม่ใช่สิ่งเดียวกัน
- **Contrast-associated AKI (CA-AKI)** = Cr ขึ้นหลังได้ contrast **ไม่ว่าจากสาเหตุใด** (ความสัมพันธ์)
- **Contrast-induced AKI (CI-AKI)** = AKI ที่ **contrast เป็นสาเหตุ** (เหตุ–ผล)
- ผู้ป่วยในโรงพยาบาลมี Cr ขึ้นลงจากเหตุอื่นบ่อย (sepsis ยา ความดันต่ำ) — การศึกษาแบบจับคู่ (propensity-matched) พบว่า **ความเสี่ยงจาก IV contrast ต่ำกว่าที่เคยเชื่อมาก** โดยเฉพาะเมื่อ eGFR ≥ 30
- อย่า **งดการตรวจที่จำเป็น** (เช่นสงสัย aortic dissection, PE, ฝีในช่องท้อง) เพียงเพราะกลัว contrast

### กลไก
[[fig:cin]]
#### ทำไมไตถึงเสียหาย
| สิ่งที่เกิด | กลไก | ผลทางคลินิก |
|---|---|---|
| **Medullary hypoxia** | contrast → adenosine/endothelin ↑ NO ↓ → หลอดเลือดหดตัว · เลือดหนืด (iso-osmolar contrast หนืดกว่า) → vasa recta ไหลช้า · outer medulla ขาด O₂ อยู่แล้วเพราะ mTAL ใช้ O₂ มาก | ไตที่มี nephron เหลือน้อย (CKD) ทนได้น้อย |
| **พิษตรงต่อเซลล์ท่อไต** | contrast เข้มข้นขึ้นขณะท่อดูดน้ำกลับ → vacuolization · ROS · apoptosis | ขาดน้ำ = contrast เข้มข้นกว่า ไหลช้ากว่า → เสี่ยงขึ้น |
| **Osmotic load** | contrast รุ่นเก่า (high-osmolar) มี osmolality หลายเท่าของพลาสมา | ปัจจุบันใช้ low-/iso-osmolar contrast แล้ว |
| **ทำไมสารน้ำช่วย** | เพิ่ม volume → กด renin/vasoconstriction · ปัสสาวะไหลเร็ว → contrast เจือจางและสัมผัสเซลล์สั้นลง | ให้ **IV isotonic fluid** ก่อนและหลังฉีด |
| **ทำไม furosemide ไม่ช่วย** | ขับน้ำ → ขาดน้ำ ทำให้ contrast ยิ่งเข้มข้น | **ห้ามใช้เป็นการป้องกัน** |

### ประเมินความเสี่ยงและป้องกัน — iodinated contrast ทางหลอดเลือดดำ
| eGFR (mL/min/1.73 m²) | ความเสี่ยง CI-AKI (ACR–NKF 2020) | ทำอะไร |
|---|---|---|
| **≥ 45** | แทบไม่มี | ไม่ต้องให้สารน้ำป้องกัน |
| **30–44** | ต่ำมาก / ไม่แน่ชัด | พิจารณาเป็นรายบุคคลในผู้ที่เสี่ยงสูง |
| **< 30 ที่ยังไม่ได้ฟอกไต** | อาจมีความเสี่ยง | **ให้ IV volume expansion (NSS)** เว้นมีข้อห้าม (หัวใจวาย น้ำเกิน) |
| **AKI** | เสี่ยงที่สุด | ถือเหมือน eGFR < 30 — ฉีดเมื่อจำเป็นจริง + ให้สารน้ำ |
| **ฟอกไตอยู่ ไม่มีปัสสาวะ** | ไม่มีไตให้เสียเพิ่ม | **ไม่ต้องฟอกเลือดทันทีหลังฉีด** (เว้นน้ำเกิน) · ถ้ายังมีปัสสาวะ ให้ระวังเหมือน CKD |
- **ESUR 2018**: ให้สารน้ำเมื่อ **eGFR < 30** (IV หรือ intra-arterial second-pass) · **eGFR < 45** ถ้าฉีดเข้าหลอดเลือดแดงที่ไปถึงไตก่อน (first-pass) · หรือมี AKI · สูตร: **NSS 1 mL/kg/h 3–4 ชม. ก่อน และ 4–6 ชม. หลังฉีด** หรือ **NaHCO₃ 1.4% 3 mL/kg/h 1 ชม. ก่อนฉีด**
- ใช้ contrast **ปริมาณน้อยที่สุด** · ชนิด low-/iso-osmolar · เลี่ยงยาที่ทำร้ายไต (NSAID) ช่วงนั้นถ้าทำได้
- **ไม่แนะนำ**: N-acetylcysteine หรือ bicarbonate แทน NSS (ไม่ดีกว่า — PRESERVE trial 2018) · **ฟอกเลือดป้องกัน** · **furosemide**
- **Metformin** (ACR Manual): eGFR **≥ 30 และไม่มี AKI → ไม่ต้องหยุด** · eGFR **< 30 หรือ AKI → หยุดตอนฉีด** แล้วเริ่มใหม่หลัง 48 ชม. เมื่อไตคงที่ — เหตุผล: metformin ขับทางไต ถ้าเกิด AKI ยาจะสะสม → **lactic acidosis** (ตัว contrast เองไม่ได้ทำปฏิกิริยากับ metformin)

### Gadolinium (MRI) กับ NSF
[[fig:gd]]
| ประเด็น | สาระ |
|---|---|
| **NSF คืออะไร** | ผิวหนังหนาแข็ง (โดยเฉพาะแขนขา) ข้อยึดติด อาจมีพังผืดในอวัยวะภายใน · ไม่มีการรักษาที่ได้ผล |
| **ใครเสี่ยง** | **eGFR < 30 · ฟอกไต · AKI** ที่ได้ยา **กลุ่ม I** (gadodiamide, gadopentetate dimeglumine, gadoversetamide — linear) |
| **ยากลุ่ม II** | gadobutrol, gadoterate, gadoteridol, gadobenate — ความเสี่ยงต่ำมาก · ACR–NKF 2021: **ไม่จำเป็นต้องงดยากลุ่ม II เพราะ eGFR ต่ำ** ถ้าการตรวจจำเป็น |
| **ไตบาดเจ็บ?** | ที่ขนาดยาของ MRI gadolinium **แทบไม่ทำให้ AKI** — ปัญหาคือ NSF ไม่ใช่ CI-AKI |
| **ผู้ป่วยฟอกไต** | ใช้ยากลุ่ม II ขนาดต่ำที่สุด แล้วนัดฟอกเลือดโดยเร็วหลังตรวจ เพื่อเอา Gd ออก |
""",
    ["CI-AKI = contrast เป็นเหตุ · CA-AKI = แค่เกิดตามหลัง — ความเสี่ยงจาก IV contrast ต่ำกว่าที่เคยคิด",
     "ป้องกันด้วย IV isotonic fluid เมื่อ eGFR < 30 (ไม่ฟอกไต) หรือมี AKI — ไม่ใช้ furosemide NAC หรือฟอกเลือด",
     "กลไก: medulla ขาด O₂ (หลอดเลือดหดตัว) + พิษตรงต่อท่อไต · ขาดน้ำทำให้แย่ลง",
     "Metformin: eGFR ≥ 30 ไม่ต้องหยุด · < 30 หรือ AKI หยุดตอนฉีด เริ่มใหม่หลัง 48 ชม.",
     "NSF: Gd³⁺ หลุดจาก chelate (linear กลุ่ม I) ใน eGFR < 30/ฟอกไต · กลุ่ม II เสี่ยงต่ำมาก"],
    [mcq(N(10), "According to the 2020 ACR–NKF consensus, prophylactic IV volume expansion before intravenous iodinated contrast is indicated in which patient (assuming no contraindication to fluids)?",
         ["A 50-year-old diabetic with eGFR 75 mL/min/1.73 m²", "A 62-year-old on metformin with eGFR 52 mL/min/1.73 m²", "A 70-year-old with eGFR 24 mL/min/1.73 m² who is not on dialysis", "An anuric patient on maintenance haemodialysis", "A 30-year-old with a previous mild contrast rash and normal eGFR"], 2,
         "ACR–NKF 2020: ให้ **IV volume expansion** เมื่อ **eGFR < 30 ที่ยังไม่ได้ฟอกไต** หรือมี **AKI** · eGFR 30–44 พิจารณาเป็นรายบุคคล · **eGFR ≥ 45 ไม่ต้องป้องกัน**\n\n- eGFR 75 และ 52 — ความเสี่ยงแทบไม่มี (เบาหวานหรือ metformin ไม่ได้เปลี่ยนเกณฑ์นี้)\n- **ฟอกไตและไม่มีปัสสาวะ** — ไม่มีไตให้เสียเพิ่ม ไม่ต้องให้สารน้ำ และไม่ต้องฟอกเลือดทันทีหลังฉีด\n- **ผื่นจาก contrast ครั้งก่อน** เป็นเรื่อง hypersensitivity (พิจารณา premedication) ไม่ใช่ CI-AKI",
         "IV fluid ป้องกันเมื่อ eGFR < 30 หรือ AKI", "CI-AKI prophylaxis threshold", ["ACR–NKF consensus 2020 (Davenport MS et al. Radiology 2020)"], ["3.3.20", "2.3.14(3)", "B9.2.7(1)"]),
     mcq(N(11), "A 60-year-old man with type 2 diabetes takes metformin. His eGFR is 55 mL/min/1.73 m² and stable. He needs a contrast-enhanced CT abdomen. What should be done with metformin?",
         ["Stop it 48 hours before and 48 hours after the scan", "Continue it; no need to withhold", "Stop it permanently and start insulin", "Withhold it for one week after the scan", "Give N-acetylcysteine so metformin can be continued"], 1,
         "ACR Manual on Contrast Media: ถ้า **eGFR ≥ 30 และไม่มี AKI → ไม่ต้องหยุด metformin** · หยุดตอนฉีดเฉพาะเมื่อ **eGFR < 30 หรือ AKI** แล้วเริ่มใหม่หลัง 48 ชม. เมื่อไตคงที่\n\nเหตุผลเชิงกลไก: contrast ไม่ได้ทำปฏิกิริยากับ metformin — ความเสี่ยงคือ **ถ้าเกิด AKI** metformin ซึ่งขับทางไตจะสะสมจน **lactic acidosis** ซึ่งเป็นไปได้น้อยมากเมื่อ eGFR 55\n\n- หยุด 48 ชม. ก่อน–หลัง หรือหยุดหนึ่งสัปดาห์ — เป็นคำแนะนำเก่าที่เข้มเกินจำเป็น\n- เปลี่ยนเป็น insulin ถาวร — ไม่มีเหตุผล\n- N-acetylcysteine ไม่ได้ป้องกัน CI-AKI และไม่เกี่ยวกับ metformin",
         "Metformin: eGFR ≥ 30 ไม่ต้องหยุด", "Metformin and iodinated contrast", ["ACR Manual on Contrast Media"], ["3.3.20", "2.3.14(3)"]),
     mcq(N(12), "Which statement about gadolinium-based contrast agents (GBCA) is correct?",
         ["At standard MRI doses, GBCA cause acute kidney injury more often than iodinated contrast", "Macrocyclic agents release free gadolinium more readily than linear agents", "Nephrogenic systemic fibrosis has been linked mainly to group I (linear) agents given to patients with eGFR < 30 or on dialysis", "Nephrogenic systemic fibrosis mainly causes fibrosis of the kidneys", "IV saline before MRI prevents nephrogenic systemic fibrosis"], 2,
         "**NSF** เกิดเมื่อ **Gd³⁺ หลุดจาก chelate** แล้วสะสมในเนื้อเยื่อ — เกิดในผู้ที่ **ขับยาช้า (eGFR < 30 ฟอกไต AKI)** และได้ยา **กลุ่ม I แบบ linear** ซึ่งเสถียรน้อย\n\n- ที่ขนาดยา MRI gadolinium **แทบไม่ทำให้ AKI** — ปัญหาหลักคือ NSF\n- **Macrocyclic เสถียรกว่า** linear (Gd ถูกล็อกในวงปิด)\n- NSF เป็นพังผืดของ **ผิวหนัง ข้อ และอวัยวะ** ไม่ใช่ของไต (ชื่อ \"nephrogenic\" มาจากการเกิดในผู้ป่วยโรคไต)\n- การให้ NSS ป้องกันไม่ได้ เพราะกลไกคือการค้างของยาในร่างกาย ไม่ใช่ hypoxia ของไต",
         "NSF = Gd³⁺ หลุดจาก linear chelate ใน eGFR < 30", "Gadolinium and NSF", ["ACR–NKF consensus on gadolinium 2021 (Weinreb JC et al. Radiology 2021)"], ["3.3.20", "2.3.14(3)", "B9.2.7(2)"]),
    ], nl=["3.3.20", "2.3.14(3)", "B9.2.7(1)", "B9.2.7(2)", "B9.3(4)"], figs=F5, src="แนวทาง ACR–NKF 2020/2021 · ACR Manual on Contrast Media · ESUR 2018 (ไม่อยู่ในสไลด์)")

# ═════════════════════════════════════════════ 6
import random as _rnd
def _speckle(rng, x0, x1, ytop, ybot, xl_top, xr_top, n, cols=("#6a6a6a", "#3c3c3c", "#7c7c7c")):
    o = []
    for _ in range(n):
        y = rng.uniform(ytop + 4, ybot - 4)
        f = (y - ytop) / (ybot - ytop)
        xl = xl_top + (x0 - xl_top) * f; xr = xr_top + (x1 - xr_top) * f
        x = rng.uniform(xl + 3, xr - 3)
        o.append(FC(x, y, rng.choice((0.9, 1.2, 1.6)), rng.choice(cols)))
    return o

def _usbeam():
    rng = _rnd.Random(7)
    o = []
    for j, x in enumerate((6, 214)):
        o.append(film(x, 26, 200, 182, "#0a0a0a"))
        sector = [(x + 80, 44), (x + 120, 44), (x + 194, 204), (x + 6, 204)]
        o.append('<polygon points="%s"%s/>' % (" ".join("%s,%s" % (_n(a), _n(b)) for a, b in sector), _st("#4a4a4a")))
        o += _speckle(rng, x + 6, x + 194, 44, 204, x + 80, x + 120, 90)
        if j == 0:
            o.append(FP("M%s 104 L%s 104 L%s 204 L%s 204 Z" % (_n(x + 76), _n(x + 124), _n(x + 136), _n(x + 64)), "#070707"))
        else:
            o.append(FP("M%s 112 L%s 112 L%s 204 L%s 204 Z" % (_n(x + 74), _n(x + 126), _n(x + 138), _n(x + 62)), "#8a8a8a"))
        o.append(FR(x + 76, 28, 48, 14, "#b9c6c2", 3))
        if j == 0:
            o += [FL(x + 90, 44, x + 90, 96, "#9ecbff", 1.2, "3 3"), FL(x + 100, 44, x + 100, 94, "#9ecbff", 1.2, "3 3"), FL(x + 110, 44, x + 110, 96, "#9ecbff", 1.2, "3 3"),
                  FP("M%s 106 Q%s 88 %s 106" % (_n(x + 74), _n(x + 100), _n(x + 126)), None, METAL, 5)]
            for k, (dx, dy) in enumerate(((-12, 118), (4, 124), (-4, 134), (10, 140), (-10, 148), (2, 156))):
                o.append(FR(x + 100 + dx, dy, 9, 4, "#ff5d5d" if k % 2 else "#5aa7ff", 1))
            o += [TF(x + 100, 186, "เงาดำ (shadow)", "xs b mid"), TF(x + 132, 140, "twinkling", "xs", "#ffd27a")]
        else:
            o += [FL(x + 90, 44, x + 90, 204, "#9ecbff", 1.2, "3 3"), FL(x + 100, 44, x + 100, 204, "#9ecbff", 1.2, "3 3"), FL(x + 110, 44, x + 110, 204, "#9ecbff", 1.2, "3 3"),
                  FC(x + 100, 96, 30, "#030303", "#d6d6d6", 1.6), TF(x + 100, 100, "น้ำ", "xs b mid"),
                  TF(x + 100, 176, "สว่างขึ้น", "xs b mid", "#111111")]
    o += [t(106, 18, "นิ่ว: echo จ้า + เงาดำ", "sm b mid"), t(314, 18, "ถุงน้ำ: ดำ + ใต้ถุงสว่างขึ้น", "sm b mid"),
          t(106, 226, "impedance ต่างมาก → สะท้อนเกือบหมด", "xs mid"), t(106, 242, "เสียงผ่านไปข้างหลังไม่ได้ → เงาดำ", "xs mid"),
          t(106, 258, "Doppler: สีสลับ (twinkling) หลังนิ่ว", "xs mid mu"),
          t(314, 226, "น้ำเนื้อเดียว ไม่มีรอยต่อ → ดำ", "xs mid"), t(314, 242, "เสียงผ่านน้ำแทบไม่ลดลง", "xs mid"),
          t(314, 258, "ใต้ถุงสว่างกว่า (posterior enhancement)", "xs mid mu"),
          t(210, 284, "ก๊าซ (EPN ลำไส้): สะท้อนกลับไปมา → เงาเทาขุ่น “dirty shadowing”", "xs mid i2")]
    return svg(420, 294, "คลื่นเสียงกระทบนิ่วเกิดเงาดำ ส่วนถุงน้ำดำและด้านหลังสว่างขึ้น", *o)

def _usnormal():
    import math
    cx, cy = 210, 118
    o = [film(8, 8, 404, 216, "#0b0b0b"),
         FP("M8 14 Q8 8 14 8 L300 8 Q270 40 200 56 Q120 70 8 60 Z", "#767676"), TF(24, 32, "ตับ (ใช้เทียบ)", "xs b", "#1a1a1a"),
         FE(cx, cy, 120, 52, "#5c5c5c", None, "#d8d8d8", 1.6)]
    for side in (-1, 1):
        for dx in (-62, -21, 21, 62):
            yb = cy + side * 36 * math.sqrt(max(0, 1 - (dx / 112) ** 2))
            ya = cy + side * (19 * math.sqrt(max(0, 1 - (dx / 72) ** 2)) + 3)
            o.append(FP("M%s %s L%s %s L%s %s Z" % (_n(cx + dx - 13), _n(yb), _n(cx + dx + 13), _n(yb), _n(cx + dx), _n(ya)), "#262626"))
    cap_top = cy - 52 * math.sqrt(1 - (60 / 120) ** 2)          # ผิวไตด้านบนที่ x = cx-60
    pyr_base = cy - 36 * math.sqrt(1 - (62 / 112) ** 2)          # ฐาน pyramid ที่ dx -62
    cap_bot = cy + 52 * math.sqrt(1 - (40 / 120) ** 2)           # ผิวไตด้านล่างที่ x = cx+40
    sin_bot = cy + 19 * math.sqrt(1 - (40 / 70) ** 2)            # ขอบ sinus ด้านล่างที่ x = cx+40
    Y = "#e8bb63"
    o += [FE(cx, cy, 70, 19, "#c9c9c9"),
          FL(cx - 60, cap_top, cx - 60, pyr_base, Y, 2), FL(cx - 66, cap_top, cx - 54, cap_top, Y, 1.5), FL(cx - 66, pyr_base, cx - 54, pyr_base, Y, 1.5),
          TF(84, 112, "C 7–10 มม.", "xs b end", "#ffd27a"), FL(86, 106, cx - 64, pyr_base - 2, "#ffd27a", 1),
          FL(cx + 40, cap_bot, cx + 40, sin_bot, Y, 2), FL(cx + 34, cap_bot, cx + 46, cap_bot, Y, 1.5), FL(cx + 34, sin_bot, cx + 46, sin_bot, Y, 1.5),
          TF(cx + 50, 186, "P 15–20 มม.", "xs b", "#ffd27a"),
          FL(90, 198, 330, 198, Y, 2), FL(90, 192, 90, 204, Y, 1.5), FL(330, 192, 330, 204, Y, 1.5),
          TF(210, 217, "L = 10–12 ซม.", "xs b mid", "#ffd27a"),
          TF(cx, cy + 4, "sinus fat", "xs b mid", "#1a1a1a"),
          TF(348, 112, "pyramid", "xs", FT2), FL(346, 108, cx + 66, 98, FT2, 1),
          TF(348, 74, "cortex", "xs", FT2), FL(346, 72, 316, 92, FT2, 1)]
    lad = [("#050505", "ปัสสาวะ/ถุงน้ำ"), ("#262626", "pyramid"), ("#5c5c5c", "cortex"), ("#767676", "ตับ/ม้าม"), ("#c9c9c9", "sinus fat")]
    for i, (c, s) in enumerate(lad):
        x = 15 + i * 80
        o += [FR(x, 236, 70, 16, c, 3, "#8a8a8a", 1), t(x + 35, 268, s, "xs mid")]
    o += [t(15, 286, "มืด (hypo/anechoic)", "xs mu"), t(405, 286, "สว่าง (hyperechoic)", "xs mu end")]
    return svg(420, 294, "ภาพ ultrasound ไตปกติตามแนวยาว พร้อมการวัดความยาว ความหนา cortex และ parenchyma", *o)

F6 = {"usbeam": fig("ทำไมนิ่วมีเงาดำ แต่ถุงน้ำกลับทำให้ด้านหลังสว่างขึ้น",
        "เสียงสะท้อนที่ **รอยต่อของสองสิ่งที่ acoustic impedance (ความหนาแน่น × ความเร็วเสียง) ต่างกัน** — ยิ่งต่างยิ่งสะท้อนมาก · **นิ่ว** ต่างจากเนื้อเยื่อมาก เสียงสะท้อนกลับเกือบหมดที่ผิวหน้า (เส้นโค้งจ้า) และถูกดูดกลืนส่วนที่เหลือ ด้านหลังจึงไม่มีเสียงไปถึง = **posterior acoustic shadow** · นิ่วเล็กที่ไม่มีเงาชัด ใช้ **twinkling artifact** บน color Doppler (สีแดง-น้ำเงินสลับหลังนิ่ว) ช่วยได้ (สไลด์) · **ถุงน้ำ** เป็นน้ำเนื้อเดียวไม่มีรอยต่อภายใน = **anechoic** และน้ำลดทอนเสียงน้อยกว่าเนื้อเยื่อ เครื่องที่ชดเชยการลดทอนตามความลึกจึงแสดงเนื้อเยื่อด้านหลังสว่างเกิน = **posterior enhancement**",
        _usbeam()),
      "usnormal": fig("ไตปกติบน ultrasound — วัดอะไร และอะไรควรสว่างกว่าอะไร",
        "ค่าปกติตามสไลด์ (Hansen 2016): **ความยาว (L) 10–12 ซม.** (สไลด์พิมพ์ mm) · **cortex (C) 7–10 มม.** วัดจากผิวไตถึงฐาน pyramid · **parenchyma (P) 15–20 มม.** วัดจากผิวไตถึง sinus · **cortex ต้องมืดกว่าตับ/ม้ามเล็กน้อย** และต้องเห็น **corticomedullary differentiation** (pyramid มืดกว่า cortex) · sinus ตรงกลางสว่างที่สุดเพราะมี **ไขมัน หลอดเลือด และพังผืด** สร้างรอยต่อจำนวนมาก",
        _usnormal())}

sec("neph-img-06", "Ultrasound ไต — echo ขนาดไต และ corticomedullary differentiation",
    "physics ของ echo · นิ่วมีเงา ถุงน้ำมี posterior enhancement · twinkling · ค่าปกติ L/C/P · ACR: AKI/CKD ใช้ US ก่อน", 9,
"""### ภาษาของ ultrasound (สไลด์)
| คำ | ความหมาย | ตัวอย่างในไต |
|---|---|---|
| **Anechoic** | ไม่มี echo = ดำสนิท | ปัสสาวะใน pelvis ที่ขยาย · simple cyst |
| **Hypoechoic** | echo น้อยกว่าสิ่งรอบข้าง | medullary pyramid · ฝีระยะแรก |
| **Hyperechoic** | echo มากกว่าสิ่งรอบข้าง | renal sinus fat · นิ่ว · ไตเรื้อรังที่เป็นพังผืด · angiomyolipoma |
สไลด์ให้ดู 4 อย่างเสมอ: **ขนาดไต · รูปร่าง · echogenicity · hydronephrosis**

### Physics — echo มาจากไหน
[[fig:usbeam]]
#### ทำไมภาพถึงออกมาแบบนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **จุดจ้า + เงาดำด้านหลัง** | นิ่วมี impedance ต่างจากเนื้อเยื่อมาก → สะท้อน/ดูดกลืนเสียงเกือบหมด | **นิ่ว** (สไลด์: hyperechoic focus with posterior acoustic shadow ใน upper pole calyx) · หินปูนในเนื้อไต |
| **Twinkling artifact** | ผิวนิ่วขรุขระเป็นผลึก ทำให้สัญญาณ Doppler แกว่ง → สีสลับเร็วหลังวัตถุ | ช่วยยืนยัน **นิ่วเล็ก** ที่ไม่มีเงาชัด (สไลด์) |
| **ก้อนดำสนิท ผนังบาง + ด้านหลังสว่าง** | น้ำไม่มีรอยต่อภายใน และลดทอนเสียงน้อย | **simple cyst** · ปัสสาวะใน hydronephrosis |
| **ก้อนดำปนเทา มี debris + ด้านหลังสว่าง** | ของเหลวข้น (หนอง เลือด) มีอนุภาคสะท้อนบ้าง | **ฝีในไต** (สไลด์ case 02) · ถุงน้ำมีเลือดออก |
| **จุดจ้า + เงาเทาขุ่นอยู่ด้านบน (non-dependent)** | ก๊าซสะท้อนหมดแล้วสะท้อนกลับไปมา (reverberation) · ก๊าซลอยขึ้นด้านบน | **emphysematous pyelonephritis** (สไลด์: dirty shadowing) |
| **ทั้งไตสว่างกว่าตับ** | พังผืดและ collagen ในเนื้อไตเพิ่มรอยต่อ | **โรคไตเรื้อรัง** (และโรคเนื้อไตเฉียบพลันบางชนิด) |

### ไตปกติ — ค่าที่ต้องจำ (สไลด์ · Hansen 2016)
[[fig:usnormal]]
| สิ่งที่วัด | ค่าปกติ | ทำไมสำคัญ |
|---|---|---|
| **ความยาว (L)** | **10–12 ซม.** (สไลด์พิมพ์ "mm" — ที่ถูกคือ ซม.) | ไตเล็กสนับสนุน CKD · สองข้างต่างกันมาก คิดถึง renal artery stenosis หรือแผลเป็น |
| **Cortical thickness (C)** | **7–10 มม.** | บางลงเมื่อ nephron หายไป |
| **Parenchymal thickness (P)** | **15–20 มม.** | |
| **Echogenicity** | **cortex มืดกว่าตับและม้ามเล็กน้อย** | cortex สว่างเท่าหรือมากกว่าตับ = ผิดปกติ |
| **Corticomedullary differentiation** | **ต้องเห็น** (pyramid มืดกว่า cortex) | หายไปใน CKD (เนื้อไตกลายเป็นเนื้อเดียว) |
ความเชื่อมโยงกับกายวิภาค: cortex มี glomeruli และ tubule ที่ขดไปมา (รอยต่อพอประมาณ) · pyramid มี collecting duct และ loop ที่เรียงขนาน มีน้ำมาก (รอยต่อน้อย → มืด) · sinus มีไขมัน หลอดเลือด พังผืด (รอยต่อมาก → สว่างที่สุด)

### ข้อดี–ข้อจำกัด
- **ไม่มีรังสี ไม่ฉีดสี ทำข้างเตียงได้ ซ้ำได้** → ตรวจแรกใน **AKI/CKD** หญิงตั้งครรภ์ และเด็ก
- **ขึ้นกับผู้ตรวจ** · ท่อไตช่วงกลางถูกลมในลำไส้บัง → หานิ่วท่อไตไม่ไวเท่า CT (แต่เห็น **hydronephrosis** ซึ่งเป็นหลักฐานทางอ้อม)
- Doppler: twinkling (นิ่ว) · ureteric jet ในกระเพาะปัสสาวะ (ไม่มี jet ข้างหนึ่ง สนับสนุนการอุดกั้น)

### ACR — ultrasound (สไลด์)
| ข้อบ่งชี้ | ความเหมาะสม |
|---|---|
| สงสัยนิ่ว | May be appropriate |
| Microscopic hematuria | Usually not appropriate |
| **AKI/CKD** | **Usually APPROPRIATE** |
| Acute pyelonephritis | May be appropriate in complicated case |
""",
    ["Anechoic = น้ำใส · hypoechoic = pyramid · hyperechoic = sinus fat นิ่ว พังผืด",
     "นิ่ว: hyperechoic + posterior acoustic shadow · นิ่วเล็ก: twinkling artifact",
     "ถุงน้ำ: anechoic ผนังบาง + posterior enhancement",
     "ไตปกติ: L 10–12 ซม. · cortex 7–10 มม. · parenchyma 15–20 มม. · cortex มืดกว่าตับ · มี CMD",
     "ACR: AKI/CKD → ultrasound usually appropriate"],
    [mcq(N(13), "In a normal adult kidney on grey-scale ultrasound, which structure is the most echogenic (brightest)?",
         ["Renal cortex", "Medullary pyramids", "Renal sinus (central echo complex)", "Urine in a mildly distended renal pelvis", "A simple cortical cyst"], 2,
         "**Renal sinus** มีไขมัน หลอดเลือด และพังผืดปนกัน สร้าง **รอยต่อจำนวนมาก** จึงสะท้อนเสียงมากที่สุด (hyperechoic)\n\n- **Cortex** — echo ปานกลาง ปกติ **มืดกว่าตับ/ม้ามเล็กน้อย**\n- **Pyramid** — มีท่อเรียงขนานและน้ำมาก → **hypoechoic** (มืดกว่า cortex)\n- **ปัสสาวะ** และ **simple cyst** — น้ำเนื้อเดียว **anechoic** (ดำสนิท)",
         "sinus fat สว่างที่สุด", "Normal renal echogenicity", REF("Ultrasonography of KUB — echogenicity"), ["B9.1.1(1)"]),
     mcq(N(14), "On renal ultrasound, a round anechoic lesion with an imperceptible wall shows increased brightness of the tissue directly behind it. What is the physical basis of this 'posterior acoustic enhancement'?",
         ["The lesion contains calcium that reflects sound", "Fluid attenuates sound less than surrounding tissue, so more energy reaches the tissue behind it", "Doppler signal from flowing blood in the cyst", "Gas bubbles causing reverberation", "The lesion is hypervascular and enhances like contrast on CT"], 1,
         "น้ำ **ลดทอน (attenuate) เสียงน้อยกว่าเนื้อเยื่อ** — เครื่อง ultrasound ชดเชยการลดทอนตามความลึกโดยสมมติว่าทุกอย่างเป็นเนื้อเยื่อ เนื้อเยื่อด้านหลังถุงน้ำจึงได้รับพลังงานมากกว่าที่เครื่องคาด และแสดง **สว่างเกิน** = posterior enhancement (สไลด์: renal abscess มี posterior enhancement เพราะเป็นของเหลว)\n\n- **แคลเซียม** ให้ผลตรงข้าม — สะท้อนหมดจนเกิด **เงาดำ**\n- **Doppler** ไม่เกี่ยวกับความสว่างของภาพ grey-scale\n- **ก๊าซ** ให้ dirty shadowing ไม่ใช่ enhancement\n- คำว่า \"enhancement\" ใน ultrasound **ไม่ใช่การรับสี** เหมือน CT",
         "ด้านหลังสว่าง = ของเหลว", "Posterior acoustic enhancement", REF("Ultrasonography of KUB; Renal abscess — posterior enhancement"), ["B9.1.1(1)", "B9.2.1-3(1)"]),
     mcq(N(15), "A 4-mm echogenic focus in a lower-pole calyx shows no definite acoustic shadow on grey-scale ultrasound, but colour Doppler shows a rapidly alternating red-blue signal immediately behind it. This finding is best explained by:",
         ["A small renal stone (twinkling artefact)", "An arteriovenous malformation", "Renal vein thrombosis", "A hypervascular renal cell carcinoma", "Normal ureteric jet"], 0,
         "**Twinkling artefact** = สัญญาณสีสลับเร็วบน color Doppler หลังวัตถุผิวขรุขระแข็งอย่าง **นิ่ว** ช่วยยืนยันนิ่วเล็กที่ไม่มีเงาชัด (สไลด์)\n\n- **AVM** — มีการไหลจริงเป็นกลุ่มหลอดเลือด สเปกตรัมเป็นคลื่นของเลือด และไม่อยู่ใน calyx เป็นจุดจ้า\n- **Renal vein thrombosis** — ไม่มีการไหลในหลอดเลือดดำ ไตบวม ไม่ใช่จุดจ้าใน calyx\n- **RCC** — เป็นก้อนเนื้อในเนื้อไต ไม่ใช่จุดจ้า 4 มม. ใน calyx\n- **Ureteric jet** — เห็นในกระเพาะปัสสาวะ ไม่ใช่ในไต",
         "Twinkling = นิ่ว", "Twinkling artefact", REF("Ultrasonography of kidney stone — twinkle artifact"), ["B9.2.3-3(1)", "2.3.14-3(15)"]),
    ], nl=["B9.1.1(1)", "2.3.14(3)", "B9.2.3-3(1)", "2.3.14-3(15)"], figs=F6)

# ═════════════════════════════════════════════ 7
def _renogram():
    X = lambda m: 56 + m * 11.4
    Y = lambda v: 238 - v * 158
    o = [line(56, 238, 404, 238, "ln"), line(56, 238, 56, 70, "ln"),
         g(t(0, 0, "รังสีในไต (counts)", "xs mid mu"), tr="translate(30 156) rotate(-90)")]
    for m in (0, 5, 10, 15, 20, 25, 30):
        o += [line(X(m), 238, X(m), 242, "ln"), t(X(m), 255, str(m), "xs mid mu")]
    o += [t(404, 272, "เวลา (นาที)", "xs end mu")]
    leg = [("lok w3", "ปกติ", 14), ("lwa w3", "ขยายแต่ไม่อุดกั้น", 112), ("lbad w3", "อุดกั้นจริง", 290)]
    for c, s, x in leg:
        o += [line(x, 20, x + 22, 20, c), t(x + 28, 24, s, "xs b")]
    o += [line(X(20), 74, X(20), 238, "lms da"), t(X(20), 66, "ฉีด furosemide", "xs b mid tms")]
    curves = [("lok w3", [(0, 0), (1, .55), (2, .86), (3, 1.0), (4, .97), (6, .82), (10, .55), (15, .35), (20, .25), (25, .18), (30, .14)]),
              ("lwa w3", [(0, 0), (2, .38), (5, .6), (10, .76), (15, .84), (20, .87), (21, .78), (22, .6), (24, .4), (27, .26), (30, .2)]),
              ("lbad w3", [(0, 0), (2, .33), (5, .5), (10, .66), (15, .76), (20, .83), (22, .86), (25, .89), (30, .92)])]
    for c, pts in curves:
        o.append(poly([(X(a), Y(b)) for a, b in pts], c))
    o += [t(X(3) + 8, Y(1.0) - 2, "ยอด 3–5 นาที", "xs tok"), t(X(8), 200, "ไหลออกเอง", "xs tok"),
          t(X(23) + 8, 150, "ล้างออกเร็ว", "xs b twa"), t(X(26), Y(.9) - 10, "ไม่ลดลง", "xs b mid tbad")]
    o += [t(8, 292, "T½ หลังฉีด furosemide: < 10 นาที = ไม่อุดกั้น · 10–20 = ก้ำกึ่ง · > 20 = อุดกั้น", "xs i2")]
    return svg(420, 300, "กราฟ diuretic renogram ปกติ อุดกั้น และขยายแต่ไม่อุดกั้น", *o)

def _tracer():
    o = [line(8, 100, 52, 100, "lbad w3"), t(8, 90, "เลือด", "xs mu"),
         circ(86, 100, 34, "bx"), circ(86, 100, 25, "bad"), t(52, 152, "glomerulus", "xs mid mu"),
         rect(124, 74, 206, 16, "ac", 2), rect(124, 110, 206, 16, "ac", 2), rect(124, 90, 206, 20, "wa", 0),
         t(227, 66, "เซลล์ proximal tubule", "xs mid mu"),
         path("M100 128 C110 150 116 154 132 154", "lbad w3"), rect(124, 146, 206, 16, "bad", 6), t(227, 178, "peritubular capillary (เลือด)", "xs mid mu"),
         ar(330, 100, 364, 100, "lwa w2", "ah-wa"), t(368, 104, "ปัสสาวะ", "xs")]
    for (x, y) in ((20, 100), (34, 100), (78, 94), (94, 94), (86, 108)):
        o.append(circ(x, y, 3.2, "waf"))
    for x in (144, 184, 224, 266, 306):
        o.append(circ(x, 100, 3.2, "waf"))
    o += [ar(112, 100, 130, 100, "lwa", "ah-wa")]
    for x in (238, 278, 314):
        o.append(poly([(x, 150), (x + 4, 154), (x, 158), (x - 4, 154)], "acf", closed=True))
    o += [ar(258, 146, 258, 106, "lac w2", "ah-ac"), t(264, 138, "หลั่ง", "xs b tac"),
          poly([(204, 96), (208, 100), (204, 104), (200, 100)], "acf", closed=True)]
    for x in (150, 196, 242, 288):
        o.append(rect(x - 3.5, 78, 7, 7, "msf", 1))
    o += [t(336, 84, "ค้างในเซลล์", "xs b tms")]
    leg = [("waf", "DTPA — กรองที่ glomerulus อย่างเดียว → วัด GFR · dynamic renogram"),
           ("acf", "MAG3 — หลั่งที่ proximal tubule → renogram ชัดแม้ไตทำงานน้อย"),
           ("msf", "DMSA — จับค้างในเซลล์ cortex → ภาพนิ่ง: แผลเป็น การทำงานแยกข้าง")]
    for i, (c, s) in enumerate(leg):
        y = 206 + i * 18
        if c == "waf": o.append(circ(18, y - 4, 4, c))
        elif c == "acf": o.append(poly([(18, y - 9), (23, y - 4), (18, y + 1), (13, y - 4)], c, closed=True))
        else: o.append(rect(14, y - 8, 8, 8, c, 1))
        o.append(t(30, y, s, "xs"))
    return svg(420, 254, "เส้นทางของยาติดรังสี DTPA MAG3 และ DMSA ใน nephron", *o)

F7 = {"tracer": fig("ยาติดรังสีแต่ละตัวไปทางไหนใน nephron — จึงวัดคนละอย่าง",
        "**DTPA** ถูกกรองที่ glomerulus เหมือน inulin ไม่ถูกหลั่งหรือดูดกลับ → ใช้ **วัด GFR** และทำ renogram · **MAG3** จับโปรตีนในเลือด ถูก **หลั่งที่ proximal tubule** (สัดส่วนที่ไตดึงออกจากเลือดต่อรอบสูงกว่า DTPA) → ภาพชัดแม้ไตทำงานลดลง จึงเป็นยามาตรฐานของ **diuretic renogram** · **DMSA** ถูกเซลล์ proximal tubule ใน cortex **จับไว้นาน** → ได้ภาพนิ่งของเนื้อไตที่ยังทำงาน เห็น **แผลเป็น** และบอก **การทำงานแยกข้าง** (ไม่อยู่ในสไลด์ — ตำราเวชศาสตร์นิวเคลียร์)",
        _tracer()),
      "renogram": fig("Diuretic renogram — แยก “ขยายเฉย ๆ” จาก “อุดกั้นจริง”",
        "กราฟคือปริมาณรังสีในไตตามเวลา · **ปกติ** (เขียว): ขึ้นถึงยอดใน 3–5 นาที แล้วลดลงเองเพราะปัสสาวะไหลออก · **ระบบขยายแต่ไม่อุดกั้น** (ฟ้า): pelvis ที่ใหญ่เป็น **อ่างเก็บ** ยาจึงค้างดูเหมือนอุดกั้น แต่เมื่อฉีด **furosemide** ปัสสาวะไหลแรงขึ้นจะ **ล้างออกเร็ว** · **อุดกั้นจริง** (แดง): มีแรงต้านคงที่ ยาไหลออกไม่ได้แม้ปัสสาวะมากขึ้น กราฟ **ขึ้นต่อหรือคงที่** · นี่คือวิธีพิสูจน์ \"nonobstructive hydronephrosis\" ที่สไลด์เตือนไว้ (ไม่อยู่ในสไลด์ — ตำราเวชศาสตร์นิวเคลียร์)",
        _renogram())}

sec("neph-img-07", "Nuclear imaging — วัด “การทำงาน” แทน “รูปร่าง”",
    "DTPA · MAG3 · DMSA · diuretic renogram แยกขยายเฉย ๆ จากอุดกั้นจริง · split function · captopril renography", 8,
"""> สไลด์มีหัวข้อ **Nuclear Imaging** ใน outline แต่ **handout ไม่มีหน้าเนื้อหา** — หัวข้อนี้เรียบเรียงจากตำราเวชศาสตร์นิวเคลียร์มาตรฐาน

### ยาติดรังสี 3 ตัวที่ต้องรู้
[[fig:tracer]]
| ยา (Tc-99m) | ไตจัดการยาอย่างไร | วัด/ให้ภาพอะไร | ใช้เมื่อ |
|---|---|---|---|
| **DTPA** | **กรองที่ glomerulus อย่างเดียว** | **GFR** (รวมและแยกข้าง) · dynamic renogram | วัด GFR · split function · obstruction เมื่อไตทำงานดี |
| **MAG3** | จับโปรตีน **หลั่งที่ proximal tubule** (+ กรองเล็กน้อย) — สะท้อน effective renal plasma flow | dynamic renogram ภาพชัด | **diuretic renogram** · ไตทำงานลด · ทารก · ไตปลูกถ่าย |
| **DMSA** | **จับค้างในเซลล์ proximal tubule ของ cortex** | ภาพนิ่งของเนื้อไตที่ทำงาน | **แผลเป็นหลังกรวยไตอักเสบ** (โดยเฉพาะเด็กที่มี VUR) · การทำงานแยกข้าง · ไตผิดที่ |
**Split (differential) function** ปกติแต่ละข้าง **45–55%** — ช่วยตัดสินใจ เช่น ไตข้างที่อุดกั้นนานยังเหลือการทำงานพอให้ผ่าตัดแก้ หรือควรตัดทิ้ง

### Diuretic renogram (MAG3/DTPA + furosemide)
[[fig:renogram]]
#### ทำไมภาพถึงออกมาแบบนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ยอดกราฟที่ 3–5 นาทีแล้วลดลงเอง** | ยาเข้าไต (perfusion → uptake) แล้วถูกขับลงท่อและไหลออก | ไตปกติ ไม่อุดกั้น |
| **กราฟค้าง แต่ลดเร็วหลัง furosemide (T½ < 10 นาที)** | pelvis ที่ใหญ่เป็นอ่างเก็บ (reservoir) ยาจึงค้างเพราะปริมาตร ไม่ใช่เพราะท่อตัน · ปัสสาวะไหลแรงขึ้นจึงล้างออกได้ | **ขยายแต่ไม่อุดกั้น** — ไม่ต้องผ่าตัด |
| **กราฟขึ้นต่อแม้ได้ furosemide (T½ > 20 นาที)** | แรงต้านคงที่ที่จุดตีบ ยาออกไม่ได้แม้ปัสสาวะเพิ่ม | **อุดกั้นจริง** เช่น PUJ obstruction |
| **ยาเข้าไตช้าและน้อยทั้งข้าง** | ไตข้างนั้นทำงานน้อย (GFR ต่ำ) — furosemide อาจกระตุ้นปัสสาวะไม่พอ | แปลผลยาก ต้องดู split function ประกอบ |

### Captopril renography — ไม่ค่อยใช้แล้ว แต่สอนกลไกได้ดี
ใน **renal artery stenosis** ไตข้างที่ตีบรักษา GFR ไว้ด้วย **angiotensin II บีบ efferent arteriole** → ให้ captopril (ACEi) ตัดกลไกนี้ → **GFR ของข้างที่ตีบลดลง** ยาเข้าไตช้าและค้างใน cortex · ปัจจุบันนิยม **duplex ultrasound, CTA หรือ MRA** มากกว่า (ความไวของ captopril scan ลดลงในผู้ป่วยที่ไตเสื่อมแล้ว)
""",
    ["DTPA = กรองอย่างเดียว → GFR · MAG3 = หลั่งที่ proximal tubule → renogram · DMSA = จับค้างใน cortex → แผลเป็น",
     "Split function ปกติ 45–55% ต่อข้าง",
     "Diuretic renogram: T½ < 10 นาที ไม่อุดกั้น · 10–20 ก้ำกึ่ง · > 20 อุดกั้น",
     "Hydronephrosis ไม่เท่ากับ obstruction เสมอ — พิสูจน์ด้วย diuretic renogram",
     "Captopril renogram: ACEi ตัด AngII ที่ efferent → GFR ข้างที่ตีบลด"],
    [mcq(N(16), "A 24-year-old man has incidental moderate left hydronephrosis on ultrasound with normal renal function. A MAG3 renogram shows tracer pooling in the dilated left pelvis, but after IV furosemide the tracer clears rapidly with a half-time of 6 minutes. What is the best interpretation?",
         ["High-grade left pelviureteric junction obstruction", "Dilated but non-obstructed left collecting system", "Left renal artery stenosis", "Non-functioning left kidney", "Left vesicoureteric reflux grade V"], 1,
         "pelvis ที่ขยายเป็น **อ่างเก็บ** ทำให้ยาค้างในช่วงแรก แต่เมื่อปัสสาวะไหลแรงขึ้นจาก furosemide ยา **ล้างออกเร็ว (T½ < 10 นาที)** = **ไม่มีการอุดกั้น** — เป็น nonobstructive hydronephrosis ที่สไลด์เตือนไว้\n\n- **PUJ obstruction** — T½ > 20 นาที กราฟขึ้นต่อแม้ได้ยา\n- **Renal artery stenosis** — ยาเข้าไตช้า/น้อย ไม่ใช่ค้างใน pelvis แล้วล้างออกดี\n- **ไตไม่ทำงาน** — แทบไม่มียาเข้าไตเลย\n- **VUR** — ต้องวินิจฉัยด้วย voiding cystourethrogram ไม่ใช่ diuretic renogram",
         "ล้างออกเร็วหลัง furosemide = ไม่อุดกั้น", "Diuretic renogram", ["ตำราเวชศาสตร์นิวเคลียร์ (ไม่อยู่ในสไลด์)"], ["2.3.14-3(9)", "B9.1.2(2)"]),
     mcq(N(17), "A 5-year-old girl recovered from a febrile urinary tract infection 6 months ago. Which nuclear medicine study is best for detecting renal cortical scarring?",
         ["Tc-99m DTPA dynamic renogram", "Tc-99m DMSA static cortical scan", "Captopril renography", "Gallium-67 scan", "Tc-99m MAG3 diuretic renogram"], 1,
         "**DMSA** ถูกเซลล์ proximal tubule ใน **cortex จับไว้นาน** ได้ภาพนิ่งของเนื้อไตที่ยังทำงาน — บริเวณ **แผลเป็นจะไม่รับยา** (photopenic defect) จึงเป็นการตรวจมาตรฐานหาแผลเป็นหลังกรวยไตอักเสบ\n\n- **DTPA/MAG3 renogram** — ดู GFR การไหลและการระบาย ภาพ cortex ไม่ละเอียดพอหาแผลเป็น\n- **Captopril renography** — หา renal artery stenosis\n- **Gallium-67** — หาการอักเสบ/ติดเชื้อ ไม่ใช่แผลเป็นเรื้อรัง",
         "แผลเป็นในไต = DMSA", "DMSA scan", ["ตำราเวชศาสตร์นิวเคลียร์ (ไม่อยู่ในสไลด์)"], ["2.3.14(14)", "B9.2.2(2)"]),
    ], nl=["B9.3(4)", "B9.1.2(2)", "2.3.14-3(9)", "2.3.14-3(13)", "B9.2.6-3(1)"], figs=F7, src="ตำราเวชศาสตร์นิวเคลียร์มาตรฐาน (สไลด์มีแค่หัวข้อใน outline)")

# ═════════════════════════════════════════════ 8
def _acr():
    cols = ["Plain KUB", "IVP", "Ultrasound", "CT"]
    rows = [("สงสัยนิ่ว", "ปวดสีข้าง", [("ms", "อาจใช้", "CT ดีกว่า"), ("bad", "ไม่ควร", ""), ("ms", "อาจใช้", ""), ("ok", "ควรทำ", "ไม่ฉีดสี")]),
            ("Microscopic", "hematuria", [("bad", "ไม่ควร", ""), ("bad", "ไม่ควร", ""), ("bad", "ไม่ควร", ""), ("ms", "อาจใช้", "CTU")]),
            ("AKI / CKD", "", [("bad", "ไม่ควร", ""), ("bad", "ไม่ควร", ""), ("ok", "ควรทำ", "ตรวจแรก"), ("ms", "อาจใช้", "ไม่ฉีดสี")]),
            ("APN", "ไม่ซับซ้อน", [("bad", "ไม่ควร", ""), ("bad", "ไม่ควร", ""), ("bad", "ไม่ควร", ""), ("bad", "ไม่ควร", "")]),
            ("APN", "ซับซ้อน/ไม่ตอบยา", [("bad", "ไม่ควร", ""), ("bad", "ไม่ควร", ""), ("ms", "อาจใช้", ""), ("ok", "ควรทำ", "ฉีดสี")])]
    o = []
    for j, c in enumerate(cols):
        o.append(t(164 + j * 72, 26, c, "xs b mid"))
    for i, (a, b, cells) in enumerate(rows):
        y = 36 + i * 48
        o += [t(10, y + 20, a, "sm b"), t(10, y + 36, b, "xs mu") if b else ""]
        for j, (cl, s1, s2) in enumerate(cells):
            x = 130 + j * 72
            tc = {"ok": "tok", "ms": "tms", "bad": "tbad"}[cl]
            o += [rect(x, y, 68, 44, cl, 6), t(x + 34, y + (20 if s2 else 27), s1, "xs b mid " + tc)]
            if s2: o.append(t(x + 34, y + 36, s2, "xs mid i2"))
    o += [rect(10, 284, 14, 12, "ok", 3), t(30, 294, "Usually appropriate (7–9)", "xs"),
          rect(180, 284, 14, 12, "ms", 3), t(200, 294, "May be (4–6)", "xs"),
          rect(292, 284, 14, 12, "bad", 3), t(312, 294, "Usually not (1–3)", "xs")]
    return svg(420, 302, "ตาราง ACR Appropriateness Criteria สรุปจากสไลด์ แยกตามสถานการณ์และการตรวจ", *o)

def _hema():
    o = [box(110, 6, 200, 30, "bx", "Dipstick: blood บวก", "b", 8, 12),
         ar(210, 36, 210, 50, "lmu", "ah-mu"),
         box(70, 52, 260, 34, "wa", "ส่องกล้อง: RBC ≥ 3 /HPF ?", "b", 8, 12),
         ar(330, 69, 350, 69, "lmu", "ah-mu"), box(352, 52, 62, 34, "sk", "ไม่มี RBC", "", 6, 11),
         t(383, 104, "Hb หรือ", "xs mid mu"), t(383, 119, "myoglobin", "xs mid mu"),
         ar(200, 86, 200, 100, "lmu", "ah-mu"),
         box(30, 102, 310, 38, "bx", "ตัดเหตุชั่วคราว: UTI ประจำเดือน ออกกำลังหนัก\nบาดเจ็บ → รักษาแล้วตรวจซ้ำ", "", 8, 11),
         ar(150, 140, 106, 158, "lmu", "ah-mu"), ar(240, 140, 300, 158, "lmu", "ah-mu"),
         rect(8, 160, 196, 98, "ac", 8), t(106, 180, "Glomerular", "sm b mid tac"),
         t(106, 198, "dysmorphic RBC / acanthocyte", "xs mid"), t(106, 214, "RBC cast · proteinuria · Cr ↑", "xs mid"),
         t(106, 234, "→ nephrology ± biopsy", "xs b mid"), t(106, 250, "(ไม่ต้อง CTU/cystoscopy)", "xs mid mu"),
         box(214, 160, 198, 52, "ms", "Non-glomerular\nแบ่งความเสี่ยง (AUA 2020)", "b", 8, 11.5),
         ar(250, 212, 250, 230, "lmu", "ah-mu"), ar(313, 212, 313, 230, "lmu", "ah-mu"), ar(376, 212, 376, 230, "lmu", "ah-mu")]
    risk = [("ok", "ต่ำ", "UA ซ้ำ\nใน 6 เดือน"), ("ms", "กลาง", "cystoscopy\n+ US ไต"), ("bad", "สูง/gross", "cystoscopy\n+ CTU")]
    for k, (c, h, s) in enumerate(risk):
        x = 218 + k * 64
        o += [rect(x, 232, 60, 74, c, 6), t(x + 30, 250, h, "xs b mid"), t(x + 30, 272, s, "xs mid", 1.35)]
    o += [t(8, 280, "เสี่ยงสูง: อายุ ≥ 60 ปี · สูบ > 30 pack-years", "xs mu"), t(8, 296, "RBC > 25/HPF · เคยปัสสาวะเป็นเลือด", "xs mu")]
    return svg(420, 314, "แผนผังการประเมินปัสสาวะเป็นเลือดและการเลือกภาพตามความเสี่ยง", *o)
F8 = {"acr": fig("How to CHOOSE — ตาราง ACR ของสไลด์รวมไว้ในภาพเดียว",
        "อ่านตามแถว: **สงสัยนิ่ว → CT ไม่ฉีดสี** · **microscopic hematuria → CTU (may be)** · **AKI/CKD → ultrasound** · **APN ไม่ซับซ้อนไม่ต้องตรวจภาพ** · **APN ซับซ้อนหรือไม่ตอบยา → CT ฉีดสี** (US เป็นทางเลือก) · **IVP ไม่ควรในทุกสถานการณ์** · ทุกช่องมาจากตาราง ACR ในสไลด์ของแต่ละ modality (ช่อง KUB ของ APN ซับซ้อนใช้แถว acute pyelonephritis ของสไลด์ plain radiograph)",
        _acr()),
      "hema": fig("ปัสสาวะเป็นเลือด — แยกต้นทางก่อน แล้วค่อยเลือกภาพ",
        "ขั้นแรกยืนยันว่ามี **RBC จริง** (dipstick บวกได้จาก hemoglobin หรือ myoglobin) · ตัดเหตุชั่วคราว · แล้วแยก **glomerular** (ส่งนักไต ไม่ต้อง CTU) กับ **non-glomerular** · กลุ่ม non-glomerular แบ่งความเสี่ยงมะเร็ง urothelium ตาม **AUA/SUFU 2020 (ปรับ 2025)** เพื่อเลือกระหว่างตรวจซ้ำ ultrasound หรือ CT urography ร่วมกับ cystoscopy (ไม่อยู่ในสไลด์ — สไลด์มีแค่แถว ACR microscopic hematuria)",
        _hema())}

sec("neph-img-08", "How to CHOOSE — เลือกการตรวจตามคำถาม และปัสสาวะเป็นเลือด",
    "ตาราง ACR รวมทุก modality · ตั้งครรภ์ · ปัสสาวะเป็นเลือด: กลไก glomerular vs non-glomerular · AUA risk strata", 10,
"""### หลักเลือกการตรวจ — C-H-O-O-S-E
สไลด์ไม่ได้ขยายตัวย่อ C-H-O-O-S-E แต่ทุก modality จบด้วยตาราง ACR ชุดเดียวกัน หลักคิดที่ได้จากตารางเหล่านั้นคือ
1. **ตั้งคำถามทางคลินิกก่อน** — หานิ่ว? อุดกั้น? แยก AKI/CKD? หาฝี/ก๊าซ? หามะเร็ง? วัดการทำงาน?
2. **เลือกการตรวจที่ตอบคำถามนั้นได้แม่นที่สุดด้วยความเสี่ยงน้อยที่สุด** — รังสี · สารทึบรังสีกับไต · ตั้งครรภ์
3. **ผลต้องเปลี่ยนการรักษา** — APN ที่ตอบยาดีไม่ต้องตรวจภาพ

[[fig:acr]]
| คำถาม | ตรวจแรก | ทำไม |
|---|---|---|
| **ปวดสีข้าง สงสัยนิ่ว** | **CT KUB ไม่ฉีดสี (low-dose)** | sens 97% spec 95% · เห็นภาวะแทรกซ้อนและโรคอื่น (เช่น AAA) |
| **AKI/CKD ไม่ทราบสาเหตุ** | **Ultrasound** | ไม่มีรังสี ไม่ฉีดสี · บอกขนาดไต (เฉียบพลันหรือเรื้อรัง) และ hydronephrosis (postrenal) |
| **APN ไม่ซับซ้อน** | **ไม่ต้องตรวจภาพ** | วินิจฉัยทางคลินิก + UA + เพาะเชื้อ |
| **APN ซับซ้อน / ไข้ไม่ลง 72 ชม.** | **CT ฉีดสี** (US ถ้าไตไม่ดี/ตั้งครรภ์) | หาฝี ก๊าซ การอุดกั้น |
| **Microscopic hematuria ความเสี่ยงสูง / gross** | **CT urography + cystoscopy** | CTU เห็นทางเดินปัสสาวะส่วนบน · cystoscopy เห็นกระเพาะปัสสาวะ |
| **ขยายแต่ไม่แน่ใจว่าอุดกั้น** | **Diuretic renogram** | แยกอ่างเก็บจากแรงต้าน |
| **ตั้งครรภ์ ปวดสีข้าง** | **Ultrasound** → MRI ไม่ฉีด gadolinium → low-dose CT ถ้าจำเป็น | เลี่ยงรังสี (ไม่อยู่ในสไลด์ — ACR) · ระวังไตขวาขยายตามสรีรวิทยาการตั้งครรภ์ |

### ปัสสาวะเป็นเลือด
[[fig:hema]]
#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **RBC รูปร่างผิดปกติ (dysmorphic, acanthocyte)** | RBC เบียดผ่านรอยรั่วของ GBM แล้วผ่าน tubule ที่ osmolality และ pH เปลี่ยนไปมา เยื่อหุ้มเซลล์เสียรูป | **glomerular** — ส่งนักไต |
| **RBC cast** | RBC ที่หลุดจาก glomerulus ถูกห่อด้วย Tamm–Horsfall protein ใน distal tubule เป็นแท่ง | glomerulonephritis (เฉพาะเจาะจงมาก) |
| **ปัสสาวะสีโคล่า/น้ำล้างเนื้อ ไม่มีลิ่มเลือด** | hemoglobin เปลี่ยนสีในปัสสาวะที่เป็นกรดระหว่างทางยาวจาก glomerulus · tubule มี urokinase ลิ่มเลือดจึงไม่ค่อยเกิด | glomerular |
| **เลือดสดแดง มีลิ่มเลือด RBC รูปร่างปกติ** | เลือดออกโดยตรงในระบบรวบรวมปัสสาวะหรือกระเพาะ ไม่ผ่าน tubule | **non-glomerular** — นิ่ว เนื้องอก ติดเชื้อ บาดเจ็บ |
| **ลิ่มเลือดเป็นเส้นยาวคล้ายหนอน** | เลือดแข็งตัวในท่อไตเป็นรูปท่อ | ต้นทางอยู่ **ทางเดินปัสสาวะส่วนบน** |
| **เลือดออกไม่เจ็บ เป็น ๆ หาย ๆ ในผู้สูงอายุสูบบุหรี่** | หลอดเลือดใหม่ของเนื้องอกเปราะ แตกเป็นครั้งคราว ไม่มีการอุดกั้นจึงไม่เจ็บ | **มะเร็ง urothelium จนกว่าจะพิสูจน์ได้ว่าไม่ใช่** — อย่าวางใจเมื่อเลือดหยุดเอง |
| **ปัสสาวะเป็นเลือด + ปวด colic** | นิ่วครูดเยื่อบุ urothelium ขณะถูกบีบไล่ | นิ่ว (หัวข้อถัดไป) |

#### การเลือกภาพใน microhematuria — สไลด์ (ACR) เทียบ AUA/SUFU 2020 (ปรับ 2025)
| แหล่ง | Ultrasound | CT urography |
|---|---|---|
| **สไลด์ (ACR)** | Usually not appropriate | May be appropriate |
| **AUA/SUFU** | ความเสี่ยง **กลาง** → **US ไต + cystoscopy** | ความเสี่ยง **สูง** → **CTU + cystoscopy** · ความเสี่ยง **ต่ำ** → ตรวจ UA ซ้ำใน 6 เดือน (หรือ cystoscopy + US ตามการตัดสินใจร่วม) |
**กลุ่มความเสี่ยง AUA/SUFU** (ย่อ) — **ต่ำ**: หญิง < 50 ปี ชาย < 40 ปี ไม่สูบหรือ < 10 pack-years RBC 3–10/HPF ครั้งเดียว · **กลาง**: หญิง 50–59 ชาย 40–59 ปี 10–30 pack-years RBC 11–25/HPF · **สูง**: อายุ ≥ 60 ปี > 30 pack-years RBC > 25/HPF หรือเคยมี gross hematuria
""",
    ["สงสัยนิ่ว → CT ไม่ฉีดสี · AKI/CKD → US · APN ไม่ซับซ้อนไม่ต้องตรวจภาพ · APN ซับซ้อน → CT ฉีดสี",
     "IVP: usually not appropriate ในทุกสถานการณ์ของสไลด์",
     "ตั้งครรภ์ปวดสีข้าง: US ก่อน → MRI ไม่ฉีด gadolinium → low-dose CT",
     "Glomerular hematuria: dysmorphic RBC, RBC cast, proteinuria, สีโคล่า ไม่มีลิ่มเลือด → ส่งนักไต ไม่ต้อง CTU",
     "เลือดออกไม่เจ็บในผู้สูงอายุสูบบุหรี่ = มะเร็ง urothelium จนกว่าจะพิสูจน์ได้ → CTU + cystoscopy"],
    [mcq(N(18), "A 28-year-old woman at 24 weeks of gestation presents with acute right flank pain and microscopic haematuria. What is the most appropriate initial imaging?",
         ["Non-contrast CT KUB", "Intravenous urogram", "Renal and bladder ultrasound", "MRI with gadolinium", "Plain KUB radiograph"], 2,
         "ในหญิงตั้งครรภ์ เริ่มด้วย **ultrasound** เสมอ (ไม่มีรังสี ไม่ใช้สารทึบรังสี) — ถ้ายังไม่ได้คำตอบ ต่อด้วย **MRI ไม่ฉีด gadolinium** และใช้ **low-dose CT** เมื่อจำเป็นจริง (ACR — ไม่อยู่ในสไลด์)\n\n- **CT ไม่ฉีดสี** — ดีที่สุดสำหรับนิ่วในคนทั่วไป แต่ในครรภ์ไม่ใช่ตรวจแรก\n- **IVU และ plain KUB** — มีรังสีและได้ข้อมูลน้อยกว่า\n- **Gadolinium** ผ่านรกได้ เลี่ยงในการตั้งครรภ์\n\nข้อควรระวัง: ไตขวาขยายเล็กน้อยได้ตามปกติในครรภ์ (มดลูกกดท่อไตที่ pelvic brim + progesterone) — ใช้ ureteric jet ช่วยแปลผล",
         "ตั้งครรภ์ → US ก่อน", "Imaging in pregnancy", ["ACR Appropriateness Criteria (ไม่อยู่ในสไลด์)"], ["2.3.14-3(15)", "2.1.11"]),
     mcq(N(19), "A 35-year-old woman who has never smoked has 5 RBC/HPF on a single urinalysis with no proteinuria, no dysmorphic red cells and no other risk factors. Under the AUA/SUFU microhaematuria guideline, what is the recommended next step?",
         ["CT urography and cystoscopy", "Renal biopsy", "Repeat urinalysis within 6 months (or shared decision on cystoscopy and ultrasound)", "Intravenous urogram", "MRI of the abdomen with gadolinium"], 2,
         "ผู้หญิง < 50 ปี ไม่สูบบุหรี่ RBC 3–10/HPF ครั้งเดียว ไม่มีปัจจัยเสี่ยง = **ความเสี่ยงต่ำ** → **ตรวจปัสสาวะซ้ำใน 6 เดือน** หรือคุยร่วมกันเรื่อง cystoscopy + US (AUA/SUFU 2020)\n\n- **CTU + cystoscopy** — สำหรับความเสี่ยงสูง (≥ 60 ปี สูบบุหรี่หนัก RBC > 25 หรือเคยมี gross hematuria)\n- **Renal biopsy** — เมื่อมีหลักฐาน glomerular (dysmorphic RBC, RBC cast, proteinuria, Cr สูง) ซึ่งไม่มี\n- **IVU** และ **MRI** — ไม่ใช่การตรวจแรกในกลุ่มนี้",
         "Microhematuria ความเสี่ยงต่ำ → UA ซ้ำ", "AUA microhematuria risk strata", ["AUA/SUFU Microhematuria Guideline 2020 (amended 2025)"], ["2.1.43", "3.1.6", "B9.3(2)"]),
     mcq(N(20), "Which urinary finding most strongly indicates that haematuria originates from the glomerulus rather than from the collecting system or bladder?",
         ["Bright red urine with clots", "Isomorphic red cells with no protein", "Red cell casts with dysmorphic red cells (acanthocytes)", "Positive dipstick for blood with no red cells on microscopy", "Haematuria only at the end of micturition"], 2,
         "**RBC cast** เกิดได้เฉพาะเมื่อ RBC เข้ามาใน tubule (จาก glomerulus) แล้วถูก Tamm–Horsfall protein ห่อเป็นแท่ง · **acanthocyte/dysmorphic RBC** เกิดจาก RBC เบียดผ่าน GBM และเจอ osmotic stress ใน tubule → บ่งชี้ **glomerular bleeding**\n\n- **เลือดสดมีลิ่ม** — non-glomerular (tubule มี urokinase ลิ่มเลือดจากไตไม่ค่อยเกิด)\n- **RBC ปกติ ไม่มีโปรตีน** — non-glomerular\n- **Dipstick บวกแต่ไม่มี RBC** — hemoglobinuria/myoglobinuria\n- **เลือดตอนท้ายปัสสาวะ** — ต้นทางที่คอกระเพาะปัสสาวะ/ต่อมลูกหมาก",
         "RBC cast + dysmorphic RBC = glomerular", "Glomerular vs non-glomerular hematuria", ["ตำราโรคไตมาตรฐาน"], ["2.1.43", "B9.3(2)", "3.1.6"]),
    ], nl=["2.1.43", "3.1.6", "B9.3(2)", "B9.2.4-3(2)", "3.3.20", "2.3.14(3)"], figs=F8, src=SRC_ADD)

# ═════════════════════════════════════════════ 9
def _colic():
    o = [bean(52, 74, 30, 52, None, 0, 1, cls="ac"), ell(84, 80, 15, 13, "wa"),
         path("M92 92 C100 120 106 160 110 196", "lwa w5"), circ(111, 205, 7.5, "inkf"),
         path("M112 213 C114 250 116 290 118 326", "lwa w2"), ell(112, 352, 44, 22, "wa"),
         ar(128, 112, 130, 136, "lms w2", "ah-ms"), ar(132, 150, 133, 176, "lms w2", "ah-ms"), t(138, 146, "บีบไล่", "xs b tms"),
         t(102, 74, "pelvis ขยาย", "xs b twa"), t(112, 384, "กระเพาะปัสสาวะ", "xs mid mu"),
         t(8, 150, "นิ่วบน/PUJ:", "xs b"), t(8, 165, "ปวดสีข้าง-หลัง", "xs"),
         t(8, 236, "นิ่วกลาง:", "xs b"), t(8, 251, "ท้องน้อยข้างนั้น", "xs"),
         t(8, 300, "นิ่วปลาย/VUJ:", "xs b"), t(8, 315, "ขาหนีบ อัณฑะ/แคม", "xs"), t(8, 330, "+ ปัสสาวะบ่อย", "xs")]
    chain = [("ms", "ท่อไตบีบไล่นิ่วแรงขึ้น\nแต่นิ่วติดที่จุดแคบ"), ("ms", "ความดันใน pelvis ↑ · PGE₂ ↑\nเลือดไปไต/ปัสสาวะ ↑ ยิ่งดันสูง"),
             ("bad", "ท่อไตกระตุก + ปลอกไตถูกยืด\nใยประสาทอวัยวะภายใน T11–L2")]
    for i, (c, s) in enumerate(chain):
        y = 8 + i * 56
        o.append(box(176, y, 236, 42, c, s, "", 8, 11.5))
        if i: o.append(ar(294, y - 14, 294, y - 1, "lmu", "ah-mu"))
    outs = [("bad", "ปวดบิดเป็นพัก ๆ ร้าวลงขาหนีบ\n(genitofemoral n. · T12–L1)"), ("bx", "คลื่นไส้ อาเจียน ลำไส้นิ่ง\n(ใช้ celiac ganglion ร่วมกับ GI)"),
            ("bad", "ปัสสาวะเป็นเลือด\n(นิ่วครูดเยื่อบุ urothelium)"), ("bx", "ชีพจรเร็ว ความดันสูง ดิ้นไปมา\n(ปวด → sympathetic)")]
    o += [line(184, 166, 184, 329, "lmu")]
    for i, (c, s) in enumerate(outs):
        y = 172 + i * 46
        o += [box(196, y, 216, 38, c, s, "", 8, 11), ar(184, y + 19, 195, y + 19, "lmu", "ah-mu")]
    o += [line(294, 162, 294, 166, "lmu"), line(184, 166, 294, 166, "lmu"),
          box(176, 362, 236, 40, "ok", "NSAID ลด PGE₂ → ความดันในท่อลด\n= ยาแก้ปวดอันดับแรก (ถ้าไตดี)", "", 8, 11)]
    return svg(420, 410, "กลไกของอาการปวดแบบ renal colic และอาการร่วม", *o)

F9 = {"colic": fig("Renal colic — จากนิ่วติดท่อ สู่อาการที่ผู้ป่วยบอก",
        "นิ่วติดที่จุดแคบ → ท่อไตเหนือนิ่ว **บีบตัวแรงเป็นพัก ๆ** (จึงปวด \"บิด\" เป็นระลอก) และ **ความดันในระบบรวบรวมปัสสาวะสูง** จนปลอกไตถูกยืด · PGE₂ ที่หลั่งออกมาทำให้หลอดเลือดแดงขาเข้าไตขยาย ปัสสาวะออกมากขึ้น ความดันยิ่งสูง (**NSAID จึงได้ผลดี**) · ใยประสาทรับความรู้สึกของไตและท่อไตเข้าไขสันหลัง **T11–L2** ร่วมกับผิวหนังสีข้าง ขาหนีบ และ genitofemoral nerve → สมองแปลว่าปวดที่ผิวหนังเหล่านั้น (**referred pain**) · ตำแหน่งปวดเลื่อนลงตามนิ่ว: นิ่วปลายท่อไตระคายผนังกระเพาะปัสสาวะ → **ปัสสาวะบ่อย กลั้นไม่อยู่** · ไตและลำไส้ใช้ celiac ganglion ร่วมกัน → **คลื่นไส้ อาเจียน bowel sound ลด** (เคส 01 ของสไลด์)",
        _colic())}

sec("neph-img-09", "Case 01 ปวดสีข้างเฉียบพลัน — renal colic และการเลือก CT",
    "เคสสไลด์: ชาย 40 ปี ปวดสีข้างขวาทันที · กลไกของอาการ · KUB 29% vs US vs CT 97/95% · soft tissue rim sign · เมื่อไรต้องระบายด่วน", 11,
"""### Case 01 (สไลด์)
ชายไทยอายุ 40 ปี แข็งแรงดี **ปวดสีข้าง (flank) ขวาทันทีทันใด 2 ชม.**
- V/S: BT **37.2 °C** · BP **169/95** · PR **130** · RR 24
- Abdomen: ไม่อืด **bowel sound ลดลง (hypoactive)** นุ่ม ไม่มีก้อน **Murphy's sign ลบ** · ไม่ซีด ไม่เหลือง

#### ทำไมถึงมีอาการนี้
[[fig:colic]]
| อาการ/อาการแสดง | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ปวดบิดเป็นพัก ๆ ทันทีทันใด** | ท่อไตเหนือนิ่วบีบตัวไล่เป็นระลอก (peristalsis + spasm) ชนกับนิ่วที่ติดจุดแคบ · ความดันในท่อและ pelvis สูงทันที | ต่างจากปวดตื้อคงที่ของ pyelonephritis |
| **ปวดสีข้าง → ร้าวลงขาหนีบ อัณฑะ/แคม** | ใยประสาทของไต/ท่อไตเข้าไขสันหลัง **T11–L2** ระดับเดียวกับผิวหนังสีข้าง ขาหนีบ และ **genitofemoral nerve** → referred pain · ปวดเลื่อนลงตามนิ่ว | ตำแหน่งปวดบอกระดับนิ่วคร่าว ๆ |
| **ปัสสาวะบ่อย ปวดเบ่ง** | นิ่วที่ VUJ ระคายผนังกระเพาะปัสสาวะ | นิ่วใกล้ลงกระเพาะแล้ว |
| **ดิ้นไปมา หาท่าสบายไม่ได้** | ปวดจากอวัยวะกลวงที่บีบตัว ไม่ใช่การอักเสบของเยื่อบุช่องท้อง | **peritonitis นอนนิ่ง** เพราะขยับแล้วเจ็บ |
| **คลื่นไส้ อาเจียน bowel sound ลด** | ไตและลำไส้ส่งสัญญาณผ่าน **celiac/splanchnic ganglion** ร่วมกัน → reflex ileus | เคสนี้ hypoactive bowel sound โดยไม่มีท้องอืด |
| **ปัสสาวะเป็นเลือด** | นิ่วครูดเยื่อบุ urothelium | พบได้บ่อย แต่ **ไม่มีก็ไม่ตัดนิ่ว** (นิ่วอุดสนิทปัสสาวะข้างนั้นไม่ไหลลงมา) |
| **HR 130 · BP 169/95** | ความปวด → sympathetic surge | ถ้า **BP ต่ำ** ในผู้สูงอายุ คิดถึง **AAA rupture** |
| **ไม่มีไข้ (37.2 °C)** | ยังไม่มีการติดเชื้อเหนือการอุดกั้น | **ไข้ + นิ่วอุด = obstructed infected kidney** ต้องระบายด่วน |

**โรคที่ห้ามพลาดเมื่อปวดสีข้าง**: AAA แตก (อายุ > 60 ปี ปวดครั้งแรก ความดันต่ำ) · APN · ท้องนอกมดลูก · ไส้ติ่งอักเสบ · ถุงน้ำดีอักเสบ (เคสนี้ Murphy ลบ) · mesenteric ischemia — **CT ไม่ฉีดสีเห็นโรคเหล่านี้ได้หลายโรคในการตรวจครั้งเดียว**

### ภาพที่ใช้ในนิ่ว (สไลด์)
**ACR Appropriateness Criteria — Flank pain (suspected urolithiasis)**
| การตรวจ | ความเหมาะสม |
|---|---|
| **CT KUB ไม่ฉีดสี** | **Usually APPROPRIATE** |
| USG KUB | May be appropriate |
| Plain KUB | May be appropriate |
| MRI ± gadolinium | Usually not appropriate |
| IVU/IVP | Usually not appropriate |
| CT KUB ฉีดสี | Usually not appropriate |

| การตรวจ | สิ่งที่เห็น (สไลด์) | ความแม่นยำ / ข้อจำกัด |
|---|---|---|
| **Plain KUB** | เงาทึบในแนวทางเดินปัสสาวะ · **staghorn stone** | sens **29%** สำหรับนิ่วทุกขนาด · **72%** สำหรับนิ่ว > 5 มม. ในท่อไตส่วนต้น · แยกจาก phlebolith ยาก · นิ่ว **uric acid, cystine, indinavir, xanthine** ไม่ทึบรังสี |
| **Ultrasound** | **hyperechoic focus + posterior acoustic shadow** ใน calyx ขั้วบน · **twinkle artifact** บน Doppler · hydronephrosis | ไม่มีรังสี เหมาะตั้งครรภ์ เด็ก ติดตามผล · ท่อไตกลางมองยาก |
| **CT ไม่ฉีดสี** | (สไลด์ใช้ภาพ CTU) corticomedullary phase เห็น **moderate left hydronephrosis** · excretory phase เห็นนิ่วท่อไตซ้ายส่วนกลางพร้อม **soft tissue rim sign** | sens **97%** · spec **95%** · บอกจำนวน ขนาด ตำแหน่ง ภาวะแทรกซ้อน วางแผนผ่าตัด · **DECT** บอกชนิดนิ่ว |

#### ทำไมภาพถึงออกมาแบบนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Soft tissue rim sign** | ผนังท่อไตบวมรอบนิ่วที่ติดอยู่ เห็นเป็นวงเนื้อเยื่อล้อมจุดขาว | นิ่ว **อยู่ในท่อไต** · phlebolith ไม่มีวงนี้ แต่มี "comet-tail" (หลอดเลือดดำที่ต่อออกมา) |
| **Hydronephrosis / hydroureter ถึงตำแหน่งนิ่ว** | ปัสสาวะค้างเหนือจุดอุด ท่อขยายลงมาหยุดที่นิ่ว | บอกว่านิ่วก้อนไหนเป็นตัวอุด |
| **Perinephric fat stranding** | ความดันสูงทำให้ fornix ของ calyx รั่ว/น้ำเหลืองคั่ง ปัสสาวะซึมออกรอบไต | การอุดกั้นเฉียบพลันที่มีความดันสูง |
| **Hydronephrosis ไม่มีในชั่วโมงแรก** | ระบบยังขยายไม่ทัน หรือผู้ป่วยขาดน้ำปัสสาวะน้อย | US ปกติในระยะแรก **ไม่ตัดนิ่ว** |
| **KUB ไม่เห็นนิ่วที่ CT เห็น** | นิ่วเล็ก ถูกลม/กระดูกบัง หรือเป็นชนิดโปร่งรังสี | สไลด์: sens เพียง 29% |

### ภาพเปลี่ยนการรักษาอย่างไร (EAU Urolithiasis 2025 — ไม่อยู่ในสไลด์)
- **ยาแก้ปวด**: **NSAID** เป็นอันดับแรก (ถ้าไตดี) เพราะลด PGE₂ ที่ทำให้ความดันในท่อสูง · opioid เป็นตัวเสริม
- **นิ่วเล็ก (≤ 5 มม.)** ส่วนใหญ่หลุดเอง → ดื่มน้ำ ยาแก้ปวด ติดตาม · **α-blocker (tamsulosin)** คลายกล้ามเนื้อเรียบท่อไตส่วนปลาย (มี α₁ receptor มาก) ช่วยขับนิ่ว — EAU แนะนำชัดสำหรับนิ่วท่อไตส่วนปลาย **> 5 มม.**
- **ระบายด่วน (PCN หรือ DJ stent)** เมื่อ: **นิ่วอุด + ติดเชื้อ/ไข้** · AKI ในไตข้างเดียวหรืออุดสองข้าง · ปวด/อาเจียนจนคุมไม่ได้ — **ยาปฏิชีวนะอย่างเดียวไม่พอ** เพราะหนองในระบบที่อุดอยู่ภายใต้ความดัน ยาเข้าไม่ถึงและเชื้อเข้ากระแสเลือดต่อเนื่อง
- **เอานิ่วออก** (URS, ESWL, PCNL) เมื่อนิ่วใหญ่หรือไม่หลุดตามเวลา
""",
    ["Renal colic: peristalsis ชนนิ่ว + ความดันใน pelvis + ปลอกไตยืด → ปวดบิด ร้าวลงขาหนีบ (T11–L2, genitofemoral)",
     "คลื่นไส้/bowel sound ลด: celiac ganglion ใช้ร่วมกับลำไส้ · ดิ้นไปมา ต่างจาก peritonitis ที่นอนนิ่ง",
     "ACR: CT KUB ไม่ฉีดสี usually appropriate · CT ฉีดสี/IVP/MRI usually not",
     "KUB sens 29% (72% ถ้า > 5 มม. ท่อไตส่วนต้น) · CT sens 97% spec 95%",
     "นิ่วอุด + ไข้ = ระบายด่วน (PCN/DJ stent) — ยาปฏิชีวนะอย่างเดียวไม่พอ"],
    [mcq(N(21), "A 40-year-old man has sudden severe right flank pain radiating to the groin, vomiting and microscopic haematuria. He has normal renal function and is afebrile. Which imaging study is most appropriate first?",
         ["Plain KUB radiograph", "Intravenous urography", "Low-dose non-contrast CT of the abdomen and pelvis (CT KUB)", "Contrast-enhanced CT abdomen in the portal venous phase", "MRI abdomen with gadolinium"], 2,
         "ACR (สไลด์): **CT KUB ไม่ฉีดสี = usually appropriate** — sens 97% spec 95% บอกขนาด ตำแหน่ง ภาวะแทรกซ้อน และเห็นโรคอื่นที่เลียนแบบได้ · ใช้ **low-dose** ลดรังสี\n\n- **Plain KUB** — may be appropriate แต่ไวเพียง 29%\n- **IVU** — usually not appropriate (ต้องฉีดสี หลายฟิล์ม)\n- **CT ฉีดสี** — contrast ที่ขับออกมาบังนิ่ว (usually not appropriate)\n- **MRI** — เห็นนิ่วไม่ดี (usually not appropriate)",
         "สงสัยนิ่ว → CT KUB ไม่ฉีดสี", "Imaging for renal colic", REF("Case 01 — ACR flank pain"), ["2.3.14-3(15)", "3.3.20", "2.1.11"]),
     mcq(N(22), "Why does pain from a stone in the ureter typically radiate from the flank to the groin and testis (or labium)?",
         ["The stone directly compresses the femoral nerve", "Visceral afferents from the ureter enter the spinal cord at T11–L2, the same segments that supply the skin of the flank and groin (including the genitofemoral nerve)", "Urine leaks into the scrotum through the inguinal canal", "The ureter is innervated by the vagus nerve", "Inflammation spreads along the psoas sheath to the testis"], 1,
         "ใยประสาทรับความรู้สึกอวัยวะภายในของไตและท่อไต (ตามเส้นทาง sympathetic) เข้าไขสันหลังระดับ **T11–L2** ซึ่งเป็นระดับเดียวกับผิวหนังสีข้าง ขาหนีบ และ **genitofemoral nerve (L1–L2)** สมองจึงแปลความปวดว่ามาจากผิวหนังบริเวณนั้น = **referred pain** · ยิ่งนิ่วเลื่อนลง ปวดยิ่งลงมาทางขาหนีบ\n\n- นิ่วไม่ได้กด femoral nerve โดยตรง\n- ปัสสาวะไม่ได้รั่วลงถุงอัณฑะ\n- ท่อไตไม่ได้รับเส้นประสาท vagus เป็นหลักในการรับปวด\n- การอักเสบตาม psoas sheath (psoas abscess) ให้อาการต่างออกไป — มีไข้ สะโพกงอ",
         "ปวดร้าวลงขาหนีบ = referred pain T11–L2", "Referred pain in renal colic", ["สรีรวิทยา/กายวิภาคมาตรฐาน"], ["2.3.14-3(15)", "B9.1.1(3)", "2.1.11"]),
     mcq(N(23), "A 52-year-old woman has a 7-mm obstructing left proximal ureteric stone with moderate hydronephrosis on non-contrast CT. She has a temperature of 39.0 °C, BP 96/58 mmHg and pyuria. Besides resuscitation and IV antibiotics, what is the most important next step?",
         ["Medical expulsive therapy with tamsulosin and review in 2 weeks", "Urgent decompression of the left collecting system (percutaneous nephrostomy or ureteric stent)", "Extracorporeal shock wave lithotripsy today", "Contrast-enhanced CT to measure split function", "Oral potassium citrate"], 1,
         "**นิ่วอุด + ติดเชื้อ (obstructed infected kidney)** เป็นภาวะฉุกเฉินทางระบบปัสสาวะ — หนองอยู่ใต้ความดันในระบบที่อุดตัน ยาปฏิชีวนะเข้าไม่ถึงและเชื้อเข้ากระแสเลือดต่อเนื่อง ต้อง **ระบายด่วนด้วย PCN หรือ DJ stent** ก่อน แล้วค่อยเอานิ่วออกเมื่อหายติดเชื้อ (EAU 2025)\n\n- **Tamsulosin รอขับนิ่ว** — ใช้ได้เฉพาะเมื่อไม่มีการติดเชื้อ\n- **ESWL/ทำลายนิ่วตอนติดเชื้อ** — เพิ่มความเสี่ยง sepsis\n- **CT ฉีดสี** ไม่ช่วยการรักษาเฉียบพลัน และเสี่ยงไตในภาวะช็อก\n- **Potassium citrate** ใช้ป้องกันนิ่วบางชนิดระยะยาว",
         "นิ่วอุด + ไข้ = ระบายด่วน", "Obstructed infected kidney", ["EAU Guidelines on Urolithiasis 2025"], ["2.3.14-3(15)", "2.3.14(14)", "2.3.14-3(9)"]),
    ], nl=["2.3.14-3(15)", "B9.2.3-3(1)", "2.1.11", "2.1.15", "2.1.43", "B9.1.1(3)", "3.3.20", "3.2.3"], figs=F9)

# ═════════════════════════════════════════════ 10
def _stones():
    rows = [("Calcium oxalate", "พบบ่อยสุด 70–80%", "#f2f2f2", "#ffffff", "Ca (Z 20) ดูดกลืนสูง", "ขาวชัดทั้งคู่"),
            ("Calcium phosphate", "ปัสสาวะด่าง · dRTA", "#ffffff", "#ffffff", "Ca + PO₄", "ทึบที่สุด"),
            ("Struvite", "MgNH₄PO₄ · staghorn", "#c9c9c9", "#ececec", "มี phosphate/Ca ปน", "ทึบปานกลาง"),
            ("Cystine", "กรรมพันธุ์", "#5c5c5c", "#c4c4c4", "มีกำมะถัน (S)", "KUB จาง ๆ"),
            ("Uric acid", "ปัสสาวะกรด · gout", None, "#a8a8a8", "C H N O ล้วน", "KUB ไม่เห็น · CT เห็น"),
            ("Indinavir", "ยาต้าน HIV ตกผลึก", None, None, "ผลึกยา ความทึบต่ำมาก", "แม้ CT ก็ไม่เห็น")]
    o = [t(196, 18, "KUB", "sm b mid"), t(262, 18, "CT", "sm b mid"), t(302, 18, "ทำไม", "sm b")]
    for i, (a, b, kc, cc, w1, w2) in enumerate(rows):
        y = 28 + i * 48
        o += [t(10, y + 18, a, "sm b"), t(10, y + 34, b, "xs mu"),
              film(166, y, 60, 40, "#353535", 4), film(232, y, 60, 40, "#6a6a6a", 4)]
        o.append(FE(196, y + 20, 11, 7.5, kc) if kc else FE(196, y + 20, 11, 7.5, None, None, "#9a9a9a", 1).replace('stroke:#9a9a9a', 'stroke:#9a9a9a;stroke-dasharray:3 2'))
        o.append(FE(262, y + 20, 11, 7.5, cc) if cc else FE(262, y + 20, 11, 7.5, None, None, "#d0d0d0", 1).replace('stroke:#d0d0d0', 'stroke:#d0d0d0;stroke-dasharray:3 2'))
        o += [t(302, y + 18, w1, "xs"), t(302, y + 34, w2, "xs mu")]
    o += [t(10, 326, "เส้นประ = มีนิ่วอยู่จริงแต่ภาพไม่แสดง", "xs mu")]
    return svg(420, 334, "ชนิดนิ่วกับความทึบบน KUB และ CT", *o)

def _ph():
    X = lambda p: 30 + (p - 4.5) * 102.9
    o = [rect(X(4.5), 70, X(5.5) - X(4.5), 18, "bad", 0), rect(X(5.5), 70, X(6.5) - X(5.5), 18, "sk", 0),
         rect(X(6.5), 70, X(8.0) - X(6.5), 18, "ms", 0), rect(X(4.5), 70, X(8.0) - X(4.5), 18, "lmu", 4)]
    for p in (4.5, 5.5, 6.5, 7.2, 8.0):
        o += [line(X(p), 88, X(p), 94, "ln"), t(X(p), 106, ("%.1f" % p), "xs mid mu")]
    o += [t(X(4.5), 62, "uric acid ตกผลึก", "xs b tbad"), t(X(4.5), 46, "(pKa ≈ 5.5)", "xs mu"),
          t(X(8.0), 62, "phosphate ตกผลึก", "xs b end tms"), t(210, 24, "pH ของปัสสาวะ", "sm b mid"),
          ar(X(5.0), 124, X(6.75), 124, "lok w2", "ah-ok"), t(X(5.0), 142, "K citrate / NaHCO₃ → pH 6.5–7 → urate ละลาย", "xs tok"),
          line(X(7.2), 160, X(8.0), 160, "lbad w3"), t(X(7.2) - 4, 164, "struvite: urease → NH₃ → pH > 7.2", "xs end tbad"),
          line(X(6.5), 182, X(8.0), 182, "lms w3"), t(X(6.5) - 4, 186, "Ca phosphate: pH > 6.5 (dRTA)", "xs end tms"),
          line(X(4.5), 204, X(8.0), 204, "lmu w2 da"), t(X(4.5), 222, "Ca oxalate: แทบไม่ขึ้นกับ pH", "xs mu")]
    return svg(420, 230, "pH ของปัสสาวะกำหนดชนิดนิ่วที่ตกผลึก", *o)

F10 = {"stones": fig("ส่วนประกอบของนิ่ว → ความทึบบน KUB และ CT",
        "ความทึบขึ้นกับ **เลขอะตอมของธาตุในนิ่ว** — นิ่วที่มี **แคลเซียม** ขาวชัดทั้ง KUB และ CT · **struvite** มี phosphate และมักมี calcium apatite ปน จึงทึบพอเห็นได้ (staghorn) · **cystine** มีกำมะถันจึงจาง ๆ บน KUB (สไลด์จัดเป็น radiolucent ตำราส่วนใหญ่เรียก faintly radiopaque) · **uric acid** มีแค่ C H N O จึง **ไม่เห็นบน KUB แต่ CT เห็น** (ราว 200–500 HU) · นิ่วจาก **indinavir** ไม่เห็นแม้บน CT ต้องอาศัยหลักฐานทางอ้อม (hydronephrosis) · รายชื่อนิ่วโปร่งรังสีตามสไลด์: uric acid, cystine, indinavir, xanthine",
        _stones()),
       "ph": fig("pH ของปัสสาวะเลือกว่านิ่วชนิดไหนจะตกผลึก",
        "**Uric acid** มี pKa ราว 5.5 — ที่ pH ต่ำกว่านี้อยู่ในรูปไม่แตกตัวซึ่งละลายน้ำได้น้อยมาก จึงตกผลึก · ทำปัสสาวะให้เป็นด่าง (potassium citrate, NaHCO₃) ถึง pH 6.5–7 กรดยูริกเปลี่ยนเป็น urate ที่ละลายได้ → **นิ่วชนิดเดียวที่ละลายด้วยยาได้** · **Struvite** เกิดเมื่อเชื้อที่สร้าง urease ย่อยยูเรียเป็นแอมโมเนีย ปัสสาวะด่างจัด (> 7.2) · **Calcium phosphate** ตกผลึกในปัสสาวะด่าง เช่น distal RTA · **Calcium oxalate** ขึ้นกับปริมาณ Ca oxalate citrate และปริมาตรปัสสาวะมากกว่า pH (ไม่อยู่ในสไลด์ — ตำราโรคไต/EAU 2025)",
        _ph())}

sec("neph-img-10", "ชนิดนิ่ว ความทึบรังสี และ staghorn",
    "ทำไมนิ่วบางชนิดไม่เห็นบน KUB · pH กับชนิดนิ่ว · staghorn = struvite จากเชื้อสร้าง urease · ข้อสอบเก่า", 9,
"""### นิ่วไม่ได้ทึบรังสีทุกชนิด (สไลด์)
> "Not all stone compositions are radiopaque. (Uric acid, cystine, indinavir, xanthine stone are radiolucent.)" — ACR Acute Onset Flank Pain, revised 2023

[[fig:stones]]
#### ทำไมภาพถึงออกมาแบบนี้
| ชนิดนิ่ว | KUB | CT | กลไก |
|---|---|---|---|
| **Calcium oxalate** (พบบ่อยที่สุด) | ทึบ | ทึบมาก (> 1000 HU) | Ca เลขอะตอมสูง |
| **Calcium phosphate** | ทึบมาก | ทึบมาก | Ca + PO₄ |
| **Struvite** | ทึบปานกลาง — **staghorn** | ทึบ | Mg NH₄ PO₄ + carbonate apatite |
| **Cystine** | จาง ("ground glass") — สไลด์จัดเป็นโปร่งรังสี | ทึบปานกลาง | มีกำมะถัน (S) |
| **Uric acid** | **ไม่เห็น** | **เห็น** (ราว 200–500 HU) | C H N O ล้วน · **DECT แยกจากนิ่วแคลเซียมได้** |
| **Indinavir** | ไม่เห็น | **ไม่เห็น** | ผลึกยาความทึบต่ำ |
| **Xanthine** | ไม่เห็น | เห็นจาง ๆ | purine (สไลด์จัดเป็นโปร่งรังสี) |
ทุกชนิดเป็น **hyperechoic + shadow บน ultrasound** เพราะ ultrasound ขึ้นกับ impedance ไม่ใช่เลขอะตอม

### pH ของปัสสาวะ — ตัวเลือกว่านิ่วชนิดไหนจะเกิด (ไม่อยู่ในสไลด์)
[[fig:ph]]
#### ทำไมถึงเกิดนิ่วชนิดนี้
| ชนิด | กลไก | ตัวอย่างผู้ป่วย |
|---|---|---|
| **Calcium oxalate** | ปัสสาวะน้อย · Ca หรือ oxalate ในปัสสาวะสูง · **citrate (ตัวยับยั้งผลึก) ต่ำ** | ดื่มน้ำน้อย อากาศร้อน · ลำไส้ดูดซึมไขมันผิดปกติ (Ca จับไขมัน oxalate อิสระถูกดูดซึมมาก) |
| **Uric acid** | **ปัสสาวะเป็นกรดตลอด** (pH < 5.5) มากกว่ากรดยูริกสูง | **เบาหวาน/metabolic syndrome** (ภาวะดื้ออินซูลินลดการสร้าง NH₄⁺ ที่ไต ปัสสาวะจึงเป็นกรด) · gout · ท้องเสียเรื้อรัง |
| **Struvite** | เชื้อสร้าง **urease** (Proteus, Klebsiella …) ย่อยยูเรีย → NH₃ → pH > 7.2 → Mg NH₄ PO₄ ตกผลึก · นิ่วเป็นที่ซ่อนของเชื้อ (biofilm) | UTI ซ้ำ · สายสวนคา · neurogenic bladder |
| **Calcium phosphate** | ปัสสาวะด่าง + Ca สูง + citrate ต่ำ | **distal RTA** (หัวข้อ Case 04) · hyperparathyroidism |
| **Cystine** | cystinuria — ท่อไตดูดกลับ cystine ornithine lysine arginine ไม่ได้ · cystine ละลายน้อยในปัสสาวะกรด | นิ่วตั้งแต่อายุน้อย · ผลึก **หกเหลี่ยม** |

### Staghorn calculus
- นิ่วแตกกิ่งเต็ม **renal pelvis และ calyces** — ส่วนใหญ่เป็น **struvite ± carbonate apatite** (infection stone) แต่ cystine และ uric acid ก็เป็น staghorn ได้
- **ทำไมโตเร็วและเป็นซ้ำ**: เชื้อฝังอยู่ในเนื้อนิ่ว ยาปฏิชีวนะฆ่าได้แค่เชื้อในปัสสาวะ — ต้อง **เอานิ่วออกให้หมด** (มักใช้ PCNL) ร่วมกับยาปฏิชีวนะ
- ปล่อยไว้: ไตเสื่อม ติดเชื้อซ้ำ sepsis · xanthogranulomatous pyelonephritis
- **KUB**: เงาทึบแตกกิ่งรูปเขากวางในตำแหน่ง pelvis/calyces (สไลด์ "Staghorn Stone") — ข้อสอบ SAQ ถามให้ **อ่าน KUB อย่างเป็นระบบ** (ดูแท็บ OSCE/SAQ)
""",
    ["Calcium oxalate พบบ่อยที่สุด · Ca stones ทึบทั้ง KUB และ CT",
     "Uric acid: KUB ไม่เห็น CT เห็น · Indinavir: แม้ CT ก็ไม่เห็น · Cystine จาง (ground glass)",
     "Uric acid ตกผลึกเมื่อ pH < 5.5 → รักษาด้วยทำปัสสาวะด่าง ดื่มน้ำ ไม่ใช่ probenecid",
     "Staghorn ส่วนใหญ่ = struvite จาก urease (Proteus) · pH > 7.2 · coffin-lid crystal",
     "Staghorn ต้องเอานิ่วออกหมด + ยาปฏิชีวนะ เพราะเชื้อฝังในนิ่ว"],
    [mcq(N(24), "A 45-year-old man with HIV taking an older protease-inhibitor regimen develops right renal colic. Non-contrast CT shows right hydronephrosis and hydroureter down to the vesicoureteric junction but no visible calculus. Which stone composition best explains this?",
         ["Calcium oxalate", "Calcium phosphate", "Struvite", "Indinavir", "Cystine"], 3,
         "นิ่วจาก **indinavir** (protease inhibitor รุ่นเก่า) เป็นผลึกยาที่ **ความทึบต่ำมากจนไม่เห็นแม้บน CT ไม่ฉีดสี** — ภาพจึงมีแต่หลักฐานทางอ้อม คือท่อขยายลงไปจนถึงจุดอุด (สไลด์จัด indinavir เป็นนิ่วโปร่งรังสี)\n\n- **Calcium oxalate / phosphate** — ทึบมากทั้ง KUB และ CT\n- **Struvite** — ทึบ มักเป็น staghorn\n- **Cystine** — จางบน KUB แต่ **เห็นชัดบน CT**",
         "นิ่วที่ CT ก็ไม่เห็น = indinavir", "Radiolucent stones on CT", REF("Plain radiograph of kidney stone — radiolucent compositions"), ["2.3.14-3(15)", "B9.2.3-3(1)", "3.3.20"]),
    ], nl=["2.3.14-3(15)", "B9.2.3-3(1)", "B9.3(2)", "3.2.3", "3.3.20"], figs=F10)

# ═════════════════════════════════════════════ 11
def _apn():
    o = [t(110, 18, "APN", "sm b mid"), t(232, 18, "ฝีในไต (abscess)", "sm b mid"), t(354, 18, "EPN (ก๊าซ)", "sm b mid"),
         t(8, 80, "US", "sm b"), t(8, 190, "CT", "sm b")]
    cols = (50, 172, 294)
    for k, x in enumerate(cols):
        cx = x + 60
        # แถว US
        o.append(film(x, 28, 120, 96, "#0b0b0b"))
        if k == 0:
            o += [FE(cx, 76, 48, 28, "#7c7c7c", None, "#d6d6d6", 1.4), FE(cx, 76, 24, 9, "#bdbdbd")]
        elif k == 1:
            o += [FE(cx, 76, 46, 26, "#5e5e5e", None, "#d6d6d6", 1.4), FE(cx, 76, 22, 8, "#bdbdbd"),
                  FP("M%s 82 L%s 82 L%s 122 L%s 122 Z" % (_n(cx - 18), _n(cx + 2), _n(cx + 4), _n(cx - 20)), "#9a9a9a"),
                  FC(cx - 8, 66, 13, "#191919", "#bdbdbd", 1), FC(cx - 12, 64, 1.4, "#5a5a5a"), FC(cx - 5, 70, 1.6, "#5a5a5a"), FC(cx - 9, 72, 1.2, "#5a5a5a")]
        else:
            o += [FE(cx, 78, 46, 26, "#5e5e5e", None, "#d6d6d6", 1.4),
                  FP("M%s 58 Q%s 52 %s 58" % (_n(cx - 22), _n(cx - 6), _n(cx + 10)), None, "#f2f2f2", 3),
                  FP("M%s 62 L%s 62 L%s 104 L%s 104 Z" % (_n(cx - 22), _n(cx + 10), _n(cx + 14), _n(cx - 26)), "#3e3e3e")]
            for dy in (70, 80, 90, 100):
                o.append(FL(cx - 20, dy, cx + 8, dy, "#8a8a8a", 1.2))
        # แถว CT
        o.append(film(x, 138, 120, 96, "#151515"))
        if k == 0:
            o += [bean(cx, 186, 30, 36, "#c6c6c6", 0, 1), FE(cx + 15, 186, 10, 9, "#2a2a2a")]
            for (a, b, c2) in ((-30, -10, -6), (-22, 20, 6), (-6, -34, -4)):
                o.append(FP("M%s %s L%s %s L%s %s Z" % (_n(cx + a), _n(186 + b), _n(cx + a + 10), _n(186 + b + 4), _n(cx + 6), _n(186 + c2)), "#707070"))
        elif k == 1:
            o += [bean(cx, 186, 30, 36, "#c6c6c6", 0, 1), FE(cx + 15, 186, 10, 9, "#2a2a2a"),
                  FC(cx - 10, 176, 14, "#4a4a4a", "#f6f6f6", 2.4)]
        else:
            o += [bean(cx, 186, 30, 36, "#a8a8a8", 0, 1), FE(cx + 15, 186, 10, 9, "#2a2a2a"),
                  FP("M%s 164 q8 -6 14 2 q6 8 -2 12 q-10 4 -12 -4 z" % _n(cx - 20), AIR),
                  FP("M%s 194 q10 -4 14 4 q2 8 -8 8 q-8 0 -6 -12 z" % _n(cx - 24), AIR), FC(cx - 4, 210, 4, AIR)]
    txt = [("ไตบวม echo เปลี่ยน", "CT: ลิ่มรับสีน้อย", "ไม่ซับซ้อน = ไม่ต้องตรวจ"),
           ("หนองเหลว: ดำปนเทา", "หลังก้อนสว่าง (enhance)", "CT: ขอบบางรับสี (rim)"),
           ("ก๊าซลอยด้านบน: จ้า", "+ dirty shadowing", "CT: ก๊าซในเนื้อไต (ยืนยัน)")]
    for k, x in enumerate(cols):
        for j, s in enumerate(txt[k]):
            o.append(t(x + 60, 252 + j * 16, s, "xs mid" + (" mu" if j == 2 else "")))
    return svg(420, 300, "ภาพ ultrasound และ CT ของ acute pyelonephritis ฝีในไต และ emphysematous pyelonephritis", *o)

F11 = {"apn": fig("กรวยไตอักเสบที่ซับซ้อน — ภาพบอกอะไรที่ยาปฏิชีวนะอย่างเดียวแก้ไม่ได้",
        "**APN**: เนื้อไตบวมจากการอักเสบ ultrasound มักปกติหรือไตโต echo เปลี่ยน · CT ฉีดสีเห็น **ลิ่มรับสีน้อยเป็นแฉก (striated/wedge-shaped)** เพราะการอักเสบทำให้ท่อไตในกลีบนั้นบวม อุดด้วยเศษเซลล์ และหลอดเลือดหดตัว contrast จึงเข้าและไหลผ่านน้อย · **ฝี**: หนองเหลวตรงกลาง (ultrasound ดำปนเทา มี **posterior enhancement** เพราะเป็นของเหลว · CT ตรงกลางไม่รับสี) ล้อมด้วย granulation tissue ที่มีหลอดเลือดใหม่จึง **ขอบรับสี (rim enhancement)** · **EPN**: ก๊าซลอยไปด้านบน (non-dependent) สะท้อนเสียงหมดแล้วสะท้อนกลับไปมาเป็น **dirty shadowing** · CT เห็นก๊าซในเนื้อไตชัดที่สุด (คำบรรยายภาพจากสไลด์ case 02 · Imaging in Urology 2018 · Comprehensive Clinical Nephrology 2024)",
        _apn())}

sec("neph-img-11", "Case 02 กรวยไตอักเสบที่ไข้ไม่ลง — ฝีในไตและ emphysematous pyelonephritis",
    "เคสสไลด์: หญิงเบาหวาน 65 ปี E. coli APN ไข้ไม่ลงหลัง ceftriaxone 7 วัน · ACR uncomplicated vs complicated · ทำไมมีก๊าซ ทำไมขอบฝีรับสี", 10,
"""### Case 02 (สไลด์)
หญิงไทยอายุ 65 ปี **เบาหวาน** นอนโรงพยาบาลมา 7 วัน
- V/S: BT **39.2 °C** · BP **105/65** · PR **120** · RR 24 · PE: **right CVA tenderness**
- Principal diagnosis: **E. coli acute pyelonephritis with septicemia** · ได้ **ceftriaxone × 7 วัน**
- ผล: **ยังมีไข้ ปวดหลังขวา** → ✍️ ลายมือในสไลด์: **"Abscess? / emphysematous"**

#### ทำไมถึงมีอาการนี้
| อาการ/อาการแสดง | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ไข้สูง หนาวสั่น** | เชื้อและ endotoxin เข้ากระแสเลือด → IL-1 IL-6 TNF → PGE₂ ที่ hypothalamus ปรับจุดตั้งอุณหภูมิขึ้น | APN มีไข้ cystitis ไม่มี |
| **เคาะ CVA เจ็บ** | ไตที่อักเสบบวม ดันปลอกไต (capsule) ให้ตึง การเคาะกระเทือนปลอกไตที่ตึงอยู่ | บอกว่าการติดเชื้ออยู่ที่เนื้อไต |
| **BP 105/65 · PR 120** | sepsis → หลอดเลือดขยาย ร่วมกับขาดน้ำ | ประเมินความรุนแรง |
| **ไข้ไม่ลงหลังได้ยาที่เหมาะสม 48–72 ชม.** | ยาเข้าไม่ถึงเชื้อ: **(1) การอุดกั้น** — หนองใต้ความดัน · **(2) ฝี** — หนองไม่มีหลอดเลือด ยาซึมเข้าน้อย · **(3) EPN** — เนื้อไตตายเป็นโพรงก๊าซ · หรือเชื้อดื้อยา/แหล่งติดเชื้ออื่น | **ข้อบ่งชี้ส่งตรวจภาพ** (complicated APN) |
| **ทำไมเบาหวานเสี่ยง** | น้ำตาลในปัสสาวะและเนื้อเยื่อเป็นอาหารเชื้อ · neutrophil ทำงานแย่ · หลอดเลือดเล็กเสื่อม (เนื้อเยื่อขาดเลือด) · กระเพาะปัสสาวะบีบตัวไม่ดีจาก neuropathy | EPN เกือบทั้งหมดเกิดในผู้ป่วยเบาหวาน |

### ACR — acute pyelonephritis (สไลด์)
| การตรวจ | **ไม่ซับซ้อน** | **ซับซ้อน** |
|---|---|---|
| USG KUB | Usually not appropriate | **May be appropriate** |
| IVU/IVP | Usually not appropriate | Usually not appropriate |
| CT KUB | Usually not appropriate (± contrast) | **CT ฉีดสี: Usually appropriate** |
| MRI ± gadolinium | Usually not appropriate | May be appropriate |
"ซับซ้อน" = ไข้ไม่ลง 72 ชม. · sepsis/ช็อก · เบาหวาน ภูมิคุ้มกันต่ำ · สงสัยการอุดกั้นหรือนิ่ว · ไตข้างเดียว · กลับเป็นซ้ำเร็ว
ถ้าไตไม่ดีหรือตั้งครรภ์ เริ่มด้วย **ultrasound** (หาการอุดกั้น/ฝีขนาดใหญ่) แล้วชั่งข้อดีของ CT ฉีดสีเป็นรายไป

### ภาพในเคสนี้ (คำบรรยายภาพจากสไลด์)
[[fig:apn]]
| โรค | Plain film / US (สไลด์) | CT (สไลด์) |
|---|---|---|
| **Emphysematous pyelonephritis** | KUB: **curvilinear gas collection outlining the lower pole** ของไตซ้าย · US: **non-dependent "dirty shadowing" echoes** ในเนื้อไต | **large gas-fluid collections** ในเนื้อไต |
| **Renal abscess (ระยะแรก)** | **enlarged hyperechoic right kidney without mass/stone/HN** | **multiple non-enhancing hypodense lesions** หลายขนาด |
| **Renal abscess (ก้อนเดียว)** | **single complex mixed anechoic–hypoechoic round lesion with posterior enhancement** ที่ขั้วบน | **large round hypodense lesion with thin rim-enhancing wall** |

#### ทำไมภาพถึงออกมาแบบนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ก๊าซในเนื้อไต** | เนื้อเยื่อมีน้ำตาลสูง + ขาดเลือด → E. coli/Klebsiella หมักกลูโคส (mixed-acid fermentation) ได้ **CO₂ และ H₂** · เลือดไหลเวียนน้อยจึงพาก๊าซออกไม่ทัน | **EPN** — ภาวะคุกคามชีวิต · ต้องระบาย ± ตัดไต |
| **ก๊าซบน KUB เป็นเงาดำโค้งรอบไต** | ก๊าซโปร่งรังสีตัดกับ soft tissue ของไต | EPN · แยกจากลมในลำไส้ที่ซ้อนทับด้วย CT |
| **Dirty shadowing ด้านบน** | ก๊าซลอยขึ้น (non-dependent) สะท้อนเสียงเกือบหมดแล้วสะท้อนกลับไปมา → เงาเทาขุ่น ต่างจากเงาดำสะอาดของนิ่ว | EPN vs นิ่ว |
| **ไตโต echo เพิ่ม ยังไม่มีก้อน** | เนื้อไตบวมอักเสบ (phlegmon) ยังไม่กลายเป็นหนองเหลว | ระยะก่อนฝี — CT ช่วยมากกว่า |
| **ก้อนดำปนเทา + posterior enhancement** | เนื้อตายกลายเป็นหนองเหลว (มีเศษเซลล์ให้ echo บ้าง) ของเหลวลดทอนเสียงน้อย | ฝี vs ก้อนเนื้อ (ก้อนเนื้อไม่มี enhancement) |
| **ตรงกลางไม่รับสี ขอบบางรับสี** | หนองไม่มีหลอดเลือด · ผนังเป็น granulation tissue ที่มีหลอดเลือดใหม่และอักเสบ | ลักษณะของฝีทุกอวัยวะ |

**การรักษาที่ภาพกำหนด** — การอุดกั้น → **ระบายด่วน** · ฝีขนาดเล็ก (ราว < 3 ซม.) มักหายด้วยยา ฝีใหญ่ (ราว > 5 ซม.) มักต้อง **เจาะระบายผ่านผิวหนัง** · EPN → ยาปฏิชีวนะ + **ระบายผ่านผิวหนัง** และพิจารณา **ตัดไต** เมื่อก๊าซลามรอบไตหรือมีอวัยวะล้มเหลว (การแบ่งชั้นตาม CT ของ Huang–Tseng 2000)
""",
    ["APN ไม่ซับซ้อน: ไม่ต้องตรวจภาพ · ซับซ้อน/ไข้ไม่ลง 72 ชม.: CT ฉีดสี usually appropriate",
     "ไข้ไม่ลง = ยาเข้าไม่ถึง: การอุดกั้น · ฝี · EPN · เชื้อดื้อยา",
     "EPN: เบาหวาน + เนื้อเยื่อขาดเลือด → เชื้อหมักกลูโคสเป็น CO₂/H₂ · US dirty shadowing · KUB ก๊าซโค้งรอบไต",
     "ฝี: US ดำปนเทา + posterior enhancement · CT hypodense ตรงกลาง + rim enhancement",
     "CT ยืนยัน EPN ได้ดีที่สุด — ระบาย ± ตัดไต"],
    [mcq(N(25), "A 65-year-old diabetic woman with E. coli acute pyelonephritis remains febrile with right flank pain after 72 hours of ceftriaxone to which the organism is susceptible. Her eGFR is 70 mL/min/1.73 m². What is the most appropriate next investigation?",
         ["Repeat urine culture only and continue the same antibiotic", "Contrast-enhanced CT of the abdomen and pelvis", "Intravenous urography", "Plain KUB radiograph only", "DMSA scan"], 1,
         "ไข้ไม่ลงหลังได้ยาที่เชื้อไวต่อยา 72 ชม. = **complicated APN** → ACR (สไลด์): **CT ฉีดสี usually appropriate** เพื่อหา **การอุดกั้น ฝี หรือ EPN** ซึ่งต้องระบาย ไม่ใช่แค่เปลี่ยนยา · eGFR 70 ฉีดสีได้ไม่ต้องป้องกัน\n\n- เพาะเชื้อซ้ำอย่างเดียว — เสียเวลา ไม่ตอบคำถามว่าทำไมยาไม่ได้ผล\n- **IVU** — usually not appropriate\n- **Plain KUB** — อาจเห็นก๊าซหรือนิ่ว แต่ไม่เห็นฝี ไวน้อย\n- **DMSA** — ใช้หาแผลเป็นในเด็กหลังหาย ไม่ใช่ในภาวะเฉียบพลันที่สงสัยฝี",
         "APN ไข้ไม่ลง 72 ชม. → CT ฉีดสี", "Imaging in complicated pyelonephritis", REF("Case 02 — ACR complicated acute pyelonephritis"), ["2.3.14(14)", "B9.2.2(2)", "3.3.20", "2.1.1"]),
     mcq(N(26), "In a poorly controlled diabetic patient with pyelonephritis, renal ultrasound shows bright echogenic foci in the non-dependent part of the renal parenchyma with 'dirty' posterior shadowing. What is the most likely diagnosis?",
         ["Staghorn calculus", "Emphysematous pyelonephritis", "Simple renal cyst", "Medullary nephrocalcinosis", "Angiomyolipoma"], 1,
         "ก๊าซลอยไปอยู่ส่วนบน (**non-dependent**) สะท้อนเสียงเกือบหมดและเกิด reverberation จึงเป็น **dirty shadowing** (สไลด์) — ในผู้ป่วยเบาหวานที่มีกรวยไตอักเสบ = **emphysematous pyelonephritis** ยืนยันด้วย CT\n\n- **นิ่ว/staghorn** — จุดจ้าพร้อม **เงาดำสะอาด (clean shadow)** อยู่ในระบบรวบรวมปัสสาวะ\n- **Simple cyst** — ดำสนิท มี posterior enhancement\n- **Medullary nephrocalcinosis** — pyramid สว่างเป็นรูปสามเหลี่ยมทั้งสองข้าง\n- **Angiomyolipoma** — ก้อนสว่างเพราะไขมัน ไม่มี dirty shadow",
         "Non-dependent echo + dirty shadow = ก๊าซ (EPN)", "Emphysematous pyelonephritis on US", REF("Emphysematous pyelonephritis — dirty shadowing"), ["2.3.14(14)", "B9.2.2(2)"]),
    ], nl=["2.3.14(14)", "B9.2.2(2)", "2.1.1", "3.3.20", "3.2.3"], figs=F11)

# ═════════════════════════════════════════════ 12
def _akickd():
    o = []
    spec = [("ปกติ", 112, 30, "#5c5c5c", True, 8, False, "#262626"),
            ("AKI", 124, 36, "#606060", True, 8, False, "#1a1a1a"),
            ("CKD", 80, 22, "#9a9a9a", False, 4, True, "#8a8a8a")]
    for k, (name, L, H, ctx, cmd, cth, cyst, pyr) in enumerate(spec):
        x = 6 + k * 138; cx, cy = x + 65, 88
        o += [film(x, 26, 130, 116, "#0b0b0b"), FR(x + 1, 27, 128, 18, "#767676", 0), TF(x + 8, 40, "ตับ", "xs b", "#1a1a1a"),
              FE(cx, cy, L / 2, H, ctx, None, "#d8d8d8", 1.4)]
        if cmd:
            for side in (-1, 1):
                for dx in (-0.55, -0.18, 0.18, 0.55):
                    px = cx + dx * L / 2
                    yb = cy + side * (H - cth)
                    ya = cy + side * (H * 0.42)
                    o.append(FP("M%s %s L%s %s L%s %s Z" % (_n(px - 9), _n(yb), _n(px + 9), _n(yb), _n(px), _n(ya)), pyr))
        o.append(FE(cx, cy, L * 0.3, H * 0.3 if k < 2 else H * 0.42, "#c9c9c9"))
        if cyst:
            o += [FC(cx - 26, cy - 10, 5, "#050505", "#cfcfcf", 1), FC(cx + 24, cy + 9, 4, "#050505", "#cfcfcf", 1)]
        o += [FL(cx - L / 2, 136, cx + L / 2, 136, "#e8bb63", 1.6)]
        o += [t(cx, 18, name, "sm b mid")]
    o += [t(71, 158, "10–12 ซม. · CMD ชัด", "xs mid"), t(71, 174, "cortex มืดกว่าตับ", "xs mid mu"),
          t(209, 158, "ขนาดปกติหรือโต · บวมกลม", "xs mid"), t(209, 174, "pyramid มืด/บวมเด่น", "xs mid mu"),
          t(347, 158, "เล็ก · cortex บาง < 10 มม.", "xs mid"), t(347, 174, "สว่างกว่าตับ · CMD หาย", "xs mid mu"),
          t(347, 190, "± ถุงน้ำ · sinus fat มากขึ้น", "xs mid mu")]
    return svg(420, 198, "เปรียบเทียบ ultrasound ไตปกติ ไตวายเฉียบพลัน และไตวายเรื้อรัง", *o)

def _hn():
    o = []
    for g in range(5):
        x = 6 + g * 82; cx, cy = x + 39, 70
        o += [film(x, 22, 78, 98, "#0b0b0b"), FE(cx, cy, 30, 40, "#5c5c5c", None, "#d8d8d8", 1.3)]
        if g == 4:
            o += [FE(cx + 1, cy, 23, 33, "#050505")]
        else:
            o.append(FE(cx + 1, cy, 11, 25, "#c9c9c9"))
            px = cx + 4
            if g == 1:
                o.append(FE(px, cy, 5, 8, "#050505"))
            elif g == 2:
                o += [FL(px, cy, cx - 3, cy - 19, "#050505", 3), FL(px, cy, cx - 3, cy + 19, "#050505", 3),
                      FE(px, cy, 7, 10, "#050505"), FC(cx - 3, cy - 20, 4, "#050505"), FC(cx - 3, cy + 20, 4, "#050505")]
            elif g == 3:
                tips = [(cx - 5, cy - 27), (cx - 13, cy - 10), (cx - 13, cy + 10), (cx - 5, cy + 27)]
                for (a, b) in tips:
                    o.append(FL(px, cy, a, b, "#050505", 5))
                o.append(FE(px, cy, 9, 13, "#050505"))
                for (a, b) in tips:
                    o.append(FC(a, b, 6.5, "#050505"))
        o.append(t(cx, 14, "SFU %d" % g, "sm b mid"))
    lab = [("ไม่ขยาย", ""), ("pelvis", "ขยายเล็กน้อย"), ("pelvis +", "บาง calyx"), ("ทุก calyx", "เนื้อไตยังหนา"), ("+ เนื้อไต", "บางลง")]
    for g, (a, b) in enumerate(lab):
        cx = 6 + g * 82 + 39
        o += [t(cx, 138, a, "xs mid"), t(cx, 153, b, "xs mid mu") if b else ""]
    o.append(t(210, 176, "ดำ = ปัสสาวะค้าง (anechoic) · ยิ่งเกรดสูง ยิ่งกดเนื้อไตให้บาง", "xs mid i2"))
    return svg(420, 184, "ระดับของ hydronephrosis ตาม SFU", *o)

def _level():
    o = []
    titles = [("อุดที่ทางออกกระเพาะ", "ต่อมลูกหมากโต ลิ่มเลือด"), ("อุดท่อไตสองข้าง", "มะเร็งในอุ้งเชิงกราน RPF"), ("อุดท่อไตข้างเดียว", "นิ่ว")]
    for k, (a, b) in enumerate(titles):
        x = 6 + k * 138; cx = x + 65
        dl, dr = (True, True) if k < 2 else (True, False)
        for side, dil in ((-1, dl), (1, dr)):
            kx = cx + side * 34
            o.append(bean(kx, 64, 14, 24, None, 0, -side, cls="ac"))
            o.append(ell(kx - side * 2, 68, 7 if dil else 3, 9 if dil else 4, "wa"))
            if k == 1:
                o += [path("M%s 78 L%s 120" % (_n(kx - side * 4), _n(cx + side * 12)), "lwa w5" if dil else "lwa w2"),
                      path("M%s 120 L%s 136" % (_n(cx + side * 12), _n(cx + side * 8)), "lwa w2"), circ(cx + side * 12, 122, 4, "badf")]
            elif k == 2 and side == -1:
                o += [path("M%s 78 L%s 112" % (_n(kx - side * 4), _n(cx + side * 13)), "lwa w5"), circ(cx + side * 13, 116, 4.5, "inkf"),
                      path("M%s 120 L%s 136" % (_n(cx + side * 13), _n(cx + side * 8)), "lwa w2")]
            else:
                o.append(path("M%s 78 L%s 136" % (_n(kx - side * 4), _n(cx + side * 8)), "lwa w5" if (k == 0) else "lwa w2"))
        o.append(ell(cx, 148, 28 if k == 0 else 16, 18 if k == 0 else 9, "wa"))
        if k == 0: o.append(rect(cx - 8, 164, 16, 10, "badf", 3))
        o += [t(cx, 14, a, "xs b mid"), t(cx, 28, b, "xs mid mu")]
    res = [("HN สองข้าง + กระเพาะโป่ง", "Cr ↑ · ใส่ Foley ก่อน"), ("HN สองข้าง กระเพาะว่าง", "Cr ↑ · PCN / DJ stent"), ("HN ข้างเดียว", "Cr มักปกติ (อีกข้างชดเชย)")]
    for k, (a, b) in enumerate(res):
        cx = 6 + k * 138 + 65
        o += [t(cx, 196, a, "xs b mid"), t(cx, 212, b, "xs mid")]
    return svg(420, 220, "ระดับการอุดกั้นกับภาพ ultrasound และผลต่อ creatinine", *o)

F12 = {"akickd": fig("Ultrasound แยก AKI กับ CKD — ขนาด ความหนา และความสว่างของเนื้อไต",
        "**ปกติ**: ยาว 10–12 ซม. cortex มืดกว่าตับเล็กน้อย เห็น pyramid ชัด · **AKI**: ขนาดปกติหรือโตขึ้น รูปร่างกลมบวม (เนื้อไตบวมน้ำ/อักเสบ) pyramid อาจมืดเด่น · **CKD**: nephron หายไปและถูกแทนที่ด้วยพังผืด → **ไตเล็กลงเรื่อย ๆ** · **cortex บาง (< 10 มม.)** · พังผืดเพิ่มรอยต่อ จึง **สว่างกว่าตับ** · cortex กับ pyramid สว่างพอกันจน **CMD หายไป** · เนื้อไตหดแล้ว **ไขมันใน sinus เข้ามาแทนที่ (sclerolipomatosis)** · อาจมีถุงน้ำ (ตาราง AKI vs CKD ในสไลด์ · Petrucci 2018)",
        _akickd()),
       "hn": fig("Hydronephrosis 5 ระดับ (SFU) — ภาพวาดแนวยาว",
        "สไลด์มีภาพ \"Grading systems of hydronephrosis\" ที่มองไม่เห็นใน handout — ภาพนี้วาดตามระบบ **Society for Fetal Urology (SFU)**: **0** ไม่ขยาย · **1** pelvis ขยายเล็กน้อย · **2** pelvis + calyx บางส่วน · **3** calyx ขยายทุกอัน เนื้อไตยังหนาปกติ · **4** ขยายมากจน **เนื้อไตบาง** · ปัสสาวะที่ค้างเป็นของเหลวใสจึง **ดำ (anechoic)** แทรกเข้าไปใน sinus ที่ปกติสว่าง (ระบบ UTD ก็ใช้ได้ — Onen 2020 ที่อาจารย์อ้าง)",
        _hn()),
       "level": fig("ระดับของการอุดกั้น → ภาพที่เห็น → ทำอะไรก่อน",
        "Creatinine จะขึ้นชัดเมื่อ **ไตทั้งสองข้างถูกอุด** (หรือมีไตข้างเดียว) เพราะไตอีกข้างที่ปกติชดเชยได้ · **อุดที่ทางออกกระเพาะปัสสาวะ** (ต่อมลูกหมากโต ลิ่มเลือด neurogenic bladder ยา anticholinergic) → กระเพาะโป่ง + hydronephrosis สองข้าง → **ใส่สายสวนปัสสาวะทันที** (Mock 182) · **อุดท่อไตสองข้าง** (มะเร็งปากมดลูก/ลำไส้/ต่อมลูกหมากลุกลาม retroperitoneal fibrosis) → กระเพาะว่าง สายสวนไม่ช่วย ต้อง **PCN หรือ DJ stent** · **อุดข้างเดียว** (นิ่ว) → Cr มักปกติ เว้นมีไตข้างเดียวหรือไตเดิมไม่ดี (ไม่อยู่ในสไลด์ — ตำราโรคไต)",
        _level())}

sec("neph-img-12", "Case 03 ไตวาย — แยก AKI กับ CKD และหา postrenal ด้วย ultrasound",
    "เคสสไลด์: ชาย 58 ปี ปัสสาวะน้อย ขาบวม Cr 2.5 · ทำไมไตเรื้อรังเล็กและสว่าง · hydronephrosis 5 ระดับ · อุดกั้นโดยไม่มี HN · HN โดยไม่อุดกั้น", 12,
"""### Case 03 (สไลด์)
ชายไทยอายุ 58 ปี **ปัสสาวะออกน้อยลงและขาบวมเล็กน้อย 7 วัน**
- V/S: BT 36.8 °C · BP 139/85 · PR 80 · RR 16 · PE: **pitting edema 1+** ปอดใส
- Lab: **BUN 63 mg/dL · Cr 2.5 mg/dL** (ไม่มีค่าเดิม)
คำถามที่ ultrasound ตอบได้ทันที: **เฉียบพลันหรือเรื้อรัง?** และ **มีการอุดกั้น (postrenal) ไหม?** — ACR: AKI/CKD → **US usually appropriate**

### Ultrasound ของไตวาย — AKI vs CKD (สไลด์ · Petrucci 2018)
| ลักษณะ | AKI | CKD |
|---|---|---|
| ผิวและขอบ | เรียบ ขอบชัด | อาจขรุขระ ± ถุงน้ำที่เกิดภายหลัง (cortex และ medulla) หรือแบบ ADPKD |
| ขนาด (ความยาว ซม.) | **ปกติ (10–12) หรือโต** | **เล็กลงเรื่อย ๆ** |
| รูปร่างและปริมาตร | **กลม บวม** ปริมาตรปกติหรือเพิ่ม | ลดลงเรื่อย ๆ · **หดเล็กใน ESKD** |
| Echogenicity | ต่างกันตามสาเหตุ | **สว่างขึ้น (hyperechoic) จากพังผืด** |
| Pyramid/medulla | อาจมืด รูปร่างผิดปกติ | **มองไม่เห็น (กลืนเป็นเนื้อเดียว)** |
| Cortex | ต่างกันตามสาเหตุ | **บาง (< 10 มม.)** ± ถุงน้ำ ± cortical nephrocalcinosis |
| Renal sinus | อาจถูกกด/เบียด | **sclerolipomatosis** |
[[fig:akickd]]
#### ทำไมภาพถึงออกมาแบบนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ไตเล็ก cortex บาง** | nephron หายไปทีละน้อย — glomerulosclerosis, tubular atrophy, interstitial fibrosis → เนื้อไตหดตัว | **CKD** · ไตเล็กมากแล้วไม่ควรเจาะชิ้นเนื้อ (ได้แต่พังผืด เลือดออกง่าย) |
| **Cortex สว่างกว่าตับ** | collagen และ glomeruli ที่แข็งตัวเพิ่มรอยต่อสะท้อนเสียง · ท่อไตฝ่อมีน้ำน้อยลง | โรคเนื้อไต (parenchymal disease) — ไวแต่ไม่จำเพาะว่าเป็นโรคอะไร |
| **CMD หาย** | ทั้ง cortex และ pyramid เป็นพังผืดจนความสว่างเท่ากัน | CKD ระยะหลัง |
| **Sinus fat มากขึ้น (sclerolipomatosis)** | เนื้อไตหด ไขมันใน sinus ขยายเข้ามาแทนที่ | CKD เรื้อรังนาน |
| **ไตบวมกลม pyramid มืดเด่น** | เนื้อไตบวมน้ำ/อักเสบเฉียบพลัน (ATN, AIN, GN) · medulla คั่ง | **AKI** |
| **CKD แต่ไตขนาดปกติหรือโต** | โรคที่ "เติม" เนื้อไต: **เบาหวาน** (hyperfiltration + mesangial expansion) · **amyloidosis** · **HIVAN** · **ADPKD** · โรคแทรกซึม (lymphoma) | ไตไม่เล็ก **ไม่ได้ตัด CKD** |
| **สองข้างขนาดต่างกันมาก** | ข้างหนึ่งขาดเลือดหรือมีแผลเป็น | **renal artery stenosis** · reflux nephropathy · ไตเจริญไม่เต็มที่ |

### Postrenal AKI — hydronephrosis
[[fig:hn]]
#### ทำไมถึงมีอาการนี้ (postrenal AKI)
| อาการ/ผลแล็บ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Cr ขึ้น** | ความดันใน tubule และ Bowman's space สูง → **แรงดันกรองสุทธิลด** → GFR ลด · ต่อมา angiotensin II/thromboxane ทำให้หลอดเลือดไตหดตัว | ต้องอุด **สองข้าง** (หรือไตข้างเดียว) Cr จึงขึ้นชัด |
| **Anuria (ไม่มีปัสสาวะเลย)** | อุดสนิทสองข้าง | สาเหตุอื่นของ anuria: cortical necrosis หลอดเลือดแดงไตอุดสองข้าง RPGN รุนแรง |
| **ปัสสาวะปกติหรือมาก** ทั้งที่อุด | อุดบางส่วน — ท่อไตเสียความสามารถในการทำปัสสาวะเข้มข้น (ดื้อ ADH) | ปัสสาวะออกปกติ **ไม่ตัด** การอุดกั้น |
| **K สูง + เลือดเป็นกรด** | ท่อส่วนปลายเสียหายจากความดัน ขับ K และ H⁺ ไม่ได้ (คล้าย type 4 RTA) | พบในอุดกั้นเรื้อรัง |
| **ปัสสาวะออกมากหลังแก้การอุด** | ขับยูเรียและเกลือที่คั่ง (osmotic diuresis) + ท่อไตยังทำปัสสาวะเข้มข้นไม่ได้ | **post-obstructive diuresis** — ต้องดูน้ำและเกลือแร่ใกล้ชิด |
| **บวม** (เคสนี้) | GFR ลด → เกลือและน้ำคั่ง | |
[[fig:level]]

### อุดกั้นโดย "ไม่มี" hydronephrosis (สไลด์)
| ภาวะ | ทำไมท่อไม่ขยาย |
|---|---|
| **Early obstruction** | ช่วงแรกระบบยังขยายไม่ทัน — ตรวจซ้ำได้ |
| **Severe volume depletion / oliguria / anuria** | ปัสสาวะสร้างน้อย ไม่มีน้ำไปดันให้ขยาย |
| **Retroperitoneal fibrosis** ∂ | พังผืดหุ้มรัดท่อไตและ pelvis ไว้ ขยายไม่ได้ |
| **TB KUB** ∂ | ผนังเป็นพังผืด/หินปูน แข็ง ตีบ |
| **Infiltrative / chronic kidney disease** ∂ | เนื้อไตแข็ง หรือก้อนแทรกซึมรอบระบบรวบรวม |
| **Partial obstruction** | ปัสสาวะยังเล็ดลอดผ่านได้ |
∂ = ภาวะเหล่านี้ **ไม่ได้ทำให้เกิด AKI เอง** แต่อาจมี AKI ซ้อนบนภาวะเหล่านี้ (สไลด์) → ถ้าสงสัยการอุดกั้นมาก แม้ US ไม่มี HN ให้ทำ CT หรือ renogram ต่อ

### Hydronephrosis โดย "ไม่มี" การอุดกั้น
สไลด์เตือน **"!! There are conditions causing nonobstructive hydronephrosis"** (ไม่ได้ยกตัวอย่าง — ตำรามาตรฐาน): **vesicoureteric reflux** · **การตั้งครรภ์** (progesterone + มดลูกกด) · **กระเพาะปัสสาวะเต็มมาก** ขณะตรวจ (ให้ปัสสาวะแล้วตรวจซ้ำ) · **ปัสสาวะมาก** (ยาขับปัสสาวะ เบาจืด post-obstructive) · **extrarenal pelvis** · ท่อที่เคยขยายแล้วยังไม่หด · **parapelvic cyst** ที่ดูคล้าย → พิสูจน์ด้วย **diuretic renogram**
""",
    ["US ตรวจแรกใน AKI/CKD: บอกเฉียบพลัน/เรื้อรัง และ postrenal",
     "CKD: ไตเล็ก cortex บาง < 10 มม. สว่างกว่าตับ CMD หาย · AKI: ขนาดปกติ/โต บวมกลม",
     "CKD แต่ไตไม่เล็ก: เบาหวาน amyloid HIVAN ADPKD",
     "อุดกั้นไม่มี HN: ระยะแรก ขาดน้ำ/anuria RPF TB โรคแทรกซึม อุดบางส่วน",
     "HN สองข้าง + กระเพาะโป่ง = bladder outlet obstruction → Foley ก่อน · ระวัง post-obstructive diuresis"],
    [mcq(N(27), "A 58-year-old man has creatinine 2.5 mg/dL with no previous value. Renal ultrasound shows both kidneys measuring 8.2 and 8.4 cm with a cortical thickness of 6 mm, cortex brighter than the liver and loss of corticomedullary differentiation. No hydronephrosis. What is the best interpretation?",
         ["Acute tubular necrosis", "Chronic kidney disease", "Bilateral obstructive uropathy", "Acute interstitial nephritis", "Normal kidneys for age"], 1,
         "ไต **เล็ก (< 9–10 ซม.)** · **cortex บาง (< 10 มม.)** · **สว่างกว่าตับ** · **CMD หาย** = ลักษณะของ **CKD** ตามตาราง AKI vs CKD ในสไลด์ — nephron หายไปและถูกแทนที่ด้วยพังผืด\n\n- **ATN / AIN** — ไตขนาดปกติหรือโต บวม\n- **Obstructive uropathy** — ต้องเห็น hydronephrosis (เว้นภาวะพิเศษ)\n- ไตยาว 8 ซม. cortex 6 มม. **ไม่ใช่ปกติ** แม้ในผู้สูงอายุ",
         "เล็ก บาง สว่าง CMD หาย = CKD", "AKI vs CKD on ultrasound", REF("Ultrasonography of kidney failure — AKI vs CKD"), ["2.3.14(3)", "B9.2.7(2)"]),
     mcq(N(28), "In a patient with long-standing chronic kidney disease (eGFR 18 mL/min/1.73 m²), which underlying disease is most likely to be associated with normal-sized or enlarged kidneys on ultrasound?",
         ["Hypertensive nephrosclerosis", "Chronic glomerulonephritis", "Diabetic kidney disease", "Bilateral chronic pyelonephritis (reflux nephropathy)", "Bilateral renal artery stenosis"], 2,
         "**เบาหวาน** ทำให้ไตโตจาก hyperfiltration และ mesangial expansion ไตจึงมักขนาดปกติหรือโตแม้ GFR ต่ำมาก — กลุ่มเดียวกับ **amyloidosis, HIVAN, ADPKD** และโรคแทรกซึม\n\n- **Hypertensive nephrosclerosis** และ **chronic GN** — ไตหดเล็กสองข้างเท่า ๆ กัน\n- **Reflux nephropathy** — ไตเล็ก ขอบขรุขระเป็นแผลเป็น\n- **Renal artery stenosis** — ไตเล็กจากการขาดเลือด มักไม่เท่ากัน",
         "CKD ไตไม่เล็ก: DM amyloid HIVAN ADPKD", "CKD with large kidneys", ["ตำราโรคไตมาตรฐาน"], ["2.3.14(3)", "B9.2.7(2)"]),
     mcq(N(29), "A 62-year-old man with rising creatinine has CT showing a periaortic soft-tissue mass encasing both ureters, consistent with retroperitoneal fibrosis. Renal ultrasound shows no hydronephrosis. What is the best explanation?",
         ["Retroperitoneal fibrosis never causes obstruction", "The fibrotic tissue encasing the ureters and collecting system prevents them from dilating despite obstruction", "Ultrasound is unable to image the renal pelvis", "The creatinine rise must be pre-renal", "Hydronephrosis only develops in children"], 1,
         "สไลด์ \"Obstruction WITHOUT hydronephrosis\" มี **retroperitoneal fibrosis** — พังผืดหุ้มรัดท่อไตและระบบรวบรวมปัสสาวะไว้ **จนขยายไม่ได้** แม้มีการอุดกั้นจริง (ภาวะอื่นในกลุ่ม: early obstruction · ขาดน้ำรุนแรง/anuria · TB · โรคแทรกซึม/CKD · อุดบางส่วน)\n\n- RPF ทำให้อุดกั้นได้และเป็นสาเหตุสำคัญของ postrenal AKI\n- Ultrasound เห็น renal pelvis ได้ดี\n- ไม่มี HN ไม่ได้แปลว่าต้องเป็น pre-renal\n- Hydronephrosis เกิดได้ทุกวัย",
         "RPF: อุดแต่ท่อขยายไม่ได้", "Obstruction without hydronephrosis", REF("Obstruction WITHOUT hydronephrosis"), ["2.3.14-3(9)", "2.3.14(3)", "B9.2.7(1)"]),
    ], nl=["2.3.14(3)", "B9.2.7(1)", "B9.2.7(2)", "2.3.14-3(9)", "2.1.44", "2.2.28", "2.2.29", "B9.2.3(1)", "2.1.39"], figs=F12)

# ═════════════════════════════════════════════ 13
def _nc():
    o = []
    for k, (name, sub) in enumerate((("ปกติ", "pyramid มืด"), ("Medullary NC", "pyramid สว่าง (กลับด้าน)"), ("Cortical NC", "ขอบ cortex สว่าง"))):
        x = 6 + k * 138; cx, cy = x + 65, 74
        o += [film(x, 26, 130, 100, "#0b0b0b"), FE(cx, cy, 54, 32, "#5c5c5c", None, "#d8d8d8", 1.4)]
        if k == 2:
            o.append(FE(cx, cy, 51, 29, None, None, "#f2f2f2", 3.4))
        for side in (-1, 1):
            for dx in (-30, -10, 10, 30):
                px = cx + dx
                yb = cy + side * 24; ya = cy + side * 11
                col = "#f0f0f0" if k == 1 else "#262626"
                o.append(FP("M%s %s L%s %s L%s %s Z" % (_n(px - 7), _n(yb), _n(px + 7), _n(yb), _n(px), _n(ya)), col))
        o.append(FE(cx, cy, 24, 8, "#c9c9c9"))
        o += [t(cx, 18, name, "sm b mid"), t(cx, 142, sub, "xs mid")]
    o += [t(209, 160, "dRTA · HPT · MSK", "xs mid mu"), t(209, 175, "Dent · Bartter · sarcoidosis", "xs mid mu"),
          t(347, 160, "cortical necrosis", "xs mid mu"), t(347, 175, "chronic GN · rejection · TB", "xs mid mu")]
    return svg(420, 182, "ultrasound ของไตปกติ medullary nephrocalcinosis และ cortical nephrocalcinosis", *o)

def _drta():
    o = [box(80, 6, 260, 42, "bad", "α-intercalated cell ขับ H⁺ ออกไม่ได้\n(distal / type 1 RTA)", "b", 8, 12)]
    cols = [("กรด", [("bx", "H⁺ ค้างในเลือด\nNH₄⁺ ออกน้อย"), ("bx", "HCO₃⁻ 12 · AG 12\n(NAGMA)"), ("ms", "urine pH 7.0\nnet charge +30")]),
            ("โพแทสเซียม", [("bx", "Na ดูดผ่าน ENaC\nต้องแลก K ออก"), ("bx", "volume ลด\naldosterone ↑"), ("bad", "K 2.0 → เซลล์\nhyperpolarize → อ่อนแรง")]),
            ("แคลเซียม", [("bx", "กรดดึง Ca/PO₄\nออกจากกระดูก"), ("bx", "Ca ในปัสสาวะ ↑\ncitrate ↓"), ("ms", "ปัสสาวะด่าง\nCaPO₄ ตกตะกอน")])]
    for c, (h, bl) in enumerate(cols):
        x = 6 + c * 140
        o += [ar(210, 48, x + 64, 66, "lmu", "ah-mu"), t(x + 64, 80, h, "xs b mid i2")]
        for i, (cl, s) in enumerate(bl):
            y = 88 + i * 64
            o.append(box(x, y, 128, 48, cl, s, "", 8, 11))
            if i: o.append(ar(x + 64, y - 16, x + 64, y - 1, "lmu", "ah-mu"))
    o += [ar(70, 266, 150, 288, "lms", "ah-ms"), ar(350, 266, 270, 288, "lms", "ah-ms"),
          box(80, 290, 260, 44, "ms", "medullary nephrocalcinosis + นิ่ว CaPO₄\n(สไลด์ Case 04)", "b", 8, 11.5)]
    return svg(420, 342, "กลไกของ distal RTA ที่ทำให้ K ต่ำ เลือดเป็นกรด และ medullary nephrocalcinosis", *o)

F13 = {"drta": fig("Distal RTA — เซลล์ชนิดเดียวพัง อธิบายได้ทั้งอ่อนแรง เลือดเป็นกรด และหินปูนในไต",
        "**กรด**: ขับ H⁺ ไม่ได้ → NH₄⁺ ในปัสสาวะน้อย (urine net charge Na + K − Cl เป็นบวก) · HCO₃⁻ ถูกใช้หมดไปกับกรดที่สร้างทุกวัน → NAGMA · ปัสสาวะยังเป็นด่าง (pH > 5.5) ทั้งที่เลือดเป็นกรด · **โพแทสเซียม**: Na ที่ดูดกลับทาง ENaC สร้างประจุลบในท่อ ปกติแลกกับ H⁺ เมื่อ H⁺ ออกไม่ได้ K จึงถูกขับแทน ร่วมกับ aldosterone ที่สูงจากการเสียเกลือ → K ต่ำ → เยื่อหุ้มกล้ามเนื้อ hyperpolarize ห่างจาก threshold → **อ่อนแรง** · **แคลเซียม**: กระดูกเป็นบัฟเฟอร์กรด ปล่อย Ca/PO₄ → Ca ในปัสสาวะสูง · กรดเพิ่มการดูดกลับและเผาผลาญ citrate (ตัวยับยั้งผลึก) → citrate ต่ำ · บวกกับปัสสาวะด่าง → **CaPO₄ ตกตะกอนใน medulla** ซึ่งปัสสาวะเข้มข้นที่สุด",
        _drta()),
       "nc": fig("Nephrocalcinosis บน ultrasound — ดูว่า “ส่วนไหน” สว่าง",
        "ปกติ pyramid มืดกว่า cortex · **Medullary nephrocalcinosis**: CaPO₄ สะสมใน pyramid จึง **สว่างกลับด้าน** เป็นสามเหลี่ยมจ้าเรียงรอบ sinus ทั้งสองข้าง (อาจมีเงา) — KUB เห็นจุดหินปูนเป็นกลุ่มตามตำแหน่ง pyramid · **Cortical nephrocalcinosis**: หินปูนจากเนื้อตายที่ cortex (dystrophic) เป็น **ขอบสว่างรอบไต** · สาเหตุตามสไลด์ (Comprehensive Clinical Nephrology 2024) อยู่ใต้ภาพ — hyperoxaluria เป็นได้ทั้งสองแบบ",
        _nc())}

sec("neph-img-13", "Case 04 อ่อนแรงจาก K ต่ำ — distal RTA และ medullary nephrocalcinosis",
    "เคสสไลด์: ชาย 30 ปี อ่อนแรงต้นแขนต้นขา K 2.0 HCO₃ 12 urine pH 7 net charge +30 · ทำไม pyramid สว่าง · สาเหตุ medullary vs cortical NC", 9,
"""### Case 04 (สไลด์)
ชายไทยอายุ 30 ปี **อ่อนแรงต้นแขนต้นขา 3 ชม.**
- V/S: BT 36.4 °C · BP 121/76 · PR 60 · RR 16 · PE: **proximal muscle weakness grade III ทุกแขนขา** · DTR 2+
- Lab: Cr 1.0 · **K 2.0 mEq/L** · **HCO₃⁻ 12 mEq/L** · **AG 12 mEq/L**
- UA: **pH 7.0** · bland sediment · **urine K 40 mmol/L** · **urine net charge +30**
- ภาพ: **"Medullary nephrocalcinosis"**

**แปลผลทีละขั้น**
1. HCO₃⁻ 12 + AG 12 (ปกติ) → **normal anion gap metabolic acidosis (NAGMA)**
2. Urine net charge (Na + K − Cl) **+30 (บวก)** → NH₄⁺ ในปัสสาวะต่ำ → **ไตขับกรดไม่ได้** (ถ้าเสีย HCO₃⁻ ทางลำไส้ ไตจะขับ NH₄⁺ มาก ค่านี้จะเป็นลบ)
3. Urine pH **7.0** ทั้งที่เลือดเป็นกรด → ทำปัสสาวะให้เป็นกรดไม่ได้ = **distal (type 1) RTA**
4. Urine K **40 mmol/L** ขณะ K เลือด 2.0 → **เสีย K ทางไต**
5. **Medullary nephrocalcinosis** → เข้ากับ distal RTA
สาเหตุ dRTA ในผู้ใหญ่: Sjögren syndrome และโรคภูมิคุ้มกันตนเอง · ยา (amphotericin B, lithium) · กรรมพันธุ์ (เช่น SLC4A1) — **ในไทยเป็นสาเหตุสำคัญของ hypokalemic paralysis**

#### ทำไมถึงมีอาการนี้
[[fig:drta]]
| อาการ/ผลแล็บ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **อ่อนแรงต้นแขนต้นขา** | K นอกเซลล์ต่ำ → resting membrane potential ติดลบมากขึ้น (hyperpolarize) ห่างจาก threshold → กล้ามเนื้อกระตุ้นยาก · กล้ามเนื้อมัดใหญ่ส่วนต้นได้รับผลก่อน | hypokalemic paralysis — แยกจาก periodic paralysis ด้วย **urine K สูง + เลือดเป็นกรด** |
| **K 2.0 กับ urine K 40** | H⁺-ATPase ของ α-intercalated cell เสีย → ประจุลบในท่อจากการดูด Na ถูกถ่วงด้วยการขับ K แทน H⁺ + aldosterone สูงจากการเสียเกลือ | dRTA และ proximal RTA = K ต่ำ · **type 4 RTA = K สูง** |
| **HCO₃⁻ 12 · AG ปกติ** | ขับกรดที่ร่างกายสร้างทุกวันไม่ได้ → HCO₃⁻ ถูกใช้ไป Cl⁻ คั่งแทน | NAGMA |
| **Urine pH 7.0** | สร้าง gradient ของ H⁺ ในท่อไม่ได้ | **dRTA: pH > 5.5 เสมอ** · proximal RTA ทำ pH < 5.5 ได้เมื่อ HCO₃⁻ ต่ำมาก |
| **Urine net charge +30** | NH₄⁺ (ประจุบวกที่ไม่ได้วัด) ออกน้อย Na + K จึงมากกว่า Cl | บวก = ไตเป็นเหตุ · ลบ = เสีย HCO₃⁻ ทางลำไส้ |
| **Ca ในปัสสาวะสูง · citrate ต่ำ** | กระดูกปล่อย Ca/PO₄ มาบัฟเฟอร์กรด · กรดเพิ่มการดูดกลับ citrate ที่ proximal tubule | สองปัจจัยเสี่ยงหลักของนิ่ว |

#### ทำไมภาพถึงออกมาแบบนี้
[[fig:nc]]
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Pyramid สว่างทั้งสองข้าง (US)** | CaPO₄ ตกตะกอนใน interstitium และท่อของ medulla ซึ่งปัสสาวะถูกทำให้เข้มข้นที่สุด (countercurrent) และเป็นด่างใน dRTA · ผลึกเพิ่มรอยต่อสะท้อนเสียง → pyramid ที่ปกติมืดกลับสว่าง | **medullary nephrocalcinosis** |
| **จุดหินปูนเป็นกลุ่มตามตำแหน่ง pyramid (KUB)** | ผลึกแคลเซียมดูดกลืนรังสี | ต่างจากนิ่วที่อยู่ใน calyx/pelvis |
| **ขอบ cortex สว่าง** | หินปูนสะสมในเนื้อตายของ cortex (dystrophic calcification) | **cortical nephrocalcinosis** — cortical necrosis เป็นต้น |

### สาเหตุของ nephrocalcinosis (สไลด์)
| Medullary | Cortical |
|---|---|
| Hyperparathyroidism | Cortical necrosis |
| **Distal RTA** | Chronic glomerulonephritis |
| Medullary sponge kidney | Transplant rejection |
| Dent disease | Renal tuberculosis |
| Bartter syndrome | Renal trauma |
| Sarcoidosis | |
| **Hyperoxaluria** — มักเป็นทั้งสองแบบ | |
การรักษา dRTA: **potassium citrate** (แก้ทั้งกรด K ต่ำ และ citrate ต่ำ → ลดการเกิดนิ่ว) · ให้ K ทางหลอดเลือดก่อนแก้กรดเมื่อ K ต่ำมาก (แก้กรดก่อน K จะเข้าเซลล์ ยิ่งต่ำลง)
""",
    ["dRTA: NAGMA + urine pH > 5.5 + urine net charge บวก + K ต่ำ (urine K สูง)",
     "อ่อนแรงจาก K ต่ำ: membrane hyperpolarize ห่าง threshold",
     "Medullary NC: CaPO₄ ตกใน pyramid (ปัสสาวะด่าง Ca สูง citrate ต่ำ) → pyramid สว่างกลับด้าน",
     "Medullary NC: HPT · dRTA · MSK · Dent · Bartter · sarcoidosis · Cortical NC: cortical necrosis · chronic GN · rejection · TB · trauma",
     "รักษา dRTA ด้วย potassium citrate · K ต่ำมากให้ K ก่อนแก้กรด"],
    [mcq(N(30), "A 30-year-old man has proximal weakness. K 2.0 mEq/L, HCO₃⁻ 12 mEq/L, anion gap 12, urine pH 7.0, urine net charge (Na + K − Cl) +30 and bilateral echogenic medullary pyramids on ultrasound. What is the most likely diagnosis?",
         ["Proximal (type 2) renal tubular acidosis", "Distal (type 1) renal tubular acidosis", "Type 4 (hyperkalaemic) renal tubular acidosis", "Chronic diarrhoea", "Hypokalaemic periodic paralysis due to thyrotoxicosis"], 1,
         "NAGMA + **urine pH > 5.5** + **urine net charge บวก** (NH₄⁺ ต่ำ) + **เสีย K ทางไต** + **medullary nephrocalcinosis** = **distal (type 1) RTA** (เคส 04 ในสไลด์)\n\n- **Proximal RTA** — ทำปัสสาวะเป็นกรดได้เมื่อ HCO₃⁻ ต่ำมาก (pH < 5.5) และ **ไม่ค่อยเกิดนิ่ว/nephrocalcinosis** เพราะ citrate ในปัสสาวะไม่ต่ำ\n- **Type 4 RTA** — **K สูง**\n- **ท้องเสียเรื้อรัง** — ไตขับ NH₄⁺ มาก urine net charge **เป็นลบ**\n- **Thyrotoxic periodic paralysis** — K เข้าเซลล์ ไม่มีเลือดเป็นกรด urine K ต่ำ",
         "NAGMA + urine pH > 5.5 + UAG บวก + NC = dRTA", "Distal RTA", REF("Case 04 — medullary nephrocalcinosis"), ["2.3.14-3(12)", "B9.2.5(2)", "2.3.4(2)", "2.1.22"]),
     mcq(N(31), "Which condition characteristically causes cortical rather than medullary nephrocalcinosis?",
         ["Distal renal tubular acidosis", "Medullary sponge kidney", "Primary hyperparathyroidism", "Acute cortical necrosis", "Bartter syndrome"], 3,
         "**Cortical necrosis** — เนื้อ cortex ตายแล้วมีหินปูนสะสมแบบ dystrophic เห็นเป็นขอบสว่างรอบไต (สาเหตุ cortical อื่นตามสไลด์: chronic GN · transplant rejection · renal TB · renal trauma)\n\n**Distal RTA · medullary sponge kidney · hyperparathyroidism · Bartter** อยู่ในกลุ่ม **medullary** ทั้งหมด เพราะกลไกคือ Ca ในปัสสาวะสูงและตกตะกอนใน pyramid ที่ปัสสาวะเข้มข้นที่สุด · **hyperoxaluria** เป็นได้ทั้งสองแบบ",
         "Cortical NC = cortical necrosis", "Nephrocalcinosis patterns", REF("Nephrocalcinosis — etiologies"), ["2.3.14-3(12)", "B9.2.5(2)"]),
    ], nl=["2.3.14-3(12)", "B9.2.5(2)", "2.3.4(2)", "2.1.22", "B9.1.2(6)", "B9.3(5)"], figs=F13)

# ═════════════════════════════════════════════ 14
def _adpkd():
    o = [bean(78, 132, 52, 96, None, 0, 1, cls="ac")]
    for (x, y, r) in ((50, 70, 14), (82, 60, 10), (62, 102, 11), (40, 134, 16), (76, 140, 12), (54, 176, 13), (86, 192, 9), (100, 110, 8), (66, 214, 8)):
        o.append(circ(x, y, r, "wa"))
    o += [circ(92, 164, 12, "bad"), t(78, 246, "ไตโต ถุงน้ำหลายขนาด", "xs mid"), t(78, 260, "(สีแดง = เลือดออกในถุง)", "xs mid mu")]
    chain = [("bx", "PKD1/PKD2 → polycystin ผิดปกติ\nที่ cilia ของเซลล์ท่อไต"), ("bx", "Ca²⁺ ในเซลล์ ↓ → cAMP ↑\n(vasopressin V2 เสริม)"),
             ("ms", "เซลล์แบ่งตัว + หลั่งน้ำเข้าถุง (CFTR)\nถุงน้ำโต กดเนื้อไตปกติ")]
    for i, (c, s) in enumerate(chain):
        y = 6 + i * 54
        o.append(box(170, y, 244, 42, c, s, "", 8, 11))
        if i: o.append(ar(292, y - 12, 292, y - 1, "lmu", "ah-mu"))
    outs = [("bad", "ปวดสีข้างถ่วง ๆ · คลำได้ก้อน", "ปลอกไตถูกยืด"), ("bad", "ปวดเฉียบพลัน + ปัสสาวะเป็นเลือด", "ถุงแตก/เลือดออก · นิ่ว · ติดเชื้อ"),
            ("ms", "ความดันสูง (ก่อน GFR ลด)", "ถุงกดหลอดเลือดในไต → ขาดเลือด → RAAS"),
            ("ms", "GFR ลดช้า ๆ → ESKD", "เนื้อไตถูกกดและเป็นพังผืด"), ("bx", "นอกไต", "ถุงน้ำตับ · aneurysm ในสมอง · MVP")]
    o += [line(292, 156, 292, 162, "lmu"), line(178, 162, 292, 162, "lmu"), line(178, 162, 178, 391, "lmu")]
    for i, (c, a, b) in enumerate(outs):
        y = 172 + i * 46
        o += [rect(190, y, 224, 38, c, 8), t(198, y + 16, a, "xs b"), t(198, y + 31, b, "xs i2"), ar(178, y + 19, 189, y + 19, "lmu", "ah-mu")]
    o += [box(6, 406, 408, 34, "ok", "tolvaptan (V2 antagonist) ลด cAMP → ชะลอการโตของถุงน้ำ", "", 8, 11.5)]
    return svg(420, 448, "กลไกของ ADPKD จากยีนถึงอาการ", *o)
F14 = {"adpkd": fig("ADPKD — ถุงน้ำโตอธิบายอาการเกือบทั้งหมด",
        "ยีน **PKD1/PKD2** สร้าง polycystin ที่ขนรับความรู้สึก (primary cilia) ของเซลล์ท่อไต · เมื่อผิดปกติ Ca²⁺ ในเซลล์ลดและ **cAMP สูง** (vasopressin ผ่าน V2 receptor กระตุ้นเพิ่ม) → เซลล์แบ่งตัวและหลั่งน้ำเข้าถุงผ่าน CFTR → ถุงน้ำโตเรื่อย ๆ · ผลที่ตามมา: **ไตโตคลำได้ ปวดถ่วง** (ปลอกไตยืด) · **ปวดเฉียบพลัน + ปัสสาวะเป็นเลือด** (ถุงแตกหรือเลือดออกในถุง นิ่ว ติดเชื้อ) · **ความดันสูงตั้งแต่ GFR ยังปกติ** (ถุงกดหลอดเลือดในไต → ขาดเลือดเฉพาะที่ → renin–angiotensin) · **GFR ลดช้า ๆ** · นอกไต: ถุงน้ำตับ หลอดเลือดสมองโป่งพอง (Mock 175: บิดาเสียชีวิตจาก aneurysm แตก) · **tolvaptan** ยับยั้ง V2 จึงลด cAMP (ไม่อยู่ในสไลด์ — KDIGO 2025 ADPKD)",
        _adpkd())}

sec("neph-img-14", "ADPKD ถุงน้ำ และก้อนในไต — ภาพบอกอะไร",
    "ไม่อยู่ในสไลด์ (เติมเพราะมีใน Mock): กลไกอาการ ADPKD · เกณฑ์ ultrasound (Pei–Ravine) · simple vs complex cyst (Bosniak) · ไขมันในก้อน = AML", 9,
"""> สไลด์กล่าวถึง ADPKD เพียงในตาราง AKI vs CKD ("ADPKD appearance") — หัวข้อนี้เติมเพราะข้อสอบ Mock ถามการวินิจฉัย ADPKD จาก ultrasound · อ้างอิง **KDIGO 2025 ADPKD guideline** · Pei–Ravine criteria · Bosniak 2019

### ADPKD — ทำไมถึงมีอาการนี้
[[fig:adpkd]]
| อาการ/อาการแสดง | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ไตโตสองข้าง คลำได้ ปวดถ่วง** | ถุงน้ำหลายพันถุงโตขึ้นเรื่อย ๆ ปลอกไตถูกยืด | ไตโตสองข้าง + ถุงน้ำหลายถุง ≠ simple cyst |
| **ปวดเฉียบพลัน + ปัสสาวะเป็นเลือด** | ถุงแตกเข้าระบบรวบรวมปัสสาวะ หรือเลือดออกในถุง · นิ่ว (uric acid/Ca oxalate พบบ่อยขึ้น) · ถุงติดเชื้อ | ถุงติดเชื้อ: ไข้ ปวดเฉพาะที่ — ยาที่ละลายในไขมันเข้าถุงได้ดีกว่า |
| **ความดันโลหิตสูงตั้งแต่อายุน้อย ก่อน GFR ลด** | ถุงกดหลอดเลือดในไต → เนื้อไตขาดเลือดเฉพาะที่ → **renin–angiotensin ทำงานมากขึ้น** | ใช้ ACEi/ARB เป็นยาหลัก |
| **GFR ลดช้าแล้วเร็วขึ้น** | เนื้อไตปกติถูกกด + พังผืด · GFR คงที่ได้นานเพราะ nephron ที่เหลือชดเชย จนปริมาตรไตโตมากแล้ว | ใช้ **ปริมาตรไต (htTKV) จาก MRI** ทำนายการดำเนินโรค (Mayo class) ตาม KDIGO 2025 |
| **ปวดศีรษะรุนแรงทันที** | **intracranial aneurysm** แตก (polycystin ในผนังหลอดเลือด) | ประวัติครอบครัว aneurysm → พิจารณาคัดกรองด้วย MRA |
| **ถุงน้ำในตับ** | polycystin ในเซลล์ท่อน้ำดีด้วย | พบบ่อยมาก โดยเฉพาะหญิง |

### ภาพของ ADPKD
- **Ultrasound** (ตรวจแรก): ไตโตสองข้าง ถุงน้ำ **anechoic** หลายขนาด มี posterior enhancement · ถุงที่มีเลือดออกมี echo ภายใน · มักเห็นถุงน้ำในตับ
- **เกณฑ์ ultrasound ในผู้ที่มีประวัติครอบครัว (Pei–Ravine unified criteria)**
| อายุ | วินิจฉัยเมื่อ |
|---|---|
| 15–39 ปี | ถุงน้ำ **≥ 3 ถุง** (ข้างเดียวหรือสองข้างรวมกัน) |
| 40–59 ปี | ถุงน้ำ **≥ 2 ถุงในแต่ละข้าง** |
| ≥ 60 ปี | ถุงน้ำ **≥ 4 ถุงในแต่ละข้าง** |
อายุ ≥ 40 ปีที่มีถุงน้ำน้อยกว่า 2 ถุง แทบตัด ADPKD ได้ · **MRI** ไวกว่าสำหรับถุงเล็กและใช้วัดปริมาตรไต

### ถุงน้ำธรรมดา vs ถุงน้ำซับซ้อน vs ก้อนเนื้อ
#### ทำไมภาพถึงออกมาแบบนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ดำสนิท ผนังบางเรียบ + posterior enhancement (US)** · **0–20 HU ไม่รับสี (CT)** | น้ำใสเนื้อเดียว ไม่มีหลอดเลือดภายใน | **simple cyst (Bosniak I)** — พบบ่อยตามอายุ ไม่ต้องติดตาม |
| **ผนังหนา/ผนังกั้นหนา ขรุขระ ที่รับสี** | มีเนื้อเยื่อที่มีหลอดเลือดอยู่ในผนัง | Bosniak III — โอกาสมะเร็งสูงขึ้นมาก |
| **ก้อนเนื้อในถุงที่รับสี** | เนื้องอกโตเข้าไปในถุง | Bosniak IV — คิดเป็นมะเร็ง |
| **ก้อนเนื้อที่รับสี ≥ 20 HU** | เนื้องอกมีหลอดเลือด | **renal cell carcinoma** จนกว่าจะพิสูจน์ได้ว่าไม่ใช่ — ส่วนใหญ่พบโดยบังเอิญ triad (ปวดสีข้าง ปัสสาวะเป็นเลือด ก้อน) พบน้อย |
| **ก้อนที่มี HU ติดลบ (ไขมัน)** | มีเซลล์ไขมันในก้อน | **angiomyolipoma** — US เป็นก้อนสว่างจ้าเพราะไขมันสร้างรอยต่อมาก (แต่ RCC เล็กก็สว่างได้ ต้อง CT/MRI ยืนยันไขมัน) |
""",
    ["ADPKD: PKD1/2 → cAMP ↑ → ถุงน้ำโต · ไตโต ปวด ปัสสาวะเป็นเลือด ความดันสูงก่อน GFR ลด",
     "HT ใน ADPKD: ถุงกดหลอดเลือด → ขาดเลือดเฉพาะที่ → RAAS",
     "Pei–Ravine: 15–39 ปี ≥ 3 ถุง · 40–59 ปี ≥ 2 ถุง/ข้าง · ≥ 60 ปี ≥ 4 ถุง/ข้าง",
     "Simple cyst: anechoic ผนังบาง posterior enhancement · CT 0–20 HU ไม่รับสี",
     "ไขมันในก้อน (HU ติดลบ) = angiomyolipoma · ก้อนรับสี = RCC จนกว่าจะพิสูจน์"],
    [mcq(N(32), "A 34-year-old woman with ADPKD has blood pressure 150/95 mmHg while her eGFR is still 95 mL/min/1.73 m². What is the main mechanism of hypertension at this stage?",
         ["Reduced GFR causing sodium retention", "Expanding cysts compress intrarenal vessels, causing regional ischaemia and activation of the renin–angiotensin system", "Primary hyperaldosteronism from an adrenal adenoma", "Coarctation of the aorta associated with ADPKD", "Renal artery stenosis from fibromuscular dysplasia"], 1,
         "ใน ADPKD ความดันสูง **เกิดก่อน GFR ลด** เพราะถุงน้ำที่โตขึ้น **กดหลอดเลือดในไต** → เนื้อไตบางส่วนขาดเลือด → **renin–angiotensin ทำงานมากขึ้น** → จึงใช้ ACEi/ARB เป็นยาหลัก (KDIGO 2025)\n\n- **GFR ลดทำให้เกลือคั่ง** — ยังไม่เกิดเมื่อ eGFR 95\n- **Primary aldosteronism / coarctation / FMD** — ไม่ใช่กลไกของ ADPKD (ADPKD สัมพันธ์กับ intracranial aneurysm และ MVP ไม่ใช่ coarctation)",
         "HT ใน ADPKD = ถุงกดหลอดเลือด → RAAS", "Hypertension in ADPKD", ["KDIGO 2025 ADPKD guideline (ไม่อยู่ในสไลด์)"], ["B9.2.1-3(1)", "B9.1.2(8)"]),
     mcq(N(33), "A 4-cm well-defined renal mass is found incidentally. Non-contrast CT shows regions measuring −60 HU within the mass. What is the most likely diagnosis?",
         ["Renal cell carcinoma, clear-cell type", "Angiomyolipoma", "Simple renal cyst", "Renal abscess", "Transitional cell carcinoma of the renal pelvis"], 1,
         "**HU ติดลบ (−60) = ไขมัน** — ก้อนในไตที่มีไขมันชัดเจนแทบทั้งหมดคือ **angiomyolipoma** (เนื้องอกไม่ร้ายที่มีหลอดเลือด กล้ามเนื้อเรียบ และไขมัน) · บน ultrasound จึงเป็นก้อน **สว่างจ้า** เพราะไขมันสร้างรอยต่อมาก\n\n- **RCC** — ก้อนเนื้อที่รับสี ไม่มีไขมันชัดเจน (ส่วนน้อยมาก)\n- **Simple cyst** — 0–20 HU\n- **ฝี** — ตรงกลางเป็นของเหลว (ค่าบวก) ขอบรับสี มีไข้\n- **TCC** — อยู่ใน pelvis เป็น filling defect",
         "ไขมันในก้อนไต = AML", "Fat-containing renal mass", ["ตำรารังสีมาตรฐาน (ไม่อยู่ในสไลด์)"], ["B9.2.4-3(1)", "B9.2.4-3(2)", "3.3.20"]),
    ], nl=["B9.2.1-3(1)", "2.1.43", "2.1.21", "B9.2.4-3(1)", "B9.2.4-3(2)", "B9.1.2(8)"], figs=F14,
    src="KDIGO 2025 ADPKD · Pei–Ravine criteria · Bosniak 2019 (ไม่อยู่ในสไลด์ — สไลด์กล่าวถึง ADPKD ในตาราง AKI vs CKD)")

# ── END SECTIONS


# ═════════════════════════════════════════════ ประกอบคาบ
LECNAME = "Essential Renal Imaging (อ.ธนิศร)"
MEQ = [{"id": "NEPH-IMG-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Obstructed infected kidney from a ureteric stone — imaging choice, decompression, contrast risk and stone type",
 "vignette": """ผู้ป่วยชายไทยอายุ 62 ปี มาห้องฉุกเฉินด้วยปวดบั้นเอวซ้าย 1 วัน
PI: ปวดบิดเป็นพัก ๆ ร้าวลงขาหนีบซ้าย คลื่นไส้อาเจียน 3 ครั้ง 6 ชม. ก่อนมามีไข้หนาวสั่น ปัสสาวะขุ่น
PH: เบาหวานชนิดที่ 2 ใช้ metformin 1,000 มก./วัน · ความดันโลหิตสูง · gout · เคยปวดแบบนี้เมื่อ 2 ปีก่อน ถ่ายภาพรังสีแล้ว "ไม่เห็นนิ่ว"
PE: BT 38.9 °C, BP 98/60 mmHg, PR 118/min, RR 24/min · left CVA tenderness · ท้องนุ่ม ไม่มีก้อน
Lab: Cr 2.1 mg/dL (3 เดือนก่อน 1.1) · UA: pH 5.0, WBC > 100/HPF, RBC 20–30/HPF, nitrite positive · serum uric acid 9.2 mg/dL""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัยเบื้องต้น และอธิบายกลไกที่ทำให้ปวดร้าวลงขาหนีบและคลื่นไส้อาเจียน (3 คะแนน)",
   "a": """**การวินิจฉัย**: นิ่วท่อไตซ้ายอุดกั้น ร่วมกับ **กรวยไตอักเสบเหนือการอุดกั้น (obstructed infected kidney) + sepsis** และ **AKI** (Cr 1.1 → 2.1)
**ปวดร้าวลงขาหนีบ**: ท่อไตบีบไล่นิ่วที่ติดจุดแคบ ความดันในระบบรวบรวมสูง ปลอกไตถูกยืด → ใยประสาทอวัยวะภายในเข้าไขสันหลัง **T11–L2** ระดับเดียวกับผิวหนังสีข้าง ขาหนีบ และ genitofemoral nerve → **referred pain**
**คลื่นไส้อาเจียน**: ไตและทางเดินอาหารส่งสัญญาณผ่าน **celiac/splanchnic ganglion ร่วมกัน** → reflex ทางเดินอาหาร"""},
  {"q": "2. จะส่งตรวจภาพอะไรเป็นอย่างแรก เพราะอะไร และทำไมภาพรังสีเมื่อ 2 ปีก่อนจึง \"ไม่เห็นนิ่ว\" (3 คะแนน)",
   "a": """**CT KUB ไม่ฉีดสี (low-dose)** — ACR: **usually appropriate** ในสงสัยนิ่ว · sens 97% spec 95% · บอกขนาด ตำแหน่ง hydronephrosis และภาวะแทรกซ้อน · **ไม่ฉีดสี** เพราะ contrast ที่ขับออกมาขาวพอ ๆ กับนิ่วจะบังนิ่ว และผู้ป่วยมี AKI
(ultrasound ข้างเตียงทำได้ทันทีเพื่อดู hydronephrosis แต่เห็นท่อไตไม่ดี)
**KUB ไม่เห็นนิ่ว**: KUB ไวเพียง **29%** และนิ่ว **uric acid** (C H N O ล้วน) **โปร่งรังสี** — ผู้ป่วยนี้มี gout uric acid สูง ปัสสาวะ pH 5.0 จึงน่าจะเป็นนิ่วกรดยูริก ซึ่ง **CT เห็นได้**"""},
  {"q": "3. CT ไม่ฉีดสีพบนิ่ว 7 มม. ที่ท่อไตซ้ายส่วนต้น มี soft tissue rim sign, moderate hydronephrosis และ perinephric fat stranding — จงอธิบายสิ่งที่เห็นและบอกการรักษาเร่งด่วน (3 คะแนน)",
   "a": """**Soft tissue rim sign** = ผนังท่อไตบวมรอบนิ่ว ยืนยันว่านิ่วอยู่ **ในท่อไต** (ไม่ใช่ phlebolith) · **Hydronephrosis** = ปัสสาวะค้างเหนือจุดอุด · **Fat stranding** = ความดันสูงจน fornix รั่ว/น้ำเหลืองคั่ง
**รักษาเร่งด่วน**: resuscitation (IV fluid) + **IV antibiotic** ภายในชั่วโมงแรก + **ระบายระบบรวบรวมปัสสาวะด่วน (PCN หรือ DJ stent)** — ยาปฏิชีวนะอย่างเดียวไม่พอ เพราะหนองอยู่ใต้ความดันในระบบที่อุด · **ยังไม่ทำ ESWL/เอานิ่วออก** จนหายติดเชื้อ · ยา NSAID เลี่ยงไว้เพราะมี AKI"""},
  {"q": "4. หลังใส่ PCN 3 วันยังมีไข้ แพทย์อยากทำ CT ฉีดสีเพื่อหาฝี Cr ล่าสุด 2.4 mg/dL — จงประเมินความเสี่ยงต่อไตและบอกการเตรียมผู้ป่วย รวมถึงเรื่อง metformin (3 คะแนน)",
   "a": """**ความเสี่ยง**: ผู้ป่วยมี **AKI** = กลุ่มที่เสี่ยง CI-AKI สูงสุด (ACR–NKF 2020 ถือเหมือน eGFR < 30)
**ทำอะไรก่อน**: ชั่งประโยชน์ — ถ้าคำถามคือฝี/การอุดที่เหลือ อาจเริ่มด้วย **ultrasound** ก่อน · ถ้าจำเป็นต้อง CT จริง **อย่างดการตรวจที่จำเป็น** แต่ให้ **IV isotonic fluid (NSS) ก่อนและหลังฉีด** (ESUR: 1 mL/kg/h 3–4 ชม. ก่อน และ 4–6 ชม. หลัง) · ใช้ contrast ปริมาณน้อยที่สุดชนิด low/iso-osmolar · งด NSAID/ยาที่ทำร้ายไต · **ไม่ใช้** furosemide NAC หรือฟอกเลือดป้องกัน
**Metformin**: มี AKI → **หยุด** (ควรหยุดตั้งแต่รับไว้เพราะ sepsis + AKI) และเริ่มใหม่เมื่อไตคงที่ ≥ 48 ชม. หลังฉีด — เพราะยาขับทางไต ถ้าไตแย่ลงจะสะสมจน lactic acidosis"""},
  {"q": "5. ผลวิเคราะห์นิ่วเป็น uric acid จงอธิบายว่าทำไมผู้ป่วยรายนี้เกิดนิ่วชนิดนี้ และให้คำแนะนำป้องกัน (3 คะแนน)",
   "a": """**กลไก**: กรดยูริกมี pKa ราว 5.5 — ผู้ป่วย **เบาหวาน/metabolic syndrome** มีภาวะดื้ออินซูลินที่ลดการสร้าง NH₄⁺ ของไต ปัสสาวะจึง **เป็นกรดตลอด (pH 5.0)** กรดยูริกอยู่ในรูปไม่แตกตัวที่ละลายน้ำได้น้อย → ตกผลึก · ร่วมกับ gout/กรดยูริกสูง
**ป้องกัน**: ดื่มน้ำให้ปัสสาวะ > 2 ลิตร/วัน · **ทำปัสสาวะให้เป็นด่าง** ด้วย potassium citrate (เป้า pH 6.5–7) — uric acid เป็น **นิ่วชนิดเดียวที่ละลายด้วยยาได้** · ลดเนื้อสัตว์/เครื่องใน · allopurinol ถ้ากรดยูริกในเลือด/ปัสสาวะสูง · **ห้ามใช้ probenecid** (เพิ่มการขับกรดยูริกทางปัสสาวะ ยิ่งเกิดนิ่ว) · ติดตามด้วย CT/US (KUB มองไม่เห็นนิ่วชนิดนี้)"""}],
 "ref": ["สไลด์ อ.ธนิศร — Case 01, ACR flank pain, CT of kidney stone", "ACR–NKF consensus 2020 · ESUR 2018 · EAU Urolithiasis 2025"],
 "nl": ["2.3.14-3(15)", "2.3.14(14)", "2.3.14(3)", "3.3.20", "B9.2.3-3(1)"],
 "years": [], "_kind": "meq", "_set": "nephro"}]

OSCE = [{"id": "NEPH-IMG-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "SAQ – Interpreting five renal imaging reports",
 "station": "SAQ (เขียนตอบ) 5 นาที",
 "instruction": """จงอ่านรายงานผลตรวจภาพต่อไปนี้ แล้วเขียน **(ก) การวินิจฉัยที่น่าจะเป็นที่สุด** และ **(ข) สิ่งที่ควรทำต่อหนึ่งอย่าง** ของแต่ละราย

1. ชาย 45 ปี ปวดบิดสีข้างขวาร้าวลงขาหนีบ · **Plain KUB ไม่พบเงาทึบ** · CT ไม่ฉีดสี: นิ่ว 5 มม. ที่ท่อไตขวาส่วนปลาย มี soft tissue rim sign, mild hydronephrosis · urine pH 5.0
2. ชาย 66 ปี Cr 3.8 mg/dL ไม่ทราบค่าเดิม · US: ไตยาว 8.1 และ 8.4 ซม. cortex หนา 6 มม. **สว่างกว่าตับ** ไม่เห็น corticomedullary differentiation ไม่มี hydronephrosis
3. ชาย 72 ปี ไม่มีปัสสาวะ 24 ชม. ปวดท้องน้อย Cr 4.5 mg/dL · US: **moderate hydronephrosis สองข้าง** กระเพาะปัสสาวะโป่งมาก ต่อมลูกหมากโต
4. หญิงเบาหวาน 60 ปี กรวยไตอักเสบ ไข้ไม่ลงหลังยา 4 วัน · US: ก้อนกลม **complex anechoic–hypoechoic มี posterior enhancement** ที่ขั้วบนไตขวา · CT: hypodense lesion มี **thin rim enhancement**
5. หญิง 28 ปี อ่อนแรง K 2.6 mEq/L HCO₃⁻ 14 mEq/L AG ปกติ urine pH 6.8 · US: **pyramid สว่างทั้งสองข้าง** (echogenic medullary pyramids)""",
 "answer": """**เกณฑ์ให้คะแนน (10 คะแนน — รายละ 2 คะแนน: วินิจฉัย 1 + สิ่งที่ทำต่อ 1)**

| ราย | (ก) การวินิจฉัย | (ข) สิ่งที่ควรทำต่อ (ข้อใดข้อหนึ่ง) |
|---|---|---|
| 1 | **นิ่ว uric acid ในท่อไตขวาส่วนปลาย** — โปร่งรังสีบน KUB แต่ CT เห็น · ปัสสาวะเป็นกรด | ยาแก้ปวด (NSAID) + ดื่มน้ำ ± tamsulosin · **ทำปัสสาวะด่างด้วย potassium citrate** · ไม่ให้ probenecid |
| 2 | **CKD** (ไตเล็ก cortex บาง สว่างกว่าตับ CMD หาย) | ดูแลแบบ CKD ค้นหาสาเหตุ/ภาวะแทรกซ้อน · **ไม่ควรเจาะชิ้นเนื้อไตที่เล็กแล้ว** · เตรียม RRT ตาม eGFR |
| 3 | **Postrenal AKI จาก bladder outlet obstruction** (BPH) | **ใส่สายสวนปัสสาวะ (Foley) ทันที** · เฝ้าระวัง **post-obstructive diuresis** และเกลือแร่ |
| 4 | **ฝีในไต (renal abscess)** — หนองเหลวตรงกลาง ขอบ granulation tissue รับสี | **เจาะระบายผ่านผิวหนัง** (ก้อนใหญ่) + ยาปฏิชีวนะต่อ · หาการอุดกั้นร่วม |
| 5 | **Medullary nephrocalcinosis จาก distal (type 1) RTA** | ตรวจ urine net charge/สาเหตุ (Sjögren) · ให้ **K ก่อนแก้กรด** แล้วให้ **potassium citrate** |

**ข้อที่ทำให้เสียคะแนน**: ตอบรายที่ 1 ว่า "ไม่มีนิ่วเพราะ KUB ปกติ" · ส่งรายที่ 3 ไปทำ CT ฉีดสีก่อนใส่สายสวน · ตอบรายที่ 4 ว่าเป็น simple cyst (simple cyst ไม่มีขอบรับสีและผู้ป่วยไม่มีไข้) · ให้ NaHCO₃ แก้กรดในรายที่ 5 ก่อนให้ K""",
 "ref": ["สไลด์ อ.ธนิศร — Case 01–04, AKI vs CKD table, nephrocalcinosis"], "nl": ["2.3.14-3(15)", "2.3.14(3)", "2.3.14-3(9)", "2.3.14(14)", "2.3.14-3(12)", "3.3.20"],
 "years": [], "_kind": "meq", "_set": "nephro"}]

LECTURE = {
 "lec": LEC, "date": "",
 "title": "Essential Renal Imaging",
 "subtitle": "มุมมองนักไต · plain KUB · IVP · CT/CTU · MRI · สารทึบรังสีกับไต · ultrasound · nuclear renogram · How to CHOOSE (ACR) · ปัสสาวะเป็นเลือด · เคสคัดสรร: นิ่ว · complicated pyelonephritis · AKI vs CKD/hydronephrosis · nephrocalcinosis · ADPKD",
 "objectives": [
   "อธิบายฟิสิกส์ที่ทำให้แต่ละเนื้อเยื่อขาว/ดำบน X-ray CT และ ultrasound และใช้หลักนั้นแปลภาพ",
   "อ่าน plain KUB อย่างเป็นระบบ และแยกนิ่วจากหินปูนอื่น",
   "บอกเฟสของ IVP และ CT urography พร้อมสิ่งที่แต่ละเฟสใช้ดู",
   "เลือกการตรวจภาพที่เหมาะสมตาม ACR Appropriateness Criteria ในนิ่ว ปัสสาวะเป็นเลือด AKI/CKD และกรวยไตอักเสบ",
   "อธิบายกลไกของอาการเด่น (renal colic ไข้ไม่ลงใน pyelonephritis อ่อนแรงจาก K ต่ำ) และของสิ่งที่เห็นในภาพ",
   "แยก AKI กับ CKD จาก ultrasound และรู้ภาวะที่อุดกั้นโดยไม่มี hydronephrosis",
   "ประเมินความเสี่ยงและป้องกันไตเสียหายจาก iodinated contrast และ gadolinium ตามแนวทางปัจจุบัน",
   "เลือกและแปลผล nuclear renogram (DTPA MAG3 DMSA) รวมถึง diuretic renogram"],
 "nlGap": "เกณฑ์ฯ มีรหัส plain KUB (`3.2.3`) CT (`3.3.20`) นิ่ว (`2.3.14-3(15)`) pyelonephritis (`2.3.14(14)`) AKI/CKD (`2.3.14(3)`) obstructive uropathy (`2.3.14-3(9)`) RTA (`2.3.14-3(12)`) ADPKD (`B9.2.1-3(1)`) และปัสสาวะเป็นเลือด (`2.1.43`) แต่ **ไม่มีรหัสของ ultrasound ไต IVP MRI nuclear renogram หรือความปลอดภัยของสารทึบรังสี (CI-AKI, NSF)** · handout **ไม่มีหน้าเนื้อหาของ MRI และ nuclear imaging** และภาพรังสีในสไลด์มองไม่เห็น — เนื้อหาส่วนนั้นจึงอิงแนวทางด้านล่างและวาดภาพประกอบใหม่",
 "guidelines": [
   "**ACR Appropriateness Criteria** — ตารางในสไลด์ทุก modality: Acute Onset Flank Pain–Suspicion of Stone Disease (revised 2023) · Acute Pyelonephritis (uncomplicated/complicated) · Hematuria · Renal Failure (อาจารย์อ้างในสไลด์)",
   "**ACR–NKF Consensus Statements on the Use of IV Iodinated Contrast Media in Patients with Kidney Disease (Radiology 2020)** — เกณฑ์ eGFR < 30/AKI สำหรับการให้สารน้ำป้องกัน",
   "**ACR–NKF Consensus on Gadolinium-based Contrast Media in Patients with Kidney Disease (Radiology 2021)** และ **ACR Manual on Contrast Media** — ยา gadolinium กลุ่ม I/II, NSF, metformin",
   "**ESUR Guidelines on Contrast Agents 2018 (post-contrast AKI)** — เกณฑ์ eGFR และสูตรการให้สารน้ำ",
   "**AUA/SUFU Guideline on Microhematuria 2020 (amended 2025)** — การแบ่งความเสี่ยงและเลือก US/CTU + cystoscopy",
   "**EAU Guidelines on Urolithiasis 2025** — low-dose CT, ปริมาณรังสี, การรักษาเฉียบพลันและการระบายด่วน",
   "**KDIGO 2025 Clinical Practice Guideline for ADPKD** — การวินิจฉัยด้วยภาพ ปริมาตรไต และการรักษา",
   "**ตำราที่อาจารย์อ้าง**: Grainger & Allison's Diagnostic Radiology 7th ed (2021) · Diagnostic Ultrasound 6th ed (2024) · Comprehensive Clinical Nephrology 7th ed (2024) · Imaging in Urology (2018) · Fried & Morgan AJKD 2019 · Madaan & Ghasi BJR 2022 · Petrucci J Nephrol 2018"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# กระจายตำแหน่งคำตอบของข้อใหม่ (ข้อที่ตัวเลือกเรียงตามธรรมชาติไม่สลับ)
ORDERED = {N(2)}
_slot = 0
for s in S:
    for it in s["items"]:
        if it["id"] in ORDERED or not it["id"].startswith("NEPH-IMG-MCQ"):
            continue
        tgt = [0, 2, 4, 1, 3][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", "nephro.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LEC]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

# ── ผูกข้อคลัง (คาบ 28 ของ อ.ธนิศร — เฉพาะข้อภาพรังสี/นิ่ว/ปัสสาวะเป็นเลือด) และ Mock
BANK_MAP = {"neph-img-08": ["N-OLD-081", "N-OLD-082"],
            "neph-img-10": ["N-OLD-084", "N-MCQ-28", "N-OLD-080", "N-MCQ-27", "N-OLD-083"]}
BANK_MEQ, BANK_OSCE = [], ["N-OSCE-03"]
MOCK_MAP = {"neph-img-05": ["MOCK-171"], "neph-img-09": ["MOCK-174"], "neph-img-12": ["MOCK-182"], "neph-img-14": ["MOCK-175"]}
added = link("nephro", LEC, BANK_MAP, meq=BANK_MEQ, osce=BANK_OSCE) if (BANK_MAP or BANK_OSCE) else 0
addm = link_mock("nephro", LEC, MOCK_MAP) if MOCK_MAP else 0

data = json.load(open(path, encoding="utf-8"))
L = [l for l in data if l["lec"] == LEC][0]
seen = set()
for l in data:
    for x in [i for s in l["sections"] for i in s["items"]] + l["meq"] + l["osce"] + [{"id": s["id"]} for s in l["sections"]]:
        assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
        seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = {c for s in L["sections"] for c in s["nl"]} | {c for s in L["sections"] for i in s["items"] for c in i["nl"]} | {c for m in L["meq"] + L["osce"] for c in m.get("nl", [])}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
for s in L["sections"]:
    assert "```" not in s["md"], s["id"]

data.sort(key=lambda l: (0, int(l["lec"])) if l["lec"].isdigit() else (1, l["lec"]))
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "nephro": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
newi = [i for s in L["sections"] for i in s["items"] if i["id"].startswith("NEPH-IMG")]
print("sections %d | ข้อใหม่ %d + คลัง %d + mock %d = %d | meq %d | osce %d | figs %d | nl %d" % (
    len(S), len(newi), added, addm, sum(len(s["items"]) for s in L["sections"]), len(L["meq"]), len(L["osce"]),
    sum(len(s.get("figs") or {}) for s in S), len(codes)))
print("answer positions (ข้อใหม่):", dict(sorted(Counter(i["answer"] for i in newi).items())))
print("nephro.json มี %d คาบ: %s" % (len(data), [l["lec"] for l in data]))
