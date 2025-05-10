import sys
input = sys.stdin.readline


for _ in range(int(input())):
    s1, s2 = input().upper().split()
    print(s2[s1.find('X')], end='')