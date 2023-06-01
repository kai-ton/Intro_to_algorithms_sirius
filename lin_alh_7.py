n = int(input())
p = [0]
ibest = 0
jbest = 1
imin = 1
p.append(int(input()))
for i in range(2, n + 1):
    # print(ibest, jbest, imin)
    p.append(p[i - 1] + int(input()))
    if p[i] <= p[imin]:
        imin = i
    if p[i] - p[imin] > p[jbest] - p[ibest]:
        ibest = imin
        jbest = i
# print(ibest, jbest, imin)
print(ibest + 1)
print(jbest)


'''p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i - 1]
isp = []
jsp = []
ibest = 0
jbest = 0
imin = 0
for j in range(1, n + 1):
    if p[j] < p[imin]:
        imin = j
    if p[j] - p[imin] > p[jbest] - p[ibest]:
        jbest = j
        ibest = imin
    else:
        if p[j] == p[ibest]:
            isp.append(j)
        if p[j] == p[jbest]:
            jsp.append(j)'''
