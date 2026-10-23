#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""เติมเนื้อหาจาก handout ใหม่สองชุดเข้าคาบ neuro ที่ขึ้นเว็บแล้ว (append only — ไม่แตะหัวข้อ/ข้อสอบเดิม)

    python3 artifact/tools/update_neuro_handouts.py            # เขียน data/neuro.json
    python3 artifact/tools/update_neuro_handouts.py --check    # ตรวจโดยไม่เขียน

- 9/10  Lumbar puncture  ← handout อ.ปองปวีณ์ (Pongpawee Ekudomsuphan) · โน้ต slides/lp2_notes.md
        หัวข้อใหม่ neuro-lp-07..09 · ข้อใหม่ NEU-LP-MCQ-11.. · callout ท้าย md ของ neuro-lp-01..04
- 21/10 Acute confusional state ← handout 2026 อ.เพชรรัตน์ (Petcharat Dusitanond) + Delirium quiz ในห้อง · โน้ต slides/acs2026_notes.md
        หัวข้อใหม่ neuro-acs-16..19 · ข้อใหม่ NEU-ACS-MCQ-31.. · callout ท้าย md ของ neuro-acs-02/07/13/15

รันซ้ำได้: หัวข้อใหม่ถูกแทนที่ด้วยฉบับล่าสุด (ไม่ซ้ำ) · callout ตรวจด้วยข้อความหัว (marker) ถ้ามีแล้วแทนที่ ไม่เพิ่มซ้ำ ·
guidelines เพิ่มเฉพาะที่ยังไม่มี · ฟิลด์ anims/mnem/figs ของหัวข้อเดิมไม่ถูกแตะ"""
import json, os, re, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
import figs_neuro_update as F

ART = os.path.dirname(TOOLS)
PATH = os.path.join(ART, "data", "neuro.json")


def mcq(iid, stem, right, wrong, pos, explain, pearl, topic, ref, nl):
    """right = คำตอบที่ถูก · wrong = ตัวลวง 4 ข้อ · pos = ตำแหน่งคำตอบ (0–4) — กระจายตำแหน่งคำตอบของข้อใหม่"""
    assert len(wrong) == 4 and 0 <= pos <= 4
    ch = list(wrong)
    ch.insert(pos, right)
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": ch, "answer": pos, "explain": explain,
            "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}


def mcq_fixed(iid, stem, choices, answer, explain, pearl, topic, ref, nl):
    """ตัวเลือกที่เรียงตามธรรมชาติ (ตัวเลข) — ไม่สลับ"""
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer, "explain": explain,
            "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}


def sec(sid, title, summary, minutes, source, nl, md, pearls, items, figs):
    used = re.findall(r"^\s*\[\[fig:([\w-]+)\]\]\s*$", md, re.M)
    fd = {k: getattr(F, k)() for k in figs}
    assert sorted(used) == sorted(fd), (sid, used, list(fd))
    return {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": source,
            "nl": nl, "md": md.strip(), "pearls": pearls, "items": items, "figs": fd}


# ═════════════════════════════════════════════════════════════════════ LP 9/10
LPSRC = "handout อ.ปองปวีณ์ (Pongpawee Ekudomsuphan) — Lumbar puncture · หน่วยประสาทวิทยา รพ.ราชวิถี"
RL = lambda p: ["สไลด์ อ.ปองปวีณ์ — " + p]
LP = []

LP.append(sec("neuro-lp-07", "สไลด์ อ.ปองปวีณ์ — ข้อบ่งชี้ ข้อห้าม และตัวเลขที่ต้องจำ",
    "Therapeutic release ใน IIH และ cryptococcal meningitis · เกณฑ์เกล็ดเลือด · heparin 24 ชม. · hydrocephalus ชนิดอุดตัน", 10,
    LPSRC, ["2.3.6", "3.1.7", "B3.3(2)", "2.3.6-3(5)", "B2.4(3)"],
"""หัวข้อ 7–9 มาจาก **handout Lumbar puncture ของ อ.ปองปวีณ์** (หน่วยประสาทวิทยา รพ.ราชวิถี) ซึ่งเป็นคนละชุดกับสไลด์ที่ใช้สร้างหัวข้อ 1–6 · เขียนเฉพาะส่วนที่ **ใหม่หรือต่างจากเดิม** · ส่วนที่ไม่ได้มาจาก handout ระบุแหล่งไว้ทุกจุด

### ข้อบ่งชี้หกกลุ่มตาม handout
| กลุ่ม | ตัวอย่างใน handout | สิ่งที่ CSF ตอบ |
|---|---|---|
| **Infectious** | encephalitis · meningitis | เซลล์ น้ำตาล โปรตีน เชื้อ (หัวข้อ 9) |
| **Inflammatory** ✍️ ไฮไลต์ | **multiple sclerosis · Guillain-Barré syndrome** | oligoclonal band · IgG index · cyto-albuminologic dissociation |
| **Subarachnoid hemorrhage** | วินิจฉัย SAH | RBC ไม่จางลง · xanthochromia |
| **Intrathecal administration** | **ยาแก้ปวด · ยาเคมีบำบัด · ยาปฏิชีวนะ** | เป็นหัตถการเพื่อให้ยา ไม่ใช่เพื่อตรวจ |
| **Malignancy** | **lymphoma · metastasis** | cytology · flow cytometry |
| **Therapeutic release** ✍️ ไฮไลต์ | **IIH · cryptococcal meningitis ใน HIV** | ระบาย CSF = การรักษา |

### Therapeutic release — เมื่อการเจาะหลังคือการรักษา
**IIH (idiopathic intracranial hypertension)** — ความดันในกะโหลกสูงโดยไม่มีก้อนและโพรงสมองไม่โต ทางเดิน CSF ยังต่อถึงกันหมด การระบายจึงลดความดันทั้งระบบ บรรเทาปวดศีรษะและลดแรงกดที่ขั้วประสาทตาได้ชั่วคราว · การรักษาระยะยาวคือ **ลดน้ำหนัก + acetazolamide** และผ่าตัดเมื่อสายตาแย่ลง (อิง IIH consensus 2018 — ไม่อยู่ใน handout)

**Cryptococcal meningitis ใน HIV** — ลายมือบนสไลด์เขียนว่า **"ไปอุด"** และ **"HIV → permanent shunt"** หมายถึงเชื้อไปอุดทางดูดกลับ CSF จนความดันสูง และถ้าระบายซ้ำแล้วยังสูงต้องใส่ shunt ถาวร

[[fig:lp2_crypto]]

[[fig:lp2_hydro]]

### ข้อห้ามตาม handout — มีตัวเลขกำกับ
| ข้อห้าม | รายละเอียด | อันตรายที่เกิด |
|---|---|---|
| **CNS lesion หรือ spinal mass ที่ทำให้ ICP สูง** | ตัวแดงในสไลด์ | **herniation** จากแรงดันต่างบน–ล่าง |
| **ผิวหนังติดเชื้อตรงหรือใกล้จุดแทง** | | เข็มพาเชื้อเข้า → meningitis · epidural abscess |
| **Platelet < 20,000/mm³** | **ควร > 50,000/mm³** | **spinal epidural hematoma** กดไขสันหลัง/cauda equina |
| **UFH หรือ LMWH ภายใน 24 ชั่วโมง** | สไลด์เขียน "unfiltered heparin" = unfractionated heparin | เลือดออกใน epidural space |
| **Coagulopathy** | hemophilia · von Willebrand disease | เลือดออก |
| **Vertebral trauma** | | กระดูกไม่มั่นคง จัดท่าไม่ได้ · เสี่ยงบาดเจ็บไขสันหลัง |

**ตารางแบ่ง relative กับ absolute (handout อ้าง PMC6707491)**
| Relative | Absolute |
|---|---|
| platelet **20,000–40,000/mm³** ✍️ ติ๊ก | **non-communicating obstructive hydrocephalus** |
| **thienopyridine** (clopidogrel, prasugrel, ticlopidine) | **bleeding diathesis ที่ยังไม่แก้** |
| | **ยาต้านการแข็งตัวของเลือด** (เวลาเจาะขึ้นกับการหยุดยาแต่ละตัว) |
| | **platelet < 20,000/mm³** |
| | **spinal canal stenosis หรือ spinal cord compression เหนือระดับที่เจาะ** |
| | **ผิวหนังติดเชื้อเฉพาะที่** |

#### กลไก: ทำไมข้อห้ามแต่ละข้ออันตราย
- **Obstructive hydrocephalus** — ทางเดิน CSF ถูกปิด (ภาพใน handout: aqueduct ตีบ lateral และ third ventricle โต fourth ventricle เล็ก) → ความดันเหนือจุดอุดสูง แต่ใต้จุดอุดไม่สูง → ระบายจากหลังยิ่งเพิ่มความต่าง → **สมองถูกดันลง (herniation)** · ต่างจาก **communicating hydrocephalus** เช่น NPH ที่การเจาะคือการตรวจวินิจฉัย (tap test)
- **Cord compression เหนือระดับที่เจาะ** — กลไกเดียวกันในช่องไขสันหลัง: ปล่อย CSF ใต้จุดกด → ไขสันหลังถูกดันลงเข้าหาจุดตีบ (spinal coning) → อาการอ่อนแรงแย่ลงทันที
- **เกล็ดเลือดต่ำ / ยาต้านการแข็งตัว** — epidural space มี **ร่างแหหลอดเลือดดำ (Batson plexus)** ที่เข็มเฉี่ยวได้เสมอ คนปกติหยุดเลือดเองได้ คนที่หยุดเลือดไม่ได้เลือดจะสะสมใน **ช่องที่ขยายไม่ได้** → กดไขสันหลังหรือ cauda equina ภายในชั่วโมง
- **ภาพใน handout ที่ต้องดูก่อนเจาะ** — obstructive hydrocephalus · brain edema · brain herniation หกแบบ (transcalvarial · subfalcine · central transtentorial · uncal · upward cerebellar · tonsillar)""",
    ["Therapeutic release: ระบาย CSF เพื่อรักษา IIH และ cryptococcal meningitis ใน HIV",
     "Platelet < 20,000 ห้ามเจาะ · ควร > 50,000 · 20,000–40,000 = relative",
     "หยุด UFH/LMWH อย่างน้อย 24 ชั่วโมงก่อนเจาะ (ตาม handout)",
     "Non-communicating (obstructive) hydrocephalus = absolute contraindication · communicating (NPH) เจาะได้",
     "Cord compression เหนือระดับที่เจาะ = ข้อห้าม เพราะเกิด spinal coning"],
    [mcq("NEU-LP-MCQ-11",
         "A 34-year-old man with advanced HIV (CD4 40 cells/µL) has 2 weeks of headache and blurred vision. CT brain shows no mass or hydrocephalus. Lumbar puncture: opening pressure 38 cmH₂O, CSF cryptococcal antigen positive. Amphotericin B and flucytosine are started. What is the most appropriate way to manage his intracranial pressure?",
         "Therapeutic lumbar puncture to drain CSF, repeated daily until the pressure is controlled",
         ["Acetazolamide 250 mg every 8 hours", "Dexamethasone 10 mg IV every 6 hours",
          "Avoid further lumbar puncture because high pressure predicts herniation", "Immediate ventriculoperitoneal shunt before any further lumbar puncture"],
         0,
         "**ตอบ: therapeutic LP ซ้ำทุกวัน** — handout จัด cryptococcal meningitis ใน HIV เป็น **therapeutic release**\n\n"
         "**กลไก** — เชื้อและแคปซูล polysaccharide **ไปอุดทางดูดกลับ CSF ที่ arachnoid granulation** (ลายมือในสไลด์: \"ไปอุด\") ทางเดิน CSF ยังต่อถึงกันหมด (communicating) ความดันจึงสูงเท่ากันทั้งระบบ · การระบายออกทางหลังลดความดันทั้งระบบ **ไม่เกิดแรงดันต่าง** จึงปลอดภัย และ **ลดอัตราตาย** เพราะการตายส่วนหนึ่งมาจาก ICP สูง · เป้าหมายคือระบายจนความดัน < 20 cmH₂O หรือลดลงครึ่งหนึ่ง (WHO 2022 — ไม่อยู่ใน handout)\n\n"
         "**ทำไมข้ออื่นผิด** — **acetazolamide** ในการศึกษาผู้ป่วย crypto ทำให้เกิด acidosis และต้องหยุดเพราะผลเสียมากกว่า · **dexamethasone** เพิ่มอัตราตายและความพิการใน cryptococcal meningitis (CryptoDex) · **การงดเจาะ** ผิดเพราะ CT ไม่มีก้อนหรือ hydrocephalus ความเสี่ยง herniation ต่ำ · **shunt** ใช้เมื่อระบายซ้ำแล้วยังสูงต่อเนื่อง (ลายมือ: HIV → permanent shunt) ไม่ใช่ขั้นแรก",
         "Cryptococcal meningitis + OP สูง → เจาะระบายซ้ำทุกวัน · ไม่ใช้ steroid หรือ acetazolamide",
         "Therapeutic LP — cryptococcal meningitis", RL("Lumbar puncture: Indication (therapeutic release)"),
         ["B3.3(2)", "B3.2.2(1)", "2.3.1-3(7)"]),
     mcq("NEU-LP-MCQ-12",
         "A 52-year-old man with acute myeloid leukaemia on induction chemotherapy develops fever, headache and neck stiffness. Platelet count is 15,000/mm³; PT and aPTT are normal. CT brain is normal. Lumbar puncture is needed. According to the handout thresholds, what is the most appropriate approach?",
         "Start empirical antibiotics now and transfuse platelets before LP, aiming for a count above 50,000/mm³",
         ["Proceed with LP immediately because the coagulation tests are normal",
          "Proceed with LP because only counts below 10,000/mm³ are a contraindication",
          "Withhold antibiotics until CSF has been obtained to maximise culture yield",
          "Lumbar puncture is permanently contraindicated in acute leukaemia"],
         1,
         "**ตอบ: ให้ยาปฏิชีวนะทันที แล้วให้เกล็ดเลือดก่อนเจาะ ให้ได้ > 50,000/mm³**\n\n"
         "**ตาม handout** — **platelet < 20,000/mm³ เป็นข้อห้าม** และ **ideally > 50,000/mm³** · ตารางใน handout จัด 20,000–40,000 เป็น relative contraindication\n\n"
         "**กลไก** — epidural space มีร่างแหหลอดเลือดดำที่เข็มเฉี่ยวได้บ่อย ถ้าเกล็ดเลือดไม่พอ เลือดสะสมใน **ช่องแคบที่ขยายไม่ได้** → **spinal epidural hematoma** กด cauda equina หรือไขสันหลัง (handout ระบุ spinal hematoma เป็นภาวะแทรกซ้อน)\n\n"
         "**ทำไมข้ออื่นผิด** — **PT/aPTT ปกติไม่ได้ชดเชยเกล็ดเลือดต่ำ** เพราะเป็นคนละขั้นของการหยุดเลือด · **10,000 ไม่ใช่เกณฑ์ของ handout** · **การชะลอยาปฏิชีวนะเพื่อรอ CSF** ใน bacterial meningitis เพิ่มอัตราตาย (เชื้อในเลือดและ PCR ยังช่วยได้) · **leukaemia ไม่ใช่ข้อห้ามถาวร** — ผู้ป่วยกลุ่มนี้ต้องเจาะหลังบ่อยเพื่อให้ยาเคมีบำบัดเข้าช่อง CSF (intrathecal)",
         "Platelet < 20,000 ห้ามเจาะ · ควรแก้ให้ > 50,000 · อย่าชะลอยาปฏิชีวนะเพื่อรอเจาะ",
         "LP contraindications — thrombocytopenia", RL("Lumbar puncture: Contraindication"),
         ["B3.3(2)", "2.3.3-3(2)", "2.3.6(5)"]),
     mcq("NEU-LP-MCQ-13",
         "A 45-year-old woman has 3 weeks of morning headache and vomiting. MRI shows markedly dilated lateral and third ventricles, a small fourth ventricle and a narrowed cerebral aqueduct. Which statement about lumbar puncture in this patient is correct?",
         "It is absolutely contraindicated because CSF removal below the obstruction creates a pressure gradient that can cause herniation",
         ["It is the preferred first treatment to lower intracranial pressure, as in IIH",
          "It is safe if the opening pressure is measured slowly with a manometer",
          "It is safe if a 25G atraumatic needle is used",
          "It is indicated as a diagnostic tap test, as in normal pressure hydrocephalus"],
         2,
         "**ตอบ: ห้ามเจาะเด็ดขาด** — ภาพนี้คือ **non-communicating (obstructive) hydrocephalus** จาก aqueduct ตีบ (lateral + third ventricle โต fourth ventricle เล็ก) ซึ่งตาราง handout จัดเป็น **absolute contraindication**\n\n"
         "**กลไก** — CSF ที่สร้างใน lateral ventricle ระบายลงข้างล่างไม่ได้ ความดัน **เหนือจุดอุดสูง** ส่วนช่องไขสันหลัง **ใต้จุดอุดไม่สูง** · การปล่อย CSF จากหลังทำให้ข้างล่างยิ่งต่ำลง → แรงดันต่างดันสมองลงผ่าน tentorium หรือ foramen magnum (**herniation**)\n\n"
         "**ทำไมข้ออื่นผิด** — **IIH** ทางเดินยังต่อกัน (communicating) จึงระบายได้ · **ระบายช้าหรือใช้เข็มเล็ก** ลดอัตราการรั่วแต่ **ไม่แก้แรงดันต่าง** ที่เกิดทันทีที่ CSF ออก · **tap test ใช้ใน NPH** ซึ่งเป็น communicating hydrocephalus ไม่ใช่ชนิดอุดตัน · การรักษาที่ถูกคือ **ระบายจากเหนือจุดอุด** (EVD หรือ endoscopic third ventriculostomy)",
         "Obstructive (non-communicating) hydrocephalus = ห้ามเจาะหลัง · ต้องระบายจากเหนือจุดอุด",
         "LP contraindications — obstructive hydrocephalus", RL("Lumbar puncture: Contraindications for LP (absolute)"),
         ["B3.3(2)", "2.3.6-3(5)", "2.2.35"]),
     mcq("NEU-LP-MCQ-14",
         "A 68-year-old woman receiving therapeutic-dose enoxaparin for a deep-vein thrombosis needs a non-urgent diagnostic lumbar puncture for suspected Guillain-Barré syndrome. Her last dose was 8 hours ago; platelets are 210,000/mm³. Based on the handout, when should the LP be performed?",
         "At least 24 hours after the last dose of low-molecular-weight heparin",
         ["Now, because platelets are normal", "Now, after checking that aPTT is normal",
          "Now, after giving full-dose protamine", "Only after enoxaparin has been stopped for 7 days"],
         3,
         "**ตอบ: รอให้ครบอย่างน้อย 24 ชั่วโมงหลังเข็มสุดท้าย** — handout ระบุข้อห้ามว่า **ใช้ unfractionated heparin หรือ LMWH ภายใน 24 ชั่วโมงที่ผ่านมา**\n\n"
         "**กลไก** — LMWH ยับยั้ง factor Xa และคงฤทธิ์นานหลายชั่วโมง (ยิ่งนานในไตเสื่อม) ช่วงที่ยายังออกฤทธิ์ เลือดจากร่างแหหลอดเลือดดำใน epidural space ที่เข็มเฉี่ยวจะไม่หยุด → **spinal epidural hematoma** · ขนาดยารักษา (therapeutic dose) ต้องรอนานกว่าขนาดป้องกัน\n\n"
         "**ทำไมข้ออื่นผิด** — **เกล็ดเลือดปกติ** ไม่บอกฤทธิ์ของ LMWH · **aPTT ไม่ไวต่อ LMWH** (ต้องวัด anti-Xa) · **protamine แก้ฤทธิ์ LMWH ได้ไม่ครบ** และไม่ควรใช้เพื่อหัตถการที่ไม่ด่วน · **7 วัน** คือเวลาหยุด clopidogrel ไม่ใช่ LMWH · โรค GBS เจาะเพื่อวินิจฉัย (cyto-albuminologic dissociation) รอ 1 วันได้",
         "UFH/LMWH ภายใน 24 ชม. = ห้ามเจาะ · aPTT ไม่บอกฤทธิ์ LMWH",
         "LP contraindications — anticoagulants", RL("Lumbar puncture: Contraindication"),
         ["B3.3(2)", "B2.4(3)", "2.3.6-3(4)"]),
     ],
    ["lp2_crypto", "lp2_hydro"]))

LP.append(sec("neuro-lp-08", "สไลด์ อ.ปองปวีณ์ — อุปกรณ์ ท่า เทคนิค และภาวะแทรกซ้อน",
    "เข็ม 20–22G · ชั้นที่เข็มผ่านและ pop · L3–4/L4–5 · bevel ขนานแนว sagittal · มุม 15° · 3–5 mL ต่อขวด · paramedian · post-LP headache", 12,
    LPSRC, ["2.3.6", "3.1.7", "B3.3(2)", "2.1.3"],
"""### อุปกรณ์ตาม handout
- **Spinal needle ที่มี stylet ขนาด 20G หรือ 22G** (ภาพในสไลด์เป็นเข็ม 22G)
- **ขวดเก็บ CSF** · **manometer พร้อม three-way valve** สำหรับวัด opening pressure
- ผ้าปูปลอดเชื้อ · ยาชาเฉพาะที่ · เข็ม **18G ดูดยาชา** และ **25G ฉีดผิวหนัง** · น้ำยา **0.5% chlorhexidine ใน 70% alcohol** · ถุงมือปลอดเชื้อ · หน้ากากพร้อม face shield · หมวก

