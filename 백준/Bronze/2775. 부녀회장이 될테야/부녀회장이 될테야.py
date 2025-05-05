import sys
input = sys.stdin.readline

dp = [[i for i in range(15)]]

for i in range(1, 15):
    temp = [0]
    for j in range(1, 15):
        temp.append(sum(dp[i-1][:j+1]))
    dp.append(temp)

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(dp[k][n])
