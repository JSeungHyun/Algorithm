import sys
input = sys.stdin.readline

for idx in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    print(f'Case #{idx}: {a+b}')