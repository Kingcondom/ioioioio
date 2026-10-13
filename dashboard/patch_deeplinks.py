import sys
def unwrap(src):
    lines=src.split("\n")
    assert lines[0].startswith("<!doctype html><html><head><meta charset=utf8>") and lines[0].endswith("<body>"), lines[0][:80]
    body="\n".join(lines[1:]).rstrip()
    assert body.endswith("</body></html>")
    body=body[:-len("</body></html>")].rstrip()+"\n"
    assert body.rstrip().endswith("</body></html>")
    return body
def sub(s,old,new):
    assert s.count(old)==1,(old[:60],s.count(old)); return s.replace(old,new)

learn_in,learn_out,drill_in,drill_out=sys.argv[1:5]
s=unwrap(open(learn_in,encoding="utf-8").read())
s=sub(s,".card{background:var(--surface);border:1px solid var(--rule);border-radius:var(--r-lg);box-shadow:var(--shadow);",
        ".card[id]{scroll-margin-top:84px}\n.card{background:var(--surface);border:1px solid var(--rule);border-radius:var(--r-lg);box-shadow:var(--shadow);")
s=sub(s,"""    if(!state.course||!COURSES.some(function(c){return c.set===state.course;}))state.course=COURSES[0].set;
    return ensure(state.course);
  }).then(render).catch(""","""    if(!state.course||!COURSES.some(function(c){return c.set===state.course;}))state.course=COURSES[0].set;
    readHash();
    return ensure(state.course);
  }).then(function(){render();landHash();}).catch(""")
s=sub(s,"""function boot(){""","""/* ---------- ลิงก์ตรงจาก Lecture Dashboard: #<ชุด> หรือ #<ชุด>-<คาบ> ----------
   เลขคาบที่มี / ใช้ . แทน (เช่น #gi-27.10 = คาบ 27/10 ของชุด GI) */
function slug(x){return String(x==null?"":x).replace(/[^A-Za-z0-9._~-]/g,".");}
var pendingLec=null;
function readHash(){
  var h=String(location.hash||"").replace(/^#/,"");
  if(!h)return false;
  var i=h.indexOf("-"),set=i<0?h:h.slice(0,i),lec=i<0?"":h.slice(i+1);
  if(!COURSES.some(function(c){return c.set===set;}))return false;
  state.course=set;state.view="home";state.sec=null;state.pid=null;state.lec=null;
  pendingLec=lec||null;
  return true;
}
function landHash(){
  if(!pendingLec)return;
  var want=pendingLec;pendingLec=null;
  var hit=lectures().filter(function(l){return slug(l.lec)===want;})[0];
  if(!hit)return;
  state.lec=hit.lec;render();
  var el=document.getElementById("lec-"+slug(hit.lec));
  if(el)el.scrollIntoView({block:"start"});
}
window.addEventListener("hashchange",function(){
  if(!COURSES.length||!readHash())return;
  render();window.scrollTo({top:0});
  ensure(state.course).then(function(){render();landHash();});
});
function boot(){""")
s=sub(s,"""    h+="<section class='card'><div class='eyebrow'>คาบ "+esc(l.lec)+(l.date""",
        """    h+="<section class='card' id='lec-"+esc(slug(l.lec))+"'><div class='eyebrow'>คาบ "+esc(l.lec)+(l.date""")
open(learn_out,"w",encoding="utf-8").write(s)

d=unwrap(open(drill_in,encoding="utf-8").read())
d=sub(d,"""
render();
})();
</script>""","""
/* ---------- ลิงก์ตรงจาก Lecture Dashboard: #<ชุด> หรือ #<ชุด>-<คาบ> เช่น #cardio-13 ---------- */
function applyHash(){
  var h=String(location.hash||"").replace(/^#/,"");
  if(!h)return false;
  var i=h.indexOf("-"),k=i<0?h:h.slice(0,i),l=i<0?"":h.slice(i+1);
  if(!BANK[k])return false;
  state.set=k;state.mode="new";state.part="all";state.lec="all";
  if(l){
    if(newItems(k).some(function(it){return it.lec===l;}))state.lec=l;
    else if(BANK[k].old.some(function(g){return g.lec===l;})){state.mode="old";state.lec=l;}
  }
  save();return true;
}
applyHash();
window.addEventListener("hashchange",function(){if(applyHash()){render();window.scrollTo(0,0);}});

render();
})();
</script>""")
open(drill_out,"w",encoding="utf-8").write(d)
print("ok",len(s),len(d))
