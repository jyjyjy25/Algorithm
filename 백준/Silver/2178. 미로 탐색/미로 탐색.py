import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

A = [[]]
visited = [[False] * (M+1) for _ in range(N+1)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().strip()))
    temp.insert(0, 0)
    A.append(temp)


def BFS(v, w):
    queue = deque()
    queue.append((v, w))
    visited[v][w] = True
    while queue:
        node = queue.popleft()
        for k in range(4):
            nx = node[0] + dx[k]
            ny = node[1] + dy[k]
            if N >= nx > 0 and M >= ny > 0:
                if not visited[nx][ny] and A[nx][ny] == 1:
                    visited[nx][ny] = True
                    A[nx][ny] = A[node[0]][node[1]] + 1
                    queue.append((nx, ny))


BFS(1, 1)
print(A[N][M])