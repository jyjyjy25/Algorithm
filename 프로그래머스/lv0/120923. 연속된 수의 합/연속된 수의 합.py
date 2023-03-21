def solution(num, total):
    start = -100
    answer = []
    
    while(True):
        answer = []
        sum = 0
        i = start
        for _ in range(num):
            sum = sum + i
            answer.append(i)
            i = i + 1
            
        if sum == total:
            break
        else:
            start = start + 1
            
    return answer