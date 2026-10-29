# -*- coding: utf-8 -*-
"""ภาพเคลื่อนไหวกลไก (section.anims) + หลักจำ (section.mnem) ของคาบ gi "Diarrhea"
build_diarrhea.py นำ ITEMS/MNEM ไปใส่ในหัวข้อ · รูปแบบตาม dashboard/learn_anim/SPEC.md
ตรวจ:  python3 anims_gi_diarrhea.py <out.json>  แล้ว  python3 ../../dashboard/anim_tool.py check ../data <out.json>"""
import json, re, sys
from svg import t, rect, circ, ell, line, ar, path, box, esc


def S(k, *parts, x=None):
    """กลุ่มที่โผล่ตั้งแต่ขั้น k (และหายตั้งแต่ขั้น x ถ้าระบุ)"""
    a = ' data-s="%d"' % k + ((' data-x="%d"' % x) if x else "")
    return "<g%s>%s</g>" % (a, "".join(p for p in parts if p))


def X(k, *parts):
    return '<g data-x="%d">%s</g>' % (k, "".join(p for p in parts if p))


def G(c, *parts):
    return '<g class="%s">%s</g>' % (c, "".join(p for p in parts if p))


def mover(r, c, dur, d, begin="0s"):
    """อนุภาควิ่งตาม path (M/L พิกัดสัมบูรณ์) · วางวงกลมที่จุดเริ่มด้วย cx/cy และแปลง path เป็นระยะจากจุดนั้น
    ภาพนิ่ง (ปิด motion) จึงเห็นอนุภาคที่ต้นทาง ไม่ค้างที่มุม (0,0)"""
    nums = [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", d)]
    x0, y0 = nums[0], nums[1]
    pts = [(nums[i] - x0, nums[i + 1] - y0) for i in range(0, len(nums), 2)]
    rel = "M0 0 " + " ".join("L%g %g" % p for p in pts[1:])
    return ('<circle cx="%g" cy="%g" r="%s" class="%s"><animateMotion dur="%s" begin="%s" repeatCount="indefinite" path="%s"/></circle>'
            % (x0, y0, r, c, dur, begin, rel))


def SVG(w, h, label, *parts):
    return ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg">' % (w, h, esc(label))
            + "".join(p for p in parts if p) + "</svg>")


# ───────────────────────── 1 · น้ำไหลผ่านลำไส้: ปริมาณบอกตำแหน่ง
def a_flow():
    tube_y, th = 70, 50
    p = []
    p.append(t(20, 58, "เข้า ~10 L/วัน", "sm b tac"))
    p.append(rect(20, tube_y, 200, th, "ac", 10))
    p.append(t(120, 92, "ลำไส้เล็ก", "mid b"))
    p.append(rect(230, tube_y, 130, th, "ok", 10))
    p.append(t(295, 92, "ลำไส้ใหญ่", "mid b"))
    p.append(rect(370, tube_y, 52, th, "sk", 10))
    p.append(t(396, 92, "rectum", "sm mid b"))
    p.append(line(28, 110, 414, 110, "lac w2 fl"))
    # น้ำผ่าน ileocecal valve
    p.append(X(2, t(225, 62, "~1.5 L", "xs mid b")))
    p.append(S(3, t(225, 62, "~1.5 L", "xs mid b")))
    p.append(S(2, t(225, 62, "หลายลิตร", "xs mid b tbad"), x=3))
    # ดูดกลับ
    p.append(ar(120, 122, 120, 156, "lok w2", "ah-ok"))
    p.append(t(128, 146, "ดูดกลับ ~8.5 L", "sm tok"))
    p.append(ar(295, 122, 295, 156, "lok w2", "ah-ok"))
    p.append(t(303, 146, "ดูดกลับ ~1.4 L", "sm tok"))
    p.append(t(230, 176, "ความจุสูงสุด ~4–5 L/วัน", "xs mu"))
    # ทางออก
    p.append(ar(396, 122, 396, 192, "lac w2", "ah-ac"))
    p.append(X(2, t(430, 212, "ออก ~0.1 L", "sm b end")))
    # หยดน้ำไหล (ปกติ)
    p.append(X(2, mover(3.5, "acf", "3.2s", "M30 100 L410 100"), mover(3.5, "acf", "3.2s", "M30 100 L410 100", "-1.6s")))
    # ขั้น 2 · cholera
    p.append(S(2,
        ar(140, 30, 140, 66, "lbad w2", "ah-bad"), ar(196, 30, 196, 66, "lbad w2", "ah-bad"),
        t(110, 24, "toxin → ลำไส้เล็กหลั่งน้ำเพิ่มหลายลิตร", "sm tbad b"),
        mover(3.5, "badf", "1.3s", "M30 100 L410 100"), mover(3.5, "badf", "1.3s", "M30 100 L410 100", "-.45s"),
        mover(3.5, "badf", "1.3s", "M30 100 L410 100", "-.9s"),
        t(230, 194, "รับเกินความจุ → ดูดไม่ทัน", "sm tbad b"),
        t(430, 212, "ถ่ายน้ำปริมาณมาก", "sm b tbad end"), x=3))
    # ขั้น 3 · rectosigmoid อักเสบ
    p.append(S(3,
        G("pl", rect(370, tube_y, 52, th, "bad", 10)), t(396, 92, "rectum", "sm mid b"),
        t(386, 194, "อักเสบ → รับแรงยืดไม่ได้", "sm tbad b end"),
        t(430, 212, "ถ่ายน้อย ถี่ ปวดเบ่ง มูกเลือด", "sm b tbad end"),
        mover(3.5, "acf", "3.2s", "M30 100 L410 100")))
    # ขั้น 4 · สรุป
    p.append(S(4,
        rect(20, 236, 196, 150, "ac"), t(118, 260, "ลำไส้เล็ก / colon ขวา", "mid b"),
        t(34, 290, "• ปริมาณมาก เป็นน้ำ", "sm"), t(34, 314, "• ปวดรอบสะดือ ขาดน้ำเร็ว", "sm"),
        t(34, 338, "• ไม่ค่อยมีเลือด", "sm"), t(34, 366, "cholera · ETEC · ไวรัส · Giardia", "xs i2"),
        rect(226, 236, 196, 150, "bad"), t(324, 260, "colon ซ้าย / rectum", "mid b"),
        t(240, 290, "• น้อย ถี่ ปวดเร่ง", "sm"), t(240, 314, "• ปวดเบ่ง (tenesmus)", "sm"),
        t(240, 338, "• มูกเลือด", "sm"), t(240, 366, "Shigella · amoeba · UC", "xs i2")))
    return SVG(440, 400, "ภาพเคลื่อนไหว: น้ำราวสิบลิตรต่อวันเข้าลำไส้เล็ก ถูกดูดกลับเกือบหมด เหลือออกมาหนึ่งร้อยมิลลิลิตร "
               "ถ้าลำไส้เล็กหลั่งน้ำเกินความจุของลำไส้ใหญ่จะถ่ายน้ำปริมาณมาก ถ้า rectum อักเสบจะถ่ายน้อยถี่ปวดเบ่งมีมูกเลือด", *p)