> **เทียบกับหัวข้อ 2** — สไลด์ชุดเดิมบอกว่า **22G เป็นปัจจัยเสี่ยงของ post-LP headache รุนแรง** ส่วน handout ใช้ 20–22G เป็นขนาดมาตรฐาน · สองข้อนี้ไม่ขัดกัน: เข็มขนาดนี้ทำให้ CSF ไหลเร็วพอวัดความดันและเก็บตัวอย่าง แต่ถ้าเลือกได้ **เข็มเล็กลงหรือ atraumatic (pencil-point)** ลด post-LP headache ได้ชัด (Nath S, Lancet 2018 — ไม่อยู่ใน handout)

### ชั้นที่เข็มผ่าน — เก้าชั้น
1. Skin
2. Subcutaneous tissue
3. Supraspinous ligament
4. Interspinous ligament
5. **Ligamentum flavum** ← มักรู้สึก **"pop"** ตอนทะลุชั้นนี้
6. Epidural space
7. Dura
8. Arachnoid
9. **Subarachnoid space** ← ที่เก็บ CSF

**ระยะจากผิวหนังถึง epidural space ประมาณ 55 mm หรือ 2/3 ของความยาวเข็ม** — ใช้กะว่าใกล้ถึงแล้วให้ดันช้าลงและถอด stylet ดูทีละ 2–3 mm

[[fig:lp2_needle]]

### ท่าและระดับที่แทง
- **ท่านั่ง (upright) หรือนอนตะแคง (lateral decubitus)** — ท่านั่งหาแนวกลางง่ายกว่าในคนอ้วน แต่ **ต้องการวัด opening pressure ต้องนอนตะแคง** (หัวข้อ 4)
- **แทงที่ช่อง L4–L5 หรือ L3–L4** เพื่อเลี่ยง **conus medullaris ซึ่งปกติสิ้นสุดที่ L1** (หัวข้อ 2 ใช้ช่วง L1–L2 ซึ่งเป็นช่วงที่พบได้ในผู้ใหญ่ ทั้งสองแหล่งให้เจาะต่ำกว่า L2 เหมือนกัน)

### เทคนิคทีละขั้นตาม handout
1. **แทงโดยมี stylet อยู่ในเข็ม** และหัน **bevel ขนานแนว sagittal (หันขึ้นเพดานเมื่อนอนตะแคง)** — handout ให้เหตุผลว่า **แหวกเส้นใยแทนการตัดขาด**
2. **ทำมุมราว 15 องศาขึ้นทางศีรษะ** — นึกภาพว่า **เล็งไปที่สะดือ** ของผู้ป่วย เพราะ spinous process ของกระดูกเอวชี้ลงล่าง
3. **เก็บ CSF ราว 3–5 mL ต่อขวด**
4. **Paramedian (paraspinous) approach** — จุดแทง **ต่ำกว่า 1 cm และออกด้านข้าง 1 cm** จาก landmark ของ L4 แล้ว **แทงเฉียงเข้าแนวกลางและขึ้นทางศีรษะราว 15 องศา** · เข็มเข้าทางด้านข้างของ spinous process จึงเลี่ยงเอ็นแนวกลางที่หนาหรือมีหินปูน ใช้ในผู้สูงอายุหรือผู้ที่งอตัวได้น้อย (ข้อบ่งชี้อิงตำรา — handout มีแต่วิธีทำ)

### วัด opening pressure และแบ่งขวด (ส่วนที่ handout ไม่ได้ลงรายละเอียด — อิงแนวทาง)
- นอนตะแคง **เหยียดขาและคลายตัว** หลังเข็มเข้าที่ · ต่อ **manometer ผ่าน three-way valve ทันทีที่ CSF ไหล ก่อนเก็บขวดใด ๆ** · อ่านค่าที่คอลัมน์หยุดขึ้นและแกว่งตามการหายใจ · ค่าปกติตาม handout **50–200 mmH₂O (5–20 cmH₂O)**
- ลำดับขวดที่ใช้ทั่วไป: **ขวด 1 chemistry (glucose โปรตีน) · ขวด 2 microbiology (Gram culture) · ขวด 3 cell count · ขวด 4 เก็บสำรอง (PCR, cytology)** — นับเซลล์ในขวดท้ายเพราะเลือดจาก traumatic tap จางลงแล้ว (Engelborghs 2017 และ StatPearls — handout ระบุเพียง 3–5 mL ต่อขวด)

### Pitfalls สี่ข้อที่ handout เตือน
| Pitfall | ผลเสีย |
|---|---|
| **Bevel ไม่หันขึ้นเพดาน** | ตัดเส้นใยดูราขวาง รูกว้าง → **post-LP headache** |
| **ดูด CSF ด้วยแรงลบ** | เพิ่มเลือดออก (หัวข้อ 2) · ดูดรากประสาทหรือเนื้อเยื่อเข้ารูเข็ม |
| **แทงหรือถอนเข็มโดยไม่มี stylet** | แทงเปล่า → เข็มคว้านผิวหนังติดเข้าไป (epidermoid tumor ในภายหลัง) · ถอนเปล่า → ดึงเส้นใย arachnoid ค้างรูดูรา (หัวข้อ 2) |
| **ตัวอย่างไม่พอ** | ต้องเจาะซ้ำ · cytology และ culture วัณโรค/เชื้อราต้องการปริมาณมาก |

### ภาวะแทรกซ้อนสี่ข้อตาม handout
- **Cerebral herniation** (หัวข้อ 3 และ 7)
- **Post-lumbar puncture headache**
- **Spinal hematoma** — ปวดหลังรุนแรงร่วมกับขาอ่อนแรง ชา ปัสสาวะอุจจาระผิดปกติหลังเจาะ → **MRI ด่วนและผ่าตัดระบายเลือด** ยิ่งเร็วยิ่งฟื้นดี (ตำรา)
- **Chronic adhesive arachnoiditis จากน้ำยาฆ่าเชื้อ** — chlorhexidine ที่ติดปลายเข็มหรือปนเข้าชุดอุปกรณ์เป็นพิษต่อ arachnoid → อักเสบเรื้อรังและเกิดพังผืด **รากประสาทติดกัน** → ปวดหลังร้าวลงขา ชา อ่อนแรงเรื้อรัง · ป้องกันโดย **ให้น้ำยาแห้งก่อนแทง** และไม่วางน้ำยาใกล้ชุดเข็ม

#### ทำไมถึงมีอาการนี้ — post-LP headache (ด้านที่เกี่ยวกับเข็ม)
| อาการ/ปัจจัย | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ปวดศีรษะเมื่อลุก ดีขึ้นเมื่อนอน ภายใน 5 วันหลังเจาะ** | รูที่ดูรารั่ว CSF ออก epidural เร็วกว่าที่สร้างทดแทน → ความดันและปริมาตร CSF ลด → ท่าตั้งสมองทรุด ดึงเยื่อหุ้มและหลอดเลือดที่ไวต่อปวด · หลอดเลือดดำในกะโหลกขยายชดเชย (Monro–Kellie) | ICHD-3 กำหนดว่าเกิดภายใน 5 วันหลังเจาะ · ปวดไม่ขึ้นกับท่า มีไข้ หรือซึมลง → คิดถึง meningitis หรือเลือดออก |
| **เป็นมากเมื่อ bevel ขวางแนวเส้นใย** | เส้นใยดูราวิ่งตามยาว ปลายตัดที่หันขวางตัดเส้นใยขาด รูอ้ากว้าง · หันขนานแค่แหวกเป็นร่องที่หดปิดเอง | เป็นเหตุผลของ pitfall ข้อแรกใน handout |
| **เข็มใหญ่หรือปลายตัด เป็นมากกว่า atraumatic** | ขนาดรูกำหนดอัตราการรั่ว · pencil-point ดันเส้นใยแยกโดยไม่ตัด ขอบรูยืดหยุ่นกลับมาปิด | การเปลี่ยนเป็นเข็ม atraumatic ลดอุบัติการณ์ราวครึ่งหนึ่ง |
| **หญิง อายุน้อย BMI ต่ำ เป็นบ่อย** | ดูรายืดหยุ่นและความดัน epidural ต่ำ รูจึงไม่ถูกกดปิด | ผู้สูงอายุเป็นน้อยกว่า |
| **ดีขึ้นทันทีหลัง epidural blood patch** | เลือดตัวเองที่ฉีดเข้า epidural **ดันช่อง CSF ทันที** แล้ว **แข็งตัวอุดรู** | ไม่ดีขึ้น → ทบทวนการวินิจฉัย |

[[fig:lp2_pdph]]

### การรักษา post-LP headache เป็นขั้นบันได
1. **ประคับประคอง** — ส่วนใหญ่หายเองภายใน 1 สัปดาห์ · นอนราบช่วยอาการ (แต่การนอนพักหลังเจาะไม่ได้ป้องกัน) · ดื่มน้ำ · paracetamol หรือ NSAID · คาเฟอีน (หดหลอดเลือดสมองที่ขยาย)
2. **Epidural blood patch** — เมื่อปวดรุนแรงหรือไม่ดีขึ้นในหลายวัน ได้ผลส่วนใหญ่ในครั้งแรก
(ส่วนนี้อิง ICHD-3 และแนวทาง LP — handout ระบุเพียงชื่อภาวะแทรกซ้อน)""",
    ["เข็ม 20–22G มี stylet · ถ้าเลือกได้ เข็มเล็ก/atraumatic ลด post-LP headache",
     "Pop = ligamentum flavum · ผิวถึง epidural ≈ 55 mm (2/3 ของเข็ม)",
     "แทง L3–4 หรือ L4–5 (conus จบ L1) · มุม 15° เล็งสะดือ · bevel หันขึ้นเพดาน",
     "เก็บ 3–5 mL ต่อขวด · ห้ามดูด · แทงและถอนพร้อม stylet",
     "Paramedian: 1 cm ใต้ + 1 cm ข้าง L4 แทงเฉียงเข้ากลางขึ้นศีรษะ 15°",
     "ภาวะแทรกซ้อนเพิ่มจากหัวข้อ 3: spinal hematoma · adhesive arachnoiditis จาก chlorhexidine"],
    [mcq("NEU-LP-MCQ-15",
         "A resident performs a lumbar puncture with the patient in the left lateral decubitus position. Which technique matches the handout's recommendations?",
         "Enter at L3–L4 or L4–L5 with the stylet in place, bevel facing the ceiling, angled about 15° cephalad towards the umbilicus",
         ["Enter at L1–L2 so the needle reaches CSF at a shallower depth",
          "Enter perpendicular to the skin with the bevel facing the patient's feet to cut through the ligaments",
          "Advance without the stylet so CSF appears as soon as the dura is crossed",
          "Aspirate gently with a syringe once the 'pop' is felt to speed up collection"],
         4,
         "**ตอบ: L3–4 หรือ L4–5 · มี stylet · bevel หันเพดาน · มุมราว 15° เล็งสะดือ** — ครบทุกข้อของ handout\n\n"
         "**เหตุผลทีละส่วน** — **ระดับ**: conus medullaris ปกติจบที่ L1 ต่ำกว่านั้นมีแต่ cauda equina ที่ลอยหลบเข็มได้ · **bevel หันเพดานในท่านอนตะแคง** = ขนานแนว sagittal จึงแหวกเส้นใยแทนการตัด รูเล็ก CSF รั่วน้อย · **มุม 15° ขึ้นศีรษะ** เพราะ spinous process ของกระดูกเอวชี้ลงล่าง ช่องว่างจึงเปิดทางเฉียงขึ้น · **stylet** กันเข็มคว้านผิวหนังเข้าไป\n\n"
         "**ทำไมข้ออื่นผิด** — **L1–L2** เสี่ยงแทงโดน conus · **แทงตั้งฉากและหัน bevel ขวาง** ชน spinous process และตัดเส้นใยดูรา · **แทงโดยไม่มี stylet** อาจนำชิ้นผิวหนังเข้าช่องไขสันหลัง (epidermoid tumor) · **การดูด** เป็น pitfall ใน handout เพิ่มเลือดออกและดูดรากประสาทเข้ารูเข็ม · pop ที่รู้สึกคือ **ligamentum flavum** ยังไม่ถึง CSF",
         "LP: L3–4/L4–5 · stylet in · bevel ขึ้นเพดาน · 15° เล็งสะดือ · ไม่ดูด",
         "LP technique", RL("Lumbar puncture: Preparation and Technique"), ["B3.3(2)", "3.1.7"]),
     mcq("NEU-LP-MCQ-16",
         "Three days after a diagnostic lumbar puncture with a 20G cutting needle, a 24-year-old woman has a headache that appears within 15 minutes of sitting up and resolves when she lies flat, with neck stiffness and tinnitus. She is afebrile. Two days of rest, fluids, paracetamol and caffeine have not helped. What is the most appropriate next step?",
         "Epidural blood patch",
         ["Repeat lumbar puncture to exclude meningitis", "Strict bed rest for another 7 days",
          "Start empirical ceftriaxone and acyclovir", "Urgent CT angiography for subarachnoid hemorrhage"],
         0,
         "**ตอบ: epidural blood patch** — ภาพครบของ **post-LP headache**: ปวดตามท่าชัดเจน เกิดภายใน 5 วัน มีคอแข็งและหูอื้อ ไม่มีไข้ และการรักษาประคับประคองไม่ได้ผล\n\n"
         "**กลไก** — เข็ม **20G ปลายตัด** ทำรูดูราใหญ่ CSF รั่วต่อเนื่อง → ความดันต่ำ สมองทรุดเมื่อลุก · คอแข็งจากเยื่อหุ้มด้านหลังถูกดึง · หูอื้อเพราะความดัน CSF ส่งผ่าน cochlear aqueduct ถึงหูชั้นใน · **blood patch ดันช่อง CSF ทันทีและก้อนเลือดอุดรู** อาการจึงหายเร็ว\n\n"
         "**ทำไมข้ออื่นผิด** — **การเจาะซ้ำ** ทำรูใหม่และไม่จำเป็นเพราะไม่มีไข้หรือซึม · **นอนพักนานขึ้น** ไม่ได้ปิดรูและเสี่ยงลิ่มเลือดดำ · **ยาปฏิชีวนะ** ไม่มีข้อบ่งชี้เมื่อปวดขึ้นกับท่าและไม่มีไข้ · **SAH** ปวดทันทีรุนแรงไม่ขึ้นกับท่า",
         "PDPH ที่ไม่ดีขึ้นด้วยการประคับประคอง → epidural blood patch",
         "Post-LP headache — management", RL("Lumbar puncture: Complications"), ["B3.3(2)", "2.1.3"]),
     ],
    ["lp2_needle", "lp2_pdph"]))

LP.append(sec("neuro-lp-09", "สไลด์ อ.ปองปวีณ์ — แปลผล CSF: ค่าปกติ meningitis สี่แบบ โรคอักเสบ และเลือดปน",
    "ค่าปกติ · ขุ่น = WBC ≥ 100–200 · เหลือง = โปรตีน ≥ 150–300 · bacterial/viral/TB/crypto · MS NMO ADEM GBS · traumatic tap vs SAH · สูตรแก้ค่า", 12,
    LPSRC, ["3.1.7", "B3.3(2)", "B3.2.2(1)", "2.3.6(5)", "2.3.6(3)", "2.3.6-3(4)"],
"""### ค่าปกติของ CSF ตาม handout
| รายการ | ค่าปกติ |
|---|---|
| สี | ใส |
| Specific gravity / pH | 1.006–1.007 / 7.4 |
| Opening pressure | **50–200 mmH₂O** (5–20 cmH₂O) |
| RBC | ไม่มี |
| WBC | **0–5 /mm³** (ทารกแรกเกิดถึง 30) · lymphocyte |
| Protein | **15–40 mg/dL** |
| Lactate | 1–3 mmol/L |
| Glucose | **50–80 mg/dL (สองในสามของน้ำตาลในเลือด)** |
| เชื้อ | ไม่พบ |

