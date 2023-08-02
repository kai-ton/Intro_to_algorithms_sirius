n = int(input())
x = [0] * (n + 3)
x[n] = 1
for i in range(n - 1, -1, -1):
    x[i] = x[i + 1] + x[i + 2] + x[i + 3]
print(x[0])
