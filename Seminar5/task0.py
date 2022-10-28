# Задача 0. С помощью анонимной функции 
# найдите в списке на 15 элементов числа, кратные 5. Заполните список 
# случайным образом числами от 1 до 100.
import random

def Myranddigits(rightstop, elements):
    numbers = [random.randint(1, rightstop) for i in range(elements)]
    return numbers


my_numbers = Myranddigits(100, 15)
print(my_numbers)
my_numbers = list(filter(lambda x: x%5 == 0, my_numbers))
print(f"Числа, кратные 5 : {my_numbers}")