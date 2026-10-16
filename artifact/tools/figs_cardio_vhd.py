# -*- coding: utf-8 -*-
"""ภาพประกอบ + กลไก คาบ cardio 27 Valvular heart disease และ acute rheumatic fever (ใส่ด้วย apply_figs.py)"""
import math
from svg import *

SET, LEC = "cardio", "27"

MR_MD = """#### ทำไมถึงมีอาการนี้ — chronic MR
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **เหนื่อยง่าย หอบเมื่อออกแรง นอนราบไม่ได้** | เลือดที่รั่วเพิ่มปริมาตรใน LA ทุกจังหวะ → เมื่อ LA ยืดจนสุดหรือ LV เริ่มล้ม ความดันจึงย้อนเข้าปอด | acute MR เหนื่อยทันทีเพราะ LA ยังไม่ได้ขยาย |
| **อ่อนเพลีย** | เลือดที่ไปข้างหน้าลดลง แม้ LVEF ดูปกติ (ส่วนหนึ่งบีบย้อนเข้า LA) | LVEF ปกติจึงไม่ได้แปลว่า forward flow ปกติ |
| **ใจสั่น · AF** | LA ขยายและถูกยืดนาน → กล้ามเนื้อ atrium เป็นพังผืด ไฟฟ้าวน | AF ใหม่เป็นเหตุผลหนึ่งให้ผ่าตัดเร็วขึ้น |
| **S3** | เลือดปริมาณมากใน LA ไหลกลับเข้า LV อย่างเร็วต้น diastole | ใน MR รุนแรง S3 บอกปริมาตรมาก ไม่จำเป็นต้องแปลว่า LV ล้ม |
| **Murmur กระจายไปรักแร้** | jet พุ่งเข้า LA ซึ่งอยู่ด้านหลังซ้าย เสียงจึงไปทางรักแร้ซ้าย | AS กระจายขึ้นคอ · TR ดังที่ LLSB และดังขึ้นเมื่อหายใจเข้า |
| **Apex แรงและกว้าง** | LV ขยายรับปริมาตรเกิน บีบเลือดออกได้สองทาง (aorta + LA) | ต่างจาก AS ที่ apex ยกค้างแต่ไม่ย้าย |"""

AS_MD = """#### ทำไมถึงตรวจพบแบบนี้ — AS
| สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Ejection murmur ที่ RUSB กระจายขึ้นคอ** | เลือดพุ่งผ่านรูแคบเข้า aorta → กระแสวนไปตามทิศ aorta ขึ้นไปที่ carotid | MR กระจายไปรักแร้ · HOCM ไม่กระจายขึ้นคอ และดังขึ้นเมื่อยืน |
| **ยิ่งตีบ ยอดเสียงยิ่งช้า (late-peaking)** | รูยิ่งเล็ก LV ยิ่งใช้เวลานานกว่าจะดันเลือดผ่านได้มากที่สุด | ความดังบอกความรุนแรงไม่ได้ (LV อ่อนแรงแล้วเสียงเบาลง) แต่จังหวะยอดเสียงบอกได้ |
| **Pulsus parvus et tardus · pulse pressure แคบ** | เลือดออกได้น้อยและช้าผ่านลิ้นตีบ → ชีพจรขึ้นช้า ยอดต่ำ | ตรงข้ามกับ AR ที่ชีพจรพุ่งแรงและ PP กว้าง |
| **S2 เบาหรือเดี่ยว** | ลิ้นหินปูนแข็งขยับไม่ได้ → A2 เบาหรือหาย · LV บีบนาน A2 จึงช้าลงมาชน P2 | ลิ้นสองแฉกในคนอายุน้อยที่ยังขยับได้อาจมี ejection click |
| **LV heave ยกค้าง · S4** | LV หนาแบบ concentric แข็ง → ต้องพึ่งแรงบีบของ atrium เติมเลือดช่วงท้าย diastole | AF ใน AS ทำให้ทรุดเร็วเพราะเสีย atrial kick |
| **ECG: LVH with strain** | กล้ามเนื้อหนา (voltage สูง) + ชั้นใต้เยื่อบุด้านในขาดเลือดเรื้อรัง (ST กด T กลับใน V5–V6) | บอกว่ามี pressure overload มานาน |"""

TR_MD = """#### กลไก: ทำไม TR ให้ JVP v ใหญ่ ตับเต้น และบวม
- ช่วง systole เลือดจาก RV รั่วย้อนเข้า RA → คลื่นความดันส่งต่อขึ้น jugular vein → **v wave ใหญ่ (cv wave)** และ x descent หายไป
- RA ไม่มีลิ้นกั้นกับ IVC และหลอดเลือดดำตับ → แรงดันย้อนถึงตับ → **ตับโตและเต้นตามจังหวะหัวใจ**
- ความดันหลอดเลือดดำทั่วร่างกายสูงต่อเนื่อง → น้ำซึมออกจากหลอดเลือดฝอย → **ท้องมาน ขาบวม** แต่ปอดใส ต่างจากหัวใจซ้ายล้ม"""

ARF_MD = """#### ทำไมถึงมีอาการนี้ — ARF
| อาการ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Polyarthritis ข้อใหญ่ ย้ายที่** | การอักเสบจาก immune complex ที่ synovium ทีละข้อ แต่ไม่ทำลายกระดูกอ่อน → แต่ละข้ออักเสบไม่กี่วันแล้วย้าย หายสนิทไม่พิการ · ตอบสนองต่อ salicylate เร็วมาก | ไม่ดีขึ้นภายในราว 48 ชั่วโมงหลังให้ aspirin → คิดถึงโรคอื่น (septic arthritis, JIA, reactive arthritis) |
| **Apical pansystolic murmur (MR)** | valvulitis ของลิ้น mitral — ลิ้นบวม ขอบปิดไม่สนิท + วงแหวนขยาย | MR ที่เกิดใหม่ในเด็กที่มีไข้และข้ออักเสบ → นึกถึง ARF ก่อน |
| **Carey Coombs (mid-diastolic สั้นที่ apex)** | ลิ้น mitral ที่บวมอักเสบ + เลือดไหลผ่านมากขึ้น (จาก MR) ในช่วงเติมเลือดเร็ว | ไม่มี opening snap และหายได้เมื่อหายอักเสบ ต่างจาก MS เรื้อรัง |
| **หัวใจโต หัวใจล้มเหลว** | myocarditis + ปริมาตรเกินจาก MR/AR ที่เกิดเร็ว | เป็นกลุ่มที่ต้องให้ prednisolone (หัวข้อถัดไป) |
| **PR ยาว** | การอักเสบและ vagal tone ทำให้การนำไฟฟ้าผ่าน AV node ช้า | PR ยาวลำพังไม่ใช่ carditis — นับเป็น minor เท่านั้น |
| **Sydenham's chorea** | แอนติบอดีจับข้ามกับเซลล์ประสาทใน basal ganglia → สัญญาณ dopamine ผิดปกติ → เคลื่อนไหวกระตุกไร้จุดหมาย | เกิดช้าหลังติดเชื้อหลายเดือน ASO อาจลดลงแล้ว → จึงวินิจฉัยได้แม้ไม่มีหลักฐาน GAS |
| **Erythema marginatum · subcutaneous nodules** | การอักเสบที่ผิวหนังและเนื้อเยื่อเกี่ยวพัน (nodule มักพบร่วมกับ carditis รุนแรง) | ผื่นไม่คัน ขอบชัด ตรงกลางซีด ย้ายที่ — ต่างจากลมพิษ |
| **ไข้ · ESR/CRP สูง** | cytokine จากการอักเสบทั่วร่างกาย | ไม่จำเพาะ จึงเป็นแค่ minor |"""

INSERTS = [
    ("cardio-vhd-01", "**Thrill**", "fig:vhd_overload"),
    ("cardio-vhd-01", 'S2 ("dub")', "fig:vhd_cycle"),
    ("cardio-vhd-02", "**Rumbling** — ความดันต่าง", "fig:vhd_murmurs"),
    ("cardio-vhd-02", "**นั่งยองหรือกำมือ**", "fig:vhd_maneuver"),
    ("cardio-vhd-03", "**Opening snap (OS)**", "fig:vhd_ms_os"),
    ("cardio-vhd-04", "| **CXR** |", "fig:vhd_ms_cxr"),
    ("cardio-vhd-04", "เงื่อนไขที่เหมาะ:", "fig:vhd_pmbc"),
    ("cardio-vhd-05", "| รักษา | **แก้ลิ้น**", "fig:vhd_mr_types"),
    ("cardio-vhd-05", "**Chronic** — LA และ LV", "fig:vhd_mr_acute"),
    ("cardio-vhd-05", "- ECG: LA/LV โต AF", MR_MD),
    ("cardio-vhd-05", "**Maneuver**", "fig:vhd_mvp"),
    ("cardio-vhd-06", "**หลักคิด** — LVEF ใน MR", "fig:vhd_mr_ef"),
    ("cardio-vhd-07", "เมื่อมีอาการแล้วการพยากรณ์แย่ลงทันที", "fig:vhd_as_triad"),
    ("cardio-vhd-07", "- ECG: **LVH with strain**", AS_MD),
    ("cardio-vhd-07", "low-flow low-gradient", "fig:vhd_lflg"),
    ("cardio-vhd-08", "**กลไก** — stroke volume ใหญ่มาก", "fig:vhd_ar_pulse"),
    ("cardio-vhd-08", "**Acute AR**", "fig:vhd_ar_lv"),
    ("cardio-vhd-09", "= Carvallo's sign", TR_MD),
    ("cardio-vhd-09", "= Carvallo's sign", "fig:vhd_tr"),
    ("cardio-vhd-10", "**ผลระยะยาวที่สำคัญคือ rheumatic heart disease**", "fig:vhd_mimicry"),
    ("cardio-vhd-10", "**หลักฐาน GAS** —", ARF_MD),
    ("cardio-vhd-10", "$", "fig:vhd_rhd_valve"),
    ("cardio-vhd-11", "**การกลับเป็นซ้ำแต่ละครั้งทำลายลิ้นเพิ่ม**", "fig:vhd_bpg"),
    ("cardio-vhd-12", "อาการกึ่งเฉียบพลัน (viridans", "fig:vhd_ie_path"),
    ("cardio-vhd-12", "| Stroke · ไตหรือม้ามตาย", "fig:vhd_ie_jet"),
    ("cardio-vhd-13", "| **ป้องกัน emboli** |", "fig:vhd_ie_why"),
]


