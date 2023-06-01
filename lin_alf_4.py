n, k, m = map(int, input().split())
a = list(map(int, input().split()))
z = 0
for j in range(k + 1):
    z += a[j]
for i in range(n - k - 1):
    if z == m:
        print(i + 1)
        break
    z -= a[i]
    z += a[i + k + 1]
else:
    if z == m:
        print(n - k)
    else:
        print(0)
