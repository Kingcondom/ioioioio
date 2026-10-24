# -*- coding: utf-8 -*-
"""ภาพประกอบคาบ derm "Derm1" — Common skin diseases for internists (อ.ภูริต · Purit Pureesrisak, MD) — ใช้ใน build_derm.py

ทุกฟังก์ชันคืน fig(title, cap, svg) · ภาพตัดขวางผิวหนังเป็น "แผนผัง" ไม่ใช่สัดส่วนจริง
สีที่ใช้: ชั้นขี้ไคล (stratum corneum) = sk · หนังกำพร้า (epidermis) = ms · หนังแท้ (dermis) = bx · ไขมัน = sk + วงกลม bx
น้ำ/สารน้ำ/บวม = wa · หนอง = msf · เซลล์อักเสบ = badf · เลือด/อันตราย = bad · ปกติ/ได้ผล = ok"""
import math
from svg import *


# ═══════════════════════════════════════ ตัวช่วย: ภาพตัดขวางผิวหนัง
def _skin(x, y, w, sc=3, ep=15, de=34, sub=14, bump=None, epx=None, ridge=3.0, step=3, fat=True):
    """ภาพตัดขวางผิวหนังแบบแผนผัง
    bump(u) = ระยะที่ผิวยกขึ้น (ค่าบวก = นูนขึ้น) ที่ตำแหน่ง u (0..w) · epx(u) = หนังกำพร้าหนาขึ้นเท่าไร
    คืน (parts, L) โดย L = dict ฟังก์ชันระดับ: top(u) sc(u) dej(u) และค่าคงที่ de_bot sub_bot"""
    bump = bump or (lambda u: 0)
    epx = epx or (lambda u: 0)
    us = [i * step for i in range(int(w / step) + 1)]
    if us[-1] != w:
        us.append(w)
    top = lambda u: y - bump(u)
    scb = lambda u: top(u) + sc
    rid = lambda u: ridge * math.sin(u * math.pi / 9) ** 2
    dej = lambda u: scb(u) + ep + epx(u) + rid(u)
    de_bot = y + sc + ep + de
    sub_bot = de_bot + sub
    out = []
    if sub:
        out.append(rect(x, de_bot, w, sub, "sk", 0))
        if fat:
            k = 0
            cx = x + 9
            while cx < x + w - 6:
                out.append(ell(cx, de_bot + sub / 2, 8, sub / 2 - 2.5, "bx"))
                cx += 18
                k += 1
    out.append(poly([(x + u, dej(u)) for u in us] + [(x + w, de_bot), (x, de_bot)], "bx", closed=True))
    out.append(poly([(x + u, scb(u)) for u in us] + [(x + u, dej(u)) for u in reversed(us)], "ms", closed=True))
    out.append(poly([(x + u, top(u)) for u in us] + [(x + u, scb(u)) for u in reversed(us)], "sk", closed=True))
    return out, {"top": top, "sc": scb, "dej": dej, "de_bot": de_bot, "sub_bot": sub_bot}


def _dome(c, half, hgt):
    """ฟังก์ชันโดม (ใช้กับ bump/epx) — กึ่งกลาง c ครึ่งความกว้าง half สูง hgt"""
    def f(u):
        d = abs(u - c) / half
        return hgt * (1 - d * d) if d < 1 else 0
    return f


def _plateau(a, b, hgt, ramp=8):
    def f(u):
        if u <= a - ramp or u >= b + ramp:
            return 0
        if a <= u <= b:
            return hgt
        d = (a - u) / ramp if u < a else (u - b) / ramp
        return hgt * (1 - d) ** 1.5 if 0 <= d < 1 else 0
    return f


def _dots(pts, r=1.8, c="badf"):
    return [circ(px, py, r, c) for px, py in pts]


def _x(cx, cy, r=6):
    return line(cx - r, cy - r, cx + r, cy + r, "lbad w3") + line(cx - r, cy + r, cx + r, cy - r, "lbad w3")


def _ok(cx, cy, r=6):
    return path("M%s %s L%s %s L%s %s" % (cx - r, cy, cx - r / 3, cy + r * 0.7, cx + r, cy - r * 0.8), "lok w3")


# ═══════════════════════════════════════ 1 Primary lesions ตามความลึก
def primary():
    W, H = 202, 122
    out = []

    def panel(k, name, rule, note):
        col, row = k % 2, k // 2
        px, py = 6 + col * (W + 6), 4 + row * (H + 6)
        out.append(rect(px, py, W, H, "bx", 8))
        out.append(t(px + 8, py + 16, name, "sm b"))
        out.append(t(px + W - 8, py + 16, rule, "xs end tac b"))
        out.append(t(px + 8, py + H - 5, note, "xs mu"))
        return px + 8, py + 38

    # macule / patch
    x, y = panel(0, "Macule · Patch", "แบน · <1 / >1 cm", "สีเปลี่ยน คลำไม่ได้")
    p, L = _skin(x, y, 186)
    out += p
    out.append(poly([(x + 70 + i, L["sc"](70 + i) + 2) for i in range(0, 47, 3)] + [(x + 116 - i, L["dej"](116 - i) - 1) for i in range(0, 47, 3)], "msf", closed=True))
    # papule / plaque
    x, y = panel(1, "Papule · Plaque", "นูน · <1 / >1 cm", "เนื้อแน่น — epidermis หนา/เซลล์ใน dermis")
    p, L = _skin(x, y, 186, bump=_plateau(60, 130, 9), epx=_plateau(60, 130, 7))
    out += p
    out += _dots([(x + 70 + 9 * i, L["dej"](70 + 9 * i) + 6 + (i % 2) * 4) for i in range(7)])
    # nodule
    x, y = panel(2, "Nodule", "ลึก · มักใหญ่ >1 cm", "ก้อนใน dermis/ไขมัน คลำได้ชัดกว่าเห็น")
    p, L = _skin(x, y, 186, bump=_dome(93, 40, 6))
    out += p
    out.append(ell(x + 93, L["de_bot"] - 4, 30, 15, "bad"))
    # wheal
    x, y = panel(3, "Wheal", "dermal edema · ชั่วคราว", "ลมพิษ — ยุบเองใน < 24 ชม.")
    p, L = _skin(x, y, 186, bump=_plateau(62, 124, 6))
    out += p
    out.append(ell(x + 93, L["dej"](93) + 10, 38, 8, "wa"))
    # vesicle / bulla
    x, y = panel(4, "Vesicle · Bulla", "น้ำใส · <1 / >1 cm", "ตุ่มน้ำ — ในหรือใต้ epidermis")
    bul = _dome(140, 34, 13)
    ves = _dome(52, 16, 9)
    p, L = _skin(x, y, 186, bump=lambda u: ves(u) + bul(u))
    out += p
    out.append(ell(x + 52, L["sc"](52) + 7, 12, 6.5, "wa"))
    base = y + 3 + 15 + 1.5
    us = list(range(108, 173, 3))
    out.append(poly([(x + u, L["dej"](u)) for u in us] + [(x + u, base) for u in reversed(us)], "wa", closed=True))
    out.append(t(x + 52, L["de_bot"] - 6, "vesicle", "xs mid twa"))
    out.append(t(x + 140, L["de_bot"] - 6, "bulla (ใต้ epidermis)", "xs mid twa"))
    # pustule
    x, y = panel(5, "Pustule", "หนอง · มัก <1 cm", "ตุ่มหนอง — มีเม็ดเลือดขาว")
    p, L = _skin(x, y, 186, bump=_dome(93, 16, 9))
    out += p
    out.append(ell(x + 93, L["sc"](93) + 7, 12, 6.5, "msf"))
    out += _dots([(x + 88, L["sc"](93) + 6), (x + 96, L["sc"](93) + 9), (x + 99, L["sc"](93) + 4)], 1.5, "paf")
    # angioedema
    x, y = panel(6, "Angioedema", "บวมลึก", "ขอบไม่ชัด ปวดตึงมากกว่าคัน")
    p, L = _skin(x, y, 186, bump=_dome(93, 80, 7))
    out += p
    out.append(ell(x + 93, L["de_bot"] - 2, 70, 12, "wa"))
    # cyst / ref layer labels
    x, y = panel(7, "ชั้นของผิว", "ใช้ทุกภาพในคาบ", "ความลึก → ชนิดของรอยโรค")
    p, L = _skin(x, y, 92)
    out += p
    out.append(t(x + 100, L["top"](0) - 1, "stratum corneum", "xs"))
    out.append(t(x + 100, L["sc"](0) + 13, "epidermis", "xs b"))
    out.append(t(x + 100, (L["dej"](0) + L["de_bot"]) / 2 + 5, "dermis", "xs b"))
    out.append(t(x + 100, (L["de_bot"] + L["sub_bot"]) / 2 + 4, "subcutis (ไขมัน)", "xs"))
    return fig("Primary lesion — บอกได้จาก “ความลึก” และ “สิ่งที่อยู่ข้างใน”",
               "ทุกช่องเป็นภาพตัดขวางผิวหนังแบบเดียวกัน (ช่องล่างขวา = ชื่อชั้น): **แบน** = สีเปลี่ยนในชั้น epidermis/dermis บน (macule <1 cm · patch >1 cm) · **นูนเนื้อแน่น** = epidermis หนาขึ้นหรือมีเซลล์สะสมใน dermis (papule <1 cm · plaque >1 cm) · **nodule** = ก้อนลึกใน dermis/ไขมัน มักคลำได้ชัดกว่ามองเห็น · **wheal** = dermis บนบวมน้ำชั่วคราว (✍️ “บวมจาก dermis” = ลมพิษ) · **vesicle/bulla** = ตุ่มน้ำใส (<1 / >1 cm) · **pustule** = ตุ่มหนอง (✍️ “ตุ่มหนอง”) · **angioedema** = บวมน้ำที่ dermis ล่างและไขมัน จึงขอบไม่ชัด",
               svg(420, 4 * (H + 6) + 2, "ภาพตัดขวางผิวหนังแสดงรอยโรคปฐมภูมิแต่ละชนิดตามความลึกของรอยโรค", *out))


# ═══════════════════════════════════════ 2 ต้นไม้ตัดสินใจเรียกชื่อรอยโรค
def lesion_tree():
    out = [box(130, 6, 160, 30, "ac", "คลำแล้วนูนไหม?", "b"),
           # flat branch
           ar(150, 36, 66, 58, "ln", "ah", "แบน", "xs i2 mid", dx=-14, dy=-2),
           box(10, 60, 112, 40, "bx", "Macule <1 cm\nPatch >1 cm", fs=12),
           # solid
           ar(210, 36, 210, 58, "ln", "ah", "นูน เนื้อแน่น", "xs i2", dx=8, dy=2),
           box(150, 60, 120, 52, "bx", "Papule <1 cm\nPlaque >1 cm\nNodule ลึก", fs=12),
           # fluid
           ar(270, 36, 352, 58, "ln", "ah", "มีน้ำข้างใน", "xs i2 mid", dx=18, dy=-2),
           box(298, 60, 112, 52, "wa", "ใส: Vesicle/\nBulla (1 cm)\nขุ่น: Pustule", fs=12),
           # transient
           box(10, 126, 400, 34, "ms", "นูนแต่ “หายเองใน < 24 ชม. แล้วไปขึ้นที่ใหม่” = Wheal (dermal edema)", fs=12),
           t(210, 182, "แล้วจึงบอก secondary change บนผิว", "sm b mid"),
           box(10, 192, 130, 30, "sk", "scale · crust", fs=11.5),
           box(145, 192, 130, 30, "sk", "erosion · ulcer", fs=11.5),
           box(280, 192, 130, 30, "sk", "lichenification", fs=11.5),
           t(210, 242, "เส้นตัด 1 cm (ตำราใหม่) — ตำราเก่าบางเล่มใช้ 0.5 cm", "xs mid mu")]
    return fig("เรียกชื่อรอยโรคใน 3 คำถาม: แบนหรือนูน · ข้างในเป็นเนื้อหรือน้ำ · ใหญ่กว่า 1 cm ไหม",
               "สไลด์ใช้เกณฑ์ **1 cm** แบ่ง macule/patch · papule/plaque · vesicle/bulla — ใช้มือคลำทุกครั้งเพราะ “นูนเล็กน้อย” มองด้วยตาอย่างเดียวพลาดง่าย · wheal ต่างจาก papule/plaque ที่ **ไม่คงที่** (หายเองภายในชั่วโมงและย้ายที่) · ถ้ามีน้ำ ให้ดูว่าใส (vesicle/bulla) หรือขุ่นเป็นหนอง (pustule)",
               svg(420, 250, "แผนภาพตัดสินใจเลือกชื่อรอยโรคปฐมภูมิจากความนูน สิ่งที่อยู่ข้างใน และขนาด", *out))


# ═══════════════════════════════════════ 3 Secondary lesions — เสียผิวลึกแค่ไหน
def secondary():
    W, H = 202, 122
    out = []

    def panel(k, name, th, note):
        col, row = k % 2, k // 2
        px, py = 6 + col * (W + 6), 4 + row * (H + 6)
        out.append(rect(px, py, W, H, "bx", 8))
        out.append(t(px + 8, py + 16, name, "sm b"))
        out.append(t(px + W - 8, py + 16, th, "xs end tac b"))
        out.append(t(px + 8, py + H - 5, note, "xs mu"))
        return px + 8, py + 40

    # scale
    x, y = panel(0, "Scale", "ขุย", "ขี้ไคลหนา/หลุดช้า → แผ่นขาว")
    p, L = _skin(x, y, 186, sc=3)
    out += p
    for i in range(6):
        u = 48 + i * 16
        out.append(rect(x + u, L["top"](u) - 5 - (i % 2) * 2, 13, 4.5, "sk", 1.5))
    # crust
    x, y = panel(1, "Crust", "สะเก็ด", "น้ำเหลือง/เลือด/หนองแห้ง")
    p, L = _skin(x, y, 186)
    out += p
    out.append(path("M%s %s Q%s %s %s %s Q%s %s %s %s Z" % (x + 60, L["top"](60), x + 93, L["top"](93) - 24, x + 126, L["top"](126),
                                                         x + 93, L["top"](93) - 2, x + 60, L["top"](60)), "msf"))
    # erosion
    x, y = panel(2, "Erosion", "ถลอก", "เสียแค่ epidermis → ไม่เป็นแผลเป็น")
    p, L = _skin(x, y, 186)
    out += p
    out.append(poly([(x + 66, L["top"](66)), (x + 72, L["sc"](72) + 8), (x + 114, L["sc"](114) + 8), (x + 120, L["top"](120))], "paf", closed=True))
    out.append(line(x + 66, L["top"](66), x + 72, L["sc"](72) + 8, "lbad") + line(x + 72, L["sc"](72) + 8, x + 114, L["sc"](114) + 8, "lbad") + line(x + 114, L["sc"](114) + 8, x + 120, L["top"](120), "lbad"))
    # ulcer
    x, y = panel(3, "Ulcer", "แผล", "ถึง dermis/ไขมัน → เป็นแผลเป็น")
    p, L = _skin(x, y, 186)
    out += p
    u0 = L["de_bot"] - 6
    out.append(poly([(x + 58, L["top"](58)), (x + 72, u0), (x + 114, u0), (x + 128, L["top"](128))], "paf", closed=True))
    out.append(poly([(x + 58, L["top"](58)), (x + 72, u0), (x + 114, u0), (x + 128, L["top"](128))], "lbad"))
    # excoriation
    x, y = panel(4, "Excoriation", "รอยเกา", "เส้นตรงตามเล็บ — บอกว่าคันจริง")
    p, L = _skin(x, y, 186)
    out += p
    for u in (60, 84, 108):
        out.append(poly([(x + u, L["top"](u)), (x + u + 4, L["sc"](u) + 9), (x + u + 10, L["sc"](u) + 9), (x + u + 14, L["top"](u))], "lbad"))
    # fissure
    x, y = panel(5, "Fissure", "ร่องแตก", "แห้งหนา ไม่ยืดหยุ่น → แตก เจ็บ")
    p, L = _skin(x, y, 186, sc=5, ep=18, de=26)
    out += p
    out.append(poly([(x + 88, L["top"](88)), (x + 93, L["dej"](93) + 7), (x + 98, L["top"](98))], "lbad w2"))
    # lichenification
    x, y = panel(6, "Lichenification", "ผิวหนา", "หนา สีคล้ำ ลายผิวชัด (เกาซ้ำ)")
    p, L = _skin(x, y, 186, sc=6, ep=22, de=22, ridge=7)
    out += p
    for u in range(20, 180, 22):
        out.append(line(x + u, L["top"](u), x + u + 3, L["top"](u) + 6, "ln w2"))
    # atrophy
    x, y = panel(7, "Atrophy", "ฝ่อ", "บาง เหี่ยว มัน / dermis ยุบ (steroid)")
    p, L = _skin(x, y, 186, sc=2, ep=7, de=30, ridge=0.4, bump=_plateau(60, 126, -5))
    out += p
    return fig("Secondary lesion — สิ่งที่เกิดตามมาบนรอยโรค บอกเวลาและพฤติกรรม (เกา/แห้ง/ติดเชื้อ)",
               "**Erosion** เสียแค่ epidermis (✍️ “partial loss”) จึงหายไม่เป็นแผลเป็น · **Ulcer** ลึกถึง dermis (✍️ “full-thickness loss”) จึงหายเป็นแผลเป็น — ใช้แยก pemphigus/impetigo (erosion) ออกจาก ecthyma/pyoderma gangrenosum (ulcer) · **crust** (✍️ “สะเก็ด/สะเก็ดน้ำเหลือง”) = ของเหลวที่ซึมออกมาแล้วแห้ง บอกว่าเคยมีตุ่มน้ำหรือแผลเปิด · **excoriation** (✍️ “รอยเกา”) และ **lichenification** (✍️ “ผิวหนังหนาขึ้น สีคล้ำขึ้น ลายผิวชัดขึ้น”) บอกว่าคันและเกามานาน · **atrophy** (✍️ “ดูฝ่อ”) — เช่นใช้ steroid แรงนานเกิน",
               svg(420, 4 * (H + 6) + 2, "ภาพตัดขวางผิวหนังแสดงรอยโรคทุติยภูมิแต่ละชนิดตามความลึกที่เสียไป", *out))


