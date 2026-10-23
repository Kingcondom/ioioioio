# -*- coding: utf-8 -*-
"""ภาพประกอบส่วนเติม neuro 9/10 (handout LP อ.ปองปวีณ์) และ neuro 21/10 (handout 2026 อ.เพชรรัตน์ + Delirium quiz)
ใช้โดย update_neuro_handouts.py · ดูภาพ: python3 artifact/tools/preview_figs.py figs_neuro_update --out <dir>"""
from svg import *


# ════════════════════════════════════════════════ LP (9/10)
def lp2_needle():
    """ภาพตัดด้านข้าง: เข็มเข้าระหว่าง L3–L4 มุม 15° เล็งสะดือ ผ่านชั้นต่าง ๆ · conus จบที่ L1"""
    out = []
    # ด้านหลัง (ผิวหนัง) อยู่ซ้าย ด้านหน้า (ท้อง) อยู่ขวา · ศีรษะอยู่บน
    out += [t(16, 18, "หลัง (ผิวหนัง)", "xs mu"), t(404, 18, "หน้า (ท้อง)", "xs mu end"),
            t(210, 18, "↑ ศีรษะ", "xs mu mid")]
    out += [rect(14, 28, 16, 330, "msf ns", 3)]
    levels = [("L1", 40), ("L2", 104), ("L3", 168), ("L4", 232), ("L5", 296)]
    for name, y in levels:
        out.append(rect(40, y + 6, 70, 30, "bx", 6))             # spinous process
        out.append(rect(236, y, 56, 50, "bx", 6))                # vertebral body
        out.append(t(264, y + 30, name, "sm b mid"))
    for _, y in levels[:-1]:
        out.append(rect(56, y + 38, 38, 24, "sk", 3))            # interspinous ligament
    out.append(line(36, 40, 36, 340, "lms w3"))                   # supraspinous
    out += [line(132, 40, 132, 350, "lac w3"),                    # ligamentum flavum
            rect(150, 40, 66, 320, "wa", 10),                     # thecal sac
            line(146, 40, 146, 350, "lbad w2")]                   # dura
    out += [path("M174 28 L174 70 Q183 92 192 70 L192 28", "lok w2"),
            t(198, 54, "conus", "xs tok"), t(198, 68, "~L1", "xs tok"),
            path("M178 84 L176 352 M183 90 L183 352 M188 84 L190 352", "lmu")]
    out += [line(4, 236, 196, 205, "lbad w3"), circ(196, 205, 3, "badf")]
    out += [t(22, 372, "ผิว", "xs mid mu"), t(132, 372, "LF", "xs mid tac"),
            t(183, 372, "ถุงดูรา", "xs mid twa")]
    out += [pill(8, 300, "pop = lig. flavum", "ac", "xs b mid tac", w=118, h=20),
            line(124, 304, 131, 226, "lac", "ah-ac")]
    out += [line(14, 398, 150, 398, "lmu w2"), t(160, 402, "ผิว → epidural ≈ 55 mm", "xs i2")]
    out += [t(358, 112, "CSF + cauda equina", "xs mid twa"), line(306, 118, 216, 160, "lwa", "ah-wa"),
            t(358, 192, "L3–4 หรือ L4–5", "sm b mid tac"), t(358, 208, "(ต่ำกว่า conus)", "xs mid mu"),
            t(358, 248, "เข็มทำมุม ~15°", "xs b mid tbad"), t(358, 262, "ขึ้นทางศีรษะ", "xs mid tbad"),
            t(358, 276, "เล็งไปทางสะดือ", "xs mid tbad"),
            t(358, 318, "bevel ขนานแนวยาว", "xs mid i2"), t(358, 332, "แยกเส้นใย", "xs mid i2"),
            t(358, 346, "ไม่ตัดขาด", "xs mid i2")]
    return fig("เข็มเดินทางอย่างไรจากผิวหนังถึง CSF",
               "แทงที่ช่อง **L3–L4 หรือ L4–L5** เพราะ conus medullaris ปกติจบที่ระดับ **L1** ต่ำกว่านั้นมีแต่รากประสาท (cauda equina) ลอยอยู่ใน CSF · "
               "เข็มผ่าน **ผิว → ใต้ผิว → supraspinous → interspinous → ligamentum flavum (รู้สึก pop) → epidural → ดูรา + arachnoid → subarachnoid** · "
               "ระยะผิวหนังถึง epidural ราว **55 mm (2/3 ของเข็ม)** · ทำมุมราว **15° ขึ้นทางศีรษะ เล็งสะดือ** เพื่อลอดใต้ spinous process ที่ชี้ลงล่าง · "
               "ภาพแนวคิด ไม่ได้ย่อส่วนจริง",
               svg(420, 410, "ภาพตัดด้านข้างกระดูกสันหลังส่วนเอว เข็มแทงระหว่าง L3 และ L4 ผ่านเอ็นและดูราเข้าสู่ช่อง CSF ต่ำกว่า conus", *out))


