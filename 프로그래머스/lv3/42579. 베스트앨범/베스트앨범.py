def solution(genres, plays):
    answer = []
    genre = {} # 장르별 총 플레이 수
    play = {} # 장르별 횟수와 인덱스 저장
    
    for i in range(len(genres)):
        if genres[i] not in genre:
            genre[genres[i]] = plays[i]
            play[genres[i]] = [[plays[i],i]]
        else:
            genre[genres[i]] += plays[i]
            play[genres[i]].append([plays[i],i])
    
    for k,v in sorted(genre.items(),key=lambda x:-x[1]):
        for i in sorted(play[k],key=lambda x:(-x[0],x[1]))[:2]:
            answer.append(i[1])
    return answer