FLOW_STEPS = [
    {"t": "ปกติ: เข้า 10 ลิตร ออก 0.1 ลิตร",
     "cap": "น้ำจากอาหารและน้ำย่อยเข้าลำไส้เล็ก **~10 L/วัน** · ลำไส้เล็กดูดกลับ ~8.5 L · ผ่าน ileocecal valve ~1.5 L · ลำไส้ใหญ่ดูดอีก ~1.4 L → **ออกมาราว 0.1 L** · ลำไส้ใหญ่ยังดูดเพิ่มได้ถึง **~4–5 L/วัน**"},
    {"t": "ลำไส้เล็กหลั่งเกิน → ถ่ายน้ำปริมาณมาก",
     "cap": "toxin ของ **cholera/ETEC** ทำให้ลำไส้เล็ก **หลั่งน้ำเพิ่มหลายลิตร** → น้ำที่ส่งต่อ **เกินความจุของลำไส้ใหญ่** แม้ลำไส้ใหญ่ปกติ → **ถ่ายน้ำปริมาณมาก ขาดน้ำเร็ว** ปวดไม่มาก"},
    {"t": "Rectum อักเสบ → น้อย ถี่ ปวดเบ่ง",
     "cap": "ปริมาณน้ำปกติ แต่ **rectosigmoid ที่อักเสบเสียหน้าที่เป็นที่พักอุจจาระ (reservoir)** — อุจจาระเพียงเล็กน้อยก็กระตุ้นให้ต้องถ่าย → **ถ่ายน้อย ถี่ ปวดเร่ง ปวดเบ่ง** แผลที่เยื่อบุ → **มูกเลือด**"},
    {"t": "สรุป: ปริมาณและอาการร่วมบอกตำแหน่ง",
     "cap": "**มาก เป็นน้ำ ขาดน้ำเร็ว = ลำไส้เล็ก/colon ขวา** · **น้อย ถี่ ปวดเบ่ง มูกเลือด = colon ซ้าย/rectum** — ใช้คัดว่าจะส่องกล้องส่วนไหนและนึกถึงเชื้ออะไร"},
]


