# -*- coding: utf-8 -*-
"""ภาพประกอบ + กลไก คาบ cardio 24 Atrial fibrillation (ใส่ด้วย apply_figs.py)"""
import math
from svg import *

SET, LEC = "cardio", "24"

MD_CAUSE = """#### กลไก: ทำไมโรคเหล่านี้จึงทำให้เกิด AF
| ภาวะ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Hypertension** | LV หนาและแข็ง (LVH) คลายตัวยาก → ต้องใช้ความดันสูงขึ้นจึงเติม LV ได้ → ความดัน LA สูงเรื้อรัง → LA ยืด โต และเกิดพังผืด | ความดันสูงเรื้อรัง · LVH ใน ECG หรือ echo |
| **Mitral stenosis** | ลิ้นแคบ เลือดผ่านจาก LA ลง LV ยาก → ความดัน LA สูงมาก LA โตมาก → f wave ใหญ่ (coarse AF) และเลือดค้างใน LA จนเกิดลิ่มเลือดง่ายมาก | diastolic rumble · opening snap · echo → ใช้ warfarin |
| **Heart failure** | ความดันเติมเลือดสูงยืดห้องบน + angiotensin II และ aldosterone กระตุ้นพังผืด | AF กับ HF ซ้ำเติมกันไปมา |
| **Hyperthyroidism** | thyroid hormone เพิ่มความไวต่อ β-adrenergic และทำให้ refractory period ของห้องบนสั้นลง → จุดยิงไฟฟ้าเกินง่ายขึ้นและวงไฟฟ้าเล็ก ๆ คงอยู่ได้ | TSH ต่ำ free T4 สูง · AF เร็วคุมยาก |
| **สุรา (holiday heart)** | พิษโดยตรงต่อกล้ามเนื้อห้องบน + ระบบประสาทอัตโนมัติแกว่ง + K และ Mg ต่ำ → จุดยิงไฟฟ้าเกิน | ใจสั่นหลังดื่มหนัก หายเองเมื่อหยุดดื่ม |
| **Sleep apnea** | หายใจเข้าแรงขณะทางเดินหายใจปิด → ความดันในช่องอกติดลบมาก ดึงผนังห้องบนให้ยืด + ออกซิเจนต่ำกระตุ้น sympathetic ทุกคืน | กรน หยุดหายใจ ง่วงกลางวัน · sleep test |
| **ASD** | เลือดไหลลัดจาก LA ไป RA → RA รับเลือดเกิน ยืดและโต | fixed splitting ของ S2 · echo |"""

MD_SIGN = """#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ใจสั่น ชีพจรไม่สม่ำเสมอแบบไม่มีรูปแบบ** | ห้องบนส่งไฟฟ้า 350–600 ครั้ง/นาทีแบบสุ่ม AV node ปล่อยผ่านเฉพาะสัญญาณที่มาถึงตอนพ้นระยะดื้อ → ช่วง R-R สุ่มทุกจังหวะ | PAC/PVC บ่อยก็ไม่สม่ำเสมอ แต่มีจังหวะพื้นที่สม่ำเสมอ → ต้องยืนยันด้วย ECG |
| **ไม่มี a wave ใน JVP** | a wave เกิดจากห้องบนขวาบีบดันเลือดย้อนขึ้นคอช่วงท้าย diastole → ห้องบนสั่นพลิ้วไม่บีบ a wave จึงหายไป | ต่างจาก atrial flutter หรือ heart block ที่ยังเห็นคลื่นจากห้องบน |
| **S1 ดังไม่เท่ากัน** | ความดังของ S1 ขึ้นกับตำแหน่งลิ้น mitral ตอน LV เริ่มบีบ — R-R สั้น ลิ้นยังเปิดกว้างแล้วถูกปิดแรง S1 ดัง · R-R ยาว ลิ้นลอยเข้าหากันก่อน S1 เบา | ร่วมกับชีพจรสุ่ม ชวนคิดถึง AF |
| **เหนื่อย ทนออกแรงไม่ได้ น้ำท่วมปอด** | เสีย atrial kick + diastole สั้น → LV เติมเลือดไม่พอ CO ลด · เลือดค้างใน LA ความดัน LA สูง → ปอดคั่งน้ำ | ทรุดเร็วในหัวใจแข็ง (LVH, HFpEF, MS) |
| **หัวใจโตและบีบอ่อนลงเมื่อ AF เร็วนาน** | tachycardia-induced cardiomyopathy — เต้นเร็วต่อเนื่องหลายสัปดาห์ กล้ามเนื้อหัวใจล้า EF ลด | EF ฟื้นได้เมื่อคุมอัตราหรือจังหวะได้ |"""

INSERTS = [
    ("cardio-af-01", "**Atrial fibrillation (AF)** คือภาวะ", "fig:af_mech"),
    ("cardio-af-01", "ห้องบนที่สั่นพลิ้วไม่บีบตัว →", "fig:af_laa"),
    ("cardio-af-02", "(AF begets AF)", "fig:af_remodel"),
    ("cardio-af-02", "| Sleep apnea |", MD_CAUSE),
    ("cardio-af-03", "**ทำไมมีอาการ**", "fig:af_kick"),
    ("cardio-af-03", "- ไม่มี a wave ใน JVP", "fig:af_deficit"),
    ("cardio-af-03", "- ไม่มี a wave ใน JVP", MD_SIGN),
    ("cardio-af-04", "| **3. Atrial rate > 300 bpm** |", "fig:af_ecg"),
    ("cardio-af-05", "**ข้อสำคัญ** — ระยะไม่ได้เปลี่ยน", "fig:af_types"),
    ("cardio-af-06", "คะแนนเต็ม 9", "fig:af_virchow"),
    ("cardio-af-07", "| | **Rivaroxaban · Apixaban · Edoxaban** |", "fig:af_coag"),
    ("cardio-af-08", "กราฟในสไลด์: INR", "fig:af_inr"),
    ("cardio-af-09", "**กลไก** — ทุกตัว", "fig:af_avnode"),
    ("cardio-af-09", "ยังคุมไม่ได้ → ใช้ยาร่วมกัน", "fig:af_wpw"),
    ("cardio-af-10", "**ทำไมต้อง 4 สัปดาห์หลัง", "fig:af_cv"),
    ("cardio-af-10", "- **AF ablation** (pulmonary vein isolation)", "fig:af_pv"),
    ("cardio-af-11", "การคุมปัจจัยเหล่านี้ทำให้", "fig:af_lifestyle"),
]


