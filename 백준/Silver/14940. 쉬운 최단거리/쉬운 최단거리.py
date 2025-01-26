import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maps = []
goal_x, goal_y = 0, 0

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    maps.append(arr)

    for j, a in enumerate(arr):
        if a == 2:
            goal_x, goal_y = i, j
            break


dx = [0, 0, -1, +1]
dy = [+1, -1, 0, 0]
visited = [[False] * M for _ in range(N)]


def BFS(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    maps[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for ax, ay in zip(dx, dy):
            nx = x + ax
            ny = y + ay
            if (N > nx and nx >= 0) and (M > ny and ny >= 0):
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1


BFS(goal_x, goal_y)

for i in range(N):
    for j in range(M):
        if not visited[i][j] and maps[i][j] == 1:
            print(-1, end=" ")
        else:
            print(maps[i][j], end=" ")
    print()