# ---------- ตัวช่วย ----------
def _plot(pts, X, Y, c):
    return poly([(X(a), Y(b)) for a, b in pts], c)


def _env(x1, x2, f, yb, c="lms w2", step=4):
    """ซองเสียง (phonocardiogram) — เส้นตั้งถี่ ๆ สูงตาม f(u) โดย u = 0..1"""
    out = []
    x = x1
    while x <= x2:
        h = f((x - x1) / max(1, x2 - x1))
        if h > 0.5:
            out.append(line(x, yb - h, x, yb + h, c))
        x += step
    return out


def _snd(x, yb, h=14):
    return rect(x - 2, yb - h, 4, 2 * h, "inkf", 1)


# ---------- คาบ 01 ----------
def vhd_cycle():
    X = lambda tt: 60 + tt * 340
    Y = lambda p: 236 - p * 1.5
    lv = [(0, 8), (0.02, 10), (0.06, 80), (0.12, 110), (0.2, 122), (0.28, 115), (0.34, 98), (0.38, 40), (0.42, 6),
          (0.5, 4), (0.7, 6), (0.86, 8), (0.9, 12), (0.95, 9), (1.0, 10)]
    ao = [(0, 82), (0.06, 80), (0.12, 108), (0.2, 120), (0.28, 114), (0.34, 100), (0.355, 95), (0.375, 99), (0.5, 94),
          (0.7, 88), (1.0, 82)]
    la = [(0, 9), (0.04, 11), (0.08, 6), (0.3, 12), (0.38, 14), (0.45, 8), (0.7, 7), (0.88, 12), (0.94, 8), (1, 9)]
    out = [rect(X(0.02), 30, X(0.345) - X(0.02), 206, "sk", 0),
           t((X(0.02) + X(0.345)) / 2, 24, "systole", "xs mid b"), t((X(0.345) + X(1)) / 2, 24, "diastole", "xs mid b"),
           line(X(0.02), 30, X(0.02), 236, "lmu da"), line(X(0.345), 30, X(0.345), 236, "lmu da"),
           line(X(0), Y(0), X(1), Y(0), "lmu"), line(X(0), Y(0), X(0), Y(130), "lmu"),
           _plot(ao, X, Y, "lbad w2"), _plot(la, X, Y, "lwa w2"), _plot(lv, X, Y, "ln w3"),
           t(X(0.045) - 6, Y(60), "LV", "sm b end"), t(X(0.72), Y(88) - 8, "Aorta", "sm b tbad"),
           t(X(0.2), Y(12) - 8, "LA", "sm b twa"), t(14, 24, "mmHg", "xs mu")]
    out += [p for v in (0, 40, 80, 120) for p in (line(X(0) - 4, Y(v), X(0), Y(v), "lmu"), t(X(0) - 7, Y(v) + 4, str(v), "xs end mu"))]
    out += [_snd(X(0.02) - 3, 262, 12), _snd(X(0.02) + 4, 262, 9), _snd(X(0.345) - 3, 262, 10), _snd(X(0.345) + 3, 262, 8),
            t(X(0.02) + 12, 258, "S1", "sm b"), t(X(0.02) + 12, 272, "M1 T1 ปิด", "xs i2"),
            t(X(0.345) + 12, 258, "S2", "sm b"), t(X(0.345) + 12, 272, "A2 P2 ปิด", "xs i2"),
            t(10, 302, "S1: LV บีบจนความดันเกิน LA → mitral ปิด → เริ่ม systole", "xs i2"),
            t(10, 320, "S2: LV คลายจนความดันต่ำกว่า aorta → aortic ปิด → เริ่ม diastole", "xs i2")]
    return fig("วงจรหัวใจ — เสียง S1 S2 เกิดตรงไหน",
               "ลิ้นหัวใจเปิดปิดตาม **ความต่างของความดัน** สองฝั่ง · LV บีบจนความดันเกิน LA ลิ้น mitral ปิด (S1) แล้วเกิน aorta ลิ้น aortic เปิด เลือดพุ่งออก · LV คลายจนความดันต่ำกว่า aorta ลิ้น aortic ปิด (S2) แล้วต่ำกว่า LA ลิ้น mitral เปิด เลือดไหลเข้า · murmur ทุกชนิดเข้าใจได้จากว่ามีความต่างของความดันผ่านลิ้นที่ผิดปกติในช่วงไหน",
               svg(420, 330, "กราฟความดัน LV aorta และ LA ในหนึ่งรอบการเต้นของหัวใจ พร้อมตำแหน่งเสียง S1 และ S2", *out))


def vhd_overload():
    return fig("Pressure overload กับ volume overload — คลำ apex ต่างกัน",
               "LV ปรับตัวต่างกันตามชนิดภาระ · **ความดันเกิน (AS)** ผนังหนาเข้าด้านใน โพรงไม่โต → apex อยู่ที่เดิมแต่ยกแรงและค้าง (sustained heave) LV แข็งจึงได้ S4 · **ปริมาตรเกิน (MR, AR)** โพรงขยาย → apex ย้ายลงล่างและออกด้านข้าง กว้างเกิน 3 ซม. และเลือดไหลเข้าเร็วได้ S3 · ส่วน **thrill** คือกระแสเลือดวนแรงจนสั่นถึงผนังอก = murmur เกรด 4 ขึ้นไป",
               svg(420, 300, "เปรียบเทียบ LV ที่หนาตัวจาก pressure overload กับ LV ที่ขยายจาก volume overload และสิ่งที่คลำและฟังได้",
                   t(105, 20, "Pressure overload", "sm b mid"), t(105, 36, "AS · ความดันใน LV สูง", "xs mid i2"),
                   t(315, 20, "Volume overload", "sm b mid"), t(315, 36, "MR · AR · ปริมาตรเกิน", "xs mid i2"),
                   ell(105, 118, 52, 68, "bad"), ell(105, 120, 22, 36, "bx"), t(105, 124, "โพรง", "xs mid"),
                   ell(315, 120, 74, 74, "bad"), ell(315, 120, 60, 60, "bx"), t(315, 124, "โพรงโต", "xs mid"),
                   t(105, 214, "sarcomere เพิ่มแบบขนาน → ผนังหนา", "xs mid"),
                   t(105, 232, "apex ไม่ย้าย · ยกค้าง (heave)", "xs mid b"),
                   t(105, 250, "LV แข็ง → S4", "xs mid tbad b"),
                   t(315, 214, "sarcomere ต่อแบบอนุกรม → โพรงโต", "xs mid"),
                   t(315, 232, "apex ย้ายลงล่าง/ออกข้าง > 3 ซม.", "xs mid b"),
                   t(315, 250, "เลือดไหลเข้าเร็ว → S3", "xs mid tbad b"),
                   line(210, 12, 210, 258, "lru da"),
                   t(210, 288, "Thrill = กระแสเลือดวนแรงจนสั่นถึงผนังอก = murmur ≥ 4/6", "xs mid i2")))


# ---------- คาบ 02 ----------
def vhd_murmurs():
    rows = [("AS", "ejection", lambda yb: _env(112, 208, lambda u: 18 * (1 - abs(2 * u - 1)), yb),
             "ความดัน LV–aorta ต่างกันมากสุดกลาง systole → ดังกลางแล้วเบา"),
            ("MR", "pansystolic", lambda yb: _env(104, 216, lambda u: 12, yb),
             "LV สูงกว่า LA ตลอด systole → ดังเท่ากันตั้งแต่ S1 ถึง S2"),
            ("AR", "blowing", lambda yb: _env(226, 340, lambda u: 16 * (1 - u), yb),
             "aorta สูงกว่า LV มากสุดต้น diastole → ดังแล้วค่อยเบา เสียงแหลม"),
            ("MS", "rumbling", lambda yb: (_env(262, 344, lambda u: 7 - 3 * u, yb, "lms w2", 3) +
                                           _env(356, 392, lambda u: 3 + 9 * u, yb, "lms w2", 3) + [_snd(250, yb, 9)]),
             "LA > LV เล็กน้อย ไหลช้า → ทุ้ม · atrium บีบ → ดังขึ้นก่อน S1")]
    out = [t(100, 14, "S1", "xs mid b"), t(220, 14, "S2", "xs mid b"), t(398, 14, "S1", "xs mid b"),
           t(160, 14, "systole", "xs mid mu"), t(309, 14, "diastole", "xs mid mu")]
    for k, (name, kind, draw, mech) in enumerate(rows):
        y0 = 22 + 88 * k
        yb = y0 + 30
        out += [rect(86, y0 + 4, 324, 52, "sk", 6), line(90, yb, 406, yb, "lru"),
                _snd(100, yb), _snd(220, yb), _snd(398, yb),
                t(10, yb + 2, name, "lg b"), t(10, yb + 18, kind, "xs i2"),
                *draw(yb), t(90, y0 + 74, mech, "xs i2")]
        if name == "MS":
            out.append(t(250, y0 + 16, "OS", "xs mid b"))
    return fig("รูปร่างของ murmur มาจากความต่างของความดัน",
               "เสียงฟู่ดังตาม **ความต่างของความดันสองฝั่งลิ้นในขณะนั้น** · AS ความต่างขึ้นแล้วลงตามการบีบ → รูปเพชร · MR ห้องล่างสูงกว่าห้องบนตลอด systole → ดังเท่ากันตลอด · AR aorta สูงกว่า LV มากที่สุดต้น diastole แล้วค่อยเท่ากัน → ดังแล้วเบา · MS ความต่างน้อย ไหลช้า → เสียงทุ้ม เริ่มหลัง opening snap และดังขึ้นช่วงท้ายเมื่อ atrium บีบ (หายไปเมื่อเป็น AF)",
               svg(420, 380, "รูปร่างเสียงฟู่ของ AS MR AR และ MS เทียบกับตำแหน่ง S1 S2 และกลไกจากความต่างของความดัน", *out))


