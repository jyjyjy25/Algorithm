import sys

N = int(sys.stdin.readline())
expression = list(sys.stdin.readline().strip())
operand = [sys.stdin.readline().strip() for _ in range(N)]

# 피연산자를 입력받은 operand에 매핑
for i, e in enumerate(expression):
    if e.isalpha():
        idx = ord(e) - 65
        expression[i] = operand[idx]

stack = []
for e in expression:
    if e.isdigit():
        stack.append(e)
    else:
        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(eval(str(op1) + str(e) + str(op2)))

print('%.2f' % float(stack[0]))