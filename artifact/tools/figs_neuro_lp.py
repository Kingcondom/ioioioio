# -*- coding: utf-8 -*-
"""ภาพประกอบ + กลไก คาบ neuro 9/10 หัตถการ: Lumbar puncture และการตรวจตาทางระบบประสาท (ใส่ด้วย apply_figs.py)"""
from svg import *

SET, LEC = "neuro", "9/10"

PDPH = """#### ทำไมถึงมีอาการนี้ — post-LP headache
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ปวดศีรษะเมื่อลุกนั่ง/ยืน ดีขึ้นเมื่อนอนราบ** | CSF รั่วออกทางรูที่ดูราเร็วกว่าที่สร้างทดแทน → สมองเสียแรงพยุงของน้ำ (buoyancy) → ท่าตั้งสมองทรุดลงตามแรงโน้มถ่วง **ดึงเยื่อหุ้มสมอง หลอดเลือด และเส้นประสาทที่ไวต่อความปวด** · ตาม Monro–Kellie ปริมาตรที่หายไปถูกแทนด้วย **หลอดเลือดดำในกะโหลกที่ขยายตัว** ซึ่งก็ปวดเช่นกัน | ปวดที่ **ขึ้นกับท่าชัดเจน** เกิดหลังเจาะ 24–48 ชม. = post-LP headache · ถ้าปวดไม่ขึ้นกับท่า มีไข้ ซึมลง ต้องคิดถึง **meningitis หรือเลือดออก** แทน |
| **คอแข็ง ปวดท้ายทอย** | สมองที่ทรุดลงดึงเยื่อหุ้มบริเวณ posterior fossa และคอ | คอแข็งแบบนี้ **ไม่มีไข้ CSF ไม่ขุ่น** ต่างจาก meningitis |
| **หูอื้อ ได้ยินเปลี่ยน** | ความดัน CSF ส่งผ่าน cochlear aqueduct ไปยัง perilymph ของหูชั้นใน — CSF ความดันต่ำ → ความดันในหูชั้นในเสียสมดุล | ดีขึ้นพร้อมอาการปวดเมื่อนอนราบ |
| **มองเห็นภาพซ้อน (มักมองด้านข้างแล้วซ้อน)** | **เส้นประสาทสมองที่ 6** วิ่งยาวในกะโหลก → ถูกยืดเมื่อสมองทรุดลง → กล้ามเนื้อ lateral rectus อ่อนแรง | เกิดร่วมกับปวดศีรษะตามท่า · ส่วนใหญ่หายเองเมื่อรูรั่วปิด |
| **ดีขึ้นทันทีหลังทำ epidural blood patch** | เลือดของผู้ป่วยที่ฉีดเข้า epidural space **กดดันช่อง CSF ให้ความดันกลับขึ้นทันที** และ **แข็งตัวอุดรูรั่ว** | ถ้า blood patch ไม่ช่วย ให้ทบทวนการวินิจฉัย |"""

OPTIC = """#### กลไก: ทำไมโรคเหล่านี้ตามัวแต่ pinhole ไม่ช่วย
| โรค | กลไก → สิ่งที่ผู้ป่วยรู้สึก/สิ่งที่ตรวจพบ | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Optic neuritis** | ปลอกไมอีลินของเส้นประสาทตาอักเสบ (demyelination) → สัญญาณจากจอตาส่งต่อไม่ได้ → **ตามัวเป็นวันถึงสัปดาห์ เห็นสีจางลง (โดยเฉพาะสีแดง)** · เส้นประสาทตาบวมอักเสบ → **ปวดเมื่อกลอกตา** เพราะกล้ามเนื้อตาดึงปลอกหุ้มที่อักเสบ · ใยประสาทนำเข้าส่งแสงได้น้อย → **RAPD** | หญิงอายุน้อย ปวดตาเวลากลอกตา · อาจเป็นอาการแรกของ **multiple sclerosis** |
| **Ischemic optic neuropathy** | หลอดเลือดเล็กที่เลี้ยงขั้วประสาทตาขาดเลือด → ใยประสาทครึ่งบนหรือครึ่งล่างตาย → **ลานสายตาหายครึ่งบนหรือครึ่งล่าง (altitudinal)** ทันที ไม่ปวด · ขั้วประสาทตาบวมข้างเดียว | ผู้สูงอายุ มีความดัน เบาหวาน · ถ้ามีปวดขมับ เจ็บเวลาเคี้ยว ต้องคิดถึง **giant cell arteritis** |
| **Central retinal artery occlusion** | ลิ่มเลือดอุด central retinal artery → จอตาชั้นในขาดเลือดทั้งแผ่น → **ตาบอดทันทีไม่ปวด** · จอตาบวมขาว เห็น **cherry red spot** (ดูภาพในหัวข้อ fundoscopy) | ต้นเหตุมักเป็น emboli จาก carotid หรือหัวใจ → ต้องหาเหมือนผู้ป่วย stroke |"""

PAPILL = """#### ทำไมถึงมีอาการนี้ — papilledema และภาพผิดปกติของจอตา
| สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ขั้วประสาทตาบวม ขอบไม่ชัด ทั้งสองข้าง** | ช่อง subarachnoid ในกะโหลก **ต่อเนื่องกับปลอกหุ้มเส้นประสาทตา** → ความดันในกะโหลกสูงส่งมาถึงด้านหลังลูกตา → กดใยประสาทตรง lamina cribrosa → **axoplasmic flow คั่ง** ใยประสาทบวม → ขั้วนูนและขอบเบลอ | ความดันส่งไปเท่ากันทั้งสองข้าง → **บวมสองข้าง** · ถ้าบวม **ข้างเดียว** คิดถึงโรคที่เส้นประสาทตาเอง (optic neuritis, ischemic optic neuropathy) |
| **หลอดเลือดดำโป่ง เลือดออกรูปเปลวไฟรอบขั้ว** | central retinal vein ออกจากลูกตาผ่านปลอกหุ้มที่ความดันสูง → เลือดดำไหลออกไม่สะดวก → หลอดเลือดดำโป่ง คดเคี้ยว **spontaneous venous pulsation หายไป** และแตกเป็นเลือดออกตามแนวใยประสาท | ถ้ายังเห็น venous pulsation ทำให้ความดันในกะโหลกสูงมีโอกาสน้อยลง |
| **สายตายังดีในระยะแรก แต่จุดบอดกว้างขึ้น** | macula ยังทำงานได้ — ที่บวมคือขั้วประสาทตา ซึ่งเบียดจอตารอบ ๆ ขั้วออกไป → **blind spot กว้างขึ้น** · ถ้าปล่อยนาน ใยประสาทตาย → ลานสายตาแคบ ตาบอดถาวร | ต่างจาก optic neuritis ที่ **สายตาลดตั้งแต่แรก** |
| **ตามืดวูบไม่กี่วินาทีเวลาลุกหรือก้ม (transient visual obscuration)** | ขั้วประสาทตาที่บวมได้รับเลือดแบบพอดี ๆ → ความดันเลือดที่ขั้วลดชั่วครู่เมื่อเปลี่ยนท่า → ใยประสาทขาดเลือดชั่วคราว | อาการเตือนของ papilledema ที่เป็นมาก โดยเฉพาะใน **IIH** |
| **Cotton wool spot** | arteriole เล็กอุด (microinfarct) → ใยประสาทชั้นผิวขาดเลือด → **ส่วนประกอบในแอกซอนขนส่งต่อไม่ได้และคั่ง** → ปื้นขาวฟุ้ง | พบในเบาหวาน ความดันสูง HIV · หายเองในหลายสัปดาห์แต่บอกว่าหลอดเลือดเล็กกำลังเสียหาย |
| **Cherry red spot** | central retinal artery อุด → **จอตาชั้นในบวมขาวทั้งแผ่น** · ที่ fovea **ไม่มีจอตาชั้นใน** และได้เลือดจาก **choroid** → สีแดงของ choroid ยังมองทะลุเห็น | ตาบอดทันทีไม่ปวด = ภาวะฉุกเฉินทางตา · ในโรคสะสม (เช่น Tay–Sachs) เซลล์ปมประสาทรอบ fovea บวมขาวจากไขมันสะสม กลไกการเห็นจุดแดงเหมือนกัน |"""