# ---------------------------------------------------------------- ECG helper
def _gauss(x, c, a, w):
    return a * math.exp(-((x - c) / w) ** 2)


def _ecg(x0, x1, base, beats, kind="sinus", amp=1.0):
    """เส้น ECG — beats = ตำแหน่ง x ของ R · kind: sinus / af / flutter"""
    pts = []
    x = x0
    while x <= x1:
        y = 0.0
        if kind == "af":
            y += 1.6 * math.sin(x * 0.9) + 1.1 * math.sin(x * 1.7 + 1) + 0.8 * math.sin(x * 2.9 + 2)
        if kind == "flutter":
            ph = ((x - x0) % 20) / 20.0
            y += -6 + 9 * ph if ph < 0.75 else 0.75 * 9 - 6 - 27 * (ph - 0.75)
        for r in beats:
            if kind == "sinus":
                y += _gauss(x, r - 18, 4.5, 4)
            y += -_gauss(x, r - 3, 3, 1.2) + _gauss(x, r, 30, 1.6) - _gauss(x, r + 3, 7, 1.4)
            y += _gauss(x, r + 22, 7, 6)
        pts.append((x, base - y * amp))
        x += 1
    return poly(pts, "ln w2")


# ---------------------------------------------------------------- af-01
def af_mech():
    def heart(y, af):
        o = [rect(20, y + 6, 140, 58, "ac", 14), t(150, y + 22, "ห้องบน", "xs end mu"),
             circ(90, y + 76, 7, "msf"), t(102, y + 80, "AV", "xs b"),
             rect(30, y + 90, 120, 60, "sk", 14), t(90, y + 126, "ห้องล่าง", "xs mid mu"),
             line(90, y + 64, 90, y + 68, "ln"), line(90, y + 83, 90, y + 98, "ln", "ah")]
        if not af:
            o += [circ(36, y + 20, 6, "okf"), t(36, y + 4, "SA node", "xs mid tok b")]
            for r in (18, 32, 46):
                o.append(path("M%s %s A%s %s 0 0 1 %s %s" % (36 + r, y + 20, r, r, 36, y + 20 + r), "lok w2"))
        else:
            for cx, cy in ((40, 22), (70, 40), (98, 20), (112, 46), (138, 40)):
                o.append(path("M%s %s A8 8 0 1 1 %s %s" % (cx + 8, y + cy, cx, y + cy + 8), "lbad w2", "ah-bad"))
        return o
    sin_beats = [210 + 56 * k for k in range(4)]
    af_beats = [206, 244, 300, 330, 392]
    out = (heart(4, False) + heart(186, True) +
           [t(176, 20, "Sinus rhythm (ปกติ)", "sm b tok"),
            _ecg(176, 412, 92, sin_beats, "sinus"),
            t(176, 130, "SA node ปล่อยคลื่นเดียว ห้องบนบีบพร้อมกัน", "xs i2"),
            t(176, 146, "P นำหน้าทุก QRS · R-R เท่ากัน", "xs i2"),
            line(8, 176, 412, 176, "lru da"),
            t(176, 202, "Atrial fibrillation", "sm b tbad"),
            _ecg(176, 412, 274, af_beats, "af"),
            t(176, 312, "วงไฟฟ้าเล็กหลายวง 350–600 ครั้ง/นาที", "xs i2"),
            t(176, 328, "ไม่มี P (เห็น f wave) · AV node กรองแบบสุ่ม", "xs i2"),
            t(176, 344, "→ R-R ไม่เท่ากัน (irregularly irregular)", "xs b tbad")])
    return fig("Sinus rhythm เทียบกับ AF",
               "จังหวะปกติ **SA node** ส่งคลื่นไฟฟ้าลูกเดียวแผ่ทั่วห้องบน ห้องบนจึงบีบพร้อมกัน (P wave) แล้วส่งต่อผ่าน AV node อย่างเป็นระเบียบ "
               "ใน **AF** ไฟฟ้าวนเป็นวงเล็ก ๆ หลายวงพร้อมกัน ห้องบนแค่ **สั่นพลิ้ว ไม่บีบ** (f wave แทน P) และ **AV node** "
               "ได้รับสัญญาณถี่เกินจะส่งได้หมด จึงปล่อยผ่านแบบสุ่ม → ห้องล่างเต้นไม่สม่ำเสมอ",
               svg(420, 352, "เทียบ sinus rhythm ที่มีคลื่นไฟฟ้าเดียวจาก SA node กับ AF ที่มีวงไฟฟ้าเล็กหลายวง และ ECG ของแต่ละแบบ", *out))


def af_laa():
    out = [ell(224, 72, 34, 15, "ac", rot=-30),
           ell(140, 110, 90, 56, "ac"),
           path("M222 66 q8 -10 18 -4 q8 6 0 14 q-6 8 -14 4 q-10 -2 -4 -14 z", "badf"),
           t(236, 22, "LAA กระเปาะปลายตัน", "xs b mid"), t(236, 36, "เลือดค้าง → ลิ่มเลือด", "xs b mid tbad"),
           line(232, 40, 232, 54, "lmu"),
           path("M108 96 A32 14 0 0 1 172 96", "lmu w2 da", "ah-mu"), path("M172 106 A32 14 0 0 1 108 106", "lmu w2 da", "ah-mu"),
           t(140, 136, "ห้องบนสั่น ไม่บีบ", "xs mid b"), t(140, 150, "เลือดวนช้า (stasis)", "xs mid i2"),
           line(140, 166, 140, 198, "ln", "ah"),
           ell(140, 228, 60, 28, "sk"), t(140, 232, "LV", "sm b mid"),
           path("M244 84 C 280 130, 240 190, 204 218", "lbad w2 da", "ah-bad"),
           path("M200 236 C 290 250, 330 230, 350 188", "lbad w2 da", "ah-bad"),
           t(250, 268, "ก้อนหลุด ผ่าน LV → aorta", "xs b tbad"),
           t(362, 96, "หลอดเลือดสมอง", "xs mid b"), t(362, 110, "ใหญ่ถูกอุด", "xs mid b tbad"),
           ell(362, 150, 48, 32, "bx"), path("M326 160 q20 -14 30 -4 q10 10 28 -2", "lbad w2"), circ(356, 156, 6, "badf"),
           box(8, 282, 404, 44, "bad", "ก้อนจาก LA ใหญ่ อุดหลอดเลือดแดงใหญ่ในสมอง\n→ stroke รุนแรงกว่า stroke จากหลอดเลือดเล็ก", fs=11.5)]
    return fig("AF ทำให้เกิด stroke ได้อย่างไร",
               "ห้องบนที่สั่นพลิ้วไม่บีบตัว เลือดใน **left atrial appendage** (กระเปาะปลายตันของ LA) จึงไหลช้าและค้าง → "
               "เกิด **ลิ่มเลือด** ที่ LAA มากที่สุด → หลุดผ่าน LV ขึ้น aorta ไปอุดหลอดเลือดสมอง · ก้อนจากหัวใจมีขนาดใหญ่ "
               "จึงมักอุดหลอดเลือดแดงใหญ่และทำให้ stroke รุนแรง — เป็นเหตุผลของยาต้านการแข็งตัวและการปิด LAA",
               svg(420, 334, "ลิ่มเลือดก่อตัวใน left atrial appendage ที่เลือดค้าง แล้วหลุดผ่าน LV และ aorta ไปอุดหลอดเลือดสมอง", *out))


