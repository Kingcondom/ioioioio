#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""อัปเดตคาบ air 23 "Approach to arthritis" ตามสไลด์จริงของ อ.กิตติวรรณ + ราวด์ข้างเตียง 5 พ.ย. 2569 — ไม่สร้างคาบใหม่

    python3 artifact/tools/update_arthritis.py            # เขียน data/air.json
    python3 artifact/tools/update_arthritis.py --check    # ตรวจโดยไม่เขียน

แหล่ง: "Lec 2.1 Lec Approach to Arthritis" (81 หน้า · ศ. 2 ต.ค. 2569) · สไลด์เคส ARTHRITIS กลุ่ม 19B/20B (52 หน้า · พฤ. 5 พ.ย.)
· ไฟล์เสียง Plaud 2 ไฟล์ของราวด์ 5 พ.ย. (กลุ่มนำเสนอ + อาจารย์สรุป) → โน้ต slides/arthritis_notes.md
- หัวข้อใหม่ air-23-art-01..07 (แทรกตามตำแหน่งใน AFTER/BEFORE) · ข้อใหม่ AIR-ART-MCQ-NN · AIR-ART-MEQ-01 · AIR-ART-OSCE-01
- callout "> **กิตติวรรณ · …**" ในหัวข้อเดิม (สิ่งที่สไลด์/ราวด์เพิ่มหรือต่าง + ✍️) · ภาพเคลื่อนไหว/หลักจำจาก anims_air_arthritis.py
- ภาพจริงจาก extract_arthritis.py → img/air/art-*.jpg (section.imgs)
- ไม่แตะ id/choices/answer ของข้อเดิม · คง anims/mnem/figs/imgs เดิมทุกชิ้น · ไม่แตะคาบอื่น

รันซ้ำได้: หัวข้อใหม่ถูกแทนที่ทั้งก้อน · callout และ marker [[anim:art-*]] [[img:art-*]] ของสคริปต์นี้ถูกถอดออกก่อนแล้วใส่ใหม่ ·
ข้อ/หลักจำ/MEQ/OSCE/guidelines/objectives ของสคริปต์นี้แทนที่ด้วย id/ชื่อ ไม่เพิ่มซ้ำ"""
import json, os, re, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(TOOLS)), "dashboard"))
import anims_air_arthritis as AN  # noqa: E402
from patch_learn_anim import _insert_marker  # noqa: E402

ART = os.path.dirname(TOOLS)
PATH = os.path.join(ART, "data", "air.json")
LEC = "23"
SRC = "สไลด์ อ.กิตติวรรณ — Approach to Arthritis (Lec 2.1) + ราวด์ข้างเตียง 5 พ.ย. 2569"
SRC_TAG = " · สไลด์ อ.กิตติวรรณ + ราวด์ 5 พ.ย."
CR_S = "ภาพจากสไลด์ Approach to Arthritis — อ.กิตติวรรณ · รพ.ราชวิถี"
CR_C = "ภาพจากสไลด์เคส ARTHRITIS กลุ่ม 19B/20B"
REF = lambda p: ["สไลด์ อ.กิตติวรรณ (Approach to Arthritis) — " + p]
REFR = lambda p: ["ราวด์ข้างเตียง 5 พ.ย. 2569 (Plaud) — " + p]
P = "AIR-ART-"


def mcq(iid, stem, right, wrong, pos, explain, pearl, topic, ref, nl):
    """right = คำตอบที่ถูก · wrong = ตัวลวง 4 ข้อ · pos = ตำแหน่งคำตอบ (กระจายเฉพาะข้อใหม่)"""
    assert len(wrong) == 4 and 0 <= pos <= 4, iid
    ch = list(wrong)
    ch.insert(pos, right)
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": ch, "answer": pos, "explain": explain,
            "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}


def mcq_fixed(iid, stem, choices, answer, explain, pearl, topic, ref, nl):
    """ตัวเลือกเรียงตามธรรมชาติ (ตัวเลข) — ไม่สลับ"""
    assert len(choices) == 5 and 0 <= answer <= 4, iid
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer, "explain": explain,
            "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}


def sec(sid, title, summary, minutes, nl, md, pearls, items, imgs=None):
    s = {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": SRC,
         "nl": nl, "md": md.strip(), "pearls": pearls, "items": items}
    if imgs:
        s["imgs"] = imgs
    return s


def img(fn, title, alt, cap=None, credit=CR_S, q=None, quiz=None):
    d = {"src": "img/air/%s.jpg" % fn, "title": title, "alt": alt, "credit": credit}
    if quiz:
        d["q"], d["quiz"] = q, quiz
    else:
        d["cap"] = cap
    return d


NL_APP = ["2.1.27", "2.1.26"]
NL_GOUT = ["2.3.13(2)", "B5.2.5(1)"]
NL_RA = ["2.3.13-3(12)", "B5.2.2-3(4)"]
NL_SPA = ["2.3.13-3(13)", "B5.2.2-3(3)"]
NL_SLE = ["2.3.13-3(15)", "B5.2.2-3(5)"]
NL_SF = ["B5.3(3)", "3.1.7"]

NEW = {}

# ═════════════════════════════════════════════════════════════════ หัวข้อใหม่ 1 · I-I-N-O-D-E
NEW["air-23-art-01"] = sec(
    "air-23-art-01", "I-I-N-O-D-E — กรอบเข้าหาผู้ป่วยปวดข้อของ อ.กิตติวรรณ",
    "หกคำถามตามลำดับ: ในข้อหรือนอกข้อ · อักเสบไหม · กี่ข้อ · เริ่มอย่างไร · กระจายแบบไหน · มีอะไรนอกข้อ — ใช้ตอบ MEQ ได้ทั้งข้อ",
    12, NL_APP + ["2.3.13-3(13)"],
    """
อาจารย์เปิดการสรุปราวด์ 5 พ.ย. ว่า **"พี่จะขอเน้นเรื่อง approach to arthritis"** — รายละเอียดของ RA และเกาต์เรียนในเลคเชอร์เฉพาะแล้ว สิ่งที่ต้องทำได้ข้างเตียงคือไล่คำถามตามลำดับนี้ทุกครั้ง (ตรงกับสไลด์ p3–p9)

| ตัวอักษร | คำถาม | เครื่องมือ |
|---|---|---|
| **I** | Intra- หรือ extra-articular | active vs passive ROM · ทุกทิศ vs บางทิศ · จุดกดเจ็บ |
| **I** | Inflammatory หรือไม่ | ลักษณะบวม · ร้อนแดง · **morning stiffness กี่นาที** · อาการทั่วกาย |
| **N** | Number | mono 1 · oligo **2–4** · poly **≥ 5** |
| **O** | Onset และ pattern | abrupt / rapid / insidious · acute vs chronic **≥ 6 สัปดาห์** · migratory / additive / intermittent |
| **D** | Distribution | สมมาตร · ข้อเล็ก/ใหญ่ · peripheral vs axial · DIP กับ MCP |
| **E** | Extra-articular features | enthesitis · dactylitis · sacroiliitis · ผิว ตา ลำไส้ ปอด ไต |

### อาการนำของโรคข้อ (สไลด์ p3)
- **Pain** — อาการที่พามาเกือบทุกราย
- **Stiffness = ข้อฝืดหลังจากไม่ได้ขยับ (inactivity)** — เห็นชัดที่สุดตอนตื่นเช้า "กางมือไม่ได้ กำมือก็ลำบาก"
- **Swelling ต้องบอก consistency** — **rubbery** (หยุ่นเหมือนยางลบ = synovium หนา) · **bony** (แข็งเป็นกระดูก = osteophyte) · **cystic** (ถุงน้ำ)
- **Limited ROM** และ **weakness/muscle atrophy** — ผู้ป่วยบางรายยกแขนไม่ขึ้นเพราะกล้ามเนื้ออ่อนแรงหรือลีบจากไม่ได้ใช้ (disuse atrophy) ไม่ใช่เพราะข้อ ต้องซักและตรวจแยกให้ได้

### I — ในข้อหรือนอกข้อ
| | Intra-articular | Extra-articular (periarticular) |
|---|---|---|
| โครงสร้าง | joint capsule เข้าไป: synovium · articular cartilage · subchondral bone · periosteum | enthesis · bursa · เอ็น · กล้ามเนื้อ · ligament · ผิวหนัง · ไขมันใต้ผิวหนัง · หลอดเลือดดำ |
| ทิศที่เจ็บ | **ทุกทิศ** ของ ROM | **บางทิศ** (ทิศที่ใช้เอ็นนั้น) |
| active / passive | **เจ็บทั้งคู่** | **เจ็บตอน active เป็นหลัก** passive แทบไม่เจ็บ |
| จุดกดเจ็บ | ไม่ชัด อยู่ตามแนวข้อ (ข้อใหญ่อยู่ลึกยิ่งไม่ชัด) | ชัด กดจุดเดียว |

**ทำไมต้องแยกก่อน** — การรักษาต่างกัน และ **ก่อนเจาะข้อ** ต้องแน่ใจว่ารอยโรคอยู่ในข้อ ถ้าผิวหนังข้างบนเป็น **cellulitis หรือแผล** การแทงเข็มผ่านจะ **พาเชื้อเข้าข้อที่สะอาด** (✍️ สไลด์ p4 "① เจาะข้อ → R/O septic") · อาจารย์: active/passive **"ไม่ต้องจำ ใช้ logic"** แล้วจะจำได้จนจบปี 6

[[anim:art-romloc]]

### I — อักเสบหรือไม่อักเสบ (สไลด์ p6)
| สิ่งที่ดู | อาจารย์สอน |
|---|---|
| Joint tenderness | **แยกไม่ได้** — กระดูกหัก เข่าพลิก ก็เจ็บ |
| Swelling | **synovial hypertrophy (บวมหยุ่น ๆ เป็นก้อน lumpy) = most reliable sign** · ✍️ **"น้ำอย่างเดียวแยกไม่ได้"** — effusion มีได้ทั้งเลือดออกจาก trauma และข้ออักเสบ |
| Erythema / warmth | septic และ RA ร้อนมาก · เลือดออกในข้อร้อนได้บ้าง (secondary inflammation) แต่ไม่มาก |
| **Morning stiffness — ต้องบอก duration** | inflammatory **> 30 นาที** (✍️ 30–60 นาที) · เกณฑ์ RA ปี 1987 ใช้ **≥ 1 ชั่วโมง** · **OA ฝืดได้แต่ขยับ 2–3 นาที ไม่เกิน ~5 นาที** (บางราย 10–15 นาที แต่ไม่เกินครึ่งชั่วโมง) |
| Constitutional | ไข้ fatigue malaise น้ำหนักลด → inflammatory joint disease |

> **ราวด์ 5 พ.ย. · morning stiffness** — อาจารย์: "เวลาถามจะได้คะแนน **ต้องระบุ duration** … โดยเฉพาะข้อสอบ **MEQ อย่าลืมถาม**" · OA ชื่อลงท้าย -itis แต่เป็น **non-inflammatory (degenerative)** · ไม่มีประวัติ trauma แต่ข้อบวมน้ำมาก → ให้น้ำหนักกับ inflammatory มากขึ้น

#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **บวมหยุ่นเป็นก้อน (rubbery/lumpy)** | synovium อักเสบแบ่งตัวหนาขึ้น มีหลอดเลือดใหม่ (pannus) คลำได้เป็นเนื้อหยุ่นรอบข้อ | ตรงกับ inflammatory มากที่สุด (RA, SpA ส่วนปลาย) |
| **บวมแข็งเป็นกระดูก (bony)** | กระดูกอ่อนสึก → กระดูกใต้ผิวข้อสร้าง osteophyte ที่ขอบข้อ | OA (Heberden, Bouchard) |
| **บวมเป็นถุงน้ำ (cystic)** | ของเหลวในโพรงข้อ/bursa — อาจเป็นน้ำอักเสบ เลือด หรือหนอง | **บอกชนิดไม่ได้จนกว่าจะเจาะ** |
| **ฝืดนาน > 30 นาทีหลังตื่น** | ขณะนอนนิ่ง น้ำอักเสบและ cytokine คั่งในเนื้อเยื่อรอบข้อ ขยับแล้ว lymphatic ค่อย ๆ ระบาย | OA ฝืดสั้น (gelling) เพราะไม่มีน้ำอักเสบคั่ง |
| **ไข้ เพลีย น้ำหนักลด** | IL-1, IL-6, TNF จาก synovium เข้ากระแสเลือด (ไฮโปทาลามัส ตับ กล้ามเนื้อ) | ไม่มีใน OA/trauma |

### N — จำนวนข้อ
**Mono = 1 · oligo = 2–4 · poly = ≥ 5** (สไลด์ p8 เขียน "> 4") — อาจารย์: "**คนละโลกกัน**" เพราะ DDx ของ mono/oligo กับ poly แทบไม่ซ้ำกัน จึงให้นักศึกษาทำโจทย์สองแบบ (เคสชาย 60 ปีข้อเดียว vs เคสหญิง 34 ปีหลายข้อ)

### O — Onset และ pattern
- **ความเร็ว** — abrupt (ถึงสุดในราว 1 ชั่วโมง) = **trauma, crystal** · rapid (1–2 วัน) = **septic**, acute inflammatory · insidious (สัปดาห์–เดือน) = **RA, OA, CTD** (สไลด์ p9 + การนำเสนอเคสเกาต์)
- **Acute vs chronic** — เส้นแบ่ง **6 สัปดาห์** (✍️ "≥ 6 wk") จำง่ายเพราะตรงกับเกณฑ์ ACR/EULAR ของ RA
- **Migratory** — ข้อเก่า **หายหรือดีขึ้นราว 50–80%** แล้วย้ายไปข้อใหม่ → **rheumatic fever** (DGI ระยะแรก)
- **Additive** — ข้อใหม่เพิ่มขณะข้อเก่ายังปวด → **RA**
- **Intermittent** — กำเริบแล้ว **หายสนิทแตะ baseline** → **crystal ทั้งกลุ่ม** (gout, CPPD, BCP) และ **palindromic rheumatism** (✍️ "ต่อ → RA, LE") · ต่างจาก chronic ที่มาก–น้อยสลับแต่ไม่แตะ baseline

[[anim:art-pattern]]

### D — Distribution
- **Symmetry** = เป็นสองข้างความรุนแรงใกล้เคียงกัน (✍️ "degree ใกล้เคียง ไม่เป๊ะ") — มือข้างถนัดเป็นมากกว่าได้ ยังเรียก symmetrical polyarthritis
- **Peripheral vs axial** — axial joint = **spine · SI joint · sternocostal · sternoclavicular · TMJ** (อาจารย์: "anatomy ต้องมา")
- **RA เป็นโรคของข้อส่วนปลาย แต่แอบมี axial ที่เดียวคือ C1–C2** (atlantoaxial subluxation) · ✍️ **RA ที่ปวดหลังส่วนล่าง ไม่ใช่ RA active → คิด osteoporosis/osteoporotic fracture** (RA + steroid ทำให้กระดูกพรุน)
- **Spondylosis = OA ของกระดูกสันหลัง** เกิดที่ **C-spine และ L-spine** (T-spine แทบไม่มี) เป็น non-inflammatory · ต่างจาก **spondylitis** (SpA) ที่อักเสบ
- **ข้อนิ้ว** — **PIP + DIP โดยไม่มี MCP → OA · PIP + MCP โดยไม่มี DIP → RA** (สไลด์ p8 · หัวข้อถัดไป)

### E — สิ่งที่อยู่นอกข้อ
สไลด์ p8 ให้ถามหา **enthesitis · dactylitis · tendinitis · sacroiliitis** (✍️ เขียน "SNSA" ไว้ที่ enthesis ในภาพ p4) และอาการระบบอื่น: สะเก็ดเงินและเล็บ · ตาแดง (uveitis, scleritis) · ท้องเสียเรื้อรัง (IBD) · ปากแห้งตาแห้ง · nodule · ผื่นแพ้แสง แผลในปาก โปรตีนในปัสสาวะ (SLE) · ปัสสาวะแสบ/ท้องเสียนำมาก่อน (ReA)

> **ราวด์ 5 พ.ย. · ข้อเดียวอักเสบเฉียบพลัน** — "เห็นโจทย์ **acute monoarthritis สิ่งแรกที่ต้องทำคือเจาะข้อ ไม่ใช่แค่ให้ NSAID**" เพราะต้องแยกโรคที่ violent และตายได้คือ **septic arthritis** ("เก๊าไปแล้วตายไหม — ไม่ตาย")
""",
    ["I-I-N-O-D-E: Intra/extra → Inflammatory? → Number → Onset/pattern → Distribution → Extra-articular",
     "ในข้อ = เจ็บทั้ง active และ passive ทุกทิศ · นอกข้อ = active บางทิศ กดเจ็บจุดเดียว",
     "บวมหยุ่น (synovial hypertrophy) = สัญญาณอักเสบที่เชื่อถือได้ที่สุด · tenderness และน้ำในข้ออย่างเดียวแยกไม่ได้",
     "Morning stiffness ต้องบอกเป็นนาที: อักเสบ > 30 · OA 2–5 นาที",
     "Intermittent = หายสนิทแตะ baseline → crystal · migratory → rheumatic fever · additive → RA",
     "RA ปวดหลังส่วนล่าง → คิดกระดูกพรุนหัก ไม่ใช่ RA active (RA axial มีแค่ C1–C2)"],
    [mcq(P + "MCQ-01",
         "A 48-year-old woman has right shoulder pain for 3 weeks after painting her house. Pain occurs when she actively lifts her arm sideways between 60° and 120°. When the examiner abducts the relaxed arm passively, the full range is painless. There is point tenderness just below the acromion, no effusion and no warmth. What is the most likely source of pain?",
         "Supraspinatus (rotator cuff) tendinopathy — an extra-articular lesion",
         ["Septic arthritis of the glenohumeral joint", "Adhesive capsulitis of the shoulder", "Calcium pyrophosphate arthritis of the glenohumeral joint", "Rheumatoid synovitis of the shoulder"], 2,
         "**เจ็บเฉพาะ active ในบางทิศ (painful arc) + passive เต็มช่วงไม่เจ็บ + กดเจ็บจุดเดียว = extra-articular** → เอ็น supraspinatus ที่อักเสบต้องหดตัวตอนยกแขนเอง แต่ตอนหมอยกให้เอ็นได้พัก\n\n"
         "- **septic / CPPD / RA ของข้อไหล่** เป็น intra-articular → **เจ็บทั้ง active และ passive ทุกทิศ** มักมีบวมร้อน\n"
         "- **adhesive capsulitis** เป็นปัญหาของ capsule → **ROM จำกัดทั้ง active และ passive** (โดยเฉพาะ external rotation) ไม่ใช่ passive ปกติ\n\n"
         "จุดนี้สำคัญก่อนเจาะข้อ — ถ้ารอยโรคอยู่นอกข้อ ไม่มีเหตุให้แทงเข็มเข้าข้อ",
         "Active เจ็บ passive ไม่เจ็บ + กดเจ็บจุดเดียว = นอกข้อ", "Intra vs extra-articular", REF("Joint pain tree p5 · Sources of pain p4"), NL_APP),
     mcq(P + "MCQ-02",
         "On examination of a swollen joint, which finding is the most reliable sign that the process is inflammatory synovitis rather than a non-inflammatory problem?",
         "Soft, boggy (rubbery) thickening of the synovium around the joint",
         ["Tenderness on pressure over the joint line", "A large knee effusion with a positive patellar tap after a twisting injury", "Coarse crepitus on movement", "Hard bony enlargement at the joint margins"], 4,
         "สไลด์ p6: **synovial hypertrophy = most reliable sign** ของข้ออักเสบ — คลำได้เนื้อหยุ่น ๆ เป็นก้อนรอบข้อ (rubbery/lumpy) จาก synovium ที่แบ่งตัวหนาขึ้น\n\n"
         "- **tenderness** แยกไม่ได้ — อาจารย์: กระดูกหักหรือเข่าพลิกก็เจ็บ\n"
         "- **effusion อย่างเดียว** แยกไม่ได้ (✍️ \"น้ำอย่างเดียวแยกไม่ได้\") — หลังบาดเจ็บอาจเป็นเลือดในข้อ\n"
         "- **crepitus หยาบ** และ **bony enlargement** เป็นลักษณะของ OA (non-inflammatory)",
         "Synovial hypertrophy (บวมหยุ่น) = สัญญาณอักเสบที่เชื่อถือได้ที่สุด", "Inflammatory signs", REF("Signs of inflammatory joint diseases p6"), NL_APP),
     mcq(P + "MCQ-03",
         "A 29-year-old woman with regular menstrual cycles reports episodes of sudden pain and swelling in one joint at a time — a wrist, then weeks later a knee, then an MCP joint. Each episode lasts 1–2 days and resolves completely, with no symptoms between attacks. Examination today is normal. Which interpretation is most appropriate?",
         "Intermittent arthritis suggesting palindromic rheumatism; check anti-CCP because it may evolve into rheumatoid arthritis",
         ["Recurrent acute gout; start allopurinol", "Migratory arthritis of acute rheumatic fever", "Additive polyarthritis of early rheumatoid arthritis", "Osteoarthritis flares; no further testing needed"], 1,
         "**กำเริบแล้วหายสนิทแตะ baseline = intermittent** → กลุ่ม crystal และ **palindromic rheumatism** (✍️ \"ต่อ → RA, LE\") · ผู้ป่วยส่วนหนึ่งกลายเป็น RA โดยเฉพาะเมื่อ anti-CCP บวก\n\n"
         "- **เกาต์**: อาจารย์ย้ำ \"**ผู้หญิงยังมีประจำเดือน เขียนเกาต์จะโดนหักคะแนน**\" — estrogen ช่วยขับ urate ทางปัสสาวะ\n"
         "- **migratory** = ข้อเก่าดีขึ้นแล้ว **ย้าย** ไปข้อใหม่ภายในไม่กี่วัน (ต่อเนื่อง ไม่ใช่ห่างกันเป็นสัปดาห์และหายสนิท)\n"
         "- **additive** = ข้อเก่ายังปวดอยู่ขณะข้อใหม่เพิ่ม\n"
         "- OA ไม่ได้มาเป็นข้ออักเสบเฉียบพลันที่หายสนิท",
         "Intermittent (หายสนิท) → crystal หรือ palindromic · ผู้หญิงก่อนหมดประจำเดือนไม่เขียนเกาต์", "Temporal pattern", REF("Historical features for DDx p9") + REFR("intermittent vs chronic · เกาต์ในผู้หญิง"), NL_APP)])

# ═════════════════════════════════════════════════════════════════ หัวข้อใหม่ 2 · แผนที่ DDx
NEW["air-23-art-02"] = sec(
    "air-23-art-02", "รูปแบบข้อบอกโรค — ต้นไม้ DDx ของสไลด์ และ RA vs OA vs SpA vs crystal vs septic",
    "ต้นไม้ inflammatory × จำนวนข้อ × เวลา (สไลด์ p11) · ตารางเทียบโรคหลักทีละมิติ · อายุ/เพศช่วยตัดโรค · RA เว้น DIP · OA เว้น MCP",
    10, NL_APP + ["2.3.13-3(12)", "2.3.13(5)"],
    """
