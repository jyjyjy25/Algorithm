from collections import deque

def solution(n, results):
    answer = 0
    
    win_list = [[] for _ in range(n+1)]
    for w, l in results:
        win_list[w].append(l)
    
    queue = deque([])
    for i, w in enumerate(win_list):
        if w:  queue.append((i, w))

    while queue:
        w, lose_nodes = queue.popleft()
        for lose in lose_nodes:
            for l in win_list[lose]:
                if l not in win_list[w]:
                    win_list[w].append(l)
                    queue.append((w, win_list[w]))
    
    
    lose_list = [[] for _ in range(n+1)]
    for w, l in results:
        lose_list[l].append(w)
    
    queue = deque([])
    for i, l in enumerate(lose_list):
        if l:  queue.append((i, l))
    
    while queue:
        l, win_nodes = queue.popleft()
        for win in win_nodes:
            for w in lose_list[win]:
                if w not in lose_list[l]:
                    lose_list[l].append(w)
                    queue.append((l, lose_list[l]))
    
    for w, l in zip(win_list, lose_list):
        if len(w) + len(l) == n-1:
            answer += 1
    
    return answer