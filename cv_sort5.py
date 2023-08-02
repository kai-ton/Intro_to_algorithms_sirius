n = int(input())
x = list(map(int, input().split()))
p = 0
for i in range(n):
    for j in range(n - i - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]
            p += 1
print(p)
