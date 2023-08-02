n = int(input())
a = list(map(int, input().split()))
a.sort()
x = []
for i in range(n - 1):
    x.append(a[i + 1] - a[i])
dp = [[0, 0] for _ in range(n - 1)]
dp[0][0] = x[0]
dp[0][1] = x[0]
for i in range(1, n - 1):
    dp[i][0] = dp[i - 1][1] + x[i]
    dp[i][1] = min(dp[i - 1][0] + 0, dp[i - 1][1] + x[i])
print(dp[-1][0])
