import sys

expression = sys.stdin.readline().strip()

A = expression.split('-')
B = []

new_expression = ""
for a in A:
    B = map(str, map(int, a.split('+')))
    new_expression += '+'.join(B)
    new_expression += '-'
new_expression = new_expression[:-1]

new_str = "("
for i, s in enumerate(new_expression):
    if s == '-':
        new_str += ")-("
    else:
        new_str += s

new_str += ')'

print(eval(new_str))