# -*- coding: utf-8 -*-
"""ตัวช่วยวาดแผนภาพ SVG สำหรับบทเรียน (section.figs) — ใช้คลาสสีที่ index.html กำหนดไว้ จึงสลับโหมดสว่าง/มืดได้เอง

    from svg import *
    figs = {"podocyte": fig("ชื่อภาพ", "คำอธิบายใต้ภาพ (ใช้ **ตัวหนา** ได้)",
            svg(560, 300, "สิ่งที่ภาพนี้บอก (aria-label)",
                box(20, 20, 140, 50, "ac", "Podocyte\\nfoot process"),
                ar(160, 45, 240, 45, "lac", "ah-ac", "สูญเสีย"),
                t(20, 290, "หมายเหตุ", "sm mu")))}
    แล้วใส่บรรทัด [[fig:podocyte]] ใน md ของหัวข้อตรงตำแหน่งที่ต้องการให้ภาพขึ้น

คลังคลาส (ดู CSS ".fig" ใน index.html)
  กล่อง (fill+stroke): bx sk ac ok bad ms wa      ทึบ: acf okf badf msf waf inkf muf ruf paf
  เส้น: ln lmu lac lok lbad lms lwa lru · ความหนา w2 w3 w5 · ประ da dt · ns = ไม่มีเส้นขอบ
  ตัวอักษร: lg sm xs b mid end · สี mu i2 tac tok tbad tms twa tpa
  ลูกศร (marker): ah ah-ac ah-ok ah-bad ah-ms ah-wa ah-mu
กฎ: ไม่มี id ใน svg · ข้อความสั้น (คำอธิบายยาวไปไว้ใน cap) · ภาพแนวตั้งกว้าง ≤ 420 อ่านบนมือถือได้ไม่ต้องเลื่อน ·
ภาพกว้าง > 440 บนมือถือจะเลื่อนซ้าย-ขวาได้"""

__all__ = ["fig", "svg", "t", "box", "ar", "line", "path", "circ", "ell", "rect", "g", "poly", "esc", "pill", "brace"]


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def _n(v):
    v = round(float(v), 1)
    return str(int(v)) if v == int(v) else str(v)


def fig(title, cap, svg_src):
    return {"title": title, "cap": cap, "svg": svg_src}


def svg(w, h, label, *parts):
    return ('<svg viewBox="0 0 %s %s" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg">' % (_n(w), _n(h), esc(label))
            + "".join(p for p in parts if p) + "</svg>")


def t(x, y, s, c="", lh=1.25, fs=None):
    """ข้อความ — "\\n" ขึ้นบรรทัดใหม่ (tspan) · y คือ baseline ของบรรทัดแรก"""
    lines = str(s).split("\n")
    cls = (' class="%s"' % c) if c else ""
    st = (' style="font-size:%spx"' % _n(fs)) if fs else ""
    if len(lines) == 1:
        return '<text x="%s" y="%s"%s%s>%s</text>' % (_n(x), _n(y), cls, st, esc(s))
    sp = "".join('<tspan x="%s" dy="%s">%s</tspan>' % (_n(x), "0" if i == 0 else "%sem" % lh, esc(ln))
                 for i, ln in enumerate(lines))
    return '<text x="%s" y="%s"%s%s>%s</text>' % (_n(x), _n(y), cls, st, sp)


def rect(x, y, w, h, c="bx", r=8, extra=""):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" class="%s"%s/>' % (_n(x), _n(y), _n(w), _n(h), _n(r), c, extra)


def box(x, y, w, h, c="bx", text=None, tc="", r=8, fs=13, lh=1.25):
    """กล่องพร้อมข้อความกึ่งกลาง (หลายบรรทัดด้วย \\n)"""
    out = rect(x, y, w, h, c, r)
    if text:
        n = len(str(text).split("\n"))
        y0 = y + h / 2 - (n - 1) * fs * lh / 2 + fs * 0.36
        out += t(x + w / 2, y0, text, ("mid " + tc).strip(), lh, fs if fs != 13 else None)
    return out


def line(x1, y1, x2, y2, c="ln", m=None):
    mk = (' marker-end="url(#%s)"' % m) if m else ""
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" class="%s"%s/>' % (_n(x1), _n(y1), _n(x2), _n(y2), c, mk)


def ar(x1, y1, x2, y2, c="ln", m="ah", label=None, lc="sm i2 mid", dx=0, dy=-6):
    """ลูกศรพร้อมป้ายกลางเส้น"""
    out = line(x1, y1, x2, y2, c, m)
    if label:
        out += t((x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy, label, lc)
    return out


def path(d, c="ln", m=None, ms=None):
    mk = (' marker-end="url(#%s)"' % m) if m else ""
    mk += (' marker-start="url(#%s)"' % ms) if ms else ""
    return '<path d="%s" class="%s"%s/>' % (d, c, mk)


def poly(pts, c="ln", closed=False, m=None):
    tag = "polygon" if closed else "polyline"
    mk = (' marker-end="url(#%s)"' % m) if m else ""
    return '<%s points="%s" class="%s"%s/>' % (tag, " ".join("%s,%s" % (_n(a), _n(b)) for a, b in pts), c, mk)


def circ(cx, cy, r, c="bx"):
    return '<circle cx="%s" cy="%s" r="%s" class="%s"/>' % (_n(cx), _n(cy), _n(r), c)


def ell(cx, cy, rx, ry, c="bx", rot=None):
    tr = (' transform="rotate(%s %s %s)"' % (_n(rot), _n(cx), _n(cy))) if rot else ""
    return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" class="%s"%s/>' % (_n(cx), _n(cy), _n(rx), _n(ry), c, tr)


def g(*parts, tr=None, c=None):
    a = (' transform="%s"' % tr) if tr else ""
    a += (' class="%s"' % c) if c else ""
    return "<g%s>%s</g>" % (a, "".join(p for p in parts if p))


def pill(x, y, s, c="ac", tc="sm b mid tac", w=None, h=22):
    """ป้ายมน (x,y = มุมซ้ายบน) — กว้างตามความยาวข้อความโดยประมาณถ้าไม่ระบุ w"""
    w = w or max(36, 7.2 * len(str(s)) + 18)
    return rect(x, y, w, h, c, h / 2) + t(x + w / 2, y + h / 2 + 4, s, tc)


def brace(x, y1, y2, c="lmu", side=1, d=7):
    """วงเล็บปีกกาแนวตั้งจาก y1 ถึง y2 (side=1 ปลายแหลมชี้ขวา · -1 ชี้ซ้าย)"""
    m, e = (y1 + y2) / 2, d * side
    return path("M%s %s Q%s %s %s %s L%s %s Q%s %s %s %s Q%s %s %s %s L%s %s Q%s %s %s %s" % tuple(_n(v) for v in (
        x, y1, x + e, y1, x + e, y1 + d, x + e, m - d, x + e, m, x + 2 * e, m,
        x + e, m, x + e, m + d, x + e, y2 - d, x + e, y2, x, y2)), c)
