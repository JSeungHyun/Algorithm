def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 집만 있고 배달 혹은 수거할것이 없으면 pop
    while deliveries and deliveries[-1] == 0:
        deliveries.pop()
    while pickups and pickups[-1] == 0:
        pickups.pop()
    
    while deliveries or pickups:
        answer += max(len(deliveries),len(pickups)) * 2 #무조건 왕복, 제일 먼 집으로
        
        box = 0
        while deliveries and box <= cap:
            if deliveries[-1] + box <= cap: # 가장 먼 집의 택배를 모두 줄 때
                box += deliveries[-1]
                deliveries.pop()
            else: # 일부만 줄 수 있을 때
                deliveries[-1] -= cap - box
                break
        
        box = 0
        while pickups and box <= cap:
            if pickups[-1] + box <= cap: # 가장 먼 집의 택배를 모두 실을 때
                box += pickups[-1]
                pickups.pop()
            else: # 일부만 실을 때
                pickups[-1] -= cap - box
                break
                
    return answer
