m = int(input())
x = list(map(int, input().split()))
n = int(input())
L = 0
R = max(x)
b = 0
while R - L > 1:
    M = (R + L) // 2
    b = 0
    for i in range(m):
        b += (x[i] + M - 1) // M
    if n < b:
        L = M
    else:
        R = M
print(R)
