# Задача 1. Задайте список случайных чисел 
# от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
import random

def Myranddigits(rightstop, elements):
    numbers = [random.randint(1, rightstop) for i in range(elements)]
    return numbers

my_numbers = Myranddigits(10, 6)
my_numbers = list(filter(lambda x: x > 5, my_numbers))
print(my_numbers)
