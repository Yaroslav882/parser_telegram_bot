import telebot
import parser

TOKEN = '869498520:AAE-JUP9a4AJXW9AWzD_M2WLZOZKc3rKaDE'
simple_bot = telebot.TeleBot(TOKEN)

# @simple_bot.message_handler(commands=['start', 'go'])
# def srat_bot(message):
#     simple_bot.send_message(message.chat.id, 'Добро пожаловать')
#     simple_bot.send_message(message.chat.id, 'Я бот который парсит с Habr.com')
#
# @simple_bot.message_handler(content_types=['text'])
# def text_handler(message):
#     text = message.text.lower()
#     chat_id = message.chat.id
#     if text == 'привет':
#         simple_bot.send_message(chat_id, 'И тебе салют, я парсерный бот.')
#     elif text == 'что делаешь?':
#         simple_bot.send_message(chat_id, 'Пытаюсь выйти в интернет!')
#     else:
#         simple_bot.send_message(chat_id, 'Я что то не понял твой текст.')
#
# @simple_bot.message_handler(content_types=['photo'])
# def photo_handler(arg):
#     chat_id = message.chat.id
#     simple_bot.send_message(chat_id, 'Я не эксперт, но зачет')

@simple_bot.message_handler(commands=['start', 'go'])
def start_bot(message):
    chat_id = message.chat.id
    text = message.text
    question = simple_bot.send_message(chat_id, 'Сколько тебе лет?')
    simple_bot.register_next_step_handler(question, askAge)

def askAge(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        question = simple_bot.send_message(chat_id, 'Надо указать число! Еще раз пожалуйста')
        simple_bot.register_next_step_handler(question, askAge)
        return
    question = simple_bot.send_message(chat_id, 'Ого...тебе ' + text + ' лет?')

simple_bot.polling()
