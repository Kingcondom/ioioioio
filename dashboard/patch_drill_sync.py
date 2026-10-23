# -*- coding: utf-8 -*-
"""ให้ MED421 Ward Drill บันทึกคำตอบในบัญชีผู้ใช้ (capability db + user) แทนที่จะอยู่แค่ localStorage

    python3 patch_drill_sync.py <index.html ของ drill ที่ดาวน์โหลด> <ไฟล์ออก>

แล้ว publish ไฟล์ออกทับ URL ของ drill พร้อม capabilities {db:{}, user:{}}

- เอกสารส่วนตัว: data/users/<id>/drill = {answers, shown}  (ชุด/โหมดที่เปิดค้างไว้ยังจำแยกเครื่อง)
- กติการวมเหมือน learn (patch_learn_sync.py): เครื่องที่เคยซิงก์และไม่มีของค้าง → ใช้ของในบัญชี
  (การกด "ล้าง" จากเครื่องอื่นจึงตามมาด้วย) · ยังไม่เคยซิงก์หรือมีของค้าง → รวมสองฝั่งแล้วอัปโหลด
  · เบราว์เซอร์ที่เคยซิงก์กับบัญชีอื่น → ใช้ของบัญชีนี้ ไม่เอาของในเครื่องไปปน
- เขียนรวบเป็นครั้งเดียวหลังหยุดกด 0.7 วินาที
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_deeplinks import unwrap, sub  # noqa: E402

SYNC_JS = r'''
/* ---------- บันทึกคำตอบในบัญชี (capability db + user) ----------
   data/users/<id>/drill = {answers, shown} · meta.cloud = เครื่องนี้เคยซิงก์แล้ว · meta.pend = มีของในเครื่องที่ยังไม่ได้อัปโหลด */
var MKEY="med421-drill-v1:sync";
var SYNC={mode:"local",ref:null,uid:"",busy:0,timer:null,first:1,sent:"",err:"",meta:{cloud:false,pend:false,uid:""}};
try{var mm=JSON.parse(localStorage.getItem(MKEY)||"{}");SYNC.meta.cloud=!!mm.cloud;SYNC.meta.pend=!!mm.pend;SYNC.meta.uid=typeof mm.uid==="string"?mm.uid:"";}catch(e){}
function saveMeta(){try{localStorage.setItem(MKEY,JSON.stringify(SYNC.meta));}catch(e){}}
function norm(o){
  o=o||{};var a={},s={};
  if(o.answers&&typeof o.answers==="object")Object.keys(o.answers).sort().forEach(function(k){
    var v=o.answers[k];if(!v||typeof v!=="object")return;
    var p=v.pick;if(typeof p!=="number"||p<0||p>9||p!==Math.floor(p))return;
    a[k]=v.auto?{pick:p,ok:!!v.ok,auto:1}:{pick:p,ok:!!v.ok};
  });
  if(o.shown&&typeof o.shown==="object")Object.keys(o.shown).sort().forEach(function(k){if(o.shown[k])s[k]=1;});
  return {answers:a,shown:s};
}
function cur(){return JSON.stringify(norm(state));}
SYNC.sent=cur();
function syncCheck(){
  if(cur()===SYNC.sent)return;
  if(!SYNC.meta.pend){SYNC.meta.pend=true;saveMeta();}
  clearTimeout(SYNC.timer);SYNC.timer=setTimeout(flush,700);
}
function flush(){
  SYNC.timer=null;
  if(SYNC.mode!=="cloud"||!SYNC.ref||SYNC.busy)return;
  var c=cur();if(c===SYNC.sent)return;
  if(c.length>240000){SYNC.err="คำตอบเยอะเกินที่บัญชีเก็บได้ ส่วนเกินบันทึกในเครื่องนี้";renderSync();return;}
  SYNC.busy=1;renderSync();
  var body=JSON.parse(c);body.v=1;body.updatedAt=new Date().toISOString();
  SYNC.ref.set(body).then(function(){
    SYNC.busy=0;SYNC.sent=c;SYNC.err="";
    if(cur()===SYNC.sent){SYNC.meta.pend=false;SYNC.meta.cloud=true;SYNC.meta.uid=SYNC.uid;saveMeta();}
    else{clearTimeout(SYNC.timer);SYNC.timer=setTimeout(flush,300);}
    renderSync();
  },function(e){
    SYNC.busy=0;var code=e&&e.code;
    if(code==="unavailable"||code==="resource_exhausted"){clearTimeout(SYNC.timer);SYNC.timer=setTimeout(flush,2500+Math.random()*2000);}
    else if(code==="revoked"){SYNC.mode="local";}
    else SYNC.err="บันทึกขึ้นบัญชีไม่ได้ ตอนนี้เก็บในเครื่องนี้";
    renderSync();
  });
}
function adopt(data){var d=norm(data);state.answers=d.answers;state.shown=d.shown;}
function merge(data){var c=norm(data),l=norm(state);
  state.answers=Object.assign({},c.answers,l.answers);state.shown=Object.assign({},c.shown,l.shown);}
function onSnap(snap){
  var data=snap.exists?snap.data():null;
  if(SYNC.first){
    SYNC.first=0;
    /* เบราว์เซอร์นี้เคยซิงก์กับบัญชีอื่น → ไม่เอาของในเครื่องไปปนกับบัญชีนี้ */
    var other=!!(SYNC.meta.uid&&SYNC.meta.uid!==SYNC.uid);
    if(!data){SYNC.sent="";if(other)adopt({});}
    else{
      SYNC.sent=JSON.stringify(norm(data));
      if(other||(SYNC.meta.cloud&&!SYNC.meta.pend))adopt(data);else merge(data);
    }
    SYNC.mode="cloud";SYNC.meta.uid=SYNC.uid;
    if(cur()===SYNC.sent){SYNC.meta.pend=false;SYNC.meta.cloud=true;}
    saveMeta();save();render();flush();renderSync();return;
  }
  if(SYNC.busy||SYNC.timer||snap.metadata&&snap.metadata.hasPendingWrites)return;
  if(!data)return;
  var c=JSON.stringify(norm(data));if(c===cur())return;
  SYNC.sent=c;adopt(data);save();render();
}
function renderSync(){
  var el=document.getElementById("lsync");if(!el)return;
  el.className="lsync"+(SYNC.mode==="cloud"&&!SYNC.err?(SYNC.busy?" busy":" cloud"):"");
  el.lastChild.textContent=SYNC.err||(SYNC.mode==="cloud"?(SYNC.busy?"กำลังบันทึก…":"บันทึกในบัญชี"):"บันทึกในเครื่องนี้");
  el.title=SYNC.mode==="cloud"?"คำตอบบันทึกในบัญชีของคุณ เปิดเครื่องไหนก็เห็นเหมือนกัน":"ยังไม่ได้เชื่อมบัญชี คำตอบเก็บในเบราว์เซอร์เครื่องนี้";
}
(function connect(){
  if(!window.claude||typeof window.claude.use!=="function")return;
  Promise.all([window.claude.use("db"),window.claude.use("user")]).then(function(r){
    var db=r[0],user=r[1];if(!db||!user)return null;
    return user.id().then(function(uid){
      if(!uid)return;
      SYNC.uid=uid;SYNC.ref=db.doc("data/users/"+uid+"/drill");
      SYNC.ref.onSnapshot(onSnap,function(e){if(e&&e.code==="revoked"){SYNC.mode="local";renderSync();}});
    });
  }).catch(function(){});
})();
'''

CSS = '''
.lsync{display:inline-flex;align-items:center;gap:7px;margin-top:10px;font-size:12.5px;color:var(--ink-3);background:var(--surface);border:1px solid var(--rule);border-radius:999px;padding:5px 11px;white-space:nowrap}
.lsync i{width:8px;height:8px;border-radius:50%;background:var(--ink-3);flex:none}
.lsync.cloud i{background:var(--ok)} .lsync.busy i{background:var(--miss)}
'''


def patch(src):
    s = unwrap(src)
    s = sub(s, '''function save(){try{localStorage.setItem("med421-drill-v1",JSON.stringify(
  {answers:state.answers,shown:state.shown,set:state.set,mode:state.mode}));}catch(e){}}''',
            '''function save(){try{localStorage.setItem("med421-drill-v1",JSON.stringify(
  {answers:state.answers,shown:state.shown,set:state.set,mode:state.mode}));}catch(e){}if(typeof syncCheck==="function")syncCheck();}''' + SYNC_JS)
    # ป้ายสถานะการบันทึกใต้คำอธิบายบนหัวหน้า
    i = s.index('<p>Cardio · Nephro')
    j = s.index('</p>', i) + len('</p>')
    s = s[:j] + '\n        <span class="lsync" id="lsync" role="status"><i></i><span>บันทึกในเครื่องนี้</span></span>' + s[j:]
    s = sub(s, '.scoreboard{display:grid;', CSS.strip() + '\n.scoreboard{display:grid;')
    s = sub(s, '''ความคืบหน้าถูกเก็บไว้ในเบราว์เซอร์นี้");''',
            '''ความคืบหน้าบันทึกในบัญชีของคุณ (ซิงก์ทุกเครื่อง) ถ้ายังไม่ได้ล็อกอินจะเก็บในเครื่องนี้ก่อน");''')
    s = sub(s, '''
render();
})();
</script>''', '''
renderSync();
render();
})();
</script>''')
    return s


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    out = patch(open(sys.argv[1], encoding="utf-8").read())
    open(sys.argv[2], "w", encoding="utf-8").write(out)
    print("ok", len(out))
