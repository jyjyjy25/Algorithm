def solution(N, number):
    answer = -1
    
    dict = {}
    for i in range(1, 9):
        num = int(str(N)*i)
        if num == number:
            return i
        
        dict[i] = set()
        dict[i].add(num)
    
    for i in range(2, 9):
        for j in range(1, i):
            for op1 in dict[j]:
                for op2 in dict[i-j]:
                    dict[i].add(op1+op2)
                    dict[i].add(op1-op2)
                    dict[i].add(op1*op2)
                    if op2 != 0:
                        dict[i].add(op1//op2)
        
        if number in dict[i]:
            return i
            break
        
    return answer