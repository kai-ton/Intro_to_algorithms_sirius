n = int(input())
x = [0] * (n + 1)
for i in range(2, n + 1):
    if i % 2 == 0:
        if i % 3 == 0:
            x[i] = min(x[i - 1], x[i // 2], x[i // 3]) + 1
        else:
            x[i] = min(x[i - 1], x[i // 2]) + 1
    else:
        if i % 3 == 0:
            x[i] = min(x[i - 1], x[i // 3]) + 1
        else:
            x[i] = x[i - 1] + 1
print(x[n])
