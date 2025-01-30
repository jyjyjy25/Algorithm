# 10:47~
def solution(citations):
    citations.sort()
    n = len(citations)
    print(citations, n)
    
    for i in range(n, -1, -1):
        cnt = 0
        for c in reversed(citations):
            if c >= i:
                cnt += 1
            else:
                break
        print(i, cnt)
        if cnt >= i:
            return i
            
#     for i, c in enumerate(reversed(citations)):
#         if n < c:
#             continue
            
#         cnt = i + 1
#         if cnt >= c:
#             return c
