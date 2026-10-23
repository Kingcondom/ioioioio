# -*- coding: utf-8 -*-
"""ไล่ว่าบทเรียนทั้งหมด (MED421 learn · Ward Drill · ห้องสมุดท่าอาจารย์ · Salmon NL) ครอบคลุมเกณฑ์ NL 2567 ข้อไหนแล้ว
แล้วฝังผลลงแท็บ "ครอบคลุม NL" ของ dashboard/index.html

    python3 dashboard/build_nl.py <learn data dir> <drill bank.json> <library items.json> [<salmon data dir>]

- learn data dir   = ไฟล์ data/*.json ของ artifact MED421 learn (รวม nl.json)
- drill bank.json  = ก้อน <script id="bank"> ของ MED421 Ward Drill
- library items.json = อาร์เรย์ ITEMS ของห้องสมุดท่าอาจารย์ ({g,t,d,u})
- salmon data dir  = ไฟล์ data/*.json ของ artifact Salmon NL (สรุปสไลด์ MedSalmon ติว NL2 Medicine, engine เดียวกับ learn)
                     ชุด exam25 (ข้อสอบ NL2 2025) นับเป็นข้อสอบอย่างเดียว ไม่นับเป็นบทสอน

หลักฐานแบ่ง 2 ระดับ
  เต็ม  = มีบทสอนเรื่องนั้นจริง: ชื่อคาบหรือชื่อหัวข้อใน learn, รหัส nl ที่ผูกระดับหัวข้อ, หรือชื่อบทในห้องสมุด
  บางส่วน = แตะเรื่องนั้น: คำโปรย/สรุปหัวข้อใน learn, ข้อสอบใน learn/drill (ชื่อข้อหรือรหัส nl)
           หรือคำบรรยายของบทในห้องสมุด
"""
import datetime, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from nl_scope import SCOPE, GROUPS  # noqa: E402

LEARN = "https://claude.ai/artifact/5jjGrfPjyBgP7wzxcu8TcE"
DRILL = "https://claude.ai/artifact/Fdi5gcNXKqFLAXg4fQBV7X"
SALMON = "https://claude.ai/artifact/EL8HrvUJawWYs1rr25qzGK"
SETS = ["air", "cardio", "chest", "endo", "gi", "hemonc", "id", "nephro", "neuro"]
SET_NAME = {"air": "AIR", "cardio": "Cardio", "chest": "Chest", "endo": "Endo", "gi": "GI",
            "hemonc": "Heme/Onc", "id": "ID", "nephro": "Nephro", "neuro": "Neuro"}


def slug(x):
    return re.sub(r"[^A-Za-z0-9._~-]", ".", str(x))


def salmon_courses(salmon_dir):
    """[(set, label, lectures, is_exam)] ของ Salmon NL"""
    if not salmon_dir:
        return []
    out = []
    for c in json.load(open(os.path.join(salmon_dir, "index.json"), encoding="utf-8")):
        ls = json.load(open(os.path.join(salmon_dir, os.path.basename(c["file"])), encoding="utf-8"))
        out.append((c["set"], c["label"], ls, c["set"] == "exam25"))
    return out


