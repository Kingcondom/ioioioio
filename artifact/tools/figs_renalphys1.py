# -*- coding: utf-8 -*-
"""ภาพประกอบคาบ nephro Physio1 — สรีรวิทยาไตพื้นฐาน I (Watchara Chongsa PhD) — ใช้ใน build_renalphys1.py

ทุกฟังก์ชันคืน fig(title, cap, svg) · กว้าง ≤ 420 · ภาพเซลล์ท่อไต: ลูเมนซ้าย · เซลล์กลาง · เลือดขวา (ทุกภาพเหมือนกัน)"""
import math
from svg import *


def _x(cx, cy, r=6):
    return line(cx - r, cy - r, cx + r, cy + r, "lbad w3") + line(cx - r, cy + r, cx + r, cy - r, "lbad w3")


def _frame(y0, y1, cell="เซลล์", lumen="ลูเมน", blood="เลือด", gap=None):
    """กรอบเซลล์ท่อไต: ลูเมน 10–100 · เซลล์ 116–304 · เลือด 320–410 · gap = (y_top, y_bottom) ช่องระหว่างเซลล์"""
    out = [rect(10, y0, 90, y1 - y0, "wa", 6), t(55, y0 + 18, lumen, "sm b mid twa"),
           rect(320, y0, 90, y1 - y0, "bad", 6), t(365, y0 + 18, blood, "sm b mid tbad")]
    if gap:
        out += [rect(116, y0, 188, gap[0] - y0, "bx", 6), rect(116, gap[1], 188, y1 - gap[1], "bx", 6)]
    else:
        out += [rect(116, y0, 188, y1 - y0, "bx", 6)]
    out += [t(210, y0 + 18, cell, "sm b mid")]
    return out


def _in(y, lab, cls="lok", m="ah-ok", lc="xs mid b"):
    """ลูกศรลูเมน → เซลล์ (ป้ายเหนือเส้นในลูเมน)"""
    return [line(18, y, 106, y, cls + " w2", m), t(58, y - 5, lab, lc)]


def _out(y, lab, cls="lms", m="ah-ms", lc="xs mid b"):
    """ลูกศรเซลล์ → ลูเมน"""
    return [line(106, y, 18, y, cls + " w2", m), t(58, y - 5, lab, lc)]


def _bl(y, lab, cls="lok", m="ah-ok", lc="xs mid b", rev=False):
    """ลูกศรเซลล์ → เลือด (rev = เลือด → เซลล์)"""
    if rev:
        return [line(402, y, 316, y, cls + " w2", m), t(362, y - 5, lab, lc)]
    return [line(314, y, 402, y, cls + " w2", m), t(362, y - 5, lab, lc)]


# ═══════════════════════════════════════ 1 หน้าที่ของไต 7 ข้อ → ไตเสียแล้วเกิดอะไร
def functions():
    rows = [("1 ขับของเสียไนโตรเจน", "creatinine · urea · uric acid", "azotemia → คลื่นไส้ อ่อนเพลีย", "ตะคริว · uric สูง → gout", "bad"),
            ("2 ขับยาและสารแปลกปลอม", "กรอง + หลั่งที่ PT", "renal drug clearance ↓", "→ ยาสะสมเป็นพิษ", "ms"),
            ("3 สมดุลเกลือแร่", "ขับ Na K Mg Pi ส่วนเกิน · เก็บ Ca", "Na คั่ง → บวม ความดันสูง", "K สูง → หัวใจเต้นผิดจังหวะ", "bad"),
            ("4 สมดุลน้ำและ osmolality", "ขับน้ำเกิน · เก็บน้ำเมื่อขาด", "ขับน้ำไม่ได้", "→ น้ำเกิน บวม ความดันสูง", "wa"),
            ("5 ต่อมไร้ท่อ", "renin · EPO · 1α-hydroxylase · PG", "EPO ↓ → ซีด · calcitriol ↓", "→ Ca ↓ PTH ↑ → กระดูกเสื่อม", "ms"),
            ("6 สมดุลกรด–ด่าง", "หลั่ง H⁺ · ดูดกลับ/สร้าง HCO₃⁻", "กรดคั่ง", "→ metabolic acidosis", "bad"),
            ("7 Gluconeogenesis", "glutamine ใน PT (คู่กับ NH₄⁺)", "สำคัญตอนอดอาหาร", "และภาวะกรด", "sk")]
    out = [t(105, 18, "หน้าที่ (ไตปกติ)", "sm b mid tac"), t(315, 18, "เมื่อไตเสีย", "sm b mid tbad")]
    y = 28
    for a, b, c, d, cl in rows:
        out += [rect(10, y, 190, 42, "ac", 7), t(18, y + 17, a, "sm b"), t(18, y + 33, b, "xs i2"),
                ar(202, y + 21, 218, y + 21, "lbad", "ah-bad"),
                rect(220, y, 190, 42, cl, 7), t(228, y + 17, c, "xs b"), t(228, y + 33, d, "xs")]
        y += 48
    return fig("หน้าที่ 7 ข้อของไต — และอาการที่ตามมาเมื่อหน้าที่นั้นหายไป",
               "สไลด์สอนหน้าที่ของไตคู่กับ **\"Decreased renal function:\"** ทุกข้อ — จำแบบนี้แล้วอาการของ CKD/AKI จะเดาได้เอง: ของเสียคั่ง (uremic symptoms) · ยาที่ขับทางไตสะสม · Na/น้ำคั่ง (บวม ความดันสูง) · K สูง (หัวใจ) · Pi สูง · EPO ต่ำ (ซีด) · calcitriol ต่ำ → Ca ต่ำ → PTH สูง → **renal osteodystrophy** · กรดคั่ง (metabolic acidosis) · ไตยังสร้างกลูโคสจาก glutamine ใน PT ได้ด้วย",
               svg(420, 366, "หน้าที่เจ็ดข้อของไตและผลที่เกิดเมื่อไตเสียแต่ละหน้าที่", *out))


# ═══════════════════════════════════════ 2 afferent vs efferent — ใครหดตัวไหน
def arterioles():
    def tube(x1, x2, y, h):
        return rect(x1, y - h / 2, x2 - x1, h, "bad", h / 2)
    out = [
        box(10, 10, 190, 74, "bad", "afferent หด → RBF ↓ GFR ↓\nNE/E (α1) ★ · adenosine (A1)\nATP (P2X) · sympathetic", fs=11),
        box(220, 10, 190, 74, "bad", "efferent หด → RBF ↓\nแต่ PGC ↑ → GFR คงไว้\nangiotensin II ★ (ไวกว่า aff.)", fs=11),
        tube(20, 160, 132, 18), t(90, 136, "afferent", "xs b mid"),
        circ(200, 132, 34, "bad"), path("M180 120 q10 -16 20 0 q10 16 20 0 M178 140 q11 14 22 0 q11 -14 22 0", "lbad"),
        t(200, 178, "glomerulus", "xs b mid"),
        tube(240, 400, 132, 12), t(320, 136, "efferent", "xs b mid"),
        line(90, 86, 90, 120, "lbad da", "ah-bad"), line(320, 86, 320, 124, "lbad da", "ah-bad"),
        line(90, 196, 90, 144, "lok da", "ah-ok"), line(320, 196, 320, 140, "lok da", "ah-ok"),
        box(10, 198, 190, 74, "ok", "afferent ขยาย → RBF ↑ GFR ↑\nPGE₂ · PGI₂ ★ · ANP\nbradykinin · kinin", fs=11),
        box(220, 198, 190, 74, "ok", "efferent ขยาย → RBF ↑\nPGC ↓ → GFR ↓\n(ACEi/ARB ตัด AII ออก)", fs=11),
        box(10, 284, 400, 34, "ms", "หดทั้งสองเส้น (RBF ↓): endothelin · thromboxane A₂ · ADH · dopamine ขนาดสูง", fs=11),
        box(10, 324, 400, 34, "ok", "ขยายทั้งสองเส้น (RBF ↑ · GFR ใกล้เดิม): nitric oxide · dopamine ขนาดต่ำ", fs=11),
    ]
    return fig("Afferent กับ efferent arteriole — สารแต่ละตัวออกฤทธิ์ที่เส้นไหน",
               "ตารางสไลด์ \"Vasoactive substances\" วาดเป็นภาพ: ★ = **major site of action** · RBF ขึ้นกับความต้านทานรวม (หดเส้นไหนก็ RBF ลด) แต่ **GFR ขึ้นกับว่าความดันในกระจุก (PGC) เปลี่ยนอย่างไร** — หด afferent = กั้นต้นทาง PGC ตก · หด efferent = กั้นปลายทาง เลือดค้างในกระจุก PGC สูง · สองตัวที่ต้องจำเพราะใช้ทางคลินิกทุกวัน: **prostaglandin ขยาย afferent** (NSAID ตัดออก) และ **angiotensin II หด efferent** (ACEi/ARB ตัดออก) — หัวข้อ 6",
               svg(420, 366, "สารที่หดหรือขยาย afferent และ efferent arteriole และผลต่อ RBF และ GFR", *out))


