# -*- coding: utf-8 -*-
# Part B: sections 07-12 (syphilis)
from gus_a import SECTIONS, SRC, LEC_REF, CDC, mcq

THAI = "กรมควบคุมโรค — คู่มือการตรวจวินิจฉัยและติดตามการรักษาโรคซิฟิลิสทางห้องปฏิบัติการ (2564)"

FIG_COURSE = (
    '<svg viewBox="0 0 420 328" role="img" aria-label="ธรรมชาติของซิฟิลิส: ระยะฟักตัว primary secondary early latent late latent tertiary และ neurosyphilis ที่เกิดได้ทุกระยะ" xmlns="http://www.w3.org/2000/svg">'
    '<rect x="8" y="6" width="404" height="38" rx="8" class="sk"/>'
    '<text x="210" y="22" class="sm b mid">สัมผัสเชื้อ → ระยะฟักตัว 10–90 วัน</text>'
    '<text x="210" y="37" class="xs mid mu">ยังไม่มีอาการ · serology อาจยังลบ</text>'
    '<line x1="210" y1="44" x2="210" y2="56" class="ln" marker-end="url(#ah)"/>'
    '<rect x="8" y="58" width="404" height="40" rx="8" class="ok"/>'
    '<text x="210" y="74" class="sm b mid">Primary — chancre</text>'
    '<text x="210" y="90" class="xs mid">แผลเดียว ไม่เจ็บ ขอบแข็ง พื้นสะอาด · หายเองใน 3–6 สัปดาห์</text>'
    '<line x1="210" y1="98" x2="210" y2="114" class="ln" marker-end="url(#ah)"/>'
    '<text x="218" y="110" class="xs mu">4–10 สัปดาห์</text>'
    '<rect x="8" y="116" width="404" height="40" rx="8" class="ok"/>'
    '<text x="210" y="132" class="sm b mid">Secondary — เชื้อกระจายทางเลือด</text>'
    '<text x="210" y="148" class="xs mid">ผื่นรวมฝ่ามือฝ่าเท้า · ต่อมน้ำเหลืองโต · mucous patch · หายเอง</text>'
    '<line x1="110" y1="156" x2="110" y2="172" class="ln" marker-end="url(#ah)"/>'
    '<line x1="310" y1="156" x2="310" y2="172" class="ln" marker-end="url(#ah)"/>'
    '<rect x="8" y="174" width="198" height="44" rx="8" class="ok"/>'
    '<text x="107" y="192" class="sm b mid">Early latent</text>'
    '<text x="107" y="209" class="xs mid">ติดเชื้อไม่เกิน 1 ปี · ไม่มีอาการ</text>'
    '<rect x="214" y="174" width="198" height="44" rx="8" class="ms"/>'
    '<text x="313" y="192" class="sm b mid">Late latent</text>'
    '<text x="313" y="209" class="xs mid">เกิน 1 ปี หรือไม่ทราบระยะ</text>'
    '<line x1="313" y1="218" x2="313" y2="234" class="lbad" marker-end="url(#ah-bad)"/>'
    '<text x="305" y="230" class="xs end tbad">หลายปี</text>'
    '<rect x="8" y="236" width="404" height="40" rx="8" class="bad"/>'
    '<text x="210" y="252" class="sm b mid">Tertiary — 10 ถึงกว่า 30 ปี</text>'
    '<text x="210" y="268" class="xs mid">gumma · aortitis และ AR · general paresis · tabes dorsalis</text>'
    '<rect x="8" y="284" width="404" height="40" rx="8" class="wa"/>'
    '<text x="210" y="300" class="sm b mid">Neurosyphilis · ocular · otic — เกิดได้ทุกระยะ</text>'
    '<text x="210" y="316" class="xs mid">ไม่ใช้ benzathine → aqueous penicillin G IV 10–14 วัน</text>'
    '</svg>'
)

FIG_ALGO = (
    '<svg viewBox="0 0 420 300" role="img" aria-label="เปรียบเทียบลำดับการตรวจซิฟิลิสแบบดั้งเดิมที่เริ่มด้วย RPR กับแบบย้อนทางที่เริ่มด้วย treponemal test" xmlns="http://www.w3.org/2000/svg">'
    '<text x="106" y="16" class="sm b mid tac">แบบดั้งเดิม (traditional)</text>'
    '<text x="314" y="16" class="sm b mid tac">แบบย้อนทาง (reverse)</text>'
    '<rect x="6" y="26" width="200" height="40" rx="8" class="sk"/>'
    '<text x="106" y="43" class="xs b mid">1. RPR/VDRL (non-treponemal)</text>'
    '<text x="106" y="58" class="xs mid mu">ลบ → จบ (ระวังระยะแรกมาก)</text>'
    '<line x1="106" y1="66" x2="106" y2="82" class="ln" marker-end="url(#ah)"/>'
    '<text x="112" y="78" class="xs mu">บวก + ทำ titre</text>'
    '<rect x="6" y="84" width="200" height="40" rx="8" class="sk"/>'
    '<text x="106" y="101" class="xs b mid">2. TPHA/TPPA (treponemal)</text>'
    '<text x="106" y="116" class="xs mid mu">ยืนยันว่าบวกจริง</text>'
    '<line x1="80" y1="124" x2="56" y2="140" class="ln" marker-end="url(#ah)"/>'
    '<line x1="132" y1="124" x2="156" y2="140" class="ln" marker-end="url(#ah)"/>'
    '<rect x="6" y="142" width="96" height="56" rx="8" class="ok"/>'
    '<text x="54" y="160" class="xs b mid">TT บวก</text>'
    '<text x="54" y="175" class="xs mid">ซิฟิลิส</text>'
    '<text x="54" y="190" class="xs mid">(ปัจจุบันหรือเคย)</text>'
    '<rect x="110" y="142" width="96" height="56" rx="8" class="bad"/>'
    '<text x="158" y="160" class="xs b mid">TT ลบ</text>'
    '<text x="158" y="175" class="xs mid">ผลบวกลวง</text>'
    '<text x="158" y="190" class="xs mid">ของ RPR (BFP)</text>'
    '<rect x="6" y="210" width="200" height="84" rx="8" class="bx"/>'
    '<text x="106" y="228" class="xs b mid tbad">จุดอ่อน</text>'
    '<text x="106" y="244" class="xs mid">late latent ราว 25–30%</text>'
    '<text x="106" y="259" class="xs mid">RPR ลดลงจนลบเอง → หลุด</text>'
    '<text x="106" y="274" class="xs mid">คู่มือไทย: ห้ามใช้แบบนี้</text>'
    '<text x="106" y="288" class="xs mid">คัดกรองหญิงตั้งครรภ์</text>'
    '<rect x="214" y="26" width="200" height="40" rx="8" class="sk"/>'
    '<text x="314" y="43" class="xs b mid">1. EIA/CLIA/RDT (treponemal)</text>'
    '<text x="314" y="58" class="xs mid mu">ลบ → จบ</text>'
    '<line x1="314" y1="66" x2="314" y2="82" class="ln" marker-end="url(#ah)"/>'
    '<text x="320" y="78" class="xs mu">บวก</text>'
    '<rect x="214" y="84" width="200" height="40" rx="8" class="sk"/>'
    '<text x="314" y="101" class="xs b mid">2. RPR พร้อม titre (NTT)</text>'
    '<text x="314" y="116" class="xs mid mu">บอกความ active และใช้ติดตาม</text>'
    '<line x1="288" y1="124" x2="264" y2="140" class="ln" marker-end="url(#ah)"/>'
    '<line x1="340" y1="124" x2="364" y2="140" class="ln" marker-end="url(#ah)"/>'
    '<rect x="214" y="142" width="96" height="56" rx="8" class="ok"/>'
    '<text x="262" y="160" class="xs b mid">RPR บวก</text>'
    '<text x="262" y="175" class="xs mid">ซิฟิลิส</text>'
    '<text x="262" y="190" class="xs mid">ประเมินระยะ</text>'
    '<rect x="318" y="142" width="96" height="56" rx="8" class="wa"/>'
    '<text x="366" y="160" class="xs b mid">RPR ลบ</text>'
    '<text x="366" y="175" class="xs mid">ตรวจ TT ตัวที่ 2</text>'
    '<text x="366" y="190" class="xs mid">(TPPA หรือ TPHA)</text>'
    '<line x1="350" y1="198" x2="270" y2="216" class="ln" marker-end="url(#ah)"/>'
    '<line x1="372" y1="198" x2="372" y2="216" class="ln" marker-end="url(#ah)"/>'
    '<rect x="214" y="218" width="110" height="76" rx="8" class="ms"/>'
    '<text x="269" y="236" class="xs b mid">TPPA บวก</text>'
    '<text x="269" y="251" class="xs mid">เคยติดเชื้อ</text>'
    '<text x="269" y="266" class="xs mid">เคยรักษา → จบ</text>'
    '<text x="269" y="281" class="xs mid">ไม่เคย → รักษา</text>'
    '<rect x="330" y="218" width="84" height="76" rx="8" class="bad"/>'
    '<text x="372" y="236" class="xs b mid">TPPA ลบ</text>'
    '<text x="372" y="251" class="xs mid">TT ตัวแรก</text>'
    '<text x="372" y="266" class="xs mid">น่าจะบวกลวง</text>'
    '</svg>'
)

