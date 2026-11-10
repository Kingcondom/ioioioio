# -*- coding: utf-8 -*-
# Part C: MEQ, OSCE, lecture assembly and dump
import json
from gus_b import SECTIONS, THAI
from gus_a import CDC, LEC_REF

LECTURE = "Genital ulcer และ syphilis (บันทึกเสียง อ. 10 พ.ย. — ไม่ระบุชื่ออาจารย์)"

MEQ = [
    {
        "id": "ID-GUS-MEQ-01",
        "part": "MEQ",
        "lec": "10/11",
        "lecture": LECTURE,
        "topic": "Secondary syphilis with ocular involvement in a man who has sex with men — serology, LP decision, treatment, follow-up and partners",
        "vignette": "ผู้ป่วยชายไทยอายุ 28 ปี อาชีพพนักงานออฟฟิศ มาด้วยผื่นตามตัวและตาขวามัว 2 สัปดาห์\nPI: 2 เดือนก่อนมีแผลที่ขอบทวารหนัก ไม่เจ็บ หายเองใน 3 สัปดาห์ · 3 สัปดาห์ก่อนมีผื่นแดงน้ำตาลไม่คันที่ลำตัว ฝ่ามือ และฝ่าเท้า ผมร่วงเป็นหย่อม · 2 สัปดาห์ก่อนตาขวาแดง มัว เห็นจุดลอย\nPH: มีเพศสัมพันธ์กับชาย คู่นอนหลายคนใน 6 เดือน ใช้ถุงยางไม่สม่ำเสมอ · ไม่เคยตรวจ HIV · ไม่มีประวัติแพ้ยา\nPE: BT 37.6 C · papulosquamous rash ที่ลำตัว ฝ่ามือ ฝ่าเท้า · ต่อมน้ำเหลืองโตทั่วตัว กดไม่เจ็บ · patchy alopecia · ตาขวา visual acuity 20/80 จักษุแพทย์ตรวจพบ panuveitis · cranial nerve และตรวจระบบประสาทอื่นปกติ ไม่มี meningism\nLab: RPR reactive 1:128 · TPPA reactive · anti-HIV (A1) reactive รอ A2/A3",
        "questions": [
            {"q": "1. จงให้การวินิจฉัยที่สมบูรณ์ที่สุด และบอกเหตุผลจากประวัติและตรวจร่างกาย (3 คะแนน)",
             "a": "**Secondary syphilis ร่วมกับ ocular syphilis (panuveitis)** · สงสัย **HIV ร่วม**\nเหตุผล: แผลไม่เจ็บที่ขอบทวารซึ่งหายเอง = **chancre** (ใน MSM มักอยู่รอบทวารจึงไม่ทันสังเกต) · 4–10 สัปดาห์ต่อมามี **ผื่น papulosquamous ไม่คันรวมฝ่ามือฝ่าเท้า + ต่อมน้ำเหลืองโตทั่วตัวไม่เจ็บ + ผมร่วงเป็นหย่อม** = secondary · ตาแดงมัวจาก panuveitis = **ocular syphilis ซึ่งเกิดได้ทุกระยะ** · RPR titre สูง + TPPA บวก ยืนยัน"},
            {"q": "2. จงแปลผล RPR และ TPPA ของผู้ป่วยรายนี้ และบอกว่าจะใช้การตรวจใดติดตามผลการรักษา (2 คะแนน)",
             "a": "- **RPR (non-treponemal)** วัด antibody ต่อ cardiolipin ที่หลุดจากเซลล์ถูกทำลาย → **titre 1:128 บอกว่าโรค active**\n- **TPPA (treponemal)** วัด antibody ต่อตัวเชื้อ → **ยืนยันว่าเป็นซิฟิลิสจริง ไม่ใช่ biologic false positive** แต่จะบวกตลอดชีวิต\n- **ติดตามด้วย RPR แบบ titre วิธีเดิมทุกครั้ง** (VDRL กับ RPR เทียบ titre กันไม่ได้) · TPPA ใช้ติดตามไม่ได้"},
            {"q": "3. ผู้ป่วยรายนี้จำเป็นต้องเจาะน้ำไขสันหลังก่อนรักษาหรือไม่ เพราะเหตุใด (2 คะแนน)",
             "a": "**ไม่จำเป็นต้องเจาะก่อนรักษา** (CDC 2021): ocular syphilis ที่จักษุแพทย์พบรอยโรคชัดและ **cranial nerve กับการตรวจระบบประสาทปกติ** ไม่ต้องตรวจ CSF ก่อน และ **ต้องรักษาแบบ neurosyphilis แม้ CSF ปกติ** — ไม่ควรรอผล CSF\nเจาะเมื่อ: มี cranial nerve dysfunction, meningitis, stroke, สับสน หรือรักษาแล้ว titre ไม่ลดร่วมกับอาการทางประสาท · (otosyphilis อย่างเดียวก็ไม่ต้องเจาะ)"},
            {"q": "4. จงเขียนการรักษาซิฟิลิสของผู้ป่วยรายนี้ พร้อมขนาดยา ระยะเวลา และสิ่งที่ต้องบอกผู้ป่วยหลังเริ่มยา (4 คะแนน)",
             "a": "- **Aqueous crystalline penicillin G 18–24 ล้านยูนิต/วัน IV** = **3–4 ล้านยูนิตทุก 4 ชั่วโมง** (หรือหยดต่อเนื่อง) **10–14 วัน** — ไม่ใช้ benzathine เดี่ยว เพราะไม่ได้ระดับยาใน CSF/น้ำในลูกตา\n- ทางเลือกถ้ามั่นใจว่ามาฉีดครบ: procaine penicillin 2.4 MU IM วันละครั้ง + probenecid 500 mg qid 10–14 วัน\n- พิจารณา BPG 2.4 MU IM สัปดาห์ละครั้ง 1–3 ครั้งหลังครบคอร์ส\n- ดูแลร่วมกับจักษุแพทย์ (steroid เสริมใช้บ่อยแต่ไม่พิสูจน์)\n- **เตือน Jarisch–Herxheimer reaction**: ไข้ หนาวสั่น ปวดเมื่อยภายใน 24 ชม. พบบ่อยใน secondary — **ไม่ใช่แพ้ยา** ให้ยาลดไข้และรักษาต่อ"},
            {"q": "5. ถ้าผล anti-HIV ยืนยันว่าติดเชื้อ จะเปลี่ยนแผนการรักษาและติดตามซิฟิลิสอย่างไร (2 คะแนน)",
             "a": "- **สูตรยาซิฟิลิสเหมือนผู้ไม่ติด HIV** ไม่ต้องเพิ่มขนาด\n- **ติดตามถี่ขึ้น**: RPR ที่ **3, 6, 9, 12 และ 24 เดือน** · หลัง neurosyphilis/ocular syphilis ถ้า RPR ในเลือดกลับปกติไม่ต้องเจาะ CSF ซ้ำ\n- เกณฑ์ CSF ผิดปกติในผู้ติด HIV ใช้เม็ดเลือดขาวมากกว่า 20 · ส่งต่อเริ่ม ART เร็ว"},
            {"q": "6. จงบอกการจัดการคู่นอนและการป้องกันการติดซ้ำ (2 คะแนน)",
             "a": "- คู่นอนที่สัมผัส **ภายใน 90 วัน** → ให้ **BPG 2.4 MU IM ครั้งเดียวทันทีแม้ผลเลือดลบ** · เกิน 90 วันตรวจก่อน (ถ้าติดตามยากให้รักษาไปเลย)\n- secondary syphilis ต้องตามคู่ย้อนหลัง **6 เดือน + ระยะที่มีอาการ**\n- ตรวจ STI อื่น (หนองใน chlamydia ทุกตำแหน่งที่สัมผัส) · ถุงยาง\n- **Doxy-PEP (CDC 2024)**: MSM ที่เคยเป็นซิฟิลิสใน 12 เดือน เสนอ doxycycline 200 mg ภายใน 72 ชม. หลังเพศสัมพันธ์ที่ไม่ใช้ถุงยาง"},
        ],
        "ref": [LEC_REF + " — ระยะของซิฟิลิส serology และการรักษา neuro/ocular/otic syphilis",
                CDC + " — Syphilis; Neurosyphilis, ocular syphilis, and otosyphilis",
                "CDC Doxy-PEP guidelines 2024"],
        "nl": ["2.3.1(19)", "2.3.7-3(8)", "3.3.16", "3.3.15", "2.3.1(9)"],
        "years": [],
        "_kind": "meq",
        "_set": "id",
    },
    {
        "id": "ID-GUS-MEQ-02",
        "part": "MEQ",
        "lec": "10/11",
        "lecture": LECTURE,
        "topic": "Syphilis detected at antenatal screening in a woman reporting penicillin allergy",
        "vignette": "หญิงไทยอายุ 24 ปี G1P0 อายุครรภ์ 14 สัปดาห์ มาฝากครรภ์ครั้งแรก ไม่มีอาการผิดปกติ\nPH: ไม่เคยตรวจเลือดมาก่อน จำไม่ได้ว่าเคยมีแผลหรือผื่น · ให้ประวัติว่าเด็ก ๆ เคยกิน amoxicillin แล้วมีผื่นลมพิษทั้งตัวและหายใจไม่สะดวก ต้องไปโรงพยาบาล\nPE: ไม่พบแผลที่อวัยวะเพศ ไม่มีผื่น ไม่มีต่อมน้ำเหลืองโต ตรวจระบบประสาทและตาปกติ\nLab (ตรวจคัดกรองฝากครรภ์ตามลำดับขั้นของโรงพยาบาล): treponemal CLIA reactive → RPR reactive 1:16 · anti-HIV negative · HBsAg negative",
        "questions": [
            {"q": "1. จงแปลผลการตรวจ และบอกระยะของโรคที่ใช้ในการรักษา พร้อมเหตุผล (3 คะแนน)",
             "a": "- ลำดับนี้คือ **reverse algorithm** (เริ่มด้วย treponemal test) ซึ่ง **คู่มือกรมควบคุมโรคกำหนดให้ใช้คัดกรองหญิงตั้งครรภ์** · CLIA บวก + RPR บวก 1:16 = **ซิฟิลิส active**\n- ไม่มีอาการ = **latent** · ไม่เคยตรวจมาก่อนและจำแผลหรือผื่นไม่ได้ → **latent syphilis of unknown duration → รักษาแบบ late latent** (อาจารย์เน้น)"},
            {"q": "2. จงบอกการรักษาที่เหมาะสม เมื่อผู้ป่วยให้ประวัติแพ้ penicillin แบบนี้ (4 คะแนน)",
             "a": "- **หญิงตั้งครรภ์ใช้ penicillin เท่านั้น** — เป็นยาเดียวที่ป้องกัน congenital syphilis ได้ · **ห้าม doxycycline/tetracycline** · erythromycin/azithromycin ผ่านรกไม่พอ · ceftriaxone ข้อมูลไม่พอ\n- ประวัติลมพิษร่วมกับหายใจไม่สะดวก = เสี่ยง IgE-mediated → ส่งประเมิน (skin test ถ้าทำได้) แล้ว **penicillin desensitization** ในโรงพยาบาลที่พร้อมรับมือ anaphylaxis\n- จากนั้นให้ **benzathine penicillin G 2.4 ล้านยูนิต IM สัปดาห์ละครั้ง × 3 ครั้ง** (แบ่งฉีดสะโพกข้างละ 1.2 ล้านยูนิต)\n- (หมายเหตุ: ข้อสอบมักถามว่า \"ทางเลือกเหมือนคนไม่ตั้งครรภ์\" — ถูกเฉพาะสูตร penicillin ไม่ใช่ยาทางเลือก)"},
            {"q": "3. หลังเข็มแรก ผู้ป่วยกลับมาฉีดเข็มที่สองช้าไป 12 วันนับจากเข็มแรก จะทำอย่างไร (1 คะแนน)",
             "a": "หญิงตั้งครรภ์ **ระยะห่างเกิน 9 วันยอมรับไม่ได้ → เริ่มชุด 3 เข็มใหม่ทั้งหมด** (CDC 2021) · ควรโทรตามและนัดภายใน 2 วันถ้าพลาดนัดวันที่ 7"},
            {"q": "4. จงบอกสิ่งที่ต้องเฝ้าระวังหลังฉีดยาและการติดตามระหว่างตั้งครรภ์ (3 คะแนน)",
             "a": "- **Jarisch–Herxheimer reaction** ภายใน 24 ชม. (ไข้ ปวดเมื่อย) · ในครึ่งหลังของการตั้งครรภ์อาจทำให้ **มดลูกหดรัดตัว เจ็บครรภ์ก่อนกำหนด หรือ fetal distress** → ให้มาโรงพยาบาลถ้ามีไข้ ท้องแข็ง หรือลูกดิ้นน้อย แต่ไม่เลื่อนการรักษา\n- **RPR titre วิธีเดิม**: รักษาที่ ≤ 24 สัปดาห์ → ตรวจซ้ำไม่เร็วกว่า 8 สัปดาห์หลังรักษาและตอนคลอด\n- ล้มเหลว (คู่มือไทย): titre เพิ่ม ≥ 4 เท่า · หรือลดน้อยกว่า 4 เท่า หรือยัง ≥ 1:8 หลัง 6 เดือน · อาการกลับมา\n- **ultrasound ทารก** ถ้าวินิจฉัยหลัง 20 สัปดาห์ · ตรวจคัดกรองซ้ำที่อายุครรภ์ 28–32 สัปดาห์ (ติดซ้ำได้จากคู่)"},
            {"q": "5. จงบอกการดูแลสามีและการวางแผนสำหรับทารกแรกเกิด (3 คะแนน)",
             "a": "- **สามี/คู่นอน** ตรวจ serology และรักษาตามผล (ซิฟิลิสไม่ทราบระยะของภรรยา → ประเมินคู่ระยะยาว · ถ้าผลบวกรักษาตามระยะ) · ตรวจ HIV และ STI อื่น — ถ้าไม่รักษาคู่ ภรรยาจะติดซ้ำระหว่างตั้งครรภ์\n- **ทารก**: แจ้งกุมารแพทย์ ตรวจ RPR ทารกเทียบกับแม่ (วิธีเดียวกัน) ตรวจร่างกายหาอาการ congenital syphilis (ตับม้ามโต ผื่นลอก snuffles) · ถ้าแม่รักษาไม่เพียงพอ (เช่น คลอดภายใน 30 วันหลังรักษา) ต้องประเมินเต็มที่และรักษาด้วย **aqueous penicillin G 50,000 ยูนิต/กก. IV ทุก 12 ชม. (อายุ ≤ 7 วัน) แล้วทุก 8 ชม. รวม 10 วัน**"},
        ],
        "ref": [LEC_REF + " — ซิฟิลิสในหญิงตั้งครรภ์ (อาจารย์: ข้อสอบชอบถาม)",
                CDC + " — Syphilis during pregnancy; Latent syphilis",
                THAI],
        "nl": ["2.3.1(19)", "2.3.16-3(1)", "2.3.15-3(11)", "B1.4.11(1)", "3.3.16"],
        "years": [],
        "_kind": "meq",
        "_set": "id",
    },
]

