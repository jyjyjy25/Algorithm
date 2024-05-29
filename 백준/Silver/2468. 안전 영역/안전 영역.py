import sys
from collections import deque

N = int(sys.stdin.readline())
# maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
maps = []
max_height = 0
for _ in range(N):
    maps.append(list(map(int, input().split())))
    max_height = max(max_height, max(maps[-1]))


def BFS(i, j, h):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < N and -1 < ny < N:
                if not visited[nx][ny] and maps[nx][ny] > h:
                    visited[nx][ny] = True
                    queue.append((nx, ny))     


# max_height = max(max(maps))
area_cnt = []
for k in range(max_height):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and maps[i][j] > k:
                cnt += 1
                BFS(i, j, k)
                
    area_cnt.append(cnt)

print(max(area_cnt))