#!/usr/bin/env python3
"""ค้นรหัสเกณฑ์ นล. 2567 ด้วย regex (ไม่สนตัวพิมพ์) — python3 tools/nl_find.py "pancreatitis|ตับอ่อน" """
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = json.load(open(os.path.join(ROOT, "data", "nl.json")))
pat = re.compile(sys.argv[1], re.I)
for c, e in NL.items():
    if pat.search(e.get("title", "")) or pat.search(e.get("section", "")):
        print(f"{c:16} g{e.get('group','') or '-':4} {e['title'][:80]}  [{e.get('section','')[:40]}]")
