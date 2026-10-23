# -*- coding: utf-8 -*-
"""ชุดข้อสอบรายคาบสำหรับ MED421 Ward Drill

    python3 drill_tool.py check <drill index.html> <ชุดใหม่.json>
    python3 drill_tool.py merge <drill index.html> <โฟลเดอร์ชุดใหม่> <out.html>

ชุดใหม่ = {"set":"endo","lec":"E06","d":"พ. 30 ก.ย.","w":3,"lecture":"Thyroid disorders (อ.…)",
           "mcq":[{id,lec,lecture,topic,stem,choices[5],answer,explain,pearl,ref[],nl[]}],
           "meq":[{id,part:"MEQ",lec,lecture,topic,vignette,questions:[{q,a}],ref,nl}
                  | {id,part:"OSCE/SAQ",lec,lecture,topic,station,instruction,answer,ref,nl}]}
merge: เพิ่มเข้า BANK[set].mcq/meq ต่อท้าย และเพิ่ม/แก้ LEC[lec] = {d, w}
"""
import sys, os, re, json, glob, collections

BANK_RE = re.compile(r'(<script[^>]*id="bank"[^>]*>)(.*?)(</script>)', re.S)
LEC_RE = re.compile(r'(var LEC = )(\{.*?\})(;\n)')
NL_RE = re.compile(r'var NL  = (\{.*?\});\n')


def unwrap_any(s):
    if s.startswith("<!doctype html><html><head><meta charset=utf8>"):
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from patch_deeplinks import unwrap
        return unwrap(s)
    return s


def load(page):
    s = unwrap_any(open(page, encoding="utf-8").read())
    bank = json.loads(BANK_RE.search(s).group(2))
    lec = json.loads(LEC_RE.search(s).group(2))
    nl = json.loads(NL_RE.search(s).group(1))
    return s, bank, lec, nl


