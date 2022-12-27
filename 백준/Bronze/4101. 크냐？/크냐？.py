import sys
input = sys.stdin.readline

while True:
    n1,n2 = map(int,input().split())
    if n1 == 0 and n2 ==0:
        break
    if n1 > n2:
        print("Yes")
    else:
        print("No")
    