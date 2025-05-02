import sys
from collections import deque


def BFS(x):
    queue = deque([(x, 0)])
    visited[x] = 0
    while queue:
        x, t = queue.popleft()
        if x == K:  # 도착
            return t
        
        for nx in [x*2, x+1, x-1]:
            if 100000 >= nx >= 0 and visited[nx] == -1:
                visited[nx] = x  # 이전 경로 값 기록
                queue.append((nx, t+1))


N, K = map(int, sys.stdin.readline().split())
visited = [-1 for _ in range(100001)]

min_time = BFS(N)
path = []  # 최단 경로

i = K  # 도착지점에서 역으로 경로 탐색
for _ in range(min_time+1):
    path.append(i)
    i = visited[i]

print(min_time)
print(" ".join(map(str, reversed(path))))