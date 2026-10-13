# -*- coding: utf-8 -*-
"""ให้ MED421 learn บันทึกความคืบหน้าในบัญชีผู้ใช้ (capability db + user) แทนที่จะอยู่แค่ localStorage

    python3 patch_learn_sync.py <index.html ของ learn ที่ดาวน์โหลด> <ไฟล์ออก>

แล้ว publish ไฟล์ออกทับ URL ของ learn พร้อม capabilities {db:{}, user:{}}

- เอกสารส่วนตัวของแต่ละคน: data/users/<id>/learn = {done, ans, rate} · data/users/<id>/learn-notes = {notes}
- localStorage ยังเก็บเหมือนเดิม (ใช้ตอนไม่ได้ล็อกอิน และเป็นสำเนาในเครื่อง)
- เปิดครั้งแรกหลังล็อกอิน: ถ้าเครื่องนี้เคยซิงก์แล้วและไม่มีของค้าง ใช้ของในบัญชี (การล้างคำตอบจากเครื่องอื่นจึงตามมาด้วย)
  ถ้ายังไม่เคยซิงก์หรือมีของที่ยังไม่ได้อัปโหลด รวมทั้งสองฝั่งแล้วอัปโหลด
- จับการเปลี่ยนแปลงจาก save() ที่หน้าเรียกอยู่แล้วทุกครั้ง แล้วเขียนรวบเป็นครั้งเดียวหลังหยุดพิมพ์ 0.7 วินาที
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_deeplinks import unwrap, sub  # noqa: E402

SYNC_JS = r'''
/* ---------- บันทึกความคืบหน้าในบัญชี (capability db + user) ----------
   data/users/<id>/learn = {done, ans, rate} · data/users/<id>/learn-notes = {notes}
   SYNC.sent = สิ่งที่อยู่ในบัญชีล่าสุดที่รู้ · meta.cloud = เครื่องนี้เคยซิงก์แล้ว · meta.pend = มีของในเครื่องที่ยังไม่ได้อัปโหลด */
var MKEY=KEY+":sync";
var SYNC={mode:"local",refs:null,uid:"",busy:{p:0,n:0},timer:null,first:{p:1,n:1},sent:{p:"",n:""},err:"",later:false,meta:{cloud:false,pend:false,uid:""}};
try{var mm=JSON.parse(localStorage.getItem(MKEY)||"{}");SYNC.meta.cloud=!!mm.cloud;SYNC.meta.pend=!!mm.pend;SYNC.meta.uid=typeof mm.uid==="string"?mm.uid:"";}catch(e){}
function saveMeta(){try{localStorage.setItem(MKEY,JSON.stringify(SYNC.meta));}catch(e){}}
function trueKeys(o){var r={};if(o&&typeof o==="object")Object.keys(o).sort().forEach(function(k){if(o[k]===true)r[k]=true;});return r;}
function pick(o,ok){var r={};if(o&&typeof o==="object")Object.keys(o).sort().forEach(function(k){if(ok(o[k]))r[k]=o[k];});return r;}
function normP(o){o=o||{};return {done:trueKeys(o.done),ans:pick(o.ans,function(v){return typeof v==="number"&&v>=0&&v<10&&v===Math.floor(v);}),
  rate:pick(o.rate,function(v){return typeof v==="string"&&v.length<40;})};}
function normN(o){o=o||{};return {notes:pick(o.notes,function(v){return v===true||(typeof v==="string"&&v.length>0);})};}
function cur(k){return JSON.stringify(k==="p"?normP(state):normN(state));}
SYNC.sent.p=cur("p");SYNC.sent.n=cur("n");
function syncCheck(){
  if(cur("p")===SYNC.sent.p&&cur("n")===SYNC.sent.n)return;
  if(!SYNC.meta.pend){SYNC.meta.pend=true;saveMeta();}
  clearTimeout(SYNC.timer);SYNC.timer=setTimeout(flush,700);
}
function flush(){
  SYNC.timer=null;
  if(SYNC.mode!=="cloud"||!SYNC.refs)return;
  ["p","n"].forEach(function(k){
    var c=cur(k);if(c===SYNC.sent[k]||SYNC.busy[k])return;
    if(c.length>240000){SYNC.err="โน้ตยาวเกินที่บัญชีเก็บได้ ส่วนนี้บันทึกในเครื่องนี้";renderSync();return;}
    SYNC.busy[k]=1;renderSync();
    var body=JSON.parse(c);body.v=1;body.updatedAt=new Date().toISOString();
    SYNC.refs[k].set(body).then(function(){
      SYNC.busy[k]=0;SYNC.sent[k]=c;SYNC.err="";
      if(cur("p")===SYNC.sent.p&&cur("n")===SYNC.sent.n){SYNC.meta.pend=false;SYNC.meta.cloud=true;SYNC.meta.uid=SYNC.uid;saveMeta();}
      else{clearTimeout(SYNC.timer);SYNC.timer=setTimeout(flush,300);}
      renderSync();
    },function(e){
      SYNC.busy[k]=0;var code=e&&e.code;
      if(code==="unavailable"||code==="resource_exhausted"){clearTimeout(SYNC.timer);SYNC.timer=setTimeout(flush,2500+Math.random()*2000);}
      else if(code==="revoked"){SYNC.mode="local";}
      else SYNC.err="บันทึกขึ้นบัญชีไม่ได้ ตอนนี้เก็บในเครื่องนี้";
      renderSync();
    });
  });
}
function adopt(k,data){
  if(k==="p"){var p=normP(data);state.done=p.done;state.ans=p.ans;state.rate=p.rate;}
  else state.notes=normN(data).notes;
}
function merge(k,data){
  if(k==="p"){var c=normP(data),l=normP(state);
    state.done=Object.assign({},c.done,l.done);state.ans=Object.assign({},l.ans,c.ans);state.rate=Object.assign({},c.rate,l.rate);}
  else state.notes=Object.assign({},normN(data).notes,normN(state).notes);
}
function rerender(){
  /* อย่ารีเรนเดอร์ทับช่องที่กำลังพิมพ์ */
  var a=document.activeElement;
  if(a&&a.tagName==="TEXTAREA"){SYNC.later=true;return;}
  if(COURSES.length&&course()._loaded)render();else save();
}
document.addEventListener("focusout",function(e){if(SYNC.later&&e.target&&e.target.tagName==="TEXTAREA"){SYNC.later=false;setTimeout(rerender,0);}});
function onSnap(k,snap){
  var data=snap.exists?snap.data():null;
  if(SYNC.first[k]){
    SYNC.first[k]=0;
    /* เบราว์เซอร์นี้เคยซิงก์กับบัญชีอื่น → ไม่เอาของในเครื่องไปปนกับบัญชีนี้ */
    var other=!!(SYNC.meta.uid&&SYNC.meta.uid!==SYNC.uid);
    if(!data){SYNC.sent[k]="";if(other)adopt(k,{});}
    else{
      SYNC.sent[k]=JSON.stringify(k==="p"?normP(data):normN(data));
      if(other||(SYNC.meta.cloud&&!SYNC.meta.pend))adopt(k,data);else merge(k,data);
    }
    if(!SYNC.first.p&&!SYNC.first.n){
      SYNC.mode="cloud";SYNC.meta.uid=SYNC.uid;
      if(cur("p")===SYNC.sent.p&&cur("n")===SYNC.sent.n){SYNC.meta.pend=false;SYNC.meta.cloud=true;}
      saveMeta();flush();
    }
    rerender();renderSync();return;
  }
  if(SYNC.busy[k]||SYNC.timer||snap.metadata&&snap.metadata.hasPendingWrites)return;
  var c=data?JSON.stringify(k==="p"?normP(data):normN(data)):"";
  if(!data||c===cur(k))return;
  SYNC.sent[k]=c;adopt(k,data);rerender();
}
function renderSync(){
  var el=document.getElementById("lsync");if(!el)return;
  var busy=SYNC.busy.p||SYNC.busy.n;
  el.className="lsync"+(SYNC.mode==="cloud"&&!SYNC.err?(busy?" busy":" cloud"):"");
  el.lastChild.textContent=SYNC.err||(SYNC.mode==="cloud"?(busy?"กำลังบันทึก…":"บันทึกในบัญชี"):"บันทึกในเครื่องนี้");
  el.title=SYNC.mode==="cloud"?"ความคืบหน้าบันทึกในบัญชีของคุณ เปิดเครื่องไหนก็เห็นเหมือนกัน":"ยังไม่ได้เชื่อมบัญชี ความคืบหน้าเก็บในเบราว์เซอร์เครื่องนี้";
}
(function connect(){
  if(!window.claude||typeof window.claude.use!=="function")return;
  Promise.all([window.claude.use("db"),window.claude.use("user")]).then(function(r){
    var db=r[0],user=r[1];if(!db||!user)return null;
    return user.id().then(function(uid){
      if(!uid)return;
      SYNC.uid=uid;var base="data/users/"+uid+"/";
      SYNC.refs={p:db.doc(base+"learn"),n:db.doc(base+"learn-notes")};
      ["p","n"].forEach(function(k){
        SYNC.refs[k].onSnapshot(function(snap){onSnap(k,snap);},function(e){
          if(e&&e.code==="revoked"){SYNC.mode="local";renderSync();}
        });
      });
    });
  }).catch(function(){});
})();
'''


def patch(src):
    s = unwrap(src)
    s = sub(s, '''function save(){try{localStorage.setItem(KEY,JSON.stringify(state));}catch(e){}}''',
            '''function save(){try{localStorage.setItem(KEY,JSON.stringify(state));}catch(e){}if(typeof syncCheck==="function")syncCheck();}''' + SYNC_JS)
    # markread: ไม่เก็บค่า false ไว้ในสถานะ (ให้การยกเลิกซิงก์ไปเครื่องอื่นได้)
    s = sub(s, '''if(t.dataset.act==="markread"){state.done[state.sec]=!state.done[state.sec];render();return;}''',
            '''if(t.dataset.act==="markread"){if(state.done[state.sec])delete state.done[state.sec];else state.done[state.sec]=true;render();return;}''')
    s = sub(s, '''if(t.dataset.reveal){var k=t.dataset.reveal+"!shown";state.notes[k]=!state.notes[k];render();return;}''',
            '''if(t.dataset.reveal){var k=t.dataset.reveal+"!shown";if(state.notes[k])delete state.notes[k];else state.notes[k]=true;render();return;}''')
    # สถานะการบันทึกในแถบบน + ข้อความท้ายหน้า
    s = sub(s, '''    <button class="btn" id="themeBtn" title="สลับธีม">โหมดสี</button>''',
            '''    <span class="lsync" id="lsync" role="status"><i></i><span>บันทึกในเครื่องนี้</span></span>
    <button class="btn" id="themeBtn" title="สลับธีม">โหมดสี</button>''')
    s = sub(s, '''.ring{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--ink-3)}''',
            '''.ring{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--ink-3)}
.lsync{display:inline-flex;align-items:center;gap:7px;font-size:12.5px;color:var(--ink-3);background:var(--surface);border:1px solid var(--rule);border-radius:999px;padding:5px 11px;white-space:nowrap}
.lsync i{width:8px;height:8px;border-radius:50%;background:var(--ink-3);flex:none}
.lsync.cloud i{background:var(--ok)} .lsync.busy i{background:var(--miss)}''')
    s = sub(s, '''· ความคืบหน้าเก็บไว้ในเครื่องของคุณเอง (localStorage)</footer>''',
            '''· ความคืบหน้าบันทึกในบัญชีของคุณ (ซิงก์ทุกเครื่อง) · ถ้ายังไม่ได้ล็อกอินจะเก็บในเครื่องนี้ก่อน แล้วรวมเข้าบัญชีให้เมื่อเชื่อมได้</footer>''')
    s = sub(s, '''boot();
})();
</script>''', '''renderSync();
boot();
})();
</script>''')
    return s


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    out = patch(open(sys.argv[1], encoding="utf-8").read())
    open(sys.argv[2], "w", encoding="utf-8").write(out)
    print("ok", len(out))
