#!/usr/bin/env python3
"""Build saq/index.html from template.html + saq_data.json.

Usage: python3 saq/build_saq.py
Publishes as an Artifact with the files in saq/img/ next to the page.
"""
import json, pathlib
here = pathlib.Path(__file__).resolve().parent
data = json.loads((here / "saq_data.json").read_text(encoding="utf-8"))
ids = {i["id"] for i in data["items"]}
exams = {e["id"] for e in data["exams"]}
for it in data["items"]:
    assert it["ex"] in exams, it["id"]
    assert it["t"] in data["topics"], it["id"]
    if "see" in it:
        assert it["see"] in ids, it["id"]
    for im in it.get("img", []):
        assert (here / "img" / im["f"]).exists(), im["f"]
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = (here / "template.html").read_text(encoding="utf-8").replace("__DATA__", blob)
(here / "index.html").write_text(html, encoding="utf-8")
print(f"index.html: {len(data['items'])} items, {len(html)//1024} KB")
