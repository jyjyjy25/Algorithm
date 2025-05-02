import sys
from collections import deque

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [1, 0, -1, 1, 0, -1, 1, -1]

def BFS(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        # print(queue)
        x, y = queue.popleft()
        for ax, ay in zip(dx, dy):
            nx = x + ax
            ny = y + ay
            if N > nx >= 0 and M > ny >= 0:
                # print(nx, ny)
                if visited[nx][ny] == -1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                else:
                    continue


N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[-1 for _ in range(M)] for _ in range(N)]
sharks = []  # 상어의 위치
for i in range(N):
    for j in range(M):
        if maps[i][j]:
            sharks.append([i, j])

for x, y in sharks:
    BFS(x, y)

print(max(list(map(max, visited))))