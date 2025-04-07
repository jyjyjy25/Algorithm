# 12:25~
def solution(genres, plays):
    answer = []
    
    candidate_genre = {}
    candidate_song = {}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in candidate_song:
            candidate_song[g] = [(i, p)]
        else:
            candidate_song[g].append((i, p))
        
        if g not in candidate_genre:
            candidate_genre[g] = p
        else:
            candidate_genre[g] += p
        
    for k, v in candidate_song.items():
        candidate_song[k] = sorted(v, key=lambda x: x[1], reverse=True)
        
    candidate_genre = sorted(candidate_genre.items(), key=lambda x: x[1], reverse=True)
    
    for genre, total in candidate_genre:
        for s in candidate_song[genre][:2]:
            answer.append(s[0])
    
    return answer