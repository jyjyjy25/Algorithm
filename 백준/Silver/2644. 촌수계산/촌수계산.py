import sys
from collections import deque

N = int(sys.stdin.readline())
c, d = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

# 그래프 초기화
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
maps = [0] * (N+1)


def BFS(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        n = queue.popleft()
        for x in graph[n]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)
                maps[x] = maps[n] + 1


BFS(c)

print(-1) if maps[d] == 0 else print(maps[d])
