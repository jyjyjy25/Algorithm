import sys

while True:
    input_num = str(sys.stdin.readline().strip())
    if input_num == "0":
        break

    l, r = 0, len(input_num) - 1
    FLAG = True
    while l <= r:
        if l == r:
            break

        if input_num[l] == input_num[r]:
            l += 1
            r -= 1
        else:
            FLAG = False
            break

    if FLAG:
        print('yes')
    else:
        print('no')
