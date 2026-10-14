# -*- coding: utf-8 -*-
"""ภาพประกอบคาบ endo 14/10 Diabetes mellitus (ใช้ใน build_diabetes.py)"""
import math
from svg import *


def insulin_map():
    rows = [("ตับ", "มี insulin: เก็บ glycogen · หยุดสร้างน้ำตาล", "ขาด: ปล่อยน้ำตาลออกทั้งคืน → FPG สูง"),
            ("กล้ามเนื้อ", "มี insulin: GLUT4 ดึงน้ำตาลเข้าเซลล์", "ขาด: น้ำตาลหลังอาหารค้างในเลือด → PPG สูง"),
            ("ไขมัน", "มี insulin: เก็บไขมัน หยุดสลายไขมัน", "ขาด: FFA ล้นไปตับ → ketone")]
    out = [box(10, 116, 130, 70, "ac", "ตับอ่อน\nβ cell", "b"), t(75, 206, "หลั่ง insulin", "sm mid i2")]
    for k, (org, a, b) in enumerate(rows):
        y = 14 + 98 * k
        out += [rect(250, y, 340, 80, "bx", 10), t(266, y + 24, org, "b"),
                t(266, y + 46, a, "sm tok"), t(266, y + 66, b, "sm tbad"),
                path("M140 151 C 190 151, 200 %d, 248 %d" % (y + 40, y + 40), "lac w2", "ah-ac")]
    return svg(600, 312, "insulin จากตับอ่อนออกฤทธิ์ที่ตับ กล้ามเนื้อ และไขมัน เมื่อขาด insulin แต่ละอวัยวะทำให้เกิดอาการต่างกัน", *out)


def renal_threshold():
    X = lambda g: 50 + g * 0.72
    Y = lambda v: 222 - v
    def reab(g):
        f = g * 0.45
        tm = 90.0
        if f < 75: return f
        # splay — โค้งเข้าหา Tm
        return tm - (tm - 75) * math.exp(-(f - 75) / 15)
    gs = list(range(0, 401, 10))
    filt = [(X(g), Y(g * 0.45)) for g in gs]
    rea = [(X(g), Y(reab(g))) for g in gs]
    exc = [(X(g), Y(g * 0.45 - reab(g))) for g in gs]
    chain = [("ms", "น้ำตาลเกิน SGLT ดูดกลับ\n→ glucose ในปัสสาวะ"), ("wa", "น้ำตามน้ำตาลออกไป\n= ปัสสาวะมาก กลางคืน"),
             ("wa", "เสียน้ำ → กระหายน้ำ\nดื่มมาก ขาดน้ำ"), ("bad", "เสีย glucose หลายสิบ g/วัน\n→ น้ำหนักลด")]
    out = [line(X(0), Y(0), X(400), Y(0), "lmu"), line(X(0), Y(0), X(0), 20, "lmu"),
           *[p for g in (0, 100, 200, 300, 400) for p in (line(X(g), Y(0), X(g), Y(0) + 4, "lmu"), t(X(g), Y(0) + 18, str(g), "xs mid mu"))],
           t(X(400), Y(0) + 34, "glucose ในพลาสมา (mg/dL)", "xs end mu"),
           poly(filt, "lwa w2"), poly(rea, "lok w2"), poly(exc, "lbad w3"),
           line(X(180), 30, X(180), Y(0), "lms da"), t(X(180) - 4, 40, "renal threshold ~180", "xs end tms b"),
           t(X(400) - 4, Y(180) - 6, "กรองออก", "xs end twa b"), t(X(400) - 4, Y(90) - 8, "ดูดกลับ (เต็มที่)", "xs end tok b"),
           t(X(400) - 4, Y(90) + 22, "ออกในปัสสาวะ", "xs end tbad b")]
    for k, (c, s) in enumerate(chain):
        y = 16 + 60 * k
        out.append(box(386, y, 204, 48, c, s, fs=11.5))
        if k < 3: out.append(line(488, y + 48, 488, y + 58, "ln", "ah"))
    return svg(600, 262, "เมื่อ glucose ในเลือดเกินราว 180 mg/dL ท่อไตดูดกลับไม่หมด glucose ออกในปัสสาวะ ดึงน้ำตามไป ทำให้ปัสสาวะมาก กระหายน้ำ และน้ำหนักลด", *out)


def sx_hub():
    sp = [("ปัสสาวะมาก", "glucose ดึงน้ำออก (osmotic diuresis)"), ("กระหายน้ำ", "เสียน้ำ → osmolality ↑ → ศูนย์กระหาย"),
          ("หิวบ่อย น้ำหนักลด", "เซลล์ใช้น้ำตาลไม่ได้ → สลายไขมัน/กล้ามเนื้อ"), ("ตามัวขึ้นลง", "น้ำตาล/sorbitol เข้าเลนส์ เลนส์บวม"),
          ("ติดเชื้อง่าย แผลหายช้า", "neutrophil ทำงานแย่ · เชื้อราชอบน้ำตาล"), ("ผิวคอ/รักแร้ดำหนา", "insulin สูงกระตุ้น IGF-1 receptor ที่ผิว")]
    cx, cy = 300, 160
    out = [ell(cx, cy, 92, 40, "ac"), t(cx, cy - 4, "ขาด insulin", "b mid"), t(cx, cy + 16, "หรือดื้อ insulin", "sm mid")]
    pos = [(10, 14), (390, 14), (10, 124), (390, 124), (10, 234), (390, 234)]
    for (x, y), (a, b) in zip(pos, sp):
        out += [rect(x, y, 200, 62, "bx", 10), t(x + 12, y + 24, a, "b"), t(x + 12, y + 46, b, "xs i2")]
        ex, ey = (x + 200, y + 31) if x < cx else (x, y + 31)
        ex += 6 if x < cx else -6
        dx, dy = ex - cx, ey - cy
        k = 1 / math.sqrt((dx / 92) ** 2 + (dy / 40) ** 2)
        out.append(line(cx + dx * k, cy + dy * k, ex, ey, "lmu"))
    return svg(600, 306, "อาการของเบาหวานหกอย่างและกลไกของแต่ละอาการ", *out)


