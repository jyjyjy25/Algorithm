import sys
import math

N = int(sys.stdin.readline())

dp = [100000] * (N+1)
dp[0] = 0
dp[1] = 1

for i in range(1, N+1):
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i], 1+ dp[i - j*j])

print(dp[N])