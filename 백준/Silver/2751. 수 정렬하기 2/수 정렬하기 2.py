import sys

num = []
N = int(input())

for _ in range(N):
    x = int(sys.stdin.readline())
    num.append(x)

num.sort()

for k in range(N):
    print(num[k])
