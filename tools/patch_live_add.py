#!/usr/bin/env python3
"""เพิ่มกลุ่มคาบใหม่เข้า Ward Drill ที่ publish อยู่ — แพตช์หน้าเว็บสด ไม่ build ใหม่

หน้าเว็บสดถูก session อื่นแพตช์ต่อไปมาก (ธีม Teaching Round, แท็บรูป, แยกปี, สุ่มข้อ, ถาม AI)
การ build จาก template.html จะลบของพวกนั้นทิ้ง จึงต้องแก้จากหน้าเว็บจริงเท่านั้น

ใช้:
    python3 tools/patch_live_add.py <live.html> <out.html> <spec.json>

spec.json:
    {"lectures": {"H05": {"d": "ศ. 25 ก.ย.", "w": 2}, ...},
     "nl": {"code": {...}, ...},
     "items": [{"set": "heme", "file": "path/to/heme_H05.json"}, ...]}

แต่ละไฟล์ข้อสอบเป็น {"mcq": [...], "meq": [...]} โดย MCQ เขียนคำตอบถูกไว้ choices[0] / answer 0
สคริปต์สลับตำแหน่งคำตอบแบบ deterministic (seed = id) · id ซ้ำ = แทนที่ → รันซ้ำได้
"""
import json, random, re, sys

WRAP_HEAD = re.compile(r'^<!doctype html><html><head>.*?<body>\n(?=<!doctype html>)', re.S | re.I)
DROP_KEYS = {"note_img"}


def strip_wrapper(html):
    m = WRAP_HEAD.match(html)
    if not m:
        return html
    html = html[m.end():]
    tail = "\n</body></html>"
    k = html.rstrip("\n").rfind(tail)
    if k >= 0 and html.count("</body></html>") >= 2:
        html = html[:k] + "\n"
    return html


def shuffle(q):
    ch = list(q["choices"])
    assert q.get("answer", 0) == 0 and len(ch) == 5 and len(set(ch)) == 5, q["id"]
    order = list(range(5))
    random.Random(q["id"]).shuffle(order)
    q["choices"] = [ch[i] for i in order]
    q["answer"] = order.index(0)
    return q


def js_json(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def main(src, out, spec_path):
    html = strip_wrapper(open(src, encoding="utf-8").read())
    spec = json.load(open(spec_path, encoding="utf-8"))

    m = re.search(r'(<script type="application/json" id="bank">)(.*?)(</script>)', html, re.S)
    bank = json.loads(m.group(2))
    added = {}
    for ent in spec["items"]:
        data = json.load(open(ent["file"], encoding="utf-8"))
        s = bank[ent["set"]]
        for part in ("mcq", "meq"):
            have = {q["id"]: i for i, q in enumerate(s[part])}
            for q in data.get(part, []):
                q = {k: v for k, v in q.items() if k not in DROP_KEYS}
                if part == "mcq":
                    q = shuffle(q)
                if q["id"] in have:
                    s[part][have[q["id"]]] = q
                else:
                    s[part].append(q)
                    have[q["id"]] = len(s[part]) - 1
                added[ent["set"]] = added.get(ent["set"], 0) + 1
    html = html[:m.start(2)] + js_json(bank) + html[m.end(2):]

    m = re.search(r'var LEC = (\{.*?\});', html, re.S)
    lec = json.loads(m.group(1))
    lec.update(spec.get("lectures", {}))
    html = html[:m.start(1)] + json.dumps(lec, ensure_ascii=False) + html[m.end(1):]

    if spec.get("nl"):
        i = html.find("var NL  = ")
        j = html.find("\n", i)
        line = html[i + len("var NL  = "):j].rstrip()
        semi = line.endswith(";")
        nl = json.loads(line.rstrip(";"))
        for k, v in spec["nl"].items():
            nl.setdefault(k, v)
        html = html[:i] + "var NL  = " + json.dumps(nl, ensure_ascii=False) + (";" if semi else "") + html[j:]

    open(out, "w", encoding="utf-8").write(html)
    print("added/replaced:", added, "| lectures:", list(spec.get("lectures", {})), "| bytes:", len(html.encode()))


if __name__ == "__main__":
    main(*sys.argv[1:4])
