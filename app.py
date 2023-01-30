import telebot
from config import keys, TOKEN
from extensions import CurrencyConverter, ConvertionException
import sqlite3
from datetime import datetime

bot = telebot.TeleBot(TOKEN)

connection = sqlite3.connect("db/tgbot.db", check_same_thread=False)
cursor = connection.cursor()
cursor.execute('create table if not exists rate(tgbot_id primary key, course_value text, currency text, date datetime)')


def db_table_val(course_value: str, currency: str,  date: str):
    cursor.execute('INSERT INTO rate (course_value, currency, date) VALUES (?, ?, ?)',
                   (course_value, currency, date))
    connection.commit()


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу введите комманду боту в следующем формате:\n<имя валюты>\
    <в какую валюту перевести> \
    <количество переводимой валюты>\nУвидеть список всех доступных валют: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров.')

        quote, base, amount = values
        total_base = CurrencyConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

        kurs = f'{total_base} {base}'
        valuta = f'{amount} {quote}'
        now = datetime.now()
        formatted_date = now.strftime("%d-%m-%Y")

        db_table_val(course_value=kurs, currency=valuta, date=formatted_date)



bot.polling(none_stop=True)





