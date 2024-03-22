import sys
from itertools import permutations

K = int(sys.stdin.readline())
C = sys.stdin.readline().split()

nums = [n for n in range(0, 10)]

answers = []
for p in permutations(nums, K+1):
    is_valid = True
    for i in range(len(p)-1): 
        if C[i] == '<':
            if p[i] > p[i+1]:
                is_valid = False
                break
        else:
            if p[i] < p[i+1]:
                is_valid = False
                break

    if is_valid:
        answers.append(p)

print(''.join(map(str, answers[-1])))
print(''.join(map(str, answers[0])))