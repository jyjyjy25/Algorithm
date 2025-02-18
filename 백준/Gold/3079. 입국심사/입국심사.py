import sys

N, M = map(int, sys.stdin.readline().split())
times = [int(sys.stdin.readline()) for _ in range(N)]

low = 0
high = max(times) * M

while (low <= high):
    mid = (low + high) // 2  # 걸리는 시간

    cnt = 0
    for time in times:
        cnt += mid // time
    
    if cnt < M:
        low = mid + 1
    elif cnt >= N:
        high = mid - 1

print(low)
