N = int(input())

array = []
for i in range(N):
    array.append(list(input().split()))

for i, a in enumerate(array):
    a.reverse()
    print(f'Case #{i+1}:', end=' ')
    for i in a:
        print(i, end=' ')
    print()
    