# ═══════════════════════════════════════ 4 วิธีบรรยายรอยโรค (ใช้ในข้อสอบ/OSCE)
def describe():
    steps = [("1", "Distribution", "ตำแหน่ง · กระจาย/เฉพาะที่ · สมมาตร?\nflexural · extensor · แดดโดน · dermatome", "ac"),
             ("2", "Arrangement", "discrete · grouped · linear · annular\nreticular · Koebner (ตามรอยเกา)", "ac"),
             ("3", "Primary lesion", "ชนิด + ขนาด (cm) + สี + ขอบชัด/ไม่ชัด\n+ ผิวเรียบ/ขรุขระ + จำนวน", "ms"),
             ("4", "Secondary change", "scale (ชนิด) · crust · erosion/ulcer\nexcoriation · lichenification", "ms"),
             ("5", "คลำ + ทดสอบ", "แข็ง/นุ่ม · กดเจ็บ · blanch (diascopy)\nNikolsky · ชา (เรื้อน) · เส้นประสาทโต", "ok")]
    out = []
    y = 6
    for n, h, d, c in steps:
        out += [rect(10, y, 400, 48, c, 8), circ(30, y + 24, 11, "inkf"), t(30, y + 28, n, "sm b mid tpa"),
                t(50, y + 19, h, "sm b"), t(160, y + 19, d.split("\n")[0], "xs"), t(160, y + 36, d.split("\n")[1], "xs i2")]
        y += 54
    out += [rect(10, y + 4, 400, 64, "sk", 8),
            t(20, y + 22, "ตัวอย่าง (ภาพสไลด์หน้า 13):", "xs b"),
            t(20, y + 40, "“Grouped vesicles on an erythematous base, unilateral,", "xs i2"),
            t(20, y + 56, "band-like (dermatomal) on one side of the back” → zoster", "xs i2")]
    return fig("บรรยายรอยโรคเป็นประโยคเดียว — ไล่จาก “ไกล” ไป “ใกล้” แล้วจึงคลำ",
               "ลำดับนี้ใช้ได้ทั้งเขียนใบ consult ตอบ MEQ และ OSCE: มองภาพรวมก่อน (กระจายที่ไหน เรียงตัวแบบไหน) แล้วจึงดูรอยโรคเดี่ยว (ชนิด ขนาด สี ขอบ) ปิดด้วยการคลำ — **การคลำเปลี่ยนการวินิจฉัยได้** เช่น nodule ที่กดเจ็บบนหน้าแข้ง (erythema nodosum) · ผื่นที่กดไม่จาง (purpura → vasculitis) · ผื่นชาและเส้นประสาทโต (เรื้อน) · ตัวอย่างล่างมาจากภาพในสไลด์ที่ ✍️ เขียนว่า “group of vesicle on erythematous base”",
               svg(420, y + 74, "ขั้นตอนห้าขั้นในการบรรยายรอยโรคผิวหนังพร้อมตัวอย่างประโยค", *out))


# ═══════════════════════════════════════ 5 Eczema acute → subacute → chronic (histology)
def eczema_stages():
    out = []
    cols = [("Acute", "ตุ่มน้ำ ซึม สะเก็ด", "spongiosis\n→ vesicle"),
            ("Subacute", "แดง ตุ่ม + ขุยบาง", "parakeratosis\n(ขุย)"),
            ("Chronic", "หนา แห้ง ลายชัด", "acanthosis +\nhyperkeratosis")]
    for i, (name, look, histo) in enumerate(cols):
        x = 8 + i * 138
        out.append(t(x + 63, 16, name, "sm b mid"))
        out.append(t(x + 63, 30, look, "xs mid i2"))
        if i == 0:
            p, L = _skin(x, 44, 126, sc=3, ep=22, de=40, sub=0, bump=_dome(63, 30, 7))
            out += p
            out.append(ell(x + 63, L["sc"](63) + 10, 14, 7, "wa"))
            for u in (28, 44, 82, 98):
                out.append(circ(x + u, L["sc"](u) + 12, 3.2, "wa"))
            out += _dots([(x + 20 + 12 * k, L["dej"](20 + 12 * k) + 8 + (k % 3) * 4) for k in range(9)])
            out.append(path("M%s %s q -3 8 0 14" % (x + 50, L["top"](50) - 4), "lwa w2"))
            out.append(path("M%s %s q 3 8 0 14" % (x + 76, L["top"](76) - 4), "lwa w2"))
        elif i == 1:
            p, L = _skin(x, 44, 126, sc=5, ep=26, de=36, sub=0, ridge=4)
            out += p
            for k in range(5):
                u = 14 + k * 24
                out.append(rect(x + u, L["top"](u) - 4, 14, 4, "sk", 1.5))
            out += _dots([(x + 20 + 14 * k, L["dej"](20 + 14 * k) + 8 + (k % 2) * 4) for k in range(8)])
            out.append(circ(x + 40, L["sc"](40) + 11, 2.6, "wa"))
            out.append(circ(x + 86, L["sc"](86) + 13, 2.6, "wa"))
        else:
            p, L = _skin(x, 44, 126, sc=9, ep=36, de=26, sub=0, ridge=9)
            out += p
            for u in range(10, 120, 18):
                out.append(line(x + u, L["top"](u), x + u + 3, L["top"](u) + 8, "ln w2"))
            out += _dots([(x + 25 + 18 * k, L["dej"](25 + 18 * k) + 6) for k in range(5)], 1.6, "inkf")
        out.append(rect(x, 120, 126, 36, "sk", 6))
        out.append(t(x + 63, 135, histo.split("\n")[0], "xs mid b"))
        out.append(t(x + 63, 149, histo.split("\n")[1], "xs mid"))
    out += [ar(134, 80, 146, 80, "lac w2", "ah-ac"), ar(272, 80, 284, 80, "lac w2", "ah-ac"),
            rect(8, 166, 402, 54, "bx", 8),
            t(16, 184, "ทำไมซึม: น้ำ (สีฟ้า) เข้าไปแทรกระหว่างเซลล์หนังกำพร้า (spongiosis)", "xs"),
            t(16, 200, "จนเป็นตุ่มน้ำเล็ก → แตก → น้ำเหลืองซึม → แห้งเป็นสะเก็ด", "xs"),
            t(16, 214, "ทำไมหนา: เกาซ้ำ → keratinocyte แบ่งตัวมากขึ้น (ป้องกันตัว)", "xs")]
    return fig("Eczema 3 ระยะ — ระยะเดียวกันของ “โรคไหนก็ได้” ในกลุ่ม eczema",
               "ภาพตัดขวาง (ไม่ตามสัดส่วนจริง): **acute** — เซลล์อักเสบ (จุดแดง) หลั่ง cytokine ทำให้น้ำแทรกระหว่าง keratinocyte (**spongiosis**) → ตุ่มน้ำเล็กมาก (minute vesicles) → แตก ซึม และเป็นสะเก็ด · **subacute** — น้ำลดลง keratinocyte สร้างใหม่เร็วจนนิวเคลียสค้าง (parakeratosis) → ขุยบาง · **chronic** — เกาซ้ำ ๆ ทำให้ epidermis หนา (acanthosis) ขี้ไคลหนา (hyperkeratosis) melanin เพิ่ม และลายผิวชัด = **lichenification** · ระยะบอก “ยาพื้นฐาน” ที่ต้องใช้: เปียกใช้แห้ง (wet dressing/cream) · แห้งใช้มัน (ointment)",
               svg(420, 226, "ภาพตัดขวางผิวหนังเปรียบเทียบผื่น eczema ระยะเฉียบพลัน กึ่งเฉียบพลัน และเรื้อรัง", *out))


# ═══════════════════════════════════════ ตัวช่วย: ลูกศรระหว่างกล่อง
def _link(a, b, c="ln", m="ah", pad=3, label=None, lc="xs i2 mid", dx=0, dy=-5):
    """a, b = (cx, cy, half_w, half_h) — ลากลูกศรจากขอบกล่อง a ไปขอบกล่อง b"""
    ax, ay, aw, ah_ = a
    bx, by, bw, bh = b
    dx_, dy_ = bx - ax, by - ay
    d = math.hypot(dx_, dy_) or 1
    ux, uy = dx_ / d, dy_ / d
    ta = min(aw / abs(ux) if ux else 1e9, ah_ / abs(uy) if uy else 1e9) + pad
    tb = min(bw / abs(ux) if ux else 1e9, bh / abs(uy) if uy else 1e9) + pad + 2
    return ar(ax + ux * ta, ay + uy * ta, bx - ux * tb, by - uy * tb, c, m, label, lc, dx, dy)


def _node(cx, cy, hw, hh, c, h, s=None, fs="xs"):
    out = [rect(cx - hw, cy - hh, 2 * hw, 2 * hh, c, 8)]
    if s:
        out += [t(cx, cy - 3, h, fs + " b mid"), t(cx, cy + 11, s, "xs mid i2")]
    else:
        out += [t(cx, cy + 4, h, fs + " b mid")]
    return out


# ═══════════════════════════════════════ 6 วงจร eczema (สไลด์ The eczema cycle) + จุดตัดวงจร
def eczema_cycle():
    N = [(135, 34, "Barrier เสีย", "✍️ ฟอกสบู่ · น้ำร้อน", "ms"),
         (210, 104, "เสียน้ำ (TEWL↑)", "ผิวแห้ง", "wa"),
         (190, 196, "สิ่งระคาย/allergen", "S. aureus แทรกเข้า", "ms"),
         (72, 196, "อักเสบ + คัน", "Th2 · IL-4/13/31", "bad"),
         (58, 104, "เกา", "✍️ “เกา”", "bad")]
    HW, HH = 50, 20
    out = []
    for i in range(5):
        a, b = N[i], N[(i + 1) % 5]
        out.append(_link((a[0], a[1], HW, HH), (b[0], b[1], HW, HH), "lbad w2", "ah-bad"))
    for cx, cy, h, s, c in N:
        out += _node(cx, cy, HW, HH, c, h, s)
    fixes = [("Emollient (vaseline)", "อุดน้ำไม่ให้ระเหย"), ("งดสบู่แรง ใช้น้ำอุ่น", "ไม่ล้างไขมันผิว"),
             ("Bleach bath / ยาฆ่าเชื้อ", "ลด S. aureus"), ("Topical steroid", "ไม่อักเสบ = ไม่คัน"),
             ("ตัดเล็บ · antihistamine", "ลดการเกา (นอนหลับ)")]
    y = 14
    out.append(t(342, 12, "ตัดวงจรตรงไหน", "sm b mid"))
    for h, s in fixes:
        out += [rect(272, y + 6, 140, 36, "ok", 8), t(342, y + 21, h, "xs b mid"), t(342, y + 35, s, "xs mid i2")]
        y += 44
    out.append(t(135, 246, "No inflammation = no itch = no scratching", "xs mid b tok"))
    return fig("The eczema cycle — ทำไมผื่นจึงเป็นซ้ำ และตัดวงจรได้กี่จุด",
               "สไลด์ใช้ภาพ “The eczema cycle” และ “Breaking the eczema cycle” · ✍️ จดว่าจุดเริ่มคือ **ฟอกสบู่** (ล้างไขมันและสารให้ความชุ่มชื้นของชั้นขี้ไคล) → น้ำระเหยออก (TEWL) ผิวแห้ง → สารระคาย allergen และ S. aureus แทรกเข้า → Th2 อักเสบ หลั่ง IL-31 ที่กระตุ้นปลายประสาทคันโดยตรง → **เกา** → barrier เสียมากขึ้น · การรักษาจึงต้องทำ **หลายจุดพร้อมกัน** (กล่องเขียว) ไม่ใช่ steroid อย่างเดียว · สไลด์: “No inflammation = no itchiness = no scratching”",
               svg(420, 256, "วงจรการเกิดผื่นเอ็กซีมาห้าขั้นและวิธีตัดวงจรในแต่ละขั้น", *out))


# ═══════════════════════════════════════ 7 บันไดการรักษา eczema
def tx_ladder():
    steps = [("ทุกราย (ฐานบันได)", "Emollient วันละ ≥ 2 ครั้ง · เลี่ยงสบู่/น้ำร้อน/สิ่งกระตุ้น\nรักษาต้นเหตุ (varicose vein, ติดเชื้อ) · ✍️ ตัวช่วยสำคัญที่สุด", "ok"),
             ("ขั้น 1 — Topical corticosteroid", "ความแรงตามอายุ/ตำแหน่ง · วันละ 1–2 ครั้งเป็นวัน ๆ\nCream = acute/subacute · Ointment = แห้ง เรื้อรัง", "ac"),
             ("ขั้น 2 — Topical calcineurin inhibitor", "Tacrolimus 0.03% ointment · Pimecrolimus 1% cream\nหน้า เปลือกตา ข้อพับ — ไม่ทำให้ผิวบาง", "ac"),
             ("ขั้น 3 — Phototherapy", "Narrowband UVB · PUVA — ผื่นกว้าง ดื้อยาทา", "ms"),
             ("ขั้น 4 — Systemic", "Steroid ระยะสั้นเฉพาะ acute รุนแรงกระจาย (ระวัง rebound)\nCyclosporine · MTX · dupilumab/JAK-i (นอกสไลด์)", "bad")]
    out = []
    n = len(steps)
    for i, (h, d, c) in enumerate(steps):
        y = 8 + (n - 1 - i) * 62
        x = 10 + i * 14
        w = 400 - i * 14
        out += [rect(x, y, w, 54, c, 8), t(x + 10, y + 18, h, "sm b")]
        ln = d.split("\n")
        out += [t(x + 10, y + 34, ln[0], "xs i2")]
        if len(ln) > 1:
            out += [t(x + 10, y + 48, ln[1], "xs i2")]
    out += [rect(10, 322, 400, 44, "sk", 8),
            t(20, 340, "+ ติดเชื้อแทรก (หนอง สะเก็ดเหลือง) → ยาปฏิชีวนะ · คันนอนไม่หลับ → oral antihistamine", "xs"),
            t(20, 357, "ขึ้นบันไดเมื่อขั้นล่างไม่พอ · ฐาน (emollient) ใช้ตลอดทุกขั้น", "xs b")]
    return fig("บันไดการรักษา eczema (สไลด์ Treatment of eczema) — ฐานกว้างที่สุดคือ emollient",
               "สไลด์ไล่การรักษา 8 ข้อ: แก้สาเหตุ · ยาปฏิชีวนะถ้าติดเชื้อ · antihistamine กิน · **topical corticosteroid** (✍️ ขีดเน้น) ความแรงตามอายุและตำแหน่ง — **cream ใช้ระยะ acute/subacute · ointment ใช้ผื่นแห้งเรื้อรัง** · emollient (vaseline) · tacrolimus 0.03%/pimecrolimus 1% · systemic steroid ระยะสั้นในรายรุนแรงกระจาย · NB-UVB/PUVA · ภาพจัดเป็นบันไดเพื่อให้เห็นว่ายาขั้นสูงไม่แทนฐาน · dupilumab/JAK inhibitor เป็นข้อมูลเพิ่ม **ไม่อยู่ในสไลด์** (AAD 2023 · EuroGuiDerm 2022)",
               svg(420, 372, "บันไดการรักษาผื่นเอ็กซีมาจากสารให้ความชุ่มชื้นจนถึงยากดภูมิคุ้มกันทั้งร่างกาย", *out))


