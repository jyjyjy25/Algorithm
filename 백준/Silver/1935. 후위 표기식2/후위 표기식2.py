import sys

N = int(sys.stdin.readline())
expression = list(sys.stdin.readline().strip())
operand = [sys.stdin.readline().strip() for _ in range(N)]
operator = ['*', '+', '/', '-']

# 피연산자를 입력받은 operand에 매핑
for i, e in enumerate(expression):
    if e.isalpha():
        idx = ord(e) - ord('A')
        expression[i] = operand[idx]

i = 0
result = 0
while (1):
    if expression[i] in operator:
        op1 = expression[i-2]
        op2 = expression[i-1]
        result = eval(op1 + expression[i] + op2)
        if len(expression) == 3:
            break
        else:
            expression = expression[:i-2] + expression[i+1:]
            expression.insert(i-2, str(result))
            i = 0
    else:
        i += 1

print('%.2f' % result)