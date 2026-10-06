# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 07:30:07 2026

@author: HP
"""
# import math
# uzunlik=lambda pi, r:2*pi*r
# print(uzunlik(math.pi,10))

# kvadrat=lambda x,y: x**y
# print(kvadrat(4,3))

# def daraja(n):
#     return lambda x:x**n
# kvadrat=daraja(2)
# kub=daraja(3)
# print(kvadrat(78))
# print(kub(6))

# from math import sqrt
# sonlar=list(range(12))
# ildizlar=list(map(sqrt,sonlar))
# print(ildizlar)

# def daraja2(x):
#     return x*x
# print(list(map(daraja2,sonlar)))

# kvadrat=list(map(lambda x:x*x, sonlar))
# print(kvadrat)

# a=[11,12,13]
# b=[14,15,16]
# yigindi=list(map(lambda x,y:x/y,a,b))
# print(yigindi, iterable))

# import random as r 
# sonlar=r.sample(range(50),10)
# print(sonlar)
# def juftmi (x):
#     return x%2==0
# juftsonlar=list(filter(lambda son: son%2==0,sonlar))
# print(juftsonlar)


mevalar = ['olma','anor','bodring','shaftoli',"o'rik","tarvuz","qovun","banan"]
# mevalar_b = list(filter(lambda meva:meva.startswith('o'),mevalar))
# print(mevalar_b)
meva2=list(filter(lambda meva:len(meva)<=5, mevalar))
print(meva2)


































