#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""อัปเดตคาบ gi 29/10 "Liver function tests" (อ.กิตติ ชื่นยง) ตามสไลด์ใหม่ปี 2570 — ไม่รัน build_lft.py ซ้ำ

    python3 artifact/tools/update_lft2570.py            # เขียน data/gi.json
    python3 artifact/tools/update_lft2570.py --check    # ตรวจโดยไม่เขียน

แหล่ง: "LFT 2570.pdf" (30 หน้า) · โน้ต slides/lft2570_notes.md · คาบเดิมสร้างจากสไลด์ 2563 ด้วย build_lft.py
- หัวข้อใหม่ gi-lft-09..13 (แทรกต่อจากหัวข้อที่เกี่ยวข้อง) · ข้อใหม่ GI-LFT7-MCQ-01..17 (prefix ใหม่ —
  GI-LFT-MCQ-NN ถูกใช้แล้วในชุด G06 ของ Ward Drill)
- callout "> **2570 · …**" ในหัวข้อเดิม (สิ่งที่สไลด์ใหม่เพิ่ม/ต่าง + ลายมือ ✍️) · ภาพเคลื่อนไหว/หลักจำจาก anims_gi_lft2570.py
- ไม่แตะ id/choices/answer ของข้อเดิม · คง anims/mnem/figs/imgs เดิมทุกชิ้น · ไม่แตะคาบอื่น

รันซ้ำได้: หัวข้อใหม่ถูกแทนที่ทั้งก้อน · callout และ marker [[anim:lft7-*]] ของสคริปต์นี้ถูกถอดออกก่อนแล้วใส่ใหม่ ·
ข้อ/หลักจำ/guidelines/objectives ของสคริปต์นี้แทนที่ด้วย id/ชื่อ ไม่เพิ่มซ้ำ"""
import json, os, re, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(TOOLS)), "dashboard"))
import anims_gi_lft2570 as AN  # noqa: E402
from patch_learn_anim import _insert_marker  # noqa: E402

ART = os.path.dirname(TOOLS)
PATH = os.path.join(ART, "data", "gi.json")
LEC = "29/10"
SRC = "สไลด์ อ.กิตติ ชื่นยง ปี 2570 — LFT 2570.pdf (Clinical Approach & Pattern Recognition)"
SRC_TAG = " · สไลด์ 2570"
REF = lambda p: ["สไลด์ นพ.กิตติ 2570 — " + p]
NL0 = ["B8.3(1)", "2.1.13"]


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


def sec(sid, title, summary, minutes, nl, md, pearls, items):
    return {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": SRC,
            "nl": nl, "md": md.strip(), "pearls": pearls, "items": items}


# ═════════════════════════════════════════════════════════════════ ข้อใหม่ที่เพิ่มในหัวข้อเดิม
OLD_ITEMS = {
    "gi-lft-01": [mcq_fixed(
        "GI-LFT7-MCQ-01",
        "A 55-year-old obese man has ALT 128 U/L (ULN 40) and ALP 68 U/L (ULN 120) at a routine check-up. What is the R ratio and the pattern of injury?",
        ["R ≈ 0.6, cholestatic", "R ≈ 1.9, cholestatic", "R ≈ 3.2, mixed", "R ≈ 5.6, hepatocellular", "R ≈ 9.0, hepatocellular"], 3,
        "**R = (ALT ÷ ULN) ÷ (ALP ÷ ULN) = (128 ÷ 40) ÷ (68 ÷ 120) = 3.2 ÷ 0.57 ≈ 5.6** → **> 5 = hepatocellular**\n\n"
        "- 1.9 = เอา ALT หาร ALP ตรง ๆ โดยไม่หาร ULN · 3.2 = หารแค่ ALT ลืมหาร ALP\n"
        "- R บอก **ชนิด** ไม่ได้บอก **ความรุนแรง** — เคสนี้ค่าสูงแค่ระดับ mild (3 เท่า) แต่เป็น hepatocellular · เคสในสไลด์ 2570 คือ **MASLD**",
        "R = (ALT/ULN) ÷ (ALP/ULN) · ต้องหาร ULN ทั้งคู่", "R ratio", REF("R ratio · เคสชาย 55 ปี"), NL0)],
    "gi-lft-02": [mcq(
        "GI-LFT7-MCQ-02",
        "A 48-year-old woman with dermatomyositis has severe proximal weakness. CK is 12,000 U/L, AST 310 U/L and ALT 160 U/L; ALP, GGT and bilirubin are normal. What is the most likely source of the raised aminotransferases?",
        "Skeletal muscle injury",
        ["Autoimmune hepatitis", "Ischaemic hepatitis", "Alcohol-associated liver disease", "Acute hepatitis E"], 2,
        "สไลด์ 2570: AST มีใน **กล้ามเนื้อลาย หัวใจ ไต สมอง ตับอ่อน เม็ดเลือด** · ALT จำเพาะต่อตับกว่า แต่สไลด์เขียนว่า **severe muscle disease ทำให้ ALT สูงได้** — กล้ามเนื้อสลายมาก ALT ก็รั่วออกมาด้วย\n\n"
        "**AST > ALT + CK สูงมาก + GGT ALP bilirubin ปกติ** → มาจากกล้ามเนื้อ ไม่ต้องไล่โรคตับ · ขาดเลือดต้องมีประวัติช็อกและค่าเป็นพัน · เหล้ามี GGT สูง · ไวรัส ALT > AST",
        "AST > ALT + CK สูง + GGT ปกติ = กล้ามเนื้อ", "Extrahepatic aminotransferase", REF("Hepatocellular injury pattern"), NL0)],
    "gi-lft-05": [mcq(
        "GI-LFT7-MCQ-10",
        "A 57-year-old man has fever 39 °C, jaundice and right upper quadrant pain for 2 days. TB 5 mg/dL, DB 3 mg/dL, AST 55 U/L, ALT 60 U/L, ALP 380 U/L. Ultrasound shows a dilated common bile duct. Besides intravenous antibiotics, what is the most appropriate next step?",
        "Biliary drainage by ERCP",
        ["Liver biopsy", "Antimitochondrial antibody", "Repeat LFT in 2 weeks", "Oral ursodeoxycholic acid"], 0,
        "สไลด์ 2570 เฉลยเคสนี้: **ไข้ + เหลือง + ปวดชายโครงขวา = Charcot's triad** · cholestatic (DB เด่น ALP > 3 เท่า · **R = 1.5 ÷ 3.2 ≈ 0.5 < 2**) → **obstructive jaundice / acute ascending cholangitis**\n\n"
        "Master algorithm: cholestasis → US → **CBD ขยาย** → ประเมิน S&S ของ cholangitis → **ERCP** (หรือ CT) · ascending cholangitis ต้อง **ระบายท่อ** ร่วมกับยาปฏิชีวนะ\n\n"
        "biopsy และ AMA ใช้เมื่อท่อ **ไม่ขยาย** (medical cholestasis) · UDCA ใช้ใน PBC",
        "Charcot's triad + CBD ขยาย → ยาปฏิชีวนะ + ERCP", "Ascending cholangitis", REF("เคสชาย 57 ปี · Master Diagnostic Algorithm"),
        NL0 + ["2.3.11-3(3)", "B8.2.2-3(6)"])],
    "gi-lft-06": [mcq(
        "GI-LFT7-MCQ-11",
        "Four days after successful ERCP clearance of a common bile duct stone, a patient is well and afebrile. Bilirubin has fallen from 6 to 2.5 mg/dL, but ALP is still 420 U/L (520 U/L before ERCP). What is the best interpretation?",
        "An expected slow fall — ALP has a half-life of about 5–7 days",
        ["A retained stone; repeat ERCP now", "New bone disease", "Drug-induced cholestasis from the antibiotic",
         "Primary biliary cholangitis unmasked by the obstruction"], 3,
        "สไลด์ 2570 เพิ่มว่า **ALP ครึ่งชีวิต 5–7 วัน — ยังสูงอยู่หลายวันหลังแก้การอุดตัน** · ALP ลดจาก 520 เหลือ 420 ใน 4 วันจึงเป็นไปตามคาด และผู้ป่วยดีขึ้น bilirubin ลดลง\n\n"
        "นิ่วค้างจะมีไข้/ปวด bilirubin ไม่ลด · โรคกระดูกไม่เกิดขึ้นใน 4 วัน · ยาเป็นไปได้น้อยเมื่อค่ากำลังลง\n\n"
        "bilirubin ที่ยังค้างบางส่วนมาจาก **delta bilirubin** (จับ albumin ครึ่งชีวิต ~20 วัน)",
        "ALP t½ 5–7 วัน → ลงช้าหลังแก้อุดตัน", "ALP kinetics", REF("การแยกแหล่งที่มาของเอนไซม์ระบบน้ำดี"), NL0)],
    "gi-lft-07": [mcq(
        "GI-LFT7-MCQ-12",
        "A 60-year-old man with known cirrhosis develops septic shock with bleeding from line sites. INR is 2.4 and platelets 60,000/µL. Which result most strongly favours DIC rather than hepatic synthetic failure alone?",
        "Low factor VIII level",
        ["Low factor VII level", "Prolonged PT that does not correct with vitamin K", "Low serum albumin", "Low factor V level"], 4,
        "✍️ อาจารย์เขียนใต้สไลด์ synthetic function: **\"DIC ↓ ทั้งหมด / VIII ยังอยู่ → Liver\"** · ตับสร้าง factor ทุกตัว **ยกเว้น VIII** (สร้างที่ endothelial cell) → ตับวาย **VIII ปกติหรือสูง** · DIC ใช้ factor หมดทุกตัว **รวม VIII**\n\n"
        "VII และ V ต่ำได้ทั้งสองภาวะ · PT ไม่ตอบสนองวิตามิน K บอกว่าตับสร้างไม่ได้ (ไม่แยก DIC) · albumin ต่ำบอกความเรื้อรัง",
        "VIII ต่ำ = DIC · VIII ปกติ/สูง = ตับ", "DIC vs liver disease", REF("Liver Synthetic Function · ลายมือ"),
        NL0 + ["2.3.3(1)", "B2.2.5(2)"])],
    "gi-lft-08": [mcq(
        "GI-LFT7-MCQ-17",
        "A 74-year-old woman admitted with pneumonia becomes jaundiced: TB 5 mg/dL, DB 3 mg/dL, ALP 540 U/L, AST and ALT normal. She has no abdominal pain. Ultrasound shows no biliary dilatation. What is the most appropriate approach?",
        "Treat the infection, review hepatotoxic drugs and follow the LFT; markers or biopsy only if it persists",
        ["ERCP to look for an occult common bile duct stone", "Start intravenous N-acetylcysteine",
         "Refer for liver transplant assessment", "Start prednisolone for presumed autoimmune hepatitis"], 4,
        "Master algorithm 2570: cholestasis → US → **ไม่พบ dilated CBD = medical (micro-duct) cholestasis** (2B) → serum markers/ประวัติยา → biopsy ถ้ายังไม่ทราบ\n\n"
        "สไลด์เฉลยเคสนี้ว่า **sepsis-induced cholestasis** — การติดเชื้อลดการขับน้ำดีของเซลล์ตับโดยไม่มีอะไรอุด → ดีขึ้นเมื่อคุมการติดเชื้อได้ · ทบทวนยาปฏิชีวนะ (เช่น amoxicillin–clavulanate) ร่วมด้วย\n\n"
        "ERCP ใช้เมื่อท่อขยายหรือมี cholangitis · NAC ใช้ใน paracetamol · ไม่มีข้อบ่งชี้ของ AIH",
        "Cholestasis + US ปกติ ระหว่าง sepsis → รักษาการติดเชื้อ ทบทวนยา", "Medical cholestasis",
        REF("เคสหญิง 74 ปี · Master Diagnostic Algorithm"), NL0)],
}

# ═════════════════════════════════════════════════════════════════ callout ในหัวข้อเดิม
# (หัวข้อ, ข้อความ) — บรรทัดแรกขึ้นต้น "> **2570 · ชื่อ**" ใช้เป็นตัวระบุตอนถอดออกเมื่อรันซ้ำ
CALLOUTS = {
    "gi-lft-01": [("5 รูปแบบ (สไลด์)", """