# ---------------------------------------------------------------- af-02
def af_remodel():
    out = [box(8, 8, 128, 58, "wa", "HT · HF · MS\n→ ความดัน LA ↑\nห้องบนยืด โต", fs=11),
           box(146, 8, 128, 58, "ms", "อายุ · อ้วน · DM\n→ อักเสบ\nพังผืด", fs=11),
           box(284, 8, 128, 58, "bad", "ไทรอยด์เป็นพิษ\nสุรา · sympathetic\n→ จุดยิงไฟฟ้าเกิน", fs=11),
           line(72, 66, 100, 92, "ln", "ah"), line(210, 66, 180, 92, "ln", "ah"), line(348, 66, 348, 92, "ln", "ah"),
           box(8, 94, 262, 44, "sk", "Substrate: ห้องบนโต + พังผืด\nนำไฟฟ้าช้า ไม่สม่ำเสมอ", fs=11.5),
           box(280, 94, 132, 44, "sk", "Trigger: ectopic\nมักจาก pulmonary vein", fs=11),
           line(139, 138, 190, 164, "ln", "ah"), line(346, 138, 250, 164, "ln", "ah"),
           box(100, 166, 220, 40, "bad", "AF: วงไฟฟ้าเล็กหลายวง (re-entry)", "b", fs=12),
           line(210, 206, 210, 230, "ln", "ah"),
           box(60, 232, 300, 52, "ms", "AF ต่อเนื่อง → refractory period สั้นลง\n+ ห้องบนโต พังผืดเพิ่ม (remodeling)", fs=11.5),
           path("M60 258 H30 V142", "lbad w2", "ah-bad"),
           t(36, 206, "AF", "xs b tbad"), t(36, 220, "begets", "xs b tbad"), t(36, 234, "AF", "xs b tbad"),
           t(210, 306, "ยิ่งเป็นนาน ยิ่งกลับเป็นจังหวะปกติยาก", "xs mid i2"),
           t(210, 322, "paroxysmal → persistent → permanent", "xs mid b")]
    return fig("กลไกร่วม: substrate + trigger และ AF begets AF",
               "AF ต้องมีสองอย่าง — **trigger** คือจุดยิงไฟฟ้าเกิน (ส่วนใหญ่จากกล้ามเนื้อที่ยื่นเข้าไปใน pulmonary vein) "
               "และ **substrate** คือห้องบนที่โตและมีพังผืดจนนำไฟฟ้าช้าไม่สม่ำเสมอ ให้วงไฟฟ้าเล็กวนต่อได้ · โรคร่วมสร้างทั้งสองอย่าง "
               "และเมื่อ AF เป็นต่อเนื่อง ห้องบนก็ **เปลี่ยนแปลงทั้งไฟฟ้าและโครงสร้าง** จน AF ยิ่งคงอยู่ง่ายขึ้น",
               svg(420, 330, "โรคร่วมทำให้ห้องบนโตและมีพังผืดและมีจุดยิงไฟฟ้า จนเกิด AF และ AF ทำให้ห้องบนเสื่อมต่อเป็นวงจร", *out))


# ---------------------------------------------------------------- af-03
def af_kick():
    X0, Y0 = 50, 190
    pas = lambda tt: 110 * (1 - math.exp(-tt / 60))
    norm = [(X0 + tt, Y0 - pas(tt)) for tt in range(0, 251, 5)]
    norm += [(X0 + 250 + k, Y0 - pas(250) - 30 * (k / 50) ** 1.5) for k in range(0, 51, 5)] + [(X0 + 310, Y0 - pas(250) - 30)]
    slow = [(X0 + tt, Y0 - pas(tt) + 0.5) for tt in range(0, 301, 5)]
    fast = [(X0 + tt, Y0 - pas(tt) + 1) for tt in range(0, 101, 5)]
    out = [line(X0, Y0, 410, Y0, "lmu"), line(X0, Y0, X0, 30, "lmu"),
           t(X0 - 4, 24, "ปริมาตรเลือดใน LV ช่วง diastole", "xs mu"), t(410, Y0 + 16, "เวลา →", "xs end mu"),
           poly(norm, "lok w3"), poly(slow, "lms w2 da"), poly(fast, "lbad w3"),
           circ(X0 + 310, Y0 - pas(250) - 30, 4, "okf"), circ(X0 + 300, Y0 - pas(300), 4, "msf"), circ(X0 + 100, Y0 - pas(100), 4, "badf"),
           t(X0 + 304, 36, "sinus: EDV เต็ม", "xs b tok end"),
           t(X0 + 246, 56, "atrial kick", "xs b tok end"), t(X0 + 246, 68, "20–30%", "xs tok end"),
           t(X0 + 300, Y0 - pas(300) + 18, "AF ช้า: ไม่มี kick", "xs b tms end"),
           t(X0 + 70, 134, "AF เร็ว: diastole สั้น", "xs b tbad"),
           t(X0 + 70, 148, "+ ไม่มี kick → EDV ต่ำสุด", "xs b tbad")]
    chain = ["EDV ↓", "SV ↓", "CO ↓", "เหนื่อย หน้ามืด\nBP ต่ำ HF"]
    for k, s in enumerate(chain):
        x = 8 + 104 * k
        out.append(box(x, 214, 92, 40, "bad" if k == 3 else "sk", s, "b" if k < 3 else "", fs=11 if k == 3 else 12.5))
        if k < 3: out.append(line(x + 92, 234, x + 102, 234, "ln", "ah"))
    out.append(t(210, 276, "หัวใจแข็ง (LVH · HFpEF · MS) พึ่ง kick มาก → ทรุดเร็วที่สุด", "xs mid b"))
    return fig("ทำไม AF จึงทำให้ CO ลด",
               "ปกติ LV เติมเลือดส่วนใหญ่เองช่วงต้น diastole แล้วห้องบนบีบเติมอีก **20–30%** ตอนท้าย (**atrial kick**) · AF ช้า "
               "เสียเฉพาะ kick · AF เร็ว diastole สั้นจน **ตัดช่วงเติมเลือด** ด้วย EDV จึงต่ำสุด → SV และ CO ลด · หัวใจที่แข็ง "
               "เติมเลือดช่วงต้นได้น้อยอยู่แล้ว จึงพึ่ง kick มากและทรุดเร็ว",
               svg(420, 286, "ปริมาตร LV ระหว่าง diastole ใน sinus AF ช้า และ AF เร็ว แสดงการเสีย atrial kick และ diastole ที่สั้น", *out))


