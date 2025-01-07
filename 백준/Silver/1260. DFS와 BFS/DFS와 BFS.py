import sys
from collections import deque


def DFS(v, visited):
    stack = [v]

    while stack:
        n = stack.pop()

        if not visited[n]:
            visited[n] = True
            print(n, end=' ')
        
            for x in reversed(graph[n]):
                stack.append(x)


def BFS(v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        n = queue.popleft()
        print(n, end=' ')

        for x in graph[n]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

# 그래프 초기화
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

visited = [False] * (N+1)
DFS(V, visited)

print()

visited = [False] * (N+1)
BFS(V, visited)