> **2570 · 3 เสาหลัก** — สไลด์ใหม่จัดเป็น **The 3 Pillars of LFTs**: **Hepatocyte integrity** (AST ALT → hepatocellular necrosis/hepatitis) · **Biliary function & cholestasis** (ALP GGT **bilirubin** 5′NT → biliary obstruction, infiltrative, medical cholestasis) · **Synthetic function** (albumin PT → "true liver function" และ **ความเรื้อรังของโรค**)
> ต่างจากเดิม: bilirubin ถูกรวมไว้ในเสาท่อน้ำดี · รูปแบบที่ 5 เรียกว่า **isolated hyperbilirubinemia** (เดิม "jaundice") · ✍️ ไฮไลต์ **albumin และ PT** และขีดเส้นใต้ทั้ง "hepatitis" และ "cholestasis" ใน mixed pattern
""")],
    "gi-lft-02": [("อัตราส่วน AST/ALT (สไลด์)", """
> **2570 · AST/ALT** — สไลด์ใหม่เพิ่มแหล่งของ AST: **สมอง ตับอ่อน เม็ดเลือด** (นอกจากหัวใจ กล้ามเนื้อลาย ไต) และเขียนว่า **ALT ก็สูงได้ใน severe muscle disease** — ALT สูงจึงไม่ได้แปลว่าเป็นโรคตับเสมอ
> ✍️ ที่ AST/ALT > 2: **"Inj. to mitochondria"** (AST ของตับ 80% อยู่ใน mitochondria) · ✍️ ใต้กล่อง: **ไม่มีตับแข็ง + AST/ALT > 2 → Wilson disease หรือ alcohol**
> ✍️ ตัวเลขช่วงตาม ULN 40: mild **≤ ~200** · moderate **200–1,600** · marked **> 1,600** · ✍️ NASH = "non-alcoholic" · ischemic hepatitis = "shock liver"
""")],
    "gi-lft-03": [("เคสในสไลด์ — ชาย 29 ปี", """
> **2570 · เคส HAV** — สไลด์ใหม่ใช้ตัวเลข **AST 1,000 · ALT 1,300** (สไลด์ 2563: 1,350/1,525) · TB 15 · PT 14 เท่าเดิม → จัดเป็น **moderate (5–40 เท่า)** · AST/ALT < 1 → **acute viral hepatitis A → ส่ง IgM anti-HAV** (กราฟ ALT IgM IgG anti-HAV ในสไลด์)
> ✍️ ที่ TB 15: **"TB > 4.5 → prefer direct"** — bilirubin สูงขนาดนี้ไม่ใช่ hemolysis อย่างเดียว (hemolysis ล้วนแทบไม่เกิน ~4–5 มก./ดล.) ต้องเป็น direct เด่นจากเซลล์ตับเสีย *(ตีความลายมือ)*
"""), ("ขั้นตอนหาสาเหตุ acute hepatitis (สไลด์)", """
> **2570 · algorithm** — ขั้นตอนเหมือนเดิม · ✍️ ที่ "alcohol": **"80 g/day (> 10 ปี) → cirrhosis"** · ✍️ ที่ HBsAg: **"Chronic > acute (พบมากกว่า)"** · สไลด์ใหม่มี **anti-HEV IgM** และกราฟผลเลือดไวรัสครบ → หัวข้อ "ผลเลือดไวรัสตับอักเสบ" ท้ายคาบ
"""), ("Paracetamol (acetaminophen) — เคสในสไลด์", """
> **2570 · paracetamol** — สไลด์ใหม่จัดเคสนี้เป็น **"Extreme elevation (50–100×)"** · severe hepatocellular necrosis "คล้ายเคส ischemic แต่บริบทต่างกัน" → **acetaminophen toxicity (DILI)** · ✍️ **"DDx 3 โรค: Para + Ischemic + Rhabdomyolysis"** · ✍️ ที่สไลด์ระดับความรุนแรง paracetamol = **"only this"** · เทียบเคสช็อกใหม่ในหัวข้อ "transaminase หลายพัน"
""")],
    "gi-lft-04": [("Wilson disease (สไลด์)", """
> **2570 · AIH/Wilson** — ✍️ Wilson **"AR"** · ✍️ extrapyramidal = **"tract ที่ไม่ใช่ corticospinal เช่น parkinsonism"** · ✍️ **"hemato → Coombs negative"** · ✍️ AIH: celiac → **"gluten"**
> สไลด์ใหม่เขียน simplified criteria เป็น "> 6 probable, > 7 definite" แต่เกณฑ์ IAIHG 2008 คือ **≥ 6 / ≥ 7** (คาบนี้ใช้ ≥) · ไม่ได้ให้ % ของโรคร่วม
> สไลด์ใหม่มีเคส **Wilsonian acute liver failure** เต็มรูปแบบ (ceruloplasmin 6.5 mg/dL · urine Cu 680 µg/วัน โดยค่าปกติ **< 40**) → หัวข้อ "Acute liver failure จาก Wilson" · เคส AIH ใหม่ (globulin 6) → หัวข้อ "MASLD และ AIH"
""")],
    "gi-lft-05": [("นิยาม (สไลด์)", """
> **2570 · micro vs macro** — สไลด์ใหม่เรียก **medical cholestasis = micro-duct level** (ยา sepsis PBC PSC AIDS cholangiopathy — ✍️ วงทุกตัว) และ **obstructive = macro-duct level** (ท่อใหญ่ที่อัลตราซาวนด์เห็นขยาย) · clinical clues เหลือ 3 ข้อ: **ปวดท้องขวาบน + ไข้ · อุจจาระซีด · Courvoisier** (ไม่มี "คัน")
"""), ("เคสในสไลด์", """
> **2570 · เฉลยเคส** — สไลด์ใหม่เฉลยเคสชาย 57 ปีว่า **ไข้ + เหลือง + ปวดชายโครงขวา = Charcot's triad** (✍️ "acute") · **R < 2** → **obstructive jaundice / acute ascending cholangitis** → **US/ERCP ฉุกเฉิน** หาตำแหน่งอุดตัน · เคสหญิง 74 ปีเฉลยว่า **sepsis-induced cholestasis** (US ปกติ ตัด obstructive ออก)
""")],
    "gi-lft-06": [("Alkaline phosphatase (สไลด์)", """
> **2570 · ALP** — สไลด์ใหม่เพิ่ม **ALP half-life 5–7 วัน** → ยังสูงอยู่หลายวันหลังแก้การอุดตัน · แหล่ง ALP: กระดูก ตับ รก ลำไส้ **ไต** · ✍️ ระบายส่วนที่ ALP ซ้อนกับ GGT ว่า **"Liver"** · กลไกของ isolated ALP = **อุดตันท่อน้ำดีขนาดเล็กหรือบางส่วน** (✍️ "จำ DDx")
"""), ("GGT (สไลด์)", """
> **2570 · GGT** — สไลด์ใหม่เพิ่มว่า **1/3 ของผู้ป่วยพิษสุราเรื้อรัง GGT อาจไม่สูง** · กลไกของ isolated GGT = **การกระตุ้นเอนไซม์โดยสารเคมีหรือยา** · **NOT found in bone disease**
""")],
    "gi-lft-07": [("Prothrombin time (สไลด์)", """
