# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 12:50:01 2026

@author: HP
"""
import random
# tanson=int(input('1 dan 9 gacha sonlar orasidan son tanlang:'))
# son=random.randint(1,10)
# if tanson==son:
#     print('sz tanlagan son togri')
# else:
#     print('sz tanlagan son notogri')


# def son_top_oyini():
#     tas_son=random.randint(1,10)
#     urinishlar_soni=0
#     topildi=False
#     while not topildi:
#         try:
#             taxmin=int(input('taxminiy son kiriting:'))
#             urinishlar_soni+=1
#             if taxmin<1 or taxmin>10:
#                 print('1 va 10 oraligidagi son kiriting')
#                 continue
#             if taxmin<tas_son:
#                 print('xato, men oylagan son bundan katta')
#             elif taxmin>tas_son:
#                 print(('xato, men oylagan son bundan kichik'))
#             else:
#                 topildi==True
#                 print(f"TABRIKLEYMIZ, sz javobni topdingiz. Togrijavob {tas_son}")
#         except ValueError:
#             print('iltimos faqat butun son kiriting')
# son_top_oyini()





def soni_topish(x=10):
    """Siz bir son o'ylaysiz va uni dastur binar qidiruv orqali topadi"""
    print(f"1 dan {x} gacha son o'ylang, men uni topishga harakat qilaman.")
    quyi = 1
    yuqori = x
    qadam = 0
    
    while quyi <= yuqori:
        qadam += 1
        # Har doim oraliqning o'rtasini taxmin qilamiz (eng samarali yo'l)
        if quyi != yuqori:
            taxmin = (quyi + yuqori) // 2
        else:
            taxmin = quyi
            
        javob = input(f"Siz o'ylagan son {taxmin} mi? \n"
                      f"To'g'ri (T), men o'ylagan son {taxmin} dan katta (+), kichik (-) >> ").lower()
        
        if javob == 't':
            print(f"Yess! Men {qadam} ta qadamda topdim!")
            return qadam
        elif javob == '+':
            quyi = taxmin + 1
        elif javob == '-':
            yuqori = taxmin - 1
            
    return qadam

















































