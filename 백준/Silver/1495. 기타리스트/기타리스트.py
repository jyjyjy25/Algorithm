import sys

N, S, M = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))

dp = [[False] * (M+1) for _ in range(N+1)]
dp[0][S] = True

answer = -1
for i in range(N):
    for j in range(M+1):
        if dp[i][j]:
            if j + V[i] <= M:
                dp[i+1][j+V[i]] = True
            if j - V[i] >= 0:
                dp[i+1][j-V[i]] = True

for i in range(M, -1, -1):
    if dp[N][i]:
        answer = i
        break

print(answer)