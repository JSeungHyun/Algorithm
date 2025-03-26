import sys
input = sys.stdin.readline

total = 0
for _ in range(5):
    s, e = input().split()
    startTime = list(map(int, s.split(':')))
    endTime = list(map(int, e.split(':')))
    total += (endTime[0] * 60 + endTime[1]) - (startTime[0] * 60 + startTime[1])

print(total)