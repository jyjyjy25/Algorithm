def solution(nums):
    types = set()
    for num in nums:
        types.add(num)

    answer = 0
    if len(types) > len(nums)/2 :
        answer = len(nums)/2
    else:
        answer = len(types)
    return answer