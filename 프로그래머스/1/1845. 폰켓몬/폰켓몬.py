from itertools import combinations

def solution(nums):
    answer = 0

#     count = []
#     for comb in combinations(nums, len(nums)//2):
#         count.append(len(set(comb)))
#         print(set(comb))

#     answer = max(count)
#     return answer

    temp = []
    for num in nums:
        if len(temp) == len(nums)//2:
            break
        
        if num in temp:
            continue
        else:
            temp.append(num)
    
    answer = len(temp)
    return answer