import sys
input = sys.stdin.readline

N = int(input())
work = []

for _ in range(N):
    T, S = map(int, input().split())
    work.append([S, T])

work.sort()
cur = work[-1][0]

while work:
    deadline, time = work.pop()
    if cur > deadline:
        cur = deadline
    cur -= time

print(cur) if cur > 0 else print(-1)
