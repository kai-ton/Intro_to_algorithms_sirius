n, m = map(int, input().split())
a = list(map(int, input().split()))
x = []
p = [0] * (n + 1)
for j in range(m):
    x.append(list(map(int, input().split())))
for i in range(2, n + 1):
    if a[i - 2] < a[i - 1]:
        p[i] = p[i - 1] + 1
    else:
        p[i] = p[i - 1]
for i in range(m):
    print(p[x[i][1]] - p[x[i][0]])
