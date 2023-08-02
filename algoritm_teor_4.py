n = int(input())
m = 0
x = [i for i in range(1, 1299710)]
for i in range(2, 1299710):
    if x[i - 1] != 0:
        m += 1
        if m == n:
            print(i)
            break
        for j in range(i + i - 1, 1299709, i):
            x[j] = 0
