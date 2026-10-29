# -*- coding: utf-8 -*-
"""ภาพเคลื่อนไหวกลไก (section.anims) + หลักจำ (section.mnem) ที่เติมให้คาบ gi 29/10 "Liver function tests"
ตามสไลด์ใหม่ปี 2570 ของ อ.กิตติ (โน้ต slides/lft2570_notes.md) · update_lft2570.py นำ ITEMS/MNEM ไปใส่ในหัวข้อ
รูปแบบตาม dashboard/learn_anim/SPEC.md (data-s = โผล่ตั้งแต่ขั้น n · data-x = หายตั้งแต่ขั้น n · fl ไหล · pl กะพริบ)

ตรวจ:  python3 artifact/tools/anims_gi_lft2570.py <out.json>
       python3 dashboard/anim_tool.py check <data dir ก่อนอัปเดต> <out.json>
ออกแบบให้ข้อความแต่ละขั้น "เพิ่ม" ในตำแหน่งใหม่ (ไม่วางข้อความใหม่ทับข้อความเก่าที่ซ่อน) เพื่อให้ check_render ไม่ฟ้องข้อความทับ"""
import json, math, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg import t, rect, circ, ell, line, ar, path, box, esc, pill  # noqa: E402


def S(k, *parts, x=None):
    """กลุ่มที่โผล่ตั้งแต่ขั้น k (และหายตั้งแต่ขั้น x ถ้าระบุ)"""
    a = ' data-s="%d"' % k + ((' data-x="%d"' % x) if x else "")
    return "<g%s>%s</g>" % (a, "".join(p for p in parts if p))


def X(k, *parts):
    return '<g data-x="%d">%s</g>' % (k, "".join(p for p in parts if p))


def G(c, *parts):
    return '<g class="%s">%s</g>' % (c, "".join(p for p in parts if p))


def mover(r, c, dur, d, begin="0s"):
    """อนุภาควิ่งตาม path (M/L พิกัดสัมบูรณ์) — วางวงกลมที่จุดเริ่ม แล้วแปลง path เป็นระยะสัมพัทธ์"""
    nums = [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", d)]
    x0, y0 = nums[0], nums[1]
    pts = [(nums[i] - x0, nums[i + 1] - y0) for i in range(0, len(nums), 2)]
    rel = "M0 0 " + " ".join("L%g %g" % p for p in pts[1:])
    return ('<circle cx="%g" cy="%g" r="%s" class="%s"><animateMotion dur="%s" begin="%s" repeatCount="indefinite" path="%s"/></circle>'
            % (x0, y0, r, c, dur, begin, rel))


def SVG(w, h, label, *parts):
    return ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg">' % (w, h, esc(label))
            + "".join(p for p in parts if p) + "</svg>")


def pts(lst):
    return " ".join("%s%g %g" % ("M" if i == 0 else "L", x, y) for i, (x, y) in enumerate(lst))


# ═══════════════════════════════════ 1 · R ratio — ใครนำ ALT หรือ ALP (gi-lft-01)
def a_rratio():
    x0, x1, lo, hi = 30, 410, math.log10(0.2), math.log10(50)
    X_ = lambda r: x0 + (x1 - x0) * (math.log10(r) - lo) / (hi - lo)
    y, h = 92, 24
    p = [t(220, 26, "R = (ALT ÷ ULN) ÷ (ALP ÷ ULN)", "mid b lg"),
         t(220, 48, "สเกล log · ซ้าย = ALP นำ · ขวา = ALT นำ · ULN ตัวอย่าง ALT 40 ALP 120", "mid xs mu"),
         rect(x0, y, X_(2) - x0, h, "wa", 4), rect(X_(2), y, X_(5) - X_(2), h, "ms", 0), rect(X_(5), y, x1 - X_(5), h, "bad", 4),
         t((x0 + X_(2)) / 2, 82, "Cholestatic < 2", "mid sm b twa"),
         t((X_(2) + X_(5)) / 2, 82, "Mixed", "mid sm b tms"),
         t((X_(5) + x1) / 2, 82, "Hepatocellular > 5", "mid sm b tbad"),
         t(X_(2) - 4, 132, "2", "end xs b"), t(X_(5) - 4, 132, "5", "end xs b")]

    def case(k, r, bx, title, l1, l2, res, cls):
        xr = X_(r)
        return S(k,
                 G("pl", circ(xr, y + h / 2, 7, "inkf")),
                 line(xr, y + h + 2, xr, 150, "ln w2"), line(xr, 150, bx + 68, 150, "ln w2"), line(bx + 68, 150, bx + 68, 158, "ln w2"),
                 rect(bx, 158, 136, 92, cls), t(bx + 68, 177, title, "mid sm b"),
                 t(bx + 8, 197, l1, "xs"), t(bx + 8, 214, l2, "xs"), t(bx + 68, 238, res, "mid sm b"))

    p.append(case(2, 0.47, 10, "ชาย 57 ปี ไข้ เหลือง", "ALT 60÷40 = 1.5", "ALP 380÷120 = 3.2", "R ≈ 0.5", "wa"))
    p.append(case(3, 5.65, 152, "ชาย 55 ปี อ้วน", "ALT 128÷40 = 3.2", "ALP 68÷120 = 0.57", "R ≈ 5.6", "bad"))
    p.append(case(4, 32.6, 294, "หญิง 23 ปี ยา 1 กำมือ", "ALT 2500÷40 = 62.5", "ALP 230÷120 = 1.9", "R ≈ 33", "bad"))
    p.append(S(5, rect(10, 262, 420, 62, "sk"),
               t(220, 284, "ALT นำ = เซลล์ตับตาย · ALP นำ = น้ำดีคั่ง", "mid sm b"),
               t(220, 306, "Mixed 2–5 → นึกถึง DILI ก่อน · นิ่วกำลังเคลื่อน · overlap · SIRS", "mid xs")))
    return SVG(440, 332, "ภาพเคลื่อนไหว: สเกล R ratio แบบ log แบ่งเป็น cholestatic น้อยกว่าสอง mixed สองถึงห้า "
               "และ hepatocellular มากกว่าห้า วางเคสจากสไลด์สามราย: cholangitis R ประมาณ 0.5 ไขมันพอกตับ R 5.6 และพิษพาราเซตามอล R ประมาณ 33", *p)


RRATIO_STEPS = [
    {"t": "R ratio ถามว่า ALT หรือ ALP นำ",
     "cap": "หารค่าของผู้ป่วยด้วย **ค่าสูงสุดของคนปกติ (ULN)** ทั้งคู่ก่อน แล้วเอามาหารกัน → ได้ตัวเลขเดียวที่บอกว่าความผิดปกติ **ทางเซลล์ตับ (ALT)** หรือ **ทางน้ำดี (ALP)** เด่นกว่า · **> 5 hepatocellular · 2–5 mixed · < 2 cholestatic**"},
    {"t": "ชาย 57 ปี ไข้ เหลือง ปวดชายโครงขวา (สไลด์ 2570)",
     "cap": "ALT 60 แทบปกติ (1.5 เท่า) แต่ ALP 380 (3.2 เท่า) → **R ≈ 0.5 = cholestatic** · ร่วมกับ **Charcot's triad** → สไลด์เฉลย **ascending cholangitis** → US/ERCP"},
    {"t": "ชาย 55 ปี อ้วน ตรวจสุขภาพ (สไลด์ 2570)",
     "cap": "ALT 128 (3.2 เท่า) · ALP 68 ปกติ → **R ≈ 5.6 = hepatocellular** แม้ค่าสูงแค่ระดับ mild — R บอก **ชนิด** ไม่ได้บอก **ความรุนแรง** · AST/ALT < 1 + metabolic syndrome → **MASLD**"},
    {"t": "หญิง 23 ปี กินยาแก้ปวด 1 กำมือ",
     "cap": "ALT 2,500 (62 เท่า) · ALP 230 → **R ≈ 33** hepatocellular ระดับ extreme → paracetamol (ขาดเลือดและ rhabdomyolysis เป็น DDx ตามลายมืออาจารย์)"},
    {"t": "สรุป: R บอกว่ามองหาโรคกลุ่มไหน",
     "cap": "**R > 5** → serology ไวรัส ยา ขาดเลือด AIH Wilson · **R < 2** → **อัลตราซาวนด์** ดูท่อน้ำดีขยาย · **2–5** → สไลด์ 2570 ให้นึกถึง **DILI (✍️ วงข้อ 1 'Drug')** overlap (AIH + immune cholangiopathy) นิ่วกำลังเคลื่อน และ LFT ของ SIRS"},
]