### ต้นไม้ DDx ของ อ.กิตติวรรณ (สไลด์ p11)
| | Mono/oligo — acute | Mono/oligo — chronic | Poly — acute | Poly — chronic |
|---|---|---|---|---|
| **Inflammatory** | **septic** · **crystal** · systemic RD | infection (TB เชื้อรา) · **CPPD** · JIA · systemic RD | rheumatic fever · **GC** · viral · bacterial endocarditis (สไลด์เขียน "BE") · early RA · Still's · SNSA | **RA · SLE · SNSA** · Behçet |
| **Non-inflammatory** | trauma · fracture · **hemarthrosis** · AVN | **OA** · AVN · osteomyelitis · tumor | — | **OA** · hemochromatosis · ochronosis · HOA · amyloidosis · acromegaly |

สไลด์เคสกลุ่ม 19B/20B แตกย่อยเพิ่ม: acute oligo แบ่งตาม pattern (**migratory** = rheumatic fever · **additive** = GC, reactive, early RA · **intermittent** = crystal, reactive, palindromic) · chronic mono = TB เชื้อรา crystal · chronic oligo = SpA RA crystal · **chronic poly = RA SpA SLE crystal**

**ใช้จริงกับเคสหญิง 34 ปี (สไลด์เคส)** — ปวดในข้อ (เจ็บทั้ง active และ passive) · อักเสบ (ร้อน บวม ฝืดเช้า ~1 ชั่วโมง น้ำหนักลด) · **> 4 ข้อ** · **> 6 สัปดาห์** · สมมาตร ข้อเล็ก + เข่า → RA · SLE · SpA · crystal → ตัด **SpA** (ไม่มีปวดหลังอักเสบ ไม่ asymmetric) → เหลือ **RA · SLE · crystal** แล้วจึงส่งแล็บเฉพาะ

### เทียบโรคหลักทีละมิติ
| | RA | OA | SpA | Gout | CPPD | Septic | SLE |
|---|---|---|---|---|---|---|---|
| อายุ/เพศ | หญิง 2–3:1 · **40–50 ปี** (อาจารย์) | สูงอายุ | ชาย < 45 ปี | ชายหลังวัยรุ่น · **หญิงหลังหมดประจำเดือน** | **> 60 ปี** (อาจารย์: 70–80) | ทุกวัย สูงอายุ/ข้อเดิมผิดปกติ | หญิง 15–45 ปี |
| Onset | insidious | insidious | insidious | **abrupt** (กลางดึก) | abrupt | **rapid 1–2 วัน** | insidious |
| Pattern | **additive** chronic | chronic | chronic | **intermittent** | intermittent | ไม่หายเอง | chronic/ขึ้นลง |
| จำนวน | poly | oligo–poly | mono/oligo (PsA poly ได้) | mono | mono | mono (10% poly) | poly |
| ข้อเด่น | **MCP PIP wrist MTP · เว้น DIP** · C1–C2 | **DIP PIP CMC1 · เข่า สะโพก · เว้น MCP** | SI · spine · ข้อใหญ่ขา ไม่สมมาตร | **MTP1** ข้อเท้า เข่า | **เข่า ข้อมือ** | **เข่า 55%** | MCP PIP wrist เข่า |
| ฝืดเช้า | **> 1 ชม.** | < 5 นาที | > 30 นาที (หลัง) | — | — | — | มี |
| นอกข้อ | nodule · sicca · ILD · vasculitis | — | enthesitis · dactylitis · uveitis · psoriasis · IBD | tophi · นิ่ว | chondrocalcinosis | ไข้ แหล่งติดเชื้อ | ผื่น แผลปาก **ไต** เม็ดเลือด |
| ตรวจหลัก | **anti-CCP** RF · X-ray erosion | X-ray (LOSS) | HLA-B27 · ภาพ SI | **ผลึกเข็ม negative** | **rhomboid positive** | **Gram/culture** WBC > 50,000 | **ANA** dsDNA C3/C4 |

[[anim:art-handmap]]

#### ทำไมถึงมีอาการนี้
| ลักษณะ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **RA เว้น DIP** | RA เป็นโรคของ **synovium** — MCP PIP wrist มีเยื่อบุข้อมากและเป็นเป้าของ immune response · DIP มี synovium น้อย | DIP เด่น → OA หรือ PsA |
| **OA เว้น MCP** | OA เป็นโรคของ **กระดูกอ่อนที่รับแรงซ้ำ** — DIP PIP ฐานนิ้วโป้ง รับแรงหยิบจับมากกว่า MCP | OA-like ที่ MCP 2–3 → นึกถึง **hemochromatosis/CPPD** (สไลด์ p11) |
| **PsA จับ DIP + เล็บ** | DIP อยู่ติด nail bed — enthesis ของ extensor tendon ต่อกับเล็บ → enthesitis ลามถึงเล็บ (pitting, onycholysis) | นิ้วบวมทั้งนิ้ว + เล็บผิดปกติ = PsA |
| **เกาต์ชอบ MTP1 · CPPD ชอบเข่า** | urate ละลายน้อยลงในข้อส่วนปลายที่อุณหภูมิต่ำ · CPP เกาะในกระดูกอ่อนชนิด fibrocartilage/hyaline ของเข่า ข้อมือ (TFCC) | ข้อเท้า/MTP1 → เกาต์ · เข่า/ข้อมือคนแก่ → CPPD |
| **Pseudogout แก่กว่าเกาต์** | การสะสม CPP เพิ่มตามอายุของกระดูกอ่อน · เกาต์ในชายเริ่มได้ตั้งแต่ urate สูงหลังวัยรุ่น หญิงมี estrogen ช่วยขับ urate จนหมดประจำเดือน | ✍️ "Pseudogout ⇒ แก่กว่า" |

> **ราวด์ 5 พ.ย. · อายุและเพศ** — อาจารย์ถามทั้งห้องว่าใครแก่กว่า: **pseudogout 70–80 ปี** · เกาต์ในผู้ชายเป็นได้ตั้งแต่ **post-puberty** · **ผู้หญิงยังมีประจำเดือน + acute monoarthritis → ห้ามเขียนเกาต์ใน DDx** ("key point ทั้งนั้นเลย") · RA ที่กลุ่มเขียนอายุ 55–75 "แก่ไป" → **40–50 ปี แก่กว่า SLE นิดหนึ่ง**
""",
    ["ต้นไม้ของสไลด์: inflammatory? → mono/oligo หรือ poly → acute หรือ chronic",
     "Chronic symmetric polyarthritis = RA · SLE · SpA · crystal (เคสกลุ่ม 19B/20B)",
     "RA เว้น DIP · OA เว้น MCP · PsA เอา DIP + เล็บ",
     "Pseudogout แก่กว่าเกาต์ (70–80 ปี) · ผู้หญิงก่อนหมดประจำเดือนไม่เป็นเกาต์",
     "Septic arthritis: rapid 1–2 วัน ไม่หายเอง · crystal: abrupt หายเองเป็นพัก ๆ"],
    [mcq(P + "MCQ-04",
         "A 58-year-old woman has had seropositive rheumatoid arthritis for 12 years and has taken prednisolone 7.5 mg daily for 6 years. Her hand and knee joints are currently quiet and ESR is normal. She develops sudden severe midline low back pain after lifting a bucket of water. There is no fever. What is the most likely cause of her back pain?",
         "Osteoporotic vertebral compression fracture",
         ["Rheumatoid involvement of the lumbar facet joints", "Atlantoaxial subluxation", "Ankylosing spondylitis developing on top of rheumatoid arthritis", "Rheumatoid nodule compressing the cauda equina"], 0,
         "✍️ สไลด์ p8: **\"RA ⇒ ปวด lower back ⇒ osteoporosis\"** · อาจารย์: RA เป็นโรคของข้อส่วนปลาย **axial มีที่เดียวคือ C1–C2** — ถ้าโจทย์ให้ RA แล้วปวดหลังส่วนล่าง **ไม่ใช่ RA active แต่เป็นภาวะแทรกซ้อน**\n\n"
         "RA ทำให้กระดูกพรุนจากการอักเสบเรื้อรัง (cytokine กระตุ้น osteoclast) + การไม่ค่อยขยับ + **steroid ≥ 7.5 mg นาน** → หักจากแรงยกของเล็กน้อย\n\n"
         "- **lumbar facet** ไม่ใช่เป้าของ RA (สไลด์ p63: spared spine except C-spine)\n"
         "- **atlantoaxial subluxation** อยู่ที่คอ อาการปวดท้ายทอย/อาการทางไขสันหลังส่วนคอ\n"
         "- AS เป็นโรคคนละกลุ่ม เริ่มก่อน 45 ปี ปวดแบบค่อยเป็น ไม่ใช่ปวดทันทีหลังยกของ",
         "RA ปวดหลังส่วนล่าง = กระดูกพรุนหัก (RA axial มีแค่ C1–C2)", "RA distribution", REF("Historical features p8 ✍️") + REFR("RA axial C1–C2"), NL_RA + ["2.3.13(6)"]),
     mcq(P + "MCQ-05",
         "A 16-year-old boy has fever and joint pain for 6 days. His right knee was hot and swollen for 2 days and improved as the left ankle became swollen; that ankle then settled as the right wrist became inflamed. He had a sore throat 3 weeks ago and a new apical pansystolic murmur. Which pattern and diagnosis fit best?",
         "Migratory polyarthritis — acute rheumatic fever",
         ["Additive polyarthritis — juvenile rheumatoid arthritis", "Intermittent monoarthritis — gout", "Chronic oligoarthritis — ankylosing spondylitis", "Acute monoarthritis — septic arthritis"], 3,
         "ข้อเก่า **ดีขึ้นขณะข้อใหม่เริ่มปวด** (อาจารย์: ดีขึ้นราว 50–80% แล้วย้าย) = **migratory** → คลาสสิกคือ **acute rheumatic fever** (Jones: polyarthritis + carditis หลังคออักเสบ GAS 2–4 สัปดาห์)\n\n"
         "- **additive** = ข้อเก่ายังปวดอยู่ (RA)\n"
         "- **intermittent** = หายสนิทแตะ baseline ห่างกันเป็นสัปดาห์–เดือน (crystal)\n"
         "- AS = chronic > 6 สัปดาห์ ปวดหลัง · septic = ข้อเดียวที่แย่ลงเรื่อย ๆ ไม่ย้าย",
         "ข้อเก่าดีขึ้นแล้วย้าย = migratory → rheumatic fever", "Temporal pattern", REF("Arthritis tree p11 · temporal patterns p9") + REFR("migratory 50–80%"), NL_APP)])


# ═════════════════════════════════════════════════════════════════ หัวข้อใหม่ 3 · เจาะไม่ได้ — prediction rule + imaging
NEW["air-23-art-03"] = sec(
    "air-23-art-03", "เจาะข้อไม่ได้ — clinical prediction rule ของเกาต์ และภาพรังสี อัลตราซาวนด์ DECT",
    "Gold standard ยังคือเจาะข้อ · คะแนน Janssens 7 ตัวแปร (กลุ่มนำเสนอให้แค่ 6 — ขาด male sex) · erosion ขอบยื่นมาช้า · double contour บนผิวกระดูกอ่อน vs CPPD กลางเนื้อกระดูกอ่อน",
    9, NL_GOUT + ["B5.3(1)", "B5.3(4)", "3.2.5"],
    """
### Gold standard ยังคือเจาะข้อ (สไลด์ p39)
- **ผลึกรูปเข็มในน้ำไขข้อ และ/หรือในเซลล์ PMN**
- น้ำไขข้อ PMN สูง แต่ **ส่วนใหญ่ไม่เกิน 80,000** · CBC leukocytosis PMN เด่น · **ESR ขึ้นแต่ส่วนใหญ่ไม่เกิน 80 mm/hr**
- **Serum urate ใช้วินิจฉัยไม่ได้** — ปกติได้ถึง **49% ขณะกำเริบ** (สไลด์ให้เหตุผลว่า IL-6 เพิ่มการขับทางไต) · วัดซ้ำหลังหายราว 2 สัปดาห์
- เกณฑ์ ACR 1977 (Wallace — สไลด์ p41): ผลึกในน้ำไขข้อ **หรือ** tophus ที่พิสูจน์ผลึก **หรือ** ≥ 6 ใน 12 ข้อทางคลินิก/แล็บ/รังสี

### Clinical prediction rule — เมื่อเจาะข้อไม่ได้ (Janssens, Arch Intern Med 2010)
กลุ่ม 6ก/6ข นำเสนอว่ามี **7 ตัวแปร แต่แจกแจงแค่ 6** — ตัวที่ขาดคือ **เพศชาย 2 คะแนน** (เติมตามต้นฉบับ)

| ตัวแปร | คะแนน |
|---|---|
| **เพศชาย** (กลุ่มไม่ได้ใส่) | **2** |
| เคยมีข้ออักเสบลักษณะเดียวกันมาก่อน | **2** |
| อาการถึงขีดสุดภายใน 1 วัน | **0.5** |
| ข้อแดง | **1** |
| **MTP ที่ 1** | **2.5** |
| ความดันโลหิตสูง หรือโรคหัวใจหลอดเลือด ≥ 1 โรค | **1.5** |
| **Serum urate > 5.88 mg/dL** (กลุ่มปัดเป็น 5.8) | **3.5** |
| รวมสูงสุด | **13** |

| คะแนน | โอกาสเป็นเกาต์ (ต้นฉบับ) | ทำอะไร |
|---|---|---|
| **≤ 4** | ~2% | หาสาเหตุอื่น |
| **> 4 ถึง < 8** | ~31% | **เจาะข้อดูผลึก** |
| **≥ 8** | ~80% | วินิจฉัยเกาต์ทางคลินิกได้ |

**เคสชาย 60 ปี (ราวด์)** — ชาย 2 · เคยปวดเข่าขวาปีก่อน 2 · ถ้าปวดถึงสุดในวันแรก 0.5 · แดง 1 · ข้อเท้า (ไม่ใช่ MTP1) 0 · ความดันสูง 1.5 · urate 9.5 → 3.5 = **10.5 → high** — แต่ **มีไข้ 38.5 °C + WBC สูง ต้องเจาะข้อเพื่อตัด septic อยู่ดี** · rule นี้สร้างในผู้ป่วยเวชปฏิบัติทั่วไปข้อเดียว **ไม่ได้ออกแบบมาตัดการติดเชื้อ**

### ภาพรังสี
- **X-ray** — ช่วงแรกเห็นแค่ soft tissue swelling · **erosion มักเห็นหลัง attack แรก 6–12 ปี** (กลุ่มนำเสนอ) · ลักษณะเฉพาะ: **punched-out erosion ขอบแข็ง (sclerotic rim) + overhanging edge** · **joint space คงอยู่จนท้าย ๆ** · ข้อจำกัด: วินิจฉัยช้า ใช้ใน acute gout ไม่ได้ (สไลด์ p38, p42)

[[img:art-gout-xray]]

- **Ultrasound** — **double contour sign** = urate เกาะเป็นเส้นสว่างบน **ผิว** กระดูกอ่อน ขนานกับเส้น subchondral bone · tophus เป็นก้อนเงาไม่สม่ำเสมอ · **CPPD เห็นจุด/เส้นสว่าง "กลางเนื้อ" กระดูกอ่อน** (กลุ่มนำเสนอ) · ข้อจำกัดตามสไลด์ p43: ไม่สัมพันธ์กับอาการ · ผิดปกติใน 25% ของคนไม่มีอาการ

[[img:art-gout-us]]

> **สไลด์ vs ปัจจุบัน** — สไลด์ p43 เขียนว่า US "cannot be use for DDx CPPD" แต่การนำเสนอและเกณฑ์ ACR/EULAR 2023 ของ CPPD ใช้ **ตำแหน่ง** ของผลึก (ผิว vs กลางกระดูกอ่อน) ช่วยแยกได้ระดับหนึ่ง — ยืนยันด้วยการเจาะข้อเมื่อทำได้

- **DECT** (dual-energy CT 80 และ 140 kV) — ระบายสี urate ได้ sensitivity/specificity สูง · ข้อจำกัด: ศึกษาในคนที่วินิจฉัยแล้ว · **gout ครั้งแรก yield เพียง ~50%** (สไลด์ p44)

