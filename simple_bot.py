import telebot

simple_bot = telebot.TeleBot('740731369:AAF574uUdnizwHGgnB8L0I6Pjl7mht-NOok')

@simple_bot.message_handler(content_types=['text'])
def get_messages(message):
    if message.text == 'Привет!':
        simple_bot.send_message(message.from_user.id, 'Привет, что тебе надо?')
    elif message.text == '/help':
        simple_bot.send_message(message.from_user.id, 'Напиши "Привет!"')
    else:
        simple_bot.send_message(message.from_user.id, 'Непонятно! Напиши /help')

simple_bot.polling(none_stop=True, interval=0)
