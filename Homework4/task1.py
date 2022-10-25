# Задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит 
# список простых множителей числа N.
def dividers(N):
    myList = []
    divider = 2
    while N > 1:
        if (N % divider == 0):
            myList.append(divider)
            N=N/divider
        else:
            divider += 1
    return myList        


myNumber = int(input("Введите число: "))
print(*dividers(myNumber))