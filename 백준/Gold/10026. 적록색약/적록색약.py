import sys
from collections import deque

N = int(sys.stdin.readline())
maps = []
for _ in range(N):
    line = sys.stdin.readline().strip()
    maps.append([l for l in line])


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def BFS_normal(x, y, color):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for ax, ay in zip(dx, dy):
            nx = x + ax
            ny = y + ay
            if N > nx >= 0 and N > ny >= 0:
                if not visited[nx][ny] and color == maps[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


def BFS_abnormal(x, y, color):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for ax, ay in zip(dx, dy):
            nx = x + ax
            ny = y + ay
            if N > nx >= 0 and N > ny >= 0:
                if not visited[nx][ny]:
                    if (color == "R" or color == "G") and (maps[nx][ny] == "R" or maps[nx][ny] == "G"):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                    elif color == "B" and maps[nx][ny] == "B":
                        visited[nx][ny] = True
                        queue.append((nx, ny))


normal_cnt = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            normal_cnt += 1
            BFS_normal(i, j, maps[i][j])

abnormal_cnt = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            abnormal_cnt += 1
            BFS_abnormal(i, j, maps[i][j])

print(normal_cnt, abnormal_cnt)
