# สร้างภาพเคลื่อนไหว "mechanical hemolysis" (chronic DIC + prosthetic valve) สำหรับ Salmon NL hemato-02-01
import json, sys

RBC = lambda x, y, extra="": (
    f'<g transform="translate({x},{y})"{extra}><ellipse rx="15" ry="9" class="badsoft"/>'
    f'<ellipse rx="6" ry="3.5" class="box" stroke="none"/></g>')


def frag(x, y, d, dur, kind=0):
    shapes = ['M-9,3 Q-9,-8 3,-8 L8,-1 L2,0 L4,5 Z',      # helmet
              'M-6,4 L0,-7 L6,4 Z',                       # triangle
              'M-7,2 Q0,-8 7,2 Q0,-1 -7,2 Z']             # crescent
    return (f'<path d="{shapes[kind]}" transform="translate({x},{y})" class="bad">'
            f'<animateMotion dur="{dur}s" repeatCount="indefinite" path="{d}"/></path>')


svg = f'''<svg viewBox="0 0 440 432" role="img" aria-label="ภาพเคลื่อนไหว: เม็ดเลือดแดงถูกฉีกขาดเชิงกลจากเส้น fibrin ใน DIC เรื้อรังและแรงเฉือนจากลิ้นหัวใจเทียม กลายเป็น schistocyte แตกในหลอดเลือด" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="sal-mh-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
<text x="20" y="24" class="tb">หลอดเลือดเล็ก</text>
<text x="420" y="24" text-anchor="end" class="t3" data-s="2">fibrin ค้างใน DIC เรื้อรัง</text>
<rect x="20" y="36" width="400" height="74" rx="6" class="sunk"/>
<path d="M20 36H420M20 110H420" class="ln"/>
<g data-x="2">
  <g transform="translate(36,73)"><ellipse rx="15" ry="9" class="badsoft"/><ellipse rx="6" ry="3.5" class="box" stroke="none"/><animateMotion dur="4.5s" repeatCount="indefinite" path="M0,0 H350"/></g>
  <g transform="translate(-120,73)"><ellipse rx="15" ry="9" class="badsoft"/><ellipse rx="6" ry="3.5" class="box" stroke="none"/><animateMotion dur="4.5s" begin="1.5s" repeatCount="indefinite" path="M156,0 H506"/></g>
  <text x="220" y="130" text-anchor="middle" class="t3">RBC ปกติ: เว้าสองด้าน นิ่ม ยืดหยุ่น บีบตัวผ่านได้ · อายุ ~120 วัน</text>
</g>
<g data-s="2">
  <path d="M196 38L232 108M214 38L188 108M226 38L250 108M240 38L214 108M206 74H246" class="lnc2"/>
  <g transform="translate(40,73)"><ellipse rx="15" ry="9" class="badsoft"/><ellipse rx="6" ry="3.5" class="box" stroke="none"/><animateMotion dur="2.2s" repeatCount="indefinite" path="M0,0 H150"/></g>
  {frag(262, 62, "M0,0 H150", 2.2, 0)}
  {frag(258, 84, "M0,0 H150", 2.2, 1)}
  {frag(270, 74, "M0,0 H140", 2.6, 2)}
</g>
<g data-s="3">
  <path d="M330 118L338 98" class="ln" marker-end="url(#sal-mh-a)"/>
  <text x="330" y="132" text-anchor="middle" class="ta">schistocyte (helmet cell)</text>
  <text x="220" y="150" text-anchor="middle" class="t3">RBC ชนเส้น fibrin แล้วถูกตัดขาด → แตกในหลอดเลือด (intravascular)</text>
  <text x="220" y="166" text-anchor="middle" class="t3">เกล็ดเลือดถูกใช้ไปกับลิ่มเลือด → platelet ต่ำ = MAHA + thrombocytopenia</text>
</g>
<g data-s="4">
  <text x="20" y="196" class="tb">ลิ้นหัวใจเทียม</text>
  <text x="420" y="196" text-anchor="end" class="t3">mechanical valve / รั่วรอบลิ้น</text>
  <rect x="20" y="206" width="400" height="84" rx="6" class="sunk"/>
  <path d="M20 206H420M20 290H420" class="ln"/>
  <rect x="140" y="207" width="16" height="30" rx="3" class="box"/>
  <rect x="140" y="259" width="16" height="30" rx="3" class="box"/>
  <path d="M160 248H300" class="lna fl" marker-end="url(#sal-mh-a)"/>
  <path d="M160 242C200 230 240 226 290 222" class="lna fl"/>
  <path d="M160 254C200 266 240 270 290 274" class="lna fl"/>
  <g transform="translate(60,248)"><ellipse rx="15" ry="9" class="badsoft"/><ellipse rx="6" ry="3.5" class="box" stroke="none"/><animateMotion dur="1.6s" repeatCount="indefinite" path="M0,0 H80"/></g>
  {frag(190, 240, "M0,0 H200", 1.1, 0)}
  {frag(200, 256, "M0,0 H190", 1.3, 1)}
  {frag(215, 248, "M0,0 H180", 0.9, 2)}
  <text x="148" y="302" text-anchor="middle" class="t3">ช่องลิ้นแคบ/รั่ว</text>
  <text x="330" y="302" text-anchor="middle" class="ta">แรงเฉือนสูง (shear) ฉีก RBC</text>
</g>
<g data-s="5">
  <rect x="20" y="318" width="194" height="76" rx="8" class="badsoft"/>
  <text x="117" y="338" text-anchor="middle" class="tb">ในเลือด</text>
  <text x="117" y="357" text-anchor="middle" class="t3">Hb อิสระจับ haptoglobin หมด</text>
  <text x="117" y="373" text-anchor="middle" class="t3">haptoglobin ↓↓ · LDH ↑</text>
  <text x="117" y="389" text-anchor="middle" class="t3">indirect bilirubin ↑ · retic ↑</text>
  <rect x="226" y="318" width="194" height="76" rx="8" class="c1soft"/>
  <text x="323" y="338" text-anchor="middle" class="tb">ในปัสสาวะ</text>
  <text x="323" y="357" text-anchor="middle" class="t3">hemoglobinuria (สีโค้ก)</text>
  <text x="323" y="373" text-anchor="middle" class="t3">เรื้อรัง → hemosiderinuria</text>
  <text x="323" y="389" text-anchor="middle" class="t3">เสียเหล็กทางไต → ขาดเหล็กได้</text>
  <text x="220" y="414" text-anchor="middle" class="t2">PBS: schistocyte · DAT ลบ (ไม่ใช่ภูมิคุ้มกัน)</text>
</g>
</svg>'''

