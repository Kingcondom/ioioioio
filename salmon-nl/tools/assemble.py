#!/usr/bin/env python3
"""รวม parts/<set>/*.py → data/<set>.json แล้วสลับคำตอบ + ตรวจ + อัปเดต index.json

ใช้: python3 tools/assemble.py <set>
"""
import json, os, sys, glob, runpy, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

def assemble(key):
    files = sorted(glob.glob(os.path.join(ROOT, "parts", key, "*.py")))
    if not files:
        print(f"[{key}] ยังไม่มีไฟล์ใน parts/{key}/")
        return
    lecs = []
    for f in files:
        ns = runpy.run_path(f)
        L = ns.get("LECTURE")
        if not L:
            raise SystemExit(f"{f}: ไม่มีตัวแปร LECTURE")
        lecs.append(L)
    lecs.sort(key=lambda l: l["lec"])
    json.dump(lecs, open(os.path.join(ROOT, "data", f"{key}.json"), "w"), ensure_ascii=False, indent=1)
    py = sys.executable
    subprocess.run([py, os.path.join(ROOT, "tools", "spread.py"), key], check=True)
    r = subprocess.run([py, os.path.join(ROOT, "tools", "check.py"), key])
    subprocess.run([py, os.path.join(ROOT, "tools", "build_index.py")], check=True)
    return r.returncode

if __name__ == "__main__":
    rc = 0
    for k in sys.argv[1:]:
        rc |= assemble(k) or 0
    sys.exit(rc)
