import sys

N = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 0
standard = 0
for s in reversed(stack):
    if s > standard:
        standard = s
        cnt += 1

print(cnt)