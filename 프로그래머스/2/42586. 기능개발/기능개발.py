from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while(progresses):
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        
        for p in progresses:
            if p >= 100:
                cnt += 1
            else:
                break
        
        if cnt >= 1:
            answer.append(cnt)
            for i in range(cnt):
                progresses.popleft()
                speeds.popleft()

    return answer