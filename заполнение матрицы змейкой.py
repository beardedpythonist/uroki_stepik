s = str(input())
ls = s.split()
n = int(ls[0])
m = int(ls[1])
matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * m
for i in range(n):
    for j in range(m):
        matrix[i][j] = 1 + j + matrix[i-1][m - 1]
for i in range(n):
    if i % 2 == 1:
         matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