def vhd_maneuver():
    rows = [("หายใจเข้า", "ความดันในอกเป็นลบ\nเลือดดำเข้าหัวใจขวา ↑", "bx", "murmur ด้านขวาดังขึ้น\n(Carvallo — TR)"),
            ("ยืน\nValsalva", "เลือดกลับหัวใจ ↓\npreload ↓ LV เล็กลง", "ms", "ส่วนใหญ่เบาลง\nHOCM ดังขึ้น\nMVP click เร็วขึ้น"),
            ("นั่งยอง\nกำมือ", "afterload ↑\n(นั่งยอง preload ↑ ด้วย)", "ok", "MR AR ดังขึ้น\nHOCM เบาลง\nMVP click ช้าลง")]
    out = []
    for k, (a, b, c, d) in enumerate(rows):
        y = 10 + 82 * k
        out += [box(10, y, 94, 70, "ac", a, "b", fs=12), line(104, y + 35, 118, y + 35, "ln", "ah"),
                box(120, y, 142, 70, "wa", b, fs=11), line(262, y + 35, 276, y + 35, "ln", "ah"),
                box(278, y, 132, 70, c, d, fs=11)]
    out += [t(10, 272, "HOCM: LV เล็ก → septum กับลิ้น mitral ชิดกัน → ทางออกแคบลง → ดังขึ้น", "xs i2"),
            t(10, 290, "MR/AR: ด้านหน้าต้านมากขึ้น (afterload ↑) → เลือดย้อนผ่านลิ้นที่รั่วมากขึ้น", "xs i2")]
    return fig("เทคนิคข้างเตียง — เปลี่ยน preload/afterload แล้วฟังซ้ำ",
               "ทุก maneuver ทำงานผ่าน **ปริมาตรเลือดที่กลับหัวใจ (preload) หรือแรงต้านด้านหน้า (afterload)** · murmur ส่วนใหญ่ดังตามปริมาณเลือดที่ไหลผ่าน จึงเบาลงเมื่อยืน · HOCM และ MVP กลับทาง เพราะ LV ที่เล็กลงทำให้ทางออกแคบลงและลิ้น mitral หย่อนเร็วขึ้น",
               svg(420, 298, "ผลของการหายใจเข้า การยืนหรือ Valsalva และการนั่งยองหรือกำมือ ต่อ preload afterload และเสียงฟู่แต่ละชนิด", *out))


# ---------- คาบ 03 ----------
def vhd_ms_os():
    X = lambda tt: 70 + tt * 550
    out = []
    for k, (title, la0, aa) in enumerate((("ตีบน้อย — LA ความดันสูงไม่มาก", 14, 6), ("ตีบมาก — LA ความดันสูงมาก", 30, 8))):
        y0 = 30 + 156 * k
        Y = lambda p, y0=y0: y0 + 104 - p * 0.86
        ts = [i / 200 for i in range(0, 121)]
        lv = lambda tt: 5 + 95 * math.exp(-tt / 0.03) + 6 * tt / 0.6
        la = lambda tt: la0 + (4 if tt < 0.04 else 0) * (1 - tt / 0.04) + (aa * math.sin(math.pi * (tt - 0.5) / 0.08) if 0.5 <= tt <= 0.58 else 0)
        tc = next(tt for tt in ts if lv(tt) < la(tt))
        shade = [(X(tt), Y(la(tt))) for tt in ts if tt >= tc] + [(X(tt), Y(lv(tt))) for tt in reversed(ts) if tt >= tc]
        out += [t(10, y0 - 8, title, "sm b"),
                poly(shade, "ms", closed=True),
                poly([(X(tt), Y(lv(tt))) for tt in ts], "lac w3"), poly([(X(tt), Y(la(tt))) for tt in ts], "lwa w3"),
                line(X(0), y0, X(0), Y(0), "lmu da"), line(X(tc), y0 + 30, X(tc), Y(0), "lbad da"),
                line(X(0.6), y0 + 30, X(0.6), Y(0), "lmu da"),
                t(X(0) - 4, Y(0) + 14, "S2", "xs b end"), t(X(tc) + 3, Y(0) + 14, "OS", "xs b tbad"),
                t(X(0.6), Y(0) + 14, "S1 ดัง", "xs b mid"),
                line(X(0), y0 + 22, X(tc), y0 + 22, "lbad w2"), t(X(tc) + 6, y0 + 26, "S2–OS", "xs b tbad"),
                t(X(0.2), Y(la(0.2)) - 6, "LA", "sm b twa"), t(X(0.03) + 8, Y(lv(0.03)), "LV", "sm b tac"),
                t(X(0.32), Y((la(0.32) + lv(0.32)) / 2) + 4, "gradient → rumble", "xs b tms") if k else "",
                line(X(0), Y(0), X(0.6), Y(0), "lmu")]
    out += [t(10, 362, "LA ยิ่งสูง → LV คลายลงถึงระดับ LA เร็วขึ้น → ลิ้นเปิด (OS) เร็วขึ้น", "xs i2"),
            t(10, 380, "→ ช่วง S2–OS สั้น = ตีบมาก · ลิ้นยังเปิดกว้างจนถึงท้าย diastole → S1 ดัง", "xs i2")]
    return fig("ทำไม S2–OS ยิ่งสั้นยิ่งตีบมาก",
               "หลัง S2 ความดัน LV ลดลงเรื่อย ๆ ลิ้น mitral ที่แข็งจะเด้งเปิดสุดทาง (opening snap) **ทันทีที่ความดัน LV ต่ำกว่า LA** · MS ยิ่งรุนแรง LA ยิ่งสูง จุดตัดจึงมาเร็ว ช่วง S2–OS สั้นลง · ช่องสีเหลืองคือความต่างของความดันตลอด diastole ที่ทำให้เกิด rumble · เมื่อหัวใจเต้นเร็ว diastole สั้นลง เลือดต้องผ่านรูแคบในเวลาน้อยลง LA จึงต้องดันแรงขึ้น → ความดันในปอดพุ่ง",
               svg(420, 388, "กราฟความดัน LV และ LA ช่วง diastole ใน mitral stenosis ระดับน้อยและมาก แสดงว่าเมื่อ LA สูง opening snap มาเร็ว", *out))


# ---------- คาบ 04 ----------
def vhd_ms_cxr():
    heart = ("M182 104 L178 160 Q146 192 162 236 Q178 264 222 266 L282 262 Q320 250 312 214 Q306 186 286 178 "
             "Q300 166 286 152 Q300 140 284 128 Q302 112 276 98 Q252 86 232 98 L216 104 Z")
    return fig("MS บน CXR — ทุกอย่างมาจาก LA ที่โต",
               "LA อยู่ด้านหลังใต้ carina · เมื่อโตจะ **ดันหลอดลมใหญ่สองข้างถ่างออก (มุม carina กว้าง)** · ขอบของ LA ซ้อนกับเงาหัวใจด้านขวาเป็น **double contour** · LA appendage ที่โปนทำให้ขอบหัวใจซ้ายตรงหรือโป่ง · LV มักไม่โตใน MS ล้วนเพราะได้เลือดน้อย · ความดันหลอดเลือดดำปอดสูงดันน้ำเข้า interlobular septa เห็นเป็น **Kerley B lines** · เมื่อมี PH จะเห็น pulmonary artery โต",
               svg(420, 300, "ภาพวาด CXR ของ mitral stenosis แสดง LA โต มุม carina กว้าง double contour LAA โป่ง และ Kerley B lines",
                   ell(210, 160, 196, 134, "lru"),
                   path(heart, "sk"), ell(214, 178, 50, 30, "lms w2 da"),
                   line(203, 10, 203, 84, "lmu w5"), line(203, 84, 160, 124, "lmu w5"), line(203, 84, 250, 120, "lmu w5"),
                   path("M188 98 Q203 110 218 98", "lbad w2"),
                   t(14, 64, "มุม carina กว้าง", "xs b tbad"), line(100, 66, 186, 100, "lmu"),
                   t(14, 150, "double contour", "xs b tms"), t(14, 164, "(ขอบ LA)", "xs tms"), line(70, 160, 166, 176, "lmu"),
                   *[line(30, 214 + 8 * j, 50, 214 + 8 * j, "lmu w2") for j in range(4)],
                   t(14, 260, "Kerley B lines", "xs b twa"), t(14, 274, "(ปอดคั่งน้ำ)", "xs twa"),
                   t(410, 84, "aortic knob", "xs end mu"), line(352, 86, 284, 100, "lmu"),
                   t(410, 118, "PA โต (ถ้ามี PH)", "xs end b"), line(330, 120, 292, 128, "lmu"),
                   t(410, 150, "LAA โป่ง → ขอบซ้ายตรง", "xs end b tms"), line(300, 152, 292, 154, "lmu"),
                   t(410, 220, "LV ไม่โต", "xs end b"), t(410, 234, "(MS ล้วน)", "xs end mu"), line(362, 222, 316, 218, "lmu"),
                   t(214, 182, "LA", "sm b mid tms")))


