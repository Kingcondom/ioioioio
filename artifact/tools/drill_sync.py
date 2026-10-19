#!/usr/bin/env python3
"""
drill_sync.py — ส่งข้อสอบใหม่จากบทเรียน (MED421 learn) เข้า Ward Drill

Ward Drill (artifact Fdi5gcNXKqFLAXg4fQBV7X) build จาก branch `claude/adoring-babbage-zkg8ih`
(config.json + data/*.json --build.py--> drill.html) ไม่ใช่ repo นี้
สคริปต์นี้เขียนไฟล์ลงใน checkout ของ branch นั้น — รันซ้ำได้ ผลเหมือนเดิม

    git worktree add ../drillwt origin/claude/adoring-babbage-zkg8ih
    python3 artifact/tools/drill_sync.py ../drillwt
    cd ../drillwt && python3 build.py --no-pdf

สิ่งที่ทำ
  1. ดึงข้อ MCQ ที่เขียนใหม่ในบทเรียน (เฉพาะ id ขึ้นต้นตาม PREFIX — ข้อ N-MCQ/MOCK มีในคลังอยู่แล้ว)
     แปลงเป็น schema คลัง โดยคงลำดับตัวเลือก/เฉลยเดิมของบทเรียน (กระจายเฉลยสมดุลแล้ว · ตัวอักษรตรงกันทั้งสองเว็บ)
  2. ดึง MEQ/OSCE ของบทเรียนเดียวกัน
  3. config.json: เพิ่มคาบ (lectures) + lecture_order + ไฟล์ใน `mcq_late`/`meq`
     `mcq_late` = ข้อที่ build.py *ไม่สลับ* ตัวเลือก และไม่ดึงเลขสุ่มของ seed → ลำดับตัวเลือกของข้อเดิมไม่เปลี่ยน
     (คำตอบที่ผู้ใช้บันทึกไว้เก็บเป็นเลขตำแหน่ง — ถ้าลำดับเปลี่ยน คำตอบเก่าจะชี้ผิดข้อ)
  4. build.py: รองรับ `mcq_late`
  5. template.html: ลิงก์ตรง #<ชุด>-<คาบ> (applyHash — ของ live v11 จาก Lecture Dashboard)
     + โจทย์ MEQ/OSCE ที่มีตารางเรนเดอร์เป็นตารางจริง
     + บันทึกคำตอบในบัญชี data/users/<id>/drill (ต้อง publish พร้อม capabilities {db:{}, user:{}})
     + โหมด "สุ่มทำข้อสอบ" (สุ่มจากระบบนี้/ทุกระบบ · 10–100 ข้อ · ทุกข้อ/ยังไม่เคยทำ/เคยตอบผิด)
  6. refs/nl_2567.json: เติมรหัส NL ที่ข้อใหม่อ้าง (คัดจาก artifact/data/nl.json — ประกาศฉบับเต็ม)
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LEARN = os.path.join(HERE, '..', 'data')

# (ไฟล์บทเรียน, lec ในบทเรียน, ชุดในคลัง, lec ในคลัง, prefix ข้อใหม่, ชื่อไฟล์คลัง, คาบใหม่ {date, week} หรือ None)
JOBS = [
    ('nephro.json', '14', 'nephro', '14', 'NEPH-GN-', 'gn', None),
    ('nephro.json', '30', 'nephro', '30', 'NEPH-UTI-', 'uti', None),
    ('nephro.json', 'Imaging', 'nephro', 'IMG', 'NEPH-IMG-', 'img',
     {'date': 'ไม่ระบุวัน — handout Lec19 (อ.ธนิศร)', 'week': '', 'al': 0}),
    ('hemonc.json', '12/10', 'heme', 'H04', 'HON-WBC-', 'wbc', {'date': 'จ. 12 ต.ค.', 'week': 5, 'al': 0}),
    ('endo.json', '14/10', 'endo', 'E05', 'END-DM-', 'dm', {'date': 'พ. 14 ต.ค.', 'week': 5, 'al': 0}),
    ('cardio.json', '36', 'cardio', '36', 'CAR-ECG-', 'ecg', None),
]
# ตำแหน่งคาบใหม่ใน lecture_order: แทรกหลังคาบนี้ (None = ขึ้นก่อน)
AFTER = {'IMG': '28', 'H04': None, 'E05': 'E04'}
BLURB = {
    'nephro': '8 คาบบรรยาย · 15.9% ของ lecture ทั้งหมด · ออกสอบหนักทุกรุ่น · '
              'ข้อจากบทเรียน glomerular disease · UTI · renal imaging',
    'heme': '4 คาบบรรยาย · Approach to WBC disorder and lymphadenopathy (อ.เบญจมาภรณ์) · '
            'โลหิตจางและธาลัสซีเมีย · เกล็ดเลือด การแข็งตัวของเลือด และการให้เลือด · มะเร็งเม็ดเลือดและภาวะฉุกเฉินที่เกี่ยวข้อง',
    'endo': '5 หัวข้อ · Diabetes mellitus ตั้งแต่วินิจฉัยถึง DKA (ศ.นพ.ชัยชาญ) · '
            'Metabolic syndrome โรคอ้วน และไขมันในเลือดผิดปกติ (อ.นวพร) · เบาหวานและภาวะฉุกเฉินทางเมตาบอลิก (DKA · HHS · น้ำตาลต่ำ) · '
            'โรคของต่อมไทรอยด์ · ต่อมหมวกไต ต่อมใต้สมอง และเมตาบอลิซึมของกระดูก',
}
MCQ_KEYS = ('id', 'lec', 'lecture', 'topic', 'stem', 'choices', 'answer', 'explain', 'pearl', 'ref', 'nl')


def lectures_of(fn):
    d = json.load(open(os.path.join(LEARN, fn), encoding='utf-8'))
    return d['lectures'] if isinstance(d, dict) else d


def dump(path, obj):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write('\n')


def convert(drill):
    cfg_p = os.path.join(drill, 'config.json')
    cfg = json.load(open(cfg_p, encoding='utf-8'))
    sets = {s['key']: s for s in cfg['sets']}
    nl_codes = set()
    report = []
    for fn, lec, setk, dlec, prefix, tag, newlec in JOBS:
        L = next(l for l in lectures_of(fn) if l['lec'] == lec)
        name = next((m['lecture'] for m in L.get('meq', []) + L.get('osce', []) if m['id'].startswith(prefix)), L['title'])
        mcq = []
        for s in L['sections']:
            for it in s.get('items', []):
                if it['kind'] != 'mcq' or not it['id'].startswith(prefix):
                    continue
                out = dict(it, lec=dlec, lecture=name)
                out = {k: out[k] for k in MCQ_KEYS if out.get(k) not in (None, '', [])}
                assert len(out['choices']) == 5 and len(set(out['choices'])) == 5, it['id']
                mcq.append(out)
        meq = []
        for m in L.get('meq', []) + L.get('osce', []):
            if not m['id'].startswith(prefix):
                continue
            o = {k: v for k, v in m.items() if not k.startswith('_') and k != 'years'}
            o['lec'], o['lecture'] = dlec, name
            meq.append(o)
        for it in mcq + meq:
            nl_codes |= set(it.get('nl', []))
        mf, ef = f'data/{setk}_mcq_{tag}.json', f'data/{setk}_meq_{tag}.json'
        dump(os.path.join(drill, mf), mcq)
        dump(os.path.join(drill, ef), meq)
        s = sets[setk]
        late = s.setdefault('mcq_late', [])
        if mf not in late:
            late.append(mf)
        if ef not in s['meq']:
            s['meq'].append(ef)
        if newlec:
            cfg['lectures'][dlec] = newlec
        order = s['lecture_order']
        if dlec not in order:
            a = AFTER.get(dlec)
            order.insert(order.index(a) + 1 if a in order else 0, dlec)
        report.append(f'{setk:7s} {dlec:4s} MCQ {len(mcq):2d} · MEQ/OSCE {len(meq)} ← learn {fn} {lec}')
    for k, b in BLURB.items():
        sets[k]['blurb'] = b
    dump(cfg_p, cfg)
    return nl_codes, report


def add_nl(drill, codes):
    p = os.path.join(drill, 'refs', 'nl_2567.json')
    ref = json.load(open(p, encoding='utf-8'))
    full = json.load(open(os.path.join(LEARN, 'nl.json'), encoding='utf-8'))
    added, missing = [], []
    for c in sorted(codes):
        if c in ref['entries']:
            continue
        if c not in full:
            missing.append(c)
            continue
        e = full[c]
        ref['entries'][c] = {k: e[k] for k in ('part', 'section', 'page', 'title') if k in e}
        added.append(c)
    dump(p, ref)
    return added, missing


def patch_build(drill):
    p = os.path.join(drill, 'build.py')
    t = open(p, encoding='utf-8').read()
    if "mcq_late" in t:
        return False
    rep = [
        ("        mcq = load_many(s.get('mcq', []))\n",
         "        mcq = load_many(s.get('mcq', []))\n"
         "        # mcq_late = ข้อจากบทเรียน (MED421 learn) จัดลำดับตัวเลือกมาแล้ว — ไม่สลับ และไม่ดึงเลขสุ่ม\n"
         "        #            ข้อเดิมจึงได้ลำดับตัวเลือกเท่าเดิมทุกข้อ (คำตอบที่บันทึกไว้เก็บเป็นเลขตำแหน่ง)\n"
         "        late = load_many(s.get('mcq_late', []))\n"),
        ("        for it in mcq + meq:\n            names.setdefault",
         "        for it in mcq + late + meq:\n            names.setdefault"),
        ("        validate(k, mcq, meq, oldg, CFG['lectures'])\n",
         "        validate(k, mcq + late, meq, oldg, CFG['lectures'])\n"),
        ("            it['answer'] = it['choices'].index(correct)\n",
         "            it['answer'] = it['choices'].index(correct)\n        mcq = mcq + late\n"),
    ]
    for a, b in rep:
        assert t.count(a) == 1, a
        t = t.replace(a, b)
    open(p, 'w', encoding='utf-8').write(t)
    return True


APPLYHASH = '''
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
'''

SYNC_JS = r"""
/* ---------- บันทึกคำตอบในบัญชี (capability db + user) ----------
   data/users/<id>/drill = {answers, shown} · localStorage ยังเป็นสำเนาในเครื่อง (ใช้ตอนไม่ได้ล็อกอิน)
   SYNC.sent = สิ่งที่อยู่ในบัญชีล่าสุดที่รู้ · meta.cloud = เครื่องนี้เคยซิงก์แล้ว · meta.pend = มีของในเครื่องที่ยังไม่ได้อัปโหลด */
