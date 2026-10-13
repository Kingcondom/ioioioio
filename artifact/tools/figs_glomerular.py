# -*- coding: utf-8 -*-
"""ภาพประกอบคาบ nephro 14 Approach to glomerular disease (ใช้ใน build_glomerular.py)"""
from svg import *


def barrier():
    gaps = [200, 322, 450, 541]
    endo, x = [], 160
    for gx in gaps:
        endo.append(rect(x, 82, gx - 6 - x, 16, "sk", 4)); x = gx + 6
    endo.append(rect(x, 82, 585 - x, 16, "sk", 4))
    feet = [rect(164 + 41 * k, 132, 30, 22, "ac", 7) for k in range(10)]
    slits = [line(196 + 41 * k, 136, 203 + 41 * k, 136, "lac w2") for k in range(10)]
    return svg(600, 322, "ตะแกรงกรองของ glomerulus 3 ชั้น น้ำผ่านได้ albumin ถูกผลักด้วยประจุลบ RBC ผ่าน GBM ไม่ได้",
        rect(160, 14, 425, 62, "bad", 6), t(575, 30, "ด้านเลือด", "xs mu end"),
        *endo, line(160, 79, 585, 79, "lms dt w2"),
        rect(160, 104, 425, 22, "ms", 3),
        *feet, *slits,
        rect(160, 160, 425, 58, "wa", 6), t(575, 210, "ด้านปัสสาวะ", "xs mu end"),
        # โมเลกุล
        circ(200, 26, 4, "waf"), circ(191, 40, 4, "waf"), circ(207, 46, 4, "waf"),
        line(200, 54, 200, 196, "lwa w2", "ah-wa"), circ(192, 204, 4, "waf"), circ(208, 208, 4, "waf"),
        t(214, 32, "น้ำ + ของเล็ก", "sm b twa"), t(214, 47, "ผ่านได้", "sm twa"),
        circ(322, 38, 11, "msf"), t(322, 43, "−", "b mid tpa"),
        line(322, 51, 322, 74, "lmu w2", "ah-mu"), t(332, 72, "✕", "b tbad"),
        t(340, 32, "albumin (−)", "sm b"), t(340, 47, "ถูกประจุลบผลัก", "sm i2"),
        ell(450, 34, 15, 7, "badf"), line(450, 43, 450, 101, "lmu w2", "ah-mu"), t(460, 100, "✕", "b tbad"),
        t(472, 32, "RBC", "sm b"), t(472, 47, "ผ่าน GBM ไม่ได้", "sm i2"),
        # ป้ายชั้น
        t(10, 48, "เลือดในหลอดฝอย", "sm b"),
        t(10, 89, "① Endothelium", "sm b"), t(10, 102, "รู fenestra + ประจุลบ", "xs mu"),
        t(10, 120, "② GBM · collagen IV", "sm b"),
        t(10, 142, "③ Podocyte", "sm b"), t(10, 155, "foot process + slit", "xs mu"),
        t(10, 190, "ช่อง Bowman", "sm b"), t(10, 204, "= น้ำกรอง", "xs mu"),
        box(10, 236, 186, 74, "ac", "podocyte / slit พัง\n→ albumin รั่ว\n= nephrotic", fs=12),
        box(207, 236, 186, 74, "ms", "GBM ฉีก / อักเสบ\n→ RBC ลอดออก\n= nephritic", fs=12),
        box(404, 236, 186, 74, "sk", "ประจุลบหาย\n→ albumin ผ่านง่าย\n(selective proteinuria)", fs=12))


