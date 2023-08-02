n = int(input())
x = [0] + list(map(int, input().split()))
for i in range(2, n + 1):
    x[i] = max(x[i - 1], x[i - 2]) + x[i]
print(x[n])
