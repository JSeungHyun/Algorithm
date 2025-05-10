import sys
input = sys.stdin.readline

for _ in range(int(input())):
    li = input().rstrip().split()
    for i in li:
        for j in reversed(i):
            print(j,end='')
        print(' ',end='')
    print()
