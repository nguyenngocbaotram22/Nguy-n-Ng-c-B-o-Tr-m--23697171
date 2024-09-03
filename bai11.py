# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:04:36 2024

@author: ADMIN
"""

a=str(input("hay nhap 1 ki tu:"))
if len(a)>1 or not a.isalpha():
    print("nhap mot ki tu khac so")
else:
    print(a.upper())