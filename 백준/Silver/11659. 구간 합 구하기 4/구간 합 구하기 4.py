import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

S = [0]
for i in range(N):
    S.append(S[i] + A[i])

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(S[e]-S[s-1])