from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    visited = [[False] * M for _ in range(N)]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def BFS(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        
        while queue:
            x, y = queue.popleft()
            for ax, ay in zip(dx, dy):
                nx = x + ax
                ny = y + ay
                if N > nx >= 0 and M > ny >= 0:
                    if maps[nx][ny] != 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        maps[nx][ny] = maps[x][y] + 1
            
    BFS(0, 0)
    if maps[N-1][M-1] != 1:
        return maps[N-1][M-1]
    else:
        return -1