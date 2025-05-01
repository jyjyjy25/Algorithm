import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque([])
for i in range(N):
    for j in range(M):
        if not visited[i][j] and maps[i][j] == 1:
            queue.append((i, j))

temp_queue = deque([])
days = 0
while queue:
    x, y = queue.popleft()
    for ax, ay in zip(dx, dy):
        nx = x + ax
        ny = y + ay
        if N > nx >= 0 and M > ny >= 0:
            if not visited[nx][ny] and maps[nx][ny] == 0:
                temp_queue.append((nx, ny))
                visited[nx][ny] = True
                maps[nx][ny] = 1
    
    if not queue:
        queue = temp_queue
        temp_queue = deque([])
        days += 1

flag = False  # 안 익은 토마토가 있는지 여부
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            flag = True
            break

if not flag:
    print(days-1)
else:
    print(-1)