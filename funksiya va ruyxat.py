# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:50:08 2026

@author: HP
"""

# def bahola (ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f"talaba {ism.title()}ning bahosini kiriting:")
#         baholar[ism]=int(baho)
#     return baholar
# talabalar=['mardon','malik','doston','bosid']
# baholar=bahola(talabalar[1:4])
# print(baholar)


# Matnlardan iborat ro'yxat qabul qilib, 
# ro'yxatdagi har bir matnning birinchi harfini katta harfga 
# o'zgatiruvchi funksiya yozing.

def katt (matnlar):
    ruyxat=[]
    while matnlar:
        matn=matnlar.pop()
        ruyxat.append(matn.title())
    return ruyxat
nom=['edik','nedik','bobik']
natija=katt(nom)
print(natija)













































