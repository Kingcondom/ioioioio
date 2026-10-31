"""Build compact post-it data from MED421 learn + Salmon NL data files.

Output (in out/):
  sec.json   topics with pearls / mnemonics / item ids
  q.json     quiz items: stem, correct answer, pearl, owning topic
"""
import json, glob, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
# learn data: ../artifact/data (this repo) · salmon data: download from the Salmon NL artifact into salmon/
SRC_DIRS = {"learn": os.path.join(ROOT, "..", "artifact", "data"), "salmon": os.path.join(ROOT, "salmon")}
OUT = os.path.join(ROOT, "data")
os.makedirs(OUT, exist_ok=True)

SOURCES = [("l", "learn"), ("s", "salmon")]


def clean(t):
    return re.sub(r"\s+\n", "\n", str(t or "")).strip()


def slug(x):
    return re.sub(r"[^A-Za-z0-9._~-]", ".", str(x if x is not None else ""))


sets_meta = {}
secs = {}
items = {}
order = []

for pre, folder in SOURCES:
    idx = json.load(open(os.path.join(SRC_DIRS[folder], "index.json")))
    sets_meta[pre] = {}
    for meta in idx:
        sets_meta[pre][meta["set"]] = {"label": meta.get("label") or meta["set"], "thai": meta.get("thai", "")}
        path = os.path.join(SRC_DIRS[folder], os.path.basename(meta["file"]))
        if not os.path.exists(path):
            print("missing", path, file=sys.stderr)
            continue
        for lec in json.load(open(path)):
            for s in lec.get("sections") or []:
                pid = pre + "-" + s["id"]
                pearls = [clean(p) for p in (s.get("pearls") or []) if clean(p)]
                mn = []
                for m in s.get("mnem") or []:
                    mn.append({
                        "n": clean(m.get("name")),
                        "w": clean(m.get("what")),
                        "l": [[clean(a), clean(b)] for a, b in (m.get("lines") or [])],
                        "x": clean(m.get("note")),
                    })
                qids = []
                seen = set(p.lower() for p in pearls)
                extra = []
                for it in s.get("items") or []:
                    iid = it.get("id")
                    if not iid:
                        continue
                    ch = it.get("choices") or []
                    ans = it.get("answer")
                    atext = ch[ans] if isinstance(ans, int) and 0 <= ans < len(ch) else ""
                    pearl = clean(it.get("pearl"))
                    items[iid] = {
                        "sec": pid,
                        "s": clean(it.get("stem")),
                        "a": clean(atext),
                        "p": pearl,
                    }
                    qids.append(iid)
                    if pearl and pearl.lower() not in seen:
                        seen.add(pearl.lower())
                        extra.append(pearl)
                secs[pid] = {
                    "src": pre,
                    "set": meta["set"],
                    "lec": str(lec.get("lec", "")),
                    "ls": slug(lec.get("lec", "")),
                    "lt": clean(lec.get("title")),
                    "t": clean(s.get("title")),
                    "sum": clean(s.get("summary")),
                    "P": pearls,
                    "X": extra,
                    "M": mn,
                    "Q": qids,
                }
                order.append(pid)

json.dump({"sets": sets_meta, "order": order, "secs": secs}, open(os.path.join(OUT, "sec.json"), "w"), ensure_ascii=False, separators=(",", ":"))
json.dump(items, open(os.path.join(OUT, "q.json"), "w"), ensure_ascii=False, separators=(",", ":"))
print("topics", len(secs), "items", len(items))
for f in ("sec.json", "q.json"):
    print(f, os.path.getsize(os.path.join(OUT, f)))
