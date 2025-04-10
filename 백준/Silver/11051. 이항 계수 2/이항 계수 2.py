import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0] * (N+1) for _ in range(N+1)]
dp[1][0] = 1
dp[1][1] = 1

for i in range(1, N+1):
    for k in range(0, (i)//2+1):
        if k == 0:
            dp[i][i] = dp[i][k] = 1
        elif k == 1:
            dp[i][k] = dp[i][i-1] = i % 10007
        else:
            dp[i][k] = dp[i][i-k] = (dp[i-1][k] + dp[i-1][k-1]) % 10007

print(dp[N][K])
