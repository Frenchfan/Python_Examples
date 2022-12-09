# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена 
# все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. 
# Определите группу с наилучшим средним баллом.

import random

def Myranddigits(leftstop, rightstop):
    m = random.randint(20, 30)
    numbers =[[random.randint(leftstop, rightstop) for j in range(m)] for i in range(random.randint(1, 10))]
    return numbers
    
def CheckMaxAverage(numbers):
    average = []
    for row in numbers:
        aver = 0
        for grade in row:
            aver += grade
        average.append(aver / len(row))
    return average.index(max(average))

my_numbers = Myranddigits(2, 5)
print(f'Наилучший средний бал у группы с индексом {CheckMaxAverage(my_numbers)}')