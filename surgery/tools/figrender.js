// node figrender.js <lecture.json>... [--png outdir]
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const args=process.argv.slice(2);let png=null;const i=args.indexOf('--png');if(i>=0){png=args[i+1];args.splice(i,2);fs.mkdirSync(png,{recursive:true});}
const base=fs.readFileSync(path.join(__dirname,'figbase.html'),'utf8');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:600,height:800},deviceScaleFactor:png?2:1});
 await p.setContent(base);await p.waitForTimeout(300);let total=0;
 for(const f of args){const L=JSON.parse(fs.readFileSync(f,'utf8'));
  for(const s of L.sections){const jobs=[];for(const [k,fg] of Object.entries(s.figs||{}))jobs.push([k,fg.svg,0]);
   for(const [k,a] of Object.entries(s.anims||{}))for(let st=1;st<=(a.steps||[]).length;st++)jobs.push([k+'@step'+st,a.svg,st]);
   for(const [k,svgsrc,step] of jobs){const fg={svg:svgsrc};
   const res=await p.evaluate(([svg,step])=>{const r=document.getElementById('root');
     r.innerHTML="<figure class='fig' style='width:540px'><div class='figsv'><div class='figin'>"+svg+"</div></div></figure>";
     const sv=r.querySelector('svg');if(!sv)return ['no svg'];
     if(step){sv.querySelectorAll('[data-s],[data-x]').forEach(el=>{const a=el.getAttribute('data-s'),x=el.getAttribute('data-x');if((a&&+a>step)||(x&&+x<=step))el.remove();});}const vb=sv.viewBox.baseVal;const probs=[];
     const T=[...sv.querySelectorAll('text')];const bbs=T.map(t=>{try{return t.getBBox()}catch(e){return null}});
     const txt=t=>t.textContent.trim().slice(0,30);
     T.forEach((t,i)=>{const bb=bbs[i];if(!bb||!bb.width)return;
       if(bb.x<vb.x-1||bb.y<vb.y-1||bb.x+bb.width>vb.x+vb.width+1||bb.y+bb.height>vb.y+vb.height+1)probs.push('text outside viewBox: "'+txt(t)+'"');});
     for(let i=0;i<T.length;i++)for(let j=i+1;j<T.length;j++){const a=bbs[i],c=bbs[j];if(!a||!c||!a.width||!c.width)continue;
       const ox=Math.min(a.x+a.width,c.x+c.width)-Math.max(a.x,c.x),oy=Math.min(a.y+a.height,c.y+c.height)-Math.max(a.y,c.y);
       if(ox>2&&oy>3)probs.push('labels overlap: "'+txt(T[i])+'" / "'+txt(T[j])+'"');}
     // text sticking out of the smallest rect that contains its start point
     const R=[...sv.querySelectorAll('rect')].map(r=>r.getBBox()).filter(r=>r.width>20&&r.height>12);
     T.forEach((t,i)=>{const bb=bbs[i];if(!bb||!bb.width)return;const cx=bb.x+Math.min(bb.width,8),cy=bb.y+bb.height/2;
       const host=R.filter(r=>cx>=r.x&&cx<=r.x+r.width&&cy>=r.y&&cy<=r.y+r.height).sort((a,b)=>a.width*a.height-b.width*b.height)[0];
       if(host&&(bb.x+bb.width>host.x+host.width+1.5||bb.y+bb.height>host.y+host.height+2||bb.y<host.y-2))probs.push('text sticks out of its box: "'+txt(t)+'"');});
     return probs;},[fg.svg,step]);
   if(res.length){total+=res.length;console.log(`${path.basename(f)} ${s.id}/${k}:`);res.forEach(x=>console.log('   ',x));}
   if(png){const el=await p.$('#root figure');await el.screenshot({path:path.join(png,`${s.id}_${k.replace('@','_')}.png`)});}
  }}}
 console.log('problems:',total);await b.close();process.exit(total?1:0);})();
