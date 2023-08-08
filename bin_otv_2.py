g = int(input())
s = list(map(int, input().split()))
t = int(input())
L = max(s) - 1
R = sum(s)
while R - L > 1:
    M = (R + L) // 2
    su = 0
    shot = 1
    i = 0
    while i < g:
        if su + s[i] <= M:
            su += s[i]
            i += 1
        else:

            su = 0
            shot += 1
    if shot > t:
        L = M
    else:
        R = M
print(R)
'''
6
1 5 6 3 1 2
3
'''