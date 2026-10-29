# -*- coding: utf-8 -*-
"""ภาพเคลื่อนไหวกลไก (section.anims) + หลักจำ (section.mnem) ของคาบ chest 21 "Image in chest"
build_chestimg.py นำ ITEMS/MNEM ไปใส่ในหัวข้อ · รูปแบบตาม dashboard/learn_anim/SPEC.md
ตรวจ:  python3 anims_chest_img.py <out.json>  แล้ว  python3 ../../dashboard/anim_tool.py check ../data <out.json>
แผนภาพเป็น "ภาพจำลอง" ไม่ใช่ฟิล์มจริง — ใช้สีธีม (สลับโหมดมืดได้) จึงใช้ป้ายบอกว่า "ทึบ = ขาวบนฟิล์ม" แทนการระบายดำ/ขาว"""
import json, re, sys
from svg import t, rect, circ, ell, line, ar, path, poly, esc


def S(k, *parts, x=None):
    a = ' data-s="%d"' % k + ((' data-x="%d"' % x) if x else "")
    return "<g%s>%s</g>" % (a, "".join(p for p in parts if p))


def X(k, *parts):
    return '<g data-x="%d">%s</g>' % (k, "".join(p for p in parts if p))


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


# ภาพทรวงอกจำลอง (frontal) — ปอดขวาของผู้ป่วยอยู่ซ้ายมือผู้ดู
RL = "M150 48 C112 58 82 150 70 292 C110 284 145 282 172 284 C160 250 172 190 192 150 L192 72 C182 56 166 46 150 48 Z"
LL = "M290 48 C328 58 358 150 370 292 C345 286 322 283 304 284 C312 240 296 180 250 152 L248 72 C258 56 274 46 290 48 Z"
HEART = "M192 150 C172 190 160 250 172 284 L304 284 C312 240 296 180 250 152 Z"


def chest(dy=0, lc="bx", hc="sk"):
    tr = (' transform="translate(0 %d)"' % dy) if dy else ""
    return ('<g%s>' % tr + path(RL, lc) + path(LL, lc) + path(HEART, hc)
            + rect(192, 26, 56, 126, hc, 4) + rect(212, 22, 16, 108, "bx", 6) + "</g>")


# ───────────────────────── 1 · PA vs AP: ทำไม AP หัวใจโต
def a_paap():
    p = []
    # ป้าย
    p.append(t(110, 22, "PA (ยืน)", "b mid"))
    p.append(t(330, 22, "AP (นอน/portable)", "b mid"))
    p.append(line(220, 30, 220, 300, "lru da"))
    # PA: หลอดรังสีอยู่หลัง (ซ้าย) ฟิล์มชิดหน้าอก (ขวา) · มุมมองจากด้านข้าง
    p.append(circ(22, 160, 9, "ms")); p.append(t(22, 186, "หลอด", "xs mid mu"))
    p.append(rect(176, 70, 10, 180, "inkf", 2)); p.append(t(181, 266, "ฟิล์ม", "xs mid mu"))
    p.append(rect(98, 80, 76, 160, "bx", 30))
    p.append(t(110, 74, "หลัง", "xs mu")); p.append(t(170, 74, "หน้า", "xs mu end"))
    p.append(ell(150, 160, 18, 30, "bad"))
    p.append(t(150, 164, "หัวใจ", "xs mid b"))
    p.append(line(22, 160, 176, 120, "lms fl")); p.append(line(22, 160, 176, 200, "lms fl"))
    p.append(line(22, 160, 176, 126, "lms")); p.append(line(22, 160, 176, 194, "lms"))
    p.append(S(2, rect(186, 124, 8, 72, "badf", 2), t(194, 290, "เงา ≈ ขนาดจริง", "sm mid tok b")))
    # AP: หลอดอยู่หน้า (ขวาสุด) ฟิล์มใต้หลัง (ซ้ายของซีก)
    p.append(circ(418, 160, 9, "ms")); p.append(t(418, 186, "หลอด", "xs mid mu"))
    p.append(rect(234, 70, 10, 180, "inkf", 2)); p.append(t(239, 266, "ฟิล์ม", "xs mid mu"))
    p.append(rect(246, 80, 76, 160, "bx", 30))
    p.append(t(250, 74, "หลัง", "xs mu")); p.append(t(318, 74, "หน้า", "xs mu end"))
    p.append(ell(300, 160, 18, 30, "bad"))
    p.append(t(300, 164, "หัวใจ", "xs mid b"))
    p.append(S(2, line(418, 160, 244, 116, "lms fl"), line(418, 160, 244, 204, "lms fl"),
               rect(226, 116, 8, 88, "badf", 2), t(330, 290, "เงาโตกว่าจริง", "sm mid tbad b")))
    p.append(S(3, rect(20, 306, 400, 84, "ac"),
               t(220, 330, "หัวใจอยู่ชิดผนังหน้าอก", "mid b"),
               t(220, 352, "PA: ใกล้ฟิล์ม → ขยายน้อย · AP: ห่างฟิล์ม + หลอดใกล้", "sm mid"),
               t(220, 374, "→ วัด CTR / ตัดสิน cardiomegaly จาก PA เท่านั้น", "sm mid tac b")))
    return SVG(440, 400, "ภาพเคลื่อนไหว: ท่า PA หัวใจอยู่ใกล้ฟิล์มเงาจึงใกล้ขนาดจริง ท่า AP หัวใจอยู่ห่างฟิล์มและหลอดรังสีอยู่ใกล้ "
               "รังสีที่บานออกทำให้เงาหัวใจโตกว่าจริง จึงตัดสินหัวใจโตจากฟิล์ม PA เท่านั้น", *p)


PAAP_STEPS = [
    {"t": "PA: รังสีเข้าทางหลัง ฟิล์มชิดหน้าอก",
     "cap": "หลอดรังสีอยู่ห่าง ~180 ซม. ด้านหลังผู้ป่วย · ฟิล์มแนบหน้าอก · **หัวใจเป็นอวัยวะด้านหน้า** จึงอยู่ใกล้ฟิล์ม"},
    {"t": "เงาหัวใจ PA ≈ ขนาดจริง · AP โตเกินจริง",
     "cap": "รังสีจากจุดเดียว **บานออก (divergent)** — วัตถุยิ่งห่างฟิล์มและยิ่งใกล้หลอด เงายิ่งขยาย · ท่า AP (portable) หลอดอยู่หน้าในระยะ ~100 ซม. หัวใจห่างฟิล์ม → **ขยาย** ✍️ อาจารย์: \"AP มันเหมือนแว่นขยาย\""},
    {"t": "สรุป: cardiomegaly อ่านใน PA เท่านั้น",
     "cap": "AP supine ยังทำให้ mediastinum กว้าง · scapula ซ้อนปอด · clavicle แนวนอน · ไม่มี air-fluid level ในกระเพาะ (ท่านอน) → **อย่าวินิจฉัยหัวใจโต/mediastinum กว้างจาก AP**"},
]


# ───────────────────────── 2 · Attenuation: ความหนาแน่นและความหนา
def a_atten():
    p = []
    mats = [("Air", "ลม", 22, "bx", 5), ("Fat", "ไขมัน", 58, "wa", 4), ("Water", "soft tissue/น้ำ", 104, "ms", 3),
            ("Bone", "กระดูก", 150, "bad", 2), ("Metal", "โลหะ", 196, "inkf", 0)]
    p.append(t(20, 22, "รังสีเข้า", "sm b mu"))
    p.append(t(430, 22, "ฟิล์ม", "sm b mu end"))
    for i, (en, th, y0, c, n) in enumerate(mats):
        y = 40 + i * 50
        p.append(line(20, y + 16, 150, y + 16, "lms w2"))
        p.append(rect(150, y, 90, 32, c, 4))
        p.append(t(195, y + 21, en, "sm mid b" + (" tpa" if c == "inkf" else "")))
        # รังสีทะลุออก
        for k in range(n):
            p.append(line(240, y + 6 + k * 6, 340, y + 6 + k * 6, "lms fl"))
        p.append(line(352, y + 2, 352, y + 30, "ln w3"))
        p.append(t(362, y + 14, ["ดำ", "ดำจาง", "ขาว", "ขาวจ้า", "ขาวสุด"][i], "sm b"))
        p.append(t(362, y + 28, ["ผ่านมาก", "ผ่านค่อนข้างมาก", "ผ่านน้อยลง", "ผ่านน้อย", "แทบไม่ผ่าน"][i], "xs mu"))
        p.append(t(34, y + 10, th, "xs mu"))
    p.append(S(2, rect(20, 296, 400, 96, "ac"),
               t(34, 318, "ความหนาก็มีผล (density เดียวกัน)", "b"),
               rect(40, 330, 30, 18, "ms", 3), line(70, 339, 120, 339, "lms fl"), line(70, 345, 120, 345, "lms fl"),
               line(70, 333, 120, 333, "lms fl"), t(130, 344, "บาง → รังสีผ่านมาก → เทา", "sm"),
               rect(40, 358, 110, 18, "ms", 3), line(150, 367, 200, 367, "lms fl"), t(210, 372, "หนา → รังสีผ่านน้อย → ขาวกว่า", "sm")))
    p.append(S(3, rect(20, 400, 400, 40, "ok"),
               t(220, 425, "เห็น \"ขอบ\" ได้เฉพาะรอยต่อของ density ต่างกัน", "sm mid b tok")))
    return SVG(440, 450, "ภาพเคลื่อนไหว: รังสีผ่านลม ไขมัน soft tissue กระดูก และโลหะได้ลดลงตามลำดับ ฟิล์มจึงดำไปจนขาว "
               "ความหนาของวัตถุทำให้ทึบขึ้นได้แม้ density เดียวกัน และขอบจะเห็นเฉพาะรอยต่อระหว่าง density ที่ต่างกัน", *p)


ATT_STEPS = [
    {"t": "5 densities: ยิ่ง attenuate มาก ฟิล์มยิ่งขาว",
     "cap": "**Air** (ปอด กระเพาะ) ดำ · **Fat** (ใต้ผิวหนัง) ดำจาง · **Soft tissue/water** (หัวใจ mediastinum กล้ามเนื้อ) ขาว · **Calcium/bone** ขาวจ้า · **Metal** ขาวที่สุด — attenuation = ความสามารถกั้นรังสีไม่ให้ถึงฟิล์ม"},
    {"t": "ความหนาเปลี่ยนความทึบได้",
     "cap": "วัตถุ density เดียวกันแต่หนากว่าจะกั้นรังสีมากกว่า → ทึบกว่า (เช่น เต้านม กล้ามเนื้อ pectoralis · ✍️ ภาพ obesity ทั้งฟิล์มขาว) — ปอดข้างที่ **ไม่มีเงาเต้านม (mastectomy)** จึงดำกว่าอีกข้าง"},
    {"t": "ขอบ = รอยต่อของสอง density",
     "cap": "ขอบหัวใจเห็นได้เพราะ **soft tissue ติดกับลมในปอด** · ถ้าลมถูกแทนด้วยน้ำ/หนอง (density เท่าหัวใจ) ขอบจะหายไป → นี่คือพื้นฐานของ **silhouette sign** และ air bronchogram"},
]


