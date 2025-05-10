def solution(topping):
    answer = 0
    soo = {} # 철수의 빵들
    bro = {} # 동생의 빵들
    # 모든 빵을 철수가 가지고 시작
    for i in topping:
        if i in soo:
            soo[i] += 1
        else:
            soo[i] = 1
    
    for i in topping:
        soo[i] -= 1
        if i in bro:
            bro[i] += 1
        else:
            bro[i] = 1
        if soo[i] == 0:
            del soo[i]
        if len(soo) == len(bro):
            answer += 1
        
    
    
    return answer