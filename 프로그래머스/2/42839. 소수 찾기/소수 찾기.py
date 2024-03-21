from itertools import permutations

def solution(numbers):
    answer = 0
    
    def is_prime(n):
        if n < 2:
            return False
        
        for i in range(2, n):
            if n % i == 0:
                return False
            
        return True
    
    nums_set = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            nums_set.add(int(''.join(p)))
    
    for n in nums_set:
        if is_prime(n):
            answer += 1
            
    return answer