# ---------------------------------------------------------------- 07
SECTIONS.append({
    "id": "id-gus-07",
    "title": "Syphilis — เชื้อ การแบ่งระยะ และธรรมชาติของโรค",
    "summary": "T. pallidum แบ่งเป็น early (primary secondary early latent) late และ neurosyphilis ที่เกิดได้ทุกระยะ ซึ่งระยะเป็นตัวกำหนดระยะเวลารักษา",
    "minutes": 8,
    "source": SRC,
    "nl": ["2.3.1(19)", "B10.2.2(1)", "B1.5.2(1)"],
    "md": """### เชื้อ
- **Treponema pallidum** — spirochete รูปเกลียว
- อาจารย์ถามว่าเคยดู **darkfield microscope** ไหม — เห็นเชื้อเป็นเกลียวสว่างบนพื้นมืด แต่ **ทำยาก ต้องใช้ความชำนาญ** จึงไม่นิยม ปัจจุบันวินิจฉัยด้วย **serology** เป็นหลัก

### การแบ่งระยะแบบที่อาจารย์ให้จำ — 3 กลุ่ม
| กลุ่ม | ประกอบด้วย | ความหมายต่อการรักษา |
|---|---|---|
| **Early syphilis** | **primary · secondary · early latent** | benzathine penicillin G **ครั้งเดียว** |
| **Late syphilis** | **late latent · ไม่ทราบระยะ · tertiary** (gumma, cardiovascular) | benzathine penicillin G **สัปดาห์ละครั้ง × 3** |
| **Neurosyphilis** (รวม ocular และ otic) | เกิดได้ **ทุกระยะ** | aqueous penicillin G ทางหลอดเลือดดำ |

[[fig:course]]

### ช่วงเวลาของแต่ละระยะ
| ระยะ | เวลา | ที่อาจารย์พูด |
|---|---|---|
| ระยะฟักตัว | 10–90 วัน (เฉลี่ยราว 3 สัปดาห์) | **นานได้ถึง 3 เดือน** |
| Primary | chancre หายเองใน 3–6 สัปดาห์ | แผลหายได้เองใน 3–6 สัปดาห์ |
| Secondary | ราว **4–10 สัปดาห์** หลังแผล | 4–10 สัปดาห์ (บางช่วงพูด 4–12) · หายเองเงียบ ๆ แล้วเข้า latent |
| Early latent | ติดเชื้อ **ไม่เกิน 1 ปี** | อยู่เงียบ ๆ พบจากการคัดกรอง RPR |
| Late latent | เกิน 1 ปี หรือไม่ทราบ | "เกินปีไปแล้วก็จะไป late" |
| Tertiary | หลายปีถึง **10–30 ปีขึ้นไป** | ราว 10–15 ปี |

- เกณฑ์ **early latent** ของ CDC และคู่มือไทยคือ **ภายใน 1 ปี** ต้องมีหลักฐาน เช่น เคยตรวจลบภายใน 1 ปี · titre เพิ่มขึ้น 4 เท่า · เคยมีอาการ primary/secondary ชัดเจนใน 1 ปี · หรือคู่นอนเป็น early syphilis — **WHO ใช้ 2 ปี**
- ซักประวัติแล้วบอกไม่ได้ว่าเคยมีแผลหรือผื่นเมื่อไร → **ถือเป็นไม่ทราบระยะ รักษาแบบ late latent** (อาจารย์เน้น — เพื่อประโยชน์ของผู้ป่วย)

> **อัปเดตแนวทาง ·** อาจารย์ประมาณว่าเข้าสู่ tertiary ราว 10–15 ปี — **CDC 2021 ระบุอาการทางระบบประสาทระยะท้ายเกิดได้ตั้งแต่ 10 ถึงกว่า 30 ปีหลังติดเชื้อ** ส่วนอาการระบบประสาทระยะแรก (รวม ocular และ otic) มักเกิดในไม่กี่เดือนถึงไม่กี่ปีแรก
""",
    "pearls": [
        "Early = primary + secondary + early latent (≤ 1 ปี) → BPG ครั้งเดียว",
        "Late = late latent + ไม่ทราบระยะ + tertiary → BPG สัปดาห์ละครั้ง × 3",
        "Neurosyphilis/ocular/otic เกิดได้ทุกระยะ → penicillin G IV",
        "ไม่ทราบระยะ → รักษาแบบ late latent เสมอ",
    ],
    "figs": {"course": {
        "title": "ธรรมชาติของซิฟิลิสที่ไม่ได้รักษา",
        "cap": "กล่องสีเขียว = **early syphilis** (รักษาด้วย benzathine penicillin G ครั้งเดียว) · สีเหลือง = **late latent หรือไม่ทราบระยะ** (สัปดาห์ละครั้ง × 3) · tertiary เป็นความเสียหายที่ย้อนคืนไม่ได้ · แถบล่าง: **neurosyphilis ocular และ otic เกิดได้ทุกระยะ** และใช้ยาฉีดเข้าหลอดเลือดดำ (ช่วงเวลาเป็นค่าประมาณตาม CDC 2021 และคู่มือไทย)",
        "svg": FIG_COURSE}},
    "items": [
        mcq(15, "Staging latent syphilis",
            "A 29-year-old woman is asymptomatic. Routine testing shows reactive RPR 1:32 and reactive TPPA. A syphilis test 8 months ago was nonreactive, and examination shows no mucocutaneous lesions or neurologic signs. What is the stage?",
            ["Primary syphilis",
             "Secondary syphilis",
             "Late latent syphilis",
             "Tertiary syphilis",
             "Early latent syphilis"],
            4,
            "ไม่มีอาการ + serology บวก = **latent** · มีหลักฐานว่า **ติดเชื้อภายใน 1 ปี** (เคยตรวจลบเมื่อ 8 เดือนก่อน = seroconversion) → **early latent** → รักษาด้วย **benzathine penicillin G 2.4 MU IM ครั้งเดียว**\n\nPrimary/secondary ต้องมีแผลหรือผื่น · late latent คือเกิน 1 ปีหรือไม่มีหลักฐานระยะเวลา · tertiary ต้องมี gumma, cardiovascular หรืออาการระบบประสาทระยะท้าย",
            "ไม่มีอาการ + เคยตรวจลบใน 1 ปี = early latent",
            [LEC_REF + " — การแบ่งระยะซิฟิลิส", CDC + " — Latent syphilis"],
            ["2.3.1(19)", "3.3.16"]),
        mcq(16, "Latent syphilis of unknown duration",
            "A 52-year-old man has reactive RPR 1:8 and reactive TPHA on a pre-employment check. He has never been tested before and cannot recall any genital ulcer or rash. Neurologic and eye examinations are normal. What is the most appropriate management?",
            ["Treat as early latent syphilis with benzathine penicillin G 2.4 million units IM once",
             "Treat as latent syphilis of unknown duration with benzathine penicillin G 2.4 million units IM weekly for 3 weeks",
             "No treatment; the result reflects a past infection",
             "Aqueous penicillin G 18–24 million units IV daily for 14 days",
             "Doxycycline 100 mg orally twice daily for 14 days"],
            1,
            "อาจารย์เน้น: ถามประวัติแผลหรือผื่นแล้ว **จำไม่ได้** → **ถือเป็นไม่ทราบระยะ รักษาแบบ late latent** เพื่อประโยชน์ของผู้ป่วย = **BPG 2.4 MU IM สัปดาห์ละครั้ง × 3 (รวม 7.2 MU)**\n\nการให้ครั้งเดียวเสี่ยงรักษาไม่พอถ้าติดมานาน · RPR บวกร่วมกับ TT บวกโดยไม่เคยรักษาต้องรักษา · penicillin G IV สงวนไว้สำหรับ neurosyphilis/ocular/otic · doxycycline (ถ้าแพ้ penicillin) ใน late latent ต้องให้ 28 วัน",
            "จำไม่ได้ว่าติดเมื่อไร = late latent → BPG × 3",
            [LEC_REF + " — late latent หรือไม่ทราบระยะ", CDC + " — Latent syphilis"],
            ["2.3.1(19)", "B1.7.2"]),
    ],
})

