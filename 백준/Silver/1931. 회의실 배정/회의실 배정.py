import sys

N = int(sys.stdin.readline().strip())

A = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    A.append((end, start))

A.sort()

end = -1
cnt = 0
for t in A:
    if t[1] >= end: # 시작 시간과 종료 시간이 같을 수 있으므로 = 필요
        end = t[0]
        cnt += 1

print(cnt)