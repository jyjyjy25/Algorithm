import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K = int(sys.stdin.readline())
find = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

prefix_sum = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    sum = 0
    for j in range(M):
        sum += arr[i][j]
        prefix_sum[i][j] = sum

for i, j, x, y in find:
    temp = 0
    for k in range(i, x+1):
        temp += prefix_sum[k-1][y-1] - prefix_sum[k-1][j-1] + arr[k-1][j-1]
    print(temp)