# ───────────────────────── 3 · Silhouette sign
def a_silh():
    p = []
    p.append(chest(dy=0))
    p.append(t(220, 312, "frontal view (จำลอง)", "xs mid mu"))
    p.append(t(20, 340, "ขอบหัวใจขวา", "sm b"))
    p.append(path("M192 150 C172 190 160 250 172 284", "lac w3"))
    p.append(X(2, t(20, 362, "soft tissue ติดลม → เห็นขอบชัด", "sm tok")))
    # ขั้น 2 RML consolidation แตะขอบหัวใจขวา
    p.append(S(2, G("pl", path("M110 200 C140 196 168 200 178 206 C170 236 168 262 172 282 C140 280 112 270 96 250 Z", "bad")),
               t(130, 244, "RML", "sm mid b tbad"),
               t(20, 362, "RML ทึบ (น้ำ/หนอง) แตะหัวใจ → ขอบขวาหาย", "sm tbad b"), x=3))
    p.append(S(2, path("M192 150 C172 190 160 250 172 284", "lbad w3 da"), x=3))
    # ขั้น 3 RLL consolidation อยู่หลัง ไม่แตะหัวใจ
    p.append(S(3, G("pl", path("M76 250 C100 236 140 236 166 250 C164 266 168 276 172 284 C130 280 100 284 70 292 Z", "ms")),
               t(116, 274, "RLL", "sm mid b tms"),
               path("M70 292 C110 284 145 282 172 284", "lbad w3 da"),
               t(20, 362, "RLL อยู่หลัง แตะ diaphragm ไม่แตะหัวใจ", "sm tms b"),
               t(20, 382, "→ ขอบหัวใจยังอยู่ · โดมขวาหาย", "sm tms")))
    p.append(S(4, rect(250, 322, 180, 92, "ac"),
               t(340, 344, "ขอบหายบอกตำแหน่ง", "sm mid b"),
               t(262, 366, "Rt heart = RML", "xs"), t(262, 384, "Rt hemidiaphragm = RLL", "xs"),
               t(262, 402, "Lt heart = lingula", "xs")))
    return SVG(440, 420, "ภาพเคลื่อนไหว silhouette sign: ขอบหัวใจขวาเห็นได้เพราะ soft tissue ติดกับลม เมื่อ RML ทึบแตะหัวใจขอบหายไป "
               "แต่เมื่อ RLL ทึบซึ่งอยู่ด้านหลังขอบหัวใจยังอยู่และโดมกะบังลมขวาหายแทน", *p)


SILH_STEPS = [
    {"t": "ขอบหัวใจเห็นได้เพราะติดกับลม",
     "cap": "หัวใจ (soft tissue) อยู่ติดกับปอดที่เต็มไปด้วยลม → รอยต่อสอง density ต่างกัน → เห็น **ขอบคม**"},
    {"t": "RML ทึบแตะหัวใจ → ขอบขวาหาย",
     "cap": "**RML (medial segment) แนบหัวใจห้องขวา** · เมื่อถุงลมถูกแทนด้วยน้ำ/หนอง density เท่าหัวใจ → ไม่มีรอยต่อ → **ขอบหัวใจขวาหาย (silhouette sign +)** · ใช้ได้กับ consolidation, atelectasis และก้อน"},
    {"t": "RLL ทึบ: หัวใจยังอยู่ แต่โดมขวาหาย",
     "cap": "RLL อยู่ **ด้านหลัง** แนบกะบังลม ไม่แนบหัวใจ → ขอบหัวใจขวายังเห็น ✍️ \"Rt heart ยังอยู่ + silhouette diaphragm\" · lateral: ทึบหลัง major fissure และกระดูกสันหลังส่วนล่างขาวขึ้น"},
    {"t": "สรุป: ขอบไหนหาย = กลีบไหน",
     "cap": "**SVC/right upper mediastinum = RUL · Rt heart = RML · Rt hemidiaphragm = RLL · aortic knob = LUL · Lt heart = lingula · Lt hemidiaphragm/descending aorta = LLL**"},
]


# ───────────────────────── 4 · Air bronchogram
def a_airbr():
    p = []
    p.append(t(20, 22, "หลอดลม + ถุงลม (จำลอง)", "sm b mu"))
    # หลอดลมแตกกิ่ง
    br = "M220 40 L220 120 M220 120 L150 200 M220 120 L290 200 M150 200 L110 280 M150 200 L180 290 M290 200 L260 290 M290 200 L340 280"
    p.append(X(2, path(br, "lru w5")))
    alv = [(x, y) for y in range(150, 330, 26) for x in range(70, 380, 26)]
    for i, (x, y) in enumerate(alv):
        p.append(X(2, circ(x, y, 10, "bx")))
    p.append(X(2, t(20, 360, "ถุงลมมีลม · หลอดลมมีลม → density เดียวกัน", "sm")))
    p.append(X(2, t(20, 380, "ผนังหลอดลมบาง → มองไม่เห็นหลอดลมในปอด", "sm mu")))
    for i, (x, y) in enumerate(alv):
        p.append(S(2, circ(x, y, 10, "bad")))
    p.append(S(2, path(br, "lwa w5")))
    p.append(S(2, t(20, 360, "ถุงลมเต็มน้ำ/หนอง/เลือด/เซลล์ (ขาว)", "sm tbad b"), x=3))
    p.append(S(2, t(20, 380, "หลอดลมยังมีลม → กิ่งดำตัดกับพื้นขาว", "sm"), x=3))
    p.append(S(3, rect(20, 344, 400, 66, "ac"),
               t(30, 366, "air bronchogram = airway เปิด + ถุงลมรอบ ๆ ทึบ", "sm b"),
               t(30, 388, "consolidation · ถ้าไม่มี = หลอดลมอุด (atelectasis/ก้อน)", "sm")))
    return SVG(440, 420, "ภาพเคลื่อนไหว air bronchogram: ปกติหลอดลมและถุงลมมีลมเหมือนกันจึงมองไม่เห็นหลอดลม "
               "เมื่อถุงลมรอบ ๆ เต็มไปด้วยของเหลวแต่หลอดลมยังมีลม กิ่งหลอดลมสีดำจะตัดกับพื้นขาว", *p)


AIRBR_STEPS = [
    {"t": "ปกติ: หลอดลมกลืนไปกับถุงลม",
     "cap": "หลอดลมส่วนปลายมีลม ถุงลมรอบ ๆ ก็มีลม · ผนังหลอดลมบางมาก → ไม่มีรอยต่อ density → **ไม่เห็นหลอดลมในเนื้อปอด**"},
    {"t": "ถุงลมเต็มของเหลว → หลอดลมโผล่",
     "cap": "**Consolidation** = ลมในถุงลมถูกแทนด้วย **fluid, blood, pus, cells** · หลอดลมที่ยังเปิดมีลมอยู่ → เห็นเป็น **กิ่งดำบนพื้นขาว (air bronchogram)** · ปริมาตรปอดไม่ลด (preserved volume)"},
    {"t": "มี/ไม่มี air bronchogram บอกอะไร",
     "cap": "มี → ทางเดินลมเปิด = **consolidation** (pneumonia, edema, hemorrhage) · ไม่มี + ปริมาตรลด → นึกถึง **หลอดลมใหญ่อุด** (resorption atelectasis จากก้อน/เสมหะ) · บน CT ถ้าเห็นหลอดเลือดวิ่งในเนื้อทึบหลังฉีดสี = CT angiogram sign"},
]


# ───────────────────────── 5 · White-out: ดึงหรือดัน
def a_whiteout():
    p = []

    def mini(x0, kind):
        """ซีกซ้ายของกรอบ = ข้างที่ขาว · แถบกลาง = mediastinum · ขวา = ปอดดี · เส้นประ = แนวกลางปกติ"""
        a, m = {"col": (40, 16), "eff": (78, 16), "con": (54, 12)}[kind]  # ความกว้างข้างที่ขาว, ความกว้าง mediastinum
        out = [rect(x0, 40, 130, 170, "bx", 10)]
        out.append(rect(x0 + 4, 46, a, 158, "ms", 8))
        out.append(t(x0 + 4 + a / 2, 130, "ขาว", "xs mid b tms"))
        out.append(rect(x0 + 4 + a, 56, m, 148, "sk", 4))
        out.append(rect(x0 + 4 + a + m, 46, 122 - a - m, 158, "bx", 8))
        tx = x0 + 4 + a + m / 2
        out.append(rect(tx - 4, 30, 8, 56, "wa", 4))
        out.append(line(x0 + 65, 34, x0 + 65, 206, "lmu da"))
        return out, tx
    p.append(t(75, 24, "ปอดยุบทั้งข้าง", "sm mid b"))
    g1, t1 = mini(10, "col"); p += g1
    p.append(t(220, 24, "น้ำท่วมทั้งข้าง", "sm mid b"))
    g2, t2 = mini(155, "eff"); p += g2
    p.append(t(365, 24, "ปอดบวมทั้งข้าง", "sm mid b"))
    g3, t3 = mini(300, "con"); p += g3
    p.append(S(2, ar(75, 100, t1 + 2, 100, "lbad w3", "ah-bad"), t(75, 232, "trachea ถูก \"ดึง\" เข้าหา", "sm mid tbad b"),
               t(75, 250, "ข้างนั้นเล็ก ซี่โครงชิด", "xs mid")))
    p.append(S(3, ar(220, 100, t2 - 2, 100, "lwa w3", "ah-wa"), t(220, 232, "trachea ถูก \"ดัน\" ออก", "sm mid twa b"),
               t(220, 250, "ข้างนั้นใหญ่ ซี่โครงห่าง", "xs mid")))
    p.append(S(4, t(365, 232, "trachea อยู่กลาง", "sm mid tok b"), t(365, 250, "air bronchogram", "xs mid")))
    p.append(S(5, rect(10, 266, 420, 100, "ac"),
               t(22, 290, "อ่าน white-out: ดูก่อนว่า mediastinum ไปทางไหน", "sm b"),
               t(22, 312, "ไปหา → volume ลด: collapse (ก้อนอุดหลอดลม) · pneumonectomy", "sm"),
               t(22, 334, "ผลักหนี → volume เพิ่ม: massive effusion · ก้อนใหญ่", "sm"),
               t(22, 356, "อยู่กลาง → consolidation · effusion + collapse ซ้อนกัน", "sm")))
    return SVG(440, 376, "ภาพเคลื่อนไหว white-out hemithorax: ปอดยุบทั้งข้างดึง trachea เข้าหา น้ำท่วมทั้งข้างดัน trachea ออก "
               "ปอดบวมทั้งข้าง trachea อยู่กลาง ดูทิศของ mediastinum ก่อนเสมอ", *p)


