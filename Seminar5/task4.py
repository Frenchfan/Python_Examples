# Задача 4. Задайте список из 15 случайных чисел. 
# Выведите все пары кратных чисел из этого списка.
import random

def Myranddigits(rightstop, elements):
    numbers = [random.randint(1, rightstop) for i in range(elements)]
    return numbers


my_numbers = Myranddigits(100, 15)