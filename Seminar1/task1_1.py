number1 = int(input("Введите первое число:"))
number2 = int(input("Введите второе число:"))
if number2 == number1 ** 2:
    print(f"{number2} является квадратом числа {number1}")
elif number1 == number2 ** 2:
    print(f"{number1} является квадратом числа {number2}")
else:
    print(f"{number2} не является квадратом числа {number1}, квадрат {number1} равен {number1 ** 2}")
