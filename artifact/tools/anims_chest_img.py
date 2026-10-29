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
    p.append(ell(290, 160, 18, 30, "bad"))
    p.append(t(290, 164, "หัวใจ", "xs mid b"))
    p.append(S(2, line(418, 160, 244, 104, "lms fl"), line(418, 160, 244, 216, "lms fl"),
               rect(226, 108, 8, 104, "badf", 2), t(330, 290, "เงาโตกว่าจริง", "sm mid tbad b")))
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
        shade = ["inkf", "muf", "ruf", "sk", "bx"][i]
        p.append(rect(360, y, 30, 32, shade, 2))
        p.append(t(396, y + 21, ["ดำ", "ดำจาง", "ขาว", "ขาวจ้า", "ขาวสุด"][i], "xs b"))
        p.append(t(34, y + 10, th, "xs mu"))
    p.append(S(2, rect(20, 296, 400, 96, "ac"),
               t(34, 318, "ความหนาก็มีผล", "b"),
               rect(40, 330, 40, 18, "ms", 3), t(88, 344, "บาง → ผ่านได้มาก → เทากว่า", "sm"),
               rect(40, 358, 110, 18, "ms", 3), t(158, 372, "หนา → ทึบกว่า", "sm"),
               t(410, 372, "density เดียวกัน", "xs end tac b")))
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
    p.append(path(br, "lwa w5"))
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
        out = []
        out.append(rect(x0, 40, 120, 170, "bx", 10))
        # trachea ตำแหน่งตาม kind
        tx = {"col": x0 + 70, "eff": x0 + 50, "con": x0 + 60}[kind]
        if kind == "eff":
            out.append(rect(x0 + 4, 44, 52, 162, "ms", 8))
            out.append(rect(x0 + 64, 60, 50, 140, "sk", 8))
        elif kind == "col":
            out.append(rect(x0 + 4, 44, 72, 162, "ms", 8))
            out.append(rect(x0 + 84, 60, 30, 140, "sk", 8))
        else:
            out.append(rect(x0 + 4, 60, 50, 140, "ms", 8))
            out.append(rect(x0 + 66, 60, 50, 140, "sk", 8))
        out.append(rect(tx - 5, 30, 10, 60, "wa", 4))
        return out
    p.append(t(70, 24, "ปอดยุบทั้งข้าง", "sm mid b"))
    p += mini(10, "col")
    p.append(t(220, 24, "น้ำท่วมทั้งข้าง", "sm mid b"))
    p += mini(160, "eff")
    p.append(t(370, 24, "ปอดบวมทั้งข้าง", "sm mid b"))
    p += mini(310, "con")
    p.append(S(2, ar(110, 70, 82, 70, "lbad w3", "ah-bad"), t(70, 232, "trachea ถูก \"ดึง\" เข้าหา", "sm mid tbad b"),
               t(70, 250, "ซี่โครงชิด โดมยก", "xs mid")))
    p.append(S(3, ar(196, 70, 224, 70, "lwa w3", "ah-wa"), t(220, 232, "trachea ถูก \"ดัน\" ออก", "sm mid twa b"),
               t(220, 250, "ช่องซี่โครงกว้าง", "xs mid")))
    p.append(S(4, t(370, 232, "trachea อยู่กลาง", "sm mid tok b"), t(370, 250, "air bronchogram", "xs mid")))
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
    p.append(t(110, 22, "frontal (ปอดขวา)", "sm mid b"))
    p.append(t(330, 22, "lateral (ปอดขวา)", "sm mid b"))
    # frontal right lung
    p.append(path("M110 40 C70 50 40 150 30 280 L170 280 L172 50 C150 36 128 34 110 40 Z", "bx"))
    p.append(line(36, 160, 170, 160, "lmu da"))  # minor fissure
    p.append(t(36, 154, "minor fissure", "xs mu"))
    # lateral
    p.append(path("M300 40 C250 50 240 150 236 280 L420 280 C420 160 380 50 330 38 Z", "bx"))
    p.append(path("M340 60 L262 278", "lmu da"))  # major fissure (oblique)
    p.append(line(300 - 0, 160, 420, 160, "lmu da"))  # minor fissure from major forward? (approx)
    p.append(t(244, 300, "หน้า", "xs mu")); p.append(t(420, 300, "หลัง", "xs mu end"))
    # step 2 RUL
    p.append(S(2, path("M110 40 C80 48 60 80 54 110 L170 100 L172 50 C150 36 128 34 110 40 Z", "bad"),
               ar(110, 150, 120, 108, "lbad w2", "ah-bad"), t(60, 136, "RUL: ขึ้นบน+ใน", "xs tbad b"),
               path("M330 40 C304 46 296 80 300 120 L346 90 Z", "bad"), ar(360, 150, 330, 110, "lbad w2", "ah-bad"), x=3))
    # step 3 RML
    p.append(S(3, path("M40 170 L170 176 L170 210 Z", "bad"), ar(100, 150, 100, 176, "lbad w2", "ah-bad"),
               t(40, 230, "RML: minor fissure ลง", "xs tbad b"),
               path("M300 168 L268 260 L340 210 Z", "bad"), t(300, 320, "ลิ่มบาง ยอดที่ hilum", "xs mid tbad"), x=4))
    # step 4 RLL
    p.append(S(4, path("M150 150 L170 280 L110 280 Z", "bad"), ar(80, 220, 120, 250, "lbad w2", "ah-bad"),
               t(36, 196, "RLL: ลง หลัง ใน", "xs tbad b"),
               path("M392 110 L420 120 L420 280 L360 280 Z", "bad"), ar(330, 200, 380, 230, "lbad w2", "ah-bad"),
               t(330, 320, "major fissure เลื่อนไปหลัง", "xs mid tbad"), x=5))
    p.append(S(5, rect(10, 300, 420, 110, "ac"),
               t(22, 322, "ปอดซ้าย (ไม่มี minor fissure)", "sm b"),
               t(22, 344, "LUL ยุบไป \"หน้า+บน\" → ม่านทึบจาง ๆ ซีกซ้ายบน (veil) · Luftsichel", "sm"),
               t(22, 366, "LLL ยุบไป \"ลง+หลัง+ใน\" → สามเหลี่ยมหลังหัวใจ · flat waist", "sm"),
               t(22, 388, "กฎเดียว: กลีบหมุนรอบ hilum ซึ่งเป็นจุดยึด", "sm tac b")))
    return SVG(440, 420, "ภาพเคลื่อนไหว ทิศทางการยุบของแต่ละกลีบ: RUL ขึ้นบนและเข้าใน minor fissure ยกขึ้น RML ทำให้ minor fissure ลง "
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
    p.append(path("M150 40 C100 50 60 160 50 320 L250 320 L252 50 C220 32 180 30 150 40 Z", "bx"))
    p.append(rect(252, 30, 70, 290, "sk", 6))
    p.append(t(286, 60, "mediastinum", "xs mid mu"))
    p.append(X(2, line(56, 190, 250, 190, "lmu w2 da")))
    p.append(X(2, t(60, 184, "minor fissure ปกติ (แนวนอน)", "xs mu")))
    p.append(S(2, path("M150 40 C110 48 82 90 64 150 C120 120 200 118 250 130 L252 50 C220 32 180 30 150 40 Z", "bad"),
               path("M64 150 C120 120 200 118 250 130", "lbad w3"), ar(100, 186, 104, 146, "lbad w2", "ah-bad"),
               t(70, 210, "RUL ยุบ → fissure ด้านนอกยกขึ้น", "sm tbad b"), x=3))
    p.append(S(3, path("M150 40 C110 48 82 90 64 150 C110 118 160 112 190 126 C214 150 236 160 250 150 L252 50 C220 32 180 30 150 40 Z", "bad"),
               G("pl", ell(220, 150, 34, 28, "ms")), t(220, 154, "ก้อน", "sm mid b tms"),
               path("M64 150 C110 118 160 112 190 126 C214 150 236 160 250 150", "lbad w3"),
               t(60, 236, "ด้านในโค้งลงรอบก้อนที่ hilum", "sm tms b"),
               t(60, 256, "→ เส้นรูปตัว S กลับด้าน", "sm tms")))
    p.append(S(4, rect(20, 280, 400, 70, "ac"),
               t(30, 304, "Golden S = RUL collapse + hilar mass", "sm b"),
               t(30, 326, "ผู้ใหญ่สูบบุหรี่ → มะเร็งปอดอุดหลอดลมจนกว่าจะพิสูจน์ได้ว่าไม่ใช่", "sm tac")))
    return SVG(440, 360, "ภาพเคลื่อนไหว Golden S sign: minor fissure ปกติแนวนอน เมื่อ RUL ยุบด้านนอกยกขึ้นเว้า "
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
    p.append(path("M220 30 L220 120", "lwa w5"))
    p.append(t(228, 50, "หลอดลม", "xs twa"))
    p.append(X(2, G("pl", circ(220, 180, 70, "bad")), t(220, 184, "ก้อน/ปอดอักเสบทึบ", "sm mid b tbad")))
    p.append(S(2, circ(220, 180, 70, "bad"), circ(220, 180, 40, "ms"), t(220, 184, "เนื้อตายตรงกลาง", "xs mid b"),
               t(30, 310, "ขาดเลือด/เอนไซม์จากเชื้อ → necrosis ตรงกลาง", "sm tbad"), x=3))
    p.append(S(3, circ(220, 180, 70, "bad"), circ(220, 180, 42, "bx"),
               rect(178, 186, 84, 36, "ms", 0), path("M178 186 L262 186", "lms w3"),
               path("M220 120 L220 140", "lwa w5"),
               mover(3, "waf", "2.2s", "M220 60 L220 150"),
               t(220, 172, "ลม", "xs mid b twa"), t(220, 210, "หนอง", "xs mid b tms"),
               t(30, 310, "เนื้อตายระบายทางหลอดลม → ลมเข้า → air-fluid level", "sm"), x=4))
    p.append(S(4, rect(20, 296, 400, 92, "ac"),
               t(30, 318, "ผนังบาง เรียบ < 3–4 มม. → มักไม่ร้าย (cyst/bulla/pneumatocele)", "sm"),
               t(30, 340, "ผนังหนา ขรุขระ เป็นปุ่ม → cavity: SCC · TB · abscess", "sm"),
               t(30, 362, "small cell แทบไม่ cavitate · SCC เป็น ~80% ของมะเร็งที่ cavitate", "sm tac b"),
               t(30, 382, "air-fluid level เห็นเฉพาะท่ายืน (ลำแสงแนวนอน)", "xs mu")))
    return SVG(440, 396, "ภาพเคลื่อนไหวการเกิดโพรง: ก้อนหรือปอดอักเสบมีเนื้อตายตรงกลาง เมื่อเนื้อตายระบายออกทางหลอดลมลมจะเข้าแทน "
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
    p.append(t(330, 22, "lateral", "sm mid b"))
    p.append(chest(dy=0))
    # lateral schematic on right
    p.append(rect(244, 40, 180, 250, "bx", 14))
    p.append(path("M256 70 C262 140 262 220 258 286", "lmu w2"))  # sternum line
    p.append(ell(316, 210, 40, 50, "sk"))  # heart
    p.append(t(316, 214, "หัวใจ", "xs mid"))
    p.append(rect(396, 60, 20, 228, "sk", 4))  # spine
    p.append(t(406, 300, "spine", "xs mid mu"))
    # anterior mass
    p.append(S(2, G("pl", ell(205, 150, 46, 34, "bad")), t(205, 154, "ก้อนหน้า", "xs mid b tbad"),
               path("M192 150 C172 190 160 250 172 284", "lbad w3 da"),
               G("pl", ell(282, 150, 26, 30, "bad")),
               t(40, 330, "ก้อนหน้า (anterior) แตะหัวใจ → ขอบหัวใจหาย", "sm tbad b"),
               t(40, 350, "aorta ส่วนลงยังเห็น", "sm"), x=3))
    # posterior mass
    p.append(S(3, G("pl", ell(272, 210, 30, 40, "ms")), t(272, 214, "ก้อนหลัง", "xs mid b tms"),
               path("M276 160 L276 284", "lms w3 da"),
               G("pl", ell(384, 180, 20, 34, "ms")),
               t(40, 330, "ก้อนหลัง (posterior) ขอบหัวใจยังอยู่", "sm tms b"),
               t(40, 350, "แต่ descending aorta / paraspinal line หาย", "sm"), x=4))
    p.append(S(4, rect(20, 316, 400, 92, "ac"),
               t(30, 338, "✍️ \"Obscure heart → Ant · silhouette descending aorta → Post\"", "sm b"),
               t(30, 360, "หน้า: 4T (thymoma teratoma thyroid lymphoma)", "sm"),
               t(30, 380, "กลาง: ต่อมน้ำเหลือง หลอดเลือด · หลัง: neurogenic tumor", "sm"),
               t(30, 400, "ยืนยันด้วย lateral และ CT", "xs mu")))
    return SVG(440, 416, "ภาพเคลื่อนไหวการบอกตำแหน่งก้อนในช่องอก: ก้อนด้านหน้าแตะหัวใจทำให้ขอบหัวใจหาย ก้อนด้านหลังขอบหัวใจยังอยู่ "
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
    # ปกติ: หลอดเลือดล่างใหญ่กว่าบน
    for x0, s in ((110, -1), (330, 1)):
        p.append(X(2, line(x0 + s * 50, 200, x0 + s * 20, 260, "lwa w3"), line(x0 + s * 40, 200, x0 + s * 70, 250, "lwa w3"),
                   line(x0 + s * 50, 140, x0 + s * 30, 90, "lwa"), line(x0 + s * 40, 140, x0 + s * 60, 100, "lwa")))
    p.append(X(2, t(220, 362, "ปกติ (ยืน): หลอดเลือดปอดล่าง > บน (แรงโน้มถ่วง)", "sm mid")))
    # ขั้น 2 cephalization
    p.append(S(2, *[line(x0 + s * 50, 140, x0 + s * 30, 90, "lwa w3") for x0, s in ((110, -1), (330, 1))],
               *[line(x0 + s * 40, 140, x0 + s * 60, 100, "lwa w3") for x0, s in ((110, -1), (330, 1))],
               rect(134, 314, 70, 18, "ms", 4), t(169, 327, "13–18", "xs mid b"),
               t(220, 362, "cephalization: หลอดเลือดกลีบบนโตเท่า/มากกว่าล่าง", "sm mid tms b"), x=3))
    # ขั้น 3 interstitial
    p.append(S(3, *[line(72, y, 90, y, "lbad w2") for y in (236, 248, 260, 272)],
               *[line(350, y, 368, y, "lbad w2") for y in (236, 248, 260, 272)],
               G("pl", ell(160, 140, 18, 30, "ms"), ell(282, 140, 18, 30, "ms")),
               rect(208, 314, 70, 18, "ms", 4), t(243, 327, "18–25", "xs mid b"),
               t(220, 362, "interstitial edema: Kerley B · peribronchial cuffing", "sm mid tbad b"), x=4))
    # ขั้น 4 alveolar
    p.append(S(4, G("pl", path("M192 110 C140 120 120 180 150 230 C170 250 186 230 192 200 Z", "bad"),
                    path("M250 110 C300 120 320 180 290 230 C270 250 254 230 250 200 Z", "bad")),
               path("M70 292 C100 270 140 270 172 284 L172 292 Z", "wa"), path("M370 292 C340 270 300 270 270 284 L270 292 Z", "wa"),
               rect(282, 314, 76, 18, "bad", 4), t(320, 327, "> 25", "xs mid b"),
               t(220, 362, "alveolar edema: bat-wing รอบขั้วปอด + effusion", "sm mid tbad b")))
    p.append(S(5, rect(20, 372, 400, 46, "ac"),
               t(30, 392, "ABCDE: Alveolar edema · kerley B · Cardiomegaly", "sm b"),
               t(30, 410, "Dilated upper lobe vessels · Effusion", "sm b")))
    return SVG(440, 424, "ภาพเคลื่อนไหวความดันหลอดเลือดดำปอดที่สูงขึ้น: ปกติหลอดเลือดส่วนล่างใหญ่กว่า เมื่อความดันสูงขึ้นเกิด cephalization "
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
    p.append(path("M150 40 C100 50 60 160 50 300 L250 300 L252 50 C220 32 180 30 150 40 Z", "bx"))
    p.append(rect(252, 30, 60, 270, "sk", 6))
    p.append(X(2, path("M50 300 Q150 250 250 300", "ln w3")))
    p.append(X(2, t(60, 324, "ปกติ: CP angle แหลม · ไม่มีน้ำ", "sm")))
    # meniscus
    p.append(S(2, path("M56 220 C90 236 150 262 250 268 L250 300 L50 300 Z", "wa"),
               path("M56 220 C90 236 150 262 250 268", "lwa w3"),
               t(60, 324, "meniscus: ขอบบนเว้า สูงด้านข้าง (> 200 มล. บน PA)", "sm twa b"),
               t(60, 344, "แรงดึงยืด (recoil) + น้ำหนักน้ำ → ชั้นน้ำหนาด้านข้าง", "xs"), x=3))
    # subpulmonic
    p.append(S(3, path("M50 300 Q200 230 250 300", "lwa w3"), path("M50 300 Q200 230 250 300 L250 300 Z", "wa"),
               path("M50 300 Q150 280 250 300", "ln da"),
               ar(200, 210, 186, 248, "lbad w2", "ah-bad"), t(150, 204, "ยอดโดมเลื่อนออกด้านข้าง", "xs tbad b"),
               t(60, 324, "subpulmonic: น้ำใต้ปอด เลียนแบบโดมยกสูง", "sm twa b"),
               t(60, 344, "ซ้าย: กระเพาะห่างจากโดม > 2 ซม.", "xs"), x=4))
    # decubitus
    p.append(S(4, rect(20, 60, 400, 140, "bx", 14), rect(20, 168, 400, 32, "wa", 6),
               t(220, 160, "ตะแคงข้างที่มีน้ำลง (lateral decubitus)", "sm mid b"),
               ar(220, 120, 220, 162, "lwa w2", "ah-wa"),
               t(220, 192, "น้ำอิสระไหลเป็นชั้นแนวยาวตามผนังด้านล่าง", "xs mid"),
               t(60, 324, "น้ำไหล = free fluid · ไม่ไหล = loculated", "sm twa b"),
               t(60, 344, "✍️ loculated มี septa → สงสัย parapneumonic/empyema", "xs")))
    return SVG(440, 352, "ภาพเคลื่อนไหวน้ำในช่องเยื่อหุ้มปอด: meniscus sign ขอบบนเว้าสูงด้านข้าง subpulmonic effusion "
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
    p.append(rect(20, 30, 220, 290, "bx", 30))  # hemithorax right
    p.append(rect(240, 30, 60, 290, "sk", 6))  # mediastinum
    p.append(t(270, 50, "mediast.", "xs mid mu"))
    p.append(rect(300, 30, 120, 290, "bx", 30))
    p.append(X(2, path("M28 40 L232 40 L232 312 L28 312 Z", "lwa"), t(130, 180, "ปอดเต็มช่อง", "sm mid")))
    p.append(X(2, t(30, 344, "ปกติ: visceral + parietal pleura แนบกัน (ความดันลบ)", "sm")))
    # step 2 simple ptx
    p.append(S(2, path("M80 70 C140 60 200 80 226 120 L228 300 C160 310 90 300 60 270 C40 200 50 110 80 70 Z", "wa"),
               path("M80 70 C140 60 200 80 226 120", "ln w3"), path("M80 70 C40 110 40 200 60 270", "ln w3"),
               t(52, 58, "visceral pleural line", "xs b"),
               t(30, 140, "ไม่มี", "xs mu"), t(30, 154, "lung", "xs mu"), t(30, 168, "marking", "xs mu"),
               t(30, 344, "ลมเข้าช่องเยื่อหุ้ม → ปอดหดด้วย recoil", "sm twa b"),
               t(30, 364, "เส้นขาวบาง ๆ + ไม่มีลายปอดนอกเส้น", "sm"), x=3))
    # step 3 tension
    p.append(S(3, path("M140 120 C180 110 210 140 214 180 C210 230 180 250 150 240 C120 220 120 150 140 120 Z", "wa"),
               G("pl", rect(258, 30, 60, 290, "sk", 6)), ar(250, 180, 300, 180, "lbad w3", "ah-bad"),
               t(270, 50, "mediast.", "xs mid mu"),
               path("M20 320 Q130 344 240 320", "lbad w3"), ar(130, 300, 130, 330, "lbad w2", "ah-bad"),
               mover(3, "badf", "1.6s", "M60 60 L110 110"),
               t(30, 344, "ลิ้นทางเดียว: ลมเข้าได้ออกไม่ได้ → ความดันบวก", "sm tbad b"),
               t(30, 364, "mediastinum ถูกดันข้าม · โดมกดต่ำ · venous return ↓", "sm tbad"), x=4))
    p.append(S(4, rect(20, 330, 400, 86, "ac"),
               t(30, 352, "ขนาด (BTS): ระยะปอด–ผนังที่ระดับ hilum > 2 ซม. ≈ 50%", "sm b"),
               t(30, 374, "ท่านอนหงาย: ลมขึ้นด้านหน้า-ล่าง → deep sulcus sign", "sm"),
               t(30, 396, "tension = วินิจฉัยทางคลินิก → needle decompression ก่อนถ่ายฟิล์ม", "sm tbad b")))
    return SVG(440, 424, "ภาพเคลื่อนไหว pneumothorax: ลมเข้าช่องเยื่อหุ้มปอดทำให้ปอดหดเห็นเส้น visceral pleura และไม่มีลายปอดนอกเส้น "
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
    p.append(rect(20, 30, 400, 200, "bx", 14))
    p.append(t(30, 50, "ถุงลม / interstitium (จำลอง)", "xs mu"))
    p.append(S(1, mover(3, "inkf", "2s", "M40 40 L150 120"), mover(3, "inkf", "2.4s", "M70 36 L170 110", "-.8s"),
               t(30, 252, "ฝุ่น crystalline silica < 5 ไมครอน เข้าถึงถุงลม", "sm"), x=2))
    p.append(S(2, circ(170, 120, 30, "ac"), circ(160, 116, 4, "inkf"), circ(178, 126, 4, "inkf"),
               t(170, 170, "macrophage กิน", "xs mid b"),
               t(30, 252, "macrophage กลืนผลึก → lysosome แตก → เซลล์ตาย", "sm"), x=3))
    p.append(S(3, G("pl", circ(170, 120, 30, "bad")), t(170, 124, "ตาย", "xs mid b tbad"),
               ar(200, 110, 260, 80, "lbad w2", "ah-bad"), ar(200, 130, 260, 160, "lbad w2", "ah-bad"),
               t(266, 84, "IL-1 TNF", "xs b tbad"), t(266, 166, "TGF-β", "xs b tbad"),
               t(30, 252, "ปล่อยผลึกออกมาให้เซลล์ใหม่กินซ้ำ + cytokine", "sm"), x=4))
    p.append(S(4, *[circ(80 + (k % 5) * 60, 70 + (k // 5) * 50, 10 + (k % 3) * 3, "ms") for k in range(12)],
               t(30, 252, "fibroblast สร้าง collagen เป็นวง → silicotic nodule", "sm tms b"),
               t(30, 272, "ปอดบน (ระบายน้ำเหลืองช้ากว่า) + ต่อมน้ำเหลือง hilum", "sm"), x=5))
    p.append(S(5, rect(20, 236, 400, 140, "ac"),
               t(30, 258, "บนฟิล์ม: small rounded opacities ปอดบน", "sm b"),
               t(30, 280, "eggshell calcification ของต่อมน้ำเหลือง hilum", "sm"),
               t(30, 302, "ก้อนรวมกัน > 1 ซม. = PMF (progressive massive fibrosis)", "sm"),
               t(30, 324, "macrophage เสีย → เสี่ยง TB สูง → คัดกรอง TB/LTBI", "sm tbad b"),
               t(30, 346, "ไม่มียารักษาให้หาย → หยุดสัมผัส + ป้องกัน", "sm"),
               t(30, 366, "(ไม่อยู่ในสไลด์ — อิงตำรา/ILO)", "xs mu")))
    return SVG(440, 384, "ภาพเคลื่อนไหว silicosis: ฝุ่นซิลิกาเข้าถุงลม macrophage กลืนแล้วตาย ปล่อยผลึกและ cytokine "
               "กระตุ้น fibroblast สร้างปุ่มพังผืดในปอดบนและต่อมน้ำเหลือง hilum เป็น eggshell calcification และเสี่ยงวัณโรค", *p)


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
    p.append(path("M150 40 C100 50 60 160 50 300 L250 300 L252 50 C220 32 180 30 150 40 Z", "bx"))
    p.append(path("M150 40 C100 50 60 160 50 300", "lmu w2"))
    p.append(t(270, 50, "ใยหินยาว บาง", "xs b"))
    p.append(S(1, *[line(140 + k * 14, 70 + k * 6, 156 + k * 14, 96 + k * 6, "ln w2") for k in range(5)],
               t(270, 70, "ใยหินยาว ไปถึง", "xs"), t(270, 84, "ปอดล่างและเยื่อหุ้ม", "xs"), x=2))
    p.append(S(2, *[G("pl", rect(58 + k * 4, 150 + k * 44, 10, 28, "ms", 3)) for k in range(3)],
               path("M60 300 Q150 286 240 300", "lms w5"),
               t(270, 140, "pleural plaque", "sm b tms"), t(270, 158, "parietal pleura", "xs"),
               t(270, 174, "บนโดม · ผนังด้านข้าง", "xs"), t(270, 190, "มัก calcify · ไม่ร้าย", "xs"), x=3))
    p.append(S(3, *[path("M%d %d l14 -8 l10 10 l14 -6" % (80 + k * 30, 240 + (k % 2) * 16), "lbad w2") for k in range(5)],
               t(270, 220, "asbestosis", "sm b tbad"), t(270, 238, "fibrosis ปอดล่าง", "xs"),
               t(270, 254, "reticular · subpleural", "xs"), x=4))
    p.append(S(4, G("pl", path("M54 120 C70 116 76 160 66 220 C62 260 60 280 56 296 C46 260 44 170 54 120 Z", "bad")),
               t(270, 220, "mesothelioma", "sm b tbad"), t(270, 238, "เยื่อหุ้มหนาเป็นปุ่ม", "xs"),
               t(270, 254, "+ effusion ข้างเดียว", "xs"), t(270, 270, "ระยะแฝง 20–40 ปี", "xs")))
    p.append(S(5, rect(20, 312, 400, 74, "ac"),
               t(30, 334, "ใยหิน: กระเบื้องลอนหลังคา ท่อซีเมนต์ ผ้าเบรก ฉนวน", "sm b"),
               t(30, 356, "plaque = ตัวบ่งชี้การสัมผัส · บุหรี่ + ใยหิน → มะเร็งปอดทวีคูณ", "sm"),
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
