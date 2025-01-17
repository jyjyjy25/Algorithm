import sys
from collections import deque


def BFS(v):
    queue = deque([v])

    while queue:
        ay, ax = queue.popleft()
        
        for nx, ny in zip(dx, dy):
            x = ax + nx
            y = ay + ny
            if M > x > -1 and N > y > -1:
                if maps[y][x] == 1 and not visited[y][x]:
                    visited[y][x] = True
                    queue.append((y, x))


dx = [0, 0, -1, +1]  # 상하좌우
dy = [+1, -1, 0, 0]

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())  # x, y, 개수

    maps = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())  # (X, Y)
        maps[b][a] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1 and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                BFS((i, j))  # (y, x)

    print(cnt)
