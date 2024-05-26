import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(T):
    I = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    rx, ry = map(int, sys.stdin.readline().split())

    maps = [[False] * I for _ in range(I)]
    count = 0
    
    maps[a][b] = 0
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == a and ny == b:
                continue
            if -1 < nx < I and -1 < ny < I:
                if not maps[nx][ny]:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                                
            if rx == nx and ry == ny:  # 종료조건
                queue = []
                break
 
    print(maps[rx][ry])