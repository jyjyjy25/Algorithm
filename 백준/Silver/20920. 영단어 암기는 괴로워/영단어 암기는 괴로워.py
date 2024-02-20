import sys
import collections

N, M = map(int, sys.stdin.readline().split())

arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

word_dict = {}
for i in arr:
    # 단어의 길이가 M 이상인 단어만 단어장에 저장
    if len(i) < M:
        continue
    
    if word_dict.get(i) is None:
        word_dict[i] = 1
    else:
        word_dict[i] += 1

# 우선순위 3, 2, 1 순으로 정렬 수행
word_dict = collections.OrderedDict(sorted(word_dict.items(), key=lambda x: x[0]))
word_dict = collections.OrderedDict(sorted(word_dict.items(), key=lambda x: len(x[0]), reverse=True))
word_dict = collections.OrderedDict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True))

for w in word_dict:
    print(w)