# Задача 1. Дан файл, заполненный числами построчно. Считайте файл. 
# Выведите все элементы, стоящие на чётных строках, а потом на нечётных.
def read_even_noteven():
    data = open('file.txt', encoding='utf-8')
    point = data.readlines()
    data.close()
    for i in range(0, len(point), 2):
        print(point[i], end = ' ')
    print()
    for i in range(1, len(point), 2):
        print(point[i], end = ' ')
read_even_noteven()
