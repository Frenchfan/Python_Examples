# Задача 4. Найдите все числа до 10000, 
# у который количество делителей равно 10.
def check_number(n):
    dividers = list()
    for divider in range(1, int(n ** 0.5)):
        if n % divider == 0:
            dividers.append(divider)
    return len(dividers) == 5

def find_numbers():
    numbers = list()
    for i in range(1, 10_001):
        if check_number(i):
            numbers.append(i)
    return numbers

print(find_numbers())