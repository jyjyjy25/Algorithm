import sys
import heapq as hq

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

hq.heapify(arr)
for _ in range(M):
    x = hq.heappop(arr)
    y = hq.heappop(arr)
    hq.heappush(arr, x + y)
    hq.heappush(arr, x + y)

print(sum(arr))