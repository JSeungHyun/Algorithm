import sys
input = sys.stdin.readline
from itertools import product

F = list(map(int, input().split()))
result = 0

def getProbability(a, b, type):
    if type == 'w': # 승
        return (4 * a) / (5 * (a+b))
    elif type == 'l': # 패
        return (4 * b) / (5 * (a + b))
    else: # 무
        # return (a + b) / (5 * (a + b))
        return 1 / 5

def getScore(type):
    if type == 'w':
        return (3, 0)
    elif type == 'l':
        return (0, 3)
    else:
        return (1, 1)

for p in product(['w', 'd', 'l'], repeat=6):
    # 6개는 순서대로 (1,2) (1,3) (1,4) (2,3) (2,4) (3,4) 의 경기 결과라고 가정
    win_score = {0: 0, 1: 0, 2: 0, 3: 0} # 승점

    r1 = p[0] # 1번과 2번 승부의 결과
    a, b = getScore(r1)
    win_score[0] += a
    win_score[1] += b

    r2 = p[1] # 1번과 3번 승부의 결과
    a, b = getScore(r2)
    win_score[0] += a
    win_score[2] += b

    r3 = p[2] # 1번과 4번 승부의 결과
    a, b = getScore(r3)
    win_score[0] += a
    win_score[3] += b

    r4 = p[3] # 2번과 3번 승부의 결과
    a, b = getScore(r4)
    win_score[1] += a
    win_score[2] += b

    r5 = p[4] # 2번과 4번 승부의 결과
    a, b = getScore(r5)
    win_score[1] += a
    win_score[3] += b

    r6 = p[5] # 3번과 4번 승부의 결과
    a, b = getScore(r6)
    win_score[2] += a
    win_score[3] += b

    # 1번 선수가 2등 안에 드는지 확인
    top_win_score = sorted(win_score.items(), key=lambda x:(-x[1], x[0]))
    top_2_keys = [key for key, value in top_win_score[:2]]
    # 들면 result 에 확률 더하기
    if 0 in top_2_keys:
        win_probability = 1
        win_probability *= getProbability(F[0], F[1], r1)
        win_probability *= getProbability(F[0], F[2], r2)
        win_probability *= getProbability(F[0], F[3], r3)
        win_probability *= getProbability(F[1], F[2], r4)
        win_probability *= getProbability(F[1], F[3], r5)
        win_probability *= getProbability(F[2], F[3], r6)


        result += (win_probability * 100)

print("{:.3f}".format(result))