import sys
from collections import deque


def BFS(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        if abs(x-end[0]) + abs(y-end[1]) <= 1000:  # 현재 위치에서 페스티벌까지의 거리가 1000 이하이면 도착 성공
            return True
        
        # 현재 위치에서 편의점까지의 거리가 1000 이하이면 방문(맥주 리필)
        for i in range(N):
            if not visited[i]:
                if abs(x - convenient_stores[i][0]) + abs(y - convenient_stores[i][1]) <= 1000:
                    queue.append((convenient_stores[i][0], convenient_stores[i][1]))
                    visited[i] = True
    return False


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())  # 편의점 개수
    
    start = list(map(int, sys.stdin.readline().split()))
    convenient_stores = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    end = list(map(int, sys.stdin.readline().split()))

    visited = [0 for _ in range(N)]  # 편의점 방문 여부
    result = BFS(start[0], start[1])  # 페스티벌 갈말
    if result:
        print("happy")
    else:
        print("sad")
