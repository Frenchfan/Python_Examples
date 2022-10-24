# Задача 2. Актёров разделили на списки по трём 
# качествам «умные», «красивые», «сильные». На главную роль
#  нужен актёр обладающий всеми тремя качествами. Определите, 
#  сколько есть претендентов на главную роль. 
# Списки актёров поместите в соответствующие файлы.
# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад
handsome = set()
strong = set()
smart = set()

with open('handsome.txt', encoding='utf-8') as inf:
    for line in inf.readlines():
        handsome.add(line.rstrip())
print(handsome)

with open('strong.txt', encoding='utf-8') as inf:
    for line in inf.readlines():
        strong.add(line.rstrip())
print(strong)

with open('smart.txt', encoding='utf-8') as inf:
    for line in inf.readlines():
        smart.add(line.rstrip())
print(smart)

print(handsome&strong&smart)