# ═══════════════════════════════════════ 8 ความแรงของ steroid ตามตำแหน่ง (การดูดซึม)
def steroid_site():
    rows = [("ถุงอัณฑะ", 42, "bad"), ("แก้ม/คาง", 13, "bad"), ("หน้าผาก", 6, "bad"), ("หนังศีรษะ", 3.5, "ms"),
            ("หลัง", 1.7, "ms"), ("ท้องแขน (อ้างอิง)", 1, "ok"), ("ฝ่ามือ", 0.83, "ok"), ("ฝ่าเท้า (โค้ง)", 0.14, "ok")]
    out = [t(10, 14, "ยาเข้าผิวได้มากกว่าท้องแขนกี่เท่า (hydrocortisone, log scale)", "xs b")]
    x0, x1 = 120, 330
    lo, hi = math.log10(0.1), math.log10(50)
    X = lambda v: x0 + (math.log10(v) - lo) / (hi - lo) * (x1 - x0)
    for v in (0.1, 1, 10):
        out.append(line(X(v), 24, X(v), 24 + len(rows) * 20, "lru da"))
        out.append(t(X(v), 24 + len(rows) * 20 + 12, "%g×" % v, "xs mid mu"))
    for i, (name, v, c) in enumerate(rows):
        y = 26 + i * 20
        out += [t(112, y + 12, name, "xs end"), rect(x0, y + 3, X(v) - x0, 12, c, 3), t(X(v) + 4, y + 13, "%g×" % v, "xs b")]
    y = 26 + len(rows) * 20 + 22
    out += [rect(10, y, 132, 70, "bad", 8), t(76, y + 16, "ผิวบาง ดูดซึมมาก", "xs b mid"), t(76, y + 32, "หน้า เปลือกตา ข้อพับ", "xs mid"),
            t(76, y + 46, "อวัยวะเพศ · เด็ก", "xs mid"), t(76, y + 62, "→ อ่อน (hydrocortisone)", "xs mid b"),
            rect(146, y, 128, 70, "ms", 8), t(210, y + 16, "ลำตัว แขน ขา", "xs b mid"), t(210, y + 32, "ผื่นทั่วไป", "xs mid"),
            t(210, y + 62, "→ กลาง (TA 0.1%)", "xs mid b"),
            rect(278, y, 132, 70, "ok", 8), t(344, y + 16, "ผิวหนา ดูดซึมน้อย", "xs b mid"), t(344, y + 32, "ฝ่ามือ ฝ่าเท้า", "xs mid"),
            t(344, y + 46, "ผื่นหนา lichenified", "xs mid"), t(344, y + 62, "→ แรง (clobetasol)", "xs mid b"),
            t(210, y + 90, "ปริมาณ: 1 FTU (ข้อปลายนิ้วชี้) ≈ 0.5 g ทาได้ ≈ 2 ฝ่ามือผู้ใหญ่", "xs mid i2")]
    return fig("ทำไม “ความแรงตามตำแหน่ง” — ผิวแต่ละที่ดูดซึม steroid ต่างกันเป็นสิบเท่า",
               "ข้อมูลการดูดซึม hydrocortisone ผ่านผิว (Feldmann & Maibach 1967 — **ไม่อยู่ในสไลด์**) เทียบกับท้องแขน: ผิวที่ชั้นขี้ไคลบางหรือถูกปิดทับ (หน้า ถุงอัณฑะ ข้อพับ) ดูดซึมยามาก จึงใช้ยาอ่อนและไม่นาน — ถ้าใช้ยาแรงจะเกิด **atrophy, striae** (ภาพในสไลด์ secondary lesion) และ telangiectasia · ฝ่ามือฝ่าเท้ามีขี้ไคลหนามาก ยาอ่อนเข้าไม่ถึง จึงต้องใช้ยาแรง · ointment ปิดผิวทำให้ยาเข้าได้มากกว่า cream ของยาตัวเดียวกัน · FTU (fingertip unit) ช่วยกำหนดปริมาณที่ทา",
               svg(420, y + 98, "แผนภูมิแท่งการดูดซึมยาสเตียรอยด์ผ่านผิวในตำแหน่งต่าง ๆ และการเลือกความแรงของยาตามตำแหน่ง", *out))


# ═══════════════════════════════════════ 9 AD กระจายตามอายุ (สไลด์ Distribution of AD by age)
def _body(cx, top, s=1.0, c="bx"):
    """คนยืนหันหน้า (แผนผัง) — คืน parts และตำแหน่งสำคัญ"""
    hr = 13 * s
    hy = top + hr
    sh = hy + hr + 4 * s
    tw, th = 30 * s, 46 * s
    out = [circ(cx, hy, hr, c), rect(cx - tw / 2, sh, tw, th, c, 6 * s),
           rect(cx - tw / 2 - 11 * s, sh + 2 * s, 9 * s, 50 * s, c, 4 * s), rect(cx + tw / 2 + 2 * s, sh + 2 * s, 9 * s, 50 * s, c, 4 * s),
           rect(cx - 13 * s, sh + th + 2 * s, 11 * s, 52 * s, c, 4 * s), rect(cx + 2 * s, sh + th + 2 * s, 11 * s, 52 * s, c, 4 * s)]
    P = {"cheekL": (cx - 6 * s, hy + 3 * s), "cheekR": (cx + 6 * s, hy + 3 * s),
         "elbowL": (cx - tw / 2 - 6.5 * s, sh + 24 * s), "elbowR": (cx + tw / 2 + 6.5 * s, sh + 24 * s),
         "handL": (cx - tw / 2 - 6.5 * s, sh + 47 * s), "handR": (cx + tw / 2 + 6.5 * s, sh + 47 * s),
         "kneeL": (cx - 7.5 * s, sh + th + 26 * s), "kneeR": (cx + 7.5 * s, sh + th + 26 * s),
         "footL": (cx - 7.5 * s, sh + th + 50 * s), "footR": (cx + 7.5 * s, sh + th + 50 * s),
         "neck": (cx, sh - 1 * s), "scalp": (cx, top + 3 * s), "bottom": sh + th + 56 * s}
    return out, P


def ad_age():
    out = []
    cols = [(72, 0.8, "ทารก 0–2 ปี", ["แก้ม หนังศีรษะ หู", "ด้าน extensor", "(คลาน ถูไถ น้ำลาย)"], ["cheekL", "cheekR", "scalp", "elbowL", "elbowR", "kneeL", "kneeR"]),
            (210, 0.95, "เด็ก 2 ปี – วัยรุ่น", ["ข้อพับแขน–ขา", "(flexural)", "แก้มได้บ้าง"], ["elbowL", "elbowR", "kneeL", "kneeR", "neck"]),
            (348, 1.05, "วัยรุ่น–ผู้ใหญ่", ["ข้อพับเฉพาะที่ · มือ", "หลังเท้า · คอ เปลือกตา", "ผื่นหนา lichenified"], ["elbowL", "elbowR", "handL", "handR", "footL", "footR", "neck"])]
    for cx, s, h, lines, zones in cols:
        top = 34 + (1.05 - s) * 60
        b, P = _body(cx, top, s)
        out.append(t(cx, 18, h, "sm b mid"))
        out += b
        for z in zones:
            zx, zy = P[z]
            out.append(ell(zx, zy, 7 * s, 6 * s, "badf"))
        for k, ln in enumerate(lines):
            out.append(t(cx, 214 + k * 14, ln, "xs mid" + (" i2" if k else " b")))
    return fig("Atopic dermatitis เปลี่ยนตำแหน่งตามวัย (สไลด์ Distribution of AD by age)",
               "จุดแดง = ตำแหน่งที่พบบ่อย · **ทารก**: แก้ม หนังศีรษะ และด้าน extensor (ผิวที่ถูไถพื้นตอนคลานและโดนน้ำลาย) และซ้อนกับ seborrheic dermatitis ได้ · **เด็ก**: ข้อพับแขนขา (เหงื่อ การเสียดสี และการเกาที่ข้อพับ) · **วัยรุ่น–ผู้ใหญ่**: ข้อพับเฉพาะที่ มือ หลังเท้า คอ เปลือกตา ผื่นมักหนาแบบ lichenified · ✍️ “พบมากในเด็ก แต่ adult ก็เจอได้” และ ✍️ ในภาพข้อพับเข่า: “eczema ตามข้อพับ → atopic dermatitis”",
               svg(420, 258, "แผนภาพร่างกายสามช่วงวัยแสดงตำแหน่งของผื่นภูมิแพ้ผิวหนังที่พบบ่อย", *out))


# ═══════════════════════════════════════ 10 กลไก AD: barrier + Th2 + atopic march
def ad_mech():
    A = (110, 30, 98, 20)
    B = (110, 96, 98, 24)
    C = (110, 166, 98, 24)
    D = (110, 236, 98, 20)
    out = []
    out += _node(*A, "ms", "ยีน FLG ผิดปกติ + สบู่/อากาศแห้ง")
    out += _node(*B, "ms", "Barrier เสีย", "NMF↓ ผิวแห้ง · pH↑ → protease↑")
    out += _node(*C, "bad", "Th2 อักเสบ", "IL-4 · IL-13 · IL-31 · IgE↑")
    out += _node(*D, "bad", "คัน → เกา → ผื่น eczema")
    out += [_link(A, B, "ln"), _link(B, C, "ln", label="allergen + S. aureus ซึมเข้า", lc="xs i2", dx=4, dy=0),
            _link(C, D, "ln")]
    out.append(path("M210 160 C 238 160 238 102 214 100", "lbad w2 da", "ah-bad"))
    out.append(t(242, 126, "IL-4/13 กด", "xs tbad"))
    out.append(t(242, 139, "filaggrin ↓", "xs tbad"))
    out += [rect(318, 40, 94, 154, "wa", 8), t(365, 58, "Atopic march", "xs b mid"),
            t(365, 80, "ทารก: AD", "xs mid"), ar(365, 86, 365, 100, "lwa", "ah-wa"),
            t(365, 114, "food allergy", "xs mid"), ar(365, 120, 365, 134, "lwa", "ah-wa"),
            t(365, 148, "asthma", "xs mid"), ar(365, 154, 365, 168, "lwa", "ah-wa"),
            t(365, 182, "allergic rhinitis", "xs mid"),
            ar(212, 180, 314, 176, "lwa w2", "ah-wa"), t(264, 198, "sensitize ผ่านผิว", "xs i2 mid")]
    return fig("ทำไม AD จึงแห้ง คัน และมาพร้อมหอบหืด/ภูมิแพ้จมูก",
               "สองกลไกเสริมกัน: (1) **barrier เสีย** — filaggrin สร้าง natural moisturizing factor ถ้าขาดผิวจะแห้งและ pH สูง เอนไซม์ protease ทำลายรอยต่อเซลล์ (2) **Th2** — allergen ที่ซึมผ่านผิวกระตุ้น IL-4/IL-13 (กด filaggrin ซ้ำ — เส้นประ) และ **IL-31 ที่จับปลายประสาทคันโดยตรง** จึงคันมากแม้ผื่นน้อย · การ sensitize ผ่านผิวที่เสียคือจุดเริ่มของ **atopic march** — สไลด์ให้ประวัติ personal/family history of atopy เป็น major feature · กลไกเป็นข้อมูลเสริมจากตำรา (**ไม่อยู่ในสไลด์**)",
               svg(420, 262, "แผนภาพกลไกของผื่นภูมิแพ้ผิวหนังจากเกราะผิวเสียและการอักเสบชนิด Th2 ไปสู่โรคภูมิแพ้อื่น", *out))


# ═══════════════════════════════════════ 11 Seborrheic dermatitis — sebum + Malassezia
def seb():
    out = [ell(92, 120, 62, 82, "bx"),
           # หนังศีรษะ
           path("M34 92 C 40 40 144 40 150 92", "ms w5"),
           # คิ้ว
           path("M58 98 Q72 90 84 98", "ms w5"), path("M100 98 Q112 90 126 98", "ms w5"),
           # หว่างคิ้ว (glabella)
           ell(92, 100, 6, 6, "ms"),
           # ตา
           ell(71, 110, 8, 3, "ln"), ell(113, 110, 8, 3, "ln"),
           # จมูก
           path("M92 104 L86 140 L98 140", "ln"),
           # ร่องจมูก-แก้ม
           path("M80 140 Q70 154 74 170", "ms w5"), path("M104 140 Q114 154 110 170", "ms w5"),
           # ปาก
           path("M80 176 Q92 182 104 176", "ln"),
           # หู
           ell(28, 120, 8, 16, "ms"), ell(156, 120, 8, 16, "ms"),
           t(92, 222, "T-zone · ไรผม · คิ้ว · ร่องจมูก · หลังหู", "xs mid b"),
           t(92, 236, "+ หน้าอก หลังส่วนบน (ต่อมไขมันมาก)", "xs mid i2")]
    A = (300, 26, 104, 18)
    B = (300, 80, 104, 22)
    C = (300, 140, 104, 22)
    D = (300, 200, 104, 22)
    out += _node(*A, "ms", "ต่อมไขมันมาก (sebum)")
    out += _node(*B, "ac", "Malassezia ชอบไขมัน", "lipase ย่อย sebum → free fatty acid")
    out += _node(*C, "bad", "ผิวคนที่ไวต่อสารนี้อักเสบ", "keratinocyte แบ่งตัวเร็ว")
    out += _node(*D, "ms", "แดง + ขุยเหลืองมัน (greasy)", "✍️ “เหลือง ๆ” ขอบไม่ชัด")
    out += [_link(A, B), _link(B, C), _link(C, D)]
    out += [rect(196, 232, 216, 30, "sk", 8), t(304, 251, "ปัจจัยเสี่ยง: Parkinson · stroke · HIV · เครียด", "xs mid")]
    return fig("Seborrheic dermatitis — ผื่นอยู่ตรงที่ต่อมไขมันมาก เพราะต้นเหตุคือ Malassezia ที่กินไขมัน",
               "Malassezia เป็นยีสต์ที่ต้องใช้ไขมันจากผิว จึงอยู่หนาแน่นที่ **หนังศีรษะ คิ้ว หว่างคิ้ว ร่องจมูก–แก้ม หลังหู หน้าอก** (✍️ “เด่นที่ T zone”) · lipase ของเชื้อย่อย sebum เป็นกรดไขมันอิสระที่ระคายผิวในคนที่ไวต่อสารนี้ → อักเสบ + keratinocyte แบ่งตัวเร็ว → **ขุยเหลืองมัน ขอบไม่ชัด** · รังแค = อาการน้อยที่สุดของโรคนี้ (✍️) · ปัจจัยเสี่ยงในสไลด์: อายุมาก ชาย อ้วน **เครียด** (✍️ “นศพ. ชอบเป็น → เครียด นอนดึก พักผ่อนน้อย”) ฤดูหนาว เหล้า บุหรี่ HTN **HIV** และ **โรคทางระบบประสาท (stroke, Parkinson)** — sebum มากขึ้นและใบหน้าขยับน้อย · การรักษา: steroid + **ยาต้านเชื้อรา** (✍️ “รักษา Malassezia yeast”)",
               svg(420, 268, "ใบหน้าแสดงตำแหน่งผื่นต่อมไขมันอักเสบ และกลไกจากไขมันผิวและเชื้อ Malassezia", *out))


