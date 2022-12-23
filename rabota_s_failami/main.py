def read_csv():
    with open('data.txt') as file1:
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
