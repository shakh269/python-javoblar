# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 09:55:13 2026

@author: HP
"""

car_0={'rusumi':'ferrari','rangi':'qizil'}
#print(car_0['rusumi'])
#print(car_0['rangi'])

en_uz={'apple':'olma','apricot':"o'rik",'banana':'banan'}
#print(en_uz['apple'])

meva={'olma':7000, 'tarvuz':8000, 'qovun':10000}
#print(f"olma narhi {meva['olma']}, so'm")
#print(meva['tarvuz'])

talaba_0={'ism.f':'karem benzema', 't_yil':'1992','yosh':'34'}
#print(talaba_0['yosh'])
#print(f"{talaba_0['ism.f'].title()}\
 #     {talaba_0['t_yil']} yilda tug'ilgan\
  #        {talaba_0['yosh']} yoshda")
talaba_0['kurs']=5#kalit so'z qo'shish
talaba_0['fakultet']='fizika'#kalit so'z qo'shish
#print(talaba_0)
talaba_0['yosh']=36#kalit so'zni alishtirish
#print(talaba_0)
talaba_1={}
talaba_1['ism']='malik'
talaba_1['yosh']=24
talaba_1['kurs']=5
#print(talaba_1)
talaba_1['kurs']=6
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} kursda") 
del talaba_1['yosh']
#print(talaba_1)

telefonlar={
    'ali':'i phonex',
    'vali':'galaxy s9',
    'kamol':'redmi8 pro',
    'laziz':'inf 7'
    }
phone=telefonlar.get('hasan','bunday qiymat mavjud emas')
#print(phone)

#Amaliyot mashqlar

ism={'ism_1':'olim', 'ism_2':'jalil'}
taom={'taom_1':'manti', 'taom_2':'osh'}
#print(f"{ism['ism_1'].title()}ning sevimli taomi {taom['taom_1']}")

#Foydalanuvchidan biror so'z kiritishni so'rang
 #va so'zning tarjimasini yuqoridagi lug'atdan 
 #chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, 
 #"Bunda so'z mavjud emas" degan xabarni chiqaring.

sozlar={'story':'hikoya','book':'kitob'}
soz=input('soz kiriting:')
if soz==sozlar['story'] or sozlar['book']:
    print("mutlaqo to'g'ri javob")
else:
    print("kiritilgan soz noto'g'ri")




























