import sys
input = sys.stdin.readline


parenthheses = input().rstrip()
stack = []
openPar = 1
res = 0

for i in range(len(parenthheses)):
    if parenthheses[i] == '(':
        stack.append('(')
        openPar *= 2
    elif parenthheses[i] == '[':
        stack.append('[')
        openPar *= 3
    elif parenthheses[i] == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if parenthheses[i-1] == '(':
            res += openPar
        stack.pop()
        openPar //= 2
    elif parenthheses[i] == ']':
        if not stack or stack[-1] == '(':
            res = 0
            break
        if parenthheses[i-1] == '[':
            res += openPar
        stack.pop()
        openPar //= 3

print(0 if stack else res)
    
