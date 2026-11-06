# -*- coding: utf-8 -*-
"""ปักหมุดใน Salmon NL (ผู้ใช้ถาม "ไม่มีปักหมุดหรอ" 6 พ.ย.)

    python3 patch_salmon_pin.py <salmon index.html> <out.html>

- ปุ่ม "ปักหมุด" บนแถบหัวเว็บ: เปิดหัวข้ออยู่ = ปักหัวข้อนั้นลงหน้า Post-it ห้ามลืม (#s-<id>) · ไม่ได้เปิด = เปิดหน้า Post-it
- ทุกตารางในเนื้อหามีปุ่ม "ปักตารางใน post-it" (แถวละใบ ผ่าน #t=<base64url JSON> เหมือน MED421 learn)
"""
import sys

CSS = '''.pinbar{display:flex;justify-content:flex-end;margin:14px 0 -8px}
.pinbar .btn{padding:3px 11px;font-size:12.5px;text-decoration:none}
a.btn{text-decoration:none;display:inline-block}
'''

HEAD_OLD = '''    <button class="btn" id="themeBtn" title="สลับธีม">โหมดสี</button>'''
HEAD_NEW = '''    <a class="btn" id="pinBtn" href="https://claude.ai/artifact/BRsYSzd35CARo2m6Jw6ANY" target="_blank" rel="noopener" title="ปักหัวข้อที่เปิดอยู่ลงหน้า Post-it ห้ามลืม">📌 ปักหมุด</a>
''' + HEAD_OLD

JS = r'''/* ---------- ปักหมุดลงหน้า Post-it ห้ามลืม ---------- */
var POSTIT="https://claude.ai/artifact/BRsYSzd35CARo2m6Jw6ANY";
function pinCellTxt(td){return String(td.innerText||td.textContent||"").replace(/[ \t]+/g," ").replace(/\s*\n\s*/g,"\n").trim();}
function pinTableHref(tw){
  var tb=tw.querySelector("table");if(!tb)return POSTIT;
  var hd=[].map.call(tb.querySelectorAll("thead th"),pinCellTxt),ctx="",el=tw.previousElementSibling;
  while(el&&!/^H[34]$/.test(el.tagName))el=el.previousElementSibling;
  if(el)ctx=pinCellTxt(el);
  var s=secOf(lecOf(state.lec),state.sec);if(!ctx)ctx=s?s.title:"Salmon NL";
  var sub=hd.length===2&&hd[1]?hd[1]:"",cards=[];
  tb.querySelectorAll("tbody tr").forEach(function(tr){
    var c=[].map.call(tr.children,pinCellTxt);if(!c.length||!c.join(""))return;
    var head=c[0]||hd[0]||"",back=[];
    for(var i=1;i<c.length;i++){if(!c[i]||c[i]==="—")continue;back.push(hd.length>2&&hd[i]?hd[i]+": "+c[i]:c[i]);}
    if(!head||!back.length)return;
    cards.push(["**"+head.replace(/\*/g,"")+"**\n"+(sub?sub.replace(/[?？]\s*$/,"")+" ?":ctx),back.join("\n")]);
  });
  var b64=btoa(unescape(encodeURIComponent(JSON.stringify({s:ctx,c:cards})))).replace(/\+/g,"-").replace(/\//g,"_").replace(/=+$/,"");
  return POSTIT+"#t="+b64;
}
function pinInit(root){
  (root||document).querySelectorAll(".prose .tablewrap").forEach(function(tw){
    if(tw._pin)return;tw._pin=1;
    if(!tw.querySelector("tbody tr td:nth-child(2)"))return;
    var bar=document.createElement("div");bar.className="pinbar";
    bar.innerHTML="<a class='btn' data-tpin='1' href='"+POSTIT+"' target='_blank' rel='noopener' title='แต่ละแถวของตารางนี้จะเป็น post-it หนึ่งใบ'>📌 ปักตารางใน post-it</a>";
    tw.parentNode.insertBefore(bar,tw);
  });
}
document.addEventListener("click",function(e){
  var a=e.target.closest&&e.target.closest("a[data-tpin],#pinBtn");if(!a)return;
  if(a.id==="pinBtn")a.href=POSTIT+(state.view==="section"&&state.sec?"#s-"+encodeURIComponent(state.sec):"");
  else{var tw=a.parentNode.nextElementSibling;if(tw)a.href=pinTableHref(tw);}
});
(function(){var m=document.getElementById("main");if(!m||!("MutationObserver" in window))return;
  new MutationObserver(function(){pinInit(m);}).observe(m,{childList:true,subtree:true});})();

'''

EDITS = [
    ('.chip.nl{border-style:dashed}', '.chip.nl{border-style:dashed}\n' + CSS.rstrip('\n')),
    (HEAD_OLD, HEAD_NEW),
    ('function viewSection(){', JS + 'function viewSection(){'),
]


def patch(s):
    if 'id="pinBtn"' in s:
        return s
    for a, b in EDITS:
        assert s.count(a) == 1, a
        s = s.replace(a, b)
    return s


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    open(sys.argv[2], "w", encoding="utf-8").write(patch(open(sys.argv[1], encoding="utf-8").read()))
    print("ok")
