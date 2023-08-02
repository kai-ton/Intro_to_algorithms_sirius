x = {}
n = int(input())
for _ in range(n):
    n = input().split()
    if 'DEPOSIT' in n:
        x[n[1]] = x.get(n[1], 0) + int(n[2])
    elif 'WITHDRAW' in n:
        x[n[1]] = x.get(n[1], 0) - int(n[2])
    elif 'BALANCE' in n:
        if n[1] in x:
            print(x[n[1]])
        else:
            print('ERROR')
    elif 'TRANSFER' in n:
        x[n[1]] = x.get(n[1], 0) - int(n[3])
        x[n[2]] = x.get(n[2], 0) + int(n[3])
    else:
        for key, val in x.items():
            if val > 0:
                x[key] += val * int(n[1]) // 100