# ═══════════════════════════════════════ 2b การหลั่ง renin 3 ทาง
def renin():
    out = [
        box(10, 10, 128, 66, "ms", "① sympathetic ↑\nβ1 ที่ JG cell\n(ความดัน/ปริมาตร ↓)", fs=11),
        box(146, 10, 128, 66, "ms", "② ความดันเลือด\nเข้าไต ↓ → JG cell\nถูกยืดน้อยลง", fs=11),
        box(282, 10, 128, 66, "ms", "③ NaCl ถึง\nmacula densa ↓\n(GFR ↓)", fs=11),
        ar(74, 76, 160, 112, "lms w2", "ah-ms"), ar(210, 76, 210, 110, "lms w2", "ah-ms"), ar(346, 76, 260, 112, "lms w2", "ah-ms"),
        box(130, 114, 160, 40, "ac", "JG cell → renin ↑", "b"),
        box(316, 118, 94, 32, "ok", "ANP ⊖", "b", fs=12), ar(314, 134, 294, 134, "lbad w2", "ah-bad"),
        ar(210, 154, 210, 176, "lac", "ah-ac"),
        t(210, 192, "angiotensinogen (ตับ) → AI → AII", "sm b mid"),
        t(210, 208, "(renin จากไต · ACE ที่ปอด)", "xs mid i2"),
        ar(210, 214, 210, 232, "lac", "ah-ac"),
        box(10, 236, 128, 58, "bad", "หด efferent\n→ คง GFR\nเมื่อเลือดเข้าไตน้อย", fs=10.5),
        box(146, 236, 128, 58, "bad", "หดหลอดเลือดทั่วไป\n→ ความดัน ↑\nRBF ↓", fs=10.5),
        box(282, 236, 128, 58, "bad", "aldosterone · ADH\nNHE3 ที่ PT ↑\n→ เก็บ Na และน้ำ", fs=10.5),
    ]
    return fig("สามทางที่สั่งให้ JG cell หลั่ง renin — ทั้งหมดคือสัญญาณ \"เลือดเข้าไตไม่พอ\"",
               "สไลด์ \"Mechanisms activating renin secretion\": ① **sympathetic (β1-AR)** — ปริมาตร/ความดันลด ออกกำลัง กลัว · ② **renal baroreceptor** — ความดันที่ afferent ต่ำ JG cell ถูกยืดน้อย (hypovolemia, **renal artery stenosis**) · ③ **macula densa** — NaCl ที่ไหลมาถึงลดลงเพราะ GFR ลด (glomerular disease, hypovolemia) หรือถูกดูดกลับไปก่อนที่ PT/loop มาก (กลูโคส/กรดอะมิโนในเลือดสูง) · **ANP ยับยั้ง** · ผลของ AII แถวล่างขวา (aldosterone, ADH, NHE3) เป็นการเติมจาก Guyton & Hall — รายละเอียดการคุมปริมาตรอยู่ใน Part II",
               svg(420, 300, "สามกลไกกระตุ้นการหลั่ง renin และผลของ angiotensin II", *out))


# ═══════════════════════════════════════ 3 PAH clearance → ERPF → RBF
def pah():
    out = [
        ar(10, 50, 72, 50, "lbad w3", "ah-bad"), t(40, 40, "PAH 100%", "xs b mid tbad"),
        circ(98, 50, 24, "bad"), t(98, 54, "glom.", "xs mid b"),
        line(122, 50, 330, 50, "lbad w3"), t(220, 40, "efferent → peritubular capillary (80%)", "xs mid i2"),
        ar(330, 50, 404, 50, "lbad w3", "ah-bad"), t(372, 40, "vein 10%", "xs b mid tbad"),
        ar(98, 74, 98, 122, "lwa w2", "ah-wa"), t(104, 102, "กรอง 20%", "xs b twa"),
        ar(200, 54, 200, 122, "lok w2", "ah-ok"), ar(250, 54, 250, 122, "lok w2", "ah-ok"), ar(300, 54, 300, 122, "lok w2", "ah-ok"),
        t(308, 86, "หลั่ง 70%", "xs b tok"), t(308, 100, "(OAT ที่ PT)", "xs tok"),
        rect(80, 124, 300, 24, "wa", 10), t(230, 140, "ท่อไต", "xs mid b twa"),
        ar(380, 136, 404, 136, "lwa w3", "ah-wa"), t(392, 166, "ปัสสาวะ 90%", "xs b end twa"),
        box(10, 182, 400, 40, "ac", "C_PAH = (U_PAH × V) / P_PAH = 90% ของ RPF = ERPF ≈ 630 mL/min", "b", fs=12),
        box(10, 230, 400, 40, "sk", "Actual RPF = ERPF ÷ extraction ratio 0.9 ≈ 700 mL/min", fs=12),
        box(10, 278, 400, 40, "bad", "RBF = RPF ÷ (1 − Hct) = 700 ÷ 0.55 ≈ 1,270 mL/min (Hct 45%)", fs=12),
    ]
    return fig("วัดเลือดที่ไหลผ่านไตด้วย PAH — สารที่ไตขับออก \"เกือบหมด\" ในรอบเดียว",
               "หลัก clearance: **ปริมาณสารในปัสสาวะ ÷ ความเข้มข้นในพลาสมา = ปริมาตรพลาสมาที่ต้องใช้ขนสารนั้นมา** · PAH ถูกกรอง 20% และ **หลั่งเพิ่มที่ท่อไตส่วนต้นอีก 70%** เหลือกลับเข้าหลอดเลือดดำเพียง 10% → clearance ของ PAH จึงเท่ากับ 90% ของพลาสมาที่ไหลผ่านไต (**effective RPF**) · หารด้วย extraction ratio 0.9 ได้ RPF จริง · แปลงเป็นเลือดทั้งหมดด้วย (1 − Hct) เพราะเม็ดเลือดแดงไม่ได้ขน PAH",
               svg(420, 326, "การกรองและหลั่ง PAH และสูตรคำนวณ ERPF RPF และ RBF", *out))


# ═══════════════════════════════════════ 3b sCr กับ GFR เป็นเส้นโค้ง hyperbola
def scr_curve():
    X = lambda g: 50 + g * 340 / 120
    Y = lambda c: 260 - c * 220 / 8
    pts = [(g, 120 / g) for g in [15, 17, 20, 24, 30, 36, 45, 60, 75, 90, 105, 120]]
    d = "M" + " L".join("%.1f %.1f" % (X(g), Y(c)) for g, c in pts)
    out = [rect(X(0), Y(1.2), 340, Y(0.6) - Y(1.2), "ok", 0),
           line(50, 260, 395, 260, "ln"), line(50, 260, 50, 32, "ln"),
           t(222, 290, "GFR (mL/min)", "sm b mid"), t(14, 24, "sCr (mg/dL)", "sm b")]
    for g in (0, 30, 60, 90, 120):
        out += [line(X(g), 260, X(g), 265, "ln"), t(X(g), 277, str(g), "xs mid mu")]
    for c in (0, 2, 4, 6, 8):
        out += [line(45, Y(c), 50, Y(c), "ln"), t(41, Y(c) + 4, str(c), "xs end mu")]
    out += [path(d, "lac w3"),
            t(X(0) + 6, Y(0.9) + 4, "ช่วงปกติของสไลด์ 0.6–1.2", "xs tok b"),
            circ(X(120), Y(1), 4, "acf"), circ(X(60), Y(2), 4, "acf"), circ(X(30), Y(4), 4, "badf"), circ(X(15), Y(8), 4, "badf"),
            path("M%.1f %.1f L%.1f %.1f" % (X(118), Y(1) - 6, X(62), Y(2) - 6), "lmu da", "ah-mu"),
            t(X(90), Y(2) - 34, "GFR หายไปครึ่ง (120 → 60)", "xs mid b"),
            t(X(90), Y(2) - 20, "sCr เพิ่มแค่ 1.0 → 2.0", "xs mid"),
            path("M%.1f %.1f L%.1f %.1f" % (X(29), Y(4) - 4, X(16.5), Y(8) + 8), "lbad da", "ah-bad"),
            t(X(25) + 8, Y(6.4), "GFR 30 → 15", "xs b tbad"),
            t(X(25) + 8, Y(6.4) + 14, "sCr 4 → 8 (+4)", "xs tbad")]
    return fig("sCr กับ GFR เป็นเส้นโค้ง — ช่วงต้นเสียไตมากแต่ sCr ขยับน้อย",
               "ถ้าการสร้าง creatinine คงที่ **sCr × GFR ≈ คงที่** (สมดุล: กรองออกเท่าที่สร้าง) จึงได้เส้น hyperbola · GFR ตกจาก 120 เหลือ 60 sCr ขึ้นแค่ราว 1 → 2 mg/dL (บางคนยังอยู่ใกล้ช่วงปกติของสไลด์ 0.6–1.2) · ช่วงท้าย GFR ลดนิดเดียว sCr พุ่ง · ความหมาย: **sCr ที่เพิ่ม 0.3–0.5 ในคนที่ sCr เดิมต่ำ คือ GFR หายไปมาก** — และต้องใช้ eGFR ที่ปรับอายุ เพศ ขนาดกล้ามเนื้อ (ภาพนี้วาดจากหลักการใน Guyton & Hall ไม่อยู่ในสไลด์ — สมมุติ sCr 1.0 ที่ GFR 120)",
               svg(420, 300, "กราฟความสัมพันธ์แบบไฮเพอร์โบลาระหว่างครีเอตินีนในเลือดและอัตราการกรอง", *out))


# ═══════════════════════════════════════ 4 glomerular filtration barrier
def barrier():
    rows = [("1 Endothelium — fenestra ~70 nm", "ผิวเคลือบ glycoprotein ประจุลบ", "กั้น RBC WBC platelet", "sk"),
            ("2 GBM — collagen IV ประจุลบ", "size + charge barrier หลัก", "กั้นโปรตีนโมเลกุลใหญ่", "ac"),
            ("3 Slit diaphragm ของ podocyte 4–14 nm", "nephrin · NEPH-1 · podocin (ประจุลบ)", "กั้นโปรตีนเล็ก (albumin)", "ok")]
    out = [box(10, 10, 400, 34, "bad", "เลือดในกระจุก: เซลล์ · albumin (−) · น้ำ Na⁺ glucose urea", fs=11.5)]
    y = 52
    for a, b, c, cl in rows:
        out += [rect(10, y, 400, 42, cl, 6), t(18, y + 17, a, "sm b"), t(18, y + 33, b, "xs i2"), t(402, y + 33, c, "xs b end tbad")]
        y += 48
    out += [box(10, y, 400, 30, "wa", "Bowman's space: น้ำ ion glucose urea creatinine ผ่านเสรี (100%)", fs=11.5)]
    y += 48
    out += [t(10, y, "filterability เทียบกับน้ำ (Boron & Boulpaep)", "sm b")]
    bars = [("Na⁺ · glucose · Cr", "< 1 nm", 100, "lwa"), ("myoglobin 17 kDa", "3.8 nm", 75, "lms"),
            ("hemoglobin 68 kDa", "6.5 nm", 3, "lbad"), ("albumin 69 kDa (−)", "7.1 nm", 0.5, "lbad")]
    y += 12
    for name, dia, v, cl in bars:
        w = max(3, v * 2.0)
        out += [t(14, y + 14, name, "xs b"), t(158, y + 14, dia, "xs end mu"),
                rect(166, y + 4, w, 14, cl.replace("l", "", 1) + "f", 3), t(172 + w, y + 15, "%s%%" % (("%g" % v)), "xs b")]
        y += 24
    out += [t(10, y + 12, "Hb กับ albumin หนักพอกัน แต่ albumin ผ่านน้อยกว่า ~6 เท่า = ผลของประจุลบ", "xs i2")]
    return fig("Filtration barrier 3 ชั้น — กั้นด้วย \"ขนาด\" และ \"ประจุลบ\"",
               "ของเหลวผ่าน 3 ชั้นเรียงกัน แต่ละชั้นกั้นของคนละขนาด: endothelium กั้น **เซลล์** · GBM กั้น **โปรตีนใหญ่** · slit diaphragm กั้น **โปรตีนเล็ก** · โมเลกุล < 3.6 nm (< 5.5 kDa) ผ่านเสรี · 3.6–8.4 nm ผ่านน้อยลงเรื่อย ๆ · > 8.4 nm (> 70 kDa) ไม่ผ่าน · ประจุลบของทั้งสามชั้นผลัก **albumin ซึ่งเป็นประจุลบ** — ไอออนเล็ก (Na⁺ Cl⁻ K⁺ HCO₃⁻) ผ่านได้หมดไม่ว่าประจุอะไร · myoglobin เล็ก (17 kDa) ผ่าน 75% → rhabdomyolysis ทำให้ปัสสาวะสีโคล่า",
               svg(420, y + 22, "ชั้นกรองสามชั้นของโกลเมอรูลัสและสัดส่วนการกรองตามขนาดโมเลกุล", *out))


