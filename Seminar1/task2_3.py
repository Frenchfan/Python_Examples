# 3. Напишите программу, которая будет на вход
# принимать число N и выводить числа от -N до N
number = int(input("Введите число: "))
# for i in range(-number, number + 1):
#     print(i, end=' ') 
number = abs(number)
n = range(- number, number + 1)
print(*n) # показывает содержимое range