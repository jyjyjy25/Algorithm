import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

A = [[]]
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().strip()))
    temp.insert(0, 0)
    A.append(temp)

visited = []
for _ in range(N+1):
    temp = [False] * (M+1)
    visited.append(temp)


def BFS(v, w):
    queue = deque()
    queue.append((v, w))
    visited[v][w] = True
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]

        if N >= x + 1 and x + 1 > 0 and M >= y and y > 0: # 우
            if not visited[x+1][y] and A[x+1][y] == 1:
                queue.append((x+1, y))
                visited[x+1][y] = True
                A[x+1][y] = A[x][y] + 1
        if N >= x - 1 and x - 1 > 0 and M >= y and y > 0: # 좌
            if not visited[x-1][y] and A[x-1][y] == 1:
                queue.append((x-1, y))
                visited[x-1][y] = True
                A[x-1][y] = A[x][y] + 1
        if N >= x and x > 0 and M >= y - 1 and y - 1 > 0: # 하
            if not visited[x][y-1] and A[x][y-1] == 1:
                queue.append((x, y-1))
                visited[x][y-1] = True
                A[x][y-1] = A[x][y] + 1
        if N >= x and x > 0 and M >= y + 1 and y + 1 > 0: # 상
            if not visited[x][y+1] and A[x][y+1] == 1:
                queue.append((x, y+1))
                visited[x][y+1] = True
                A[x][y+1] = A[x][y] + 1


BFS(1, 1)
print(A[N][M])