# ───────────────────────── 2 · ความลึกที่เชื้อรุกล้ำ
def a_invasion():
    p = []
    p.append(t(14, 30, "โพรงลำไส้", "xs mu"))
    p.append(t(14, 186, "ใต้เยื่อบุ (lamina propria)", "xs mu"))
    xs = [30 + i * 62 for i in range(6)]
    for x in xs:
        p.append(rect(x, 112, 58, 56, "bx", 6))
        p.append(circ(x + 29, 148, 7, "sk"))
        for k in range(5):
            p.append(line(x + 8 + k * 10, 112, x + 8 + k * 10, 104, "lmu"))
    p.append(t(14, 104, "เยื่อบุ", "xs mu"))
    p.append(rect(30, 226, 370, 24, "bad", 12))
    p.append(t(42, 242, "หลอดเลือด", "xs b"))
    p.append(ar(424, 40, 424, 246, "lbad w2", "ah-bad"))
    p.append(t(424, 30, "ลึก", "xs mid tbad b"))
    p.append(rect(20, 272, 400, 138, "sk"))
    # ขั้น 1
    p.append(S(1, t(34, 300, "เยื่อบุปกติ — ดูดน้ำกลับ", "b"),
               t(34, 326, "เรียงตามความลึก: toxin → เกาะผิว → ทำลายเซลล์", "sm"),
               t(34, 348, "→ บุกเนื้อเยื่อ → เข้ากระแสเลือด", "sm"), x=2))
    # ขั้น 2 · toxin
    p.append(S(2,
        ell(110, 66, 13, 7, "acf"), ell(250, 58, 13, 7, "acf"),
        circ(140, 90, 3, "msf"), circ(180, 96, 3, "msf"), circ(280, 92, 3, "msf"), circ(220, 100, 3, "msf"),
        line(150, 102, 150, 72, "lwa w2 fl"), line(212, 102, 212, 72, "lwa w2 fl"), line(274, 102, 274, 72, "lwa w2 fl"),
        t(300, 52, "Cl⁻ + น้ำ", "sm twa b"), x=3))
    p.append(S(2, t(34, 300, "Toxin: cholera · ETEC · preformed", "b"),
               t(34, 326, "cAMP ↑ → หลั่งน้ำ · เซลล์ไม่ตาย", "sm"),
               t(34, 350, "ถ่ายน้ำมาก · อาเจียน · ไม่มีไข้ · ไม่มี WBC", "sm tac b"), x=3))
    # ขั้น 3 · cytotoxin
    p.append(S(3,
        G("pl", rect(154, 112, 58, 56, "bad", 6), rect(216, 112, 58, 56, "bad", 6)),
        t(214, 150, "เซลล์ตาย", "xs mid b tbad")))
    p.append(S(3, t(34, 300, "Cytotoxin: C. difficile · EHEC", "b"),
               t(34, 326, "toxin ทำลายเซลล์เยื่อบุ (Shiga toxin → HUS)", "sm"),
               t(34, 350, "ปวดมาก · ไข้ต่ำ–ปานกลาง · บางครั้งมีเลือด", "sm tac b"), x=4))
    # ขั้น 4 · invasive
    p.append(S(4,
        ell(320, 140, 10, 6, "acf"), ell(160, 200, 10, 6, "acf"), ell(330, 200, 10, 6, "acf"),
        G("pl", circ(300, 204, 6, "msf"), circ(350, 188, 6, "msf"), circ(130, 212, 6, "msf"), circ(90, 184, 6, "msf")),
        t(312, 220, "neutrophil", "xs b"),
        circ(170, 92, 4, "badf"), circ(196, 80, 4, "badf"), circ(232, 88, 4, "badf"),
        t(120, 54, "เลือด + มูก + WBC", "sm tbad b")))
    p.append(S(4, t(34, 300, "Invasive: Shigella · EIEC · E. histolytica", "b"),
               t(34, 326, "บุกเข้าเนื้อเยื่อ → อักเสบ → แผล", "sm"),
               t(34, 350, "ไข้สูง · ปวดบิด · ปวดเบ่ง · มูกเลือด = dysentery", "sm tac b"), x=5))
    # ขั้น 5 · systemic
    p.append(S(5,
        mover(5, "acf", "2.6s", "M40 238 L392 238"), mover(5, "acf", "2.6s", "M40 238 L392 238", "-1.3s"),
        ar(160, 208, 160, 226, "lbad w2", "ah-bad")))
    p.append(S(5, t(34, 300, "Systemic: typhoid · listeriosis · hepatitis", "b"),
               t(34, 326, "เชื้อเข้ากระแสเลือด → ไข้ อาการทั้งตัวเด่น", "sm"),
               t(34, 350, "ท้องเสียเป็นแค่อาการร่วม — ต้องหาโรคหลัก", "sm tac b")))
    p.append(S(5, t(34, 386, "ยิ่งลึก → ยิ่งไข้ ปวดบิด และมีเลือด", "sm b tbad")))
    return SVG(440, 420, "ภาพเคลื่อนไหว: เชื้อก่อท้องเสียเรียงตามความลึก toxin กระตุ้นการหลั่งน้ำโดยเซลล์ไม่ตาย "
               "cytotoxin ทำลายเซลล์ เชื้อ invasive บุกเนื้อเยื่อมีเม็ดเลือดขาวและเลือด systemic เข้ากระแสเลือด", *p)


INV_STEPS = [
    {"t": "เยื่อบุปกติ",
     "cap": "เยื่อบุลำไส้หนึ่งชั้นเรียงบน lamina propria ที่มีหลอดเลือด · สไลด์เรียงกลไกของเชื้อ **ตามความลึกที่รุกล้ำ** — ใช้ทำนายอาการได้ทันที"},
    {"t": "Toxin — หลั่งน้ำโดยเซลล์ไม่ตาย",
     "cap": "**cholera, ETEC** ปล่อย enterotoxin เกาะผิว → **cAMP/cGMP สูง → หลั่ง Cl⁻ และน้ำ** · **preformed toxin (B. cereus, S. aureus)** อาเจียนภายในไม่กี่ชั่วโมง · เซลล์ไม่ตาย → **ไม่มีไข้ ไม่มีเม็ดเลือดขาว**"},
    {"t": "Cytotoxin — ทำลายเซลล์",
     "cap": "**C. difficile (toxin A/B)** และ **EHEC (Shiga toxin)** ทำลายเซลล์เยื่อบุ → **ปวดท้องมาก** อาจมีเลือด · Shiga toxin เข้ากระแสเลือดทำลาย endothelium ของไต → **HUS** — **ห้ามให้ยาปฏิชีวนะใน STEC**"},
    {"t": "Invasive — บุกเข้าเนื้อเยื่อ",
     "cap": "**Shigella, EIEC, E. histolytica** (และ Salmonella, Campylobacter ระดับปานกลาง) เข้าเซลล์และใต้เยื่อบุ → **neutrophil มารวม แผล** → **ไข้สูง ปวดบิด ปวดเบ่ง ถ่ายน้อยถี่มีมูกเลือดและ WBC** = dysentery"},
    {"t": "Systemic — เข้ากระแสเลือด",
     "cap": "เชื้อ/โรคที่เข้ากระแสเลือด (typhoid, listeriosis, hepatitis, SARS-CoV-2) → **อาการทั้งตัวกลบท้องเสีย** · หลักจำ: **ยิ่งลึก ยิ่งไข้ ปวดบิด และมีเลือด** — จึงห้ามใช้ loperamide เดี่ยวเมื่อมีไข้หรือเลือด"},
]


