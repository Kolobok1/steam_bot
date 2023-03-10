from bs4 import BeautifulSoup
import re, requests
import time,random
import asyncio
import json


headers = {
    "Accept": "*/*",
}

def urls(num, headers, url):
    
    r = requests.get(url, headers=headers)
    
    if r.status_code != 200:
        print('\n' + 'Подождите немного' + '\n')
        time.sleep(30)
        stop, num = urls(num, headers, url)
        return stop, num
            
    html = r.json()['results_html']

    soup = BeautifulSoup(html, "lxml")

    name_item = soup.find_all('a', class_='market_listing_row_link') #  select('.market_listing_row_link')

    if name_item == []:
        stop = 0
        return stop, num


    for el in name_item:
        try:
            item_url = el.get('href') # el['href']
            name = el.find('span', class_='market_listing_item_name') # имя
            quantity = el.find('span', class_='market_listing_num_listings_qty').text # количество
            price = el.find('span', class_='sale_price').text #  цена

            quantity = int(quantity)

        except:
            print('ошибка')
            quantity = 0
            continue


        if price >= min_price and price <= max_price:
            if quantity >= 20:

                name = el.find('span', class_='market_listing_item_name').text
                slov[name] = {'url': item_url, 'price': price}

                file = open("name_items_list.json", 'w')
                json.dump(slov,file)
                file.close()

                num += 1

                print(f'Найдено предметов: {num}')

        asyncio.sleep(3000)        
        time.sleep(1)


    stop = 1
    return stop, num


start = int(input('С какой страницы '))
page = start
start = (start - 1)* 10           
min_price = input('Введите минимальную цену в USD: ')
min_price = '$' + str(min_price) + ' USD'
max_price = input('Введите максимальную цену в USD: ')
max_price = '$' + str(max_price) + ' USD'

num = 0
slov = {}

slots = ['tag_armor', 'tag_weapon', 'tag_head', 'tag_offhand_weapon', 'tag_mount', 'tag_legs', 'tag_shoulder', 'tag_belt', 'tag_arms'] # 'tag_back', 'tag_tail','tag_neck'

for slot in slots:
    stop = 1
    
    while stop == 1:
        
        
        url = f'https://steamcommunity.com/market/search/render/?query=&start={start}&count=10&search_descriptions=0&sort_column=popular&sort_dir=desc&appid=570&category_570_Slot[]={slot}&category_570_Quality[]=tag_strange'
        stop, num = urls(num, headers=headers, url=url)   
        start += 10
        # time.sleep(2)
        asyncio.sleep(3000)
        with open(f"pages_done.txt",'w', encoding='utf-8') as file:
            file.write('Страница '+ str(page) + ' готова ' )
        
        page = int(page) + 1
    start = 0    
       
