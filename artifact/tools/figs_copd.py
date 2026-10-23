# -*- coding: utf-8 -*-
"""ภาพประกอบคาบ chest 37 COPD (GOLD 2026) — ใช้ใน build_copd.py
ทุกฟังก์ชันคืน fig(title, cap, svg) · กว้าง ≤ 420 · ใช้คลาสสีจาก svg.py เท่านั้น"""
import math
from svg import *


def _curve(pts, c, X, Y):
    return poly([(X(a), Y(b)) for a, b in pts], c)


# ───────────────────────────── 1. lung function trajectory
def trajectory():
    X = lambda a: 46 + a * 3.675
    Y = lambda v: 222 - v * 1.8
    out = [line(46, 222, 340, 222, "ln"), line(46, 222, 46, 30, "ln"),
           t(193, 252, "อายุ (ปี)", "sm mid i2"), t(8, 14, "FEV1 (% ของค่าสูงสุด)", "xs i2")]
    for a in (0, 20, 40, 60, 80):
        out += [line(X(a), 222, X(a), 227, "ln"), t(X(a), 238, str(a), "xs mid mu")]
    out += [line(46, Y(55), 340, Y(55), "lbad da"), t(196, Y(55) + 14, "ระดับที่เริ่มมีอาการ (COPD)", "xs mid tbad")]
    norm = [(0, 20), (10, 55), (20, 95), (25, 100), (35, 100), (50, 92), (65, 84), (80, 76)]
    low = [(0, 15), (10, 42), (20, 72), (25, 75), (35, 75), (50, 67), (65, 59), (80, 51)]
    acc = [(25, 100), (35, 98), (45, 85), (55, 70), (65, 55), (80, 36)]
    out += [_curve(norm, "lok w3", X, Y), _curve(low, "lms w3", X, Y), _curve(acc, "lbad w3", X, Y),
            t(X(80) + 4, Y(76) + 4, "ปกติ", "sm b tok"),
            t(X(80) + 4, Y(51) + 6, "โตไม่เต็มที่", "sm b tms"),
            t(X(80) + 4, Y(36) + 4, "ลดเร็ว", "sm b tbad"),
            t(X(22), Y(100) - 8, "สูงสุดอายุ 20–25 ปี", "xs mid i2"),
            t(96, 176, "เส้นเหลือง: คลอดก่อนกำหนด · ติดเชื้อรุนแรงวัยเด็ก ·", "xs tms"),
            t(96, 190, "แม่สูบบุหรี่ขณะตั้งครรภ์ · หอบหืดในเด็ก", "xs tms"),
            t(232, 30, "เส้นแดง: บุหรี่ · ควันชีวมวล", "xs tbad"),
            t(232, 42, "· PM2.5 · ฝุ่น/สารเคมีจากอาชีพ", "xs tbad")]
    return fig("เส้นทางสมรรถภาพปอดตลอดชีวิต — COPD เกิดได้ 2 ทาง",
               "ปอดโตเต็มที่ราวอายุ **20–25 ปี** แล้วค่อย ๆ ลดตามวัย · ผู้ป่วย COPD ราวครึ่งหนึ่ง **สมรรถภาพปอดลดเร็วกว่าปกติ** (เส้นแดง: สูบบุหรี่ ควันชีวมวล มลพิษ) "
               "อีกครึ่งหนึ่ง **ปอดโตไม่เต็มที่ตั้งแต่วัยเด็ก** (เส้นเหลือง) แม้ลดในอัตราปกติก็แตะระดับที่มีอาการได้ — GOLD 2026 จึงเรียกสาเหตุรวมว่า **GETomics** (ยีน × สิ่งแวดล้อม × ช่วงเวลาของชีวิต)",
               svg(420, 258, "กราฟ FEV1 ตามอายุ 3 เส้น ปกติ โตไม่เต็มที่ และลดเร็ว เทียบกับระดับที่เริ่มมีอาการ", *out))


# ───────────────────────────── 2. alveolar attachments
def tethering():
    out = [t(105, 20, "ปอดปกติ", "b mid tok"), t(315, 20, "Emphysema", "b mid tbad")]
    cx, cy = 105, 108
    for k in range(8):
        a = math.radians(k * 45 + 22.5)
        ax, ay = cx + 56 * math.cos(a), cy + 56 * math.sin(a)
        out += [circ(ax, ay, 17, "sk"),
                line(cx + 19 * math.cos(a), cy + 19 * math.sin(a), cx + 39 * math.cos(a), cy + 39 * math.sin(a), "lok w2")]
    out += [circ(cx, cy, 19, "ac"), circ(cx, cy, 12, "bx")]
    cx = 315
    for k, a0 in enumerate((30, 150, 270)):
        a = math.radians(a0)
        out.append(circ(cx + 58 * math.cos(a), cy + 58 * math.sin(a), 33, "sk"))
    for a0 in (90, 210, 330):
        a = math.radians(a0)
        out.append(line(cx + 14 * math.cos(a), cy + 10 * math.sin(a), cx + 26 * math.cos(a), cy + 22 * math.sin(a), "lbad da"))
    out += [ell(cx, cy, 18, 8, "ac"), ell(cx, cy, 11, 2.5, "bx"),
            t(105, 186, "ผนังถุงลม = เส้นยึดดึงหลอดลม", "xs mid"),
            t(105, 200, "เล็กให้เปิดตอนหายใจออก", "xs mid"),
            t(315, 186, "ผนังถุงลมถูกย่อย → ถุงลมรวมเป็นโพรง", "xs mid"),
            t(315, 200, "ไม่มีแรงดึง → หลอดลมแฟบตอนหายใจออก", "xs mid tbad"),
            box(10, 214, 400, 40, "ms", None),
            t(210, 230, "elastic recoil ↓ + แรงต้านทานใน small airway ↑ (อักเสบ เสมหะ พังผืด)", "xs mid b"),
            t(210, 246, "→ ลมออกช้า (FEV1 ↓) → ลมค้าง (air trapping) → ปอดพอง (hyperinflation)", "xs mid")]
    return fig("ทำไมลมออกไม่หมด — alveolar attachments",
               "หลอดลมเล็ก (< 2 mm) ไม่มีกระดูกอ่อน อยู่ได้เพราะ **ผนังถุงลมรอบ ๆ ยึดดึงเป็นรัศมี** · ใน emphysema โปรตีเอส (neutrophil elastase, MMP) "
               "ย่อย elastin จนผนังถุงลมหาย **แรงดึงหายไปพร้อม elastic recoil** หลอดลมจึงแฟบก่อนลมออกหมด · ร่วมกับ small airway disease (ผนังหนา เสมหะอุด) "
               "เป็นที่มาของ airflow obstruction ที่ไม่กลับคืนเต็มที่",
               svg(420, 262, "เทียบหลอดลมเล็กที่มีผนังถุงลมยึดดึงในปอดปกติ กับหลอดลมที่แฟบใน emphysema", *out))