# ═══════════════════════════════════════ 5 Starling forces → NFP → GFR
def starling():
    out = [
        t(16, 50, "afferent", "xs b"), t(404, 50, "efferent", "xs b end"),
        rect(70, 34, 280, 46, "bad", 20), t(210, 62, "glomerular capillary", "sm b mid tbad"),
        rect(40, 140, 340, 46, "wa", 10), t(210, 168, "Bowman's space", "sm b mid twa"),
        line(120, 82, 120, 136, "lok w3", "ah-ok"), t(132, 106, "P_GC 60", "sm b tok"), t(132, 120, "ดันออก", "xs tok"),
        line(225, 138, 225, 84, "lwa w3", "ah-wa"), t(233, 106, "P_BC 18", "sm b twa"), t(233, 120, "ดันกลับ", "xs twa"),
        line(320, 138, 320, 84, "lms w3", "ah-ms"), t(328, 106, "π_GC 32", "sm b tms"), t(328, 120, "ดึงกลับ", "xs tms"),
        box(10, 198, 400, 36, "ac", "NFP = P_GC − (P_BC + π_GC) = 60 − (18 + 32) = 10 mmHg", "b", fs=12.5),
        box(10, 240, 400, 36, "ok", "GFR = Kf × NFP = 12.5 × 10 = 125 mL/min ≈ 180 L/วัน", "b", fs=12.5),
        box(10, 284, 196, 52, "sk", "Kf = พื้นที่ × การซึมผ่าน\nmesangial หด · GBM หนา ↓", fs=11),
        box(214, 284, 196, 52, "sk", "P_GC = ความต้านทาน\nafferent vs efferent", fs=11),
        box(10, 342, 196, 52, "sk", "P_BC ↑ เมื่อทางเดิน\nปัสสาวะอุด (นิ่ว prostate)", fs=11),
        box(214, 342, 196, 52, "sk", "π_GC ตาม albumin\nalbumin ต่ำ → GFR ↑", fs=11),
    ]
    return fig("แรง Starling ข้ามผนังกระจุก — แรงสุทธิแค่ 10 mmHg แต่กรองได้วันละ 180 ลิตร",
               "ตัวเลขจากสไลด์: ความดันในกระจุก **60** ดันน้ำออก · ความดันใน Bowman's space **18** และ oncotic pressure ของพลาสมา **32** ต้านกลับ (oncotic ใน Bowman ≈ 0 เพราะไม่มีโปรตีน) → **NFP 10 mmHg** · ที่กรองได้มากเพราะ Kf สูงมาก (12.5 mL/min/mmHg) · ทุกโรค/ยาที่เปลี่ยน GFR ต้องผ่านหนึ่งในสี่ช่องล่างนี้ · หมายเหตุ (Boron & Boulpaep): π_GC ไม่คงที่ — เพิ่มขึ้นตามความยาวกระจุกเพราะน้ำออกไปแล้วโปรตีนเข้มข้นขึ้น ตัวเลข 32 คือค่าเฉลี่ย",
               svg(420, 402, "แรงสตาร์ลิงสามแรงข้ามผนังโกลเมอรูลัส การคำนวณแรงกรองสุทธิและ GFR และปัจจัยที่เปลี่ยนแต่ละแรง", *out))


# ═══════════════════════════════════════ 5b สี่แบบ: หด/ขยาย afferent/efferent
def arterioles4():
    def panel(x, y, title, ha, he, res, ex, cl):
        out = [rect(x, y, 200, 150, cl, 8), t(x + 100, y + 18, title, "sm b mid"),
               rect(x + 10, y + 56 - ha / 2, 72, ha, "bad", ha / 2), circ(x + 100, y + 56, 18, "bad"),
               rect(x + 118, y + 56 - he / 2, 72, he, "bad", he / 2),
               t(x + 46, y + 86, "aff.", "xs mid mu"), t(x + 154, y + 86, "eff.", "xs mid mu")]
        for i, r in enumerate(res):
            out.append(t(x + 100, y + 106 + 15 * i, r, "xs mid b"))
        out.append(t(x + 100, y + 142, ex, "xs mid i2"))
        return out
    out = (panel(10, 10, "หด afferent", 5, 12, ["RBF ↓ · P_GC ↓", "GFR ↓ (FF ≈ เดิม)"], "NE/E · NSAID (ตัด PG)", "bad")
           + panel(210, 10, "หด efferent", 12, 5, ["RBF ↓ · P_GC ↑", "GFR ↑/คงไว้ (FF ↑)"], "angiotensin II", "ms")
           + panel(10, 166, "ขยาย afferent", 18, 12, ["RBF ↑ · P_GC ↑", "GFR ↑"], "PGE₂ PGI₂ · ANP", "ok")
           + panel(210, 166, "ขยาย efferent", 12, 18, ["RBF ↑ · P_GC ↓", "GFR ↓ (FF ↓)"], "ACEi / ARB (ตัด AII)", "wa"))
    return fig("หลักเดียวใช้ได้ทุกยา: หด/ขยาย afferent หรือ efferent ทำอะไรกับ GFR",
               "**RBF ตามความต้านทานรวม** — หดเส้นไหน RBF ก็ลด ขยายเส้นไหน RBF ก็เพิ่ม · **GFR ตาม P_GC** ซึ่งขึ้นกับว่าแคบ \"ก่อน\" หรือ \"หลัง\" กระจุก: แคบก่อน (afferent) = เลือดเข้าน้อย P_GC ตก · แคบหลัง (efferent) = เลือดออกยาก ค้างอยู่ในกระจุก P_GC สูง · ข้อควรรู้ (Guyton & Hall): efferent หดมากเกินจน RBF ลดมาก π_GC จะขึ้นจนกลับทำให้ GFR ลด — ความสัมพันธ์จึงเป็นรูประฆัง",
               svg(420, 326, "ผลของการหดและขยาย afferent และ efferent arteriole ต่อ RBF ความดันในกระจุก และ GFR", *out))


# ═══════════════════════════════════════ 6 low-flow state + NSAID / ACEi
def lowflow():
    def row(y, title, sub, ha, he, xa, xe, res, cl, rc):
        out = [rect(10, y, 400, 74, cl, 8), t(18, y + 18, title, "sm b"), t(18, y + 34, sub, "xs i2"),
               rect(130, y + 52 - ha / 2, 76, ha, "bad", ha / 2), circ(222, y + 52, 15, "bad"),
               rect(238, y + 52 - he / 2, 76, he, "bad", he / 2),
               t(168, y + 38, xa, "xs mid b " + ("tbad" if "✕" in xa else "tok")),
               t(276, y + 38, xe, "xs mid b " + ("tbad" if "✕" in xe else "tok")),
               t(402, y + 50, res[0], "xs b end " + rc), t(402, y + 64, res[1], "xs end " + rc)]
        return out
    out = (row(10, "ไตขาดเลือด", "shock · ขาดน้ำ · HF", 14, 6, "PG ขยาย", "AII หด", ["GFR ยังพอ", "ชดเชยได้"], "sk", "tok")
           + row(92, "+ NSAID", "ตัด PG", 5, 6, "✕ PG → หด", "AII หด", ["GFR ↓↓", "AKI"], "bad", "tbad")
           + row(174, "+ ACEi / ARB", "ตัด AII", 14, 14, "PG ขยาย", "✕ AII → คลาย", ["P_GC ↓ GFR ↓", "Cr ↑"], "ms", "tbad")
           + row(256, "Triple whammy", "ทั้งสอง + ยาขับปัสสาวะ", 5, 14, "✕ PG", "✕ AII", ["ปริมาตร ↓ ด้วย", "AKI รุนแรง"], "bad", "tbad"))
    out += [t(10, 350, "ไตปกติ ปริมาตรปกติ: PG/AII แทบไม่ได้คุม GFR → ยาสองกลุ่มนี้ปลอดภัยกว่ามาก", "xs i2")]
    return fig("ทำไม NSAID และ ACEi/ARB ทำให้ไตวายเฉียบพลันเฉพาะตอน \"เลือดเข้าไตน้อย\"",
               "เมื่อเลือดเข้าไตน้อย ไตพยุง GFR ด้วยสองมือ: **prostaglandin ขยาย afferent** (สไลด์: PG ช่วยคง RBF ใน hemorrhage และ shock) และ **angiotensin II หด efferent** (สไลด์: AII ช่วยคง GFR เมื่อความดันเข้าไตต่ำ) · **NSAID** ตัดมือแรก → afferent หด → AKI (สไลด์: ให้ NSAID ระหว่าง hemorrhagic shock ทำให้เกิด AKI) · **ACEi/ARB** ตัดมือที่สอง → efferent คลาย P_GC ตก (bilateral renal artery stenosis, HF, ขาดน้ำ) · ตัดทั้งสองมือ + ยาขับปัสสาวะลดปริมาตร = **\"triple whammy\"** (คำนี้มาจากวรรณกรรมเภสัชวิทยา ไม่อยู่ในสไลด์)",
               svg(420, 362, "ไตที่ขาดเลือดพยุง GFR ด้วย prostaglandin และ angiotensin II และผลเมื่อใช้ NSAID หรือ ACEi หรือทั้งสองร่วมกับยาขับปัสสาวะ", *out))


