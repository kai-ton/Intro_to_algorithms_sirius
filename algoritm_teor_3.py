n = int(input())
x = set()
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        x.add(i)
        x.add(n // i)
print(len(x), sum(x))
