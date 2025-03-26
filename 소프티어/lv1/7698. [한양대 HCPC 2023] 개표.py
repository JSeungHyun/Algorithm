import sys
input = sys.stdin.readline

for _ in range(int(input())):
    vote = int(input())
    print('++++ ' * (vote // 5) + '|' * (vote % 5))