n, k = map(int, input().split())
x = list(map(int, input().split()))
for i in range(k):
    d = 0
    m = 0
    for j in range(i, n):
        if x[j] > d:
            d = x[j]
            m = j
    x[m], x[i] = x[i], d
print(x[k - 1])