### สองกฎจากตาเปล่า
- **CSF ขุ่น = WBC อย่างน้อย 100–200 /mm³** — เซลล์จำนวนมากกระเจิงแสง
- **CSF เหลือง = โปรตีนอย่างน้อย 150–300 mg/dL** — โปรตีนสูงมาก (และ bilirubin จากเลือดเก่า) ทำให้สีเหลืองได้ เช่น TB meningitis หรือการอุดกั้นช่องไขสันหลัง · จึงไม่ใช่ทุกสีเหลืองที่เป็น SAH

### ตาราง meningitis สี่แบบ (handout)
| | Bacterial | Viral | TB | Cryptococcal |
|---|---|---|---|---|
| **Opening pressure** | ↑ 20–50 cmH₂O | ปกติหรือสูงเล็กน้อย 9–20 | ↑ 20–50 | **↑↑ > 25 (บางราย > 40–50)** |
| **ลักษณะ** | ขุ่น เป็นหนอง | ใส | ใสหรือขุ่นเล็กน้อย | ใสถึงขุ่นเล็กน้อย |
| **WBC /µL** | 1,000–5,000 (100–10,000) | 10–1,000 (มัก < 500) | 100–500 (50–1,000) | 20–500 (บางราย < 50) |
| **ชนิดเซลล์** | **neutrophil > 80%** | lymphocyte | lymphocyte (ระยะแรก 7 วันเป็น neutrophil ได้ ✍️) | lymphocyte (บางครั้ง mixed) |
| **Protein mg/dL** | ↑↑ 100–500+ (บางราย > 1,000) | ปกติหรือ 50–100 | ↑↑ 100–500 | ↑ 100–500 |
| **Glucose mg/dL** | **↓↓ < 40 (ratio < 0.4)** | ปกติ 45–80 | ↓ < 45 (ratio < 0.5) | ↓ < 40 (ratio < 0.5) |
| **Gram stain** | บวก 60–90% | ลบ | ลบ | ลบ |
| **ย้อมพิเศษ** | – | – | Ziehl–Neelsen · PCR AFB | **India ink (ไว 50–80%)** |
| **Antigen / PCR** | latex agglutination · PCR | PCR enterovirus/HSV | Xpert MTB/RIF | **CrAg ไว > 95%** |
| **Culture** | มาตรฐาน | ไม่ค่อยทำ | มาตรฐาน (ช้า) | มาตรฐาน |

**จุดที่ handout เติมเอง** — โปรตีนเฉลี่ย bacterial 111 ± 84 mg/dL และ TB 259 ± 409 mg/dL · lactate > 6 mmol/L ใน bacterial · ADA สูงใน TB · aseptic meningitis หลังผ่าตัดสมองหรือได้ยาปฏิชีวนะมาแล้วอาจเด่น neutrophil

#### กลไก: ทำไมแต่ละเชื้อให้ภาพต่างกัน
- **Bacterial** — สารจากผนังเซลล์แบคทีเรียกระตุ้น cytokine ดึง **neutrophil** จำนวนมากผ่าน BBB ที่รั่ว (โปรตีนสูง) · แบคทีเรียและ neutrophil ใช้ glucose และ GLUT1 ทำงานผิดปกติ → **glucose ต่ำมาก**
- **Viral** — การอักเสบชนิด T cell → **lymphocyte** · ไวรัสไม่ใช้ glucose ของ CSF → **glucose ปกติ**
- **TB** — granuloma ที่ฐานสมองหลั่งโปรตีนและทำให้ CSF ไหลช้า → **โปรตีนสูงมาก** (CSF อาจเหลือง) · ระยะแรกอาจเด่น neutrophil ก่อนเปลี่ยนเป็น lymphocyte
- **Cryptococcus** — แคปซูลกดการอักเสบ เซลล์จึงน้อยได้ (โดยเฉพาะ HIV) แต่ **แคปซูลอุด arachnoid granulation → ความดันสูงมาก** (หัวข้อ 7) · CrAg จับแคปซูลโดยตรงจึงไวที่สุด

### CSF ในโรคอักเสบ (handout)
| โรค | ลักษณะทางคลินิก | CSF |
|---|---|---|
| **Transverse myelitis** | sensorimotor + autonomic ของไขสันหลังสองข้าง · **sensory level ชัด** · hyperreflexia Babinski | pleocytosis · โปรตีนสูง · OCB หรือ IgG index สูง · IL-6 สูง · PCR เชื้อลบ · น้ำตาลและความดันปกติ |
| **Multiple sclerosis** | ชา อ่อนแรง ตามัว เดินเซ ความคิด อ่อนล้า ปัสสาวะผิดปกติ | lymphocyte 5–50 · โปรตีนสูงเล็กน้อย · **OCB (highly diagnostic)** · IgG index สูง |
| **Neuromyelitis optica** | transverse myelitis รุนแรง + optic neuropathy | ไม่จำเพาะ · lymphocyte 5–50 · โปรตีนสูง · น้ำตาลปกติ |
| **ADEM** | ไข้ meningeal sign encephalopathy · แย่สุดใน 4–7 วัน · พบในเด็ก · MRI วินิจฉัย | เซลล์ 5–50 และ/หรือโปรตีนสูง อาจปกติ · ถ้ามี OCB ให้คิดถึง MS มากกว่า |
| **Guillain-Barré syndrome** | อ่อนแรงสมมาตรไต่ขึ้น reflex หาย หลังติดเชื้อ · autonomic · cranial nerve | **เซลล์ปกติ โปรตีนสูง = cyto-albuminologic dissociation** |

> **ข้อควรระวังเรื่อง NMO** — handout เขียนว่า OCB "may be present (most cases)" แต่การศึกษาส่วนใหญ่พบ OCB ใน NMOSD เพียงราว 15–30% และมักหายไป · **OCB ที่คงอยู่จึงช่วยแยก MS ออกจาก NMOSD**

### Traumatic tap หรือ SAH
| ลักษณะ CSF | Traumatic tap | SAH |
|---|---|---|
| สี | แดง | แดง ชมพู เหลือง |
| สีขวด 1 → 3 | **จางลงเรื่อย ๆ** | **เท่าเดิม** |
| Xanthochromia | ตาม handout: พบในขวดหลัง | **พบตั้งแต่ขวดแรก** |
| เลือดแข็งตัว | **ได้** | **ไม่ได้** |
| ปั่นแล้ว | ส่วนบนใส | **เหลือง (xanthochromia)** |

[[fig:lp2_tubes]]

> **ข้อสังเกตเรื่อง xanthochromia ใน traumatic tap** — ตามกลไก RBC ที่เพิ่งออกขณะเจาะยังไม่แตกและยังไม่ถูกเปลี่ยนเป็น bilirubin ถ้าปั่นทันทีส่วนบนจะใส (handout เขียนเองในแถวสุดท้ายว่า "ปั่น = สีใส") · xanthochromia ใน traumatic tap จะพบได้ก็ต่อเมื่อ **ส่งตรวจช้า** หรือ **RBC มากจนแตกในหลอด** หรือ **โปรตีนสูงมาก** · ถ้าเจอคำถามเชิงกลไก ให้ตอบว่า **SAH มี xanthochromia ส่วน traumatic tap ไม่มี**

### แก้ค่าเมื่อมีเลือดปน (handout อ้าง PMC5607637)
- **WBC: หัก 1 ตัว ต่อ RBC 500–1,000 /mm³** (เลือดปกติมี WBC : RBC ราว 1 : 700)
- **Protein: หัก 1.1–1.9 mg/dL ต่อ RBC 1,000 /mm³** (ตำราส่วนใหญ่ใช้ราว 1 mg/dL ต่อ 1,000)
- ตัวอย่าง: RBC 10,000 WBC 40 → WBC จากเลือดราว 10–20 → WBC ที่แท้จริงยังเกิน 5 = **มี pleocytosis จริง**""",
    ["CSF ปกติ: WBC 0–5 · โปรตีน 15–40 · glucose 50–80 (2/3 ของเลือด) · OP 50–200 mmH₂O",
     "ขุ่น = WBC ≥ 100–200 · เหลือง = โปรตีน ≥ 150–300",
     "Bacterial: neutrophil glucose < 40 ratio < 0.4 · Crypto: OP > 25 CrAg ไว > 95%",
     "GBS = เซลล์ปกติ โปรตีนสูง · MS = OCB",
     "Traumatic tap: จางลงขวด 1→3 แข็งตัวได้ ส่วนบนใส · SAH: เท่ากันทุกขวด xanthochromia",
     "แก้ค่า: WBC 1 ต่อ RBC 500–1,000 · โปรตีน ~1–2 mg/dL ต่อ RBC 1,000"],
    [mcq("NEU-LP-MCQ-17",
         "A 48-year-old woman presents 2 hours after a sudden severe headache; CT brain is normal. Lumbar puncture yields bloody CSF. RBC counts are 12,000/mm³ in tube 1 and 300/mm³ in tube 4; the specimen forms a small clot and the supernatant is clear after immediate centrifugation. WBC in tube 1 is 18/mm³. Which interpretation is most appropriate?",
         "A traumatic tap is most likely, and the WBC count is consistent with contamination from peripheral blood",
         ["Subarachnoid hemorrhage is confirmed because the CSF is bloody",
          "Bacterial meningitis is likely because the WBC count exceeds 5/mm³",
          "Subarachnoid hemorrhage is confirmed because blood clotted in the tube",
          "Xanthochromia is absent, so the LP must be repeated at the same level immediately"],
         1,
         "**ตอบ: traumatic tap** — ครบตามตาราง handout: **RBC ลดลงมากจากหลอดแรกถึงหลอดท้าย · เลือดแข็งตัว · ปั่นแล้วส่วนบนใส**\n\n"
         "**กลไก** — เข็มเฉี่ยวหลอดเลือดดำใน epidural ขณะเจาะ เลือดจึงปนมากตอนแรกแล้วถูก CSF ใสชะออก · เลือดสดยังมี fibrinogen จึงแข็งตัว · ใน SAH เลือดผสมทั่วช่อง CSF มาก่อน ทุกขวดแดงเท่ากันและไม่แข็งตัว\n\n"
         "**แก้ค่า WBC** — handout: **WBC 1 ตัวต่อ RBC 500–1,000** → RBC 12,000 คาดว่ามี WBC จากเลือด 12–24 ตัว ค่าที่วัดได้ 18 จึง **อธิบายได้ด้วยเลือดปน**\n\n"
         "**ทำไมข้ออื่นผิด** — **CSF มีเลือดไม่ได้แปลว่า SAH** · **WBC 18 ไม่ได้แปลว่าติดเชื้อ** ถ้ายังไม่แก้ค่า · **เลือดแข็งตัวสนับสนุน traumatic tap** ไม่ใช่ SAH · **xanthochromia ต้องรอราว 12 ชั่วโมง** หลังเลือดออก ผลลบที่ 2 ชั่วโมงจึงตัด SAH ไม่ได้ ถ้ายังสงสัยให้ทำ CT angiography หรือเจาะซ้ำที่ระดับสูงขึ้นหลังครบ 12 ชั่วโมง ไม่ใช่เจาะซ้ำทันทีที่เดิม",
         "Traumatic tap: จางลง แข็งตัว ส่วนบนใส · แก้ WBC 1 ต่อ RBC 500–1,000",
         "Traumatic tap vs SAH", RL("Lumbar puncture: Traumatic tap vs SAH · CSF correction"),
         ["B3.3(2)", "3.1.7", "2.3.6(3)"]),
     mcq("NEU-LP-MCQ-18",
         "A 30-year-old man with HIV presents with 3 weeks of headache. CSF: opening pressure 42 cmH₂O, clear appearance, WBC 30/µL (lymphocytes 85%), protein 90 mg/dL, glucose 35 mg/dL (serum 110 mg/dL), Gram stain negative. Which test on this CSF is most sensitive for the most likely diagnosis?",
         "Cryptococcal antigen (CrAg)",
         ["India ink stain", "Ziehl–Neelsen stain for acid-fast bacilli", "PCR for HSV and enterovirus", "Latex agglutination for bacterial antigens"],
         2,
         "**ตอบ: cryptococcal antigen** — ภาพเข้ากับ **cryptococcal meningitis**: HIV · **opening pressure สูงมาก (> 25 ตามตาราง handout)** · ใส · lymphocyte เซลล์ไม่มาก · glucose ต่ำ (ratio ≈ 0.32) · Gram ลบ\n\n"
         "**ทำไม CrAg ไวที่สุด** — ตรวจจับ **polysaccharide ของแคปซูล** ที่ละลายอยู่ใน CSF จำนวนมาก ไม่ต้องเห็นตัวเชื้อ · handout: **CrAg ไว > 95%** · **India ink ไวเพียง 50–80%** เพราะต้องเห็นเชื้อในหยดน้ำที่ส่อง\n\n"
         "**ทำไมข้ออื่นผิด** — **India ink** ใช้ได้เร็วแต่พลาดได้มาก · **Ziehl–Neelsen** สำหรับ TB meningitis ซึ่งโปรตีนมักสูงกว่านี้และความดันไม่สูงเท่า (และย้อมติดน้อย) · **PCR HSV/enterovirus** สำหรับ viral ที่ glucose ปกติ · **latex agglutination** สำหรับแบคทีเรียซึ่งเซลล์มากเด่น neutrophil · ผู้ป่วยรายนี้ต้อง **เจาะระบายความดันซ้ำ** ด้วย (หัวข้อ 7)",
         "HIV + OP สูงมาก + lymphocyte เซลล์น้อย glucose ต่ำ → crypto → CrAg ไว > 95%",
         "CSF interpretation — cryptococcal meningitis", RL("Lumbar puncture: CSF analysis in meningitis"),
         ["B3.3(2)", "B3.2.2(1)", "2.3.1-3(7)"]),
     mcq("NEU-LP-MCQ-19",
         "A 26-year-old woman has painful monocular visual loss followed 6 months later by numbness ascending from both legs. CSF: WBC 12/mm³ (lymphocytes), protein 52 mg/dL, glucose normal, Gram stain and PCR negative. Which CSF finding most strongly supports the most likely diagnosis?",
         "Oligoclonal IgG bands present in CSF but absent in serum",
         ["Neutrophil predominance with low glucose", "Normal cell count with protein of 250 mg/dL",
          "Opening pressure above 40 cmH₂O", "Positive India ink stain"],
         3,
         "**ตอบ: oligoclonal band ใน CSF ที่ไม่มีใน serum** — ประวัติ optic neuritis แล้วตามด้วยอาการไขสันหลังต่างเวลา = **multiple sclerosis** ซึ่ง handout ระบุว่า **OCB \"highly diagnostic\"** ร่วมกับ IgG index สูงและ lymphocyte 5–50\n\n"
         "**กลไก** — B cell/plasma cell กลุ่มเล็ก ๆ ที่เข้ามาอยู่ในระบบประสาทกลางสร้าง IgG เองในช่อง CSF (intrathecal synthesis) แต่ละกลุ่มให้แถบเดียวบน electrophoresis จึงเห็นเป็น **หลายแถบใน CSF แต่ไม่มีใน serum** · ใช้แทนเกณฑ์ dissemination in time ได้ในเกณฑ์ McDonald 2017\n\n"
         "**ทำไมข้ออื่นผิด** — **neutrophil + glucose ต่ำ** = bacterial · **เซลล์ปกติโปรตีนสูงมาก** = cyto-albuminologic dissociation ของ **GBS** · **ความดันสูงมาก** = cryptococcal หรือ IIH · **India ink** = cryptococcus",
         "MS: lymphocyte 5–50 · โปรตีนสูงเล็กน้อย · OCB เฉพาะใน CSF",
         "CSF in inflammatory disease — MS", RL("Lumbar puncture: CSF in inflammatory conditions"),
         ["B3.3(2)", "3.1.7"]),
     ],
    ["lp2_tubes"]))

LP_CALLOUTS = {
    "neuro-lp-01": "> **เพิ่มจาก handout อ.ปองปวีณ์ (หัวข้อ 7)** — handout จัด **IIH และ cryptococcal meningitis ใน HIV** เป็น **therapeutic release** (ระบาย CSF เพื่อลดความดัน = การรักษา) ไม่ใช่แค่ข้อบ่งชี้เพื่อวินิจฉัยอย่างในรายการข้างบน · เพิ่ม **intrathecal analgesics** และ **metastasis** ในกลุ่มมะเร็ง",
    "neuro-lp-02": "> **เทียบกับ handout อ.ปองปวีณ์ (หัวข้อ 7–8)** — handout ให้เกณฑ์เป็นตัวเลข: **platelet < 20,000/mm³ ห้ามเจาะ (ควร > 50,000)** · **UFH หรือ LMWH ภายใน 24 ชั่วโมง** · coagulopathy · vertebral trauma · obstructive hydrocephalus · cord compression เหนือระดับที่เจาะ · handout ใช้เข็ม **20G หรือ 22G** เป็นอุปกรณ์มาตรฐาน ซึ่งไม่ขัดกับข้อ 1 ข้างบน: ถ้าเลือกได้ เข็มเล็กลงหรือ atraumatic ลด post-LP headache · ระดับที่แทง **L3–4 หรือ L4–5** เพราะ conus ปกติจบที่ **L1**",
    "neuro-lp-03": "> **handout อ.ปองปวีณ์ เพิ่มภาวะแทรกซ้อนอีกสองอย่าง** — **spinal hematoma** และ **chronic adhesive arachnoiditis จากน้ำยาฆ่าเชื้อ** · รายละเอียดและกลไกของ post-LP headache ด้านเข็ม (bevel, atraumatic) อยู่ในหัวข้อ 8",
    "neuro-lp-04": "> **handout อ.ปองปวีณ์** — เก็บ **3–5 mL ต่อขวด** · ค่าปกติของ CSF ตาราง meningitis สี่แบบ CSF ในโรคอักเสบ traumatic tap กับ SAH และสูตรแก้ค่าเมื่อมีเลือดปน อยู่ในหัวข้อ 9",
}
LP_GUIDE = [
    "**Handout อ.ปองปวีณ์ (Pongpawee Ekudomsuphan) — Lumbar puncture** (หัวข้อ 7–9) อ้าง StatPearls NBK557553 · PMC6707491 (contraindications, CSF ใน meningitis) · PMC5607637 (CSF correction)",
    "**WHO 2022 — Guidelines for diagnosing, preventing and managing cryptococcal disease** — therapeutic LP เมื่อ opening pressure สูง",
]

# ═════════════════════════════════════════════════════════════════════ ACS 21/10
ACSSRC = "handout 2026 อ.เพชรรัตน์ (Petcharat Dusitanond, MD, Neurologist) — Acute confusional state and Alteration of consciousness · คาบ 21 ต.ค. 2569"
RA = lambda p: ["สไลด์ อ.เพชรรัตน์ — " + p]
RQ = ["สไลด์ อ.เพชรรัตน์ — Delirium Quiz ในคาบ 21 ต.ค. 2026"]
ACS = []

ACS.append(sec("neuro-acs-16", "ที่อาจารย์เน้นในคาบ 21 ต.ค. 2026 (handout + Delirium quiz)",
    "เฉลย Delirium quiz หกข้อที่ทำในห้อง · สิ่งที่อาจารย์เขียนเน้น · จุดที่ต่างจากหัวข้อ 1–15", 12,
    ACSSRC, ["2.1.78", "B3.2.9(2)", "2.2.36", "B3.2.5(4)"],
"""หัวข้อ 16–19 มาจาก **handout ปี 2026 ของ อ.เพชรรัตน์ ดุสิตานนท์** (Petcharat Dusitanond, MD, Neurologist) ที่บรรยายวันที่ 21 ต.ค. 2569 · handout ฉบับนี้มี **ภาพหน้าจอ Delirium Quiz (Google Form) ที่ทำในห้อง** และลายมือของผู้ใช้ — คำถามในควิซคือสิ่งที่อาจารย์ต้องการให้รู้แน่ ๆ

