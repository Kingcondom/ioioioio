"""เทียบรายการโรค NL 2567 (ข.2.3 โรคตามระบบ + ข.2.2 ภาวะฉุกเฉิน) กับแก่นโพย
สถานะ: Y = มีแก่นตรง, P = แตะแค่บางส่วน/มุมเดียว, N = ไม่เคยออกในโพย, X = นอกขอบเขตอายุรกรรม (ศัลย์ สูติ เด็ก ตา หูคอจมูก จิตเวช ออร์โธ)
ตัดสินจากชื่อแก่นใน analysis/themes/ ร่วมกับค้นคำในโจทย์+คำตอบของข้อสอบเก่าทุกข้อ
"""
import json, os
R = """
2.3.1 ติดเชื้อ|2|Acute viral hepatitis|Y|Hepatitis A, HBV serology
2.3.1 ติดเชื้อ|2|Arthropod-borne viral infection (dengue, chikungunya, zika)|Y|Dengue, chikungunya
2.3.1 ติดเชื้อ|2|Botulism|N|
2.3.1 ติดเชื้อ|2|Diphtheria|P|อยู่ในแก่น pharyngitis ข้อเดียว
2.3.1 ติดเชื้อ|2|Tetanus|Y|
2.3.1 ติดเชื้อ|2|Pertussis|N|
2.3.1 ติดเชื้อ|2|GI infection, food-borne intoxication|Y|Acute watery diarrhea, dysentery, food poisoning
2.3.1 ติดเชื้อ|2|Herpes simplex|Y|
2.3.1 ติดเชื้อ|2|HIV disease|Y|ART, OI, window period
2.3.1 ติดเชื้อ|2|Infectious mononucleosis|N|
2.3.1 ติดเชื้อ|2|Influenza|P|โผล่แค่ในแก่นวัคซีน ไม่มีข้อวินิจฉัย/oseltamivir
2.3.1 ติดเชื้อ|2|Intestinal parasites (ascaris, hookworm, strongyloides, taenia …)|N|
2.3.1 ติดเชื้อ|2|Leptospirosis|Y|
2.3.1 ติดเชื้อ|2|Malaria|Y|
2.3.1 ติดเชื้อ|2|Mumps|N|
2.3.1 ติดเชื้อ|2|Melioidosis|Y|
2.3.1 ติดเชื้อ|2|Meningococcal disease|Y|
2.3.1 ติดเชื้อ|2|Pneumocystosis in HIV|Y|
2.3.1 ติดเชื้อ|2|STI (syphilis, gonorrhea, chlamydia, chancroid, trichomonas, HPV)|Y|syphilis, chancroid, urethritis
2.3.1 ติดเชื้อ|2|Tuberculosis|Y|
2.3.1 ติดเชื้อ|2|Typhoid / paratyphoid|P|มีแค่ Salmonella complication ข้อเดียว
2.3.1 ติดเชื้อ|2|Varicella zoster|Y|
2.3.1 ติดเชื้อ|2|Viral exanthemata (measles, rubella, HFMD …)|Y|measles, herpangina
2.3.1 ติดเชื้อ|3|Rabies|Y|
2.3.1 ติดเชื้อ|3|Poliomyelitis|N|
2.3.1 ติดเชื้อ|3|Chronic viral hepatitis|Y|
2.3.1 ติดเชื้อ|3|CMV disease|N|
2.3.1 ติดเชื้อ|3|Emerging infection (COVID-19)|Y|
2.3.1 ติดเชื้อ|3|OI (isospora, cryptosporidium …)|Y|
2.3.1 ติดเชื้อ|3|Systemic mycoses (crypto, talaromyces, candida …)|Y|
2.3.1 ติดเชื้อ|3|Tissue parasites (angiostrongylus, gnathostoma, toxoplasma …)|P|มีแค่ eosinophilic meningitis จากหอย
2.3.1 ติดเชื้อ|3|Zoonosis (brucellosis, anthrax …)|N|
2.3.2 มะเร็ง|3|มะเร็งตามอวัยวะ (ปอด เต้านม ลำไส้ อัณฑะ เม็ดเลือด …)|P|มีปอด เต้านม CRC อัณฑะ เม็ดเลือด แต่ไม่มีตับ ตับอ่อน ไทรอยด์ ไต ต่อมลูกหมาก โพรงจมูก
2.3.2 มะเร็ง|2|Benign skin neoplasm|N|
2.3.2 มะเร็ง|3|Malignant skin neoplasm|N|
2.3.3 เลือด|2|Acquired coagulation disorder (vit K, warfarin, heparin)|Y|แปลผล coagulation
2.3.3 เลือด|2|Agranulocytosis, febrile neutropenia|Y|
2.3.3 เลือด|2|G6PD deficiency|Y|
2.3.3 เลือด|2|Immune hemolytic anemia|Y|AIHA
2.3.3 เลือด|2|Immune thrombocytopenia|Y|immune cytopenia
2.3.3 เลือด|2|Lymphadenitis|N|
2.3.3 เลือด|2|Nutritional anemia (iron, folate, B12)|Y|
2.3.3 เลือด|2|Thalassemia, hemoglobinopathy|Y|
2.3.3 เลือด|3|Aplastic anemia|Y|pancytopenia
2.3.3 เลือด|3|Platelet disorders|P|ET, pseudothrombocytopenia
2.3.3 เลือด|3|Hereditary RBC membrane defect|Y|
2.3.3 เลือด|3|Hemophilia, vWD|Y|
2.3.3 เลือด|3|Immune deficiency (asplenia, post-chemo)|P|วัคซีน asplenia, febrile neutropenia
2.3.3 เลือด|3|Non-immune hemolysis (PNH, MAHA)|Y|
2.3.4 ต่อมไร้ท่อ|2|Diabetes mellitus|Y|
2.3.4 ต่อมไร้ท่อ|2|Fluid, electrolyte, acid-base|Y|
2.3.4 ต่อมไร้ท่อ|2|Goiter|P|มีแต่ thyroid nodule
2.3.4 ต่อมไร้ท่อ|2|Hypothyroidism|Y|
2.3.4 ต่อมไร้ท่อ|2|Iodine deficiency|N|
2.3.4 ต่อมไร้ท่อ|2|Metabolic syndrome|Y|
2.3.4 ต่อมไร้ท่อ|2|Obesity|P|อยู่ในแก่น lifestyle
2.3.4 ต่อมไร้ท่อ|2|Protein-energy malnutrition|N|
2.3.4 ต่อมไร้ท่อ|2|Thyrotoxicosis|Y|
2.3.4 ต่อมไร้ท่อ|2|Vitamin deficiency (A B C D E K)|P|B1 (Wernicke), B12, C, K แต่ไม่มี A, D
2.3.4 ต่อมไร้ท่อ|3|Cushing syndrome|Y|
2.3.4 ต่อมไร้ท่อ|3|Thyroiditis|Y|
2.3.4 ต่อมไร้ท่อ|3|Thyroid storm|Y|
2.3.4 ต่อมไร้ท่อ|3|Addison, pituitary, DI, parathyroid, hypogonadism|Y|
2.3.4 ต่อมไร้ท่อ|3|SIADH|Y|
2.3.4 ต่อมไร้ท่อ|3|Vitamin toxicity|N|
2.3.5 จิตเวช|2|Alcohol / substance disorders|P|alcohol withdrawal, opioid overdose
2.3.5 จิตเวช|2|Depression, panic, anxiety, adjustment|X|
2.3.5 จิตเวช|3|Neurocognitive disorder (dementia)|Y|Alzheimer, delirium
2.3.6 ประสาท|2|Encephalitis, myelitis|P|HSV encephalitis ครบ แต่ไม่มี myelitis
2.3.6 ประสาท|2|Bell palsy|Y|
2.3.6 ประสาท|2|ICH, SAH|Y|
2.3.6 ประสาท|2|Migraine|Y|
2.3.6 ประสาท|2|Meningitis|Y|
2.3.6 ประสาท|2|Metabolic encephalopathy (hepatic, Wernicke)|Y|
2.3.6 ประสาท|2|Periodic paralysis|Y|
2.3.6 ประสาท|2|Tension headache|Y|
2.3.6 ประสาท|2|Seizure, epilepsy|Y|
2.3.6 ประสาท|3|Alzheimer|Y|
2.3.6 ประสาท|3|ALS|N|
2.3.6 ประสาท|3|Guillain-Barré|Y|
2.3.6 ประสาท|3|Hydrocephalus|Y|NPH
2.3.6 ประสาท|3|Intracranial abscess|N|
2.3.6 ประสาท|3|Myasthenia gravis|Y|
2.3.6 ประสาท|3|Parkinsonism|Y|
2.3.6 ประสาท|3|Polyneuropathy|Y|
2.3.6 ประสาท|3|Nerve entrapment|Y|
2.3.6 ประสาท|3|Trigeminal neuralgia|N|
2.3.9 หัวใจหลอดเลือด|2|Arrhythmias (AF, SVT, VT, AV block …)|Y|
2.3.9 หัวใจหลอดเลือด|2|Deep vein thrombosis|P|อยู่ในแก่น PE เท่านั้น
2.3.9 หัวใจหลอดเลือด|2|Dyslipidemia|Y|
2.3.9 หัวใจหลอดเลือด|2|Hypertension|Y|
2.3.9 หัวใจหลอดเลือด|2|Heart failure|Y|
2.3.9 หัวใจหลอดเลือด|2|Ischemic heart disease|Y|
2.3.9 หัวใจหลอดเลือด|3|Acute rheumatic fever|Y|
2.3.9 หัวใจหลอดเลือด|3|Aortic aneurysm, dissection|P|ข้อเดียว (ยาที่ห้ามให้เดี่ยว)
2.3.9 หัวใจหลอดเลือด|3|Cerebrovascular disease|Y|
2.3.9 หัวใจหลอดเลือด|3|Peripheral vein disease (thrombophlebitis, varicose)|N|
2.3.9 หัวใจหลอดเลือด|3|Infective endocarditis|Y|
2.3.9 หัวใจหลอดเลือด|3|Pericarditis, myocarditis|Y|
2.3.9 หัวใจหลอดเลือด|3|Peripheral arterial occlusive disease|P|เทียบ vascular claudication ใน lumbar stenosis
2.3.9 หัวใจหลอดเลือด|3|Valvular heart disease|Y|
2.3.10 หายใจ|2|Asthma|Y|
2.3.10 หายใจ|2|Atelectasis|N|
2.3.10 หายใจ|2|COPD|Y|
2.3.10 หายใจ|2|Epiglottitis|N|
2.3.10 หายใจ|2|LRTI (pneumonia, lung abscess, bronchiectasis)|Y|
2.3.10 หายใจ|2|Pneumothorax|Y|
2.3.10 หายใจ|2|Pleural effusion|Y|
2.3.10 หายใจ|2|Vasomotor / allergic rhinitis|N|
2.3.10 หายใจ|2|URTI|Y|common cold, pharyngitis
2.3.10 หายใจ|3|ARDS|Y|
2.3.10 หายใจ|3|Empyema thoracis|Y|complicated parapneumonic
2.3.10 หายใจ|3|Occupational lung disease|Y|
2.3.10 หายใจ|3|Obstructive sleep apnea|N|
2.3.10 หายใจ|3|Nasal polyp, deep neck infection, tracheostomy|X|
2.3.11 ทางเดินอาหาร|2|Acute pancreatitis|Y|
2.3.11 ทางเดินอาหาร|2|Alcoholic liver disease|Y|
2.3.11 ทางเดินอาหาร|2|Cirrhosis|Y|
2.3.11 ทางเดินอาหาร|2|GERD, esophagitis|Y|
2.3.11 ทางเดินอาหาร|2|Functional GI (IBS, dyspepsia, constipation)|Y|
2.3.11 ทางเดินอาหาร|2|Liver abscess|Y|
2.3.11 ทางเดินอาหาร|2|Oral ulcer (aphthous, thrush)|P|aphthous ใน Behçet
2.3.11 ทางเดินอาหาร|2|Peptic ulcer, gastritis|Y|NSAID ulcer, H. pylori
2.3.11 ทางเดินอาหาร|3|Chronic diarrhea|Y|
2.3.11 ทางเดินอาหาร|3|Gallstone, cholecystitis, cholangitis|Y|
2.3.11 ทางเดินอาหาร|3|GI hemorrhage|Y|
2.3.11 ทางเดินอาหาร|3|Hepatic failure|P|paracetamol overdose
2.3.11 ทางเดินอาหาร|3|Diverticular disease|Y|
2.3.11 ทางเดินอาหาร|3|Peritonitis|Y|SBP
2.3.11 ทางเดินอาหาร|3|Appendicitis, obstruction, hernia, anal/perianal|X|
2.3.12 ผิวหนัง|2|Acne|Y|
2.3.12 ผิวหนัง|2|Skin abscess|N|
2.3.12 ผิวหนัง|2|Cellulitis|Y|erysipelas
2.3.12 ผิวหนัง|2|Dermatitis, eczema|Y|
2.3.12 ผิวหนัง|2|Dyshidrosis, miliaria|Y|
2.3.12 ผิวหนัง|2|Impetigo|Y|
2.3.12 ผิวหนัง|2|Ectoparasites (scabies, lice)|Y|
2.3.12 ผิวหนัง|2|Superficial mycoses|Y|
2.3.12 ผิวหนัง|2|Urticaria|Y|
2.3.12 ผิวหนัง|2|Wart|Y|
2.3.12 ผิวหนัง|2|Skin ulcer|N|
2.3.12 ผิวหนัง|2|Burn, corn, cyst, scar|X|
2.3.12 ผิวหนัง|3|Alopecia areata|N|
2.3.12 ผิวหนัง|3|Bullous dermatoses|Y|
2.3.12 ผิวหนัง|3|Cutaneous larva migrans|N|
2.3.12 ผิวหนัง|3|Cutaneous lupus|Y|
2.3.12 ผิวหนัง|3|Erythema multiforme, erythema nodosum|P|มี EN ไม่มี EM
2.3.12 ผิวหนัง|3|Gas gangrene|N|
2.3.12 ผิวหนัง|3|Leprosy|N|
2.3.12 ผิวหนัง|3|Melasma|N|
2.3.12 ผิวหนัง|3|Papulosquamous (psoriasis, PR, LP)|Y|
2.3.12 ผิวหนัง|3|SSSS|N|
2.3.12 ผิวหนัง|3|Scleroderma|Y|
2.3.12 ผิวหนัง|3|Vitiligo|N|
2.3.12 ผิวหนัง|3|Hemangioma, keloid|X|
2.3.13 กระดูกข้อ|2|Costochondritis|N|
2.3.13 กระดูกข้อ|2|Crystal arthropathy|Y|
2.3.13 กระดูกข้อ|2|Degenerative spine|P|lumbar spinal stenosis
2.3.13 กระดูกข้อ|2|Intervertebral disc disorder|N|
2.3.13 กระดูกข้อ|2|Osteoarthritis|Y|
2.3.13 กระดูกข้อ|2|Osteoporosis|N|
2.3.13 กระดูกข้อ|2|Soft-tissue rheumatism|Y|
2.3.13 กระดูกข้อ|3|HSP|Y|
2.3.13 กระดูกข้อ|3|Fibromyalgia|Y|
2.3.13 กระดูกข้อ|3|Infective arthritis|Y|
2.3.13 กระดูกข้อ|3|Myopathy|Y|statin myopathy
2.3.13 กระดูกข้อ|3|Osteonecrosis|Y|AVN จาก steroid
2.3.13 กระดูกข้อ|3|Osteomyelitis|N|
2.3.13 กระดูกข้อ|3|Polymyositis, dermatomyositis|Y|
2.3.13 กระดูกข้อ|3|Pyomyositis|N|
2.3.13 กระดูกข้อ|3|Rheumatoid arthritis|Y|
2.3.13 กระดูกข้อ|3|Spondyloarthropathy|Y|
2.3.13 กระดูกข้อ|3|SLE|Y|
2.3.13 กระดูกข้อ|3|Vasculitis|Y|
2.3.13 กระดูกข้อ|3|Spine curvature, fracture, juvenile arthritis, spondylolisthesis|X|
2.3.14 ไตและทางเดินปัสสาวะ|2|Acute glomerulonephritis|Y|
2.3.14 ไตและทางเดินปัสสาวะ|2|AKI, CKD|Y|
2.3.14 ไตและทางเดินปัสสาวะ|2|Cystitis, urethritis|Y|
2.3.14 ไตและทางเดินปัสสาวะ|2|BPH|P|obstructive AKI จาก BPH
2.3.14 ไตและทางเดินปัสสาวะ|2|Nephrotic syndrome|Y|
2.3.14 ไตและทางเดินปัสสาวะ|2|Pyelonephritis|Y|
2.3.14 ไตและทางเดินปัสสาวะ|3|Chronic glomerulonephritis|Y|IgA, glomerular disease
2.3.14 ไตและทางเดินปัสสาวะ|3|Erectile dysfunction|N|
2.3.14 ไตและทางเดินปัสสาวะ|3|Hypogonadism|Y|
2.3.14 ไตและทางเดินปัสสาวะ|3|Interstitial nephritis|Y|
2.3.14 ไตและทางเดินปัสสาวะ|3|Obstructive uropathy|Y|
2.3.14 ไตและทางเดินปัสสาวะ|3|Renal tubular acidosis|N|มีแค่ Fanconi
2.3.14 ไตและทางเดินปัสสาวะ|3|Renal artery stenosis|P|ข้อเดียว (ห้าม ACEI)
2.3.14 ไตและทางเดินปัสสาวะ|3|Urolithiasis|Y|
2.3.14 ไตและทางเดินปัสสาวะ|2|สูติ-นรีเวช, อัณฑะ (orchitis, torsion, hydrocele)|X|
2.2 ฉุกเฉิน|1|Acute coronary syndrome|Y|
2.2 ฉุกเฉิน|1|Cardiac tamponade|Y|
2.2 ฉุกเฉิน|1|Cardiopulmonary arrest|P|มีแค่ pulseless VT → defib
2.2 ฉุกเฉิน|1|Malignant hypertension|P|ข้อเดียว (HT emergency + pulmonary edema)
2.2 ฉุกเฉิน|1|Pulmonary edema|Y|
2.2 ฉุกเฉิน|1|Aortic dissection|P|ข้อเดียว
2.2 ฉุกเฉิน|1|Shock (hypovolemic, anaphylactic, septic, cardiogenic)|Y|
2.2 ฉุกเฉิน|1|Acute respiratory failure|Y|
2.2 ฉุกเฉิน|1|Airway obstruction|P|BVM ข้อเดียว
2.2 ฉุกเฉิน|1|Asthma / COPD exacerbation|Y|
2.2 ฉุกเฉิน|1|Acute pulmonary embolism|Y|
2.2 ฉุกเฉิน|1|SVC obstruction|Y|
2.2 ฉุกเฉิน|1|Tension pneumothorax|Y|
2.2 ฉุกเฉิน|1|Hyperkalemia, severe hypokalemia|Y|
2.2 ฉุกเฉิน|1|Hyperglycemic crisis|P|DKA ครบ ไม่มี HHS
2.2 ฉุกเฉิน|1|Hypoglycemia|Y|
2.2 ฉุกเฉิน|1|Acute hemolytic crisis|P|G6PD
2.2 ฉุกเฉิน|1|Acute limb ischemia|N|
2.2 ฉุกเฉิน|1|DIC|P|อยู่ในแก่น MAHA
2.2 ฉุกเฉิน|1|Incompatible blood transfusion|Y|
2.2 ฉุกเฉิน|1|Hyperventilation syndrome|Y|
2.2 ฉุกเฉิน|1|Anuria / oliguria|Y|
2.2 ฉุกเฉิน|1|Acute urinary retention|P|BPH anuria
2.2 ฉุกเฉิน|1|Acute increased ICP|P|ข้อเดียว (CT ก่อน LP)
2.2 ฉุกเฉิน|1|Coma|Y|GCS
2.2 ฉุกเฉิน|1|Status epilepticus|Y|
2.2 ฉุกเฉิน|1|Spinal cord compression|N|
2.2 ฉุกเฉิน|1|Stroke|Y|
2.2 ฉุกเฉิน|1|Syncope|Y|
2.2 ฉุกเฉิน|1|Acute abdomen|P|pancreatitis, appendicitis
2.2 ฉุกเฉิน|1|Massive bleeding (UGIB …)|Y|
2.2 ฉุกเฉิน|1|Bites and stings|Y|งูกัด, ผึ้งต่อย
2.2 ฉุกเฉิน|1|Acute poisoning|Y|
2.2 ฉุกเฉิน|1|Sepsis|Y|
2.2 ฉุกเฉิน|1|SJS / TEN|Y|
2.2 ฉุกเฉิน|1|Necrotizing fasciitis|N|
2.2 ฉุกเฉิน|1|จิตเวช ตา สูติ ทารก บาดเจ็บ (2.2.8, 23–27, 30–34, 41–42, 47)|X|
"""
rows = [dict(zip(('sec', 'grp', 'name', 'st', 'note'), l.split('|'))) for l in R.strip().split('\n')]
ROOT = os.path.dirname(os.path.abspath(__file__))
json.dump(rows, open(f'{ROOT}/nl_coverage.json', 'w'), ensure_ascii=False, indent=1)
import collections
c = collections.Counter(r['st'] for r in rows); print(c)
for s in ('2.2',):
    print(collections.Counter(r['st'] for r in rows if r['sec'].startswith(s)))
print(collections.Counter(r['st'] for r in rows if not r['sec'].startswith('2.2')))
print(collections.Counter((r['grp'],r['st']) for r in rows if not r['sec'].startswith('2.2')))