def twomech():
    kids = lambda x, items: [line(x + 8, 126, x + 8, items[-1][0] + items[-1][1] / 2, "ln")] + [
        p for (y, h, c, s) in items for p in (line(x + 8, y + h / 2, x + 22, y + h / 2, "ln", "ah"), box(x + 24, y, 166, h, c, s, fs=12.5))]
    return svg(400, 360, "การบาดเจ็บของ glomerulus ให้อาการผ่านสองกลไก คือ ตะแกรงรั่ว กับ GFR ลดลง",
        box(110, 8, 180, 40, "sk", "Glomerular injury", "b"),
        line(170, 48, 100, 78, "ln", "ah"), line(230, 48, 300, 78, "ln", "ah"),
        box(8, 80, 186, 46, "ac", "ตะแกรงรั่ว\nloss of barrier", "b", fs=12.5),
        box(206, 80, 186, 46, "ms", "กรองได้น้อยลง\nGFR ↓", "b", fs=12.5),
        *kids(4, [(144, 48, "bx", "Proteinuria\n→ ปัสสาวะเป็นฟอง"), (204, 48, "bad", "Hematuria\n→ สีน้ำล้างเนื้อ / โค้ก")]),
        *kids(202, [(144, 36, "bx", "Azotemia (BUN, Cr ↑)"), (190, 36, "bx", "Oliguria"),
                    (236, 48, "ms", "เกลือ + น้ำคั่ง\n→ บวม + BP ↑")]),
        t(200, 316, "รั่วเด่น (ฝั่งซ้าย) = nephrotic", "sm mid tac"),
        t(200, 336, "GFR ลด + hematuria เด่น (ฝั่งขวา) = nephritic", "sm mid tms"))


def dipstick():
    def tube(x, y):
        return (path("M%d %d V%d a11 11 0 0 0 22 0 V%d" % (x, y, y + 36, y), "ln") +
                path("M%d %d V%d a10 10 0 0 0 20 0 V%d Z" % (x + 1, y + 16, y + 36, y + 16), "ruf") +
                circ(x + 7, y + 30, 1.6, "paf") + circ(x + 14, y + 38, 1.6, "paf") + circ(x + 10, y + 24, 1.6, "paf"))
    return svg(560, 250, "dipstick ตรวจเจอเฉพาะ albumin ส่วน SSA ตกตะกอนโปรตีนทุกชนิด รวมถึง light chain",
        t(185, 20, "Dipstick", "b mid"), t(185, 36, "แผ่นสีเปลี่ยนเมื่อจับ albumin", "xs mu mid"),
        t(430, 20, "SSA (sulfosalicylic acid)", "b mid"), t(430, 36, "กรดทำโปรตีนทุกชนิดตกตะกอน", "xs mu mid"),
        line(300, 12, 300, 176, "lru da"), line(10, 112, 550, 112, "lru"),
        circ(40, 66, 11, "msf"), t(40, 96, "albumin", "xs mid"),
        rect(100, 56, 170, 22, "sk", 4), rect(232, 59, 32, 16, "ok", 3), ar(56, 67, 96, 67, "lmu", "ah-mu"),
        t(248, 98, "บวก ✓", "sm mid tok b"),
        tube(380, 50), t(412, 74, "ขุ่น = บวก ✓", "sm tok b"),
        ell(40, 140, 13, 5, "inkf"), ell(40, 152, 13, 5, "inkf"), t(40, 174, "light chain", "xs mid"),
        rect(100, 136, 170, 22, "sk", 4), rect(232, 139, 32, 16, "ms", 3), ar(56, 147, 96, 147, "lmu", "ah-mu"),
        t(248, 176, "ลบ ✗", "sm mid tbad b"),
        tube(380, 128), t(412, 152, "ขุ่น = บวก ✓", "sm tok b"),
        box(10, 190, 540, 52, "ac", "dipstick ลบหรือ 1+ แต่ SSA / 24-h protein สูง → มีโปรตีนที่ไม่ใช่ albumin\n→ คิดถึง light chain (multiple myeloma) · ส่ง serum/urine protein electrophoresis", fs=12))


def protsrc():
    tub = "M148 150 H330 V250 H380 V170 H520 V292"
    return svg(600, 320, "โปรตีนในปัสสาวะมาจาก 4 กลไก glomerular tubular overflow และ functional",
        circ(100, 150, 48, "bx"), circ(86, 136, 12, "bad"), circ(112, 134, 12, "bad"), circ(120, 158, 12, "bad"),
        circ(96, 166, 12, "bad"), circ(78, 156, 11, "bad"),
        line(8, 150, 50, 150, "lbad w3", "ah-bad"), t(10, 140, "เลือด", "xs mu"),
        path(tub, "lru w5"), path(tub, "lwa w2", "ah-wa"),
        t(240, 142, "proximal tubule", "xs mu mid"), t(532, 296, "ปัสสาวะ", "sm b"),
        pill(10, 30, "① Glomerular", "ac"), t(10, 72, "ตะแกรงรั่ว · albumin", "xs i2"), t(10, 86, "ได้มากถึง > 3.5 g/d", "xs i2"),
        pill(200, 100, "② Tubular", "ac", w=86), t(170, 174, "PT ดูดโปรตีนเล็กกลับไม่ได้", "xs i2"),
        t(170, 188, "β2-microglobulin · < 1–2 g/d", "xs i2"),
        pill(10, 214, "③ Overflow", "bad", "sm b mid tbad"), t(10, 252, "โปรตีนเล็กในเลือดล้น", "xs i2"),
        t(10, 266, "light chain · myoglobin · Hb", "xs i2"),
        pill(392, 30, "④ Functional / orthostatic", "ms", "sm b mid tms"), t(392, 72, "แรงดัน/การไหลผ่าน glomerulus", "xs i2"),
        t(392, 86, "เปลี่ยนชั่วคราว: ออกกำลัง ไข้ HF ยืน", "xs i2"), t(392, 100, "< 1–2 g/d · ตะกอนปกติ", "xs i2"),
        path("M390 50 Q260 40 152 116", "lms da", "ah-ms"))


