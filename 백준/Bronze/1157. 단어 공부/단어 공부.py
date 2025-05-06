import sys

strs = sys.stdin.readline().strip()

str_dict = {}  # key: 알파벳 대문자 value: 개수
for s in strs:
    S = s.capitalize()
    if S in str_dict:
        str_dict[S] += 1
    else:
        str_dict[S] = 1

str_dict_values = list(str_dict.values())
max_value = max(str_dict_values)  # 가장 많이 사용된 알파벳의 개수
if str_dict_values.count(max_value) >= 2:  # 가장 많이 사용된 알파벳이 여러 개 존재
    print("?")
else:
    for k, v in str_dict.items():
        if v == max_value:
            print(k)
