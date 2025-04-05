import sys
input = sys.stdin.readline
from itertools import permutations

N, M, K = map(int, input().split())
mix = list(permutations(list(map(int, input().split())), N))
result = sys.maxsize

for i in range(len(mix)):
    idx = 0 # 현재 담을 박스 위치
    cnt = 0 # 일의 진행 수
    boxes = mix[i]
    weight = 0 # 이 순서로 진행했을때의 무게
    temp = 0
    while cnt < K:
        temp += boxes[idx % N]
        idx += 1
        if temp + boxes[(idx) % N] > M: # 다음 택배를 담을 수 없으면
            weight += temp
            temp = 0
            cnt += 1

            if weight > result:
                weight = sys.maxsize
                cnt = sys.maxsize

    result = min(result, weight)


print(result)
