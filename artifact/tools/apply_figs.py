#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""เติมภาพประกอบ SVG + ย่อหน้ากลไก (pathophysiology) ลงคาบที่ขึ้นเว็บไปแล้ว โดยไม่ต้องสร้างคาบใหม่

โมดูลภาพของแต่ละคาบชื่อ `figs_<set>_<ชื่อ>.py` อยู่ใน tools/ มีหน้าตาแบบนี้

    from svg import *
    SET, LEC = "cardio", "10"
    INSERTS = [
        # (section id, anchor, payload)
        ("cardio-10-02", "### Preload", "fig:frankstarling"),            # ภาพ = ฟังก์ชันชื่อ frankstarling()
        ("cardio-10-02", "### Preload", "#### ทำไมถึงมีอาการนี้\\n..."),   # ข้อความ markdown แทรก
    ]
    def frankstarling():
        return fig("ชื่อภาพ", "คำอธิบายใต้ภาพ", svg(420, 300, "aria-label", ...))

anchor = ข้อความส่วนหนึ่งของบรรทัดใน md (บรรทัดแรกที่มีข้อความนี้)
  - บรรทัดหัวข้อ (#) → แทรกต่อจากหัวข้อทันที
  - บรรทัดอื่น → แทรกหลังจบก้อน (ย่อหน้า/ตาราง/รายการ ที่ต่อกันจนถึงบรรทัดว่าง)
  - "^" = ต้นหัวข้อ · "$" = ท้ายหัวข้อ
รายการที่ anchor เดียวกันจะเรียงตามลำดับใน INSERTS · รันซ้ำได้ (ข้ามสิ่งที่มีอยู่แล้ว)
ฟังก์ชันที่ขึ้นต้นด้วย _ เป็นตัวช่วย ไม่ใช่ภาพ

    python3 apply_figs.py --check figs_cardio_shock     # ตรวจอย่างเดียว ไม่เขียนไฟล์
    python3 apply_figs.py figs_cardio_shock             # เขียนลง data/<set>.json
    python3 apply_figs.py --all                         # ทุกโมดูลที่มี INSERTS
"""
import glob, importlib, json, os, re, sys
import xml.etree.ElementTree as ET

TOOLS = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
MARKERS = ("ah", "ah-ac", "ah-ok", "ah-bad", "ah-ms", "ah-wa", "ah-mu")


def fig_problems(k, f):
    bad = []
    v = f.get("svg", "")
    if not v.startswith("<svg"): return ["%s: svg ต้องขึ้นต้นด้วย <svg" % k]
    if not re.search(r'viewBox="[-\d. ]+"', v): bad.append("%s: ไม่มี viewBox" % k)
    if 'role="img"' not in v or "aria-label=" not in v: bad.append("%s: ขาด role=img/aria-label" % k)
    if re.search(r"<script|<style|foreignObject|\son\w+=", v, re.I): bad.append("%s: มี script/style/foreignObject/on*=" % k)
    if re.search(r'\sid="', v): bad.append("%s: มี id ภายใน svg" % k)
    for m in re.findall(r"url\(#([\w-]+)\)", v):
        if m not in MARKERS: bad.append("%s: marker #%s ไม่มีใน index.html" % (k, m))
    try: ET.fromstring(v)
    except ET.ParseError as e: bad.append("%s: SVG ไม่ใช่ XML ที่ถูกต้อง (%s)" % (k, e))
    for fld in ("title", "cap"):
        if str(f.get(fld, "")).count("**") % 2: bad.append("%s: %s ดอกจันไม่ครบคู่" % (k, fld))
    if not f.get("cap"): bad.append("%s: ไม่มี cap" % k)
    return bad


def md_problems(block):
    bad = []
    if "```" in block: bad.append("มี code fence")
    for ln in block.split("\n"):
        if not ln.strip().startswith("|") and ln.count("**") % 2: bad.append("** ไม่ครบคู่ในบรรทัด: " + ln[:60])
        if re.search(r"[A-Za-z0-9]\\?\*[0-9]", ln): bad.append("ดอกจันติดตัวเลข: " + ln[:60])
    return bad


def insert_at(md, anchor, block):
    lines = md.split("\n")
    if anchor == "^":
        return block + "\n\n" + md.lstrip("\n"), 1
    if anchor == "$":
        return md.rstrip("\n") + "\n\n" + block + "\n", 1
    hits = [i for i, ln in enumerate(lines) if anchor in ln]
    if not hits: return md, 0
    i = hits[0]
    if not lines[i].lstrip().startswith("#"):
        while i + 1 < len(lines) and lines[i + 1].strip():
            i += 1
    out = lines[:i + 1] + ["", block, ""] + lines[i + 1:]
    s = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", s), len(hits)


def apply_module(name, data, check):
    mod = importlib.import_module(name)
    L = next((l for l in data if l["lec"] == mod.LEC), None)
    if L is None: return ["ไม่มีคาบ %s ใน %s" % (mod.LEC, mod.SET)], 0, 0
    secs = {s["id"]: s for s in L["sections"]}
    probs, nfig, nmd = [], 0, 0
    # anchor เดียวกันหลายรายการ → แทรกแบบย้อนลำดับเพื่อให้ลำดับสุดท้ายตรงกับ INSERTS
    groups = {}
    for sid, anchor, payload in mod.INSERTS:
        groups.setdefault((sid, anchor), []).append(payload)
    for (sid, anchor), payloads in groups.items():
        s = secs.get(sid)
        if s is None: probs.append("ไม่มีหัวข้อ %s" % sid); continue
        s.setdefault("figs", {})
        todo = []
        for p in payloads:
            if p.startswith("fig:"):
                key = p[4:]
                fn = getattr(mod, key, None)
                if fn is None: probs.append("%s: ไม่มีฟังก์ชัน %s()" % (sid, key)); continue
                f = fn()
                probs += ["%s: %s" % (sid, x) for x in fig_problems(key, f)]
                if any(key in ss.get("figs", {}) and ss is not s for ss in L["sections"]):
                    probs.append("%s: key %s ซ้ำกับหัวข้ออื่น" % (sid, key))
                s["figs"][key] = f
                nfig += 1
                if "[[fig:%s]]" % key not in s["md"]: todo.append("[[fig:%s]]" % key)
            else:
                probs += ["%s: %s" % (sid, x) for x in md_problems(p)]
                nmd += 1
                if p.split("\n")[0] not in s["md"]: todo.append(p)
        if not todo: continue
        new, hits = s["md"], 0
        for block in reversed(todo):
            new, hits = insert_at(new, anchor, block)
            if not hits: break
        if not hits: probs.append("%s: หา anchor ไม่เจอ: %r" % (sid, anchor)); continue
        if hits > 1 and check: print("   ⚠ %s: anchor %r เจอ %d บรรทัด ใช้บรรทัดแรก" % (sid, anchor, hits))
        s["md"] = new
    for s in L["sections"]:
        used = re.findall(r"^\s*\[\[fig:([\w-]+)\]\]\s*$", s["md"], re.M)
        for k in s.get("figs", {}):
            if k not in used: probs.append("%s: ภาพ %s ไม่ถูกอ้างใน md" % (s["id"], k))
    return probs, nfig, nmd


def main():
    args = sys.argv[1:]
    check = "--check" in args
    args = [a for a in args if a != "--check"]
    if "--all" in args:
        args = sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(TOOLS, "figs_*.py"))
                      if "INSERTS" in open(p, encoding="utf-8").read())
    idx = json.load(open(os.path.join(ART, "data", "index.json"), encoding="utf-8"))
    files = {m["set"]: os.path.join(ART, m["file"]) for m in idx}
    cache, failed = {}, False
    for name in args:
        mod = importlib.import_module(name)
        if mod.SET not in cache:
            cache[mod.SET] = json.load(open(files[mod.SET], encoding="utf-8"))
        probs, nf, nm = apply_module(name, cache[mod.SET], check)
        print("%s %-28s %s %-8s ภาพ %2d · ข้อความ %d%s" % ("✗" if probs else "✓", name, mod.SET, mod.LEC, nf, nm,
                                                         "".join("\n   - " + p for p in probs)))
        failed |= bool(probs)
    if check or failed:
        if failed: print("มีปัญหา — ไม่เขียนไฟล์")
        sys.exit(1 if failed else 0)
    for st, data in cache.items():
        with open(files[st], "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))
        print("เขียน", os.path.relpath(files[st], ART))


if __name__ == "__main__":
    main()
