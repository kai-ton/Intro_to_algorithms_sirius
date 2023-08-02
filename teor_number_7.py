def NOD(a, b):
    if b == 0:
        return a
    return NOD(b, a % b)


c, d = map(int, input().split())


print(c // NOD(c, d), d // NOD(c, d))
