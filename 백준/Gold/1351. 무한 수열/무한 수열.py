import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, P, Q = map(int, input().split())
dp = {}
dp[0] = 1

def getDpValue(v):
    global dp
    if v in dp:
        return dp[v]
    else:
        dp[v] = getDpValue(v // P) + getDpValue(v // Q)
        return dp[v]

print(getDpValue(N))