var MKEY="med421-drill-v1:sync";
var SYNC={mode:"local",ref:null,uid:"",busy:0,timer:null,first:1,sent:"",err:"",meta:{cloud:false,pend:false,uid:""}};
try{var mm=JSON.parse(localStorage.getItem(MKEY)||"{}");SYNC.meta.cloud=!!mm.cloud;SYNC.meta.pend=!!mm.pend;SYNC.meta.uid=typeof mm.uid==="string"?mm.uid:"";}catch(e){}
function saveMeta(){try{localStorage.setItem(MKEY,JSON.stringify(SYNC.meta));}catch(e){}}
function normA(a){var r={};if(a&&typeof a==="object")Object.keys(a).sort().forEach(function(k){var v=a[k];
  if(v&&typeof v==="object"&&typeof v.pick==="number"&&v.pick>=0&&v.pick<10&&v.pick===Math.floor(v.pick)){
    r[k]={pick:v.pick,ok:!!v.ok};if(v.auto)r[k].auto=1;}});return r;}
function normS(s){var r={};if(s&&typeof s==="object")Object.keys(s).sort().forEach(function(k){if(s[k])r[k]=1;});return r;}
function norm(o){o=o||{};return {answers:normA(o.answers),shown:normS(o.shown)};}
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
  if(c.length>600000){SYNC.err="คำตอบเยอะเกินที่บัญชีเก็บได้ ส่วนนี้บันทึกในเครื่องนี้";renderSync();return;}
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
function adopt(data){var n=norm(data);state.answers=n.answers;state.shown=n.shown;}
function merge(data){var c=norm(data),l=norm(state);
  state.answers=Object.assign({},c.answers,l.answers);state.shown=Object.assign({},c.shown,l.shown);}
