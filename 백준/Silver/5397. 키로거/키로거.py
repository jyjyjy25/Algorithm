import sys

N = int(sys.stdin.readline())
for _ in range(N):
    command = sys.stdin.readline().strip()
    cur_left = []
    cur_right = []

    for c in command:
        if c == "-":
            if cur_left:
                cur_left.pop()
        elif c == "<":
            if cur_left:
                cur_right.append(cur_left.pop())
        elif c == ">":
            if cur_right:
                cur_left.append(cur_right.pop())
        else:
            cur_left.append(c)

    print("".join(cur_left + list(reversed(cur_right))))