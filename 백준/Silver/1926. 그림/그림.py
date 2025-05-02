import sys
from collections import deque

# 방향벡터(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y):
    size = 1  # 그림 크기

    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for ax, ay in zip(dx, dy):
            nx = x + ax
            ny = y + ay
            if N > nx >= 0 and M > ny >= 0:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = 1
                    size += 1
                    queue.append((nx, ny))
    return size

N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

painting_cnt = 0  # 그림의 수
painting_size = 0  # 그림 크기
for i in range(N):
    for j in range(M):
        if not visited[i][j] and maps[i][j] == 1:
            painting_cnt += 1
            size = BFS(i, j)
            painting_size = max(painting_size, size)

print(painting_cnt)
print(painting_size)