#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ผูกข้อสอบคาบ 13 Ischemic heart disease ในคลัง Ward Drill (33 ข้อ) เข้าบทเรียน cardio คาบ 13 (เดิมใช้เลข 24/9)
รันหลัง build_ihd.py ทุกครั้ง"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from link_bank import link

MAP = {
    "cardio-ihd-01": ["C-MCQ-14", "C-OLD-35"],                                   # plaque rupture
    "cardio-ihd-02": ["C-OLD-40", "C-OLD-38", "C-OLD-48"],                       # stable angina / first test
    "cardio-ihd-03": ["C-OLD-49", "C-MCQ-17", "C-OLD-41"],                       # CCS Rx · INOCA
    "cardio-ihd-04": ["C-OLD-36"],                                               # ACS chest pain pattern
    "cardio-ihd-05": ["C-OLD-42", "C-OLD-43", "C-OLD-53", "C-OLD-54", "C-OLD-51", "C-MCQ-15"],  # STEMI ECG
    "cardio-ihd-06": ["C-MCQ-11", "C-OLD-33", "C-OLD-52", "C-OLD-34"],           # reperfusion
    "cardio-ihd-07": ["C-MCQ-12", "C-OLD-50"],                                   # fibrinolysis
    "cardio-ihd-08": ["C-MCQ-13", "C-OLD-37", "C-OLD-39"],                       # NSTE-ACS / UA
    "cardio-ihd-11": ["C-MCQ-16", "C-OLD-45", "C-OLD-46", "C-OLD-47", "C-OLD-55", "C-OLD-44"],  # secondary prevention
}
n = link("cardio", "13", MAP, meq=["C-MEQ-01"], osce=["C-OSCE-01"])
print("ผูกเพิ่ม %d ข้อ" % n)
