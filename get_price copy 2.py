import requests
from bs4 import BeautifulSoup
import json
import time


headers = {
    "Accept": "*/*",
}

login = 'login'
password = 'password'


proxies_list = [ 
    {'https':f'http://{login}:{password}@188.74.210.207:6286'},
    {'https': f'http://{login}:{password}@185.199.229.156:7492'},
    {'https': f'http://{login}:{password}@185.199.228.220:7300'},
    {'https': f'http://{login}:{password}@185.199.231.45:8382'},
    {'https': f'http://{login}:{password}@188.74.183.10:8279'},
    {'https': f'http://{login}:{password}@188.74.210.21:6100'},
    {'https': f'http://{login}:{password}@45.155.68.129:8133'},
    {'https': f'http://{login}:{password}@154.95.36.199:6893'},
    {'https': f'http://{login}:{password}@45.94.47.66:8110'},
    {'https': f'http://{login}:{password}@144.168.217.88:8780'}
    
]

n = 0
proxies = proxies_list[n]



num = 0
with open('list_items_buy.json', 'r', encoding='utf-8') as fh:
    urls = json.load(fh)

ses = requests.Session()


def get_html(proxies):
    id = urls[name]['id']

    params = {
        'country': 'RU',
        'language': 'russian',
        'currency': '5',
        'item_nameid': id,
        'two_factor': '0',
    }

    response = ses.get('https://steamcommunity.com/market/itemordershistogram', params=params, headers=headers, proxies=proxies).text



    soup = BeautifulSoup(response, "lxml")
    
    a = soup.find_all('tr')
        
    price = a[-6].text
        
    price =price.partition(' ')[0].replace(',','.')
    
    urls[name]['new_price'] = price
    file = open("list_items_buy.json", 'w')
    json.dump(urls,file)
    file.close()
    return price

for name in urls:
    try:
        get_html(proxies)

        num += 1
        print('готово ' + str(num))
        time.sleep(2)
        
    except IndexError: 
        n += 1
        num += 1
        print('смена IP адреса')
        proxies = proxies_list[n]
  
        get_html(proxies)
