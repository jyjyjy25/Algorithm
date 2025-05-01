import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().strip()) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for ax, ay in zip(dx, dy):
            nx = x + ax
            ny = y + ay
            if H > nx >= 0 and W > ny >= 0:
                if not visited[nx][ny] and maps[nx][ny] == "L":
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


answer = 0
for i in range(H):
    for j in range(W):
        if maps[i][j] == "L":
            visited = [[0 for _ in range(W)] for _ in range(H)]
            BFS(i, j, visited)
            answer = max(answer, max(map(max, visited))-1)

print(answer)