function keep(){try{localStorage.setItem("med421-drill-v1",JSON.stringify(
  {answers:state.answers,shown:state.shown,set:state.set,mode:state.mode}));}catch(e){}}
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
    saveMeta();keep();flush();render();renderSync();return;
  }
  if(SYNC.busy||SYNC.timer||snap.metadata&&snap.metadata.hasPendingWrites)return;
  if(!data)return;
  var c=JSON.stringify(norm(data));
  if(c===cur())return;
  SYNC.sent=c;adopt(data);keep();render();
}
function renderSync(){
  var el=document.getElementById("lsync");if(!el)return;
  el.className="lsync"+(SYNC.mode==="cloud"&&!SYNC.err?(SYNC.busy?" busy":" cloud"):"");
  el.lastChild.textContent=SYNC.err||(SYNC.mode==="cloud"?(SYNC.busy?"กำลังบันทึก…":"บันทึกในบัญชี"):"บันทึกในเครื่องนี้");
  el.title=SYNC.mode==="cloud"?"คำตอบบันทึกในบัญชีของคุณ เปิดเครื่องไหนก็เห็นเหมือนกัน":"ยังไม่ได้เชื่อมบัญชี คำตอบเก็บในเบราว์เซอร์เครื่องนี้ (อาจหายเมื่อเปิดในแอปหรือล้างข้อมูลเบราว์เซอร์)";
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
"""

SYNC_CSS = """.lsync{display:inline-flex;align-items:center;gap:7px;margin-top:10px;font-size:12px;color:var(--ink-3);background:var(--surface-sunk);border-radius:999px;padding:5px 11px;white-space:nowrap}
.lsync i{width:8px;height:8px;border-radius:50%;background:var(--ink-3);flex:none}
.lsync.cloud i{background:var(--ok)} .lsync.busy i{background:var(--miss)}
"""

QUIZ_JS = r"""
/* ---------- สุ่มทำข้อสอบ (โหมด quiz) ----------
   สุ่มจาก MCQ ใหม่ + ข้อสอบเก่าที่มีตัวเลือก · ขอบเขตระบบนี้/ทุกระบบ · ทุกข้อ/ยังไม่เคยทำ/เคยตอบผิด
   คำตอบในชุดสุ่มเก็บใน quiz.ans (ชุดใหม่เริ่มสะอาด) และเขียนทับ state.answers ด้วย → ซิงก์เข้าบัญชีตามปกติ
   รายการข้อของชุดสุ่มเก็บในเครื่อง (med421-drill-quiz) */
var QZ_SCOPE=[{k:"set",label:"ระบบนี้ทุกคาบ"},{k:"all",label:"ทุกระบบ"}];
var QZ_NS=[10,20,50,100];
var QZ_POOL=[{k:"any",label:"ทุกข้อ"},{k:"fresh",label:"ยังไม่เคยทำ"},{k:"wrong",label:"เคยตอบผิด"}];
var QKEY="med421-drill-quiz";
var quiz={scope:"set",n:20,pool:"any",ids:[],ans:{},set:"",from:""};
try{var qr=JSON.parse(localStorage.getItem(QKEY)||"null");if(qr&&typeof qr==="object"){
  if(qr.scope==="set"||qr.scope==="all")quiz.scope=qr.scope;
  if(QZ_NS.indexOf(qr.n)>=0)quiz.n=qr.n;
  if(qr.pool==="any"||qr.pool==="fresh"||qr.pool==="wrong")quiz.pool=qr.pool;
  if(Array.isArray(qr.ids))quiz.ids=qr.ids.filter(function(x){return typeof x==="string";});
  quiz.ans=normA(qr.ans);quiz.set=String(qr.set||"");quiz.from=String(qr.from||"");}}catch(e){}
function qSave(){try{localStorage.setItem(QKEY,JSON.stringify(quiz));}catch(e){}}
var QIDX=null;
function qIndex(){
  if(QIDX)return QIDX;QIDX={};
  SETS.forEach(function(s){var B=BANK[s.k];if(!B)return;
    B.mcq.forEach(function(it){QIDX[it.id]={it:it,set:s.k,kind:"mcq"};});
    B.old.forEach(function(g){g.items.forEach(function(it){if(it.choices&&!QIDX[it.id])QIDX[it.id]={it:it,set:s.k,kind:"old",g:g};});});
  });
  return QIDX;
}
function setLabel(k){var s=SETS.filter(function(x){return x.k===k;})[0];return s?s.label:k;}
function qPool(){
  var idx=qIndex();
  return Object.keys(idx).filter(function(id){
    var e=idx[id];if(quiz.scope==="set"&&e.set!==state.set)return false;
    var a=state.answers[id];
    if(quiz.pool==="fresh")return !a;
    if(quiz.pool==="wrong")return !!(a&&!a.ok&&!a.auto);
    return true;
  });
}
function qShuffle(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t;}return a;}
function qDraw(ids){
  quiz.ids=ids||qShuffle(qPool()).slice(0,quiz.n);quiz.ans={};quiz.set=state.set;
  quiz.from=ids?"ข้อที่ผิดจากชุดก่อน":(quiz.scope==="all"?"ทุกระบบ":setLabel(state.set))+" · "+QZ_POOL.filter(function(p){return p.k===quiz.pool;})[0].label;
  qSave();render();window.scrollTo({top:0});
}
function qItems(){var idx=qIndex();return quiz.ids.filter(function(id){return idx[id];}).map(function(id){return idx[id];});}
function qChips(id,opts,cur,pick){
  var el=document.getElementById(id);el.innerHTML="";
  opts.forEach(function(o){
    var b=document.createElement("button");b.type="button";b.className="chip";
    b.setAttribute("aria-pressed",String(o.k===cur));b.textContent=o.label;
    b.addEventListener("click",function(){pick(o.k);qSave();render();});
    el.appendChild(b);
  });
}
function buildQuizRail(){
  qChips("qzscope",QZ_SCOPE,quiz.scope,function(k){quiz.scope=k;});
  qChips("qzn",QZ_NS.map(function(n){return {k:n,label:n+" ข้อ"};}),quiz.n,function(k){quiz.n=k;});
  qChips("qzpool",QZ_POOL,quiz.pool,function(k){quiz.pool=k;});
  var n=qPool().length;
  document.getElementById("qzinfo").textContent="มีให้สุ่ม "+n+" ข้อ"+(n<quiz.n&&n?" (น้อยกว่าที่เลือก จะได้ "+n+" ข้อ)":"");
  document.getElementById("btn-qdraw").disabled=!n;
}
function qScore(){
  var its=qItems(),done=0,right=0;
  its.forEach(function(e){var a=quiz.ans[e.it.id];if(a){done++;if(a.ok)right++;}});
  return {n:its.length,done:done,right:right};
}
function renderQuiz(stream){
  var its=qItems(),sc=qScore();
  var head=document.createElement("div");head.className="part-head";
  head.innerHTML="<h2>สุ่มทำข้อสอบ</h2><span class='meta'>"+(its.length?"ทำแล้ว "+sc.done+"/"+sc.n:"ยังไม่ได้สุ่ม")+"</span>";
  stream.appendChild(head);
  if(!its.length){
    var pool=qPool().length,c=document.createElement("section");c.className="item qzcard";
    c.innerHTML="<h3 class='topic'>สุ่มข้อสอบมาทำเป็นชุด</h3>"+
      "<p class='stem'>สุ่มจาก MCQ ใหม่และข้อสอบเก่าที่มีตัวเลือก คละทุกคาบ"+(quiz.scope==="all"?" ทุกระบบ":" ของ "+esc(setLabel(state.set)))+
      " · ตั้งขอบเขต จำนวนข้อ และเลือกเฉพาะข้อที่ยังไม่เคยทำหรือเคยตอบผิดได้ที่แถบด้านข้าง</p>"+
      (pool?"":"<p class='lecline'>ไม่มีข้อในเงื่อนไขนี้ — ลองเปลี่ยนเป็น “ทุกข้อ” หรือ “ทุกระบบ”</p>");
    var b=document.createElement("button");b.type="button";b.className="reveal qzgo";
    b.textContent="เริ่มสุ่ม "+Math.min(quiz.n,pool)+" ข้อ";b.disabled=!pool;
    b.addEventListener("click",function(){qDraw();});
    c.appendChild(b);stream.appendChild(c);return;
  }
  var info=document.createElement("p");info.className="oldnote wide";
  info.textContent="ชุดนี้: "+quiz.from+" · "+sc.n+" ข้อ · ตอบแล้วเฉลยทันที กด 1–5 เพื่อตอบข้อที่เห็นอยู่บนจอ";
  stream.appendChild(info);
  its.forEach(function(e,i){
    var el=e.kind==="mcq"?renderMCQ(e.it,i,quiz.ans):renderOldChoice(e.it,e.g,quiz.ans);
    var ih=el.querySelector(".ihead");
    if(ih)ih.insertAdjacentHTML("afterbegin","<span class='tag qzno'>ข้อ "+(i+1)+"/"+sc.n+"</span>"+
      (quiz.scope==="all"||e.set!==state.set?"<span class='tag'>"+esc(setLabel(e.set))+"</span>":""));
    stream.appendChild(el);
  });
  if(sc.done===sc.n){
    var pct=Math.round(sc.right*100/sc.n),s=document.createElement("section");s.className="item qzcard";
    var by={},wrong=[];
    its.forEach(function(e){var a=quiz.ans[e.it.id];by[e.set]=by[e.set]||{n:0,r:0};by[e.set].n++;if(a.ok)by[e.set].r++;else wrong.push(e.it.id);});
    var rows=Object.keys(by).map(function(k){return "<li><b>"+esc(setLabel(k))+"</b> "+by[k].r+"/"+by[k].n+"</li>";}).join("");
    s.innerHTML="<h3 class='topic'>สรุปชุดนี้: ถูก "+sc.right+"/"+sc.n+" ข้อ ("+pct+"%)</h3>"+
      (Object.keys(by).length>1?"<ul class='qzby'>"+rows+"</ul>":"");
    var acts=document.createElement("div");acts.className="railacts qzacts";
    var b1=document.createElement("button");b1.type="button";b1.className="reveal";b1.textContent="สุ่มชุดใหม่";
    b1.addEventListener("click",function(){qDraw();});acts.appendChild(b1);
    if(wrong.length){var b2=document.createElement("button");b2.type="button";b2.className="reveal";
      b2.textContent="ทำข้อที่ผิดอีกรอบ ("+wrong.length+")";b2.addEventListener("click",function(){qDraw(qShuffle(wrong.slice()));});acts.appendChild(b2);}
    s.appendChild(acts);stream.appendChild(s);
  }
}
document.getElementById("btn-qdraw").addEventListener("click",function(){qDraw();});
"""

QUIZ_HTML = """    <div id="quizblock" style="display:none">
      <h2>สุ่มจาก</h2>
      <div class="parts" id="qzscope"></div>
      <h2 class="qzh">จำนวนข้อ</h2>
      <div class="parts" id="qzn"></div>
      <h2 class="qzh">เลือกข้อ</h2>
      <div class="parts" id="qzpool"></div>
      <button class="ghost qzbtn" id="btn-qdraw" type="button">สุ่มชุดใหม่</button>
      <p class="qzinfo" id="qzinfo"></p>
    </div>
