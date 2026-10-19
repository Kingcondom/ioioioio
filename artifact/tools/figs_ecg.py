# -*- coding: utf-8 -*-
"""ภาพประกอบคาบ cardio 36 Basic ECG + common arrhythmia (ใช้ใน build_ecg.py)

มีเครื่องวาด ECG จริงบนกระดาษกราฟ: 25 mm/s · 10 mm/mV · 1 mm = K px
คลื่นแต่ละตัวประกอบจาก gaussian (ศูนย์กลาง วินาที, แอมพลิจูด mV, ความกว้าง วินาที)"""
import math
from svg import *

K = 4  # px ต่อ mm


# ───────────────────────────── เครื่องวาด ECG
def _g(c, a, s):
    return (c, a, s)


def beat(tR, kind="n", pr=0.16, p=True, p_amp=0.13, p_inv=False, r=1.0, s=0.22, q=0.06,
         t_amp=0.28, st=0.0, peaked=False, t_inv=False, p_kind="n", pr_dep=0.0, u=0.0):
    """คลื่นหนึ่งจังหวะ — tR = เวลาของยอด R (วินาที) · คืน list ของ gaussian"""
    out = []
    on = tR - 0.04                       # จุดเริ่ม QRS
    if p:
        pc = on - pr + 0.05              # กลาง P (P กว้าง ~0.1 s)
        sgn = -1 if p_inv else 1
        if p_kind == "pulm":
            out.append(_g(pc, sgn * 0.30, 0.017))
        elif p_kind == "mitr":
            out += [_g(pc - 0.028, sgn * 0.11, 0.019), _g(pc + 0.04, sgn * 0.12, 0.019)]
        else:
            out.append(_g(pc, sgn * p_amp, 0.021))
        if pr_dep:
            out.append(_g(on - 0.035, -pr_dep, 0.022))
    if kind == "n":
        out += [_g(tR - 0.026, -q, 0.007), _g(tR, r, 0.0105), _g(tR + 0.027, -s, 0.0095)]
        T = (tR + 0.26, (-1 if t_inv else 1) * t_amp, 0.045)
    elif kind == "v":                    # QRS กว้างจาก ventricle (PVC / ventricular rhythm / VT)
        out += [_g(tR + 0.01, r * 0.95, 0.032), _g(tR + 0.085, -0.45, 0.026)]
        T = (tR + 0.33, -0.32, 0.06)
    elif kind == "rbbb_v1":
        out += [_g(tR - 0.012, 0.28, 0.009), _g(tR + 0.025, -0.32, 0.011), _g(tR + 0.072, 0.72, 0.017)]
        T = (tR + 0.31, -0.18, 0.05)
    elif kind == "rbbb_v6":
        out += [_g(tR - 0.026, -0.08, 0.007), _g(tR, 0.95, 0.0105), _g(tR + 0.055, -0.28, 0.028)]
        T = (tR + 0.3, 0.25, 0.05)
    elif kind == "lbbb_v1":
        out += [_g(tR - 0.03, 0.08, 0.008), _g(tR + 0.04, -1.25, 0.036)]
        T = (tR + 0.31, 0.32, 0.055)
    elif kind == "lbbb_v6":
        out += [_g(tR - 0.006, 0.82, 0.024), _g(tR + 0.062, 0.88, 0.024)]
        T = (tR + 0.33, -0.3, 0.06)
    elif kind == "lvh_v1":
        out += [_g(tR - 0.01, 0.15, 0.01), _g(tR + 0.025, -2.0, 0.013)]
        T = (tR + 0.27, 0.3, 0.05)
    elif kind == "lvh_v5":
        out += [_g(tR - 0.026, -0.08, 0.007), _g(tR, 2.2, 0.011), _g(tR + 0.028, -0.15, 0.009)]
        T = (tR + 0.27, -0.35, 0.05)
        out.append(_g(tR + 0.13, -0.12, 0.05))          # strain ST ต่ำลงแบบลาดลง
    elif kind == "wide_k":             # hyperkalemia รุนแรง: QRS กว้าง กลืน T
        out += [_g(tR + 0.02, 0.7, 0.04), _g(tR + 0.11, -0.45, 0.04)]
        T = (tR + 0.3, 0.7, 0.05)
    if peaked:
        T = (T[0] - 0.02, 0.85, 0.028)
    out.append(_g(*T))
    if st:
        out.append(_g(tR + 0.15, st, 0.065))
    if u:
        out.append(_g(tR + 0.5, u, 0.04))
    return out


def _flutter(t):
    f = (t * 5.0) % 1.0
    return -0.22 * f + 0.11 if f < 0.85 else 0.11 - 0.22 * 0.85 + (f - 0.85) / 0.15 * 0.22 * 0.85


def _fib(t):
    return 0.045 * math.sin(2 * math.pi * 6.3 * t) + 0.035 * math.sin(2 * math.pi * 8.7 * t + 1.1) + 0.025 * math.sin(2 * math.pi * 11.9 * t + 2.3)


def _vf(t):
    env = 0.62 + 0.38 * math.sin(2 * math.pi * 0.55 * t + 0.4)
    return env * (0.55 * math.sin(2 * math.pi * 4.6 * t) + 0.22 * math.sin(2 * math.pi * 7.3 * t + 0.8))


def _sine(t):
    return 0.75 * math.sin(2 * math.pi * 2.2 * t)


BASES = {"flutter": _flutter, "fib": _fib, "vf": _vf, "sine": _sine}


def _trace(x0, ybase, dur, comps, base=None, k=K, step=1.0, c="ln", sw=1.6):
    pts = []
    n = int(dur * 25 * k / step)
    for i in range(n + 1):
        px = i * step
        tt = px / (25.0 * k)
        v = sum(a * math.exp(-0.5 * ((tt - cc) / ss) ** 2) for cc, a, ss in comps if abs(tt - cc) < 5 * ss)
        if base:
            v += BASES[base](tt)
        pts.append("%s %s" % (round(x0 + px, 1), round(ybase - v * 10 * k, 1)))
    return ('<path d="M%s" class="%s" style="stroke-width:%s;stroke-linejoin:round;stroke-linecap:round"/>'
            % (" L".join(pts), c, sw))


def _grid(x0, y0, w_mm, h_mm, k=K):
    w, h = w_mm * k, h_mm * k
    sm = "".join("M%s %sV%s" % (round(x0 + i * k, 1), y0, y0 + h) for i in range(w_mm + 1) if i % 5) + \
         "".join("M%s %sH%s" % (x0, round(y0 + j * k, 1), x0 + w) for j in range(h_mm + 1) if j % 5)
    lg = "".join("M%s %sV%s" % (round(x0 + i * k, 1), y0, y0 + h) for i in range(0, w_mm + 1, 5)) + \
         "".join("M%s %sH%s" % (x0, round(y0 + j * k, 1), x0 + w) for j in range(0, h_mm + 1, 5))
    return ('<path d="%s" class="lbad" style="stroke-width:.35;opacity:.22"/>' % sm +
            '<path d="%s" class="lbad" style="stroke-width:.7;opacity:.42"/>' % lg)


def strip(x0, y0, dur, comps, base=None, h_mm=20, k=K, base_at=0.62, label=None, lc="sm b", grid=True):
    """แถบ ECG บนกระดาษกราฟ — คืน (svg parts, ฟังก์ชัน x(t), y baseline)"""
    w_mm = int(round(dur * 25))
    yb = y0 + h_mm * k * base_at
    out = [_grid(x0, y0, w_mm, h_mm, k)] if grid else []
    out.append(_trace(x0, yb, dur, comps, base, k))
    if label:
        out.append(t(x0 + 4, y0 + 13, label, lc))
    X = lambda tt: x0 + tt * 25 * k
    return "".join(out), X, yb


def rhythm(times, **kw):
    out = []
    for tR in times:
        out += beat(tR, **kw)
    return out


def _ticks(X, y, t1, t2, s, c="lmu", tc="xs mid i2", above=True):
    d = -1 if above else 1
    out = [line(X(t1), y, X(t2), y, c), line(X(t1), y - 4, X(t1), y + 4, c), line(X(t2), y - 4, X(t2), y + 4, c)]
    out.append(t((X(t1) + X(t2)) / 2, y + (-6 if above else 14), s, tc))
    return "".join(out)


