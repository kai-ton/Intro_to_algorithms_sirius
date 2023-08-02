x = list(input())
a = [0] * 10
for i in range(len(x)):
    if x[i] == '0':
        a[0] += 1
    elif x[i] == '1':
        a[1] += 1
    elif x[i] == '2':
        a[2] += 1
    elif x[i] == '3':
        a[3] += 1
    elif x[i] == '4':
        a[4] += 1
    elif x[i] == '5':
        a[5] += 1
    elif x[i] == '6':
        a[6] += 1
    elif x[i] == '7':
        a[7] += 1
    elif x[i] == '8':
        a[8] += 1
    elif x[i] == '9':
        a[9] += 1
if a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] + a[9] == 0:
    print(-1)
elif a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] + a[9] == 0:
    print(0)
else:
    for i in range(10):
        for j in range(a[9 - i]):
            print(9 - i, end='')
