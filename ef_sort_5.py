n = int(input())
z = list(map(int, input().split()))
z.sort()
m = int(input())
x = list(map(int, input().split()))
x.sort()
za = set()
xa = set()
for i in range(n):
    za.add(z[i])
for i in range(m):
    xa.add(x[i])
if za == xa:
    print('YES')
else:
    print('NO')
