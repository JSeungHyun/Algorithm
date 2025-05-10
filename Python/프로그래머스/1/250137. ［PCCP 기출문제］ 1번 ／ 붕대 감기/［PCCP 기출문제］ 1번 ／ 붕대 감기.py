def solution(bandage, health, attacks):
    answer = health
    cont = 0 # 연속 성공 수
    t, x, y = bandage
    games = attacks[-1][0]
    attackTime, damage = attacks.pop(0)
    
    for i in range(1, games + 1):
        if i == attackTime: # 현재 시간과 공격 시간이 같을 때
            cont = 0
            answer -= damage
            if answer < 0:
                return -1
            if len(attacks) > 0:
                attackTime, damage = attacks.pop(0)
        else:        
            cont += 1
            if cont == t:
                answer += y
                cont = 0

            answer = answer + x if answer + x <= health else health
        
    return answer if answer > 0 else -1