# ---------------------------------------------------------------- 08
SECTIONS.append({
    "id": "id-gus-08",
    "title": "Syphilis — อาการ primary, secondary, latent และ tertiary",
    "summary": "Chancre ไม่เจ็บพื้นสะอาด ผื่น secondary ที่ฝ่ามือฝ่าเท้าเป็นตัวแยกจากผื่นอื่น ส่วน tertiary เป็นความเสียหายถาวร",
    "minutes": 9,
    "source": SRC,
    "nl": ["2.3.1(19)", "B10.2.2(1)", "2.1.48", "2.1.57", "2.3.9-3(2)"],
    "md": """### Primary — chancre
- ตำแหน่งที่เชื้อเข้า: ส่วนใหญ่ **อวัยวะเพศ** แต่พบที่ **ปาก ลิ้น ทวารหนัก** ได้
- **เส้นผ่านศูนย์กลาง 1–2 ซม. · แผลเดียว · ขอบนูนแข็ง · พื้นสะอาด · ไม่เจ็บ** (clean base, indurated, painless) · ต่อมน้ำเหลืองใกล้เคียงโต แข็ง ไม่เจ็บ
- ใน **MSM** chancre มักอยู่ **รอบทวารหรือในทวารหนัก** จึงไม่ทันสังเกต · ในผู้หญิงแผลที่ช่องคลอดหรือปากมดลูกก็มักไม่เห็น
- แผล **หายเองใน 3–6 สัปดาห์** แม้ไม่รักษา — แผลหายไม่ได้แปลว่าโรคหาย

### Secondary — ผื่นทั่วตัว
- **Macule/papule สีชมพูถึงแดง** ขนาดเล็ก (มม. ถึงราว 1 ซม.) กระจายตามลำตัว · นานไปเปลี่ยนเป็น **สีน้ำตาลและลอกเป็นขุย** · ไม่คัน
- **ดูฝ่ามือฝ่าเท้าก่อนเลย** (อาจารย์เน้น) — ผื่นตามตัวแยกไม่ออกจาก **ผื่นแพ้ยา ยุงกัด rubella** · ถ้าฝ่ามือฝ่าเท้ามี papule หรือรอยลอกเป็นขุยหลังเป็นมาหลายสัปดาห์ → นึกถึง secondary syphilis
- **ผมร่วงเป็นหย่อม (patchy, moth-eaten alopecia)** · รอยโรคในปากและลิ้น (mucous patch) · **condyloma lata** ที่รอบทวารหรืออวัยวะเพศ (ต่างจากหูดหงอนไก่)
- **ต่อมน้ำเหลืองโตทั่วตัว กดไม่เจ็บ** — คอ ใบหน้า หน้าและหลังหู · บางรายเห็นต่อมในช่องท้องจาก CT แต่อาจารย์เตือนว่าเป็นภาพไม่ปกติ เจอไม่บ่อย อย่าเพิ่งไปทำ CT
- บางรายเชื้อ **เข้า CNS ตั้งแต่ระยะนี้** → uveitis, cranial nerve palsy (ดู section neurosyphilis)
- รอยโรคทั้งหมด **หายเองได้** แล้วเข้าสู่ latent

### Latent
- **ไม่มีอาการ** มีแต่ serology บวก · พบจากการคัดกรอง (ฝากครรภ์ บริจาคเลือด ตรวจสุขภาพ)

### Tertiary (late)
- **Gumma** — ก้อน granuloma ทำลายผิว กระดูก อวัยวะ
- **Cardiovascular** — aortitis ของ ascending aorta → **aortic regurgitation** และ aneurysm (จาก endarteritis ของ vasa vasorum)
- **Late neurosyphilis** — general paresis (สมองเสื่อม บุคลิกเปลี่ยน) · tabes dorsalis (เสียการรับรู้ตำแหน่ง ปวดแปลบ) · Argyll Robertson pupil
- อาจารย์ (สไลด์สุดท้าย): **tertiary รักษาได้แค่หยุดโรค** — ความเสียหายที่เกิดแล้ว เช่น peripheral nerve palsy หรือการมองเห็นที่เสียไป **ย้อนคืนไม่ได้**
""",
    "pearls": [
        "Chancre: 1–2 ซม. แผลเดียว ขอบแข็ง พื้นสะอาด ไม่เจ็บ · หายเอง 3–6 สัปดาห์",
        "ผื่นแยกไม่ออก → ดูฝ่ามือฝ่าเท้า (อาจารย์เน้น)",
        "Secondary: alopecia เป็นหย่อม · mucous patch · condyloma lata · LN โตทั่วตัวไม่เจ็บ",
        "Tertiary: gumma · aortitis/AR · general paresis · tabes — ความเสียหายถาวร",
    ],
    "items": [
        mcq(17, "Distinguishing secondary syphilis rash",
            "A 24-year-old man has a 3-week non-pruritic rash on the trunk that began 6 weeks after a painless penile sore healed. Which additional finding most strongly favors secondary syphilis over a drug eruption?",
            ["Scaly copper-colored papules on the palms and soles with generalized non-tender lymphadenopathy",
             "Urticarial wheals that each resolve within 24 hours",
             "Target lesions with oral erosions shortly after starting a new drug",
             "Painful vesicles in a single dermatomal distribution",
             "Erythema limited to sun-exposed areas"],
            0,
            "อาจารย์สอนว่า **ผื่นตามตัวแยกจากผื่นแพ้ยาหรือยุงกัดไม่ได้ → ให้ดูฝ่ามือฝ่าเท้า** · papule สีแดงน้ำตาลที่ฝ่ามือฝ่าเท้าที่เริ่มลอกเป็นขุย + **ต่อมน้ำเหลืองโตทั่วตัวกดไม่เจ็บ** + ประวัติแผลไม่เจ็บที่หายไปเมื่อ 4–10 สัปดาห์ก่อน = **secondary syphilis** (เชื้อกระจายทางเลือดจึงขึ้นได้ทุกตำแหน่ง)\n\nWheals ที่หายใน 24 ชม. = urticaria · target lesion + mucosa หลังยาใหม่ = EM/SJS · ตุ่มน้ำตาม dermatome = zoster · ผื่นเฉพาะที่โดนแดด = photosensitivity",
            "ผื่นแยกไม่ออก → ดูฝ่ามือฝ่าเท้า",
            [LEC_REF + " — Secondary syphilis"],
            ["2.3.1(19)", "2.1.57"]),
        mcq(18, "Cardiovascular syphilis",
            "A 68-year-old man has a diastolic decrescendo murmur. Imaging shows dilatation of the ascending aorta with linear calcification, and his treponemal test is reactive. What is the underlying mechanism?",
            ["Cystic medial degeneration caused by hypertension",
             "Atherosclerosis predominantly affecting the infrarenal aorta",
             "Immune-complex vasculitis of the coronary arteries",
             "Obliterative endarteritis of the vasa vasorum of the ascending aorta",
             "Rheumatic involvement of the mitral valve"],
            3,
            "**Cardiovascular syphilis (tertiary)** — T. pallidum ทำให้ **endarteritis obliterans ของ vasa vasorum** ของ ascending aorta → ผนังชั้นกลางขาดเลือดและเป็นแผลเป็น → aorta ส่วนต้นโป่ง (aneurysm) และ **aortic regurgitation** (เสียง diastolic decrescendo) · เกิดหลายปีถึงหลายสิบปีหลังติดเชื้อ ความเสียหายแก้คืนไม่ได้แม้รักษาเชื้อ\n\nCystic medial degeneration พบใน Marfan/ความดัน · atherosclerosis มักที่ aorta ส่วนท้อง · ไม่ใช่ vasculitis ของ coronary หรือโรคหัวใจรูมาติก",
            "Syphilitic aortitis = ascending aorta + AR",
            [LEC_REF + " — tertiary syphilis"],
            ["2.3.1(19)", "2.3.9-3(2)"]),
    ],
})

