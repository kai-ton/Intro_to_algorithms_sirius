a = float(input())
n = int(input())
L = 0
R = 1000
for _ in range(25):
    M = (R + L) / 2
    sum = 1
    for _ in range(n):
        sum *= M
    if sum < a:
        L = M
    else:
        R = M
print(R)
