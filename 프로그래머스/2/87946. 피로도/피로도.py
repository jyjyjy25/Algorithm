from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    nums = [n for n in range(len(dungeons))]
    
    max_visit = []
    for per in permutations(nums, len(nums)):
        temp_k = k
        visit_cnt = 0
        for p in per:
            if dungeons[p][0] <= temp_k:
                temp_k -= dungeons[p][1]
                visit_cnt += 1
            else:
                break

        max_visit.append(visit_cnt)
        
    answer = max(max_visit)
    
    return answer