def lp2_pdph():
    """ขนาด/ชนิดของรูเข็มบนดูรา → ปริมาณ CSF รั่ว → PDPH"""
    out = [t(210, 16, "ดูรามองจากด้านหลัง (เส้นใยวิ่งตามยาว)", "sm b mid")]
    xs = [(18, "ตัด: bevel ขวางเส้นใย", "bad", "รูกว้าง ขอบขาด"), (152, "ตัด: bevel ขนานเส้นใย", "ms", "รูเป็นร่อง ปิดง่ายกว่า"),
          (286, "atraumatic (pencil-point)", "ok", "แหวกเส้นใย ปิดเอง")]
    for x, title, c, cap in xs:
        out.append(rect(x, 26, 116, 120, "sk", 8))
        for k in range(7):
            out.append(line(x + 14 + k * 15, 32, x + 14 + k * 15, 140, "lmu"))
        out.append(t(x + 58, 162, title, "xs b mid t" + c))
        out.append(t(x + 58, 176, cap, "xs mid i2"))
    # holes
    out += [ell(76, 86, 30, 9, "bad"), ell(210, 86, 6, 22, "ms"), ell(344, 86, 4, 12, "ok")]
    chain = [("ms", "รูดูรา → CSF รั่วออก epidural เร็วกว่าสร้างทดแทน", 196),
             ("wa", "ความดัน/ปริมาตร CSF ลด → สมองเสียแรงพยุง", 240),
             ("bad", "ลุกนั่ง/ยืน → สมองทรุด ดึงโครงสร้างไวปวด\n+ หลอดเลือดดำขยายชดเชย → ปวดศีรษะตามท่า", 284)]
    for c, s, y in chain:
        h = 46 if "\n" in s else 32
        out.append(box(30, y, 360, h, c, s, fs=12))
    out += [line(210, 228, 210, 238, "ln", "ah"), line(210, 272, 210, 282, "ln", "ah"),
            line(210, 330, 210, 342, "ln", "ah"),
            box(10, 344, 196, 64, "ok", "ขั้นที่ 1 (ส่วนใหญ่หายเอง)\nนอนพัก น้ำ ยาแก้ปวด\nคาเฟอีน", fs=11.5),
            box(214, 344, 196, 64, "ok", "ขั้นที่ 2 ถ้าไม่ดีขึ้น\nepidural blood patch\nอุดรู + ดันความดันกลับ", fs=11.5)]
    return fig("ทำไมชนิดเข็มและทิศของ bevel กำหนดความเสี่ยง post-LP headache",
               "ดูรามีเส้นใยวิ่งตามแนวยาวของลำตัว · เข็มปลายตัด (Quincke) ที่หัน bevel **ขวาง** เส้นใยจะตัดเส้นใยขาดเป็นรูกว้าง · หัน bevel **ขนาน** (หันขึ้นเพดานในท่านอนตะแคง ตามสไลด์) เส้นใยถูกแหวกเป็นร่องที่หดปิดได้ · "
               "เข็ม **atraumatic (pencil-point)** ดันเส้นใยแยกออกโดยไม่ตัด จึงรั่วน้อยที่สุด · ยิ่งรูเล็ก CSF รั่วน้อย ความดันไม่ตก สมองไม่ทรุด · "
               "การรักษาเป็นขั้นบันได: ประคับประคองก่อน ถ้าไม่ดีขึ้นจึงทำ **epidural blood patch** (เรื่องเข็ม atraumatic และการรักษาอิง ICHD-3 และ Nath S, Lancet 2018 — ไม่อยู่ในสไลด์ อ.ปองปวีณ์)",
               svg(420, 416, "เปรียบเทียบรูบนดูราจากเข็มตัดที่หัน bevel ขวางหรือขนานเส้นใย และเข็ม atraumatic แล้วโยงไปกลไกปวดศีรษะหลังเจาะหลัง", *out))


