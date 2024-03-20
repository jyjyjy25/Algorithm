def solution(brown, yellow):
    answer = []
    
    # 소인수 구하기
    primes = brown + yellow
    prime_list = []
    for p in range(1, primes):
        if primes % p == 0:
            prime_list.append((p, primes//p))
    
    for x, y in reversed(prime_list):
        if 2*x + 2*y - 4 == brown and x*y - 2*x - 2*y + 4 == yellow:
            answer.append(x)
            answer.append(y)
            break
            
    answer.sort(reverse=True)
    
    return answer