# ───────────────────────────── 1. คลื่นพื้นฐาน
def beat_anatomy():
    k = 9
    k = 8.5
    comps = beat(0.36, pr=0.16)
    s, X, yb = strip(10, 30, 0.8, comps, h_mm=26, k=k, base_at=0.66, grid=True)
    y = 30 + 26 * k
    out = [s,
           t(X(0.195), yb - 40, "P", "b tac mid"), t(X(0.36), 50, "R", "b mid"), t(X(0.335), yb + 26, "Q", "sm mid i2"),
           t(X(0.392), yb + 34, "S", "sm mid i2"), t(X(0.62), yb - 45, "T", "b tac mid"),
           _ticks(X, y + 18, 0.155, 0.32, "PR 0.12–0.20 s", above=False),
           _ticks(X, y + 40, 0.32, 0.41, "QRS < 0.12 s", above=False),
           _ticks(X, y + 62, 0.32, 0.73, "QT (แก้ตาม HR = QTc)", above=False),
           path("M%s %s L%s %s" % (X(0.41), yb - 2, X(0.52), yb - 2), "lac w2"),
           t(X(0.46), yb + 18, "ST", "xs b tac mid"),
           box(10, 30 + 26 * k + 84, 400, 52, "sk", None),
           t(20, 30 + 26 * k + 104, "1 ช่องเล็ก = 1 mm = 0.04 s · 0.1 mV", "xs i2"),
           t(20, 30 + 26 * k + 124, "1 ช่องใหญ่ = 5 mm = 0.20 s · 0.5 mV · 25 mm/s · 10 mm = 1 mV", "xs i2")]
    return fig("หนึ่งจังหวะบนกระดาษ ECG — แต่ละคลื่นคือไฟฟ้าผ่านส่วนไหน",
               "**P** = ไฟฟ้ากระจายผ่าน atrium · **PR** = เวลาตั้งแต่ atrium เริ่มจนถึง ventricle เริ่ม (ส่วนใหญ่คือการหน่วงใน AV node) · "
               "**QRS** = ventricle depolarize ผ่าน His–Purkinje · **ST** = ventricle depolarize ครบแล้ว ทุกเซลล์ศักย์เท่ากัน จึงควรแบนอยู่ระดับเดียวกับ PR · "
               "**T** = ventricle repolarize · ค่าปกติตามสไลด์: P < 2.5 ช่องเล็ก · PR < 1 ช่องใหญ่ · QRS < 3 ช่องเล็ก",
               svg(420, 30 + 26 * k + 142, "ECG หนึ่งจังหวะพร้อมชื่อคลื่นและช่วงเวลา PR QRS QT บนกระดาษกราฟ", *out))


def conduction():
    rows = [("SA node", "จุดกำเนิด · 60–100/นาที", "ac", "P เริ่ม"),
            ("Atrium", "ไฟฟ้ากระจายทั่ว atrium", "bx", "P wave"),
            ("AV node", "หน่วงช้า ~0.1 s ให้ atrium บีบเลือดลง ventricle ก่อน", "ms", "PR segment แบน"),
            ("His → bundle branch", "ทางด่วน แยกซ้าย–ขวา", "bx", "QRS เริ่ม"),
            ("Purkinje → ventricle", "กระจายทั่ว ventricle ใน < 0.12 s", "ok", "QRS แคบ"),
            ("Ventricle repolarize", "เซลล์กลับสู่ศักย์พัก", "sk", "T wave")]
    out = []
    for i, (a, b, c, w) in enumerate(rows):
        y = 10 + i * 56
        out += [box(10, y, 170, 44, c, a, "b", fs=13), t(194, y + 18, b, "xs i2"), pill(300, y + 24, w, "sk", "xs b mid", w=110)]
        if i < len(rows) - 1:
            out.append(ar(95, y + 44, 95, y + 56, "ln", "ah"))
    return fig("ทางเดินไฟฟ้าในหัวใจ กับคลื่นที่เห็นบน ECG",
               "ลำดับนี้คือคำอธิบายว่าทำไม **PR ยาว = AV conduction ช้า (heart block)** · **QRS กว้าง = ventricle ไม่ได้ depolarize ผ่านทางด่วน** "
               "(bundle branch block หรือจังหวะเกิดจาก ventricle เอง) · AV node เป็นจุดเดียวที่ไฟฟ้าจาก atrium ลงสู่ ventricle ได้ในคนปกติ",
               svg(420, 10 + 6 * 56 - 4, "ลำดับการนำไฟฟ้าจาก SA node ผ่าน atrium AV node His bundle Purkinje และคลื่น ECG ที่ตรงกัน", *out))


# ───────────────────────────── 2. lead
def chest_leads():
    cx = 210
    out = [path("M110 20 Q 210 0 310 20 L 330 330 Q 210 350 90 330 Z", "sk"),
           rect(cx - 14, 30, 28, 220, "bx", 6), t(cx, 262, "sternum", "xs mid mu")]
    ics = {2: 70, 3: 115, 4: 160, 5: 205}
    for n, y in ics.items():
        out += [path("M120 %d Q 210 %d 300 %d" % (y, y - 8, y), "lmu da"), t(104, y + 4, "ICS%d" % n, "xs end mu")]
    std = [("V1", cx - 26, 160, "ok"), ("V2", cx + 26, 160, "ok")]
    hi = [("V1-1", cx - 26, 115), ("V2-1", cx + 26, 115), ("V1-2", cx - 26, 70), ("V2-2", cx + 26, 70)]
    oth = [("V3", cx + 52, 182), ("V4", cx + 74, 205), ("V5", cx + 94, 208), ("V6", cx + 112, 211)]
    for nm, x, y, c in std:
        out += [circ(x, y, 9, c), t(x, y + 4, nm, "xs b mid")]
    for nm, x, y in hi:
        out += [circ(x, y, 11, "ac"), t(x, y + 4, nm, "xs b mid tac")]
    for nm, x, y in oth:
        out += [circ(x, y, 9, "bx"), t(x, y + 4, nm, "xs mid")]
    out += [t(cx - 70, 300, "ขวาของผู้ป่วย", "xs mid mu"), t(cx + 70, 300, "ซ้ายของผู้ป่วย", "xs mid mu"),
            box(10, 350, 400, 50, "ac", None), t(20, 370, "Brugada leads (สีเข้ม): ย้าย V1/V2 ขึ้นไป ICS3 และ ICS2", "xs b tac"),
            t(20, 388, "โดยใช้ขั้ว V3–V6 มาติดแทน · มองตามภาพหันหน้าเข้าหาผู้ป่วย", "xs i2")]
    return fig("ตำแหน่ง chest lead มาตรฐาน และ Brugada leads (สไลด์)",
               "V1 = ขวา sternum ICS4 · V2 = ซ้าย ICS4 · **Brugada leads**: V1-1/V2-1 ที่ ICS3 และ V1-2/V2-2 ที่ ICS2 (ย้ายขั้ว V3–V6 มาใช้) — "
               "เพราะ RVOT อยู่สูงกว่าตำแหน่ง V1–V2 ปกติ ลักษณะ coved ST elevation ของ Brugada จึงเห็นชัดขึ้นเมื่อขยับ lead ขึ้น · "
               "สไลด์ย้ำว่าติดผิด ICS ไป 1 ช่องหรือให้นั่งแทนนอน ทำให้ QRST เปลี่ยนได้มาก",
               svg(420, 406, "ภาพหน้าอกแสดงตำแหน่ง V1 ถึง V6 และ Brugada leads ที่ ICS3 และ ICS2", *out))


def lewis():
    out = [path("M90 20 Q 190 0 290 20 L 300 300 Q 190 320 80 300 Z", "sk"), rect(176, 30, 28, 210, "bx", 6),
           circ(150, 58, 12, "ac"), t(150, 62, "RA", "xs b mid tac"), t(120, 48, "ICS2 ขวา", "xs end i2"),
           circ(150, 150, 12, "ac"), t(150, 154, "LA", "xs b mid tac"), t(120, 150, "ICS4 ขวา", "xs end i2"),
           circ(120, 268, 12, "ac"), t(120, 272, "LL", "xs b mid tac"), t(102, 292, "ชายโครงขวา", "xs mid i2"),
           ar(150, 72, 150, 136, "lac w2", "ah-ac", "lead I", "xs b tac", dx=24, dy=4),
           box(318, 40, 96, 150, "bx", None), t(366, 62, "Lewis lead", "xs b mid"),
           t(366, 84, "ขั้วสองขั้วอยู่", "xs mid i2"), t(366, 100, "ตามแนว atrium", "xs mid i2"),
           t(366, 120, "→ อ่าน lead I", "xs mid tac b"), t(366, 140, "P / คลื่น flutter", "xs mid i2"),
           t(366, 156, "ใหญ่ขึ้น เห็นชัด", "xs mid i2")]
    return fig("Lewis lead — ทำให้ P wave ที่ซ่อนอยู่โผล่ (สไลด์)",
               "ย้ายขั้วแขนมาไว้บนหน้าอกขวา: **RA = ICS2 ขวา (หรือ manubrium) · LA = ICS4 ขวา · LL = ชายโครงขวา** · chest leads ตามปกติ · "
               "lead I จึงวัดตามแนวยาวของ atrium พอดี → P wave/คลื่น flutter ใหญ่ขึ้น ใช้แยก VT (มี AV dissociation) หรือหา P ที่ซ่อนใน tachycardia",
               svg(420, 320, "ตำแหน่งขั้ว RA LA LL ของ Lewis lead บนหน้าอกด้านขวา", *out))


