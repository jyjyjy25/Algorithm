import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

s = [0]
for i, n in enumerate(num_list):
    s.append(s[i] + n)

for i in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(s[j] - s[i-1])