def af_deficit():
    beats = [92, 140, 160, 206, 226, 276, 294, 336, 382]
    base, thr = 196, 166
    out = [t(8, 64, "ECG", "xs b mu"), _ecg(80, 412, 64, beats, "af", 0.8),
           t(8, 122, "ชีพจร", "xs b mu"), t(8, 136, "ที่ข้อมือ", "xs b mu"),
           line(80, base, 412, base, "lru"), line(80, thr, 412, thr, "lms da"), t(8, thr + 4, "แรงพอคลำ", "xs tms b")]
    felt = 0
    for i, x in enumerate(beats):
        rr = x - beats[i - 1] if i else 60
        amp = min(56, rr * 0.95)
        nxt = beats[i + 1] if i + 1 < len(beats) else 412
        w = min(34, nxt - x)
        sh = [(0.12, 0), (0.3, 0.8), (0.4, 1), (0.52, 0.92), (0.62, 0.7), (0.68, 0.73), (0.85, 0.35), (1, 0)]
        pts = [(x + w * a, base - amp * b) for a, b in sh]
        ok = base - amp < thr
        felt += ok
        out += [line(x, 96, x, base - 2, "lru dt"), poly(pts, "lbad w2" if ok else "lmu w2"),
                t(x + 12, base + 16, "✓" if ok else "✕", "xs mid b " + ("tok" if ok else "tbad"))]
    out += [t(8, 234, "R-R สั้น → LV เติมเลือดน้อย → SV น้อย → แรงดันไม่ถึงข้อมือ", "xs i2"),
            t(8, 252, "ฟังที่หัวใจ %d ครั้ง · คลำชีพจรได้ %d ครั้ง → pulse deficit %d" % (len(beats), felt, len(beats) - felt), "sm b")]
    return fig("Pulse deficit",
               "ทุก QRS ทำให้ห้องล่างบีบและได้ยินเสียงหัวใจ แต่จังหวะที่มาหลัง **R-R สั้น** มีเวลาเติมเลือดน้อย SV จึงเล็กจน "
               "**แรงดันไปไม่ถึงข้อมือ** · นับที่หัวใจจึงได้มากกว่าคลำชีพจร — ต้องนับอัตราจากการฟังหรือ ECG ไม่ใช่จากชีพจร",
               svg(420, 262, "ECG ของ AF กับคลื่นความดันที่ข้อมือ จังหวะที่ R-R สั้นให้คลื่นเล็กจนคลำไม่ได้ เกิด pulse deficit", *out))


# ---------------------------------------------------------------- af-04
def af_ecg():
    sin_beats = [40 + 80 * k for k in range(5)]
    af_beats = [36, 88, 166, 210, 282, 324, 398]
    fl_beats = [40 + 40 * k for k in range(10)]
    out = [t(8, 16, "Sinus · 75/นาที", "sm b tok"), _ecg(8, 412, 70, sin_beats, "sinus"),
           t(8, 100, "P นำหน้าทุก QRS · R-R เท่ากัน", "xs i2"),
           t(8, 130, "AF", "sm b tbad"), _ecg(8, 412, 186, af_beats, "af"),
           line(88, 140, 166, 140, "lbad", "ah-bad"), t(127, 134, "ยาว", "xs mid tbad b"),
           line(166, 140, 210, 140, "lbad", "ah-bad"), t(188, 134, "สั้น", "xs mid tbad b"),
           line(210, 140, 282, 140, "lbad", "ah-bad"), t(246, 134, "ยาว", "xs mid tbad b"),
           t(8, 216, "ไม่มี P · เส้นฐานเป็นคลื่นเล็กไม่เป็นระเบียบ (f wave) · R-R สุ่ม", "xs i2"),
           t(8, 246, "Atrial flutter 2:1", "sm b tms"), _ecg(8, 412, 300, fl_beats, "flutter"),
           t(8, 330, "ฟันเลื่อย (sawtooth) 300/นาที · ผ่าน AV ทุก 2 ลูก → 150 สม่ำเสมอ", "xs i2")]
    return fig("ECG: AF เทียบกับ sinus และ atrial flutter",
               "**AF** — ห้องบนไม่ได้ depolarize เป็นก้อนเดียวจึง **ไม่มี P** เห็นเป็น f wave เล็ก ๆ ที่เส้นฐาน และ AV node ปล่อยผ่านแบบสุ่ม "
               "จึง **R-R ไม่เท่ากัน** · **Atrial flutter** มีวงไฟฟ้าวงใหญ่วงเดียวใน RA จึงได้คลื่นฟันเลื่อยสม่ำเสมอราว 300/นาที "
               "และ AV node ปล่อยผ่านเป็นสัดส่วนคงที่ (มัก 2:1) ชีพจรจึง **สม่ำเสมอ** ราว 150",
               svg(420, 340, "ECG เปรียบเทียบ sinus rhythm AF ที่ R-R ไม่เท่ากันและไม่มี P และ atrial flutter ที่เป็นคลื่นฟันเลื่อย", *out))


