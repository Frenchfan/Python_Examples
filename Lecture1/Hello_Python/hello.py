# типы данных и переменная
# int, float, boolean, str, list, None

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
d = int(input()) #показывает, что нужно целое число
e = int(input()) # без int будет конкатенация строк
print(d, ' + ', e, ' = ', d+e)
g = 2
h = 8
i = g//h # это целочисленное деление
j = g ** h  # возведение в степень - встроенная функция
print(i)