# ───────────────────────────── 3. dynamic hyperinflation
def dyn_hyper():
    out = [line(40, 40, 410, 40, "lbad da"), t(44, 34, "TLC (เพดานปอด)", "xs tbad"),
           line(40, 222, 410, 222, "lmu da"), t(44, 236, "RV ของคนปกติ", "xs mu"),
           line(176, 46, 176, 226, "lru da"),
           t(104, 64, "พัก", "sm b mid"), t(294, 64, "ออกกำลัง (หายใจเร็ว)", "sm b mid tms")]
    pts = []
    for i in range(0, 131):
        x = 40 + i
        pts.append((x, 175 - 25 * (1 - math.cos(2 * math.pi * i / 43)) * 1.0))
    out.append(poly(pts, "lac w2"))
    lows = [175, 160, 147, 136, 128, 122]
    pts = []
    x0 = 180
    for b, lo in enumerate(lows[:5]):
        hi_ = lo - 70
        nxt = lows[b + 1]
        # หายใจเข้าเร็ว (ขึ้น) แล้วหายใจออกไม่ทันจบ (ลงไม่ถึงจุดเดิม)
        for j in range(0, 16):
            pts.append((x0 + j, lo - (lo - hi_) * math.sin(math.pi / 2 * j / 15)))
        for j in range(1, 30):
            pts.append((x0 + 15 + j, hi_ + (nxt - hi_) * (1 - math.cos(math.pi / 2 * j / 29))))
        x0 += 43
    out.append(poly(pts, "lms w2"))
    out += [poly([(40, 175), (176, 175)], "lok dt w2"), poly([(180, 175), (223, 160), (266, 147), (309, 136), (352, 128), (395, 122)], "lbad dt w2"),
            t(120, 190, "EELV ที่พัก", "xs mid tok"), t(318, 168, "EELV สูงขึ้นทุกครั้ง", "xs mid tbad"),
            line(156, 172, 156, 44, "ln", "ah"), line(156, 44, 156, 172, "ln", "ah"),
            t(150, 112, "IC", "xs end b"), t(150, 124, "กว้าง", "xs end"),
            line(406, 119, 406, 44, "lbad", "ah-bad"), t(410, 28, "IC แคบลง", "xs end b tbad")]
    return fig("Dynamic hyperinflation — ทำไมเหนื่อยเมื่อออกแรง",
               "COPD ต้องใช้เวลาหายใจออกนาน (ลมออกช้า) · ตอนออกแรงหายใจเร็วขึ้น **เวลาหายใจออกสั้นลง** ลมจึงออกไม่หมดก่อนหายใจเข้าครั้งถัดไป "
               "ปริมาตรปอดท้ายหายใจออก (**EELV**) ขยับขึ้นทีละจังหวะ (breath stacking) · inspiratory capacity (**IC**) แคบลง ปริมาตรหายใจเข้าชนเพดาน TLC "
               "กล้ามเนื้อหายใจทำงานในช่วงที่ปอดแข็งและเสียเปรียบเชิงกล = **เหนื่อยแบบหายใจเข้าไม่อิ่ม** · ยาขยายหลอดลมช่วยเพราะลด hyperinflation มากกว่าเพิ่ม FEV1",
               svg(420, 246, "กราฟปริมาตรปอดตามเวลา ตอนพักและตอนออกกำลัง แสดง EELV สูงขึ้นและ IC แคบลง", *out))


# ───────────────────────────── 4. hypoxemia → cor pulmonale
def cor_chain():
    out = [box(10, 8, 196, 46, "wa", "ถุงลมระบายอากาศไม่ดี\n(low V/Q)", "b", fs=12),
           box(214, 8, 196, 46, "sk", "ผนังถุงลม + capillary\nถูกทำลาย (emphysema)", "b", fs=12),
           ar(108, 54, 108, 76, "ln", "ah"), ar(312, 54, 312, 76, "ln", "ah"),
           box(10, 76, 196, 46, "bx", "PAO2 ต่ำ → หลอดเลือด\nหดตัว (HPV)", fs=12),
           box(214, 76, 196, 46, "bx", "พื้นที่หลอดเลือดปอด\nลดลง", fs=12),
           ar(108, 122, 190, 146, "ln", "ah"), ar(312, 122, 230, 146, "ln", "ah"),
           box(110, 146, 200, 38, "ms", "Pulmonary hypertension", "b", fs=13),
           ar(210, 184, 210, 204, "ln", "ah"),
           box(110, 204, 200, 38, "bad", "RV หนา → RV ล้ม = cor pulmonale", "b", fs=11.5),
           ar(210, 242, 210, 262, "lbad", "ah-bad"),
           box(60, 262, 300, 34, "bx", "JVP สูง · ขาบวม · ตับโต · P2 ดัง · RV heave", fs=11.5),
           box(10, 146, 92, 96, "sk", None), t(56, 164, "hypoxemia", "xs mid b"), t(56, 178, "เรื้อรัง", "xs mid b"),
           t(56, 196, "→ EPO ↑", "xs mid"), t(56, 210, "→ Hct > 55%", "xs mid tbad"), t(56, 226, "→ เลือดหนืด", "xs mid"),
           ar(102, 194, 110, 172, "lbad", "ah-bad"),
           box(318, 146, 92, 96, "ok", None), t(364, 166, "LTOT", "sm mid b tok"), t(364, 184, "แก้ HPV", "xs mid"),
           t(364, 198, "ลด Hct", "xs mid"), t(364, 212, "ชะลอ PH", "xs mid"), t(364, 228, "= อยู่รอดนานขึ้น", "xs mid tok"),
           ar(318, 166, 310, 166, "lok", "ah-ok")]
    return fig("จาก hypoxemia สู่ cor pulmonale",
               "ถุงลมที่ระบายอากาศไม่ดีทำให้ PAO2 ต่ำ หลอดเลือดแดงเล็กรอบถุงลมนั้น **หดตัว (hypoxic pulmonary vasoconstriction)** เพื่อส่งเลือดไปถุงลมที่ดี — ดีในระยะสั้น "
               "แต่ถ้าเกิดทั่วปอดเรื้อรังจะเกิด **pulmonary hypertension** ร่วมกับการสูญเสีย capillary bed · RV ต้องบีบต้านแรงดันสูง → หนาตัว → ล้ม (**cor pulmonale**) · "
               "hypoxemia เรื้อรังกระตุ้น EPO จน **secondary polycythemia** เลือดหนืดยิ่งเพิ่มแรงต้าน · **LTOT ตัดวงจรนี้ จึงเป็นการรักษาที่ยืดชีวิตได้**",
               svg(420, 302, "แผนผังลำดับจาก low V/Q และ emphysema ไปสู่ pulmonary hypertension และ cor pulmonale พร้อมจุดที่ LTOT ช่วย", *out))


# ───────────────────────────── 5. pursed-lip breathing / equal pressure point
def pursed_lip():
    def row(y0, title, vals, epp_x, coll_from, coll_to, tc):
        o = [t(10, y0 - 24, title, "sm b " + tc),
             rect(70, y0 - 2, 290, 52, "sk", 6), t(215, y0 + 62, "แรงดันในช่องอก (pleural) +10", "xs mid mu"),
             circ(46, y0 + 24, 22, "wa"), t(46, y0 + 20, "ถุงลม", "xs mid"), t(46, y0 + 32, "+15", "xs mid b")]
        o.append(path("M68 %s L%s %s L%s %s L%s %s L388 %s" % (y0 + 14, coll_from, y0 + 14, coll_from + 10, y0 + 20, coll_to, y0 + 20, y0 + 14), "ln w2"))
        o.append(path("M68 %s L%s %s L%s %s L%s %s L388 %s" % (y0 + 34, coll_from, y0 + 34, coll_from + 10, y0 + 28, coll_to, y0 + 28, y0 + 34), "ln w2"))
        for x, v in vals:
            o.append(t(x, y0 + 10, v, "xs mid i2"))
        o += [line(epp_x, y0 + 4, epp_x, y0 + 44, "lbad da"), t(epp_x, y0 - 6, "EPP", "xs mid b tbad")]
        return o
    out = row(40, "หายใจออกปกติ — จุดแฟบอยู่ใน small airway (ไม่มีกระดูกอ่อน)",
              [(100, "+14"), (140, "+12"), (232, "+5"), (300, "+3"), (382, "0")], 165, 172, 280, "tbad")
    out += row(150, "เป่าปาก (pursed-lip) — แรงดันย้อนกลับ ดัน EPP ไปทางปาก",
               [(100, "+14"), (150, "+13"), (220, "+12"), (290, "+11"), (382, "+6")], 330, 336, 360, "tok")
    out += [t(392, 204, "ปาก", "xs mu"), t(392, 94, "ปาก", "xs mu"),
            box(10, 224, 400, 40, "ok", None),
            t(210, 240, "ผลเพิ่ม: หายใจช้าลง → เวลาหายใจออกยาว → ลมค้างน้อยลง", "xs mid b"),
            t(210, 256, "ผู้ป่วยทำเองโดยสัญชาตญาณ = ตรวจร่างกายพบ pursed-lip breathing", "xs mid")]
    return fig("Pursed-lip breathing — ทำไมผู้ป่วยเป่าปากหายใจออก",
               "ตอนหายใจออก แรงดันในหลอดลมลดลงจากถุงลมไปปาก จุดที่แรงดันในหลอดลมเท่ากับแรงดันในช่องอกเรียก **equal pressure point (EPP)** ถัดจากจุดนี้หลอดลมถูกบีบ · "
               "ใน emphysema elastic recoil ต่ำ แรงดันเริ่มต้นต่ำ EPP จึงเลื่อนลึกไปอยู่ใน **small airway ที่ไม่มีกระดูกอ่อน → แฟบ ลมค้าง** · "
               "การเป่าปากเพิ่มแรงต้านที่ปาก แรงดันทั้งเส้นทางสูงขึ้น EPP เลื่อนไปอยู่ในหลอดลมใหญ่ที่มีกระดูกอ่อนค้ำ หลอดลมเล็กจึงเปิดค้างได้ (หลักเดียวกับ PEEP) · ตัวเลขในภาพเป็นค่าสมมติเพื่ออธิบายหลักการ",
               svg(420, 270, "เทียบตำแหน่ง equal pressure point ขณะหายใจออกปกติและขณะเป่าปากใน emphysema", *out))


