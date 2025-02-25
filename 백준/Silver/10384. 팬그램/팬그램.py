import string
import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    alphabet_count = [0] * 26
    sentence = input().rstrip()
    for s in sentence:
        if s.isalpha():
            alphabet_count[ord(s.lower()) - ord('a')] += 1

    minValue = min(alphabet_count)
    print(f"Case {i}:", end=' ')
    if minValue == 0:
        print("Not a pangram")
    elif minValue == 1:
        print("Pangram!")
    elif minValue == 2:
        print("Double pangram!!")
    elif minValue == 3:
        print("Triple pangram!!!")

