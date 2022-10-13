# Задача 1. Напишите программу, которая принимает на вход
#  число N и выдает список факториалов для чисел от 1 до N.
def factorial_list(number):
    fact_list = []
    for i in range(1, number + 1):
        tempsum = 1
        for j in range (1, i + 1):
            tempsum *= j
        fact_list.append(tempsum)
    print(*fact_list)

number = int(input("Введите число: "))
factorial_list(number)