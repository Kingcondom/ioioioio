import json,re,sys,collections
s=open(sys.argv[1],encoding='utf-8').read()
i=s.index('<script type="application/json" id="bank">')+len('<script type="application/json" id="bank">');j=s.index('</script>',i)
B=json.loads(s[i:j])
items=[]
def walk(o,path):
  if isinstance(o,dict):
    if isinstance(o.get('choices'),list) and isinstance(o.get('answer'),int):items.append((path,o))
    for k,v in o.items():walk(v,path+[k])
  elif isinstance(o,list):
    for x in o:walk(x,path)
walk(B,[])
print('items',len(items), 'top keys',list(B.keys()))
par=lambda t:'(' in t or '（' in t
flag=collections.Counter();ex=[]
for p,o in items:
  ch=[str(c) for c in o['choices']];a=o['answer']
  if not(0<=a<len(ch)):continue
  c=ch[a];d=[x for k,x in enumerate(ch) if k!=a]
  if not d:continue
  f=[]
  if par(c) and not any(par(x) for x in d):f.append('paren')
  if len(c)>1.4*max(len(x) for x in d) and len(c)-max(len(x) for x in d)>12:f.append('long')
  if f:
    flag[(p[0],'+'.join(f))]+=1;ex.append((o.get('id'),f,c,d))
print(sum(flag.values()));
for k,v in sorted(flag.items()):print(k,v)
json.dump([{'id':e[0],'f':e[1],'c':e[2],'d':e[3]} for e in ex],open(sys.argv[2],'w',encoding='utf-8'),ensure_ascii=False,indent=0)
