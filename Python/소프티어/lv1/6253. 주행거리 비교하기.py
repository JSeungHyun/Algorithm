import sys
input = sys.stdin.readline

a, b = map(int, input().split())

print('A' if a > b else 'B' if b > a else 'same')