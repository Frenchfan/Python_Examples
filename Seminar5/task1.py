# Задача 1. На вход подаётся 
# четырёхзначное число. Получите список, состоящий 
# из цифр данного числа, увеличенных на 10.
# 9650 –> [19, 16, 15, 10]
# 1043 –> [11, 10, 14, 13]
number = list(input("Enter a 4-digit number: "))
print(number)
number = list(map(lambda x: int(x) + 10, number))
print(number)