import sys
from itertools import permutations

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
operator_cnt = list(map(int, sys.stdin.readline().split()))
operator = ["+", "-", "*", "/"]

operator_list = []
for cnt, op in zip(operator_cnt, operator):
    for _ in range(cnt):
        operator_list.append(op)

results = []
for p in permutations(operator_list):
    pre_result = arr[0]
    for i in range(N-1):
        if p[i] == "+":
            pre_result += arr[i+1]
        elif p[i] == "-":
            pre_result -= arr[i+1]
        elif p[i] == "*":
            pre_result *= arr[i+1]
        elif p[i] == "/":
            if pre_result < 0:
                pre_result = -1 * ((-1 * pre_result) // arr[i+1])
            else:
                pre_result //= arr[i+1]
    results.append(pre_result)

print(max(results))
print(min(results))
