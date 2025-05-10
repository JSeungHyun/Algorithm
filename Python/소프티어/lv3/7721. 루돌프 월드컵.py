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
    rounds = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    win_score = {0: 0, 1: 0, 2: 0, 3: 0} # 승점
    win_probability = 1

    for idx, (a, b) in enumerate(rounds):
        round_result = p[idx]
        r1, r2 = getScore(round_result)
        win_score[a] += r1
        win_score[b] += r2
        win_probability *= getProbability(F[a], F[b], round_result)

    # 1번 선수가 2등 안에 드는지 확인
    top_win_score = sorted(win_score.items(), key=lambda x:(-x[1], x[0]))
    top_2_keys = [key for key, value in top_win_score[:2]]
    # 들면 result 에 확률 더하기
    if 0 in top_2_keys:
        result += (win_probability * 100)

print("{:.3f}".format(result))