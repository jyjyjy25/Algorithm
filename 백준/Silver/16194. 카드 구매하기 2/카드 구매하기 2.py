import sys

N = int(sys.stdin.readline())

P = [0] * (N+1)
for i, p in enumerate(sys.stdin.readline().rstrip().split()):
    P[i+1] = int(p)

DP = [10000] * (N+1)
DP[0] = 0

for i in range(1, N+1):
    for j in range(1, i+1):
        DP[i] = min(DP[i], P[j] + DP[i-j])

print(DP[N])
