def solution(n):
    if n % 2 == 1:
        return 0
    else:
        dp = [0] * (n+1)
        dp[2] = 3
        dp[4] = 11
        for i in range(6,n+1,2):
            dp[i] = ((dp[i-2] * 4) - dp[i-4]) % 1000000007
        return dp[n]

'''
1 - 0
2 - 3
3 - 0
4 - 11
5 - 0
6 - 41
7 - 0
8 - 153
'''