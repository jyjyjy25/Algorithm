# 11:25~

def solution(routes):
    answer = 0
    
    routes.sort()
    prev_s, prev_e = routes[0][0], routes[0][1]
    answer += 1
    
    record = []
    for s, e in routes[1:]:
        if prev_e >= s:  # 두 차량의 경로가 겹침
            prev_e = min(prev_e, e)
        else:
            answer += 1
            prev_e = e

    return answer