def redurine():
    return svg(400, 392, "ปัสสาวะสีแดง ปั่นแล้วดูว่าสีแดงอยู่ที่ตะกอนหรือน้ำส่วนบน แล้วตรวจ dipstick heme",
        box(110, 8, 180, 36, "bad", "ปัสสาวะสีแดง", "b"), line(200, 44, 200, 62, "ln", "ah"),
        box(110, 64, 180, 36, "sk", "ปั่นปัสสาวะ (centrifuge)", fs=12.5),
        line(160, 100, 96, 128, "ln", "ah"), line(240, 100, 304, 128, "ln", "ah"),
        box(10, 130, 172, 48, "bad", "ตะกอนแดง\nน้ำส่วนบนใส", fs=12.5), line(96, 178, 96, 198, "ln", "ah"),
        box(10, 200, 172, 40, "bad", "Hematuria", "b"), line(96, 240, 96, 260, "ln", "ah"),
        box(10, 262, 172, 56, "sk", "ส่องตะกอน\nglomerular หรือไม่?", fs=12),
        box(218, 130, 172, 48, "ms", "น้ำส่วนบนแดง\nไม่มีตะกอน", fs=12.5), line(304, 178, 304, 198, "ln", "ah"),
        box(218, 200, 172, 40, "sk", "Dipstick heme ?", fs=12.5),
        line(282, 240, 262, 268, "ln", "ah"), line(326, 240, 346, 268, "ln", "ah"),
        box(212, 270, 90, 62, "bad", "บวก\nmyoglobin\nhemoglobin", fs=11.5),
        box(306, 270, 88, 62, "bx", "ลบ\nยา · อาหาร\nporphyrin", fs=11.5),
        t(10, 358, "heme บวกแต่ไม่มี RBC = rhabdomyolysis หรือ hemolysis", "xs i2"),
        t(10, 376, "heme ลบ = rifampin · porphyrin · beet root · สีผสมอาหาร", "xs i2"))


