from itertools import product

def solution(word):
    answer = 0
    
    alpha = ['A', 'E', "I", "O", "U"]
    dic = []
    for i in range(1, len(alpha)+1):
        for per in product(alpha, repeat=i):
            dic.append(''.join(per))
    
    dic.sort()
    answer = dic.index(word) + 1
    
    return answer