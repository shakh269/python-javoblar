# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 12:26:51 2026

@author: HP
"""

class Fan():
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]
    def add_students(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
    def see_methods(klass):
        return[method for method in dir(klass) if method.startswith('__')]
matem=Fan("oliy matematika")




#vorislik va polimarfizim
class Shaxs:
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        return yil - self.tyil
    
class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
 #super klass bu Shaxs shuni xususiyatlarini oldik 
   
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
class Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
    
inson=Shaxs("Shoxruh", "Tillayev", "AV2334567", 1990)

talaba1_manzil=Manzil(1,"tillakori", "sarbon", "fargona")
talaba1=Talaba("Bobur","Mahkamov", "AD12345", 1998, 6767585890, talaba1_manzil)



























