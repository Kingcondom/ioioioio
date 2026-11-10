# -*- coding: utf-8 -*-
# Part A: helpers + sections 01-06 (genital ulcer, chancroid, HSV, donovanosis, LGV)

SRC = "บรรยาย (ไม่ได้ระบุชื่ออาจารย์ในบันทึก) — Genital ulcer และ syphilis (อ. 10 พ.ย. 2569, บันทึกเสียง)"
LEC_REF = "บรรยาย 10 พ.ย. 2569 (บันทึกเสียง)"
CDC = "CDC STI Treatment Guidelines 2021"


def mcq(i, topic, stem, choices, answer, explain, pearl, ref, nl):
    assert len(choices) == 5 and len(set(choices)) == 5, i
    return {"id": "ID-GUS-MCQ-%02d" % i, "kind": "mcq", "topic": topic, "stem": stem,
            "choices": choices, "answer": answer, "explain": explain, "pearl": pearl,
            "src": "", "ref": ref, "nl": nl}


SECTIONS = []

# ---------------------------------------------------------------- 01
SECTIONS.append({
    "id": "id-gus-01",
    "title": "แนวทางประเมินแผลที่อวัยวะเพศ และตารางแยกห้าโรค",
    "summary": "ดูจำนวน ความเจ็บ ความแข็ง ขอบ พื้นแผล และต่อมน้ำเหลือง แล้วตรวจซิฟิลิส HSV และ HIV ทุกราย เพราะดูด้วยตาอย่างเดียวไม่แม่น",
    "minutes": 8,
    "source": SRC,
    "nl": ["2.1.48", "2.3.1(19)", "B10.2.2(1)", "2.1.57", "3.3.15"],
    "md": """### ขอบเขตของคาบนี้
กลุ่มโรคที่รอยโรค **จำกัดอยู่ที่อวัยวะเพศ ทวารหนัก หรือรอบทวาร (perianal)** มาได้หลายรูปแบบ — แผล (ulcer) · หูด (wart) · ตุ่มน้ำ (vesicle) · แผลเดียวหรือหลายแผล

### สิ่งที่อาจารย์ให้ดูทุกครั้งที่เจอแผล
- **จำนวน** แผลเดียวหรือหลายแผล · แยกกันหรือรวมกัน — แต่ **อย่าใช้จำนวนแผลอย่างเดียวแยกโรค** (chancroid มักแผลเดียวแต่หลายแผลได้ · chancre ก็หลายแผลได้)
- **ความเจ็บ** — ถามว่าเจ็บตุบ ๆ ไหม (บางคนเจ็บ บางคนไม่เจ็บ)
- **ความแข็งเมื่อคลำ (induration)** · **ขอบแผล** ยกนูน เซาะ หรือขรุขระ · **พื้นแผล** สะอาด มีหนอง หรือแดงสด
- **ต่อมน้ำเหลืองขาหนีบ** โต เจ็บ แข็ง หรือแตกเป็นหนอง (bubo)

### ตารางแยกโรค
| โรค | เชื้อ | ลักษณะแผล | เจ็บ | ต่อมน้ำเหลือง | ตรวจที่ช่วย |
|---|---|---|---|---|---|
| **Syphilis (chancre)** | Treponema pallidum | แผลเดียว 1–2 ซม. · ขอบนูนแข็ง · พื้นสะอาด | **ไม่เจ็บ** | โต แข็ง ไม่เจ็บ | darkfield หรือ PCR จากแผล · serology |
| **Chancroid (แผลริมอ่อน)** | Haemophilus ducreyi | นุ่ม ลึก · ขอบขรุขระเซาะ · พื้นหนองดูสกปรก | **เจ็บ** | เจ็บ อาจเป็น bubo แตก | Gram stain แบบฝูงปลา · NAAT |
| **Genital herpes** | HSV-2 (HSV-1 ได้) | ตุ่มน้ำเป็นกลุ่มบนพื้นแดง → แผลตื้นหลายแผล | **เจ็บ/แสบ** | เจ็บ (ครั้งแรก) | **HSV NAAT (PCR)** · Tzanck |
| **Granuloma inguinale** | Klebsiella granulomatis | ค่อย ๆ โต · แดงสด เลือดออกง่าย · ขอบขรุขระ | ไม่ค่อยเจ็บ | ไม่โตจริง (pseudobubo) | Donovan bodies จาก crush prep หรือชิ้นเนื้อ |
| **LGV** | Chlamydia trachomatis L1–L3 | ตุ่มหรือแผลเล็ก หายเร็ว มักไม่ทันเห็น | ไม่เจ็บ | **โตเด่น เจ็บ แตกเป็นหนอง** (ฝีมะม่วง) | C. trachomatis NAAT |

### หลักปฏิบัติ
- ลักษณะแผล **ทับซ้อนกันมาก** และติดเชื้อร่วมได้ — อาจารย์ย้ำว่าแผลริมอ่อนกับแผลซิฟิลิส **ขนาดใกล้กันมาก แยกยาก** จึงต้อง **differential ซิฟิลิสกับเริมทุกครั้ง**
- ผู้ป่วยแผลอวัยวะเพศทุกราย: **serology ซิฟิลิส + ตรวจ HSV จากแผล (NAAT) + ตรวจ HIV** (CDC 2021) · ถ้ามี chancroid ระบาดให้ตรวจ H. ducreyi ด้วย
- **Serology ซิฟิลิสอาจยังลบ** เพราะแผลขึ้นก่อนแอนติบอดี (อาจารย์เน้น) → ตรวจจากแผลโดยตรง หรือเจาะเลือดซ้ำ 2–4 สัปดาห์
- WHO 2021: ที่ที่ตรวจ molecular ไม่ได้ ให้รักษาแบบ **syndromic** ในวันที่มาตรวจ (ครอบคลุมซิฟิลิส ± chancroid ± HSV ตามระบาดวิทยาท้องถิ่น)
- แผลทุกชนิด **เพิ่มโอกาสติดและแพร่ HIV**
""",
    "pearls": [
        "จำนวนแผลอย่างเดียวแยกโรคไม่ได้ — ดูความเจ็บ ความแข็ง ขอบ พื้นแผล และต่อมน้ำเหลืองร่วมกัน",
        "ไม่เจ็บ + แข็ง + สะอาด = chancre · เจ็บ + นุ่ม + หนอง = chancroid · ตุ่มน้ำเป็นกลุ่ม = HSV",
        "LGV: แผลเล็กจนไม่ทันเห็น แต่ต่อมน้ำเหลืองโตเด่น (ฝีมะม่วง)",
        "แผลอวัยวะเพศทุกราย → ตรวจซิฟิลิส + HSV NAAT + HIV",
    ],
    "items": [
        mcq(1, "Initial work-up of genital ulcer disease",
            "A 26-year-old man has had a single genital ulcer for 5 days. He had condomless sex with a new partner 3 weeks ago. Which approach to investigation is most appropriate for every patient presenting with a genital ulcer?",
            ["Gram stain of the ulcer only, because most ulcers are bacterial",
             "Clinical diagnosis from the ulcer appearance, with laboratory tests only if treatment fails",
             "Syphilis serology, HSV nucleic acid amplification test from the lesion, and HIV testing",
             "Viral culture of the ulcer only",
             "Excisional biopsy of the ulcer for histology"],
            2,
            "CDC 2021 ระบุว่าการวินิจฉัยแผลอวัยวะเพศจาก **ลักษณะแผลอย่างเดียวไม่แม่น** และพบติดเชื้อร่วมได้ → ทุกรายควรได้ **serology ซิฟิลิส + HSV NAAT จากแผล + ตรวจ HIV**\n\nGram stain อย่างเดียวช่วยเฉพาะ chancroid และไม่ไว · viral culture ไวต่ำกว่า NAAT · การตัดชิ้นเนื้อสงวนไว้สำหรับแผลเรื้อรังหรือสงสัยมะเร็ง/donovanosis · การรอให้รักษาล้มเหลวก่อนตรวจทำให้พลาดซิฟิลิสและ HIV",
            "แผลอวัยวะเพศ = ซิฟิลิส + HSV + HIV ทุกราย",
            [LEC_REF + " — การประเมินแผลอวัยวะเพศ", CDC + " — Diseases characterized by genital, anal, or perianal ulcers"],
            ["2.1.48", "2.3.1(19)", "3.3.15"]),
        mcq(2, "Unreliable feature in ulcer differentiation",
            "When differentiating the cause of a genital ulcer clinically, which single feature is the LEAST reliable for distinguishing chancroid from primary syphilis?",
            ["Presence or absence of pain",
             "Induration of the ulcer on palpation",
             "Appearance of the ulcer base (clean versus purulent)",
             "Character of the inguinal lymph nodes",
             "Number of ulcers (single versus multiple)"],
            4,
            "อาจารย์เน้นว่า **จำนวนแผลไม่ควรใช้เป็นเกณฑ์เดียว** — chancroid มักแผลเดียวแต่หลายแผลได้ และ chancre ก็หลายแผลได้ ขนาดแผลทั้งสองก็ใกล้กัน\n\nสิ่งที่ช่วยแยกได้ดีกว่าคือ **ความเจ็บ** (chancroid เจ็บ · chancre ไม่เจ็บ) **ความแข็ง** (chancre แข็ง · chancroid นุ่ม = แผลริมอ่อน) **พื้นแผล** (chancroid มีหนองดูสกปรก · chancre สะอาด) และ **ต่อมน้ำเหลือง** (chancroid เจ็บ อาจเป็น bubo) — แต่สุดท้ายต้องตรวจทางห้องปฏิบัติการยืนยัน",
            "นับแผลไม่พอ — ต้องคลำความแข็งและถามความเจ็บ",
            [LEC_REF + " — ลักษณะแผล chancroid เทียบ chancre"],
            ["2.1.48", "2.3.1(19)"]),
    ],
})