> **2570 · synthetic** — สไลด์ใหม่เรียก **albumin = ตัวชี้วัดระยะยาว** (t½ ~20 วัน · ลดในโรคตับเรื้อรัง/ตับแข็ง มักคู่กับ globulin สูง) และ **PT = ตัวชี้วัดกระบวนการสร้าง** · ทดสอบด้วยการ **ฉีดวิตามิน K ใต้ผิวหนัง** · ✍️ **"DIC ↓ ทั้งหมด / VIII ยังอยู่ → Liver"** · สไลด์ใหม่ไม่ได้กล่าวถึง factor V (คงไว้จากสไลด์ 2563)
"""), ("Bilirubin เด่น (สไลด์)", """
> **2570 · bilirubin** — สไลด์ใหม่แบ่งเป็น **Path A (IB/TB > 0.8) ความผิดปกติก่อนเข้าตับ** และ **Path B (DB/TB > 0.5) ที่ตับหรือหลังตับ** และเพิ่มสาเหตุ direct: **liver congestion · alcoholic hepatitis · end-stage cirrhosis · DILI** → หัวข้อ "Direct bilirubin สูง"
""")],
    "gi-lft-08": [("Mixed pattern (สไลด์)", """
> **2570 · mixed** — สไลด์ใหม่เหลือ 4 สาเหตุ: **DILI** (✍️ วงข้อ ① "Drug") · **overlap syndrome (AIH + immune cholangiopathy)** · **acute passing stone** · **LFT of SIRS** — infiltrative และตับคั่งเลือดถูกย้ายออก (ตับคั่งเลือดไปอยู่ในสาเหตุของ direct bilirubin) · ✍️ ที่ R 2–5: "only cause เดียว แต่ … คู่" (?) = สาเหตุเดียวที่ให้ทั้ง hepatitis และ cholestasis *(ตีความลายมือ)*
"""), ("ขั้นตอนดูแลผู้ป่วยเหลือง (สไลด์)", """
> **2570 · Master algorithm** — LFT pattern → Hx + PE → **Hepatitis**: serum markers → biopsy · **Cholestasis** → US → **2A CBD ขยาย** → ประเมิน S&S ของ cholangitis → **ERCP หรือ CT** · **2B ไม่ขยาย** → serum markers/ประวัติยา → biopsy · **Mixed** → DILI overlap passing stone SIRS
> ต่างจากเดิม: สไลด์ใหม่ไม่ได้แยก "มี cholangitis → ERCP · ไม่มี → CT/MRCP" ไว้ชัด (เขียนรวม "ERCP หรือ CT") · ตารางรูปแบบตามโรคและเรื่องไข้ร่วมกับเหลืองไม่อยู่ในสไลด์ 2570 (คงไว้จากสไลด์ 2563)
""")],
}

# แก้ข้อความเดิมที่อ้างเลขหัวข้อ (เลขเปลี่ยนเมื่อแทรกหัวข้อใหม่)
TEXT_FIX = {
    "gi-lft-08": [("3. Hepatitis → serology ไวรัส ประวัติยาเหล้า (หัวข้อ 3–4)",
                   "3. Hepatitis → serology ไวรัส ประวัติยาเหล้า (หัวข้อ \"Transaminase สูงมาก\" และ \"สูงเล็กน้อยเรื้อรัง\")")],
}

# ═════════════════════════════════════════════════════════════════ หัวข้อใหม่
NEW = {}

NEW["gi-lft-09"] = sec(
    "gi-lft-09", "สไลด์ 2570: transaminase หลายพัน — shock liver vs paracetamol vs rhabdomyolysis",
    "เคสใหม่หญิง 65 ปี ปอดอักเสบ BP 80/40 → AST 3,900 · ✍️ ULN 40: 200 / 1,600 · zone 3 ไวต่อช็อก paracetamol เหล้า halothane · ✍️ DDx 3 โรค",
    9, NL0 + ["2.3.11-3(7)", "2.2.7", "B7.2.5(4)"],
    """
หัวข้อนี้และหัวข้อที่มีคำว่า **"สไลด์ 2570"** มาจาก **สไลด์ใหม่ของ อ.กิตติ ปี 2570** (บรรยาย 29 ต.ค. 2569) · เขียนเฉพาะเนื้อหาที่ **ใหม่หรือต่างจากสไลด์ 2563** · ✍️ = ลายมือ/ไฮไลต์ในห้อง

### ระดับ transaminase เป็นตัวเลข (✍️ ULN 40)
| ระดับ | เท่าของ ULN | ✍️ เป็นตัวเลข | กลุ่มสาเหตุในสไลด์ |
|---|---|---|---|
| **Mild** | 2–5 เท่า | ถึง ~**200** | เหล้า · NASH (✍️ "non-alcoholic") · infiltrative |
| **Moderate** | 5–40 เท่า | **200–1,600** | ไวรัส · AIH · ยา · Wilson · hemochromatosis |
| **Marked** | 40–100 เท่า | **> 1,600** | **ตับขาดเลือด** (✍️ "shock liver") · **paracetamol** (✍️ "only this") |

### เคสใหม่ — หญิง 65 ปี DM ปอดอักเสบ ความดันตก
**BP 80/40** · TB 0.7 DB 0.3 · Alb 4.2 Glob 3.2 · **AST 3,900 ALT 3,500** · AP 140
- รูปแบบ: **massive hepatocellular necrosis จากการขาดเลือด** — ระดับ extreme แต่ **bilirubin และ albumin ยังปกติ**
- จุดเปลี่ยน: เอนไซม์พุ่งเป็นพัน **หลังความดันตก (shock)** + **ALT/LDH < 1.5**
- วินิจฉัย: **ischemic hepatitis (shock liver)**
- จัดการ (สไลด์): **แก้ภาวะ shock ต้นเหตุ** — ตัวเลขเอนไซม์ลดลงอย่างรวดเร็วเมื่อการไหลเวียนเลือดกลับมาเป็นปกติ

### เคสเดิมในสไลด์ใหม่ — หญิง 23 ปี ยาแก้ปวด 1 กำมือ
TB 8 DB 5 · **AST 3,580 ALT 2,500** · AP 230 → สไลด์ 2570 เรียก **"Extreme elevation (50–100×)"** และเขียนว่า **คล้ายเคส ischemic liver แต่บริบทต่างกัน** → **acetaminophen toxicity (DILI)** · การรักษาอยู่ในหัวข้อ "Transaminase สูงมาก"
✍️ ใต้สไลด์: **"DDx 3 โรค: Para + Ischemic + Rhabdomyolysis"**

| | **Ischemic (shock liver)** | **Paracetamol** | **Rhabdomyolysis** |
|---|---|---|---|
| บริบท | ช็อก หัวใจล้มเหลว ขาด O₂ | กินยาเกินขนาด | ชัก ออกกำลังหนัก ถูกกดทับ statin |
| AST/ALT | หลายพัน ALT ≈ AST | หลายพัน AST อาจ > ALT | **AST >> ALT** |
| ตัวช่วยแยก | **LDH สูงมาก ALT/LDH < 1.5** | ระดับยา ประวัติ INR ยาวเร็ว | **CK สูงมาก** ปัสสาวะสีโค้ก |
| Bilirubin/INR | ปกติช่วงแรก | INR ยาว bilirubin ขึ้น | **ปกติ** (ไม่ใช่ตับ) |
| รักษา | แก้ shock | **NAC ทันที** | สารน้ำมาก ๆ ป้องกันไตวาย |

#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Transaminase หลายพันใน 1–3 วัน** | เซลล์ zone 3 (รอบ central vein ที่ได้ O₂ น้อยสุด) ตายพร้อมกันครั้งเดียว ปล่อยเอนไซม์ทั้งหมด | ไวรัสขึ้นช้ากว่าและค้างหลายสัปดาห์ |
| **ลดลงเร็วหลังแก้ช็อก** | ไม่มีการทำลายต่อเนื่อง ค่าลดตามครึ่งชีวิตของเอนไซม์ | ไม่ลด → คิดสาเหตุร่วม (paracetamol ไวรัส) |
| **LDH สูงมาก · ALT/LDH < 1.5** | เนื้อเยื่อทั้งร่างกายที่ขาด O₂ ปล่อย LDH | ไวรัส/paracetamol มักมากกว่า 1.5 |
| **Bilirubin ปกติในวันแรก** | เซลล์ zone 1–2 ยังจับคู่และขับ bilirubin ได้ · bilirubin ขึ้นตามมาภายหลัง | bilirubin สูงมากตั้งแต่ต้น → ไม่น่าใช่ช็อกอย่างเดียว |
| **AST >> ALT + CK สูงมาก** | AST มีมากในกล้ามเนื้อ · กล้ามเนื้อสลายรุนแรง ALT ก็รั่วได้ (สไลด์ 2570) | rhabdomyolysis: INR bilirubin ปกติ |
| **Creatinine สูงร่วม** | ไตขาดเลือดจากช็อกเดียวกัน · myoglobin อุดท่อไต | พบได้ทั้ง ischemic และ rhabdomyolysis |

