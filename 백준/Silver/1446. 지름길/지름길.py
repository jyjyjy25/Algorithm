import sys

N, D = map(int, sys.stdin.readline().split())

routes = [[] for _ in range(D+1)]
for _ in range(N):
    S, E, L = map(int, sys.stdin.readline().split())
    
    if S < 0 or E > D:  # 지름길의 위치가 범위를 벗어난 경우
        continue
    if E - S < L:  # 지름길이 더 긴 거리를 갖는 경우
        continue
    
    routes[E].append((S, L))

answer = [0 for _ in range(D+1)]
for i in range(1, D+1):
    answer[i] = answer[i-1] + 1

    if routes[i]:
        for route in routes[i]:
            S, L = route
            answer[i] = min(answer[i], answer[S] + L)

print(answer[D])