CSFWHY = """#### กลไก: ทำไมต้องเก็บและแปลผลแบบนี้
- **อัตราส่วน CSF/serum glucose** — glucose เข้า CSF ทาง **ตัวขนส่ง GLUT1** ที่ choroid plexus และหลอดเลือดสมอง → CSF glucose ตาม serum ราว 0.6 เท่าเสมอ (และตามหลังไปราว 2–4 ชั่วโมง) → ถ้าน้ำตาลในเลือดสูง CSF ก็สูงตาม ค่าที่ดูเหมือนปกติจึงอาจต่ำเมื่อเทียบอัตราส่วน · ใน **bacterial meningitis** แบคทีเรียและ neutrophil ใช้ glucose และการขนส่งเสียไป → อัตราส่วนต่ำ
- **Opening pressure ต้องวัดท่านอนตะแคง** — ในท่านั่ง จุดที่เข็มอยู่ต่ำกว่าศีรษะหลายสิบเซนติเมตร → ความดันที่อ่านได้รวม **น้ำหนักของลำน้ำ CSF ที่อยู่เหนือเข็ม** เข้าไปด้วย → สูงเกินจริง · ท่านอนตะแคง เข็มกับศีรษะอยู่ระดับเดียวกัน จึงสะท้อนความดันในกะโหลก
- **Xanthochromia ต้องรอ ~12 ชั่วโมง** — สีเหลืองคือ **bilirubin** ที่ macrophage ในช่อง subarachnoid สร้างจาก heme ของ RBC ที่แตก ต้องใช้เวลาให้เอนไซม์ heme oxygenase ทำงาน → **traumatic tap** ที่เลือดเพิ่งออกขณะเจาะจึงไม่มีสีเหลือง (ถ้าปั่นแยกทันที) และเลือดจางลงจากหลอดแรกไปหลอดท้าย
- **Cytology ไวต่ำ** — เซลล์มะเร็งเกาะเยื่อหุ้มเป็นหย่อม ๆ และหลุดลอยลงมาในน้ำไม่มาก → ต้องเก็บปริมาณมากและเก็บซ้ำ"""

INSERTS = [
    ("neuro-lp-01", "น้ำไขสันหลังตอบได้ดีเป็นพิเศษ", "fig:lp_csf_flow"),
    ("neuro-lp-02", "### ข้อห้ามที่ต้องคิดถึงก่อนเสมอ", "fig:lp_level"),
    ("neuro-lp-02", "| **ผู้ป่วยไม่ให้ความร่วมมือ**", "fig:lp_layers"),
    ("neuro-lp-02", "ถ้าถอนเข็มโดยไม่ใส่ stylet กลับ", "fig:lp_stylet"),
    ("neuro-lp-03", "**การรักษา** — นอนพัก", "fig:lp_pdph"),
    ("neuro-lp-03", "**การรักษา** — นอนพัก", PDPH),
    ("neuro-lp-03", "เกิดเมื่อเจาะหลังในผู้ป่วยที่มี", "fig:lp_herniation"),
    ("neuro-lp-04", "**ต้องเจาะน้ำตาลในเลือดพร้อมกันเสมอ**", "fig:lp_glucose"),
    ("neuro-lp-04", "**ต้องเจาะน้ำตาลในเลือดพร้อมกันเสมอ**", "fig:lp_xantho"),
    ("neuro-lp-04", "**ต้องเจาะน้ำตาลในเลือดพร้อมกันเสมอ**", CSFWHY),
    ("neuro-lp-05", "**หลักการ** — รูเข็มยอมให้", "fig:lp_pinhole"),
    ("neuro-lp-05", "> ในทางอายุรกรรม **ข้อนี้สำคัญมาก**", OPTIC),
    ("neuro-lp-05", "> ในทางอายุรกรรม **ข้อนี้สำคัญมาก**", "fig:lp_rapd"),
    ("neuro-lp-06", "จุดแดงที่ macula ตัดกับ", "fig:lp_papilledema"),
    ("neuro-lp-06", "จุดแดงที่ macula ตัดกับ", "fig:lp_retina"),
    ("neuro-lp-06", "จุดแดงที่ macula ตัดกับ", PAPILL),
]


