# -*- coding: utf-8 -*-
"""ภาพประกอบ + กลไก คาบ gi 12/10 Acute and chronic hepatitis (ใส่ด้วย apply_figs.py)"""
import math
from svg import *

SET, LEC = "gi", "12/10"

TX_ACUTE = """#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **อาการนำคล้ายไข้หวัด** ไข้ต่ำ อ่อนเพลีย เบื่ออาหาร | เกิดช่วงที่ **ไวรัสในเลือดสูง** → interferon และ cytokine จากภูมิคุ้มกันระยะแรก → อาการทั่วตัว | มาก่อนเหลือง ~1–2 สัปดาห์ |
| **ไข้หายเมื่อเริ่มเหลือง** | ถึงช่วงที่ **T cell ไล่ทำลายเซลล์ตับที่ติดเชื้อ** ไวรัสในเลือดลดลงแล้ว → อาการทั่วตัวซาลง แต่เซลล์ตับเสียหายมากที่สุด → เหลือง | เหลืองแล้ว **ยังไข้สูงหนาวสั่น** → คิด cholangitis ฝีในตับ leptospirosis |
| **อึดอัด/กดเจ็บชายโครงขวา ตับโต** | ตับบวมจากการอักเสบ → **แคปซูล Glisson ถูกยืด** (มีปลายประสาทรับความเจ็บ) | ปวดตื้อคงที่ ไม่ใช่ปวดบิดเป็นพักแบบนิ่ว |
| **ตัวเหลือง ปัสสาวะสีเข้ม** | เซลล์ตับบวมเบียด canaliculi + เซลล์ตาย → **conjugated bilirubin ไหลย้อนเข้าเลือด** → ละลายน้ำ กรองออกทางไต | bilirubin ขึ้น **หลัง ALT** · ปัสสาวะเข้มมักนำมาก่อนตาเหลือง |
| **อุจจาระสีซีด คัน** (บางราย) | bilirubin ลงลำไส้น้อย → stercobilin น้อย · กรดน้ำดีค้างในเลือด → คัน | เด่นใน **cholestatic hepatitis A** ของผู้สูงอายุ |
| **PT ยาว** | ตับสร้าง factor II V VII X ไม่ทัน (factor VII ครึ่งชีวิต ~6 ชม.) | **บอกความรุนแรงได้ดีกว่าระดับ ALT** |"""

TX_ALF = """#### กลไก: ทำไมตับวายจึงซึม เลือดออกง่าย และห้ามยานอนหลับ
- เซลล์ตับตายจำนวนมาก → **สร้าง clotting factor ไม่ทัน** (factor VII ครึ่งชีวิต ~6 ชม.) → **INR ขึ้นภายในวัน** จึงบอกความรุนแรงได้ไวกว่า albumin
- **urea cycle ในตับล้ม** → ammonia จากลำไส้ไม่ถูกเปลี่ยนเป็น urea → เข้าสมอง → **astrocyte เปลี่ยนเป็น glutamine** ซึ่งดึงน้ำเข้าเซลล์ → **สมองบวม** ซึม สับสน จนถึง brain herniation
- ตับ **สร้างและปล่อยน้ำตาลไม่ได้** → hypoglycemia ซ้ำเติมอาการซึม ต้องเจาะน้ำตาลบ่อย
- ตับ **กำจัดยาไม่ได้** → ยานอนหลับ/narcotic ค้าง กดสมองเพิ่ม และ **บดบังว่า encephalopathy แย่ลงหรือไม่**"""

TX_ALC = """#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ไข้ WBC สูง** แม้ไม่มีติดเชื้อ | เหล้าทำให้ลำไส้รั่ว → **endotoxin (LPS)** ผ่าน portal vein → Kupffer cell หลั่ง **TNF-α, IL-8** → **neutrophil** แทรกในตับ | ยังต้อง **หาการติดเชื้อร่วมเสมอ** (SBP ปอดอักเสบ) ก่อนให้ steroid |
| **ตับโตกดเจ็บ** | เซลล์ตับพองจากไขมันและ ballooning → แคปซูลตึง | ตับโต ต่างจากตับแข็งระยะท้ายที่ตับเล็กลง |
| **ตัวเหลือง** | เซลล์ตับบวมเบียด canaliculi + เซลล์ตาย → ขับ conjugated bilirubin ไม่ได้ | bilirubin สูงมากได้ ทั้งที่ AST ไม่เกิน ~400 |
| **ท้องมาน สับสน** | ตับแข็งเดิม + อักเสบเฉียบพลันซ้อน → portal pressure ↑ · albumin ↓ · ammonia ↑ | บ่งว่ารุนแรง (acute-on-chronic) |
| **Spider naevi, palmar erythema** | ตับทำลาย **estrogen** ได้น้อยลง + androgen ถูกเปลี่ยนเป็น estrogen ที่เนื้อเยื่อส่วนปลายมากขึ้น → หลอดเลือดเล็กขยาย | บอกว่า **มีโรคตับเรื้อรังอยู่ก่อน** |"""

TX_DILI = """#### กลไก: ขนาดยาและภูมิคุ้มกันทำลายตับอย่างไร
- **Direct toxic (paracetamol)** — ขนาดปกติส่วนใหญ่ถูกจับกับ glucuronide/sulfate ขับออก ส่วนน้อยผ่าน **CYP2E1 → NAPQI** แล้วถูก **glutathione** ทำลาย · เกินขนาด → NAPQI มากจน **glutathione หมด** → จับโปรตีนใน mitochondria → **เซลล์ตับรอบ central vein (zone 3) ตาย** · **N-acetylcysteine** เติม glutathione
- **Idiosyncratic / immunoallergic** — สารตัวกลางจับโปรตีนในเซลล์จนกลายเป็น "ของแปลก" (hapten) → เฉพาะคนที่มี **HLA หรือยีนเปลี่ยนยาบางแบบ** T cell จึงโจมตีเซลล์ตับ → **ไม่ขึ้นกับขนาด** และ **เกิดหลังเริ่มยาหลายวันถึงหลายสัปดาห์** (เวลาที่ภูมิคุ้มกันต้องใช้) · immunoallergic มี eosinophil จึงมีผื่น ไข้ eosinophil สูง"""

TX_RARE = """#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Ischemic: ALT/AST > 10,000 แล้วลงเร็วใน 72 ชม.** | zone 3 อยู่ปลายทางเลือด O₂ ต่ำสุด → ช็อกทำให้เซลล์แถบนี้ตายพร้อมกันครั้งเดียว · ความดันกลับมาแล้ว **ไม่มีการทำลายต่อเนื่อง** | ไวรัสขึ้นช้ากว่าและลงช้ากว่า · ขาดเลือดมี **LDH สูงมาก** |
| **Ischemic: AST > ALT ช่วงแรก · ไม่ค่อยเหลือง** | ขาด O₂ ทำลาย mitochondria (มี AST) · เซลล์ zone 1–2 ที่รอดยังขับ bilirubin ได้ | — |
| **AIH: globulin (IgG) สูง** | plasma cell ที่แทรกอยู่รอบ portal tract สร้าง IgG จำนวนมาก · ANA ASMA เป็นเครื่องหมายของภูมิที่ผิดทาง | globulin > 1.5 × ULN ช่วยแยกจากไวรัส |
| **AIH: เฉียบพลันแต่มีอาการโรคตับเรื้อรัง** | อักเสบเงียบมานานก่อนมีอาการ → มีพังผืด/ตับแข็งแล้วตอนมาครั้งแรก | ม้ามโต spider naevi ในคนที่ "เพิ่งป่วย" |
| **Wilson: ceruloplasmin ต่ำ** | ATP7B เสีย → ใส่ทองแดงลง apo-ceruloplasmin ไม่ได้ → โปรตีนที่ไม่มีทองแดงถูกสลายเร็ว | ต่ำได้ในตับวายอื่นและขาดโปรตีน → แปลร่วมกับทองแดงในปัสสาวะ |
| **Wilson: เม็ดเลือดแดงแตก Coombs ลบ** | เซลล์ตับตาย → **ทองแดงอิสระทะลักเข้าเลือด** → ทำลายเยื่อหุ้มเม็ดเลือดแดงแบบ oxidative | ตับวาย + hemolysis ในคนอายุน้อย → คิด Wilson |
| **Wilson: ALP ต่ำ · ALP/TB < 2** | bilirubin สูงมาก (hemolysis + ตับวาย) ขณะที่ ALP ต่ำผิดคาด (เชื่อว่าทองแดงแทนที่ zinc ซึ่ง ALP ต้องใช้) | แทบไม่พบในตับวายจากสาเหตุอื่น |
| **Wilson: KF ring · extrapyramidal** | ทองแดงที่ล้นจากตับไปเกาะ **Descemet membrane** ของกระจกตา และ **basal ganglia** | ตรวจ slit lamp |"""

