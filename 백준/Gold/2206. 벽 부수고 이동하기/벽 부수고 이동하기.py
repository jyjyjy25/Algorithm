import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


def BFS(x, y, c):
    queue = deque([(x, y, c)])
    visited[x][y][c] = 1

    while queue:
        x, y, c = queue.popleft()

        # 목적지에 도달하였다면 return
        if x == N - 1 and y == M - 1:
            return visited[x][y][c]

        for ax, ay in zip(dx, dy):
            nx = x + ax
            ny = y + ay
            if N > nx >= 0 and M > ny >= 0:
                if maps[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
                elif maps[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    queue.append((nx, ny, c))

    return -1


print(BFS(0, 0, 0))