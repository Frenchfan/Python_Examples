# Задача 2. В файле находятся названия фруктов.
# Выведите все фрукты, названия которых 
# начинаются на заданную букву.
def give_me_fruits(letter):
    data = open('fruit.txt', encoding='utf-8')
    content = data.read()
    data.close()
    content = content.split()
    for fruit in content:
        if fruit.startswith(letter):
            print(fruit)
letter = input("Введите первую букву фруктов: ")
give_me_fruits(letter) 