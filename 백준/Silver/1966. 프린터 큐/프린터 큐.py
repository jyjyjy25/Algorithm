import sys
from collections import deque

cnt = int(sys.stdin.readline())

for _ in range(cnt):
    N, M = map(int, sys.stdin.readline().split())
    que = list(map(int, sys.stdin.readline().split()))
    queue = deque()
    for i, q in enumerate(que):
        queue.append((i, q))
    
    target = queue[M]
    count = 0
    while(queue):
        q = queue.popleft()

        count += 1
        for i in range(len(queue)):
            if queue[i][1] > q[1]:
                queue.append(q)
                count -= 1
                break
        
        if target not in queue:
            break

    print(count)