# ───────────────────────────── 3. rate
def rate_count():
    times = [0.2 + 0.8 * i for i in range(5)]
    s, X, yb = strip(10, 30, 4.0, rhythm(times), h_mm=18)
    out = [s]
    labs = ["R", "300", "150", "100", "75", "60", "50"]
    for i, lab in enumerate(labs):
        x = X(0.2 + 0.2 * i)
        out += [line(x, 22, x, 30, "lac"), t(x, 18, lab, "xs b mid " + ("tbad" if lab == "75" else "tac"))]
    out += [t(10, 130, "R ตัวถัดไปตกที่เส้นใหญ่เส้นที่ 4 → 75/นาที  (= 300 ÷ 4 ช่องใหญ่ = 1500 ÷ 20 ช่องเล็ก)", "xs i2"),
            t(10, 150, "จังหวะไม่สม่ำเสมอ: นับ QRS ในแถบ 6 วินาที (30 ช่องใหญ่) × 10", "xs i2")]
    return fig("นับ rate: 300 / ช่องใหญ่ · 1500 / ช่องเล็ก",
               "กระดาษวิ่ง 25 mm/s → 1 ช่องใหญ่ = 0.2 s → ใน 1 นาทีมี **300 ช่องใหญ่** · ถ้า R ห่างกัน n ช่องใหญ่ HR = 300/n · "
               "เลขจำ (golden number ที่จดในสไลด์) **300 – 150 – 100 – 75 – 60 – 50** · ต้องการละเอียดใช้ 1500/ช่องเล็ก · "
               "จังหวะไม่สม่ำเสมอ (AF) ใช้ 6 วินาที × 10 (ตัวอย่างในสไลด์ 13 × 6 = 78 ใช้แถบ 10 วินาที)",
               svg(420, 160, "แถบ ECG 75 ครั้งต่อนาทีพร้อมเลข 300 150 100 75 60 50 บนเส้นช่องใหญ่", *out))


def rate_bands():
    X = lambda v: 20 + v * 1.0
    segs = [(0, 60, "bad", "brady\n< 60"), (60, 100, "ok", "ปกติ\n60–100"), (100, 250, "ms", "tachycardia\n101–250"),
            (250, 350, "ac", "flutter\n250–350"), (350, 400, "bad", "fib\n> 350")]
    out = []
    for a, b, c, s in segs:
        out.append(box(X(a), 40, X(b) - X(a), 46, c, s, "xs b", fs=11))
    for v in (0, 60, 100, 250, 350):
        out.append(t(X(v), 102, str(v), "xs mid mu"))
    pace = [("ventricle", 20, 40, 130), ("junction", 40, 60, 152), ("sinus", 60, 100, 174)]
    for nm, a, b, y in pace:
        out += [rect(X(a), y - 10, X(b) - X(a), 12, "sk", 3), t(X(b) + 6, y, nm + " " + "%d–%d" % (a, b), "xs i2")]
    out += [t(20, 26, "อัตราของ \"ห้องที่เต้น\" (atrial rate สำหรับ flutter/fib)", "xs b"),
            t(20, 206, "เร็วกว่าอัตราประจำตัวของจุดนั้น แต่ ≤ 100 = accelerated rhythm", "xs tac b"),
            t(20, 224, "เช่น AIVR 50–100 · accelerated junctional 60–100", "xs i2")]
    return fig("ช่วงอัตรา (สไลด์) และอัตราประจำตัวของแต่ละจุดกำเนิด",
               "สไลด์ให้ 5 ช่วง: bradycardia < 60 · tachycardia 101–250 · flutter 250–350 · fibrillation > 350 · และ **accelerated** "
               "(จดในสไลด์ว่า \"if not sinus\") = จังหวะที่ไม่ใช่ sinus แต่เร็วกว่าอัตราประจำตัวของจุดนั้น เช่น ventricle ปกติยิง 20–40 ถ้ายิง 60–100 = AIVR",
               svg(420, 234, "แถบอัตราการเต้น bradycardia ปกติ tachycardia flutter fibrillation และอัตราประจำตัวของ sinus junction ventricle", *out))


# ───────────────────────────── 4. rhythm
def pacemaker_ladder():
    levels = [("SA node", "60–100", "ok", "เร็วสุด → คุมจังหวะ"), ("Atrium (ectopic)", "60–100", "bx", "P รูปร่างแปลก"),
              ("AV junction", "40–60", "ms", "P หัวกลับ/ไม่เห็น"), ("Ventricle", "20–40", "bad", "QRS กว้าง")]
    out = []
    for i, (a, r_, c, d) in enumerate(levels):
        y = 14 + i * 64
        out += [box(20, y, 150, 48, c, a + "\n" + r_ + "/นาที", "b", fs=12), t(186, y + 28, d, "sm i2")]
        if i < 3:
            out.append(ar(95, y + 48, 95, y + 64, "lmu", "ah-mu"))
    out += [path("M282 40 C 330 40, 330 220, 282 220", "lok w2", "ah-ok"), t(326, 120, "overdrive", "xs b tok"),
            t(326, 136, "suppression", "xs b tok"),
            path("M290 228 C 250 250, 250 250, 210 244", "lbad da", "ah-bad"), t(250, 270, "ตัวบนหยุด → ตัวล่าง escape", "xs mid tbad")]
    return fig("ลำดับชั้นของจุดกำเนิดไฟฟ้า — ใครเร็วกว่าคุม",
               "ทุกจุดยิงไฟฟ้าเองได้ (automaticity) แต่จุดที่เร็วที่สุด (SA node) ไปถึงก่อนและ **รีเซ็ตจุดล่างทุกจังหวะ (overdrive suppression)** · "
               "ถ้าจุดบนหยุด (sick sinus, AV block) จุดล่างจะยิงตามอัตราของตัวเอง = **escape rhythm** — จึงยิ่งต่ำยิ่งช้าและ QRS ยิ่งกว้าง",
               svg(420, 282, "ลำดับ SA node atrium AV junction ventricle พร้อมอัตราประจำตัวและลูกศร overdrive suppression กับ escape", *out))


def four_rhythms():
    rows = [("Sinus · 75", dict(), [0.3 + 0.8 * i for i in range(5)], "ok"),
            ("Ectopic atrial · P แปลกรูป", dict(p_inv=True, pr=0.14), [0.3 + 0.82 * i for i in range(5)], "ac"),
            ("Junctional · 50 · ไม่เห็น P", dict(p=False), [0.4 + 1.2 * i for i in range(3)], "ms"),
            ("Ventricular · 35 · QRS กว้าง", dict(kind="v", p=False), [0.5 + 1.7 * i for i in range(3)], "bad")]
    out = []
    for i, (lab, kw, times, c) in enumerate(rows):
        y = 8 + i * 86
        s, X, yb = strip(10, y + 16, 3.9, rhythm(times, **kw), h_mm=15)
        out += [t(12, y + 11, lab, "xs b t" + c), s]
    return fig("4 จังหวะพื้นฐาน (สไลด์) — แยกด้วย P, PR และความกว้าง QRS (lead II)",
               "**Sinus**: P ตั้งใน I/II/aVF รูปเดียวกันทุกตัว PR 0.12–0.20 · **Atrial**: P ไม่ใช่ sinus P (จดในสไลด์ \"not from SA node\") · "
               "**Junctional** 40–60: P หัวกลับใน II/III/aVF หรือมองไม่เห็นเพราะซ่อนใน QRS · **Ventricular** 20–40: ไม่มี P QRS > 0.12 s "
               "และ T ชี้สวนทาง QRS (repolarize ผิดลำดับ)",
               svg(420, 8 + 4 * 86, "แถบ ECG สี่แบบ sinus atrial junctional และ ventricular rhythm", *out))