# ---------------------------------------------------------------- 09
SECTIONS.append({
    "id": "id-gus-09",
    "title": "Syphilis serology — non-treponemal กับ treponemal และลำดับการตรวจ",
    "summary": "RPR/VDRL ขึ้นลงตามโรคใช้คัดกรองและติดตาม ส่วน TPHA/TPPA/EIA บวกตลอดชีวิตใช้ยืนยัน และต้องแปลผลร่วมกันเสมอ",
    "minutes": 11,
    "source": SRC,
    "nl": ["3.3.16", "B10.3(8)", "B1.5.1(8)", "2.3.1(19)", "B1.4.13"],
    "md": """### ตรวจหาเชื้อโดยตรง (direct)
- **Darkfield** จากแผล — เห็นเกลียว แต่ต้องใช้ความชำนาญ
- **PCR / NAAT** จากแผล — ไวและสะดวกกว่า (ยังไม่แพร่หลายทุกที่)

### ตรวจทางอ้อม (serology) — สองชนิด
| | **Non-treponemal (NTT)** | **Treponemal (TT)** |
|---|---|---|
| ตัวอย่าง | **VDRL, RPR** | **TPHA, TPPA, FTA-ABS, EIA/CLIA, rapid test** |
| วัดอะไร | antibody ต่อ **lipoidal substance (cardiolipin)** ที่หลุดจากเซลล์ผู้ป่วยที่ถูกทำลาย — **ไม่ได้วัดตัวเชื้อ** | antibody ต่อ **antigen ของตัวเชื้อ** |
| ผลตามเวลา | **ขึ้นลงตาม activity ของโรค** · ลดลงหลังรักษา | **บวกตลอดชีวิต** (ราว 75–85%) แม้รักษาหายแล้ว |
| ใช้ทำอะไร | คัดกรอง + **ติดตามผลการรักษาด้วย titre** | **ยืนยันว่าเคยติดเชื้อ** — ไม่บอกว่ายัง active |
| ผลบวกลวง | **SLE, autoimmune, rheumatoid, malaria, leptospirosis** (อาจารย์ยกตัวอย่าง — **ออกสอบ**) · ตั้งครรภ์ HIV ฉีดยาเสพติด อายุมาก วัคซีน | น้อย (yaws, pinta, Lyme) |

### แปลผลร่วมกัน (อาจารย์ไล่ให้ทั้งห้อง)
| NTT (RPR/VDRL) | TT (TPHA/TPPA) | แปลผล |
|---|---|---|
| บวก | บวก | **ซิฟิลิส** — ยังไม่รักษาหรือเพิ่งรักษา (ดู titre และประวัติ) |
| บวก | ลบ | **ผลบวกลวงของ NTT (biologic false positive)** · หรือระยะแรกมากที่ TT ยังไม่ขึ้น |
| ลบ | บวก | **เคยติดและรักษาแล้ว** · primary ระยะแรก · late latent ที่ RPR ลดลงเอง · prozone |
| ลบ | ลบ | ไม่ติดเชื้อ หรืออยู่ในระยะฟักตัว → ถ้าเพิ่งเสี่ยง **เจาะซ้ำ 2–4 สัปดาห์** |

- **ทำไมระยะแรกผลลบได้** — TT ชนิด IgM ตรวจพบราวสัปดาห์ที่ 2 หลังติดเชื้อ ส่วน RPR/VDRL ราว 3–6 สัปดาห์ (คู่มือไทย) · chancre จึงขึ้นก่อน serology บวก
- **Prozone** — secondary syphilis ราว 1–2% มี antibody มากเกินจน RPR ไม่จับกลุ่ม ให้ผลลบปลอม → ขอให้ **เจือจาง serum (เช่น 1:16)** ถ้าอาการเข้าได้
- **Serofast** — รักษาถูกต้องแล้ว titre ลดลงแต่ค้างที่ระดับต่ำคงที่ ไม่ต้องรักษาซ้ำถ้าไม่มีอาการและ titre ไม่เพิ่ม
- อาจารย์: ส่ง VDRL เพราะอยากรู้ว่า **โรคยัง active และยังไม่ได้รักษาหรือไม่** — ลบก็จบ บวกต้องดู titre และยืนยันด้วย TT ว่าบวกจริงหรือบวกลวง ก่อนตัดสินใจรักษา

> **ข้อควรระวัง ·** ในบันทึกอาจารย์อธิบาย TT ว่าเป็น "rapid test ที่ดู IgM กับ IgG" — ที่ถูกคือ TPHA/TPPA/FTA-ABS/EIA ตรวจ **antibody ต่อตัวเชื้อ** (ส่วนใหญ่วัดรวม IgM และ IgG) และ rapid test ส่วนใหญ่ก็เป็น TT ชนิดหนึ่ง จุดสำคัญที่ถูกต้องคือ **TT บวกตลอดชีวิต NTT ขึ้นลงตามโรค**

> **อัปเดตแนวทาง ·** อาจารย์บอกว่าปัจจุบัน "เป็น RPR หมดแล้ว เขียน VDRL ไปก็ส่ง RPR ให้" — **คู่มือกรมควบคุมโรค (2564) กำหนดให้ห้องปฏิบัติการรายงานผลด้วยชื่อ RPR ห้ามรายงานเป็น VDRL** และ **CDC 2024 ระบุว่า titre ของ VDRL และ RPR เทียบกันไม่ได้** → ติดตามด้วยวิธีเดิม (และควรเป็นห้องปฏิบัติการเดิม) ทุกครั้ง

### ลำดับการตรวจ: traditional เทียบ reverse
[[fig:algo]]

- **Reverse algorithm** นิยมขึ้นเพราะ TT ทำด้วยเครื่องอัตโนมัติได้ (EIA/CLIA) · กรณี **TT บวก RPR ลบ** → ตรวจ **TT ตัวที่สอง (TPPA หรือ TPHA)** · ถ้าบวกและ **ไม่เคยรักษา → รักษาแบบ latent ไม่ทราบระยะ** · ถ้าลบ → TT ตัวแรกน่าจะบวกลวง
- CDC 2024 ยอมรับทั้งสองแบบ · reverse บวกลวงมากกว่าในประชากรความชุกต่ำ · traditional พลาด early primary และ late latent ได้

> **อัปเดตแนวทาง ·** อาจารย์สอนว่าการคัดกรองฝากครรภ์ใช้ VDRL/RPR — **คู่มือกรมควบคุมโรค (2564) ให้ใช้ reverse algorithm (เริ่มด้วย TT) สำหรับหญิงตั้งครรภ์และคู่ "ไม่ให้ใช้" แบบดั้งเดิม** เพราะ late latent ราว 25–30% มี RPR ลดลงจนลบเอง · WHO 2024 แนะนำ **dual rapid test (TT + NTT)** เป็นอีกทางเลือก
""",
    "pearls": [
        "NTT (RPR/VDRL) = cardiolipin · ขึ้นลงตามโรค · ใช้ติดตาม titre",
        "TT (TPHA/TPPA/FTA-ABS/EIA) = บวกตลอดชีวิต · ยืนยัน ไม่บอก activity",
        "RPR บวก TT ลบ = BFP: SLE, RA, malaria, leptospirosis, ตั้งครรภ์, HIV (ออกสอบ)",
        "Prozone → เจือจาง serum · serofast → titre ต่ำคงที่หลังรักษา ไม่ต้องรักษาซ้ำ",
        "Reverse: TT บวก RPR ลบ → TPPA · บวกและไม่เคยรักษา → รักษาแบบ late latent",
    ],
    "mnem": [{
        "name": "VDRL",
        "what": "สาเหตุของ non-treponemal test บวกลวง",
        "lines": [["V", "**Viral** infection — mono (EBV), hepatitis"],
                  ["D", "**Drugs** — ผู้ใช้ยาเสพติดชนิดฉีด"],
                  ["R", "**Rheumatic** fever และ **rheumatoid** arthritis"],
                  ["L", "**Lupus** (SLE/antiphospholipid) และ **leprosy**"]],
        "note": "อาจารย์เพิ่ม **malaria และ leptospirosis** · CDC เพิ่ม **การตั้งครรภ์ HIV อายุมาก และหลังฉีดวัคซีน** · หลักคือ titre มักต่ำ และ TT ลบ",
        "src": "First Aid for the USMLE Step 1 (VDRL false positives: Viral, Drugs, Rheumatic fever, Lupus/leprosy)",
    }],
    "figs": {"algo": {
        "title": "ลำดับการตรวจซิฟิลิสสองแบบ",
        "cap": "**ซ้าย: traditional** เริ่มด้วย RPR/VDRL แล้วยืนยันด้วย TPHA/TPPA · **ขวา: reverse** เริ่มด้วย treponemal test อัตโนมัติหรือ rapid test แล้วตามด้วย RPR พร้อม titre · ผลขัดแย้ง (TT บวก RPR ลบ) ตัดสินด้วย TT ตัวที่สอง · คู่มือกรมควบคุมโรค (2564) กำหนดให้ใช้ **reverse** คัดกรองหญิงตั้งครรภ์และคู่",
        "svg": FIG_ALGO}},
    "items": [
        mcq(19, "Biologic false-positive nontreponemal test",
            "A 32-year-old woman with systemic lupus erythematosus has a reactive VDRL at a titre of 1:2. TPPA is nonreactive. She has no genital lesions or rash. What is the most likely interpretation?",
            ["Latent syphilis requiring benzathine penicillin weekly for 3 weeks",
             "Prozone phenomenon",
             "Biologic false-positive nontreponemal test",
             "Previously treated syphilis",
             "Neurosyphilis"],
            2,
            "VDRL/RPR วัด antibody ต่อ **cardiolipin** ซึ่งไม่จำเพาะ — โรคที่มีการอักเสบหรือทำลายเนื้อเยื่อทำให้บวกได้ (**SLE, autoimmune, rheumatoid, malaria, leptospirosis** — ที่อาจารย์ถามในห้อง) · **titre ต่ำ + TT ลบ = biologic false positive**\n\nProzone ทำให้ RPR **ลบปลอม** ไม่ใช่บวก · treated syphilis และ neurosyphilis ต้องมี TT บวก",
            "VDRL บวก + TT ลบ = BFP",
            [LEC_REF + " — non-treponemal false positive", CDC + " — Syphilis, diagnostic considerations"],
            ["3.3.16", "B10.3(8)", "B1.5.1(8)"]),
        mcq(20, "Monitoring response to syphilis treatment",
            "A man is treated for secondary syphilis. Which test should be used to monitor his response to treatment?",
            ["TPHA titre",
             "FTA-ABS",
             "TPPA",
             "Signal-to-cutoff ratio of the treponemal immunoassay",
             "Quantitative RPR titre, using the same test method each time"],
            4,
            "อาจารย์ถามห้อง: ติดตามด้วยตัวไหน → **non-treponemal (RPR หรือ VDRL) แบบมี titre** เพราะ **ขึ้นลงตาม activity ของโรค** · ต้องใช้ **วิธีเดิมทุกครั้ง** เพราะ titre ของ VDRL และ RPR เทียบกันไม่ได้\n\nTT ทุกชนิด (TPHA, TPPA, FTA-ABS, EIA) **บวกตลอดชีวิต** และระดับไม่สัมพันธ์กับการตอบสนองต่อการรักษา จึงใช้ติดตามไม่ได้",
            "ติดตาม = RPR titre วิธีเดิม",
            [LEC_REF + " — ติดตามด้วย VDRL/RPR", CDC + " — Syphilis, diagnostic considerations"],
            ["3.3.16", "B10.3(8)"]),
        mcq(21, "Discordant reverse-sequence result",
            "A 45-year-old man is screened with an automated treponemal EIA, which is reactive. Reflex RPR is nonreactive, and a TPPA is reactive. He has never been treated for syphilis and has no symptoms; neurologic examination is normal. What is the most appropriate next step?",
            ["No further action; this pattern is always a false positive",
             "Treat as latent syphilis of unknown duration with benzathine penicillin G weekly for 3 weeks",
             "Repeat the EIA in 6 months before deciding",
             "Perform lumbar puncture before any treatment",
             "Report the EIA as a laboratory error"],
            1,
            "Reverse algorithm: **TT บวก + RPR ลบ** → ตัดสินด้วย **TT ตัวที่สอง (TPPA)** · **TPPA บวก = เคยติดเชื้อจริง** · ถ้า **ไม่เคยได้รับการรักษา** → อาจเป็น late latent ที่ RPR ลดลงเอง → **รักษาแบบ latent ไม่ทราบระยะ (BPG สัปดาห์ละครั้ง × 3)** (CDC 2021 และคู่มือไทย)\n\nถ้าเคยรักษาครบแล้วไม่ต้องทำอะไร · ถ้า TPPA ลบจึงคิดว่า EIA บวกลวง · ไม่มีอาการทางระบบประสาทจึงไม่ต้องเจาะหลัง",
            "EIA+/RPR−/TPPA+ ไม่เคยรักษา → รักษาแบบ late latent",
            [LEC_REF + " — การแปลผล serology", CDC + " — Reverse sequence algorithm", THAI],
            ["3.3.16", "B10.3(8)", "B1.5.1(8)"]),
        mcq(22, "Prozone phenomenon",
            "A 25-year-old woman has a widespread papulosquamous rash including the palms, patchy alopecia and generalized lymphadenopathy. Undiluted RPR is nonreactive, but TPPA is reactive. What is the best next step?",
            ["Ask the laboratory to repeat the RPR on diluted serum",
             "Diagnose seronegative secondary syphilis and stop testing",
             "Conclude that the TPPA is a false positive",
             "Perform lumbar puncture",
             "Start oral acyclovir"],
            0,
            "ภาพทางคลินิกเป็น **secondary syphilis** แต่ RPR ลบ + TT บวก → นึกถึง **prozone phenomenon**: antibody มากเกินจน antigen-antibody ไม่จับกลุ่ม (ราว 1–2% ของ secondary) → **เจือจาง serum (เช่น 1:16) แล้วตรวจใหม่** จะได้ผลบวกพร้อม titre สูง\n\nSecondary syphilis เป็นระยะที่ RPR ไวเกือบ 100% จึงไม่ควรสรุปว่า seronegative · TPPA บวกเข้ากับภาพจึงไม่น่าบวกลวง · ไม่มีข้อบ่งชี้เจาะหลังถ้าไม่มีอาการทางประสาท ตา หรือหู",
            "Secondary แต่ RPR ลบ → เจือจาง serum (prozone)",
            [THAI + " — prozone phenomenon", CDC + " — Syphilis"],
            ["3.3.16", "B10.3(8)"]),
    ],
})

