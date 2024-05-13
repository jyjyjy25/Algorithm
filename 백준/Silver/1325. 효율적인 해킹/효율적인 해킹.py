import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)


def BFS(v):
    queue = deque([v])
    visited = [False for _ in range(N+1)]
    visited[v] = True
    cnt = 0
    
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)
                cnt += 1
    return cnt


count = [0 for _ in range(N+1)] 
for i in range(1, N+1):
    count[i] = BFS(i)

max_value = max(count)
for i in range(1, N+1):
    if max_value == count[i]:
        print(i, end=' ')