# ---------------------------------------------------------------- af-05
def af_types():
    X = {"0": 112, "48": 152, "7d": 214, "1y": 320}
    rows = [("Paroxysmal", "หายเอง ≤ 7 วัน", 112, 186, True), ("Persistent", "> 7 วัน", 112, 262, True),
            ("Long-standing", "> 1 ปี ยังแก้จังหวะ", 112, 360, True), ("Permanent", "ตกลงไม่แก้จังหวะ", 112, 412, False)]
    out = [t(X["0"], 26, "เริ่ม", "xs mid mu")]
    for k, lab in (("48", "48 ชม."), ("7d", "7 วัน"), ("1y", "1 ปี")):
        out += [line(X[k], 32, X[k], 214, "lmu da"), t(X[k], 26, lab, "xs mid b")]
    for i, (a, b, x1, x2, conv) in enumerate(rows):
        y = 44 + 48 * i
        out += [t(8, y + 12, a, "sm b"), t(8, y + 28, b, "xs i2"),
                rect(x1, y + 4, x2 - x1, 18, "bad", 4), t(x1 + 6, y + 17, "AF", "xs b tbad")]
        if conv and i == 0:
            out += [line(x2, y + 13, 412, y + 13, "lok w3"), t(x2 + 6, y + 34, "กลับ sinus เอง", "xs tok")]
        elif conv:
            out += [t(x2 + 4, y + 18, "⚡", "sm"), line(x2 + 16, y + 13, 412, y + 13, "lok w3")]
            if i == 1: out.append(t(x2 + 4, y + 36, "cardioversion", "xs tok"))
        else:
            out.append(t(404, y + 38, "คุมอัตราอย่างเดียว", "xs end tbad"))
    out += [path("M112 250 H404", "lms w2", "ah-ms"),
            t(112, 268, "ยิ่งนาน ห้องบนยิ่งโต พังผืดมาก → กลับ sinus ยากขึ้น", "xs b tms"),
            t(8, 290, "48 ชม.: ลิ่มเลือดอาจก่อตัวใน LAA แล้ว → ถ้าเกินหรือไม่ทราบ", "xs i2"),
            t(8, 306, "ต้องได้ยาต้านการแข็งตัวก่อนแก้จังหวะ · ทุกระยะเสี่ยง stroke เท่ากัน", "xs i2")]
    return fig("ระยะของ AF ตามเวลาที่เป็นต่อเนื่อง",
               "แบ่งตามระยะเวลาที่ AF คงอยู่ — **paroxysmal** หายเองภายใน 7 วัน · **persistent** อยู่เกิน 7 วันจนต้องทำ cardioversion · "
               "**long-standing persistent** เกิน 1 ปีแต่ยังตั้งใจแก้จังหวะ · **permanent** ตกลงกันว่าไม่แก้จังหวะแล้ว · ห้องบนที่เป็น AF นาน "
               "ยิ่งโตและมีพังผืด จึงมักเลื่อนไปทางขวา · ระยะไม่ได้บอกความเสี่ยง stroke",
               svg(420, 316, "ระยะ paroxysmal persistent long-standing persistent และ permanent ตามระยะเวลาที่ AF เป็นต่อเนื่อง", *out))


# ---------------------------------------------------------------- af-06
def af_virchow():
    out = [box(130, 8, 160, 42, "wa", "เลือดไหลช้า (stasis)\nห้องบนไม่บีบ LA โต", fs=11),
           box(8, 196, 170, 42, "ms", "ผนังห้องบนผิดปกติ\nพังผืด อักเสบ", fs=11),
           box(242, 196, 170, 42, "bad", "เลือดแข็งตัวง่าย\nเกล็ดเลือด · coag ↑", fs=11),
           line(180, 50, 110, 196, "lmu"), line(240, 50, 310, 196, "lmu"), line(178, 217, 242, 217, "lmu"),
           box(150, 112, 120, 40, "bad", "ลิ่มเลือดใน LAA", "b", fs=12),
           line(210, 50, 210, 110, "ln", "ah"), line(130, 196, 178, 154, "ln", "ah"), line(290, 196, 244, 154, "ln", "ah"),
           t(8, 22, "C  HF: ความดัน LA ↑", "xs b"), t(8, 38, "H  HT: LA โต แข็ง", "xs b"),
           t(298, 22, "A  อายุ: LA โต", "xs b"), t(298, 38, "    พังผืดสะสม", "xs b"),
           t(8, 258, "V  หลอดเลือดแข็ง", "xs b"), t(8, 274, "D  เบาหวาน: ผนังเสื่อม", "xs b"),
           t(242, 258, "A  อายุ: เลือดแข็งตัวง่าย", "xs b"), t(242, 274, "D  เบาหวาน: เกล็ดเลือดไว", "xs b"),
           line(8, 290, 412, 290, "lru da"),
           t(8, 310, "S₂ เคยมีลิ่มเลือดหลุดแล้ว = พิสูจน์ว่าเกิดได้ → 2 คะแนน", "xs b tbad"),
           t(8, 328, "Sc หญิง = ตัวปรับความเสี่ยงเมื่อมีปัจจัยอื่น → ESC 2024 ตัดออก", "xs i2")]
    return fig("ทำไมปัจจัยใน CHA₂DS₂-VASc จึงเพิ่มลิ่มเลือด",
               "ลิ่มเลือดใน LAA เกิดจาก **Virchow's triad** — เลือดไหลช้า ผนังผิดปกติ และเลือดแข็งตัวง่าย · ปัจจัยแต่ละตัวในคะแนนเติมมุมใดมุมหนึ่ง "
               "(HF และ HT ทำให้ LA โตและเลือดค้าง · อายุและเบาหวานทำให้ผนังเสื่อมและเลือดแข็งตัวง่าย) ยิ่งมีหลายตัว "
               "ยิ่งเสี่ยงมาก · **เคยเป็น stroke** และ **อายุ ≥ 75** ได้ 2 คะแนนเพราะเพิ่มความเสี่ยงมากที่สุด — การอธิบายรายตัวเป็นกลไกโดยประมาณ",
               svg(420, 336, "Virchow's triad ในห้องบนซ้าย และปัจจัยใน CHA2DS2-VASc ที่เพิ่มแต่ละมุม", *out))


