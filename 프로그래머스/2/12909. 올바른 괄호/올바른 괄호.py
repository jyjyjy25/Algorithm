def solution(s):
    answer = True
    
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)

    if stack:
        answer = False
        
    return answer