import sys
import heapq

N = int(sys.stdin.readline())

leftHeap = [] # 최대 힙
rightHeap = [] # 최소 힙
for _ in range(N):
    x = int(sys.stdin.readline())
    
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -x)
    else:
        heapq.heappush(rightHeap, x)

    if rightHeap and leftHeap and -leftHeap[0] > rightHeap[0]:
        large = heapq.heappop(leftHeap)
        small = heapq.heappop(rightHeap)
        
        heapq.heappush(leftHeap, -small)
        heapq.heappush(rightHeap, -large)
    
    print(-leftHeap[0])