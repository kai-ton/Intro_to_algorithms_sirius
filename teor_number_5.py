def power(b, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(b, n/2)**2 % p
    else:
        return b*power(b, n-1) % p


t = int(input())
for i in range(t):
    p, a = map(int, input().split())
    print(power(a, p - 2))
