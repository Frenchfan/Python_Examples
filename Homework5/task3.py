# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.

import random
from collections import Counter

def Myranddigits(rightstop, elements):
    numbers = [random.randint(1, rightstop) for i in range(elements)]
    return numbers

def Countrepeats(myList):
    myList = dict(Counter(my_numbers))
    sum = 0
    for i in myList:
        if myList.get(i) > 1:
            sum += myList.get(i)
    return sum

my_numbers = Myranddigits(10, 15)
norepeats = set(my_numbers)
print("Исходный список:")
print(my_numbers)
print("Список без повторов:")
print(norepeats)
print(f"Кол-во повторов в начальном списке - {Countrepeats(my_numbers)}")