[[anim:lft7-zone3]]
""",
    ["✍️ ULN 40: mild ≤ ~200 · moderate 200–1,600 · marked > 1,600",
     "Transaminase หลายพัน: Para + Ischemic + Rhabdo (✍️ DDx 3 โรค)",
     "Zone 3 (รอบ central vein) ไวต่อช็อก paracetamol เหล้า halothane",
     "Shock liver: พุ่ง 1–3 วัน ลงเร็ว ALT/LDH < 1.5 → แก้ shock ต้นเหตุ",
     "AST >> ALT + CK สูงมาก + INR ปกติ = rhabdomyolysis ไม่ใช่ตับ"],
    [mcq("GI-LFT7-MCQ-03",
         "A 65-year-old diabetic woman with pneumonia had a blood pressure of 80/40 mmHg yesterday. Today AST is 3,900 U/L, ALT 3,500 U/L and LDH 4,800 U/L; bilirubin 0.7 mg/dL and ALP 140 U/L. What is the most appropriate management of the liver abnormality?",
         "Restore perfusion and treat the septic shock; the enzymes should fall rapidly",
         ["Urgent ERCP", "Prednisolone for presumed autoimmune hepatitis", "Liver biopsy before any treatment",
          "Immediate listing for liver transplantation"], 4,
         "เคสใหม่ในสไลด์ 2570: **ความดันตก + AST/ALT เป็นพัน + ALT/LDH = 3,500 ÷ 4,800 ≈ 0.7 (< 1.5)** + bilirubin ยังปกติ = **ischemic hepatitis (shock liver)**\n\n"
         "สไลด์: **แก้ไขภาวะ shock ต้นเหตุ** — เอนไซม์ลดลงอย่างรวดเร็วเมื่อการไหลเวียนกลับมา · ไม่มียาเฉพาะต่อตับ\n\n"
         "ERCP ใช้ใน cholangitis · steroid ไม่มีบทบาท · biopsy/ปลูกถ่ายตับไม่จำเป็นเมื่อสาเหตุชัดและแก้ได้",
         "ช็อก + ALT เป็นพัน + ALT/LDH < 1.5 → แก้ shock", "Ischaemic hepatitis", REF("เคสหญิง 65 ปี (shock liver)"),
         NL0 + ["2.2.7"]),
     mcq("GI-LFT7-MCQ-04",
         "Which region of the hepatic acinus is most vulnerable to hypotension, paracetamol overdose, alcohol and halothane?",
         "Zone 3 — the pericentral hepatocytes around the central vein",
         ["Zone 1 — the periportal hepatocytes", "Zone 2 — the midzonal hepatocytes",
          "The bile ductules within the portal tract", "The limiting plate at the portal–parenchymal interface"], 1,
         "✍️ อาจารย์เขียนใต้สไลด์ AST/ALT: **\"Zone 3 ใกล้ตรงกลาง = sensitive to shock / Para / เหล้า / halothane\"**\n\n"
         "- เลือดไหลจาก portal tract (zone 1) ไป central vein (zone 3) → **zone 3 ได้ O₂ น้อยสุด** ตายก่อนเมื่อช็อก\n"
         "- zone 3 มี **CYP2E1** มากสุด → สร้าง **NAPQI** จาก paracetamol และสารพิษจากเหล้า/halothane มากสุด\n"
         "- zone 1 = ไวรัสและสารพิษที่กินเข้าไป · limiting plate = interface hepatitis ของ AIH",
         "Zone 3 = ขาดเลือด paracetamol เหล้า halothane", "Hepatic zonation", REF("ลายมือ zone 3 ใต้สไลด์ AST/ALT"), NL0),
     mcq("GI-LFT7-MCQ-05",
         "A 30-year-old man is found on the floor after a prolonged generalised seizure. AST is 4,200 U/L, ALT 900 U/L, bilirubin 0.8 mg/dL and INR 1.0. His urine is dark and dipstick-positive for blood, with few red cells on microscopy. Which test is most useful next?",
         "Serum creatine kinase",
         ["Serum paracetamol level", "IgM anti-HAV", "Serum ceruloplasmin", "Doppler ultrasound of the hepatic veins"], 0,
         "✍️ อาจารย์: transaminase หลายพัน **DDx 3 โรค = Para + Ischemic + Rhabdomyolysis**\n\n"
         "เบาะแส rhabdomyolysis: **ชักนาน/นอนกดทับ** · **AST >> ALT** (AST มาจากกล้ามเนื้อ) · **bilirubin และ INR ปกติ** (ตับยังทำงาน) · ปัสสาวะ **dipstick blood บวกแต่ไม่มีเม็ดเลือดแดง = myoglobin** → ตรวจ **CK**\n\n"
         "ระดับ paracetamol ส่งได้ถ้าสงสัยกินยา แต่รูปแบบนี้ชี้ไปที่กล้ามเนื้อ · ไวรัสมี ALT > AST",
         "AST >> ALT + INR ปกติ + myoglobinuria → CK", "Rhabdomyolysis", REF("ลายมือ DDx 3 โรค (เคส paracetamol)"), NL0)])

NEW["gi-lft-10"] = sec(
    "gi-lft-10", "สไลด์ 2570: เคส ALT สูงเล็กน้อยจาก MASLD และ AIH ที่ globulin 6",
    "ชาย 55 ปี อ้วน AST 76 ALT 128 → NAFLD/MASLD (✍️ MAFLD) · หญิง 35 ปี อาการตับเรื้อรัง AST 600 ALT 575 globulin 6 → AIH · reversed A/G · polyclonal vs monoclonal",
    9, NL0 + ["2.3.4(6)", "B11.2.5(7)", "B1.4.11(2)"],
    """
### เคสใหม่ 1 — ชาย 55 ปี ตรวจสุขภาพประจำปี
ไม่มีประวัติโรคตับ ดื่มเพียงเล็กน้อย · **รูปร่างท้วม มีลักษณะ metabolic syndrome** (✍️ วงไว้) · **AST 76 · ALT 128** · ALP 68 · albumin globulin bilirubin ปกติ
- รูปแบบ: **mild diffused hepatocellular abnormality** (2–5 เท่า · R ≈ 5.6)
- จุดเปลี่ยน: **AST/ALT < 1** = non-alcoholic pattern (เหล้า AST มักนำ ALT)
- วินิจฉัย: **NAFLD/NASH** — ✍️ อาจารย์เขียน **"MAFLD"** · ชื่อปัจจุบันตามแนวทาง AASLD/EASL 2023 คือ **MASLD/MASH**
- ขั้นต่อไป (สไลด์ ✓ ทุกข้อ): **ประเมิน metabolic syndrome (DM HT DLP)** และ **อาจเจาะชิ้นเนื้อตับหากจำเป็น**
- เพิ่มเติม *(ไม่ได้มาจากสไลด์)*: ยังต้องตรวจ HBsAg anti-HCV ตาม algorithm "mild diffused LFT" · ประเมินพังผืดด้วย **FIB-4** ก่อนคิดเจาะชิ้นเนื้อ · รักษาหลักคือ **ลดน้ำหนัก 7–10%** ออกกำลังกาย คุมเบาหวานและไขมัน

[[anim:lft7-masld]]

### เคสใหม่ 2 — หญิง 35 ปี LFT ผิดปกติเรื้อรัง
อ่อนเพลีย ไม่ดื่มเหล้า ไม่เคยรับเลือด · **ขาดประจำเดือน · palmar erythema · spider telangiectasia** (✍️ วงไว้ "Chronic") · **TB 7 DB 4 · AST 600 ALT 575** (✍️ "พอ ๆ") · **albumin 3.3 · globulin 6**
- รูปแบบ: **moderate hepatocellular injury** ในหญิงอายุน้อย
- จุดเปลี่ยน: **hyperglobulinemia อย่างชัดเจน (globulin 6 g/dL)** ร่วมกับอาการทาง autoimmune
- วินิจฉัย: **autoimmune hepatitis** → ตรวจ **ANA · SMA (type 1 AIH)** ร่วมกับ IgG
- ✍️ ใต้สไลด์: **"Reverse A/G → represent chronic liver"** และ **"globulin ไม่สูงขนาดนี้"** (ในตับแข็งทั่วไป) · ✍️ โยง hyperglobulinemia กับคำว่า **"Monoclonal"**

