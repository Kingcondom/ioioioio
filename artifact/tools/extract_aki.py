#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ดึงภาพจริงจากสไลด์ "AKI year 4 update 2569" (พญ.วรรณิยา มีนุ่น · รพ.ราชวิถี) → artifact/img/nephro/aki-NN-*.jpg

    python3 -I artifact/tools/extract_aki.py "<path>/AKI year 4 update 2569.pdf" [--sheet <contact.png>]

- PDF เป็นสไลด์ที่ผู้ใช้ export จาก iPad พร้อมลายมือจดในห้อง → ลบ "หมึกของผู้ใช้" ออกก่อนตัดภาพ
  หมึกอยู่ใน content stream (หลัง clean_contents) เป็นกลุ่ม  q <cm> /Cs CS <rgb> SCN 1 J 1 j <w> w ... S Q  (round cap/join)
  เหมือนไฟล์ chest · ลูกศร/ป้าย/ตัวเลขของอาจารย์อยู่ในภาพฝังหรือเป็น path แบบ fill จึงยังอยู่ครบ
- render เฉพาะกรอบ (clip) ที่ 200 dpi → ตัดขอบขาว → ย่อกว้างไม่เกิน 900 px → JPEG q78 (ลดคุณภาพทีละขั้นถ้าเกิน 150 KB)
- รายการภาพ (หน้า, กรอบหน่วย pt ของหน้า 720×540) อยู่ใน SPEC — ลำดับ = เลขในชื่อไฟล์ = key i<NN> ใน build_aki.py
"""
import io, os, re, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(TOOLS), "img", "nephro")

# (ชื่อไฟล์, หน้า, (x0, y0, x1, y1) หน่วย pt)
SPEC = [
    ("aki-01-normal-glomerulus", 16, (0, 0, 720, 540)),
    ("aki-02-rpgn-crescent", 20, (36, 123, 720, 531)),
    ("aki-03-ain-histology", 24, (9, 112, 720, 540)),
    ("aki-04-wbc-cast-eosinophiluria", 26, (292, 26, 689, 502)),
    ("aki-05-atn-histology", 29, (0, 112, 720, 540)),
    ("aki-06-myoglobin-cast", 30, (0, 123, 720, 540)),
    ("aki-07-pnh-hemosiderin", 31, (14, 128, 706, 540)),
    ("aki-08-red-urine-algorithm", 33, (0, 0, 720, 502)),
    ("aki-09-cipro-crystal", 36, (9, 227, 720, 487)),
    ("aki-10-drug-crystals", 38, (20, 4, 720, 536)),
    ("aki-11-urine-crystals", 39, (50, 18, 704, 534)),
    ("aki-12-film-kub", 53, (14, 15, 447, 502)),
    ("aki-13-film-ivp", 55, (16, 21, 405, 514)),
    ("aki-14-us-kidney", 56, (0, 0, 720, 540)),
    ("aki-15-us-kidney-size", 57, (0, 0, 720, 540)),
    ("aki-16-ecg-hyperk-patterns", 60, (70, 165, 675, 445)),
    ("aki-17-ecg-sine-wave", 61, (45, 180, 680, 365)),
    ("aki-18-ecg-hyperk-12lead", 62, (0, 112, 720, 531)),
    ("aki-19-complication-table", 66, (0, 0, 711, 540)),
    ("aki-20-complication-table-2", 70, (34, 9, 701, 514)),
]

INK = re.compile(rb"(?<![A-Za-z])q\s+(?:[-\d.]+\s+){6}cm\s+/\w+\s+CS\s+(?:[-\d.]+\s+){1,4}SCN?\s+1\s+J\s+1\s+j\s")
TOK = re.compile(rb"(?<![^\s\]\[(){}<>/])([qQ])(?![^\s\]\[(){}<>/])")


def strip_ink(doc, page):
    """ลบกลุ่มเส้นปากกา round-cap ของผู้ใช้ออกจาก content stream (ไม่แตะภาพและ path แบบ fill)"""
    page.clean_contents()
    xs = page.get_contents()
    s = b"".join(doc.xref_stream(x) for x in xs)
    out, pos, n = [], 0, 0
    while True:
        m = INK.search(s, pos)
        if not m:
            break
        depth, end = 0, len(s)
        for t in TOK.finditer(s, m.start()):
            depth += 1 if t.group(1) == b"q" else -1
            if depth == 0:
                end = t.end()
                break
        out.append(s[pos:m.start()])
        pos, n = end, n + 1
    out.append(s[pos:])
    doc.update_stream(xs[0], b"".join(out))
    for x in xs[1:]:
        doc.update_stream(x, b"")
    return n


def trim_white(im, thr=246, pad=2):
    g = im.convert("L").point(lambda v: 255 if v < thr else 0)
    bb = g.getbbox()
    if not bb:
        return im
    x0, y0, x1, y1 = bb
    return im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad)))


def main():
    import pymupdf
    from PIL import Image
    args = sys.argv[1:]
    sheet = None
    if "--sheet" in args:
        i = args.index("--sheet"); sheet = args[i + 1]; del args[i:i + 2]
    doc = pymupdf.open(args[0])
    os.makedirs(OUT, exist_ok=True)
    cleaned, made = {}, []
    for name, pg, rect in SPEC:
        page = doc[pg - 1]
        if pg not in cleaned:
            cleaned[pg] = strip_ink(doc, page)
        pix = page.get_pixmap(dpi=200, clip=pymupdf.Rect(*rect) & page.rect)
        im = trim_white(Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB"))
        if im.width > 900:
            im = im.resize((900, round(im.height * 900 / im.width)), Image.LANCZOS)
        if im.height > 900:
            im = im.resize((round(im.width * 900 / im.height), 900), Image.LANCZOS)
        path = os.path.join(OUT, name + ".jpg")
        for q in (78, 72, 66, 60):
            im.save(path, "JPEG", quality=q, optimize=True, progressive=True)
            if os.path.getsize(path) < 150 * 1024:
                break
        made.append((name, pg, cleaned[pg], im.size, os.path.getsize(path), q))
    total = sum(m[4] for m in made)
    for n, pg, ink, sz, s, q in made:
        print("%-34s p%-3d ink%-2d %4dx%-4d %6.1f KB q%d" % (n, pg, ink, sz[0], sz[1], s / 1024, q))
    print("%d ภาพ · รวม %.2f MB" % (len(made), total / 1048576))
    if sheet:  # ภาพรวมสำหรับตรวจด้วยตา
        from PIL import ImageDraw
        th = []
        for m in made:
            im = Image.open(os.path.join(OUT, m[0] + ".jpg")); im.thumbnail((300, 260)); th.append((m[0], im))
        cols, cw, ch = 5, 310, 285
        rows = (len(th) + cols - 1) // cols
        S = Image.new("RGB", (cols * cw, rows * ch), "white")
        dr = ImageDraw.Draw(S)
        for k, (n, im) in enumerate(th):
            x, y = (k % cols) * cw, (k // cols) * ch
            S.paste(im, (x + 5, y + 18)); dr.text((x + 5, y + 3), n, fill="red")
        S.save(sheet)


if __name__ == "__main__":
    main()
