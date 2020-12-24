import json
import requests

from telegram.ext import (Updater, CommandHandler)
TOKEN = 'ваш токен'
URL = 'https://alfabank.ru/ext-json/0.2/exchange/cashless_alfa?offset=0&limit=6&mode=rest'


def get_bank_info(currency):
    r = requests.get(URL)
    currency_info = json.loads(r.content)
    if currency == 'USD':
        return currency_info['usd'][0]['value']
    else:
        return currency_info['eur'][0]['value']


def start(update, context):
    update.message.reply_text('Введите команду /usd2rub и количество долларов или /eur2rub и количество долларов')


def Usd2Rub(update, context):
    chat = update.effective_chat
    rate = get_bank_info('USD')
    try:
        user_val = float(context.args[0])
        result = round(user_val * rate, 2)
        context.bot.send_message(chat_id=chat.id,
                                 text=f"USD -> RUB \n{result}")
    except ValueError:
        context.bot.send_message(chat_id=chat.id,
                                 text="Напишите число для перевода")


def Eur2Rub(update, context):
    chat = update.effective_chat
    rate = get_bank_info('EURO')
    try:
        user_val = float(context.args[0])
        result = round(user_val * rate, 2)
        context.bot.send_message(chat_id=chat.id,
                                 text=f"EURO -> RUB \n{result}")
    except ValueError:
        context.bot.send_message(chat_id=chat.id,
                                 text="Напишите число для перевода")


def main():
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('usd2rub', Usd2Rub))
    updater.dispatcher.add_handler(CommandHandler('eur2rub', Eur2Rub))
 
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
