import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot("7199680669:AAFlVbRG6IH_Q7NXB7Sz3o2vXlwUyzANDxE")


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://ru.wikipedia.org/wiki/%D0%A8%D0%B0%D1%85%D0%BC%D0%B0%D1%82%D1%8B')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nОтправь картинку и узнай моё мнение')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u> information</u></em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == '/start':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = (types.InlineKeyboardButton('Перейти на сайт', url='https://souvenir-vip.ru/shakhmaty-premialnye/'))
    markup.row(btn1)
    btn2 = (types.InlineKeyboardButton('Удалить фото', callback_data='delete'))
    btn3 = (types.InlineKeyboardButton('Изменить текст', callback_data='edit'))
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
    elif callback.data == 'edit':
        bot.edit_message_text('edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(non_stop=True)