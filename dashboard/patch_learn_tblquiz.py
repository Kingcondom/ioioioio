# -*- coding: utf-8 -*-
"""ปิดตารางเพื่อทวน (ผู้ใช้ขอ 25 ต.ค.) — ทุกตารางในเนื้อหา learn มีปุ่ม "ปิดเพื่อทวน"

    python3 patch_learn_tblquiz.py <learn index.html> <out.html>

กดแล้ว: หัวตาราง + คอลัมน์แรกยังเห็น (เป็นโจทย์) · ช่องอื่นถูกปิดเป็นกล่อง เหลือคำใบ้ = ตัวอักษรแรก ๆ + จำนวนข้อในช่อง
แตะช่องเพื่อเปิดทีละช่อง · ปุ่ม "เปิดทั้งหมด" / "ปิดใหม่" / "เลิกทวน"
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_deeplinks import unwrap, sub  # noqa: E402

CSS = r'''
/* ---------- ปิดตารางเพื่อทวน ---------- */
.tqbar{display:flex;gap:6px;align-items:center;flex-wrap:wrap;margin:14px 0 -6px}
.tqbar .btn{padding:4px 11px;font-size:12.5px}
.tqbar .tqn{font-size:12px;color:var(--ink-3)}
table.tq td.cv{cursor:pointer;position:relative;background:var(--surface-sunk)}
table.tq td.cv:not(.op),table.tq td.cv:not(.op) *{color:transparent!important;text-shadow:none!important}
table.tq td.cv:not(.op)::after{content:attr(data-hint);position:absolute;inset:4px;display:flex;align-items:center;justify-content:center;
  border:1px dashed var(--rule-strong);border-radius:8px;color:var(--ink-3);font-size:12.5px;font-weight:600;background:var(--surface);text-align:center;padding:0 4px}
table.tq td.cv.op{background:var(--ok-soft)}
'''

JS = r'''
/* ---------- ปิดตารางเพื่อทวน ---------- */
var TQSEG=(window.Intl&&Intl.Segmenter)?new Intl.Segmenter("th",{granularity:"grapheme"}):null;
function tqHint(t){
  t=String(t||"");
  var segs=t.split(/\s·\s|\n/).filter(function(x){return x.trim();}).length;
  t=t.replace(/\s+/g," ").trim();
  if(!t)return "";
  var core=t.replace(/[↑↓↔≈=<>≥≤+\-–—()*.,:;\/\s]/g,"");
  if(core.length<=2)return "?";
  var g=TQSEG?Array.from(TQSEG.segment(t),function(x){return x.segment;}):Array.from(t);
  var head=g.slice(0,2).join("").trim();
  return head+"…"+(segs>1?" ("+segs+")":"");
}
function tqSet(tw,on){
  var tb=tw.querySelector("table");if(!tb)return;
  tb.classList.toggle("tq",on);
  tb.querySelectorAll("tbody tr").forEach(function(tr){
    Array.prototype.forEach.call(tr.children,function(td,i){
      if(i===0||td.tagName!=="TD")return;
      if(on){if(!td.hasAttribute("data-hint"))td.setAttribute("data-hint",tqHint(td.innerText));td.classList.add("cv");td.classList.remove("op");}
      else td.classList.remove("cv","op");
    });
  });
  var bar=tw.previousElementSibling;if(bar&&bar.classList.contains("tqbar"))tqBar(bar,on);
}
function tqBar(bar,on){
  bar.innerHTML=on?"<button class='btn' data-tq='all'>เปิดทั้งหมด</button><button class='btn' data-tq='re'>ปิดใหม่</button><button class='btn' data-tq='off'>เลิกทวน</button><span class='tqn'>แตะช่องเพื่อเปิดทีละช่อง · คำใบ้ = ตัวแรก ๆ (จำนวนข้อ)</span>"
    :"<button class='btn' data-tq='on'>ปิดเพื่อทวน</button>";
}
function tqInit(root){
  (root||document).querySelectorAll(".prose .tablewrap").forEach(function(tw){
    if(tw._tq)return;tw._tq=1;
    var tb=tw.querySelector("table");if(!tb||!tb.querySelector("tbody tr td:nth-child(2)"))return;
    var bar=document.createElement("div");bar.className="tqbar";tqBar(bar,false);tw.parentNode.insertBefore(bar,tw);
  });
}
document.addEventListener("click",function(e){
  var b=e.target.closest&&e.target.closest("[data-tq]");
  if(b){var bar=b.closest(".tqbar"),tw=bar.nextElementSibling,act=b.getAttribute("data-tq");
    if(act==="on"||act==="re")tqSet(tw,true);
    else if(act==="off")tqSet(tw,false);
    else if(act==="all")tw.querySelectorAll("td.cv").forEach(function(td){td.classList.add("op");});
    return;}
  var td=e.target.closest&&e.target.closest("table.tq td.cv");
  if(td)td.classList.toggle("op");
});
(function(){var m=document.getElementById("main");if(!m||!("MutationObserver" in window))return;
  new MutationObserver(function(){tqInit(m);}).observe(m,{childList:true,subtree:true});})();
'''


def patch(src):
    s = unwrap(src) if src.startswith("<!doctype html><html><head><meta charset=utf8>") else src
    if "function tqInit" in s:
        return s
    s = sub(s, '.chip.anc{', CSS.strip() + '\n.chip.anc{')
    s = sub(s, '/* ---------- tiny markdown (เหมือน drill.html) ---------- */',
            JS.strip() + '\n\n/* ---------- tiny markdown (เหมือน drill.html) ---------- */')
    return s


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    open(sys.argv[2], "w", encoding="utf-8").write(patch(open(sys.argv[1], encoding="utf-8").read()))
    print("ok")