OSCE = [
    {
        "id": "ID-GUS-OSCE-01",
        "part": "OSCE/SAQ",
        "lec": "10/11",
        "lecture": LECTURE,
        "topic": "SAQ – Interpreting syphilis serology in five patients",
        "station": "SAQ (แปลผลการตรวจทางห้องปฏิบัติการ) 5 นาที",
        "instruction": "จงแปลผลการตรวจซิฟิลิสของผู้ป่วย 5 รายต่อไปนี้ และบอกสิ่งที่ควรทำต่อ\n\n| ราย | ข้อมูลทางคลินิก | RPR | TPPA |\n|---|---|---|---|\n| A | หญิง 30 ปี เป็น SLE ไม่มีอาการ | reactive 1:2 | nonreactive |\n| B | ชาย 40 ปี รักษาซิฟิลิสครบเมื่อ 5 ปีก่อน มีเอกสาร | nonreactive | reactive |\n| C | ชาย 22 ปี แผลไม่เจ็บที่องคชาต 4 วัน | nonreactive | nonreactive |\n| D | หญิง 25 ปี ผื่นทั่วตัวรวมฝ่ามือ ผมร่วงหย่อม | nonreactive (ไม่เจือจาง) | reactive |\n| E | ชาย 35 ปี ไม่มีอาการ ไม่เคยตรวจและไม่เคยรักษา | reactive 1:8 | reactive |\n\n**เขียนคำตอบเป็นข้อ ๆ ทีละราย**",
        "answer": "**เกณฑ์ให้คะแนน (10 คะแนน)**\n\n| ราย | คำตอบที่ต้องได้ | คะแนน |\n|---|---|---|\n| A | **Biologic false positive** ของ non-treponemal test (cardiolipin ไม่จำเพาะ — SLE, autoimmune, malaria, leptospirosis, ตั้งครรภ์) · ไม่ต้องรักษาซิฟิลิส | 2 |\n| B | **เคยติดเชื้อและรักษาแล้ว** — treponemal test บวกตลอดชีวิต · ไม่ต้องรักษาซ้ำถ้าไม่มีอาการหรือความเสี่ยงใหม่ | 2 |\n| C | **ยังสรุปว่าไม่เป็นไม่ได้** — chancre ขึ้นก่อน serology บวก · ตรวจจากแผล (darkfield หรือ PCR) ตรวจ HSV NAAT · เจาะซ้ำ 2–4 สัปดาห์ หรือรักษา presumptive ถ้าความเสี่ยงสูง · ตรวจ HIV | 2 |\n| D | **สงสัย prozone phenomenon** ใน secondary syphilis → ขอให้ห้องปฏิบัติการ **เจือจาง serum (เช่น 1:16) แล้วตรวจ RPR ใหม่** · รักษาด้วย BPG 2.4 MU IM ครั้งเดียว | 2 |\n| E | **Latent syphilis ไม่ทราบระยะ** → รักษาแบบ late latent: **BPG 2.4 MU IM สัปดาห์ละครั้ง × 3** · ตรวจ HIV · ประเมินคู่ · ติดตาม RPR ที่ 6, 12, 24 เดือน | 2 |\n\n**ข้อที่ทำให้เสียคะแนน**: ใช้ TPPA ติดตามผลการรักษา · รักษาราย A หรือ B ด้วย penicillin โดยไม่จำเป็น · บอกว่าราย C ไม่เป็นซิฟิลิสแน่นอน · ให้ BPG ครั้งเดียวในราย E",
        "ref": [LEC_REF + " — non-treponemal กับ treponemal test", CDC + " — Syphilis, diagnostic considerations", THAI],
        "nl": ["3.3.16", "B10.3(8)", "B1.5.1(8)", "2.3.1(19)"],
        "years": [],
        "_kind": "meq",
        "_set": "id",
    },
    {
        "id": "ID-GUS-OSCE-02",
        "part": "OSCE/SAQ",
        "lec": "10/11",
        "lecture": LECTURE,
        "topic": "OSCE – Counselling a patient newly diagnosed with primary syphilis",
        "station": "OSCE (ให้คำปรึกษาผู้ป่วยมาตรฐาน) 5 นาที",
        "instruction": "ชายอายุ 27 ปี มีแผลไม่เจ็บที่องคชาต 1 สัปดาห์ ผล darkfield พบ spirochete · RPR reactive 1:16 · TPHA reactive · ไม่มีประวัติแพ้ยา\n\nแพทย์วินิจฉัย **primary syphilis** ผู้ป่วยถามว่า \"ต้องกินยานานไหม แฟนต้องรู้ไหม แล้วจะหายขาดหรือเปล่า\"\n\n**จงอธิบายโรค การรักษา และให้คำแนะนำผู้ป่วยภายใน 5 นาที**",
        "answer": "**เกณฑ์ให้คะแนน (10 คะแนน)**\n\n| ข้อ | สิ่งที่ต้องทำ | คะแนน |\n|---|---|---|\n| 1 | แนะนำตัว ยืนยันตัวผู้ป่วย ใช้ห้องที่เป็นส่วนตัว ไม่ตัดสินพฤติกรรม | 1 |\n| 2 | อธิบายว่าเป็น **ซิฟิลิสระยะแรก** ติดต่อทางเพศสัมพันธ์ · **แผลหายเองได้แต่โรคไม่หาย** ถ้าไม่รักษาจะเข้าระยะที่ 2 และทำลายระบบประสาท ตา หัวใจได้ · **รักษาหายได้** | 2 |\n| 3 | การรักษา: **benzathine penicillin G 2.4 ล้านยูนิต ฉีดเข้ากล้ามครั้งเดียว** (แบ่งสะโพกสองข้าง) ไม่ต้องกินยาต่อ | 1 |\n| 4 | เตือน **Jarisch–Herxheimer reaction** — ไข้ หนาวสั่น ปวดเมื่อยใน 24 ชม. หลังฉีด ไม่ใช่แพ้ยา กินยาลดไข้ได้ ถ้าหายใจลำบากหรือผื่นลมพิษให้กลับมาทันที | 1 |\n| 5 | **คู่นอนต้องรู้และมารักษา** — คู่นอนใน **90 วัน** ได้ยาฉีดทันทีแม้ผลเลือดปกติ · ตามคู่ย้อนหลัง 3 เดือน + ระยะที่มีแผล · เสนอวิธีแจ้งคู่ (แจ้งเอง หรือให้เจ้าหน้าที่ช่วยโดยไม่เปิดเผยชื่อ) | 2 |\n| 6 | **งดเพศสัมพันธ์** จนรักษาครบและแผลหาย และจนคู่ได้รับการรักษา · ใช้ถุงยางทุกครั้ง | 1 |\n| 7 | ตรวจ **HIV** และ STI อื่นวันนี้ · เสนอ PrEP ถ้าผลลบและเสี่ยงสูง | 1 |\n| 8 | นัด **ติดตาม RPR ที่ 6 และ 12 เดือน** — ต้องลด 4 เท่า · TPHA จะบวกตลอดไปไม่ได้แปลว่าไม่หาย · ติดซ้ำได้ ไม่มีภูมิคุ้มกัน · เปิดโอกาสถาม | 1 |\n\n**ข้อที่ทำให้เสียคะแนน**: บอกว่าแผลหายแล้วไม่ต้องรักษา · บอกให้คู่รอดูอาการก่อน · ไม่พูดถึง HIV · ใช้คำตำหนิ · เปิดเผยข้อมูลผู้ป่วยกับคู่โดยไม่ได้รับอนุญาต",
        "ref": [LEC_REF + " — การรักษาซิฟิลิสระยะแรก", CDC + " — Syphilis, management of sex partners; Primary and secondary syphilis"],
        "nl": ["2.3.1(19)", "B10.2.2(1)", "3.3.15"],
        "years": [],
        "_kind": "meq",
        "_set": "id",
    },
]

