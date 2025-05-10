import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
res = [0,0]

def quest(x,y,n):
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j]:
                quest(x,y,n//2)
                quest(x+n//2,y,n//2)
                quest(x,y+n//2,n//2)
                quest(x+n//2,y+n//2,n//2)
                return
    res[color] += 1

quest(0,0,N)
print(res[0])
print(res[1])