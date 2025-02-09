import sys
sys.setrecursionlimit(10**6)


def DFS(y, x):
    visited[y][x] = True

    for ax, ay in zip(dx, dy):
        nx = x + ax
        ny = y + ay
        if w > nx >= 0 and h > ny >= 0:
            if maps[ny][nx] == 1 and not visited[ny][nx]:
                DFS(ny, nx)


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    maps = []
    for _ in range(h):
        maps.append(list(map(int, sys.stdin.readline().split())))
    
    dx = [0, 0, -1, 1, 1, 1, -1, -1]  # 상하좌우 + 대각선
    dy = [1, -1, 0, 0, 1, -1, 1, -1]

    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and not visited[i][j]:
                cnt += 1
                DFS(i, j)

    print(cnt)
