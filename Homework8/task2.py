# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк 
# превосходит сумму главной диагонали матрицы.

import random

def Myranddigits(leftstop, rightstop):
    m = random.randint(1, 10)
    numbers =[[random.randint(leftstop, rightstop) for j in range(m)] for i in range(random.randint(1, 10))]
    return numbers
    
def whichisMore(numbers):
    for i in numbers:
        print(i)
    sum_main_diagonal = 0
    sum_row = []
    for i in range(len(numbers)):
        sum_main_diagonal += numbers[i][i]
    print(f"Сумма главной диагонали = {sum_main_diagonal}")
    for i in numbers:
        sum_row.append(sum(i))             
    for i in range(len(sum_row)):
        if sum_row[i] > sum_main_diagonal:
            print(f"в {i + 1} группе сумма больше, чем сумма элементов диагонали")

my_numbers = Myranddigits(1, 10)
whichisMore(my_numbers)
