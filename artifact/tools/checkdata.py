#!/usr/bin/env python3
"""ตรวจความสมบูรณ์ของ artifact/data/*.json โดยไม่ต้องเปิดเบราว์เซอร์

verify.py ตรวจว่า "หน้าเว็บทำงานถูก" — ไฟล์นี้ตรวจว่า "ข้อมูลที่ป้อนเข้าไปไม่พัง"
ซึ่งเป็นความพังที่เงียบที่สุด: [[fig:x]] ที่ไม่มีรูป · รหัส นล. ที่ไม่มีในพจนานุกรม ·
ตารางที่คอลัมน์ไม่เท่ากัน · ** ที่ไม่ปิด · ไฟล์รูปที่หาย — ทุกอย่างนี้ไม่ทำให้หน้าพัง
จึงไม่มีเทสต์ไหนจับได้ แต่ผู้ใช้เห็นเป็นช่องว่างหรือข้อความดิบ

    python3 artifact/tools/checkdata.py          # ตรวจทุกชุด
    python3 artifact/tools/checkdata.py nephro   # ตรวจชุดเดียว

ออก 0 = ผ่าน · 1 = มี error (ของที่พังจริง) · warning ไม่ทำให้ fail
"""
import glob
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # artifact/
DATA = os.path.join(ROOT, "data")
MARK = re.compile(r"\[\[(fig|anim|img):([^\]]+)\]\]")
# ชุด key ของ section ที่เก็บ markdown ให้ตรวจ (ตัว md หลักและคำอธิบายในข้อสอบ)
TEXT_KEYS = ("md", "summary", "explain", "pearl", "cap", "stem", "mnem")

errors, warns = [], []


def err(where, msg):
    errors.append(f"{where}: {msg}")


def warn(where, msg):
    warns.append(f"{where}: {msg}")


def texts(obj):
    """ไล่เก็บสตริงทุกตัวใน object พร้อม path หยาบ ๆ ไว้อ้างอิง"""
    if isinstance(obj, dict):
        for k, v in obj.items():
            for p, s in texts(v):
                yield (f"{k}.{p}" if p else k), s
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            for p, s in texts(v):
                yield (f"[{i}].{p}" if p else f"[{i}]"), s
    elif isinstance(obj, str):
        yield "", obj


def check_markers(where, sec):
    """[[fig:x]] [[anim:x]] [[img:x]] ต้องมีของจริงใน section เดียวกัน"""
    pools = {"fig": sec.get("figs") or {}, "anim": sec.get("anims") or {},
             "img": sec.get("imgs") or {}}
    used = {k: set() for k in pools}
    for path, s in texts(sec):
        for kind, name in MARK.findall(s):
            used[kind].add(name)
            if name not in pools[kind]:
                err(where, f"[[{kind}:{name}]] ใน {path or 'md'} ไม่มีของจริงใน "
                           f"{kind}s (มี: {', '.join(sorted(pools[kind])) or 'ไม่มีเลย'})")
    for kind, pool in pools.items():
        for name in sorted(set(pool) - used[kind]):
            warn(where, f"{kind} '{name}' ประกาศไว้แต่ไม่มี [[{kind}:{name}]] "
                        f"ที่ไหนเลย จะไม่ถูกแสดง")


def check_svg(where, sec):
    for kind in ("figs", "anims"):
        for name, fig in (sec.get(kind) or {}).items():
            svg = fig.get("svg") if isinstance(fig, dict) else None
            if not svg:
                continue
            try:
                ET.fromstring(svg)
            except ET.ParseError as e:
                err(where, f"{kind}.{name} svg parse ไม่ผ่าน: {e}")


def check_img_files(where, sec):
    for name, im in (sec.get("imgs") or {}).items():
        src = im.get("src") if isinstance(im, dict) else None
        if not src:
            err(where, f"imgs.{name} ไม่มี src")
            continue
        if not os.path.exists(os.path.join(ROOT, src)):
            err(where, f"imgs.{name} src ชี้ไปที่ไฟล์ที่ไม่มี: {src}")


def check_tables(where, sec):
    """ตารางใน markdown — จำนวนคอลัมน์ต้องเท่าหัวตาราง"""
    for path, s in texts(sec):
        if "|" not in s:
            continue
        lines = s.split("\n")
        head = None
        for n, raw in enumerate(lines, 1):
            line = raw.strip()
            if not line.startswith("|"):
                head = None
                continue
            cells = len(line.strip("|").split("|"))
            if head is None:
                head = cells
                continue
            if re.fullmatch(r"\|[\s:|-]+\|?", line):
                if cells != head:
                    err(where, f"{path or 'md'} บรรทัด {n}: เส้นคั่นตารางมี "
                               f"{cells} คอลัมน์ แต่หัวตารางมี {head}")
                continue
            if cells != head:
                err(where, f"{path or 'md'} บรรทัด {n}: แถวมี {cells} คอลัมน์ "
                           f"แต่หัวตารางมี {head} — ตารางจะเพี้ยน")


