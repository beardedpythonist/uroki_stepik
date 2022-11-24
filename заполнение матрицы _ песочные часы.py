n = int(input())
matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * n
for i in range(n):
    for j in range(n):
        if i < j and i < (n - 1 - j):
           matrix[i][j] = 1
        if i > j and i > n - 1 - j:
            matrix[i][j] = 1
        matrix[i][i] = 1
        matrix[i][n - i - 1] = 1  # зполнение побочной диагонали
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()