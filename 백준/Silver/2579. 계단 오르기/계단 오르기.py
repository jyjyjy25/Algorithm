import sys

N = int(sys.stdin.readline())
stairs = [0] * 301

for i in range(1, N+1):
    stairs[i] = int(sys.stdin.readline())

DP = [0] * 301
DP[1] = stairs[1]
DP[2] = stairs[1] + stairs[2]
DP[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, N+1):
    DP[i] = max(DP[i-3] + stairs[i-1] + stairs[i], DP[i-2] + stairs[i])

print(DP[N])