### Delirium Quiz — เฉลยและเหตุผลสั้น
| ข้อ | คำถาม (ย่อ) | คำตอบ | เหตุผลหนึ่งบรรทัด |
|---|---|---|---|
| 1 | สารสื่อประสาทใดมีบทบาทสำคัญใน delirium | **Acetylcholine** | **ACh ขาด** เป็นกลไกหลักของสมาธิเสีย · ยา anticholinergic ทำให้เกิด delirium ได้เอง |
| 2 | Delirium ชนิดใดพบบ่อยที่สุด | **Hypoactive** | ✍️ "Mostly" บนสไลด์ · เงียบจึงถูกมองข้าม |
| 3 | อายุเท่าใดขึ้นไปเพิ่มความเสี่ยง | **65 ปี** | ปัจจัยเสี่ยงตาม NICE CG103 |
| 4 | หญิง 78 ปีมีผู้ดูแลประจำ ควรซักประวัติจากใคร | **ผู้ดูแลประจำ** | เห็น baseline และการเปลี่ยนแปลงทุกวัน |
| 5 | Digit span ปกติในผู้ใหญ่ | **5–7 ตัว** | ทวนตัวเลขไปข้างหน้าได้ไม่ถึง 5 = สมาธิเสีย |
| 6 | ชาย 40 ปี หยุดสุรา 3 วัน สับสน สั่น ภาพหลอน ไข้ ชีพจรเร็ว | **Alcohol withdrawal (delirium tremens)** | ช่วงเวลา 48–96 ชม. + autonomic hyperactivity |

> **ที่มาของควิซ** — อ่านได้จากข้อความ OCR ของภาพหน้าจอเท่านั้น (ไฟล์ 25 MB ใหญ่เกินกว่าจะเปิดดูภาพได้) จึงอาจมีข้อที่ OCR ไม่ติด · ข้อ 1 มีเครื่องหมาย × กำกับ และ OCR พบตัวเลือก Substance P ถูกทำเครื่องหมาย จึงน่าจะเป็นข้อที่ตอบพลาด — ดูเหตุผลในข้อ NEU-ACS-MCQ-31

[[fig:acs2_dts]]

### สิ่งที่อาจารย์เน้น (ไฮไลต์และลายมือบน handout)
- **Hypoactive = mostly** — ชนิดที่พบบ่อยที่สุด (สอดคล้องกับหัวข้อ 13)
- **ตรวจหา localizing sign เสมอ** — ✍️ เขียนต่อท้ายว่า **structural brain: stroke, tumor** → มี localizing sign ต้องทำภาพสมอง
- **Haloperidol** — ✍️ **EPS** และ **QT prolong → torsades de pointes** (ใช้ขนาดต่ำเมื่อจำเป็นเท่านั้น)
- **Trazodone** ที่ใช้ช่วยนอน — ✍️ **serotonin syndrome**
- **Reduced sensory input** ใน DELIRIUM — ✍️ "loss sensory" → คืนแว่นและเครื่องช่วยฟัง
- **Asterixis และ multifocal myoclonus** — ✍️ **metabolic** encephalopathy
- **Pupillary light reflex ทนต่อภาวะเมแทบอลิกมาก** — ผู้ป่วยซึมที่รูม่านตายังตอบสนองดี ให้คิดถึงเมแทบอลิกก่อน · **CN III palsy** ✍️ มี **ptosis** ร่วม
- **RAS เป็น "สวิตช์ไฟหลัก"** — handout มีภาพแบบกดดูนิวเคลียส (หัวข้อ 18)

