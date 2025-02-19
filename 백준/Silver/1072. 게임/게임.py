import sys
import math

X, Y = map(int, sys.stdin.readline().split())
Z = math.floor(Y * 100 / X)

low = 1
high = 1000000000

while low <= high:
    mid = (low + high) // 2

    nX = math.floor(((Y + mid) * 100 / (X + mid)))
    if nX == Z:
        low = mid + 1
    else:
        high = mid - 1

nX = math.floor(((Y + low) * 100 / (X + low)))
if nX == Z:
    print(-1)
else:
    print(low)