def vhd_pmbc():
    out = []
    for k, (title, rx, ry, lab, sub) in enumerate((("ปกติ", 32, 15, "เปิดกว้าง", "MVA 4–6 ซม.²"),
                                                    ("Rheumatic MS", 12, 5, "commissure เชื่อมติด", "MVA ≤ 1.5 ซม.² (fish-mouth)"),
                                                    ("หลัง PMBC", 24, 10, "แยกตรงรอยเชื่อม", "MVA เพิ่มราว 2 เท่า"))):
        cx = 70 + 140 * k
        out += [t(cx, 18, title, "sm b mid"), circ(cx, 80, 46, "sk"), ell(cx, 80, rx, ry, "bad")]
        if k == 1:
            out += [line(cx - 12, 80, cx - 44, 80, "lmu w5"), line(cx + 12, 80, cx + 44, 80, "lmu w5")]
        if k == 2:
            out += [line(cx - 24, 80, cx - 44, 80, "lmu w3"), line(cx + 24, 80, cx + 44, 80, "lmu w3")]
        out += [t(cx, 146, lab, "xs mid b"), t(cx, 162, sub, "xs mid i2")]
    out += [ar(258, 80, 292, 80, "lok w2", "ah-ok", "บอลลูน", lc="xs b mid tok", dy=-8),
            line(140, 30, 140, 168, "lru da"),
            t(210, 186, "สายสวน: หลอดเลือดดำ → RA → เจาะผนังกั้น atrium → LA → ลิ้น mitral", "xs mid i2"),
            box(8, 200, 132, 66, "ok", "ลิ้นยืดหยุ่น หินปูนน้อย\n→ แยกตรงรอยเชื่อม\nไม่ฉีกตัวลิ้น", fs=10.5),
            box(144, 200, 132, 66, "bad", "ลิ่มเลือดใน LA\n→ สายผ่าน LA ดันลิ่มหลุด\n→ stroke", fs=10.5),
            box(280, 200, 132, 66, "ms", "MR มากอยู่แล้ว\n→ แยกแล้วรั่วมากขึ้น", fs=10.5)]
    return fig("PMBC — บอลลูนแยกรอยเชื่อมของลิ้น",
               "ไข้รูมาติกทำให้ขอบลิ้นสองแผ่น **เชื่อมกันที่มุม (commissure)** รูเหลือเป็นช่องแคบรูปปากปลา · บอลลูนที่สอดผ่านผนังกั้น atrium เข้าไปพองกลางรู จะฉีก **ตรงรอยเชื่อมเดิม** ทำให้ MVA กว้างขึ้นราวเท่าตัว · เงื่อนไขทั้งสามข้อในสไลด์มาจากกลไกนี้: ลิ้นต้องยืดหยุ่นพอจะแยกตรงรอยเชื่อม ไม่มีลิ่มเลือดใน LA ที่สายจะผ่าน และ MR ต้องไม่มากเพราะการแยกมักเพิ่มการรั่ว",
               svg(420, 276, "ลิ้น mitral ปกติ ลิ้นตีบจากรูมาติกที่ commissure เชื่อมกัน และหลังขยายด้วยบอลลูน พร้อมเงื่อนไขการทำ", *out))


# ---------- คาบ 05 ----------
def vhd_mr_types():
    out = []
    for k in range(2):
        cx = 105 + 210 * k
        out.append(path("M%d 60 C%d 22 %d 22 %d 60" % (cx - 44, cx - 60, cx + 60, cx + 44), "ln"))
        out.append(t(cx + 24, 38, "LA", "sm b mid twa"))
        if k == 0:
            out += [path("M%d 60 C%d 110 %d 176 %d 182 C%d 176 %d 110 %d 60" % (cx - 44, cx - 64, cx - 34, cx, cx + 34, cx + 64, cx + 44), "ln w2"),
                    ell(cx - 24, 154, 7, 13, "sk"), ell(cx + 24, 154, 7, 13, "sk"),
                    line(cx - 24, 142, cx - 16, 70, "lmu"), line(cx - 24, 142, cx - 2, 74, "lmu"),
                    line(cx + 24, 142, cx + 34, 64, "lmu"), line(cx + 24, 142, cx + 16, 116, "lmu"), t(cx + 20, 112, "✕", "xs b tbad"),
                    line(cx - 44, 60, cx + 2, 76, "ln w3"), path("M%d 60 Q%d 40 %d 46" % (cx + 44, cx + 30, cx + 12), "lms w3"),
                    line(cx + 2, 70, cx - 22, 28, "lbad w3", "ah-bad"), t(cx, 132, "LV", "sm b mid")]
        else:
            out += [path("M%d 60 C%d 110 %d 206 %d 210 C%d 206 %d 110 %d 60" % (cx - 44, cx - 96, cx - 66, cx, cx + 66, cx + 96, cx + 44), "ln w2"),
                    ell(cx - 48, 176, 7, 13, "sk"), ell(cx + 48, 176, 7, 13, "sk"),
                    line(cx - 48, 164, cx - 8, 94, "lmu"), line(cx - 48, 164, cx - 26, 78, "lmu"),
                    line(cx + 48, 164, cx + 8, 94, "lmu"), line(cx + 48, 164, cx + 26, 78, "lmu"),
                    line(cx - 44, 60, cx - 6, 94, "ln w3"), line(cx + 44, 60, cx + 6, 94, "ln w3"),
                    line(cx, 92, cx, 30, "lbad w3", "ah-bad"), t(cx, 150, "LV โต", "sm b mid")]
    out += [t(105, 16, "Primary — ตัวลิ้นเสีย", "sm b mid"), t(315, 16, "Secondary — ห้องหัวใจโต", "sm b mid"),
            line(210, 8, 210, 270, "lru da"),
            t(105, 232, "ลิ้นพลิกเข้า LA · chordae ขาด", "xs mid"), t(105, 248, "jet พุ่งเฉียงหนีลิ้นที่เสีย", "xs mid"),
            t(105, 268, "→ ซ่อมลิ้น", "sm mid b tok"),
            t(315, 232, "LV โต ดึง papillary ออกห่าง", "xs mid"), t(315, 248, "ลิ้นถูกรั้งลง ปิดไม่ถึงกัน", "xs mid"),
            t(315, 268, "→ รักษาหัวใจก่อน", "sm mid b tok")]
    return fig("Primary กับ secondary MR — ปัญหาอยู่คนละที่",
               "**Primary MR** ตัวลิ้นหรือ chordae เสีย (MVP, chordae ขาด, IE, RHD) ลิ้นพลิกขึ้นไปใน LA เลือดพุ่งเฉียงออกไปทางตรงข้ามกับลิ้นที่เสีย → แก้ที่ลิ้น · **Secondary MR** ลิ้นปกติ แต่ LV ที่โตดึง papillary muscle ออกห่าง chordae จึงรั้งลิ้นลงไปในโพรง (tethering) ขอบลิ้นแตะกันไม่ถึง → ต้องรักษาให้ LV เล็กลงก่อน (GDMT, CRT, revascularization)",
               svg(420, 280, "เปรียบเทียบ primary MR ที่ลิ้นพลิกและ chordae ขาด กับ secondary MR ที่ LV โตรั้งลิ้นจนปิดไม่สนิท", *out))


def vhd_mr_acute():
    out = []
    data = [("Acute MR", 24, [(0, 15), (0.1, 14), (0.2, 22), (0.35, 34), (0.45, 50), (0.55, 26), (0.7, 16), (1, 15)],
             "bad", "ความดันพุ่ง → ปอดบวมน้ำ ช็อก\nเสียงฟู่สั้นและเบา\n(LA ไล่ความดันทัน LV เร็ว)"),
            ("Chronic MR", 44, [(0, 10), (0.2, 11), (0.45, 19), (0.55, 13), (0.7, 10), (1, 10)],
             "ms", "LA ยืดรับ ความดันไม่สูง\nไม่มีอาการนาน\nLV ขยาย → เสื่อมเงียบ ๆ")]
    for k, (title, r, pts, c, txt) in enumerate(data):
        x0 = 210 * k
        cx = x0 + 105
        X = lambda tt, x0=x0: x0 + 24 + tt * 166
        Y = lambda p: 222 - p * 1.4
        out += [t(cx, 18, title, "sm b mid"), circ(cx, 72, r, "wa"), t(cx, 76, "LA", "sm b mid twa"),
                line(cx + r * 0.5 + 10, 130, cx + r * 0.4, 72 + r * 0.6, "lbad w3", "ah-bad"),
                t(cx + r + 6, 104, "เลือดรั่ว\njาก LV".replace("j", "จ"), "xs tbad"),
                t(x0 + 24, 152, "ความดัน LA", "xs mu"),
                line(X(0), Y(0), X(1), Y(0), "lmu"), line(X(0), Y(12), X(1), Y(12), "lru da"),
                _plot(pts, X, Y, "lwa w3"),
                box(x0 + 10, 236, 190, 66, c, txt, fs=11)]
    out += [t(24 + 0.45 * 166 + 8, 222 - 50 * 1.4 + 4, "v wave สูง", "xs b tbad"), line(210, 10, 210, 304, "lru da")]
    return fig("Acute กับ chronic MR — ขนาดของ LA เปลี่ยนทุกอย่าง",
               "เลือดที่รั่วปริมาณเท่ากัน ถ้าเข้า **LA ขนาดปกติที่ยังยืดไม่ได้ (acute)** ความดันพุ่งเป็น v wave สูง ส่งย้อนเข้าปอดทันที และเพราะความดัน LA ไล่ทัน LV เร็ว เสียงฟู่จึงสั้นและเบา · ถ้าค่อย ๆ รั่ว **(chronic)** LA และ LV มีเวลาขยาย ความดันแทบไม่ขึ้น ผู้ป่วยจึงไม่มีอาการนาน แต่ LV ทำงานหนักจนเสื่อมโดยไม่รู้ตัว",
               svg(420, 312, "เปรียบเทียบ acute MR ที่ LA เล็ก ความดันพุ่งเป็น v wave สูง กับ chronic MR ที่ LA ขยายรับได้ ความดันไม่สูง", *out))


