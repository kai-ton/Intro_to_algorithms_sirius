x, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ibest = 0
jbest = 1 + k
imax = 0
for j in range(2, x):
    if a[j - 1] > a[imax]:
        imax = j - 1
    if j < x - k and a[j + k] + a[imax] > a[jbest] + a[ibest]:
        jbest = j + k
        ibest = imax
print(ibest + 1, jbest + 1)