WO_STEPS = [
    {"t": "ซีกหนึ่งขาวทั้งหมด — แยกอย่างไร",
     "cap": "ทั้งสามภาวะทำให้ซีกหนึ่งทึบเหมือนกัน · ตัวแยกคือ **ปริมาตรของซีกนั้น** ซึ่งดูได้จาก trachea, mediastinum, ช่องซี่โครง และโดมกะบังลม"},
    {"t": "Collapse: ดึงเข้าหา",
     "cap": "ก้อน/เสมหะอุดหลอดลมใหญ่ → ลมถูกดูดซึม → ปอด **เล็กลง** → trachea และหัวใจถูก **ดึงเข้าหา** · ซี่โครงชิด โดมยก · มักไม่มี air bronchogram"},
    {"t": "Massive effusion: ดันออก",
     "cap": "น้ำปริมาณมากเพิ่มปริมาตรในซีกนั้น → **ดัน mediastinum ไปฝั่งตรงข้าม** · ✍️ \"Massive PE\" ในสไลด์ซีกซ้ายขาวและ mediastinum ถูกดันไปขวา"},
    {"t": "Consolidation: อยู่กลาง",
     "cap": "ถุงลมเต็มหนองแต่ปริมาตรปอด **เท่าเดิม** → trachea อยู่กลาง · เห็น air bronchogram"},
    {"t": "สรุปการอ่าน",
     "cap": "**ไปหา = volume ลด (collapse, pneumonectomy) · หนี = volume เพิ่ม (effusion, ก้อนใหญ่) · กลาง = consolidation** หรือ effusion + collapse ที่หักล้างกัน (เช่น มะเร็งอุดหลอดลม + น้ำ) → ต้อง CT/ส่องกล้อง"},
]


# ───────────────────────── 6 · Lobar collapse vectors
def a_collapse():
    p = []
    p.append(t(105, 22, "frontal (ปอดขวา)", "sm mid b"))
    p.append(t(335, 22, "lateral (ปอดขวา)", "sm mid b"))
    # frontal: ผนังด้านนอกซ้ายมือ mediastinum ขวามือ · hilum (160,150)
    p.append(path("M110 40 C70 50 40 150 30 280 L172 280 L172 50 C150 36 128 34 110 40 Z", "bx"))
    p.append(X(2, line(44, 150, 160, 150, "lmu da")))
    p.append(X(2, t(48, 144, "minor fissure", "xs mu")))
    p.append(circ(162, 150, 5, "muf"))
    p.append(t(152, 142, "hilum", "xs mu end"))
    # lateral: หน้าซ้ายมือ หลังขวามือ · major fissure (395,64)→(268,280) · minor (250,160)→(338,160)
    p.append(path("M300 40 C262 50 250 150 250 270 L270 280 L420 284 C424 160 392 52 330 38 Z", "bx"))
    p.append(X(4, line(385, 76, 268, 280, "lmu da")))
    p.append(X(2, line(250, 160, 338, 160, "lmu da")))
    p.append(circ(330, 160, 5, "muf"))
    p.append(t(254, 298, "หน้า", "xs mu")); p.append(t(416, 298, "หลัง", "xs mu end"))
    # ขั้น 2 · RUL
    p.append(S(2, path("M110 40 C80 48 60 80 52 112 C90 104 130 96 172 92 L172 50 C150 36 128 34 110 40 Z", "bad"),
               path("M52 112 C90 104 130 96 172 92", "lbad w3"), ar(110, 146, 110, 112, "lbad w2", "ah-bad"),
               path("M300 40 C276 48 262 70 254 110 C280 104 306 92 330 72 C320 54 312 42 300 40 Z", "bad"),
               ar(300, 156, 296, 112, "lbad w2", "ah-bad"),
               t(220, 318, "RUL: minor fissure ยกขึ้น · ยุบขึ้นบน-หน้า-เข้าใน", "sm mid tbad b"), x=3))
    # ขั้น 3 · RML
    p.append(S(3, path("M100 172 L172 158 L172 236 Z", "bad"), path("M44 180 L160 154", "lbad w3"),
               ar(96, 150, 96, 168, "lbad w2", "ah-bad"),
               path("M330 158 L252 196 L256 232 Z", "bad"),
               t(220, 318, "RML: minor fissure ลง · lateral เป็นลิ่มบางยอดที่ hilum", "sm mid tbad b"), x=4))
    # ขั้น 4 · RLL
    p.append(S(4, path("M162 150 L172 280 L104 280 Z", "bad"), ar(60, 214, 106, 252, "lbad w2", "ah-bad"),
               t(40, 200, "ลง-หลัง-ใน", "xs tbad b"),
               path("M336 166 L420 190 L420 284 L362 284 Z", "bad"), line(336, 166, 362, 284, "lbad w2 da"),
               ar(296, 226, 338, 232, "lbad w2", "ah-bad"),
               t(220, 318, "RLL: สามเหลี่ยมยอดที่ hilum · major fissure ไปหลัง", "sm mid tbad b"), x=5))
    p.append(S(5, rect(10, 306, 420, 108, "ac"),
               t(22, 328, "ปอดซ้าย (ไม่มี minor fissure)", "sm b"),
               t(22, 350, "LUL ยุบไป \"หน้า+บน\" → ม่านทึบจาง ๆ ซีกซ้ายบน · Luftsichel", "sm"),
               t(22, 372, "LLL ยุบไป \"ลง+หลัง+ใน\" → สามเหลี่ยมหลังหัวใจ · flat waist", "sm"),
               t(22, 396, "กฎเดียว: กลีบพับเข้าหา hilum ซึ่งเป็นจุดยึด", "sm tac b")))
    return SVG(440, 420, "ภาพเคลื่อนไหว ทิศทางการยุบของแต่ละกลีบ: RUL ยุบขึ้นบนและเข้าใน minor fissure ยกขึ้น RML ทำให้ minor fissure ลง "
               "เป็นลิ่มบางยอดที่ hilum RLL ยุบลงล่างไปหลังและเข้าใน LUL ยุบไปหน้าและบน LLL ยุบลงหลังหัวใจ", *p)


COL_STEPS = [
    {"t": "ปอดขวา: 2 fissures เป็นตัวบอก",
     "cap": "**Minor fissure** แบ่ง RUL/RML (ระดับ anterior 4th rib) · **major fissure** แบ่งกลีบล่างออกจากกลีบบน/กลาง · เมื่อกลีบยุบ fissure จะ **เคลื่อนเข้าหากลีบที่ยุบ** = direct sign"},
    {"t": "RUL: ขึ้นบนและเข้าใน",
     "cap": "minor fissure **ยกขึ้น โค้งขึ้น** · hilum ขวายกสูง ✍️ \"ขึ้นมาพอ ๆ กับ Lt\" · trachea ไปขวา · juxtaphrenic peak · ถ้ามีก้อนที่ hilum → **Golden S**"},
    {"t": "RML: minor fissure ลง",
     "cap": "minor fissure ลง major fissure ส่วนล่างมาข้างหน้า → **ลิ่มบางยอดที่ hilum** บน lateral · frontal: ทึบจาง ๆ **ขอบหัวใจขวาหาย** ✍️ \"triangular shade\""},
    {"t": "RLL: ลง หลัง เข้าใน",
     "cap": "สามเหลี่ยมทึบ **ยอดที่ hilum ฐานที่กะบังลม** · hilum ขวาลง · interlobar PA หาย · โดมขวาหาย แต่ **ขอบหัวใจขวายังเห็น** · lateral: major fissure ไปหลัง"},
    {"t": "ปอดซ้าย: LUL ไปหน้า · LLL ลงหลังหัวใจ",
     "cap": "**LUL** ไม่มี minor fissure จึงยุบไปข้างหน้าเป็นม่านทึบ + **Luftsichel** · **LLL** เป็นสามเหลี่ยมหลังหัวใจ · ✍️ \"loss of retrocardiac space\" · ขอบหัวใจซ้ายแบน (**flat waist**)"},
]


# ───────────────────────── 7 · Golden S sign
def a_golden():
    p = []
    p.append(path("M150 40 C100 50 60 140 50 250 L250 250 L252 50 C220 32 180 30 150 40 Z", "bx"))
    p.append(rect(252, 30, 70, 220, "sk", 6))
    p.append(t(286, 60, "mediastinum", "xs mid mu"))
    p.append(X(2, line(56, 150, 250, 150, "lmu w2 da")))
    p.append(X(2, t(60, 144, "minor fissure ปกติ (แนวนอน)", "xs mu")))
    OP2 = "M150 40 C110 48 82 90 64 150 C120 118 200 116 250 126 L252 50 C220 32 180 30 150 40 Z"
    p.append(S(2, path(OP2, "bad"), path("M64 150 C120 118 200 116 250 126", "lbad w3"),
               ar(110, 176, 110, 136, "lbad w2", "ah-bad"),
               t(60, 200, "RUL ยุบ → fissure ด้านนอกยกขึ้น (เว้า)", "sm tbad b"), x=3))
    EDGE3 = "M64 150 C110 118 150 112 176 124 C192 148 210 172 232 168 C244 164 250 156 250 150"
    p.append(S(3, path("M150 40 C110 48 82 90 64 150 C110 118 150 112 176 124 C192 148 210 172 232 168 C244 164 250 156 250 150 "
                       "L252 50 C220 32 180 30 150 40 Z", "bad"),
               G("pl", ell(214, 140, 30, 24, "ms")), t(214, 144, "ก้อน", "sm mid b tms"),
               path(EDGE3, "lbad w3"),
               t(60, 196, "ด้านในโป่งลงรอบก้อนที่ hilum (นูน)", "sm tms b"),
               t(60, 216, "→ เส้นรูปตัว S กลับด้าน", "sm tms")))
    p.append(S(4, rect(20, 262, 400, 70, "ac"),
               t(30, 286, "Golden S = RUL collapse + hilar mass", "sm b"),
               t(30, 308, "ผู้ใหญ่สูบบุหรี่ → มะเร็งปอดอุดหลอดลมจนกว่าจะพิสูจน์ได้ว่าไม่ใช่", "sm tac")))
    return SVG(440, 340, "ภาพเคลื่อนไหว Golden S sign: minor fissure ปกติแนวนอน เมื่อ RUL ยุบด้านนอกยกขึ้นเว้า "
               "ถ้ามีก้อนที่ hilum ด้านในจะโป่งลงรอบก้อน เกิดเส้นรูปตัว S กลับด้าน บ่งมะเร็งปอดอุดหลอดลม", *p)


GOLD_STEPS = [
    {"t": "Minor fissure ปกติ",
     "cap": "แนวนอนที่ระดับ **anterior 4th rib** แบ่ง RUL กับ RML"},
    {"t": "RUL ยุบ → fissure ยกขึ้นเป็นโค้งเว้า",
     "cap": "กลีบที่ยุบดึง fissure ขึ้นและเข้าหา hilum → ขอบล่างของเงาทึบ **เว้าขึ้น (concave)** ตลอดแนว"},
    {"t": "มีก้อนที่ hilum → ด้านในโป่งลง",
     "cap": "**ก้อนที่ขั้วปอด (hilar mass)** ไม่ยุบตาม → ส่วนในของ fissure ถูกดันโค้งลง (convex) · ส่วนนอกยังเว้า → **reverse S** ✍️ อาจารย์เขียน \"Cancer\""},
    {"t": "แปลผล",
     "cap": "**Golden S sign = RUL atelectasis จากก้อนอุดหลอดลมที่ hilum** — ในผู้ใหญ่ต้องคิดถึง **มะเร็งปอด (มักเป็น squamous cell ที่อยู่ส่วนกลาง)** → CT + bronchoscopy"},
]


