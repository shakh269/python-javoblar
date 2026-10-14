# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


"""


# import random
# words=("bosh", "bola", "oila", "maktab", "dars", "kitob", "suv",
#     "yer", "osmon", "quyosh", "oy", "shakar", "non", "choy", "pul", "do'st", "dushman",
#     "ona", "ota", "aka", "uka", "opa", "singil", "farzand", "ayol", "erkak", "kishi",
#     "davlat", "vatan", "xalq", "dunyo", "olam", "tabiat", "guruh", "tizim", "ishchi",
#     "rahbar", "shifokor", "o'qituvchi", "talaba", "yoshlar", "kuch", "ilm", "baxt")

# # soz topish oyini dasturi 


# tas_son=random.choice(words)
# def soztop():
#     taxminlar=0
#     while True:
#         taxminlar+=1
#         taxmin=(input("taxminiy harf yoki soz kiriting:")).lower()
#         if taxmin==tas_son :
#             print(f"tabrikleyman, sz sozni topdingiz")
#             break
#         elif taxmin in tas_son:
#             print(f"tabrikleyman, sz sozdagi harfni topdingiz")
#         else:
#             print('soz yoki harf topilmadi, kiritishda davom eting')
#     return taxminlar
# natija=soztop()
# print(f"sz sozni {natija} ta urinishda topdingiz")



# krill==lotin translator#


# # print(to_latin('йил'))
# # print(to_cyrillic('dasturchi'))

# print(to_cyrillic(matn))


from transliterate import to_cyrillic, to_latin
import telebot
TOKEN='8602702576:AAEGVnT4wd6PMwsmyj8gzqytog3YN6RVu0E'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalom u alaykum hayrli kun, Xush kelibsiz"
    javob+="\nMatn kiriting (lotin yoki krill alifbosida):"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    javob= lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # if msg.isascii():
    #     javob=to_cyrillic(msg)
    # else:
    #     javob=to_latin(msg)
    bot.reply_to(message, javob(msg))
    
bot.infinity_polling(timeout=8, long_polling_timeout=4)  
    
    
# matn=input('matn kiriting:')
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))































