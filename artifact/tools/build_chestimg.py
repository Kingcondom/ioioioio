#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Image in chest — อ่าน CXR อย่างเป็นระบบ และโรคปอดจากการทำงาน (Potjanee Korrungruang, MD · อ.พจนี)
→ data/chest.json คาบ "21" (คาบ Ward Drill 21 "Chest X-ray / Occupational lung diseases") · พฤ. 1 ต.ค. 2569 13:00–15:00
ต้นฉบับ: "Image in chest.pdf" (191 หน้า · ลายมือผู้ใช้จดในห้อง) · โน้ต slides/chestimg_notes.md
ภาพรังสีจริงจากสไลด์: extract_chestimg.py → artifact/img/chest/*.jpg (section.imgs + [[img:key]])
ภาพนิ่ง SVG: figs_chest_img.py (apply_figs) · ภาพเคลื่อนไหว + หลักจำ: anims_chest_img.py
สไลด์ไม่มีส่วน occupational lung disease / heart failure / มะเร็งปอด → อิงแนวทาง: Fleischner 2017 · BTS 2023 ·
ILO 2022 · ATS/JRS/ALAT 2020 (HP) · ACCP 2013 (lung cancer staging)"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
REPO = os.path.dirname(BUILD)
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.join(REPO, "dashboard"))
from link_bank import link
from patch_learn_anim import _insert_marker
from apply_figs import apply_module
import anims_chest_img as AN
from extract_chestimg import SPEC as IMGSPEC

SET, LEC = "chest", "21"
LECNAME = "Chest X-ray / Occupational lung diseases (อ.พจนี)"
NLN = ["3.2.1"]
SRC = "สไลด์ อ.พจนี — Image in chest (191 หน้า)"
CREDIT = "ภาพจากสไลด์ Image in Chest — Potjanee Korrungruang, MD · รพ.ราชวิถี"
FILES = {int(n[4:6]): n for n, _, _ in IMGSPEC}
S = []


def sec(sid, title, summary, minutes, md, pearls, items, nl=None, src=SRC, imgs=None):
    s = {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": src,
         "nl": nl or NLN, "md": md, "pearls": pearls, "items": items}
    if imgs:
        s["imgs"] = imgs
    S.append(s)


def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None, keep=False):
    assert len(choices) == 5 and 0 <= answer <= 4 and len(set(choices)) == 5
    d = {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
         "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
    if keep:
        d["_keep"] = True
    return d


def IM(n, title, alt, cap=None, q=None, quiz=None):
    """ภาพจริงจากสไลด์ · key = c<NN> · cap = คำอธิบาย หรือ q + quiz = ให้ลองอ่านก่อนแล้วกดดูเฉลย"""
    d = {"src": "img/chest/%s.jpg" % FILES[n], "title": title, "alt": alt, "credit": CREDIT}
    if quiz:
        d["q"] = q or "ลองอ่านฟิล์มนี้ก่อน — เห็นอะไร และอยู่ตรงไหน"
        d["quiz"] = quiz
    else:
        d["cap"] = cap
    return "c%02d" % n, d


def IMGS(*xs):
    return dict(xs)


N = lambda n: "CH-IMG-MCQ-%02d" % n
R = lambda p: ["สไลด์ อ.พจนี — " + p]

# ───────────────────────────── 1
sec("chest-img-01", "ก่อนอ่าน: ตรวจตัวผู้ป่วย ท่าถ่าย และ view พิเศษ",
    "อ่าน 4 ขั้น: patient ID → position → technical adequacy → interpretation · PA ยืน = มาตรฐาน · AP นอนทุกอย่างดูใหญ่ · lateral ดูหน้า–หลัง · lordotic ดู apex · decubitus ดูน้ำ", 9,
"""### หลักการอ่านภาพถ่ายรังสีทรวงอก
สไลด์เปิดด้วยลำดับที่ต้องทำ **ทุกครั้งก่อนบอกว่าเห็นอะไร**
1. **Patient identification** — ชื่อ HN วันที่ถ่าย และหาฟิล์มเก่ามาเทียบ (ก้อนที่ไม่โตใน 2 ปีบอกอะไรได้มากกว่าการเดา)
2. **Position** — ฟิล์มนี้ถ่ายท่าไหน (ดูป้าย Upright / Supine / PORTABLE และสัญญาณบนภาพ)
3. **Technical adequacy** — ฟิล์มดีพอจะแปลผลไหม (หัวข้อถัดไป)
4. **Chest film interpretation** — อ่านอย่างเป็นระบบ

### ท่าถ่ายและ view พิเศษ
| View | ใช้เมื่อ | สิ่งที่ต้องสังเกต |
|---|---|---|
| **Upright PA** | **มาตรฐาน** ✍️ "Standard" | รังสีเข้าทางหลัง ฟิล์มชิดหน้าอก · มือเท้าเอวห่อไหล่ → **scapula หมุนออกนอกปอด** · **gastric bubble มี air-fluid level** |
| **Supine AP** (portable) | ผู้ป่วยยืนไม่ได้ (ICU ER) | ✍️ "**ทุกอย่างจะดูใหญ่มาก**" · scapula ซ้อนบนปอด · clavicle แนวนอน · กระเพาะไม่มี air-fluid level |
| **Lateral** | ✍️ "ดูส่วนหน้า/หลัง" · หาตำแหน่งรอยโรค | retrosternal และ retrocardiac clear space ต้องโปร่ง |
| **Oblique** (RAO/LAO) | รอยโรค **retrocardiac, posterior costophrenic angle, chest wall** | ซี่โครงหักที่มองไม่เห็นในภาพตรง |
| **Lordotic** | รอยโรค **apical lung** | ยก clavicle พ้นยอดปอด ✍️ "เห็นรอยชัดขึ้น" |
| **Lateral decubitus** | สงสัย **pleural effusion** ✍️ "เอาไว้ดูน้ำ" | น้ำอิสระไหลลงด้านล่าง · ดูปอดที่เคยถูกน้ำบัง |

[[img:c01]]

[[img:c02]]

### PA เทียบกับ AP — ทำไมหัวใจดูโตใน AP
| | **PA upright** | **AP supine / portable** |
|---|---|---|
| หลอดรังสี–ฟิล์ม | ~180 ซม. รังสีเกือบขนาน | ~100 ซม. รังสีบานออกมาก |
| หัวใจ (อยู่ด้านหน้า) | ใกล้ฟิล์ม → ขยายน้อย | ห่างฟิล์ม → **ขยาย** |
| Mediastinum | ขนาดจริง | ดูกว้าง (ขยาย + ท่านอนเลือดกลับหัวใจมาก) |
| Scapula | หมุนออกนอกปอด | ซ้อนบนปอด |
| ระดับน้ำ–ลม | เห็น (ลำแสงแนวนอน) | **ไม่เห็น** — น้ำไปอยู่หลัง ลมขึ้นหน้า |

✍️ อาจารย์: "**Cardiomegaly ควรอ่านใน film PA only** → AP มันเหมือนแว่นขยาย"

[[img:c03]]

### เมื่อสงสัยน้ำแต่ผู้ป่วยนอนอยู่
ฟิล์ม AP ท่านอน น้ำในช่องเยื่อหุ้มปอดไม่ลงไปที่มุมล่าง แต่ **กระจายเป็นชั้นบาง ๆ ทางด้านหลัง** → ทั้งซีกขาวจาง ๆ แบบม่าน (veil) ยังเห็นหลอดเลือดผ่าน · ไม่มี meniscus

[[img:c04]]

[[img:c05]]

[[img:c06]]

#### ทำไมถึงเห็นแบบนี้
| สิ่งที่เห็น | กลไก | ใช้ทำอะไร |
|---|---|---|
| **air-fluid level ในกระเพาะ** | ลำแสงแนวนอนตั้งฉากกับผิวน้ำ จึงเห็นเส้นตรง · ท่านอนลำแสงแนวตั้ง ผ่านผิวน้ำแบบแผ่นแบน ไม่เกิดเส้น | บอกว่าฟิล์ม **ยืน** · ใช้ดู air-fluid level ในโพรง/ฝีได้เฉพาะฟิล์มยืนหรือ decubitus |
| **หัวใจโตใน AP** | รังสีบานจากจุดเดียว วัตถุห่างฟิล์มขยายมาก · หัวใจเป็นอวัยวะด้านหน้า | ห้ามวินิจฉัย cardiomegaly / mediastinum กว้างจาก AP |
| **ซีกขาวจางทั้งข้างในท่านอน** | น้ำลงไปอยู่ด้านหลัง (ต่ำสุดเมื่อนอนหงาย) ลำแสงผ่านชั้นน้ำทั่วซีก | สงสัยน้ำ → decubitus หรือ ultrasound |
| **Lordotic เห็นยอดปอดชัด** | เอียงลำแสงขึ้น clavicle และ 1st rib ถูกฉายสูงพ้นยอดปอด | รอยโรค TB/Pancoast ที่ apex |
""",
    ["อ่าน 4 ขั้นเสมอ: ID → position → technical → interpretation",
     "PA ยืน = มาตรฐาน · AP portable ทุกอย่างดูใหญ่ — วินิจฉัย cardiomegaly จาก PA เท่านั้น",
     "เห็น air-fluid level ในกระเพาะ = ถ่ายท่ายืน",
     "Lordotic ดูยอดปอด · lateral decubitus ดูน้ำ · oblique ดูหลังหัวใจ/มุมหลัง/ผนังอก",
     "น้ำในท่านอน = ซีกขาวจางทั้งข้าง ไม่มี meniscus"],
    [mcq(N(1), "A 72-year-old man in the ICU has a portable AP supine chest radiograph. The cardiothoracic ratio measures 0.58 and the superior mediastinum looks widened. A standing PA radiograph taken 3 weeks earlier, when he was well, showed a cardiothoracic ratio of 0.46. He is haemodynamically stable. What is the most appropriate interpretation?",
         ["The apparent enlargement is likely projectional; cardiac size should not be judged on an AP supine film", "He has developed a large pericardial effusion and needs urgent pericardiocentesis", "He has acute aortic dissection because the mediastinum is widened", "He has new dilated cardiomyopathy and needs an echocardiogram today", "The previous PA film was underexposed and underestimated heart size"], 0,
         "ฟิล์ม **AP supine** หลอดรังสีอยู่ใกล้และหัวใจ (อวัยวะด้านหน้า) อยู่ห่างฟิล์ม → เงา **ขยายเกินจริง** · ท่านอนยังทำให้เลือดกลับหัวใจและ mediastinum ดูกว้างขึ้น\n\nจึง **ไม่วินิจฉัย cardiomegaly หรือ mediastinum กว้างจาก AP** ✍️ \"Cardiomegaly ควรอ่านใน film PA only\" · ถ้าสงสัยจริงให้เทียบกับอาการ หรือส่ง echo\n\n- pericardial effusion/dissection ต้องมีอาการหรือสัญญาณชีพผิดปกติ ไม่ใช่ตัดสินจากฟิล์ม AP เทียบ PA\n- exposure ไม่ได้ทำให้ขนาดหัวใจเปลี่ยน",
         "AP = แว่นขยาย · ตัดสินหัวใจโตจาก PA", "Projection", R("Position, Magnification"), NLN + ["2.3.9(5)"]),
     mcq(N(2), "A 30-year-old man has a chronic cough. On the PA radiograph a possible opacity at the right apex is partly hidden behind the clavicle and first rib. Which additional plain radiograph is most useful to clarify the apex?",
         ["Apical lordotic view", "Lateral decubitus view with the right side down", "Expiratory PA view", "Right anterior oblique view", "AP supine view"], 0,
         "**Lordotic view** เอียงลำแสงขึ้น ทำให้ **clavicle และซี่โครงแรกถูกฉายสูงพ้นยอดปอด** → เห็นรอยโรค apical ชัดขึ้น (✍️ \"เห็นรอยชัดขึ้น\") — สไลด์ใช้กับ TB และรอยโรคยอดปอด\n\n- **Decubitus** ใช้ดูน้ำในช่องเยื่อหุ้มปอด\n- **Expiratory** ใช้หา air trapping/pneumothorax เล็ก\n- **Oblique** ใช้ดู retrocardiac, posterior CP angle และผนังอก\n- AP supine ยิ่งทำให้ภาพขยายและบิด\n\nในทางปฏิบัติปัจจุบันมักส่ง CT ต่อ แต่โจทย์ถาม plain film",
         "Apex ถูก clavicle บัง → lordotic view", "Special views", R("Position of chest radiography"), NLN + ["B6.2.2(8)"]),
    ], NLN + ["B6.1.1(3)"],
    imgs=IMGS(
        IM(1, "PA upright — ฟิล์มมาตรฐาน", "CXR ท่า PA ยืน มีป้าย Upright มุมขวาบน มีเส้นสีขาวลากตามขอบ scapula ขวาซึ่งอยู่นอกปอด ลูกศรแดงชี้ขอบ scapula เส้นส้มตาม clavicle และวงรีดำล้อม gastric bubble ใต้โดมซ้าย",
           cap="ป้าย **Upright** · scapula (เส้นขาว) **อยู่นอกปอด** เพราะผู้ป่วยห่อไหล่ไปข้างหน้า · clavicle (ส้ม) · **gastric bubble** (วงรีดำ) มี air-fluid level = ท่ายืน"),
        IM(2, "AP supine (portable)", "CXR ท่า AP แบบ portable เส้นเขียวตามขอบ scapula ที่ซ้อนบนปอดซ้าย เส้นดำตาม clavicle ที่วางแนวนอน ลูกศรสีน้ำเงินแสดงความกว้างของหัวใจ ตัว X ที่ใต้โดมซ้าย",
           cap="**PORTABLE** · scapula (เขียว) **ซ้อนบนปอด** · clavicle (ดำ) แนวนอน · หัวใจกว้าง (ลูกศรน้ำเงิน) · ใต้โดมซ้าย (X) ไม่มี air-fluid level ✍️ \"ทุกอย่างจะดูใหญ่มาก\""),
        IM(3, "PA upright เทียบ AP supine ในผู้ป่วยคนเดียวกัน", "ภาพสองภาพเคียงกัน ซ้ายเป็น PA upright ขวาเป็น AP supine ของผู้ป่วยคนเดียวกัน มีเส้นเขียวตามขอบ scapula เส้นเหลืองแสดงความกว้างของหัวใจ และลูกศรแดงชี้ gastric bubble",
           cap="คนเดียวกัน — ภาพ AP: scapula เข้ามาในปอด (เขียว) · **หัวใจกว้างขึ้น** (เหลือง) · vascular pedicle กว้างขึ้น · gastric bubble ไม่มีระดับน้ำ"),
        IM(4, "AP ท่านอน — ซีกขวาขาวจาง ๆ", "CXR ท่า AP ผู้ป่วยนอน ปอดขวาทั้งซีกทึบจางแบบม่าน ยังเห็นเงาหลอดเลือดผ่าน ปอดซ้ายมีจุดทึบเล็ก ๆ กระจาย ไม่เห็นมุม costophrenic ขวา",
           q="ลองอ่านก่อน — ฟิล์ม AP ท่านอน ซีกขวาดูต่างจากซีกซ้ายอย่างไร และจะยืนยันด้วยท่าอะไร",
           quiz="**คำตอบ:** สงสัย **Rt pleural effusion** ในท่านอน · **จุดที่ต้องเห็น:** ซีกขวาขาว **จาง ๆ ทั่วทั้งซีก** แบบม่านแต่ยังเห็นหลอดเลือดผ่าน · ไม่มี meniscus · **กลไก:** นอนหงายน้ำไหลไปด้านหลังเป็นชั้นบาง ลำแสง AP ผ่านชั้นน้ำทั่วซีก · **ยืนยัน:** **lateral decubitus** ตะแคงขวาลง (ภาพถัดไป) หรือ ultrasound"),
        IM(5, "Right lateral decubitus — น้ำไหลลงด้านล่าง", "CXR ท่าตะแคงขวาลง ลำแสงแนวนอน เห็นแถบทึบตามผนังทรวงอกด้านล่าง ลูกศรสีแดงสองอันชี้ชั้นน้ำ",
           cap="ผู้ป่วยรายเดียวกัน ตะแคง **ขวาลง** — น้ำอิสระ **ไหลเป็นชั้นตามผนังด้านล่าง** (ลูกศรแดง) = **free-flowing effusion** · ถ้าไม่ไหลแปลว่า loculated"),
        IM(6, "Lordotic view — รอยโรคที่ยอดปอด", "ภาพวาดท่าถ่าย lordotic คู่กับ CXR ท่า lordotic clavicle ถูกยกพ้นยอดปอด มีลูกศรแดงชี้รอยทึบใต้ clavicle ขวา และเส้นเหลืองชี้ยอดปอดซ้าย",
           cap="ผู้ป่วยแอ่นตัวไปด้านหลัง (ภาพวาด) → **clavicle ถูกฉายสูงพ้นยอดปอด** · ลูกศรแดงชี้รอยโรคที่ apex ที่ซ่อนหลัง clavicle ในภาพ PA ✍️ \"เห็นรอยชัดขึ้น\""),
    ))

# ───────────────────────────── 2
sec("chest-img-02", "Technical adequacy — RIPE และสิ่งที่ฟิล์มไม่ดีหลอกเรา",
    "Exposure เห็นกระดูกสันหลังจาง ๆ หลังหัวใจ · หายใจเข้าเต็ม = posterior rib 9–10 / anterior rib 6 · rotation วัด spinous process–หัว clavicle · AP ขยาย · angulation ทำ clavicle ลอยสูง", 9,
"""### ห้าข้อที่ต้องตรวจก่อนแปลผล
| ข้อ | เกณฑ์ (สไลด์) | ถ้าไม่ได้ — หลอกอะไร |
|---|---|---|
| **Exposure** | **intervertebral space เห็นจาง ๆ หลังเงาหัวใจ** · กระดูกสันหลังใต้โดมเห็นจาง ๆ · เห็นซี่โครงหลังหัวใจ | **Under (ขาว):** ปอดขาวเหมือนมี infiltrate/edema · **Over (ดำ):** ✍️ "**ไม่เห็น lung marking**" → พลาดก้อน/รอยโรคจาง ดูเหมือน emphysema |
| **Inspiration** | **posterior rib 9–10** หรือ **anterior rib 6** อยู่เหนือโดมขวา | หายใจตื้น: ✍️ "**diaphragm ยกสูงขึ้น**" หัวใจดูโต ฐานปอดแออัดเหมือน infiltrate |
| **Rotation** | ระยะ **spinous process ↔ medial end ของ clavicle** สองข้างเท่ากัน | hilum ข้างหนึ่งเด่น mediastinum ดูกว้าง ความทึบสองข้างต่างกันหลอก |
| **Magnification** | รู้ว่าเป็น AP supine หรือไม่ | หัวใจและ mediastinum ดูโต |
| **Angulation** | upright หรือ semi-upright | ลำแสงเอียง → clavicle ลอยเหนือยอดปอด หัวใจรูปร่างผิด |

[[img:c07]]

[[img:c08]]

### Rotation — นับระยะจาก spinous process
spinous process อยู่ด้านหลัง ส่วนหัว clavicle อยู่ด้านหน้า — เมื่อตัวหมุน วัตถุหน้า–หลังจะเลื่อนสวนทางกันบนภาพ ระยะสองข้างจึงไม่เท่ากัน
- หัว clavicle ข้างที่ **ห่าง** spinous process มากกว่า = ด้านที่ตัวหมุนออกจากฟิล์ม (ในฟิล์ม PA)
- ข้อสำคัญในข้อสอบไม่ใช่ทิศ แต่คือ **ฟิล์มหมุน → ห้ามแปลความไม่สมมาตรของ hila, mediastinum และความทึบปอด**

[[img:c09]]

### Magnification และ angulation
[[img:c10]]

[[img:c11]]

#### ทำไมถึงเห็นแบบนี้
| สิ่งที่เห็น | กลไก | ความหมาย |
|---|---|---|
| **ฟิล์มขาวทั้งแผ่น (underexposed)** | รังสีน้อยเกิน ผ่านเนื้อเยื่อได้น้อย → ทุกอย่างขาว | ปอดดูทึบหลอก · ไม่เห็นสายหรือก้อนหลังหัวใจ |
| **ฟิล์มดำ (overexposed)** | รังสีมากเกินทะลุแม้ลายหลอดเลือด | ลายปอดหาย ✍️ "ไม่เห็น lung marking" → ดูเหมือน emphysema/pneumothorax |
| **หายใจตื้น → หัวใจโต ฐานทึบ** | โดมสูงดันหัวใจให้นอนแบนและกว้างขึ้น · ปอดล่างพองไม่เต็ม หลอดเลือดอัดชิดกัน | อย่าเรียก cardiomegaly หรือ basal pneumonia จนกว่าจะดูจำนวนซี่โครง |
| **หายใจลึกเกิน (> 10–11 posterior ribs)** | ปอดพองมาก โดมแบน | นึกถึง hyperinflation (COPD) |
| **Hilum ข้างหนึ่งเด่น** | ตัวหมุน ทำให้โครงสร้างกลางอกฉายเลื่อนไปข้างหนึ่ง | ตรวจ rotation ก่อนเรียก hilar mass (ข้อสอบคลัง) |
""",
    ["ตรวจคุณภาพฟิล์มด้วย RIPE ก่อนแปลผล",
     "Exposure พอดี: เห็น intervertebral space จาง ๆ หลังหัวใจ",
     "หายใจเข้าเต็ม: posterior rib 9–10 / anterior rib 6 เหนือโดมขวา",
     "Rotation: spinous process อยู่กึ่งกลางหัว clavicle สองข้าง — หมุนแล้วห้ามแปล hila/mediastinum",
     "Overexposure ลายปอดหาย · underexposure ปอดขาวหลอก"],
    [mcq(N(3), "A PA chest radiograph shows the right hemidiaphragm at the level of the posterior seventh rib. The heart appears broad and both lung bases look hazy with crowded vessels. The patient is afebrile with clear lungs on auscultation. What is the best interpretation?",
         ["The film is taken in suboptimal inspiration and the basal haziness and heart size may be artefactual", "Bilateral lower lobe pneumonia is present", "Cardiomegaly with pulmonary venous congestion is present", "Bilateral pleural effusions are present", "The film is overexposed, causing loss of lung markings"], 0,
         "หายใจเข้าเต็มต้องเห็น **posterior rib 9–10 (anterior rib 6)** เหนือโดมขวา · เห็นแค่ 7 = **หายใจตื้น (suboptimal inspiration)**\n\nกลไก: โดมสูงดันหัวใจให้นอนแบนและกว้างขึ้น · ปอดล่างพองไม่เต็ม หลอดเลือดอัดชิดกันจนดูขาวเหมือน infiltrate ✍️ \"diaphragm ยกสูงขึ้น · หายใจตื้น\"\n\n- ไม่มีไข้และฟังปอดปกติ ไม่สนับสนุน pneumonia\n- จะเรียก cardiomegaly/congestion ต้องมีฟิล์มหายใจเข้าเต็ม\n- effusion ต้องเห็น meniscus/มุมทื่อ\n- overexposure ทำให้ปอด **ดำ** ไม่ใช่ขาว",
         "นับซี่โครงก่อนเรียกหัวใจโต/ฐานปอดทึบ", "Inspiration", R("Technical adequacy — Inspiration")),
     mcq(N(4), "On a PA chest radiograph, the lungs appear diffusely white, the thoracic vertebrae and disc spaces cannot be seen through the heart, and a nasogastric tube cannot be traced below the carina. What is the main technical problem?",
         ["Underexposure", "Overexposure", "Patient rotation", "Excessive inspiration", "AP projection magnification"], 0,
         "เกณฑ์ exposure ที่เหมาะสม: **เห็น intervertebral space จาง ๆ หลังเงาหัวใจ** และเห็นซี่โครงหลังหัวใจ\n\nภาพนี้มองไม่เห็นกระดูกสันหลังหลังหัวใจ และปอดขาวทั่ว = **underexposure (ฟิล์มขาว)** — รังสีน้อยเกินผ่านเนื้อเยื่อไม่ได้ → ปอดดูทึบหลอก และไม่เห็นสาย/ก้อนหลังหัวใจ\n\n- **overexposure** ตรงข้าม: ฟิล์มดำ ลายปอดหาย\n- rotation ดูจาก spinous process–clavicle · inspiration ดูจากซี่โครง · AP ทำให้หัวใจขยาย",
         "มองไม่เห็นกระดูกสันหลังหลังหัวใจ = underexposed", "Exposure", R("Exposure quality")),
    ], NLN,
    imgs=IMGS(
        IM(7, "Overexposure vs underexposure", "CXR สองภาพของผู้ป่วยคนเดียวกัน ภาพซ้ายเขียนว่า Overexposure ปอดดำเข้มเห็นลายปอดน้อย ภาพขวาเขียนว่า Underexposure ทั้งภาพขาวจางกระดูกเห็นไม่ชัด",
           cap="**ซ้าย overexposure** — ปอดดำ ✍️ \"ไม่เห็น lung marking\" · **ขวา underexposure** — ภาพขาวทั้งแผ่น หลังเงาหัวใจมองไม่เห็นอะไร"),
        IM(8, "Full inspiration vs suboptimal inspiration", "CXR สองภาพเคียงกัน ภาพซ้าย Full inspiration ปอดยาว โดมต่ำ ภาพขวา Suboptimal inspiration โดมสูง หัวใจดูกว้าง ฐานปอดทึบ",
           cap="**Full inspiration** = posterior rib 9–10 / anterior rib 6 · **Suboptimal** ✍️ \"diaphragm ยกสูงขึ้น · หายใจตื้น\" หัวใจดูกว้าง ฐานปอดทึบหลอก"),
        IM(9, "ฟิล์มนี้หมุนหรือไม่", "CXR PA ท่ายืน มีเส้นสีน้ำเงินตามแนว spinous process วงเล็บสีแดงที่หัว clavicle ทั้งสองข้าง และลูกศรดำวัดระยะจากแนวกลางถึงหัว clavicle แต่ละข้างซึ่งยาวไม่เท่ากัน",
           q="ลองตรวจ rotation — วัดระยะจาก spinous process ถึงหัว clavicle สองข้าง",
           quiz="**คำตอบ:** ฟิล์ม **หมุน (rotated)** · **จุดที่ต้องเห็น:** หัว clavicle สองข้างห่างแนว spinous process **ไม่เท่ากัน** · ผลคือ mediastinum และ hilum ข้างหนึ่งดูเด่น ความทึบปอดสองข้างต่างกัน · **กลไก:** spinous process อยู่หลัง หัว clavicle อยู่หน้า เมื่อหมุนจะเลื่อนสวนทางกันบนภาพ · **ทำต่อ:** แปลความไม่สมมาตรด้วยความระวัง หรือถ่ายใหม่"),
        IM(10, "Magnification — PA เทียบ AP portable", "CXR สองภาพ ภาพซ้ายเป็นท่ามาตรฐาน ภาพขวาเป็น AP portable มีลูกศรแดงแสดงความกว้างของ mediastinum ส่วนบนและลูกศรสีน้ำเงินแสดงความกว้างของหัวใจซึ่งกว้างกว่า",
           cap="ภาพ **PORTABLE** ขวา: mediastinum ส่วนบน (แดง) และหัวใจ (น้ำเงิน) กว้างกว่าภาพซ้าย ✍️ \"Cardiomegaly ควรอ่านใน film PA only → AP มันเหมือนแว่นขยาย\""),
        IM(11, "Angulation", "CXR สองภาพ ภาพซ้ายท่าตรง ภาพขวาลำแสงเอียง clavicle ทั้งสองข้างลอยสูงเหนือยอดปอด มีวงรีดำล้อม clavicle สองข้าง ซี่โครงหน้าวางแนวนอน",
           cap="ลำแสงเอียง (semi-upright/lordotic) → **clavicle ลอยเหนือยอดปอด** (วงรีดำ) ซี่โครงหน้าแนวนอน หัวใจรูปร่างผิด — อย่าแปลผลขนาดหัวใจจากภาพนี้"),
    ))

# ───────────────────────────── 3
sec("chest-img-03", "Density และ attenuation — ภาษาของขาวกับดำ",
    "5 densities: air ดำ · fat ดำจาง · soft tissue/water ขาว · calcium/bone ขาวจ้า · metal ขาวสุด · ความหนาเปลี่ยนความทึบ · ขอบเกิดจากรอยต่อสอง density", 7,
"""### 5 densities บนฟิล์ม
| Density | สีบนฟิล์ม | ตัวอย่าง |
|---|---|---|
| **Air / gas** | **ดำเข้ม** | ปอด กระเพาะ ลำไส้ ลมใต้ผิวหนัง |
| **Fat** | **ดำจาง** | ไขมันใต้ผิวหนัง ไขมันรอบหัวใจ (pericardial fat pad) |
| **Soft tissue / water** | **ขาว** | หัวใจ mediastinum กล้ามเนื้อ เลือด น้ำ หนอง |
| **Calcium / bone** | **ขาวจ้า** | กระดูก หินปูนใน granuloma ต่อมน้ำเหลือง plaque |
| **Metal** | **ขาวจ้าที่สุด** | ลวดเย็บ sternum คลิป ท่อ tracheostomy ขั้ว ECG |

**Attenuation** = ความสามารถในการกั้นไม่ให้รังสีผ่านไปตกบนฟิล์ม
- **Low attenuation** → รังสีถึงฟิล์มมาก → **ดำ (radiolucency)**
- **High attenuation** → รังสีถึงฟิล์มน้อย → **ขาว (radiopacity)**
- **วัตถุ density เดียวกันอาจให้สีต่างกันตามความหนา** (สไลด์ p31)

[[img:c12]]

### ขอบ (border) เกิดจากอะไร
เราไม่ได้ "เห็นหัวใจ" — เราเห็น **รอยต่อระหว่างหัวใจ (soft tissue) กับปอด (air)** · ถ้าสองสิ่งที่อยู่ติดกันมี density เท่ากัน รอยต่อจะหายไป หลักข้อเดียวนี้อธิบายได้ทั้ง
- **silhouette sign** — ปอดที่ติดหัวใจกลายเป็นน้ำ ขอบหัวใจหาย
- **air bronchogram** — หลอดลมมีลมอยู่ท่ามกลางถุงลมที่กลายเป็นน้ำ จึงโผล่ให้เห็น
- **visceral pleural line ใน pneumothorax** — เนื้อปอดถูกล้อมด้วยลมทั้งสองด้าน เยื่อหุ้มบาง ๆ จึงเห็นเป็นเส้น

#### ทำไมถึงเห็นแบบนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรค |
|---|---|---|
| **ก้อนขาวเท่ากระดูก** | มีแคลเซียม attenuation สูงกว่า soft tissue | หินปูนแบบ benign (granuloma เก่า hamartoma) |
| **เส้นดำในกล้ามเนื้อหน้าอก/คอ** | ลมแทรกในเนื้อเยื่อ (density ต่ำกว่าไขมัน) | **subcutaneous emphysema** — หา pneumothorax/pneumomediastinum |
| **ซีกหนึ่งขาวทั้งหมด** ✍️ "ต้องเป็นอะไรสักอย่างที่กั้นแสงได้มาก" | ลมในปอดถูกแทนด้วยน้ำ/เนื้อ หรือปอดหายไป | effusion · collapse · consolidation · pneumonectomy (ดูหัวข้อ atelectasis) |
| **ปอดข้างหนึ่งดำกว่า** | ผนังอกข้างนั้นบางกว่า (ไม่มีเต้านม/กล้ามเนื้อ) หรือมีลม/เลือดน้อยลง | mastectomy · Poland · Westermark · air trapping |
""",
    ["Air ดำ · fat ดำจาง · soft tissue/water ขาว · calcium ขาวจ้า · metal ขาวสุด",
     "Attenuation สูง = ขาว (radiopaque) · ต่ำ = ดำ (radiolucent)",
     "ความหนาเปลี่ยนความทึบได้แม้ density เดียวกัน",
     "เห็นขอบได้เฉพาะรอยต่อของ density ต่างกัน → ฐานของ silhouette sign และ air bronchogram"],
    [mcq(N(5), "Why is the right heart border normally seen as a sharp line on a PA chest radiograph?",
         ["Soft-tissue density of the right atrium lies directly against air-filled lung, creating an interface", "The pericardium contains calcium that outlines the heart", "Epicardial fat is denser than lung tissue", "Blood in the right atrium is denser than myocardium", "The X-ray beam is tangential to the sternum at that point"], 0,
         "ขอบทุกเส้นบนฟิล์มคือ **รอยต่อระหว่างสอง density** — ขอบหัวใจขวาเกิดจาก **right atrium (soft tissue) แนบกับ RML ที่มีลม**\n\nถ้า RML กลายเป็นน้ำ/หนอง ขอบจะหาย = **silhouette sign** (หัวข้อถัดไป)\n\n- เยื่อหุ้มหัวใจปกติไม่มีหินปูน\n- ไขมันรอบหัวใจ (epicardial fat) ทึบกว่าลมจริง แต่เป็นชั้นบางที่ไม่ได้สร้างขอบหัวใจขวา — ขอบเกิดจาก RA แนบปอด\n- เลือดกับกล้ามเนื้อหัวใจ density ใกล้กัน จึงแยกกันไม่ได้บน CXR",
         "ขอบ = รอยต่อ soft tissue กับลม", "Density", R("Density, Attenuation")),
     mcq(N(6), "A 45-year-old asymptomatic woman has a 1 cm round nodule in the right upper zone. It is as white as the adjacent rib cortex and has not changed compared with a radiograph from 5 years ago. What does this density most likely indicate?",
         ["Diffuse calcification in a healed granuloma", "Air within a thin-walled cyst", "Fat within a lipoma", "Fluid within a bronchogenic cyst", "A metallic foreign body"], 0,
         "ก้อนที่ **ขาวเท่ากระดูก** = **density ของแคลเซียม** · หินปูนแบบ **ทั่วทั้งก้อน (diffuse)** และ **ไม่เปลี่ยนขนาด ≥ 2 ปี** เป็นลักษณะของ **granuloma เก่า (TB/fungus)** ที่ไม่ต้องติดตามต่อ\n\n- ลมในถุงน้ำจะ **ดำ**\n- ไขมัน **ดำจาง** กว่า soft tissue\n- น้ำในถุงน้ำ = soft tissue density (เท่าหัวใจ ไม่ใช่เท่ากระดูก)\n- โลหะขาวกว่ากระดูกมากและขอบคมผิดธรรมชาติ",
         "ขาวเท่ากระดูก + คงที่ ≥ 2 ปี = calcified granuloma", "Density", R("Density") + ["Fleischner Society 2017 — benign calcification"], NLN + ["B6.2.2(8)"]),
    ], NLN,
    imgs=IMGS(
        IM(12, "หา 5 densities ในฟิล์มนี้", "CXR PA มีตัวอักษร A ที่ปอดสองข้างและในกระเพาะ F ที่ไขมันใต้ผิวหนังด้านข้าง S/W ที่หัวใจ C ที่ clavicle และ S ที่ soft tissue ด้านข้าง",
           q="ตัวอักษร A, F, S/W และ C บนฟิล์มหมายถึง density อะไร และเรียงจากดำไปขาวอย่างไร",
           quiz="**A = air** (ปอด ลมในกระเพาะ) ดำที่สุด · **F = fat** (ไขมันใต้ผิวหนัง) ดำจาง · **S/W = soft tissue/water** (หัวใจ กล้ามเนื้อ) ขาว · **C = calcium/bone** (clavicle ซี่โครง) ขาวจ้า · โลหะ (ไม่มีในภาพนี้) ขาวที่สุด · **กลไก:** ยิ่งเลขอะตอมและความหนาแน่นสูง ยิ่ง attenuate รังสี → รังสีถึงฟิล์มน้อย → ขาว"),
    ))

# ───────────────────────────── 4
sec("chest-img-04", "Normal anatomy · อ่านเป็นระบบ · เงาผนังอกที่หลอกตา",
    "CTR < 0.5 (เด็ก < 0.6) บน PA · Rt interlobar PA ชาย < 16 หญิง < 15 มม. · hilum ซ้ายสูงกว่าขวา 1–2 ซม. · โดมขวาสูงกว่าได้ 2 ซม. · hidden areas · skin fold ไม่ใช่ pneumothorax", 11,
"""### Frontal anatomy ที่ต้องชี้ได้
[[img:c13]]

ค่าปกติจากสไลด์
| โครงสร้าง | ค่าปกติ |
|---|---|
| **Cardiothoracic ratio** (A+B)/C | **ผู้ใหญ่ < 0.5 · เด็ก < 0.6** (วัดบน PA) |
| **Rt interlobar pulmonary artery** (ระดับ bronchus intermedius) | **ชาย < 16 มม. · หญิง < 15 มม.** |
| **Hilum** | **ซ้ายสูงกว่าขวา 1–2 ซม.** (left PA พาดข้าม left main bronchus) |
| **Hemidiaphragm** | **ขวาสูงกว่าซ้ายได้ถึง 2 ซม. ใน 90%** · excursion ปกติ 3–7 ซม. · costophrenic sulcus แหลม |
| **Trachea** | ชาย 13–27 มม. · หญิง 10–23 มม. |
| **Subcarinal angle** | **35–90°** (กว้างขึ้นเมื่อ LA โตหรือต่อมน้ำเหลืองใต้ carina โต) |

[[img:c19]]

[[img:c20]]

### Lateral film
- **Retrosternal clear space** (หลัง sternum หน้า ascending aorta) และ **retrocardiac clear space** (หลังหัวใจหน้ากระดูกสันหลัง) ต้องโปร่ง — ทึบขึ้น = ก้อน anterior mediastinum หรือ lower lobe
- โดมขวา **เห็นตลอดแนวถึง sternum** · โดมซ้าย **ขาดหายตรงที่หัวใจวางอยู่** (หัวใจแนบโดมซ้ายด้านหน้า = silhouette)
- ปกติกระดูกสันหลังส่วนล่าง **ดำลงเรื่อย ๆ** (มีปอดล้อมมากขึ้น) — ถ้าล่างขาวกว่าบน นึกถึงรอยโรค lower lobe

[[img:c14]]

[[img:c21]]

### อ่านอย่างเป็นระบบ และ hidden areas
ใช้ลำดับเดิมทุกครั้ง (หลักจำ ABCDE ท้ายหัวข้อ) แล้ว ✍️ "**มองหาจุดซ่อนเร้น**" ที่สไลด์ไล่ไว้
| Hidden area | พลาดอะไรได้ |
|---|---|
| **Apices** | **Pancoast tumour** · TB · pneumothorax เล็ก |
| **Hila** | ก้อน ต่อมน้ำเหลือง — ดู **ตำแหน่ง ขนาด ความทึบ** |
| **Retrocardiac** | LLL collapse/consolidation · hiatal hernia |
| **ใต้โดม** | ลมใต้กะบังลม (perforation) · ปอดส่วนหลังที่ลงต่ำกว่าโดม |
| **กระดูก ซี่โครง clavicle ไหล่** | **metastasis** · กระดูกหัก · ไหล่หลุด |
| **Thoracic spine & paraspinal lines** | trauma · ก้อน posterior mediastinum |
| **Breasts** | mastectomy (ปอดข้างนั้นดำกว่า) |
| **Lung parenchyma** | ก้อนเล็กที่ซ้อนกับซี่โครง/หลอดเลือด |

### เงาผนังอกและ soft tissue ที่หลอกตา
[[img:c15]]

| เงา | เลียนแบบ | แยกอย่างไร |
|---|---|---|
| **Skin fold** (ผู้ป่วยนอน/ผอม/สูงอายุ) | pneumothorax | ✍️ "**ออกมานอกปอดเลย · No pleural line**" — เส้นวิ่งเลยออกนอกทรวงอก เป็นขอบทึบ–ดำ (ไม่ใช่เส้นขาวบาง) และ **ยังเห็นลายปอดเลยเส้น** |
| **Nipple shadow** | ก้อนในปอด | สองข้างสมมาตร ขอบด้านนอกคม ด้านในจาง · ติด nipple marker แล้วถ่ายซ้ำ |
| **Breast / mastectomy** | ฐานปอดทึบ / ปอดข้างหนึ่งดำ | ดูเงาเต้านมและรอยผ่าตัด |
| **Companion shadow ของ clavicle** · SCM | pleural thickening ที่ apex | ขนานกับ clavicle |
| **Morbid obesity** | ปอดทึบทั่ว | soft tissue หนา ทั้งฟิล์มขาว |

[[img:c16]]

[[img:c17]]

[[img:c18]]
""",
    ["CTR < 0.5 (ผู้ใหญ่, PA) · เด็ก < 0.6",
     "Hilum ซ้ายสูงกว่าขวา 1–2 ซม. · hilum ขวาสูงเท่าซ้าย = มีอะไรดึงขึ้น (RUL collapse)",
     "โดมขวาสูงกว่าซ้ายได้ถึง 2 ซม. · โดมซ้ายบน lateral ขาดหายที่หัวใจ",
     "ดู hidden areas ทุกครั้ง: apex · hila · retrocardiac · ใต้โดม · กระดูก",
     "Skin fold: เส้นเลยออกนอกทรวงอก ยังเห็นลายปอด → ไม่ใช่ pneumothorax"],
    [mcq(N(7), "A mechanically ventilated patient has a portable AP radiograph showing a vertical curvilinear line over the left lower chest. The line continues beyond the lateral chest wall into the soft tissues, lung markings are visible lateral to the line, and the line is an edge between grey and darker grey rather than a thin white line. What is the most appropriate action?",
         ["Recognise a skin fold and continue routine care", "Insert an intercostal chest drain for pneumothorax", "Perform needle decompression in the second intercostal space", "Request an urgent CT pulmonary angiogram", "Reduce PEEP because of barotrauma"], 0,
         "ลักษณะของ **skin fold** ✍️ \"ออกมานอกปอดเลย · No pleural line\"\n- เส้น **วิ่งเลยขอบทรวงอก** (pleura อยู่ในทรวงอกเท่านั้น)\n- เป็น **ขอบระหว่างเทากับเทาเข้ม** ไม่ใช่เส้นขาวบางของ visceral pleura\n- **ยังเห็นลายปอดด้านนอกเส้น**\n\npneumothorax ต้องมี **เส้นขาวบาง + ไม่มีลายปอดนอกเส้น** · การใส่สายหรือเจาะโดยไม่มี pneumothorax ทำให้เกิด pneumothorax/เลือดออกได้",
         "เส้นเลยนอกทรวงอก + ยังเห็นลายปอด = skin fold", "Pneumothorax mimic", R("Skin fold"), NLN + ["2.3.10(6)"]),
     mcq(N(8), "A 55-year-old woman has a PA radiograph in which the left hemithorax is uniformly more lucent than the right. The pulmonary vessels on both sides are of similar size and number, the mediastinum is central and lung volumes are equal. Which is the most likely cause?",
         ["Previous left mastectomy", "Left-sided pulmonary embolism with oligaemia", "Left main bronchus foreign body with air trapping", "Large left pneumothorax", "Left lower lobe collapse"], 0,
         "ปอดข้างหนึ่งดำกว่าแต่ **หลอดเลือดเท่ากัน ปริมาตรเท่ากัน mediastinum อยู่กลาง** → ความต่างมาจาก **ผนังอก** ไม่ใช่ปอด · ผนังข้างนั้นบางลง (ไม่มีเต้านม) จึงกั้นรังสีน้อยกว่า = **mastectomy** (สไลด์: \"No Rt breast shadow\") หรือ Poland syndrome\n\n- PE (Westermark): หลอดเลือด **น้อย/เล็กลง** ในบริเวณนั้น\n- foreign body + air trapping: ข้างนั้น **พองค้าง** mediastinum ถูกดันออก (ชัดในฟิล์มหายใจออก)\n- pneumothorax: เห็น pleural line และ **ไม่มีลายปอด**\n- LLL collapse ทำให้ทึบ ไม่ใช่ดำ",
         "ดำกว่าแต่หลอดเลือดปกติ = ผนังอก (mastectomy)", "Hyperlucency", R("Thoracic soft tissues, Decreased lung density")),
    ], NLN + ["B6.1.1(3)", "B6.1.1(5)"],
    imgs=IMGS(
        IM(13, "Normal anatomy — frontal", "ภาพวาดกายวิภาคบนภาพถ่ายรังสีหน้าตรงพร้อมหมายเลข 1 trachea 2 apex 4 carina 5 right main bronchus 6 right descending pulmonary artery 8 right cardiophrenic angle 10 costophrenic angle 12 descending aorta 13 left descending pulmonary artery 14 left hilum 15 left ascending pulmonary vein 16 aortic knob พร้อมเงาห้องหัวใจ RA LV LA",
           cap="1 trachea · 2 apex · 4 carina · 5 Rt main bronchus · 6 Rt descending PA · 8 Rt cardiophrenic angle · 10 costophrenic angle · 12 descending aorta · 13 Lt descending PA · 14 Lt hilum · 15 Lt ascending pulmonary v. · **16 aortic knob** · ขอบหัวใจขวา = **RA** · ขอบซ้าย = **LV** · LA อยู่ใต้ carina"),
        IM(19, "Cardiothoracic ratio", "CXR PA มีเส้นวัด A จากแนวกลางถึงขอบหัวใจขวา B จากแนวกลางถึงขอบหัวใจซ้าย และ C ความกว้างภายในทรวงอกที่กว้างที่สุด",
           cap="**CTR = (A + B) / C** · A, B = ระยะจากแนวกลางถึงขอบหัวใจขวาและซ้ายที่กว้างที่สุด · C = ความกว้างภายในทรวงอกที่กว้างที่สุด · **ผู้ใหญ่ < 0.5 · เด็ก < 0.6** · วัดบน **PA หายใจเข้าเต็ม** เท่านั้น"),
        IM(20, "Hilum ปกติ", "CXR ที่วาดเส้นแดงตาม pulmonary artery ซ้ายขวาและ main PA เส้นฟ้าตาม SVC และ RA ป้าย R truncus anterior, R ILPA, L interlobar PA, main PA และ tricuspid valve ลูกศรน้ำเงินวัดความกว้าง right interlobar PA",
           cap="**Rt interlobar PA (R ILPA)** วัดที่ระดับ bronchus intermedius — **ชาย < 16 มม. หญิง < 15 มม.** · **left PA พาดข้าม left main bronchus → hilum ซ้ายสูงกว่าขวา 1–2 ซม.** · hilum = PA + pulmonary vein + bronchus + ต่อมน้ำเหลือง"),
        IM(14, "Lateral film — 2 clear spaces", "ภาพวาด lateral ระบายสีแสดง retrosternal space สีฟ้าและ retrocardiac space สีแดงพร้อมตัวอักษร S T PA",
           cap="**Retrosternal clear space** (ฟ้า) และ **retrocardiac clear space** (แดง) ต้องโปร่ง — ทึบขึ้นเมื่อมีก้อน anterior mediastinum หรือ lower lobe collapse (✍️ \"loss of retrocardiac space\")"),
        IM(21, "Diaphragm บน frontal และ lateral", "CXR frontal และ lateral มีป้าย Rt dome และ Lt dome โดมขวาสูงกว่าซ้ายเล็กน้อย บนภาพ lateral โดมขวาเห็นตลอดถึง sternum โดมซ้ายหายไปตรงหัวใจ",
           cap="โดมขวา **สูงกว่าซ้ายได้ถึง 2 ซม.** · บน lateral **โดมขวาเห็นต่อเนื่องถึง sternum** · **โดมซ้ายขาดหายตรงหัวใจ** และมี gastric bubble ใต้โดมซ้าย"),
        IM(15, "Soft tissue บนผนังอก", "CXR PA มีลูกศรชี้ sternocleidomastoid muscle, axillary fold, nipple และ breast shadow ทั้งสองข้าง",
           cap="**SCM** · **axillary fold** · **nipple** · **breast shadow** — เงาเหล่านี้ซ้อนบนปอดได้ ต้องรู้จักก่อนเรียกว่ารอยโรค"),
        IM(16, "เส้นตรงนี้คือ pneumothorax หรือไม่", "CXR ท่านอน portable มีเส้นโค้งแนวตั้งที่ทรวงอกซ้ายด้านนอก ลูกศรเหลืองชี้เส้น และป้ายคำว่า Skin fold เส้นประสีดำแสดงขอบทรวงอก",
           cap="**Skin fold** (ลูกศรเหลือง) — เส้นวิ่ง **เลยออกนอกทรวงอก** (เทียบเส้นประขอบผนัง) เป็นขอบเทา–ดำ ไม่ใช่เส้นขาวบาง และ **ยังเห็นลายปอดด้านนอก** ✍️ \"ออกมานอกปอดเลย · No pleural line\""),
        IM(17, "ปอดข้างไหนดำกว่า เพราะอะไร", "CXR สองภาพ ภาพซ้ายปกติมีเงาเต้านมสองข้าง ภาพขวาไม่มีเงาเต้านมด้านขวา ปอดขวาส่วนล่างดำกว่าซ้าย",
           q="ภาพขวา ปอดล่างข้างหนึ่งดำกว่าอีกข้าง — ปอดผิดปกติหรือไม่",
           quiz="**คำตอบ:** **No Rt breast shadow — right mastectomy** · **จุดที่ต้องเห็น:** ไม่มีขอบเต้านมด้านขวา ปอดขวาล่างดำกว่า แต่ **หลอดเลือดสองข้างเท่ากัน** ปริมาตรเท่ากัน · **กลไก:** ผนังอกบางลง กั้นรังสีน้อยลง (attenuation ต่ำ) · ไม่ใช่โรคปอด — แต่ต้องดูกระดูกและต่อมน้ำเหลืองหามะเร็งกลับเป็นซ้ำ"),
        IM(18, "ฟิล์ม portable ผู้ป่วยหลังผ่าตัด", "CXR AP portable มีลมเป็นเส้นดำแตกแขนงในเนื้อเยื่อผนังอกทั้งสองข้างและที่คอ ตามแนวกล้ามเนื้อ pectoralis",
           q="ลองดูนอกปอด — เส้นดำแตกกิ่งในผนังอกและคอคืออะไร",
           quiz="**คำตอบ:** **Subcutaneous emphysema** · **จุดที่ต้องเห็น:** ลม (ดำ) แทรกเป็นเส้นตามใยกล้ามเนื้อ pectoralis และที่คอ ซ้อนบนปอดจนเหมือนลายปอดผิดปกติ · **กลไก:** ลมรั่วจากปอด/หลอดลม (pneumothorax, pneumomediastinum, barotrauma, หลังใส่สาย) เซาะตาม fascia · **ทำต่อ:** หา pneumothorax ที่อาจซ่อนอยู่ · ส่วนนี้คือ density ของ air ในบริเวณที่ไม่ควรมี"),
    ))

# ───────────────────────────── 5
sec("chest-img-05", "Air-space disease — consolidation และ ground-glass opacity",
    "Consolidation = ลมในถุงลมถูกแทนด้วย fluid blood pus cells · ทึบเนียนกลบหลอดเลือด + air bronchogram + ปริมาตรคงเดิม · GGO ทึบน้อยกว่า ยังเห็นหลอดเลือด", 10,
"""### Infiltration มีหลาย pattern
สไลด์แบ่ง infiltration ตามรูปแบบ — เลือก pattern ที่เด่นก่อน แล้วจึงคิด DDx
| Pattern | ส่วนของปอดที่ผิดปกติ | หัวข้อ |
|---|---|---|
| **Air-space (alveolar) consolidation** · **GGO** | ถุงลม (เติมเต็มหรือเติมบางส่วน) | หัวข้อนี้ |
| **Linear/septal** · **reticular** · **nodular** · **reticulonodular** | interstitium (ผนังถุงลม septa รอบหลอดลม) | Interstitial patterns |

### Consolidation — นิยามและลักษณะ
**Air-space consolidation** = ลมในถุงลมถูกแทนที่ด้วย **fluid, blood, pus, cells หรือสารอื่น**

ลักษณะบนฟิล์ม (สไลด์)
- **Homogeneous opacity obscuring vessels** — ทึบเนียนจนกลบหลอดเลือด
- **Air bronchograms** · air alveolograms
- ขอบไม่ชัด ปุย (ill-defined, fluffy) · patchy · acinar nodules
- **Preserved lung volume** — ปริมาตรไม่ลด (ต่างจาก atelectasis)
- ลามถึงผิว pleura · CT: **CT angiogram sign** (หลอดเลือดที่ฉีดสีวิ่งผ่านเนื้อทึบ)

| สิ่งที่อยู่ในถุงลม | ตัวอย่าง |
|---|---|
| **หนอง (pus)** | pneumonia (lobar, bronchopneumonia), TB |
| **น้ำ (water)** | cardiogenic pulmonary edema · **ARDS** |
| **เลือด (blood)** | pulmonary hemorrhage (vasculitis) · contusion · infarct |
| **เซลล์ (cells)** | invasive mucinous adenocarcinoma · lymphoma · organizing pneumonia |
| **โปรตีน** | pulmonary alveolar proteinosis |

[[img:c23]]

### Air bronchogram — ทำไมหลอดลมโผล่
[[img:c26]]

### Ground-glass opacity
- **ความทึบเพิ่มขึ้นแต่ยังไม่ถึง frank consolidation** — หลอดเลือดพร่าเล็กน้อยแต่ **ยังมองเห็นได้**
- ✍️ อาจารย์สรุป "**ง่าย ๆ → ขาวน้อยกว่า vascular + เห็น vascular marking**"
- กลไก: ถุงลมเติมของเหลว **บางส่วน** หรือผนังถุงลม/interstitium หนาขึ้นเล็กน้อย จนต่ำกว่าความละเอียดของภาพ (partial volume)
- DDx GGO ทั่วปอด: edema ระยะแรก · **PJP** · viral pneumonia (COVID-19) · hemorrhage · HP · drug

[[img:c27]]

[[img:c28]]

### Diffuse air-space disease
[[img:c24]]

[[img:c25]]

#### ทำไมถึงเห็นแบบนี้
| สิ่งที่เห็น | กลไก | บอกอะไร / DDx |
|---|---|---|
| **ทึบเนียนกลบหลอดเลือด** | ถุงลมรอบหลอดเลือดกลายเป็นน้ำ density เท่าหลอดเลือด → รอยต่อหาย | consolidation (ไม่ใช่ GGO) |
| **Air bronchogram** | หลอดลมยังเปิดและมีลม ล้อมด้วยถุงลมที่ทึบ | ทางเดินลมไม่อุด → pneumonia/edema · ไม่ใช่ obstructive atelectasis |
| **ปริมาตรคงเดิม** | ถุงลมถูก "เติม" ไม่ได้ "ยุบ" | แยกจาก atelectasis (fissure/hilum ไม่ขยับ) |
| **ขอบคมตรงตามรอยแยก** | consolidation ลามในกลีบจนชน fissure แล้วหยุด | lobar pneumonia · บอกกลีบได้ (RUL ขอบล่างเรียบตาม minor fissure) |
| **ขอบปุย ไม่ชัด** | ของเหลวลามผ่าน pores of Kohn ไปถุงลมข้างเคียงเป็นหย่อม | air-space ไม่ใช่ก้อนเนื้อ |
| **ทึบรอบขั้วปอดสองข้าง (ARDS/edema)** | ของเหลวรั่วจากหลอดเลือดที่เสียหาย (ARDS) หรือความดันสูง (cardiogenic) | ARDS: หัวใจไม่โต ไม่มี Kerley B · edema: หัวใจโต effusion |
""",
    ["Consolidation = ถุงลมเต็ม fluid/blood/pus/cells",
     "ทึบเนียน กลบหลอดเลือด + air bronchogram + ปริมาตรคงเดิม",
     "Air bronchogram = หลอดลมเปิด → ไม่ใช่ obstructive collapse",
     "GGO: ทึบแต่ยังเห็นหลอดเลือด ✍️ \"ขาวน้อยกว่า vascular\"",
     "ขอบเรียบตรงตาม fissure บอกกลีบ"],
    [mcq(N(9), "Which combination of radiographic features best distinguishes lobar consolidation from lobar atelectasis?",
         ["Air bronchograms with preserved lobar volume and no fissural displacement", "Absent air bronchograms with displacement of the fissure toward the opacity", "Elevation of the ipsilateral hemidiaphragm and hilum", "Shift of the trachea toward the opacity", "Crowding of vessels and approximation of ribs"], 0,
         "**Consolidation** = ถุงลมถูก **เติม** ด้วยหนอง/น้ำ → **ปริมาตรคงเดิม** fissure ไม่ขยับ และหลอดลมยังเปิด → **air bronchogram**\n\n**Atelectasis** = ถุงลม **ยุบ** → volume loss: **fissure เลื่อนเข้าหา** (direct sign), vessels ชิดกัน, hilum/โดมถูกดึง, trachea เลื่อนเข้าหา, ซี่โครงชิด (indirect signs) · ถ้าเกิดจากหลอดลมอุด มักไม่มี air bronchogram\n\nตัวเลือกอื่นทั้งหมดเป็นสัญญาณของ volume loss",
         "เติม (volume คงที่) vs ยุบ (volume ลด)", "Consolidation vs atelectasis", R("Consolidation, Atelectasis"), NLN + ["2.3.10(5)", "2.3.10(2)"]),
     mcq(N(10), "A 35-year-old man with advanced HIV infection has 2 weeks of dry cough and exertional desaturation. Chest radiograph shows bilateral hazy perihilar opacities through which the pulmonary vessels remain visible; there are no air bronchograms or effusions. What term best describes this opacity?",
         ["Ground-glass opacity", "Lobar consolidation", "Miliary nodules", "Reticular (honeycomb) pattern", "Lobar atelectasis"], 0,
         "ความทึบที่ **ยังมองเห็นหลอดเลือดผ่านได้** = **ground-glass opacity (GGO)** ✍️ \"ขาวน้อยกว่า vascular + เห็น vascular marking\"\n\nกลไก: ถุงลมเติมของเหลวบางส่วน/ผนังถุงลมหนาขึ้น ยังไม่ถึงกับไล่ลมออกหมด · ในบริบท HIV + desaturation นึกถึง **PJP** ก่อน (สไลด์ PJP: GGO + clustered cysts บน CT)\n\n- consolidation ต้องกลบหลอดเลือด + มี air bronchogram\n- miliary = จุดเล็ก 1–3 มม. · reticular = ตาข่าย · atelectasis = มี volume loss",
         "เห็นหลอดเลือดผ่าน = GGO · HIV + GGO → PJP", "GGO", R("Ground-glass opacity, PJP pneumonia"), NLN + ["2.3.10(5)", "2.3.1(20)"]),
    ], NLN + ["2.3.10(5)", "2.3.10-3(1)", "B6.2.2(4)"],
    imgs=IMGS(
        IM(23, "Air-space disease กลีบไหน", "CXR PA ปอดขวาส่วนบนทึบขาวเนียนตั้งแต่ยอดปอดลงมาถึงระดับกลางปอด ขอบล่างค่อนข้างเรียบ ปอดซ้ายปกติ",
           q="ลองอ่านก่อน — ทึบแบบไหน กลีบไหน และขอบล่างบอกอะไร",
           quiz="**คำตอบ:** **RUL consolidation** · **จุดที่ต้องเห็น:** ทึบเนียน (homogeneous) ทั้งปอดขวาบน **กลบหลอดเลือด** ✍️ \"undefined vascular marking\" · ขอบล่าง **เรียบตาม minor fissure** · ขอบ mediastinum ขวาบนหาย (silhouette กับ SVC) · **กลไก:** ถุงลมทั้งกลีบเต็มหนอง ลามจนชน fissure แล้วหยุด · ปริมาตรไม่ลด (fissure ไม่ยกขึ้น) — ต่างจาก RUL collapse"),
        IM(26, "Consolidation — air bronchogram และ CT angiogram sign", "ภาพ CXR ขยายแสดงความทึบที่มีกิ่งหลอดลมสีดำวิ่งผ่าน คู่กับภาพ CT ที่ฉีดสีเห็นหลอดเลือดขาววิ่งในเนื้อปอดที่ทึบ",
           cap="**ทึบเนียนกลบหลอดเลือด + air bronchograms** บน CXR · CT ฉีดสีเห็น **หลอดเลือดวิ่งผ่านเนื้อทึบ (CT angiogram sign)** ✍️ \"key alveolar infiltration\""),
        IM(27, "Ground-glass opacity", "CXR ขยายบริเวณ hilum ขวา ทึบจาง ๆ หลอดเลือดยังมองเห็นแต่ขอบพร่า คู่กับ CT ที่เห็นเนื้อปอดเป็นฝ้าขาวจางทั่ว",
           cap="**GGO** — ทึบเพิ่มเล็กน้อยรอบ hilum ขวา **หลอดเลือดยังเห็นแต่พร่า** ✍️ \"ง่าย ๆ → ขาวน้อยกว่า vascular + เห็น vascular marking\""),
        IM(28, "Consolidation เทียบ GGO", "ภาพสองภาพเคียงกัน ซ้ายเขียนว่า Consolidation ทึบเนียนมองไม่เห็นหลอดเลือด ขวาเขียนว่า Ground glass opacity ทึบจางยังเห็นหลอดเลือด",
           cap="ซ้าย **consolidation** กลบหลอดเลือดหมด · ขวา **GGO** ทึบกว่าปอดปกติแต่ **ยังเห็นหลอดเลือด**"),
        IM(24, "ผู้ป่วยใส่ท่อช่วยหายใจ ออกซิเจนต่ำมาก", "CXR AP portable ผู้ป่วยใส่ท่อช่วยหายใจและสายต่าง ๆ ปอดทั้งสองข้างทึบขาวกระจายทั่ว มี air bronchogram ขนาดหัวใจไม่โต",
           q="ผู้ป่วยใส่ท่อช่วยหายใจ PaO₂/FiO₂ ต่ำมาก — ลองอ่านก่อน",
           quiz="**คำตอบ:** **Diffuse alveolar infiltration — ARDS** · **จุดที่ต้องเห็น:** ทึบแบบ air-space **ทั้งสองข้างทั่วปอด** มี air bronchogram · หัวใจไม่โต ไม่เห็น Kerley B/effusion ชัด · มีท่อช่วยหายใจ · **กลไก:** alveolar–capillary membrane เสียหาย โปรตีนและน้ำรั่วเข้าถุงลม (non-cardiogenic edema) + ขาด surfactant → ถุงลมยุบ (adhesive atelectasis) · ต้องแยกจาก cardiogenic edema ด้วยประวัติและ echo"),
        IM(25, "ทึบจางทั่วปอดทั้งสองข้าง", "CXR AP portable ปอดทั้งสองข้างทึบจางทั่วแบบฝ้า ยังเห็นหลอดเลือด ไม่มีจุดทึบเนียนเป็นกลีบ",
           q="ลองอ่านก่อน — pattern นี้เรียกว่าอะไร และนึกถึงอะไรบ้าง",
           quiz="**คำตอบ:** **Diffuse ground-glass opacity** · **จุดที่ต้องเห็น:** ปอดสองข้างเป็นฝ้าทั่ว **ยังเห็นหลอดเลือดผ่าน** ไม่มี air bronchogram ชัด · **DDx:** PJP (HIV) · viral pneumonia · pulmonary edema ระยะแรก · hemorrhage · hypersensitivity pneumonitis · drug · **ทำต่อ:** ประวัติภูมิคุ้มกัน + HRCT"),
    ))

# ───────────────────────────── 6
sec("chest-img-06", "Silhouette sign — บอกกลีบจากขอบที่หาย",
    "รอยโรคทึบที่แตะโครงสร้าง soft tissue ทำให้ขอบหาย · SVC = RUL · ขอบหัวใจขวา = RML · โดมขวา = RLL · aortic knob = LUL · ขอบหัวใจซ้าย = lingula · โดมซ้าย/descending aorta = LLL", 10,
"""### Silhouette sign — หลักการ
สไลด์: เมื่อปอดที่ทึบ (consolidation) หรือก้อน soft tissue **สัมผัส** กับโครงสร้างอื่น ขอบของโครงสร้างนั้น **มองไม่เห็นหรือพร่า** · ใช้บอกว่ามีความผิดปกติในปอด (consolidation, atelectasis, mass) และ **บอกตำแหน่ง** ได้

ตรงข้าม — ถ้ารอยโรคอยู่ **คนละระนาบ** (หน้า–หลัง) กับโครงสร้าง ขอบจะยังคมแม้ภาพซ้อนกัน

[[img:c29]]

### ขอบไหนหาย = กลีบไหน
| ขอบที่หาย (frontal) | กลีบ |
|---|---|
| **Rt superior mediastinum (SVC)** · paratracheal stripe · azygos arch | **RUL** |
| **Rt heart border** | **RML** (หรือ medial RLL — พบน้อย) |
| **Rt hemidiaphragm** | **RLL** |
| **Lt superior mediastinum (aortic knob)** | **LUL** (apicoposterior) |
| **Lt heart border** | **Lingula** ของ LUL |
| **Lt hemidiaphragm · descending aorta** | **LLL** |

| ขอบที่หาย (lateral) | กลีบ |
|---|---|
| **ขอบหลังหัวใจ / โดมซ้ายส่วนหลัง** | **LLL** (หรือ hiatal hernia) |
| **โดมขวาส่วนหน้า** | **RML** |
| **โดมขวาส่วนหลัง** | **RLL** |

✍️ จากสไลด์ RLL consolidation: "**Rt heart ยังอยู่ + silhouette diaphragm**" · LLL: "**silhouette diaphragm**"

### ไล่ทีละกลีบ
[[img:c30]]

[[img:c31]]

[[img:c32]]

[[img:c33]]

[[img:c34]]

#### ทำไมถึงเห็นแบบนี้
| สิ่งที่เห็น | กลไก | ใช้แยกกลีบ |
|---|---|---|
| **ขอบหัวใจขวาหาย** | RML (medial segment) แนบ right atrium ด้านหน้า | RML · ถ้าโดมขวาหายแต่หัวใจยังคม = RLL |
| **ขอบหัวใจซ้ายหาย** | lingula แนบ LV ด้านหน้า | lingula (ไม่ใช่ LLL) |
| **โดมซ้าย/descending aorta หาย** | LLL อยู่ด้านหลัง แนบ aorta และโดมส่วนหลัง | LLL · ขอบหัวใจซ้ายยังเห็น |
| **ขอบ mediastinum ขวาบนหาย** | RUL แนบ SVC และ trachea | RUL · ขอบล่างเรียบตาม minor fissure |
| **Spine sign** (lateral) | ปกติกระดูกสันหลังส่วนล่างดำกว่าบนเพราะมีปอดล้อมมาก · lower lobe ทึบ → ส่วนล่างกลับขาวขึ้น | lower lobe (ตำรา — ไม่อยู่ในสไลด์) |
""",
    ["Silhouette = ทึบ density เดียวกันแตะกัน → ขอบหาย",
     "Rt heart = RML · Rt dome = RLL · Lt heart = lingula · Lt dome/desc. aorta = LLL",
     "SVC/Rt upper mediastinum = RUL · aortic knob = LUL",
     "ทึบซ้อนหัวใจแต่ขอบยังคม = รอยโรคอยู่คนละระนาบ (มักเป็น lower lobe)",
     "ยืนยันตำแหน่งด้วย lateral film"],
    [mcq(N(11), "A 60-year-old woman has fever and productive cough. Her PA radiograph shows an ill-defined opacity in the left mid zone that obscures the left heart border; the left hemidiaphragm and the descending aorta remain sharply outlined. Which segment is most likely involved?",
         ["Lingula of the left upper lobe", "Superior segment of the left lower lobe", "Posterior basal segment of the left lower lobe", "Apicoposterior segment of the left upper lobe", "Left lower lobe as a whole"], 0,
         "**ขอบหัวใจซ้ายหาย** = รอยโรคแนบ LV ด้านหน้า = **lingula** (อยู่ใน LUL)\n\nLLL อยู่ด้านหลัง แนบ **โดมซ้ายและ descending aorta** — ซึ่งยังคมอยู่ จึงไม่ใช่ LLL\n\n- apicoposterior LUL จะทำให้ **aortic knob** หาย\n- superior segment ของ lower lobe อยู่หลังระดับ hilum ไม่แนบขอบหัวใจ",
         "Lt heart border หาย = lingula", "Silhouette sign", R("Silhouette sign and corresponding lobes"), NLN + ["2.3.10(5)"]),
     mcq(N(12), "On a lateral chest radiograph of a patient with pneumonia, the lower thoracic vertebrae appear whiter than the upper thoracic vertebrae, and the posterior part of the right hemidiaphragm is not visible while the anterior part is clearly seen. Where is the consolidation?",
         ["Right lower lobe", "Right middle lobe", "Right upper lobe", "Anterior mediastinum", "Lingula"], 0,
         "บน lateral: **โดมขวาส่วนหลังหาย = RLL** (สไลด์) · โดมขวาส่วนหน้าหาย = RML\n\n**Spine sign** — ปกติกระดูกสันหลังส่วนล่างดูดำลงเรื่อย ๆ เพราะมีปอดที่มีลมล้อมมากขึ้น ถ้า lower lobe ทึบ ส่วนล่างกลับ **ขาวกว่า** ส่วนบน\n\n- RML อยู่หน้า เป็นลิ่มระหว่าง minor และ major fissure\n- RUL อยู่บน · lingula อยู่ซ้าย",
         "Lateral: โดมหลังหาย = lower lobe · spine sign", "Silhouette sign (lateral)", R("Silhouette sign — lateral view, RLL consolidation"), NLN + ["2.3.10(5)"]),
    ], NLN + ["2.3.10(5)", "B6.1.1(3)"],
    imgs=IMGS(
        IM(29, "Silhouette sign — แผนที่ขอบกับกลีบ", "ภาพวาดปอดสีเหลืองกับ mediastinum สีชมพูพร้อมป้าย paratracheal stripe azygos arch right heart border right hemidiaphragm aortic arch left heart border descending aorta left hemidiaphragm และกล่องข้อความระบุกลีบของแต่ละขอบ",
           cap="**ขวา:** SVC/paratracheal/azygos = **RUL** · ขอบหัวใจขวา = **RML** (หรือ medial RLL) · โดมขวา = **RLL** · **ซ้าย:** aortic arch = **LUL** · ขอบหัวใจซ้าย = **lingula** · โดมซ้าย/descending aorta = **LLL**"),
        IM(30, "PA + lateral — กลีบไหน", "CXR PA ปอดขวาบนทึบ ขอบล่างเรียบแนวนอน คู่กับภาพ lateral ที่ทึบอยู่ด้านหน้าบน มีลูกศรขาวชี้ minor fissure และลูกศรดำชี้ major fissure",
           q="ลองอ่านก่อน — ทึบอยู่กลีบไหน ใช้อะไรบอกบน lateral",
           quiz="**คำตอบ:** **RUL consolidation** · **จุดที่ต้องเห็น:** PA — ทึบปอดขวาบน **ขอบล่างเรียบตาม minor fissure** ขอบ mediastinum ขวาบนพร่า · lateral — ทึบอยู่ **เหนือ minor fissure (ลูกศรขาว) และหน้า major fissure (ลูกศรดำ)** · **กลไก:** consolidation ลามเต็มกลีบแล้วชน fissure จึงหยุดเป็นขอบคม"),
        IM(31, "RML consolidation", "CXR PA และ lateral มีลูกศรสีม่วงแดงชี้ minor fissure และลูกศรขาวชี้ major fissure ความทึบอยู่ข้างหัวใจขวาบน PA และเป็นลิ่มระหว่าง fissure ทั้งสองบน lateral",
           cap="**RML** — PA: ทึบข้างหัวใจขวา ขอบหัวใจขวาพร่า ขอบบนตาม **minor fissure** (ลูกศรม่วง) · lateral: ทึบเป็นลิ่มระหว่าง **minor fissure** กับ **major fissure** (ลูกศรขาว)"),
        IM(32, "ขอบหัวใจขวายังอยู่ไหม", "CXR PA ปอดขวาส่วนล่างทึบ ลูกศรดำชี้ขอบหัวใจขวาที่ยังคม คู่กับภาพ lateral ที่ทึบอยู่ด้านหลังล่าง ลูกศรชี้ major fissure",
           q="ลองอ่านก่อน — ทึบปอดขวาล่าง ดูขอบหัวใจขวาและโดมขวา แล้วบอกกลีบ",
           quiz="**คำตอบ:** **RLL consolidation** · **จุดที่ต้องเห็น:** PA — **ขอบหัวใจขวายังคม** (ลูกศรดำ) แต่ **โดมขวาหาย** ✍️ \"Rt heart ยังอยู่ + silhouette diaphragm\" · lateral — ทึบ **หลัง major fissure** ทับกระดูกสันหลังส่วนล่าง · **กลไก:** RLL อยู่ด้านหลังแนบโดม ไม่แนบหัวใจ (หัวใจแนบ RML ด้านหน้า)"),
        IM(33, "ทึบซีกซ้ายบนแบบจาง ๆ", "CXR PA ปอดซ้ายส่วนบนและกลางทึบจาง ๆ แบบไม่มีขอบชัด ขอบ aortic knob และขอบหัวใจซ้ายส่วนบนพร่า ปอดขวาปกติ",
           q="ลองอ่านก่อน — ซีกซ้ายบนทึบจาง ๆ ขอบไหนหาย",
           quiz="**คำตอบ:** **LUL consolidation** · **จุดที่ต้องเห็น:** ทึบจาง ๆ ซีกซ้ายบนไม่มีขอบล่างคม (**ปอดซ้ายไม่มี minor fissure**) · ขอบ aortic knob/หัวใจซ้ายส่วนบนพร่า · **กลไก:** LUL ห่อหน้าหัวใจ ภาพหน้าตรงจึงเป็นม่านทึบจาง ๆ ต่างจาก RUL ที่มีขอบล่างตาม minor fissure"),
        IM(34, "PA + lateral ปอดซ้ายล่าง", "CXR PA ปอดซ้ายล่างหลังหัวใจทึบ โดมซ้ายหายไป ขอบหัวใจซ้ายยังเห็น คู่กับภาพ lateral ที่ทึบหลังหัวใจด้านล่าง ลูกศรชี้",
           q="ลองอ่านก่อน — ขอบหัวใจซ้ายยังอยู่ไหม โดมซ้ายล่ะ",
           quiz="**คำตอบ:** **LLL consolidation** · **จุดที่ต้องเห็น:** **โดมซ้ายหาย** ✍️ \"silhouette diaphragm\" · ขอบหัวใจซ้าย **ยังเห็น** · ทึบหลังหัวใจ (retrocardiac) · lateral: ทึบด้านหลังล่าง โดมซ้ายส่วนหลังหาย · **กลไก:** LLL แนบโดมซ้ายและ descending aorta ด้านหลัง ไม่แนบ LV ด้านหน้า"),
    ))

# ───────────────────────────── 7
sec("chest-img-07", "Interstitial patterns — reticular, nodular, miliary, reticulonodular",
    "Reticular = ตาข่าย (fine < 3 · medium 3–10 · coarse > 10 มม.) = ILD · nodular ≤ 5 มม. = interstitial/metastasis/granuloma · miliary = interstitial · reticulonodular: sarcoid lymphangitic amyloid · บน vs ล่าง", 10,
"""### Secondary pulmonary lobule — ทำไม pattern ต่างกัน
รอยโรคในปอดจะ "หน้าตา" ต่างกันตามส่วนของ lobule ที่ผิดปกติ — ถุงลม (air-space) หรือโครงร่าง (interstitium: septa, ผนังถุงลม, รอบหลอดลม-หลอดเลือด)

### Reticular pattern
- **Reticular = netlike** — เส้นตัดกันหลายเส้น ล้อมช่องกลมหรือไม่สม่ำเสมอ → บ่งว่ามี **interstitial lung disease** ✍️ "interstitial มีหลาย pattern"
- แบ่งตามขนาดช่อง: **fine (< 3 มม.) · medium (3–10 มม.) · coarse (> 10 มม.)**
- **ปอดเล็กลง + reticular ที่ฐานปอด** = รูปแบบของพังผืด (IPF/UIP, CTD-ILD, asbestosis)
- coarse reticular ช่อง > 1 ซม. = **honeycombing / cystic lung** (end-stage fibrosis)

[[img:c35]]

### Nodular pattern และ miliary
- **ปุ่มเล็กนับไม่ถ้วน** ขนาดไม่กี่มิลลิเมตรถึง 1 ซม. — เป็นได้ทั้ง interstitial หรือ air-space
- **Miliary nodules** (1–3 มม. เท่า ๆ กัน กระจายทั่ว) มักเป็น **interstitial** — มาทางกระแสเลือด
- ปุ่ม **≤ 5 มม.** ไม่ว่าขอบชัดหรือไม่ เกือบทั้งหมดเป็น **interstitial disease, metastases หรือ granulomatous disease**
- ✍️ "**Size จะบ่งบอก malignancy**" — ยิ่งใหญ่ ยิ่งไม่เท่ากัน ยิ่งนึกถึง metastasis

| ลักษณะ | นึกถึง |
|---|---|
| **Miliary 1–3 มม. เท่ากันทั่วปอด** | **miliary TB** · fungus (histoplasma) · metastasis (thyroid, renal, melanoma) · silicosis · sarcoidosis |
| **ปุ่มขนาดต่างกัน กลม ขอบชัด ฐานปอดมากกว่า** | hematogenous metastases (cannonball) |
| **ปุ่มเล็กปอดบน + ต่อมน้ำเหลือง hilum มีหินปูนแบบเปลือกไข่** | silicosis / CWP (หัวข้อโรคปอดจากการทำงาน) |

[[img:c36]]

[[img:c37]]

### Reticulonodular pattern
- เส้น + จุดร่วมกัน → **ตัดสินว่าแบบไหนเด่น แล้วใช้ DDx ของแบบนั้น**
- ที่เป็นสองแบบร่วมกันจริงทางพยาธิมีน้อย: **sarcoidosis · lymphangitic spread of tumor · diffuse amyloidosis**

[[img:c38]]

### ปอดบนหรือปอดล่าง — ตัวช่วยแคบ DDx
| เด่นปอดบน | เด่นปอดล่าง |
|---|---|
| silicosis · coal worker's pneumoconiosis · sarcoidosis · TB · Langerhans cell histiocytosis · ankylosing spondylitis · HP เรื้อรัง | **IPF** · RA · scleroderma · **asbestosis** · ยา (amiodarone, nitrofurantoin) |
| กลไก: ปอดบนการไหลเวียนเลือดและน้ำเหลืองน้อยกว่า (V/Q สูง) ฝุ่นจึงค้าง · TB ชอบ O₂ สูง | กลไก: ฐานปอดถูกยืด–หด (mechanical stress) มากที่สุด · ใยหินยาวตกลงล่าง |

#### ทำไมถึงเห็นแบบนี้
| Pattern | กลไก | ตัวอย่าง |
|---|---|---|
| **Kerley B / septal lines** | interlobular septa (มี vein + lymphatic) หนาจากน้ำหรือเซลล์มะเร็ง | interstitial edema · lymphangitic carcinomatosis |
| **Reticular + volume ลด** | collagen แทนที่ผนังถุงลม ปอดหดรั้ง | IPF · CTD-ILD · asbestosis |
| **Honeycombing** | ถุงลมพังรวมเป็นช่องผนังหนาเรียงหลายชั้นใต้ pleura | end-stage fibrosis (UIP) |
| **Miliary** | เชื้อ/เซลล์กระจายทางกระแสเลือดไปติดทุก lobule เท่า ๆ กัน | miliary TB · metastasis |
| **Upper zone nodules + hilar node** | ฝุ่นถูก macrophage พาไปตามท่อน้ำเหลืองสู่ hilum · ปอดบนเคลียร์ช้า | silicosis · CWP |
""",
    ["Reticular = ตาข่าย = ILD · fine < 3 · medium 3–10 · coarse > 10 มม.",
     "ปอดเล็กลง + reticular ฐานปอด = fibrosis (IPF, CTD, asbestosis)",
     "Miliary 1–3 มม. เท่ากันทั่ว = interstitial ทางกระแสเลือด → TB ก่อน",
     "Reticulonodular จริง: sarcoidosis · lymphangitic · amyloidosis",
     "ปอดบน: silicosis CWP sarcoid TB · ปอดล่าง: IPF RA scleroderma asbestosis"],
    [mcq(N(13), "A 40-year-old man with uncontrolled HIV infection has 3 weeks of fever, night sweats and weight loss. Chest radiograph shows innumerable uniform 1–2 mm nodules evenly distributed throughout both lungs. Which is the most likely diagnosis?",
         ["Miliary tuberculosis", "Cannonball metastases from renal carcinoma", "Bilateral lobar pneumonia", "Idiopathic pulmonary fibrosis", "Cardiogenic pulmonary oedema"], 0,
         "**ปุ่มเล็ก 1–3 มม. ขนาดเท่ากัน กระจายสม่ำเสมอทั่วปอด** = **miliary pattern** ซึ่งเป็น **interstitial** ที่มาทาง **กระแสเลือด** — เชื้อถูกหว่านไปติดทุก lobule พร้อมกันจึงขนาดเท่ากัน\n\nผู้ป่วย HIV + ไข้ เหงื่อออกกลางคืน น้ำหนักลด → **miliary TB** ต้องคิดก่อน (ส่ง sputum/Xpert, ตรวจเลือด/ปัสสาวะ/ไขกระดูกหาเชื้อ และเริ่มยาเร็ว)\n\n- **cannonball metastases** ก้อนใหญ่กว่าและขนาดไม่เท่ากัน\n- lobar pneumonia เป็นทึบเนียนกลีบ · IPF เป็น reticular ฐานปอด · edema เป็น septal lines/air-space รอบขั้ว",
         "Miliary เท่ากันทั่วปอด + ไข้ = miliary TB", "Nodular pattern", R("Nodular pattern, Miliary nodules"), NLN + ["B6.2.2(8)", "2.3.1(20)"]),
     mcq(N(14), "Which of the following conditions characteristically produces fibrosis or nodules predominantly in the UPPER zones on chest radiography?",
         ["Silicosis", "Asbestosis", "Idiopathic pulmonary fibrosis", "Systemic sclerosis-associated interstitial lung disease", "Rheumatoid arthritis-associated interstitial lung disease"], 0,
         "**Silicosis** (และ CWP, sarcoidosis, TB, Langerhans cell histiocytosis, ankylosing spondylitis) **เด่นปอดบน** — ปอดบนเคลียร์ฝุ่นทางน้ำเหลืองได้ช้ากว่า (หลักจำ **SCHARTS**)\n\n**ปอดล่าง** (หลักจำ **RASCO**): **R**A · **A**sbestosis · **S**cleroderma · **C**ryptogenic fibrosing alveolitis (IPF) · **O**thers (ยา)\n\nจุดนี้ใช้แยก silicosis กับ asbestosis ในโจทย์อาชีพได้ทันที",
         "ปอดบน: SCHARTS · ปอดล่าง: RASCO", "Zonal distribution", R("Reticular pattern") + ["Radiopaedia — upper vs lower zone predominant lung disease"], NLN + ["2.3.10-3(4)"]),
    ], NLN + ["B6.1.1(3)", "2.3.10-3(4)", "B6.2.2(8)"],
    imgs=IMGS(
        IM(35, "Reticular pattern", "ภาพ CXR สามภาพซ้อนกัน ภาพแรกปอดเล็กลงมีเส้นตาข่ายไม่สม่ำเสมอที่ฐานปอด ภาพขยายแสดงเส้นที่ล้อมช่องขนาดไม่เกินหนึ่งเซนติเมตร และภาพปอดขวาที่มีลายตาข่ายทั่ว",
           cap="**ปอดเล็กลง + reticular ไม่สม่ำเสมอที่ฐาน** = รูปแบบพังผืด · ภาพขยาย: เส้นล้อมช่อง **≤ 1 ซม. = medium reticular** · ✍️ \"interstitial มีหลาย pattern\""),
        IM(36, "ปุ่มทั่วปอดทั้งสองข้าง", "CXR PA ปอดทั้งสองข้างมีปุ่มทึบขนาดหลายมิลลิเมตรถึงเกือบหนึ่งเซนติเมตรจำนวนมาก กระจายทั่วโดยเฉพาะส่วนกลางและล่าง ขอบปุ่มไม่ค่อยชัด",
           q="ลองอ่านก่อน — pattern อะไร ขนาดเท่ากันไหม และนึกถึงอะไร",
           quiz="**คำตอบ:** **Diffuse nodular infiltration** · **จุดที่ต้องเห็น:** ปุ่มนับไม่ถ้วนทั้งสองข้าง ขนาดหลายมิลลิเมตร (ใหญ่กว่า miliary) · ✍️ \"Size จะบ่งบอก malignancy\" — ปุ่มใหญ่ขึ้น/ไม่เท่ากัน นึกถึง metastasis มากขึ้น · **DDx:** metastases · TB/fungal · pneumoconiosis · sarcoidosis · **ทำต่อ:** HRCT ดูการกระจายของปุ่ม (centrilobular / perilymphatic / random)"),
        IM(37, "Miliary nodules", "ภาพขยาย CXR สองภาพแสดงจุดทึบเล็กขนาดไม่กี่มิลลิเมตรจำนวนมากเท่า ๆ กัน และภาพ CT ปอดที่มีจุดเล็กกระจายทั่วแบบสุ่ม",
           cap="**Miliary** — ปุ่ม **ไม่กี่มิลลิเมตร ขนาดเท่ากัน** นับไม่ถ้วน · CT: กระจายแบบสุ่ม (random) ทั่ว lobule = มาทางกระแสเลือด → **miliary TB** · metastasis · fungus"),
        IM(38, "เส้นปนจุดทั่วปอด", "CXR PA ปอดทั้งสองข้างมีทั้งเส้นตาข่ายและจุดทึบเล็กปนกันทั่ว โดยเฉพาะส่วนกลางและล่าง",
           q="ลองอ่านก่อน — เป็น pattern อะไร และควรทำอย่างไรกับ DDx",
           quiz="**คำตอบ:** **Diffuse reticulonodular infiltration** · **จุดที่ต้องเห็น:** เส้น (reticular) + จุด (nodular) ปนกันทั่วปอด · **หลักสไลด์:** ตัดสินว่าแบบไหน **เด่น** แล้วใช้ DDx ของแบบนั้น · ที่เป็นสองแบบจริง: **sarcoidosis · lymphangitic carcinomatosis · amyloidosis** · **ทำต่อ:** HRCT"),
    ))

# ───────────────────────────── 8
sec("chest-img-08", "Atelectasis — ชนิด สัญญาณ volume loss และ white-out",
    "Resorption (พบบ่อย) · relaxation · adhesive · cicatricial · direct: fissure เลื่อน vessels ชิด · indirect: โดมยก mediastinum/hilum ถูกดึง ซี่โครงชิด · white-out: ดึง = collapse · ดัน = effusion", 10,
"""### Atelectasis คืออะไร
**Atelectasis = incomplete stretching = collapse** — ถุงลมไม่พอง ปริมาตรส่วนนั้น **ลดลง** ต่างจาก consolidation ที่ปริมาตรคงเดิม

### ชนิดของ atelectasis ตามกลไก
| ชนิด | กลไก | ลักษณะ |
|---|---|---|
| **Resorption (obstructive)** ✍️ common | หลอดลมอุด → ก๊าซในถุงลมถูกเลือดดูดซึม | เกิด **ภายใน 24 ชม.** · **เร็วขึ้นเมื่อหายใจ O₂** · อาจเป็น drowned lung (เต็มเสมหะ) ปริมาตรลดน้อย · collateral ventilation อาจกันไม่ให้ยุบ · **หลอดลมใหญ่อุด มักไม่มี air bronchogram** |
| **Relaxation (passive)** | effusion, pneumothorax หรือก้อนกด → ปอดหดตาม recoil | ความทึบอาจไม่มาก |
| **Adhesive** | ขาด surfactant → แรงตึงผิวสูง ถุงลมยุบ | RDS ทารก · **ARDS** · radiation pneumonitis |
| **Cicatricial** | พังผืดดึงรั้ง | ✍️ **TB เก่า** · fibrosis |

### Direct และ indirect signs
| Direct signs (volume loss ของกลีบนั้นเอง) | Indirect signs (ผลตามมา) |
|---|---|
| **Fissure เลื่อนเข้าหา** กลีบที่ยุบ | **โดมยกสูง** |
| **Vessels ชิดกัน** ✍️ "เส้นเลือดรวม ชิดแคบ ๆ" | **Mediastinum เลื่อนเข้าหา** |
| | ปอดส่วนอื่นพองชดเชย (compensatory overinflation) |
| | **Hilum เลื่อน** · หลอดลม/hilum หมุนทิศ |
| | **ซี่โครงชิดกัน** |
| | ทึบขึ้น · **ไม่มี air bronchogram** · shifting granuloma |

สัญญาณเฉพาะชนิด: **Golden S** (RUL) · **juxtaphrenic peak** (upper lobe) · **Luftsichel** (upper lobe มักซ้าย) · **flat waist** (LLL) · **comet-tail** (rounded atelectasis) — ✍️ อาจารย์บอก "**ไม่จำ**" ชื่อทั้งหมด → **เข้าใจว่า volume loss ดึงอะไรไปทางไหน** ก็อ่านออก

### Platelike และ rounded atelectasis
- **Platelike (discoid)** — แถบทึบแนวนอนบาง ๆ ที่ฐานปอด · หายใจตื้น (หลังผ่าตัด ปวดท้อง) ถุงลมส่วนล่างไม่พอง
- **Rounded atelectasis** ✍️ "**3 component**" ✍️ "Specific" — (1) **pleura หนา/effusion ติดกัน** (2) **ก้อนกลมใต้ pleura ทำมุมแหลมกับ pleura** (3) **comet-tail** หลอดเลือด/หลอดลมโค้งวนเข้าก้อน + volume loss ของกลีบนั้น · พบบ่อยในผู้สัมผัส **asbestos** · ไม่ใช่มะเร็งแต่ต้องแยกด้วย CT

[[img:c48]]

[[img:c49]]

### Hemithorax ขาวทั้งข้าง — ดึงหรือดัน
[[img:c72]]

| ภาวะ | Trachea/mediastinum | อื่น ๆ |
|---|---|---|
| **Total lung collapse** (ก้อน/เสมหะอุด main bronchus) | **ถูกดึงเข้าหา** | ซี่โครงชิด โดมยก ไม่มี air bronchogram |
| **Pneumonectomy** | ถูกดึงเข้าหา | ซี่โครงถูกตัด/คลิป |
| **Massive pleural effusion** | **ถูกดันออก** | ช่องซี่โครงกว้าง |
| **Consolidation ทั้งข้าง** | อยู่กลาง | air bronchogram |
| **Effusion + collapse ร่วมกัน** (มะเร็งอุดหลอดลม + น้ำ) | อยู่กลาง (หักล้างกัน) | ต้อง CT/bronchoscopy |
""",
    ["Atelectasis = volume ลด · consolidation = volume คงที่",
     "Resorption พบบ่อยสุด: หลอดลมอุด ก๊าซถูกดูดซึม เร็วขึ้นเมื่อให้ O₂",
     "Direct: fissure เลื่อน + vessels ชิด · indirect: โดม hilum mediastinum ถูกดึง ซี่โครงชิด",
     "Rounded atelectasis 3 องค์ประกอบ: pleura หนา + ก้อนใต้ pleura + comet-tail · asbestos",
     "White-out: mediastinum ไปหา = collapse · หนี = effusion · กลาง = consolidation"],
    [mcq(N(15), "Two hours after a patient with a mucus plug obstructing the left lower lobe bronchus was placed on 100% oxygen, the left lower lobe collapsed completely. Why does breathing high-concentration oxygen accelerate resorption atelectasis distal to an obstruction?",
         ["Oxygen is rapidly absorbed into capillary blood, and without nitrogen to splint the alveoli they empty quickly", "Oxygen directly inhibits surfactant secretion by type II pneumocytes within minutes", "Oxygen causes reflex bronchoconstriction that tightens the obstruction", "High oxygen increases alveolar surface tension by oxidising the alveolar lining fluid", "Oxygen raises pulmonary artery pressure, compressing the alveoli"], 0,
         "หลังหลอดลมอุด ก๊าซที่ค้างในถุงลมถูก **ดูดซึมเข้าเลือด** (ความดันรวมของก๊าซในเลือดดำต่ำกว่าในถุงลม)\n\n**ไนโตรเจน** ถูกดูดซึมช้ามาก จึงทำหน้าที่ \"ค้ำ\" ถุงลมไว้ · เมื่อให้ **O₂ 100%** ไนโตรเจนถูกไล่ออก (denitrogenation) ถุงลมเหลือแต่ O₂ ซึ่งถูกดูดซึมเร็ว → **ยุบภายในไม่กี่ชั่วโมง** (สไลด์: resorption atelectasis เร็วขึ้นเมื่อหายใจ O₂)\n\nตัวเลือกอื่นไม่ใช่กลไกหลักในช่วงเวลาสั้นแบบนี้",
         "Resorption atelectasis เร็วขึ้นเมื่อให้ O₂ — ไม่มี N₂ ค้ำ", "Atelectasis mechanism", R("Atelectasis — types"), NLN + ["2.3.10(2)", "B6.2.3(5)"]),
     mcq(N(16), "A 66-year-old retired shipyard worker has an incidental 3.5 cm rounded subpleural opacity in the right lower lobe. CT shows it abuts an area of thickened pleura with an acute angle, bronchovascular bundles curve into its margin like a comet tail, and there is volume loss of the right lower lobe. What is the most likely diagnosis?",
         ["Rounded atelectasis", "Malignant pleural mesothelioma", "Bronchogenic carcinoma", "Pulmonary infarct", "Loculated empyema"], 0,
         "ครบ **3 องค์ประกอบของ rounded atelectasis** ✍️ \"3 component\"\n1. ติดกับ **pleura หนา/effusion**\n2. **ก้อนกลมใต้ pleura** ทำมุมแหลม\n3. **comet-tail sign** — หลอดเลือดและหลอดลมโค้งวนเข้าก้อน + volume loss\n\nกลไก: pleura ที่หนาจาก asbestos หดรั้งปอดส่วนติดกันให้ม้วนพับเป็นก้อน · ประวัติ **อู่ต่อเรือ (asbestos)** เข้ากัน\n\n- mesothelioma: pleura หนาเป็นปุ่มรอบปอด + effusion · ไม่มี comet tail\n- มะเร็งปอด: ขอบ spiculated ไม่มีหลอดเลือดวนเข้า\n- infarct: รูปลิ่มฐานที่ pleura · empyema: รูปเลนส์มุมป้าน",
         "Rounded atelectasis = pleura หนา + ก้อนใต้ pleura + comet tail", "Rounded atelectasis", R("Rounded atelectasis"), NLN + ["2.3.10(2)", "2.3.10-3(4)"]),
    ], NLN + ["2.3.10(2)", "B6.2.3(5)"],
    imgs=IMGS(
        IM(48, "Platelike (discoid) atelectasis", "CXR PA และ lateral มีแถบทึบบางแนวนอนที่ฐานปอดสองข้าง ลูกศรขาวชี้",
           cap="**Platelike/discoid atelectasis** — แถบทึบบางแนวนอนที่ฐานปอด (ลูกศร) ทั้ง PA และ lateral · พบหลังผ่าตัด/หายใจตื้น · หายได้เมื่อหายใจลึก ไอ ลุกเดิน"),
        IM(49, "ก้อนที่ฐานปอดขวา", "CXR PA มีความทึบไม่มีขอบชัดที่ฐานปอดขวาด้านนอกมีตัวอักษร ra มุม costophrenic ขวาทื่อ mediastinum เลื่อนไปทางขวาเล็กน้อย",
           q="ลองอ่านก่อน — ก้อนที่ฐานขวา + มุมทื่อ + mediastinum เลื่อน คิดถึงอะไร",
           quiz="**คำตอบ:** **Rounded atelectasis** (ra) · **จุดที่ต้องเห็น:** ทึบขอบไม่ชัดที่ฐานปอดขวา · **มุม costophrenic ขวาทื่อ** (pleura หนา/น้ำ) · **mediastinum เลื่อนไปขวา** (volume loss) · **กลไก:** pleura ที่หนาหดรั้งปอดส่วนติดกันให้ม้วนเป็นก้อน ✍️ \"3 component\" \"Specific\" · **ทำต่อ:** CT หา comet-tail · ถามประวัติ asbestos"),
        IM(72, "ซีกซ้ายขาวทั้งหมด — trachea ไปทางไหน", "CXR PA ซีกซ้ายทึบขาวทั้งหมด trachea และ mediastinum ถูกดันไปทางขวา ปอดขวาเห็นลายปอดปกติ",
           q="ลองอ่านก่อน — ซีกซ้ายขาวทั้งหมด trachea และ mediastinum ไปทางไหน แปลว่าอะไร",
           quiz="**คำตอบ:** **Massive pleural effusion** ซ้าย ✍️ \"Massive PE\" · **จุดที่ต้องเห็น:** ซีกซ้ายทึบทั้งหมด **trachea และ mediastinum ถูกดันไปขวา** = ซีกซ้ายมี **ปริมาตรเพิ่ม** · **กลไก:** น้ำหลายลิตรแทนที่ปอดและเบียดอวัยวะกลางอก · ถ้า trachea ถูก **ดึงเข้าหา** จะเป็น total collapse · อยู่กลาง = consolidation หรือ effusion + collapse · **ทำต่อ:** ultrasound + thoracentesis (คาบ Thoracentesis)"),
    ))

# ───────────────────────────── 9
sec("chest-img-09", "Lobar collapse ทีละกลีบ — RUL RML RLL LUL LLL",
    "RUL: minor fissure ยกขึ้น hilum ขวาสูง (Golden S ถ้ามีก้อน) · RML: ขอบหัวใจขวาหาย ลิ่มบน lateral · RLL: สามเหลี่ยมยอดที่ hilum · LUL: ม่านทึบ + Luftsichel · LLL: สามเหลี่ยมหลังหัวใจ flat waist", 12,
"""### ทิศทางการยุบของแต่ละกลีบ
กลีบปอดยึดอยู่ที่ **hilum** — เมื่อยุบจะ "พับ" เข้าหา hilum ตามทิศที่ fissure อนุญาต
| กลีบ | ยุบไปทาง | Frontal | Lateral |
|---|---|---|---|
| **RUL** | ขึ้นบน + เข้าใน (+ หน้า) | ทึบบน · **minor fissure ยกขึ้นโค้งขึ้น** · **hilum ขวายกสูง** · trachea ไปขวา · juxtaphrenic peak · SVC silhouette | minor fissure ขึ้น · major fissure ส่วนบนมาหน้า |
| **RML** | ลง + เข้าใน (บาง) | minor fissure มองไม่เห็น · ทึบจาง · **ขอบหัวใจขวาหาย** | minor fissure ลง · major fissure ส่วนล่างมาหน้า → **ลิ่มบางยอดที่ hilum** |
| **RLL** | ลง + หลัง + เข้าใน | **สามเหลี่ยมยอดที่ hilum ฐานที่โดม** · hilum ขวาลง · **interlobar PA หาย** · โดมขวาหาย · ขอบหัวใจขวายังอยู่ | major fissure ไปหลัง · โดมส่วนหลังหาย |
| **LUL** | ขึ้น + **ไปหน้า** (ไม่มี minor fissure) | **ม่านทึบจาง ๆ** ซีกซ้ายบน (จางลงเมื่อยุบมาก) · aortic knob หาย · trachea ไปซ้าย · **Luftsichel** · hilum ยก · juxtaphrenic peak | major fissure มาหน้า → ทึบด้านหน้ายาวขนาน sternum |
| **LLL** | ลง + หลัง + เข้าใน | **สามเหลี่ยมหลังหัวใจ** · โดมซ้ายหาย · Lt interlobar PA ไม่ชัด · **flat waist** · หัวใจเลื่อนซ้าย | major fissure ไปหลัง ✍️ "loss of retrocardiac space" |

### RUL collapse
[[img:c39]]

### Golden S sign
[[img:c40]]

### RML collapse
[[img:c41]]

[[img:c42]]

### RLL collapse
[[img:c43]]

### LUL collapse และ Luftsichel sign
- **Luftsichel** = "air crescent" (ภาษาเยอรมัน) — **superior segment ของ LLL พองชดเชย** แทรกเข้าระหว่าง LUL ที่ยุบไปข้างหน้ากับ mediastinum → แถบโปร่งรูปเสี้ยวล้อม **aortic knob**
- พบน้อยใน RUL collapse
- ✍️ ภาพในสไลด์: "**Lt > Rt (ปกติ Rt > Lt)**" — โดมซ้ายกลับสูงกว่าขวาเพราะถูกดึงขึ้น

[[img:c44]]

[[img:c45]]

### LLL collapse และ flat waist
[[img:c46]]

[[img:c47]]

#### ทำไมถึงเห็นแบบนี้
| สัญญาณ | กลไก | บอกอะไร |
|---|---|---|
| **Fissure เลื่อน** | fissure คือขอบของกลีบ — กลีบเล็กลง ขอบจึงถูกดึงตาม | direct sign ที่เชื่อถือได้มากที่สุด |
| **Hilum ขวาสูงเท่าซ้าย** | ปกติ hilum ซ้ายสูงกว่า 1–2 ซม. · RUL ยุบดึง hilum ขวาขึ้น ✍️ "ขึ้นมาพอ ๆ กับ Lt" | RUL volume loss |
| **Juxtaphrenic peak** | inferior accessory fissure/ligament ถูกดึงขึ้นเมื่อปอดบนยุบ เป็นยอดแหลมเล็กบนโดม | upper lobe collapse |
| **Luftsichel** | superior segment LLL พองชดเชย แทรกระหว่าง LUL ที่ยุบไปหน้ากับ aortic arch | LUL collapse |
| **Flat waist** | LLL ยุบดึงหัวใจหมุนไปซ้าย-หลัง ขอบ aortic knob–main PA ที่ปกติเว้าจึงแบนลง | LLL collapse |
| **ไม่มี air bronchogram** | หลอดลมส่วนต้นอุด ลมในหลอดลมก็ถูกดูดซึมด้วย | ก้อน/เสมหะอุดหลอดลมใหญ่ → bronchoscopy |
""",
    ["กลีบยุบเข้าหา hilum: RUL ขึ้น · RML/RLL/LLL ลง · LUL ไปหน้า",
     "RUL: minor fissure ยกขึ้น + hilum ขวาสูง · Golden S = มีก้อนที่ hilum → มะเร็ง",
     "RML: ขอบหัวใจขวาหาย · lateral เป็นลิ่มบางยอดที่ hilum",
     "LUL: ม่านทึบจาง + Luftsichel ล้อม aortic knob",
     "LLL: สามเหลี่ยมหลังหัวใจ โดมซ้ายหาย flat waist · ดู retrocardiac ทุกครั้ง"],
    [mcq(N(17), "A 64-year-old man who smokes 50 pack-years has haemoptysis. PA radiograph shows opacification of the right upper zone whose inferior margin is concave laterally and convex medially, forming a reversed S shape; the right hilum is elevated and the trachea is deviated to the right. What is the most appropriate next step?",
         ["Contrast CT of the chest followed by bronchoscopy", "Empirical antibiotics and repeat radiograph in 6 weeks", "Chest physiotherapy to clear a mucus plug", "Diagnostic thoracentesis", "Reassurance because this is a normal variant"], 0,
         "**Golden S sign** = **RUL collapse** (ส่วนนอกของ minor fissure ยกขึ้นเว้า) + **ก้อนที่ hilum** (ส่วนในโป่งลง) · hilum ขวายก trachea ไปขวา = volume loss ✍️ อาจารย์เขียน \"**Cancer**\"\n\nผู้สูบบุหรี่หนัก + ไอเป็นเลือด → **มะเร็งปอดชนิด central (มักเป็น squamous) อุดหลอดลม** จนกว่าจะพิสูจน์ได้ว่าไม่ใช่ → **CT ฉีดสี** (ขนาด ต่อมน้ำเหลือง ระยะ) + **bronchoscopy** เพื่อชิ้นเนื้อ\n\n- ให้ยาปฏิชีวนะแล้วรอ 6 สัปดาห์ = ช้าเกินไปเมื่อเห็นก้อน\n- physiotherapy ใช้กับ mucus plug ในผู้ป่วยหลังผ่าตัด ไม่ใช่ภาพที่มีก้อน\n- ไม่มีน้ำ จึงไม่เจาะปอด",
         "Golden S = RUL collapse + hilar mass → CT + bronchoscopy", "Lobar collapse", R("Golden's sign"), NLN + ["2.3.10(2)", "B6.2.4-3(2)", "3.3.20"]),
     mcq(N(18), "A frontal radiograph shows a triangular opacity behind the heart with its apex at the left hilum, loss of the medial left hemidiaphragm outline, a depressed left hilum, and a flattened left heart border. The left heart border itself remains visible. Which lobe has collapsed?",
         ["Left lower lobe", "Left upper lobe", "Lingula", "Right middle lobe", "Right lower lobe"], 0,
         "**LLL collapse**: ทึบ **สามเหลี่ยมหลังหัวใจ** ยอดที่ hilum ฐานที่โดม · **โดมซ้ายส่วนในหาย** · **hilum ซ้ายลง** · ขอบหัวใจซ้ายแบน = **flat waist sign** (หัวใจหมุนตาม volume loss) · ขอบหัวใจซ้ายยังเห็นเพราะ LLL อยู่หลัง ไม่แนบ LV\n\n- **LUL** ยุบไปหน้า เป็นม่านทึบซีกบน hilum ยกขึ้น\n- **lingula** ทำให้ขอบหัวใจซ้ายหาย\n- RML/RLL อยู่ฝั่งขวา\n\n✍️ อาจารย์: lateral จะ \"loss of retrocardiac space\"",
         "สามเหลี่ยมหลังหัวใจ + โดมซ้ายหาย + flat waist = LLL collapse", "Lobar collapse", R("LLL atelectasis"), NLN + ["2.3.10(2)"]),
    ], NLN + ["2.3.10(2)", "B6.2.3(5)"],
    imgs=IMGS(
        IM(39, "ปอดขวาบน — ดู minor fissure และ hilum", "CXR PA ปอดขวาส่วนบนทึบเล็กลง ลูกศรขาวใหญ่ชี้ขอบล่างที่โค้งขึ้น ลูกศรขาวเล็กชี้ hilum ขวาที่ยกสูง ลูกศรดำชี้ยอดแหลมบนโดมขวา",
           q="ลองอ่านก่อน — ลูกศรสามจุดชี้อะไร และรวมกันเป็นภาวะอะไร",
           quiz="**คำตอบ:** **RUL atelectasis** · **จุดที่ต้องเห็น:** ลูกศรขาวใหญ่ = **minor fissure ยกขึ้น (upward displacement)** ✍️ \"Direct sign\" · ลูกศรขาวเล็ก = **hilum ขวายก** และ descending PA หมุนออก ✍️ \"ขึ้นมาพอ ๆ กับ Lt\" · ลูกศรดำ = **juxtaphrenic peak** บนโดมขวา · **กลไก:** กลีบบนยุบเข้าหา hilum ดึง fissure, hilum และ ligament ใต้ปอดขึ้น"),
        IM(40, "ขอบล่างรูปตัว S กลับด้าน", "CXR PA ปอดขวาบนทึบ ลูกศรขาวชี้ขอบด้านนอกที่โค้งขึ้น ลูกศรดำสองอันชี้ขอบด้านในที่โป่งลงใกล้ hilum mediastinum ขวาบนพร่า โดมขวายก",
           q="ลองอ่านก่อน — ขอบล่างของเงาทึบมีรูปร่างอย่างไร บ่งอะไร",
           quiz="**คำตอบ:** **Golden's S sign** · **จุดที่ต้องเห็น:** ส่วนนอกของ minor fissure **ยกขึ้น (เว้า)** จาก atelectasis (ลูกศรขาว) + ส่วนใน **โป่งลง (นูน)** รอบ **ก้อนที่ hilum** (ลูกศรดำ) → reverse S ✍️ \"Reverse S\" · ขอบ mediastinum ขวาบนหาย · โดมขวายก · **ความหมาย:** ✍️ \"Cancer\" — มะเร็งปอดอุดหลอดลม RUL · **ทำต่อ:** CT + bronchoscopy"),
        IM(41, "ทึบข้างหัวใจขวา", "CXR PA มีป้าย Upright ความทึบรูปสามเหลี่ยมจาง ๆ ข้างหัวใจขวา ขอบหัวใจขวาพร่า",
           q="ลองอ่านก่อน — ทึบข้างหัวใจขวาเป็นรูปอะไร ขอบหัวใจขวาเป็นอย่างไร",
           quiz="**คำตอบ:** **RML atelectasis** · **จุดที่ต้องเห็น:** ทึบจาง ๆ **รูปสามเหลี่ยม** ✍️ \"triangular shade\" ข้างหัวใจขวา · **ขอบหัวใจขวาพร่า (silhouette)** · minor fissure มองไม่เห็น · **กลไก:** RML ยุบลงและเข้าใน ทำให้บาง ทึบน้อยลงเมื่อยุบมาก · ยืนยันด้วย lateral (ภาพถัดไป) · RML ยุบบ่อยเพราะหลอดลมยาว แคบ มีต่อมน้ำเหลืองล้อม (middle lobe syndrome)"),
        IM(42, "RML collapse บน lateral", "ภาพ lateral มีแถบทึบบางรูปลิ่มเฉียงจากด้านหน้าล่างไปยัง hilum ลูกศรขาวชี้ minor fissure ที่ลดลง ลูกศรดำชี้ major fissure ที่เลื่อนมาด้านหน้า",
           cap="**Thin wedge-shaped opacity with apex at the hilum** · minor fissure **ลง** (ลูกศรขาว) · major fissure **มาหน้า** (ลูกศรดำ)"),
        IM(43, "RLL atelectasis", "CXR PA มีความทึบรูปสามเหลี่ยมที่ฐานปอดขวาข้างหัวใจ ลูกศรขาวชี้ hilum ลูกศรดำชี้ขอบเงาที่เป็น major fissure",
           cap="**RLL** — สามเหลี่ยม **ยอดที่ hilum ฐานที่โดม** (ลูกศรดำ = major fissure ที่เลื่อน) · hilum ขวาลง · interlobar PA มองไม่เห็นเพราะจมในเงาทึบ · โดมขวาหาย · หัวใจ/mediastinum หมุนไปขวา"),
        IM(44, "ซีกซ้ายบนทึบจาง + แถบโปร่งรอบ aortic knob", "CXR PA ซีกซ้ายบนทึบจางแบบม่าน ลูกศรขาวเล็กชี้แถบโปร่งรูปเสี้ยวรอบ aortic knob ลูกศรขาวใหญ่ชี้ trachea ที่เบนไปซ้าย ลูกศรดำชี้ยอดแหลมบนโดมซ้าย",
           q="ลองอ่านก่อน — แถบโปร่งรูปเสี้ยวรอบ aortic knob คืออะไร",
           quiz="**คำตอบ:** **LUL atelectasis + Luftsichel sign** · **จุดที่ต้องเห็น:** ม่านทึบจาง ๆ ซีกซ้ายบน · **แถบโปร่งรูปเสี้ยว** ล้อม aortic knob (ลูกศรขาวเล็ก) = superior segment ของ LLL ที่พองชดเชย ✍️ \"เข้ามาแทนที่\" · **trachea ไปซ้าย** · left main bronchus ยก · **juxtaphrenic peak** (ลูกศรดำ) · โดมซ้ายสูงกว่าขวา ✍️ \"Lt > Rt (ปกติ Rt > Lt)\" · (กล่องในสไลด์เขียน RUL แต่ภาพนี้เป็นซ้าย)"),
        IM(45, "LUL collapse บน lateral", "ภาพ lateral มีลูกศรดำชี้ major fissure ที่เลื่อนมาด้านหน้าเป็นแนวยาวขนานกับ sternum ความทึบอยู่ด้านหน้า",
           cap="**Anterior displacement of major fissure** (ลูกศร) · LUL ยุบไปข้างหน้าเป็นแถบทึบขนาน sternum"),
        IM(46, "ทึบหลังหัวใจ", "CXR PA ทึบรูปสามเหลี่ยมหลังหัวใจด้านซ้าย ลูกศรขาวชี้ขอบ major fissure โดมซ้ายส่วนในหายไป หัวใจเลื่อนไปทางซ้าย ขอบหัวใจซ้ายแบน",
           q="ลองอ่านก่อน — ดูหลังหัวใจซ้าย โดมซ้าย และรูปขอบหัวใจซ้าย",
           quiz="**คำตอบ:** **LLL atelectasis** · **จุดที่ต้องเห็น:** ทึบ **สามเหลี่ยมหลังหัวใจ** (ขอบ = major fissure ที่ถูกดึง ✍️ \"major fissure\") · **โดมซ้ายส่วนในหาย** · หัวใจเลื่อนไปซ้าย · **ขอบหัวใจซ้ายแบน (flat waist)** · Lt interlobar PA ไม่ชัด · ซี่โครงซ้ายชิด · **บทเรียน:** ต้องดู retrocardiac ทุกฟิล์ม (hidden area)"),
        IM(47, "LLL collapse บน lateral", "ภาพ lateral มีลูกศรขาวชี้ major fissure ที่เลื่อนไปด้านหลัง ความทึบอยู่ด้านหลังล่างทับกระดูกสันหลัง",
           cap="**Posterior displacement of major fissure** (ลูกศร) · ✍️ \"**loss of retrocardiac space**\" — ช่องหลังหัวใจที่ปกติโปร่งกลายเป็นทึบ"),
    ))

# ───────────────────────────── 10
sec("chest-img-10", "Nodule และ mass — ในหรือนอกปอด · Fleischner · มะเร็งปอดบนฟิล์ม",
    "Nodule < 3 ซม. · mass ≥ 3 ซม. · ในปอด = มุมแหลม ขอบครบ · นอกปอด = มุมป้าน ขอบเรียว · ก้อนจาก CXR: เทียบฟิล์มเก่าก่อน → CT · Fleischner 2017 · central SCC/small cell · Pancoast · SVC", 12,
"""### นิยาม
- **Nodule < 3 ซม. · Mass ≥ 3 ซม.** ✍️ "complete border" (ก้อนในปอดมีลมล้อมรอบจึงเห็นขอบครบ)
- **Solitary pulmonary nodule (SPN)** — focal opacity บน CXR หรือ CT · ค่อนข้างขอบชัด · **ล้อมด้วยปอดอย่างน้อยบางส่วน** · ค่อนข้างกลม · **≤ 3 ซม.**

[[img:c50]]

### ก้อนอยู่ในปอดหรือนอกปอด — ดูมุม
[[img:c51]]

[[img:c52]]

[[img:c53]]

### ลักษณะที่ช่วยแยก benign กับ malignant
สไลด์ให้เฉพาะนิยามและขนาด ส่วนนี้อิงตำราและ Fleischner
| ลักษณะ | ค่อนไปทาง benign | ค่อนไปทาง malignant |
|---|---|---|
| ขนาด | < 6 มม. | ≥ 8 มม. · ใหญ่ขึ้นยิ่งเสี่ยง |
| ขอบ | เรียบ คม | **spiculated** · lobulated |
| หินปูน | **diffuse · central · laminated (เป็นวง) · popcorn (hamartoma)** | eccentric/stippled หรือไม่มี |
| การเปลี่ยนแปลง | **solid คงที่ ≥ 2 ปี** · โตเร็วมาก (< 20 วัน = ติดเชื้อ) | doubling time ~20–400 วัน |
| ผู้ป่วย | อายุน้อย ไม่สูบ | อายุมาก สูบบุหรี่ ประวัติมะเร็ง ปอดบน emphysema |

### ก้อนจาก CXR — ทำอะไรก่อน
1. **หาฟิล์มเก่ามาเทียบ** — ถ้าคงที่ ≥ 2 ปี (solid) หรือมีหินปูนแบบ benign ชัด ไม่ต้องทำต่อ
2. ถ้าใหม่หรือไม่แน่ใจ → **CT ทรวงอก** (ยืนยันว่าอยู่ในปอดจริง ขนาด ลักษณะ หินปูน ต่อมน้ำเหลือง)
3. ใช้ **Fleischner 2017** กับก้อนที่พบโดยบังเอิญบน CT (อายุ ≥ 35 ปี ไม่มีมะเร็ง ไม่ภูมิคุ้มกันบกพร่อง)

| Solid nodule เดี่ยว (CT) | ความเสี่ยงต่ำ | ความเสี่ยงสูง |
|---|---|---|
| **< 6 มม.** | ไม่ต้องติดตาม | CT ซ้ำที่ 12 เดือน (ไม่บังคับ) |
| **6–8 มม.** | CT 6–12 เดือน แล้วพิจารณา 18–24 เดือน | CT 6–12 เดือน **และ** 18–24 เดือน |
| **> 8 มม.** | พิจารณา CT 3 เดือน · **PET/CT** · หรือ **ตัดชิ้นเนื้อ** | เหมือนกัน |

### มะเร็งปอดบนฟิล์ม — clinical correlation
| สิ่งที่เห็น/อาการ | คิดถึง |
|---|---|
| **ก้อนที่ hilum + lobar collapse / Golden S** | central tumour — **squamous cell** หรือ **small cell** |
| **ก้อนมีโพรงผนังหนา** | **squamous cell** (หัวข้อถัดไป) |
| **ก้อนที่ apex** (hidden area) + ปวดไหล่/แขนด้านใน + **Horner** | **Pancoast (superior sulcus) tumour** — บุก brachial plexus C8–T1 และ sympathetic chain |
| **หน้า แขนบวม หลอดเลือดดำคอ/อกโป่งไม่เต้น** + ก้อน RUL/mediastinum | **SVC syndrome** |
| **Na ต่ำ** ใน central tumour + ต่อมน้ำเหลือง mediastinum โตเร็ว | **small cell — SIADH** (ACTH, Lambert–Eaton) |
| **Ca สูง** | squamous cell — **PTHrP** |
| **Mediastinal node โตบน CT/PET** ในผู้ที่จะผ่าตัด | ยืนยันระยะด้วย **EBUS-TBNA** ก่อน (ACCP) |
""",
    ["Nodule < 3 ซม. · mass ≥ 3 ซม.",
     "ในปอด: มุมแหลม ขอบครบ · นอกปอด: มุมป้าน ขอบเรียว ขอบด้านผนังหาย + ดูซี่โครง",
     "ก้อนจาก CXR: เทียบฟิล์มเก่าก่อน → CT · solid คงที่ ≥ 2 ปี = benign",
     "Fleischner 2017: < 6 มม. ไม่ต้องติดตาม (เสี่ยงต่ำ) · > 8 มม. → CT 3 เดือน/PET/biopsy",
     "Central: squamous (Ca↑ cavitation) · small cell (SIADH) · apex: Pancoast"],
    [mcq(N(19), "A 38-year-old non-smoker has an incidental 2 cm smooth, well-circumscribed nodule in the left lower lobe. CT shows coarse 'popcorn' calcification and small areas of fat attenuation within it. What is the most likely diagnosis?",
         ["Pulmonary hamartoma", "Adenocarcinoma of the lung", "Squamous cell carcinoma", "Carcinoid tumour", "Solitary metastasis from osteosarcoma"], 0,
         "หินปูนแบบ **popcorn** + **ไขมันในก้อน** = **hamartoma** (benign tumour ที่มีกระดูกอ่อน ไขมัน และเนื้อเยื่ออื่น) — หินปูนแบบ benign อื่น: diffuse, central, laminated\n\nกลไก: กระดูกอ่อนในก้อนสะสมแคลเซียมเป็นก้อนเล็ก ๆ คล้ายข้าวโพดคั่ว · ไขมัน (−40 ถึง −120 HU) แทบไม่พบในมะเร็งปอด\n\n- adenocarcinoma/SCC: ขอบ spiculated หินปูนผิดปกติหรือไม่มี\n- carcinoid: มักอยู่ส่วนกลาง มีหินปูนได้แต่ไม่มีไขมัน\n- metastasis จาก osteosarcoma มีกระดูกได้ แต่มักหลายก้อนและมีประวัติมะเร็ง",
         "Popcorn calcification + fat = hamartoma", "Solitary pulmonary nodule", ["Fleischner Society 2017 guideline", "สไลด์ อ.พจนี — Solitary pulmonary nodule"], NLN + ["B6.2.4-3(1)", "3.3.20"]),
     mcq(N(20), "A 59-year-old smoker has 4 months of severe right shoulder pain radiating down the inner arm, weakness of the intrinsic hand muscles, and right ptosis with miosis. Which radiographic area is most important to scrutinise?",
         ["The right lung apex", "The retrocardiac region", "The right costophrenic angle", "The left hilum", "The subdiaphragmatic region"], 0,
         "ปวดไหล่ร้าวแขนด้านใน + กล้ามเนื้อมือ (C8–T1) อ่อนแรง + **Horner syndrome** = **Pancoast (superior sulcus) tumour** ที่ **ยอดปอด** บุก brachial plexus และ sympathetic chain/stellate ganglion\n\n**Apex เป็น hidden area** ในสไลด์ (\"Apices (pancoast tumour)\") — ซ่อนหลัง clavicle และซี่โครงแรก · ดูความหนาของ apical cap เทียบสองข้าง ซี่โครง 1–3 กร่อน · ใช้ lordotic view หรือ CT/MRI\n\nบริเวณอื่นไม่อธิบายกลุ่มอาการนี้",
         "Horner + ปวดไหล่แขน = Pancoast ที่ apex (hidden area)", "Lung cancer correlation", R("Hidden areas") + ["ตำราอายุรศาสตร์ — superior sulcus tumour"], NLN + ["B6.2.4-3(2)"]),
    ], NLN + ["B6.2.4-3(2)", "B6.2.4-3(1)", "3.3.20", "2.2.13"],
    imgs=IMGS(
        IM(50, "Nodule เทียบ mass", "CXR สองภาพ ซ้ายมีก้อนกลมเล็กในปอดขวาส่วนกลางป้าย Nodule size น้อยกว่า 3 cm ขวามีก้อนใหญ่ที่ hilum ขวาป้าย Mass size มากกว่าหรือเท่ากับ 3 cm",
           cap="ซ้าย **nodule (< 3 ซม.)** ✍️ \"complete border\" · ขวา **mass (≥ 3 ซม.)** ที่ hilum ขวา — ก้อนใหญ่ที่ hilum ในผู้สูบบุหรี่ = มะเร็งชนิด central จนกว่าจะพิสูจน์ได้ว่าไม่ใช่"),
        IM(51, "Intraparenchymal lesion", "CXR PA มีก้อนกลมขอบคมใน LLL วงกลมสีแดงและเครื่องหมายดอกจันที่ก้อน ลูกศรเหลืองชี้มุมแหลมระหว่างก้อนกับ pleura คู่กับภาพ CT แสดงก้อนกลมในปอดซ้ายส่วนหลัง",
           cap="**Well-defined, sharply marginated rounded mass, acute angle to adjacent pleura in LLL** · ก้อนในเนื้อปอดมีลมล้อมรอบ → ขอบครบ มุมแหลม (ลูกศรเหลือง) · ซ้อนหลังหัวใจแต่ขอบหัวใจยังคม = คนละระนาบ"),
        IM(52, "ก้อนนี้อยู่ในปอดหรือไม่", "CXR PA และ lateral มีก้อนกลมที่ปอดขวาส่วนล่างติดขอบ mediastinum วงกลมสีชมพูล้อมก้อน ลูกศรและเส้นเหลืองชี้มุมป้านที่ขอบบนและล่างของก้อนกับ mediastinum บนภาพ lateral มีวงกลมแสดงตำแหน่งก้อน",
           q="ลองอ่านก่อน — ขอบก้อนครบรอบไหม มุมกับโครงสร้างข้างเคียงเป็นอย่างไร",
           quiz="**คำตอบ:** **Extrapulmonary lesion** · **จุดที่ต้องเห็น:** ขอบด้านที่ติดโครงสร้างข้างเคียง **หายไป (incomplete border)** และทำ **มุมป้าน** (ลูกศรเหลือง) · ขอบด้านปอดคมเรียบ · **กลไก:** ก้อนนอกปอดดันเยื่อหุ้มปอดเข้ามา มีลมล้อมเพียงด้านเดียว · lateral ช่วยบอกตำแหน่งหน้า–หลัง · **ทำต่อ:** CT"),
        IM(53, "ก้อนติดผนังอก — ดูซี่โครง", "ภาพขยายผนังทรวงอกมีก้อนเรียบนูนเข้าปอด ขอบเรียวทำมุมป้านกับผนัง ลูกศรดำชี้ซี่โครงด้านหน้าที่ถูกกร่อน",
           q="ลองอ่านก่อน — มุมของก้อนกับผนังอก และซี่โครงตรงลูกศร",
           quiz="**คำตอบ:** **Extrapulmonary (chest wall) lesion + lytic anterior rib** · **จุดที่ต้องเห็น:** ก้อนเรียบนูนเข้าปอด **ขอบเรียว (tapering) มุมป้าน** ✍️ \"มุมป้านกับ chest wall\" · ซี่โครงหน้า **ถูกกร่อน (lytic)** ที่ลูกศร · **DDx:** **metastasis ที่ซี่โครง** (ปอด เต้านม ไต ไทรอยด์) · **multiple myeloma** · chondrosarcoma · **บทเรียน:** กระดูกเป็น hidden area"),
    ))

# ───────────────────────────── 11
sec("chest-img-11", "Cavity, cyst, bulla, pneumatocele และ lung abscess",
    "Cyst ผนังเรียบ ≤ 3 มม. · cavity ผนังหนา/ขรุขระ · cavitation ~10% ของมะเร็ง SCC 80% small cell แทบไม่เกิด · bleb < 1 ซม. · bulla ≥ 1 ซม. ผนัง < 1 มม. · pneumatocele: S. aureus PJP · abscess: air-fluid level", 10,
"""### Cyst หรือ cavity
| | **Cyst** ✍️ "กลม ๆ มีความกลวง" | **Cavity** |
|---|---|---|
| ผนัง | **เรียบ สม่ำเสมอ ≤ 3 มม.** (มี epithelium หรือ fibrous wall) | **หนากว่า หรือขรุขระ** · หรือเป็นช่องลมที่ **กำลังเกิด** ในเนื้อทึบ |
| ขนาด | ≥ 1 ซม. | ใดก็ได้ |
| หมายเหตุ | ผนังบางเป็นได้ทั้งสองอย่าง · **cyst ที่ผนังหนาขึ้น = ติดเชื้อหรือเนื้องอก** | ผนังหนา/ขรุขระ = cavity (ยกเว้น infected cyst) |

### Cavity เกิดได้อย่างไร
[[img:c54]]

**มะเร็งกับโพรง** (สไลด์)
- cavitation พบ **~10% ของมะเร็งปอด** · **squamous cell carcinoma บ่อยที่สุด (80%)** · รองลงมา large cell และ adenocarcinoma
- **small cell แทบไม่ cavitate**
- โพรงจากมะเร็ง **ผนังหนา เป็นปุ่ม (nodular)** · โพรง benign มัก **ผนังบางเรียบ**

[[img:c55]]

### Cyst และช่องลมผนังบาง
| ชนิด | นิยาม (สไลด์) | ความหมายทางคลินิก |
|---|---|---|
| **Bleb** | ลมอยู่ **ใน visceral pleura** · **< 1 ซม.** · ที่ **ยอดปอด** · ลมจากถุงลมแตกเซาะเข้า interstitium | แตก → **primary spontaneous pneumothorax** (ชายสูงผอม) |
| **Bulla** | **≥ 1 ซม.** ผนังเรียบ **< 1 มม.** · อาจมีผนังกั้น · มักเป็น **paraseptal emphysema** ใต้ pleura ใหญ่สุดที่ apex · อาจมีน้ำจากติดเชื้อ เลือด เนื้องอก | bullous emphysema · pneumothorax |
| **Pneumatocele** | ผนังบาง **โตขึ้นในหลายวัน–สัปดาห์** · กลไก check-valve หรือผนังหลอดลมตายแล้วลมเซาะ | หลัง pneumonia จาก **S. aureus**, **Pneumocystis** · **หายเองในสัปดาห์–เดือน** |
| **Cyst อื่น ๆ** | honeycombing · cystic bronchiectasis · subacute HP · trauma (laceration) · healing cavities · **parasite** ✍️ ✓ | ดูการกระจายและประวัติ |

[[img:c56]]

### Lung abscess
- โพรงที่มีหนอง ผนังหนาไม่เรียบ มัก **air-fluid level** · ✍️ "**alveolar process**" — เริ่มจาก pneumonia ที่เนื้อตาย (anaerobe จากการสำลัก, S. aureus, Klebsiella)
- แยกจาก **empyema** ที่มี air-fluid level (ไม่อยู่ในสไลด์ — อิงตำรา)

| | **Lung abscess** | **Empyema (มีลมจาก bronchopleural fistula)** |
|---|---|---|
| รูปร่าง | กลม | รูปเลนส์ ตามผนัง |
| มุมกับผนัง | **แหลม** | **ป้าน** |
| air-fluid level บน PA vs lateral | **ยาวเท่ากัน** (ทรงกลม) | **ยาวไม่เท่ากัน** |
| CT | ผนังหนาไม่เรียบ หลอดเลือดสิ้นสุดที่ขอบ | split pleura sign · ดันปอดออก |
| รักษา | ยาปฏิชีวนะนาน (ส่วนใหญ่ไม่ต้องระบาย) | **ต้องระบาย** (ICD) |

[[img:c57]]
""",
    ["Cyst: ผนังเรียบ ≤ 3 มม. · cavity: ผนังหนา/ขรุขระ",
     "มะเร็ง cavitate ~10% · SCC 80% · small cell แทบไม่ cavitate",
     "Bleb < 1 ซม. ใน visceral pleura → PSP · bulla ≥ 1 ซม. ผนัง < 1 มม.",
     "Pneumatocele: S. aureus, PJP · โตเร็ว หายเอง",
     "Abscess: กลม มุมแหลม air-fluid level ยาวเท่ากันสอง view · empyema: รูปเลนส์ ยาวไม่เท่า ต้องระบาย"],
    [mcq(N(21), "A 67-year-old heavy smoker has a 5 cm right upper lobe mass with a central cavity. The cavity wall is 15 mm thick with an irregular, nodular inner margin, and a small air-fluid level is present. He is afebrile. Which histological type of lung cancer is most likely?",
         ["Squamous cell carcinoma", "Small cell carcinoma", "Bronchial carcinoid", "Adenocarcinoma in situ", "Metastatic thyroid carcinoma"], 0,
         "สไลด์: cavitation พบราว **10% ของมะเร็งปอด** และ **~80% เป็น squamous cell carcinoma** · โพรงจากมะเร็ง **ผนังหนา เป็นปุ่ม ขรุขระ**\n\nกลไก: SCC โตเร็วและ keratinize → ตรงกลางขาดเลือดตาย (central necrosis) → ระบายทางหลอดลม → โพรง + air-fluid level\n\n- **small cell แทบไม่ cavitate** (โตเร็วแต่ไปทางต่อมน้ำเหลือง/mediastinum)\n- carcinoid เป็นก้อนเรียบในหลอดลม · adenocarcinoma in situ เป็น GGO เล็ก · metastasis จาก thyroid เป็น miliary",
         "โพรงผนังหนาเป็นปุ่มในผู้สูบบุหรี่ = SCC", "Cavitation", R("Cavitation, Squamous cell CA"), NLN + ["B6.2.4-3(2)"]),
     mcq(N(22), "A patient with fever and foul-smelling sputum has a cavitary lesion with an air-fluid level in the right lower zone. On the PA view the air-fluid level is 6 cm long and on the lateral view it is also about 6 cm long; the lesion makes an acute angle with the chest wall. What is the most likely diagnosis?",
         ["Lung abscess", "Empyema with a bronchopleural fistula", "Hydropneumothorax", "Infected bulla with a very thin wall", "Loculated pleural effusion"], 0,
         "โพรงที่ **กลม** ทำมุม **แหลม** กับผนัง และ **air-fluid level ยาวเท่ากันทั้ง PA และ lateral** (เพราะโพรงเป็นทรงกลม) = **lung abscess** ในเนื้อปอด ✍️ \"alveolar process\"\n\nเสมหะเหม็น = anaerobe จากการสำลัก\n\n- **empyema** เป็นรูปเลนส์ตามผนังอก มุมป้าน air-fluid level **ยาวไม่เท่ากัน** ใน 2 view\n- hydropneumothorax: ระดับน้ำยาวเต็มความกว้างของซีก ไม่มีผนังโพรง\n- bulla ที่ติดเชื้อผนังบางมาก · loculated effusion ไม่มีลม",
         "Air-fluid level ยาวเท่ากันสอง view + มุมแหลม = lung abscess", "Lung abscess", R("Lung abscess") + ["ตำรารังสีวิทยาทรวงอก — abscess vs empyema"], NLN + ["2.3.10(5)", "2.3.10-3(2)"]),
    ], NLN + ["2.3.10(5)", "B6.2.4-3(2)", "B6.2.2(4)"],
    imgs=IMGS(
        IM(54, "ก้อนใกล้ hilum ซ้าย", "CXR PA มีก้อนใหญ่ทรงกลมที่ปอดซ้ายส่วนกลางใกล้ hilum ภายในมีช่องโปร่ง ผนังหนา",
           q="ลองอ่านก่อน — ก้อนนี้มีอะไรข้างใน ผนังเป็นอย่างไร",
           quiz="**คำตอบ:** **Cavity** — large, round, **thick-walled** lung cavity ที่ Lt middle zone ใกล้ hilum · **จุดที่ต้องเห็น:** ช่องโปร่งในก้อน ผนังหนา (ไม่ใช่ cyst ผนังบาง) ✍️ cyst / cavity · มีน้ำก้นโพรง ✍️ \"fluid\" · **DDx:** **SCC** · **TB** · lung abscess · GPA · **ทำต่อ:** sputum AFB/Xpert, CT, bronchoscopy"),
        IM(55, "Squamous cell CA — cavitary mass", "ภาพ CXR ขยายมีก้อนที่มีโพรงในปอด คู่กับภาพ CT ก้อนมีโพรงผนังหนาขรุขระเป็นปุ่ม มีระดับลมกับน้ำ ลูกศรขาวชี้ผนัง ลูกศรดำชี้ระดับน้ำ",
           cap="**Squamous cell carcinoma** — cavitary mass มี **air-fluid level** (ลูกศรดำ) · **ขอบหนา เป็นปุ่ม ผนังขรุขระ** (ลูกศรขาว)"),
        IM(56, "CT ผู้ป่วย HIV", "ภาพ CT ปอดทั้งสองข้างเป็นฝ้าขาวจางทั่วและมีถุงลมผนังบางหลายถุงรวมกันเป็นกลุ่มโดยเฉพาะปอดบน",
           q="ผู้ป่วย HIV CD4 ต่ำ หอบ — ลองอ่าน CT นี้ก่อน",
           quiz="**คำตอบ:** **PJP pneumonia** (ในสไลด์อาจารย์วงไว้) · **จุดที่ต้องเห็น:** **ground-glass opacity ทั่ว** + **ถุงผนังบางหลายถุงเป็นกลุ่ม (pneumatoceles)** · **กลไก:** Pneumocystis ทำให้ถุงลมเต็มของเหลวโปรตีน (GGO) และผนังหลอดลมฝอยเสียจนลมเซาะเป็นถุง · ถุงแตก → **pneumothorax** ได้ · **ทำต่อ:** induced sputum/BAL · co-trimoxazole + steroid ถ้า PaO₂ < 70"),
        IM(57, "Lung abscess", "ภาพ CT ฉีดสีมีโพรงขอบไม่เรียบเต็มไปด้วยน้ำ ผนังขอบติดสี ลูกศรขาวชี้ คู่กับ CXR PA ปอดขวาส่วนกลางล่างทึบมีขอบเขตเป็นวงประ",
           cap="**Lung abscess** — CT: โพรง **ขอบไม่เรียบ มีน้ำ ผนังติดสี (wall enhancement)** · CXR: ทึบปอดขวากลาง–ล่างที่เริ่มจาก pneumonia ✍️ \"alveolar process\""),
    ))

# ───────────────────────────── 12
sec("chest-img-12", "ปอดดำเกิน — emphysema, bulla, Westermark และ bronchiectasis",
    "Hyperlucency: ผนังอก · ลมเกินทั่วปอด (emphysema) หรือเฉพาะที่ (FB air trapping) · หลอดเลือดน้อย (PE, Swyer-James) · overinflation: lung height ≥ 29.9 ซม. โดมแบน retrosternal > 2.5 ซม. · bronchiectasis: tram tracks signet ring", 11,
"""### ปอดดำเกิน (decreased lung density) — คิดเป็น 3 กลุ่ม
| กลุ่ม | ตัวอย่าง (สไลด์) |
|---|---|
| **ผนังอกบางลง** | Poland syndrome (ไม่มี pectoralis) · **mastectomy** |
| **ลมเกิน — ทั่วไป** | **emphysema** (overinflation) |
| **ลมเกิน — เฉพาะที่** | **air trapping:** bronchial atresia, congenital lobar emphysema, **distal endobronchial foreign body** · **ไม่มี air trapping (ชดเชย):** หลังผ่าตัดปอด, ข้างเคียงกลีบที่ยุบ |
| **หลอดเลือดน้อย (oligemia)** | **PE** · emphysema (ทำลายหลอดเลือดปลาย) · unilateral absence of PA (TOF) · PPH · non-vascular: **Swyer-James-McLeod** · bronchial obstruction (hypoxic vasoconstriction) |

### Emphysema — overinflation
[[img:c61]]

[[img:c62]]

[[img:c58]]

### ลมค้างเฉพาะที่ — foreign body
- สิ่งแปลกปลอมในหลอดลมทำหน้าที่เป็น **ลิ้นทางเดียว (check valve)** — ลมเข้าได้ตอนหายใจเข้า (หลอดลมขยาย) แต่ออกไม่ได้ตอนหายใจออก
- ฟิล์มหายใจเข้าอาจปกติ → **ฟิล์มหายใจออก** (หรือ decubitus ในเด็ก): ข้างที่อุด **ยังพองค้าง** mediastinum ถูกดันไปอีกข้าง (ไม่อยู่ในสไลด์ — เทคนิคมาตรฐาน)

### Oligemia และ Westermark sign
- **Westermark sign** — ปอดบริเวณหลัง PE **โปร่งขึ้น หลอดเลือดหาย** ✍️ "Oligemia" · อาจเห็น PA ส่วนต้นโตจากลิ่มเลือด · **specific แต่ไม่ sensitive** (ฟิล์มใน PE ส่วนใหญ่ปกติ)

[[img:c59]]

### Bronchiectasis
- **ขยายถาวรของหลอดลมเฉพาะที่ (> 2–3 มม.)** · ผนังหนา อักเสบ สูญเสียกล้ามเนื้อและ elastic → ถูกเนื้อเยื่อรอบ ๆ ดึงให้ขยาย · หลอดลมเล็กอุดตัน แขนงลดลง
- ✍️ "**Normal จะเรียวเล็กลงที่ periphery**" — bronchiectasis **ไม่เรียว (lack of tapering)**

| สัญญาณ | คืออะไร |
|---|---|
| **Tram tracks** | เส้นขนานคู่ = ผนังหลอดลมหนาที่วิ่งขนานกับลำแสง |
| **Signet-ring sign** (CT) | หลอดลม (วง) **ใหญ่กว่า pulmonary artery ข้างเคียง** (หัวแหวน) → bronchoarterial ratio > 1 |
| **Finger-in-glove / hand-in-glove** | เสมหะอุดในหลอดลมที่ขยาย เป็นแท่ง/กิ่งทึบ |
| **Tree-in-bud** | หลอดลมฝอยเต็มหนอง/เสมหะ (varicose, infection) |
| **ชนิด** | **cylindrical** (ขนาน) · **varicose** (เป็นปล้อง) · **cystic** (ถุง > 2 ซม. มี air-fluid level) |

[[img:c60]]

#### ทำไมถึงเห็นแบบนี้
| สิ่งที่เห็น | กลไก | ความหมาย |
|---|---|---|
| **โดมแบน ต่ำ** | ปอดพองค้างดันกะบังลมลง กล้ามเนื้อทำงานเสียเปรียบ | overinflation (COPD) |
| **retrosternal space ลึก (> 2.5 ซม.)** | ปอดส่วนหน้าพองแทรกระหว่าง sternum กับ aorta | overinflation |
| **หัวใจแคบยาว** | โดมต่ำดึง mediastinum ลง | emphysema ไม่ใช่หัวใจเล็กจริง |
| **ปอดดำ หลอดเลือดปลายเล็กลง** | ผนังถุงลมและ capillary bed ถูกทำลาย | emphysema · ถ้าเฉพาะที่หลัง PE = Westermark |
| **hila เด่น** | ความดันในหลอดเลือดปอดสูงจากการสูญเสีย capillary bed | pulmonary hypertension จาก COPD |
| **ข้างหนึ่งดำค้างตอนหายใจออก** | check-valve ลมเข้าได้ออกไม่ได้ | foreign body (มักหลอดลมขวา) |
""",
    ["Hyperlucency: ผนังอก · ลมเกิน (ทั่ว/เฉพาะที่) · หลอดเลือดน้อย",
     "Overinflation: lung height ≥ 29.9 ซม. · โดมแบน · retrosternal > 2.5 ซม. · โดมต่ำกว่า anterior 7th rib",
     "Bulla ≥ 1 ซม. ผนัง < 1 มม. · bullae ใหญ่ดันปอดปกติลงล่าง",
     "Westermark = oligemia หลัง PE (specific ไม่ sensitive)",
     "Bronchiectasis: ไม่เรียว · tram tracks · signet ring (bronchus > artery)"],
    [mcq(N(23), "A 3-year-old boy developed sudden coughing while eating peanuts. Inspiratory chest radiograph is nearly normal. On an expiratory film the right lung remains hyperlucent and large while the mediastinum shifts to the left. What is the mechanism of these findings?",
         ["Check-valve obstruction of the right main bronchus allowing air in on inspiration but not out on expiration", "Complete obstruction of the right main bronchus with resorption atelectasis", "Right tension pneumothorax from alveolar rupture", "Compensatory overinflation after left lower lobe collapse", "Reflex vasoconstriction causing right-sided oligaemia"], 0,
         "สิ่งแปลกปลอม (มักไปหลอดลม **ขวา** เพราะสั้น กว้าง ชันกว่า) ทำหน้าที่เป็น **ลิ้นทางเดียว (check valve)**: หายใจเข้าหลอดลมขยาย ลมผ่านได้ · หายใจออกหลอดลมแคบลง ลมออกไม่ได้ → **air trapping** · ฟิล์มหายใจออก ข้างที่อุดยัง **พองและดำ** ดัน mediastinum ไปอีกข้าง (สไลด์: local excess of air — distal endobronchial FB)\n\n- อุดสนิทจะเกิด **collapse** (ทึบ volume ลด) ไม่ใช่ดำ\n- pneumothorax ต้องเห็น pleural line\n- compensatory overinflation ไม่มี air trapping",
         "FB check valve → air trapping เห็นชัดในฟิล์มหายใจออก", "Local excess of air", R("Local excess of air"), NLN + ["B6.2.3(1)"]),
     mcq(N(24), "On high-resolution CT of a patient with chronic productive cough, a bronchus seen in cross-section has an internal diameter clearly larger than that of the accompanying pulmonary artery, and peripheral bronchi fail to taper. What is the diagnosis?",
         ["Bronchiectasis", "Centrilobular emphysema", "Pulmonary arterial hypertension", "Lymphangitic carcinomatosis", "Hypersensitivity pneumonitis"], 0,
         "**Signet-ring sign** — หลอดลม (วงแหวน) **ใหญ่กว่า pulmonary artery ข้างเคียง** (หัวแหวน) = bronchoarterial ratio > 1 + **lack of tapering** = **bronchiectasis**\n\nปกติหลอดลมกับหลอดเลือดแดงขนาดใกล้กัน และ ✍️ \"normal จะเรียวเล็กลงที่ periphery\"\n\nกลไก: การติดเชื้อ-อักเสบซ้ำ (vicious circle) ทำลายกล้ามเนื้อและ elastic ในผนัง → หลอดลมถูกดึงขยายถาวร\n\n- emphysema: ช่องลมไม่มีผนัง ไม่ใช่หลอดลม\n- PAH: **artery** โต (ratio < 1)",
         "Bronchus > artery = signet ring = bronchiectasis", "Bronchiectasis", R("Bronchiectasis, Cylindrical bronchiectasis"), NLN + ["2.3.10(5)", "3.3.20"]),
    ], NLN + ["2.3.10(3)", "2.3.10(5)", "B6.2.2(5)"],
    imgs=IMGS(
        IM(61, "Overinflation — สัญญาณบน PA และ lateral", "CXR PA และ lateral พร้อมกล่องข้อความ lung height เพิ่ม lucent lung และหลอดเลือดเล็ก prominence of hila blunt costophrenic angle โดมขวาต่ำกว่าซี่โครงหน้าที่ 7 retrosternal space ลึกและโปร่ง diaphragms flattened and inverted",
           cap="↑ **lung height** · **ปอดโปร่ง หลอดเลือดเล็ก** · **hila เด่น** · **โดมขวาต่ำกว่า anterior 7th rib** · มุม costophrenic ทื่อ (โดมแบน) · lateral: **retrosternal space ลึกและโปร่ง** · **โดมแบน/กลับด้าน** · ✍️ \"Flat\""),
        IM(62, "PA + lateral ผู้สูบบุหรี่หอบเรื้อรัง", "CXR PA และ lateral ปอดบนสองข้างโปร่งมากไม่มีลายปอด เห็นผนังบาง ๆ ของถุงลมใหญ่ ปอดส่วนล่างถูกดันลงเห็นลายปอดหนาแน่นขึ้น ลูกศรขาวชี้ผนังบนภาพ lateral",
           q="ลองอ่านก่อน — ปอดบนโปร่งเพราะอะไร และปอดล่างเป็นอย่างไร",
           quiz="**คำตอบ:** **Bullous emphysema** · **จุดที่ต้องเห็น:** **bullae ใหญ่ในปอดบน** ไม่มีลายปอด เห็นผนังบาง (ลูกศร) · **ปอดปกติถูกดันลงฐาน** ลายปอดล่างจึงหนาแน่น · **กลไก:** paraseptal/centrilobular emphysema รวมเป็นถุงใหญ่ · **ระวัง:** bulla ใหญ่แยกจาก pneumothorax โดยดูผนังโค้งเว้าเข้าด้านใน (ไม่ใช่ขอบปอดขนานผนังอก) — ใส่สายผิดจะเกิด bronchopleural fistula"),
        IM(58, "Bullae บน CT และ CXR", "ภาพ CT มี bullae ใต้ pleura หลายถุงทั้งสองข้าง คู่กับ CXR ที่มีถุงลมผนังบางหลายถุงในปอดขวาบางถุงมีระดับน้ำ",
           cap="**Bullous emphysema with large subpleural bullae** (CT) · **Multiple thin-walled bullae with air-fluid levels** (CXR) — น้ำในถุงจากติดเชื้อหรือเลือดออก"),
        IM(59, "ปอดขวาโปร่งกว่าซ้าย", "CXR AP ปอดขวาโปร่งกว่าซ้ายทั้งซีก หลอดเลือดในปอดขวาน้อยลง ลูกศรขาวชี้ pulmonary artery ขวาที่โตขึ้น",
           q="ลองอ่านก่อน — ปอดขวาโปร่ง หลอดเลือดน้อย + ลูกศรชี้อะไร",
           quiz="**คำตอบ:** **Westermark's sign** (อาจารย์วงไว้) · **จุดที่ต้องเห็น:** **ปอดขวาโปร่งทั้งซีก หลอดเลือดน้อย** ✍️ \"Oligemia\" + **right interlobar PA โต** (ลูกศร) จากลิ่มเลือดอัด · **กลไก:** ลิ่มเลือดอุดหลอดเลือดแดงปอด เลือดไปส่วนปลายไม่ถึง · **ความหมาย:** สงสัย **pulmonary embolism** → CTPA (specific แต่ไม่ sensitive)"),
        IM(60, "Cylindrical bronchiectasis — tram tracks", "CXR PA และภาพขยายสองภาพ มีเส้นสีแดงคู่ขนานและลูกศรขาวชี้ผนังหลอดลมที่หนาเป็นเส้นคู่ในปอดส่วนล่าง",
           cap="**Tram tracks** — เส้นขนานคู่ (เส้นแดง/ลูกศร) = **ผนังหลอดลมหนาที่ไม่เรียว** · ✍️ \"Normal จะเรียวเล็กลงที่ periphery\""),
    ))

# ───────────────────────────── 13
sec("chest-img-13", "Mediastinum และ hila — แบ่งช่อง บอกตำแหน่งก้อน",
    "5 โครงสร้างสำคัญ: trachea/carina · aortic arch · main PA · azygos · หัวใจ · Felson: anterior / middle / posterior · ก้อนหน้าทำขอบหัวใจหาย (4T) · ก้อนหลังทำขอบ descending aorta หาย (neurogenic) · BHL", 10,
"""### 5 important mediastinal structures
**Trachea · carina · main bronchi** · **aortic arch** · **main pulmonary artery** · **azygos vein** · **หัวใจและห้องต่าง ๆ** — ขอบของโครงสร้างเหล่านี้คือ "เส้น" ที่เราใช้หาก้อนในช่องอก

[[img:c63]]

### Felson's mediastinal divisions
- **Anterior** — หลัง sternum ถึงเส้นที่ลากตาม **ผนังหน้าของ trachea และขอบหลังของหัวใจ**
- **Posterior** — หลังเส้นที่อยู่ **1 ซม. หลังขอบหน้าของ vertebral body** ไปจนถึงผนังอก
- **Middle** — ระหว่างสองเส้น

[[img:c64]]

| ช่อง | สิ่งที่อยู่ (สไลด์) | ก้อนที่พบบ่อย |
|---|---|---|
| **Anterior** | thymus · thyroid/parathyroid ที่ลงมาใต้ sternum · ต่อมน้ำเหลือง | **4T**: thymoma · teratoma/germ cell · thyroid · lymphoma |
| **Middle** | หัวใจ เยื่อหุ้มหัวใจ · aortic arch และหลอดเลือดใหญ่ · SVC · trachea main bronchi · hila · ต่อมน้ำเหลือง · phrenic/vagus | ต่อมน้ำเหลืองโต (lymphoma, sarcoid, TB, metastasis) · bronchogenic cyst · aneurysm |
| **Posterior** | esophagus · descending aorta · azygos/hemiazygos · thoracic duct · ต่อมน้ำเหลือง · vagus · sympathetic chain | **neurogenic tumour** · ก้อนหลอดอาหาร · hiatal hernia · ฝีข้างกระดูกสันหลัง (TB spine) · extramedullary hematopoiesis (thalassemia) |

### บอกตำแหน่งก้อนด้วย silhouette
[[img:c65]]

[[img:c66]]

สัญญาณเสริม (ตำรา — ไม่อยู่ในสไลด์)
- **Hilum overlay sign** — ก้อนซ้อนบน hilum แต่ **ยังเห็นหลอดเลือด hilum ผ่าน** → ก้อนอยู่หน้า/หลัง ไม่ใช่ hilum โต
- **Cervicothoracic sign** — ก้อนที่ขอบเหนือ clavicle ยังคม = อยู่ **หลัง** (มีปอดล้อม) · ขอบหายเหนือ clavicle = อยู่ **หน้า** (ต่อกับคอ)

### Hila โต
| ลักษณะ | นึกถึง |
|---|---|
| **สองข้างสมมาตร + paratracheal ขวา** | **sarcoidosis** (Löfgren: erythema nodosum + BHL + ข้อเท้าอักเสบ + ไข้) |
| สองข้าง **ไม่สมมาตร** + anterior mediastinum | lymphoma |
| ข้างเดียว | TB (เด็ก) · มะเร็งปอด · metastasis |
| หินปูนเป็นวงรอบ (**eggshell**) | silicosis · sarcoidosis · lymphoma หลังฉายแสง |
| PA โตทั้งสองข้าง (ไม่ใช่ต่อม) | pulmonary hypertension |
""",
    ["Felson: anterior หน้าเส้น trachea–ขอบหลังหัวใจ · posterior หลังเส้น 1 ซม. หลังขอบหน้า vertebra",
     "Anterior mass ทำขอบหัวใจหาย → 4T",
     "Posterior mass: หัวใจยังคม ขอบ descending aorta/paraspinal หาย → neurogenic",
     "Hilum overlay: เห็นหลอดเลือด hilum ผ่านก้อน = ก้อนไม่ได้อยู่ที่ hilum",
     "BHL สมมาตร + erythema nodosum = sarcoidosis (Löfgren)"],
    [mcq(N(25), "A 38-year-old woman has 3 months of drooping eyelids and double vision that worsen towards evening. Chest radiograph shows a smooth lobulated mass projecting to the right of the upper heart that obscures the right heart border; on the lateral view the retrosternal clear space is opacified. What is the most likely mass?",
         ["Thymoma", "Neurofibroma", "Bronchogenic cyst", "Oesophageal leiomyoma", "Descending thoracic aortic aneurysm"], 0,
         "ก้อนที่ **ทำให้ขอบหัวใจหาย** (อยู่ระนาบเดียวกับหัวใจด้านหน้า) + **retrosternal space ทึบ** = **anterior mediastinal mass** ✍️ \"Obscure heart → Ant\"\n\nร่วมกับอาการ **myasthenia gravis** (อ่อนแรงล้าเมื่อใช้งาน หนังตาตก เห็นภาพซ้อนตอนเย็น) → **thymoma** (หนึ่งใน 4T)\n\n- **neurofibroma** อยู่ posterior (ขอบหัวใจยังคม ขอบ aorta/paraspinal หาย)\n- bronchogenic cyst มักอยู่ middle ใต้ carina\n- ก้อนหลอดอาหารและ descending aorta อยู่ posterior",
         "ขอบหัวใจหาย + myasthenia = thymoma", "Mediastinal mass", R("Anterior mediastinal mass"), NLN + ["3.3.20"]),
     mcq(N(26), "A 28-year-old woman has painful red nodules on both shins, ankle swelling and low-grade fever for 2 weeks. Chest radiograph shows symmetrical bilateral hilar lymphadenopathy with right paratracheal widening and clear lung fields. What is the most likely diagnosis?",
         ["Sarcoidosis (Löfgren syndrome)", "Hodgkin lymphoma", "Primary pulmonary tuberculosis", "Metastatic lung cancer", "Silicosis"], 0,
         "**Erythema nodosum + bilateral hilar lymphadenopathy (สมมาตร) + ข้อเท้าอักเสบ + ไข้** = **Löfgren syndrome** ของ **sarcoidosis** · ต่อมน้ำเหลือง hilum สองข้าง + paratracheal ขวา (Garland triad) เป็นรูปแบบคลาสสิก · มักหายเอง ใช้ NSAIDs\n\n- lymphoma: ไม่สมมาตร มักมี anterior mediastinal mass\n- primary TB: ต่อมน้ำเหลืองมักข้างเดียว\n- มะเร็งปอด/metastasis: ข้างเดียว อายุมาก\n- silicosis: ต้องมีประวัติฝุ่น + ปุ่มปอดบน ± eggshell",
         "BHL สมมาตร + erythema nodosum = Löfgren (sarcoid)", "Hilar enlargement", ["ตำราอายุรศาสตร์ — sarcoidosis (ไม่อยู่ในสไลด์)", "สไลด์ อ.พจนี — Mediastinal structure"], NLN),
    ], NLN + ["3.3.20", "B6.1.1(5)"],
    imgs=IMGS(
        IM(63, "Mediastinal structures บน CXR", "CXR PA ส่วนกลางอกมีป้าย azygos arch RUL T car LA RA RV LV Aortic arch PA LAA พร้อมลูกศรชี้แต่ละโครงสร้าง",
           cap="**azygos arch** · RUL bronchus · **T** trachea · **car** carina · **aortic arch** · **PA** · **LAA** (left atrial appendage) · LA · RA · RV · LV — ขอบเหล่านี้คือเส้นที่ใช้หาก้อน"),
        IM(64, "Felson's divisions บน lateral", "ภาพ lateral มีเส้นแบ่งช่องอกเป็น Ant Med ด้านหน้า Mid Med ตรงกลาง และ Post Med ด้านหลัง",
           cap="**Ant Med** (หน้าเส้นตามผนังหน้า trachea–ขอบหลังหัวใจ) · **Mid Med** · **Post Med** (หลังเส้น 1 ซม. หลังขอบหน้า vertebral body) · ✍️ thyroid ที่ลงมาใต้ sternum อยู่ช่องหน้า"),
        IM(65, "Anterior mediastinal mass", "ภาพถ่ายจอแสดง CXR หัวเรื่อง Anterior mediastinal mass มีก้อนใหญ่ซ้อนกึ่งกลางอกด้านบนขยายไปทางขวา ขอบหัวใจขวาส่วนบนมองไม่เห็น",
           cap="(ภาพถ่ายจอในห้อง) ก้อนกลางอกขยายไปขวา **ขอบหัวใจขวาหาย** ✍️ \"**Obscure heart ด้านขวา → Ant**\" · ✍️ \"Post → ดู descending aorta\""),
        IM(66, "ก้อนกลางอกด้านซ้ายล่าง", "ภาพถ่ายจอแสดง CXR มีก้อนทึบขนาดใหญ่ซ้อนเงาหัวใจด้านซ้ายล่าง ขอบหัวใจซ้ายยังเห็นเป็นเส้นคม แต่ขอบ descending aorta ส่วนล่างมองไม่เห็น มีจุดแสงเลเซอร์สีแดงบนภาพ",
           q="ลองอ่านก่อน — ก้อนซ้อนหัวใจ แต่ขอบหัวใจยังอยู่ไหม ขอบไหนหาย",
           quiz="**คำตอบ:** **Posterior mediastinal mass** · **จุดที่ต้องเห็น:** ขอบหัวใจ **ยังคม** แม้ก้อนซ้อนอยู่ = อยู่คนละระนาบ · ขอบ **descending aorta ส่วนล่างหาย** ✍️ \"**silhouette desc. aorta → Post**\" · **DDx:** neurogenic tumour · ก้อนหลอดอาหาร · hiatal hernia · ฝีข้างกระดูกสันหลัง · extramedullary hematopoiesis · **ทำต่อ:** lateral + CT/MRI"),
    ))

# ───────────────────────────── 14
sec("chest-img-14", "Vascular — PE, pulmonary hypertension และ heart failure",
    "PE: CXR มักปกติ · Westermark (oligemia) · Hampton hump (infarct รูปลิ่มฐานที่ pleura) · CTPA filling defect/doughnut · chronic PE mosaic · PHT: main PA > aorta · HF: cephalization → Kerley B → bat-wing + effusion", 11,
"""### Pulmonary embolism บน CXR และ CT
- CXR ในผู้ป่วย PE **ส่วนใหญ่ปกติหรือไม่จำเพาะ** — ใช้ตัดโรคอื่น (pneumothorax, pneumonia) มากกว่ายืนยัน PE
- **Westermark sign** — oligemia หลังจุดอุด (หัวข้อปอดดำเกิน)
- **Hampton's hump** ✍️ "Hampton" — **ทึบรูปลิ่ม ฐานติด pleura ยอดชี้ไปทาง hilum** ที่ปอดล่าง = **pulmonary infarction**
- **CTPA** — **intraluminal filling defect** · ตัดขวางเห็นลิ่มเลือดกลางหลอดเลือดล้อมด้วยสี = **doughnut (polo mint) sign** · ตามยาวเป็นแถบ (railway track)
- **Chronic PE** — ลิ่มเลือดแนบผนัง (eccentric, mural) · หลอดเลือดเล็กลง · **mosaic attenuation** (บริเวณเลือดน้อยดำกว่า เลือดถูกเบนไปปอดปกติ)

[[img:c67]]

[[img:c68]]

### Pulmonary hypertension
- CT: **main PA กว้างกว่า ascending aorta** (PA:Ao > 1) หรือ main PA ≥ 29 มม.
- CXR: hilum สองข้างโต PA ส่วนกลางโป่ง แต่ **หลอดเลือดส่วนปลายเล็กลงทันที (pruning)**

[[img:c69]]

### Heart failure บน CXR (ไม่อยู่ในสไลด์)
สไลด์มีเฉพาะ CTR แต่ภาพนี้พบบ่อยที่สุดในวอร์ด จึงเพิ่มจากตำรารังสีวิทยาทรวงอก
| ระยะ (PCWP โดยประมาณ) | สิ่งที่เห็น | กลไก |
|---|---|---|
| **ปกติ < 12 mmHg** | หลอดเลือดกลีบล่าง > กลีบบน (ท่ายืน) | แรงโน้มถ่วง |
| **13–18** | **Cephalization** — หลอดเลือดกลีบบนเท่า/ใหญ่กว่ากลีบล่าง | ฐานปอดบวมใน interstitium หลอดเลือดถูกกด เลือดเบนขึ้นบน |
| **18–25** | **Interstitial edema** — **Kerley B lines** · peribronchial cuffing · hilum พร่า · fissure หนา | น้ำซึมเข้า interlobular septa (มี vein + lymphatic) |
| **> 25** | **Alveolar edema** — ทึบรอบขั้วปอด **bat-wing** + air bronchogram · **pleural effusion** | น้ำล้นเข้าถุงลม · pleura ระบายไม่ทัน |
| ร่วมด้วย | **cardiomegaly** (CTR > 0.5 บน PA) · vascular pedicle กว้าง | ภาวะน้ำเกิน |

- **Kerley B** = เส้นสั้นแนวนอน **1–2 ซม.** ที่ขอบปอดล่าง ตั้งฉากกับ pleura · **Kerley A** = เส้นยาวเฉียงชี้ไป hilum ในปอดบน
- ภาพอาจช้ากว่าความดันหลายชั่วโมง (radiological lag) และหายช้ากว่าอาการ

#### ทำไมถึงเห็นแบบนี้
| สิ่งที่เห็น | กลไก | บอกอะไร |
|---|---|---|
| **Hampton's hump รูปลิ่มที่ขอบปอด** | ปอดมีเลือดสองระบบ (pulmonary + bronchial) · infarct เกิดเมื่อ bronchial collateral ไม่พอ ซึ่งมักเป็นส่วนปลายใต้ pleura | PE ที่มี infarction (เจ็บอกแบบ pleuritic ไอเป็นเลือด) |
| **Doughnut sign** | ลิ่มเลือด (ไม่ติดสี) อยู่กลางหลอดเลือดที่สีล้อมรอบ | acute PE (ลิ่มลอยกลาง) · chronic = แนบผนัง |
| **Mosaic attenuation** | เลือดไหลไม่เท่ากันเป็นหย่อม — บริเวณหลอดเลือดอุดดำ บริเวณได้เลือดเกินขาว | chronic thromboembolic disease (แยกจาก air trapping ด้วยฟิล์มหายใจออก) |
| **Main PA โต ส่วนปลายเล็ก** | ความดันสูงทำให้ PA ส่วนต้นขยาย · หลอดเลือดเล็กหดตัว/ถูกทำลาย | pulmonary hypertension |
| **Bat-wing** | น้ำสะสมรอบขั้วปอดก่อน ส่วนปลายใต้ pleura มีน้ำเหลืองระบายดีกว่า | alveolar edema (cardiogenic) |
""",
    ["CXR ใน PE มักปกติ · Westermark = oligemia · Hampton hump = infarct รูปลิ่มฐานที่ pleura",
     "CTPA: filling defect · doughnut sign · chronic: ลิ่มแนบผนัง + mosaic",
     "PHT: main PA > ascending aorta บน CT",
     "HF: cephalization (13–18) → Kerley B (18–25) → bat-wing + effusion (> 25)",
     "Kerley B = interlobular septa บวม · เส้นสั้นแนวนอนที่ขอบปอดล่าง"],
    [mcq(N(27), "Five days after hip surgery, a 70-year-old woman develops pleuritic chest pain and blood-streaked sputum. Chest radiograph shows a peripheral wedge-shaped opacity in the right lower zone whose base abuts the pleura and whose rounded apex points toward the hilum. What does this opacity most likely represent?",
         ["Pulmonary infarction from pulmonary embolism", "Lobar pneumonia of the right lower lobe", "Round atelectasis from asbestos exposure", "Septic emboli with cavitation", "Loculated pleural effusion"], 0,
         "ทึบ **รูปลิ่ม ฐานติด pleura ยอดมนชี้ไปทาง hilum** = **Hampton's hump** ✍️ \"Hampton\" = **pulmonary infarction** — หลังผ่าตัดสะโพก (เสี่ยง VTE) + เจ็บอกแบบ pleuritic + ไอเป็นเลือด เข้ากับ PE\n\nกลไก: ปอดมีเลือดสองระบบ infarct จึงเกิดเฉพาะเมื่อ bronchial collateral ไม่พอ ซึ่งมักเป็น **ส่วนปลายใต้ pleura** → เลือดออกและเนื้อตายเป็นรูปลิ่มตามการแตกแขนงของหลอดเลือด\n\n**ทำต่อ:** CTPA (Wells/YEARS) · ฟิล์มปกติไม่ได้ตัด PE ออก\n\n- lobar pneumonia ทึบตามกลีบมี air bronchogram · rounded atelectasis ต้องมี pleura หนา + comet tail · septic emboli เป็นปุ่มหลายอันมีโพรง",
         "ลิ่มฐานที่ pleura ยอดชี้ hilum = Hampton hump (infarct)", "Pulmonary embolism", R("Pulmonary infarction"), NLN + ["2.2.12", "B6.2.6(2)"]),
     mcq(N(28), "In a patient with decompensated left heart failure, short horizontal lines 1–2 cm long are seen at the lateral lung bases, perpendicular to the pleura. What do these lines represent?",
         ["Thickened interlobular septa from interstitial oedema", "Dilated upper lobe pulmonary veins", "Fluid within the minor fissure", "Plate-like atelectasis", "Thickened bronchial walls seen end-on"], 0,
         "**Kerley B lines** = **interlobular septa หนา** — septa เป็นที่วิ่งของ **pulmonary vein และท่อน้ำเหลือง** · เมื่อ PCWP ~18–25 mmHg น้ำซึมเข้า interstitium → septa บวม เห็นเป็นเส้นสั้นแนวนอนที่ขอบปอดล่างตั้งฉากกับ pleura (ดูภาพ secondary pulmonary lobule)\n\n- หลอดเลือดกลีบบนโต = **cephalization** (ระยะก่อนหน้า)\n- fissure หนามีน้ำได้ แต่เป็นเส้นยาวตามตำแหน่ง fissure\n- platelike atelectasis เป็นแถบหนากว่า ยาวหลายเซนติเมตร ไม่ถึงขอบ pleura เสมอไป\n- bronchial wall ตัดขวางเป็นวงแหวน (peribronchial cuffing)",
         "Kerley B = interlobular septa บวม (interstitial edema)", "Heart failure", ["ตำรารังสีวิทยาทรวงอก — pulmonary venous hypertension (ไม่อยู่ในสไลด์)"], NLN + ["2.3.9(5)", "2.2.5", "B6.2.6(1)"]),
    ], NLN + ["2.2.12", "B6.2.6(2)", "2.3.9(5)", "2.2.5", "3.3.20"],
    imgs=IMGS(
        IM(67, "ทึบรูปลิ่มที่ฐานปอดขวา", "ภาพขยายฐานปอดขวามีเงาทึบรูปลิ่มฐานติดเยื่อหุ้มปอด ลูกศรขาวชี้ เส้นสีน้ำเงินลากขอบปอด เส้นสีแดงลากขอบบนที่โค้งนูนของเงาทึบ และลายมือวงคำว่า Hampton คู่กับ CXR PA ที่มีเงาทึบลักษณะเดียวกันที่ฐานปอดขวา",
           q="ผู้ป่วยหลังผ่าตัด เจ็บอกเวลาหายใจ — ลองอ่านก่อน",
           quiz="**คำตอบ:** **Pulmonary infarction — Hampton's hump** ✍️ \"Hampton\" · **จุดที่ต้องเห็น:** ทึบ **รูปลิ่ม ฐานติด pleura** ยอดมนชี้ไปทาง hilum (เส้นแดง) ที่ปอดล่างสองข้าง · **กลไก:** PE อุดหลอดเลือดส่วนปลาย bronchial collateral ไม่พอ → เลือดออก/เนื้อตายใต้ pleura · **ทำต่อ:** CTPA · หายช้าแบบ \"melting ice cube\" (หดจากขอบเข้าใน)"),
        IM(68, "Acute PE บน CTPA", "ภาพ CT ฉีดสีสองภาพ ภาพแรกเห็นลิ่มเลือดเกือบอุดตันใน pulmonary artery กลีบล่างทั้งสองข้าง ลูกศรขาวชี้ ภาพที่สองเห็นลิ่มกลมอยู่กลางหลอดเลือดกลีบล่างซ้ายล้อมด้วยสี",
           cap="**Nearly occlusive thrombus in both lower lobe PA** · **round intraluminal filling defect within Lt lower lobe PA = doughnut sign** (ลิ่มไม่ติดสีอยู่กลางวงสี)"),
        IM(69, "CT ระดับ main PA", "ภาพ CT ฉีดสีระดับ main pulmonary artery มีลูกศรสีแดงวัด ascending aorta และลูกศรสีน้ำเงินวัด main pulmonary artery ซึ่งกว้างกว่า มีป้าย SVC",
           q="ลองเทียบเส้นแดงกับเส้นน้ำเงิน — บอกภาวะอะไร",
           quiz="**คำตอบ:** **Pulmonary hypertension (PHT)** · **จุดที่ต้องเห็น:** **main PA (น้ำเงิน) กว้างกว่า ascending aorta (แดง)** — PA:Ao > 1 · **กลไก:** ความดันใน PA สูงเรื้อรังทำให้ผนังส่วนต้นขยาย · **ทำต่อ:** echocardiography (TR velocity) → หาสาเหตุ: โรคหัวใจซ้าย · โรคปอด/hypoxia (COPD ILD) · **CTEPH** · PAH · ยืนยันด้วย right heart catheterization"),
    ))

# ───────────────────────────── 15
sec("chest-img-15", "Pleural effusion — meniscus, subpulmonic, loculated",
    "Lateral ทื่อ > 50 มล. · PA meniscus > 200 มล. · subpulmonic: ยอดโดมปลอมเลื่อนออกด้านข้าง · decubitus: free ไหล · loculated มี septa → parapneumonic/empyema · massive ดัน mediastinum · CT 0–20 HU", 10,
"""### ปริมาณน้ำที่เริ่มเห็น
| ฟิล์ม | สิ่งที่เห็น | ปริมาณโดยประมาณ |
|---|---|---|
| **Lateral (ยืน)** | **มุม costophrenic ด้านหลังทื่อ** (posterior sulcus ต่ำสุด) | **> 50 มล.** |
| **PA (ยืน)** | **meniscus sign** มุมด้านข้างทื่อ | **> 200 มล.** |
| PA | โดมหายทั้งหมด | ~500 มล. (ตำรา) |
| Supine AP | ซีกขาวจางแบบม่าน ไม่มี meniscus | ต้องปริมาณมาก |
| Lateral decubitus / ultrasound | ชั้นน้ำบาง ๆ | ไม่กี่สิบมิลลิลิตร |

### Meniscus และ subpulmonic — ทำไมเป็นรูปนี้
[[img:c70]]

[[img:c73]]

### Decubitus — free หรือ loculated
- สไลด์: "**Fluid will move to dependent part** and sharp edge between lung and fluid would become obvious"

[[img:c71]]

[[img:c74]]

### CT findings (สไลด์)
- **ทึบรูปเคียว (sickle-shaped) ในส่วนที่ต่ำ** · **density ของน้ำ 0–20 HU**
- 4 เกณฑ์แยกน้ำในช่องเยื่อหุ้มปอดจาก ascites: **diaphragm sign · displaced crus sign · interface sign · bare area sign** (ชื่อเกณฑ์อิงตำรา)
- ต่อไปที่ **คาบ Thoracentesis** — เจาะ แปลผล Light's criteria

#### ทำไมถึงเห็นแบบนี้
| สิ่งที่เห็น | กลไก | ใช้ทำอะไร |
|---|---|---|
| **มุมหลังทื่อก่อนมุมข้าง** | posterior costophrenic sulcus ลึกและต่ำที่สุดเมื่อยืน น้ำไปรวมก่อน | lateral ไวกว่า PA |
| **Meniscus สูงด้านข้าง** | ปอดมี elastic recoil ดึงเข้า hilum · น้ำเป็นชั้นรอบปอด ภาพหน้าตรงผ่านชั้นน้ำหนาที่สุดด้านข้าง | ยืนยันว่าเป็นน้ำอิสระ |
| **ยอดโดมปลอมเลื่อนออกด้านข้าง** | น้ำขังใต้ฐานปอดโดยปอดไม่ยกตัว ขอบบนของน้ำขนานกับโดมจริงแต่ยอดอยู่นอก | subpulmonic effusion · ซ้าย: gastric bubble ห่างโดม > 2 ซม. |
| **น้ำไม่ไหลเมื่อตะแคง / รูปเลนส์ติดผนัง** | fibrin สร้าง septa กั้นเป็นช่อง | loculated → parapneumonic/empyema/TB → ต้องระบาย |
| **Massive: mediastinum ถูกดัน** | ปริมาตรซีกนั้นเพิ่ม | ถ้า mediastinum ไม่ถูกดันทั้งที่ขาวทั้งซีก → มี collapse ซ่อน (มะเร็งอุดหลอดลม) |
""",
    ["Lateral มุมหลังทื่อ > 50 มล. · PA meniscus > 200 มล.",
     "Meniscus สูงด้านข้าง = น้ำอิสระรอบปอดที่มี recoil",
     "Subpulmonic: ยอดโดมปลอมเลื่อนออกด้านข้าง ✍️ ★",
     "Decubitus: free ไหลเป็นชั้น · loculated ไม่ไหล มี septa → parapneumonic/empyema",
     "ขาวทั้งซีกแต่ mediastinum ไม่ถูกดัน → มี collapse ซ่อนอยู่"],
    [mcq(N(29), "A 50-year-old man's erect PA radiograph shows an apparently elevated right hemidiaphragm whose highest point lies far lateral to its normal position near the midclavicular line, with a sharp but shallow costophrenic angle. The lateral view shows blunting of the posterior costophrenic sulcus. What is the most likely finding?",
         ["Subpulmonic pleural effusion", "Right phrenic nerve palsy", "Right lower lobe collapse", "Eventration of the right hemidiaphragm", "Subphrenic abscess with gas"], 0,
         "**Subpulmonic effusion** ✍️ ★ อาจารย์วงไว้ — น้ำขังใต้ฐานปอด ทำให้เห็น **โดมปลอม (pseudodiaphragm)** ที่ดูยกสูง แต่ **ยอดเลื่อนไปด้านข้าง** ✍️ \"(ยอด) จะเปิดไปทาง lateral\" (โดมจริงยอดอยู่ค่อนกลาง) · lateral มุมหลังทื่อยืนยันว่ามีน้ำ\n\n**ทำต่อ:** lateral decubitus หรือ ultrasound\n\n- phrenic palsy/eventration: โดมสูงแต่รูปร่างโค้งปกติ ยอดไม่เลื่อนออก ไม่มีมุมหลังทื่อ\n- RLL collapse ต้องมีทึบสามเหลี่ยมและ volume loss\n- subphrenic abscess มีลม/ระดับน้ำใต้โดม",
         "โดมสูง + ยอดเลื่อนออกด้านข้าง = subpulmonic effusion", "Pleural effusion", R("Subpulmonic effusion"), NLN + ["2.3.10(7)"]),
     mcq(N(30), "On an erect PA chest radiograph, approximately what minimum volume of pleural fluid is usually needed before the lateral costophrenic angle becomes blunted with a meniscus?",
         ["About 10 mL", "About 50 mL", "About 200 mL", "About 1000 mL", "About 2000 mL"], 2,
         "สไลด์: **meniscus sign บนภาพหน้าตรง > 200 มล.** · **lateral film มุมหลังทื่อ > 50 มล.** (posterior sulcus ต่ำสุด น้ำไปรวมก่อน)\n\nจึงใช้ **lateral** หรือ **ultrasound** ถ้าสงสัยน้ำน้อย · ~10 มล. คือปริมาณน้ำปกติในช่องเยื่อหุ้มปอด · 1–2 ลิตรทำให้ขาวครึ่งซีกขึ้นไป",
         "PA meniscus > 200 มล. · lateral > 50 มล.", "Pleural effusion", R("Pleural effusion: radiographic sign"), NLN + ["2.3.10(7)"], keep=True),
    ], NLN + ["2.3.10(7)", "B6.2.2(10)", "2.3.10-3(2)"],
    imgs=IMGS(
        IM(70, "ปอดซ้ายล่าง", "CXR PA ปอดซ้ายส่วนล่างขาวสม่ำเสมอ ขอบบนเว้าสูงด้านข้าง ขอบหัวใจซ้าย มุม costophrenic และโดมซ้ายมองไม่เห็น มีกล่องข้อความ Meniscus sign",
           cap="**Meniscus sign** ✍️ \"moderate amount of PE\" — left lower zone ขาวสม่ำเสมอ · **ขอบบนเว้า สูงด้านข้าง** · ขอบหัวใจซ้าย มุม costophrenic และโดมซ้ายหาย (silhouette กับน้ำ)"),
        IM(73, "โดมขวาสูง — ดูตำแหน่งยอด", "CXR PA เส้นแนวตั้งสีแดงลากผ่านกลางปอดขวา ลูกศรแดงชี้ยอดโดมขวาซึ่งอยู่ด้านนอกมาก โดมขวาดูยกสูง",
           q="ลองอ่านก่อน — โดมขวาดูสูง แต่ยอดโดมอยู่ตรงไหนเมื่อเทียบเส้นแดง",
           quiz="**คำตอบ:** **Subpulmonic effusion** ✍️ ★ · **จุดที่ต้องเห็น:** \"โดม\" ขวาดูสูง แต่ **ยอดเลื่อนไปด้านข้าง (lateral displacement of apex)** เลยเส้นกึ่งกลาง (ลูกศรแดง) — โดมจริงยอดอยู่ค่อนกลาง ✍️ \"มีน้ำขังอยู่ → (ยอด) จะเปิดไปทาง lateral\" · **กลไก:** น้ำขังใต้ฐานปอดโดยปอดไม่ยกตัว · **ทำต่อ:** lateral decubitus/ultrasound"),
        IM(71, "Decubitus — น้ำไหลลงด้านล่าง", "ภาพขยายท่าตะแคงมีลูกศรสีน้ำเงินสองอันชี้ขอบระหว่างปอดกับชั้นน้ำที่อยู่ด้านล่างตามผนังทรวงอก",
           cap="ท่าตะแคง **น้ำไหลไปส่วนต่ำ** ขอบปอด–น้ำคมชัด (ลูกศร) = **free-flowing** · ความหนาของชั้นน้ำช่วยประเมินว่าเจาะได้ปลอดภัยไหม (ตำรา: > 1 ซม.)"),
        IM(74, "Effusion ที่ไม่ได้อยู่ตำแหน่งต่ำ", "CXR ผู้ป่วยมีท่อ tracheostomy ซีกขวาทึบเกือบทั้งหมด เหลือเนื้อปอดที่มีลมเป็นหย่อมดำไม่สม่ำเสมอตรงกลางส่วนบน ล้อมด้วยความทึบรวมถึงที่ยอดปอดและผนังด้านข้าง ปอดซ้ายปกติ",
           q="ลองอ่านก่อน — ความทึบซีกขวาเป็นน้ำแบบไหน",
           quiz="**คำตอบ:** **Loculated pleural effusion** · **จุดที่ต้องเห็น:** ความทึบ **ล้อมปอดรวมถึงยอดปอดและผนังด้านข้าง** ไม่ได้ลงไปอยู่ส่วนที่ต่ำตามแรงโน้มถ่วง เหลือปอดที่มีลมเป็นหย่อมตรงกลาง ✍️ \"น้ำขังอยู่ ไม่ free fluid\" · **กลไก:** fibrin และ septa กั้นช่องเยื่อหุ้มปอด ✍️ \"**มี septate → สงสัย parapneumonic → empyema**\" · **ทำต่อ:** ultrasound/CT · เจาะดู pH glucose LDH · ระบาย (ICD ± fibrinolytic) หรือผ่าตัด"),
    ))

# ───────────────────────────── 16
sec("chest-img-16", "Pneumothorax — visceral pleural line, tension และขนาด",
    "White pleural line + ไม่มีลายปอดนอกเส้น · deep sulcus (ท่านอน) · ระวัง skin fold และ bulla · tension: mediastinum ถูกดัน โดมกด = วินิจฉัยทางคลินิก · Large > 2 ซม. ที่ระดับ hilum (BTS) · BTS 2023 ดูอาการเป็นหลัก", 10,
"""### Classic signs (สไลด์)
- **White pleural line** — visceral pleura เป็นเส้นขาวบาง
- **Absence of lung markings beyond the white line**
- **Deep sulcus sign** — ท่านอนหงาย ลมลอยไปด้านหน้า-ล่าง มุม costophrenic ลึกและดำผิดปกติ
- **Prominent pericardial fat tags** — ลมล้อมไขมันข้างหัวใจจนเห็นชัด

[[img:c22]]

[[img:c75]]

| สิ่งที่เลียนแบบ | แยกอย่างไร |
|---|---|
| **Skin fold** | เส้นเลยออกนอกทรวงอก · เป็นขอบเทา–ดำ ไม่ใช่เส้นขาวบาง · ยังเห็นลายปอดนอกเส้น |
| **Bulla ใหญ่** | ผนังโค้ง **เว้าเข้าหาผนังอก** (ไม่ขนานผนัง) · มีลายปอดรอบ ๆ · CT ถ้าไม่แน่ใจ — ห้ามใส่สายผิด |
| **ขอบ scapula** | ต่อเนื่องออกนอกทรวงอก |

### กลไก — visceral pleural line และ tension
[[img:c76]]

[[img:c77]]

[[img:c78]]

### ขนาด
[[img:c79]]

- สไลด์: **Large > 2 ซม. ≈ 50% ของปริมาตร** ✍️ "ดู size ตรงนี้" (ชี้ระยะ b)
- **British (BTS):** วัด **ระยะระหว่าง pleura ที่ระดับ hilum** (b) — ≥ 2 ซม. = large
- **American (ACCP):** วัด **ระยะยอดปอดถึงโดมเยื่อหุ้ม (apex–cupola, a)** — ≥ 3 ซม. = large

### การดูแลตาม BTS 2023 (ไม่อยู่ในสไลด์)
- **Tension pneumothorax = วินิจฉัยทางคลินิก** (หอบมาก ความดันต่ำ หลอดเลือดดำคอโป่ง trachea เบี้ยว เสียงหายใจหาย) → **needle decompression ทันที ไม่รอฟิล์ม** แล้วใส่สาย
- Secondary pneumothorax (มีโรคปอดเดิม เช่น COPD) → ส่วนใหญ่ต้องระบาย
- **Primary spontaneous** ที่ไม่มี high-risk features → เลือกตามอาการและความต้องการผู้ป่วย: **conservative** (แม้ขนาดใหญ่) · needle aspiration · ambulatory device
""",
    ["Pneumothorax: เส้นขาวบาง + ไม่มีลายปอดนอกเส้น",
     "ท่านอน: ลมขึ้นหน้า-ล่าง → deep sulcus sign",
     "Tension: mediastinum/trachea ถูกดัน โดมกด — วินิจฉัยทางคลินิก ไม่รอฟิล์ม",
     "Large > 2 ซม. ที่ระดับ hilum (BTS) ≈ 50%",
     "BTS 2023: PSP ไม่มี high-risk → ตัดสินตามอาการ ไม่ใช่ขนาด"],
    [mcq(N(31), "A 24-year-old man is stabbed in the left chest. He is agitated, RR 36/min, BP 78/50 mmHg, HR 140/min, with distended neck veins, tracheal deviation to the right and absent breath sounds on the left. What is the most appropriate immediate action?",
         ["Immediate needle decompression of the left chest, followed by chest drain insertion", "Urgent portable chest radiograph to confirm the diagnosis", "CT chest to look for associated injuries", "Bedside echocardiography to exclude cardiac tamponade before any intervention", "Intubation and positive-pressure ventilation before decompression"], 0,
         "**Tension pneumothorax** — trachea ถูกดันไปขวา เสียงหายใจซ้ายหาย หลอดเลือดดำคอโป่ง ช็อก = **วินิจฉัยทางคลินิก** → **needle decompression ทันที** (ผู้ใหญ่ ATLS 10th: ช่องซี่โครง 4–5 หน้าต่อ midaxillary line · หรือ 2nd ICS midclavicular line) แล้วใส่ **chest drain**\n\nกลไก: ลิ้นทางเดียว ลมเข้าได้ออกไม่ได้ → ความดันบวกดัน mediastinum กด vena cava → venous return ลด → ช็อก\n\n- **รอฟิล์ม/CT = เสียเวลาจนหัวใจหยุดเต้น** (ภาพในสไลด์ \"early tension\" ใช้เรียนรู้ แต่ในชีวิตจริงไม่ควรได้เห็นบ่อย)\n- ใส่ท่อช่วยหายใจ + positive pressure ก่อนระบาย ทำให้ tension แย่ลงทันที",
         "Tension = clinical → needle decompression ก่อนฟิล์ม", "Tension pneumothorax", R("Large pneumothorax: early tension") + ["ATLS 10th edition", "BTS Guideline for pleural disease 2023"], NLN + ["2.2.14", "2.3.10(6)"]),
     mcq(N(32), "A ventilated ICU patient lying supine has a portable AP radiograph showing an unusually deep and lucent left costophrenic angle extending down the flank, a sharply outlined left hemidiaphragm and heart border, but no visible apical pleural line. What is the most likely diagnosis?",
         ["Anterior pneumothorax shown by the deep sulcus sign", "Left lower lobe collapse", "Subpulmonic pleural effusion", "Normal appearance in a supine patient", "Pneumoperitoneum"], 0,
         "ท่า **นอนหงาย** ลมใน pleura ไม่ขึ้นไปที่ apex แต่ **ลอยไปด้านหน้า-ล่าง** (ส่วนที่สูงที่สุดเมื่อนอน) → มุม costophrenic **ลึกและดำผิดปกติ** = **deep sulcus sign** · ขอบโดมและหัวใจคมขึ้นเพราะมีลมล้อม · จึงไม่เห็นเส้น pleura ที่ apex\n\nผู้ป่วยใส่เครื่องช่วยหายใจเสี่ยง barotrauma → อาจกลายเป็น tension ได้เร็ว · ยืนยันด้วย ultrasound (lung sliding หาย) หรือ CT\n\n- LLL collapse ทำให้ทึบ · subpulmonic effusion ทึบ · pneumoperitoneum เป็นลมใต้โดม",
         "Supine: ลมไปหน้า-ล่าง → deep sulcus sign", "Pneumothorax", R("Pneumothorax — classic signs"), NLN + ["2.3.10(6)", "B6.2.3(4)"]),
    ], NLN + ["2.3.10(6)", "2.2.14", "B6.2.3(4)"],
    imgs=IMGS(
        IM(22, "Visible visceral pleural line", "CXR AP portable ผู้ป่วยใน ICU มีป้าย Visible visceral pleural line และ Pneumothorax Rt lung ลูกศรเหลืองชี้เส้น visceral pleura ที่ปอดขวาด้านบน",
           cap="**Visible visceral pleural line** (ลูกศรเหลือง) — **Pneumothorax Rt lung** ในผู้ป่วย ICU · นอกเส้นไม่มีลายปอด · pleura เห็นได้เพราะมีลมล้อมทั้งสองด้าน (ลมในปอดกับลมในช่องเยื่อหุ้ม)"),
        IM(75, "Pneumothorax ที่ยอดปอดซ้าย", "CXR PA มีเส้นสีน้ำเงินลากตามขอบปอดซ้ายส่วนบนที่หดลงจากผนังทรวงอก นอกเส้นไม่มีลายปอด",
           cap="**Visible pleural edge** (เส้นน้ำเงิน) · **lung markings not visible beyond this edge** · ยอดปอดซ้ายหดลงจากผนัง"),
        IM(76, "หอบ ความดันเริ่มลด", "CXR PA ซีกขวาดำไม่มีลายปอด ขอบปอดขวาหดเข้าหา hilum mediastinum และ trachea เลื่อนไปทางซ้าย โดมขวากดต่ำลงเล็กน้อย",
           q="ลองอ่านก่อน — ดู trachea, mediastinum และโดมขวา แล้วบอกความรุนแรง",
           quiz="**คำตอบ:** **Large pneumothorax: early tension** ✍️ \"tension pneumothorax\" · **จุดที่ต้องเห็น:** ปอดขวาหดเข้าหา hilum ไม่มีลายปอดรอบนอก · **mediastinum เลื่อนไปซ้าย** · **trachea เบี้ยวไปซ้ายเล็กน้อย** · **โดมขวากดต่ำ** · **กลไก:** ความดันบวกในช่องเยื่อหุ้มดันโครงสร้างข้างเคียง · **ทำต่อ:** ถ้ามีอาการ tension ทางคลินิก → needle decompression ทันที"),
        IM(77, "Portable — ซีกซ้าย", "CXR AP portable ซีกซ้ายด้านนอกดำไม่มีลายปอด ลูกศรเหลืองชี้ขอบปอดซ้ายด้านข้าง ด้านในข้างหัวใจ และที่ฐานปอดเหนือโดมซ้าย",
           q="ลองอ่านก่อน — ลูกศรเหลืองชี้อะไร ทำไมมีทั้งด้านข้าง ด้านใน และที่ฐาน",
           quiz="**คำตอบ:** **Large left pneumothorax** · **จุดที่ต้องเห็น:** ลูกศรชี้ **visceral pleural line รอบปอดซ้าย** — ด้านข้าง (ชี้ซ้าย) · ด้านในข้างขอบหัวใจ (ชี้ขวา) · ที่ฐานเหนือโดม (ชี้ขึ้น) · นอกเส้นดำไม่มีลายปอด · **กลไก:** ฟิล์ม portable ผู้ป่วยกึ่งนอน ลมกระจายไปส่วนที่สูงซึ่งรวมถึงด้านหน้า-ใน และด้านล่าง (anteromedial/subpulmonic) ไม่ใช่แค่ยอดปอด · **ทำต่อ:** ประเมินอาการ tension · ใส่สายระบาย"),
        IM(78, "Upright — ซีกขวา", "CXR PA ท่ายืน ลูกศรเหลืองสี่อันชี้ขอบปอดขวาที่หดเข้า ปอดซ้ายมีจุดทึบเล็กกระจาย",
           cap="**Right pneumothorax** (ลูกศรเหลือง = visceral pleural line) · ปอดซ้ายมีปุ่มกระจาย → ถ้ามีโรคปอดเดิม = **secondary pneumothorax** ซึ่งมักต้องระบาย"),
        IM(79, "Pneumothorax size", "แผนภาพปอดสองข้างแสดงระยะ a จากยอดปอดถึงยอดเยื่อหุ้มปอดตามแนวทางอเมริกัน และระยะ b ระหว่างเยื่อหุ้มที่ระดับ hilum ตามแนวทางอังกฤษ มีกล่องข้อความ Large มากกว่า 2 cm 50% by volume",
           cap="**Large > 2 ซม. ≈ 50% by volume** · **a** = apex–cupola (American) · **b** = interpleural distance ที่ระดับ hilum (British) ✍️ \"ดู size ตรงนี้\""),
    ))

# ───────────────────────────── 17
sec("chest-img-17", "Pneumoconiosis — silica, ถ่านหิน และใยหิน (ไม่อยู่ในสไลด์)",
    "Silicosis: ปุ่มปอดบน + eggshell + PMF + เสี่ยง TB · CWP: ปุ่มปอดบน ไม่มี eggshell · Caplan · asbestos: pleural plaque · asbestosis ปอดล่าง · mesothelioma · บุหรี่ × ใยหิน · ILO 2022", 13,
"""ส่วน **occupational lung disease** ของคาบ 21 **ไม่มีในไฟล์สไลด์** ที่ได้รับ — เนื้อหาหัวข้อนี้และหัวข้อถัดไปอิงตำราอายุรศาสตร์และแนวทาง (ILO 2022) เพื่อให้ครอบคลุมข้อสอบในคลังของคาบนี้

### หลักคิดโรคปอดจากการทำงาน
- **ประวัติอาชีพละเอียด**: งานทุกงานตั้งแต่เริ่มทำงาน ทำอะไร สัมผัสอะไร นานเท่าไร ป้องกันอย่างไร เพื่อนร่วมงานป่วยไหม · อาการสัมพันธ์กับวันทำงานไหม
- **ระยะแฝง (latency)** ยาวหลายปีถึงหลายสิบปี — ผู้ป่วยอาจเลิกงานนั้นไปนานแล้ว
- ภาพรังสีอ่านและบันทึกตาม **ILO classification**
- **โรคจากการทำงานป้องกันได้** — แจ้ง/รายงาน ใช้สิทธิกองทุนเงินทดแทน และคัดกรองเพื่อนร่วมงาน

### Silicosis
- ฝุ่น **crystalline silica** — ตัด ขัด เจียหิน **หินสังเคราะห์ (engineered stone)** · **พ่นทราย (sandblasting)** · เหมือง โรงโม่หิน เซรามิก
- รูปแบบ: **chronic** (> 10 ปี) · **accelerated** (5–10 ปี) · **acute silicoproteinosis** (สัมผัสสูงมาก ไม่กี่เดือน–ปี คล้าย PAP)
- ภาพ: **small rounded opacities ปอดบนและหลัง** · ต่อมน้ำเหลือง hilum โต **eggshell calcification** · ปุ่มรวมกัน > 1 ซม. = **progressive massive fibrosis (PMF)** มักปอดบนสองข้าง เคลื่อนเข้าหา hilum
- **เสี่ยง TB สูงหลายเท่า** (macrophage ทำงานเสีย) → **คัดกรอง TB และ latent TB เป็นระยะ** · ระวังโพรงใน PMF = TB จนกว่าจะพิสูจน์ได้
- เพิ่มความเสี่ยง **มะเร็งปอด** (silica = IARC group 1) · โรค autoimmune (scleroderma, RA) · CKD
- **ไม่มียารักษาให้หาย** — steroid, chelation ไม่ช่วย · whole-lung lavage ใช้เฉพาะ acute silicoproteinosis · หลักคือ **หยุดสัมผัส** เลิกบุหรี่ วัคซีน ปลูกถ่ายปอดในรายรุนแรง

### Coal worker's pneumoconiosis (CWP)
- ฝุ่นถ่านหิน (มี silica ปนน้อยกว่า) · **simple CWP**: ปุ่มเล็ก **ปอดบน** · **complicated** = PMF
- ต่างจาก silicosis: **ไม่มี eggshell** เป็นลักษณะเด่น · ความเสี่ยง TB เพิ่มน้อยกว่ามาก · simple CWP สมรรถภาพปอดมักใกล้ปกติ
- **Caplan syndrome** — **rheumatoid arthritis + rheumatoid nodules 0.5–5 ซม. ในปอด** ของคนงานเหมืองถ่านหิน (พบได้ใน silica/asbestos)

### โรคจากใยหิน (asbestos)
แหล่งในไทย: **กระเบื้องลอน/แผ่นหลังคาซีเมนต์ใยหิน** ท่อซีเมนต์ ผ้าเบรก ฉนวน อู่ต่อเรือ งานรื้อถอนอาคาร
| โรค | ระยะแฝง | ภาพ/ลักษณะ |
|---|---|---|
| **Pleural plaque** (พบบ่อยสุด) | 20–30 ปี | หนาตัวของ **parietal pleura** เป็นแผ่น มัก **calcify** ที่ **โดมกะบังลม** และผนังข้าง-หลัง · ไม่มีอาการ · **บอกว่าเคยสัมผัส** ไม่กลายเป็นมะเร็ง |
| **Benign asbestos pleural effusion** | < 20 ปี (อาการแรกสุด) | exudate มักมีเลือด/eosinophil · ต้องตัดมะเร็ง/TB |
| **Diffuse pleural thickening** | | ลามถึงมุม costophrenic · restrictive |
| **Rounded atelectasis** | | ก้อนใต้ pleura + comet tail (หัวข้อ atelectasis) |
| **Asbestosis** | > 15–20 ปี | **fibrosis ปอดล่าง subpleural** (reticular, honeycomb) · fine crackles · clubbing · restrictive + DLCO ต่ำ |
| **Malignant mesothelioma** | **30–40 ปี** | **effusion ข้างเดียว + pleura หนาเป็นปุ่มล้อมปอด** · ไม่สัมพันธ์กับบุหรี่ · ต้อง **pleural biopsy** |
| **มะเร็งปอด** | | **ใยหิน × บุหรี่ = ความเสี่ยงทวีคูณ** |

### ILO classification — อ่านฟิล์ม pneumoconiosis อย่างไร

| | **Silicosis** | **CWP** | **Asbestosis** |
|---|---|---|---|
| โซน | **ปอดบน** | **ปอดบน** | **ปอดล่าง** |
| รูปแบบ | ปุ่มกลม (p q r) | ปุ่มกลม | เส้น (s t u) reticular |
| ต่อมน้ำเหลือง | **eggshell** | ไม่เด่น | ไม่เด่น |
| เยื่อหุ้มปอด | ปกติ | ปกติ | **plaque** · thickening |
| TB | **เสี่ยงสูงมาก** | เพิ่มเล็กน้อย | ไม่เพิ่ม |
| มะเร็ง | ปอด | — | ปอด + **mesothelioma** |
""",
    ["Silicosis: ปุ่มปอดบน + eggshell hilar node + PMF + เสี่ยง TB → คัดกรอง TB/LTBI",
     "CWP: ปุ่มปอดบน ไม่มี eggshell · Caplan = RA + rheumatoid nodules",
     "Pleural plaque = marker ของการสัมผัส ใยหิน calcify บนโดม ไม่เป็นมะเร็ง",
     "Asbestosis = fibrosis ปอดล่าง · mesothelioma = effusion + pleura หนาเป็นปุ่ม ระยะแฝง 30–40 ปี",
     "ใยหิน × บุหรี่ = มะเร็งปอดทวีคูณ · หลักการรักษาทุกโรค: หยุดสัมผัส"],
    [mcq(N(33), "A 58-year-old asymptomatic man worked for 25 years making asbestos-cement roofing sheets. Routine chest radiograph shows bilateral calcified plaques on the diaphragmatic and posterolateral pleura with clear lung fields; spirometry is normal. He smokes 15 cigarettes a day. What is the most appropriate advice?",
         ["The plaques indicate past asbestos exposure and need no specific treatment; stop smoking because smoking and asbestos multiply lung cancer risk", "Start oral corticosteroids to prevent progression of the plaques to asbestosis", "Arrange thoracoscopic pleural biopsy because the plaques are premalignant", "Perform pleurectomy to prevent mesothelioma", "Begin antifibrotic therapy with pirfenidone"], 0,
         "**Pleural plaques** = หนาตัวของ parietal pleura จากใยหิน มัก **calcify ที่โดมกะบังลมและผนังข้าง-หลัง** · ไม่มีอาการ สมรรถภาพปอดปกติ · เป็น **ตัวบ่งชี้ว่าเคยสัมผัส** ไม่ใช่ premalignant และไม่ต้องรักษา\n\nสิ่งสำคัญที่สุดคือ **เลิกบุหรี่** — ใยหินกับบุหรี่เพิ่มความเสี่ยงมะเร็งปอดแบบ **ทวีคูณ (multiplicative)** · ให้ความรู้อาการของ mesothelioma (เจ็บอก น้ำในช่องเยื่อหุ้มปอด) · ลงทะเบียนโรคจากการทำงาน\n\n- steroid/antifibrotic ไม่มีข้อบ่งชี้ (ไม่มี asbestosis)\n- biopsy/pleurectomy ไม่จำเป็นสำหรับ plaque ที่ calcify แบบทั่วไป",
         "Plaque = marker ของการสัมผัส · เลิกบุหรี่", "Asbestos-related disease", ["ตำราอายุรศาสตร์ — asbestos-related pleural disease (ไม่อยู่ในสไลด์)"], NLN + ["2.3.10-3(4)"]),
     mcq(N(34), "A 55-year-old former underground coal miner with seropositive rheumatoid arthritis has multiple well-defined 1–3 cm nodules scattered in both lungs that appeared over a few months, on a background of small rounded upper-zone opacities. Some nodules have cavitated. What is the most likely diagnosis?",
         ["Caplan syndrome (rheumatoid pneumoconiosis)", "Progressive massive fibrosis from silicosis", "Metastatic carcinoma", "Methotrexate-induced pneumonitis", "Asbestosis"], 0,
         "**Caplan syndrome** = **rheumatoid arthritis + rheumatoid nodules ขนาด 0.5–5 ซม. หลายก้อนในปอด** เกิดค่อนข้างเร็วในคนงานที่สัมผัสฝุ่น (เดิมอธิบายใน **คนงานเหมืองถ่านหิน** · พบได้ใน silica/asbestos) · ปุ่มอาจ cavitate หรือ calcify\n\nกลไก: ภูมิคุ้มกันที่ไวเกินใน RA ตอบสนองต่อฝุ่นเป็น necrobiotic nodule รอบอนุภาค\n\n- **PMF** เป็นก้อนรวมขนาดใหญ่ในปอดบนสองข้าง เกิดช้ากว่า\n- metastasis ต้องมีมะเร็งต้นกำเนิด\n- methotrexate pneumonitis เป็น GGO/consolidation กระจาย ไม่ใช่ปุ่มหลายก้อน\n- asbestosis เป็น fibrosis ปอดล่าง",
         "RA + ฝุ่น + ปุ่มหลายก้อน = Caplan", "Coal worker's pneumoconiosis", ["ตำราอายุรศาสตร์ — coal worker's pneumoconiosis (ไม่อยู่ในสไลด์)"], NLN + ["2.3.10-3(4)"]),
    ], NLN + ["2.3.10-3(4)", "B6.2.2(8)", "B6.2.4-3(2)"], src="ไม่อยู่ในสไลด์ — อิงตำราอายุรศาสตร์และ ILO 2022")

# ───────────────────────────── 18
sec("chest-img-18", "Hypersensitivity pneumonitis และ occupational asthma (ไม่อยู่ในสไลด์)",
    "HP: แอนติเจน (นก เชื้อรา หญ้าแห้ง) · centrilobular GGO nodules + mosaic + air trapping · ปอดบน-กลาง · หยุดสัมผัสคือหัวใจ · occupational asthma: แย่ลงวันทำงาน ดีขึ้นวันหยุด · serial PEF · byssinosis: Monday", 10,
"""### Hypersensitivity pneumonitis (HP)
- ปฏิกิริยาภูมิคุ้มกัน (type III + IV) ต่อ **แอนติเจนอินทรีย์ที่สูดเข้าไปซ้ำ ๆ** ใน **หลอดลมฝอยและถุงลม**
| แอนติเจน | ชื่อโรค |
|---|---|
| ขน/มูลนก (นกพิราบ นกแก้ว ขนเป็ดในหมอน) | **bird fancier's lung** |
| หญ้าแห้ง/ฟางขึ้นรา (thermophilic actinomycetes) | **farmer's lung** |
| เชื้อราในเครื่องปรับอากาศ/ความชื้น อ่างน้ำร้อน (MAC) | humidifier lung · hot tub lung |
| isocyanate (สี โฟม) | chemical worker's lung |
- **ATS/JRS/ALAT 2020** แบ่งเป็น **non-fibrotic** และ **fibrotic HP**
- **อาการ:** แบบเฉียบพลัน — ไข้ หนาวสั่น หอบ ไอ **4–8 ชม. หลังสัมผัส** หายใน 1–2 วัน · แบบเรื้อรัง — หอบค่อยเป็นค่อยไป ไอแห้ง crackles น้ำหนักลด
- **HRCT:** **centrilobular ground-glass nodules** · GGO · **mosaic attenuation + air trapping บนภาพหายใจออก** (three-density pattern) · เด่น **ปอดบน–กลาง** · fibrotic: reticulation, traction bronchiectasis
- **ตรวจเพิ่ม:** serum precipitins/specific IgG (บอกการสัมผัส ไม่ใช่การวินิจฉัย) · **BAL lymphocytosis** · spirometry restrictive + DLCO ต่ำ
- **รักษา:** **หยุดสัมผัสแอนติเจนอย่างถาวรสำคัญที่สุด** → corticosteroid ในรายรุนแรง/ไม่ดีขึ้น → fibrotic ที่ลุกลาม พิจารณา **nintedanib**

### Occupational asthma
- **Sensitizer-induced** (มีระยะแฝง): สารโมเลกุลใหญ่ — **แป้งสาลี/เอนไซม์ (เบเกอรี่)** latex สัตว์ทดลอง · สารโมเลกุลเล็ก — **isocyanate (สีพ่นรถ)** ฝุ่นไม้บางชนิด persulfate (ร้านทำผม)
- **Irritant-induced (RADS)** — หลังสัมผัสสารระคายเคืองความเข้มข้นสูงครั้งเดียว
- ต้องแยกจาก **work-exacerbated asthma** (หืดเดิมกำเริบจากที่ทำงาน)
- **ยืนยัน:** บันทึก **serial PEF ≥ 4 ครั้ง/วัน นาน 3–4 สัปดาห์** ทั้งวันทำงานและวันหยุด · ± specific inhalation challenge
- **รักษา:** **ย้ายออกจากการสัมผัสสารก่อโรคให้เร็ว** + ยาตามแนวทางหืด · ทำงานเดิมต่อพร้อม ICS = โรคถาวร

### Byssinosis — รูปแบบกลับด้าน
- ฝุ่น **ฝ้าย ป่าน ปอ** · แน่นหน้าอก หอบ **วันแรกที่กลับมาทำงาน (Monday chest tightness)** แล้วดีขึ้นในวันต่อ ๆ ไปของสัปดาห์ — ตรงข้ามกับ occupational asthma ที่แย่ลงตลอดสัปดาห์

### ฝุ่น/สาร → โรค (สรุปสำหรับข้อสอบ)
| สาร | อาชีพ | โรค |
|---|---|---|
| Silica | หิน ทราย เหมือง | silicosis · TB · มะเร็งปอด |
| ถ่านหิน | เหมืองถ่านหิน | CWP · Caplan |
| ใยหิน | กระเบื้องหลังคา ผ้าเบรก อู่เรือ | plaque · asbestosis · mesothelioma · มะเร็งปอด |
| Beryllium | อิเล็กทรอนิกส์ อวกาศ | berylliosis (granuloma เหมือน sarcoid) |
| ฝ้าย | โรงทอ | byssinosis |
| แอนติเจนนก/เชื้อรา | เลี้ยงนก เกษตรกร | HP |
| แป้ง isocyanate latex | เบเกอรี่ สีพ่น โรงพยาบาล | occupational asthma |
""",
    ["HP: แอนติเจนอินทรีย์ → centrilobular GGO nodules + mosaic + air trapping (ปอดบน-กลาง)",
     "HP: หยุดสัมผัสถาวรสำคัญที่สุด · fibrotic ลุกลาม → nintedanib",
     "Acute HP: ไข้ หอบ 4–8 ชม. หลังสัมผัส (farmer's lung)",
     "Occupational asthma: แย่ลงวันทำงาน ดีขึ้นวันหยุด → serial PEF → ย้ายออกจากการสัมผัส",
     "Byssinosis: แน่นอกวันแรกของสัปดาห์ (Monday)"],
    [mcq(N(35), "A 45-year-old farmer develops fever, chills, dry cough and breathlessness about 6 hours after forking mouldy hay in a closed barn. The symptoms resolve over 2 days but recur each time he repeats the task. Chest examination reveals fine inspiratory crackles. Which mechanism best explains his illness?",
         ["Immune-mediated hypersensitivity pneumonitis to inhaled thermophilic actinomycete antigens", "IgE-mediated occupational asthma to grass pollen", "Toxic pneumonitis from nitrogen dioxide in silage", "Invasive pulmonary aspergillosis", "Acute silicosis from soil dust"], 0,
         "**Farmer's lung** — **acute hypersensitivity pneumonitis**: อาการไข้ หนาวสั่น ไอ หอบ **4–8 ชั่วโมงหลังสัมผัส** หายใน 1–2 วันและเป็นซ้ำทุกครั้ง · แอนติเจนคือ **thermophilic actinomycetes** ในหญ้าแห้งขึ้นรา · กลไก type III (immune complex) + type IV (T cell, granuloma) ในหลอดลมฝอยและถุงลม → crackles\n\n**รักษา:** เลี่ยงการสัมผัส (หน้ากาก ปรับวิธีเก็บหญ้า) ± steroid\n\n- occupational asthma (IgE) อาการเริ่มเร็วกว่า เป็น wheeze ไม่มีไข้\n- silo-filler's disease (NO₂) เกิดจากไซโลข้าวโพดสด ไม่ใช่หญ้าแห้งขึ้นรา\n- invasive aspergillosis เกิดในผู้ภูมิคุ้มกันต่ำ\n- silicosis ไม่เกิดเป็นพัก ๆ ตามการสัมผัส",
         "อาการ 4–8 ชม. หลังสัมผัส + ไข้ + crackles = acute HP", "Hypersensitivity pneumonitis", ["ATS/JRS/ALAT HP guideline 2020 (ไม่อยู่ในสไลด์)"], NLN + ["2.3.10-3(4)"]),
     mcq(N(36), "A 40-year-old cotton-mill worker reports chest tightness and cough that are worst on the first day back at work after the weekend and improve over the following working days. What is the most likely diagnosis?",
         ["Byssinosis", "Sensitiser-induced occupational asthma", "Chronic hypersensitivity pneumonitis", "Silicosis", "Berylliosis"], 0,
         "**Byssinosis** จากฝุ่น **ฝ้าย/ป่าน/ปอ** — ลักษณะเฉพาะคือ **แน่นหน้าอกวันแรกที่กลับมาทำงาน (Monday chest tightness)** แล้ว **ดีขึ้น** ในวันถัดไปของสัปดาห์ (tolerance ชั่วคราว) · กลไกเชื่อว่าเกี่ยวกับ endotoxin ในฝุ่นกระตุ้นการอักเสบและหลอดลมหดเกร็ง\n\n- **occupational asthma**: แย่ลง **ตลอดสัปดาห์ทำงาน** ดีขึ้นวันหยุด (รูปแบบตรงข้าม)\n- HP เรื้อรัง: หอบค่อยเป็นค่อยไป crackles ไม่ใช่รูปแบบรายสัปดาห์\n- silicosis/berylliosis: โรคพังผืด/granuloma เรื้อรัง ไม่ผันแปรตามวัน",
         "Monday chest tightness = byssinosis (ตรงข้าม occupational asthma)", "Occupational lung disease", ["ตำราอายุรศาสตร์ — occupational lung disease (ไม่อยู่ในสไลด์)"], NLN + ["2.3.10-3(4)", "2.3.10(1)"]),
    ], NLN + ["2.3.10-3(4)", "2.3.10(1)", "B6.2.2(2)"], src="ไม่อยู่ในสไลด์ — อิง ATS/JRS/ALAT 2020 (HP) และตำราอายุรศาสตร์")

# ───────────────────────────── MEQ / OSCE
MEQ = [{"id": "CH-IMG-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Stone-grinding worker with upper-zone nodules, eggshell hilar calcification and a cavitating mass — systematic CXR reading, silicotuberculosis vs lung cancer, occupational management",
 "vignette": """ผู้ป่วยชายไทยอายุ 52 ปี อาชีพตัดและขัดหินแกรนิตในโรงงานหินมา 25 ปี ไม่ค่อยใส่หน้ากาก สูบบุหรี่ 20 pack-years
CC: ไอมีเสมหะ 2 เดือน
PI: 2 ปีก่อนเริ่มเหนื่อยง่ายเวลาขึ้นบันได ค่อย ๆ มากขึ้น · 2 เดือนนี้ไอมีเสมหะสีเหลือง มีไข้ต่ำ ๆ ตอนเย็น เหงื่อออกกลางคืน น้ำหนักลด 6 กก.
PE: BT 37.8 °C · RR 22/min · SpO₂ 94% (room air) · ไม่มี clubbing · ต่อมน้ำเหลืองไม่โต · fine crackles ปอดบนสองข้าง
CXR PA (บรรยาย): ป้าย Upright · หัว clavicle ห่าง spinous process เท่ากัน · เห็น posterior rib 10 เหนือโดมขวา · ปุ่มกลมขนาด 2–5 มม. จำนวนมากกระจายในปอดบนทั้งสองข้าง · ต่อมน้ำเหลือง hilum สองข้างโตและมีหินปูนเป็นวงรอบ · ที่ RUL มีก้อนทึบขนาด 4 ซม. ภายในมีโพรงผนังหนา 8 มม. · hilum ทั้งสองข้างถูกดึงขึ้น · ไม่มีน้ำในช่องเยื่อหุ้มปอด · CTR 0.45""",
 "questions": [
  {"q": "1. จงอ่านฟิล์มนี้อย่างเป็นระบบ และสรุปสิ่งผิดปกติสำคัญ (3 คะแนน)",
   "a": """**คุณภาพ (RIPE):** PA ยืน ไม่หมุน (clavicle–spinous process เท่ากัน) หายใจเข้าเต็ม (posterior rib 10) → แปลผลได้
**สิ่งผิดปกติ**
- **small rounded opacities ปอดบนสองข้าง** (ILO ชนิด p/q) — upper zone nodular pattern
- **bilateral hilar lymphadenopathy + eggshell calcification**
- **conglomerate mass 4 ซม. ที่ RUL** (= PMF) **มีโพรงผนังหนา**
- hilum ถูกดึงขึ้น (volume loss ปอดบนจากพังผืด)
- หัวใจขนาดปกติ ไม่มี effusion"""},
  {"q": "2. จงให้การวินิจฉัยแยกโรค 3 อันดับ พร้อมเหตุผล (3 คะแนน)",
   "a": """1. **Silicosis with progressive massive fibrosis + pulmonary TB (silicotuberculosis)** — อาชีพตัดหิน 25 ปี ปุ่มปอดบน + eggshell + PMF · มี **ไข้ เหงื่อกลางคืน น้ำหนักลด และโพรงในก้อน** · silica ทำให้ macrophage เสียหน้าที่ **เสี่ยง TB สูงมาก**
2. **มะเร็งปอด (squamous cell) ที่มีโพรง** — สูบบุหรี่ + silica (IARC group 1) · โพรงผนังหนาเป็นลักษณะของ SCC
3. **PMF ที่เนื้อตายจากขาดเลือด (ischemic cavitation)** หรือติดเชื้ออื่น เช่น NTM/fungus
(silicosis อย่างเดียวไม่อธิบายไข้และน้ำหนักลด)"""},
  {"q": "3. จงบอกการส่งตรวจที่เหมาะสม (3 คะแนน)",
   "a": """- **Sputum AFB smear 2–3 ครั้ง + Xpert MTB/RIF + culture/DST** (รวม NTM)
- **Anti-HIV** (ผู้ป่วย TB ทุกราย)
- **CT chest ฉีดสี** — ลักษณะโพรง ผนัง ก้อนอื่น ต่อมน้ำเหลือง mediastinum
- ถ้าเสมหะไม่พบเชื้อหรือสงสัยมะเร็ง → **bronchoscopy + BAL + biopsy** หรือ CT-guided biopsy
- **Spirometry + DLCO** (ประเมิน restrictive/mixed) · CBC LFT Cr ก่อนเริ่มยา TB
- อ่านฟิล์มตาม **ILO classification** เพื่อบันทึกโรคจากการทำงาน"""},
  {"q": "4. ผล Xpert พบ MTB ไม่ดื้อ rifampicin จงวางแผนการรักษาและการดูแลด้านอาชีพ (3 คะแนน)",
   "a": """**รักษา TB:** สูตรมาตรฐาน 2HRZE/4HR ตามแนวทางแห่งชาติ · ติดตามใกล้ชิดเพราะ silicotuberculosis ตอบสนองช้าและกลับเป็นซ้ำสูงกว่า (บางแนวทางพิจารณาขยายระยะเวลา) · DOT · ตรวจผู้สัมผัสร่วมบ้าน
**Silicosis:** **ไม่มียารักษาให้หาย** → **หยุดการสัมผัส silica (ย้ายงาน)** · **เลิกบุหรี่** · วัคซีนไข้หวัดใหญ่/pneumococcus · pulmonary rehabilitation · O₂ ถ้าจำเป็น · ติดตามมะเร็งปอด
**ด้านอาชีพ:** แจ้งเป็น **โรคจากการทำงาน** และใช้สิทธิ **กองทุนเงินทดแทน** · แนะนำสถานประกอบการ — **ตัดหินแบบเปียก ระบายอากาศ ใช้ respirator (N95/P2)** · **คัดกรองเพื่อนร่วมงาน** ด้วย CXR (ILO) + spirometry และคัดกรอง TB/latent TB เป็นระยะ"""}],
 "ref": ["ตำราอายุรศาสตร์ — silicosis/silicotuberculosis (ไม่อยู่ในสไลด์)", "ILO Guidelines for the use of the ILO International Classification of Radiographs of Pneumoconioses (revised 2022)", "สไลด์ อ.พจนี — Nodular pattern, Cavitation"],
 "nl": ["2.3.10-3(4)", "B6.2.2(8)", "3.2.1", "B6.2.4-3(2)"], "years": [], "_kind": "meq", "_set": SET}]

OSCE = [{"id": "CH-IMG-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "OSCE – Systematic presentation of a chest radiograph (right upper lobe collapse with Golden S sign)",
 "station": "OSCE (อ่านและนำเสนอฟิล์ม) 5 นาที · ผู้คุมสอบ 1 คน · ฟิล์ม CXR PA หนึ่งแผ่น",
 "instruction": """ผู้ป่วยชายอายุ 64 ปี สูบบุหรี่ 50 pack-years มาด้วยไอเป็นเลือด 1 เดือน น้ำหนักลด
ท่านได้รับฟิล์ม CXR PA ของผู้ป่วย (ฟิล์มในสถานีเหมือนภาพ **Golden's sign** ในหัวข้อ Lobar collapse — ปอดขวาบนทึบ ขอบล่างรูปตัว S กลับด้าน hilum ขวายก trachea เบี้ยวไปขวา)

**จงทำสิ่งต่อไปนี้**
1. นำเสนอการอ่านฟิล์มอย่างเป็นระบบให้ผู้คุมสอบฟัง
2. สรุปการแปลผล (impression) และการวินิจฉัยแยกโรค
3. บอกการตรวจขั้นต่อไป""",
 "answer": """| หัวข้อ | สิ่งที่ต้องทำ/พูด | คะแนน |
|---|---|---|
| **ตรวจตัวผู้ป่วยและฟิล์ม** | ชื่อ อายุ HN วันที่ถ่าย · **ขอฟิล์มเก่ามาเทียบ** | 1 |
| **ท่าถ่าย** | PA ยืน (ป้าย/gastric bubble/scapula นอกปอด) | 1 |
| **คุณภาพ (RIPE)** | rotation (clavicle–spinous process) · inspiration (นับซี่โครง) · exposure (เห็นกระดูกสันหลังหลังหัวใจ) | 2 |
| **Airway** | **trachea เบี้ยวไปขวา** (ถูกดึง) | 1 |
| **Lungs — บรรยายรอยโรค** | ทึบ **ปอดขวาบน** · ขอบล่าง **ส่วนนอกเว้าขึ้น ส่วนในโป่งลง = reverse S** · minor fissure ยกขึ้น | 2 |
| **Volume loss / silhouette** | **hilum ขวายก** · ขอบ mediastinum ขวาบนหาย · (juxtaphrenic peak/โดมขวายก) — บอกว่าเป็น **atelectasis ไม่ใช่ consolidation** | 2 |
| **Heart · mediastinum · hila อีกข้าง** | ขนาดหัวใจ (PA) · hilum ซ้าย · ต่อมน้ำเหลือง | 1 |
| **Diaphragm · ใต้โดม · hidden areas** | apex · retrocardiac · กระดูก/ซี่โครง (หา metastasis) · soft tissue | 1 |
| **Impression** | **RUL collapse with Golden S sign → central obstructing mass ที่ hilum ขวา** เข้าได้กับ **มะเร็งปอด (มัก squamous cell)** | 2 |
| **DDx + ขั้นต่อไป** | DDx: ก้อน/ต่อมน้ำเหลือง TB อุดหลอดลม · carcinoid · **CT chest ฉีดสี (staging) + bronchoscopy biopsy** · Ca Na · sputum AFB | 1 |
| **การนำเสนอ** | เป็นลำดับ ใช้ศัพท์ถูก สรุปกระชับ | 1 |

**รวม 15 คะแนน** · **ข้อผิดพลาดร้ายแรง:** เรียกว่า RUL pneumonia แล้วให้ยาปฏิชีวนะโดยไม่บอกการหาก้อน · ไม่ตรวจคุณภาพฟิล์ม""",
 "ref": ["สไลด์ อ.พจนี — หลักการอ่านภาพถ่ายรังสีทรวงอก, Technical adequacy, RUL atelectasis, Golden's sign", "หลักจำ RIPE / ABCDE"],
 "nl": ["3.2.1", "2.3.10(2)", "B6.2.4-3(2)"], "years": [], "_kind": "meq", "_set": SET}]

LECTURE = {
 "lec": LEC, "date": "พฤ. 1 ต.ค.",
 "title": "Image in chest — อ่าน CXR อย่างเป็นระบบ และโรคปอดจากการทำงาน",
 "subtitle": "ท่าถ่ายและคุณภาพฟิล์ม (RIPE) · density กับขอบ · anatomy และ hidden areas · consolidation GGO silhouette · interstitial patterns · atelectasis และ lobar collapse · nodule cavity · hyperlucency · mediastinum · PE/HF · effusion · pneumothorax · pneumoconiosis HP occupational asthma — พร้อมภาพรังสีจริงจากสไลด์ 79 ภาพ",
 "objectives": [
   "ตรวจตัวผู้ป่วย ท่าถ่าย และคุณภาพฟิล์ม (RIPE) และบอกได้ว่าฟิล์มไม่ดีหลอกให้เห็นอะไร",
   "อธิบาย density และ attenuation และใช้หลัก \"ขอบเกิดจากรอยต่อ\" อธิบาย silhouette sign air bronchogram และ pleural line",
   "อ่าน CXR อย่างเป็นระบบตาม ABCDE และตรวจ hidden areas ทุกครั้ง พร้อมรู้ค่าปกติ (CTR, hilum, โดม)",
   "แยก consolidation, GGO, interstitial patterns และ atelectasis และใช้ silhouette sign บอกกลีบ",
   "บอกลักษณะการยุบของแต่ละกลีบ (Golden S, Luftsichel, flat waist) และแปลผล white-out hemithorax",
   "แยกก้อนในปอด/นอกปอด cyst/cavity/bulla/abscess และวางแผนดูแลก้อนตาม Fleischner 2017",
   "อ่านสัญญาณของ emphysema, bronchiectasis, PE, pulmonary hypertension และ heart failure",
   "อ่าน pleural effusion (meniscus, subpulmonic, loculated) และ pneumothorax (tension, ขนาด) และเชื่อมกับการรักษา",
   "อธิบายกลไกและภาพของ silicosis, CWP, โรคจากใยหิน, HP และ occupational asthma และการป้องกัน"],
 "nlGap": "เกณฑ์ฯ มีรหัส `นล. 3.2.1` Chest x-ray เป็นแกนของคาบ และ `2.3.10-3(4)` Occupational lung diseases แต่ **ไฟล์สไลด์ที่ได้รับ (191 หน้า) ไม่มีส่วน occupational lung disease, heart failure และมะเร็งปอด** — หัวข้อเหล่านั้นอิงตำราและแนวทางด้านล่าง · การดูแล pneumothorax ในสไลด์มีเฉพาะเกณฑ์ขนาด จึงเพิ่ม BTS 2023 · ก้อนในปอดสไลด์มีเฉพาะนิยาม จึงเพิ่ม Fleischner 2017",
 "guidelines": [
   "**Fleischner Society 2017** — management of incidental pulmonary nodules on CT (MacMahon H, et al. Radiology 2017)",
   "**BTS Guideline for pleural disease 2023** — pneumothorax: ตัดสินตามอาการและ high-risk features (Roberts ME, et al. Thorax 2023)",
   "**ILO International Classification of Radiographs of Pneumoconioses (revised 2022)**",
   "**ATS/JRS/ALAT 2020** — diagnosis of hypersensitivity pneumonitis in adults",
   "**ACCP 2013** — methods for staging non-small cell lung cancer (EBUS-TBNA ก่อนผ่าตัด)",
   "**ATLS 10th edition** — needle decompression ใน tension pneumothorax"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ───────────────────────────── ประกอบ
# ภาพเคลื่อนไหว + หลักจำ
secs = {s_["id"]: s_ for s_ in S}
for it in AN.ITEMS:
    s_ = secs[it["sec"]]
    a = it["anim"]
    s_.setdefault("anims", {})[a["key"]] = {k: a[k] for k in ("title", "svg", "steps")}
    s_["md"], ok = _insert_marker(s_["md"], it.get("after", ""), "[[anim:%s]]" % a["key"])
    assert ok, ("ไม่พบหัวข้อ", it["sec"], it.get("after"))
for m in AN.MNEM:
    secs[m["sec"]].setdefault("mnem", []).append({x: m[x] for x in ("name", "what", "lines", "note", "src") if m.get(x)})

# กระจายตำแหน่งคำตอบ (คำตอบถูกเขียนไว้ที่ choices[0] · ข้อที่ตัวเลือกเรียงตามตัวเลข keep ไว้)
_slot = 0
for s_ in S:
    for it in s_["items"]:
        if it.pop("_keep", False):
            continue
        assert it["answer"] == 0, it["id"]
        tgt = [2, 4, 1, 3, 0][_slot % 5]; _slot += 1
        ch = it["choices"]; ch[0], ch[tgt] = ch[tgt], ch[0]; it["answer"] = tgt

# ตรวจภาพจริง: ทุก [[img:]] มีใน imgs, ทุก imgs ถูกใช้, src ตรงรูปแบบและไฟล์มีจริง
import re
for s_ in S:
    used = re.findall(r"^\s*\[\[img:([\w-]+)\]\]\s*$", s_["md"], re.M)
    imgs = s_.get("imgs", {})
    assert set(used) == set(imgs), (s_["id"], set(used) ^ set(imgs))
    assert len(used) == len(set(used)), s_["id"]
    for k, g in imgs.items():
        assert re.match(r"^img/[\w/.-]+\.(jpg|png|webp)$", g["src"]), g["src"]
        assert os.path.exists(os.path.join(BUILD, g["src"])), g["src"]
        assert g.get("alt") and g.get("credit") and (g.get("cap") or g.get("quiz")), (s_["id"], k)
allimg = [k for s_ in S for k in s_.get("imgs", {})]
assert len(allimg) == len(set(allimg)), "key ภาพซ้ำ"

path = os.path.join(BUILD, "data", SET + ".json")
data = json.load(open(path, encoding="utf-8"))
data = [l for l in data if l.get("lec") != LEC]
pos = next(i + 1 for i, l in enumerate(data) if l.get("lec") == "17")
data.insert(pos, LECTURE)
probs, nfig, _ = apply_module("figs_chest_img", data, False)
assert not probs, probs
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

BANK_MAP = {
    "chest-img-02": ["CH-MCQ-25"],
    "chest-img-06": ["CH-OLD-39"],
    "chest-img-08": ["CH-MCQ-31"],
    "chest-img-10": ["CH-MCQ-26", "CH-MCQ-27", "CH-OLD-40", "CH-OLD-41", "CH-OLD-42"],
    "chest-img-17": ["CH-MCQ-29", "CH-MCQ-30", "CH-OLD-35", "CH-OLD-36", "CH-OLD-37"],
    "chest-img-18": ["CH-MCQ-28", "CH-OLD-38"],
}
added = link(SET, LEC, BANK_MAP)

d = json.load(open(path, encoding="utf-8"))
L = [l for l in d if l["lec"] == LEC][0]
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = ({c for s_ in L["sections"] for c in s_["nl"]} | {c for s_ in L["sections"] for i in s_["items"] for c in i.get("nl", [])}
         | {c for m in L["meq"] + L["osce"] for c in m["nl"]})
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
ids = [i["id"] for l in d for s_ in l["sections"] for i in s_["items"]]
dup = {x for x in ids if ids.count(x) > 1}
assert not dup, dup
for s_ in L["sections"]:
    assert "```" not in s_["md"], s_["id"]
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == SET:
        m["lectureCount"] = len(d)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | ข้อใหม่ %d + คลัง %d | meq %d | osce %d | figs %d | anims %d | mnem %d | imgs %d | nl %d" % (
    len(S), sum(1 for s_ in S for i in s_["items"]), added, len(MEQ), len(OSCE), nfig, len(AN.ITEMS), len(AN.MNEM),
    len(allimg), len(codes)))