# ═══════════════════════════════════════ 12 Stasis dermatitis — venous hypertension
def stasis():
    out = [t(60, 16, "ลิ้นปกติ", "xs b mid"), t(160, 16, "ลิ้นรั่ว", "xs b mid tbad")]
    # หลอดเลือดดำปกติ
    out += [rect(46, 26, 28, 168, "wa", 10)]
    for y in (60, 110, 160):
        out += [path("M47 %s L60 %s L73 %s" % (y, y - 12, y), "lwa w2")]
    out += [ar(60, 186, 60, 36, "lok w3", "ah-ok"), t(60, 210, "เลือดไหลขึ้น", "xs mid tok")]
    # หลอดเลือดดำรั่ว (โป่ง)
    out += [path("M146 26 C 136 70 136 150 146 194 L 174 194 C 186 150 186 70 174 26 Z", "wa")]
    for y in (60, 110, 160):
        out += [line(146 - 2, y, 152, y - 10, "lbad w2"), line(176, y, 168, y - 10, "lbad w2")]
    out += [ar(160, 40, 160, 182, "lbad w3", "ah-bad"), t(160, 210, "ย้อนลง ค้างที่ขา", "xs mid tbad"),
            t(110, 232, "ambulatory venous", "xs mid b"), t(110, 245, "hypertension", "xs mid b")]
    A = (318, 24, 92, 18)
    B = (318, 76, 92, 24)
    C = (318, 136, 92, 24)
    D = (318, 196, 92, 24)
    E = (318, 252, 92, 18)
    out += _node(*A, "bad", "ความดันใน capillary ขาสูง")
    out += _node(*B, "wa", "น้ำ + fibrinogen รั่ว", "บวม · fibrin cuff รอบหลอดเลือด")
    out += _node(*C, "ms", "RBC รั่ว → hemosiderin", "✍️ สีน้ำตาลเหลือง (hemosiderin)")
    out += _node(*D, "bad", "WBC ติดค้าง → อักเสบ", "คัน eczema · ผิวแข็ง · แผล")
    out += _node(*E, "ok", "Compression = แก้ที่ต้นเหตุ")
    out += [_link(A, B), _link(B, C), _link(C, D), _link(D, E, "lok", "ah-ok")]
    out.append(ar(194, 110, 222, 30, "lbad w2", "ah-bad"))
    return fig("Stasis dermatitis — ทุกอาการมาจาก “ความดันหลอดเลือดดำที่ขาสูงค้าง”",
               "ลิ้นหลอดเลือดดำรั่ว (varicose vein, หลัง DVT) → เวลายืนหรือเดิน เลือดไม่ถูกบีบขึ้น ความดันที่ขาส่วนล่างจึงสูงค้าง (**ambulatory venous hypertension**) → capillary รั่วน้ำ (บวม) fibrinogen (fibrin cuff ขัดขวาง O2) และเม็ดเลือดแดง ซึ่งถูกย่อยเป็น **hemosiderin** สีน้ำตาลเหลือง (สไลด์: triad = alopecia, waxy appearance, yellow-brown pigment) → เม็ดเลือดขาวติดค้างและหลั่งสารอักเสบ → ผื่น eczema ทั้งสองขา รอบข้อเท้าและน่อง · ภาวะแทรกซ้อน: **แผล (มักเหนือตาตุ่มใน) cellulitis lymphangitis** · ผิวที่อักเสบเรื้อรังและทายาหลายชนิด จึง **แพ้ยาทา (ACD) แทรกบ่อย** — neomycin/ยาปฏิชีวนะทา lanolin paraben balsam of Peru น้ำหอม · การรักษาหลักคือ **compression** (stocking, elastic bandage) + steroid ทา + emollient",
               svg(420, 272, "หลอดเลือดดำปกติเทียบกับลิ้นรั่ว และลำดับกลไกที่นำไปสู่ผื่น stasis", *out))


# ═══════════════════════════════════════ 13 Xerotic eczema — crazy paving
def xerosis():
    out = [t(100, 14, "มองจากผิว: “cracked porcelain”", "xs b mid")]
    # ลายกระเบื้อง (polygonal plates)
    import random
    rnd = random.Random(4)
    pts = {}
    for i in range(6):
        for j in range(4):
            pts[(i, j)] = (14 + i * 34 + rnd.uniform(-7, 7) * (0 < i < 5), 26 + j * 40 + rnd.uniform(-7, 7) * (0 < j < 3))
    out.append(rect(14, 26, 170, 120, "ms", 4))
    for i in range(6):
        for j in range(4):
            if i < 5:
                out.append(line(*pts[(i, j)], *pts[(i + 1, j)], "lbad w2"))
            if j < 3:
                out.append(line(*pts[(i, j)], *pts[(i, j + 1)], "lbad w2"))
    out.append(t(100, 162, "แผ่นขุยแห้ง + ร่องแดงหลายเหลี่ยม", "xs mid"))
    # ภาพตัดขวาง
    out.append(t(310, 14, "ภาพตัดขวาง", "xs b mid"))
    p, L = _skin(212, 26, 196, sc=6, ep=16, de=30, sub=0)
    out += p
    for u in (40, 98, 156):
        out.append(poly([(212 + u - 5, L["top"](u)), (212 + u, L["sc"](u) + 9), (212 + u + 5, L["top"](u))], "lbad w2"))
        out += _dots([(212 + u - 4, L["dej"](u) + 7), (212 + u + 3, L["dej"](u) + 11), (212 + u + 8, L["dej"](u) + 6)])
    out += [t(310, 104, "ไขมันใน stratum corneum ↓", "xs mid"), t(310, 118, "→ ขี้ไคลหดตัว แตกเป็นร่อง", "xs mid"),
            t(310, 132, "→ ร่องลึกถึง epidermis → อักเสบ", "xs mid"),
            t(310, 146, "✍️ “หน้าแข้ง (ปกติแห้งสุด)”", "xs mid tac")]
    out += [rect(10, 176, 400, 92, "bad", 8), t(20, 194, "Xerosis กว้างทั้งตัว — มองหาสาเหตุ (สไลด์ Extensive xerotic eczema)", "xs b"),
            t(20, 212, "• มะเร็งภายใน โดยเฉพาะ lymphoma  • ยาขับปัสสาวะ (diuretic)", "xs"),
            t(20, 228, "• atopic eczema · ไตวายเรื้อรัง · ตับวาย · AIDS", "xs"),
            t(20, 244, "• myxedema (hypothyroid) · malabsorption (vitamin A, zinc)", "xs"),
            t(20, 260, "ผู้สูงอายุ + ฤดูหนาว + อาบน้ำร้อน/ฟอกสบู่บ่อย = สาเหตุที่พบบ่อยที่สุด", "xs i2")]
    return fig("Xerotic (asteatotic) eczema — ผิวแห้งจน “แตกลายงา”",
               "ผู้สูงอายุมีไขมันในชั้นขี้ไคลลดลงและเสียน้ำผ่านผิว (TEWL) มากขึ้น โดยเฉพาะหน้าหนาว → ชั้นขี้ไคลหดตัวและแตกเป็นร่องหลายเหลี่ยมเหมือนกระเบื้องร้าว (**cracked porcelain · crazy pavement · dry riverbed**) — ร่องที่ลึกถึง epidermis ทำให้อักเสบเป็นเส้นแดงและคัน · พบบ่อยที่สุดที่ **หน้าแข้งด้านหน้า–ข้าง** (✍️ “หน้าแข้ง ปกติแห้งสุด” · ✍️ “แห้ง ๆ แตก ๆ”) · ถ้าแห้งกว้างทั้งตัว (✍️ ในภาพหน้าท้อง “แห้งมากกกก”) ต้องคิดถึงโรคทางระบบตามกล่องแดง",
               svg(420, 274, "ลายผิวแห้งแตกแบบกระเบื้องร้าว ภาพตัดขวางของร่องแตก และสาเหตุของผิวแห้งทั่วตัว", *out))


# ═══════════════════════════════════════ 14 วงจรคัน–เกา: LSC · prurigo nodularis · nummular
def itch_scratch():
    out = []
    I = (120, 34, 70, 20)
    S = (120, 168, 70, 20)
    E = (36, 101, 0, 0)
    out += _node(120, 34, 70, 20, "bad", "คัน", "IL-31 · histamine · ผิวแห้ง")
    out += _node(120, 168, 70, 20, "bad", "เกา / ถู / แกะ", "ชั่วคราวหายคัน (pain กลบ itch)")
    out.append(path("M190 40 C 236 60 236 150 192 164", "lbad w2", "ah-bad"))
    out.append(path("M50 162 C 4 142 4 60 48 40", "lbad w2", "ah-bad"))
    out += [rect(24, 82, 192, 52, "ms", 8), t(120, 100, "ผิวและเส้นประสาทเปลี่ยน", "xs b mid"),
            t(120, 114, "epidermis หนา · ปลายประสาทงอกเพิ่ม", "xs mid"), t(120, 127, "ไวต่อการคันมากขึ้น (sensitization)", "xs mid")]
    rows = [("Lichen simplex chronicus", "ถูซ้ำ → plaque หนา ลายผิวชัด", "ท้ายทอย ข้อเท้า · ✍️ scrotum"),
            ("Prurigo nodularis", "แกะ → nodule แข็ง 0.5–3 cm", "แขนขา extensor · ✍️ nodule เกา"),
            ("Nummular eczema", "papulovesicle → วงเหรียญ ซึม", "หลังมือ (หญิง) · ขา (ชาย)")]
    y = 8
    for h, a, b in rows:
        out += [rect(244, y, 168, 62, "sk", 8), t(252, y + 17, h, "xs b"), t(252, y + 33, a, "xs"), t(252, y + 49, b, "xs i2")]
        y += 68
    out += [rect(10, 210, 402, 46, "ok", 8), t(20, 228, "ต้องตัดวงจร: steroid แรงทาปิด (occlusion) · ปิดแผลกันเกา · antihistamine ก่อนนอน", "xs"),
            t(20, 245, "หาโรคทางระบบที่ทำให้คันทั้งตัว (ไต ตับ เลือด ไทรอยด์ HIV) โดยเฉพาะ prurigo nodularis", "xs")]
    return fig("Itch–scratch cycle — ทำไมเกาแล้วผื่นยิ่งหนาและยิ่งคัน",
               "การเกาทำให้หายคันชั่วครู่ (ความเจ็บกลบสัญญาณคันที่ไขสันหลัง) แต่ (1) keratinocyte แบ่งตัวป้องกันตัวจน epidermis หนา และ (2) **ปลายประสาทงอกเพิ่มและไวขึ้น** → คันง่ายขึ้นอีก · รูปแบบการเกาบอกชนิดของโรค: **ถูซ้ำเป็นบริเวณ** = lichen simplex chronicus (plaque หนา) · **แกะเป็นจุด** = prurigo nodularis (nodule หลายเม็ด สัมพันธ์กับ AD หรือคันจากโรคทางระบบ) · nummular eczema เป็นผื่นรูปเหรียญที่ซึมได้ (สไลด์: chronic, unknown etiology) · กลไกประสาทเป็นข้อมูลเสริม (**ไม่อยู่ในสไลด์**)",
               svg(420, 262, "วงจรคันและเกา และโรคสามชนิดที่เกิดจากรูปแบบการเกาต่างกัน", *out))


# ═══════════════════════════════════════ 15 Dyshidrosis — ทำไมเป็นตุ่มน้ำลึก “เม็ดสาคู”
def pompholyx():
    out = [t(102, 16, "ผิวบาง (ลำตัว)", "sm b mid"), t(318, 16, "ฝ่ามือ/ข้างนิ้ว", "sm b mid")]
    p, L = _skin(10, 40, 184, sc=3, ep=16, de=34, sub=10, bump=_dome(92, 18, 10))
    out += p
    out.append(ell(102, L["sc"](92) + 7, 13, 7, "wa"))
    out.append(path("M%s %s q -4 10 0 18" % (84, L["top"](80) - 2), "lwa w2"))
    out.append(path("M%s %s q 4 10 0 18" % (120, L["top"](104) - 2), "lwa w2"))
    out += [t(102, 128, "หลังคาบาง → แตกง่าย", "xs mid"), t(102, 142, "ซึม + สะเก็ด", "xs mid i2")]
    p, L = _skin(226, 40, 184, sc=14, ep=18, de=26, sub=10, ridge=4)
    out += p
    for u, r in ((50, 6), (92, 8), (134, 6)):
        out.append(circ(226 + u, L["sc"](u) + 9, r, "wa"))
    out += [t(318, 128, "ขี้ไคลหนามาก กดตุ่มไว้", "xs mid"), t(318, 142, "ไม่แตก เห็นเป็น “เม็ดสาคู”", "xs mid i2"),
            rect(10, 156, 400, 92, "sk", 8),
            t(20, 174, "✍️ “ใส ๆ คัน ๆ อยู่ลึก ๆ” · “มาเป็นตุ่มน้ำ” · “เคยเป็น!”", "xs b"),
            t(20, 192, "วัยรุ่น/ผู้ใหญ่ตอนต้น · ฝ่ามือ ข้างนิ้ว ฝ่าเท้า · คันมาก · ติดเชื้อแทรกบ่อย", "xs"),
            t(20, 210, "สัมพันธ์กับ atopy (✍️ allergic rhinitis, asthma) · เหงื่อ ความเครียด อากาศร้อน", "xs"),
            t(20, 228, "รักษา: ✍️ topical steroid (แรง เพราะผิวหนา) · ติดเชื้อ → antibiotic", "xs"),
            t(20, 243, "แยกจาก tinea (ขูด KOH) · scabies (ซอกนิ้ว อุโมงค์) · ACD", "xs i2")]
    return fig("Dyshidrosis (pompholyx) — ตุ่มน้ำเดียวกับ eczema แต่ “อยู่ใต้ขี้ไคลที่หนา”",
               "ตุ่มน้ำของ eczema เกิดจาก spongiosis ในชั้น epidermis เหมือนกันทุกที่ แต่บนฝ่ามือ ข้างนิ้ว และฝ่าเท้า **ชั้นขี้ไคลหนามาก** จึงกดตุ่มไว้ไม่ให้แตก → เห็นเป็นตุ่มน้ำใสลึกแบบ **“tapioca” (✍️ เม็ดสาคู)** คันมาก ต่างจากผิวบางที่ตุ่มแตกง่ายแล้วซึม · ชื่อ dyshidrosis มาจากความเชื่อเดิมว่าเกิดจากต่อมเหงื่อ ปัจจุบันถือเป็น eczema ชนิดหนึ่ง (ต่อมเหงื่อไม่ได้อุด) · ✍️ ผู้จดเขียนว่า “เคยเป็น!” — พบบ่อยในนักศึกษาวัยนี้",
               svg(420, 254, "ภาพตัดขวางเปรียบเทียบตุ่มน้ำบนผิวบางกับตุ่มน้ำลึกบนฝ่ามือในโรค dyshidrosis", *out))


# ═══════════════════════════════════════ 16 Miliaria — ท่อเหงื่ออุดที่ระดับไหน
def miliaria():
    p, L = _skin(10, 40, 200, sc=6, ep=34, de=64, sub=18, ridge=3)
    out = list(p)
    # ต่อมเหงื่อ + ท่อ
    gx = 110
    out.append(ell(gx, L["de_bot"] - 4, 18, 10, "wa"))
    d = "M%s %s" % (gx, L["de_bot"] - 14)
    yy = L["de_bot"] - 14
    while yy > L["top"](gx - 10) + 2:
        d += " q 8 -5 0 -10 q -8 -5 0 -10"
        yy -= 20
    out.append(path(d, "lwa w2"))
    lv = [(L["sc"](gx) - 2, "crystallina", "ใต้ขี้ไคล · ตุ่มใสไม่แดง", "wa"),
          (L["sc"](gx) + 18, "rubra (ผดผื่นแดง)", "กลาง epidermis · ตุ่มแดงคัน/แสบ", "bad"),
          (L["dej"](gx) + 10, "profunda", "ใต้ DEJ · ตุ่มสีเนื้อ ไม่มีเหงื่อ", "ms")]
    for k, (y, h, s, c) in enumerate(lv):
        out += [circ(gx, y, 5, c + "f" if c != "wa" else "waf"), line(gx + 7, y, 226, 30 + k * 62, "lmu da"),
                rect(226, 14 + k * 62, 186, 52, c, 8), t(234, 32 + k * 62, "Miliaria " + h, "xs b"), t(234, 48 + k * 62, s, "xs")]
    out += [rect(10, 196, 402, 50, "sk", 8),
            t(20, 214, "สาเหตุ: เหงื่อออกซ้ำ ๆ ในที่ร้อน/ทารก + แบคทีเรียประจำผิว + UV → ท่อเหงื่อเสีย", "xs"),
            t(20, 232, "เหงื่อรั่วออกนอกท่อ: ตื้น = ตุ่มใส · ลึก = อักเสบแดง · หายเองใน ~1 วันเมื่อเย็นลง", "xs")]
    return fig("Miliaria (ผด) — ชนิดขึ้นกับว่าท่อเหงื่ออุดตื้นหรือลึก",
               "สไลด์: miliaria เกิดจาก **ท่อเหงื่อเสียความต่อเนื่อง (disruption of sweat ductal integrity)** · ปัจจัยเสริม: UV แบคทีเรียประจำผิว และเหงื่อออกซ้ำ ๆ · พบบ่อยในทารกและที่อากาศร้อน · **หายเองภายในราว 1 วัน** · เหงื่อที่รั่วตรงไหนกำหนดหน้าตา: ใต้ขี้ไคล = **crystallina** ตุ่มใสเหมือนหยดน้ำ ไม่แดง (ภาพในสไลด์) · กลาง epidermis = **rubra** ตุ่มแดงคัน (อาจเป็น pustulosa) · ลึกระดับ DEJ = **profunda** · รักษา: ทำให้เย็น ใส่เสื้อโปร่ง เลี่ยงครีมข้น (dyshidrosis และ miliaria อยู่ในรหัส นล. เดียวกัน)",
               svg(420, 252, "ภาพตัดขวางผิวหนังแสดงท่อเหงื่อและระดับการอุดตันของผดสามชนิด", *out))


