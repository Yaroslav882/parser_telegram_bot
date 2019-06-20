import telebot
import parser

TOKEN = '869498520:AAE-JUP9a4AJXW9AWzD_M2WLZOZKc3rKaDE'
simple_bot = telebot.TeleBot(TOKEN)

@simple_bot.message_handler(commands=['start', 'go'])
def srat_bot(message):
    simple_bot.send_message(message.chat.id, 'Добро пожаловать')
    simple_bot.send_message(message.chat.id, 'Я бот который парсит с Habr.com')

@simple_bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == 'привет':
        simple_bot.send_message(chat_id, 'И тебе салют, я парсерный бот.')
    elif text == 'что делаешь?':
        simple_bot.send_message(chat_id, 'Пытаюсь выйти в интернет!')
    else:
        simple_bot.send_message(chat_id, 'Я что то не понял твой текст.')

simple_bot.polling()