# ═══════════════════════════════════════ 7 autoregulation curve
def autoreg():
    X = lambda p: 50 + p * 340 / 200
    Y = lambda f: 210 - f * 170 / 150
    pts = [(0, 0), (25, 25), (50, 55), (65, 78), (75, 90), (80, 95), (90, 98), (110, 100), (140, 101), (160, 102), (170, 104),
           (180, 112), (190, 124), (200, 138)]
    d = "M" + " L".join("%.1f %.1f" % (X(p), Y(f)) for p, f in pts)
    out = [rect(X(80), 30, X(170) - X(80), 180, "ok", 0), t((X(80) + X(170)) / 2, 46, "MAP 80–170", "xs b mid tok"), t((X(80) + X(170)) / 2, 60, "RBF/GFR เกือบคงที่", "xs mid tok"),
           rect(X(0), 30, X(75) - X(0), 180, "bad", 0), t(X(37), 46, "< 75 mmHg", "xs b mid tbad"), t(X(37), 60, "ตามความดัน", "xs mid tbad"),
           line(50, 210, 395, 210, "ln"), line(50, 210, 50, 28, "ln"),
           t(222, 240, "ความดันเลือดเฉลี่ย MAP (mmHg)", "sm b mid"), t(14, 20, "RBF, GFR (% ของปกติ)", "sm b")]
    for p in (0, 50, 100, 150, 200):
        out += [line(X(p), 210, X(p), 215, "ln"), t(X(p), 227, str(p), "xs mid mu")]
    for f in (0, 50, 100, 150):
        out += [line(45, Y(f), 50, Y(f), "ln"), t(41, Y(f) + 4, str(f), "xs end mu")]
    out += [path(d, "lac w3"),
            box(10, 252, 196, 92, "ac", "① Myogenic (3–10 วินาที)\nความดัน ↑ ผนังยืด\n→ stretch-gated cation ch.\n→ VGCC เปิด Ca²⁺ เข้า → หด", fs=11),
            box(214, 252, 196, 92, "ac", "② Tubuloglomerular\nfeedback (TGF)\nNaCl ถึง macula densa ↑\n→ afferent หด → GFR ลง", fs=11)]
    return fig("Autoregulation — ไตตรึง RBF และ GFR ไว้แม้ความดันแกว่ง 80–170 mmHg",
               "สองกลไกในตัวไต (ไม่ต้องอาศัยเส้นประสาทหรือฮอร์โมน): **myogenic** ที่ arcuate/interlobular artery และ afferent — ผนังถูกยืดแล้วหดกลับเอง (เปลี่ยนท่า ป้องกันกระจุกจากความดันสูงใน HT, DM) · **TGF** ที่ juxtaglomerular apparatus · ข้อจำกัดในสไลด์: **ใช้ไม่ได้เมื่อ MAP < 75** (shock → GFR ตกตามความดัน = pre-renal) · ไม่สมบูรณ์ (ยังขยับเล็กน้อย) · ฮอร์โมนและ sympathetic ยังเปลี่ยน RBF/GFR ได้ · เส้นกราฟวาดเชิงหลักการ",
               svg(420, 352, "กราฟ autoregulation ของ RBF และ GFR ตามความดันเลือดเฉลี่ย และกลไก myogenic กับ tubuloglomerular feedback", *out))


# ═══════════════════════════════════════ 7b TGF loop + เบาหวาน/SGLT2i
def tgf():
    out = [
        box(10, 24, 180, 54, "ms", "GFR ↑ (เช่น MAP ↑)\n→ NaCl ไหลถึง\nmacula densa ↑", fs=11),
        box(230, 24, 180, 54, "ac", "macula densa รับ NaCl\nผ่าน NKCC2 → หลั่ง\nATP → adenosine", fs=11),
        box(230, 118, 180, 54, "bad", "adenosine (A1R)\n→ afferent หด\n(renin ↓ ด้วย)", fs=11),
        box(10, 118, 180, 54, "ok", "P_GC ↓ → GFR\nกลับสู่ค่าเดิม", fs=11),
        ar(190, 51, 228, 51, "lms w2", "ah-ms"), ar(320, 78, 320, 116, "lac w2", "ah-ac"),
        ar(230, 145, 192, 145, "lbad w2", "ah-bad"), ar(100, 118, 100, 80, "lok w2", "ah-ok"),
        t(210, 104, "TGF", "sm b mid tac"),
        t(10, 196, "เบาหวาน: hyperfiltration (สไลด์) และ SGLT2 inhibitor (ตำรา)", "sm b"),
        box(10, 206, 196, 112, "bad", "น้ำตาลสูง → SGLT2 ใน PT\nดูด Na⁺ + glucose มาก\n→ NaCl ถึง macula densa ↓\n→ TGF เข้าใจว่า GFR ต่ำ\n→ afferent ขยาย\n→ hyperfiltration", fs=11),
        box(214, 206, 196, 112, "ok", "SGLT2i บล็อก SGLT2\n→ Na⁺ ถึง macula densa ↑\n→ TGF ทำงานคืน\n→ afferent หด P_GC ↓\n→ eGFR ลดเล็กน้อยช่วงแรก\n= ลดภาระกระจุก", fs=11),
    ]
    return fig("Tubuloglomerular feedback — ท่อไตบอกกระจุกของตัวเองว่า \"กรองมากไป\"",
               "**macula densa** อยู่ที่ปลาย TAL แนบกับ afferent ของ nephron ตัวเอง ใช้ปริมาณ NaCl ที่ไหลผ่านเป็นตัววัด GFR · สไลด์บอกเพียงว่า TGF ทำงานที่ JGA เพื่อคง GFR และ **\"hyperglycemia in DM activates TGF → glomerular hyperfiltration → diabetic nephropathy\"** · รายละเอียดโมเลกุล (NKCC2 → ATP/adenosine → A1 receptor) และกลไกของ **SGLT2 inhibitor** เติมจาก Boron & Boulpaep / Guyton & Hall และหลักฐานทางคลินิก (KDIGO 2022 Diabetes in CKD) — ACEi/ARB ลด P_GC ทางขยาย efferent ส่วน SGLT2i ลดทางหด afferent จึงเสริมกัน",
               svg(420, 326, "วงจร tubuloglomerular feedback และกลไก hyperfiltration ในเบาหวานกับผลของ SGLT2 inhibitor", *out))


# ═══════════════════════════════════════ 8 FF + glomerulotubular balance
def ff_gtb():
    out = [
        ar(10, 50, 64, 50, "lbad w3", "ah-bad"), t(34, 40, "RPF 625", "xs b mid tbad"),
        circ(88, 50, 22, "bad"),
        line(110, 50, 404, 50, "lbad w3"), t(256, 40, "efferent → peritubular capillary: 500 mL/min", "xs mid i2"),
        ar(88, 72, 88, 120, "lwa w2", "ah-wa"), t(82, 96, "GFR 125", "xs b end twa"), t(82, 110, "(FF 20%)", "xs end twa"),
        rect(70, 122, 340, 24, "wa", 10), t(240, 138, "proximal tubule", "xs mid b twa"),
        ar(250, 120, 250, 58, "lok w2", "ah-ok"), ar(320, 120, 320, 58, "lok w2", "ah-ok"), ar(380, 120, 380, 58, "lok w2", "ah-ok"),
        t(352, 82, "ดูดกลับ", "xs mid b tok"),
        t(170, 74, "π_c สูง (โปรตีนเข้มข้น)", "xs b mid tms"), t(170, 88, "P_c ต่ำ (ผ่าน efferent)", "xs b mid tms"),
        box(10, 158, 400, 34, "ac", "FF = GFR / RPF ≈ 125 / 625 = 0.16–0.20", "b", fs=12.5),
        t(10, 214, "Glomerulotubular balance เมื่อปริมาตรเลือดลด", "sm b"),
        box(10, 222, 400, 30, "ms", "ปริมาตรลด → sympathetic ↑ (หด aff.+eff.) · AII ↑ (หด efferent)", fs=11),
        ar(210, 252, 210, 266, "lms", "ah-ms"),
        box(10, 268, 400, 30, "ms", "RPF ↓ มาก แต่ GFR เกือบเดิม → FF ↑", fs=11),
        ar(210, 298, 210, 312, "lms", "ah-ms"),
        box(10, 314, 400, 30, "ok", "peritubular: P_c ↓ π_c ↑ → แรงดูดกลับสุทธิ ↑ → PT ดูด Na⁺ และน้ำ ↑", fs=11),
    ]
    return fig("Filtration fraction ผูกการกรองกับการดูดกลับ — ยิ่งกรองออกมาก หลอดเลือดรอบท่อยิ่ง \"ดูด\" แรง",
               "เลือดที่ออกจากกระจุกเสียน้ำไปแล้ว ~20% แต่โปรตีนยังอยู่ครบ → **oncotic pressure ใน peritubular capillary สูง** และความดันน้ำต่ำเพราะผ่าน efferent ที่ต้านไว้ → ดึงน้ำและ Na⁺ ที่ PT ดูดออกมาเข้าเลือด · FF ยิ่งสูง แรงนี้ยิ่งมาก → **glomerulotubular balance**: PT ดูดกลับตามสัดส่วนของที่กรองมา · ภาวะขาดน้ำจึงทั้งรักษา GFR และเก็บ Na/น้ำในคราวเดียว (urea ถูกดูดกลับตามน้ำด้วย → BUN/Cr สูงใน pre-renal — หัวข้อ 14)",
               svg(420, 352, "filtration fraction และแรงในหลอดเลือดรอบท่อไตที่เพิ่มการดูดกลับที่ท่อไตส่วนต้น", *out))


