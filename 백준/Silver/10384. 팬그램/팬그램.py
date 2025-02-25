import string
import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    alphabet_dict = dict.fromkeys(string.ascii_lowercase, 0)
    sentence = input().rstrip()
    for s in sentence:
        if s.isalpha():
            alphabet_dict[s.lower()] += 1

    minValue = min(alphabet_dict.values())    
    print(f"Case {i}:", end=' ')
    if minValue == 0:
        print("Not a pangram")
    elif minValue == 1:
        print("Pangram!")
    elif minValue == 2:
        print("Double pangram!!")
    elif minValue == 3:
        print("Triple pangram!!!")

