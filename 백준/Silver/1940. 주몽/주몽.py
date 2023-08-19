import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
items = list(map(int, sys.stdin.readline().split()))

cnt = 0
start_pointer = 0
end_pointer = N - 1

items.sort()
while (start_pointer < end_pointer):
    if (items[start_pointer] + items[end_pointer] < M):
        start_pointer = start_pointer + 1
    elif (items[start_pointer] + items[end_pointer] > M):
        end_pointer = end_pointer - 1
    else:
        cnt = cnt + 1
        end_pointer = end_pointer - 1
        start_pointer = start_pointer + 1

print(cnt)