# ═══════════════════════════════════════ 9 Proximal tubule cell
def pt_cell():
    out = [rect(10, 28, 90, 330, "wa", 6), t(55, 46, "ลูเมน", "sm b mid twa"),
           rect(320, 28, 90, 330, "bad", 6), t(365, 46, "เลือด", "sm b mid tbad"),
           rect(116, 28, 188, 282, "bx", 6), t(210, 46, "เซลล์ PT", "sm b mid"),
           rect(116, 326, 188, 32, "bx", 6)]
    out += _in(76, "Na⁺ glucose") + [circ(116, 76, 8, "ok"), t(130, 80, "SGLT2", "xs b")]
    out += [circ(304, 76, 8, "ok"), t(290, 80, "GLUT2", "xs b end")] + _bl(76, "glucose")
    out += _in(116, "Na⁺ AA") + [circ(116, 116, 8, "ok"), t(130, 120, "Na–AA", "xs b")]
    out += [circ(304, 120, 9, "ac"), t(290, 116, "Na⁺/K⁺-", "xs b end"), t(290, 128, "ATPase", "xs b end"),
            line(314, 114, 402, 114, "lac w2", "ah-ac"), t(362, 108, "3Na⁺", "xs mid b"),
            line(402, 128, 316, 128, "lac w2", "ah-ac"), t(362, 142, "2K⁺", "xs mid b")]
    out += _in(160, "Na⁺ Pi") + [circ(116, 160, 8, "ok"), t(130, 158, "NaPi-IIa", "xs b"), t(130, 172, "✕ PTH · FGF-23", "xs tbad")]
    out += _in(204, "Na⁺") + _out(218, "H⁺", "lbad", "ah-bad", "xs mid b tbad") + [circ(116, 211, 8, "ok"), t(130, 208, "NHE3", "xs b"), t(130, 222, "AII ↑", "xs tok")]
    out += [t(55, 244, "HCO₃⁻ + H⁺", "xs mid b"), t(55, 258, "↓ CA (ผิวลูเมน)", "xs mid"), t(55, 272, "CO₂ + H₂O", "xs mid b"),
            ar(100, 268, 128, 262, "lmu", "ah-mu"),
            t(136, 258, "CO₂ + H₂O", "xs b"), t(136, 272, "→ CA → H⁺ + HCO₃⁻", "xs"),
            t(136, 294, "✕ acetazolamide (CA)", "xs b tbad"),
            circ(304, 266, 8, "ok"), t(290, 250, "NBC1", "xs b end")] + _bl(266, "HCO₃⁻ Na⁺")
    out += [line(18, 318, 402, 318, "lwa w2", "ah-wa"), t(210, 346, "ช่องระหว่างเซลล์: น้ำ (+AQP1) Cl⁻ K⁺ Ca²⁺", "xs mid b twa")]
    out += [box(10, 368, 400, 50, "bad", "Na⁺/K⁺-ATPase คือแบตเตอรี่ของทุกตัวขนส่ง (Na⁺ ในเซลล์ 10 vs ลูเมน 140)\nFanconi: ระบบนี้ล้ม → glucose AA Pi HCO₃⁻ หลุดพร้อมกัน", fs=11)]
    return fig("ท่อไตส่วนต้น — ดูดกลับ 65% ของที่กรอง โดยใช้ Na⁺ เป็นตัวพา",
               "**Na⁺/K⁺-ATPase ด้านเลือด** สูบ Na⁺ ออกจนในเซลล์เหลือ ~10 mEq/L (ลูเมน 140) → Na⁺ ไหลเข้าเซลล์จากลูเมนเองและ **พาสารอื่นเข้ามาด้วย**: glucose (SGLT2 ~100%) กรดอะมิโน (~100%) phosphate (NaPi-IIa 80% — PTH และ FGF-23 ดึงตัวขนส่งเข้าไปทำลาย) และแลก H⁺ ออก (NHE3 — AII กระตุ้น) · H⁺ ที่ออกไปจับ HCO₃⁻ กลายเป็น CO₂ เข้าเซลล์ แล้วสร้าง HCO₃⁻ ใหม่ส่งออกทาง NBC1 (ดูดกลับ HCO₃⁻ 80%) — **carbonic anhydrase** คือจุดที่ acetazolamide บล็อก · น้ำตามออสโมซิส (AQP1) ของเหลวจึงยัง isosmotic · ภาพวาดตามป้ายในสไลด์ ชื่อ NHE3/NBC1/NaPi-IIa ตามสไลด์และ Boron & Boulpaep",
               svg(420, 424, "แผนภาพเซลล์ท่อไตส่วนต้นแสดงตัวขนส่งกลูโคส กรดอะมิโน ฟอสเฟต โซเดียมไฮโดรเจน และการดูดกลับไบคาร์บอเนต", *out))


# ═══════════════════════════════════════ 10 glucose titration curve
def titration():
    X = lambda p: 52 + p * 340 / 800
    Y = lambda m: 250 - m * 210 / 1000
    gfr, tm = 1.25, 375.0
    def reab(p):
        f = p * gfr
        return f if f < 225 else tm - (tm - 225) * math.exp(-(f - 225) / (tm - 225))
    ps = [i * 10 for i in range(81)]
    dF = "M%.1f %.1f L%.1f %.1f" % (X(0), Y(0), X(800), Y(1000))
    dR = "M" + " L".join("%.1f %.1f" % (X(p), Y(reab(p))) for p in ps)
    dE = "M" + " L".join("%.1f %.1f" % (X(p), Y(max(0, p * gfr - reab(p)))) for p in ps if p >= 170)
    out = [line(52, 250, 395, 250, "ln"), line(52, 250, 52, 30, "ln"),
           t(222, 280, "glucose ในพลาสมา (mg/dL)", "sm b mid"), t(10, 20, "mg/min", "sm b")]
    for p in (0, 200, 400, 600, 800):
        out += [line(X(p), 250, X(p), 255, "ln"), t(X(p), 267, str(p), "xs mid mu")]
    for m in (0, 250, 500, 750, 1000):
        out += [line(47, Y(m), 52, Y(m), "ln"), t(43, Y(m) + 4, str(m), "xs end mu")]
    out += [line(X(0), Y(tm), X(800), Y(tm), "lmu da"), t(X(0) + 6, Y(tm) - 6, "Tm 375 mg/min", "xs b"),
            line(X(180), Y(0), X(180), Y(560), "lbad da"), t(X(180) + 4, Y(560), "threshold 180", "xs b tbad"),
            path(dF, "lwa w3"), path(dR, "lok w3"), path(dE, "lbad w3"),
            t(X(560) - 6, Y(700) - 8, "กรอง", "xs b end twa"), t(X(640), Y(tm) + 16, "ดูดกลับ", "xs b mid tok"),
            t(X(780) - 4, Y(600) - 14, "ขับออก", "xs b end tbad"),
            t(X(300) + 6, Y(300) + 20, "splay", "xs b i2")]
    out += [box(10, 292, 128, 62, "ms", "glucose ↑ เกิน\nthreshold\n(เบาหวาน)", fs=11),
            box(146, 292, 128, 62, "wa", "filtered load ↑\nGFR ↑ · Tm ↓\n(ตั้งครรภ์)", fs=11),
            box(282, 292, 128, 62, "bad", "SGLT2 ใช้ไม่ได้\nfamilial · Fanconi\n· ยา SGLT2i", fs=11)]
    return fig("Glucose titration curve — ทำไมน้ำตาลรั่วตั้งแต่ 180 ทั้งที่ Tm ยังไม่เต็ม",
               "ที่กรอง = P_glucose × GFR (เส้นฟ้า) · ท่อไตดูดกลับได้สูงสุด **Tm 375 mg/min** (เส้นเขียว) · ที่เหลือออกในปัสสาวะ (เส้นแดง) · ตัวเลข **threshold 180 mg/dL** และ Tm 375 มาจากสไลด์ · ช่วงโค้ง **splay** (ตำรา Guyton & Hall): nephron แต่ละตัว Tm ไม่เท่ากัน ตัวที่ Tm ต่ำอิ่มก่อน จึงเริ่มรั่วตั้งแต่ ~180 แม้ค่า Tm รวม (คำนวณแล้วตรงกับ ~300 mg/dL ที่ GFR 125) ยังไม่ถึง · กล่องล่าง = สามทางที่ทำให้เกิด glucosuria ตามสไลด์ (+ยา SGLT2i)",
               svg(420, 362, "กราฟการกรอง การดูดกลับ และการขับกลูโคสตามระดับน้ำตาลในพลาสมา พร้อม threshold และ Tm", *out))


# ═══════════════════════════════════════ 11 Thick ascending limb
def tal():
    out = [rect(10, 28, 90, 234, "wa", 6), t(55, 46, "ลูเมน", "sm b mid twa"),
           rect(320, 28, 90, 234, "bad", 6), t(365, 46, "เลือด", "sm b mid tbad"),
           rect(116, 28, 188, 168, "bx", 6), t(210, 46, "เซลล์ TAL", "sm b mid"),
           rect(116, 212, 188, 50, "bx", 6)]
    out += _in(80, "Na⁺ K⁺ 2Cl⁻") + [circ(116, 80, 8, "ok"), t(130, 78, "NKCC2", "xs b"), t(130, 92, "✕ furosemide", "xs b tbad")]
    out += _out(128, "K⁺ รั่วกลับ") + [circ(116, 128, 8, "ms"), t(130, 132, "ROMK", "xs b")]
    out += [circ(304, 80, 9, "ac"), t(290, 84, "Na⁺/K⁺-ATPase", "xs b end")] + _bl(80, "3Na⁺", "lac", "ah-ac")
    out += [circ(304, 120, 8, "ok"), t(290, 124, "ClC-Kb", "xs b end")] + _bl(120, "Cl⁻")
    out += [circ(304, 164, 8, "bad"), t(290, 160, "CaSR", "xs b end"), t(290, 174, "Ca²⁺ สูง → ปิด", "xs end tbad")]
    out += [t(55, 166, "+8 mV", "lg b mid tac"), t(55, 182, "ลูเมนเป็นบวก", "xs mid b")]
    out += [line(18, 204, 402, 204, "lok w3", "ah-ok"),
            t(210, 232, "Ca²⁺ Mg²⁺ (Na⁺ K⁺) ลอด claudin-16/19", "xs mid b tok"), t(210, 248, "ประจุบวกในลูเมนดันออกไปเลือด", "xs mid i2")]
    out += [t(10, 284, "น้ำผ่านไม่ได้ → ของเหลวออกจาก TAL เจือจาง ~100 mOsm (diluting segment)", "xs b i2"),
            box(10, 294, 400, 84, "bad", "Furosemide ปิด NKCC2 →\n① Na⁺ ไหลไปปลายทางมาก → แลก K⁺ ที่ CD → K ต่ำ\n② ไม่มี K⁺ รั่วกลับ → ศักย์บวกหาย → Ca²⁺ Mg²⁺ หลุด\n③ medulla ไม่เข้มข้น → ปัสสาวะเข้มข้นไม่ได้", fs=11)]
    return fig("Thick ascending limb — ดูด NaCl 25% และ Mg²⁺ 60% โดยไม่ดูดน้ำ",
               "**NKCC2** ดึง Na⁺ K⁺ 2Cl⁻ เข้าเซลล์ · K⁺ ส่วนใหญ่ **รั่วกลับลูเมนทาง ROMK** (ให้ NKCC2 มี K⁺ ใช้ต่อ) และทำให้ลูเมนเป็น **บวก ~+8 mV** → ดันไอออนบวก (Ca²⁺ Mg²⁺) ลอดช่องระหว่างเซลล์ที่มี **claudin-16/19** · ผนังไม่ซึมน้ำ จึงเหลือของเหลวเจือจางและทิ้งเกลือไว้ใน medulla · **CaSR** ด้านเลือดรับ Ca²⁺ สูงแล้วลดการทำงานนี้ (ขับ Ca ทิ้งเอง) · ClC-Kb (ทางออกของ Cl⁻) เติมจาก Boron & Boulpaep · กลไกนี้คือเหตุที่ loop diuretic และ **Bartter syndrome** ให้ภาพ K ต่ำ Ca ในปัสสาวะสูง Mg ต่ำ",
               svg(420, 386, "แผนภาพเซลล์ thick ascending limb แสดง NKCC2 ROMK ศักย์บวกในลูเมน และการดูดกลับแคลเซียมแมกนีเซียมผ่านช่องระหว่างเซลล์", *out))


