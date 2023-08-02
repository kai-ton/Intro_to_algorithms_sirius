n = int(input())
for i in range(1, int(n**0.5)):
    if n % (i + 1) == 0:
        print(i + 1)
        break
else:
    print(n)