# ═══════════════════════════════════════ 17 Contact dermatitis: ICD vs ACD
def contact():
    out = [t(102, 16, "Irritant (ICD) — 80%", "sm b mid"), t(318, 16, "Allergic (ACD) — type IV", "sm b mid")]
    L_ = [("สารระคาย: สบู่ น้ำ ตัวทำละลาย", "alcohol rub · กรด/ด่าง", "ms"),
          ("ทำลาย keratinocyte โดยตรง", "ขึ้นกับขนาด/ความถี่ — ใครก็เป็น", "bad"),
          ("ครั้งแรกก็เป็น · นาที–ชั่วโมง", "แสบ เจ็บ > คัน", "bad"),
          ("ขอบเขต = ตรงที่สัมผัส", "patch test ลบ", "sk")]
    R_ = [("Sensitization (ครั้งแรก ไม่มีผื่น)", "hapten (nickel) + โปรตีนผิว", "ms"),
          ("Langerhans → ต่อมน้ำเหลือง", "สร้าง memory T cell 10–14 วัน", "ac"),
          ("Elicitation: สัมผัสซ้ำ", "T cell กลับมา → 48–72 ชม.", "bad"),
          ("คันมาก ลามเกินขอบได้", "patch test บวก (crescendo)", "sk")]
    for col, items in ((0, L_), (1, R_)):
        x = 10 + col * 216
        prev = None
        for k, (h, s, c) in enumerate(items):
            y = 28 + k * 58
            out += [rect(x, y, 184, 46, c, 8), t(x + 92, y + 19, h, "xs b mid"), t(x + 92, y + 35, s, "xs mid i2")]
            if k:
                out.append(ar(x + 92, y - 11, x + 92, y - 2, "ln", "ah"))
    out += [rect(10, 266, 400, 48, "ac", 8),
            t(20, 284, "ICD เรื้อรัง (มือ) → patch test เสมอเพื่อตัด ACD ที่ซ้อน (สไลด์)", "xs b"),
            t(20, 302, "AD = ปัจจัยเสี่ยงหลักของ irritant hand dermatitis (barrier เสียอยู่แล้ว)", "xs")]
    return fig("Contact dermatitis — ICD “ระคาย ไม่ใช่แพ้” vs ACD “แพ้ ต้องเคยสัมผัสมาก่อน”",
               "✍️ “ระคายเคือง ไม่ใช่แพ้” · **ICD** = สารทำลายผิวโดยตรง ไม่ผ่านภูมิคุ้มกัน จึงเป็นได้ทุกคนตั้งแต่ครั้งแรก ขึ้นกับปริมาณและความถี่ (พยาบาลที่ใช้ alcohol rub บ่อย ช่างเชื่อม คนล้างจาน) — 80% ของ contact dermatitis สัมพันธ์กับอาชีพ · **ACD** = type IV delayed hypersensitivity สองระยะ: ครั้งแรก hapten จับโปรตีนผิว Langerhans cell นำไปต่อมน้ำเหลืองสร้าง memory T cell (ไม่มีผื่น) → ครั้งต่อมา T cell กลับมาที่ผิวใน 48–72 ชม. → ผื่น eczema คันมาก ลามเลยขอบได้ · ตำแหน่งบอกสาเหตุ: หัวเข็มขัด/แหวน (nickel — ✍️ “from หัวเข็มขัด”) · เปลือกตา (ยาทาเล็บ เครื่องสำอาง) · หน้าแข้งที่มี stasis (ยาทา)",
               svg(420, 320, "เปรียบเทียบกลไกผื่นระคายสัมผัสกับผื่นแพ้สัมผัสสองระยะ", *out))


# ═══════════════════════════════════════ 18 Patch test — crescendo vs decrescendo
def patch_test():
    x0, x1, y0, y1 = 50, 400, 30, 170
    days = [0, 2, 3, 4, 7]
    X = lambda d: x0 + d / 7 * (x1 - x0)
    Y = lambda v: y1 - v / 3 * (y1 - y0)
    out = [line(x0, y1, x1, y1, "ln"), line(x0, y1, x0, y0 - 6, "ln"),
           t(x0 - 6, Y(0) + 4, "0", "xs end mu"), t(x0 - 6, Y(1) + 4, "+", "xs end mu"), t(x0 - 6, Y(2) + 4, "++", "xs end mu"),
           t(x0 - 6, Y(3) + 4, "+++", "xs end mu"), t(14, y0 - 12, "ความแรงของปฏิกิริยา", "xs b")]
    for d in days:
        out += [line(X(d), y1, X(d), y1 + 4, "ln"), t(X(d), y1 + 16, "D%d" % d, "xs mid")]
    out += [t(X(0), y1 + 30, "แปะ", "xs mid i2"), t(X(2), y1 + 30, "ลอก+อ่าน", "xs mid i2"), t(X(3.6), y1 + 30, "อ่านซ้ำ", "xs mid i2"),
            t(X(7), y1 + 30, "อ่านช้า", "xs mid i2")]
    al = [(0, 0), (2, 1), (3, 2), (4, 2.6), (7, 2.2)]
    ir = [(0, 0), (2, 2.2), (3, 1.2), (4, 0.6), (7, 0.1)]
    out.append(poly([(X(d), Y(v)) for d, v in al], "lbad w3"))
    out.append(poly([(X(d), Y(v)) for d, v in ir], "lms w3 da"))
    out += [t(X(4) + 8, Y(2.6) - 6, "Allergic: crescendo", "xs b tbad"), t(X(2) - 10, Y(2.2) - 4, "Irritant: decrescendo", "xs b tms end")]
    out += [rect(10, 214, 400, 34, "sk", 8), t(210, 235, "แปะสารมาตรฐานที่หลัง 48 ชม. — ACD ขึ้นช้าและแรงขึ้น · ระคายขึ้นเร็วแล้วจางลง", "xs mid")]
    return fig("Patch test — อ่านอย่างไรให้แยก allergic จาก irritant",
               "patch test = จำลอง **elicitation phase** ของ ACD บนหลัง: แปะสารมาตรฐาน 48 ชม. แล้วอ่านที่ D2 และ D3–D4 (± D7) · ปฏิกิริยาแพ้แบบ type IV **ค่อย ๆ แรงขึ้น (crescendo)** เพราะ T cell ต้องใช้เวลาเดินทางมา ส่วนปฏิกิริยาระคาย **แรงตอนลอกแล้วจางลง (decrescendo)** · ภาพสไลด์ (Fig 13-8) แสดงผล patch test บวกหลายตำแหน่ง และสารที่ก่อโรคบางตัวไม่อยู่ในชุดคัดกรองมาตรฐาน · รายละเอียดการอ่านเป็นข้อมูลเสริม (**ไม่อยู่ในสไลด์**)",
               svg(420, 254, "กราฟความแรงของปฏิกิริยาแพทช์เทสต์ตามวัน เปรียบเทียบแบบแพ้กับแบบระคาย", *out))


# ═══════════════════════════════════════ 19 Urticaria — mast cell → wheal และ flare
def urt_mast():
    W = 250
    p, L = _skin(10, 54, W, sc=3, ep=15, de=78, sub=14, bump=_plateau(90, 160, 7))
    out = [t(135, 14, "wheal (ซีด/นูน) ล้อมด้วย flare (แดง)", "xs b mid")]
    out += p
    # flare zones
    out += [line(10 + 40, L["top"](40) - 4, 10 + 82, L["top"](82) - 4, "lbad w5"), line(10 + 168, L["top"](168) - 4, 10 + 210, L["top"](210) - 4, "lbad w5"),
            t(10 + 61, 32, "flare", "xs mid tbad b"), t(10 + 189, 32, "flare", "xs mid tbad b"), t(135, 36, "wheal", "xs mid twa b")]
    # oedema
    out.append(ell(135, L["dej"](125) + 16, 44, 13, "wa"))
    # venule
    vy = L["dej"](125) + 46
    out += [ell(135, vy, 26, 8, "bad"), t(135, vy + 3, "venule", "xs mid")]
    for dx in (-14, 0, 14):
        out.append(ar(135 + dx, vy - 9, 135 + dx * 1.6, vy - 24, "lwa w2", "ah-wa"))
    # mast cell
    mx, my = 62, vy - 6
    out += [circ(mx, my, 13, "ac")] + _dots([(mx - 5, my - 4), (mx + 4, my - 6), (mx - 2, my + 5), (mx + 6, my + 3), (mx - 7, my + 2)], 2, "inkf")
    out += [t(mx, my - 18, "mast cell", "xs mid b"), ar(mx + 14, my, 106, vy - 2, "lac w2", "ah-ac"), t(100, vy + 18, "histamine", "xs mid tac")]
    # sensory nerve axon reflex
    out.append(path("M200 %s C 214 %s 222 %s 214 %s" % (L["de_bot"] - 6, L["de_bot"] - 30, L["dej"](210) + 18, L["dej"](210) + 4), "lms w2"))
    out += [t(256, L["de_bot"] - 5, "ประสาท: คัน · axon reflex", "xs tms end")]
    # right column
    R = [("Allergic (type I)", "allergen + IgE บน mast cell", "ac"),
         ("Non-allergic (ตรง)", "aspirin · NSAID · opiate\nvancomycin · cipro\npolymyxin · rifampicin", "ms"),
         ("Chronic spontaneous", "autoantibody ต่อ IgE/FcεRI", "sk")]
    y = 18
    out.append(t(340, 12, "อะไรกระตุ้น mast cell", "xs b mid"))
    for h, d, c in R:
        n = d.count("\n")
        hh = 40 + 13 * n
        out += [rect(274, y, 138, hh, c, 8), t(282, y + 16, h, "xs b")]
        for k, ln in enumerate(d.split("\n")):
            out.append(t(282, y + 31 + 13 * k, ln, "xs i2"))
        y += hh + 6
    out += [rect(10, 200, 402, 80, "sk", 8),
            t(20, 218, "histamine → H1 บน endothelium → รอยต่อเปิด → plasma รั่ว = wheal", "xs"),
            t(20, 234, "(น้ำที่บวมกดหลอดเลือดตรงกลาง จึงซีดกลาง)", "xs i2"),
            t(20, 250, "ปลายประสาทส่งสัญญาณย้อน (axon reflex) → arteriole รอบ ๆ ขยาย = flare แดง", "xs"),
            t(20, 268, "histamine ถูกทำลายเร็ว + lymphatic ดูดน้ำกลับ → แต่ละวงหายใน < 24 ชม.", "xs b")]
    return fig("Wheal and flare — ทำไมลมพิษนูน แดงรอบ คัน และหายเองภายในวันเดียว",
               "สไลด์ (Urticaria: pathophysiology): mast cell เป็นแหล่ง histamine หลักในผิว · **allergic** = allergen จับ IgE บนผิว mast cell → degranulation · **non-allergic** = สารกระตุ้น mast cell โดยตรง (aspirin, NSAID, opiate, ciprofloxacin, polymyxin, rifampicin, vancomycin, neuropeptide) → capillary/venule รั่วเฉพาะที่ · ✍️ “บวมจาก dermis” · ลมพิษเรื้อรังชนิด spontaneous ส่วนหนึ่งเกิดจาก autoantibody ต่อ IgE หรือ FcεRI (ข้อมูลเสริม) · ความ “ชั่วคราว” เป็นลักษณะสำคัญที่สุด: ถ้าวงเดียวอยู่นาน > 24–48 ชม. เจ็บมากกว่าคัน หรือหายแล้วทิ้งรอยช้ำ ให้คิดถึง **urticarial vasculitis** และพิจารณาตัดชิ้นเนื้อ",
               svg(420, 286, "ภาพตัดขวางผิวหนังแสดง mast cell หลั่ง histamine ทำให้เกิดวงนูนลมพิษและวงแดงรอบ", *out))


# ═══════════════════════════════════════ 20 Urticaria vs angioedema
def urt_vs_angio():
    out = [t(105, 16, "Urticaria (wheal)", "sm b mid"), t(315, 16, "Angioedema", "sm b mid")]
    p, L = _skin(12, 42, 186, sc=3, ep=14, de=44, sub=20, bump=_plateau(66, 120, 6))
    out += p
    out.append(ell(105, L["dej"](93) + 9, 30, 7, "wa"))
    p, L2 = _skin(222, 42, 186, sc=3, ep=14, de=44, sub=20, bump=_dome(93, 86, 9))
    out += p
    out.append(ell(315, L2["de_bot"] + 2, 80, 16, "wa"))
    rows = [("ชั้น", "dermis บน", "dermis ล่าง + ไขมัน/เยื่อบุ"),
            ("อาการ", "คันมาก", "ตึง ปวด > คัน"),
            ("ขอบ/สี", "ชัด แดง ซีดกลาง", "ไม่ชัด สีผิว/ซีด"),
            ("อยู่นาน", "แต่ละวง < 24 ชม.", "1–3 วัน (bradykinin นานกว่า)"),
            ("ที่พบ", "ที่ไหนก็ได้", "ปาก เปลือกตา ลิ้น กล่องเสียง"),
            ("อันตราย", "น้อย", "ทางเดินหายใจอุดกั้น")]
    y = 136
    for h, a, b in rows:
        out += [rect(10, y, 402, 22, "sk" if rows.index((h, a, b)) % 2 else "bx", 3), t(18, y + 15, h, "xs b"),
                t(105, y + 15, a, "xs mid"), t(315, y + 15, b, "xs mid")]
        y += 22
    out += [rect(10, y + 6, 402, 50, "ms", 8),
            t(20, y + 24, "ไม่มีลมพิษเลย → คิดถึง bradykinin: ACE inhibitor · hereditary (C1-INH↓)", "xs b"),
            t(20, y + 42, "antihistamine/steroid/adrenaline ได้ผลน้อย — ต้องหยุด ACEi / ให้ icatibant, C1-INH", "xs")]
    return fig("Urticaria vs angioedema — กลไกเดียวกัน ต่างกันที่ “ความลึก”",
               "สไลด์: urticaria = wheal คัน ขอบชัด แดง และ **evanescent** + flare · angioedema = บวมของ **deep dermis และ subcutaneous/submucosa** — **เจ็บมากกว่าคัน ขอบไม่ชัด สีซีดหรือสีผิว** · ทำไมต่างกัน: ชั้นลึกมีปลายประสาทรับความเจ็บ/ตึงมากกว่าปลายประสาทคัน และเนื้อเยื่อหลวมเก็บน้ำได้มาก lymphatic ดูดกลับช้า จึงบวมนาน 1–3 วัน · ภาพสไลด์ (Fig 38-3) มีทั้งลมพิษที่หน้า คอ ลำตัว และ angioedema รอบตา · angioedema ที่ไม่มีลมพิษเลยเป็นกลไก bradykinin (ข้อมูลเสริม **ไม่อยู่ในสไลด์**)",
               svg(420, y + 62, "ภาพตัดขวางเปรียบเทียบลมพิษกับ angioedema และตารางความแตกต่าง", *out))


