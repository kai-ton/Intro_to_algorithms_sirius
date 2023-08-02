col = int(input())
x = list(map(int, input().split()))
b = int(input())
a = list(map(int, input().split()))
for i in range(b):
    x[a[i] - 1] -= 1
for i in range(col):
    if x[i] < 0:
        print('yes')
    else:
        print('no')