def p_axis():
    out = [path("M150 40 C 90 60, 70 160, 120 230 C 160 285, 260 300, 300 250 C 340 200, 330 90, 280 60 C 240 30, 190 30, 150 40 Z", "sk"),
           circ(140, 70, 10, "ok"), t(118, 60, "SA", "xs b end tok"), circ(212, 160, 10, "ms"), t(228, 156, "AV", "xs b tms"),
           ar(148, 78, 202, 150, "lok w3", "ah-ok"), t(150, 128, "sinus", "xs b tok"),
           ar(204, 166, 150, 92, "lbad w2 da", "ah-bad"), t(196, 112, "junctional", "xs b tbad"),
           path("M60 300 L 330 300", "lmu"),
           ar(250, 30, 330, 168, "lac w2", "ah-ac"), t(338, 182, "lead II", "xs b tac"),
           t(338, 198, "(+60°)", "xs tac"),
           box(10, 312, 400, 52, "bx", None),
           t(20, 332, "ไฟฟ้าวิ่งเข้าหา lead → คลื่นตั้ง · วิ่งหนี → คลื่นหัวกลับ", "xs b"),
           t(20, 352, "sinus วิ่งลงล่างซ้าย (เข้าหา II) · junctional วิ่งย้อนขึ้นบน (หนี II, III, aVF)", "xs i2")]
    return fig("ทำไม P ของ sinus ตั้งใน II แต่ P ของ junctional หัวกลับ",
               "SA node อยู่บนขวา AV node อยู่ล่างซ้าย → ไฟฟ้าใน atrium ของ sinus วิ่ง **ลงล่างซ้าย ขนานกับ lead II** → P ตั้งใน I, II, aVF (เกณฑ์ข้อแรกของ sinus) · "
               "จังหวะที่เกิดใน AV junction กระตุ้น atrium **ย้อนจากล่างขึ้นบน (retrograde)** → P หัวกลับใน II, III, aVF และมักมาชิด/ซ่อนใน QRS → PR สั้นมากหรือไม่เห็น",
               svg(420, 372, "ทิศของไฟฟ้าใน atrium จาก SA node ลงล่างซ้ายเทียบกับ junctional ที่ย้อนขึ้น และทิศของ lead II", *out))


# ───────────────────────────── 5. premature / escape
def premature():
    comps = rhythm([0.3, 1.1, 1.9]) + beat(2.38, kind="v", p=False) + rhythm([3.5])
    s, X, yb = strip(10, 26, 4.0, comps, h_mm=20)
    out = [s, t(X(2.38), 22, "PVC", "xs b mid tbad"),
           _ticks(X, 26 + 80 + 14, 1.9, 3.5, "สองช่วง RR พอดี = full compensatory pause", above=False),
           _ticks(X, 26 + 80 + 38, 1.9, 2.7, "RR ปกติ 0.8 s", above=False)]
    return fig("Premature beat — มาก่อนจังหวะ แล้วตามด้วย pause",
               "**PVC**: เซลล์ใน ventricle ยิงเองก่อนกำหนด → QRS กว้าง ไม่มี P นำ T สวนทาง · SA node **ไม่ถูกรีเซ็ต** (ไฟฟ้าย้อนไม่ถึง) "
               "แต่ P ถัดไปตกช่วงที่ ventricle ยังดื้ออยู่ → ช่วงห่างรวมเท่ากับ 2 RR พอดี (full compensatory pause) · "
               "**PAC** มี P แปลกรูปมาก่อนเวลาและรีเซ็ต SA node → pause ไม่ครบ · PVC ทุกจังหวะสลับ = **bigeminy** (ตัวอย่างในสไลด์)",
               svg(420, 26 + 80 + 66, "แถบ ECG มี PVC ตามด้วย compensatory pause ที่ยาวเท่าสองช่วง RR", *out))


def escape():
    comps = rhythm([0.3, 1.1]) + beat(3.0, p=False) + rhythm([3.8])
    s, X, yb = strip(10, 26, 4.0, comps, h_mm=20)
    out = [s, _ticks(X, 22, 1.1, 3.0, "sinus หยุด (sinus pause / SSS)", c="lbad", tc="xs mid tbad"),
           t(X(3.0), 26 + 80 + 16, "junctional escape", "xs b mid tms"), t(X(3.0), 26 + 80 + 30, "(ไม่มี P · QRS แคบ)", "xs mid i2")]
    return fig("Escape beat — มาหลัง pause ยาว เพื่อกันหัวใจหยุด",
               "ต่างจาก premature beat ตรงที่ **มาช้ากว่ากำหนด** · SA node หยุด (เช่น **sick sinus syndrome** ที่จดในสไลด์) หรือ AV block → "
               "จุดล่างที่ถูกกดไว้พ้นจาก overdrive suppression แล้วยิงเองตามอัตราประจำตัว · escape เป็น **กลไกช่วยชีวิต ห้ามให้ยากด**",
               svg(420, 26 + 80 + 40, "แถบ ECG sinus หยุดเป็นช่วงยาว ตามด้วย junctional escape beat", *out))


def aivr():
    comps = rhythm([0.3, 1.25], pr=0.16) + rhythm([2.1, 2.95, 3.8], kind="v", p=False)
    s, X, yb = strip(10, 26, 4.0, comps, h_mm=20)
    out = [s, t(X(0.75), 22, "sinus ~63", "xs b mid tok"), t(X(3.0), 22, "AIVR ~70 · QRS กว้าง", "xs b mid tms")]
    return fig("Accelerated idioventricular rhythm (AIVR) — reperfusion arrhythmia",
               "ventricle ยิงเองเร็วกว่าปกติของมัน (20–40) จนขึ้นมาราว **50–110** ใกล้ sinus จึงแย่งคุมจังหวะกันได้ · พบบ่อยหลัง **เปิดหลอดเลือดใน STEMI** "
               "(ลายมือในสไลด์: \"MI → treat → reperfusion arrhythmia\") · มักหายเอง ไม่ต้องให้ยาต้าน arrhythmia เพราะเป็นสัญญาณว่าเลือดกลับมาเลี้ยง",
               svg(420, 26 + 80 + 12, "แถบ ECG sinus สองจังหวะต่อด้วย accelerated idioventricular rhythm QRS กว้างอัตราราว 70", *out))


# ───────────────────────────── 6. tachy
def tachy():
    rows = [("Sinus tachycardia 120 · มี P ตั้งนำทุก QRS", "ok", rhythm([0.25 + 0.5 * i for i in range(8)], pr=0.13, t_amp=0.22), None),
            ("Atrial flutter 2:1 → 150 · ฟันเลื่อย 300", "ac", rhythm([0.3 + 0.4 * i for i in range(10)], p=False, t_amp=0.12), "flutter"),
            ("AF · ไม่มี P · RR ไม่สม่ำเสมอแบบสุ่ม", "ms", rhythm([0.2, 0.62, 1.32, 1.7, 2.45, 2.8, 3.55], p=False, t_amp=0.15), "fib"),
            ("VT ~180 · QRS กว้างสม่ำเสมอ", "bad", rhythm([0.15 + 0.333 * i for i in range(12)], kind="v", p=False), None),
            ("VF · คลื่นยุ่งเหยิง ไม่มี QRS", "bad", [], "vf")]
    out = []
    for i, (lab, c, comps, base) in enumerate(rows):
        y = 6 + i * 84
        s, X, yb = strip(10, y + 16, 4.0, comps, base, h_mm=15, base_at=0.58)
        out += [t(12, y + 11, lab, "xs b t" + c), s]
    return fig("Tachyarrhythmia ที่ต้องจำหน้าตา (สไลด์ p42–46)",
               "**Flutter**: วงไฟฟ้าวนรอบ tricuspid valve 300/นาที → คลื่นฟันเลื่อยชัดใน II, III, aVF · AV node ปล่อยลงครึ่งเดียว (2:1) → "
               "**HR 150 คงที่** ให้นึกถึง flutter เสมอ · **AF**: วงไฟฟ้าเล็ก ๆ หลายวง > 350 → ไม่มี P และ RR สุ่ม · "
               "**VT**: วงไฟฟ้าใน ventricle (มักรอบแผลเป็นเก่า) → QRS กว้าง · **VF**: ventricle สั่นไม่บีบ = หัวใจหยุดเต้น",
               svg(420, 6 + 5 * 84, "แถบ ECG sinus tachycardia atrial flutter atrial fibrillation ventricular tachycardia และ ventricular fibrillation", *out))


