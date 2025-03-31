import sys

N, d, k, c = map(int, sys.stdin.readline().split())
sushi = [int(sys.stdin.readline()) for _ in range(N)]

max_value = 0
for i in range(0, N):
    if i <= N-k:
        case = set(sushi[i:i+k] + [c])
    else:
        case = set(sushi[i:] + sushi[:(i+k)%N] + [c])
    max_value = max(max_value, len(case))

print(max_value)
