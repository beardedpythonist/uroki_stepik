s = str(input())
ls = s.split()
n = int(ls[0])
m = int(ls[1])
matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * m
nm = 0
for q in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                nm += 1
                matrix[i][j] = nm
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()


