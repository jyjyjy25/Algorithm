import sys
from collections import deque

def is_all_melt():
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0:
                return False
    return True

def BFS(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for ax, ay in zip(dx, dy):
            nx = x + ax
            ny = y + ay
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny]:
                if maps[nx][ny] != 0:  # 인접한 칸이 육지이면
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                else:  # 인접한 칸이 바다이면
                    if maps[x][y] > 0:
                        maps[x][y] -= 1  # 빙산의 높이 1 감소


N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
years = 0

status = ""
while True:
    pieces = 0  # 빙산 덩어리 개수
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and maps[i][j] != 0:
                pieces += 1  # 빙산 덩어리 1 증가
                BFS(i, j, visited)
    years += 1

    if pieces >= 2:  # 빙산이 두 덩어리 이상으로 분리되었으면
        status = "SEPERATE"
        break
    
    if is_all_melt():  # 빙산이 모두 녹았다면
        status = "MELT"
        break

if status == "SEPERATE":
    print(years-1)
elif status == "MELT":
    print(0)
