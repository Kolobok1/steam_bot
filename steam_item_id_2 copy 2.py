import os
import asyncio,time
import requests
import json

headers = {
         "Accept": "*/*"
}

data = {}
s = requests.Session()

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
    asyncio.sleep(6000)
    time.sleep(2)