# ═══════════════════════════════════ 2 · เอนไซม์อยู่ส่วนไหนของเซลล์ตับ (gi-lft-02)
def a_leak():
    p = [rect(16, 14, 408, 36, "bad", 8), t(220, 37, "เลือด (sinusoid) — สิ่งที่วัดได้ในซีรัม", "mid sm b"),
         rect(16, 96, 290, 226, "sk", 14), t(263, 286, "เซลล์ตับ", "mid b sm"), t(263, 304, "(hepatocyte)", "mid xs i2"),
         # ALT + AST ใน cytosol
         t(30, 222, "cytosol: ALT + AST 20%", "xs i2"),
         circ(44, 160, 5, "acf"), circ(66, 172, 5, "acf"), circ(90, 158, 5, "acf"), circ(56, 190, 5, "acf"),
         circ(82, 196, 5, "waf"), circ(110, 180, 5, "acf"),
         # mitochondria
         ell(222, 168, 66, 30, "ok"), t(222, 165, "mitochondria", "mid sm b"), t(222, 182, "AST 80%", "mid xs"),
         circ(186, 168, 4, "waf"), circ(258, 168, 4, "waf"),
         # ER
         rect(30, 232, 190, 72, "wa", 10), t(125, 254, "ER / ribosome", "mid sm b"),
         t(125, 272, "สร้าง albumin", "mid xs"), t(125, 289, "+ clotting factor II V VII IX X", "mid xs"),
         # canaliculus
         rect(318, 96, 106, 226, "ms", 14), t(371, 116, "ท่อน้ำดีฝอย", "mid sm b"),
         t(371, 134, "(canaliculus)", "mid xs i2"), t(371, 156, "เยื่อหุ้ม: ALP · GGT", "mid xs b")]
    # ขั้น 2 · เยื่อหุ้มเซลล์แตก → ALT รั่ว
    p.append(S(2, G("pl", rect(16, 96, 290, 226, "lbad w3", 14)),
               ar(60, 150, 60, 54, "lbad w2", "ah-bad"), ar(92, 150, 92, 54, "lbad w2", "ah-bad"),
               t(100, 80, "ALT รั่ว (+AST cytosol)", "sm b tbad"),
               mover(4, "acf", "1.6s", "M66 172 L66 40"), mover(4, "acf", "1.6s", "M90 158 L90 40", "-.8s")))
    # ขั้น 3 · mitochondria เสีย → AST
    p.append(S(3, G("pl", ell(222, 168, 66, 30, "lbad w3")),
               ar(250, 136, 268, 54, "lbad w2", "ah-bad"), t(276, 74, "AST mito", "sm b tbad"),
               mover(4, "waf", "1.6s", "M258 168 L272 40")))
    # ขั้น 4 · cholestasis → สร้าง ALP GGT เพิ่ม
    p.append(S(4, G("pl", rect(328, 172, 86, 140, "bad", 10)),
               t(371, 196, "กรดน้ำดีค้าง", "mid xs b"), t(371, 214, "→ สั่งสร้าง", "mid xs"), t(371, 232, "ALP GGT เพิ่ม", "mid xs b"),
               t(371, 250, "+ ละลายหลุด", "mid xs"), t(371, 268, "เข้าเลือด", "mid xs"),
               ar(400, 172, 400, 54, "lms w2", "ah-ms")))
    # ขั้น 5 · สร้างไม่ได้
    p.append(S(5, G("pl", rect(30, 232, 190, 72, "lbad w3", 10)),
               t(16, 342, "สร้างไม่ได้ → PT ยาวใน ชม. (VII t½ ~6 ชม.) · albumin ลดช้า (t½ ~20 วัน)", "xs b tbad")))
    p.append(S(6, pill(16, 360, "AST ALT = เซลล์ตาย", "bad", "xs b mid", 130),
               pill(152, 360, "ALP GGT bili = น้ำดี", "ms", "xs b mid", 136),
               pill(294, 360, "Alb PT = การทำงานจริง", "wa", "xs b mid", 130)))
    return SVG(440, 392, "ภาพเคลื่อนไหว: เซลล์ตับมี ALT และ AST ส่วนน้อยใน cytosol AST ส่วนใหญ่อยู่ใน mitochondria "
               "ALP GGT อยู่ที่เยื่อหุ้มด้านท่อน้ำดีฝอย และ ER สร้าง albumin กับ clotting factor "
               "เมื่อเซลล์แตก ALT รั่ว เมื่อ mitochondria เสีย AST รั่ว เมื่อน้ำดีค้าง ALP ถูกสร้างเพิ่ม และเมื่อสร้างไม่ได้ PT ยาว", *p)


LEAK_STEPS = [
    {"t": "เอนไซม์แต่ละตัวอยู่คนละที่ในเซลล์ตับ",
     "cap": "**ALT** อยู่ใน cytosol เกือบทั้งหมดและจำเพาะต่อตับ · **AST ของตับ 80% อยู่ใน mitochondria** 20% ใน cytosol และยังมีใน **หัวใจ กล้ามเนื้อ ไต สมอง ตับอ่อน เม็ดเลือด** (สไลด์ 2570) · ALP GGT อยู่ที่ **เยื่อหุ้มด้านท่อน้ำดี** · albumin และ clotting factor สร้างที่ ER"},
    {"t": "เยื่อหุ้มเซลล์แตก (ไวรัส ขาดเลือด ยา) → ALT นำ",
     "cap": "เซลล์บวมแตก → ของใน cytosol รั่วก่อน → **ALT สูงกว่า AST** · ALT ยังมี **ครึ่งชีวิตยาวกว่า (~47 vs ~17 ชม.)** จึงค้างนานกว่า → **AST/ALT < 1** ในไวรัสและไขมันพอกตับ (ยกเว้นตับแข็ง)"},
    {"t": "Mitochondria ถูกทำลายโดยตรง → AST นำ",
     "cap": "✍️ อาจารย์เขียน **\"Inj. to mitochondria\"** ที่ AST/ALT > 2 · เหล้าทำลาย mitochondria + ขาด **pyridoxal-5′-phosphate** ทำให้สร้าง ALT น้อย → **AST/ALT > 2** · ✍️ ถ้า **ไม่มีตับแข็ง** แล้ว AST/ALT > 2 นึกถึง **เหล้า หรือ Wilson**"},
    {"t": "น้ำดีค้าง → ALP GGT ถูกสร้างเพิ่ม",
     "cap": "ALP/GGT ไม่ได้รั่วจากเซลล์ตายแบบ AST/ALT แต่ **กรดน้ำดีที่ค้างเหนี่ยวนำให้สร้างเพิ่ม** และละลายเอนไซม์จากเยื่อหุ้มเข้าเลือด → จึงขึ้นช้ากว่า (1–2 วัน) และ **ALP ครึ่งชีวิต 5–7 วัน** (สไลด์ 2570) ลงช้า"},
    {"t": "ตับสร้างไม่ได้ → PT ยาวก่อน albumin ลด",
     "cap": "เสาที่ 3 ของสไลด์ 2570 (✍️ ไฮไลต์): **albumin และ PT = การทำงานจริงของตับ** · factor VII ครึ่งชีวิต ~6 ชม. → **PT ยาวได้ในไม่กี่ชั่วโมง** (บอกความรุนแรงของโรคเฉียบพลัน) · albumin ครึ่งชีวิต ~20 วัน → **บอกความเรื้อรัง**"},
    {"t": "สรุป 3 เสาหลักของ LFT",
     "cap": "**Hepatocyte integrity** (AST ALT) · **Biliary function** (ALP GGT bilirubin 5′NT) · **Synthetic function** (albumin PT) — ค่าเอนไซม์สูงไม่ได้แปลว่า \"ตับทำงานแย่\" ต้องดู albumin/PT/bilirubin ประกอบ"},
]


# ═══════════════════════════════════ 3 · Zone 3 — ทำไมช็อก paracetamol เหล้า ทำลายตรงกลาง (gi-lft-09)
def a_zone3():
    yc = 132
    p = [t(220, 22, "Acinus: เลือดไหลจาก portal tract → central vein", "mid sm b"),
         circ(48, yc, 30, "sk"), circ(38, yc - 8, 8, "wa"), circ(58, yc - 8, 6, "bad"), circ(48, yc + 12, 6, "ms"),
         t(48, yc + 48, "portal triad", "mid xs b"),
         rect(84, 96, 100, 72, "ok", 0), rect(184, 96, 100, 72, "ms", 0), rect(284, 96, 90, 72, "sk", 0),
         t(134, 90, "Zone 1", "mid sm b"), t(234, 90, "Zone 2", "mid sm b"), t(329, 90, "Zone 3", "mid sm b"),
         t(134, 186, "O₂ สูง", "mid xs tok b"), t(329, 186, "O₂ ต่ำสุด", "mid xs b"),
         t(329, 202, "CYP2E1 มากสุด", "mid xs b"),
         circ(400, yc, 22, "wa"), t(400, yc + 4, "CV", "mid xs b"), t(400, 102, "central vein", "mid xs b"),
         line(80, yc, 376, yc, "lwa w2 fl"),
         X(2, mover(3.5, "badf", "2.6s", "M80 132 L376 132"), mover(3.5, "badf", "2.6s", "M80 132 L376 132", "-.9s"),
           mover(3.5, "badf", "2.6s", "M80 132 L376 132", "-1.7s"))]
    p.append(S(2, t(16, 50, "BP 80/40 → O₂ หมดก่อนถึงปลายทาง", "sm b tbad"),
               mover(3.5, "badf", "2.6s", "M80 132 L240 132"),
               G("pl", rect(288, 100, 82, 64, "lbad w3", 4)), t(329, 152, "ตาย", "mid b tbad")))
    p.append(S(3, rect(206, 214, 218, 26, "bad", 6), t(315, 232, "paracetamol → NAPQI (CYP2E1)", "mid xs b")))
    p.append(S(4, rect(206, 246, 218, 26, "bad", 6), t(315, 264, "เหล้า · halothane → zone 3 เช่นกัน", "mid xs b")))
    p.append(S(2, rect(10, 286, 136, 108, "bad"), t(78, 306, "Ischemic", "mid sm b"),
               t(78, 326, "หลังช็อก 1–3 วัน", "mid xs"), t(78, 344, "พุ่งเป็นพัน ลงเร็ว", "mid xs"),
               t(78, 362, "LDH สูงมาก", "mid xs"), t(78, 380, "ALT/LDH < 1.5", "mid xs b")))
    p.append(S(3, rect(152, 286, 136, 108, "bad"), t(220, 306, "Paracetamol", "mid sm b"),
               t(220, 326, "ยา 1 กำมือ", "mid xs"), t(220, 344, "AST อาจ > ALT", "mid xs"),
               t(220, 362, "INR ยาวเร็ว", "mid xs"), t(220, 380, "ให้ NAC ทันที", "mid xs b")))
    p.append(S(5, rect(294, 286, 136, 108, "ms"), t(362, 306, "Rhabdomyolysis", "mid sm b"),
               t(362, 326, "ไม่ใช่ตับ!", "mid xs b"), t(362, 344, "AST >> ALT", "mid xs"),
               t(362, 362, "CK สูงมาก", "mid xs"), t(362, 380, "ปัสสาวะสีโค้ก", "mid xs")))
    p.append(S(5, t(220, 412, "✍️ อาจารย์: transaminase หลายพัน DDx 3 โรค = Para + Ischemic + Rhabdo", "mid xs b tac")))
    return SVG(440, 422, "ภาพเคลื่อนไหว: acinus ของตับ เลือดไหลจาก portal triad ผ่าน zone 1 2 3 ไป central vein "
               "zone 3 ได้ออกซิเจนน้อยสุดและมี CYP2E1 มากสุด จึงตายก่อนเมื่อช็อก ได้ paracetamol เหล้า หรือ halothane "
               "และกล่องเปรียบเทียบสามโรคที่ทำให้ transaminase สูงหลายพัน: ขาดเลือด paracetamol และ rhabdomyolysis", *p)


