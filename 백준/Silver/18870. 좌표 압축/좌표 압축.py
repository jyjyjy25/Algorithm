import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(list(set(arr)))

arr_dict = {}
for i, a in enumerate(sorted_arr):
    arr_dict[a] = i

answer = []
for a in arr:
    answer.append(arr_dict[a])

print(' '.join(list(map(str, answer))))