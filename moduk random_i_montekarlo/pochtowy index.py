# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 00 до 9999 (включительно).
#
# Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.
#
# Примечание 1. Пример правильного (неправильного) индекса Латверии:
#
# AB23_56VG          # правильный
# V3F_231GT          # неправильный
# Примечание 2. Обратите внимание на символ _ в почтовом индексе.
from random import *
def generate_index():
    n = 1
    ls = []

    while n <= 7:
        if n == 1 or n == 2:
            x = randint(65,90)
            x = chr(x)
            ls.append(str(x))
            n += 1
        if n == 3:
            x = randint(0, 99)
            ls.append(str(x))
            n += 1
        if n == 4:
            ls.append('_')
            n += 1
        if n == 5:
            x = randint(0, 99)
            ls.append(str(x))
            n += 1
        if n == 6:
            x = randint(65, 90)
            x = chr(x)
            ls.append(str(x))
            n += 1
        if n == 7:
            x = randint(65, 90)
            x = chr(x)
            ls.append(str(x))
            n += 1
    s =''.join(ls)
    return s
