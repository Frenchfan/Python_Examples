# Задача 3. Создайте скрипт бота, который находит ответы
# на фразы по ключу в словаре. Бот должен, как минимум, 
# отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.
def start_bot():
    botdictionary = {}
    botdictionary = \
        {
            'привет': 'и тебе привет',
            'как тебя зовут': 'Афанасий',
            'сколько тебе лет': '115 годкрв',
            'давай до свидания': 'пока'
        }
    inputphrase = ''
    while inputphrase != 'exit':
        inputphrase = input("Введите фразу / вопрос: ")
        if inputphrase in botdictionary:
            print(botdictionary.get(inputphrase))
        else:
            print("Даже не знаю, что и сказать")
start_bot()