def reentry():
    out = [path("M150 60 C 80 60, 80 220, 150 220", "lms w3", "ah-ms"), t(76, 140, "ทางช้า", "sm b end tms"),
           t(76, 158, "(ฟื้นตัวเร็ว)", "xs end i2"),
           path("M150 220 C 220 220, 220 60, 150 60", "lwa w3"), t(222, 140, "ทางเร็ว", "sm b twa"), t(222, 158, "(ฟื้นตัวช้า)", "xs i2"),
           path("M150 20 L150 60", "ln w2", "ah"), t(158, 34, "PAC มาก่อนเวลา", "xs i2"),
           path("M196 128 L 212 140", "lbad w3"), path("M196 140 L 212 128", "lbad w3"),
           t(222, 100, "ทางเร็วยังดื้อ → ติด", "xs tbad b"),
           path("M150 220 L150 262", "ln w2", "ah"), t(158, 252, "ลง ventricle", "xs i2"),
           box(252, 176, 164, 82, "ac", None), t(334, 198, "ไฟฟ้าย้อนขึ้นทางเร็ว", "xs b mid tac"),
           t(334, 216, "ที่ฟื้นแล้ว → วนไม่รู้จบ", "xs mid i2"), t(334, 236, "adenosine บล็อก AV node", "xs mid b tok"),
           t(334, 252, "ชั่วขณะ → ตัดวง", "xs mid tok")]
    return fig("Re-entry — กลไกของ AVNRT (และ flutter, VT)",
               "ต้องมี **2 ทาง** ที่ความเร็วและระยะดื้อต่างกัน + **block ทางเดียว** + ทางช้าพอให้อีกทางฟื้น · PAC ที่มาก่อนเวลาเจอทางเร็วยังดื้อ "
               "จึงลงทางช้า แล้วย้อนขึ้นทางเร็ว → วนต่อเนื่อง ~150–250/นาที · **วงของ AVNRT อยู่ใน AV node** → vagal maneuver/adenosine ที่ทำให้ AV node ดื้อชั่วขณะ จึงตัดวงได้",
               svg(420, 280, "วงจร re-entry ใน AV node ที่มีทางช้าและทางเร็ว PAC ติด block ในทางเร็วแล้ววนกลับ", *out))


def acls():
    out = [box(130, 6, 160, 34, "bx", "Tachycardia + ชีพจร?", "b", fs=12),
           ar(160, 40, 70, 64, "lbad", "ah-bad"), t(96, 52, "ไม่มี", "xs tbad end"),
           box(6, 64, 150, 50, "bad", "VF / pulseless VT\n→ CPR + defibrillate", "b", fs=11),
           t(81, 128, "(unsynchronized)", "xs mid tbad"),
           ar(260, 40, 300, 64, "lok", "ah-ok"), t(296, 52, "มี", "xs tok"),
           box(230, 64, 184, 50, "ms", "unstable? ช็อก สับสน\nเจ็บหน้าอก HF", "b", fs=11),
           ar(300, 114, 300, 140, "lbad", "ah-bad"), t(306, 130, "ใช่", "xs tbad"),
           box(230, 140, 184, 40, "bad", "Synchronized cardioversion", "b", fs=11),
           ar(240, 114, 150, 150, "lok", "ah-ok"), t(178, 132, "ไม่", "xs tok"),
           box(20, 150, 180, 40, "bx", "stable → ดู QRS", "b", fs=12),
           ar(70, 190, 60, 212, "ln", "ah"), ar(150, 190, 230, 212, "ln", "ah"),
           box(6, 212, 150, 82, "ok", None), t(81, 232, "แคบ + สม่ำเสมอ", "xs b mid tok"),
           t(81, 250, "1 vagal maneuver", "xs mid"), t(81, 266, "2 adenosine 6 → 12 mg", "xs mid"),
           t(81, 282, "IV push เร็ว + flush", "xs mid i2"),
           box(176, 212, 238, 82, "ms", None), t(295, 232, "กว้าง (คิดว่า VT จนกว่าจะพิสูจน์)", "xs b mid tms"),
           t(295, 252, "amiodarone / procainamide", "xs mid"), t(295, 270, "พร้อม cardioversion · ปรึกษา", "xs mid i2"),
           t(295, 286, "AF/flutter แคบ: คุม rate", "xs mid i2")]
    return fig("Tachycardia ที่มีชีพจร vs ไม่มีชีพจร (AHA ACLS — ไม่อยู่ในสไลด์)",
               "คำถามแรกเสมอคือ **มีชีพจรไหม** · ไม่มี = cardiac arrest → CPR + **defibrillation แบบไม่ sync** · มีชีพจรแต่ไม่เสถียร "
               "(hypotension, สับสน, ischemic chest pain, acute HF) → **synchronized cardioversion** (sync ให้ช็อกตรง R ไม่ตกช่วง T ที่จะเหนี่ยวนำ VF) · "
               "เสถียร → แยกตาม QRS แคบ/กว้าง",
               svg(420, 300, "แผนภูมิการรักษา tachycardia ตามการมีชีพจร ความเสถียร และความกว้างของ QRS", *out))


# ───────────────────────────── 8. axis
def hexaxial():
    cx, cy, R = 162, 150, 100
    leads = [("I", 0), ("II", 60), ("III", 120), ("aVF", 90), ("aVL", -30), ("aVR", -150)]
    out = [path("M%s %s L%s %s A%s %s 0 0 1 %s %s Z" % (cx, cy, cx + R * math.cos(math.radians(-30)), cy + R * math.sin(math.radians(-30)),
                                                       R, R, cx, cy + R), "ok"),
           path("M%s %s L%s %s A%s %s 0 0 1 %s %s Z" % (cx, cy, cx, cy + R, R, R, cx - R, cy), "ms"),
           path("M%s %s L%s %s A%s %s 0 0 0 %s %s Z" % (cx, cy, cx + R * math.cos(math.radians(-30)), cy + R * math.sin(math.radians(-30)),
                                                       R, R, cx, cy - R), "ac"),
           path("M%s %s L%s %s A%s %s 0 0 1 %s %s Z" % (cx, cy, cx - R, cy, R, R, cx, cy - R), "bad")]
    for nm, a in leads:
        x = cx + (R + 10) * math.cos(math.radians(a)); y = cy + (R + 10) * math.sin(math.radians(a))
        out += [line(cx, cy, cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)), "ln"),
                t(x + (6 if math.cos(math.radians(a)) > 0.2 else -6 if math.cos(math.radians(a)) < -0.2 else 0), y + 4,
                  "%s %s°" % (nm, ("+%d" % a) if a > 0 else str(a)), "xs b " + ("" if abs(math.cos(math.radians(a))) <= 0.2 else "end" if math.cos(math.radians(a)) < 0 else ""))]
    out += [t(cx + 46, cy + 46, "ปกติ", "sm b tok"), t(cx + 46, cy + 62, "−30 ถึง +90", "xs tok"),
            t(cx - 60, cy + 46, "RAD", "sm b tms mid"), t(cx + 54, cy - 40, "LAD", "sm b tac"),
            t(cx - 60, cy - 40, "extreme", "sm b tbad mid")]
    tb = [("lead I", "aVF", "แปลผล"), ("+", "+", "ปกติ"), ("+", "−", "LAD*"), ("−", "+", "RAD"), ("−", "−", "extreme")]
    for i, row in enumerate(tb):
        y = 40 + i * 26
        out += [t(334, y, row[0], "xs mid" + (" b" if i == 0 else "")), t(368, y, row[1], "xs mid" + (" b" if i == 0 else "")),
                t(404, y, row[2], "xs mid" + (" b" if i == 0 else ""))]
    out += [t(316, 182, "*ดู lead II ต่อ:", "xs i2"), t(316, 198, "II บวก = ยังปกติ", "xs i2"), t(316, 214, "(−30 ถึง 0)", "xs i2")]
    return fig("Axis — ดู lead I กับ aVF แล้ววางลงวงกลม hexaxial",
               "QRS **ตั้ง** ใน lead ใด = ไฟฟ้าเฉลี่ยของ ventricle วิ่ง **เข้าหา** lead นั้น · lead I (0°) บอกซ้าย/ขวา aVF (+90°) บอกบน/ล่าง · "
               "ไฟฟ้าเอียง **เข้าหาด้านที่กล้ามเนื้อหนา (hypertrophy)** และ **หนีด้านที่ตาย (infarct)** — นี่คือสาเหตุ axis เบี่ยงที่จดในสไลด์",
               svg(436, 300, "วงกลม hexaxial แสดง lead I II III aVF aVL aVR และช่วง axis ปกติ LAD RAD และตารางแปลผลจาก lead I กับ aVF", *out))


