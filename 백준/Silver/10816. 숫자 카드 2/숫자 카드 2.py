from collections import Counter

N = int(input())
card_list = sorted(list(map(int, input().split())))
M = int(input())
num_list = list(map(int, input().split()))

count = Counter(card_list)

for n in num_list:
    if n in count:
        print(count[n], end=' ')
    else:
        print(0, end=' ')