# ───────────────────────────── 6. diaphragm / barrel chest
def diaphragm():
    out = [t(105, 18, "ปกติ", "b mid tok"), t(315, 18, "ปอดพอง (hyperinflation)", "b mid tbad")]
    # normal chest
    out += [path("M40 40 Q105 22 170 40 L178 170 L32 170 Z", "bx"),
            path("M40 168 Q70 96 105 100 Q140 96 170 168", "lac w3"),
            line(36, 150, 46, 150, "lok w2"), line(164, 150, 174, 150, "lok w2"),
            t(105, 130, "โดมสูง", "xs mid tac"), t(105, 144, "ใยกล้ามเนื้อยาว", "xs mid tac"),
            t(105, 188, "AP : lateral ≈ 1 : 2", "xs mid"),
            t(105, 204, "หดตัว → กดอวัยวะช่องท้องลง", "xs mid"),
            t(105, 218, "+ ขยายซี่โครงล่างออก (zone of apposition)", "xs mid")]
    # barrel chest
    out += [path("M248 34 Q315 14 382 34 L392 172 L238 172 Z", "bx"),
            path("M242 166 Q275 150 315 150 Q355 150 388 166", "lbad w3"),
            ar(250, 158, 266, 150, "lbad", "ah-bad"), ar(380, 158, 364, 150, "lbad", "ah-bad"),
            t(315, 136, "กะบังลมแบนราบ", "xs mid tbad"), t(315, 92, "ปอดพอง", "sm mid b"),
            t(315, 106, "ทรวงอกถังเบียร์", "xs mid"),
            t(315, 188, "AP : lateral → 1 : 1", "xs mid tbad"),
            t(315, 204, "ใยกล้ามเนื้อสั้น แรงหดตัวลด", "xs mid"),
            t(315, 218, "หดตัวแล้วดึงซี่โครงล่างเข้า (Hoover sign)", "xs mid tbad")]
    return fig("กะบังลมแบน — barrel chest, Hoover sign และความเหนื่อย",
               "ปอดพองดันกะบังลมลงจนแบน · ใยกล้ามเนื้อสั้นลง จึงอยู่นอกช่วงความยาวที่ออกแรงได้ดีที่สุด (length–tension) แรงหดตัวต่อสัญญาณประสาทลดลง · "
               "ทรวงอกขยายค้างในท่าหายใจเข้า (**barrel chest**, AP diameter เพิ่ม) · กะบังลมแบนเมื่อหดตัวจึง **ดึงขอบซี่โครงล่างเข้าแทนการดันออก (Hoover sign)** · "
               "ผู้ป่วยต้องใช้กล้ามเนื้อช่วยหายใจ (sternocleidomastoid, scalene) และนั่งโน้มตัวเท้าแขน (tripod) เพื่อให้กล้ามเนื้อเหล่านี้ยึดจุดได้",
               svg(420, 226, "เทียบรูปทรงทรวงอกและกะบังลมของคนปกติกับผู้ป่วยปอดพอง", *out))


# ───────────────────────────── 7. spirometry volume-time
def spiro_vt():
    X = lambda s: 50 + s * 55
    Y = lambda v: 218 - v * 34
    out = [line(50, 218, 395, 218, "ln"), line(50, 218, 50, 30, "ln"),
           t(222, 252, "เวลา (วินาที)", "sm mid i2"), t(12, 120, "ลิตร", "sm i2")]
    for s in range(0, 7):
        out += [line(X(s), 218, X(s), 223, "ln"), t(X(s), 234, str(s), "xs mid mu")]
    for v in range(1, 6):
        out += [line(45, Y(v), 50, Y(v), "ln"), t(41, Y(v) + 4, str(v), "xs end mu")]
    n = [(s / 10, 5 * (1 - math.exp(-(s / 10) / 0.62))) for s in range(0, 61)]
    c = [(s / 10, 3.4 * (1 - math.exp(-(s / 10) / 1.6))) for s in range(0, 61)]
    out += [_curve(n, "lok w3", X, Y), _curve(c, "lbad w3", X, Y),
            line(X(1), 218, X(1), 40, "lmu da"), t(X(1) + 4, 46, "1 วินาที", "xs mu"),
            circ(X(1), Y(4.0), 4, "okf"), circ(X(1), Y(1.58), 4, "badf"),
            t(X(1) + 8, Y(4.0) + 16, "FEV1 4.0", "xs b tok"), t(X(1) + 8, Y(1.58) + 16, "FEV1 1.6", "xs b tbad"),
            t(X(6), Y(4.98) - 8, "FVC 5.0", "xs end b tok"), t(X(6), Y(3.32) - 8, "FVC 3.4", "xs end b tbad"),
            box(222, 120, 176, 54, "sk", None),
            t(230, 138, "ปกติ 4.0/5.0 = 0.80", "xs b tok"),
            t(230, 154, "COPD 1.6/3.4 = 0.47 (< 0.7)", "xs b tbad"),
            t(230, 168, "FEV1 ลดมากกว่า FVC", "xs i2")]
    return fig("Spirometry แบบ volume–time — ปกติ vs COPD",
               "ผู้ป่วยสูดลมเต็มที่แล้วเป่าออกแรงและเร็วที่สุดจนหมด · **FEV1** = ปริมาตรที่เป่าออกในวินาทีแรก · **FVC** = ปริมาตรทั้งหมด · "
               "COPD ลมออกช้าเพราะแรงต้านสูงและ recoil ต่ำ **FEV1 ลดมาก** ส่วน FVC ลดน้อยกว่า (ลมค้างทำให้ FVC ลดบ้าง) อัตราส่วนจึงต่ำ · "
               "เส้นของ COPD ยังไม่ราบที่ 6 วินาที — ต้องเป่าให้นานพอจึงได้ FVC จริง · วินิจฉัยด้วย **post-bronchodilator FEV1/FVC < 0.7**",
               svg(420, 258, "กราฟปริมาตรตามเวลาของ spirometry คนปกติเทียบกับ COPD พร้อมค่า FEV1 FVC", *out))


# ───────────────────────────── 8. flow-volume loop
def flow_vol():
    X = lambda v: 50 + v * 64
    Y = lambda f: 150 - f * 12
    out = [line(50, 150, 390, 150, "ln"), line(50, 40, 50, 212, "ln"),
           t(220, 248, "ปริมาตรที่เป่าออก (ลิตร) — เริ่มจาก TLC", "sm mid i2"),
           t(8, 24, "flow (L/s) — บน: หายใจออก · ล่าง: หายใจเข้า", "xs i2")]
    for v in range(0, 6):
        out += [line(X(v), 150, X(v), 155, "ln"), t(X(v) + 6, 164, str(v), "xs mid mu")]
    ne = [(0, 0), (0.12, 5), (0.5, 8), (5, 0)]
    out += [_curve(ne, "lok w3", X, Y),
            path("M%s %s Q%s %s %s %s" % (X(5), Y(0), X(2.5), Y(-9), X(0), Y(0)), "lok w2"),
            _curve([(0, 0), (0.08, 2.8), (0.3, 4.2), (0.65, 2.5), (1.1, 1.5), (1.8, 0.8), (2.6, 0.35), (3.4, 0)], "lbad w3", X, Y),
            path("M%s %s Q%s %s %s %s" % (X(3.4), Y(0), X(1.7), Y(-7), X(0), Y(0)), "lbad w2"),
            t(X(0.6), Y(8) - 6, "PEF ปกติ", "xs tok"), t(X(2.7), Y(4.6) - 14, "ลดลงเป็นเส้นตรง", "xs tok"),
            t(X(0.55), Y(4.2) - 6, "ยอดต่ำ", "xs tbad"), t(X(1.6), 112, "ส่วนท้ายเว้า (scooped)", "xs tbad"),
            t(X(1.6), 124, "= small airway แฟบ", "xs tbad"),
            t(X(5), Y(0) - 6, "FVC", "xs end tok"), t(X(3.4), Y(0) - 6, "FVC", "xs end tbad"),
            t(X(2.5), 230, "หายใจเข้าใกล้ปกติ (แรงดันลบดึงหลอดลมเปิด)", "xs mid i2")]
    return fig("Flow–volume loop — รูปเว้าของ obstruction",
               "ส่วนบนคือการหายใจออก ส่วนล่างคือการหายใจเข้า · คนปกติ flow พุ่งถึงยอด (PEF) แล้วลดลงเป็นเส้นค่อนข้างตรง · "
               "ใน COPD ยอดต่ำและ **ส่วนท้ายเว้าลง (scooped, concave)** เพราะเมื่อปริมาตรปอดลดลง recoil ยิ่งน้อยและ small airway แฟบ flow จึงตกเร็ว · "
               "การหายใจเข้าไม่ค่อยผิดปกติเพราะแรงดันลบในช่องอกตอนหายใจเข้าดึงหลอดลมให้เปิด",
               svg(420, 256, "flow volume loop ของคนปกติเทียบกับ COPD ที่มีส่วนท้ายเว้า", *out))


