'''999999937 999999929'''


'''def eil(m, a):
    x = 0
    for i in range(m):
        if i * a % m == 1:
            print(i)
            break
    else:
        print(-1)


m, a = map(int, input().split())
eil(m, a)'''


'''def asd(m, a):
    if a == 1:
        return -1
    else:
        for i in range(2, a + 1):
            if a % i == 0 and m % i == 0:
                return -1
        else:
            return a ** (eil(m) - 1) % m'''


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


def razl(x):
    st = set()
    st.add(x)
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            st.add(i)
            st.add(x // i)
    return st


def pow(a, b):
    # print('-')
    if b == 0:
        return 1
    if b % 2 == 1:
        return pow(a, b - 1) * a % m
    return pow(a * a % m, b // 2) % m


def asd(m, a):
    if a == 1:
        return -1
    else:
        # print(razl(m), razl(a))
        if (razl(m) & razl(a)) != set():
            return -1
        else:
            return pow(a, eil(m) - 1)


m, a = map(int, input().split())
print(asd(m, a))