# ═══════════════════════════════════════ 12a Early DT — thiazide → Ca สูง
def dct():
    out = [rect(10, 28, 90, 226, "wa", 6), t(55, 46, "ลูเมน", "sm b mid twa"),
           rect(320, 28, 90, 226, "bad", 6), t(365, 46, "เลือด", "sm b mid tbad"),
           rect(116, 28, 188, 226, "bx", 6), t(210, 46, "เซลล์ early DT", "sm b mid")]
    out += _in(84, "Na⁺ Cl⁻") + [circ(116, 84, 8, "ok"), t(130, 82, "NCC", "xs b"), t(130, 96, "✕ thiazide", "xs b tbad")]
    out += [circ(304, 84, 9, "ac"), t(290, 88, "Na⁺/K⁺-ATPase", "xs b end")] + _bl(84, "3Na⁺", "lac", "ah-ac")
    out += _in(150, "Ca²⁺", "lac", "ah-ac", "xs mid b tac") + [circ(116, 150, 8, "ac"), t(130, 148, "TRPV5", "xs b"), t(130, 162, "PTH · calcitriol ↑", "xs tok")]
    out += [t(210, 186, "calbindin พา Ca²⁺", "xs mid i2")]
    out += [circ(304, 150, 8, "ac"), t(290, 146, "NCX", "xs b end"), t(290, 160, "(+PMCA)", "xs end mu"),
            line(314, 146, 402, 146, "lac w2", "ah-ac"), t(362, 140, "Ca²⁺ ออก", "xs mid b"),
            line(402, 160, 316, 160, "lok w2", "ah-ok"), t(362, 176, "3Na⁺ เข้า", "xs mid b")]
    out += _in(222, "Mg²⁺") + [circ(116, 222, 8, "ok"), t(130, 226, "TRPM6 (thiazide ลดจำนวน)", "xs b")]
    out += [t(10, 276, "ทำไม thiazide ทำให้ Ca ในเลือดสูง (แต่ loop ทำให้ต่ำ)", "sm b"),
            box(10, 284, 400, 30, "sk", "thiazide ปิด NCC → Na⁺ ในเซลล์ ↓", fs=11), ar(210, 314, 210, 326, "lac", "ah-ac"),
            box(10, 328, 400, 30, "sk", "Na⁺ จากเลือดเข้าทาง NCX ง่ายขึ้น → ดัน Ca²⁺ ออกเลือดมากขึ้น", fs=11), ar(210, 358, 210, 370, "lac", "ah-ac"),
            box(10, 372, 400, 30, "ok", "Ca²⁺ ในเซลล์ ↓ → TRPV5 ดึง Ca²⁺ จากลูเมนเข้ามาอีก → Ca ในปัสสาวะ ↓", fs=11)]
    return fig("Early distal tubule — ดูด NaCl ~5% ผ่าน NCC และเป็นที่ปรับ Ca²⁺ ด้วย PTH",
               "เซลล์ส่วนนี้ **ไม่ซึมน้ำ** (ยังเป็น diluting segment) · ดูด NaCl 5% · **Ca²⁺ 8%** แบบผ่านเซลล์ (TRPV5 → calbindin → NCX/PMCA) ซึ่ง **PTH และ 1,25(OH)₂D₃** เพิ่ม · Mg²⁺ 5% · ลำดับเหตุผลด้านล่างตรงกับสไลด์ \"low [Na⁺]i → ↑Na⁺/Ca²⁺ exchanger → ↓[Ca²⁺]i → ↑Ca²⁺ reabsorption\" · thiazide ยังลดจำนวนช่อง Mg²⁺ → Mg ต่ำ · **Gitelman syndrome** = NCC บกพร่องแต่กำเนิด (เหมือนกิน thiazide ตลอดชีวิต: K ต่ำ Mg ต่ำ Ca ในปัสสาวะต่ำ) · ชื่อ TRPV5/TRPM6/PMCA เติมจาก Boron & Boulpaep",
               svg(420, 410, "แผนภาพเซลล์ distal tubule ส่วนต้น แสดง NCC การดูดกลับแคลเซียม และเหตุที่ thiazide ทำให้แคลเซียมในเลือดสูง", *out))


# ═══════════════════════════════════════ 12b Principal cell + intercalated cells
def pcell():
    out = [rect(10, 28, 90, 196, "wa", 6), t(55, 46, "ลูเมน", "sm b mid twa"),
           rect(320, 28, 90, 196, "bad", 6), t(365, 46, "เลือด", "sm b mid tbad"),
           rect(116, 28, 188, 196, "bx", 6), t(210, 46, "Principal cell (2/3)", "sm b mid")]
    out += _in(80, "Na⁺") + [circ(116, 80, 8, "ok"), t(130, 78, "ENaC", "xs b"), t(130, 92, "✕ amiloride", "xs b tbad")]
    out += _out(124, "K⁺") + [circ(116, 124, 8, "ms"), t(130, 128, "ROMK · BK", "xs b")]
    out += _in(170, "H₂O", "lwa", "ah-wa", "xs mid b twa") + [circ(116, 170, 8, "wa"), t(130, 168, "AQP2", "xs b"), t(130, 182, "ADH (V2) ↑", "xs twa")]
    out += [circ(304, 80, 9, "ac"), t(290, 84, "Na⁺/K⁺-ATPase", "xs b end")] + _bl(80, "3Na⁺", "lac", "ah-ac")
    out += [line(402, 96, 316, 96, "lac w2", "ah-ac"), t(362, 112, "2K⁺", "xs mid b")]
    out += [box(196, 130, 104, 46, "ac", "aldosterone\n→ MR ในเซลล์", fs=10.5), t(248, 192, "✕ spironolactone", "xs b mid tbad"),
            t(248, 206, "eplerenone", "xs b mid tbad")]
    out += [t(55, 200, "ลูเมนเป็นลบ", "xs mid b"), t(55, 214, "ดึง K⁺ ออก", "xs mid i2")]
    out += [rect(10, 236, 196, 108, "ms", 8), t(108, 254, "Type A I-cell (ภาวะกรด)", "sm b mid"),
            t(20, 274, "H⁺ → ลูเมน: H⁺-ATPase", "xs"), t(20, 290, "(aldosterone ↑)", "xs i2"),
            t(20, 308, "H⁺/K⁺-ATPase: หลั่ง H⁺", "xs"), t(20, 324, "แลก K⁺ กลับเข้า", "xs i2"),
            rect(214, 236, 196, 108, "wa", 8), t(312, 254, "Type B I-cell (ภาวะด่าง)", "sm b mid"),
            t(224, 274, "HCO₃⁻ → ลูเมน", "xs"), t(224, 290, "Cl⁻/HCO₃⁻ (pendrin)", "xs i2"),
            t(224, 308, "หลั่ง K⁺ ทาง K⁺ channel", "xs"), t(224, 324, "→ ปรับสมดุลกรด–ด่าง", "xs i2")]
    return fig("Late DT และ cortical collecting duct — จุดที่ aldosterone แลก Na⁺ กับ K⁺",
               "**Principal cell** ดูด Na⁺ ทาง **ENaC** (aldosterone เพิ่ม · ANP ลด) — Na⁺ เข้าโดยไม่มีประจุลบตาม ลูเมนจึง **เป็นลบ** แล้ว K⁺ ไหลออกทาง ROMK/BK (ลูเมนลบเป็นคำอธิบายจาก Boron & Boulpaep) · ปัจจัยที่เพิ่มการหลั่ง K⁺ ตามสไลด์: **aldosterone · tubular flow สูง · Na⁺ ในท่อสูง** · น้ำผ่านเฉพาะเมื่อมี ADH (AQP2) · **K-sparing diuretic** สองแบบ: ENaC blocker (amiloride, triamterene) และ aldosterone antagonist (spironolactone, eplerenone) → Na⁺ ↓ K⁺ ↑ กรดคั่ง · **intercalated cell** type A หลั่ง H⁺ (ภาวะกรด) type B หลั่ง HCO₃⁻ (ภาวะด่าง) — รายละเอียดกรด–ด่างอยู่ใน Part II",
               svg(420, 352, "แผนภาพ principal cell และ intercalated cell ชนิด A และ B ของ collecting duct", *out))


