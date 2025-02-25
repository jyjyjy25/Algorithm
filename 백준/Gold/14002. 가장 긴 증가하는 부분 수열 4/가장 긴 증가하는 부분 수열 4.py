import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [[arr[i]] for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j] and len(dp[j]) + 1 > len(dp[i]):
            dp[i] = dp[j] + [arr[i]]

print(len(max(dp, key=len)))
print(*max(dp, key=len))