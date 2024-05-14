from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])

    visited = [[False] * (M) for _ in range(N)]
    
    dx = [1, -1, 0, 0]  # 동서남북
    dy = [0, 0, -1, 1]
    
    def BFS():
        queue = deque()
        queue.append((0, 0))
        visited[0][0] = True
        
        while queue:
            y, x = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if maps[ny][nx] and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((ny, nx))
                        maps[ny][nx] = maps[y][x] + 1       
            
    BFS()
    
    if maps[N-1][M-1]==1:
        return -1
    else:
        return maps[N-1][M-1]