def rbcjourney():
    bleb = lambda cx, cy: [circ(cx, cy, 12, "bad")] + [circ(cx + dx, cy + dy, 3.4, "badf") for dx, dy in
                                                     ((0, -12), (11, -5), (8, 9), (-8, 9), (-11, -5))]
    return svg(600, 250, "RBC จาก glomerulus เบียดผ่าน GBM และเจอความเข้มข้นที่เปลี่ยนในท่อไต จึงผิดรูปและถูกห่อเป็น cast ส่วนเลือดจากทางเดินปัสสาวะส่วนล่าง RBC รูปร่างปกติ อาจมีลิ่มเลือด",
        t(200, 18, "เลือดจาก glomerulus", "b mid tac"),
        rect(20, 96, 42, 14, "ms", 3), rect(74, 96, 46, 14, "ms", 3), t(122, 92, "GBM", "xs mu end"),
        ell(68, 66, 15, 7, "badf"), ell(68, 103, 5, 13, "badf"), ell(68, 136, 13, 8, "badf"),
        t(70, 170, "① เบียดผ่าน", "xs mid"), t(70, 184, "รูใน GBM ที่ฉีก", "xs mid"),
        line(96, 134, 136, 112, "ln", "ah"),
        rect(140, 82, 100, 44, "wa", 10), t(165, 76, "เจือจาง", "xs mu mid"), t(217, 76, "เข้มข้น", "xs mu mid"),
        ell(168, 104, 11, 7, "badf"), ell(212, 104, 9, 8, "badf"),
        t(186, 170, "② ความเข้มข้นในท่อ", "xs mid"), t(186, 184, "เปลี่ยนสลับ RBC บวม-หด", "xs mid"),
        line(242, 94, 264, 76, "ln", "ah"), line(242, 114, 252, 124, "ln", "ah"),
        *bleb(280, 62), t(300, 58, "③ acanthocyte", "xs b"), t(300, 72, "dysmorphic RBC", "xs i2"),
        rect(254, 126, 130, 24, "ms", 12), *[ell(274 + 22 * k, 138, 8, 5, "badf") for k in range(5)],
        t(330, 170, "③ ห่อใน Tamm–Horsfall", "xs mid"), t(330, 184, "= RBC cast", "xs mid b"),
        t(20, 214, "Hb เจอกรดในปัสสาวะนาน → สีน้ำตาล = สีโค้ก / ชา", "sm i2"),
        t(20, 234, "ไม่มีลิ่มเลือด · โปรตีนมัก > 500 มก./วัน", "sm i2"),
        line(400, 10, 400, 240, "lru da"),
        t(500, 18, "เลือดจากทางเดิน", "b mid tbad"), t(500, 34, "ปัสสาวะส่วนล่าง", "b mid tbad"),
        path("M434 56 Q434 150 500 160 Q566 150 566 56", "ln w2"),
        circ(462, 122, 7, "badf"), circ(482, 138, 7, "badf"), circ(524, 132, 7, "badf"), circ(544, 112, 7, "badf"),
        path("M484 86 q6 -14 20 -8 q8 -8 16 2 q10 8 0 16 q4 12 -12 12 q-10 6 -18 -4 q-12 -2 -6 -18 z", "badf"),
        t(532, 88, "ลิ่มเลือด", "xs tbad"),
        t(500, 184, "RBC รูปร่างปกติ · ไม่มี cast", "xs mid"), t(500, 200, "อาจมีลิ่มเลือด (clot)", "xs mid"),
        t(500, 216, "สีแดงสด / ชมพู", "xs mid"))


def spectrum():
    rows = [("Minimal change disease (MCD)", 4, 0), ("Membranous nephropathy (MN)", 4, 1), ("FSGS", 3, 2),
            ("Mesangial proliferative (IgAN, LN)", 2, 2), ("MPGN", 2, 3), ("Severe GN (IgAN, LN)", 2, 3),
            ("Crescentic GN", 1, 4)]
    cx, u, out = 392, 34, []
    for k, (name, a, b) in enumerate(rows):
        y = 42 + 27 * k
        out += [t(10, y + 14, name, "sm"), rect(cx - u * a, y + 2, u * a, 16, "ac", 3) if a else "",
                rect(cx, y + 2, u * b, 16, "ms", 3) if b else "",
                t(cx - u * a - 6, y + 14, "+" * a, "xs end tac b") if a else "",
                t(cx + u * b + 6, y + 14, "+" * b if b else "–", "xs tms b")]
    return svg(600, 252, "สเปกตรัมของโรค glomerulus จาก nephrotic ล้วนไปจนถึง nephritic ล้วน ตามตารางในสไลด์",
        t(cx - 8, 26, "← nephrotic", "sm b end tac"), t(cx + 8, 26, "nephritic →", "sm b tms"),
        line(cx, 34, cx, 236, "lmu"), *out,
        t(10, 244, "ความยาวแท่ง = จำนวน + ในตารางสไลด์ · บนลงล่าง = อักเสบมากขึ้น", "xs mu"))


