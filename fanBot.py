import requests
import random
import telebot
from bs4 import BeautifulSoup as b

import requests


URL = 'https://www.anekdot.ru/'
API_KAY ='7497362360:AAFJ6XqpE43k4p9Rn5CBpzcVhHVcmFkigyo'
def parser(url):
    r= requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return[c.text for c in anekdots]

#   print(parser(URL));

list_of_anekdots = parser(URL)
random.shuffle(list_of_anekdots)


bot=telebot.TeleBot(API_KAY)

@bot.message_handler(commands=['начать'])

def hello(message):
    bot.send_message(message.chat.id, 'Привет! Нажми любую цифру')


@bot.message_handler(content_types=['text'])

def joke(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_anekdots[0])
        del list_of_anekdots[0]
    else:
        bot.send_message(message.chat.id, 'Нужно ввести цифру от 1 до 9')

bot.polling()
    