# Парсинг

from bs4 import BeautifulSoup # Библиотека для работы с данными страницы
import urllib.request
import re
req = urllib.request.urlopen('http://minecraftrating.ru/') #Делаем запрос по ссылке
html = req.read() # Читаем содержимое ответа
soup = BeautifulSoup(html, 'html.parser') # Создали объект для работы с html
servers = soup.find_all('div', class_='info') # Делаем поиск по всем div у которых класс name получаем на выходе список
results = [] # создаю массив с элементами
for item in servers:
    #title = item.find('div', class_='name').get_text()
    href = item.a.get('href')
    results.append({
        "href": href
    })

for item in results:
    # siteReq = urllib.request.urlopen(f'http://minecraftrating.ru{item['href']}')
    print(f'http://minecraftrating.ru{item["href"]}')


