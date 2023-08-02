n = int(input())
x = list(map(int, input().split()))
p = 0
c = True
while c:
    c = False
    for j in range(n - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]
            c = True
    p += 1
print(p)
