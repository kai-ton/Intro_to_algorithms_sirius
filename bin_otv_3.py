n, x, y = map(int, input().split())
n -= 1
L = 0
R = n * min(x, y)
while R - L > 1:
    M = (R + L) // 2
    if M // x + M // y < n:
        L = M
    else:
        R = M
print(R + min(x, y))
