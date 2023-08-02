w, h, n = map(int, input().split())
L = 0
R = n * max(w, h)
while R - L > 1:
    M = (R + L) // 2
    if (M // w) * (M // h) < n:
        L = M
    else:
        R = M
print(R)
