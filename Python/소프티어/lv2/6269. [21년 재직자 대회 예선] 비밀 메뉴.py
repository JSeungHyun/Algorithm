import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
hidden = input().rstrip().replace(' ', '')
menu = input().rstrip().replace(' ', '')

print('secret' if hidden in menu else 'normal')