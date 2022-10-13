from re import A


colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) #разделителей не будет
data.close # при этом подходе нужно закрывать файл

with open('file.txt', 'a') as data:
    data.write('line 1\n')
    data.write('line 2\n')
# в этом режиме не нужно закрывать - это происходи автоматически

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close

def fib(n):
    if n in [1, 2]:
        return 1
    else:
            return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34


a = (3, 4) # это пример кортежа
print(a)

# словари
dictionary = {}
dictionary = \
    {
        'up': 'вверх',
        'left': 'влево',
        'right': 'вправо',
        'down': 'вниз'
    }
print(dictionary) #{'up': 'вверх', 'left': 'влево', 'right': 'вправо', 'down': 'вниз'}
print(dictionary['left']) #влево

for k in dictionary.keys():
    print(k)
for k in dictionary.values():
    print(k)
for k in dictionary.keys():
    print(dictionary[k])

# множества - коллекция уникальных неупорядоченных элементов
colors = {'red', 'green', 'blue'}
colors.add('red') # нет ошибки, но и добавлен не будет - повтор
colors.remove('red') # удаление элемента из множества, вызывает ошбику, если нет элемента
colors.discard('red') # удаляет, не вызывает ошибку, если элемента нет
colors.clear() # очищает множество

a = frozenset('red') # неизменяемое множество