def dx_line():
    rows = [("FPG (mg/dL)", 70, 150, [(70, 100, "ok", "ปกติ < 100"), (100, 126, "ms", "IFG 100–125"), (126, 150, "bad", "DM ≥ 126")]),
            ("2-h OGTT (mg/dL)", 100, 240, [(100, 140, "ok", "ปกติ < 140"), (140, 200, "ms", "IGT 140–199"), (200, 240, "bad", "DM ≥ 200")]),
            ("HbA1c (%)", 5.0, 7.5, [(5.0, 5.7, "ok", "< 5.7"), (5.7, 6.5, "ms", "5.7–6.4*"), (6.5, 7.5, "bad", "DM ≥ 6.5")])]
    out = []
    for k, (name, lo, hi, zones) in enumerate(rows):
        y = 26 + 70 * k
        X = lambda v: 170 + (v - lo) / (hi - lo) * 410
        out.append(t(10, y + 22, name, "sm b"))
        for a, b, c, lab in zones:
            out += [rect(X(a), y, X(b) - X(a), 30, c, 0), t((X(a) + X(b)) / 2, y + 20, lab, "xs mid b")]
    out += [t(170, 238, "IFG/IGT = prediabetes (สไลด์) · *ช่วง prediabetes ของ HbA1c ตาม ADA", "xs mu"),
            t(170, 254, "ไม่มีอาการ ต้องยืนยันอีกวัน · มีอาการ + casual PG ≥ 200 วินิจฉัยได้เลย", "xs mu")]
    return svg(600, 264, "เกณฑ์วินิจฉัยเบาหวานและภาวะก่อนเบาหวานของ FPG OGTT และ HbA1c", *out)


def t1_course():
    X = lambda yr: 40 + yr * 52
    Y = lambda pct: 210 - pct * 1.7
    pts = [(0, 100), (2.5, 100), (3, 98), (4, 90), (5, 75), (6, 55), (7, 35), (7.6, 20), (8.4, 12), (9.5, 5), (10.5, 2)]
    stages = [(0.2, "พันธุกรรม\nเสี่ยง"), (2.3, "ตัวกระตุ้น\n(ไวรัส ฯลฯ)"), (4.1, "ภูมิต้านตนเอง\nautoantibody +"),
              (5.9, "insulitis\nT cell ทำลาย")]
    out = [line(X(0), Y(0), X(10.6), Y(0), "lmu"), line(X(0), Y(0), X(0), Y(100) - 6, "lmu"),
           t(X(0) - 6, Y(100) + 4, "100%", "xs end mu"), t(X(0) - 6, Y(20) + 4, "20%", "xs end mu"), t(X(0) - 6, Y(0) + 4, "0", "xs end mu"),
           t(14, 20, "มวล β cell", "xs mu"), t(X(10.6), Y(0) + 18, "เวลา (เดือน–ปี)", "xs end mu"),
           line(X(0), Y(20), X(10.6), Y(20), "lbad da"), t(X(0) + 6, Y(20) - 6, "เกณฑ์ที่เริ่มมีอาการ", "xs tbad"),
           poly([(X(a), Y(b)) for a, b in pts], "lac w3"),
           circ(X(7.6), Y(20), 6, "badf"), t(X(7.6) + 16, Y(20) - 28, "วินิจฉัย DM", "sm b tbad"), t(X(7.6) + 16, Y(20) - 11, "β cell ถูกทำลาย > 80%", "xs tbad")]
    for x, s in stages:
        out += [line(X(x), Y(0), X(x), Y(0) - 8, "lmu"), t(X(x), Y(0) + 18, s.split("\n")[0], "xs mid b"), t(X(x), Y(0) + 32, s.split("\n")[1], "xs mid i2")]
    return svg(600, 252, "T1DM β cell ถูกภูมิต้านตนเองทำลายทีละน้อยหลายปี อาการเกิดเมื่อถูกทำลายมากกว่าร้อยละ 80", *out)


def t2_natural():
    X = lambda yr: 60 + (yr + 15) * 11.4
    Y = lambda v: 212 - v * 1.7
    ir = [(-15, 30), (-10, 55), (-5, 72), (0, 80), (10, 82), (30, 82)]
    ins = [(-15, 35), (-10, 55), (-5, 75), (-2, 80), (0, 70), (5, 50), (15, 30), (30, 15)]
    ppg = [(-15, 10), (-8, 14), (-5, 25), (0, 50), (10, 70), (30, 88)]
    fpg = [(-15, 8), (-5, 10), (-2, 16), (0, 30), (10, 55), (30, 78)]
    out = [rect(X(-15), 20, X(-8) - X(-15), 192, "ok", 0), rect(X(-8), 20, X(0) - X(-8), 192, "ms", 0),
           rect(X(0), 20, X(30) - X(0), 192, "bad", 0),
           t((X(-15) + X(-8)) / 2, 36, "ปกติ", "xs mid b"), t((X(-8) + X(0)) / 2, 36, "เสี่ยง", "xs mid b"), t((X(0) + X(30)) / 2, 36, "เบาหวาน", "xs mid b"),
           line(X(-15), Y(0), X(30), Y(0), "lmu"),
           *[p for yr in (-15, -10, -5, 0, 5, 10, 15, 20, 25, 30) for p in (line(X(yr), Y(0), X(yr), Y(0) + 4, "lmu"), t(X(yr), Y(0) + 17, str(yr), "xs mid mu"))],
           t(X(30), Y(0) + 32, "ปีนับจากวินิจฉัย", "xs end mu"),
           poly([(X(a), Y(b)) for a, b in ir], "lms w3"), poly([(X(a), Y(b)) for a, b in ins], "lok w3"),
           poly([(X(a), Y(b)) for a, b in ppg], "lbad w2"), poly([(X(a), Y(b)) for a, b in fpg], "lbad w2 da"),
           t(X(12), Y(82) - 8, "insulin resistance", "xs b tms"), t(X(-9), Y(80) - 10, "ระดับ insulin (ชดเชย)", "xs b tok"),
           t(X(17), Y(30) - 18, "β cell ล้า", "xs b tok"),
           t(X(30) - 2, Y(88) - 8, "น้ำตาลหลังอาหาร", "xs b end tbad"), t(X(30) - 2, 112, "น้ำตาลขณะอดอาหาร (เส้นประ)", "xs b end tbad")]
    return svg(600, 262, "ธรรมชาติของเบาหวานชนิดที่ 2 insulin resistance สูงก่อน ตับอ่อนชดเชยด้วย insulin สูงจนล้า น้ำตาลหลังอาหารขึ้นก่อนน้ำตาลขณะอดอาหาร", *out)


