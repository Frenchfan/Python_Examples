# Задача 2. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа -определять количество вхождений одной строки в другую.
string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")
count = 0
if len(string1) > len(string2):
    for i in range(len(string1)):
        if string2 == string1[i: i + len(string2)]:
            count += 1
    print(f"Количество вхождений в строку составляет {string1.count(string2)}")
else:
    for i in range(len(string2)):
        if string1 == string2[i: i + len(string1)]:
            count += 1
    print(f"Количество вхождений в строку составляет {string2.count(string1)}")

print(f"Количество вхождений одной строки в другую: {count}")