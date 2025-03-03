import sys

while True:
    line = sys.stdin.readline().strip("\n")
    if line == ".":
        break

    answer = "yes"
    stack = []
    for l in line:
        if l == "(" or l == "[":
            stack.append(l)
        elif l == ")":
            if not stack or stack.pop() != "(":
                answer = "no"
                break
        elif l == "]":
            if not stack or stack.pop() != "[":
                answer = "no"
                break
    
    if stack:
        print('no')
    else:
        print(answer)