# ───────────────────────────── 9. ABE (GOLD 2026)
def abe():
    out = [t(70, 22, "ประวัติ exacerbation", "sm b mid"), t(70, 36, "ในปีที่ผ่านมา", "sm b mid"),
           t(275, 28, "อาการ (mMRC / CAT)", "sm b mid"),
           box(10, 50, 120, 70, "sk", "≥ 1 ครั้ง\nmoderate หรือ\nsevere (admit)", fs=11.5),
           box(140, 50, 270, 70, "bad", None), t(275, 80, "E", "lg b mid tbad", fs=26), t(275, 104, "ไม่ว่าอาการมากหรือน้อย", "xs mid"),
           box(10, 130, 120, 80, "sk", "0 ครั้ง", fs=12),
           box(140, 130, 130, 80, "ok", None), t(205, 166, "A", "b mid tok", fs=26), t(205, 192, "อาการน้อย", "xs mid"),
           box(280, 130, 130, 80, "ms", None), t(345, 166, "B", "b mid tms", fs=26), t(345, 192, "อาการมาก", "xs mid"),
           t(205, 228, "mMRC 0–1 · CAT < 10", "xs mid b"), t(345, 228, "mMRC ≥ 2 · CAT ≥ 10", "xs mid b"),
           box(10, 242, 400, 52, "ac", None),
           t(210, 260, "แยกเกรด spirometry: GOLD 1 ≥ 80 · 2 = 50–79 · 3 = 30–49 · 4 < 30", "xs mid b"),
           t(210, 276, "(post-BD FEV1 % predicted · ใช้บอกความรุนแรงการอุดกั้น ไม่ได้ใช้จัดกลุ่ม)", "xs mid"),
           t(210, 312, "GOLD 2026: เดิม E = ≥ 2 moderate หรือ ≥ 1 admit → ตอนนี้ 1 moderate ก็เป็น E", "xs mid tbad")]
    return fig("การจัดกลุ่ม ABE ตาม GOLD 2026",
               "ใช้กับผู้ป่วยที่ **ยังไม่เคยได้ยา maintenance** เพื่อเลือกยาเริ่มต้น · ขั้นแรกถามประวัติ exacerbation — **แค่ moderate (ต้องใช้ steroid และ/หรือ antibiotic) 1 ครั้ง หรือ admit 1 ครั้ง = กลุ่ม E** "
               "(GOLD 2026 ลดเกณฑ์จาก ≥ 2 ครั้ง เพราะข้อมูลใหม่พบว่าแม้ครั้งเดียวก็เพิ่มความเสี่ยงครั้งต่อไป) · ถ้าไม่มี exacerbation ใช้อาการแยก A กับ B · "
               "ตัวเลข mMRC/CAT ในภาพเป็นค่าตามรูป ABE ของ GOLD ฉบับก่อน (ข้อความ GOLD 2026 ยืนยัน CAT ≥ 10 และ mMRC ≥ 2)",
               svg(420, 320, "แผนภาพจัดกลุ่ม A B E ตามประวัติ exacerbation และอาการ พร้อมเกรด spirometry GOLD 1 ถึง 4", *out))


# ───────────────────────────── 10. asthma vs COPD
def asthma_copd():
    X = lambda d: 50 + d * 25
    Y = lambda v: 160 - v * 1.3
    out = [line(50, 160, 400, 160, "ln"), line(50, 160, 50, 28, "ln"),
           t(225, 178, "เวลา (สัปดาห์ – เดือน)", "xs mid i2"), t(14, 92, "FEV1", "xs i2"), t(14, 104, "%pred", "xs mu"),
           line(50, Y(80), 400, Y(80), "lmu da"), t(54, Y(80) + 12, "ปกติ", "xs mu")]
    a = [(0, 90), (2, 88), (3, 60), (4, 66), (5, 90), (7, 92), (8, 70), (9, 62), (10, 85), (12, 92), (14, 90)]
    c = [(0, 48), (2, 47), (3, 40), (4, 44), (5, 47), (7, 46), (8, 45), (10, 44), (12, 42), (14, 41)]
    out += [_curve(a, "lac w3", X, Y), _curve(c, "lbad w3", X, Y),
            t(X(3), Y(60) + 14, "หอบ", "xs mid tac"), t(X(5.5), Y(92) - 6, "ยา → กลับปกติ", "xs mid tac"),
            t(X(11), Y(41) + 16, "ต่ำค้าง ค่อย ๆ ลด", "xs mid tbad"),
            box(10, 190, 196, 98, "ac", None), t(108, 208, "Asthma", "sm b mid tac"),
            t(108, 226, "eosinophil · mast cell · Th2", "xs mid"), t(108, 242, "เริ่มวัยเด็ก มี atopy", "xs mid"),
            t(108, 258, "อาการขึ้นลง กลางคืน/เช้ามืด", "xs mid"), t(108, 274, "แปรปรวนมาก กลับปกติได้", "xs mid b"),
            box(214, 190, 196, 98, "bad", None), t(312, 208, "COPD", "sm b mid tbad"),
            t(312, 226, "neutrophil · macrophage · CD8", "xs mid"), t(312, 242, "> 40 ปี มีบุหรี่/ควัน", "xs mid"),
            t(312, 258, "เหนื่อยเวลาออกแรง ค่อยเป็นมากขึ้น", "xs mid"), t(312, 274, "ไม่กลับปกติ (persistent)", "xs mid b")]
    return fig("Asthma vs COPD — ความแปรปรวนของการอุดกั้น",
               "asthma อักเสบแบบ **type 2** (eosinophil) ทำให้กล้ามเนื้อเรียบหดตัวและบวมแบบกลับคืนได้ FEV1 จึงขึ้นลงและกลับปกติเมื่อได้ ICS · "
               "COPD มีการทำลายโครงสร้าง (emphysema, small airway พังผืด) **FEV1 ต่ำค้าง** ตอบสนองยาขยายหลอดลมเพียงเล็กน้อย · "
               "GOLD 2026: ค่า bronchodilator reversibility และ eosinophil **แยกสองโรคไม่ได้แน่นอน** ใช้ภาพรวมทางคลินิก · ถ้ามีทั้งสองโรค ให้รักษาตามแนวทาง asthma (ต้องมี ICS)",
               svg(420, 294, "กราฟ FEV1 ตามเวลาของ asthma ที่แปรปรวนเทียบ COPD ที่ต่ำค้าง พร้อมตารางเปรียบเทียบ", *out))