ZONE3_STEPS = [
    {"t": "เลือดไหลจาก zone 1 ไป zone 3",
     "cap": "เลือดจาก portal vein + hepatic artery เข้าที่ **zone 1 (periportal)** แล้วไหลผ่าน sinusoid ไป **central vein** · เซลล์ zone 1 ใช้ O₂ ไปก่อน → **zone 3 ได้ O₂ น้อยสุด** และเป็นที่อยู่ของ **CYP2E1** มากสุด"},
    {"t": "ช็อก (BP 80/40) → zone 3 ตายพร้อมกัน",
     "cap": "✍️ \"Zone 3 = sensitive to shock\" · ความดันต่ำ → O₂ หมดก่อนถึงปลายทาง → เซลล์รอบ central vein ตายในครั้งเดียว → **AST/ALT 3,900/3,500 ภายใน 1–3 วัน** (เคสหญิง 65 ปี ปอดอักเสบ สไลด์ 2570) · เนื้อเยื่อทั้งตัวขาด O₂ → **LDH สูงมาก → ALT/LDH < 1.5**"},
    {"t": "Paracetamol ก็ตาย zone 3",
     "cap": "CYP2E1 ใน zone 3 เปลี่ยนยาเป็น **NAPQI** → glutathione หมด → zone 3 ตาย → **transaminase ระดับ extreme (50–100 เท่า)** · ✍️ อาจารย์เขียน **\"only this\"** ที่ paracetamol = ยาที่ทำให้ขึ้นถึงระดับนี้"},
    {"t": "เหล้าและ halothane — zone 3 เหมือนกัน",
     "cap": "✍️ ลายมือในห้อง: **\"Zone 3 ใกล้ตรงกลาง = sensitive to shock / Para / เหล้า / halothane\"** · ทั้งหมดอาศัย O₂ ต่ำ หรือการเผาผลาญผ่าน CYP ที่หนาแน่นใน zone 3"},
    {"t": "DDx สามโรคของ transaminase หลายพัน",
     "cap": "✍️ **\"DDx 3 โรค: Para + Ischemic + Rhabdomyolysis\"** · rhabdomyolysis ไม่ใช่โรคตับ: AST มาจากกล้ามเนื้อ → **AST >> ALT + CK สูงมาก** (ALT ขึ้นตามได้ใน severe muscle disease) · แยกด้วยประวัติ (ยา ช็อก ชัก/ออกกำลัง/กดทับ) + LDH + CK"},
]


# ═══════════════════════════════════ 4 · AIH — interface hepatitis → globulin สูง A/G กลับข้าง (gi-lft-04)
def a_aih():
    base, sc = 236, 26  # px ต่อ g/dL
    p = [circ(70, 120, 46, "sk"), t(70, 116, "portal", "mid sm b"), t(70, 132, "tract", "mid sm b"),
         t(70, 186, "limiting plate →", "mid xs i2")]
    for c in range(2):
        for r in range(5):
            p.append(rect(128 + c * 38, 56 + r * 30, 34, 26, "ok", 4))
    p.append(t(166, 220, "แผ่นเซลล์ตับ", "mid xs b"))
    p += [t(340, 22, "ซีรัม (g/dL)", "mid sm b"), line(258, base, 424, base, "ln w2"),
          rect(272, base - 4.5 * sc, 56, 4.5 * sc, "wa", 3), t(300, base + 18, "Albumin", "mid xs b"),
          rect(352, base - 3.0 * sc, 56, 3.0 * sc, "ms", 3), t(380, base + 18, "Globulin", "mid xs b"),
          X(4, t(300, base - 4.5 * sc - 6, "4.5", "mid xs")), X(3, t(380, base - 3.0 * sc - 6, "3.0", "mid xs"))]
    p.append(S(2, circ(52, 100, 6, "paf"), circ(82, 96, 6, "paf"), circ(64, 142, 6, "paf"), circ(92, 130, 6, "paf"),
               mover(5, "paf", "2.2s", "M100 120 L140 120"), mover(5, "paf", "2.2s", "M96 90 L140 70", "-1.1s"),
               G("pl", rect(126, 54, 38, 152, "lbad w3", 4)),
               t(16, 252, "lymphocyte + plasma cell ลามข้ามแผ่นแรก", "xs b tbad"),
               t(16, 268, "= interface hepatitis → AST ≈ ALT", "xs b tbad")))
    p.append(S(3, rect(352, base - 6.0 * sc, 56, 6.0 * sc, "ms", 3), t(380, base - 6.0 * sc - 6, "6.0", "mid xs b tbad"),
               path("M96 80 L122 42 L330 42 L366 62", "lms w2 fl", "ah-ms"), t(226, 36, "IgG หลายชนิด", "mid xs b")))
    p.append(S(4, rect(272, base - 4.5 * sc, 56, 4.5 * sc, "sk", 3), rect(272, base - 3.3 * sc, 56, 3.3 * sc, "wa", 3),
               t(300, base - 3.3 * sc - 6, "3.3", "mid xs b tbad"),
               t(16, 292, "เป็นนาน → สร้าง albumin ไม่พอ", "xs b"),
               t(16, 308, "+ palmar erythema spider ขาดประจำเดือน", "xs")))
    p.append(S(5, rect(270, 264, 158, 50, "bad", 8), t(349, 284, "A/G = 3.3/6 = 0.55", "mid sm b"),
               t(349, 304, "< 1 = reversed A/G", "mid xs b"),
               rect(10, 324, 418, 54, "sk", 8), t(219, 344, "globulin สูงขนาด 6 → คิด AIH (polyclonal IgG)", "mid xs b"),
               t(219, 364, "✍️ ถ้าเป็นแถบเดียว (monoclonal) → myeloma ไม่ใช่ AIH", "mid xs")))
    return SVG(440, 386, "ภาพเคลื่อนไหว: autoimmune hepatitis lymphocyte และ plasma cell จาก portal tract ลามข้ามแผ่นเซลล์ตับแผ่นแรก "
               "เกิด interface hepatitis plasma cell สร้าง IgG หลายชนิดทำให้ globulin สูงถึงหก albumin ลดเมื่อเป็นนาน "
               "อัตราส่วน albumin ต่อ globulin จึงกลับข้าง", *p)


AIH_STEPS = [
    {"t": "ปกติ: portal tract กับแผ่นเซลล์ตับแผ่นแรก",
     "cap": "แผ่นเซลล์ตับแถวที่ติด portal tract เรียก **limiting plate** · ซีรัมปกติ albumin ~4.5 globulin ~3 → **A/G > 1**"},
    {"t": "Interface hepatitis",
     "cap": "ภูมิคุ้มกันเสียสมดุล → **lymphocyte และ plasma cell** ลุกจาก portal tract ข้าม limiting plate ทำลายเซลล์ทีละแถว → transaminase ระดับ moderate (เคสสไลด์ 2570: **AST 600 ALT 575** ✍️ \"พอ ๆ\")"},
    {"t": "Plasma cell สร้าง IgG หลายชนิด → globulin 6",
     "cap": "IgG สูงแบบ **polyclonal** (หลายโคลน) → globulin ในเคสขึ้นถึง **6 g/dL** · IgG สูงเป็นหนึ่งคะแนนใน simplified criteria · ✍️ อาจารย์โยงคำว่า **\"Monoclonal\"** — ถ้าเป็น spike เดียวต้องคิด myeloma"},
    {"t": "เป็นนานจนสร้าง albumin ไม่พอ",
     "cap": "albumin ครึ่งชีวิต ~20 วัน จะลดก็ต่อเมื่อโรคเป็นนาน → **albumin 3.3** + อาการตับเรื้อรัง (✍️ \"Chronic\"): **ขาดประจำเดือน palmar erythema spider** — estrogen ที่ตับกำจัดไม่ได้"},
    {"t": "Reversed A/G — ตับเรื้อรัง แต่ globulin สูงเกินไป",
     "cap": "✍️ **\"Reverse A/G → represent chronic liver\"** แต่ **\"globulin ไม่สูงขนาดนี้\"** ในตับแข็งทั่วไป → globulin 6 ในหญิงอายุน้อย = **AIH** → ตรวจ **ANA + ASMA (type 1)** · anti-LKM1 (type 2)"},
]


# ═══════════════════════════════════ 5 · MASLD — insulin resistance → ไขมัน → ALT (gi-lft-10)
def a_masld():
    p = [box(16, 40, 120, 64, "ms", "ไขมันหน้าท้อง\n+ insulin\nresistance", "b", fs=11.5),
         rect(196, 30, 228, 150, "sk", 14), t(310, 50, "เซลล์ตับ", "mid sm b"),
         ar(136, 60, 194, 60, "lms w3 fl", "ah-ms"), t(165, 52, "FFA", "mid xs b"),
         ar(136, 92, 194, 92, "lms w2 fl", "ah-ms"), t(165, 112, "insulin สูง", "mid xs"), t(165, 126, "→ สร้างไขมัน", "mid xs")]
    p.append(S(2, circ(236, 92, 16, "msf"), circ(276, 120, 20, "msf"), circ(330, 86, 18, "msf"), circ(372, 128, 14, "msf"),
               circ(300, 150, 10, "msf"), t(310, 172, "หยดไขมัน (steatosis)", "mid xs b")))
    p.append(S(3, G("pl", rect(196, 30, 228, 150, "lbad w3", 14)),
               ar(400, 30, 400, 8, "lbad w2", "ah-bad"), t(392, 20, "ALT รั่ว", "end xs b tbad"),
               t(16, 150, "lipotoxicity:", "xs b tbad"), t(16, 166, "oxidative stress", "xs"), t(16, 182, "→ เซลล์อักเสบ", "xs")))
    xs = [12, 118, 224, 330]
    labs = ["ไขมันพอก", "MASH (NASH)", "พังผืด", "ตับแข็ง"]
    cls = ["ms", "bad", "ac", "bad"]
    p.append(t(220, 214, "การดำเนินโรค", "mid sm b"))
    for i, (x, lb, c) in enumerate(zip(xs, labs, cls)):
        k = i + 2
        p.append(S(k, box(x, 226, 92, 34, c, lb, "sm b")))
        if i:
            p.append(S(k, ar(x - 13, 243, x - 2, 243, "ln w2", "ah")))
    p.append(S(2, t(58, 282, "ALT ≥ AST", "mid xs b")))
    p.append(S(3, t(164, 282, "ALT > AST", "mid xs b")))
    p.append(S(4, t(270, 282, "stellate cell", "mid xs"), t(270, 298, "→ collagen", "mid xs")))
    p.append(S(5, t(376, 282, "AST > ALT", "mid xs b tbad"), t(376, 298, "เกล็ดเลือดต่ำ", "mid xs")))
    p.append(S(5, rect(16, 314, 408, 60, "wa", 8),
               t(220, 334, "เคส 2570: ชาย 55 ปี อ้วน · AST 76 ALT 128 · ALP ปกติ", "mid xs b"),
               t(220, 352, "AST/ALT < 1 + metabolic syndrome → NAFLD/NASH (✍️ MAFLD)", "mid xs"),
               t(220, 368, "ประเมิน DM HT DLP · ประเมินพังผืด (FIB-4) · biopsy ถ้าจำเป็น", "mid xs")))
    return SVG(440, 382, "ภาพเคลื่อนไหว: ไขมันหน้าท้องและภาวะดื้ออินซูลินส่งกรดไขมันอิสระเข้าตับ อินซูลินสูงกระตุ้นสร้างไขมัน "
               "เกิดหยดไขมันในเซลล์ตับ lipotoxicity ทำให้ ALT รั่ว และดำเนินจากไขมันพอกไปเป็น MASH พังผืด และตับแข็ง "
               "ซึ่งอัตราส่วน AST ต่อ ALT จะกลับเป็นมากกว่าหนึ่ง", *p)


