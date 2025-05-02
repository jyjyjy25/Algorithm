#4:27

def solution(numbers):
    str_nums = list(map(str, numbers))
    str_nums.sort(reverse=True, key=lambda x: str(x)*(6//len(x)))
    answer = "".join(str_nums)
    return str(int(answer))