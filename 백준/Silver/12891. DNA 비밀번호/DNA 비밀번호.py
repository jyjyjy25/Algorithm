import sys

DNA_str_len, partial_str_len = map(int, sys.stdin.readline().split())
DNA_str = sys.stdin.readline()
min_A, min_C, min_G, min_T = map(int, sys.stdin.readline().split())
cnt = 0


def check_condition(curr_str_dict):
    global cnt
    if curr_str_dict['A'] >= min_A and curr_str_dict['C'] >= min_C and curr_str_dict['G'] >= min_G and curr_str_dict['T'] >= min_T:
        cnt += 1


# 초기 문자열 할당
curr_str_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in range(partial_str_len):
    curr_str_dict[DNA_str[i]] += 1
check_condition(curr_str_dict)

for i in range(DNA_str_len - partial_str_len):
    start_p = i
    end_p = start_p + partial_str_len

    curr_str_dict[DNA_str[start_p]] -= 1
    curr_str_dict[DNA_str[end_p]] += 1
    check_condition(curr_str_dict)

print(cnt)