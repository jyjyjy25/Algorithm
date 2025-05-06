import sys

strs = sys.stdin.readline().strip()

str_dict = {}
for s in strs:
    S = s.capitalize()
    if S in str_dict:
        str_dict[S] += 1
    else:
        str_dict[S] = 1

str_dict_values = sorted(str_dict.values(), reverse=True)
max_value = str_dict_values[0]
if len(str_dict_values) > 1 and max_value == str_dict_values[1]:  # 가장 많이 사용된 알파벳이 여러 개 존재
    print("?")
else:
    for k, v in str_dict.items():
        if v == max_value:
            print(k)
