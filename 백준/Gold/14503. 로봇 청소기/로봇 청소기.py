import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())  # 0: 북, 1: 동, 2: 남, 3: 서
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

global cleaning
cleaning = 0

visited = [[False for _ in range(M)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check_inner(x, y):
    if -1 < x < N and -1 < y < M:
        return True
    else:
        return False

def robot_cleaning(x, y, d):
    global cleaning
    if maps[x][y] == 0 and not visited[x][y]:
        visited[x][y] = True
        cleaning += 1
    
    isEmpty = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if check_inner(nx, ny) and maps[nx][ny] == 0 and not visited[nx][ny]:
            isEmpty = True
            break

    if isEmpty:
        d = (d-1) % 4  # 반시계방향 90도 회전
        if d == 0:  # 북쪽
            if check_inner(x-1, y) and maps[x-1][y] == 0 and not visited[x-1][y]:
                x -= 1
        elif d == 1:  # 동쪽
            if check_inner(x, y+1) and maps[x][y+1] == 0 and not visited[x][y+1]:
                y += 1
        elif d == 2:  # 남쪽
            if check_inner(x+1, y) and maps[x+1][y] == 0 and not visited[x+1][y]:
                x += 1
        elif d == 3:  # 서쪽
            if check_inner(x, y-1) and maps[x][y-1] == 0 and not visited[x][y-1]:
                y -= 1
        robot_cleaning(x, y, d)
    else:  # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        is_can_stop = False
        if d == 0:  # 북쪽
            if check_inner(x+1, y) and maps[x+1][y] == 0:
                x += 1
                robot_cleaning(x, y, d)
            else:
                is_can_stop = True
        elif d == 1:  # 동쪽
            if check_inner(x, y-1) and maps[x][y-1] == 0:
                y -= 1
                robot_cleaning(x, y, d)
            else:
                is_can_stop = True
        elif d == 2:  # 남쪽
            if check_inner(x-1, y) and maps[x-1][y] == 0:
                x -= 1
                robot_cleaning(x, y, d)
            else:
                is_can_stop = True
        elif d == 3:  # 서쪽
            if check_inner(x, y+1) and maps[x][y+1] == 0:
                y += 1
                robot_cleaning(x, y, d)
            else:
                is_can_stop = True
        
        if is_can_stop:
            return


robot_cleaning(r, c, d)
print(cleaning)
