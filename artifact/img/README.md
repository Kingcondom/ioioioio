# ไฟล์ภาพของ artifact

ภาพเหล่านี้เป็นไฟล์ที่ publish ไปกับ artifact (อ้างถึงจาก `data/*.json`)
จึงต้องเก็บไว้ใน repo ด้วย ไม่ใช่สร้างใหม่ได้จากสคริปต์

- `pbs/p-*.jpg` · `pbs/s-*.jpg` — ภาพ peripheral blood smear ของชุด Heme/Onc

ดึงกลับจาก artifact ได้ด้วย
`Artifact action:read` + `paths:[...]` + `out_dir:/home/user/ioioioio/artifact`
(ดูรายชื่อไฟล์ทั้งหมดด้วย `Artifact action:list scope:files`)
