from collections import deque

def solution(m, n, puddles):
    visited = [[False]*(m+1) for _ in range(n+1)]
    dp = [[0]*(m+1) for _ in range(n+1)]  # m == x
    dp[1][1] = 1
    
    dx = [1, 0]  # [오른쪽, 아래쪽]
    dy = [0, 1]
    
    def BFS(x, y):
        queue = deque([(1, 1)])
        while queue:
            y, x = queue.popleft()
            for ax, ay in zip(dx, dy):
                nx = x + ax
                ny = y + ay
                if m >= nx > 0 and n >= ny > 0:
                    if [nx, ny] not in puddles and not visited[ny][nx]:
                        queue.append((ny, nx))
                        visited[ny][nx] = True
                        
                        if m >= nx-1 > 0 and n >= ny-1 > 0:
                            dp[ny][nx] = dp[ny][nx-1] + dp[ny-1][nx]
                        elif m >= nx-1 > 0:
                            dp[ny][nx] = dp[ny][nx-1]
                        else:
                            dp[ny][nx] = dp[ny-1][nx]

    BFS(1, 1)
    return dp[n][m] % 1000000007