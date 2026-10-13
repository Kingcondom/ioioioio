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
