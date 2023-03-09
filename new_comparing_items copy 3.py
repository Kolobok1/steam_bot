from bs4 import BeautifulSoup
import requests, re
import time,random
import asyncio
import json

headers = {
    "Accept": "*/*",
}

login = 'login'
password = 'password'

def proxies_fun(n):
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

    proxies = proxies_list[n]
        
    return proxies


n = 0
err = 0



def Inscribed(price_item,name):
    price = urls[name]['price']
    
    price_item = re.findall(r'\d+', price_item) 
    price_item = float(price_item[0]) + (float(price_item[1])/100)
    price_item -= price_item * 0.09
    price_item =  round(price_item,2)
    price_item = '$' + str(price_item) + ' USD'
    
    if price_item  > price:

        data[name]={'url': url_item}
        with open('list_items_buy.json', 'w') as file:
            json.dump(data, file)

def Ordinary(price_item, price):
    
    price = re.findall(r'\d+', price) 
    price = float(price[0]) + (float(price[1])/100)
    price -= price * 0.23
    price =  round(price,2)
    price = '$' + str(price) + ' USD'
    
    if price_item < price:
        with open(f"list_item_Ordinary.html",'a', encoding='utf-8') as file:
            file.write(name + '\n')


def comparison(url,name,proxies): 
    
    r = requests.get(url, headers=headers,proxies=proxies) #,proxies=proxies
    print(r)
    
    if r.status_code == 200:
    
        try:
            src = r.text
                
            soup = BeautifulSoup(src, "lxml")

            price_item = soup.find('span', class_='sale_price').text
            if quality == 'редкое':
                Inscribed(price_item,name)
            elif quality == 'обычное':
                Ordinary(price_item)
            else:
                print('Error')
    
            asyncio.sleep(3000)
            time.sleep(1)
        except:
            global err
            err += 1

    else:

        print('смена IP адреса')
        asyncio.sleep(2000)
        global n
        n+=1
        if n == 9:
            n = 0
        proxies = proxies_fun(n)
        comparison(url,name,proxies)

with open('name_items_list.json', 'r', encoding='utf-8') as fh:
    urls = json.load(fh)

num = 0

data = {}

quality = input('Введите качество предмета (обычное или редкое) ')

for name in urls:
    

    price = urls[name]['price']
    
    
    url_item = urls[name]['url']
    url = 'https://steamcommunity.com/market/search?category_570_Hero%5B%5D=any&category_570_Slot%5B%5D=any&category_570_Type%5B%5D=any&category_570_Quality[]=tag_unique&appid=570&q=' + name.replace('Inscribed ','')

    proxies = proxies_fun(n)
    comparison(url,name,proxies) #,proxies

    
    num += 1
    print('Предметов проверено: ' + str(num))
    
    asyncio.sleep(4000)
    time.sleep(1)

print(f'найдено ошибок {err}')