#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **MASLD: ALT > AST** | ไขมันพอกทำให้เซลล์บวมอักเสบ ALT จาก cytosol รั่ว · mitochondria ยังไม่เสียมาก | เหล้า AST นำ · ตับแข็งทุกสาเหตุ AST นำ |
| **MASLD: อ้วนลงพุง DM ไขมันสูง** | insulin resistance → FFA เข้าตับมาก + insulin สูงกระตุ้นการสร้างไขมันในตับ | ไม่มีปัจจัยเมตาบอลิก → หาสาเหตุอื่น |
| **AIH: globulin 6 (polyclonal IgG)** | plasma cell ใน portal tract สร้าง IgG หลายชนิด | แถบเดียว (monoclonal) → myeloma/MGUS ต้องทำ SPEP |
| **ตับแข็งทั่วไป: globulin สูงเล็กน้อย** | แอนติเจนจากลำไส้ผ่าน portosystemic shunt โดยไม่ถูก Kupffer cell กรอง → กระตุ้นภูมิทั้งระบบ | สูงแค่ราว 4–5 · ✍️ "ไม่สูงขนาดนี้" |
| **Reversed A/G (< 1)** | albumin ลดเพราะสร้างไม่พอ (t½ 20 วัน → โรคต้องเป็นนาน) + globulin เพิ่ม | บอกว่าเป็น **โรคตับเรื้อรัง** |
| **ขาดประจำเดือน palmar erythema spider** | ตับเสื่อมกำจัด estrogen ไม่ได้ + แกน hypothalamus–pituitary–gonad ถูกกด | อาการแสดงของตับเรื้อรัง (✍️ "Chronic") |
| **AIH: AST ≈ ALT ระดับหลายร้อย** | interface hepatitis ทำลายเซลล์ต่อเนื่องแต่ไม่พร้อมกันทั้งตับ | moderate 5–40 เท่า ต่างจาก shock liver ที่เป็นพัน |
""",
    ["ALT > AST + อ้วน metabolic syndrome = MASLD (เดิม NAFLD · ✍️ MAFLD)",
     "MASLD: ประเมิน DM HT DLP + พังผืด (FIB-4) ก่อนคิด biopsy",
     "Globulin 6 ในหญิงอายุน้อย + อาการตับเรื้อรัง = AIH → ANA ASMA IgG",
     "Reversed A/G = ตับเรื้อรัง · globulin สูงมากหรือ monoclonal ต้องแยก myeloma"],
    [mcq("GI-LFT7-MCQ-06",
         "A 35-year-old woman has 1 year of fatigue and amenorrhoea. She has palmar erythema and spider naevi. TB 7 mg/dL, DB 4 mg/dL, AST 600 U/L, ALT 575 U/L, albumin 3.3 g/dL, globulin 6.0 g/dL. Viral markers are negative and she does not drink alcohol. Which tests best support the most likely diagnosis?",
         "Antinuclear and anti-smooth muscle antibodies with serum IgG",
         ["Antimitochondrial antibody", "Serum ferritin and transferrin saturation", "IgM anti-HEV",
          "Urine porphobilinogen"], 3,
         "เคสใหม่ในสไลด์ 2570: หญิงอายุน้อย **อาการตับเรื้อรัง** (ขาดประจำเดือน palmar erythema spider) · AST ≈ ALT ระดับ moderate · **globulin 6 (hyperglobulinemia ชัดเจน)** → **autoimmune hepatitis** → ตรวจ **ANA + SMA (type 1)** และ IgG (คะแนนใน simplified criteria)\n\n"
         "AMA ใช้ใน PBC (cholestatic) · ferritin ใช้ใน hemochromatosis (ไม่ทำให้ globulin สูง) · HEV เป็นเฉียบพลัน",
         "Globulin สูงมาก + transaminase moderate ในหญิงสาว = AIH → ANA ASMA IgG", "Autoimmune hepatitis",
         REF("เคสหญิง 35 ปี (AIH)"), NL0 + ["B1.4.11(2)"]),
     mcq("GI-LFT7-MCQ-07",
         "A 55-year-old man with BMI 31, hypertension and dyslipidaemia has AST 76 U/L, ALT 128 U/L and ALP 68 U/L; albumin, globulin and bilirubin are normal. He drinks one beer a week. HBsAg and anti-HCV are negative. What is the most likely diagnosis?",
         "Metabolic dysfunction–associated steatotic liver disease (MASLD/NAFLD)",
         ["Alcohol-associated hepatitis", "Autoimmune hepatitis", "Primary biliary cholangitis", "Wilson disease"], 4,
         "เคสใหม่ในสไลด์ 2570: **mild (2–5 เท่า) · AST/ALT < 1** · ALP ปกติ · มี **metabolic syndrome** · ไม่ดื่ม · ไวรัสลบ → **NAFLD/NASH** (ชื่อปัจจุบัน **MASLD**)\n\n"
         "เหล้า AST/ALT > 2 · AIH globulin สูง · PBC ALP สูง · Wilson มักอายุน้อยและ AST/ALT > 2 ในรายตับวาย\n\n"
         "ขั้นต่อไปตามสไลด์: ประเมิน DM HT DLP และอาจเจาะชิ้นเนื้อหากจำเป็น (ปัจจุบันประเมินพังผืดด้วย FIB-4 ก่อน)",
         "ALT > AST เล็กน้อย + metabolic syndrome = MASLD", "MASLD", REF("เคสชาย 55 ปี (NAFLD)"), NL0 + ["2.3.4(6)"])])

NEW["gi-lft-11"] = sec(
    "gi-lft-11", "สไลด์ 2570: Acute liver failure จาก Wilson disease — case challenge",
    "หญิง 17 ปี เหลืองเร็ว HE KF ring Hb 6.8 Coombs ลบ INR 3.8 · AST/ALT 2.48 > 2.2 · ALP 38 · ALP/TB 1.69 < 4 · ceruloplasmin 6.5 · urine Cu 680 · ATP7B",
    9, NL0 + ["2.3.11-3(7)", "B8.2.5-3(1)", "B3.2.5(2)"],
    """
สไลด์ใหม่หน้า 12 เป็น **"Acute liver failure case challenge"** ที่ขยายจากตัวเลข AST/ALT > 2.2 และ ALP/TB < 4 ในหัวข้อ Wilson เดิม

### เคส — หญิง 17 ปี
| หมวด | ข้อมูลในสไลด์ |
|---|---|
| ประวัติ | **เหลืองเข้มเร็วใน 5 วัน** ซึม ปัสสาวะเข้ม หลังอ่อนเพลีย 2 สัปดาห์ |
| ตรวจร่างกาย | ตาเหลือง palmar erythema · **asterixis + สับสน (HE grade I–II)** · ม้ามโต ascites ปานกลาง · **slit lamp: Kayser–Fleischer ring** |
| CBC/coag | **Hb 6.8 (Coombs-negative hemolytic anemia)** · **INR 3.8** |
| LFT | **AST 520 · ALT 210 → AST/ALT 2.48** · **TB 22.5** · **ALP 38 (ต่ำ)** → **ALP/TB 1.69** · albumin 2.4 |
| ทองแดง | **ceruloplasmin 6.5 mg/dL** (ปกติ 20–40) · **urine Cu 24 ชม. 680 µg** (ปกติ < 40) · **non-ceruloplasmin Cu 45 µg/dL** (ปกติ 5–15) |
| ยืนยัน | direct Coombs ลบ (hemolysis ที่ไม่ใช่ภูมิคุ้มกัน) · **ATP7B** homozygous/compound mutation |
| วินิจฉัย | **Acute Wilsonian liver failure (fulminant Wilson disease)** |

### ตัวเลขที่ต้องจำ (✍️ "จำ" ทั้งสองค่า)
- **AST/ALT > 2.2** — เคส 520 ÷ 210 = **2.48** (✍️ เขียน "(2.2)!" กำกับ)
- **ALP/TB < 4** — เคส 38 ÷ 22.5 = **1.69**
- สไลด์เรียกว่า "diagnostic triad": **(1) สองอัตราส่วนนี้ร่วมกัน** ("100% diagnostic accuracy") **(2) ALP ต่ำมากร่วมกับเหลืองมาก และ Coombs-negative hemolytic anemia**
- ข้อควรระวัง *(ไม่ได้มาจากสไลด์)*: "100%" มาจากการศึกษาขนาดเล็ก (Korman 2008) การศึกษาต่อมาพบความแม่นยำต่ำกว่า — ใช้เป็นเบาะแสแล้วยืนยันด้วยทองแดง KF ring และยีน

### เทียบกับคาบเดิม
- ✍️ **"AR"** · ✍️ ที่สไลด์ AST/ALT: **ไม่มีตับแข็ง + AST/ALT > 2 → Wilson หรือ alcohol**
- ✍️ ทางเลือด: **"hemato → Coombs negative → microspherocyte + auto agglutination"** (ลายมืออ่านได้ไม่ชัดทั้งหมด)
- ทองแดงในปัสสาวะ: สไลด์ใหม่ใช้ค่าปกติ **< 40 µg/วัน** · คาบเดิมเขียนเกณฑ์ดั้งเดิม > 100 µg — แนวทาง AASLD 2022 ถือว่า **> 40 µg/วัน ชวนสงสัย** และ > 100 µg สนับสนุนชัดเจน

#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Ceruloplasmin ต่ำ** | ATP7B ใส่ทองแดงลง apo-ceruloplasmin ไม่ได้ → สลายเร็ว | ต่ำได้ในตับวายทุกสาเหตุ · เป็น acute phase reactant จึงอาจปกติได้ |
| **Non-ceruloplasmin Cu และ urine Cu สูง** | ทองแดงที่ไม่ได้จับ ceruloplasmin ล้นเข้าเลือด กรองออกทางไต | ยืนยันเมื่อ ceruloplasmin กำกวม |
| **Coombs-negative hemolysis** | เซลล์ตับตายปล่อยทองแดงอิสระ → oxidative damage ต่อเยื่อหุ้มเม็ดเลือดแดง | ไม่ใช่ภูมิคุ้มกัน → Coombs ลบ |
| **Bilirubin สูงมาก (22.5)** | indirect จากเม็ดเลือดแดงแตก + direct จากตับวาย | ทำให้ ALP/TB ต่ำ |
| **ALP ต่ำผิดคาด** | กลไกยังไม่ชัด (สมมติฐาน: ทองแดงรบกวน zinc ซึ่งเป็นโคแฟกเตอร์ของ ALP) | เหลืองมากแต่ ALP ต่ำ → คิด Wilson |
| **AST > ALT (2.48)** | ทองแดงทำลาย mitochondria → AST จาก mitochondria รั่ว | ไวรัส/paracetamol มักไม่ได้อัตราส่วนนี้ |
| **ม้ามโต ascites ใน "เฉียบพลัน"** | มีตับแข็งซ่อนอยู่เดิม แล้วกำเริบ (acute on chronic) | บอกว่าทองแดงสะสมมานาน |

[[anim:lft7-wilson]]

