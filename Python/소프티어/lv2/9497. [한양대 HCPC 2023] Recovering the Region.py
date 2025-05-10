import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(6)]

for i in range(N):
    print(' '.join(map(str, [i + 1] * N)))


            