"""

QUIZ_CSS = """.ihead .tag{white-space:normal;max-width:100%}
.qzh{margin-top:16px!important}
.qzbtn{margin-top:16px;width:100%}
.qzbtn[disabled]{opacity:.5;cursor:default}
.qzinfo{margin:10px 0 0;font-size:12.5px;color:var(--ink-3)}
.tag.qzno{color:var(--on-accent);background:var(--accent);font-weight:600}
.qzcard .reveal{margin-top:6px}
.reveal.qzgo{font-size:14px;padding:11px 22px;background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.reveal.qzgo:hover{background:var(--accent-ink);border-color:var(--accent-ink)}
.reveal.qzgo[disabled]{opacity:.5;cursor:default}
.qzby{margin:4px 0 12px;padding-inline-start:18px;color:var(--ink-2);font-size:14px}
.qzacts{background:none;border:0;box-shadow:none;padding:0}
"""


def patch_quiz(t):
    """โหมดสุ่มทำข้อสอบ — ต้องรันหลัง account-sync (ใช้ normA)"""
    if 'function qDraw' in t:
        return t, False
    rep = [
        # renderMCQ / renderOldChoice รับที่เก็บคำตอบได้ (โหมดสุ่มใช้ quiz.ans)
        ('function renderMCQ(it,idx){', 'function renderMCQ(it,idx,store){store=store||state.answers;'),
        ('function renderOldChoice(it,g){', 'function renderOldChoice(it,g,store){store=store||state.answers;'),
        ('{k:"hot",label:"ออกบ่อย"}];', '{k:"hot",label:"ออกบ่อย"},{k:"quiz",label:"สุ่มทำข้อสอบ"}];'),
        ('  if(!mcounts[state.mode]){state.mode="new";save();}',
         '  if(!mcounts[state.mode]&&state.mode!=="quiz"){state.mode="new";save();}'),
        ('    MODES.filter(function(m){return m.k==="new"||mcounts[m.k]>0;}),state.mode,function(k){',
         '    MODES.filter(function(m){return m.k==="new"||m.k==="quiz"||mcounts[m.k]>0;}),state.mode,function(k){'),
        ('  var showBtns=(state.mode==="new")||oldHasCh||state.mode==="hot"||state.mode==="year";',
         '  var qz=state.mode==="quiz";\n'
         '  document.getElementById("lecbar").parentNode.style.display=qz?"none":"";\n'
         '  document.getElementById("quizblock").style.display=qz?"":"none";\n'
         '  if(qz)buildQuizRail();\n'
         '  var showBtns=!qz&&((state.mode==="new")||oldHasCh||state.mode==="hot"||state.mode==="year");'),
        ('  if(state.mode==="new")renderNew(stream);\n',
         '  if(qz)renderQuiz(stream);\n  else if(state.mode==="new")renderNew(stream);\n'),
        ('function updateScore(){\n',
         'function updateScore(){\n'
         '  if(state.mode==="quiz"){var q=qScore(),qp=q.done?Math.round(q.right/q.done*100):0;\n'
         '    document.getElementById("sc-done").textContent=q.done;document.getElementById("sc-right").textContent=q.right;\n'
         '    var qa=document.getElementById("sc-acc");qa.textContent=q.done?qp+"%":"—";qa.style.setProperty("--pct",qp);\n'
         '    document.getElementById("railnote").innerHTML="<b>สุ่มทำข้อสอบ</b> คะแนนด้านบนนับเฉพาะชุดที่สุ่มอยู่ · คำตอบนับรวมในแต่ละระบบด้วย และบันทึกในบัญชีของคุณ";\n'
         '    return;}\n'),
        ('    <div class="railacts">\n', QUIZ_HTML + '    <div class="railacts">\n'),
        ('.scoreboard{', QUIZ_CSS + '.scoreboard{'),
        ('/* ---------- actions ---------- */', QUIZ_JS + '\n/* ---------- actions ---------- */'),
    ]
    for a, b in rep:
        assert t.count(a) == 1, a[:70]
        t = t.replace(a, b)
    # ทั้งสองฟังก์ชัน: อ่าน/เขียนคำตอบผ่าน store (เขียน state.answers ด้วยเสมอ)
    for fn in ('function renderMCQ(', 'function renderOldChoice('):
        i = t.index(fn)
        j = t.index('\nfunction ', i + 10)
        body = t[i:j]
        assert body.count('var ans=state.answers[it.id];') == 1
        assert body.count('state.answers[it.id]={pick:ci,ok:ci===it.answer};') == 1
        body = body.replace('var ans=state.answers[it.id];', 'var ans=store[it.id];')
        body = body.replace('state.answers[it.id]={pick:ci,ok:ci===it.answer};',
                            'store[it.id]=state.answers[it.id]={pick:ci,ok:ci===it.answer};if(store===quiz.ans)qSave();')
        t = t[:i] + body + t[j:]
    return t, True


def patch_template(drill):
    p = os.path.join(drill, 'template.html')
    t = open(p, encoding='utf-8').read()
    done = []
    if 'function applyHash' not in t:
        a = '\n\nrender();\n})();\n</script>'
        assert t.count(a) == 1
        t = t.replace(a, '\n' + APPLYHASH + '\nrender();\n})();\n</script>')
        done.append('applyHash')
    old = ('  if(it.vignette)h+="<div class=\'vign\'>"+inline(it.vignette)+"</div>";\n'
           '  if(it.instruction)h+="<div class=\'vign\'>"+inline(it.instruction)+"</div>";\n')
    new = ('  if(it.vignette)h+=vign(it.vignette);\n'
           '  if(it.instruction)h+=vign(it.instruction);\n')
    if old in t:
        t = t.replace(old, new)
        a = 'function md(src){'
        t = t.replace(a, '/* โจทย์ MEQ/OSCE: มีตาราง → เรนเดอร์ด้วย md() ไม่งั้นคงบรรทัดเดิม (pre-wrap) */\n'
                         'function vign(s){return /^\\s*\\|/m.test(s)?"<div class=\'vign md vmd\'>"+md(s)+"</div>":'
                         '"<div class=\'vign\'>"+inline(s)+"</div>";}\n' + a, 1)
        a = '.vign strong{font-weight:600}'
        t = t.replace(a, a + '\n.vign.vmd{white-space:normal}', 1)
        done.append('vign-md')
    if 'data/users/' not in t:
        # บันทึกคำตอบในบัญชี — publish พร้อม capabilities {db:{}, user:{}}
        a = 'function save(){try{localStorage.setItem("med421-drill-v1",JSON.stringify(\n  {answers:state.answers,shown:state.shown,set:state.set,mode:state.mode}));}catch(e){}}\n'
        assert t.count(a) == 1
        t = t.replace(a, a.replace('catch(e){}}', 'catch(e){}if(typeof syncCheck==="function")syncCheck();}') + SYNC_JS)
        a = '.scoreboard{'
        assert t.count(a) == 1
        t = t.replace(a, SYNC_CSS + a)
        a = re.search(r'(<div class="brand">.*?</p>)', t, re.S).group(1)
        t = t.replace(a, a + '\n        <span class="lsync" id="lsync" role="status"><i></i><span>บันทึกในเครื่องนี้</span></span>', 1)
        a = '\nrender();\n})();\n</script>'
        assert t.count(a) == 1
        t = t.replace(a, '\nrender();renderSync();\n})();\n</script>')
        done.append('account-sync')
    a = 'ความคืบหน้าถูกเก็บไว้ในเบราว์เซอร์นี้'
    if a in t:
        t = t.replace(a, 'ความคืบหน้าบันทึกในบัญชีของคุณ (ถ้ายังไม่ได้เชื่อมบัญชีจะเก็บในเบราว์เซอร์นี้)')
        done.append('railnote')
    t, q = patch_quiz(t)
    if q:
        done.append('quiz')
    open(p, 'w', encoding='utf-8').write(t)
    return done


def main():
    if len(sys.argv) != 2 or not os.path.exists(os.path.join(sys.argv[1], 'build.py')):
        sys.exit(__doc__)
    drill = sys.argv[1]
    codes, report = convert(drill)
    added, missing = add_nl(drill, codes)
    print('\n'.join(report))
    print(f'NL: เติม {len(added)} รหัส' + (f' · ไม่พบในประกาศ {missing}' if missing else ''))
    print('build.py:', 'patched' if patch_build(drill) else 'มี mcq_late แล้ว')
    print('template.html:', patch_template(drill) or 'ครบแล้ว')


if __name__ == '__main__':
    main()