def vhd_mvp():
    out = [t(110, 18, "S1", "xs mid b"), t(300, 18, "S2", "xs mid b")]
    rows = [("นอนราบ", 206, "click กลาง"), ("ยืน · Valsalva", 156, "เร็วขึ้น ยาวขึ้น"), ("นั่งยอง", 254, "ช้าลง สั้นลง")]
    for k, (lab, cx, note) in enumerate(rows):
        yb = 48 + 58 * k
        out += [t(10, yb + 4, lab, "sm b"), line(104, yb, 306, yb, "lru"), _snd(110, yb, 14), _snd(300, yb, 12),
                rect(cx - 2, yb - 18, 4, 36, "acf", 1), t(cx, yb - 22, "C", "xs mid b tac"),
                *_env(cx + 8, 292, lambda u: 3 + 9 * u, yb, "lms w2", 3),
                t(314, yb + 4, note, "xs i2")]
    out += [t(10, 214, "LV เล็กลง → ลิ้นที่หย่อนยานเกินขนาดโพรงพลิกเข้า LA เร็วขึ้น", "xs i2"),
            t(10, 232, "LV ใหญ่ขึ้น → chordae ตึงกว่า ลิ้นพลิกช้าลง", "xs i2")]
    return fig("MVP — click เลื่อนตามขนาดของ LV",
               "ลิ้น myxomatous ยืดยาวเกินขนาดของโพรง เมื่อ LV บีบจนเล็กถึงจุดหนึ่ง ลิ้นจะพลิกเข้า LA ทันที chordae ที่ตึงขึ้นทันทีให้เสียง **click** แล้วเลือดเริ่มรั่ว (late systolic murmur) · อะไรที่ทำให้ **LV เล็กลง** (ยืน, Valsalva) ทำให้ถึงจุดนั้นเร็วขึ้น click จึงเลื่อนมาใกล้ S1 และ murmur ยาวขึ้น ส่วนการนั่งยองทำตรงข้าม",
               svg(420, 242, "ตำแหน่ง click และเสียงฟู่ของ mitral valve prolapse เมื่อนอนราบ ยืนหรือ Valsalva และนั่งยอง", *out))


# ---------- คาบ 06 ----------
def vhd_mr_ef():
    S = 1.45
    x0 = 92
    out = [t(10, 18, "ปริมาตรเลือดใน LV ต่อจังหวะ (มล.)", "sm b")]
    rows = [("ปกติ", [("sk", 50, "ESV 50"), ("ok", 70, "ไปข้างหน้า 70")], "EF = 70/120 ≈ 58%"),
            ("MR รุนแรง", [("sk", 80, "ESV 80"), ("ok", 60, "ไปหน้า 60"), ("bad", 60, "รั่วกลับ LA 60")], "EF = 120/200 = 60% ดูปกติ!")]
    for k, (lab, segs, ef) in enumerate(rows):
        y = 36 + 92 * k
        out.append(t(10, y + 22, lab, "sm b"))
        x = x0
        for c, v, s in segs:
            out += [rect(x, y, v * S, 34, c, 0), t(x + v * S / 2, y + 21, s, "xs mid b")]
            x += v * S
        out += [t(x0, y + 54, "EDV %d" % sum(v for _, v, _ in segs), "xs mu"),
                t(410, y + 54, ef, "xs end b" + (" tbad" if k else ""))]
    out += [box(10, 228, 400, 60, "ms", "LV บีบเลือดส่วนหนึ่งเข้า LA ที่ความดันต่ำ (afterload ต่ำ)\n→ EF สูงเกินความจริง · EF 60% ใน MR = LV เริ่มเสื่อมแล้ว", fs=11.5),
            t(10, 308, "RVol ≥ 60 มล. · RF = 60/120 ≥ 50% → severe MR", "xs i2")]
    return fig("ทำไม LVEF ใน MR สูงเกินจริง",
               "EF คิดจาก **เลือดทั้งหมดที่ LV บีบออก** ไม่ว่าจะไปทาง aorta หรือรั่วกลับเข้า LA · ใน MR รุนแรง LV ขยาย (EDV ใหญ่) และบีบออกได้ง่ายเพราะมีทางออกที่ความดันต่ำ EF จึงดูปกติทั้งที่เลือดไปเลี้ยงร่างกายจริงลดลง · เมื่อผ่าตัดปิดทางรั่ว LV ต้องบีบเข้า aorta อย่างเดียว EF จะลดลงทันที — จึงต้องผ่าตัดตั้งแต่ LVEF ≤ 60% หรือ LVESD ≥ 40 มม. ก่อน LV เสียถาวร (ตัวเลขในภาพเป็นตัวอย่าง)",
               svg(420, 316, "แท่งปริมาตรเลือด LV เทียบคนปกติกับ MR รุนแรง แสดงว่า EF ใน MR ดูปกติทั้งที่เลือดไปข้างหน้าน้อยลง", *out))


# ---------- คาบ 07 ----------
def vhd_as_triad():
    cols = [("bad", "Angina", "กล้ามเนื้อหนา\nใช้ O2 มากขึ้น\n+ ผนังตึงบีบหลอด\nเลือดใต้เยื่อบุใน"),
            ("ms", "Syncope เมื่อออกแรง", "หลอดเลือด\nกล้ามเนื้อขยาย\nแต่ CO เพิ่มไม่ได้\n→ BP ตก สมองขาดเลือด"),
            ("wa", "Heart failure", "LV แข็ง LVEDP ↑\n→ ปอดคั่ง\nนานไป LV บีบไม่ไหว\n→ EF ลด")]
    out = [box(60, 8, 300, 34, "bad", "ลิ้น aortic ตีบ → LV ต้องสร้างความดันสูงมาก", fs=11.5),
           line(210, 42, 210, 56, "ln", "ah"),
           box(60, 58, 300, 34, "ms", "LV หนาตัวแบบ concentric (pressure overload)", fs=11.5)]
    for k, (c, title, txt) in enumerate(cols):
        x = 8 + 136 * k
        out += [line(210, 92, x + 66, 114, "ln", "ah"), box(x, 116, 132, 30, c, title, "b", fs=11.5),
                box(x, 152, 132, 86, "bx", txt, fs=10.5)]
    out += [t(210, 266, "อายุเฉลี่ยหลังเริ่มอาการ ถ้าไม่เปลี่ยนลิ้น (ข้อมูลคลาสสิก)", "xs mid i2"),
            t(210, 286, "angina ~5 ปี · syncope ~3 ปี · heart failure ~2 ปี", "sm mid b tbad")]
    return fig("AS — อาการสามอย่างมาจาก LV ที่หนาและ output ที่ตายตัว",
               "รูลิ้นที่แคบบังคับให้ LV สร้างความดันสูงจนผนังหนา · **angina** เพราะกล้ามเนื้อมากขึ้นต้องใช้ O2 มากขึ้น ขณะที่ความดันในผนังบีบหลอดเลือดชั้นใน · **syncope** เพราะเวลาออกแรงหลอดเลือดกล้ามเนื้อขยาย แต่ cardiac output ถูกล็อกไว้ด้วยรูลิ้น ความดันจึงตก · **heart failure** จาก LV ที่แข็งแล้วสุดท้ายบีบไม่ไหว · เมื่อมีอาการแล้วอัตรารอดลดลงเร็ว จึงเป็นข้อบ่งชี้ให้เปลี่ยนลิ้น",
               svg(420, 296, "กลไกของ angina syncope และ heart failure ใน aortic stenosis และอายุเฉลี่ยหลังเริ่มอาการ", *out))


def vhd_lflg():
    X = lambda f: 60 + f * 3.4
    Y = lambda g: 240 - g * 3.4
    k = 46 / 75 ** 2
    true = [(f, k * f * f) for f in range(0, 91, 3)]
    g45 = k * 45 * 45
    pseudo = [(f, g45 + (f - 45) * 0.36) for f in range(45, 91, 3)]
    out = [line(X(0), Y(0), X(100), Y(0), "lmu"), line(X(0), Y(0), X(0), Y(60), "lmu"),
           line(X(0), Y(40), X(100), Y(40), "lbad da"), t(X(0) + 4, Y(40) - 5, "mean gradient 40 mmHg", "xs b tbad"),
           _plot(true, X, Y, "lbad w3"), _plot(pseudo, X, Y, "lms w3"),
           circ(X(45), Y(g45), 6, "inkf"), t(X(45) + 2, Y(g45) + 22, "พัก: flow ต่ำ", "xs b mid"),
           t(X(45) + 2, Y(g45) + 36, "gradient < 40 · AVA ≤ 1.0", "xs mid i2"),
           circ(X(75), Y(46), 6, "badf"), t(X(75) - 10, Y(46) - 4, "AS จริง", "xs b end tbad"),
           circ(X(75), Y(g45 + 30 * 0.36), 6, "msf"), t(X(75) + 10, Y(g45 + 30 * 0.36) + 16, "pseudo-severe", "xs b tms"),
           t(X(60), Y(g45) + 6, "dobutamine →", "xs b mid i2"),
           t(16, 24, "gradient", "xs mu"), t(X(100), 258, "flow ผ่านลิ้น (stroke volume)", "xs end mu"),
           box(10, 272, 196, 58, "bad", "AVA คงที่ gradient ขึ้นถึง ≥ 40\n→ AS รุนแรงจริง\n→ เปลี่ยนลิ้น", fs=11),
           box(214, 272, 196, 58, "ms", "ลิ้นเปิดกว้างขึ้น AVA > 1.0\ngradient ไม่ถึง 40\n→ ปัญหาหลักที่กล้ามเนื้อ", fs=11),
           t(10, 350, "ถ้า SV ไม่เพิ่ม (ไม่มี contractile reserve) → ใช้ CT calcium score แทน", "xs i2")]
    return fig("Low-flow low-gradient AS — gradient ขึ้นกับ flow",
               "gradient ไม่ได้ขึ้นกับรูลิ้นอย่างเดียว แต่ **ขึ้นกับปริมาณเลือดที่ไหลผ่าน** (โดยประมาณแปรตาม flow²) · LV ที่อ่อนแรงดันเลือดได้น้อย gradient จึงต่ำแม้ลิ้นตีบมาก และลิ้นที่ตีบไม่มากก็อาจเปิดไม่เต็มที่จนคำนวณ AVA ได้เล็ก · dobutamine เพิ่มแรงบีบ: ถ้า **AVA คงที่และ gradient พุ่ง** = ตีบจริง · ถ้า **ลิ้นเปิดกว้างขึ้นและ gradient ไม่ถึง** = pseudo-severe (ตัวเลขในกราฟเป็นตัวอย่าง)",
               svg(420, 360, "กราฟ gradient เทียบ flow ใน low-flow low-gradient AS เมื่อให้ dobutamine แยก AS รุนแรงจริงกับ pseudo-severe", *out))