def proinsulin():
    return svg(580, 186, "proinsulin ถูกตัดเป็น insulin กับ C-peptide ในปริมาณเท่ากัน C-peptide จึงบอกปริมาณ insulin ที่ร่างกายสร้างเอง",
        t(110, 20, "Proinsulin", "b mid"),
        line(30, 70, 190, 70, "lok w5"), t(30, 60, "B chain", "xs tok b"),
        line(40, 120, 170, 120, "lwa w5"), t(40, 140, "A chain", "xs twa b"),
        path("M190 70 C 240 60, 240 130, 170 120", "lms w3 da"), t(214, 54, "C-peptide", "xs tms b"),
        line(80, 72, 80, 118, "lmu w2"), line(130, 72, 130, 118, "lmu w2"), t(105, 100, "S–S", "xs mid mu"),
        line(262, 96, 322, 96, "ln w2", "ah"), t(292, 86, "ตัด", "xs mid i2"),
        t(410, 20, "Insulin", "b mid"),
        line(340, 60, 480, 60, "lok w5"), line(350, 100, 470, 100, "lwa w5"), line(380, 62, 380, 98, "lmu w2"), line(430, 62, 430, 98, "lmu w2"),
        t(540, 20, "C-peptide", "b mid tms"), path("M510 60 C 560 50, 560 110, 520 110", "lms w3 da"),
        t(290, 156, "ออกมาจำนวนเท่ากัน · C-peptide ไม่ถูกตับดึงทิ้งรอบแรก และไม่มีใน insulin ฉีด", "xs mid i2"),
        t(290, 174, "→ C-peptide ต่ำ = ตับอ่อนสร้างเองไม่ได้ (T1) · ปกติ/สูง = ยังสร้างได้แต่ดื้อ (T2)", "xs mid i2 b"))


def pedersen():
    def kid(x, y, c, s):
        return box(x, y, 184, 64, c, s, fs=11.5)
    return svg(400, 420, "กลไก Pedersen glucose ของแม่ผ่านรก insulin ไม่ผ่าน ทารกสร้าง insulin เกินจนตัวโต น้ำตาลต่ำหลังคลอด ปอดไม่พร้อม และเม็ดเลือดแดงข้น",
        box(80, 8, 240, 44, "bad", "แม่: น้ำตาลสูง (ดื้อ insulin\nจากฮอร์โมนรก)", fs=12),
        rect(10, 72, 380, 26, "ms", 6), t(20, 90, "รก", "sm b tms"),
        line(150, 52, 150, 120, "lbad w2", "ah-bad"), t(158, 66, "glucose ผ่าน ✓", "xs b tbad"),
        line(260, 52, 260, 70, "lmu w2"), t(268, 66, "insulin ไม่ผ่าน ✕", "xs b mu"),
        box(80, 122, 240, 44, "ac", "ทารก: น้ำตาลสูง → ตับอ่อนสร้าง\ninsulin มาก (fetal hyperinsulinemia)", fs=12),
        line(200, 166, 200, 316, "ln"),
        line(200, 226, 188, 226, "ln", "ah"), line(200, 226, 212, 226, "ln", "ah"),
        line(200, 316, 188, 316, "ln", "ah"), line(200, 316, 212, 316, "ln", "ah"),
        kid(4, 194, "ms", "insulin = ฮอร์โมนเร่งโต\n→ ตัวโต (macrosomia)\nคลอดยาก ผ่าคลอด"),
        kid(212, 194, "bad", "คลอดแล้วน้ำตาลจากแม่หยุด\ninsulin ยังสูง\n→ น้ำตาลต่ำแรกเกิด"),
        kid(4, 284, "wa", "insulin ยับยั้งการสร้าง\nsurfactant\n→ RDS (ปอดไม่พร้อม)"),
        kid(212, 284, "sk", "เผาผลาญมาก ใช้ O₂ มาก\n→ EPO ↑ เลือดข้น\n→ ตัวเหลือง"),
        t(200, 376, "แม่: preeclampsia · ครรภ์แฝดน้ำ · กรวยไตอักเสบ (สไลด์)", "xs mid i2"),
        t(200, 396, "50% เป็นเบาหวานถาวรใน 10 ปี", "xs mid i2 b"))


