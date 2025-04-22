# 6:40~
import heapq as hp

def solution(jobs):
    new_jobs = []
    hp.heapify(new_jobs)
    for i, (s, l) in enumerate(jobs):
        hp.heappush(new_jobs, (s, l, i))  # (요청시각, 소요시간, 작업번호)
    
    waiting_queue = []  # 우선순위 큐
    hp.heapify(waiting_queue)
    
    s, l, i = hp.heappop(new_jobs)
    hp.heappush(waiting_queue, (l, s, i))  # (소요시간, 요청시각, 작업번호)
    
    time = 0
    total_return_time = 0  # 총 반환 시간
    while waiting_queue or new_jobs:
        if not waiting_queue and new_jobs:
            if min(new_jobs)[0] <= time:  # 현재 시간을 기준으로 작업 가능한 요청들을 우선순위 큐에 삽입
                while new_jobs and min(new_jobs)[0] <= time:
                    s, l, i = hp.heappop(new_jobs)
                    hp.heappush(waiting_queue, (l, s, i))
            else:  # 현재 시간을 기준으로 작업 가능한 요청이 없으므로 시간 1 증가
                time += 1
        elif waiting_queue:
            if min(waiting_queue)[1] > time:
                time += 1
            else:
                l, s, i = hp.heappop(waiting_queue)
                time += l
                return_time = time - s  # 반환 시간
                total_return_time += return_time

            if new_jobs:
                while new_jobs and min(new_jobs)[0] <= time:  # 현재 시간을 기준으로 작업 가능한 요청들을 우선순위 큐에 삽입
                    s, l, i = hp.heappop(new_jobs)
                    hp.heappush(waiting_queue, (l, s, i))     
        
    return int(total_return_time / len(jobs))
