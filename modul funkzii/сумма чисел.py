# #На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
#
# Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если у двух чисел одинаковая сумма цифр, их следует вывести в порядке неубывания.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
#
# Формат выходных данных
# Программа должна вывести отсортированный список чисел в соответствии с условием задачи, разделяя его элементы одним пробелом.

s = input()
ls =[c for c in s.split()]
ls1 = [int(c) for c in ls]
ls1.sort()
def sum_chisel(point):
    n = 0
    point = int(point)
    while point > 0:
        y = point % 10
        n += y
        point = point // 10
    return n
x = sorted(ls1, key=sum_chisel)
print(*x)

