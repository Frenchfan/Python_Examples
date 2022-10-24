# Задача 4. Считайте строковые данные из файла. 
# Создайте словарь, содержащий все символы в файле.
def dictionaries():
    data = open('file.txt', encoding='utf-8')
    content = data.read()
    data.close()
    mydict = {}
    print(content)
    counter = 0
    for i in content:
        mydict[counter] = i
        counter += 1
    print(mydict)
dictionaries()