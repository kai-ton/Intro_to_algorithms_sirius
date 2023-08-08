def razl(x):
    st = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            st.add(i)
            st.add(x // i)
    st = sorted(list(st))
    return st


def dil(s):
    p = 2
    sp = set()
    while s > 1:
        if s % p == 0:
            sp.add(p)
            s = s // p
        else:
            p += 1
    return sp


n = int(input())
z = razl(n)
# print(len(z))
sd = []
chot = 0
for i in z:
    sd.append([i, dil(i)])
# print(sd)
for i in range(len(z) - 1):
    for j in range(i + 1, len(z)):
        if z[i] * z[j] > n:
            break
        if sd[i][1] & sd[j][1] == set():
            chot += 1
print(chot)
