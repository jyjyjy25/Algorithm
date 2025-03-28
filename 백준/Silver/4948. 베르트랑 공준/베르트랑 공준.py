def is_prime(x):
    if x == 1:
        return False

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    
    return True

all_list = list(range(2, 246912))
prime_list = []
for i in all_list:
    if is_prime(i):
        prime_list.append(i)

result_list = []
while (True):
    N = int(input())
    if N == 0:
        break

    prime_cnt = 0
    for i in prime_list:
        if N < i <= 2*N:
            prime_cnt += 1
        if i > 2*N:
            break

    result_list.append(prime_cnt)

for result in result_list:
    print(result)
