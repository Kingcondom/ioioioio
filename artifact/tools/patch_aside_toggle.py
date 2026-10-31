#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""แพตช์หน้า MED421 learn: ปุ่มซ่อนแถบสารบัญ "หัวข้อทั้งหมด" + เนื้อหาเต็มความกว้างจอ

ผู้ใช้คอมเมนต์ 31 ต.ค. 2569 บนแถบ #outline: "ซ่อนตรงนี้ให้หน่อย แล้วก็ซูมเนื้อหาเข้าตามหน้าจอของผู้ใช้"
- ปุ่ม "ซ่อนสารบัญ ◂" / "สารบัญ ▸" ข้างปุ่มซ่อนเมนู (ยังเห็นตอนพับเมนู) · จำค่าใน localStorage 'med421-learn-aside'
- เมื่อซ่อน: คอลัมน์เดียว และเลิกจำกัดความกว้าง .wrap (1220px) → เนื้อหากว้างตามจอ

ใช้: python3 patch_aside_toggle.py <index.html ต้นทาง (ถอด wrapper แล้ว)> <ปลายทาง> · รันซ้ำได้
"""
import sys

MARK = 'id="asideBtn"'
REPS = [
("#mastBtn{padding:6px 13px}",
 "#mastBtn{padding:6px 13px}\n"
 "/* ซ่อนแถบสารบัญ \"หัวข้อทั้งหมด\" แล้วให้เนื้อหาขยายเต็มความกว้างจอ (ผู้ใช้ขอ 31 ต.ค.) — จำไว้ในเครื่องนี้ */\n"
 "#asideBtn{padding:6px 13px;order:-1}\n"
 "body.noaside .cols{grid-template-columns:minmax(0,1fr)}body.noaside .cols>aside{display:none}\n"
 "body.noaside .wrap{max-width:none}"),
("""    <button class="btn" id="mastBtn" aria-expanded="true" title="ซ่อนแถบเมนู">ซ่อนเมนู ▴</button>""",
 """    <button class="btn" id="asideBtn" aria-controls="outline" aria-expanded="true" title="ซ่อนแถบสารบัญ ให้เนื้อหาเต็มจอ">ซ่อนสารบัญ ◂</button>
    <button class="btn" id="mastBtn" aria-expanded="true" title="ซ่อนแถบเมนู">ซ่อนเมนู ▴</button>"""),
("""try{setMast(localStorage.getItem('med421-learn-mast')==='min');}catch(e){}""",
 """try{setMast(localStorage.getItem('med421-learn-mast')==='min');}catch(e){}
function setAside(off){
  document.body.classList.toggle('noaside',off);
  var b=document.getElementById('asideBtn');if(!b)return;
  b.setAttribute('aria-expanded',off?'false':'true');
  b.textContent=off?'สารบัญ ▸':'ซ่อนสารบัญ ◂';b.title=off?'แสดงแถบสารบัญ':'ซ่อนแถบสารบัญ ให้เนื้อหาเต็มจอ';
}
try{setAside(localStorage.getItem('med421-learn-aside')==='off');}catch(e){}"""),
("""  if(t.id==="mastBtn"){""",
 """  if(t.id==="asideBtn"){
    var off=!document.body.classList.contains('noaside');setAside(off);
    try{localStorage.setItem('med421-learn-aside',off?'off':'');}catch(e2){}
    return;
  }
  if(t.id==="mastBtn"){"""),
]

if __name__ == "__main__":
    s = open(sys.argv[1], encoding="utf-8").read()
    if MARK in s:
        print("มีแพตช์อยู่แล้ว")
    else:
        for o, n in REPS:
            assert s.count(o) == 1, "ไม่พบจุดแพตช์: " + o[:40]
            s = s.replace(o, n)
        print("แพตช์แล้ว")
    open(sys.argv[2], "w", encoding="utf-8").write(s)