# ---------------------------------------------------------------- af-07
def af_coag():
    out = [rect(8, 8, 404, 70, "sk", 10), t(20, 28, "ตับ", "sm b"),
           t(52, 28, "vitamin K ทำให้ factor II · VII · IX · X ทำงานได้", "xs"),
           pill(20, 40, "Warfarin ✕ วงจร vitamin K", "bad", "xs b mid tbad", w=176),
           t(206, 55, "→ factor 4 ตัวลด · วัดด้วย INR", "xs b"),
           t(20, 72, "แก้: vitamin K (ช้า 12–24 ชม.) · FFP/PCC (ทันที)", "xs tok"),
           line(100, 78, 100, 96, "ln", "ah"),
           box(8, 98, 184, 34, "bx", "VII · IX", fs=12), line(100, 132, 100, 152, "ln", "ah"),
           box(8, 154, 184, 34, "bx", "X → Xa", "b", fs=12.5), line(100, 188, 100, 208, "ln", "ah"),
           box(8, 210, 184, 34, "bx", "II → IIa (thrombin)", "b", fs=12.5), line(100, 244, 100, 264, "ln", "ah"),
           box(8, 266, 184, 40, "bad", "fibrinogen → fibrin\n= ลิ่มเลือด", fs=12),
           box(240, 149, 172, 44, "ac", "-xaban (anti-Xa)\nแก้: PCC / andexanet", fs=11.5),
           line(240, 171, 196, 171, "lac w3"), line(196, 162, 196, 180, "lac w3"),
           box(240, 205, 172, 44, "ac", "Dabigatran (anti-IIa)\nแก้: idarucizumab", fs=11.5),
           line(240, 227, 196, 227, "lac w3"), line(196, 218, 196, 236, "lac w3"),
           t(246, 272, "⊣ = ยับยั้ง", "xs mu")]
    return fig("ยาต้านการแข็งตัวออกฤทธิ์ที่ไหนของ coagulation",
               "**Warfarin** ไปยับยั้งวงจร vitamin K ที่ตับ ทำให้ factor **II VII IX X** ที่ทำงานได้ลดลง (ออกฤทธิ์ช้า ต้องวัด INR) · "
               "**-xaban** จับ **factor Xa** โดยตรง · **dabigatran** จับ **thrombin (IIa)** โดยตรง · ยาแก้ฤทธิ์ตามเป้า: vitamin K "
               "ให้ตับสร้างใหม่ (ช้า) FFP/PCC เติม factor ทันที · idarucizumab เป็นแอนติบอดีจับ dabigatran",
               svg(420, 314, "ตำแหน่งออกฤทธิ์ของ warfarin anti-Xa และ dabigatran บน coagulation cascade พร้อมยาแก้ฤทธิ์", *out))


# ---------------------------------------------------------------- af-08
def af_inr():
    X = lambda v: 50 + (v - 1) * 70
    st = lambda v: 190 - 130 * math.exp(-(v - 1) * 2.2)
    bl = lambda v: 195 - 145 * math.exp(-(6 - v) * 1.1)
    vs = [1 + k * 0.05 for k in range(101)]
    out = [rect(X(2), 30, X(3) - X(2), 170, "ok", 0), t((X(2) + X(3)) / 2, 44, "เป้า 2–3", "xs b mid tok"),
           line(X(1), 200, X(6), 200, "lmu"),
           *[p for v in range(1, 7) for p in (line(X(v), 200, X(v), 204, "lmu"), t(X(v), 218, str(v), "xs mid mu"))],
           t(X(6), 234, "INR", "xs end b mu"), t(46, 24, "อัตราเกิดเหตุ", "xs mu"),
           poly([(X(v), st(v)) for v in vs], "lwa w3"), poly([(X(v), bl(v)) for v in vs], "lbad w3"),
           t(X(1.2), 60, "stroke ↑", "xs b twa"), t(X(1.2), 74, "(ยาไม่พอ)", "xs twa"),
           t(X(5.6), 60, "เลือดออก", "xs b end tbad"), t(X(5.6), 74, "ในสมอง ↑", "xs b end tbad"),
           ar(X(4.2), 256, X(5.4), 256, "lbad w2", "ah-bad"), t(X(4.1), 260, "INR ↑: ยาปฏิชีวนะ amiodarone fluconazole", "xs end tbad"),
           ar(X(2.8), 276, X(1.6), 276, "lwa w2", "ah-wa"), t(X(2.9), 280, "INR ↓: ผักใบเขียว rifampicin ลืมยา", "xs twa")]
    return fig("INR ช่วงเป้าแคบ: ต่ำไปเกิด stroke สูงไปเลือดออก",
               "เมื่อ INR **ต่ำกว่า 2** ยาไม่พอ stroke เพิ่ม · **สูงกว่า 3–4** เลือดออกในสมองเพิ่มชัด ช่วงปลอดภัยจึงแคบ (**2–3**) "
               "สิ่งที่ดัน INR ขึ้นคือยาที่ยับยั้งการทำลาย warfarin หรือลดแบคทีเรียสร้าง vitamin K ในลำไส้ · สิ่งที่ดันลงคือ vitamin K "
               "จากอาหาร ยาที่เร่งการทำลาย warfarin (rifampicin) และการลืมกินยา — จึงต้องถามก่อนปรับขนาดเสมอ",
               svg(420, 290, "กราฟ INR กับอัตรา stroke และเลือดออก ช่วงเป้า 2 ถึง 3 และปัจจัยที่ดัน INR ขึ้นหรือลง", *out))


# ---------------------------------------------------------------- af-09
def af_avnode():
    def row(y, n_out, lab, sub, tc):
        o = [rect(8, y, 120, 70, "ac", 12), t(68, y + 86, "ห้องบน 350–600/นาที", "xs mid i2")]
        import random
        rnd = random.Random(3)
        for k in range(14):
            o.append(circ(22 + rnd.random() * 92, y + 10 + rnd.random() * 50, 2.4, "acf"))
        for k in range(7):
            o.append(line(128, y + 8 + k * 9, 166, y + 35, "lac"))
        o += [circ(180, y + 35, 14, "ms"), t(180, y + 39, "AV", "xs mid b")]
        for k in range(n_out):
            yy = y + 35 + (k - (n_out - 1) / 2) * 12
            o.append(line(194, y + 35, 286, yy, "ln w2", "ah"))
        o += [rect(290, y, 122, 70, "sk", 12), t(351, y + 32, lab, "sm mid b " + tc), t(351, y + 50, sub, "xs mid i2")]
        return o
    out = (row(8, 4, "เร็ว ไม่สม่ำเสมอ", "ใจสั่น CO ↓", "tbad") + row(126, 2, "< 110 ครั้ง/นาที", "ยังเป็น AF", "tok") +
           [t(180, 120, "β-blocker · diltiazem/verapamil · digoxin", "xs mid b tok"),
            t(8, 230, "ยาไม่ได้หยุด AF — แค่ทำให้ AV node ดื้อนานขึ้น (refractory ยาวขึ้น)", "xs i2"),
            t(8, 246, "สัญญาณที่มาถึงตอน AV node ยังดื้อถูกทิ้ง → ผ่านลงห้องล่างน้อยลง", "xs i2")])
    return fig("Rate control: ชะลอที่ AV node",
               "ห้องบนยังส่งสัญญาณ 350–600 ครั้ง/นาทีเหมือนเดิม **AV node** เป็นประตูที่หลังส่งผ่านแต่ละครั้งต้องพัก (refractory) "
               "ยาคุมอัตรา (**β-blocker · non-DHP CCB · digoxin**) ทำให้ช่วงพักยาวขึ้นหรือการนำช้าลง สัญญาณจึงผ่านลงห้องล่างน้อยลง "
               "→ อัตราห้องล่างต่ำกว่า 110 ห้องล่างมีเวลาเติมเลือดมากขึ้น",
               svg(420, 254, "ยาคุมอัตราทำให้ AV node ปล่อยสัญญาณจากห้องบนลงห้องล่างน้อยลง อัตราหัวใจจึงช้าลง", *out))