MASLD_STEPS = [
    {"t": "ภาวะดื้ออินซูลินส่งไขมันเข้าตับ",
     "cap": "ไขมันหน้าท้อง + **insulin resistance** → lipolysis ไม่หยุด **FFA ไหลเข้าตับ** มาก · insulin ที่สูงยังกระตุ้น **de novo lipogenesis** ในตับ → ไขมันเข้า > ออก"},
    {"t": "Steatosis — ไขมันพอกตับ",
     "cap": "triglyceride สะสมเป็นหยดใน hepatocyte · ระยะนี้ LFT อาจปกติหรือ **ALT สูงเล็กน้อย (mild 2–5 เท่า)** · ชื่อใหม่ **MASLD** (✍️ อาจารย์เขียน MAFLD) = ไขมันพอก + ปัจจัยเสี่ยง cardiometabolic อย่างน้อย 1 ข้อ"},
    {"t": "Lipotoxicity → MASH → ALT รั่ว",
     "cap": "FFA และสารตัวกลางของไขมัน → **oxidative stress** + ER stress → เซลล์บวม (ballooning) อักเสบ → ALT รั่วจาก cytosol → **AST/ALT < 1** (เคส: **AST 76 ALT 128**) ต่างจากเหล้าที่ AST นำ"},
    {"t": "พังผืด — ตัวกำหนดพยากรณ์โรค",
     "cap": "เซลล์ตาย → **hepatic stellate cell** ถูกกระตุ้นสร้าง collagen · **ระดับพังผืดไม่ใช่ระดับ ALT** เป็นตัวบอกพยากรณ์โรค → ใช้ **FIB-4** (อายุ AST ALT เกล็ดเลือด) คัดกรองก่อน (แนวทาง AASLD 2023 — ไม่ได้มาจากสไลด์)"},
    {"t": "ตับแข็ง — อัตราส่วนกลับข้าง",
     "cap": "เมื่อเป็นตับแข็ง sinusoid เก็บกวาด AST ได้น้อยลง → **AST/ALT > 1** (สไลด์: \"ยกเว้นกรณีมี cirrhosis ร่วม\") · ม้ามโต เกล็ดเลือดต่ำ · next step ตามสไลด์: **ประเมิน metabolic syndrome (DM HT DLP) และเจาะชิ้นเนื้อเมื่อจำเป็น**"},
]


# ═══════════════════════════════════ 6 · Wilson — ATP7B เสีย ทองแดงล้น (gi-lft-11)
def a_wilson():
    p = [box(16, 24, 108, 44, "sk", "อาหาร → ลำไส้\nทองแดง (Cu)", "", fs=11.5),
         rect(150, 16, 168, 176, "sk", 14), t(234, 36, "เซลล์ตับ", "mid sm b"),
         ar(124, 46, 148, 46, "ln w2 fl", "ah"),
         pill(196, 98, "ATP7B", "ok", "sm b mid", 76),
         rect(338, 16, 86, 272, "bad", 10), t(381, 36, "เลือด", "mid sm b"),
         ar(272, 106, 336, 82, "lok w2 fl", "ah-ok"), t(381, 62, "ceruloplasmin", "mid xs b"),
         t(381, 76, "(Cu 6 อะตอม)", "mid xs"),
         ar(234, 120, 234, 212, "lms w2 fl", "ah-ms"),
         box(170, 214, 128, 36, "ms", "น้ำดี → อุจจาระ", "sm b")]
    for i in range(3):
        p.append(X(2, mover(3, "msf", "2.4s", "M124 46 L234 70 L234 109 L234 212", "-%.1fs" % (0.8 * i))))
    p.append(S(2, line(200, 94, 268, 124, "lbad w3"), line(200, 124, 268, 94, "lbad w3"),
               t(226, 146, "AR (ATP7B)", "end xs b tbad"),
               G("pl", circ(176, 62, 5, "msf"), circ(196, 76, 5, "msf"), circ(272, 60, 5, "msf"), circ(292, 80, 5, "msf"),
                 circ(176, 170, 5, "msf"), circ(200, 178, 5, "msf"), circ(270, 170, 5, "msf"), circ(292, 160, 5, "msf")),
               t(381, 108, "ceruloplasmin ↓", "mid xs b tbad"), t(381, 122, "6.5 mg/dL", "mid xs")))
    p.append(S(3, G("pl", rect(150, 16, 168, 176, "lbad w3", 14)),
               ar(318, 168, 336, 168, "lbad w3", "ah-bad"),
               mover(4, "msf", "1.8s", "M300 168 L400 168 L400 240"),
               t(381, 150, "Cu อิสระ ↑", "mid xs b tbad"), t(381, 164, "(45 µg/dL)", "mid xs"),
               circ(356, 194, 9, "badf"), circ(380, 202, 9, "badf"), circ(404, 192, 9, "badf"),
               t(381, 230, "เม็ดเลือดแดงแตก", "mid xs b"), t(381, 244, "Coombs ลบ", "mid xs b"),
               t(381, 258, "Hb 6.8", "mid xs")))
    p.append(S(4, ar(381, 288, 381, 306, "lbad w2", "ah-bad"),
               box(312, 308, 112, 44, "wa", "ไต: Cu ปัสสาวะ\n680 µg/วัน", "", fs=11),
               ar(338, 264, 134, 286, "lbad w2", "ah-bad"),
               box(16, 258, 116, 52, "ac", "ตา: KF ring\nสมอง: basal\nganglia", "", fs=11)))
    p.append(S(5, rect(140, 300, 166, 92, "ms", 8), t(223, 320, "ลายเซ็นใน LFT", "mid sm b"),
               t(223, 340, "AST/ALT 520/210 = 2.48 > 2.2", "mid xs b tbad"),
               t(223, 358, "ALP/TB 38/22.5 = 1.69 < 4", "mid xs b tbad"),
               t(223, 380, "✍️ จำ ทั้งสองค่า", "mid xs b tac")))
    return SVG(440, 400, "ภาพเคลื่อนไหว: ทองแดงจากอาหารเข้าเซลล์ตับ ATP7B ใส่ทองแดงลงใน ceruloplasmin และขับลงน้ำดี "
               "ใน Wilson disease ATP7B เสีย ทองแดงสะสมในเซลล์ ceruloplasmin ต่ำ เซลล์ตายปล่อยทองแดงอิสระทำให้เม็ดเลือดแดงแตกแบบ Coombs ลบ "
               "ทองแดงล้นไปไต ตา และสมอง และ LFT มี AST ต่อ ALT มากกว่า 2.2 กับ ALP ต่อ bilirubin น้อยกว่า 4", *p)


WILSON_STEPS = [
    {"t": "ปกติ: ATP7B ส่งทองแดงสองทาง",
     "cap": "ทองแดงจากอาหารเข้าเซลล์ตับ → **ATP7B** (copper-transporting ATPase) ส่งต่อ 2 ทาง: **ใส่ลงใน apo-ceruloplasmin** แล้วปล่อยเข้าเลือด และ **ขับลงน้ำดี** ออกทางอุจจาระ (ทางกำจัดหลัก)"},
    {"t": "Wilson: ATP7B เสีย (autosomal recessive)",
     "cap": "✍️ **\"AR\"** · ขับลงน้ำดีไม่ได้ → **ทองแดงสะสมในเซลล์ตับ** · apo-ceruloplasmin ที่ไม่มีทองแดงสลายเร็ว → **ceruloplasmin ต่ำ** (เคส **6.5 mg/dL** ปกติ 20–40 · เกณฑ์สไลด์ < 200 mg/L = < 20 mg/dL)"},
    {"t": "เซลล์ตับตาย → ทองแดงอิสระ → เม็ดเลือดแดงแตก",
     "cap": "ทองแดงทำลาย mitochondria → เซลล์ตายจำนวนมาก (acute liver failure) และ **ปล่อยทองแดงอิสระ** (non-ceruloplasmin Cu **45 µg/dL** ปกติ 5–15) → oxidative damage ต่อเยื่อหุ้มเม็ดเลือดแดง → **hemolysis แบบ Coombs ลบ** · bilirubin จึงสูงมาก (**TB 22.5**)"},
    {"t": "ทองแดงล้นไปไต ตา สมอง",
     "cap": "ไตกรองทองแดงอิสระ → **ทองแดงในปัสสาวะ 24 ชม. 680 µg** (ปกติ < 40) · เกาะ Descemet membrane → **Kayser–Fleischer ring** · basal ganglia → **extrapyramidal** (✍️ \"tract ที่ไม่ใช่ corticospinal เช่น parkinsonism\")"},
    {"t": "ลายเซ็นใน LFT ของ Wilsonian ALF",
     "cap": "**AST/ALT > 2.2** (ทองแดงทำลาย mitochondria → AST นำ) และ **ALP/TB < 4** (ALP **ต่ำผิดคาด** ขณะ bilirubin สูงมากจาก hemolysis + ตับวาย) · สไลด์ 2570 ✍️ **\"จำ\"** ทั้งสองค่า · กลไกที่ ALP ต่ำยังไม่ชัด (สมมติฐาน: ทองแดง/zinc รบกวนเอนไซม์ — ไม่ได้มาจากสไลด์)"},
]


