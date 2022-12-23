# Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все строки наибольшей длины из файла, не меняя их порядок.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести строки указанного файла, имеющие наибольшую длину, не меняя их порядка.
with open('lines.txt', encoding ='utf-8') as file:
    ls = [line.strip() for line in file.readlines()]
def dlina(x):
    return len(x)
ls = sorted(ls, key=dlina, reverse=True)
ls = list(filter(lambda x: len(x) == len(ls[0]), ls))
print(*ls, sep='\n')

