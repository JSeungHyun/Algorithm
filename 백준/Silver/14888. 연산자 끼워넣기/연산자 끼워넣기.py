import sys
input = sys.stdin.readline


resMin = sys.maxsize
resMax = -sys.maxsize

N = int(input())
nums = list(map(int,input().split()))
op = list(map(int,input().split()))

def dfs(depth,total,pl,mi,mu,de):
    global resMax,resMin
    if depth == N:
        resMax = max(resMax,total)
        resMin = min(resMin,total)
        return
    if pl:
        dfs(depth+1,total + nums[depth],pl-1,mi,mu,de)
    if mi:
        dfs(depth+1,total - nums[depth],pl,mi-1,mu,de)
    if mu:
        dfs(depth+1,total * nums[depth],pl,mi,mu-1,de)
    if de:
        dfs(depth+1, int(total / nums[depth]),pl,mi,mu,de-1)
        
dfs(1,nums[0],op[0],op[1],op[2],op[3])
print(resMax)
print(resMin)        