### จุดที่ handout 2026 ต่างจากหัวข้อ 1–15
| เรื่อง | หัวข้อเดิม | handout 2026 | ใช้อย่างไร |
|---|---|---|---|
| **ระดับความรู้สึกตัว** | สี่ระดับ: alert · lethargy · stupor · coma | **ห้าระดับ: drowsiness · lethargy · obtundation · stupor · coma** | ทั้งสองแหล่งย้ำว่า **บรรยายสิ่งที่เห็นจริง** (หัวข้อ 19) |
| **Caloric test** | น้ำเย็นจัด 10 มล. | **น้ำเย็น 50 mL (≤ 30 °C) ใน 30 วินาที · รอ 1 นาที · เว้น 5 นาทีระหว่างหู** | ตอบตามอาจารย์ในคาบ · ปริมาณต่างกันตามตำรา หลักการเหมือนกัน |
| **นิยาม delirium** | DSM-5 ห้าข้อ | **Alexander & Needham 2023** — fluctuating · inattention เด่น · awareness เปลี่ยน + visual hallucination · สัมพันธ์กับตัวกระตุ้น | ใช้คู่กัน (หัวข้อ 17) |
| **การดูแล** | ห้าหัวข้อของสไลด์เดิม | **Marcantonio NEJM 2017 สี่ขั้น + DELIRIUM** | หัวข้อ 17 |
| **ยาที่ทำให้สับสน** | Usual suspects | **เพิ่มยาปฏิชีวนะ** (cefepime, quinolone, carbapenem, metronidazole ฯลฯ) | หัวข้อ 17 |
| **การนอน** | สามอาการของ circadian disruption | **two-process model · GABA/orexin · melatonin, ramelteon, DORA, dexmedetomidine** | หัวข้อ 18 |
| **Ocular bobbing** | ลงเร็ว ค้าง แล้วกลับช้า | ลงเร็วกลับช้า **และไม่มีการกลอกตาแนวนอน** · เพิ่ม sustained up/down gaze | หัวข้อ 19 |""",
    ["Delirium quiz: ACh · hypoactive · อายุ ≥ 65 · ซักประวัติจากผู้ดูแลประจำ · digit span 5–7 · delirium tremens",
     "Localizing sign ใน delirium → คิดถึงรอยโรคโครงสร้าง ทำภาพสมอง",
     "Haloperidol: EPS + QT ยาว (torsades) · trazodone: serotonin syndrome",
     "Light reflex ทนต่อเมแทบอลิก → ซึมแต่รูม่านตาตอบสนองดี = คิดถึงเมแทบอลิก",
     "Handout 2026: ระดับความรู้สึกตัว 5 ระดับ · caloric น้ำเย็น 50 mL"],
    [mcq("NEU-ACS-MCQ-31",
         "สาร neurotransmitter ใดต่อไปนี้ มีบทบาทสำคัญที่สุดในการเกิด delirium",
         "Acetylcholine",
         ["Dopamine", "Glutamate", "Substance P", "Oxytocin"],
         0,
         "**ตอบ: Acetylcholine** — กลไกหลักที่ได้รับการยอมรับมากที่สุดของ delirium คือ **cholinergic deficiency** (สไลด์: ARAS dysfunction สัมพันธ์กับ **ACh ขาด และ dopamine เกิน**)\n\n"
         "**กลไก** — เครือข่ายสมาธิและความตื่นตัว (pedunculopontine/basal forebrain → thalamus → cortex) ใช้ ACh เป็นหลัก · ภาวะที่ทำให้เกิด delirium แทบทุกชนิดไปลด ACh: **ขาดออกซิเจนหรือน้ำตาล** (การสร้าง ACh ต้องใช้ acetyl-CoA จากการเผาผลาญกลูโคส) · **cytokine** · **ยา anticholinergic** · หลักฐานสนับสนุนคือ **ยา anticholinergic ทำให้เกิด delirium ได้เอง** และ **anticholinergic burden สูงสัมพันธ์กับ delirium**\n\n"
         "**ทำไมตัวเลือกอื่นไม่ใช่คำตอบที่ดีที่สุด** — **Dopamine** เกินเป็นอีกด้านของความไม่สมดุล (จึงใช้ haloperidol ลดอาการกระวนกระวาย) แต่เป็นผลที่ตามมาเมื่อเทียบกับ ACh ที่ขาด · **Glutamate** เกี่ยวกับ excitotoxicity และภาวะถอนสุรา แต่ไม่ใช่กลไกร่วมหลัก · **Substance P** เป็น neuropeptide ของทางเดินความเจ็บปวดและการคลื่นไส้ (ตัวรับ NK1) **ไม่มีบทบาทที่ยอมรับใน delirium** — ภาพหน้าจอควิซดูเหมือนเลือกข้อนี้และมีเครื่องหมายผิด · **Oxytocin** ไม่เกี่ยวข้อง",
         "Delirium = ACh ขาด + dopamine เกิน · ยา anticholinergic จึงเป็นตัวการบ่อย",
         "Delirium pathophysiology (quiz)", RQ, ["2.1.78", "B3.2.9(2)", "B3.1.2(4)"]),
     mcq("NEU-ACS-MCQ-32",
         "Delirium type ใดพบบ่อยที่สุด",
         "Hypoactive",
         ["Hyperactive", "Mixed", "พบพอ ๆ กันทุกชนิด", "Catatonic"],
         2,
         "**ตอบ: Hypoactive** — handout แบ่งสามชนิด และมีลายมือ **\"Mostly\"** กำกับที่ hypoactive\n\n"
         "**ทำไมพบบ่อยแต่ถูกมองข้าม** — ผู้ป่วย **ซึม เฉื่อย เฉยเมย (motor retardation, apathy)** ไม่รบกวนใคร จึงถูกบันทึกว่า \"หลับดี\" หรือ \"ซึมเศร้า\" · กลไกที่ทำให้เป็นชนิดนี้มักเป็น **cytokine จากการติดเชื้อ ยากดประสาท และภาวะเมแทบอลิก** ซึ่งกดการทำงานของสมองมากกว่ากระตุ้น · ผู้สูงอายุที่ apathy lethargy หรืออารมณ์ซึม **ต้องประเมิน delirium** (handout)\n\n"
         "**ทำไมข้ออื่นผิด** — **hyperactive** เด่นชัดจึงถูกจดจำ แต่เป็นส่วนน้อย (พบมากในภาวะถอนสุราและผู้ป่วยอายุน้อย) · **mixed** พบรองลงมา · สัดส่วน **ไม่เท่ากัน** · **catatonic ไม่ใช่ชนิดย่อยมาตรฐานของ delirium**",
         "Hypoactive พบบ่อยที่สุด — ต้องคัดกรองเชิงรุก ไม่รอให้ผู้ป่วยโวยวาย",
         "Delirium subtypes (quiz)", RQ, ["2.1.78", "B3.2.9(2)"]),
     mcq_fixed("NEU-ACS-MCQ-33",
         "จากข้อมูลงานวิจัย อายุตั้งแต่เท่าใดขึ้นไป เพิ่มความเสี่ยงต่อการเกิด delirium",
         ["40 ปี", "50 ปี", "55 ปี", "60 ปี", "65 ปี"], 4,
         "**ตอบ: 65 ปีขึ้นไป** — แนวทาง **NICE CG103** ระบุปัจจัยเสี่ยงสำคัญของ delirium ในผู้ป่วยในโรงพยาบาลคือ **อายุ ≥ 65 ปี · มีภาวะสมองเสื่อมหรือการรู้คิดบกพร่องเดิม · กระดูกสะโพกหัก · เจ็บป่วยรุนแรง** และให้คัดกรองทุกรายที่มีปัจจัยเหล่านี้\n\n"
         "**กลไก** — handout: ความน่าจะเป็นของ delirium = **ความเปราะบางของสมองเดิม (predisposing) × ความรุนแรงของสิ่งกระตุ้น (precipitating)** · อายุมากทำให้ **ACh สำรองลดลง BBB รั่วขึ้น microglia ไวต่อการอักเสบ** สิ่งกระตุ้นเล็กน้อยก็ข้ามเกณฑ์ได้\n\n"
         "**ทำไมตัวเลขอื่นผิด** — 40–60 ปีไม่ใช่จุดตัดที่ใช้ในแนวทางหรือแบบประเมินความเสี่ยงหลัก · ความเสี่ยงเพิ่มต่อเนื่องตามอายุ แต่จุดตัดที่ใช้คัดกรองคือ **65 ปี**",
         "อายุ ≥ 65 ปี + สมองเสื่อมเดิม + สะโพกหัก + ป่วยหนัก = กลุ่มเสี่ยง delirium ต้องคัดกรอง",
         "Delirium risk factors (quiz)", RQ, ["2.1.78", "B3.2.9(2)"]),
     mcq("NEU-ACS-MCQ-34",
         "ผู้ป่วยหญิง 78 ปี ลูกสาวพามาโรงพยาบาลเนื่องจากมีอาการสับสนมา 2 วัน เดิมผู้ป่วยช่วยเหลือตนเองได้น้อย มีโรคประจำตัว DM, HT, DLP และ old ischemic stroke มีผู้ดูแลประจำ ลูกสาวอยู่บ้านติดกันและแวะมาเยี่ยมเป็นครั้งคราว ท่านเป็นแพทย์ที่ดูแล ควรซักประวัติจากใครเหมาะสมที่สุด",
         "ผู้ดูแลประจำ",
         ["ผู้ป่วย", "ลูกสาวที่พามาโรงพยาบาล", "แพทย์ที่เคยดูแลผู้ป่วย", "เพื่อนบ้าน"],
         3,
         "**ตอบ: ผู้ดูแลประจำ** — การวินิจฉัย delirium ต้องอาศัย **CAM feature 1: การเปลี่ยนแปลงเฉียบพลันจาก baseline และอาการขึ้นลง** ข้อมูลนี้ได้จาก **คนที่อยู่กับผู้ป่วยทุกวัน** เท่านั้น\n\n"
         "**เหตุผล** — handout: delirium เป็น **clinical diagnosis** ที่ประวัติและการตรวจช่วยมากกว่าการตรวจใด ๆ และให้เก็บข้อมูลจาก **เพื่อน ครอบครัว เพื่อนบ้าน และบันทึกของผู้ดูแล** · ผู้ดูแลประจำบอกได้ว่า **เดิมทำอะไรได้แค่ไหน เริ่มเปลี่ยนเมื่อไร เปลี่ยนเร็วแค่ไหน ขึ้นลงช่วงไหนของวัน กินยาอะไร หกล้มหรือไม่ กินดื่มขับถ่ายอย่างไร** ซึ่งเป็นกุญแจแยก delirium จาก dementia เดิม\n\n"
         "**ทำไมข้ออื่นด้อยกว่า** — **ผู้ป่วย** กำลังสับสนและสมาธิเสีย ข้อมูลเชื่อถือไม่ได้ (แต่ยังต้องตรวจสภาพจิตของผู้ป่วยเอง) · **ลูกสาว** เห็นเป็นครั้งคราว อาจไม่รู้ baseline ล่าสุดหรือช่วงที่อาการขึ้นลง · **แพทย์เดิม** และเวชระเบียนให้ข้อมูลโรคและยาที่มีค่า แต่ไม่เห็นการเปลี่ยนแปลงสองวันที่ผ่านมา · **เพื่อนบ้าน** ห่างกว่าผู้ดูแล",
         "Delirium: ซักประวัติจากคนที่เห็นผู้ป่วยทุกวัน — baseline · onset · fluctuation · ยา",
         "Delirium — history taking (quiz)", RQ, ["2.1.78", "B3.2.9(2)"]),
     mcq_fixed("NEU-ACS-MCQ-35",
         "การตรวจ digit span (ทวนตัวเลขไปข้างหน้า) ในผู้ใหญ่ที่สุขภาพและสมองปกติ จะพูดตามผู้ตรวจได้กี่ตัวเลข",
         ["3–4 ตัว", "5–7 ตัว", "8–10 ตัว", "11–13 ตัว", "14 ตัวขึ้นไป"], 1,
         "**ตอบ: 5–7 ตัว** — ผู้ใหญ่ปกติทวนตัวเลขไปข้างหน้าได้ราว **7 ± 2** และ **ได้อย่างน้อย 5 ตัว** · ถ้าได้น้อยกว่า 5 ตัว (ไม่มีปัญหาภาษาหรือการได้ยิน) แปลว่า **สมาธิเสีย**\n\n"
         "**กลไก** — digit span ทดสอบ **working memory ระยะสั้นมาก** ที่ต้องอาศัยการจดจ่อต่อเนื่องไม่กี่วินาที ไม่ได้ทดสอบความจำระยะยาว จึงใช้เป็น **การทดสอบสมาธิ** ซึ่งเป็น feature 2 ของ CAM · วิธีทำ: พูดตัวเลขสุ่มทีละ 1 ตัวต่อวินาที เริ่มจาก 3 ตัว เพิ่มทีละตัวจนผิดสองครั้ง · การทวนถอยหลังมักได้น้อยกว่าไปข้างหน้า 1–2 ตัว\n\n"
         "**ทำไมข้ออื่นผิด** — **3–4 ตัว** ผิดปกติ (สมาธิเสีย) · **8–10** อยู่ปลายบนของคนเพียงบางส่วน ไม่ใช่ช่วงปกติทั่วไป · **11–13 และ 14 ขึ้นไป** เกินความจุของ working memory โดยไม่ใช้เทคนิคช่วยจำ",
         "Digit span ไปข้างหน้า < 5 = inattention · ปกติ 7 ± 2",
         "Attention testing — digit span (quiz)", RQ, ["2.1.78", "B3.2.9(2)"]),
     mcq("NEU-ACS-MCQ-36",
         "ผู้ป่วยชาย 40 ปี ถูกนำส่งโรงพยาบาลเนื่องจากมีอาการสับสนเฉียบพลัน พูดจาไม่รู้เรื่อง มือสั่นทั้งสองข้าง เห็นภาพหลอน กระสับกระส่าย เหงื่อออกมาก มีประวัติหยุดดื่มสุรามาได้ 3 วัน ปฏิเสธโรคประจำตัวเนื่องจากไม่เคยตรวจร่างกาย ตรวจร่างกาย T 40 °C, PR 110/min, RR 25/min, BP 160/100 mmHg, disorientation to time, place, person, inattention, cannot follow simple command, normal extraocular movement, coarse tremor of both hands สาเหตุใดเป็นไปได้มากที่สุด",
         "Alcohol withdrawal (delirium tremens)",
         ["Meningoencephalitis", "Hepatic encephalopathy", "Neuroleptic malignant syndrome", "Wernicke encephalopathy"],
         1,
         "**ตอบ: alcohol withdrawal — delirium tremens** — หยุดดื่ม **72 ชั่วโมง** (ช่วง DT 48–96 ชั่วโมง) + **delirium** (สับสน สมาธิเสีย ภาพหลอน) + **autonomic hyperactivity** (ไข้ ชีพจรเร็ว หายใจเร็ว BP สูง เหงื่อท่วม) + **coarse tremor**\n\n"
         "**กลไก** — สุราเสริม GABA-A และกด NMDA อยู่นาน สมองปรับตัวโดย **ลดตัวรับ GABA เพิ่มตัวรับ NMDA** · เมื่อหยุดดื่ม แรงยับยั้งหายทันทีแต่ระบบกระตุ้นยังสูง → **glutamate และ norepinephrine พุ่ง** → สั่น ชัก ภาพหลอน sympathetic ทำงานเกิน ไข้\n\n"
         "**ทำไมข้ออื่นผิด** — **meningoencephalitis** ต้องคิดเสมอเพราะไข้ 40 °C (ถ้ามีคอแข็ง อาการไม่ดีขึ้นด้วย benzodiazepine หรือไม่มีประวัติถอนสุราชัด ต้องเจาะหลัง) แต่ภาพทั้งหมดอธิบายด้วยการถอนสุราได้ดีกว่า · **hepatic encephalopathy** มักซึม มี asterixis ดีซ่าน ไม่มี sympathetic เกินแบบนี้ · **NMS** ต้องมีประวัติได้ยาต้านโรคจิต และเด่นที่ **กล้ามเนื้อแข็งแบบ lead pipe** ไม่ใช่สั่น · **Wernicke** มี ophthalmoplegia/nystagmus และเดินเซ แต่ผู้ป่วยรายนี้ **กลอกตาปกติ** — ถึงอย่างนั้นทุกรายต้องได้ **thiamine ก่อนกลูโคส** · การรักษา DT คือ **benzodiazepine** (เป็นข้อยกเว้นที่ BZD รักษา delirium ได้)",
         "หยุดสุรา 48–96 ชม. + delirium + ไข้ ชีพจรเร็ว BP สูง เหงื่อ = delirium tremens → BZD + thiamine",
         "Delirium — alcohol withdrawal (quiz)", RQ, ["2.1.78", "B3.2.5(4)", "2.3.5(1)"]),
     ],
    ["acs2_dts"]))

ACS.append(sec("neuro-acs-17", "Delirium ตาม handout 2026: นิยาม 3D-CAM สี่ขั้นการดูแล DELIRIUM ยาและยาปฏิชีวนะ",
    "Alexander & Needham 2023 · 3D-CAM · delirium/dementia/depression · Marcantonio สี่ขั้น · DELIRIUM · ยาและยาปฏิชีวนะที่ทำให้สับสน · การส่งตรวจตามไข้และ focal sign", 14,
    ACSSRC, ["2.1.78", "B3.2.9(2)", "2.3.5-3(5)", "B3.4(4)", "2.3.19(1)"],
"""### นิยามที่ใช้ในคาบนี้ (Alexander SK, Needham E. Pract Neurol 2023)
**Delirium** = ความผิดปกติเฉียบพลันของ **สมาธิและความตื่นรู้ที่ขึ้นลง** มีลักษณะเฉพาะที่ทำให้ **วินิจฉัยเชิงบวกได้** แยกจากสาเหตุอื่นของการสับสนเฉียบพลัน
- **Fluctuating course** — อาการขึ้นลงในวันเดียวกัน
- **Inattention เด่น** ร่วมกับการรู้คิดด้านอื่นเสีย
- **Awareness เปลี่ยน และ visual hallucination**
- **สัมพันธ์ทางเวลากับตัวกระตุ้น** และดีขึ้นเมื่อแก้หรือเอาตัวกระตุ้นออก

**สามชนิด** — hyperactive (กระวนกระวาย) · **hypoactive (เคลื่อนไหวช้า เฉยเมย) — พบบ่อยที่สุด** · mixed

**Delirium เป็น clinical diagnosis** — ประวัติและการตรวจร่างกายอย่างละเอียดช่วยได้มากกว่าการตรวจใด ๆ · ความน่าจะเป็น = **ความเปราะบางของสมอง (predisposing) × ความรุนแรงของภาวะทางกาย (precipitating)** (ภาพ threshold ในหัวข้อ 11)

### ประเมินผู้ป่วยตาม handout
- **ประวัติ** — จาก **เพื่อน ครอบครัว เพื่อนบ้าน** · บันทึกจากคลินิกเดิม รถพยาบาล และพยาบาล · ระยะเวลาและสถานที่ที่ได้รับการดูแล
- **ตรวจร่างกายทั่วไป** — สัญญาณชีพรวม **O₂ saturation** · หัวใจ ปอด ท้อง
- **ตรวจระบบประสาท** — มองหา **ลักษณะเฉพาะของ delirium** (การรู้คิดและพฤติกรรมขึ้นลง) และ **localizing sign** ✍️ ซึ่งชี้ไปที่ **รอยโรคโครงสร้าง เช่น stroke หรือ tumor** มากกว่าสมองทำงานผิดปกติทั่วไป

### CAM และ 3D-CAM (Marcantonio NEJM 2017)
- **CAM** — ต้องมี **feature 1 (เฉียบพลัน + ขึ้นลง) และ 2 (inattention)** ร่วมกับ **3 (disorganized thinking) หรือ 4 (ระดับความรู้สึกตัวเปลี่ยน)** (หัวข้อ 13)
- **3D-CAM** — สัมภาษณ์ที่มีโครงสร้าง **ใช้เวลาราว 3 นาที** ถามคำถามทดสอบสมาธิและการรับรู้ (เช่น บอกวัน ทวนตัวเลขถอยหลัง บอกวันในสัปดาห์ถอยหลัง) แล้วให้ผู้ตรวจสังเกต · **ครั้งแรก**: ข้อมูลการเปลี่ยนแปลงจากเวชระเบียนหรือญาติถือว่ามี feature 1 · **ครั้งต่อมา**: ตอบผิดใหม่หรือมีอาการใหม่เมื่อเทียบครั้งก่อน = feature 1 · ผู้ป่วยต้อง **หลับจริงระหว่างสัมภาษณ์** จึงนับว่าง่วงผิดปกติ

### Delirium · dementia · depression — ต้องแยกก่อนรักษา
| | Delirium | Dementia | Depression |
|---|---|---|---|
| **เริ่ม** | เฉียบพลัน ชั่วโมงถึงวัน | ค่อยเป็นค่อยไป เดือนถึงปี | สัปดาห์ถึงเดือน มักมีเหตุการณ์นำ |
| **ขึ้นลงในวัน** | **ขึ้นลงชัด** แย่ตอนกลางคืน | ค่อนข้างคงที่ | แย่ตอนเช้าได้ |
| **สมาธิ** | **เสียตั้งแต่แรก** | ปกติจนระยะท้าย | ลดลงจากแรงจูงใจ แต่ทดสอบได้ |
| **ระดับความรู้สึกตัว** | **เปลี่ยน** (ซึมหรือตื่นเกิน) | ปกติ | ปกติ |
| **การตอบคำถาม** | สับสน ไม่ตรงประเด็น | พยายามตอบ ปิดบังด้วยการเลี่ยง | **\"ไม่รู้\"** ไม่พยายาม |
| **การกลับคืน** | **กลับได้ถ้าแก้เหตุ** | ไม่กลับ | ดีขึ้นด้วยการรักษา |

(ตารางในสไลด์เป็นภาพที่อ่านไม่ได้ — ตารางนี้เรียบเรียงตามมาตรฐานของแหล่งที่สไลด์อ้าง health.vic.gov.au)
- **ผู้สูงอายุที่ apathy, lethargy หรืออารมณ์ซึม ต้องประเมิน delirium** — hypoactive delirium มักถูกเรียกว่าซึมเศร้า
- **ผู้สูงอายุที่ความจำเสีย ต้องคัดกรองซึมเศร้า** — ซึมเศร้าทำให้ดูเหมือนสมองเสื่อมได้ (pseudodementia)
- **Dementia อาจมาพร้อมหรือนำด้วยช่วงที่มีอาการซึมเศร้า**

### การดูแล delirium สี่ขั้น (Marcantonio NEJM 2017)
**1) ประเมินและแก้ปัจจัยที่แก้ได้ — DELIRIUM**
| อักษร | สาเหตุ | ตัวอย่างที่ต้องดู |
|---|---|---|
| **D** | **Drugs** | ยาใหม่ ยาเพิ่มขนาด ยาที่มีฤทธิ์ต่อสมอง (ตารางด้านล่าง) |
| **E** | **Electrolyte disturbances** | Na · Ca · glucose · ภาวะขาดน้ำ · ไต/ตับ/ไทรอยด์ |
| **L** | **Lack of drugs** | ภาวะถอนสุราหรือยานอนหลับ · **ความเจ็บที่ควบคุมไม่พอ** |
| **I** | **Infection** | ทางเดินปัสสาวะ ปอด ผิวหนัง |
| **R** | **Reduced sensory input** ✍️ | ไม่ได้ใส่แว่นหรือเครื่องช่วยฟัง |
| **I** | **Intracranial disorders** | stroke เลือดออก การติดเชื้อ ชัก (มองหา focal sign) |
| **U** | **Urinary and fecal disorders** | **ปัสสาวะคั่ง** · **อุจจาระอัดแน่น** |
| **M** | **Myocardial and pulmonary disorders** | MI · หัวใจล้มเหลว · ขาดออกซิเจน · CO₂ คั่ง |

