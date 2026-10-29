#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ดึงภาพรังสีจริงจากสไลด์ "Image in chest" (อ.พจนี · Potjanee Korrungruang, MD) → artifact/img/chest/*.jpg

    python3 -I artifact/tools/extract_chestimg.py "<path>/Image in chest.pdf" [--sheet <contact.png>]

- ไฟล์ PDF เป็นสไลด์ที่ผู้ใช้ export จาก iPad พร้อมลายมือจดในห้อง → ลบ "หมึกของผู้ใช้" ออกก่อนตัดภาพ
  หมึกจาก iPad อยู่ใน content stream เป็นกลุ่ม  q <cm> /Cs CS <rgb> SCN 1 J 1 j <w> w <path> S Q
  (เส้นปลายมน round cap) ส่วนลูกศร/วง/ป้ายของอาจารย์เป็นภาพซ้อนหรือ path แบบ fill จึงยังอยู่ครบ
- ตัดภาพด้วยการ render เฉพาะกรอบ (clip) ที่ 200 dpi → ตัดขอบขาว → ย่อกว้างไม่เกิน 900 px → JPEG q78
- รายการภาพ (หน้า กรอบเป็นหน่วย pt ของหน้า 792×594) อยู่ใน SPEC — key ตรงกับ section.imgs ใน build_chestimg.py
"""
import io, os, re, sys

import pymupdf
from PIL import Image

TOOLS = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(TOOLS), "img", "chest")

# (ชื่อไฟล์, หน้า, (x0, y0, x1, y1) หน่วย pt)
SPEC = [
    ("cxr-01-pa-upright", 5, (155, 0, 637, 594)),
    ("cxr-02-ap-supine", 7, (100, 0, 720, 594)),
    ("cxr-03-pa-vs-ap", 8, (0, 93, 792, 501)),
    ("cxr-04-supine-effusion", 14, (91, 20, 700, 500)),
    ("cxr-05-decubitus", 15, (35, 0, 757, 594)),
    ("cxr-06-lordotic", 17, (0, 0, 792, 545)),
    ("cxr-07-exposure", 21, (7, 96, 791, 500)),
    ("cxr-08-inspiration", 23, (0, 90, 792, 526)),
    ("cxr-09-rotation", 25, (272, 0, 792, 594)),
    ("cxr-10-magnification", 26, (0, 118, 792, 541)),
    ("cxr-11-angulation", 27, (0, 127, 792, 583)),
    ("cxr-12-densities", 29, (108, 0, 683, 594)),
    ("cxr-13-anatomy-diagram", 34, (0, 0, 792, 594)),
    ("cxr-14-lateral-spaces", 38, (205, 97, 587, 580)),
    ("cxr-15-soft-tissue", 43, (109, 0, 652, 594)),
    ("cxr-16-skin-fold", 44, (89, 0, 702, 594)),
    ("cxr-17-mastectomy", 45, (0, 75, 792, 518)),
    ("cxr-18-subcut-emphysema", 46, (0, 0, 792, 545)),
    ("cxr-19-ctr", 48, (20, 103, 480, 573)),
    ("cxr-20-hilum", 49, (0, 77, 438, 533)),
    ("cxr-21-diaphragm", 52, (0, 8, 792, 586)),
    ("cxr-22-visceral-line", 54, (102, 0, 689, 594)),
    ("cxr-23-rul-consolidation", 72, (102, 0, 689, 540)),
    ("cxr-24-ards", 73, (52, 0, 740, 495)),
    ("cxr-25-diffuse-ggo", 74, (76, 0, 716, 520)),
    ("cxr-26-air-bronchogram", 75, (40, 170, 750, 440)),
    ("cxr-27-ggo", 76, (323, 246, 790, 581)),
    ("cxr-28-consol-vs-ggo", 77, (0, 0, 792, 594)),
    ("cxr-29-silhouette-lobes", 81, (0, 120, 792, 555)),
    ("cxr-30-rul-pa-lat", 84, (56, 176, 710, 526)),
    ("cxr-31-rml-consolidation", 86, (68, 165, 736, 550)),
    ("cxr-32-rll-consolidation", 88, (46, 181, 744, 531)),
    ("cxr-33-lul-consolidation", 89, (402, 180, 750, 535)),
    ("cxr-34-lll-consolidation", 91, (40, 184, 752, 531)),
    ("cxr-35-reticular", 93, (0, 0, 792, 594)),
    ("cxr-36-diffuse-nodular", 96, (128, 0, 663, 530)),
    ("cxr-37-miliary", 97, (20, 180, 740, 475)),
    ("cxr-38-reticulonodular", 99, (40, 0, 750, 530)),
    ("cxr-39-rul-atelectasis", 105, (315, 148, 732, 568)),
    ("cxr-40-golden-s", 106, (401, 153, 782, 548)),
    ("cxr-41-rml-atelectasis", 108, (4, 171, 423, 584)),
    ("cxr-42-rml-lateral", 109, (432, 152, 752, 563)),
    ("cxr-43-rll-atelectasis", 111, (415, 43, 762, 426)),
    ("cxr-44-luftsichel", 115, (40, 168, 397, 544)),
    ("cxr-45-lul-lateral", 116, (56, 134, 344, 548)),
    ("cxr-46-lll-atelectasis", 118, (38, 113, 348, 463)),
    ("cxr-47-lll-lateral", 119, (52, 153, 357, 560)),
    ("cxr-48-platelike", 120, (44, 219, 744, 498)),
    ("cxr-49-rounded-atelectasis", 122, (355, 173, 756, 536)),
    ("cxr-50-nodule-mass", 124, (0, 112, 792, 594)),
    ("cxr-51-intraparenchymal", 126, (6, 108, 788, 570)),
    ("cxr-52-extrapulmonary", 127, (47, 158, 747, 558)),
    ("cxr-53-extrapleural-rib", 128, (36, 154, 378, 561)),
    ("cxr-54-cavity", 131, (27, 181, 462, 536)),
    ("cxr-55-scc-cavity", 132, (123, 156, 738, 546)),
    ("cxr-56-pjp-cysts", 135, (178, 162, 636, 476)),
    ("cxr-57-lung-abscess", 136, (26, 124, 792, 594)),
    ("cxr-58-bullae", 143, (37, 136, 742, 458)),
    ("cxr-59-westermark", 146, (201, 115, 590, 410)),
    ("cxr-60-tram-tracks", 152, (10, 96, 760, 561)),
    ("cxr-61-overinflation", 161, (0, 0, 792, 594)),
    ("cxr-62-bullous-emphysema", 162, (108, 120, 670, 424)),
    ("cxr-63-mediastinal-structures", 165, (487, 141, 778, 572)),
    ("cxr-64-felson", 166, (43, 163, 288, 550)),
    ("cxr-65-anterior-mediastinal", 168, (208, 166, 523, 566)),
    ("cxr-66-posterior-mediastinal", 169, (150, 125, 630, 565)),
    ("cxr-67-infarction", 172, (13, 118, 770, 454)),
    ("cxr-68-acute-pe-ct", 173, (0, 155, 792, 560)),
    ("cxr-69-pht-ct", 177, (138, 127, 630, 540)),
    ("cxr-70-meniscus", 181, (20, 35, 422, 420)),
    ("cxr-71-decubitus-fluid", 182, (31, 170, 471, 545)),
    ("cxr-72-massive-effusion", 183, (158, 0, 634, 594)),
    ("cxr-73-subpulmonic", 184, (188, 121, 603, 474)),
    ("cxr-74-loculated", 185, (198, 155, 595, 562)),
    ("cxr-75-pneumothorax", 187, (20, 124, 398, 586)),
    ("cxr-76-early-tension", 188, (333, 171, 758, 553)),
    ("cxr-77-large-ptx-left", 189, (108, 0, 683, 594)),
    ("cxr-78-ptx-right", 190, (141, 0, 650, 594)),
    ("cxr-79-ptx-size", 191, (55, 153, 760, 562)),
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
    args = sys.argv[1:]
    sheet = None
    if "--sheet" in args:
        i = args.index("--sheet"); sheet = args[i + 1]; del args[i:i + 2]
    pdf = args[0]
    doc = pymupdf.open(pdf)
    os.makedirs(OUT, exist_ok=True)
    cleaned, made = set(), []
    for name, pg, rect in SPEC:
        page = doc[pg - 1]
        if pg not in cleaned:
            strip_ink(doc, page); cleaned.add(pg)
        pix = page.get_pixmap(dpi=200, clip=pymupdf.Rect(*rect) & page.rect)
        im = trim_white(Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB"))
        if im.width > 900:
            im = im.resize((900, round(im.height * 900 / im.width)), Image.LANCZOS)
        if im.height > 1000:
            im = im.resize((round(im.width * 1000 / im.height), 1000), Image.LANCZOS)
        path = os.path.join(OUT, name + ".jpg")
        im.save(path, "JPEG", quality=78, optimize=True, progressive=True)
        made.append((name, im.size, os.path.getsize(path)))
    total = sum(s for _, _, s in made)
    for n, sz, s in made:
        print("%-34s %4dx%-4d %6.1f KB" % (n, sz[0], sz[1], s / 1024))
    print("%d ภาพ · รวม %.2f MB" % (len(made), total / 1048576))
    if sheet:  # ภาพรวมสำหรับตรวจด้วยตา
        th = []
        for n, _, _ in made:
            im = Image.open(os.path.join(OUT, n + ".jpg")); im.thumbnail((300, 260)); th.append((n, im))
        cols, cw, ch = 5, 310, 285
        rows = (len(th) + cols - 1) // cols
        from PIL import ImageDraw
        S = Image.new("RGB", (cols * cw, rows * ch), "white")
        dr = ImageDraw.Draw(S)
        for k, (n, im) in enumerate(th):
            x, y = (k % cols) * cw, (k // cols) * ch
            S.paste(im, (x + 5, y + 18)); dr.text((x + 5, y + 3), n, fill="red")
        S.save(sheet)


if __name__ == "__main__":
    main()
