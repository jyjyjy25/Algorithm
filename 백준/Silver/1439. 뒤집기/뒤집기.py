import sys

S = sys.stdin.readline()

cnt = {'1': 0, '0': 0}

prev_num = S[0]
for s in S[1:]:
    if prev_num == s:
        continue
    else:
        cnt[prev_num] += 1
        prev_num = s

print(min(cnt.values()))
