

n = int(input())
matrix = [0] * n

for i in range(n):
    matrix[i] = [] * n
s = ''
for i in range(n):
    s = str(input())
    ls = s.split()
    for j in range(len(ls)):
        ls[j] = int(ls[j])
        matrix[i].append(ls[j])
summa = 0
count = 0
sred = int
for i in range(n):
    summa = sum(matrix[i])
    sred = summa / n
    for j in range(n):
        if matrix[i][j] > sred:
            count += 1
    print(count)
    count = 0

# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=' ')
#     print()
