#



n = 8
xy = input()
y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])
matrix = ['.'] * n
for i in range(n):
    matrix[i] = ['.'] * n

for i in range(n):
    for j in range(n):
        if x == j and y == i:
            matrix[j][i] = 'N'
        INX = (x - j) * (y - i)
        if INX == 2 or INX == -2:
            matrix[j][i] = '*'

for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()
