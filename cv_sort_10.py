n = int(input())
x = []
for i in range(n):
    x.append(list(map(int, input().split())))
for i in range(n):
    d = [999999, 0]
    b = 0
    for j in range(i, n):
        if (x[j][1] == d[1] and x[j][0] < d[0]) or x[j][1] > d[1]:
            d = x[j]
            b = j
    x[i], x[b] = x[b], x[i]
for i in range(n):
    print(*x[i])
