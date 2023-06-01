n = int(input())
a = list(map(int, input().split()))
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i - 1]
print(*p)
ibest = 0
jbest = 0
imin0 = 0
imin1 = 0
imin2 = 0
for j in range(1, n + 1):
    print(p[j], imin0, imin1, imin2, ibest, jbest)

    if p[j] % 3 == 0:
        if p[j] < p[imin0] or imin0 == 0:
            imin0 = j
    elif p[j] % 3 == 1:
        if p[j] < p[imin1] or imin1 == 0:
            imin1 = j
    else:
        if p[j] < p[imin2] or imin2 == 0:
            imin2 = j

    if (p[j] - p[imin0]) % 3 == 0 and (p[j] - p[imin0] > p[jbest] - p[ibest] or ibest == 0 and jbest == 0):
        jbest = j
        ibest = imin0
    if (p[j] - p[imin1]) % 3 == 0 and (p[j] - p[imin1] > p[jbest] - p[ibest] or ibest == 0 and jbest == 0):
        jbest = j
        ibest = imin1
    if (p[j] - p[imin2]) % 3 == 0 and (p[j] - p[imin2] > p[jbest] - p[ibest] or ibest == 0 and jbest == 0):
        jbest = j
        ibest = imin2
print(p[j], imin0, imin1, imin2, ibest, jbest)
if jbest == 0:
    print(-1)
else:
    print(ibest + 1, jbest)
# print(ibest + 1, jbest)
