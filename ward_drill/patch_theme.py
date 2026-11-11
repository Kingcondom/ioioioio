#!/usr/bin/env python3
"""ปุ่มเลือกโหมดสี (อัตโนมัติ / สว่าง / มืด) ที่หัวหน้า Ward Drill (ผู้ใช้ขอ 11 พ.ย. 2569)

CSS ของหน้ามีชุดสีมืดอยู่แล้ว (prefers-color-scheme + :root[data-theme]) — แพตช์นี้แค่ให้เลือกเองได้
เก็บค่าใน localStorage med421-drill-theme · ตั้ง data-theme ก่อนวาดเนื้อหา ไม่มีหน้ากระพริบ

ใช้:  python3 ward_drill/patch_theme.py ward_drill/index.html   (แก้ไฟล์เดิม · รันซ้ำได้)
"""
import sys

CSS = """/* ---------- ปุ่มโหมดสี ---------- */
.thm{display:inline-flex;align-items:center;gap:2px;margin:10px 0 0 8px;padding:3px;background:var(--surface-sunk);border-radius:999px;vertical-align:top}
.thm button{appearance:none;border:0;background:none;color:var(--ink-3);font:inherit;font-size:12px;font-weight:600;padding:4px 11px;border-radius:999px;cursor:pointer;white-space:nowrap;
  transition:background .2s var(--e),color .2s var(--e)}
.thm button:hover{color:var(--ink)}
.thm button[aria-pressed="true"]{background:var(--surface);color:var(--accent-ink);box-shadow:0 1px 2px rgba(0,0,0,.12)}
@media print{.thm{display:none!important}}
"""

HTML = """        <span class="thm" id="thm" role="group" aria-label="โหมดสี"><button type="button" data-t="auto">อัตโนมัติ</button><button type="button" data-t="light">สว่าง</button><button type="button" data-t="dark">มืด</button></span>
        <script>
        (function(){var K="med421-drill-theme",root=document.documentElement,box=document.getElementById("thm");
          function get(){try{var v=localStorage.getItem(K);return v==="light"||v==="dark"?v:"auto";}catch(e){return "auto";}}
          function apply(t){if(t==="auto"){root.removeAttribute("data-theme");root.style.colorScheme="light dark";}
            else{root.setAttribute("data-theme",t);root.style.colorScheme=t;}
            [].forEach.call(box.querySelectorAll("button"),function(b){b.setAttribute("aria-pressed",String(b.getAttribute("data-t")===t));});}
          apply(get());
          box.addEventListener("click",function(e){var b=e.target.closest("button[data-t]");if(!b)return;var t=b.getAttribute("data-t");
            try{if(t==="auto")localStorage.removeItem(K);else localStorage.setItem(K,t);}catch(x){}apply(t);});
        })();
        </script>
"""

REPL = [
    ("/* ---------- ข้อสอบแยกปี ---------- */\n", "/* ---------- ข้อสอบแยกปี ---------- */\n" + CSS, ".thm{display:inline-flex"),
    ('        <span class="lsync" id="lsync" role="status"><i></i><span>บันทึกในเครื่องนี้</span></span>\n',
     '        <span class="lsync" id="lsync" role="status"><i></i><span>บันทึกในเครื่องนี้</span></span>\n' + HTML,
     'id="thm"'),
]


def main():
    p = sys.argv[1]
    html = open(p, encoding="utf-8").read()
    for old, new, marker in REPL:
        if marker in html:
            continue
        c = html.count(old)
        assert c == 1, f"anchor found {c}x: {old[:70]!r}"
        html = html.replace(old, new)
    open(p, "w", encoding="utf-8").write(html)
    print("patched", p)


if __name__ == "__main__":
    main()
