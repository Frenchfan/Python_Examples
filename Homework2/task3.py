# Задача 3. Даны две строки. Посчитайте 
# сколько раз каждый символ первой строки встречается во второй
def count_the_symbols(string1, string2):
    for i in range(len(string1)):
        print(f"{string1[i]} - {string2.count(string1[i])}")
        
string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")
count_the_symbols(string1, string2)