# ---------------------------------------------------------------- 02
SECTIONS.append({
    "id": "id-gus-02",
    "title": "Chancroid (แผลริมอ่อน) — แยกจาก chancre และรักษาแบบครั้งเดียว",
    "summary": "H. ducreyi ทำแผลนุ่ม เจ็บ พื้นหนอง ต่างจาก chancre ที่แข็ง ไม่เจ็บ พื้นสะอาด และรักษาด้วย azithromycin หรือ ceftriaxone ครั้งเดียว",
    "minutes": 7,
    "source": SRC,
    "nl": ["2.3.1(19)", "B10.2.2(1)", "2.1.48", "3.1.9", "B1.5.2(5)", "B1.7.2"],
    "md": """### Chancroid
- เชื้อ **Haemophilus ducreyi** — Gram-negative coccobacillus · ย้อม Gram เรียงเป็นแถวเหมือน **ฝูงปลา (school of fish)** (อาจารย์ให้ดูภาพ)
- แผล **นุ่ม ลึก เจ็บ** มีสารคัดหลั่งคล้ายหนองซึม ทำให้พื้นแผล **ดูสกปรก** · มักแผลเดียวแต่หลายแผลได้
- **ต่อมน้ำเหลืองขาหนีบโต** อาจแข็งหรือกลายเป็นหนอง (bubo)

### แผลริมอ่อน เทียบ แผลริมแข็ง — อาจารย์สรุปให้จำ
| | Chancroid | Syphilis chancre |
|---|---|---|
| ภาษาไทย | **แผลริมอ่อน** | **แผลริมแข็ง** |
| คลำ | นุ่ม | แข็ง (indurated) |
| เจ็บ | เจ็บ | ไม่เจ็บ |
| พื้นแผล | หนองซึม สกปรก | สะอาด |
| ขนาด | ใกล้กันมาก — แยกจากขนาดไม่ได้ | ใกล้กันมาก |

- อาจารย์: ทางคลินิกแยกยาก → ต้องตรวจซิฟิลิสทุกครั้ง · **VDRL อาจยังลบ** เพราะแผลซิฟิลิสระยะแรกขึ้นก่อนที่ serology จะบวก · ถ้าแผลเป็นมาราว **2 สัปดาห์** โอกาสพบหลักฐานซิฟิลิสมากขึ้น
- ตรวจหาเชื้อซิฟิลิสโดยตรงจากแผล: **darkfield** หรือ **PCR (nucleic acid amplification test)**

### Probable chancroid (CDC 2021) — ต้องครบ 4 ข้อ
1. แผลเจ็บอย่างน้อย 1 แผล
2. ลักษณะแผลและต่อมน้ำเหลืองเข้าได้กับ chancroid
3. **ไม่พบ T. pallidum** จากแผล และ serology ซิฟิลิสลบ (เจาะหลังแผลขึ้นอย่างน้อย 7–14 วัน)
4. **HSV NAAT หรือ culture จากแผลลบ**

### การรักษา
| ยา | ขนาด | หมายเหตุจากอาจารย์ |
|---|---|---|
| **Azithromycin** | **1 g กินครั้งเดียว** | เม็ด 250 mg = 4 เม็ดพร้อมกัน — **คลื่นไส้มาก** แม้ดูกินง่าย |
| **Ceftriaxone** | **250 mg IM ครั้งเดียว** | cephalosporin ฉีดครั้งเดียว |
| **Ciprofloxacin** | 500 mg วันละ 2 ครั้ง **3 วัน** | fluoroquinolone |
| **Erythromycin base** | 500 mg วันละ 3 ครั้ง **7 วัน** | ใช้เมื่อไม่มี azithromycin |

- นัดดู **3–7 วัน** — อาการดีขึ้นใน 3 วัน แผลดีขึ้นชัดใน 7 วัน · ไม่ดีขึ้น → ทบทวนการวินิจฉัย ติดเชื้ออื่นร่วม HIV ไม่กินยา หรือดื้อยา
- Bubo เป็นหนอง → **เจาะดูดหรือผ่าระบาย** (แผลต่อมน้ำเหลืองหายช้ากว่าแผล)
- คู่นอนภายใน **10 วัน** ก่อนเริ่มอาการ → ตรวจและรักษาแม้ไม่มีอาการ · **ตรวจ HIV ทุกราย** (ผู้ติด HIV และชายที่ไม่ได้ขลิบตอบสนองช้ากว่า)
""",
    "pearls": [
        "Chancroid = แผลริมอ่อน: นุ่ม เจ็บ พื้นหนอง + ต่อมน้ำเหลืองเจ็บ/bubo",
        "Gram stain: Gram-negative coccobacilli เรียงแบบฝูงปลา",
        "Azithromycin 1 g ครั้งเดียว · ceftriaxone 250 mg IM ครั้งเดียว · cipro 500 bid 3 วัน · erythro 500 tid 7 วัน",
        "นัด 3–7 วัน · คู่นอน 10 วันก่อนอาการ · ตรวจซิฟิลิสและ HIV เสมอ",
    ],
    "mnem": [{
        "name": "You do cry (ducreyi)",
        "what": "จำว่า chancroid คือแผลที่เจ็บ",
        "lines": [["Ducreyi", "Haemophilus **ducreyi** — \"it's so painful, you **do cry**\" → แผลเจ็บ ต่างจาก chancre ของซิฟิลิสที่ไม่เจ็บ"]],
        "note": "ใช้คู่กับคำไทยของอาจารย์: แผลริม**อ่อน** (chancroid) เทียบ แผลริม**แข็ง** (syphilis)",
        "src": "First Aid for the USMLE Step 1 (Haemophilus ducreyi — \"you do cry\")",
    }],
    "items": [
        mcq(3, "Treatment of chancroid",
            "A 28-year-old man has a painful, soft, 1.5-cm penile ulcer with a ragged edge and a purulent base, and a tender left inguinal node. Gram stain of the exudate shows Gram-negative coccobacilli in parallel chains. Darkfield examination and HSV PCR of the ulcer are negative. What is the most appropriate treatment?",
            ["Azithromycin 1 g orally as a single dose",
             "Benzathine penicillin G 2.4 million units IM once",
             "Acyclovir 400 mg orally three times daily for 7–10 days",
             "Doxycycline 100 mg orally twice daily for 21 days",
             "Metronidazole 2 g orally as a single dose"],
            0,
            "แผลนุ่ม เจ็บ พื้นหนอง + ต่อมน้ำเหลืองเจ็บ + Gram-negative coccobacilli เรียงเป็นแถว (**school of fish**) + ตัดซิฟิลิสและ HSV แล้ว = **chancroid** จาก H. ducreyi → **azithromycin 1 g ครั้งเดียว** (หรือ ceftriaxone 250 mg IM ครั้งเดียว · cipro 500 mg bid 3 วัน · erythromycin base 500 mg tid 7 วัน)\n\nBenzathine penicillin รักษาซิฟิลิส ไม่ครอบคลุม H. ducreyi · acyclovir รักษา HSV · doxycycline 21 วันเป็นสูตรของ LGV · metronidazole ใช้กับ trichomonas",
            "Chancroid → azithromycin 1 g ครั้งเดียว",
            [LEC_REF + " — การรักษาแผลริมอ่อน", CDC + " — Chancroid"],
            ["2.3.1(19)", "B1.7.2", "3.1.9"]),
        mcq(4, "Chancre versus chancroid",
            "Which combination of findings most strongly favors primary syphilis over chancroid?",
            ["A painful, soft ulcer with a purulent base",
             "Multiple grouped vesicles on an erythematous base",
             "A ragged, undermined ulcer edge with a suppurative inguinal bubo",
             "A painless, indurated ulcer with a clean base and firm, non-tender inguinal nodes",
             "A beefy-red ulcer that bleeds easily on contact without lymphadenopathy"],
            3,
            "**Chancre = แผลริมแข็ง**: ไม่เจ็บ คลำแข็ง พื้นสะอาด ต่อมน้ำเหลืองโต แข็ง ไม่เจ็บ — เพราะ T. pallidum ทำให้เกิด endarteritis และการอักเสบแบบ lymphocyte/plasma cell ไม่มีหนองมาก\n\nแผลนุ่ม เจ็บ หนอง ขอบเซาะ + bubo = **chancroid (แผลริมอ่อน)** · ตุ่มน้ำเป็นกลุ่ม = **HSV** · แผลแดงสด เลือดออกง่าย ไม่มีต่อมน้ำเหลืองโต = **donovanosis**",
            "แข็ง ไม่เจ็บ สะอาด = chancre",
            [LEC_REF + " — แผลริมอ่อน เทียบ แผลริมแข็ง"],
            ["2.3.1(19)", "2.1.48"]),
    ],
})

