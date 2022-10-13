# Задача 0. Дано число N. Найти все его делители. 
# Для каждого делителя укажите чётный он или нечётный.
def CheckEven(x):
    if x % 2 == 0:
        return " - четный"
    else:
        return " - нечетный"

def Zadacha0():
    number = 60
    for i in range(1, number + 1):
        if number % i == 0:
            print (i, end = " ")
            print(CheckEven(i))    
Zadacha0()