LEC = {
    "lec": "10/11",
    "date": "อ. 10 พ.ย.",
    "title": "Genital ulcer และ syphilis",
    "subtitle": "ประเมินแผลอวัยวะเพศและตารางแยกห้าโรค · chancroid · genital herpes วินิจฉัยและยา · เริมรุนแรงและ encephalitis · donovanosis และ LGV · ระยะของซิฟิลิส · อาการแต่ละระยะ · serology และลำดับการตรวจ · neuro ocular otic syphilis · รักษาตามระยะ แพ้ยา และ JH reaction · ตั้งครรภ์ ติดตาม titre คู่นอน และการป้องกัน",
    "objectives": [
        "ซักประวัติและตรวจแผลที่อวัยวะเพศอย่างเป็นระบบ และแยก syphilis chancroid herpes donovanosis และ LGV จากลักษณะแผลและต่อมน้ำเหลือง",
        "เลือกการตรวจที่เหมาะสมสำหรับแผลอวัยวะเพศ ได้แก่ serology ซิฟิลิส HSV NAAT และการตรวจ HIV และอธิบายข้อจำกัดของ Tzanck smear",
        "สั่งยาต้านไวรัสสำหรับ genital herpes ครั้งแรก กลับเป็นซ้ำ กดการกำเริบ ผู้ภูมิคุ้มกันบกพร่อง และ HSV encephalitis ได้ถูกขนาด",
        "รักษา chancroid donovanosis และ LGV ด้วยยาและระยะเวลาที่ถูกต้อง",
        "จัดระยะซิฟิลิสเป็น early late และ neurosyphilis และอธิบายอาการเด่นของแต่ละระยะ",
        "แปลผล non-treponemal และ treponemal test ร่วมกัน รวมถึงผลบวกลวง prozone serofast และลำดับการตรวจแบบ traditional และ reverse",
        "บอกข้อบ่งชี้การเจาะหลังและให้การรักษา neurosyphilis ocular และ otic syphilis",
        "รักษาซิฟิลิสตามระยะ ในผู้แพ้ penicillin ผู้ติด HIV และหญิงตั้งครรภ์ และอธิบาย Jarisch–Herxheimer reaction",
        "ติดตาม titre หลังรักษา ตัดสินการรักษาล้มเหลว จัดการคู่นอน และให้คำแนะนำการป้องกันรวมถึง doxy-PEP",
    ],
    "guidelines": [
        "**CDC Sexually Transmitted Infections Treatment Guidelines, 2021** (MMWR Recomm Rep 2021;70(4)) — chancroid, genital herpes, granuloma inguinale, LGV, syphilis ทุกระยะ, neurosyphilis/ocular/otic syphilis, ซิฟิลิสในหญิงตั้งครรภ์, การจัดการคู่นอน",
        "**CDC Laboratory Recommendations for Syphilis Testing, United States, 2024** (MMWR Recomm Rep 2024;73(1)) — traditional เทียบ reverse algorithm, titre ของ VDRL กับ RPR เทียบกันไม่ได้",
        "**CDC Clinical Guidelines on the Use of Doxycycline Postexposure Prophylaxis for Bacterial STI Prevention, 2024** (MMWR Recomm Rep 2024;73(2))",
        "**CDC NCHHSTP Dear Colleague letter — Bicillin L-A shortage (10 มี.ค. 2026)** — สงวน benzathine penicillin G ให้หญิงตั้งครรภ์ ใช้ doxycycline ในผู้ไม่ตั้งครรภ์ และนำเข้า Lentocilin",
        "**WHO Guidelines for the management of symptomatic sexually transmitted infections (2021)** — genital ulcer syndromic management",
        "**WHO Updated recommendations for the treatment of Neisseria gonorrhoeae, Chlamydia trachomatis and Treponema pallidum (syphilis), and new recommendations on syphilis testing and partner services (2024)** และ WHO guidelines for the treatment of Treponema pallidum (2016)",
        "**กรมควบคุมโรค (กลุ่มบางรักโรคติดต่อทางเพศสัมพันธ์ กองโรคเอดส์และโรคติดต่อทางเพศสัมพันธ์) — คู่มือการตรวจวินิจฉัยและติดตามการรักษาโรคซิฟิลิสทางห้องปฏิบัติการ (2564)** — สูตรยาตามระยะ, reverse algorithm สำหรับหญิงตั้งครรภ์, prozone, serofast, เกณฑ์รักษาล้มเหลวในหญิงตั้งครรภ์",
        "**กองโรคเอดส์และโรคติดต่อทางเพศสัมพันธ์ — สถานการณ์โรคซิฟิลิสแต่กำเนิด ประเทศไทย พ.ศ. 2565** — การคัดกรองซ้ำที่อายุครรภ์ 28–32 สัปดาห์",
    ],
    "nlGap": "เกณฑ์ฯ มีรหัส STI รวม (`นล. 2.3.1(19)`, `B10.2.2(1)`) herpes simplex (`2.3.1(8)`) และ treponemal serology (`3.3.16`, `B10.3(8)`) แต่ **ไม่มีรหัสแยกของ LGV, granuloma inguinale, neurosyphilis/ocular/otic syphilis และ penicillin desensitization** และบันทึกเสียงไม่มีสไลด์ประกอบ ตารางยาส่วนนั้นจึงอิงแนวทางด้านล่าง",
    "sections": SECTIONS,
    "meq": MEQ,
    "osce": OSCE,
}

if __name__ == "__main__":
    out = "/tmp/claude-0/-home-user-ioioioio/dcdfbb25-5693-54b2-b69b-68e8376251a3/scratchpad/newlec/id_gus.json"
    json.dump(LEC, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", out, len(SECTIONS), "sections", sum(len(s["items"]) for s in SECTIONS), "mcq")