# ───────────────────────────── 9. infarction
def st_measure():
    k = 9
    comps = beat(0.4, pr=0.16, st=0.22, t_amp=0.38)
    s, X, yb = strip(20, 20, 0.9, comps, h_mm=28, k=k, base_at=0.62)
    j = 0.445
    out = [s, path("M%s %s H%s" % (X(0.2), yb, X(0.88)), "lok da"),
           t(X(0.86), yb + 14, "baseline (PR / TP)", "xs end tok"),
           circ(X(j), yb - 0.13 * 10 * k, 4, "acf"), t(X(j) - 6, yb - 0.13 * 10 * k - 8, "J point", "xs b end tac"),
           line(X(j + 0.06), yb - 2, X(j + 0.06), 30, "lac da"), t(X(j + 0.06) + 4, 40, "J + 60–80 ms", "xs b tac"),
           ar(X(j + 0.12), yb, X(j + 0.12), yb - 0.2 * 10 * k + 2, "lbad w2", "ah-bad"),
           t(X(j + 0.12) + 6, yb - 0.1 * 10 * k, "ST ยก ~2 mm", "xs b tbad")]
    return fig("วัด ST elevation — เทียบกับ PR segment (หรือ TP) ที่ J point",
               "สไลด์: วิธีง่ายสุดคือเทียบ ST กับ **PR segment** · แต่ atrial repolarization (Ta wave) มีทิศตรงข้าม P และกดต่ำ PR ได้ถึง 40–80 ms หลัง QRS → "
               "อีกวิธีคือเทียบกับ **TP segment** ที่ **60 หรือ 80 ms หลัง J point** (J point = จุดที่ QRS จบ ST เริ่ม)",
               svg(730, 20 + 28 * k + 10, "ECG หนึ่งจังหวะที่ ST ยก แสดง baseline J point และตำแหน่งวัด J บวก 60 ถึง 80 มิลลิวินาที", *out))


def territories():
    grid = [["I", "aVR", "V1", "V4"], ["II", "aVL", "V2", "V5"], ["III", "aVF", "V3", "V6"]]
    col = {"I": "ac", "aVL": "ac", "V5": "ac", "V6": "ac", "II": "ms", "III": "ms", "aVF": "ms",
           "V1": "wa", "V2": "wa", "V3": "bad", "V4": "bad", "aVR": "sk"}
    out = []
    for r_, row in enumerate(grid):
        for c_, nm in enumerate(row):
            out.append(box(10 + c_ * 100, 10 + r_ * 50, 92, 42, col[nm], nm, "b", fs=14))
    leg = [("ms", "Inferior: II, III, aVF", "RCA (ส่วนใหญ่)"), ("wa", "Septal: V1–V2", "LAD (septal)"),
           ("bad", "Anterior: V3–V4", "LAD"), ("ac", "Lateral: I, aVL, V5–V6", "LCx / diagonal")]
    for i, (c, a, b) in enumerate(leg):
        y = 176 + i * 30
        out += [rect(10, y - 13, 18, 18, c, 4), t(36, y, a, "xs b"), t(250, y, b, "xs i2")]
    out += [t(10, 306, "ST ยกในหลายกลุ่มติดกัน = แผ่กว้าง (เช่น V2–V6 + I, aVL = anterolateral)", "xs i2"),
            t(10, 324, "ST ต่ำฝั่งตรงข้าม = reciprocal change → ยืนยันว่าเป็น MI", "xs tbad b")]
    return fig("ผนังหัวใจกับ lead ที่มอง (ผัง 12 lead มาตรฐาน)",
               "แต่ละ lead มองผนังหัวใจด้านหนึ่ง · STEMI ต้องเห็น ST ยกใน **2 lead ที่ติดกัน (contiguous)** ของผนังเดียวกัน · "
               "ตัวอย่างในสไลด์ (p80): STE V2–V6, I, aVL + STD II, III, aVF = **acute anterior (anterolateral) MI พร้อม reciprocal change ที่ inferior**",
               svg(420, 334, "ผัง 12 lead ระบายสีตามผนัง inferior septal anterior lateral และหลอดเลือดที่เลี้ยง", *out))


def stemi_evo():
    stages = [("ปกติ", dict()), ("นาที:\nhyperacute T", dict(peaked=True)), ("ชั่วโมง:\nST ยก", dict(st=0.3, t_amp=0.35)),
              ("วัน: Q + T กลับ", dict(q=0.45, r=0.55, st=0.12, t_inv=True)), ("สัปดาห์: Q ค้าง", dict(q=0.45, r=0.55, t_inv=True, t_amp=0.15))]
    out = []
    for i, (lab, kw) in enumerate(stages):
        x = 6 + i * 83
        s, X, yb = strip(x, 40, 0.6, beat(0.2, pr=0.12, **kw), h_mm=22, k=3.2, base_at=0.6)
        out += [s, t(x + 38, 18, lab.split("\n")[0], "xs b mid"), t(x + 38, 32, lab.split("\n")[1] if "\n" in lab else "", "xs mid i2")]
        if i < 4:
            out.append(ar(x + 70, 120, x + 86, 120, "lmu", "ah-mu"))
    return fig("วิวัฒนาการของ STEMI (สไลด์ p68)",
               "**hyperacute T** (T สูงกว้าง) มาก่อน ST ยก → **ST ยก** (กระแส injury จากเซลล์ที่ขาดเลือดทั้งชั้น) → กล้ามเนื้อตาย = ไม่มีไฟฟ้า "
               "lead จึงมองทะลุไปเห็นไฟฟ้าวิ่งหนี = **Q wave** → **T กลับหัว** · ลายมือในสไลด์: ดู **dynamic change** — ECG แรกไม่ชัด ให้ **ทำซ้ำทุก 15–30 นาที**",
               svg(420, 132, "ECG ห้าระยะ ปกติ hyperacute T ST ยก Q wave กับ T กลับหัว และ Q ค้าง", *out))


# ───────────────────────────── 10. hypertrophy
def p_waves():
    out = []
    rows = [("ปกติ", "n", "ok", "< 2.5 mm · < 0.12 s"), ("P pulmonale (RAE)", "pulm", "ms", "สูง > 2.5 mm"),
            ("P mitrale (LAE)", "mitr", "ac", "กว้าง > 0.12 s · หยัก")]
    for i, (lab, pk, c, d) in enumerate(rows):
        x = 6 + i * 138
        s, X, yb = strip(x, 30, 0.52, beat(0.36, pr=0.17, p_kind=pk), h_mm=20, k=5, base_at=0.66)
        out += [s, t(x + 65, 18, lab, "xs b mid t" + c), t(x + 65, 150, d, "xs mid i2")]
    out += [box(6, 162, 408, 68, "bx", None),
            t(16, 182, "P = RA (ขึ้นก่อน) + LA (ตามมา) ซ้อนกัน", "xs b"),
            t(16, 200, "RA โต → ส่วนแรกสูงขึ้น เวลาไม่เพิ่ม → P แหลมสูง", "xs tms"),
            t(16, 218, "LA โต → ส่วนหลังยาวขึ้น → P กว้าง มีสองยอด", "xs tac")]
    return fig("Atrial enlargement จากรูปร่าง P (lead II)",
               "เกณฑ์ในสไลด์: **RA = P สูง > 2.5 mm** · **LA = P กว้าง > 0.12 s (3 mm) และหยัก (notched)** · "
               "P mitrale พบใน mitral stenosis (LA รับแรงดันสูง) · P pulmonale พบใน pulmonary hypertension/COPD",
               svg(420, 236, "P wave ปกติ P pulmonale ที่สูงแหลม และ P mitrale ที่กว้างมีสองยอด", *out))


