# Задача 3. Дано число N. Заполните список 
# длиной N элементами 1, -3, 9, -27, 81, -243...
number = int(input("Введите число: "))
outputrange = []
for i in range(0, number):
    outputrange.append((-3)**i)
print(*outputrange)
