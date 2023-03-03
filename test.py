from steampy.client import SteamClient #импортируем библиотеку
from steampy.models import GameOptions, Currency
from bs4 import BeautifulSoup
import requests
import json,pickle
import time,asyncio

headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"
}


# def price_stat(price):
#     print(price)

# steam_client = SteamClient('67FF61057B1CEBA7828E7009A2770B3D') 
# steam_client.login('kolobo4ik0_0', 'Qwas1452', 'steam_guard.json')

with open(f"steamClient.pkl", 'rb') as file:
    steam_client = pickle.load(file)


with open('list_items_buy.json', 'r') as fh:
    urls = json.load(fh)

num = 0

buy_item_manually = []
num_manually = 0

# for name in urls:
#     price = urls[name]["new_price"][0].replace('.','')
#     print(price)

for name in urls:
    try:
        num += 1
        price = urls[name]["new_price"].replace('.','')

        price = int(price) + 1
        
        

        response = steam_client.market.create_buy_order(f'{name}', f'{price}', 1, GameOptions.DOTA2, Currency.RUB)
        buy_order_id = response["buy_orderid"]
        urls[name]['buy_order_id'] = buy_order_id
        file = open("list_items_buy.json", 'w')
        json.dump(urls,file)
        file.close()
        
        print('выставлено: ' + str(num))
        asyncio.sleep(4000)
        time.sleep(2)
        
    except KeyError:
            print(f'цена на "{name}" не указана')
            continue
        
    except:
        try:
            print(f'выставляем новый запрос на "{name}"')
            time.sleep(1)

            buy_order_id = urls[name]['buy_order_id']
            response = steam_client.market.cancel_buy_order(buy_order_id)

            
            response = steam_client.market.create_buy_order(f'{name}', f'{price}', 1, GameOptions.DOTA2, Currency.RUB)
            buy_order_id = response["buy_orderid"]
            urls[name]['buy_order_id'] = buy_order_id
            file = open("list_items_buy.json", 'w')
            json.dump(urls,file)
            file.close()
            # time.sleep(4)
            continue
        except:
            print('ЗАПРОС ВЫСТАВЛЕН ВРУЧНУЮ')
            buy_item_manually.append(name)
            num_manually += 1
            
            urls[name]['buy_order_id'] = ''
            file = open("list_items_buy.json", 'w')
            json.dump(urls,file)
            file.close()
            
            time.sleep(1)
            continue
            # steam_client
            # url = urls[name]['url']
            # # req = requests.get(url,headers=headers)
            # req = steam_client
            # src = req.text
            # soup = BeautifulSoup(src, 'lxml')
            # cancel = soup.find('div', class_='market_listing_cancel_button')
            # # buy_order_id = cancel.find('href')
            # print(cancel)

if buy_item_manually != []:
    print(buy_item_manually)
    print(num_manually)
