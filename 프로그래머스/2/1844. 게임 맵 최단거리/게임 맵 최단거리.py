from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    visited = [[False] * M for _ in range(N)]
    xlist = [0, 0, -1, 1]  # 상하좌우
    ylist = [1, -1, 0, 0]
    
    x, y = 0, 0  # 시작 좌표
    queue = deque([(x, y)])
    visited[x][y] = False
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(xlist, ylist):
            nx = x + dx
            ny = y + dy
            if N > nx >= 0 and M > ny >= 0:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = False
                    maps[nx][ny] = maps[x][y] + 1
    
    if maps[N-1][M-1] == 1:
        return -1
    else:
        return maps[N-1][M-1]