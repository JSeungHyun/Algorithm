def solution(friends, gifts):
    giftMap = {}
    giftScoreMap = {}
    resMap = {}
    
    # map 초기화
    for F1 in friends:
        innerGiftMap = {}
        for F2 in friends:
            if F1 == F2:
                continue
            innerGiftMap[F2] = 0
        giftMap[F1] = innerGiftMap
        giftScoreMap[F1] = 0
        resMap[F1] = 0
    
    # 선물지수 저장 및 선물 기록
    for gift in gifts:
        giver, receiver = gift.split()
        giftScoreMap[giver] += 1
        giftScoreMap[receiver] -= 1
        giftMap[giver][receiver] += 1
    
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            F1 = friends[i]
            F2 = friends[j]
            
            if giftMap[F1][F2] > giftMap[F2][F1]: # F1 친구가 준 선물이 많은 경우
                resMap[F1] += 1
            elif giftMap[F1][F2] < giftMap[F2][F1]: # F2 친구가 준 선물이 많은 경우
                resMap[F2] += 1
            else: # 준 선물이 같은 경우
                if giftScoreMap[F1] > giftScoreMap[F2]:
                    resMap[F1] += 1
                elif giftScoreMap[F1] < giftScoreMap[F2]:
                    resMap[F2] += 1
                    
        
    return max(resMap.values())
    
            
    
            