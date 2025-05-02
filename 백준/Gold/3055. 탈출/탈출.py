# 5:25~
import sys
from collections import deque


R, C = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().strip()) for _ in range(R)]

queueS = deque([])  # 고슴도치의 위치
destination = []  # 비버의 굴 위치(D)
queueW = deque([])  # 물 위치(*)
for i in range(R):
    for j in range(C):
        if maps[i][j] == ".":
            continue

        if maps[i][j] == "S":
            queueS = deque([(i, j)])
            maps[i][j] = 0
        elif maps[i][j] == "D":
            destination = [i, j]
        elif maps[i][j] == "*":
            queueW.append((i, j))

# 방향 벡터(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    while True:
        # 고슴도치 이동
        for _ in range(len(queueS)):  # 이전 고슴도치의 영역에 대해서만 이동
            x, y = queueS.popleft()
            
            # 물로 덮어졌다면 이동 불가
            if maps[x][y] == "*":
                continue

            for ax, ay in zip(dx, dy):
                nx = x + ax
                ny = y + ay
                if R > nx >= 0 and C > ny >= 0:
                    if maps[nx][ny] == ".":
                        maps[nx][ny] = maps[x][y] + 1  # 이동
                        queueS.append((nx, ny))
                    elif maps[nx][ny] == "D":
                        return maps[x][y] + 1

        # 물 확장
        for _ in range(len(queueW)):  # 이전 물의 영역에 대해서만 확장
            x, y = queueW.popleft()
            for ax, ay in zip(dx, dy):
                nx = x + ax
                ny = y + ay
                if R > nx >= 0 and C > ny >= 0:
                    if maps[nx][ny] != "X" and maps[nx][ny] != "D" and maps[nx][ny] != "*":  # 바위나 비버 굴이 아니면 방문
                        maps[nx][ny] = "*"  # 물 확장
                        queueW.append((nx, ny))

        if not queueS:
            return "KAKTUS"

print(BFS())