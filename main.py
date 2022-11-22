n = int(input())
m = int(input())
matrix = [0] * n
for i in range(n):
    matrix[i] = [] * m
s = ''
ls1 = []
for i in range(n):
    s = str(input())
    ls = s.split()
    for j in range(len(ls)):
        ls[j] = int(ls[j])
        matrix[i].append(ls[j])
maxi = matrix[0][0]
x = 0
y = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > maxi:
            maxi = matrix[i][j]
            x = i
            y = j
print(x, y)