def _skull(cx, top, high_above=False, block=False, mass=False):
    o = [ell(cx, top + 52, 70, 50, "bx")]
    o.append(ell(cx, top + 50, 22, 18, "wa" if not high_above else "wa"))   # ventricle
    if high_above:
        o.append(ell(cx, top + 50, 34, 26, "wa"))
    if mass:
        o.append(circ(cx - 34, top + 40, 14, "bad"))
    # aqueduct / outflow
    o.append(rect(cx - 5, top + 76, 10, 34, "wa", 3))
    if block:
        o.append(line(cx - 14, top + 92, cx + 14, top + 92, "lbad w5"))
    # spinal canal
    o.append(rect(cx - 12, top + 110, 24, 130, "wa", 6))
    return o


def lp2_hydro():
    """communicating (IIH/crypto) vs non-communicating/mass — ทำไมเจาะได้/ห้ามเจาะ"""
    out = [t(105, 16, "ทางเดิน CSF ต่อถึงกัน", "sm b mid tok"), t(105, 30, "IIH · cryptococcal meningitis", "xs mid i2"),
           t(315, 16, "ทางเดิน CSF ถูกปิด / มีก้อน", "sm b mid tbad"), t(315, 30, "obstructive hydrocephalus · mass", "xs mid i2")]
    out += _skull(105, 36) + _skull(315, 36, high_above=True, block=True, mass=True)
    out += [line(210, 8, 210, 300, "lru da")]
    # pressures
    out += [pill(16, 56, "↑", "ms", "xs b mid tms", w=26), pill(16, 222, "↑", "ms", "xs b mid tms", w=26),
            t(105, 296, "ความดันบน = ล่าง", "xs b mid tok"),
            pill(226, 56, "↑↑", "bad", "xs b mid tbad", w=30), pill(226, 222, "↓", "wa", "xs b mid twa", w=26),
            t(315, 296, "ความดันบน ≫ ล่าง หลังเจาะ", "xs b mid tbad")]
    # needle arrows
    out += [line(56, 240, 90, 240, "lwa w2", "ah-wa"), t(48, 256, "LP", "xs b tac"),
            line(266, 240, 300, 240, "lwa w2", "ah-wa"), t(258, 256, "LP", "xs b tac")]
    out += [path("M300 120 L306 146", "lbad w2", "ah-bad"), t(336, 150, "สมองถูกดูดลง", "xs tbad"),
            t(336, 164, "(tonsil/uncus)", "xs tbad")]
    out += [box(10, 308, 196, 58, "ok", "ระบาย CSF = ลดความดัน\nทั้งระบบ → รักษาได้\n(therapeutic release)", fs=11.5),
            box(214, 308, 196, 58, "bad", "ระบายจากล่าง = เกิด\nแรงดันต่าง → herniation\n(absolute contraindication)", fs=11.5)]
    return fig("ทำไม IIH และ cryptococcal meningitis เจาะระบายได้ แต่ obstructive hydrocephalus ห้ามเจาะ",
               "ใน **IIH** และ **cryptococcal meningitis** ช่อง CSF ในกะโหลกยังต่อถึงช่องไขสันหลัง ความดันสูงเท่ากันทั้งระบบ การปล่อย CSF จากหลังจึง **ลดความดันทั้งระบบ** ไม่เกิดแรงดันต่าง · "
               "ใน **non-communicating (obstructive) hydrocephalus** หรือ **ก้อนที่มี mass effect** ทางเดินระหว่างบนกับล่างถูกปิด ปล่อยน้ำจากล่างทำให้ความดันล่างตก แต่ข้างบนยังสูง → **สมองถูกดันลงผ่านช่องแคบ (herniation)** · "
               "ภาพแนวคิด",
               svg(420, 374, "เปรียบเทียบกะโหลกที่ทางเดิน CSF ต่อกันซึ่งเจาะระบายได้ กับกะโหลกที่ทางเดินถูกปิดหรือมีก้อนซึ่งเจาะแล้วเกิด herniation", *out))


