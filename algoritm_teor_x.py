def eil(n):
    ri = n
    p = 2
    while p**2 <= n:
        if n % p == 0:
            ri -= ri // p
        while n % p == 0:
            n //= p
        p += 1
    if n > 1:
        ri -= ri // n
    return ri


print(eil(int(input())))
