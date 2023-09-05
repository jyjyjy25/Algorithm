import sys
N = int(sys.stdin.readline())
array = [(int(sys.stdin.readline().strip()), i) for i in range(N)]

sorted_array = sorted(array)

max_index = 0
for i in range(N):
    index_sub = sorted_array[i][1] - i
    if max_index < index_sub:
        max_index = index_sub

print(max_index + 1)