**ยาที่เพิ่มความเสี่ยงหรือทำให้ delirium แย่ลง (handout)**
| กลุ่ม | ตัวอย่าง |
|---|---|
| **Benzodiazepines** | midazolam · lorazepam |
| **Non-BZD hypnotics** | zolpidem |
| **Anticonvulsants** | phenobarbital · phenytoin |
| **Antiparkinsonian** | levodopa · amantadine |
| **Antipsychotics โดยเฉพาะ low-potency typical** | chlorpromazine · thioridazine |
| **Alcohol** | |
| **Anticholinergics** | oxybutynin · benztropine · trihexyphenidyl |
| **TCA** | amitriptyline · imipramine · doxepin |
| **Antihistamines** | doxylamine · diphenhydramine · chlorpheniramine |
| **H2 blockers** | cimetidine · ranitidine · famotidine |
| **Opioids** | **meperidine** |

**ยาปฏิชีวนะที่สัมพันธ์กับ delirium (Teng & Frei 2021)**
| กลุ่ม | ตัวอย่าง | กลไกที่เสนอ |
|---|---|---|
| **Cephalosporins** | **cefepime** · ceftazidime · cefuroxime · cefaclor | ต้าน **GABA-A** · cefepime สะสมเมื่อไตเสื่อมแล้วไม่ปรับขนาด → สับสน myoclonus non-convulsive status |
| **Carbapenems** | imipenem · ertapenem | ต้าน GABA-A · ชักง่าย |
| **Fluoroquinolones** | ciprofloxacin · levofloxacin · ofloxacin · moxifloxacin | ต้าน GABA-A และกระตุ้น NMDA |
| **Macrolides** | clarithromycin · azithromycin | กลไกไม่ชัด · clarithromycin ยับยั้ง CYP3A4 ทำให้ยาอื่นสะสม |
| **Metronidazole** | | พิษต่อสมองน้อยและ white matter เมื่อใช้นาน |
| **Linezolid** | | ยับยั้ง MAO → **serotonin syndrome** เมื่อใช้คู่ SSRI |
| **TMP-SMX** | | สับสนและประสาทหลอนในผู้สูงอายุ/HIV |
| **Penicillin + BLI** | ampicillin-sulbactam · piperacillin-tazobactam | ต้าน GABA-A เมื่อขนาดสูงหรือไตเสื่อม |

**2) ป้องกันและดูแลภาวะแทรกซ้อน** — ปัสสาวะราด · **นอนนิ่งและหกล้ม** · แผลกดทับ · การนอนผิดปกติ · การกินผิดปกติ (สำลัก ขาดอาหาร)

**3) ความสบายและความปลอดภัย**
- **พฤติกรรม** — สอนทีมให้ใช้เทคนิค **de-escalation** กับผู้ป่วย hyperactive · ให้ครอบครัวมาเยี่ยม · **หลีกเลี่ยงการผูกยึด**
- **ยา** — **high-potency antipsychotic ขนาดต่ำ (haloperidol) เฉพาะเมื่อจำเป็น** · ✍️ ระวัง **EPS** และ **QT ยาว → torsades de pointes**

**4) ฟื้นฟูการทำงาน**
- **สิ่งแวดล้อม** — ลดของเกะกะและเสียง · แสงสว่างพอ · ให้ญาตินำของคุ้นเคยจากบ้านมา
- **Cognitive reconditioning** — **บอกเวลา สถานที่ บุคคลซ้ำอย่างน้อยวันละสามครั้ง**
- **ADL** — กายภาพบำบัดและกิจกรรมบำบัด · เมื่อ delirium ดีขึ้นให้ทำเองตามความสามารถ
- **ครอบครัว** — อธิบายสาเหตุ การกลับคืนได้ วิธีสื่อสาร และบทบาทของครอบครัว
- **วางแผนจำหน่าย** — เพิ่มการช่วยกิจวัตรประจำวันตามจำเป็น · **สอนญาติใช้สภาพจิตเป็น \"barometer\" ของการฟื้นตัว**

### ส่งตรวจอะไร (algorithm ใน handout)
[[fig:acs2_labalgo]]

#### ทำไมถึงมีอาการนี้ — ยาที่ไม่ใช่ยาจิตเวชทำให้สับสนได้อย่างไร
| สิ่งที่พบ | กลไก | ใช้อย่างไร |
|---|---|---|
| **สับสนหลังได้ antihistamine, oxybutynin, TCA** | ปิดตัวรับ muscarinic ในเครือข่ายสมาธิ → ACh ใช้งานไม่ได้ · ร่วมกับปากแห้ง ปัสสาวะคั่ง ท้องผูก รูม่านตาขยาย | นับ **anticholinergic burden** รวมทุกตัว |
| **สับสน กระตุก หลังได้ cefepime ในไตเสื่อม** | ยาสะสม ผ่าน BBB ไปจับ GABA-A แบบต้าน → สมองถูกกระตุ้นเกิน · myoclonus หรือชักแบบไม่ชักกระตุก | ปรับขนาดตาม CrCl · หยุดยาแล้วดีขึ้นใน 1–3 วัน · EEG ถ้ายังซึม |
| **ภาวะถอนยา (Lack of drugs)** | ระบบที่ถูกกดนาน (GABA) ปรับตัวไว้ เมื่อขาดยาฉับพลันระบบกระตุ้นเด่น | ถามยานอนหลับและสุราที่ใช้ก่อนนอนโรงพยาบาล |
| **ปัสสาวะคั่ง อุจจาระอัด ทำให้สับสน** | ความเจ็บและแรงดันในกระเพาะปัสสาวะ/ลำไส้กระตุ้น sympathetic และขัดการนอน · ผู้ป่วยบอกไม่ได้ | ตรวจคลำท้อง bladder scan ตรวจทวาร — แก้ได้ทันที |""",
    ["นิยาม 2023: fluctuating · inattention เด่น · awareness เปลี่ยน + visual hallucination · สัมพันธ์กับตัวกระตุ้น",
     "3D-CAM = สัมภาษณ์มีโครงสร้าง 3 นาที ใช้อัลกอริทึม CAM เดิม",
     "สี่ขั้น: แก้ DELIRIUM → ป้องกันภาวะแทรกซ้อน → ปลอดภัย (ไม่ผูกยึด haloperidol ขนาดต่ำ) → ฟื้นฟู",
     "ยาปฏิชีวนะก็ทำให้สับสนได้: cefepime (ไตเสื่อม) · quinolone · carbapenem · metronidazole · linezolid",
     "ไม่มีไข้/คอแข็ง/focal → ชุดเมแทบอลิก + EKG + tox + หาการติดเชื้อ · ไข้หรือคอแข็ง → CSF · focal หรือชัก → ภาพสมอง + EEG"],
    [mcq("NEU-ACS-MCQ-37",
         "An 82-year-old woman with CKD (creatinine clearance 20 mL/min) is treated for hospital-acquired pneumonia. On day 3 she becomes confused, inattentive and has multifocal myoclonic jerks. Glucose, sodium and calcium are normal; CT brain is unremarkable. Which current medication is the most likely cause?",
         "Cefepime 2 g IV every 8 hours",
         ["Amlodipine 5 mg daily", "Paracetamol 500 mg every 6 hours", "Atorvastatin 20 mg nightly", "Omeprazole 20 mg daily"],
         4,
         "**ตอบ: cefepime ที่ไม่ได้ปรับขนาดตามไต** — handout จัด cephalosporins (โดยเฉพาะ **cefepime**) อยู่ในยาปฏิชีวนะที่สัมพันธ์กับ delirium (Teng & Frei 2021)\n\n"
         "**กลไก** — cefepime ขับทางไต ใน CrCl 20 ยาสะสมสูง ผ่าน BBB และ **จับ GABA-A แบบต้าน** → สมองขาดแรงยับยั้ง → **สับสน myoclonus และอาจเป็น non-convulsive status epilepticus** · ขนาด 2 g ทุก 8 ชั่วโมงเป็นขนาดของไตปกติ\n\n"
         "**สิ่งที่ควรทำ** — ลดขนาดหรือเปลี่ยนยา · ส่ง **EEG** ถ้ายังซึม (หา NCSE) · อาการมักดีขึ้นใน 1–3 วันหลังหยุด (รายรุนแรงอาจต้องฟอกเลือด)\n\n"
         "**ทำไมข้ออื่นผิด** — **amlodipine, paracetamol ขนาดปกติ, atorvastatin** ไม่ใช่ยาที่ทำให้เกิด delirium ร่วมกับ myoclonus · **omeprazole** เกี่ยวกับ hypomagnesemia ได้บ้าง แต่ไม่ใช่ตัวการที่น่าจะเป็นที่สุดเมื่อเทียบกับ cefepime ที่สะสม",
         "Delirium + myoclonus ในไตเสื่อมที่ได้ cefepime → นึกถึง cefepime neurotoxicity",
         "Delirium — antibiotic-associated", RA("Antibiotics linked to Delirium"), ["2.1.78", "B3.2.9(2)"]),
     mcq("NEU-ACS-MCQ-38",
         "A 70-year-old man becomes acutely confused on a medical ward. Temperature is 38.6 °C and there is marked neck stiffness; there is no focal neurological sign. According to the laboratory evaluation algorithm in the handout, which investigation must be added to the basic metabolic, ECG, toxicology and infection work-up?",
         "Cerebrospinal fluid examination by lumbar puncture (after CT if indicated)",
         ["EEG as the first test", "Serum ammonia only", "Thyroid function tests only", "No further tests until the confusion has lasted 7 days"],
         0,
         "**ตอบ: ตรวจ CSF** — algorithm ใน handout: **มีไข้หรือ meningeal sign → CSF (meningitis/encephalitis)** · **focal sign หรือชัก → CT/MRI และ EEG** · ไม่มีทั้งสองอย่าง → ชุดพื้นฐาน\n\n"
         "**เหตุผล** — meningitis ในผู้สูงอายุอาจมาด้วย **สับสนเป็นอาการเด่น** และเป็นสาเหตุที่ถึงตายแต่รักษาได้ · ผู้ป่วยอายุ > 60 ปีและระดับความรู้สึกตัวเปลี่ยน **ควรทำ CT ก่อนเจาะ** (หัวข้อ 2 ของคาบ LP) แต่ **ห้ามชะลอยาปฏิชีวนะ**\n\n"
         "**ทำไมข้ออื่นผิด** — **EEG** เป็นการตรวจเพิ่มเมื่อมีชักหรือสงสัย NCSE ไม่ใช่ข้อแรกเมื่อมีคอแข็ง · **ammonia หรือ thyroid อย่างเดียว** อยู่ในชุดเมแทบอลิกที่ต้องทำอยู่แล้ว แต่ไม่ตอบคำถามเรื่อง meningitis · **การรอ 7 วัน** ผิดหลัก delirium ที่ต้องหาเหตุทันที",
         "Delirium + ไข้/คอแข็ง → CSF · + focal/ชัก → ภาพสมอง + EEG",
         "Delirium — laboratory evaluation", RA("Laboratory evaluation of delirium patient"), ["2.1.78", "B3.3(2)", "2.3.6(5)"]),
     mcq("NEU-ACS-MCQ-39",
         "A 76-year-old man with hyperactive delirium from urosepsis is pulling at his intravenous line and has struck a nurse despite de-escalation and family presence. His QTc is 440 ms and he has no history of Parkinson's disease. Which pharmacological option best follows the handout?",
         "Low-dose haloperidol, with ECG monitoring for QT prolongation and observation for extrapyramidal signs",
         ["Chlorpromazine 50 mg IM", "Lorazepam 2 mg IV", "Diphenhydramine 50 mg IV", "Bilateral wrist restraints without medication for the next 24 hours"],
         2,
         "**ตอบ: haloperidol ขนาดต่ำ** — handout (Marcantonio 2017): **ใช้ high-potency antipsychotic ขนาดต่ำเฉพาะเมื่อจำเป็น** · ลายมือในคาบ: ระวัง **EPS** และ **QT ยาว → torsades de pointes** จึงต้องติดตาม ECG\n\n"
         "**กลไก** — haloperidol ต้าน **D2** แรงโดยแทบไม่มีฤทธิ์ anticholinergic จึงลดอาการจาก **dopamine ที่เด่นเกิน** โดยไม่ซ้ำเติม ACh ที่ขาด · ใช้เพื่อ **ความปลอดภัย** ระหว่างแก้เหตุ (urosepsis) ไม่ได้รักษา delirium เอง\n\n"
         "**ทำไมข้ออื่นผิด** — **chlorpromazine** เป็น low-potency typical ที่มีฤทธิ์ anticholinergic และ alpha-blockade สูง — **อยู่ในรายการยาที่ทำให้ delirium แย่ลง** และทำให้ความดันตก · **lorazepam** ทำให้ delirium ทั่วไปแย่ลงและยาวขึ้น (ใช้เฉพาะถอนสุรา/ยานอนหลับ) · **diphenhydramine** เป็น anticholinergic ตัวการสำคัญ · **การผูกยึด** handout ให้หลีกเลี่ยง เพิ่มความกระวนกระวาย บาดเจ็บ และยืดระยะ delirium",
         "จำเป็นต้องใช้ยา → haloperidol ขนาดต่ำ · ห้าม low-potency typical, BZD, antihistamine",
         "Delirium — pharmacological management", RA("Maintain patient comfort and safety"), ["2.1.78", "B3.4(4)", "2.2.25"]),
     mcq("NEU-ACS-MCQ-40",
         "An 84-year-old woman admitted with a hip fracture is described by nurses as 'quiet and depressed'. She lies still, speaks little, falls asleep during the interview and cannot name the days of the week backwards; her daughter says she was independent and chatty until 3 days ago. What is the most appropriate interpretation?",
         "Hypoactive delirium, which should prompt a search for precipitating causes",
         ["Major depressive disorder requiring an SSRI", "Progression of an undiagnosed dementia",
          "Normal response to hospitalisation in the elderly", "Hyperactive delirium requiring haloperidol"],
         3,
         "**ตอบ: hypoactive delirium** — เข้า CAM ครบ: **feature 1** เปลี่ยนเฉียบพลันจาก baseline ภายใน 3 วัน (จากลูกสาว) · **feature 2** บอกวันถอยหลังไม่ได้ (inattention) · **feature 4** หลับระหว่างสัมภาษณ์ (ใน 3D-CAM ต้องหลับจริงจึงนับ)\n\n"
         "**หลักจาก handout** — **ผู้สูงอายุที่ apathy, lethargy หรืออารมณ์ซึม ต้องประเมิน delirium** · กระดูกสะโพกหักเป็นทั้งปัจจัยเสี่ยงและตัวกระตุ้น (ความเจ็บ ยาแก้ปวด เลือดออก ปัสสาวะคั่ง) → หาเหตุด้วย **DELIRIUM**\n\n"
         "**ทำไมข้ออื่นผิด** — **ซึมเศร้า** ไม่ทำให้ระดับความรู้สึกตัวลดและไม่เกิดใน 3 วัน · **สมองเสื่อม** ค่อยเป็นค่อยไป สมาธิดีในระยะแรก · **ไม่ใช่เรื่องปกติของผู้สูงอายุ** — delirium เพิ่มอัตราตาย · **ไม่ใช่ hyperactive** และ hypoactive ไม่มีข้อบ่งชี้ให้ยาต้านโรคจิต",
         "เงียบ ซึม หลับง่าย + สมาธิเสีย + เปลี่ยนเร็ว = hypoactive delirium ไม่ใช่ซึมเศร้า",
         "Delirium vs depression vs dementia", RA("Features differentiate among delirium, dementia, depression"), ["2.1.78", "B3.2.9(2)", "2.3.5-3(5)"]),
     ],
    ["acs2_labalgo"]))

ACS.append(sec("neuro-acs-18", "การนอนพังใน delirium และสารสื่อประสาทของ RAS",
    "Circadian inversion · two-process model · GABA กับ orexin · RAS สี่นิวเคลียส · melatonin ramelteon DORA dexmedetomidine · trazodone", 10,
    ACSSRC, ["B3.1.2(11)", "B3.1.3(2)", "B3.1.2(4)", "2.1.78", "2.1.79", "B3.4(4)"],
"""### Sleep–wake disturbance เป็นลักษณะหลักของ delirium (Levinsohn EA et al. J Clin Pharmacol 2025)
- **Circadian rhythm กลับขั้ว** — ง่วงกลางวัน ตื่นกลางคืน
- **การนอนแตกเป็นช่วง (fragmentation)**
- **REM และ slow-wave sleep ลดลง**
- การดูแลเน้น **(1) แก้ภาวะทางกายที่เป็นเหตุ** และ **(2) ฟื้นจังหวะกลางวัน–กลางคืนด้วยวิธีที่ไม่ใช้ยา**

### พยาธิสรีรวิทยาสามชั้นตาม handout
1. **Two-process model ถูกรบกวน** — การหลับเกิดเมื่อ **process C (circadian)** และ **process S (homeostatic sleep pressure)** สอดประสานกัน
2. **สมดุลสารสื่อประสาทเสีย** — **GABA ส่งเสริมการหลับ** · **orexin คงความตื่น**
3. **ARAS ทำงานผิดปกติ** — **ACh ขาด และ dopamine เกิน** (กลไกเดียวกับ delirium) · ✍️ melatonin

[[fig:acs2_twoprocess]]

