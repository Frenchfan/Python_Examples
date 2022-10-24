# Задача 1. Создайте кортеж, заполненный 
# случайными числами. Напишите метод, 
# который заменяет элемент в кортеже по заданному индексу.
import random

def myranddigits():
    size = random.randint(5,12) #интервал включает! границы
    numbers = tuple(random.randint(1, 100) for i in range(size))
    return numbers

def ChangeIndex(r, index):
    r = list(r)
    r[index - 1] = random.randint(1, 100)
    r=tuple(r)    
    return r

r = ()
r = myranddigits()
print(r)
index = int(input("Какой элемент кортежа ВЫ хотите заменить: "))
r = ChangeIndex(r, index)
print(r)