def check_bold(where, sec):
    """** ที่ไม่ปิด ทำให้ผู้ใช้เห็นดอกจันดิบ"""
    for path, s in texts(sec):
        for n, line in enumerate(s.split("\n"), 1):
            if line.count("**") % 2:
                err(where, f"{path or 'md'} บรรทัด {n}: ** ไม่เป็นคู่ "
                           f"({line.strip()[:60]!r})")


def check_nl(where, obj, nl):
    for code in obj.get("nl") or []:
        if code not in nl:
            err(where, f"รหัส นล. '{code}' ไม่มีใน data/nl.json")


def main(sets=None):
    nl = json.load(open(os.path.join(DATA, "nl.json"), encoding="utf-8"))
    index = json.load(open(os.path.join(DATA, "index.json"), encoding="utf-8"))
    listed = [e["set"] for e in index]

    files = sorted(glob.glob(os.path.join(DATA, "*.json")))
    files = [f for f in files
             if os.path.basename(f) not in ("index.json", "nl.json")]
    on_disk = [os.path.splitext(os.path.basename(f))[0] for f in files]

    for s in sorted(set(listed) - set(on_disk)):
        err("index.json", f"ชุด '{s}' อยู่ในสารบัญแต่ไม่มีไฟล์ data/{s}.json")
    for s in sorted(set(on_disk) - set(listed)):
        err("index.json", f"ไฟล์ data/{s}.json มีอยู่แต่ไม่อยู่ในสารบัญ "
                          f"— ผู้ใช้จะเข้าไม่ถึง")
    dup = [s for s, c in Counter(listed).items() if c > 1]
    if dup:
        err("index.json", f"ชุดซ้ำในสารบัญ: {', '.join(dup)}")

    sec_ids, item_ids = defaultdict(list), defaultdict(list)
    nsec = nitem = 0

    for f in files:
        name = os.path.splitext(os.path.basename(f))[0]
        if sets and name not in sets:
            continue
        lessons = json.load(open(f, encoding="utf-8"))
        if not isinstance(lessons, list):
            err(name, "ไฟล์ชุดต้องเป็น list ของคาบ")
            continue
        for li, L in enumerate(lessons):
            lw = f"{name}[{li}] {str(L.get('title'))[:40]}"
            if not L.get("sections"):
                err(lw, "คาบนี้ไม่มี sections")
                continue
            for sec in L["sections"]:
                sid = sec.get("id")
                if not sid:
                    err(lw, "มี section ที่ไม่มี id")
                    continue
                sec_ids[sid].append(lw)
                where = f"{name}/{sid}"
                nsec += 1
                if not str(sec.get("title", "")).strip():
                    err(where, "section ไม่มี title")
                check_markers(where, sec)
                check_svg(where, sec)
                check_img_files(where, sec)
                check_tables(where, sec)
                check_bold(where, sec)
                check_nl(where, sec, nl)
                for it in sec.get("items") or []:
                    nitem += 1
                    iid = it.get("id")
                    if iid:
                        item_ids[iid].append(where)
                    else:
                        err(where, "มีข้อสอบที่ไม่มี id")
                    check_nl(f"{where}/{iid}", it, nl)
                    ch = it.get("choices")
                    if ch is not None:
                        ans = it.get("answer")
                        if not isinstance(ans, int) or not 0 <= ans < len(ch):
                            err(f"{where}/{iid}",
                                f"answer={ans!r} ไม่ชี้ไปที่ choice ที่มีจริง "
                                f"(มี {len(ch)} ตัวเลือก)")

    for sid, places in sec_ids.items():
        if len(places) > 1:
            err("ทั้งโปรเจกต์", f"section id ซ้ำ '{sid}' — {'; '.join(places)}")
    for iid, places in item_ids.items():
        if len(places) > 1:
            err("ทั้งโปรเจกต์", f"item id ซ้ำ '{iid}' — {'; '.join(places)}")

    print(f"ตรวจ {nsec} หัวข้อ · {nitem} ข้อสอบ · {len(files)} ชุด · "
          f"พจนานุกรม นล. {len(nl)} รหัส")
    for w in warns:
        print("  เตือน  ", w)
    for e in errors:
        print("  ผิด    ", e)
    print(f"\n{'ไม่ผ่าน' if errors else 'ผ่าน'} — "
          f"{len(errors)} error · {len(warns)} warning")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or None))