**การรักษา** *(ไม่ได้มาจากสไลด์ · AASLD 2022)*: fulminant Wilson **พยากรณ์โรคแย่มากหากไม่ปลูกถ่ายตับ** → ส่งศูนย์ปลูกถ่ายตับทันที (New Wilson Index ≥ 11) · ระหว่างรอ: plasma exchange หรือ albumin dialysis ลดทองแดงและ hemolysis · chelation (D-penicillamine, trientine) ใช้ในรายเรื้อรัง
""",
    ["Wilsonian ALF: AST/ALT > 2.2 + ALP/TB < 4 (✍️ จำ)",
     "ALP ต่ำ + bilirubin สูงมาก + hemolysis Coombs ลบ ในวัยรุ่น = Wilson",
     "Ceruloplasmin ↓ · urine Cu ↑ (ปกติ < 40 µg/วัน) · non-ceruloplasmin Cu ↑ · KF ring · ATP7B",
     "Fulminant Wilson → ส่งปลูกถ่ายตับ"],
    [mcq("GI-LFT7-MCQ-08",
         "A 17-year-old girl presents with acute liver failure: AST 520 U/L, ALT 210 U/L, ALP 38 U/L, total bilirubin 22.5 mg/dL, Hb 6.8 g/dL with a negative direct Coombs test. Which pair of ratios supports acute Wilsonian liver failure?",
         "AST/ALT > 2.2 and ALP/total bilirubin < 4",
         ["AST/ALT < 1 and ALP/total bilirubin > 4", "ALT/LDH < 1.5 and AST/ALT < 1",
          "AST/ALT > 2.2 and ALP/total bilirubin > 10", "R ratio < 2 and AST/ALT < 1"], 2,
         "เคส case challenge ในสไลด์ 2570: **AST/ALT = 520 ÷ 210 = 2.48 (> 2.2)** และ **ALP/TB = 38 ÷ 22.5 = 1.69 (< 4)** — ✍️ อาจารย์เขียน **\"จำ\"** ทั้งสองค่า\n\n"
         "กลไก: ทองแดงทำลาย mitochondria → AST นำ · bilirubin สูงมากจาก **hemolysis Coombs ลบ** + ตับวาย ขณะที่ **ALP ต่ำผิดคาด** → อัตราส่วน ALP/TB ต่ำ\n\n"
         "ALT/LDH < 1.5 = ischemic hepatitis · AST/ALT < 1 = ไวรัส/MASLD",
         "Wilsonian ALF: AST/ALT > 2.2 + ALP/TB < 4", "Wilson disease", REF("Acute liver failure case challenge"),
         NL0 + ["2.3.11-3(7)"]),
     mcq("GI-LFT7-MCQ-09",
         "A 17-year-old with fulminant Wilson disease has haemolytic anaemia with a negative direct Coombs test. What is the mechanism of the haemolysis?",
         "Free (non-ceruloplasmin-bound) copper released from necrotic hepatocytes oxidatively damages red-cell membranes",
         ["IgG autoantibodies against red-cell surface antigens", "Hypersplenism from portal hypertension alone",
          "Microangiopathic fragmentation from disseminated intravascular coagulation", "Vitamin B12 deficiency from malabsorption"], 1,
         "สไลด์ 2570: **Coombs test direct negative (non-immune severe intravascular hemolysis)** · non-ceruloplasmin Cu 45 µg/dL (ปกติ 5–15)\n\n"
         "เซลล์ตับที่อัดทองแดงไว้ตายพร้อมกัน → **ทองแดงอิสระทะลักเข้าเลือด** → oxidative injury ต่อเยื่อหุ้มเม็ดเลือดแดง → แตกในหลอดเลือด · ไม่ผ่านแอนติบอดี Coombs จึงลบ\n\n"
         "IgG autoantibody ให้ Coombs บวก · hypersplenism ทำให้ซีดเล็กน้อยไม่ถึง Hb 6.8 เร็วขนาดนี้",
         "Wilson: ทองแดงอิสระ → hemolysis Coombs ลบ", "Wilson disease", REF("Acute liver failure case challenge"),
         NL0 + ["2.3.11-3(7)"])])

NEW["gi-lft-12"] = sec(
    "gi-lft-12", "สไลด์ 2570: Direct bilirubin สูง — ตับคั่งเลือด ตับอักเสบจากเหล้า ตับแข็งระยะท้าย DILI",
    "IB/TB > 0.8 ก่อนเข้าตับ · DB/TB > 0.5 ที่ตับหรือหลังตับ · liver congestion: congestive hepatopathy BCS SOS hyperthyroidism (✍️ HF/N-HF) · ✍️ alcoholic 4 forms · 80 g/วัน > 10 ปี",
    9, NL0 + ["2.3.9(5)", "2.3.11(2)", "B8.2.5(3)"],
    """
### Jaundice breakdown (สไลด์ 2570)
**Total bilirubin = direct (conjugated) + indirect (unconjugated)**
| เส้นทาง | เกณฑ์ | ผิดปกติที่ | สาเหตุในสไลด์ |
|---|---|---|---|
| **Path A — unconjugated** | **IB/TB > 0.8** | **ก่อนเข้าตับ** | hemolysis · **Gilbert** · **Crigler–Najjar** (✍️ ขีดเส้นใต้) |
| **Path B — conjugated** | **DB/TB > 0.5** | **ที่ตับหรือหลังตับ** | cholestasis ทุกชนิด + **liver congestion** (congestive hepatopathy · BCS · SOS · hyperthyroidism) · **alcoholic hepatitis** · **end-stage cirrhosis** · **DILI** |
- ✍️ วงคำว่า **"Direct"** ที่รูปตับ และ **"ผู้ใหญ่"** — ผู้ใหญ่ที่ตัวเหลืองส่วนใหญ่เป็นชนิด direct
- ✍️ แตก **"Liver congest" → HF / N-HF** · N-HF = **BCS · VOD (SOS) · hyperthyroidism**

[[anim:lft7-congest]]

### ตับคั่งเลือด — สี่สาเหตุในสไลด์
| สาเหตุ | ตำแหน่งที่เลือดออกไม่ได้ | เบาะแส |
|---|---|---|
| **Congestive hepatopathy (HF)** | หัวใจห้องขวา → IVC → hepatic vein | JVP สูง hepatojugular reflux ตับโตกดเจ็บ TR · ascites SAAG สูง โปรตีนสูง |
| **Budd–Chiari syndrome** | ลิ่มเลือดที่ hepatic vein หรือ IVC | ปวดท้อง ตับโต ascites เร็ว · ภาวะเลือดแข็งตัวง่าย (MPN) · Doppler ไม่เห็นการไหลใน hepatic vein |
| **Sinusoidal obstruction syndrome (VOD)** | endothelium ของ sinusoid | หลัง HSCT/เคมีบำบัด · สมุนไพรที่มี pyrrolizidine alkaloid · ตับโตเจ็บ น้ำหนักขึ้น เหลือง |
| **Hyperthyroidism** | ไม่ได้อุด — high-output HF + zone 3 ขาด O₂ สัมพัทธ์ + ฮอร์โมนทำลายเซลล์ตรง | thyroid storm ร่วมกับเหลือง · ยา PTU ก็ทำตับอักเสบได้ |
สไลด์ระบุเพียงชื่อสาเหตุ — **ตำแหน่งและเบาะแสในตารางนี้เติมจากตำรา (ไม่ได้มาจากสไลด์)**

### โรคตับจากเหล้า — ✍️ "Alcoholic – 4 forms"
หน้าว่างท้ายสไลด์ อาจารย์เขียนสดในห้อง: **① transaminitis … ④ cirrhosis** (ข้อ ② ③ ไม่ได้จด) · ✍️ อีกหน้า: **"80 g/day (> 10 ปี) → cirrhosis"**
สเปกตรัมมาตรฐาน (เติมข้อ ② ③ จากตำรา — ไม่ได้มาจากสไลด์):
| ระยะ | LFT | กลไก |
|---|---|---|
| **① ไขมันพอกจากเหล้า (transaminitis)** | AST ALT สูงเล็กน้อย AST นำ · GGT สูง · MCV โต | NADH เกินจากการเผาผลาญเหล้า → สร้างไขมันเพิ่ม เผาผลาญไขมันลด · หายได้ถ้าหยุดดื่ม |
| **② Alcoholic hepatitis** | **AST/ALT > 2 · AST มักไม่เกิน 300–400** · **bilirubin สูง (direct)** · WBC สูง ไข้ | acetaldehyde + ROS + endotoxin จากลำไส้กระตุ้น neutrophil · Mallory–Denk bodies |
| **③ พังผืด (fibrosis)** | อาจปกติ | stellate cell สร้าง collagen รอบ central vein |
| **④ ตับแข็ง** | albumin ต่ำ INR ยาว เกล็ดเลือดต่ำ · AST > ALT | nodule + พังผืดทั่วตับ |
- ประเมินความรุนแรง alcoholic hepatitis: **Maddrey DF ≥ 32 หรือ MELD > 20** → พิจารณา prednisolone 40 มก./วัน *(ไม่ได้มาจากสไลด์ · ACG 2024)*