# ---------- คาบ 08 ----------
def vhd_ar_pulse():
    beats = [("ปกติ", "120/80", "", [(0, 80), (0.06, 100), (0.12, 118), (0.18, 120), (0.3, 108), (0.36, 98), (0.38, 102), (0.5, 96), (0.75, 88), (1, 80)], "ln w2"),
             ("AS", "~110/90", "ขึ้นช้า ยอดต่ำ\nPP แคบ", [(0, 88), (0.1, 92), (0.2, 100), (0.3, 106), (0.38, 108), (0.44, 102), (0.5, 99), (0.75, 93), (1, 88)], "lms w3"),
             ("AR", "~160/50", "พุ่งแรง ตกเร็ว\nPP กว้าง", [(0, 50), (0.04, 110), (0.08, 155), (0.12, 160), (0.2, 140), (0.3, 110), (0.36, 96), (0.5, 76), (0.75, 60), (1, 50)], "lbad w3")]
    out = []
    for k, (name, bp, sub, pts, c) in enumerate(beats):
        y0 = 10 + 92 * k
        X = lambda tt: 130 + tt * 136
        Y = lambda p, y0=y0: y0 + 76 - (p - 40) * 0.55
        two = pts + [(1 + a, b) for a, b in pts[1:]]
        out += [t(10, y0 + 30, name, "lg b"), t(10, y0 + 48, bp, "sm"), t(10, y0 + 64, sub, "xs i2", lh=1.3),
                line(X(0), Y(120), X(2), Y(120), "lru da"), line(X(0), Y(80), X(2), Y(80), "lru da"),
                t(X(0) - 4, Y(120) + 4, "120", "xs end mu"), t(X(0) - 4, Y(80) + 4, "80", "xs end mu"),
                _plot(two, X, Y, c)]
    out += [t(10, 296, "AR: stroke volume รวมเลือดที่รั่วกลับ → ดันความดัน systolic สูง", "xs i2"),
            t(10, 314, "diastole เลือดไหลย้อนกลับเข้า LV → ความดัน diastolic ตกต่ำ", "xs i2")]
    return fig("ชีพจร AS กับ AR — ตรงข้ามกัน",
               "**AS** เลือดออกผ่านรูแคบได้ช้าและน้อย ชีพจรจึงขึ้นช้า ยอดต่ำ (parvus et tardus) pulse pressure แคบ · **AR** LV ต้องบีบเลือดปริมาณมาก (เลือดปกติ + เลือดที่รั่วกลับมา) ความดันจึงพุ่งสูง แล้วใน diastole เลือดไหลย้อนกลับเข้า LV ความดันจึงตกฮวบ — ชีพจรกระแทกแล้วยุบ (water-hammer) และอาการแสดงตามชื่อต่าง ๆ ล้วนมาจาก pulse pressure ที่กว้างนี้",
               svg(420, 322, "รูปคลื่นความดันหลอดเลือดแดงของคนปกติ AS และ AR แสดง pulse pressure แคบใน AS และกว้างใน AR", *out))


def vhd_ar_lv():
    return fig("Acute กับ chronic AR — LV มีเวลาปรับตัวหรือไม่",
               "ใน **chronic AR** LV รับทั้งปริมาตรเกิน (เลือดรั่วกลับ) และความดันเกิน (บีบเลือดปริมาณมากเข้า aorta) จึงทั้งขยายและหนา โพรงใหญ่ยืดหยุ่น รับเลือดได้มากโดยความดันไม่ขึ้น ผู้ป่วยไม่มีอาการนานหลายปี — ต้องผ่าตัดเมื่อ LV เริ่มเสื่อม · ใน **acute AR** (IE, aortic dissection) LV ขนาดเดิมยืดไม่ทัน ความดันปลาย diastole พุ่ง → ปอดบวมน้ำและช็อก และ pulse pressure ไม่กว้างเพราะความดัน aorta กับ LV เท่ากันเร็ว",
               svg(420, 296, "เปรียบเทียบ LV ใน acute AR ที่ขนาดเดิมความดันพุ่ง กับ chronic AR ที่ LV ขยายและหนา",
                   t(105, 18, "Acute AR", "sm b mid"), t(315, 18, "Chronic AR", "sm b mid"),
                   ell(105, 100, 40, 56, "bad"), ell(105, 102, 28, 42, "bx"), t(105, 106, "LV", "sm b mid"),
                   line(105, 26, 105, 64, "lbad w3", "ah-bad"),
                   ell(315, 104, 74, 80, "bad"), ell(315, 106, 58, 64, "bx"), t(315, 110, "LV โต", "sm b mid"),
                   line(315, 24, 315, 58, "lbad w3", "ah-bad"),
                   t(105, 186, "LV ขนาดเดิม ยืดไม่ทัน", "xs mid"), t(105, 202, "LVEDP พุ่ง → ปอดบวมน้ำ ช็อก", "xs mid b tbad"),
                   t(105, 218, "PP ไม่กว้าง · murmur สั้น", "xs mid"),
                   box(20, 232, 170, 36, "bad", "→ ผ่าตัดด่วน · ห้ามใส่ IABP", fs=11),
                   t(315, 202, "ขยาย + หนา รับเลือดได้มาก", "xs mid"), t(315, 218, "ไม่มีอาการนาน · apex ย้าย · PP กว้าง", "xs mid"),
                   box(230, 232, 170, 36, "ms", "→ ผ่าตัดก่อน LV เสื่อม", fs=11),
                   line(210, 10, 210, 276, "lru da"),
                   t(210, 290, "IABP พองตอน diastole → ดันเลือดย้อนเข้า LV มากขึ้น", "xs mid i2")))


# ---------- คาบ 09 ----------
def vhd_tr():
    X = lambda tt: 80 + tt * 320
    nrm = [(0, 4), (0.08, 10), (0.14, 5), (0.18, 7), (0.35, 1), (0.55, 8), (0.68, 2), (0.9, 4), (1, 4)]
    trp = [(0, 6), (0.08, 10), (0.14, 9), (0.2, 14), (0.45, 22), (0.55, 24), (0.66, 4), (0.9, 6), (1, 6)]
    Yn = lambda v: 80 - v * 2.6
    Yt = lambda v: 170 - v * 2.6
    out = [t(10, 18, "JVP", "sm b"),
           t(10, 66, "ปกติ", "sm b"), line(X(0), Yn(0), X(1), Yn(0), "lru"), _plot(nrm, X, Yn, "lwa w3"),
           t(X(0.08), Yn(10) - 6, "a", "xs b mid"), t(X(0.18), Yn(7) - 6, "c", "xs b mid"), t(X(0.35), Yn(1) + 14, "x", "xs b mid"),
           t(X(0.55), Yn(8) - 6, "v", "xs b mid"), t(X(0.68), Yn(2) + 14, "y", "xs b mid"),
           t(10, 156, "TR รุนแรง", "sm b"), line(X(0), Yt(0), X(1), Yt(0), "lru"), _plot(trp, X, Yt, "lbad w3"),
           t(X(0.5), Yt(24) - 8, "cv wave ใหญ่ · x หาย", "xs b mid tbad"), t(X(0.66) + 6, Yt(4) + 14, "y ลึกชัน", "xs b tbad")]
    cols = [(10, "Carvallo's sign", [("ac", "หายใจเข้า\nความดันในอกเป็นลบ"), ("wa", "เลือดดำเข้า RA/RV ↑"),
                                     ("bx", "RV บีบเลือดมากขึ้น\nรั่วผ่าน tricuspid มากขึ้น"), ("ms", "murmur ที่ LLSB ดังขึ้น")]),
            (214, "Secondary TR", [("sk", "หัวใจซ้าย/ปอด → PH"), ("bx", "RV ขยาย"),
                                   ("bx", "วงแหวน tricuspid ถ่าง\nลิ้นปิดไม่ถึงกัน"), ("bad", "JVP v ใหญ่ ตับเต้น\nท้องมาน ขาบวม")])]
    for x, title, items in cols:
        out.append(t(x + 98, 210, title, "sm b mid"))
        y = 220
        for k, (c, s) in enumerate(items):
            h = 44 if "\n" in s else 32
            out.append(box(x, y, 196, h, c, s, fs=11))
            if k < 3:
                out.append(line(x + 98, y + h, x + 98, y + h + 10, "ln", "ah"))
            y += h + 12
    return fig("TR — JVP และเสียงที่ดังขึ้นเมื่อหายใจเข้า",
               "ปกติ JVP มีคลื่น a (atrium บีบ) แล้วตกเป็น x descent ช่วง systole · ใน TR เลือดจาก RV พุ่งย้อนเข้า RA ตลอด systole จึง **ถม x descent จนกลายเป็นคลื่น cv ใหญ่** ส่งไปถึงคอและตับ · การหายใจเข้าดึงเลือดดำเข้าหัวใจขวามากขึ้น RV บีบเลือดมากขึ้นจึงรั่วมากขึ้น เสียงจึงดังขึ้น (Carvallo) — ใช้แยกจาก MR ที่ไม่เปลี่ยนตามการหายใจ · TR ส่วนใหญ่เป็นแบบ secondary จากความดันในปอดสูง",
               svg(420, 420, "รูปคลื่น JVP ปกติเทียบกับ TR และกลไกของ Carvallo's sign กับ secondary TR", *out))


