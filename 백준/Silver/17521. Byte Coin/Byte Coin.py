import sys

n, W = map(int, sys.stdin.readline().split())
bc_graph = [int(sys.stdin.readline()) for _ in range(n)]

coins = W // bc_graph[0]
W -= coins * bc_graph[0]
status = "+"

for i in range(0, len(bc_graph)-1):
    if bc_graph[i] < bc_graph[i+1]:
        if status == "-":  # 매수
            coins = W // bc_graph[i]
            W -= coins * bc_graph[i]
            status = "+"
    elif bc_graph[i] > bc_graph[i+1]:
        if status == "+":  # 매도
            W += coins * bc_graph[i]
            coins = 0
            status = "-"

# n일째 모든 코인 매도
W += coins * bc_graph[n-1]
print(W)