# Задача 2. При работе с документацией 
# менеджер допустил ошибку, названия товаров 
# перемешались с ценами. Помогите восстановить 
# документ. Порядковый номер 
# товара совпадает с номером цены.

def read_prices():
    data = open('price.txt', encoding='utf-8')
    content = data.readline()
    data.close()
    mydata = content.split()
    prices = []
    tags = []
    for i in mydata:
        if i.isdigit():
            prices.append(i)
        else:
            tags.append(i)
    data = open('price.txt', 'w', encoding='utf-8')
    for i in range(len(tags)):
        data.write(tags[i] + "   " + prices[i] + '\n')
    data.close()
read_prices()

