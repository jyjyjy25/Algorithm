import sys

N = int(sys.stdin.readline())
arr = [0]
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

DP = [0 for _ in range(N+1)]
DP[1] = arr[1]

if N == 1:
    print(DP[1])
else:
    DP[2] = arr[1] + arr[2]
    for i in range(3, N+1):
        DP[i] = max(DP[i-3] + arr[i-1] + arr[i], DP[i-2] + arr[i], DP[i-1])

    print(DP[N])