# ───────────────────────── 8 · Cavity formation
def a_cavity():
    p = []
    p.append(rect(20, 30, 400, 260, "bx", 12))
    p.append(path("M220 30 L220 116", "lwa w5"))
    p.append(t(228, 50, "หลอดลม", "xs twa"))
    p.append(X(2, G("pl", circ(220, 180, 70, "bad")), t(220, 184, "ก้อน/ปอดอักเสบทึบ", "sm mid b tbad")))
    p.append(X(2, t(30, 312, "เริ่มจากก้อนหรือปอดอักเสบที่ทึบทั้งก้อน", "sm")))
    p.append(S(2, circ(220, 180, 70, "bad"), circ(220, 180, 40, "ms"), t(220, 184, "เนื้อตายตรงกลาง", "xs mid b"),
               t(30, 312, "ขาดเลือด/เอนไซม์จากเชื้อ → necrosis ตรงกลาง", "sm tbad"), x=3))
    PUS = "M178.4 186 L261.6 186 A42 42 0 0 1 178.4 186 Z"
    p.append(S(3, circ(220, 180, 70, "bad"), circ(220, 180, 42, "bx"), path(PUS, "ms"), line(178, 186, 262, 186, "lms w3"),
               path("M220 110 L220 140", "lwa w5"),
               mover(3, "waf", "2.2s", "M220 60 L220 160"),
               t(220, 170, "ลม", "xs mid b twa"), t(220, 206, "หนอง", "xs mid b tms")))
    p.append(S(3, t(30, 312, "เนื้อตายระบายทางหลอดลม → ลมเข้า → air-fluid level", "sm"), x=4))
    p.append(S(4, rect(20, 298, 400, 98, "ac"),
               t(30, 320, "ผนังบาง เรียบ ≤ 3 มม. → cyst/bulla/pneumatocele", "sm"),
               t(30, 342, "ผนังหนา ขรุขระ เป็นปุ่ม → cavity: SCC · TB · abscess", "sm"),
               t(30, 364, "small cell แทบไม่ cavitate · SCC ~80% ของมะเร็งที่ cavitate", "sm tac b"),
               t(30, 386, "air-fluid level เห็นเฉพาะท่ายืน (ลำแสงแนวนอน)", "xs mu")))
    return SVG(440, 404, "ภาพเคลื่อนไหวการเกิดโพรง: ก้อนหรือปอดอักเสบมีเนื้อตายตรงกลาง เมื่อเนื้อตายระบายออกทางหลอดลมลมจะเข้าแทน "
               "เกิดโพรงที่มีระดับลมและน้ำ ผนังหนาขรุขระบ่งมะเร็งหรือฝี", *p)


CAV_STEPS = [
    {"t": "เริ่มจากก้อนหรือปอดอักเสบทึบ",
     "cap": "ก้อนมะเร็ง (โดยเฉพาะ **squamous cell**), ฝีจากเชื้อ (anaerobe, S. aureus, Klebsiella) หรือ **TB** เริ่มเป็นเนื้อทึบ"},
    {"t": "ตรงกลางขาดเลือด → เนื้อตาย",
     "cap": "ก้อนโตเร็วกว่าหลอดเลือด / เอนไซม์จากเชื้อและเม็ดเลือดขาว / caseous necrosis ใน TB → **เนื้อตายเหลวตรงกลาง**"},
    {"t": "ระบายทางหลอดลม → air-fluid level",
     "cap": "เมื่อโพรงทะลุหลอดลม เนื้อตายถูกไอออก **ลมเข้าแทน** → เห็นโพรงดำ + **air-fluid level** (ท่ายืน) · ผู้ป่วยอาจไอเป็นหนองเหม็น (anaerobe) หรือไอเป็นเลือด"},
    {"t": "อ่านผนังโพรง",
     "cap": "**cyst** ผนังเรียบ ≤ 3 มม. · **cavity** ผนังหนาหรือขรุขระ · มะเร็งผนังหนาเป็นปุ่ม · benign มักผนังบางเรียบ · สไลด์: cavitation ~10% ของมะเร็ง ส่วนใหญ่เป็น **SCC (80%)** · small cell แทบไม่เกิด"},
]


# ───────────────────────── 9 · Hyperinflation in emphysema
def a_hyper():
    p = []
    p.append(t(110, 22, "ปกติ", "sm mid b"))
    p.append(t(330, 22, "emphysema", "sm mid b"))
    # normal side: alveoli small many
    for i in range(4):
        for j in range(3):
            p.append(circ(60 + i * 30, 60 + j * 30, 12, "bx"))
    p.append(path("M30 190 Q110 140 190 190", "ln w3"))
    p.append(t(110, 214, "โดมนูน", "xs mid"))
    # emphysema side
    p.append(X(2, G("", *[circ(280 + i * 30, 60 + j * 30, 12, "bx") for i in range(4) for j in range(3)])))
    p.append(X(2, path("M250 190 Q330 140 410 190", "ln w3")))
    p.append(S(2, circ(300, 80, 30, "bx"), circ(370, 74, 26, "bx"), circ(334, 128, 22, "bx"),
               t(330, 172, "ผนังถุงลมถูกทำลาย", "xs mid tbad b"), x=3))
    p.append(S(3, circ(300, 80, 30, "bx"), circ(370, 74, 26, "bx"), circ(334, 128, 22, "bx"),
               path("M250 214 Q330 204 410 214", "lbad w3"), ar(330, 170, 330, 204, "lbad w2", "ah-bad"),
               t(330, 236, "โดมแบน ต่ำ", "xs mid tbad b")))
    p.append(S(3, mover(3, "waf", "1.4s", "M300 40 L300 70"), t(250, 256, "ลมเข้าได้ ออกไม่หมด (air trapping)", "xs")))
    p.append(S(4, rect(20, 270, 400, 112, "ac"),
               t(30, 292, "สิ่งที่เห็นบนฟิล์ม (overinflation)", "sm b"),
               t(30, 314, "โดมขวาต่ำกว่า anterior 7th rib · lung height ≥ 29.9 ซม.", "sm"),
               t(30, 336, "โดมแบน (< 1.5 ซม. PA / < 2.7 ซม. lateral)", "sm"),
               t(30, 358, "retrosternal space ลึก (> 2.5 ซม.) · หลอดเลือดส่วนปลายหาย", "sm"),
               t(30, 376, "หัวใจแคบยาว (ถูกยืดลง)", "xs mu")))
    return SVG(440, 392, "ภาพเคลื่อนไหว emphysema: ผนังถุงลมถูกทำลายจน elastic recoil ลด ลมเข้าได้แต่ออกไม่หมด ปอดพองดันโดมกะบังลมให้แบนต่ำ "
               "เห็นซี่โครงมาก retrosternal space ลึก และหลอดเลือดส่วนปลายหายไป", *p)


HYP_STEPS = [
    {"t": "ปกติ: ถุงลมเล็กจำนวนมาก โดมนูน",
     "cap": "ผนังถุงลมและเส้นใย elastic ช่วยดึงทางเดินลมเล็กให้เปิดตอนหายใจออก และให้ **elastic recoil** ไล่ลมออก"},
    {"t": "ผนังถุงลมถูกทำลาย",
     "cap": "protease จากควันบุหรี่ทำลายผนัง → ถุงลมรวมเป็นช่องใหญ่ (emphysema/bulla) · recoil ลด · ทางเดินลมเล็กยุบตอนหายใจออก"},
    {"t": "Air trapping → ปอดพอง โดมแบน",
     "cap": "ลมค้าง → ปริมาตรปอดเพิ่ม → **กดโดมกะบังลมให้แบนต่ำ** · ปอดโปร่งดำขึ้น (หลอดเลือดส่วนปลายถูกทำลาย = oligemia) ✍️ \"Flat\""},
    {"t": "เกณฑ์บนฟิล์ม",
     "cap": "สไลด์: **lung height ≥ 29.9 ซม.** · โดมขวาสูง **< 1.5 ซม. (PA) / < 2.7 ซม. (lateral)** · **retrosternal air space > 2.5 ซม.** · โดมขวาต่ำกว่า **anterior 7th rib** · sternodiaphragmatic angle > 90°"},
]


# ───────────────────────── 10 · Mediastinal mass localisation
def a_mediast():
    p = []
    p.append(t(110, 22, "frontal", "sm mid b"))
    p.append(t(333, 22, "lateral", "sm mid b"))
    # frontal ย่อ 0.6 วางในกรอบ x 0–220
    fr = ('<g transform="translate(-22 18) scale(0.6)">' + path(RL, "bx") + path(LL, "bx") + path(HEART, "sk")
          + rect(192, 26, 56, 126, "sk", 4) + rect(212, 22, 16, 108, "bx", 6) + "</g>")
    p.append(fr)

    def F(x, y):  # พิกัดเต็ม → พิกัดย่อ
        return -22 + 0.6 * x, 18 + 0.6 * y
    hx = [F(192, 150), F(172, 190), F(160, 250), F(172, 284)]
    RHB = "M%g %g C%g %g %g %g %g %g" % (hx[0] + hx[1] + hx[2] + hx[3])
    a1, a2 = F(262, 150), F(262, 284)
    p.append(path(RHB, "lac w3"))
    p.append(line(a1[0], a1[1], a2[0], a2[1], "lac w3"))
    p.append(t(F(262, 300)[0], F(262, 300)[1] + 4, "desc. aorta", "xs mid tac"))
    p.append(t(F(150, 300)[0] - 6, F(150, 300)[1] + 4, "ขอบหัวใจขวา", "xs mid tac"))
    # lateral กรอบ x 236–430
    p.append(rect(236, 40, 194, 250, "bx", 14))
    p.append(path("M252 60 C256 140 256 220 252 286", "lmu w2"))
    p.append(t(258, 56, "sternum", "xs mu"))
    p.append(ell(312, 214, 40, 50, "sk")); p.append(t(312, 218, "หัวใจ", "xs mid"))
    p.append(rect(404, 60, 18, 228, "sk", 4)); p.append(t(413, 302, "spine", "xs mid mu"))
    p.append(line(392, 110, 392, 286, "lac w3")); p.append(t(388, 104, "aorta", "xs end tac"))
    # ขั้น 2 ก้อนหน้า
    c = F(176, 190)
    p.append(S(2, G("pl", ell(c[0], c[1], 24, 22, "bad")), path(RHB, "lbad w3 da"),
               G("pl", ell(274, 140, 20, 30, "bad")), t(274, 144, "ก้อน", "xs mid b tbad"),
               t(20, 330, "ก้อนหน้า (anterior) แตะหัวใจ → ขอบหัวใจหาย", "sm tbad b"),
               t(20, 350, "ขอบ descending aorta ยังคม · retrosternal space ทึบ", "sm"), x=3))
    # ขั้น 3 ก้อนหลัง
    c2 = F(262, 228)
    p.append(S(3, G("pl", ell(c2[0], c2[1], 20, 24, "ms")), line(a1[0], a1[1] + 30, a2[0], a2[1], "lms w3 da"),
               G("pl", ell(386, 200, 20, 34, "ms")), t(362, 204, "ก้อน", "xs end b tms"),
               line(392, 166, 392, 236, "lms w3 da"),
               t(20, 330, "ก้อนหลัง (posterior): ขอบหัวใจยังคม", "sm tms b"),
               t(20, 350, "แต่ขอบ descending aorta / paraspinal line หาย", "sm"), x=4))
    p.append(S(4, rect(20, 316, 400, 96, "ac"),
               t(30, 338, "✍️ \"Obscure heart → Ant · silhouette desc. aorta → Post\"", "sm b"),
               t(30, 360, "หน้า: 4T (thymoma teratoma thyroid lymphoma)", "sm"),
               t(30, 382, "กลาง: ต่อมน้ำเหลือง หลอดเลือด · หลัง: neurogenic tumor", "sm"),
               t(30, 402, "ยืนยันด้วย lateral และ CT", "xs mu")))
    return SVG(440, 420, "ภาพเคลื่อนไหวการบอกตำแหน่งก้อนในช่องอก: ก้อนด้านหน้าแตะหัวใจทำให้ขอบหัวใจหาย ก้อนด้านหลังขอบหัวใจยังอยู่ "
               "แต่ขอบ descending aorta และ paraspinal line หาย", *p)