# ═══════════════════════════════════════ 21 บันไดรักษา chronic urticaria
def urt_ladder():
    out = [t(118, 14, "EAACI/GA²LEN/EuroGuiDerm/APAAACI 2022", "xs b mid")]
    steps = [("1", "sgAH ขนาดปกติ (วันละ 1 เม็ด)", "cetirizine · loratadine · fexofenadine …", "ok"),
             ("2", "เพิ่ม sgAH ได้ถึง 4 เท่า", "ตัวเดิม — ไม่ผสมหลายตัว", "ok"),
             ("3", "+ Omalizumab (anti-IgE)", "300 mg SC ทุก 4 สัปดาห์", "ac"),
             ("4", "+ Cyclosporine", "ถ้า omalizumab ไม่ได้ผล", "ms")]
    gaps = ["ไม่คุมใน 2–4 สัปดาห์", "ไม่คุมใน 2–4 สัปดาห์", "ไม่คุมใน 6 เดือน"]
    y = 24
    for k, (n, h, s, c) in enumerate(steps):
        out += [rect(10, y, 216, 46, c, 8), circ(28, y + 23, 10, "inkf"), t(28, y + 27, n, "xs b mid tpa"),
                t(44, y + 19, h, "xs b"), t(44, y + 35, s, "xs i2")]
        if k < 3:
            out += [ar(118, y + 48, 118, y + 70, "ln w2", "ah"), t(126, y + 63, gaps[k], "xs i2")]
        y += 72
    out += [rect(10, y - 6, 216, 34, "bad", 8), t(118, y + 7, "กำเริบ: prednisolone สั้น ≤ 10 วัน", "xs b mid"), t(118, y + 21, "ไม่ใช้ steroid ระยะยาว", "xs mid")]
    out += [rect(240, 24, 172, 128, "sk", 8), t(326, 42, "สไลด์ (Beck 2017 · US)", "xs b mid"),
            t(248, 60, "เพิ่ม H2 blocker", "xs"), t(248, 76, "(cimetidine, ranitidine)", "xs i2"),
            t(248, 94, "เพิ่ม leukotriene antagonist", "xs"), t(248, 112, "first-gen AH ก่อนนอน", "xs"),
            t(248, 130, "(hydroxyzine, doxepin)", "xs i2"),
            t(326, 146, "2022: ไม่แนะนำเป็นขั้นมาตรฐาน", "xs mid tbad b"),
            rect(240, 162, 172, 152, "bad", 8), t(326, 180, "Acute + ทางเดินหายใจ", "xs b mid"),
            t(248, 198, "บวมลิ้น/กล่องเสียง หายใจเสียงดัง", "xs"), t(248, 214, "BP ตก → anaphylaxis", "xs"),
            t(248, 236, "Adrenaline 1 mg/mL", "xs b"), t(248, 252, "0.5 mg IM ต้นขาด้านนอก", "xs b"),
            t(248, 268, "ซ้ำได้ทุก 5–15 นาที", "xs"), t(248, 286, "(สไลด์เขียน SC 1:1000 —", "xs i2"),
            t(248, 300, "ปัจจุบันให้ IM ดูดซึมเร็วกว่า)", "xs i2")]
    return fig("บันไดรักษาลมพิษเรื้อรัง — sgAH เป็นแกน ขยับขั้นทุก 2–4 สัปดาห์",
               "สไลด์ (Chronic urticaria: treatment) ใช้แผนภาพจาก Beck LA et al. 2017 ที่เทียบแนวทาง EAACI กับ US practice parameter · แนวทาง **EAACI/GA²LEN/EuroGuiDerm/APAAACI 2022** (ฉบับปัจจุบัน — ข้อมูลเสริม) คงสามขั้นหลัก: **sgAH → เพิ่มถึง 4 เท่า → omalizumab → cyclosporine** และ **ไม่แนะนำ** H2 blocker, montelukast หรือ first-gen antihistamine เป็นขั้นมาตรฐาน (ง่วง ผลต่อการเรียน/ขับรถ) · ranitidine ถูกถอนจากตลาดปี 2020 · ✍️ ข้อ 4 Systemic drug “ให้ยากิน” · adrenaline ในสไลด์เขียน SC และเว้นขนาดไว้ — ปัจจุบันให้ **0.5 mg IM** (WAO/EAACI anaphylaxis)",
               svg(420, 344, "บันไดการรักษาลมพิษเรื้อรังสี่ขั้นตามแนวทางปี 2022 เทียบกับสไลด์ และการรักษา angioedema ที่ทางเดินหายใจ", *out))


# ═══════════════════════════════════════ 22 Genital ulcer — เจ็บหรือไม่เจ็บ
def ulcer_cmp():
    rows = [("Syphilis (chancre)", "ไม่เจ็บ · ขอบแข็ง (indurated) พื้นสะอาด", "LN โตทั้งสองข้าง แข็ง ไม่เจ็บ",
             "T. pallidum → endarteritis + lymphocyte/plasma cell ไม่มีหนอง", "syph"),
            ("Chancroid", "เจ็บมาก · นุ่ม ขอบขรุขระ เซาะใต้ หนอง", "bubo เจ็บ เป็นหนอง แตกได้",
             "H. ducreyi → neutrophil + necrosis", "chan"),
            ("Herpes (HSV)", "เจ็บ/แสบ · ตุ่มน้ำเป็นกลุ่ม → แผลตื้นหลายแผล", "LN เจ็บ (ครั้งแรก)",
             "ไวรัสในปลายประสาท → ตุ่มน้ำ · เป็นซ้ำ", "hsv"),
            ("LGV (L1–L3)", "แผลเล็ก ไม่เจ็บ หายเร็ว (มักไม่ทันเห็น)", "bubo ข้างเดียว · groove sign",
             "Chlamydia ลุกลามไปต่อมน้ำเหลือง", "lgv")]
    out = []
    y = 6
    for name, ulc, node, mech, kind in rows:
        out += [rect(10, y, 402, 74, "bx", 8)]
        cx, cy = 46, y + 40
        if kind == "syph":
            out += [ell(cx, cy, 24, 16, "ms"), ell(cx, cy, 24, 16, "ln w5"), ell(cx, cy, 13, 8, "bad")]
        elif kind == "chan":
            out += [path("M%s %s l6 -10 l7 6 l6 -9 l8 7 l5 8 l-4 9 l4 8 l-9 5 l-7 -6 l-8 7 l-8 -7 l-5 -8 Z" % (cx - 22, cy + 2), "bad"),
                    ell(cx, cy + 1, 10, 6, "msf")]
        elif kind == "hsv":
            for dx, dy in ((-10, -6), (2, -9), (12, -3), (-6, 6), (7, 7)):
                out.append(circ(cx + dx, cy + dy, 5, "bad"))
        else:
            out += [circ(cx - 14, cy - 10, 4, "bad"), ell(cx + 2, cy + 8, 13, 8, "ms"), ell(cx + 26 - 6, cy + 8, 9, 7, "ms"),
                    line(cx + 13, cy + 2, cx + 13, cy + 14, "ln w2")]
        out += [t(84, y + 18, name, "sm b"), t(84, y + 35, ulc, "xs"), t(84, y + 51, node, "xs"), t(84, y + 66, mech, "xs i2")]
        y += 80
    return fig("Genital ulcer — เจ็บหรือไม่เจ็บบอกเชื้อได้ เพราะกลไกการอักเสบต่างกัน",
               "**Chancre (syphilis)**: T. pallidum ทำให้หลอดเลือดเล็กอักเสบอุดตัน (endarteritis obliterans) และมี lymphocyte/plasma cell หนาแน่น ไม่มีหนองและไม่ค่อยหลั่งสารปวด → แผล **ไม่เจ็บ ขอบแข็งเหมือนกระดุม พื้นสะอาด** (สไลด์: firm to palpation, occasionally multiple) · **Chancroid**: H. ducreyi ดึง neutrophil มามาก เนื้อตายและเป็นหนอง → **เจ็บ นุ่ม ขอบขรุขระเซาะใต้** (✍️ “แผลริมอ่อน กดเจ็บ”) + bubo เจ็บ · **HSV**: ตุ่มน้ำเป็นกลุ่มแตกเป็นแผลตื้น แสบมาก · **LGV**: แผลแรกเล็กมากไม่เจ็บ ระยะที่ 2 เป็นต่อมน้ำเหลืองขาหนีบโตข้างเดียว เหนือและใต้ inguinal ligament = **groove sign** · donovanosis (granuloma inguinale) อยู่ในรายการสไลด์แต่ไม่มีรายละเอียด · ทุกรายที่มีแผลอวัยวะเพศ: ตรวจ syphilis serology + HIV",
               svg(420, y, "เปรียบเทียบแผลอวัยวะเพศสี่ชนิด ความเจ็บ ต่อมน้ำเหลือง และกลไก", *out))


# ═══════════════════════════════════════ 23 Syphilis natural history
def syph_timeline():
    out = [line(16, 76, 404, 76, "ln w2")]
    marks = [(16, "ติดเชื้อ"), (70, "~3 สัปดาห์\n(10–90 วัน)"), (150, "6 สัปดาห์–6 เดือน"), (250, "1 ปี"), (330, "2–20+ ปี")]
    for x, lab in marks:
        out += [line(x, 70, x, 82, "ln w2")]
        for k, ln in enumerate(lab.split("\n")):
            out.append(t(x, 95 + 12 * k, ln, "xs mid i2"))
    bars = [(52, 108, 30, "Primary", "chancre", "bad"),
            (118, 196, 30, "Secondary", "ผื่น · LN", "bad"),
            (196, 250, 34, "Early", "< 1 ปี", "ms"),
            (250, 330, 34, "Late latent", "> 1 ปี", "sk"),
            (330, 404, 30, "Tertiary", "~⅓ ไม่รักษา", "ac")]
    for a, b, yy, h, s, c in bars:
        out += [rect(a, yy - 22 + 14, b - a, 34, c, 6), t((a + b) / 2, yy - 9 + 14, h, "xs b mid"), t((a + b) / 2, yy + 5 + 14, s, "xs mid i2")]
    out.append(path("M223 22 C 223 8 157 6 157 18", "lms w2 da", "ah-ms"))
    out.append(t(232, 14, "relapse 25% ใน 1–2 ปี", "xs tms"))
    out += [rect(52, 124, 196, 26, "bad", 6), t(150, 141, "ติดต่อได้ (early syphilis) — รอยโรคเปียก", "xs mid b"),
            rect(16, 162, 192, 104, "sk", 8),
            t(24, 180, "Primary: chancre หายเอง 3–6 สัปดาห์", "xs"),
            t(24, 196, "Secondary: 3–10 สัปดาห์หลัง chancre", "xs"),
            t(24, 210, "ผื่นทั้งตัว ฝ่ามือฝ่าเท้า condyloma lata", "xs i2"),
            t(24, 226, "หายเอง 3–12 สัปดาห์ → latent", "xs"),
            t(24, 242, "Latent: ไม่มีอาการ มีแต่ serology", "xs"),
            t(24, 258, "✍️ ไม่รักษา → หาย หรือ neuro/cardio", "xs tac"),
            rect(214, 162, 198, 104, "ac", 8),
            t(222, 180, "Tertiary", "xs b"),
            t(222, 196, "Gumma: ผิว กระดูก ตับ (พังผืด)", "xs"),
            t(222, 212, "Cardiovascular: aortitis, AR, aneurysm", "xs"),
            t(222, 228, "Neurosyphilis: tabes, general paresis", "xs"),
            t(222, 248, "Neuro/ocular/otic เกิดได้ทุกระยะ", "xs b tbad"),
            t(222, 262, "(ไม่ใช่เฉพาะ tertiary)", "xs i2")]
    return fig("Syphilis natural history — โรคที่ “หายเอง” ซ้ำ ๆ จนเข้าสู่ระยะแฝง",
               "สไลด์ (Natural history of untreated syphilis): ระยะฟักตัว **10–90 วัน (เฉลี่ย 3 สัปดาห์)** → primary (chancre) → แพร่ทางกระแสเลือด **3–10 สัปดาห์หลังเกิด chancre** → secondary → **ผื่นหายเองใน 3–12 สัปดาห์** → latent (**relapse ได้ถึง 25% ใน 1–2 ปีแรก**) → **2–20 ปี** ต่อมา หาย (✍️ “หายไปเลย”) หรือเป็น tertiary (✍️ “neuro/cardio syphilis”) · แบ่ง early latent (< 1 ปี) และ late latent (> 1 ปี หรือไม่ทราบ) เพื่อเลือกขนาดยา (CDC 2021) · ช่วง early ติดต่อทางเพศได้เพราะมีรอยโรคเปียกที่มีเชื้อมาก (chancre, condyloma lata, mucous patch) · neurosyphilis/ocular/otic syphilis เกิดได้ทุกระยะ",
               svg(420, 272, "เส้นเวลาของซิฟิลิสที่ไม่ได้รักษาจากระยะแรกจนถึงระยะที่สาม", *out))


# ═══════════════════════════════════════ 24 Serology curves
def serology():
    x0, x1, y0, y1 = 46, 404, 26, 170
    out = [line(x0, y1, x1, y1, "ln"), line(x0, y1, x0, y0 - 4, "ln"), t(10, 16, "ระดับ antibody", "xs b")]
    seg = [(46, "ติดเชื้อ"), (96, "primary"), (170, "secondary"), (330, "1 ปี"), (404, "")]
    for x, lab in seg:
        out += [line(x, y1, x, y1 + 4, "ln"), t(x, y1 + 16, lab, "xs mid i2")]
    trep = [(60, 168), (90, 120), (120, 70), (160, 46), (250, 44), (330, 48), (404, 50)]
    nontrep = [(70, 168), (100, 130), (130, 78), (170, 52), (250, 56), (275, 98), (300, 130), (330, 150), (404, 156)]
    nontx = [(250, 56), (300, 80), (360, 104), (404, 110)]
    out += [path("M" + " L".join("%s %s" % p for p in trep), "lac w3"),
            path("M" + " L".join("%s %s" % p for p in nontrep), "lbad w3"),
            path("M" + " L".join("%s %s" % p for p in nontx), "lbad w2 da"),
            t(404, 22, "Treponemal (TPHA/TPPA/FTA-ABS)", "xs b tac end"), t(404, 34, "บวกตลอดชีวิต", "xs tac end"),
            t(146, 118, "Non-treponemal (RPR/VDRL)", "xs b tbad"), t(146, 132, "หลังรักษาลด ≥ 4 เท่า = ตอบสนอง", "xs tbad"),
            t(374, 98, "ไม่รักษา", "xs tbad mid"),
            ar(250, 184, 250, 172, "lok w2", "ah-ok"), t(250, 196, "รักษา (BPG)", "xs b mid tok"),
            circ(170, 52, 5, "badf")]
    out += [rect(10, 204, 196, 92, "ms", 8), t(18, 222, "Prozone (secondary)", "xs b"),
            t(18, 238, "antibody มากเกินจนไม่จับกลุ่ม", "xs"), t(18, 252, "→ RPR ลบปลอม ทั้งที่ผื่นชัด", "xs"),
            t(18, 268, "แก้: เจือจางซีรัมแล้วตรวจซ้ำ", "xs b"),
            rect(214, 204, 198, 92, "sk", 8), t(222, 222, "Serofast", "xs b"),
            t(222, 238, "รักษาถูกแล้ว RPR ไม่ลดถึงลบ", "xs"), t(222, 252, "ค้างไตเตอร์ต่ำ (≤ 1:4) คงที่", "xs"),
            t(222, 268, "ถ้าเพิ่ม ≥ 4 เท่า = ติดใหม่/ล้มเหลว", "xs b"),
            t(222, 284, "(สไลด์: หรือ neurosyphilis)", "xs i2")]
    return fig("Syphilis serology — non-treponemal ใช้ติดตามการรักษา · treponemal บวกตลอดชีวิต",
               "**Non-treponemal (RPR, VDRL)** วัด antibody ต่อ cardiolipin จากเซลล์ที่ถูกทำลาย จึง **ขึ้นลงตามการอักเสบ** — สูงสุดในระยะ secondary (sensitivity 100% ในสไลด์) ลดลงเองในระยะแฝงและ **ลด ≥ 4 เท่า (เช่น 1:32 → 1:8) หลังรักษา** ใช้ติดตามผล · **Treponemal (TPHA, TPPA, FTA-ABS, EIA)** วัด antibody ต่อตัวเชื้อ **บวกตลอดชีวิต** แม้หายแล้ว จึงใช้ยืนยัน ไม่ใช้ติดตาม · ในระยะ primary ทั้งสองแบบอาจยังลบ (RPR sens 86%) → darkfield ที่แผล (สไลด์ Fig 82.3) · prozone และ serofast เป็นข้อมูลเสริม · RPR บวกปลอม (biologic false positive): ตั้งครรภ์ SLE/APS HIV ผู้สูงอายุ ไวรัสเฉียบพลัน",
               svg(420, 302, "กราฟระดับแอนติบอดีชนิด treponemal และ non-treponemal ตามระยะของซิฟิลิสและหลังการรักษา", *out))


