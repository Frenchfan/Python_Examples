# 5. Напишите программу, которая находит наибольшее 
# и наименьшее число из списка значений
#mylist = [5,8,1,4,35,-5]
mylist = [int(el) for el in input().split()]
maximum = minimum = mylist[0]
for i in mylist:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i
print(f"Максимальное число из списка равно {maximum}, минимальное число равно {minimum}")
print(f"Второй способ: Максимальное число из списка равно {max(mylist)}, минимальное число равно {min(mylist)}")
