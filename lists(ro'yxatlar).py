# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:14:45 2026

@author: HP
"""

meva=['olma','nok','behi','uzum']
#print(meva)

narhlar=[1000,2000,10900,22000]
#print(narhlar)

son=['bir', 'ikki', 4,5]
ismlar=[]
#print(ismlar)
#print(meva[-1].upper())
#print(meva[-2].title())

#print(meva[-1])
#manfiy ishora bilan chaqrilsa eng oxrigi elementdan keladi

#print(narhlar[1]+narhlar[2])
#elementlarni chaqrgan holda qiymat chiqarsa buladi

meva[0]='anor'#list ruyxatini uzgartirish
#print([meva])

meva.append('tarvuz')
#print(meva)

meva.insert(0,'sabzi')#indeks metodi yordamida listning ixtiyoriy qismiga element qushish munkin
#print(meva)
#meva.insert(8,'banan')
#print(meva)

cars=[]
cars.append('lacetti')
cars.append('nexia')
cars.append('malibu')
cars.append('tracker')
cars.append('cobalt')
#print(cars)

del cars[0]#1-usul del operatori yordamida element ochiriladi
#print(cars)
cars.insert(0,'lacetti')#insert operatori orqali element qoshiladi

#agar element indeks raqamini bilmasak remove operatoridan foydalanmiz
#cars.remove('malibu')
#print(cars)

cars.insert(0,'lacetti')
#print(cars)

hayvonlar=['mushuk', 'sichqon', 'ari', 'mushuk']
#hayvonlar.remove('mushuk')
#print(hayvonlar)

bozorlik=['yog', 'un', 'piyoz', 'shakar', 'gosht']
mahsulot=bozorlik.pop(1)#ruyxat ichidan element sugurub olish metodi
#print(mahsulot)
#print(bozorlik)

#print('men' ,mahsulot, 'sotib oldim')
#print('sotib olinmagan mahsulot', bozorlik)

mahsulot2=bozorlik.pop()
#print(mahsulot2)
#print(bozorlik)