# ---------------------------------------------------------------- 10
SECTIONS.append({
    "id": "id-gus-10",
    "title": "Neurosyphilis, ocular และ otic syphilis — ใครต้องเจาะหลัง และรักษาอย่างไร",
    "summary": "เชื้อเข้า CNS ได้ทุกระยะ อาการตา หู หรือระบบประสาทร่วมกับ serology บวกต้องรักษาด้วย aqueous penicillin G IV 18–24 MU ต่อวัน 10–14 วัน",
    "minutes": 10,
    "source": SRC,
    "nl": ["2.3.1(19)", "2.3.7-3(8)", "B3.2.10-3(2)", "2.1.72", "2.3.8-3(2)", "3.1.7", "B3.3(2)", "B1.7.2"],
    "md": """### เชื้อเข้า CNS ได้ตั้งแต่ระยะแรก
- อาจารย์: บางคนเชื้อเข้าไปอยู่ใน CNS **เงียบ ๆ ไม่มีอาการ** ถ้าไม่ตรวจเลือดก็ไม่รู้ · CDC: **CNS involvement เกิดได้ทุกระยะ** ocular และ otic syphilis ก็เกิดได้ทุกระยะ แต่มักพบในระยะแรก

### อาการที่อาจารย์ยกตัวอย่าง (ต้องนึกถึงซิฟิลิส)
| ระบบ | อาการ |
|---|---|
| **หู (otosyphilis)** | **หูอื้อ หูมีเสียง (tinnitus) โดยไม่ทราบสาเหตุ** · เวียนศีรษะ · การได้ยินลดลงแบบ sensorineural |
| **ตา (ocular)** | **ตาแดง ตาบวมไม่ทราบสาเหตุ** · uveitis (มักเป็น posterior หรือ panuveitis) · **papillitis/optic neuritis** · การมองเห็นลดลง |
| **เส้นประสาทสมอง** | **หน้าเบี้ยวข้างเดียว** · **หนังตาตกข้างเดียว** · Horner syndrome · ชา |
| **Meningovascular** | ปวดศีรษะ meningitis · stroke ในคนอายุน้อย |
| **Late** | general paresis · tabes dorsalis (อ่อนแรง เกร็ง เสียการรับรู้ตำแหน่ง) · Argyll Robertson pupil |

### ใครต้องเจาะหลัง (CSF examination) — CDC 2021
- **มีอาการหรืออาการแสดงทางระบบประสาท** (cranial nerve dysfunction, meningitis, stroke, สับสน)
- **Ocular syphilis ที่มี cranial nerve ผิดปกติ** หรืออาการทางระบบประสาทอื่น (ถ้าตรวจตาพบรอยโรคชัดและ CN 2–6 ปกติ ไม่จำเป็นต้องเจาะก่อนรักษา)
- สงสัย **รักษาล้มเหลว** หรือ titre ไม่ลดตามเกณฑ์ ร่วมกับอาการทางระบบประสาท
- Latent syphilis ที่ **ไม่มีการสัมผัสทางเพศเลยในปีที่ผ่านมา** แล้ว titre ไม่ตอบสนอง (พิจารณา)
- **Otosyphilis ที่มีแต่อาการหู** และตรวจระบบประสาทปกติ → **ไม่แนะนำให้เจาะ** (CSF มักปกติ) แต่รักษาแบบ neurosyphilis

> **อัปเดตแนวทาง ·** อาจารย์เล่าว่าผู้ที่ VDRL บวกบางรายถูกส่งเจาะหลังตรวจ CSF VDRL เพื่อหา neurosyphilis แม้ไม่มีอาการ — **CDC 2021 ไม่แนะนำการเจาะหลังเป็นประจำในผู้ไม่มีอาการ** (รวมผู้ติด HIV) ให้เจาะตามข้อบ่งชี้ข้างต้นเท่านั้น

### CSF ที่เข้าได้กับ neurosyphilis
- เม็ดเลือดขาว **มากกว่า 5 cells/µL** (ผู้ติด HIV ใช้มากกว่า 20) · โปรตีนสูง
- **CSF-VDRL จำเพาะสูงแต่ไวต่ำ** — บวกยืนยันได้ ลบตัดไม่ได้ · **CSF FTA-ABS ไวกว่าแต่จำเพาะน้อยกว่า** — ลบช่วยตัดโรค

### การรักษา (เปลี่ยนจาก benzathine เป็นยาฉีดเข้าหลอดเลือด)
| | ยา |
|---|---|
| **แนะนำ** | **Aqueous crystalline penicillin G (PGS) 18–24 ล้านยูนิต/วัน** = **3–4 ล้านยูนิต IV ทุก 4 ชั่วโมง (วันละ 6 ครั้ง)** หรือหยดต่อเนื่อง นาน **10–14 วัน** (อาจารย์: ราว 14 วัน) |
| ทางเลือก (ถ้ามั่นใจว่าผู้ป่วยมาฉีดครบ) | **Procaine penicillin G 2.4 MU IM วันละครั้ง + probenecid 500 mg วันละ 4 ครั้ง** 10–14 วัน |
| แพ้ penicillin | **Ceftriaxone 1–2 g IV/IM วันละครั้ง 10–14 วัน** (ข้อมูลจำกัด) หรือยืนยันการแพ้แล้วทำ desensitization · หญิงตั้งครรภ์ → desensitize เสมอ |
| หลังครบคอร์ส | พิจารณา BPG 2.4 MU IM สัปดาห์ละครั้ง 1–3 ครั้ง ให้ระยะเวลารวมเท่าการรักษา latent |

- **Ocular และ otic syphilis รักษาแบบ neurosyphilis แม้ CSF ปกติ** · ดูแลร่วมกับจักษุแพทย์หรือแพทย์หู คอ จมูก · steroid เสริมใช้บ่อยแต่ยังไม่พิสูจน์ประโยชน์
- ติดตาม: RPR ในเลือดกลับปกติทำนายว่า CSF จะกลับปกติ → **ไม่ต้องเจาะซ้ำ** ถ้าตอบสนองทั้งอาการและ serology · ตรวจ HIV ทุกราย

> **อัปเดตแนวทาง ·** ในบันทึกอาจารย์พูดว่า neurosyphilis "ให้ benzathine ก็ได้ หรือ PGS ก็ได้ แต่ส่วนใหญ่เป็น PGS" — **CDC 2021 และคู่มือไทยให้ aqueous penicillin G IV เท่านั้นเป็นสูตรหลัก** (ทางเลือกคือ procaine + probenecid) เพราะ **benzathine ไม่ได้ระดับยาฆ่าเชื้อใน CSF** · benzathine มีบทบาทแค่เสริมหลังครบคอร์ส · อาจารย์เองสังเกตว่าแนวทางยุโรปและอเมริการะยะหลังใช้ PGS แทบทั้งหมด
""",
    "pearls": [
        "Neuro/ocular/otic syphilis เกิดได้ทุกระยะ · หูอื้อ ตาแดง หน้าเบี้ยว หนังตาตก + VDRL บวก → คิดถึง",
        "Aqueous penicillin G 18–24 MU/วัน = 3–4 MU IV q4h × 10–14 วัน",
        "ไม่เจาะหลังเป็นประจำ · เจาะเมื่อมีอาการทางประสาท · otic อย่างเดียวไม่ต้องเจาะ",
        "CSF-VDRL จำเพาะแต่ไม่ไว · CSF FTA-ABS ลบช่วยตัดโรค",
        "Benzathine ไม่ถึง CSF → ห้ามใช้เดี่ยวใน neurosyphilis",
    ],
    "mnem": [{
        "name": "Prostitute's pupil (Argyll Robertson)",
        "what": "รูม่านตาใน neurosyphilis ระยะท้าย",
        "lines": [["Accommodates", "หดเมื่อมองใกล้ (accommodation) ได้ — \"accommodates but does not react\""],
                  ["Doesn't react", "ไม่หดต่อแสง (light reflex เสีย) · รูม่านตาเล็กทั้งสองข้าง"]],
        "note": "เป็นอาการของ **late neurosyphilis** (tabes dorsalis/general paresis) — ต่างจาก ocular syphilis ระยะแรกที่มาด้วย uveitis หรือ optic neuritis",
        "src": "First Aid for the USMLE Step 1 (Argyll Robertson pupil — \"prostitute's pupil\")",
    }],
    "items": [
        mcq(23, "Ocular syphilis management",
            "A 34-year-old man has 2 weeks of blurred vision and a red right eye. Ophthalmology finds panuveitis. RPR is 1:128 and TPPA is reactive. Cranial nerve and neurologic examinations are otherwise normal. What is the most appropriate treatment?",
            ["Benzathine penicillin G 2.4 million units IM once",
             "Benzathine penicillin G 2.4 million units IM weekly for 3 weeks",
             "Lumbar puncture first, and treat only if the CSF is abnormal",
             "Aqueous crystalline penicillin G 18–24 million units/day IV (3–4 million units every 4 hours) for 10–14 days, with ophthalmology co-management",
             "Doxycycline 100 mg orally twice daily for 28 days"],
            3,
            "**Ocular syphilis รักษาแบบ neurosyphilis** แม้ CSF ปกติ: **aqueous penicillin G 18–24 MU/วัน IV (3–4 MU ทุก 4 ชั่วโมง) 10–14 วัน** ร่วมกับจักษุแพทย์ — อาจารย์เน้นว่าเจอตาแดงหรือหูอื้อไม่ทราบสาเหตุแล้ว VDRL บวก ให้ **เปลี่ยนจาก benzathine เป็น PGS**\n\nBenzathine ไม่ได้ระดับยาใน CSF และน้ำในลูกตา · CDC 2021: ถ้ามีรอยโรคที่ตาชัดและ CN ปกติ **ไม่จำเป็นต้องเจาะหลังก่อน** และไม่ควรรอผล CSF จึงรักษา · doxycycline ไม่ใช่สูตรสำหรับ ocular syphilis",
            "ตา/หู + serology บวก = penicillin G IV",
            [LEC_REF + " — neuro/ocular/otic syphilis", CDC + " — Neurosyphilis, ocular syphilis, and otosyphilis"],
            ["2.3.7-3(8)", "2.3.1(19)", "B1.7.2"]),
        mcq(24, "Indication for CSF examination",
            "Which patient with reactive syphilis serology most clearly requires lumbar puncture before treatment?",
            ["An asymptomatic HIV-negative woman with early latent syphilis",
             "A man with secondary syphilis whose only findings are rash and lymphadenopathy",
             "A man with latent syphilis who has new left facial palsy and headache",
             "A woman with isolated tinnitus and a normal neurologic examination",
             "A man treated for primary syphilis whose RPR fell fourfold at 6 months"],
            2,
            "CDC 2021: เจาะหลังเมื่อมี **อาการหรืออาการแสดงทางระบบประสาท** — หน้าเบี้ยว (cranial nerve VII) + ปวดศีรษะ = สงสัย **early neurosyphilis (meningitis/cranial neuritis)** → ตรวจ CSF แล้วรักษาด้วย penicillin G IV\n\nไม่มีอาการทางประสาท (early latent, secondary ที่มีแค่ผื่น) **ไม่เจาะเป็นประจำ** · **otosyphilis ที่มีแต่อาการหูและตรวจประสาทปกติ ไม่แนะนำให้เจาะ** แต่รักษาแบบ neurosyphilis · titre ลด 4 เท่าคือตอบสนองดี",
            "อาการทางประสาท = เจาะหลัง · หูอย่างเดียวไม่ต้อง",
            [LEC_REF + " — การเจาะหลังในซิฟิลิส", CDC + " — Neurosyphilis"],
            ["3.1.7", "B3.3(2)", "2.3.1(19)"]),
        mcq(25, "Why benzathine fails in neurosyphilis",
            "Why is benzathine penicillin G alone not adequate treatment for neurosyphilis?",
            ["It frequently causes the Jarisch-Herxheimer reaction",
             "The injection is too painful to repeat",
             "Treponema pallidum has acquired resistance to penicillin",
             "It is nephrotoxic at the doses required",
             "It does not reliably achieve treponemicidal concentrations in the cerebrospinal fluid"],
            4,
            "Benzathine penicillin เป็นเกลือที่ละลายช้า ปล่อยยา **ระดับต่ำแต่นาน** (long-acting) — พอสำหรับเชื้อในเนื้อเยื่อทั่วไป แต่ **ระดับใน CSF ไม่ถึงระดับฆ่าเชื้อ** จึงต้องใช้ **aqueous penicillin G (short-acting) ทางหลอดเลือดดำขนาดสูงทุก 4 ชั่วโมง** — ตรงกับที่อาจารย์อธิบายว่า PGS ออกฤทธิ์สั้นจึงต้องให้ถี่\n\nT. pallidum ยังไม่ดื้อ penicillin · JH reaction เกิดได้กับทุกสูตรและไม่ใช่เหตุผลเลี่ยงยา · ไม่ใช่ปัญหาพิษต่อไตหรือความเจ็บ",
            "Benzathine ระดับต่ำนาน แต่ไม่ถึง CSF",
            [LEC_REF + " — benzathine เทียบ penicillin G sodium", CDC + " — Neurosyphilis"],
            ["B1.7.2", "2.3.1(19)"]),
    ],
})

