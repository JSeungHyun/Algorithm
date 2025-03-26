import sys
input = sys.stdin.readline

n = int(input())
viliage = list(map(int, input().split()))
dict = {}

for i in range(n-1):
    dist = abs(viliage[i] - viliage[i + 1])
    dict[dist] = dict.get(dist, 0) + 1

print(dict[min(dict.keys())])