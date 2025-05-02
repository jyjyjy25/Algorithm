import sys


def DFS(x):
    visited[x] = True
    for n in graph[x]:
        if not visited[n]:
            DFS(n)


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    for i, a in enumerate(arr):
        graph[i+1].append(a)
    
    cycle = 0
    for i in range(1, N+1):
        if not visited[i]:
            cycle += 1
            DFS(i)
    print(cycle)
