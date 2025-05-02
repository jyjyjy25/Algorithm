import sys
from itertools import permutations

def cal_ans(arr):
    sum = 0
    for i in range(1, len(arr)):
        sum += abs(arr[i-1] - arr[i])
    return sum


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

max_value = 0
for p in permutations(arr):
    max_value = max(max_value, cal_ans(p))

print(max_value)