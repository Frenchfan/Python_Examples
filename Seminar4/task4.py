# Задача 4. Дано число N. Найдите площадь круга
#  с радиусом N. Ответ округлите до сотых.

import math


def RoundSquare(n):
    square = math.pi * n**2
    return round(square, 2)

newN = int(input("Введите радиус круга: "))
print(RoundSquare(newN))