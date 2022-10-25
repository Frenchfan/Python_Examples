# Задача 4*. Даны два файла, в каждом 
# из которых находится запись многочлена. 
# Найдите сумму данных многочленов.
from cgi import test


def summing_equations(equation1, equation2):
    mylist = equation1.split(" + ") + equation2.split(" + ")
    print(mylist)
    firstindex = 0
    secondindex = 0
    thirdindex = 0
    for i in mylist:
        if "x^2" in i:
            pos = i.find("x^2")
            if pos == 0:
                firstindex += 1
            else:
                firstindex += int(i[:pos])
        elif "x" in i:
            pos = i.find("x")
            if pos == 0:
                secondindex += 1
            else:
                secondindex += int(i[:i.find("x")])
        else:
            if i.isdigit:
                thirdindex += int(i)
    newequation = str(firstindex) + "x^2" + " + " + str(secondindex) + "x" + " + " + str(thirdindex)
    print(newequation)

with open("equation1.txt", 'r', encoding = "utf-8") as data:
    equation1 = data.readline()
with open("equation2.txt", 'r', encoding = "utf-8") as data:
    equation2 = data.readline()
summing_equations(equation1, equation2)