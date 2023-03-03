import json

with open('list_items_buy.json', 'r', encoding='utf-8') as fh:
    urls = json.load(fh)
    
data = {}

def remake():
    n = 0
    print('нажмите + чтобы оставить предмет')
    for name in urls:
        print(name)
        ver = input()
        if ver == '+':
            data[name] = urls[name]
            n += 1

    file = open("list_items_buy.json", 'w')
    json.dump(data,file)
    file.close()
    print(n)

def price_buy():
    print('введите цену без точки')
    for name in urls:
        print(name)
        print(urls[name]['url'])
        price = input()
        urls[name]['new_price'] = price

    file = open("list_items_buy.json", 'w')
    json.dump(urls,file)
    file.close()

def rer():
    for name in urls:
        print(name)
        ver = input()
        if ver != '-':
            data[name] = urls[name]
            
    file = open("list_items_buy.json", 'w')
    json.dump(data,file)
    file.close()

wat = input('убрать или цена: ')
if wat == 'убрать':
    rer()
elif wat == 'цена':
    price_buy()

    
    