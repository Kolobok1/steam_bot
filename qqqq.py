import json

def calculate():
    n = 0

    for i in urls:
        # print(i)
        n+=1

    print(n)


# добавить buy_order_id из прошлых запросов
def add_buy_order_id():
    
    with open('77777.json', 'r', encoding='utf-8') as fh:
        dob = json.load(fh)
    
    for name in dob:
        try:
            buy_order_id = dob[name]['buy_order_id']
            urls[name]['buy_order_id'] = buy_order_id
            file = open("list_items_buy.json", 'w')
            json.dump(urls,file)
            file.close()
            # print(buy_order_id)
        except KeyError:
            continue


with open('list_items_buy.json', 'r', encoding='utf-8') as fh:
    urls = json.load(fh)
    
    
# with open('name_items_list.json', 'r', encoding='utf-8') as fh:
#     urls = json.load(fh)


wat = input('посчитать или добавить: ')

if wat == 'посчитать':
    calculate()
elif wat == 'добавить':
    add_buy_order_id()

    
