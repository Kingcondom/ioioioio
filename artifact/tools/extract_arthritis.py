#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ดึงภาพจริงจากสไลด์ "Approach to Arthritis" (อ.กิตติวรรณ สุเมธกุล · Lec 2.1) และสไลด์เคส ARTHRITIS (กลุ่ม 19B/20B)
→ artifact/img/air/art-NN-<slug>.jpg  (ใช้ใน section.imgs ของคาบ air 23 ผ่าน update_arthritis.py)

    python3 -I artifact/tools/extract_arthritis.py <slides.pdf> <case.pdf> [--sheet <contact.png>]

- สไลด์อาจารย์เป็นไฟล์ที่ผู้ใช้ export จาก iPad พร้อมลายมือ → ลบหมึกของผู้ใช้ (strip_ink ของ extract_chestimg.py)
  ก่อน render · ลูกศร/วงสีแดงที่ฝังอยู่ในภาพของอาจารย์ยังอยู่ครบ
- กรอบเป็นหน่วย pt ของหน้า (สไลด์ 612×459 · เคส 1440×810) · render 200 dpi → ตัดขอบขาว → กว้าง ≤ 900 px → JPEG q80
- ไม่มีภาพที่ระบุตัวผู้ป่วย (ภาพมือ/ภาพรังสีไม่มีชื่อหรือ HN)
"""
import io, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
from extract_chestimg import strip_ink, trim_white  # noqa: E402

OUT = os.path.join(os.path.dirname(TOOLS), "img", "air")

# (ชื่อไฟล์, "s"=สไลด์อาจารย์ | "c"=สไลด์เคส | "x"=ภาพดิบในสไลด์เคส, หน้า, กรอบ pt หรือ xref)
SPEC = [
    ("art-01-ra-xray-stages", "s", 59, (0, 224, 592, 446)),
    ("art-02-ra-marginal-erosion", "s", 69, (11, 97, 602, 362)),
    ("art-03-atlantoaxial", "s", 64, (0, 219, 612, 449)),
    ("art-04-gout-xray", "s", 38, (108, 22, 514, 326)),
    ("art-05-gout-us", "s", 43, (0, 148, 352, 414)),
    ("art-06-msu-microscopy", "s", 40, (84, 263, 572, 442)),
    ("art-07-crystals-polarized", "x", 20, 687),  # ภาพดิบ (xref) — ในหน้าถูกตัดเป็นสองกรอบ
    ("art-08-sacroiliitis", "s", 77, (66, 71, 515, 440)),
    ("art-09-bamboo-spine", "s", 78, (107, 71, 520, 445)),
    ("art-10-tophaceous-hands", "s", 37, (0, 17, 405, 216)),
    ("art-11-swan-boutonniere", "c", 15, (49, 171, 1375, 639)),
]


def main():
    import pymupdf
    from PIL import Image
    args = sys.argv[1:]
    sheet = None
    if "--sheet" in args:
        i = args.index("--sheet"); sheet = args[i + 1]; del args[i:i + 2]
    docs = {"s": pymupdf.open(args[0]), "c": pymupdf.open(args[1])}
    os.makedirs(OUT, exist_ok=True)
    cleaned, made = set(), []
    for name, which, pg, rect in SPEC:
        if which == "x":  # ภาพดิบจากสไลด์เคสตาม xref
            raw = docs["c"].extract_image(rect)
            im = Image.open(io.BytesIO(raw["image"])).convert("RGB")
            path = os.path.join(OUT, name + ".jpg")
            im.save(path, "JPEG", quality=80, optimize=True, progressive=True)
            made.append((name, im.size, os.path.getsize(path), 80))
            continue
        doc = docs[which]
        page = doc[pg - 1]
        if (which, pg) not in cleaned:
            n = strip_ink(doc, page)
            cleaned.add((which, pg))
            if n:
                print("  ลบหมึกผู้ใช้ %s หน้า %d: %d กลุ่ม" % (which, pg, n))
        pix = page.get_pixmap(dpi=200 if which == "s" else 110, clip=pymupdf.Rect(*rect) & page.rect)
        im = trim_white(Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB"))
        if im.width > 900:
            im = im.resize((900, round(im.height * 900 / im.width)), Image.LANCZOS)
        if im.height > 900:
            im = im.resize((round(im.width * 900 / im.height), 900), Image.LANCZOS)
        path = os.path.join(OUT, name + ".jpg")
        q = 80
        while True:
            im.save(path, "JPEG", quality=q, optimize=True, progressive=True)
            if os.path.getsize(path) < 150 * 1024 or q <= 60:
                break
            q -= 5
        made.append((name, im.size, os.path.getsize(path), q))
    total = sum(m[2] for m in made)
    for n, sz, s, q in made:
        print("%-30s %4dx%-4d %6.1f KB q%d" % (n, sz[0], sz[1], s / 1024, q))
    print("%d ภาพ · รวม %.2f MB" % (len(made), total / 1048576))
    if sheet:
        from PIL import ImageDraw
        th = []
        for n, *_ in made:
            im = Image.open(os.path.join(OUT, n + ".jpg")); im.thumbnail((440, 300)); th.append((n, im))
        cols, cw, ch = 3, 450, 325
        rows = (len(th) + cols - 1) // cols
        S = Image.new("RGB", (cols * cw, rows * ch), "white")
        dr = ImageDraw.Draw(S)
        for k, (n, im) in enumerate(th):
            x, y = (k % cols) * cw, (k // cols) * ch
            S.paste(im, (x + 5, y + 20)); dr.text((x + 5, y + 4), n, fill="red")
        S.save(sheet)


if __name__ == "__main__":
    main()