#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Double contour** | MSU ตกผลึกบนผิวกระดูกอ่อน hyaline → สะท้อนเสียงเป็นเส้นสว่างเส้นที่สองเหนือ subchondral bone | CPPD เกาะ **ในเนื้อ** กระดูกอ่อน |
| **Overhanging edge** | tophus ค่อย ๆ กดกร่อนกระดูกจากข้างนอก ขณะที่กระดูกรอบ ๆ สร้างใหม่ยื่นออกมาคลุมก้อน (ทั้ง destructive และ hypertrophic — สไลด์ p38) | RA erosion อยู่ขอบข้อ (bare area) + กระดูกบาง ไม่มีขอบยื่น |
| **Joint space คงอยู่นาน** | tophus กัดกระดูกเฉพาะจุด กระดูกอ่อนส่วนใหญ่ยังอยู่ | RA และ OA ช่องข้อแคบเร็วกว่า |
| **Serum urate ปกติขณะกำเริบ** | การอักเสบเพิ่มการขับ urate (IL-6) + urate ส่วนหนึ่งถูกดึงไปเป็นผลึก | ห้ามใช้ตัดเกาต์ |
""",
    ["Gold standard ของเกาต์ = ผลึกเข็มในน้ำไขข้อ · urate ปกติได้ 49% ขณะกำเริบ",
     "Janssens rule: ชาย 2 · เคยเป็น 2 · ถึงสุดใน 1 วัน 0.5 · แดง 1 · MTP1 2.5 · HT/CVD 1.5 · urate > 5.88 3.5",
     "≤ 4 หาสาเหตุอื่น · > 4–< 8 เจาะข้อ · ≥ 8 เกาต์ — แต่มีไข้ต้องเจาะตัด septic เสมอ",
     "X-ray: punched-out + overhanging edge มาช้า (6–12 ปี) · joint space คงอยู่นาน",
     "US: double contour บนผิวกระดูกอ่อน = MSU · จุดกลางเนื้อกระดูกอ่อน = CPPD"],
    [mcq_fixed(P + "MCQ-06",
               "A 58-year-old man cannot undergo arthrocentesis at a community hospital. He has a red, swollen left ankle; the pain reached its maximum within 12 hours. He had a similar attack in the big toe 1 year ago, has treated hypertension, and serum urate is 7.2 mg/dL. He is afebrile. Using the Janssens clinical prediction rule for gout, what is his score?",
               ["4.0", "7.0", "8.5", "10.5", "13.0"], 3,
               "**ชาย 2 + เคยเป็น 2 + ถึงสุดใน 1 วัน 0.5 + ข้อแดง 1 + MTP1 0 (ครั้งนี้เป็นข้อเท้า) + ความดันสูง 1.5 + urate > 5.88 → 3.5 = 10.5** → **≥ 8 = high probability (~80%)**\n\n"
               "- **8.5** = ใช้รายการ 6 ข้อของกลุ่มนำเสนอซึ่ง **ลืมเพศชาย 2 คะแนน** (ยังได้ ≥ 8 แต่คะแนนผิด)\n"
               "- **13.0** = ให้ MTP1 ทั้งที่ข้อที่อักเสบ **ครั้งนี้** คือข้อเท้า\n"
               "- 7.0 / 4.0 = ลืมหลายตัวแปร\n\n"
               "ระวัง: rule นี้ไม่ได้ใช้ตัด septic arthritis — ถ้ามีไข้หรือดูป่วย ต้องเจาะข้อ",
               "Janssens: ชาย 2 · เคยเป็น 2 · < 1 วัน 0.5 · แดง 1 · MTP1 2.5 · HT 1.5 · urate 3.5", "Gout prediction rule",
               REFR("clinical prediction rule ของกลุ่ม 6ก/6ข (เติม male sex ตาม Janssens 2010)"), NL_GOUT),
     mcq(P + "MCQ-07",
         "Ultrasound of the first metatarsophalangeal joint shows an irregular hyperechoic band lying on the surface of the articular cartilage, running parallel to the bright subchondral bone line. What does this finding indicate?",
         "Monosodium urate deposition (double contour sign of gout)",
         ["Calcium pyrophosphate deposition within the cartilage", "Osteophyte formation of osteoarthritis", "Marginal erosion of rheumatoid arthritis", "Normal hyaline cartilage"], 0,
         "**Double contour sign** = MSU เกาะบน **ผิว** กระดูกอ่อน → เห็นเส้นสว่างสองเส้นขนานกัน (ผิวกระดูกอ่อน + subchondral bone) — กลุ่มนำเสนออธิบายด้วยภาพ US ในราวด์\n\n"
         "- **CPPD** = จุด/เส้นสว่าง **กลางเนื้อ** กระดูกอ่อน (chondrocalcinosis บน US)\n"
         "- osteophyte = ปุ่มกระดูกยื่นที่ขอบข้อ ไม่ใช่เส้นบนผิวกระดูกอ่อน\n"
         "- RA erosion = รอยเว้าของ cortex ที่ขอบข้อ\n"
         "- กระดูกอ่อนปกติเป็นแถบมืด (anechoic) เรียบ",
         "Double contour (บนผิวกระดูกอ่อน) = urate · กลางเนื้อกระดูกอ่อน = CPPD", "Gout imaging", REF("Other diagnostic tools — ultrasound p43") + REFR("double contour vs CPPD"), NL_GOUT + ["3.2.5"])],
    imgs={
        "art-gout-xray": img("art-04-gout-xray", "เกาต์เรื้อรังบนภาพรังสี — erosion ขอบยื่น (overhanging edge)",
                             "ภาพรังสีมือซ้ายมีก้อนเงาเนื้อเยื่ออ่อนที่ข้อนิ้ว ลูกศรแดงสองอันชี้รอยกร่อนกระดูกที่มีขอบยื่น และภาพรังสีข้อเท้ามีวงแดงล้อมรอยกร่อน",
                             cap="ลูกศรแดง: **punched-out erosion + overhanging edge** ข้างก้อน tophus · วงแดง: erosion ขอบแข็งที่ข้อเท้า · สไลด์: gouty erosion เป็น **ทั้ง destructive และ hypertrophic** และ **joint space มักคงอยู่จนท้าย ๆ**"),
        "art-gout-us": img("art-05-gout-us", "อัลตราซาวนด์ในเกาต์ — double contour และ tophus",
                           "ภาพอัลตราซาวนด์หกช่อง A ถึง F ช่อง A และ B มีลูกศรชี้เส้นสว่างบนผิวกระดูกอ่อน ช่อง C และ D มีลูกศรประชี้ก้อน ช่อง E และ F มีหัวลูกศรชี้แถบในเอ็น",
                           cap="**A–B: double contour** — เส้นสว่างบนผิวกระดูกอ่อนขนานกับ subchondral bone (mth = metatarsal head · f = femur) · **C–D: tophus/aggregate** (ลูกศรประ) · **E–F: urate ในเอ็น** (หัวลูกศร) · ข้อจำกัดตามสไลด์: ผิดปกติได้ใน 25% ของคนไม่มีอาการ")})

# ═════════════════════════════════════════════════════════════════ หัวข้อใหม่ 4 · ผลึก 6 ชนิด
NEW["air-23-art-04"] = sec(
    "air-23-art-04", "ผลึก 6 ชนิดในน้ำไขข้อ — รูปร่าง การหักเหแสง และความหมาย",
    "MSU · CPPD · cholesterol · corticosteroid · calcium oxalate · BCP — ขนานเหลือง = MSU · ABC = Aligned Blue Calcium · เจอผลึกยังตัดติดเชื้อไม่ได้",
    8, NL_GOUT + NL_SF,
    """
ราวด์ 5 พ.ย. กลุ่ม 6ก/6ข เทียบผลึกที่พบในน้ำไขข้อ 6 ชนิด โดยดู **รูปร่าง · birefringence · ความหมายทางคลินิก** — อาจารย์ย้ำว่า **ผลึกเกาต์รูปเข็มเห็นด้วย light microscope ธรรมดาได้** ถ้าโจทย์ไม่มี polarized microscope

| ผลึก | รูปร่าง | Birefringence (ขนานแกน compensator) | พบเมื่อ |
|---|---|---|---|
| **Monosodium urate (MSU)** | **เข็มยาวปลายแหลม** มักอยู่ใน PMN ช่วงกำเริบ | **negative แรง · เหลือง** (ตั้งฉาก = ฟ้า) | **เกาต์** |
| **Calcium pyrophosphate (CPP)** | **rhomboid หรือแท่งสั้น** | **positive อ่อน · ฟ้า** (ตั้งฉาก = เหลือง) · หลายผลึกแทบไม่เรือง | **CPPD / pseudogout** |
| **Cholesterol** | **แผ่นสี่เหลี่ยมใหญ่ มีมุมบาก (notched plate)** | เรืองแสง | **effusion เรื้อรัง** — RA, OA ที่บวมนาน (ไม่ใช่สาเหตุของการอักเสบเฉียบพลัน) |
| **Corticosteroid** | **แผ่นแบน รูปร่างหลากหลาย ไม่สม่ำเสมอ** | เรืองแสงทั้งสองแบบ | **หลังฉีด steroid เข้าข้อ** (อยู่ได้หลายสัปดาห์ ทำให้ข้ออักเสบชั่วคราวได้) |
| **Calcium oxalate** | **ทรงซองจดหมาย (envelope/bipyramidal)** หรือแท่ง | เรืองแสง (ส่วนใหญ่ positive) | **CKD ที่ฟอกไต** · primary oxalosis |
| **Basic calcium phosphate (apatite)** | **ก้อนเล็กมาก** เกาะเป็นกระจุก | **ไม่ birefringent** · ต้องย้อม **alizarin red** หรือ EM | OA · Milwaukee shoulder · **calcific tendinitis** |

[[anim:art-biref]]

[[img:art-msu-micro]]

[[img:art-crystals]]

#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **สีกลับกันระหว่าง MSU กับ CPP** | ผลึกมีดัชนีหักเหต่างกันตามแนวแกน — แสงที่สั่นขนานแกนยาวของ MSU เดิน "เร็ว" กว่าแนวตั้งฉาก (negative) ส่วน CPP กลับกัน (positive) เมื่อซ้อนกับ red plate จึงได้สีตรงข้าม | จำ MSU \"ขนานเหลือง\" อันเดียว แล้ว CPP กลับทุกอย่าง |
| **MSU เรืองสว่าง CPP เรืองจาง** | MSU birefringence แรง · CPP อ่อน และผลึกเล็ก | ไม่เห็นผลึกใน polarized ไม่ได้ตัด CPPD |
| **ผลึกอยู่ใน PMN** | neutrophil กลืนผลึกขณะอักเสบ | ช่วงสงบ (intercritical) อาจเจอผลึกนอกเซลล์ได้ (สไลด์ p35) |
| **BCP มองไม่เห็นใน polarized** | ผลึก apatite เล็กระดับนาโน ไม่หักเหแสงพอ | ข้ออักเสบที่ \"ไม่มีผลึก\" ในผู้สูงอายุ/ไหล่ → นึกถึง BCP |
| **Steroid crystal หลังฉีด** | ยาฉีดชนิด suspension ตกค้างเป็นผลึก | ประวัติฉีดข้อ → อย่าวินิจฉัยเกาต์/CPPD ผิด |

> **ราวด์ 5 พ.ย. · ผลึกไม่ได้ตัดการติดเชื้อ** — **crystal และ septic อยู่ข้อเดียวกันครั้งเดียวกันได้** · เคยเป็น intermittent arthritis มาก่อน ครั้งนี้เข่าบวม WBC 80,000 → **ให้ยาปฏิชีวนะแม้เจอผลึก** และห้ามฉีด steroid เข้าข้อจนกว่าผลเพาะเชื้อออก
""",
    ["MSU: เข็ม · negative แรง · ขนานเหลือง",
     "CPP: rhomboid · positive อ่อน · ขนานฟ้า (ABC = Aligned Blue Calcium)",
     "Cholesterol = notched plate ใน effusion เรื้อรัง · steroid crystal = หลังฉีดข้อ",
     "Calcium oxalate = ซองจดหมาย ในผู้ฟอกไต · BCP ไม่ birefringent ต้องย้อม alizarin red",
     "เจอผลึกแล้วยังต้องดู Gram stain/culture — crystal + septic อยู่ข้อเดียวกันได้"],
    [mcq(P + "MCQ-08",
         "A 70-year-old woman with knee osteoarthritis received an intra-articular injection 10 days ago. The knee is now mildly warm with an effusion. Aspirate shows 3,500 WBC/µL and flat, irregular plate-like birefringent crystals of variable shapes; Gram stain is negative. She has never had gout. What is the most likely explanation for the crystals?",
         "Corticosteroid crystals from the recent intra-articular steroid injection",
         ["Monosodium urate crystals of a first gout attack", "Calcium oxalate crystals from chronic kidney disease", "Basic calcium phosphate crystals of Milwaukee shoulder", "Cholesterol crystals from rheumatoid arthritis"], 1,
         "ผลึก **แผ่นแบน รูปร่างหลากหลาย** + ประวัติ **ฉีดยาเข้าข้อ** = **corticosteroid crystal** (ตารางของกลุ่ม 6ก/6ข) — ยา suspension ตกค้างได้หลายสัปดาห์และทำให้อักเสบชั่วคราว (post-injection flare)\n\n"
         "- MSU = **เข็ม** negative แรง\n"
         "- calcium oxalate = **ซองจดหมาย** ในผู้ฟอกไต\n"
         "- BCP **ไม่ birefringent** มองไม่เห็นใน polarized\n"
         "- cholesterol = แผ่นสี่เหลี่ยมมุมบาก ใน effusion เรื้อรัง ผู้ป่วยไม่มี RA\n\n"
         "ยังต้องรอผล culture เพราะการฉีดข้อเป็นปัจจัยเสี่ยงของ septic arthritis",
         "ผลึกแผ่นแบนรูปร่างหลากหลายหลังฉีดข้อ = steroid crystal", "Synovial crystals", REFR("ตารางผลึก 6 ชนิดของกลุ่ม 6ก/6ข"), NL_SF + ["2.3.13(5)"]),
     mcq(P + "MCQ-09",
         "A 62-year-old man with long-standing rheumatoid arthritis has had a chronically swollen right knee for 8 months. Aspirated fluid is yellow and shimmering. Microscopy shows large flat rectangular plates with a notched corner. Which crystal is this?",
         "Cholesterol crystals in a chronic effusion",
         ["Calcium pyrophosphate crystals", "Monosodium urate crystals", "Calcium oxalate crystals", "Basic calcium phosphate (apatite) crystals"], 0,
         "**แผ่นสี่เหลี่ยมใหญ่มุมบาก (notched rhomboid plate)** = **cholesterol** พบใน **effusion เรื้อรัง** เช่น RA หรือ OA ที่บวมนาน (น้ำขุ่นวาวเหมือนมีประกาย) — เป็นผลของน้ำค้างนาน ไม่ใช่สาเหตุของข้ออักเสบ\n\n"
         "- CPP = rhomboid **เล็ก** positive อ่อน\n"
         "- MSU = เข็ม · calcium oxalate = ซองจดหมาย · BCP = ก้อนเล็กไม่ birefringent",
         "Notched plate ในน้ำข้อเรื้อรัง = cholesterol", "Synovial crystals", REFR("ตารางผลึก 6 ชนิดของกลุ่ม 6ก/6ข"), NL_SF + NL_RA)],
    imgs={
        "art-msu-micro": img("art-06-msu-microscopy", "ผลึก MSU — light microscope (ซ้าย) และ compensated polarized light (ขวา)",
                             "ภาพซ้ายเป็นเซลล์เม็ดเลือดขาวกลม ๆ ใต้กล้องธรรมดามีผลึกแท่งเล็กอยู่ระหว่างเซลล์ ภาพขวาพื้นสีชมพูม่วงมีผลึกเข็มยาวสีเหลืองแนวทแยง และผลึกเข็มสีฟ้าแนวนอน",
                             cap="ซ้าย: ใต้ **light microscope ธรรมดา** ก็เห็นผลึกเข็มระหว่าง/ในเม็ดเลือดขาว (อาจารย์: ไม่มี polarized ก็ดูได้) · ขวา: polarized — เข็มที่วางแนวหนึ่งเป็น **เหลือง** อีกแนวตั้งฉากเป็น **ฟ้า** = **negative birefringence** · ลบลายมือที่ผู้ใช้จดบนภาพออกแล้ว"),
        "art-crystals": img("art-07-crystals-polarized", "ผลึกสองชนิดใต้ polarized light — แยกให้ได้",
                            "ภาพสองช่อง ซ้ายพื้นม่วงมีผลึกเข็มยาวจำนวนมากสีเหลืองและฟ้า ขวาพื้นชมพูมีผลึกเล็กรูปสี่เหลี่ยมขนมเปียกปูนและแท่งสั้น บางอันสีฟ้า มีคำบรรยายใต้ภาพ",
                            credit=CR_C, q="ผลึกซ้ายและขวาคืออะไร — ดูรูปร่าง ความสว่าง และสีเมื่อขนานแกน",
                            quiz="**ซ้าย = MSU (เกาต์)** เข็มยาว เรืองสว่าง **ขนานเหลือง** = negative แรง · **ขวา = CPP (CPPD)** rhomboid/แท่งสั้น เรืองจาง **ขนานฟ้า** = positive อ่อน — **ABC: Aligned Blue → Calcium**")})


# ═════════════════════════════════════════════════════════════════ หัวข้อใหม่ 5 · RA
NEW["air-23-art-05"] = sec(
    "air-23-art-05", "Rheumatoid arthritis — เกณฑ์ 2010 จากเคสจริง กลไก นอกข้อ และพยากรณ์โรค",
    "คิดคะแนน ACR/EULAR 2010 ของเคสหญิง 34 ปี (ได้ 6 โดยไม่ต้องรอแล็บ) · HLA-DR4 + บุหรี่ → citrullination → ACPA → pannus · RA ไม่ค่อยโดนไต · C1–C2",
    12, NL_RA + ["B5.3(5)", "B5.3(1)"],
    """
### ภาพรวม (สไลด์ p58–p63)
- **Chronic polyarthritis · F:M 2–3:1** · สไลด์ให้อายุ **30–55 ปี (1/3 เริ่มหลัง 60)** · อาจารย์แก้กลุ่มที่เขียน 55–75 ว่า "แก่ไป" → **40–50 ปี แก่กว่า SLE นิดหนึ่ง** (✍️ "กลาง ๆ")
- **Additive · slow progression · wax and wane**
- **Genetic: shared epitope บน HLA class II — HLA-DRB1 (0401) กรดอะมิโน 70–74** → สัมพันธ์ anti-CCP บวกและโรครุนแรง · อาจารย์: "**HLA class II, HLA-DR4 มีสิทธิ์ถาม**"
- **Environment: smoking · viral (EBV, parvovirus) · mycoplasma** (✍️ วงทุกตัว)
- ข้อที่โดน: **TMJ · PIP · MCP · wrist · shoulder · elbow · hip · knee · ankle · MTP · midtarsal — ยกเว้น DIP** · spine รอด **ยกเว้น C-spine (C1–C2)**

[[img:art-ra-stages]]

### เกณฑ์ ACR/EULAR 2010 (classification) — ≥ 6 จาก 10 = RA
ใช้กับผู้ที่มี **synovitis อย่างน้อย 1 ข้อ** ที่อธิบายด้วยโรคอื่นไม่ได้ (เป็น classification criteria ไม่ใช่ diagnostic criteria)

| หมวด | เกณฑ์ | คะแนน |
|---|---|---|
| **Joint (0–5)** | ข้อกลาง/ใหญ่ 1 ข้อ | 0 |
| | ข้อกลาง/ใหญ่ 2–10 ข้อ | 1 |
| | ข้อเล็ก 1–3 ข้อ (มีข้อใหญ่ร่วมหรือไม่ก็ได้) | 2 |
| | ข้อเล็ก 4–10 ข้อ | 3 |
| | **> 10 ข้อ (มีข้อเล็กอย่างน้อย 1)** | **5** |
| **Serology (0–3)** | RF และ ACPA ลบ | 0 |
| | RF หรือ ACPA บวกต่ำ (≤ 3 เท่า ULN) | 2 |
| | RF หรือ ACPA **บวกสูง (> 3 เท่า ULN)** | 3 |
| **Acute phase (0–1)** | CRP และ ESR ปกติ / ผิดปกติอย่างใดอย่างหนึ่ง | 0 / 1 |
| **Duration (0–1)** | < 6 สัปดาห์ / **≥ 6 สัปดาห์** | 0 / 1 |

