def solution(prices):
    answer = []
    
    for i, p in enumerate(prices):
        seconds = 0
        for j in range(i+1, len(prices)):
            seconds += 1
            if p > prices[j]:
                break
            
        answer.append(seconds)
    
    return answer