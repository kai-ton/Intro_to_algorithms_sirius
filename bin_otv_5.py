N_monsters = int(input())
xps = list(map(int, input().split()))
N_attacks = int(input())
if N_attacks >= N_monsters:
    L = 1
    R = max(xps)
    while R - L > 1:
        M = (R + L) // 2
        shot = 0
        for i in range(N_monsters):
            shot += (xps[i] + M - 1) // M
        if shot > N_attacks:
            L = M
        else:
            R = M
    print(R)
else:
    print(-1)
