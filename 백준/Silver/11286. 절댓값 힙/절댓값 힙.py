import sys
from queue import PriorityQueue

heap = PriorityQueue()

N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap.empty():
            print(0)
        else:
            print(heap.get()[1])
    else:
        heap.put((abs(x), x))