#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **HF: direct bilirubin ขึ้น ALT ขึ้นเล็กน้อย** | CVP สูงย้อนถึง sinusoid → zone 3 ขาด O₂ ฝ่อ + sinusoid โป่งกด canaliculus | ดีขึ้นเมื่อรักษา HF · ถ้า cardiac output ตกฉับพลันกลายเป็น shock liver |
| **ตับโตกดเจ็บใน HF/BCS** | ตับบวมเลือดยืด Glisson capsule | ยุบลงเมื่อ CVP ลด |
| **Ascites โปรตีนสูง SAAG ≥ 1.1** | ความดัน sinusoid สูง แต่ sinusoid ยังรั่วโปรตีนได้ (ยังไม่เป็นพังผืด) | ตับแข็ง: SAAG สูงแต่โปรตีนต่ำ |
| **Alcoholic hepatitis: ไข้ WBC สูง** | การอักเสบจาก neutrophil ในตับเอง ไม่จำเป็นต้องติดเชื้อ | ต้องตัด SBP/ปอดอักเสบก่อนให้ steroid |
| **End-stage cirrhosis: direct bilirubin สูง** | เซลล์ตับเหลือน้อย ขั้นขับ bilirubin ออก (ใช้พลังงาน) เสียก่อนขั้นจับคู่ | bilirubin เป็นตัวแปรใน MELD และ Child–Pugh |
""",
    ["IB/TB > 0.8 = ก่อนตับ (hemolysis Gilbert Crigler–Najjar) · DB/TB > 0.5 = ที่ตับ/หลังตับ",
     "Liver congestion: HF · BCS · SOS · hyperthyroidism (✍️ HF / N-HF)",
     "Direct bilirubin สูงแบบไม่อุดตัน: congestion · alcoholic hepatitis · end-stage cirrhosis · DILI",
     "✍️ เหล้า 80 g/วัน > 10 ปี → cirrhosis · alcoholic hepatitis AST มักไม่เกิน 300–400"],
    [mcq("GI-LFT7-MCQ-13",
         "A 70-year-old man with severe tricuspid regurgitation and right heart failure has tender hepatomegaly, a raised JVP and ascites. TB 3.8 mg/dL, DB 2.6 mg/dL, ALP 190 U/L, GGT 160 U/L, AST 70 U/L, ALT 62 U/L. Ultrasound shows dilated hepatic veins and IVC without biliary dilatation. What is the most likely cause of the jaundice?",
         "Congestive hepatopathy",
         ["Gilbert syndrome", "Choledocholithiasis", "Haemolytic anaemia", "Acute hepatitis A"], 2,
         "สไลด์ 2570 เพิ่มสาเหตุของ **direct hyperbilirubinemia (DB/TB > 0.5)**: **liver congestion — congestive hepatopathy** · BCS · SOS · hyperthyroidism\n\n"
         "**DB/TB = 2.6 ÷ 3.8 ≈ 0.68** · หัวใจห้องขวาล้มเหลว → CVP สูงย้อนถึง sinusoid → zone 3 ขาด O₂ + sinusoid โป่งกดท่อน้ำดีฝอย → direct bilirubin ALP GGT สูงเล็กน้อย · **hepatic vein/IVC โป่ง ท่อน้ำดีไม่ขยาย**\n\n"
         "Gilbert และ hemolysis เป็น indirect · นิ่วในท่อจะเห็นท่อขยาย · ไวรัส ALT เป็นพัน",
         "HF + direct bilirubin + hepatic vein โป่ง ท่อไม่ขยาย = congestive hepatopathy", "Congestive hepatopathy",
         REF("การวิเคราะห์ Bilirubin & ดีซ่าน"), NL0 + ["2.3.9(5)"]),
     mcq("GI-LFT7-MCQ-14",
         "A 45-year-old man who has drunk about 120 g of alcohol daily for 15 years has 2 weeks of fever, tender hepatomegaly and jaundice. WBC 16,000/µL, TB 12 mg/dL, AST 220 U/L, ALT 90 U/L, INR 1.8. Which diagnosis best fits?",
         "Alcohol-associated hepatitis",
         ["Acute hepatitis A", "Ischaemic hepatitis", "Paracetamol toxicity", "Ascending cholangitis"], 1,
         "ดื่มหนักนาน (✍️ อาจารย์: **80 g/วัน > 10 ปี → cirrhosis**) + ไข้ ตับโตเจ็บ เหลือง WBC สูง + **AST/ALT ≈ 2.4 (> 2) และ AST < 300–400** + bilirubin สูง = **alcoholic hepatitis** (หนึ่งใน ✍️ \"Alcoholic – 4 forms\") · สไลด์ 2570 จัด alcoholic hepatitis เป็นสาเหตุของ direct hyperbilirubinemia\n\n"
         "ไวรัส/ขาดเลือด/paracetamol ค่าเป็นพัน · cholangitis เป็น cholestatic ALP เด่น\n\n"
         "*(ไม่ได้มาจากสไลด์)* Maddrey DF = 4.6 × (PT ผู้ป่วย − PT control) + TB ≥ 32 → พิจารณา prednisolone หลังตัดการติดเชื้อ",
         "เหล้าหนัก + ไข้ เหลือง + AST/ALT > 2 AST < 400 = alcoholic hepatitis", "Alcoholic hepatitis",
         REF("Causes of conjugated hyperbilirubinemia · ลายมือ Alcoholic 4 forms"), NL0 + ["2.3.11(2)", "B8.2.5(3)"])])

NEW["gi-lft-13"] = sec(
    "gi-lft-13", "สไลด์ 2570: ผลเลือดไวรัสตับอักเสบ — HAV HEV HCV HBV และ core window",
    "IgM anti-HAV · IgM anti-HEV · anti-HCV ขึ้นหลัง ~3 เดือน ค้างแม้หาย · HCV RNA = active · ตาราง HBV ห้าแถว · core window มีแต่ anti-HBc IgM",
    8, ["B8.3(2)", "2.1.13", "2.3.1(1)", "2.3.1-3(3)", "B8.2.2-3(5)"],
    """
สไลด์ 2570 ปิดท้ายด้วยผลเลือดไวรัส (หน้า 26–29) — คาบเดิมอ้างไปที่คาบ **Acute and chronic hepatitis (12 ต.ค.)** · หัวข้อนี้สรุปเฉพาะสิ่งที่อยู่ในสไลด์ LFT ใหม่

### Viral serology master matrix (สไลด์)
| ไวรัส | Marker | ความหมาย |
|---|---|---|
| **HAV** | **anti-HAV IgM** | ติดเชื้อเฉียบพลัน |
| HAV | anti-HAV IgG | เคยติดเชื้อ หรือได้วัคซีน |
| **HEV** | **anti-HEV IgM** | ติดเชื้อเฉียบพลัน (ใหม่ในสไลด์ 2570) |
| **HCV** | anti-HCV | กำลังติดเชื้อ **หรือ** เคยติดเชื้อ |
| HCV | **HCV RNA (PCR)** | ยืนยันว่ามีเชื้ออยู่ตอนนี้ (active) |
| **HBV** | HBV DNA · HBsAg · **anti-HBc IgM** | มีเชื้อ (active) · IgM = acute |
| HBV | HBeAg | ไวรัสแบ่งตัวสูง (replicative phase) |

### Acute HCV — ภูมิขึ้นช้า (สไลด์)
- **anti-HCV บวกหลังสัมผัสเชื้อราว 3 เดือน** → anti-HCV ลบในช่วงแรก **ตัด acute HCV ไม่ได้**
- **anti-HCV ลบ + HCV RNA บวก = acute HCV**
- anti-HCV **บวกตลอดไปแม้รักษาหายแล้ว** → ดูผลการรักษาด้วย HCV RNA ไม่ใช่ antibody
- กราฟในสไลด์: HCV RNA ขึ้นภายใน 1–2 สัปดาห์ · anti-HCV (EIA รุ่น 3) ขึ้นเฉลี่ย ~70 วัน

### ตาราง HBV ห้าแถว (สไลด์)
| ภาวะ | HBsAg | anti-HBs | anti-HBc IgG | anti-HBc IgM |
|---|---|---|---|---|
| Susceptible (ไม่มีภูมิ) | − | − | − | − |
| Immune จากวัคซีน | − | **+** | − | − |
| Immune จากการติดเชื้อ (past) | − | **+** | **+** | − |
| **Chronic** | **+** | − | **+** | − |
| **Acute** | +/− | − | +/− | **+** |
แถว acute ที่ HBsAg เป็นลบได้ คือ **core window** (✍️ อาจารย์เขียน "acute" ที่ช่วงนี้บนกราฟ)

[[anim:lft7-hbv]]

