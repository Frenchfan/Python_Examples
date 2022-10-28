# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, 
# описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.

import random

def Myranddigits(rightstop, elements):
    numbers = [random.randint(1, rightstop) for i in range(elements)]
    return numbers

my_numbers = Myranddigits(100, 15)
print(my_numbers)
startSequence = random.randint(1, len(my_numbers) - 1)
print(my_numbers[startSequence])
my_Sequence = [my_numbers[startSequence], ]
currentIndex = startSequence
for i in range(startSequence, len(my_numbers) - 1):
    if my_numbers[i] > my_numbers[currentIndex]:
        my_Sequence.append(my_numbers[i])
        currentIndex = i
print(my_Sequence)