n = int(input())
x = sorted(list(map(int, input().split())))
m = int(input())
y = list(map(int, input().split()))
# L = -1
# R = n
for i in range(m):
    L = -1
    R = n
    while R - L > 1:
        M = (R + L) // 2
        if x[M] < y[i]:
            L = M
        else:
            R = M
    print(R, end=' ')