anim = {
    "id": "hemato-02-01-a1",
    "title": "กลไก: RBC ถูกฉีกเชิงกล (chronic DIC · ลิ้นหัวใจเทียม)",
    "svg": svg,
    "steps": [
        {"t": "RBC ปกติ", "cap": "เม็ดเลือดแดงปกติเว้าสองด้าน นิ่มและยืดหยุ่น จึง **บีบตัวผ่านหลอดเลือดเล็ก** และช่องในม้ามได้ อยู่ได้ราว **120 วัน**"},
        {"t": "Chronic DIC: เส้น fibrin ขวางทาง", "cap": "ใน DIC เรื้อรัง (เช่น **มะเร็ง**, aortic aneurysm, giant hemangioma) มีการสร้าง thrombin ต่อเนื่อง → **เส้น fibrin ค้างเป็นตาข่าย** ในหลอดเลือดเล็ก RBC ที่ไหลผ่านจึงชนเส้นเหล่านี้"},
        {"t": "Schistocyte → แตกในหลอดเลือด", "cap": "แรงไหลดึง RBC ผ่านเส้น fibrin จน **ถูกตัดเป็นชิ้น** (helmet cell, triangle) = **schistocyte** · ชิ้นเล็กแตกต่อใน **หลอดเลือด** และเกล็ดเลือดถูกใช้ไปกับลิ่ม → platelet ต่ำ"},
        {"t": "ลิ้นหัวใจเทียม: แรงเฉือนสูง", "cap": "ไม่ต้องมี fibrin ก็ได้: ช่องลิ้นเทียมที่แคบ เสื่อม หรือ **รั่วรอบลิ้น (paravalvular leak)** ทำให้เลือดพุ่งเร็วและปั่นป่วน → **shear stress** ฉีก RBC โดยตรง (macroangiopathic) · เป็นได้นานเท่าที่ลิ้นยังผิดปกติ จึงจัดเป็น **chronic, extrinsic**"},
        {"t": "ผลที่ตรวจพบ", "cap": "Hb อิสระจับ haptoglobin จน **haptoglobin ↓↓**, **LDH ↑** · ไตกรอง Hb → **hemoglobinuria** · ถ้าเรื้อรัง เหล็กค้างในเซลล์ท่อไตแล้วหลุดออกมา = **hemosiderinuria** → ขาดเหล็กได้ · PBS เห็น **schistocyte**, **DAT ลบ**"}
    ]
}

