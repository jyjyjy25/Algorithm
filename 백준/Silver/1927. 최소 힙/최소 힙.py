import sys
import heapq as hq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        hq.heappush(heap, x)
    elif x == 0 and heap:
        print(hq.heappop(heap))
    elif x == 0 and not heap:
        print(0)
