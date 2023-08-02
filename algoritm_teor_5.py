def ghj(n):
    p = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            p[d] = p.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        p[n] = 1
    e = 0
    for keys, vals in p.items():
        if e == 1:
            print('*', end='')
        e = 1
        if vals == 1:
            print(keys, end='')
        else:
            print(keys, '^', vals, sep='', end='')


ghj(int(input()))
