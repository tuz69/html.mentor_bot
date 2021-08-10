import telebot
import sqlite3
import config

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


bot.polling(none_stop=True)