# ---------------------------------------------------------------- 03
SECTIONS.append({
    "id": "id-gus-03",
    "title": "Genital herpes — ลักษณะทางคลินิกและการวินิจฉัย",
    "summary": "ตุ่มน้ำใสเป็นกลุ่มบนพื้นแดงที่กลับเป็นซ้ำ วินิจฉัยด้วย HSV NAAT จากแผล ส่วน Tzanck smear ถูกแต่ไม่ไวและไม่จำเพาะ",
    "minutes": 7,
    "source": SRC,
    "nl": ["2.3.1(8)", "B4.2.2(5)", "2.3.1(19)", "3.1.10", "2.1.48"],
    "md": """### ธรรมชาติของโรค
- เป็น **ไวรัส ไม่ใช่แบคทีเรีย** · ติดแล้ว **อยู่ตลอดชีวิต** (แฝงใน sensory ganglion) และกลับเป็นซ้ำได้
- ตำแหน่งที่พบบ่อยคือ **อวัยวะเพศและช่องปาก** แต่พบใกล้เคียงได้ เช่น **ขาหนีบ สะโพก รอบทวาร**
- โดยทั่วไป **HSV-1 → ปาก · HSV-2 → อวัยวะเพศ** แต่สลับกันได้ (ไม่บ่อย) · อาจารย์: ถ้าพบ HSV-1 ที่อวัยวะเพศ ให้นึกถึงช่องทางการติด เช่น oral sex และกลุ่มชายที่มีเพศสัมพันธ์กับชาย (MSM) ซึ่งเป็นที่ทวารหนักได้

> **อัปเดตแนวทาง ·** CDC 2021 ระบุว่า **HSV-1 เป็นสาเหตุของ genital herpes ครั้งแรกในสัดส่วนที่เพิ่มขึ้น** โดยเฉพาะในวัยรุ่น ผู้หญิง และ MSM (ไม่จำกัดเฉพาะ MSM) และ **genital HSV-1 กลับเป็นซ้ำน้อยกว่า HSV-2** — การรู้ type จึงช่วยบอกพยากรณ์และวางแผน suppressive therapy

### ลักษณะรอยโรค
- **กลุ่มตุ่มน้ำใส (grouped vesicles)** มี **ขอบแดงเป็นฐาน** → แตกเป็นแผลตื้นหลายแผล เจ็บแสบ
- ครั้งแรกมักรุนแรงกว่า อาจมีไข้ ต่อมน้ำเหลืองขาหนีบเจ็บ ปัสสาวะแสบ · ครั้งต่อมาเบากว่าและมักกลับมาที่ตำแหน่งเดิม

### การวินิจฉัย
| วิธี | เห็นอะไร | ข้อดีและข้อจำกัด |
|---|---|---|
| **Tzanck smear** (ขูดฐานแผลย้อม) | **multinucleated giant cells** | ถูกมาก — อาจารย์ยกตัวอย่างต้นทุน **ไม่ถึง 50 บาท** · แต่ **ไม่ไวและไม่จำเพาะ** แยก HSV จาก VZV ไม่ได้ |
| **HSV NAAT (PCR) จากแผล** | DNA ของไวรัส · บอก type ได้ | **ไวที่สุด** · แพงกว่าหลายเท่า (อาจารย์ประมาณหลายร้อยถึงราว 1,000 บาท แล้วแต่สถานที่) |
| Viral culture | ไวรัสขึ้น | ไวต่ำ โดยเฉพาะแผลที่ตกสะเก็ดหรือแผลที่กลับเป็นซ้ำ |
| Type-specific serology (IgG ต่อ glycoprotein G) | เคยติด HSV-1 หรือ HSV-2 | ใช้บางสถานการณ์ เช่น แผลหายแล้วหรือคู่นอนของผู้ป่วย · **HSV IgM ไม่แนะนำ** |

> **อัปเดตแนวทาง ·** อาจารย์เล่าว่า Tzanck smear เป็นวิธีดั้งเดิมที่ถูกกว่า PCR ราว 100 เท่า — **CDC 2021 แนะนำ HSV NAAT จากแผลเป็นวิธีที่เลือก** และระบุว่า **Tzanck/cytology ไม่ไวและไม่จำเพาะ ไม่ควรใช้เป็นหลัก** · ไม่แนะนำ HSV IgM และไม่ควรใช้ PCR จากเลือดยกเว้นสงสัย disseminated infection
""",
    "pearls": [
        "HSV = ไวรัสแฝงตลอดชีวิต · ตุ่มน้ำใสเป็นกลุ่มบนพื้นแดง แตกเป็นแผลตื้นหลายแผล",
        "HSV-1 ปาก · HSV-2 อวัยวะเพศ แต่สลับได้ · genital HSV-1 เป็นซ้ำน้อยกว่า",
        "Tzanck: multinucleated giant cells — ถูกแต่ไม่ไว แยก HSV/VZV ไม่ได้",
        "วิธีที่เลือกคือ HSV NAAT (PCR) จากแผล",
    ],
    "items": [
        mcq(5, "Preferred diagnostic test for genital herpes",
            "A 23-year-old woman has painful grouped vesicles and shallow ulcers on the labia for 3 days, with dysuria and tender inguinal nodes. Which test is preferred to confirm the diagnosis?",
            ["Tzanck smear of the ulcer base",
             "HSV nucleic acid amplification test (PCR) of a lesion swab",
             "Serum HSV IgM",
             "Blood HSV PCR",
             "Direct immunofluorescence of a lesion scraping"],
            1,
            "CDC 2021: **HSV NAAT (PCR) จากแผล** ไวที่สุดและบอก type ได้ จึงเป็นวิธีที่เลือก\n\nTzanck smear เห็น multinucleated giant cells แต่ **ไม่ไวและไม่จำเพาะ** · **HSV IgM ไม่แนะนำ** เพราะไม่จำเพาะต่อ type และขึ้นได้ในการกลับเป็นซ้ำ · **PCR จากเลือด** ใช้เมื่อสงสัย disseminated infection เท่านั้น · direct immunofluorescence ไม่แนะนำเพราะไวต่ำ",
            "แผลเริม → swab ส่ง HSV PCR",
            [LEC_REF + " — การวินิจฉัยเริม", CDC + " — Genital herpes"],
            ["2.3.1(8)", "B4.2.2(5)", "3.1.10"]),
        mcq(6, "Tzanck smear interpretation",
            "A Tzanck smear from the base of a genital vesicle shows multinucleated giant cells. Which statement about this result is correct?",
            ["It confirms HSV-2 infection",
             "It excludes varicella-zoster virus infection",
             "It is more sensitive than PCR for recurrent lesions",
             "It indicates bacterial superinfection of the ulcer",
             "It cannot distinguish HSV from VZV and is less sensitive than PCR"],
            4,
            "Multinucleated giant cells เกิดจาก **ไวรัสในกลุ่ม herpes ทำให้ keratinocyte หลอมรวมกัน** — เห็นได้ทั้ง **HSV-1, HSV-2 และ VZV** จึงบอก type และแยก VZV ไม่ได้ และ **ไวต่ำกว่า PCR** มาก (โดยเฉพาะแผลเก่าหรือกลับเป็นซ้ำ)\n\nข้อดีที่อาจารย์ยกมาคือ **ราคาถูกมาก** เทียบกับ PCR · ไม่เกี่ยวกับการติดเชื้อแบคทีเรียซ้ำซ้อน",
            "Giant cells = กลุ่ม herpes แต่ไม่บอกว่าตัวไหน",
            [LEC_REF + " — Tzanck smear เทียบ PCR"],
            ["2.3.1(8)", "3.1.10"]),
    ],
})

