import sys
def solution(x, y, n):
    answer = 0
    dp = [sys.maxsize] * (y+1)
    dp[x] = 0
    for i in range(x+1,y+1):
        if i/2 == i//2:
            dp[i] = min(dp[i],dp[i//2]+1)
        if i/3 == i//3:
            dp[i] = min(dp[i],dp[i//3]+1)
        if 0 < i-n <= y-x:
            dp[i] = min(dp[i],dp[i-n]+1)
    
    if dp[y] == sys.maxsize:
        return -1
    else:
        return dp[y]