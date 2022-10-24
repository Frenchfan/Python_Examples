# Задача 3. Напишите скрипт генератора паролей заданной длины,
#  состоящих из букв и чисел.
# Создайте скрипт для сохранения пароля в файл password.txt.
from random import random, randrange


def pass_gen(mylen):
    mypass = ""    
    for i in range(mylen):
        mypass += str(randrange(0, 100))
    data = open('password.txt', 'a', encoding='utf-8')
    data.write(mypass)
    data.close()
pass_gen(6)