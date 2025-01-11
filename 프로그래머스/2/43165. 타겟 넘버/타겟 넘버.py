def solution(numbers, target):
    global answer
    answer = 0
    
    def DFS(i, sum):
        global answer
        if i == len(numbers):
            if sum == target:
                answer += 1
            return
        
        DFS(i+1, sum+numbers[i])
        DFS(i+1, sum-numbers[i])
    
    DFS(0, 0)
    
    return answer