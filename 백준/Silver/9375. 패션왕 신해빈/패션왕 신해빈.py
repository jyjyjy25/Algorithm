import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    clothes = {}
    for i in range(N):
        name, t = sys.stdin.readline().split()
        if t not in clothes:
            clothes[t] = []
        clothes[t].append(name)

    cases = 1
    for i, c in enumerate(clothes):
        cases *= len(clothes[c]) + 1

    print(cases - 1)
