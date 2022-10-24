#Задача 0. Создайте файл random.txt. 
# Запишите в него 10 случайных чисел.

import random

def myrandigits(numbers):
    for i in range(10):
        numbers.append(random.randint(1, 100))
    return numbers

with open("numbers.txt", 'w') as data:
    r=[]
    myrandigits(r)
    data.writelines(str(r))
