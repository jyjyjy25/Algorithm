import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())

def BFS(x):
    queue = deque([(x, 0)])
    visited[x] = True
    
    while queue:
        floor, d = queue.popleft()
        if floor == G:  # 도착층인 경우
            print(d)
            break

        if 1 <= floor + U <= F and not visited[floor+U]:
            queue.append(((floor+U, d+1)))
            visited[floor+U] = True
        if 1 <= floor - D <= F and not visited[floor-D]:
            queue.append(((floor-D, d+1)))
            visited[floor-D] = True
    else:
        print("use the stairs")


visited = [False for _ in range(F+1)]
BFS(S)