import sys

N = int(sys.stdin.readline())
sequence_list = list(map(int, sys.stdin.readline().split()))

stack = []
NGE = [-1] * N
for i, s in enumerate(sequence_list):
    stack.append(i)
    if i == N-1:  # 수열의 마지막 값에 대한 NGE는 항상 -1
        NGE[stack.pop()] = -1
        break

    while stack and sequence_list[stack[-1]] < sequence_list[i+1]:
        NGE[stack.pop()] = sequence_list[i+1]

print(*NGE)