def dka():
    def col(x, items):
        out, y = [], 116
        for k, (h, c, s) in enumerate(items):
            out.append(box(x, y, 196, h, c, s, fs=11.5))
            if k < len(items) - 1: out.append(line(x + 98, y + h, x + 98, y + h + 12, "ln", "ah"))
            y += h + 14
        return out
    return svg(420, 380, "กลไก DKA ขาด insulin ร่วมกับฮอร์โมนต้าน ทำให้น้ำตาลสูงจนขาดน้ำ และสลายไขมันจนเกิดกรด ketone",
        box(30, 8, 360, 48, "ac", "ขาด insulin + ฮอร์โมนต้าน ↑\nglucagon · cortisol · catecholamine · GH", fs=12),
        line(130, 56, 106, 76, "ln", "ah"), line(290, 56, 314, 76, "ln", "ah"),
        box(8, 78, 196, 28, "sk", "ตับ + กล้ามเนื้อ", "b", fs=12), box(216, 78, 196, 28, "sk", "เนื้อเยื่อไขมัน", "b", fs=12),
        *col(8, [(52, "ms", "ตับสร้างน้ำตาลเพิ่ม\nกล้ามเนื้อใช้ไม่ได้ → glucose ↑"), (52, "wa", "glucose ล้นไต\n→ osmotic diuresis"),
                 (66, "bad", "เสียน้ำราว 6 ลิตร + Na + K\n→ ชีพจรเร็ว BP ต่ำ\nปากแห้ง AKI")]),
        *col(216, [(52, "ms", "สลายไขมัน (lipolysis)\n→ FFA ไหลไปตับ"), (52, "ms", "ตับ (glucagon สูง) เปลี่ยน FFA\n→ β-OHB · acetoacetate"),
                   (80, "bad", "กรด ketone → HCO₃ ↓ AG ↑\n→ หายใจหอบลึก (Kussmaul)\nลมหายใจกลิ่นผลไม้ (acetone)\nปวดท้อง อาเจียน")]),
        t(210, 352, "K ในเลือดปกติ/สูง แต่ K ทั้งร่างกายพร่อง (ภาพหัวข้อถัดไป)", "xs mid i2"),
        t(210, 370, "ตัวกระตุ้นบ่อย: ติดเชื้อ · หยุด insulin · T1 รายใหม่ · MI · SGLT2i", "xs mid i2"))


def dkahhs():
    X = lambda i: 60 + i * 5
    Y = lambda e: 220 - e * 1.8
    sig = lambda i, ec: 0 if i <= 0 else 100 / (1 + (ec / i) ** 3)
    xs = [i * 0.5 for i in range(0, 201)]
    return svg(600, 262, "insulin ปริมาณน้อยก็หยุดการสลายไขมันได้ แต่ต้องมากกว่านั้นจึงคุมน้ำตาล HHS มี insulin พอกัน ketone แต่ไม่พอคุมน้ำตาล",
        line(X(0), Y(0), X(100), Y(0), "lmu"), line(X(0), Y(0), X(0), Y(100) - 4, "lmu"),
        t(X(0) - 6, Y(100) + 4, "100%", "xs end mu"), t(X(0) - 6, Y(0) + 4, "0", "xs end mu"),
        t(X(100), Y(0) + 18, "ระดับ insulin ในเลือด →", "xs end mu"),
        poly([(X(i), Y(sig(i, 12))) for i in xs], "lok w3"), poly([(X(i), Y(sig(i, 55))) for i in xs], "lwa w3"),
        t(X(20) + 8, Y(78), "หยุดสลายไขมัน → ไม่มี ketone", "sm b tok"),
        t(X(70) + 6, Y(62), "ดึงน้ำตาลเข้าเซลล์ + หยุดตับ", "sm b twa"),
        t(X(70) + 6, Y(62) + 16, "ปล่อยน้ำตาล → คุม glucose", "sm b twa"),
        line(X(4), Y(0), X(4), 30, "lbad da"), line(X(30), Y(0), X(30), 30, "lms da"),
        pill(X(4) - 30, 4, "DKA", "bad", "sm b mid tbad", w=60), pill(X(30) - 30, 4, "HHS", "ms", "sm b mid tms", w=60),
        t(X(4) + 6, 66, "ไม่มี insulin", "xs tbad"), t(X(30) + 6, 66, "insulin มีบ้าง", "xs tms"))


def kshift():
    def cell(cx, title, inward):
        o = [t(cx, 20, title, "b mid"), circ(cx, 110, 56, "sk"), t(cx, 104, "ในเซลล์", "xs mid mu"),
             t(cx, 124, "K⁺ K⁺ K⁺" if inward else "K⁺", "sm mid b")]
        for ang in (30, 150, 270):
            a = math.radians(ang)
            x1, y1 = cx + 60 * math.cos(a), 110 - 60 * math.sin(a)
            x2, y2 = cx + 92 * math.cos(a), 110 - 92 * math.sin(a)
            o.append(line(x2, y2, x1, y1, "lok w2", "ah-ok") if inward else line(x1, y1, x2, y2, "lbad w2", "ah-bad"))
        return o
    return svg(600, 290, "ใน DKA โพแทสเซียมเคลื่อนออกนอกเซลล์และหายทางปัสสาวะ เมื่อให้ insulin โพแทสเซียมกลับเข้าเซลล์ ระดับในเลือดจึงดิ่ง",
        *cell(150, "ก่อนให้ insulin", False), *cell(450, "หลังให้ insulin", True),
        t(150, 196, "ขาด insulin + กรด + osmolality สูง", "xs mid i2"), t(150, 211, "→ K ออกนอกเซลล์ · K ในเลือดดูปกติ/สูง", "xs mid tbad b"),
        t(150, 226, "แต่หายทางปัสสาวะไปมาก (K ทั้งตัวพร่อง)", "xs mid i2"),
        t(450, 196, "insulin + แก้กรด ดัน K กลับเข้าเซลล์", "xs mid i2"), t(450, 211, "→ K ในเลือดดิ่ง → หัวใจเต้นผิดจังหวะ", "xs mid tbad b"),
        t(450, 226, "จึงต้องรู้ค่า K ก่อนเริ่ม insulin เสมอ", "xs mid i2"),
        line(300, 30, 300, 230, "lru da"),
        pill(10, 250, "K < 3.3: ให้ K ก่อน ยังไม่ให้ insulin", "bad", "xs b mid tbad", w=196),
        pill(212, 250, "3.3–5.2: ผสม K 20–30 mEq/L", "ms", "xs b mid tms", w=176),
        pill(394, 250, "> 5.2: ยังไม่ให้ K เช็คทุก 2 ชม.", "ok", "xs b mid tok", w=196))


