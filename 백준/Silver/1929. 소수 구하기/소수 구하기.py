import sys

def gcd(x):
    if x == 1:
        return False
    elif x == 2 or x == 3:
        return True
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

M, N = map(int, sys.stdin.readline().split())
for i in range(M, N+1):
    if gcd(i):
        print(i)
