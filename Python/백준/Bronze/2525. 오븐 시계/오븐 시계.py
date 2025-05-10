import sys
input = sys.stdin.readline

h,m = map(int,input().split())
c = int(input())

m += c
if m >= 60:
    h += m // 60
    m %= 60
h %= 24

print(h,m)