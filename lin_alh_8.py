n, r = map(int, input().split())
p = list(map(int, input().split()))
x = 0
go = True
for i in range(n - 1):
    go = True
    a = i
    while go:
        a += 1
        if a > n - 1:
            break
        if p[a] - p[i] <= r:
            x += 1
        else:
            go = False
print((n * (n - 1) // 2) - x)
