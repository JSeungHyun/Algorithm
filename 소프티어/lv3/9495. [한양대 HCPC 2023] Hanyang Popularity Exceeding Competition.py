import sys
input = sys.stdin.readline

X = 0

for _ in range(int(input())):
    p, c = map(int, input().split())
    if -c <= abs(X - p) <= c:
        X += 1

print(X)