def hypo_ladder():
    Y = lambda g: 40 + (100 - g) * 3.6
    right = [(80, "≈ 80 ตับอ่อนหยุดหลั่ง insulin", "", "i2"), (70, "≈ 65–70 glucagon + adrenaline หลั่ง", "", "tms"),
             (58, "≈ 55–60 อาการเตือน: ใจสั่น มือสั่น", "เหงื่อแตก หิว กังวล (adrenergic)", "tms"),
             (48, "< 50 สมองขาดน้ำตาล: สับสน", "พูดไม่ชัด พฤติกรรมเปลี่ยน ง่วงซึม", "tbad"), (30, "≈ 30 ชัก หมดสติ", "", "tbad")]
    out = [rect(130, Y(100), 26, Y(70) - Y(100), "ok", 0), rect(130, Y(70), 26, Y(54) - Y(70), "ms", 0),
           rect(130, Y(54), 26, Y(20) - Y(54), "bad", 0), t(143, 28, "mg/dL", "xs mid mu")]
    for g, a, b, c in right:
        y = Y(g)
        out += [line(156, y, 172, y, "lmu"), t(178, y + 4, a, "sm b " + c)]
        if b: out.append(t(178, y + 20, b, "xs i2"))
    out += [line(114, Y(70), 130, Y(70), "lmu"), t(108, Y(70) + 4, "level 1 < 70", "xs end b tms"),
            line(114, Y(54), 130, Y(54), "lmu"), t(108, Y(54) + 4, "level 2 < 54", "xs end b tbad"),
            t(108, Y(36), "level 3 =", "xs end b tbad"), t(108, Y(36) + 14, "ต้องมีคนช่วย", "xs end tbad"),
            path("M126 %.1f C 112 %.1f, 112 %.1f, 126 %.1f" % (Y(60), Y(57), Y(47), Y(44)), "lbad da", "ah-bad"),
            t(10, Y(20) + 22, "hypoglycemia บ่อย → เกณฑ์อาการเตือนเลื่อนลง (ลูกศรประ) → สับสนก่อนรู้ตัว", "xs b tbad"),
            t(10, Y(20) + 38, "= hypoglycemia unawareness · ระดับ level ตาม ADA", "xs tbad")]
    return svg(420, 388, "ลำดับการตอบสนองเมื่อน้ำตาลในเลือดลดลง จากหยุดหลั่ง insulin ฮอร์โมนต้าน อาการเตือน ไปจนถึงสมองขาดน้ำตาลและชัก", *out)


def retina():
    def eye(cx, kind):
        o = [circ(cx, 82, 60, "bad"), circ(cx + 30, 76, 11, "ms"), circ(cx - 12, 86, 8, "sk")]
        for d in ("M%d 76 Q%d 40 %d 34", "M%d 76 Q%d 112 %d 128", "M%d 76 Q%d 60 %d 70", "M%d 76 Q%d 96 %d 102"):
            o.append(path(d % (cx + 30, cx, cx - 40), "lbad w2"))
        if kind >= 1:
            o += [circ(cx + dx, 82 + dy, 1.8, "badf") for dx, dy in ((-30, -20), (-10, 24), (6, -30), (-36, 10), (14, 26))]
            o += [ell(cx - 24, 60, 5, 3.5, "badf"), ell(cx + 4, 112, 6, 4, "badf")]
        if kind == 1:
            o += [circ(cx + dx, 82 + dy, 2.4, "msf") for dx, dy in ((-34, 30), (-40, -6))]
        if kind == 2:
            o += [circ(cx - 12 + 15 * math.cos(a / 6 * math.pi), 86 + 15 * math.sin(a / 6 * math.pi), 2.6, "msf") for a in range(12)]
        if kind == 3:
            o += [path("M%d 70 q4 -6 8 0 q4 6 8 0 q4 -6 8 0" % (cx + 14), "lbad w2"), path("M%d 92 q4 -6 8 0 q4 6 8 0" % (cx + 18), "lbad w2"),
                  ell(cx - 18, 104, 18, 12, "badf")]
        return o
    labels = [("ปกติ", "จานประสาทตา (ขวา)", "macula (กลาง)"), ("NPDR", "microaneurysm · จุดเลือด", "exudate · ยังมองเห็นปกติ"),
              ("Macular edema", "รั่วรอบ macula", "→ ตามัว แม้เป็น NPDR"), ("PDR", "หลอดเลือดใหม่เปราะ", "เลือดออกในวุ้นตา จอตาลอก")]
    out = []
    for k, (a, b, c) in enumerate(labels):
        cx = 78 + 148 * k
        out += eye(cx, k) + [t(cx, 166, a, "b mid"), t(cx, 182, b, "xs mid i2"), t(cx, 197, c, "xs mid i2")]
    return svg(600, 206, "จอประสาทตาปกติ NPDR macular edema และ PDR", *out)


def dn_stages():
    X = lambda y: 60 + y * 25
    Yg = lambda v: 210 - v * 1.1
    gfr = [(0, 120), (1, 142), (3, 150), (8, 140), (10, 122), (13, 80), (15, 42), (18, 12), (20, 6)]
    stages = [(0, 2, "1"), (2, 5, "2"), (5, 10, "3"), (10, 15, "4"), (15, 20, "5")]
    out = []
    for k, (a, b, s) in enumerate(stages):
        out += [rect(X(a), 34, X(b) - X(a), 176, "sk" if k % 2 == 0 else "bx", 0), t((X(a) + X(b)) / 2, 50, "ระยะ " + s, "xs mid b")]
    out += [line(X(0), Yg(0), X(20), Yg(0), "lmu"), t(X(0) - 6, Yg(150) + 4, "150", "xs end mu"), t(X(0) - 6, Yg(60) + 4, "60", "xs end mu"),
            t(X(0) - 6, Yg(0) + 4, "0", "xs end mu"), t(12, 24, "GFR", "xs mu b"),
            poly([(X(a), Yg(b)) for a, b in gfr], "lac w3"),
            t(X(1.0), Yg(150) - 10, "hyperfiltration", "xs b tac"), t(X(3.2), Yg(105), "GBM หนา", "xs i2"), t(X(3.2), Yg(105) + 14, "(เงียบ)", "xs i2"),
            t(X(13.6), Yg(80) - 4, "overt proteinuria", "xs b tbad"), t(X(15.6), Yg(42) - 2, "GFR ↓ เร็ว", "xs b tbad"),
            t(X(17.2), Yg(12) - 10, "uremia", "xs b tbad"),
            rect(X(0), 222, X(5) - X(0), 16, "ok", 0), rect(X(5), 222, X(10) - X(5), 16, "ms", 0), rect(X(10), 222, X(20) - X(10), 16, "bad", 0),
            t(X(2.5), 234, "albumin ปกติ", "xs mid b"), t(X(7.5), 234, "micro 30–300", "xs mid b"), t(X(15), 234, "overt > 300 mg/วัน", "xs mid b"),
            *[t(X(y), 256, str(y), "xs mid mu") for y in (0, 5, 10, 15, 20)], t(X(20), 272, "ปีหลังเป็นเบาหวาน", "xs end mu")]
    return svg(600, 280, "ระยะของ diabetic nephropathy GFR สูงช่วงแรกแล้วลดลง ขณะที่ albuminuria เพิ่มจาก micro เป็น overt", *out)


