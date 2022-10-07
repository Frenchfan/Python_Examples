# типы данных и переменная
# int, float, boolean, str, list, None

from operator import inv


value = None
print(type(value))
a = 123
b = 1.23
print(a)
print(b)
value = 1234
print(value)
print(type(a))
print(type(b))
print(type(value)) # показать тип переменной
s = 'hello \nworld'
print(s) # вывод строки
print(a, ' - ', b, ' - ', s)
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s)) #переставил буквы
f = True
print(type(f))

list = [1, 2, 3, 'rrrt'] # можно чередовать разные типы
print(list)
d = int(input('Введите первое число')) #показывает, что нужно целое число
e = int(input()) # без int будет конкатенация строк
print(d, ' + ', e, ' = ', d+e)
g = 2
h = 8
i = g//h # это целочисленное деление
j = g ** h  # возведение в степень - встроенная функция
print(i)
k = 1.3
l = 3
m = round(k * l, 1) #Без функции round даст 3.9000000000000004 
print(m)
l += 5
print(l)
n = 1 < 4 and 5 > 2
print(n)
o = 1 < 3 < 5 #можно использовать тройные  и четверные неравенства
p = [1, 2, 3, 4] #список - заменяет массивы
print(2 in p)

if d > e:
    print(d)
else:
    print(e)
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит')
print(inverted)

for i in 1,2,3,4,5:
    print(i**2)

    r = range(10)
    for i in r: #цикл будет повторяться от 1 до 9
        print(i)    
for i in range(1, 5, 2): # третье число обозначает шаг - 2 тут
    print(i**2)
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
    print(c)
print(text[0]) # c представление списка как набора символов
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ - от нулевого символа до второго
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2 # кладем только во внутреннюю переменную, не в список
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue
for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return