def asd(a, b):
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


def cort(a):
    if len(a) <= 1:
        return a
    k = len(a) // 2
    return asd(cort(a[:k]), cort(a[k:]))


sd = int(input())
x = list(map(int, input().split()))
print(*cort(x))
