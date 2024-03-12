import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    M = int(sys.stdin.readline())
    
    left_heap = [] #최대 힙
    right_heap = [] # 최소 힙
    answer = []

    r = M // 10 + 1
    arr = []
    for _ in range(r):
        temp = list(map(int, sys.stdin.readline().split()))
        for t in temp:
            arr.append(t)

    for i, a in enumerate(arr):
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -a)
        else:
            heapq.heappush(right_heap, a)
        
        if left_heap and right_heap and -left_heap[0] > right_heap[0]:
            large = heapq.heappop(left_heap)
            small = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -small)
            heapq.heappush(right_heap, -large)
        
        if i % 2 == 0:
            answer.append(-left_heap[0])
    
    print(len(answer))
    for i, ans in enumerate(answer):
        if i % 10 == 0 and i > 1:
            print()
        print(ans, end=' ')
        
        if i == len(answer)-1:
            print()