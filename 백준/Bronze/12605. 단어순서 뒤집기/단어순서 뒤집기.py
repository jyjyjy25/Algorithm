N = int(input())

stack = [input().split() for _ in range(N)]
for i, s in enumerate(stack):
    result = ' '.join(s[::-1])
    print(f'Case #{i+1}: {result}')