def renoprot():
    panels = [("เบาหวาน (hyperfiltration)", "w5", "w2", "แรงดันใน glomerulus ↑", "tbad"),
              ("+ ACEi / ARB", "w5", "w5", "efferent คลาย → แรงดัน ↓", "tok"),
              ("+ SGLT2i", "w2", "w2", "afferent หด → แรงดัน ↓", "tok")]
    out = []
    for k, (title, aw, ew, res, rc) in enumerate(panels):
        cx = 100 + 200 * k
        out += [t(cx, 22, title, "b mid"), line(cx - 92, 90, cx - 28, 90, "lbad " + aw), line(cx + 28, 90, cx + 92, 90, "lbad " + ew),
                circ(cx, 90, 26, "bad"), t(cx - 60, 76, "afferent", "xs mid mu"), t(cx + 60, 76, "efferent", "xs mid mu"),
                t(cx, 140, res, "sm b mid " + rc)]
    out += [line(200, 12, 200, 200, "lru da"), line(400, 12, 400, 200, "lru da"),
            t(100, 162, "SGLT2 ดูด Na มาก → macula densa", "xs mid i2"), t(100, 176, "เห็น Na น้อย → afferent ขยาย", "xs mid i2"),
            t(300, 162, "angiotensin II หด efferent", "xs mid i2"), t(300, 176, "ACEi/ARB ปลดตรงนี้", "xs mid i2"),
            t(500, 162, "Na ถึง macula densa มากขึ้น", "xs mid i2"), t(500, 176, "→ TGF หด afferent กลับ", "xs mid i2"),
            t(300, 206, "ทั้งสองยาทำให้ Cr ขึ้นเล็กน้อยช่วงแรก = ผลของแรงดันที่ลด ไม่ใช่ไตเสีย", "xs mid b")]
    return svg(600, 216, "กลไกที่ ACEi ARB และ SGLT2 inhibitor ลดแรงดันใน glomerulus ของผู้ป่วยเบาหวาน", *out)


def neuro():
    body = [circ(75, 26, 16, "bx"), rect(44, 44, 62, 86, "bx", 10), rect(26, 48, 16, 108, "bx", 7), rect(108, 48, 16, 108, "bx", 7),
            rect(48, 128, 24, 136, "bx", 8), rect(78, 128, 24, 136, "bx", 8),
            rect(48, 206, 24, 58, "ms", 8), rect(78, 206, 24, 58, "ms", 8), rect(26, 138, 16, 18, "ms", 7), rect(108, 138, 16, 18, "ms", 7),
            t(118, 238, "stocking", "xs tms b"), t(128, 152, "glove", "xs tms b"),
            t(75, 284, "เส้นยาวสุดเสียก่อน", "xs mid i2")]
    ins = [("bx", "Sensory: ชา ไม่เจ็บ\n→ ไม่รู้ว่ามีแผล"), ("bx", "Motor: กล้ามเนื้อเท้าอ่อน\n→ นิ้วงอ จุดกดทับ callus"),
           ("bx", "Autonomic: เหงื่อไม่ออก\n→ ผิวแห้ง แตก"), ("ms", "PAD: เลือดไปน้อย\n→ แผลหายช้า")]
    out = []
    for k, (c, s) in enumerate(ins):
        y = 10 + 68 * k
        out += [box(176, y, 196, 56, c, s, fs=11.5), line(372, y + 28, 404, 140, "ln", "ah")]
    out += [box(406, 112, 184, 56, "bad", "แผลที่เท้า\n(neuropathic ulcer)", "b", fs=12), line(498, 168, 498, 196, "ln", "ah"),
            box(406, 198, 184, 56, "bad", "ติดเชื้อ → ตัดขา\nครึ่งหนึ่งของการตัดขา", fs=11.5),
            t(406, 278, "+ บาดเจ็บเล็กน้อย (รองเท้าคับ เดินเท้าเปล่า)", "xs i2")]
    return svg(600, 292, "เบาหวานทำลายเส้นประสาทยาวที่สุดก่อนเป็นรูปถุงเท้าถุงมือ ร่วมกับเส้นเลือดตีบนำไปสู่แผลที่เท้าและการตัดขา", *body, *out)


def glyc_target():
    X = lambda a: 60 + (a - 6) * 200
    return svg(600, 196, "เป้า HbA1c ปรับตามผู้ป่วย ยิ่งต่ำยิ่งลด microvascular แต่ยิ่งเสี่ยง hypoglycemia",
        rect(X(6), 60, X(7) - X(6), 40, "ok", 0), rect(X(7), 60, X(7.5) - X(7), 40, "sk", 0), rect(X(7.5), 60, X(8.5) - X(7.5), 40, "ms", 0),
        t((X(6) + X(7)) / 2, 85, "เข้มงวด < 6.5–7%", "sm b mid tok"), t((X(7.5) + X(8.5)) / 2, 85, "ผ่อนปรน ≥ 7.5%", "sm b mid tms"),
        *[p for a in (6, 6.5, 7, 7.5, 8, 8.5) for p in (line(X(a), 100, X(a), 106, "lmu"), t(X(a), 120, "%g" % a, "xs mid mu"))],
        t(X(6.5), 142, "วินิจฉัยใหม่ · อายุขัยยาว", "xs mid i2"), t(X(6.5), 157, "ไม่มีโรคหัวใจ", "xs mid i2"),
        t(X(8), 142, "เด็กเล็ก · สูงอายุมาก", "xs mid i2"), t(X(8), 157, "ภาวะแทรกซ้อนมาก · hypo บ่อย", "xs mid i2"),
        line(X(8.4), 30, X(6.1), 30, "lok w2", "ah-ok"), t(X(7.25), 22, "ยิ่งต่ำ: microvascular ลด", "xs mid tok b"),
        line(X(8.4), 186, X(6.1), 186, "lbad w2", "ah-bad"), t(X(7.25), 178, "ยิ่งต่ำ: hypoglycemia เพิ่ม", "xs mid tbad b"))


