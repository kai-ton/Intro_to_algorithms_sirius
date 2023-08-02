from bisect import *
n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
y = list(map(int, input().split()))
for i in range(m):
    # if 0 not in x and y[i] == 0:
    #     print('NO')
    if x[bisect(x, y[i]) - 1] == y[i]:
        print('YES')
    else:
        print('NO')
