import sys
input = sys.stdin.readline

word = list(input().rstrip())
idx = 0

while idx < len(word):
    if word[idx] == '<':
        idx += 1
        while word[idx] != '>':
            idx += 1
        idx += 1
    elif word[idx].isalnum():
        s = idx
        while idx < len(word) and word[idx].isalnum():
            idx += 1
        tmp = word[s:idx]
        word[s:idx] = reversed(tmp)
    else:
        idx += 1

print(''.join(word))