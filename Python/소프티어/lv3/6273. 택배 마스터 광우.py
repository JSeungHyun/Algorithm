import sys
from itertools import permutations

input = sys.stdin.readline

N, M, K = map(int, input().split())
boxes = list(map(int, input().split()))
result = sys.maxsize

for perm in permutations(boxes):
    weight = 0  # 총 무게
    temp = 0    # 현재 박스에 담긴 무게
    idx = 0     # 담을 박스 index

    for i in range(K):  # K번 작업 수행
        while temp + perm[idx % N] <= M:  # 현재 박스에 담을 수 있을 때까지 반복
            temp += perm[idx % N]
            idx += 1
        
        weight += temp  # 현재 박스의 무게를 추가
        temp = 0        # 새로운 박스를 시작
    
        if weight >= result:  # 이미 최소값보다 크면 중단
            break

    result = min(result, weight)  # 최소값 갱신

print(result)