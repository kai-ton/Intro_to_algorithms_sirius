def NOD(a, b):
    if b == 0:
        return a
    return NOD(b, a % b)


c, d = map(int, input().split())
print(c * d // NOD(c, d))
