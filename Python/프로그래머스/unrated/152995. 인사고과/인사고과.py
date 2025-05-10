def solution(scores):
    wonScoreA = scores[0][0]
    wonScoreB = scores[0][1]
    wonScore = wonScoreA + wonScoreB # 원호 점수
    scores.sort(key=lambda x: (-x[0], x[1]))
    std, answer = 0, 1
    for a,b in scores:
        if wonScoreA < a and wonScoreB < b:
            return -1
        if std <= b:
            if wonScore < a+b:
                answer += 1
            std = b
    return answer