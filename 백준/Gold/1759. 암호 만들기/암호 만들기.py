import sys
input = sys.stdin.readline

L,C =  map(int,input().split())
words = sorted((input().rstrip().split()))

def dfs(word,idx):
    word += words[idx]
    if len(word) == L:
        vowl,cons = 0,0
        for i in word:
            if i in ['a','e','i','o','u']:
                vowl += 1
            else:
                cons += 1
        if vowl >= 1 and cons >= 2:
            print(''.join(word))
        return
    for i in range(idx+1,C):
        dfs(word,i)
    
for x in range(C-L+1):
    dfs('',x)    
