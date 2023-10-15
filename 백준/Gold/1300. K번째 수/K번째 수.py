import sys

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())

start = 1
end = K
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for n in range(1, N+1):
        cnt += min(mid // n, N)

    if cnt < K:
        start = mid + 1
    elif cnt >= K:
        end = mid - 1

print(start)