### RAS — "สวิตช์ไฟหลัก" ของความตื่น
- ทอดยาวจาก **medulla ผ่าน pons ถึง midbrain** รับข้อมูลจากไขสันหลัง ทางรับความรู้สึก thalamus และ cortex แล้วส่งสัญญาณปลุก cortex ทั้งสองซีก
- **สี่นิวเคลียสหลัก** — locus coeruleus → **norepinephrine** · raphe nuclei → **serotonin** · tuberomammillary nucleus → **histamine** · pedunculopontine tegmentum → **acetylcholine**
- **ทุกกลุ่มถูกกระตุ้นด้วย orexin (hypocretin) จาก lateral hypothalamus** · **ขาด orexin = narcolepsy**
- **หน้าที่สี่ข้อ (Toy, Case Files Neuroscience)** — ปลุกและจดจ่อ · คงโทนของ cortex · **กรองข้อมูล** ว่าอะไรควรส่งขึ้นไป · คุมวงจรหลับตื่น (ตอนหลับสร้าง REM ตอนตื่นคงความตื่นตัว)

[[fig:acs2_ras]]

#### ทำไมถึงมีอาการนี้ — การนอนใน delirium
| อาการ | กลไก | ใช้อย่างไร |
|---|---|---|
| **ง่วงกลางวัน ตื่นกระวนกระวายกลางคืน** | ในหอผู้ป่วย/ICU แสงสว่างตลอด ไม่มีแสงแดด ถูกปลุกบ่อย → **SCN ไม่ได้สัญญาณตั้งเวลา melatonin กลางคืนลดและเลื่อน** → process C แบน | เปิดม่านกลางวัน มืดและเงียบกลางคืน รวมการวัดสัญญาณชีพ |
| **หลับเป็นช่วงสั้น ๆ ไม่ลึก** | ถูกปลุกก่อน process S สะสมพอ · ความเจ็บ ปัสสาวะคั่ง เสียงเตือน | eye mask และ earplug เพิ่มเวลานอน (handout) |
| **REM และ slow-wave sleep ลด** | benzodiazepine, opioid และ sedative กด slow-wave/REM · การอักเสบรบกวนการนอนลึก | ยานอนหลับบางชนิด "ทำให้หลับ" แต่ไม่ใช่การนอนที่ฟื้นฟูสมอง |
| **ง่วงหลังยาแก้แพ้รุ่นเก่า** | ปิดตัวรับ H1 ของ tuberomammillary + ฤทธิ์ anticholinergic → ทั้งง่วงและสับสน | เลี่ยงใช้เป็นยานอนหลับในผู้สูงอายุ |

### การดูแลการนอน
**ไม่ใช้ยา (ทำก่อนเสมอ)** — สร้างสิ่งแวดล้อมที่ช่วย **reorientation · ให้เคลื่อนไหว · สิ่งเร้าพอดีไม่มากเกิน · มีปฏิสัมพันธ์กับคน** · **eye mask และ earplug**

**ยาที่มีหลักฐานค่อนข้างดี (handout)**
| ยา | กลไก | เหตุผลที่เหมาะกับ delirium |
|---|---|---|
| **Melatonin** | ตัวรับ MT1/MT2 ที่ SCN → ตั้งนาฬิกาและส่งสัญญาณกลางคืน | ซ่อม process C โดยตรง ผลข้างเคียงน้อย |
| **Ramelteon** | agonist ของตัวรับ melatonin | เหมือนข้างบน ออกฤทธิ์แรงกว่า |
| **DORA — suvorexant, lemborexant** | **ต้านตัวรับ orexin** → ปิดสัญญาณตื่นแทนการกดสมองทั้งหมด | ไม่กด GABA ทั่วสมอง จึงไม่ทำให้สับสนแบบ BZD |
| **Dexmedetomidine** | alpha-2 agonist ที่ locus coeruleus → ลด NE คล้ายการนอนธรรมชาติ | ใช้ใน ICU · ปลุกได้ ไม่กดการหายใจ |

**ยาที่ใช้บ่อยในทางปฏิบัติแต่ต้องระวัง** — **trazodone** (✍️ **serotonin syndrome** เมื่อใช้ร่วมยา serotonergic) · **antipsychotics** (EPS, QT) · **benzodiazepines** (ทำให้ delirium แย่ลง ยกเว้นภาวะถอนสุรา/ยานอนหลับ)""",
    ["Delirium: circadian กลับขั้ว · นอนแตกเป็นช่วง · REM และ slow-wave ลด",
     "Two-process: S (แรงดันง่วง) × C (นาฬิกา) · GABA ส่งเสริมหลับ · orexin คงความตื่น",
     "RAS: LC-NE · raphe-5HT · TMN-histamine · PPT-ACh · orexin กระตุ้นทุกตัว",
     "ยานอนหลับใน delirium ที่มีหลักฐาน: melatonin · ramelteon · DORA · dexmedetomidine",
     "Eye mask + earplug + แสงกลางวัน = แก้ที่นาฬิกา ไม่ใช่กดสมอง"],
    [mcq("NEU-ACS-MCQ-41",
         "Suvorexant and lemborexant are used to treat insomnia, including sleep disturbance in delirium. Which mechanism explains how they promote sleep without the global CNS depression typical of benzodiazepines?",
         "They block orexin receptors, removing the hypothalamic drive that activates the arousal nuclei of the reticular activating system",
         ["They enhance GABA-A receptor chloride conductance throughout the cortex", "They block central histamine H1 receptors in the tuberomammillary nucleus",
          "They block muscarinic acetylcholine receptors in the pedunculopontine tegmentum", "They act as agonists at melatonin MT1/MT2 receptors in the suprachiasmatic nucleus"],
         1,
         "**ตอบ: ต้านตัวรับ orexin (DORA)** — handout: **orexin จาก lateral hypothalamus กระตุ้นทุกนิวเคลียสของ RAS** และ **ยา DORA (ต้าน orexin) ใช้เป็นยานอนหลับ** · ขาด orexin ถาวร = narcolepsy\n\n"
         "**ทำไมกดสมองน้อยกว่า** — DORA **ปิดสวิตช์ตื่นที่ต้นทาง** ให้กลไกการนอนตามธรรมชาติทำงาน ไม่ได้เพิ่มการยับยั้งทั่วทั้งสมองเหมือน BZD จึงคงสมาธิและการหายใจได้ดีกว่า\n\n"
         "**ทำไมข้ออื่นผิด** — **เสริม GABA-A** คือกลไกของ benzodiazepine และ Z-drug ซึ่งกดสมองทั่วไปและทำให้ delirium แย่ลง · **ต้าน H1** คือยาแก้แพ้รุ่นเก่า ง่วงแต่มีฤทธิ์ anticholinergic ทำให้สับสน · **ต้าน muscarinic** ทำให้เกิด delirium · **agonist ของ melatonin** คือกลไกของ melatonin และ ramelteon ไม่ใช่ DORA",
         "DORA = ต้าน orexin · melatonin/ramelteon = ตั้งนาฬิกา · BZD = กด GABA ทั้งสมอง",
         "Sleep in delirium — DORA", RA("Reticular activating system · Pharmacologic management of sleep-wake disturbances"),
         ["B3.1.2(11)", "B3.1.2(4)", "B3.4(4)"]),
     mcq("NEU-ACS-MCQ-42",
         "A 79-year-old man on day 4 of treatment for pneumonia has delirium that is worse at night; he sleeps most of the day. Lights and monitor alarms are on all night. After optimising the environment (daylight, eye mask, earplugs, clustered care), sleep remains poor. Which medication has the strongest support in the handout for delirium-related sleep disturbance?",
         "Melatonin or ramelteon in the evening",
         ["Lorazepam at bedtime", "Diphenhydramine at bedtime", "Zolpidem at bedtime", "Amitriptyline at bedtime"],
         4,
         "**ตอบ: melatonin หรือ ramelteon ตอนหัวค่ำ** — handout จัดไว้ในกลุ่มยาที่มีหลักฐานค่อนข้างดี (ร่วมกับ DORA และ dexmedetomidine)\n\n"
         "**กลไก** — ปัญหาของผู้ป่วยคือ **process C แบนและกลับขั้ว** จากแสงตลอดคืนและการอักเสบ · melatonin/ramelteon ไปที่ **SCN** ตั้งนาฬิกาใหม่และส่งสัญญาณกลางคืน แก้ที่ต้นเหตุโดยไม่กดสมอง\n\n"
         "**ทำไมข้ออื่นผิด** — ทุกตัวอยู่ใน **รายการยาที่เพิ่มความเสี่ยงหรือทำให้ delirium แย่ลง** ของ handout: **lorazepam** (benzodiazepine) · **zolpidem** (non-BZD hypnotic) · **diphenhydramine** (antihistamine + anticholinergic) · **amitriptyline** (TCA anticholinergic)",
         "Delirium นอนไม่หลับ: แก้สิ่งแวดล้อมก่อน → melatonin/ramelteon · เลี่ยง BZD Z-drug antihistamine TCA",
         "Sleep in delirium — pharmacological", RA("Pharmacologic management of sleep-wake disturbances in delirium"),
         ["B3.1.3(2)", "2.1.78", "B3.4(4)"]),
     ],
    ["acs2_twoprocess", "acs2_ras"]))

ACS.append(sec("neuro-acs-19", "ส่วนเติมจาก handout 2026: ระดับความรู้สึกตัว 5 ขั้น เบาะแสจากร่างกาย ตาแนวดิ่ง caloric และ algorithm",
    "Drowsiness → obtundation → coma · cherry-red · myxedema · asterixis · light reflex ทนเมแทบอลิก · sustained gaze · bobbing กับ dipping · caloric 50 mL · Cheyne-Stokes/Kussmaul · algorithm คอแข็ง", 12,
    ACSSRC, ["2.2.36", "2.1.78", "B3.1.1(5)", "2.2.35"],
"""### ระดับความรู้สึกตัวห้าขั้น (handout)
| ระดับ | ลักษณะ | ปลุกได้ด้วย |
|---|---|---|
| **Drowsiness (somnolence)** | อยากหลับ เผลอหลับถ้าไม่กระตุ้น · **ตื่นแล้วการรู้คิดปกติ** | สิ่งเร้าเล็กน้อย เช่น เรียกชื่อ แตะไหล่ |
| **Lethargy** | ง่วงมาก เฉื่อย ความตื่นตัวลดเล็กน้อย | เสียงพูดปกติหรือสะกิดเบา ๆ |
| **Obtundation** | ความตื่นตัวลดมากขึ้น สนใจสิ่งแวดล้อมน้อย ตอบสนองช้า | ต้องกระตุ้นซ้ำระดับปานกลาง เช่น เขย่าเบา ๆ ตะโกน |
| **Stupor** | แทบไม่โต้ตอบเอง พูดเป็นเสียงคราง | ต้องกระตุ้นแรง ซ้ำ หรือเจ็บ · **หยุดกระตุ้นแล้วกลับไม่ตอบสนองทันที** |
| **Coma** | ไม่ตอบสนองเลย | ปลุกไม่ได้แม้เจ็บลึก |

> **"It is best practice to write down the exact clinical observation."** — เขียนว่ากระตุ้นอย่างไรแล้วได้อะไร ดีกว่าเขียนคำว่า obtunded ลอย ๆ (ตรงกับหัวข้อ 2)

### ลำดับการเข้าหาผู้ป่วยระดับความรู้สึกตัวเปลี่ยน
1. **Airway · Breathing · Circulation**
2. **ประวัติจากญาติ** — สภาพเดิม อาการนำทั้งทางกายและระบบประสาท โรคประจำตัว **ยา สารเสพติด สุรา**
3. **ตรวจร่างกายทั่วไป แล้วตรวจระบบประสาทเจ็ดข้อ** — ระดับความรู้สึกตัว (GCS) · การเคลื่อนไหวผิดปกติและท่า · รูม่านตา · การกลอกตาที่เกิดเอง · การกลอกตาจากรีเฟล็กซ์ · จอประสาทตา · รูปแบบการหายใจ

### เบาะแสจากการตรวจร่างกายทั่วไป
| สิ่งที่เห็น | นึกถึง | กลไก |
|---|---|---|
| ริมฝีปากและเล็บเขียว | ออกซิเจนไม่พอ | deoxyhemoglobin > 5 g/dL ในเลือดฝอย |
| **ผิวสีแดงเชอร์รี** | **carbon monoxide** | carboxyhemoglobin สีแดงสด · ผิวแดงแม้เนื้อเยื่อขาดออกซิเจน (พบไม่บ่อย อย่ารอสีนี้) |
| เส้นเลือดฝอยขยายและหน้า/ตาแดง | สุราเรื้อรัง | vasodilation เรื้อรังจากแอลกอฮอล์ · ตับแข็ง |
| **หน้าบวมฉุ** | **myxedema** | glycosaminoglycan สะสมในชั้นหนังแท้ ดึงน้ำ |

### การเคลื่อนไหวและท่า
- **กระสับกระส่าย กระตุก multifocal myoclonus และ asterixis** → ✍️ **metabolic encephalopathy** (ไต ตับ CO₂ คั่ง ยา)
- **Decorticate** = รอยโรค **เหนือ red nucleus** (cerebral hemisphere, internal capsule, thalamus) · **Decerebrate** = **ใต้ red nucleus** (midbrain หรือ pons) — เหมือนหัวข้อ 8

### รูม่านตา — "light reflex ทนต่อภาวะเมแทบอลิกมาก"
| ลักษณะ | แปลผล |
|---|---|
| **เล็ก ตอบสนองต่อแสง** | รอยโรคที่ diencephalon · **ภาวะเมแทบอลิก** |
| **ขนาดกลาง ไม่ตอบสนอง** | รอยโรคที่ **midbrain** |
| **ใหญ่ ไม่ตอบสนอง** | รอยโรคก้านสมองกว้าง · **anoxia** · **anticholinergic poisoning หรือยาขยายม่านตา** |
| **เล็กเท่ารูเข็ม** | **pons** · **opiates** |
| **ข้างเดียว ขยาย ไม่ตอบสนอง** | **CN III palsy** ✍️ ร่วมกับ **ptosis** |
(OCR พบคำว่า sedative overdose อยู่ในตารางนี้ด้วยแต่ระบุแถวไม่ได้ — barbiturate ขนาดสูงมากทำให้รูม่านตาไม่ตอบสนองได้)

**ใช้อย่างไร** — ผู้ป่วยโคม่าที่ **รูม่านตายังตอบสนองดี** แต่ไม่มีรีเฟล็กซ์อื่น ให้คิดถึง **เมแทบอลิกหรือยา** ก่อนรอยโรคโครงสร้าง เพราะทางเดินของ light reflex (midbrain) ทนต่อภาวะเมแทบอลิกได้นานกว่าส่วนอื่น

### การกลอกตาที่เกิดเอง — เจ็ดแบบ
| แบบ | ลักษณะ | สาเหตุที่ handout ระบุ |
|---|---|---|
| **Conjugate deviation** | ตาเบนไปข้างเดียวกัน | ซีกสมอง/pons/ชัก (หัวข้อ 7) |
| **Skew deviation** | ตาสองข้างอยู่คนละระดับ | **posterior fossa** — ก้านสมองหรือสมองน้อย |
| **Sustained downward gaze** | ตาจ้องลงล่างค้าง | **ICP สูง/hydrocephalus จาก aqueduct ตีบหรือ shunt ตัน** · **Parinaud (dorsal midbrain)** จากก้อนหรือ stroke · **thalamus** เลือดออก/ขาดเลือด · **hepatic encephalopathy** |
| **Sustained upward gaze** | ตาจ้องขึ้นค้าง | **ชัก** · **HIE** · **oculogyric crisis** (ผู้ป่วยยังรู้ตัว — จากยาต้าน dopamine) |
| **Roving** | ช้า ไปมาแนวนอนสองข้างพร้อมกัน | ปกติใน NREM ระยะ 1 และ REM · **toxic-metabolic** (น้ำตาลต่ำ ตับ Wernicke opioid) · **แปลว่าก้านสมองยังดี** |
| **Ocular bobbing** | **กระตุกลงเร็ว แล้วกลับช้า** · **ไม่มีการกลอกตาแนวนอนทั้งที่เกิดเองและจากรีเฟล็กซ์** | **pons** ขาดเลือดหรือเลือดออก · HIE |
| **Ocular dipping** | **ลงช้า แล้วกลับเร็ว** | เปลือกสมองเสียทั่ว: **HIE · status epilepticus นาน · CJD · บาดเจ็บศีรษะรุนแรง** |

[[fig:acs2_bobbing]]

### Doll's eye ตาม handout — ห้าขั้น และรูปแบบที่บอกตำแหน่ง
1. **ตัดการบาดเจ็บกระดูกคอก่อน**
2. ถ่างหนังตาไว้
3. **หันศีรษะเร็ว ๆ ซ้าย–ขวา และค้างไว้สั้น ๆ ที่ปลายแต่ละข้าง**
4. **ผลบวก = ตาหมุนสวนทิศกับศีรษะ**
5. ก้มและเงยศีรษะ — **เงยแล้วตามองลง ก้มแล้วตามองขึ้น** = ปกติในแนวดิ่ง