# ---------------------------------------------------------------- lp-01
def lp_csf_flow():
    L, W = 10, 196
    cx = L + W / 2
    chain = [(10, 46, "wa", "Choroid plexus สร้าง CSF\n~500 mL/วัน · มีอยู่ ~150 mL"),
             (68, 32, "bx", "Lateral → 3rd ventricle"),
             (112, 32, "bx", "Aqueduct → 4th ventricle"),
             (156, 32, "bx", "Foramen Luschka · Magendie"),
             (200, 46, "wa", "Subarachnoid space\nรอบสมอง + ไขสันหลัง")]
    out = []
    for k, (y, h, c, s) in enumerate(chain):
        out.append(box(L, y, W, h, c, s, fs=12 if k else 11.5))
        if k < 4:
            ny = chain[k + 1][0]
            out.append(line(cx, y + h, cx, ny - 2, "lwa w2", "ah-wa"))
    out += [
        line(cx, 246, cx, 270, "lwa w2", "ah-wa"),
        box(L, 272, W, 46, "ac", "Lumbar cistern\nเข็ม LP เก็บ CSF ที่นี่", fs=12),
        path("M206 240 Q270 244 300 268", "lwa w2", "ah-wa"),
        box(222, 272, 188, 46, "wa", "Arachnoid granulation\n→ ดูดกลับสู่ venous sinus", fs=11.5),
        # notes
        brace(212, 70, 186, "lms", 1, 6),
        box(232, 74, 178, 108, "ms", "ช่องแคบอุดตัน\n(ก้อน · เลือด · หนอง)\n→ CSF คั่งเหนือจุดอุด\n→ ventricle โป่ง\n= obstructive\nhydrocephalus", fs=11.5),
        box(232, 194, 178, 42, "bad", "เชื้อ เซลล์อักเสบ\nเซลล์มะเร็ง เลือด ลอยในชั้นนี้", fs=11.5),
        line(232, 215, 210, 215, "lbad", "ah-bad"),
        t(210, 342, "ดูดกลับไม่ทัน → ความดันในกะโหลกสูง (IIH) · การไหลเวียนผิดปกติ → NPH", "xs mid i2"),
        t(210, 360, "CSF ไหลวนผ่านเยื่อหุ้มทั้งหมด จึงเป็น “ตัวอย่าง” ของสิ่งที่เกิดในช่อง subarachnoid", "xs mid i2"),
    ]
    return fig("CSF สร้างที่ไหน ไหลไปไหน และทำไมเจาะที่หลังแล้วรู้เรื่องในสมอง",
               "CSF สร้างจาก **choroid plexus** ไหลผ่าน ventricle ออกสู่ **ช่อง subarachnoid** ที่หุ้มทั้งสมองและไขสันหลัง แล้วถูกดูดกลับที่ **arachnoid granulation** · "
               "เพราะช่องนี้ต่อถึงกันหมด เชื้อ เซลล์อักเสบ เซลล์มะเร็ง และเลือดจาก SAH จึงปนมาให้เก็บได้ที่ **lumbar cistern** · ถ้าการดูดกลับเสีย ความดันจะสูง (IIH) ซึ่งเจาะเพื่อวัดและระบายได้",
               svg(420, 372, "CSF สร้างจาก choroid plexus ไหลผ่าน ventricle สู่ช่อง subarachnoid ลงไปถึง lumbar cistern ที่เจาะ และถูกดูดกลับที่ arachnoid granulation", *out))


# ---------------------------------------------------------------- lp-02
def lp_level():
    names = ["T12", "L1", "L2", "L3", "L4", "L5"]
    out = []
    for k, n in enumerate(names):
        y = 16 + 44 * k
        out += [rect(40, y, 74, 36, "sk", 6), t(77, y + 23, n, "sm b mid"),
                rect(184, y + 12, 44, 26, "sk", 6)]
    out.append(poly([(40, 284), (114, 284), (104, 352), (60, 352)], "sk", True))
    out.append(t(80, 322, "S", "sm b mid"))
    out += [
        rect(124, 6, 52, 318, "wa", 16),                     # dural sac + CSF
        path("M140 6 V92 Q150 116 160 92 V6 Z", "ac"),        # spinal cord + conus
        *[line(144 + 4 * j, 108, 132 + 8 * j, 312, "lac") for j in range(5)],
        # Tuffier line
        line(10, 226, 300, 226, "lms da w2"),
        # needle at L3-L4 interspace (y ~ 188)
        line(400, 188, 152, 188, "ln w3", "ah"), rect(370, 180, 36, 16, "ms", 4),
        # labels
        line(250, 104, 164, 104, "lmu", "ah-mu"),
        t(254, 100, "ไขสันหลังสิ้นสุด (conus)", "xs b"), t(254, 114, "ระดับ L1–L2", "xs i2"),
        t(254, 152, "cauda equina ลอยในน้ำ", "xs b"), t(254, 166, "เข็มเบียดผ่าน ไม่ทิ่มไขสันหลัง", "xs i2"),
        t(254, 210, "เจาะช่อง L3–L4 หรือ L4–L5", "xs b tac"),
        t(254, 248, "เส้นเชื่อมยอด iliac crest", "xs tms b"), t(254, 262, "ผ่าน L4 หรือช่อง L4–L5", "xs tms"),
        line(250, 318, 180, 318, "lmu", "ah-mu"), t(254, 314, "dural sac ยาวถึง S2", "xs b"),
        t(254, 328, "มี CSF ให้เก็บได้", "xs i2"),
        t(150, 344, "หน้า ←", "xs mu end"), t(204, 344, "→ หลัง", "xs mu"),
    ]
    return fig("ทำไมเจาะที่ L3–L4 หรือ L4–L5",
               "ในผู้ใหญ่ **ไขสันหลังสิ้นสุดที่ L1–L2** ต่ำกว่านั้นมีแต่ **cauda equina** ที่ลอยอยู่ในถุงดูราซึ่งยาวลงไปถึง S2 · เจาะต่ำกว่า L2 เข็มจึงเบียดรากประสาทออกไปได้โดยไม่บาดเจ็บไขสันหลัง · "
               "หาระดับข้างเตียงด้วย **เส้นเชื่อมยอด iliac crest (Tuffier’s line)** ซึ่งผ่าน L4 หรือช่อง L4–L5 · ถ้าเข็มไปโดนรากประสาท ผู้ป่วยจะปวดแปลบหรือชาร้าวลงขา (radicular)",
               svg(420, 356, "ภาพตัดตามยาวของกระดูกสันหลังส่วนเอว ไขสันหลังสิ้นสุดที่ L1 ถึง L2 เข็มเจาะที่ช่อง L3 ถึง L4 ใต้ระดับนั้นมีเพียง cauda equina", *out))


