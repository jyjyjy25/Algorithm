import sys

N = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 0
standard = stack[-1]
for i in reversed(range(N)):
    if cnt == 0:
        cnt += 1
        continue
    else:
        if standard < stack[i]:
            standard = stack[i]
            cnt += 1

print(cnt)