def lp2_crypto():
    """cryptococcal capsule อุด arachnoid granulation → ICP สูง → LP ซ้ำ / shunt"""
    out = []
    chain = [("ac", "Cryptococcus ในช่อง subarachnoid\n(ภูมิคุ้มกันต่ำ เช่น HIV CD4 < 100)", 10, 46),
             ("ms", "แคปซูล polysaccharide + เชื้อจำนวนมาก\nไปอุดทางดูดกลับ CSF ที่ arachnoid granulation", 74, 46),
             ("wa", "CSF สร้างตามปกติ แต่ดูดกลับไม่ทัน\n→ ความดันสูงแบบ communicating", 138, 46),
             ("bad", "Opening pressure มัก > 25 cmH₂O\nปวดศีรษะ ตามัว CN VI · ตายจาก ICP สูง", 202, 46)]
    for c, s, y, h in chain:
        out.append(box(20, y, 380, h, c, s, fs=12))
    for y in (56, 120, 184):
        out.append(line(210, y, 210, y + 16, "ln", "ah"))
    out += [line(210, 248, 210, 264, "ln", "ah"),
            box(20, 266, 380, 46, "ok", "Therapeutic LP: ระบาย CSF จน OP < 20 หรือลดลงครึ่งหนึ่ง\nทำซ้ำทุกวันจนความดันคงที่", fs=12),
            line(210, 312, 210, 326, "ln", "ah"),
            box(20, 328, 380, 40, "ms", "ยังสูงต่อเนื่องแม้ระบายซ้ำ → พิจารณา shunt ถาวร (ลายมือในสไลด์)", fs=12)]
    return fig("Cryptococcal meningitis: ทำไมการเจาะหลังเป็นการรักษา",
               "ลายมือบนสไลด์ อ.ปองปวีณ์ เขียนว่า **\"ไปอุด\"** ข้างคำว่า Cryptococcal และ **\"HIV → permanent shunt\"** · "
               "กลไก: เชื้อและแคปซูล polysaccharide ไปอุด **arachnoid granulation** CSF จึงดูดกลับไม่ทันทั้งที่ทางเดินยังต่อกัน (communicating) ความดันสูงทั้งระบบ · "
               "การระบายออกทางหลังจึง **ปลอดภัยและเป็นการรักษาที่ลดอัตราตาย** · เกณฑ์ระบายจนความดัน < 20 cmH₂O หรือลดลง 50% และเจาะซ้ำทุกวัน อิง WHO 2022 / IDSA (ไม่อยู่ในสไลด์)",
               svg(420, 376, "ลำดับเหตุการณ์จากเชื้อ cryptococcus อุดทางดูดกลับ CSF ทำให้ความดันสูง และการรักษาด้วยการเจาะระบายซ้ำหรือใส่ shunt", *out))


def _tube3(x, y, fill, sup, clot=False):
    o = [rect(x, y, 22, 92, "bx", 10), rect(x + 2, y + 28, 18, 62, fill + " ns", 8), rect(x + 2, y + 12, 18, 16, sup + " ns", 2)]
    if clot:
        o.append(circ(x + 11, y + 78, 5, "badf"))
    return o