TX_FIB = """#### กลไก: พังผืดเกิดอย่างไร และ Fibroscan วัดอะไร
- เซลล์ตับบาดเจ็บซ้ำนานหลายปี → Kupffer cell และเซลล์ที่ตายปล่อย **TGF-β** → **hepatic stellate cell** เปลี่ยนเป็น myofibroblast → **collagen** สะสมรอบ portal (F1–F2) → เชื่อมเป็นสะพาน (F3) → ล้อมเนื้อตับเป็นก้อน (**F4 ตับแข็ง**)
- พังผืดทำให้ตับ **แข็งขึ้น** → Fibroscan ส่ง **shear wave** เข้าไปในตับ คลื่นวิ่ง **เร็วขึ้นในเนื้อที่แข็ง** แล้วแปลงเป็น kPa · ไขมันทำให้คลื่นอัลตราซาวนด์ **ลดทอนมากขึ้น** = ค่า CAP
- ตับแข็ง **ชั่วคราว** จากอักเสบมาก ตับคั่งเลือด ท่อน้ำดีอุดตัน หรือเพิ่งกินอาหาร → kPa สูงเกินจริง"""

TX_HBV = """#### กลไก: ทำไมอายุที่ติดเชื้อกำหนดว่าจะเรื้อรัง
- HBV **ไม่ได้ทำลายเซลล์ตับโดยตรง** — ตับอักเสบเกิดจาก **T cell ที่ไล่ทำลายเซลล์ติดเชื้อ**
- ทารกที่ติดจากแม่ → ภูมิยังไม่โต + **HBeAg ผ่านรกทำให้ T cell ทนต่อไวรัส (immune tolerance)** → ไม่มีใครกำจัด → เรื้อรัง > 90% แต่ตับอักเสบน้อยในช่วงแรก
- ผู้ใหญ่มี T cell ตอบสนองแรง → ตับอักเสบเฉียบพลันชัดกว่า แต่ **กำจัดไวรัสได้ > 90%**
- เรื้อรังหลายสิบปี → อักเสบซ้ำ → พังผืด · DNA ของ HBV **แทรกใน genome** ของเซลล์ตับ → **มะเร็งตับได้แม้ไม่มีตับแข็ง**"""

TX_HCV = """#### กลไก: อาการนอกตับของ HCV
- HCV กระตุ้น **B cell เรื้อรัง** → B cell โคลนเดียวขยาย สร้าง **IgM ที่เป็น rheumatoid factor** จับ IgG และอนุภาคไวรัส → **cryoglobulin** (ตกตะกอนเมื่อเย็น) → ติดผนังหลอดเลือดเล็ก → **ผื่นจ้ำ ปวดข้อ ปลายประสาทอักเสบ** · ติดที่ glomerulus → **MPGN** โปรตีนรั่ว
- B cell ถูกกระตุ้นนานจนกลายพันธุ์ → **B-cell lymphoma**
- โปรตีนของไวรัสรบกวน insulin signaling ในเซลล์ตับ + ไขมันพอก → **ดื้ออินซูลิน เบาหวาน**"""

TX_MASLD = """#### กลไก: จากดื้ออินซูลินถึงพังผืด
- ไขมันหน้าท้องดื้อ insulin → **สลายไขมันไม่หยุด** → FFA ไหลเข้าตับทาง portal vein (แหล่งใหญ่ที่สุดของไขมันในตับ)
- insulin ในเลือดสูง + น้ำตาล/fructose → ตับ **สร้างไขมันเอง (de novo lipogenesis)** เพิ่ม
- ไขมันเกินกว่าที่ตับจะเผาหรือส่งออกเป็น VLDL → **TG สะสม = steatosis** (มักไม่มีอาการ ALT ปกติหรือสูงเล็กน้อย)
- ไขมันพิษ (FFA อิสระ ceramide) → ROS · ER stress → เซลล์บวมตาย (ballooning) → อักเสบ = **MASH** → stellate cell สร้างพังผืด
- ปัจจัยเมตาบอลิกเดียวกันทำให้ **หลอดเลือดแข็ง** → ผู้ป่วย MASLD **ตายจากหัวใจมากกว่าจากตับ**
- ลดน้ำหนัก → FFA เข้าตับลด → ไขมันลดก่อน แล้วการอักเสบและพังผืดจึงถอยตาม"""

INSERTS = [
    ("gi-hep-01", "- ขาดเลือดไม่มีการอักเสบ", "fig:hep_enzymes"),
    ("gi-hep-01", "| **Acute liver failure** |", "fig:hep_severity"),
    ("gi-hep-02", "**ทำไม B เรื้อรังได้", "fig:hep_routes"),
    ("gi-hep-03", "- **Delta-bilirubin**", "fig:hep_course"),
    ("gi-hep-03", "- **Delta-bilirubin**", TX_ACUTE),
    ("gi-hep-03", "**กับดัก** — **HBsAg อาจเป็นลบ", "fig:hep_hbvsero"),
    ("gi-hep-03", "| **anti-HBs ≥ 10 IU/L** |", "fig:hep_virion"),
    ("gi-hep-04", "→ **ส่งต่อศูนย์ปลูกถ่ายตับทันที**", "fig:hep_alf"),
    ("gi-hep-04", "→ **ส่งต่อศูนย์ปลูกถ่ายตับทันที**", TX_ALF),
    ("gi-hep-05", "- **ราวครึ่งหนึ่งมีตับแข็งแล้ว**", TX_ALC),
    ("gi-hep-05", "| **GGT สูง · MCV สูง** |", "fig:hep_alcohol"),
    ("gi-hep-06", "| **Immunoallergic** |", "fig:hep_dili"),
    ("gi-hep-06", "| **Immunoallergic** |", TX_DILI),
    ("gi-hep-07", "- **ALT ลดลงเร็วภายใน 72 ชม.**", "fig:hep_zone3"),
    ("gi-hep-07", "- Wilson เฉียบพลันรุนแรงมักต้อง", "fig:hep_wilson"),
    ("gi-hep-07", "$", TX_RARE),
    ("gi-hep-08", "**F0–F4**", "fig:hep_fibrosis"),
    ("gi-hep-08", "**F0–F4**", TX_FIB),
    ("gi-hep-09", "- **โอกาสเป็นเรื้อรังขึ้นกับอายุที่ติด**", TX_HBV),
    ("gi-hep-09", "- **คุมได้ทุกราย แต่หายขาดเพียง 1–3%**", "fig:hep_hbvcycle"),
    ("gi-hep-10", "| **HCV** | RNA แบ่งตัว", "fig:hep_reservoir"),
    ("gi-hep-10", "**อาการนอกตับ**", TX_HCV),
    ("gi-hep-11", "- พังผืดเพิ่ม **~1 ระยะทุก 7 ปี**", "fig:hep_masld"),
    ("gi-hep-11", "- พังผืดเพิ่ม **~1 ระยะทุก 7 ปี**", TX_MASLD),
]