# ---------------------------------------------------------------- 04
SECTIONS.append({
    "id": "id-gus-04",
    "title": "Genital herpes — ยาต้านไวรัสในคนปกติและผู้ภูมิคุ้มกันบกพร่อง",
    "summary": "ครั้งแรก acyclovir 400 mg tid 7–10 วัน กดการกำเริบ 400 mg bid และผู้ภูมิคุ้มกันบกพร่องใช้ขนาดใกล้กันแต่ให้นานขึ้นได้",
    "minutes": 8,
    "source": SRC,
    "nl": ["2.3.1(8)", "B4.2.2(5)", "2.3.1(19)", "B1.7.2", "2.3.1(9)"],
    "md": """### คนภูมิคุ้มกันปกติ (normal host)
| สถานการณ์ | ที่อาจารย์สอน | CDC 2021 |
|---|---|---|
| **ครั้งแรก (first episode)** — ทุกรายควรได้ยา | **Acyclovir 400 mg วันละ 3 ครั้ง 7–10 วัน** · หรือ 200 mg วันละ 5 ครั้ง (ยุ่งยาก) · famciclovir/valacyclovir วันละ 1–2 ครั้ง สะดวกกว่าแต่แพงกว่าหลายเท่า 7–10 วัน | Acyclovir 400 mg tid · **valacyclovir 1 g bid** · famciclovir 250 mg tid — ทั้งหมด **7–10 วัน** ขยายได้ถ้าแผลยังไม่หาย |
| **Suppressive** (กลับเป็นซ้ำบ่อย) | **Acyclovir 400 mg วันละ 2 ครั้ง** ต่อเนื่อง ระยะเวลาแล้วแต่ราย | Acyclovir 400 mg bid · valacyclovir 500 mg–1 g วันละครั้ง · famciclovir 250 mg bid |
| **Episodic** (รักษาเมื่อกำเริบ) | กลับเป็นใหม่หลังรักษาไม่นาน (เช่นใน 3 เดือน) → เพิ่มขนาดเป็น **800 mg วันละ 2–3 ครั้ง** | **Acyclovir 800 mg bid 5 วัน หรือ 800 mg tid 2 วัน** · valacyclovir 500 mg bid 3 วัน หรือ 1 g วันละครั้ง 5 วัน · famciclovir 1 g bid 1 วัน — เริ่มภายใน 1 วันหลังแผลขึ้นหรือช่วงอาการนำ |

- อาจารย์ชวนสังเกต: ขนาด **"กินวันละ 5 ครั้ง" ที่จำกันมักเป็นของ zoster** (acyclovir 800 mg วันละ 5 ครั้ง) ส่วนเริมอวัยวะเพศใช้ 400 mg tid เป็นหลัก

> **อัปเดตแนวทาง ·** อาจารย์ให้ acyclovir 200 mg วันละ 5 ครั้งเป็นทางเลือกของครั้งแรก — **CDC 2021 ระบุว่าได้ผลแต่ไม่แนะนำแล้วเพราะความถี่ในการกินยา** · ส่วนการกำเริบ CDC ใช้ **คอร์สสั้น** (acyclovir 800 mg bid 5 วัน หรือ 800 mg tid 2 วัน) ที่เริ่มให้เร็วที่สุด ไม่ใช่การ "เพิ่มขนาดแล้วให้นานขึ้น" (ตัวเลขระยะเวลาในบันทึกเสียงช่วงนี้ฟังไม่ชัด)

### ผู้ภูมิคุ้มกันบกพร่อง
อาจารย์: "immunocompromised" ไม่ได้มีแค่ HIV — ผู้ป่วยปลูกถ่ายอวัยวะหรือกินยากดภูมิก็สถานะเดียวกัน
| สถานการณ์ | ขนาดยา |
|---|---|
| **Episodic** | **Acyclovir 400 mg วันละ 3 ครั้ง 5–10 วัน** (ใกล้เคียง normal host) · **ขยายเกิน 10 วันได้** ถ้าแผลดีขึ้นไม่มาก · ทางเลือก valacyclovir 1 g bid หรือ famciclovir 500 mg bid |
| **Suppressive** | **Acyclovir 400–800 mg วันละ 2–3 ครั้ง** ต่อเนื่องเป็นเดือน · ทางเลือก valacyclovir 500 mg bid หรือ famciclovir 500 mg bid |
- ไม่ตอบสนองแม้ให้ยาถูกต้อง → สงสัย **acyclovir-resistant HSV** (พบในผู้กดภูมิ) → ส่งตรวจและปรึกษาผู้เชี่ยวชาญ (foscarnet หรือ cidofovir)

### ข้อควรรู้เพิ่ม
- หญิงตั้งครรภ์ที่มีประวัติเริมอวัยวะเพศ: CDC แนะนำ suppressive ตั้งแต่ **อายุครรภ์ 36 สัปดาห์** (acyclovir 400 mg tid หรือ valacyclovir 500 mg bid) เพื่อลดแผลขณะคลอด
- ยารักษาแค่ลดอาการและการแพร่เชื้อ **ไม่กำจัดไวรัสแฝง** → ให้คำปรึกษาเรื่องการแพร่เชื้อแม้ไม่มีแผล (asymptomatic shedding) และใช้ถุงยาง
""",
    "pearls": [
        "ครั้งแรก: acyclovir 400 mg tid 7–10 วัน (valacyclovir 1 g bid · famciclovir 250 mg tid)",
        "Suppressive: acyclovir 400 mg bid · กำเริบ: acyclovir 800 mg bid 5 วัน หรือ tid 2 วัน",
        "กินวันละ 5 ครั้งที่จำกัน = zoster 800 mg ไม่ใช่เริมอวัยวะเพศ",
        "Immunocompromised: episodic 400 mg tid 5–10 วัน ขยายได้ · suppressive 400–800 mg 2–3 ครั้ง/วัน",
    ],
    "items": [
        mcq(7, "First-episode genital herpes regimen",
            "A healthy 22-year-old woman has her first episode of genital herpes confirmed by HSV-2 PCR. Lesions began 2 days ago. Which regimen is most appropriate?",
            ["Acyclovir 800 mg orally five times daily for 7 days",
             "Valacyclovir 500 mg orally once daily for 3 days",
             "Acyclovir 400 mg orally three times daily for 7–10 days",
             "Topical acyclovir cream alone",
             "Famciclovir 1 g orally twice daily for 1 day"],
            2,
            "ครั้งแรกทุกรายควรได้ยากิน: **acyclovir 400 mg tid 7–10 วัน** (หรือ valacyclovir 1 g bid / famciclovir 250 mg tid 7–10 วัน) — ขยายได้ถ้าแผลยังไม่หาย\n\nAcyclovir 800 mg วันละ 5 ครั้งเป็นขนาดของ **herpes zoster** (จุดที่อาจารย์เตือนว่าคนมักสับสน) · valacyclovir 500 mg และ famciclovir 1 g bid 1 วันเป็นคอร์สสั้นสำหรับ **การกำเริบ** ไม่พอสำหรับครั้งแรก · ยาทาไม่มีประโยชน์ทางคลินิก",
            "ครั้งแรก = 400 mg tid 7–10 วัน",
            [LEC_REF + " — การรักษาเริมครั้งแรก", CDC + " — Genital herpes"],
            ["2.3.1(8)", "B1.7.2"]),
        mcq(8, "Suppressive therapy for recurrent genital herpes",
            "A 30-year-old man has 8 recurrences of genital herpes per year and wants to reduce their frequency and the risk of transmission to his partner. Which regimen is most appropriate?",
            ["Acyclovir 400 mg orally twice daily, taken continuously",
             "Acyclovir 400 mg orally three times daily for 7–10 days with each recurrence only",
             "Intravenous acyclovir 5 mg/kg every 8 hours once a month",
             "Valacyclovir 1 g orally twice daily for 21 days, then stop",
             "Famciclovir 1 g orally twice daily for 1 day each month"],
            0,
            "กลับเป็นซ้ำบ่อย → **suppressive therapy: acyclovir 400 mg bid ต่อเนื่อง** (หรือ valacyclovir 500 mg–1 g วันละครั้ง · famciclovir 250 mg bid) — ลดความถี่การกำเริบและลดการแพร่เชื้อสู่คู่นอน\n\nการรักษาเฉพาะตอนกำเริบไม่ลดความถี่ · ยาฉีดเป็นระยะไม่มีบทบาท · คอร์สจำกัดแล้วหยุดหรือกินเดือนละวันไม่ใช่การกดการกำเริบ",
            "กลับเป็นบ่อย → acyclovir 400 mg bid ต่อเนื่อง",
            [LEC_REF + " — suppressive therapy", CDC + " — Genital herpes"],
            ["2.3.1(8)", "B1.7.2"]),
        mcq(9, "Genital herpes in HIV infection",
            "A 35-year-old man with HIV (CD4 180 cells/mm³) has painful perianal herpetic ulcers. Which episodic regimen is recommended?",
            ["Acyclovir 200 mg orally five times daily for 3 days",
             "Acyclovir 800 mg orally three times daily for 2 days",
             "Intravenous acyclovir 10 mg/kg every 8 hours for 21 days",
             "Acyclovir 400 mg orally three times daily for 5–10 days, extended if lesions have not healed",
             "No antiviral until CD4 rises above 200 cells/mm³"],
            3,
            "ผู้ภูมิคุ้มกันบกพร่อง (HIV ปลูกถ่ายอวัยวะ ยากดภูมิ): **acyclovir 400 mg tid 5–10 วัน** — อาจารย์ชี้ว่าใกล้เคียง normal host แต่ **ขยายเกิน 10 วันได้** ถ้า follow up แล้วแผลยังดีขึ้นไม่มาก (CDC: valacyclovir 1 g bid หรือ famciclovir 500 mg bid ก็ได้)\n\nคอร์สสั้น 2–3 วันออกแบบสำหรับคนภูมิปกติ · IV acyclovir สงวนไว้สำหรับโรครุนแรงหรือแพร่กระจาย · ไม่มีเหตุผลให้รอ CD4",
            "HIV + เริม → 400 mg tid 5–10 วัน ขยายได้",
            [LEC_REF + " — เริมในผู้ภูมิคุ้มกันบกพร่อง", CDC + " — Genital herpes, persons with HIV"],
            ["2.3.1(8)", "2.3.1(9)", "B1.7.2"]),
    ],
})

