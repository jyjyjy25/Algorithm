import sys

N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
moves = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]


def move_clouds(clouds, d, s):
    new_clouds = []
    
    for r, c in clouds:
        nx = (r + dx[d] * s) % N
        ny = (c + dy[d] * s) % N
        new_clouds.append((nx, ny))
    
    return new_clouds


for move in moves:
    d, s = move
    new_clouds = move_clouds(clouds, d, s)  # 1. 모든 구름이 di 방향으로 si칸 이동
    visited = [[False for _ in range(N)] for _ in range(N)]

    for nr, nc in new_clouds:  # 2. 비가 내려 각 칸의 바구니에 물 1씩 증가
        maps[nr][nc] += 1
        visited[nr][nc] = True
    
    for nr, nc in new_clouds:  # 4. 물복사마법
        for i in range(2, len(dx), 2):
            nx = nr + dx[i]
            ny = nc + dy[i]
            if -1 < nx < N and -1 < ny < N and maps[nx][ny]:
                maps[nr][nc] += 1

    clouds = []
    for i in range(N):  # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다
        for j in range(N):
            if maps[i][j] >= 2 and not visited[i][j]:
                clouds.append((i, j))
                maps[i][j] -= 2

print(sum(map(sum, maps)))
