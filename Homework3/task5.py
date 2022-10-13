# Задайте число. Составьте список 
# чисел Фибоначчи, в том числе 
# для отрицательных индексов.
def Fibonacci(number):
    if number in [1, 2]:                       
        return 1
    else:
        return Fibonacci(number-1) + Fibonacci(number-2)

def NegaFibonacci(number):
    if number == 1:                       
        return 1
    elif number == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, number):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
number = int(input('Введите число: '))
for e in range(1, number + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)