# ═══════════════════════════════════ 7 · นิ่วอุด CBD → ALT ALP bilirubin ขึ้นลงคนละจังหวะ (gi-lft-05)
def a_choltime():
    X0, Y0, DX, H = 50, 372, 26.4, 200
    P = lambda d, v: (X0 + DX * d, Y0 - H * v)
    curve = lambda lst: pts([P(d, v) for d, v in lst])
    p = [box(16, 26, 84, 48, "sk", "ตับ", "b"),
         rect(100, 42, 228, 16, "ms", 4), t(214, 34, "CBD", "mid xs b"),
         box(330, 22, 94, 56, "bad", "ลำไส้เล็ก", "sm b"),
         X(3, t(377, 98, "อุจจาระน้ำตาล", "mid xs"))]
    for i in range(3):
        p.append(X(2, mover(3.5, "msf", "2.4s", "M104 50 L340 50", "-%.1fs" % (0.8 * i))))
    # ขั้น 3 ท่อขยาย (วาดก่อนก้อนนิ่ว)
    p.append(S(3, rect(100, 34, 140, 32, "ms", 6), t(160, 88, "ท่อเหนือนิ่วขยาย", "mid xs b"),
               t(58, 96, "ย้อนเข้าเลือด", "mid xs b tbad"), ar(58, 74, 58, 82, "lbad w2", "ah-bad")))
    p.append(S(3, t(377, 114, "อุจจาระซีด", "mid xs b tbad"), x=4))
    p.append(S(4, t(377, 130, "อุจจาระกลับสีเดิม", "mid xs b tok")))
    p.append(S(2, G("pl", circ(252, 50, 11, "muf")), x=4))
    p.append(S(2, t(252, 84, "นิ่วอุด", "mid xs b tbad"), x=4))
    p.append(S(4, t(270, 104, "ERCP เอานิ่วออก", "mid xs b tok"),
               mover(3.5, "msf", "2.4s", "M104 50 L340 50"), mover(3.5, "msf", "2.4s", "M104 50 L340 50", "-1.2s")))
    # กราฟ
    p += [line(X0, Y0, 424, Y0, "ln w2"), line(X0, Y0, X0, 170, "ln w2"),
          t(X0 - 4, 164, "ระดับ (สัมพัทธ์)", "xs mu"),
          t(X0, Y0 + 16, "0", "mid xs"), t(P(3, 0)[0], Y0 + 16, "3", "mid xs"), t(P(7, 0)[0], Y0 + 16, "7", "mid xs"),
          t(P(14, 0)[0], Y0 + 16, "14 วัน", "end xs")]
    alt = [(0, .05), (.5, .5), (1, .85), (1.5, .6), (2, .4), (3, .22), (4, .13), (6, .07), (14, .05)]
    alp_up = [(0, .05), (1, .2), (2, .45), (3, .6)]
    alp_dn = [(3, .6), (6, .42), (9, .3), (12, .21), (14, .17)]
    bil_up = [(0, .05), (1, .3), (2, .6), (3, .8)]
    bil_dn = [(3, .8), (4, .6), (5, .48), (7, .4), (10, .34), (14, .3)]
    p.append(S(2, path(curve(alt), "lbad w3"), line(250, 148, 268, 148, "lbad w3"), t(272, 152, "ALT", "xs b tbad")))
    p.append(S(3, path(curve(bil_up), "lms w3"), path(curve(alp_up), "lac w3"),
               line(310, 148, 328, 148, "lms w3"), t(332, 152, "bilirubin", "xs b"),
               line(150, 148, 168, 148, "lac w3"), t(172, 152, "ALP", "xs b tac")))
    p.append(S(4, line(P(3, 0)[0], Y0, P(3, 0)[0], 166, "lok w2 da"), t(P(3, 0)[0] + 4, 178, "ERCP", "xs b tok")))
    p.append(S(5, path(curve(bil_dn), "lms w3"), path(curve(alp_dn), "lac w3"),
               t(420, P(14, .3)[1] - 8, "bilirubin ค้าง (delta)", "end xs b"),
               t(420, P(14, .17)[1] + 16, "ALP t½ 5–7 วัน", "end xs b tac")))
    return SVG(440, 392, "ภาพเคลื่อนไหว: นิ่วอุดท่อน้ำดีร่วม ALT พุ่งชั่วคราวแล้วลงเร็ว ท่อเหนือนิ่วขยาย bilirubin และ ALP ค่อย ๆ สูงขึ้น "
               "อุจจาระซีด หลัง ERCP เอานิ่วออก ALP ลดช้าตามครึ่งชีวิตห้าถึงเจ็ดวัน และ bilirubin ค้างนานจาก delta bilirubin", *p)


CHOLTIME_STEPS = [
    {"t": "ปกติ: น้ำดีไหลผ่าน CBD ลงลำไส้",
     "cap": "conjugated bilirubin + กรดน้ำดี ไหลจากตับลงลำไส้ → แบคทีเรียเปลี่ยนเป็น stercobilin → **อุจจาระสีน้ำตาล** · กรดน้ำดีช่วยดูดซึมไขมันและวิตามิน A D E K"},
    {"t": "นิ่วหลุดมาอุด → ALT พุ่งชั่วคราว",
     "cap": "แรงดันในท่อที่ขึ้นทันทีทำให้เซลล์ตับรอบ portal บาดเจ็บ → **ALT/AST ขึ้นได้หลายร้อยถึง > 1,000 ใน 24–48 ชม. แล้วลงเร็ว** — นี่คือ **\"acute passing stone\"** ที่สไลด์ 2570 จัดเป็นสาเหตุของ **mixed pattern**"},
    {"t": "น้ำดีค้าง → bilirubin ALP ขึ้น อุจจาระซีด",
     "cap": "conjugated bilirubin **ย้อนเข้าเลือด** → เหลือง **ปัสสาวะสีชา** · ลำไส้ไม่ได้ bilirubin → **อุจจาระซีด** · กรดน้ำดีค้าง **เหนี่ยวนำการสร้าง ALP** (ขึ้นช้ากว่า 1–2 วัน) · ท่อเหนือจุดอุด **ขยาย** = macro-duct (obstructive) cholestasis → เห็นใน US"},
    {"t": "ERCP เอานิ่วออก",
     "cap": "ถ้ามี **Charcot's triad (ไข้ เหลือง ปวดชายโครงขวา)** = ascending cholangitis → ยาปฏิชีวนะ + **ระบายท่อด้วย ERCP** (algorithm สไลด์ 2570: ท่อขยาย → ประเมิน S&S cholangitis → **ERCP หรือ CT**) · น้ำดีกลับมาไหล"},
    {"t": "หลังแก้: แต่ละค่าลงคนละจังหวะ",
     "cap": "ALT ปกติในไม่กี่วัน · **ALP ครึ่งชีวิต 5–7 วัน** (สไลด์ 2570) → ยังสูงอีกหลายวัน · bilirubin ส่วนหนึ่งจับ albumin แบบโควาเลนต์ (**delta bilirubin**, t½ ~20 วัน) → **เหลืองค้างนาน** ทั้งที่ท่อโล่งแล้ว — ไม่ได้แปลว่า ERCP ล้มเหลว"},
]


# ═══════════════════════════════════ 8 · ALP มาจากไหน — GGT เป็นตัวตัดสิน (gi-lft-06)
def a_alpggt():
    src = [(12, "กระดูก", "(osteoblast)", "sk"), (116, "รก", "(ไตรมาส 3)", "sk"),
           (220, "ตับ/ท่อน้ำดี", "", "ms"), (324, "เหล้า · ยากันชัก", "· warfarin", "sk")]
    p = []
    for x, a, b, c in src:
        p.append(rect(x, 16, 98, 50, c, 8))
        p.append(t(x + 49, 36 if b else 46, a, "mid sm b"))
        if b:
            p.append(t(x + 49, 54, b, "mid xs"))
    p += [pill(96, 130, "ALP", "ac", "sm b mid", 90), pill(254, 130, "GGT", "wa", "sm b mid", 90),
          t(141, 172, "กระดูก รก ตับ ลำไส้ ไต", "mid xs i2"), t(299, 172, "ไม่มีในกระดูก", "mid xs b twa")]
    p.append(S(2, ar(61, 66, 118, 128, "lac w2", "ah-ac"), ar(165, 66, 141, 128, "lac w2", "ah-ac"),
               rect(10, 190, 420, 38, "sk", 8), t(20, 206, "ALP ↑ + GGT ปกติ", "sm b"),
               t(20, 222, "→ กระดูก (Paget mets กระดูกหัก วัยรุ่น) · รก (ตั้งครรภ์)", "xs")))
    p.append(S(3, ar(250, 66, 168, 128, "lms w3", "ah-ms"), ar(280, 66, 290, 128, "lms w3", "ah-ms"),
               rect(10, 236, 420, 54, "ms", 8), t(20, 252, "ALP ↑ + GGT ↑ (5′NT ↑) = ตับ", "sm b"),
               t(20, 268, "ท่อหลักตันท่อเดียว · แทรกซึม/ก้อน · cholestasis ระยะแรก", "xs"),
               t(20, 283, "(PBC · ยา) — ✍️ \"จำ DDx\"", "xs")))
    p.append(S(4, ar(373, 66, 322, 128, "lbad w2", "ah-bad"), t(360, 104, "induction", "xs b tbad"),
               rect(10, 298, 420, 38, "wa", 8), t(20, 314, "GGT ↑ อย่างเดียว → เหล้า · กันชัก · warfarin", "sm b"),
               t(20, 330, "แต่ 1/3 ของผู้ติดสุราเรื้อรัง GGT ไม่สูง (สไลด์ 2570)", "xs")))
    p.append(S(5, rect(10, 344, 420, 38, "bad", 8), t(20, 360, "ALP t½ 5–7 วัน → ค้างหลังแก้การอุดตัน", "sm b"),
               t(20, 376, "ยืนยันว่า ALP มาจากตับ: GGT หรือ 5′NT สูงร่วม", "xs")))
    return SVG(440, 390, "ภาพเคลื่อนไหว: ALP มาจากกระดูก รก และตับ ส่วน GGT ไม่มีในกระดูก ALP สูงกับ GGT ปกติจึงมาจากกระดูกหรือรก "
               "ALP และ GGT สูงคู่กันมาจากตับ GGT สูงอย่างเดียวจากเหล้าและยาที่เหนี่ยวนำเอนไซม์", *p)


ALPGGT_STEPS = [
    {"t": "ALP มีหลายแหล่ง · GGT ไม่มีในกระดูก",
     "cap": "สไลด์ 2570 วาดเป็น Venn: **ALP** มาจาก **กระดูก ตับ รก ลำไส้ ไต** · **GGT** อยู่ในตับและท่อน้ำดี (ไต ตับอ่อน ฯลฯ) แต่ **NOT found in bone disease** → ✍️ ส่วนที่ ALP กับ GGT ซ้อนกัน = **\"Liver\"**"},
    {"t": "ALP สูง + GGT ปกติ → ไม่ใช่ตับ",
     "cap": "osteoblast ที่สร้างกระดูกใหม่ (วัยรุ่น Paget มะเร็งกระจายไปกระดูก กระดูกหักกำลังติด) และรกในไตรมาสสาม สร้าง ALP ของตัวเองโดยไม่มี GGT → **ALP สูงอย่างเดียว GGT ปกติ = ไม่ต้องไล่โรคตับ**"},
    {"t": "ALP + GGT สูงคู่กัน → ตับ",
     "cap": "กลไกของ isolated ALP จากตับ = **อุดตันท่อน้ำดีขนาดเล็กหรือบางส่วน**: ท่อหลักตันเพียงท่อเดียว · infiltrative/ก้อน · cholestasis ระยะแรก (PBC ยา) — ตับส่วนที่เหลือยังขับ bilirubin ได้ bilirubin จึงปกติ"},
    {"t": "GGT สูงอย่างเดียว → enzyme induction",
     "cap": "เหล้า ยากันชัก (phenytoin carbamazepine) และ warfarin **เหนี่ยวนำการสร้าง GGT** โดยไม่มี cholestasis · สไลด์ 2570 เพิ่ม: **1/3 ของผู้ป่วยพิษสุราเรื้อรัง GGT อาจไม่สูง** — GGT ปกติจึงตัดการดื่มออกไม่ได้"},
    {"t": "ALP ลงช้า — ครึ่งชีวิต 5–7 วัน",
     "cap": "หลังแก้การอุดตันแล้ว ALP ยัง **สูงอยู่หลายวัน** (t½ 5–7 วัน สไลด์ 2570) · ยืนยันแหล่งตับด้วย **GGT หรือ 5′-nucleotidase** ที่สูงร่วม (หรือ ALP isoenzyme)"},
]


