# 6:21~
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
visited = [[False] * M for _ in range(N)]
maps = []
x, y = 0, 0

for i in range(N):
    line = sys.stdin.readline()
    temp = []
    for j, l in enumerate(line):
        if l == "\n":
            continue

        if l == "I":
            x, y = i, j
        temp.append(l)
    maps.append(temp)


dx = [0, 0, -1, +1]
dy = [1, -1, 0, 0]

cnt = 0
def BFS(x, y):
    global cnt
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        if maps[x][y] == "P":
            cnt += 1
        
        for ax, ay in zip(dx, dy):
            nx = x + ax
            ny = y + ay
            if (N > nx and nx >= 0) and (M > ny and ny >= 0):
                if not visited[nx][ny] and maps[nx][ny] != "X":
                    queue.append((nx, ny))
                    visited[nx][ny] = True


BFS(x, y)
print(cnt) if cnt else print("TT")
