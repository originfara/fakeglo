import os

import telebot
from telebot import types

os.system('cls' if os.name == 'nt' else 'clear')

bot = telebot.TeleBot('5476423037:AAEQdWT0E-VksJqCFYygJ0pw2IaINI4EBbw')
print('Бот запущен')


@bot.message_handler(commands=['go'])
def start(message):
    print('Бот запущен')
    bot.send_message(message.chat.id,
                     'Введи код с пачки стиков *neo/Kent* и других марок, которые импортирует ТОО «БРИТИШ АМЕРИКАН ТОБАККО КАЗАХСТАН ТРЕЙДИНГ».    '
                     '\n❗️ *Внимание* – можно добавлять только 14 кодов в неделю**')


@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, 'Идёт поиск...')
    bot.send_message(message.chat.id, f'Код: {message.text} принят.', parse_mode='html')
    print(message.chat.id, f'Код: {message.text}')
    bot.send_message(message.chat.id, 'Начислено 20 коинов (монет) за код')
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('🤝Пригласи респондента', callback_data='question_1')
    item2 = types.InlineKeyboardButton('Оставить отзыв', callback_data='goodbye')
    item3 = types.InlineKeyboardButton('Добавить еще один код', callback_data='goodbye_1')
    item4 = types.InlineKeyboardButton('Главное меню', callback_data='goodbye_2')
    markup.add(item, item2, item3, item4)

    bot.send_message(message.chat.id, 'Мои коины: 600', reply_markup=markup)


bot.polling()