# ---------------------------------------------------------------- 11
SECTIONS.append({
    "id": "id-gus-11",
    "title": "รักษาซิฟิลิสตามระยะ แพ้ penicillin และ Jarisch–Herxheimer reaction",
    "summary": "Early ใช้ benzathine penicillin G 2.4 MU ครั้งเดียว late ใช้สัปดาห์ละครั้ง × 3 แพ้ยาใช้ doxycycline 14 หรือ 28 วัน และไข้หลังฉีดคือ JH ไม่ใช่แพ้ยา",
    "minutes": 10,
    "source": SRC,
    "nl": ["2.3.1(19)", "B10.2.2(1)", "B1.7.2", "B1.4.11(1)", "2.3.1(9)"],
    "md": """### สูตรยาตามระยะ — **อาจารย์เน้น: ข้อสอบถามชื่อยาและขนาด (ออกสอบ) "พวกนี้จำง่าย"**
| ระยะ | สูตรหลัก | แพ้ penicillin (ไม่ตั้งครรภ์) |
|---|---|---|
| **Early** — primary · secondary · early latent | **Benzathine penicillin G 2.4 ล้านยูนิต IM ครั้งเดียว** | **Doxycycline 100 mg bid 14 วัน** · tetracycline 500 mg qid 14 วัน · ceftriaxone (ดูด้านล่าง) |
| **Late** — late latent · ไม่ทราบระยะ · tertiary ที่ไม่ใช่ neuro | **Benzathine penicillin G 2.4 ล้านยูนิต IM สัปดาห์ละครั้ง × 3** (รวม 7.2 MU) | **Doxycycline 100 mg bid 28 วัน** · tetracycline 500 mg qid 28 วัน |
| **Neurosyphilis · ocular · otic** | **Aqueous penicillin G 18–24 MU/วัน IV 10–14 วัน** | ceftriaxone 1–2 g/วัน 10–14 วัน หรือ desensitize |

- คู่มือไทย: ฉีด BPG **แบ่งสะโพกข้างละ 1.2 ล้านยูนิต** · ลดปวดได้โดยผสม **1% lidocaine ที่ไม่มี epinephrine 0.5–1.0 mL**
- **ผู้ติด HIV ใช้สูตรเดียวกัน** (ไม่ต้องเพิ่มขนาด) แต่ติดตามถี่กว่า
- **ทางเลือกอื่นที่อาจารย์พูดถึง**: procaine penicillin + probenecid · **ceftriaxone IM หรือ IV วันละครั้ง 10–14 วัน** (ทางเลือกสำหรับคนกลัวเข็ม IM ที่ปวด — แต่ต้องมาฉีดทุกวัน)

### ทำไม benzathine ฉีดครั้งเดียวพอ แต่ PGS ต้องให้ถี่ (อาจารย์อธิบาย)
- **Benzathine penicillin = long-acting** ปล่อยยาระดับต่ำนานราว 3 สัปดาห์ เหมาะกับเชื้อที่แบ่งตัวช้ามาก
- **Penicillin G sodium (PGS) = short-acting** ถ้าให้ IV ต้องให้ **ทุก 4 ชั่วโมง วันละ 6 ครั้ง**
- **ลืมนัด (late latent)**: ห่างกัน 7 วันดีที่สุด · คนไม่ตั้งครรภ์ห่างได้ถึง 10–14 วัน · เกินกว่านั้นเริ่มชุดใหม่ · **หญิงตั้งครรภ์ห่างเกิน 9 วัน → เริ่มใหม่ทั้งชุด**

> **อัปเดตแนวทาง ·** อาจารย์ไม่แน่ใจว่า ceftriaxone ต้องให้นานเท่าไร — **CDC 2021**: primary/secondary ใช้ **ceftriaxone 1 g IM/IV วันละครั้ง 10 วัน** (ขนาดที่ดีที่สุดยังไม่ชัด) · neurosyphilis 1–2 g/วัน 10–14 วัน · late latent ยังไม่มีขนาดที่ชัดเจน ต้องปรึกษาผู้เชี่ยวชาญ · คู่มือไทย (2564) ใช้ 1–2 g วันละครั้ง 10–14 วัน และเตือนว่า cross-reaction กับผู้แพ้ penicillin ได้ราว 10% · **azithromycin 2 g ครั้งเดียว CDC ไม่แนะนำแล้ว** เพราะ T. pallidum ดื้อยาและรักษาล้มเหลว (คู่มือไทยยังระบุไว้พร้อมคำเตือนเรื่องดื้อยา)

### ผู้ป่วยที่บอกว่าแพ้ penicillin
- ส่วนใหญ่ไม่ได้แพ้จริง → ประเมินประวัติ · **skin test หรือ oral challenge** ถ้าทำได้
- **ต้อง desensitize แล้วให้ penicillin** เมื่อ: **ตั้งครรภ์** · neurosyphilis · หรือไม่มั่นใจว่าจะกินยาหรือมาติดตามครบ

### Jarisch–Herxheimer reaction
- **ไข้ หนาวสั่น ปวดศีรษะ ปวดกล้ามเนื้อ ภายใน 24 ชั่วโมง** หลังเริ่มยาไม่ว่าสูตรใด · พบบ่อยใน **early syphilis**
- กลไก: เชื้อตายพร้อมกันปล่อย lipoprotein กระตุ้น cytokine — **ไม่ใช่แพ้ยา** ไม่ต้องหยุดยาหรือติดป้ายแพ้
- ให้ยาลดไข้บรรเทาอาการ (ป้องกันไม่ได้) · **บอกผู้ป่วยล่วงหน้า**
- ในหญิงตั้งครรภ์ครึ่งหลังอาจกระตุ้น **เจ็บครรภ์คลอดก่อนกำหนดหรือ fetal distress** แต่ **ห้ามเลื่อนการรักษา**

> **อัปเดตแนวทาง ·** ปัญหา **benzathine penicillin G ขาดแคลน** ในสหรัฐฯ ยังต่อเนื่อง (Bicillin L-A ถูกเรียกคืนบางล็อตปี 2025) — **CDC Dear Colleague letter (10 มี.ค. 2026)** ให้ **สงวน BPG สำหรับหญิงตั้งครรภ์และทารก congenital syphilis** และใช้ **doxycycline 100 mg bid 14 วัน (early) หรือ 28 วัน (late)** ในชายและหญิงไม่ตั้งครรภ์ · FDA อนุญาตนำเข้า **Lentocilin** ชั่วคราว (วิธีเตรียมยาต่างจาก Bicillin) — เป็นบริบทของสหรัฐฯ ในไทยให้ใช้ตามยาที่มีและแนวทางกรมควบคุมโรค
""",
    "pearls": [
        "Early: BPG 2.4 MU IM ครั้งเดียว · แพ้ → doxycycline 100 mg bid 14 วัน",
        "Late/ไม่ทราบระยะ: BPG 2.4 MU สัปดาห์ละครั้ง × 3 · แพ้ → doxycycline 28 วัน",
        "HIV ใช้สูตรเดียวกัน · azithromycin 2 g ไม่แนะนำแล้ว (ดื้อยา)",
        "JH reaction: ไข้ใน 24 ชม. ไม่ใช่แพ้ยา ให้ยาลดไข้และรักษาต่อ",
        "ลืมนัด BPG: ไม่ตั้งครรภ์ ≤ 10–14 วัน · ตั้งครรภ์เกิน 9 วัน เริ่มใหม่",
    ],
    "items": [
        mcq(26, "Penicillin allergy in secondary syphilis",
            "A 27-year-old non-pregnant woman with secondary syphilis reports a history of urticaria after amoxicillin. She is reliable and will attend follow-up. Penicillin skin testing is not available. Which treatment is most appropriate?",
            ["Azithromycin 2 g orally as a single dose",
             "Doxycycline 100 mg orally twice daily for 14 days",
             "Doxycycline 100 mg orally twice daily for 28 days",
             "Ciprofloxacin 500 mg orally twice daily for 3 days",
             "No treatment is possible without penicillin desensitization"],
            1,
            "Early syphilis (primary/secondary/early latent) ในคน **ไม่ตั้งครรภ์ที่แพ้ penicillin** → **doxycycline 100 mg bid 14 วัน** (หรือ tetracycline 500 mg qid 14 วัน · ceftriaxone 1 g/วัน 10 วัน)\n\n28 วันเป็นสูตรของ **late latent/ไม่ทราบระยะ** · **azithromycin 2 g ไม่แนะนำแล้ว** เพราะ T. pallidum ดื้อยา · cipro ใช้กับ chancroid · desensitization จำเป็นใน **หญิงตั้งครรภ์** neurosyphilis หรือเมื่อไม่มั่นใจเรื่องการกินยา",
            "Early + แพ้ (ไม่ตั้งครรภ์) = doxycycline 14 วัน",
            [LEC_REF + " — แพ้ penicillin", CDC + " — Primary and secondary syphilis"],
            ["B1.7.2", "B1.4.11(1)", "2.3.1(19)"]),
        mcq(27, "Syphilis treatment in HIV infection",
            "A 30-year-old man with well-controlled HIV on antiretroviral therapy is diagnosed with primary syphilis. He has no neurologic, ocular or otic symptoms. What is the recommended treatment?",
            ["Benzathine penicillin G 2.4 million units IM once, the same as for people without HIV",
             "Benzathine penicillin G 2.4 million units IM weekly for 3 weeks because of HIV",
             "Aqueous penicillin G IV for 14 days because of HIV",
             "Benzathine penicillin G plus 10 days of amoxicillin and probenecid",
             "Lumbar puncture is mandatory before any treatment"],
            0,
            "CDC 2021 และคู่มือไทย: **ผู้ติด HIV รักษาซิฟิลิสด้วยสูตรเดียวกับผู้ไม่ติดเชื้อ** → primary syphilis = **BPG 2.4 MU IM ครั้งเดียว** · การให้ยาเพิ่ม (BPG หลายครั้ง amoxicillin) ไม่เพิ่มประสิทธิภาพ\n\nไม่ต้องเจาะหลังเป็นประจำถ้าไม่มีอาการทางประสาท ตา หรือหู · สิ่งที่ต่างคือ **ติดตาม titre ถี่กว่า** (3, 6, 9, 12 และ 24 เดือน)",
            "HIV ไม่เปลี่ยนสูตร แต่ติดตามถี่ขึ้น",
            [CDC + " — Syphilis among persons with HIV", THAI],
            ["2.3.1(19)", "2.3.1(9)", "B1.7.2"]),
        mcq(28, "Penicillin allergy in late latent syphilis",
            "A 48-year-old non-pregnant woman has latent syphilis of unknown duration and a documented history of penicillin anaphylaxis. Neurologic and eye examinations are normal. Which regimen is acceptable?",
            ["Doxycycline 100 mg orally twice daily for 14 days",
             "Azithromycin 2 g orally as a single dose",
             "Ceftriaxone 1 g IM as a single dose",
             "Doxycycline 100 mg orally twice daily for 28 days",
             "Erythromycin 500 mg orally four times daily for 14 days"],
            3,
            "Late latent หรือไม่ทราบระยะ + แพ้ penicillin (ไม่ตั้งครรภ์) → **doxycycline 100 mg bid 28 วัน** (หรือ tetracycline 500 mg qid 28 วัน) — อาจารย์: ขยายจาก 2 สัปดาห์เป็น **4 สัปดาห์** ให้สอดคล้องกับการฉีด BPG สามสัปดาห์\n\n14 วันพอสำหรับ early เท่านั้น · azithromycin ดื้อยา · ceftriaxone ครั้งเดียวไม่พอ และขนาดใน late latent ยังไม่ชัด · erythromycin ผ่านรกและ CSF ได้ไม่ดี ผลรักษาต่ำ",
            "Late + แพ้ = doxycycline 28 วัน",
            [LEC_REF + " — late latent แพ้ penicillin", CDC + " — Latent syphilis"],
            ["B1.7.2", "B1.4.11(1)", "2.3.1(19)"]),
    ],
})

