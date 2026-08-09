# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:01:35 2026

@author: HP
"""

talaba_0={
    'ism':'ali',
    'familiya':'valiyev',
    'yosh':22,
    'fakultet':'fizika',
    'kurs':5
    }
#print(talaba_0.items())
#for kalit, qiymat in talaba_0.items():
    #print(f"Kalit:{kalit}")
    #print(f"Qiymat:{qiymat}\n")

telefonlar={'ali':'galaxy 10s',
            'vali':'redmi 7pro',
            'mardon':'samsung a10',
            'hamid':'galaxy 10s',
            'malik':'redmi 7pro'
            }
#for k,q in telefonlar.items():
 #   print(f"{k.title()} ning telefoni {q}")

mahsulotlar={
    'behi':10000,
    'anjir':20000,
    'mango':30000,
    }
#print(mahsulotlar.keys())
#print("Do'kondagi mahsulotlar:")
#for mahsulot in mahsulotlar.keys():
 #   print(mahsulot.title())

bozorlik=('behi','mango','banan','guruch')
#for mahsulot in mahsulotlar:
 #   if mahsulot in bozorlik:
  #      print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#for buyum in bozorlik:
 #   if buyum not in mahsulotlar:
  #      print(f" iltimos, do'koningizga {buyum} ham olib keling")

#print("do'konimizdagi mahsulotlar:")
#for mahsulot in sorted(mahsulotlar):
 #   print(mahsulot.title())

#print(telefonlar.values())
print("foydalanuvchilar quyidagi tellarni ishlatadilar")
#for tel in (telefonlar.values()):
 #   print(tel)
 
 
for tel in set(telefonlar.values()):
    print(tel)




































