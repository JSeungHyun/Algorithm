def solution(picks, minerals):
    answer = 0
    minerals = minerals[:sum(picks) * 5] # 곡괭이의 수 * 5 만큼의 광물만 꺼내기
    mineral = [minerals[i:i+5] for i in range(0,len(minerals),5)] # 5개씩 묶음
    # 다이아몬드가 많은 순, 같다면 철, 나머지 돌 순으로 정렬
    mineral.sort(key=lambda x:(-x.count("diamond"), -x.count("iron"), -x.count("stone")))
    
    for i in mineral:
        if picks[0] > 0:
            picks[0] -= 1
            answer += len(i)
        elif picks[1] > 0:
            picks[1] -= 1
            for j in i:
                if j == "diamond":
                    answer += 5
                else:
                    answer += 1
        else:
            picks[2] -= 1
            for j in i:
                if j == "diamond":
                    answer += 25
                elif j == "iron":
                    answer += 5
                else:
                    answer += 1
                    
    return answer