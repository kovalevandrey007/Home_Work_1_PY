"""
4. Программа загадывает число от 0 до 1000. Необходимо угадать
число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки.
Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
from random import randint

def guess_number():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    for i in range(10):
        guess = int(input('Введите число: '))
        if guess < num:
            print('Ваше число меньше загаданного')
        elif guess > num:
            print('Ваше число больше загаданного')
        else:
            print('Вы угадали!')
            break

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
guess_number()

