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
ACS, ACS_CALLOUTS, ACS_GUIDE = [], {}, []  # @@STUB@@
#@@ACS@@


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
