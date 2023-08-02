n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    x[i] = [sum(map(int, list(str(x[i])))), -i, x[i]]
x.sort(reverse=True)
for i in range(n):
    print(x[i][2], end=' ')
