# Задача 4. Напишите программу, которая на вход 
# принимает число (N), а на выходе показывает все чётные числа от 1 до N.
number = int(input("Введите число: "))
print(*range(2, number+1, 2))