def lvh():
    s1, X1, yb1 = strip(10, 20, 0.6, beat(0.25, kind="lvh_v1", pr=0.15), h_mm=56, k=3.2, base_at=0.36, label="V1")
    s2, X2, yb2 = strip(220, 20, 0.6, beat(0.25, kind="lvh_v5", pr=0.15), h_mm=56, k=3.2, base_at=0.62, label="V5")
    out = [s1, s2,
           ar(X1(0.3) + 14, yb1, X1(0.3) + 14, yb1 + 20 * 3.2 - 4, "lbad w2", "ah-bad"), t(X1(0.3) + 20, yb1 + 36, "S 20 mm", "xs b tbad"),
           ar(X2(0.25) + 14, yb2, X2(0.25) + 14, yb2 - 22 * 3.2 + 4, "lbad w2", "ah-bad"), t(X2(0.25) + 20, yb2 - 40, "R 22 mm", "xs b tbad"),
           t(X2(0.5), yb2 + 26, "strain: ST ลาดลง", "xs end tms"), t(X2(0.5), yb2 + 40, "+ T กลับหัว", "xs end tms"),
           box(10, 210, 400, 30, "ac", "S(V1 หรือ V2) + R(V5 หรือ V6) = 42 mm > 35 → LVH", "b", fs=12)]
    return fig("LVH — กล้ามเนื้อหนาขึ้น ไฟฟ้ามากขึ้น (Sokolow–Lyon ในสไลด์)",
               "LV หนา → มวลที่ depolarize มากขึ้นและผนังใกล้ chest wall → **R ใน lead ซ้าย (V5–V6) สูง และ S ใน lead ขวา (V1–V2) ลึก** · "
               "เกณฑ์สไลด์: **S V1/V2 + R V5/V6 > 35 mm** · ผนังหนามากจนเลือดเลี้ยง subendocardium ไม่พอ → **strain pattern** (ST กดลาดลง + T กลับใน lead ซ้าย) · "
               "RVH: right axis + R > S ใน V1 + S ลึกค้างใน V5–V6",
               svg(420, 246, "ECG lead V1 ที่ S ลึกและ V5 ที่ R สูงพร้อม strain pattern และผลรวม 42 มิลลิเมตร", *out))


# ───────────────────────────── 11. AV block
def av_strips():
    rows = [("1st degree · PR 0.28 s คงที่ ทุก P มี QRS", "ok", [beat(0.4 + 0.85 * i, pr=0.28) for i in range(5)]),
            ("Mobitz I · PR ยาวขึ้นเรื่อย ๆ แล้ว P หลุด", "ms",
             [beat(0.35, pr=0.16), beat(1.25, pr=0.24), beat(2.2, pr=0.32)] + [[_g(2.84, 0.13, 0.021)]] + [beat(3.46, pr=0.16)]),
            ("Mobitz II · PR คงที่ แล้ว P หลุดเฉย ๆ", "bad",
             [beat(0.35, pr=0.18), beat(1.15, pr=0.18)] + [[_g(1.79, 0.13, 0.021)]] + [beat(2.75, pr=0.18), beat(3.55, pr=0.18)]),
            ("3rd degree · P 90 กับ QRS 38 เดินแยกกัน", "bad",
             [[_g(0.12 + 0.667 * i, 0.13, 0.021)] for i in range(6)] + [beat(0.55 + 1.58 * i, kind="v", p=False) for i in range(3)])]
    out = []
    for i, (lab, c, parts) in enumerate(rows):
        y = 6 + i * 104
        comps = [x for p_ in parts for x in p_]
        s, X, yb = strip(10, y + 16, 4.0, comps, h_mm=16)
        out += [t(12, y + 11, lab, "xs b t" + c), s]
        if i == 1:
            for tt in (2.84,):
                out.append(t(X(tt), y + 16 + 16 * K + 12, "P หลุด", "xs mid tms b"))
        if i == 2:
            out.append(t(X(1.79), y + 16 + 16 * K + 12, "P หลุด", "xs mid tbad b"))
    return fig("AV block 4 แบบบน ECG (lead II)",
               "**1st**: PR > 0.20 s ทุกตัว ไม่มี P หลุด · **Mobitz I (Wenckebach)**: PR ยาวขึ้นทีละน้อยจน P ไม่ลง — PR ยาวสุดก่อนหลุด สั้นสุดหลังหลุด · "
               "**Mobitz II**: PR คงที่ (ปกติหรือยาวก็ได้) แล้ว P หลุดโดยไม่มีสัญญาณเตือน มักคู่กับ QRS กว้าง · "
               "**3rd (complete)**: P กับ QRS ไม่สัมพันธ์กันเลย (AV dissociation) QRS มาจาก escape ด้านล่าง",
               svg(420, 6 + 4 * 104 - 10, "แถบ ECG first degree AV block Mobitz I Mobitz II และ complete heart block", *out))


def block_level():
    out = [box(62, 10, 146, 34, "ms", "ที่ AV node", "b"), box(214, 10, 196, 34, "bad", "ใต้ AV node (His–Purkinje)", "b", fs=12)]
    rows = [("ตัวอย่าง", "1st · Mobitz I\nCHB ใน inferior MI", "Mobitz II\nCHB ใน anterior MI / พังผืด"),
            ("กลไก", "เซลล์ AV node ล้าทีละน้อย\n(decremental)", "His–Purkinje ส่งได้หรือไม่ได้เลย\n(all-or-none)"),
            ("สาเหตุ", "vagal สูง · ยา β-blocker\nCCB digoxin · ischemia", "โครงสร้างเสีย: infarct\nfibrosis necrosis"),
            ("escape", "junctional 40–60\nQRS แคบ", "ventricular 20–40\nQRS กว้าง"),
            ("atropine", "ได้ผล\n(ลด vagal ที่ AV node)", "มักไม่ได้ผล"),
            ("รักษา", "สังเกต / ตัดยา\n(conservative)", "pacemaker (ลายมือในสไลด์)")]
    for i, (h, a, b) in enumerate(rows):
        y = 54 + i * 48
        out += [t(4, y + 25, h, "xs b mu"), box(62, y, 146, 42, "bx", a, "", fs=10.5), box(214, y, 196, 42, "bx", b, "", fs=10.5)]
    return fig("Block ที่ AV node เทียบกับใต้ AV node — ทำไมพยากรณ์ต่างกัน",
               "สไลด์: Mobitz I มักเป็น block **ที่ AV node** จากเซลล์ \"ล้า\" ทีละน้อยแบบกลับคืนได้ · Mobitz II มักเป็น **His–Purkinje** ที่ล้มเหลวทันทีจาก **โครงสร้างเสียหาย** · "
               "complete block จาก AV node (เช่น vagal สูงช่วง **inferior MI**) **ตอบ atropine และพยากรณ์ดีกว่า**",
               svg(420, 54 + 6 * 48, "ตารางเทียบ block ที่ AV node กับ block ที่ His Purkinje ด้านกลไก สาเหตุ escape การตอบสนองต่อ atropine และการรักษา", *out))


# ───────────────────────────── 12. BBB
def bbb():
    out = []
    rows = [("RBBB", "rbbb_v1", "rbbb_v6", "M ใน V1 (rsR')", "S กว้างใน V6", "ac"),
            ("LBBB", "lbbb_v1", "lbbb_v6", "W/QS ลึกใน V1", "R กว้างหยัก (M) ใน V6", "ms")]
    for i, (nm, k1, k6, d1, d6, c) in enumerate(rows):
        y = 8 + i * 140
        s1, X1, yb1 = strip(70, y + 14, 0.64, beat(0.28, kind=k1, pr=0.15), h_mm=26, k=3.6, base_at=0.55, label="V1")
        s6, X6, yb6 = strip(250, y + 14, 0.64, beat(0.28, kind=k6, pr=0.15), h_mm=26, k=3.6, base_at=0.62, label="V6")
        out += [box(4, y + 40, 58, 44, c, nm, "b"), s1, s6,
                t(70 + 29 * 1.8, y + 14 + 26 * 3.6 + 14, d1, "xs mid b t" + c), t(250 + 29 * 1.8, y + 14 + 26 * 3.6 + 14, d6, "xs mid b t" + c)]
    out.append(t(210, 294, "จำ WiLLiaM MaRRoW: W-M = LBBB · M-W = RBBB (ลายมือในสไลด์)", "xs b mid"))
    return fig("Bundle branch block — QRS กว้าง ≥ 0.12 s และรูปร่างใน V1/V6",
               "ทางด่วนข้างหนึ่งขาด → ventricle ข้างนั้นต้องรับไฟฟ้าแบบ **เซลล์ต่อเซลล์ผ่านกล้ามเนื้อ (ช้า)** หลังข้างที่ดี → QRS กว้าง · "
               "**RBBB**: RV depolarize ทีหลัง → แรงไฟฟ้าช่วงท้ายชี้ไปขวาหน้า = R' ใน V1 และ S กว้างใน V6 · พบในคนปกติได้ · "
               "**LBBB**: septum depolarize กลับทิศ + LV ทีหลัง → ไฟฟ้าทั้งก้อนชี้ไปซ้ายหลัง = QS ลึกใน V1 R กว้างหยักใน V6 · LBBB ใหม่ร่วมเจ็บหน้าอก = ถือเป็นภาวะเสี่ยงสูง",
               svg(420, 304, "QRS ใน V1 และ V6 ของ RBBB และ LBBB พร้อมคำจำ WiLLiaM MaRRoW", *out))