| รูปแบบ (Plum & Posner) | ตำแหน่ง |
|---|---|
| ตาสวนทิศครบทุกทาง | **ก้านสมองดี** (เช่น metabolic encephalopathy) |
| มองไปข้างหนึ่งไม่ได้ทั้งสองตา | **pons ด้านข้าง (PPRF/นิวเคลียส VI)** — gaze paralysis |
| ตาข้างที่ต้องหุบเข้าไม่หุบ | **MLF** — internuclear ophthalmoplegia |
| ข้างหนึ่งไม่ไปเลย อีกข้างไปได้แค่ด้านนอก | **paramedian pons** — one-and-a-half syndrome |
| แนวดิ่งเสีย | **midbrain สองข้าง** |

### Caloric test ตาม handout
1. **ยกศีรษะ 30 องศา**
2. **ตรวจว่าเยื่อแก้วหูไม่ทะลุและช่องหูโล่ง**
3. **หยอดน้ำเย็น 50 mL (≤ 30 °C) ช้า ๆ ใน 30 วินาที**
4. **รอดู 1 นาทีหลังหยอด และเว้น 5 นาทีก่อนทำอีกข้าง** (ให้ระบบ vestibular กลับสู่สมดุล)
5. **หยอดสองหูพร้อมกัน** เพื่อประเมิน vestibulo-ocular reflex แนวดิ่ง (น้ำเย็นสองข้าง → ตาเบนลง)
> หัวข้อ 7 (สไลด์เดิม) ใช้น้ำเย็นจัด 10 มล. — ปริมาณต่างตามตำรา หลักการแปลผลเหมือนเดิม

### จอประสาทตาและการหายใจ
- **Papilledema** — ICP สูง · **subhyaloid hemorrhage** — เลือดออกหน้าจอตาขอบบนตรงเป็นแนวน้ำ พบใน **SAH** (ความดันในกะโหลกพุ่งจนเลือดดำในจอตาแตก — Terson syndrome)
- **รูปแบบหายใจจากเหตุนอกระบบประสาท** — **Cheyne-Stokes**: หัวใจล้มเหลว ขาดออกซิเจน CO (ระบบควบคุมการหายใจตอบสนองช้าเพราะเลือดไหลเวียนช้า → แกว่งเกินเป้า) · **Kussmaul**: **DKA ไตวาย sepsis methanol ethylene glycol** (metabolic acidosis → หายใจลึกเร็วเพื่อขับ CO₂)

### สาเหตุและ algorithm ปิดท้าย
**รอยโรคที่ทำให้ระดับความรู้สึกตัวเปลี่ยน** — รอยโรคซีกเดียวที่มี herniation · รอยโรคทั่วสมอง · รอยโรคสองซีก · รอยโรคที่ก้านสมอง (หัวข้อ 1)

| มี localizing sign? | ต่อไป | นึกถึง |
|---|---|---|
| **มี** | supratentorial หรือ infratentorial | **structural lesion** → CT/MRI |
| **ไม่มี + ไม่มีคอแข็ง** | | **toxic-metabolic encephalopathy** |
| **ไม่มี + คอแข็ง** | | **SAH หรือ meningitis** → CT แล้ว LP |""",
    ["ห้าระดับ: drowsiness → lethargy → obtundation → stupor → coma · เขียนสิ่งที่เห็นจริง",
     "Asterixis/multifocal myoclonus = metabolic · light reflex ทนเมแทบอลิก",
     "Bobbing: ลงเร็วกลับช้า = pons · Dipping: ลงช้ากลับเร็ว = HIE/เปลือกสมองทั่ว",
     "Sustained downward gaze: hydrocephalus/shunt · Parinaud · thalamus · hepatic",
     "Caloric (handout): น้ำเย็น 50 mL ≤ 30 °C ใน 30 วินาที รอ 1 นาที เว้น 5 นาที",
     "ไม่มี localizing + คอแข็ง → SAH หรือ meningitis"],
    [mcq("NEU-ACS-MCQ-43",
         "A 58-year-old man is comatose after a cardiac arrest. Every few seconds both eyes drift slowly downward and then return rapidly to the midline. Horizontal doll's eye responses are present. Which pattern is this and what does it most likely indicate?",
         "Ocular dipping, indicating diffuse cortical injury such as hypoxic–ischaemic encephalopathy",
         ["Ocular bobbing, indicating an acute pontine lesion", "Roving eye movements, indicating intact brainstem function in light sleep",
          "Sustained downward gaze, indicating dorsal midbrain compression", "Skew deviation, indicating a posterior fossa lesion"],
         0,
         "**ตอบ: ocular dipping** — **ลงช้าแล้วกลับเร็ว** และ **ยังมีการกลอกตาแนวนอนจากรีเฟล็กซ์** (ก้านสมองยังดี) หลังหัวใจหยุดเต้น = **diffuse cortical dysfunction จาก HIE** (handout: HIE · status epilepticus นาน · CJD · บาดเจ็บศีรษะรุนแรง)\n\n"
         "**กลไก** — เปลือกสมองที่เสียทั่วปล่อยให้วงจรแนวดิ่งในก้านสมองทำงานผิดจังหวะ ตาจึงไหลลงช้า ๆ แล้วระบบ saccade ของก้านสมองดึงกลับเร็ว\n\n"
         "**ทำไมข้ออื่นผิด** — **bobbing** ตรงกันข้าม: **กระตุกลงเร็วกลับช้า** และ **ไม่มีตาแนวนอน** เพราะ pons ที่คุมแนวนอนเสีย · **roving** เป็นการเคลื่อนช้า **แนวนอน** · **sustained downward gaze** ตาจ้องลงค้าง ไม่ขึ้นลงเป็นจังหวะ · **skew deviation** ตาสองข้างอยู่คนละระดับแบบคงที่",
         "Bobbing ลงเร็ว = pons · Dipping ลงช้า = HIE/เปลือกสมองทั่ว",
         "Coma — spontaneous vertical eye movements", RA("Spontaneous eye movement: ocular bobbing and dipping"),
         ["2.2.36", "B3.1.1(5)"]),
     mcq("NEU-ACS-MCQ-44",
         "When performing caloric testing (oculovestibular reflex) on a comatose patient, which procedure follows the handout?",
         "Elevate the head 30°, confirm intact tympanic membranes, instil 50 mL of cold water (≤ 30 °C) over 30 seconds, observe for 1 minute and wait 5 minutes before testing the other ear",
         ["Keep the head flat, instil 5 mL of warm water rapidly and test both ears within 1 minute",
          "Proceed even with a perforated tympanic membrane because the test is urgent",
          "Instil cold water into both ears simultaneously to assess horizontal gaze",
          "Rotate the head briskly first in every patient, even if a cervical spine injury has not been excluded"],
         2,
         "**ตอบ: ศีรษะ 30° · เยื่อแก้วหูปกติ · น้ำเย็น 50 mL ≤ 30 °C ใน 30 วินาที · ดู 1 นาที · เว้น 5 นาที** ตามขั้นตอนใน handout\n\n"
         "**เหตุผลของแต่ละขั้น** — **ศีรษะ 30°** ทำให้ **lateral semicircular canal อยู่แนวดิ่ง** การพาความร้อนของ endolymph จึงแรงที่สุด · **ตรวจเยื่อแก้วหู** เพราะน้ำเข้าหูชั้นกลางทำให้ติดเชื้อและผลเพี้ยน · **หยอดช้า** ให้ความเย็นส่งผ่านสม่ำเสมอ · **เว้น 5 นาที** ให้ระบบ vestibular ข้างแรกกลับสู่สมดุลก่อน ไม่ให้ผลสองข้างปนกัน\n\n"
         "**ทำไมข้ออื่นผิด** — **ศีรษะราบ น้ำอุ่นน้อยและเร็ว** กระตุ้นไม่พอ ผลลบลวงได้ · **เยื่อแก้วหูทะลุ** เป็นข้อห้าม · **หยอดสองหูพร้อมกัน** ใช้ประเมิน **แนวดิ่ง** ไม่ใช่แนวนอน · **doll's eye** ห้ามทำก่อนตัด C-spine injury (เป็นเหตุผลที่ต้องใช้ caloric แทน)\n\n"
         "**หมายเหตุ** — สไลด์ชุดเดิม (หัวข้อ 7) ใช้น้ำเย็นจัด 10 มล. ปริมาณต่างตามตำรา ในข้อสอบของคาบนี้ให้ตอบตาม handout",
         "Caloric: 30° · TM intact · cold 50 mL/30 s · ดู 1 นาที · เว้น 5 นาที · สองหูพร้อมกัน = แนวดิ่ง",
         "Coma — caloric test technique", RA("Reflex eye movements: Caloric test"), ["2.2.36", "B3.1.1(5)"]),
     mcq("NEU-ACS-MCQ-45",
         "A 45-year-old woman is brought in stuporous after a sudden severe headache. Pupils are equal and reactive, there is no hemiparesis and plantar responses are flexor, but she has marked neck stiffness. Fundoscopy shows a large haemorrhage in front of the retina with a flat upper border. Following the handout's algorithm, which group of causes should be considered first?",
         "Subarachnoid haemorrhage or meningitis",
         ["Supratentorial structural lesion with uncal herniation", "Infratentorial structural lesion compressing the brainstem",
          "Toxic–metabolic encephalopathy", "Psychogenic unresponsiveness"],
         3,
         "**ตอบ: SAH หรือ meningitis** — algorithm ปิดท้ายของ handout: **ไม่มี localizing sign + คอแข็ง → SAH หรือ meningitis** · ไม่มี localizing sign + ไม่มีคอแข็ง → toxic-metabolic · มี localizing sign → structural\n\n"
         "**เบาะแสเพิ่ม** — **ปวดศีรษะทันทีรุนแรง** + **subhyaloid hemorrhage** (handout แสดงภาพนี้ในหัวข้อ fundi) ชี้ไปที่ **SAH** อย่างมาก · กลไก: ความดันในกะโหลกพุ่งทันทีขณะหลอดเลือดโป่งแตก ส่งผ่านปลอกหุ้มเส้นประสาทตา → หลอดเลือดดำในจอตาคั่งและแตก เลือดอยู่หน้าจอตาจึงมีขอบบนเป็นแนวราบตามแรงโน้มถ่วง · คอแข็งเกิดจากเลือดระคายเยื่อหุ้มสมอง\n\n"
         "**ทำไมข้ออื่นผิด** — **supra/infratentorial structural lesion** ต้องมี localizing sign (รูม่านตาไม่เท่ากัน แขนขาอ่อนแรง สัญญาณก้านสมอง) · **toxic-metabolic** ไม่ทำให้คอแข็งหรือเลือดออกในจอตา · **psychogenic** ไม่มีคอแข็งหรือเลือดออกในจอตา · ขั้นต่อไปคือ **CT brain** ถ้าลบให้เจาะหลัง",
         "ซึม + ไม่มี localizing sign + คอแข็ง = SAH หรือ meningitis · subhyaloid hemorrhage ชี้ SAH",
         "Coma — diagnostic algorithm", RA("Pathologic causes of alteration of consciousness (algorithm)"),
         ["2.2.36", "2.3.6(3)", "2.3.6(5)"]),
     ],
    ["acs2_bobbing"]))

ACS_CALLOUTS = {
    "neuro-acs-02": "> **handout 2026 (อ.เพชรรัตน์) แบ่งเป็นห้าระดับ** — **drowsiness → lethargy → obtundation → stupor → coma** (เพิ่ม drowsiness และ obtundation จากสี่ระดับข้างบน) · หลักเดียวกันคือ **เขียนสิ่งที่เห็นจริง** · ดูหัวข้อ 19",
    "neuro-acs-07": "> **Caloric test ใน handout 2026 ใช้ปริมาณต่างจากข้างบน** — **น้ำเย็น 50 mL (≤ 30 °C) หยอดช้า ๆ ใน 30 วินาที รอดู 1 นาที และเว้น 5 นาทีก่อนทำอีกข้าง** · หยอดสองหูพร้อมกันเพื่อดูแนวดิ่ง · ocular bobbing ใน handout ระบุเพิ่มว่า **ไม่มีการกลอกตาแนวนอนทั้งที่เกิดเองและจากรีเฟล็กซ์** · ดูหัวข้อ 19",
    "neuro-acs-13": "> **handout 2026 เพิ่ม 3D-CAM** — สัมภาษณ์ที่มีโครงสร้าง 3 นาทีที่ใช้อัลกอริทึม CAM เดิม และนิยาม delirium ของ Alexander & Needham 2023 ที่รวม **visual hallucination** และ **ความสัมพันธ์กับตัวกระตุ้น** · ดูหัวข้อ 17",
    "neuro-acs-15": "> **handout 2026 (Marcantonio NEJM 2017)** — ถ้าจำเป็นต้องใช้ยา ให้ **high-potency antipsychotic ขนาดต่ำ (haloperidol)** ระวัง **EPS และ QT ยาว (torsades)** · **low-potency typical เช่น chlorpromazine และ thioridazine อยู่ในรายการยาที่ทำให้ delirium แย่ลง** · การดูแลสี่ขั้นและ DELIRIUM อยู่ในหัวข้อ 17",
}
ACS_GUIDE = [
    "**Handout 2026 อ.เพชรรัตน์ (Petcharat Dusitanond) — Acute confusional state and Alteration of consciousness** (หัวข้อ 16–19) รวมภาพหน้าจอ Delirium Quiz ในคาบ 21 ต.ค. 2569",
    "**Marcantonio ER. Delirium in Hospitalized Older Adults. N Engl J Med 2017;377:1456-66** — CAM/3D-CAM · การดูแลสี่ขั้น · DELIRIUM · ยาที่ก่อ delirium",
    "**Alexander SK, Needham E. Diagnosis of delirium: a practical approach. Pract Neurol 2023;23:192-199**",
    "**Levinsohn EA et al. J Clin Pharmacol 2025;65:285-302** — sleep–wake disturbance ใน delirium และยา (melatonin, ramelteon, DORA, dexmedetomidine)",
    "**Teng C, Frei CR. Drugs Real World Outcomes 2021;9:23-29** — ยาปฏิชีวนะที่สัมพันธ์กับ delirium",
    "**Allen C et al. Neurohospitalist 2025;15:402-406** — spontaneous abnormal vertical eye movements of coma",
]


# ═════════════════════════════════════════════════════════════════════ apply
def add_callout(s, text):
    marker = text.split("—")[0].strip()
    md = s["md"]
    if text in md:
        return False
    if marker in md:  # ฉบับเก่าของ callout เดิม → แทนที่บล็อกนั้น
        i = md.index(marker)
        j = md.find("\n\n", i)
        md = md[:i] + text + ("" if j < 0 else md[j:])
        s["md"] = md
        return True
    s["md"] = md.rstrip() + "\n\n" + text
    return True


def apply(data, lec, new_secs, callouts, guides):
    L = next(x for x in data if x["lec"] == lec)
    ids = {s["id"] for s in new_secs}
    old = [s for s in L["sections"] if s["id"] not in ids]
    keep_new = {s["id"]: s for s in L["sections"] if s["id"] in ids}
    for s in new_secs:
        assert "anims" not in s and "mnem" not in s
        if s["id"] in keep_new:   # คงฟิลด์ที่เครื่องมืออื่นอาจเติมให้หัวข้อใหม่ภายหลัง
            for k in ("anims", "mnem"):
                if k in keep_new[s["id"]]:
                    s[k] = keep_new[s["id"]][k]
    L["sections"] = old + new_secs
    n = 0
    for s in L["sections"]:
        if s["id"] in callouts:
            n += add_callout(s, callouts[s["id"]])
    g = L.setdefault("guidelines", [])
    for x in guides:
        if x not in g:
            g.append(x)
    return n


def main():
    data = json.load(open(PATH, encoding="utf-8"))
    before = json.dumps(data, ensure_ascii=False)
    n1 = apply(data, "9/10", LP, LP_CALLOUTS, LP_GUIDE)
    n2 = apply(data, "21/10", ACS, ACS_CALLOUTS, ACS_GUIDE)
    # ตรวจ id ซ้ำทั้งไฟล์ + code fence
    seen = set()
    for L in data:
        for s in L["sections"]:
            assert s["id"] not in seen, s["id"]; seen.add(s["id"])
            assert "```" not in s["md"], s["id"]
            for it in s["items"]:
                assert it["id"] not in seen, it["id"]; seen.add(it["id"])
    out = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    changed = json.dumps(data, ensure_ascii=False) != before
    print("LP: %d หัวข้อใหม่ %d ข้อใหม่ · callout เปลี่ยน %d" % (len(LP), sum(len(s["items"]) for s in LP), n1))
    print("ACS: %d หัวข้อใหม่ %d ข้อใหม่ · callout เปลี่ยน %d" % (len(ACS), sum(len(s["items"]) for s in ACS), n2))
    if "--check" in sys.argv:
        print("--check: ไม่เขียนไฟล์ ·", "จะมีการเปลี่ยนแปลง" if changed else "ไม่มีอะไรเปลี่ยน")
        return
    if changed:
        open(PATH, "w", encoding="utf-8").write(out)
        print("เขียน", PATH)
    else:
        print("ไม่มีอะไรเปลี่ยน")


if __name__ == "__main__":
    main()
