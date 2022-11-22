# Задача 2. Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число. Напишите 
# программу, которая определяет, есть в массиве 
# последовательность из трёх элементов, совпадающая с 
# введённым числом

import random

def Myranddigits(rightstop, elements):
    numbers = [random.randint(0, rightstop) for i in range(elements)]
    print(numbers)
    return numbers
    
def CheckChain(numbers, digit):
    numberstr = ''
    for i in numbers:
        numberstr += str(i)
    if numberstr.count(digit) > 0:
        print("Да")
    else:
        print("Нет")

my_numbers = Myranddigits(9, 15)
myDigit = input("Введите трехзначное число: ")
CheckChain(my_numbers, myDigit)