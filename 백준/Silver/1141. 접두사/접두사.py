import sys

N = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
arr.sort()

cnt = 1
for i in range(len(arr)-1):
    if len(arr[i]) <= len(arr[i+1]) and arr[i] == arr[i+1][:len(arr[i])]:
        continue

    cnt += 1

print(cnt)