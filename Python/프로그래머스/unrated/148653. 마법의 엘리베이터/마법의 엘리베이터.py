def solution(storey):
    answer = 0
    while storey:
        e = storey % 10
        if e > 5:
            answer += 10 - e
            storey //= 10
            storey += 1
        elif e < 5:
            answer += e
            storey //= 10
        else:
            if storey > 10 and (storey//10) % 10 > 4:
                answer += 10 - e
                storey //= 10
                storey += 1
            else:                    
                answer += e
                storey //= 10
            
    return answer