def lp_layers():
    layers = [("bx", "ผิวหนัง · ไขมันใต้ผิว", ""),
              ("sk", "Supraspinous ligament", ""),
              ("sk", "Interspinous ligament", ""),
              ("ms", "Ligamentum flavum", "แน่น → รู้สึก “pop” ครั้งแรก"),
              ("bad", "Epidural space", "ไขมัน + venous plexus"),
              ("ac", "Dura + arachnoid", "“pop” ครั้งที่สอง"),
              ("wa", "Subarachnoid space", "CSF ไหลออก = ถึงเป้า")]
    out = []
    y = 14
    for k, (c, a, b) in enumerate(layers):
        h = 40 if k in (4, 6) else 30
        out += [rect(40, y, 160, h, c, 4), t(120, y + h / 2 + 4, a, "xs mid b")]
        if b:
            out.append(t(212, y + h / 2 + 4, b, "xs i2"))
        y += h + 4
    out += [line(24, 4, 24, 268, "ln w3", "ah"), t(18, 14, "เข็ม", "xs end mu")]
    # problems
    out += [
        box(12, 298, 194, 74, "bad", "เลือดแข็งตัวผิดปกติ\nvenous plexus ฉีก\n→ epidural hematoma\n→ กดไขสันหลัง/cauda", fs=11),
        box(214, 298, 196, 74, "ms", "มี epidural abscess\nเข็มทะลุหนอง\n→ พาเชื้อเข้า subarachnoid\n→ meningitis", fs=11),
        t(210, 288, "ถ้ามีข้อห้าม สิ่งที่เกิดใน epidural space", "sm b mid tbad"),
    ]
    return fig("ชั้นที่เข็มผ่าน และจุดที่ข้อห้ามกลายเป็นอันตราย",
               "เข็มผ่านเอ็นสามชั้น ทะลุ **ligamentum flavum** เข้า **epidural space** แล้วผ่าน **ดูรา–arachnoid** จึงถึง CSF · "
               "epidural space มี **ร่างแหหลอดเลือดดำ** — ถ้าเลือดแข็งตัวผิดปกติ เลือดที่ออกจะสะสมเป็นก้อนกดไขสันหลัง (ปวดหลังรุนแรง ขาอ่อนแรง ปัสสาวะผิดปกติ) · "
               "ถ้ามีหนองในชั้นนี้หรือผิวหนังติดเชื้อ เข็มจะลากเชื้อเข้าช่อง CSF",
               svg(420, 380, "ชั้นที่เข็มเจาะหลังผ่าน จากผิวหนังถึงช่อง subarachnoid และภาวะแทรกซ้อนที่เกิดใน epidural space", *out))


def lp_stylet():
    out = [t(105, 20, "ถอนเข็มโดยไม่ใส่ stylet", "sm b mid tbad"), t(315, 20, "ใส่ stylet กลับก่อนถอน", "sm b mid tok"),
           line(210, 10, 210, 300, "lru da")]
    for x0, ok in ((10, False), (220, True)):
        cx = x0 + 95
        # dura band with hole
        out += [rect(x0, 150, 80, 16, "ac", 3), rect(x0 + 110, 150, 80, 16, "ac", 3),
                t(x0 + 186, 184, "ดูรา–arachnoid", "xs end mu"),
                rect(x0, 192, 190, 40, "wa", 6), t(x0 + 186, 226, "CSF", "xs end twa b")]
        # needle tube going up (withdrawing)
        out += [line(cx - 10, 36, cx - 10, 118, "ln w2"), line(cx + 10, 36, cx + 10, 118, "ln w2"),
                line(cx + 30, 110, cx + 30, 58, "lmu w2", "ah-mu"), t(cx + 36, 92, "ถอน", "xs mu")]
        if ok:
            out += [rect(cx - 7, 40, 14, 76, "inkf", 2), t(cx - 16, 64, "stylet", "xs end i2"),
                    rect(x0 + 80, 150, 30, 16, "ac", 3),
                    line(x0 + 95, 150, x0 + 95, 166, "lac"),
                    box(x0 + 5, 246, 180, 48, "ok", "ไม่มีอะไรติดออกมา\nรูหดปิดเอง → รั่วน้อย", fs=11.5)]
        else:
            out += [path("M%d 214 C%d 196 %d 184 %d 166 C%d 150 %d 130 %d 70" % (cx - 2, cx - 16, cx + 8, cx, cx - 6, cx + 6, cx - 2), "lms w3"),
                    t(cx - 18, 82, "เส้นใย", "xs end tms"), t(cx - 18, 96, "arachnoid", "xs end tms"),
                    circ(cx - 22, 176, 3, "waf"), circ(cx - 16, 140, 3, "waf"),
                    circ(cx + 18, 136, 3, "waf"),
                    box(x0 + 5, 246, 180, 48, "bad", "เส้นใยค้างคารู → รูเปิด\n→ CSF รั่วต่อเนื่อง", fs=11.5)]
    out.append(t(210, 316, "เข็มใหญ่ = รูใหญ่ = รั่วมาก · ปล่อยไหลเอง ห้ามดูด (เพิ่มเลือดออก)", "xs mid i2"))
    return fig("Stylet ป้องกัน post-LP headache อย่างไร",
               "เข็มกลวงที่ถอนออกเปล่า ๆ ทำตัวเหมือนหลอดดูด **เส้นใย arachnoid ถูกดึงเข้ารูเข็มและลากมาค้างคารูดูรา** รูจึงปิดไม่ได้ CSF รั่วต่อ · "
               "ใส่ stylet กลับเต็มรูก่อนถอน ไม่มีอะไรติดออกมา รูดูราหดปิดเองได้ · ขนาดรูขึ้นกับขนาดเข็ม จึงใช้เข็มเล็กเมื่อทำได้",
               svg(420, 326, "เมื่อถอนเข็มโดยไม่มี stylet เส้นใย arachnoid ถูกลากมาค้างที่รูดูราทำให้ CSF รั่ว ส่วนเมื่อใส่ stylet รูปิดได้เอง", *out))


# ---------------------------------------------------------------- lp-03
def _head(cx, cy, sag):
    dy = 16 if sag else 0
    out = [circ(cx, cy, 52, "wa"), ell(cx, cy + dy, 40, 34 if sag else 38, "sk")]
    if sag:
        out += [line(cx - 20, cy - 44, cx - 20, cy - 22, "lbad w2", "ah-bad"),
                line(cx + 20, cy - 44, cx + 20, cy - 22, "lbad w2", "ah-bad")]
    return out


def lp_pdph():
    out = [t(105, 18, "นอนราบ", "sm b mid tok"), t(315, 18, "ลุกนั่ง/ยืน", "sm b mid tbad"),
           *_head(105, 82, False), *_head(315, 82, True),
           t(105, 152, "CSF พยุงสมองไว้รอบด้าน", "xs mid i2"), t(105, 166, "แรงดึงกระจายเท่ากัน → ไม่ปวด", "xs mid tok"),
           t(315, 152, "สมองทรุดลง ดึงเยื่อหุ้ม", "xs mid i2"), t(315, 166, "หลอดเลือด เส้นประสาท → ปวด", "xs mid tbad"),
           line(210, 10, 210, 172, "lru da")]
    chain = [("ms", "รูดูรา → CSF รั่วเร็วกว่าสร้าง"),
             ("wa", "ปริมาตร + ความดัน CSF ลด (intracranial hypotension)")]
    y = 186
    for k, (c, s) in enumerate(chain):
        out.append(box(40, y, 340, 30, c, s, fs=12))
        out.append(line(210, y + 30, 210, y + 40, "ln", "ah"))
        y += 42
    out += [line(210, 256, 110, 266, "ln", "ah"), line(210, 256, 310, 266, "ln", "ah"),
            box(10, 268, 196, 66, "bad", "สมองเสียแรงพยุง\n→ ลุกแล้วทรุด ดึงเนื้อเยื่อ\nที่ไวต่อปวด + CN VI", fs=11.5),
            box(214, 268, 196, 66, "bad", "Monro–Kellie\nปริมาตรที่หายไป\n→ หลอดเลือดดำขยายแทน", fs=11.5),
            box(40, 350, 340, 44, "ok", "Epidural blood patch: ก้อนเลือดอุดรู\n+ ดันช่อง CSF → ความดันกลับขึ้น", fs=12),
            line(108, 334, 150, 348, "lok", "ah-ok"), line(312, 334, 270, 348, "lok", "ah-ok")]
    return fig("ทำไม post-LP headache ปวดเมื่อลุกและหายเมื่อนอน",
               "CSF ที่รั่วออกทางรูดูราทำให้สมองขาดน้ำพยุง เมื่อ **ลุกขึ้นสมองทรุดลงตามแรงโน้มถ่วง** ดึงเยื่อหุ้มสมองและหลอดเลือดที่ไวต่อปวด และดึงเส้นประสาทสมองที่ 6 (ภาพซ้อน) · "
               "เมื่อ **นอนราบ** แรงดึงหายไป อาการจึงดีขึ้นชัด · **epidural blood patch** อุดรูและคืนความดันได้ทันที",
               svg(420, 402, "เมื่อ CSF รั่ว สมองเสียแรงพยุง ลุกนั่งแล้วสมองทรุดลงดึงโครงสร้างที่ไวต่อปวด นอนราบแล้วดีขึ้น", *out))


