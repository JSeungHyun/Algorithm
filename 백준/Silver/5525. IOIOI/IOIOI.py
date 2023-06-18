import sys
input = sys.stdin.readline

res = 0
n = int(input())
m = int(input())
s = input().rstrip()
k = 'I' + 'OI' * n
for i in range(m - (2 * n)):
    if s[i : (i + 2 * n) + 1] == k:
        res += 1
        i += 3

print(res)