# ═══════════════════════════════════ 9 · PT กับวิตามิน K · DIC vs ตับวาย (gi-lft-07)
def a_vitk():
    p = [box(16, 22, 116, 56, "wa", "ลำไส้: ดูดซึม\nวิตามิน K\n(ละลายในไขมัน)", "", fs=11),
         rect(176, 14, 150, 96, "sk", 12), t(251, 34, "เซลล์ตับ", "mid sm b"),
         t(251, 54, "γ-carboxylation", "mid xs"), t(251, 72, "II VII IX X", "mid sm b"), t(251, 90, "(+ V fibrinogen)", "mid xs"),
         box(340, 14, 84, 56, "bad", "endothelium\nสร้าง VIII", "", fs=11),
         X(2, ar(132, 40, 174, 40, "lok w2 fl", "ah-ok")), t(153, 32, "vit K", "mid xs b tok"),
         ar(176, 96, 134, 70, "lms w2 fl", "ah-ms"), t(118, 98, "น้ำดี", "mid xs b"),
         ar(251, 110, 251, 128, "ln w2", "ah"), pill(214, 130, "PT / INR", "ac", "sm b mid", 74)]
    p.append(S(2, ar(132, 40, 174, 40, "lbad w2 da", "ah-bad"), line(144, 72, 160, 90, "lbad w3"), line(160, 72, 144, 90, "lbad w3"),
               rect(10, 168, 136, 132, "ms", 8), t(78, 188, "ท่อน้ำดีอุดตัน", "mid sm b"),
               t(78, 208, "ไม่มีน้ำดี → ดูด K ไม่ได้", "mid xs"), t(78, 226, "PT ยาว", "mid xs b"),
               t(78, 246, "ฉีด vit K SC/IV", "mid xs"), t(78, 264, "→ PT ปกติใน 24–48 ชม.", "mid xs b tok"),
               t(78, 284, "factor V ปกติ", "mid xs")))
    p.append(S(3, G("pl", rect(176, 14, 150, 96, "lbad w3", 12)),
               rect(152, 168, 136, 132, "bad", 8), t(220, 188, "ตับวาย", "mid sm b"),
               t(220, 208, "เซลล์สร้างไม่ได้", "mid xs"), t(220, 226, "PT ยาว", "mid xs b"),
               t(220, 246, "ฉีด vit K", "mid xs"), t(220, 264, "→ ไม่ดีขึ้น", "mid xs b tbad"),
               t(220, 284, "V ต่ำ · VIII ปกติ/สูง", "mid xs")))
    p.append(S(4, rect(294, 168, 136, 132, "ac", 8), t(362, 188, "DIC", "mid sm b"),
               t(362, 208, "ใช้ factor จนหมด", "mid xs"), t(362, 226, "PT aPTT ยาว", "mid xs b"),
               t(362, 246, "ทุกตัวต่ำ", "mid xs"), t(362, 264, "รวม VIII ↓", "mid xs b tbad"),
               t(362, 284, "PLT ↓ D-dimer ↑", "mid xs"),
               t(220, 320, "✍️ \"DIC ↓ ทั้งหมด / VIII ยังอยู่ → Liver\"", "mid xs b tac")))
    p.append(S(5, rect(10, 334, 420, 52, "sk", 8),
               t(20, 354, "factor VII t½ ~6 ชม. → PT ยาวเร็ว = บอกความรุนแรงตอนนี้", "xs b"),
               t(20, 374, "albumin t½ ~20 วัน → ตัวชี้วัดระยะยาว = บอกความเรื้อรัง", "xs b")))
    return SVG(440, 394, "ภาพเคลื่อนไหว: วิตามิน K ดูดซึมจากลำไส้โดยอาศัยน้ำดี ตับใช้สร้าง factor II VII IX X ที่วัดด้วย PT "
               "ส่วน factor VIII สร้างที่ endothelium ท่อน้ำดีอุดตัน PT ยาวแต่แก้ได้ด้วยวิตามิน K ตับวาย PT ยาวแก้ไม่ได้ VIII ปกติ "
               "DIC ใช้ factor หมดทุกตัวรวม VIII", *p)


VITK_STEPS = [
    {"t": "PT วัด factor ที่ตับสร้าง",
     "cap": "ตับ **สร้าง clotting factor ทั้งหมดยกเว้น VIII** (สร้างที่ endothelial cell) · II VII IX X ต้องใช้ **วิตามิน K** เติมหมู่ carboxyl จึงทำงานได้ · วิตามิน K ละลายในไขมัน → ดูดซึมได้ต้องมี **น้ำดี**"},
    {"t": "ท่อน้ำดีอุดตัน → ขาดวิตามิน K",
     "cap": "ไม่มีน้ำดีในลำไส้ → ดูดวิตามิน K ไม่ได้ → PT ยาว ทั้งที่เซลล์ตับปกติ · **ฉีดวิตามิน K ใต้ผิวหนัง (สไลด์) / IV** → PT ดีขึ้น = **ขาดวิตามิน K** (เช่นเดียวกับยาปฏิชีวนะ ขาดอาหาร)"},
    {"t": "ตับวาย → ให้ K ก็สร้างไม่ได้",
     "cap": "เซลล์ตับที่เหลือน้อย **ใช้วิตามิน K ไม่ได้** → PT ไม่ตอบสนอง = **liver dysfunction** · factor V (ไม่ขึ้นกับวิตามิน K) ต่ำ ยืนยันว่าตับสร้างไม่ได้ · **factor VIII ปกติหรือสูง** เพราะไม่ได้สร้างที่ตับ"},
    {"t": "DIC → ใช้หมดทุกตัว รวม VIII",
     "cap": "✍️ อาจารย์เขียนใต้สไลด์ synthetic function: **\"DIC ↓ ทั้งหมด / VIII ยังอยู่ → Liver\"** · DIC กินทั้ง factor และเกล็ดเลือด → **VIII ต่ำ** · ตับวาย VIII ยังอยู่ → ใช้ factor VIII แยกสองภาวะที่ PT ยาวทั้งคู่"},
    {"t": "PT = เฉียบพลัน · albumin = เรื้อรัง",
     "cap": "สไลด์ 2570 เรียก **PT = ตัวชี้วัดกระบวนการสร้าง** (factor VII t½ ~6 ชม. → เปลี่ยนในวัน ใช้ติดตามตับวายเฉียบพลัน) และ **albumin = ตัวชี้วัดระยะยาว** (t½ ~20 วัน → ลดในโรคตับเรื้อรัง/ตับแข็ง มักคู่กับ globulin สูง)"},
]


# ═══════════════════════════════════ 10 · ตับคั่งเลือด → direct bilirubin สูง (gi-lft-12)
def a_congest():
    p = [box(10, 56, 64, 48, "wa", "portal\nvein", "", fs=11),
         rect(80, 62, 182, 36, "sk", 4), t(171, 52, "sinusoid  zone 1 → 3", "mid xs b"),
         circ(284, 80, 18, "wa"), t(284, 84, "CV", "mid xs b"),
         rect(302, 74, 40, 12, "wa", 2), t(340, 114, "hepatic v.", "end xs"),
         rect(344, 40, 18, 112, "wa", 4), t(353, 166, "IVC", "mid xs b"),
         box(368, 22, 62, 54, "ok", "หัวใจ\nห้องขวา", "", fs=11)]
    for i in range(3):
        p.append(X(2, mover(3.5, "waf", "3s", "M74 80 L284 80 L353 80 L353 50 L368 50", "-%.1fs" % (1.0 * i))))
    p.append(S(2, G("pl", rect(368, 22, 62, 54, "lbad w3", 8)),
               path("M368 60 L353 60 L353 80 L300 80", "lbad w3 fl"), t(399, 94, "CVP ↑", "mid xs b tbad"),
               G("pl", rect(206, 54, 58, 52, "lbad w3", 4)), t(232, 124, "zone 3 คั่ง", "mid xs b tbad")))
    p.append(S(3, line(314, 72, 330, 88, "lbad w3"), line(330, 72, 314, 88, "lbad w3"), t(322, 134, "BCS", "mid xs b tbad"),
               line(130, 70, 146, 90, "lbad w3"), line(146, 70, 130, 90, "lbad w3"), t(138, 124, "SOS", "mid xs b tbad")))
    p.append(S(2, rect(10, 180, 136, 124, "bad", 8), t(78, 200, "หัวใจล้มเหลว (HF)", "mid sm b"),
               t(78, 220, "JVP สูง ตับโตกดเจ็บ", "mid xs"), t(78, 238, "hepatojugular reflux", "mid xs"),
               t(78, 256, "DB ↑ · ALP GGT ↑ น้อย", "mid xs b"), t(78, 274, "ALT ↑ เล็กน้อย", "mid xs"),
               t(78, 292, "\"nutmeg liver\"", "mid xs i2")))
    p.append(S(3, rect(152, 180, 136, 124, "ac", 8), t(220, 200, "ไม่ใช่ HF (✍️ N-HF)", "mid sm b"),
               t(220, 220, "BCS: ลิ่มเลือดอุด", "mid xs"), t(220, 238, "hepatic vein / IVC", "mid xs"),
               t(220, 256, "SOS: endothelium", "mid xs"), t(220, 274, "ของ sinusoid เสีย", "mid xs"),
               t(220, 292, "Hyperthyroidism", "mid xs b")))
    p.append(S(4, rect(294, 180, 136, 124, "ms", 8), t(362, 200, "ทำไม direct ↑", "mid sm b"),
               t(362, 220, "zone 3 ขาด O₂ ฝ่อ", "mid xs"), t(362, 238, "sinusoid โป่งกด", "mid xs"),
               t(362, 256, "canaliculus", "mid xs"), t(362, 274, "→ ขับ bilirubin", "mid xs"),
               t(362, 292, "ที่จับคู่แล้วไม่ทัน", "mid xs b")))
    p.append(S(5, rect(10, 314, 420, 72, "sk", 8),
               t(20, 334, "DB/TB > 0.5 (สไลด์ 2570): liver congestion · alcoholic hepatitis", "xs b"),
               t(20, 352, "· end-stage cirrhosis · DILI  (+ cholestasis ทุกชนิด)", "xs b"),
               t(20, 372, "✍️ \"Direct\" · \"ผู้ใหญ่\" — ผู้ใหญ่ที่เหลือง ส่วนใหญ่เป็น direct", "xs tac b")))
    return SVG(440, 394, "ภาพเคลื่อนไหว: เลือดไหลจาก portal vein ผ่าน sinusoid central vein hepatic vein IVC เข้าหัวใจห้องขวา "
               "หัวใจล้มเหลวทำให้ความดันย้อนจนตับ zone 3 คั่ง Budd-Chiari และ SOS อุดทางออก "
               "ผลคือ zone 3 ขาดออกซิเจนและ sinusoid โป่งกดท่อน้ำดีฝอย direct bilirubin จึงสูง", *p)


