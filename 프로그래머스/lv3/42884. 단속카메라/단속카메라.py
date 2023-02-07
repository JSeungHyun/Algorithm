def solution(routes):
    answer = 1
    routes.sort(key=lambda x:(x[1],x[0]))
    std = routes[0][1]
    
    for i in range(1,len(routes)):
        if routes[i][0] > std:
            answer += 1
            std = routes[i][1]
    
    return answer