def lp_herniation():
    out = [
        # skull
        path("M20 150 Q20 18 160 18 Q300 18 300 150 L300 200 Q300 232 250 236 L190 236 L190 250 L130 250 L130 236 L70 236 Q20 232 20 200 Z", "bx"),
        # tentorium
        path("M20 158 L126 176", "ln w3"), path("M300 158 L194 176", "ln w3"),
        t(76, 196, "tentorium", "xs mid mu"),
        # mass
        circ(84, 90, 30, "bad"), t(84, 94, "ก้อน", "sm b mid tbad"),
        # pressure label
        t(210, 64, "ความดัน", "sm b mid tbad"), t(210, 80, "เหนือ tentorium สูง", "xs mid tbad"),
        # arrows downward
        line(132, 100, 152, 170, "lbad w3", "ah-bad"), line(196, 100, 170, 170, "lbad w3", "ah-bad"),
        # uncus herniating through notch
        ell(160, 186, 14, 10, "bad"),
        # tonsil through foramen magnum
        ell(160, 244, 16, 12, "bad"),
        # spinal canal
        rect(136, 256, 48, 90, "wa", 8),
        t(128, 270, "foramen", "xs end mu"), t(128, 284, "magnum", "xs end mu"),
        # needle draining
        line(290, 316, 188, 316, "ln w3", "ah"), circ(200, 332, 3, "waf"), circ(212, 340, 3, "waf"), circ(226, 336, 3, "waf"),
        t(300, 306, "LP ปล่อย CSF", "xs b"), t(300, 320, "ความดันล่าง", "xs tbad"), t(300, 334, "ลดทันที", "xs tbad"),
        # outcomes
        line(176, 186, 304, 186, "lmu", "ah-mu"), t(310, 182, "uncal herniation", "xs b"), t(310, 196, "กด CN III", "xs i2"), t(310, 210, "→ รูม่านตาขยาย", "xs i2"),
        line(178, 244, 304, 244, "lmu", "ah-mu"), t(310, 240, "tonsillar herniation", "xs b"), t(310, 254, "กด medulla", "xs i2"), t(310, 268, "→ หยุดหายใจ", "xs tbad b"),
        box(10, 356, 400, 38, "ok", "ป้องกัน: CT ก่อนเจาะใน 5 ข้อบ่งชี้ · papilledema · brain abscess ห้ามเจาะ", fs=11.5),
    ]
    return fig("Cerebral herniation หลังเจาะหลังเกิดอย่างไร",
               "ก้อนในสมองทำให้ **ความดันเหนือ tentorium สูง** แต่ยังสมดุลกับช่องไขสันหลังด้านล่าง · LP ปล่อย CSF จากด้านล่าง ความดันล่างลดทันที เกิด **แรงดันต่างระหว่างบนกับล่าง** "
               "เนื้อสมองจึงถูกดันลงผ่านช่อง tentorium (uncal) และ foramen magnum (tonsillar) กดก้านสมองจนหยุดหายใจ · ป้องกันได้ด้วยการทำภาพก่อนเจาะ",
               svg(420, 402, "ก้อนในสมองทำให้ความดันด้านบนสูง เมื่อปล่อย CSF ด้านล่าง เนื้อสมองถูกดันลงผ่าน tentorium และ foramen magnum", *out))


# ---------------------------------------------------------------- lp-04
def lp_glucose():
    Y0, k = 250, 0.55   # baseline, px per mg/dL
    cols = [("ปกติ", 100, 60, "0.6", "tok", "ปกติ"),
            ("DM ไม่มีติดเชื้อ", 300, 180, "0.6", "tok", "ปกติ"),
            ("DM + bacterial", 300, 90, "0.3", "tbad", "ต่ำ!")]
    out = [line(40, Y0, 410, Y0, "lmu"), t(36, Y0 - 4, "0", "xs end mu"),
           line(40, Y0 - 100 * k, 410, Y0 - 100 * k, "lru dt"), t(36, Y0 - 100 * k + 4, "100", "xs end mu"),
           line(40, Y0 - 200 * k, 410, Y0 - 200 * k, "lru dt"), t(36, Y0 - 200 * k + 4, "200", "xs end mu"),
           line(40, Y0 - 300 * k, 410, Y0 - 300 * k, "lru dt"), t(36, Y0 - 300 * k + 4, "300", "xs end mu"),
           t(10, 18, "mg/dL", "xs mu")]
    for j, (name, bg, cg, r, tc, verdict) in enumerate(cols):
        x = 62 + 122 * j
        out += [rect(x, Y0 - bg * k, 40, bg * k, "bad", 3), rect(x + 46, Y0 - cg * k, 40, cg * k, "wa", 3),
                t(x + 20, Y0 - bg * k - 6, str(bg), "xs mid b"), t(x + 66, Y0 - cg * k - 6, str(cg), "xs mid b"),
                t(x + 43, Y0 + 18, name, "xs mid b"), t(x + 43, Y0 + 34, "ratio " + r + " · " + verdict, "xs mid b " + tc)]
    out += [rect(60, 296, 14, 12, "bad", 2), t(80, 306, "serum", "xs"), rect(140, 296, 14, 12, "wa", 2), t(160, 306, "CSF", "xs"),
            t(410, 306, "CSF 90 ดูปกติ แต่ ratio ต่ำมาก", "xs end tbad b"),
            box(10, 318, 196, 54, "wa", "ปกติ: GLUT1 ขนส่ง\nglucose เข้า CSF ~0.6 เท่า", fs=11.5),
            box(214, 318, 196, 54, "bad", "Bacterial: เชื้อ + neutrophil\nใช้ glucose · ขนส่งเสีย", fs=11.5)]
    return fig("ทำไมต้องดู CSF/serum glucose ratio ไม่ใช่ตัวเลข CSF เดี่ยว ๆ",
               "glucose เข้า CSF ทาง **GLUT1** ได้ราว 0.6 เท่าของเลือด จึงขึ้นลงตามน้ำตาลในเลือดเสมอ · ในผู้ป่วยเบาหวาน CSF glucose 90 mg/dL ดูปกติ "
               "แต่ถ้าเลือด 300 อัตราส่วนคือ 0.3 = **ต่ำ** แบบ bacterial meningitis ที่ **แบคทีเรียและ neutrophil ใช้ glucose** และการขนส่งผ่านเยื่อที่อักเสบเสียไป (ตัวเลขในภาพเป็นตัวอย่าง)",
               svg(420, 380, "แผนภูมิแท่งเปรียบเทียบ glucose ในเลือดและ CSF ในคนปกติ คนเป็นเบาหวาน และเบาหวานที่มี bacterial meningitis", *out))


