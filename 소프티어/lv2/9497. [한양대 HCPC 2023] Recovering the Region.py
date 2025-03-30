import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(6)]

for i in range(1, N+1):
    print((str(i) + " ") * N)
    

            
