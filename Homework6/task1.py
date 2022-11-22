# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396
def SummingNs(N):
    singleN = str(N)
    doubleN = str(N) + str(N)
    tripleN = str(N) + str(N) + str(N)
    return int(singleN) + int(doubleN) + int(tripleN)   


myN = int(input("Введите число N: "))
print(SummingNs(myN))