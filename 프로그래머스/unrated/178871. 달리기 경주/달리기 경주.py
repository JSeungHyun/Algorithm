def solution(players, callings):
    rank = {}
    for i in range(len(players)):
        rank[players[i]] = i
    rankIdx = {v:k for k,v in rank.items()}
    
    for i in callings:
        p1_idx = rank[i]
        p2_idx = p1_idx - 1
        p2 = rankIdx[p2_idx]
        
        rank[i] = p2_idx
        rank[p2] = p1_idx
        rankIdx[p2_idx] = i
        rankIdx[p1_idx] = p2
        
    rank = sorted(rank.items(), key=lambda x:x[1])
    answer = []
    for k,v in rank:
        answer.append(k)
    return answer
        
    