import telebot
import config
import sqlite3
import happy
from random import choice

from telebot import types

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def id_add(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS birthday_users(
        id INTEGER,
        birthday TEXT
    )''')
    connect.commit()

    cursor.execute(
        f"SELECT id FROM birthday_users WHERE id = {message.chat.id}")
    data = cursor.fetchone()
    if data is None:
        user_info = [message.chat.id, '[]']
        cursor.execute("INSERT INTO birthday_users VALUES(?, ?);", user_info)
    connect.commit()
    connect.close()


@bot.message_handler(content_types=['text'])
def date_add(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute(
        f"SELECT birthday FROM birthday_users WHERE id = {message.chat.id}")
    user_date = eval(cursor.fetchall()[0][0])
    # print(user_info)
    # print(type(user_info))
    user_date.append((message.text))
    cursor.execute(f"DELETE FROM birthday_users WHERE id = {message.chat.id}")
    user_info = [message.chat.id, str(user_date)]
    cursor.execute("INSERT INTO birthday_users VALUES(?, ?);", user_info)
    connect.commit()
    connect.close()



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
   Привет тут короче будет что-то о 
   developer - 
   designer - 
   Кто-тут такой Герман)
   Даня чёрт, но наш чёрт)
   GG WP
   
    """)
#############################################################

##########################################     GOOGLE :-)      ##########################################

@bot.message_handler(commands = ["google"])
def google(message):
   bot.send_sticker(message.chat.id, choice(stickers))
#########################################################################################################


bot.polling(none_stop = True)