# ---------------------------------------------------------------- 05
SECTIONS.append({
    "id": "id-gus-05",
    "title": "เริมรุนแรง แพร่กระจาย และภาวะแทรกซ้อนทางระบบประสาท",
    "summary": "Disseminated HSV ปอดอักเสบ meningitis หรือ encephalitis ต้องใช้ acyclovir ฉีด 5–10 mg/kg ทุก 8 ชั่วโมง และ encephalitis ให้นาน 14–21 วัน",
    "minutes": 8,
    "source": SRC,
    "nl": ["2.3.1(8)", "2.3.6(1)", "B3.2.2(2)", "2.3.6(5)", "3.1.7", "B3.3(2)", "B1.7.2"],
    "md": """### เมื่อไรเรียกว่ารุนแรง
- **Disseminated** — รอยโรคกระจายหลายตำแหน่ง รอบลำตัว ไม่ใช่แค่ที่อวัยวะเพศ
- **Systemic** — ต่อมน้ำเหลืองโต **ปอดอักเสบ** ตับอักเสบ หรือ **meningitis / encephalitis**
- มักพบในผู้ภูมิคุ้มกันบกพร่องและหญิงตั้งครรภ์

### การรักษา
| ภาวะ | ยาและระยะเวลา |
|---|---|
| **Disseminated / systemic** | **Acyclovir IV 5–10 mg/kg ทุก 8 ชั่วโมง** · อาจารย์: อย่างน้อย **10 วัน** และอาจนาน **2–3 สัปดาห์** ถ้ามี CNS · CDC: ให้ IV จนอาการดีขึ้นแล้วเปลี่ยนเป็นยากิน รวมเกิน 10 วัน |
| **HSV meningitis** (มักเป็น HSV-2) | IV จนดีขึ้น แล้วต่อ valacyclovir 1 g tid ให้ครบ **10–14 วัน** (CDC) |
| **HSV encephalitis** (ผู้ใหญ่ส่วนใหญ่เป็น HSV-1) | **Acyclovir IV 10 mg/kg ทุก 8 ชั่วโมง** · อาจารย์: อย่างน้อย 7–14 วัน |

> **อัปเดตแนวทาง ·** อาจารย์ให้ HSV encephalitis อย่างน้อย 7–14 วัน — **CDC 2021 ระบุว่า encephalitis ต้องใช้ IV acyclovir นานกว่า คือ 14–21 วัน** (สอดคล้องกับแนวทาง encephalitis ของ IDSA)

- ปรับขนาดตามไต · **ให้สารน้ำพอและหยดช้า** เพราะ acyclovir ตกผลึกในท่อไตได้

### Encephalitis ทางคลินิก
- อาจารย์: HSV-1 จากช่องปาก "ใกล้ CNS" มากกว่า จึงเป็นสาเหตุหลักของ encephalitis แต่ HSV-2 ก็เป็นได้
- **ไข้ ปวดศีรษะ ซึมลง สับสน ระดับความรู้สึกตัวเปลี่ยน ชัก เกร็ง** — รุนแรง ต้องใช้ยาฉีดแน่นอน
- เริ่ม acyclovir **ทันทีที่สงสัย** ไม่ต้องรอผล · ยืนยันด้วย **CSF HSV PCR** · MRI มักเห็นรอยโรคที่ temporal lobe

### แยก CSF แบบ aseptic จาก pyogenic
| | Bacterial (pyogenic) | Viral / aseptic (รวม HSV) |
|---|---|---|
| เพาะเชื้อ | ขึ้น | **ไม่ขึ้น** |
| เซลล์เด่น | neutrophil | lymphocyte |
| น้ำตาล | **ต่ำ** | **ปกติ** |
| โปรตีน | สูงมาก | ปกติหรือสูงเล็กน้อย |
- อาจารย์สรุปลักษณะ aseptic: **culture ไม่ขึ้น น้ำตาลไม่ต่ำ โปรตีนไม่สูงมาก** — ส่วน HSV encephalitis อาจพบเม็ดเลือดแดงใน CSF จากเนื้อสมองตายแบบเลือดออก
""",
    "pearls": [
        "Disseminated/systemic HSV → acyclovir IV 5–10 mg/kg q8h รวมเกิน 10 วัน",
        "HSV encephalitis → acyclovir IV 10 mg/kg q8h 14–21 วัน เริ่มทันทีที่สงสัย",
        "CSF aseptic: culture ลบ lymphocyte น้ำตาลปกติ โปรตีนไม่สูงมาก · ยืนยันด้วย CSF HSV PCR",
        "Acyclovir IV: ให้น้ำพอ หยดช้า ปรับตามไต",
    ],
    "items": [
        mcq(10, "Treatment of HSV encephalitis",
            "A 45-year-old woman has fever, headache, confusion and a focal seizure. MRI shows left temporal lobe hyperintensity, and CSF HSV-1 PCR is positive. Which treatment is most appropriate?",
            ["Oral valacyclovir 1 g three times daily for 7 days",
             "Intravenous acyclovir 10 mg/kg every 8 hours for 14–21 days",
             "Intravenous acyclovir 5 mg/kg every 8 hours for 3 days, then stop",
             "Intravenous ganciclovir 5 mg/kg every 12 hours",
             "Intravenous ceftriaxone and vancomycin alone"],
            1,
            "HSV encephalitis เป็นภาวะรุนแรง ต้องใช้ **acyclovir IV 10 mg/kg ทุก 8 ชั่วโมง นาน 14–21 วัน** (CDC 2021 และแนวทาง encephalitis) — อาจารย์พูดว่าอย่างน้อย 7–14 วัน แต่แนวทางปัจจุบันให้นานกว่า\n\nยากินไม่พอสำหรับ encephalitis · 3 วันสั้นเกินไปจนกลับเป็นซ้ำได้ · ganciclovir ใช้กับ CMV · ceftriaxone + vancomycin ครอบคลุมเฉพาะแบคทีเรีย (เริ่มคู่กันได้ก่อนได้ผล แต่ไม่ใช่การรักษา HSV)",
            "HSV encephalitis = IV acyclovir 10 mg/kg q8h 14–21 วัน",
            [LEC_REF + " — HSV encephalitis", CDC + " — Genital herpes, severe disease"],
            ["2.3.6(1)", "B3.2.2(2)", "2.3.1(8)"]),
        mcq(11, "CSF profile of viral meningitis",
            "A 27-year-old woman with recent genital herpes has headache, neck stiffness and photophobia. CSF shows WBC 150 cells/µL (90% lymphocytes), glucose 60 mg/dL (serum 95 mg/dL), protein 70 mg/dL and a negative Gram stain. Which diagnosis best fits?",
            ["Acute bacterial meningitis",
             "Tuberculous meningitis",
             "Cryptococcal meningitis",
             "Normal CSF",
             "Viral (aseptic) meningitis, such as HSV-2 meningitis"],
            4,
            "CSF แบบ **aseptic**: lymphocyte เด่น · **น้ำตาลปกติ** (CSF/serum ≈ 0.6) · โปรตีนสูงเล็กน้อย · Gram stain และ culture ลบ — เข้ากับ **viral meningitis** ซึ่ง HSV-2 เป็นสาเหตุสำคัญหลังเริมอวัยวะเพศ\n\nBacterial: neutrophil เด่น น้ำตาลต่ำ โปรตีนสูงมาก · TB และ cryptococcus: lymphocyte เด่นแต่ **น้ำตาลต่ำ** และโปรตีนสูงกว่า · CSF ปกติไม่ควรมีเม็ดเลือดขาว 150",
            "Lymphocyte + น้ำตาลปกติ = viral",
            [LEC_REF + " — CSF profile ของ aseptic meningitis"],
            ["2.3.6(5)", "3.1.7", "B3.3(2)"]),
    ],
})