ข้อเล็ก = MCP · PIP · MTP 2–5 · IP นิ้วโป้ง · **ข้อมือ** · ข้อกลาง/ใหญ่ = ไหล่ ศอก สะโพก **เข่า** ข้อเท้า (DIP, CMC1, MTP1 ไม่นับ — เป็นข้อของ OA)

**คิดคะแนนเคสกลุ่ม 19B/20B (หญิง 34 ปี)** — ข้อมือ 2 + PIP 8 (ข้อเล็กรวม 10) + เข่า 2 = **12 ข้อ มีข้อเล็ก → 5** · อาการ 4 เดือน **→ 1** · ยังไม่ได้ส่ง RF/anti-CCP/ESR/CRP → 0 → **รวม 6 = เข้าเกณฑ์ RA ได้ทันทีโดยไม่ต้องรอแล็บ** (ยังควรส่งเพื่อดูพยากรณ์โรค)
สไลด์ p65 เทียบ: **ACR 1987 (≥ 4/7) sensitivity 47.1% specificity 92.9%** (✍️ "สูงมาก") vs **2010 sensitivity 73.5% specificity 71.4%** — เกณฑ์ใหม่จับ RA ระยะแรกได้มากขึ้น

### Serology
- **RF** = แอนติบอดี (IgM IgG IgA IgE) ต่อ **Fc ของ IgG** → กระตุ้น classical complement · บวก **75–80%** ใน RA · สัมพันธ์ extra-articular และความรุนแรง · แต่บวกใน **Sjögren ~90% · SLE ~40%** ติดเชื้อเรื้อรัง และผู้สูงอายุ 5–25%
- **ACPA (anti-CCP)** — **sensitivity 77% specificity 97%** (✍️ "เจอแต่ต่ำ จำเพาะสูง") · ทำนาย **erosion รุนแรง** และ **การกลายเป็น RA ใน early arthritis**

[[anim:art-rapath]]

#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ฝืดตอนเช้า > 1 ชั่วโมง** | synovium อักเสบสร้างน้ำและ cytokine คั่งขณะนอนนิ่ง + cortisol ช่วงเช้ายังต่ำ | OA ไม่กี่นาที |
| **Swan neck** (PIP เหยียดเกิน · DIP งอ) | synovitis ที่ MCP/PIP ทำให้ volar plate หลวม + intrinsic muscle ตึง ดึง PIP ให้เหยียดเกิน | ภาพในสไลด์เคส |
| **Boutonnière** (PIP งอ · DIP เหยียดเกิน) | synovitis ที่ PIP ยืด/ฉีก **central slip** → lateral band เลื่อนลงด้านฝ่ามือ PIP ทะลุขึ้นมาเหมือนรังดุม | |
| **Ulnar drift ที่ MCP** | capsule และ collateral ligament หลวม + แรงดึงของเอ็นเหยียดเลื่อนไปด้าน ulnar | |
| **Erosion ขอบข้อ (bare area)** | pannus กัดตรงขอบที่ไม่มีกระดูกอ่อนคลุม · RANKL → osteoclast | เกาต์มีขอบยื่น · OA มี osteophyte |
| **ซีด เพลีย CRP สูง** | IL-6 → ตับสร้าง CRP + **hepcidin** ขังเหล็ก → anemia of inflammation | |

[[img:art-swan]]

[[img:art-ra-erosion]]

### นอกข้อ (สไลด์ p60 + สไลด์เคส)
| ระบบ | สิ่งที่ต้องรู้ |
|---|---|
| ผิว/หลอดเลือด | **rheumatoid nodule** แข็งไม่เจ็บที่ศอก (มัก seropositive) · **rheumatoid vasculitis** — นิ้วขาดเลือด แผล mononeuritis multiplex |
| ตา | **keratoconjunctivitis sicca** (secondary Sjögren) · episcleritis · **scleritis ปวดลึกมาก → ส่งจักษุด่วน** · scleromalacia perforans |
| ปอด | **ILD (UIP, NSIP)** · nodule · pleural effusion (glucose ต่ำ) · bronchiectasis · organizing pneumonia |
| หัวใจ | **accelerated atherosclerosis = สาเหตุตายอันดับหนึ่ง** · pericarditis · HFpEF |
| เลือด | **anemia of inflammation** · **Felty = RA + splenomegaly + neutropenia** (ปัจจุบันพบน้อย) · LGL leukemia (✍️ "one of lymphoma") · lymphoma |
| ประสาท | **carpal tunnel** (✍️) · mononeuritis multiplex · **atlantoaxial subluxation** |
| กระดูก | **osteoporosis** (โดยเฉพาะใช้ steroid นาน) |
| ไต | ✍️ **"RA ไม่โดนไต"** — AA amyloidosis เฉพาะโรคนานที่ไม่ได้รักษา (ปัจจุบันพบน้อย) · ไตผิดปกติมักมาจากยา (NSAIDs) |

> **ราวด์ 5 พ.ย. · polyarthritis + โปรตีนในปัสสาวะ** — "คนไข้ปวดข้อหลายข้อสองมือ แล้วมี **proteinuria** ด้วย (แม้ RF บวก) → ตอบ **SLE** ไม่ตอบ RA" เพราะ RA ไม่ค่อยโดนไต และ RF บวกได้ใน SLE ~40%

[[img:art-atlantoaxial]]

### พยากรณ์โรค
- **Poor prognostic factors (สไลด์เคส)**: **anti-CCP บวก · erosion บน X-ray ที่ลุกลาม · RF สูง · ESR/CRP สูง** · สไลด์ p73 เพิ่ม: extra-articular · physical function ต่ำ · เศรษฐานะและการศึกษาต่ำ · ใช้ prednisone นาน
- **ตายจาก ischemic heart disease และ infection** — คุม CV risk ไปพร้อมกับการอักเสบ
- อาจารย์ประเมินเคสหญิง 34 ปีว่า **early RA (~4 เดือน)** = ช่วงที่ DMARD เร็วป้องกัน erosion ได้มากที่สุด
""",
    ["ACR/EULAR 2010: > 10 ข้อ (มีข้อเล็ก) 5 · บวกสูง 3 · CRP/ESR 1 · ≥ 6 สัปดาห์ 1 · ≥ 6 = RA",
     "ข้อมือนับเป็นข้อเล็ก · เข่าเป็นข้อใหญ่ · DIP/CMC1/MTP1 ไม่นับ",
     "Anti-CCP: sens 77% spec 97% ทำนาย erosion · RF บวกใน Sjögren SLE ผู้สูงอายุ",
     "HLA class II (HLA-DRB1 0401 / DR4) + บุหรี่ → citrullination → ACPA",
     "RA ไม่ค่อยโดนไต: polyarthritis + proteinuria → คิด SLE",
     "ตายจากโรคหัวใจหลอดเลือดและการติดเชื้อ · C1–C2 subluxation ระวังตอนใส่ท่อช่วยหายใจ"],
    [mcq_fixed(P + "MCQ-10",
               "A 34-year-old woman has had pain and swelling of both wrists, all eight proximal interphalangeal joints of the fingers and both knees for 4 months. ESR is 48 mm/h (raised), and both rheumatoid factor and anti-CCP are negative. What is her 2010 ACR/EULAR classification score for rheumatoid arthritis?",
               ["5", "6", "7", "8", "9"], 2,
               "**Joint: 12 ข้อ (ข้อมือ 2 + PIP 8 = ข้อเล็ก 10 · เข่า 2) → > 10 ข้อมีข้อเล็ก = 5** · serology ลบทั้งคู่ = 0 · **ESR สูง = 1** · **4 เดือน ≥ 6 สัปดาห์ = 1** → **รวม 7 ≥ 6 = RA**\n\n"
               "- **6** = ลืมให้คะแนน ESR (ตัวเลขของสไลด์เคสที่ยังไม่ได้ส่งแล็บ)\n"
               "- **5** = นับเฉพาะข้อเล็ก 4–10 ได้ 3 แล้วบวกอีก 2 — ผิด เพราะรวมทุกข้อ > 10 ได้ 5 ทันที\n"
               "- 8/9 = ให้คะแนน serology ทั้งที่ลบ\n\n"
               "Seronegative ก็เข้าเกณฑ์ได้ถ้าข้อมากและอาการนาน",
               "> 10 ข้อ (มีข้อเล็ก) = 5 ทันที · ข้อมือเป็นข้อเล็ก", "ACR/EULAR 2010",
               ["สไลด์เคส ARTHRITIS กลุ่ม 19B/20B — 2010 ACR/EULAR scoring"] + REF("Classification criteria p65"), NL_RA),
     mcq(P + "MCQ-11",
         "A 41-year-old smoker has had symmetric small-joint polyarthritis of the hands for 10 weeks. Which laboratory test is the most specific for rheumatoid arthritis and best predicts future erosive disease?",
         "Anti-cyclic citrullinated peptide antibody (ACPA)",
         ["IgM rheumatoid factor", "Antinuclear antibody", "C-reactive protein", "HLA-B27"], 2,
         "**ACPA (anti-CCP): sensitivity 77% · specificity 97%** (สไลด์ p68 — ✍️ \"เจอแต่ต่ำ จำเพาะสูง\") · บอก **erosion รุนแรง** และ **การลุกลามเป็น RA ใน early arthritis** · บุหรี่กระตุ้น citrullination จึงพบ ACPA บ่อยในผู้สูบบุหรี่\n\n"
         "- **RF** บวก 75–80% แต่ไม่จำเพาะ (Sjögren ~90% SLE ~40% ผู้สูงอายุ ติดเชื้อ)\n"
         "- **ANA** ใช้คัด SLE (ANA ลบ = ตัด SLE ได้เกือบหมด)\n"
         "- **CRP** บอกการอักเสบ ไม่บอกโรค\n"
         "- **HLA-B27** = spondyloarthritis",
         "Anti-CCP: จำเพาะ 97% ทำนาย erosion", "RA serology", REF("ACPA p68 · RF p67"), NL_RA + ["B5.3(5)"]),
     mcq(P + "MCQ-12",
         "A 66-year-old woman with 20 years of erosive rheumatoid arthritis is scheduled for elective hip replacement under general anaesthesia. She reports occipital pain and occasional tingling in both hands when she flexes her neck. Which preoperative investigation is most important?",
         "Lateral cervical spine radiographs in flexion and extension",
         ["Lumbar spine MRI", "Nerve conduction study of the median nerves", "Bone densitometry of the hip", "Rheumatoid factor titre"], 3,
         "RA มี axial involvement ที่เดียวคือ **C1–C2** → **atlantoaxial subluxation** (synovitis กัด transverse ligament) · ปวดท้ายทอย + อาการไขสันหลังเมื่อก้มคอ → ต้องประเมิน **atlanto-dens interval** (ปกติ **< 3 มม. ในผู้ใหญ่** — สไลด์ p64) ก่อนใส่ท่อช่วยหายใจซึ่งต้องแหงนคอ\n\n"
         "- lumbar spine ไม่ใช่เป้าของ RA\n"
         "- carpal tunnel ทำให้ชามือแต่ไม่สัมพันธ์กับการก้มคอ\n"
         "- BMD และ RF ไม่เปลี่ยนการเตรียมผ่าตัดเรื่องความปลอดภัยของไขสันหลัง",
         "RA นาน + ปวดท้ายทอย/ชามือเมื่อก้มคอ → flexion–extension C-spine ก่อนดมยา", "Atlantoaxial subluxation", REF("C1C2-subluxation p64") + REFR("RA axial C1–C2"), NL_RA + ["B5.3(1)"])],
    imgs={
        "art-ra-stages": img("art-01-ra-xray-stages", "ภาพรังสี RA จากระยะแรกถึงระยะสุดท้าย",
                             "ภาพรังสีมือสี่ภาพเรียงจาก early RA moderate severe ถึง terminal RA มีหัวลูกศรสีฟ้า ชมพู เหลือง ดำ และเขียวชี้ความผิดปกติ และแถบคำอธิบายสีด้านล่าง",
                             cap="ฟ้า = **joint space narrowing** · ชมพู = **bone erosion** · เหลือง = subluxation · ดำ = ankylosis (ข้อมือ) · เขียว = subluxation และ mutilating change — RA ไล่จากข้อเล็กมือ/ข้อมือ **สองข้าง** และ DIP รอดจนระยะท้าย"),
        "art-ra-erosion": img("art-02-ra-marginal-erosion", "Marginal erosion ใน RA — ภาพรังสีและแผนภาพ",
                              "ภาพรังสีมือทั้งสองข้างของผู้ป่วย RA และแผนภาพข้อปกติเทียบกับข้อ RA ที่มี pannus กัดกร่อนบริเวณ bare area ที่ขอบข้อ",
                              cap="แผนภาพ: ข้อปกติมี **bare area** ตรงขอบข้อที่กระดูกไม่มีกระดูกอ่อนคลุม · ใน RA **synovitis/pannus** กัดตรงนั้นก่อน = **marginal erosion** · ภาพรังสีมือสองข้าง (สไลด์ p69 Radiography) ให้ฝึกหา erosion ที่ขอบ MCP/PIP และข้อมือ"),
        "art-atlantoaxial": img("art-03-atlantoaxial", "C1–C2 subluxation — atlanto-dens interval",
                                "แผนภาพกระดูกคอ C1 C2 ระบุ normal atlantodens interval น้อยกว่า 3 มิลลิเมตรในผู้ใหญ่และน้อยกว่า 4.5 มิลลิเมตรในเด็ก และภาพรังสีคอด้านข้างมีลูกศรสองอันชี้ระยะห่างที่กว้างขึ้น",
                                cap="ระยะระหว่าง anterior arch ของ C1 กับ dens ปกติ **< 3 มม. (ผู้ใหญ่) · < 4.5 มม. (เด็ก)** · ภาพรังสีขวา (ลูกศร) ระยะกว้างขึ้น = subluxation จาก synovitis กัด transverse ligament — ระวังตอนแหงนคอใส่ท่อช่วยหายใจ"),
        "art-swan": img("art-11-swan-boutonniere", "Swan neck และ Boutonnière deformity",
                        "แผนภาพนิ้วสองแบบ ซ้าย swan neck มี PIP เหยียดเกินและ DIP งอ ขวา boutonniere มี PIP งอและ DIP เหยียดเกิน พร้อมวงขยายแสดงการฉีกขาดของ central slip",
                        credit=CR_C,
                        cap="**Swan neck**: PIP เหยียดเกิน + DIP งอ · **Boutonnière**: PIP งอ + DIP เหยียดเกิน จาก **central slip ฉีก** (วงขยาย) — เป็นผลของ synovitis เรื้อรัง ไม่ได้รักษา")})

# ═════════════════════════════════════════════════════════════════ หัวข้อใหม่ 6 · ยา RA
NEW["air-23-art-06"] = sec(
    "air-23-art-06", "ยารักษา RA — treat to target · csDMARD · biologic · JAK และพิษที่ต้องรู้",
    "อาจารย์: รู้ชื่อยา + ผลข้างเคียง ไม่ต้องรู้ขนาด · MTX = anchor · steroid = bridge · anti-TNF → TB (รวมนอกปอด) · rituximab = anti-CD20 · JAK → งูสวัด VTE",
    10, NL_RA + ["B5.4(3)", "B5.4(1)"],
    """
### หลักการ (สไลด์ p70–p72 + สไลด์เคส)
- **เริ่ม DMARD ให้เร็ว** — ช่วงแรกของโรค (early RA เช่นเคสหญิง 34 ปีที่เป็น 4 เดือน) คือช่วงที่ป้องกัน erosion ได้มากที่สุด
- **Methotrexate = anchor drug** · ใช้ **steroid ขนาดต่ำเป็น bridging therapy** ระหว่างรอ csDMARD ออกฤทธิ์ราว **2–3 เดือน** แล้วลดเลิก
- **Treat to target** — เป้าหมาย remission หรือ low disease activity · ไม่ดีขึ้นใน ~3 เดือนหรือไม่ถึงเป้าใน ~6 เดือน → ปรับยา/เพิ่ม biologic หรือ JAK *(ตามแนวทาง EULAR 2022/ACR 2021 — สไลด์ไม่ได้ลงรายละเอียด)*
- อาจารย์: **"biologic ทั้งหลาย รู้ชื่อก็พอ ไม่ต้องรู้ dose แล้วก็รู้ side effect"** (✍️ "รู้ชื่อ + complication")

