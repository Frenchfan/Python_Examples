# Задача 2. В первой строке файла находится 
# информация об ассортименте мороженного, во второй -
# информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.
def find_dif(a,b):
    c = a - b
    return c

def read_lines(filename):
    with open(filename, "r", encoding = "utf-8") as data:
        fullchoice = set(data.readline()[1:-2].split('», «'))
        leftchoice = set(data.readline()[1:-1].split('», «'))
    print(fullchoice)
    print(leftchoice)
    print("Закончилось: " , *find_dif(fullchoice, leftchoice))

read_lines("icecream.txt")

