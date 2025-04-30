import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def DFS(x, y, flag):
    global cnt

    visited[x][y] = True
    cnt += 1
    for ax, ay in zip(dx, dy):
        nx = x + ax
        ny = y + ay
        if M > nx >= 0 and N > ny >= 0:
            if not visited[nx][ny] and maps[nx][ny] == flag:
                DFS(nx, ny, flag)


N, M = map(int, sys.stdin.readline().split(" "))

maps = [list(sys.stdin.readline().strip()) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

W, B = 0, 0
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            cnt = 0
            DFS(i, j, maps[i][j])
            if maps[i][j] == "W":
                W += cnt ** 2
            else:
                B += cnt ** 2

print(W, B)