# 11:25~

def solution(routes):
    answer = 0
    
    routes.sort()
    camera = routes[0][1]
    answer += 1
    
    record = []
    for s, e in routes[1:]:
        if camera >= s:  # 두 차량의 이동 경로가 겹침
            camera = min(camera, e)
        else:
            camera = e
            answer += 1

    return answer