CONGEST_STEPS = [
    {"t": "ทางออกของเลือดจากตับ",
     "cap": "เลือดจาก portal vein ไหลผ่าน **sinusoid (zone 1 → 3)** เข้า **central vein → hepatic vein → IVC → หัวใจห้องขวา** · ตับไม่มีลิ้นกั้น ความดันในหัวใจห้องขวาจึงส่งย้อนถึง sinusoid ได้ตรง ๆ"},
    {"t": "หัวใจล้มเหลว → ความดันย้อน → zone 3 คั่ง",
     "cap": "right HF / TR / constrictive → **CVP สูง** → sinusoid รอบ central vein โป่งคั่งเลือด (**congestive hepatopathy · nutmeg liver**) → ตับโตกดเจ็บ hepatojugular reflux · ✍️ อาจารย์แตก \"Liver congest\" เป็น **HF / N-HF**"},
    {"t": "ไม่ใช่หัวใจ: BCS · SOS · hyperthyroidism",
     "cap": "**Budd–Chiari (BCS)**: ลิ่มเลือดอุด hepatic vein/IVC (ภาวะเลือดข้น MPN) · **SOS (VOD)**: endothelium ของ sinusoid ถูกทำลาย (หลัง HSCT, pyrrolizidine alkaloid) · **hyperthyroidism**: high-output HF + ความต้องการ O₂ ของ zone 3 สูง + ฮอร์โมนทำลายเซลล์ตรง → เหลืองแบบ cholestatic"},
    {"t": "ทำไม bilirubin เป็น direct",
     "cap": "zone 3 ขาด O₂ จนเซลล์ฝ่อ + sinusoid ที่โป่ง **กดท่อน้ำดีฝอย** → เซลล์จับคู่ bilirubin ได้แต่ **ขับออกไม่ทัน** → **conjugated (direct) bilirubin สูง** · ALP GGT สูงเล็กน้อย ALT สูงเล็กน้อย · ถ้า cardiac output ตกฉับพลัน → **shock liver** (ALT หลายพัน)"},
    {"t": "สาเหตุ direct hyperbilirubinemia ตามสไลด์ 2570",
     "cap": "**DB/TB > 0.5** = ความผิดปกติ **ที่ตับหรือหลังตับ**: cholestasis (หัวข้อก่อน ๆ) + ที่สไลด์ใหม่เพิ่ม **liver congestion (congestive hepatopathy BCS SOS hyperthyroidism) · alcoholic hepatitis · end-stage cirrhosis · DILI** · ✍️ \"ผู้ใหญ่\" — เหลืองในผู้ใหญ่ส่วนใหญ่เป็นชนิด direct"},
]


# ═══════════════════════════════════ 11 · HBV serology + core window (gi-lft-13)
def a_hbv():
    X0, Y0, DX, H = 44, 236, 46.5, 170
    P = lambda m, v: (X0 + DX * m, Y0 - H * v)
    curve = lambda lst: pts([P(m, v) for m, v in lst])
    p = [line(X0, Y0, 420, Y0, "ln w2"), line(X0, Y0, X0, 56, "ln w2"),
         line(X0, Y0 - H * .1, 420, Y0 - H * .1, "lmu da")]
    for m in range(0, 9):
        p.append(t(P(m, 0)[0], Y0 + 15, str(m), "mid xs"))
    p.append(t(232, Y0 + 30, "เดือนหลังสัมผัสเชื้อ · เส้นประ = ระดับที่ตรวจพบ", "mid xs mu"))
    p.append(S(3, rect(P(5.2, 0)[0], 56, P(6.0, 0)[0] - P(5.2, 0)[0], Y0 - 56, "ms", 2),
               t((P(5.2, 0)[0] + P(6.0, 0)[0]) / 2, 50, "core window", "mid xs b tms")))
    hbs = [(.8, 0), (1.5, .1), (2.3, .6), (3.3, .8), (4.3, .45), (5, .12), (5.4, 0)]
    igm = [(2.2, 0), (3, .4), (4, .62), (5, .58), (6, .4), (7, .15), (7.8, .04)]
    igg = [(2.0, 0), (2.6, .45), (3.5, .82), (5, .9), (8, .92)]
    ahbs = [(5.7, 0), (6.1, .12), (7, .55), (8, .66)]
    p.append(path(curve(hbs), "lbad w3"))
    p.append(S(2, path(curve(igm), "lms w3"), path(curve(igg), "lac w2")))
    p.append(S(4, path(curve(ahbs), "lok w3")))
    p.append(S(5, path(pts([P(3.3, .8), P(4.5, .74), P(8, .74)]), "lbad w2 da")))
    # legend
    p += [line(14, 278, 34, 278, "lbad w3"), t(38, 282, "HBsAg", "xs b tbad")]
    p.append(S(2, line(104, 278, 124, 278, "lms w3"), t(128, 282, "anti-HBc IgM", "xs b"),
               line(220, 278, 240, 278, "lac w2"), t(244, 282, "anti-HBc IgG", "xs b tac")))
    p.append(S(4, line(334, 278, 354, 278, "lok w3"), t(358, 282, "anti-HBs", "xs b tok")))
    p.append(S(3, rect(10, 294, 420, 30, "ms", 6), t(20, 314, "Core window: HBsAg − · anti-HBs − · anti-HBc IgM + → acute HBV", "xs b")))
    p.append(S(4, rect(10, 330, 420, 30, "ok", 6), t(20, 350, "หายแล้ว: anti-HBs + และ anti-HBc IgG + · วัคซีน: anti-HBs + อย่างเดียว", "xs b")))
    p.append(S(5, rect(10, 366, 420, 30, "bad", 6), t(20, 386, "Chronic: HBsAg + นาน > 6 เดือน + anti-HBc IgG + · anti-HBs −", "xs b")))
    return SVG(440, 404, "ภาพเคลื่อนไหว: กราฟผลเลือดไวรัสตับอักเสบบีตามเวลา HBsAg ขึ้นก่อน ตามด้วย anti-HBc IgM และ IgG "
               "HBsAg หายก่อน anti-HBs จะขึ้นเกิดช่วง core window ที่มีแต่ anti-HBc IgM บวก "
               "anti-HBs ขึ้นเมื่อหาย และถ้า HBsAg ค้างเกินหกเดือนเป็นโรคเรื้อรัง", *p)


HBV_STEPS = [
    {"t": "HBsAg ขึ้นก่อน — มีเชื้ออยู่ในตัว",
     "cap": "หลังระยะฟักตัว 1–2 เดือน **HBsAg** (โปรตีนเปลือกไวรัส) ขึ้นเหนือระดับที่ตรวจพบ ก่อนมีอาการ · HBeAg = ไวรัสแบ่งตัวสูง (replicative phase) แพร่เชื้อง่าย"},
    {"t": "Anti-HBc IgM = ตัวบอก acute",
     "cap": "ภูมิต่อ core antigen ขึ้นพร้อมอาการและ ALT · **IgM = ติดเชื้อเฉียบพลัน** (ตาราง 2570: acute = HBsAg +/− · anti-HBc IgG +/− · **anti-HBc IgM +**) · IgG ค้างตลอดชีวิตไม่ว่าจะหายหรือเรื้อรัง"},
    {"t": "Core window — HBsAg หายก่อน anti-HBs ขึ้น",
     "cap": "ช่วงที่ร่างกายกำจัด HBsAg ได้แล้วแต่ anti-HBs ยังไม่ถึงระดับที่ตรวจพบ → **ตรวจแค่ HBsAg จะได้ผลลบปลอม** · มีแต่ **anti-HBc IgM บวก** (✍️ อาจารย์เขียน \"acute\" ที่ core window) → ผู้ป่วยตับอักเสบเฉียบพลันจึงต้องส่ง **HBsAg + IgM anti-HBc** คู่กัน"},
    {"t": "Anti-HBs ขึ้น = หายและมีภูมิ",
     "cap": "**anti-HBs + และ anti-HBc IgG +** = เคยติดเชื้อแล้วหาย (immune, past) · **anti-HBs + อย่างเดียว** = ภูมิจากวัคซีน (วัคซีนมีแต่ HBsAg ไม่มี core) · ทุกตัวลบ = susceptible"},
    {"t": "Chronic — HBsAg ค้างเกิน 6 เดือน",
     "cap": "ไม่สร้าง anti-HBs → **HBsAg + นาน > 6 เดือน + anti-HBc IgG +** · ติดตอนเป็นผู้ใหญ่กลายเป็นเรื้อรังส่วนน้อย แต่ติดจากแม่ส่วนใหญ่เรื้อรัง → ในไทย ✍️ **\"chronic > acute (พบมากกว่า)\"** เมื่อเจอ HBsAg บวก"},
]