def lp2_tubes():
    out = [t(105, 16, "Traumatic tap", "sm b mid tac"), t(315, 16, "Subarachnoid hemorrhage", "sm b mid tbad")]
    fills = ["badf", "bad", "bx"]
    for k, f in enumerate(fills):
        out += _tube3(46 + k * 40, 30, f, "bx", clot=(k == 0))
        out.append(t(57 + k * 40, 140, str(k + 1), "xs mid mu"))
    for k in range(3):
        out += _tube3(256 + k * 40, 30, "badf", "msf")
        out.append(t(267 + k * 40, 140, str(k + 1), "xs mid mu"))
    out += [line(210, 8, 210, 300, "lru da")]
    rows = [("สีหลอด 1 → 3", "จางลงเรื่อย ๆ", "แดงเท่าเดิม"),
            ("ก้อนเลือด", "แข็งตัวได้", "ไม่แข็งตัว"),
            ("ปั่นแล้วส่วนบน", "ใส", "เหลือง (xanthochromia)"),
            ("เวลา", "เลือดเพิ่งออกขณะเจาะ", "เลือดค้าง ≥ ~12 ชม.")]
    y = 160
    for a, b, c in rows:
        out += [t(210, y, a, "xs b mid mu"), t(105, y + 16, b, "xs mid i2"), t(315, y + 16, c, "xs mid i2")]
        y += 36
    out += [box(20, 306, 380, 46, "sk", "แก้ค่า: ลบ WBC 1 ตัว ต่อ RBC 500–1,000\nprotein ≈ 1–2 mg/dL ต่อ RBC 1,000 (ค่าตามสไลด์ 1.1–1.9)", fs=12)]
    return fig("Traumatic tap กับ SAH: อ่านจากหลอดสามหลอด",
               "**Traumatic tap** — เข็มเฉี่ยวหลอดเลือดดำใน epidural ขณะเจาะ เลือดปนมากในหลอดแรกแล้ว **จางลงเรื่อย ๆ** และยังมี fibrinogen จึง **แข็งตัวได้** · ปั่นแล้วส่วนบนใส เพราะ RBC ยังไม่แตก · "
               "**SAH** — เลือดผสมกับ CSF ทั้งช่องมาก่อน **ทุกหลอดแดงเท่ากัน** ไม่แข็งตัวเพราะ fibrin ถูกสลายในช่อง CSF ไปแล้ว และ macrophage เปลี่ยน heme เป็น bilirubin → **xanthochromia** · "
               "ใช้สูตรแก้ค่า WBC/protein เมื่อมีเลือดปน (สไลด์ อ.ปองปวีณ์ อ้าง PMC5607637)",
               svg(420, 360, "หลอด CSF สามหลอด traumatic tap เลือดจางลงจากหลอดแรกถึงหลอดสาม ส่วน SAH แดงเท่ากันทุกหลอดและส่วนบนเหลือง", *out))


# ════════════════════════════════════════════════ ACS (21/10)
def acs2_ras():
    out = [box(110, 8, 200, 44, "ac", "Lateral hypothalamus\nOrexin (hypocretin)", fs=12)]
    nuc = [("Locus coeruleus", "Norepinephrine", 10), ("Raphe nuclei", "Serotonin", 112),
           ("Tuberomammillary", "Histamine", 214), ("PPT / LDT", "Acetylcholine", 316)]
    for name, nt, x in nuc:
        out.append(box(x, 86, 94, 46, "bx", name + "\n" + nt, fs=10.5))
        out.append(line(210, 52, x + 47, 84, "lac", "ah-ac"))
    out += [box(60, 166, 300, 36, "wa", "Thalamus → เปลือกสมองทั้งสองซีก", fs=12)]
    for _, _, x in nuc:
        out.append(line(x + 47, 132, min(max(x + 47, 90), 330), 164, "ln", "ah"))
    out += [t(210, 228, "ยาหรือภาวะที่ไปตัดแต่ละสาย", "sm b mid")]
    rows = [("ยาแก้แพ้รุ่นเก่า", "ต้าน histamine → ง่วง", "ms"),
            ("DORA (suvorexant, lemborexant)", "ต้าน orexin → ยานอนหลับ", "ok"),
            ("ขาด orexin", "narcolepsy", "ms"),
            ("Anticholinergic · delirium", "ACh ↓ + dopamine ↑ → สมาธิเสีย", "bad")]
    y = 240
    for a, b, c in rows:
        out += [rect(10, y, 400, 30, c, 6), t(20, y + 20, a, "xs b"), t(400, y + 20, b, "xs end")]
        y += 36
    return fig("RAS: สวิตช์ปลุกที่ใช้สารสื่อประสาทสี่ชนิด และ orexin เป็นตัวคุม",
               "RAS ทอดจาก medulla ผ่าน pons ถึง midbrain ประกอบด้วยกลุ่มนิวเคลียสหลักสี่กลุ่ม — **locus coeruleus (NE) · raphe (serotonin) · tuberomammillary (histamine) · pedunculopontine/laterodorsal tegmentum (ACh)** — "
               "ส่งสัญญาณผ่าน thalamus ไปปลุกเปลือกสมองทั้งสองซีก · **orexin จาก lateral hypothalamus กระตุ้นทุกกลุ่ม** · "
               "จึงอธิบายได้ว่ายาแก้แพ้รุ่นเก่าทำให้ง่วง DORA ใช้เป็นยานอนหลับ และ **การขาด ACh ร่วมกับ dopamine เด่นเกิน** ทำให้ RAS เสียหน้าที่ใน delirium (สไลด์ อ.เพชรรัตน์)",
               svg(420, 388, "orexin กระตุ้นนิวเคลียสสี่กลุ่มของ RAS ซึ่งปลุกเปลือกสมองผ่าน thalamus และยาหรือภาวะที่ไปขัดแต่ละสาย", *out))


