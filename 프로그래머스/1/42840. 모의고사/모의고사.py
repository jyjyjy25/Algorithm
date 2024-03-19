def solution(answers):
    answer = []
    
    per_1 = [1, 2, 3, 4, 5]
    per_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    per_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_cnt = {"1": 0, "2": 0, "3": 0}
    for i, a in enumerate(answers):
        if a == per_1[i%5]:
            answer_cnt["1"] += 1
        if a == per_2[i%8]:
            answer_cnt["2"] += 1
        if a == per_3[i%10]:
            answer_cnt["3"] += 1
    
    answer_cnt = sorted(answer_cnt.items(), key=lambda x: x[1], reverse=True)
    
    max = 0
    for k, v in answer_cnt:
        if max <= v:
            max = v
            answer.append(int(k))
    
    return answer