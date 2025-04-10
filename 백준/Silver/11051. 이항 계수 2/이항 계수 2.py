import sys

N, K = map(int, sys.stdin.readline().split())
dp = []
for i in range(N+1):
    dp.append([1 for _ in range(i+1)])

for i in range(2, N+1):
    for k in range(1, (i)//2+1):
        if k == 1:
            dp[i][k] = dp[i][i-1] = i % 10007
        else:
            dp[i][k] = dp[i][i-k] = (dp[i-1][k] + dp[i-1][k-1]) % 10007

print(dp[N][K])
