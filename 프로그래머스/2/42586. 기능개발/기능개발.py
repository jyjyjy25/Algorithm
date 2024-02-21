import math
def solution(progresses, speeds):
    answer = []
    
    release = []
    # 배포까지 소요되는 날를 구한다.
    for i, p in enumerate(progresses):
        release.append(math.ceil((100-p) / speeds[i]))
    
    while len(release) > 0:
        tmp = release.pop(0)
        cnt = 1
        while len(release) > 0 and tmp >= release[0]:
            release.pop(0)
            cnt += 1
        
        answer.append(cnt)
    
    return answer