# ---------- คาบ 10 ----------
def vhd_mimicry():
    out = [box(60, 8, 300, 34, "sk", "GAS คออักเสบ ที่รักษาไม่พอ", fs=12), line(210, 42, 210, 54, "ln", "ah"),
           box(60, 56, 300, 34, "ac", "แอนติบอดี + T cell ต่อ M protein", fs=12), line(210, 90, 210, 102, "ln", "ah"),
           box(60, 104, 300, 34, "ms", "จับข้ามกับโปรตีนของร่างกาย (molecular mimicry)", fs=11.5),
           line(24, 150, 24, 330, "ln"), line(210, 138, 210, 150, "ln"), line(24, 150, 210, 150, "ln")]
    rows = [("bad", "หัวใจ — myosin · laminin ของลิ้น\n→ carditis / valvulitis → แผลเป็นถาวร (RHD)"),
            ("ms", "ข้อ — synovium (immune complex)\n→ arthritis ข้อใหญ่ ย้ายที่ หายสนิท"),
            ("ac", "สมอง — เซลล์ประสาทใน basal ganglia\n→ Sydenham's chorea (เกิดช้า หลายเดือน)"),
            ("sk", "ผิวหนัง / เนื้อเยื่อเกี่ยวพัน\n→ erythema marginatum · subcutaneous nodule")]
    for k, (c, s) in enumerate(rows):
        y = 160 + 50 * k
        out += [line(24, y + 21, 38, y + 21, "ln", "ah"), box(40, y, 370, 42, c, s, fs=11)]
    X = lambda w: 40 + w * 30
    out += [line(X(0), 384, X(12), 384, "lmu", "ah-mu"),
            circ(X(0), 384, 5, "inkf"), t(X(0), 406, "เจ็บคอ", "xs mid b"),
            rect(X(2), 377, X(4) - X(2), 14, "bad", 3), t(X(3), 406, "2–4 สัปดาห์: ไข้ ข้อ หัวใจ", "xs mid b"),
            rect(X(6), 377, X(11) - X(6), 14, "ac", 3), t(X(8.5), 406, "หลายเดือน: chorea", "xs mid b"),
            t(X(12), 372, "เวลา (สัปดาห์)", "xs end mu")]
    return fig("ไข้รูมาติก — ภูมิคุ้มกันต่อเชื้อหันมาทำร้ายตัวเอง",
               "ตัวเชื้อ GAS ไม่ได้ไปที่หัวใจ — **แอนติบอดีและ T cell ที่สร้างขึ้นต่อ M protein ไปจับโปรตีนของร่างกายที่หน้าตาคล้ายกัน** จึงต้องรอ 2–4 สัปดาห์ให้ภูมิคุ้มกันสร้างขึ้นก่อน · ข้ออักเสบหายสนิท แต่ลิ้นหัวใจกลายเป็นแผลเป็น · chorea เกิดช้ากว่าอาการอื่นหลายเดือน หลักฐานการติดเชื้ออาจหายไปแล้ว จึงเป็นข้อยกเว้นที่ไม่ต้องมีหลักฐาน GAS",
               svg(420, 414, "กลไก molecular mimicry ของไข้รูมาติก จาก GAS คออักเสบสู่หัวใจ ข้อ สมอง และผิวหนัง พร้อมลำดับเวลา", *out))


def vhd_rhd_valve():
    out = []
    for k, (title, a, b) in enumerate((("ระยะเฉียบพลัน", "ลิ้นบวม มีตุ่มที่ขอบปิด", "→ ปิดไม่สนิท = MR"),
                                        ("หายเป็นแผลเป็น", "ลิ้นหนา chordae สั้นหนา", "เป็นซ้ำแต่ละครั้ง → หนาขึ้น"),
                                        ("ปลายทาง: MS", "commissure เชื่อมติด", "→ รู fish-mouth"))):
        cx = 70 + 140 * k
        out += [t(cx, 18, title, "sm b mid"), t(cx, 168, a, "xs mid"), t(cx, 184, b, "xs mid b")]
        if k == 0:
            out += [line(cx - 44, 50, cx - 6, 92, "lms w5"), line(cx + 44, 50, cx + 6, 92, "lms w5"),
                    *[circ(x, y, 3, "acf") for x, y in ((cx - 12, 84), (cx - 20, 76), (cx + 12, 84), (cx + 20, 76))],
                    line(cx - 6, 92, cx - 20, 136, "lmu"), line(cx + 6, 92, cx + 20, 136, "lmu"),
                    ell(cx - 22, 142, 7, 9, "sk"), ell(cx + 22, 142, 7, 9, "sk"),
                    line(cx, 112, cx, 40, "lbad w2", "ah-bad")]
        elif k == 1:
            out += [line(cx - 44, 50, cx - 10, 84, "lmu w5"), line(cx + 44, 50, cx + 10, 84, "lmu w5"),
                    line(cx - 10, 84, cx - 18, 112, "lmu w3"), line(cx + 10, 84, cx + 18, 112, "lmu w3"),
                    ell(cx - 20, 120, 8, 10, "sk"), ell(cx + 20, 120, 8, 10, "sk")]
        else:
            out += [circ(cx, 90, 44, "sk"), ell(cx, 90, 13, 5, "bad"),
                    line(cx - 13, 90, cx - 42, 90, "lmu w5"), line(cx + 13, 90, cx + 42, 90, "lmu w5")]
    out += [ar(118, 90, 132, 90, "ln", "ah"), ar(258, 90, 272, 90, "ln", "ah"),
            box(10, 200, 400, 40, "ok", "ป้องกันการเป็นซ้ำ (secondary prophylaxis) = หยุดไม่ให้แผลเป็นสะสมเพิ่ม", fs=11.5)]
    return fig("จาก valvulitis สู่ rheumatic MS",
               "ช่วงเฉียบพลันลิ้น mitral บวมและมีตุ่มเล็ก ๆ (verrucae) ตามแนวขอบปิด ลิ้นจึงปิดไม่สนิท — **MR** เป็นเสียงที่พบในระยะนี้ · เมื่อหายอักเสบจะซ่อมด้วยพังผืด ลิ้นหนา chordae สั้นและเชื่อมกัน ทุกครั้งที่เป็นซ้ำแผลเป็นจะเพิ่ม · หลายปีต่อมาขอบลิ้นเชื่อมกันที่ commissure จนเหลือรูแคบ กลายเป็น **MS** ซึ่งเป็นผลระยะยาวที่พบบ่อยที่สุดในไทย",
               svg(420, 250, "ลำดับการเปลี่ยนแปลงของลิ้น mitral ในไข้รูมาติก จากลิ้นบวมเป็น MR ไปสู่แผลเป็นและ MS", *out))


# ---------- คาบ 11 ----------
def vhd_bpg():
    X = lambda w: 60 + w * 28
    Y = lambda L: 140 - L * 88
    lam = math.log(1 / 0.15) / 4
    lv = lambda w: sum(math.exp(-lam * (w - ti)) for ti in (0, 4, 8) if w >= ti)
    pts = []
    for seg in ((0, 4), (4, 8), (8, 12)):
        for i in range(0, 41):
            w = seg[0] + i * 0.1
            if w >= seg[1]:
                w = seg[1] - 1e-6
            pts.append((X(w), Y(lv(w))))
    out = [t(10, 18, "ระดับ penicillin หลังฉีด BPG ทุก 4 สัปดาห์", "sm b"),
           line(X(0), Y(0), X(12), Y(0), "lmu"), poly(pts, "lok w3"),
           line(X(0), Y(0.15), X(12), Y(0.15), "lbad da"), t(X(12), Y(0.15) - 5, "ระดับที่กันเชื้อได้", "xs end b tbad")]
    out += [p for w in (0, 4, 8) for p in (line(X(w), Y(0) + 14, X(w), Y(0) + 3, "lac w2", "ah-ac"), t(X(w), Y(0) + 28, "ฉีด", "xs mid b tac"))]
    out += [p for w in (0, 2, 4, 6, 8, 10, 12) for p in (t(X(w) + (10 if w in (0, 4, 8) else 0), Y(0) + 14, str(w), "xs mid mu"),)]
    out.append(t(X(12), 190, "สัปดาห์", "xs end mu"))
    X2 = lambda yr: 60 + yr * 33
    Y2 = lambda d: 330 - d * 1.0
    none = [(0, 0), (0.5, 0), (0.5, 30), (2, 30), (2, 55), (4, 55), (4, 74), (7, 74), (7, 92), (10, 92)]
    prop = [(0, 0), (0.5, 0), (0.5, 30), (10, 30)]
    out += [t(10, 214, "ความเสียหายของลิ้นสะสม", "sm b"),
            line(X2(0), Y2(0), X2(10), Y2(0), "lmu"), line(X2(0), Y2(0), X2(0), Y2(100), "lmu"),
            _plot(none, X2, Y2, "lbad w3"), _plot(prop, X2, Y2, "lok w3"),
            *[circ(X2(a), Y2(b), 4, "badf") for a, b in ((2, 55), (4, 74), (7, 92))],
            t(X2(7) - 6, Y2(92) - 8, "ไม่ป้องกัน: เป็นซ้ำทีละครั้ง", "xs b end tbad"),
            t(X2(10), Y2(30) - 8, "ได้ BPG สม่ำเสมอ", "xs b end tok"),
            t(X2(0.5), Y2(30) + 16, "ARF ครั้งแรก", "xs i2"),
            t(X2(10), 348, "ปี", "xs end mu")]
    return fig("Secondary prophylaxis — กันการติดเชื้อซ้ำ = กันลิ้นพังเพิ่ม",
               "ผู้ที่เคยเป็นไข้รูมาติกแล้ว เมื่อติด GAS ที่คออีก ภูมิคุ้มกันที่เคยถูกกระตุ้นจะทำร้ายลิ้นซ้ำได้ง่าย **ความเสียหายสะสมเป็นขั้นบันได** · BPG ฉีดเข้ากล้ามค่อย ๆ ปล่อย penicillin ออกมาให้ระดับยาอยู่เหนือระดับที่กันเชื้อได้เกือบตลอดรอบ จึงต้องฉีดตรงเวลา — ช่วงท้ายรอบระดับยาเริ่มต่ำ เป็นเหตุที่บางแนวทางใช้ทุก 3 สัปดาห์ในรายเสี่ยงสูง (กราฟเป็นแผนภาพ ไม่ใช่ค่าจริง)",
               svg(420, 356, "ระดับ penicillin หลังฉีด BPG ทุกสี่สัปดาห์ และความเสียหายของลิ้นที่สะสมเมื่อไม่ได้ป้องกันเทียบกับได้ยาสม่ำเสมอ", *out))


