#!/usr/bin/env python3
"""Phase 0 — แยก courses JSON และ NL dictionary ออกจาก index.html เป็นไฟล์ data/*.json

อ่าน HTML ที่ดึงมาจาก artifact (มี wrapper ของ service ห่ออยู่) แล้วเขียน
  build/index.html
  artifact/data/index.json      meta ของทุก set + ชื่อไฟล์
  artifact/data/<set>.json      array ของ lectures
  artifact/data/nl.json         พจนานุกรมเลขหมวด นล.
"""
import json
import os
import re
import sys

SRC = "/root/.claude/projects/-home-user-ioioioio/a0382be8-c9ca-5bf2-8480-36307efc7b44/tool-results/artifact-265bd849-1789821927-106b.html"
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/

html = open(SRC, encoding="utf-8").read()

# ---- 1. ลอก wrapper ของ artifact service ออก ให้เหลือเอกสารที่เขียนเอง ----
start = html.find("<!doctype html>", 5)
assert start > 0, "หา doctype ตัวที่สองไม่เจอ"
doc = html[start:]
tail = "\n</body></html>\n"
assert doc.endswith(tail + "</body></html>\n") or doc.count("</body></html>") == 2, "tail ไม่เป็นไปตามที่คาด"
doc = doc[: doc.rfind("</body></html>")]          # ตัด </body></html> ของ wrapper
doc = doc.rstrip() + "\n"

# ---- 2. ดึง courses JSON ----
m = re.search(r'<script type="application/json" id="courses">(.*?)</script>\n?', doc, re.S)
assert m, "หาบล็อก courses ไม่เจอ"
courses = json.loads(m.group(1))
doc = doc[: m.start()] + doc[m.end():]

# ---- 3. ดึง NL dictionary ----
i = doc.find("var NL=")
j = doc.find("};\nvar KEY=", i)
assert i > 0 and j > i, "หาบล็อก NL ไม่เจอ"
nl = json.loads(doc[i + len("var NL=") : j + 1])

# ---- 4. เขียนไฟล์ data ----
os.makedirs(os.path.join(OUT, "data"), exist_ok=True)
index = []
for c in courses:
    meta = {k: v for k, v in c.items() if k != "lectures"}
    meta["file"] = "data/%s.json" % c["set"]
    meta["lectureCount"] = len(c["lectures"])
    index.append(meta)
    with open(os.path.join(OUT, "data", "%s.json" % c["set"]), "w", encoding="utf-8") as f:
        json.dump(c["lectures"], f, ensure_ascii=False, separators=(",", ":"))

with open(os.path.join(OUT, "data", "index.json"), "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=1)
with open(os.path.join(OUT, "data", "nl.json"), "w", encoding="utf-8") as f:
    json.dump(nl, f, ensure_ascii=False, separators=(",", ":"))

# ---- 5. แทน COURSES + NL ด้วย loader ----
LOADER = '''var COURSES=[];
var NL={};
function ensure(set){
  var c=COURSES.filter(function(x){return x.set===set;})[0];
  if(!c||c._loaded)return Promise.resolve();
  if(!c._p)c._p=fetch(c.file,{cache:"no-cache"})
    .then(function(r){if(!r.ok)throw new Error("HTTP "+r.status);return r.json();})
    .then(function(ls){c.lectures=ls;c._loaded=true;})
    .catch(function(e){c.lectures=[];c._loaded=true;c._err=String(e);});
  return c._p;
}
function boot(){
  Promise.all([
    fetch("data/index.json",{cache:"no-cache"}).then(function(r){return r.json();}),
    fetch("data/nl.json",{cache:"no-cache"}).then(function(r){return r.json();}).catch(function(){return {};})
  ]).then(function(res){
    NL=res[1];
    COURSES=res[0].map(function(meta){
      var c={};for(var k in meta)c[k]=meta[k];
      c.lectures=[];c._loaded=false;return c;
    });
    if(!COURSES.length)throw new Error("ไม่มีชุดวิชาใน data/index.json");
    if(!state.course||!COURSES.some(function(c){return c.set===state.course;}))state.course=COURSES[0].set;
    return ensure(state.course);
  }).then(render).catch(function(e){
    document.getElementById("main").innerHTML=
      "<section class='card'><h2>โหลดเนื้อหาไม่สำเร็จ</h2><p class='lede'>"+
      String(e&&e.message||e)+"</p></section>";
  });
}
'''

old_courses = "var COURSES=JSON.parse(document.getElementById('courses').textContent);\n"
assert old_courses in doc, "หาบรรทัด COURSES=JSON.parse ไม่เจอ"
doc = doc.replace(old_courses, "", 1)

# ลบบล็อก NL ทั้งก้อน (ตำแหน่งขยับหลังลบบรรทัด COURSES จึงค้นใหม่)
i = doc.find("var NL=")
j = doc.find("};\nvar KEY=", i)
assert i > 0 and j > i
doc = doc[:i] + LOADER + doc[j + 2 :]

# ---- 6. render() ต้องไม่พังตอน set ยังโหลดไม่เสร็จ ----
old_render = """function render(){
  renderMast();renderOutline();
  var m=document.getElementById('main'),h;"""
new_render = """function render(){
  renderMast();renderOutline();
  var m=document.getElementById('main'),h;
  var cc=course();
  if(!cc._loaded){
    m.innerHTML=cc._err
      ? "<section class='card'><h2>โหลดชุด "+esc(cc.label)+" ไม่สำเร็จ</h2><p class='lede'>"+esc(cc._err)+"</p></section>"
      : "<section class='card'><p class='lede'>กำลังโหลดเนื้อหา "+esc(cc.label)+" …</p></section>";
    return;
  }"""
assert old_render in doc, "หา render() ไม่เจอ"
doc = doc.replace(old_render, new_render, 1)

# ---- 7. สลับ set แล้วต้องโหลดไฟล์ของ set นั้นก่อน ----
old_sw = """      state.course=t.dataset.course;state.view="home";state.lec=null;state.sec=null;state.pid=null;
      render();window.scrollTo({top:0});"""
new_sw = """      state.course=t.dataset.course;state.view="home";state.lec=null;state.sec=null;state.pid=null;
      render();window.scrollTo({top:0});ensure(state.course).then(render);"""
assert old_sw in doc, "หา handler สลับ set ไม่เจอ"
doc = doc.replace(old_sw, new_sw, 1)

# ---- 8. state เริ่มต้นห้ามอ้าง COURSES[0] ----
old_state = 'var state={course:COURSES[0].set,view:"home"'
assert old_state in doc, "หา state init ไม่เจอ"
doc = doc.replace(old_state, 'var state={course:"",view:"home"', 1)

# ---- 9. เรียก boot() แทน render() ตอนเริ่ม ----
old_boot = "\nrender();\n})();"
assert doc.count(old_boot) == 1, "หา render() ท้ายสคริปต์ไม่เจอ (หรือเจอมากกว่าหนึ่งที่)"
doc = doc.replace(old_boot, "\nboot();\n})();", 1)

with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(doc)

# ---- รายงาน ----
print("index.html      %8d chars" % len(doc))
total = 0
for name in sorted(os.listdir(os.path.join(OUT, "data"))):
    n = os.path.getsize(os.path.join(OUT, "data", name))
    total += n
    print("data/%-14s %8d bytes" % (name, n))
print("data รวม        %8d bytes" % total)
print("เดิมทั้งหน้า     %8d chars" % len(html))
