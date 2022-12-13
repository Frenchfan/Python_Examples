# Задача 1. Создайте telegram-бота, который 
# записывает все ответы пользователя в файл.

# Задача 2. Добавьте боту команды приветствия.

# Задача 3. Добавьте модуль для определения погоды с помощью 
# сайта wttr.in

# Задача 4. Перешлите с помощью бота себе файл с 
# компьютера.

# Задача 1. Добавьте telegram-боту возможность вычислять выражения:1 + 4 * 2 -> 9

# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000. 
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
import requests
import time
from random import randint


number = None
count = 1
is_started_game = False
is_started_calc = False
result = None

bot = telebot.TeleBot("Token", parse_mode=None)

@bot.message_handler(content_types=["text"])

def hello_user(message):
    global is_started_game
    global number
    global count
    global is_started_calc
    global result
    if 'привет' in message.text:
        bot.reply_to(message, 'привет, ' + message.from_user.first_name)
    elif message.text == 'играть':
        number = randint(1, 1001)
        count = 1
        is_started_game = True
        bot.reply_to(message, f'Я загадал число от 1 до 1000. Попробуй отгадай!')
        bot.reply_to(message, 'Если захочешь закончить игру, просто введи слово "стоп". Введи первое число')
    elif message.text == 'майкун':
        bot.reply_to(message, 'Симба - лучший, Симба - класс, кто не верит - тому в глаз!')
    elif message.text == 'погода':
        r = requests.get('https://wttr.in/?0T') # Эта ссылка сокращает выходные данные на сайте погоды
        bot.reply_to(message, r.text)
    elif message.text == 'котик':
        r = f'https://cataas.com/cat?t=${time.time()}'
        bot.send_photo(message.chat.id, r)
    elif message.text == 'файл':
        data2 = open('user_message.txt', encoding='utf-8') # это должно быть не обязательно, но иначе не работало
        bot.send_document(message.chat.id, data2)
        data2.close()
    elif message.text == 'калькулятор':
        is_started_calc = True
        result = None
        bot.reply_to(message, 'Введи выражение вида a+b, используя знаки +, -, *, /')
        bot.send_message(message.from_user.id, 'Для выхода введите "стоп"') 
    if is_started_game:       
        if message.text.isdigit():
            input_number = int(message.text)            
            if input_number > number:
                bot.send_message(message.from_user.id, 'Меньше!')                
            elif input_number < number:
                bot.send_message(message.from_user.id, 'Больше!')
            else:                
                is_started_game = False
                bot.send_message(message.from_user.id, f'Ты выиграл! Загаднное число {number}')
                bot.send_message(message.from_user.id, f'Количество попыток: {count}')
            count = count + 1
        elif message.text == 'стоп':
            is_started_game = False
            bot.send_message(message.from_user.id, 'Игра закончена')
        else:
            bot.send_message(message.from_user.id, 'Введи простое число')
    elif is_started_calc:                
        exp = str(message.text)
        if not '/' and not '*' and '-' in exp:
            exp = exp.replace('-', '+-')        
        if '+' in exp:
            exp = exp.split('+')            
            for number in exp:
                if number.isdigit():                       
                    result = int(exp[0]) + int(exp[1])
                else:
                    bot.send_message(message.from_user.id, 'Вы ввели некорректное выражение, введите выражение вида a+b')
                    bot.send_message(message.from_user.id, 'Для выхода введите "стоп"')
            bot.send_message(message.from_user.id, f'{message.text} = {result}')
            result = None
        elif '/' in exp:
            exp = exp.split('/')
            for number in exp:
                if number.isdigit():
                    result = int(exp[0]) / int(exp[1])                    
                else:
                    bot.send_message(message.from_user.id, 'Вы ввели некорректное выражение, введите выражение вида a+b')
                    bot.send_message(message.from_user.id, 'Для выхода введите "стоп"')
            bot.send_message(message.from_user.id, f'{message.text} = {result}')
            result = None
        elif '*' in exp:
            exp = exp.split('*')
            for number in exp:
                if number.isdigit():
                    result = int(exp[0]) * int(exp[1])                    
                else:
                    bot.send_message(message.from_user.id, 'Вы ввели некорректное выражение, введите выражение вида a+b')
                    bot.send_message(message.from_user.id, 'Для выхода введите "стоп"')
            bot.send_message(message.from_user.id, f'{message.text} = {result}')
            result = None
        elif message.text == 'стоп':
            is_started_calc = False
            bot.send_message(message.from_user.id, 'Вы вышли из режима вычисление')
        else:
            bot.send_message(message.from_user.id, 'Введите выражиажение вида a+b, используя знаки +, -, *, /')
            bot.send_message(message.from_user.id, 'Для выхода введите "стоп"')  
    # elif message.text == 'песик':
    #     r = requests.get(r'https://dog.ceo/api/breeds/image/random')
    #     mydata = json.loads(r.url)
    #     print(f'Вот какая фигня - {mydata}')
    #     # bot.send_photo(message.chat.id, mydata)

    data = open('user_message.txt', 'a+', encoding='utf-8')
    data.writelines(str(message.from_user.id) + ' ' + message.text + '\n')
    data.close()
    # bot.reply_to(message, message.text) #message.text - вытаскиваем сообщения

@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()