def _curve(fn, a, b, X, Y, n=60):
    return [(X(a + (b - a) * i / n), Y(fn(a + (b - a) * i / n))) for i in range(n + 1)]


def hep_enzymes():
    alt = [circ(x, y, 5, "waf") for x, y in ((32, 54), (52, 64), (38, 78), (64, 48))]
    ast = [circ(x, y, 5, "badf") for x, y in ((32, 110), (50, 122), (66, 106))]
    mdots = [circ(x, y, 4, "badf") for x, y in ((44, 162), (62, 154), (78, 166), (94, 156))]
    return fig("เอนไซม์ตับอยู่ตรงไหนในเซลล์",
               "**ALT** อยู่ใน cytoplasm ของเซลล์ตับเป็นหลัก (ครึ่งชีวิต ~47 ชม.) ส่วน **AST** อยู่ทั้งใน cytoplasm (~17 ชม.) และ "
               "**mitochondria** (~87 ชม.) และยังพบในกล้ามเนื้อ หัวใจ เม็ดเลือดแดง — เซลล์ตับบาดเจ็บทั่วไปเยื่อหุ้มรั่ว ของใน cytoplasm "
               "ออกมาก่อนและ ALT อยู่นานกว่า จึงได้ **ALT > AST** · ถ้า mitochondria พัง (เหล้า ขาดเลือด) หรือต้นเหตุอยู่นอกตับ **AST จะเด่น**",
               svg(420, 352, "ALT อยู่ใน cytoplasm ของเซลล์ตับ AST อยู่ทั้ง cytoplasm และ mitochondria และในกล้ามเนื้อ หัวใจ เม็ดเลือดแดง",
                   rect(10, 10, 262, 190, "sk", 26), t(26, 34, "เซลล์ตับ", "sm b"),
                   *alt, t(82, 62, "ALT", "sm b twa"), t(82, 77, "แทบมีเฉพาะในตับ", "xs i2"),
                   *ast, t(82, 112, "AST ใน cytoplasm", "sm b tbad"),
                   ell(110, 160, 92, 22, "ms"), *mdots, t(156, 164, "AST ใน mito", "xs b mid tbad"),
                   t(110, 194, "mitochondria", "xs mid mu"),
                   line(186, 70, 280, 52, "lok w2", "ah-ok"),
                   line(204, 156, 280, 146, "lbad w2", "ah-bad"),
                   box(284, 14, 126, 74, "ok", "บาดเจ็บทั่วไป\nเยื่อหุ้มรั่ว\n→ ALT > AST", fs=11.5),
                   box(284, 110, 126, 74, "bad", "เหล้า / ขาดเลือด\nmitochondria พัง\n→ AST เด่น", fs=11.5),
                   t(10, 226, "AST ยังอยู่ในเนื้อเยื่ออื่นด้วย", "sm b"),
                   box(10, 236, 124, 44, "bx", "กล้ามเนื้อสลาย\n(ดู CK)", fs=11.5),
                   box(148, 236, 124, 44, "bx", "หัวใจขาดเลือด", fs=11.5),
                   box(286, 236, 124, 44, "bx", "เม็ดเลือดแดงแตก", fs=11.5),
                   line(72, 280, 130, 302, "ln", "ah"), line(210, 280, 210, 302, "ln", "ah"), line(348, 280, 290, 302, "ln", "ah"),
                   box(60, 304, 300, 42, "bad", "AST สูงกว่า ALT หลายเท่า\n→ หาต้นเหตุนอกตับก่อน", fs=12)))


def hep_severity():
    rows = [(30, "sk", "เซลล์ตับอักเสบ ตับบวม\nเอนไซม์รั่ว · cytokine", "bx", "ไข้ต่ำ คลื่นไส้\nอึดอัดชายโครงขวา",
             "① มีอาการ", "tok"),
            (120, "ms", "ขับ bilirubin ไม่ทัน\nสร้าง factor II V VII X ไม่ทัน", "ms", "เหลือง\nPT / INR ยาว",
             "② Severe acute liver injury", "tms"),
            (210, "bad", "เซลล์ตายมากจน\nกำจัด ammonia ไม่ได้", "bad", "ซึม สับสน\n= encephalopathy",
             "③ Acute liver failure", "tbad")]
    out = []
    for k, (y, c1, s1, c2, s2, tag, tc) in enumerate(rows):
        out += [box(10, y, 200, 56, c1, s1, fs=11.5), line(210, y + 28, 236, y + 28, "ln", "ah"),
                box(238, y, 172, 56, c2, s2, fs=12), t(410, y - 6, tag, "xs b end " + tc)]
        if k < 2:
            out += [line(110, y + 56, 110, y + 88, "lbad w2", "ah-bad"), t(118, y + 76, "เซลล์ตายมากขึ้น", "xs mu")]
    return fig("ความรุนแรง = จำนวนเซลล์ตับที่หายไป",
               "ตับอักเสบเล็กน้อยให้แค่อาการทั่วตัวและอึดอัดจากแคปซูลตึง · เมื่อเซลล์ตายมากจนหน้าที่ **ขับ bilirubin** และ "
               "**สร้าง clotting factor** ไม่พอ จะเห็นเหลืองร่วมกับ **PT ยาว** (severe acute liver injury) · ถ้าเหลือเซลล์น้อยจน "
               "**กำจัด ammonia ไม่ได้** จะเกิด encephalopathy = **acute liver failure** — ระดับ ALT จึงไม่ได้บอกความรุนแรง",
               svg(420, 300, "เซลล์ตับตายมากขึ้นจากมีอาการ สู่เหลืองและ PT ยาว สู่ encephalopathy",
                   *out, t(210, 292, "ALT สูงแค่ไหนไม่บอกระดับ — ดู bilirubin, INR และระดับความรู้สึกตัว", "xs mid i2")))


