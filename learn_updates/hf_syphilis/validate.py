#!/usr/bin/env python3
"""validate.py <set> <lecture.json>
Drops the lecture into a temp copy of the learn data (replacing a lecture with the same "lec"),
checks ids/choices/NL codes/schema, then runs the repo's checkdata.py on that set."""
import json, os, shutil, subprocess, sys, tempfile
SRC = "/home/user/learnmain/artifact"
setname, path = sys.argv[1], sys.argv[2]
lec = json.load(open(path, encoding="utf-8"))
tmp = tempfile.mkdtemp()
shutil.copytree(os.path.join(SRC, "data"), os.path.join(tmp, "data"))
shutil.copytree(os.path.join(SRC, "tools"), os.path.join(tmp, "tools"))
for d in ("img", "anim"):
    if os.path.isdir(os.path.join(SRC, d)): os.symlink(os.path.join(SRC, d), os.path.join(tmp, d))
fp = os.path.join(tmp, "data", setname + ".json")
data = json.load(open(fp, encoding="utf-8"))
nl = json.load(open(os.path.join(tmp, "data", "nl.json"), encoding="utf-8"))
nlkeys = set(nl.keys()) if isinstance(nl, dict) else {x.get("code") for x in nl}
errs = []
need_l = ["lec", "date", "title", "subtitle", "objectives", "guidelines", "sections", "meq", "osce"]
for k in need_l:
    if k not in lec: errs.append("lecture missing key " + k)
others = [l for l in data if l["lec"] != lec["lec"]]
oldsec = {s["id"] for l in others for s in l["sections"]}
olditem = {i["id"] for l in others for s in l["sections"] for i in s["items"]} | {x["id"] for l in others for x in l.get("meq", []) + l.get("osce", [])}
seen = set()
for s in lec["sections"]:
    for k in ["id", "title", "summary", "minutes", "source", "nl", "md", "pearls", "items"]:
        if k not in s: errs.append(f"{s.get('id')}: missing {k}")
    if s["id"] in oldsec or s["id"] in seen: errs.append("dup section id " + s["id"])
    seen.add(s["id"])
    for c in s.get("nl", []):
        if c not in nlkeys: errs.append(f"{s['id']}: NL code not in nl.json: {c}")
    for it in s["items"]:
        if it["id"] in olditem or it["id"] in seen: errs.append("dup item id " + it["id"])
        seen.add(it["id"])
        for k in ["id", "kind", "stem", "choices", "answer", "explain", "pearl", "topic", "src", "ref", "nl"]:
            if k not in it: errs.append(f"{it.get('id')}: missing {k}")
        ch = it.get("choices", [])
        if len(ch) != 5 or len(set(ch)) != 5: errs.append(f"{it['id']}: need 5 distinct choices")
        if not (isinstance(it.get("answer"), int) and 0 <= it["answer"] < len(ch)): errs.append(f"{it['id']}: bad answer index")
        for c in it.get("nl", []):
            if c not in nlkeys: errs.append(f"{it['id']}: NL code not in nl.json: {c}")
for x in lec.get("meq", []) + lec.get("osce", []):
    if x["id"] in olditem or x["id"] in seen: errs.append("dup meq/osce id " + x["id"])
    seen.add(x["id"])
ans = [it["answer"] for s in lec["sections"] for it in s["items"]]
from collections import Counter
print("answer-position spread:", dict(Counter(ans)), "| sections", len(lec["sections"]), "| MCQ", len(ans), "| MEQ", len(lec.get("meq", [])), "| OSCE", len(lec.get("osce", [])))
data = others + [lec]
json.dump(data, open(fp, "w", encoding="utf-8"), ensure_ascii=False)
r = subprocess.run([sys.executable, os.path.join(tmp, "tools", "checkdata.py"), setname], capture_output=True, text=True)
print(r.stdout[-4000:], r.stderr[-2000:])
for e in errs: print("ERROR:", e)
ok = not errs and r.returncode == 0
print("RESULT:", "PASS" if ok else "FAIL")
shutil.rmtree(tmp)
sys.exit(0 if ok else 1)
