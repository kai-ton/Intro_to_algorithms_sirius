c, n = map(int, input().split())
z = {}
x = [0 for i in range(c)]
for i in range(n):
    m = input().split()
    z[m[1]] = int(m[0])
for key, val in z.items():
    x[val - 1] += 1
print(*x)