def hep_routes():
    return fig("เส้นทางของไวรัสตับอักเสบ",
               "**HAV และ HEV** ติดทางปาก ผ่านลำไส้เข้า portal vein ไปแบ่งตัวในตับ แล้วถูกขับออกทาง **น้ำดีลงอุจจาระ** "
               "จึงวนกลับไปปนเปื้อนอาหารและน้ำ (ในไทย HEV มาจากเนื้อหมูไม่สุก) · **HBV HCV HDV** เข้าทางเลือด เพศสัมพันธ์ หรือแม่สู่ลูก "
               "และ **HDV ต้องยืมเปลือก HBsAg** จึงติดได้เฉพาะคนที่มี HBV · A กับ E ถูกภูมิกำจัดหมดจึงไม่เรื้อรัง ส่วน B ซ่อน cccDNA ไว้ในนิวเคลียส",
               svg(420, 318, "HAV และ HEV ติดทางปาก ขับออกทางน้ำดีลงอุจจาระ HBV HCV HDV ติดทางเลือด HDV ต้องใช้เปลือก HBsAg",
                   t(10, 18, "ทางปาก: A · E", "sm b tok"), t(410, 18, "ทางเลือด: B · C · D", "sm b end tbad"),
                   box(24, 30, 104, 42, "bx", "อาหาร / น้ำ\nปนเปื้อน", fs=11.5),
                   ar(76, 72, 76, 108, "lok w2", "ah-ok", "กิน", "xs i2", dx=8, dy=4),
                   box(24, 110, 104, 42, "bx", "ลำไส้", fs=12),
                   ar(128, 131, 178, 131, "lok w2", "ah-ok", "portal", "xs i2 mid", dy=-6),
                   ell(240, 131, 60, 32, "bad"), t(240, 128, "ตับ", "b mid"), t(240, 144, "ไวรัสแบ่งตัว", "xs mid"),
                   ar(206, 158, 130, 212, "lok w2", "ah-ok", "ขับทางน้ำดี", "xs i2", dx=6, dy=16),
                   box(24, 206, 104, 40, "bx", "อุจจาระ", fs=12),
                   path("M24 226 H12 V51 H20", "lok da", "ah-ok"),
                   box(296, 30, 114, 56, "bad", "เลือด · เข็ม\nเพศ · แม่→ลูก", fs=11.5),
                   ar(330, 86, 290, 106, "lbad w2", "ah-bad"),
                   circ(312, 204, 17, "ac"), *[circ(312 + 17 * math.cos(a / 6 * math.pi), 204 + 17 * math.sin(a / 6 * math.pi), 3, "acf") for a in range(12)],
                   circ(312, 204, 7, "msf"),
                   t(338, 200, "HDV ใช้เปลือก", "xs"), t(338, 214, "HBsAg ของ B", "xs b tac"),
                   box(10, 262, 196, 46, "ok", "A · E: ภูมิกำจัดหมด\n→ ไม่เรื้อรัง", fs=12),
                   box(214, 262, 196, 46, "bad", "B: cccDNA ซ่อนในนิวเคลียส\nC: กลายพันธุ์หลบภูมิ", fs=11.5)))


def hep_course():
    X = lambda w: 40 + w * 45
    Y = lambda v: 230 - v * 150
    alt = lambda w: (w / 1.6) ** 2 if w < 1.6 else 0.45 ** (w - 1.6)
    def bil(w):
        if w < 1.2: return 0
        if w < 3: return 0.8 * ((w - 1.2) / 1.8) ** 1.6
        return 0.8 * (0.6 * 0.5 ** (w - 3) + 0.4 * 0.5 ** ((w - 3) / 3))
    def dlt(w):
        if w < 1.8: return 0
        if w < 3: return 0.32 * (w - 1.8) / 1.2
        return 0.32 * 0.5 ** ((w - 3) / 3)
    ticks = [p for w in range(0, 9) for p in (line(X(w), 230, X(w), 234, "lmu"), t(X(w), 247, str(w), "xs mid mu"))]
    return fig("เส้นเวลาของตับอักเสบจากไวรัสเฉียบพลัน",
               "ALT ขึ้นสูงสุดช่วงต้น แล้วลด **50–70% ต่อสัปดาห์** · bilirubin ขึ้นสูงสุด **ตามหลัง ALT** และลด ~50% ต่อสัปดาห์ "
               "แต่มีหางยาวจาก **delta-bilirubin** (bilirubin ที่จับ albumin ครึ่งชีวิต ~21 วัน ขับทางไตไม่ได้) — ตัวเหลืองจึงหายช้ากว่าเอนไซม์ "
               "· อาการทั่วตัวและไข้ซาลงเมื่อเริ่มเหลือง (แกนตั้งเทียบกับค่าสูงสุดของแต่ละตัว ไม่ใช่ค่าจริง)",
               svg(420, 270, "ALT ขึ้นก่อนและลงเร็ว bilirubin ขึ้นทีหลังและมีหางยาวจาก delta-bilirubin ไข้หายเมื่อเริ่มเหลือง",
                   rect(X(0), 40, X(1.5) - X(0), 18, "sk", 4), t((X(0) + X(1.5)) / 2, 53, "อาการนำ", "xs mid b"),
                   rect(X(1.5), 40, X(6) - X(1.5), 18, "ms", 4), t((X(1.5) + X(6)) / 2, 53, "ตัวเหลือง", "xs mid b tms"),
                   line(X(1.5), 58, X(1.5), 230, "lmu da"), t(X(1.5) - 4, 32, "↓ ไข้หายเมื่อเริ่มเหลือง", "xs i2"),
                   line(X(0), 230, X(8), 230, "lmu"), line(X(0), 230, X(0), 66, "lmu"), *ticks,
                   t(X(8), 264, "สัปดาห์หลังเริ่มมีอาการ", "xs end mu"),
                   poly(_curve(alt, 0, 8, X, Y), "lac w3"), poly(_curve(bil, 1.2, 8, X, Y), "lms w3"),
                   poly(_curve(dlt, 1.8, 8, X, Y), "lms w2 da"),
                   t(X(1.6) + 8, Y(1) + 6, "ALT สูงสุดก่อน", "xs b tac"),
                   t(X(3) + 8, Y(0.8) - 4, "bilirubin สูงสุดทีหลัง", "xs b tms"),
                   t(X(8), 180, "delta-bilirubin ค้างนาน", "xs end tms")))


def hep_virion():
    spikes = [circ(90 + 58 * math.cos(a * math.pi / 8), 128 + 58 * math.sin(a * math.pi / 8), 5, "acf") for a in range(16)]
    return fig("ส่วนประกอบของ HBV กับแอนติบอดีที่ตามมา",
               "**HBsAg** คือโปรตีนเปลือก ร่างกายสร้าง **anti-HBs** ซึ่งจับเปลือกกันไวรัสเข้าเซลล์ = ภูมิคุ้มกัน · วัคซีนทำจาก HBsAg "
               "อย่างเดียว จึงให้ **anti-HBs เพียงตัวเดียว** · **HBcAg** เป็นแกนในที่ร่างกายเห็นเฉพาะเมื่อมีไวรัสจริงแบ่งตัว จึงได้ "
               "**anti-HBc = เคยติดเชื้อ** (IgM ช่วงแรก IgG ตลอดไป) · **HBeAg** ถูกหลั่งจากเซลล์ที่ไวรัสแบ่งตัวมาก",
               svg(420, 316, "อนุภาค HBV มีเปลือก HBsAg แกน HBcAg และเซลล์หลั่ง HBeAg แต่ละตัวทำให้เกิดแอนติบอดีที่มีความหมายต่างกัน",
                   circ(90, 128, 58, "ac"), *spikes, circ(90, 128, 32, "ms"),
                   path("M90 112 A16 16 0 1 1 76 120", "lbad w2"), t(90, 132, "DNA", "xs mid b tbad"),
                   circ(40, 228, 5, "msf"), circ(60, 238, 5, "msf"), circ(34, 248, 5, "msf"), circ(56, 256, 5, "msf"),
                   t(48, 278, "HBeAg (หลั่ง)", "xs mid"),
                   line(136, 92, 184, 42, "lmu da"), line(122, 130, 184, 122, "lmu da"), line(68, 240, 184, 204, "lmu da"),
                   t(190, 36, "HBsAg = เปลือกนอก", "sm b tac"), t(190, 54, "→ anti-HBs = มีภูมิคุ้มกัน", "sm"),
                   t(190, 70, "วัคซีนมีแค่ส่วนนี้", "xs mu"),
                   t(190, 118, "HBcAg = แกนใน", "sm b tms"), t(190, 136, "→ anti-HBc = เคยติดจริง", "sm"),
                   t(190, 152, "IgM ติดใหม่ · IgG ติดนานแล้ว", "xs mu"),
                   t(190, 200, "HBeAg = หลั่งจากเซลล์", "sm b tms"), t(190, 218, "→ ไวรัสแบ่งตัวมาก ติดต่อง่าย", "sm"),
                   t(190, 234, "anti-HBe = แบ่งตัวลดลง", "xs mu"),
                   box(150, 262, 260, 44, "ac", "วัคซีน → anti-HBs อย่างเดียว\nติดเชื้อจริง → anti-HBc บวกเสมอ", fs=12)))


