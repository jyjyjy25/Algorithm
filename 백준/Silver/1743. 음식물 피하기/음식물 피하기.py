import sys
sys.setrecursionlimit(10**5)

N, M, K = map(int, sys.stdin.readline().split())

visited = [[False for _ in range(M)] for _ in range(N)]
maps = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    maps[r-1][c-1] = 1


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    global size

    visited[x][y] = True
    size += 1
    for ax, ay in zip(dx, dy):
        nx = x + ax
        ny = y + ay
        if N > nx >= 0 and M > ny >= 0:
            if not visited[nx][ny] and maps[nx][ny] == 1:
                DFS(nx, ny)


max_size = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and maps[i][j] == 1:
            size = 0
            DFS(i, j)
            max_size = max(max_size, size)

print(max_size)