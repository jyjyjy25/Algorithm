import sys
from collections import deque


def BFS(x):
    global min_time

    queue = deque([(x, 0)])
    visited[x] = True
    while queue:
        x, t = queue.popleft()
        visited[x] = True  # 큐에서 꺼낸 후에 방문처리
        if t > min_time:
            continue
        
        if x == K:  # 동생 발견
            min_time = min(min_time, t)
            arrive_time_list.append(t)
        else:
            for nx in [x*2, x-1, x+1]:
                if 100000 >= nx >= 0 and not visited[nx]:
                    queue.append((nx, t+1))


N, K = map(int, sys.stdin.readline().split())
visited = [False for _ in range(100001)]

min_time = 100000  # 가장 빠른 시간
arrive_time_list = []  # K에 도착한 시간
cnt = 0  # min_time에 도착한 경우의 수

BFS(N)
for a in arrive_time_list:
    if a == min_time:
        cnt += 1
print(min_time)
print(cnt)