### csDMARD และยาบรรเทาอาการ
| ยา | กลไก (สั้น) | ผลข้างเคียงที่ออกสอบ | ข้อห้าม/ข้อควรทำ |
|---|---|---|---|
| **Methotrexate** | antifolate ขนาดต่ำ (DHFR) · ต้านอักเสบผ่าน **adenosine** | แผลในปาก · **transaminitis/ตับ** · **กดไขกระดูก** · **pneumonitis** (ไข้ ไอแห้ง หอบ) · teratogen | **สัปดาห์ละครั้ง** + **folic acid** · ห้ามตั้งครรภ์ (หยุดก่อนตั้งครรภ์ 1–3 เดือน) · ESRD · โรคตับ/ดื่มเหล้า |
| **Leflunomide** | ยับยั้งการสร้าง pyrimidine ของ lymphocyte | ตับ · ท้องเสีย · ความดันสูง · teratogen ค้างนาน | ต้อง washout (cholestyramine) ก่อนตั้งครรภ์ |
| **Sulfasalazine** | prodrug → แบคทีเรียลำไส้แยกเป็น **5-ASA + sulfapyridine** · ยับยั้ง NF-κB เพิ่ม adenosine | **hemolysis ใน G6PD deficiency** · leukopenia · SJS/TEN · **อสุจิลดชั่วคราว** | แพ้ sulfa/salicylate |
| **Hydroxychloroquine** | weak base สะสมใน lysosome ของ APC → ลดการนำเสนอผ่าน MHC II · TLR7/9 | **retinal toxicity (bull's-eye maculopathy)** เมื่อใช้นาน → ตรวจตา | **ไม่กดภูมิ ไม่เป็นพิษต่อไต** · ปลอดภัยที่สุดในกลุ่ม (ใช้ในตั้งครรภ์ได้) |
| **Glucocorticoid ขนาดต่ำ** | กด NF-κB → ลด IL-1 IL-6 TNF | Cushingoid · น้ำตาล ไขมัน น้ำหนักขึ้น · **osteoporosis** · AVN · ต้อกระจก · ติดเชื้อ | bridging ระยะสั้น · ระวัง systemic fungal infection · live vaccine เมื่อขนาดสูง |
| **NSAIDs** | ยับยั้ง COX-1/2 | แผลกระเพาะ/เลือดออก · AKI · ความดัน · หัวใจ | **บรรเทาอาการเท่านั้น ไม่ชะลอโรค** · เลี่ยงใน PUD · CrCl < 30 · NYHA III–IV |

> **สไลด์เคส vs ข้อเท็จจริง** — กลุ่มนำเสนอพูดว่า MTX ทำให้ "acute interstitial nephritis มีไข้ ไอแห้ง" — อาการไข้ ไอแห้ง หอบ คือ **MTX pneumonitis** (hypersensitivity) ต้องหยุดยา · และ "ห้ามใช้ NSAIDs ใน active RA" ไม่ถูก — NSAIDs ใช้บรรเทาอาการได้ ข้อห้ามมาจากกระเพาะ ไต หัวใจ · อาจารย์เตือนในราวด์ว่า "**ฟังไว้ก่อน อย่าเชื่อไปหมด**"

### bDMARD และ tsDMARD
| กลุ่ม | ยา | ผลข้างเคียงสำคัญ |
|---|---|---|
| **Anti-TNF** | infliximab · etanercept · adalimumab · golimumab · certolizumab (+ biosimilar) | **TB reactivation รวม extrapulmonary TB** (✍️ สไลด์ p72) · เชื้อรา · HBV · หัวใจล้มเหลวแย่ลง · demyelination · drug-induced lupus |
| **Anti-CD20** | **rituximab** (ใช้ในไทย — อาจารย์) | ปฏิกิริยาระหว่างให้ยา · HBV reactivation · hypogammaglobulinemia |
| **CTLA4-Ig** | abatacept (บล็อก CD80/86–CD28 ของ T cell) | ติดเชื้อ · COPD กำเริบ |
| **Anti-IL-6R** | **tocilizumab** · sarilumab | **ไขมัน LDL สูง** · transaminitis · neutropenia · **ลำไส้ส่วนล่างทะลุ** · **CRP/ESR ปกติแม้ติดเชื้อ** |
| **IL-1RA** | anakinra | ติดเชื้อ ปฏิกิริยาที่ผิวหนัง |
| **JAK inhibitor** | tofacitinib (JAK1/3) · baricitinib (JAK1/2) · upadacitinib | **herpes zoster** · **VTE** · **MACE** · ไขมันสูง · cytopenia · ห้ามในตั้งครรภ์/ให้นม |

> **ราวด์ 5 พ.ย. · anti-TNF** — อาจารย์ถามทั้งห้อง "ฉีด anti-TNF ไปแล้วเกิดอะไร — **TB** … complication ที่สำคัญมาก ๆ ของการอยู่เมืองไทย" รวม **TB นอกปอด** · ก่อนเริ่มยาต้อง **คัดกรอง latent TB (IGRA/TST + CXR) และ HBV** (รายละเอียดในคาบ 33)

#### ทำไมถึงมีผลข้างเคียงนี้
| ผลข้างเคียง | กลไก | ใช้ในข้อสอบ |
|---|---|---|
| **Anti-TNF → TB** | TNF จำเป็นต่อการคง **granuloma** ที่ขัง M. tuberculosis — ตัด TNF granuloma แตก เชื้อออกมา มักเป็น extrapulmonary/disseminated | คัดกรอง latent TB ก่อนทุกครั้ง |
| **MTX → แผลปาก เม็ดเลือดต่ำ** | ขาด folate ในเซลล์ที่แบ่งตัวเร็ว (เยื่อบุ ไขกระดูก) | ให้ folic acid ลดพิษ · ห้ามกินทุกวัน |
| **SSZ → hemolysis** | sulfapyridine เป็นสารออกซิไดซ์ · ใน G6PD deficiency เม็ดเลือดแดงทนไม่ได้ | ตรวจ G6PD ในคนไทยก่อนเริ่ม |
| **HCQ → จอตา** | ยาจับ melanin สะสมใน retinal pigment epithelium | ตรวจตาเป็นระยะ |
| **Tocilizumab → CRP ปกติ** | **IL-6 คือตัวสั่งตับสร้าง CRP** — ปิด IL-6R ก็ไม่มี CRP แม้ติดเชื้อ | อย่าใช้ CRP ตัดการติดเชื้อ |
| **JAK → งูสวัด** | interferon และ IL-15 ส่งสัญญาณผ่าน JAK เพื่อคุมไวรัส (NK, CD8) | พิจารณาวัคซีนงูสวัดก่อน |
""",
    ["MTX = anchor · สัปดาห์ละครั้ง + folic acid · ห้ามตั้งครรภ์ · ไข้ไอแห้งหอบ = MTX pneumonitis",
     "Steroid ขนาดต่ำเป็น bridge 2–3 เดือนระหว่างรอ csDMARD",
     "Anti-TNF → TB (รวมนอกปอด) — คัดกรอง latent TB + HBV ก่อนเริ่ม",
     "Rituximab = anti-CD20 (B cell) · abatacept = CTLA4-Ig · tocilizumab = IL-6R (CRP ปกติแม้ติดเชื้อ)",
     "JAK inhibitor: งูสวัด · VTE · MACE",
     "SSZ: hemolysis ใน G6PD · HCQ: จอตา แต่ไม่กดภูมิ ปลอดภัยที่สุด"],
    [mcq(P + "MCQ-13",
         "A 45-year-old Thai woman with rheumatoid arthritis has persistent active synovitis despite 6 months of methotrexate 20 mg weekly and sulfasalazine. Adalimumab is planned. Which screening is most important before the first dose?",
         "Interferon-gamma release assay or tuberculin skin test plus chest radiograph, together with hepatitis B serology",
         ["Antinuclear antibody and anti-dsDNA", "HLA-B5801 genotyping", "Bone mineral density", "Echocardiography"], 0,
         "**Anti-TNF → reactivation of latent TB** (✍️ สไลด์ p72 \"anti-TNF ⇒ TB extrapulmonary\") — TNF จำเป็นต่อ granuloma · อาจารย์: complication ที่สำคัญที่สุดของการอยู่เมืองไทย → **คัดกรอง latent TB (IGRA/TST + CXR)** และ **HBV** ก่อนเสมอ ถ้าเป็น latent TB ให้รักษาก่อน/พร้อมกันตามแนวทาง\n\n"
         "- ANA/anti-dsDNA ไม่ใช่การคัดกรองก่อนยา (anti-TNF ทำ drug-induced lupus ได้ แต่ไม่ต้องตรวจก่อน)\n"
         "- **HLA-B5801** ใช้ก่อน **allopurinol**\n"
         "- BMD และ echo ไม่ใช่ข้อบังคับ (ระวังเฉพาะผู้ที่มีหัวใจล้มเหลวรุนแรง)",
         "ก่อน anti-TNF: latent TB (IGRA/TST + CXR) + HBV", "Biologic safety", REF("bDMARD table p72 ✍️") + REFR("anti-TNF → TB"), NL_RA + ["B5.4(3)"]),
     mcq(P + "MCQ-14",
         "A 59-year-old man started methotrexate for rheumatoid arthritis 8 weeks ago. He now has fever, a dry cough and progressive dyspnoea over 1 week. SpO2 is 90% on room air and CT chest shows new bilateral ground-glass opacities. Blood and sputum cultures are negative so far. What is the most likely diagnosis?",
         "Methotrexate-induced pneumonitis",
         ["Acute interstitial nephritis from methotrexate", "Rheumatoid nodules of the lung", "Usual interstitial pneumonia of long-standing RA", "Rheumatoid pleural effusion"], 4,
         "**ไข้ + ไอแห้ง + หอบ + GGO สองข้าง ภายในไม่กี่เดือนหลังเริ่ม MTX = MTX pneumonitis** (hypersensitivity) → **หยุด MTX** ตัดการติดเชื้อ (รวม PJP) และให้ steroid\n\n"
         "- กลุ่มนำเสนอพูดว่า \"acute interstitial nephritis มีไข้ ไอแห้ง\" — **AIN เป็นโรคไต** (ไข้ ผื่น eosinophiluria creatinine ขึ้น) ไม่ทำให้ไอและ GGO\n"
         "- rheumatoid nodule เป็นก้อน ไม่ใช่ GGO เฉียบพลันพร้อมไข้\n"
         "- RA-ILD แบบ UIP ค่อยเป็นค่อยไปเป็นปี มี reticulation/honeycomb ฐานปอด\n"
         "- pleural effusion เห็นน้ำในช่องปอด ไม่ใช่ GGO",
         "เริ่ม MTX ไม่กี่เดือน + ไข้ ไอแห้ง หอบ GGO = MTX pneumonitis → หยุดยา", "DMARD toxicity",
         ["สไลด์เคส ARTHRITIS กลุ่ม 19B/20B — csDMARDs (แก้คำว่า AIN)"] + REFR("ผลข้างเคียง MTX"), NL_RA + ["B5.4(3)"]),
     mcq(P + "MCQ-15",
         "A 67-year-old man with rheumatoid arthritis, hypertension and a 40 pack-year smoking history is considering tofacitinib. Which group of adverse effects is particularly associated with JAK inhibitors?",
         "Herpes zoster reactivation, venous thromboembolism and major cardiovascular events",
         ["Retinal toxicity and haemolysis in G6PD deficiency", "Interstitial nephritis and hyperkalaemia", "Drug-induced lupus and demyelination", "Lower gastrointestinal perforation with masking of CRP"], 1,
         "สไลด์เคส: **JAK inhibitor → herpes zoster (สูงกว่า DMARD อื่นชัดเจน) · VTE · MACE** + ไขมันสูง เม็ดเลือดต่ำ · ระวังมากในผู้สูงอายุ สูบบุหรี่ มี CV risk (ผู้ป่วยรายนี้)\n\n"
         "- retinal toxicity = HCQ · hemolysis ใน G6PD = SSZ\n"
         "- drug-induced lupus/demyelination = **anti-TNF**\n"
         "- GI perforation + CRP ปกติ = **tocilizumab** (anti-IL-6R)\n"
         "- interstitial nephritis/hyperkalaemia ไม่ใช่ลักษณะของ JAK",
         "JAK → งูสวัด · VTE · MACE", "tsDMARD toxicity", ["สไลด์เคส ARTHRITIS กลุ่ม 19B/20B — tsDMARDs"] + REF("tsDMARDs p72"), NL_RA + ["B5.4(3)"])])


# ═════════════════════════════════════════════════════════════════ หัวข้อใหม่ 7 · SLE arthritis + SpA
NEW["air-23-art-07"] = sec(
    "air-23-art-07", "SLE arthritis และ spondyloarthritis — แยกจาก RA ให้ได้",
    "SLE: polyarthritis สมมาตรแบบไม่กัดกร่อน + อาการหลายระบบ · ANA ลบตัด SLE · proteinuria ชี้ SLE · SpA: HLA-B27 · enthesitis · dactylitis · axial · ไม่สมมาตร (ตรงข้าม RA)",
    9, NL_SPA + NL_SLE + ["B5.3(5)"],
    """
### SLE — ข้ออักเสบที่หน้าตาเหมือน RA
- หญิงวัยเจริญพันธุ์ **15–45 ปี** · ปัจจัย: พันธุกรรม/ครอบครัว · **แสง UV · ไวรัส · บุหรี่ · ยา (hydralazine, isoniazid)** (สไลด์เคส)
- ข้อ: ตั้งแต่ **arthralgia** (ปวดแต่ไม่บวม) ถึง arthritis — **symmetric polyarthritis ข้อเล็ก MCP PIP wrist** + เข่า มีฝืดเช้า
- ต่างจาก RA: **ไม่กัดกร่อน (non-erosive)** · ถ้าผิดรูปมักดันกลับได้ (Jaccoud arthropathy — *เพิ่มตามตำรา*) · มี **อาการหลายระบบ** ผื่น แผลปาก ผมร่วง serositis **ไต** เม็ดเลือดต่ำ
- แล็บ: **ANA ลบ → ตัด SLE ได้เกือบหมด** (สไลด์เคส: "ANA (−) → rule out") · ANA บวก → **anti-dsDNA / anti-Sm · C3 C4** · RF บวกได้ ~40% ของ SLE (สไลด์ p67) อย่าถูกหลอก
- อาจารย์: **polyarthritis สองมือ + proteinuria → ตอบ SLE** (RA ไม่ค่อยโดนไต) — รายละเอียดเกณฑ์และ lupus nephritis อยู่ในคาบ 33

### Spondyloarthritis (SNSA) — ทำไมจัดเป็นกลุ่มเดียวกัน (สไลด์ p74–p76)
สมาชิก: **ankylosing spondylitis (prototype) · psoriatic arthritis · reactive arthritis (เดิมเรียก Reiter) · enteropathic (IBD) · undifferentiated**

| ลักษณะร่วม | รายละเอียด |
|---|---|
| **HLA-B27** | AS > 90% · ReA 85% · Reiter 80% · IBD 50% · PsA-spondylitis 50% (peripheral 15%) · Whipple 30% |
| **Enthesitis** | เอ็นร้อยหวาย · **plantar fascia** (ปวดส้นเท้าก้าวแรกตอนเช้า) |
| **Axial** | **sacroiliitis · spondylitis** → inflammatory back pain |
| **Peripheral** | **asymmetric oligoarthritis ข้อใหญ่ขา** (เข่า ข้อเท้า สะโพก) — **ตรงข้ามกับ RA** · PsA เป็น poly ได้ |
| **Extra-articular** | **anterior uveitis** · psoriasis/เล็บ · IBD · keratoderma blennorrhagicum (ReA) |
| **Seronegative** | RF และ ANA ลบ (anti-CCP ก็ลบ) — "sero-negative" หมายถึงซีรัมลบต่อ autoantibody ของ RA ไม่ใช่ไม่มีโรค |

**Inflammatory back pain** (สไลด์เคส) — เริ่มก่อน 45 ปี ค่อยเป็นค่อยไป เรื้อรัง > 3 เดือน · **แย่ลงเมื่อพัก ดีขึ้นเมื่อขยับ/ออกกำลัง** · ฝืดหลังตอนเช้า > 30 นาที · ปวดกลางดึก
**Dactylitis** = นิ้วบวมทั้งนิ้วเหมือนไส้กรอก (PsA, ReA) · อาจารย์ให้คะแนนคนตอบได้ว่า SNSA สัมพันธ์กับ **HLA-B27**

> **ราวด์ 5 พ.ย. · spondylosis ≠ spondylitis** — **spondylosis = OA ของกระดูกสันหลัง (C และ L)** non-inflammatory · **spondylitis = SpA** อักเสบ · AS = **bamboo spine** · SpA peripheral ส่วนใหญ่ mono/oligo **ยกเว้น PsA ที่เป็น poly ได้คล้าย RA** ต้องดู distribution (DIP เล็บ dactylitis)

[[anim:art-enthesis]]

[[img:art-si]]

[[img:art-bamboo]]
""",
    ["SLE arthritis: สมมาตรข้อเล็ก ไม่กัดกร่อน + อาการหลายระบบ · ANA ลบตัด SLE",
     "Polyarthritis + proteinuria (แม้ RF บวก) → SLE ไม่ใช่ RA",
     "SpA: HLA-B27 · enthesitis · axial · peripheral ไม่สมมาตรข้อใหญ่ขา · uveitis psoriasis IBD · RF/ANA ลบ",
     "Inflammatory back pain: < 45 ปี · ดีขึ้นเมื่อขยับ แย่ลงเมื่อพัก · ฝืดเช้า > 30 นาที",
     "Spondylosis = OA ของ C/L spine (ไม่อักเสบ) · spondylitis = SpA"],
    [mcq(P + "MCQ-16",
         "A 26-year-old woman has symmetric pain and swelling of the MCP and PIP joints of both hands and both wrists for 3 months, with oral ulcers and hair loss. Rheumatoid factor is weakly positive. Urinalysis shows protein 2+ and 10–20 red cells/HPF with red-cell casts. Which test is the most appropriate next step to establish the diagnosis?",
         "Antinuclear antibody followed by anti-dsDNA and complement C3/C4",
         ["Anti-CCP antibody to confirm rheumatoid arthritis", "HLA-B27", "Serum urate", "Radiographs of the hands to look for erosions"], 3,
         "อาจารย์: **polyarthritis สองมือ + proteinuria → ตอบ SLE ไม่ใช่ RA** — RA \"ไม่ค่อยโดนไต\" (✍️ สไลด์ p60) และ **RF บวกได้ ~40% ใน SLE** · ผู้ป่วยมีแผลปาก ผมร่วง RBC cast = lupus nephritis → **ANA** (ลบ = ตัด SLE) แล้ว **anti-dsDNA · C3/C4** ตามแผนภาพของสไลด์เคส\n\n"
         "- anti-CCP ช่วย RA แต่ไม่อธิบาย active urinary sediment\n"
         "- HLA-B27 = SpA · urate = เกาต์\n"
         "- X-ray มือ: SLE ไม่กัดกร่อน ไม่ช่วยยืนยัน",
         "Polyarthritis + proteinuria/RBC cast → SLE → ANA, anti-dsDNA, C3/C4", "SLE vs RA",
         REFR("RA ไม่โดนไต · polyarthritis + proteinuria") + ["สไลด์เคส ARTHRITIS กลุ่ม 19B/20B — investigation chart"], NL_SLE + ["B5.3(5)"]),
     mcq(P + "MCQ-17",
         "A 24-year-old man has low back pain for 8 months that wakes him at night and improves with exercise but not with rest, plus heel pain on the first steps each morning. Last year he had a painful red eye with photophobia. His right knee and left ankle are swollen. Which feature best distinguishes his peripheral arthritis from rheumatoid arthritis?",
         "Asymmetric oligoarthritis of large lower-limb joints with enthesitis",
         ["Symmetric involvement of MCP and PIP joints", "High-titre anti-CCP antibody", "Morning stiffness of the hands lasting more than 1 hour", "Marginal erosions of the metacarpal heads"], 2,
         "ภาพนี้คือ **spondyloarthritis**: inflammatory back pain (< 45 ปี ดีขึ้นเมื่อขยับ ปวดกลางคืน) + **enthesitis** (plantar fascia/Achilles) + **anterior uveitis** · peripheral arthritis ของ SpA = **asymmetric oligoarthritis ข้อใหญ่ขา** — สไลด์ p76: \"asymmetric (**opposite to RA**)\" · สัมพันธ์ **HLA-B27**\n\n"
         "- MCP/PIP สมมาตร · anti-CCP สูง · ฝืดมือ > 1 ชม. · marginal erosion = ลักษณะของ **RA**",
         "SpA: ไม่สมมาตร ข้อใหญ่ขา + enthesitis (ตรงข้าม RA)", "SpA vs RA", REF("SNSA p76") + REFR("enthesitis dactylitis HLA-B27"), NL_SPA)],
    imgs={
        "art-si": img("art-08-sacroiliitis", "ภาพรังสีเชิงกราน — SI joint",
                      "ภาพรังสีเชิงกรานท่าหน้าตรง มีอักษร L มุมขวาบน เห็นข้อต่อ sacroiliac ทั้งสองข้างและข้อสะโพก",
                      q="ดูข้อต่อ sacroiliac สองข้าง — ปกติหรือไม่ และนึกถึงโรคกลุ่มใด",
                      quiz="**SI joint ทั้งสองข้างช่องข้อหายไปเป็นกระดูกเชื่อมกัน (ossification/ankylosis)** — สไลด์ p77 \"Ossification of SI joint space\" = **sacroiliitis ระยะท้าย** ของ **ankylosing spondylitis** (SpA · HLA-B27) · ต่างจาก OA สะโพกที่ช่องข้อแคบ + osteophyte"),
        "art-bamboo": img("art-09-bamboo-spine", "Bamboo spine — ankylosing spondylitis",
                          "ภาพรังสีกระดูกสันหลังส่วนเอวท่าหน้าตรงและท่าข้าง เห็นขอบกระดูกสันหลังแต่ละข้อเชื่อมกันด้วยแถบกระดูกบาง ๆ ทำให้แนวกระดูกดูเป็นปล้องเหมือนลำไผ่",
                          cap="**Syndesmophyte** บาง ๆ เชื่อมขอบ vertebra ต่อกันตลอดแนว + ligament ข้างกระดูกสันหลังกลายเป็นกระดูก → แนวเป็นปล้องเหมือน **ลำไผ่** = enthesitis ที่ซ่อมด้วยกระดูกใหม่ (ไม่ใช่ osteophyte ของ spondylosis ที่ยื่นออกด้านข้าง)")})


# ═════════════════════════════════════════════════════════════════ ข้อใหม่ที่เพิ่มในหัวข้อเดิม
OLD_ITEMS = {
    "air-23-01": [mcq(
        P + "MCQ-18",
        "A 63-year-old man with known gout (three previous self-limited attacks) presents with a hot, swollen right knee for 2 days and temperature 38.7 °C. Synovial fluid is turbid with 80,000 WBC/µL (92% neutrophils); polarized microscopy shows intracellular negatively birefringent needle-shaped crystals; Gram stain shows no organisms. Blood and synovial cultures are sent. What is the most appropriate management now?",
        "Start empirical intravenous antibiotics pending cultures, and treat the gout flare without intra-articular steroid",
        ["Treat as acute gout only with an intra-articular corticosteroid injection", "Discharge on colchicine because crystals explain the findings", "Start allopurinol 300 mg daily immediately", "Withhold all treatment until synovial culture results are available"], 4,
        "อาจารย์ในราวด์ใช้ตัวอย่างนี้ตรง ๆ: **เคยเป็น crystal/intermittent มาก่อน แต่ครั้งนี้ WBC 80,000 → \"ยังไงพี่ก็ใส่ antibiotic ก่อน แม้ว่าจะเจอ crystal\"** — **crystal และ septic อยู่ข้อเดียวกันครั้งเดียวกันได้** · WBC > 50,000 + ไข้ = ต้องคิด septic จนกว่า culture จะลบ · **Gram stain ลบไม่ตัด septic** (sensitivity 50–75% ใน Gram บวก — สไลด์ p18)\n\n"
        "- ฉีด steroid เข้าข้อที่อาจติดเชื้อ = อันตราย\n"
        "- ส่งกลับด้วย colchicine = พลาดข้อติดเชื้อที่ทำลายข้อในไม่กี่วัน\n"
        "- **ไม่เริ่ม** allopurinol ระหว่างกำเริบเฉียบพลันโดยไม่มี prophylaxis และไม่ใช่สิ่งเร่งด่วนตอนนี้\n"
        "- รอผล culture โดยไม่ให้ยา = ช้าเกินไป",
        "WBC > 50,000 + ไข้ แม้เจอผลึก → ยาปฏิชีวนะก่อน", "Crystal plus septic", REFR("WBC 80,000 + crystal → antibiotics") + REF("Investigations p18"),
        NL_SF + ["2.3.13-3(6)", "2.3.13(2)"])],
    "air-23-02": [mcq(
        P + "MCQ-19",
        "A 31-year-old woman at 32 weeks of gestation is found to have a serum uric acid of 6.4 mg/dL at an antenatal visit. Her blood pressure is 152/98 mmHg and urine dipstick shows protein 1+. She has no joint symptoms. What is the most important interpretation of the raised uric acid?",
        "It suggests pre-eclampsia, because urate is normally low in pregnancy as GFR rises",
        ["It is normal for the third trimester and needs no action", "It indicates early gout and allopurinol should be started", "It is caused by tumour lysis and needs urgent haematology review", "It is due to a high-purine diet and needs dietary advice only"], 2,
        "สไลด์ p26: **ตั้งครรภ์ urate > 4 mg/dL → pre-eclampsia** (✍️ วงไว้พร้อมเขียน \"Diag\") · อาจารย์: **ในคนท้องยูริกจะต่ำเพราะ GFR เพิ่ม ขับออกทางไตมากขึ้น — ถ้าสูง \"ไดแอคเลยว่าเป็น preeclampsia\"** · ผู้ป่วยรายนี้มีความดันสูง + proteinuria ด้วย\n\n"
        "- ไตรมาสสาม urate ขึ้นได้เล็กน้อยแต่ไม่ถึงระดับนี้ร่วมกับความดันสูง\n"
        "- หญิงก่อนหมดประจำเดือนแทบไม่เป็นเกาต์ (estrogen ช่วยขับ urate) และ **ห้ามใช้ allopurinol แบบนี้ในครรภ์**\n"
        "- tumour lysis และอาหาร ไม่เข้ากับบริบท",
        "ตั้งครรภ์ urate ควรต่ำ (GFR ↑) — สูง > 4 + ความดันสูง = pre-eclampsia", "Urate in women", REF("Hyperuricemia definition p26 ✍️") + REFR("gout ในผู้หญิงและคนท้อง"),
        NL_GOUT + ["B5.3(4)"])],
    "air-23-03": [mcq(
        P + "MCQ-20",
        "A 54-year-old man with recurrent gout has newly diagnosed hypertension (BP 158/96 mmHg). Serum urate is 8.9 mg/dL and eGFR is 82 mL/min/1.73 m². Which antihypertensive also lowers serum urate by increasing its urinary excretion?",
        "Losartan",
        ["Hydrochlorothiazide", "Furosemide", "Metoprolol", "Hydralazine"], 3,
        "สไลด์ p53: **mild uricosurics = losartan, fenofibrate** · กลุ่ม 6ก/6ข แนะนำ **losartan** สำหรับผู้ป่วยเกาต์ที่มีความดันสูงในเคสชาย 60 ปี — losartan ยับยั้ง **URAT1** ที่ท่อไตส่วนต้น จึงขับ urate ออกมากขึ้น (ARB ตัวอื่นไม่มีฤทธิ์นี้ชัด)\n\n"
        "- **thiazide และ loop** เพิ่มการดูดกลับ urate (สไลด์ p29 ยาที่ทำให้ขับออกน้อย · และเป็นปัจจัยเสี่ยงของ allopurinol hypersensitivity)\n"
        "- beta-blocker สัมพันธ์กับ urate สูงขึ้น/เสี่ยงเกาต์มากขึ้นเล็กน้อย\n"
        "- hydralazine ไม่มีฤทธิ์ขับ urate",
        "ความดันสูง + เกาต์ → losartan (uricosuric อ่อน ๆ) · เลี่ยง thiazide/loop", "Gout comorbidity", REF("Uricosurics p53") + REFR("losartan ในผู้ป่วยความดันสูง"),
        NL_GOUT + ["B5.4(4)"])],
    "air-23-05": [mcq(
        P + "MCQ-21",
        "A 72-year-old woman had a total knee replacement 14 months ago. She now has 6 weeks of increasing knee pain, a small effusion and a low-grade fever. Aspirate shows 4,800 WBC/µL with 85% neutrophils. Which organism is the most common cause in this setting?",
        "Coagulase-negative staphylococci such as Staphylococcus epidermidis",
        ["Neisseria gonorrhoeae", "Salmonella species", "Streptococcus pneumoniae", "Pasteurella multocida"], 4,
        "สไลด์ p16: **prosthetic joint — common = coagulase-negative staphylococci (S. epidermidis) และ S. aureus** · เชื้อสร้าง biofilm บนข้อเทียม อาการจึงค่อยเป็นค่อยไป ไข้ต่ำ และ WBC ในน้ำข้อต่ำกว่าข้อปกติที่ติดเชื้อ (เกณฑ์ข้อเทียมใช้ค่าต่ำกว่า 50,000 มาก)\n\n"
        "- GC = คนหนุ่มสาวที่มีเพศสัมพันธ์ (naive joint)\n"
        "- Salmonella = Gram ลบในผู้สูงอายุ > 60 ปี/มีปัจจัยเสี่ยง (เช่น sickle cell, ภูมิต่ำ) แต่ไม่ใช่สาเหตุหลักของข้อเทียม\n"
        "- S. pneumoniae = naive joint\n"
        "- Pasteurella = สัตว์กัด",
        "ข้อเทียม → CoNS (S. epidermidis) + S. aureus", "Septic arthritis organisms", REF("Organisms prosthetic joint p16"),
        ["2.3.13-3(6)", "B5.2.2-3(1)"]),
        mcq(
        P + "MCQ-22",
        "A 55-year-old man receiving chemotherapy for lymphoma (absolute neutrophil count 400/µL) develops fever 39 °C and an acutely swollen left knee. After synovial fluid and two blood cultures are taken, Gram stain of the fluid shows no organisms. According to the lecture, which empirical antibiotic approach is most appropriate?",
        "Broad empirical cover including an anti-pseudomonal agent (for example ceftazidime, cefepime, piperacillin–tazobactam or meropenem)",
        ["Ceftriaxone alone", "Oral amoxicillin–clavulanate", "Withhold antibiotics until cultures are reported", "Intra-articular corticosteroid and observation"], 1,
        "สไลด์ p19: **normal host → ceftriaxone หรือ cefotaxime** · **immunocompromised / sepsis / septic shock / neutropenia / bacteremia / burn → เชื้อดื้อยา > 10–15% → anti-Pseudomonas 1–2 ตัว** (ceftazidime, ciprofloxacin, meropenem, Tazocin, cefepime, gentamicin) แล้วปรับตามผลเพาะเชื้อ · ✍️ สไลด์ p15 \"Gram −ve: immunocompromised\" · อาจารย์ในราวด์: Gram ลบคิดเพิ่มในเบาหวาน ไตวาย มี UTI และผู้ภูมิคุ้มกันบกพร่อง\n\n"
        "- ceftriaxone อย่างเดียวพอสำหรับคนปกติ ไม่ครอบคลุม Pseudomonas ในผู้ป่วย neutropenia\n"
        "- ยากินและการรอผลเพาะเชื้อ = ช้าเกินไปในข้อติดเชื้อ (mortality 7–15%)\n"
        "- **Gram stain ลบไม่ตัด septic** · ห้ามฉีด steroid",
        "Neutropenia/ภูมิต่ำ + ข้อติดเชื้อ → anti-pseudomonal (สไลด์) · คนปกติ → ceftriaxone/cefotaxime", "Septic arthritis empiric", REF("Treatment empiric ATB p19") + REFR("Gram ลบในผู้ภูมิคุ้มกันบกพร่อง"),
        ["2.3.13-3(6)", "B5.2.2-3(1)"])],
}

# ═════════════════════════════════════════════════════════════════ callout ในหัวข้อเดิม
# (หัวข้อ, ข้อความ) — บรรทัดแรกขึ้นต้น "> **กิตติวรรณ · ชื่อ**" ใช้เป็นตัวระบุตอนถอดออกเมื่อรันซ้ำ
CALLOUTS = {
    "air-23-01": [("การเจาะน้ำไขข้อ (arthrocentesis)", """
> **กิตติวรรณ · เจาะข้อ** — ✍️ สไลด์ p12: **"present with acute mono → เจาะเพื่อ R/O septic! เสมอ!"** · ขั้นแรกแยก **hemarthrosis** (trauma · coagulopathy เช่น hemophilia · neuropathic arthropathy · tumor · CPPD arthropathy) แล้วใช้ **WBC > 2,000/mm³ = inflammatory** (✍️ "= inflame") · ไม่ถึง = non-inflammatory (OA, trauma, AVN) · ดู **color · volume · clarity (clear → turbid → pus-like) · viscosity (syrup = ปกติ · saline = ลดลง)** · ส่ง cell count · crystal · Gram + C/S (± AFB)
> ราวด์ 5 พ.ย.: **ความขุ่นกับความหนืดไม่ไปด้วยกัน** — ข้ออักเสบ **ขุ่น (WBC) แต่หนืดลดเหมือนน้ำเกลือ** · ตัวเลขที่อาจารย์ให้จำ: **2,000** (เส้นแบ่งอักเสบ) และ **> 50,000** (หนอง ยิ่งสูงยิ่งคิด septic) · กลุ่มนำเสนอเพิ่มวัตถุประสงค์ที่ 4 = **therapeutic aspiration** ลดแรงดันในข้อ · flowchart ของกลุ่ม: WBC > 5,000 → Gram stain · ถ้ารักษาเป็นเกาต์/CPPD โดยไม่มีข้อบ่งชี้ติดเชื้อ ให้ **ติดตามใน 24–48 ชั่วโมง** ไม่ดีขึ้นต้องเจาะซ้ำ
""")],
    "air-23-02": [("กลไก", """
> **กิตติวรรณ · urate homeostasis** — สไลด์ p26–p31: hyperuricemia **> 7 mg/dL (ชาย) · > 6 (หญิง)** · urate มาจากอาหาร + สร้างเอง ขับออก **ทางไต 60–70% · ลำไส้ 30–40%** (✍️ "สร้างมาก or ขับน้อย") · **งดอาหาร purine ลด urate ได้เพียง ~25%** · สร้างมากเกิน 10% (PRPP synthetase ทำงานเกิน · ขาด HGPRT — Lesch–Nyhan/Kelley–Seegmiller · GSD type 1 · ATP turnover สูง) vs **ขับน้อย 90%** (ไตเสื่อม · thiazide ciclosporin เหล้า aspirin ขนาดต่ำ · lactic/keto acidosis) · **hyperuricemia ≠ gout** มี 4 ระยะ · อาจารย์ให้ไปทบทวน basic science ของเอนไซม์ (PRPP synthetase, HGPRT, xanthine oxidase) เอง
"""), ("ภาพทางคลินิกและผลึก", """
> **กิตติวรรณ · ใครเป็นเกาต์** — สไลด์ p33: อายุเริ่ม **ชาย 40–60 ปี · หญิง > 60 ปี · เริ่มก่อน 25 ปี = atypical** (หาสาเหตุสร้างมากเกิน) · acute monoarthritis 90% (หรือ bursitis/tendinitis) ไข้ หนาวสั่นได้ · ประวัติ intermittent · **หายเองสนิท** · MTP1 เป็นในที่สุด ~90% · ตัวกระตุ้น (p47): บาดเจ็บ/เลือดออก/ติดเชื้อ · เหล้า · เครียด/ผ่าตัด · กินมาก · **หยุดยากะทันหัน** · นอนโรงพยาบาล (เสี่ยง 20%)
> ราวด์ 5 พ.ย.: **estrogen ช่วยขับ urate ทางปัสสาวะ** → ผู้หญิงเป็นเกาต์ **หลังหมดประจำเดือน** — "ผู้หญิงยังมีประจำเดือน acute monoarthritis **เขียนเกาต์จะโดนหักคะแนน**" · **ตั้งครรภ์ urate ต่ำ (GFR ↑) — สูง > 4 mg/dL คิด pre-eclampsia** (สไลด์ p26) · serum urate ปกติได้ **49%** ขณะกำเริบ (สไลด์ p39)
"""), ("รักษาช่วงกำเริบ — เลือกตามโรคร่วม ไม่ใช่ตามความชอบ", """
> **กิตติวรรณ · flare** — สไลด์ p46: **critical point = เริ่มรักษาภายใน 24 ชั่วโมง** + สอนผู้ป่วยให้เริ่มยาเองเมื่อรู้สึกว่ากำลังกำเริบ · การรักษาช่วงกำเริบแก้แค่อาการ **ผลึกยังอยู่ในข้อ** · p48: NSAIDs · **colchicine (ได้ผลดีถ้าเริ่มใน 36 ชั่วโมง)** · steroid เป็น first line ทั้งสามกลุ่ม · ACTH = second line
> กลุ่มนำเสนอ (เคสชาย 60 ปี): แบ่งความรุนแรงตาม pain score **≤ 4 mild · 5–6 moderate · ≥ 7 severe** → mild–moderate ใช้ยาเดี่ยว · **severe หรือหลายข้อใช้ร่วมกัน (เช่น colchicine + NSAID)** · ขนาดที่กลุ่มใช้: **colchicine 1.2 mg → 0.6 mg ใน 1 ชม. → 0.6 mg วันละ 1–2 ครั้งจนหาย** · **naproxen 500 mg วันละ 2 ครั้ง 5–7 วัน (+ PPI ถ้าเสี่ยง)** · **prednisolone 0.5 mg/kg/วัน 5–10 วัน** หรือฉีดเข้าข้อเมื่อเป็น 1–2 ข้อ **หลังตัดการติดเชื้อ** · ไม่ดีขึ้นใน 24 ชม. → เปลี่ยน/เพิ่มยา และ **ทบทวนเรื่องติดเชื้อ** · พักข้อ ยกสูง ประคบเย็น · ใช้ ULT อยู่แล้วให้กินต่อ
""")],
    "air-23-03": [("ใครควรเริ่มยาลดกรดยูริก (urate-lowering therapy, ULT)", """
> **กิตติวรรณ · ข้อบ่งชี้ ULT** — สไลด์ p51: **attack > 2 ครั้ง/6 เดือน หรือ > 3 ครั้ง/ปี · tophi · chronic gouty arthritis · นิ่ว · ป้องกัน tumor lysis** · กลุ่มนำเสนอใช้ตามแนวทางสากล: **tophus · flare ≥ 2 ครั้ง/ปี** (strong) และ **flare ครั้งเดียวร่วมกับ CKD ≥ stage 3 · urate > 9 · นิ่ว** (conditional — ACR 2020; ในไฟล์เสียงถอดคำว่า "นิ่ว" ผิดเป็น "angina")
> ราวด์ 5 พ.ย.: อาจารย์ให้ไปอ่าน **แนวทางเวชปฏิบัติโรคเกาต์ภาษาไทยสำหรับแพทย์ทั่วไปที่เพิ่งออกปีนี้ — "มีสิทธิ์ออกข้อสอบ"** (เนื้อหาแนวทางฉบับนั้นไม่ได้อยู่ในสไลด์และไฟล์เสียง — ต้องอ่านเพิ่มเอง)
"""), ("หลักการใช้ยา", """
> **กิตติวรรณ · ยาลดกรดยูริก** — สไลด์ p52: **เป้า < 6 mg/dL · ใช้ตลอดชีวิต** (หยุด ๆ กิน ๆ → flare และ hypersensitivity) · อาจารย์: "**จำตัวเดียว 6** ไม่ขึ้นกับขนาดยา" · มี tophus ต่ำกว่า 5 ละลายเร็วขึ้น · "**อย่าลืม prophylaxis**" และเริ่มยาแบบไม่เร่ง (อาจารย์ใช้คำว่า delay loading agent)
> **Allopurinol** (p54): purine analogue → oxypurinol · **เริ่ม 100 mg/วัน (50 mg ถ้า GFR ต่ำ) ปรับทุก 2–5 สัปดาห์ สูงสุด 800 mg** · AR: transaminitis eosinophilia · **allopurinol hypersensitivity syndrome 1:1,000 ตาย 20–25%** (SJS/TEN eosinophilia vasculitis) ส่วนใหญ่ในไม่กี่เดือนแรก · ปัจจัยเสี่ยง **HLA-B5801 (คนไทย 6–8%) · ไตเสื่อม · thiazide** → ตรวจ HLA-B5801 ก่อนเริ่ม · **Febuxostat** (p55): non-purine XOI ไม่ต้องปรับขนาดในไตเสื่อมและตับเสื่อมเล็กน้อย–ปานกลาง · **Uricosuric** (p53): probenecid sulfinpyrazone benzbromarone · ฤทธิ์อ่อน **losartan fenofibrate** · เหมาะเมื่อ **อายุ < 60 · CrCl > 80 · ไม่มีนิ่ว · urine uric acid 24 ชม. < 800 mg** + ดื่มน้ำ ≥ 1.5 L/วัน + ทำปัสสาวะให้เป็นด่าง · **Uricase** (p56): urate → allantoin ระวัง immunogenicity hemolysis methemoglobinemia
"""), ("เกาต์เรื้อรังและ tophus", """
> **กิตติวรรณ · tophaceous gout** — สไลด์ p35–p36: intercritical gout ช่วงปลอดอาการ **สั้นลงเรื่อย ๆ** และพบผลึกในข้อที่ไม่มีอาการได้ · **chronic tophaceous gout เกิดหลัง hyperuricemia เฉลี่ย 11.6 ปี** → ปวดบวมฝืดต่อเนื่อง **polyarthritis เลียน RA หรือ PsA** ภาพรังสีผิดปกติบ่อย (เทียบ MCQ หญิง 76 ปีกิน thiazide) · กลุ่มนำเสนอ: ภาวะแทรกซ้อน tophus ข้อผิดรูป urate nephropathy AKI บน CKD นิ่ว · ตา (conjunctivitis uveitis scleritis) พบน้อย · **ไทย: เกาต์พบไม่มาก แต่ hyperuricemia พบมาก**
""")],
    "air-23-04": [("ที่อาจารย์เน้นในสไลด์", """
> **กิตติวรรณ · CPPD ในราวด์ 5 พ.ย.** — อาจารย์: แยก gout กับ pseudogout ด้วย intermittent **ไม่ได้** ต้อง **เจาะดูผลึก** · อายุช่วยได้: **pseudogout 70–80 ปี** (✍️ "Pseudogout ⇒ แก่กว่า") · กลุ่มนำเสนอ: เข่า (บ่อยสุด) ข้อมือ ไหล่ สะโพก · metabolic: hemochromatosis hyperparathyroidism hypomagnesemia hypophosphatasia · X-ray **chondrocalcinosis** (เส้นขาวในกระดูกอ่อนเข่า) · US เห็นผลึก **กลางเนื้อกระดูกอ่อน** (เทียบ double contour ของเกาต์ที่ผิวกระดูกอ่อน) · สไลด์ p11 จัด CPPD เป็นทั้ง acute และ chronic inflammatory mono/oligoarthritis และ **CPPD arthropathy เป็นสาเหตุหนึ่งของ hemarthrosis** (p12) · กลุ่มเขียน "หญิง > ชาย" — แต่ละแหล่งยังไม่ตรงกัน
""")],
    "air-23-04b": [("Basic calcium phosphate (BCP / hydroxyapatite)", """
> **กิตติวรรณ · ผลึกที่อาจารย์ถามในห้อง** — นอกจากเกาต์และ pseudogout: **oxalate** และ **hydroxyapatite = basic calcium phosphate (ชื่อเดียวกัน)** → มาด้วย **calcific tendinitis** "อยู่ ๆ เจ็บเอ็นขึ้นมา" — ผลึกทั้งหมดนี้ให้ pattern **intermittent** (✍️ สไลด์ p9 "crystal → Basic CaPO4") · ตารางผลึก 6 ชนิดดูหัวข้อ "ผลึก 6 ชนิดในน้ำไขข้อ"
""")],
    "air-23-05": [("ที่อาจารย์เน้นในสไลด์", """
> **กิตติวรรณ · septic arthritis (สไลด์ p13–p24)** — acute monoarthritis เป็นส่วนใหญ่ แต่ **10% มาเป็น polyarthritis** · **medical emergency ตาย 7–15%** · มักมีโรคข้อเดิม (RA OA) · ข้อที่พบ: **เข่า 55%** ข้อเท้า 10% ข้อมือ 9% ไหล่ 7% สะโพก/SC/ศอก 5% SI/เท้า 2% · ทางเข้า: กระแสเลือด · จาก osteomyelitis · เนื้อเยื่อข้างเคียง · หัตถการ · แผลทะลุ
> **ผลตรวจ**: SF Gram stain บวก **50–75% (Gram บวก) · < 50% (Gram ลบ)** · SF culture **70–90%** · hemoculture **40–50%** และ **10% บวกแค่ hemoculture** · เก็บใน sterile tube (EDTA/heparin) หรือขวด H/C · ทำ septic work-up อื่น (UA, urine Gram, U/C) แล้ว **เริ่มยาทันที** · procalcitonin · PCR (16S) เมื่อเพาะไม่ขึ้นแต่สงสัยมาก
> **ยา**: normal host **ceftriaxone หรือ cefotaxime** · ภูมิคุ้มกันบกพร่อง/sepsis/ช็อก/neutropenia/bacteremia/burn → **anti-pseudomonal 1–2 ตัว** แล้วปรับตาม C/S (ถ้า Gram stain เห็น GPC เป็นกลุ่มให้คลุม S. aureus ตามหัวข้อนี้) · **IV อย่างน้อย 2 สัปดาห์ รวม 2–6 สัปดาห์** · ไม่ตอบสนองใน **5 วัน** → เจาะเพาะซ้ำ + หาผลึกซ้ำ · สงสัยเชื้อรา/วัณโรค → synovial biopsy · นึกถึง reactive arthritis · X-ray/MRI หา osteomyelitis · **surgical drainage** เมื่อเข็ม/arthroscopy ระบายไม่พอ · effusion ยังอยู่หลังเจาะซ้ำ 7 วัน · สงสัยสิ่งแปลกปลอม
> **พยากรณ์แย่** (p21): สูงอายุ · ข้อเดิมผิดปกติ (RA OA gouty tophi) · ข้อเทียม · วินิจฉัยช้า · > 3 ข้อ/ข้อเล็กมือ · bacteremia · S. aureus/P. aeruginosa · ยากดภูมิ · โรคตับ ไต หัวใจ · WBC สูงแรกรับ · ไตแย่ลง

| กลุ่มผู้ป่วย | เชื้อที่ต้องนึกถึง (สไลด์ p15–p16 + ราวด์) |
|---|---|
| ข้อปกติ (naive) — ทั่วไป | **S. aureus 40–60%** · streptococci ~20–30% (สไลด์เขียนเป็น S. pneumoniae) · β-hemolytic strep กลุ่ม A G B |
| วัยมีเพศสัมพันธ์ | **N. gonorrhoeae** — อาจารย์: ดูอายุและประวัติ แต่ "**เด็ก 18 ปฏิเสธเพศสัมพันธ์ เจาะเข่าเจอ GC**" — ในโจทย์ไม่หลอก ชีวิตจริงหลอก |
| อายุ > 60 ปี หรือมีปัจจัยเสี่ยง | **Enterobacteriaceae เช่น Salmonella** |
| เบาหวาน ไตวาย UTI ภูมิคุ้มกันบกพร่อง | **Gram ลบเพิ่มขึ้น** (✍️ "Gram −ve: immunocompromised") · อาจารย์เตือนเชื้อ Gram ลบที่มากับ **น้ำจืด/ดิน** *(ตีความจากไฟล์เสียง)* |
| ข้อเทียม | **coagulase-negative staphylococci (S. epidermidis)** · S. aureus |
| พบน้อย | Pseudomonas · TB · H. influenzae · N. meningitidis · Pasteurella (สัตว์กัด) · anaerobes · Mycoplasma · เชื้อรา · Borrelia |
""")],
    "air-23-06": [("ภาพทางคลินิก", """
> **กิตติวรรณ · OA ในราวด์** — **OA ชื่อลงท้าย -itis แต่เป็น non-inflammatory (degenerative)** · ฝืดเช้าได้แต่ **ขยับ 2–3 นาที ไม่เกิน ~5 นาที** ดีขึ้น (✍️ สไลด์ p5 "morning 3–5 min") · **spondylosis = OA ของ C-spine และ L-spine** · ที่มือ **PIP + DIP โดยไม่มี MCP → OA** (สไลด์ p8) · สไลด์ p11 จัด non-inflammatory polyarthritis เรื้อรัง: OA · hemochromatosis · ochronosis · hypertrophic osteoarthropathy · amyloidosis · acromegaly
""")],
    "air-23-07": [("Reactive arthritis", """
> **กิตติวรรณ · reactive arthritis อยู่ในกลุ่ม SNSA** — enthesitis และ dactylitis เจอใน ReA PsA IBD-associated · HLA-B27 (ReA ~85% — สไลด์ p76) · ผื่น **keratoderma blennorrhagicum** ที่ฝ่ามือฝ่าเท้า (สไลด์ p80) · ในเคสชาย 60 ปีกลุ่มนำเสนอ **ตัด ReA เพราะไม่มีประวัติติดเชื้อทางเดินอาหารหรือทางเดินปัสสาวะ-สืบพันธุ์** · ภาพรวม SpA ดูหัวข้อ "SLE arthritis และ spondyloarthritis"
""")],
    "air-23-08": [("วินิจฉัย", """
> **กิตติวรรณ · RA กับหลัง** — ✍️ สไลด์ p8 **"RA ⇒ ปวด lower back ⇒ osteoporosis"** · อาจารย์: RA มี axial แค่ C1–C2 ถ้าโจทย์เป็น RA แล้วปวดหลังส่วนล่าง **ไม่ใช่ RA active แต่เป็นกระดูกพรุน/กระดูกหักจากกระดูกพรุน** (อักเสบเรื้อรัง + steroid + ขยับน้อย)
""")],
}

# ภาพจริงในหัวข้อเดิม: (หัวข้อ, key, ข้อมูล) — marker วางท้ายหัวข้อนั้น
OLD_IMGS = {
    "air-23-03": [("เกาต์เรื้อรังและ tophus", "art-tophi",
                   img("art-10-tophaceous-hands", "Chronic tophaceous gout ที่มือ",
                       "ภาพหลังมือทั้งสองข้างมีก้อนนูนสีเหลืองขาวหลายก้อนรอบข้อนิ้ว ทำให้นิ้วผิดรูปไม่สมมาตร",
                       cap="ก้อน **tophus** หลายก้อนรอบข้อนิ้วสองมือ **ไม่สมมาตร** — chronic tophaceous gout เป็น polyarthritis เลียน RA ได้ (สไลด์ p36: hyperuricemia เฉลี่ย 11.6 ปี) · ต่างจาก RA ตรงที่ก้อนแข็งสีเหลืองขาวและอาจแตกมีสารขาวเหมือนชอล์ก"))],
}


# ═════════════════════════════════════════════════════════════════ MEQ · OSCE
LECTURE_NAME = "Approach to arthritis / crystal and infective arthropathy"
MEQ = {
    "id": P + "MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECTURE_NAME,
    "topic": "Acute monoarthritis with fever — septic vs crystal (เคสราวด์ 5 พ.ย.)",
    "vignette": ("ผู้ป่วยชายไทยอายุ 60 ปี มาด้วยไข้และปวดข้อเท้าขวา 2 วัน\n"
                 "PI: 2 วันก่อนตื่นนอนตอนเช้ามีปวดข้อเท้าขวา บวม แดง ร้อน ปวดมากที่สุดภายในวันแรกจนลงน้ำหนักไม่ได้ มีไข้ร่วม 1 ปีก่อนเคยปวดบวมเข่าขวา ซื้อยาแก้ปวดกินเองหายใน 1 สัปดาห์ "
                 "ดื่มเหล้าตามงานสังคม เคยถูกบอกว่าความดันสูงแต่ไม่ได้รักษา ไม่มีประวัติบาดเจ็บ ไม่มีท้องเสียหรือปัสสาวะแสบขัดก่อนหน้า\n"
                 "PE: BT 38.5 °C, BP 150/90 mmHg, PR 90/min, BMI 30 kg/m²\n"
                 "Right ankle: marked swelling, tender, warm, erythema, limited ROM in all directions ทั้ง active และ passive · ข้ออื่นปกติ · ผิวหนังเหนือข้อไม่มีแผลหรือ cellulitis · ไม่พบ tophus\n"
                 "Lab: Hb 13.5 g/dL, WBC 12,000/µL (PMN 90%), Plt 210,000/µL · UA: protein neg, RBC 5–10/HPF, WBC 0–1/HPF · "
                 "BUN 14 mg/dL, Cr 1.01 mg/dL (eGFR ~85) · uric acid 9.5 mg/dL · Chol 230, TG 200, HDL 35, LDL 155 mg/dL"),
    "questions": [
        {"q": "1. จงเขียน problem list และการวินิจฉัยแยกโรค 3 อันดับแรกพร้อมเหตุผล (3 คะแนน)",
         "a": "**Problem list**: acute monoarthritis ข้อเท้าขวา 2 วันร่วมกับไข้ · ประวัติปวดเข่าขวาที่หายเอง (intermittent?) · metabolic syndrome (อ้วน ความดันสูงไม่รักษา dyslipidemia hyperuricemia) · microscopic hematuria\n"
              "1) **Septic arthritis** (ต้องคิดก่อน) — ไข้ 38.5 WBC 12,000 PMN 90% ข้อเดียว rapid onset 1–2 วัน จำกัดการขยับทุกทิศ · ตายได้ 7–15%\n"
              "2) **Acute gouty arthritis** — ชาย 60 ปี อ้วน ดื่มเหล้า urate 9.5 เคยมีข้ออักเสบที่หายเอง · ข้อเท้าเป็นตำแหน่งที่พบบ่อย · ไข้และ WBC สูงได้จาก IL-1β\n"
              "3) **CPPD (pseudogout)** — อายุ > 60 ปี ข้ออักเสบเฉียบพลันข้อเดียว (แต่มักเป็นเข่า/ข้อมือ)\n"
              "(ตัด reactive arthritis เพราะไม่มีประวัติติดเชื้อทางเดินอาหาร/ปัสสาวะ · trauma ไม่มีประวัติ)"},
        {"q": "2. การตรวจที่สำคัญที่สุดลำดับแรกคืออะไร จะส่งตรวจอะไรบ้าง และต้องทำอะไรก่อนให้ยาปฏิชีวนะ (4 คะแนน)",
         "a": "**Arthrocentesis ข้อเท้าขวา** (ผิวหนังไม่มี cellulitis จึงแทงผ่านได้) — อาจารย์: \"acute monoarthritis สิ่งแรกที่ต้องทำคือเจาะข้อ ไม่ใช่แค่ NSAID\"\n"
              "ส่ง: 1) **cell count + differential** 2) **Gram stain** 3) **culture** (sterile tube/ขวด H/C) 4) **crystal ด้วย polarized microscope** + ดู color clarity viscosity\n"
              "ก่อนยาปฏิชีวนะ: **hemoculture 2 ชุด** + septic work-up อื่น (UA, U/C) — แล้ว **เริ่ม empirical ATB ทันทีถ้าสงสัย septic** ไม่ต้องรอผลเพาะเชื้อ\n"
              "อื่น ๆ: X-ray ข้อเท้า (baseline · ตัด fracture/osteomyelitis) · ESR/CRP"},
        {"q": "3. ผลน้ำไขข้อ: ขุ่นเหลือง ความหนืดลดลง WBC 35,000/µL PMN 85% พบผลึกรูปเข็มในเซลล์ สีเหลืองเมื่อขนานแกน compensator · Gram stain ไม่พบเชื้อ — จงแปลผลและบอกว่าตัด septic arthritis ได้หรือยัง (3 คะแนน)",
         "a": "- **Inflammatory fluid** (WBC 2,000–50,000 · ขุ่นแต่หนืดลด)\n"
              "- **ผลึก MSU** (เข็ม · negative birefringence · ขนานเหลือง) อยู่ในเซลล์ = **acute gouty arthritis**\n"
              "- **ยังตัด septic ไม่ได้** จนกว่า culture จะลบ — Gram stain sensitivity เพียง 50–75% และ **crystal + septic อยู่ข้อเดียวกันได้** · WBC < 50,000 ทำให้นึกถึงเกาต์มากกว่า แต่ถ้า WBC สูงมาก (เช่น 80,000) หรืออาการแย่ลงให้ยาปฏิชีวนะแม้เจอผลึก · ติดตามใน 24–48 ชั่วโมง"},
        {"q": "4. ถ้าโรงพยาบาลนี้เจาะข้อไม่ได้ จงคำนวณ clinical prediction rule ของเกาต์ (Janssens) และแปลผล (3 คะแนน)",
         "a": "ชาย **2** · เคยมีข้ออักเสบมาก่อน **2** · ถึงขีดสุดภายใน 1 วัน **0.5** · ข้อแดง **1** · MTP1 **0** (ครั้งนี้เป็นข้อเท้า) · ความดันสูง **1.5** · urate > 5.88 **3.5** → **รวม 10.5 = ≥ 8 → high probability (~80%)**\n"
              "แต่ **rule นี้ไม่ได้ใช้ตัด septic arthritis** — ผู้ป่วยมีไข้และ WBC สูง ต้องส่งต่อเพื่อเจาะข้อ/ให้ยาปฏิชีวนะตามความเสี่ยง · (กลุ่มนำเสนอในราวด์ให้ตัวแปรแค่ 6 ข้อ ลืม **เพศชาย 2 คะแนน**)"},
        {"q": "5. เมื่อตัดการติดเชื้อแล้ว จงสั่งยารักษา gout flare ครั้งนี้ (eGFR ~85) พร้อมเหตุผล (4 คะแนน)",
         "a": "เริ่มให้เร็ว **ภายใน 24 ชั่วโมง** · พักข้อ ยกสูง ประคบเย็น\n"
              "- **Colchicine low dose** 1.2 mg แล้ว 0.6 mg ใน 1 ชั่วโมง ต่อด้วย 0.6 mg วันละ 1–2 ครั้งจนหาย (ได้ผลดีถ้าเริ่มใน 36 ชั่วโมง · ไตปกติใช้ขนาดปกติได้ · ผลข้างเคียงท้องเสีย · ระวังยาที่ยับยั้ง CYP3A4/P-gp)\n"
              "- และ/หรือ **NSAID** เช่น naproxen 500 mg วันละ 2 ครั้ง 5–7 วัน + PPI ถ้าเสี่ยง (ระวังความดันสูง)\n"
              "- ถ้าใช้ไม่ได้: **prednisolone 0.5 mg/kg/วัน 5–10 วัน** หรือฉีดเข้าข้อเมื่อแน่ใจว่าไม่ติดเชื้อ\n"
              "ปวดรุนแรง (pain ≥ 7) อาจใช้ colchicine + NSAID ร่วมกัน · ไม่ดีขึ้นใน 24 ชั่วโมง → เพิ่ม/เปลี่ยนยาและทบทวนเรื่องติดเชื้อ · **ยังไม่เริ่ม allopurinol ระหว่างกำเริบโดยไม่มีแผน**"},
        {"q": "6. หลังหายจาก flare ผู้ป่วยถามว่าต้องกินยาลดกรดยูริกตลอดชีวิตหรือไม่ จงวางแผนระยะยาว (3 คะแนน)",
         "a": "- ข้อบ่งชี้: เป็นครั้งที่ 2 ใน 1 ปี (ยังไม่ถึงเกณฑ์สไลด์ > 2 ครั้ง/6 เดือน หรือ > 3 ครั้ง/ปี) แต่มี **urate > 9 และ microscopic hematuria ที่ต้องตรวจหานิ่ว** — ถ้าพบนิ่วหรือกำเริบซ้ำ → เริ่ม ULT (ACR 2020: flare ≥ 2 ครั้ง/ปี tophus → strong · นิ่ว/urate > 9/CKD ≥ 3 → conditional)\n"
              "- ถ้าเริ่ม: **ตรวจ HLA-B5801 ก่อน allopurinol** · เริ่ม 100 mg/วัน ปรับทุก 2–5 สัปดาห์ · **เป้า urate < 6 mg/dL** · **prophylaxis colchicine ขนาดต่ำ 3–6 เดือน** · ใช้ต่อเนื่องตลอดชีวิต\n"
              "- ไม่ใช้ยา: ลดน้ำหนัก ลดเหล้า เลี่ยงเนื้อแดง เครื่องใน อาหารทะเล น้ำหวานฟรุกโตส · ดื่มน้ำมาก\n"
              "- โรคร่วม: รักษาความดันด้วย **losartan** (uricosuric) เลี่ยง thiazide · คุมไขมัน · US KUB หา urate stone"},
    ],
    "ref": REFR("เคสชาย 60 ปี acute monoarthritis ของกลุ่ม 6ก/6ข") + ["สไลด์เคส ARTHRITIS กลุ่ม 19B/20B — lab sheet p25"],
    "nl": ["2.1.27", "2.3.13(2)", "2.3.13-3(6)", "B5.3(3)", "B5.4(4)"], "years": [],
}

OSCE = {
    "id": P + "OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECTURE_NAME,
    "topic": "นำเสนอผู้ป่วยหลายข้อด้วย I-I-N-O-D-E และคิดคะแนน ACR/EULAR 2010",
    "station": "OSCE นำเสนอผู้ป่วย/ตอบปากเปล่า 7 นาที",
    "instruction": ("หญิงไทยอายุ 34 ปี ปวดบวมข้อมือทั้งสองข้าง ข้อนิ้ว PIP ทุกนิ้วของทั้งสองมือ และเข่าทั้งสองข้าง มา 4 เดือน ปวดมากที่สุดตอนตื่นนอนและฝืดนานราว 1 ชั่วโมง "
                    "เบื่ออาหาร น้ำหนักลด 4 กก. ใน 3 เดือน · ตรวจ: ข้อมือ tender swelling warmth · PIP ทุกนิ้ว tender swelling · เข่าสองข้าง tender swelling warm ballottement บวก · "
                    "จำกัด ROM ทั้ง active และ passive · ระบบอื่นปกติ\n\n"
                    "1) จงสรุปผู้ป่วยรายนี้ตามกรอบ I-I-N-O-D-E ทีละตัวอักษร (6 คะแนน)\n"
                    "2) บอกการวินิจฉัยแยกโรค 3 โรคที่ต้องคิด และโรคที่ตัดออกได้เพราะอะไร (2 คะแนน)\n"
                    "3) คิดคะแนน ACR/EULAR 2010 จากข้อมูลที่มีตอนนี้ และบอกว่าจะส่งแล็บอะไรต่อเพื่ออะไร (4 คะแนน)\n"
                    "4) ผู้ป่วยถามว่าจะใช้ยาอะไรและต้องระวังอะไร — ตอบสั้น ๆ (3 คะแนน)"),
    "answer": ("| ข้อ | สิ่งที่ต้องพูด | คะแนน |\n|---|---|---|\n"
               "| **I** intra/extra | เจ็บและจำกัดทั้ง **active และ passive** · บวมรอบข้อ effusion (ballottement) → **intra-articular** | 1 |\n"
               "| **I** inflammatory | ร้อน บวม **ฝืดเช้า ~60 นาที (> 30)** · น้ำหนักลด เบื่ออาหาร → **inflammatory** | 1 |\n"
               "| **N** number | ข้อมือ 2 + PIP 8 + เข่า 2 = **12 ข้อ → polyarthritis** | 1 |\n"
               "| **O** onset/pattern | insidious **4 เดือน ≥ 6 สัปดาห์ → chronic** (ซักต่อว่า additive ไหม) | 1 |\n"
               "| **D** distribution | **สมมาตร** ข้อเล็ก (MCP?/PIP ข้อมือ) + เข่า · **ไม่มี DIP** · peripheral | 1 |\n"
               "| **E** extra-articular | ซักหา sicca nodule ผื่น แผลปาก ผมร่วง แพ้แสง ตาแดง ปวดหลัง สะเก็ดเงิน ท้องเสีย ปัสสาวะผิดปกติ — ตอนนี้ปกติ | 1 |\n"
               "| DDx | **RA (มากที่สุด) · SLE · crystal (polyarticular tophaceous)** · ตัด SpA ได้เพราะไม่มีปวดหลังอักเสบและเป็นแบบสมมาตรข้อเล็ก | 2 |\n"
               "| ACR/EULAR | **> 10 ข้อมีข้อเล็ก = 5 · ≥ 6 สัปดาห์ = 1 → 6 = เข้าเกณฑ์ RA ได้แล้ว** (serology/APR ยัง 0) | 2 |\n"
               "| แล็บต่อ | **RF · anti-CCP** (พยากรณ์ + คะแนน) · **ESR/CRP** · **ANA** (ลบ → ตัด SLE) ± anti-dsDNA C3/C4 · CBC LFT Cr (ก่อน MTX) · **X-ray มือ/เท้า** หา erosion · HBV HCV · CXR | 2 |\n"
               "| ยา | **MTX สัปดาห์ละครั้ง + folic acid** (ห้ามตั้งครรภ์ · คุมกำเนิด) ± HCQ/SSZ · **steroid ขนาดต่ำเป็น bridge** · ระวังตับ เม็ดเลือด ปอดอักเสบจาก MTX · ถ้าต้องใช้ anti-TNF ต้องคัดกรอง **TB** ก่อน · เลิกบุหรี่ | 3 |\n\n"
               "**จุดที่ผู้คุมสอบให้ตก**: ไม่บอก duration ของ morning stiffness · นับเข่าเป็นข้อเล็ก · บอกว่าต้องรอ RF ก่อนจึงวินิจฉัยได้ · ลืม ANA เพื่อตัด SLE ในหญิงวัยเจริญพันธุ์"),
    "ref": ["สไลด์เคส ARTHRITIS กลุ่ม 19B/20B — เคสหญิง 34 ปี + 2010 ACR/EULAR scoring"] + REFR("กรอบ I-I-N-O-D-E"),
    "nl": ["2.1.27", "2.3.13-3(12)", "B5.3(5)", "B5.4(3)"], "years": [],
}

# ═════════════════════════════════════════════════════════════════ ตำแหน่งหัวข้อใหม่ (เรียงตามลำดับที่ต้องแทรก)
PLACE = [("air-23-art-01", "before", "air-23-01"), ("air-23-art-02", "after", "air-23-art-01"),
         ("air-23-art-03", "after", "air-23-02"), ("air-23-art-04", "after", "air-23-03"),
         ("air-23-art-05", "after", "air-23-05"), ("air-23-art-06", "after", "air-23-art-05"),
         ("air-23-art-07", "after", "air-23-art-06")]

OBJECTIVES = [
    "ใช้กรอบ I-I-N-O-D-E ของ อ.กิตติวรรณ (in/extra · inflammatory · number · onset/pattern · distribution · extra-articular) ซักประวัติ ตรวจร่างกาย และนำเสนอผู้ป่วยปวดข้อ",
    "คิดคะแนน ACR/EULAR 2010 จากเคสจริง อธิบายกลไก RA ตั้งแต่ citrullination ถึง erosion และบอกพิษของ DMARD/biologic/JAK ที่ออกสอบ",
    "แยก SLE arthritis และ spondyloarthritis ออกจาก RA และจำแนกผลึก 6 ชนิดในน้ำไขข้อ",
]
GUIDES = [
    "**สไลด์ อ.กิตติวรรณ สุเมธกุล — Approach to Arthritis (Lec 2.1 · ศ. 2 ต.ค. 2569 · 81 หน้า)** และ **ราวด์ข้างเตียง 5 พ.ย. 2569** (สไลด์เคส ARTHRITIS กลุ่ม 19B/20B + ไฟล์เสียง 2 ไฟล์) — โน้ต slides/arthritis_notes.md",
    "**2010 ACR/EULAR RA classification criteria** (Aletaha et al. Ann Rheum Dis 2010) · **ACR 2021 / EULAR 2022 RA management** — treat to target, MTX anchor, คัดกรอง TB/HBV ก่อน biologic",
    "**Janssens et al. Arch Intern Med 2010** — clinical diagnostic rule for gout (7 ตัวแปร รวม 13 คะแนน)",
    "**ACR 2020 Gout guideline** — ข้อบ่งชี้ ULT · เป้า < 6 · HLA-B5801 ก่อน allopurinol ในคนเชื้อสายเอเชียตะวันออกเฉียงใต้ · prophylaxis 3–6 เดือน · อาจารย์แนะนำแนวทางเวชปฏิบัติโรคเกาต์ภาษาไทยสำหรับแพทย์ทั่วไปฉบับปีนี้",
]
SUBTITLE_ADD = " · สไลด์ อ.กิตติวรรณ (ศ. 2 ต.ค.) + ราวด์ข้างเตียง 5 พ.ย.: I-I-N-O-D-E · RA · SLE/SpA · ผลึก 6 ชนิด · gout prediction rule"
DATE = "ศ. 2 ต.ค."
NLGAP = ("รหัส นล. ครอบคลุมโรคหลักของคาบนี้ (2.1.27 · 2.3.13 crystal/OA/infective/RA/SpA/SLE · B5.3 · B5.4) — "
         "ส่วนที่ไม่มีรหัสเฉพาะ: palindromic rheumatism · clinical prediction rule ของเกาต์ · รายละเอียด biologic/JAK (นับอยู่ใต้ B5.4(3) DMARD) "
         "→ อิงสไลด์ อ.กิตติวรรณ ราวด์ 5 พ.ย. และแนวทางใน guidelines")


# ═════════════════════════════════════════════════════════════════ apply
CALLOUT_RE = re.compile(r"^> \*\*กิตติวรรณ · [^*]+\*\*")
MY_MARK = re.compile(r"^\s*\[\[(?:anim|img):art-[\w-]+\]\]\s*$")


def strip_mine(md):
    """ถอด callout '> **กิตติวรรณ · …**' (+ ตารางที่ตามมาติดกัน) และ marker [[anim:art-*]] [[img:art-*]] ที่สคริปต์นี้เคยใส่"""
    out, skip = [], False
    for ln in md.split("\n"):
        if CALLOUT_RE.match(ln):
            skip = True
            continue
        if skip and (ln.startswith(">") or ln.startswith("|") or not ln.strip()):
            continue
        skip = False
        if MY_MARK.match(ln):
            continue
        out.append(ln)
    md = "\n".join(out)
    while "\n\n\n" in md:
        md = md.replace("\n\n\n", "\n\n")
    return md.strip()


def insert_block(md, after, block):
    new, ok = _insert_marker(md, after, block.strip())
    assert ok, ("ไม่พบหัวข้อ", after)
    while "\n\n\n" in new:
        new = new.replace("\n\n\n", "\n\n")
    return new


def apply(data):
    L = next(x for x in data if x["lec"] == LEC)
    secs = L["sections"]
    my_ids = set(NEW)
    keep = {s["id"]: s for s in secs if s["id"] in my_ids}
    secs = [s for s in secs if s["id"] not in my_ids]
    for sid, how, ref in PLACE:
        s = json.loads(json.dumps(NEW[sid]))
        old = keep.get(sid, {})
        if old.get("figs"):
            s["figs"] = old["figs"]
        s["anims"] = {k: v for k, v in (old.get("anims") or {}).items() if not k.startswith("art-")}
        s["mnem"] = [m for m in (old.get("mnem") or []) if m.get("name") not in {x["name"] for x in AN.MNEM}]
        oi = {k: v for k, v in (old.get("imgs") or {}).items() if k not in (s.get("imgs") or {})}
        if oi:
            s.setdefault("imgs", {}).update(oi)
        i = next(j for j, x in enumerate(secs) if x["id"] == ref)
        secs.insert(i if how == "before" else i + 1, s)
    byid = {s["id"]: s for s in secs}
    # หัวข้อเดิม: callout · ภาพจริง · source
    for sid, s in byid.items():
        if sid in my_ids:
            continue
        md = strip_mine(s["md"])
        for head, block in CALLOUTS.get(sid, []):
            md = insert_block(md, head, block)
        for head, key, d in OLD_IMGS.get(sid, []):
            md = insert_block(md, head, "[[img:%s]]" % key)
            s.setdefault("imgs", {})[key] = d
        s["md"] = md
        if sid in CALLOUTS and SRC_TAG not in (s.get("source") or ""):
            s["source"] = (s.get("source") or "สร้างจากคลังข้อสอบ") + SRC_TAG
    # ข้อใหม่ในหัวข้อเดิม (แทนที่ด้วย id)
    for sid, its in OLD_ITEMS.items():
        s = byid[sid]
        ids = {i["id"] for i in its}
        s["items"] = [i for i in s["items"] if i["id"] not in ids] + json.loads(json.dumps(its))
    # ภาพเคลื่อนไหว
    for it in AN.ITEMS:
        s, a = byid[it["sec"]], it["anim"]
        s.setdefault("anims", {})[a["key"]] = {k: a[k] for k in ("title", "svg", "steps")}
        mk = "[[anim:%s]]" % a["key"]
        if it["after"] is None:
            assert mk in s["md"], (it["sec"], mk)
        else:
            s["md"] = insert_block(s["md"], it["after"], mk)
    # หลักจำ (แทนที่ด้วยชื่อ)
    names = {m["name"] for m in AN.MNEM}
    for s in secs:
        if s.get("mnem"):
            s["mnem"] = [m for m in s["mnem"] if m.get("name") not in names]
    for m in AN.MNEM:
        byid[m["sec"]].setdefault("mnem", []).append({x: m[x] for x in ("name", "what", "lines", "note", "src") if m.get(x)})
    for s in secs:
        if "mnem" in s and not s["mnem"]:
            del s["mnem"]
        if "anims" in s and not s["anims"]:
            del s["anims"]
    L["sections"] = secs
    # MEQ / OSCE (แทนที่ด้วย id · ใช้ _kind/_set ตามรายการเดิม)
    for key, obj in (("meq", MEQ), ("osce", OSCE)):
        lst = L.setdefault(key, [])
        o = json.loads(json.dumps(obj))
        if lst:
            for f in ("_kind", "_set"):
                if f in lst[0]:
                    o[f] = lst[0][f]
        L[key] = [x for x in lst if x["id"] != o["id"]] + [o]
    # ระดับคาบ
    L["date"] = DATE
    if SUBTITLE_ADD.strip(" ·") not in L["subtitle"]:
        L["subtitle"] = L["subtitle"] + SUBTITLE_ADD
    for o in OBJECTIVES:
        if o not in L["objectives"]:
            L["objectives"].append(o)
    if not L.get("nlGap"):
        L["nlGap"] = NLGAP
    g = L.setdefault("guidelines", [])
    for x in GUIDES:
        if x not in g:
            g.append(x)
    return L


# ═════════════════════════════════════════════════════════════════ index.json (intro/howto ของชุด air)
INTRO_OLD = "เนื้อหาของคาบ 23 และ 33 เสริมด้วยสิ่งที่อาจารย์เน้นในสไลด์บรรยาย"
INTRO_NEW = ("เนื้อหาของคาบ 23 และ 33 เสริมด้วยสิ่งที่อาจารย์เน้นในสไลด์บรรยาย · คาบ 23 (Approach to arthritis) อัปเดตตามสไลด์จริงของ อ.กิตติวรรณ (ศ. 2 ต.ค.) "
             "และราวด์ข้างเตียง 5 พ.ย. — เริ่มจากกรอบ I-I-N-O-D-E แล้วต่อด้วย RA, SLE/SpA, ผลึก 6 ชนิด และ gout prediction rule")
HOWTO_ADD = ("\n\nคาบ 23 แนะนำให้เรียนตามลำดับในหน้า: **I-I-N-O-D-E → รูปแบบข้อบอกโรค → น้ำไขข้อ → เกาต์ → ผลึก → septic → RA → ยา RA → SLE/SpA** · "
             "กล่องที่ขึ้นต้นว่า **กิตติวรรณ ·** คือสิ่งที่สไลด์หรือราวด์ 5 พ.ย. เพิ่มหรือต่างจากเนื้อหาเดิม")


def update_index(path):
    idx = json.load(open(path, encoding="utf-8"))
    before = json.dumps(idx, ensure_ascii=False)
    x = next(a for a in idx if a["set"] == "air")
    if INTRO_NEW not in x["intro"]:
        assert INTRO_OLD in x["intro"], "intro ของ air เปลี่ยนไปจากที่สคริปต์รู้จัก"
        x["intro"] = x["intro"].replace(INTRO_OLD, INTRO_NEW)
    if HOWTO_ADD.strip() not in x["howto"]:
        x["howto"] = x["howto"].rstrip() + HOWTO_ADD
    others = [json.dumps(a, ensure_ascii=False) for a in json.loads(before) if a["set"] != "air"]
    assert others == [json.dumps(a, ensure_ascii=False) for a in idx if a["set"] != "air"]
    return idx, json.dumps(idx, ensure_ascii=False) != before


def main():
    data = json.load(open(PATH, encoding="utf-8"))
    before = json.dumps(data, ensure_ascii=False)
    old_items = {i["id"]: (i["choices"], i["answer"]) for L in data if L["lec"] == LEC for s in L["sections"] for i in s["items"]}
    old_keys = {(s["id"], f, k) for L in data if L["lec"] == LEC for s in L["sections"]
                for f in ("anims", "figs", "imgs") for k in (s.get(f) or {})}
    old_mn = {(s["id"], m["name"]) for L in data if L["lec"] == LEC for s in L["sections"] for m in s.get("mnem", [])}
    old_mq = {m["id"] for L in data if L["lec"] == LEC for m in L.get("meq", []) + L.get("osce", [])}
    others = [json.dumps(L, ensure_ascii=False) for L in data if L["lec"] != LEC]
    L = apply(data)
    # ตรวจ: ข้อเดิมไม่เปลี่ยน · ภาพ/หลักจำเดิมยังอยู่ · คาบอื่นไม่เปลี่ยน · id ไม่ซ้ำ · ไม่มี code fence · ภาพมีไฟล์จริง
    now = {i["id"]: (i["choices"], i["answer"]) for s in L["sections"] for i in s["items"]}
    for k, v in old_items.items():
        if not k.startswith(P):
            assert now.get(k) == v, ("ข้อเดิมเปลี่ยน", k)
    keys = {(s["id"], f, k) for s in L["sections"] for f in ("anims", "figs", "imgs") for k in (s.get(f) or {})}
    assert old_keys <= keys, old_keys - keys
    assert old_mn <= {(s["id"], m["name"]) for s in L["sections"] for m in s.get("mnem", [])}
    assert old_mq <= {m["id"] for m in L["meq"] + L["osce"]}
    assert others == [json.dumps(x, ensure_ascii=False) for x in data if x["lec"] != LEC], "คาบอื่นเปลี่ยน"
    seen = set()
    for X in data:
        for s in X["sections"]:
            assert s["id"] not in seen, s["id"]; seen.add(s["id"])
            assert "```" not in s["md"], s["id"]
            for it in s["items"]:
                assert it["id"] not in seen, it["id"]; seen.add(it["id"])
    for s in L["sections"]:
        used = set(re.findall(r"^\s*\[\[anim:([\w-]+)\]\]\s*$", s["md"], re.M))
        assert used == set(s.get("anims") or {}), (s["id"], used, set(s.get("anims") or {}))
        usedi = set(re.findall(r"^\s*\[\[img:([\w-]+)\]\]\s*$", s["md"], re.M))
        assert usedi == set(s.get("imgs") or {}), (s["id"], usedi, set(s.get("imgs") or {}))
        for k, v in (s.get("imgs") or {}).items():
            assert re.match(r"^img/[\w/.-]+\.(jpg|png|webp)$", v["src"]), v["src"]
            fp = os.path.join(ART, v["src"])
            assert os.path.exists(fp), fp
            assert os.path.getsize(fp) < 150 * 1024, fp
            assert ("quiz" not in v) or v.get("q"), (k, "ภาพแบบทายต้องมี q")
    new = [i for s in L["sections"] for i in s["items"] if i["id"].startswith(P)]
    from collections import Counter
    print("หัวข้อ %d (ใหม่ %d) · ข้อใหม่ %d ตำแหน่งคำตอบ %s · anims ใหม่ %d · mnem ใหม่ %d · ภาพจริง %d" % (
        len(L["sections"]), len(NEW), len(new), dict(sorted(Counter(i["answer"] for i in new).items())), len(AN.ITEMS), len(AN.MNEM),
        sum(1 for s in L["sections"] for k in (s.get("imgs") or {}) if k.startswith("art-"))))
    out = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    changed = json.dumps(data, ensure_ascii=False) != before
    ipath = os.path.join(ART, "data", "index.json")
    idx, ichanged = update_index(ipath)
    if "--check" in sys.argv:
        print("--check: ไม่เขียนไฟล์ ·", "จะมีการเปลี่ยนแปลง" if (changed or ichanged) else "ไม่มีอะไรเปลี่ยน")
        return
    if changed:
        open(PATH, "w", encoding="utf-8").write(out)
        print("เขียน", PATH)
    else:
        print("air.json ไม่มีอะไรเปลี่ยน")
    if ichanged:
        raw = open(ipath, encoding="utf-8").read()
        l1 = raw.split("\n")[1] if "\n" in raw else ""
        indent = (len(l1) - len(l1.lstrip())) or None
        open(ipath, "w", encoding="utf-8").write(json.dumps(idx, ensure_ascii=False, indent=indent) + ("\n" if raw.endswith("\n") else ""))
        print("เขียน", ipath)


if __name__ == "__main__":
    main()
