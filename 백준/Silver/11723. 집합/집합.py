import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    a = sys.stdin.readline().split()
    if len(a) == 2:
        a, x = a[0], int(a[1])
    else:
        a = a[0]

    if a == "add":
        S.add(x)
    elif a == "remove":
        S.discard(x)
    elif a == "check":
        print(1) if x in S else print(0)
    elif a == "toggle":
        S.discard(x) if x in S else S.add(x)
    elif a == "all":
        S = set([i for i in range(1, 21)])
    elif a == "empty":
        S = set()
