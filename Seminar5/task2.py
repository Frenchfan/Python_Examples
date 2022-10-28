# Задача 2. В зоопарк отправили отчёт 
# о новом поступлении зверей с ошибкой, 
# в результате которой некоторые данные 
# не расшифровались. Расшифруйте данные. 
# Определите, в какой клетке находится лев. 
# Номер клетки совпадает с номером строки.
# Используется русский алфавит - абвгдеёжзийклмнопрстуфхцчшщъыьэюя
# нужно вспомнить, что мощность алфавита равна 33 (кол-во букв)
# при двоичной кодировке в одну клетку мы можем записать 
# только 2 комбинации (0 или 1)
# поскольку мощность алфавита 33, то для кодировки одного символа 
# нужно 6! клеток
#Кол-во клеток определяем степенью 2 и достаточностью - 2^5 = 32 - этого мало
# 2^6 - 64 - этого достаточно для кодировки 33 символов
# поэтому каждые 6 символов - это одна буква!
# слово лев состоит из 3-х букв - то есть 18 двоичных символов
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# вариант решения без лямбды
# with open('animals.txt') as inf:
#     for line in inf.readlines():
#         numbers = line.rstrip()
#         chars = [numbers[i:i+6] for i in range(0, len(numbers), 6)]
#         print(chars)
#         for char in chars:
#             i = int(char, 2)
#             print(alphabet[i], end='')
#         print()
def ConvertToBinary2(number):
    result = ''
    while number > 0:
        result = str(number%2) + result
        number //= 2
    return result

codeList = [str(i) for i in range(len(alphabet))]
convertToBinary = lambda x: bin(int(x))[2:]
codeList = list(map(convertToBinary, codeList))
codeList = ["0"*(6 - len(i)) + i for i in codeList]
print(codeList)            
dictionary = {}
for i in range(len(codeList)):
    dictionary[codeList[i]] = alphabet[i]
print(dictionary)
data = open('animals.txt', 'r')
animalCodeList = data.readlines()
data.close()
for animal in animalCodeList:
    for i in range(len(animal)//6):
        bias = i * 6
        print(dictionary[animal[bias: bias + 6]], end = "")
    print()