# ═══════════════════════════════════ ตำแหน่ง: sec + after (หัวข้อ ###/#### ใน md ตรงตัวอักษร · "" = ท้าย section)
# หัวข้อใหม่ (gi-lft-09..13) ใส่ [[anim:key]] ไว้ใน md เองแล้ว → after = None
ITEMS = [
    {"sec": "gi-lft-01", "after": "R ratio (ACG 2017)",
     "anim": {"key": "lft7-rratio", "title": "R ratio — วางเคสจากสไลด์ 2570 บนสเกลเดียวกัน", "svg": a_rratio(), "steps": RRATIO_STEPS}},
    {"sec": "gi-lft-02", "after": "อัตราส่วน AST/ALT (สไลด์)",
     "anim": {"key": "lft7-leak", "title": "เอนไซม์แต่ละตัวรั่วจากส่วนไหนของเซลล์ตับ", "svg": a_leak(), "steps": LEAK_STEPS}},
    {"sec": "gi-lft-04", "after": "Autoimmune hepatitis (สไลด์)",
     "anim": {"key": "lft7-aih", "title": "AIH — interface hepatitis → globulin สูง → A/G กลับข้าง", "svg": a_aih(), "steps": AIH_STEPS}},
    {"sec": "gi-lft-05", "after": "เคสในสไลด์",
     "anim": {"key": "lft7-choltime", "title": "นิ่วอุด CBD — ALT ALP bilirubin ขึ้นลงคนละจังหวะ", "svg": a_choltime(), "steps": CHOLTIME_STEPS}},
    {"sec": "gi-lft-06", "after": "GGT (สไลด์)",
     "anim": {"key": "lft7-alpggt", "title": "ALP สูง — GGT บอกว่ามาจากตับหรือไม่", "svg": a_alpggt(), "steps": ALPGGT_STEPS}},
    {"sec": "gi-lft-07", "after": "Prothrombin time (สไลด์)",
     "anim": {"key": "lft7-vitk", "title": "PT ยาว — ขาดวิตามิน K ตับวาย หรือ DIC", "svg": a_vitk(), "steps": VITK_STEPS}},
    {"sec": "gi-lft-09", "after": None,
     "anim": {"key": "lft7-zone3", "title": "Zone 3 — ทำไมช็อก paracetamol เหล้า ทำลายรอบ central vein", "svg": a_zone3(), "steps": ZONE3_STEPS}},
    {"sec": "gi-lft-10", "after": None,
     "anim": {"key": "lft7-masld", "title": "MASLD — insulin resistance → ไขมันพอก → ALT รั่ว → พังผืด", "svg": a_masld(), "steps": MASLD_STEPS}},
    {"sec": "gi-lft-11", "after": None,
     "anim": {"key": "lft7-wilson", "title": "Wilson disease — ATP7B เสีย ทองแดงล้นจากตับไปทั้งตัว", "svg": a_wilson(), "steps": WILSON_STEPS}},
    {"sec": "gi-lft-12", "after": None,
     "anim": {"key": "lft7-congest", "title": "ตับคั่งเลือด — ทำไม direct bilirubin สูงโดยไม่มีอะไรอุดท่อ", "svg": a_congest(), "steps": CONGEST_STEPS}},
    {"sec": "gi-lft-13", "after": None,
     "anim": {"key": "lft7-hbv", "title": "ผลเลือด HBV ตามเวลา — core window", "svg": a_hbv(), "steps": HBV_STEPS}},
]

MNEM = [
    {"sec": "gi-lft-01", "name": "R > 5 · 2–5 · < 2", "what": "R ratio — จำแค่เลข 2 กับ 5 แล้วถามว่า ALT หรือ ALP นำ",
     "lines": [["> 5", "**Hepatocellular** — ALT นำ → ไวรัส ยา ขาดเลือด AIH Wilson"],
               ["2–5", "**Mixed** — DILI (✍️ วงเป็นข้อ 1) · overlap · นิ่วกำลังเคลื่อน · LFT ของ SIRS"],
               ["< 2", "**Cholestatic** — ALP นำ → **อัลตราซาวนด์** ดูท่อขยาย"]],
     "note": "ใช้ ALT (ไม่ใช้ AST) และหารด้วย ULN ของแล็บนั้นก่อนเสมอ · เกณฑ์ DILI สากลเขียนเป็น ≥ 5 และ ≤ 2 ความหมายเดียวกับสไลด์",
     "src": "หลักจำทั่วไป — เกณฑ์ R ratio ของ ACG 2017 / CIOMS (DILI)"},
    {"sec": "gi-lft-09", "name": "Zone 1 · 2 · 3", "what": "บริเวณของ acinus ที่ถูกทำลายในแต่ละโรค",
     "lines": [["Zone 1", "periportal — O₂ สูงสุด · ไวรัสตับอักเสบ · สารพิษที่กินเข้าไป (เช่น cocaine)"],
               ["Zone 2", "midzonal — yellow fever"],
               ["Zone 3", "pericentral — O₂ ต่ำสุด CYP450 มากสุด · **ขาดเลือด · paracetamol · เหล้า · halothane** · alcoholic hepatitis"]],
     "note": "ตรงกับลายมืออาจารย์ ✍️ \"Zone 3 = sensitive to shock / Para / เหล้า / halothane\"",
     "src": "First Aid for the USMLE Step 1 (Gastrointestinal — Liver tissue architecture)"},
    {"sec": "gi-lft-09", "name": "> 1,000: Shock · Toxin · Virus", "what": "สาเหตุหลักของ transaminase สูงเป็นพัน",
     "lines": [["Shock", "ischemic hepatitis (**shock liver**) — หลังความดันตก ALT/LDH < 1.5"],
               ["Toxin", "**paracetamol** (✍️ \"only this\") · เห็ดพิษ"],
               ["Virus", "HAV HBV HEV เฉียบพลัน (HSV ในคนภูมิต่ำ/ตั้งครรภ์)"],
               ["+ อื่น", "AIH flare · Wilson · นิ่วเคลื่อนเฉียบพลัน · Budd–Chiari"],
               ["ไม่ใช่ตับ", "**rhabdomyolysis** — AST >> ALT · CK สูงมาก"]],
     "note": "อาจารย์สรุป ✍️ \"DDx 3 โรค: Para + Ischemic + Rhabdomyolysis\" — สามข้อนี้ขึ้นได้ถึงหลายพัน",
     "src": "หลักจำทั่วไป — กลุ่มสาเหตุของ marked aminotransferase elevation (ACG 2017)"},
    {"sec": "gi-lft-11", "name": "ABCD (Wilson)", "what": "อาการและสิ่งตรวจพบของ Wilson disease",
     "lines": [["A", "**A**sterixis"],
               ["B", "**B**asal ganglia degeneration — parkinsonism/extrapyramidal (✍️ ไม่ใช่ corticospinal tract)"],
               ["C", "**C**eruloplasmin ↓ · **C**irrhosis · **C**orneal deposits (KF ring) · **C**opper accumulation · **C**horeiform movements"],
               ["D", "**D**ementia · **D**ysarthria · **D**ystonia"],
               ["+ H", "**H**emolytic anemia แบบ Coombs ลบ"]],
     "note": "สไลด์ 2570 ให้จำเพิ่ม: Wilsonian ALF → **AST/ALT > 2.2 + ALP/TB < 4** · ถ่ายทอดแบบ AR (ATP7B)",
     "src": "First Aid for the USMLE Step 1 (ฉบับก่อน ๆ — Wilson disease \"ABCD\")"},
    {"sec": "gi-lft-06", "name": "ALP สูง → \"กระดูก รก หรือตับ\"", "what": "แหล่งของ ALP และวิธีแยกด้วย GGT",
     "lines": [["กระดูก", "วัยรุ่น · Paget · มะเร็งกระจายไปกระดูก · กระดูกหักกำลังติด → **GGT ปกติ**"],
               ["รก", "ตั้งครรภ์ไตรมาสสาม → **GGT ปกติ**"],
               ["ตับ", "**GGT/5′NT สูงร่วม** → ท่อหลักตันท่อเดียว · แทรกซึม/ก้อน · cholestasis ระยะแรก (PBC ยา)"]],
     "note": "✍️ สไลด์ 2570 เขียน \"จำ — DDx\" ที่ isolated ALP · GGT ไม่มีในกระดูก (NOT found in bone disease)",
     "src": "หลักจำทั่วไป — แหล่งของ ALP (ตำราชีวเคมีคลินิก)"},
    {"sec": "gi-lft-07", "name": "GC ต้นทาง · DR = Direct", "what": "Hyperbilirubinemia ทางพันธุกรรม 4 โรค",
     "lines": [["G", "**Gilbert** — UGT1A1 ลดลงเล็กน้อย · indirect สูงเวลาอดอาหาร/ป่วย · ไม่ต้องรักษา"],
               ["C", "**Crigler–Najjar** — type I ไม่มี UGT1A1 → kernicterus ในทารก · type II บางส่วน ตอบสนอง phenobarbital"],
               ["D", "**Dubin–Johnson** — MRP2 เสีย ขับ conjugated ออกไม่ได้ → **direct** สูง · **ตับสีดำ**"],
               ["R", "**Rotor** — คล้าย Dubin–Johnson แต่เบากว่า ตับไม่ดำ (เก็บสะสม bilirubin ไม่ได้)"]],
     "note": "สไลด์ 2570 ✍️ ขีดเส้นใต้ Gilbert และ Crigler–Najjar ใน Path A (IB/TB > 0.8)",
     "src": "First Aid for the USMLE Step 1 (Hereditary hyperbilirubinemias) — ตัวย่อ GC/DR เป็นการย่อเพิ่มเพื่อช่วยจำ"},
    {"sec": "gi-lft-12", "name": "Alcoholic — 4 forms", "what": "สเปกตรัมโรคตับจากเหล้า (✍️ ที่อาจารย์เขียนในห้อง)",
     "lines": [["①", "**ไขมันพอก** — transaminitis (✍️) AST นำ GGT สูง · หายได้ถ้าหยุด"],
               ["②", "**Alcoholic hepatitis** — ไข้ เหลือง ตับโตเจ็บ · AST/ALT > 2 · AST < 300–400"],
               ["③", "**พังผืด** — รอบ central vein"],
               ["④", "**ตับแข็ง** (✍️) — 80 g/วัน > 10 ปี (✍️)"]],
     "note": "อาจารย์จดเฉพาะข้อ ① และ ④ · ข้อ ② ③ เติมตามสเปกตรัมมาตรฐาน",
     "src": "สเปกตรัมมาตรฐานในตำราพยาธิวิทยา (Robbins) + ลายมือในห้อง"},
    {"sec": "gi-lft-13", "name": "Vowels hit your bowels", "what": "ไวรัสตับอักเสบที่ติดทางอาหาร/อุจจาระ (fecal–oral)",
     "lines": [["A", "**HAV** — หอยดิบ (เคสสไลด์) · IgM anti-HAV · ไม่เรื้อรัง"],
               ["E", "**HEV** — น้ำ/อาหารปนเปื้อน เนื้อหมูดิบ · IgM anti-HEV (สไลด์ 2570) · รุนแรงในหญิงตั้งครรภ์"]],
     "note": "B C D ติดทางเลือด เพศสัมพันธ์ และแม่สู่ลูก",
     "src": "First Aid for the USMLE Step 1 (Microbiology — Hepatitis viruses)"},
]


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "anims_gi_lft2570.json"
    json.dump({"set": "gi", "items": [dict(i, after=i["after"] or "") for i in ITEMS], "mnem": MNEM},
              open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("anims %d · mnem %d → %s" % (len(ITEMS), len(MNEM), out))
