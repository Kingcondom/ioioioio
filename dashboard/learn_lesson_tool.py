# -*- coding: utf-8 -*-
"""เพิ่มคาบใหม่ (ทั้งคาบ) ลง MED421 learn จากไฟล์ section หลายไฟล์

    python3 learn_lesson_tool.py check <learn data dir> <sections.json>
    python3 learn_lesson_tool.py assemble <learn data dir> <header.json> <out data dir> <sections.json>...

sections.json = list ของ section {id,title,minutes,summary,source,nl[],md,pearls[],items[],figs{}}
  items = [{id,kind:"mcq",topic,stem,choices[5],answer,explain,pearl,src,ref[],nl[]}]
header.json = {"set":"hemonc","lec":"9/11","date":"…","title":"…","subtitle":"…","objectives":[…],"guidelines":[…],"meq":[],"osce":[]}
assemble: คัด data dir ทั้งหมด → เพิ่มคาบลงชุด (แทนคาบ lec เดิมถ้ามี) เรียง section ตาม id · อัปเดต lectureCount ใน index.json
"""
import sys, os, re, json, glob, shutil


def nl_codes(data_dir):
    nl = json.load(open(os.path.join(data_dir, "nl.json"), encoding="utf-8"))
    codes = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("code", "c") and isinstance(v, str):
                    codes.add(v)
                walk(v)
            for k in o:
                if re.match(r"^[0-9B][\w.()\-]*$", k):
                    codes.add(k)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(nl)
    return codes


def used_ids(data_dir):
    ids = set()
    for f in glob.glob(os.path.join(data_dir, "*.json")):
        if os.path.basename(f) in ("index.json", "nl.json"):
            continue
        for L in json.load(open(f, encoding="utf-8")):
            for s in L["sections"]:
                ids.add(s["id"])
                for it in s.get("items", []):
                    ids.add(it["id"])
    return ids


def check(data_dir, path):
    secs = json.load(open(path, encoding="utf-8"))
    codes, used = nl_codes(data_dir), used_ids(data_dir)
    errs, seen = [], set()
    if not isinstance(secs, list) or not secs:
        return ["ไฟล์ต้องเป็น list ของ section"]
    for s in secs:
        w = s.get("id", "?")
        for f in ("id", "title", "summary", "source", "md"):
            if not isinstance(s.get(f), str) or not s[f].strip():
                errs.append(f"{w}: ไม่มี {f}")
        if not re.match(r"^hon-anm-\d\d$", s.get("id", "")):
            errs.append(f"{w}: id ต้องเป็น hon-anm-NN")
        if not isinstance(s.get("minutes"), int):
            errs.append(f"{w}: minutes ต้องเป็นจำนวนเต็ม")
        if len(s.get("md", "")) < 2500:
            errs.append(f"{w}: md สั้นไป ({len(s.get('md',''))} ตัวอักษร · ต้องลึก ≥ 2,500)")
        for h in ("### ", ):
            if h not in s.get("md", ""):
                errs.append(f"{w}: md ต้องแบ่งหัวข้อด้วย ###")
        if not isinstance(s.get("pearls"), list) or len(s["pearls"]) < 3:
            errs.append(f"{w}: pearls ต้อง ≥ 3")
        figs = s.get("figs") or {}
        for m in re.findall(r"\[\[fig:([\w-]+)\]\]", s.get("md", "")):
            if m not in figs:
                errs.append(f"{w}: [[fig:{m}]] ไม่มีใน figs")
        if "[[anim:" in s.get("md", ""):
            errs.append(f"{w}: อย่าใส่ [[anim:]] เอง — ภาพเคลื่อนไหวใส่ผ่านไฟล์ anim (patch_learn_anim.py)")
        bad = [c for c in s.get("nl", []) if c not in codes]
        if bad:
            errs.append(f"{w}: รหัส NL ไม่มีใน nl.json: {bad}")
        items = s.get("items", [])
        if len(items) < 3:
            errs.append(f"{w}: items ต้อง ≥ 3 ข้อ")
        for it in items:
            iw = f"{w}/{it.get('id')}"
            if not re.match(r"^HON-ANM-MCQ-\d\d\d?$", it.get("id", "")):
                errs.append(f"{iw}: id ต้องเป็น HON-ANM-MCQ-NN")
            if it.get("kind") != "mcq":
                errs.append(f"{iw}: kind ต้องเป็น mcq")
            ch = it.get("choices")
            if not isinstance(ch, list) or len(ch) != 5 or len(set(ch)) != 5:
                errs.append(f"{iw}: choices ต้องมี 5 ตัวเลือกไม่ซ้ำ")
            if it.get("answer") not in range(5):
                errs.append(f"{iw}: answer 0–4")
            for f in ("stem", "explain", "pearl", "topic"):
                if not it.get(f):
                    errs.append(f"{iw}: ไม่มี {f}")
            if len(it.get("explain", "")) < 250:
                errs.append(f"{iw}: explain สั้นไป")
            bad = [c for c in it.get("nl", []) if c not in codes]
            if bad:
                errs.append(f"{iw}: รหัส NL ไม่มี: {bad}")
            if not isinstance(it.get("ref"), list):
                errs.append(f"{iw}: ref ต้องเป็น list")
            if it.get("id") in seen or it.get("id") in used:
                errs.append(f"{iw}: id ซ้ำ")
            seen.add(it.get("id"))
        if s.get("id") in seen or s.get("id") in used:
            errs.append(f"{w}: section id ซ้ำ")
        seen.add(s.get("id"))
    return errs


def assemble(data_dir, header, out_dir, files):
    h = json.load(open(header, encoding="utf-8"))
    if os.path.abspath(out_dir) != os.path.abspath(data_dir):
        shutil.rmtree(out_dir, ignore_errors=True)
        shutil.copytree(data_dir, out_dir)
    secs = []
    for f in files:
        secs += json.load(open(f, encoding="utf-8"))
    secs.sort(key=lambda s: s["id"])
    p = os.path.join(out_dir, h["set"] + ".json")
    d = json.load(open(p, encoding="utf-8"))
    L = {k: v for k, v in h.items() if k != "set"}
    L["sections"] = secs
    d = [x for x in d if x["lec"] != h["lec"]] + [L]
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    ip = os.path.join(out_dir, "index.json")
    idx = json.load(open(ip, encoding="utf-8"))
    for c in idx:
        if c.get("set") == h["set"]:
            c["lectureCount"] = len(d)
    json.dump(idx, open(ip, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print("ok", h["set"], h["lec"], len(secs), "sections", sum(len(s.get("items", [])) for s in secs), "items")


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "check":
        e = check(sys.argv[2], sys.argv[3])
        for x in e:
            print("ผิด:", x)
        print("ผ่าน" if not e else f"ไม่ผ่าน {len(e)} จุด")
        sys.exit(1 if e else 0)
    elif len(sys.argv) >= 6 and sys.argv[1] == "assemble":
        assemble(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:])
    else:
        sys.exit(__doc__)