# ───────────────────────── 3 · ORS กับ SGLT1
def a_sglt1():
    p = []
    p.append(t(14, 30, "โพรงลำไส้", "xs mu"))
    p.append(rect(20, 120, 88, 150, "sk", 6))
    p.append(rect(332, 120, 88, 150, "sk", 6))
    p.append(rect(120, 120, 200, 150, "bx", 8))
    p.append(t(205, 170, "เซลล์เยื่อบุ", "sm mid mu"))
    p.append(t(205, 188, "ลำไส้เล็ก", "sm mid mu"))
    for k in range(9):
        p.append(line(130 + k * 22, 120, 130 + k * 22, 110, "lmu"))
    p.append(rect(20, 292, 400, 36, "bad", 10))
    p.append(t(30, 315, "หลอดเลือด", "xs b"))
    # ตัวพา
    p.append(ell(165, 122, 22, 12, "ok"))
    p.append(t(165, 126, "SGLT1", "xs mid b"))
    p.append(ell(282, 122, 20, 12, "ms"))
    p.append(t(282, 126, "CFTR", "xs mid b"))
    p.append(ell(165, 268, 22, 12, "ok"))
    p.append(t(165, 272, "GLUT2", "xs mid b"))
    p.append(circ(250, 268, 14, "ac"))
    p.append(t(250, 272, "Na/K", "xs mid b"))
    p.append(rect(20, 340, 400, 74, "sk"))
    # ขั้น 1
    p.append(S(1, t(34, 364, "ปกติ: เกลือและน้ำถูกดูดกลับ", "b"),
               t(34, 390, "SGLT1 ขน glucose 1 + Na⁺ 2 เข้าเซลล์", "sm"), x=2))
    # ขั้น 2 · cholera
    p.append(S(2,
        G("pl", ell(282, 122, 20, 12, "bad")), t(282, 126, "CFTR", "xs mid b"),
        line(282, 108, 282, 50, "lwa w3 fl rv"), line(300, 110, 330, 50, "lwa w2 fl rv"),
        t(296, 42, "Cl⁻ + น้ำ ไหลออก", "sm twa b")))
    p.append(S(2, t(34, 364, "Cholera toxin → cAMP ↑ → CFTR เปิดค้าง", "b"),
               t(34, 390, "หลั่ง Cl⁻ และน้ำออก · แต่ SGLT1 ยังปกติ", "sm tac b"), x=3))
    # ขั้น 3 · ORS เข้า
    p.append(S(3,
        t(24, 56, "ORS", "lg b tok"),
        circ(30, 74, 4, "okf"), t(40, 78, "glucose", "xs tok b"), circ(30, 92, 4, "acf"), t(40, 96, "Na⁺", "xs tac b"),
        mover(5, "okf", "2.4s", "M110 60 L165 120"), mover(4, "acf", "2.4s", "M124 82 L160 120", "-.8s"),
        mover(4, "acf", "2.4s", "M140 50 L170 120", "-1.6s")))
    p.append(S(3, t(34, 364, "ให้ ORS: glucose + 2 Na⁺ เข้าทาง SGLT1", "b"),
               t(34, 390, "toxin ไม่ได้ทำลายตัวพานี้", "sm tac b"), x=4))
    # ขั้น 4 · ออกด้านเลือด น้ำตาม
    p.append(S(4,
        mover(5, "okf", "2.4s", "M165 136 L165 300"), mover(4, "acf", "2.4s", "M175 140 L250 282 L250 302", "-.4s"),
        line(114, 104, 114, 290, "lok w3 fl"), line(326, 104, 326, 290, "lok w3 fl"),
        line(296, 136, 296, 288, "lok w2 fl"),
        t(54, 290, "น้ำตาม", "sm tok b"), t(354, 290, "น้ำตาม", "sm tok b")))
    p.append(S(4, t(34, 364, "Na⁺ ถูกปั๊มออก · glucose ออกทาง GLUT2", "b"),
               t(34, 390, "Cl⁻ และน้ำตาม → ดูดกลับมากกว่าที่หลั่ง", "sm tok b"), x=5))
    p.append(S(5, t(34, 364, "น้ำเปล่า/เกลืออย่างเดียว ไม่ได้ผลเท่า", "b"),
               t(34, 390, "น้ำอัดลม: น้ำตาลสูง Na ต่ำ → ดึงน้ำเข้าลำไส้", "sm tbad b")))
    return SVG(440, 420, "ภาพเคลื่อนไหว: cholera toxin เปิด CFTR ให้หลั่ง Cl และน้ำ แต่ SGLT1 ยังทำงาน "
               "เมื่อให้ ORS glucose คู่ Na เข้าเซลล์ Na ถูกปั๊มออก glucose ออกทาง GLUT2 น้ำไหลตามกลับเข้าเลือด", *p)


SGLT_STEPS = [
    {"t": "เซลล์เยื่อบุลำไส้เล็กปกติ",
     "cap": "ด้านโพรงลำไส้มี **SGLT1** (ขน glucose คู่ Na⁺) และช่อง **CFTR** (หลั่ง Cl⁻) · ด้านเลือดมี **GLUT2** และ **Na⁺/K⁺-ATPase** · น้ำผ่านได้ระหว่างเซลล์"},
    {"t": "Cholera toxin เปิด CFTR ค้าง",
     "cap": "toxin → Gsα ทำงานตลอด → **cAMP สูง → CFTR หลั่ง Cl⁻ น้ำตามออก** และยับยั้งการดูด NaCl ปกติ → ถ่ายน้ำปริมาณมาก · **แต่ SGLT1 ไม่ถูกแตะ**"},
    {"t": "ORS: glucose ลากโซเดียมเข้าเซลล์",
     "cap": "ORS ให้ **glucose และ Na⁺ คู่กัน** → SGLT1 ขน **glucose 1 + Na⁺ 2** เข้าเซลล์ · จึงต้องมีทั้งน้ำตาลและเกลือในสัดส่วนที่เหมาะ (สูตรลดออสโมลาริตี glucose 75 Na 75)"},
    {"t": "น้ำตามเกลือกลับเข้าเลือด",
     "cap": "Na⁺ ถูก **Na⁺/K⁺-ATPase** ปั๊มออกด้านเลือด glucose ออกทาง **GLUT2** → ช่องระหว่างเซลล์เข้มข้นขึ้น → **Cl⁻ และน้ำไหลตาม** → **ดูดกลับมากกว่าที่ toxin หลั่ง**"},
    {"t": "ทำไมเครื่องดื่มอื่นใช้แทนไม่ได้",
     "cap": "น้ำเปล่าไม่มี Na⁺/glucose ให้ลาก · **น้ำอัดลม เครื่องดื่มเกลือแร่สำหรับนักกีฬา** น้ำตาลสูง Na ต่ำ → **ออสโมลาริตีสูงดึงน้ำเข้าโพรงลำไส้** ถ่ายมากขึ้น → ใช้ ORS หรือสูตรทำเอง เกลือ 1 + น้ำตาล 8 ช้อนชา ต่อน้ำ 1 ลิตร"},
]