def acs2_twoprocess():
    def panel(y0, title, tc, s_pts, c_pts, sleep_bars, note):
        o = [t(10, y0 + 12, title, "sm b " + tc), rect(36, y0 + 20, 370, 110, "bx", 6)]
        # night shading
        o.append(rect(36 + 370 * 15 / 24, y0 + 20, 370 * 9 / 24, 110, "sk ns", 0))
        o.append(poly([(36 + 370 * h / 24, y0 + 130 - v) for h, v in s_pts], "lms w3"))
        o.append(poly([(36 + 370 * h / 24, y0 + 130 - v) for h, v in c_pts], "lac w2 da"))
        for a, b in sleep_bars:
            o.append(rect(36 + 370 * a / 24, y0 + 134, 370 * (b - a) / 24, 8, "wa", 2))
        o.append(t(10, y0 + 142, "หลับ", "xs mu"))
        o.append(t(221, y0 + 160, note, "xs mid i2"))
        return o
    out = [pill(60, 4, "S = แรงดันง่วงสะสม", "ms", "xs b mid tms", w=140), pill(220, 4, "C = สัญญาณตื่นตามนาฬิกา", "ac", "xs b mid tac", w=170)]
    out += panel(30, "ปกติ", "tok",
                 [(0, 20), (15, 95), (16, 80), (19, 50), (22, 30), (24, 20)],
                 [(0, 40), (4, 60), (8, 80), (12, 92), (14, 90), (16, 70), (18, 45), (21, 22), (24, 30)],
                 [(15, 24)], "S สูงสุดตอนกลางคืน + C ตก → หลับยาวต่อเนื่อง")
    out += panel(206, "Delirium / ICU", "tbad",
                 [(0, 50), (3, 40), (5, 55), (8, 45), (11, 60), (13, 45), (16, 55), (19, 45), (22, 55), (24, 50)],
                 [(0, 58), (6, 62), (12, 66), (18, 60), (24, 58)],
                 [(2, 3.5), (6, 7), (10, 11.5), (13.5, 14.5), (17, 18), (21, 22)], "หลับเป็นช่วงสั้น ๆ ทั้งวัน · กลางวันง่วง กลางคืนตื่น")
    out += [t(36, 392, "07 น.", "xs mu"), t(267, 392, "22 น.", "xs mu mid"), t(406, 392, "07 น.", "xs mu end"), t(340, 32 + 30, "กลางคืน", "xs mu mid")]
    return fig("Two-process model: ทำไมผู้ป่วย delirium หลับกลางวัน ตื่นกลางคืน",
               "การหลับเกิดจาก **process S** (แรงดันง่วงที่สะสมระหว่างตื่นและถูกล้างระหว่างหลับ) ทำงานร่วมกับ **process C** (สัญญาณตื่นตามนาฬิกาชีวภาพ suprachiasmatic nucleus–melatonin) · "
               "ใน delirium/ICU แสงตลอดวัน เสียง การปลุกบ่อย ยา และการอักเสบ **ทำให้ C แบนลง และ S ไม่เคยสะสมพอ** การนอนจึงแตกเป็นช่วง **REM และ slow-wave sleep ลดลง** และอาจกลับขั้วเป็นหลับกลางวัน (Levinsohn 2025 ในสไลด์ อ.เพชรรัตน์) · กราฟแนวคิด ไม่ใช่ข้อมูลจริง",
               svg(420, 400, "กราฟแนวคิด process S และ process C ใน 24 ชั่วโมง เทียบคนปกติที่หลับยาวกลางคืน กับผู้ป่วย delirium ที่หลับเป็นช่วงสั้นทั้งวัน", *out))


