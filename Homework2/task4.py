# Задача 4. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.
def shifting_the_list(number, shift):
    mylist = list(range(- number, number + 1))
    for i in range(shift):
        mylist.insert(0,mylist.pop())
    print(*mylist)
number = int(input("Введите число: "))
shift = int(input("Введите число для сдвига элементов промежутка: "))
shifting_the_list(number, shift)