MED_STEPS = [
    {"t": "Silhouette ใช้กับ mediastinum ได้",
     "cap": "หัวใจอยู่หน้า · descending aorta และ paraspinal line อยู่หลัง · ก้อน soft tissue แตะโครงสร้างไหน ขอบโครงสร้างนั้นหาย"},
    {"t": "ก้อนหน้า: ขอบหัวใจหาย",
     "cap": "สไลด์ anterior mediastinal mass ✍️ **\"Obscure heart ด้านขวา → Ant\"** · lateral: retrosternal clear space ทึบ · นึกถึง **4T**"},
    {"t": "ก้อนหลัง: หัวใจยังอยู่ ขอบ aorta หาย",
     "cap": "สไลด์ posterior mediastinal mass ✍️ **\"silhouette descending aorta → Post\"** · ขอบหัวใจยังคม (ก้อนอยู่คนละระนาบ) · ส่วนใหญ่เป็น **neurogenic tumor** · ดูการกร่อนของซี่โครง/กระดูกสันหลัง"},
    {"t": "สรุป",
     "cap": "Felson: anterior = หน้าเส้นตามผนังหน้า trachea + ขอบหลังหัวใจ · posterior = หลังเส้น 1 ซม. หลังขอบหน้า vertebral body · ระหว่างนั้น = middle"},
]


# ───────────────────────── 11 · Pulmonary venous hypertension stages
def a_chf():
    p = []
    p.append(chest(dy=0))
    p.append(rect(20, 310, 400, 26, "sk", 6))
    p.append(t(30, 328, "PCWP", "xs b"))
    p.append(X(2, rect(70, 314, 60, 18, "ok", 4), t(100, 327, "< 12", "xs mid b")))

    def vessels(cls_low, cls_up):
        out = []
        for s in (1, -1):  # ขวาของผู้ป่วย (ซ้ายมือ) s=1
            def X_(x):
                return x if s == 1 else 440 - x
            out.append(line(X_(184), 172, X_(140), 250, cls_low)); out.append(line(X_(180), 176, X_(112), 238, cls_low))
            out.append(line(X_(184), 146, X_(150), 92, cls_up)); out.append(line(X_(180), 148, X_(126), 112, cls_up))
        return out
    p.append(X(2, *vessels("lwa w3", "lwa")))
    p.append(X(2, t(220, 362, "ปกติ (ยืน): หลอดเลือดปอดล่าง > บน (แรงโน้มถ่วง)", "sm mid")))
    p.append(S(2, *vessels("lwa", "lwa w3")))
    p.append(S(2, rect(134, 314, 70, 18, "ms", 4), t(169, 327, "13–18", "xs mid b"),
               t(220, 362, "cephalization: หลอดเลือดกลีบบนโตเท่า/มากกว่าล่าง", "sm mid tms b"), x=3))
    p.append(S(3, *[line(84, y, 100, y, "lbad w2") for y in (232, 244, 256, 268)],
               *[line(340, y, 356, y, "lbad w2") for y in (232, 244, 256, 268)],
               t(92, 222, "Kerley B", "xs mid tbad b"),
               G("pl", ell(176, 160, 14, 24, "ms"), ell(264, 160, 14, 24, "ms")),
               rect(208, 314, 70, 18, "ms", 4), t(243, 327, "18–25", "xs mid b"),
               t(220, 362, "interstitial edema: Kerley B · peribronchial cuffing", "sm mid tbad b"), x=4))
    BW = "M190 112 C150 120 126 170 144 214 C158 240 180 236 190 222 Z"
    BW2 = path(BW, "bad").replace("<path", '<path transform="matrix(-1 0 0 1 440 0)"')
    p.append(S(4, G("pl", path(BW, "bad"), BW2),
               path("M72 292 C100 270 140 270 172 284 L172 292 Z", "wa"), path("M368 292 C340 270 300 270 268 284 L268 292 Z", "wa"),
               rect(282, 314, 76, 18, "bad", 4), t(320, 327, "> 25", "xs mid b")))
    p.append(S(4, t(220, 362, "alveolar edema: bat-wing รอบขั้วปอด + effusion", "sm mid tbad b"), x=5))
    p.append(S(5, rect(20, 348, 400, 66, "ac"),
               t(30, 370, "ABCDE: Alveolar edema · kerley B · Cardiomegaly", "sm b"),
               t(30, 394, "Dilated upper lobe vessels · Effusion", "sm b")))
    return SVG(440, 420, "ภาพเคลื่อนไหวความดันหลอดเลือดดำปอดที่สูงขึ้น: ปกติหลอดเลือดส่วนล่างใหญ่กว่า เมื่อความดันสูงขึ้นเกิด cephalization "
               "ต่อด้วย interstitial edema เห็น Kerley B lines และ alveolar edema รูปปีกค้างคาวกับน้ำในช่องเยื่อหุ้มปอด", *p)


CHF_STEPS = [
    {"t": "ปกติ: ล่างใหญ่กว่าบน",
     "cap": "ในท่ายืนแรงโน้มถ่วงทำให้เลือดไปปอดส่วนล่างมาก → หลอดเลือดกลีบล่างใหญ่กว่ากลีบบน · PCWP ราว < 12 mmHg"},
    {"t": "PCWP ~13–18: cephalization",
     "cap": "ปอดส่วนล่างเริ่มบวมใน interstitium → หลอดเลือดถูกกด/หดตัว เลือดถูกเบนขึ้นกลีบบน → **หลอดเลือดกลีบบนโตเท่าหรือมากกว่ากลีบล่าง** (ดูได้เฉพาะฟิล์มยืน)"},
    {"t": "PCWP ~18–25: interstitial edema",
     "cap": "น้ำซึมเข้า **interlobular septa** (ที่มี pulmonary vein และน้ำเหลืองวิ่ง) → **Kerley B lines** เส้นสั้นแนวนอน ≤ 2 ซม. ที่ขอบปอดล่าง · peribronchial cuffing · hilum พร่า"},
    {"t": "PCWP > 25: alveolar edema",
     "cap": "น้ำล้นเข้าถุงลม → **ทึบรอบขั้วปอดรูปปีกค้างคาว (bat-wing)** + air bronchogram + **pleural effusion** (มักขวาหรือสองข้าง) · ตัวเลขเป็นค่าประมาณตามตำรา — ภาพอาจช้ากว่าความดันได้หลายชั่วโมง"},
    {"t": "จำเป็นชุด ABCDE",
     "cap": "**A**lveolar edema · **B** (Kerley B) lines · **C**ardiomegaly · **D**ilated upper lobe vessels · **E**ffusion — ส่วนนี้ **ไม่อยู่ในสไลด์** อิงตำรารังสีวิทยาทรวงอกมาตรฐาน"},
]


# ───────────────────────── 12 · Pleural effusion: meniscus, subpulmonic, decubitus
def a_effusion():
    p = []
    LUNG = "M150 40 C100 50 60 160 50 300 L250 300 L252 50 C220 32 180 30 150 40 Z"
    p.append(path(LUNG, "bx"))
    p.append(rect(252, 30, 60, 270, "sk", 6))
    p.append(t(282, 50, "mediast.", "xs mid mu"))
    p.append(t(40, 30, "ผนังด้านข้าง", "xs mu"))
    p.append(X(2, path("M50 300 Q150 250 250 300", "ln w3")))
    p.append(X(2, t(60, 330, "ปกติ: CP angle แหลม · ไม่มีน้ำ", "sm")))
    p.append(S(2, path("M56 220 C90 236 150 262 250 268 L250 300 L50 300 Z", "wa"),
               path("M56 220 C90 236 150 262 250 268", "lwa w3"),
               t(60, 330, "meniscus: ขอบบนเว้า สูงด้านข้าง (> 200 มล. บน PA)", "sm twa b"),
               t(60, 350, "recoil ของปอด + น้ำหนักน้ำ → ชั้นน้ำหนาด้านข้าง", "xs"), x=3))
    p.append(S(3, path("M50 300 Q60 222 250 300 Z", "wa"), path("M50 300 Q60 222 250 300", "lwa w3"),
               path("M50 300 Q150 270 250 300", "ln da"), t(246, 292, "โดมจริง", "xs mu end"),
               ar(140, 214, 108, 252, "lbad w2", "ah-bad"), t(110, 206, "ยอดโดมปลอมเลื่อนออกด้านข้าง", "xs tbad b"),
               t(60, 330, "subpulmonic: น้ำใต้ปอด เลียนแบบโดมยกสูง", "sm twa b"),
               t(60, 350, "ซ้าย: gastric bubble ห่างจาก \"โดม\" > 2 ซม.", "xs"), x=4))
    p.append(S(4, rect(20, 14, 400, 290, "bx", 14),
               t(220, 56, "ตะแคงข้างที่มีน้ำลง (lateral decubitus)", "sm mid b"),
               rect(60, 90, 320, 150, "sk", 30), path("M70 112 C150 98 290 98 370 112 L370 190 L70 190 Z", "bx"),
               t(220, 150, "ปอด", "sm mid"),
               rect(64, 192, 312, 44, "wa", 18), t(220, 220, "น้ำอิสระไหลเป็นชั้นตามผนังด้านล่าง", "xs mid b twa"),
               ar(400, 100, 400, 220, "lwa w2", "ah-wa"), t(396, 262, "แรงโน้มถ่วง", "xs end twa"),
               t(60, 330, "น้ำไหล = free fluid · ไม่ไหล = loculated", "sm twa b"),
               t(60, 350, "✍️ loculated มี septa → สงสัย parapneumonic/empyema", "xs")))
    return SVG(440, 360, "ภาพเคลื่อนไหวน้ำในช่องเยื่อหุ้มปอด: meniscus sign ขอบบนเว้าสูงด้านข้าง subpulmonic effusion "
               "ที่ยอดโดมปลอมเลื่อนออกด้านข้าง และท่าตะแคงที่น้ำอิสระไหลเป็นชั้นตามผนังด้านล่าง", *p)


