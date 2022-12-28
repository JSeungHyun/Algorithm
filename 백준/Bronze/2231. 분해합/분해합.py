import sys
input = sys.stdin.readline

N = int(input())
for i in range(1,N+1):
    li = list(map(int,str(i))) # 자리마다 구분
    eq = i + sum(li) # 숫자와 자리수의 합
    if eq == N: # 목표값과 같다면 출력
        print(i)
        break
else: # 출력하지 못했다면 0 출력
    print(0)

    