# ───────────────────────── 4 · Stool osmotic gap
def a_gap():
    base, top = 300, 100          # 290 mOsm/kg = 200 px
    k = 200 / 290.0
    def bar(x, salt, label_salt, cls_gap="ms"):
        o = []
        hs = salt * k
        o.append(rect(x, base - hs, 90, hs, "wa", 3))
        o.append(t(x + 45, base - hs / 2 + 4, label_salt, "xs mid b"))
        if salt < 290:
            o.append(rect(x, top, 90, base - hs - top, cls_gap, 3))
        return o
    p = []
    p.append(t(220, 28, "gap = 290 − 2 × (Na⁺ + K⁺ ในอุจจาระ)", "mid b"))
    p.append(t(220, 50, "290 = osmolality อุจจาระในลำไส้ (เท่าพลาสมา)", "sm mid mu"))
    p.append(line(30, top, 420, top, "lmu da"))
    p.append(t(30, top - 6, "290", "xs b"))
    p.append(line(30, base, 420, base, "ln"))
    # ขั้น 2 · secretory
    c1 = 55
    p.append(S(2, *bar(c1, 280, "เกลือ 280"),
               t(c1 + 45, top - 6, "gap 10", "xs mid b tms"),
               t(c1 + 45, 320, "Secretory", "sm mid b"),
               t(c1 + 45, 338, "Na 95 · K 45", "xs mid"),
               t(c1 + 45, 356, "gap < 50", "sm mid b twa")))
    # ขั้น 3 · osmotic
    c2 = 175
    p.append(S(3, *bar(c2, 110, "เกลือ 110"),
               t(c2 + 45, 170, "lactose", "sm mid b"), t(c2 + 45, 186, "+ กรดจาก", "xs mid"), t(c2 + 45, 200, "การหมัก", "xs mid"),
               t(c2 + 45, 320, "Osmotic", "sm mid b"),
               t(c2 + 45, 338, "Na 30 · K 25", "xs mid"),
               t(c2 + 45, 356, "gap 180 > 100", "sm mid b tms"),
               t(c2 + 45, 216, "pH < 6", "xs mid b tbad")))
    # ขั้น 4 · งดอาหาร
    p.append(S(4,
        G("pl", rect(c1 - 4, 366, 98, 24, "ok", 12)), t(c1 + 45, 382, "งดอาหาร: ยังถ่าย", "xs mid b"),
        G("pl", rect(c2 - 4, 366, 98, 24, "ok", 12)), t(c2 + 45, 382, "งดอาหาร: หยุด", "xs mid b")))
    # ขั้น 5 · ติดลบ
    c3 = 300
    hs = 320 * k
    p.append(S(5,
        rect(c3, base - hs, 90, hs, "wa", 3),
        rect(c3, base - hs, 90, top - (base - hs), "bad", 3),
        t(c3 + 45, base - 60, "2(Na+K) 320", "xs mid b"),
        t(c3 + 45, base - hs - 6, "gap −30", "xs mid b tbad"),
        t(c3 + 45, 320, "ติดลบ", "sm mid b tbad"),
        t(c3 + 45, 338, "Na 120 · K 40", "xs mid"),
        t(c3 + 45, 356, "PO₄/SO₄ ยาระบาย", "xs mid b tbad")))
    return SVG(440, 400, "ภาพเคลื่อนไหว: stool osmotic gap เท่ากับ 290 ลบสองเท่าของโซเดียมบวกโพแทสเซียม "
               "secretory เกลือเกือบเต็ม gap ต่ำกว่า 50 osmotic มีสารอื่นเช่น lactose gap มากกว่า 100 "
               "งดอาหารแล้ว osmotic หยุด secretory ยังถ่าย gap ติดลบจากยาระบาย phosphate sulfate", *p)


GAP_STEPS = [
    {"t": "หลักคิด: 290 = เกลือ + สารอื่น",
     "cap": "อุจจาระในลำไส้มี osmolality **เท่าพลาสมา ~290** (ไม่ใช้ค่าที่วัดได้ เพราะแบคทีเรียหมักต่อหลังเก็บ) · ส่วนที่เป็นเกลือประมาณด้วย **2 × (Na⁺ + K⁺)** · ที่เหลือคือ **gap** = สารอื่นที่ดึงน้ำ"},
    {"t": "Secretory: เกลือเต็มเกือบหมด",
     "cap": "เยื่อบุ **หลั่งเกลือออกมาเอง** → น้ำในอุจจาระคือ \"น้ำเกลือ\" · 2(95 + 45) = 280 → **gap 10 (< 50)** · เช่น VIPoma, carcinoid, microscopic colitis, bile acid, ติดเชื้อ"},
    {"t": "Osmotic: สารที่ดูดซึมไม่ได้แทนที่เกลือ",
     "cap": "**lactose** ที่ย่อยไม่ได้ (หรือ Mg, sorbitol, PEG) ดึงน้ำไว้ · เกลือจึงเหลือน้อย 2(30 + 25) = 110 → **gap 180 (> 100)** · แบคทีเรียหมักคาร์โบไฮเดรตเป็นกรด → **pH < 6**"},
    {"t": "ทดสอบงดอาหาร",
     "cap": "**Osmotic หยุดเมื่องดอาหาร** (ไม่มีสารดึงน้ำเข้ามา) · **Secretory ยังถ่ายต่อ** รวมทั้งตอนกลางคืน — ใช้ยืนยันผล gap ได้ข้างเตียง"},
    {"t": "Gap ติดลบ = นึกถึงยาระบาย",
     "cap": "Na และ K จับคู่กับ **anion หลายประจุ (phosphate, sulfate)** ที่ดูดซึมได้น้อย → สูตร 2(Na+K) ประเมินเกินจริง → 2(120 + 40) = 320 → **gap −30** → ส่ง **laxative screen** (แอบกินยาระบาย)"},
]


