import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited_alph = set()


def DFS(x, y):
    global cnt, max_count
    visited_alph.add(board[x][y])

    for ax, ay in zip(dx, dy):
        nx = x + ax
        ny = y + ay
        if R > nx >= 0 and C > ny >= 0:
            if board[nx][ny] not in visited_alph:
                cnt += 1
                DFS(nx, ny)
                
                max_count = max(cnt, max_count)
                cnt -= 1
                visited_alph.remove(board[nx][ny])


cnt, max_count = 1, 1
DFS(0, 0)
print(max_count)
