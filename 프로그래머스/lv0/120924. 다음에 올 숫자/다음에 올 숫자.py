def solution(common):
    answer = 0
    i = 0
    
    ## 등차수열인지 확인
    if (common[i+1] - common[i] == common[i+2] - common[i+1]):
        r = common[i+1] - common[i]
        answer = common[-1] + r
    ## 등비수열인지 확인
    elif (common[i+1] / common[i] == common[i+2] / common[i+1]):
        r = common[i+1] / common[i]
        answer = common[-1] * r
    
    return answer