# Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна содержать реализованную функцию read_csv.
#
# Примечание 1. Вызывать функцию read_csv не нужно.
#
# Примечание 2. Функция read_csv не должна принимать аргументов.



def read_csv():
    with open('data.csv') as file1:
        ls_wsjo = [c.strip() for c in file1.readlines()]
        ls_keys = ls_wsjo[0].split(',')
        ls_values = []
        for c in range(1, len(ls_wsjo)):
            x = ls_wsjo[c].split(',')
            ls_values.append(x)
        ls_otwet = []
        for c in range(len(ls_values)):
            y = dict(zip(ls_keys, ls_values[c]))
            ls_otwet.append(y)
        return ls_otwet