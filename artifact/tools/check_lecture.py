#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ตรวจข้อมูลคาบเรียนก่อน publish — ไม่ต้องเปิดเบราว์เซอร์

    python3 artifact/tools/check_lecture.py                # ตรวจทุกชุดวิชา
    python3 artifact/tools/check_lecture.py id 5/10        # ตรวจละเอียดเฉพาะคาบ (แสดงสถิติ)

ตรวจ: schema ตาม HANDOFF §3 · id ไม่ชนกันทั้งเว็บ · รหัส นล. มีในพจนานุกรม · ไม่มี code fence ·
ตัวเลือก 5 ข้อ answer 0–4 · ตำแหน่งคำตอบไม่กระจุก · ดอกจันไม่คู่ (ทำให้ ** ค้างบนจอ) ·
lectureCount ใน index.json ตรงกับไฟล์ · ไฟล์ทุกชุดใน index มีจริง
คืนค่า exit code 1 ถ้ามีข้อผิดพลาด (คำเตือนไม่ทำให้ล้ม)"""
import json, os, re, sys
from collections import Counter

ART = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ART, "data")
err, warn = [], []

idx = json.load(open(os.path.join(D, "index.json"), encoding="utf-8"))
nl = json.load(open(os.path.join(D, "nl.json"), encoding="utf-8"))
want_set = sys.argv[1] if len(sys.argv) > 1 else None
want_lec = sys.argv[2] if len(sys.argv) > 2 else None

def units(src):
    """แยกข้อความเป็นหน่วยที่หน้าเว็บส่งเข้า inline() ทีละหน่วย — เลียนแบบ md() ใน index.html
    (ย่อหน้า: ทีละบรรทัด · รายการ: รวมบรรทัดต่อ · ตาราง: ทีละช่อง · หัวข้อ: ทั้งบรรทัด · > callout: เรียกซ้ำ)"""
    L = str(src or "").split("\n"); i = 0; out = []
    item = lambda ln, o: re.match(r"^\s*\d+[.)]\s+(.*)$", ln) if o else re.match(r"^\s*[-•]\s+(.*)$", ln)
    while i < len(L):
        ln = L[i]
        if re.match(r"^\s*>\s?", ln):
            q = []
            while i < len(L) and re.match(r"^\s*>\s?", L[i]): q.append(re.sub(r"^\s*>\s?", "", L[i])); i += 1
            out += units("\n".join(q)); continue
        if re.match(r"^\s*#{3,4}\s+", ln): out.append(ln); i += 1; continue
        if re.match(r"^\s*\|", ln):
            while i < len(L) and re.match(r"^\s*\|", L[i]):
                out += [c for c in L[i].strip().strip("|").split("|")]; i += 1
            continue
        for o in (False, True):
            if item(ln, o):
                while i < len(L):
                    m = item(L[i], o)
                    if not m: break
                    t = m.group(1); i += 1
                    while (i < len(L) and re.match(r"^\s{2,}\S", L[i]) and not re.match(r"^\s*[-•]\s", L[i])
                           and not re.match(r"^\s*\d+[.)]\s", L[i]) and not re.match(r"^\s*\|", L[i])):
                        t += " " + L[i].strip(); i += 1
                    out.append(t)
                break
        else:
            if ln.strip(): out.append(ln.strip())
            i += 1
    return out

def odd_stars(text, inline_only=False):
    """หน่วยที่ ** ไม่ครบคู่ = หน้าเว็บจะโชว์ ** ดิบ · ดอกจันติดตัวเลขกลางคำ (เช่น HLA-B*57) ทำให้ markdown พัง"""
    bad = []
    for u in ([str(text)] if inline_only else units(text)):
        if u.count("**") % 2:
            bad.append(u.strip()[:70])
        elif re.search(r"[A-Za-z0-9]\\?\*[0-9]", u):
            bad.append("ดอกจันกลางคำ: " + u.strip()[:60])
    return bad

seen = {}
for meta in idx:
    path = os.path.join(ART, meta["file"])
    if not os.path.exists(path):
        err.append("index.json อ้างไฟล์ที่ไม่มี: " + meta["file"]); continue
    data = json.load(open(path, encoding="utf-8"))
    if meta.get("lectureCount") != len(data):
        err.append("%s: lectureCount=%s แต่ไฟล์มี %d คาบ" % (meta["set"], meta.get("lectureCount"), len(data)))
    for L in data:
        tag = "%s/%s" % (meta["set"], L.get("lec"))
        for k in ("lec", "title", "subtitle", "objectives", "sections", "meq", "osce"):
            if k not in L:
                err.append("%s: ไม่มีฟิลด์ %s" % (tag, k))
        if L.get("guidelines") and not L.get("nlGap"):
            warn.append("%s: มี guidelines แต่ไม่มี nlGap" % tag)
        items = []
        for s in L.get("sections", []):
            for k in ("id", "title", "summary", "minutes", "nl", "md", "pearls", "items"):
                if k not in s:
                    err.append("%s/%s: section ไม่มีฟิลด์ %s" % (tag, s.get("id"), k))
            if "```" in s.get("md", ""):
                err.append("%s/%s: มี code fence (``` ) — parser ไม่รองรับ" % (tag, s["id"]))
            for b in odd_stars(s.get("md", "")) + [x for p in s.get("pearls", []) for x in odd_stars(p, True)]:
                err.append("%s/%s: markdown ดอกจันไม่ครบคู่ → %s" % (tag, s["id"], b))
            items += s.get("items", [])
            ids = [s["id"]]
            for c in s.get("nl", []):
                if c not in nl: err.append("%s/%s: รหัส นล. %s ไม่มีในพจนานุกรม" % (tag, s["id"], c))
            for i in s.get("items", []):
                ids.append(i["id"])
                if len(i.get("choices", [])) != 5: err.append("%s: %s ตัวเลือกไม่ครบ 5" % (tag, i["id"]))
                if not (0 <= i.get("answer", -1) <= 4): err.append("%s: %s answer นอกช่วง 0–4" % (tag, i["id"]))
                if i.get("kind") not in ("mcq", "old"): err.append("%s: %s kind=%r" % (tag, i["id"], i.get("kind")))
                for c in i.get("nl", []):
                    if c not in nl: err.append("%s: %s รหัส นล. %s ไม่มีในพจนานุกรม" % (tag, i["id"], c))
                for b in odd_stars(i.get("explain", "")) + odd_stars(i.get("stem", "")):
                    err.append("%s: %s ดอกจันไม่ครบคู่ → %s" % (tag, i["id"], b))
            for x in ids:
                if x in seen: err.append("id ซ้ำ %s (%s และ %s)" % (x, seen[x], tag))
                seen[x] = tag
        for x in L.get("meq", []) + L.get("osce", []):
            if x["id"] in seen: err.append("id ซ้ำ %s (%s และ %s)" % (x["id"], seen[x["id"]], tag))
            seen[x["id"]] = tag
            for c in x.get("nl", []):
                if c not in nl: err.append("%s: %s รหัส นล. %s ไม่มีในพจนานุกรม" % (tag, x["id"], c))
        new = [i for i in items if i.get("kind") == "mcq"]
        if len(new) >= 10:
            cnt = Counter(i["answer"] for i in new)
            top = max(cnt.values())
            if top > 0.4 * len(new):
                warn.append("%s: คำตอบกระจุก %s (ข้อใหม่ %d ข้อ) — ใช้บล็อก spread ใน build_hiv.py" % (tag, dict(sorted(cnt.items())), len(new)))
        if meta["set"] == want_set and (want_lec is None or L["lec"] == want_lec):
            codes = {c for s in L["sections"] for c in s["nl"]} | {c for i in items for c in i["nl"]}
            print("── %s · %s" % (tag, L["title"]))
            print("   หัวข้อ %d · ข้อ %d (ใหม่ %d · คลัง %d) · MEQ %d · OSCE %d · รหัส นล. %d · guidelines %d" % (
                len(L["sections"]), len(items), len(new), len(items) - len(new),
                len(L["meq"]), len(L["osce"]), len(codes), len(L.get("guidelines", []))))
            print("   ตำแหน่งคำตอบ:", dict(sorted(Counter(i["answer"] for i in items).items())))

for w in warn: print("  ! " + w)
for e in err: print("  ✗ " + e)
print("\n" + ("✅ ข้อมูลผ่านทุกข้อ" if not err else "❌ พบข้อผิดพลาด %d รายการ" % len(err)) + ("" if not warn else " · คำเตือน %d" % len(warn)))
sys.exit(1 if err else 0)
