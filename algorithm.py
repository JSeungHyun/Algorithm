import sys
input = sys.stdin.readline
from collections import deque

# n: 트럭의 수, w: 다리 길이, L: 최대하중
n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque([0] * w)
result = 0

while trucks:
    result += 1
    bridge.popleft()
    if sum(bridge) + trucks[0] > L:
        bridge.append(0)
        continue
    bridge.append(trucks.popleft())

print(result + len(bridge))