def _tube(x, y, fill_cls, sup_cls, pellet=11):
    out = [path("M%d %d V%d a12 12 0 0 0 24 0 V%d" % (x, y, y + 60, y), "ln"),
           path("M%d %d V%d a11 11 0 0 0 22 0 V%d Z" % (x + 1, y + 20, y + 60, y + 20), sup_cls)]
    if pellet:
        top = y + 71 - pellet
        out.append(path("M%d %d H%d V%d a11 11 0 0 1 -22 0 Z" % (x + 1, top, x + 23, y + 60) if pellet > 11 else
                        "M%d %d a11 11 0 0 0 22 0 Z" % (x + 1, y + 60), fill_cls))
    return out


def lp_xantho():
    X = lambda h: 40 + h   # px
    out = [line(30, 64, 410, 64, "lmu"),
           *[p for (px, s) in ((30, "0"), (90, "2 ชม."), (190, "12 ชม."), (290, "หลายวัน"), (400, "2 สัปดาห์"))
             for p in (line(px, 60, px, 68, "lmu"), t(px, 84, s, "xs mid mu"))],
           rect(30, 30, 60, 20, "bad", 4), t(60, 44, "RBC แตก", "xs mid b"),
           rect(90, 30, 100, 20, "bad", 4), t(140, 44, "oxyHb สีชมพู", "xs mid b"),
           rect(190, 30, 220, 20, "ms", 4), t(300, 44, "bilirubin สีเหลือง = xanthochromia", "xs mid b"),
           t(210, 18, "macrophage ใช้ heme oxygenase เปลี่ยน heme → bilirubin (ต้องใช้เวลา)", "xs mid i2"),
           line(210, 96, 210, 300, "lru da"),
           t(110, 112, "SAH (เลือดออกก่อนเจาะ)", "sm b mid tbad"), t(320, 112, "Traumatic tap", "sm b mid tms")]
    for j in range(4):
        out += _tube(32 + 46 * j, 126, "badf", "msf")
        out.append(t(44 + 46 * j, 224, str(j + 1), "xs mid mu"))
    for j, pel in enumerate((24, 15, 11, 0)):
        out += _tube(242 + 46 * j, 126, "badf", "sk", pellet=pel)
        out.append(t(254 + 46 * j, 224, str(j + 1), "xs mid mu"))
    out += [t(110, 246, "แดงพอ ๆ กันทุกหลอด", "xs mid i2"), t(110, 262, "ปั่นแล้วน้ำส่วนบนเหลือง", "xs mid tbad b"),
            t(110, 278, "(ถ้าเจาะหลังเลือดออก ≥ 12 ชม.)", "xs mid i2"),
            t(320, 246, "เลือดมากหลอดแรก น้อยลงหลอดท้าย", "xs mid i2"), t(320, 262, "ปั่นแล้วน้ำส่วนบนใส", "xs mid tms b"),
            t(320, 278, "เลือดเพิ่งออก ยังไม่เป็น bilirubin", "xs mid i2"),
            box(10, 296, 400, 40, "ms", "เจาะเร็วกว่า 12 ชม. หลังปวดศีรษะ → ยังไม่เหลือง → อาจลบลวงใน SAH", fs=11.5)]
    return fig("Xanthochromia: นาฬิกาที่บอกว่าเลือดอยู่ในช่อง CSF มานานแค่ไหน",
               "RBC ที่ค้างในช่อง subarachnoid แตกออกให้ oxyhemoglobin แล้ว **macrophage เปลี่ยน heme เป็น bilirubin** ใช้เวลาราว **12 ชั่วโมง** น้ำส่วนบนหลังปั่นจึงเป็นสีเหลือง และคงอยู่ราว 2 สัปดาห์ · "
               "**traumatic tap** เลือดเพิ่งออกขณะเจาะ จึงยังไม่เหลือง และเลือดจางลงจากหลอดแรกไปหลอดสุดท้าย",
               svg(420, 344, "เส้นเวลาการเปลี่ยน hemoglobin เป็น bilirubin และหลอด CSF ใน subarachnoid hemorrhage เทียบกับ traumatic tap", *out))


# ---------------------------------------------------------------- lp-05
def _eye(cy, focus_x, pin=False, sick=False):
    cx = 250
    out = [circ(cx, cy, 46, "bx"), ell(212, cy, 7, 22, "wa"),
           path("M%d %d A46 46 0 0 1 %d %d" % (cx + 26, cy - 38, cx + 26, cy + 38), "lac w3")]
    rays = [-4, 4] if pin else [-24, 0, 24]
    for r in rays:
        y1 = cy + r
        x_end = 212
        if pin:
            out.append(line(40, y1, x_end, y1, "lms"))
        else:
            out.append(line(40, y1, x_end, y1, "lms"))
        # after lens → focus → retina (x=296)
        fy = cy
        sx = 296
        if focus_x < sx:
            ey = fy + (fy - y1) * (sx - focus_x) / (focus_x - x_end)
            out.append(line(x_end, y1, focus_x, fy, "lms"))
            out.append(line(focus_x, fy, sx, ey, "lms"))
        else:
            out.append(line(x_end, y1, sx, fy, "lms"))
    if pin:
        out += [line(150, cy - 40, 150, cy - 6, "ln w5"), line(150, cy + 6, 150, cy + 40, "ln w5"),
                t(150, cy + 56, "pinhole", "xs mid b")]
        for r in (-24, 24):
            out.append(line(40, cy + r, 146, cy + r, "lms da"))
    if sick:
        out += [t(306, cy + 4, "✕", "b tbad"), path("M%d %d A46 46 0 0 1 %d %d" % (291, cy - 16, 291, cy + 16), "lbad w5")]
    return out


