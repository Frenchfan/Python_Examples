def Open_Contacts():
    data = open('C:\Projects\GB\Python\Python_Examples\Homework7\contacts.txt', 'r', encoding="utf=8")
    tell = data.read()
    data.close
    return tell

def Add_Contacts():
    data = open('C:\Projects\GB\Python\Python_Examples\Homework7\contacts.txt', 'a')
    name = input('Введите Имя и телефон (Name 321654987): ')
    data.write(f"{name}\n")
    data.close

def Search_Contacts():
    data = open('C:\Projects\GB\Python\Python_Examples\Homework7\contacts.txt', 'r', encoding="utf=8")
    name = data.read()
    name = name.split('\n')
    data.close
    search = input("Введите имя: ")
    for i in range(len(name)):
        value = name[i]
        if search == str(value[0: len(search)]):
            return value