# ---------- คาบ 12 ----------
def vhd_ie_path():
    chain = [("sk", "ลิ้นผิดปกติ (RHD · ลิ้นเทียม) → เลือดพุ่งแรง\nendothelium ถลอก"),
             ("sk", "เกล็ดเลือด + fibrin มาเกาะเป็นก้อน (ยังไม่มีเชื้อ)"),
             ("ms", "bacteremia ชั่วคราว (ฟัน · ยาฉีด · สายสวน)\n→ เชื้อเกาะก้อนเกล็ดเลือด"),
             ("bad", "Vegetation — เชื้อแบ่งตัวในก้อน fibrin\nเม็ดเลือดขาวเข้าไม่ถึง")]
    out = []
    y = 8
    for k, (c, s) in enumerate(chain):
        h = 42 if "\n" in s else 30
        out.append(box(40, y, 340, h, c, s, fs=11))
        if k < 3:
            out.append(line(210, y + h, 210, y + h + 10, "ln", "ah"))
        y += h + 12
    out += [line(210, y - 12, 210, y), line(24, y, 24, y + 188), line(24, y, 210, y)]
    rows = [("bad", "ทำลายลิ้น → รั่ว/ทะลุ → murmur ใหม่ HF\nฝีลามถึงระบบนำไฟฟ้า → AV block"),
            ("ms", "ก้อนหลุด (emboli) → stroke · ไต/ม้ามตาย\nJaneway · splinter · mycotic aneurysm"),
            ("ac", "Immune complex → Osler · Roth\nGN · rheumatoid factor บวก"),
            ("wa", "เชื้อในเลือดต่อเนื่อง → ไข้\nเพาะเชื้อขึ้นทุกขวด")]
    for k, (c, s) in enumerate(rows):
        yy = y + 10 + 52 * k
        out += [line(24, yy + 22, 38, yy + 22, "ln", "ah"), box(40, yy, 370, 44, c, s, fs=11)]
    return fig("Infective endocarditis — จากลิ้นที่ถลอกสู่อาการสี่กลุ่ม",
               "IE ต้องมีสองอย่างพร้อมกัน: **ผิวลิ้นที่เสีย** (กระแสเลือดพุ่งแรงจากลิ้นผิดปกติทำให้ endothelium ถลอก มีเกล็ดเลือดและ fibrin มาเกาะ) และ **เชื้อในเลือดชั่วคราว** ที่มาเกาะก้อนนั้น · อาการทั้งหมดจัดได้สี่กลุ่ม: ลิ้นถูกทำลาย · ก้อนหลุดไปอุด · immune complex · และเชื้อที่หลุดเข้าเลือดตลอดเวลา ซึ่งเป็นเหตุที่เพาะเชื้อหลายชุดจากต่างตำแหน่งขึ้นเชื้อเดียวกันทุกชุด",
               svg(420, 432, "กลไกการเกิด infective endocarditis และอาการสี่กลุ่ม การทำลายลิ้น emboli immune complex และเชื้อในเลือด", *out))


def vhd_ie_jet():
    out = []
    for k, (title, top, bot, jet_up, veg_dy, lab) in enumerate((("MR — ลิ้น mitral", "LA (ความดันต่ำ)", "LV (ความดันสูง)", True, -7, "ก้อนอยู่ด้าน LA"),
                                                                  ("AR — ลิ้น aortic", "Aorta (ความดันสูง)", "LV (ความดันต่ำ)", False, 8, "ก้อนอยู่ด้าน LV"))):
        cx = 105 + 210 * k
        out += [t(cx, 18, title, "sm b mid"), t(cx, 40, top, "xs mid i2"), t(cx, 196, bot, "xs mid i2"),
                line(cx - 70, 100, cx - 50, 100, "lmu w3"), line(cx + 50, 100, cx + 70, 100, "lmu w3"),
                line(cx - 50, 100, cx - 5, 118, "ln w3"), line(cx + 50, 100, cx + 5, 118, "ln w3"),
                ell(cx - 18, 113 + veg_dy, 9, 6, "badf"), ell(cx + 22, 111 + veg_dy, 7, 5, "badf"),
                t(cx, 222, lab, "xs mid b tbad")]
        out.append(line(cx, 178, cx, 56, "lbad w3", "ah-bad") if jet_up else line(cx, 56, cx, 178, "lbad w3", "ah-bad"))
    out += [line(210, 10, 210, 228, "lru da"),
            t(210, 248, "เชื้อเกาะด้านความดันต่ำ ปลายทางของ jet — ตรงที่ endothelium ถูกกระแทก", "xs mid i2")]
    return fig("Vegetation อยู่ด้านไหนของลิ้น",
               "เลือดที่พุ่งผ่านรูรั่วจากด้านความดันสูงไปด้านความดันต่ำ กระแทก endothelium ด้าน **ปลายทางของ jet** และเกิดแรงดูดที่ทำให้เกล็ดเลือดและเชื้อตกตะกอนตรงนั้น · vegetation ของ MR จึงอยู่ด้าน atrium ของลิ้น mitral ส่วนของ AR อยู่ด้าน ventricle ของลิ้น aortic · เป็นเหตุผลเดียวกับที่ลิ้นรั่วจาก RHD เสี่ยง IE มากกว่าลิ้นปกติ",
               svg(420, 258, "ตำแหน่ง vegetation อยู่ด้านความดันต่ำของลิ้น ด้าน LA ใน MR และด้าน LV ใน AR", *out))


# ---------- คาบ 13 ----------
def vhd_ie_why():
    bact = [(70 + 13 * (i % 8) + (6 if (i // 8) % 2 else 0), 56 + 12 * (i // 8)) for i in range(40)]
    bact = [(x, y) for x, y in bact if ((x - 120) / 74) ** 2 + ((y - 80) / 38) ** 2 < 0.8]
    return fig("ทำไมต้องให้ยานานและเมื่อไรยาไม่พอ",
               "เชื้อใน vegetation **แน่นมาก แบ่งตัวช้า และถูก fibrin หุ้มไว้** เม็ดเลือดขาวเข้าไม่ถึง และก้อนนี้ไม่มีหลอดเลือดเลี้ยง ยาจึงต้องให้ขนาดสูงทางหลอดเลือดและนานพอ (4–6 สัปดาห์) · ยาฆ่าเชื้อได้แต่ซ่อมลิ้นที่พังไม่ได้ (**หัวใจล้มเหลว**) · ซึมเข้าฝีรอบลิ้นได้น้อย (**ติดเชื้อคุมไม่ได้**) · และไม่ทำให้ก้อนใหญ่หดทันที (**emboli**) — สามเหตุผลของการผ่าตัด",
               svg(420, 330, "vegetation มีเชื้อหนาแน่นหุ้มด้วย fibrin ยาและเม็ดเลือดขาวเข้าถึงยาก และสามเหตุผลที่ต้องผ่าตัด",
                   ell(120, 80, 82, 46, "ms"), *[circ(x, y, 2.6, "inkf") for x, y in bact],
                   circ(28, 46, 7, "ac"), circ(214, 112, 7, "ac"), t(28, 30, "WBC", "xs mid tac b"),
                   t(120, 144, "vegetation: fibrin + เกล็ดเลือด + เชื้อ", "xs mid i2"),
                   t(226, 46, "เชื้อแน่นมาก แบ่งตัวช้า", "xs b"), t(226, 62, "→ ยาฆ่าได้ช้า", "xs i2"),
                   t(226, 86, "fibrin หุ้ม · ไม่มีหลอดเลือด", "xs b"), t(226, 102, "→ ยาและ WBC เข้าถึงยาก", "xs i2"),
                   box(226, 116, 186, 40, "ok", "ยาขนาดสูงทางหลอดเลือด\n4–6 สัปดาห์", fs=11),
                   line(10, 170, 410, 170, "lru da"), t(210, 190, "เมื่อยาอย่างเดียวไม่พอ → ผ่าตัด", "sm b mid"),
                   box(8, 202, 132, 92, "bad", "Heart failure\nลิ้นพัง/ทะลุ\nยาซ่อมไม่ได้", fs=11),
                   box(144, 202, 132, 92, "ms", "ติดเชื้อคุมไม่ได้\nฝีรอบลิ้นยาเข้าไม่ถึง\nเชื้อดื้อยา · เชื้อรา\n→ ไข้ไม่ลง AV block", fs=10.5),
                   box(280, 202, 132, 92, "ac", "ป้องกัน emboli\nก้อน ≥ 10 มม.\n+ เคยมี emboli", fs=11),
                   t(210, 318, "ถ้า IV ≥ 10 วันแล้วคงที่ ไม่มีฝี → เปลี่ยนเป็นยากินได้ (POET)", "xs mid i2")))