def lp_pinhole():
    out = [t(10, 18, "① สายตาสั้น: แสงโฟกัสหน้าจอตา", "sm b"),
           *_eye(76, 266),
           rect(294, 60, 6, 32, "bad", 2), t(316, 72, "แสงกระจาย", "xs tbad b"), t(316, 86, "เป็นวงกว้าง", "xs tbad"), t(316, 100, "= ภาพมัว", "xs tbad"),
           t(10, 148, "② มองผ่าน pinhole: เหลือแต่ลำแสงแกนกลาง", "sm b"),
           *_eye(206, 266, pin=True),
           rect(294, 202, 6, 8, "ok", 2), t(316, 202, "วงแสงเล็ก", "xs tok b"), t(316, 216, "= ชัดขึ้น", "xs tok b"),
           t(10, 288, "③ โรคจอตา/เส้นประสาทตา/ต้อกระจก", "sm b"),
           *_eye(346, 400, sick=True),
           t(324, 340, "โฟกัสถูก แต่", "xs i2"), t(324, 354, "ตัวรับ/สายเสีย", "xs tbad b"), t(324, 368, "→ ไม่ดีขึ้น", "xs tbad b"),
           t(40, 404, "pinhole แก้ได้เฉพาะปัญหา “โฟกัส” ไม่ได้แก้ตัวรับภาพหรือสายส่งภาพ", "xs i2")]
    return fig("Pinhole แยก refractive error ออกจากโรคของตาและเส้นประสาทตาอย่างไร",
               "ในสายตาสั้น ยาว เอียง แสงไม่ได้โฟกัสบนจอตาพอดี จุดแสงจึงกลายเป็น **วงกระจาย (blur circle)** · รูเข็มให้ผ่านเฉพาะ **ลำแสงแนวแกนที่ไม่ต้องหักเห** วงกระจายจึงเล็กลง ภาพชัดขึ้น · "
               "ถ้าปัญหาอยู่ที่ **ตัวรับภาพ (macula) หรือสายส่ง (optic nerve)** หรือสื่อนำแสงขุ่น ทำให้โฟกัสแค่ไหนก็ไม่ช่วย → ต้องหาสาเหตุต่อ",
               svg(420, 414, "ลำแสงเข้าตาในสายตาสั้น มองผ่าน pinhole และในโรคจอตาหรือเส้นประสาทตา pinhole ช่วยได้เฉพาะปัญหาการหักเหแสง", *out))


def lp_rapd():
    out = [
        # eyes
        circ(110, 40, 26, "bx"), circ(110, 40, 8, "inkf"), t(110, 82, "ตาขวา", "xs mid"),
        circ(310, 40, 26, "bx"), circ(310, 40, 8, "inkf"), t(310, 82, "ตาซ้าย", "xs mid"),
        # afferent optic nerves to chiasm
        line(118, 64, 202, 120, "lwa w3"), line(302, 64, 218, 120, "lbad w3 da"),
        t(254, 100, "✕", "b mid tbad"), t(322, 104, "เส้นประสาทตา", "xs mid tbad b"),
        t(322, 118, "ซ้ายเสีย", "xs mid tbad b"), t(322, 132, "(optic neuritis ฯลฯ)", "xs mid tbad"),
        ell(210, 128, 18, 9, "wa"), t(210, 154, "chiasm → optic tract", "xs mid mu"),
        box(150, 166, 120, 30, "wa", "Pretectal nucleus", fs=11.5),
        line(180, 196, 128, 222, "lok", "ah-ok"), line(240, 196, 292, 222, "lok", "ah-ok"),
        box(64, 224, 120, 30, "ok", "EW → CN III ขวา", fs=11.5), box(236, 224, 120, 30, "ok", "EW → CN III ซ้าย", fs=11.5),
        t(210, 214, "ส่งออกสองข้างเท่ากัน", "xs mid tok"),
        line(30, 40, 30, 239, "lok"), line(30, 239, 64, 239, "lok"), line(30, 40, 80, 40, "lok", "ah-ok"),
        line(390, 40, 390, 239, "lok"), line(390, 239, 356, 239, "lok"), line(390, 40, 340, 40, "lok", "ah-ok"),
        t(36, 150, "ส่งออก", "xs tok"), t(36, 164, "CN III", "xs tok"),
        line(10, 268, 410, 268, "lru da"),
    ]
    # swinging flashlight states
    for k, (title, r, sub, c) in enumerate((("ส่องไฟตาขวา (ดี)", 6, "รูม่านตาหดทั้งสองข้าง", "tok"),
                                           ("แกว่งไฟไปตาซ้าย (เสีย)", 13, "รูม่านตาขยายทั้งสองข้าง = RAPD", "tbad"))):
        x0 = 10 + 205 * k
        out += [t(x0 + 97, 288, title, "xs mid b"),
                circ(x0 + 55, 318, 18, "bx"), circ(x0 + 55, 318, r, "inkf"),
                circ(x0 + 140, 318, 18, "bx"), circ(x0 + 140, 318, r, "inkf"),
                t(x0 + 97, 354, sub, "xs mid " + c + " b")]
        lx = x0 + 55 if k == 0 else x0 + 140
        out.append(poly([(lx - 6, 296), (lx + 6, 296), (lx, 302)], "msf", True))
    out.append(t(210, 380, "ต้อกระจก/refractive error ไม่ทำให้เกิด RAPD — สัญญาณยังเข้าถึงสมองได้", "xs mid i2"))
    return fig("Swinging flashlight test: ดูว่าเส้นประสาทตาข้างไหนส่งสัญญาณได้น้อย",
               "แสงเข้าตาข้างใดก็ตาม สัญญาณผ่าน **optic nerve → pretectal nucleus** แล้วกระจายไป **EW ทั้งสองข้าง** รูม่านตาจึงหดเท่ากันสองข้างเสมอ · "
               "ถ้าเส้นประสาทตาซ้ายเสีย เมื่อแกว่งไฟจากตาขวามาตาซ้าย สมองรับแสงได้น้อยลง รูม่านตา **ทั้งสองข้างกลับขยาย** = **relative afferent pupillary defect (RAPD)** — ชี้ว่าตามัวเพราะเส้นประสาทตา/จอตาเป็นวงกว้าง ไม่ใช่สายตาหรือต้อกระจก",
               svg(420, 390, "วงจร pupillary light reflex และ swinging flashlight test เมื่อเส้นประสาทตาซ้ายเสีย รูม่านตาขยายทั้งสองข้างเมื่อส่องตาซ้าย", *out))