def deposits():
    feet = [rect(152 + 34 * k, 130, 26, 20, "ac", 6) for k in range(13)]
    return svg(600, 300, "ตำแหน่งของ immune deposit กำหนดว่าโรคจะเป็น nephritic หรือ nephrotic",
        rect(150, 40, 440, 50, "bad", 6), t(580, 56, "เลือด · complement · เซลล์อักเสบ", "xs mu end"),
        rect(150, 94, 440, 10, "sk", 3), rect(150, 108, 440, 18, "ms", 3), *feet,
        rect(150, 156, 440, 40, "wa", 6), t(580, 188, "ปัสสาวะ", "xs mu end"),
        ell(205, 106, 14, 5, "inkf"), ell(250, 106, 12, 5, "inkf"),
        *[ell(320 + 25 * k, 128, 6, 3.5, "inkf") for k in range(4)],
        ell(502, 136, 17, 11, "inkf"),
        line(228, 34, 228, 100, "lmu da"), t(228, 16, "Subendothelial", "sm b mid"), t(228, 30, "LN III/IV · MPGN", "xs mid i2"),
        line(357, 200, 357, 132, "lmu da"), t(357, 214, "Subepithelial เล็ก สม่ำเสมอ", "sm b mid"), t(357, 228, "MN", "xs mid i2"),
        line(502, 200, 502, 148, "lmu da"), t(502, 214, "Hump ก้อนใหญ่", "sm b mid"), t(502, 228, "PSGN", "xs mid i2"),
        rect(10, 60, 122, 100, "sk", 12), t(71, 80, "Mesangium", "sm b mid"),
        ell(48, 112, 10, 6, "inkf"), ell(86, 122, 9, 5, "inkf"), ell(66, 140, 8, 5, "inkf"),
        t(71, 182, "IgAN · LN II", "xs mid i2"), t(71, 196, "→ hematuria", "xs mid i2"),
        box(10, 244, 286, 48, "ms", "ติดด้านเลือด → เซลล์อักเสบเข้าถึง\n→ nephritic", fs=12),
        box(304, 244, 286, 48, "ac", "อยู่นอก GBM ด้านปัสสาวะ → ทำร้าย podocyte\n→ nephrotic ตะกอนใส", fs=12))


def nstree():
    def col(x, spine_top, items):
        out = [line(x + 8, spine_top, x + 8, items[-1][0] + 28, "ln")]
        for y, c, s in items:
            out += [line(x + 8, y + 28, x + 16, y + 28, "ln", "ah"), box(x + 18, y, 177, 56, c, s, fs=11.5)]
        return out
    return svg(420, 470, "ต้นไม้ของ nephrotic syndrome จาก podocyte พัง สู่โปรตีนรั่ว albumin ต่ำ และโปรตีนอื่นรั่วตาม แต่ละกิ่งให้อาการต่างกัน",
        box(120, 8, 180, 40, "ac", "Podocyte บาดเจ็บ", "b"), line(210, 48, 210, 68, "ln", "ah"),
        box(90, 70, 240, 48, "ac", "Proteinuria > 3.5 g/วัน\nปัสสาวะเป็นฟอง", fs=12.5),
        line(170, 118, 108, 140, "ln", "ah"), line(250, 118, 312, 140, "ln", "ah"),
        box(10, 142, 195, 38, "wa", "Albumin ในเลือดต่ำ", "b twa"),
        box(215, 142, 195, 38, "sk", "โปรตีนอื่นรั่วตาม", "b"),
        *col(2, 180, [(196, "ms", "บวม\noncotic ↓ + ENaC เปิด"), (266, "sk", "ตับเร่งสร้าง lipoprotein\n+ LPL ทำงานลด")]),
        line(108, 322, 108, 340, "ln", "ah"), box(20, 342, 177, 56, "sk", "ไขมันสูง → lipiduria\noval fat body", fs=11.5),
        *col(207, 180, [(196, "bad", "Antithrombin III ↓\n→ ลิ่มเลือด RVT PE DVT"), (266, "ms", "IgG, factor B ↓\n→ ติดเชื้อ SBP cellulitis"),
                        (336, "sk", "VDBP · TBG · transferrin ↓\n→ Ca ↓ · T4 รวม ↓ · ซีด")]),
        t(210, 428, "ยิ่ง albumin ต่ำ ยิ่งบวมมากและเสี่ยงลิ่มเลือดมาก", "sm mid i2"),
        t(210, 448, "MN เสี่ยง RVT สูงสุด · เด็ก MCD เสี่ยง SBP จาก pneumococcus", "sm mid i2"))