def drug_sites():
    org = [(10, 10, 180, 66, "สมอง", ["GLP-1RA: อิ่มเร็ว กินน้อยลง"]),
           (210, 10, 180, 66, "กระเพาะ", ["GLP-1RA: บีบตัวช้า อิ่มนาน"]),
           (410, 10, 180, 66, "ลำไส้", ["AGI: ชะลอย่อยแป้ง", "อาหาร → หลั่ง incretin"]),
           (10, 132, 180, 66, "ตับ", ["metformin: ลดตับปล่อยน้ำตาล", "(insulin sensitizer)"]),
           (410, 112, 180, 106, "ตับอ่อน", ["β: SU/glinide ปิด K-ATP", "  หลั่งเสมอ → hypo ได้", "β: GLP-1RA/DPP4i หลั่งเมื่อ", "  น้ำตาลสูงเท่านั้น · α: glucagon ↓"]),
           (10, 254, 180, 66, "กล้ามเนื้อ / ไขมัน", ["TZD (PPAR-γ): ไวต่อ insulin", "insulin ฉีด: ดึงน้ำตาลเข้า"]),
           (410, 254, 180, 66, "ไต", ["SGLT2i: ทิ้งน้ำตาลทาง", "ปัสสาวะ ไม่ขึ้นกับ insulin"])]
    out = [circ(300, 166, 48, "wa"), t(300, 162, "glucose", "b mid twa"), t(300, 180, "ในเลือด", "sm mid twa")]
    for x, y, w, h, name, lines in org:
        out += [rect(x, y, w, h, "bx", 10), t(x + 10, y + 20, name, "sm b")]
        out += [t(x + 10, y + 38 + 16 * i, ln, "xs tac") for i, ln in enumerate(lines)]
        tx, ty = x + w / 2, y + h / 2
        dx, dy = tx - 300, ty - 166
        d = math.hypot(dx, dy)
        ex = tx - dx / d * (w / 2 + 2) if abs(dx) > abs(dy) * 1.2 else tx - dx / d * (h / 2 + 2) * abs(dx) / max(abs(dy), 1)
        ey = ty - dy / d * (h / 2 + 2) if abs(dy) * 1.2 >= abs(dx) else ty - dy / d * (w / 2 + 2) * abs(dy) / max(abs(dx), 1)
        out.append(line(300 + dx / d * 50, 166 + dy / d * 50, ex, ey, "lmu da"))
    return svg(600, 330, "ยาเบาหวานแต่ละกลุ่มออกฤทธิ์ที่อวัยวะต่างกัน", *out)


def incretin():
    def plot(x0, title, pts, cls, note):
        o = [t(x0 + 85, 132, title, "sm b mid"), line(x0 + 10, 212, x0 + 170, 212, "lmu"), line(x0 + 10, 212, x0 + 10, 146, "lmu")]
        o += [poly([(x0 + 10 + px * 160, 212 - py * 60) for px, py in pts], cls)]
        o += [t(x0 + 85, 244, note, "xs mid i2")]
        for mx in (0.15, 0.5, 0.85):
            o.append(t(x0 + 10 + mx * 160, 226, "▲", "xs mid mu"))
        return o
    nat = [(0, 0.05), (0.12, 0.05), (0.15, 0.5), (0.2, 0.08), (0.47, 0.05), (0.5, 0.5), (0.55, 0.08), (0.82, 0.05), (0.85, 0.5), (0.9, 0.08), (1, 0.05)]
    dpp = [(0, 0.15), (0.12, 0.15), (0.16, 0.8), (0.28, 0.25), (0.47, 0.18), (0.51, 0.8), (0.63, 0.25), (0.82, 0.18), (0.86, 0.8), (0.98, 0.25), (1, 0.2)]
    glp = [(0, 0.9), (1, 0.9)]
    return svg(600, 254, "incretin หลั่งจากลำไส้เมื่อกินอาหาร กระตุ้น insulin เฉพาะเมื่อน้ำตาลสูงและลด glucagon ถูก DPP-4 ทำลายในไม่กี่นาที DPP-4 inhibitor ยืดเวลา GLP-1 receptor agonist ให้ระดับสูงต่อเนื่อง",
        box(10, 20, 90, 50, "sk", "อาหาร", "b"), line(100, 45, 126, 45, "ln", "ah"),
        box(128, 14, 200, 62, "bx", "ลำไส้\nL cell → GLP-1 · K cell → GIP", fs=12), line(328, 45, 368, 45, "ln", "ah"),
        box(370, 14, 220, 62, "ac", "ตับอ่อน: insulin ↑ เมื่อน้ำตาลสูง\nglucagon ↓ → ตับปล่อยน้ำตาลลด", fs=11.5),
        pill(214, 84, "✕ DPP-4 ตัดทิ้งใน 1–2 นาที", "bad", "xs b mid tbad", w=176),
        *plot(0, "GLP-1 ธรรมชาติ", nat, "lmu w2", "อยู่ไม่กี่นาทีหลังอาหาร"),
        *plot(200, "DPP-4 inhibitor", dpp, "lok w2", "ของตัวเองอยู่นานขึ้น · น้ำหนักคงที่"),
        *plot(400, "GLP-1RA (ฉีด/กิน)", glp, "lac w3", "สูงต่อเนื่อง → อิ่ม น้ำหนักลด คลื่นไส้"),
        t(590, 120, "▲ = มื้ออาหาร", "xs end mu"), line(200, 124, 200, 250, "lru da"), line(400, 124, 400, 250, "lru da"))


