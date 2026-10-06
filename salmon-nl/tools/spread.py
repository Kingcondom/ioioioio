#!/usr/bin/env python3
"""สลับตำแหน่งคำตอบของข้อที่เขียนแบบ "คำตอบถูกอยู่ choices[0]"

ข้อที่ยังไม่ได้สลับต้องมี "_raw": true และ "answer": 0
สคริปต์จะสลับแบบ deterministic ตาม id (รันซ้ำได้ผลเดิม) แล้วลบ _raw ทิ้ง
ข้อที่ตัวเลือกเรียงตามธรรมชาติ (ตัวเลข ระยะโรค) ใส่ "keep_order": true — จะไม่สลับ แค่ลบ _raw

ใช้: python3 tools/spread.py <set>
"""
import json, sys, os, hashlib, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ชุดที่ publish ไปแล้วก่อนมีโหมดสมดุล — คงวิธีเดิมไว้ ไม่ให้คำตอบที่ผู้ใช้เคยทำผิดตำแหน่ง
LEGACY = {"gi", "cardio", "resp", "nephro"}

def spread(key):
    path = os.path.join(ROOT, "data", f"{key}.json")
    data = json.load(open(path))
    n = 0
    if key not in LEGACY:
        raw = [it for l in data for s in l.get("sections", []) for it in s.get("items", []) if it.get("_raw")]
        seq = []
        rng0 = random.Random(int(hashlib.md5(key.encode()).hexdigest(), 16))
        while len(seq) < len(raw):
            blk = list(range(5)); rng0.shuffle(blk); seq += blk
        for it, target in zip(raw, seq):
            it.pop("_raw")
            if it.pop("keep_order", False):
                continue
            assert it["answer"] == 0, it["id"]
            rng = random.Random(int(hashlib.md5(it["id"].encode()).hexdigest(), 16))
            rest = it["choices"][1:]; rng.shuffle(rest)
            it["choices"] = rest[:target] + [it["choices"][0]] + rest[target:]
            it["answer"] = target
            n += 1
    for l in data:
        for s in l.get("sections", []):
            for it in s.get("items", []):
                if not it.pop("_raw", False):
                    continue
                if it.pop("keep_order", False):
                    continue
                assert it["answer"] == 0, it["id"]
                seed = int(hashlib.md5(it["id"].encode()).hexdigest(), 16)
                rng = random.Random(seed)
                order = list(range(len(it["choices"])))
                rng.shuffle(order)
                it["choices"] = [it["choices"][i] for i in order]
                it["answer"] = order.index(0)
                n += 1
    json.dump(data, open(path, "w"), ensure_ascii=False, indent=1)
    print(f"[{key}] สลับคำตอบ {n} ข้อ")

if __name__ == "__main__":
    for k in sys.argv[1:]:
        spread(k)
