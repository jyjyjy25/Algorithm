import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
maps = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def BFS():
    while queue:
        z, x, y = queue.popleft()
        for ax, ay, az in zip(dx, dy, dz):
            nx = x + ax
            ny = y + ay
            nz = z + az
            if N > nx >= 0 and M > ny >= 0 and H > nz >= 0:
                if maps[nz][nx][ny] == 0:
                    queue.append((nz, nx, ny))
                    maps[nz][nx][ny] = maps[z][x][y] + 1


# 익은 토마토들의 좌표 구하기
queue = deque([])
for h in range(H):
    for n in range(N):
        for m in range(M):
            if maps[h][n][m] == 1:
                queue.append((h, n, m))

BFS()

flag = True  # 토마토가 모두 익었는지 여부
for h in range(H):
    for n in range(N):
        if 0 in maps[h][n]:
            flag = False
            break

if flag:
    days = 0
    for h in range(H):
        for n in range(N):
            days = max(days, max(maps[h][n]))
    print(days - 1)
else:
    print(-1)