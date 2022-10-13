# Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.
from operator import mul


def multiply_pairs(mylist):
    half = int(len(mylist) / 2)
    newlist = []
    for i in range(0, half):
        newlist.append(mylist[i] * mylist[len(mylist) - 1 - i])
    if (len(mylist) % 2) !=0:
        newlist.append(mylist[half] * mylist[half])
    print(*newlist)
mylist = [2, 3, 4, 5, 6]
multiply_pairs(mylist)
mylist2 = [2, 3, 5, 6]
multiply_pairs(mylist2)

        
