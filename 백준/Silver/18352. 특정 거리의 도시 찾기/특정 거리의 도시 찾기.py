import sys
from collections import deque


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in graph[now_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[now_node] + 1


N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]  # 인접 리스트
visited = [False] * (N+1)  # 방문 리스트
distance = [0] * (N+1)  # 노드 별 최단 거리 리스트

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

BFS(X)

if K in distance:
    for i, d in enumerate(distance):
        if d == K:
            print(i)
else:
    print(-1)