md_add = """
### กลไกของแต่ละช่องในตาราง (ทำไมเม็ดเลือดแดงถึงแตก)

- **Intrinsic · chronic — โครงสร้าง RBC ผิดตั้งแต่เกิด:** HS/HE ขาดโปรตีนโครงร่างเยื่อหุ้ม (spectrin, ankyrin) → เยื่อหุ้มหลุดเป็นถุงเล็ก ๆ จน RBC กลมแข็ง (spherocyte) → **ติดค้างในม้าม** ถูก macrophage กิน (extravascular) · thalassemia สร้าง globin ไม่สมดุล → สายที่เกินตกตะกอนในเซลล์ → ถูกทำลายทั้งในไขกระดูก (ineffective erythropoiesis) และม้าม · **PNH** ขาดโปรตีนยึดด้วย GPI (CD55, CD59) ที่ปกติกัน complement → **complement เจาะเยื่อหุ้มในหลอดเลือด** โดยเฉพาะตอนนอน
- **Intrinsic · acute — มีตัวกระตุ้นจากภายนอกมาเปิดจุดอ่อน:** **G6PD** ต่ำ → สร้าง NADPH ไม่พอ → glutathione ไม่พอสู้ oxidant (ไข้ติดเชื้อ ยา ถั่วปากอ้า) → Hb ตกตะกอนเป็น **Heinz body** → ม้ามตัดออกเป็น **bite cell** และแตกในหลอดเลือดเฉียบพลัน (ปัสสาวะสีโค้ก)
- **Extrinsic · chronic — RBC ปกติแต่สิ่งแวดล้อมทำร้ายต่อเนื่อง:** **chronic DIC** มีเส้น fibrin ค้างในหลอดเลือดเล็ก · **ลิ้นหัวใจเทียมผิดปกติ** มีแรงเฉือนสูง → RBC ถูกฉีกเชิงกลเป็น **schistocyte** แตกในหลอดเลือด (ดูภาพเคลื่อนไหวด้านล่าง)
- **Extrinsic · acute — มีสิ่งโจมตีเกิดขึ้นทันที:** **AIHA** IgG เคลือบ RBC → macrophage ในม้ามกัดเยื่อหุ้มทีละส่วน → spherocyte (extravascular · **DAT บวก**) · **MAHA เฉียบพลัน** (DIC, TTP, HUS, HELLP) ลิ่มเลือดในหลอดเลือดเล็กฉีก RBC แบบเดียวกับ chronic DIC แต่เร็วและรุนแรง · **malaria** เชื้อโตในเซลล์แล้วแตกออก

[[anim:hemato-02-01-a1]]
"""

if __name__ == "__main__":
    src, out = sys.argv[1], sys.argv[2]
    d = json.load(open(src, encoding="utf-8"))
    s = [x for L in d for x in L["sections"] if x["id"] == "hemato-02-01"][0]
    key = "(PNH เป็นความผิดปกติ intrinsic แต่ถูกทำลายด้วย complement — เสริม)"
    assert key in s["md"] and "[[anim:" not in s["md"]
    s["md"] = s["md"].replace(key, key + "\n" + md_add, 1)
    s["anims"] = {anim["id"]: {k: anim[k] for k in ("title", "svg", "steps")}}
    json.dump(d, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print("ok")
