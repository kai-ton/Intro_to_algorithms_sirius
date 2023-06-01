x, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ibest = 0
jbest = 1
imin = 0
if x > 1:
    for j in range(2, len(a)):
        if a[j - 1] < a[imin]:
            imin = j - 1
        if k // a[imin] * b[j] + k % a[imin] > k // a[ibest] * b[jbest] + k % a[ibest]:
            jbest = j
            ibest = imin
    if k // a[ibest] * b[jbest] + k % a[ibest] > k:
        print(k // a[ibest] * b[jbest] + k % a[ibest])
        print(ibest + 1, jbest + 1)
    else:
        print(k)
        print('-1 -1')
else:
    print(k)
    print('-1 -1')