# ═══════════════════════════════════════ 12c แผนที่ยาขับปัสสาวะตามส่วนของ nephron
def diuretic_map():
    rows = [("PT", "65%", "acetazolamide", "Na K ↓ · HCO₃⁻ หลุด → กรดคั่ง", "SGLT2i: glucosuria", "sk"),
            ("TAL", "25%", "furosemide · bumetanide", "K ↓ · Ca ↓ · Mg ↓ · ด่าง", "แรงสุด (ตัดกลไกเข้มข้น)", "bad"),
            ("Early DT", "5%", "HCTZ · bendroflumethiazide", "K ↓ · Na ↓ · Ca ↑ · Mg ↓ · ด่าง", "Na ต่ำบ่อยกว่า loop", "ms"),
            ("Late DT/CD", "2–4%", "amiloride · spironolactone", "K ↑ · Na ↓ · กรดคั่ง", "\"K-sparing\"", "ok")]
    out = [t(14, 20, "ส่วน · Na⁺ ที่ดูดกลับ", "xs b mu"), t(150, 20, "ยา → รูปแบบเกลือแร่", "xs b mu")]
    y = 28
    for seg, pct, drug, pat, note, cl in rows:
        out += [rect(10, y, 400, 66, cl, 8), t(18, y + 22, seg, "sm b"), t(18, y + 44, pct, "lg b tac"),
                t(150, y + 20, drug, "sm b"), t(150, y + 38, pat, "xs"), t(150, y + 55, note, "xs i2")]
        y += 72
    out += [t(14, y + 10, "Na⁺ ที่ไม่ถูกดูดต้นทาง → ไปถึงปลายทาง → แลกเป็น K⁺ ที่ CD", "xs b i2")]
    return fig("แผนที่ยาขับปัสสาวะ — ตำแหน่งที่ออกฤทธิ์ทำนายเกลือแร่ที่ผิดปกติ",
               "สัดส่วน Na⁺ ที่แต่ละส่วนดูดกลับจากสไลด์ (PT 65% · TAL 25% · early DT 5% · CD ~2–4%) · ยาที่ออกฤทธิ์ **ก่อน** collecting duct ทุกตัวทำให้ **K ต่ำ** เพราะส่ง Na⁺ และน้ำไปถึง principal cell มากขึ้น (สไลด์เขียนซ้ำในทุกยา: \"↑tubular flow rate & ↑tubular [Na⁺] → ↑K⁺ secretion at P cell\") · loop vs thiazide ต่างกันที่ **Ca** (กลไกในภาพ TAL และ DT) · ยาที่ CD ทำตรงข้าม: K สูง · ด่าง/กรดและ Na ต่ำเพิ่มเติมจาก Guyton & Hall · SGLT2i ไม่อยู่ในสไลด์",
               svg(420, y + 18, "ตารางตำแหน่งออกฤทธิ์ของยาขับปัสสาวะในแต่ละส่วนของ nephron และความผิดปกติของเกลือแร่ที่เกิด", *out))


# ═══════════════════════════════════════ 12d ทำไม K ต่ำมาคู่กับด่าง
def hypok_alk():
    out = [
        box(10, 10, 400, 34, "ms", "loop / thiazide · อาเจียน · aldosterone เกิน", "b", fs=12),
        ar(110, 44, 110, 62, "lms", "ah-ms"), ar(310, 44, 310, 62, "lms", "ah-ms"),
        box(10, 64, 196, 64, "sk", "Na⁺ + น้ำ ไปถึง CD มาก\n(flow ↑ · Na⁺ ↑)", fs=11),
        box(214, 64, 196, 64, "sk", "ปริมาตรลด\n→ renin/AII/aldosterone ↑", fs=11),
        ar(110, 128, 110, 146, "lms", "ah-ms"), ar(310, 128, 310, 146, "lms", "ah-ms"),
        box(10, 148, 196, 64, "bad", "principal cell: ENaC ↑\nลูเมนลบ → หลั่ง K⁺ ↑\n→ K ต่ำ", fs=11),
        box(214, 148, 196, 64, "bad", "type A I-cell: H⁺-ATPase ↑\nหลั่ง H⁺ ↑ → HCO₃⁻ ใหม่\n→ ด่าง", fs=11),
        ar(110, 212, 110, 232, "lbad", "ah-bad"), ar(310, 212, 310, 232, "lbad", "ah-bad"),
        box(10, 234, 400, 76, "ac", "K ต่ำเองยิ่งทำให้ด่างคงอยู่: K⁺ ออกจากเซลล์แลก H⁺ เข้า (เซลล์เป็นกรด)\n→ ท่อไตหลั่ง H⁺ และสร้าง NH₄⁺ มากขึ้น · H⁺/K⁺-ATPase ดูด K⁺ แลก H⁺ ทิ้ง\n→ แก้ด่างไม่หายถ้าไม่เติม K (และ Cl⁻ + น้ำ)", fs=11),
    ]
    return fig("ทำไม K ต่ำมักมาคู่กับ metabolic alkalosis — สองทางที่ไปจบที่ collecting duct",
               "สไลด์สอนว่าทุกยาขับปัสสาวะที่ออกฤทธิ์ก่อน CD ทำให้ K ต่ำผ่าน **flow และ Na⁺ ที่ไปถึง principal cell** · ส่วนที่เชื่อมไปถึง \"ด่าง\" เติมจาก Guyton & Hall / Boron & Boulpaep: ปริมาตรที่ลดกระตุ้น **aldosterone** ซึ่งเพิ่มทั้ง ENaC (หลั่ง K⁺) และ **H⁺-ATPase ของ type A I-cell** (สไลด์: H⁺-ATPase — aldosterone +) · K ต่ำทำให้เซลล์ท่อไตเป็นกรดภายใน จึงหลั่ง H⁺/สร้าง NH₄⁺ ต่อ และ H⁺/K⁺-ATPase ยิ่งทิ้ง H⁺ — วงจรนี้เป็นเหตุที่ต้องแก้ K ก่อนด่างจึงหาย · กลไกกรด–ด่างเต็มรูปแบบอยู่ใน Part II",
               svg(420, 318, "กลไกที่ยาขับปัสสาวะและภาวะปริมาตรลดทำให้โพแทสเซียมต่ำและเลือดเป็นด่าง", *out))


# ═══════════════════════════════════════ 13a OAT / OCT secretion
def oat_oct():
    out = [rect(10, 28, 90, 220, "wa", 6), t(55, 46, "ลูเมน", "sm b mid twa"),
           rect(320, 28, 90, 220, "bad", 6), t(365, 46, "เลือด", "sm b mid tbad"),
           rect(116, 28, 188, 220, "bx", 6), t(210, 46, "เซลล์ PT ส่วนปลาย", "sm b mid")]
    out += [t(210, 70, "OA⁻ (กรดอ่อน)", "sm b mid tac")]
    out += _bl(94, "OA⁻", "lac", "ah-ac", rev=True) + [circ(304, 94, 8, "ac"), t(290, 98, "OAT1/3", "xs b end")]
    out += _out(94, "OA⁻", "lac", "ah-ac") + [circ(116, 94, 8, "ac"), t(130, 98, "MRP2/4", "xs b")]
    out += [t(210, 122, "PAH · penicillin · furosemide", "xs mid"), t(210, 136, "methotrexate · urate · probenecid", "xs mid")]
    out += [line(126, 146, 294, 146, "lru da")]
    out += [t(210, 166, "OC⁺ (ด่างอ่อน)", "sm b mid tms")]
    out += _bl(190, "OC⁺", "lms", "ah-ms", rev=True) + [circ(304, 190, 8, "ms"), t(290, 194, "OCT2", "xs b end")]
    out += _out(190, "OC⁺") + [circ(116, 190, 8, "ms"), t(130, 194, "MATE", "xs b")]
    out += [t(210, 218, "creatinine · metformin", "xs mid"), t(210, 232, "procainamide · cimetidine", "xs mid")]
    out += [t(10, 270, "สารที่ใช้ตัวขนส่งเดียวกัน \"แย่งคิว\" → อีกตัวค้างในเลือด", "sm b"),
            box(10, 280, 196, 74, "ac", "probenecid → penicillin\n(cidofovir) ค้าง\nNSAID → methotrexate ค้าง", fs=11),
            box(214, 280, 196, 74, "ms", "trimethoprim/cimetidine\n→ creatinine ↑ (GFR เท่าเดิม)\n→ procainamide ค้าง\npyrimethamine → metformin", fs=10.5)]
    return fig("การหลั่งสารอินทรีย์ที่ PT ส่วนปลาย — ประตูทางออกของยา และที่มาของ drug interaction",
               "ไตไม่ได้แค่กรอง — สารอินทรีย์ที่จับโปรตีน (กรองไม่ได้) ถูก **ดึงจากเลือดเข้าเซลล์ PT แล้วปล่อยลงลูเมน** ด้วยระบบ 2 ชุด: **organic anion** (OAT ด้านเลือด → MRP/BCRP ด้านลูเมน) และ **organic cation** (OCT ด้านเลือด → MATE/MDR ด้านลูเมน) · ตัวอย่างการแย่งตัวขนส่งทั้งหมดจากสไลด์ · ข้อ creatinine ↑ จาก trimethoprim/cimetidine ทั้งที่ GFR ไม่เปลี่ยนเป็นการเติมจากตำรา (creatinine เป็น OC⁺ ในสไลด์ และ ~10–20% ของ creatinine ในปัสสาวะมาจากการหลั่ง) · ชื่อตัวขนส่งย่อย (OAT1/3, MRP2/4, OCT2) จาก Boron & Boulpaep",
               svg(420, 362, "การหลั่ง organic anion และ organic cation ผ่านเซลล์ท่อไตส่วนต้นและตัวอย่าง drug interaction", *out))


