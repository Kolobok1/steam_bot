import os
import asyncio,time
import requests
import json


# def load_file_rows(file_name, default=''):
#     # если файл существует
#     if os.path.isfile(file_name):
#         # чтение из файла
#         with open(file_name, "r") as file:
#             # читаем все строки и удаляем переводы строк
#             lines = file.readlines()
#             # и возвращаем ссылки на страницы для лайков
#             return [line.rstrip('\n') for line in lines]
#     else:
#         return [default]

# заголовки для авторизации
headers = {
         "Accept": "*/*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"
          }

# создадим сессию
data = {}
s = requests.Session()

# получичаем ID предмета
def get_item_id(url):
    r = s.get(url)
    html = r.text
    pos = html.find('Market_LoadOrderSpread(')
    if pos != -1:
        html = html[pos : ]
        pos = html.find(')')
        if pos != -1:
            html = html[ : pos - 1]
            html = html[ 24 : ]
            return html
        else:
            return None
    else:
        return None

with open('list_items_buy.json', 'r', encoding='utf-8') as fh:
    urls = json.load(fh)

for name in urls:
    url = urls[name]['url']
    # print(url)
    id = get_item_id(url)
    urls[name]['id'] = id
    file = open("list_items_buy.json", 'w')
    json.dump(urls,file)
    file.close()
    if id is not None:
        print(f'Item ID = {id}')
    else:
        print('ID not found')
    # print('WAIT 5 seconds')
    asyncio.sleep(6000)
    time.sleep(2)