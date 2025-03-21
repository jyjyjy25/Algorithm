import sys

N, M = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(M+1)]]
for _ in range(N):
    temp_arr = [0]
    arr.append(temp_arr + list(map(int, sys.stdin.readline().split())))

K = int(sys.stdin.readline())
find = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

prefix_sum = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(M+1):
        if j == 0 and i == 0:
            continue
        elif j == 0:
            prefix_sum[i][j] = prefix_sum[i-1][j]
        else:
            prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + arr[i][j]

for i, j, x, y in find:
    print(prefix_sum[x][y] - prefix_sum[x][j-1] - prefix_sum[i-1][y] + prefix_sum[i-1][j-1])