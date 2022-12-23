# Статистика по файлу
# Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести три найденных числа в формате, приведенном в примере.
#
# Примечание 1. Если бы файл file.txt содержал строки:
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# то результатом было бы:
#
# Input file contains:
# 108 letters
# 20 words
# 4 lines



import string
with open('file.txt', 'r') as file1:
    count = 0
    ls = [c.strip() for c in file1.readlines()]
    s1 = ' '.join(ls)
    for c in range(len(s1)):
        if s1[c] in string.ascii_letters:
            count += 1
    ls2 = s1.split()
print(f'Input file contains: \n' f'{count} letters \n' f'{len(ls2)} words \n' f'{len(ls)} lines')






