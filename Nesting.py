# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 18:18:23 2026

@author: HP
"""

car0={
      'model':'lacetti',
      'rang':'oq',
      'yil':2015,
      'narh':13000,
      'km':50000,
      'korobka':'avtomat'
      }


car2={
      'model':'cobalt',
      'rang':'oq',
      'yil':2020,
      'narh':20000,
      'km':660000,
      'korobka':'mexanika'
      }

car3={
      'model':'tracker',
      'rang':'oq',
      'yil':2024,
      'narh':24000,
      'km':89000,
      'korobka':'avtomat'
      }
#car=car0
#print(f"{car['model'].title()}",
 #     f"{car['rang']} rang,"
  #   f"{car['yil']}-yil, {car['narh']} $" )
  
  
cars=[car0,car2,car3]
#for car in cars:
#    print(f"{car['model'].title()}",
#          f"{car['rang']} rang,"
#         f"{car['yil']}-yil, {car['narh']} $" )
    
#print(cars[0]['model'])   

#print(f"{cars[2]['rang'].title()} "
 #     f"{cars[2]['model']}")

onixes=[]
for n in range(10):
    new_car={
        'model':'onix',
        'rangi':'noaniq',
        'yil':2026,
        'narh':15000,
        'km':00,
        }
    (onixes.append(new_car))
   # print(new_car)

#for onix in onixes[:3]:
  #onix['rangi']='qizil'  
#]for onix in onixes:
 #   print(onix)
#for onix in onixes[3:6]:
    #onix['rangi']='qora'
   # onix['km']=15
#for onix in onixes[6:]:
   # onix['narh']=20000
#for onix in onixes:
   # print(onix)
   
   
#for onix in onixes:
    #if onix['rangi']=='qora':
      #  onix['narh']=40000
   # else:
       # onix['narh']=33000
#for onix in onixes:
  #  print(onix)

dasturchilar={
    'ali':['python','C++'],
    'john':['html','css','js'],
    'mike':['php','sql'],
    'jonson':['php', 'css']
    }
#r ism, tillar in dasturchilar.items():
 #  print(f"\n{ism.title()} quyidagi tillarni biladi:")
  # for til in tillar:
   #    print(f'{ til.upper()}', end='')

#lug'at ichiga lug'at joylaymiz

dostlar={
    'ali':{'familiya':'sattorov',
           'yil':1995,
           'malumot':'oliy',
           'tillar':'python',
           },
    'mardon':{'familiya':'olimov',
           'yil':1999,
           'malumot':'orta',
           'tillar':'php'
           }
}


#rint(dostlar)
for ism, info in dostlar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}",
          f"{info['yil']}- yilda tugilgan",
          f"malumoti:{info['malumot']}")

































