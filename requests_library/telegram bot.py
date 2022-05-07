import json

import telebot
from configuration import TOKEN, keys
from extensions import APIException, Exchange

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help','start'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду в следующем формате: \n<имя валюты цену которой вы хотите узнать> \
<имя валюты в которой надо узнать цену первой валюты> \
<количество первой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text,key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Введите команду или 3 параметра')

        quote, base, amount = values
        total_base = Exchange.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Что-то пошло не так с {e}')
    else:
        text = f'Цена {quote} в {base}\n{amount} = {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()