# ───────────────────────────── 11. β2 / M3 receptors
def receptors():
    out = [box(10, 8, 190, 34, "ok", "SABA / LABA", "b tok", fs=12),
           box(220, 8, 190, 34, "bx", "vagus → acetylcholine", "b", fs=12),
           ar(105, 42, 105, 84, "lok", "ah-ok"), ar(315, 42, 315, 84, "ln", "ah"),
           rect(6, 60, 408, 196, "sk", 12), t(180, 76, "เซลล์กล้ามเนื้อเรียบหลอดลม", "xs mid mu"),
           box(30, 84, 150, 30, "ok", "β2 receptor", "b", fs=12),
           box(240, 84, 150, 30, "ms", "M3 receptor", "b", fs=12),
           box(300, 52, 30, 22, "bad", "✕", "b tbad", fs=13), t(338, 64, "SAMA/LAMA", "xs b tbad"), t(338, 77, "บล็อกตรงนี้", "xs tbad"),
           ar(105, 114, 105, 128, "ln", "ah"), ar(315, 114, 315, 128, "ln", "ah"),
           box(30, 128, 150, 28, "bx", "Gs → adenylyl cyclase", fs=11),
           box(240, 128, 150, 28, "bx", "Gq → PLC → IP3", fs=11),
           ar(105, 156, 105, 170, "ln", "ah"), ar(315, 156, 315, 170, "ln", "ah"),
           box(30, 170, 150, 28, "bx", "cAMP ↑ → PKA", fs=11),
           box(240, 170, 150, 28, "bx", "Ca2+ ในเซลล์ ↑", fs=11),
           ar(105, 198, 105, 212, "lok", "ah-ok"), ar(315, 198, 315, 212, "lbad", "ah-bad"),
           box(30, 212, 150, 34, "ok", "Ca2+ ↓ · MLCK ถูกยับยั้ง\n→ คลายตัว", fs=10.5),
           box(240, 212, 150, 34, "bad", "myosin หดตัว + ต่อมเมือก\nหลั่งมาก → หลอดลมตีบ", fs=10.5),
           box(10, 264, 400, 54, "ac", None),
           t(210, 280, "β2 agonist: ใจสั่น · มือสั่น · K ต่ำ (Na/K-ATPase ดึง K เข้าเซลล์)", "xs mid"),
           t(210, 296, "antimuscarinic: ปากแห้ง · ปัสสาวะคั่ง (ต่อมลูกหมากโต)", "xs mid"),
           t(210, 312, "· ต้อหินมุมปิดถ้าละอองเข้าตา (พ่นผ่าน mask)", "xs mid")]
    return fig("ยาขยายหลอดลมออกฤทธิ์ที่ไหน — β2 กับ M3",
               "ทางซ้าย: **β2 agonist** จับ β2 receptor → Gs → cAMP ↑ → PKA ลด Ca2+ และยับยั้ง myosin light-chain kinase → กล้ามเนื้อเรียบคลาย · "
               "ทางขวา: เส้นประสาท vagus หลั่ง acetylcholine จับ **M3** → Gq → IP3 → Ca2+ ↑ → หดตัวและหลั่งเมือก · ใน COPD **cholinergic tone สูง** ยา antimuscarinic (**SAMA ipratropium, LAMA tiotropium**) จึงได้ผลดี · "
               "สองกลไกเสริมกัน = เหตุผลของ **LABA+LAMA** · กล่องล่างคือผลข้างเคียงที่อธิบายด้วย receptor เดียวกันในอวัยวะอื่น",
               svg(420, 324, "กลไก β2 receptor และ M3 receptor ในเซลล์กล้ามเนื้อเรียบหลอดลม และตำแหน่งที่ยาออกฤทธิ์", *out))


# ───────────────────────────── 12. inhaler inspiratory flow
def inhaler():
    X = lambda s: 50 + s * 62
    Y = lambda f: 170 - f * 1.5
    out = [line(50, 170, 400, 170, "ln"), line(50, 170, 50, 30, "ln"),
           t(225, 198, "เวลา (วินาที)", "xs mid i2"), t(8, 20, "แรงสูด (L/min)", "xs i2")]
    for s in range(0, 6):
        out += [line(X(s), 170, X(s), 174, "ln"), t(X(s), 184, str(s), "xs mid mu")]
    for f in (30, 60, 90):
        out += [line(46, Y(f), 50, Y(f), "ln"), t(42, Y(f) + 4, str(f), "xs end mu")]
    pm = [(0, 0), (0.4, 28), (1, 30), (3, 30), (4, 28), (4.5, 0)]
    dp = [(0, 0), (0.25, 75), (0.6, 85), (1.2, 70), (2, 40), (2.6, 0)]
    out += [_curve(pm, "lac w3", X, Y), _curve(dp, "lms w3", X, Y),
            t(X(3.6), Y(30) - 8, "pMDI / SMI: ช้า ลึก 3–5 วิ", "xs b tac"),
            t(X(1.25), Y(80) - 4, "DPI: แรง เร็ว ตั้งแต่ต้น", "xs b tms"),
            t(X(2.65), Y(30) + 18, "pMDI: กดพ่นพร้อมเริ่มสูด", "xs tac"),
            box(10, 208, 196, 82, "ac", None), t(108, 226, "pMDI", "sm b mid tac"),
            t(108, 243, "ละอองพุ่งเร็ว ถ้าสูดแรง", "xs mid"), t(108, 258, "จะกระแทกคอ (> 5 µm)", "xs mid"),
            t(108, 274, "ใช้ spacer ถ้าจังหวะไม่ตรง", "xs mid b"),
            box(214, 208, 196, 82, "ms", None), t(312, 226, "DPI", "sm b mid tms"),
            t(312, 243, "ผงต้องใช้แรงลมปั่น (turbulence)", "xs mid"), t(312, 258, "จึงแตกเป็นอนุภาคเล็ก", "xs mid"),
            t(312, 274, "สูดแรงไม่ได้ → เปลี่ยน device", "xs mid b")]
    return fig("สูดยาให้ถูก device — แรงสูดต่างกัน",
               "**pMDI/SMI** ปล่อยละอองที่พุ่งเร็วอยู่แล้ว ต้อง **สูดช้าและลึก** พร้อมกดพ่น ถ้าสูดแรงละอองจะกระแทกคอหอยแทนลงปอด · "
               "**DPI** ไม่มีแรงขับในตัว ต้อง **สูดแรงและเร็วตั้งแต่ต้น** ให้เกิดลมหมุนในเครื่องจนผงยาแตกเป็นอนุภาค 1–5 µm · ทั้งสองแบบ **หายใจออกให้สุดก่อน (ไม่เป่าใส่เครื่อง) และกลั้นหายใจ 5–10 วินาทีหลังสูด** · "
               "GOLD 2026: ผู้ป่วยกว่า 2 ใน 3 ใช้ผิดอย่างน้อย 1 ขั้น ต้องให้สาธิตกลับ (teach-back) ทุกครั้งที่นัด",
               svg(420, 296, "กราฟแรงสูดตามเวลาของ pMDI ที่ต้องสูดช้า เทียบ DPI ที่ต้องสูดแรงเร็ว", *out))


# ───────────────────────────── 13. initial pharmacotherapy
def initial_rx():
    out = [box(10, 8, 400, 74, "bad", None), t(30, 34, "E", "b tbad", fs=24),
           t(220, 30, "LABA + LAMA", "b mid", fs=15),
           t(220, 50, "eos ≥ 300 → พิจารณา LABA + LAMA + ICS", "xs mid b tbad"),
           t(220, 68, "ไม่ใช้ LABA + ICS (ถ้าต้องมี ICS ให้ใช้ triple)", "xs mid"),
           box(10, 92, 196, 80, "ok", None), t(28, 116, "A", "b tok", fs=24),
           t(118, 116, "ยาขยายหลอดลม", "sm b mid"), t(118, 134, "1 ตัว", "sm b mid"),
           t(108, 156, "long-acting ดีกว่าถ้ามี/จ่ายได้", "xs mid"),
           box(214, 92, 196, 80, "ms", None), t(232, 116, "B", "b tms", fs=24),
           t(322, 120, "LABA + LAMA", "sm b mid"),
           t(312, 142, "ไม่เหมาะ → LABA หรือ LAMA", "xs mid"), t(312, 156, "+ หาโรคร่วม (หัวใจ ซึมเศร้า)", "xs mid"),
           box(10, 182, 400, 34, "ac", "ทุกกลุ่ม: SABA (หรือ SAMA) พ่นเมื่อมีอาการ · สอน inhaler technique", "b", fs=11.5),
           box(10, 224, 400, 50, "sk", None),
           t(210, 242, "นอกจากยา: เลิกบุหรี่ · วัคซีน · ออกกำลังกาย · B/E → pulmonary rehab", "xs mid"),
           t(210, 260, "นัดประเมินซ้ำ: อาการ (CAT/mMRC) · exacerbation · ท่าพ่นยา · adherence", "xs mid")]
    return fig("ยาเริ่มต้นตามกลุ่ม ABE (GOLD 2026 Figure 3.8)",
               "**A** = ยาขยายหลอดลมตัวเดียว (ถ้าเหนื่อยนาน ๆ ครั้งใช้ short-acting ได้) · **B** = **LABA+LAMA** (RCT ในคน CAT ≥ 10 ดีกว่า LAMA เดี่ยว) · "
               "**E** = **LABA+LAMA** ซึ่งลด exacerbation ได้ดีที่สุดในยาขยายหลอดลม · เพิ่ม ICS ตั้งแต่ต้นเฉพาะเมื่อ **eosinophil ≥ 300 cells/µL** · "
               "**LABA+ICS ไม่แนะนำใน COPD** — ถ้ามีข้อบ่งชี้ ICS ให้เป็น triple เพราะดีกว่า · ถ้ามี asthma ร่วม รักษาแบบ asthma",
               svg(420, 280, "แผนภาพยาเริ่มต้นสำหรับกลุ่ม A B และ E ตาม GOLD 2026", *out))


