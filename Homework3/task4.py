# Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.
def ToBinary(number):
    if number > 1:
        ToBinary(number//2)
    print(number%2, end = "")
number = int(input("Введите число для преобразования в двоичное: "))
ToBinary(number)
