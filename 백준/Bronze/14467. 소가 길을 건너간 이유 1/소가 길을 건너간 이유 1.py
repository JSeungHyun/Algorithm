import sys
input = sys.stdin.readline

N = int(input())
cows = {}
result = 0

for _ in range(N):
    c, l = map(int, input().split())
    if c not in cows:
        cows[c] = l
    elif cows[c] != l:
        cows[c] = l
        result += 1

print(result)