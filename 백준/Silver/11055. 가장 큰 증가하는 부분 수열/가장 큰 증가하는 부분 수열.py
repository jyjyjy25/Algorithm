import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = arr[i]
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + arr[i], dp[i])

print(max(dp))