def sglt2():
    def row(y, blocked):
        o = [circ(40, y, 20, "bad"), rect(62, y - 10, 470, 20, "wa", 10), t(552, y + 4, "ปัสสาวะ", "xs b")]
        o += [rect(90, y - 12, 210, 24, "lok", 6) if not blocked else rect(90, y - 12, 210, 24, "lbad da", 6),
              rect(306, y - 12, 100, 24, "lok", 6)]
        n_after = 8 if blocked else 0
        dots = [(110 + 22 * k, y) for k in range(9)]
        for k, (dx, dy) in enumerate(dots):
            keep = blocked or k < 2
            o.append(circ(dx, dy, 3.2, "msf" if keep else "paf"))
        o += [circ(420 + 18 * k, y, 3.2, "msf") for k in range(n_after // 2)]
        if not blocked:
            o += [line(130 + 30 * k, y - 12, 130 + 30 * k, y - 28, "lok", "ah-ok") for k in range(6)]
        else:
            o += [t(195, y - 18, "✕ SGLT2 ถูกยับยั้ง", "xs mid b tbad")]
        return o
    return svg(600, 236, "SGLT2 ที่ proximal tubule ดูดกลับ glucose ส่วนใหญ่ เมื่อยับยั้ง glucose จึงออกทางปัสสาวะ",
        t(10, 20, "ปกติ", "sm b"), *row(56, False), t(195, 84, "S1–S2: SGLT2 ดูดกลับ ~90%", "xs mid tok"), t(356, 84, "S3: SGLT1 ~10%", "xs mid tok"),
        t(10, 116, "ให้ SGLT2 inhibitor", "sm b tbad"), *row(150, True),
        pill(10, 186, "ทิ้งน้ำตาลวันละหลายสิบกรัม → น้ำหนักลด", "ok", "xs b mid tok", w=230),
        pill(248, 186, "ขับ Na/น้ำ → BP ลด · ปกป้องไต/หัวใจ", "ok", "xs b mid tok", w=210),
        pill(10, 212, "AE: เชื้อราอวัยวะเพศ (น้ำตาลในปัสสาวะ)", "bad", "xs b mid tbad", w=230),
        pill(248, 212, "ขาดน้ำ · euglycemic DKA (น้ำตาลไม่สูงแต่มี ketone)", "bad", "xs b mid tbad", w=300))


def insulin_profiles():
    X = lambda h: 50 + h * 21
    Y = lambda e: 214 - e * 160
    curves = [("Rapid (lispro, aspart)", "lbad w3", [(0, 0), (0.17, 0.04), (0.75, 0.6), (1.5, 1), (2.5, 0.5), (4, 0)], (1.5, 1.0, 6, -8)),
              ("Regular", "lms w3", [(0, 0), (0.5, 0.04), (1, 0.42), (2, 0.82), (3, 0.6), (4.5, 0.25), (6, 0)], (3.0, 0.62, 8, 0)),
              ("NPH", "lwa w3", [(0, 0), (1.5, 0.05), (3, 0.32), (6, 0.52), (8, 0.48), (12, 0.24), (16, 0.05), (18, 0)], (6.6, 0.52, 0, -10)),
              ("Glargine", "lok w3", [(0, 0), (1.5, 0.14), (3, 0.27), (5, 0.3), (12, 0.3), (20, 0.29), (24, 0.22)], (16, 0.3, 0, -10))]
    out = [line(X(0), Y(0), X(24), Y(0), "lmu"), line(X(0), Y(0), X(0), Y(1) - 6, "lmu"), t(14, 22, "ฤทธิ์", "xs mu"),
           *[p for h in (0, 2, 4, 6, 8, 12, 16, 20, 24) for p in (line(X(h), Y(0), X(h), Y(0) + 4, "lmu"), t(X(h), Y(0) + 17, str(h), "xs mid mu"))],
           t(X(24), Y(0) + 32, "ชั่วโมงหลังฉีด", "xs end mu")]
    for name, cls, pts, (lx, ly, dx, dy) in curves:
        out += [poly([(X(a), Y(b)) for a, b in pts], cls), t(X(lx) + dx, Y(ly) + dy, name, "xs b")]
    return svg(600, 252, "รูปแบบการออกฤทธิ์ของ insulin rapid regular NPH และ glargine", *out)


def basal_bolus():
    X = lambda h: 60 + (h - 6) * 21.7
    def panel(y0, title, basal_cls, bolus_cls):
        base = y0 + 70
        o = [t(10, y0 + 14, title, "sm b"), line(X(6), base, X(30), base, "lmu"),
             rect(X(6), base - 14, X(30) - X(6), 14, basal_cls, 0)]
        for m in (7, 12, 18):
            o.append(path("M%.1f %.1f Q%.1f %.1f %.1f %.1f Q%.1f %.1f %.1f %.1f" % (
                X(m), base - 14, X(m + 0.8), base - 64, X(m + 1.4), base - 50, X(m + 2.4), base - 18, X(m + 3.6), base - 14), bolus_cls))
        return o
    out = panel(10, "ร่างกายปกติ", "ok", "lok w2") + panel(118, "Basal–bolus (T1)", "wa", "lbad w2")
    out += [t(X(m), 214, lab, "xs mid mu") for m, lab in ((7, "เช้า"), (12, "กลางวัน"), (18, "เย็น"), (22, "ก่อนนอน"))]
    out += [t(X(22.6), 168, "basal: glargine / NPH ก่อนนอน", "xs twa b"), t(X(20.5), 132, "bolus: rapid/regular ก่อนอาหาร", "xs tbad b")]
    return svg(600, 224, "insulin ปกติของร่างกายมี basal ต่อเนื่องและ bolus หลังอาหาร การฉีดแบบ basal bolus เลียนแบบรูปแบบนี้", *out)