# ---------------------------------------------------------------- lp-06
def lp_papilledema():
    top = [
        # globe
        circ(70, 100, 56, "bx"), path("M114 66 A56 56 0 0 1 114 134", "lac w3"),
        t(60, 104, "ลูกตา", "xs mid mu"),
        # optic nerve with sheath
        rect(124, 70, 236, 60, "wa", 10),              # sheath with SAS (CSF)
        rect(124, 86, 236, 28, "ac", 4),               # nerve
        t(250, 104, "optic nerve", "xs mid b"),
        t(250, 64, "ช่อง subarachnoid รอบเส้นประสาทตา (CSF)", "xs mid twa"),
        # brain side
        rect(360, 40, 52, 120, "sk", 10), t(386, 96, "กะโหลก", "xs mid"), t(386, 110, "ICP ↑", "xs mid tbad b"),
        line(356, 78, 300, 78, "lbad w2", "ah-bad"), line(356, 122, 300, 122, "lbad w2", "ah-bad"),
        # disc swelling bump
        path("M114 88 Q98 100 114 112", "lbad w3"),
        line(140, 76, 140, 86, "lbad w2", "ah-bad"), line(140, 124, 140, 114, "lbad w2", "ah-bad"),
        t(104, 154, "ขั้วบวม", "xs mid tbad b"),
        t(176, 146, "กดใยประสาท + central retinal vein", "xs i2"),
    ]
    out = [g(*top, tr="translate(0,-34)")]
    chain = [("bad", "ICP ↑ ส่งผ่าน CSF มาถึงหลังลูกตา (ทั้งสองข้าง)"),
             ("ms", "กดตรง lamina cribrosa → axoplasmic flow คั่ง"),
             ("ms", "ใยประสาทบวม → ขั้วนูน ขอบเบลอ"),
             ("bad", "central retinal vein ถูกกด → venous pulsation หาย\nหลอดเลือดดำโป่ง เลือดออกรอบขั้ว")]
    y = 136
    for k, (c, s) in enumerate(chain):
        h = 44 if "\n" in s else 30
        out.append(box(20, y, 380, h, c, s, fs=12))
        if k < 3:
            out.append(line(210, y + h, 210, y + h + 10, "ln", "ah"))
        y += h + 12
    out += [box(20, y + 2, 186, 58, "ok", "macula ยังดี\n→ สายตาปกติระยะแรก", fs=11.5),
            box(214, y + 2, 186, 58, "ms", "ขั้วบวมเบียดจอตารอบ\n→ blind spot กว้างขึ้น", fs=11.5)]
    return fig("Papilledema: ความดันในกะโหลกเดินทางมาถึงขั้วประสาทตาอย่างไร",
               "ช่อง subarachnoid ต่อเนื่องไปหุ้ม **เส้นประสาทตาถึงหลังลูกตา** เมื่อ ICP สูง ความดันจึงกดใยประสาทตรง **lamina cribrosa** ทำให้การขนส่งในแอกซอนคั่ง ใยประสาทบวม ขั้วประสาทตานูน ขอบไม่ชัด และกด **central retinal vein** · "
               "เพราะความดันส่งไปเท่ากัน จึง **บวมสองข้าง** และสายตามักยังดีในระยะแรก — ต่างจาก optic neuritis ที่ตามัวตั้งแต่แรก",
               svg(420, 386, "ความดันในกะโหลกสูงส่งผ่าน CSF ในปลอกหุ้มเส้นประสาทตา กดใยประสาทและหลอดเลือดดำที่ขั้วประสาทตา ทำให้ขั้วบวม", *out))


def _fundus(cx, cy, pale=False):
    out = [circ(cx, cy, 70, "bx" if pale else "sk"), circ(cx - 34, cy, 13, "ms")]
    for d in ("M%d %d Q%d %d %d %d", ):
        pass
    vs = [("M%d %d Q%d %d %d %d" % (cx - 34, cy - 8, cx - 10, cy - 50, cx + 40, cy - 52)),
          ("M%d %d Q%d %d %d %d" % (cx - 34, cy + 8, cx - 10, cy + 50, cx + 40, cy + 52)),
          ("M%d %d Q%d %d %d %d" % (cx - 40, cy - 10, cx - 52, cy - 40, cx - 40, cy - 64)),
          ("M%d %d Q%d %d %d %d" % (cx - 40, cy + 10, cx - 52, cy + 40, cx - 40, cy + 64))]
    out += [path(v, "lbad w2") for v in vs]
    return out


def lp_retina():
    cA, cB = 105, 315
    out = [t(cA, 18, "Cotton wool spot", "sm b mid"), t(cB, 18, "Cherry red spot (CRAO)", "sm b mid"),
           line(210, 10, 210, 330, "lru da"),
           *_fundus(cA, 100),
           ell(cA + 18, 70, 12, 8, "muf"), ell(cA + 30, 124, 10, 7, "muf"),
           circ(cA + 22, 100, 5, "ms"),
           *_fundus(cB, 100, pale=True),
           circ(cB + 22, 100, 7, "badf"),
           line(cB + 22, 108, cB + 52, 172, "lmu"), t(cB + 52, 184, "fovea แดง", "xs mid tbad b"),
           line(cA + 30, 124, cA + 60, 172, "lmu"), t(cA + 60, 184, "ปื้นขาวฟุ้ง", "xs mid b"),
           ]
    a = [("bad", "arteriole เล็กอุด"), ("ms", "ใยประสาทชั้นผิวขาดเลือด"), ("ms", "axoplasm คั่ง → บวมขาว")]
    b = [("bad", "central retinal artery อุด"), ("ms", "จอตาชั้นในบวมขาวทั้งแผ่น"), ("ok", "fovea ไม่มีชั้นใน\nchoroid ยังเลี้ยง → แดง")]
    for x0, items in ((10, a), (220, b)):
        y = 196
        for k, (c, s) in enumerate(items):
            h = 40 if "\n" in s else 28
            out.append(box(x0, y, 190, h, c, s, fs=11.5))
            if k < 2:
                out.append(line(x0 + 95, y + h, x0 + 95, y + h + 8, "ln", "ah"))
            y += h + 10
    out.append(t(105, 330, "DM · HT · HIV", "xs mid i2"))
    out.append(t(315, 336, "ตาบอดทันทีไม่ปวด", "xs mid tbad b"))
    return fig("Cotton wool spot และ cherry red spot เกิดจากการขาดเลือดคนละระดับ",
               "**Cotton wool spot** — arteriole เล็กอุด ใยประสาทชั้นผิวขาดเลือด ของที่ขนส่งในแอกซอนจึงคั่งเป็นปื้นขาวขอบฟุ้ง · "
               "**Cherry red spot** — หลอดเลือดแดงใหญ่ของจอตาอุด จอตาชั้นในบวมขาวทั้งแผ่น แต่ **fovea บางและได้เลือดจาก choroid** จึงยังเห็นเป็นจุดแดงตัดกับพื้นซีด",
               svg(420, 344, "จอตาที่มี cotton wool spot จาก arteriole เล็กอุด เทียบกับ cherry red spot จาก central retinal artery occlusion", *out))
