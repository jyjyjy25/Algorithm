def solution(babbling):
    answer = 0
    available = ["aya", "ye", "woo", "ma"]
    
    for x in babbling:
        length = 0
        for a in available:
            if a in x:
                length = length + len(a)
        if(length == len(x)):
            answer = answer + 1     
        
    return answer