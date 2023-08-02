n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
y = list(map(int, input().split()))
for i in range(m):
    L = -1
    R = n
    while R - L > 1:
        M = (R + L) // 2
        if x[M] <= y[i]:
            L = M
        else:
            R = M
    if L == -1:
        L = 0
    if R == n:
        R = n - 1
    if R < n and x[R] == y[i]:
        print(y[i])
    else:
        if abs(x[R] - y[i]) < abs(x[L] - y[i]):
            print(x[R])
        else:
            print(x[L])
