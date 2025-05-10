import math
def solution(n, stations, w):
    answer = 0
    now = 1
    
    for i in stations:
        answer += math.ceil(((i - w) - now) / (2 * w + 1))
        now = i + w + 1
    
    answer += math.ceil(((n+1) - now) / (2 * w + 1))
    return answer