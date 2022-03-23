n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
iterr, iterr2 = 0, 0
maxx = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > maxx:
            maxx = a[i][j]
            iterr, iterr2 = i, j
print(iterr, iterr2)
