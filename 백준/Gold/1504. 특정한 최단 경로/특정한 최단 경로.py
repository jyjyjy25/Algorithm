import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())  # 꼭 지나야 하는 정점
INF = 987654321


def dijkstra(v):
    distances = [INF for _ in range(N+1)]
    distances[v] = 0
    queue = []
    heapq.heappush(queue, (distances[v], v))
    
    while queue:
        dist, n = heapq.heappop(queue)

        if distances[n] < dist: continue

        for new_node, w in graph[n]:
            if dist + w < distances[new_node]:
                distances[new_node] = dist + w
                heapq.heappush(queue, (distances[new_node], new_node))
    
    return distances


d_1 = dijkstra(1)
d_v1 = dijkstra(v1)
d_v2 = dijkstra(v2)

v1_to_v2 = d_1[v1] + d_v1[v2] + d_v2[N]
v2_to_v1 = d_1[v2] + d_v2[v1] + d_v1[N]

if v1_to_v2 >= INF and v2_to_v1 >= INF:
    print(-1)
else:
    print(min(v1_to_v2, v2_to_v1))