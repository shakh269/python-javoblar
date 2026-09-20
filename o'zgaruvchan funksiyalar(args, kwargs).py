# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:11:59 2026

@author: HP
"""
# def summa (*sonlar):
#     # """oraliqdagi sonlar yigindisini hisoblayman"""
#     # yigindi=0
    # for son in sonlar:
    #     yigindi+=son
    # return yigindi
# print(summa(1,2,5,7))
# print(summa(3,5,8,9))



# def summa (*sonlar):
#     return sum(sonlar)
# print(summa(1,2,5,7))
# print(summa(3,5,8,9))

# uzgarmas qiymatli
# def summa (x,y,*sonlar):
#     return x+y+sum(sonlar)
# print(summa(1,2,5,7))
# print(summa(3,5,8,9))
# print(summa(2))error


def avto_info(kompaniya, model, **malumotlar):
    """avto haqida lugat tayyorlayman"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
avto1=avto_info("GM","MALIBU",rang='qora', yili=2026, narh=23000)
print(avto1)






















































