# ═══════════════════════════════════════ 25 Syphilis treatment by stage + JHR
def syph_tx():
    rows = [("Primary · Secondary · Early latent", "Benzathine penicillin G 2.4 MU IM ครั้งเดียว", "แพ้ (ไม่ตั้งครรภ์): doxycycline 100 mg bid 14 วัน", "ok"),
            ("Late latent · ไม่ทราบระยะ · Tertiary (ไม่ใช่ neuro)", "BPG 2.4 MU IM สัปดาห์ละครั้ง × 3 ครั้ง", "แพ้: doxycycline 100 mg bid 28 วัน", "ms"),
            ("Neurosyphilis · ocular · otic", "Aqueous penicillin G 18–24 MU/วัน IV 10–14 วัน", "BPG เข้า CSF ไม่พอ", "bad"),
            ("ตั้งครรภ์ (ทุกระยะ)", "Penicillin ตามระยะเท่านั้น — แพ้ต้อง desensitize", "ห้าม doxycycline (สไลด์)", "ac")]
    out = []
    y = 6
    for h, a, b, c in rows:
        out += [rect(10, y, 402, 52, c, 8), t(20, y + 17, h, "xs b"), t(20, y + 32, a, "xs"), t(20, y + 46, b, "xs i2")]
        y += 58
    out += [rect(10, y, 196, 120, "bad", 8), t(108, y + 18, "Jarisch–Herxheimer", "xs b mid"),
            t(18, y + 36, "เชื้อตายพร้อมกันหลังฉีดยา", "xs"), t(18, y + 50, "→ lipoprotein ของเชื้อหลุด", "xs"),
            t(18, y + 64, "→ TNF-α · IL-6 · IL-8", "xs"), t(18, y + 80, "ไข้ หนาวสั่น ปวดเมื่อย ผื่นชัดขึ้น", "xs b"),
            t(18, y + 94, "ภายใน 24 ชม. หายเองใน 24 ชม.", "xs"), t(18, y + 110, "ให้ยาลดไข้ · ไม่ใช่แพ้ยา", "xs b tok"),
            rect(214, y, 198, 120, "sk", 8), t(313, y + 18, "Partner notification", "xs b mid"),
            t(222, y + 36, "คู่นอนใน 90 วันก่อนวินิจฉัย", "xs"), t(222, y + 50, "(primary 3 เดือน + อาการ)", "xs i2"),
            t(222, y + 64, "→ ให้ BPG ทันที แม้ RPR ลบ", "xs b"), t(222, y + 80, "นานกว่า 90 วัน → ตรวจก่อน", "xs"),
            t(222, y + 94, "ตรวจ HIV + STI อื่นทุกราย", "xs"), t(222, y + 110, "นัด RPR 6 · 12 (· 24) เดือน", "xs")]
    return fig("รักษา syphilis ตามระยะ — penicillin เป็นยาหลักทุกระยะ",
               "สไลด์ (CDC Table 200-2) เน้น ✍️: **primary/secondary → benzathine penicillin G 2.4 ล้านยูนิต IM ครั้งเดียว** · แพ้ penicillin (ไม่ตั้งครรภ์) → doxycycline 100 mg bid 14 วัน · **หญิงตั้งครรภ์ห้ามใช้ doxycycline ถ้าแพ้ต้อง desensitize แล้วให้ BPG** · ติดตาม RPR ที่ 6 และ 12 เดือน (HIV: 3, 6, 9, 12, 24) คาดหวังลด 4 เท่าใน 6–12 เดือน (early latent 12–24 เดือน) · ถ้าไม่ลด → ติดใหม่ ล้มเหลว หรือ neurosyphilis · late latent, neurosyphilis และ partner notification เป็นข้อมูลจาก **CDC STI Treatment Guidelines 2021** (ไม่อยู่ในสไลด์) · BPG ออกฤทธิ์ช้าและนาน (คงระดับ ~3 สัปดาห์) เหมาะกับเชื้อที่แบ่งตัวช้ามาก (~30 ชม.)",
               svg(420, y + 126, "ตารางการรักษาซิฟิลิสตามระยะ ปฏิกิริยา Jarisch–Herxheimer และการแจ้งคู่นอน", *out))


# ═══════════════════════════════════════ 26 Gonorrhoea + DGI
def gono():
    out = [t(105, 16, "ระยะ bacteremia (พบบ่อยกว่า)", "xs b mid"), t(315, 16, "Septic arthritis เฉพาะที่", "xs b mid")]
    L_ = [("Triad (สไลด์ highlight)", "tenosynovitis · ผื่น · ปวดข้อย้ายที่"),
          ("ผิว: pustule น้อยเม็ดที่ปลายมือเท้า", "เลือดออก ศูนย์กลางตาย สีเทา"),
          ("ข้อ: ปวดย้ายที่ ไม่ค่อยมีหนอง", "hemoculture บวกได้ · ข้อมักเพาะไม่ขึ้น")]
    R_ = [("ข้อเดียว/สองสามข้อ (เข่า ข้อมือ)", "mono/pauciarticular (สไลด์ ✍️)"),
          ("น้ำไขข้อขุ่น WBC > 50,000", "เพาะเชื้อจากข้อบวกได้ ~50%"),
          ("มักไม่มีผื่น", "hemoculture มักลบ")]
    for col, items in ((0, L_), (1, R_)):
        x = 10 + col * 210
        for k, (h, s) in enumerate(items):
            y = 26 + k * 52
            out += [rect(x, y, 192, 44, "ms" if col == 0 else "bad", 8), t(x + 96, y + 18, h, "xs b mid"), t(x + 96, y + 34, s, "xs mid i2")]
    out += [rect(10, 186, 402, 56, "sk", 8),
            t(20, 204, "ผื่นเกิดจาก: เชื้อในกระแสเลือดไปติดหลอดเลือดเล็กปลายมือเท้า + immune complex", "xs"),
            t(20, 220, "→ dermal vasculitis + neutrophil · ✍️ “ผื่นป้อนหนองตาม distal organ”", "xs"),
            t(20, 236, "ตรวจ NAAT/เพาะเชื้อจากทุกช่องทาง: urethra/cervix · คอหอย · ทวารหนัก + เลือด + ข้อ", "xs b"),
            rect(10, 250, 402, 72, "ok", 8),
            t(20, 268, "Uncomplicated (CDC 2021): ceftriaxone 500 mg IM ครั้งเดียว (≥ 150 kg: 1 g)", "xs b"),
            t(20, 284, "+ doxycycline 100 mg bid 7 วัน ถ้ายังไม่ตัด chlamydia (สไลด์ยังเป็น 125 mg + azithro)", "xs"),
            t(20, 300, "DGI: ceftriaxone 1 g IV/IM ทุก 24 ชม. → ดีขึ้น 24–48 ชม. เปลี่ยนเป็นกิน รวม ≥ 7 วัน", "xs b"),
            t(20, 316, "แพ้ cephalosporin: สไลด์ spectinomycin 2 g · CDC 2021 gentamicin + azithro", "xs i2")]
    return fig("Gonorrhoea และ DGI — เชื้อตัวเดียว สองหน้าตาของข้ออักเสบ",
               "สไลด์: N. gonorrhoeae ติดเยื่อบุทางเดินปัสสาวะ-สืบพันธุ์ ทวารหนัก และคอ · Gram stain หนองจากท่อปัสสาวะชาย: **Gram-negative diplococci ใน neutrophil** · **DGI** เกิด 0.5–3% ของผู้ติดเชื้อ (✍️ “หนองใน → disseminated gonococcal infection”) — ระยะ bacteremia มี **classic triad: dermatitis, migratory polyarthritis, tenosynovitis** (ผื่นเป็น hemorrhagic vesicopustule น้อยเม็ดบนฐานแดงที่ฝ่ามือฝ่าเท้า ศูนย์กลางตาย สีเทา “gun metal gray”) ส่วน **septic arthritis จริงมักเป็นข้อเดียวหรือสองสามข้อ** · ขนาดยาในสไลด์ (ceftriaxone 125 mg + azithromycin) เป็นแนวทางเก่า → **CDC 2020/2021: ceftriaxone 500 mg IM** และให้ doxycycline ถ้ายังไม่ตัด chlamydia",
               svg(420, 328, "เปรียบเทียบการติดเชื้อหนองในแพร่กระจายระยะกระแสเลือดกับข้ออักเสบติดเชื้อ และการรักษา", *out))


# ═══════════════════════════════════════ 27 Leprosy spectrum (Ridley–Jopling)
def lepro_spectrum():
    xs = [136, 190, 244, 298, 352]
    names = ["TT", "BT", "BB", "BL", "LL"]
    out = [t(10, 14, "ภูมิคุ้มกันกำหนดหน้าตาโรค (สไลด์ Fig 75.2 · Table 75.2)", "xs b")]
    y0, y1 = 26, 120
    out += [path("M112 34 C 200 36 280 100 378 116", "lok w3"), path("M112 116 C 210 100 290 36 378 34", "lbad w3"),
            t(14, 70, "Cell-mediated", "xs b tok"), t(14, 82, "(Th1) IL-2 · IFN-γ", "xs tok"),
            t(408, 70, "เชื้อ + antibody", "xs b tbad end"), t(408, 82, "(Th2) IL-4 · IL-10", "xs tbad end"),
            line(30, 124, 410, 124, "ln")]
    for x, n in zip(xs, names):
        out += [line(x, 120, x, 128, "ln"), t(x, 142, n, "sm b mid")]
    rows = [("จำนวนผื่น", ["1–5", "น้อย+", "มาก", "มาก", "มากมาย"]),
            ("ขอบ", ["ชัดมาก", "ชัด", "กลาง ๆ", "ไม่ชัด", "เลือน"]),
            ("ความรู้สึก", ["ชา", "ชา", "ลดลง", "ลดลง", "ปกติ*"]),
            ("เชื้อในผื่น", ["ไม่พบ", "1+", "มาก", "มาก", "globi"])]
    tx = [136, 190, 244, 298, 352]
    y = 152
    for k, (h, vals) in enumerate(rows):
        out += [rect(30, y, 380, 24, "sk" if k % 2 else "bx", 3), t(36, y + 16, h, "xs b")]
        for x, v in zip(tx, vals):
            out.append(t(x, y + 16, v, "xs mid"))
        y += 24
    out.append(t(404, y + 2 + 10, "*LL: ชาตามปลายมือเท้าในระยะหลัง", "xs end i2"))
    y += 12
    out += [rect(30, y + 8, 150, 26, "ok", 6), t(105, y + 25, "PB: ≤ 5 ผื่น · smear ลบ", "xs b mid"),
            rect(186, y + 8, 224, 26, "bad", 6), t(298, y + 25, "MB: > 5 ผื่น หรือ smear บวก", "xs b mid"),
            rect(110, y + 40, 220, 22, "ms", 6), t(220, y + 55, "Type 1 reaction (borderline: BT–BL)", "xs mid b"),
            rect(270, y + 66, 140, 22, "bad", 6), t(340, y + 81, "Type 2 (ENL): BL–LL", "xs mid b")]
    return fig("Leprosy spectrum — ภูมิคุ้มกันยิ่งดี ผื่นยิ่งน้อยและชัด แต่ทำลายเส้นประสาทเร็ว",
               "สไลด์: M. leprae เป็นปรสิตในเซลล์ macrophage และ **Schwann cell** · แบ่งตามภูมิคุ้มกัน: **tuberculoid (Th1)** — granuloma คุมเชื้อได้ จึงมีผื่นน้อย ขอบชัด **ชา** และแทบไม่พบเชื้อ · **lepromatous (Th2)** — คุมเชื้อไม่ได้ เชื้อเต็มผิวหนังและน้ำมูก ผื่นมาก สมมาตร ขอบไม่ชัด ความรู้สึกยังปกติในระยะแรก (เส้นประสาทถูกทำลายช้าแต่กว้าง) · กลุ่ม borderline ไม่คงที่ จึงเกิด **type 1 reaction** (ภูมิเปลี่ยนเร็ว เส้นประสาทอักเสบเฉียบพลัน) ส่วน **type 2 (erythema nodosum leprosum)** เป็น immune complex ใน BL–LL · การแบ่ง PB/MB ของ WHO ใช้เลือกสูตรยา (ภาพสไลด์ใช้ > 5 ผื่น = MB)",
               svg(420, y + 94, "สเปกตรัมของโรคเรื้อนจาก tuberculoid ถึง lepromatous เทียบภูมิคุ้มกัน จำนวนผื่น ความรู้สึก และเชื้อ", *out))


# ═══════════════════════════════════════ 28 Leprosy — ทำไมผื่นชาและเส้นประสาทโต
def lepro_nerve():
    out = [t(100, 14, "เส้นประสาทส่วนปลาย (ตัดขวาง)", "xs b mid")]
    out += [circ(100, 92, 64, "bx"), circ(100, 92, 64, "ln w2")]
    fas = [(74, 70), (122, 66), (100, 108), (64, 112), (136, 110)]
    for k, (fx, fy) in enumerate(fas):
        out.append(circ(fx, fy, 16, "ms"))
        out.append(circ(fx, fy, 4, "inkf"))
    out += [ell(108, 86, 30, 22, "bad"), t(108, 90, "granuloma", "xs mid b")]
    out += _dots([(84, 70, ), (90, 104), (118, 102), (128, 76)], 2, "badf")
    out += [t(100, 172, "บวม + พังผืด → คลำได้โต แข็ง", "xs mid b"), t(100, 186, "✍️ “มี nerve trunk enlargement”", "xs mid tac")]
    A = (310, 24, 100, 18)
    B = (310, 76, 100, 24)
    C = (310, 136, 100, 24)
    D = (310, 196, 100, 24)
    out += _node(*A, "sk", "M. leprae ชอบที่เย็น 27–30 °C")
    out += _node(*B, "ms", "เข้าสู่ Schwann cell (PGL-1)", "ผิว จมูก เส้นประสาทใกล้ผิว")
    out += _node(*C, "bad", "ปลายประสาทเล็กในผื่นถูกทำลาย", "ร้อน–เย็นหายก่อน → เจ็บ → สัมผัส")
    out += _node(*D, "bad", "Autonomic + motor เสีย", "เหงื่อไม่ออก ผิวแห้ง · มือเท้าผิดรูป")
    out += [_link(A, B), _link(B, C), _link(C, D)]
    out += [rect(10, 232, 402, 76, "sk", 8),
            t(20, 250, "คลำ: ulnar (ข้อศอก) · common peroneal (คอกระดูก fibula) · great auricular (คอ)", "xs"),
            t(20, 266, "radial cutaneous (ข้อมือ) · posterior tibial · median (สไลด์ Fig 75.3)", "xs"),
            t(20, 284, "ผลตามมา: claw hand (ulnar+median) · foot drop · lagophthalmos · แผลฝ่าเท้า", "xs b"),
            t(20, 300, "นิ้วสั้น (กระดูกถูกดูดซึมจากแผล/ติดเชื้อซ้ำ ไม่ใช่เชื้อกินนิ้ว)", "xs i2")]
    return fig("Leprosy — ทำไมผื่น “ชา” และเส้นประสาท “โต”",
               "M. leprae แบ่งตัวช้ามาก (~12–14 วัน) และชอบอุณหภูมิต่ำกว่าแกนกาย จึงอยู่ที่ **ผิว จมูก ใบหู และเส้นประสาทที่วิ่งใกล้ผิว** · เชื้อจับ laminin-α2 บน Schwann cell (ผ่าน PGL-1) แล้วเข้าไปอาศัย → ร่างกายสร้าง granuloma ในเส้นประสาท (TT) หรือมีเชื้อจำนวนมาก (LL) → **เส้นประสาทบวม หนา คลำได้** และถูกบีบในช่องกระดูก–พังผืด → **ปลายประสาทเล็กในผื่นถูกทำลาย** ความรู้สึกร้อน–เย็นหายก่อน แล้วเจ็บและสัมผัส = **anaesthetic patch** · เส้นประสาท autonomic เสีย → เหงื่อไม่ออก ผิวแห้ง (acquired ichthyosis) · motor เสีย → claw hand, foot drop, lagophthalmos (ภาพ sequelae ในสไลด์) · cardinal signs ของ WHO = ผื่นซีด/แดงที่ชาชัด + เส้นประสาทโต/ชา/อ่อนแรง + smear บวก (ข้อมูลเสริม)",
               svg(420, 314, "ภาพตัดขวางเส้นประสาทที่มี granuloma และลำดับกลไกที่ทำให้ผื่นโรคเรื้อนชา", *out))


