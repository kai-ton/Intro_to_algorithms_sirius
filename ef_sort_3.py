x = int(input())
a = [i**2 for i in range(1, x + 1)]
b = [i**3 for i in range(1, x + 1)]
i = 0
j = 0
v = 0
# z = 0
for _ in range(x):
    if a[i] < b[j]:
        v = a[i]
        i += 1
        # z = 1
    elif a[i] > b[j]:
        v = b[j]
        j += 1
        # z = 2
    else:
        v = a[i]
        i += 1
        j += 1
        # z = 3
    # print(i, z)
print(v)
# print(a)
# print(b)