import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().strip()) for _ in range(N)]
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def BFS(x, y):
    queue = deque([(x, y)])
    maps[x][y] = 0
    while queue:
        x, y = queue.popleft()
        if x == x2-1 and y == y2-1:  # 도착지점
            return maps[x2-1][y2-1]

        for ax, ay in zip(dx, dy):
            for i in range(1, K+1):  # 같은 방향으로 최대 K번 이동
                nx = x + ax * i
                ny = y + ay * i
                if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 범위를 벗어나는 경우
                    break
                if maps[nx][ny] == "#":  # 벽인 경우
                    break
                if maps[nx][ny] == ".":  # 빈칸인 경우
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
                elif maps[nx][ny] > maps[x][y]:  # 이미 방문한 경우 
                    continue
                else:
                    break
    return -1


print(BFS(x1-1, y1-1))