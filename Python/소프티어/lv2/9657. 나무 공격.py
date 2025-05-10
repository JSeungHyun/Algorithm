import sys
input = sys.stdin.readline

y, x = map(int, input().split())
dict = []

for i in range(y):
    wreckers = list(map(int, input().split()))
    dict.append(sum(wreckers))

for _ in range(2):
    s, e = map(int, input().split())
    
    for i in range(s, e + 1):
        if  dict[i-1] > 0:
            dict[i-1] -= 1

print(sum(dict))