# ---------------------------------------------------------------- 12
SECTIONS.append({
    "id": "id-gus-12",
    "title": "ซิฟิลิสในหญิงตั้งครรภ์ การติดตาม titre คู่นอน และการป้องกัน",
    "summary": "หญิงตั้งครรภ์ใช้ penicillin เท่านั้นและต้อง desensitize ถ้าแพ้ ติดตาม RPR ให้ลด 4 เท่า รักษาคู่นอนใน 90 วันทันที และตรวจ HIV ทุกราย",
    "minutes": 10,
    "source": SRC,
    "nl": ["2.3.1(19)", "2.3.16-3(1)", "B10.2.2-3(1)", "2.3.15-3(11)", "3.3.16", "3.3.15", "B1.4.11(1)"],
    "md": """### หญิงตั้งครรภ์ — **อาจารย์: ข้อสอบชอบถาม "หญิงตั้งครรภ์ VDRL บวก ทำอย่างไร" (ออกสอบ)**
- RPR/VDRL เป็นหนึ่งในแล็บคัดกรองตอนฝากครรภ์ (คู่กับ anti-HIV, HBsAg) · บวกแล้วรักษาด้วย **penicillin** และอาจารย์สรุปว่า **สูตรตามระยะเหมือนคนไม่ตั้งครรภ์**
- ไทยคัดกรอง **ตอนฝากครรภ์ครั้งแรกและซ้ำที่อายุครรภ์ 28–32 สัปดาห์** (ตรวจคู่ด้วย) · CDC: ครั้งแรกทุกราย + ซ้ำที่ 28 สัปดาห์และตอนคลอดในพื้นที่ความชุกสูงหรือผู้มีความเสี่ยง · ทารกตายคลอดหลัง 20 สัปดาห์ต้องตรวจแม่

> **อัปเดตแนวทาง ·** อาจารย์บอกว่าทางเลือกการรักษาในหญิงตั้งครรภ์ "เหมือนไม่ตั้งครรภ์" — ถูกเฉพาะสูตร **penicillin ตามระยะ** แต่ **ทางเลือกสำหรับคนแพ้ใช้ไม่ได้**: **CDC 2021 คู่มือไทย และ WHO 2024** ระบุว่า **penicillin เป็นยาเดียวที่ป้องกัน congenital syphilis ได้** · **ห้าม doxycycline/tetracycline** · erythromycin และ azithromycin ไม่ผ่านรกพอ · ceftriaxone ข้อมูลไม่พอ → **แพ้ penicillin ต้อง desensitize แล้วให้ penicillin** · early syphilis อาจให้ **BPG เข็มที่สองห่าง 1 สัปดาห์** · late latent ถ้าเลื่อนนัดเกิน 9 วันต้องเริ่มใหม่ทั้งชุด

- **JH reaction** ในครึ่งหลังของการตั้งครรภ์ → เจ็บครรภ์ก่อนกำหนด fetal distress → แนะนำให้มาโรงพยาบาลถ้ามีไข้ มดลูกหดรัดตัว หรือลูกดิ้นน้อย แต่ **ไม่เลื่อนการรักษา**
- วินิจฉัยหลัง 20 สัปดาห์ → **ultrasound ทารก** (ตับโต ascites hydrops รกหนา = เสี่ยงรักษาล้มเหลว) แต่ไม่เลื่อนการรักษา
- ติดตาม titre: รักษาที่ ≤ 24 สัปดาห์ → ตรวจซ้ำไม่เร็วกว่า 8 สัปดาห์ และตอนคลอด · **คลอดภายใน 30 วันหลังรักษา = ถือว่ารักษาแม่ไม่เพียงพอ** ต้องประเมินทารกเต็มที่
- คู่มือไทย — การรักษาในหญิงตั้งครรภ์ **ล้มเหลว**: อาการไม่ดีขึ้นหรือกลับเป็นซ้ำ · titre **เพิ่ม 4 เท่าขึ้นไป** · หรือ titre **ลดน้อยกว่า 4 เท่า หรือยัง ≥ 1:8 หลังรักษาอย่างน้อย 6 เดือน**

### Congenital syphilis (ข้อมูลเสริม)
- **Early** (ก่อน 2 ขวบ ส่วนใหญ่ใน 5 สัปดาห์แรก): น้ำมูกเรื้อรัง (snuffles) ตับม้ามโต ผื่นลอกที่ฝ่ามือฝ่าเท้า osteochondritis คลอดก่อนกำหนด
- **Late** (หลัง 2 ขวบ): Hutchinson teeth · จมูกยุบ (saddle nose) · interstitial keratitis · หูหนวกจากเส้นประสาทที่ 8 · saber shin
- รักษาทารก: **aqueous penicillin G 50,000 ยูนิต/กก./ครั้ง IV ทุก 12 ชม. (อายุ 1–7 วัน) แล้วทุก 8 ชม. (อายุเกิน 7 วัน) รวม 10 วัน** (คู่มือไทย)

### ติดตามหลังรักษา — ใช้ RPR/VDRL แบบมี titre วิธีเดิม
| กลุ่ม | ตรวจซ้ำ | ตอบสนองพอ |
|---|---|---|
| Primary/secondary | **6 และ 12 เดือน** | titre ลด **4 เท่า (2 dilution) ภายใน 12 เดือน** |
| Latent | **6, 12 และ 24 เดือน** | titre เริ่มต้นสูง (มากกว่า 1:32) ควรลด 4 เท่าภายใน 24 เดือน |
| ผู้ติด HIV (primary/secondary) | **3, 6, 9, 12 และ 24 เดือน** | เกณฑ์เดียวกัน |
- **titre เพิ่ม 4 เท่าค้างเกิน 2 สัปดาห์ หรืออาการกลับมา** → ติดซ้ำหรือรักษาล้มเหลว → ตรวจ HIV ประเมินระบบประสาท ± CSF แล้วรักษาซ้ำ
- **ลดไม่ถึง 4 เท่า** (ราว 10–20% ของผู้รักษา primary/secondary) → ติดตามเพิ่ม ตรวจ HIV · ถ้าติดตามไม่ได้ให้ BPG สัปดาห์ละครั้ง × 3 และพิจารณา CSF
- **อย่าใช้ TT ที่ยังบวกมาสรุปว่ารักษาไม่หาย** (อาจารย์เน้น)

### คู่นอน (CDC 2021)
- คู่นอนที่สัมผัส **ภายใน 90 วัน** ก่อนวินิจฉัย primary/secondary/early latent → **รักษาแบบ early syphilis ทันทีแม้ผลเลือดลบ** (อาจอยู่ในระยะฟักตัว)
- สัมผัส **เกิน 90 วัน** → ตรวจ serology ถ้าได้ผลไม่ทันหรือติดตามยาก ให้รักษาไปเลย
- ช่วงเวลาที่ต้องตามคู่: primary = **3 เดือน + ระยะที่มีอาการ** · secondary = **6 เดือน + ระยะที่มีอาการ** · early latent = **1 ปี**
- คู่มือไทย: early syphilis ติดตามและรักษาคู่เพศสัมพันธ์ **แม้ไม่มีอาการและผลเลือดลบ** · late ให้รักษาคู่ถ้าผลเลือดผิดปกติ

### HIV และการป้องกัน
- **ตรวจ HIV ทุกราย** ที่เป็นซิฟิลิสหรือแผลอวัยวะเพศ · ผลลบในกลุ่มเสี่ยงสูง → เสนอ **PrEP** และตรวจซ้ำที่ 3 เดือน

> **อัปเดตแนวทาง ·** มาตรการป้องกันที่อาจารย์ไม่ได้พูดถึง — **CDC 2024 doxy-PEP**: MSM และหญิงข้ามเพศที่เคยเป็น **ซิฟิลิส หนองใน หรือ chlamydia ใน 12 เดือนที่ผ่านมา** ให้คำปรึกษาและเสนอ **doxycycline 200 mg ครั้งเดียวภายใน 72 ชั่วโมงหลังมีเพศสัมพันธ์ที่ไม่ใช้ถุงยาง** (ไม่เกิน 200 mg ใน 24 ชม.) และตรวจ STI ทุก 3–6 เดือน · ยังไม่แนะนำในหญิงตามเพศกำเนิดเพราะหลักฐานไม่พอ · WHO 2024 แนะนำ **partner services** และ syphilis self-testing เป็นทางเลือกเพิ่ม
""",
    "pearls": [
        "ตั้งครรภ์: penicillin เท่านั้น · แพ้ → desensitize · ห้าม doxycycline (ออกสอบ)",
        "ไทยคัดกรองฝากครรภ์ครั้งแรก + 28–32 สัปดาห์ ด้วย reverse algorithm",
        "P/S: RPR ที่ 6 และ 12 เดือน ต้องลด 4 เท่าใน 12 เดือน · HIV ตรวจถี่กว่า",
        "คู่นอนใน 90 วัน → BPG ทันทีแม้ผลลบ",
        "ตรวจ HIV ทุกราย · doxy-PEP 200 mg ใน 72 ชม. สำหรับ MSM/TGW ที่เคยเป็น STI (CDC 2024)",
    ],
    "items": [
        mcq(29, "Missed benzathine dose in pregnancy",
            "A 26-year-old woman at 22 weeks of gestation has latent syphilis of unknown duration and is receiving benzathine penicillin G 2.4 million units weekly. She received the first dose, then returns 11 days later for the second dose. What should be done?",
            ["Give the second dose now and the third dose 7 days later",
             "Give the remaining two doses together today",
             "Restart the full 3-dose series",
             "Switch to doxycycline 100 mg twice daily for 28 days",
             "Stop treatment, since one dose is adequate in pregnancy"],
            2,
            "CDC 2021: ในหญิงตั้งครรภ์ **ระยะห่างระหว่างเข็มเกิน 9 วันยอมรับไม่ได้ ต้องเริ่มชุดใหม่ทั้งหมด** (คนไม่ตั้งครรภ์ยืดได้ถึง 10–14 วัน) เพราะต้องคงระดับ penicillin ต่อเนื่องเพื่อป้องกัน congenital syphilis\n\nห้ามรวมเข็ม · **doxycycline ห้ามใช้ในหญิงตั้งครรภ์** · late latent/ไม่ทราบระยะต้องได้ครบสามเข็ม",
            "ตั้งครรภ์ ห่างเกิน 9 วัน = เริ่มใหม่",
            [CDC + " — Syphilis during pregnancy", CDC + " — Latent syphilis"],
            ["2.3.16-3(1)", "2.3.15-3(11)", "B1.7.2"]),
        mcq(30, "Management of sex partners",
            "A 35-year-old man is diagnosed with primary syphilis. His female partner, with whom he had sex 4 weeks ago, has no symptoms and a nonreactive RPR and treponemal test today. What is the most appropriate management for her?",
            ["Reassure her; no treatment is needed",
             "Repeat serology in 3 months and treat only if it becomes reactive",
             "Doxycycline 100 mg orally twice daily for 7 days",
             "Treat only if she develops a genital ulcer or rash",
             "Benzathine penicillin G 2.4 million units IM once now"],
            4,
            "คู่นอนที่สัมผัส **ภายใน 90 วัน** ก่อนผู้ป่วยได้รับการวินิจฉัย primary/secondary/early latent → **รักษาแบบ early syphilis ทันที (BPG 2.4 MU IM ครั้งเดียว) แม้ serology ลบ** เพราะอาจอยู่ในระยะฟักตัวที่ยังไม่มี antibody (CDC 2021 · คู่มือไทยก็ให้รักษาคู่แม้ผลเลือดลบ)\n\nการรอดูผลซ้ำหรือรอให้มีอาการเสี่ยงต่อการแพร่เชื้อและ congenital syphilis · doxycycline 7 วันเป็นสูตร chlamydia",
            "คู่นอนใน 90 วัน = BPG ทันทีแม้ผลลบ",
            [CDC + " — Syphilis, management of sex partners", THAI],
            ["2.3.1(19)", "B10.2.2(1)"]),
        mcq(31, "Inadequate serologic response",
            "A 33-year-old HIV-negative man was treated with benzathine penicillin G 2.4 million units for secondary syphilis. His pretreatment RPR was 1:64. At 12 months the RPR is 1:32. He has no symptoms and denies new exposures. How should this be interpreted and managed?",
            ["Adequate response; no further follow-up is needed",
             "Inadequate serologic response; re-evaluate including HIV testing and a neurologic examination (with CSF evaluation if indicated), and consider retreatment with benzathine penicillin weekly for 3 weeks",
             "Serofast state that never requires further evaluation",
             "Reinfection; give a single dose of benzathine penicillin",
             "Switch monitoring to TPHA titres"],
            1,
            "Primary/secondary ต้องมี titre **ลด 4 เท่า (2 dilution) ภายใน 12 เดือน** · 1:64 → 1:32 ลดแค่ 2 เท่า = **inadequate serologic response / อาจรักษาล้มเหลว** → ประเมินซ้ำ: **ตรวจ HIV ตรวจระบบประสาท (± CSF)** และพิจารณารักษาซ้ำด้วย **BPG สัปดาห์ละครั้ง × 3** โดยเฉพาะถ้าติดตามต่อไม่ได้\n\nSerofast ใช้เมื่อ titre ลดลงตามเกณฑ์แล้วค้างที่ต่ำคงที่ · reinfection ต้องมี titre **เพิ่ม** 4 เท่า · TT ใช้ติดตามไม่ได้",
            "P/S ลดไม่ถึง 4 เท่าใน 12 เดือน = ประเมินใหม่",
            [CDC + " — Primary and secondary syphilis, follow-up", LEC_REF + " — ติดตาม VDRL/RPR"],
            ["3.3.16", "2.3.1(19)"]),
    ],
})
