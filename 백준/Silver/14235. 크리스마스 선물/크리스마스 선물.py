import sys
import heapq

N = int(sys.stdin.readline())

present = []
for _ in range(N):
    A = sys.stdin.readline().rstrip()
    if A == '0':
        if len(present) == 0:
            print(-1)
        else:
            print(-heapq.heappop(present))
    else:  
        A = list(map(int, A.split()))
        for i in range(1, len(A)):
            heapq.heappush(present, -A[i])