# ───────────────────────── 5 · ถ่ายเป็นมัน: 3 ขั้นของการดูดซึมไขมัน
def a_fat():
    p = []
    p.append(t(14, 24, "โพรงลำไส้เล็ก", "xs mu"))
    # แหล่ง lipase และน้ำดี
    p.append(box(110, 32, 90, 26, "ac", "ตับอ่อน", "sm b"))
    p.append(box(240, 32, 110, 26, "ok", "ตับ/ถุงน้ำดี", "sm b"))
    p.append(ar(155, 58, 155, 80, "lac w2", "ah-ac", "lipase", "xs b tac", dx=24, dy=0))
    p.append(ar(295, 58, 295, 80, "lok w2", "ah-ok", "กรดน้ำดี", "xs b tok", dx=30, dy=0))
    # ไขมันในโพรงลำไส้
    p.append(ell(56, 100, 30, 18, "ms"))
    p.append(t(56, 104, "TG", "sm mid b"))
    p.append(ar(90, 100, 128, 100, "ln", "ah"))
    for dx, dy in ((150, 92), (162, 106), (174, 94), (186, 108)):
        p.append(circ(dx, dy, 4, "msf"))
    p.append(t(168, 128, "FA + MG", "xs mid"))
    p.append(ar(200, 100, 262, 100, "ln", "ah"))
    p.append(circ(295, 100, 22, "ok"))
    for dx, dy in ((288, 94), (300, 92), (292, 106), (304, 106)):
        p.append(circ(dx, dy, 3.5, "msf"))
    p.append(t(330, 104, "micelle", "sm b"))
    # เยื่อบุ
    p.append(t(14, 152, "เยื่อบุ", "xs mu"))
    for i in range(5):
        x = 60 + i * 66
        p.append(rect(x, 156, 60, 64, "bx", 6))
        for k in range(5):
            p.append(line(x + 6 + k * 12, 156, x + 6 + k * 12, 148, "lmu"))
    p.append(circ(320, 194, 9, "ac"))
    p.append(t(346, 198, "chylomicron", "xs b"))
    # น้ำเหลือง
    p.append(t(14, 248, "น้ำเหลือง", "xs mu"))
    p.append(rect(60, 236, 324, 22, "wa", 11))
    p.append(t(384, 230, "→ thoracic duct", "xs end"))
    # เส้นทางปกติ
    p.append(X(2, mover(4, "msf", "4.2s", "M60 100 L168 100 L295 100 L320 194 L320 247 L380 247"),
               mover(4, "msf", "4.2s", "M60 100 L168 100 L295 100 L320 194 L320 247 L380 247", "-2.1s")))
    p.append(rect(20, 278, 400, 140, "sk"))
    p.append(S(1, t(34, 304, "ไขมันต้องผ่าน 3 ขั้น", "b"),
               t(34, 330, "1 ย่อยในโพรงลำไส้ (lipase + น้ำดี)", "sm"),
               t(34, 354, "2 ดูดเข้าเยื่อบุ → chylomicron", "sm"),
               t(34, 378, "3 ส่งออกทางน้ำเหลือง", "sm"), x=2))
    cross = lambda x, y: (line(x - 9, y - 9, x + 9, y + 9, "lbad w3") + line(x - 9, y + 9, x + 9, y - 9, "lbad w3"))
    # ขั้น 2 · ตับอ่อน
    p.append(S(2, G("pl", rect(110, 32, 90, 26, "bad", 8)), t(155, 49, "ตับอ่อน", "sm mid b"), cross(155, 70),
               G("pl", ell(56, 100, 30, 18, "bad")), t(56, 104, "TG", "sm mid b"), x=3))
    p.append(S(2, t(34, 304, "Luminal · ขาด lipase", "b tbad"),
               t(34, 330, "ตับอ่อนอักเสบเรื้อรัง มะเร็งตับอ่อน CF", "sm"),
               t(34, 354, "ต้องเสียหน้าที่ ≥ 90% · stool elastase ต่ำ", "sm"),
               t(34, 378, "D-xylose ปกติ · ให้เอนไซม์ดีขึ้น", "sm tok b"), x=3))
    # ขั้น 3 · น้ำดี
    p.append(S(3, G("pl", rect(240, 32, 110, 26, "bad", 8)), t(295, 49, "ตับ/ถุงน้ำดี", "sm mid b"), cross(295, 70),
               G("pl", circ(295, 100, 22, "bad")), x=4))
    p.append(S(3, t(34, 304, "Luminal · ขาดกรดน้ำดี", "b tbad"),
               t(34, 330, "ท่อน้ำดีอุดตัน · ตับแข็ง", "sm"),
               t(34, 354, "ตัด ileum > 100 ซม. · SIBO แยกกรดน้ำดี", "sm"),
               t(34, 378, "micelle ไม่เกิด → ไขมันค้าง", "sm tok b"), x=4))
    # ขั้น 4 · เยื่อบุ
    p.append(S(4, G("pl", rect(60, 156, 324, 64, "bad", 6)), t(222, 194, "villi ฝ่อ", "mid b tbad"), x=5))
    p.append(S(4, t(34, 304, "Mucosal · ผิวดูดซึมหาย", "b tbad"),
               t(34, 330, "celiac · tropical sprue · Whipple · Giardia", "sm"),
               t(34, 354, "ขาดทั้งไขมัน เหล็ก โฟเลต วิตามิน", "sm"),
               t(34, 378, "D-xylose ผิดปกติ", "sm tbad b"), x=5))
    # ขั้น 5 · น้ำเหลือง
    p.append(S(5, G("pl", rect(60, 236, 324, 22, "bad", 11)), cross(222, 247)))
    p.append(S(5, t(34, 304, "Lymphatic · ท่อน้ำเหลืองอุด", "b tbad"),
               t(34, 330, "intestinal lymphangiectasia · lymphoma", "sm"),
               t(34, 354, "น้ำเหลืองรั่วกลับลงลำไส้", "sm"),
               t(34, 378, "albumin ต่ำ บวม lymphocyte ต่ำ", "sm tbad b")))
    return SVG(440, 430, "ภาพเคลื่อนไหว: ไขมันต้องผ่านสามขั้น ย่อยด้วย lipase จากตับอ่อนและกรดน้ำดีเป็น micelle "
               "ดูดเข้าเยื่อบุเป็น chylomicron และส่งออกทางน้ำเหลือง เสียขั้นใดขั้นหนึ่งทำให้ถ่ายเป็นมัน", *p)


