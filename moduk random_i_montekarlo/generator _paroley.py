# Генератор паролей 2 🌶️
# Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
# Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.
#
# Формат входных данных
# На вход программе подаются два числа nn и mm, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести nn паролей длиной mm символов в соответствии с условием задачи, каждый на отдельной строке.
#
# Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые пароли сгенерировать возможно.
#
# Примечание 2. Решение задачи удобно оформить в виде двух вспомогательных функций:
#
# функция generate_password(length) – возвращает случайный пароль длиной length символов;
# функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.
import string
from random import choice
def generate_password(lenth):
    s_up = string.ascii_uppercase.replace('I', '').replace('O', '')
    s_low = string.ascii_lowercase.replace('l', '').replace('o', '')
    dg = '23456789'
    q = s_up + s_low + dg
    parolj =''
    c = 0
    while c < lenth:
        c += 1
        x = choice(s_up)
        parolj += x
        if c == lenth:
            break
        c += 1
        x = choice(s_low)
        parolj += x
        if c == lenth:
            break
        c += 1
        x = choice(dg)
        parolj += x
        if c == lenth:
            break
        c += 1
        x = choice(q)
        parolj = parolj + x
        if c == lenth:
            break
    return parolj

def generate_passwords(count, length):
    for c in range(count):
        print(generate_password(length))
n, m = int(input()), int(input())
generate_passwords(n, m)