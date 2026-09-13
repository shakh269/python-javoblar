# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 15:56:34 2026

@author: HP
"""

# def t_i_y (ism,familiya):
#     toliq_ism=f"{ism}, {familiya}"
#     return toliq_ism
# talaba=t_i_y('doston', 'ubaydullayev')
# #rint(talaba)
# talaba1=t_i_y('avaz', 'olimovq')
# print(f"darsga kelmagan talabalar: {talaba} va {talaba1}")


# def t_i_y (ism, familiya, otasi_ismi=''):
#     if otasi_ismi:
#         toliq_ism=f"{ism} {otasi_ismi} {familiya}"
#     else:
#         toliq_ism=f"{ism} {familiya}"
#     return toliq_ism
# talaba1=t_i_y('olim','mikeov')
# talaba2=t_i_y('lazi', 'karimovich','rozziqov')
# print(f"darsga kelmaganlar {talaba1} va {talaba2}")

def avto_info (kompaniya, model, rangi, karobka, yili):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rang':rangi,
          'karobka':karobka,
          'yili':yili
          }
    return(avto)
# avto1=avto_info('gm','malibu','qora','mexanika',2021)
# avto2=avto_info('gm','gentra','oq','avtomat',2020)
# avtolar=[avto1, avto2]
# # print(avtolar)
# for avto in avtolar:
#     if avto['rang']=='qora':
#         print(f"{avto['model']} dagi mashina mavjud")
#     else:
#         print('qora rangli mashinalar mavjud emas')


# def oraliq (min, max):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=4
#     return sonlar
# print(oraliq(35,78))
# sonlar=oraliq(23,43)
# print(sonlar)

# qadam=int(input("qadamni kiriting:")
# def oraliq (min, max, qadam=3):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min) 
#         min+=qadam
#     return sonlar
# print(oraliq(1,12,2))
# sonlar=oraliq(23,43)
# print(sonlar)

# def avto_info (kompaniya, model, rangi, karobka, yili):
#     avto={'company':kompaniya,
#           'model':model,
#           'color':rangi,
#           'engine':karobka,
#           'year':yili     }
#     return(avto)


# avtolar=[]
# while True:
#     print("\nQuyidagilarga ma;lumot kiriting?")
#     company=input('kompaniya nomi'),
#     model=input('modeli'),
#     color=input('rangini kiriting'),
#     engine=input('karobkani kiriting'),
#     year=input('chiqarilgan yili')
#        avtolar.append(avto_info(company, model,color, engine, year))
        # jvob=input('yana avto kiritaszmi? (yes/no)')
        #            if javob =='no':
        #                break
   






































































