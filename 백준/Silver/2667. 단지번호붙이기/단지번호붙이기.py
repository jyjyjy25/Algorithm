import sys

N = int(sys.stdin.readline())

house_num = []
visited = [[False] * N for _ in range(N)]

maps = []
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().rstrip())))

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def DFS(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:  # 지도 밖을 벗어나지 않는지 확인
            if maps[nx][ny] and not visited[nx][ny]:  # 집이 있고 방문한 적이 없는 경우
                DFS(nx, ny)


for x in range(N):
    for y in range(N):
        if maps[x][y] and not visited[x][y]:
            cnt = 0
            DFS(x, y)
            if cnt != 0:
                house_num.append(cnt)

print(len(house_num))
for h in sorted(house_num):
    print(h)