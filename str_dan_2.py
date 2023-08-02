n = list(input())
x = set()
for i in range(len(n)):
    if n[i] not in x:
        print(n[i], end='')
        x.add(n[i])
