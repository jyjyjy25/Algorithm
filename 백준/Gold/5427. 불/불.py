import sys
from collections import deque


def BFS():
    # 방향벡터(상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while True:
        # 상근이 탈출
        for _ in range(len(queue_escape)):
            x, y = queue_escape.popleft()
            if maps[x][y] == "*":  # 불이 번진 경우
                continue
            for ax, ay in zip(dx, dy):
                nx = x + ax
                ny = y + ay
                if h > nx >= 0 and w > ny >= 0:
                    if not visited_escape[nx][ny] and maps[nx][ny] == ".":  # 빈 공간인 경우
                        maps[nx][ny] = maps[x][y] + 1
                        queue_escape.append((nx, ny))
                        visited_escape[nx][ny] = True
                else:
                    return maps[x][y] + 1

        if not queue_escape:  # 탈출 조건: 상근이가 탈출한 경우
            return "IMPOSSIBLE"

        # 불 확장
        for _ in range(len(queue_fire)):
            x, y = queue_fire.popleft()
            for ax, ay in zip(dx, dy):
                nx = x + ax
                ny = y + ay
                if h > nx >= 0 and w > ny >= 0:
                    if not visited_fire[nx][ny] and maps[nx][ny] != "#":  # 벽이 아닌 경우
                        maps[nx][ny] = "*"
                        queue_fire.append((nx, ny))
                        visited_fire[nx][ny] = True


T = int(sys.stdin.readline())
for _ in range(T):
    w, h = map(int, sys.stdin.readline().split())
    maps = [list(sys.stdin.readline().strip()) for _ in range(h)]

    queue_fire = deque([])
    queue_escape = deque([])
    visited_fire = [[False for _ in range(w)] for _ in range(h)]
    visited_escape = [[False for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] == "@":  # 상근이 위치
                queue_escape.append((i, j))
                maps[i][j] = 0
                visited_escape[i][j] = True
            elif maps[i][j] == "*":  # 불 위치
                queue_fire.append((i, j))
                visited_fire[i][j] = True

    print(BFS())