EFF_STEPS = [
    {"t": "ปกติ: costophrenic angle แหลม",
     "cap": "ช่องเยื่อหุ้มปอดมีน้ำเพียง ~10–20 มล. · มุมแหลมคมทั้งบน PA และ lateral"},
    {"t": "Meniscus sign",
     "cap": "น้ำลงที่ต่ำสุดก่อน → **lateral film มุมหลังทื่อเมื่อ > 50 มล.** · **PA เห็น meniscus เมื่อ > 200 มล.** · ขอบบนเว้า **สูงด้านข้าง** เพราะปอดมีแรง recoil ดึงเข้าหา hilum ชั้นน้ำรอบปอดจึงหนาสุดด้านข้างในภาพหน้าตรง · ขอบหัวใจ/โดมหาย"},
    {"t": "Subpulmonic effusion",
     "cap": "น้ำขังใต้ฐานปอดแต่ปอดไม่ยกตัว → เห็น **โดมปลอม (pseudodiaphragm)** ที่ยอดเลื่อนไป **ด้านข้าง** (ปกติยอดอยู่ค่อนกลาง) ✍️ \"ด้าน Lt dome มีน้ำขังอยู่ → (ยอด) เปิดไปทาง lateral\" · ซ้าย: gastric bubble ห่างจากโดม"},
    {"t": "Decubitus: ไหลหรือไม่ไหล",
     "cap": "ตะแคงให้ข้างที่สงสัยอยู่ล่าง (ใช้ลำแสงแนวนอน) → **free fluid ไหลเป็นชั้น** ขอบปอด–น้ำคมชัด · ถ้าไม่ไหล = **loculated** (มี septa → parapneumonic/empyema/TB) · ท่านอนหงาย น้ำกระจายไปหลัง ทั้งซีกจึงขาวจาง ๆ ไม่มี meniscus"},
]


# ───────────────────────── 13 · Pneumothorax and tension
def a_ptx():
    p = []
    # ซีกขวาของผู้ป่วย (ซ้ายมือ) + mediastinum + ซีกซ้าย
    p.append(X(3, rect(20, 30, 220, 270, "bx", 30)))
    p.append(X(3, rect(240, 30, 60, 270, "sk", 6), t(270, 50, "mediast.", "xs mid mu"), rect(300, 30, 120, 270, "bx", 30)))
    LUNG1 = "M40 50 L220 50 L222 280 L36 280 Z"
    p.append(X(2, path(LUNG1, "wa"), t(130, 170, "ปอดเต็มช่อง", "sm mid")))
    for d in ("M222 160 L140 110", "M222 170 L120 190", "M222 180 L150 250", "M140 110 L90 80", "M120 190 L70 210"):
        p.append(X(2, path(d, "lwa")))
    p.append(X(2, t(30, 330, "ปกติ: visceral + parietal pleura แนบกัน (ความดันลบ)", "sm")))
    LUNG2 = "M120 90 C170 78 214 96 226 130 L228 290 C170 298 128 290 108 262 C92 200 96 126 120 90 Z"
    p.append(S(2, path(LUNG2, "wa"), path("M226 130 C214 96 170 78 120 90 C96 126 92 200 108 262", "ln w3"),
               path("M226 170 L170 140", "lwa"), path("M226 180 L150 210", "lwa"),
               t(32, 110, "ไม่มี", "xs mu"), t(32, 124, "ลาย", "xs mu"), t(32, 138, "ปอด", "xs mu"),
               t(104, 76, "visceral pleural line", "xs b"),
               t(30, 330, "ลมเข้าช่องเยื่อหุ้ม → ปอดหดด้วย recoil", "sm twa b"),
               t(30, 350, "เส้นขาวบาง ๆ + ไม่มีลายปอดนอกเส้น", "sm"), x=3))
    # tension: ซีกขวาขยาย mediastinum ถูกดันไปซ้าย
    p.append(S(3, rect(20, 30, 250, 284, "bx", 30), G("pl", rect(270, 30, 50, 270, "sk", 6)),
               t(295, 50, "mediast.", "xs mid mu"), rect(320, 30, 100, 270, "bx", 30),
               path("M216 130 C246 124 266 146 268 180 C266 220 240 236 216 230 C194 216 194 150 216 130 Z", "wa"),
               ar(228, 258, 282, 258, "lbad w3", "ah-bad"),
               path("M24 300 Q130 312 266 300", "lbad w3"), ar(130, 270, 130, 300, "lbad w2", "ah-bad"),
               t(60, 290, "โดมกดต่ำ", "xs tbad b")))
    p.append(S(3, t(30, 336, "ลิ้นทางเดียว: ลมเข้าได้ออกไม่ได้ → ความดันบวก", "sm tbad b"),
               t(30, 356, "mediastinum ถูกดันข้าม · โดมกดต่ำ · venous return ↓", "sm tbad"), x=4))
    p.append(S(4, rect(20, 322, 400, 92, "ac"),
               t(30, 344, "ขนาด (BTS): ระยะปอด–ผนังที่ระดับ hilum > 2 ซม. ≈ 50%", "sm b"),
               t(30, 366, "ท่านอนหงาย: ลมขึ้นด้านหน้า-ล่าง → deep sulcus sign", "sm"),
               t(30, 388, "tension = วินิจฉัยทางคลินิก → needle decompression", "sm tbad b"),
               t(30, 406, "ก่อนถ่ายฟิล์ม", "sm tbad b")))
    return SVG(440, 420, "ภาพเคลื่อนไหว pneumothorax: ลมเข้าช่องเยื่อหุ้มปอดทำให้ปอดหดเห็นเส้น visceral pleura และไม่มีลายปอดนอกเส้น "
               "ใน tension pneumothorax ลมเข้าได้ออกไม่ได้ ความดันดัน mediastinum ไปอีกข้างและกดโดมให้ต่ำลง", *p)


PTX_STEPS = [
    {"t": "ปกติ: เยื่อหุ้มสองชั้นแนบกัน",
     "cap": "ความดันในช่องเยื่อหุ้มปอดเป็นลบ เพราะปอดมี **elastic recoil ดึงเข้า** และผนังอกดึงออก → ปอดเต็มช่อง ลายปอดเห็นถึงขอบ"},
    {"t": "Simple pneumothorax",
     "cap": "ลมเข้าช่องเยื่อหุ้ม → ปอดหดตาม recoil → **visceral pleural line** เส้นขาวบาง + **ไม่มี lung marking นอกเส้น** · ✍️ ระวัง **skin fold** ที่เส้นเลยออกนอกทรวงอกและมีลายปอดต่อเนื่อง"},
    {"t": "Tension: ลิ้นทางเดียว",
     "cap": "ลมเข้าได้ทุกครั้งที่หายใจเข้าแต่ออกไม่ได้ → ความดันบวก → **mediastinum/trachea ถูกดันไปอีกข้าง · โดมกดต่ำ · ช่องซี่โครงกว้าง** · หลอดเลือดดำใหญ่ถูกกด → venous return ลด → ช็อก"},
    {"t": "ขนาดและข้อควรจำ",
     "cap": "สไลด์: **Large > 2 ซม. (≈ 50% ปริมาตร)** วัดระยะระหว่างเยื่อหุ้มที่ระดับ hilum (British) · ท่านอนหงายลมขึ้นด้านหน้า-ล่าง → **deep sulcus sign** · tension เป็น **การวินิจฉัยทางคลินิก** อย่ารอฟิล์ม"},
]


# ───────────────────────── 14 · Silica → silicosis
def a_silica():
    p = []
    p.append(rect(20, 30, 400, 196, "bx", 14))
    p.append(circ(96, 128, 70, "sk")); p.append(t(96, 50, "ถุงลม", "xs mid mu"))
    p.append(mover(3, "inkf", "2s", "M30 40 L80 110"))
    p.append(mover(3, "inkf", "2.4s", "M40 34 L104 120", "-.8s"))
    for x, y in ((80, 150), (110, 160), (70, 120)):
        p.append(X(2, rect(x, y, 6, 6, "inkf", 1)))
    p.append(S(1, t(30, 248, "ฝุ่น crystalline silica เล็กพอเข้าถึงถุงลม", "sm"), x=2))
    p.append(S(2, circ(96, 128, 30, "ac"), rect(86, 120, 6, 6, "inkf", 1), rect(100, 130, 6, 6, "inkf", 1),
               t(96, 176, "macrophage", "xs mid b"), x=3))
    p.append(S(2, t(30, 248, "macrophage กลืนผลึก → lysosome แตก → เซลล์ตาย", "sm"), x=3))
    p.append(S(3, G("pl", circ(96, 128, 30, "bad")), rect(86, 120, 6, 6, "inkf", 1), rect(100, 130, 6, 6, "inkf", 1),
               t(96, 176, "ตาย → ปล่อยผลึกซ้ำ", "xs mid b tbad"),
               ar(130, 112, 190, 92, "lbad w2", "ah-bad"), ar(130, 140, 190, 152, "lbad w2", "ah-bad"),
               t(196, 96, "IL-1 · TNF", "xs b tbad"), t(196, 156, "TGF-β", "xs b tbad"),
               ell(262, 128, 30, 14, "ms"), t(262, 132, "fibroblast", "xs mid b")))
    p.append(S(3, t(30, 248, "cytokine กระตุ้น fibroblast · ผลึกถูกกินซ้ำเป็นวงจร", "sm"), x=4))
    nod = []
    for cx, cy in ((330, 70), (376, 96), (338, 126), (390, 150), (346, 180)):
        nod += [circ(cx, cy, 14, "ms"), circ(cx, cy, 9, "lms"), circ(cx, cy, 4, "lms")]
    p.append(S(4, ar(294, 128, 316, 128, "lms w2", "ah-ms"), *nod, t(362, 212, "silicotic nodule", "xs mid b tms")))
    p.append(S(4, t(30, 248, "collagen เรียงเป็นวงซ้อน → ปุ่มปอดบน + ต่อมน้ำเหลือง hilum", "sm tms b"), x=5))
    p.append(S(5, rect(20, 234, 400, 142, "ac"),
               t(30, 256, "บนฟิล์ม: small rounded opacities ปอดบน", "sm b"),
               t(30, 278, "eggshell calcification ของต่อมน้ำเหลือง hilum", "sm"),
               t(30, 300, "ก้อนรวมกัน > 1 ซม. = PMF (progressive massive fibrosis)", "sm"),
               t(30, 322, "macrophage เสีย → เสี่ยง TB สูง → คัดกรอง TB/LTBI", "sm tbad b"),
               t(30, 344, "ไม่มียารักษาให้หาย → หยุดสัมผัส + ป้องกัน", "sm"),
               t(30, 366, "(ไม่อยู่ในสไลด์ — อิงตำรา/ILO)", "xs mu")))
    return SVG(440, 384, "ภาพเคลื่อนไหว silicosis: ฝุ่นซิลิกาเข้าถุงลม macrophage กลืนแล้วตาย ปล่อยผลึกและ cytokine "
               "กระตุ้น fibroblast สร้างปุ่มพังผืดที่มี collagen เป็นวงซ้อนในปอดบนและต่อมน้ำเหลือง hilum และเสี่ยงวัณโรค", *p)