def acs2_labalgo():
    out = [box(110, 6, 200, 40, "ac", "Delirium (CAM +)\nประวัติ + ตรวจร่างกายก่อน", fs=12)]
    cols = [(10, "ok", "ไม่มีไข้ ไม่มี meningeal\nsign ไม่มี focal sign"),
            (146, "ms", "มีไข้ หรือ\nmeningeal sign"),
            (282, "bad", "Focal sign\nหรือชัก")]
    for x, c, s in cols:
        out.append(box(x, 76, 128, 46, c, s, fs=11))
        out.append(line(210, 46, x + 64, 74, "ln", "ah"))
    tests = [(10, "Glucose · BUN · Na/K\nCa · LFT · ABG\nEKG\nToxicology screen\nCBC · CXR\nUA + culture · H/C"),
             (146, "+ ตรวจกลุ่มซ้าย\n+ CSF (LP)\n(CT ก่อนถ้ามีข้อบ่งชี้)"),
             (282, "+ ตรวจกลุ่มซ้าย\nCT หรือ MRI brain\nEEG")]
    for x, s in tests:
        n = s.count("\n") + 1
        out.append(box(x, 140, 128, 20 + 15 * n, "bx", s, fs=10.5))
        out.append(line(x + 64, 122, x + 64, 138, "ln", "ah"))
    out += [box(10, 268, 400, 44, "sk", "หาเหตุที่แก้ได้ก่อนเสมอ: DELIRIUM — Drugs · Electrolytes · Lack of drugs\nInfection · Reduced sensory · Intracranial · Urinary/fecal · Myocardial/lung", fs=10.5)]
    return fig("ส่งตรวจอะไรในผู้ป่วย delirium — แยกตามไข้ คอแข็ง และอาการเฉพาะที่",
               "ตามสไลด์ อ.เพชรรัตน์ (อิง Marcantonio NEJM 2017) **ทุกรายต้องได้ชุดพื้นฐาน** — เมแทบอลิก EKG สารพิษ และหาการติดเชื้อทั่วร่างกาย · "
               "**มีไข้หรือ meningeal sign** เพิ่ม **CSF** เพราะ meningitis/encephalitis อาจมาด้วยสับสนอย่างเดียว · **focal sign หรือชัก** เพิ่ม **ภาพสมองและ EEG** (non-convulsive status) · "
               "กล่องล่างคือตัวช่วยจำ DELIRIUM ของสาเหตุที่แก้ได้",
               svg(420, 320, "แผนภูมิการส่งตรวจผู้ป่วย delirium แบ่งสามกลุ่มตามไข้ meningeal sign และ focal sign", *out))


