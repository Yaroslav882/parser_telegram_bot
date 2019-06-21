import telebot
import bs4
import parser
from Task import Task

TOKEN = '869498520:AAE-JUP9a4AJXW9AWzD_M2WLZOZKc3rKaDE'
simple_bot = telebot.TeleBot(TOKEN)
task = Task()


@simple_bot.message_handler(commands=['start', 'go'])
def start_bot(message):
    if not task.isRunning:
        chat_id = message.chat.id
        question = simple_bot.send_message(chat_id, 'От куда будем парсить?')
        simple_bot.register_next_step_handler(question, askSource)
        isRunning = True

def askSource(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[0]:
        task.mySource = 'top'
        question = simple_bot.send_message(chat_id, 'За какой промежуток?')
        simple_bot.register_next_step_handler(question, askAge)
    elif text in task.names[1]:
        task.mySource = 'all'
        question = simple_bot.send_message(chat_id, 'Какой минимальный рейтинг?')
        simple_bot.register_next_step_handler(question, askRating)
    else:
        question = simple_bot.send_message(chat_id, 'Извините, такого раздела нет. Введите раздел корректно.')
        simple_bot.register_next_step_handler(question, askSource)

def askAge(message):
    chat_id = message.chat.id
    text = message.text.lower()
    filters = task.filters[0]
    if text not in filters:
        question = simple_bot.send_message(chat_id, 'Такого временного промежутка нет. Введите порог корректно.')
        simple_bot.register_next_step_handler(question, askAge)
        return
    task.myFilter = task.filters_code_names[0][filters.index(text)]
    question = simple_bot.send_message(chat_id, 'Сколько страниц парсить?')
    simple_bot.register_next_step_handler(question, askAmount)

def askRating(message):
    chat_id = message.chat.id
    text = message.text.lower()
    filters = task.filters[1]
    if text not in filters:
        question = simple_bot.send_message(chat_id, 'Такого порога нет. Введите порог корректно.')
        simple_bot.register_next_step_handler(question, askRating)
        return
    task.myFilter = task.filters_code_names[1][filters.index(text)]
    question = simple_bot.send_message(chat_id, 'Сколько страниц парсить?')
    simple_bot.register_next_step_handler(question, askAmount)

def askAmount(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if not text.isdigit():
        question = simple_bot.send_message(chat_id, 'Количество страниц должно быть числом. Введите корректно.')
        simple_bot.register_next_step_handler(question, askAmount)
        return
    if int(text) < 1 or int(text) > 11:
        question = simple_bot.send_message(chat_id, 'Количество страниц должно быть >0 и <11. Введите корректно.')
        simple_bot.register_next_step_handler(question, askAmount)
        return
    task.isRunning = False
    output = ''
    if task.mySource == 'top':
        output = parser.getTitlesFromTop(int(text), task.myFilter)
    else:
        output = parser.getTitlesFromAll(int(text), task.myFilter)
    question = simple_bot.send_message(chat_id, output)

simple_bot.polling(none_stop=True)
