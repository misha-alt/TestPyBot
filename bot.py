import telebot
import requests
from bs4 import BeautifulSoup
import time

token = "7340360500:AAFWvWg3AtQJj3Xt2HdfCT5DjtNsZplPD8w"
idcanal = '@newLincMisha'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def commands(message):
    #bot.send_message(channel_id, message.text)
    if message.text == "Старт":
        #bot.send_message(channel_id, "Hello")
        back_post_id = None
        while True:
            post_text = parserNews(back_post_id)
            back_post_id = post_text[1] 

            if post_text[0] != None:
                bot.send_message(message.chat.id, post_text[0])
                time.sleep(30)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши Старт")



def parserNews(back_post_id):
    URL = 'https://habr.com/ru/news/'

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find("div", class_="tm-articles-list")

    title = post.find("h2", class_="tm-title tm-title_h2").text.strip()
    urlH = post.find("a", class_="tm-title__link", href=True)["href"].strip()

    # post_id = post["id"]
    post_id = post.find('article')['id']
    
    if post_id != back_post_id:
        title = post.find("h2", class_="tm-title tm-title_h2").text.strip()
        urlH = post.find("a", class_="tm-title__link", href=True)["href"].strip()
        fullUrl = f"https://habr.com{urlH}"
        
        return f"{title}\n\n{fullUrl}", post_id
    else:
        return None, post_id

bot.polling()    