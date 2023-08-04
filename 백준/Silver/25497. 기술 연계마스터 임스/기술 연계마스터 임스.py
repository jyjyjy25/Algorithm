import sys

N = int(sys.stdin.readline())
stack = sys.stdin.readline().strip()

use_L, use_R = 0, 0
use_S, use_K = 0, 0

success = 0
for i in stack:
    if i.isdigit():
        success += 1
    elif i == 'K':
        if use_S == 0:
            break
        else:
            use_S -= 1
            success += 1
    elif i == 'R':
        if use_L == 0:
            break
        else:
            use_R -= 1
            success += 1
    elif i == 'L':
        use_L += 1
    elif i == 'S':
        use_S += 1

print(success)