FAT_STEPS = [
    {"t": "ไขมันต้องผ่านสามขั้น",
     "cap": "TG ถูก **lipase ของตับอ่อน** ย่อยเป็น fatty acid + monoglyceride → **กรดน้ำดี** ห่อเป็น **micelle** → **เยื่อบุลำไส้เล็ก** ดูดเข้าและประกอบเป็น **chylomicron** → ออกทาง **lacteal/น้ำเหลือง**"},
    {"t": "ขั้น 1 พัง: ขาด lipase",
     "cap": "**ตับอ่อนบกพร่อง** (ตับอ่อนอักเสบเรื้อรัง มะเร็ง cystic fibrosis) — ต้องเสียหน้าที่ **≥ 90%** จึงถ่ายเป็นมัน · **stool elastase ต่ำ** · D-xylose ปกติ (ไม่ต้องใช้เอนไซม์) · **ลองให้เอนไซม์ตับอ่อน**"},
    {"t": "ขั้น 1 พัง: ขาดกรดน้ำดี",
     "cap": "micelle ไม่เกิด → ไขมันไม่ละลายเข้าเยื่อบุ · **ท่อน้ำดีอุดตัน ตับแข็ง** · **ตัด ileum > 100 ซม.** (กรดน้ำดีหายจากวงจร) · **SIBO** แบคทีเรียแยกกรดน้ำดี · ลองให้กรดน้ำดีเสริม"},
    {"t": "ขั้น 2 พัง: เยื่อบุเสีย",
     "cap": "**celiac** (villi ฝ่อ) · tropical sprue · **Whipple** · Giardia · ลำไส้เล็กสั้น → ดูดซึมผิดปกติทุกอย่าง (ซีดขาดเหล็ก/โฟเลต) · **D-xylose ผิดปกติ** · ยืนยันด้วย serology และ biopsy ลำไส้เล็ก"},
    {"t": "ขั้น 3 พัง: น้ำเหลืองอุด",
     "cap": "**intestinal lymphangiectasia, lymphoma**, Whipple → chylomicron ออกไม่ได้ น้ำเหลืองรั่วกลับลงลำไส้ → ถ่ายมัน + **protein-losing enteropathy**: albumin ต่ำ บวม lymphocyte ต่ำ"},
]


ITEMS = [
    {"sec": "gi-dia-03", "after": "ลำไส้เล็ก vs ลำไส้ใหญ่ส่วนปลาย",
     "anim": {"key": "dia-flow", "title": "น้ำ 10 ลิตรผ่านลำไส้ — ปริมาณอุจจาระบอกตำแหน่งโรค", "svg": a_flow(), "steps": FLOW_STEPS}},
    {"sec": "gi-dia-05", "after": "อ่านตารางอย่างไร",
     "anim": {"key": "dia-invasion", "title": "ยิ่งรุกล้ำลึก ยิ่งไข้ ปวดบิด และมีเลือด — toxin ถึง systemic", "svg": a_invasion(), "steps": INV_STEPS}},
    {"sec": "gi-dia-07", "after": "กลไกที่ทำให้ ORS ได้ผล",
     "anim": {"key": "dia-sglt1", "title": "ทำไม ORS ได้ผลใน cholera — SGLT1 ไม่ถูก toxin แตะ", "svg": a_sglt1(), "steps": SGLT_STEPS}},
    {"sec": "gi-dia-10", "after": "คำนวณ stool osmotic gap",
     "anim": {"key": "dia-gap", "title": "Stool osmotic gap — เกลือเต็มหรือมีสารอื่นแทรก", "svg": a_gap(), "steps": GAP_STEPS}},
    {"sec": "gi-dia-11", "after": "สามขั้นของการดูดซึมไขมัน — เสียขั้นไหนก็ถ่ายเป็นมัน",
     "anim": {"key": "dia-fat", "title": "ถ่ายเป็นมัน — พังที่ขั้นไหนของการดูดซึมไขมัน", "svg": a_fat(), "steps": FAT_STEPS}},
]

