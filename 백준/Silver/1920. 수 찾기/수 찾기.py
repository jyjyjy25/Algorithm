import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
X = list(map(int, sys.stdin.readline().split()))


def binary_search(x):
    global A, EXIST
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == x:
            EXIST = 1
            break
        elif A[mid] > x:
            end = mid - 1
        elif A[mid] < x:
            start = mid + 1
    

A.sort()

EXIST = 0
for x in X:
    EXIST = 0
    binary_search(x)
    print(EXIST)