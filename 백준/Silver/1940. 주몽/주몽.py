import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
pointer_a = 0
pointer_b = len(arr)-1

cnt = 0
while pointer_a < pointer_b:
    if arr[pointer_a] + arr[pointer_b] == M:
        cnt += 1
        pointer_a += 1
        pointer_b -= 1
    elif arr[pointer_a] + arr[pointer_b] > M:
        pointer_b -= 1
    elif arr[pointer_a] + arr[pointer_b] < M:
        pointer_a += 1

print(cnt)