# ═══════════════════════════════════════ 13b FE scale + FENa
def fe_scale():
    pos = [("glucose\nAA", 0, 26, "0%"), ("Na⁺", 1, 76, "1–2%"), ("Pi", 17, 140, "15–20%"), ("K⁺ · urea", 35, 204, "20–40%"),
           ("creatinine\ninulin", 100, 300, "100%"), ("PAH", 150, 388, "> 100%")]
    out = [box(10, 10, 400, 34, "ac", "FE_x = (U_x × P_Cr) / (P_x × U_Cr) × 100", "b", fs=12.5),
           line(20, 96, 400, 96, "ln w3"), t(210, 70, "FE (% ของที่กรองที่ออกในปัสสาวะ) — ไม่ใช่สเกลเชิงเส้น", "xs mid mu")]
    for name, v, x, lab in pos:
        c = "badf" if v == 0 else ("acf" if v < 100 else ("okf" if v == 100 else "msf"))
        out += [circ(x, 96, 6, c), t(x, 116, lab, "xs b mid"),
                t(x, 132, name, "xs mid")]
    out += [t(26, 162, "ดูดกลับหมด", "xs mid tbad"), t(300, 162, "กรองอย่างเดียว", "xs mid tok"), t(388, 162, "+ หลั่ง", "xs mid tms")]
    out += [t(10, 192, "FENa แยกสาเหตุ AKI (สไลด์)", "sm b"),
            box(10, 200, 196, 104, "ok", "Pre-renal (ไตขาดเลือด)\nท่อไตยังดี + AII/aldosterone\n→ ดูด Na⁺ เต็มที่\nFENa < 1%", fs=11),
            box(214, 200, 196, 104, "bad", "ATN (ท่อไตตาย)\nตัวขนส่ง Na⁺ เสีย\n→ Na⁺ หลุดลงปัสสาวะ\nFENa > 2%", fs=11),
            t(10, 326, "ได้ loop/thiazide มา → FENa สูงหลอก ใช้ FE_urea < 35% แทน (ตำรา)", "xs b i2")]
    return fig("Fractional excretion — สัดส่วนของที่กรองแล้ว \"หลุด\" ออกในปัสสาวะ บอกว่าท่อไตทำอะไรกับสารนั้น",
               "FE เทียบ clearance ของสารกับ clearance ของ creatinine (ตัวแทน GFR) — **V ตัดกันหายจึงใช้ปัสสาวะครั้งเดียว (spot urine) ได้** · ค่าปกติจากสไลด์: FENa 1–2% · FEK 30–40% · FEurea 20–40% · FEPi 15–20% · 0% = ดูดกลับหมด (glucose, AA) · 100% = กรองอย่างเดียว (inulin, creatinine) · > 100% = มีการหลั่ง (PAH, organic acid/base) · ตำแหน่งบนเส้นวาดแบบไม่เป็นสัดส่วน · การใช้ FEurea เมื่อได้ยาขับปัสสาวะเป็นการเติมจากตำรา (urea ถูกดูดกลับที่ PT ซึ่งยาเหล่านี้ไม่ได้ออกฤทธิ์)",
               svg(420, 334, "สเกล fractional excretion ของสารต่าง ๆ และการใช้ FENa แยก prerenal จาก ATN", *out))


# ═══════════════════════════════════════ 14a countercurrent + urea
def countercurrent():
    bands = [(300, 30, 96, "sk"), (600, 96, 166, "ms"), (900, 166, 236, "ms"), (1200, 236, 306, "bad")]
    out = []
    for v, y1, y2, c in bands:
        out += [rect(10, y1, 400, y2 - y1, c, 0), t(404, y1 + 16, "%s" % format(v, ","), "xs b end")]
    out += [t(14, 46, "cortex", "xs b mu"), t(14, 112, "medulla", "xs b mu"), t(14, 252, "papilla", "xs b mu"),
            t(404, 296, "mOsm/kg", "xs end mu"),
            # loop
            path("M90 20 L90 290 Q90 302 105 302 Q120 302 120 290 L120 20", "lwa w5"),
            t(90, 16, "300", "xs b mid twa"), t(126, 16, "100 →", "xs b twa"),
            ar(84, 130, 56, 130, "lwa w2", "ah-wa", "H₂O", "xs b mid twa", 0, -6), ar(84, 200, 56, 200, "lwa w2", "ah-wa", "H₂O", "xs b mid twa", 0, -6),
            ar(84, 266, 56, 266, "lwa w2", "ah-wa", "H₂O", "xs b mid twa", 0, -6),
            ar(126, 190, 156, 190, "lms w2", "ah-ms", "NaCl", "xs b mid tms", 0, -6), ar(126, 262, 156, 262, "lms w2", "ah-ms", "NaCl", "xs b mid tms", 0, -6),
            ar(126, 120, 156, 120, "lms w3", "ah-ms", "NaCl (TAL)", "xs b mid tms", 10, -6),
            # vasa recta
            path("M200 30 L200 290 Q200 300 212 300 Q224 300 224 290 L224 30", "lbad w2 da"),
            t(212, 20, "vasa recta", "xs b mid tbad"),
            # collecting duct
            path("M300 20 L300 312", "lac w5"), t(300, 16, "CD", "xs b mid tac"),
            ar(306, 120, 334, 120, "lwa w2", "ah-wa", "H₂O", "xs b mid twa", 6, -6), ar(306, 190, 334, 190, "lwa w2", "ah-wa", "H₂O", "xs b mid twa", 6, -6),
            ar(306, 262, 334, 262, "lac w2", "ah-ac", "urea", "xs b mid tac", 6, -6),
            t(340, 278, "UT-A1", "xs tac")]
    out += [box(10, 318, 196, 62, "ok", "ADH มาก (ขาดน้ำ · SIADH)\nAQP2 + UT-A1 → น้ำออก\nปัสสาวะ ~1,200", fs=11),
            box(214, 318, 196, 62, "wa", "ไม่มี ADH (ดื่มน้ำมาก · DI)\nCD ไม่ซึมน้ำ\nปัสสาวะ 50–100", fs=11)]
    return fig("Countercurrent — loop สร้างความเข้มข้นใน medulla · vasa recta รักษาไว้ · ADH ตัดสินว่าใช้หรือไม่",
               "**Countercurrent multiplication** (loop of Henle): ขาลงซึมน้ำแต่ไม่ซึมเกลือ (น้ำออก 15%) ขาขึ้นไม่ซึมน้ำแต่ดูดเกลือ → ทิ้ง NaCl ไว้ใน medulla และส่งของเหลวเจือจาง ~100 mOsm ไปปลายทาง (ADH ↑ / loop diuretic ↓) · **Countercurrent exchanger** (vasa recta) ไหลรูปตัว U จึงไม่ชะเกลือออก — เลือดไหลเร็ว (volume overload, osmotic diuretic) จะ washout · **urea recycling** ให้ ~40–50% (500–600 mOsm) ของความเข้มข้นใน inner medulla (ADH เพิ่ม UT-A1 · กินโปรตีนมากเพิ่ม) · CD ใช้ gradient นี้ดูดน้ำเมื่อมี ADH → ปัสสาวะ 50–1,200 mOsm/kg · การควบคุม ADH/กระหายน้ำอยู่ใน Part II",
               svg(420, 388, "แผนภาพ countercurrent multiplication ใน loop of Henle vasa recta และ collecting duct พร้อมความเข้มข้นของ medulla", *out))


# ═══════════════════════════════════════ 14b Cosm / CH2O
def ch2o():
    rows = [("ดื่มน้ำมาก / DI", "U 100 · V 3 mL/min", 1.0, 2.0, "+2.0", "tok", "C_H₂O บวก = ขับน้ำเปล่าทิ้ง"),
            ("isosmotic (ATN · loop นาน)", "U 300 · V 1 mL/min", 1.0, 0.0, "0", "i2", "เจือจาง/เข้มข้นไม่ได้"),
            ("ขาดน้ำ / SIADH", "U 600 · V 0.5 mL/min", 1.0, -0.5, "−0.5", "tbad", "C_H₂O ลบ = เก็บน้ำเปล่าไว้")]
    S = 80
    out = [box(10, 10, 400, 34, "ac", "C_osm = (U_osm × V) / P_osm · C_H₂O = V − C_osm", "b", fs=12.5),
           t(14, 64, "P_osm 300 · แถบ = ปริมาตรปัสสาวะต่อนาที", "xs mu")]
    y = 74
    for name, sub, cos, cw, val, tc, note in rows:
        out += [t(14, y + 14, name, "sm b"), t(14, y + 28, sub, "xs i2"),
                rect(180, y + 4, cos * S, 26, "sk", 4),
                t(180 + cos * S / 2, y + 21, "C_osm 1", "xs mid b")]
        if cw > 0:
            out += [rect(180 + cos * S, y + 4, cw * S, 26, "wa", 4), t(180 + cos * S + cw * S / 2, y + 21, "C_H₂O " + val, "xs mid b twa")]
        elif cw < 0:
            out += [rect(180 + (cos + cw) * S, y + 33, -cw * S, 7, "badf", 2), t(180 + cos * S + 6, y + 21, "C_H₂O " + val, "xs b tbad"),
                    t(180 + cos * S + 6, y + 40, "(V เหลือ 0.5)", "xs tbad")]
        else:
            out += [t(180 + cos * S + 6, y + 21, "C_H₂O 0", "xs b")]
        out += [t(14, y + 46, note, "xs b " + tc)]
        y += 66
    out += [box(10, y + 4, 196, 54, "wa", "Water diuresis\nC_H₂O ↑↑↑ · C_osm ↔", fs=11),
            box(214, y + 4, 196, 54, "ms", "Osmotic diuresis\nC_osm ↑↑↑ · C_H₂O ↓", fs=11)]
    return fig("Osmolal clearance และ free water clearance — แบ่งปัสสาวะเป็น \"น้ำที่พาตัวละลาย\" กับ \"น้ำเปล่า\"",
               "**C_osm** = ปริมาตรที่จะขนตัวละลายทั้งหมดในปัสสาวะได้ ถ้าเข้มข้นเท่าพลาสมา (ปกติ ~3 mL/min · เพิ่มเมื่อกินโปรตีนมาก ได้ยาขับปัสสาวะ เบาหวาน) · ส่วนที่เหลือของ V คือ **C_H₂O** (ปกติ ~ −1 mL/min) — บวก = ไตทิ้งน้ำเปล่า (ไม่มี ADH) · ลบ = ไตเก็บน้ำเปล่าไว้ (มี ADH) · 0 = เจือจาง/เข้มข้นไม่ได้ · ตัวอย่างตัวเลขทั้งสามแถวผู้เขียนตั้งให้ C_osm = 1 เพื่อเทียบง่าย · **water diuresis** (ดื่มน้ำ, DI) กับ **osmotic diuresis** (ยาขับปัสสาวะ, เบาหวาน) ต่างกันที่ส่วนไหนเพิ่ม (สไลด์)",
               svg(420, y + 66, "แถบเปรียบเทียบ osmolal clearance และ free water clearance ในปัสสาวะเจือจาง เท่าพลาสมา และเข้มข้น", *out))