# ───────────────────────────── 14. eosinophil & ICS
def eos_ics():
    out = [t(210, 18, "blood eosinophil (cells/µL) — ประโยชน์ของ ICS ในการลด exacerbation", "xs mid b"),
           box(10, 30, 126, 64, "bad", None), t(73, 54, "< 100", "b mid tbad"), t(73, 72, "ได้ประโยชน์น้อย", "xs mid"), t(73, 86, "เสี่ยง pneumonia เด่น", "xs mid"),
           box(146, 30, 128, 64, "ms", None), t(210, 54, "100 – 299", "b mid tms"), t(210, 72, "พิจารณาเมื่อมี", "xs mid"), t(210, 86, "exacerbation ซ้ำ", "xs mid"),
           box(284, 30, 126, 64, "ok", None), t(347, 54, "≥ 300", "b mid tok"), t(347, 72, "ได้ประโยชน์มากสุด", "xs mid"), t(347, 86, "(T2 inflammation)", "xs mid"),
           line(20, 108, 400, 108, "lok w3", "ah-ok"), t(210, 124, "ยิ่ง eos สูง ICS ยิ่งลด exacerbation ได้มาก", "xs mid tok"),
           box(10, 134, 400, 46, "sk", None),
           t(210, 152, "ระวัง/ไม่ใช้ ICS: pneumonia ซ้ำ · ประวัติ TB/NTM หรือ TB sequelae", "xs mid b tbad"),
           t(210, 168, "(GOLD 2026: ICS ขนาดสูงเพิ่มความเสี่ยงวัณโรค — แยก active TB ก่อนเริ่มยา)", "xs mid")]
    return fig("Blood eosinophil กับการเลือกใช้ ICS",
               "eosinophil ในเลือดสะท้อน **การอักเสบแบบ type 2** ในหลอดลม ซึ่งเป็นส่วนที่ steroid ระงับได้ · ผู้ป่วย COPD ที่ eos ต่ำ การอักเสบเป็นแบบ neutrophil ซึ่ง steroid ไม่ค่อยได้ผล "
               "ได้แต่ผลเสีย (pneumonia, เชื้อรา, TB) · ใช้ eos ร่วมกับประวัติ exacerbation เสมอ ไม่ใช้ eos ตัวเดียว · "
               "ช่วงตัวเลข 3 ระดับนี้ตรงกับข้อความใน GOLD 2026 (≥ 300 เริ่มได้ตั้งแต่แรก · ≥ 100 เพิ่มเมื่อยัง exacerbate · < 100 ไม่ได้ประโยชน์)",
               svg(420, 186, "แถบระดับ blood eosinophil 3 ช่วงกับประโยชน์ของ ICS และข้อควรระวัง", *out))


# ───────────────────────────── 15. LTOT
def ltot():
    out = [box(80, 6, 260, 40, "bx", "COPD ระยะคงที่ (ไม่ใช่ช่วง exacerbation)\nSpO2 ขณะพัก ≤ 92% → เจาะ ABG", fs=11),
           ar(210, 46, 210, 64, "ln", "ah"),
           box(10, 64, 196, 78, "bad", None), t(108, 84, "PaO2 ≤ 55 mmHg", "sm b mid tbad"), t(108, 100, "หรือ SaO2 ≤ 88%", "xs mid"),
           t(108, 116, "± hypercapnia", "xs mid"), t(108, 132, "ยืนยัน 2 ครั้งใน 3 สัปดาห์", "xs mid"),
           box(214, 64, 196, 78, "ms", None), t(312, 82, "PaO2 55–60 mmHg", "sm b mid tms"), t(312, 98, "(SaO2 88%) ร่วมกับ", "xs mid"),
           t(312, 112, "PH · ขาบวม (cor pulmonale)", "xs mid"), t(312, 126, "· Hct > 55%", "xs mid"),
           ar(108, 142, 190, 158, "lbad", "ah-bad"), ar(312, 142, 230, 158, "lms", "ah-ms"),
           box(80, 158, 260, 50, "ok", None), t(210, 178, "LTOT > 15 ชั่วโมง/วัน", "b mid tok"), t(210, 196, "ยืดชีวิตได้ (NOTT, MRC)", "xs mid"),
           ar(210, 208, 210, 222, "ln", "ah"),
           box(10, 222, 400, 34, "bx", "ประเมินซ้ำ 60–90 วัน (ABG/SpO2 ทั้ง room air และขณะให้ O2)", fs=10.5),
           box(10, 266, 400, 46, "sk", None),
           t(210, 284, "desaturation ปานกลาง (ขณะพักหรือออกแรง) → LTOT ไม่ยืดชีวิต ไม่ลด admit (LOTT)", "xs mid"),
           t(210, 300, "24 ชม./วัน ไม่ดีกว่า 15 ชม./วัน · ห้ามสูบบุหรี่ใกล้ออกซิเจน (ไฟไหม้)", "xs mid b")]
    return fig("ข้อบ่งชี้ long-term oxygen therapy (LTOT)",
               "ต้องวัดตอน **stable** เพราะช่วง exacerbation ออกซิเจนต่ำชั่วคราว · เกณฑ์ GOLD 2026: **PaO2 ≤ 55 mmHg หรือ SaO2 ≤ 88%** ยืนยัน 2 ครั้งในช่วง 3 สัปดาห์ "
               "หรือ **PaO2 55–60 mmHg ที่มีหลักฐานว่า hypoxemia ทำร้ายอวัยวะแล้ว** (pulmonary hypertension, ขาบวมจาก cor pulmonale, Hct > 55%) · "
               "ได้ประโยชน์เพราะแก้ hypoxic vasoconstriction และ polycythemia — คนที่ออกซิเจนต่ำปานกลางยังไม่มีวงจรนี้ จึงไม่ได้ประโยชน์ด้านการรอดชีวิต",
               svg(420, 318, "แผนผังเกณฑ์ให้ long-term oxygen therapy ตามค่า PaO2 และภาวะแทรกซ้อน", *out))


