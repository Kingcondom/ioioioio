# -*- coding: utf-8 -*-
"""ภาพเคลื่อนไหวกลไก (section.anims) + หลักจำ (section.mnem) สำหรับคาบ air 23 "Approach to arthritis"
ตามสไลด์ อ.กิตติวรรณ (Lec 2.1) และราวด์ข้างเตียง 5 พ.ย. 2569 (โน้ต slides/arthritis_notes.md) · update_arthritis.py นำ ITEMS/MNEM ไปใส่

ตรวจ:  python3 artifact/tools/anims_air_arthritis.py <out.json>
       python3 dashboard/anim_tool.py check artifact/data <out.json>      (หลังรัน update_arthritis.py แล้ว)
รูปแบบตาม dashboard/learn_anim/SPEC.md (data-s = โผล่ตั้งแต่ขั้น n · data-x = หายตั้งแต่ขั้น n · fl ไหล · pl กะพริบ)
ข้อความของแต่ละขั้นวางในตำแหน่งใหม่ (ไม่ทับข้อความเก่าที่ซ่อน) ยกเว้นที่ระบุไว้"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg import t, rect, circ, ell, line, ar, path, esc, pill, poly  # noqa: E402


def S(k, *parts, x=None):
    a = ' data-s="%d"' % k + ((' data-x="%d"' % x) if x else "")
    return "<g%s>%s</g>" % (a, "".join(p for p in parts if p))


def G(c, *parts):
    return '<g class="%s">%s</g>' % (c, "".join(p for p in parts if p))


def mover(r, c, dur, d, begin="0s"):
    nums = [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", d)]
    x0, y0 = nums[0], nums[1]
    pts = [(nums[i] - x0, nums[i + 1] - y0) for i in range(0, len(nums), 2)]
    rel = "M0 0 " + " ".join("L%g %g" % p for p in pts[1:])
    return ('<circle cx="%g" cy="%g" r="%s" class="%s"><animateMotion dur="%s" begin="%s" repeatCount="indefinite" path="%s"/></circle>'
            % (x0, y0, r, c, dur, begin, rel))


def SVG(w, h, label, *parts):
    return ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg">' % (w, h, esc(label))
            + "".join(p for p in parts if p) + "</svg>")


def bolt(x, y, c="badf"):
    return path("M%g %g L%g %g L%g %g L%g %g Z" % (x, y, x - 6, y + 10, x + 1, y + 10, x - 4, y + 20), c)


# ═══════════════════════════════════ 1 · active vs passive ROM (I ตัวแรก)
def a_romloc():
    def joint(cx, inflamed):
        return "".join([
            rect(cx - 22, 34, 44, 92, "sk", 12), rect(cx - 22, 144, 44, 92, "sk", 12),
            ell(cx, 135, 42, 30, "lbad w3" if inflamed else "lmu w2"),
        ])
    L, R = 110, 330
    p = [t(L, 18, "ในข้อ (intra-articular)", "mid sm b tbad"), t(R, 18, "นอกข้อ (extra-articular)", "mid sm b tms"),
         joint(L, True), t(L, 182, "synovium/capsule", "mid xs tbad"),
         joint(R, False), path("M%d 40 L%d 230" % (R + 34, R + 34), "lms w5"), t(R + 40, 60, "เอ็น", "xs b tms"),
         circ(R + 30, 150, 9, "ms"), t(R + 44, 170, "bursa", "xs")]
    # ขั้น 2 · active
    p.append(S(2, G("pl", ell(L, 135, 42, 30, "lbad w5")), bolt(L + 52, 92), bolt(R + 50, 92),
               G("pl", path("M%d 40 L%d 230" % (R + 34, R + 34), "lbad w5")),
               t(L, 256, "Active: ผู้ป่วยขยับเอง → เจ็บ", "mid xs b"), t(R, 256, "Active: เอ็นหดตัว → เจ็บ", "mid xs b")))
    # ขั้น 3 · passive
    p.append(S(3, ar(L - 60, 70, L - 40, 52, "ln w2", "ah"), t(L - 60, 86, "หมอขยับให้", "mid xs"),
               ar(R - 60, 70, R - 40, 52, "ln w2", "ah"), t(R - 60, 86, "หมอขยับให้", "mid xs"),
               t(L, 276, "Passive: capsule ยังถูกยืด → เจ็บ", "mid xs b tbad"),
               t(R, 276, "Passive: เอ็นพัก → ไม่ค่อยเจ็บ", "mid xs b tok")))
    # ขั้น 4 · ทิศทาง
    p.append(S(4, ar(L, 130, L, 106, "lbad w2", "ah-bad"), ar(L, 140, L, 164, "lbad w2", "ah-bad"),
               ar(L - 6, 135, L - 34, 135, "lbad w2", "ah-bad"), ar(L + 6, 135, L + 34, 135, "lbad w2", "ah-bad"),
               ar(R + 34, 120, R + 34, 96, "lms w3", "ah-ms"),
               t(L, 296, "เจ็บทุกทิศของ ROM", "mid xs b"), t(R, 296, "เจ็บเฉพาะทิศที่ใช้เอ็นนั้น", "mid xs b")))
    # ขั้น 5 · ตำแหน่งกดเจ็บ + สรุป
    p.append(S(5, t(L, 316, "กดเจ็บไม่ชัด ตามแนวข้อ (ข้อใหญ่อยู่ลึก)", "mid xs"),
               t(R, 316, "กดเจ็บจุดเดียวชัด", "mid xs"),
               rect(10, 332, 420, 56, "sk"),
               t(220, 354, "Intra → เจาะข้อได้ · Extra เช่น cellulitis → ห้ามแทงเข็มผ่าน", "mid xs b"),
               t(220, 374, "(พาเชื้อจากผิวหนังเข้าข้อที่สะอาด = iatrogenic septic arthritis)", "mid xs tbad")))
    return SVG(440, 396, "ภาพเคลื่อนไหว: เทียบรอยโรคในข้อกับนอกข้อ ในข้อเจ็บทั้ง active และ passive ทุกทิศ กดเจ็บไม่ชัด "
               "นอกข้อเจ็บเฉพาะ active ในทิศที่ใช้เอ็นนั้น กดเจ็บเป็นจุด และถ้ารอยโรคอยู่นอกข้อห้ามแทงเข็มผ่าน", *p)


ROMLOC_STEPS = [
    {"t": "I แรก: ปวดในข้อ หรือ นอกข้อ",
     "cap": "ในข้อ = จาก joint capsule เข้าไป (synovium, articular cartilage, subchondral bone) · นอกข้อ = enthesis, bursa, เอ็น, กล้ามเนื้อ, ligament, ผิวหนัง, ไขมันใต้ผิวหนัง — **ต้องแยกก่อนเพราะการรักษาและการเจาะข้อต่างกัน**"},
    {"t": "Active ROM — ผู้ป่วยขยับเอง",
     "cap": "ทั้งสองแบบเจ็บได้: ในข้อ capsule ที่อักเสบถูกยืด · นอกข้อ เอ็น/กล้ามเนื้อที่อักเสบต้องหดตัวทำงาน → active อย่างเดียว **แยกไม่ได้**"},
    {"t": "Passive ROM — หมอขยับให้ ผู้ป่วยอยู่นิ่ง",
     "cap": "**ในข้อยังเจ็บ** เพราะ joint line ยังขยับ capsule ยังถูกยืด · **นอกข้อแทบไม่เจ็บ** เพราะเอ็นที่อักเสบไม่ได้หดตัว — อาจารย์: \"ไม่ต้องจำ ใช้ logic\""},
    {"t": "ทุกทิศ vs บางทิศ",
     "cap": "capsule หุ้มรอบข้อทั้งวง → ขยับทางไหนก็เจ็บ (**all directions**) · เอ็นเส้นหนึ่งทำงานเฉพาะบางทิศ → เจ็บเฉพาะทิศนั้น (**some directions**)"},
    {"t": "ตำแหน่งกดเจ็บ → ตัดสินใจเจาะข้อ",
     "cap": "ในข้อ: จุดเจ็บไม่ชัด อยู่ตามแนวข้อ (ข้อใหญ่อยู่ลึก) · นอกข้อ: จุดเจ็บชัด (well localized) · ✍️ \"เจาะข้อ → R/O septic\" แต่ถ้ารอยโรคอยู่นอกข้อ เช่น **cellulitis ห้ามแทงเข็มผ่าน** เพราะจะพาเชื้อเข้าข้อ"},
]


# ═══════════════════════════════════ 2 · temporal pattern (O)
def a_pattern():
    x0, x1 = 96, 430
    rows = [(26, "Migratory"), (120, "Additive"), (214, "Intermittent"), (308, "Chronic")]
    p = [t(220, 14, "ความรุนแรงของอาการตามเวลา (แกนนอน = เวลา)", "mid xs mu")]
    for y, name in rows:
        base = y + 70
        p += [line(x0, base, x1, base, "lmu da"), t(10, y + 40, name, "sm b")]
    # migratory
    b = 96
    mig = [("M110 %d L130 %d L160 %d L190 %d L215 %d" % (b, b - 54, b - 54, b - 20, b), "lbad w3"),
           ("M180 %d L205 %d L240 %d L265 %d L290 %d" % (b, b - 50, b - 50, b - 18, b), "lwa w3"),
           ("M255 %d L280 %d L320 %d L345 %d L370 %d" % (b, b - 52, b - 52, b - 16, b), "lok w3")]
    p.append(S(2, *[path(d, c) for d, c in mig], t(138, 36, "ข้อ 1", "xs b tbad"), t(218, 40, "ข้อ 2", "xs b twa"),
               t(298, 38, "ข้อ 3", "xs b tok"), t(10, 82, "→ rheumatic fever", "xs tbad")))
    # additive
    b = 190
    p.append(S(3, path("M110 %d L130 %d L430 %d" % (b, b - 30, b - 30), "lbad w3"),
               path("M180 %d L200 %d L430 %d" % (b, b - 46, b - 46), "lwa w3"),
               path("M250 %d L270 %d L430 %d" % (b, b - 62, b - 62), "lok w3"),
               t(150, b - 36, "ข้อ 1", "xs b tbad"), t(215, b - 52, "+ ข้อ 2", "xs b twa"), t(285, b - 68, "+ ข้อ 3", "xs b tok"),
               t(10, 176, "→ RA", "xs tbad")))
    # intermittent
    b = 284
    d = "M100 %d " % b + " ".join("L%d %d L%d %d L%d %d" % (s + 12, b - 56, s + 24, b - 56, s + 60, b) + " L%d %d" % (s + 110, b)
                                  for s in (100, 210, 320))
    p.append(S(4, path(d, "lms w3"), t(260, b + 14, "หายสนิท แตะ baseline ทุกครั้ง", "mid xs b tms"),
               t(10, 270, "→ crystal", "xs tbad"), t(10, 284, "palindromic", "xs tbad")))
    # chronic
    b = 378
    d = "M100 %d L130 %d " % (b, b - 40) + " ".join("L%d %d L%d %d" % (x, b - 22, x + 30, b - 48) for x in range(160, 420, 60))
    p.append(S(5, path(d, "lbad w3"), t(260, b + 14, "มาก–น้อยสลับ แต่ไม่แตะ baseline", "mid xs b tbad"),
               t(10, 364, "≥ 6 สัปดาห์", "xs tbad")))
    p.append(S(6, rect(10, 400, 420, 48, "sk"),
               t(220, 420, "Onset: นาที–ชม. = trauma/crystal · 1–2 วัน = septic", "mid xs b"),
               t(220, 438, "สัปดาห์–เดือน (insidious) = RA OA CTD", "mid xs")))
    return SVG(440, 456, "ภาพเคลื่อนไหว: กราฟความรุนแรงตามเวลาสี่แบบ migratory ข้อเก่าหายแล้วย้ายไปข้อใหม่ additive ข้อใหม่เพิ่มโดยข้อเก่ายังปวด "
               "intermittent กำเริบแล้วหายสนิทแตะ baseline และ chronic มากน้อยสลับไม่แตะ baseline", *p)


PATTERN_STEPS = [
    {"t": "O: onset และ pattern ของข้ออักเสบ",
     "cap": "นอกจาก acute vs **chronic (≥ 6 สัปดาห์** — จำตาม ACR/EULAR ของ RA) ต้องบอกให้ได้ว่า **วิธีที่ข้อใหม่โผล่มา** เป็นแบบไหน — สไลด์ อ.กิตติวรรณ: migratory · additive · intermittent"},
    {"t": "Migratory — ข้อเก่าดีขึ้นแล้วย้ายไปข้อใหม่",
     "cap": "ข้อเดิมหายหรือดีขึ้นราว **50–80%** ก่อนข้อใหม่เริ่มปวด → คลาสสิกคือ **rheumatic fever** (และระยะแรกของ DGI) — อาจารย์: \"อยากได้คำตอบแบบนี้ ไม่ได้อยากให้แปลคำศัพท์\""},
    {"t": "Additive — ข้อใหม่เพิ่มโดยข้อเก่ายังไม่หาย",
     "cap": "มือซ้าย → อีก 2 วันมือขวา → เข่าซ้าย → เข่าขวา ตอนนี้ปวดพร้อมกัน 4 ข้อ → **RA** (สไลด์: additive, slow progression, wax and wane)"},
    {"t": "Intermittent — กำเริบแล้วหายสนิท",
     "cap": "**ต้องแตะ baseline** (กลับเป็นปกติเลย) ถึงเรียก intermittent → **crystal ทั้งกลุ่ม** (gout, CPPD, BCP) และ **palindromic rheumatism** (ต่อไปอาจกลายเป็น RA หรือ SLE หรือหายไป)"},
    {"t": "Chronic — มาก–น้อยสลับแต่ไม่หายสนิท",
     "cap": "อาการขึ้นลงแต่ไม่เคยกลับสู่ปกติ — ต่างจาก intermittent ตรงนี้ · ระยะเวลา **≥ 6 สัปดาห์** · RA, SpA, SLE, OA, chronic tophaceous gout"},
    {"t": "Onset เร็วแค่ไหน",
     "cap": "**Abrupt (ถึงจุดสูงสุดใน ~1 ชม.)** = trauma, crystal · **Rapid (1–2 วัน)** = septic, acute inflammatory · **Insidious (สัปดาห์–เดือน)** = RA, OA, CTD — จากการนำเสนอเคสเกาต์ 5 พ.ย. และสไลด์ p9"},
]


# ═══════════════════════════════════ 3 · hand map RA vs OA vs PsA (D)
def a_handmap():
    fx = [150, 186, 222, 258]          # index → little
    MCP, PIP, DIP = 248, 188, 140
    p = [rect(136, 240, 140, 96, "sk", 18)]
    for x in fx:
        p.append(rect(x - 13, 112, 26, 140, "sk", 13))
    p.append(path("M138 300 L104 262 L92 220", "lmu w5"))
    p.append(ell(206, 360, 64, 14, "sk"))
    base = []
    for x in fx:
        base += [circ(x, MCP, 7, "bx"), circ(x, PIP, 7, "bx"), circ(x, DIP, 7, "bx")]
    base += [circ(124, 296, 7, "bx"), circ(104, 262, 7, "bx"), circ(93, 222, 7, "bx"), circ(206, 360, 7, "bx")]
    p += base
    p += [t(286, MCP + 4, "MCP", "xs mu"), t(286, PIP + 4, "PIP", "xs mu"), t(286, DIP + 4, "DIP", "xs mu"),
          t(40, 300, "CMC1", "xs mu"), t(206, 392, "wrist", "mid xs mu")]
    # ขั้น 2 · RA
    ra = [circ(x, MCP, 8, "badf") for x in fx] + [circ(x, PIP, 8, "badf") for x in fx] + [circ(206, 360, 8, "badf"), circ(104, 262, 8, "badf")]
    p.append(S(2, G("pl", *ra), *[circ(x, DIP, 8, "lok w3") for x in fx],
               t(330, 40, "RA", "lg b tbad"), t(330, 60, "MCP PIP wrist", "xs b"), t(330, 76, "สมมาตร 2 ข้าง", "xs"),
               t(330, 92, "เว้น DIP (วงเขียว)", "xs tok"), x=3))
    # ขั้น 3 · OA
    oa = [circ(x, DIP, 8, "msf") for x in fx] + [circ(x, PIP, 8, "msf") for x in fx] + [circ(124, 296, 8, "msf")]
    p.append(S(3, G("pl", *oa), *[circ(x, MCP, 8, "lok w3") for x in fx],
               t(330, 132, "OA", "lg b tms"), t(330, 152, "DIP (Heberden)", "xs b"), t(330, 168, "PIP (Bouchard)", "xs"),
               t(330, 184, "CMC1 · เว้น MCP", "xs tok"), x=4))
    # ขั้น 4 · PsA
    p.append(S(4, G("pl", rect(fx[1] - 17, 108, 34, 148, "wa", 16)), circ(fx[3], DIP, 8, "waf"), circ(fx[1], DIP, 8, "waf"),
               t(330, 224, "PsA", "lg b twa"), t(330, 244, "DIP + nail", "xs b"), t(330, 260, "dactylitis ทั้งนิ้ว", "xs"),
               t(330, 276, "ไม่สมมาตร", "xs"), x=5))
    # ขั้น 5 · สรุป
    p.append(S(5, rect(316, 300, 118, 100, "sk"), t(375, 320, "RA เว้น DIP", "mid xs b tbad"),
               t(375, 340, "OA เว้น MCP", "mid xs b tms"), t(375, 360, "PsA เอา DIP", "mid xs b twa"),
               t(375, 384, "RA axial: C1–C2", "mid xs b")))
    return SVG(440, 404, "ภาพเคลื่อนไหว: แผนที่ข้อมือ RA จับ MCP PIP ข้อมือ สมมาตร เว้น DIP · OA จับ DIP PIP และ CMC ที่หนึ่ง เว้น MCP · "
               "psoriatic arthritis จับ DIP และนิ้วบวมทั้งนิ้ว ไม่สมมาตร", *p)


HANDMAP_STEPS = [
    {"t": "D: distribution — ดูว่าข้อไหนโดน ข้อไหนรอด",
     "cap": "สไลด์ p8: **PIP, DIP without MCP → OA · PIP, MCP without DIP → RA** — อาจารย์: \"แต่ละโรคมี distribution ต่างกัน **เอาไปเตรียมเลย**\""},
    {"t": "RA — MCP + PIP + wrist สมมาตร เว้น DIP",
     "cap": "ข้อเล็กปลายมือปลายเท้าสองข้าง (MCP PIP MTP wrist) · **spares DIP** และ **spares spine ยกเว้น C1–C2** · สมมาตร = สองข้างใกล้เคียงกัน ไม่ต้องเท่ากันเป๊ะ (มือข้างถนัดเป็นมากกว่าได้)"},
    {"t": "OA — DIP + PIP + CMC1 เว้น MCP",
     "cap": "ข้อที่รับแรงซ้ำ ๆ: Heberden node (DIP) · Bouchard node (PIP) · ฐานนิ้วโป้ง (CMC1) · **MCP รอด** — ถ้า OA-like ที่ MCP 2–3 ให้นึกถึง hemochromatosis (สไลด์ p11 non-inflammatory polyarthritis)"},
    {"t": "PsA — DIP + dactylitis ไม่สมมาตร",
     "cap": "SpA ส่วนปลายส่วนใหญ่ mono/oligo **ยกเว้น PsA เป็น poly ได้** จึงต้องดู distribution: DIP + เล็บผิดปกติ + **นิ้วบวมทั้งนิ้ว (sausage digit)** + ไม่สมมาตร"},
    {"t": "สรุปที่ออกสอบ",
     "cap": "**RA เว้น DIP · OA เว้น MCP · PsA เอา DIP** · RA มี axial ที่เดียวคือ **C1–C2 (atlantoaxial subluxation)** — RA ที่ปวดหลังส่วนล่าง ไม่ใช่ RA active ให้คิด **osteoporotic fracture** (✍️)"},
]


# ═══════════════════════════════════ 4 · RA: citrullination → ACPA → cytokine → pannus → erosion
def a_rapath():
    p = []
    bx = [(18, "บุหรี่ · ไวรัส (EBV parvo) · เหงือกอักเสบ", "sk"),
          (78, "PAD: arginine (+) → citrulline (กลาง)", "ms"),
          (138, "APC + HLA-DR4 shared epitope → T cell", "wa"),
          (198, "B cell → ACPA (anti-CCP) + RF", "ac"),
          (258, "macrophage → TNF · IL-1 · IL-6", "bad")]
    # โครงข้อ (ขวา)
    p += [rect(270, 20, 150, 120, "sk", 30), rect(270, 230, 150, 120, "sk", 30),
          rect(282, 128, 126, 14, "bx", 6), rect(282, 228, 126, 14, "bx", 6),
          path("M262 70 Q248 185 262 300", "lmu w3"), path("M428 70 Q442 185 428 300", "lmu w3"),
          t(345, 190, "ช่องข้อ", "mid xs mu"), '<g data-x="5">' + t(345, 370, "ข้อปกติ: synovium บาง", "mid xs mu") + "</g>"]
    p.append(S(1, rect(10, bx[0][0], 236, 40, bx[0][2], 8), t(128, bx[0][0] + 25, bx[0][1], "mid xs b")))
    for k, (y, s, c) in enumerate(bx[1:], start=2):
        p.append(S(k, ar(128, y - 20, 128, y - 2, "ln w2", "ah"), rect(10, y, 236, 40, c, 8), t(128, y + 25, s, "mid xs b")))
    # ขั้น 5 · synovitis + pannus
    p.append(S(5, G("pl", path("M262 80 Q236 185 262 296", "lbad w5"), path("M428 80 Q454 185 428 296", "lbad w5")),
               path("M268 150 Q300 160 300 186 Q300 212 268 222 Z", "bad"),
               path("M422 150 Q390 160 390 186 Q390 212 422 222 Z", "bad"),
               t(345, 168, "pannus", "mid xs b tbad"), ar(246, 278, 262, 250, "lbad w2", "ah-bad"),
               mover(3, "badf", "1.8s", "M246 278 L282 186"), mover(3, "badf", "1.8s", "M246 290 L404 186", "-.9s")))
    # ขั้น 6 · erosion
    p.append(S(6, path("M270 122 L282 112 L290 128 Z", "inkf"), path("M420 238 L408 248 L400 232 Z", "inkf"),
               t(345, 392, "RANKL → osteoclast → erosion", "mid xs b tbad"),
               t(345, 408, "MMP → cartilage บาง → JSN", "mid xs tbad")))
    p.append(S(7, rect(10, 322, 244, 104, "bx"),
               t(132, 340, "ยาตัดวงจรตรงไหน", "mid xs b"),
               t(18, 358, "csDMARD (MTX SSZ HCQ LEF) ทั้งระบบ", "xs"),
               t(18, 374, "rituximab (CD20) · abatacept (T cell)", "xs"),
               t(18, 390, "anti-TNF · tocilizumab (IL-6R)", "xs"),
               t(18, 406, "JAK inh. ตัดสัญญาณ cytokine ในเซลล์", "xs")))
    return SVG(440, 430, "ภาพเคลื่อนไหว: กลไก RA จากบุหรี่และไวรัส เอนไซม์ PAD เปลี่ยน arginine เป็น citrulline APC ที่มี HLA-DR4 นำเสนอให้ T cell "
               "B cell สร้าง ACPA และ RF macrophage หลั่ง TNF IL-1 IL-6 เยื่อบุข้อหนาเป็น pannus กัดกร่อนกระดูกที่ขอบข้อ และยาแต่ละกลุ่มตัดวงจรตรงไหน", *p)


RAPATH_STEPS = [
    {"t": "ปัจจัยแวดล้อมในคนที่มีพันธุกรรมเสี่ยง",
     "cap": "**smoking** · ไวรัส **EBV parvovirus** · mycoplasma (สไลด์ p58 ✍️ วงทุกตัว) · F:M 2–3:1 · อาจารย์: อายุที่พบบ่อย **40–50 ปี** (แก่กว่า SLE นิดหนึ่ง)"},
    {"t": "Citrullination — โปรตีนตัวเองถูกดัดแปลง",
     "cap": "เอนไซม์ **PAD** เปลี่ยน **arginine (ประจุบวก) → citrulline (เป็นกลาง)** บน filaggrin, vimentin — บุหรี่กระตุ้น · อาจารย์เรียก **epigenetic modification**: ยีนเดิมดี แต่สิ่งแวดล้อมเปลี่ยนโปรตีน"},
    {"t": "HLA class II (HLA-DR4) ยื่นโปรตีนแปลกให้ T cell",
     "cap": "**shared epitope บน HLA-DRB1 (0401) กรดอะมิโน 70–74** จับ peptide ที่มี citrulline ได้ดี → T cell หลุด tolerance · \"**HLA class II, HLA-DR4 — มีสิทธิ์ถาม**\" (อาจารย์)"},
    {"t": "B cell สร้าง ACPA และ RF — ก่อนข้ออักเสบหลายปี",
     "cap": "**ACPA/anti-CCP: sens 77% spec 97%** (✍️ \"เจอแต่ต่ำ จำเพาะสูง\") ทำนาย erosion และการเป็น RA ใน early arthritis · **RF** = Ab ต่อ Fc ของ IgG (75–80% ใน RA แต่พบใน Sjögren SLE ติดเชื้อ ผู้สูงอายุ)"},
    {"t": "Synovitis → synovium หนาเป็น pannus",
     "cap": "immune complex + complement → macrophage หลั่ง **TNF-α, IL-1, IL-6** → synovial hyperplasia + หลอดเลือดงอกใหม่ (hypervascular) → **pannus** (✍️ \"Pannus!\") คลานจากขอบข้อเข้าหากระดูกอ่อน · IL-6 → CRP สูง ซีด อ่อนเพลีย"},
    {"t": "Erosion ที่ขอบข้อ — ย้อนกลับไม่ได้",
     "cap": "**RANKL → osteoclast** กัดกระดูกตรง **bare area** (ขอบข้อที่ไม่มีกระดูกอ่อนคลุม) = marginal erosion · MMP ย่อยกระดูกอ่อน → joint space แคบ **สมมาตร** (ต่างจาก OA ที่แคบเฉพาะฝั่งรับน้ำหนัก)"},
    {"t": "ยาแต่ละกลุ่มตัดวงจรตรงไหน",
     "cap": "MTX (anchor) และ csDMARD กดทั้งระบบ · **rituximab = anti-CD20 (B cell)** · abatacept บล็อก costimulation ของ T cell · **anti-TNF** / tocilizumab (IL-6R) ดัก cytokine · **JAK inhibitor** ตัดสัญญาณภายในเซลล์ — รู้ชื่อ + ผลข้างเคียง ไม่ต้องรู้ขนาดยา"},
]


# ═══════════════════════════════════ 5 · birefringence
def a_biref():
    p = [rect(10, 6, 420, 48, "sk"), ar(120, 42, 320, 42, "ln w3", "ah"), ar(320, 42, 120, 42, "ln w3", "ah"),
         t(220, 24, "แกน slow ray ของ compensator (red plate)", "mid xs b"),
         t(118, 72, "MSU (เกาต์) — เข็ม", "mid sm b"), t(330, 72, "CPPD — rhomboid/แท่ง", "mid sm b"),
         t(8, 124, "ขนาน", "xs b"), t(8, 214, "ตั้งฉาก", "xs b"),
         line(220, 84, 220, 300, "lmu da"), rect(60, 90, 116, 60, "lmu", 6), rect(60, 180, 116, 60, "lmu", 6),
         rect(270, 90, 120, 60, "lmu", 6), rect(270, 180, 120, 60, "lmu", 6)]
    p.append(S(2, G("pl", line(76, 120, 160, 120, "lms w5")), t(118, 168, "เหลือง", "mid xs b tms")))
    p.append(S(3, G("pl", line(118, 186, 118, 234, "lwa w5")), t(118, 258, "ฟ้า", "mid xs b twa"),
               t(118, 282, "= negative birefringence", "mid xs b")))
    p.append(S(4, G("pl", poly([(290, 110), (360, 110), (370, 130), (300, 130)], "waf", closed=True)),
               t(330, 168, "ฟ้า", "mid xs b twa")))
    p.append(S(5, G("pl", poly([(320, 188), (340, 188), (340, 232), (320, 232)], "msf", closed=True)),
               t(330, 258, "เหลือง", "mid xs b tms"), t(330, 282, "= positive (อ่อน)", "mid xs b")))
    p.append(S(6, rect(10, 300, 420, 82, "bx"),
               t(220, 322, "จำอันเดียว: MSU \"ขนานเหลือง ตั้งฉากฟ้า\"", "mid sm b"),
               t(220, 344, "CPPD กลับกัน · ABC = Aligned Blue → Calcium", "mid xs b twa"),
               t(220, 366, "ไม่มี polarized ก็เห็นผลึกเข็มด้วย light microscope ได้", "mid xs")))
    return SVG(440, 390, "ภาพเคลื่อนไหว: ผลึก MSU รูปเข็มวางขนานแกน compensator เป็นสีเหลือง ตั้งฉากเป็นสีฟ้า เรียก negative birefringence "
               "ผลึก CPPD รูป rhomboid ขนานเป็นสีฟ้า ตั้งฉากเป็นสีเหลือง เรียก positive birefringence", *p)


BIREF_STEPS = [
    {"t": "Compensated polarized light — ดูสีเทียบแกน",
     "cap": "พื้นหลังเป็นสีแดงม่วง (first-order red compensator) · สีของผลึกขึ้นกับว่า **แกนยาวของผลึกวางขนานหรือตั้งฉาก** กับแกน slow ray ของ compensator"},
    {"t": "MSU ขนานแกน → เหลือง",
     "cap": "ผลึกเกาต์ = **เข็มยาว ปลายแหลม** เรืองแสงสว่าง (birefringence แรง) · วางขนานแกนเป็น **สีเหลือง**"},
    {"t": "MSU ตั้งฉาก → ฟ้า = negative birefringence",
     "cap": "หมุนผลึกตั้งฉากกับแกน สีกลับเป็นฟ้า · อาจารย์: \"**จำแค่อันเดียวว่า negative = ขนานเหลือง ตั้งฉากฟ้า**\" · ✍️ สไลด์ p40"},
    {"t": "CPPD ขนานแกน → ฟ้า",
     "cap": "ผลึก calcium pyrophosphate = **rhomboid หรือแท่งสั้น** เรืองแสงจาง (birefringence อ่อน หลายผลึกแทบไม่เรือง) · ขนานแกนเป็น **สีฟ้า**"},
    {"t": "CPPD ตั้งฉาก → เหลือง = positive",
     "cap": "ตรงข้ามกับ MSU ทุกอย่าง: รูปร่าง (rhomboid vs เข็ม) · ความสว่าง (อ่อน vs แรง) · สี (ขนานฟ้า vs ขนานเหลือง)"},
    {"t": "สรุป + เคล็ดลับห้องสอบ",
     "cap": "MSU ขนานเหลือง · **ABC = Aligned (ขนาน) Blue → Calcium (CPPD)** · ไม่มี polarized ก็เห็นผลึกเข็มใน light microscope ได้ (อาจารย์) · **เจอผลึกแล้วยังต้องดู Gram stain/culture** — crystal + septic อยู่ข้อเดียวกันได้"},
]


# ═══════════════════════════════════ 6 · เริ่ม ULT แล้วกำเริบ
def a_ultflare():
    X = lambda m: 60 + m * 30           # เดือน 0–12
    Y = lambda u: 300 - (u - 3) * 30    # urate 3–10
    p = [line(60, 300, 430, 300, "ln w2"), line(60, 300, 60, 60, "ln w2"),
         t(20, Y(9.5) + 4, "9.5", "xs"), t(28, Y(6) + 4, "6", "xs b"), t(28, Y(5) + 4, "5", "xs"),
         line(60, Y(6), 430, Y(6), "lok da"), t(428, Y(6) - 6, "เป้า < 6", "end xs b tok"),
         line(60, Y(5), 430, Y(5), "lok dt"), t(428, Y(5) + 14, "< 5 ถ้ามี tophus", "end xs tok"),
         t(245, 336, "เดือนหลังเริ่ม ULT", "mid xs mu"), t(14, 50, "urate (mg/dL)", "xs mu")]
    for m in (0, 3, 6, 9, 12):
        p.append(t(X(m), 316, str(m), "mid xs mu"))
    p.append(path("M60 %g L%g %g" % (Y(9.5), X(1), Y(9.5)), "lbad w3"))
    p.append(S(1, circ(90, 360, 18, "ms"), t(116, 356, "ผลึกสะสมในข้อ/tophus", "xs b"), t(116, 372, "(ระดับสูงคงที่ = สมดุล)", "xs")))
    d = "M%g %g L%g %g L%g %g L%g %g L%g %g L%g %g L%g %g" % (X(1), Y(9.5), X(2), Y(8.3), X(3), Y(7.4), X(4), Y(6.6),
                                                          X(5), Y(5.9), X(6), Y(5.4), X(12), Y(5.0))
    p.append(S(2, path(d, "lwa w3"), t(238, 170, "allopurinol 100 mg", "xs b twa"), t(238, 186, "ปรับทุก 2–5 สัปดาห์", "xs twa")))
    p.append(S(3, G("pl", bolt(X(2), Y(9.6)), bolt(X(3.3), Y(8.9)), bolt(X(4.6), Y(8.4))),
               circ(250, 360, 12, "ms"), circ(272, 352, 3, "msf"), circ(280, 366, 3, "msf"), circ(268, 374, 3, "msf"),
               mover(3, "msf", "2s", "M262 360 L300 340"), t(300, 366, "ผิวผลึกละลาย", "xs b tbad"),
               t(300, 382, "ผลึกเล็กหลุด → flare", "xs tbad")))
    p.append(S(4, rect(X(0) + 4, 64, X(6) - X(0) - 4, 22, "ok", 4), t((X(0) + X(6)) / 2 + 2, 80, "prophylaxis 3–6 เดือน", "mid xs b")))
    p.append(S(5, rect(10, 398, 420, 40, "sk"), t(220, 416, "ULT ใช้ตลอดชีวิต · flare ระหว่างทาง = ห้ามหยุดยา", "mid xs b"),
               t(220, 432, "HLA-B5801 ก่อน allopurinol (คนไทย 6–8%)", "mid xs tbad")))
    return SVG(440, 444, "ภาพเคลื่อนไหว: กราฟกรดยูริกลดลงจาก 9.5 เมื่อเริ่ม allopurinol ขนาดต่ำแล้วปรับขึ้น ช่วงเดือนแรกผิวผลึกที่สะสมละลายหลุดทำให้เกาต์กำเริบ "
               "จึงให้ colchicine ป้องกัน 3 ถึง 6 เดือนจนยูริกถึงเป้าต่ำกว่า 6", *p)


ULTFLARE_STEPS = [
    {"t": "ก่อนเริ่มยา — ผลึกสะสมคงที่",
     "cap": "urate สูงนาน → MSU ตกผลึกสะสมในข้อและ tophus (chronic tophaceous ใช้เวลาเฉลี่ย **11.6 ปี** — สไลด์ p36) · ระดับคงที่ ผลึกอยู่ในสมดุลกับของเหลวรอบ ๆ"},
    {"t": "เริ่ม ULT แบบ start low go slow",
     "cap": "**allopurinol 100 mg/วัน (50 ถ้า GFR ต่ำ) ปรับทุก 2–5 สัปดาห์ สูงสุด 800** (สไลด์ p54) · อาจารย์: เป้า **< 6 \"จำตัวเดียวไปเลย ไม่ขึ้นกับขนาดยา\"** · tophus < 5 ละลายเร็วขึ้น"},
    {"t": "ระดับลด → ผิวผลึกละลาย → flare",
     "cap": "urate ในของเหลวลดเร็ว ผลึกเก่าละลายจากผิว ผลึกเล็ก ๆ หลุดออกจาก tophus/กระดูกอ่อน → macrophage กลืน → **NLRP3 → IL-1β** → กำเริบในช่วงเดือนแรก ๆ (ยิ่งลดเร็วยิ่งกำเริบ)"},
    {"t": "Prophylaxis ช่วงเริ่มยา",
     "cap": "**low-dose colchicine** (หรือ NSAID / prednisolone ขนาดต่ำ) ราว 3–6 เดือน · สไลด์ p49: ลดความถี่และความรุนแรงของ flare **แต่ไม่หยุดการทำลายข้อ** — ที่หยุดการทำลายคือ ULT ถึงเป้า"},
    {"t": "ถึงเป้า — ใช้ตลอดชีวิต",
     "cap": "สไลด์ p52: **therapy should be lifelong** · หยุด ๆ กิน ๆ = flare และเสี่ยง hypersensitivity · **ตรวจ HLA-B5801 ก่อน allopurinol** (AHS 1:1,000 ตาย 20–25%) · มี flare ระหว่างทาง **ห้ามหยุด ULT** รักษา flare ไปพร้อมกัน"},
]


# ═══════════════════════════════════ 7 · enthesitis → new bone (SpA)
def a_enthesis():
    p = [t(110, 16, "Enthesis (เอ็นเสียบเข้ากระดูก)", "mid sm b"), t(330, 16, "กระดูกสันหลัง", "mid sm b"),
         rect(20, 120, 180, 110, "sk", 12), t(110, 216, "กระดูก (calcaneus)", "mid xs mu"),
         path("M60 30 L80 122 M80 30 L96 122 M100 30 L112 122 M120 30 L128 122", "lms w3"),
         path("M80 122 L74 146 M96 122 L94 150 M112 122 L114 148 M128 122 L134 144", "lms w2"),
         t(150, 60, "เอ็นร้อยหวาย", "xs b tms"), t(150, 76, "/plantar fascia", "xs tms")]
    for k, y in enumerate((40, 104, 168, 232)):
        p += [rect(290, y, 80, 46, "sk", 8)]
    p += [rect(300, 86, 60, 18, "wa", 6), rect(300, 150, 60, 18, "wa", 6), rect(300, 214, 60, 18, "wa", 6),
          t(380, 100, "disc", "xs twa")]
    # ขั้น 2 · inflammation
    p.append(S(2, G("pl", circ(104, 128, 22, "lbad w3")), t(110, 248, "IL-23 → IL-17 (HLA-B27)", "mid xs b tbad"),
               t(110, 264, "ปวดส้นเท้า เจ็บตอนก้าวแรกตอนเช้า", "mid xs")))
    # ขั้น 3 · new bone
    p.append(S(3, path("M86 122 L96 98 L112 104 L120 122 Z", "msf"), t(110, 284, "ซ่อมด้วยกระดูกใหม่ (enthesophyte)", "mid xs b tms"),
               t(110, 300, "≠ RA ที่กัดกร่อน (erosion)", "mid xs")))
    # ขั้น 4 · syndesmophyte → bamboo
    br = [path("M292 86 Q284 95 292 104", "lms w3"), path("M368 86 Q376 95 368 104", "lms w3"),
          path("M292 150 Q284 159 292 168", "lms w3"), path("M368 150 Q376 159 368 168", "lms w3"),
          path("M292 214 Q284 223 292 232", "lms w3"), path("M368 214 Q376 223 368 232", "lms w3")]
    p.append(S(4, G("pl", *br), t(330, 300, "syndesmophyte เชื่อมข้อ", "mid xs b tms"), t(330, 316, "→ bamboo spine (AS)", "mid xs b")))
    # ขั้น 5 · dactylitis + สรุป
    p.append(S(5, rect(20, 330, 200, 34, "sk", 17), G("pl", rect(20, 326, 200, 42, "lwa w3", 21)),
               t(120, 351, "dactylitis = นิ้วไส้กรอก", "mid xs b twa"),
               t(120, 384, "synovitis + tenosynovitis + enthesitis", "mid xs"),
               rect(236, 330, 196, 70, "bx"), t(334, 350, "SpA: HLA-B27 · ไม่สมมาตร", "mid xs b"),
               t(334, 368, "ข้อใหญ่ขา · IBP < 45 ปี", "mid xs"), t(334, 386, "RF ANA ลบ (seronegative)", "mid xs")))
    return SVG(440, 404, "ภาพเคลื่อนไหว: เอ็นเสียบเข้ากระดูกเหมือนรากไม้ อักเสบจาก IL-23 IL-17 ในคนที่มี HLA-B27 แล้วซ่อมด้วยกระดูกงอกใหม่ "
               "ที่กระดูกสันหลังเกิด syndesmophyte เชื่อมกันเป็น bamboo spine และนิ้วบวมทั้งนิ้วเป็น dactylitis", *p)


ENTHESIS_STEPS = [
    {"t": "Enthesis = จุดที่เอ็นเสียบเข้ากระดูก",
     "cap": "อาจารย์เปรียบ **\"เหมือนรากต้นไม้ (รากหูกระจง) ที่จิ้มลงดิน\"** — อยู่ **นอกข้อ** · อักเสบตรงนี้ = **enthesitis** → นึกถึง **SNSA** (✍️ เขียน SNSA ไว้ที่ enthesis ในสไลด์ p4)"},
    {"t": "แรงกด + HLA-B27 → IL-23/IL-17",
     "cap": "enthesis รับแรงดึงซ้ำ ๆ → ในคนที่มี **HLA-B27** การตอบสนองต่อความเสียหายเล็ก ๆ ผ่าน **IL-23/IL-17** มากเกิน → ปวดส้นเท้า (Achilles, plantar fascia) โดยเฉพาะก้าวแรกตอนเช้า"},
    {"t": "ซ่อมด้วยกระดูกใหม่ — ตรงข้ามกับ RA",
     "cap": "หลังอักเสบ ร่างกายสร้าง **กระดูกงอกใหม่ (enthesophyte)** แทนการกัดกร่อน — RA = erosion/osteopenia · SpA = **new bone formation** → ข้อแข็งติด"},
    {"t": "กระดูกสันหลัง: syndesmophyte → bamboo spine",
     "cap": "enthesitis ที่ขอบ vertebra + annulus → syndesmophyte เชื่อมข้อต่อกัน → **bamboo spine** (AS) · SI joint ปิดเป็นกระดูก (ภาพสไลด์ p77–78) · ต่างจาก **spondylosis = OA ของ C และ L spine** ซึ่ง non-inflammatory"},
    {"t": "Dactylitis + ภาพรวม SpA",
     "cap": "**นิ้วบวมทั้งนิ้ว** = synovitis + tenosynovitis + enthesitis พร้อมกัน → PsA, ReA, SpA · กลุ่ม SNSA รวมกันเพราะ **HLA-B27 · enthesitis · axial · peripheral ไม่สมมาตร (ตรงข้าม RA) · extra-articular · RF/ANA ลบ** (สไลด์ p76)"},
]


# ═══════════════════════════════════ 8 · ขุ่น ≠ หนืด (น้ำไขข้อ)
def a_visc():
    cols = [(60, "ปกติ", "< 200", "bx"), (165, "ไม่อักเสบ (OA)", "200–2,000", "ms"),
            (275, "อักเสบ", "2,000–50,000", "ms"), (380, "ติดเชื้อ", "> 50,000", "bad")]
    p = [t(220, 16, "หลอดน้ำไขข้อ: ความใส (มองทะลุ) และความหนืด (string test)", "mid xs b")]
    for x, name, wbc, c in cols:
        p += [rect(x - 26, 30, 52, 110, "lmu w2", 10), t(x, 158, name, "mid xs b"), t(x, 174, "WBC " + wbc, "mid xs")]
    # ขั้น 2 · ปกติ: ใส มองทะลุ + string ยาว
    p.append(S(2, t(60, 90, "ABC", "mid sm b"), rect(56, 196, 8, 14, "inkf", 2),
               path("M60 210 L60 270", "lwa w3"), circ(60, 272, 4, "waf"), t(60, 292, "ยืดเป็นเส้นยาว", "mid xs b twa"),
               t(60, 306, "(hyaluronan)", "mid xs")))
    p.append(S(3, t(165, 90, "ABC", "mid sm b"), rect(161, 196, 8, 14, "inkf", 2),
               path("M165 210 L165 252", "lwa w3"), circ(165, 254, 4, "waf"), t(165, 292, "ยังหนืด", "mid xs b twa")))
    # ขั้น 4 · อักเสบ: ขุ่น (WBC) + หยดเป็นหยด
    dots = [circ(275 + dx, 50 + dy, 3, "inkf") for dx, dy in ((-16, 8), (-4, 20), (10, 6), (16, 30), (-12, 44), (2, 58), (14, 70), (-8, 80), (8, 46), (-18, 66))]
    p.append(S(4, t(275, 90, "ABC", "mid sm b"), *dots, rect(271, 196, 8, 14, "inkf", 2),
               circ(275, 222, 4, "waf"), circ(275, 244, 4, "waf"), circ(275, 266, 4, "waf"),
               t(275, 292, "หยดเหมือนน้ำเกลือ", "mid xs b tbad"), t(275, 306, "ขุ่น แต่ไม่หนืด", "mid xs")))
    p.append(S(5, rect(355, 32, 50, 106, "bad", 9), t(380, 90, "หนอง", "mid xs b"), rect(376, 196, 8, 14, "inkf", 2),
               circ(380, 224, 5, "badf"), t(380, 292, "PMN > 75–90%", "mid xs b tbad"), t(380, 306, "→ septic จนพิสูจน์", "mid xs")))
    p.append(S(6, rect(10, 322, 420, 60, "sk"),
               t(220, 344, "ขุ่น = WBC มาก · หนืดลด = เอนไซม์ neutrophil ตัด hyaluronan", "mid xs b"),
               t(220, 366, "เหมือนน้ำมันทอดปลาเค็ม: ดำแต่ใสโจ๋ง ไม่หนืดแล้ว", "mid xs")))
    return SVG(440, 390, "ภาพเคลื่อนไหว: น้ำไขข้อปกติใสมองทะลุและยืดเป็นเส้นยาว ข้อเสื่อมยังใสและหนืด ข้ออักเสบขุ่นจากเม็ดเลือดขาวแต่หยดเหมือนน้ำเกลือ "
               "ติดเชื้อเป็นหนอง ความขุ่นกับความหนืดจึงไม่ไปด้วยกัน", *p)


VISC_STEPS = [
    {"t": "ดู 2 อย่างแยกกัน: clarity กับ viscosity",
     "cap": "สไลด์ p12: color · volume · **clarity (clear → turbid → pus-like)** · **viscosity (increased = syrup / decreased = saline)** — อาจารย์: \"ความขุ่นกับความหนืด **ไม่ไปด้วยกัน อย่าถูกหลอก**\""},
    {"t": "ปกติ: ใส + หนืดมาก",
     "cap": "มองตัวหนังสือผ่านหลอดได้ · **hyaluronic acid** และโปรตีนดี ๆ ทำให้หนืดเหมือน **น้ำเชื่อม/น้ำมันเครื่องใหม่ (ใสและหนืด)** ช่วยหล่อลื่นและรับแรงกระแทก · หยดจากเข็มยืดเป็นเส้นยาว (string sign)"},
    {"t": "Non-inflammatory (OA, trauma): ยังใส ยังหนืด",
     "cap": "WBC **200–2,000** · PMN < 25% · ใสหรือเหลืองอ่อน · **WBC > 2,000 = inflammatory** — เส้นแบ่งที่ต้องจำ (✍️ \"= inflame\")"},
    {"t": "Inflammatory: ขุ่น แต่ความหนืดลด",
     "cap": "WBC **2,000–50,000** ทำให้ขุ่นมองไม่ทะลุ · เอนไซม์และ ROS จาก neutrophil **ตัดโซ่ hyaluronan** → หยดทีละหยด \"**เหมือนน้ำเกลือ**\" — gout, CPPD, RA, ReA"},
    {"t": "Septic: หนอง > 50,000",
     "cap": "WBC **> 50,000** (มัก > 100,000) PMN > 75–90% glucose ต่ำ · อาจารย์: **ยิ่งสูงยิ่งคิด septic** — เคยเป็น crystal มาก่อนแต่ครั้งนี้ WBC 80,000 → **ให้ยาปฏิชีวนะแม้เจอผลึก** และไม่ฉีด steroid"},
    {"t": "สรุปด้วยภาพที่อาจารย์ใช้",
     "cap": "น้ำมันทอดไข่ใหม่ = ใสและหนืด · ทอดปลาเค็มแล้ว = **ดำแต่ใสโจ๋ง ไม่หนืด** → น้ำไขข้ออักเสบ: ขุ่นขึ้นแต่หนืดลง · ตัวเลขที่ต้องจำ: **2,000** (inflam) และ **50,000** (คิด septic)"},
]


# ═══════════════════════════════════ 9 · MSU → NLRP3 → IL-1β
def a_nlrp3():
    p = [ell(140, 170, 120, 100, "sk"), t(140, 66, "macrophage", "mid sm b"),
         poly([(30, 40), (70, 30), (74, 38), (34, 48)], "msf", closed=True), t(52, 24, "MSU", "mid xs b tms"),
         t(140, 290, "เซลล์ในเยื่อบุข้อ", "mid xs mu")]
    p.append(S(2, rect(96, 104, 130, 26, "wa", 8), t(161, 122, "NF-κB → pro-IL-1β", "mid xs b"), t(161, 98, "signal 1", "mid xs b twa"),
               t(268, 96, "(TLR · free fatty acid", "xs"), t(268, 112, "จากงานเลี้ยง/เหล้า)", "xs")))
    p.append(S(3, ar(64, 50, 92, 140, "lms w2", "ah-ms"), circ(110, 168, 18, "ms"),
               poly([(100, 162), (118, 158), (120, 164), (102, 168)], "msf", closed=True),
               G("pl", circ(170, 168, 22, "lbad w3")), t(170, 172, "NLRP3", "mid xs b"),
               t(268, 150, "กลืนผลึก → lysosome แตก", "xs b"), t(268, 166, "→ inflammasome", "xs b"),
               t(268, 182, "→ caspase-1", "xs")))
    p.append(S(4, ar(190, 196, 230, 230, "lbad w3", "ah-bad"), t(236, 246, "IL-1β", "sm b tbad"),
               mover(4, "badf", "1.5s", "M196 200 L280 260"), mover(4, "badf", "1.5s", "M196 200 L280 260", "-.75s"),
               t(300, 236, "หลอดเลือดขยาย รั่ว", "xs"), t(300, 252, "neutrophil เข้าข้อ", "xs"),
               t(300, 268, "ไข้ (pyrogen)", "xs"), t(300, 284, "= ปวด บวม แดง ร้อน", "xs b tbad")))
    p.append(S(5, rect(10, 306, 420, 60, "bx"), t(220, 324, "ยาตัดตรงไหน", "mid xs b"),
               t(220, 342, "colchicine: microtubule → neutrophil เดินไม่ได้ + NLRP3 ประกอบไม่ได้", "mid xs"),
               t(220, 358, "NSAID: prostaglandin · steroid: NF-κB · anakinra: IL-1", "mid xs")))
    p.append(S(6, t(220, 388, "หายเองใน 3–10 วัน: NETs ห่อผลึก + ย่อย cytokine", "mid xs b tok")))
    return SVG(440, 400, "ภาพเคลื่อนไหว: ผลึก MSU ถูก macrophage กลืน lysosome แตก กระตุ้น NLRP3 inflammasome และ caspase-1 ตัด pro-IL-1β เป็น IL-1β "
               "ทำให้หลอดเลือดขยาย neutrophil เข้าข้อ มีไข้ ปวดบวมแดงร้อน และยาแต่ละตัวตัดวงจรตรงไหน", *p)


NLRP3_STEPS = [
    {"t": "MSU ตกผลึกเจอ macrophage ในเยื่อบุข้อ",
     "cap": "urate > ~6.8 mg/dL (จุดอิ่มตัวที่ 37 °C) → ตกผลึก MSU ในข้อเย็น ๆ ปลายเท้า · ผลึกเองยังไม่ทำให้ปวดจนกว่าเซลล์จะถูกกระตุ้น"},
    {"t": "Signal 1 — เตรียม pro-IL-1β",
     "cap": "สัญญาณกระตุ้น (TLR, กรดไขมันอิสระหลังกินเลี้ยง/ดื่มเหล้า) ผ่าน **NF-κB, AP-1, MAPK** → สร้าง **pro-IL-1β** และส่วนประกอบของ NLRP3 รอไว้ (เคสเกาต์ 5 พ.ย. พูดถึง ROS/oxidative stress ด้วย)"},
    {"t": "Signal 2 — กลืนผลึก lysosome แตก → NLRP3",
     "cap": "ผลึกแหลมทำให้ lysosome แตก (+ K⁺ ไหลออก ROS) → ประกอบ **NLRP3 inflammasome** → **caspase-1** ตัด pro-IL-1β เป็น IL-1β ที่ทำงานได้"},
    {"t": "IL-1β → ปวด บวม แดง ร้อน ไข้",
     "cap": "IL-1β ทำให้ **หลอดเลือดขยาย + perivascular permeability** → neutrophil จำนวนมากเข้าข้อ (น้ำไขข้อ inflammatory, PMN สูง) · เป็น pyrogen → **ไข้ + WBC ในเลือดสูงได้โดยไม่ติดเชื้อ** แต่ยังตัด septic ทิ้งไม่ได้"},
    {"t": "ยาช่วงกำเริบตัดวงจรตรงไหน",
     "cap": "**colchicine** จับ tubulin → neutrophil เคลื่อนที่ไม่ได้ + inflammasome ประกอบไม่ได้ (ได้ผลดีถ้าเริ่มใน **36 ชม.**) · NSAID ลด prostaglandin · steroid กด NF-κB · anti-IL-1 (anakinra) ตรงเป้า — **เริ่มรักษาใน 24 ชม.**"},
    {"t": "ทำไมหายเองได้",
     "cap": "neutrophil ที่ตายปล่อย **NETs** ห่อผลึกเป็นก้อนและย่อย cytokine → หายเองใน 3–10 วัน (สไลด์: spontaneous recovery ชม.–สัปดาห์ หายสนิท = intermittent) · แต่ผลึกยังอยู่ (สไลด์ p46) → ต้องลด urate จึงจะไม่กลับมา"},
]


# ═══════════════════════════════════ ตำแหน่ง (sec + after) · หัวข้อใหม่ใส่ marker เองใน md → after = None
ITEMS = [
    {"sec": "air-23-art-01", "after": None,
     "anim": {"key": "art-romloc", "title": "Active vs passive ROM — บอกได้ว่าปวดในข้อหรือนอกข้อ", "svg": a_romloc(), "steps": ROMLOC_STEPS}},
    {"sec": "air-23-art-01", "after": None,
     "anim": {"key": "art-pattern", "title": "Migratory · additive · intermittent · chronic — ข้อใหม่โผล่มาอย่างไร", "svg": a_pattern(), "steps": PATTERN_STEPS}},
    {"sec": "air-23-art-02", "after": None,
     "anim": {"key": "art-handmap", "title": "แผนที่ข้อมือ — RA เว้น DIP · OA เว้น MCP · PsA เอา DIP", "svg": a_handmap(), "steps": HANDMAP_STEPS}},
    {"sec": "air-23-art-05", "after": None,
     "anim": {"key": "art-rapath", "title": "RA — citrullination → ACPA → cytokine → pannus → erosion", "svg": a_rapath(), "steps": RAPATH_STEPS}},
    {"sec": "air-23-art-04", "after": None,
     "anim": {"key": "art-biref", "title": "Birefringence — ขนานเหลือง (MSU) vs ขนานฟ้า (CPPD)", "svg": a_biref(), "steps": BIREF_STEPS}},
    {"sec": "air-23-03", "after": "หลักการใช้ยา",
     "anim": {"key": "art-ultflare", "title": "เริ่มยาลดกรดยูริกแล้วทำไมกำเริบ — และ prophylaxis", "svg": a_ultflare(), "steps": ULTFLARE_STEPS}},
    {"sec": "air-23-art-07", "after": None,
     "anim": {"key": "art-enthesis", "title": "Enthesitis → กระดูกงอกใหม่ → bamboo spine และ dactylitis", "svg": a_enthesis(), "steps": ENTHESIS_STEPS}},
    {"sec": "air-23-01", "after": "การเจาะน้ำไขข้อ (arthrocentesis)",
     "anim": {"key": "art-visc", "title": "น้ำไขข้อ: ขุ่นไม่เท่ากับหนืด — ทำไมข้ออักเสบขุ่นแต่ใสเหมือนน้ำเกลือ", "svg": a_visc(), "steps": VISC_STEPS}},
    {"sec": "air-23-02", "after": "กลไก",
     "anim": {"key": "art-nlrp3", "title": "MSU → NLRP3 inflammasome → IL-1β — กลไกของเกาต์กำเริบ", "svg": a_nlrp3(), "steps": NLRP3_STEPS}},
]

MNEM = [
    {"sec": "air-23-art-01", "name": "I-I-N-O-D-E", "what": "กรอบซักประวัติและตรวจร่างกายผู้ป่วยปวดข้อ (เรียงตามลำดับที่ต้องตัดสินใจ)",
     "lines": [["I", "**I**ntra- vs extra-articular — เทียบ active กับ passive ROM · ทุกทิศ vs บางทิศ · จุดกดเจ็บ"],
               ["I", "**I**nflammatory vs non-inflammatory — morning stiffness **เป็นนาที** (> 30 vs < 30 · OA 2–5 นาที) · lumpy swelling · constitutional"],
               ["N", "**N**umber — mono 1 · oligo 2–4 · poly ≥ 5"],
               ["O", "**O**nset & pattern — acute vs chronic ≥ 6 สัปดาห์ · migratory · additive · intermittent"],
               ["D", "**D**istribution — สมมาตร · เล็ก/ใหญ่ · peripheral vs axial · RA เว้น DIP (แต่ C1–C2) · OA เว้น MCP"],
               ["E", "**E**xtra-articular — enthesitis dactylitis sacroiliitis · ผิว ตา ลำไส้ ปอด nodule · ไข้ น้ำหนักลด"]],
     "note": "ใช้ตอบ MEQ ได้ทันที: เขียนเป็นข้อ ๆ ตามตัวอักษร · อย่าลืมระบุ **duration** ของ morning stiffness (อาจารย์: \"ถามแล้วได้คะแนนต้องระบุ duration\")",
     "src": "กรอบที่ อ.กิตติวรรณ สรุปในราวด์ 5 พ.ย. 2569 — ตัวย่อตามโน้ตของผู้ใช้ · ลำดับตรงกับสไลด์ Joint pain → Historical features for DDx (p5–p9)"},
    {"sec": "air-23-art-02", "name": "RA spares DIP · OA spares MCP", "what": "แยก RA กับ OA ที่มือด้วยข้อที่ \"รอด\"",
     "lines": [["RA", "**MCP + PIP + wrist** สองข้าง · **เว้น DIP** · spine รอดยกเว้น **C1–C2**"],
               ["OA", "**DIP (Heberden) + PIP (Bouchard) + CMC1** · **เว้น MCP** · spine เสื่อมที่ C และ L"],
               ["PsA", "**DIP** + เล็บ + dactylitis · ไม่สมมาตร"],
               ["ข้อยกเว้น", "OA-like ที่ **MCP 2–3** → hemochromatosis · CPPD ก็จับ MCP ได้"]],
     "note": "สไลด์ p8: PIP, DIP without MCP → OA · PIP, MCP without DIP → RA",
     "src": "หลักจำมาตรฐานในตำรารูมาตอลยี (เช่น Harrison's — distribution of joint involvement)"},
    {"sec": "air-23-art-04", "name": "ABC = Aligned · Blue · Calcium", "what": "สีของผลึกใน compensated polarized light",
     "lines": [["A", "**A**ligned — วางขนานกับแกน compensator"],
               ["B", "**B**lue — ถ้าเป็นสีฟ้าเมื่อขนาน"],
               ["C", "**C**alcium (pyrophosphate) — CPPD · positive birefringence · rhomboid"],
               ["ตรงข้าม", "MSU: ขนาน**เหลือง** ตั้งฉากฟ้า · negative · เข็ม"]],
     "note": "อาจารย์ให้จำอันเดียวคือ MSU \"ขนานเหลือง ตั้งฉากฟ้า = negative\" แล้ว CPPD กลับกันทั้งหมด",
     "src": "Libre Pathology — Crystals in body fluids (\"ABC+ = aligned blue is calcium, positively birefringent\")"},
    {"sec": "air-23-art-07", "name": "PAIR", "what": "โรคในกลุ่ม seronegative spondyloarthritis",
     "lines": [["P", "**P**soriatic arthritis — DIP · dactylitis · เล็บ · เป็น poly ได้"],
               ["A", "**A**nkylosing spondylitis — prototype · bamboo spine · HLA-B27 > 90%"],
               ["I", "**I**BD-associated (enteropathic) — Crohn, UC"],
               ["R", "**R**eactive arthritis — หลังติดเชื้อทางเดินอาหาร/ปัสสาวะ-สืบพันธุ์"]],
     "note": "สไลด์ p75 เพิ่ม **undifferentiated SpA** · HLA-B27: AS > 90% · ReA 85% · IBD 50% · PsA-spondylitis 50% (peripheral 15%)",
     "src": "หลักจำที่ใช้ทั่วไปในการทบทวนรูมาตอลยี (เช่น First Aid for the USMLE Step 1 — Seronegative spondyloarthritis)"},
]


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "anims_air_arthritis.json"
    json.dump({"set": "air", "items": [dict(i, after=i["after"] or "") for i in ITEMS], "mnem": MNEM},
              open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for i in ITEMS:
        print("%-14s %5d chars %d steps" % (i["anim"]["key"], len(i["anim"]["svg"]), len(i["anim"]["steps"])))
    print("anims %d · mnem %d → %s" % (len(ITEMS), len(MNEM), out))
