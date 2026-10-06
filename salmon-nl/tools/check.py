#!/usr/bin/env python3
"""ตรวจไฟล์ data/<set>.json ของ Salmon NL

ใช้:  python3 tools/check.py <set>      (เช่น gi)
      python3 tools/check.py --all

✗ = ต้องแก้ก่อน publish · ! = คำเตือน
"""
import json, re, sys, os, glob
import xml.etree.ElementTree as ET
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = json.load(open(os.path.join(ROOT, "data", "nl.json")))

def all_ids(skip=None):
    ids = Counter()
    for f in glob.glob(os.path.join(ROOT, "data", "*.json")):
        k = os.path.basename(f)[:-5]
        if k in ("nl", "index") or k == skip:
            continue
        try:
            for l in json.load(open(f)):
                for s in l.get("sections", []):
                    ids[s["id"]] += 1
                    for it in s.get("items", []):
                        ids[it["id"]] += 1
        except Exception:
            pass
    return ids

def md_problems(txt, where, errs):
    if "```" in txt:
        errs.append(f"✗ {where}: มี code fence")
    for n, line in enumerate(txt.split("\n")):
        if line.count("**") % 2:
            errs.append(f"✗ {where}: ** ไม่ครบคู่ในบรรทัด {n+1}: {line[:70]}")
        if re.search(r"\w\*\d", line):
            errs.append(f"! {where}: มี * ติดตัวเลข อาจกลายเป็นตัวเอียง: {line[:60]}")

def check_svg(svg, where, errs):
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as e:
        errs.append(f"✗ {where}: SVG parse ไม่ผ่าน ({e})")
        return
    if not root.tag.endswith("svg") or "viewBox" not in root.attrib:
        errs.append(f"✗ {where}: ต้องขึ้นต้นด้วย <svg viewBox=...>")
    if re.search(r"#[0-9a-fA-F]{3,6}\b|rgb\(|<style|<script|on\w+=|font-family", svg):
        errs.append(f"✗ {where}: SVG มีสีตายตัว/style/script — ใช้ class ของธีมเท่านั้น")
    if "<foreignObject" in svg:
        errs.append(f"✗ {where}: ห้ามใช้ foreignObject")
    for m in re.finditer(r'font-size="(\d+(?:\.\d+)?)"', svg):
        if float(m.group(1)) < 11:
            errs.append(f"! {where}: ตัวอักษรเล็กกว่า 11")

def check(key):
    path = os.path.join(ROOT, "data", f"{key}.json")
    errs = []
    data = json.load(open(path))
    others = all_ids(skip=key)
    seen = Counter()
    n_sec = n_items = n_fig = 0
    pos = Counter()
    for l in data:
        for k in ("lec", "title", "sections"):
            if k not in l:
                errs.append(f"✗ คาบ {l.get('lec')}: ขาด {k}")
        l.setdefault("meq", []); l.setdefault("osce", [])
        for s in l.get("sections", []):
            n_sec += 1
            sid = s.get("id", "?")
            seen[sid] += 1
            for k in ("id", "title", "summary", "md", "pearls", "items"):
                if k not in s:
                    errs.append(f"✗ {sid}: ขาด {k}")
            md_problems(s.get("md", ""), sid, errs)
            for p in s.get("pearls", []):
                md_problems(p, sid + " pearl", errs)
            for c in s.get("nl", []):
                if c not in NL:
                    errs.append(f"! {sid}: รหัส นล. {c} ไม่มีใน nl.json")
            figs = s.get("figs", [])
            fids = [f.get("id") for f in figs]
            for ref in re.findall(r"\[\[fig:([\w-]+)\]\]", s.get("md", "")):
                if ref not in fids:
                    errs.append(f"✗ {sid}: อ้าง [[fig:{ref}]] แต่ไม่มีใน figs")
            for f in figs:
                n_fig += 1
                if not f.get("id") or not f.get("svg"):
                    errs.append(f"✗ {sid}: fig ขาด id/svg")
                    continue
                check_svg(f["svg"], f"{sid} fig {f['id']}", errs)
            if len(s.get("items", [])) < 2:
                errs.append(f"! {sid}: ข้อสอบน้อยกว่า 2 ข้อ")
            for it in s.get("items", []):
                n_items += 1
                iid = it.get("id", "?")
                seen[iid] += 1
                ch = it.get("choices", [])
                if len(ch) != 5:
                    errs.append(f"✗ {iid}: ตัวเลือกไม่ครบ 5 ({len(ch)})")
                if len(set(c.strip().lower() for c in ch)) != len(ch):
                    errs.append(f"✗ {iid}: ตัวเลือกซ้ำ")
                a = it.get("answer")
                if not isinstance(a, int) or not 0 <= a < len(ch):
                    errs.append(f"✗ {iid}: answer ผิดช่วง")
                else:
                    pos[a] += 1
                if it.get("_raw"):
                    errs.append(f"✗ {iid}: ยังไม่ได้รัน tools/spread.py")
                for k in ("stem", "explain", "pearl"):
                    if not it.get(k):
                        errs.append(f"✗ {iid}: ขาด {k}")
                md_problems(it.get("explain", ""), iid, errs)
                md_problems(it.get("stem", ""), iid + " stem", errs)
                if re.search(r"(ข้อ|ตัวเลือก|choice|option)\s*\(?[A-E]\)?(?![a-z])", it.get("explain", "")):
                    errs.append(f"! {iid}: คำอธิบายอ้างตัวอักษรตัวเลือก (จะผิดหลังสลับ) — อ้างด้วยเนื้อหาแทน")
                for c in it.get("nl", []):
                    if c not in NL:
                        errs.append(f"! {iid}: รหัส นล. {c} ไม่มีใน nl.json")
    for i, c in seen.items():
        if c > 1:
            errs.append(f"✗ id ซ้ำในไฟล์: {i}")
        if others.get(i):
            errs.append(f"✗ id ชนกับชุดอื่น: {i}")
    hard = [e for e in errs if e.startswith("✗")]
    print(f"[{key}] {len(data)} หมวด · {n_sec} หัวข้อ · {n_items} ข้อ · {n_fig} ภาพ · ตำแหน่งคำตอบ "
          + " ".join(f"{'ABCDE'[k]}{pos[k]}" for k in range(5)))
    for e in errs[:200]:
        print("  " + e)
    print(f"  → ✗ {len(hard)} · ! {len(errs)-len(hard)}")
    return len(hard)

if __name__ == "__main__":
    keys = sys.argv[1:]
    if keys == ["--all"]:
        keys = [os.path.basename(f)[:-5] for f in sorted(glob.glob(os.path.join(ROOT, "data", "*.json")))
                if os.path.basename(f) not in ("nl.json", "index.json")]
    bad = sum(check(k) for k in keys)
    sys.exit(1 if bad else 0)
