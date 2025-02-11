import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def DFS(v):
    visited[v] = True

    for g in graph[v]:
        if not visited[g]:
            DFS(g)


visited = [False] * (N+1)
DFS(1)
print(sum(visited) - 1)