SIL_STEPS = [
    {"t": "สูดฝุ่นซิลิกา",
     "cap": "อาชีพ: **ตัด ขัด เจียหิน หินสังเคราะห์ (engineered stone) · พ่นทราย (sandblasting) · เหมือง · โรงโม่หิน** · อนุภาคเล็กพอเข้าถึงถุงลม"},
    {"t": "Macrophage กลืนผลึก",
     "cap": "ผลึกทำลายเยื่อ lysosome → กระตุ้น **NLRP3 inflammasome** → เซลล์ตาย"},
    {"t": "วงจรตาย–กินซ้ำ + cytokine",
     "cap": "ผลึกถูกปล่อยออกให้ macrophage ใหม่กินซ้ำ → อักเสบต่อเนื่อง · **IL-1, TNF, TGF-β** กระตุ้น fibroblast"},
    {"t": "Silicotic nodule ปอดบน",
     "cap": "collagen เรียงเป็นวงซ้อน → ปุ่มเล็ก **กระจายปอดบนและหลัง** + ต่อมน้ำเหลือง hilum โต"},
    {"t": "สิ่งที่ต้องจำ",
     "cap": "**eggshell calcification** · PMF · **เสี่ยง TB สูงมาก** (macrophage ทำงานเสีย) → คัดกรอง TB และ latent TB เป็นระยะ · เพิ่มความเสี่ยงมะเร็งปอด และโรค autoimmune · อ่านฟิล์มตาม **ILO classification**"},
]


# ───────────────────────── 15 · Asbestos → pleural plaque, asbestosis, mesothelioma
def a_asbestos():
    p = []
    WALL = "M150 40 C100 50 60 160 50 300"
    p.append(path("M150 40 C100 50 60 160 50 300 L250 300 L252 50 C220 32 180 30 150 40 Z", "bx"))
    p.append(path(WALL, "ln w3"))
    p.append(t(40, 30, "ผนังอก + parietal pleura", "xs mu"))
    p.append(S(1, *[line(150 + k * 16, 64 + k * 34, 166 + k * 16, 86 + k * 34, "ln w2") for k in range(5)],
               mover(2, "inkf", "2.6s", "M200 50 L230 240"),
               t(270, 54, "ใยหินยาว บาง", "xs b"), t(270, 70, "ลงถึงปอดล่างและเยื่อหุ้ม", "xs")))
    p.append(S(2, *[G("pl", rect(x, y, 9, 26, "ms", 3)) for x, y in ((92, 140), (76, 196))],
               path("M66 296 Q150 286 240 296", "lms w5"),
               t(270, 120, "pleural plaque", "sm b tms"), t(270, 136, "parietal pleura · บนโดม", "xs"),
               t(270, 152, "มัก calcify · ไม่ร้าย", "xs")))
    p.append(S(3, *[path("M%d %d l12 -8 l10 10 l12 -6" % (110 + k * 26, 236 + (k % 2) * 14), "lbad w2") for k in range(5)],
               t(270, 200, "asbestosis", "sm b tbad"), t(270, 216, "fibrosis ปอดล่าง subpleural", "xs")))
    MESO = ("M146 46 C126 50 112 60 102 76 C112 86 104 98 92 110 C100 122 92 136 82 150 C92 164 84 180 74 196 "
            "C84 212 76 230 68 246 C78 262 70 280 62 296 L54 300 C60 160 100 50 150 40 Z")
    p.append(S(4, G("pl", path(MESO, "bad")), path("M60 300 C70 280 90 272 120 276 C150 280 200 282 240 290 L250 300 Z", "wa"),
               t(270, 254, "mesothelioma", "sm b tbad"), t(270, 270, "pleura หนาเป็นปุ่มรอบปอด", "xs"),
               t(270, 286, "+ effusion · ระยะแฝง 30–40 ปี", "xs")))
    p.append(S(5, rect(20, 312, 400, 74, "ac"),
               t(30, 334, "ใยหิน: กระเบื้องลอนหลังคา ท่อซีเมนต์ ผ้าเบรก ฉนวน", "sm b"),
               t(30, 356, "plaque = ตัวบ่งชี้การสัมผัส · บุหรี่ × ใยหิน → มะเร็งปอดทวีคูณ", "sm"),
               t(30, 376, "(ไม่อยู่ในสไลด์ — อิงตำรา)", "xs mu")))
    return SVG(440, 392, "ภาพเคลื่อนไหวโรคจากใยหิน: ใยยาวบางไปถึงปอดล่างและเยื่อหุ้มปอด ทำให้เกิด pleural plaque บนโดมและผนังข้าง "
               "asbestosis เป็นพังผืดปอดล่าง และ mesothelioma เยื่อหุ้มหนาเป็นปุ่มกับน้ำในช่องเยื่อหุ้มปอดหลังระยะแฝงหลายสิบปี", *p)


ASB_STEPS = [
    {"t": "ใยหินยาวบาง เคลียร์ไม่ออก",
     "cap": "ใยยาว > 5–10 ไมครอน macrophage กลืนไม่หมด (frustrated phagocytosis) · ใยแทงทะลุไปถึง **ปอดล่าง** และ **เยื่อหุ้มปอด**"},
    {"t": "Pleural plaque",
     "cap": "หนาตัวของ **parietal pleura** เป็นแผ่น มัก **calcify** ที่ **โดมกะบังลม** และผนังด้านข้าง · บอกว่าเคยสัมผัส · ไม่ทำให้เป็นมะเร็งโดยตัวมันเอง"},
    {"t": "Asbestosis",
     "cap": "พังผืดในเนื้อปอดแบบ **reticular ปอดล่าง subpleural** (คล้าย UIP) · restrictive + DLCO ต่ำ · ต้องสัมผัสปริมาณมาก ระยะแฝง > 15–20 ปี"},
    {"t": "Malignant mesothelioma",
     "cap": "**pleural effusion exudate ข้างเดียว + เยื่อหุ้มหนาเป็นปุ่ม** ล้อมรอบปอด · ระยะแฝง 20–40 ปี · cytology มักไม่พอ ต้อง **pleural biopsy (thoracoscopy)**"},
    {"t": "สรุปและการป้องกัน",
     "cap": "**ใยหิน + บุหรี่ → มะเร็งปอดเพิ่มแบบทวีคูณ** · mesothelioma ไม่สัมพันธ์กับบุหรี่ · แหล่งในไทย: **กระเบื้องลอน/แผ่นหลังคา** ท่อซีเมนต์ ผ้าเบรก"},
]


# ───────────────────────── 16 · Occupational asthma peak-flow week
def a_occasthma():
    p = []
    days = ["จ", "อ", "พ", "พฤ", "ศ", "ส", "อา", "จ"]
    x0, y0, w = 50, 40, 360
    p.append(line(x0, y0, x0, 230, "ln")); p.append(line(x0, 230, x0 + w, 230, "ln"))
    p.append(t(20, 34, "PEF", "xs b"))
    for i, d in enumerate(days):
        x = x0 + 20 + i * 46
        p.append(t(x, 248, d, "xs mid"))
    p.append(rect(x0 + 20 + 5 * 46 - 18, y0, 2 * 46 + 6, 190, "ok", 4))
    p.append(t(x0 + 20 + 5.5 * 46, 56, "วันหยุด", "xs mid b tok"))
    # PEF line: drops through week, recovers weekend
    vals = [200, 175, 160, 150, 140, 190, 205, 175]
    pts = [(x0 + 20 + i * 46, 230 - (v - 100) * 1.4) for i, v in enumerate(vals)]
    p.append(S(2, poly(pts, "lbad w3"), *[circ(x, y, 4, "badf") for x, y in pts]))
    p.append(X(2, t(220, 150, "บันทึก PEF วันละ ≥ 4 ครั้ง ทั้งวันทำงานและวันหยุด", "sm mid mu")))
    p.append(S(2, t(60, 278, "แย่ลงตลอดสัปดาห์ทำงาน ดีขึ้นวันหยุด", "sm tbad b"), x=3))
    p.append(S(3, rect(20, 262, 400, 110, "ac"),
               t(30, 284, "Occupational asthma (เช่น แป้งในเบเกอรี่ isocyanate สี)", "sm b"),
               t(30, 306, "ยืนยัน: บันทึก PEF ≥ 4 ครั้ง/วัน ≥ 3 สัปดาห์ ทั้งวันทำงาน–หยุด", "sm"),
               t(30, 328, "รักษาหลัก: หยุดสัมผัสสารก่อโรคให้เร็ว", "sm tac b"),
               t(30, 350, "ทำงานต่อ + ICS อย่างเดียว → โรคถาวรได้", "sm"),
               t(30, 366, "(ไม่อยู่ในสไลด์ — อิงแนวทาง)", "xs mu")))
    return SVG(440, 380, "ภาพเคลื่อนไหวกราฟ peak expiratory flow ตลอดหนึ่งสัปดาห์: ค่าลดลงทุกวันทำงานและฟื้นในวันหยุด "
               "เป็นรูปแบบของ occupational asthma การรักษาหลักคือหยุดสัมผัสสารก่อโรค", *p)


OA_STEPS = [
    {"t": "บันทึก PEF ทุกวัน",
     "cap": "ให้ผู้ป่วยเป่า peak flow ≥ 4 ครั้งต่อวัน อย่างน้อย 3 สัปดาห์ (ทั้งช่วงทำงานและหยุด)"},
    {"t": "ลดลงวันทำงาน ฟื้นวันหยุด",
     "cap": "รูปแบบ **work-related** — อาการเริ่มหลังเข้างานไม่กี่ชั่วโมง แย่ลงตลอดสัปดาห์ ดีขึ้นชัดวันหยุด/ลาพักร้อน · ตัวอย่างสาร: **แป้งสาลี/เอนไซม์ (เบเกอรี่)** isocyanate (สีพ่นรถ) latex"},
    {"t": "การจัดการ",
     "cap": "**หยุดสัมผัสสารก่อโรคให้เร็วที่สุด** (ย้ายงาน/เปลี่ยนกระบวนการ) ร่วมกับยาตามแนวทางหืด · การให้ ICS แล้วทำงานเดิมต่อ ทำให้โรคเรื้อรังและไวมากขึ้น"},
]


