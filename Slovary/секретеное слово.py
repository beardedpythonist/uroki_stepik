# Секретное слово
# Напишите программу для расшифровки секретного слова методом частотного анализа.
#
# Формат входных данных
# В первой строке задано зашифрованное слово. Во второй строке задано одно целое число nn – количество букв в словаре. В следующих nn строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.
#
# Формат выходных данных
# Программа должна вывести дешифрованное слово.
#
# Примечание. Гарантируется, что частоты букв не повторяются.


s = str(input())
slovar = {}
for c in range(int(input())):
    s1 = str(input())
    a, b = s1.split(': ')
    slovar[b] = a
sloavar2 = {}
for i in s:
    sloavar2[i] = sloavar2.get(i, 0) + 1
for key1, val1 in slovar.items():
    for ke2, val2 in sloavar2.items():
        if key1 == str(val2):
            s = s.replace(ke2, val1)
print(s)