# ---------------------------------------------------------------- 06
SECTIONS.append({
    "id": "id-gus-06",
    "title": "Granuloma inguinale (donovanosis) และ Lymphogranuloma venereum",
    "summary": "Donovanosis เป็นแผลแดงสดไม่เจ็บที่ไม่มีต่อมน้ำเหลืองโตจริง ส่วน LGV แผลเล็กแต่ต่อมน้ำเหลืองโตแตกหรือเป็น proctocolitis และทั้งคู่ใช้ยานานอย่างน้อย 3 สัปดาห์",
    "minutes": 9,
    "source": SRC,
    "nl": ["2.3.1(19)", "B10.2.2(1)", "2.1.48", "2.1.57", "B1.7.2", "3.1.9"],
    "md": """### Granuloma inguinale (donovanosis)
- เชื้อ **Klebsiella granulomatis** (ชื่อเดิม Calymmatobacterium granulomatis) — ในบันทึกเสียงมีช่วงหนึ่งที่พูดเป็น "Treponema pallidum" ซึ่งน่าจะพูดผิด เพราะช่วงหลังอาจารย์เรียกเชื้อได้ถูกต้อง
- แผลมักเดี่ยว **ค่อนข้างสะอาด** · **ขอบไม่ยกสูง** แบบแผลริมแข็งหรือริมอ่อน แต่ **ขรุขระแหว่งคล้ายรอยแทะ** · พื้นแผล **เงา** (อาจารย์บรรยาย)
- ลักษณะตามตำรา: แผล **ไม่เจ็บ** ค่อย ๆ ลาม **สีแดงสด (beefy red) หลอดเลือดมาก เลือดออกง่าย** · **ไม่มีต่อมน้ำเหลืองโตจริง** — ก้อนใต้ผิวที่ขาหนีบคือ granuloma (**pseudobubo**)
- วินิจฉัย: **Donovan bodies** = เชื้อที่อยู่ในไซโตพลาสซึมของ histiocyte/macrophage เห็นจาก **crush preparation หรือชิ้นเนื้อ** ย้อม Giemsa/Wright (อาจารย์เรียก "granular body")

| | ยา (CDC 2021) |
|---|---|
| **แนะนำ** | **Azithromycin 1 g สัปดาห์ละครั้ง** หรือ 500 mg วันละครั้ง |
| ทางเลือก | **Doxycycline 100 mg วันละ 2 ครั้ง** · erythromycin base 500 mg วันละ 4 ครั้ง · **TMP-SMX DS วันละ 2 ครั้ง** |
| ระยะเวลา | **อย่างน้อย 3 สัปดาห์ และจนแผลหายหมด** · กลับเป็นซ้ำได้ 6–18 เดือนหลังดูเหมือนหาย |

- อาจารย์: azithromycin 1 g **สัปดาห์ละครั้ง 3 สัปดาห์** (ต่างจาก chancroid ที่ 1 g ครั้งเดียว) · doxycycline วันละ 2 ครั้ง 3 สัปดาห์ · ยาสำรองอีกตัวที่พูดถึงฟังคล้าย "Bactrim" (TMP-SMX) แต่บันทึกไม่ชัด

> **อัปเดตแนวทาง ·** อาจารย์ให้ระยะเวลาเป็น 3 สัปดาห์คงที่ — **CDC 2021 ให้ "อย่างน้อย 3 สัปดาห์ และจนแผลหายหมด"** (azithromycin 1 g สัปดาห์ละครั้งหรือ 500 mg ทุกวัน) และให้ติดตามจนแผลหาย เพราะกลับเป็นซ้ำได้

### Lymphogranuloma venereum (LGV)
- เชื้อ **Chlamydia trachomatis serovar L1, L2, L3** (บุกรุกท่อน้ำเหลืองและต่อมน้ำเหลือง)
- ดำเนินโรคเป็นขั้น: ตุ่มหรือแผลเล็กไม่เจ็บ หายเร็วจนมักไม่ทันเห็น → **ต่อมน้ำเหลืองขาหนีบโต เจ็บ มักข้างเดียว** → รวมกันเป็นก้อน **แตกเป็นแผลและทางระบายหนอง (bubo)** · อาจเห็น **groove sign** (ต่อมเหนือและใต้ inguinal ligament)
- อาจารย์: สมัยก่อนพบบ่อย คนไข้ต่อมบวมเจ็บ ใส่กางเกงเดินขาเป๋ จึงถูกล้อว่าเป็น **"ฝีมะม่วง"**
- **Proctocolitis** (โดยเฉพาะ MSM ที่รับทางทวาร) — คล้าย IBD: **ปวดทวาร ถ่ายมีมูกเลือด ปวดเบ่ง (tenesmus) ไข้** และอาการทั่วร่างกาย · ถ้าเรื้อรังเกิดตีบหรือ fistula ได้
- วินิจฉัย: **C. trachomatis NAAT (PCR)** จากตำแหน่งที่มีอาการ (แผล ต่อมที่ดูด หรือทวาร) · Gram stain เห็น neutrophil · genotyping L serovar ยืนยันแต่หาได้ยาก · การตรวจแบบเดิมหรือชิ้นเนื้อมักเจอเชื้อยาก

| | ยา (CDC 2021) |
|---|---|
| **แนะนำ** | **Doxycycline 100 mg วันละ 2 ครั้ง 21 วัน** (ตรงกับที่อาจารย์สอน และอ้างแนวทางกระทรวงสาธารณสุข) |
| ทางเลือก | Azithromycin 1 g **สัปดาห์ละครั้ง 3 สัปดาห์** · erythromycin base 500 mg วันละ 4 ครั้ง 21 วัน |
| คู่นอน | สัมผัสภายใน **60 วัน** ก่อนอาการ → ตรวจ และให้ doxycycline 100 mg bid 7 วันแม้ไม่มีอาการ |

> **อัปเดตแนวทาง ·** ในบันทึกเสียงอาจารย์พูดถึง azithromycin 1 g เป็นทางเลือกของ LGV แต่ช่วงวิธีให้ยาฟังไม่ชัด — **CDC 2021 ให้ azithromycin 1 g สัปดาห์ละครั้งนาน 3 สัปดาห์** (ข้อมูลยังจำกัด พิจารณา test of cure ด้วย NAAT ที่ 4 สัปดาห์) ไม่ใช่ครั้งเดียวแบบ chlamydia ทั่วไป
""",
    "pearls": [
        "Donovanosis: K. granulomatis · แผลแดงสด ไม่เจ็บ เลือดออกง่าย · ไม่มี LN จริง (pseudobubo) · Donovan bodies",
        "Donovanosis: azithromycin 1 g สัปดาห์ละครั้ง ≥ 3 สัปดาห์จนแผลหาย",
        "LGV: C. trachomatis L1–L3 · แผลเล็กหายเร็ว → ต่อมน้ำเหลืองโตแตก (ฝีมะม่วง) · MSM: proctocolitis คล้าย IBD",
        "LGV: doxycycline 100 mg bid 21 วัน · คู่นอน 60 วัน",
    ],
    "items": [
        mcq(12, "Organism of donovanosis",
            "A 40-year-old man has a slowly enlarging, painless, beefy-red genital ulcer that bleeds easily on contact. There is no true inguinal lymphadenopathy. A crush preparation of tissue shows intracytoplasmic inclusions within macrophages on Giemsa stain. Which organism is responsible?",
            ["Treponema pallidum",
             "Haemophilus ducreyi",
             "Chlamydia trachomatis serovar L2",
             "Klebsiella granulomatis",
             "Herpes simplex virus type 2"],
            3,
            "แผล **ไม่เจ็บ แดงสด หลอดเลือดมาก เลือดออกง่าย** ค่อย ๆ ลาม และ **ไม่มีต่อมน้ำเหลืองโตจริง** + **Donovan bodies** (เชื้ออยู่ใน macrophage) = **granuloma inguinale (donovanosis)** จาก **Klebsiella granulomatis**\n\nT. pallidum ทำแผลแข็งพื้นสะอาด · H. ducreyi แผลนุ่มเจ็บมีหนอง · C. trachomatis L2 (LGV) แผลเล็กหายเร็วแต่ต่อมน้ำเหลืองโตเด่น · HSV-2 ตุ่มน้ำเป็นกลุ่มที่เจ็บ",
            "แผลแดงสดเลือดออกง่าย + Donovan bodies = K. granulomatis",
            [LEC_REF + " — Granuloma inguinale", CDC + " — Granuloma inguinale (donovanosis)"],
            ["2.3.1(19)", "2.1.48"]),
        mcq(13, "Treatment duration in donovanosis",
            "A patient is diagnosed with granuloma inguinale. Which treatment plan is recommended?",
            ["Azithromycin 1 g weekly (or 500 mg daily) for at least 3 weeks and until all lesions have healed",
             "Azithromycin 1 g orally as a single dose",
             "Benzathine penicillin G 2.4 million units IM once",
             "Ceftriaxone 250 mg IM as a single dose",
             "Oral acyclovir 400 mg three times daily for 10 days"],
            0,
            "Donovanosis ต้องใช้ยานาน: **azithromycin 1 g สัปดาห์ละครั้ง (หรือ 500 mg ทุกวัน) อย่างน้อย 3 สัปดาห์ และจนแผลหายหมด** · ทางเลือก doxycycline 100 mg bid, erythromycin base หรือ TMP-SMX DS bid ระยะเวลาเท่ากัน · กลับเป็นซ้ำได้ 6–18 เดือน\n\nอาจารย์ชี้ความต่าง: chancroid ใช้ azithromycin 1 g **ครั้งเดียว** แต่ donovanosis ใช้ 1 g **สัปดาห์ละครั้งหลายสัปดาห์** · penicillin และ acyclovir ไม่ได้รักษาโรคนี้",
            "Donovanosis = ยานาน ≥ 3 สัปดาห์จนแผลหาย",
            [LEC_REF + " — การรักษา granuloma inguinale", CDC + " — Granuloma inguinale (donovanosis)"],
            ["2.3.1(19)", "B1.7.2"]),
        mcq(14, "LGV proctocolitis treatment",
            "A 31-year-old man who has receptive anal sex with men presents with rectal pain, tenesmus, mucopurulent bloody discharge and fever for 2 weeks. Colonoscopy shows proctitis resembling inflammatory bowel disease. Rectal swab NAAT is positive for Chlamydia trachomatis. What is the most appropriate treatment?",
            ["Azithromycin 1 g orally as a single dose",
             "Doxycycline 100 mg orally twice daily for 7 days",
             "Doxycycline 100 mg orally twice daily for 21 days",
             "Ceftriaxone 500 mg IM as a single dose",
             "Mesalamine and oral prednisolone"],
            2,
            "Proctocolitis รุนแรง (ปวดเบ่ง มูกเลือด ไข้) ใน MSM + rectal C. trachomatis NAAT บวก → สงสัย **LGV** (serovar L1–L3) แม้ยังไม่ได้ genotype → รักษาด้วย **doxycycline 100 mg bid 21 วัน**\n\nDoxycycline 7 วันหรือ azithromycin ครั้งเดียวเป็นสูตรของ chlamydia ทั่วไป (non-LGV) ไม่พอสำหรับ LGV · ceftriaxone รักษา gonorrhea · ให้ยา IBD จะพลาดโรคติดเชื้อที่รักษาหายได้",
            "LGV = doxycycline 21 วัน",
            [LEC_REF + " — การรักษา LGV", CDC + " — Lymphogranuloma venereum"],
            ["2.3.1(19)", "B1.7.2"]),
    ],
})
