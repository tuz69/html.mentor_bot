import telebot
import config
from random import choice

from telebot import types

bot = telebot.TeleBot(config.TOKEN)



################# sticker #####################
stickers = ["CAACAgIAAxkBAAECnF1g-AHfri9acrFiG28goqcP5dtwPAACNwEAAvu2vi4nzE8gMkIeFyAE", "CAACAgIAAxkBAAECnGBg-AOMX1RSzuSzB-tew7XpGIB74AACPgEAAvu2vi70729eNnlS3SAE", "CAACAgIAAxkBAAECnGFg-AOMiGU-1M0UWArk9XIrq8frtQACQwEAAvu2vi6h9BKN7yOEZSAE"]
###############################################

##################### Удаление уведомления о входе/выходе из беседы ######################################
@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
   bot.delete_message(message.chat.id, message.message_id) 

@bot.message_handler(content_types=['left_chat_member'])
def greeting(message):
   bot.delete_message(message.chat.id, message.message_id) 

##########################################################################################################

#################### Помощь и Правила *Правила под вопросом* #######################################
@bot.message_handler(commands=["help"])
def help(message):
   bot.send_message(message.chat.id, f"""
   Привет, человек)
   Я бот создан для этого чата)
   Мой создатель Eduard  👽
   Если я буду себя как-то странно вести - пишите ему (Описывайте поведение и приложите скрины)
   
    А по поводу всех команд и их значения вы можете узнать по команде /commands 
    """)
#############################################################
#В имя надо будет запихнуть ссылку на мой акк
##########################################     GOOGLE :-)      ##########################################

@bot.message_handler(commands = ["google"])
def google(message):
   bot.send_sticker(message.chat.id, choice(stickers))
#########################################################################################################

##########################################     Commands :)      ##########################################

@bot.message_handler(commands = ["commands"])
def commands(message):
    bot.send_message(message.chat.id, f"""
    Доступны такие команды:
    /help - Помощь и основная инфа
    /hb - День рождение (Команда доступна ток для developer и designer
    /start - Что-то будет хз ещё
    /useful - Ссылка на что-то полезное например на гугл диск Дани
    СПАМ ЛЮБЫМИ КОМАНДАМИ ЗАПРЕЩЁН!  
     """)
#########################################################################################################


bot.polling(none_stop = True)