ITEMS = [
    {"sec": "chest-img-01", "after": "PA เทียบกับ AP — ทำไมหัวใจดูโตใน AP",
     "anim": {"key": "ci-paap", "title": "PA vs AP — ทำไมเงาหัวใจใน AP โตเกินจริง", "svg": a_paap(), "steps": PAAP_STEPS}},
    {"sec": "chest-img-03", "after": "5 densities บนฟิล์ม",
     "anim": {"key": "ci-atten", "title": "Attenuation — ทำไมลมดำ กระดูกขาว และขอบเกิดจากรอยต่อ", "svg": a_atten(), "steps": ATT_STEPS}},
    {"sec": "chest-img-05", "after": "Air bronchogram — ทำไมหลอดลมโผล่",
     "anim": {"key": "ci-airbr", "title": "Air bronchogram — หลอดลมที่มีลมตัดกับถุงลมที่ทึบ", "svg": a_airbr(), "steps": AIRBR_STEPS}},
    {"sec": "chest-img-06", "after": "Silhouette sign — หลักการ",
     "anim": {"key": "ci-silh", "title": "Silhouette sign — ขอบหายเพราะ density เท่ากัน", "svg": a_silh(), "steps": SILH_STEPS}},
    {"sec": "chest-img-08", "after": "Hemithorax ขาวทั้งข้าง — ดึงหรือดัน",
     "anim": {"key": "ci-whiteout", "title": "White-out hemithorax — trachea ไปทางไหนบอกโรค", "svg": a_whiteout(), "steps": WO_STEPS}},
    {"sec": "chest-img-09", "after": "ทิศทางการยุบของแต่ละกลีบ",
     "anim": {"key": "ci-collapse", "title": "Lobar collapse — แต่ละกลีบยุบไปทางไหน", "svg": a_collapse(), "steps": COL_STEPS}},
    {"sec": "chest-img-09", "after": "Golden S sign",
     "anim": {"key": "ci-golden", "title": "Golden S sign — RUL ยุบรอบก้อนที่ hilum", "svg": a_golden(), "steps": GOLD_STEPS}},
    {"sec": "chest-img-11", "after": "Cavity เกิดได้อย่างไร",
     "anim": {"key": "ci-cavity", "title": "Cavity — จากก้อนทึบสู่โพรงที่มี air-fluid level", "svg": a_cavity(), "steps": CAV_STEPS}},
    {"sec": "chest-img-12", "after": "Emphysema — overinflation",
     "anim": {"key": "ci-hyper", "title": "Emphysema — ทำไมโดมแบนและปอดดำ", "svg": a_hyper(), "steps": HYP_STEPS}},
    {"sec": "chest-img-13", "after": "บอกตำแหน่งก้อนด้วย silhouette",
     "anim": {"key": "ci-mediast", "title": "ก้อนใน mediastinum — หน้าหรือหลัง ดูจากขอบที่หาย", "svg": a_mediast(), "steps": MED_STEPS}},
    {"sec": "chest-img-14", "after": "Heart failure บน CXR (ไม่อยู่ในสไลด์)",
     "anim": {"key": "ci-chf", "title": "ความดันหลอดเลือดดำปอดสูงขึ้น — cephalization ถึง bat-wing", "svg": a_chf(), "steps": CHF_STEPS}},
    {"sec": "chest-img-15", "after": "Meniscus และ subpulmonic — ทำไมเป็นรูปนี้",
     "anim": {"key": "ci-effusion", "title": "Pleural effusion — meniscus, subpulmonic และ decubitus", "svg": a_effusion(), "steps": EFF_STEPS}},
    {"sec": "chest-img-16", "after": "กลไก — visceral pleural line และ tension",
     "anim": {"key": "ci-ptx", "title": "Pneumothorax — ปอดหดตาม recoil และ tension ดัน mediastinum", "svg": a_ptx(), "steps": PTX_STEPS}},
    {"sec": "chest-img-17", "after": "Silicosis",
     "anim": {"key": "ci-silica", "title": "Silicosis — ฝุ่นซิลิกาสู่ปุ่มพังผืดและวัณโรค", "svg": a_silica(), "steps": SIL_STEPS}},
    {"sec": "chest-img-17", "after": "โรคจากใยหิน (asbestos)",
     "anim": {"key": "ci-asbestos", "title": "Asbestos — plaque, asbestosis และ mesothelioma", "svg": a_asbestos(), "steps": ASB_STEPS}},
    {"sec": "chest-img-18", "after": "Occupational asthma",
     "anim": {"key": "ci-occasthma", "title": "Occupational asthma — peak flow ลดวันทำงาน ฟื้นวันหยุด", "svg": a_occasthma(), "steps": OA_STEPS}},
]

MNEM = [
    {"sec": "chest-img-02", "name": "RIPE", "what": "ตรวจคุณภาพฟิล์มก่อนอ่านทุกครั้ง (technical adequacy)",
     "lines": [["R", "**R**otation — medial end ของ clavicle สองข้างห่าง spinous process เท่ากัน"],
               ["I", "**I**nspiration — เห็น posterior rib 9–10 (หรือ anterior rib 6) เหนือโดมขวา"],
               ["P", "**P**rojection — PA หรือ AP (portable/supine) · AP ห้ามตัดสินหัวใจโต"],
               ["E", "**E**xposure — เห็น intervertebral space จาง ๆ หลังเงาหัวใจ"]],
     "note": "สไลด์ อ.พจนี เพิ่ม magnification (AP supine) และ angulation (lordotic/semi-upright) — ทั้งสองข้ออยู่ใต้ P ของหลักจำนี้",
     "src": "หลักจำทั่วไปในการสอนอ่าน CXR (เช่น Radiopaedia, Geeky Medics — chest X-ray interpretation)"},
    {"sec": "chest-img-04", "name": "ABCDE", "what": "อ่าน CXR อย่างเป็นระบบ หลังตรวจชื่อผู้ป่วยและคุณภาพฟิล์ม",
     "lines": [["A", "**A**irway — trachea อยู่กลาง carina หลอดลมใหญ่"],
               ["B", "**B**reathing — ปอดทั้งสาม zone เทียบซ้าย-ขวา · pleura · CP angle"],
               ["C", "**C**ardiac — ขนาด (CTR บน PA) ขอบหัวใจ mediastinum hila"],
               ["D", "**D**iaphragm — ระดับ รูปโดม ลมใต้กะบังลม gastric bubble"],
               ["E", "**E**verything else — กระดูก soft tissue สายและอุปกรณ์ + จุดซ่อน (apex, retrocardiac, ใต้โดม)"]],
     "note": "✍️ อาจารย์ให้ \"มองหาจุดซ่อนเร้น\" (hidden areas) ทุกครั้ง — apices, หลังหัวใจ, ใต้โดม, hila, กระดูกและซี่โครง",
     "src": "หลักจำทั่วไป (เช่น Geeky Medics / Radiology Masterclass — systematic CXR review)"},
    {"sec": "chest-img-07", "name": "SCHARTS", "what": "พังผืด/ปุ่มที่เด่น \"ปอดบน\"",
     "lines": [["S", "**S**arcoidosis"], ["C", "**C**oal worker's pneumoconiosis"],
               ["H", "**H**istiocytosis (Langerhans cell)"], ["A", "**A**nkylosing spondylitis"],
               ["R", "**R**adiation (ตามแนวรังสี มักบนในมะเร็งเต้านม/ศีรษะลำคอ)"], ["T", "**T**uberculosis"],
               ["S", "**S**ilicosis"]],
     "note": "ใช้คู่กับ RASCO (ปอดล่าง) · ปอดบนระบายน้ำเหลืองและเลือดน้อยกว่า ฝุ่นจึงค้างนาน",
     "src": "หลักจำทั่วไปทางรังสีวิทยา (Radiopaedia — upper zone predominant lung disease)"},
    {"sec": "chest-img-07", "name": "RASCO", "what": "พังผืดที่เด่น \"ปอดล่าง\" (reticular ที่ฐาน)",
     "lines": [["R", "**R**heumatoid arthritis"], ["A", "**A**sbestosis"], ["S", "**S**cleroderma (systemic sclerosis)"],
               ["C", "**C**ryptogenic fibrosing alveolitis = IPF"], ["O", "**O**thers — ยา: amiodarone, methotrexate, nitrofurantoin, bleomycin"]],
     "note": "สไลด์ p93: \"decreased lung volumes and irregular reticular opacities at lung bases\" = รูปแบบนี้",
     "src": "หลักจำทั่วไปทางรังสีวิทยา (Radiopaedia — lower zone predominant fibrosis)"},
    {"sec": "chest-img-10", "name": "Sentral S's", "what": "มะเร็งปอดชนิดที่อยู่ \"ตรงกลาง\" (central) — มักทำให้หลอดลมอุด/ยุบ",
     "lines": [["S", "**S**quamous cell — central, **cavitate** บ่อยสุด, hyper**C**alcemia (PTHrP)"],
               ["S", "**S**mall cell — central, ต่อมน้ำเหลือง mediastinum โตเร็ว, SIADH, ACTH, Lambert–Eaton"],
               ["S", "**S**moking — สัมพันธ์สูงสุดทั้งสองชนิด"]],
     "note": "adenocarcinoma มักอยู่ส่วนปลาย (peripheral) และพบในผู้ไม่สูบบุหรี่ได้",
     "src": "First Aid for the USMLE Step 1 (Respiratory — lung cancer: \"Sentral\" squamous and small cell)"},
    {"sec": "chest-img-11", "name": "CAVITY", "what": "สาเหตุของโพรงในปอด",
     "lines": [["C", "**C**ancer — squamous cell (~80% ของมะเร็งที่ cavitate)"],
               ["A", "**A**utoimmune — GPA (Wegener), rheumatoid nodule"],
               ["V", "**V**ascular — septic emboli, pulmonary infarct"],
               ["I", "**I**nfection — TB, lung abscess (anaerobe), S. aureus, Klebsiella, fungus"],
               ["T", "**T**rauma — pneumatocele, laceration"],
               ["Y", "**Y**oung (congenital) — CPAM, sequestration, bronchogenic cyst"]],
     "note": "ผนังหนา ขรุขระ เป็นปุ่ม → มะเร็ง/ฝี · ผนังบางเรียบ → cyst, bulla, pneumatocele",
     "src": "Radiopaedia — cavitating pulmonary lesions (mnemonic CAVITY)"},
    {"sec": "chest-img-13", "name": "4 T's", "what": "ก้อนใน anterior mediastinum",
     "lines": [["T", "**T**hymoma (ร่วมกับ myasthenia gravis)"], ["T", "**T**eratoma / germ cell tumor (ชายหนุ่ม)"],
               ["T", "**T**hyroid — retrosternal goitre (ต่อจากคอ)"], ["T", "\"**T**errible\" lymphoma"]],
     "note": "ก้อนหน้าทำให้ขอบหัวใจหาย และลามขึ้นคอได้ (cervicothoracic sign) · ✍️ \"Obscure heart → Ant\"",
     "src": "หลักจำทั่วไป (First Aid / ตำรารังสีวิทยาทรวงอก — anterior mediastinal mass)"},
    {"sec": "chest-img-14", "name": "ABCDE (heart failure)", "what": "สิ่งที่หาใน CXR ของภาวะหัวใจล้มเหลว",
     "lines": [["A", "**A**lveolar edema — bat-wing รอบขั้วปอด"], ["B", "Kerley **B** lines — interlobular septa บวม"],
               ["C", "**C**ardiomegaly — CTR > 0.5 บน PA"], ["D", "**D**ilated upper lobe vessels — cephalization"],
               ["E", "pleural **E**ffusion — มักสองข้างหรือขวา"]],
     "note": "ส่วนนี้ไม่อยู่ในสไลด์ อ.พจนี (สไลด์มีเฉพาะ CTR) — เพิ่มเพราะเป็นภาพที่พบบ่อยที่สุดในวอร์ด",
     "src": "หลักจำทั่วไป (Radiopaedia / Geeky Medics — CXR features of heart failure)"},
]


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "anims_chest_img.json"
    json.dump({"set": "chest", "items": ITEMS, "mnem": MNEM}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("anims %d · mnem %d → %s" % (len(ITEMS), len(MNEM), out))
