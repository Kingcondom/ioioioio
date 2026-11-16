import sys
p=open(sys.argv[1],encoding='utf-8').read()
def R(o,n):
    global p
    assert p.count(o)==1,(p.count(o),o[:80])
    p=p.replace(o,n)
# 1) background no longer fixed-attached; the two decorative blobs scroll with the page and use gradients instead of a 60px blur filter
R("linear-gradient(160deg,#eef2fb,#dfe6f6 60%,#e8e6f8);background-attachment:fixed}",
  "linear-gradient(160deg,#eef2fb,#dfe6f6 60%,#e8e6f8)}")
R('body::before,body::after{content:"";position:fixed;z-index:-1;border-radius:50%;filter:blur(60px);opacity:.55;pointer-events:none}',
  'body{position:relative}\nbody::before,body::after{content:"";position:absolute;z-index:-1;border-radius:50%;opacity:.55;pointer-events:none}')
R("body::before{width:46vmax;height:46vmax;right:-14vmax;top:-12vmax;background:linear-gradient(135deg,#ffffff,#a9c1ff)}",
  "body::before{width:46vmax;height:46vmax;right:-14vmax;top:-12vmax;background:radial-gradient(closest-side,#a9c1ff,rgba(169,193,255,0))}")
R("body::after{width:40vmax;height:40vmax;left:-16vmax;bottom:-10vmax;background:linear-gradient(135deg,#b7c8ff,#ffffff)}",
  "body::after{width:40vmax;height:40vmax;left:-16vmax;top:60vh;background:radial-gradient(closest-side,#b7c8ff,rgba(183,200,255,0))}\nhtml,body{overflow-x:clip}")
# 2) frosted blur only where something actually slides under it (sticky header, floating nav); in-page cards get a slightly more opaque fill instead
R(".wrap{max-width:1100px;margin:0 auto;padding:16px}",
  "/* แอปรัวตอนเลื่อน (ผู้ใช้บอก 15 พ.ย.) — เบลอเฉพาะแถบบน/แถบล่างที่มีเนื้อหาเลื่อนผ่าน การ์ดในหน้าใช้พื้นทึบขึ้นแทน */\n"
  ".glass:not(header):not(.nav){-webkit-backdrop-filter:none;backdrop-filter:none;background:rgba(255,255,255,.66)}\n"
  ".wrap{max-width:1100px;margin:0 auto;padding:16px}")
# 3) clock: write the text only when the shown value changes
R("const tick=()=>{const left=(end-Date.now())/1000;c.textContent=fmt(left);",
  "let shown=\"\";const tick=()=>{const left=(end-Date.now())/1000,f=fmt(left);if(f!==shown){shown=f;c.textContent=f}")
open(sys.argv[2],'w',encoding='utf-8').write(p)
print("ok")
