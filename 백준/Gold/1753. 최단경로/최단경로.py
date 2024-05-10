import sys
import heapq

INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
distance = [INF] * (V+1)

for _ in range(E):
    n, e, w = map(int, sys.stdin.readline().split())
    graph[n].append((e, w))


def dijkstra(K):
    queue = []
    heapq.heappush(queue, (0, K))  # (거리, 시작노드)로 초기화, 최소힙
    distance[K] = 0
    while queue:
        dist, now_node = heapq.heappop(queue)

        if distance[now_node] < dist:  # 큐에서 꺼낸 최단 거리가 최단거리 리스트에 기록된 거리보다 크면, dist는 최단거리 정보가 아니다. 즉. 업데이트가 되지 않은 정보임.
            continue
        
        for e, w in graph[now_node]:
            cost = dist + w  # 최단 거리 계산
            if cost < distance[e]:  # 최단 거리로 업데이트
                distance[e] = cost
                heapq.heappush(queue, (cost, e))


dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])