# ═══════════════════════════════════════ 29 EM vs SJS/TEN — target lesions + BSA
def em_sjs():
    out = [t(10, 14, "ชนิดของ target lesion", "xs b")]
    # typical
    cx = 60
    out += [circ(cx, 60, 30, "bad"), circ(cx, 60, 20, "bx"), circ(cx, 60, 10, "badf"),
            t(cx, 106, "Typical", "xs b mid"), t(cx, 119, "3 วง นูน ขอบชัด", "xs mid"), t(cx, 132, "EM (ปลายมือเท้า)", "xs mid tok b")]
    cx = 170
    out += [circ(cx, 60, 28, "bad"), circ(cx, 60, 13, "badf"),
            t(cx, 106, "Atypical raised", "xs b mid"), t(cx, 119, "2 วง ขอบไม่ชัด", "xs mid"), t(cx, 132, "EM", "xs mid tok b")]
    cx = 290
    out += [path("M%s 36 C %s 30 %s 52 %s 62 C %s 80 %s 92 %s 86 C %s 90 %s 70 %s 60 C %s 44 %s 34 %s 36 Z" % (
        cx - 6, cx + 20, cx + 30, cx + 28, cx + 26, cx + 8, cx - 8, cx - 26, cx - 32, cx - 28, cx - 28, cx - 18, cx - 6), "bad"),
            ell(cx, 62, 13, 10, "badf"), ell(cx + 4, 58, 7, 5, "wa"),
            t(cx, 106, "Atypical flat (dusky)", "xs b mid"), t(cx, 119, "แบน ม่วงคล้ำ ± ตุ่มน้ำกลาง", "xs mid"), t(cx, 132, "SJS/TEN (ลำตัว หน้า)", "xs mid tbad b")]
    out += [t(10, 152, "พื้นที่ผิวหนังลอก (% BSA) — สไลด์ Table 20.4", "xs b")]
    x0, x1 = 30, 400
    X = lambda v: x0 + v / 100 * (x1 - x0)
    out += [rect(X(0), 172, X(10) - X(0), 30, "ms", 4), rect(X(10), 172, X(30) - X(10), 30, "bad", 4), rect(X(30), 172, X(100) - X(30), 30, "badf", 4),
            t((X(0) + X(10)) / 2, 222, "SJS", "xs b mid"), t((X(0) + X(10)) / 2, 235, "< 10%", "xs mid"),
            t((X(10) + X(30)) / 2, 191, "overlap", "xs b mid"), t((X(10) + X(30)) / 2, 222, "10–30%", "xs mid"),
            t((X(30) + X(100)) / 2, 191, "TEN > 30%", "sm b mid tpa"),
            t(X(30) + 10, 222, "ตาย SJS 1–5% · TEN 25–35% (สไลด์)", "xs b tbad")]
    for v in (0, 10, 30, 100):
        out.append(t(X(v), 168, "%d" % v, "xs mid mu"))
    out += [rect(10, 246, 402, 62, "ok", 8),
            t(20, 264, "EM ไม่ได้อยู่บนเส้นนี้: เกิดหลัง HSV/Mycoplasma (90% ติดเชื้อ) · ผื่นขึ้นใน 24 ชม.", "xs"),
            t(20, 280, "typical target ที่ปลายมือเท้า · EM major มีเยื่อบุ แต่ “ไม่ลุกลามเป็น TEN” (สไลด์)", "xs b"),
            t(20, 296, "SJS/TEN = ยาเป็นสาเหตุหลัก · เริ่ม 4–28 วันหลังได้ยา · ผื่นแบนคล้ำที่ลำตัว", "xs")]
    return fig("EM vs SJS/TEN — ดูรูปร่าง target และพื้นที่ที่ลอก",
               "สไลด์ (Atypical target lesions in SJS vs typical target lesions in EM): **typical target** มี ≥ 3 วงชัด (กลางคล้ำ/ตุ่มน้ำ → วงซีดบวม → วงแดงนอก) นูน อยู่ที่ปลายมือเท้า (acral) = **EM** ซึ่งส่วนใหญ่ตามหลัง **HSV** · **atypical flat (dusky) macule** รูปร่างไม่สม่ำเสมอ ม่วงคล้ำ มักมีตุ่มน้ำตรงกลาง เริ่มที่ **ลำตัวและหน้า** = **SJS/TEN** ซึ่งมีสาเหตุหลักจาก **ยา** · แบ่งตามพื้นที่ที่ลอก (นับเฉพาะผิวที่ลอกหรือลอกได้ ไม่นับผื่นแดง): SJS < 10% · overlap 10–30% · TEN > 30% · เยื่อบุถูกเป็นใน ~80–90% ของ SJS/TEN",
               svg(420, 314, "ชนิดของ target lesion และแถบพื้นที่ผิวหนังลอกที่แบ่ง SJS overlap และ TEN", *out))


# ═══════════════════════════════════════ 30 SJS/TEN — ทำไม epidermis ลอกทั้งแผ่น
def sjs_mech():
    out = [t(105, 14, "keratinocyte ตายทั้งชั้น", "xs b mid")]
    p, L = _skin(10, 50, 190, sc=3, ep=22, de=44, sub=12, bump=_plateau(60, 150, 12))
    out += p
    base = 50 + 3 + 22 + 1.5
    us = list(range(56, 156, 3))
    out.append(poly([(10 + u, L["dej"](u)) for u in us] + [(10 + u, base) for u in reversed(us)], "wa", closed=True))
    for k in range(9):
        u = 64 + k * 10
        out.append(circ(10 + u, L["sc"](u) + 10 + (k % 2) * 4, 3, "inkf"))
    out += _dots([(40, L["de_bot"] - 14), (60, L["de_bot"] - 22), (150, L["de_bot"] - 18), (175, L["de_bot"] - 12)], 3, "badf")
    out += [t(105, L["de_bot"] + 26, "ผิวลอกที่รอยต่อ (DEJ)", "xs mid b"), t(105, L["de_bot"] + 40, "dermis ยังอยู่ → Nikolsky +", "xs mid"),
            t(105, L["de_bot"] + 54, "“wet cigarette paper”", "xs mid i2")]
    A = (316, 24, 96, 18)
    B = (316, 76, 96, 24)
    C = (316, 136, 96, 24)
    D = (316, 196, 96, 24)
    out += _node(*A, "ms", "ยา + HLA (เช่น HLA-B1502)")
    out += _node(*B, "ac", "CD8 T cell/NK เฉพาะยาแบ่งตัว", "ใช้เวลา 4–28 วัน (ครั้งแรก)")
    out += _node(*C, "bad", "Granulysin · FasL · perforin", "สั่ง keratinocyte apoptosis")
    out += _node(*D, "bad", "ผิว + เยื่อบุลอกเหมือนไฟไหม้", "เสียน้ำ ติดเชื้อ อุณหภูมิตก")
    out += [_link(A, B), _link(B, C), _link(C, D)]
    out += [rect(10, 232, 402, 62, "sk", 8),
            t(20, 250, "ยาเสี่ยงสูง (สไลด์ Table 20.6): allopurinol · carbamazepine · phenytoin · lamotrigine", "xs"),
            t(20, 266, "sulfonamide/TMP-SMX · nevirapine · oxicam NSAID · aminopenicillin · barbiturate", "xs"),
            t(20, 282, "คนไทย: HLA-B1502 → carbamazepine · HLA-B5801 → allopurinol", "xs b")]
    return fig("SJS/TEN — ทำไมหนังกำพร้าหลุดทั้งแผ่นทั้งที่ dermis ยังดี",
               "ยาหรือเมแทบอไลต์จับกับ HLA บางชนิด (เช่น **HLA-B1502** กับ carbamazepine ในคนไทย/เอเชีย) → กระตุ้น **CD8 T cell และ NK cell** ที่จำเพาะต่อยา ซึ่งต้องใช้เวลาแบ่งตัว จึงเกิดอาการ **4–28 วันหลังเริ่มยา** (สไลด์) → หลั่ง **granulysin** (ตัวหลัก ระดับสัมพันธ์กับความรุนแรง) **FasL** และ perforin/granzyme → keratinocyte ตายแบบ apoptosis **ทั้งความหนา** → หนังกำพร้าแยกจาก dermis ที่รอยต่อ → ตุ่มน้ำหย่อน ผิวลอกเป็นแผ่น และ **Nikolsky sign** · เยื่อบุ (ตา ปาก อวัยวะเพศ) เป็นเหมือนกัน · ผลทางระบบเหมือนแผลไฟไหม้ · กลไกโมเลกุลเป็นข้อมูลเสริม (**ไม่อยู่ในสไลด์**)",
               svg(420, 300, "ภาพตัดขวางผิวหนังที่หนังกำพร้าตายทั้งชั้นและลอกออก และลำดับกลไกจากยาถึงผิวลอก", *out))


# ═══════════════════════════════════════ 31 SCORTEN
def scorten():
    items = ["อายุ > 40 ปี", "HR > 120 /นาที", "มะเร็ง/มะเร็งเม็ดเลือด", "ผิวลอกวันแรก > 10%",
             "Urea > 10 mmol/L (BUN > 28)", "HCO3 < 20 mmol/L", "Glucose > 14 mmol/L (> 252)"]
    out = [rect(10, 6, 186, 22 + 20 * len(items), "sk", 8), t(103, 22, "1 คะแนนต่อข้อ (วันที่ 1–3)", "xs b mid")]
    for k, it in enumerate(items):
        out += [circ(24, 40 + 20 * k, 6, "inkf"), t(24, 43 + 20 * k, str(k + 1), "xs mid tpa b"), t(36, 44 + 20 * k, it, "xs")]
    data = [("0–1", 3.2), ("2", 12.1), ("3", 35.8), ("4", 58.3), ("≥5", 90)]
    x0, y0, y1 = 214, 20, 150
    bw = 34
    out += [line(x0, y1, 410, y1, "ln"), t(312, 14, "อัตราตาย (%) ตามคะแนน (สไลด์)", "xs b mid")]
    for k, (lab, v) in enumerate(data):
        x = x0 + 8 + k * (bw + 4)
        h = v / 100 * (y1 - y0)
        c = "ok" if v < 10 else ("ms" if v < 40 else "bad")
        out += [rect(x, y1 - h, bw, h, c, 3), t(x + bw / 2, y1 - h - 4, "%g" % v, "xs b mid"), t(x + bw / 2, y1 + 14, lab, "xs mid")]
    out += [t(312, y1 + 30, "คะแนน SCORTEN", "xs mid i2"),
            rect(10, 194, 402, 60, "bad", 8),
            t(20, 212, "จัดการ (สไลด์ Fig 20.15): หยุดยาที่สงสัยทุกตัวทันที → ICU/หอผู้ป่วยไฟไหม้", "xs b"),
            t(20, 228, "สารน้ำ เกลือแร่ อาหาร · ดูแลตา (จักษุแพทย์) ปาก อวัยวะเพศ · ป้องกันติดเชื้อ", "xs"),
            t(20, 244, "IVIG/cyclosporine/steroid = หลักฐานไม่แน่น · เพาะเชื้อเป็นระยะ ไม่ให้ยาฆ่าเชื้อป้องกัน", "xs i2")]
    return fig("SCORTEN — 7 ข้อ ทำนายอัตราตายของ SJS/TEN",
               "สไลด์ (Table 20.7 SCORTEN) ให้ 1 คะแนนต่อข้อ: อายุ > 40 · ชีพจร > 120 · มะเร็ง · ผิวลอกวันแรก > 10% · urea > 10 mmol/L · bicarbonate < 20 mmol/L · glucose > 14 mmol/L → อัตราตาย 0–1 = 3.2% · 2 = 12.1% · 3 = 35.8% · 4 = 58.3% · ≥ 5 = 90% · ทุกข้อสะท้อนว่า “ร่างกายรับภาระแบบแผลไฟไหม้ไม่ไหว” (เสียน้ำ → urea สูง · catabolic/stress → glucose สูง · hypoperfusion → HCO3 ต่ำ) · คิดคะแนนภายใน 24 ชม. แรกและวันที่ 3 · ค่า BUN/glucose หน่วย mg/dL เป็นการแปลงหน่วยเพิ่มเติม",
               svg(420, 260, "เกณฑ์เจ็ดข้อของ SCORTEN และแผนภูมิแท่งอัตราตายตามคะแนน", *out))


# ═══════════════════════════════════════ 32 Erythema nodosum — septal panniculitis
def en():
    out = [t(100, 14, "Septal panniculitis (EN)", "xs b mid"), t(318, 14, "Lobular + vasculitis", "xs b mid")]

    def block(x, septal):
        p, L = _skin(x, 26, 188, sc=3, ep=12, de=26, sub=0, bump=_dome(94, 70, 6))
        o = list(p)
        top = L["de_bot"]
        o.append(rect(x, top, 188, 96, "bad" if septal else "sk", 0))
        g = 9 if septal else 3
        cw, chh = (188 - 5 * g) / 4, (96 - 4 * g) / 3
        for r_ in range(3):
            for c_ in range(4):
                lx, ly = x + g + c_ * (cw + g), top + g + r_ * (chh + g)
                inflamed = (not septal) and r_ <= 1 and 1 <= c_ <= 2
                o.append(rect(lx, ly, cw, chh, "ms" if inflamed else "bx", 7))
                if inflamed:
                    o += _dots([(lx + 8 + (k % 3) * 10, ly + 7 + (k // 3) * 9) for k in range(6)], 2, "badf")
        if septal:
            for c_ in range(1, 4):
                sx = x + c_ * (cw + g) + g / 2
                o += _dots([(sx, top + 14), (sx, top + 44), (sx, top + 76)], 2.4, "badf")
            for r_ in range(1, 3):
                sy = top + r_ * (chh + g) + g / 2
                o += _dots([(x + 26, sy), (x + 162, sy)], 2.4, "badf")
            o += [circ(x + 2 * (cw + g) + g / 2, top + chh + g + chh / 2 + 4, 6, "ac"), t(x + 94, top + 112, "septa หนา อักเสบ · Miescher granuloma", "xs mid tbad")]
        else:
            o += [ell(x + 2 * (cw + g) + g / 2, top + chh + g / 2, 8, 5, "badf"), t(x + 94, top + 112, "ไขมันตาย ± vasculitis → แตกเป็นแผล", "xs mid tbad")]
        return o
    out += block(10, True)
    out += block(222, False)
    out += [rect(10, 252, 402, 98, "bx", 8),
            t(20, 270, "ทำไมกดเจ็บ: septa มีหลอดเลือดและเส้นประสาท อักเสบบวมดึงรั้ง", "xs"),
            t(20, 286, "ทำไมไม่แตก/ไม่เป็นแผลเป็น: อักเสบที่ septa · ไม่มี vasculitis · ไขมันไม่ตาย", "xs"),
            t(20, 302, "ทำไมเหมือนรอยช้ำ: RBC รั่ว → hemoglobin สลาย แดง → ม่วง → เขียวเหลือง", "xs"),
            t(20, 320, "erythema induratum (TB) / ENL (เรื้อน) = lobular ± vasculitis → อาจแตก", "xs i2"),
            t(20, 338, "สาเหตุ: strep · TB · sarcoid · IBD · ยา (OCP, sulfa) · ตั้งครรภ์ · idiopathic 37–60%", "xs b")]
    return fig("Erythema nodosum — อักเสบที่ “ผนังกั้น” ของไขมัน จึงเจ็บแต่ไม่แตก",
               "สไลด์ (Panniculitis) วงชั้น “fat” ในภาพผิวหนังเพื่อบอกว่าโรคอยู่ที่ชั้นไขมัน · **EN** = **septal panniculitis** ไม่มี vasculitis (ภาพ histology ในสไลด์: septa หนาขึ้น มี multinucleated giant cell และ **Miescher’s radial granuloma**) → nodule แดง **กดเจ็บ** สมมาตรที่หน้าแข้ง **ไม่แตก ไม่เป็นแผลเป็น** อยู่ 3–6 สัปดาห์ ผื่นใหม่ขึ้นได้ถึง 6 สัปดาห์ พบในหญิงมากกว่า มีไข้ ปวดข้อร่วม · เทียบกับ panniculitis แบบ lobular ± vasculitis (erythema induratum จาก TB, ENL ในเรื้อน) ที่ไขมันตายจึงแตกเป็นแผลได้ · รักษา: หาสาเหตุ + นอนพัก ยกขา aspirin/NSAID",
               svg(420, 356, "ภาพตัดขวางชั้นไขมันเปรียบเทียบการอักเสบที่ผนังกั้นใน erythema nodosum กับการอักเสบในก้อนไขมัน", *out))
