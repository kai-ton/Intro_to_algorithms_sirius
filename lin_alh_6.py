n = int(input())
a = list(map(int, input().split()))
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i - 1]
ibest = 0
jbest = -999999
imin0 = 0
imin1 = -1
imin2 = -1
for j in range(1, n + 1):
    if p[j] % 3 == 0 and j - imin0 > jbest - ibest:
        ibest = imin0
        jbest = j
    if imin1 == -1 and p[j] % 3 == 1:
        imin1 = j
    elif imin1 != -1 and p[j] % 3 == 1 and j - imin1 > jbest - ibest:
        ibest = imin1
        jbest = j
    if imin2 == -1 and p[j] % 3 == 2:
        imin2 = j
    elif imin2 != -1 and p[j] % 3 == 2 and j - imin2 > jbest - ibest:
        ibest = imin2
        jbest = j
if jbest == -999999:
    print(-1)
else:
    print(ibest + 1, jbest)