#### ทำไมถึงมีผลเลือดแบบนี้
| สิ่งที่เห็น | กลไก | ใช้อย่างไร |
|---|---|---|
| **IgM ขึ้นก่อน IgG** | B cell สร้าง IgM ก่อน แล้วจึง class-switch เป็น IgG | IgM = เฉียบพลัน (HAV HEV anti-HBc) |
| **Core window** | ภูมิจับ HBsAg เป็น immune complex จนตรวจไม่พบ ก่อน anti-HBs อิสระจะเหลือพอวัด | ตับอักเสบเฉียบพลันต้องส่ง **HBsAg + IgM anti-HBc** คู่กัน |
| **วัคซีน: anti-HBs อย่างเดียว** | วัคซีนมีแต่ HBsAg (recombinant) ไม่มี core | anti-HBc บวก = เคยติดเชื้อจริง |
| **anti-HCV ขึ้นช้าราว 3 เดือน** | HCV หลบภูมิได้ดี ภูมิขึ้นช้า | ช่วงแรกส่ง HCV RNA |
| **HAV ไม่เรื้อรัง** | ไวรัสถูกกำจัดหมดหลังติดเชื้อเฉียบพลัน (HEV เรื้อรังได้ในผู้ปลูกถ่ายอวัยวะ — ไม่ได้มาจากสไลด์) | ไม่มี "chronic HAV" |
✍️ ที่ algorithm acute hepatitis อาจารย์เขียนข้าง HBsAg ว่า **"Chronic > acute (พบมากกว่า)"** → ผู้ใหญ่ไทยที่ HBsAg บวกส่วนใหญ่เป็น chronic HBV (ติดตั้งแต่เกิด) จึงต้องดู IgM anti-HBc เพื่อแยก acute หรือ chronic กำเริบ
""",
    ["Acute HAV/HEV = IgM บวก · IgG = เคยติด/วัคซีน",
     "anti-HCV ขึ้นหลัง ~3 เดือน ลบช่วงแรกตัด acute HCV ไม่ได้ → HCV RNA · anti-HCV ค้างแม้หาย",
     "Core window: HBsAg − anti-HBs − anti-HBc IgM + = acute HBV",
     "anti-HBs + อย่างเดียว = วัคซีน · + anti-HBc IgG = เคยติดแล้วหาย · HBsAg > 6 เดือน = chronic"],
    [mcq("GI-LFT7-MCQ-15",
         "A 30-year-old man had acute hepatitis 4 months ago with ALT 1,800 U/L; ALT is now 90 U/L. HBsAg is negative, anti-HBs negative and IgM anti-HBc positive. What is the interpretation?",
         "Recovering acute hepatitis B in the window period",
         ["Chronic hepatitis B", "Immunity from hepatitis B vaccination", "Never infected (susceptible)"
          , "Past hepatitis B infection with established immunity"], 3,
         "ตาราง HBV ในสไลด์ 2570: **acute = HBsAg +/− · anti-HBs − · anti-HBc IgM +** · ช่วงที่ HBsAg หายแล้วแต่ anti-HBs ยังไม่ขึ้น = **core window** (✍️ \"acute\")\n\n"
         "chronic ต้อง HBsAg + นาน > 6 เดือน · วัคซีน = anti-HBs + อย่างเดียว · past = anti-HBs + และ anti-HBc IgG + · susceptible = ลบทุกตัว",
         "HBsAg − anti-HBs − IgM anti-HBc + = core window", "HBV serology", REF("Hepatitis B Panel Interpretation"),
         ["B8.3(2)", "2.3.1(1)"]),
     mcq("GI-LFT7-MCQ-16",
         "Six weeks after a needlestick injury from an HCV-positive patient, a nurse develops ALT 640 U/L. Anti-HCV is negative and HCV RNA is positive. What is the interpretation?",
         "Acute HCV infection — the antibody has not yet appeared",
         ["False-positive HCV RNA; infection is excluded by the negative antibody", "Past HCV infection that has cleared",
          "Chronic HCV infection", "HCV is unlikely; look for hepatitis A instead"], 0,
         "สไลด์ 2570 (Acute HCV immune response): **anti-HCV บวกหลังสัมผัสเชื้อราว 3 เดือน** — ลบในช่วงแรก **ตัด acute HCV ไม่ได้** · **anti-HCV ลบแต่ HCV RNA บวก = acute HCV**\n\n"
         "past infection = anti-HCV + แต่ RNA − · chronic = RNA + นานกว่า 6 เดือน (และ anti-HCV มักบวก)",
         "anti-HCV − + HCV RNA + = acute HCV", "HCV serology", REF("Acute HCV immune response"),
         ["B8.3(2)", "2.3.1(1)"])])

# ตำแหน่งแทรกหัวข้อใหม่: ต่อจากหัวข้อเดิมที่เกี่ยวข้อง
AFTER = {"gi-lft-09": "gi-lft-03", "gi-lft-10": "gi-lft-04", "gi-lft-11": "gi-lft-10",
         "gi-lft-12": "gi-lft-07", "gi-lft-13": "gi-lft-08"}

OBJECTIVES = [
    "แปลเคสใหม่ในสไลด์ 2570: shock liver, MASLD, AIH ที่ globulin สูง และ Wilsonian acute liver failure",
    "บอกสาเหตุของ direct hyperbilirubinemia ที่ไม่ใช่การอุดตัน และแปลผลเลือดไวรัสตับอักเสบ (core window, acute HCV)",
]
GUIDES = [
    "**สไลด์ อ.กิตติ ปี 2570 (LFT 2570.pdf · 30 หน้า)** — 3 pillars · เคสใหม่ · master algorithm · ผลเลือดไวรัส (โน้ต slides/lft2570_notes.md) · คาบนี้ระบุจุดที่ต่างจากสไลด์ 2563 ด้วย callout \"2570\"",
    "**AASLD Practice Guidance: MASLD (2023)** และ multisociety nomenclature 2023 — MASLD/MASH · FIB-4",
    "**Korman et al. Hepatology 2008** — ALP/TB < 4 + AST/ALT > 2.2 ใน acute liver failure จาก Wilson",
    "**ACG Clinical Guideline: Alcohol-associated liver disease (2024)** — Maddrey DF/MELD · prednisolone",
]
SUBTITLE_ADD = " · สไลด์ 2570: 3 pillars · shock liver · MASLD · AIH globulin สูง · Wilson ALF · ตับคั่งเลือด · ผลเลือดไวรัส"
NLGAP_OLD = "และสไลด์ปี 2563 ไม่ได้กล่าวถึงการรักษา"
NLGAP_NEW = "และสไลด์ทั้งปี 2563 และ 2570 ไม่ได้กล่าวถึงการรักษา (ยกเว้น \"แก้ shock\" ใน shock liver)"


# ═════════════════════════════════════════════════════════════════ apply
CALLOUT_RE = re.compile(r"^> \*\*2570 · [^*]+\*\*")


def strip_mine(md):
    """ถอด callout '> **2570 · …**' และ marker [[anim:lft7-*]] ที่สคริปต์นี้เคยใส่"""
    out, skip = [], False
    for ln in md.split("\n"):
        if CALLOUT_RE.match(ln):
            skip = True
            continue
        if skip and ln.startswith(">"):
            continue
        skip = False
        if re.match(r"^\s*\[\[anim:lft7-[\w-]+\]\]\s*$", ln):
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
    # แทรกหัวข้อใหม่ (คงฟิลด์ที่เครื่องมืออื่นอาจเติมให้ภายหลัง เช่น figs/imgs/anims อื่น/mnem อื่น)
    for sid in ["gi-lft-09", "gi-lft-10", "gi-lft-11", "gi-lft-12", "gi-lft-13"]:
        s = json.loads(json.dumps(NEW[sid]))
        old = keep.get(sid, {})
        for k in ("figs", "imgs"):
            if old.get(k):
                s[k] = old[k]
        s["anims"] = {k: v for k, v in (old.get("anims") or {}).items() if not k.startswith("lft7-")}
        s["mnem"] = [m for m in (old.get("mnem") or []) if m.get("name") not in {x["name"] for x in AN.MNEM}]
        i = next(j for j, x in enumerate(secs) if x["id"] == AFTER[sid])
        secs.insert(i + 1, s)
    byid = {s["id"]: s for s in secs}
    # หัวข้อเดิม: แก้ข้อความ · callout · source
    for sid, s in byid.items():
        if sid in my_ids:
            continue
        md = strip_mine(s["md"])
        for a, b in TEXT_FIX.get(sid, []):
            md = md.replace(a, b)
        for head, block in CALLOUTS.get(sid, []):
            md = insert_block(md, head, block)
        s["md"] = md
        if sid in CALLOUTS and SRC_TAG not in s.get("source", ""):
            s["source"] = s.get("source", "") + SRC_TAG
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
    # ระดับคาบ
    L["date"] = "พฤ. 29 ต.ค."
    if SUBTITLE_ADD.strip(" ·") not in L["subtitle"]:
        L["subtitle"] = L["subtitle"] + SUBTITLE_ADD
    for o in OBJECTIVES:
        if o not in L["objectives"]:
            L["objectives"].append(o)
    g = L.setdefault("guidelines", [])
    for x in GUIDES:
        if x not in g:
            g.append(x)
    if NLGAP_OLD in L.get("nlGap", ""):
        L["nlGap"] = L["nlGap"].replace(NLGAP_OLD, NLGAP_NEW)
    return L


def main():
    data = json.load(open(PATH, encoding="utf-8"))
    before = json.dumps(data, ensure_ascii=False)
    old_items = {i["id"]: (i["choices"], i["answer"]) for L in data if L["lec"] == LEC for s in L["sections"] for i in s["items"]}
    old_keys = {(s["id"], f, k) for L in data if L["lec"] == LEC for s in L["sections"]
                for f in ("anims", "figs") for k in (s.get(f) or {})}
    old_mn = {(s["id"], m["name"]) for L in data if L["lec"] == LEC for s in L["sections"] for m in s.get("mnem", [])}
    others = [json.dumps(L, ensure_ascii=False) for L in data if L["lec"] != LEC]
    L = apply(data)
    # ตรวจ: ข้อเดิมไม่เปลี่ยน · ภาพ/หลักจำเดิมยังอยู่ · คาบอื่นไม่เปลี่ยน · id ไม่ซ้ำ · ไม่มี code fence
    now = {i["id"]: (i["choices"], i["answer"]) for s in L["sections"] for i in s["items"]}
    for k, v in old_items.items():
        if not k.startswith("GI-LFT7-"):
            assert now.get(k) == v, ("ข้อเดิมเปลี่ยน", k)
    keys = {(s["id"], f, k) for s in L["sections"] for f in ("anims", "figs") for k in (s.get(f) or {})}
    assert old_keys <= keys, old_keys - keys
    assert old_mn <= {(s["id"], m["name"]) for s in L["sections"] for m in s.get("mnem", [])}
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
    new = [i for s in L["sections"] for i in s["items"] if i["id"].startswith("GI-LFT7-")]
    from collections import Counter
    print("หัวข้อ %d (ใหม่ %d) · ข้อใหม่ %d ตำแหน่งคำตอบ %s · anims ใหม่ %d · mnem ใหม่ %d" % (
        len(L["sections"]), len(NEW), len(new), dict(sorted(Counter(i["answer"] for i in new).items())), len(AN.ITEMS), len(AN.MNEM)))
    out = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    changed = json.dumps(data, ensure_ascii=False) != before
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
