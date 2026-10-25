# งาน: คาบ "อ่าน Peripheral Blood Smear — ตาม Atlas ของ อ.Chaicharoen Tantanate" ใน MED421 learn

ผู้ใช้ (นศพ.ปี 4 ไทย) ขอ: **"เอาไฟล์นี้ของอาจารย์มาสอนอ่าน PBS หน่อย แปะรูปอาจารย์ไว้เลย"**
ไฟล์ = Atlas of Blood Smears in Common Hematologic Diseases (Chaicharoen Tantanate, v.01.2025) — ผู้เขียนอนุญาตให้แชร์ฟรีเพื่อการศึกษา (ห้ามขาย)
**ภาพ smear ในหนังสือผู้เขียนระบุว่าสร้างด้วย AI ตามการตีความของผู้เขียน ไม่ใช่เคสจริง** — บอกผู้เรียนไว้ในหัวข้อแรก

## วัตถุดิบ
- รูปทั้งหน้าของอาจารย์ (มีหัวเรื่อง ภาพ smear ป้ายชี้ และตาราง RBC/WBC/Platelet): `PUB/img/pbs/p-NN.jpg` (NN = เลขหน้า 01, 08–57)
- รูป smear ล้วนที่ฝังในหนังสือ (ไม่มีป้ายชื่อโรค เหมาะทำแบบฝึกทาย): `PUB/img/pbs/s-PPP-N.jpg` (PPP = หน้าที่มา)
- ข้อความทั้งเล่ม: `PBSDIR/atlas_text.txt` · **เปิดดูรูปทุกหน้าในช่วงของคุณด้วย Read** ก่อนเขียน (ข้อความที่สกัดได้บางทีลำดับเพี้ยน)
- ตัวอย่างรูปแบบ section ของ learn: ดู `BASE/hemonc.json` คาบ "9/11" (anemia) ที่เพิ่งทำ

## ส่งงาน `OUT/sec_<G>.json` = list ของ section
```json
{"id":"hon-pbs-NN","title":"…","minutes":10,"summary":"…",
 "source":"Atlas of Blood Smears (อ.Chaicharoen Tantanate) หน้า X–Y",
 "nl":["รหัสจาก BASE/nl.json"],
 "md":"### …\n[[img:p20]]\n…",
 "imgs":{"p20":{"src":"img/pbs/p-20.jpg","title":"Thalassemia traits — α-thal 1 trait / homozygous α-thal 2 / β-thal trait","alt":"…","credit":"ภาพจาก Atlas of Blood Smears in Common Hematologic Diseases — อ.Chaicharoen Tantanate"}},
 "pearls":["…"],
 "items":[{"id":"HON-PBS-MCQ-NN","kind":"mcq","topic":"…","stem":"…","choices":["","","","",""],"answer":0,"explain":"…","pearl":"…","src":"","ref":["Atlas of Blood Smears (อ.Chaicharoen Tantanate) หน้า X"],"nl":["…"]}],
 "figs":{}}
```
ตรวจ: `cd TOOLS && LEARN_IMG_ROOT=PUB python3 learn_lesson_tool.py check BASE OUT/sec_<G>.json`

## เนื้อหาแต่ละ section (ภาษาไทยปนศัพท์อังกฤษ)
1. **แปะรูปทั้งหน้าของอาจารย์ทุกหน้าในช่วงของคุณ** ตามลำดับหน้า ด้วย `[[img:pNN]]` (credit ทุกรูป)
2. ใต้/ระหว่างรูป: **สอนอ่าน** — "มองหาอะไรก่อน" ทีละขั้น (RBC ขนาด/สี/รูปร่าง/inclusion → WBC → platelet) ชี้ว่าในรูปของอาจารย์ตรงไหนคืออะไร (เช่น "เซลล์ที่มีจุดน้ำเงินเล็ก ๆ ในกรอบขยาย = basophilic stippling")
3. **ทำไมถึงเห็นแบบนี้** — กลไกของแต่ละ finding (ใช้คำอธิบายของอาจารย์เป็นแกน + เติมจากตำราได้ แต่ห้ามขัด) ตาราง | สิ่งที่เห็น | กลไก |
4. **แยกจากภาวะที่หน้าคล้าย** (ตารางถ้ามีในหนังสือใช้ตามนั้น)
5. **สิ่งที่ smear บอกไม่ได้ / ต้องตรวจอะไรต่อ** สั้น ๆ
- เรียบเรียงเป็นภาษาของเราเอง ไม่คัดลอกยาว · ตัวเลข/เกณฑ์ (เช่น grading) ใช้ตามหนังสือได้
- `items`: MCQ 2–3 ข้อต่อ section (ข้อความล้วน ไม่ต้องอ้างรูป) stem อังกฤษแบบ vignette ที่ให้ผล smear เป็นคำบรรยาย → ให้เลือกการวินิจฉัย/กลไก/ตรวจต่อ · 5 ตัวเลือก · explain ไทย ≥ 400 ตัวอักษร · กระจายเฉลย
- `pearls` 3–6 ข้อ · md ≥ 1,500 ตัวอักษร
- ห้ามใส่ `[[anim:]]` · ไม่ต้องทำภาพเคลื่อนไหว

## ห้าม
แก้ไฟล์อื่นนอก OUT/sec_<G>.json และ WORK/<G>/ · ห้าม publish/commit · เขียนแต่ละ section เป็นไฟล์เล็กแยกใน WORK/<G>/ แล้วรวมด้วยสคริปต์สั้น ๆ (อย่าเขียนไฟล์ยักษ์ครั้งเดียว — อาจถูกตัด)

## รายงานตอนจบ (สั้น)
section ที่ทำ · หน้า/รูปที่ใช้ · จำนวน items · ข้อที่ไม่แน่ใจ · ยืนยัน check ผ่าน