def fill():
    L = ["Albumin ↓ มาก", "Oncotic pressure ในหลอดเลือด ↓", "น้ำซึมออกไปอยู่ใน interstitium",
         "Plasma volume ↓ (underfill)", "RAAS · ADH · sympathetic ↑", "ไตเก็บ Na + น้ำ → บวมยิ่งมาก"]
    Rr = ["Plasminogen รั่วออกมากับน้ำกรอง", "ถูกเปลี่ยนเป็น plasmin ใน collecting duct", "ตัด γ-subunit → ENaC เปิดค้าง",
          "ดูด Na กลับมาก (renin ต่ำ)", "Plasma volume ↑ (overfill)", "บวม ± ความดันขึ้น"]
    out = []
    for col, (x, items, last) in enumerate(((10, L, "ms"), (310, Rr, "ms"))):
        for k, s in enumerate(items):
            y = 40 + 42 * k
            out.append(box(x, y, 280, 30, last if k == 5 else ("wa" if col == 0 and k < 2 else "bx"), s, fs=12))
            if k < 5: out.append(line(x + 140, y + 30, x + 140, y + 40, "ln", "ah"))
    return svg(600, 312, "บวมใน nephrotic เกิดจากสองกลไก underfill จาก albumin ต่ำ และ overfill จาก ENaC ที่ถูก plasmin กระตุ้น",
        t(150, 24, "Underfill — เริ่มจาก albumin ต่ำ", "sm b mid twa"), t(450, 24, "Overfill — ไตเก็บโซเดียมเอง", "sm b mid tms"),
        line(300, 34, 300, 290, "lru da"), *out,
        t(300, 306, "ผู้ป่วยจริงมีทั้งสองกลไกปนกัน · amiloride ปิด ENaC ได้", "xs mid mu"))


def _pol(cx, cy, r, deg):
    import math
    a = math.radians(deg)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def glomx():
    out = []
    loops = [(-18, -16), (14, -20), (24, 6), (4, 22), (-22, 12), (0, 0)]
    for k, (title, sub) in enumerate((("ปกติ", "ช่องหลอดเลือดเปิด กรองดี"),
                                      ("Nephritic", "เซลล์อักเสบอุดหลอดเลือด → GFR ↓"),
                                      ("RPGN", "crescent เบียดกระจุกหลอดเลือด"))):
        cx, cy = 100 + 200 * k, 104
        out.append(circ(cx, cy, 64, "bx"))
        if k == 2:
            o1, o2 = _pol(cx, cy, 62, 205), _pol(cx, cy, 62, -25)
            i1, i2 = _pol(cx, cy, 40, 205), _pol(cx, cy, 40, -25)
            out.append(path("M%.1f %.1f A62 62 0 1 1 %.1f %.1f L%.1f %.1f A40 40 0 1 0 %.1f %.1f Z" % (o1 + o2 + i2 + i1), "ms"))
            out += [circ(cx + dx, cy + dy, 4, "msf") for dx, dy in ((-46, -14), (-30, -44), (6, -54), (40, -38), (50, -6))]
        for dx, dy in loops:
            if k == 2:
                dx, dy = dx * 0.55, dy * 0.45 + 22
            r = 13 if k < 2 else 8
            out.append(circ(cx + dx, cy + dy, r, "bad"))
            if k == 1:
                out += [circ(cx + dx + ex, cy + dy + ey, 3.2, "inkf") for ex, ey in ((-5, -4), (5, -3), (0, 6), (-6, 4), (6, 5))]
        out += [t(cx, 190, title, "b mid"), t(cx, 208, sub, "xs mid i2")]
    return svg(600, 222, "glomerulus ปกติ เทียบกับ nephritic ที่ช่องหลอดเลือดถูกอุด และ RPGN ที่มี crescent",
        *out,
        line(200, 20, 200, 210, "lru da"), line(400, 20, 400, 210, "lru da"))


def ifpat():
    out = []
    for k, (cls, title, sub) in enumerate((("lok w3", "Linear", "Anti-GBM (Goodpasture)"),
                                            ("lok w3 dt", "Granular", "PSGN · IgAN · LN · MPGN"),
                                            ("lru", "Pauci-immune", "ANCA (MPO, PR3)"))):
        cx = 100 + 200 * k
        out.append(rect(cx - 86, 14, 172, 112, "sk", 12))
        out += [circ(cx + dx, 70 + dy, 22, cls) for dx, dy in ((-30, -14), (14, -22), (30, 16), (-12, 22))]
        out += [t(cx, 148, title, "b mid"), t(cx, 166, sub, "xs mid i2")]
    return svg(600, 182, "รูปแบบ immunofluorescence สามแบบ linear granular และ pauci-immune บอกกลไกของ RPGN",
        *out, line(200, 14, 200, 170, "lru da"), line(400, 14, 400, 170, "lru da"))
