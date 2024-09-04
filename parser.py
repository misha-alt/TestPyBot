import requests
from bs4 import BeautifulSoup




URL = 'https://habr.com/ru/news/'

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

post = soup.find("div", class_="tm-articles-list")

title = post.find("h2", class_="tm-title tm-title_h2").text.strip()

article_id = post.find('article')['id']


# Извлекаем первый абзац
paragraph = soup.find("article").find('p')
if paragraph:
    paragraph_text = paragraph.text.strip()
else:
    paragraph_text = "Абзац не найден."

# artikle = post.find("article", class_="tm-articles-list__item").text.strip()
# next = post.find("div", class_="tm-article-snippet tm-article-snippet").text.strip()

urlH = post.find("a", class_="tm-title__link", href=True)["href"].strip()
print(paragraph_text)


