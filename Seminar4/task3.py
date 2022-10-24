# Задача 3. Сгенерируйте список случайных чисел от 1 до 20, 
# состоящий из 10 элементов. 
# Удалите из списка дубликаты уже имеющихся элементов.
import random

def myranddigits(numbers):
    numbers = [random.randint(1, 20) for i in range(10)]
    return numbers

myList = ()
myList = myranddigits(myList)
print(myList)
mySet = set(myList)
print(mySet)