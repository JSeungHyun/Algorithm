def solution(targets):
    answer = 1
    targets.sort(key=lambda x:(x[1],x[0]))
    cur = targets[0]
    
    for i in range(1, len(targets)):
        if targets[i][0] >= cur[1]:
            cur = targets[i]
            answer += 1
            
    return answer