def main(learn_dir, bank_path, lib_path, salmon_dir=None):
    nl = json.load(open(os.path.join(learn_dir, "nl.json"), encoding="utf-8"))
    pats = {c: [re.compile(p, re.I) for p in ps] for c, ps in SCOPE.items()}
    missing = [c for c in SCOPE if c not in nl]
    if missing:
        sys.exit("รหัสใน nl_scope.py ที่ไม่มีใน nl.json: %s" % missing)

    strong = {c: {} for c in SCOPE}   # code -> {key: (label, url)}
    names = {"L": {}, "S": {}, "B": {}}  # ชื่อแหล่งสำหรับหมายเหตุบทซ้อน
    weak = {c: {} for c in SCOPE}

    def hit(text):
        return [c for c, ps in pats.items() if any(p.search(text) for p in ps)]

    def add(store, codes, key, label, url):
        for c in codes:
            if c in store:
                store[c].setdefault(key, (label, url))

    # ---- MED421 learn
    for s in SETS:
        for L in json.load(open(os.path.join(learn_dir, s + ".json"), encoding="utf-8")):
            url = LEARN + "#" + s + "-" + slug(L["lec"])
            lname = "Learn · " + SET_NAME[s] + " · " + L["title"]
            names["L"][s + "-" + slug(L["lec"])] = SET_NAME[s] + " · " + L["title"]
            add(strong, hit(L["title"]), "L:" + url, lname, url)
            add(weak, hit(L.get("subtitle") or ""), "L:" + url, lname, url)
            for sec in L.get("sections", []):
                add(strong, hit(sec["title"]), "L:" + url, lname, url)
                add(weak, hit(sec.get("summary") or ""), "L:" + url, lname, url)
                add(strong, sec.get("nl") or [], "L:" + url, lname, url)
                for it in sec.get("items", []):
                    codes = set(hit(it.get("topic") or "")) | set(c for c in (it.get("nl") or []) if c in SCOPE)
                    add(weak, codes, "LQ:" + url, lname + " (ข้อเช็ค)", url)
            for k in ("meq", "osce"):
                for it in L.get(k, []):
                    codes = set(hit(it.get("topic") or "")) | set(c for c in (it.get("nl") or []) if c in SCOPE)
                    add(weak, codes, "LQ:" + url, lname + " (" + k.upper() + ")", url)

    # ---- Ward Drill
    bank = json.load(open(bank_path, encoding="utf-8"))
    for s, v in bank.items():
        if s == "mock":
            continue
        for it in v["mcq"] + v["meq"]:
            url = DRILL + "#" + s + "-" + it["lec"]
            codes = set(hit(it.get("topic") or "")) | set(c for c in (it.get("nl") or []) if c in SCOPE)
            add(weak, codes, "D:" + url, "Drill · " + (it.get("lecture") or s).split(" (")[0], url)
        for g in v["old"]:
            url = DRILL + "#" + s + "-" + g["lec"]
            for it in g["items"]:
                codes = set(c for c in (it.get("nl") or []) if c in SCOPE)
                add(weak, codes, "D:" + url, "Drill · " + (g.get("lecture") or s).split(" (")[0] + " (คลังเก่า)", url)

    # ---- Salmon NL: ชื่อคาบ/หัวข้อ/รหัส nl ระดับหัวข้อ = เต็ม · คำโปรย/สรุป/ข้อสอบ = บางส่วน
    salmon = salmon_courses(salmon_dir)
    for cset, clabel, ls, is_exam in salmon:
        for L in ls:
            url = SALMON + "#" + cset + "-" + slug(L["lec"])
            lname = "Salmon NL · " + clabel + " · " + L["title"]
            names["S"][cset + "-" + slug(L["lec"])] = clabel + " · " + L["title"]
            if not is_exam:
                add(strong, hit(L["title"]), "S:" + url, lname, url)
                add(weak, hit(L.get("subtitle") or ""), "S:" + url, lname, url)
            for sec in L.get("sections", []):
                if not is_exam:
                    add(strong, hit(sec["title"]), "S:" + url, lname, url)
                    add(weak, hit(sec.get("summary") or ""), "S:" + url, lname, url)
                    add(strong, [c for c in (sec.get("nl") or []) if c in SCOPE], "S:" + url, lname, url)
                for it in sec.get("items", []):
                    codes = set(hit(it.get("topic") or "")) | set(c for c in (it.get("nl") or []) if c in SCOPE)
                    add(weak, codes, "SQ:" + url, lname + " (ข้อสอบ)", url)

    # ---- ห้องสมุดท่าอาจารย์
    lib = json.load(open(lib_path, encoding="utf-8"))
    for it in lib:
        names["B"][it["u"].rstrip("/").rsplit("/", 1)[-1]] = it["t"]
        add(strong, hit(it["t"]), "B:" + it["u"], "ห้องสมุด · " + it["t"], it["u"])
        add(weak, hit(it.get("d") or ""), "B:" + it["u"], "ห้องสมุด · " + it["t"], it["u"])

    # ---- บทเรียน artifact อื่นของผู้ใช้ที่ยังไม่อยู่ในห้องสมุด (extra_lessons.tsv: ชื่อ<TAB>artifact id[<TAB>หัวข้อที่แตะ])
    in_lib = {it["u"].rstrip("/").rsplit("/", 1)[-1] for it in lib}
    for line in open(os.path.join(HERE, "extra_lessons.tsv"), encoding="utf-8"):
        if not line.strip():
            continue
        parts = line.rstrip("\n").split("\t")
        title, aid = parts[0], parts[1]
        if aid in in_lib:
            continue
        url = "https://claude.ai/artifact/" + aid
        label = "บทเรียน · " + re.sub(r"\s*\([^)]*\)\s*$", "", title)
        names["B"][aid] = re.sub(r"\s*\([^)]*\)\s*$", "", title)
        add(strong, hit(title), "B:" + url, label, url)
        if len(parts) > 2:  # คอลัมน์ 3 = หัวข้อที่บทนั้นแตะ (ตรวจจากเนื้อหาจริง)
            add(weak, hit(parts[2]), "B:" + url, label, url)

    # ---- เลนส์คลังข้อสอบ: ข้อหนึ่งถามเรื่องอะไร (นับข้อละครั้ง ไม่ซ้ำ id)
    #   ถามตรง = รหัส nl ที่ผูก + ชื่อข้อ + ตัวเลือกที่ถูก · แตะในเฉลย = ต้นคำอธิบาย 220 ตัวอักษร
    def correct(it):
        ch = it.get("choices") or []
        try:
            return ch[int(it.get("answer"))] if ch else ""
        except (TypeError, ValueError, IndexError):
            return ""

    def tags(it):
        return {c for c in (it.get("nl") or []) if c in SCOPE}

    Q = {}
    for s, v in bank.items():
        src = "mock" if s == "mock" else "drill"
        for it in v["mcq"] + v["meq"]:
            d = tags(it) | set(hit((it.get("topic") or "") + " · " + correct(it)))
            Q[it["id"]] = (src, d, set(hit((it.get("explain") or "")[:220])) - d)
        for g in v["old"]:
            for it in g["items"]:
                d = tags(it) | set(hit(correct(it)))
                Q[it["id"]] = ("old", d, set(hit((it.get("note") or "")[:220])) - d)
    for s in SETS:
        for L in json.load(open(os.path.join(learn_dir, s + ".json"), encoding="utf-8")):
            for sec in L.get("sections", []):
                for it in sec.get("items", []):
                    if it["id"] in Q:
                        continue
                    d = tags(it) | set(hit((it.get("topic") or "") + " · " + correct(it)))
                    Q[it["id"]] = ("learn", d, set(hit((it.get("explain") or "")[:220])) - d)
    for cset, clabel, ls, is_exam in salmon:
        for L in ls:
            for sec in L.get("sections", []):
                for it in sec.get("items", []):
                    d = tags(it) | set(hit((it.get("topic") or "") + " · " + correct(it)))
                    Q["salmon:" + it["id"]] = ("nl25" if is_exam else "salmon", d, set(hit((it.get("explain") or "")[:220])) - d)
    qd = {c: 0 for c in SCOPE}
    qx = {c: 0 for c in SCOPE}
    per = {k: set() for k in ("drill", "old", "mock", "learn", "salmon", "nl25")}
    nsrc = {k: 0 for k in per}
    for src, d, x in Q.values():
        nsrc[src] += 1
        for c in d:
            qd[c] += 1
            per[src].add(c)
        for c in x:
            qx[c] += 1

    def key(c):
        return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", c)]

    rows = []
    for c in sorted(SCOPE, key=key):
        e = nl[c]
        st = 2 if strong[c] else (1 if weak[c] else 0)
        part = [v for k, v in weak[c].items() if k not in strong[c]]
        grp = next(g for g, _, pre in GROUPS if c.startswith(pre))
        rows.append({
            "c": c, "t": e["title"], "lv": e.get("group") or "", "g": grp, "s": st,
            "L": [list(v) for v in strong[c].values()][:5],
            "P": [list(v) for v in part][:4],
            "q": qd[c], "qx": qx[c],
        })
    # ---- หัวข้อ NL ที่แต่ละแหล่งสอนเต็ม (ใช้บอกว่าบทอ่านของคาบหนึ่งซ้อนทับกันตรงไหน)
    #   L = บท Learn (key = hash คาบ) · S = Salmon NL (<ชุด>-<คาบ>) · B = ห้องสมุด/บทข้างเตียง (artifact id)
    #   D = Drill (hash lec) นับจากข้อสอบ จึงเป็นแค่ "แตะ"
    src = {"L": {}, "S": {}, "B": {}, "D": {}}
    def keyed(store, kinds):
        for c in SCOPE:
            for k in store[c]:
                kind, url = k.split(":", 1)
                if kind in kinds:
                    sid = url.rsplit("#", 1)[1] if kind != "B" else url.rstrip("/").rsplit("/", 1)[-1]
                    src[kind].setdefault(sid, set()).add(c)
    keyed(strong, ("L", "S", "B"))
    keyed(weak, ("D",))
    src = {k: {i: sorted(v, key=key) for i, v in sorted(d.items())} for k, d in src.items()}
    _t = datetime.date.today()
    _m = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."][_t.month - 1]
    out = {"asof": "%d %s %d" % (_t.day, _m, _t.year + 543), "groups": [[g, n] for g, n, _ in GROUPS], "rows": rows,
           "qtotal": len(Q), "qsrc": {k: [nsrc[k], len(per[k])] for k in per}, "src": src,
           "names": {k: {i: n for i, n in sorted(d.items()) if i in src[k]} for k, d in names.items()}}
    path = os.path.join(HERE, "nl_data.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

    html = os.path.join(HERE, "index.html")
    page = open(html, encoding="utf-8").read()
    blob = json.dumps(out, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    new, n = re.subn(r'(<script type="application/json" id="nldata">).*?(</script>)',
                     lambda m: m.group(1) + blob + m.group(2), page, flags=re.S)
    if n != 1:
        sys.exit("ไม่พบ <script id=\"nldata\"> ใน index.html")
    open(html, "w", encoding="utf-8").write(new)

    tot = len(rows)
    full = sum(r["s"] == 2 for r in rows)
    part = sum(r["s"] == 1 for r in rows)
    print("NL ในขอบเขต %d ข้อ · มีบทเรียน %d · บางส่วน %d · ยังไม่มี %d" % (tot, full, part, tot - full - part))
    q1 = sum(r["q"] >= 1 for r in rows)
    print("คลังข้อสอบ %d ข้อ · หัวข้อที่มีข้อถามตรง %d (%d%%) · ≥3 ข้อ %d · นับเฉลยด้วย %d" % (
        len(Q), q1, round(100 * q1 / tot), sum(r["q"] >= 3 for r in rows), sum(1 for r in rows if r["q"] or r["qx"])))
    for g, n, _ in GROUPS:
        rs = [r for r in rows if r["g"] == g]
        print("  %-24s %3d  เต็ม %3d  บางส่วน %3d  ไม่มี %3d" % (n, len(rs), sum(r["s"] == 2 for r in rs),
                                                               sum(r["s"] == 1 for r in rs), sum(r["s"] == 0 for r in rs)))


if __name__ == "__main__":
    if len(sys.argv) not in (4, 5):
        sys.exit(__doc__)
    main(*sys.argv[1:])