def af_wpw():
    def heart(x0, blocked):
        o = [rect(x0 + 16, 34, 164, 46, "ac", 12), t(x0 + 98, 62, "AF 350–600/นาที", "xs mid b"),
             rect(x0 + 16, 150, 164, 50, "sk", 12),
             line(x0 + 64, 80, x0 + 64, 106, "ln"), circ(x0 + 64, 116, 11, "ms"), t(x0 + 64, 120, "AV", "xs mid b"),
             line(x0 + 130, 80, x0 + 130, 146, "lbad " + ("w3" if blocked else "w2"), "ah-bad"),
             t(x0 + 138, 108, "accessory", "xs tbad b"), t(x0 + 138, 122, "pathway", "xs tbad b")]
        if blocked:
            o += [line(x0 + 64, 128, x0 + 64, 148, "lmu da"), t(x0 + 84, 122, "✕", "b tbad"),
                  t(x0 + 98, 180, "ทุกสัญญาณลงทางลัด", "xs mid b tbad")]
        else:
            o += [line(x0 + 64, 128, x0 + 64, 146, "ln", "ah"), t(x0 + 98, 180, "ลงได้สองทาง", "xs mid b")]
        return o
    out = (heart(8, False) + heart(216, True) +
           [t(106, 20, "ก่อนให้ยา", "sm b mid"), t(314, 20, "ให้ยากด AV node", "sm b mid tbad"),
            line(212, 14, 212, 206, "lru da"),
            t(106, 226, "QRS กว้าง รูปร่างเปลี่ยนไปมา", "xs mid i2"), t(106, 242, "เร็ว ไม่สม่ำเสมอ", "xs mid i2"),
            box(224, 216, 188, 46, "bad", "ห้องล่างเต้น > 250/นาที\n→ VF หัวใจหยุดเต้น", fs=11.5),
            t(8, 286, "ทางลัดไม่มีการหน่วงสัญญาณแบบ AV node → ห้ามยากด AV node → ablation ทางลัด", "xs b")])
    return fig("Pre-excited AF (WPW): ทำไมห้ามยากด AV node",
               "ใน WPW มี **accessory pathway** ต่อห้องบนกับห้องล่างโดยตรง ซึ่ง **ไม่หน่วงสัญญาณ** เหมือน AV node · เมื่อเกิด AF "
               "สัญญาณบางส่วนลงทางลัดจึงได้ QRS กว้างเร็วมาก · ถ้าให้ β-blocker, CCB, digoxin หรือ adenosine ไปปิด AV node "
               "สัญญาณทั้งหมดจะเทลงทางลัด ห้องล่างเต้นเร็วจนกลายเป็น **VF**",
               svg(420, 296, "Pre-excited AF ใน WPW เมื่อให้ยากด AV node สัญญาณทั้งหมดลง accessory pathway ทำให้ VF", *out))


# ---------------------------------------------------------------- af-10
def af_cv():
    X = lambda w: 60 + (w + 3) * 48
    rec = [(X(0), 120)] + [(X(w / 10), 120 - 62 * (1 - math.exp(-(w / 10) / 1.3))) for w in range(1, 41)]
    out = [t(8, 16, "Elective cardioversion ใน AF > 48 ชม.", "sm b"),
           rect(X(-3), 30, X(4) - X(-3), 18, "ok", 6), t(X(-3) + 8, 43, "ยาต้านการแข็งตัว", "xs b tok"),
           line(X(4), 39, 412, 39, "lok w2", "ah-ok"),
           rect(X(-3), 120, X(0) - X(-3), 8, "badf", 2), t((X(-3) + X(0)) / 2, 142, "AF: ห้องบนไม่บีบ", "xs mid b tbad"),
           rect(X(0), 64, X(4) - X(0), 56, "ms", 0),
           poly(rec, "lok w3"), line(X(4), 58, 412, 58, "lok w3"),
           t(X(1.6), 91, "ห้องบนยัง “ชา”", "xs b tms"), t(X(1.6), 104, "(atrial stunning)", "xs tms"), t(X(1.6), 117, "ลิ่มเลือดยังเกิดได้", "xs tms"),
           t(56, 72, "เส้นเขียว = แรงบีบห้องบน", "xs tok"),
           t(X(0), 112, "⚡", "lg mid"),
           line(X(0), 150, X(0), 160, "lmu"),
           line(56, 160, 412, 160, "lmu"),
           *[p for w in range(-3, 5) for p in (line(X(w), 160, X(w), 164, "lmu"), t(X(w), 178, ("+" if w > 0 else "") + str(w), "xs mid mu"))],
           t(412, 194, "สัปดาห์", "xs end mu"),
           t((X(-3) + X(0)) / 2, 206, "≥ 3 สัปดาห์ก่อน", "xs mid b"), t((X(0) + X(4)) / 2, 206, "≥ 4 สัปดาห์หลัง", "xs mid b"),
           box(8, 220, 404, 44, "wa", "ทางลัด: TEE ไม่เห็นลิ่มเลือดใน LAA → ทำ cardioversion ได้เลย\n(ยังต้องให้ยาหลังทำ 4 สัปดาห์) · Emergency: ช็อกทันที เริ่มยาพร้อมกัน", fs=11)]
    return fig("ยาต้านการแข็งตัวรอบ cardioversion",
               "**3 สัปดาห์ก่อน** ให้ลิ่มเลือดที่อาจซ่อนอยู่ใน LAA ถูกสลายหรือยึดติดผนัง ไม่หลุดตอนห้องบนกลับมาบีบ · หลังช็อก ECG เป็น sinus ทันที "
               "แต่กล้ามเนื้อห้องบน **ยังบีบไม่เต็มที่หลายสัปดาห์ (atrial stunning)** เลือดยังค้าง จึงต้องให้ยาต่อ **อย่างน้อย 4 สัปดาห์** "
               "แล้วต่อระยะยาวตามคะแนนความเสี่ยง · การบีบตัวในภาพเป็นแนวโน้มเชิงคุณภาพ",
               svg(420, 272, "ไทม์ไลน์ยาต้านการแข็งตัว 3 สัปดาห์ก่อนและ 4 สัปดาห์หลัง cardioversion และการบีบตัวของห้องบนที่ฟื้นช้า", *out))