def acs2_bobbing():
    def trace(y0, title, tc, pts, lab, where):
        o = [t(10, y0 + 12, title, "sm b " + tc), line(60, y0 + 30, 400, y0 + 30, "lmu da"),
             t(54, y0 + 34, "กลาง", "xs mu end"), t(54, y0 + 92, "ลง", "xs mu end")]
        o.append(poly([(60 + x, y0 + 30 + v) for x, v in pts], "lbad w3" if tc == "tbad" else "lac w3"))
        o += [t(230, y0 + 116, lab, "xs mid i2"), t(230, y0 + 130, where, "xs b mid " + tc)]
        return o
    bob = [(0, 0), (30, 0), (38, 60), (60, 60), (150, 0), (190, 0), (198, 60), (220, 60), (310, 0), (340, 0)]
    dip = [(0, 0), (30, 0), (110, 60), (124, 60), (130, 0), (190, 0), (270, 60), (284, 60), (290, 0), (340, 0)]
    out = trace(4, "Ocular bobbing", "tbad", bob, "กระตุกลงเร็ว → ลอยกลับช้า · ไม่มีตาเคลื่อนแนวนอน", "รอยโรคที่ pons (infarct/hemorrhage) · HIE")
    out += trace(150, "Ocular dipping", "tac", dip, "เคลื่อนลงช้า → เด้งกลับเร็ว", "เปลือกสมองเสียทั่ว: HIE · status epilepticus · CJD · head trauma")
    out += [t(400, 296, "เวลา →", "xs mu end")]
    return fig("Ocular bobbing กับ ocular dipping: ดูว่าช่วงไหนเร็ว",
               "**Bobbing** — ตา **กระตุกลงเร็วพร้อมกันสองข้าง แล้วลอยกลับช้า ๆ** ร่วมกับ **ไม่มีการกลอกตาแนวนอนทั้งที่เกิดเองและจากรีเฟล็กซ์** เพราะศูนย์ควบคุมแนวนอน (PPRF/นิวเคลียส VI) ที่ pons เสีย เหลือแต่ระบบแนวดิ่งจาก midbrain → **pontine lesion** · "
               "**Dipping** — **ลงช้าแล้วเด้งกลับเร็ว** พบในสมองเสียหายทั่ว เช่น **ขาดออกซิเจน (HIE) ชักต่อเนื่อง CJD** ก้านสมองมักยังดี (สไลด์ อ.เพชรรัตน์ อ้าง Allen C, Neurohospitalist 2025) · กราฟแนวคิด",
               svg(420, 304, "กราฟตำแหน่งตาเทียบเวลา ocular bobbing ลงเร็วขึ้นช้า และ ocular dipping ลงช้าขึ้นเร็ว", *out))


def acs2_dts():
    out = [line(30, 40, 400, 40, "ln w2", "ah"), t(400, 30, "เวลาหลังดื่มแก้วสุดท้าย", "xs end mu")]
    ticks = [(0, "0"), (24, "24 ชม."), (48, "48"), (72, "72"), (96, "96")]
    X = lambda h: 30 + h * 3.6
    for h, s in ticks:
        out += [line(X(h), 36, X(h), 44, "ln"), t(X(h), 58, s, "xs mid mu")]
    bars = [(6, 36, "ms", "Minor withdrawal: สั่น เหงื่อ ใจสั่น นอนไม่หลับ"),
            (12, 48, "ac", "Alcoholic hallucinosis: ภาพหลอน แต่ยังรู้ตัว"),
            (12, 48, "bad", "Withdrawal seizure (GTC)"),
            (48, 96, "bad", "Delirium tremens: สับสน + ไข้ ชีพจรเร็ว BP สูง")]
    y = 70
    for a, b, c, s in bars:
        out += [rect(X(a), y, X(b) - X(a), 18, c, 4), t(X(a), y + 32, s, "xs")]
        y += 46
    out += [box(10, 260, 400, 60, "sk", "โจทย์ในห้อง: หยุดสุรา 3 วัน (72 ชม.) + สับสน สั่น ภาพหลอน\nเหงื่อ ไข้ 40 °C ชีพจร 110 BP 160/100 = autonomic hyperactivity\n→ อยู่ในช่วงของ delirium tremens", fs=11)]
    return fig("Alcohol withdrawal เกิดอะไรเมื่อไร",
               "เอทานอลกระตุ้น **GABA-A** และกด **NMDA** อยู่ตลอด สมองจึงปรับตัวลดตัวรับ GABA และเพิ่มตัวรับ NMDA · เมื่อหยุดดื่ม แรงยับยั้งหายไปทันทีขณะที่ระบบกระตุ้นยังสูง → **สั่น ชัก ภาพหลอน และ sympathetic ทำงานเกิน** · "
               "**Delirium tremens** มักเริ่ม **48–96 ชั่วโมง** หลังหยุดดื่ม ต่างจาก alcoholic hallucinosis ที่ยังรู้ตัวดี · ช่วงเวลาเป็นค่าโดยประมาณตามตำรา (ไม่อยู่ในสไลด์) · "
               "การรักษาหลักคือ **benzodiazepine** + thiamine ก่อนกลูโคส",
               svg(420, 328, "เส้นเวลาของอาการถอนสุรา จากสั่นใน 6 ชั่วโมง ถึง delirium tremens ที่ 48 ถึง 96 ชั่วโมง", *out))