MNEM = [
    {"sec": "gi-dia-04", "name": "Reheated rice syndrome", "what": "Bacillus cereus — อาหารเป็นพิษจากข้าวที่หุงทิ้งไว้",
     "lines": [["Rice", "**ข้าวผัด/ข้าวหุงค้าง**ที่วางไว้อุณหภูมิห้อง → สปอร์ทนความร้อนแตกตัว"],
               ["Emetic", "toxin สร้างไว้ก่อน → **อาเจียนเด่นใน 1–6 ชม.** ไม่มีไข้"],
               ["Diarrheal", "อีกชนิดสร้าง toxin ในลำไส้ → ถ่ายเป็นน้ำใน 8–16 ชม."]],
     "note": "สไลด์จัด B. cereus เป็น preformed toxin (อาการภายใน ~4 ชม.) ร่วมกับ S. aureus (มายองเนส ขนมครีม)",
     "src": "First Aid for the USMLE Step 1 (Microbiology — Bacillus cereus)"},
    {"sec": "gi-dia-08", "name": "4C antibiotics", "what": "ยาปฏิชีวนะที่เสี่ยงทำให้เกิด C. difficile สูงสุด",
     "lines": [["C", "**C**lindamycin"], ["C", "**C**ephalosporins (โดยเฉพาะรุ่น 2–3)"],
               ["C", "**C**o-amoxiclav (amoxicillin-clavulanate)"], ["C", "**C**iprofloxacin และ fluoroquinolone อื่น"]],
     "note": "ยาปฏิชีวนะทุกตัวเสี่ยงได้ — ผู้ป่วยในที่ท้องเสียหลังได้ยาเหล่านี้ให้ตรวจ C. difficile และหยุดยาต้นเหตุถ้าทำได้",
     "src": "แนวทางควบคุมการใช้ยาปฏิชีวนะในโรงพยาบาลของสหราชอาณาจักร (NHS — high-risk '4C' antibiotics)"},
    {"sec": "gi-dia-09", "name": "Be FDR", "what": "Carcinoid syndrome — สิ่งที่หาได้จากการตรวจร่างกายในท้องเสียเรื้อรัง",
     "lines": [["B", "**B**ronchospasm — wheeze"], ["F", "**F**lushing — หน้าแดงวูบวาบ"],
               ["D", "**D**iarrhea — secretory"], ["R", "**R**ight-sided valvular disease — tricuspid/pulmonic"]],
     "note": "เกิดเมื่อ neuroendocrine tumor (มักจาก midgut) **กระจายไปตับ** serotonin จึงเข้ากระแสเลือดโดยไม่ถูกตับทำลาย · ตรวจ urine 5-HIAA",
     "src": "First Aid for the USMLE Step 1 (Endocrine — carcinoid syndrome)"},
    {"sec": "gi-dia-10", "name": "WDHA", "what": "VIPoma (Verner–Morrison syndrome) — secretory diarrhea จากฮอร์โมน",
     "lines": [["W", "**W**atery"], ["D", "**D**iarrhea — ปริมาณมาก ยังถ่ายแม้งดอาหาร"],
               ["H", "**H**ypokalemia"], ["A", "**A**chlorhydria — VIP ยับยั้งการหลั่งกรด"]],
     "note": "gap < 50 · VIP กระตุ้น cAMP เหมือน cholera toxin · รักษาด้วย octreotide และผ่าตัดก้อนที่ตับอ่อน",
     "src": "First Aid for the USMLE Step 1 (Endocrine — pancreatic islet cell tumors)"},
    {"sec": "gi-dia-11", "name": "ADEK", "what": "วิตามินละลายในไขมันที่ขาดเมื่อถ่ายเป็นมัน",
     "lines": [["A", "ตาบอดกลางคืน ตาแห้ง"], ["D", "Ca ต่ำ กระดูกบาง กระดูกอ่อน"],
               ["E", "ปลายประสาทเสื่อม เดินเซ"], ["K", "**PT ยาว เลือดออกง่าย** — แก้ได้ด้วยวิตามิน K ฉีด"]],
     "note": "สไลด์ให้ส่ง PT และ Ca P ในแล็บพื้นฐานของท้องเสียเรื้อรังด้วยเหตุนี้",
     "src": "หลักจำมาตรฐานในตำราชีวเคมี/โภชนาการ (fat-soluble vitamins A, D, E, K)"},
    {"sec": "gi-dia-13", "name": "FODMAP", "what": "คาร์โบไฮเดรตสายสั้นที่ดูดซึมไม่ดี ถูกหมักและดึงน้ำ — ลดในอาหาร low FODMAP สำหรับ IBS",
     "lines": [["F", "**F**ermentable — แบคทีเรียหมักเกิดแก๊ส"], ["O", "**O**ligosaccharides — fructan (ข้าวสาลี หอม กระเทียม) · GOS (ถั่ว)"],
               ["D", "**D**isaccharides — lactose (นม)"], ["M", "**M**onosaccharides — fructose เกิน glucose (น้ำผึ้ง แอปเปิล)"],
               ["A", "**A**nd"], ["P", "**P**olyols — sorbitol mannitol xylitol (หมากฝรั่งไม่มีน้ำตาล พีช)"]],
     "note": "แนวทางไทย 2022: งดระยะสั้น ไม่ดีขึ้นให้หยุด ดีขึ้นให้ค่อย ๆ reintroduce ทีละรายการ · ระวังทุพโภชนาการ",
     "src": "Monash University low FODMAP program (ชื่อย่อมาตรฐานของอาหารชนิดนี้)"},
]


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "anims_gi_diarrhea.json"
    json.dump({"set": "gi", "items": ITEMS, "mnem": MNEM}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("anims %d · mnem %d → %s" % (len(ITEMS), len(MNEM), out))