def af_pv():
    def panel(y0, iso):
        cy = y0 + 84
        veins = [(130, cy - 24, 64, cy - 52), (130, cy + 24, 64, cy + 52), (290, cy - 24, 356, cy - 52), (290, cy + 24, 356, cy + 52)]
        o = [ell(210, cy, 128, 54, "ac")]
        for x1, y1, x2, y2 in veins:
            o += [line(x1, y1, x2, y2, "lru w5"), circ(x1, y1, 12, "sk")]
        o += [circ(76, cy - 46, 5, "badf")] + [line(76 + 7 * math.cos(a), cy - 46 + 7 * math.sin(a), 76 + 12 * math.cos(a), cy - 46 + 12 * math.sin(a), "lbad w2")
                                              for a in (0.3, 1.4, 2.5, 3.6, 4.7, 5.8)]
        if iso:
            o += [ell(130, cy, 26, 50, "lok w3 da"), ell(290, cy, 26, 50, "lok w3 da"),
                  line(86, cy - 40, 106, cy - 30, "lbad w2"), t(110, cy - 36, "✕", "b tbad"),
                  t(210, cy + 4, "sinus ยังคุมห้องบน", "xs mid b tok")]
        else:
            o += [path("M88 %s Q 150 %s 196 %s" % (cy - 40, cy - 30, cy - 6), "lbad w2", "ah-bad"),
                  t(210, cy + 18, "AF", "sm mid b tbad")]
        return o
    out = (panel(0, False) + panel(176, True) +
           [t(8, 16, "ก่อน: ไฟฟ้าจาก pulmonary vein ยิงเข้า LA", "sm b"),
            t(412, 160, "ด้านหลังของ LA และ PV ทั้งสี่", "xs end mu"),
            line(8, 170, 412, 170, "lru da"),
            t(8, 192, "หลัง PVI: วงจี้ล้อมรอบ PV ไฟฟ้าออกมาไม่ได้", "sm b tok")])
    return fig("AF ablation: pulmonary vein isolation",
               "จุดยิงไฟฟ้าที่เริ่ม AF ส่วนใหญ่อยู่ใน **ปลอกกล้ามเนื้อที่ยื่นเข้าไปในรูเปิดของ pulmonary vein** · การจี้ (ความร้อนหรือความเย็น) "
               "ทำ **แผลเป็นวงรอบรูเปิด PV** เป็นฉนวนไฟฟ้า จุดยิงยังยิงได้แต่สัญญาณออกมาถึงห้องบนไม่ได้ จังหวะจึงคงเป็น sinus",
               svg(420, 352, "ก่อนและหลัง pulmonary vein isolation จุดยิงไฟฟ้าใน PV ถูกกั้นด้วยวงจี้รอบรูเปิด", *out))


# ---------------------------------------------------------------- af-11
def af_lifestyle():
    rf = ["อ้วน → ไขมันรอบหัวใจ อักเสบ", "HT → ความดัน LA ↑", "OSA → อกติดลบ ดึงห้องบน", "สุรา → พิษต่อเซลล์ห้องบน",
          "DM → พังผืด ผนังเสื่อม"]
    rx = ["ลดน้ำหนัก ≥ 10%", "คุมความดัน ACEI/ARB", "วินิจฉัยและรักษา OSA", "เลี่ยงดื่มหนัก / เลิก", "HbA1c < 6.5% · SGLT2i",
          "ออกกำลัง 150–300 นาที/สัปดาห์"]
    out = []
    for k, s in enumerate(rf):
        y = 8 + 38 * k
        out += [box(8, y, 196, 30, "ms", s, fs=11), line(204, y + 15, 254, 96, "lmu")]
    patches = [(300, 70), (340, 60), (352, 106), (318, 124), (284, 104), (330, 88)]
    out += [ell(330, 96, 72, 56, "ac")] + [rect(x - 7, y - 3, 14, 6, "inkf", 2) for x, y in patches]
    out += [t(330, 170, "LA โต พังผืด อักเสบ", "xs mid b"), t(330, 184, "AF กลับเป็นซ้ำบ่อย", "xs mid b tbad"),
            line(330, 192, 330, 226, "lok w3", "ah-ok"),
            ell(330, 268, 48, 38, "ac")] + [rect(x - 7, y - 3, 14, 6, "inkf", 2) for x, y in ((318, 262), (344, 276))]
    out += [t(330, 322, "LA เล็กลง AF ซ้ำ ↓", "xs mid b tok"), t(330, 336, "ablation ได้ผลดีขึ้น", "xs mid b tok"),
            t(8, 214, "คุมปัจจัยเสี่ยง (C ใน ABC):", "xs b tok")]
    for k, s in enumerate(rx):
        out.append(t(16, 234 + 18 * k, "✓ " + s, "xs tok"))
    return fig("คุมโรคร่วมแล้วห้องบนดีขึ้นได้",
               "โรคร่วมแต่ละตัวทำร้ายห้องบนคนละทาง — ยืดห้องบน เพิ่มการอักเสบจากไขมันรอบหัวใจ สร้างพังผืด · substrate นี้ **ย้อนกลับได้บางส่วน** "
               "เมื่อลดน้ำหนัก คุมความดัน รักษา OSA และงดสุรา ห้องบนเล็กลง AF กลับเป็นซ้ำน้อยลงและ ablation ได้ผลดีขึ้น "
               "(จุดดำ = พังผืด)",
               svg(420, 344, "โรคร่วมทำให้ห้องบนโตและมีพังผืด การคุมปัจจัยเสี่ยงทำให้ห้องบนเล็กลงและ AF กลับเป็นซ้ำน้อยลง", *out))