# ───────────────────────────── 13. pericarditis / electrolytes
def peri_vs_stemi():
    s1, X1, yb1 = strip(10, 30, 0.72, beat(0.32, pr=0.16, st=0.16, t_amp=0.3, pr_dep=0.09), h_mm=26, k=3.8, base_at=0.62)
    s2, X2, yb2 = strip(222, 30, 0.72, beat(0.32, pr=0.16, st=0.34, t_amp=0.35), h_mm=26, k=3.8, base_at=0.62)
    out = [s1, s2, t(78, 22, "Pericarditis", "sm b mid tac"), t(290, 22, "STEMI", "sm b mid tbad"),
           t(X1(0.2), yb1 + 22, "PR กดลง", "xs mid b tac"), ar(X1(0.2), yb1 + 12, X1(0.24), yb1 + 3, "lac", "ah-ac")]
    rows = [("ST ยก", "ทั่วทุก lead · เว้าหงาย", "เฉพาะผนัง · โค้งคว่ำ"), ("reciprocal", "ไม่มี (ยกเว้น aVR)", "มี ฝั่งตรงข้าม"),
            ("PR", "กดลง (aVR ยกขึ้น)", "ปกติ"), ("Q wave", "ไม่เกิด", "เกิดตามมา")]
    for i, (a, b, c) in enumerate(rows):
        y = 168 + i * 24
        out += [t(10, y, a, "xs b"), t(96, y, b, "xs tac"), t(270, y, c, "xs tbad")]
    return fig("Pericarditis เทียบ STEMI (ลายมือในสไลด์: PR depress)",
               "เยื่อหุ้มหัวใจอักเสบระคายผิว epicardium **ทั่วทั้งหัวใจ** → ST ยกทุก lead ไม่จำกัดผนัง ไม่มี reciprocal · "
               "อักเสบลามผิว atrium → atrial repolarization ผิดปกติ → **PR segment กดลง** (และยกใน aVR) — ข้อนี้ออกสอบบ่อย",
               svg(420, 262, "ECG pericarditis ที่ ST ยกเว้าและ PR กดลง เทียบกับ STEMI ที่ ST ยกโค้ง พร้อมตารางแยก", *out))


def potassium():
    stages = [("K ปกติ", dict(), None), ("~6–7: T สูงแหลม", dict(peaked=True), None),
              ("~7–8: P แบน PR ยาว QRS กว้าง", dict(kind="wide_k", p_amp=0.05, pr=0.24, peaked=True), None),
              ("> 8: sine wave → VF", dict(), "sine")]
    out = []
    for i, (lab, kw, base) in enumerate(stages):
        x = 6 + (i % 2) * 208; y = 8 + (i // 2) * 128
        if base:
            s, X, yb = strip(x, y + 16, 1.0, [], base, h_mm=24, k=4, base_at=0.5)
        else:
            s, X, yb = strip(x, y + 16, 1.0, beat(0.42, **kw), h_mm=24, k=4, base_at=0.62)
        out += [t(x + 2, y + 10, lab, "xs b " + ("tok" if i == 0 else "tbad")), s]
    s, X, yb = strip(6, 270, 1.0, beat(0.32, t_amp=0.08, st=-0.09, u=0.16), h_mm=20, k=4, base_at=0.6)
    out += [t(8, 264, "HypoK: T แบน ST กด U ชัด", "xs b tms"), s, t(X(0.82), 300, "U", "xs b tms mid")]
    out += [box(214, 268, 202, 82, "ok", None), t(315, 288, "HyperK + ECG เปลี่ยน", "xs b mid tok"),
            t(315, 306, "1 Ca gluconate IV ทันที", "xs mid"), t(315, 322, "(ทำให้เยื่อหุ้มเซลล์เสถียร)", "xs mid i2"),
            t(315, 340, "2 insulin+glucose · 3 ขับ K", "xs mid")]
    return fig("Potassium กับ ECG (สไลด์ HyperK / HypoK)",
               "K สูง → potassium channel เปิดมากขึ้น → **repolarization เร็ว = T สูงแหลมฐานแคบ** · K สูงมาก → resting potential บวกขึ้น Na channel ถูก inactivate "
               "→ **การนำไฟฟ้าช้า: P แบน PR ยาว QRS กว้าง** จนรวมกับ T เป็น sine wave → VF/asystole · K ต่ำ → repolarize ช้า: **T แบน ST กด U wave ชัด QT(U) ยาว**",
               svg(420, 358, "ECG ระยะ hyperkalemia ตั้งแต่ T สูงแหลม QRS กว้าง ถึง sine wave และ hypokalemia ที่มี U wave", *out))


# ───────────────────────────── 14. รวม
def read_flow():
    steps = [("1 Rate", "300/ช่องใหญ่ · 1500/ช่องเล็ก · 6 วิ × 10"), ("2 Rhythm", "มี P ไหม · P–QRS สัมพันธ์ไหม · RR สม่ำเสมอไหม"),
             ("3 Axis", "lead I + aVF"), ("(ช่วงเวลา)", "PR · QRS · QTc"), ("4 Infarction", "ST/T/Q · lead ไหน · reciprocal"),
             ("5 Hypertrophy", "P (RA/LA) · voltage (LVH/RVH)"), ("สรุป Dx", "ใส่ rhythm + สิ่งผิดปกติ")]
    out = []
    for i, (a, b) in enumerate(steps):
        y = 8 + i * 44
        c = "ac" if a[0].isdigit() else ("ok" if a.startswith("สรุป") else "sk")
        out += [box(8, y, 118, 36, c, a, "b", fs=12), t(138, y + 23, b, "xs i2")]
        if i < len(steps) - 1:
            out.append(ar(67, y + 36, 67, y + 44, "lmu", "ah-mu"))
    return fig("อ่าน ECG 5 ขั้นของอาจารย์ (Rate · Rhythm · Axis · Infarction · Hypertrophy)",
               "ทำครบทุกขั้นทุกครั้งแม้เจอความผิดปกติแรกแล้ว · ตัวอย่างในสไลด์ (p78): \"NSR · rate 13 × 6 = 78 · normal axis · no infarction · no chamber enlargement · "
               "seen bigeminy PVCs → **Dx: NSR with bigeminy PVCs**\" · ในข้อสอบ SAQ ให้เขียนตามลำดับนี้",
               svg(420, 8 + 7 * 44 - 4, "ขั้นตอนอ่าน ECG rate rhythm axis ช่วงเวลา infarction hypertrophy และสรุป", *out))


def bigeminy():
    comps = []
    for i in range(3):
        comps += beat(0.3 + 1.3 * i, pr=0.16) + beat(0.3 + 1.3 * i + 0.56, kind="v", p=False)
    s, X, yb = strip(10, 24, 4.0, comps, h_mm=20)
    out = [s, t(X(0.3), 20, "N", "xs b mid tok"), t(X(0.86), 20, "V", "xs b mid tbad"), t(X(1.6), 20, "N", "xs b mid tok"),
           t(X(2.16), 20, "V", "xs b mid tbad"), t(10, 24 + 80 + 18, "Dx: NSR with ventricular bigeminy (ตัวอย่างสไลด์ p78)", "xs b")]
    return fig("Ventricular bigeminy — PVC สลับทุกจังหวะ",
               "N = sinus beat (มี P QRS แคบ) · V = PVC (QRS กว้าง ไม่มี P T สวนทาง) · นับ rate ให้นับทุก QRS · "
               "ชีพจรที่ข้อมืออาจได้ครึ่งเดียวเพราะ PVC มาเร็วจน ventricle ยังไม่เต็ม (stroke volume ต่ำ)",
               svg(420, 24 + 80 + 28, "แถบ ECG sinus สลับ PVC ทุกจังหวะ ventricular bigeminy", *out))
