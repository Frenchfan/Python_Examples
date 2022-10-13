# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.
def summing_elements(mylist):
    mysum = 0
    for i in range(1, len(mylist), 2):
        mysum += mylist[i]
    print(f"Сумма элементов на нечетных позициях равна: {mysum}")
newlist = [2, 3, 5, 9, 3]
summing_elements(newlist)
newlist2 = [3, 5, 4, 7, 2, 57, 18, 2]
summing_elements(newlist2)