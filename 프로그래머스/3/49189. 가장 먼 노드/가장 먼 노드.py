# 11:26~
from collections import deque

def BFS(v, graph, visited):
    distances = [0 for _ in range(len(visited))]
    
    visited[v] = True
    queue = deque([v])
    
    while queue:
        node = queue.popleft()
        for new_node in graph[node]:
            if not visited[new_node]:
                visited[new_node] = True
                distances[new_node] = distances[node] + 1
                queue.append(new_node)
    
    return distances

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False for _ in range(n+1)]
    dists = BFS(1, graph, visited)
    max_dist = max(dists)
    
    return dists.count(max_dist)