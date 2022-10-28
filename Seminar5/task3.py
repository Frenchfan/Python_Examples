# Задача 3. Имеется информация о том, 
# телефонами каких компаний сейчас 
# торгуют магазины. Определите те компании, 
# чьи телефоны присутствуют в каждом магазине.
data = open("phones.txt", 'r')
lines = data.readlines()
data.close()
mySet1 = set(lines[1].replace("\n", "").split(", "))
mySet2 = set(lines[3].replace("\n", "").split(", "))
mySet3 = set(lines[5].replace("\n", "").split(", "))
print(mySet1.intersection(mySet2).intersection(mySet3))