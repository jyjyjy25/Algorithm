import sys
import math
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())


def is_prime(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


def DFS(x):
    if len(str(x)) == N:
        print(x)
    else:
        for i in range(1, 10, 2):
            if is_prime(x * 10 + i):
                DFS(x * 10 + i)


prime_num = [2, 3, 5, 7]
for p in prime_num:
    DFS(p)