def check(page, path):
    _, bank, lec, nl = load(page)
    a = json.load(open(path, encoding="utf-8"))
    errs, warns = [], []
    st, L = a.get("set"), a.get("lec")
    if st not in bank:
        return [f"set '{st}' ไม่มีใน Drill (มี {list(bank)})"], []
    if not L or not re.match(r"^[A-Z0-9]{2,4}$", L):
        errs.append("lec ต้องเป็นรหัสสั้น เช่น E06")
    used = {i["id"] for s2 in bank for i in bank[s2]["mcq"] + bank[s2]["meq"]}
    if any(i.get("lec") == L for i in bank[st]["mcq"] + bank[st]["meq"]):
        warns.append(f"lec {L} มีข้อเดิมอยู่แล้วใน {st} — ข้อใหม่จะต่อท้าย")
    for f in ("d", "lecture"):
        if not a.get(f):
            errs.append(f"ไม่มี {f}")
    ids = set()
    mcq = a.get("mcq", [])
    if len(mcq) < 20:
        errs.append(f"MCQ {len(mcq)} ข้อ (ต้อง ≥ 20)")
    for i, q in enumerate(mcq):
        w = f"mcq[{i}] {q.get('id')}"
        for f in ("id", "topic", "stem", "explain", "pearl"):
            if not isinstance(q.get(f), str) or not q.get(f).strip():
                errs.append(f"{w}: ไม่มี {f}")
        if q.get("lec") != L or q.get("lecture") != a.get("lecture"):
            errs.append(f"{w}: lec/lecture ต้องตรงกับหัวไฟล์")
        ch = q.get("choices")
        if not isinstance(ch, list) or len(ch) != 5 or not all(isinstance(c, str) and c.strip() for c in ch):
            errs.append(f"{w}: choices ต้องมี 5 ตัวเลือก")
        elif len(set(c.strip().lower() for c in ch)) != 5:
            errs.append(f"{w}: ตัวเลือกซ้ำกัน")
        if q.get("answer") not in (0, 1, 2, 3, 4):
            errs.append(f"{w}: answer ต้องเป็น 0–4")
        if len(q.get("explain", "")) < 200:
            errs.append(f"{w}: explain สั้นเกิน (ต้องอธิบายกลไกและทำไมข้ออื่นผิด)")
    for i, q in enumerate(a.get("meq", [])):
        w = f"meq[{i}] {q.get('id')}"
        if q.get("lec") != L or q.get("lecture") != a.get("lecture"):
            errs.append(f"{w}: lec/lecture ต้องตรงกับหัวไฟล์")
        if q.get("part") == "MEQ":
            qs = q.get("questions")
            if not q.get("vignette") or not isinstance(qs, list) or len(qs) < 3 or not all(x.get("q") and x.get("a") for x in qs):
                errs.append(f"{w}: MEQ ต้องมี vignette และ questions ≥ 3 ข้อ {{q,a}}")
        elif q.get("part") == "OSCE/SAQ":
            for f in ("station", "instruction", "answer"):
                if not q.get(f):
                    errs.append(f"{w}: OSCE/SAQ ไม่มี {f}")
        else:
            errs.append(f"{w}: part ต้องเป็น MEQ หรือ OSCE/SAQ")
        if not q.get("topic"):
            errs.append(f"{w}: ไม่มี topic")
    if not any(q.get("part") == "MEQ" for q in a.get("meq", [])):
        errs.append("ต้องมี MEQ อย่างน้อย 1 ข้อ")
    for q in mcq + a.get("meq", []):
        if q.get("id") in ids or q.get("id") in used:
            errs.append(f"id ซ้ำ: {q.get('id')}")
        ids.add(q.get("id"))
        if not isinstance(q.get("ref"), list) or not q.get("ref"):
            errs.append(f"{q.get('id')}: ref ต้องเป็น list ไม่ว่าง")
        bad = [c for c in (q.get("nl") or []) if c not in nl]
        if bad:
            errs.append(f"{q.get('id')}: รหัส NL ไม่มีใน Drill: {bad}")
        if not q.get("nl"):
            errs.append(f"{q.get('id')}: ไม่มี nl")
    dist = collections.Counter(q.get("answer") for q in mcq)
    if mcq and max(dist.values()) > 0.4 * len(mcq):
        errs.append(f"เฉลยกระจุกที่ตัวเลือกเดียวเกินไป: {dict(dist)}")
    stems = [re.sub(r"\W+", " ", q.get("stem", "").lower())[:120] for q in mcq]
    olds = {re.sub(r"\W+", " ", i.get("stem", "").lower())[:120] for s2 in bank for i in bank[s2]["mcq"]}
    dup = [s for s in stems if s in olds]
    if dup:
        errs.append(f"stem ซ้ำกับข้อที่มีอยู่แล้ว {len(dup)} ข้อ")
    return errs, warns


def merge(page, folder, out):
    s, bank, lec, nl = load(page)
    for f in sorted(glob.glob(os.path.join(folder, "*.json"))):
        a = json.load(open(f, encoding="utf-8"))
        bank[a["set"]]["mcq"] += a["mcq"]
        bank[a["set"]]["meq"] += a.get("meq", [])
        lec[a["lec"]] = {"d": a["d"], "w": a.get("w", "")}
        print(a["set"], a["lec"], len(a["mcq"]), len(a.get("meq", [])))
    bj = json.dumps(bank, ensure_ascii=False).replace("</", "<\\/")
    s = BANK_RE.sub(lambda m: m.group(1) + bj + m.group(3), s, count=1)
    s = LEC_RE.sub(lambda m: m.group(1) + json.dumps(lec, ensure_ascii=False) + m.group(3), s, count=1)
    open(out, "w", encoding="utf-8").write(s)


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "check":
        e, w = check(sys.argv[2], sys.argv[3])
        for x in w:
            print("เตือน:", x)
        for x in e:
            print("ผิด:", x)
        print("ผ่าน" if not e else f"ไม่ผ่าน {len(e)} จุด")
        sys.exit(1 if e else 0)
    elif len(sys.argv) == 5 and sys.argv[1] == "merge":
        merge(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        sys.exit(__doc__)