# ───────────────────────────── 16. AECOPD management flow
def ae_flow():
    out = [box(60, 6, 300, 40, "bx", "เหนื่อย/ไอ/เสมหะ แย่ลงภายใน ≤ 14 วัน\nแยกโรคเลียนแบบ: pneumonia · PE · HF · pneumothorax", fs=10.5),
           ar(210, 46, 210, 60, "ln", "ah"),
           box(60, 60, 300, 36, "ms", "ประเมินความรุนแรง (Rome) + ABG ถ้า SpO2 ต่ำ/ซึม", "b", fs=11),
           ar(210, 96, 210, 110, "ln", "ah"),
           box(10, 110, 400, 132, "sk", None),
           t(24, 130, "1. O2 แบบควบคุม เป้า SpO2 88–92% (Venturi 24–28%)", "xs b"),
           t(24, 150, "2. SABA ± SAMA พ่น ทุก 1 ชม. 2–3 ครั้ง → ทุก 2–4 ชม.", "xs b"),
           t(36, 164, "nebulizer ใช้ลมอัด (air-driven) ไม่ใช้ O2 ขับ", "xs i2"),
           t(24, 184, "3. Prednisolone 40 mg/วัน × 5 วัน (oral = IV)", "xs b"),
           t(24, 204, "4. Antibiotic ถ้าเสมหะเป็นหนอง + อีก 1 อาการ หรือใช้ NIV/ventilator", "xs b"),
           t(36, 218, "amox-clav · macrolide · doxycycline · 5 วัน", "xs i2"),
           t(24, 236, "+ VTE prophylaxis · ไม่ใช้ aminophylline IV", "xs i2"),
           ar(210, 242, 210, 256, "ln", "ah"),
           box(60, 256, 300, 34, "bx", "ABG ซ้ำ 30–60 นาที", "b", fs=11.5),
           ar(120, 290, 80, 306, "lbad", "ah-bad"), ar(300, 290, 340, 306, "lok", "ah-ok"),
           box(10, 306, 196, 52, "bad", None), t(108, 326, "pH ≤ 7.35 + PaCO2 ≥ 45", "xs mid b tbad"), t(108, 344, "→ NIV (BiPAP)", "sm mid b"),
           box(214, 306, 196, 52, "ok", None), t(312, 326, "ดีขึ้น", "xs mid b tok"), t(312, 344, "→ เริ่ม/ปรับ LABD ก่อนกลับบ้าน", "xs mid")]
    return fig("แนวทางรักษา AECOPD ในห้องฉุกเฉิน",
               "เรียงตามลำดับที่ทำจริง · **O2 ให้แบบควบคุม** เพราะออกซิเจนมากเกินทำให้ CO2 คั่ง · **SABA ± SAMA** เป็นยาขยายหลอดลมตัวแรก · "
               "**steroid 5 วัน** ลดเวลาหาย treatment failure และวันนอน · **antibiotic** เฉพาะผู้ที่มีหลักฐานติดเชื้อแบคทีเรีย (เสมหะเป็นหนอง) หรือใช้เครื่องช่วยหายใจ · "
               "ABG ซ้ำหลังให้ O2 เพื่อดูว่า CO2 ขึ้นหรือ pH ตก → NIV · เป้า SpO2 88–92% อยู่ในรูปของ GOLD ที่อ่านไม่ได้ — อิง GOLD 2023–2025 และ BTS oxygen guideline",
               svg(420, 364, "แผนผังการรักษา COPD exacerbation ตั้งแต่ประเมิน ให้ออกซิเจน ยา จนถึงการตัดสินใจใช้ NIV", *out))


# ───────────────────────────── 17. O2-induced hypercapnia
def o2_co2():
    def panel(x0, title, poor_flow, tc):
        o = [t(x0 + 100, 18, title, "sm b mid " + tc),
             circ(x0 + 50, 62, 28, "wa"), t(x0 + 50, 58, "ระบายดี", "xs mid"), t(x0 + 50, 72, "V/Q สูง", "xs mid b"),
             circ(x0 + 150, 62, 28, "sk"), t(x0 + 150, 58, "เสมหะอุด", "xs mid"), t(x0 + 150, 72, "V/Q ต่ำ", "xs mid b"),
             path("M%s 92 L%s 92" % (x0 + 50, x0 + 50), "ln"),
             line(x0 + 50, 90, x0 + 50, 112, "lbad " + ("w3" if not poor_flow else "w2")),
             line(x0 + 150, 90, x0 + 150, 112, "lbad " + ("w5" if poor_flow else "w2 da")),
             line(x0 + 20, 112, x0 + 180, 112, "lbad w2"),
             ar(x0 + 100, 132, x0 + 100, 114, "lbad", "ah-bad"), t(x0 + 100, 146, "เลือดดำ CO2 สูง", "xs mid tbad")]
        return o
    out = panel(0, "ก่อนให้ O2 สูง", False, "tok") + panel(214, "หลังให้ O2 สูงเกิน", True, "tbad")
    out += [t(100, 166, "HPV หดหลอดเลือดถุงลมเสีย", "xs mid"), t(100, 180, "เลือดไปถุงลมดี → ขับ CO2 ได้", "xs mid tok"),
            t(314, 166, "O2 ปลด HPV → เลือดไหลกลับ", "xs mid"), t(314, 180, "ไปถุงลมที่ระบายไม่ได้ → CO2 ค้าง", "xs mid tbad"),
            line(210, 10, 210, 186, "lru da"),
            box(10, 196, 196, 64, "ms", None), t(108, 214, "Haldane effect", "xs b mid tms"),
            t(108, 230, "O2 จับ Hb มากขึ้น → Hb ปล่อย", "xs mid"), t(108, 244, "CO2 ที่จับไว้ → PaCO2 ↑", "xs mid"),
            box(214, 196, 196, 64, "sk", None), t(312, 214, "hypoxic drive ลด", "xs b mid"),
            t(312, 230, "มีส่วนน้อยกว่าที่เคยเชื่อ", "xs mid"), t(312, 244, "minute ventilation ลดเล็กน้อย", "xs mid"),
            box(10, 270, 400, 40, "ok", None),
            t(210, 286, "ทางแก้: ไม่ใช่งด O2 แต่ให้แบบควบคุม SpO2 88–92%", "xs mid b"),
            t(210, 302, "Venturi mask · ABG ซ้ำใน 30–60 นาที · CO2 สูง + pH ต่ำ → NIV", "xs mid")]
    return fig("ทำไมออกซิเจนมากเกินทำให้ CO2 คั่งใน COPD",
               "กลไกหลักคือ **V/Q mismatch แย่ลง**: ปกติถุงลมที่เสมหะอุดจะมี PAO2 ต่ำจนหลอดเลือดหดตัว (HPV) เลือดถูกส่งไปถุงลมที่ระบายดี · เมื่อให้ O2 ความเข้มข้นสูง "
               "PAO2 ในถุงลมเสียก็สูงขึ้น HPV ถูกปลด เลือดไหลกลับไปถุงลมที่ **ระบายอากาศไม่ได้ จึงขับ CO2 ไม่ได้** · ร่วมกับ **Haldane effect** (Hb ที่จับ O2 ปล่อย CO2 ออกมา) "
               "และ hypoxic drive ที่ลดลงเล็กน้อย · ผลคือ respiratory acidosis ซึม — แต่ hypoxemia ฆ่าคนได้เร็วกว่า **ห้ามงด O2** ให้ตามเป้าแทน",
               svg(420, 316, "เทียบการไหลเวียนเลือดในถุงลมก่อนและหลังให้ออกซิเจนสูง พร้อม Haldane effect", *out))


# ───────────────────────────── 18. NIV / IMV
def niv():
    Y = lambda ph: 30 + (7.45 - ph) * 600
    out = [t(70, 18, "pH (ABG)", "sm b mid"),
           rect(50, Y(7.45), 40, Y(7.35) - Y(7.45), "ok", 0), rect(50, Y(7.35), 40, Y(7.25) - Y(7.35), "ms", 0),
           rect(50, Y(7.25), 40, Y(7.15) - Y(7.25), "bad", 0)]
    for ph in (7.45, 7.35, 7.25, 7.15):
        out += [line(44, Y(ph), 96, Y(ph), "ln"), t(40, Y(ph) + 4, "%.2f" % ph, "xs end")]
    out += [box(110, Y(7.45) + 4, 300, Y(7.35) - Y(7.45) - 8, "ok", "O2 ควบคุม + ยา · เฝ้าดู ABG", fs=11),
            box(110, Y(7.35) + 4, 300, Y(7.25) - Y(7.35) - 8, "ms", "NIV (BiPAP) ในหอที่เฝ้าระวังได้\nprotocol IPAP เริ่ม ~10–12 · EPAP 4–5 cmH2O", fs=10.5),
            box(110, Y(7.25) + 4, 300, Y(7.15) - Y(7.25) - 8, "bad", "NIV ใน ICU · เตรียมใส่ท่อช่วยหายใจ\nถ้าไม่ดีขึ้นใน 1–2 ชม.", fs=10.5),
            box(10, 222, 196, 120, "ms", None), t(108, 240, "ข้อบ่งชี้ NIV (≥ 1)", "xs b mid tms"),
            t(18, 258, "• pH ≤ 7.35 + PaCO2 ≥ 45", "xs"), t(18, 274, "• เหนื่อยมาก กล้ามเนื้อหายใจล้า", "xs"),
            t(26, 288, "(accessory muscle, ท้องบุ๋ม", "xs i2"), t(26, 302, "สวนทางทรวงอก)", "xs i2"),
            t(18, 318, "• hypoxemia ไม่ดีขึ้นแม้ให้ O2", "xs"),
            box(214, 222, 196, 120, "bad", None), t(312, 240, "ข้อบ่งชี้ใส่ท่อ (IMV)", "xs b mid tbad"),
            t(222, 258, "• NIV ล้มเหลว/ทนไม่ได้", "xs"), t(222, 274, "• หยุดหายใจ/หัวใจหยุดเต้น", "xs"),
            t(222, 290, "• ซึมลง กระสับกระส่ายคุมไม่ได้", "xs"), t(222, 306, "• สำลัก อาเจียนต่อเนื่อง ขับเสมหะไม่ได้", "xs"),
            t(222, 322, "• shock · arrhythmia รุนแรง", "xs")]
    return fig("เมื่อไรใช้ NIV เมื่อไรใส่ท่อช่วยหายใจ",
               "**NIV เป็นวิธีแรกของ acute hypercapnic respiratory failure ใน COPD** สำเร็จ 80–85% เพิ่ม pH ลด PaCO2 ลดงานการหายใจ **ลดการใส่ท่อและลดตาย** · "
               "กลไก: IPAP ช่วยแรงหายใจเข้าให้ tidal volume ใหญ่ขึ้น (ขับ CO2) · EPAP ต้าน auto-PEEP จาก air trapping ทำให้เริ่มหายใจเข้าง่ายขึ้น · "
               "แถบ pH แบ่งตามการจำแนกผู้ป่วยในของ GOLD 2026 (ventilatory failure = pH ≤ 7.25) · รายการข้อบ่งชี้ NIV/IMV เป็นรูปที่อ่านไม่ได้ อิง GOLD 2025 Figure 4.8–4.9 · ค่าตั้งเครื่องเป็นค่าเริ่มต้นทั่วไป",
               svg(420, 348, "แถบ pH กับระดับการรักษา และรายการข้อบ่งชี้ NIV และการใส่ท่อช่วยหายใจ", *out))