def hep_hbvsero():
    X = lambda m: 30 + m * 40
    Y = lambda v: 236 - v
    s = lambda a, b, h: (lambda m: h * math.sin(math.pi * (m - a) / (b - a)) if a < m < b else 0)
    sg = lambda c, k, h, st: (lambda m: h / (1 + math.exp(-(m - c) * k)) if m > st else 0)
    igm = lambda m: 92 * math.sin(math.pi / 2 * (m - 2.3) / 1.4) if m < 3.7 else 92 * math.exp(-(m - 3.7) / 1.6)
    curves = [(s(1, 5, 112), 1, 5, "lbad w3", "HBsAg"), (s(1.5, 4, 72), 1.5, 4, "lms w2 da", "HBeAg"),
              (igm, 2.3, 9, "lwa w3", "anti-HBc IgM"), (sg(4, 2.2, 130, 2.5), 2.5, 9, "lwa w2 dt", "anti-HBc IgG"),
              (sg(6.8, 2.5, 100, 5.8), 5.8, 9, "lok w3", "anti-HBs"), (s(2.5, 4.6, 58), 2.5, 4.6, "lmu w2 da", "ALT")]
    out, leg = [], []
    for k, (fn, a, b, c, name) in enumerate(curves):
        out.append(poly(_curve(fn, a, b, X, Y), c))
        lx, ly = 14 + (k % 3) * 136, 290 + (k // 3) * 20
        leg += [line(lx, ly - 4, lx + 26, ly - 4, c), t(lx + 32, ly, name, "xs")]
    ticks = [p for m in range(0, 10) for p in (line(X(m), 236, X(m), 240, "lmu"), t(X(m), 251, str(m), "xs mid mu"))]
    return fig("ลำดับผลเลือดใน HBV เฉียบพลันที่หายได้",
               "**HBsAg** ขึ้นก่อนและหายภายในราว 6 เดือน · **anti-HBc IgM** ขึ้นตามมาพร้อมช่วงตับอักเสบ · **anti-HBs** ขึ้นช้า "
               "จึงมีช่วง **window period** ที่ HBsAg ลบแล้วแต่ anti-HBs ยังไม่ขึ้น — ช่วงนี้มีเพียง **anti-HBc IgM** ที่บอกการติดเชื้อ "
               "เหตุนี้สงสัย HBV เฉียบพลันต้องส่ง **HBsAg + anti-HBc IgM** คู่กันเสมอ · anti-HBc IgG อยู่ตลอดชีวิต (เส้นเวลาโดยประมาณ)",
               svg(420, 320, "เส้นเวลาของ HBsAg HBeAg anti-HBc IgM IgG และ anti-HBs ใน HBV เฉียบพลัน มีช่วง window period ที่มีเพียง anti-HBc",
                   rect(X(5), 70, X(6) - X(5), 166, "ms", 2), t((X(5) + X(6)) / 2, 62, "window", "xs b mid tms"),
                   line(X(0), 236, X(9), 236, "lmu"), *ticks, t(X(0), 268, "เดือนหลังได้รับเชื้อ", "xs mu"),
                   *out, *leg))


def hep_alf():
    rows = [("สร้าง factor II V VII X ไม่ได้\n(factor VII t½ ~6 ชม.)", "sk", "INR ≥ 1.5\nเลือดออกง่าย", "ms"),
            ("urea cycle ล้ม\nammonia ค้าง เข้าสมอง", "sk", "astrocyte สร้าง glutamine\nบวม → ซึม สมองบวม", "bad"),
            ("สร้าง / ปล่อยน้ำตาลไม่ได้", "sk", "น้ำตาลต่ำ → ซึมยิ่งขึ้น", "ms"),
            ("กำจัดยาไม่ได้", "sk", "ยานอนหลับ / narcotic ค้าง\nกดสมอง + บดบังอาการ", "ms")]
    out = [path("M60 30 H8 V%d" % (78 + 62 * 3 + 24), "ln")]
    for k, (a, ca, b, cb) in enumerate(rows):
        y = 78 + 62 * k
        out += [line(8, y + 24, 16, y + 24, "ln", "ah"), box(18, y, 186, 48, ca, a, fs=11.5),
                line(204, y + 24, 222, y + 24, "ln", "ah"), box(224, y, 186, 48, cb, b, fs=11.5)]
    return fig("Acute liver failure — หน้าที่ไหนล้ม ทำให้เห็นอะไร",
               "เซลล์ตับตายจำนวนมากในเวลาสั้น ทำให้หน้าที่ของตับล้มพร้อมกัน — **INR ยาว** จากสร้าง clotting factor ไม่ได้ "
               "และ **encephalopathy** จาก ammonia ที่ astrocyte เปลี่ยนเป็น glutamine จนเซลล์บวม (สมองบวม) คือสองเกณฑ์ของ ALF · "
               "น้ำตาลต่ำและยาที่ตับขับไม่ได้ซ้ำเติมอาการซึม จึงเลี่ยงยานอนหลับและ narcotic",
               svg(420, 346, "เซลล์ตับตายจำนวนมากทำให้ INR ยาว ammonia ค้างจนสมองบวม น้ำตาลต่ำ และยาค้าง",
                   box(60, 8, 300, 46, "bad", "เซลล์ตับตายจำนวนมากในเวลาสั้น\nไวรัส · paracetamol · ยา · AIH · Wilson", fs=11.5),
                   *out,
                   t(210, 336, "INR ≥ 1.5 + encephalopathy = ALF → ส่งศูนย์ปลูกถ่ายตับ", "sm mid b tbad")))


def hep_alcohol():
    rows = [("ms", "NADH ล้น → สร้างไขมัน ↑\nเผาไขมัน ↓", "ms", "ไขมันพอกตับ\n(90–95% ของคนดื่มหนัก)"),
            ("bad", "acetaldehyde + ROS (CYP2E1)\nทำลาย mitochondria", "bad", "AST จาก mitochondria รั่ว\n→ AST/ALT > 2"),
            ("sk", "ขาด vitamin B6\n(ALT ต้องใช้ทำงาน)", "sk", "ALT ต่ำกว่าที่ควร\nAST ไม่ค่อยเกิน ~400"),
            ("wa", "ลำไส้รั่ว → endotoxin (LPS)\nเข้า portal vein", "bad", "Kupffer → TNF, IL-8\nneutrophil: ไข้ WBC ↑ เหลือง")]
    out = []
    for k, (c1, a, c2, b) in enumerate(rows):
        y = 80 + 64 * k
        out += [t(4, y + 30, "①②③④"[k], "sm b mu"), box(20, y, 186, 50, c1, a, fs=11),
                line(206, y + 25, 222, y + 25, "ln", "ah"), box(224, y, 186, 50, c2, b, fs=11)]
    return fig("เหล้าทำร้ายเซลล์ตับอย่างไร",
               "ตับเปลี่ยน ethanol ด้วย **ADH → acetaldehyde → ALDH → acetate** ① NADH ที่ล้นจากปฏิกิริยานี้เบนเมตาบอลิซึมไปสร้างไขมัน "
               "② acetaldehyde และ ROS จาก CYP2E1 ทำลาย mitochondria → AST รั่ว ③ ขาด pyridoxine (B6) ทำให้ ALT ต่ำกว่าที่ควร → "
               "**AST/ALT > 2** ④ endotoxin จากลำไส้กระตุ้น Kupffer cell เรียก neutrophil → ไข้ WBC สูง ตับโตกดเจ็บ เหลือง",
               svg(420, 336, "ethanol ถูกเปลี่ยนเป็น acetaldehyde และ acetate ทำให้ไขมันพอก mitochondria พัง ALT ต่ำ และ neutrophil อักเสบ",
                   box(10, 12, 100, 36, "ms", "Ethanol", "b"),
                   ar(110, 30, 148, 30, "ln", "ah", "ADH", "xs i2 mid"),
                   box(150, 12, 120, 36, "bad", "Acetaldehyde", "b", fs=12.5),
                   ar(270, 30, 308, 30, "ln", "ah", "ALDH", "xs i2 mid"),
                   box(310, 12, 100, 36, "bx", "Acetate", fs=12.5),
                   t(129, 66, "NADH ↑", "xs b mid tms"), line(129, 36, 129, 56, "lms", "ah-ms"),
                   *out))


def hep_dili():
    cols = [("bad", "Direct toxic", "ขนาดสูงจน\nglutathione หมด\n→ เซลล์ตายตรง ๆ", "ขึ้นกับขนาด\nคาดเดาได้\nparacetamol"),
            ("ms", "Idiosyncratic", "จับโปรตีนเซลล์\nในคนที่มียีนเสี่ยง\n→ ภูมิ / mito พัง", "ไม่ขึ้นกับขนาด\nแฝง 4 วัน–8 สัปดาห์\nPTU · ยาวัณโรค"),
            ("ac", "Immunoallergic", "ยา+โปรตีน = hapten\n→ T cell, eosinophil\n(HLA-B5801)", "ผื่น ไข้ eos ↑\nallopurinol\nphenytoin")]
    out = []
    for k, (c, h, m, o) in enumerate(cols):
        x = 10 + 137 * k
        out += [line(210, 108, x + 63, 130, "ln", "ah"), box(x, 132, 126, 28, c, h, "b", fs=12),
                line(x + 63, 160, x + 63, 172, "ln", "ah"), box(x, 174, 126, 66, "bx", m, fs=11),
                line(x + 63, 240, x + 63, 252, "ln", "ah"), box(x, 254, 126, 66, c, o, fs=11)]
    return fig("ยาทำร้ายตับได้สามทาง",
               "ยาและสมุนไพรส่วนใหญ่ถูก **CYP450** เปลี่ยนเป็นสารตัวกลางที่ไวปฏิกิริยา · **Direct toxic** — ขนาดสูงเกินกำลังกำจัดพิษ "
               "(glutathione) เซลล์จึงตายตามขนาดยา · **Idiosyncratic** — สารตัวกลางจับโปรตีนเซลล์ในคนที่มียีนเสี่ยง เกิดหลังได้ยาหลายวัน–สัปดาห์ "
               "· **Immunoallergic** — ยาเกาะโปรตีนเป็น hapten กระตุ้น T cell และ eosinophil จึงมีผื่น ไข้ eosinophil สูง "
               "(allopurinol ป้องกันได้ด้วยตรวจ **HLA-B5801**)",
               svg(420, 326, "ยาถูก CYP450 เปลี่ยนเป็นสารตัวกลาง แล้วทำร้ายตับแบบ direct toxic idiosyncratic และ immunoallergic",
                   box(130, 8, 160, 34, "bx", "ยา / สมุนไพร", fs=12.5), line(210, 42, 210, 58, "ln", "ah"),
                   box(100, 60, 220, 48, "sk", "ตับเปลี่ยนยา (CYP450)\n→ สารตัวกลางไวปฏิกิริยา", fs=11.5),
                   *out))


def hep_zone3():
    return fig("ทำไมช็อกและ paracetamol ทำลาย zone 3",
               "เลือดจาก hepatic artery และ portal vein เข้าที่ **portal triad (zone 1)** แล้วไหลผ่าน sinusoid ไปออกที่ **central vein (zone 3)** "
               "O₂ จึงต่ำสุดที่ zone 3 และ zone 3 มี **CYP2E1** มากที่สุด · ความดันต่ำทำให้เซลล์แถบนี้ตายพร้อมกันครั้งเดียว ALT/AST พุ่ง "
               "> 10,000 แต่เมื่อเลือดกลับมาไม่มีการทำลายต่อ จึง **ลดลงเร็วใน 72 ชม.** และไม่ค่อยเหลือง",
               svg(420, 304, "เลือดไหลจาก portal triad zone 1 ไป central vein zone 3 O2 ลดลง ช็อกและ paracetamol จึงทำลาย zone 3",
                   t(214, 50, "เลือดไหลผ่าน sinusoid", "xs mid mu"), line(110, 62, 318, 62, "lmu", "ah-mu"),
                   t(64, 66, "O₂ สูง", "xs b tok"), t(364, 66, "O₂ ต่ำสุด", "xs b end tbad"),
                   rect(64, 76, 100, 80, "ok", 4), rect(164, 76, 100, 80, "ms", 4), rect(264, 76, 100, 80, "bad", 4),
                   t(114, 94, "zone 1", "xs b mid"), t(214, 94, "zone 2", "xs b mid"), t(314, 94, "zone 3", "xs b mid"),
                   line(68, 114, 360, 114, "lbad w2", "ah-bad"), line(68, 138, 360, 138, "lwa w2", "ah-wa"),
                   circ(30, 104, 7, "badf"), circ(44, 122, 11, "waf"), circ(26, 132, 6, "okf"),
                   t(36, 166, "portal triad", "xs mid"),
                   circ(388, 116, 20, "wa"), t(388, 166, "central vein", "xs mid"),
                   t(64, 182, "CYP2E1 น้อย", "xs tok"), t(364, 182, "CYP2E1 มาก", "xs end tbad"),
                   box(10, 198, 195, 70, "bad", "ช็อก / ความดันต่ำ\nzone 3 ขาด O₂ ก่อน\n→ ALT/AST > 10,000", fs=11.5),
                   box(215, 198, 195, 70, "bad", "Paracetamol ขนาดสูง\nNAPQI สร้างมากที่ zone 3\n→ ตายรอบ central vein", fs=11.5),
                   t(210, 292, "เลือดกลับมา → ไม่มีการอักเสบต่อ → ALT ลดเร็วใน 72 ชม.", "xs mid i2")))


def hep_wilson():
    cu = [circ(166 + 15 * i, 52 + 14 * j, 3.6, "msf") for i in range(7) for j in range(4)]
    tg = [("RBC แตก\nCoombs ลบ", "bad"), ("สมอง\nextrapyramidal\nจิตเวช", "ms"), ("กระจกตา\nKF ring", "ms"),
          ("ไต\nCu ปัสสาวะ ↑", "wa")]
    out = []
    for k, (s, c) in enumerate(tg):
        x = 10 + 101 * k
        out += [line(210, 238, x + 48, 264, "ln", "ah"), box(x, 266, 96, 60, c, s, fs=11)]
    return fig("Wilson's disease — ทองแดงออกจากตับไม่ได้",
               "ปกติเซลล์ตับใช้ **ATP7B** ใส่ทองแดงลงใน ceruloplasmin และขับส่วนเกินออกทางน้ำดี · เมื่อ ATP7B เสีย ทองแดงสะสมในเซลล์ตับ "
               "→ ตับอักเสบ/ตับแข็ง และ apo-ceruloplasmin ที่ไม่มีทองแดงถูกสลายเร็ว → **ceruloplasmin ต่ำ** · เมื่อเซลล์ตับตาย "
               "**ทองแดงอิสระทะลักเข้าเลือด** → เม็ดเลือดแดงแตก (Coombs ลบ) ไปเกาะ basal ganglia และกระจกตา (KF ring) และออกทางปัสสาวะ",
               svg(420, 334, "ATP7B เสีย ทองแดงสะสมในตับ ceruloplasmin ต่ำ เซลล์ตับตายปล่อยทองแดงไปทำลายเม็ดเลือดแดง สมอง กระจกตา และออกทางไต",
                   box(10, 30, 104, 44, "bx", "ทองแดง\nจากอาหาร", fs=11.5), line(114, 52, 138, 52, "ln", "ah"),
                   rect(140, 8, 270, 112, "sk", 16), t(152, 28, "เซลล์ตับ", "sm b"), *cu,
                   box(282, 38, 120, 26, "bad", "ATP7B ✕", "b", fs=12),
                   t(286, 86, "→ น้ำดี ✕", "xs i2"), t(286, 102, "→ ceruloplasmin ✕", "xs i2"),
                   line(176, 120, 116, 136, "ln", "ah"), line(300, 120, 316, 136, "ln", "ah"),
                   box(10, 138, 196, 46, "wa", "apo-ceruloplasmin ไม่มี Cu\nสลายเร็ว → ระดับต่ำ", fs=11.5),
                   box(214, 138, 196, 46, "ms", "Cu สะสมในเซลล์\n→ ตับอักเสบ / ตับแข็ง", fs=11.5),
                   line(312, 184, 280, 202, "ln", "ah"),
                   box(60, 204, 300, 34, "bad", "เซลล์ตับตาย → Cu อิสระทะลักเข้าเลือด", fs=12),
                   *out))


def _tile(x, y, k):
    s, o = 66, []
    P = [(x + 8, y + 8), (x + s - 8, y + 8), (x + 8, y + s - 8), (x + s - 8, y + s - 8)]
    C = (x + s / 2, y + s / 2)
    o.append(rect(x, y, s, s, "sk", 6))
    if k >= 1: o += [circ(px, py, 8, "ms") for px, py in P]
    if k == 2:
        o += [line(px, py, px + (C[0] - px) * 0.4, py + (C[1] - py) * 0.4, "lms w3") for px, py in P]
    if k == 3:
        o += [line(P[0][0], P[0][1], P[1][0], P[1][1], "lms w3"), line(P[2][0], P[2][1], P[3][0], P[3][1], "lms w3"),
              line(P[0][0], P[0][1], C[0], C[1], "lms w3"), line(P[3][0], P[3][1], C[0], C[1], "lms w3")]
    if k == 4:
        o = [rect(x, y, s, s, "sk", 6)]
        o += [rect(x + 8, y + 8, s - 16, s - 16, "lms w3", 2), line(x + s / 2, y + 8, x + s / 2, y + s - 8, "lms w3"),
              line(x + 8, y + s / 2, x + s - 8, y + s / 2, "lms w3"),
              *[circ(x + s / 2 + dx, y + s / 2 + dy, 9, "ok") for dx in (-12.5, 12.5) for dy in (-12.5, 12.5)]]
    o += [circ(px, py, 3.4, "acf") for px, py in P] + [circ(C[0], C[1], 3.4, "waf")]
    return o


def _wave(x0, y0, L, amp, n, cls):
    pts = [(x0 + i, y0 + amp * math.sin(2 * math.pi * i / L)) for i in range(0, n + 1, 2)]
    return poly(pts, cls)


def hep_fibrosis():
    chain = [("บาดเจ็บซ้ำ\nหลายปี", "bad"), ("หลั่ง TGF-β", "sk"), ("stellate cell\n→ myofibroblast", "ms"), ("collagen\nสะสม", "ms")]
    out = []
    for k, (s, c) in enumerate(chain):
        x = 10 + 102 * k
        out.append(box(x, 10, 92, 44, c, s, fs=11))
        if k < 3: out.append(line(x + 92, 32, x + 101, 32, "ln", "ah"))
    tiles = []
    for k in range(5):
        x = 12 + 80 * k
        tiles += _tile(x, 76, k) + [t(x + 33, 158, ["F0", "F1", "F2", "F3", "F4 ตับแข็ง"][k], "xs b mid")]
    return fig("พังผืดสะสมจาก F0 ถึง F4 และที่มาของค่า kPa",
               "การบาดเจ็บซ้ำกระตุ้น **stellate cell** ให้สร้าง collagen — เริ่มรอบ portal tract (F1) ยื่นออกมา (F2) "
               "เชื่อมเป็นสะพานระหว่าง portal กับ central vein (F3) จนล้อมเนื้อตับเป็นก้อน (F4) · **≥ F2** เสี่ยงโรคดำเนินต่อ "
               "**≥ F3** เสี่ยงตับแข็งเสื่อมและมะเร็ง · Fibroscan วัด **ความเร็ว shear wave** ที่วิ่งเร็วขึ้นในตับที่แข็ง "
               "(จุดสีเข้ม = portal tract · จุดฟ้า = central vein)",
               svg(420, 340, "บาดเจ็บซ้ำกระตุ้น stellate cell สร้าง collagen พังผืดเพิ่มจาก F0 ถึง F4 ตับยิ่งแข็งคลื่นยิ่งวิ่งเร็ว",
                   *out, *tiles,
                   line(172, 172, 400, 172, "lms w3"), t(166, 176, "≥ F2 significant", "xs end tms b"),
                   line(252, 188, 400, 188, "lbad w3"), t(246, 192, "≥ F3 advanced", "xs end tbad b"),
                   t(10, 220, "Fibroscan: ส่งแรงสั่นแล้ววัดความเร็วคลื่น", "sm b"),
                   rect(14, 236, 16, 40, "sk", 3), _wave(32, 256, 22, 10, 160, "lok w2"),
                   t(110, 296, "นุ่ม: คลื่นช้า (< 8 kPa)", "xs mid tok"),
                   rect(222, 236, 16, 40, "sk", 3), _wave(240, 256, 60, 10, 168, "lbad w2"),
                   t(320, 296, "แข็ง: คลื่นเร็ว (≥ 12 kPa)", "xs mid tbad"),
                   t(210, 326, "ความถี่เท่ากัน คลื่นที่วิ่งเร็วจึงยืดยาวกว่า", "xs mid i2")))


def hep_hbvcycle():
    return fig("วงจรชีวิตของ HBV และจุดที่ยาออกฤทธิ์",
               "HBV ส่ง DNA เข้านิวเคลียสแล้วซ่อมเป็น **cccDNA** ซึ่งเป็นแม่แบบถาวร · cccDNA สร้าง pgRNA แล้วไวรัส "
               "**reverse transcribe** กลับเป็น DNA ในแกน — **tenofovir/entecavir หยุดขั้นนี้** HBV DNA ในเลือดจึงตรวจไม่พบ "
               "แต่ cccDNA และ HBsAg ยังอยู่ (หายขาดเพียง 1–3%) · **หยุดยาเอง** ไวรัสกลับมาแบ่งตัวทันที ตับอักเสบกำเริบรุนแรงได้ · "
               "DNA ที่แทรกใน genome ทำให้เกิด **มะเร็งตับได้แม้ไม่มีตับแข็ง**",
               svg(420, 316, "HBV สร้าง cccDNA ในนิวเคลียส ยา tenofovir หยุดการสร้าง DNA ใหม่ แต่ cccDNA และ HBsAg ยังอยู่",
                   rect(10, 28, 400, 236, "sk", 22), t(316, 48, "เซลล์ตับ", "sm b"),
                   circ(40, 14, 9, "ac"), circ(40, 14, 4, "msf"), line(48, 22, 82, 92, "lac w2", "ah-ac"),
                   ell(130, 154, 100, 64, "bx"), t(130, 112, "นิวเคลียส", "xs mid mu"),
                   circ(90, 150, 18, "lbad w3"), t(90, 190, "cccDNA", "xs b mid tbad"),
                   line(140, 144, 216, 144, "lmu w3"), line(170, 144, 190, 144, "lbad w5"),
                   t(178, 166, "DNA แทรก genome", "xs mid"), t(178, 180, "→ มะเร็งตับ", "xs mid tbad"),
                   line(106, 140, 248, 78, "ln", "ah"),
                   box(250, 62, 150, 30, "bx", "pgRNA", fs=11.5), line(325, 92, 325, 108, "ln", "ah"),
                   box(250, 110, 150, 40, "ms", "reverse transcription\nในแกนไวรัส", fs=11),
                   pill(250, 156, "✕ tenofovir / entecavir", "ok", "xs b mid tok", w=150),
                   line(325, 178, 325, 200, "ln", "ah"),
                   box(266, 202, 118, 28, "bx", "virion ใหม่", fs=11.5), line(325, 230, 325, 282, "lbad w2", "ah-bad"),
                   t(335, 300, "HBV DNA ในเลือด", "xs tbad"),
                   line(140, 214, 120, 282, "lac w2", "ah-ac"), t(22, 300, "HBsAg ยังออกมาแม้กินยา", "xs b tac")))


def hep_reservoir():
    out = []
    data = [("HBV", "ms", "ยาคุมได้\nหายขาด 1–3%"), ("HIV", "bad", "ยาคุมได้\nหายขาดไม่ได้"), ("HCV", "ok", "DAA 12 สัปดาห์\nหาย > 95%")]
    for k, (name, c, res) in enumerate(data):
        x = 10 + 137 * k
        cx = x + 63
        out += [rect(x, 8, 126, 196, "sk", 16), t(cx, 30, name, "b mid"), circ(cx, 82, 34, "bx")]
        if k == 0:
            out += [circ(cx, 82, 12, "lbad w3"), t(cx, 142, "cccDNA", "xs b mid tbad"), t(cx, 158, "ขดอยู่ในนิวเคลียส", "xs mid"),
                    t(cx, 172, "ยาไม่แตะต้อง", "xs mid")]
        elif k == 1:
            out += [line(cx - 26, 82, cx + 26, 82, "lmu w3"), line(cx - 9, 82, cx + 9, 82, "lbad w5"),
                    t(cx, 142, "provirus", "xs b mid tbad"), t(cx, 158, "แทรกใน DNA เซลล์", "xs mid"),
                    t(cx, 172, "ถาวรในเซลล์ความจำ", "xs mid")]
        else:
            out += [_wave(cx - 44, 132, 12, 4, 30, "lac w2"), _wave(cx + 12, 128, 12, 4, 30, "lac w2"),
                    t(cx, 152, "RNA ใน cytoplasm", "xs b mid tac"), t(cx, 168, "ไม่มีที่ซ่อน", "xs mid"),
                    t(cx, 184, "นิวเคลียสว่าง", "xs mid")]
        out += [line(cx, 204, cx, 214, "ln", "ah"), box(x, 216, 126, 46, c, res, fs=11.5)]
    return fig("ทำไม HCV หายขาดได้ แต่ HBV และ HIV ไม่",
               "ไวรัสที่หายขาดยากล้วนมี **แม่แบบสำรองในนิวเคลียส** — HBV มี **cccDNA** HIV มี **provirus** แทรกใน DNA ของเซลล์ "
               "ยาหยุดได้แค่การสร้างไวรัสใหม่ · **HCV** แบ่งตัวเป็น RNA ใน cytoplasm ล้วน ๆ ไม่มีรูปแบบซ่อน เมื่อ DAA หยุดการแบ่งตัว "
               "12 สัปดาห์ RNA ที่เหลือถูกทำลายหมด = **SVR หายขาด**",
               svg(420, 270, "HBV มี cccDNA HIV มี provirus ในนิวเคลียส HCV มีแต่ RNA ใน cytoplasm จึงหายขาดได้", *out))


def hep_masld():
    chain = [(84, "ms", "TG สะสมในเซลล์ตับ\n= steatosis (MASLD)"), (150, "bad", "เกินกำลังเก็บ → lipotoxicity\nROS · ER stress → เซลล์บวมตาย"),
             (216, "bad", "อักเสบ = MASH"), (282, "sk", "stellate cell → พังผืด F1–F4\n→ ตับแข็ง / มะเร็งตับ")]
    out = []
    for k, (y, c, s) in enumerate(chain):
        out.append(box(10, y, 250, 50 if k != 2 else 38, c, s, fs=11.5))
        if k < 3:
            ye = y + (50 if k != 2 else 38)
            out.append(line(135, ye, 135, chain[k + 1][0] - 2, "ln", "ah"))
    lv = [(108, "≥ 3%: ไขมันลด"), (176, "≥ 5%: อักเสบลด"), (236, "≥ 7%: MASH หาย"), (306, "≥ 10%: พังผืดถอย")]
    return fig("MASLD — จากดื้ออินซูลินสู่พังผืด",
               "ไขมันหน้าท้องที่ดื้อ insulin สลายไขมันไม่หยุด ส่ง **FFA** เข้าตับ ร่วมกับ insulin สูงที่เร่ง **de novo lipogenesis** "
               "→ TG สะสม (steatosis) · ไขมันเกินกำลังเก็บกลายเป็น **lipotoxicity** → เซลล์บวมตาย อักเสบ (MASH) → พังผืด · "
               "การลดน้ำหนักย้อนกลไกนี้ตามลำดับ (ลูกศรเขียว) · โรคเมตาบอลิกเดียวกันทำให้ **ตายจากหัวใจมากที่สุด**",
               svg(420, 392, "ดื้อ insulin ทำให้ FFA เข้าตับและตับสร้างไขมันเอง ไขมันสะสม เป็นพิษ อักเสบ และเกิดพังผืด ลดน้ำหนักย้อนกลับได้",
                   box(10, 8, 190, 50, "ms", "ไขมันหน้าท้องดื้อ insulin\n→ สลายไขมัน FFA ↑", fs=11.5),
                   box(214, 8, 196, 50, "ms", "insulin สูง + น้ำตาล/fructose\n→ ตับสร้างไขมันเอง", fs=11.5),
                   line(105, 58, 120, 82, "ln", "ah"), line(300, 58, 200, 82, "ln", "ah"),
                   *out,
                   line(286, 330, 286, 92, "lok w3", "ah-ok"), t(296, 84, "ลดน้ำหนัก", "sm b tok"),
                   *[t(296, y, s, "xs tok") for y, s in lv],
                   box(10, 346, 400, 38, "bad", "เมตาบอลิกเดียวกัน → หลอดเลือดแข็ง → ตายจากหัวใจมากที่สุด", fs=11.5)))
