# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:57:53 2026

@author: HP
"""

#ism=input(" ismingizni kiriting?:")
#yosh=input(f"{ism.title()}, yoshingiz nechida?:")
#print(f"{ism} ning yoshi {yosh} da")
#yosh=int(yosh)
#height=input("Boyingiz nechida")
#height=float(height)
#print(height)

#son=1
#while son<=6:
 #   print(son , end=' ')
  #  son+=2
#print('dastur tugadi.')

#savol="Istalgan son kiriting:"
#savol+="(Dasturni to'xtashish uchun 'exit' deb yozing)"
#qiymat=" "
#while qiymat !='exit':
 #   qiymat=input(savol)
  #  if qiymat !='exit':
   #     print(float(qiymat)**2)

#avol="istalgan son kiriting:"
#avol+="dasturni uzish uchun 'exit' deb yozing"
#shora=True
#hile ishora:
 #  qiymat=input(savol)
  # if qiymat=='exit':
   #    ishora=False
   #else:
    #   print(float(qiymat)**2)

#BREAK dan foydalanish
#avol="istalgan son kiriting:"
#avol+="dasturni uzish uchun 'exit' deb yozing"

#hile True:
   #qiymat=input(savol)
   #if qiymat=='exit':
   #    break
  # else:
   #    print(float(qiymat)**2)


#onlar=list(range(1,11))
#or son in sonlar:
 #  if son==5:
  #     break
   #print(f" {son} ning 2-darajasi ({son**2}) ga teng")

#Continue bilan ishlash
#son=1
# while son>0:
#     son+=1
#     if son%2==0:
#         continue
#     else:
#         print(son)


# #Amaliy mashg'ulotlar
# # Foydalanuvchidan yaxshi ko'rgan 
# kitoblarini kiritishni so'rang. Foydalanuvchi 
# stop so'zini yozishi bilan dasturni to'xtating

# savol=('kitobingizni nomini kiriting:')
# while book!='stop':
#     book=input(savol)    
#     if book=='stop':
#         break
# print(f"siz kiritgan kitob:{book}")




# savol='yaxshi korgan kitobingizni kiriting'
# while True:
#     kitob=input(savol)
#     if kitob.lower()=='stop':
#         break
#     print(f"siz kiritgan kitob:{kitob}")





# Muzeyga chipta narhi foydalanuvchining 
# yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 
# 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
# Shunday while tsikl yozingki, dastur foydalanuvchi yoshini 
# so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit 
# deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).


savol=('yoshingizni kiriting:')
while True:
  yosh= (input(savol))
  if yosh==('exit' or 'quit'):
      break
  else:
    if int(yosh)<7:
        print('chipta narxi:2000')
    elif 7<int(yosh)<18:
        print('chipta narxi:3000')
    elif 18<int(yosh)<65:
        print('chipta narxi:10000')
    elif int(yosh)>65:
        print('sizga bepul')
    
       
















