# ───────────────────────────── 19. follow-up algorithm (read more)
def followup_rx():
    out = [box(10, 6, 400, 36, "sk", "ทบทวน → ประเมิน (ท่าพ่นยา adherence โรคร่วม) → ปรับยา", "b", fs=11.5),
           t(108, 62, "ปัญหาหลัก: เหนื่อย", "sm b mid tac"), t(312, 62, "ปัญหาหลัก: exacerbation", "sm b mid tbad"),
           box(10, 72, 196, 36, "bx", "ยาเดี่ยว → LABA + LAMA", fs=11),
           ar(108, 108, 108, 122, "ln", "ah"),
           box(10, 122, 196, 74, "ac", None), t(108, 140, "ยังเหนื่อย", "xs mid b"),
           t(108, 156, "เปลี่ยน device/ตัวยา", "xs mid"), t(108, 170, "pulmonary rehab", "xs mid"), t(108, 184, "ensifentrine (ถ้ามี)", "xs mid"),
           box(10, 206, 196, 52, "sk", None), t(108, 224, "หาเหตุอื่นของเหนื่อย", "xs mid b"), t(108, 240, "หัวใจ ซีด อ้วน ซึมเศร้า", "xs mid"),
           box(214, 72, 196, 36, "bx", "ยาเดี่ยว → LABA + LAMA", fs=11),
           ar(312, 108, 312, 122, "ln", "ah"),
           box(214, 122, 196, 50, "ms", None), t(312, 140, "LABA + LAMA ยัง exacerbate", "xs mid b"),
           t(312, 156, "eos ≥ 100 → + ICS (triple)", "xs mid"),
           ar(260, 172, 260, 186, "ln", "ah"), ar(364, 172, 364, 186, "ln", "ah"),
           box(214, 186, 92, 102, "sk", None), t(260, 202, "eos < 100", "xs mid b"), t(260, 218, "azithromycin", "xs mid"),
           t(260, 232, "(ไม่สูบบุหรี่)", "xs mid i2"), t(260, 250, "roflumilast", "xs mid"), t(260, 264, "(FEV1 < 50%", "xs mid i2"), t(260, 276, "+ CB)", "xs mid i2"),
           box(312, 186, 98, 102, "bad", None), t(361, 202, "triple ยัง", "xs mid b"), t(361, 216, "exacerbate", "xs mid b"),
           t(361, 234, "eos ≥ 300:", "xs mid"), t(361, 248, "dupilumab (CB)", "xs mid"), t(361, 262, "mepolizumab", "xs mid"), t(361, 278, "หรือ azithro/roflu", "xs mid i2"),
           t(210, 306, "ใช้ได้ทุกคนที่ได้ยาแล้ว ไม่ว่าตอนเริ่มอยู่กลุ่มไหน · มีทั้งสองปัญหา → ใช้เส้นทาง exacerbation", "xs mid"),
           t(210, 322, "CB = chronic bronchitis (ไอมีเสมหะเรื้อรัง)", "xs mid mu")]
    return fig("ปรับยาระหว่างติดตาม (GOLD 2026 Figure 3.9)",
               "หลังเริ่มยาแล้ว ไม่ต้องจัดกลุ่ม ABE ใหม่ ให้ดู **treatable trait** ที่เด่น · เส้นทางเหนื่อย: ขยายหลอดลมให้เต็มที่แล้วหันไปหา rehab และสาเหตุอื่น · "
               "เส้นทาง exacerbation: LABA+LAMA → เพิ่ม ICS ถ้า eos ≥ 100 → ยาเสริมตามลักษณะผู้ป่วย · **azithromycin** ลด exacerbation แต่ระวังเชื้อดื้อยา QT ยาว และการได้ยิน · "
               "**roflumilast** (PDE4 inhibitor) เฉพาะ FEV1 < 50% + chronic bronchitis + เคย admit · **biologics** เฉพาะ eos ≥ 300 ที่ยัง exacerbate บน triple",
               svg(420, 330, "แผนผังปรับยา COPD ระหว่างติดตาม แยกเส้นทางเหนื่อยและ exacerbation", *out))


# ───────────────────────────── 20. endobronchial valve (read more)
def ebv():
    out = [t(105, 18, "ก่อนใส่ valve", "sm b mid"), t(315, 18, "หลังใส่ valve", "sm b mid tok"),
           path("M30 40 Q105 26 180 40 L186 190 L24 190 Z", "bx"),
           ell(105, 84, 62, 42, "ms"), t(105, 80, "กลีบบนพองมาก", "xs mid b"), t(105, 94, "(emphysema)", "xs mid"),
           ell(105, 158, 52, 22, "wa"), t(105, 162, "ปอดดีถูกกด", "xs mid"),
           path("M26 194 Q105 184 184 194", "lbad w3"), t(105, 210, "กะบังลมแบน", "xs mid tbad"),
           path("M240 40 Q315 26 390 40 L396 190 L234 190 Z", "bx"),
           ell(315, 62, 50, 16, "sk"), t(315, 66, "กลีบบนยุบ", "xs mid"),
           ell(315, 128, 62, 42, "wa"), t(315, 126, "ปอดดีขยายได้", "xs mid b tok"),
           path("M236 192 Q315 150 394 192", "lok w3"), t(315, 210, "กะบังลมกลับเป็นโดม", "xs mid tok"),
           rect(304, 80, 22, 10, "acf", 3), t(336, 90, "valve ทางเดียว", "xs tac"),
           box(10, 222, 400, 42, "sk", None),
           t(210, 239, "ลมออกได้ เข้าไม่ได้ → กลีบที่พองยุบ · ต้องมี fissure สมบูรณ์ (ไม่มี collateral ventilation)", "xs mid"),
           t(210, 255, "ภาวะแทรกซ้อนสำคัญ: pneumothorax ~27% ส่วนใหญ่ใน 72 ชม.", "xs mid tbad")]
    return fig("Endobronchial one-way valve — ลดปริมาตรปอดโดยไม่ผ่าตัด",
               "กลีบปอดที่เป็น emphysema รุนแรงพองค้างกินที่ในทรวงอก กดปอดส่วนที่ยังดีและดันกะบังลมให้แบน · valve ทางเดียวที่ใส่ผ่านกล้องให้ลมออกได้แต่เข้าไม่ได้ "
               "กลีบนั้นจึงค่อย ๆ ยุบ (เหมือน LVRS โดยไม่ตัด) ปอดดีขยาย กะบังลมกลับเป็นโดม FEV1, 6MWD และคุณภาพชีวิตดีขึ้น · ถ้ามีลมรั่วข้ามกลีบ (collateral ventilation) กลีบจะไม่ยุบ",
               svg(420, 270, "เทียบทรวงอกก่อนและหลังใส่ endobronchial valve ในกลีบบนที่เป็น emphysema", *out))
